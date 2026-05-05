# rocm-hip-map Review 报告

## 执行摘要

- **审查日期：** 2026-05-02
- **审查范围：** 10 个功能模块 / 前端组件、Python 数据管道、爬虫、数据库、CI 工作流、测试基线
- **总体结论：** 项目在“功能存在性”上整体较强，多个核心模块已经落地；但在“可验证性”上存在明显短板：**前端 typecheck 失败、前后端测试基础设施几乎为空、部分本地依赖缺失、爬虫旧架构存在 API 漂移、价格数据尚未落地**。因此本次结论不是“功能未实现”，而是 **“实现较多，但工程质量与验收闭环不达标”**。

---

## 审查证据来源

1. `docs/plans/2026-05-02-core-features-review.md`
2. `README.md`
3. `docs/PROGRESS.md`
4. 代码库直接验证：
   - `website` TypeScript typecheck
   - `website` production build
   - Python 脚本 `--help` / import 验证
   - SQLite 数据库查询
   - 背景 explore / librarian 审查结果

---

## 功能达成情况

| 模块 | README / PROGRESS 预期 | 实际实现 | 达成状态 | 评分 |
|------|------------------------|----------|----------|------|
| Task 1 双语阅读组件 | 左右分栏、逐段对照、移动端适配 | `BilingualViewer` / `ParallelView` / `InterleavedView` / `styles.module.css` 全部存在，且 MDX 已使用 | **部分达成**：功能实现 ✅，但 `npm run typecheck` ❌、零测试 ❌ | 7/10 |
| Task 2 文章元信息组件 | 标题、来源、链接、发布时间、标签、可信度、生命周期 | `ArticleHeader`、`ArticleMeta`、`CredibilityStars`、`LifecycleBadge`、`TagBadge` 已广泛接入（178 篇 MDX 使用 `ArticleHeader`） | **部分达成**：功能实现 ✅，typecheck 受前端错误影响 ❌，零测试 ❌ | 7/10 |
| Task 3 CUDA→HIP / 错误码 / 兼容性矩阵 | 对照数据库、错误码库、矩阵 | `CudaHipMap`、`ErrorCodeLookup`、`CompatibilityMatrix` 都存在；CUDA→HIP 304 条；兼容矩阵组件存在 | **部分达成**：功能实现 ✅，但零测试 ❌；错误码数据较弱（`known-issues.json` 仍是模板感强） | 7/10 |
| Task 4 翻译管道 | 多后端、术语表、增量翻译、workflow | `translate.py` 具备多后端、增量、术语表、paper/doc 模式；`translate.yml` 存在 | **部分达成**：功能实现 ✅，但系统 Python 缺 `yaml`，本地直接执行失败；零测试 ❌ | 6/10 |
| Task 5 爬虫框架 v2 | BaseCrawler + HTTPClient + Extractor + Dedup + 三级发现 + 44+ 源 | 顶层 `crawlers/` 模块基本齐备；46 个源配置；去重/正文提取/ETag 逻辑存在 | **部分达成**：主架构存在 ✅，但旧 `crawlers/sources/` 子模块存在 API 漂移，且本地依赖缺失导致 import/test 失败；测试极弱 ❌ | 5/10 |
| Task 6 数据库层 | 10 张表、DAO、WAL、导出/迁移 | Schema 10 张表，DAO ~20 方法，WAL 开启，DB 文件可查询 | **部分达成**：数据库结构完整 ✅，但数据迁移不完全（articles 仅 56 vs 分类 739），零测试 ❌ | 7/10 |
| Task 7 论文搜集与翻译 | 论文抓取、PDF 提取、论文页生成、CI | `fetch-papers.py`、`extract-pdf.py`、`generate-docs.py` 存在；87 篇论文 + 87 个 MDX 页面 | **部分达成**：主链路实现 ✅，但 `papers.json` 没有显式提取状态字段，零测试 ❌ | 7/10 |
| Task 8 GPU 价格追踪 | eBay 多站点、历史、图表、CI | `fetch-prices-ebay.py`、`normalize-prices.py`、`PriceTracker`、`PriceChart`、`sync-prices.yml` 存在 | **部分达成**：代码实现 ✅，但 `data/prices/` 当前为空，零测试 ❌ | 6/10 |
| Task 9 CI/CD 工作流 | 部署、校验、定时同步 | 8 个 workflow 全部存在；deploy / validate / sync / translate / verify / papers / sync-prices / test-translate | **基本达成**：工作流覆盖充分 ✅，但没有任何测试执行步骤 ❌ | 8/10 |
| Task 10 测试覆盖综合评估 | 明确覆盖现状与风险 | 已完成统计和分级 | **已达成** | 9/10 |

---

## 关键验证结果

### 1) 前端构建与类型系统

#### `npm run typecheck`
**失败。** 直接报出 TypeScript 错误：

- `website/src/components/ArticleHeader.tsx(10,42): error TS2503: Cannot find namespace 'JSX'.`
- `website/src/components/ArticleHeader.tsx(14,20): error TS2339: Property 'credibility' does not exist on type 'DocFrontMatter'.`
- `website/src/components/FlagBadge.tsx(21,65): error TS2503: Cannot find namespace 'JSX'.`
- `website/src/components/PaperArticleHeader.tsx(10,47): error TS2503: Cannot find namespace 'JSX'.`

