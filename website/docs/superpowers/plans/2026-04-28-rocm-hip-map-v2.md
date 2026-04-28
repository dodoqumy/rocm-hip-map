# rocm-hip-map 实现计划（v2 — 对齐 README）

> **面向 AI 代理的工作者：** 使用 subagent-driven-development 逐任务实现此计划。步骤使用复选框（`- [ ]`）语法来跟踪进度。
>
> **更新日志：**
> - v1 (2026-04-27)：初始计划，聚焦 ROCm 官方 docs
> - v2 (2026-04-28)：对齐 README.md 规格，扩展 HIP、CUDA→HIP、Issue 情报、兼容性矩阵等

**目标：** 建设 **ROCm + HIP 一手情报中外文对照阅读网站**，面向开发者/工程师/研究者。核心价值：官方优先、原文可追溯、双语对照、结构化检索。

**架构：** Docusaurus 3.x (website/) + 内容仓库分层 (docs/ + content/ + data/) + 脚本管道 (scripts/) → GitHub Pages 部署。

**技术栈：** Docusaurus 3 (React/MDX)、TypeScript、Node.js 20+、Python 3 (同步/转换/分类脚本)、GitHub Actions、GitHub Pages

**Docusaurus 选定理由（2026-04-27）：**
- ✅ 原生 i18n + 版本管理 + React 组件扩展，Meta 活跃维护，63k+ stars
- 🔴 MkDocs Material 2025.11 进入维护模式
- README 标注 VitePress "首选" → Docusaurus 在 i18n 原生支持上优于 VitePress（VitePress 的 i18n 需手动管理路径），经调研后选定 Docusaurus

---

## 文件结构（对齐 README.md 第七节）

