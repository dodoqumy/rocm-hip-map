# rocm-hip-map 核心功能 Review 计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 系统性验证 rocm-hip-map 项目代码实现是否达成 README 预期目标，评估测试覆盖充分性，识别功能-测试差距。

**Architecture:** 基于 gap-analysis.md 的差距评估，按核心功能模块分组审查。每个模块执行三阶段：实现验证 → 测试评估 → 功能-测试差距报告。

**Tech Stack:** Docusaurus 3.10 + React 19 + TypeScript + Python 3.11 + SQLite + httpx + Docusaurus MDX

**审查范围：** 依据 PROGRESS.md 标记为 ✅ 的功能项，对照 README.md 预期要求。

---

## 审查方法论

### 三阶段审查流程

```
Phase A: 实现验证
  ├─ 文件是否存在？代码是否可执行？
  ├─ 功能输出是否符合预期？
  └─ 与 README 要求是否匹配？

Phase B: 测试评估
  ├─ 是否存在测试？（单元/集成/E2E）
  ├─ 测试覆盖核心路径吗？（happy path + edge cases）
  └─ 测试能否独立运行通过？

Phase C: 差距报告
  ├─ 功能 ✅ 但测试 ❌ = 高风险
  ├─ 功能 ✅ 但测试不足 = 中风险
  └─ 功能 ❌ = 按 gap-analysis.md 处理
```

### 审查矩阵

| 功能模块 | 验证方法 | 通过标准 |
|---------|---------|---------|
| React 组件 | 编译检查 + 视觉验证 | tsc 无错 + 页面渲染正确 |
| Python 脚本 | 实际运行 + 输出验证 | 脚本 exit 0 + 产出文件正确 |
| CI Workflows | YAML 语法 + 执行历史 | validate.yml 通过 + GitHub Actions 绿色 |
| 数据库 | Schema 验证 + DAO 测试 | 10 张表可查询 + DAO CRUD 正常 |
| 爬虫模块 | 实际抓取 + 去重验证 | 能抓取有效内容 + 去重生效 |
| 分类系统 | 分类结果抽样 | 739 篇文章分类合理 |
| 翻译管道 | 增量翻译验证 | 术语表生效 + 输出格式正确 |

---

## 审查任务清单

### Task 1: 双语阅读组件（BilingualViewer）

**对应 README 要求：** "提供中英双语阅读"、"中英对照模式（左右分栏）"
**PROGRESS.md：** Phase 4.1-4.4 ✅
**Files:**
- `website/src/components/BilingualViewer/index.tsx`
- `website/src/components/BilingualViewer/ParallelView.tsx`
- `website/src/components/BilingualViewer/InterleavedView.tsx`
- `website/src/components/BilingualViewer/styles.module.css`

- [ ] **Step 1: 验证组件编译**

```bash
cd website && npx tsc --noEmit 2>&1 | grep -i "BilingualViewer" || echo "✅ BilingualViewer 编译无错误"
```
Expected: 无 BilingualViewer 相关 TypeScript 错误

- [ ] **Step 2: 验证 ParallelView 实现左右分栏**

```bash
grep -n "flex\|grid\|display" website/src/components/BilingualViewer/ParallelView.tsx
```
Expected: 存在 flex/grid 布局，左右两个内容区域

- [ ] **Step 3: 验证 InterleavedView 实现逐段对照**

```bash
grep -n "interleave\|paragraph\|segment\|交替\|逐段" website/src/components/BilingualViewer/InterleavedView.tsx
```
Expected: 段落级交替渲染逻辑

- [ ] **Step 4: 验证模式切换功能**

```bash
grep -n "mode\|switch\|toggle" website/src/components/BilingualViewer/index.tsx
```
Expected: 存在 mode state + 切换按钮

- [ ] **Step 5: 验证移动端自适应（Phase 4.4）**

```bash
grep -n "media\|mobile\|responsive\|breakpoint\|@media" website/src/components/BilingualViewer/styles.module.css
```
Expected: 存在 @media 查询，小屏幕切换为上下布局

