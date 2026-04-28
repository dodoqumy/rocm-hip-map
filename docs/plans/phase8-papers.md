# Phase 8: ROCm/HIP 技术论文搜集与翻译模块

> 创建日期：2026-04-28 | 状态：📋 计划阶段

---

## 一、调研结论

### 已有论文证据（arXiv 搜索验证）

搜索 `ROCm HIP AMD GPU` 已命中多篇 2024-2026 论文：

| 论文 | arXiv ID | 主题 |
|------|----------|------|
| HipKittens: Fast and Furious AMD Kernels | 2511.08083 | AMD GPU 高性能 kernel 编程 |
| CASS: Nvidia to AMD Transpilation | 2505.16968 | CUDA→HIP 自动迁移 |
| GROMACS on AMD GPU Using SYCL | 2405.01420 | HPC 应用 ROCm 适配 |
| Tracing GPU Stall Root Causes | 2604.20032 | 跨厂商 GPU 调试 |
| Flash Attention on ONNX Runtime (HIP) | 2603.12646 | HIP kernel + ONNX |

→ **论文源充足，值得建模块。**

---

## 二、架构设计

```
                    ┌──────────────────────┐
                    │  fetch-papers.py     │  ← 新增
                    │  每周运行（arXiv API）│
                    └─────────┬────────────┘
                              │
                    ┌─────────▼────────────┐
                    │  data/papers.json    │  ← 新增
                    │  { id, title, abs,  │
                    │    authors, arxiv_id,│
                    │    pdf_url, tags... } │
                    └─────────┬────────────┘
                              │
              ┌───────────────┼───────────────┐
              │                               │
    ┌─────────▼──────────┐      ┌────────────▼──────────┐
    │ extract-pdf.py     │      │ translate-paper.py    │
    │ PDF → Markdown     │      │ 摘要 + 结论 优先翻译  │
    │ (pymupdf/pdftotext)│      │ (专用 prompt)         │
    └─────────┬──────────┘      └────────────┬──────────┘
              │                               │
    ┌─────────▼──────────┐      ┌────────────▼──────────┐
    │ content/raw/paper/ │      │ content/translated/   │
    │ papers/arxiv_*.md  │      │ zh/papers/arxiv_*.md  │
    └─────────┬──────────┘      └────────────┬──────────┘
              │                               │
              └───────────────┬───────────────┘
                              │
                    ┌─────────▼────────────┐
                    │ generate-docs.py     │  ← 复用
                    │ (source_type=paper)  │
                    └─────────┬────────────┘
                              │
                    ┌─────────▼────────────┐
                    │ website/docs/papers/ │
                    │ 📜 论文分类页        │
                    └──────────────────────┘
```

---

## 三、arXiv API 对接方案

### 端点

```
http://export.arxiv.org/api/query?search_query=ALL:ROCm+AND+ALL:GPU&start=0&max_results=50&sortBy=submittedDate&sortOrder=descending
```

### 搜索策略（6 组定期查询）

```python
QUERIES = [
    # 直接相关
    'all:ROCm AND all:GPU',                          # ROCm + GPU
    'all:HIP AND all:AMD AND all:GPU',               # HIP 编程
    'all:AMD AND all:Instinct AND all:GPU',           # MI 系列
    'all:CDNA OR all:RDNA AND all:GPU',               # 架构
    # 间接相关
    'all:CUDA AND all:portability AND all:AMD',       # CUDA 迁移
    'all:AMD AND all:GPU AND all:LLM',                # LLM on AMD
]
```

### 去重策略

按 `arxiv_id` 去重，已收录的论文不会重复下载。

### 速率限制

arXiv API 要求礼貌使用：请求间隔 ≥ 3 秒，每次 ≤ 50 条。

---

## 四、论文元数据模型

```json
{
  "id": "2511.08083",
  "title": "HipKittens: Fast and Furious AMD Kernels",
  "authors": ["Author1", "Author2"],
  "abstract": "...",
  "arxiv_id": "2511.08083v1",
  "arxiv_url": "https://arxiv.org/abs/2511.08083",
  "pdf_url": "https://arxiv.org/pdf/2511.08083",
  "published": "2025-11-12",
  "updated": "2026-01-15",
  "categories": ["cs.DC", "cs.AR"],
  "source_type": "paper",
  "source_org": "arxiv",
  "credibility": 4,
  "tags": ["hip", "kernel-optimization", "amd-gpu"],
  "citation_count": null,
  "conference": null,
  "lifecycle": "latest"
}
```

