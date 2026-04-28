# Phase 10: AMD GPU 二手市场价格追踪系统

> 创建日期：2026-04-28 | 状态：📋 计划阶段

---

## 一、调研结论

### 各主要国家二手交易平台

| 国家 | 核心平台 | API/抓取可行性 | 反爬强度 | 价格货币 |
|------|---------|--------------|---------|---------|
| 🇺🇸 美国 | eBay.com | **eBay Browse API** ✅ | 低 (官方API) | USD |
| 🇺🇸 美国 | Amazon | Keepa/CCC 价格历史 ✅ | 低 | USD |
| 🇺🇸 美国 | /r/hardwareswap | Reddit API ✅ | 低 | USD |
| 🇨🇳 中国 | 闲鱼 (Goofish) | 网页抓取 ⚠ | **高** (需登录/验证) | CNY |
| 🇨🇳 中国 | 淘宝 | 网页抓取 ⚠ | 高 | CNY |
| 🇯🇵 日本 | Yahoo Auctions | 网页抓取 ⚠ | 中 | JPY |
| 🇯🇵 日本 | Mercari (メルカリ) | 网页抓取 ⚠ | 中 | JPY |
| 🇩🇪 德国 | eBay.de | eBay Browse API ✅ | 低 | EUR |
| 🇩🇪 德国 | Kleinanzeigen.de | 网页抓取 ⚠ | 中 | EUR |
| 🇫🇷 法国 | Leboncoin.fr | 网页抓取 ⚠ | 中 | EUR |
| 🇬🇧 英国 | eBay.co.uk | eBay Browse API ✅ | 低 | GBP |
| 🇬🇧 英国 | CEX | 网页抓取 | 低 | GBP |
| 🇷🇺 俄罗斯 | Avito.ru | 网页抓取 ⚠ | 中-高 | RUB |
| 🇰🇷 韩国 | Joonggonara (중고나라) | 网页抓取 ⚠ | 中 | KRW |
| 🇰🇷 韩国 | Bunjang (번개장터) | 网页抓取 ⚠ | 中 | KRW |
| 🇮🇹 意大利 | Subito.it | 网页抓取 | 低-中 | EUR |

### 关键发现

1. **eBay Browse API 是主力** — 免费注册 Developer Program，`/item_summary/search` 端点可直接搜索 sold listings，返回 JSON（价格 + 日期 + 链接 + 卖家），覆盖 US/DE/UK 三个核心市场。
2. **亚洲市场无官方 API** — 闲鱼、Mercari、Yahoo Auctions 均需网页抓取，反爬强度中到高。
3. **已有价格参考点**（调研确认）：
   - MI50: $182-520 (eBay US)
   - MI100: $2,088-2,499 (Newegg)
   - RX 7900 XTX: 各国均有成交记录

---

## 二、追踪 GPU 型号清单

### 计算卡 (Instinct)

| 型号 | 显存 | 架构 | 二手市场活跃度 |
|------|------|------|-------------|
| MI50 (16GB) | 16GB HBM2 | Vega 20 (GCN5) | 🟢 高 |
| MI50 (32GB) | 32GB HBM2 | Vega 20 (GCN5) | 🟡 中 |
| MI100 | 32GB HBM2 | CDNA1 | 🟡 中 |
| MI210 | 64GB HBM2e | CDNA2 | 🟠 低 |
| MI250 | 128GB HBM2e | CDNA2 | 🔴 极少 |
| MI250X | 128GB HBM2e | CDNA2 | 🔴 极少 |
| MI300X | 192GB HBM3 | CDNA3 | 🔴 极少 (新上市) |

### 消费卡 (Radeon — 可用于 ROCm)

| 型号 | 显存 | 架构 | 二手市场活跃度 |
|------|------|------|-------------|
| RX 6800 | 16GB GDDR6 | RDNA2 | 🟢 高 |
| RX 6800 XT | 16GB GDDR6 | RDNA2 | 🟢 高 |
| RX 6900 XT | 16GB GDDR6 | RDNA2 | 🟢 高 |
| RX 6950 XT | 16GB GDDR6 | RDNA2 | 🟡 中 |
| RX 7900 XT | 20GB GDDR6 | RDNA3 | 🟢 高 |
| RX 7900 XTX | 24GB GDDR6 | RDNA3 | 🟢 高 |
| RX 7900 GRE | 16GB GDDR6 | RDNA3 | 🟡 中 |

---

## 三、技术架构

```
                      每周定时运行 (cron: 0 3 * * 1)  ← 每周一凌晨 3 点
                                   │
              ┌────────────────────┼────────────────────┐
              │                    │                    │
     ┌────────▼────────┐  ┌───────▼────────┐  ┌───────▼────────┐
     │ eBay Price Fetcher│ │ Web Scrapers   │ │ Community APIs  │
     │ (Browse API)     │ │ (Xianyu/Mercari│ │ (Reddit/Keepa)  │
     │ US/DE/UK + 中文  │ │  Leboncoin等)   │ │                 │
     └────────┬────────┘  └───────┬────────┘  └───────┬────────┘
              │                    │                    │
              └────────────────────┼────────────────────┘
                                   │
                        ┌──────────▼──────────┐
                        │  price-normalizer.py │  ← 货币统一 (USD)
                        │  中位数/均值/最低价   │     条件加权
                        │  异常值过滤 (IQR)     │
                        └──────────┬──────────┘
                                   │
                        ┌──────────▼──────────┐
                        │  data/prices/        │
                        │  prices-2026-W17.json│  ← 每周快照
                        │  price-history.json  │  ← 历史趋势
                        └──────────┬──────────┘
                                   │
                        ┌──────────▼──────────┐
                        │  PriceChart.tsx      │  ← 前端组件
                        │  价格趋势图 + 对比表  │
                        │  来源链接标注         │
                        └──────────────────────┘
```

