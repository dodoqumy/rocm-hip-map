# ROCm 中外文对照阅读网站 — 实现计划

> **面向 AI 代理的工作者：** 使用 subagent-driven-development 逐任务实现此计划。步骤使用复选框（`- [ ]`）语法来跟踪进度。

**目标：** 构建一个基于 Docusaurus 的静态文档网站，以中英文对照方式展示 ROCm 官方技术文档，支持按版本、环境、组件等多维度分类和筛选。

**架构：** Docusaurus 3.x + React 自定义双语对照组件 + AI 翻译管道 + GitHub Actions 自动同步 → 部署到 GitHub Pages。

**技术栈：** Docusaurus 3 (React/MDX)、TypeScript、Node.js 20+、Python 3 (内容同步脚本)、GitHub Actions、GitHub Pages

**调研结论（2026-04-27）：**
- ✅ Docusaurus：原生 i18n + 版本管理 + React 组件扩展，Meta 活跃维护，63k+ stars
- 🔴 MkDocs Material：2025.11 进入维护模式，停止新功能开发（后继 Zensical 尚未成熟）
- ❌ Hugo：无原生 i18n/版本管理，不适合双语对照场景

---

## 文件结构

```
~/projects/rocm-bilingual-docs/
├── docusaurus.config.ts          # Docusaurus 配置（i18n、版本、导航）
├── sidebars.ts                   # 侧边栏定义（按分类组织）
├── package.json                  # Node 依赖
├── tsconfig.json                 # TypeScript 配置
├── docs/                         # 英文原文（默认语言）
│   ├── 7.2.2/
│   │   ├── getting-started/
│   │   │   └── what-is-rocm.md
│   │   ├── install/
│   │   │   └── linux-install.md
│   │   └── ...
│   ├── 7.1.0/                    # 版本化文档（Docusaurus versioning）
│   └── ...
├── i18n/zh-Hans/                 # 中文翻译（Docusaurus i18n 输出目录）
│   └── docusaurus-plugin-content-docs/
│       └── current/
│           └── ...               # 镜像 docs/ 结构，内容为中文
├── src/
│   ├── components/
│   │   ├── BilingualViewer/      # 双语对照视图组件
│   │   │   ├── index.tsx
│   │   │   ├── ParallelView.tsx  # 左右分栏
│   │   │   ├── InterleavedView.tsx # 逐段对照
│   │   │   └── styles.module.css
│   │   ├── ArticleMeta/          # 文章元信息组件
│   │   │   ├── index.tsx
│   │   │   └── TagBadge.tsx
│   │   ├── VersionSelector/      # 版本选择器
│   │   │   └── index.tsx
│   │   └── GlossaryTooltip/      # 术语悬浮提示
│   │       ├── index.tsx
│   │       └── glossary.ts       # 术语表
│   ├── theme/                    # 主题定制（swizzled）
│   └── css/
│       └── custom.css
├── scripts/
│   ├── sync-rocm-docs.py         # 从 ROCm GitHub 同步文档
│   ├── translate.py              # AI 翻译管道（调用翻译 API）
│   ├── convert-rst-to-md.py      # RST → Markdown 转换
│   └── validate-links.py         # 链接完整性检查
├── glossary/                     # 中英术语对照表
│   └── rocm-terms.yaml
├── .github/
│   └── workflows/
│       ├── deploy.yml            # 构建 + 部署到 GitHub Pages
│       └── sync-and-translate.yml # 定时同步上游文档
├── static/
│   └── img/
└── blog/                         # Phase 2：AMD ROCm 博客
```

每文件职责：
- `docusaurus.config.ts` — i18n 语言、版本列表、导航栏、页脚、Algolia 搜索配置
- `sidebars.ts` — 按一级分类组织侧边栏（入门/安装/编程/概念/教程/库/硬件/配置/发布/术语）
- `BilingualViewer/` — 核心对照组件，支持左右分栏和逐段对照两种模式
- `ArticleMeta/` — 显示原文链接、ROCm 版本、标签、适用环境等元信息
- `scripts/sync-rocm-docs.py` — 从 `github.com/ROCm/` 克隆源仓库，提取 RST/MD 文件，转换为统一 MD
- `scripts/translate.py` — 批量调用翻译 API，生成中文译文，对齐段落
- `glossary/rocm-terms.yaml` — 术语中英对照，用于翻译一致性保证和悬浮提示
- `.github/workflows/` — CI/CD：构建部署 + 内容同步

---

## Phase 0：环境准备

### 任务 0.1：确认开发环境

**文件：** 无新建

- [ ] **步骤 1：检查 Node.js 版本**

```bash
node -v   # 需要 >= 18.0，推荐 20+
npm -v    # 需要 >= 9
```

- [ ] **步骤 2：检查 Git 配置**

```bash
git config user.name
git config user.email
```

- [ ] **步骤 3：创建项目仓库**

```bash
cd ~/projects/rocm-bilingual-docs
git init
echo "node_modules/\n.docusaurus/\nbuild/\ni18n/\n__pycache__/\n.env" > .gitignore
```

---

## Phase 1：Docusaurus 脚手架

### 任务 1.1：初始化 Docusaurus 项目

**文件：**
- 创建：整个项目骨架（由 `create-docusaurus` 生成）

- [ ] **步骤 1：使用脚手架创建项目**

