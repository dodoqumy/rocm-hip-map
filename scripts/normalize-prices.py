#!/usr/bin/env python3
"""normalize-prices.py — 价格标准化（Phase 10.4 P1）。

从各平台原始价格数据合并、去异常值、统一货币(USD)、条件加权，
输出标准化价格数据供前端使用。

汇率来源：ECB (European Central Bank) 免费公开汇率 API。

用法：
  python3 scripts/normalize-prices.py                     # 标准化本周数据
  python3 scripts/normalize-prices.py --week 2026-W17     # 指定周
  python3 scripts/normalize-prices.py --rebuild-history   # 重建全部历史
"""
import argparse
import json
import math
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import requests

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PRICES_DIR = PROJECT_ROOT / "data" / "prices"

# ── 条件权重 ─────────────────────────────────────
# 开封 = 基准, 二手 = 95% 价值, 翻新 = 85%, 零件 = 60%
CONDITION_WEIGHTS = {
    "new": 1.00,
    "open_box": 1.00,
    "used": 0.95,
    "refurbished": 0.85,
    "parts": 0.60,
}


# ── 汇率获取 ─────────────────────────────────────

def get_exchange_rates() -> dict[str, float]:
    """获取 ECB 汇率（免费，无需 API Key）。"""
    try:
        # ECB publishes daily XML with rates
        resp = requests.get(
            "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml",
            timeout=15,
        )
        resp.raise_for_status()

        import xml.etree.ElementTree as ET
        root = ET.fromstring(resp.text)
        ns = {"gesmes": "http://www.gesmes.org/xml/2002-08-16",
              "eurofxref": "http://www.ecb.int/vocabulary/2002-08-16/eurofxref"}

        rates = {"EUR": 1.0}
        for cube in root.findall(".//eurofxref:Cube[@currency][@rate]", ns):
            currency = cube.attrib["currency"]
            rate = float(cube.attrib["rate"])
            rates[currency] = rate

        # ECB rates are EUR-based; convert to USD-based
        eur_to_usd = rates.get("USD", 1.08)  # fallback
        usd_rates = {}
        for cur, rate in rates.items():
            usd_rates[cur] = rate / eur_to_usd
        usd_rates["EUR"] = 1.0 / eur_to_usd

        # Add known missing currencies
        usd_rates.setdefault("CNY", 7.25)
        usd_rates.setdefault("JPY", 149.5)
        usd_rates.setdefault("KRW", 1380.0)
        usd_rates.setdefault("RUB", 98.5)
        usd_rates.setdefault("GBP", 0.79)
        usd_rates.setdefault("TWD", 32.5)

        print(f"  💱 Exchange rates loaded (ECB), USD/EUR={eur_to_usd:.4f}")
        return usd_rates
    except Exception as e:
        print(f"  ⚠ Cannot fetch ECB rates: {e}. Using fallback rates.", file=sys.stderr)
        return {
            "USD": 1.0, "EUR": 0.92, "GBP": 0.79, "CNY": 7.25,
            "JPY": 149.5, "KRW": 1380.0, "RUB": 98.5, "TWD": 32.5,
        }


# ── 异常值过滤 (IQR) ─────────────────────────────

def filter_outliers(prices: list[float]) -> list[float]:
    """IQR 方法过滤异常值：去除上下 1.5×IQR 之外的数据点。"""
    if len(prices) < 4:
        return prices  # 样本太小不滤

    sorted_prices = sorted(prices)
    n = len(sorted_prices)
    q1_idx = n // 4
    q3_idx = (3 * n) // 4
    q1 = sorted_prices[q1_idx]
    q3 = sorted_prices[q3_idx]
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    filtered = [p for p in prices if lower <= p <= upper]
    removed = len(prices) - len(filtered)
    if removed > 0:
        print(f"    🧹 Removed {removed} outliers (IQR: {lower:.0f}–{upper:.0f})")
    return filtered


# ── 标准化单个条目 ──────────────────────────────

