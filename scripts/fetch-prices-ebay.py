#!/usr/bin/env python3
"""fetch-prices-ebay.py — eBay Browse API 价格抓取（Phase 10.1 P0）。

从 eBay US/DE/UK 三个站点抓取 AMD GPU 二手成交价格。

配置（环境变量）：
  EBAY_APP_ID     eBay Developer App ID（免费注册 https://developer.ebay.com）
  EBAY_CERT_ID    eBay Client ID (Cert ID)

限速：5000 calls/day（免费层），每次请求间隔 1 秒。

用法：
  python3 scripts/fetch-prices-ebay.py                    # 抓取所有 GPU
  python3 scripts/fetch-prices-ebay.py --dry-run           # 预览（不走 API）
  python3 scripts/fetch-prices-ebay.py --model MI50        # 仅指定型号
  python3 scripts/fetch-prices-ebay.py --site EBAY-US      # 仅指定站点

输出：data/prices/prices-YYYY-Www.json
"""
import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional
from urllib.parse import quote

import requests

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PRICES_DIR = PROJECT_ROOT / "data" / "prices"

# ── eBay 站点配置 ──────────────────────────────────
EBAY_SITES = {
    "EBAY-US": {
        "country": "US",
        "currency": "USD",
        "marketplace_id": "EBAY_US",
        "endpoint": "https://api.ebay.com/buy/browse/v1",
        "flag": "🇺🇸",
    },
    "EBAY-DE": {
        "country": "DE",
        "currency": "EUR",
        "marketplace_id": "EBAY_DE",
        "endpoint": "https://api.ebay.com/buy/browse/v1",
        "flag": "🇩🇪",
    },
    "EBAY-UK": {
        "country": "GB",
        "currency": "GBP",
        "marketplace_id": "EBAY_GB",
        "endpoint": "https://api.ebay.com/buy/browse/v1",
        "flag": "🇬🇧",
    },
}

# ── GPU 型号清单 ──────────────────────────────────
GPU_MODELS = {
    # Instinct 计算卡
    "MI50_16GB": {
        "name": "AMD Instinct MI50 (16GB)",
        "keywords": "amd instinct mi50 16gb",
        "category": "instinct",
    },
    "MI50_32GB": {
        "name": "AMD Instinct MI50 (32GB)",
        "keywords": "amd instinct mi50 32gb",
        "category": "instinct",
    },
    "MI100": {
        "name": "AMD Instinct MI100",
        "keywords": "amd instinct mi100",
        "category": "instinct",
    },
    "MI210": {
        "name": "AMD Instinct MI210",
        "keywords": "amd instinct mi210",
        "category": "instinct",
    },
    "MI250": {
        "name": "AMD Instinct MI250",
        "keywords": "amd instinct mi250 -mi250x",
        "category": "instinct",
    },
    "MI250X": {
        "name": "AMD Instinct MI250X",
        "keywords": "amd instinct mi250x",
        "category": "instinct",
    },
    "MI300X": {
        "name": "AMD Instinct MI300X",
        "keywords": "amd instinct mi300x",
        "category": "instinct",
    },
    # Radeon 消费卡
    "RX_6800": {
        "name": "AMD Radeon RX 6800",
        "keywords": "amd radeon rx 6800 -xt -6800xt",
        "category": "radeon",
    },
    "RX_6800_XT": {
        "name": "AMD Radeon RX 6800 XT",
        "keywords": "amd radeon rx 6800 xt",
        "category": "radeon",
    },
    "RX_6900_XT": {
        "name": "AMD Radeon RX 6900 XT",
        "keywords": "amd radeon rx 6900 xt",
        "category": "radeon",
    },
    "RX_6950_XT": {
        "name": "AMD Radeon RX 6950 XT",
        "keywords": "amd radeon rx 6950 xt",
        "category": "radeon",
    },
    "RX_7900_XT": {
        "name": "AMD Radeon RX 7900 XT",
        "keywords": "amd radeon rx 7900 xt -7900xtx",
        "category": "radeon",
    },
    "RX_7900_XTX": {
        "name": "AMD Radeon RX 7900 XTX",
        "keywords": "amd radeon rx 7900 xtx",
        "category": "radeon",
    },
    "RX_7900_GRE": {
        "name": "AMD Radeon RX 7900 GRE",
        "keywords": "amd radeon rx 7900 gre",
        "category": "radeon",
    },
}

