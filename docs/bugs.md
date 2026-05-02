# 🐛 Bug 记录

> 记录项目开发过程中发现的所有 bug，按时间倒序排列。
> 每个 bug 包含：症状 → 根因 → 修改点 → 预防措施。

---

## BUG-001: 全量路径常量 `.resolve()` 缺失 (2026-04-29)

**严重程度：** 🔴 Critical  
**提交：** `e9379ea`  
**分类：** Python / 路径解析  
**状态：** ✅ 已修复

### 症状

`gen-papers-sidebar.py` 在非项目根目录运行时 `os.listdir(Path("website/docs/papers"))` 崩溃。
其余 4 脚本 (`cache-images`, `generate-docs`, `related-articles`, `verify`) 的路径常量从 resolved PROJECT_ROOT 派生但未 `.resolve()`。

### 根因

| 脚本 | 问题 | 风险 |
|------|------|------|
| `gen-papers-sidebar.py` | 3 个常量是纯相对路径 `Path("...")`，无 PROJECT_ROOT | 🔴 必炸 |
| `cache-images.py` | 6 个常量未 `.resolve()` | 🟡 可能炸 |
| `generate-docs.py` | 4 个常量未 `.resolve()` | 🟡 可能炸 |
| `related-articles.py` | 3 个常量未 `.resolve()` | 🟡 可能炸 |
| `verify.py` | 4 个常量未 `.resolve()` | 🟡 可能炸 |

### 修改点

全部 5 脚本的 20 个路径常量加 `.resolve()`。`gen-papers-sidebar.py` 额外补充 `PROJECT_ROOT`。

### 预防

建立铁律：**所有 Python Path 常量必须 `(PROJECT_ROOT / "rel").resolve()`**。

---

## BUG-002: translate.py 翻译输出嵌套路径 (2026-04-29)

**严重程度：** 🟡 Medium  
**提交：** `e7403f6` `eebb8ca`  
**分类：** Python / 路径解析  
**状态：** ✅ 已修复（两次迭代）

### 症状

翻译输出到 `content/translated/zh/content/raw/english/xxx_zh.md`（嵌套），正确应为 `content/translated/zh/xxx_zh.md`。

### 根因

`--file` 接受相对路径 → `Path(args.file)` 保持相对 → `filepath.parents` 中无绝对路径 → `CONTENT_RAW_EN in filepath.parents` 为 `False` → 命中 else 分支输出嵌套路径。

- **第一次修复 (e7403f6):** `--file` handler 加 `path.resolve()`，但路径常量未 resolve。
- **第二次修复 (eebb8ca):** 5 个路径常量全部 `.resolve()`。

### 预防

- Path 常量与比较对象必须同时 resolve
- CI 诊断用确定性路径而非 `find` 通配符

---

## BUG-003: `generate-docs.py` `../_images/` 图片路径 (2026-04-29)

**严重程度：** 🟡 Medium  
**提交：** `874136f`  
**分类：** Python / 内容生成  
**状态：** ✅ 已修复

### 症状

Pandoc 转换的 MDX 文件中，图片引用指向 `../_images/`，Docusaurus 无法解析。

### 根因

Pandoc 在导出时保持原始 Markdown 相对路径，但这些路径在 Docusaurus 的 `static/` 目录下不存在。

### 修改点

`generate-docs.py` 中将 `../_images/` 替换为 `/rocm-hip-map/img/`。

### 预防

内容生成脚本应在生成后运行路径校验步骤。

---

## BUG-004: `validate.yml` `continue-on-error` 缩进 (2026-04-29)

**严重程度：** 🟡 Medium  
**提交：** `09d0298`  
**分类：** CI/CD / YAML  
**状态：** ✅ 已修复

### 症状

`validate.yml` 的 `continue-on-error: true` 缩进层级错误，导致该 step 的 shell 命令未执行。

### 根因

YAML 中 `continue-on-error` 放到了与 `run` 同级而非 `step` 级别，GitHub Actions 静默忽略后该 step 退化为 no-op。

### 修改点

将 `continue-on-error: true` 移到正确的缩进层级（`- name:` 同级）。

### 预防

