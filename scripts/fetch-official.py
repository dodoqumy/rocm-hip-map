#!/usr/bin/env python3
"""fetch-official.py — 从多源抓取 ROCm/HIP 官方一手文档。

支持来源（按 README §一手来源定义）：
  - AMD ROCm Official Docs (rocm.docs.amd.com)
  - AMD ROCm Blog RSS
  - PyTorch ROCm docs
  - TensorFlow ROCm docs
  - ROCm GitHub org README/docs
  - HIP GitHub docs

输出：
  - content/raw/english/*.md     原始英文文章
  - content/raw/chinese/*.md    原始中文文章
  - data/articles.json          文章索引（增量更新）
  - data/fetch-state.json      抓取状态（增量更新）

用法：
  python3 scripts/fetch-official.py              # 全量同步
  python3 scripts/fetch-official.py --dry-run     # 预览
  python3 scripts/fetch-official.py --source rocm # 仅指定源
  python3 scripts/fetch-official.py --auto-discover  # 从 sitemap 自动发现
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional, Set
from urllib.parse import urljoin, urlparse
import xml.etree.ElementTree as ET

# ── 项目根目录 ──────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONTENT_RAW_EN = PROJECT_ROOT / "content" / "raw" / "english"
CONTENT_RAW_ZH = PROJECT_ROOT / "content" / "raw" / "chinese"
DATA_DIR = PROJECT_ROOT / "data"
ARTICLES_JSON = DATA_DIR / "articles.json"
FETCH_STATE_JSON = DATA_DIR / "fetch-state.json"

# ── 增量更新状态管理 ──────────────────────────────────────
def load_fetch_state() -> dict:
    """加载抓取状态。"""
    if FETCH_STATE_JSON.exists():
        with open(FETCH_STATE_JSON) as f:
            return json.load(f)
    return {}


def save_fetch_state(state: dict):
    """保存抓取状态。"""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(FETCH_STATE_JSON, "w") as f:
        json.dump(state, f, indent=2)


def get_content_hash(content: str) -> str:
    """计算内容 SHA256 哈希。"""
    return hashlib.sha256(content.encode("utf-8", errors="ignore")).hexdigest()[:16]


def url_to_filename(url: str) -> str:
    """URL 转合法文件名。"""
    parsed = urlparse(url)
    path = parsed.path.rstrip("/")
    if path.endswith(".html"):
        path = path[:-5]
    if path.endswith("/index"):
        path = path[:-6]
    parts = [p for p in path.split("/") if p and p != "en" and p != "latest"]
    return "_".join(parts) if parts else "index"

# ── 源配置 ──────────────────────────────────────────
SOURCES = {
    "rocm": {
        "name": "ROCm Official Docs",
        "base_url": "https://rocm.docs.amd.com/en/latest/",
        "source_type": "official",
        "source_org": "amd",
        "credibility": 5,
        "pages": [
            # ── 总览 ──
            "what-is-rocm.html",
            "index.html",
            # ── About ──
            "about/release-notes.html",
            "about/license.html",
            # ── Compatibility ──
            "compatibility/compatibility-matrix.html",
            "compatibility/ml-compatibility/pytorch.html",
            "compatibility/ml-compatibility/tensorflow.html",
            "compatibility/ml-compatibility/jax.html",
            "compatibility/ml-compatibility/dgl.html",
            # ── Conceptual ──
            "conceptual/gpu-arch.html",
            "conceptual/gpu-arch/mi100.html",
            "conceptual/gpu-arch/mi250.html",
            "conceptual/gpu-arch/mi300.html",
            "conceptual/file-reorg.html",
            "conceptual/gpu-isolation.html",
            "conceptual/cmake-packages.html",
            "conceptual/ai-pytorch-inception.html",
            "conceptual/compiler-topics.html",
            # ── How-To: General ──
            "how-to/deep-learning-rocm.html",
            "how-to/programming_guide.html",
            "how-to/build-rocm.html",
            "how-to/system-debugging.html",
            "how-to/setting-cus.html",
            "how-to/Bar-Memory.html",
            # ── How-To: Performance ──
            "how-to/gpu-performance/mi300x.html",
            "how-to/tuning-guides/mi300x/index.html",
            "how-to/system-optimization/index.html",
            "how-to/system-optimization/rdna3.5.html",
            # ── ROCm for AI ──
            "how-to/rocm-for-ai/index.html",
            "how-to/rocm-for-ai/install.html",
            "how-to/rocm-for-ai/system-setup/index.html",
            "how-to/rocm-for-ai/training/index.html",
            "how-to/rocm-for-ai/training/scale-model-training.html",
            "how-to/rocm-for-ai/inference/index.html",
            "how-to/rocm-for-ai/inference/deploy-your-model.html",
            "how-to/rocm-for-ai/inference/hugging-face-models.html",
            "how-to/rocm-for-ai/inference/llm-inference-frameworks.html",
            "how-to/rocm-for-ai/fine-tuning/index.html",
            "how-to/rocm-for-ai/inference-optimization/index.html",
            "how-to/rocm-for-ai/inference-optimization/model-quantization.html",
            # ── ROCm for HPC ──
            "how-to/rocm-for-hpc/index.html",
            # ── Reference ──
            "reference/api-libraries.html",
            "reference/env-variables.html",
            "reference/rocm-tools.html",
            "reference/gpu-arch-specs.html",
            "reference/gpu-atomics-operation.html",
            "reference/precision-support.html",
            "reference/graph-safe-support.html",
            "reference/glossary/index.html",
            # ── Contribute ──
            "contribute/contributing.html",
            "contribute/building.html",
            "contribute/toolchain.html",
            # ── Release ──
            "release/versions.html",
            "release/changelog.html",
        ],
    },
    "hip": {
        "name": "HIP Official Docs",
        "base_url": "https://rocm.docs.amd.com/projects/HIP/en/latest/",
        "source_type": "official",
        "source_org": "amd",
        "credibility": 5,
        "pages": [
            "index.html",
            "how-to/hip_porting_guide.html",
            "reference/index.html",
            "how-to/hip_install.html",
            "how-to/hip_debugging.html",
        ],
    },
    "rocm-install-linux": {
        "name": "ROCm Install (Linux)",
        "base_url": "https://rocm.docs.amd.com/projects/install-on-linux/en/latest/",
        "source_type": "official",
        "source_org": "amd",
        "credibility": 5,
        "pages": [
            "index.html",
            "reference/system-requirements.html",
            "install/install-quick.html",
            "install/install-amdgpu.html",
            "install/install-post.html",
        ],
    },
    "hipify": {
        "name": "HIPIFY Docs",
        "base_url": "https://rocm.docs.amd.com/projects/HIPIFY/en/latest/",
        "source_type": "official",
        "source_org": "amd",
        "credibility": 5,
        "pages": [
            "index.html",
            "supported_apis.html",
            "hipify-clang.html",
            "hipify-perl.html",
        ],
    },
    "amd-blog": {
        "name": "AMD ROCm Blog",
        "base_url": "https://rocm.blogs.amd.com/",
        "source_type": "blog",
        "source_org": "amd",
        "credibility": 4,
        "rss": "https://rocm.blogs.amd.com/feed.xml",
    },
}


def url_to_filename(url: str) -> str:
    """将 URL 转换为安全的文件名。"""
    parsed = urlparse(url)
    path = parsed.path.strip("/").replace("/", "_")
    if not path:
        path = "index"
    # 移除扩展名
    path = re.sub(r"\.(html?|php|aspx?)$", "", path)
    return re.sub(r"[^a-zA-Z0-9_-]", "_", path)[:128]


def url_fingerprint(content: str) -> str:
    """生成内容指纹，用于去重。"""
    # 去除空白后取 hash
    cleaned = re.sub(r"\s+", "", content)[:4096]
    return hashlib.sha256(cleaned.encode()).hexdigest()[:16]


def load_existing_index() -> dict:
    """加载已有文章索引。"""
    if ARTICLES_JSON.exists():
        with open(ARTICLES_JSON) as f:
            return json.load(f)
    return {"articles": [], "fingerprints": {}}


def save_index(index: dict):
    """保存文章索引。"""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(ARTICLES_JSON, "w") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)


# ── Sitemap 自动发现 ──────────────────────────────────────
SITEMAP_URLS = {
    "rocm": "https://rocm.docs.amd.com/sitemap.xml",
    "hip": "https://rocmdocs.readthedocs.io/en/latest/sitemap.xml",  # fallback
}


def discover_urls_from_sitemap(sitemap_url: str, max_urls: int = 500) -> Set[str]:
    """从 sitemap.xml 自动发现所有文档 URL。"""
    print(f"  🗺️ Discovering from sitemap...")
    html = fetch_page(sitemap_url)
    if not html:
        print(f"  ⚠ Failed to fetch sitemap: {sitemap_url}")
        return set()

    try:
        root = ET.fromstring(html)
    except ET.ParseError:
        print(f"  ⚠ Failed to parse sitemap XML")
        return set()

    NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
    urls = set()

    # Handle sitemap index (multiple sitemaps)
    if root.tag == f"{NS}sitemapindex" or root.tag == "sitemapindex":
        for sub in root.findall(f"{NS}sitemap") or root.findall("sitemap"):
            loc = sub.find(f"{NS}loc") or sub.find("loc")
            if loc is None or not loc.text:
                continue
            sub_url = loc.text.strip()
            if "python" in sub_url or "json" in sub_url:
                continue  # skip non-doc sitemaps

            sub_html = fetch_page(sub_url)
            if not sub_html:
                continue
            try:
                sub_root = ET.fromstring(sub_html)
            except ET.ParseError:
                continue

            for url_el in sub_root.findall(f"{NS}url") or sub_root.findall("url"):
                loc_el = url_el.find(f"{NS}loc") or url_el.find("loc")
                if loc_el is None or not loc_el.text:
                    continue
                url = loc_el.text.strip()
                # Only keep valid HTML docs
                if url.endswith(".html") or url.endswith("/"):
                    if "/pdf/" not in url and ".pdf" not in url:
                        urls.add(url)

                if len(urls) >= max_urls:
                    break
            if len(urls) >= max_urls:
                break
    else:
        # Single sitemap (urlset directly)
        # Use namespace aware parsing
        for url_el in root.findall(f"{NS}url"):
            loc_el = url_el.find(f"{NS}loc")
            if loc_el is None or not loc_el.text:
                continue
            url = loc_el.text.strip()
            if (url.endswith(".html") or url.endswith("/")) and "/pdf/" not in url:
                urls.add(url)
        # Fallback for non-namespaced XML
        if not urls:
            for url_el in root.findall("url"):
                loc_el = url_el.find("loc")
                if loc_el is None or not loc_el.text:
                    continue
                url = loc_el.text.strip()
                if (url.endswith(".html") or url.endswith("/")) and "/pdf/" not in url:
                    urls.add(url)

    print(f"  🔍 Discovered {len(urls)} document URLs")
    return urls


def fetch_page(url: str, timeout: int = 30) -> Optional[str]:
    """抓取单个页面，返回 HTML 文本。"""
    try:
        result = subprocess.run(
            ["curl", "-sL", "--max-time", str(timeout),
             "-H", "User-Agent: rocm-hip-map-fetcher/1.0",
             url],
            capture_output=True, text=True, timeout=timeout + 5,
        )
        if result.returncode != 0 or not result.stdout.strip():
            return None
        return result.stdout
    except Exception as e:
        print(f"  ⚠ fetch failed: {url} ({e})")
        return None


def html_to_markdown(html: str, url: str) -> Optional[str]:
    """将 HTML 转为 Markdown（使用 pandoc）。"""
    try:
        result = subprocess.run(
            ["pandoc", "-f", "html", "-t", "markdown",
             "--wrap=none", "--strip-comments",
             f"--metadata=title:Imported from {url}"],
            input=html, capture_output=True, text=True, timeout=60,
        )
        if result.returncode != 0:
            return None
        return result.stdout
    except Exception:
        return None


def generate_frontmatter(meta: dict) -> str:
    """生成 v2 frontmatter YAML。"""
    lines = ["---"]
    for key in [
        "title", "source_url", "source_type", "source_org",
        "published_date", "original_lang",
        "credibility", "lifecycle", "version",
        "rocm_versions", "os", "gpu", "gpu_arch", "driver",
        "frameworks", "tags", "difficulty",
    ]:
        val = meta.get(key)
        if val is None:
            continue
        if isinstance(val, list):
            if all(isinstance(v, str) for v in val):
                lines.append(f"{key}: [{', '.join(repr(v) for v in val)}]")
            else:
                lines.append(f"{key}: {json.dumps(val)}")
        elif isinstance(val, bool):
            lines.append(f"{key}: {str(val).lower()}")
        elif isinstance(val, (int, float)):
            lines.append(f"{key}: {val}")
        else:
            lines.append(f"{key}: {json.dumps(str(val))}")
    lines.append("synced_date: " + datetime.now(timezone.utc).strftime("%Y-%m-%d"))
    lines.append("---")
    return "\n".join(lines)


def process_source(source_key: str, config: dict, dry_run: bool = False,
                 auto_discover: bool = False, verbose: bool = False,
                 known_urls: dict = None) -> dict:
    """处理单个来源，返回处理结果统计。

    Returns: {"processed": int, "new": int, "updated": int, "unchanged": int}
    """
    if known_urls is None:
        known_urls = {}

    print(f"\n📥 {config['name']} ({source_key})")
    stats = {"processed": 0, "new": 0, "updated": 0, "unchanged": 0}
    base = config["base_url"]

    # 自动发现：从 sitemap 获取 URLs
    urls_to_fetch = []
    if auto_discover:
        sitemap_url = SITEMAP_URLS.get(source_key, "")
        if sitemap_url:
            discovered = discover_urls_from_sitemap(sitemap_url)
            urls_to_fetch = sorted(discovered)
            if verbose:
                print(f"   Discovered {len(urls_to_fetch)} URLs from sitemap")
        else:
            urls_to_fetch = [urljoin(base, p) for p in config.get("pages", [])]
    else:
        urls_to_fetch = [urljoin(base, p) for p in config.get("pages", [])]

    for url in urls_to_fetch:
        fname = f"{source_key}_{url_to_filename(url)}.md"
        out_path = CONTENT_RAW_EN / fname

        # 增量更新检查
        url_state = known_urls.get(url, {})
        last_hash = url_state.get("hash", "")

        if dry_run:
            print(f"  [DRY] {url} → {fname}")
            stats["processed"] += 1
            continue

        # 抓取内容
        html = fetch_page(url)
        if not html:
            continue

        content_hash = get_content_hash(html)

        if out_path.exists():
            # 文件已存在：检查是否需要更新
            if last_hash and last_hash == content_hash:
                # 内容未变化
                if verbose:
                    print(f"  ⏭ unchanged: {fname}")
                stats["unchanged"] += 1
                stats["processed"] += 1
                continue
            else:
                # 内容已变化，需要重新抓取
                if verbose:
                    print(f"  🔄 updated: {fname}")
                stats["updated"] += 1
        else:
            # 新文件
            print(f"  🆕 new: {fname}")
            stats["new"] += 1

        md = html_to_markdown(html, url)
        if not md:
            print(f"  ⚠ conversion failed: {url}")
            continue

        # 生成 frontmatter
        title = ""
        for line in md.split("\n"):
            stripped = line.strip()
            if stripped.startswith("# ") and not stripped.startswith("# :"):
                candidate = stripped[2:].strip()
                if candidate and "{" not in candidate and ":::" not in candidate:
                    if candidate not in ("Skip to main content", "Back to top"):
                        title = candidate
                        break
        if not title:
            from urllib.parse import urlparse
            path = urlparse(url).path
            title = path.split("/")[-1].replace(".html", "").replace("-", " ").title()

        meta = {
            "title": title,
            "source_url": url,
            "source_type": config["source_type"],
            "source_org": config["source_org"],
            "credibility": config["credibility"],
            "lifecycle": "latest",
            "original_lang": "en",
        }
        frontmatter = generate_frontmatter(meta)
        full_content = frontmatter + "\n\n" + md

        CONTENT_RAW_EN.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w") as f:
            f.write(full_content)

        # 记录 URL 状态（更新 known_urls dict）
        known_urls[url] = {
            "hash": content_hash,
            "last_fetch": datetime.now(timezone.utc).isoformat(),
            "file": fname,
        }

        print(f"  ✅ {fname} ({len(md)} chars)")
        stats["processed"] += 1
        time.sleep(0.5)  # 礼貌间隔

    return stats


def _run_cache_images():
    """Phase 11.2: 抓取完成后自动缓存图片。"""
    cache_script = PROJECT_ROOT / "scripts" / "cache-images.py"
    if not cache_script.exists():
        print("  ⚠ cache-images.py not found — skipping image cache")
        return
    print("\n🖼️  Syncing image cache...")
    try:
        subprocess.run(
            [sys.executable, str(cache_script)],
            check=True, timeout=180,
            capture_output=False,
        )
    except subprocess.CalledProcessError:
        print("  ⚠ Image caching had errors (non-fatal)")
    except subprocess.TimeoutExpired:
        print("  ⚠ Image caching timed out (non-fatal)")


def main():
    parser = argparse.ArgumentParser(description="Fetch ROCm/HIP official docs")
    parser.add_argument("--dry-run", action="store_true", help="Preview only")
    parser.add_argument("--source", choices=list(SOURCES.keys()), help="Single source")
    parser.add_argument("--auto-discover", action="store_true", help="自动从 sitemap 发现 URL")
    parser.add_argument("--verbose", "-v", action="store_true", help="详细输出")
    args = parser.parse_args()

    print("🔍 rocm-hip-map fetch-official.py (v1.5)")
    print(f"   {'DRY RUN' if args.dry_run else 'LIVE MODE'}")
    if args.auto_discover:
        print("   AUTO-DISCOVER: enabled")

    # 加载抓取状态
    fetch_state = load_fetch_state()
    known_urls = fetch_state.get("urls", {})
    total_urls = len(known_urls)
    stats = {"known": total_urls, "updated": 0, "new": 0, "unchanged": 0}

    sources = {args.source: SOURCES[args.source]} if args.source else SOURCES
    total = 0

    for key, config in sources.items():
        result = process_source(key, config, dry_run=args.dry_run,
                           auto_discover=args.auto_discover, verbose=args.verbose,
                           known_urls=known_urls)
        total += result["processed"]
        stats["updated"] += result["updated"]
        stats["new"] += result["new"]
        stats["unchanged"] += result["unchanged"]

    # 保存抓取状态
    if not args.dry_run and (stats["new"] > 0 or stats["updated"] > 0):
        fetch_state["urls"] = known_urls
        fetch_state["last_fetch"] = datetime.now(timezone.utc).isoformat()
        save_fetch_state(fetch_state)

    print(f"\n📊 Stats:")
    print(f"   {stats['known']} known urls")
    print(f"   {stats['new']} new")
    print(f"   {stats['updated']} updated")
    print(f"   {stats['unchanged']} unchanged")
    print(f"\n   Total: {total} {'(preview)' if args.dry_run else 'fetched'}")

    if not args.dry_run and total > 0:
        print(f"   Raw files → {CONTENT_RAW_EN}")
        print("   Run 'python3 scripts/classify.py' to classify & tag.")
        # ── Phase 11.2: 跟随抓取同步缓存图片 ──
        _run_cache_images()


if __name__ == "__main__":
    main()
