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
        """发现 RSS feed"""
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
            if html and "<rss" in html.lower():
                return self._parse_rss(html)
        
        # 尝试从首页发现
        html = self.http.get(base)
        if not html:
            return []
        
        # 查找 link rel="alternate" type="application/rss+xml"
        feeds = re.findall(r'href="([^"]*feed[^"]*)"', html, re.IGNORECASE)
        feeds += re.findall(r'href="([^"]*\.xml)"', html)
        
        urls = []
        for feed in feeds[:5]:
            if not feed.startswith("http"):
                feed = base.strip("/") + "/" + feed
            
            html = self.http.get(feed)
            if html:
                urls.extend(self._parse_rss(html))
        
        return urls[:max_urls]
    
    def _parse_rss(self, html: str) -> List[str]:
        """解析 RSS"""
        urls = []
        
        # item > link
        for match in re.findall(r"<link>([^<]+)</link>", html):
            if match:
                urls.append(match)
        
        for match in re.findall(r"<link>([^<]+)</link>", html, re.IGNORECASE):
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