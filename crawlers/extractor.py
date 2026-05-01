"""
rocm-hip-map/crawlers/extractor.py
Phase 2.1.1 — 正文提取器

策略（按优先级）：
1. trafilatura（最佳正文 + 元信息）
2. selectolax（快速 HTML 解析）
3. stdlib html.parser（兜底）
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Optional

try:
    import trafilatura
    _HAS_TRAFILATURA = True
except ImportError:
    _HAS_TRAFILATURA = False

try:
    from selectolax.parser import HTMLParser
    from selectolax.tree import Node
    _HAS_SELECTOLAX = True
except ImportError:
    _HAS_SELECTOLAX = False


@dataclass
class ExtractedContent:
    """提取结果。"""
    title: str
    body: str
    excerpt: str
    author: str
    published_at: str
    language: str


def extract(html: bytes | str, url: str = "") -> ExtractedContent:
    """
    从 HTML 中提取正文 + 元信息。

    使用最佳可用库。
    """
    if isinstance(html, bytes):
        html = html.decode("utf-8", errors="replace")

    # 策略 1：trafilatura（最好效果）
    if _HAS_TRAFILATURA:
        result = trafilatura.extract(
            html,
            url=url,
            include_comments=False,
            include_tables=True,
            include_images=False,
            output_format="json",
            with_metadata=True,
        )
        if result:
            import json
            meta = json.loads(result)
            return ExtractedContent(
                title=meta.get("title", ""),
                body=meta.get("text", ""),
                excerpt=meta.get("description", "") or _make_excerpt(meta.get("text", "")),
                author=meta.get("author", "") or meta.get("authors", ""),
                published_at=meta.get("date", "") or meta.get("published", ""),
                language=meta.get("language", "en"),
            )

    # 策略 2：selectolax（快速提取 title + 正文）
    if _HAS_SELECTOLAX:
        return _extract_selectolax(html)

    # 策略 3：stdlib（兜底）
    return _extract_stdlib(html)


def _extract_selectolax(html: str) -> ExtractedContent:
    """用 selectolax 提取 title + 正文段落。"""
    tree = HTMLParser(html)

    title = ""
    title_el = tree.css_first("title")
    if title_el:
        title = title_el.text()

    # 常见正文容器
    for sel in ["article", "main", '[role="main"]', ".content", "#content"]:
        el = tree.css_first(sel)
        if el and len(el.text()) > 200:
            body = _extract_paragraphs(el)
            if body:
                return ExtractedContent(
                    title=title,
                    body=body,
                    excerpt=_make_excerpt(body),
                    author="",
                    published_at="",
                    language=_detect_lang(body),
                )

    # 最后兜底：整个 body
    body_el = tree.css_first("body")
    if body_el:
        return ExtractedContent(
            title=title,
            body=_extract_paragraphs(body_el),
            excerpt=_make_excerpt(body),
            author="",
            published_at="",
            language=_detect_lang(body),
        )

    return ExtractedContent(title=title, body="", excerpt="",
                           author="", published_at="", language="en")


def _extract_paragraphs(node: "Node") -> str:
    """从节点提取可读段落。"""
    lines = []
    for el in node.css("p, h1, h2, h3, h4, li, pre, blockquote"):
        text = el.text().strip()
        if len(text) > 30:  # 过滤噪音
            lines.append(text)
    return "\n\n".join(lines)


def _extract_stdlib(html: str) -> ExtractedContent:
    """纯 stdlib 提取（无任何外部依赖）。"""
    from html.parser import HTMLParser
    import html as html_module

    class TextExtractor(HTMLParser):
        def __init__(self):
            super().__init__()
            self.title = ""
            self.body_parts = []
            self.in_title = False
            self.in_body = False
            self._skip_tags = {"script", "style", "nav", "header", "footer", "aside"}

        def handle_starttag(self, tag, attrs):
            if tag == "title":
                self.in_title = True
            elif tag == "body":
                self.in_body = True
            elif tag in self._skip_tags:
                pass

        def handle_endtag(self, tag):
            if tag == "title":
                self.in_title = False
            elif tag == "body":
                self.in_body = False

        def handle_data(self, data: str):
            text = data.strip()
            if not text:
                return
            if self.in_title:
                self.title = text
            elif self.in_body:
                self.body_parts.append(text)

    parser = TextExtractor()
    try:
        parser.feed(html)
    except Exception:
        pass

    body = "\n\n".join(parser.body_parts)
    return ExtractedContent(
        title=parser.title or "",
        body=body,
        excerpt=_make_excerpt(body),
        author="",
        published_at="",
        language=_detect_lang(body),
    )


def _make_excerpt(text: str, length: int = 200) -> str:
    """生成摘要。"""
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= length:
        return text
    return text[:length].rsplit(" ", 1)[0] + "…"


def _detect_lang(text: str) -> str:
    """简单语言检测（中/英）。"""
    if re.search(r"[\u4e00-\u9fff]", text):
        return "zh"
    return "en"
