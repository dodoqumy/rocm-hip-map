# 内容更新策略：差异化增量爬取与变更检测

**创建时间：** 2026-04-29  
**状态：** 📋 待评审  
**依赖：** 无（独立功能）

---

## 目标

为项目所有内容源建立**差异化更新策略**，区分"一次抓取即可"（不可变）和"需要持续监控更新"（可变）两种内容类型，实现：

1. **不可变内容免重复抓取** — 论文、博客、存档类文章抓一次即标记完成
2. **可变内容高效增量更新** — 官方文档、Issue 等仅检测变更，有变化才重抓
3. **新资源智能发现** — 根据文章发布日期判断是否为新内容，增量而非全量

---

## 现状分析

### 当前抓取脚本与更新行为

| 脚本 | 内容类型 | 当前行为 | 问题 |
|------|----------|----------|------|
| `fetch-official.py` | AMD 官方文档 (68篇) | 静态 URL 列表，文件存在即 skip | ①无更新检测 ②无新页面发现 ③首次跑完后永远不会有新文章 |
| `fetch-papers.py` | arXiv 论文 | arXiv API 按关键词搜索 | 论文不可变 ✅ 但每次 sync 都重新搜索（浪费 API 配额） |
| `sync-github.py` | GitHub Issues/PR | 拉取 Issues 列表 | 需检测新评论/状态变更 |
| `fetch-asia.py` / `fetch-eu.py` | 多语言情报 | URL + search_terms 抓取 | 部分页面可能更新，部分是一次性存档 |

### 当前数据模型缺陷

`articles.json` 缺少更新策略元数据：
```json
{
  "file": "content/raw/english/xxx.md",
  "title": "...",
  "source_url": "...",
  "source_type": "official",
  // ❌ 缺少:
  // "content_hash": "abc123",        — 内容指纹，用于变更检测
  // "update_policy": "immutable",     — 更新策略
  // "last_checked": "2026-04-29",    — 最后检查时间
  // "last_modified_remote": "..."     — 远端最后修改时间（如有）
}
```

---

## 方案设计

### 1. 内容分类：不可变 vs 可变

```
┌─────────────────────────────────────────────────────────┐
│                    内容更新策略分类                        │
├──────────────┬──────────────────┬────────────────────────┤
│   不可变      │    准不可变       │      可变              │
│  (immutable) │  (semi-mutable)  │    (mutable)           │
├──────────────┼──────────────────┼────────────────────────┤
│ • arXiv 论文  │ • 博客文章       │ • AMD 官方文档         │
│ • 会议论文   │ • 新闻稿         │ • GitHub Issues/PR    │
│ • PDF 存档   │ • 培训材料       │ • Wiki 页面            │
│ • 已发表报告 │ • 版本发布说明   │ • 社区讨论             │
│              │                  │ • API 参考             │
├──────────────┼──────────────────┼────────────────────────┤
│ 策略：       │ 策略：           │ 策略：                 │
│ 抓一次即完成 │ 低频率检查       │ 每次 sync 都检查       │
│ 永不再抓     │ （周级别）       │ （日级别）             │
│              │ 对比发布日期     │ 对比内容 hash          │
└──────────────┴──────────────────┴────────────────────────┘
```

### 2. 数据模型扩展

在 `data/articles.json` 中为每篇文章增加 `sync_meta` 字段：

```json
{
  "file": "content/raw/english/rocm_en_latest_what-is-rocm.md",
  "source_url": "https://rocm.docs.amd.com/en/latest/what-is-rocm.html",
  "source_type": "official",
  "source_org": "amd",
  
  "sync_meta": {
    "update_policy": "mutable",           // immutable | semi-mutable | mutable
    "content_hash": "a1b2c3d4e5f6a7b8",  // SHA256 前 16 字符
    "last_fetched": "2026-04-29T08:00:00Z",
    "last_checked": "2026-04-29T08:00:00Z",
    "last_modified_remote": null,         // HTTP Last-Modified / ETag
    "check_interval_hours": 24,           // 检查间隔（可变=24h, 准不可变=168h, 不可变=-1）
    "status": "current"                   // current | stale | archived | error
  }
}
```

### 3. 各脚本改造

#### 3.1 `fetch-official.py`（核心改造）

**当前：** 遍历静态 `pages` 列表 → 文件存在则 `skip`  
**改造后：**

```
for each source_url in pages:
    article = find_in_index(source_url)
    
    if article.sync_meta.update_policy == "immutable":
        skip                    # 不可变，永不重抓
    
    if article.sync_meta.update_policy == "semi-mutable":
        if hours_since_last_check < 168:
            skip                # 准不可变，周内不重复检查
    
    # 可变：抓取 → 对比 hash
    html = fetch(url)
    new_hash = sha256(content)
    
    if new_hash == article.sync_meta.content_hash:
        update_last_checked()   # 无变更，仅更新时间戳
        continue
    
    # 有变更 → 重新保存
    save_markdown(html, url)
    update_sync_meta(hash=new_hash, status="updated")
```

**新增能力：** 对可变源读取 HTTP `Last-Modified` / `ETag` 头，免去完整下载（若浏览器支持 304 Not Modified）。

#### 3.2 `fetch-papers.py`（最小改造）

**当前：** 每次 sync 调用 arXiv API + 搜索  
**改造后：** 检测 `papers.json` 中最新论文日期，仅查询该日期以后的新论文：

