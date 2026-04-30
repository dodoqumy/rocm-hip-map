# 下阶段开发任务列表

**创建时间：** 2026-04-30
**依据：** docs/PROGRESS.md + plan-phase2.0-claude.md

---

## 优先级 P0 — 必须先完成

### 🔴 T1：合并翻译修复分支（5 分钟）

**当前状态：** 分支 `fix/translation-incremental-false-complete` 已 push，commit `add711b`
**操作：**
```bash
# 切到 main
git checkout main && git pull
# 合并
git merge fix/translation-incremental-false-complete
git push
```
**验证：** GitHub Actions 运行日志无报错

---

### 🔴 T2：全量重翻译 16 篇无效文件（30 分钟）

**背景：** audit 扫描发现 19 篇中仅 3 篇有效，16 篇伪翻译
**操作：** GitHub Actions → translate.yml → 手动触发
- `max_files`: `16`
- `model`: `big-pickle`
- `base_url`: `https://opencode.ai/zen/v1`
**验证：** `python3 scripts/audit_translations.py` → Valid ≥ 19

---

## 优先级 P1 — 高价值独立任务

### 🟡 T3：Phase 8.7 — 论文部署验证（30 分钟）

**任务：** 浏览器验证 5 篇论文页面可访问
**操作：** 访问 `https://dodoqumy.github.io/rocm-hip-map/` 检查论文分类页
**验证：** 无 404，页面加载正常

---

### 🟡 T4：Phase 9.5 — 多语言国旗标签（1 小时）

**任务：** 给语言标签加上国家旗帜 emoji
**文件：** `src/components/TagBadge.tsx` 或相关多语言组件
**示例：**
- ES → 🇪🇸
- DE → 🇩🇪
- JP → 🇯🇵
- KR → 🇰🇷
**验证：** 页面显示正确国旗

---

### 🟡 T5：Phase 7.1 — 文章正文嵌入修复（1 小时）

**任务：** 检查 MDX 生成后正文内容是否正确嵌入
**文件：** `scripts/generate-docs.py`
**验证：** 至少 3 篇文档正文可读（非空洞页面）

---

## 优先级 P2 — 中期扩展

### 🟢 T6：Phase 9.4 — 多语言翻译适配（2 小时）

**任务：** 实现 `xx→en→zh` 翻译链
**修改：** `scripts/translate.py` 新增 `--source-lang` 参数
**验证：** 一篇非英语文档翻译成功

---

### 🟢 T7：Phase 10.2-3 — 亚洲/欧洲价格平台（3 小时）

**任务：**
- 闲鱼/淘宝爬虫
- 日本 Mercari
- 欧洲 Leboncoin
**文件：** `scripts/fetch-asia.py`, `scripts/fetch-eu.py`
**验证：** JSON 数据抓取成功

---

## 优先级 P3 — Phase 2.0 前置

### 🔲 T8：Phase 9.7 — CI 多语言同步

**任务：** 新增 `sync-multilingual.yml`
**触发：** 每周

---

### 🔲 T9：Phase 7.2 — GitHub Issues 同步

**任务：** 修复 `sync-github.py` 速率限制问题
**文件：** `scripts/sync-github.py`

---

### 🔲 T10：Phase 7.4 — PyTorch/TF 文档

**任务：** 新增文档抓取

---

### 🔲 T11：Phase 7.5 — 中文学术论文

**任务：** 扩展论文采集

---

### 🔲 T12：Phase 7.7 — 图片 OCR 翻译

**任务：** 集成 Tesseract OCR

---

### 🔲 T13：Phase 7.8 — GA/Umami 分析

**任务：** 集成网站分析

---

## 执行顺序

```
T1(合并) → T2(重翻) → T3(论文验证) → T4(国旗) → T5(正文)
         ↑_______________________________并行_______________↓
```

---

## 修改文件预估

| 文件 | 涉及任务 |
|------|----------|
| `scripts/translate.py` | T2, T6 |
| `scripts/generate-docs.py` | T5 |
| `src/components/*.tsx` | T4, T5 |
| `.github/workflows/translate.yml` | T2 |
| `docs/PROGRESS.md` | T1-T13 完成后更新 |
| `docs/plan/phase2.0-*.md` | T8-T13 完成后更新 |

---

## 风险与依赖

- **T2 依赖 T1**：必须先合并才能用新判定逻辑
- **T4/T5 独立**：可并行推进
- **Phase 2.0**：T8-T13 全部完成后才启动

---

## 验证方法

每个任务完成后：
1. 运行 `python3 scripts/audit_translations.py`（涉及翻译时）
2. 本地 `npm run build` + `npm run start` 验证页面
3. 更新 PROGRESS.md 状态