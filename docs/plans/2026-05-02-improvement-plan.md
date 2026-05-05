# rocm-hip-map 针对性改善计划

> **目标：** 逐一修复 review report (`docs/plans/2026-05-02-core-features-review-report.md`) 中发现的所有失败项，使项目完全通过 review plan (`docs/plans/2026-05-02-core-features-review.md`) 的全部验收标准。
> 
> **日期：** 2026-05-02
> **优先级策略：** P0 基线修复 → P1 测试基建 → P2 数据闭环 → P3 CI 集成

---

## Phase P0：修复基线（使项目可验证）

### P0-1：修复前端 TypeScript 类型错误

**问题来源：** Review Report §1 — `npm run typecheck` 失败，4 个 TS 错误。
**影响 Task：** Task 1, Task 2

#### Step 1.1：修复 `JSX` namespace 错误（TS2503）

- **文件：** `website/src/components/ArticleHeader.tsx` (line 10), `FlagBadge.tsx` (line 21), `PaperArticleHeader.tsx` (line 10)
- **根因：** 使用了 `JSX.Element` 但未导入 React 19 的类型定义，或 `tsconfig.json` 未正确配置 `jsx` 编译选项。
- **修复方案：**
  1. 检查 `website/tsconfig.json` 的 `compilerOptions.jsx` 是否为 `"react-jsx"`（Docusaurus 3 推荐）。
  2. 若配置正确，则在各组件顶部添加 `import type { JSX } from 'react';` 或直接使用 `React.ReactElement` 替代 `JSX.Element`。
  3. 若使用 `React.FC` 类型，确保 React 已正确导入。

#### Step 1.2：修复 `DocFrontMatter` 缺少 `credibility` 属性（TS2339）

- **文件：** `website/src/components/ArticleHeader.tsx` (line 14)
- **根因：** `ArticleHeader` 访问 `frontMatter.credibility`，但 `DocFrontMatter` 类型定义中未声明该字段。
- **修复方案：**
  1. 找到 `DocFrontMatter` 类型定义位置（通常在 `website/src/types.ts` 或 `website/global.d.ts`）。
  2. 添加可选字段：`credibility?: number;` 或 `credibility?: 1 | 2 | 3 | 4 | 5;`。
  3. 同步检查是否还有其他缺失字段（如 `lifecycle`, `tags` 等），一次性补全。

#### Step 1.3：验证修复

```bash
cd website && npm run typecheck 2>&1 | tail -5
```

**验收标准：**
- [ ] `npm run typecheck` exit 0，零 TS 错误
- [ ] `npm run build` 仍成功

---

### P0-2：标准化 Python 执行环境

**问题来源：** Review Report §2 — 系统 Python 缺 `yaml`，repo venv 缺 `httpx`。
**影响 Task：** Task 4, Task 5

#### Step 2.1：建立完整的依赖声明

- **行动：** 创建或更新 `requirements.txt`（或 `pyproject.toml`），包含所有运行时和开发依赖：
  ```
  # 运行时
  httpx>=0.27
  pyyaml>=6.0
  trafilatura>=1.12
  sqlite-utils>=3.36
  
  # 开发/测试
  pytest>=8.0
  pytest-cov>=5.0
  pytest-httpx>=0.30
  ```

#### Step 2.2：提供环境初始化脚本

- **行动：** 创建 `scripts/setup-env.sh`：
  ```bash
  #!/usr/bin/env bash
  set -euo pipefail
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  echo "✅ Environment ready. Use: source venv/bin/activate"
  ```

#### Step 2.3：重建 venv 并验证

```bash
rm -rf venv && bash scripts/setup-env.sh
./venv/bin/python3 scripts/translate.py --help
./venv/bin/python3 -c "import httpx, yaml; print('✅ deps OK')"
```

**验收标准：**
- [ ] `./venv/bin/python3 scripts/translate.py --help` exit 0
- [ ] `./venv/bin/python3 -c "from crawlers import BaseCrawler; print('OK')"` 成功
- [ ] `requirements.txt` 包含所有 import 的第三方库

---

### P0-3：修复爬虫旧 API 漂移

**问题来源：** Review Report §D — `crawlers/sources/*.py` 依赖已删除的 `RawDoc` / `ParsedArticle`。
**影响 Task：** Task 5

#### Step 3.1：分析当前 `crawlers/base.py` 的新数据模型

- **行动：** 确认 `base.py` 中替代 `RawDoc` / `ParsedArticle` 的新类型名称和字段结构。

