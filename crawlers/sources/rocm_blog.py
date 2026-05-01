"""
rocm-hip-map/crawlers/sources/rocm_blog.py
Phase 2.1.2 — ROCm Blog 爬虫

从 RSS feed 和归档页发现文章。
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


BLOG_FEED = "https://rocm.blogs.amd.com/feed.xml"


class RocmBlogCrawler(BaseCrawler):
    """ROCm Blog 爬虫。"""

    slug = "rocm-blog"
    name = "AMD ROCm Blog"
    source_type = "blog"
    rate_limit = 0.5

    _http: HttpClient

    def __init__(self):
        super().__init__()
        self._http = HttpClient(timeout=20.0)

    def discover(self) -> Iterator[str]:
        """从 RSS feed 发现文章 URL。"""
        self._log.info("Fetching RSS feed: %s", BLOG_FEED)
        try:
            raw = self._http.fetch(BLOG_FEED)
            if not raw.ok:
                self._log.error("Failed to fetch RSS: HTTP %d", raw.status_code)
                return

            root = ET.fromstring(raw.content)
            ns = {"atom": "http://www.w3.org/2005/Atom",
                  "dc": "http://purl.org/dc/elements/1.1/"}
            entries = root.findall("atom:entry", ns) or root.findall("entry")

            if not entries:
                entries = root.findall("item")  # RSS 2.0

            for entry in entries:
                loc_el = entry.find("atom:link[@rel='alternate']", ns)
                if loc_el is None:
                    loc_el = entry.find("link")
                if loc_el is None:
                    loc_el = entry.find("atom:id", ns)

                url = None
                if loc_el is not None:
                    url = (loc_el.get("href") or loc_el.text or "").strip()
                else:
                    # RSS 2.0 <link> 可能直接是文本
                    for child in entry:
                        if child.tag in ("link", "{http://www.w3.org/2005/Atom}link"):
                            url = (child.text or child.get("href") or "").strip()
                            break

                if url and url.startswith("http"):
                    yield normalize_url(url)

        except ET.ParseError as e:
            self._log.error("Failed to parse RSS: %s", e)
        except Exception as e:
            self._log.error("Error discovering blog URLs: %s", e)

    def fetch(self, url: str) -> RawDoc:
        return self._http.fetch(url)

    def parse(self, raw: RawDoc) -> ParsedArticle:
        content = extract(raw.content, raw.url)

        # 解析发布日期
        published = ""
        try:
            # 从 HTML 中找 <time datetime="...">
            m = re.search(r'<time[^>]+datetime="([^"]+)"', raw.content.decode("utf-8", errors="replace"))
            if m:
                published = m.group(1)[:10]
        except Exception:
            pass

        return ParsedArticle(
            title=content.title or raw.url,
            body=content.body,
            excerpt=content.excerpt,
            published_at=published,
            author=content.author,
            difficulty=self._guess_difficulty(content.title, content.body),
            word_count=len(content.body.split()),
        )

    def _guess_difficulty(self, title: str, body: str) -> str:
        t = (title + " " + body).lower()
        if any(k in t for k in ["announce", "release notes", "new version", "launch"]):
            return "reference"
        if any(k in t for k in ["tutorial", "how to", "step by step"]):
            return "beginner"
        return "intermediate"
