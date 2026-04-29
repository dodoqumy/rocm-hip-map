# 定时任务并行化解耦评估

**创建时间：** 2026-04-29  
**状态：** 📋 待评审  
**依赖：** 无

---

## 目标

评估全部 5 个定时任务的 AI 依赖程度和并行化可行性，找出可拆分并行加速的任务，识别 AI 强依赖导致不便并行的瓶颈。

---

## 各任务评估

### 1. sync.yml — 内容抓取+分类

**AI 依赖：** 🟢 无（纯 HTTP + 文件 I/O）  
**当前耗时：** ~1min  
**并行化空间：** 🟡 有，但当前够快不需要

| 步骤 | 耗时 | 独立性 | 可并行？ |
|------|------|--------|----------|
| `fetch-official.py` | ~30s | 独立 | ✅ |
| `sync-github.py` | ~5s | 独立 | ✅ |
| `classify.py` | ~5s | 依赖 fetch 产出 | ❌ 需串行 |
| `release-watch.py` | ~5s | 独立 | ✅ |

**并行方案：** `fetch-official` 和 `sync-github` 可同时在两个 job 跑，但总耗时从 45s 降到 30s，收益太小（<15s），不建议过度拆分。

**结论：** 维持现状 ✅

---

### 2. translate.yml — AI 翻译

**AI 依赖：** 🔴 极强（每篇调用 opencode DeepSeek API）  
**当前耗时：** ~25min（5 篇 × 5min/篇）  
**并行化空间：** 🟡 理论上可并行，但受 API key 限流

| 因素 | 分析 |
|------|------|
| API 限流 | opencode-go 免费层有速率限制，并行 `--file` 调用会触发 429 |
| API Key 共享 | 只有一个 `TRANSLATE_API_KEY`，所有并行 worker 抢同一个 key |
| 断点续传 | 已有 `--incremental`，文件系统即断点，天然适合串行队列 |
| 文件级独立 | 每篇翻译完全独立，不需要共享状态 |

**可尝试的并行方案（保守）：**

```
不并行翻译 API 调用本身，而是并行「翻译的前后步骤」：

┌──────────────────────────────────────────────────┐
│ translate.yml                                     │
│                                                    │
│  Step 1: 扫描待翻译文件列表 (串行, ~1s)            │
│     ↓                                              │
│  Step 2: 生成术语表 (串行, ~0.1s)                 │
│     ↓                                              │
│  Step 3: 串行翻译 N 篇 (串行, N×5min) ← 瓶颈      │
│     ↓                                              │
│  Step 4: git commit (串行, ~5s)                    │
└──────────────────────────────────────────────────┘
```

瓶颈在 Step 3（API 调用串行），无法通过拆分 workflow 加速。

**如果将来有多个 API Key 或 opencode 放宽限流：**

```yaml
# 批量并行翻译（matrix 模式）
strategy:
  matrix:
    file: [file1.md, file2.md, file3.md, file4.md, file5.md]
  max-parallel: 3
steps:
  - run: python3 scripts/translate.py --file ${{ matrix.file }}
```

**结论：** 维持串行增量 ✅。拆分并行收益为负（会触发 API 429 限流导致整体更慢）。

---

### 3. verify.yml — 内容校验

**AI 依赖：** 🔴 强（翻译准确性/通顺性校验调用 LLM）  
**当前耗时：** ~5min（校验全部文章）  
**并行化空间：** 🟡 同 translate.yml，受 API key 限流

| 校验维度 | 耗时占比 | 是否调用 AI | 可并行？ |
|----------|----------|-------------|----------|
| 原文一致性 | ~20% | ❌ 纯 HTTP HEAD + curl | ✅ 可独立 |
| 翻译准确性 | ~40% | 🔴 LLM 审查 | ⚠️ 受限 API |
| 翻译通顺性 | ~40% | 🔴 LLM 审查 | ⚠️ 受限 API |

**可做的优化（非并行）：**

1. 拆成两个 workflow：`verify-content.yml`（纯 HTTP 一致性，每日 08:30）+ `verify-translation.yml`（LLM 校验，错峰运行）
2. 翻译校验按文章分批，每批 10 篇，避免单次运行超时
3. 一致性校验可全并行（HEAD 请求无 API key 限制）

```
原 verify.yml (~5min)
  ├── 一致性校验 (20%, 无 AI)  → 移到 sync.yml 之后立即跑
  └── 翻译校验 (80%, 强 AI)    → 保留在 verify.yml，与 translate 错峰
```

**结论：** 🟡 建议拆分一致性校验出来。翻译校验串行不变。

---

### 4. sync-prices.yml — GPU 价格抓取

**AI 依赖：** 🟢 无（纯 HTTP API）  
**当前耗时：** ~2min（3 个国家串行）  
**并行化空间：** 🟢 **高！最适合拆分并行**

| 因素 | 分析 |
|------|------|
| 国家独立性 | US、DE、UK 完全独立，不同站点、不同货币 |
| API 限流 | eBay API 5000 calls/day，单国家 ~50 calls，并行 3 国家 ~150 |
| 脚本改造量 | 小 — `fetch-prices-ebay.py` 已有 `--site` 参数 |
| 归一化依赖 | `normalize-prices.py` 需要等所有国家抓完才能合并 → 必须串行在最后 |

**拆分方案：**

