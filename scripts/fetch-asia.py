#!/usr/bin/env python3
"""
fetch-asia.py — 亚洲多语言情报抓取（日本/韩国）

扫描 config/sources.yaml 中的亚洲源，抓取一手情报并保存为 Markdown。
在 DuckDuckGo 基础上增加 CiNii (日本) / KISTI (韩国) 专用搜索后端。

用法：
  python3 scripts/fetch-asia.py                     # 全部亚洲源
  python3 scripts/fetch-asia.py --source titech-tsubame  # 单个源
  python3 scripts/fetch-asia.py --country jp         # 按国家
  python3 scripts/fetch-asia.py --limit 3            # 每个源最多 N 篇
  python3 scripts/fetch-asia.py --dry-run            # 预览
"""

import argparse
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

import requests
import yaml

# ── 项目路径 ────────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent.parent
SOURCES_YAML = PROJECT_ROOT / "config" / "sources.yaml"
CONTENT_RAW_ML = PROJECT_ROOT / "content" / "raw" / "multilingual"

# ── 请求配置 ────────────────────────────────────────
HEADERS = {
    "User-Agent": (
        "rocm-hip-map/1.0 (research; multilingual fetcher; "
        "+https://github.com/dodoqumy/rocm-hip-map)"
    ),
}
REQUEST_DELAY = 5  # 秒（礼貌策略）
REQUEST_TIMEOUT = 30

# ── 语言代码 → 语言名 ──────────────────────────────
LANG_NAMES = {
    "fi": "Finnish", "fr": "French", "de": "German",
    "it": "Italian", "ja": "Japanese", "ko": "Korean",
    "es": "Spanish", "nl": "Dutch", "pt": "Portuguese",
    "ru": "Russian", "sv": "Swedish", "en": "English",
    "zh": "Chinese",
}


# ═══════════════════════════════════════════════════════
#  辅助函数（与 fetch-eu.py 共享）
# ═══════════════════════════════════════════════════════

def load_sources(region: str = None, country: str = None,
                 source_id: str = None) -> list:
    """加载源配置。"""
    with open(SOURCES_YAML) as f:
        data = yaml.safe_load(f)

    sources = data.get("sources", [])
    if source_id:
        sources = [s for s in sources if s["id"] == source_id]
    if region:
        sources = [s for s in sources if s.get("region") == region]
    if country:
        sources = [s for s in sources if s.get("country") == country]

    return sources


def slugify(text: str, max_len: int = 64) -> str:
    """生成 URL 安全的 slug。"""
    slug = re.sub(r"[^a-zA-Z0-9_-]", "-", text.lower())
    slug = re.sub(r"-{2,}", "-", slug).strip("-")
    return slug[:max_len]


def fetch_url(url: str) -> tuple[str, int, str]:
    """抓取单个 URL，返回 (文本内容, 状态码, 错误信息)。"""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        return resp.text, resp.status_code, ""
    except requests.Timeout:
        return "", 0, "timeout"
    except requests.ConnectionError as e:
        return "", 0, f"connection: {e}"
    except requests.HTTPError as e:
        code = e.response.status_code if e.response is not None else 0
        return "", code, f"HTTP {code}"
    except requests.RequestException as e:
        return "", 0, f"{type(e).__name__}"


def extract_text(html: str) -> str:
    """从 HTML 中提取可读文本（简单提取）。"""
    # 去掉 script/style
    html = re.sub(
        r"<script[^>]*>.*?</script>", "", html, flags=re.DOTALL | re.IGNORECASE
    )
    html = re.sub(
        r"<style[^>]*>.*?</style>", "", html, flags=re.DOTALL | re.IGNORECASE
    )

    # 去掉 HTML 标签
    text = re.sub(r"<[^>]+>", " ", html)

    # 解码 HTML 实体
    text = (text.replace("&amp;", "&").replace("&lt;", "<")
                .replace("&gt;", ">").replace("&quot;", '"')
                .replace("&#39;", "'").replace("&nbsp;", " "))

    # 合并空格和空行
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def detect_language(text: str) -> str:
    """基于字符范围检测语言（日/韩优先）。"""
    # 日文（平假名/片假名）
    if re.search(r"[\u3040-\u309f\u30a0-\u30ff]", text):
        return "ja"
    # 韩文
    if re.search(r"[\uac00-\ud7af]", text):
        return "ko"
    # 中文
    if re.search(r"[\u4e00-\u9fff]", text):
        return "zh"
    # 西里尔（俄语）
    if re.search(r"[\u0400-\u04ff]", text):
        return "ru"
    return "en"


