# 翻译文本质量修复设计 — Phase 1A

**日期**：2026-05-04
**状态**：用户已认可，推进实施
**范围**：仅文本翻译逻辑修复（不含图片OCR、链接本地化）

---

## 一、问题根因

1. **术语表应用顺序错误**：先替换术语再翻译，导致 `ROCm（开放计算平台）` 被 API 二次翻译，出现 `ROCm（ROCm（开放计算平台））` 嵌套
2. **`max_tokens=4096` 限制**：长段落截断，导致大段未翻译
3. **`_is_translatable_paragraph()` 判断有误**：短引用（<60字符）直接跳过，可能误判含中英文字符的行
4. **翻译后无自检**：无法发现大段未翻译的英文段落

---

## 二、改进方案

### 2.1 修复术语表应用顺序

**当前逻辑**（`translate.py` 第 210 行）：
```python
text = _apply_glossary(text, glossary)  # 先替换术语
# 然后调用 API
```

**改为**：先翻译，后替换术语（避免 API 二次翻译）

注意：`translate.py` 中现有翻译调用函数为 `call_llm()`（第 139-171 行），我们将在 2.5 节封装为 `_call_translation_api()` 增加重试逻辑。

```python
# 1. 先翻译（将使用封装后的 _call_translation_api，见 2.5 节）
translated = _call_translation_api(text)
# 2. 后替换术语（确保术语一致性）
translated = _apply_glossary(translated, glossary)
```

**注意**：术语表中的英文术语在翻译后可能已被翻译，需要：
- 方案 A：术语表包含中英文映射，在翻译后替换时匹配中文术语
- 方案 B：翻译前用占位符标记术语，翻译后替换占位符

**推荐方案 B**（更可靠）：
```python
import re

def _mark_terms_with_placeholders(text, glossary):
    """用占位符标记术语，避免 API 翻译"""
    placeholders = {}
    marked_text = text
    for i, (en_term, zh_term) in enumerate(glossary.items()):
        placeholder = f"__TERM_{i}__"
        # 只替换完整单词（避免部分匹配）
        pattern = r'\b' + re.escape(en_term) + r'\b'
        if re.search(pattern, marked_text):
            placeholders[placeholder] = zh_term
            marked_text = re.sub(pattern, placeholder, marked_text)
    return marked_text, placeholders

def _replace_placeholders(translated, placeholders):
    """将占位符替换为中文术语"""
    result = translated
    for placeholder, zh_term in placeholders.items():
        result = result.replace(placeholder, zh_term)
    return result
```

### 2.2 优化分段策略

**当前问题**：`split_markdown()` 按空行分段落，长段落可能超过 4096 tokens

**改进**：增加段落长度检查，按句子边界二次分割
```python
def _split_long_paragraph(paragraph, max_chars=3000):
    """按句子边界分割超长段落"""
    if len(paragraph) <= max_chars:
        return [paragraph]
    
    # 按句子边界分割（. ! ? 后跟空格或结束）
    sentences = re.split(r'(?<=[.!?])\s+', paragraph)
    
    chunks = []
    current_chunk = ""
    for sentence in sentences:
        if len(current_chunk) + len(sentence) <= max_chars:
            current_chunk += sentence + " "
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = sentence + " "
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks
```

**集成到 `translate.py`**：
```python
def split_markdown(text):
    """按空行分段，并对超长段落二次分割"""
    paragraphs = text.split('\n\n')
    result = []
    for para in paragraphs:
        if len(para) > 3000:  # 超长段落
            result.extend(_split_long_paragraph(para))
        else:
            result.append(para)
    return result
```

### 2.3 修复跳过逻辑

**当前**（`translate.py` 第 331 行）：短引用（<60字符）直接跳过  
**问题**：可能误判包含中英文字符的行

**改进**：仅跳过纯符号/数字/链接行
```python
def _is_translatable_paragraph(text):
    """判断段落是否需要翻译"""
    # 去除空白
    text = text.strip()
    if not text:
        return False
    
    # 跳过纯符号/数字/链接
    if re.match(r'^[\s\*\-\d\.\/]*$', text):
        return False
    
    # 如果包含中英文字符，即使 <60 字符也翻译
    if re.search(r'[\u4e00-\u9fff\u3040-\u30ff]', text):
        return True
    
    # 如果包含英文字符且长度 >10，翻译
    if re.search(r'[a-zA-Z]', text) and len(text) > 10:
        return True
    
    return False
```

### 2.4 增加翻译后自检

