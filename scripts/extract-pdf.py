#!/usr/bin/env python3
"""
extract-pdf.py — 从 arXiv 下载论文 PDF，提取正文为 Markdown。

用法：
  python3 scripts/extract-pdf.py                  # 增量提取（跳过已有）
  python3 scripts/extract-pdf.py --limit 5         # 只处理前 5 篇
  python3 scripts/extract-pdf.py --force           # 强制重新提取所有
  python3 scripts/extract-pdf.py --arxiv-id 2301.00001  # 单篇提取
"""
import argparse
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import fitz  # PyMuPDF
import requests

# ── 项目路径 ────────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
CONTENT_RAW_PAPERS = PROJECT_ROOT / "content" / "raw" / "papers"
PAPERS_JSON = DATA_DIR / "papers.json"
PDF_CACHE_DIR = DATA_DIR / "pdfs"

# ── 请求配置 ────────────────────────────────────────
HEADERS = {"User-Agent": "rocm-hip-map-pdf-extractor/1.0"}
DOWNLOAD_TIMEOUT = 60
REQUEST_DELAY = 1.0  # arXiv 限速

# ── 正文清洗配置 ─────────────────────────────────────
MIN_SECTION_LENGTH = 40  # 段落最少字符
MAX_ABSTRACT_LINES = 80  # 摘要最多行（改写作法用）


def sanitize_text(text: str) -> str:
    """清洗提取的文本：去除换行符断裂、非法字符。"""
    # 合并断行（单换行 → 空格）
    text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text)
    # 去除页码
    text = re.sub(r'\n\s*\d+\s*\n', '\n', text)
    # 压缩多余空行
    text = re.sub(r'\n{3,}', '\n\n', text)
    # 压缩多余空格
    text = re.sub(r' {2,}', ' ', text)
    return text.strip()


def extract_sections(doc: fitz.Document) -> list[dict]:
    """按页提取文本，尝试识别章节标题。

    返回: [{"title": str, "content": str}, ...]
    """
    sections = []
    current_title = ""
    current_lines = []

    # 章节标题检测正则
    section_patterns = [
        re.compile(r'^(?:\d+\.?\s+)?(?:[A-Z][A-Za-z\s\-]{3,50})$'),  # "1. Introduction"
        re.compile(r'^(?:[IVX]+\.?\s+)?[A-Z][A-Za-z\s\-]{3,50}$'),  # "III. Method"
        re.compile(r'^[A-Z][A-Z\s\-]{5,50}$'),  # "RELATED WORK"
    ]

    for page in doc:
        blocks = page.get_text("blocks")
        blocks.sort(key=lambda b: (b[1], b[0]))  # 按 y, x 排序

        for block in blocks:
            text = block[4].strip()
            if not text or len(text) < 5:
                continue

            # 跳过页眉页脚
            if re.match(r'^arXiv:\d+\.\d+', text):
                continue
            if len(text) < 20 and text.isdigit():
                continue

            # 检测章节标题
            is_title = False
            for pat in section_patterns:
                if pat.match(text) and 4 < len(text) < 80:
                    is_title = True
                    break

            if is_title and len(text) > 5:
                # 保存前一节
                if current_lines:
                    content = sanitize_text("\n".join(current_lines))
                    if len(content) > MIN_SECTION_LENGTH:
                        sections.append({
                            "title": current_title or "正文",
                            "content": content,
                        })
                current_title = text
                current_lines = []
            else:
                current_lines.append(text)

    # 最后一节
    if current_lines:
        content = sanitize_text("\n".join(current_lines))
        if len(content) > MIN_SECTION_LENGTH:
            sections.append({
                "title": current_title or "正文",
                "content": content,
            })

    return sections


def download_pdf(arxiv_id: str) -> Optional[Path]:
    """下载论文 PDF 到本地缓存。"""
    PDF_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    pdf_path = PDF_CACHE_DIR / f"{arxiv_id}.pdf"

    if pdf_path.exists():
        return pdf_path

    url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=DOWNLOAD_TIMEOUT)
        resp.raise_for_status()

        # 检查是不是真的 PDF
        content_type = resp.headers.get("Content-Type", "")
        if "pdf" not in content_type and "octet" not in content_type:
            # arXiv 有时返回 HTML（限速页面）
            if b"<html" in resp.content[:200].lower():
                print(f"    ⚠ arXiv 返回 HTML（可能限速），等待重试...")
                time.sleep(5)
                return None

        with open(pdf_path, "wb") as f:
            f.write(resp.content)
        return pdf_path

    except requests.RequestException as e:
        print(f"    ❌ 下载失败: {e}")
        return None


