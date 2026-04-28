# Git 工作流 — rocm-hip-map

> **规范基础：** 提交格式遵循 `chinese-git-workflow` 技能，此处只写项目特有约定。

## 1. 提交铁律（三条）

| 时机 | 说明 |
|------|------|
| **删文件前** | 先 `git add -A && git commit -m "chore: snapshot before cleanup"` |
| **跑批量脚本前** | `scripts/generate-docs.py`、`scripts/fetch-official.py` 等会大量改文件，先提交 |
| **每日收工** | 至少一个 WIP commit，push 到远程 |

**原则：** 宁可多提交 10 个 WIP，也不要丢了东西才后悔。`git rebase -i` 事后可以整理，但丢了就真没了。

## 2. 急救：找回删掉的东西

```bash
# 1. 看历史操作记录
git reflog

# 2. 找到删文件之前的 commit（比如 abc1234）
# 3. 恢复那个 commit 的某个文件
git checkout abc1234 -- path/to/deleted/file.mdx

# 4. 或者整个回到那个 commit（临时）
git checkout abc1234
# 看完后回来
git checkout main

# 5. 如果已经 commit 了删除，撤销那个 commit
git revert <删除commit的hash>
```

`git reflog` 保留 90 天——只要 commit 过，就能找回。

## 3. 分支策略

本项目**单主干**，只用一个 `main` 分支。

- 所有改动直接在 `main` 上做，commit → push
- **不需要** PR / feature 分支 / code review（单人项目 + AI agent）
- 如果某天需要多人协作，再按 `chinese-git-workflow` 技能引入分支策略

## 4. 自动化提交

GitHub Actions 会自动 commit 并 push 到 `main`：

| 工作流 | 触发时间 | 提交内容 |
|--------|---------|---------|
| `sync.yml` | 每天 08:00 CST | 抓取新文档 + 翻译 + 生成 MDX，提交后触发部署 |
| `verify.yml` | 每天 10:00 CST | 校验一致性，如原文更新则标记 `verified v1`，提交标签变更 |

**注意：** 不要在自动化运行期间（08:00-10:00）手动 commit，否则可能冲突。如果不小心冲突了，`git pull --rebase` 解决。

## 5. 提交格式

沿用 Conventional Commits，英文 type + 中文描述：

```
<type>(<scope>): <中文简述>

<详细说明，可选>
```

示例：

```
feat(cuda-map): 新增 50 条 cuBLAS → hipBLAS 映射
fix(build): 修复 {#main-content} 导致 MDX 构建失败
docs(ops): 添加 Git 工作流文档
chore: 删除 BUILD_BROKEN 之前的快照
```

完整规范见 `chinese-commit-conventions` 技能。本项目不强制 commitlint 钩子（轻量优先）。

## 6. 快速参考

| 想做什么 | 命令 |
|----------|------|
| 提交所有 | `git add -A && git commit -m "..." && git push` |
| 看最近改动 | `git log --oneline -10` |
| 看当前状态 | `git status` |
| 放弃本地改动 | `git checkout -- <file>` |
| 回到某个 commit | `git checkout <hash>` |
| 撤销上次 commit（保留改动） | `git reset --soft HEAD~1` |
| 看谁改了哪行 | `git blame <file>` |
