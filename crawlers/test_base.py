#!/usr/bin/env python3
"""rocm-hip-map/crawlers/test_base.py — Phase 2.1.1 验证"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

# 测试 dedup
from crawlers.dedup import normalize_url, url_hash, content_hash, is_tracking_url

assert normalize_url("https://example.com/?utm_source=x&fbclid=abc") == "https://example.com/"
assert normalize_url("https://EXAMPLE.com/") == "https://example.com/"
assert normalize_url("https://example.com/page/?") == "https://example.com/page"
assert is_tracking_url("https://ads.example.com/click?id=123") == True
assert is_tracking_url("https://rocm.docs.amd.com/HIP/") == False
assert len(url_hash("https://example.com")) == 16
assert len(content_hash("hello world")) == 16
print("✅ dedup: all assertions passed")

# 测试 extractor（stdlib 兜底）
from crawlers.extractor import extract, _extract_stdlib

html = b"""
<!DOCTYPE html><html><head><title>Test Article</title></head>
<body><article>
<p>This is a paragraph with enough content to pass the length filter. It contains more than 30 characters.</p>
<p>Another paragraph with substantial text content for testing extraction.</p>
</article></body></html>
"""
result = extract(html, "https://example.com/test")
assert result.title == "Test Article"
assert "paragraph" in result.body
assert result.excerpt
print(f"✅ extractor: title='{result.title}', body_len={len(result.body)}, excerpt='{result.excerpt[:50]}'")

# 测试 base 模块可导入
from crawlers.base import BaseCrawler, RawDoc, ParsedArticle
assert RawDoc(url="http://x.com", status_code=200, content=b"ok", headers={}).ok == True
assert RawDoc(url="http://x.com", status_code=304, content=b"", headers={}).not_modified == True
print("✅ base: BaseCrawler / RawDoc / ParsedArticle import OK")

# 测试 http_client 可导入
from crawlers.http_client import HttpClient
client = HttpClient(timeout=5.0)
assert client.timeout == 5.0
print(f"✅ http_client: HttpClient(timeout={client.timeout}) OK")

print("\n🎉 Phase 2.1.1 modules: all tests passed")