#### Step 3.2：更新 `crawlers/sources/` 中的 import

- **文件：** `crawlers/sources/rocm_docs.py`, `crawlers/sources/rocm_blog.py` 等
- **行动：**
  1. 将所有 `from crawlers.base import RawDoc, ParsedArticle` 替换为新的类型 import。
  2. 更新所有使用 `RawDoc` / `ParsedArticle` 构造函数的调用，适配新字段名。
  3. 若旧类型已完全废弃且无替代方案，则评估 `crawlers/sources/` 是否应整体删除（视为死代码）。

#### Step 3.3：验证导入链

```bash
./venv/bin/python3 -c "
from crawlers.sources.rocm_docs import *
from crawlers.sources.rocm_blog import *
print('✅ All source modules import clean')
"
```

**验收标准：**
- [ ] `crawlers/sources/` 中无对 `RawDoc` / `ParsedArticle` 的引用
- [ ] 所有 source 模块可成功导入
- [ ] 无死代码残留（若决定废弃旧子模块，则完全删除）

---

## Phase P1：建立测试基础设施

### P1-1：前端测试基建（Vitest + Testing Library）

**问题来源：** Review Report §3 — 前端零测试。
**影响 Task：** Task 1, Task 2, Task 3, Task 8

#### Step 1.1：安装测试依赖

```bash
cd website
npm install -D vitest @testing-library/react @testing-library/jest-dom jsdom @vitejs/plugin-react
```

#### Step 1.2：配置 Vitest

- **文件：** 创建 `website/vitest.config.ts`
  ```typescript
  import { defineConfig } from 'vitest/config';
  import react from '@vitejs/plugin-react';
  
  export default defineConfig({
    plugins: [react()],
    test: {
      environment: 'jsdom',
      globals: true,
      setupFiles: ['src/test-setup.ts'],
      include: ['src/**/*.test.{ts,tsx}'],
    },
  });
  ```

- **文件：** 创建 `website/src/test-setup.ts`
  ```typescript
  import '@testing-library/jest-dom';
  ```

#### Step 1.3：添加 test script

- **文件：** `website/package.json` → 添加 `"test": "vitest run"` 和 `"test:watch": "vitest"`

#### Step 1.4：编写首批核心组件测试

| 组件 | 测试内容 | 优先级 |
|------|---------|--------|
| `BilingualViewer` | 渲染两种模式（Parallel/Interleaved），模式切换 | 🔴 |
| `ArticleHeader` | 渲染所有元信息字段，credibility 显示 | 🔴 |
| `CudaHipMap` | 渲染映射表，搜索过滤功能 | 🟡 |
| `PriceTracker` | 渲染价格列表，空数据处理 | 🟡 |

#### Step 1.5：验证

```bash
cd website && npm run test 2>&1 | tail -10
```

**验收标准：**
- [ ] `npm run test` exit 0
- [ ] 至少 4 个核心组件有测试覆盖
- [ ] 测试覆盖率报告可生成（`vitest run --coverage`）

---

### P1-2：Python 测试基建（pytest）

**问题来源：** Review Report §3 — Python 无 pytest，测试配置缺失。
**影响 Task：** Task 4, Task 5, Task 6, Task 7, Task 8

#### Step 2.1：安装 pytest 并创建配置

- **文件：** 创建 `pyproject.toml`（或 `pytest.ini`）：
  ```toml
  [tool.pytest.ini_options]
  testpaths = ["tests"]
  python_files = "test_*.py"
  python_classes = "Test*"
  python_functions = "test_*"
  addopts = "-v --tb=short"
  ```

- **目录：** 创建 `tests/__init__.py`

#### Step 2.2：编写首批 Python 测试

| 模块 | 测试内容 | 优先级 |
|------|---------|--------|
| `scripts/translate.py` | 术语表加载、增量翻译逻辑、多后端配置解析 | 🔴 |
| `db/dao.py` | insert + get + update 基本 CRUD（使用内存 SQLite） | 🔴 |
| `crawlers/dedup.py` | URL 去重、SHA256 哈希一致性 | 🔴 |
| `crawlers/extractor.py` | 正文提取函数（mock HTML 输入） | 🟡 |
| `db/export.py` | 导出格式验证 | 🟢 |

#### Step 2.3：验证

```bash
./venv/bin/python3 -m pytest tests/ -v 2>&1 | tail -15
```

