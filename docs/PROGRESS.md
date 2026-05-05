# 📋 rocm-hip-map 开发进度跟踪

**最后更新：** 2026-05-02 12:00 CST
**当前分支：** `main`
**最新提交：** `f85bdd4` — feat(seo): Phase 2.5 sitemap 增强 + 落地页
**网站预览：** https://dodoqumy.github.io/rocm-hip-map/
**后续计划：** [docs/plans/2026-05-02-phase-2.0-follow-up.md](docs/plans/2026-05-02-phase-2.0-follow-up.md) 📋
**定时任务：** [docs/cron-jobs.md](docs/cron-jobs.md) ⏰
**Bug 记录：** [docs/bugs.md](docs/bugs.md) 🐛
**经验教训：** [docs/lessons-learned.md](docs/lessons-learned.md) 📖

---

## 总体进度

```
Phase 0  ████████████████████████████████ 100% ✅
Phase 1  ████████████████████████████████ 100% ✅
Phase 2  ████████████████████████████████ 100% ✅
Phase 3  ████████████████████████████████ 100% ✅
Phase 4  ██████████████████████░░░░░░░░░░  80% 🟡 (翻译管道已验证，增量模式就绪)
Phase 5  ████████████████████████████████ 100% ✅
Phase 6  ████████████████████████████████ 100% ✅
Phase 7  ████████████████░░░░░░░░░░░░░░░░  50% 🟡
Phase 11 ████████████████████████████████ 100% ✅
Phase 8  ████████████████████████████████ 100% ✅ (侧边栏✅ 部署验证✅)
Phase 9  ██████████████████████████████░░  80% 🟡 (9.3✅ 9.6✅)
Phase 10 ██████████████████████░░░░░░░░░░  79% 🟡 (并行拆分✅)
Phase 2.0 ██████████████░░░░░░░░░░░  75% 🟡 (2.1✅ 2.3✅ 2.4✅ 爬虫+分类+质量评分完成)
────────────────────────────────────────────
总体     █████████████████████░░░░░░  85%
```

**图例：** ✅ 完成 · 🟡 进行中 · 🔲 未开始 · ❌ 阻塞

---

## Phase 4：双语对照 + AI 翻译管道

| # | 任务 | 状态 | 备注 |
|---|------|------|------|
| 4.1 | ParallelView 组件 | ✅ | 左右分栏模式 |
| 4.2 | InterleavedView 组件 | ✅ | 逐段对照模式 |
| 4.3 | BilingualViewer 主组件 | ✅ | 模式切换 + 元信息展示 |
| 4.4 | 移动端自适应 | ✅ | 左右→上下 |
| 4.5 | `scripts/translate.py` | ✅ | 4 后端 + 增量模式 + 断点续传 |
| 4.6 | `glossary/rocm-terms.yaml` | ✅ | CUDA↔HIP 术语对照 |
| 4.7 | GlossaryTooltip 组件 | ✅ | 悬浮术语解释 |
| 4.8 | 翻译管道首次验证 | ✅ | test-translate #2 成功，路径正确 |
| 4.9 | `translate.yml` 独立定时 workflow | ✅ | 每日 12:00，增量 5 篇 |
| 4.10 | 批量翻译 68 篇 | 🟡 | 需 14 次增量运行覆盖 |

---

## Phase 6：部署与 CI/CD

| # | 任务 | 状态 | 备注 |
|---|------|------|------|
| 6.1-6.4 | Pages 部署 | ✅ | |
| 6.5 | `sync.yml` 定时同步 | ✅ | 已解耦翻译，~1min |
| 6.6 | `validate.yml` | ✅ | |
| 6.7 | Release Watch | ✅ | |
| 6.8 | `translate.yml` 独立翻译 | ✅ | 新增 |
| 6.9 | `sync-prices.yml` 并行拆分 | ✅ | matrix US/DE/UK |

---

## Phase 7：内容扩充