---

## 五、翻译策略（论文特化）

### 与文档翻译的区别

| 维度 | 文档翻译 | 论文翻译 |
|------|---------|---------|
| 内容密度 | 中 | 高（每句信息量大） |
| 数学符号 | 偶尔 | 频繁（公式、算法） |
| 专业术语 | GPU 通用 | 领域特化（HPC/编译器/ML） |
| 翻译量 | 全文 | **摘要优先 + 结论核心** |
| 版权 | 开源 | 尊重预印本政策 |

### 翻译 Prompt（论文专用）

```
You are a technical translator specializing in GPU/HPC academic papers.
Translate the following English academic text to Simplified Chinese.

Rules:
1. Preserve ALL mathematical notation, LaTeX, and formulas unchanged.
2. Preserve author names, institution names, and paper titles unchanged.
3. Keep technical terms: ROCm, HIP, CUDA, GPU, kernel, warp, wavefront...
4. For the abstract: provide a complete, polished translation.
5. For the conclusion: focus on key findings, preserve quantitative results.
6. Output ONLY the translation — no explanations.
```

---

## 六、新增/修改文件清单

| 文件 | 操作 | 说明 |
|------|------|------|
| `scripts/fetch-papers.py` | **新建** | arXiv API 搜索 + 索引生成 |
| `scripts/extract-pdf.py` | **新建** | PDF → Markdown 提取 |
| `data/papers.json` | **新建** | 论文索引 |
| `content/raw/papers/` | **新建** | 论文原文存放 |
| `content/translated/zh/papers/` | **新建** | 论文翻译 |
| `scripts/translate.py` | 修改 | 增加论文翻译专用 prompt |
| `scripts/generate-docs.py` | 修改 | 论文 source_type 适配 |
| `scripts/generate-sidebar.py` | 修改 | 新增 📜 分类 |
| `website/src/components/ArticleMeta/index.tsx` | 修改 | 新增 `paper` 类型标签 |
| `.github/workflows/sync.yml` | 修改 | 增加 fetch-papers + translate-papers 步骤 |
| `docs/PROGRESS.md` | 修改 | 记录 Phase 8 |

---

## 七、实施步骤（7 步）

### 8.1 核心抓取脚本 — `fetch-papers.py`
- 调用 arXiv API，执行 6 组查询
- Atom XML 解析，提取元数据
- 按 `arxiv_id` 去重
- 输出 `data/papers.json`
- 干跑先测试产出数量

### 8.2 PDF 提取 — `extract-pdf.py`
- PyMuPDF (`fitz`) 提取文本
- Markdown 格式输出
- 跳过参考文献页（优化）
- 处理数学公式转 LaTeX

### 8.3 论文翻译适配
- `translate.py` 增加 `--mode paper` 选项
- 专用 system prompt（见 §五）
- 摘要 100% 翻译 + 结论详细翻译 + 正文可选
- 数学公式保护

### 8.4 MDX 生成适配
- `generate-docs.py` 识别 `source_type=paper`
- PaperArticleHeader 组件（显示作者、arXiv ID、分类）
- arXiv 原文链接 + PDF 链接

### 8.5 侧边栏 + 标签
- 新增 `📜 技术论文` 分类
- 按 arXiv 分类（cs.DC / cs.AR / cs.LG）分子类
- Paper 标签：`paper`、`arxiv`、`peer-reviewed`

### 8.6 CI 集成
- `sync.yml` 增加 `fetch-papers` 步骤（每周运行）
- 或新建独立 `sync-papers.yml`（每周末运行，避免频繁）

### 8.7 部署后验证
- 至少 5 篇论文展示在网站
- 摘要中文翻译正确
- PDF 下载链接可达

---

## 八、风险与注意

| 风险 | 缓解 |
|------|------|
| arXiv API 限速 | 请求间隔 3s，单次 ≤ 50 条 |
| PDF 解析质量 | PyMuPDF 优于 pdftotext；公式损失可接受 |
| 论文版权 | 仅收录 arXiv 预印本（开放获取），不翻译全文发布，仅摘要+结论 |
| 重复/低质论文 | 关键词过滤 + credibility=4（由用户手动调高到 5） |
| 翻译成本 | opencode 免费端点，每篇摘要 ~500 tokens → 68 篇也够用 |