```text
~/projects/hermes/rocm-hip-map/
├── README.md                          # 项目规格书（已有）
├── LICENSE                            # MIT（已有）
├── CONTRIBUTING.md                    # 贡献指南
├── sources.md                         # 一手来源定义（已有）
├── roadmap.md                         # 路线图
│
├── website/                           # ⭐ Docusaurus 网站框架
│   ├── docusaurus.config.ts           # i18n、版本、导航
│   ├── sidebars.ts                    # 分类侧边栏
│   ├── package.json
│   ├── docs/                          # Docusaurus 文档内容
│   │   └── getting-started/
│   │       ├── index.md
│   │       └── what-is-rocm.md
│   ├── src/
│   │   ├── components/
│   │   │   ├── BilingualViewer/       # 双语对照（左右分栏 + 逐段对照）
│   │   │   ├── ArticleMeta/           # 元信息：可信度星级 + 生命周期 + 原文链接
│   │   │   ├── CompatibilityMatrix/   # GPU×ROCm×OS×Framework 交叉表
│   │   │   ├── CudaHipMap/           # CUDA→HIP API 对照表
│   │   │   ├── ErrorCodeLookup/       # 错误码查询
│   │   │   └── VersionSelector/       # 版本选择器
│   │   ├── css/custom.css
│   │   └── pages/
│   ├── i18n/zh-Hans/                  # Docusaurus i18n 翻译
│   └── static/img/
│
├── docs/                              # 📚 内容仓库（README 规划，非 Docusaurus docs）
│   ├── index.md                       # 文档总索引
│   ├── articles/                      # 文章
│   │   ├── official/                  # 官方来源
│   │   │   ├── amd/                   #   AMD 官方
│   │   │   ├── rocm/                  #   ROCm 官方
│   │   │   ├── pytorch/               #   PyTorch 官方 ROCm
│   │   │   └── paddle/                #   PaddlePaddle 官方
│   │   ├── github/                    # GitHub 来源
│   │   │   ├── issues/                #   Issues
│   │   │   └── prs/                   #   Pull Requests
│   │   └── papers/                    # 学术论文
│   ├── bilingual/                     # 双语对照内容
│   │   ├── en-zh/                     #   英文原文→中文翻译
│   │   └── zh-en/                     #   中文原文→英文翻译
│   ├── compatibility/                 # 兼容性矩阵
│   │   ├── gpu.md                     #   GPU 兼容
│   │   ├── os.md                      #   OS 兼容
│   │   ├── frameworks.md              #   框架兼容
│   │   └── drivers.md                 #   驱动兼容
│   ├── versions/                      # 版本专项
│   │   ├── rocm-5.x.md
│   │   ├── rocm-6.x.md
│   │   └── rocm-7.x.md
│   ├── cuda-to-hip/                   # CUDA→HIP 对照
│   │   ├── api-map.md                 #   API 对照表
│   │   ├── hipify.md                  #   hipify 工具指南
│   │   └── migration.md               #   迁移指南
│   ├── errors/                        # 错误码库
│   │   ├── runtime.md                 #   运行时错误
│   │   ├── install.md                 #   安装错误
│   │   └── compile.md                 #   编译错误
│   └── tags/                          # 标签定义
│
├── content/                           # 🗂️ 原始 & 翻译内容
│   ├── raw/
│   │   ├── english/                   #   英文原文存档
│   │   └── chinese/                   #   中文原文存档
│   └── translated/
│       ├── zh/                        #   翻译为中文
│       └── en/                        #   翻译为英文
│
├── data/                              # 📊 结构化数据
│   ├── articles.json                  #   文章索引（已有模板）
│   ├── versions.json                  #   版本数据
│   ├── gpu.json                       #   GPU 型号库
│   ├── drivers.json                   #   驱动版本库
│   ├── issues.json                    #   Issue 情报
│   ├── cuda-hip-api-map.json          #   CUDA→HIP API 映射（已有）
│   ├── known-issues.json              #   已知问题库（已有）
│   └── tags.json                      #   标签定义
│
├── scripts/                           # 🛠️ 自动化脚本
│   ├── fetch-official.py              #   抓取官方文档
│   ├── sync-github.py                 #   同步 GitHub Issues/PRs
│   ├── classify.py                    #   自动分类 + 标签
│   ├── translate.py                   #   AI 翻译管道
│   ├── build-index.py                 #   构建全局索引
│   └── validate-links.py             #   链接有效性检查
│
├── glossary/                          # 📖 术语表
│   └── rocm-terms.yaml               #   中英术语对照
│
└── .github/workflows/
    ├── deploy.yml                     #   构建部署到 GitHub Pages
    ├── sync.yml                       #   定时同步上游
    └── validate.yml                   #   链接 + 数据校验
```

---

## 核心原则（来自 README 第二节，所有 Phase 必须遵守）

1. **只收录一手情报** — 不转载二手/搬运文章
2. **官方来源优先** — AMD/ROCm/PyTorch 官方文档优先级最高
3. **所有文章保留原文链接** — 可追溯、可验证
4. **标注发布时间/来源/版本** — frontmatter 必备字段
5. **中英双语阅读** — 原文为英文→提供中文翻译；原文为中文→提供英文翻译
6. **翻译与原文分离** — 原文不可被翻译覆盖
7. **可信度评级** — 每篇文章标注 ★（官方★★★★★ → 实验★★）
8. **生命周期状态** — 标注"最新""已过时""即将废弃""已弃用"

---

## Frontmatter 元数据规范（新增字段）

每篇文章的 YAML frontmatter 必须包含以下字段：

```yaml
---
title: "What is ROCm?"
source_url: "https://rocm.docs.amd.com/en/latest/what-is-rocm.html"
source_type: official           # official | github-issue | github-pr | blog | paper | community
source_org: amd                 # amd | rocm | pytorch | tensorflow | paddle | llvm | mesa | linux
published_date: 2026-04-17
synced_date: 2026-04-28
original_lang: en               # en | zh
credibility: 5                  # 1-5 ★
lifecycle: latest               # latest | outdated | deprecating | deprecated
version: "7.2.2"
rocm_versions: ["7.0", "7.1", "7.2"]
tags: [intro, getting-started]
os: [linux, windows]
gpu: [mi300x, mi250, mi210, rx7900, rx6800]
gpu_arch: [cdna3, cdna2, rdna3]
driver: [amdgpu-6.x]
frameworks: [pytorch, tensorflow]
difficulty: beginner            # beginner | intermediate | advanced | reference
---
```