```bash
cd ~/projects
npx create-docusaurus@latest rocm-bilingual-docs classic --typescript
```

- [ ] **步骤 2：验证开发服务器启动**

```bash
cd ~/projects/rocm-bilingual-docs
npm run start
# 预期：localhost:3000 显示 Docusaurus 默认首页
# 验证后 Ctrl+C 停止
```

- [ ] **步骤 3：安装额外依赖**

```bash
npm install clsx                           # 条件类名工具
npm install @docusaurus/plugin-content-docs # 文档插件（通常已内置）
npm install prism-react-renderer           # 代码高亮（已内置，确认版本）
```

- [ ] **步骤 4：Commit**

```bash
git add -A
git commit -m "chore: initialize Docusaurus project with TypeScript"
```

### 任务 1.2：配置 i18n 双语支持

**文件：**
- 修改：`docusaurus.config.ts`

- [ ] **步骤 1：在 `docusaurus.config.ts` 添加 i18n 配置**

```typescript
// docusaurus.config.ts 关键片段
const config: Config = {
  // ... 其他配置
  
  // i18n 配置
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'zh-Hans'],
    localeConfigs: {
      en: {
        htmlLang: 'en-US',
        label: 'English',
      },
      'zh-Hans': {
        htmlLang: 'zh-Hans',
        label: '简体中文',
      },
    },
  },

  // 主题配置：添加语言切换
  themeConfig: {
    navbar: {
      // ... 其他导航项
      items: [
        {
          type: 'localeDropdown',
          position: 'right',
        },
      ],
    },
  },
};
```

- [ ] **步骤 2：添加中文翻译的基础 UI 字符串**

```bash
npm run write-translations -- --locale zh-Hans
# 检查 i18n/zh-Hans/ 目录是否生成
```

- [ ] **步骤 3：修改 `i18n/zh-Hans/code.json` 中的导航文本**

关键修改项：
```json
{
  "theme.common.editThisPage": {
    "message": "在 GitHub 上编辑此页"
  },
  "theme.common.skipToMainContent": {
    "message": "跳到主要内容"
  },
  "theme.SearchPage.placeholder": {
    "message": "搜索文档..."
  }
}
```

- [ ] **步骤 4：验证双语切换**

```bash
npm run start -- --locale zh-Hans
# 访问 http://localhost:3000/zh-Hans/ 确认中文界面
```

- [ ] **步骤 5：Commit**

```bash
git add docusaurus.config.ts i18n/
git commit -m "feat: configure i18n for English and Simplified Chinese"
```

### 任务 1.3：配置版本管理

**文件：**
- 修改：`docusaurus.config.ts`
- 创建：`docs/` 下的版本化目录结构

- [ ] **步骤 1：创建首个版本文档目录**

```bash
# 将默认 docs/ 内容移动到版本化位置（当前最新版本 7.2.2）
mkdir -p docs/7.2.2
mv docs/intro.md docs/7.2.2/ 2>/dev/null || true
mv docs/tutorial-basics docs/7.2.2/ 2>/dev/null || true
mv docs/tutorial-extras docs/7.2.2/ 2>/dev/null || true
```

- [ ] **步骤 2：在 `docusaurus.config.ts` 添加版本配置**

```typescript
// 在 presets 中配置
presets: [
  [
    'classic',
    {
      docs: {
        path: 'docs',
        routeBasePath: 'docs',
        sidebarPath: './sidebars.ts',
        // 版本配置
        lastVersion: 'current',      // "current" 指向最新版
        versions: {
          current: {
            label: '7.2.2 (最新)',
            path: '7.2.2',
            banner: 'none',
          },
        },
        // 仅包含 7.2.2+ 的文档（不显示旧版默认内容）
        onlyIncludeVersions: ['current'],
      },
    },
  ],
],
```

- [ ] **步骤 3：修改 `sidebars.ts` 分类结构**

```typescript
// sidebars.ts — 一级分类侧边栏
const sidebars = {
  docs: [
    {
      type: 'category',
      label: '入门指南',
      link: { type: 'doc', id: 'getting-started/what-is-rocm' },
      items: [
        'getting-started/what-is-rocm',
        'getting-started/overview',
      ],
    },
    {
      type: 'category',
      label: '安装部署',
      items: [
        'install/linux-install',
        'install/windows-install',
        'install/radeon-ryzen',
      ],
    },
    // ... 后续分类按需扩展
  ],
};
export default sidebars;
```

- [ ] **步骤 4：Commit**

```bash
git add docusaurus.config.ts sidebars.ts docs/
git commit -m "feat: configure version management for ROCm 7.2.2"
```

---

## Phase 2：内容管道（同步 + 转换）

### 任务 2.1：编写 ROCm 文档同步脚本

**文件：**
- 创建：`scripts/sync-rocm-docs.py`

**说明：** 从 ROCm GitHub 仓库拉取源文档（RST/MD），转换为 Markdown，按分类组织到 `docs/7.2.2/` 目录。

- [ ] **步骤 1：编写同步脚本核心逻辑**

