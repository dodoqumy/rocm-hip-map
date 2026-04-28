#!/usr/bin/env python3
"""
generate-docs.py — 将 content/raw/ 的原始 Markdown 转为 Docusaurus MDX 页面。

按来源自动分配类别，产生双语对照页面。
用法：
  python3 scripts/generate-docs.py                # 全量生成
  python3 scripts/generate-docs.py --dry-run       # 预览
"""

import argparse
import json
import re
import sys
from pathlib import Path
from datetime import datetime, timezone

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONTENT_RAW_EN = PROJECT_ROOT / "content" / "raw" / "english"
WEBSITE_DOCS = PROJECT_ROOT / "website" / "docs"
ARTICLES_JSON = PROJECT_ROOT / "data" / "articles.json"

# ── 来源 → 网站目录映射 ──────────────────────────
SOURCE_TO_DOCS_DIR = {
    "rocm": "rocm-core",
    "hip": "hip",
    "rocm-install-linux": "install",
    "hipify": "hipify",
}

# ── 来源 → 侧边栏分类标签 ──────────────────────────
SOURCE_TO_SIDEBAR_LABEL = {
    "rocm": "📦 ROCm 核心",
    "hip": "💻 HIP 编程",
    "rocm-install-linux": "📥 安装指南",
    "hipify": "🔄 HIPIFY 迁移",
}

# ── 按 URL 路径判断二级分类 ──────────────────────────
def infer_sub_category(url: str, source: str) -> str:
    """根据 URL 路径推断子分类。"""
    url_lower = url.lower()
    
    if source == "rocm":
        if "/about/" in url_lower:
            return "About"
        elif "/compatibility/" in url_lower:
            return "兼容性"
        elif "/conceptual/" in url_lower:
            return "概念"
        elif "/how-to/rocm-for-ai/" in url_lower:
            return "ROCm for AI"
        elif "/how-to/rocm-for-hpc/" in url_lower:
            return "ROCm for HPC"
        elif "/how-to/system-optimization/" in url_lower:
            return "系统优化"
        elif "/how-to/tuning-guides/" in url_lower:
            return "性能调优"
        elif "/how-to/gpu-performance/" in url_lower:
            return "GPU 性能"
        elif "/how-to/" in url_lower:
            return "操作指南"
        elif "/reference/glossary/" in url_lower:
            return "术语表"
        elif "/reference/" in url_lower:
            return "参考"
        elif "/contribute/" in url_lower:
            return "贡献"
        elif "/release/" in url_lower:
            return "版本发布"
        else:
            return "总览"
    elif source == "hip":
        if "/how-to/" in url_lower:
            return "操作指南"
        elif "/reference/" in url_lower:
            return "参考"
        else:
            return "总览"
    elif source == "rocm-install-linux":
        if "/install/" in url_lower:
            return "安装步骤"
        elif "/reference/" in url_lower:
            return "参考"
        else:
            return "总览"
    elif source == "hipify":
        return "总览"
    return "其他"


def parse_title_from_md(content: str) -> str:
    """从 Markdown 内容中提取有效标题。"""
    # 先看 frontmatter 里的 title
    fm_match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if fm_match:
        fm_text = fm_match.group(1)
        m = re.search(r'(?:^|\n)title:\s*(.+)', fm_text)
        if m:
            title = m.group(1).strip().strip('"').strip("'")
            # 过滤 pandoc artifacts
            if title and not title.startswith('::') and '{' not in title and len(title) > 2:
                return title
    
    # 再看第一个 # 标题，跳过 artifact 行
    for line in content.split("\n"):
        stripped = line.strip()
        if stripped.startswith("# "):
            title = stripped[2:].strip()
            # 跳过 pandoc artifacts
            if title.startswith(":::") or "{#" in title or title in ("Skip to main content", "Back to top"):
                continue
            if len(title) > 2:
                return title
    
    return "Untitled"


