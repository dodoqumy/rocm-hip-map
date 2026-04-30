#!/usr/bin/env python3
"""
rocm-hip-map/db/export.py
Phase 2.0.0 导出层
将 SQLite 数据导出为 articles.json（保持与 sidebar 生成器兼容）

运行方式：
    python -m db.export [--output data/articles.json]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).parent.parent.resolve()
DATA_DIR = ROOT / "data"

sys.path.insert(0, str(ROOT))
from db import cursor


def export_articles_json(output_path: Path | None = None) -> int:
    """导出 articles 表为 articles.json（兼容旧格式）。"""
    if output_path is None:
        output_path = DATA_DIR / "articles.json"

    with cursor() as cur:
        cur.execute(
            """SELECT
                a.url_hash AS file_key,
                a.url AS source_url,
                a.title,
                a.source_type,
                a.source_org,
                a.credibility,
                a.lifecycle,
                a.difficulty,
                a.char_count,
                GROUP_CONCAT(DISTINCT t.tag) AS tags_extra,
                GROUP_CONCAT(DISTINCT CASE WHEN t.namespace = 'os' THEN t.tag END) AS os_tags,
                a.updated_at AS classified_at
               FROM articles a
               LEFT JOIN article_tags at ON at.article_id = a.id
               LEFT JOIN tags t ON t.id = at.tag_id
               WHERE a.is_indexed = 1
               GROUP BY a.id
               ORDER BY a.discovered_at DESC"""
        )
        rows = cur.fetchall()

    articles = []
    for row in rows:
        d = dict(row)
        file_key = d["file_key"]
        # 构造兼容旧格式的 file 路径
        if d["source_type"] == "official":
            # 从 URL 提取路径
            url = d["source_url"] or ""
            slug = file_key[:40]
            d["file"] = f"content/raw/english/{slug}.md"
        else:
            d["file"] = f"content/raw/{d['source_type']}/{file_key}.md"

        # tags_extra 从 GROUP_CONCAT 中提取
        raw_tags = d.get("tags_extra", "") or ""
        d["tags_extra"] = [t.strip() for t in raw_tags.split(",") if t.strip()]
        raw_os = d.get("os_tags", "") or ""
        d["os"] = [t.strip() for t in raw_os.split(",") if t.strip()]

        articles.append({
            "file": d["file"],
            "title": d["title"],
            "source_url": d["source_url"],
            "source_type": d["source_type"],
            "source_org": d["source_org"] or "",
            "credibility": d["credibility"] or 5,
            "lifecycle": d["lifecycle"] or "latest",
            "os": d["os"],
            "tags_extra": d["tags_extra"],
            "difficulty": d["difficulty"] or "beginner",
            "char_count": d["char_count"] or 0,
            "classified_at": d["classified_at"] or "",
        })

    output = {"articles": articles, "updated": datetime.now(timezone.utc).isoformat()}

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    return len(articles)


def export_versions_json(output_path: Path | None = None) -> int:
    """导出 versions 表为 versions.json。"""
    if output_path is None:
        output_path = DATA_DIR / "versions.json"

    with cursor() as cur:
        cur.execute(
            """SELECT project, version, release_date, is_latest, release_notes_url
               FROM versions ORDER BY project, release_date DESC"""
        )
        rows = cur.fetchall()

    versions = {}
    for row in rows:
        d = dict(row)
        proj = d.pop("project")
        if proj not in versions:
            versions[proj] = []
        versions[proj].append(d)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(versions, f, ensure_ascii=False, indent=2)

    return sum(len(v) for v in versions.values())


def export_sidebar_data(output_dir: Path | None = None) -> None:
    """
    导出侧边栏所需的聚合数据（按 source_type / lifecycle / difficulty 分组）。
    用于 generate-docs.py / generate-sidebar.py 读取。
    """
    if output_dir is None:
        output_dir = DATA_DIR / "sidebar_cache"
    output_dir.mkdir(parents=True, exist_ok=True)

    # 按 source_type 统计
    with cursor() as cur:
        cur.execute(
            """SELECT source_type, COUNT(*) as cnt
               FROM articles WHERE is_indexed=1
               GROUP BY source_type ORDER BY cnt DESC"""
        )
        by_source = [{"type": r["source_type"], "count": r["cnt"]} for r in cur.fetchall()]

    # 按 difficulty 统计
    with cursor() as cur:
        cur.execute(
            """SELECT difficulty, COUNT(*) as cnt
               FROM articles WHERE is_indexed=1 AND difficulty IS NOT NULL
               GROUP BY difficulty ORDER BY cnt DESC"""
        )
        by_difficulty = [{"difficulty": r["difficulty"], "count": r["cnt"]} for r in cur.fetchall()]

    # 按 lifecycle 统计
    with cursor() as cur:
        cur.execute(
            """SELECT lifecycle, COUNT(*) as cnt
               FROM articles WHERE is_indexed=1
               GROUP BY lifecycle ORDER BY cnt DESC"""
        )
        by_lifecycle = [{"lifecycle": r["lifecycle"], "count": r["cnt"]} for r in cur.fetchall()]

    # 标签云
    with cursor() as cur:
        cur.execute(
            """SELECT t.tag, t.namespace, COUNT(*) as cnt
               FROM article_tags at
               JOIN tags t ON t.id = at.tag_id
               JOIN articles a ON a.id = at.article_id
               WHERE a.is_indexed=1
               GROUP BY t.tag ORDER BY cnt DESC LIMIT 50"""
        )
        tag_cloud = [{"tag": r["tag"], "namespace": r["namespace"], "count": r["cnt"]}
                     for r in cur.fetchall()]

    data = {
        "by_source": by_source,
        "by_difficulty": by_difficulty,
        "by_lifecycle": by_lifecycle,
        "tag_cloud": tag_cloud,
        "exported_at": datetime.now(timezone.utc).isoformat(),
    }

    path = output_dir / "sidebar_stats.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"  ✅ Exported sidebar stats to {path}")


def main() -> None:
    print("📤 Exporting data from SQLite to JSON...")

    count = export_articles_json()
    print(f"  ✅ {count} articles → articles.json")

    ver_count = export_versions_json()
    print(f"  ✅ {ver_count} version entries → versions.json")

    export_sidebar_data()
    print("\n✅ All exports complete.")


if __name__ == "__main__":
    main()