**结论：** 前端“能运行 build”不等于“类型安全通过”。计划中的“组件编译无 TypeScript 错误”验收标准当前**不成立**。

#### `npm run build`
**成功。**
- build exit code = 0
- static files generated in `website/build`

**结论：** 站点能构建发布，但类型系统已经出现回归，说明 CI 目前偏重构建成功，未形成严格的 TS 质量闸门。

---

### 2) Python 执行环境

#### `python3 scripts/translate.py --help`
**失败。**
- `ModuleNotFoundError: No module named 'yaml'`

#### `./venv/bin/python3 scripts/translate.py --help`
**成功。**
- 能输出 help，支持 `--mode {doc,paper}`、`--incremental`、`--max-files`

**结论：** 翻译脚本本身可用，但**依赖环境未标准化**；默认系统 Python 不能直接跑。这会影响“本地可验收性”和新贡献者上手成本。

#### `./venv/bin/python3` 下的爬虫测试脚本
仍失败：
- `ModuleNotFoundError: No module named 'httpx'`

**结论：** 仓库内 `venv` 也不是完整可运行基线，至少缺 `httpx`。本地验证环境不稳定。

---

### 3) 测试基线

#### 前端测试
- `website/src/` 下 **0 个** `*.test.*` / `*.spec.*`
- `website/package.json` **没有** `test` script
- `website/package.json` **没有** `vitest` / `jest` / `@testing-library/*`

#### Python 测试
- Python 源文件约 **40** 个
- Python 测试文件仅 **2** 个：
  - `crawlers/test_base.py`
  - `crawlers/test_sources.py`
- 无 `pytest.ini` / `pyproject.toml` / `setup.cfg` 测试配置
- repo 中未建立标准 `tests/` 测试体系

#### 官方/行业基线（来自外部研究）
- Docusaurus + React + TS 项目通常至少有：`vitest` + `@testing-library/react` + `jsdom`
- Python crawler / script / SQLite 项目通常至少有：`pytest` + `pytest-cov` + HTTP mock（如 `respx` / `pytest-httpx`）

**结论：** 该项目目前的测试基础设施基本空白，严格来说不具备“足够测试支持”。

---

## 测试覆盖矩阵

| 模块 | 文件数 | 有测试 | 覆盖率 | 风险等级 |
|------|--------|--------|--------|---------|
| 前端组件（核心审查组件） | 10+ | 0 | 0% | 🔴 Critical |
| `scripts/` 数据管道 | 18+ | 0 | 0% | 🔴 Critical |
| `crawlers/` 顶层模块 | 10 | 2 个旧脚本式测试 | <20% | 🔴 Critical |
| `crawlers/sources/` 旧子模块 | 5 | 0 | 0% | 🔴 Critical |
| `db/` 数据库层 | 4 | 0 | 0% | 🔴 Critical |
| CI workflow 本身 | 8 | YAML + 触发检查可验证 | N/A | 🟡 Medium |

---

## 关键发现

### A. 功能完整但零测试（高风险）

以下模块从实现层面已经存在，但没有任何 automated tests：

- `website/src/components/BilingualViewer/*`
- `website/src/components/ArticleHeader.tsx`
- `website/src/components/ArticleMeta/*`
- `website/src/components/CudaHipMap.tsx`
- `website/src/components/ErrorCodeLookup.tsx`
- `website/src/components/CompatibilityMatrix.tsx`
- `website/src/components/PriceTracker.tsx`
- `website/src/components/PriceChart.tsx`
- `website/src/components/IssueTracker.tsx`
- `website/src/components/GlossaryTooltip.tsx`
- `website/src/components/RelatedArticles.tsx`
- `scripts/translate.py`
- `scripts/fetch-papers.py`
- `scripts/extract-pdf.py`
- `scripts/generate-docs.py`
- `scripts/fetch-prices-ebay.py`
- `scripts/normalize-prices.py`
- `db/__init__.py`
- `db/dao.py`
- `db/migrate.py`
- `db/export.py`

**判断：** 这不是“测试不足”，而是**核心工程面几乎无测试覆盖**。

---

### B. 功能部分缺失 / 验收未过

#### 1. 前端类型系统未过
虽然 build 成功，但 typecheck 明确失败，说明前端核心组件当前并未达到“严格工程可验收”状态。

#### 2. 价格追踪代码存在，但数据为空
- `sync-prices.yml` 存在
- `fetch-prices-ebay.py` / `normalize-prices.py` 存在
- `PriceTracker` / `PriceChart` 存在
- 但 `data/prices/` 当前为空

**判断：** 功能实现已开始，但“数据链路是否真实跑通”还不能算完成。

#### 3. 数据库化已完成一部分，但 DB 与大规模内容数据未完全对齐
- DB 中 `articles` 为 **56**
- `articles_classified.json` 中实际分类文章为 **739**（在 `articles` 列表字段下）

