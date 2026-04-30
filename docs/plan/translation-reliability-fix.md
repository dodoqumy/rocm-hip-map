# 翻译可靠性修复方案

## 问题根因

### 问题1：增量完成判定过于粗糙
- 原逻辑：`_zh.md` 存在且 > 200B 就跳过
- 问题：很多 `_zh.md` 实际是英文原文（API 失败 fallback），被误判为已翻译

### 问题2：翻译失败时写入英文原文
- 原逻辑：API 失败时 `translated_parts.append(seg["content"])` 写入原文
- 问题：生成伪 `_zh.md`，被误判为成功

### 问题3：统计误导
- 原输出：`5 translated, 0 resumed, 63 skipped`
- 问题：实际可能 0 篇真正翻译

---

## 修复方案

### 1. 新增 `is_valid_translation()` 函数
```python
def is_valid_translation(path: Path) -> bool:
    # 规则：
    # 1. 文件存在
    # 2. 大于 200 bytes
    # 3. 含中文字符
    # 4. 中文占比 > 3%
```

### 2. 修改增量判定
```python
# 旧
if zh_file.exists() and zh_file.stat().st_size > MIN_VALID_SIZE:

# 新
if is_valid_translation(zh_file):
```

### 3. 翻译失败时不写原文
```python
# 旧
else:
    translated_parts.append(seg["content"])

# 新
else:
    failed_count += 1
    # 不写入原文，保持空白让 is_valid_translation 检测
```

### 4. 修复统计输出
```python
# 旧
📊 5 translated, 0 resumed, 63 skipped

# 新
📊 Success: 5, Failed: 0, Skipped(valid): 63, Remaining: 0
```

### 5. 新增诊断脚本
`scripts/audit_translations.py` 输出：
- 无中文文件
- 小于 200B 文件
- 疑似英文伪翻译
- 总数统计

---

## 修改文件列表

| 文件 | 修改内容 |
|------|----------|
| `scripts/translate.py` | 添加 is_valid_translation，修改判定和统计逻辑 |
| `scripts/audit_translations.py` | 新增诊断脚本 |
| `.github/workflows/translate.yml` | 添加 audit step |

---

## 后续优化建议

1. **自动修复断点**：cron job 检测到失败自动重试
2. **失败告警**：连续失败 3 次发送通知
3. **翻译质量评分**：基于中文占比打分