"""
rocm-hip-map/crawlers/sources/third_party.py
Phase 2.1.4 — 第三方来源爬虫（Phoronix / Reddit / arXiv / Hacker News）

每个爬虫独立实现 discover()。
"""
from __future__ import annotations

import re
import time
from typing import Iterator

import httpx

from ..base import BaseCrawler
from ..dedup import normalize_url


# ═══════════════════════════════════════════════════════════
# 1. Phoronix — AMD/ROCm 评测文章
# ═══════════════════════════════════════════════════════════
class PhoronixCrawler(BaseCrawler):
    """PhoronixTestSuite 评测 + AMD GPU 文章。"""

    SOURCE_ID = "phoronix"
    SOURCE_NAME = "Phoronix / OpenBenchmarking"

    SEARCHES = [
        "https://www.phoronix.com/search.php?q=ROCm",
        "https://www.phoronix.com/search.php?q=AMD+GPU",
        "https://www.phoronix.com/search.php?q=radeon",
    ]

    @property
    def source_id(self) -> str:
        return self.SOURCE_ID

    @property
    def source_name(self) -> str:
        return self.SOURCE_NAME

    def discover(self) -> Iterator[str]:
        seen = set()
        for search_url in self.SEARCHES:
            resp = self._http.fetch(search_url)
            if not resp.ok:
                continue
            # 从搜索结果页提取文章链接
            links = re.findall(r'href="(/show[^"?]+)"', resp.text)
            for link in links[:30]:  # 最多 30 篇/搜索词
                url = normalize_url("https://www.phoronix.com" + link)
                if url not in seen:
                    seen.add(url)
                    yield url
            time.sleep(1)

    def fetch(self, url: str):
        resp = self._http.fetch(url)
        return resp.content if resp.ok else None

    def parse(self, content: bytes):
        from ..extractor import ContentExtractor
        extractor = ContentExtractor()
        return extractor.extract(content, url="https://www.phoronix.com")


# ═══════════════════════════════════════════════════════════
# 2. Reddit — r/ROCm / r/AMD / r/hardware 帖子
# ═══════════════════════════════════════════════════════════
class RedditCrawler(BaseCrawler):
    """从 Reddit API 拉取 ROCm 相关帖子。"""

    SOURCE_ID = "reddit"
    SOURCE_NAME = "Reddit Communities"

    SUBREDDITS = ["ROCm", "AMD", "hardware", "hardware", "Programmer"]

    @property
    def source_id(self) -> str:
        return self.SOURCE_ID

    @property
    def source_name(self) -> str:
        return self.SOURCE_NAME

    def discover(self) -> Iterator[str]:
        seen = set()
        for sub in self.SUBREDDITS:
            url = f"https://www.reddit.com/r/{sub}/search.json?q=ROCm+OR+hip+OR+AMD+gpu&restrict_sr=1&sort=top&limit=100"
            resp = self._http.fetch(url)
            if not resp.ok:
                continue
            import json
            try:
                data = json.loads(resp.text)
                children = data.get("data", {}).get("children", [])
                for child in children:
                    post_url = child.get("data", {}).get("url", "")
                    if post_url and post_url.startswith("http"):
                        norm = normalize_url(post_url)
                        if norm not in seen:
                            seen.add(norm)
                            yield norm
            except (json.JSONDecodeError, KeyError):
                pass
            time.sleep(1)

    def fetch(self, url: str):
        resp = self._http.fetch(url)
        return resp.content if resp.ok else None

    def parse(self, content: bytes):
        from ..extractor import ContentExtractor
        return ContentExtractor().extract(content, url="https://reddit.com")


