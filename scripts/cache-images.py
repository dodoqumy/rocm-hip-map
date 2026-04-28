#!/usr/bin/env python3
"""
cache-images.py — 将原始 Markdown 中的远程图片缓存到本地。

扫描 content/raw/ 下的 markdown 文件 → 解析图片 URL → 下载 → 压缩 → 生成映射表

用法：
  python3 scripts/cache-images.py              # 增量缓存（跳过已有的）
  python3 scripts/cache-images.py --force       # 强制重新下载所有
  python3 scripts/cache-images.py --dry-run     # 预览不下载
  python3 scripts/cache-images.py --clean-orphans  # 清理孤立文件
"""
import argparse
import hashlib
import json
import re
import sys
import time
from datetime import datetime, timezone
from io import BytesIO
from pathlib import Path
from typing import Optional, Tuple
from urllib.parse import urljoin, urlparse

import requests
from PIL import Image

# ── 项目根目录 ──────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONTENT_RAW_EN = PROJECT_ROOT / "content" / "raw" / "english"
CONTENT_RAW_ZH = PROJECT_ROOT / "content" / "raw" / "chinese"
STATIC_IMG = PROJECT_ROOT / "website" / "static" / "img" / "cached"
DATA_DIR = PROJECT_ROOT / "data"
CACHE_JSON = DATA_DIR / "image-cache.json"
FALLBACKS_JSON = PROJECT_ROOT / "website" / "static" / "data" / "image-fallbacks.json"


def save_fallbacks(cache: dict):
    """生成前端可直接使用的 fallback 映射 JSON。

    格式: { "https://绝对URL": "/img/cached/本地路径", ... }
    """
    fallbacks = {}
    for raw_path, mapping in cache.get("mappings", {}).items():
        source_url = mapping.get("source_url", "")
        local = mapping.get("local", "")
        if source_url and local:
            fallbacks[source_url] = local

    out_path = FALLBACKS_JSON
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(fallbacks, f, indent=2, ensure_ascii=False)
    print(f"   前端 fallback 表: {out_path} ({len(fallbacks)} 条)")

# ── 源 base_url 映射（用于解析相对路径）────────────
SOURCE_BASE_URLS = {
    "rocm": "https://rocm.docs.amd.com/en/latest/",
    "hip": "https://rocm.docs.amd.com/projects/HIP/en/latest/",
    "rocm-install-linux": "https://rocm.docs.amd.com/projects/install-on-linux/en/latest/",
    "hipify": "https://rocm.docs.amd.com/projects/HIPIFY/en/latest/",
}

# ── 请求配置 ────────────────────────────────────────
HEADERS = {
    "User-Agent": "rocm-hip-map-image-cacher/1.0",
}
REQUEST_TIMEOUT = 30
MAX_RETRIES = 3

# ── 图片格式配置 ────────────────────────────────────
WEBP_QUALITY = 85
MAX_IMAGE_SIZE_MB = 20  # 单张图片最大 20MB

# ── 图片 URL 正则（匹配 Markdown ![alt](url) ──────
# 支持：![alt](url)、![alt](url){.class}、[![alt](url)](url2) 等
IMG_RE = re.compile(
    r'!\[([^\]]*)\]\(([^)]+)\)',
)


def extract_source_key(filename: str) -> str:
    """从文件名推断来源 key。"""
    for key in SOURCE_BASE_URLS:
        if filename.startswith(key + "_"):
            return key
    return "rocm"  # 默认


def extract_page_url(content: str) -> Optional[str]:
    """从 frontmatter 中提取 source_url（页面原始 URL）。"""
    fm_match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if fm_match:
        m = re.search(r'(?:^|\n)source_url:\s*"?(.+?)"?\s*$', fm_match.group(1), re.MULTILINE)
        if m:
            url = m.group(1).strip().strip('"').strip("'")
            if url.startswith("http"):
                return url
    return None


def resolve_image_url(raw_path: str, page_url: str) -> Optional[str]:
    """将 Markdown 中的相对/绝对图片路径解析为绝对 URL。"""
    # 跳过 data: URI
    if raw_path.startswith("data:"):
        return None

    # 已经是绝对 HTTP URL
    if raw_path.startswith("http://") or raw_path.startswith("https://"):
        return raw_path

    # 相对路径 → 用页面 URL 解析
    try:
        return urljoin(page_url, raw_path)
    except Exception:
        return None