def normalize_entry(
    entry: dict,
    rates: dict[str, float],
) -> Optional[dict]:
    """标准化单个价格条目。

    处理：货币转换 → 条件加权 → 异常值过滤 → 输出统一格式
    """
    currency = entry.get("currency", "USD")
    rate = rates.get(currency, 1.0)
    condition = entry.get("condition", "used")
    weight = CONDITION_WEIGHTS.get(condition, 0.95)

    listings = entry.get("listings", [])
    if not listings:
        return None

    # 提取所有价格并转为 USD
    raw_prices = []
    for item in listings:
        item_currency = item.get("currency", currency)
        item_rate = rates.get(item_currency, 1.0)
        usd_price = item["price"] * weight / item_rate
        raw_prices.append(usd_price)

    # 过滤异常值
    clean_prices = filter_outliers(raw_prices)
    if not clean_prices:
        return None

    # 统计
    clean_prices.sort()
    n = len(clean_prices)
    median = clean_prices[n // 2] if n % 2 else (clean_prices[n // 2 - 1] + clean_prices[n // 2]) / 2

    return {
        "gpu_id": entry.get("gpu_id", ""),
        "gpu_name": entry.get("gpu_name", ""),
        "country": entry.get("country", ""),
        "platform": entry.get("platform", ""),
        "condition": condition,
        "currency_original": currency,
        "median_usd": round(median, 2),
        "min_usd": round(clean_prices[0], 2),
        "max_usd": round(clean_prices[-1], 2),
        "sample_size": n,
        "original_sample_size": len(listings),
        "source_url": entry.get("source_url", ""),
        "collected_at": entry.get("collected_at", ""),
    }


# ── 合并标准化 ──────────────────────────────────

def normalize_week(week_tag: str, rates: dict[str, float]) -> list[dict]:
    """标准化某一周的全部价格数据。"""
    week_file = PRICES_DIR / f"prices-{week_tag}.json"
    if not week_file.exists():
        print(f"  ⚠ No data for {week_tag}")
        return []

    with open(week_file) as f:
        data = json.load(f)

    entries = data.get("entries", [])
    normalized = []
    for entry in entries:
        result = normalize_entry(entry, rates)
        if result:
            normalized.append(result)

    # Sort by GPU name then country
    normalized.sort(key=lambda x: (x["gpu_name"], x["country"]))

    # Write normalized output
    out_path = PRICES_DIR / f"prices-{week_tag}-normalized.json"
    output = {
        "updated": datetime.now(timezone.utc).isoformat(),
        "week": week_tag,
        "rates": rates,
        "entries": normalized,
    }
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"  ✅ {len(normalized)} normalized entries → {out_path}")
    return normalized


def rebuild_history(rates: dict[str, float]):
    """重建全部历史标准化数据。"""
    week_files = sorted(PRICES_DIR.glob("prices-20*-W*.json"))
    # Filter out normalized files
    week_files = [f for f in week_files if "normalized" not in f.name]

    all_history = {}
    for wf in week_files:
        week_tag = wf.stem.replace("prices-", "")
        normalized = normalize_week(week_tag, rates)
        if normalized:
            all_history[week_tag] = {
                "entries": normalized,
                "updated": datetime.now(timezone.utc).isoformat(),
            }

    history_path = PRICES_DIR / "price-history.json"
    with open(history_path, "w", encoding="utf-8") as f:
        json.dump({"updated": datetime.now(timezone.utc).isoformat(), "weeks": all_history}, f, ensure_ascii=False, indent=2)

    print(f"\n📈 History rebuilt: {len(all_history)} weeks → {history_path}")


# ── 主函数 ───────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="GPU 价格标准化")
    parser.add_argument("--week", help="指定 ISO 周标签 (e.g. 2026-W17)")
    parser.add_argument("--rebuild-history", action="store_true", help="重建全部历史")
    args = parser.parse_args()

    print("📊 GPU 价格标准化")
    rates = get_exchange_rates()

    if args.rebuild_history:
        print("  🔄 Rebuilding all history...")
        rebuild_history(rates)
    elif args.week:
        normalize_week(args.week, rates)
    else:
        # 默认处理本周
        now = datetime.now(timezone.utc)
        iso_week = now.isocalendar()
        week_tag = f"{now.year}-W{iso_week.week:02d}"
        print(f"  📅 Current week: {week_tag}")
        normalize_week(week_tag, rates)


if __name__ == "__main__":
    main()