# ═══════════════════════════════════════════════════════════
# 3. arXiv — GPU / HIP / CUDA 学术论文
# ═══════════════════════════════════════════════════════════
class ArxivCrawler(BaseCrawler):
    """从 arXiv 搜索 HIP/GPU 相关学术论文。"""

    SOURCE_ID = "arxiv"
    SOURCE_NAME = "arXiv Academic Papers"

    QUERIES = [
        "ti:ROCm OR ti:HIP+GPU",
        "ti:AMD+GPU+kernel",
        "abs:parallel+compute+GPU",
    ]

    BASE_URL = "http://export.arxiv.org/api/query?"

    @property
    def source_id(self) -> str:
        return self.SOURCE_ID

    @property
    def source_name(self) -> str:
        return self.SOURCE_NAME

    def discover(self) -> Iterator[str]:
        seen = set()
        import xml.etree.ElementTree as ET

        for query in self.QUERIES:
            url = self.BASE_URL + f"search_query={query}&start=0&max_results=50&sortBy=submittedDate&sortOrder=descending"
            resp = self._http.fetch(url)
            if not resp.ok:
                continue

            try:
                root = ET.fromstring(resp.content)
                # 尝试 ATOM namespace，无则视为无 namespace
                for entry in root.findall("{http://www.w3.org/2005/Atom}entry") or root.findall("entry"):
                    link = entry.find("{http://www.w3.org/2005/Atom}link") or entry.find("link")
                    if link is not None:
                        href = link.get("href", "")
                        if href and href not in seen:
                            seen.add(href)
                            yield href
            except ET.ParseError:
                pass
            time.sleep(3)

    def fetch(self, url: str):
        resp = self._http.fetch(url)
        return resp.content if resp.ok else None

    def parse(self, content: bytes):
        import xml.etree.ElementTree as ET
        try:
            root = ET.fromstring(content)
            entry = root.find("{http://www.w3.org/2005/Atom}entry") or root.find("entry") or root
            title_el = entry.find("{http://www.w3.org/2005/Atom}title") or entry.find("title")
            summary_el = entry.find("{http://www.w3.org/2005/Atom}summary") or entry.find("summary")
            title = title_el.text.strip() if title_el is not None and title_el.text else ""
            summary = summary_el.text.strip() if summary_el is not None and summary_el.text else ""

            def get_author(a):
                n = a.find("{http://www.w3.org/2005/Atom}name") or a.find("name")
                return n.text if n is not None and n.text else ""

            authors = [get_author(a) for a in
                entry.findall("{http://www.w3.org/2005/Atom}author") or entry.findall("author")]

            return {
                "title": title,
                "text": summary,
                "url": "",
                "authors": [a for a in authors if a],
            }
        except ET.ParseError:
            return None


# ═══════════════════════════════════════════════════════════
# 4. Hacker News — HIP / ROCm / GPU 技术讨论
# ═══════════════════════════════════════════════════════════
class HackerNewsCrawler(BaseCrawler):
    """从 Hacker News API 搜索 GPU/HIP 相关讨论。"""

    SOURCE_ID = "hackernews"
    SOURCE_NAME = "Hacker News"

    HN_API = "https://hacker-news.firebaseio.com/v0"

    KEYWORDS = ["ROCm", "HIP", "AMD GPU", "CUDA", "GPU kernel"]

    @property
    def source_id(self) -> str:
        return self.SOURCE_ID

    @property
    def source_name(self) -> str:
        return self.SOURCE_NAME

    def discover(self) -> Iterator[str]:
        seen = set()
        # 拉最新 1000 条，找关键词匹配
        resp = self._http.fetch(f"{self.HN_API}/topstories.json")
        if not resp.ok:
            return
        import json
        try:
            story_ids = json.loads(resp.text)[:500]  # 最近 500 条
        except json.JSONDecodeError:
            return

        for sid in story_ids:
            item_resp = self._http.fetch(f"{self.HN_API}/item/{sid}.json")
            if not item_resp.ok:
                continue
            try:
                story = json.loads(item_resp.text)
            except json.JSONDecodeError:
                continue

            title = story.get("title", "") or ""
            if any(kw.lower() in title.lower() for kw in self.KEYWORDS):
                url = story.get("url") or f"https://news.ycombinator.com/item?id={sid}"
                norm = normalize_url(url)
                if norm not in seen:
                    seen.add(norm)
                    yield norm
            time.sleep(0.1)

    def fetch(self, url: str):
        resp = self._http.fetch(url)
        return resp.content if resp.ok else None

    def parse(self, content: bytes):
        from ..extractor import ContentExtractor
        return ContentExtractor().extract(content, url="https://news.ycombinator.com")
