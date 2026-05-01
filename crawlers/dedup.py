"""
URL 去重与规范化 (Phase 2.1)
"""

import re
import hashlib
from urllib.parse import urlparse, urljoin
from typing import Set, Optional


def normalize_url(url: str) -> str:
    """URL 基本规范化"""
    # 移除 utm 参数
    url = re.sub(r"utm_[^=]+=[^&]+&?", "", url)
    url = re.sub(r"fbclid=[^&]+&?", "", url)
    url = re.sub(r"ref[^=]+=[^&]+&?", "", url)
    
    # 移除尾随 &
    url = url.rstrip("&")
    
    # 移除空参数
    url = re.sub(r"\?$", "", url)
    
    return url


def url_to_filename(url: str) -> str:
    """URL 转文件名"""
    # https://rocm.docs.amd.com/en/latest/about/license.html
    # → about_license
    parsed = urlparse(url)
    path = parsed.path
    
    # 移除版本前缀
    path = re.sub(r"/en/(?:latest|docs-[\d.]+)/", "/", path)
    path = re.sub(r"/projects/[\w-]+/en/latest/", "/", path)
    
    # 移除扩展名和目录
    path = path.strip("/")
    path = re.sub(r"\.html?$", "", path)
    path = re.sub(r"index$", "", path)
    
    # 转义
    path = path.replace("/", "_")
    path = path.replace("-", "_")
    path = path.replace(".", "_")
    
    return path


def compute_url_hash(url: str) -> str:
    """URL hash (去重)"""
    normalized = normalize_url(url)
    return hashlib.md5(normalized.encode()).hexdigest()[:16]


def compute_content_hash(content: str) -> str:
    """Content hash (增量)"""
    return hashlib.sha256(content.encode()).hexdigest()[:16]


class Deduplicator:
    """去重器"""
    
    def __init__(self):
        self._seen_urls: Set[str] = set()
        self._seen_content: Set[str] = set()
    
    def is_seen(self, url: str) -> bool:
        """URL 已存在"""
        url_hash = compute_url_hash(url)
        if url_hash in self._seen_urls:
            return True
        self._seen_urls.add(url_hash)
        return False
    
    def is_content_unchanged(self, content: str) -> bool:
        """内容未变"""
        content_hash = compute_content_hash(content)
        if content_hash in self._seen_content:
            return True
        self._seen_content.add(content_hash)
        return False
    
    def load_state(self, state: dict):
        """加载状态"""
        self._seen_urls = set(state.get("urls", []))
        self._seen_content = set(state.get("content", []))
    
    def save_state(self) -> dict:
        """保存状态"""
        return {
            "urls": list(self._seen_urls),
            "content": list(self._seen_content),
        }