def extract_paper(arxiv_id: str, title: str, abstract: str, force: bool = False) -> Optional[dict]:
    """提取单篇论文。

    返回: {"arxiv_id": ..., "title": ..., "sections": [...], ...}
    """
    # 检查是否已有提取结果
    output_path = CONTENT_RAW_PAPERS / f"{arxiv_id}.md"
    if output_path.exists() and not force:
        return None

    # 下载 PDF
    pdf_path = download_pdf(arxiv_id)
    if not pdf_path:
        return None

    # 提取文本
    try:
        doc = fitz.open(str(pdf_path))
    except Exception as e:
        print(f"    ❌ PDF 打开失败: {e}")
        # 删除损坏的 PDF
        pdf_path.unlink(missing_ok=True)
        return None

    sections = extract_sections(doc)
    doc.close()

    # 构建正文 Markdown
    body = _build_markdown(arxiv_id, title, abstract, sections)

    # 写入 raw 文件
    CONTENT_RAW_PAPERS.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(body)

    total_chars = sum(len(s["content"]) for s in sections)
    return {
        "arxiv_id": arxiv_id,
        "title": title,
        "sections_count": len(sections),
        "chars": total_chars,
        "file": str(output_path.relative_to(PROJECT_ROOT)),
    }


def _build_markdown(arxiv_id: str, title: str, abstract: str,
                    sections: list[dict]) -> str:
    """组装 Markdown 正文。

    格式：
      ---
      frontmatter
      ---
      # Abstract
      ...
      ## Section title
      ...
    """
    # 转义 title 中的双引号
    safe_title = title.replace('"', "'")
    safe_abstract = abstract[:500].replace('"', "'").replace("\n", " ")

    fm = f"""---
title: "{safe_title}"
source_url: "https://arxiv.org/abs/{arxiv_id}"
source_type: "paper"
source_org: "arxiv"
original_lang: "en"
credibility: 4
lifecycle: "latest"
synced_date: {datetime.now(timezone.utc).strftime('%Y-%m-%d')}
arxiv_id: "{arxiv_id}"
---

"""

    body = fm

    # 摘要
    if abstract.strip():
        body += f"## 摘要\n\n{abstract.strip()}\n\n"

    # 各节
    for sec in sections:
        title_text = sec.get("title", "")
        content = sec.get("content", "")

        if not content.strip():
            continue

        if title_text and title_text != "正文":
            body += f"## {title_text}\n\n"
        body += f"{content}\n\n"

    return body


def load_papers() -> list[dict]:
    """加载 papers.json。"""
    if not PAPERS_JSON.exists():
        print(f"❌ {PAPERS_JSON} not found — run fetch-papers.py first")
        return []
    with open(PAPERS_JSON) as f:
        data = json.load(f)
    return data.get("papers", [])


def main():
    parser = argparse.ArgumentParser(description="Extract text from arXiv PDFs")
    parser.add_argument("--limit", type=int, default=0, help="只处理前 N 篇")
    parser.add_argument("--force", action="store_true", help="强制重新提取所有")
    parser.add_argument("--arxiv-id", type=str, help="单篇提取指定 ID")
    args = parser.parse_args()

    print("📄 rocm-hip-map extract-pdf.py")
    print(f"   {'FORCE' if args.force else 'INCREMENTAL'}"
          f"{' limit=' + str(args.limit) if args.limit else ''}")

    # 单篇模式
    if args.arxiv_id:
        print(f"\n   📥 Extracting {args.arxiv_id}...")
        result = extract_paper(args.arxiv_id, "Paper", "", force=True)
        if result:
            print(f"   ✅ {result['sections_count']} sections, {result['chars']} chars")
        else:
            print(f"   ❌ Extraction failed")
        return

    # 批量模式
    papers = load_papers()
    if not papers:
        return

    papers = papers[:args.limit] if args.limit else papers
    print(f"   {len(papers)} papers to process")

    success = 0
    skipped = 0
    failed = 0

    for i, paper in enumerate(papers):
        arxiv_id = paper.get("arxiv_id", "")
        title = paper.get("title", "")

        if not arxiv_id:
            continue

        print(f"\n  [{i+1}/{len(papers)}] {arxiv_id}")
        print(f"    {title[:80]}...")

        result = extract_paper(arxiv_id, title, paper.get("abstract", ""),
                              force=args.force)

        if result:
            print(f"    ✅ {result['sections_count']} sections, {result['chars']:,} chars")
            success += 1
        elif CONTENT_RAW_PAPERS.joinpath(f"{arxiv_id}.md").exists():
            print(f"    ⏭ Already extracted")
            skipped += 1
        else:
            print(f"    ❌ Failed")
            failed += 1

        # arXiv 限速：每秒最多 1 请求
        time.sleep(REQUEST_DELAY)

    print(f"\n📊 结果: {success} extracted, {skipped} skipped, {failed} failed")
    print(f"   输出目录: {CONTENT_RAW_PAPERS}")


if __name__ == "__main__":
    main()
