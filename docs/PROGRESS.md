# 📋 rocm-hip-map 开发进度跟踪

**最后更新：** 2026-04-28 10:30 CST  
**当前分支：** `main`  
**最新提交：** `c0df267` — docs(ops): 添加 Git 工作流文档  
**网站预览：** https://dodoqumy.github.io/rocm-hip-map/  
**用户操作手顺：** [docs/ops/user-actions.md](docs/ops/user-actions.md) 🔧  
**Git 工作流：** [docs/ops/git-workflow.md](docs/ops/git-workflow.md) 📋  
**MDX 模板规范：** [docs/templates/page-template.md](docs/templates/page-template.md) 📄

---

## 总体进度

```
Phase 0  ████████████████████████████████ 100% ✅
Phase 1  ████████████████████████████████ 100% ✅
Phase 2  ████████████████████████████████ 100% ✅
Phase 3  ████████████████████████████████ 100% ✅
Phase 4  ██████████████████████░░░░░░░░░░  67% 🟡 (翻译管道待首次运行)
Phase 5  ████████████████████████████████ 100% ✅
Phase 6  ████████████████████████████████ 100% ✅
Phase 7  ████████████████░░░░░░░░░░░░░░░░  50% 🟡 (304条API + 校验管道就绪)
Phase 8  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   0% 🔲 (论文搜集翻译 — 计划已定)
────────────────────────────────────────────
总体     ████████████████████░░░░░░░░░░░░  80%
```

**图例：** ✅ 完成 · 🟡 部分完成/进行中 · 🔲 未开始 · ❌ 阻塞

---

## Phase 0：环境准备

| # | 任务 | 状态 | 备注 |
|---|------|------|------|
| 0.1 | Node.js v22.22.2 | ✅ | WSL Ubuntu |
| 0.2 | npm 10.9.7 | ✅ | |
| 0.3 | Git 配置 | ✅ | |
| 0.4 | pandoc 3.9 | ✅ | RST→MD 转换 |
| 0.5 | Python 3.11 | ✅ | 脚本运行环境 |
| 0.6 | 项目初始化 git init | ✅ | `660ae75` 提交 |

---

## Phase 1：Docusaurus 脚手架

| # | 任务 | 状态 | 备注 |
|---|------|------|------|
| 1.1 | `create-docusaurus` 项目 | ✅ | v3.10，`website/` 目录 |
| 1.2 | i18n 双语言配置 | ✅ | `en` + `zh-Hans` |
| 1.3 | 版本管理 | ✅ | ROCm 7.2.2 |
| 1.4 | 首篇文章 | ✅ | `getting-started/what-is-rocm.mdx` |
| 1.5 | 首页配置 | ✅ | HomepageFeatures 组件 |
| 1.6 | 构建通过 | ✅ | `en` + `zh-Hans` 双版本零错误 |

---

## Phase 2：分类与标签系统

| # | 任务 | 状态 | 备注 |
|---|------|------|------|
| 2.1 | v2 frontmatter 规范升级 | ✅ | `what-is-rocm.md` 已更新 |
| 2.2 | `data/tags.json` 标签定义 | ✅ | 所有合法标签值 |
| 2.3 | CredibilityStars 组件 | ✅ | ★★★★★ 渲染 |
| 2.4 | LifecycleBadge 组件 | ✅ | 🟢🟡🟠🔴 颜色编码 |
| 2.5 | TagBadge 多维标签 | ✅ | GPU/OS/Driver/Framework |
| 2.6 | ArticleHeader 统一包装 | ✅ | 含原文链接 + 来源标注 |
| 2.7 | `styles.module.css` | ✅ | 组件样式 |

---

## Phase 3：内容管道 — 多渠道同步

| # | 任务 | 状态 | 备注 |
|---|------|------|------|
| 3.1 | `fetch-official.py` | ✅ | 多源支持 + RST→MD + 去重 + `--dry-run` |
| 3.2 | `sync-github.py` | ✅ | Issues/PRs 同步脚本 |
| 3.3 | `classify.py` | ✅ | 自动分类 + 标签脚本 |
| 3.4 | `release-watch.py` | ✅ | 版本更新追踪脚本 |
| 3.5 | 干跑测试 | ✅ | 22 篇文章抓取正常 |
| 3.6 | 定时同步 CI (`sync.yml`) | ✅ | 每天 08:00 CST |
| 3.7 | 首次正式同步运行 | 🟡 进行中 | push 后 CI 自动执行 |

---

## Phase 4：双语对照 + AI 翻译管道

