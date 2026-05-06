# ⏰ 定时任务文档

> 最后更新：2026-04-29
> 所有时间均为 UTC，括号内为北京时间 (UTC+8)

---

## 定时任务总览

```
北京时间
  06:00 ─────────────────────────────────────────────
  08:00 ██ sync.yml       抓取→分类→翻译→提交
  10:00 ██ verify.yml     校验全部文章
  11:00 ██ sync-prices.yml  (仅周一)
  14:00 ██ papers.yml      (仅周六)
  20:00 ─────────────────────────────────────────────
```

| Workflow | Cron | 北京时间 | 频率 | 耗时 | 状态 |
|----------|------|----------|------|------|------|
| `sync.yml` | `0 0 * * *` | 每天 08:00 | 每日 | ~1min | ✅ 已解耦 |
| `translate.yml` | `0 4 * * *` | 每天 12:00 | 每日 | ~25min (5篇) | ✅ 新增 |
| `verify.yml` | `0 2 * * *` | 每天 10:00 | 每日 | ~5min | ✅ |
| `sync-prices.yml` | `0 3 * * 1` | 周一 11:00 | 每周 | ~2min | ✅ |
| `papers.yml` | `0 6 * * 6` | 周六 14:00 | 每周 | ~10min | ✅ |
| `test-translate.yml` | — | 手动 | 按需 | ~30min | ✅ |

---

## 各任务详解

### 1. sync.yml — Sync Content

**触发：** 每日 UTC 00:00 (北京时间 08:00) + 手动  
**超时：** 6h，实际 ~1min
**状态：** ✅ 已解耦（翻译已移至 translate.yml）

**步骤链：**

```
┌──────────────────────────┐
│ 1. fetch-official.py     │  抓取 68 篇 AMD 官方文档 (~30s)
├──────────────────────────┤
│ 2. sync-github.py        │  同步 GitHub Issues/PRs (~5s)
├──────────────────────────┤
│ 3. classify.py           │  自动分类 + 打标签 (~5s)
├──────────────────────────┤
│ 4. release-watch.py      │  版本更新检测 (~5s)
├──────────────────────────┤
│ 5. git commit + push     │  ✅ 不再被翻译阻塞 (~5s)
└──────────────────────────┘
```

---

### 2. translate.yml — Translate Content (新增)

**触发：** 每日 UTC 04:00 (北京时间 12:00) + 手动  
**超时：** 6h，实际 ~25min（5篇×5min）
**状态：** ✅ 新增

**断点续传机制：**
```
检查 content/translated/zh/{stem}_zh.md：
  → 不存在          → 📝 翻译
  → is_valid=True   → ✅ 跳过（已完成）
  → is_valid=False  → 🔄 续传（上次失败，重新翻译）
```

**提交策略：** 每翻译完一篇文档立即独立 commit + push，而非批量提交。
- commit message: `translate: {文件名}`
- 中断时已完成的文件不丢失
- git history 可见每篇翻译的精确时间

**手动触发选项：**
- `max_files`: 每次最多翻译篇数（默认 5）
- `mode`: `doc` (文档) / `paper` (论文)

**与 test-translate.yml 的区别：**
| | translate.yml | test-translate.yml |
|--|--------------|-------------------|
| 触发 | 定时 + 手动 | 仅手动 |
| 选文件 | 增量扫描全部未翻译 | 指定文件名列表 |
| 用途 | 日常自动化 | 测试/调试单篇或指定批次 |

---

### 3. verify.yml — Verify Content

**触发：** 每日 UTC 02:00 (北京时间 10:00) + 手动  
**超时：** 未设（默认 6h），实际 ~5min

**步骤：**
```
1. verify.py → 三维校验（一致性 + 准确性 + 通顺性）
2. 产出 data/verification/*.json
3. git commit verification results
```

**依赖：**
- 需要 `data/articles.json`（由 sync.yml 的 classify 产出）
- 需要 `content/translated/zh/*.md`（由 translate 产出）
- 如果 sync.yml 超时导致 articles.json 未更新 → verify.yml 使用旧数据（降级可用）

---

### 4. sync-prices.yml — Sync GPU Prices

**触发：** 周一 UTC 03:00 (北京时间 11:00) + 手动  
**超时：** 未设，实际 ~2min

**步骤：**
```
1. fetch-prices-ebay.py → eBay API (US/DE/UK)
2. normalize-prices.py  → ECB 汇率 + IQR 异常值过滤
3. git commit price updates
```

**依赖：** 无（完全独立）

---

### 5. papers.yml — Sync Papers

**触发：** 周六 UTC 06:00 (北京时间 14:00) + 手动  
**超时：** 未设，实际 ~10min

