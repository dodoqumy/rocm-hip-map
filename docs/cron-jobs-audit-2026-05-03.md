# Cron 任务审计报告 — 2026-05-03

## 一、成功执行的任务

### 1. `sync.yml` 链路（已完成）

- **`scripts/fetch-official.py`**
  - 预期结果：获取 AMD 官方 ROCm 文档的所有可用文章
  - 实际结果：**1288** 篇英文文章（`data/articles.json` 记录）
  - 评价：❌ 数量不足，远未达到官方文档实际体量

- **`scripts/sync-github.py`**
  - 预期结果：同步 `ROCm/rocm-docs` 等仓库的所有 Issues
  - 实际结果：仅 **215** 条 Issue 记录
  - 评价：❌ 数量严重不足，大量 Issue 未被获取

- **`scripts/classify.py`**
  - 预期结果：对全部 1288 篇文章完成分类打标
  - 实际结果：`data/known-issues.json` 已生成
  - 评价：✅ 流程走通，但分类覆盖是否完整未验证

- **`scripts/release-watch.py`**
  - 预期结果：追踪所有监控仓库的最新 Release
  - 实际结果：`data/versions.json` 已生成
  - 评价：✅ 流程走通

### 2. `papers.yml` 链路（已完成）

- **`scripts/fetch-papers.py`**
  - 预期结果：获取所有 ROCm 相关学术论文
  - 实际结果：**88** 篇论文 Markdown
  - 评价：❌ 数量偏少，学术数据源覆盖不足

- **`scripts/extract-pdf.py --limit 3`**
  - 预期结果：提取 3 篇 PDF 全文内容
  - 实际结果：3 篇提取完成
  - 评价：✅ 符合预期

- **复制到 `website/static/data/papers.json`**
  - 预期结果：静态数据文件更新
  - 实际结果：复制完成
  - 评价：✅ 符合预期

### 3. 翻译审计（已完成，质量堪忧）

- **`scripts/translate.py --incremental --max-files 5`**（经两次恢复）
  - 预期结果：5 篇高质量中文翻译文档
  - 实际结果：5 篇"有效"翻译（最终规范化结果）
  - 翻译文件列表：
    - `amdsmi-latest_projects_amdsmi_en_latest_conceptual_ras_zh.md`
    - `rocm-docs-latest_en_latest_how-to_programming_guide_zh.md` ⚠️（后续检查为无效翻译）
    - `rocm-docs-latest_en_latest_conceptual_gpu-arch_zh.md`
    - `rocm-docs-latest_en_latest_how-to_tuning-guides_mi300x_index_zh.md`
    - `rocm-docs-latest_en_latest_how-to_build-rocm_zh.md`
  - 总翻译文件数：**29**（含历史翻译）
  - 评价：❌ 翻译质量非常差，大段未翻译，缺少图片处理

### 4. `sync-prices.yml` 链路（已推迟）

- **`scripts/fetch-prices-ebay.py --dry-run`**
  - 预期结果：入口点结构可运行
  - 实际结果：dry-run 成功
  - 状态：**已推迟** — `EBAY_APP_ID` 和 `EBAY_CERT_ID` 未就绪
  - 评价：⏸️ 仅验证入口，线上 API 未测试

---

## 二、执行失败 / 不完整的任务

### 5. `verify.py` 验证（失败）

- **`scripts/verify.py --dry-run`**
  - 预期结果：验证逻辑可运行
  - 实际结果：成功
  - 评价：✅ 入口正常

- **`scripts/verify.py --stamp`**（完整验证）
  - 预期结果：1288 篇文章验证报告 + `summary.json`
  - 实际结果：仅 **645** 个报告（超时中断），`summary.json` **未生成**
  - 失败原因：无条件 `time.sleep(2)` 导致全量验证不可行（1288 篇需约 43 分钟无意义等待）
  - 评价：❌ **验证标准糊弄** — 所有文章问题都没有验证出来，更别提翻译准确性

---

## 三、翻译质量检查（最新 5 个翻译文件）

| 文件名 | 是否有效 | 问题 |
|--------|----------|------|
| `rocm_en_latest_how-to_programming_guide_zh.md` | ❌ 无效 | `is_valid_translation(...)` 返回 `False`，大段未翻译 |
| `amdsmi-latest_projects_amdsmi_en_latest_conceptual_ras_zh.md` | ✅ 有效 | — |
| `rocm-docs-latest_en_latest_conceptual_gpu-arch_zh.md` | ✅ 有效 | — |
| `rocm-docs-latest_en_latest_how-to_tuning-guides_mi300x_index_zh.md` | ✅ 有效 | — |
| `rocm-docs-latest_en_latest_how-to_build-rocm_zh.md` | ✅ 有效 | — |

