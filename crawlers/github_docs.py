"""
GitHub Docs 爬虫 (Phase 2.1)
Level 3: 从 GitHub 源码 docs/ 目录抓取
"""

import re
from typing import List, Optional
import logging

from .base import BaseCrawler, FetchResult
from .http_client import HTTPClient

logger = logging.getLogger(__name__)


class GithubDocsCrawler(BaseCrawler):
    """从 GitHub 源码 docs/ 抓取"""
    
    def __init__(self, config, http_client):
        super().__init__(config, http_client)
        self.repo = self._extract_repo(config.base_url)
    
    def _extract_repo(self, url: str) -> str:
        """从 URL 提取 repo"""
        # https://github.com/ROCm/rocBLAS/tree/master/docs
        match = re.search(r"github\.com/([^/]+/[^/]+)", url)
        return match.group(1) if match else ""
    
    def discover(self, max_urls: int = 200) -> List[str]:
        """发现 docs/ 目录内容"""
        if not self.repo:
            return []
        
        # Tree API
        api_url = f"https://api.github.com/repos/{self.repo}/contents/docs"
        
        resp = self.http.http.get(api_url)
        if not resp:
            logger.warning(f"  ⚠ No docs dir: {self.repo}")
            return []
        
        import json
        try:
            items = json.loads(resp)
        except:
            return []
        
        urls = []
        for item in items:
            if item["type"] == "file" and item["name"].endswith((".md", ".rst")):
                # 获取原始内容
                raw_url = item.get("download_url") or item.get("content")
                urls.append(raw_url)
        
        return urls[:max_urls]
    
    def fetch(self, url: str) -> Optional[FetchResult]:
        """抓取单个文件"""
        self.http.rate_limit_per_domain("github.com")
        
        resp = self.http.http.get(url)
        if not resp:
            return None
        
        # 标题
        title = url.split("/")[-1]
        if title.endswith(".md"):
            title = title[:-3]
        elif title.endswith(".rst"):
            title = title[:-4]
        
        return FetchResult(
            url=url,
            content=resp,
            title=title,
        )