- [ ] **Step 6: 测试评估**

```bash
find website/src/components/BilingualViewer -name "*.test.*" -o -name "*.spec.*"
```
Expected: ❌ 无测试文件（已知差距）

- [ ] **Step 7: 构建验证**

```bash
cd website && npm run build 2>&1 | tail -5
```
Expected: Build successful

**验收标准：**
- [ ] 组件编译无 TypeScript 错误
- [ ] ParallelView 实现左右分栏布局
- [ ] InterleavedView 实现逐段对照
- [ ] 支持模式切换
- [ ] 移动端响应式布局
- [ ] ⚠️ 无单元测试 → 记录为"功能完整、测试缺失"

---

### Task 2: 文章元信息组件（ArticleMeta 系列）

**对应 README 要求：** "标题、来源网站、原文链接、发布时间、更新时间、原文语言、标签系统"
**PROGRESS.md：** ArticleHeader, ArticleMeta, CredibilityStars, LifecycleBadge, TagBadge 全部 ✅
**Files:**
- `website/src/components/ArticleHeader.tsx`
- `website/src/components/ArticleMeta/index.tsx`
- `website/src/components/ArticleMeta/CredibilityStars.tsx`
- `website/src/components/ArticleMeta/LifecycleBadge.tsx`
- `website/src/components/ArticleMeta/TagBadge.tsx`

- [ ] **Step 1: 验证 ArticleHeader 包含所有元信息字段**

```bash
grep -c "source\|url\|date\|publish\|update\|language\|lang" website/src/components/ArticleHeader.tsx
```
Expected: ≥5 个元信息相关字段引用

- [ ] **Step 2: 验证 CredibilityStars 实现可信度评级**

```bash
grep -n "star\|rating\|credibility\|★★★★\|level\|tier" website/src/components/ArticleMeta/CredibilityStars.tsx
```
Expected: 星级渲染逻辑 + 多级别支持

- [ ] **Step 3: 验证 LifecycleBadge 实现生命周期状态**

```bash
grep -n "lifecycle\|deprecated\|outdated\|latest\|status\|badge" website/src/components/ArticleMeta/LifecycleBadge.tsx
```
Expected: 至少 4 种状态（最新推荐、已过时、即将废弃、已弃用）

- [ ] **Step 4: 验证 TagBadge 标签系统**

```bash
grep -n "tag\|label\|category" website/src/components/ArticleMeta/TagBadge.tsx
```
Expected: 标签渲染逻辑

- [ ] **Step 5: 验证组件在实际页面中的使用**

```bash
grep -rl "ArticleHeader\|ArticleMeta\|CredibilityStars\|LifecycleBadge" website/docs/ --include="*.mdx" | head -5
```
Expected: ≥3 篇 MDX 文件引用了这些组件

- [ ] **Step 6: 测试评估**

```bash
find website/src/components/ArticleMeta website/src/components/ArticleHeader.tsx -name "*.test.*" 2>/dev/null
find website/src -path "*ArticleMeta*" -name "*.test.*" 2>/dev/null
echo "---"
ls website/src/components/ArticleMeta/*.test.* 2>/dev/null || echo "❌ 无测试"
```
Expected: ❌ 无测试文件

**验收标准：**
- [ ] ArticleHeader 展示全部要求的元信息
- [ ] CredibilityStars 至少支持 4 级可信度
- [ ] LifecycleBadge 至少支持 4 种状态
- [ ] TagBadge 渲染标签
- [ ] 组件在实际文章中使用
- [ ] ⚠️ 无测试 → 记录为"功能完整、测试缺失"

---

### Task 3: CUDA→HIP 映射 + 错误码库 + 兼容性矩阵

**对应 README 要求：** "CUDA → HIP 对照数据库"、"常见错误码库"、"兼容性矩阵"
**PROGRESS.md：** 7.3 ✅（301 条映射），组件清单全部 ✅
**Files:**
- `website/src/components/CudaHipMap.tsx`
- `website/src/components/ErrorCodeLookup.tsx`
- `website/src/components/CompatibilityMatrix.tsx`
- `data/cuda-hip-api-map.json`
- `data/known-issues.json`

