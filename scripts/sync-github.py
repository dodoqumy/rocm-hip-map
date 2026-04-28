#!/usr/bin/env python3
"""sync-github.py — 同步 GitHub Issues/PRs/Discussions 作为情报来源。

从 ROCm 组织仓库拉取：
  - Issues（含 bug/workaround 标签）
  - PRs（重大变更、bugfix）
  - Discussions（社区问答）

输出：
  - data/known-issues.json    结构化 Issue 数据
  - content/raw/english/github_*.md  原始 Issue 正文
  - docs/articles/github/issues/*.md   网站页面

用法：
  python3 scripts/sync-github.py                  # 全量同步
  python3 scripts/sync-github.py --dry-run         # 预览
  python3 scripts/sync-github.py --repo ROCm/ROCm  # 单仓库
"""
import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional
import subprocess

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
KNOWN_ISSUES_JSON = DATA_DIR / "known-issues.json"
CONTENT_RAW_EN = PROJECT_ROOT / "content" / "raw" / "english"

# ── 监控的仓库列表 ─────────────────────────────────
WATCH_REPOS = [
    {
        "org": "ROCm",
        "repo": "ROCm",
        "labels": ["bug", "workaround", "compatibility", "performance"],
    },
    {
        "org": "ROCm",
        "repo": "HIP",
        "labels": ["bug", "question", "documentation"],
    },
    {
        "org": "ROCm",
        "repo": "HIPIFY",
        "labels": ["bug"],
    },
    {
        "org": "ROCm",
        "repo": "pytorch",
        "labels": ["bug", "module: rocm"],
    },
]


def gh_api(path: str, per_page: int = 10) -> Optional[list]:
    """调用 GitHub REST API（公开 repo 无需认证但有速率限制）。"""
    url = f"https://api.github.com/{path}"
    if "?" in url:
        url += f"&per_page={per_page}"
    else:
        url += f"?per_page={per_page}&state=all&sort=updated&direction=desc"

    try:
        result = subprocess.run(
            ["curl", "-s", "--max-time", "30",
             "-H", "Accept: application/vnd.github+json",
             "-H", "User-Agent: rocm-hip-map-sync/1.0",
             url],
            capture_output=True, text=True, timeout=35,
        )
        if result.returncode != 0:
            return None
        data = json.loads(result.stdout)
        if isinstance(data, dict) and "message" in data:
            print(f"  ⚠ API: {data['message']}")
            return None
        return data if isinstance(data, list) else []
    except Exception as e:
        print(f"  ⚠ {e}")
        return None


def load_existing_issues() -> list:
    """加载已有 Issue 数据。"""
    if KNOWN_ISSUES_JSON.exists():
        with open(KNOWN_ISSUES_JSON) as f:
            data = json.load(f)
            return data.get("issues", [])
    return []


def save_issues(issues: list):
    """保存 Issue 数据。"""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(KNOWN_ISSUES_JSON, "w") as f:
        json.dump({"issues": issues, "synced_at": datetime.now(timezone.utc).isoformat()}, f, indent=2)


def extract_hardware(text: str) -> list:
    """从文本中提取 GPU 型号。"""
    gpu_patterns = [
        r"\b(MI300X|MI300|MI250X?|MI210|MI100|MI50)\b",
        r"\b(RX\s*79\d\d\s*XTX?|RX\s*68\d\d|RX\s*69\d\d)\b",
        r"\b(CDNA[123]|RDNA[23])\b",
    ]
    found = set()
    for pattern in gpu_patterns:
        found.update(re.findall(pattern, text, re.IGNORECASE))
    return sorted(found)


def extract_rocm_version(text: str) -> list:
    """从文本中提取 ROCm 版本。"""
    versions = set()
    for m in re.finditer(r"ROCm\s*(\d+\.\d+(?:\.\d+)?)", text, re.IGNORECASE):
        versions.add(m.group(1))
    return sorted(versions)


def sync_repo(org: str, repo: str, labels: list, dry_run: bool = False) -> int:
    """同步单个仓库的 Issues。"""
    print(f"\n🐛 {org}/{repo}")
    count = 0

    # 获取 Issues
    issues = gh_api(f"repos/{org}/{repo}/issues", per_page=20)
    if not issues:
        return 0

    # 筛选带标签的 Issue
    for issue in issues:
        if "pull_request" in issue:  # 跳过 PR（后续单独处理）
            continue

        issue_labels = [l["name"] for l in issue.get("labels", [])]
        has_target_label = any(l in issue_labels for l in labels)

        if not has_target_label and "bug" not in issue_labels:
            continue

        issue_id = f"{org}/{repo}#{issue['number']}"
        print(f"  📋 {issue_id}: {issue['title'][:80]}")

        if dry_run:
            count += 1
            continue

        # 保存为 Markdown
        body = issue.get("body") or "(no description)"
        title = issue["title"]
        md_content = f"""---
title: "{title}"
source_url: {issue['html_url']}
source_type: github-issue
source_org: rocm
published_date: {issue['created_at'][:10]}
credibility: 3
lifecycle: latest
tags: [github-issue, {', '.join(issue_labels[:5])}]
gpu: {json.dumps(extract_hardware(body))}
rocm_versions: {json.dumps(extract_rocm_version(body))}
---

# {title}

> 🐛 **GitHub Issue:** [{issue_id}]({issue['html_url']})
> **状态:** {issue['state']} | **标签:** {', '.join(issue_labels)}
> **创建:** {issue['created_at'][:10]} | **更新:** {issue['updated_at'][:10]}

{body}
"""
        fname = f"github_{org}_{repo}_{issue['number']}.md"
        CONTENT_RAW_EN.mkdir(parents=True, exist_ok=True)
        with open(CONTENT_RAW_EN / fname, "w") as f:
            f.write(md_content)

        count += 1
        time.sleep(2)  # API 速率限制

    return count


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--repo", help="e.g. ROCm/ROCm")
    args = parser.parse_args()

    print("🐛 rocm-hip-map sync-github.py")
    print(f"   {'DRY RUN' if args.dry_run else 'LIVE MODE'}")

    repos = WATCH_REPOS
    if args.repo:
        org, repo = args.repo.split("/")
        repos = [r for r in WATCH_REPOS if r["org"] == org and r["repo"] == repo]

    total = 0
    for r in repos:
        total += sync_repo(r["org"], r["repo"], r["labels"], dry_run=args.dry_run)

    print(f"\n📊 Total issues synced: {total} {'(preview)' if args.dry_run else ''}")


if __name__ == "__main__":
    import re  # needed for extract functions
    main()
