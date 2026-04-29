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
from urllib.parse import urljoin, urlparse

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONTENT_RAW_EN = PROJECT_ROOT / "content" / "raw" / "english"
WEBSITE_DOCS = PROJECT_ROOT / "website" / "docs"
ARTICLES_JSON = PROJECT_ROOT / "data" / "articles.json"
CACHE_JSON = PROJECT_ROOT / "data" / "image-cache.json"


def load_image_cache() -> dict:
    """加载图片缓存映射表。key = raw markdown 中的原始路径，value = {local, ...}。"""
    if not CACHE_JSON.exists():
        return {}
    with open(CACHE_JSON) as f:
        data = json.load(f)
    return data.get("mappings", {})


def rewrite_image_urls(body: str, page_url: str) -> str:
    """将正文中的相对图片路径解析为绝对远程 URL。

    保留远程 URL 作为主源，让客户端 fallback 模块处理加载失败。

    例如:
      ![](../../_images/image001.png)
      → ![](https://rocm.docs.amd.com/en/latest/_images/image001.png)

    Pandoc RST→MD 转换会生成 ../_images/ 前缀，但 AMD Sphinx 构建中
    _images/ 实际位于页面同级目录（latest/ 下），而非父目录（en/ 下）。
    因此对 ../_images/ 做特殊处理：去掉 ../，按页面目录解析。
    """
    if not page_url:
        return body

    def resolve_ref(m):
        prefix = m.group(1)  # ![
        alt_text = m.group(2) or ""  # alt text or empty
        close_bracket = m.group(3)  # ](
        url = m.group(4)  # the URL
        suffix = m.group(5) or ""  # ) or ){.class}

        # 跳过 data: URI
        if url.startswith("data:"):
            return m.group(0)

        # 跳过已经是绝对 HTTP URL 的
        if url.startswith("http://") or url.startswith("https://"):
            return m.group(0)

        # 跳过本地缓存路径
        if url.startswith("/img/cached/"):
            return m.group(0)

        # Pandoc RST artifact: ../_images/ → _images/（AMD docs 中图片在页面同级目录）
        # urljoin('.../latest/page.html', '../_images/x.png') → '.../en/_images/x.png' (错)
        # urljoin('.../latest/page.html', '_images/x.png') → '.../latest/_images/x.png' (对)
        url = re.sub(r'^(\.\./)+(_images/)', r'\2', url)

        # 相对路径 → 用页面 URL 解析为绝对 URL
        abs_url = urljoin(page_url, url)
        return f"{prefix}{alt_text}{close_bracket}{abs_url}{suffix}"

    # 匹配 ![...](...) 模式
    body = re.sub(
        r'(!\\[)([^\\]]*)(\\]\\()([^)]+)(\\))',
        resolve_ref,
        body,
    )

    return body

def raw_frontmatter_field(content: str, field: str, default: str = "") -> str:
    """从 raw markdown 的 frontmatter 中提取单个字段。"""
    m = re.search(rf'(?:^|\n){field}:\s*"?(.+?)"?\s*$', content, re.MULTILINE)
    if m:
        return m.group(1).strip().strip('"').strip("'")
    return default


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


