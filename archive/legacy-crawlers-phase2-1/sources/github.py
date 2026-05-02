"""
rocm-hip-map/crawlers/sources/github.py
Phase 2.1.3 — GitHub Issues/PRs 爬虫

数据源：
  - ROCm/ROCm: ~235 open issues
  - ROCm/rocm-libraries: ~877 open issues
  - ROCm/triton: ~83 issues

Token 策略：
  - 有 GITHUB_TOKEN / GH_TOKEN / gh auth token → GraphQL（高效，一次拉取 100 条）
  - 无 token → REST API（每小时 60 次限制，逐条拉取）
"""
from __future__ import annotations

import os
import re
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Iterator, Optional

import httpx

from ..base import BaseCrawler
from ..dedup import normalize_url

LOG = __import__("logging").getLogger(__name__)

# 核心 ROCm 仓库
CORE_REPOS = [
    "ROCm/ROCm",
    "ROCm/rocm-libraries",
    "ROCm/triton",
    "ROCm/hipTensor",
]

# 关键词过滤（包含任一关键词才收录）
KEYWORDS = [
    "hip", "rocblas", "rocfft", "miopen", "tensor",
    "cuda", "gpu", "kernel", "memory", "compute",
    "opencl", " HCC", "hcc", "rocm", "amdgpu",
    "wave32", "wave64", "lds", "vgpr", "gfx",
]


@dataclass
class GitHubIssue:
    number: int
    title: str
    body: str
    state: str
    url: str
    repo: str
    labels: list[str]
    created_at: str
    updated_at: str
    comments: int
    is_pr: bool


def _github_token() -> Optional[str]:
    """获取 GitHub token，优先级：环境变量 > gh CLI。"""
    return (
        os.environ.get("GITHUB_TOKEN")
        or os.environ.get("GH_TOKEN")
        or os.environ.get("GITHUB_TOKEN_HERMES")  # 自定义 key
        or __import__("subprocess").run(
            ["gh", "auth", "token"], capture_output=True, text=True
        ).stdout.strip()
        or None
    )