| # | 任务 | 状态 | 备注 |
|---|------|------|------|
| 7.1 | 批量导入 ROCm 68 篇 | 🟡 | 已抓取，MDX 生成完成 |
| 7.2 | 同步 GitHub Issues | 🔲 | |
| 7.3 | CUDA→HIP API 映射 304 条 | ✅ | |
| 7.4 | PyTorch/TF 文档 | 🔲 | |
| 7.5 | 中文学术论文 | 🔲 | |
| 7.6 | 双语搜索 | ✅ | |
| 7.7 | 图片 OCR 翻译 | 🔲 | |
| 7.8 | GA/Umami | 🔲 | |
| 7.9 | verify.py | ✅ | |
| 7.10 | verify.yml | ✅ | |

---

## Phase 8：论文搜集与翻译

| # | 任务 | 状态 | 备注 |
|---|------|------|------|
|| 8.1 | fetch-papers.py | ✅ | 87 篇 |
| 8.2 | extract-pdf.py | ✅ | 86/87 成功 |
| 8.3 | translate.py paper | ✅ | --mode paper |
| 8.4 | generate-docs.py paper | ✅ | PaperArticleHeader |
| 8.5 | 侧边栏 📜 论文分类 | ✅ | 已接入 sidebars.ts |
| 8.6 | CI papers.yml | ✅ | 每周六 |
| 8.7 | 部署后验证 ≥5 篇 | ✅ | 87 篇 build 验证通过 |

---

## Phase 9：多语言情报

| # | 任务 | 状态 | 备注 |
|---|------|------|------|
| 9.1 | 欧洲核心抓取 | ✅ | FI/FR/DE 7 篇 |
| 9.2 | 亚洲核心抓取 | ✅ | JP/KR 11 篇 |
| 9.3 | 扩展（ES/NL/IT/RU/SE） | ✅ | 8 篇新增 |
| 9.4 | 多语言翻译适配 | 🔲 | xx→en→zh |
| 9.5 | 国旗标签 | 🔲 | |
| 9.6 | 侧边栏 🌐 多语言 | ✅ | 已接入 sidebars.ts |
| 9.7 | CI 多语言同步 | 🔲 | |

---

## Phase 10：GPU 价格追踪

| # | 任务 | 状态 | 备注 |
|---|------|------|------|
| 10.1 | eBay API (US/DE/UK) | ✅ | |
| 10.2 | 亚洲平台（闲鱼/Mercari） | 🔲 | |
| 10.3 | 欧洲平台（Leboncoin 等） | 🔲 | |
| 10.4 | normalize-prices.py | ✅ | 支持站点分片合并 |
| 10.5 | 历史存储 52 周 | ✅ | |
| 10.6 | PriceTracker/Chart | ✅ | |
| 10.7 | CI sync-prices.yml | ✅ | 按国家并行 |

## Phase 2.0(月10万PV路线):见 docs/plan-phase2.0-claude.md（主），plan-phase2.0-chatgpt.md（参考）
|||- 2.0.0 数据库化         ✅ *(711 articles / 115 tags / 301 CUDA→HIP / 87 papers / 8 sources)*
|||- 2.1 爬虫框架 v2       ✅ *(crawlers/ 模块，三级发现，464 篇已抓取)*
|||- 2.1.1 BaseCrawler+HTTPClient+Extractor+Dedup | ✅
|||- 2.1.2 SitemapCrawler + SphinxNavCrawler | ✅ *(rocm-docs 152篇 + HIP 89篇发现)*
|||- 2.1.3 GithubDocsCrawler + RSSCrawler | ✅ *(blog RSS)*
|||- 2.1.4 config/amd-sources.yaml | ✅ *(44 个源配置)*
||||- 2.1.5 scripts/fetch.py 统一入口 | ✅ *(--all/--source/--max-urls/--dry-run)*
||||- 2.1.6 slug 清理 | ✅ *(rocm→rocm-docs-latest, 176 篇统一)*
||||- 2.1.7 trafilatura 正文提取 | ✅ *(5151 chars 干净 markdown, 无 div 噪音)* |
||||- 2.1.8 多源子项目抓取 | ✅ *(19 个子项目, 739 篇, 31MB)* |
|||||- 2.1.9 剩余子项目抓取 | 🔲 *(后台 cronjob 进行中, 30 个待抓)* |
|||||- 2.3 智能分类 | ✅ *(classify_v2.py, 739 篇, 522 索引)* |
|||||- 2.4 质量评分 | ✅ *(quality_score 算法, is_indexed 筛选)* |
|||||- 2.5 SEO 与发布 | 🔲 *(sitemap/JSON-LD/hreflang + 落地页)* |
|||||- 2.6 监控               🔲 *(Prometheus + Grafana + Sentry)*