---

## 四、数据模型

### 每周价格快照 `price-history.json`

```json
{
  "updated": "2026-05-04T03:00:00Z",
  "currency": "USD",
  "rates": {
    "CNY": 7.25, "JPY": 149.5, "EUR": 0.92,
    "GBP": 0.79, "RUB": 98.5, "KRW": 1380
  },
  "cards": {
    "MI50_16GB": {
      "name": "AMD Instinct MI50 (16GB)",
      "prices": [
        {
          "country": "US",
          "platform": "eBay",
          "condition": "used",
          "currency": "USD",
          "local_price": 199.00,
          "usd_price": 199.00,
          "median": 215.00,
          "min": 150.00,
          "max": 350.00,
          "sample_size": 12,
          "source_url": "https://www.ebay.com/sch/i.html?_nkw=amd+instinct+mi50",
          "collected_at": "2026-05-04T02:30:00Z"
        },
        {
          "country": "CN",
          "platform": "闲鱼",
          "condition": "used",
          "currency": "CNY",
          "local_price": 1200.00,
          "usd_price": 165.52,
          "median": 1300.00,
          "min": 900.00,
          "max": 1800.00,
          "sample_size": 8,
          "source_url": "https://2.taobao.com/...",
          "collected_at": "2026-05-04T02:30:00Z"
        }
      ]
    }
  }
}
```

---

## 五、实现步骤

### 10.1 eBay API 集成 (P0 — 主力源)
- 注册 eBay Developer Program（免费）
- 生产环境 App ID 申请
- `search` 端点调用：按 GPU 型号搜索 sold listings
- 限速：5000 calls/day（免费层，足够用）
- 支持 US、DE、UK 三个站点

### 10.2 亚洲平台抓取器 (P1)
- **闲鱼**：Cookie 认证抓取，关键词搜索
- **Mercari JP**：公开 API 端点（mercari.com/jp/search/）
- **Yahoo Auctions JP**：RSS feed 或网页抓取

### 10.3 欧洲平台抓取器 (P1)
- **Leboncoin.fr**：网页抓取（无明显反爬）
- **Kleinanzeigen.de**：网页抓取
- 法国/德国/意大利均已 eBay 覆盖，本土平台做补充

### 10.4 价格标准化 (P1)
- 汇率转换（fixer.io 免费 API 或 ECB 汇率）
- 异常值过滤（IQR 方法，去除上下 1.5×IQR）
- 条件加权（开封 > 二手 > 维修过的 95%/85%/60%）
- 中位数作为主要参考价（抗异常值）

### 10.5 历史存储 + 趋势 (P2)
- 每周 JSON 快照存储在 `data/prices/`
- `price-history.json` 聚合 52 周趋势
- 自动标记价格突变（周波动 > 20%）

### 10.6 前端组件 (P2)
- `PriceTracker.tsx`：多卡片价格对比表 + 趋势折线图
- `PriceChart.tsx`：单卡 12 周价格走势
- 来源链接：每个价格点都有可点击的来源URL
- 支持国家/货币切换

### 10.7 CI 集成
- 新建 `sync-prices.yml`：每周一凌晨 3:00 UTC
- 汇率实时获取
- 价格变更 > 10% 发送通知

---

## 六、来源可信度标注

每个价格必须标注：

| 标注项 | 内容 |
|--------|------|
| 🏪 平台 | eBay / 闲鱼 / Mercari / Leboncoin ... |
| 📍 国家 | 🇺🇸 🇨🇳 🇯🇵 🇩🇪 🇫🇷 🇬🇧 🇷🇺 🇰🇷 🇮🇹 |
| 📅 采集日期 | 2026-05-04 |
| 📊 样本量 | 12 条成交记录 |
| 🔗 来源链接 | [查看搜索结果](url) |
| ⚠ 数据说明 | 中位数价格，不含运费，仅供参考 |

---

## 七、文件清单

| 文件 | 操作 | 说明 |
|------|------|------|
| `scripts/fetch-prices-ebay.py` | **新建** | eBay Browse API 价格抓取 |
| `scripts/fetch-prices-asia.py` | **新建** | 闲鱼/Mercari/雅虎拍卖抓取 |
| `scripts/fetch-prices-eu.py` | **新建** | Leboncoin/Kleinanzeigen 抓取 |
| `scripts/normalize-prices.py` | **新建** | 货币统一 + 异常值过滤 |
| `data/prices/price-history.json` | **新建** | 历史趋势数据 |
| `data/prices/prices-YYYY-Www.json` | **新建** | 每周价格快照 |
| `website/src/components/PriceTracker.tsx` | **新建** | 价格对比组件 |
| `website/src/components/PriceChart.tsx` | **新建** | 趋势图组件 |
| `website/docs/prices/index.mdx` | **新建** | 价格追踪页面 |
| `.github/workflows/sync-prices.yml` | **新建** | 每周价格同步 CI |
| `docs/plans/phase10-prices.md` | **新建** | 本文档 |

---

## 八、注意事项

| 注意项 | 说明 |
|--------|------|
| 法律合规 | 遵守各平台 robots.txt / ToS；仅抓取公开数据 |
| 价格仅供参考 | 标注"非投资建议，实际成交价可能因成色/地区而异" |
| API 限速 | eBay 5000 次/天，闲鱼/淘宝需间隔 3-5 秒 |
| 汇率波动 | 每周一固定时间获取 ECB 汇率 |
| 数据存储 | 历史快照保存 52 周，超过自动归档 |
| 隐私 | 不存储卖家信息，仅保留价格/型号/链接 |