**字段说明：**

| 字段 | 类型 | 必需 | 说明 |
|------|------|------|------|
| `source_type` | enum | ✅ | `official` / `github-issue` / `github-pr` / `blog` / `paper` / `community` |
| `source_org` | enum | ✅ | 来源组织 |
| `credibility` | int 1-5 | ✅ | ★ 评级（见下表） |
| `lifecycle` | enum | ✅ | 内容时效状态 |
| `rocm_versions` | list | ✅ | 适用的 ROCm 版本范围 |
| `os` | list | ✅ | 适用操作系统 |
| `gpu` | list | ✅ | 适用 GPU 型号 |
| `gpu_arch` | list | ✅ | GPU 架构（CDNA2/CDNA3/RDNA3） |
| `driver` | list | ✅ | 驱动版本 |
| `frameworks` | list | ⬜ | 相关框架 |

**可信度评级：**
| ★ | 含义 | 来源 |
|---|------|------|
| ★★★★★ | 官方权威 | AMD/ROCm 官方文档正式版 |
| ★★★★ | 官方渠道 | GitHub org README、官方博客、release notes |
| ★★★ | 社区权威 | GitHub Issues/Discussions、PyTorch 官方 ROCm 文档 |
| ★★ | 实验性质 | WIP PR、RFC、实验性文档 |
| ★ | 仅供参考 | 第三方翻译、个人博客（本项目不收录 ★） |

**生命周期状态：**
| 状态 | 标签颜色 | 含义 |
|------|---------|------|
| `latest` | 🟢 绿色 | 当前推荐阅读 |
| `outdated` | 🟡 黄色 | 部分内容过时但仍可参考 |
| `deprecating` | 🟠 橙色 | 即将在新版本中废弃 |
| `deprecated` | 🔴 红色 | 已废弃，仅作历史存档 |

---

## 实施 Phase（重新编排）

### ✅ Phase 0：环境准备（已完成）
- Node.js v22.22.2 / npm 10.9.7 / Git / pandoc 3.9 / Python 3.11

### ✅ Phase 1：Docusaurus 脚手架 + i18n + 版本管理（已完成）
- Docusaurus 3.10 项目在 `website/`
- 中英双语 i18n、ROCm 7.2.2 版本管理
- 首页 + 首篇文章 What is ROCm?
- 构建通过（en + zh-Hans）

### 🔲 Phase 2：分类与标签系统（重新设计）
目标：将 README 的多维分类落地为 Docusaurus 标签 + 侧边栏 + frontmatter。

#### 任务 2.1：更新 frontmatter 规范
**文件：** 修改 `website/docs/getting-started/what-is-rocm.md`、新建 `data/tags.json`

- [ ] 将现有文章 frontmatter 升级到 v2 规范（添加 `source_type`, `credibility`, `lifecycle`, `gpu`, `gpu_arch`, `driver`, `frameworks`）
- [ ] 创建 `data/tags.json` 定义所有合法标签值

#### 任务 2.2：创建 ArticleMeta 组件（含可信度星级 + 生命周期徽章）
**文件：** `website/src/components/ArticleMeta/index.tsx`、`TagBadge.tsx`、`CredibilityStars.tsx`

- [ ] 可信度星级组件（★★★★★ 渲染）
- [ ] 生命周期徽章（颜色编码）
- [ ] GPU / OS / Driver / Framework 多维标签展示
- [ ] 原文链接 + 来源标注

#### 任务 2.3：扩展侧边栏（README 分类体系）
**文件：** `website/sidebars.ts`

- [ ] 按 README 主题分类重组：ROCm Core / HIP Programming / GPU Driver / PyTorch ROCm / TensorFlow ROCm / Performance / Debugging / Compatibility / Installation / Release Notes / Hardware Support
- [ ] 每个分类设置 `collapsible` + 图标