```python
#!/usr/bin/env python3
"""同步 ROCm 官方文档源文件到 Docusaurus docs/ 目录。

从 GitHub ROCm 组织仓库克隆源文档，提取 RST/MD 文件，
转换为 Markdown，按分类组织目录结构。
"""
import os
import subprocess
import shutil
from pathlib import Path

# ROCm 源仓库列表（优先级从高到低）
SOURCE_REPOS = [
    {
        "name": "ROCm",
        "url": "https://github.com/ROCm/ROCm.git",
        "branch": "develop",
        "doc_path": "docs/",
        "category": "getting-started",  # 映射到分类
    },
    {
        "name": "HIP",
        "url": "https://github.com/ROCm/HIP.git",
        "branch": "develop",
        "doc_path": "docs/",
        "category": "programming",
    },
    # Phase 2 扩展更多子项目 repo
]

DOCS_DIR = Path("docs/7.2.2")
TEMP_DIR = Path("/tmp/rocm-sync")
REPO_CACHE = Path.home() / ".cache/rocm-repos"  # 避免重复 clone

# TODO: 后续扩展更多仓库
```

- [ ] **步骤 2：添加 RST → Markdown 转换支持（使用 pandoc）**

```bash
# 确保 pandoc 已安装
which pandoc || sudo apt install -y pandoc
```

```python
def convert_rst_to_md(rst_path: Path, md_path: Path) -> bool:
    """使用 pandoc 将 RST 转换为 Markdown，并保留 frontmatter。"""
    try:
        result = subprocess.run(
            ["pandoc", str(rst_path), "-f", "rst", "-t", "markdown",
             "--wrap=none", "-o", str(md_path)],
            capture_output=True, text=True, timeout=60,
        )
        if result.returncode != 0:
            print(f"  ⚠ pandoc failed: {result.stderr[:200]}")
            return False
        # 添加 Docusaurus frontmatter
        inject_frontmatter(md_path, rst_path)
        return True
    except Exception as e:
        print(f"  ✗ {e}")
        return False
```

- [ ] **步骤 3：添加 frontmatter 注入逻辑**

```python
def inject_frontmatter(md_path: Path, source_path: Path):
    """为 Markdown 文件添加 Docusaurus frontmatter 元数据。

    注入：title、source_url、version、tags、last_update
    """
    with open(md_path, 'r') as f:
        content = f.read()

    # 提取原标题（第一个 # heading）
    title = "Untitled"
    for line in content.split('\n'):
        if line.startswith('# '):
            title = line[2:].strip()
            break

    relative_path = source_path.name
    source_url = f"https://rocm.docs.amd.com/en/latest/{relative_path.replace('.rst', '.html')}"

    frontmatter = f"""---
title: {title}
source_url: {source_url}
version: "7.2.2"
tags: [auto-synced]
last_update: {datetime.now().strftime('%Y-%m-%d')}
---
"""
    with open(md_path, 'w') as f:
        f.write(frontmatter + '\n' + content)
```

- [ ] **步骤 4：添加干运行模式**

```bash
python3 scripts/sync-rocm-docs.py --dry-run
# 预期：列出将要同步的文件清单，不实际写入
python3 scripts/sync-rocm-docs.py
# 预期：同步文档到 docs/7.2.2/，输出同步统计
```

- [ ] **步骤 5：验证同步结果**

```bash
find docs/7.2.2/ -name "*.md" | wc -l   # 预期 > 0
head -20 docs/7.2.2/getting-started/what-is-rocm.md  # 检查 frontmatter
```

- [ ] **步骤 6：Commit**

```bash
git add scripts/sync-rocm-docs.py
git commit -m "feat: add ROCm docs sync script with RST→MD conversion"
```

### 任务 2.2：手动导入首批核心文章

**文件：**
- 创建：`docs/7.2.2/getting-started/what-is-rocm.md`
- 创建：`docs/7.2.2/release/release-notes.md`
- 创建：`docs/7.2.2/compatibility/compatibility-matrix.md`
- ... 更多文章

- [ ] **步骤 1：从 ROCm 官网提取 What is ROCm 页面**

```bash
# 手动方式（Phase 1）：用浏览器访问 https://rocm.docs.amd.com/en/latest/what-is-rocm.html
# 复制内容 → 粘贴到 Markdown 文件，添加 frontmatter
```

创建 `docs/7.2.2/getting-started/what-is-rocm.md`：
```markdown
---
title: What is ROCm?
source_url: https://rocm.docs.amd.com/en/latest/what-is-rocm.html
version: "7.2.2"
tags: [intro, getting-started, linux, windows]
category: getting-started
environment: [Linux, Windows]
application: [AI, HPC, General]
difficulty: beginner
last_update: 2026-04-17
---

# What is ROCm?

> **📎 原文链接：** https://rocm.docs.amd.com/en/latest/what-is-rocm.html

ROCm is an open-source software platform optimized to extract HPC and AI
workload performance from AMD Instinct GPUs and AMD Radeon GPUs while
maintaining compatibility with industry software frameworks.

...（后续内容）
```

- [ ] **步骤 2：首批 5-10 篇核心文章导入清单**

| # | 文章 | 源 URL | 分类 |
|---|------|--------|------|
| 1 | What is ROCm? | `what-is-rocm.html` | 入门指南 |
| 2 | Release Notes 7.2.2 | `about/release-notes.html` | 版本发布 |
| 3 | Compatibility Matrix | `compatibility/compatibility-matrix.html` | 环境与配置 |
| 4 | ROCm on Linux Install | `projects/install-on-linux/` | 安装部署 |
| 5 | GPU Architecture Overview | `conceptual/gpu-arch.html` | 概念原理 |
| 6 | Environment Variables | `reference/env-variables.html` | 环境与配置 |
| 7 | ROCm Libraries | `reference/api-libraries.html` | 库与工具 |
| 8 | Deep Learning with ROCm | `how-to/deep-learning-rocm.html` | 操作教程 |
| 9 | System Optimization | `how-to/system-optimization/` | 性能优化 |
| 10 | Glossary | `reference/glossary.html` | 术语表 |

