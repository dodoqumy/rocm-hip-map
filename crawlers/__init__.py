"""
ROCm 文档爬虫套件 (Phase 2.1)
"""

from .base import BaseCrawler, CrawlerConfig, load_sources, get_crawler, FetchResult
from .http_client import HTTPClient, compute_content_hash
from .dedup import Deduplicator, normalize_url, compute_url_hash
from .url_family import normalize_url_family, extract_version, is_latest_version
from .extractor import ContentExtractor, is_doxygen_page, is_js_rendered

__all__ = [
    "BaseCrawler",
    "CrawlerConfig", 
    "load_sources",
    "get_crawler",
    "FetchResult",
    "HTTPClient",
    "compute_content_hash",
    "Deduplicator",
    "normalize_url",
    "compute_url_hash",
    "normalize_url_family",
    "extract_version",
    "is_latest_version",
    "ContentExtractor",
    "is_doxygen_page",
    "is_js_rendered",
]