---

### 🔲 Phase 3：内容管道 — 多渠道同步

#### 任务 3.1：官方文档同步脚本
**文件：** `scripts/fetch-official.py`

- [ ] 支持多源：ROCm docs / AMD Blog RSS / PyTorch ROCm docs / TensorFlow ROCm docs
- [ ] RST→MD 转换（pandoc）
- [ ] 自动注入 v2 frontmatter
- [ ] 去重（URL 指纹比对）
- [ ] `--dry-run` 模式

#### 任务 3.2：GitHub Issues/PRs 同步脚本
**文件：** `scripts/sync-github.py`

- [ ] 从 `github.com/ROCm/*` 仓库拉取 Issues/PRs
- [ ] 筛选含 `bug`/`workaround`/`fix` 标签的项
- [ ] 提取：标题、描述、workaround、fix version、影响硬件
- [ ] 保存到 `data/known-issues.json` + `docs/articles/github/issues/`

#### 任务 3.3：自动分类脚本
**文件：** `scripts/classify.py`

- [ ] 根据 URL/内容自动判定 `source_type`、`source_org`
- [ ] 自动打标签（GPU 型号检测、OS 检测、框架检测）
- [ ] 输出结构化 JSON 到 `data/articles.json`

#### 任务 3.4：Release Watch 脚本
**文件：** `scripts/release-watch.py`、`.github/workflows/sync.yml`

- [ ] 监控 ROCm 版本页 (`release/versions.html`)
- [ ] 监控 PyTorch ROCm release
- [ ] 监控 HIP API changelog
- [ ] 检测到新版本 → 自动创建 issue 或通知

---

### 🔲 Phase 4：双语对照 + AI 翻译管道

#### 任务 4.1：BilingualViewer 组件
**文件：** `website/src/components/BilingualViewer/`

- [ ] 左右分栏模式（`ParallelView`）
- [ ] 逐段对照模式（`InterleavedView`）
- [ ] 模式切换按钮
- [ ] 原文链接 + 可信度星级 + 生命周期徽章
- [ ] 移动端自适应（左右→上下）

#### 任务 4.2：AI 翻译管道
**文件：** `scripts/translate.py`、`glossary/rocm-terms.yaml`

- [ ] 基于术语表确保翻译一致性
- [ ] 段落级翻译（保留代码块）
- [ ] 双语内容存入 `content/translated/` + `docs/bilingual/`
- [ ] 支持多翻译后端（DeepL / GPT-4 / 本地模型）

#### 任务 4.3：术语表完善
**文件：** `glossary/rocm-terms.yaml`、`website/src/components/GlossaryTooltip/`

- [ ] 扩展术语表（CUDA↔HIP 对照、ROCm 专有术语）
- [ ] GlossaryTooltip 组件（悬浮显示中文解释）

---

### 🔲 Phase 5：特色功能组件

#### 任务 5.1：兼容性矩阵组件
**文件：** `website/src/components/CompatibilityMatrix/`、`docs/compatibility/`

- [ ] 交叉表：GPU × ROCm 版本 × OS × Framework
- [ ] 支持筛选/排序
- [ ] 数据源：`data/gpu.json` + `data/drivers.json`
- [ ] 渲染为 Docusaurus MDX 页面

#### 任务 5.2：CUDA→HIP API 对照表
**文件：** `website/src/components/CudaHipMap/`、`docs/cuda-to-hip/api-map.md`

- [ ] API 对照表（动态搜索 + 筛选）
- [ ] 数据源：`data/cuda-hip-api-map.json`（已有模板）
- [ ] hipify 工具使用指南页面

#### 任务 5.3：错误码查询
**文件：** `website/src/components/ErrorCodeLookup/`、`docs/errors/`

- [ ] 错误码搜索（支持中英文）
- [ ] 每个错误码关联：原因、workaround、版本修复信息
- [ ] 数据源：`data/known-issues.json`

#### 任务 5.4：Issue 情报面板
**文件：** `website/src/components/IssueTracker/`