| # | 任务 | 状态 | 备注 |
|---|------|------|------|
| 4.1 | ParallelView 组件 | ✅ | 左右分栏模式 |
| 4.2 | InterleavedView 组件 | ✅ | 逐段对照模式 |
| 4.3 | BilingualViewer 主组件 | ✅ | 模式切换 + 元信息展示 |
| 4.4 | 移动端自适应 | ✅ | 左右→上下 |
| 4.5 | `scripts/translate.py` | ✅ | 4 后端就绪：DeepSeek / opencode-go / OpenAI / DeepL |
| 4.6 | `glossary/rocm-terms.yaml` | ✅ | CUDA↔HIP 术语对照 |
| 4.7 | GlossaryTooltip 组件 | ✅ | 悬浮术语解释 |
| 4.8 | 翻译管道实际对接运行 | 🟡 进行中 | 首次批量翻译 API Key 就绪 |
| 4.9 | `docs/bilingual/` 内容填充 | 🟡 进行中 | 翻译产出后自动填充 |

---

## Phase 5：特色功能组件

| # | 任务 | 状态 | 备注 |
|---|------|------|------|
| 5.1 | CompatibilityMatrix 组件 | ✅ | GPU×ROCm×OS×Framework 交叉表 |
| 5.2 | CudaHipMap 组件 | ✅ | CUDA→HIP API 对照 + 搜索 |
| 5.3 | ErrorCodeLookup 组件 | ✅ | 错误码搜索 + 原因 + workaround |
| 5.4 | IssueTracker 组件 | ✅ | GitHub Issues 展示 + 筛选 |
| 5.5 | `docs/compatibility/overview.mdx` | ✅ | 组件 MDX 页面 + 来源链接 + 使用提示 |
| 5.6 | `docs/cuda-to-hip/api-map.mdx` | ✅ | CUDA→HIP 对照 MDX 页面 |
| 5.7 | `docs/errors/index.mdx` | ✅ | 错误码库 MDX 页面 |
| 5.8 | `docs/issues/index.mdx` | ✅ | Issue 情报 MDX 页面 |
| 5.9 | 侧边栏同步 | ✅ | 4 个新分类已接入 sidebars.ts |

---

## Phase 6：部署与 CI/CD

| # | 任务 | 状态 | 备注 |
|---|------|------|------|
| 6.1 | GitHub Pages 启用 | ✅ | 仓库 Settings → Pages → Actions |
| 6.2 | Actions 写入权限 | ✅ | Settings → Actions → Read/write |
| 6.3 | `deploy.yml` 工作流 | ✅ | 自动构建 + 部署到 Pages |
| 6.4 | 首次部署成功 | ✅ | `https://dodoqumy.github.io/rocm-hip-map/` |
| 6.5 | `sync.yml` 定时同步 | ✅ | 每天 08:00 CST 自动运行（抓取→分类→翻译→提交） |
| 6.6 | `validate.yml` 数据校验 | ✅ | PR 触发：链接有效性 + frontmatter + 构建验证 |
| 6.7 | Release Watch → Issue 通知 | ✅ | 版本检测已集成进 sync.yml |

---

## Phase 7：内容扩充（持续）

| # | 任务 | 状态 | 备注 |
|---|------|------|------|
| 7.1 | 批量导入 ROCm 7.2.2 全套文档（~68篇） | 🟡 | 68 篇已抓取，MDX 生成/翻译待完成 |
| 7.2 | 同步 2025-2026 GitHub Issues | 🔲 | |
| 7.3 | CUDA→HIP API 映射库（304条） | ✅ | 完整映射：设备/内存/流/事件/图/库/原子操作等 25 类 |
| 7.4 | PyTorch/TensorFlow ROCm 官方文档 | 🔲 | |
| 7.5 | 中文学术论文 + AMD 中国资料 | 🔲 | |
| 7.6 | Algolia DocSearch 双语搜索 | 🔲 | |
| 7.7 | 图片文字翻译（OCR→翻译→重生成） | 🔲 | 需求已写入 README §三 |
| 7.8 | 网站分析（GA/Umami） | 🔲 | |
| 7.9 | 内容校验管道 `verify.py` | ✅ | 3 维校验 + LLM 审查 + 自动打 verified 标签 |
| 7.10 | 定时校验 CI (`verify.yml`) | ✅ | 每天 10:00 CST + 手动触发 |

---

## Phase 8：ROCm/HIP 技术论文搜集与翻译（新增）

> 详细计划：[docs/plans/phase8-papers.md](docs/plans/phase8-papers.md)

| # | 任务 | 状态 | 备注 |
|---|------|------|------|
| 8.1 | `scripts/fetch-papers.py` arXiv 搜索脚本 | 🔲 | 6 组查询，Atom XML 解析 |
| 8.2 | `scripts/extract-pdf.py` PDF 提取脚本 | 🔲 | PyMuPDF → Markdown |
| 8.3 | `translate.py` 论文专用 prompt 适配 | 🔲 | 摘要+结论优先，数学符号保护 |
| 8.4 | `generate-docs.py` paper 类型适配 | 🔲 | PaperArticleHeader 组件 |
| 8.5 | 侧边栏 📜 分类 + arXiv 子分类 | 🔲 | |
| 8.6 | CI 集成（每周同步） | 🔲 | sync.yml 或独立 workflow |
| 8.7 | 部署后验证 ≥5 篇论文 | 🔲 | |

---

