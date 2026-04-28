#!/usr/bin/env python3
"""
fetch-papers.py — 从 arXiv API 抓取 ROCm/HIP/AMD GPU 相关学术论文。

搜索策略（6 组查询）→ 按 arxiv_id 去重 → 输出 data/papers.json

用法：
  python3 scripts/fetch-papers.py              # 全量抓取
  python3 scripts/fetch-papers.py --dry-run     # 预览不写入
  python3 scripts/fetch-papers.py --max 20      # 每查询最多 N 篇
"""
import argparse
import json
import re
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

# ── 项目路径 ────────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
PAPERS_JSON = DATA_DIR / "papers.json"

# ── 6 组定期查询（按相关性 + 覆盖面设计）────────────
QUERIES = [
    ("rocm-gpu",    "all:ROCm AND all:GPU"),
    ("hip-amd-gpu", "all:HIP AND all:AMD AND all:GPU"),
    ("mi-instinct", "all:AMD AND all:Instinct AND all:GPU"),
    ("cdna-rdna",   "all:CDNA OR all:RDNA AND all:GPU"),
    ("cuda-port",   "all:CUDA AND all:portability AND all:AMD"),
    ("amd-llm",     "all:AMD AND all:GPU AND all:LLM"),
]

# ── arXiv API ───────────────────────────────────────
ARXIV_API = "http://export.arxiv.org/api/query"
REQUEST_DELAY = 3  # 秒（arXiv 礼貌策略）
MAX_RESULTS_PER_QUERY = 30

# ── Atom XML 命名空间 ──────────────────────────────
NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
}


def load_existing_index() -> dict[str, dict]:
    """加载已有论文索引，用于去重。"""
    if not PAPERS_JSON.exists():
        return {}
    with open(PAPERS_JSON) as f:
        data = json.load(f)
    return {p["arxiv_id"]: p for p in data.get("papers", [])}


def search_arxiv(query: str, max_results: int = 30) -> list[dict]:
    """调用 arXiv API，返回论文列表。"""
    url = (
        f"{ARXIV_API}?search_query={urllib.request.quote(query)}"
        f"&start=0&max_results={max_results}"
        f"&sortBy=submittedDate&sortOrder=descending"
    )

    papers = []
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "rocm-hip-map/1.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            xml_data = resp.read().decode("utf-8")
    except Exception as e:
        print(f"  ⚠ API 错误 ({query[:40]}...): {e}")
        return papers

    # 解析 Atom XML
    try:
        root = ET.fromstring(xml_data)
    except ET.ParseError as e:
        print(f"  ⚠ XML 解析错误: {e}")
        return papers

    for entry in root.findall("atom:entry", NS):
        paper = _parse_entry(entry)
        if paper:
            papers.append(paper)

    return papers