def derive_slug(filename: str) -> str:
    """从文件名派生目录 slug。"""
    stem = Path(filename).stem
    # 去掉 source_ 前缀
    for key in SOURCE_BASE_URLS:
        if stem.startswith(key + "_"):
            stem = stem[len(key) + 1:]
            break
    return stem[:64]  # 限制长度


def compute_hash(data: bytes) -> str:
    """计算 SHA256 前 8 位。"""
    return hashlib.sha256(data).hexdigest()[:8]


def download_image(url: str) -> Optional[bytes]:
    """下载图片，带重试，返回字节。"""
    for attempt in range(MAX_RETRIES):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=REQUEST_TIMEOUT)
            resp.raise_for_status()

            # 检查大小
            content_length = resp.headers.get("Content-Length")
            if content_length:
                size_mb = int(content_length) / (1024 * 1024)
                if size_mb > MAX_IMAGE_SIZE_MB:
                    print(f"  ⚠ 图片过大 ({size_mb:.1f}MB)，跳过: {url}")
                    return None

            # 检查 Content-Type 是图片
            content_type = resp.headers.get("Content-Type", "")
            if content_type and not content_type.startswith("image/"):
                # 有些 CDN 不返回正确的 content-type，不阻塞
                pass

            return resp.content

        except requests.RequestException as e:
            if attempt < MAX_RETRIES - 1:
                wait = 2 ** attempt
                print(f"  ⚠ 下载失败 (重试 {attempt+1}/{MAX_RETRIES}): {url} - {e}")
                time.sleep(wait)
            else:
                print(f"  ❌ 下载失败: {url} - {e}")
                return None


def detect_format(data: bytes) -> str:
    """通过文件头检测图片格式。"""
    if data[:4] == b'\x89PNG':
        return 'png'
    if data[:2] == b'\xff\xd8':
        return 'jpg'
    if data[:4] == b'RIFF' and data[8:12] == b'WEBP':
        return 'webp'
    if data[:3] == b'GIF':
        return 'gif'
    if data[:4] == b'<svg' or data[:5] == b'<?xml':
        return 'svg'
    # 默认
    return 'png'


def convert_to_webp(data: bytes, source_format: str) -> Optional[bytes]:
    """将图片转为 WebP 格式。SVG 不转换。"""
    if source_format == 'svg':
        return None  # SVG 保持原样
    if source_format == 'webp':
        return data  # 已是 WebP

    try:
        img = Image.open(BytesIO(data))
        buf = BytesIO()
        # RGBA → RGB（WebP 不支持 alpha 时用 PNG 保留透明）
        if img.mode in ('RGBA', 'LA', 'P'):
            # 有透明通道 → 保持 PNG 原格式，不转 WebP
            return None
        img.save(buf, format='WEBP', quality=WEBP_QUALITY)
        return buf.getvalue()
    except Exception as e:
        print(f"  ⚠ WebP 转换失败: {e}，保留原格式")
        return None


def load_cache() -> dict:
    """加载已有映射表。"""
    if CACHE_JSON.exists():
        with open(CACHE_JSON) as f:
            return json.load(f)
    return {"version": 1, "updated": "", "mappings": {}}