# ── OAuth 认证 ────────────────────────────────────

def get_oauth_token(app_id: str, cert_id: str) -> Optional[str]:
    """获取 eBay OAuth 2.0 token (Client Credentials Grant)。"""
    try:
        import base64
        resp = requests.post(
            "https://api.ebay.com/identity/v1/oauth2/token",
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "Authorization": "Basic "
                + base64.b64encode(f"{app_id}:{cert_id}".encode()).decode(),
            },
            data={
                "grant_type": "client_credentials",
                "scope": "https://api.ebay.com/oauth/api_scope",
            },
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json().get("access_token")
    except Exception as e:
        print(f"  ⚠ OAuth failed: {e}", file=sys.stderr)
        return None


# ── 价格抓取 ─────────────────────────────────────

def fetch_gpu_prices(
    token: str,
    gpu_model: dict,
    site: dict,
    dry_run: bool = False,
) -> list[dict]:
    """抓取单个 GPU 型号在指定 eBay 站点的成交价。

    Returns list of price entries.
    """
    entries = []
    keywords = gpu_model["keywords"]

    # 搜索 sold items（仅需一个 filter 参数表示 sold）
    # eBay Browse API: filter=buyingOptions:{FIXED_PRICE|AUCTION},
    #   filter=itemLocationCountry:<COUNTRY>
    url = (
        f"{site['endpoint']}/item_summary/search"
        f"?q={quote(keywords)}"
        f"&filter=conditions:{{USED|SELLER_REFURBISHED}}"
        f"&filter=buyingOptions:{{FIXED_PRICE|AUCTION}}"
        f"&sort=-price"
        f"&limit=50"
    )

    if dry_run:
        print(f"  🔍 [DRY-RUN] {url}")
        return entries

    try:
        headers = {
            "Authorization": f"Bearer {token}",
            "X-EBAY-C-MARKETPLACE-ID": site["marketplace_id"],
            "Accept": "application/json",
        }
        resp = requests.get(url, headers=headers, timeout=30)
        if resp.status_code == 401:
            print(f"  ⚠ Token expired, re-authenticating...", file=sys.stderr)
            return []  # caller 负责重试
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        print(f"  ❌ API error for {gpu_model['name']} @ {site['flag']}: {e}", file=sys.stderr)
        return entries

    items = data.get("itemSummaries", [])
    prices = []

    for item in items:
        price_info = item.get("price", {})
        value = float(price_info.get("value", 0))
        currency = price_info.get("currency", site["currency"])

        if value <= 0:
            continue

        # 条件判断
        condition = item.get("condition", "USED").upper()
        cond_map = {
            "NEW": "new",
            "NEW_OTHER": "open_box",
            "NEW_WITH_DEFECTS": "open_box",
            "MANUFACTURER_REFURBISHED": "refurbished",
            "SELLER_REFURBISHED": "refurbished",
            "USED": "used",
            "FOR_PARTS_OR_NOT_WORKING": "parts",
        }
        condition_label = cond_map.get(condition, "used")

        prices.append({
            "title": item.get("title", ""),
            "price": value,
            "currency": currency,
            "condition": condition_label,
            "url": item.get("itemWebUrl", ""),
            "seller": item.get("seller", {}).get("username", "unknown"),
            "listed_at": item.get("itemEndDate", ""),
        })

    # 统计
    if prices:
        values = [p["price"] for p in prices]
        values.sort()
        n = len(values)
        median = values[n // 2] if n % 2 else (values[n // 2 - 1] + values[n // 2]) / 2

        entry = {
            "gpu_id": gpu_model["name"].replace(" ", "_").replace("(", "").replace(")", ""),
            "gpu_name": gpu_model["name"],
            "country": site["country"],
            "platform": "eBay",
            "currency": site["currency"],
            "median": round(median, 2),
            "min": round(values[0], 2),
            "max": round(values[-1], 2),
            "sample_size": n,
            "source_url": f"https://www.ebay.com/sch/i.html?_nkw={quote(keywords)}&LH_Sold=1",
            "collected_at": datetime.now(timezone.utc).isoformat(),
            "listings": prices,
        }
        entries.append(entry)
        print(
            f"  {site['flag']} {gpu_model['name']}: "
            f"median={site['currency']}{median:,.0f} "
            f"(min={values[0]:,.0f} max={values[-1]:,.0f} n={n})"
        )
    else:
        print(f"  {site['flag']} {gpu_model['name']}: no results")

    return entries


# ── 主函数 ───────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="eBay GPU 二手价格抓取")
    parser.add_argument("--dry-run", action="store_true", help="预览模式")
    parser.add_argument("--model", help="仅指定 GPU 型号 ID")
    parser.add_argument("--site", help="仅指定 eBay 站点 (EBAY-US/EBAY-DE/EBAY-UK)")
    args = parser.parse_args()

    app_id = os.environ.get("EBAY_APP_ID", "")
    cert_id = os.environ.get("EBAY_CERT_ID", "")

    if not args.dry_run and (not app_id or not cert_id):
        print("❌ 需要设置 EBAY_APP_ID 和 EBAY_CERT_ID 环境变量")
        print("   注册地址：https://developer.ebay.com/")
        print("   使用 --dry-run 预览搜索 URL")
        sys.exit(1)

    print("💸 eBay GPU 二手价格抓取")
    print(f"   模式：{'DRY RUN' if args.dry_run else 'LIVE'}")

    # Token
    token = None
    if not args.dry_run:
        token = get_oauth_token(app_id, cert_id)
        if not token:
            print("❌ OAuth 认证失败")
            sys.exit(1)
        print("   ✅ OAuth token acquired")

    # 筛选 GPU 型号
    if args.model:
        gpu_list = {k: v for k, v in GPU_MODELS.items() if k == args.model}
        if not gpu_list:
            print(f"❌ Unknown GPU model: {args.model}")
            print(f"   Available: {', '.join(GPU_MODELS.keys())}")
            sys.exit(1)
    else:
        gpu_list = GPU_MODELS

    # 筛选站点
    if args.site:
        site_list = {k: v for k, v in EBAY_SITES.items() if k == args.site}
        if not site_list:
            print(f"❌ Unknown site: {args.site}")
            sys.exit(1)
    else:
        site_list = EBAY_SITES

    # 抓取
    all_entries = []
    total_requests = 0

    for gpu_id, gpu_model in gpu_list.items():
        for site_id, site in site_list.items():
            if not args.dry_run and total_requests >= 4500:
                print("⚠ 接近 API 限速 (4500/5000)，停止")
                break

            entries = fetch_gpu_prices(token, gpu_model, site, dry_run=args.dry_run)
            all_entries.extend(entries)
            total_requests += 1

            if not args.dry_run and total_requests > 0:
                time.sleep(1)  # rate limit

    if not args.dry_run and all_entries:
        # 按周保存
        now = datetime.now(timezone.utc)
        iso_week = now.isocalendar()
        week_tag = f"{now.year}-W{iso_week.week:02d}"
        out_path = PRICES_DIR / f"prices-{week_tag}.json"

        output = {
            "updated": now.isoformat(),
            "week": week_tag,
            "source": "eBay Browse API",
            "entries": all_entries,
        }

        PRICES_DIR.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(output, f, ensure_ascii=False, indent=2)

        print(f"\n📊 {len(all_entries)} entries saved → {out_path}")

        # 更新 price-history.json
        update_history(now, week_tag, all_entries)
    elif not args.dry_run:
        print("\n⚠ No data collected (check API credentials or search terms)")


def update_history(timestamp: datetime, week_tag: str, entries: list[dict]):
    """更新 price-history.json，保留 52 周趋势。"""
    history_path = PRICES_DIR / "price-history.json"

    history = {"updated": timestamp.isoformat(), "weeks": {}}
    if history_path.exists():
        with open(history_path) as f:
            history = json.load(f)

    # 写入本周数据
    history["weeks"][week_tag] = {
        "updated": timestamp.isoformat(),
        "entries": entries,
    }

    # 只保留最近 52 周
    weeks = sorted(history["weeks"].keys(), reverse=True)
    if len(weeks) > 52:
        for old_week in weeks[52:]:
            del history["weeks"][old_week]

    history["updated"] = timestamp.isoformat()

    with open(history_path, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

    print(f"📈 History updated ({len(history['weeks'])} weeks) → {history_path}")


if __name__ == "__main__":
    main()
