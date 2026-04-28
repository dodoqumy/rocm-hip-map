#!/usr/bin/env python3
"""
fetch-eu.py — 多语言情报抓取脚本（欧洲核心）

扫描 config/sources.yaml 中的多语言源，抓取一手情报并保存为 Markdown。

用法：
  python3 scripts/fetch-eu.py                     # 全部源
  python3 scripts/fetch-eu.py --source csc-lumi   # 单个源
  python3 scripts/fetch-eu.py --region eu          # 按区域
  python3 scripts/fetch-eu.py --limit 3            # 每个源最多 N 篇
  python3 scripts/fetch-eu.py --dry-run            # 预览
"""
import argparse
import json
import os
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
DATA_DIR = PROJECT_ROOT / "data"

# ── 请求配置 ────────────────────────────────────────
HEADERS = {
    "User-Agent": "rocm-hip-map/1.0 (research; multilingual fetcher; +https://github.com/dodoqumy/rocm-hip-map)",
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


def load_sources(region: str = None, source_id: str = None) -> list:
    """加载源配置。"""
    with open(SOURCES_YAML) as f:
        data = yaml.safe_load(f)

    sources = data.get("sources", [])
    if source_id:
        sources = [s for s in sources if s["id"] == source_id]
    if region:
        sources = [s for s in sources if s.get("region") == region]

    return sources


def slugify(text: str, max_len: int = 64) -> str:
    """生成 URL 安全的 slug。"""
    slug = re.sub(r"[^a-zA-Z0-9_-]", "-", text.lower())
    slug = re.sub(r"-{2,}", "-", slug).strip("-")
    return slug[:max_len]


def fetch_url(url: str) -> tuple[str, int]:
    """抓取单个 URL，返回 (文本内容, 状态码)。"""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        return resp.text, resp.status_code
    except requests.RequestException as e:
        return "", getattr(e.response, "status_code", 0) if hasattr(e, "response") else 0


def extract_text(html: str) -> str:
    """从 HTML 中提取可读文本（简单提取，避免依赖 BeautifulSoup）。"""
    # 去掉 script/style
    html = re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r"<style[^>]*>.*?</style>", "", html, flags=re.DOTALL | re.IGNORECASE)

    # 去掉 HTML 标签
    text = re.sub(r"<[^>]+>", " ", html)

    # 解码 HTML 实体
    text = text.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    text = text.replace("&quot;", '"').replace("&#39;", "'").replace("&nbsp;", " ")

    # 合并空格和空行
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = text.strip()

    return text


def detect_language(text: str) -> str:
    """基于字符范围简单检测语言。"""
    # 日文特征
    if re.search(r"[\u3040-\u309f\u30a0-\u30ff]", text):
        return "ja"
    # 韩文特征
    if re.search(r"[\uac00-\ud7af]", text):
        return "ko"
    # 中文特征
    if re.search(r"[\u4e00-\u9fff]", text):
        return "zh"
    # 西里尔（俄语）
    if re.search(r"[\u0400-\u04ff]", text):
        return "ru"
    # 默认英文
    return "en"


def search_web(query: str, limit: int = 5) -> list:
    """使用 DuckDuckGo 搜索（无 API key 方案）。"""
    # 使用 DDG HTML 搜索
    results = []
    try:
        url = f"https://html.duckduckgo.com/html/?q={requests.utils.quote(query)}"
        resp = requests.get(url, headers=HEADERS, timeout=15)
        if resp.status_code == 200:
            # 提取结果链接
            for m in re.finditer(
                r'<a[^>]*class="result__a"[^>]*href="([^"]+)"[^>]*>(.*?)</a>',
                resp.text,
                re.DOTALL,
            ):
                href = m.group(1)
                title = re.sub(r"<[^>]+>", "", m.group(2)).strip()
                if href and not href.startswith("//duckduckgo.com"):
                    results.append({"url": href, "title": title})
    except Exception:
        pass

    return results[:limit]


def save_article(source: dict, url: str, title: str, text: str, lang: str) -> Path:
    """保存文章到 content/raw/multilingual/{lang}/。"""
    out_dir = CONTENT_RAW_ML / lang
    out_dir.mkdir(parents=True, exist_ok=True)

    slug = slugify(title) or urlparse(url).path.strip("/").replace("/", "-")[:64]
    if not slug:
        slug = f"article-{hash(url) % 10000}"

    filepath = out_dir / f"{source['id']}_{slug}.md"

    # Frontmatter
    fm = f"""---
title: \"{title}\"
source_url: \"{url}\"
source_type: \"multilingual\"
source_org: \"{source['id']}\"
source_name: \"{source['name']}\"
original_lang: \"{lang}\"
credibility: {source.get('credibility', 3)}
lifecycle: \"latest\"
synced_date: {datetime.now(timezone.utc).strftime('%Y-%m-%d')}
region: \"{source.get('region', 'unknown')}\"
country: \"{source.get('country', 'unknown')}\"
---

{text[:50000]}  <!-- 截断至 50K 字符 -->
"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(fm)

    return filepath


def process_source(source: dict, limit: int = 5, dry_run: bool = False) -> int:
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

        html, status = fetch_url(url)
        if status == 200 and html:
            text = extract_text(html)
            if len(text) > 200:  # 最少 200 字符才算有效
                detected = detect_language(text) or lang
                title = source["name"] + " — " + urlparse(url).path.strip("/").split("/")[-1]
                path = save_article(source, url, title, text, detected)
                print(f"    ✅ {path.name} ({len(text)} chars, lang={detected})")
                saved += 1
        else:
            print(f"    ❌ HTTP {status}")

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

        results = search_web(query, limit=2)
        for r in results:
            if saved >= limit:
                break
            url = r["url"]
            title = r.get("title", url)
            print(f"    ↓ {url[:80]}")

            html, status = fetch_url(url)
            if status == 200 and html:
                text = extract_text(html)
                if len(text) > 200:
                    detected = detect_language(text) or lang
                    path = save_article(source, url, title, text, detected)
                    print(f"      ✅ {path.name} ({len(text)} chars, lang={detected})")
                    saved += 1
            else:
                print(f"      ❌ HTTP {status}")

            time.sleep(REQUEST_DELAY)

    return saved


def main():
    parser = argparse.ArgumentParser(description="多语言情报抓取 — 欧洲核心")
    parser.add_argument("--source", help="单个源 ID")
    parser.add_argument("--region", choices=["eu", "asia"], help="按区域")
    parser.add_argument("--limit", type=int, default=5, help="每个源最多 N 篇")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    print("🌐 rocm-hip-map fetch-eu.py")
    print(f"   {'DRY RUN' if args.dry_run else 'LIVE MODE'}")

    sources = load_sources(region=args.region, source_id=args.source)
    print(f"   Loaded {len(sources)} sources")

    total = 0
    for src in sources:
        count = process_source(src, limit=args.limit, dry_run=args.dry_run)
        total += count
        print(f"   ↳ {count} articles from {src['id']}")

    print(f"\n📊 Total: {total} articles from {len(sources)} sources")
    if not args.dry_run and total > 0:
        print(f"   Output: {CONTENT_RAW_ML}/")


if __name__ == "__main__":
    main()
