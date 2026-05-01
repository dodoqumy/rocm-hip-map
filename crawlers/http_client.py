"""
HTTP 客户端 (Phase 2.1)
支持速率限制、ETag 缓存、重试
"""

import httpx
import time
import hashlib
from typing import Optional, Dict
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


class DomainRateLimiter:
    """按域名全局限速"""
    _limiters: Dict[str, float] = {}
    
    @classmethod
    def wait(cls, domain: str, rate_limit: float = 1.0):
        """等待直到允许发送请求"""
        now = time.time()
        last_request = cls._limiters.get(domain, 0)
        elapsed = now - last_request
        
        if elapsed < rate_limit:
            time.sleep(rate_limit - elapsed)
        
        cls._limiters[domain] = time.time()


class HTTPClient:
    """HTTP 客户端封装"""
    
    def __init__(self, rate_limit: float = 1.0, user_agent: str = "rocm-hip-map/0.2"):
        self.rate_limit = rate_limit
        self.user_agent = user_agent
        self._etag_cache: Dict[str, str] = {}
        self._last_modified: Dict[str, str] = {}
        self._last_response: str = ""
        
    def get(self, url: str, check_etag: bool = True) -> Optional[str]:
        """GET 请求"""
        headers = {
            "User-Agent": self.user_agent,
        }
        
        # ETag 检查
        if check_etag and url in self._etag_cache:
            headers["If-None-Match"] = self._etag_cache[url]
        if check_etag and url in self._last_modified:
            headers["If-Modified-Since"] = self._last_modified[url]
        
        try:
            resp = httpx.get(url, headers=headers, timeout=30, follow_redirects=True)
            
            # 保存响应文本 (用于 sitemap 解析)
            self._last_response = resp.text
            
            if resp.status_code == 304:
                logger.debug(f"  ⏭ ETag 304: {url}")
                return None  # 未变
            
            if resp.status_code != 200:
                logger.warning(f"  ⚠ HTTP {resp.status_code}: {url}")
                return None
            
            # 缓存 ETag / Last-Modified
            etag = resp.headers.get("ETag")
            if etag:
                self._etag_cache[url] = etag
            
            last_modified = resp.headers.get("Last-Modified")
            if last_modified:
                self._last_modified[url] = last_modified
            
            return resp.text
            
        except httpx.Timeout:
            logger.warning(f"  ⚠ Timeout: {url}")
            return None
        except Exception as e:
            logger.error(f"  ⚠ Error: {url} - {e}")
            return None
    
    def head(self, url: str) -> Optional[Dict]:
        """HEAD 请求 (探测)"""
        try:
            resp = httpx.head(url, timeout=10)
            return {"status": resp.status_code, "headers": dict(resp.headers)}
        except:
            return None
    
    def rate_limit_per_domain(self, domain: str):
        """按域名限速"""
        DomainRateLimiter.wait(domain, self.rate_limit)


def compute_content_hash(content: str) -> str:
    """计算内容 SHA256 前 16 位"""
    return hashlib.sha256(content.encode()).hexdigest()[:16]