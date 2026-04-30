-- ============================================================
-- rocm-hip-map SQLite Schema
-- Phase 2.0.0 数据库化
-- 目标：替代 articles.json，实现多源采集 + 分类 + 质量评分
-- ============================================================

PRAGMA journal_mode = WAL;
PRAGMA foreign_keys = ON;
PRAGMA busy_timeout = 30000;

-- ----------------------------------------------------------
-- 1. sources — 数据源注册表
-- ----------------------------------------------------------
CREATE TABLE IF NOT EXISTS sources (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    slug            TEXT    NOT NULL UNIQUE,
    name            TEXT    NOT NULL,
    source_type     TEXT    NOT NULL CHECK(source_type IN ('official','blog','github','arxiv','phoronix','reddit','hn','zhihu','other')),
    base_url        TEXT,
    enabled         INTEGER NOT NULL DEFAULT 1,
    rate_limit_hz  REAL    NOT NULL DEFAULT 1.0,
    crawl_interval  TEXT    NOT NULL DEFAULT '6h',   -- e.g. '30m', '1h', '6h', '12h'
    priority        TEXT    NOT NULL DEFAULT 'medium' CHECK(priority IN ('critical','high','medium','low')),
    last_crawled_at TEXT,                              -- ISO8601
    next_crawl_at   TEXT,                              -- ISO8601
    created_at      TEXT    NOT NULL DEFAULT (datetime('now')),
    updated_at      TEXT    NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_sources_enabled ON sources(enabled);
CREATE INDEX IF NOT EXISTS idx_sources_priority ON sources(priority);

-- ----------------------------------------------------------
-- 2. articles — 文章主表
-- ----------------------------------------------------------
CREATE TABLE IF NOT EXISTS articles (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    url             TEXT    NOT NULL,
    url_hash        TEXT    NOT NULL UNIQUE,           -- sha256(url_normalized)
    title           TEXT    NOT NULL,
    slug            TEXT,                               -- url-safe slug for SEO
    content_hash    TEXT    NOT NULL,                   -- sha256(body)
    body            TEXT,                               -- full text content
    excerpt         TEXT,                               -- 200 char excerpt

    source_id       INTEGER REFERENCES sources(id),
    source_url      TEXT,
    source_type     TEXT    NOT NULL,
    source_org      TEXT,
    credibility     INTEGER DEFAULT 3 CHECK(credibility BETWEEN 1 AND 5),

    -- lifecycle: latest, maintenance, deprecated
    lifecycle       TEXT    DEFAULT 'latest',
    difficulty      TEXT    CHECK(difficulty IN ('beginner','intermediate','advanced','reference')),

    -- Content metadata
    word_count      INTEGER DEFAULT 0,
    char_count      INTEGER DEFAULT 0,
    has_code        INTEGER DEFAULT 0,
    has_benchmark   INTEGER DEFAULT 0,
    has_images      INTEGER DEFAULT 0,

    -- Quality scoring
    quality_score   REAL    DEFAULT 0.0 CHECK(quality_score BETWEEN 0 AND 1),
    is_indexed      INTEGER NOT NULL DEFAULT 1,         -- 1=主索引, 0=仅存档
    manual_override INTEGER DEFAULT 0,                  -- 1=人工干预过

    -- Bilingual
    has_translation INTEGER DEFAULT 0,
    translation_lang TEXT,                               -- 'zh', 'en', etc.
    translated_at   TEXT,

    -- Timestamps
    published_at    TEXT,                               -- 原始发布时间
    discovered_at   TEXT    NOT NULL DEFAULT (datetime('now')),
    updated_at      TEXT    NOT NULL DEFAULT (datetime('now')),
    fetched_at      TEXT,                               -- 最后一次抓取

    -- HTTP caching
    etag            TEXT,
    last_modified   TEXT,
    http_status     INTEGER,

    -- Status
    status          TEXT    NOT NULL DEFAULT 'discovered'
                    CHECK(status IN ('discovered','fetched','parsed','classified','translated','published','error','archived')),
    error_message   TEXT,

    -- SEO
    canonical_url   TEXT,
    no_index        INTEGER DEFAULT 0,
    created_at      TEXT    NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_articles_url_hash     ON articles(url_hash);
CREATE INDEX IF NOT EXISTS idx_articles_content_hash ON articles(content_hash);
CREATE INDEX IF NOT EXISTS idx_articles_status       ON articles(status);
CREATE INDEX IF NOT EXISTS idx_articles_quality      ON articles(quality_score DESC) WHERE is_indexed = 1;
CREATE INDEX IF NOT EXISTS idx_articles_published    ON articles(published_at DESC) WHERE published_at IS NOT NULL;
CREATE INDEX IF NOT EXISTS idx_articles_discovered    ON articles(discovered_at DESC);
CREATE INDEX IF NOT EXISTS idx_articles_source_type   ON articles(source_type);
CREATE INDEX IF NOT EXISTS idx_articles_is_indexed    ON articles(is_indexed) WHERE is_indexed = 1;

-- ----------------------------------------------------------
-- 3. tags — 标签命名空间
-- ----------------------------------------------------------
CREATE TABLE IF NOT EXISTS tags (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    tag             TEXT    NOT NULL UNIQUE,
    namespace       TEXT    NOT NULL                  -- 'gpu','gpu_arch','frameworks','os','difficulty','topic'
                    CHECK(namespace IN ('gpu','gpu_arch','frameworks','os','difficulty','topic','issue_type')),
    label           TEXT    NOT NULL,                  -- display name
    label_zh        TEXT,                             -- Chinese label
    description     TEXT,
    gfx_target      TEXT,                             -- LLVM target, e.g. 'gfx1100', 'gfx942'
    gfx_generation  TEXT,                             -- e.g. 'rdna3', 'cdna3'
    color           TEXT,                             -- hex color for UI
    created_at      TEXT    NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_tags_namespace ON tags(namespace);
CREATE INDEX IF NOT EXISTS idx_tags_gfx_target ON tags(gfx_target) WHERE gfx_target IS NOT NULL;

-- ----------------------------------------------------------
-- 4. article_tags — 多对多关联（含置信度）
-- ----------------------------------------------------------
CREATE TABLE IF NOT EXISTS article_tags (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    article_id      INTEGER NOT NULL REFERENCES articles(id) ON DELETE CASCADE,
    tag_id          INTEGER NOT NULL REFERENCES tags(id) ON DELETE CASCADE,
    confidence      REAL    NOT NULL DEFAULT 1.0 CHECK(confidence BETWEEN 0 AND 1),
    method          TEXT    NOT NULL DEFAULT 'rule'  -- 'rule','llm','manual'
                    CHECK(method IN ('rule','llm','manual')),
    created_at      TEXT    NOT NULL DEFAULT (datetime('now')),
    UNIQUE(article_id, tag_id)
);

CREATE INDEX IF NOT EXISTS idx_article_tags_article ON article_tags(article_id);
CREATE INDEX IF NOT EXISTS idx_article_tags_tag     ON article_tags(tag_id);

-- ----------------------------------------------------------
-- 5. crawl_log — 爬取记录
-- ----------------------------------------------------------
CREATE TABLE IF NOT EXISTS crawl_log (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    source_id       INTEGER REFERENCES sources(id),
    started_at      TEXT    NOT NULL DEFAULT (datetime('now')),
    finished_at     TEXT,
    status          TEXT    NOT NULL                  -- 'running','success','partial','failed','circuit_broken'
                    CHECK(status IN ('running','success','partial','failed','circuit_broken')),
    total_urls      INTEGER DEFAULT 0,
    new_articles    INTEGER DEFAULT 0,
    updated_articles INTEGER DEFAULT 0,
    skipped_304     INTEGER DEFAULT 0,
    failed          INTEGER DEFAULT 0,
    error_message   TEXT,
    duration_ms     INTEGER,
    is_incremental  INTEGER DEFAULT 1
);

CREATE INDEX IF NOT EXISTS idx_crawl_log_source    ON crawl_log(source_id);
CREATE INDEX IF NOT EXISTS idx_crawl_log_started   ON crawl_log(started_at DESC);
CREATE INDEX IF NOT EXISTS idx_crawl_log_status    ON crawl_log(status);

-- ----------------------------------------------------------
-- 6. versions — ROCm/HIP 版本追踪
-- ----------------------------------------------------------
CREATE TABLE IF NOT EXISTS versions (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    project         TEXT    NOT NULL,                 -- 'rocm','hip','rocminfo', etc.
    version         TEXT    NOT NULL,                 -- e.g. '7.2.0'
    release_date    TEXT,
    is_latest       INTEGER DEFAULT 0,
    release_notes_url TEXT,
    source          TEXT    NOT NULL DEFAULT 'rocm.docs.amd.com',
    created_at      TEXT    NOT NULL DEFAULT (datetime('now')),
    UNIQUE(project, version)
);

CREATE INDEX IF NOT EXISTS idx_versions_project    ON versions(project);
CREATE INDEX IF NOT EXISTS idx_versions_latest     ON versions(project, is_latest DESC) WHERE is_latest = 1;

-- ----------------------------------------------------------
-- 7. cuda_hip_map — CUDA→HIP API 映射 (304 条)
-- ----------------------------------------------------------
CREATE TABLE IF NOT EXISTS cuda_hip_map (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    cuda_api        TEXT    NOT NULL,
    hip_api         TEXT    NOT NULL,
    category        TEXT    NOT NULL,                 -- e.g. '设备管理', '内存管理'
    status          TEXT    NOT NULL                  -- 'supported','unsupported','n/a'
                    CHECK(status IN ('supported','unsupported','n/a')),
    rocm_version    TEXT,                             -- First supported version
    source_url      TEXT,
    notes           TEXT,
    created_at      TEXT    NOT NULL DEFAULT (datetime('now')),
    UNIQUE(cuda_api, hip_api)
);

CREATE INDEX IF NOT EXISTS idx_cuda_hip_cuda_api ON cuda_hip_map(cuda_api);
CREATE INDEX IF NOT EXISTS idx_cuda_hip_hip_api  ON cuda_hip_map(hip_api);
CREATE INDEX IF NOT EXISTS idx_cuda_hip_category  ON cuda_hip_map(category);

-- ----------------------------------------------------------
-- 8. papers — 论文表
-- ----------------------------------------------------------
CREATE TABLE IF NOT EXISTS papers (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    arxiv_id        TEXT    UNIQUE,
    title           TEXT    NOT NULL,
    authors         TEXT,
    abstract        TEXT,
    published_at    TEXT,
    pdf_url         TEXT,
    pdf_local_path  TEXT,
    categories      TEXT,                             -- comma-separated arxiv categories
    keywords        TEXT,                             -- comma-separated extracted keywords
    rocm_relevance  REAL DEFAULT 0.0,                -- 0-1 relevance score
    quality_score   REAL DEFAULT 0.0,
    is_indexed      INTEGER NOT NULL DEFAULT 1,
    source_url      TEXT,
    created_at      TEXT    NOT NULL DEFAULT (datetime('now')),
    updated_at      TEXT    NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_papers_arxiv_id      ON papers(arxiv_id);
CREATE INDEX IF NOT EXISTS idx_papers_published     ON papers(published_at DESC);
CREATE INDEX IF NOT EXISTS idx_papers_rocm_relevance ON papers(rocm_relevance DESC);
CREATE INDEX IF NOT EXISTS idx_papers_is_indexed    ON papers(is_indexed) WHERE is_indexed = 1;

-- ----------------------------------------------------------
-- 9. known_issues — Known Issues (from AMD)
-- ----------------------------------------------------------
CREATE TABLE IF NOT EXISTS known_issues (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    title           TEXT,
    component       TEXT,                             -- install/driver/pytorch/hip/performance
    status          TEXT    CHECK(status IN ('open','fixed','workaround')),
    rocm_version    TEXT,
    gpu             TEXT,                             -- e.g. 'MI300X', 'RX 7900 XTX'
    os              TEXT,
    source_url      TEXT,
    summary         TEXT,
    workaround      TEXT,
    published_at    TEXT,
    created_at      TEXT    NOT NULL DEFAULT (datetime('now')),
    UNIQUE(source_url)
);

CREATE INDEX IF NOT EXISTS idx_issues_status       ON known_issues(status);
CREATE INDEX IF NOT EXISTS idx_issues_rocm_version  ON known_issues(rocm_version);
CREATE INDEX IF NOT EXISTS idx_issues_gpu           ON known_issues(gpu);

-- ----------------------------------------------------------
-- 10. prices — GPU 价格追踪
-- ----------------------------------------------------------
CREATE TABLE IF NOT EXISTS prices (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    country         TEXT    NOT NULL,                 -- US/DE/UK/JP/KR/CN
    gpu_model       TEXT    NOT NULL,
    condition       TEXT    NOT NULL DEFAULT 'used',  -- new/used
    price_eur       REAL,                            -- normalized to EUR
    price_local      REAL,                            -- original currency
    currency        TEXT,                             -- original currency code
    source_url      TEXT,
    scraped_at      TEXT    NOT NULL DEFAULT (datetime('now')),
    UNIQUE(country, gpu_model, condition, scraped_at)
);

CREATE INDEX IF NOT EXISTS idx_prices_country       ON prices(country);
CREATE INDEX IF NOT EXISTS idx_prices_gpu            ON prices(gpu_model);
CREATE INDEX IF NOT EXISTS idx_prices_scraped       ON prices(scraped_at DESC);