**验收标准：**
- [ ] `pytest tests/` exit 0
- [ ] 至少 5 个核心模块有测试覆盖
- [ ] 测试不依赖外部网络（HTTP mock 或 fixture）

---

### P1-3：补充已知缺失的单元测试

**问题来源：** Review Report §A — 18+ scripts、10 crawlers、4 db 文件零测试。
**影响 Task：** Task 4, Task 5, Task 6, Task 7

#### Step 3.1：翻译管道测试

- **文件：** `tests/test_translate.py`
- **测试内容：**
  - `test_glossary_loads()` — 术语表正确加载
  - `test_incremental_skips_translated()` — 增量模式跳过已翻译文件
  - `test_backend_config_parsing()` — 多后端配置解析

#### Step 3.2：数据库 DAO 测试

- **文件：** `tests/test_dao.py`
- **测试内容：**
  - 使用 `:memory:` SQLite 创建临时 DB
  - `test_insert_article()` / `test_get_article_by_url()` / `test_update_article()`

#### Step 3.3：爬虫去重测试

- **文件：** `tests/test_dedup.py`
- **测试内容：**
  - `test_dedup_removes_duplicates()` — 相同 URL 只保留一次
  - `test_url_normalization()` — `http://` vs `https://` 统一处理

#### Step 3.4：爬虫提取器测试

- **文件：** `tests/test_extractor.py`
- **测试内容：**
  - `test_extract_body_from_html()` — 给定 mock HTML，返回正文文本
  - `test_extract_returns_empty_on_invalid()` — 无效 HTML 返回空

**验收标准：**
- [ ] 以上测试全部通过
- [ ] Python 测试覆盖率 ≥ 30%（`pytest --cov=scripts --cov=crawlers --cov=db`）

---

## Phase P2：数据闭环与功能补全

### P2-1：数据库与分类数据对齐

**问题来源：** Review Report §B.3 — DB `articles` 56 行 vs `articles_classified.json` 739 篇。
**影响 Task：** Task 6

#### Step 1.1：编写迁移脚本

- **文件：** 创建 `scripts/migrate-articles-to-db.py`
- **逻辑：**
  1. 读取 `data/articles_classified.json`
  2. 对每篇文章，检查是否已在 DB 中（按 URL 去重）
  3. 插入缺失的文章记录到 `articles` 表
  4. 同步写入 `tags` / `article_tags` 关联

#### Step 1.2：执行迁移并验证

```bash
./venv/bin/python3 scripts/migrate-articles-to-db.py
./venv/bin/python3 -c "
import sqlite3
conn = sqlite3.connect('data/rocm-hip-map.db')
cursor = conn.cursor()
cursor.execute('SELECT COUNT(*) FROM articles')
print(f'articles 表现数: {cursor.fetchone()[0]}')
conn.close()
"
```

**验收标准：**
- [ ] DB `articles` 表行数 ≥ 700
- [ ] 迁移脚本可重复运行（幂等，按 URL 去重）

---

### P2-2：价格数据链路跑通

**问题来源：** Review Report §B.2 — `data/prices/` 为空。
**影响 Task：** Task 8

#### Step 2.1：检查 fetch-prices-ebay.py 的可执行性

```bash
./venv/bin/python3 scripts/fetch-prices-ebay.py --help 2>&1 | head -10
```

#### Step 2.2：执行单次抓取（测试模式）

- **行动：** 以最小参数运行一次抓取，确保产出文件写入 `data/prices/`。
- **注意：** 若 eBay 需要 API key 或反爬限制，考虑：
  1. 添加 mock 模式（从本地 fixture 文件读取样例数据）
  2. 或在 CI 中仅执行 dry-run

#### Step 2.3：验证数据文件

```bash
ls -la data/prices/
./venv/bin/python3 -c "
import json, os, glob
files = glob.glob('data/prices/*.json')
print(f'价格文件数: {len(files)}')
if files:
    with open(files[0]) as f:
        data = json.load(f)
    print(f'首个文件条目数: {len(data) if isinstance(data, list) else \"N/A\"}')
"
```

**验收标准：**
- [ ] `data/prices/` 至少包含 1 个有效价格数据文件
- [ ] `PriceTracker` / `PriceChart` 组件能正确渲染该数据
- [ ] 若无法实时抓取，mock 数据文件已就位且格式正确

---

### P2-3：升级 `known_issues.json` 数据质量

**问题来源：** Review Report §B.4 — 模板化占位数据。
**影响 Task：** Task 3

#### Step 3.1：收集真实 issue 数据