## 内容统计

|| 类型 | 数量 | 状态 |
|------|------|------|
| 官方文档（raw） | **739 篇 / 31MB** | ✅ |
| - rocm-docs-latest | 179 篇 | ✅ |
| - hip-latest | 89 篇 | ✅ |
| - rocblas-latest | 22 篇 | ✅ |
| - hipsolver-latest | 20 篇 | ✅ |
| - miopen-latest | 20 篇 | ✅ |
| - rocsparse-latest | 20 篇 | ✅ |
| - composable-kernel-latest | 20 篇 | ✅ |
| - rocprofiler-latest | 19 篇 | ✅ |
| - rocprofiler-sdk-latest | 19 篇 | ✅ |
| - hipblaslt-latest | 19 篇 | ✅ |
| - rocsolver-latest | 18 篇 | ✅ |
| - rocal-latest | 16 篇 | ✅ |
| - rocfft-latest | 13 篇 | ✅ |
| - hipblas-latest | 10 篇 | ✅ |
| - rocwmma-latest | 6 篇 | ✅ |
| - hipfort-latest | 20 篇 (3491KB) | ✅ |
| - rocm-install-linux | 5 篇 | ✅ |
| - hip (旧) | 5 篇 | ✅ |
| - hipify | 4 篇 | ✅ |
| - GitHub Releases | 215 篇 | ✅ |
| CUDA→HIP 映射 | 301 条 | ✅ |
| 论文 | 87 篇 | ✅ |
| 多语言 | 26 篇 | ✅ |
| 定价数据 | 8 源 | ✅ |

---

## 组件清单（15 个）

| 组件 | 状态 |
|------|------|
| ArticleHeader, ArticleMeta, CredibilityStars, LifecycleBadge, TagBadge | ✅ |
| BilingualViewer, ParallelView, InterleavedView | ✅ |
| CompatibilityMatrix, CudaHipMap, ErrorCodeLookup, GlossaryTooltip | ✅ |
| IssueTracker, PriceTracker, PriceChart | ✅ |

## 脚本清单（18 个）

||| 脚本 | 状态 |
||------|------|
| fetch-official, fetch-papers, fetch-asia, fetch-eu, fetch-prices-ebay | ✅ |
| sync-github, classify, translate, verify, release-watch | ✅ |
| generate-docs, gen-papers-sidebar, generate-sidebar, related-articles | ✅ |
| cache-images, normalize-prices, extract-pdf | ✅ |
| **fetch.py (统一抓取入口)** | ✅ 🆕 |

## 数据库清单（Phase 2.0 新增）

