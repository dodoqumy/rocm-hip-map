"""
rocm-hip-map/crawlers/sources/rocm_docs.py
Phase 2.1.2 — AMD ROCm 官方文档爬虫

从 rocm.docs.amd.com 的 sitemap.xml 发现所有页面。
预期：68 篇 → 1500+ 篇。
"""
from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from typing import Iterator

from ..base import BaseCrawler, RawDoc, ParsedArticle
from ..http_client import HttpClient
from ..extractor import extract
from ..dedup import normalize_url


SITEMAP_ROCM = "https://rocm.docs.amd.com/sitemap.xml"


class RocmDocsCrawler(BaseCrawler):
    """ROCm 官方文档爬虫（sitemap 驱动）。"""

    slug = "rocm-docs"
    name = "AMD ROCm Documentation"
    source_type = "official"
    rate_limit = 0.5  # 0.5 req/s（官方站点，保守）

    _http: HttpClient
    _sitemap_urls: list[str] = []
    _discovered: int = 0

    def __init__(self):
        super().__init__()
        self._http = HttpClient(timeout=20.0)

    def discover(self) -> Iterator[str]:
        """
        从 sitemap.xml 发现所有页面 URL。

        处理逻辑：
        1. 抓主 sitemap
        2. 解析 <sitemap> 子节点（多个子 sitemap）
        3. 解析 <url> 节点（具体页面）
        4. 过滤：只保留 HTML 页面，排除 PDF/视频
        """
        self._log.info("Discovering URLs from %s", SITEMAP_ROCM)
        seen = set()

        try:
            raw = self._http.fetch(SITEMAP_ROCM)
            if not raw.ok:
                self._log.error("Failed to fetch sitemap: HTTP %d", raw.status_code)
                return

            root = ET.fromstring(raw.content)

            # namespace URI（sitemap 用 {uri}tag 格式）
            NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
            sitemaps = root.findall(f"{{{NS}}}sitemap")
            urls = root.findall(f"{{{NS}}}url")

            if sitemaps:
                # 主 sitemap 包含子 sitemap
                for sm in sitemaps:
                    loc = sm.find(f"{{{NS}}}loc")
                    if loc is None or not loc.text:
                        continue
                    sub_url = normalize_url(loc.text.strip())
                    if sub_url in seen:
                        continue
                    seen.add(sub_url)

                    try:
                        sub_raw = self._http.fetch(sub_url)
                        if not sub_raw.ok:
                            continue
                        sub_root = ET.fromstring(sub_raw.content)
                        sub_urls = sub_root.findall(f"{{{NS}}}url")
                        for url_el in sub_urls:
                            loc_el = url_el.find(f"{{{NS}}}loc")
                            if loc_el is None or not loc_el.text:
                                continue
                            final_url = normalize_url(loc_el.text.strip())
                            if final_url not in seen:
                                seen.add(final_url)
                                if self._filter_url(final_url):
                                    self._discovered += 1
                                    yield final_url
                    except Exception as e:
                        self._log.warning("Failed to fetch sub-sitemap %s: %s", sub_url, e)

            elif urls:
                # 主 sitemap 直接包含页面
                for url_el in urls:
                    loc_el = url_el.find(f"{{{NS}}}loc")
                    if loc_el is None or not loc_el.text:
                        continue
                    final_url = normalize_url(loc_el.text.strip())
                    if final_url not in seen and self._filter_url(final_url):
                        seen.add(final_url)
                        self._discovered += 1
                        yield final_url

        except ET.ParseError as e:
            self._log.error("Failed to parse sitemap XML: %s", e)

    def _filter_url(self, url: str) -> bool:
        """过滤掉非 HTML 页面和不需要的路径。"""
        url_lower = url.lower()

        # 排除
        skip_patterns = [
            "/pdf/", ".pdf", "/video/", "/changelog",
            "/archive/", "/deprecated/", "/doxygen/",
            "/search", "/404", "/search.html",
        ]
        for pat in skip_patterns:
            if pat in url_lower:
                return False

        # 必须包含
        required_patterns = ["rocm.docs.amd.com"]
        for pat in required_patterns:
            if pat not in url_lower:
                return False

        return True

    def fetch(self, url: str) -> RawDoc:
        return self._http.fetch(url)

    def parse(self, raw: RawDoc) -> ParsedArticle:
        content = extract(raw.content, raw.url)

        # 从 URL 推断 difficulty
        difficulty = self._guess_difficulty(raw.url, content.body)

        return ParsedArticle(
            title=content.title or raw.url,
            body=content.body,
            excerpt=content.excerpt,
            published_at=content.published_at,
            author=content.author,
            difficulty=difficulty,
            word_count=len(content.body.split()),
        )

    def _guess_difficulty(self, url: str, body: str) -> str:
        """从 URL + 内容推断难度。"""
        u = url.lower()
        b = body.lower()

        if any(k in u for k in ["/getting-started", "/install", "/quick-start"]):
            return "beginner"
        if any(k in u for k in ["/api/", "/reference", "/doxygen"]):
            return "reference"
        if any(k in u for k in ["/advanced/", "/tuning/", "/debugging"]):
            return "advanced"
        if any(k in u for k in ["/tutorial", "/how-to", "/examples"]):
            return "intermediate"

        # 基于代码块密度
        code_density = body.count("```") / max(len(body.split()), 1)
        if code_density > 0.03:
            return "advanced"
        elif code_density > 0.01:
            return "intermediate"
        return "beginner"
