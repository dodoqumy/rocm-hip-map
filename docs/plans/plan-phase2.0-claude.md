# 📋 Phase 2.0 开发计划：从玩具脚本到月访问 10 万的内容站

> **目标：** 把 `rocm-hip-map` 从硬编码 URL 清单升级到真正的多源采集 + 分类 + SEO 内容站
> **周期：** 17 个工作日（约 4 周）
> **预期产出：** 内容池从 ~70 篇 → 7000+ 篇，月 PV 目标 10 万
> **创建日期：** 2026-05-01

---

## 📑 目录

- [一、现状诊断](#一现状诊断)
- [二、目标架构](#二目标架构)
- [三、Phase 2.0 任务清单](#三phase-2-任务清单)
  - [Phase 2.0.0 数据库化](#phase-20-数据库化2-天)
  - [Phase 2.0.1 爬虫架构重写](#phase-21-爬虫架构重写4-天)
  - [Phase 2.0.2 调度器](#phase-22-调度器2-天)
  - [Phase 2.0.3 智能分类](#phase-23-智能分类3-天)
  - [Phase 2.0.4 内容质量评分](#phase-24-内容质量评分2-天)
  - [Phase 2.0.5 SEO 与发布层](#phase-25-seo-与发布层3-天)
  - [Phase 2.0.6 监控与可观测](#phase-26-监控与可观测1-天)
- [四、时间表](#四时间表)
- [五、最小可用路径（MVP）](#五最小可用路径mvp)
- [六、KPI 与验收标准](#六kpi-与验收标准)

---

## 一、现状诊断

### 1.1 现有工作流的根本问题

| 模块 | 现状 | 问题 |
|---|---|---|
| `fetch-official.py` | 硬编码 68 个 URL | 不是爬虫，是 wget 列表；新页面永不发现 |
| `sync-github.py` | per_page=20，无认证 | 速率 60/h，4 个 repo 即用尽；issue 实际抓到 0 条 |
| `classify.py` | 30 条简单正则 | 没有 gfx target、Wave32/64、CK、aotriton 等关键词 |
| 论文 | `fetch-papers.py` 标 ✅ 但未运行 | 实际 0 篇 |
| 第三方一手内容 | 完全没接 | Phoronix、Reddit、HN、知乎全空白 |
| 存储 | 文件 + JSON | 1 万篇后会爆 |
| 去重 | 仅文件名比对 | 同一文章不同 URL 重复 |
| 增量 | 无 ETag/Last-Modified | 每次全量重抓 |
| 调度 | GitHub Actions 串行 | 无法扩展 |
| 失败重试 | 无 | 网络波动 = 数据缺失 |

### 1.2 为什么日志显示"几乎为空"

```
Total articles: 0 fetched      ← 68 篇全已存在，新一次跑零产出
Total issues synced: 0         ← per_page=20 + bug 标签筛选 = 全过滤掉
68 files scanned, 68 classified ← 但每篇平均仅 0-1 个 GPU 标签
```

**这不是 bug，是设计天花板。** 必须重构架构才能突破。

---

## 二、目标架构

### 2.1 分层视图

```
┌─────────────────────────────────────────────────────────────┐
│  L1 SOURCES         L2 CRAWL          L3 STORE       L4 SERVE│
├─────────────────────────────────────────────────────────────┤
│  AMD 官方文档    ──┐                                          │
│  AMD ROCm Blog   ──┤                  ┌─ raw/ (md+html)        │
│  GitHub Issues   ──┤                  │                       │
│  arXiv 论文      ──┼─→ 调度器(Prefect)─├─ SQLite (主索引) ──→ 站点│
│  Reddit          ──┤      ↓            ├─ DuckDB (分析查询)    │
│  Hacker News     ──┤   Worker 池        └─ Meilisearch (搜索) │
│  Phoronix        ──┤   (并发+去重                              │
│  知乎/B站        ──┤    +重试+ETag)    ↑                      │
│  YouTube 转录    ──┘                增量 + sitemap + RSS      │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 数据流

```
discover() → URL 候选 → 去重 → fetch() → ETag 304 跳过 / 200 入库
                                  ↓
                              parse() → trafilatura 提正文
                                  ↓
                              classify() → 规则 + LLM 双层
                                  ↓
                              quality_score() → 阈值过滤
                                  ↓
                              translate() → 中文版
                                  ↓
                              publish() → 站点 + sitemap + RSS
```

---

## 三、Phase 2.0 任务清单

### Phase 2.0.0 数据库化（2 天）

**目标：** 用 SQLite 替代 articles.json，为后续所有功能打基础。

#### 2.0.1 建立 schema

- [ ] **2.0.1.1** 创建 `db/schema.sql`，定义 6 张核心表
  - `sources` — 数据源注册表
  - `articles` — 文章主表（含 url_hash、content_hash、ETag、status）
  - `tags` — 标签命名空间（gpu/arch/os/framework/topic）
  - `article_tags` — 多对多关联（含 confidence）
  - `crawl_log` — 每次爬取记录（用于诊断）
  - `versions` — ROCm/HIP 版本追踪（替代 versions.json）
- [ ] **2.0.1.2** 创建关键索引
  - `idx_articles_status`、`idx_articles_quality`、`idx_articles_published`
  - `idx_articles_url_hash`（去重用）
  - `idx_articles_content_hash`（变更检测用）
- [ ] **2.0.1.3** 写 `scripts/db/migrate.py` — 一次性迁移
  - 把 68 篇官方文档从文件解析入库
  - 把 `data/articles.json` 元数据合并
  - 把 `data/versions.json` 入 versions 表
  - 把 `data/known-issues.json` 入 articles 表（source_type=github-issue）

#### 2.0.2 数据访问层

- [ ] **2.0.2.1** 写 `db/dao.py` — 封装常用查询
  - `Article.upsert(url, content_hash, ...)` — 智能 upsert
  - `Article.find_stale(days)` — 找需要重抓的
  - `Source.due_for_crawl()` — 返回该跑的 source
- [ ] **2.0.2.2** 写 `db/__init__.py` — 连接池 + WAL 模式

#### 2.0.3 兼容旧脚本

- [ ] **2.0.3.1** 让 `classify.py` 既能写 JSON 也能写 DB（过渡期）
- [ ] **2.0.3.2** 加 `db/export.py` — 导出 articles.json（保持 sidebar 生成兼容）

**验收：**
- ✅ `sqlite3 data/rocm-hip-map.db ".tables"` 显示 6 张表
- ✅ 68 篇文章全部入库且 url_hash 去重正确
- ✅ 现有站点构建不破坏

---

### Phase 2.0.1 爬虫架构重写（4 天）

**目标：** 从"URL 清单"升级到真正的多源爬虫框架。

#### 2.1.1 基础框架（1 天）

- [ ] **2.1.1.1** 写 `crawlers/base.py` — `BaseCrawler` 抽象类
  ```python
  class BaseCrawler(ABC):
      source_slug: str
      rate_limit: float = 1.0    # req/sec
      def discover(self) -> Iterator[str]: ...
      def fetch(self, url) -> RawDoc: ...
      def parse(self, raw) -> Article: ...
      def run(self): ...   # 模板方法
  ```
- [ ] **2.1.1.2** 写 `crawlers/http_client.py`
  - 用 `httpx.AsyncClient` 替代 subprocess curl
  - 支持 HTTP/2、连接池
  - 集成 ETag/Last-Modified 缓存
  - 失败重试（指数退避，最多 3 次）
- [ ] **2.1.1.3** 写 `crawlers/extractor.py`
  - `trafilatura` 提取正文（去导航/广告）
  - `selectolax` 做 HTML 解析（比 pandoc 快 50 倍）
  - `readability-lxml` 兜底
- [ ] **2.1.1.4** 写 `crawlers/dedup.py`
  - URL 规范化（去 utm_*、fbclid 等参数）
  - URL hash + 内容 hash 双重去重

#### 2.1.2 官方源 Crawler（1 天）

- [ ] **2.1.2.1** `RocmDocsCrawler`
  - 从 `https://rocm.docs.amd.com/sitemap.xml` 发现所有页面
  - 处理多个子项目 sitemap（HIP、HIPIFY、install-on-linux 等）
  - 预期：1500+ 页（vs 现在 68 页）
- [ ] **2.1.2.2** `RocmBlogCrawler`
  - RSS：`https://rocm.blogs.amd.com/feed.xml`
  - 归档页扫描（按月份倒序）
  - 预期：200+ 篇
- [ ] **2.1.2.3** `PytorchDocsCrawler`
  - PyTorch 官方文档 ROCm 相关页
  - GitHub Releases notes（每个版本）
- [ ] **2.1.2.4** `TheRockCrawler`
  - ROCm/TheRock 仓库 README、docs/
  - 重要：这是 2026 新硬件适配的关键入口

#### 2.1.3 GitHub Crawler（1 天）

- [ ] **2.1.3.1** `GithubCrawler` — 用 GraphQL API
  - 必须配置 `GITHUB_TOKEN`（速率 5000/h vs 60/h）
  - 监控仓库列表：
    ```
    ROCm/ROCm, ROCm/HIP, ROCm/HIPIFY, ROCm/composable_kernel,
    ROCm/aotriton, ROCm/flash-attention, ROCm/TheRock,
    ROCm/pytorch, pytorch/pytorch (label:module:rocm),
    triton-lang/triton (label:amd), vllm-project/vllm (label:rocm)
    ```
  - 抓取：Issues + PR + Discussions + Releases
  - 增量：用 `since` 参数（last_crawled_at）
- [ ] **2.1.3.2** Issue 标签智能识别
  - 处理标签命名差异（`bug` vs `Bug` vs `type:bug` vs `kind/bug`）
  - 提取 issue 中的 ROCm 版本、GPU 型号、错误日志
- [ ] **2.1.3.3** PR 关联
  - PR-Issue 关联（fixes/closes 关键词）
  - 合并状态追踪（哪些 issue 已被解决）

#### 2.1.4 第三方源 Crawler（1 天）

- [ ] **2.1.4.1** `ArxivCrawler`
  - arXiv API：分类 cs.DC + cs.LG
  - 关键词：ROCm, HIP, AMD GPU, MI300, RDNA, CDNA
  - PDF 下载 + 用现有 `extract-pdf.py`
- [ ] **2.1.4.2** `PhoronixCrawler`
  - tag/AMD-ROCm RSS：`https://www.phoronix.com/rss-tag/AMD-ROCm`
  - 处理反爬：User-Agent 轮换 + 1.5s 间隔
  - 价值：Phoronix 是 ROCm 第三方测评最权威源
- [ ] **2.1.4.3** `RedditCrawler`
  - subreddit：r/LocalLLaMA, r/ROCm, r/Amd, r/StableDiffusion
  - 用 `.json` API（公开，无需 OAuth）
  - 筛选：score >= 10 OR comments >= 20
- [ ] **2.1.4.4** `HnCrawler`
  - Algolia HN API：`https://hn.algolia.com/api/v1/search`
  - 关键词：ROCm, HIP, MI300, AMD GPU
- [ ] **2.1.4.5** `ZhihuCrawler`（中文主力）
  - 知乎搜索 API + 专栏抓取
  - 关键词：ROCm, AMD 显卡, MI300, 计算卡
  - **要点：** 必须用代理池

**验收：**
- ✅ 8 个 crawler 各跑一次成功
- ✅ articles 表新增 ≥ 5000 条
- ✅ 重跑一次只增量（已存在的 304 跳过）
- ✅ crawl_log 表完整记录

---

### Phase 2.0.2 调度器（2 天）

**目标：** 替换 GitHub Actions 串行模式，支持并发 + 失败重试 + 优先级。

#### 2.2.1 选型决策

- [ ] **2.2.1.1** 评估三种方案，写决策文档
  | 方案 | 优 | 劣 |
  |---|---|---|
  | Prefect Cloud Free | 5 万 task/月免费、UI 好 | 锁定 |
  | APScheduler 自托管 | 完全自主 | T5820 必须常开 |
  | Cloudflare Workers Cron | 免费额度大 | 不适合长任务 |
- [ ] **2.2.1.2** 推荐 **Prefect Cloud** 起步（最快上线）

#### 2.2.2 Prefect Flow 实现

- [ ] **2.2.2.1** `flows/crawl_flow.py`
  - 主 flow：拉取 `sources.due_for_crawl()` → 分发 worker
  - 子 flow：每个 source 一个，独立失败隔离
- [ ] **2.2.2.2** 定义优先级队列
  ```yaml
  rocm-docs:        { interval: 6h,  priority: high }
  rocm-blog:        { interval: 1h,  priority: high }
  github-rocm:      { interval: 30m, priority: critical }
  arxiv-amd:        { interval: 12h, priority: medium }
  reddit-localllama:{ interval: 15m, priority: high }
  phoronix:         { interval: 2h,  priority: medium }
  hn:               { interval: 30m, priority: medium }
  zhihu:            { interval: 6h,  priority: low }
  ```
- [ ] **2.2.2.3** 失败处理
  - 单 source 失败 3 次 → 自动 disable 24h
  - 写入 `crawl_log.status = 'circuit_broken'`
  - 通过 Prefect 通知（Discord/Slack webhook）

#### 2.2.3 与现有 GitHub Actions 共存

- [ ] **2.2.3.1** 旧的 `sync.yml`、`papers.yml` 保留作为 fallback
- [ ] **2.2.3.2** 新 flow 跑通 1 周后再下线 cron yaml
- [ ] **2.2.3.3** 写 `docs/scheduler-migration.md` 迁移记录

**验收：**
- ✅ Prefect Cloud 仪表盘看到 8 个 source 自动跑
- ✅ 一个 source 故意制造失败，circuit breaker 生效
- ✅ 全链路失败有通知

---

### Phase 2.0.3 智能分类（3 天）

**目标：** 标签覆盖率从现在的 0-3 个/篇提升到 8-15 个/篇，准确度 >90%。

#### 2.3.1 规则增强（1 天）

- [ ] **2.3.1.1** `classify/rules.py` — 扩展到 ~300 条规则
- [ ] **2.3.1.2** 关键扩充类别：
  - **gpu_target（LLVM target）** — ROCm 世界最关键的标识
    ```
    gfx1201 (RX 9070 XT/GRE)
    gfx1200 (RX 9060 XT)
    gfx1151 (Strix Halo)
    gfx1103 (Phoenix APU)
    gfx1100 (RX 7900 XTX/XT, W7900)
    gfx1101 (RX 7800 XT)
    gfx1102 (RX 7700 XT)
    gfx950  (RDNA 4 中新增)
    gfx942  (MI300A)
    gfx940  (MI300X)
    gfx90a  (MI200/MI250X)
    gfx908  (MI100)
    ```
  - **架构层级**
    ```
    rdna4, rdna3, rdna2, rdna1
    cdna4, cdna3, cdna2, cdna1
    wave32, wave64
    matrix-cores, wmma
    ```
  - **库与工具链**
    ```
    aotriton, hipblaslt, composable-kernel, miopen,
    rccl, rocblas, rocsolver, rocfft, rocsparse,
    hipblas, hipsparse, hipfft, hipsolver,
    rocprofiler, rocgdb, hipify-clang, hipify-perl,
    omniperf, omnitrace
    ```
  - **AI 框架与运行时**
    ```
    pytorch-rocm, tensorflow-rocm, jax-rocm, onnx-rocm,
    vllm-rocm, ollama-rocm, llama-cpp-rocm,
    flash-attention-ck, flash-attention-triton,
    triton-amd, sglang-rocm
    ```
  - **常见痛点模式**
    ```
    wave32-incompat: r"wave32.*not.*support"
    pcie-atomics-required: r"PCIe.*atomic"
    iommu-pt-required: r"iommu=pt"
    fa-rdna-fail: r"flash.*attention.*RDNA.*fail"
    hsa-override: r"HSA_OVERRIDE_GFX_VERSION"
    ```
- [ ] **2.3.1.3** 单元测试：每条规则至少 1 个正样本 + 1 个负样本

#### 2.3.2 LLM 分类（1.5 天）

- [ ] **2.3.2.1** `classify/llm.py` — 用 Claude/DeepSeek 兜底
  - 触发条件：规则匹配 < 3 个标签，OR quality_score > 0.6
  - prompt 模板见附录 A
  - 输出严格 JSON，schema 校验
- [ ] **2.3.2.2** 成本控制
  - 每天处理量 ≤ 200 篇
  - 优先处理新文章（discovered_at 近 7 天）
  - 用 DeepSeek 做大部分（成本低 10x），Claude 做精筛
- [ ] **2.3.2.3** 缓存
  - 同一 content_hash 不重复调 LLM
  - 缓存写入 `tags_cache` 表

#### 2.3.3 难度分类升级（0.5 天）

- [ ] **2.3.3.1** 替换字数判断为更聪明的启发
  - 代码块密度（高 → advanced）
  - 引用 paper / 学术词汇 → research
  - tutorial/getting started 关键词 → beginner
  - 含 benchmark 数据 → intermediate
- [ ] **2.3.3.2** 受众标签
  ```
  audience: [user|developer|researcher|sysadmin]
  ```

**验收：**
- ✅ 现有 68 篇平均标签数从 ~1.5 升到 ~10
- ✅ 抽样 30 篇人工核验，准确率 ≥ 90%
- ✅ LLM 分类日成本 < $1

---

### Phase 2.0.4 内容质量评分（2 天）

**目标：** 自动过滤低质内容，主索引只收 quality_score ≥ 0.3 的。

#### 2.4.1 评分函数

- [ ] **2.4.1.1** `quality/score.py` — 多因子打分
  ```python
  def quality_score(article):
      s = 0.5  # 基线
      s += 0.2 if article.source.credibility >= 4 else 0
      s += min(article.word_count / 3000, 1) * 0.1
      s += 0.1 if has_code_block(article.body) else 0
      s += 0.1 if has_benchmark_data(article.body) else 0
      s -= 0.2 if is_listicle(article.title) else 0
      s -= 0.3 if is_press_release(article.body) else 0
      s += github_stars_factor(article)
      s += freshness_decay(article.published_at)
      return clamp(s, 0, 1)
  ```
- [ ] **2.4.1.2** 各子函数实现
  - `has_code_block`：detect ``` 或 `<pre><code>` 块
  - `has_benchmark_data`：检测 tok/s, ms, GB/s, % 等单位 + 表格
  - `is_listicle`：标题正则 `^(Top|Best|N+)\s+\d+`
  - `is_press_release`：检测 PR 模板词（"announces", "is excited to"）
  - `github_stars_factor`：仓库 stars > 1000 +0.1
  - `freshness_decay`：1 - days_since_published / 730

#### 2.4.2 主索引筛选

- [ ] **2.4.2.1** 加 `articles.is_indexed` 字段
  - quality_score >= 0.3 → is_indexed = 1
  - 否则只存档，不进侧边栏、不生成 sitemap、不翻译
- [ ] **2.4.2.2** 网站过滤逻辑
  - 文章列表页只显示 is_indexed = 1
  - 但搜索仍能搜到全部（Meilisearch 收全集）

#### 2.4.3 人工干预

- [ ] **2.4.3.1** 加 `articles.manual_override` 字段
  - 允许手动 promote 或 demote 文章
  - admin 工具：`scripts/curate.py --promote <id>`

**验收：**
- ✅ 7000 篇内容池筛出 ≥ 1500 篇主索引内容
- ✅ 抽样人工核验：高分文章质量主观评分 ≥ 7/10

---

### Phase 2.0.5 SEO 与发布层（3 天）

**目标：** 这是冲 10 万月 PV 的关键。前面所有工作都为这一层服务。

#### 2.5.1 站点结构（0.5 天）

- [ ] **2.5.1.1** 设计 SEO 友好的 URL 结构
  ```
  /                              首页：今日新增 + 热门
  /gpu/{gfx_target}/             gfx1100、gfx942 落地页（高搜索量）
  /topic/{slug}/                 flash-attention-rocm、wave32 等
  /article/{year}/{slug}/        文章页
  /cuda-hip-map/                 304 条 API 映射（已有，强化）
  /compatibility/                兼容矩阵（独立工具页）
  /issues/{repo}/{number}/       GitHub Issue 镜像页
  /papers/{arxiv_id}/            论文页
  /zh/...                        中文版独立路径
  ```
- [ ] **2.5.1.2** 在 Docusaurus 中配置路由
- [ ] **2.5.1.3** 301 重定向（旧路径 → 新路径）

#### 2.5.2 结构化数据（0.5 天）

- [ ] **2.5.2.1** JSON-LD 注入
  - Article schema（title、author、datePublished、image）
  - BreadcrumbList schema
  - FAQPage schema（issue 镜像页特别有效）
- [ ] **2.5.2.2** Open Graph + Twitter Card meta
- [ ] **2.5.2.3** 用 Google Rich Results Test 验证 5 类页面

#### 2.5.3 sitemap + RSS（0.5 天）

- [ ] **2.5.3.1** 自动生成 sitemap.xml
  - 主 sitemap → 索引文件
  - 分片：每 5 万 URL 一个子 sitemap
  - 包含 lastmod、priority、changefreq
- [ ] **2.5.3.2** 生成 RSS / Atom feed
  - `/rss/all.xml`、`/rss/gpu/{gfx}.xml`、`/rss/topic/{slug}.xml`
  - 中文版独立 feed
- [ ] **2.5.3.3** robots.txt 优化

#### 2.5.4 双语 SEO（0.5 天）

- [ ] **2.5.4.1** hreflang tag 双向声明
  ```html
  <link rel="alternate" hreflang="en" href="...">
  <link rel="alternate" hreflang="zh" href="/zh/...">
  <link rel="alternate" hreflang="x-default" href="...">
  ```
- [ ] **2.5.4.2** canonical URL 处理（避免英中重复内容惩罚）
- [ ] **2.5.4.3** 中文 sitemap 单独提交到百度站长

#### 2.5.5 SEO 落地页 10 篇（1 天）

> **这 10 篇决定了能否冲到月 10 万 PV。每篇都针对一个高搜索量长尾词。**

- [ ] **2.5.5.1** `/gpu/rx-7900-xtx-rocm-guide/`
  - 关键词：`RX 7900 XTX ROCm`、`7900 XTX flash attention`
  - 内容：完整安装、性能、踩坑、benchmarks
- [ ] **2.5.5.2** `/gpu/rx-9070-xt-rocm-guide/`
  - 关键词：`RX 9070 XT AI`、`gfx1201 PyTorch`
- [ ] **2.5.5.3** `/gpu/strix-halo-rocm-guide/`
  - 关键词：`Strix Halo ROCm`、`gfx1151 LLM`
- [ ] **2.5.5.4** `/gpu/mi300x-vllm-benchmark/`
  - 关键词：`MI300X vLLM`、`MI300X Llama benchmark`
- [ ] **2.5.5.5** `/topic/flash-attention-rocm-rdna/`
  - 关键词：`flash attention RDNA`、`Wave32 flash attention`
- [ ] **2.5.5.6** `/topic/rocm-vs-cuda-2026/`
  - 关键词：`ROCm vs CUDA`、`AMD vs NVIDIA AI`
- [ ] **2.5.5.7** `/topic/rocm-install-ubuntu-2404/`
  - 关键词：`ROCm install Ubuntu 24.04`
- [ ] **2.5.5.8** `/topic/rocm-windows-wsl2-guide/`
  - 关键词：`ROCm WSL2`、`AMD GPU PyTorch Windows`
- [ ] **2.5.5.9** `/topic/cuda-to-hip-porting-guide/`
  - 关键词：`CUDA to HIP`、`hipify tutorial`
- [ ] **2.5.5.10** `/topic/local-llm-amd-gpu-2026/`
  - 关键词：`local LLM AMD`、`Ollama AMD GPU`

每篇要求：
- 中英双语
- ≥ 2000 字
- 含 benchmarks 表格
- 含截图/示意图
- 含 FAQ section（喂给 FAQPage schema）
- 内链 ≥ 5 个

#### 2.5.6 性能与提交

- [ ] **2.5.6.1** Cloudflare CDN + Brotli + 图片 WebP
- [ ] **2.5.6.2** 验证 Lighthouse 分数 ≥ 90
- [ ] **2.5.6.3** Google Search Console + Bing Webmaster + 百度站长
  - 提交 sitemap
  - 监控 Coverage 报告
- [ ] **2.5.6.4** 内链算法升级
  - `related-articles.py` 用 embedding 相似度（替代关键词匹配）
  - 每篇文章末尾自动 5 个相关推荐

**验收：**
- ✅ 10 篇 SEO 落地页全部上线
- ✅ Google Search Console 显示已索引 ≥ 1000 页
- ✅ Lighthouse SEO 分数 100
- ✅ Rich Results Test 全部通过

---

### Phase 2.0.6 监控与可观测（1 天）

**目标：** 全链路可见，问题秒级发现。

#### 2.6.1 指标

- [ ] **2.6.1.1** Prometheus 指标导出（`/metrics` 端点）
  - `crawl_total{source, status}` — 抓取计数
  - `crawl_duration_seconds{source}` — 耗时
  - `articles_total{status}` — 文章状态分布
  - `translate_queue_size` — 翻译队列
  - `llm_classify_cost_usd` — LLM 成本
- [ ] **2.6.1.2** Grafana Cloud 免费层
  - 仪表盘：8 个 source 的成功率、抓取量、延迟
  - 仪表盘：文章漏斗（discovered → fetched → classified → translated → published）

#### 2.6.2 错误追踪

- [ ] **2.6.2.1** Sentry 接入
  - 免费层 5K events/月够用
  - 关键操作（fetch、parse、classify）包 try-except 上报
- [ ] **2.6.2.2** 日志结构化
  - 用 `structlog` 替代 print
  - 输出 JSON 到 stdout，便于聚合

#### 2.6.3 站点分析

- [ ] **2.6.3.1** Plausible 或 Umami（隐私友好，GDPR 合规）
  - 不用 GA（中国访问问题 + 隐私）
- [ ] **2.6.3.2** 关键事件埋点
  - 翻译切换、术语 tooltip 点击、API 映射查询、价格图查看

**验收：**
- ✅ Grafana 仪表盘可看到全部 8 个 source 状态
- ✅ Sentry 收到至少 1 个测试错误
- ✅ Plausible 实时统计在线

---

## 四、时间表

| 周 | Phase | 任务 | 验收 |
|---|---|---|---|
| **W1 D1-2** | 2.0 | DB 化迁移 | 68 篇全部进 SQLite，6 张表建好 |
| **W1 D3-5** | 2.1a | base + 4 个官方 crawler | 抓 1700+ 官方页 |
| **W2 D1-2** | 2.1b | GitHub + 4 个第三方 crawler | 抓 5000+ 文章 |
| **W2 D3-4** | 2.2 | Prefect 调度 | 8 source 自动跑 |
| **W2 D5** | 2.3a | 规则分类增强 | 标签覆盖率 ≥ 90% |
| **W3 D1-2** | 2.3b | LLM 分类 | 每天 100-200 篇 |
| **W3 D3** | 2.4 | quality_score | 主索引筛过 |
| **W3 D4-5** | 2.5a | sitemap + JSON-LD + hreflang | GSC 提交 |
| **W4 D1-2** | 2.5b | 10 篇 SEO 落地页 | 排名监控启动 |
| **W4 D3** | 2.6 | 监控仪表盘 | 全链路可见 |
| **W4 D4-5** | buffer | bug 修复 + 文档 | 发布 v0.2 |

**总计：** 17 个工作日（约 4 周）

---

## 五、最小可用路径（MVP）

> **如果时间紧，前 6 天就能解决你现在所有痛点。**

| 优先级 | 任务 | 天数 | 影响 |
|---|---|---|---|
| 🔴 P0 | DB 化 + RocmDocsCrawler 用 sitemap 重写 | 3 | 立刻从 68 篇 → 1500+ |
| 🔴 P0 | GithubCrawler 用 GraphQL + token | 1 | issue 从 0 → 5000+ |
| 🔴 P0 | 加 Phoronix + Reddit + arXiv 三个 crawler | 2 | 真正有"情报站"的样子 |

完成 P0 后内容池 ~7000 篇，剩余任务可按节奏推进。

---

## 六、KPI 与验收标准

### 6.1 内容指标

| 指标 | 当前 | Phase 2.0 完成后 | 月 10 万 PV 目标 |
|---|---|---|---|
| 总文章数 | 68 | 7000+ | 15000+ |
| 主索引文章 | 68 | 1500+ | 5000+ |
| 中文翻译完成 | ~10% | 50%+ | 80%+ |
| 论文数 | 0（标 ✅ 但实际 0） | 200+ | 500+ |
| GitHub Issue 镜像 | 0 | 5000+ | 10000+ |

### 6.2 技术指标

| 指标 | 目标 |
|---|---|
| 单 source 抓取成功率 | ≥ 95% |
| 增量抓取效率 | ETag 304 占比 ≥ 70% |
| LLM 分类准确率 | ≥ 90%（人工抽样） |
| Lighthouse SEO 分 | 100 |
| Lighthouse 性能分 | ≥ 90 |
| LCP（页面最大内容渲染） | < 2s |

### 6.3 SEO 指标（90 天监控）

| 指标 | 30 天 | 60 天 | 90 天 |
|---|---|---|---|
| Google 已索引页数 | 1000+ | 3000+ | 8000+ |
| 月 PV | 5000 | 30000 | 100000 |
| 月独立访客 | 2000 | 10000 | 30000 |
| 平均会话时长 | ≥ 1min | ≥ 1.5min | ≥ 2min |
| 反链域名数 | 5 | 20 | 50 |

### 6.4 流量来源拆解（10 万 PV 目标）

```
长尾搜索        60% (60K) — gfx1100 flash attention 等
直接访问/书签    15% (15K)
Reddit/HN/Twitter 15% (15K)
中文搜索引擎     10% (10K) — 百度/必应中文
```

---

## 附录 A：LLM 分类 prompt 模板

```
你是 ROCm/HIP 技术分类专家。分析下面这篇文章，输出严格的 JSON。

文章标题：{title}
文章正文：{body_truncated_to_4000_chars}

请输出 JSON，schema 如下：
{
  "primary_topic": "..." (单选: install|tutorial|benchmark|troubleshooting|news|paper|api-reference|comparison|review),
  "gpus_mentioned": [...] (具体型号，如 ["RX 7900 XTX", "MI300X"]),
  "gfx_targets": [...] (LLVM target，如 ["gfx1100", "gfx942"]),
  "rocm_versions": [...] (如 ["6.4.0", "7.2.1"]),
  "frameworks": [...] (如 ["pytorch", "vllm", "ollama"]),
  "is_workaround_post": bool,
  "is_benchmark": bool,
  "is_news_post": bool,
  "actionable_for_users_with": [...] (能直接帮到哪些卡的用户),
  "key_takeaway": "..." (一句话核心要点，中文),
  "summary_zh": "..." (3-5 句中文摘要),
  "audience": "..." (user|developer|researcher|sysadmin),
  "estimated_quality": float (0-1，你对文章质量的主观评估)
}

只输出 JSON，不要任何其他文字。
```

---

## 附录 B：项目结构（Phase 2.0 完成后）

```
rocm-hip-map/
├── crawlers/                    # 🆕 新爬虫框架
│   ├── base.py
│   ├── http_client.py
│   ├── extractor.py
│   ├── dedup.py
│   ├── rocm_docs.py
│   ├── rocm_blog.py
│   ├── github.py
│   ├── arxiv.py
│   ├── phoronix.py
│   ├── reddit.py
│   ├── hn.py
│   └── zhihu.py
├── classify/                    # 🆕 分类模块
│   ├── rules.py
│   ├── llm.py
│   └── difficulty.py
├── quality/                     # 🆕 质量评分
│   └── score.py
├── db/                          # 🆕 数据库层
│   ├── schema.sql
│   ├── dao.py
│   └── migrate.py
├── flows/                       # 🆕 Prefect flows
│   ├── crawl_flow.py
│   └── publish_flow.py
├── scripts/                     # 旧脚本（兼容期保留）
│   ├── fetch-official.py        # ⚠️ deprecated
│   ├── sync-github.py           # ⚠️ deprecated
│   ├── classify.py              # ⚠️ deprecated
│   ├── translate.py             # 保留
│   ├── extract-pdf.py           # 保留
│   └── generate-docs.py         # 保留
├── content/
│   └── raw/                     # 原始文件（仍保留）
├── data/
│   └── rocm-hip-map.db          # 🆕 主数据库
├── docs/
│   ├── PROGRESS.md
│   ├── PHASE-2-PLAN.md          # 🆕 本文件
│   └── ...
└── docusaurus/                  # 站点
```

---

## 附录 C：依赖清单（新增）

```
# Python
httpx[http2]>=0.27
selectolax>=0.3.21
trafilatura>=1.12
readability-lxml>=0.8
prefect>=3.0
sqlalchemy>=2.0
structlog>=24.1
sentry-sdk>=2.0
prometheus-client>=0.20
pydantic>=2.0

# 可选
openai>=1.0          # 走 DeepSeek 兼容接口
anthropic>=0.40      # Claude API
```

---

> **更新规则：** 每完成一个 checkbox 立即勾选并 commit。
> **PROGRESS.md 同步：** 每个 Phase 2.0.X 完成后在主 PROGRESS.md 加一行总结。