- **行动：** 从 ROCm/HIP GitHub Issues 中搜集真实 bug 数据，包含：
  - issue 标题
  - 错误码（如 `hipErrorNoBinaryForGpu`）
  - workaround / fix version
  - 影响的 GPU 型号

#### Step 3.2：更新 `data/known-issues.json`

- **目标结构：**
  ```json
  [
    {
      "error_code": "hipErrorNoBinaryForGpu",
      "description": "...",
      "workaround": "...",
      "fix_version": "ROCm 6.2",
      "affected_gpus": ["MI210", "MI300X"],
      "source_url": "https://github.com/ROCm/ROCm/issues/..."
    }
  ]
  ```

**验收标准：**
- [ ] `known_issues.json` 包含 ≥10 条真实 issue 情报
- [ ] `ErrorCodeLookup` 组件渲染效果显著改善

---

### P2-4：为 papers.json 增加提取状态字段

**问题来源：** Review Report §P2-10。
**影响 Task：** Task 7

#### Step 4.1：更新数据模型

- **行动：** 为每篇论文添加 `extracted` (bool)、`translated` (bool)、`pdf_url` (string) 字段。

#### Step 4.2：更新 `fetch-papers.py` 写入这些字段

**验收标准：**
- [ ] `papers.json` 中每篇条目包含 `extracted` / `translated` 字段
- [ ] 可通过脚本查询提取/翻译进度

---

## Phase P3：CI 集成测试

### P3-1：在 validate.yml 中增加测试执行步骤

**问题来源：** Review Report §C — 无 workflow 执行 Python 或 frontend tests。
**影响 Task：** Task 9

#### Step 1.1：更新 `.github/workflows/validate.yml`

添加以下 job：

```yaml
  test-frontend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'npm'
          cache-dependency-path: website/package-lock.json
      - run: cd website && npm ci
      - run: cd website && npm run typecheck
      - run: cd website && npm run test

  test-python:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: pytest tests/ -v --tb=short
```

#### Step 1.2：确保 CI 通过

- **行动：** 在本地模拟 CI 环境运行上述命令，确保 exit 0 后再推送到远端。

**验收标准：**
- [ ] `validate.yml` PR 触发时同时运行 `test-frontend` 和 `test-python`
- [ ] 两个测试 job 均 exit 0
- [ ] 前端 typecheck 作为 CI 闸门生效

---

## 执行顺序与依赖关系

```
P0-1 (Frontend TS fix)  ─────┐
P0-2 (Python env)       ─────┼──→ P1-1 (Frontend tests) ──→ P3-1 (CI)
P0-3 (Crawler API fix)  ─────┤
                             ├──→ P1-2 (Python tests) ─────→ P3-1 (CI)
                             ├──→ P1-3 (Supplement tests)
                             │
                             ├──→ P2-1 (DB migration)
                             ├──→ P2-2 (Price data)
                             ├──→ P2-3 (known_issues.json)
                             └──→ P2-4 (papers status fields)
```

- **P0 三项可并行**执行
- **P1 依赖 P0 完成**（基线不修好，测试无法写）
- **P2 可与 P1 并行**（数据补全不依赖测试基建）
- **P3 必须在 P0+P1 完成后**执行

---

## 预期改善后的 Review 通过率

| Task | 当前状态 | 改善后预期 | 关键修复项 |
|------|---------|-----------|-----------|
| Task 1 | 部分通过 | ✅ 通过 | TS2503/2339 修复 + Vitest 测试 |
| Task 2 | 部分通过 | ✅ 通过 | DocFrontMatter 补全 + Vitest 测试 |
| Task 3 | 部分通过 | ✅ 通过 | known_issues.json 升级 + Vitest 测试 |
| Task 4 | 部分通过 | ✅ 通过 | 依赖基线 + pytest 测试 |
| Task 5 | 部分通过/高风险 | ✅ 通过 | API 漂移修复 + pytest 测试 |
| Task 6 | 部分通过 | ✅ 通过 | DB 迁移 + DAO 测试 |
| Task 7 | 部分通过 | ✅ 通过 | papers 状态字段 + pytest 测试 |
| Task 8 | 部分通过 | ✅ 通过 | 价格数据产出 + pytest 测试 |
| Task 9 | 通过但不充分 | ✅ 通过 | CI 增加 test-frontend + test-python |
| Task 10 | 通过 | ✅ 通过 | 覆盖矩阵更新 |

**最终目标：** 10/10 Task 全部通过。