def sanitize_filename(name: str) -> str:
    """生成安全的文件名 slug。"""
    # 去特殊字符，转小写，空格转横线
    slug = re.sub(r'[^a-zA-Z0-9\u4e00-\u9fff\s_-]', '', name)
    slug = re.sub(r'[\s_]+', '-', slug).strip('-')
    return slug.lower()[:80]


def clean_title(raw: str) -> str:
    """彻底清理标题中的 pandoc artifact。"""
    # 截断 artifact 后缀
    # 模式: "Real Title'main\\'}" 或 "Real Title"main\"}"
    cleaned = re.sub(r"['\"]main[\\\\'\"}\s]*$", "", raw)
    cleaned = re.sub(r"\s*['\"]?\s*\{\s*#\s*main-content\s*.*?\}\s*['\"]?\s*$", "", cleaned)
    cleaned = cleaned.strip().strip('"').strip("'")
    # 去除连续的冒号 artifact
    if cleaned and all(c in ': ' for c in cleaned):
        return ""
    return cleaned


def _list_to_yaml(seq, max_len=8):
    """将 Python list 转为 YAML 内联数组字符串。"""
    if not seq:
        return "[]"
    items = seq[:max_len]
    return "[" + ", ".join(f'"{str(t)}"' for t in items) + "]"


def _opt_str(val, default=""):
    """返回 YAML 安全的字符串或空字符串。"""
    if val is None or val == "":
        return default
    return str(val).replace('"', "'").replace("\n", " ")


def generate_mdx(article: dict, raw_content: str) -> str:
    """为单篇文章生成 Docusaurus MDX 内容。

    模板参考：docs/templates/page-template.md
    """
    title = article.get("title", parse_title_from_md(raw_content))
    title = clean_title(title)
    if not title or len(title) < 2 or title == "404 - Page Not Found":
        fallback = article.get("file", "")
        if fallback:
            title = Path(fallback).stem.replace("_", " ").replace("-", " ").title()
    if not title or len(title) < 2:
        title = "Untitled"

    source_url = article.get("source_url", "")
    source_type = article.get("source_type", "official")
    source_org = article.get("source_org", "amd")
    credibility = article.get("credibility", 5)
    lifecycle = article.get("lifecycle", "latest")
    tags = article.get("tags_extra", article.get("tags", []))

    # ── 环境分类字段（从 article metadata 或 tags 推断）──
    version = article.get("version", "")
    rocm_versions = article.get("rocm_versions", [])
    os_list = article.get("os", article.get("operating_systems", []))
    gpu = article.get("gpu", [])
    gpu_arch = article.get("gpu_arch", [])
    driver = article.get("driver", [])
    frameworks = article.get("frameworks", [])
    difficulty = article.get("difficulty", "")
    published_date = article.get("published_date", article.get("date", ""))
    synced_date = article.get("synced_date", datetime.now(timezone.utc).strftime("%Y-%m-%d"))

    # ── Frontmatter ──
    safe_title = title.replace('"', "'").replace("\n", " ")
    safe_desc = (article.get("description") or safe_title[:60]).replace('"', "'").replace("\n", " ")

    fm = f"""---
title: "{safe_title}"
description: "{safe_desc}"
source_url: {source_url}
source_type: {source_type}
source_org: {source_org}
credibility: {credibility}
lifecycle: {lifecycle}
version: "{_opt_str(version)}"
rocm_versions: {_list_to_yaml(rocm_versions)}
os: {_list_to_yaml(os_list)}
gpu: {_list_to_yaml(gpu)}
gpu_arch: {_list_to_yaml(gpu_arch)}
driver: {_list_to_yaml(driver)}
frameworks: {_list_to_yaml(frameworks)}
difficulty: "{_opt_str(difficulty)}"
tags: {_list_to_yaml(tags)}
published_date: "{_opt_str(published_date)}"
synced_date: "{_opt_str(synced_date)}"
generated_at: "{datetime.now(timezone.utc).strftime('%Y-%m-%d')}"
---"""

    # Issue 检测
    issue_check = ""
    is_issue = (
        "bug" in tags or "issue" in tags or "troubleshoot" in tags
        or "github.com" in source_url and "/issues/" in source_url
    )
    if is_issue:
        issue_check = '\nimport IssueNotice from "@site/src/components/IssueNotice";\n\n<IssueNotice />'

    mdx = f"""{fm}

import {{ ArticleHeader }} from "@site/src/components/ArticleHeader";
{issue_check}

<ArticleHeader />

> 📄 **原文链接：** [{source_url}]({source_url})
> 🏷 **来源：** AMD 官方文档 · 可信度：{"⭐" * credibility}

---

{{/* BilingualViewer 待修复后重新启用 */}}
{{/* import BilingualViewer from "@site/src/components/BilingualViewer"; */}}
{{/* <BilingualViewer enPath="/data/raw/english/" zhPath="/data/translated/zh/" /> */}}
"""
    return mdx


