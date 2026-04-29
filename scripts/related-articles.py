#!/usr/bin/env python3
"""
related-articles.py — 为每篇文章计算最相关的 3-5 篇推荐文章。

基于关键词 Jaccard 相似度 + 标签重叠度加权排序。

用法：
  python3 scripts/related-articles.py              # 全量计算
  python3 scripts/related-articles.py --top-n 3     # 每篇推荐 N 篇
  python3 scripts/related-articles.py --dry-run     # 预览
"""
import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# ── 项目路径 ────────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = (PROJECT_ROOT / "website" / "docs").resolve()
DATA_DIR = (PROJECT_ROOT / "data").resolve()
OUTPUT_JSON = (DATA_DIR / "related-articles.json").resolve()

# ── 关键词黑名单（太泛的关键词不加权）──────────────
STOP_KEYWORDS = {
    "amd", "rocm", "gpu", "官方文档", "amd官方", "bilingual",
    "中英对照", "双语", "翻译", "gpu编程", "hpc", "人工智能",
    "深度学习", "并行计算",
}

# ── 高权重关键词（专业术语，重叠多说明话题高度相关）─
BOOST_KEYWORDS = {
    # GPU 型号
    "mi100", "mi250", "mi300x", "mi300", "mi210", "cdna2", "cdna3",
    "rdna3", "rdna3.5", "gfx90a", "gfx942",
    # 框架
    "pytorch", "tensorflow", "jax", "onnx", "triton",
    # 技术领域
    "hip", "hipify", "rocblas", "rocfft", "miopen", "migraphx",
    "inference", "fine-tuning", "training", "quantization",
    "performance", "optimization", "benchmark",
    # 安装/环境
    "installation", "install", "setup", "docker", "container",
    "ubuntu", "wsl2", "linux", "windows",
    # 调试
    "debugging", "profiling", "troubleshoot",
}


def parse_mdx_frontmatter(content: str) -> dict:
    """解析 MDX 文件的 frontmatter。"""
    m = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not m:
        return {}

    fm_text = m.group(1)
    result = {}

    # 提取 title
    title_m = re.search(r'title:\s*["\']?(.+?)["\']?\s*$', fm_text, re.MULTILINE)
    if title_m:
        result["title"] = title_m.group(1).strip().strip('"').strip("'")

    # 提取 keywords 数组
    kw_m = re.search(r'keywords:\s*\[(.*?)\]', fm_text, re.DOTALL)
    if kw_m:
        kw_text = kw_m.group(1)
        kws = re.findall(r'"([^"]+)"', kw_text)
        result["keywords"] = [k.strip() for k in kws if k.strip()]

    # 提取其他字段
    for field in ["source_url", "source_type", "credibility", "lifecycle",
                   "difficulty", "published_date"]:
        m = re.search(rf'{field}:\s*["\']?(.+?)["\']?\s*$', fm_text, re.MULTILINE)
        if m:
            val = m.group(1).strip().strip('"').strip("'")
            # 数字字段
            if field == "credibility":
                try:
                    result[field] = int(val)
                except ValueError:
                    result[field] = 3
            else:
                result[field] = val

    # 提取 tags
    tags_m = re.search(r'tags:\s*\[(.*?)\]', fm_text, re.DOTALL)
    if tags_m:
        tags_text = tags_m.group(1)
        result["tags"] = re.findall(r'"([^"]+)"', tags_text)

    return result


def keyword_weight(keyword: str) -> float:
    """计算单个关键词的权重。

    权重规则：
      - 高权重关键词（专业术语）：2.0x
      - 停用词（通用词）：0.1x
      - 普通关键词：1.0x
    """
    kl = keyword.lower()
    if kl in BOOST_KEYWORDS:
        return 2.0
    if kl in STOP_KEYWORDS:
        return 0.1
    return 1.0


