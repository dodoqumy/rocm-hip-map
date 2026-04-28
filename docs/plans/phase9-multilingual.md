# Phase 9: 多语言一手情报检索与翻译模块

> 创建日期：2026-04-28 | 状态：📋 计划阶段

---

## 一、调研结论

### 多语言 ROCm/HIP 一手资源已验证存在

| 区域 | 语言 | 关键机构/来源 | 资源类型 | 已确认 |
|------|------|-------------|---------|--------|
| 🇫🇮 芬兰 | fi, en | **CSC** (LUMI 超算) | ROCm 教程, 用户指南, 性能报告 | ✅ |
| 🇫🇷 法国 | fr, en | **GENCI, CEA, INRIA** | 超算文档, 研究报告, Alice Recoque | ✅ |
| 🇩🇪 德国 | de, en | **Jülich, LRZ, HLRS, Fraunhofer** | HPC 论文, 教程, EuroHPC 项目 | ✅ |
| 🇮🇹 意大利 | it, en | **CINECA** (Leonardo 超算) | HPC 文档, 培训材料 | ✅ |
| 🇯🇵 日本 | ja, en | **AMD Japan, RIKEN** | AMD HEROES 活动, 企业技术文档 | ✅ |
| 🇷🇺 俄罗斯 | ru | **超算社区, 大学** | GPU 论文, Instinct mod 社区 | ⚠ 碎片化 |
| 🇪🇸 西班牙 | es | **BSC** (MareNostrum) | HPC 文档 | ✅ |
| 🇳🇱 荷兰 | nl, en | **SURF** (Dutch HPC) | 研究论文 | ✅ |
| 🇰🇷 韩国 | ko | **KISTI, Samsung** | HPC 论文, 企业研究 | ⚠ 待确认 |
| 🇸🇪 瑞典 | sv, en | **KTH, ENCCS** | ROCm 培训 | ✅ |

### 核心发现

1. **LUMI 是金矿**：380 PFlop/s、11912 块 AMD MI250X GPU 的欧洲最大超算。CSC 定期举办 ROCm 开发培训，产出芬兰语 + 英语材料。
2. **EuroHPC JU**：欧洲 8 台超算中至少 3 台用 AMD GPU（LUMI、Leonardo、Alice Recoque），产出法/德/意/芬/英五种语言材料。
3. **AMD 官方多语言活动**：日本 AMD HEROES、中国 AMD ROCm 中文站、欧洲各 HPC 中心的 ROCm 工作坊。

---

## 二、各语言检索策略

### 2.1 芬兰语 (fi)

```
源：CSC.fi 官方文档 + LUMI 用户门户
检索词：(ROCm OR HIP OR AMD GPU) AND (laskenta OR ohjelmointi OR optimointi) site:csc.fi
抓取：CSC 培训材料、性能报告、用户指南
```

### 2.2 法语 (fr)

```
源：HAL (法国开放科学存档), CEA, GENCI, INRIA
检索词：(ROCm OR HIP OR calcul GPU) AMD
抓取：GENCI 白皮书、CEA 技术报告、INRIA 研究论文
```

### 2.3 德语 (de)

```
源：arXiv (德国机构), Jülich JuSER, LRZ 文档
检索词：(ROCm OR HIP OR GPU) AND (Hochleistungsrechnen OR Beschleuniger)
抓取：Jülich 技术报告、LRZ 用户文档、Fraunhofer 研究
```

### 2.4 日语 (ja)

```
源：CiNii (日本学术), J-STAGE, AMD Japan
检索词：(ROCm OR HIP OR GPU) AND (計算 OR 高速化 OR 並列)
抓取：学术论文、AMD Japan 技术博客、大学研究报告
```

### 2.5 俄语 (ru)

```
源：eLibrary.ru, CyberLeninka, arXiv (RU authors)
检索词：(ROCm OR HIP OR AMD GPU) AND (вычисления OR ускоритель)
抓取：学术论文、超算中心报告
```

### 2.6 意大利语 (it)

```
源：CINECA 门户, AIR (意大利开放存档)
检索词：(ROCm OR HIP OR GPU) AMD
抓取：CINECA 培训材料、意大利大学论文
```

### 2.7 韩语 (ko)

```
源：KISTI, RISS (韩国学术)
检索词：(ROCm OR HIP OR AMD GPU) AND (계산 OR 프로그래밍)
抓取：KISTI 论文、三星/海力士 GPU 研究
```

---

## 三、技术架构

```
                    多语言抓取层
    ┌───────────────────┼───────────────────┐
    │                   │                   │
    ▼                   ▼                   ▼
fetch-eu.py        fetch-asia.py      fetch-ru.py
(芬兰/法/德/意)     (日本/韩国)         (俄罗斯)
    │                   │                   │
    └───────────────────┼───────────────────┘
                        │
              ┌─────────▼──────────┐
              │  data/articles.json │
              │  + lang: fi/fr/de.. │
              └─────────┬──────────┘
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
    translate.py   classify.py   generate-docs.py
   (多语言→中/英)  (语言+领域标签)  (多语言页面)
          │             │             │
          ▼             ▼             ▼
  content/translated/  website/docs/  侧边栏: 🌐 多语言情报
```