- [ ] **步骤 3：Commit**

```bash
git add docs/7.2.2/
git commit -m "docs: add initial 10 core ROCm articles with frontmatter"
```

---

## Phase 3：双语对照阅读组件

### 任务 3.1：创建 BilingualViewer 组件

**文件：**
- 创建：`src/components/BilingualViewer/index.tsx`
- 创建：`src/components/BilingualViewer/ParallelView.tsx`
- 创建：`src/components/BilingualViewer/InterleavedView.tsx`
- 创建：`src/components/BilingualViewer/styles.module.css`

- [ ] **步骤 1：创建组件入口**

```typescript
// src/components/BilingualViewer/index.tsx
import React, { useState } from 'react';
import ParallelView from './ParallelView';
import InterleavedView from './InterleavedView';
import styles from './styles.module.css';

type ViewMode = 'parallel' | 'interleaved';

interface BilingualViewerProps {
  enContent: string;    // 英文原文（Markdown 渲染后的 HTML）
  zhContent: string;    // 中文译文
  sourceUrl: string;    // 原文链接
  metadata: {
    version: string;
    tags: string[];
    environment: string[];
  };
}

export default function BilingualViewer({
  enContent,
  zhContent,
  sourceUrl,
  metadata,
}: BilingualViewerProps) {
  const [viewMode, setViewMode] = useState<ViewMode>('parallel');

  return (
    <div className={styles.container}>
      {/* 工具栏：模式切换 + 原文链接 + 元信息 */}
      <div className={styles.toolbar}>
        <div className={styles.modeToggle}>
          <button
            className={viewMode === 'parallel' ? styles.active : ''}
            onClick={() => setViewMode('parallel')}
          >
            ⬌ 左右对照
          </button>
          <button
            className={viewMode === 'interleaved' ? styles.active : ''}
            onClick={() => setViewMode('interleaved')}
          >
            ⬍ 逐段对照
          </button>
        </div>
        <a href={sourceUrl} target="_blank" rel="noopener" className={styles.sourceLink}>
          📎 查看原文
        </a>
      </div>

      {/* 对照内容区 */}
      {viewMode === 'parallel' ? (
        <ParallelView enContent={enContent} zhContent={zhContent} />
      ) : (
        <InterleavedView enContent={enContent} zhContent={zhContent} />
      )}
    </div>
  );
}
```

- [ ] **步骤 2：创建左右对照视图**

```typescript
// src/components/BilingualViewer/ParallelView.tsx
import React from 'react';
import styles from './styles.module.css';

interface ParallelViewProps {
  enContent: string;
  zhContent: string;
}

export default function ParallelView({ enContent, zhContent }: ParallelViewProps) {
  return (
    <div className={styles.parallel}>
      <div className={styles.column}>
        <div className={styles.columnHeader}>🇺🇸 English (Original)</div>
        <div
          className={styles.content}
          dangerouslySetInnerHTML={{ __html: enContent }}
        />
      </div>
      <div className={styles.column}>
        <div className={styles.columnHeader}>🇨🇳 中文翻译</div>
        <div
          className={styles.content}
          dangerouslySetInnerHTML={{ __html: zhContent }}
        />
      </div>
    </div>
  );
}
```

- [ ] **步骤 3：创建逐段对照视图**

```typescript
// src/components/BilingualViewer/InterleavedView.tsx
import React from 'react';
import styles from './styles.module.css';

interface InterleavedViewProps {
  enContent: string;
  zhContent: string;
}

export default function InterleavedView({ enContent, zhContent }: InterleavedViewProps) {
  // 将内容按 <p> 分段，中英交替展示
  const enParagraphs = enContent.split('</p>').filter(s => s.trim());
  const zhParagraphs = zhContent.split('</p>').filter(s => s.trim());

  const pairedParagraphs = [];
  const maxLen = Math.max(enParagraphs.length, zhParagraphs.length);
  for (let i = 0; i < maxLen; i++) {
    pairedParagraphs.push({
      en: enParagraphs[i] || '',
      zh: zhParagraphs[i] || '',
    });
  }

  return (
    <div className={styles.interleaved}>
      {pairedParagraphs.map((pair, i) => (
        <div key={i} className={styles.pair}>
          <div className={styles.enBlock}>
            <div
              className={styles.content}
              dangerouslySetInnerHTML={{ __html: pair.en + '</p>' }}
            />
          </div>
          <div className={styles.zhBlock}>
            <div
              className={styles.content}
              dangerouslySetInnerHTML={{ __html: pair.zh + '</p>' }}
            />
          </div>
        </div>
      ))}
    </div>
  );
}
```

- [ ] **步骤 4：编写 CSS 样式**