def jaccard_weighted(kw_a: list[str], kw_b: list[str]) -> float:
    """计算加权 Jaccard 相似度。

    加权规则：每个关键词按其权重计入交/并集。
    """
    if not kw_a or not kw_b:
        return 0.0

    # 转小写集合
    set_a = {k.lower() for k in kw_a}
    set_b = {k.lower() for k in kw_b}

    # 加权交集
    intersection_weight = sum(
        keyword_weight(k) for k in (set_a & set_b)
    )

    # 加权并集
    union_weight = sum(
        keyword_weight(k) for k in (set_a | set_b)
    )

    if union_weight == 0:
        return 0.0

    # Jaccard
    jaccard = intersection_weight / union_weight

    return round(jaccard, 4)


def compute_related(articles: list[dict], top_n: int = 5) -> dict[str, list]:
    """为每篇文章计算 top-N 相关文章。

    articles: [{"slug": str, "keywords": [...], "title": str}, ...]

    返回: { "article-slug": [{"slug": ..., "title": ..., "score": ...}, ...] }
    """
    result = {}

    for i, article in enumerate(articles):
        slug = article.get("slug", "")
        kw_a = article.get("keywords", [])

        scores = []
        for j, other in enumerate(articles):
            if i == j:
                continue
            kw_b = other.get("keywords", [])
            score = jaccard_weighted(kw_a, kw_b)
            if score > 0:
                scores.append({
                    "slug": other.get("slug", ""),
                    "title": other.get("title", "Untitled"),
                    "keywords_overlap_score": score,
                })

        # 按分数降序排列，取 top N
        scores.sort(key=lambda x: x["keywords_overlap_score"], reverse=True)
        result[slug] = scores[:top_n]

    return result


def main():
    parser = argparse.ArgumentParser(description="计算文章相关度推荐")
    parser.add_argument("--top-n", type=int, default=5, help="每篇推荐 N 篇")
    parser.add_argument("--dry-run", action="store_true", help="预览")
    args = parser.parse_args()

    print("🔗 rocm-hip-map related-articles.py")
    print(f"   top-N={args.top_n} {'DRY RUN' if args.dry_run else ''}")

    # 扫描所有 MDX 文件
    mdx_files = sorted(DOCS_DIR.rglob("*.mdx"))
    if not mdx_files:
        print("⚠ No MDX files found")
        return

    articles = []
    for mdx_file in mdx_files:
        with open(mdx_file, encoding="utf-8") as f:
            content = f.read()
        fm = parse_mdx_frontmatter(content)

        # 计算 slug（文件相对路径，去扩展名）
        slug = str(mdx_file.relative_to(DOCS_DIR)).replace(".mdx", "")

        articles.append({
            "slug": slug,
            "title": fm.get("title", mdx_file.stem.replace("_", " ").title()),
            "keywords": fm.get("keywords", []),
            "tags": fm.get("tags", []),
            "source_url": fm.get("source_url", ""),
            "difficulty": fm.get("difficulty", ""),
        })

    print(f"   Found {len(articles)} articles")

    # 计算相关度
    related = compute_related(articles, top_n=args.top_n)

    # 统计
    total_pairs = sum(len(v) for v in related.values())
    avg_pairs = total_pairs / len(related) if related else 0
    print(f"   Computed {total_pairs} related pairs (avg {avg_pairs:.1f}/article)")

    if args.dry_run:
        # 展示前 3 篇的推荐结果
        for slug, recs in list(related.items())[:3]:
            print(f"\n  📄 {slug}")
            for r in recs[:3]:
                bar = "█" * min(int(r["keywords_overlap_score"] * 10), 10)
                print(f"     {r['keywords_overlap_score']:.2f} {bar} {r['title'][:60]}")
        return

    # 输出 JSON
    output = {
        "version": 1,
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "top_n": args.top_n,
        "total_articles": len(articles),
        "related": related,
    }

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\n📊 已输出: {OUTPUT_JSON}")
    print("💡 下一步: python3 scripts/generate-docs.py  # 重新生成 MDX 嵌入推荐组件")


if __name__ == "__main__":
    main()
