# 📖 经验教训

> 开发过程中的踩坑记录和最佳实践，避免重复犯错。

---

## 1. Python Path 常量必须 `.resolve()`

**教训来源：** BUG-001, BUG-002  
**日期：** 2026-04-29

### 问题

Python 的 `pathlib.Path` 对象在 "未 resolve" 和 "已 resolve" 状态下，`==` 和 `in` 比较可能失败，即使指向同一文件。

### 铁律

```python
# ❌ 错误
PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = PROJECT_ROOT / "content" / "raw"    # 未 resolve!

# ✅ 正确
PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = (PROJECT_ROOT / "content" / "raw").resolve()
```

**适用范围：** 项目中所有 Python 脚本的 **每一个** Path 常量，无一例外。

### 为什么 `.resolve()` 是必要的

1. **`path in parents` 比较：** 当两个 Path 对象一个 resolved、一个 unresolved 时，字符串表示可能不同（symlink、大小写、尾部斜杠）
2. **CI 环境差异：** GitHub Actions 的 `/home/runner/work/` 可能是挂载点，路径字符串与本地不同
3. **`.relative_to()` 失败：** 如果目标路径比源路径更 "resolved"，`relative_to()` 抛出 `ValueError`

### 检查清单

代码审查时检查以下模式：
- `Path("相对路径")` → 必须改为 `(PROJECT_ROOT / "相对路径").resolve()`
- `PROJECT_ROOT / "..."` → 必须包裹 `.resolve()`
- `path in other.parents` → 两边都必须是 resolved
- `path.relative_to(base)` → base 必须是 resolved

---

## 2. CI 诊断用确定性路径，不用模糊搜索

**教训来源：** BUG-001  
**日期：** 2026-04-29

### 问题

```bash
# ❌ 模糊 — 找不到时不知道是路径错了还是文件真不存在
OUT=$(find content/translated/zh -name "${STEM}_zh.md" | head -1)

# ✅ 确定 — 路径错了直接暴露
OUT="content/translated/zh/${STEM}_zh.md"
if [ -f "$OUT" ]; then ...
```

---

## 3. CI 修复后必须总结经验

**教训来源：** 用户要求  
**日期：** 2026-04-29

每次 CI/构建修复后，按以下格式输出：
1. 根因分析
2. 修改点
3. 如何预防再次发生
4. 更新 `docs/bugs.md`
5. 更新 `docs/lessons-learned.md`（通用问题）

---

## 4. 功能变更必须同步更新三类文档

**教训来源：** 用户要求  
**日期：** 2026-04-29

每次功能变更（新增 Phase、修改组件、调整管道），必须同步更新：
1. `docs/templates/page-template.md` — 模板规范
2. `scripts/generate-docs.py` — 生成器（如涉及 MDX）
3. `docs/PROGRESS.md` — 进度文档

---

## 5. Docusaurus `metadata.source` 不是业务外链

**教训来源：** BUG-013  
**日期：** 2026-05-02

### 问题

`useDoc().metadata.source` 指向仓库中的文档源文件，不是 frontmatter 中的原文 URL。

### 规则

- 原文链接只能来自显式业务字段（如 `source_url`）
- 框架 metadata 只能在确认语义后再参与 UI 映射

---

## 6. 测试生成物必须排除出 TypeScript 工程

**教训来源：** 本次 remediation 过程中的 `coverage/` 污染 `tsc`  
**日期：** 2026-05-02

### 问题

Vitest coverage 产物进入 `tsc` 默认 include 范围后，会触发无关的 TS6053 文件错误。

### 规则

- `tsconfig.json` 必须显式排除 `coverage`
- 测试工具输出目录要视为构建产物，不参与类型检查

---

## 7. 全局 stub 需要和测试生命周期绑定

**教训来源：** TypeScript reviewer + 前端测试回归  
**日期：** 2026-05-02

### 问题

`vi.stubGlobal()` 在测试文件顶层执行时，容易造成跨文件污染；启用 `unstubGlobals` 后又会暴露顶层 stub 丢失问题。

### 规则

- 全局 stub 放进 `beforeEach`
- Vitest 配置启用 `unstubGlobals: true`
- 让隔离成为默认，而不是依赖测试执行顺序
