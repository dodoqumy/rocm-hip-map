"""
rocm-hip-map/db/dao.py
数据访问对象 — Phase 2.0.0
所有数据库操作必须经过此模块，禁止直接操作 sqlite3
"""
from __future__ import annotations

import hashlib
import json
import re
import textwrap
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional, Any

from . import get_connection, transaction, cursor

# ── URL 规范化 ────────────────────────────────────────────────────────────────


def normalize_url(url: str) -> str:
    """去除 utm_*/fbclid/ref 等追踪参数，用于去重。"""
    url = re.sub(r"[?&](utm_|fbclid|ref|mc_cid|mc_eid|ref_src|ref_url)=[^&]+", "", url)
    url = url.rstrip("?")
    return url


def url_hash(url: str) -> str:
    """返回规范化 URL 的 sha256 前 16 位。"""
    return hashlib.sha256(normalize_url(url).encode()).hexdigest()[:16]


def content_hash(content: str) -> str:
    """返回内容 sha256 前 16 位（用于变更检测）。"""
    return hashlib.sha256(content.encode()).hexdigest()[:16]


# ────────────────────────────────────────────────────────────────────────────
# Article DAO
# ────────────────────────────────────────────────────────────────────────────

def slug_from_title(title: str) -> str:
    """从标题生成 URL-safe slug。"""
    slug = re.sub(r"[^\w\s-]", "", title.lower())
    slug = re.sub(r"[\s_]+", "-", slug)
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug[:80]