### 与现有管道的差异

| 维度 | 英文官方文档 | 多语言情报 |
|------|------------|-----------|
| 源类型 | 单一（rocm.docs） | 分散（10+ 网站） |
| 检索方式 | 固定 URL 列表 | 搜索引擎 + API |
| 语言检测 | 不需要 | langdetect 自动识别 |
| 翻译方向 | en→zh | xx→zh + xx→en（双语产出） |
| 可信度 | 5（官方） | 3-5（按来源评级） |
| 更新频率 | 每日 | 每周（变化慢） |
| 去重 | arxiv_id/url | url + content hash |

---

## 四、翻译策略（多语言特化）

### 4.1 翻译方向

```
原文 (fi/fr/de/ja/ru/...) 
  ├─→ 中文 (zh) — 用于网站展示
  └─→ 英文 (en) — 用于对照 + SEO（Google 索引）
```

### 4.2 多语言翻译 Prompt（与英文不同）

```
You translate {source_lang} GPU/HPC technical content to {target_lang}.
The text is about AMD ROCm/HIP GPU programming.

Rules:
1. Preserve all code, commands, API names, hardware names unchanged.
2. Translate technical explanations accurately in {target_lang}.
3. For Finnish/German compound nouns, break into standard {target_lang} phrasing.
4. For Japanese, preserve honorific forms in technical context naturally.
5. Output ONLY the translation.
```

### 4.3 翻译成本估算

| 源语言 | 预计数量 | 每篇 tokens | 总 tokens |
|--------|---------|------------|----------|
| 芬兰语 | 10-20 | ~2000 | ~40K |
| 法语 | 15-30 | ~2500 | ~75K |
| 德语 | 10-25 | ~2500 | ~62K |
| 日语 | 15-30 | ~2000 | ~60K |
| 俄语 | 5-15 | ~2500 | ~37K |
| 意大利语 | 5-15 | ~2000 | ~30K |
| 韩语 | 5-10 | ~2000 | ~20K |
| **合计** | **65-145** | | **~325K** |

> opencode 免费端点 325K tokens ≈ 可承受（deepseek-v4-pro 免费额度充足）

---

## 五、来源可信度评级体系

| 可信度 | 标准 | 示例 |
|--------|------|------|
| ⭐⭐⭐⭐⭐ | 官方文档/官方博客 | AMD 官方多语言站、CSC 官方教程 |
| ⭐⭐⭐⭐ | 国家超算中心/顶级大学 | GENCI、Jülich、CINECA、RIKEN |
| ⭐⭐⭐ | 大学/研究机构论文 | 各国大学 GPU 研究（经 peer review） |
| ⭐⭐ | 社区/个人博客 | 开发者博客、社区论坛 |
| ⭐ | 未验证来源 | 匿名/低可信度来源（不收录） |

---

## 六、具体实现文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `scripts/fetch-eu.py` | **新建** | 欧洲多语言源抓取 |
| `scripts/fetch-asia.py` | **新建** | 亚洲多语言源抓取 |
| `config/sources.yaml` | **新建** | 多语言源配置（URL、检索词、频率） |
| `data/multilingual-sources.json` | **新建** | 多语言源索引 |
| `scripts/translate.py` | 修改 | 增加 `--source-lang` 参数 + 多语言 prompt |
| `scripts/classify.py` | 修改 | 增加语言标签自动识别 |
| `scripts/generate-docs.py` | 修改 | `source_org` 扩展到各国机构 |
| `website/src/components/ArticleMeta/index.tsx` | 修改 | 新增语言国旗图标 |
| `.github/workflows/sync-multilingual.yml` | **新建** | 每周多语言同步 CI |

---

## 七、分阶段实施（3 个阶段）

### Phase 9.1 — 欧洲核心（芬兰 + 法国 + 德国）
- LUMI/CSC 材料（芬兰语 + 英语）— 最丰富
- GENCI/CEA 法语文档
- Jülich/LRZ 德语文档
- 预计产出：30-50 篇

### Phase 9.2 — 亚洲核心（日本 + 韩国）
- J-STAGE/CiNii 日语论文
- AMD Japan 技术博客
- KISTI 韩国论文
- 预计产出：20-40 篇

### Phase 9.3 — 扩展（俄罗斯 + 意大利 + 其他）
- eLibrary/CyberLeninka 俄语论文
- CINECA 意大利语材料
- BSC 西班牙语文档
- 预计产出：15-30 篇

---

## 八、风险与缓解

| 风险 | 缓解 |
|------|------|
| 非英语 LLM 翻译质量差 | deepseek-v4-pro 支持多语言，先用小样本验证 |
| 芬兰语/韩语等小语种翻译差 | 降级策略：xx→en 用 LLM，en→zh 用现有管道 |
| 源网站反爬 | 礼貌间隔（5s），User-Agent 声明，尊重 robots.txt |
| PDF 提取质量 | PyMuPDF（已在 Phase 8 验证） |
| 法律/版权风险 | 仅收录公开预印本/官方文档，标注来源链接 |