def _parse_entry(entry: ET.Element) -> dict | None:
    """解析单个 Atom entry 为论文元数据。"""

    # arXiv ID
    id_url = entry.findtext("atom:id", "", NS)
    arxiv_id = id_url.split("/abs/")[-1] if "/abs/" in id_url else ""
    if not arxiv_id:
        return None

    # 标题（清理换行符）
    title = entry.findtext("atom:title", "", NS).strip()
    title = re.sub(r"\s+", " ", title)

    # 摘要
    abstract = entry.findtext("atom:summary", "", NS).strip()
    abstract = re.sub(r"\s+", " ", abstract)

    # 作者
    authors = []
    for author_el in entry.findall("atom:author", NS):
        name = author_el.findtext("atom:name", "", NS)
        if name:
            authors.append(name.strip())

    # 发布日期
    published_str = entry.findtext("atom:published", "", NS)
    published = published_str[:10] if published_str else ""

    # 更新日期
    updated_str = entry.findtext("atom:updated", "", NS)
    updated = updated_str[:10] if updated_str else ""

    # arXiv 分类
    categories = []
    for cat_el in entry.findall("atom:category", NS):
        term = cat_el.get("term", "")
        if term:
            categories.append(term)

    # PDF 链接
    pdf_url = f"https://arxiv.org/pdf/{arxiv_id}"
    arxiv_url = f"https://arxiv.org/abs/{arxiv_id}"

    # 自动标签（从标题 + 摘要推断）
    tags = _infer_tags(title, abstract, categories)

    return {
        "id": arxiv_id,
        "arxiv_id": arxiv_id,
        "title": title,
        "authors": authors,
        "abstract": abstract,
        "arxiv_url": arxiv_url,
        "pdf_url": pdf_url,
        "published": published,
        "updated": updated,
        "categories": categories,
        "source_type": "paper",
        "source_org": "arxiv",
        "credibility": 4,
        "tags": tags,
        "lifecycle": "latest",
        "fetched_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


def _infer_tags(title: str, abstract: str, categories: list[str]) -> list[str]:
    """从标题/摘要/分类自动推断标签。"""
    tags = set()
    text = (title + " " + abstract).lower()

    keyword_map = {
        "hip": ["hip", "hipify"],
        "cuda": ["cuda", "nvcc"],
        "kernel": ["kernel", "warp", "wavefront"],
        "performance": ["performance", "benchmark", "throughput", "latency"],
        "optimization": ["optimization", "optimize", "tuning"],
        "hpc": ["hpc", "supercomputing", "exascale"],
        "machine-learning": ["machine learning", "deep learning", "neural network"],
        "llm": ["llm", "large language model", "transformer", "gpt"],
        "inference": ["inference", "deployment", "serving"],
        "training": ["training", "fine-tuning", "pretrain"],
        "mi300": ["mi300", "mi300x", "mi250", "mi210", "mi100"],
        "cdna": ["cdna", "cdna2", "cdna3"],
        "rdna": ["rdna", "rdna3"],
        "rocm": ["rocm", "amd gpu"],
        "porting": ["porting", "migration", "transpilation", "portability"],
    }

    for tag, keywords in keyword_map.items():
        if any(kw in text for kw in keywords):
            tags.add(tag)

    # 从 arXiv 分类补充
    cat_map = {
        "cs.DC": "distributed-computing",
        "cs.AR": "architecture",
        "cs.LG": "machine-learning",
        "cs.AI": "ai",
        "cs.PF": "performance",
        "cs.MS": "modeling-simulation",
    }
    for cat in categories:
        if cat in cat_map:
            tags.add(cat_map[cat])

    return sorted(tags)[:10]


def fetch_all(max_per_query: int = 30, dry_run: bool = False) -> int:
    """执行全部 6 组查询，增量化写入。"""
    existing = load_existing_index()
    new_papers: dict[str, dict] = {}
    total_checked = 0

    for group_name, query in QUERIES:
        if dry_run:
            print(f"\n🔍 [{group_name}] {query}")
        else:
            print(f"\n📡 [{group_name}] 搜索中...")

        papers = search_arxiv(query, max_results=max_per_query)
        total_checked += len(papers)

        new_in_group = 0
        for paper in papers:
            aid = paper["arxiv_id"]
            if aid in existing or aid in new_papers:
                continue
            new_papers[aid] = paper
            new_in_group += 1

        status = "预览" if dry_run else f"+{new_in_group} 新 / {len(papers)} 返回"
        print(f"   {status}")

        if not dry_run and group_name != QUERIES[-1][0]:
            time.sleep(REQUEST_DELAY)

    if dry_run:
        print(f"\n📊 预览: {total_checked} 篇检查，去重后 {len(new_papers)} 新论文")
        for aid, p in list(new_papers.items())[:5]:
            print(f"   📄 {aid}: {p['title'][:80]}")
        return len(new_papers)

    # 合并已有 + 新增
    all_papers = list(existing.values()) + list(new_papers.values())
    # 按发布日期降序
    all_papers.sort(key=lambda x: x.get("published", ""), reverse=True)

    output = {
        "version": 1,
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "total": len(all_papers),
        "papers": all_papers,
    }

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(PAPERS_JSON, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\n📊 结果: {len(new_papers)} 新论文 / {len(all_papers)} 总计")
    print(f"   索引: {PAPERS_JSON}")
    print(f"   💡 下一步: python3 scripts/extract-pdf.py  # 下载 PDF 提取正文")

    return len(new_papers)


def main():
    parser = argparse.ArgumentParser(description="Fetch ROCm/HIP papers from arXiv")
    parser.add_argument("--dry-run", action="store_true", help="Preview only")
    parser.add_argument("--max", type=int, default=MAX_RESULTS_PER_QUERY,
                        help=f"Max results per query (default: {MAX_RESULTS_PER_QUERY})")
    args = parser.parse_args()

    print("📜 rocm-hip-map fetch-papers.py")
    print(f"   {'DRY RUN' if args.dry_run else 'LIVE MODE'}")
    print(f"   {len(QUERIES)} 查询组 × {args.max} 篇/组")

    fetch_all(max_per_query=args.max, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
