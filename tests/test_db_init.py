from __future__ import annotations

import db


def test_get_connection_enables_wal_and_foreign_keys(isolated_db):
    conn = db.get_connection()

    journal_mode = conn.execute('PRAGMA journal_mode').fetchone()[0]
    foreign_keys = conn.execute('PRAGMA foreign_keys').fetchone()[0]

    assert journal_mode.lower() == 'memory'
    assert foreign_keys == 1


def test_get_stats_counts_seeded_rows(isolated_db):
    conn = db.get_connection()
    conn.execute("INSERT INTO sources (slug, name, source_type) VALUES ('amd', 'AMD', 'official')")
    conn.execute(
        "INSERT INTO articles (url, url_hash, title, content_hash, source_type, status) VALUES (?, ?, ?, ?, ?, ?)",
        ('https://example.com', 'hash123', 'Example', 'content123', 'official', 'discovered'),
    )

    stats = db.get_stats()

    assert stats['sources'] == 1
    assert stats['articles'] == 1
