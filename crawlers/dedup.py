"""
rocm-hip-map/crawlers/dedup.py
Phase 2.1.1 — 去重模块

提供 URL 规范化、内容 hash 双重去重。
"""
from __future__ import annotations

import re
import hashlib
from urllib.parse import urlparse, urlencode, parse_qs


# ── URL 规范化 ────────────────────────────────────────────────────────────────

# 追踪参数黑名单
_TRACKING_PARAMS = {
    # UTM 系列
    "utm_source", "utm_medium", "utm_campaign", "utm_content",
    "utm_term", "utm_id", "utm_source_platform", "utm_creative_format",
    "utm_marketing_tactic",
    # 广告追踪
    "fbclid", "gclid", "gclsrc", "dclid", "msclkid",
    # 社交追踪
    "mc_cid", "mc_eid", "ref", "ref_src", "ref_url",
    # 电商追踪
    "affiliate", "aff_id", "campaign_id", "zanpid",
    # 通用追踪
    "trk", "trkInfo", "yclid", "rb_clickid",
    # HubSpot / Marketo
    "mkt_tok", "_hsenc", "_hsmi", "hsCtaTracking",
    # 锚点（通常不影响内容）
    "ref_", "source", "via",
}

# 可移除的路径模式
_PATH_PATTERNS_TO_REMOVE = re.compile(
    r"(\btrack|click|redirect|out|go\b)", re.IGNORECASE
)


def normalize_url(url: str) -> str:
    """
    URL 规范化，用于去重。

    步骤：
    1. scheme + netloc 小写
    2. 移除追踪参数（utm_*, fbclid, ...）
    3. 移除空 query / fragment
    4. 移除末尾斜杠（homepage）
    """
    if not url or not isinstance(url, str):
        return url or ""

    url = url.strip()

    # 移除 #fragment
    if "#" in url:
        url = url.split("#", 1)[0]

    try:
        parsed = urlparse(url)
    except Exception:
        return url

    # scheme + netloc 小写
    scheme = parsed.scheme.lower() if parsed.scheme else "https"
    netloc = parsed.netloc.lower()

    # 移除默认端口
    if netloc.endswith(":80") and scheme == "http":
        netloc = netloc[:-3]
    elif netloc.endswith(":443") and scheme == "https":
        netloc = netloc[:-4]

    # 去除追踪参数
    qs = parse_qs(parsed.query, keep_blank_values=True)
    qs = {k: v for k, v in qs.items() if k not in _TRACKING_PARAMS}

    # 空 query → 去掉 ?
    if not qs:
        query = ""
    else:
        query = urlencode(qs, doseq=True)

    result = f"{scheme}://{netloc}{parsed.path}"

    # 移除末尾斜杠（仅 homepage / 避免 / vs 空 差异）
    if result.endswith("/") and len(parsed.path) > 1:
        result = result[:-1]

    if query:
        result += "?" + query

    return result


def url_hash(url: str) -> str:
    """规范化 URL 的 sha256 前 16 位。"""
    return hashlib.sha256(normalize_url(url).encode()).hexdigest()[:16]


def content_hash(content: str) -> str:
    """文本内容的 sha256 前 16 位。"""
    normalized = re.sub(r"\s+", " ", content or "").strip()
    return hashlib.sha256(normalized.encode()).hexdigest()[:16]


def is_tracking_url(url: str) -> bool:
    """判断 URL 是否为纯追踪跳转页（无实质内容）。"""
    if not url:
        return True
    url_lower = url.lower()
    # 已知追踪域名
    tracking_domains = {
        "redirect", "click", "link", "out", "goto",
        "ads.", "ad.", "tracking.", "clk.", "trk.",
    }
    try:
        netloc = urlparse(url).netloc.lower()
        for t in tracking_domains:
            if netloc.startswith(t) or f".{t}" in netloc:
                return True
    except Exception:
        pass
    return False


def strip_utm(url: str) -> str:
    """简化别名。"""
    return normalize_url(url)
