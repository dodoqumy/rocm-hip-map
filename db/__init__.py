"""
rocm-hip-map/db/
SQLite 数据库层 — Phase 2.0.0
WAL 模式 + 连接池（thread-local）
"""
from __future__ import annotations

import sqlite3
import threading
import os
from pathlib import Path
from contextlib import contextmanager
from typing import Generator, Any

# ── 路径常量（.resolve() 硬编码，禁止相对路径） ──────────────────────────────
_DB_DIR = (Path(__file__).parent.parent / "data").resolve()
_DB_PATH = (_DB_DIR / "rocm-hip-map.db").resolve()

# 确保 data/ 目录存在
_DB_DIR.mkdir(parents=True, exist_ok=True)

# ── Thread-local 连接池 ────────────────────────────────────────────────────────
_local = threading.local()


def get_connection() -> sqlite3.Connection:
    """获取当前线程的 SQLite 连接（WAL 模式，单例）。"""
    if not hasattr(_local, "conn") or _local.conn is None:
        conn = sqlite3.connect(
            str(_DB_PATH),
            timeout=30.0,
            isolation_level=None,          # autocommit off（事务由代码控制）
            check_same_thread=False,      # 允许跨线程持有（但每线程独立）
        )
        conn.row_factory = sqlite3.Row   # 返回字典行
        # 每次新建连接都确保 WAL + 外键
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA foreign_keys=ON")
        conn.execute("PRAGMA busy_timeout=30000")
        conn.execute("PRAGMA synchronous=NORMAL")
        conn.execute("PRAGMA cache_size=-64000")   # 64MB cache
        conn.execute("PRAGMA temp_store=MEMORY")
        _local.conn = conn
    return _local.conn


def close_connection() -> None:
    """关闭当前线程的连接（显式调用，用于 CLI 脚本退出）。"""
    if hasattr(_local, "conn") and _local.conn:
        _local.conn.close()
        _local.conn = None


@contextmanager
def transaction() -> Generator[sqlite3.Connection, None, None]:
    """自动管理事务：正常提交，异常回滚。"""
    conn = get_connection()
    conn.execute("BEGIN")
    try:
        yield conn
        conn.execute("COMMIT")
    except Exception:
        conn.execute("ROLLBACK")
        raise


@contextmanager
def cursor() -> Generator[sqlite3.Cursor, None, None]:
    """快速获取游标的上下文管理器（只读查询推荐）。"""
    conn = get_connection()
    cur = conn.cursor()
    try:
        yield cur
    finally:
        cur.close()


def init_schema() -> None:
    """初始化数据库 schema（幂等，多次调用安全）。"""
    schema_path = Path(__file__).parent / "schema.sql"
    conn = get_connection()
    conn.executescript(schema_path.read_text())


def vacuum() -> None:
    """压缩 WAL 文件，释放磁盘空间（建议每周跑一次）。"""
    with transaction() as conn:
        conn.execute("VACUUM")


def get_stats() -> dict[str, int]:
    """返回各表行数统计（用于健康检查）。"""
    tables = [
        "sources", "articles", "tags", "article_tags",
        "crawl_log", "versions", "cuda_hip_map",
        "papers", "known_issues", "prices"
    ]
    stats = {}
    with cursor() as cur:
        for t in tables:
            cur.execute(f"SELECT COUNT(*) FROM {t}")
            stats[t] = cur.fetchone()[0]
    return stats