**判断：** 数据库层 schema/DAO 做了，但“全量内容进入 DB”尚未完成。

#### 4. `known_issues.json` 数据质量偏弱
文件结构更像模板化占位数据，尚未体现 README 中“已知 bug / workaround / fix version / 影响硬件”的真实情报价值。

---

### C. 测试基础设施缺失

#### Python
- 无 pytest
- 无测试配置
- 无统一 test runner
- 现有两个 `crawlers/test_*.py` 也只是脚本式验证，不是成熟测试体系

#### Frontend
- 无 Vitest / Jest / Testing Library
- 无 test script
- 无 component render / interaction / snapshot 测试

#### CI
- `validate.yml` 会做链接、图片、frontmatter、build 校验
- 但 **没有任何 workflow 执行 Python tests 或 frontend tests**

---

### D. 爬虫架构存在旧 API 漂移（重要）

背景审查发现 `crawlers/sources/*.py` 仍然依赖 `RawDoc` / `ParsedArticle`，但当前 `crawlers/base.py` 中已经不存在这两个类型：

- `base_has_RawDoc = False`
- `base_has_ParsedArticle = False`
- `rocm_docs_imports_RawDoc = True`
- `rocm_docs_imports_ParsedArticle = True`
- `rocm_blog_imports_RawDoc = True`
- `rocm_blog_imports_ParsedArticle = True`

**结论：** `crawlers/` 已经演进到新基类模型，但 `crawlers/sources/` 还残留旧接口假设。当前本地 import 首先被依赖缺失挡住，但即便补齐依赖，这块仍有较高概率出现 API 兼容问题。

---

## 各 Task 验收结论

| Task | 结论 |
|------|------|
| Task 1 双语阅读组件 | **部分通过**：功能齐，但 typecheck 失败、无测试 |
| Task 2 文章元信息组件 | **部分通过**：功能齐，但 typecheck 受阻、无测试 |
| Task 3 CUDA→HIP / 错误码 / 兼容性 | **部分通过**：数据和组件都在，但无测试，错误码数据质量一般 |
| Task 4 翻译管道 | **部分通过**：代码能力强，但默认 Python 环境不可直接运行，无测试 |
| Task 5 爬虫框架 | **部分通过 / 高风险**：新架构存在，旧架构漂移，依赖未闭合，测试极弱 |
| Task 6 数据库层 | **部分通过**：schema/DAO 完整，但全量数据迁移未闭环，无测试 |
| Task 7 论文搜集与翻译 | **部分通过**：论文数据与页面都在，但提取状态不可见，无测试 |
| Task 8 GPU 价格追踪 | **部分通过**：代码已写，数据为空，无测试 |
| Task 9 CI/CD 工作流 | **通过但不充分**：workflow 完整，但缺测试执行步骤 |
| Task 10 测试覆盖综合评估 | **通过**：已明确识别核心差距 |

---

## 建议优先级

### P0 / 立即处理

1. **修复前端 typecheck**
   - 先把 `JSX` namespace 和 `DocFrontMatter` 类型问题修掉
   - 否则后续组件测试和迭代都在不稳定基线上进行

2. **建立 Python 测试基础设施**
   - 引入 `pytest`
   - 最少先覆盖：`translate.py`、`db/dao.py`、`crawlers/dedup.py`、`crawlers/extractor.py`

3. **建立前端测试基础设施**
   - `vitest` + `@testing-library/react` + `jsdom`
   - 最少先覆盖：`BilingualViewer`、`CudaHipMap`、`PriceTracker`

### P1 / 当前阶段应尽快补齐

4. **补齐 CI 的 test step**
   - 在 `validate.yml` 或单独 `test.yml` 中跑 Python + frontend tests

5. **修复 crawler 旧 API 漂移**
   - 统一 `crawlers/` 与 `crawlers/sources/` 的基类接口
   - 删除死代码或迁移旧子模块

6. **让 repo 提供可复现本地环境**
   - 至少明确 requirements / dev dependencies
   - 解决系统 Python 缺 `yaml`、repo venv 缺 `httpx` 这类基线问题

### P2 / 功能闭环增强

7. **把 739 篇内容与 SQLite DB 真正对齐**
8. **让价格数据链路至少产出一轮真实数据**
9. **把 `known_issues.json` 从模板数据升级为真实 issue intelligence**
10. **为 papers 数据增加显式 extracted / translated 状态字段**

---

## 最终判断

如果问题是：

> **“代码实现是否达成了预期目标，是否有足够的测试支持？”**

那么本次审查结论是：

### 结论

- **预期目标：部分达成。**
  - 功能层面：多数核心模块已经做出来了。
  - 工程层面：仍有显著未过验收项（typecheck、依赖基线、数据闭环、旧 API 漂移）。

- **测试支持：明显不足。**
  - 当前不能说“有足够测试支持”。
  - 更准确的说法是：**项目主要依赖 build / 脚本运行 / CI 流程自证，而非测试体系自证。**

这意味着项目已经具备“可演示的功能形态”，但距离“稳定可回归、可持续扩展的工程质量”还有一段距离。
