#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import db
from db import dao

CLASSIFIED_JSON = PROJECT_ROOT / 'data' / 'articles_classified.json'

SOURCE_TYPE_MAP = {
    'github': 'github',
    'rocm': 'official',
    'hip': 'official',
    'hipify': 'official',
    'rocm-install': 'official',
}

TAG_NAMESPACE_MAP = {
    'library': 'topic',
    'topic': 'topic',
    'os': 'os',
    'gpu': 'gpu',
    'driver': 'topic',
    'framework': 'frameworks',
}


def load_articles() -> list[dict]:
    with CLASSIFIED_JSON.open(encoding='utf-8') as f:
        payload = json.load(f)
    return payload.get('articles', [])


def infer_source(article: dict) -> tuple[str, str]:
    library = article.get('library', '')
    source_type = SOURCE_TYPE_MAP.get(library, 'official')
    source_org = library or 'amd'
    return source_type, source_org


def main() -> int:
    db.init_schema()
    articles = load_articles()
    inserted_or_updated = 0

    for article in articles:
        source_type, source_org = infer_source(article)
        article_id, _ = dao.article_upsert(
            url=article.get('url', ''),
            title=article.get('title', ''),
            body='',
            excerpt='',
            source_url=article.get('url', ''),
            source_type=source_type,
            source_org=source_org,
            credibility=4 if source_type == 'official' else 3,
            lifecycle='latest',
            difficulty=article.get('difficulty', ''),
        )
        inserted_or_updated += 1

        for tag in article.get('tags', []):
            tag_name = tag.get('tag', '')
            ns = TAG_NAMESPACE_MAP.get(tag.get('ns', ''), 'topic')
            if not tag_name:
                continue
            tag_id = dao.tag_get_or_create(tag_name, ns, label=tag_name)
            dao.tag_add_to_article(
                article_id,
                tag_id,
                confidence=float(tag.get('conf', 1.0)),
                method='rule',
            )

    total = dao.article_count()
    print(json.dumps({
        'processed': len(articles),
        'upserted': inserted_or_updated,
        'db_article_count': total,
    }, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
