#!/usr/bin/env python3
"""
rocm-hip-map/db/migrate.py
Phase 2.0.0 数据迁移
将现有的 JSON 数据迁移到 SQLite 数据库

运行方式：
    python -m db.migrate [--force]

--force: 强制重建数据库（会清空所有数据）
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
import textwrap
from datetime import datetime, timezone
from pathlib import Path

# 项目根目录
ROOT = Path(__file__).parent.parent.resolve()
DATA_DIR = ROOT / "data"
CONTENT_DIR = ROOT / "content"

# 导入 db 模块
sys.path.insert(0, str(ROOT))
from db import init_schema, get_connection, transaction, cursor
from db.dao import (
    url_hash, content_hash, slug_from_title,
    article_upsert, source_upsert, tag_upsert, tag_add_to_article,
    tag_get_or_create, paper_upsert, known_issue_upsert,
    cuda_hip_map_bulk_insert,
)


def load_json(path: Path) -> dict | list:
    if not path.exists():
        return [] if "papers" in path.name else {}
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def read_article_body(file_path: str) -> tuple[str, int]:
    """读取文章正文并返回 (body, char_count)。"""
    if not file_path:
        return "", 0
    full_path = ROOT / file_path
    if not full_path.exists():
        return "", 0
    try:
        text = full_path.read_text(encoding="utf-8")
        return text, len(text)
    except Exception:
        return "", 0


def guess_lifecycle(source_url: str) -> str:
    """从 URL 猜 lifecycle。"""
    if "/deprecated/" in source_url:
        return "deprecated"
    if "/archives/" in source_url or "/v" in source_url:
        # 简单判断：含版本号目录
        if re.search(r"/(v\d+|ROCm[-_]\d)", source_url):
            return "maintenance"
    return "latest"


def migrate_sources() -> None:
    """注册所有数据源。"""
    print("📦 Migrating sources...")
    sources = [
        ("rocm-docs", "AMD ROCm Documentation", "official",
         "https://rocm.docs.amd.com", 0.5, "6h", "high"),
        ("rocm-blog", "AMD ROCm Blog", "blog",
         "https://rocm.blogs.amd.com", 0.5, "1h", "high"),
        ("rocm-github", "ROCm GitHub Issues/PR", "github",
         "https://github.com/ROCm", 2.0, "30m", "critical"),
        ("arxiv-amd", "arXiv AMD GPU Papers", "arxiv",
         "https://arxiv.org", 1.0, "12h", "medium"),
        ("phoronix", "Phoronix AMD-ROCm", "phoronix",
         "https://www.phoronix.com", 0.5, "2h", "medium"),
        ("reddit", "Reddit r/ROCm/r/LocalLLaMA", "reddit",
         "https://reddit.com", 0.5, "15m", "high"),
        ("hn", "Hacker News AMD/ROCm", "hn",
         "https://news.ycombinator.com", 1.0, "30m", "medium"),
        ("zhihu", "知乎 ROCm/AMD 显卡", "zhihu",
         "https://www.zhihu.com", 0.3, "6h", "low"),
    ]
    count = 0
    for slug, name, stype, base, rate, interval, priority in sources:
        source_upsert(
            slug=slug, name=name, source_type=stype,
            base_url=base, rate_limit_hz=rate,
            crawl_interval=interval, priority=priority,
        )
        count += 1
    print(f"  ✅ {count} sources registered")


def migrate_tags() -> None:
    """从 tags.json 迁移标签定义。"""
    print("📦 Migrating tags...")
    tags_path = DATA_DIR / "tags.json"
    tags_data = load_json(tags_path)
    if not isinstance(tags_data, dict):
        print("  ⚠️  tags.json unexpected format, skipping")
        return

    ns_map = {
        "gpu": "gpu", "gpu_arch": "gpu_arch",
        "frameworks": "frameworks", "os": "os",
        "difficulty": "difficulty", "tags": "topic",
    }

    count = 0
    for ns, ns_data in tags_data.items():
        if not isinstance(ns_data, dict):
            continue
        values = ns_data.get("values", [])
        labels = ns_data.get("labels", {})
        for v in values:
            tag_upsert(
                tag=v,
                namespace=ns_map.get(ns, "topic"),
                label=labels.get(v, v),
            )
            count += 1
    print(f"  ✅ {count} tags registered")


def migrate_articles() -> tuple[int, int]:
    """迁移 articles.json → articles 表。返回 (imported, skipped)。"""
    print("📦 Migrating articles...")
    articles_path = DATA_DIR / "articles.json"
    raw = load_json(articles_path)

    # 兼容两种格式
    articles = raw.get("articles", raw) if isinstance(raw, dict) else raw
    if not isinstance(articles, list):
        articles = []

    imported = 0
    skipped = 0

    # 批量获取 tag id 映射
    tag_id_map = {}
    difficulty_tag_map = {}
    with cursor() as cur:
        cur.execute("SELECT id, tag, namespace FROM tags")
        for row in cur.fetchall():
            tag_id_map[row["tag"]] = row["id"]
            if row["namespace"] == "difficulty":
                difficulty_tag_map[row["tag"]] = row["id"]

    for article in articles:
        try:
            file_path = article.get("file", "")
            body, char_count = read_article_body(file_path)
            source_url = article.get("source_url", "")
            title = article.get("title", "Untitled")

            # 跳过 404 页面
            if title == "404 - Page Not Found" or not source_url:
                skipped += 1
                continue

            lifecycle = article.get("lifecycle", guess_lifecycle(source_url))
            difficulty = article.get("difficulty", "")

            article_id, is_new = article_upsert(
                url=source_url,
                title=title,
                body=body,
                excerpt="",
                source_type=article.get("source_type", "official"),
                source_org=article.get("source_org", ""),
                credibility=article.get("credibility", 5),
                lifecycle=lifecycle,
                difficulty=difficulty,
            )

            # 添加 difficulty tag
            if difficulty and difficulty in difficulty_tag_map:
                tag_add_to_article(
                    article_id, difficulty_tag_map[difficulty],
                    confidence=1.0, method="rule",
                )

            # 添加 tags_extra
            for extra_tag in article.get("tags_extra", []):
                if extra_tag in tag_id_map:
                    tag_add_to_article(
                        article_id, tag_id_map[extra_tag],
                        confidence=0.8, method="rule",
                    )

            # 添加 OS tags
            for os_tag in article.get("os", []):
                if os_tag in tag_id_map:
                    tag_add_to_article(
                        article_id, tag_id_map[os_tag],
                        confidence=0.9, method="rule",
                    )

            imported += 1
        except Exception as e:
            print(f"  ⚠️  Error migrating article: {e}")
            skipped += 1

    print(f"  ✅ {imported} imported, {skipped} skipped")
    return imported, skipped


def migrate_cuda_hip_map() -> int:
    """迁移 cuda-hip-api-map.json。"""
    print("📦 Migrating CUDA→HIP map...")
    path = DATA_DIR / "cuda-hip-api-map.json"
    data = load_json(path)
    if not isinstance(data, list):
        data = []
    count = cuda_hip_map_bulk_insert(data)
    print(f"  ✅ {count} CUDA→HIP mappings imported")
    return count


def migrate_known_issues() -> int:
    """迁移 known-issues.json。"""
    print("📦 Migrating known issues...")
    path = DATA_DIR / "known-issues.json"
    data = load_json(path)
    if not isinstance(data, list):
        # 尝试解析
        if isinstance(data, dict) and "issues" in data:
            data = data["issues"]
        else:
            data = []
    count = 0
    for issue in data:
        if not issue.get("source_url"):
            continue
        known_issue_upsert(
            title=issue.get("title", ""),
            component=issue.get("component", ""),
            status=issue.get("status", "open"),
            rocm_version=issue.get("rocm_version", ""),
            gpu=issue.get("gpu", ""),
            os=issue.get("os", ""),
            source_url=issue.get("source_url", ""),
            summary=issue.get("summary", ""),
            workaround=issue.get("workaround", ""),
        )
        count += 1
    print(f"  ✅ {count} known issues imported")
    return count


def migrate_papers() -> int:
    """迁移 papers.json。"""
    print("📦 Migrating papers...")
    path = DATA_DIR / "papers.json"
    data = load_json(path)
    if isinstance(data, dict):
        papers = data.get("papers", [])
    elif isinstance(data, list):
        papers = data
    else:
        papers = []

    count = 0
    for paper in papers:
        arxiv_id = paper.get("arxiv_id") or paper.get("id", "")
        if not arxiv_id:
            continue
        paper_upsert(
            arxiv_id=arxiv_id,
            title=str(paper.get("title", "")),
            authors=",".join(paper["authors"]) if isinstance(paper.get("authors"), list) else str(paper.get("authors", "")),
            abstract=str(paper.get("abstract", "")),
            published_at=paper.get("published", ""),
            categories=",".join(paper.get("categories", [])) if isinstance(paper.get("categories"), list) else str(paper.get("categories", "")),
            pdf_url=paper.get("pdf_url", ""),
            source_url=paper.get("url", paper.get("source_url", "")),
        )
        count += 1
    print(f"  ✅ {count} papers imported")
    return count


def reset_db() -> None:
    """强制重建数据库（删除所有表后重建）。"""
    print("⚠️  Resetting database...")
    conn = get_connection()
    tables = [
        "article_tags", "articles", "tags",
        "crawl_log", "sources",
        "versions", "cuda_hip_map",
        "papers", "known_issues", "prices",
    ]
    for t in tables:
        conn.execute(f"DROP TABLE IF EXISTS {t}")
    print("  ✅ All tables dropped")


def main() -> None:
    force = "--force" in sys.argv

    print(f"\n{'='*60}")
    print(f"rocm-hip-map DB Migration — Phase 2.0.0")
    print(f"Database: {ROOT / 'data' / 'rocm-hip-map.db'}")
    print(f"{'='*60}\n")

    if force:
        reset_db()

    print("🔧 Initializing schema...")
    init_schema()
    print("  ✅ Schema ready\n")

    # 迁移各数据源
    migrate_sources()
    migrate_tags()
    articles_imported, articles_skipped = migrate_articles()
    cuda_count = migrate_cuda_hip_map()
    issues_count = migrate_known_issues()
    papers_count = migrate_papers()

    # 统计
    from db import get_stats
    stats = get_stats()
    print(f"\n{'='*60}")
    print("📊 Migration Complete")
    print(f"{'='*60}")
    for table, count in stats.items():
        print(f"  {table:<20} {count:>6} rows")
    print(f"\nTotal articles imported: {articles_imported}")
    print(f"Articles skipped:        {articles_skipped}")
    print(f"\n✅ Migration finished successfully.")
    print(f"\nTo verify: sqlite3 {ROOT/'data'/'rocm-hip-map.db'} '.tables'")


if __name__ == "__main__":
    main()