```yaml
# Before (串行, ~2min):
#   fetch-prices-ebay.py → normalize-prices.py → commit

# After (并行, ~1min):
jobs:
  # ── 并行抓取各国价格 ──
  fetch-us:
    runs-on: ubuntu-latest
    steps: [..., run: fetch-prices-ebay.py --site EBAY-US]
  fetch-de:
    runs-on: ubuntu-latest
    steps: [..., run: fetch-prices-ebay.py --site EBAY-DE]
  fetch-uk:
    runs-on: ubuntu-latest
    steps: [..., run: fetch-prices-ebay.py --site EBAY-UK]

  # ── 归一化 + 提交（等待所有抓取完成） ──
  normalize:
    needs: [fetch-us, fetch-de, fetch-uk]
    steps: [..., run: normalize-prices.py, git commit]
```

**未来扩展：** Phase 10.2-3 的亚洲/欧洲平台抓取天然适合加入并行矩阵：
```
fetch-us (eBay)  ┐
fetch-de (eBay)  ├── 并行跑
fetch-uk (eBay)  ┘
fetch-jp (Yahoo) ── 独立平台
fetch-cn (闲鱼)  ── 独立平台
```

**结论：** ✅ 推荐拆分。收益明显（2min → 1min），无副作用。

---

### 5. papers.yml — 论文同步

**AI 依赖：** 🟢 无（arXiv API + PDF 提取）  
**当前耗时：** ~10min  
**并行化空间：** 🟢 中等

| 步骤 | 耗时 | 独立性 | 可并行？ |
|------|------|--------|----------|
| `fetch-papers.py` | ~2s | 独立 | ✅ 但太小不需要 |
| `extract-pdf.py` | ~10min | 87 篇 PDF | ✅ 可按论文并行 |

**拆分方案（PDF 提取并行）：**

```yaml
strategy:
  matrix:
    batch: [0, 1, 2, 3, 4]  # 87篇分5批
  max-parallel: 3
steps:
  - run: python3 scripts/extract-pdf.py --batch ${{ matrix.batch }} --total-batches 5
```

但 `extract-pdf.py` 目前没有 `--batch` 参数，需要先改造脚本。改造量中等。

**性价比评估：** 10min 每周一次，并行化降到 3min。改造 1h 换 7min 节省。收益不大。

**结论：** 🟢 暂时维持现状。等论文数量突破 200 篇再考虑。

---

## 汇总表

| Workflow | AI 依赖 | 当前耗时 | 可并行？ | 建议 | 优先级 |
|----------|---------|----------|----------|------|--------|
| `sync.yml` | 🟢 无 | ~1min | 有但收益小 | 维持现状 | — |
| `translate.yml` | 🔴 极强 | ~25min | ❌ API 限流 | 维持串行增量 | — |
| `verify.yml` | 🔴 强 | ~5min | 部分可拆 | 拆分一致性校验 | 🟡 |
| `sync-prices.yml` | 🟢 无 | ~2min | ✅ 按国家并行 | **立即拆分** | 🔴 |
| `papers.yml` | 🟢 无 | ~10min | 可但收益小 | 维持现状 | 🟢 |

---

## 关键规律总结

### ✅ 适合拆分的任务特征

1. **无 AI/API 依赖** — 纯计算或独立 HTTP 请求
2. **天然可分区** — 按国家/类别/文件分片，无共享状态
3. **耗时占比大** — 拆分后收益明显

→ `sync-prices.yml` 是教科书级别的拆分候选。

### ❌ 不适合拆分的任务特征

1. **共享稀缺资源** — 单一 API Key、DB 连接、限流配额
2. **并行代价 > 串行** — 触发 429 后 retry 比串行更慢
3. **已有断点续传** — 文件系统即队列，天然适合串行

→ `translate.yml` 和 `verify.yml` 的 AI 部分属于此类。硬拆只会触发 429，整体更慢。

---

## 实施建议

### 短期（立即可做）

**sync-prices.yml 按国家并行拆分：**
- `fetch-prices-ebay.py` 已有 `--site` 参数，无需改脚本
- 新建 3 个并行 job（US/DE/UK）
- `normalize-prices.py` 等待全部完成后运行
- 预期收益：~2min → ~1min

### 中期（下个 Phase）

**verify.yml 拆分一致性校验：**
- 新建 `verify-content.yml` — 纯 HTTP HEAD 校验（无 AI，无 API key）
- 可全并行（文章间无依赖）
- 原 `verify.yml` 专注翻译质量校验

### 长期（有多个 API Key 后）

**translate.yml 并行化：**
- 需要多个 API key 分散到不同 provider（DeepSeek + OpenAI + DeepL）
- 或 opencode-go 放宽限流
- 实现后可 5 篇并行 → 5min 完成

---

## 文件变更清单（短期）

| 文件 | 操作 | 说明 |
|------|------|------|
| `.github/workflows/sync-prices.yml` | 重写 | matrix 并行按国家拆分 |
| `docs/cron-jobs.md` | 更新 | 并发说明 |

## 文件变更清单（中期）

| 文件 | 操作 | 说明 |
|------|------|------|
| `.github/workflows/verify.yml` | 拆分 | 一致性校验移出 |
| `.github/workflows/verify-content.yml` | 新建 | 纯 HTTP 校验 |
| `docs/cron-jobs.md` | 更新 | 时间线调整 |

---

## 待确认

1. **sync-prices 并行拆分是否立即执行？** — 改造量最小（~30min），收益最明确
2. **verify 拆分的优先级？** — 是否是当前最紧迫的任务，还是排在翻译管道之后
3. **是否需要为 translate 申请多个 API key？** — 如果有预算，可注册 DeepSeek + OpenAI 各一个，实现 2 路并行翻译