**步骤：**
```
1. fetch-papers.py  → arXiv API 搜索
2. extract-pdf.py   → PDF → Markdown
3. Copy data to website/static/
4. git commit
```

**依赖：** 无（完全独立）

---

## 依赖关系图（已解耦）

```
                    ┌─────────────┐
                    │  sync.yml   │ (每日 08:00)
                    │ fetch+分类+ │
                    │ 提交        │ ← ✅ ~1min，无阻塞
                    └──┬──────────┘
                       │
          ┌────────────┘
          ▼
   data/articles.json
   content/raw/english/*.md
          │
          │
          ▼
   ┌──────────────┐     ┌──────────────────┐
   │ verify.yml   │     │ translate.yml    │ (每日 12:00)
   │ (每日 10:00) │     │ 增量翻译 5篇     │ ← ✅ 独立，断点续传
   │ 三维校验     │     │ 超时安全         │
   └──────────────┘     └──────────────────┘
                               │
                               ▼
                        content/translated/zh/
                        *_zh.md
                               │
                               ▼
                        ┌──────────────┐
                        │ verify.yml   │ (次日校验翻译)
                        └──────────────┘

   ┌──────────────┐     ┌──────────────┐
   │sync-prices   │     │ papers.yml   │
   │(周一 11:00)  │     │(周六 14:00)  │
   │✅ 完全独立   │     │✅ 完全独立   │
   └──────────────┘     └──────────────┘
```

**关键改进：**
1. `translate.yml` 与 `sync.yml` **完全解耦** — 互不阻塞
2. 翻译采用**增量模式 + 断点续传** — 每次 5 篇，失败可续
3. `verify.yml` 在翻译之前运行 — 先校验原文一致性，次日再校验翻译质量
4. `sync-prices.yml` 和 `papers.yml` 始终独立运行 ✅

---

## 解耦方案（✅ 已实施）

### 实施内容

1. **translate.py 增量模式** — `--incremental` + `--max-files 5`
2. **sync.yml 移除翻译** — 不再执行 `translate.py`
3. **新建 translate.yml** — 独立定时 workflow (每日 12:00)
4. **断点续传** — `_zh.md` 文件大小 > 200B 视为完成，≤200B 视为失败重新翻译

### 拆分后

```
原 sync.yml → 拆为两个独立 workflow：

┌─────────────────────────────────────────────┐
│ sync.yml (每日 08:00, ~1min)               │
│  1. fetch-official.py                      │
│  2. sync-github.py                         │
│  3. classify.py                            │
│  4. release-watch.py                       │
│  5. git commit ← ✅ 不再被翻译阻塞！       │
└─────────────────────────────────────────────┘
              │
              │ 产出: content/raw/english/*.md
              │       data/articles.json
              ▼
┌─────────────────────────────────────────────┐
│ translate.yml (每日 12:00, ~30min 首批)     │
│  translate.py --incremental                 │
│  → 只翻译 _zh.md 不存在的文件               │
│  → 单次最多 ~5 篇新文件（~25min）           │
│  → 超时安全                                  │
└─────────────────────────────────────────────┘
              │
              │ 产出: content/translated/zh/*_zh.md
              ▼
┌─────────────────────────────────────────────┐
│ verify.yml (每日 10:00, ~5min) ← 不变       │
└─────────────────────────────────────────────┘
```

### 新时间线 (北京时间)

```
08:00  sync.yml           抓取+分类+提交  (~1 min)
10:00  verify.yml         校验全部文章    (~5 min)
12:00  translate.yml      增量翻译        (~25 min，仅新增)
11:00  sync-prices.yml    价格同步 (周一) (~2 min)
14:00  papers.yml         论文同步 (周六) (~10 min)
```

---

## translate.py 增量模式设计

```python
# 新增 --incremental 标志
# 遍历 content/raw/english/*.md，检查 content/translated/zh/ 是否已有 _zh.md
# 已有 → skip
# 没有 → translate
# 单次上限: --max-files N (默认 5)

python3 scripts/translate.py --incremental --max-files 5
```

**首次运行：** 翻译前 5 篇未翻译的  
**第二次运行：** 翻译下 5 篇  
**...**  
**68 篇全部翻译完毕：** 运行 14 次×25min，零超时风险  
**之后每天（amd 新增文章时）：** 只翻译增量 1-2 篇，秒级完成

---

## translate.py 增量模式 — 与现有 --file 模式配合

| 场景 | 命令 | 谁触发 |
|------|------|--------|
| 每日增量翻译 | `--incremental --max-files 5` | `translate.yml` 定时 |
| 测试单篇 | `--file xxx.md` | `test-translate.yml` 手动 |
| 全量重翻 | 无参数 (不推荐) | 手动 workflow_dispatch |
| 论文翻译 | `--papers-dir ...` | `papers.yml` 后续扩展 |