**新增函数**：检测大段未翻译的英文
```python
def _check_translation_quality(original, translated):
    """检查翻译质量，返回 (is_ok, issues)"""
    issues = []
    
    # 1. 检测大段未翻译（连续 >50 个英文字符）
    long_english = re.findall(r'[a-zA-Z][a-zA-Z\s,\.!?;:]{49,}', translated)
    if long_english:
        issues.append(f"未翻译段落: {len(long_english)} 处")
    
    # 2. 检测术语嵌套（如 ROCm（ROCm（...）））
    nested_terms = re.findall(r'(\w+（\1（)', translated)
    if nested_terms:
        issues.append(f"术语嵌套: {nested_terms}")
    
    return len(issues) == 0, issues
```

**集成到翻译流程**：
```python
def translate_text(text, glossary):
    # 1. 标记术语占位符
    marked_text, placeholders = _mark_terms_with_placeholders(text, glossary)
    
    # 2. 翻译
    translated = _call_translation_api(marked_text)
    
    # 3. 替换占位符
    translated = _replace_placeholders(translated, placeholders)
    
    # 4. 自检
    is_ok, issues = _check_translation_quality(text, translated)
    if not is_ok:
        # 重试一次
        translated = _call_translation_api(marked_text)
        translated = _replace_placeholders(translated, placeholders)
        is_ok, issues = _check_translation_quality(text, translated)
        
    return translated, is_ok, issues
```

### 2.5 改进 API 调用健壮性

**当前**：`call_llm()` 使用 `urllib`，超时可能无清晰错误  
**改进**：增加重试逻辑（指数退避）
```python
import time

def _call_translation_api(text, max_retries=3):
    """调用翻译 API，带重试逻辑"""
    for attempt in range(max_retries):
        try:
            result = call_llm(text)  # 原有调用逻辑
            if result and len(result) > 10:  # 基本有效性检查
                return result
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            time.sleep(2 ** attempt)  # 指数退避：1s, 2s, 4s
    
    return ""  # 所有重试失败
```

**移除无条件 `time.sleep(2)`**：仅在 API 调用后按需延迟（rate limit 处理）
```python
# 原 translate.py 第 563 行（在 verify.py 中）
# 改为：只有实际调用了 LLM 才 sleep
if api_was_called:
    time.sleep(2)  # LLM rate limit
```

---

## 三、可量化的验收标准

| 验收项 | 测试方法 | 通过标准 |
|--------|---------|---------|
| 术语不再嵌套 | 翻译 `ROCm` 相关文档，检查输出 | 无 `ROCm（ROCm（...））` 嵌套，术语格式统一为 `ROCm（开放计算平台）` |
| 长段落无未翻译 | 选择 3 个超长文档（>5000 字符）翻译 | 翻译后检测：连续 >50 个英文字符的段落数为 0 |
| 短行正确翻译 | 翻译包含短标题、列表项的文档 | 所有包含中英文字符的行均被翻译（无跳过） |
| API 调用不 sleep（无 API 调用时） | 翻译 10 篇无翻译文件的文章（只检查是否需要翻译） | 总耗时 < 20 秒（无 API 调用时不 sleep） |
| 翻译后自检生效 | 人为构造未翻译段落（>50 英文字符），运行翻译 | 检测到未翻译，重试或标记 `needs_review` |
| 重试逻辑生效 | 模拟 API 失败（临时改 endpoint），运行翻译 | 在 3 次重试后失败，或成功重试 |

---

## 四、测试策略

### 4.1 单元测试（针对新增函数）
- `_mark_terms_with_placeholders()`：测试术语标记和占位符替换
- `_split_long_paragraph()`：测试超长段落分割
- `_is_translatable_paragraph()`：测试各种边界情况
- `_check_translation_quality()`：测试未翻译检测和术语嵌套检测

### 4.2 集成测试
- 翻译 5 个已知问题文档（包含术语嵌套、长段落、短行）
- 对比翻译前后的质量指标（未翻译段落数、术语一致性）

### 4.3 回归测试
- 翻译 10 个历史翻译文件，确保新逻辑不降低质量
- 对比新旧翻译结果（人工抽查）

---

## 五、后续阶段（Phase 1B、1C）

用户选择分阶段实施：
- ✅ **Phase 1A**（本设计）：文本翻译逻辑修复
- ⬜ **Phase 1B**：图片 OCR + 重绘管线
- ⬜ **Phase 1C**：链接本地化

---

## 六、风险提示

1. **占位符方案可能失败**：如果 API 修改了占位符格式（如添加空格），替换会失败  
   **缓解**：翻译后检查占位符是否都存在，缺失则重试

2. **分段可能破坏 Markdown 格式**：按句子分割可能拆分代码块、列表等  
   **缓解**：在 `split_markdown()` 中保留代码块（```）和列表的完整性

3. **deepseek-v4-flash 质量可能仍不理想**：即使修复逻辑，模型本身质量有限  
   **缓解**：本阶段先修复逻辑，质量提升有限；后续可考虑升级模型（Phase 2）

---

**设计状态**：✅ 完成，待用户审查和推进实施
