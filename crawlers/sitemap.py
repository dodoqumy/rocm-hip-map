"""
Sitemap 爬虫 (Phase 2.1)
Level 1: 从 sitemap.xml 发现 URL
"""

import re
import xml.etree.ElementTree as ET
from typing import List, Optional
import logging

from .base import BaseCrawler, FetchResult
from .http_client import compute_content_hash

logger = logging.getLogger(__name__)


class SitemapCrawler(BaseCrawler):
    """从 sitemap.xml 发现 URL"""
    
    def discover(self, max_urls: int = 500) -> List[str]:
        """发现所有 URL"""
        sitemap_url = self.config.sitemap
        if not sitemap_url:
            sitemap_url = self.config.base_url + "sitemap.xml"
        
        logger.info(f"  🗺️ Fetching sitemap: {sitemap_url}")
        
        html = self.http.get(sitemap_url)
        if not html:
            logger.warning(f"  ⚠ No sitemap: {sitemap_url}")
            return []
        
        try:
            root = ET.fromstring(html)
        except ET.ParseError:
            logger.warning(f"  ⚠ Invalid XML: {sitemap_url}")
            return []
        
        # 解析 namespace
        ns = {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        
        urls = []
        
        # 处理 sitemap index
        if root.tag == "{http://www.sitemaps.org/schemas/sitemap/0.9}sitemapindex":
            for sub in root.findall("ns:sitemap", ns) or root.findall("sitemap"):
                loc = sub.find("ns:loc", ns) or sub.find("loc")
                if loc is None:
                    continue
                
                sub_url = loc.text.strip()
                if self._should_skip_sub_sitemap(sub_url):
                    continue
                
                sub_html = self.http.get(sub_url)
                if not sub_html:
                    continue
                
                try:
                    sub_root = ET.fromstring(sub_html)
                    urls.extend(self._extract_urls(sub_root))
                except:
                    pass
        else:
            # 直接 urlset
            urls = self._extract_urls(root)
        
        # 过滤并修复 URL 格式 (/en/latest/en/7.2.2 → /en/latest/)
        import re
        fixed_urls = []
        for url in urls:
            # /en/latest/en/7.2.2/xxx → /en/latest/xxx
            fixed = re.sub(r'(/en/latest)/en/\d+\.\d+\.\d+(/)', r'\1\2', url)
            fixed_urls.append(fixed)
        
        # 去重
        fixed_urls = list(set(fixed_urls))
        
        logger.info(f"  📍 Found {len(fixed_urls)} URLs (URLs fixed)")
        return fixed_urls[:max_urls]
    
    def _should_skip_sub_sitemap(self, url: str) -> bool:
        """跳过非文档的子 sitemap"""
        skip = ["python", "json", "doxygen", "api"]
        return any(s in url.lower() for s in skip)
    
    def _extract_urls(self, root) -> List[str]:
        """从 urlset 提取 URL - 使用 regex 更可靠"""
        import re
        
        # 直接从 XML 文本提取 (绕过 ET namespace 问题)
        xml_text = self.http._last_response  # 需要修改 HTTP client
        if not xml_text:
            return []
        
        # 简单 regex 提取
        locations = re.findall(r'<loc>([^<]+)</loc>', xml_text)
        
        urls = []
        for url in locations:
            url = url.strip()
            if not url.endswith(".html"):
                continue
            
            # 过滤 404/search/genindex
            if "/404." in url or "/search.html" in url or "/genindex." in url:
                continue
            
            urls.append(url)
        
        return urls
    
    def fetch(self, url: str) -> Optional[FetchResult]:
        """抓取单个页面"""
        # 速率限制
        self.http.rate_limit_per_domain(self.domain)
        
        html = self.http.get(url)
        if not html:
            return None
        
        # 提取标题
        title_match = re.search(r"<title>([^<]+)</title>", html, re.IGNORECASE)
        title = title_match.group(1) if title_match else ""
        if "—" in title:
            title = title.split("—")[0].strip()
        if "|" in title:
            title = title.split("|")[0].strip()
        
        # 提取内容
        content = self.extractor.extract(html, url)
        if not content:
            content = html  # fallback
        
        return FetchResult(
            url=url,
            content=content,
            title=title,
            content_hash=compute_content_hash(content),
        )