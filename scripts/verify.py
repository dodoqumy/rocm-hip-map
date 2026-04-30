#!/usr/bin/env python3
"""
verify.py — 文章一致性 & 翻译质量校验器。

职责：只检查，不修改。

三个校验维度：
  1. 原文一致性 — 本地存档 vs 当前线上原文（内容是否一致）
  2. 翻译准确性 — 术语正确、语义忠实
  3. 翻译通顺性 — 流畅度、错别字、标点

输出：
  data/verification/<article_id>.json   — 逐篇校验报告
  data/verification/summary.json       — 全量汇总

用法：
  python3 scripts/verify.py                            # 校验全部
  python3 scripts/verify.py --id rocm_what-is-rocm     # 校验单篇
  python3 scripts/verify.py --dry-run                   # 预览
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

# ── 项目根 ─────────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONTENT_RAW_EN = (PROJECT_ROOT / "content" / "raw" / "english").resolve()
CONTENT_TRANSLATED_ZH = (PROJECT_ROOT / "content" / "translated" / "zh").resolve()
VERIFICATION_DIR = (PROJECT_ROOT / "data" / "verification").resolve()
ARTICLES_JSON = (PROJECT_ROOT / "data" / "articles.json").resolve()


def _find_translation_file(article_id: str) -> Path:
    """Find Chinese translation file for given article_id.
    
    Tries multiple strategies:
    1. Direct: article_id + "_zh.md"
    2. Normalized: Try replacing common prefixes (hip_projects_HIP_, etc.) with "rocm_"
    3. Glob search for any file ending with article_id suffix + "_zh.md"
    """
    # Strategy 1: Direct match with _zh suffix
    zh_file = CONTENT_TRANSLATED_ZH / f"{article_id}_zh.md"
    if zh_file.exists():
        return zh_file
    
    # Strategy 2: Try normalized naming (replace project prefixes)
    # e.g., "hip_projects_HIP_en_latest_xxx" -> "rocm_en_latest_xxx"
    normalized = article_id
    for prefix in ["hip_projects_HIP_", "hipify_projects_HIPIFY_", "rocm-install-linux_projects_install-on-linux_"]:
        if normalized.startswith(prefix):
            normalized = "rocm_" + normalized[len(prefix):]
            break
    
    if normalized != article_id:
        zh_file = CONTENT_TRANSLATED_ZH / f"{normalized}_zh.md"
        if zh_file.exists():
            return zh_file
    
    # Strategy 3: Glob search for any matching file
    # Extract suffix after first "_en_" or similar pattern
    pattern_suffixes = ["_en_", "_latest_"]
    for suffix in pattern_suffixes:
        if suffix in article_id:
            parts = article_id.split(suffix)
            if len(parts) > 1:
                search_pattern = f"*{suffix}{parts[-1]}_zh.md"
                matches = list(CONTENT_TRANSLATED_ZH.glob(search_pattern))
                if matches:
                    return matches[0]
    
    # Return empty path if not found
    return Path("")


# ── 翻译校验用 LLM 配置 ─────────────────────────────
LLM_PROVIDER = os.environ.get("TRANSLATE_PROVIDER", "opencode")
LLM_API_KEY = os.environ.get("TRANSLATE_API_KEY", "")
LLM_MODEL = os.environ.get("TRANSLATE_MODEL", "deepseek-v4-pro")
LLM_BASE_URL = os.environ.get("TRANSLATE_BASE_URL", "https://opencode.ai/zen/go/v1")


def load_article_index() -> list[dict]:
    """加载文章索引。"""
    if not ARTICLES_JSON.exists():
        return []
    with open(ARTICLES_JSON) as f:
        data = json.load(f)
    return data.get("articles", [])


def fetch_current_page(url: str, timeout: int = 30) -> Optional[str]:
    """抓取当前线上页面。"""
    try:
        result = subprocess.run(
            ["curl", "-sL", "--max-time", str(timeout),
             "-H", "User-Agent: rocm-hip-map-verifier/1.0",
             url],
            capture_output=True, text=True, timeout=timeout + 5,
        )
        if result.returncode != 0 or not result.stdout.strip():
            return None
        return result.stdout
    except Exception:
        return None


def html_to_text(html: str) -> str:
    """HTML → 纯文本（pandoc）。"""
    try:
        result = subprocess.run(
            ["pandoc", "-f", "html", "-t", "plain", "--wrap=none"],
            input=html, capture_output=True, text=True, timeout=60,
        )
        if result.returncode == 0:
            return result.stdout.strip()
        return html  # fallback
    except Exception:
        return html


def extract_body_text(md_content: str) -> str:
    """从 Markdown 中提取正文（去掉 frontmatter + 代码块）。"""
    # 去掉 YAML frontmatter
    body = re.sub(r'^---\s*\n.*?\n---\s*\n', '', md_content, flags=re.DOTALL)
    # 去掉代码块
    body = re.sub(r'```.*?```', '[CODE_BLOCK]', body, flags=re.DOTALL)
    body = re.sub(r'`[^`]+`', '[INLINE_CODE]', body)
    return body.strip()


def call_llm(prompt: str, system: str = "You are a technical documentation reviewer.") -> str:
    """调用 LLM（opencode-go / DeepSeek）。"""
    if not LLM_API_KEY:
        return '{"error": "No API key configured"}'

    import urllib.request
    import urllib.error

    body = json.dumps({
        "model": LLM_MODEL,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.1,
        "max_tokens": 2000,
    }).encode()

    req = urllib.request.Request(
        f"{LLM_BASE_URL}/chat/completions",
        data=body,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {LLM_API_KEY}",
        },
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read())
            return data["choices"][0]["message"]["content"]
    except Exception as e:
        return json.dumps({"error": str(e)})


def check_content_consistency(local_md: str, current_url: str) -> dict:
    """
    校验本地存档与当前线上原文的一致性。
    返回：{status, score, notes}
    """
    # 抓取当前线上版本
    current_html = fetch_current_page(current_url)
    if not current_html:
        return {"status": "error", "score": 0, "notes": "无法抓取线上原文"}

    current_text = html_to_text(current_html)
    local_text = extract_body_text(local_md)

    if not local_text or len(local_text) < 100:
        return {"status": "error", "score": 0, "notes": "本地存档内容过短"}

    # 简单相似度：基于文本长度比 + 关键词命中
    len_ratio = min(len(local_text), len(current_text)) / max(len(local_text), len(current_text), 1)

    # 提取关键词比较
    import re as re_module
    def extract_keywords(text: str) -> set:
        words = re_module.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
        return set(words)

    local_kw = extract_keywords(local_text[:10000])
    current_kw = extract_keywords(current_text[:10000])

    if not local_kw or not current_kw:
        kw_overlap = 0
    else:
        kw_overlap = len(local_kw & current_kw) / max(len(local_kw | current_kw), 1)

    score = (len_ratio * 0.3 + kw_overlap * 0.7)

    if score >= 0.85:
        status = "pass"
        notes = f"内容一致 (相似度 {score:.0%})"
    elif score >= 0.60:
        status = "warn"
        notes = f"可能有更新 (相似度 {score:.0%})，建议重新抓取"
    else:
        status = "fail"
        notes = f"内容差异大 (相似度 {score:.0%})，可能原文已大幅改版"

    return {"status": status, "score": round(score, 3), "notes": notes}


def check_translation_quality(source_en: str, translated_zh: str) -> dict:
    """
    LLM 校验翻译质量（准确性 + 通顺性 + 错别字）。
    返回：{status, score, notes, issues}
    """
    if not LLM_API_KEY:
        return {
            "status": "skip",
            "score": 0,
            "notes": "未配置 API Key，跳过翻译校验",
            "issues": [],
        }

    # 截断过长的内容
    src_sample = source_en[:3000]
    tgt_sample = translated_zh[:3000] if translated_zh else ""

    if not tgt_sample:
        return {"status": "error", "score": 0, "notes": "无翻译内容", "issues": []}

    prompt = f"""你是一个中英双语技术文档审查员。请审查以下 ROCm 技术文档的翻译质量。

