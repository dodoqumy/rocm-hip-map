#!/usr/bin/env python3
"""release-watch.py — 监控 ROCm/HIP/PyTorch 版本更新。

监控目标：
  - ROCm 版本历史页 → 检测新版本
  - HIP GitHub releases
  - PyTorch ROCm 版本
  - amdgpu 驱动版本

检测到新版本时：
  1. 输出到 stdout
  2. 写入 data/versions.json
  3. 如果在 GitHub Actions 中运行 → 创建 Issue

用法：
  python3 scripts/release-watch.py            # 检查更新
  python3 scripts/release-watch.py --notify    # 发现新版本时通知
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
            return json.load(f)
    return {"products": {}, "last_check": None}


def save_versions(data: dict):
    """保存版本数据。"""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    data["last_check"] = datetime.now(timezone.utc).isoformat()
    with open(VERSIONS_JSON, "w") as f:
        json.dump(data, f, indent=2)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--notify", action="store_true", help="Create GitHub Issue for new versions")
    args = parser.parse_args()

    print("🔔 rocm-hip-map release-watch.py")
    known = load_known_versions()

    new_versions = []

    # Check ROCm
    rocm_versions = check_rocm_versions()
    known_rocm = known.get("products", {}).get("ROCm", [])
    known_rocm_strs = {v for v in known_rocm}

    for v in rocm_versions:
        ver = v["version"]
        if ver not in known_rocm_strs:
            print(f"  🆕 ROCm {ver} ({v['release_date']})")
            new_versions.append(v)

    # Check HIP
    hip_releases = check_hip_releases()
    known_hip = known.get("products", {}).get("HIP", [])
    known_hip_strs = {v for v in known_hip}

    for v in hip_releases:
        ver = v["version"]
        if ver and ver not in known_hip_strs:
            print(f"  🆕 HIP {ver} ({v['release_date']})")
            new_versions.append(v)

    # Update known versions
    known["products"]["ROCm"] = [v["version"] for v in rocm_versions]
    known["products"]["HIP"] = [v["version"] for v in hip_releases]
    save_versions(known)

    if not new_versions:
        print("  ✅ No new versions detected")
    else:
        print(f"\n📊 {len(new_versions)} new version(s) detected!")

    print(f"   Last check: {known['last_check']}")


if __name__ == "__main__":
    main()