- [ ] **Step 1: 验证 CUDA→HIP 数据量**

```bash
python3 -c "
import json
with open('data/cuda-hip-api-map.json') as f:
    data = json.load(f)
count = len(data) if isinstance(data, list) else len(data.get('mappings', data.get('entries', [])))
print(f'CUDA→HIP 映射条目数: {count}')
assert count >= 300, f'预期 ≥300 条，实际 {count}'
print('✅ 数据量达标')
"
```
Expected: ≥300 条映射

- [ ] **Step 2: 验证 CudaHipMap 组件搜索/过滤功能**

```bash
grep -n "search\|filter\|input\|query" website/src/components/CudaHipMap.tsx
```
Expected: 搜索或过滤功能实现

- [ ] **Step 3: 验证 ErrorCodeLookup 组件数据结构**

```bash
python3 -c "
import json
with open('data/known-issues.json') as f:
    data = json.load(f)
print(f'已知问题数: {len(data) if isinstance(data, list) else len(data.keys())}')
print(json.dumps(data, indent=2, ensure_ascii=False)[:500])
"
```
Expected: 至少包含示例错误码（如 hipErrorNoBinaryForGpu）

- [ ] **Step 4: 验证 CompatibilityMatrix 数据结构**

```bash
grep -n "matrix\|row\|column\|GPU\|ROCm\|Ubuntu" website/src/components/CompatibilityMatrix.tsx | head -10
```
Expected: 矩阵表格渲染逻辑

- [ ] **Step 5: 测试评估**

```bash
ls website/src/components/CudaHipMap.test.* website/src/components/ErrorCodeLookup.test.* website/src/components/CompatibilityMatrix.test.* 2>/dev/null || echo "❌ 三个组件均无测试"
```
Expected: ❌ 无测试

**验收标准：**
- [ ] CUDA→HIP 映射 ≥300 条
- [ ] CudaHipMap 支持搜索/过滤
- [ ] ErrorCodeLookup 有错误码数据
- [ ] CompatibilityMatrix 有矩阵渲染
- [ ] ⚠️ 三个组件均无测试 → 高风险（数据密集型组件）

---

### Task 4: 翻译管道（translate.py）

**对应 README 要求：** "提供中英双语阅读"、"翻译内容与原文分离"、术语表约束
**PROGRESS.md：** Phase 4.5-4.9 ✅，4.10 🟡
**Files:**
- `scripts/translate.py`
- `glossary/rocm-terms.yaml`
- `.github/workflows/translate.yml`

- [ ] **Step 1: 验证多翻译后端支持**

```bash
grep -n "backend\|provider\|openai\|anthropic\|deepseek\|gemini\|api_key\|Base URL" scripts/translate.py | head -15
```
Expected: 至少 4 个后端配置

- [ ] **Step 2: 验证增量模式**

```bash
grep -n "incremental\|resume\|checkpoint\|batch\|limit\|offset\|state\|progress" scripts/translate.py | head -10
```
Expected: 增量翻译逻辑（断点续传）

- [ ] **Step 3: 验证术语表集成**

```bash
python3 -c "
import yaml
with open('glossary/rocm-terms.yaml') as f:
    terms = yaml.safe_load(f)
count = len(terms) if isinstance(terms, list) else len(terms.get('terms', terms.get('entries', [])))
print(f'术语表条目数: {count}')
assert count > 20, f'术语表过少: {count}'
print('✅ 术语表规模合理')
"
```
Expected: ≥20 条术语

- [ ] **Step 4: 验证术语表在翻译中的使用**

```bash
grep -n "glossary\|rocm-terms\|terminology\|yaml" scripts/translate.py | head -5
```
Expected: 术语表加载和应用逻辑

- [ ] **Step 5: 验证 translate.yml workflow**

```bash
grep -n "schedule\|cron\|incremental\|batch\|limit" .github/workflows/translate.yml
```
Expected: 定时触发 + 增量参数