def save_article(source: dict, url: str, title: str,
                 text: str, lang: str) -> Path:
    """保存文章到 content/raw/multilingual/{lang}/。"""
    out_dir = CONTENT_RAW_ML / lang
    out_dir.mkdir(parents=True, exist_ok=True)

    slug = slugify(title) or urlparse(url).path.strip("/").replace("/", "-")[:64]
    if not slug:
        slug = f"article-{hash(url) % 10000}"

    filepath = out_dir / f"{source['id']}_{slug}.md"

    fm = f"""---
title: "{title}"
source_url: "{url}"
source_type: "multilingual"
source_org: "{source['id']}"
source_name: "{source['name']}"
original_lang: "{lang}"
credibility: {source.get('credibility', 3)}
lifecycle: "latest"
synced_date: {datetime.now(timezone.utc).strftime('%Y-%m-%d')}
region: "{source.get('region', 'unknown')}"
country: "{source.get('country', 'unknown')}"
---

{text[:50000]}  <!-- 截断至 50K 字符 -->
"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(fm)

    return filepath


# ═══════════════════════════════════════════════════════
#  日韩专用搜索后端
# ═══════════════════════════════════════════════════════

def search_ddg_jp(query: str, limit: int = 5) -> list:
    """DuckDuckGo 日语优化搜索（区域=日本）。"""
    results = []
    try:
        url = (
            "https://html.duckduckgo.com/html/?"
            f"q={requests.utils.quote(query)}&kl=jp-jp"
        )
        resp = requests.get(url, headers=HEADERS, timeout=15)
        if resp.status_code in (200, 202):
            for m in re.finditer(
                r'<a[^>]*class="result__a"[^>]*href="([^"]+)"[^>]*>(.*?)</a>',
                resp.text,
                re.DOTALL,
            ):
                href = m.group(1)
                title = re.sub(r"<[^>]+>", "", m.group(2)).strip()
                if href and "//duckduckgo.com" not in href:
                    results.append({"url": href, "title": title})
    except Exception:
        pass
    return results[:limit]


def search_ddg_kr(query: str, limit: int = 5) -> list:
    """DuckDuckGo 韩语优化搜索（区域=韩国）。"""
    results = []
    try:
        url = (
            "https://html.duckduckgo.com/html/?"
            f"q={requests.utils.quote(query)}&kl=kr-kr"
        )
        resp = requests.get(url, headers=HEADERS, timeout=15)
        if resp.status_code in (200, 202):
            for m in re.finditer(
                r'<a[^>]*class="result__a"[^>]*href="([^"]+)"[^>]*>(.*?)</a>',
                resp.text,
                re.DOTALL,
            ):
                href = m.group(1)
                title = re.sub(r"<[^>]+>", "", m.group(2)).strip()
                if href and "//duckduckgo.com" not in href:
                    results.append({"url": href, "title": title})
    except Exception:
        pass
    return results[:limit]


def search_cinii(query: str, limit: int = 5) -> list:
    """
    CiNii Articles OpenSearch 检索日本学术论文。

    CiNii API: https://cir.nii.ac.jp/opensearch/
    免费，无需 API key，返回 RSS/Atom 格式的学术论文结果。
    """
    results = []
    try:
        url = (
            "https://cir.nii.ac.jp/opensearch/articles?"
            f"q={requests.utils.quote(query)}&count={limit}&format=rss"
        )
        resp = requests.get(url, headers=HEADERS, timeout=15)
        if resp.status_code == 200:
            # 解析 RSS <item> 条目
            for m in re.finditer(
                r"<item>.*?<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>"
                r".*?<link>(.*?)</link>",
                resp.text,
                re.DOTALL,
            ):
                title = m.group(1).strip()
                link = m.group(2).strip()
                if link:
                    results.append({"url": link, "title": title})
    except Exception:
        pass
    return results[:limit]


def search_riss(query: str, limit: int = 5) -> list:
    """
    RISS International API 检索韩国学术论文。

    免费开放 API，无需 key。
    如果 API 不可用，回退到 DDG 韩语搜索。
    """
    results = []
    try:
        url = (
            "http://www.riss.kr/openapi/SearchApi.do?"
            f"key=free&query={requests.utils.quote(query)}"
            f"&display={limit}&start=1"
        )
        resp = requests.get(url, headers=HEADERS, timeout=15,
                           allow_redirects=True)
        if resp.status_code == 200 and "item" in resp.text.lower():
            for m in re.finditer(
                r"<title>(.*?)</title>.*?<link>(.*?)</link>",
                resp.text,
                re.DOTALL,
            ):
                title = re.sub(r"<[^>]+>", "", m.group(1)).strip()
                link = re.sub(r"<[^>]+>", "", m.group(2)).strip()
                if link:
                    results.append({"url": link, "title": title})
    except Exception:
        pass

    # 如果 RISS API 失败，回退到 DDG 韩语
    if not results:
        results = search_ddg_kr(query, limit)
    return results[:limit]


def search_web(query: str, lang: str = "en", limit: int = 5) -> list:
    """
    多后端搜索调度：
    - ja (日语) → CiNii → DDG Japan 回退
    - ko (韩语) → RISS → DDG Korea 回退
    - 其他     → DDG 通用
    """
    if lang == "ja":
        results = search_cinii(query, limit)
        if not results:
            print("        (CiNii 无结果，回退到 DDG Japan)")
            results = search_ddg_jp(query, limit)
    elif lang == "ko":
        results = search_riss(query, limit)
    else:
        # 通用 DDG
        results = search_ddg_jp(query, limit) if lang in ("ja",) else []
        if not results:
            r = _search_ddg_generic(query, limit)
            results = r
    return results


def _search_ddg_generic(query: str, limit: int = 5) -> list:
    """通用 DDG 搜索。"""
    results = []
    try:
        url = "https://html.duckduckgo.com/html/?" \
              f"q={requests.utils.quote(query)}"
        resp = requests.get(url, headers=HEADERS, timeout=15)
        if resp.status_code in (200, 202):
            for m in re.finditer(
                r'<a[^>]*class="result__a"[^>]*href="([^"]+)"[^>]*>(.*?)</a>',
                resp.text,
                re.DOTALL,
            ):
                href = m.group(1)
                title = re.sub(r"<[^>]+>", "", m.group(2)).strip()
                if href and "//duckduckgo.com" not in href:
                    results.append({"url": href, "title": title})
    except Exception:
        pass
    return results[:limit]


# ═══════════════════════════════════════════════════════
#  主处理逻辑
# ═══════════════════════════════════════════════════════

def process_source(source: dict, limit: int = 5,
                   dry_run: bool = False) -> int:
    """处理单个源。返回抓取文章数。"""
    lang = source.get("language", "en")
    lang_name = LANG_NAMES.get(lang, lang)
    print(f"\n{'='*60}")
    print(f"📡 {source['name']} [{lang_name}] ({source.get('country', '?')})")
    print(f"   Credibility: {'⭐' * source.get('credibility', 3)}")

    saved = 0

    # 1. 先尝试直接 URL
    urls = source.get("urls", [])
    for url in urls:
        if saved >= limit:
            break
        print(f"  🔗 {url[:80]}...")
        if dry_run:
            saved += 1
            continue

        html, status, err = fetch_url(url)
        if status == 200 and html:
            text = extract_text(html)
            if len(text) > 200:
                detected = detect_language(text) or lang
                path_part = urlparse(url).path.strip("/").split("/")[-1]
                title = f"{source['name']} — {path_part}"
                path = save_article(source, url, title, text, detected)
                print(f"    ✅ {path.name} ({len(text)} chars, lang={detected})")
                saved += 1
            else:
                print(f"    ⚠️ 内容太短 ({len(text)} chars)，跳过")
        else:
            err_msg = err or f"HTTP {status}"
            print(f"    ❌ {err_msg}")

        time.sleep(REQUEST_DELAY)

    # 2. 搜索补充
    search_terms = source.get("search_terms", [])
    for query in search_terms:
        if saved >= limit:
            break
        print(f"  🔍 \"{query}\"")
        if dry_run:
            saved += 1
            continue

        results = search_web(query, lang=lang, limit=2)
        for r in results:
            if saved >= limit:
                break
            url = r["url"]
            title = r.get("title", url)
            print(f"    ↓ {url[:80]}")

            html, status, err = fetch_url(url)
            if status == 200 and html:
                text = extract_text(html)
                if len(text) > 200:
                    detected = detect_language(text) or lang
                    path = save_article(source, url, title, text, detected)
                    print(f"      ✅ {path.name} ({len(text)} chars, lang={detected})")
                    saved += 1
                else:
                    print(f"      ⚠️ 内容太短 ({len(text)} chars)")
            else:
                err_msg = err or f"HTTP {status}"
                print(f"      ❌ {err_msg}")

            time.sleep(REQUEST_DELAY)

    return saved


def main():
    parser = argparse.ArgumentParser(
        description="亚洲多语言情报抓取 — 日本/韩国"
    )
    parser.add_argument("--source", help="单个源 ID")
    parser.add_argument("--country", choices=["jp", "kr"], help="按国家")
    parser.add_argument("--limit", type=int, default=5,
                       help="每个源最多 N 篇")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    print("🌏 rocm-hip-map fetch-asia.py")
    print(f"   {'DRY RUN' if args.dry_run else 'LIVE MODE'}")

    # 默认 region=asia，可通过 --country 进一步过滤
    region = None if args.country else "asia"
    sources = load_sources(region=region, country=args.country,
                           source_id=args.source)
    print(f"   Loaded {len(sources)} sources")

    jp_count = sum(1 for s in sources if s.get("country") == "jp")
    kr_count = sum(1 for s in sources if s.get("country") == "kr")
    print(f"   🇯🇵 {jp_count} Japanese  |  🇰🇷 {kr_count} Korean")

    total = 0
    for src in sources:
        count = process_source(src, limit=args.limit, dry_run=args.dry_run)
        total += count
        flag = "🇯🇵" if src.get("country") == "jp" else "🇰🇷"
        print(f"   {flag} {count} articles from {src['id']}")

    print(f"\n📊 Total: {total} articles from {len(sources)} sources")
    if not args.dry_run and total > 0:
        print(f"   Output: {CONTENT_RAW_ML}/")


if __name__ == "__main__":
    main()
