#!/usr/bin/env python3
"""classify.py — 自动分类 + 打标签。

扫描 content/raw/ 中的文章，根据内容自动判定：
  - os: 检测操作系统关键词
  - gpu: 检测 GPU 型号
  - gpu_arch: 检测架构关键词
  - driver: 检测驱动版本
  - frameworks: 检测框架关键词
  - difficulty: 根据文章长度和关键词推断
  - tags: 主题标签

输出：
  - data/articles.json    更新后的文章索引
  - 各文章的 frontmatter 注入标签

用法：
  python3 scripts/classify.py
  python3 scripts/classify.py --dry-run
"""
import argparse
import json
import re
from pathlib import Path
from datetime import datetime, timezone
from typing import List, Set

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONTENT_RAW_EN = PROJECT_ROOT / "content" / "raw" / "english"
CONTENT_RAW_ZH = PROJECT_ROOT / "content" / "raw" / "chinese"
DATA_DIR = PROJECT_ROOT / "data"
TAGS_JSON = DATA_DIR / "tags.json"
ARTICLES_JSON = DATA_DIR / "articles.json"


# ── 分类规则 ────────────────────────────────────────
CLASSIFICATION_RULES = {
    "os": {
        "linux": [r"\blinux\b", r"\bubuntu\b", r"\bdebian\b", r"\brhel\b", r"\bcentos\b", r"\bfedora\b", r"\barch\b", r"\bsles\b"],
        "windows": [r"\bwindows\b", r"\bwin10\b", r"\bwin11\b"],
        "wsl2": [r"\bwsl2?\b", r"\bwindows subsystem\b"],
        "docker": [r"\bdocker\b", r"\bcontainer\b"],
    },
    "gpu": {
        "mi300x": [r"\bmi\s*300\s*x\b", r"\bmi300x\b"],
        "mi250x": [r"\bmi\s*250\s*x\b", r"\bmi250x\b"],
        "mi250": [r"\bmi\s*250\b(?!\s*x)", r"\bmi250\b(?!x)"],
        "mi210": [r"\bmi\s*210\b", r"\bmi210\b"],
        "mi100": [r"\bmi\s*100\b", r"\bmi100\b"],
        "mi50": [r"\bmi\s*50\b", r"\bmi50\b"],
        "rx7900xtx": [r"\brx\s*7900\s*xtx\b"],
        "rx7900": [r"\brx\s*7900\b(?!\s*xtx)"],
        "rx6800": [r"\brx\s*68\d\d\b"],
        "rx6900": [r"\brx\s*69\d\d\b"],
    },
    "gpu_arch": {
        "cdna3": [r"\bcdna\s*3\b", r"\bcdna3\b"],
        "cdna2": [r"\bcdna\s*2\b", r"\bcdna2\b"],
        "cdna1": [r"\bcdna\s*1\b", r"\bcdna1\b"],
        "rdna3": [r"\brdna\s*3\b", r"\brdna3\b"],
        "rdna2": [r"\brdna\s*2\b", r"\brdna2\b"],
    },
    "driver": {
        "amdgpu-6.x": [r"\bamdgpu\s*6\.", r"\bROCr?\s*6\.", r"\brocm\s*6\.\d"],
        "amdgpu-5.x": [r"\bamdgpu\s*5\.", r"\bROCr?\s*5\.", r"\brocm\s*5\.\d"],
    },
    "frameworks": {
        "pytorch": [r"\bpytorch\b", r"\btorch\b"],
        "tensorflow": [r"\btensorflow\b", r"\btf\b"],
        "jax": [r"\bjax\b"],
        "paddle": [r"\bpaddle\b"],
        "onnx": [r"\bonnx\b"],
    },
    "tags_extra": {
        "install": [r"\binstall\b", r"\bsetup\b", r"\bconfigure\b", r"\bapt\b.*\binstall\b"],
        "performance": [r"\bperformance\b", r"\boptimization\b", r"\btuning\b", r"\bthroughput\b"],
        "debugging": [r"\bdebug\b", r"\btroubleshoot\b", r"\berror\b.*\bfix\b"],
        "compatibility": [r"\bcompatib\b", r"\bsupport\b.*\bmatrix\b"],
        "container": [r"\bdocker\b", r"\bcontainer\b", r"\bkubernetes\b"],
    },
}


def classify_text(text: str) -> dict:
    """对文本进行分类，返回标签字典。"""
    result = {}
    text_lower = text.lower()

    for category, rules in CLASSIFICATION_RULES.items():
        matched = []
        for tag, patterns in rules.items():
            for pattern in patterns:
                if re.search(pattern, text_lower):
                    matched.append(tag)
                    break
        if matched:
            result[category] = sorted(set(matched))

    return result


def infer_difficulty(text: str, char_count: int) -> str:
    """推断难度等级。"""
    advanced_keywords = ["advanced", "optimization", "profiling", "assembly",
                         "intrinsic", "pipeline", "wavefront", "memory coalescing"]
    beginner_keywords = ["introduction", "getting started", "overview", "quick start",
                         "beginner", "tutorial", "basic"]

    lower = text.lower()
    if any(kw in lower for kw in advanced_keywords):
        return "advanced"
    if any(kw in lower for kw in beginner_keywords):
        return "beginner"
    if char_count > 20000:
        return "reference"
    if char_count > 8000:
        return "intermediate"
    return "beginner"


def scan_and_classify(dry_run: bool = False) -> dict:
    """扫描所有原始文章并分类。"""
    results = {"articles": [], "stats": {}}
    stats = {"total": 0, "classified": 0, "skipped": 0}

    for raw_dir in [CONTENT_RAW_EN, CONTENT_RAW_ZH]:
        if not raw_dir.exists():
            continue

        for md_file in sorted(raw_dir.glob("*.md")):
            stats["total"] += 1
            with open(md_file) as f:
                content = f.read()

            # 分离 frontmatter
            fm = {}
            body = content
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    # 简单 YAML 解析（不用完整库）
                    for line in parts[1].strip().split("\n"):
                        if ":" in line:
                            k, v = line.split(":", 1)
                            fm[k.strip()] = v.strip().strip('"').strip("'")
                    body = parts[2]

            # 分类
            tags = classify_text(body)

            article = {
                "file": str(md_file.relative_to(PROJECT_ROOT)),
                "title": fm.get("title", md_file.stem),
                "source_url": fm.get("source_url", ""),
                "source_type": fm.get("source_type", ""),
                "source_org": fm.get("source_org", ""),
                "credibility": int(fm.get("credibility", 3)),
                "lifecycle": fm.get("lifecycle", "latest"),
                **tags,
                "difficulty": infer_difficulty(body, len(body)),
                "char_count": len(body),
                "classified_at": datetime.now(timezone.utc).isoformat(),
            }

            if not dry_run:
                results["articles"].append(article)
            stats["classified"] += 1
            print(f"  ✅ {article['file']}: {len(tags.get('gpu',[]))} GPUs, {len(tags.get('os',[]))} OS, {article['difficulty']}")

    results["stats"] = stats
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    print("🏷️  rocm-hip-map classify.py")
    print(f"   {'DRY RUN' if args.dry_run else 'LIVE MODE'}")

    results = scan_and_classify(dry_run=args.dry_run)

    if not args.dry_run:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        with open(ARTICLES_JSON, "w") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\n📊 {results['stats']['total']} files scanned, {results['stats']['classified']} classified")


if __name__ == "__main__":
    main()