- [ ] **Step 6: 脚本可执行性验证**

```bash
python3 scripts/translate.py --help 2>&1 | head -10
```
Expected: 帮助信息输出，exit 0

- [ ] **Step 7: 测试评估**

```bash
ls scripts/test_translate* tests/test_translate* 2>/dev/null || echo "❌ 翻译脚本无测试"
grep -n "test\|assert\|unittest\|pytest" scripts/translate.py | head -3
```
Expected: ❌ 无测试

**验收标准：**
- [ ] 支持 ≥4 个翻译后端
- [ ] 增量模式（断点续传）可用
- [ ] 术语表加载并应用于翻译
- [ ] 定时 workflow 配置正确
- [ ] 脚本可执行（--help 正常）
- [ ] ⚠️ 无测试 → 高风险（核心数据管道）

---

### Task 5: 爬虫框架 v2（crawlers/）

**对应 README 要求：** "只收录一手情报"、"官方来源优先"
**PROGRESS.md：** Phase 2.1 全部 ✅，2.1.9 🟡
**Files:**
- `crawlers/__init__.py`
- `crawlers/base.py`
- `crawlers/http_client.py`
- `crawlers/extractor.py`
- `crawlers/dedup.py`
- `crawlers/sitemap.py`
- `crawlers/sphinx_nav.py`
- `crawlers/github_docs.py`
- `crawlers/rss.py`
- `crawlers/url_family.py`
- `config/amd-sources.yaml`

- [ ] **Step 1: 验证模块可导入**

```bash
cd /home/lijy/projects/hermes/rocm-hip-map && python3 -c "
from crawlers import BaseCrawler, SitemapCrawler, SphinxNavCrawler, GithubDocsCrawler, RSSCrawler
from crawlers.http_client import HTTPClient
from crawlers.extractor import Extractor
from crawlers.dedup import Dedup
from crawlers.url_family import normalize_url_family
print('✅ 所有爬虫模块可导入')
"
```
Expected: 所有 import 成功

- [ ] **Step 2: 验证三级发现架构**

```bash
grep -n "level\|Level\|LEVEL\|discovery\|sitemap\|sphinx\|github\|rss" crawlers/__init__.py
```
Expected: 三级发现定义（Level 1: Sitemap, Level 2: Sphinx Nav, Level 3: GitHub/RSS）

- [ ] **Step 3: 验证去重机制**

```bash
grep -n "sha256\|hash\|dedup\|duplicate\|seen\|url_norm" crawlers/dedup.py
```
Expected: SHA256 去重 + URL 规范化

- [ ] **Step 4: 验证正文提取**

```bash
grep -n "trafilatura\|pandoc\|markdown\|extract\|clean" crawlers/extractor.py | head -10
```
Expected: trafilatura + pandoc 支持

- [ ] **Step 5: 验证 ETag 缓存**

```bash
grep -n "etag\|ETag\|cache\|If-None-Match\|304" crawlers/http_client.py
```
Expected: ETag 缓存逻辑

- [ ] **Step 6: 验证源配置**

```bash
python3 -c "
import yaml
with open('config/amd-sources.yaml') as f:
    config = yaml.safe_load(f)
sources = config.get('sources', [])
print(f'配置的源数量: {len(sources)}')
assert len(sources) >= 40, f'源过少: {len(sources)}'
print('✅ 源配置规模合理')
"
```
Expected: ≥40 个源

- [ ] **Step 7: 验证抓取产出**

```bash
python3 -c "
import json
with open('data/articles_classified.json') as f:
    data = json.load(f)
print(f'已分类文章数: {len(data)}')
assert len(data) >= 500, f'文章过少: {len(data)}'
print('✅ 抓取产出达标')
"
```
Expected: ≥500 篇

- [ ] **Step 8: 测试评估**

