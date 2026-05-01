"""
rocm-hip-map/crawlers/http_client.py
Phase 2.1.1 — HTTP 客户端（httpx + 重试 + ETag）
"""
from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Optional

import httpx

from .base import RawDoc


_USER_AGENTS = [
    "Mozilla/5.0 (compatible; rocm-hip-map/2.0; +https://github.com/dodoqumy/rocm-hip-map)",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
]


@dataclass
class HttpClient:
    """
    线程安全的 HTTP 客户端。

    - 连接池（httpx）
    - ETag / Last-Modified 缓存
    - 指数退避重试
    - User-Agent 轮换
    """
    timeout: float = 15.0
    max_retries: int = 3
    retry_delay: float = 1.0

    # ETag 缓存
    _etag_cache: dict = field(default_factory=dict)
    _ua_index: int = 0

    def _headers(self, url: str) -> dict[str, str]:
        """构造请求头（带条件请求）。"""
        ua = _USER_AGENTS[self._ua_index % len(_USER_AGENTS)]
        headers = {
            "User-Agent": ua,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
        }
        cached = self._etag_cache.get(url)
        if cached:
            if cached.get("etag"):
                headers["If-None-Match"] = cached["etag"]
            if cached.get("last_modified"):
                headers["If-Modified-Since"] = cached["last_modified"]
        return headers

    def fetch(self, url: str) -> RawDoc:
        """同步 fetch（支持重试）。"""
        headers = self._headers(url)

        for attempt in range(self.max_retries):
            try:
                response = httpx.get(
                    url,
                    headers=headers,
                    timeout=self.timeout,
                    follow_redirects=True,
                )

                # 更新 ETag 缓存
                etag = response.headers.get("etag", "").strip('"') or None
                lm = response.headers.get("last-modified") or None
                if etag or lm:
                    self._etag_cache[url] = {"etag": etag, "last_modified": lm}

                return RawDoc(
                    url=url,
                    status_code=response.status_code,
                    content=response.content,
                    headers=dict(response.headers),
                    etag=etag,
                    last_modified=lm,
                )

            except (httpx.TimeoutException, httpx.ConnectError,
                    httpx.NetworkError) as e:
                if attempt < self.max_retries - 1:
                    delay = self.retry_delay * (2 ** attempt)
                    time.sleep(delay)
                else:
                    raise

        raise RuntimeError(f"Failed after {self.max_retries} retries: {url}")

    def fetch_all(self, urls: list[str]) -> list[RawDoc]:
        """串行批量 fetch。"""
        results = []
        for url in urls:
            try:
                results.append(self.fetch(url))
            except Exception:
                results.append(
                    RawDoc(url=url, status_code=0, content=b"", headers={})
                )
        return results