CI 配置文件用 `yamllint` 或 GitHub Actions VS Code 插件检查缩进。

---

## BUG-005: `validate.yml` 外链检查 403 (2026-04-29)

**严重程度：** 🟢 Low  
**提交：** `a7a9691`  
**分类：** CI/CD / 网络  
**状态：** ✅ 已修复

### 症状

`validate.yml` 的外链检查对 `docs.amd.com` 全部返回 403。

### 根因

AMD 官方文档服务器屏蔽 GitHub Actions runner IP 段。

### 修改点

外链检查改为格式校验（URL 格式是否合法），不再做 HTTP 可达性验证。

### 预防

对已知会屏蔽 CI IP 的外部源，建立豁免列表。

---

## BUG-006: `validate.yml` `articles.json` 结构 (2026-04-29)

**严重程度：** 🟡 Medium  
**提交：** `7a70997`  
**分类：** CI/CD / 数据格式  
**状态：** ✅ 已修复

### 症状

`validate.yml` 将 `articles.json` 当作 `list` 处理，实际数据结构为 `{"articles": [...], "stats": {...}}`，导致 `for article in articles` 迭代 dict key。

### 根因

脚本初期 `articles.json` 是纯列表，后来增加了 `stats` 字段包裹为 dict，CI 未同步更新。

### 修改点

`validate.yml` 将 `jq '.[]'` 改为 `jq '.articles[]'`。

### 预防

数据 schema 变更时，必须同步更新所有消费者（CI、脚本、生成器）。

---

## BUG-007: 部署烟雾测试脚本 (2026-04-28~29)

**严重程度：** 🟡 Medium  
**提交：** `9d5a81b` `4756aa1`  
**分类：** CI/CD / 部署  
**状态：** ✅ 已修复

### 症状

初始烟雾测试仅检查静态 HTML 文件存在性，未验证 HTTP 响应。

### 修改点

改为两步验证：(1) 部署前检查 `website/build/` 产物完整性，(2) 部署后对 5+ 关键页面做 HTTP 200 断言。

### 预防

部署验证必须做 HTTP 层面的测试，不能仅依赖文件存在检查。

---

## BUG-008: `translate.py` 跳过模式不完整 (2026-04-28)

**严重程度：** 🟢 Low  
**提交：** `d16398f`  
**分类：** Python / 翻译管道  
**状态：** ✅ 已修复

### 症状

`changelog.md`、`versions.md`、`release-notes.md` 等不适合翻译的文件仍被处理。

### 修改点

`translate_markdown_file()` 添加 `SKIP_PATTERNS` 列表 + 超大文件 (>500KB) 自动跳过。

### 预防

翻译管道应有文件类型白名单/黑名单机制。

---

## BUG-009: `sync.yml` `cache:pip` 失败 (2026-04-28)

**严重程度：** 🟡 Medium  
**提交：** `fa2994d`  
**分类：** CI/CD / GitHub Actions  
**状态：** ✅ 已修复

### 症状

`setup-python@v5` + `cache: pip` 在 repo 根没有 `requirements.txt` 时失败。

### 根因

`cache: pip` 需要在仓库根目录存在 `requirements.txt` 才能计算缓存 hash。

### 修改点

移除 `cache: pip`，改为纯 `pip install`（依赖少，安装快）。

### 预防

使用 `cache: pip` 前确认仓库根存在 `requirements.txt`；否则不加 cache。

---

## BUG-010: GitHub Pages 部署权限 (2026-04-28)

**严重程度：** 🔴 Critical  
**提交：** `ffe4fa7`  
**分类：** CI/CD / 部署  
**状态：** ✅ 已修复

### 症状

Deploy job 报 `Permission denied` 无法写入 `gh-pages` 分支。

### 根因

未使用 `actions/deploy-pages@v4`，手动 git push 方式缺乏 Pages 写入权限。

### 修改点

改用 GitHub 官方 Action：`actions/configure-pages` → `actions/upload-pages-artifact` → `actions/deploy-pages`。

### 预防

GitHub Pages 部署必须使用官方 Action 链，不走手动 git 流程。

---