```css
/* src/components/BilingualViewer/styles.module.css */
.container {
  margin: 2rem 0;
}

.toolbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.75rem 1rem;
  background: var(--ifm-color-emphasis-100);
  border-radius: 8px;
  margin-bottom: 1.5rem;
}

.modeToggle button {
  padding: 0.4rem 0.8rem;
  border: 1px solid var(--ifm-color-emphasis-300);
  background: transparent;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.85rem;
}

.modeToggle button.active {
  background: var(--ifm-color-primary);
  color: white;
  border-color: var(--ifm-color-primary);
}

.sourceLink {
  font-size: 0.85rem;
  color: var(--ifm-color-primary);
}

.parallel {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
}

.column {
  border: 1px solid var(--ifm-color-emphasis-200);
  border-radius: 8px;
  overflow: hidden;
}

.columnHeader {
  padding: 0.5rem 1rem;
  background: var(--ifm-color-emphasis-100);
  font-weight: 600;
  font-size: 0.85rem;
}

.content {
  padding: 1rem;
}

.interleaved .pair {
  margin-bottom: 1.5rem;
  padding-bottom: 1.5rem;
  border-bottom: 1px dashed var(--ifm-color-emphasis-200);
}

.enBlock {
  margin-bottom: 0.5rem;
}

.zhBlock {
  color: var(--ifm-color-emphasis-700);
  font-style: italic;
}

@media (max-width: 768px) {
  .parallel {
    grid-template-columns: 1fr;
  }
}
```

- [ ] **步骤 5：验证组件渲染**

在 Docusaurus 开发服务器中测试：
```bash
npm run start
# 访问 http://localhost:3000/docs/7.2.2/getting-started/what-is-rocm
# 确认双语对照组件渲染正常
```

- [ ] **步骤 6：Commit**

```bash
git add src/components/BilingualViewer/
git commit -m "feat: add bilingual viewer component with parallel and interleaved modes"
```

### 任务 3.2：创建 ArticleMeta 组件（标签 + 元信息）

**文件：**
- 创建：`src/components/ArticleMeta/index.tsx`
- 创建：`src/components/ArticleMeta/TagBadge.tsx`

- [ ] **步骤 1：编写元信息组件**

```typescript
// src/components/ArticleMeta/index.tsx
import React from 'react';
import TagBadge from './TagBadge';

interface ArticleMetaProps {
  version: string;
  tags: string[];
  environment: string[];
  sourceUrl: string;
  lastUpdate: string;
}

export default function ArticleMeta({
  version,
  tags,
  environment,
  sourceUrl,
  lastUpdate,
}: ArticleMetaProps) {
  return (
    <div style={{ marginBottom: '1.5rem' }}>
      {/* 版本标签 */}
      <TagBadge label={`ROCm ${version}`} color="primary" />
      {/* 环境标签 */}
      {environment.map(env => (
        <TagBadge key={env} label={env} color="info" icon="💻" />
      ))}
      {/* 分类标签 */}
      {tags.map(tag => (
        <TagBadge key={tag} label={tag} color="secondary" />
      ))}
      <div style={{ fontSize: '0.8rem', color: '#888', marginTop: '0.5rem' }}>
        最后更新：{lastUpdate} · <a href={sourceUrl}>📎 原文</a>
      </div>
    </div>
  );
}
```

```typescript
// src/components/ArticleMeta/TagBadge.tsx
import React from 'react';

interface TagBadgeProps {
  label: string;
  color?: 'primary' | 'secondary' | 'info';
  icon?: string;
}

export default function TagBadge({ label, color = 'secondary', icon }: TagBadgeProps) {
  const colors = {
    primary: 'var(--ifm-color-primary)',
    secondary: 'var(--ifm-color-emphasis-500)',
    info: 'var(--ifm-color-info)',
  };

  return (
    <span style={{
      display: 'inline-block',
      padding: '2px 8px',
      margin: '2px 4px 2px 0',
      borderRadius: '4px',
      fontSize: '0.75rem',
      background: colors[color] + '20',
      color: colors[color],
      border: `1px solid ${colors[color]}40`,
    }}>
      {icon && <span style={{ marginRight: '4px' }}>{icon}</span>}
      {label}
    </span>
  );
}
```

- [ ] **步骤 2：Commit**

```bash
git add src/components/ArticleMeta/
git commit -m "feat: add article metadata component with tag badges"
```

---

## Phase 4：翻译管道

### 任务 4.1：创建术语表（保证翻译一致性）

**文件：**
- 创建：`glossary/rocm-terms.yaml`

- [ ] **步骤 1：编写核心术语对照表**

