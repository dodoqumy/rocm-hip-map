from __future__ import annotations

from crawlers.dedup import Deduplicator, compute_content_hash, compute_url_hash, normalize_url


def test_normalize_url_and_hash_strip_tracking_parameters():
    normalized = normalize_url('https://example.com/path?utm_source=x&fbclid=abc&ref_src=feed')

    assert normalized == 'https://example.com/path'
    assert compute_url_hash(normalized) == compute_url_hash('https://example.com/path?utm_source=foo')
    assert normalize_url('https://example.com/post?utm_source=test&a=1') == 'https://example.com/post?a=1'


def test_deduplicator_tracks_seen_urls_and_content():
    dedup = Deduplicator()

    assert dedup.is_seen('https://example.com/path?utm_source=x') is False
    assert dedup.is_seen('https://example.com/path?utm_source=y') is True
    assert dedup.is_content_unchanged('same body') is False
    assert dedup.is_content_unchanged('same body') is True
    assert len(compute_content_hash('same body')) == 16
