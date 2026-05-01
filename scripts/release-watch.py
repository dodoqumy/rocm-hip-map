#!/usr/bin/env python3
"""release-watch.py — 监控 ROCm/HIP/PyTorch 版本更新 (v1.5)。

监控目标：
  - ROCm 版本历史页 → 检测新版本
  - HIP GitHub releases
  - ROCm 核心库 releases (MIOpen, RCCL, rocBLAS, etc.)
  - PyTorch ROCm 版本

检测到新版本时：
  1. 输出到 stdout
  2. 写入 data/versions.json

用法：
  python3 scripts/release-watch.py            # 检查更新
  python3 scripts/release-watch.py --verbose   # 详细输出
"""
import argparse
import json
import re
import sys
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
VERSIONS_JSON = DATA_DIR / "versions.json"

# ── 扩展的版本源列表 ──────────────────────────────────────
VERSION_REPOS = [
    {"org": "ROCm", "repo": "ROCm", "product": "ROCm"},
    {"org": "ROCm", "repo": "HIP", "product": "HIP"},
    {"org": "ROCm", "repo": "MIOpen", "product": "MIOpen"},
    {"org": "ROCm", "repo": "RCCL", "product": "RCCL"},
    {"org": "ROCm", "repo": "rocBLAS", "product": "rocBLAS"},
    {"org": "ROCm", "repo": "rocFFT", "product": "rocFFT"},
    {"org": "ROCm", "repo": "rocSOLVER", "product": "rocSOLVER"},
    {"org": "ROCm", "repo": "rocSparse", "product": "rocSparse"},
]


def fetch_url(url: str) -> Optional[str]:
    """抓取 URL。"""
    try:
        result = subprocess.run(
            ["curl", "-sL", "--max-time", "30",
             "-H", "User-Agent: rocm-hip-map-release-watch/1.0",
             url],
            capture_output=True, text=True, timeout=35,
        )
        return result.stdout if result.returncode == 0 else None
    except Exception:
        return None


def check_rocm_versions() -> list:
    """检查 ROCm 版本页面。"""
    url = "https://rocm.docs.amd.com/en/latest/release/versions.html"
    html = fetch_url(url)
    if not html:
        print("⚠ Cannot fetch ROCm versions page")
        return []

    # Extract version numbers from the page
    # Pattern: rows like "7.2.2 | April 14, 2026"
    versions = []
    for m in re.finditer(r'(\d+\.\d+\.\d+)\s*\|\s*([A-Z][a-z]+ \d{1,2}, \d{4})', html):
        versions.append({
            "product": "ROCm",
            "version": m.group(1),
            "release_date": m.group(2),
            "source": url,
        })

    return versions


def check_hip_releases() -> list:
    """检查 HIP GitHub releases。"""
    releases = gh_api("repos/ROCm/HIP/releases", per_page=5)
    results = []
    for rel in (releases or []):
        results.append({
            "product": "HIP",
            "version": rel.get("tag_name", "").lstrip("rocm-").lstrip("v"),
            "release_date": rel.get("published_at", "")[:10],
            "source": rel.get("html_url", ""),
        })
    return results


def check_github_releases(org: str, repo: str, product: str) -> list:
    """检查任意 GitHub 仓库的 releases。"""
    releases = gh_api(f"repos/{org}/{repo}/releases", per_page=10)
    results = []
    for rel in (releases or []):
        tag = rel.get("tag_name", "")
        results.append({
            "product": product,
            "version": tag.lstrip("rocm-").lstrip("v").lstrip(product.lower() + "-") if tag else "",
            "release_date": rel.get("published_at", "")[:10],
            "source": rel.get("html_url", ""),
        })
    return results


def gh_api(path: str, per_page: int = 5) -> Optional[list]:
    """调用 GitHub API。"""
    url = f"https://api.github.com/{path}?per_page={per_page}"
    try:
        result = subprocess.run(
            ["curl", "-s", "--max-time", "20",
             "-H", "Accept: application/vnd.github+json",
             "-H", "User-Agent: rocm-hip-map/1.0",
             url],
            capture_output=True, text=True, timeout=25,
        )
        if result.returncode != 0:
            return None
        data = json.loads(result.stdout)
        if isinstance(data, dict) and "message" in data:
            return None
        return data if isinstance(data, list) else []
    except Exception:
        return None


def load_known_versions() -> dict:
    """加载已知版本。"""
    if VERSIONS_JSON.exists():
        with open(VERSIONS_JSON) as f:
            data = json.load(f)
            # Ensure products key exists
            if "products" not in data:
                data["products"] = {}
            return data
    return {"products": {}, "last_check": None}


def save_versions(data: dict):
    """保存版本数据。"""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    data["last_check"] = datetime.now(timezone.utc).isoformat()
    with open(VERSIONS_JSON, "w") as f:
        json.dump(data, f, indent=2)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", "-v", action="store_true", help="详细输出")
    args = parser.parse_args()

    print("🔔 rocm-hip-map release-watch.py (v1.5)")
    known = load_known_versions()

    new_versions = []

    # Check ROCm docs versions
    rocm_versions = check_rocm_versions()
    known_rocm = known.get("products", {}).get("ROCm", [])
    known_rocm_strs = {v for v in known_rocm}

    for v in rocm_versions:
        ver = v["version"]
        if ver not in known_rocm_strs:
            print(f"  🆕 ROCm {ver} ({v['release_date']})")
            new_versions.append(v)
        elif args.verbose:
            print(f"  ⏭ ROCm {ver}")

    # Check all GitHub repos
    for repo_info in VERSION_REPOS:
        org, repo, product = repo_info["org"], repo_info["repo"], repo_info["product"]
        releases = check_github_releases(org, repo, product)
        known_prod = known.get("products", {}).get(product, [])
        known_strs = {v for v in known_prod}

        for v in releases:
            ver = v["version"]
            if ver and ver not in known_strs:
                print(f"  🆕 {product} {ver} ({v['release_date']})")
                new_versions.append(v)
            elif args.verbose and ver:
                print(f"  ⏭ {product} {ver}")

        # Update known
        known["products"][product] = [v["version"] for v in releases if v["version"]]

    # Update ROCm docs versions separately
    known["products"]["ROCm"] = [v["version"] for v in rocm_versions]
    save_versions(known)

    if not new_versions:
        print("  ✅ No new versions detected")
    else:
        print(f"\n📊 {len(new_versions)} new version(s) detected!")

    print(f"   Last check: {known['last_check']}")


if __name__ == "__main__":
    main()