```yaml
# glossary/rocm-terms.yaml
# ROCm 专业术语中英对照表
# 用于：翻译管道术语一致性 + 前端 GlossaryTooltip 组件

terms:
  - en: "ROCm"
    zh: "ROCm（Radeon 开放计算平台）"
    context: "AMD 的开源 GPU 计算软件栈"
    keep_original: true  # 保留英文原名

  - en: "HIP"
    zh: "HIP（异构接口可移植性）"
    context: "AMD 的 CUDA 兼容编程接口"
    keep_original: true

  - en: "HPC"
    zh: "高性能计算 (HPC)"
    context: "High Performance Computing"

  - en: "GPU"
    zh: "GPU（图形处理单元）"
    context: "Graphics Processing Unit"

  - en: "Instinct"
    zh: "Instinct（AMD 数据中心 GPU 系列）"
    context: "AMD data center GPU brand"

  - en: "Radeon"
    zh: "Radeon（AMD 消费级 GPU 系列）"
    context: "AMD consumer GPU brand"

  - en: "CDNA"
    zh: "CDNA（计算 DNA 架构）"
    context: "AMD 数据中心 GPU 架构"

  - en: "RDNA"
    zh: "RDNA（Radeon DNA 架构）"
    context: "AMD 消费级 GPU 架构"

  - en: "Kernel"
    zh: "内核函数 (Kernel)"
    context: "GPU 上并行执行的函数"

  - en: "Wavefront"
    zh: "波前 (Wavefront)"
    context: "GPU 调度基本单元（AMD 架构术语）"

  - en: "Warp"
    zh: "线程束 (Warp)"
    context: "NVIDIA GPU 调度基本单元（等效于 AMD Wavefront）"

  - en: "MIOpen"
    zh: "MIOpen（AMD 深度学习基元库）"
    context: "AMD's Deep Learning Primitives Library"

  - en: "rocBLAS"
    zh: "rocBLAS（ROCm 基础线性代数子程序库）"
    context: "ROCm Basic Linear Algebra Subprograms"

  - en: "Compatibility Matrix"
    zh: "兼容性矩阵"
    context: "OS/GPU/ROCm 版本兼容对照表"

  - en: "Environment Variables"
    zh: "环境变量"
    context: "运行时可配置的系统和库级参数"

  - en: "Compute Unit (CU)"
    zh: "计算单元 (CU)"
    context: "GPU 的基本计算核心组"

  - en: "Infinity Fabric"
    zh: "Infinity Fabric（AMD 高速互联总线）"
    context: "AMD 的芯片互联技术"
    keep_original: true

  - en: "ROCclr"
    zh: "ROCclr（ROCm 计算语言运行时）"
    context: "ROCm Compute Language Runtime"

  - en: "WMMA"
    zh: "WMMA（波前矩阵乘加）"
    context: "Wavefront Matrix Multiply-Accumulate"
```

- [ ] **步骤 2：Commit**

```bash
git add glossary/
git commit -m "docs: add ROCm terminology glossary (EN-ZH)"
```

### 任务 4.2：编写 AI 翻译脚本

**文件：**
- 创建：`scripts/translate.py`

**说明：** 批量翻译 Markdown 文章，保留代码块和 frontmatter，利用术语表确保一致性。

- [ ] **步骤 1：编写翻译脚本**

```python
#!/usr/bin/env python3
"""AI 翻译管道：将英文 ROCm 文档翻译为中文。

工作流：
1. 扫描 docs/7.2.2/ 中无中文翻译的文章
2. 按段落分割，跳过代码块
3. 使用术语表确保专业术语一致
4. 调用翻译 API（DeepL / GPT-4）逐段翻译
5. 保存到 i18n/zh-Hans/ 镜像目录
"""
import os
import re
import yaml
import hashlib
from pathlib import Path
from typing import List, Tuple

DOCS_DIR = Path("docs/7.2.2")
I18N_DIR = Path("i18n/zh-Hans/docusaurus-plugin-content-docs/current")
GLOSSARY_PATH = Path("glossary/rocm-terms.yaml")


def load_glossary() -> dict:
    """加载术语表，构建英文→中文映射。"""
    with open(GLOSSARY_PATH) as f:
        data = yaml.safe_load(f)

    mapping = {}
    for term in data.get("terms", []):
        mapping[term["en"]] = {
            "zh": term["zh"],
            "keep_original": term.get("keep_original", False),
            "context": term.get("context", ""),
        }
    return mapping


def split_markdown(content: str) -> List[Tuple[str, str]]:
    """将 Markdown 内容分割为段落，标注类型。

    Returns: [(type, text), ...]
      type: 'heading' | 'paragraph' | 'code' | 'frontmatter' | 'other'
    """
    segments = []
    lines = content.split('\n')
    i = 0
    in_code = False
    in_frontmatter = False
    buffer = []

    while i < len(lines):
        line = lines[i]

        # Frontmatter 检测
        if i == 0 and line.strip() == '---':
            in_frontmatter = True
            buffer = [line]
            i += 1
            while i < len(lines):
                buffer.append(lines[i])
                if lines[i].strip() == '---':
                    segments.append(('frontmatter', '\n'.join(buffer)))
                    buffer = []
                    in_frontmatter = False
                    i += 1
                    break
                i += 1
            continue

        # 代码块检测
        if line.strip().startswith('```'):
            if in_code:
                buffer.append(line)
                segments.append(('code', '\n'.join(buffer)))
                buffer = []
                in_code = False
            else:
                if buffer:
                    segments.append(('paragraph', '\n'.join(buffer)))
                    buffer = []
                buffer = [line]
                in_code = True
            i += 1
            continue

        if in_code:
            buffer.append(line)
            i += 1
            continue

        # 空行 → 段落分隔
        if line.strip() == '' and buffer:
            segments.append(('paragraph', '\n'.join(buffer)))
            buffer = []
        elif line.strip():
            buffer.append(line)

        i += 1

    if buffer:
        segments.append(('paragraph' if not in_code else 'code', '\n'.join(buffer)))

    return segments


def translate_text(text: str, glossary: dict, api_key: str = None) -> str:
    """调用翻译 API 翻译单个段落。

    优先使用术语表替换专业术语。
    翻译 API 可以是 DeepL、OpenAI GPT-4、或本地模型。
    """
    # TODO Phase 2: 接入实际翻译 API
    # 当前返回占位符 —— 实际使用时替换为 API 调用
    return f"[ZH] {text[:50]}..." if len(text) > 50 else f"[ZH] {text}"