## 组件清单（13 个）

| 组件 | 文件 | 状态 |
|------|------|------|
| ArticleHeader | `website/src/components/ArticleHeader.tsx` | ✅ |
| ArticleMeta (index) | `website/src/components/ArticleMeta/index.tsx` | ✅ |
| CredibilityStars | `website/src/components/ArticleMeta/CredibilityStars.tsx` | ✅ |
| LifecycleBadge | `website/src/components/ArticleMeta/LifecycleBadge.tsx` | ✅ |
| TagBadge | `website/src/components/ArticleMeta/TagBadge.tsx` | ✅ |
| BilingualViewer | `website/src/components/BilingualViewer/index.tsx` | ✅ |
| ParallelView | `website/src/components/BilingualViewer/ParallelView.tsx` | ✅ |
| InterleavedView | `website/src/components/BilingualViewer/InterleavedView.tsx` | ✅ |
| CompatibilityMatrix | `website/src/components/CompatibilityMatrix.tsx` | ✅ |
| CudaHipMap | `website/src/components/CudaHipMap.tsx` | ✅ |
| ErrorCodeLookup | `website/src/components/ErrorCodeLookup.tsx` | ✅ |
| GlossaryTooltip | `website/src/components/GlossaryTooltip.tsx` | ✅ |
| IssueTracker | `website/src/components/IssueTracker.tsx` | ✅ |

---

## 脚本清单（5 个）

| 脚本 | 文件 | 状态 | 干跑测试 |
|------|------|------|----------|
| fetch-official | `scripts/fetch-official.py` | ✅ | ✅ 22 篇文章 |
| sync-github | `scripts/sync-github.py` | ✅ | ✅ |
| classify | `scripts/classify.py` | ✅ | ✅ |
| translate | `scripts/translate.py` | ✅ | ✅ |
| release-watch | `scripts/release-watch.py` | ✅ | ✅ |
| verify | `scripts/verify.py` | ✅ | ✅ 3 维校验 |

---

## 数据文件清单

| 文件 | 状态 | 备注 |
|------|------|------|
| `data/tags.json` | ✅ 已填充 | 标签定义 |
| `data/cuda-hip-api-map.json` | ✅ 304 条 | 25 类完整映射（HIPIFY 7.2 规范） |
| `data/known-issues.json` | 🟡 模板 | 1 条示例，待扩充 |
| `data/articles.json` | 🔲 | 文章索引，脚本产出 |
| `data/versions.json` | 🔲 | 版本数据 |
| `data/gpu.json` | 🔲 | GPU 型号库 |
| `data/drivers.json` | 🔲 | 驱动版本库 |
| `data/issues.json` | 🔲 | Issue 情报，脚本产出 |

## 文档清单

| 文件 | 状态 | 备注 |
|------|------|------|
| `docs/PROGRESS.md` | ✅ | 开发进度跟踪 |
| `docs/ops/user-actions.md` | ✅ | 用户操作手顺 |
| `docs/ops/git-workflow.md` | ✅ | Git 工作流文档 |
| `docs/templates/page-template.md` | ✅ | MDX 页面模板规范 |

---

## 下一步行动（优先级排序）

1. **🔴 Phase 8.1** — arXiv 论文抓取脚本（已调研：arXiv API 可用，已有 5+ 篇 ROCm/HIP 论文）
2. **🟡 Phase 4.8** — sync.yml 首次自动翻译完成验证（翻译进行中 30min+，可能 opencode 限速）
3. **🟡 Phase 4.9** — `docs/bilingual/` 内容填充（翻译产出后自动写入）
4. **🟢 Phase 7.1** — 文章正文嵌入（正在修复 generate-docs.py）
5. **🟢 Phase 7.6** — 接入 Algolia DocSearch 双语搜索

---

## Git 提交历史（最近 10 条）

| 提交 | 信息 |
|------|------|
| `c0df267` | docs(ops): 添加 Git 工作流文档 |
| `cb46042` | fix: Docusaurus build passes — remove BilingualViewer from auto-generated pages |
| `412b2d1` | fix: repair generate-docs.py f-string syntax error |
| `a7497f7` | feat: Phase 7.1 bulk import 68 ROCm docs + verify pipeline + IssueNotice |
| `b3155d4` | feat: Phase 7.3 + 7.9 — 304-entry CUDA→HIP API map + verify pipeline |
| `0c20bd2` | feat: Phase 5 complete — 4 feature component MDX pages + sidebar wiring |
| `5c63657` | feat: Phase 6 complete — sync.yml (daily) + validate.yml (PR triggers) |
| `9291c20` | feat: add DeepSeek/opencode-go translation backend + ops/user-actions.md |
| `a03d90e` | docs: add real-time PROGRESS.md tracking (Phase 0-7 tasklist) + link in README |
| `ac24686` | docs: add live preview URL to README |

---

> **更新规则：** 每次完成一个任务后，立即更新本文档中对应任务的状态。提交时附带 `docs: update PROGRESS.md` 信息。