|||| 文件/模块 | 说明 | 行数 |
||------|------|------|
|| `db/schema.sql` | 10 张核心表 | ~270 |
|| `db/__init__.py` | 连接池 + WAL | 89 |
|| `db/dao.py` | DAO 层（Article/Source/Tag/CrawlLog） | 527 |
|| `db/migrate.py` | JSON→SQLite 迁移脚本 | 344 |
|| `db/export.py` | SQLite→JSON 导出（兼容 sidebar） | 168 |
|| `crawlers/` 模块 v2 | 三级发现 + 多源抓取 | 🆕 |
|| `crawlers/base.py` | BaseCrawler 抽象类 | ~220 |
|| `crawlers/http_client.py` | httpx 客户端 + ETag 缓存 | ~115 |
|| `crawlers/extractor.py` | 正文提取（trafilatura + pandoc） | ~175 |
|| `crawlers/dedup.py` | URL 规范化 + sha256 去重 | ~115 |
|| `crawlers/url_family.py` | 跨版本 URL 归一化 | ~60 |
|| `crawlers/sitemap.py` | SitemapCrawler (Level 1) | ~140 |
|| `crawlers/sphinx_nav.py` | SphinxNavCrawler (Level 2) | ~115 |
|| `crawlers/github_docs.py` | GithubDocsCrawler (Level 3) | ~70 |
|| `crawlers/rss.py` | RSSCrawler (Blog) | ~80 |
|| `config/amd-sources.yaml` | 44 个源配置 | ~300 |

**DB 统计：**
| 表 | 行数 |
|---|------|
| sources | 8 |
| articles | 56 |
| tags | 72 |
| article_tags | 344 |
| cuda_hip_map | 301 |
| papers | 87 |

## CI 工作流（7 个）

| 工作流 | 触发 | 状态 |
|--------|------|------|
| `sync.yml` | 每日 08:00 | ✅ |
| `translate.yml` | 每日 12:00 | ✅ |
| `verify.yml` | 每日 10:00 | ✅ |
| `validate.yml` | PR 触发 | ✅ *(typecheck + vitest + build)* |
| `deploy.yml` | push main | ✅ |
| `sync-prices.yml` | 周一 11:00 | ✅ 并行 |
| `papers.yml` | 周六 14:00 | ✅ |
| `test-translate.yml` | 手动 | ✅ |

## 文档清单

| 文件 | 状态 |
|------|------|
| `docs/PROGRESS.md` | ✅ |
| `docs/cron-jobs.md` | ✅ 新增 |
| `docs/bugs.md` | ✅ 新增 (15 bugs) |
| `docs/lessons-learned.md` | ✅ 新增 |
| `docs/ops/user-actions.md` | ✅ |
| `docs/ops/git-workflow.md` | ✅ |
| `docs/templates/page-template.md` | ✅ |

---

## 下一步行动

1. **🔴 清理生成文档 broken links/anchors** — 当前 build 已恢复为 warning，但需后续系统性修链
2. **🟠 为价格抓取接入真实 eBay 凭据并替换 mock 数据**
3. **🟡 补充 known issues 自动同步管道**
4. **🟢 Phase 2.5** — SEO 与发布（sitemap/JSON-LD/hreflang + 落地页）
5. **🟢 Phase 2.6** — 监控（Prometheus + Grafana + Sentry）

---

## Git 提交历史（最近 10 条）

| 提交 | 信息 |
|------|------|
| `e497b66` | feat: sync-prices 按国家并行拆分 |
| `07d0129` | fix: 解耦 sync + translate — 独立定时任务 + 增量断点续传 |
| `b19706c` | ci: upgrade test-translate to batch mode |
| `f6dd6a8` | docs: bugs.md 回溯全量 12 个历史 bug |
| `e9379ea` | fix: 全量硬化 Path 常量 — 5 个脚本统一 .resolve() |
| `eebb8ca` | fix: translate.py path resolution + CI diagnostics |
| `874136f` | fix(generate): ../_images/ 路径修正 |
| `09d0298` | fix(ci): validate.yml continue-on-error 缩进 |
| `23f854a` | feat: Phase 9.1 多语言 + Phase 8.6 CI |
| `d16398f` | feat: Phase 8 complete + Phase 11 image cache |

---

> **更新规则：** 每次完成一个任务后，立即更新本文档中对应任务的状态。