def translate_article(source_path: Path, glossary: dict) -> bool:
    """翻译单篇文章，保存到 i18n 目录。"""
    with open(source_path) as f:
        content = f.read()

    segments = split_markdown(content)
    translated_segments = []

    for seg_type, text in segments:
        if seg_type in ('code', 'frontmatter'):
            translated_segments.append(text)
        elif seg_type == 'paragraph':
            # 应用术语表替换
            for en_term, info in glossary.items():
                if info.get("keep_original"):
                    # 保留原始英文术语但添加中文注释
                    pattern = re.compile(r'\b' + re.escape(en_term) + r'\b')
                    text = pattern.sub(f"{en_term}（{info['zh']}）", text)

            translated = translate_text(text, glossary)
            translated_segments.append(translated)
        else:
            translated_segments.append(text)

    # 确定目标路径
    rel_path = source_path.relative_to(DOCS_DIR)
    target_path = I18N_DIR / rel_path
    target_path.parent.mkdir(parents=True, exist_ok=True)

    with open(target_path, 'w') as f:
        f.write('\n\n'.join(translated_segments))

    return True


def main():
    glossary = load_glossary()
    print(f"📖 已加载 {len(glossary)} 个术语")

    for md_file in sorted(DOCS_DIR.rglob("*.md")):
        rel_path = md_file.relative_to(DOCS_DIR)
        target = I18N_DIR / rel_path

        if target.exists():
            # TODO: 检查源文件是否更新，决定是否重新翻译
            continue

        print(f"🌐 翻译: {rel_path}")
        try:
            translate_article(md_file, glossary)
            print(f"  ✅ 已保存 → {target}")
        except Exception as e:
            print(f"  ❌ 失败: {e}")


if __name__ == "__main__":
    main()
```

- [ ] **步骤 2：测试脚本**

```bash
python3 scripts/translate.py
# 预期：扫描 docs/7.2.2/，输出翻译进度，文件生成到 i18n/zh-Hans/
```

- [ ] **步骤 3：Commit**

```bash
git add scripts/translate.py
git commit -m "feat: add AI translation pipeline with glossary integration"
```

---

## Phase 5：分类与标签系统

### 任务 5.1：配置文档标签和筛选

**文件：**
- 修改：`docusaurus.config.ts`
- 创建：`src/theme/DocSidebar/` (swizzled sidebar with category filters)

- [ ] **步骤 1：在 `docusaurus.config.ts` 添加标签定义**

```typescript
themeConfig: {
  // 标签云配置
  tagline: 'ROCm 官方文档 · 中英对照阅读',
  
  // 分类颜色映射
  colorMode: {
    defaultMode: 'dark',   // 深色主题更护眼
    disableSwitch: false,
  },
  
  // ... 其他配置
}
```

- [ ] **步骤 2：更新 `sidebars.ts` 完整分类**

```typescript
const sidebars = {
  docs: [
    {
      type: 'category',
      label: '🚀 入门指南',
      collapsible: true,
      collapsed: false,
      items: [
        { type: 'autogenerated', dirName: 'getting-started' },
      ],
    },
    {
      type: 'category',
      label: '📦 安装部署',
      collapsible: true,
      collapsed: true,
      items: [
        { type: 'autogenerated', dirName: 'install' },
      ],
    },
    {
      type: 'category',
      label: '💻 编程指南',
      collapsible: true,
      collapsed: true,
      items: [
        { type: 'autogenerated', dirName: 'programming' },
      ],
    },
    {
      type: 'category',
      label: '🧠 概念原理',
      collapsible: true,
      collapsed: true,
      items: [
        { type: 'autogenerated', dirName: 'conceptual' },
      ],
    },
    {
      type: 'category',
      label: '📖 操作教程',
      collapsible: true,
      collapsed: true,
      items: [
        { type: 'autogenerated', dirName: 'how-to' },
      ],
    },
    {
      type: 'category',
      label: '⚡ 性能优化',
      collapsible: true,
      collapsed: true,
      items: [
        { type: 'autogenerated', dirName: 'performance' },
      ],
    },
    {
      type: 'category',
      label: '📚 库与工具',
      collapsible: true,
      collapsed: true,
      items: [
        { type: 'autogenerated', dirName: 'libraries-tools' },
      ],
    },
    {
      type: 'category',
      label: '🔧 环境与配置',
      collapsible: true,
      collapsed: true,
      items: [
        { type: 'autogenerated', dirName: 'environment' },
      ],
    },
    {
      type: 'category',
      label: '📋 版本发布',
      collapsible: true,
      collapsed: true,
      items: [
        { type: 'autogenerated', dirName: 'release' },
      ],
    },
    {
      type: 'category',
      label: '📝 术语表',
      items: [
        { type: 'autogenerated', dirName: 'glossary' },
      ],
    },
  ],
};
```

- [ ] **步骤 2：验证分类侧边栏**

```bash
npm run start
# 访问 http://localhost:3000/docs/7.2.2/
# 确认侧边栏分类正确展开/折叠
```

- [ ] **步骤 3：Commit**

```bash
git add sidebars.ts docusaurus.config.ts
git commit -m "feat: configure full category sidebar and tag system"
```

---

## Phase 6：部署到 GitHub Pages

### 任务 6.1：创建 GitHub Actions 部署工作流

**文件：**
- 创建：`.github/workflows/deploy.yml`

- [ ] **步骤 1：编写部署 Actions**

```yaml
# .github/workflows/deploy.yml
name: Deploy to GitHub Pages

