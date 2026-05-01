#!/usr/bin/env python3
"""
正文提取器 + HTML→Markdown 转换 (Phase 2.1)
优先 trafilatura，降级 pandoc + 简单提取
"""

import re
import subprocess
import sys
import os
from typing import Optional
import logging

logger = logging.getLogger(__name__)

# 优先导入 trafilatura（必须在 httpx 等依赖之前，避免 lxml 路径冲突）
_TRAFILATURA_OK = False
try:
    import trafilatura  # noqa: F401
    _TRAFILATURA_OK = True
except ImportError:
    pass


def is_doxygen_page(html: str) -> bool:
    """识别 doxygen 页面（API 文档，不需要提取）"""
    markers = [
        '<meta name="generator" content="Doxygen',
        'class="doxygen"',
        '<div class="memitem">',
        '/doxygen/html/',
    ]
    return any(marker in html for marker in markers)


def is_js_rendered(html: str) -> bool:
    """识别 JS 渲染页面（无法提取）"""
    if len(html) < 5000 and "noscript" in html:
        return True
    if "Loading application" in html or "Please enable JavaScript" in html:
        return True
    return False


def extract_title(html: str) -> str:
    """从 HTML 提取标题"""
    match = re.search(r"<title>([^<]+)</title>", html, re.IGNORECASE)
    if match:
        title = match.group(1).split("—")[0].split("|")[0].strip()
        return title
    match = re.search(r"<h1[^>]*>([^<]+)</h1>", html, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return ""


def _try_trafilatura(html: str) -> Optional[str]:
    """用 trafilatura 提取（首选）"""
    try:
        import trafilatura
        result = trafilatura.extract(
            html,
            output_format='markdown',
            include_links=True,
            include_tables=True,
            include_images=False,
            favor_precision=True,
        )
        if result and len(result) > 200:
            return result
    except ImportError:
        pass
    except Exception as e:
        logger.debug(f"trafilatura failed: {e}")
    return None


def _try_pandoc(html: str) -> Optional[str]:
    """用 pandoc 提取（备选）"""
    try:
        # 预处理 HTML：移除明显噪音
        html = _preclean_html(html)
        if not html or len(html) < 100:
            return None

        proc = subprocess.run(
            ["pandoc", "-f", "html", "-t", "markdown", "--wrap=none", "-s"],
            input=html,
            capture_output=True,
            text=True,
            timeout=30,
        )
        if proc.returncode == 0 and len(proc.stdout) > 200:
            return _postclean_markdown(proc.stdout)
    except Exception as e:
        logger.debug(f"pandoc failed: {e}")
    return None


def _preclean_html(html: str) -> str:
    """HTML 预处理：移除脚本/样式/导航"""
    # 移除脚本、样式
    html = re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.DOTALL)
    html = re.sub(r"<style[^>]*>.*?</style>", "", html, flags=re.DOTALL)

    # 移除 nav/footer
    html = re.sub(r"<nav[^>]*>.*?</nav>", "", html, flags=re.DOTALL)
    html = re.sub(r"<footer[^>]*>.*?</footer>", "", html, flags=re.DOTALL)

    # 移除版本警告
    html = re.sub(r'<div[^>]*class="[^"]*version-warning[^"]*"[^>]*>.*?</div>', "", html, flags=re.DOTALL)

    # 提取 main/article 主体（减少噪音）
    for pattern in [
        r'<main[^>]*>(.*?)</main>',
        r'<article[^>]*>(.*?)</article>',
        r'<div[^>]*id="main-content"[^>]*>(.*?)</div>\s*(?:</div>\s*){3,}',
    ]:
        m = re.search(pattern, html, re.DOTALL)
        if m and len(m.group(1)) > 500:
            return m.group(1)

    return html


def _postclean_markdown(md: str) -> str:
    """Markdown 后处理：移除 Sphinx/CSS 噪音"""
    if not md:
        return ""

    # 移除 pandoc 块级 div 标记
    md = re.sub(r'^:::\{[^}]+\}\s*$', '', md, flags=re.MULTILINE)
    md = re.sub(r'^:::\{[^}]+\}', '', md, flags=re.MULTILINE)
    md = re.sub(r'^:::\s*$', '', md, flags=re.MULTILINE)
    md = re.sub(r'^::::\s*$', '', md, flags=re.MULTILINE)

    # 移除 Sphinx 内部链接标记
    md = re.sub(r'\[\^\d+\]\s*', '', md)
    md = re.sub(r'\[¶\]\([^)]+\)\s*"[^"]*"\s*', '', md)
    md = re.sub(r'\[[#]?\^?\w+\]\([^)]+\)\s*\{[^}]*\}\s*', '', md)

    # 移除纯装饰性符号行（5个以上连续符号）
    lines = [l for l in md.split('\n')
             if not re.match(r'^[:=_#*.-|]{5,}$', l.strip())]
    md = '\n'.join(lines)

    # 移除连续空行
    while '\n\n\n' in md:
        md = md.replace('\n\n\n', '\n\n')

    return md.strip()


def _simple_extract(html: str) -> Optional[str]:
    """简单提取（最终 fallback）"""
    match = re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL)
    if not match:
        match = re.search(r'<body[^>]*>(.*?)</body>', html, re.DOTALL)
    content = match.group(1) if match else html

    # 移除标签
    content = re.sub(r"<[^>]+>", "", content)
    content = content.replace("&nbsp;", " ").replace("&lt;", "<")
    content = content.replace("&gt;", ">").replace("&amp;", "&")
    content = content.replace("&quot;", '"').replace("&#39;", "'")

    lines = [l.strip() for l in content.split("\n") if l.strip()]
    return "\n\n".join(lines) if lines else None


class ContentExtractor:
    """正文提取器"""

    def __init__(self):
        self._trafilatura_ok = _TRAFILATURA_OK
        self._pandoc_ok = self._check_pandoc()

    def _check_pandoc(self) -> bool:
        try:
            subprocess.run(["pandoc", "--version"], capture_output=True, timeout=5)
            return True
        except Exception:
            return False

    def extract(self, html: str, url: str = "") -> Optional[str]:
        """提取正文，按优先级尝试"""
        # Doxygen/API 页面直接跳过
        if is_doxygen_page(html):
            logger.debug(f"  🔧 Doxygen page skipped: {url}")
            return None

        if is_js_rendered(html):
            logger.warning(f"  ⚠ JS rendered page: {url}")
            return None

        # 1. trafilatura（最干净）
        if self._trafilatura_ok:
            result = _try_trafilatura(html)
            if result:
                logger.debug(f"  ✅ trafilatura: {len(result)} chars")
                return result

        # 2. pandoc（保留表格/代码）
        if self._pandoc_ok:
            result = _try_pandoc(html)
            if result:
                logger.debug(f"  ✅ pandoc: {len(result)} chars")
                return result

        # 3. 简单提取（最后兜底）
        result = _simple_extract(html)
        if result:
            logger.debug(f"  ⚠ simple fallback: {len(result)} chars")
            return result

        return None