## BUG-011: MDX 构建失败 — BilingualViewer 残骸 + ArticleHeader 导入 (2026-04-28)

**严重程度：** 🔴 Critical  
**提交：** `cb46042` `d238cc0`  
**分类：** Docusaurus / React / MDX  
**状态：** ✅ 已修复

### 症状

`npm run build` 失败，错误指向 `BilingualViewer` 组件不存在、`ArticleHeader` 导入方式错误。

### 根因

1. **BilingualViewer 残骸：** 组件已删除 (`BilingualViewer.tsx` 移除)，但 `generate-docs.py` 仍为所有 MDX 生成 `<BilingualViewer ...>` 标签
2. **ArticleHeader 导入：** `ArticleHeader` 是 `default export`，MDX 中 `import { ArticleHeader }` 应改为 `import ArticleHeader`

### 修改点

- `generate-docs.py`：移除 `<BilingualViewer>` 模板片段
- 68+ 篇 MDX：批量替换 `{ ArticleHeader }` → `ArticleHeader`

### 预防

- 删除组件后必须同步更新 `generate-docs.py` 模板
- 组件导出方式变更后需检查所有 MDX 导入

---

## BUG-012: `generate-docs.py` f-string 语法错误 (2026-04-28)

**严重程度：** 🔴 Critical  
**提交：** `412b2d1`  
**分类：** Python / 语法  
**状态：** ✅ 已修复

### 症状

`generate-docs.py` 运行时 `SyntaxError: f-string expression part cannot include a backslash`。

### 根因

f-string 内部使用 `\n` 转义：
```python
f"...{value.replace('\n', ' ')}..."  # ❌
```

### 修改点

将包含 `\` 的表达式提取为变量：
```python
_val = value.replace('\n', ' ')
f"...{_val}..."  # ✅
```

### 预防

Python 3.11 及以下不允许 f-string 表达式含 `\`。用 pylint/flake8 静态检查。

---

## BUG-013: `ArticleHeader` 错误回退到 `metadata.source` (2026-05-02)

**严重程度：** 🟡 Medium  
**分类：** Docusaurus / Frontmatter / 外链  
**状态：** ✅ 已修复

### 症状

当文档缺少 `source_url` 时，页面“查看原文”链接会回退到站内 Markdown 源文件路径，而不是外部原文地址。

### 根因

`metadata.source` 是 Docusaurus 的源码路径，不是原始文章 URL。

### 修改点

`website/src/components/ArticleHeader.tsx` 不再使用 `metadata.source` 作为外链回退；测试同步修正。

### 预防

Docusaurus `metadata.*` 字段必须先确认语义，不能把源码路径误当业务 URL。

---

## BUG-014: `db/dao.py` 读取行对象时重复 `fetchone()` (2026-05-02)

**严重程度：** 🔴 Critical  
**分类：** Python / SQLite DAO  
**状态：** ✅ 已修复

### 症状

`article_get_by_id()` / `article_get_by_hash()` 在已有记录时仍返回 `None`，导致读取文章记录失败。

### 根因

同一查询里调用了两次 `fetchone()`，第一次已消耗结果，第二次返回 `None`。

### 修改点

统一先保存 `row = cur.fetchone()`，再做 `dict(row) if row else None`。

### 预防

DAO 查询返回单行时，禁止在同一分支里多次调用 `fetchone()`。

---

## BUG-015: URL 规范化未正确保留非追踪查询参数 (2026-05-02)

**严重程度：** 🔴 Critical  
**分类：** Python / 去重 / 数据一致性  
**状态：** ✅ 已修复

### 症状

例如 `https://example.com/post?utm_source=test&a=1` 被错误规范化为 `https://example.com/post&a=1`，导致 URL 哈希错误。

### 根因

去除首个追踪参数后，没有把后续 `&` 恢复成合法的 `?` 查询串起始符。

### 修改点

`db/dao.py` 的 `normalize_url()` 改为先删除追踪参数，再清理 `?&`、重复 `&` 和尾部残留分隔符。

### 预防

URL 规范化测试必须覆盖“追踪参数 + 正常参数混合”场景，而不只是纯追踪参数场景。