```bash
echo "=== 已有测试 ==="
wc -l crawlers/test_base.py crawlers/test_sources.py
echo "=== 测试内容分析 ==="
grep -c "assert\|test_\|def test" crawlers/test_base.py crawlers/test_sources.py
echo "=== 缺失测试的模块 ==="
for f in crawlers/http_client.py crawlers/extractor.py crawlers/dedup.py crawlers/sitemap.py crawlers/sphinx_nav.py crawlers/github_docs.py crawlers/rss.py crawlers/url_family.py; do
    module=$(basename "$f" .py)
    if ! grep -q "test_$module" crawlers/test_*.py 2>/dev/null; then
        echo "❌ 无测试: $module"
    fi
done
```
Expected: 仅 base 和 sources 有简单测试，其余 8 个模块无测试

**验收标准：**
- [ ] 所有模块可导入
- [ ] 三级发现架构实现
- [ ] 去重机制（SHA256 + URL 规范化）
- [ ] 正文提取（trafilatura）
- [ ] ETag 缓存
- [ ] 源配置 ≥40 个
- [ ] 抓取产出 ≥500 篇
- [ ] ⚠️ 仅 2 个简单测试覆盖 10 个模块 → 极高风险

---

### Task 6: 数据库层（db/）

**对应 README 要求：** （Phase 2.0 新增，非 README 原始要求）
**PROGRESS.md：** Phase 2.0.0 ✅
**Files:**
- `db/schema.sql`
- `db/__init__.py`
- `db/dao.py`
- `db/migrate.py`
- `db/export.py`
- `data/rocm-hip-map.db`

- [ ] **Step 1: 验证 Schema 表数量**

```bash
grep -c "CREATE TABLE" db/schema.sql
```
Expected: 10 张表

- [ ] **Step 2: 列出所有表名**

```bash
grep "CREATE TABLE" db/schema.sql
```
Expected: sources, articles, tags, article_tags, cuda_hip_map, papers, crawl_log 等

- [ ] **Step 3: 验证数据库文件存在且可查询**

```bash
python3 -c "
import sqlite3
conn = sqlite3.connect('data/rocm-hip-map.db')
cursor = conn.cursor()
cursor.execute(\"SELECT name FROM sqlite_master WHERE type='table'\")
tables = [row[0] for row in cursor.fetchall()]
print(f'数据库表: {tables}')
print(f'表数量: {len(tables)}')
conn.close()
assert len(tables) >= 8, f'表过少: {len(tables)}'
print('✅ 数据库可访问')
"
```
Expected: ≥8 张表

- [ ] **Step 4: 验证各表数据量**

```bash
python3 -c "
import sqlite3
conn = sqlite3.connect('data/rocm-hip-map.db')
cursor = conn.cursor()
cursor.execute(\"SELECT name FROM sqlite_master WHERE type='table'\")
tables = [row[0] for row in cursor.fetchall()]
for table in tables:
    cursor.execute(f'SELECT COUNT(*) FROM {table}')
    count = cursor.fetchone()[0]
    print(f'  {table}: {count} 行')
conn.close()
"
```
Expected: 各表有数据（非空）

- [ ] **Step 5: 验证 DAO 层 CRUD**

```bash
grep -n "def get\|def insert\|def update\|def delete\|def find\|def create" db/dao.py | head -20
```
Expected: ≥10 个 CRUD 方法

- [ ] **Step 6: 验证连接池 + WAL 模式**

```bash
grep -n "wal\|WAL\|pool\|connect\|sqlite3" db/__init__.py
```
Expected: WAL 模式设置 + 连接管理

- [ ] **Step 7: 测试评估**

```bash
find db/ -name "test_*" -o -name "*_test.py" 2>/dev/null
ls tests/test_db* 2>/dev/null || echo "❌ 数据库层无测试"
```
Expected: ❌ 无测试

**验收标准：**
- [ ] Schema 定义 10 张表
- [ ] 数据库文件存在且 ≥8 张表
- [ ] 各表有数据
- [ ] DAO 层 ≥10 个方法
- [ ] WAL 模式启用
- [ ] ⚠️ 数据库层零测试 → 高风险（数据完整性依赖）

---

### Task 7: 论文搜集与翻译（Phase 8）

