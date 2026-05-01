"""
rocm-hip-map/crawlers/base.py
Phase 2.1.1 — 爬虫基类
从 "URL 清单" 升级到真正的多源爬虫框架

模板方法 run() 已实现，子类只需实现：
  discover() → 发现待抓 URL
  fetch(url) → 抓取单页（返回 RawDoc）
  parse(raw) → 解析为 ParsedArticle
"""
from __future__ import annotations

import logging
import time as _time
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Iterator, Optional

import sys
_ROOT = __file__.rsplit("/crawlers/", 1)[0]
sys.path.insert(0, _ROOT)

from db import cursor
from db.dao import (
    article_upsert,
    crawl_log_start,
    crawl_log_finish,
    source_upsert,
    source_update_crawled,
)

logger = logging.getLogger("crawlers")


# ── 数据模型 ────────────────────────────────────────────────────────────────

@dataclass
class RawDoc:
    """原始 HTTP 响应。"""
    url: str
    status_code: int
    content: bytes
    headers: dict[str, str]
    etag: Optional[str] = None
    last_modified: Optional[str] = None

    @property
    def ok(self) -> bool:
        return 200 <= self.status_code < 300

    @property
    def not_modified(self) -> bool:
        return self.status_code == 304


@dataclass
class ParsedArticle:
    """结构化文章对象。"""
    title: str
    body: str
    excerpt: str = ""
    published_at: str = ""
    author: str = ""
    tags: list[str] = field(default_factory=list)
    difficulty: str = ""
    word_count: int = 0


# ── BaseCrawler ─────────────────────────────────────────────────────────────

class BaseCrawler(ABC):
    """
    所有爬虫的基类。

    使用模板方法模式：run() 已实现并发控制、失败重试、ETag 缓存、
    去重、爬取记录。子类只需实现 discover/fetch/parse。
    """

    # 并发控制
    rate_limit: float = 1.0   # req/sec
    max_retries: int = 3
    retry_base_delay: float = 1.0

    # 来源
    slug: str = "base"
    name: str = "Base Crawler"
    source_type: str = "other"

    # 内部状态
    _log_id: int = 0
    _total: int = 0
    _new: int = 0
    _updated: int = 0
    _skipped: int = 0
    _failed: int = 0
    _log = None

    def __init__(self):
        self._log = logger.getChild(self.slug)

    # ── 子类必须实现 ─────────────────────────────────────────────────────

    @abstractmethod
    def discover(self) -> Iterator[str]:
        """yield 所有候选 URL。"""
        ...

    @abstractmethod
    def fetch(self, url: str) -> RawDoc:
        """抓取单个 URL，返回 RawDoc。"""
        ...

    @abstractmethod
    def parse(self, raw: RawDoc) -> ParsedArticle:
        """将 RawDoc 解析为 ParsedArticle。"""
        ...

    # ── 可选覆盖 ─────────────────────────────────────────────────────────

    def normalize_url(self, url: str) -> str:
        """去除 utm_*/fbclid 等追踪参数。"""
        from urllib.parse import urlparse, urlencode, parse_qs
        parsed = urlparse(url)
        qs = {k: v for k, v in parse_qs(parsed.query).items()
              if k not in {"utm_source", "utm_medium", "utm_campaign",
                            "utm_content", "utm_term", "fbclid", "ref",
                            "mc_cid", "mc_eid"}}
        return parsed._replace(query=urlencode(qs, doseq=True)).geturl()

    def get_source_id(self) -> int | None:
        """尝试从 slug 查找 source_id。"""
        with cursor() as cur:
            cur.execute("SELECT id FROM sources WHERE slug = ?", (self.slug,))
            r = cur.fetchone()
            return r["id"] if r else None

    def is_seen(self, url: str) -> bool:
        """检查 url 是否已存在于数据库。"""
        from hashlib import sha256
        h = sha256(self.normalize_url(url).encode()).hexdigest()[:16]
        with cursor() as cur:
            cur.execute("SELECT 1 FROM articles WHERE url_hash = ?", (h,))
            return cur.fetchone() is not None

    # ── 模板方法 ─────────────────────────────────────────────────────────

    def run(self, limit: int = 0, source_id: int | None = None) -> dict:
        """
        运行爬虫主流程。

        limit: 最大抓取数（0=不限）
        source_id: 手动传入 source_id（否则从 slug 查）
        返回: {total, new, updated, skipped, failed, duration_ms}
        """
        if source_id is None:
            source_id = self.get_source_id()

        self._log_id = crawl_log_start(source_id or 0)
        started = datetime.now(timezone.utc)

        self._log.info("Starting %s", self.slug)
        seen_count = 0

        try:
            for url in self.discover():
                if limit and seen_count >= limit:
                    break

                normalized = self.normalize_url(url)
                if self.is_seen(normalized):
                    self._skipped += 1
                    self._log.debug("Skipped (seen): %s", url)
                    continue

                try:
                    article = self._fetch_and_parse(url)
                    if article is None:
                        self._failed += 1
                        continue

                    article_id, is_new = article_upsert(
                        url=url,
                        title=article.title,
                        body=article.body,
                        excerpt=article.excerpt,
                        source_type=self.source_type,
                        published_at=article.published_at,
                        difficulty=article.difficulty,
                        source_id=source_id,
                    )

                    if is_new:
                        self._new += 1
                    else:
                        self._updated += 1
                    self._total += 1

                except Exception as e:
                    self._failed += 1
                    self._log.warning("Failed %s: %s", url, e)

                seen_count += 1

                # 速率限制
                if self.rate_limit > 0:
                    _time.sleep(1.0 / self.rate_limit)

            duration_ms = int(
                (datetime.now(timezone.utc) - started).total_seconds() * 1000
            )
            crawl_log_finish(
                self._log_id,
                status="success" if self._failed == 0 else "partial",
                total=self._total,
                new_articles=self._new,
                updated=self._updated,
                skipped=self._skipped,
                failed=self._failed,
            )
            if source_id:
                source_update_crawled(source_id, self._new)

            self._log.info(
                "%s done: total=%d new=%d updated=%d skipped=%d failed=%d (%.1fs)",
                self.slug, self._total, self._new,
                self._updated, self._skipped, self._failed,
                duration_ms / 1000
            )
            return {
                "total": self._total, "new": self._new,
                "updated": self._updated, "skipped": self._skipped,
                "failed": self._failed, "duration_ms": duration_ms,
            }

        except Exception as e:
            crawl_log_finish(self._log_id, status="failed", error=str(e))
            self._log.error("Crawler failed: %s", e)
            raise

    def _fetch_and_parse(self, url: str) -> Optional[ParsedArticle]:
        """fetch + parse + 重试。"""
        for attempt in range(self.max_retries):
            try:
                raw = self.fetch(url)
                if raw.not_modified:
                    self._skipped += 1
                    return None
                if not raw.ok:
                    return None
                return self.parse(raw)
            except Exception as e:
                if attempt < self.max_retries - 1:
                    delay = self.retry_base_delay * (2 ** attempt)
                    self._log.debug("Retry %d/%d %s after %.1fs: %s",
                                   attempt + 1, self.max_retries, url, delay, e)
                    _time.sleep(delay)
                else:
                    raise
        return None