```python
last_date = max(p.get("published", "2000-01-01") for p in existing_papers)
# arXiv API: search_query=cat:cs.DC+AND+submittedDate:[20260428+TO+*]
```

#### 3.3 `sync-github.py`

**改造：** 对比 Issue `updated_at` 时间戳，跳过未变更的 Issue。仅当有新评论或状态变更时重新拉取。

#### 3.4 `fetch-asia.py` / `fetch-eu.py`（多语言）

**改造：** 在 `config/sources.yaml` 中新增 `update_policy` 字段：

```yaml
- id: bsc
  name: "BSC — 巴塞罗那超算中心"
  update_policy: semi-mutable    # 超算文档偶尔更新
  check_interval_hours: 168
```

---

## 实施步骤

### Step 1: 扩展数据模型（~30min）

| 文件 | 改动 |
|------|------|
| `scripts/classify.py` | 为每篇文章生成初始 `sync_meta`，根据 `source_type` 推断默认 `update_policy` |
| `data/articles.json` | 回填已有文章的 `sync_meta`（一次性的迁移脚本） |

**默认 policy 映射：**
```
source_type = "paper"     → immutable,  check_interval = -1
source_type = "blog"      → semi-mutable, check_interval = 168
source_type = "official"  → mutable,      check_interval = 24
source_type = "issue"     → mutable,      check_interval = 24
source_type = "community" → mutable,      check_interval = 24
```

### Step 2: 改造 fetch-official.py（~1h）

| 改动 | 说明 |
|------|------|
| HTTP `HEAD` 请求获取 `Last-Modified` / `ETag` | 免下载检测变更 |
| `content_hash` 对比（SHA256 first 4KB） | 兜底变更检测 |
| `update_policy` 判断 | 根据不同 policy 决定是否跳过 |
| 移除静态 `pages` 列表依赖 `articles.json` 索引 | 改为从 index 读 URL 列表 |

### Step 3: 改造其余 fetch 脚本（~1.5h）

| 脚本 | 改动 |
|------|------|
| `fetch-papers.py` | 增量：从最新论文日期起查询 |
| `sync-github.py` | 增量：对比 `updated_at` |
| `fetch-asia.py` / `fetch-eu.py` | `config/sources.yaml` 加 `update_policy` |
| `cache-images.py` | 不变（图片缓存已独立） |

### Step 4: 新资源发现机制（~1h）

当前所有源都是**已知 URL 列表**——没有"发现新页面"的能力。需新增：

| 源类型 | 发现方式 |
|--------|----------|
| AMD docs | RSS feed (`https://rocm.docs.amd.com/en/latest/`) + sitemap |
| 博客 | RSS feed 已配置但未使用 (`SOURCES["amd-blog"]["rss"]`) |
| arXiv | API 增量查询 |
| 多语言 | `search_terms` → 搜索引擎 API（Google/Bing） |

**RSS 增量逻辑：**
```python
def fetch_rss_new(feed_url, last_check_date):
    items = parse_rss(feed_url)
    new_items = [i for i in items if i.pub_date > last_check_date]
    return new_items
```

### Step 5: 迁移与验证（~30min）

- 为已有 195 篇文章回填 `sync_meta`
- 干跑测试：`fetch-official.py --dry-run` 验证增量逻辑
- 单篇测试：选一篇官方文档，手动修改原文 → 验证重新抓取

---

## 文件变更清单

| 文件 | 操作 | 说明 |
|------|------|------|
| `scripts/classify.py` | 修改 | 生成初始 sync_meta |
| `scripts/fetch-official.py` | 重写 | HEAD 检测 + hash 对比 + policy |
| `scripts/fetch-papers.py` | 修改 | 增量 arXiv 查询 |
| `scripts/sync-github.py` | 修改 | updated_at 对比 |
| `scripts/fetch-asia.py` | 修改 | sources.yaml policy |
| `scripts/fetch-eu.py` | 修改 | sources.yaml policy |
| `config/sources.yaml` | 修改 | 每源加 update_policy |
| `data/articles.json` | 扩展 | 回填 sync_meta |
| `docs/cron-jobs.md` | 更新 | sync 流程说明 |

---

## 风险与待定问题

| 风险 | 缓解 |
|------|------|
| AMD docs 无 `Last-Modified` 头 | 降级到 content hash 对比（需完整下载） |
| `articles.json` schema 变更需向后兼容 | `sync_meta` 作为可选字段，缺省时走全量逻辑 |
| RSS feed 不包含所有页面 | RSS + sitemap 双通道 |
| 短时间内抓取频率过高触发限流 | 保持 1s sleep + HEAD 请求减少带宽 |

### 待确认

1. **准不可变（semi-mutable）是否需要？** — 博客、新闻稿等几乎不会修改已发布内容。可以直接归为 immutable，简化模型。
2. **全量校验频率？** — 即使有增量检测，是否仍需要每月一次全量 hash 校验（防止漏检）？
3. **`search_terms` 搜索引擎成本？** — Google/Bing API 有免费配额限制，需评估。

---

## 验证标准

- [ ] `fetch-official.py --dry-run` 对无变更文件输出 `⏭ skip (unchanged)` 而非 `⏭ skip (exists)`
- [ ] 修改一篇测试文件的存档内容后，`fetch-official.py` 检测到 hash 变化并重新抓取
- [ ] `fetch-papers.py` 仅查询 2026-04-28 以后的论文，不重复拉已有 87 篇
- [ ] 已有文章全部回填 `sync_meta`，无缺漏
- [ ] `npm run build` 通过