**对应 README 要求：** "学术论文原文"
**PROGRESS.md：** Phase 8.1-8.7 全部 ✅
**Files:**
- `scripts/fetch-papers.py`
- `scripts/extract-pdf.py`
- `scripts/translate.py` (--mode paper)
- `scripts/generate-docs.py`
- `data/papers.json`

- [ ] **Step 1: 验证论文数据量**

```bash
python3 -c "
import json
with open('data/papers.json') as f:
    papers = json.load(f)
count = len(papers) if isinstance(papers, list) else len(papers.get('papers', []))
print(f'论文数量: {count}')
assert count >= 80, f'论文过少: {count}'
print('✅ 论文规模达标')
"
```
Expected: ≥80 篇

- [ ] **Step 2: 验证 PDF 提取成功率**

```bash
python3 -c "
import json
with open('data/papers.json') as f:
    papers = json.load(f)
if isinstance(papers, list):
    extracted = sum(1 for p in papers if p.get('extracted') or p.get('content'))
    print(f'已提取: {extracted}/{len(papers)}')
else:
    print('数据格式待分析')
" 2>/dev/null || echo "⚠️ papers.json 格式待确认"
```
Expected: ≥80% 提取率

- [ ] **Step 3: 验证论文页面实际存在**

```bash
ls website/docs/papers/*.mdx 2>/dev/null | wc -l
```
Expected: ≥80 篇 MDX 文件

- [ ] **Step 4: 验证 papers.yml CI workflow**

```bash
grep -n "schedule\|cron\|weekly\|saturday" .github/workflows/papers.yml
```
Expected: 每周六定时触发

- [ ] **Step 5: 测试评估**

```bash
ls tests/test_paper* scripts/test_paper* 2>/dev/null || echo "❌ 论文相关无测试"
```
Expected: ❌ 无测试

**验收标准：**
- [ ] 论文 ≥80 篇
- [ ] PDF 提取率 ≥80%
- [ ] 论文页面在 website/docs/papers/ 存在
- [ ] CI 定时同步
- [ ] ⚠️ 无测试

---

### Task 8: GPU 价格追踪（Phase 10）

**对应 README 要求：** （建议新增功能）
**PROGRESS.md：** Phase 10.1-10.7 大部分 ✅
**Files:**
- `scripts/fetch-prices-ebay.py`
- `scripts/normalize-prices.py`
- `website/src/components/PriceTracker.tsx`
- `website/src/components/PriceChart.tsx`
- `.github/workflows/sync-prices.yml`

- [ ] **Step 1: 验证价格数据存在**

```bash
ls data/prices/ && ls data/prices/ | wc -l
```
Expected: 至少存在价格数据文件

- [ ] **Step 2: 验证 eBay 多站点支持**

```bash
grep -n "ebay\|siteid\|domain\|ebay.de\|ebay.co.uk\|ebay.com" scripts/fetch-prices-ebay.py | head -5
```
Expected: US/DE/UK 三站点

- [ ] **Step 3: 验证 sync-prices.yml 并行配置**

```bash
grep -n "matrix\|country\|US\|DE\|UK\|parallel" .github/workflows/sync-prices.yml
```
Expected: matrix 策略按国家并行

- [ ] **Step 4: 验证 PriceChart 组件可视化**

```bash
grep -n "chart\|graph\|canvas\|svg\|recharts\|chart.js\|d3" website/src/components/PriceChart.tsx | head -5
```
Expected: 图表库集成

- [ ] **Step 5: 验证 52 周历史存储**

```bash
grep -n "week\|52\|history\|week.*store\|retention" scripts/normalize-prices.py
```
Expected: 52 周历史存储逻辑

- [ ] **Step 6: 测试评估**

```bash
ls tests/test_price* scripts/test_price* 2>/dev/null || echo "❌ 价格追踪无测试"
```
Expected: ❌ 无测试

**验收标准：**
- [ ] eBay 三站点价格数据
- [ ] CI 按国家并行
- [ ] 价格图表组件可用
- [ ] 52 周历史
- [ ] ⚠️ 无测试

