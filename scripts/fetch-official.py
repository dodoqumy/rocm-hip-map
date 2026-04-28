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

用法：
  python3 scripts/fetch-official.py              # 全量同步
  python3 scripts/fetch-official.py --dry-run     # 预览
  python3 scripts/fetch-official.py --source rocm # 仅指定源
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
from typing import Optional
from urllib.parse import urljoin, urlparse

# ── 项目根目录 ──────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONTENT_RAW_EN = PROJECT_ROOT / "content" / "raw" / "english"
CONTENT_RAW_ZH = PROJECT_ROOT / "content" / "raw" / "chinese"
DATA_DIR = PROJECT_ROOT / "data"
ARTICLES_JSON = DATA_DIR / "articles.json"

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


def process_source(source_key: str, config: dict, dry_run: bool = False) -> int:
    """处理单个来源，返回新增文章数。"""
    print(f"\n📥 {config['name']} ({source_key})")
    count = 0
    base = config["base_url"]

    for page in config.get("pages", []):
        url = urljoin(base, page)
        fname = f"{source_key}_{url_to_filename(url)}.md"
        out_path = CONTENT_RAW_EN / fname

        if dry_run:
            print(f"  [DRY] {url} → {fname}")
            count += 1
            continue

        # 检查是否已存在
        if out_path.exists():
            print(f"  ⏭ skip (exists): {fname}")
            continue

        html = fetch_page(url)
        if not html:
            continue

        md = html_to_markdown(html, url)
        if not md:
            print(f"  ⚠ conversion failed: {url}")
            continue

        # 生成 frontmatter
        # 智能提取标题：跳过 pandoc artifact 行
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
            title = page.replace(".html", "").replace("index", "Overview")
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

        print(f"  ✅ {fname} ({len(md)} chars)")
        count += 1
        time.sleep(1)  # 礼貌间隔

    return count


def main():
    parser = argparse.ArgumentParser(description="Fetch ROCm/HIP official docs")
    parser.add_argument("--dry-run", action="store_true", help="Preview only")
    parser.add_argument("--source", choices=list(SOURCES.keys()), help="Single source")
    args = parser.parse_args()

    print("🔍 rocm-hip-map fetch-official.py")
    print(f"   {'DRY RUN' if args.dry_run else 'LIVE MODE'}")

    sources = {args.source: SOURCES[args.source]} if args.source else SOURCES
    total = 0

    for key, config in sources.items():
        total += process_source(key, config, dry_run=args.dry_run)

    print(f"\n📊 Total articles: {total} {'(preview)' if args.dry_run else 'fetched'}")
    if not args.dry_run and total > 0:
        print(f"   Raw files → {CONTENT_RAW_EN}")
        print("   Run 'python3 scripts/classify.py' to classify & tag.")


if __name__ == "__main__":
    main()
