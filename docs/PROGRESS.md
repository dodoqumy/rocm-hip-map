# 📋 rocm-hip-map 开发进度跟踪

**最后更新：** 2026-04-28 09:30 CST  
**当前分支：** `main`  
**最新提交：** `ac24686` — docs: add live preview URL to README  
**网站预览：** https://dodoqumy.github.io/rocm-hip-map/  
**用户操作手顺：** [docs/ops/user-actions.md](docs/ops/user-actions.md) 🔧

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
Phase 7  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   0% 🔲
────────────────────────────────────────────
总体     ██████████████████████░░░░░░░░░░  71%
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
| 5.5 | `docs/compatibility/` 页面 | 🔲 | 兼容性矩阵 MDX 页面 |
| 5.6 | `docs/cuda-to-hip/` 页面 | 🔲 | CUDA→HIP 对照 MDX 页面 |
| 5.7 | `docs/errors/` 页面 | 🔲 | 错误码库 MDX 页面 |
| 5.8 | 数据文件填充 | 🔲 | `gpu.json`, `drivers.json`, `versions.json` 等 |

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
| 7.1 | 批量导入 ROCm 7.2.2 全套文档（~50篇） | 🔲 | |
| 7.2 | 同步 2025-2026 GitHub Issues | 🔲 | |
| 7.3 | CUDA→HIP API 映射库（≥200条） | 🔲 | 现有模板 `data/cuda-hip-api-map.json` |
| 7.4 | PyTorch/TensorFlow ROCm 官方文档 | 🔲 | |
| 7.5 | 中文学术论文 + AMD 中国资料 | 🔲 | |
| 7.6 | Algolia DocSearch 双语搜索 | 🔲 | |
| 7.7 | 图片文字翻译（OCR→翻译→重生成） | 🔲 | 需求已写入 README §三 和 v2 计划 |
| 7.8 | 网站分析（GA/Umami） | 🔲 | |

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

---

## 数据文件清单

| 文件 | 状态 | 备注 |
|------|------|------|
| `data/tags.json` | ✅ 已填充 | 标签定义 |
| `data/cuda-hip-api-map.json` | 🟡 模板 | 2 条示例，待扩充 |
| `data/known-issues.json` | 🟡 模板 | 1 条示例，待扩充 |
| `data/articles.json` | 🔲 | 文章索引，脚本产出 |
| `data/versions.json` | 🔲 | 版本数据 |
| `data/gpu.json` | 🔲 | GPU 型号库 |
| `data/drivers.json` | 🔲 | 驱动版本库 |
| `data/issues.json` | 🔲 | Issue 情报，脚本产出 |

---

## 下一步行动（优先级排序）

1. **🔴 Phase 3.7** — 首次正式同步运行（CI push 后自动触发 → 填充 content/raw/ + data/articles.json）
2. **🔴 Phase 4.8** — 翻译管道首次运行（CI 同步中自动翻译 22+ 篇）
3. **🟡 Phase 5.5-5.7** — 为特色组件创建对应的 MDX 文档页面
4. **🟢 Phase 7.1** — 批量导入 ROCm 7.2.2 官方文档 50 篇
5. **🟢 Phase 7.3** — 扩充 CUDA→HIP API 映射库 ≥200 条

---

## Git 提交历史（最近 10 条）

| 提交 | 信息 |
|------|------|
| `ac24686` | docs: add live preview URL to README |
| `8e32b1f` | docs: add image text translation requirement |
| `660ae75` | feat: Phase 3-5 complete — scripts, bilingual viewer, feature components |
| `986e0c5` | ci: retrigger deploy after Actions enabled |
| `d5cf347` | ci: trigger deploy after enabling Actions + Pages |
| `ffe4fa7` | ci: fix GitHub Pages deploy — use actions/deploy-pages |
| `85e7d13` | feat: Phase 2 — v2 frontmatter + classification + ArticleMeta component |
| `52ef2ce` | docs: comprehensive v2 plan aligned with README.md spec |
| `0fbad97` | feat: migrate Docusaurus website to website/ |
| `cbcc6f6` | Initial commit |

---

> **更新规则：** 每次完成一个任务后，立即更新本文档中对应任务的状态。提交时附带 `docs: update PROGRESS.md` 信息。