@dataclass
class GitHubCrawler(BaseCrawler):
    """
    抓取 ROCm GitHub issues/PRs。

    用 GraphQL 批量查询（有 token）或 REST 分页拉取（无 token）。
    """

    repos: list[str] = field(default_factory=lambda: CORE_REPOS.copy())
    token: Optional[str] = field(default_factory=None)
    _session: httpx.Client = field(default=None, repr=False)
    _headers: dict = field(default_factory=dict, repr=False)

    def __post_init__(self):
        self.token = self.token or _github_token()
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "rocm-hip-map-crawler/2.0",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        self._headers = headers
        self._session = httpx.Client(
            headers=headers,
            timeout=httpx.Timeout(30.0),
            follow_redirects=True,
        )

    def __del__(self):
        if hasattr(self, "_session") and self._session:
            self._session.close()

    @property
    def source_id(self) -> str:
        return "github"

    @property
    def source_name(self) -> str:
        return "GitHub Issues & PRs"

    def _rate_limit_remaining(self, resp: httpx.Response) -> int:
        return int(resp.headers.get("X-RateLimit-Remaining", 9999))

    def _check_rate_limit(self, resp: httpx.Response):
        """接近限制时 sleep。"""
        remaining = self._rate_limit_remaining(resp)
        if remaining <= 2:
            reset = int(resp.headers.get("X-RateLimit-Reset", 0))
            wait = max(reset - time.time(), 0) + 1
            LOG.warning("Rate limit low (%d), waiting %.0fs", remaining, wait)
            time.sleep(min(wait, 60))

    def _graphql_query(
        self, query: str, variables: dict, per_page: int = 100
    ) -> list[dict]:
        """GraphQL 查询（有 token 高效路径）。"""
        variables["per_page"] = per_page
        payload = {"query": query, "variables": variables}
        resp = self._session.post(
            "https://api.github.com/graphql",
            json=payload,
        )
        if resp.status_code != 200:
            LOG.error("GraphQL HTTP %d: %s", resp.status_code, resp.text[:200])
            return []
        data = resp.json()
        if "errors" in data:
            LOG.error("GraphQL errors: %s", data["errors"])
            return []
        return data.get("data", {})

    def discover(self) -> Iterator[str]:
        """发现所有目标 issues/PRs URL。"""
        for repo in self.repos:
            LOG.info("Discovering issues in %s", repo)
            if self.token:
                yield from self._discover_graphql(repo)
            else:
                yield from self._discover_rest(repo)

    def _discover_graphql(self, repo: str) -> Iterator[str]:
        """GraphQL 发现（高效，无 60 次/小时限制）。"""
        query = """
        query($owner: String!, $name: String!, $per_page: Int!, $after: String) {
          repository(owner: $owner, name: $name) {
            issues(first: $per_page, after: $after, orderBy: {field: UPDATED_AT, direction: DESC}) {
              pageInfo { hasNextPage endCursor }
              nodes {
                number url state title body createdAt updatedAt
                labels(first: 10) { nodes { name } }
                comments { totalCount }
              }
            }
            pullRequests(first: $per_page, after: $after, orderBy: {field: UPDATED_AT, direction: DESC}) {
              pageInfo { hasNextPage endCursor }
              nodes {
                number url state title body createdAt updatedAt
                labels(first: 10) { nodes { name } }
                comments { totalCount }
              }
            }
          }
        }
        """
        owner, name = repo.split("/")
        after = None
        total = 0

        for _ in range(20):  # 最多 2000 条/仓库
            variables = {"owner": owner, "name": name, "after": after}
            data = self._graphql_query(query, variables)
            issues = data.get("repository", {}).get("issues", {})
            prs = data.get("repository", {}).get("pullRequests", {})

            for node in issues.get("nodes", []):
                if self._filter_keywords(node["title"], node.get("body", "")):
                    url = normalize_url(node["url"])
                    total += 1
                    yield url

            for node in prs.get("nodes", []):
                if self._filter_keywords(node["title"], node.get("body", "")):
                    url = normalize_url(node["url"])
                    total += 1
                    yield url

            page_info = issues.get("pageInfo", {})
            if not page_info.get("hasNextPage"):
                break
            after = page_info["endCursor"]

        LOG.info("%s: yielded %d items", repo, total)

    def _discover_rest(self, repo: str) -> Iterator[str]:
        """REST 发现（无 token，60 次/小时限制）。"""
        page = 1
        total = 0
        while page <= 10:  # 最多 300 条/仓库
            resp = self._session.get(
                f"https://api.github.com/repos/{repo}/issues",
                params={"state": "open", "per_page": 100, "page": page, "sort": "updated"},
            )
            if resp.status_code == 403:
                LOG.warning("Rate limited on %s page %d", repo, page)
                break
            if resp.status_code != 200:
                LOG.error("HTTP %d for %s page %d", resp.status_code, repo, page)
                break

            self._check_rate_limit(resp)
            items = resp.json()
            if not items:
                break

            for item in items:
                if item.get("pull_request"):  # skip PRs (separate endpoint)
                    continue
                title = item.get("title", "")
                body = item.get("body", "") or ""
                if self._filter_keywords(title, body):
                    url = normalize_url(item["html_url"])
                    total += 1
                    yield url

            page += 1
            time.sleep(1.0)  # 无 token：1 req/s 安全限制

        LOG.info("%s: yielded %d items", repo, total)

    def _filter_keywords(self, title: str, body: str) -> bool:
        """标题或正文包含 ROCm/GPU 相关关键词。"""
        text = (title + " " + body).lower()
        return any(kw.lower() in text for kw in KEYWORDS)

    def fetch(self, url: str) -> Optional[bytes]:
        """抓取 issue/PR 原始 HTML。"""
        # 转换 GitHub API URL → HTML URL
        html_url = url
        if "/repos/" in url and not url.endswith("/issues"):
            # API URL 已经是 HTML URL
            pass
        resp = self._session.get(html_url, headers={"Accept": "text/html,application/xhtml+xml"})
        if resp.status_code == 200:
            return resp.content
        LOG.warning("Failed to fetch %s: HTTP %d", html_url, resp.status_code)
        return None

    def parse(self, content: bytes) -> Optional[GitHubIssue]:
        """从 HTML 解析 issue/PR 数据。"""
        from ..extractor import ContentExtractor
        extractor = ContentExtractor()
        parsed = extractor.extract(content, url="https://github.com")

        if not parsed or not parsed.get("text"):
            return None

        # 解析 URL 中的 repo 和 number
        match = re.search(r"github\.com/([^/]+)/([^/]+)/(issues|pull)/(\d+)", parsed.get("url", ""))
        if not match:
            return None

        repo = f"{match.group(1)}/{match.group(2)}"
        number = int(match.group(4))
        is_pr = match.group(3) == "pull"

        # 从 HTML 提取 labels
        labels = []
        label_pattern = re.findall(r'<a[^>]+class="[^"]*IssueLabel[^"]*"[^>]*>([^<]+)<', parsed.get("text", ""))
        if not label_pattern:
            label_pattern = re.findall(r'<span[^>]+class="[^"]*Label[^"]*"[^>]*>([^<]+)<', parsed.get("text", ""))

        return GitHubIssue(
            number=number,
            title=parsed.get("title", "") or "Untitled",
            body=parsed.get("text", ""),
            state="open",
            url=parsed.get("url", ""),
            repo=repo,
            labels=label_pattern,
            created_at=datetime.now(timezone.utc).isoformat(),
            updated_at=datetime.now(timezone.utc).isoformat(),
            comments=0,
            is_pr=is_pr,
        )