---

### Task 9: CI/CD 工作流验证

**对应 README 要求：** "部署简单"
**PROGRESS.md：** Phase 6 全部 ✅
**Files:**
- `.github/workflows/deploy.yml`
- `.github/workflows/sync.yml`
- `.github/workflows/translate.yml`
- `.github/workflows/verify.yml`
- `.github/workflows/validate.yml`
- `.github/workflows/sync-prices.yml`
- `.github/workflows/papers.yml`
- `.github/workflows/test-translate.yml`

- [ ] **Step 1: 验证所有 workflow 文件存在**

```bash
for wf in deploy sync translate verify validate sync-prices papers test-translate; do
    if [ -f ".github/workflows/${wf}.yml" ]; then
        echo "✅ ${wf}.yml"
    else
        echo "❌ ${wf}.yml 缺失"
    fi
done
```
Expected: 8 个全部 ✅

- [ ] **Step 2: 验证 YAML 语法**

```bash
python3 -c "
import yaml, sys
workflows = ['deploy', 'sync', 'translate', 'verify', 'validate', 'sync-prices', 'papers', 'test-translate']
all_ok = True
for wf in workflows:
    try:
        with open(f'.github/workflows/{wf}.yml') as f:
            yaml.safe_load(f)
        print(f'✅ {wf}.yml 语法正确')
    except Exception as e:
        print(f'❌ {wf}.yml 语法错误: {e}')
        all_ok = False
if not all_ok:
    sys.exit(1)
"
```
Expected: 全部语法正确

- [ ] **Step 3: 验证定时触发配置**

```bash
grep -H "cron:" .github/workflows/*.yml
```
Expected: 多个 workflow 有 cron 配置

- [ ] **Step 4: 验证 deploy.yml 触发条件**

```bash
grep -n "push\|branches\|main\|trigger" .github/workflows/deploy.yml | head -5
```
Expected: push to main 触发

- [ ] **Step 5: 验证 validate.yml PR 触发**

```bash
grep -n "pull_request\|pull_request_target" .github/workflows/validate.yml
```
Expected: PR 触发

**验收标准：**
- [ ] 8 个 workflow 文件全部存在
- [ ] YAML 语法全部正确
- [ ] 定时触发配置正确
- [ ] deploy 响应 push to main
- [ ] validate 响应 PR

---

### Task 10: 测试覆盖度综合评估（核心差距）

**目的：** 量化全项目测试覆盖现状，形成可操作的差距清单。

- [ ] **Step 1: 统计所有 Python 文件**

```bash
echo "=== Python 源文件 ==="
find . -name "*.py" -not -path "*/venv/*" -not -path "*/__pycache__/*" -not -name "test_*" -not -name "*_test.py" | wc -l
echo "=== Python 测试文件 ==="
find . -name "test_*.py" -o -name "*_test.py" | grep -v venv | wc -l
echo "=== 测试文件行数 ==="
find . -name "test_*.py" | grep -v venv -exec wc -l {} + 2>/dev/null
```

- [ ] **Step 2: 统计所有 TypeScript/React 测试**

```bash
echo "=== TSX/TS 源文件 ==="
find website/src -name "*.tsx" -o -name "*.ts" | grep -v node_modules | grep -v '.docusaurus' | wc -l
echo "=== TSX/TS 测试文件 ==="
find website/src -name "*.test.*" -o -name "*.spec.*" | wc -l
```

- [ ] **Step 3: 检查测试框架配置**

```bash
echo "=== Python 测试框架 ==="
pip list 2>/dev/null | grep -i "pytest\|unittest" || echo "❌ 无 pytest"
echo "=== JS 测试框架 ==="
grep -E '"jest"|"vitest"|"@testing-library"' website/package.json || echo "❌ 无前端测试框架"
```

- [ ] **Step 4: 生成测试覆盖矩阵**