on:
  push:
    branches: [main]
  # 支持手动触发
  workflow_dispatch:

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 0  # 获取完整历史（Docusaurus 需要）

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Build site
        run: npm run build
        env:
          NODE_OPTIONS: --max-old-space-size=4096

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./build
          # 如果需要自定义域名：
          # cname: rocm-docs.yourdomain.com
```

- [ ] **步骤 2：修改 `docusaurus.config.ts` 部署配置**

```typescript
const config: Config = {
  // GitHub Pages 部署配置
  url: 'https://<your-github-username>.github.io',
  baseUrl: '/rocm-bilingual-docs/',  // repo 名称
  organizationName: '<your-github-username>',
  projectName: 'rocm-bilingual-docs',
  // ...
};
```

- [ ] **步骤 3：推送到 GitHub 并验证部署**

```bash
# 创建 GitHub 仓库
gh repo create rocm-bilingual-docs --public --push --source .
# 等待 GitHub Actions 完成
# 访问 https://<username>.github.io/rocm-bilingual-docs/
```

- [ ] **步骤 4：Commit**

```bash
git add .github/workflows/deploy.yml docusaurus.config.ts
git commit -m "ci: add GitHub Pages deployment workflow"
```

### 任务 6.2：创建定时同步工作流（Phase 2 启用）

**文件：**
- 创建：`.github/workflows/sync-and-translate.yml`

```yaml
# .github/workflows/sync-and-translate.yml
name: Sync ROCm Docs & Translate

on:
  schedule:
    # 每周一 UTC 0:00 执行
    - cron: '0 0 * * 1'
  workflow_dispatch:

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install system deps
        run: sudo apt-get install -y pandoc

      - name: Sync ROCm docs
        run: python3 scripts/sync-rocm-docs.py
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}

      - name: Translate new articles
        run: python3 scripts/translate.py
        env:
          TRANSLATE_API_KEY: ${{ secrets.TRANSLATE_API_KEY }}

      - name: Commit changes
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add docs/ i18n/
          git diff --staged --quiet || git commit -m "chore: auto-sync ROCm docs [skip ci]"
          git push
```

---

## Phase 7：未来增强（Phase 2+）

以下功能不在 Phase 1 范围内，但已预留在架构中：

### 7.1 术语表悬浮提示
- **文件：** `src/components/GlossaryTooltip/index.tsx`
- 基于 `glossary/rocm-terms.yaml`，在文章中检测术语并添加 tooltip

### 7.2 版本对比视图
- **文件：** `src/components/VersionDiff/index.tsx`
- 选择两个 ROCm 版本，diff 高亮显示文档变更
- 后端：Git diff 两个版本的文档目录

### 7.3 搜索双语索引
- 配置 Algolia DocSearch（Docusaurus 原生支持）
- 中文内容也能索引，支持跨语言搜索

### 7.4 PDF 导出
- 添加 `docusaurus-plugin-pdf` 或自定义脚本
- 一键导出中英对照排版的 PDF

### 7.5 更新追踪与通知
- 定时检查上游文档变更
- 生成 diff 报告 → 通过 Cron / Telegram 推送通知

### 7.6 ECS 数据库对接
- 当需要用户系统、书签、阅读进度等功能时
- 准备 PostgreSQL 或 SQLite
- API 层：可用 Next.js API Routes 或独立服务

### 7.7 AMD ROCm 博客同步（Phase 2）
- 源：`https://rocm.blogs.amd.com/`（RSS 订阅）
- 同步到 Docusaurus 内置 blog 功能
- 同样进行中英对照处理

---

## 环境要求总览

| 工具 | 版本要求 | 用途 |
|------|---------|------|
| Node.js | >= 20.x | Docusaurus 运行环境 |
| npm | >= 9 | 包管理 |
| Python | >= 3.10 | 同步脚本、翻译管道 |
| Git | >= 2.40 | 版本控制 |
| pandoc | >= 3.1 | RST → Markdown 转换 |
| GitHub CLI (gh) | 可选 | 仓库管理、部署 |

你的环境（Windows 11 + WSL + Ubuntu + VSCode + Node + Python）已完全满足所有要求，无需额外安装系统级工具。唯一需要额外安装的是 `pandoc`：

```bash
sudo apt update && sudo apt install -y pandoc
```

---

## Phase 1 最小可行交付物（MVP）

完成以上 Phase 1-6 后，网站具备以下核心功能：

- ✅ 静态文档站，GitHub Pages 可访问
- ✅ 中/英双语界面切换
- ✅ 左右对照 + 逐段对照阅读模式
- ✅ 首批 10 篇核心 ROCm 文档
- ✅ 按分类（入门/安装/编程/概念/教程等）组织侧边栏
- ✅ 每篇文章带标签（版本、环境、难度、组件）
- ✅ 📎 原文链接直达 rocm.docs.amd.com
- ✅ 版本号标注（7.2.2）
- ✅ 支持后续扩展更多版本