**严重质量问题总结：**

1. ❌ **所有爬取文章数量都不够** — `fetch-official.py` 仅 1288 篇、`sync-github.py` 仅 215 条，远未达到官方实际数据量
2. ❌ **翻译质量非常差** — 已翻译文章中经常看到大段未翻译的英文原文
3. ❌ **缺少图片处理** — 未对图片中的英文文字进行 OCR → 翻译 → 重生成对照图片
4. ❌ **链接未替换** — 翻译后的文章中，link 链接仍然是原英文地址，应该替换成本地已翻译的对应页面（TODO：都翻译完再统一处理）
5. ❌ **验证标准糊弄** — `verify.py` 所有文章问题都没有验证出来，更别提翻译准确性检查

---

## 四、输出快照

| 指标 | 数值 |
|------|------|
| 英文原文数量 | **1288** |
| GitHub Issue 数量 | **215** |
| 翻译文件数量 | **29** |
| 验证报告数量 | **645**（共应 1288） |
| 验证摘要存在 | **否** |
| 论文 Markdown 数量 | **88** |
| 价格 JSON 数量 | **0**（已推迟） |
| `data/articles.json` | ✅ 存在 |
| `data/versions.json` | ✅ 存在 |
| `data/known-issues.json` | ✅ 存在 |
| `data/papers.json` | ✅ 存在 |

---

## 五、关键发现

### `classify.py` vs `classify_v2.py`
- `classify.py` 是当前接入 `sync.yml` 的生产分类器
- `classify_v2.py` 未接入任何工作流，仍是原型 / 未来选项

### 翻译流水线发现
- `scripts/translate.py --incremental` 按字典序优先选择 Doxygen/HTML 生成页面，不适合有界审计
- 小型、人类可读的 Markdown 文档翻译可靠且快速
- **严重缺陷**：翻译质量无保障，图片未处理，链接未本地化

### 验证流水线发现
- `scripts/verify.py` 无法在合理时间内完成 1288 篇文章的完整验证
- 无条件 `time.sleep(2)` 导致每次即使无 LLM 调用也会等待
- **严重缺陷**：验证标准糊弄，所有文章问题都没检测出来

---

## 六、推迟的 TODO

### `sync-prices.yml` 线上验证
**原因**：`EBAY_APP_ID` 和 `EBAY_CERT_ID` 尚未就绪

**推迟步骤**：
1. 运行 `python3 scripts/fetch-prices-ebay.py --site EBAY-US`
2. 运行 `python3 scripts/fetch-prices-ebay.py --site EBAY-DE`
3. 运行 `python3 scripts/fetch-prices-ebay.py --site EBAY-UK`
4. 运行 `python3 scripts/normalize-prices.py`
5. 生成 `data/prices/prices-latest.json`
6. 验证多区域标准化输出

**当前审计状态**：脚本入口点仅通过 dry-run 验证；线上 API 路径有意推迟。

---

## 七、建议与后续行动

### 立即修复（高优先级）

1. **修复爬取数量不足问题**
   - 检查 `fetch-official.py` 是否有遗漏的文档源
   - 检查 `sync-github.py` 的 API 分页 / 时间范围设置
   - 检查 `fetch-papers.py` 的数据源覆盖

2. **修复翻译质量**
   - 解决大段未翻译问题（检查翻译 API 调用逻辑）
   - 实现图片文字处理流水线：OCR (Tesseract/PaddleOCR) → 翻译（术语表约束）→ 图像编辑（PIL/OpenCV）重生成对照图片
   - 将翻译后文章中的链接替换为本地已翻译页面

3. **修复验证标准**
   - 重新设计 `verify.py` 的验证逻辑（移除无条件 `time.sleep(2)`）
   - 至少能检测出明显的文章格式 / 链接问题
   - 增加翻译准确性检查（对比原文与译文的关键术语）

### 长期优化

4. 保持 `classify.py` 作为当前工作流分类器，直到有意向迁移 `classify_v2.py` 的计划
5. 在信任 `scripts/verify.py` 作为每日全仓库验证器之前，彻底重构其验证逻辑
6. 重新检查现有遗留翻译文件（如 `rocm_en_latest_how-to_programming_guide_zh.md`）

---

**审计执行环境**：隔离 worktree `feature/cron-job-audit-exec`，未 commit / 未 merge / 未 push