def article_upsert(
    *,
    url: str,
    title: str,
    body: str = "",
    excerpt: str = "",
    source_id: int | None = None,
    source_url: str = "",
    source_type: str = "other",
    source_org: str = "",
    credibility: int = 3,
    lifecycle: str = "latest",
    difficulty: str = "",
    published_at: str = "",
    etag: str = "",
    last_modified: str = "",
    http_status: int = 200,
    **extra: Any,
) -> tuple[int, bool]:
    """
    插入或更新文章。

    返回 (id, is_new)
      - is_new=True  表示这是新发现 URL
      - is_new=False 表示内容有更新（body_changed=True）

    变更检测：url_hash 存在时比较 content_hash
    """
    conn = get_connection()
    normalized_url = normalize_url(url)
    u_hash = url_hash(normalized_url)
    c_hash = content_hash(body)
    slug = slug_from_title(title)
    word_count = len(body.split()) if body else 0
    char_count = len(body) if body else 0
    has_code = 1 if body and ("```" in body or "<pre>" in body) else 0
    has_benchmark = 1 if body and any(
        re.search(r"(\d+\.?\d*)\s*(ms|tok/s|GB/s|%|fps|TOPS)", body)
        for _ in [1]
    ) else 0
    now = datetime.now(timezone.utc).isoformat()

    # 先查 url_hash 是否存在
    with cursor() as cur:
        cur.execute("SELECT id, content_hash FROM articles WHERE url_hash = ?", (u_hash,))
        row = cur.fetchone()

    if row:
        # 内容无变化，跳过
        if row["content_hash"] == c_hash:
            return row["id"], False
        # 有变化，更新
        cur2 = conn.execute(
            """UPDATE articles SET
                title=?, slug=?, body=?, excerpt=?,
                content_hash=?, word_count=?, char_count=?,
                has_code=?, has_benchmark=?,
                published_at=?, updated_at=?, fetched_at=?,
                etag=?, last_modified=?, http_status=?
               WHERE url_hash=?""",
            (title, slug, body, excerpt[:200],
             c_hash, word_count, char_count,
             has_code, has_benchmark,
             published_at or None, now, now,
             etag or None, last_modified or None, http_status,
             u_hash),
        )
        return row["id"], False

    # 新插入
    cur2 = conn.execute(
        """INSERT INTO articles
           (url, url_hash, title, slug, body, excerpt,
            content_hash, word_count, char_count, has_code, has_benchmark,
            source_id, source_url, source_type, source_org, credibility,
            lifecycle, difficulty, published_at,
            etag, last_modified, http_status,
            status, discovered_at, fetched_at, updated_at)
           VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
        (url, u_hash, title, slug, body, excerpt[:200],
         c_hash, word_count, char_count, has_code, has_benchmark,
         source_id, source_url, source_type, source_org, credibility,
         lifecycle, difficulty or None, published_at or None,
         etag or None, last_modified or None, http_status,
         "discovered", now, now, now),
    )
    return cur2.lastrowid, True


def article_get_by_hash(url_hash: str) -> dict | None:
    """通过 url_hash 查单篇。"""
    with cursor() as cur:
        cur.execute("SELECT * FROM articles WHERE url_hash = ?", (url_hash,))
        return dict(cur.fetchone()) if cur.fetchone() else None


def article_find_stale(days: int = 7, limit: int = 100) -> list[dict]:
    """找 N 天内未更新的文章（用于重抓）。"""
    cutoff = (datetime.now(timezone.utc) - timedelta(days=days)).isoformat()
    with cursor() as cur:
        cur.execute(
            """SELECT id, url, url_hash, title FROM articles
               WHERE updated_at < ? AND status != 'error'
               ORDER BY updated_at ASC LIMIT ?""",
            (cutoff, limit),
        )
        return [dict(r) for r in cur.fetchall()]


def article_set_status(
    article_id: int,
    status: str,
    error_message: str = "",
) -> None:
    """更新文章状态。"""
    conn = get_connection()
    conn.execute(
        "UPDATE articles SET status=?, error_message=? WHERE id=?",
        (status, error_message, article_id),
    )


def article_get_by_id(article_id: int) -> dict | None:
    """查单篇。"""
    with cursor() as cur:
        cur.execute("SELECT * FROM articles WHERE id = ?", (article_id,))
        return dict(cur.fetchone()) if cur.fetchone() else None


def article_count(status: str | None = None) -> int:
    """文章总数（可按状态过滤）。"""
    with cursor() as cur:
        if status:
            cur.execute("SELECT COUNT(*) FROM articles WHERE status = ?", (status,))
        else:
            cur.execute("SELECT COUNT(*) FROM articles")
        return cur.fetchone()[0]


def article_list(
    is_indexed: bool | None = None,
    source_type: str | None = None,
    limit: int = 100,
    offset: int = 0,
) -> list[dict]:
    """分页查询文章列表。"""
    where = []
    params = []
    if is_indexed is not None:
        where.append("is_indexed = ?")
        params.append(1 if is_indexed else 0)
    if source_type:
        where.append("source_type = ?")
        params.append(source_type)

    where_sql = "WHERE " + " AND ".join(where) if where else ""
    with cursor() as cur:
        cur.execute(
            f"""SELECT id, url_hash, title, slug, source_type, source_org,
                       credibility, lifecycle, difficulty, quality_score,
                       word_count, has_translation, status, discovered_at, published_at
                FROM articles
                {where_sql}
                ORDER BY discovered_at DESC
                LIMIT ? OFFSET ?""",
            (*params, limit, offset),
        )
        return [dict(r) for r in cur.fetchall()]


# ────────────────────────────────────────────────────────────────────────────
# Source DAO
# ────────────────────────────────────────────────────────────────────────────

INTERVAL_MAP = {
    "30m": 30,
    "1h": 60,
    "2h": 120,
    "6h": 360,
    "12h": 720,
    "1d": 1440,
}


def source_upsert(
    *,
    slug: str,
    name: str,
    source_type: str,
    base_url: str = "",
    rate_limit_hz: float = 1.0,
    crawl_interval: str = "6h",
    priority: str = "medium",
) -> int:
    """Upsert source，返回 id。"""
    conn = get_connection()
    cur = conn.execute(
        """INSERT INTO sources (slug, name, source_type, base_url, rate_limit_hz,
                                crawl_interval, priority, created_at, updated_at)
           VALUES (?,?,?,?,?,?,?,?,?)
           ON CONFLICT(slug) DO UPDATE SET
               name=excluded.name, source_type=excluded.source_type,
               base_url=excluded.base_url, rate_limit_hz=excluded.rate_limit_hz,
               crawl_interval=excluded.crawl_interval, priority=excluded.priority,
               updated_at=excluded.updated_at""",
        (slug, name, source_type, base_url, rate_limit_hz,
         crawl_interval, priority,
         datetime.now(timezone.utc).isoformat(),
         datetime.now(timezone.utc).isoformat()),
    )
    return conn.execute(
        "SELECT id FROM sources WHERE slug = ?", (slug,)
    ).fetchone()["id"]


def source_due_for_crawl(limit: int = 5) -> list[dict]:
    """返回应该立即抓取的 source 列表（按优先级排序）。"""
    now = datetime.now(timezone.utc).isoformat()
    with cursor() as cur:
        cur.execute(
            """SELECT * FROM sources
               WHERE enabled = 1 AND (next_crawl_at IS NULL OR next_crawl_at <= ?)
               ORDER BY
                   CASE priority
                       WHEN 'critical' THEN 1 WHEN 'high' THEN 2
                       WHEN 'medium' THEN 3 WHEN 'low' THEN 4
                   END ASC,
                   next_crawl_at ASC NULLS FIRST
               LIMIT ?""",
            (now, limit),
        )
        return [dict(r) for r in cur.fetchall()]


def source_update_crawled(source_id: int, new_article_count: int = 0) -> None:
    """更新 source 抓取时间并计算下次抓取时间。"""
    conn = get_connection()
    cur = conn.execute("SELECT crawl_interval FROM sources WHERE id = ?", (source_id,))
    row = cur.fetchone()
    if not row:
        return
    interval_min = INTERVAL_MAP.get(row["crawl_interval"], 360)
    next_time = datetime.now(timezone.utc) + timedelta(minutes=interval_min)
    conn.execute(
        """UPDATE sources SET
               last_crawled_at=?,
               next_crawl_at=?,
               updated_at=?
           WHERE id=?""",
        (datetime.now(timezone.utc).isoformat(),
         next_time.isoformat(),
         datetime.now(timezone.utc).isoformat(),
         source_id),
    )


# ────────────────────────────────────────────────────────────────────────────
# Tag DAO
# ────────────────────────────────────────────────────────────────────────────

def tag_upsert(
    *,
    tag: str,
    namespace: str,
    label: str = "",
    label_zh: str = "",
    description: str = "",
    gfx_target: str = "",
    gfx_generation: str = "",
    color: str = "",
) -> int:
    """Upsert tag，返回 id。"""
    conn = get_connection()
    conn.execute(
        """INSERT INTO tags (tag, namespace, label, label_zh, description,
                            gfx_target, gfx_generation, color, created_at)
           VALUES (?,?,?,?,?,?,?,?,?)
           ON CONFLICT(tag) DO UPDATE SET
               label=excluded.label, label_zh=excluded.label_zh,
               description=excluded.description,
               gfx_target=excluded.gfx_target,
               gfx_generation=excluded.gfx_generation,
               color=excluded.color""",
        (tag, namespace, label or tag, label_zh or label, description,
         gfx_target or None, gfx_generation or None, color or None,
         datetime.now(timezone.utc).isoformat()),
    )
    return conn.execute("SELECT id FROM tags WHERE tag = ?", (tag,)).fetchone()["id"]


def tag_add_to_article(
    article_id: int,
    tag_id: int,
    confidence: float = 1.0,
    method: str = "rule",
) -> None:
    """关联 article-tag（幂等）。"""
    conn = get_connection()
    conn.execute(
        """INSERT INTO article_tags (article_id, tag_id, confidence, method, created_at)
           VALUES (?,?,?,?,?)
           ON CONFLICT(article_id, tag_id) DO UPDATE SET
               confidence=excluded.confidence, method=excluded.method""",
        (article_id, tag_id, confidence, method, datetime.now(timezone.utc).isoformat()),
    )


def tag_get_by_namespace(ns: str) -> list[dict]:
    """按命名空间查所有标签。"""
    with cursor() as cur:
        cur.execute("SELECT * FROM tags WHERE namespace = ? ORDER BY tag", (ns,))
        return [dict(r) for r in cur.fetchall()]


def article_get_tags(article_id: int) -> list[dict]:
    """查某文章的所有标签。"""
    with cursor() as cur:
        cur.execute(
            """SELECT t.*, at.confidence, at.method
               FROM article_tags at
               JOIN tags t ON t.id = at.tag_id
               WHERE at.article_id = ?
               ORDER BY t.namespace, t.tag""",
            (article_id,),
        )
        return [dict(r) for r in cur.fetchall()]


def tag_get_or_create(tag: str, namespace: str, **kw) -> int:
    """获取或创建标签，返回 id。"""
    with cursor() as cur:
        cur.execute("SELECT id FROM tags WHERE tag = ?", (tag,))
        row = cur.fetchone()
    if row:
        return row["id"]
    return tag_upsert(tag=tag, namespace=namespace, **kw)


# ────────────────────────────────────────────────────────────────────────────
# CrawlLog DAO
# ────────────────────────────────────────────────────────────────────────────

def crawl_log_start(source_id: int) -> int:
    """开始一次爬取记录，返回 log_id。"""
    conn = get_connection()
    cur = conn.execute(
        """INSERT INTO crawl_log (source_id, started_at, status, is_incremental)
           VALUES (?, ?, 'running', 1)""",
        (source_id, datetime.now(timezone.utc).isoformat()),
    )
    return cur.lastrowid


def crawl_log_finish(
    log_id: int,
    status: str,
    total: int = 0,
    new_articles: int = 0,
    updated: int = 0,
    skipped: int = 0,
    failed: int = 0,
    error: str = "",
) -> None:
    """结束爬取记录。"""
    conn = get_connection()
    now = datetime.now(timezone.utc).isoformat()
    conn.execute(
        """UPDATE crawl_log SET
               finished_at=?, status=?, total_urls=?,
               new_articles=?, updated_articles=?,
               skipped_304=?, failed=?, error_message=?,
               duration_ms=? WHERE id=?""",
        (now, status, total, new_articles, updated, skipped, failed,
         error, (datetime.now(timezone.utc) -
                 datetime.fromisoformat(
                     conn.execute("SELECT started_at FROM crawl_log WHERE id=?", (log_id,))
                     .fetchone()["started_at"]
                 )).total_seconds() * 1000 if log_id else 0,
         log_id),
    )


# ────────────────────────────────────────────────────────────────────────────
# Papers DAO
# ────────────────────────────────────────────────────────────────────────────

def paper_upsert(
    *,
    arxiv_id: str,
    title: str,
    authors: str = "",
    abstract: str = "",
    published_at: str = "",
    categories: str = "",
    pdf_url: str = "",
    source_url: str = "",
) -> int:
    """Upsert paper，返回 id。"""
    conn = get_connection()
    conn.execute(
        """INSERT INTO papers (arxiv_id, title, authors, abstract, published_at,
                               categories, pdf_url, source_url, created_at, updated_at)
           VALUES (?,?,?,?,?,?,?,?,?,?)
           ON CONFLICT(arxiv_id) DO UPDATE SET
               title=excluded.title, authors=excluded.authors,
               abstract=excluded.abstract, published_at=excluded.published_at,
               categories=excluded.categories, pdf_url=excluded.pdf_url,
               source_url=excluded.source_url, updated_at=excluded.updated_at""",
        (arxiv_id, title, authors, abstract, published_at,
         categories, pdf_url, source_url,
         datetime.now(timezone.utc).isoformat(),
         datetime.now(timezone.utc).isoformat()),
    )
    return conn.execute(
        "SELECT id FROM papers WHERE arxiv_id = ?", (arxiv_id,)
    ).fetchone()["id"]


# ────────────────────────────────────────────────────────────────────────────
# Known Issues DAO
# ────────────────────────────────────────────────────────────────────────────

def known_issue_upsert(
    *,
    title: str = "",
    component: str = "",
    status: str = "open",
    rocm_version: str = "",
    gpu: str = "",
    os: str = "",
    source_url: str = "",
    summary: str = "",
    workaround: str = "",
) -> int:
    """Upsert known issue，返回 id。"""
    conn = get_connection()
    conn.execute(
        """INSERT INTO known_issues
           (title, component, status, rocm_version, gpu, os,
            source_url, summary, workaround, created_at)
           VALUES (?,?,?,?,?,?,?,?,?,?)
           ON CONFLICT(source_url) DO UPDATE SET
               title=excluded.title, component=excluded.component,
               status=excluded.status, rocm_version=excluded.rocm_version,
               gpu=excluded.gpu, os=excluded.os,
               summary=excluded.summary, workaround=excluded.workaround""",
        (title, component, status, rocm_version, gpu, os,
         source_url, summary, workaround,
         datetime.now(timezone.utc).isoformat()),
    )
    # 尝试查 id（ON CONFLICT DO NOTHING 时可能没插入）
    row = conn.execute(
        "SELECT id FROM known_issues WHERE source_url = ?", (source_url,)
    ).fetchone()
    return row["id"] if row else 0


# ────────────────────────────────────────────────────────────────────────────
# CUDA→HIP Map DAO
# ────────────────────────────────────────────────────────────────────────────

def cuda_hip_map_bulk_insert(mappings: list[dict]) -> int:
    """批量导入 304 条 CUDA→HIP 映射。"""
    conn = get_connection()
    inserted = 0
    for m in mappings:
        cur = conn.execute(
            """INSERT OR IGNORE INTO cuda_hip_map
               (cuda_api, hip_api, category, status, rocm_version, source_url, notes)
               VALUES (?,?,?,?,?,?,?)""",
            (m.get("cuda", ""), m.get("hip", ""), m.get("category", ""),
             m.get("status", "supported"), m.get("rocm_version", ""),
             m.get("source_url", ""), m.get("notes", "")),
        )
        inserted += cur.rowcount
    return inserted