def generate_mdx(article: dict, raw_content: str, doc_slug: str = "") -> str:
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

    # ── 自动生成 SEO 关键词（中英双语）──
    def gen_keywords(article, tags, os_list, gpu, gpu_arch, driver, frameworks) -> list:
        """从文章元数据生成 SEO 关键词。"""
        kw = set()
        # 来源关键词
        source_type = article.get("source_type", "official")
        if source_type == "official":
            kw.update(["ROCm", "AMD", "GPU", "官方文档", "AMD官方"])
        elif source_type == "paper":
            kw.update(["ROCm", "AMD", "GPU", "论文", "学术", "arXiv"])
        elif source_type == "github-issue":
            kw.update(["ROCm", "AMD", "GPU", "Issue", "问题", "bug"])
        
        # 从 tags 提取
        for t in tags:
            t_lower = t.lower()
            if t_lower in ("tutorial", "guide", "reference"):
                kw.add("教程" if t_lower != "reference" else "参考")
            elif t_lower in ("troubleshoot", "bug", "issue", "debugging"):
                kw.add("故障排查")
            elif t_lower in ("performance", "optimization"):
                kw.update(["性能", "优化", "performance"])
            elif t_lower in ("installation", "install", "setup"):
                kw.update(["安装", "配置", "部署"])
            else:
                kw.add(t)
        
        # 从 GPU / 架构
        for g in gpu:
            kw.add(g.upper() if len(g) <= 8 else g)
        for a in gpu_arch:
            kw.add(a.upper() if len(a) <= 8 else a)
        
        # 从 OS
        os_cn = {"linux": "Linux", "windows": "Windows", "docker": "Docker",
                 "ubuntu-22.04": "Ubuntu", "wsl2": "WSL2"}
        for o in os_list:
            kw.add(os_cn.get(o, o))
        
        # 从框架
        fw_cn = {"pytorch": "PyTorch", "tensorflow": "TensorFlow",
                 "jax": "JAX", "onnx": "ONNX"}
        for f in frameworks:
            kw.add(fw_cn.get(f, f))
        
        # 从 driver
        for d in driver:
            kw.add(d)
        
        # 中文通用关键词
        kw.update(["中英对照", "双语", "翻译", "bilingual", "GPU编程",
                    "HPC", "人工智能", "深度学习", "并行计算"])
        
        # 限制 20 个，去重排序
        return sorted(list(kw))[:20]

    keywords = gen_keywords(article, tags, os_list, gpu, gpu_arch, driver, frameworks)
    kw_str = "[" + ", ".join(f'"{k}"' for k in keywords) + "]"

    # ── Frontmatter ──
    safe_title = title.replace('"', "'").replace("\n", " ")
    safe_desc = (article.get("description") or safe_title[:60]).replace('"', "'").replace("\n", " ")

    fm = f"""---
title: "{safe_title}"
description: "{safe_desc}"
keywords: {kw_str}
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
arxiv_id: "{_opt_str(article.get("arxiv_id", ""))}"
---"""

    # Issue 检测
    issue_check = ""
    is_issue = (
        "bug" in tags or "issue" in tags or "troubleshoot" in tags
        or "github.com" in source_url and "/issues/" in source_url
    )
    if is_issue:
        issue_check = '\nimport IssueNotice from "@site/src/components/IssueNotice";\n\n<IssueNotice />'

    # ── 正文：清洗 raw_content（pandoc artifact 清理）+ 嵌入 ──
    body = raw_content
    # 1. 去除源文件的 frontmatter
    if body.startswith("---"):
        end_fm = body.find("---", 3)
        if end_fm != -1:
            body = body[end_fm + 3:].strip()
    # 2. 去除 pandoc artifact: ::::: ::: 区块标记
    body = re.sub(r'^:{3,}.*$', '', body, flags=re.MULTILINE)
    # 3. 去除 pandoc inline class: {.class} {.class1 .class2}
    body = re.sub(r'\{[.][a-zA-Z0-9_ .-]*\}', '', body)
    # 4. 去除 pandoc header anchor: {#id}
    body = re.sub(r'\{#[a-zA-Z0-9_-]+\}', '', body)
    # 5. 去除空的 [] 和 [ ] 占位符
    body = re.sub(r'\[\s*\]', '', body)
    # 6. 删除纯 artifact 空行（base64 SVG data:image 行等）
    body = re.sub(r'^\[?\s*!\[\]\(data:image[^)]*\)\s*\]?\s*$', '', body, flags=re.MULTILINE)
    # 7. 删除 headerlink artifact (# GPU arch[\#](...){.headerlink} → # GPU arch)
    body = re.sub(r'\[\\\\#\]\([^)]*\)', '', body)
    # 8. 合并多余空行
    body = re.sub(r'\n{3,}', '\n\n', body)
    # 8.5. 图片路径解析：相对路径 → 绝对远程 URL（保留远程主源 + 客户端 fallback）
    body = rewrite_image_urls(body, source_url)
    # 9. 转义 MDX 花括号（防止被 React 当成表达式）
    #    但先保护已存在的 HTML 实体
    body = body.replace('&', '&amp;')
    body = body.replace('&amp;lt;', '&lt;').replace('&amp;gt;', '&gt;')
    body = body.replace('&amp;amp;', '&amp;')
    body = body.replace('&amp;quot;', '&quot;')
    # 10. 花括号转义为 HTML 实体
    body = body.replace('{', '&#123;').replace('}', '&#125;')
    # 恢复常见的 HTML 实体
    for ent in ['lt', 'gt', 'amp', 'quot', 'apos', '#123', '#125']:
        body = body.replace(f'&amp;{ent};', f'&{ent};')
    # 11. 转义尖括号为 HTML 实体
    #    所有内容（论文 + 官方文档）均为 RST/PDF 转换产物，不含合法 HTML
    body = body.replace('<', '&lt;').replace('>', '&gt;')
    
    # ── 来源行（文档 vs 论文）──
    stars = "\u2b50" * credibility
    src_label = "arXiv：" if source_type == "paper" else "原文链接："
    org_label = "学术论文 · 同行评审" if source_type == "paper" else "AMD 官方文档 · 可信度"
    source_line = "> 📄 **" + src_label + "** [" + source_url + "](" + source_url + ")  \n> 🏷 **来源：** " + org_label + "：" + stars


    mdx = f"""{fm}

import ArticleHeader from "@site/src/components/ArticleHeader";
import PaperArticleHeader from "@site/src/components/PaperArticleHeader";
{issue_check}

<ArticleHeader />
<PaperArticleHeader />

{source_line}

---

{body}
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
        # 跳过大文件和非阅读文档
        fname_lower = md_file.name.lower()
        SKIP_PATTERNS = ['changelog', 'release-notes', 'versions', 'compatibility-matrix']
        SKIP_SIZE_KB = 500
        if any(p in fname_lower for p in SKIP_PATTERNS):
            print(f"  skip: {md_file.name} (non-reading doc)")
            continue
        if md_file.stat().st_size > SKIP_SIZE_KB * 1024:
            print(f"  skip: {md_file.name} ({md_file.stat().st_size // 1024}KB)")
            continue
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
    
    # 清理被跳过文件对应的旧 MDX
    if not args.dry_run:
        cleaned = 0
        SKIP_PATTERNS = ['changelog', 'release-notes', 'versions', 'compatibility-matrix']
        SKIP_SIZE_KB = 500
        for mdx_file in sorted(WEBSITE_DOCS.rglob("*.mdx")):
            mdx_name = mdx_file.stem
            raw_file = CONTENT_RAW_EN / f"{mdx_name}.md"
            if raw_file.exists():
                fname_lower = raw_file.name.lower()
                if any(p in fname_lower for p in SKIP_PATTERNS) or \
                   raw_file.stat().st_size > SKIP_SIZE_KB * 1024:
                    mdx_file.unlink()
                    cleaned += 1
        if cleaned:
            print(f"   🧹 cleaned {cleaned} stale MDX from skipped docs")

    # ── 论文页生成 ──
    papers_dir = PROJECT_ROOT / "content" / "raw" / "papers"
    if papers_dir.exists():
        paper_files = sorted(papers_dir.glob("*.md"))
        paper_generated = 0
        for pf in paper_files:
            with open(pf) as f:
                raw = f.read()
            article = article_index.get(pf.stem, {})
            # 从 raw frontmatter 补全论文特有字段
            article["source_type"] = "paper"
            article["source_org"] = "arxiv"
            if not article.get("source_url"):
                article["source_url"] = raw_frontmatter_field(raw, "source_url", "")
            if not article.get("arxiv_id"):
                article["arxiv_id"] = raw_frontmatter_field(raw, "arxiv_id", pf.stem)
            if not article.get("title"):
                article["title"] = raw_frontmatter_field(raw, "title", pf.stem)
            out_path = WEBSITE_DOCS / "papers" / f"{pf.stem}.mdx"
            mdx = generate_mdx(article, raw, str(out_path.relative_to(WEBSITE_DOCS)).replace(".mdx", ""))
            if not args.dry_run:
                out_path.parent.mkdir(parents=True, exist_ok=True)
                with open(out_path, "w") as f:
                    f.write(mdx)
            paper_generated += 1
        print(f"\n📜 {paper_generated} paper pages generated in website/docs/papers/")

    # ── 多语言情报页生成 ──
    ml_dir = PROJECT_ROOT / "content" / "raw" / "multilingual"
    if ml_dir.exists():
        ml_generated = 0
        for lang_dir in sorted(ml_dir.iterdir()):
            if not lang_dir.is_dir():
                continue
            lang = lang_dir.name
            for pf in sorted(lang_dir.glob("*.md")):
                with open(pf) as f:
                    raw = f.read()
                article = article_index.get(pf.stem, {})
                article["source_type"] = "multilingual"
                article["source_org"] = raw_frontmatter_field(raw, "source_org", "unknown")
                article["source_url"] = raw_frontmatter_field(raw, "source_url", "")
                article["original_lang"] = raw_frontmatter_field(raw, "original_lang", lang)
                if not article.get("title"):
                    article["title"] = raw_frontmatter_field(raw, "title", pf.stem)
                out_path = WEBSITE_DOCS / "multilingual" / lang / f"{pf.stem}.mdx"
                mdx = generate_mdx(article, raw, str(out_path.relative_to(WEBSITE_DOCS)).replace(".mdx", ""))
                if not args.dry_run:
                    out_path.parent.mkdir(parents=True, exist_ok=True)
                    with open(out_path, "w") as f:
                        f.write(mdx)
                ml_generated += 1
        print(f"\n🌐 {ml_generated} multilingual pages generated in website/docs/multilingual/")


if __name__ == "__main__":
    main()