def save_cache(cache: dict):
    """保存映射表。"""
    cache["updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(CACHE_JSON, "w") as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)


def process_file(md_path: Path, cache: dict, force: bool = False, dry_run: bool = False) -> int:
    """处理单个 raw markdown 文件，缓存其中所有图片。返回缓存图片数。"""
    with open(md_path, encoding="utf-8") as f:
        content = f.read()

    filename = md_path.name
    source = extract_source_key(filename)
    page_url = extract_page_url(content)
    if not page_url:
        print(f"  ⚠ 无 source_url，跳过: {filename}")
        return 0
    slug = derive_slug(filename)

    cached_count = 0
    seen_urls = set()  # 同一文件内去重

    for match in IMG_RE.finditer(content):
        alt_text = match.group(1) or ""
        raw_path = match.group(2)

        # 跳过 data: URI
        if raw_path.startswith("data:"):
            continue

        # 解析为绝对 URL（相对于页面 URL）
        abs_url = resolve_image_url(raw_path, page_url)
        if not abs_url:
            continue

        # 文件内去重
        if abs_url in seen_urls:
            continue
        seen_urls.add(abs_url)

        # 检查是否已缓存
        if raw_path in cache["mappings"] and not force:
            cached_count += 1
            continue

        if dry_run:
            print(f"  [DRY] {raw_path} → {abs_url}")
            cached_count += 1
            continue

        # 下载
        print(f"  ↓ {raw_path}")
        img_data = download_image(abs_url)
        if not img_data:
            continue

        # 计算哈希
        img_hash = compute_hash(img_data)

        # 检测格式
        fmt = detect_format(img_data)

        # 转 WebP（可选）
        webp_data = convert_to_webp(img_data, fmt)

        # 保存原始格式
        orig_name = f"{img_hash}-{Path(raw_path).name}"
        if not orig_name.lower().endswith(f".{fmt}"):
            orig_name = f"{img_hash}-{Path(raw_path).stem}.{fmt}"

        out_dir = STATIC_IMG / source / slug
        out_dir.mkdir(parents=True, exist_ok=True)

        orig_path = out_dir / orig_name
        with open(orig_path, "wb") as f:
            f.write(img_data)

        # 保存 WebP（如果转换成功）
        if webp_data and fmt != 'webp':
            webp_name = f"{img_hash}-{Path(raw_path).stem}.webp"
            webp_path = out_dir / webp_name
            with open(webp_path, "wb") as f:
                f.write(webp_data)

        # 记录到映射表（key 使用 raw markdown 中的原始路径）
        local_path = f"/img/cached/{source}/{slug}/{orig_name}"
        cache["mappings"][raw_path] = {
            "local": local_path,
            "hash": img_hash,
            "size_bytes": len(img_data),
            "downloaded_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "source_url": abs_url,
        }
        cached_count += 1

    return cached_count


def clean_orphans(cache: dict):
    """删除磁盘上孤立（不在映射表中的）缓存文件。"""
    if not STATIC_IMG.exists():
        return

    valid_paths = set()
    for mapping in cache["mappings"].values():
        local = mapping.get("local", "")
        if local:
            # /img/cached/rocm/foo/bar.png → 文件系统路径
            rel = local.replace("/img/cached/", "")
            valid_paths.add(str(STATIC_IMG / rel))

    removed = 0
    for img_file in STATIC_IMG.rglob("*"):
        if img_file.is_file():
            if str(img_file) not in valid_paths:
                img_file.unlink()
                print(f"  🗑 清理: {img_file.relative_to(STATIC_IMG)}")
                removed += 1

    # 清理空目录
    for dirpath in sorted(STATIC_IMG.rglob("*"), reverse=True):
        if dirpath.is_dir() and not any(dirpath.iterdir()):
            dirpath.rmdir()

    return removed


def main():
    parser = argparse.ArgumentParser(description="缓存 raw markdown 中的远程图片到本地")
    parser.add_argument("--dry-run", action="store_true", help="预览不下载")
    parser.add_argument("--force", action="store_true", help="强制重新下载所有")
    parser.add_argument("--clean-orphans", action="store_true", help="清理孤立缓存文件")
    args = parser.parse_args()

    print("🖼️  rocm-hip-map cache-images.py")
    print(f"   {'DRY RUN' if args.dry_run else 'LIVE MODE'}{' (force)' if args.force else ''}")

    cache = load_cache()

    if args.clean_orphans:
        removed = clean_orphans(cache)
        print(f"\n📊 清理了 {removed} 个孤立文件")
        save_cache(cache)
        return

    # 扫描 raw markdown 文件
    md_files = sorted(CONTENT_RAW_EN.glob("*.md"))

    if not md_files:
        print("⚠ content/raw/english/ 为空 — 请先运行 fetch-official.py")
        return

    total_cached = 0
    files_with_images = 0

    for md_path in md_files:
        count = process_file(md_path, cache, force=args.force, dry_run=args.dry_run)
        if count > 0:
            total_cached += count
            files_with_images += 1

    save_cache(cache)
    save_fallbacks(cache)

    print(f"\n📊 结果: {files_with_images} 个文件 / {total_cached} 张图片"
          f"{' (预览)' if args.dry_run else ' 已缓存'}")
    print(f"   映射表: {CACHE_JSON}")
    print(f"   缓存目录: {STATIC_IMG}")

    if not args.dry_run and total_cached > 0:
        print("\n💡 下一步:")
        print("   npm run build  # 重新构建即可，图片路径无需修改")


if __name__ == "__main__":
    main()
