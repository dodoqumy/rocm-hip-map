from __future__ import annotations

from db import dao


def test_article_upsert_inserts_and_updates_records(isolated_db):
    article_id, is_new = dao.article_upsert(
        url='https://example.com/post?utm_source=test',
        title='Hello ROCm',
        body='Initial body with enough content to hash correctly.',
        source_type='official',
        source_org='amd',
        credibility=5,
        lifecycle='latest',
    )

    stored = dao.article_get_by_id(article_id)

    assert is_new is True
    assert stored is not None
    assert stored['url_hash'] == dao.url_hash('https://example.com/post')
    assert stored['source_org'] == 'amd'

    same_id, same_is_new = dao.article_upsert(
        url='https://example.com/post?utm_source=test',
        title='Hello ROCm',
        body='Initial body with enough content to hash correctly.',
        source_type='official',
        source_org='amd',
        credibility=5,
        lifecycle='latest',
    )
    assert same_id == article_id
    assert same_is_new is False

    updated_id, updated_is_new = dao.article_upsert(
        url='https://example.com/post?utm_source=test',
        title='Hello ROCm Updated',
        body='Updated body with changed content and enough words to trigger a new content hash.',
        source_type='official',
        source_org='amd',
        credibility=5,
        lifecycle='latest',
    )
    updated = dao.article_get_by_id(article_id)

    assert updated_id == article_id
    assert updated_is_new is False
    assert updated['title'] == 'Hello ROCm Updated'


def test_source_upsert_and_due_for_crawl(isolated_db):
    source_id = dao.source_upsert(
        slug='rocm-docs',
        name='ROCm Docs',
        source_type='official',
        base_url='https://rocm.docs.amd.com',
        crawl_interval='1h',
        priority='high',
    )

    due = dao.source_due_for_crawl(limit=10)

    assert source_id > 0
    assert any(item['slug'] == 'rocm-docs' for item in due)