```bash
python3 -c "
import os, json

# 需要测试的核心模块
modules = {
    'scripts': ['translate.py', 'fetch-official.py', 'classify_v2.py', 'generate-docs.py', 'verify.py', 'release-watch.py', 'sync-github.py', 'extract-pdf.py', 'normalize-prices.py', 'fetch-prices-ebay.py', 'fetch-asia.py', 'fetch-eu.py', 'fetch-papers.py', 'cache-images.py', 'classify.py', 'audit_translations.py', 'related-articles.py', 'gen-papers-sidebar.py', 'generate-sidebar.py'],
    'crawlers': ['base.py', 'http_client.py', 'extractor.py', 'dedup.py', 'sitemap.py', 'sphinx_nav.py', 'github_docs.py', 'rss.py', 'url_family.py'],
    'db': ['__init__.py', 'dao.py', 'migrate.py', 'export.py'],
    'components': ['BilingualViewer', 'ArticleMeta', 'CudaHipMap', 'ErrorCodeLookup', 'CompatibilityMatrix', 'PriceTracker', 'PriceChart', 'IssueTracker', 'GlossaryTooltip', 'RelatedArticles']
}

print('=== 测试覆盖矩阵 ===')
print(f'{\"模块\":<20} {\"总数\":>5} {\"有测试\":>6} {\"覆盖率\":>6}')
print('-' * 40)

for category, files in modules.items():
    total = len(files)
    tested = 0
    for f in files:
        if category == 'components':
            test_exists = os.path.exists(f'website/src/components/{f}.test.tsx') or os.path.exists(f'website/src/components/{f}.test.ts')
        elif category == 'crawlers':
            test_exists = os.path.exists(f'crawlers/test_{f}')
        else:
            test_exists = os.path.exists(f'tests/test_{f.replace(\".py\", \"\")}.py') or os.path.exists(f'scripts/test_{f}')

        if test_exists:
            tested += 1

    coverage = (tested / total * 100) if total > 0 else 0
    bar = '█' * int(coverage / 10) + '░' * (10 - int(coverage / 10))
    print(f'{category:<20} {total:>5} {tested:>5}  {coverage:>5.0f}% {bar}')

print()
print('⚠️ 覆盖率 < 20% = 极高风险')
print('⚠️ 覆盖率 20-50% = 高风险')
print('⚠️ 覆盖率 50-80% = 中风险')
print('✅ 覆盖率 > 80% = 可接受')
"
```

**验收标准：**
- [ ] 完成全量测试覆盖统计
- [ ] 生成覆盖矩阵
- [ ] 识别零测试模块
- [ ] 按风险等级分类

---

## 审查报告模板

完成上述 10 个 Task 后，生成以下报告：

```markdown
# rocm-hip-map Review 报告

## 执行摘要
- 审查日期：
- 审查范围：X 个功能模块，Y 个文件
- 总体结论：

## 功能达成情况

| 模块 | README 预期 | 实际实现 | 达成状态 | 评分 |
|------|-----------|---------|---------|------|

## 测试覆盖矩阵

| 模块 | 文件数 | 有测试 | 覆盖率 | 风险等级 |
|------|--------|--------|--------|---------|

## 关键发现

### 功能完整但零测试（高风险）
- 列表

### 功能部分缺失
- 列表（参照 gap-analysis.md）

### 测试基础设施缺失
- Python: 无 pytest
- Frontend: 无 jest/vitest/testing-library

## 建议优先级

1. 🔴 建立测试基础设施（pytest + jest）
2. 🔴 为核心数据管道补充测试（translate.py, crawlers/）
3. 🟡 为数据库层补充测试（db/dao.py）
4. 🟡 为前端组件补充快照测试
5. 🟢 补齐 gap-analysis.md 中标注的功能差距
```

---

## 执行说明

1. **Task 1-9** 可并行执行（每个 Task 独立验证一个模块）
2. **Task 10** 依赖 Task 1-9 的结果，最后执行
3. 每个 Task 完成后立即记录 ✅/❌
4. 所有 Task 完成后生成审查报告

**推荐执行方式：** 使用 subagent-driven-development，每个 Task 分配独立 subagent 并行执行，收集结果后汇总。
