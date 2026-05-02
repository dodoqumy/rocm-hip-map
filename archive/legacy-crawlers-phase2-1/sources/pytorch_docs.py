"""
rocm-hip-map/crawlers/sources/pytorch_docs.py
Phase 2.1.2 — PyTorch ROCm 文档爬虫

抓取 PyTorch 官方文档中与 ROCm 相关的页面。
"""
from __future__ import annotations

import re
from typing import Iterator

from ..base import BaseCrawler, RawDoc, ParsedArticle
from ..http_client import HttpClient
from ..extractor import extract
from ..dedup import normalize_url


# PyTorch ROCm 相关 sitemap
PYTORCH_ROCM_SITEMAPS = [
    "https://pytorch.org/docs/master/sitemap.xml",
    "https://pytorch.org/docs/stable/sitemap.xml",
]

# 关键词：只在标题/URL 含这些词的页面才抓
ROCM_KEYWORDS = [
    "rocm", "amd", "hip", "mi300", "mi250", "mi210",
    "radeon", "gfx", "rocblas", "hipblas", "rccl",
    "rocfft", "miopen", "rocprofiler",
]


class PyTorchDocsCrawler(BaseCrawler):
    """PyTorch ROCm 相关文档爬虫。"""

    slug = "pytorch-docs"
    name = "PyTorch ROCm Documentation"
    source_type = "official"
    rate_limit = 0.5

    _http: HttpClient

    def __init__(self):
        super().__init__()
        self._http = HttpClient(timeout=20.0)

    def discover(self) -> Iterator[str]:
        """从 sitemap 过滤出 ROCm 相关页面。"""
        import xml.etree.ElementTree as ET

        for sitemap_url in PYTORCH_ROCM_SITEMAPS:
            self._log.info("Scanning sitemap: %s", sitemap_url)
            try:
                raw = self._http.fetch(sitemap_url)
                if not raw.ok:
                    continue

                root = ET.fromstring(raw.content)
                ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
                urls = root.findall("sm:url", ns) or root.findall("url")

                for url_el in urls:
                    loc_el = url_el.find("sm:loc", ns) or url_el.find("loc")
                    if loc_el is None or not loc_el.text:
                        continue
                    url = loc_el.text.strip()
                    if self._is_rocm_related(url):
                        yield normalize_url(url)

            except Exception as e:
                self._log.warning("Failed sitemap %s: %s", sitemap_url, e)

    def _is_rocm_related(self, url: str) -> bool:
        """判断 URL 是否与 ROCm 相关。"""
        url_lower = url.lower()
        for kw in ROCM_KEYWORDS:
            if kw in url_lower:
                return True
        return False

    def fetch(self, url: str) -> RawDoc:
        return self._http.fetch(url)

    def parse(self, raw: RawDoc) -> ParsedArticle:
        content = extract(raw.content, raw.url)
        return ParsedArticle(
            title=content.title or raw.url,
            body=content.body,
            excerpt=content.excerpt,
            published_at=content.published_at,
            difficulty=self._guess_difficulty(content.title, content.body),
            word_count=len(content.body.split()),
        )

    def _guess_difficulty(self, title: str, body: str) -> str:
        t = (title + " " + body).lower()
        if any(k in t for k in ["install", "getting started", "prerequisite"]):
            return "beginner"
        if any(k in t for k in ["api", "reference", "nn.module"]):
            return "reference"
        if any(k in t for k in ["benchmark", "performance", "tuning"]):
            return "advanced"
        return "intermediate"