## 英文原文（节选）：
{src_sample}

## 中文翻译（节选）：
{tgt_sample}

请评估以下方面，并输出 JSON：
1. 术语翻译是否准确（ROCm 术语如 kernel→内核, wavefront→波前, occupancy→占用率）
2. 语义是否忠实于原文
3. 语句是否通顺自然
4. 是否有错别字或标点错误

返回纯 JSON（不要 markdown 包裹）：
{{
  "terminology_score": 0-100,
  "fidelity_score": 0-100,  
  "fluency_score": 0-100,
  "typos": ["错别字1", "错别字2"],
  "issues": ["具体问题描述1", "具体问题描述2"],
  "overall_score": 0-100,
  "summary": "一句话总结"
}}
"""
    response = call_llm(prompt)
    try:
        result = json.loads(response)
        # 确保字段存在
        result.setdefault("terminology_score", 0)
        result.setdefault("fidelity_score", 0)
        result.setdefault("fluency_score", 0)
        result.setdefault("typos", [])
        result.setdefault("issues", [])
        result.setdefault("overall_score", 0)
        result.setdefault("summary", "")

        score = result["overall_score"] / 100
        if score >= 0.80:
            status = "pass"
        elif score >= 0.60:
            status = "warn"
        else:
            status = "fail"

        return {
            "status": status,
            "score": round(score, 3),
            "notes": result["summary"],
            "issues": result["typos"] + result["issues"],
            "details": {
                "terminology": result["terminology_score"],
                "fidelity": result["fidelity_score"],
                "fluency": result["fluency_score"],
            },
        }
    except (json.JSONDecodeError, KeyError):
        return {
            "status": "error",
            "score": 0,
            "notes": f"LLM 返回解析失败: {response[:200]}",
            "issues": [],
        }


def check_issue_completeness(raw_md: str, article: dict) -> dict:
    """
    Issue 类文章信息完整性校验。
    检测维度：描述 / 环境 / 错误日志 / 解决状态 / 解决方案。
    返回：{status, score, notes, dimensions}
    """
    # 判断是否为 Issue 类文章
    tags = article.get("tags_extra", article.get("tags", []))
    source_url = article.get("source_url", "")
    title = article.get("title", "").lower()
    body = extract_body_text(raw_md).lower()[:5000]

    is_issue = (
        "bug" in tags or "issue" in tags or "troubleshoot" in tags
        or "github.com" in source_url and ("/issues/" in source_url or "/pull/" in source_url)
        or any(kw in title for kw in ["bug", "issue", "error", "problem", "fail", "crash", "hang"])
        or any(kw in body[:500] for kw in ["error:", "traceback", "segfault", "assertion failed"])
    )

    if not is_issue:
        return {"status": "skip", "score": 1, "notes": "非 Issue 类文章", "dimensions": {}}

    # 结构检测
    dimensions = {
        "has_description": bool(re.search(r'(problem|issue|bug|error|描述|问题)', body[:2000])),
        "has_environment": bool(re.search(r'(rocm\s*\d|ubuntu|rhel|mi\d|gfx\d|driver|kernel|环境)', body[:2000])),
        "has_error_log": bool(re.search(r'(error:|traceback|segfault|log|dmesg|journalctl|rocminfo)', body[:2000])),
        "has_resolution_status": bool(re.search(r'(fixed|resolved|solved|closed|workaround|修复|解决|已修复|已关闭)', body[:3000])),
        "has_solution": bool(re.search(r'(solution|workaround|fix|patch|commit|pr|解决|方案|办法|步骤)', body[:3000])),
    }

    # 评分
    total = len(dimensions)
    passed = sum(1 for v in dimensions.values() if v)
    score = passed / total if total else 0

    missing = [k.replace("has_", "") for k, v in dimensions.items() if not v]

    if score >= 0.8:
        status = "pass"
        notes = f"信息完整 ({passed}/{total})"
    elif score >= 0.4:
        status = "warn"
        notes = f"缺少: {', '.join(missing)}"
    else:
        status = "fail"
        notes = f"严重缺失: {', '.join(missing)}"

    return {"status": status, "score": round(score, 3), "notes": notes, "dimensions": dimensions}


def verify_article(article: dict) -> dict:
    """校验单篇文章，返回报告。"""
    # Extract article_id from "file" field - take the filename stem
    file_path = article.get("file", "")
    article_id = Path(file_path).stem  # e.g., "hip_projects_HIP_en_latest_how-to_hip_debugging"
    
    source_url = article.get("source_url", "")
    title = article.get("title", "Untitled")

    print(f"\n{'='*60}")
    print(f"🔍 {article_id}")
    print(f"   {title}")

    report = {
        "article_id": article_id,
        "title": title,
        "source_url": source_url,
        "verified_at": datetime.now(timezone.utc).isoformat(),
        "checks": {},
        "overall": "pending",
    }

    # ── 1. 原文一致性校验 ──
    raw_file = CONTENT_RAW_EN / f"{article_id}.md"
    if raw_file.exists():
        with open(raw_file) as f:
            local_md = f.read()
        report["checks"]["content_consistency"] = check_content_consistency(local_md, source_url)
        print(f"   📄 一致性: {report['checks']['content_consistency']['status']} "
              f"({report['checks']['content_consistency']['score']:.0%})")
    else:
        report["checks"]["content_consistency"] = {
            "status": "warn", "score": 0, "notes": "本地存档不存在"
        }
        print("   📄 一致性: warn (本地存档不存在)")

    # ── 2. 翻译质量校验 ──
    # Try to find Chinese translation with _zh suffix
    zh_file = _find_translation_file(article_id)
    if zh_file.exists() and zh_file.is_file() and raw_file.exists():
        with open(raw_file) as f:
            src_content = f.read()
        with open(zh_file) as f:
            tgt_content = f.read()
        report["checks"]["translation_quality"] = check_translation_quality(src_content, tgt_content)
        status = report["checks"]["translation_quality"]["status"]
        score = report["checks"]["translation_quality"]["score"]
        print(f"   🌐 翻译: {status} ({score:.0%})")
        if report["checks"]["translation_quality"]["issues"]:
            for issue in report["checks"]["translation_quality"]["issues"][:3]:
                print(f"      ⚠ {issue}")
    elif not raw_file.exists():
        report["checks"]["translation_quality"] = {
            "status": "skip", "score": 0, "notes": "无原文文件", "issues": []
        }
        print("   🌐 翻译: skip (无原文文件)")
    else:
        report["checks"]["translation_quality"] = {
            "status": "skip", "score": 0, "notes": "翻译暂未完成", "issues": []
        }
        print("   🌐 翻译: skip (翻译暂未完成)")

    # ── 3. Issue 信息完整性（仅 Issue 类文章）──
    if raw_file.exists():
        with open(raw_file) as f:
            local_md = f.read()
        report["checks"]["issue_completeness"] = check_issue_completeness(local_md, article)
        if report["checks"]["issue_completeness"]["status"] != "skip":
            ic = report["checks"]["issue_completeness"]
            print(f"   📋 Issue 完整性: {ic['status']} ({ic['score']:.0%}) — {ic['notes']}")

    # ── 4. 判定 overall ──
    statuses = [c["status"] for c in report["checks"].values()]
    if all(s == "pass" for s in statuses):
        report["overall"] = "pass"
    elif "fail" in statuses:
        report["overall"] = "fail"
    elif "warn" in statuses:
        report["overall"] = "warn"
    else:
        report["overall"] = "pending"

    print(f"   🏷 overall: {report['overall']}")

    return report


def save_report(report: dict):
    """保存校验报告。"""
    VERIFICATION_DIR.mkdir(parents=True, exist_ok=True)
    path = VERIFICATION_DIR / f"{report['article_id']}.json"
    with open(path, "w") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)


def update_summary(reports: list[dict]):
    """更新全量汇总。"""
    summary = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total": len(reports),
        "pass": sum(1 for r in reports if r["overall"] == "pass"),
        "warn": sum(1 for r in reports if r["overall"] == "warn"),
        "fail": sum(1 for r in reports if r["overall"] == "fail"),
        "pending": sum(1 for r in reports if r["overall"] == "pending"),
        "articles": [
            {
                "article_id": r["article_id"],
                "overall": r["overall"],
                "content_score": r.get("checks", {}).get("content_consistency", {}).get("score", 0),
                "translation_score": r.get("checks", {}).get("translation_quality", {}).get("score", 0),
            }
            for r in reports
        ],
    }
    path = VERIFICATION_DIR / "summary.json"
    with open(path, "w") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    return summary


def stamp_verified_articles(reports: list[dict], dry_run: bool = False):
    """
    对 overall=pass 的文章打上核对版本标签。
    修改 articles.json 和对应 MDX 文件的 frontmatter。
    """
    passed = [r for r in reports if r["overall"] == "pass"]
    if not passed:
        print("\n✅ 无 newly-passed 文章（所有文章要么未通过，要么已标记）")
        return

    if not ARTICLES_JSON.exists():
        print("\n⚠ articles.json 不存在，无法打标签")
        return

    with open(ARTICLES_JSON) as f:
        index_data = json.load(f)

    articles = index_data.get("articles", [])
    updated = 0

    for article in articles:
        aid = article.get("id", "")
        matching_report = next((r for r in passed if r["article_id"] == aid), None)
        if not matching_report:
            continue

        ver = article.get("verification", {})
        if ver.get("status") == "verified":
            continue  # 已验证过

        ver["status"] = "verified"
        ver["version"] = "v1"
        ver["verified_at"] = matching_report["verified_at"]
        article["verification"] = ver
        updated += 1

        if dry_run:
            print(f"  [DRY] {aid} → verified v1")
        else:
            print(f"  ✅ {aid} → verified v1")

    if updated > 0 and not dry_run:
        with open(ARTICLES_JSON, "w") as f:
            json.dump(index_data, f, indent=2, ensure_ascii=False)
        print(f"\n📊 {updated} 篇文章已标记为 verified v1")


def main():
    parser = argparse.ArgumentParser(description="Verify article consistency & translation quality")
    parser.add_argument("--id", help="Verify single article by ID")
    parser.add_argument("--dry-run", action="store_true", help="Preview only")
    parser.add_argument("--stamp", action="store_true", help="Stamp passed articles as verified")
    args = parser.parse_args()

    print("🔍 rocm-hip-map verify.py")
    print(f"   {'DRY RUN' if args.dry_run else 'LIVE MODE'}")
    print(f"   Provider: {LLM_PROVIDER} | Model: {LLM_MODEL}")
    print(f"   API Key: {'configured' if LLM_API_KEY else '⚠ NOT CONFIGURED'}")

    index = load_article_index()

    if args.id:
        # 单篇模式 - match by file stem
        target_stem = args.id
        article = None
        for a in index:
            if Path(a.get("file", "")).stem == target_stem:
                article = a
                break
        if not article:
            print(f"❌ 文章 {args.id} 在索引中未找到")
            sys.exit(1)
        reports = [verify_article(article)]
    else:
        # 全量模式
        if not index:
            print("⚠ articles.json 为空或不存在")
            sys.exit(0)
        print(f"\n📚 共 {len(index)} 篇文章待校验")
        reports = []
        for article in index:
            report = verify_article(article)
            reports.append(report)
            if not args.dry_run:
                save_report(report)
            time.sleep(2)  # LLM rate limit

    # 保存汇总
    summary = update_summary(reports)
    if not args.dry_run:
        print(f"\n📊 全量汇总已保存: {VERIFICATION_DIR / 'summary.json'}")
    print(f"   pass={summary['pass']} warn={summary['warn']} "
          f"fail={summary['fail']} pending={summary['pending']}")

    # 打标签
    if args.stamp:
        stamp_verified_articles(reports, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