- [ ] 展示已知 bug 列表（来自 GitHub Issues）
- [ ] 筛选：按 GPU/ROCm 版本/状态
- [ ] 链接回 GitHub Issue

---

### 🔲 Phase 6：部署与 CI/CD

#### 任务 6.1：GitHub Pages 部署
**文件：** `.github/workflows/deploy.yml`（已有模板）

- [ ] 确认 GitHub Pages 在仓库设置中启用
- [ ] 确认 Actions 有写入权限
- [ ] 首次部署验证

#### 任务 6.2：定时同步工作流
**文件：** `.github/workflows/sync.yml`

- [ ] 每周自动运行 `fetch-official.py` + `sync-github.py` + `classify.py` + `translate.py`
- [ ] 检测到新内容 → 自动 commit + push → 触发 deploy
- [ ] Release Watch 检测到新版本 → 创建 GitHub Issue

#### 任务 6.3：数据校验工作流
**文件：** `.github/workflows/validate.yml`

- [ ] `validate-links.py` 检查所有原文链接是否可达
- [ ] frontmatter 规范校验
- [ ] 构建验证（PR 上自动运行）

---

### 🔲 Phase 7：内容扩充（持续）

- [ ] Phase 7.1：批量导入 ROCm 7.2.2 全套官方文档（~50 篇）
- [ ] Phase 7.2：同步 2025-2026 年关键 GitHub Issues
- [ ] Phase 7.3：建立 CUDA→HIP API 映射数据库（≥200 条）
- [ ] Phase 7.4：收录 PyTorch/TensorFlow ROCm 官方文档
- [ ] Phase 7.5：中文学术论文 + AMD 中国官方资料
- [ ] Phase 7.6：启用 Algolia DocSearch 双语搜索
- [ ] Phase 7.7：图片文字翻译 — OCR 提取原文图片中文字 → 翻译 → 重生成对照图片（README §三）
- [ ] Phase 7.8：网站分析（GA/Umami）用户行为统计

---

## Phase 优先级矩阵

| 优先级 | Phase | 依赖 | 估时 |
|--------|-------|------|------|
| 🔴 P0 | Phase 2（分类标签） | Phase 1 | 30min |
| 🔴 P0 | Phase 4（双语对照+翻译） | Phase 1 | 60min |
| 🟡 P1 | Phase 3（内容管道） | Phase 2 | 90min |
| 🟡 P1 | Phase 5（特色组件） | Phase 2+4 | 120min |
| 🟢 P2 | Phase 6（CI/CD） | Phase 1-5 | 30min |
| 🟢 P2 | Phase 7（内容扩充） | 全部 | 持续 |

---

## 与 README 需求覆盖度

| README 需求 | 对应 Phase | 覆盖 |
|------------|-----------|------|
| 一手情报原则 | Phase 3 (source_type 字段) | ✅ |
| 官方优先 + 原文链接 | Phase 2 (ArticleMeta) + Phase 4 (BilingualViewer) | ✅ |
| 双语阅读（左右分栏） | Phase 4 | ✅ |
| 按主题/环境/GPU/版本/驱动分类 | Phase 2 (frontmatter + 侧边栏) | ✅ |
| 搜索功能 | Phase 7.6 (Algolia) + Docusaurus 内置 | ✅ |
| 兼容性矩阵 | Phase 5.1 | ✅ |
| Issue 情报系统 | Phase 3.2 + Phase 5.4 | ✅ |
| Release Watch | Phase 3.4 | ✅ |
| 可信度评级 ★ | Phase 2.2 | ✅ |
| 生命周期状态 | Phase 2.2 | ✅ |
| CUDA→HIP 对照 | Phase 5.2 | ✅ |
| 常见错误码库 | Phase 5.3 | ✅ |
| 图片文字翻译 | Phase 7.7 (OCR + 翻译 + 重生成) | ⏳ |
| 收藏/阅读历史 | Phase 7+ (需数据库 ECS) | ⏳ |
