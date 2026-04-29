# 🐛 Bug 记录

> 记录项目开发过程中发现的所有 bug，包含根因分析、修复方案和预防措施。

---

## BUG-001: 翻译输出嵌套路径（translate.py）

**发现日期：** 2026-04-29  
**严重程度：** 🟡 Medium（翻译结果路径错位，功能不可用但不影响主站）  
**提交：** `eebb8ca` `e7403f6`  
**状态：** ✅ 已修复

### 症状

翻译文件输出到嵌套路径：
```
实际: content/translated/zh/content/raw/english/xxx_zh.md
预期: content/translated/zh/xxx_zh.md
```

### 根因分析

**因果链：**
```
translate.py --file 接受相对路径
  → Path(args.file) 保持相对
  → filepath.parents = {Path('content/raw/english'), Path('content'), Path('.')}
  → CONTENT_RAW_EN = Path('/abs/path/content/raw/english')（绝对）
  → "相对" in "绝对列表" → False
  → 命中 else 分支
  → rel_path = filepath（仍为相对路径）
  → out = CONTENT_TRANSLATED_ZH / rel_path / ...  ← 嵌套！
```

**根本原因：** 路径常量 `CONTENT_RAW_EN` 等未调用 `.resolve()`，与已 resolve 的 `filepath` 在 `in filepath.parents` 比较时不匹配。

### 修改点

- `scripts/translate.py:35-39` — 5 个路径常量全部加 `.resolve()`
- `.github/workflows/test-translate.yml` — 诊断步骤改用直接路径断言，扩大 find 深度

### 为何之前没发现

1. **本地测试习惯用绝对路径：** 开发时通常 `cd` 到项目根再跑脚本，相对路径展开后碰巧匹配
2. **CI 首次运行即暴露：** `workflow_dispatch` 触发时，输入的 `content/raw/english/xxx` 是相对路径
3. **e7403f6 只修了 --file handler：** 上次修复只加了 `path.resolve()`，没意识到路径常量也需要 resolve
4. **`else` 分支覆写隐患：** 代码中 else 分支重写了 rel_path → out_path 逻辑，掩盖了 if 未被命中的事实

### 最小修复

路径常量加 `.resolve()`（已应用）。

### 长期优化

- **BUG-002 全量硬化：** 项目所有 Python 脚本的 Path 常量一律 `.resolve()`
- **新增 lint 规则：** PR 审查时检查 `path in other.parents` 模式，确保两边都是绝对路径

### 新增测试

- CI workflow 的 "Show translation result" 步骤改为直接路径断言（不再依赖 find 通配符）
- 本地编译验证：`npm run build` 每次 PR 前强制执行

---

## BUG-002: 全量路径常量 resolution 缺失

**发现日期：** 2026-04-29  
**严重程度：** 🔴 Critical（`gen-papers-sidebar.py` 纯相对路径，跨目录运行必炸）  
**提交：** TBD  
**状态：** ✅ 已修复

### 症状

`gen-papers-sidebar.py` 在任何非项目根目录运行时，`os.listdir(Path("website/docs/papers"))` 因相对路径找不到目录而崩溃。

其余 4 个脚本的路径常量虽是绝对路径（从 resolved PROJECT_ROOT 派生），但未 `.resolve()`，与 BUG-001 模式相同，可能在 symlink 环境或 CI 中触发。

### 根因分析

| 脚本 | 问题 | 风险 |
|------|------|------|
| `gen-papers-sidebar.py` | 3 个常量全是纯相对路径 `Path("relative")`，没有 PROJECT_ROOT | 🔴 必炸 |
| `cache-images.py` | 6 个常量从 resolved PROJECT_ROOT 派生但未 .resolve() | 🟡 可能炸 |
| `generate-docs.py` | 4 个常量同上 | 🟡 可能炸 |
| `related-articles.py` | 3 个常量同上 | 🟡 可能炸 |
| `verify.py` | 4 个常量同上 | 🟡 可能炸 |

### 修改点

全部 5 个脚本的所有路径常量加 `.resolve()`，`gen-papers-sidebar.py` 额外补充 PROJECT_ROOT。

### 长期优化

建立项目编码规范：**所有 Path 常量必须 `.resolve()`**，写入 `docs/lessons-learned.md`。
