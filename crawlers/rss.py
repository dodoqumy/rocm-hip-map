"""
RSS/Atom 爬虫 (Phase 2.1)
用于博客、新闻源
"""

import re
from typing import List, Optional
import logging
from datetime import datetime

from .base import BaseCrawler, FetchResult

logger = logging.getLogger(__name__)


class RSSCrawler(BaseCrawler):
    """RSS/Atom 爬虫"""
    
    def discover(self, max_urls: int = 50) -> List[str]:
        """发现 RSS/Atom feed"""
        base = self.config.base_url
        
        # 尝试常见 feed 位置
        feed_urls = [
            base + "feed/",
            base + "feed.xml",
            base + "atom.xml",
            base + "rss.xml",
        ]
        
        for url in feed_urls:
            html = self.http.get(url)
            if html and ("<rss" in html.lower() or "<feed" in html.lower()):
                return self._parse_rss(html)
        
        # 尝试从首页发现
        html = self.http.get(base)
        if not html:
            return []
        
        # 查找 link rel="alternate" type="application/rss+xml" or atom
        feeds = re.findall(r'href="([^"]*feed[^"]*)"', html, re.IGNORECASE)
        feeds += re.findall(r'href="([^"]*\\.(?:xml|rss|atom))"', html, re.IGNORECASE)
        # Also check for link tags with type attribute
        feeds += re.findall(r'<link[^>]*href="([^"]*)"[^>]*type="application/(?:rss|atom)\+xml"', html, re.IGNORECASE)
        feeds += re.findall(r'type="application/(?:rss|atom)\+xml"[^>]*href="([^"]*)"', html, re.IGNORECASE)
        
        # Remove duplicates while preserving order
        seen = set()
        unique_feeds = []
        for f in feeds:
            if f not in seen:
                seen.add(f)
                unique_feeds.append(f)
        
        urls = []
        for feed in unique_feeds[:5]:
            if not feed.startswith("http"):
                feed = base.rstrip("/") + "/" + feed.lstrip("/")
            
            html = self.http.get(feed)
            if html:
                urls.extend(self._parse_rss(html))
        
        return urls[:max_urls]
    
    def _parse_rss(self, html: str) -> List[str]:
        """解析 RSS/Atom feed"""
        urls = []
        
        # RSS 2.0: <item><link>url</link>
        for match in re.findall(r"<link>([^<]+)</link>", html, re.IGNORECASE):
            if match and match not in urls:
                urls.append(match)
        
        # Atom: <entry><link href="url"/> or <link href="url" />
        for match in re.findall(r'<entry[^>]*>.*?<link\s+href="([^"]+)"', html, re.IGNORECASE | re.DOTALL):
            if match and match not in urls:
                urls.append(match)
        
        # Atom (alternate format): <link href="url" rel="alternate"> in entry context
        for match in re.findall(r'<entry[^>]*>.*?<link[^>]*href="([^"]+)"[^>]*rel="alternate"', html, re.IGNORECASE | re.DOTALL):
            if match and match not in urls:
                urls.append(match)
        
        return urls
    
    def fetch(self, url: str) -> Optional[FetchResult]:
        """抓取文章"""
        self.http.rate_limit_per_domain(self.domain)
        
        html = self.http.get(url)
        if not html:
            return None
        
        # 标题
        title_match = re.search(r"<title>([^<]+)</title>", html, re.IGNORECASE)
        title = title_match.group(1) if title_match else ""
        
        content = self.extractor.extract(html, url)
        if not content:
            content = html
        
        return FetchResult(
            url=url,
            content=content,
            title=title,
        )