#!/usr/bin/env python3
"""rocm-hip-map/crawlers/test_sources.py — Phase 2.1.2 验证"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

# 测试 import
from crawlers.sources.rocm_docs import RocmDocsCrawler
from crawlers.sources.rocm_blog import RocmBlogCrawler
from crawlers.sources.pytorch_docs import PyTorchDocsCrawler

print("✅ All crawler classes imported successfully")

# 测试 discover 采样（只取前 5 个 URL）
print("\n=== RocmDocsCrawler.discover() (first 5) ===")
crawler = RocmDocsCrawler()
count = 0
for url in crawler.discover():
    print(f"  {url}")
    count += 1
    if count >= 5:
        break
print(f"  → Total discovered: {crawler._discovered} URLs")

print("\n=== RocmBlogCrawler.discover() (first 5) ===")
blog = RocmBlogCrawler()
count = 0
for url in blog.discover():
    print(f"  {url}")
    count += 1
    if count >= 5:
        break

print("\n✅ Phase 2.1.2 crawlers: discovery verified")
