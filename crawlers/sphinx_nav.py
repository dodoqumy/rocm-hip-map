"""
Sphinx Nav 爬虫 (Phase 2.1)
Level 2: 从 Sphinx 导航页发现 URL (无 sitemap 时 fallback)
"""

import re
from typing import List, Optional, Set
import logging

from .base import BaseCrawler, FetchResult
from .http_client import compute_content_hash

logger = logging.getLogger(__name__)


class SphinxNavCrawler(BaseCrawler):
    """从 Sphinx 导航页发现 URL"""
    
    def discover(self, max_urls: int = 500) -> List[str]:
        """发现所有 URL"""
        base = self.config.base_url
        logger.info(f"  🔍 Crawling nav: {base}")
        
        # 获取首页
        index_url = base if base.endswith("/") else base + "/"
        html = self.http.get(index_url)
        if not html:
            logger.warning(f"  ⚠ Failed to fetch index: {index_url}")
            return []
        
        # 从导航提取所有链接
        urls = set()
        urls.update(self._extract_from_toc(html, base))
        urls.update(self._extract_from_sidebar(html, base))
        
        # 递归抓取子目录
        if len(urls) < max_urls:
            for url in list(urls)[:20]:
                if self._is_category_page(url):
                    sub_urls = self._crawl_category(url, base)
                    urls.update(sub_urls)
        
        # 过滤
        urls = [u for u in urls if not self.should_skip(u)]
        
        logger.info(f"  📍 Discovered {len(urls)} URLs")
        return list(urls)[:max_urls]
    
    def _extract_from_toc(self, html: str, base: str) -> Set[str]:
        """从 TOC 提取"""
        urls = set()
        
        # toctree 链接
        for match in re.findall(r'href="(?!http|mailto:|:)([^"#]+\.html)"', html):
            if match.startswith("/"):
                url = base.strip("/") + match
            else:
                url = base.strip("/") + "/" + match
            
            if url.endswith(".html"):
                urls.add(url)
        
        # 相对链接
        for match in re.findall(r'href="([^"]*index\.html)"', html):
            url = base.strip("/") + "/" + match
            urls.add(url)
        
        return urls
    
    def _extract_from_sidebar(self, html: str, base: str) -> Set[str]:
        """从侧边栏提取"""
        return self._extract_from_toc(html, base)
    
    def _is_category_page(self, url: str) -> bool:
        """判断是否为分类页"""
        return url.endswith("/index.html") or "category" in url.lower()
    
    def _crawl_category(self, url: str, base: str) -> Set[str]:
        """抓取分类页"""
        urls = set()
        html = self.http.get(url)
        if not html:
            return urls
        
        urls.update(self._extract_from_toc(html, base))
        return urls
    
    def fetch(self, url: str) -> Optional[FetchResult]:
        """抓取单个页面"""
        self.http.rate_limit_per_domain(self.domain)
        
        html = self.http.get(url)
        if not html:
            return None
        
        # 提取标题
        title_match = re.search(r"<title>([^<]+)</title>", html, re.IGNORECASE)
        title = title_match.group(1) if title_match else ""
        if "—" in title:
            title = title.split("—")[0].strip()
        
        content = self.extractor.extract(html, url)
        if not content:
            content = html
        
        return FetchResult(
            url=url,
            content=content,
            title=title,
            content_hash=compute_content_hash(content),
        )