def load_articles_index() -> dict[str, dict]:
    """加载文章索引，构建 file→article 映射。"""
    if not ARTICLES_JSON.exists():
        return {}
    with open(ARTICLES_JSON) as f:
        data = json.load(f)
    idx = {}
    for a in data.get("articles", []):
        fname = a.get("file", "")
        if fname:
            # 去掉 .md 后缀方便匹配
            stem = Path(fname).stem
            idx[stem] = a
    return idx


def main():
    parser = argparse.ArgumentParser(description="Generate Docusaurus MDX pages from raw content")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    print("📄 rocm-hip-map generate-docs.py")
    print(f"   {'DRY RUN' if args.dry_run else 'LIVE MODE'}")
    
    if not CONTENT_RAW_EN.exists() or not any(CONTENT_RAW_EN.iterdir()):
        print("⚠ content/raw/english/ 为空 — 请先运行 fetch-official.py")
        return

    article_index = load_articles_index()

    generated = 0
    by_dir = {}

    for md_file in sorted(CONTENT_RAW_EN.glob("*.md")):
        with open(md_file) as f:
            raw_content = f.read()
        
        fname = md_file.stem
        
        # 从 articles.json 取元数据
        article = article_index.get(fname, {})
        
        # 来源
        source = "rocm"
        for key in SOURCE_TO_DOCS_DIR:
            if fname.startswith(key + "_"):
                source = key
                break
        
        doc_dir_name = SOURCE_TO_DOCS_DIR.get(source, "other")
        sub_cat = ""
        
        if article and article.get("source_url"):
            sub_cat = infer_sub_category(article["source_url"], source)
        
        # 构建输出路径
        if sub_cat:
            doc_path = WEBSITE_DOCS / doc_dir_name / sub_cat.lower().replace(" ", "-") / f"{fname}.mdx"
        else:
            doc_path = WEBSITE_DOCS / doc_dir_name / f"{fname}.mdx"
        
        mdx_content = generate_mdx(article, raw_content)
        
        if args.dry_run:
            print(f"  [DRY] {doc_path.relative_to(WEBSITE_DOCS)} ({len(mdx_content)} chars)")
        else:
            doc_path.parent.mkdir(parents=True, exist_ok=True)
            with open(doc_path, "w") as f:
                f.write(mdx_content)
            print(f"  ✅ {doc_path.relative_to(WEBSITE_DOCS)}")
        
        key = str(doc_path.parent.relative_to(WEBSITE_DOCS))
        by_dir[key] = by_dir.get(key, 0) + 1
        generated += 1
    
    print(f"\n📊 {generated} pages generated in {len(by_dir)} directories:")
    for d, c in sorted(by_dir.items()):
        print(f"   {d}: {c} pages")


if __name__ == "__main__":
    main()
