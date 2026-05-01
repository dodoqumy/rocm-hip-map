"""
正文提取器 + HTML→Markdown 转换 (Phase 2.1)
"""

import re
import subprocess
from typing import Optional
import logging

logger = logging.getLogger(__name__)


def is_doxygen_page(html: str) -> bool:
    """识别 doxygen 页面"""
    markers = [
        '<meta name="generator" content="Doxygen',
        'class="doxygen"',
        '<div class="memitem">',
    ]
    return any(marker in html for marker in markers)


def is_js_rendered(html: str) -> bool:
    """识别 JS 渲染页面"""
    if len(html) < 5000 and "noscript" in html:
        return True
    if "Loading application" in html or "Please enable JavaScript" in html:
        return True
    return False


def extract_title(html: str) -> str:
    """从 HTML 提取标题"""
    # <title>
    match = re.search(r"<title>([^<]+)</title>", html, re.IGNORECASE)
    if match:
        title = match.group(1).split("—")[0].split("|")[0].strip()
        return title
    
    # <h1>
    match = re.search(r"<h1[^>]*>([^<]+)</h1>", html, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    
    return ""


def html_to_markdown(html: str, url: str = "") -> Optional[str]:
    """HTML 转 Markdown (使用 pandoc)"""
    # 清理 HTML
    html = clean_html(html)
    
    if not html:
        return None
    
    # 使用 pandoc 转换
    try:
        proc = subprocess.run(
            ["pandoc", "-f", "html", "-t", "markdown", "--wrap=none"],
            input=html,
            capture_output=True,
            text=True,
            timeout=30,
        )
        
        if proc.returncode == 0 and proc.stdout:
            return clean_markdown(proc.stdout)
    except Exception as e:
        logger.warning(f"  ⚠ pandoc failed: {e}")
    
    # Fallback: 简单提取
    return simple_extract(html)


def clean_html(html: str) -> str:
    """清理 HTML"""
    # 移除脚本
    html = re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.DOTALL)
    html = re.sub(r"<style[^>]*>.*?</style>", "", html, flags=re.DOTALL)
    
    # 移除导航栏
    html = re.sub(r"<nav[^>]*>.*?</nav>", "", html, flags=re.DOTALL)
    
    # 移除 footer
    html = re.sub(r"<footer[^>]*>.*?</footer>", "", html, flags=re.DOTALL)
    
    # 移除 version warning
    html = re.sub(r'<div class="[^"]*version-warning[^"]*".*?</div>', "", html, flags=re.DOTALL)
    
    return html


def simple_extract(html: str) -> Optional[str]:
    """简单提取 (fallback)"""
    # 提取 main 内容
    match = re.search(r"<main[^>]*>(.*?)</main>", html, re.DOTALL)
    if match:
        content = match.group(1)
    else:
        # 提取 body
        match = re.search(r"<body[^>]*>(.*?)</body>", html, re.DOTALL)
        if match:
            content = match.group(1)
        else:
            content = html
    
    # 移除 HTML 标签
    content = re.sub(r"<[^>]+>", "", content)
    
    # 解码 HTML 实体
    content = content.replace("&nbsp;", " ")
    content = content.replace("&lt;", "<")
    content = content.replace("&gt;", ">")
    content = content.replace("&amp;", "&")
    
    # 清理空白
    lines = [line.strip() for line in content.split("\n") if line.strip()]
    
    return "\n\n".join(lines)


def clean_markdown(md: str) -> str:
    """清理 Markdown"""
    if not md:
        return ""
    
    # 移除版本切换器
    md = re.sub(r"##\s*Other versions.*", "", md)
    md = re.sub(r"##\s*Download.*", "", md)
    md = re.sub(r"##\s*Table of contents.*", "", md)
    md = re.sub(r"##\s*On this page.*", "", md)
    
    # 移除 pandoc 块标记
    md = re.sub(r":::\{[^}]+\}", "", md)
    md = re.sub(r":::(\s|$)", "\n", md)
    md = re.sub(r"^:::\s*$", "", md, flags=re.MULTILINE)
    
    # 移除导航链接
    md = re.sub(r"\[Skip to main content\]\([^)]+\)", "", md)
    md = re.sub(r"\[¶\].*?Skip to main content", "", md)
    md = re.sub(r"Skip to main content", "", md)
    
    # 移除空行
    while "\n\n\n" in md:
        md = md.replace("\n\n\n", "\n\n")
    
    # 移除开头空行
    md = md.strip()
    
    return md


class ContentExtractor:
    """正文提取器"""
    
    def __init__(self):
        self._trafilatura_available = self._check_trafilatura()
        self._pandoc_available = self._check_pandoc()
    
    def _check_trafilatura(self) -> bool:
        try:
            import trafilatura
            return True
        except ImportError:
            return False
    
    def _check_pandoc(self) -> bool:
        try:
            subprocess.run(["pandoc", "--version"], capture_output=True, timeout=5)
            return True
        except:
            return False
    
    def extract(self, html: str, url: str = "") -> Optional[str]:
        """提取正文"""
        if is_doxygen_page(html):
            logger.debug(f"  🔧 Doxygen page: {url}")
            return None
        
        if is_js_rendered(html):
            logger.warning(f"  ⚠ JS rendered: {url}")
            return None
        
        # 使用 pandoc
        if self._pandoc_available:
            md = html_to_markdown(html, url)
            if md and len(md) > 200:
                return md
        
        # 使用 trafilatura
        if self._trafilatura_available:
            try:
                import trafilatura
                result = trafilatura.extract(
                    html,
                    output_format="markdown",
                    include_links=True,
                    include_tables=True,
                )
                if result and len(result) > 200:
                    return clean_markdown(result)
            except Exception as e:
                logger.warning(f"  ⚠ trafilatura failed: {e}")
        
        # Fallback: 简单提取
        return simple_extract(html)