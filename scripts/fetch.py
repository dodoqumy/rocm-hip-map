#!/usr/bin/env python3
"""
统一抓取入口 (Phase 2.1)
支持发现、抓取、保存
"""

import argparse
import logging
import sys
import json
import hashlib
from pathlib import Path
from datetime import datetime, timezone

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from crawlers import load_sources, get_crawler, compute_content_hash

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
logger = logging.getLogger(__name__)


CONTENT_DIR = PROJECT_ROOT / "content" / "raw" / "english"
STATE_FILE = PROJECT_ROOT / "data" / "fetch-state.json"


def save_article(url: str, title: str, content: str, source: str) -> str:
    """保存文章到 content/raw/english/"""
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    
    # 生成文件名
    path = url.replace("https://rocm.docs.amd.com/", "")
    path = path.replace("https://", "")
    path = path.strip("/")
    path = path.replace(".html", "")
    path = path.replace("/", "_")
    
    # 避免文件名太长
    if len(path) > 100:
        path = path[:100]
    
    fname = f"{source}_{path}.md"
    fpath = CONTENT_DIR / fname
    
    # Frontmatter
    content_hash = compute_content_hash(content)
    frontmatter = f"""---
title: "{title}"
source_url: "{url}"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: {datetime.now(timezone.utc).isoformat()}
content_hash: "{content_hash}"
---

{content}
"""
    
    fpath.write_text(frontmatter)
    logger.info(f"  💾 {fname} ({len(content)} chars)")
    
    return fname


def load_state() -> dict:
    """加载抓取状态"""
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {}


def save_state(state: dict):
    """保存抓取状态"""
    STATE_FILE.write_text(json.dumps(state, indent=2))


def run_crawler(slug: str, dry_run: bool = False, max_urls: int = 0, force: bool = False):
    """运行单个爬虫"""
    sources = load_sources(PROJECT_ROOT / "config/amd-sources.yaml")
    
    config = None
    for s in sources:
        if s.slug == slug:
            config = s
            break
    
    if not config:
        logger.error(f"Unknown source: {slug}")
        return {"error": f"Unknown source: {slug}"}
    
    logger.info(f"🚀 Starting: {config.name}")
    
    crawler = get_crawler(config)
    
    # Discover
    urls = crawler.discover(max_urls)
    logger.info(f"  📍 Discovered {len(urls)} URLs")
    
    if dry_run:
        for url in urls[:20]:
            print(f"    {url}")
        return {"discovered": len(urls), "dry_run": True}
    
    # Load state
    state = load_state()
    source_state = state.get(slug, {"urls": {}, "last_fetch": None})
    
    # Fetch
    saved = 0
    errors = 0
    
    for i, url in enumerate(urls):
        # 限速
        crawler.http.rate_limit_per_domain(crawler.domain)
        
        # 检查是否已抓取 (跳过 unchanged)
        if not force and url in source_state.get("urls", {}):
            last_hash = source_state["urls"][url].get("content_hash", "")
            logger.debug(f"  ⏭ {url[:50]}... (cached)")
            continue
        
        result = crawler.fetch(url)
        if result and result.content:
            # Extract title
            if not result.title:
                result.title = url.split("/")[-1].replace(".html", "").replace("_", " ").title()
            
            # Save
            try:
                save_article(url, result.title, result.content, slug)
                saved += 1
                
                # Update state
                source_state.setdefault("urls", {})[url] = {
                    "content_hash": result.content_hash,
                    "fetched_at": datetime.now(timezone.utc).isoformat(),
                }
            except Exception as e:
                logger.error(f"  ⚠ Save failed: {e}")
                errors += 1
        else:
            errors += 1
        
        if (i + 1) % 10 == 0:
            logger.info(f"  📥 Progress: {i+1}/{len(urls)}")
    
    # Save state
    source_state["last_fetch"] = datetime.now(timezone.utc).isoformat()
    state[slug] = source_state
    save_state(state)
    
    logger.info(f"  ✅ Done: {saved} saved, {errors} errors")
    
    return {
        "slug": slug,
        "discovered": len(urls),
        "saved": saved,
        "errors": errors,
    }


def run_all(dry_run: bool = False, max_per_source: int = 0):
    """运行所有源"""
    sources = load_sources(PROJECT_ROOT / "config/amd-sources.yaml")
    
    logger.info(f"📚 Running {len(sources)} sources...")
    
    results = []
    for config in sources:
        try:
            result = run_crawler(config.slug, dry_run=dry_run, max_urls=max_per_source)
            results.append(result)
        except Exception as e:
            logger.error(f"  ⚠ {config.slug}: {e}")
            results.append({"slug": config.slug, "error": str(e)})
    
    total = sum(r.get("saved", 0) for r in results)
    
    logger.info(f"📊 Total: {total} articles saved")
    
    return {
        "sources": len(sources),
        "total_saved": total,
        "results": results,
    }


def main():
    parser = argparse.ArgumentParser(description="ROCm 文档抓取")
    parser.add_argument("--all", action="store_true", help="全量抓取")
    parser.add_argument("--source", help="单源 slug")
    parser.add_argument("--dry-run", action="store_true", help="预览不抓取")
    parser.add_argument("--max-urls", type=int, default=0, help="最大 URL 数")
    parser.add_argument("--force", action="store_true", help="强制重抓")
    parser.add_argument("--verbose", action="store_true", help="详细输出")
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    if args.source:
        result = run_crawler(args.source, dry_run=args.dry_run, max_urls=args.max_urls, force=args.force)
    elif args.all:
        result = run_all(dry_run=args.dry_run, max_per_source=args.max_urls)
    else:
        parser.print_help()
        sys.exit(1)
    
    print(f"\n✅ Done: {result}")
    return 0


if __name__ == "__main__":
    sys.exit(main())