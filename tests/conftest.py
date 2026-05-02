from __future__ import annotations

import sqlite3
import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import db  # noqa: E402


@pytest.fixture
def isolated_db():
    original_conn = getattr(db._local, 'conn', None)
    conn = sqlite3.connect(':memory:', check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute('PRAGMA foreign_keys=ON')
    db._local.conn = conn
    db.init_schema()
    try:
        yield conn
    finally:
        conn.close()
        db._local.conn = original_conn
