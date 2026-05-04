# 翻译文本质量修复实施计划 — Phase 1A

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 修复翻译文本质量（术语嵌套、长段落未翻译、短行跳过、无自检）

**Architecture:** 使用占位符方案B避免术语二次翻译；按句子边界分割超长段落；改进跳过逻辑识别中英文混合行；增加翻译后自检和API重试逻辑。

**Tech Stack:** Python 3, re (regex), deepseek-v4-flash API

---

### Task 1: 添加术语占位符函数

**Files:**
- Modify: `scripts/translate.py:41-77` (在 `load_glossary()` 后添加)

- [ ] **Step 1: 添加 `_mark_terms_with_placeholders()` 函数**

```python
def _mark_terms_with_placeholders(text: str, glossary: dict) -> tuple[str, dict]:
    """用占位符标记术语，避免 API 翻译术语"""
    placeholders = {}
    marked_text = text
    mapping = glossary.get("mapping", {})
    
    # 按术语长度降序，避免部分匹配
    sorted_terms = sorted(mapping.items(), key=lambda x: -len(x[0]))
    
    for i, (en_term, info) in enumerate(sorted_terms):
        placeholder = f"__TERM_{i}__"
        # 只替换完整单词（避免部分匹配）
        pattern = r'\b' + re.escape(en_term) + r'\b'
        if re.search(pattern, marked_text):
            placeholders[placeholder] = info["zh"]
            marked_text = re.sub(pattern, placeholder, marked_text)
    
    return marked_text, placeholders
```

- [ ] **Step 2: 添加 `_replace_placeholders()` 函数**

```python
def _replace_placeholders(translated: str, placeholders: dict) -> str:
    """将占位符替换为中文术语"""
    result = translated
    for placeholder, zh_term in placeholders.items():
        result = result.replace(placeholder, zh_term)
    return result
```

- [ ] **Step 3: 运行测试验证函数**

Run: `python3 -c "
from scripts.translate import _mark_terms_with_placeholders, _replace_placeholders
glossary = {'terms': [{'en': 'ROCm', 'zh': 'ROCm（开放计算平台）', 'keep_original': False}], 'mapping': {'ROCm': {'zh': 'ROCm（开放计算平台）', 'keep_original': False}}}
text = 'ROCm is a platform. ROCm provides HIP.'
marked, ph = _mark_terms_with_placeholders(text, glossary)
print('Marked:', marked)
result = _replace_placeholders('__TERM_0__ 是一个平台。__TERM_0__ 提供 HIP。', ph)
print('Result:', result)
"`
Expected: Marked 文本中 ROCm 被 `__TERM_0__` 替换，替换后恢复为 `ROCm（开放计算平台）`

- [ ] **Step 4: Commit**

```bash
git add scripts/translate.py
git commit -m "feat(translate): add term placeholder functions to prevent double-translation"
```

---

### Task 2: 修改 `translate()` 函数使用占位符方案

**Files:**
- Modify: `scripts/translate.py:189-226` (修改 `translate()` 函数)

- [ ] **Step 1: 先翻译后替换术语**

修改 `translate()` 函数（第 209-210 行）：
```python
def translate(text: str, glossary: dict, mode: str = "doc") -> Optional[tuple[str, bool, list]]:
    """统一翻译入口，自动选择后端。返回 (翻译结果, 是否成功, 问题列表)"""
    provider = os.environ.get("TRANSLATE_PROVIDER", "deepseek")
    api_key = os.environ.get("TRANSLATE_API_KEY", "")
    
    if not api_key:
        print("  ⚠ No TRANSLATE_API_KEY set — skipping translation")
        return None, False, ["no_api_key"]
    
    # 1. 标记术语占位符
    marked_text, placeholders = _mark_terms_with_placeholders(text, glossary)
    
    # 2. 翻译（使用封装后的 API 调用，见 Task 6）
    translated = _call_translation_api(marked_text, mode)
    
    if not translated:
        return None, False, ["api_call_failed"]
    
    # 3. 替换占位符
    translated = _replace_placeholders(translated, placeholders)
    
    # 4. 自检（见 Task 5）
    is_ok, issues = _check_translation_quality(text, translated)
    
    return translated, is_ok, issues
```

- [ ] **Step 2: 更新调用点**

修改 `translate_markdown_file()` 第 338 行：
```python
# 原代码：
# translated = translate(text, glossary, mode=mode)

# 改为：
translated, is_ok, issues = translate(text, glossary, mode=mode)
if translated:
    translated_parts.append(translated)
    if not is_ok:
        print(f"  ⚠ Translation quality issues: {issues}")
else:
    failed_count += 1
```

- [ ] **Step 3: 运行测试验证**

Run: `python3 scripts/translate.py --file <path_to_test_file> --dry-run`
Expected: 翻译后无 `ROCm（ROCm（...））` 嵌套，术语格式统一

- [ ] **Step 4: Commit**

```bash
git add scripts/translate.py
git commit -m "feat(translate): use placeholder approach to prevent term double-translation"
```

---

### Task 3: 添加长段落分割函数

**Files:**
- Modify: `scripts/translate.py:231-292` (在 `split_markdown()` 前添加)

- [ ] **Step 1: 添加 `_split_long_paragraph()` 函数**

```python
def _split_long_paragraph(paragraph: str, max_chars: int = 3000) -> list:
    """按句子边界分割超长段落"""
    if len(paragraph) <= max_chars:
        return [paragraph]
    
    # 按句子边界分割（. ! ? 后跟空格或结束）
    # 保留分隔符
    parts = re.split(r'(?<=[.!?])\s+', paragraph)
    
    chunks = []
    current_chunk = ""
    
    for part in parts:
        if len(current_chunk) + len(part) <= max_chars:
            current_chunk += part + " "
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = part + " "
    
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks
```

- [ ] **Step 2: 修改 `split_markdown()` 集成长段落分割**

修改 `split_markdown()` 函数（第 231-292 行）：
```python
def split_markdown(content: str) -> list:
    """将 Markdown 分割为可翻译段落和不可翻译块。"""
    segments = []
    lines = content.split("\n")
    i = 0
    in_code = False
    in_frontmatter = False
    buffer = []
    
    while i < len(lines):
        line = lines[i]
        
        # ... [保持原有的 frontmatter、code block 处理逻辑不变] ...
        
        if in_code:
            buffer.append(line)
            i += 1
            continue
        
        if line.strip() == "" and buffer:
            if any(l.strip() for l in buffer):
                # 对段落进行长度检查
                para = "\n".join(buffer)
                if len(para) > 3000:
                    # 超长段落二次分割
                    sub_paras = _split_long_paragraph(para)
                    for sub_para in sub_paras:
                        segments.append({"type": "paragraph", "content": sub_para})
                else:
                    segments.append({"type": "paragraph", "content": para})
                buffer = []
            else:
                if any(l.strip() for l in buffer):
                    para = "\n".join(buffer)
                    segments.append({"type": "paragraph", "content": para})
                buffer = []
        
        i += 1
    
    # ... [保持原有的结尾处理逻辑不变] ...
    
    return segments
```

- [ ] **Step 3: 运行测试验证**

Run: 选择 3 个超长文档（>5000 字符）运行翻译
Expected: 翻译后检测连续 >50 个英文字符的段落数为 0

- [ ] **Step 4: Commit**

```bash
git add scripts/translate.py
git commit -m "feat(translate): add long paragraph splitting by sentence boundary"
```

---

### Task 4: 重写 `_is_translatable_paragraph()` 函数

**Files:**
- Modify: `scripts/translate.py:381-427` (重写整个函数)

- [ ] **Step 1: 重写判断逻辑**

```python
def _is_translatable_paragraph(text: str) -> bool:
    """判断段落是否需要翻译"""
    # 去除空白
    text = text.strip()
    if not text:
        return False
    
    # 跳过纯符号/数字/链接
    if re.match(r'^[\s\*\-\d\.\/]*$', text):
        return False
    
    # 如果包含中文字符，即使 <60 字符也翻译
    if re.search(r'[\u4e00-\u9fff\u3040-\u30ff]', text):
        return True
    
    # 如果包含英文字符且长度 >10，翻译
    if re.search(r'[a-zA-Z]', text) and len(text) > 10:
        return True
    
    # 短引用（<60字符）但包含中英文字符，翻译
    if len(text) < 60:
        if re.search(r'[a-zA-Z]', text) and re.search(r'[\u4e00-\u9fff]', text):
            return True
        return False
    
    return True
```

- [ ] **Step 2: 更新 `translate_markdown_file()` 使用新函数**

修改第 331 行：
```python
# 原代码：
# if not text or text.startswith(">") and len(text) < 60:

# 改为：
if not _is_translatable_paragraph(text):
```

- [ ] **Step 3: 运行测试验证**

Run: 翻译包含短标题、列表项的文档
Expected: 所有包含中英文字符的行均被翻译（无跳过）

- [ ] **Step 4: Commit**

```bash
git add scripts/translate.py
git commit -m "fix(translate): improve translatable paragraph detection logic"
```

---

### Task 5: 添加翻译后自检函数

**Files:**
- Modify: `scripts/translate.py` (在 `translate()` 函数前添加)

- [ ] **Step 1: 添加 `_check_translation_quality()` 函数**

```python
def _check_translation_quality(original: str, translated: str) -> tuple[bool, list]:
    """检查翻译质量，返回 (是否通过, 问题列表)"""
    issues = []
    
    # 1. 检测大段未翻译（连续 >50 个英文字符）
    long_english = re.findall(r'[a-zA-Z][a-zA-Z\s,\.!?;:]{49,}', translated)
    if long_english:
        issues.append(f"未翻译段落: {len(long_english)} 处")
    
    # 2. 检测术语嵌套（如 ROCm（ROCm（...）））
    nested_terms = re.findall(r'(\w+（\1（)', translated)
    if nested_terms:
        issues.append(f"术语嵌套: {nested_terms}")
    
    # 3. 检测术语占位符是否都替换了
    remaining_placeholders = re.findall(r'__TERM_\d+__', translated)
    if remaining_placeholders:
        issues.append(f"未替换占位符: {len(remaining_placeholders)} 个")
    
    return len(issues) == 0, issues
```

- [ ] **Step 2: 在 `translate()` 函数中调用自检**

见 Task 2 Step 1 已包含自检调用

- [ ] **Step 3: 运行测试验证**

Run: 人为构造未翻译段落（>50 个英文字符），运行翻译
Expected: 检测到未翻译，返回 is_ok=False，issues 非空

- [ ] **Step 4: Commit**

```bash
git add scripts/translate.py
git commit -m "feat(translate): add post-translation self-check for quality"
```

---

### Task 6: 添加 API 调用重试封装

**Files:**
- Modify: `scripts/translate.py` (在现有 `translate_deepseek()` 等函数后添加)

- [ ] **Step 1: 添加 `_call_translation_api()` 封装函数**

```python
import time

def _call_translation_api(text: str, mode: str = "doc", max_retries: int = 3) -> Optional[str]:
    """封装翻译 API 调用，带重试逻辑"""
    for attempt in range(max_retries):
        try:
            provider = os.environ.get("TRANSLATE_PROVIDER", "deepseek")
            api_key = os.environ.get("TRANSLATE_API_KEY", "")
            model = os.environ.get("TRANSLATE_MODEL", "deepseek-v4-flash")
            base_url = os.environ.get("TRANSLATE_BASE_URL", "https://api.deepseek.com/v1")
            
            # 根据 provider 调用对应的翻译函数
            if provider in ("deepseek", "opencode"):
                result = translate_deepseek(text, api_key, model=model, base_url=base_url, mode=mode)
            elif provider == "openai":
                result = translate_openai(text, api_key, model=model)
            elif provider == "deepl":
                result = translate_deepl(text, api_key)
            else:
                print(f"  ⚠ Unknown provider: {provider}")
                return None
            
            if result and len(result) > 10:  # 基本有效性检查
                return result
            else:
                print(f"  ⚠ Attempt {attempt+1}: translation too short or empty")
        except Exception as e:
            print(f"  ⚠ Attempt {attempt+1} failed: {e}")
        
        if attempt < max_retries - 1:
            sleep_time = 2 ** attempt
            print(f"  ⏳ Retrying in {sleep_time}s...")
            time.sleep(sleep_time)
    
    return None  # 所有重试失败
```

- [ ] **Step 2: 移除现有 `translate()` 中的直接 API 调用**

修改 `translate()` 函数（Task 2 已包含此修改）

- [ ] **Step 3: 移除 `verify.py` 中的无条件 `time.sleep(2)`**

修改 `scripts/verify.py` 第 563 行：
```python
# 原代码：
# time.sleep(2)  # LLM rate limit

# 改为：仅在 API 调用后按需延迟
# 在 verify_article() 中，如果调用了 LLM，则 sleep
if api_was_called:
    time.sleep(2)  # LLM rate limit
```

- [ ] **Step 4: 运行测试验证**

Run: 模拟 API 失败（临时改 endpoint），运行翻译
Expected: 在 3 次重试后失败，或成功重试

- [ ] **Step 5: Commit**

```bash
git add scripts/translate.py scripts/verify.py
git commit -m "feat(translate): add API retry logic and remove unconditional sleep"
```

---

### Task 7: 更新 `translate_markdown_file()` 使用新逻辑

**Files:**
- Modify: `scripts/translate.py:295-378` (更新翻译段落处理)

- [ ] **Step 1: 更新翻译段落处理逻辑**

修改 `translate_markdown_file()` 中的翻译段落处理（第 326-345 行）：
```python
for seg in segments:
    if seg["type"] in ("frontmatter", "code"):
        translated_parts.append(seg["content"])
    elif seg["type"] == "paragraph":
        text = seg["content"].strip()
        if not _is_translatable_paragraph(text):
            translated_parts.append(seg["content"])
            continue
        
        if dry_run:
            translated_parts.append(f"[ZH-TRANSLATED] {text[:80]}...")
        else:
            translated, is_ok, issues = translate(text, glossary, mode=mode)
            if translated:
                translated_parts.append(translated)
                if not is_ok:
                    print(f"  ⚠ Quality issues: {issues}")
                    # 重试一次
                    translated, is_ok, issues = translate(text, glossary, mode=mode)
                    if translated:
                        translated_parts.append(translated)
            else:
                failed_count += 1
    else:
        translated_parts.append(seg["content"])
```

- [ ] **Step 2: 运行集成测试**

Run: `python3 scripts/translate.py --incremental --max-files 5`
Expected: 5 个文件翻译成功，无术语嵌套，无未翻译段落

- [ ] **Step 3: Commit**

```bash
git add scripts/translate.py
git commit -m "feat(translate): integrate new translation pipeline in markdown processor"
```

---

### Task 8: 编写单元测试

**Files:**
- Create: `tests/test_translate.py`

- [ ] **Step 1: 编写测试用例**

```python
import pytest
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.translate import (
    _mark_terms_with_placeholders,
    _replace_placeholders,
    _split_long_paragraph,
    _is_translatable_paragraph,
    _check_translation_quality,
)

def test_mark_terms_with_placeholders():
    glossary = {
        "terms": [
            {"en": "ROCm", "zh": "ROCm（开放计算平台）", "keep_original": False},
        ],
        "mapping": {"ROCm": {"zh": "ROCm（开放计算平台）", "keep_original": False}}
    }
    text = "ROCm is a platform. It provides HIP."
    marked, placeholders = _mark_terms_with_placeholders(text, glossary)
    assert "__TERM_0__" in marked
    assert "ROCm" not in marked.replace("__TERM_0__", "")

def test_replace_placeholders():
    placeholders = {"__TERM_0__": "ROCm（开放计算平台）"}
    translated = "__TERM_0__ 是一个平台。"
    result = _replace_placeholders(translated, placeholders)
    assert "ROCm（开放计算平台）" in result
    assert "__TERM_0__" not in result

def test_split_long_paragraph():
    long_text = "First sentence. " * 100  # >3000 chars
    chunks = _split_long_paragraph(long_text)
    assert len(chunks) > 1
    for chunk in chunks:
        assert len(chunk) <= 3000

def test_is_translatable_paragraph():
    assert _is_translatable_paragraph("Hello world") == True
    assert _is_translatable_paragraph("ROCm 是平台") == True  # 中英混合
    assert _is_translatable_paragraph("> short quote") == False
    assert _is_translatable_paragraph("https://example.com") == False

def test_check_translation_quality():
    original = "This is a test."
    translated_good = "这是一个测试。"
    translated_bad = "This is a test. 这是一个测试。"  # 未翻译部分
    translated_nested = "ROCm（ROCm（开放计算平台））是一个平台。"
    
    is_ok, issues = _check_translation_quality(original, translated_good)
    assert is_ok == True
    
    is_ok, issues = _check_translation_quality(original, translated_bad)
    assert is_ok == False
    assert len(issues) > 0
    
    is_ok, issues = _check_translation_quality(original, translated_nested)
    assert is_ok == False
```

- [ ] **Step 2: 运行测试**

Run: `pytest tests/test_translate.py -v`
Expected: 所有测试 PASS

- [ ] **Step 3: Commit**

```bash
git add tests/test_translate.py
git commit -m "test(translate): add unit tests for new translation functions"
```

---

### Task 9: 集成测试与验收

**Files:**
- Modify: None (使用现有文档测试)

- [ ] **Step 1: 测试术语不再嵌套**

Run: `python3 scripts/translate.py --file content/raw/english/rocm-docs-latest_en_latest_conceptual_rocm-overview_zh.md`
Check: 翻译后文件中无 `ROCm（ROCm（...））` 嵌套

- [ ] **Step 2: 测试长段落无未翻译**

Run: 选择 3 个超长文档（>5000 字符）翻译
Check: `grep -E '[a-zA-Z]{50,}' <translated_file>` 返回空（无未翻译长段落）

- [ ] **Step 3: 测试短行正确翻译**

Run: 翻译包含短标题、列表项的文档
Check: 所有包含中英文字符的行均被翻译（无跳过）

- [ ] **Step 4: 测试 API 调用不 sleep（无 API 调用时）**

Run: `time python3 scripts/translate.py --file <file_without_translation_needed>` 
Check: 总耗时 < 20 秒（无 API 调用时不 sleep）

- [ ] **Step 5: 最终验证**

Run: `python3 scripts/translate.py --incremental --max-files 5`
Check: 5 个文件翻译成功，所有验收标准通过

- [ ] **Step 6: Commit (如有修复)**

```bash
git add scripts/translate.py
git commit -m "fix(translate): final adjustments after integration testing"
```

---

## 验收标准检查表

| 验收项 | 测试方法 | 通过标准 | 状态 |
|--------|---------|---------|------|
| 术语不再嵌套 | 翻译 `ROCm` 相关文档，检查输出 | 无 `ROCm（ROCm（...））` 嵌套，术语格式统一为 `ROCm（开放计算平台）` | [ ] |
| 长段落无未翻译 | 选择 3 个超长文档（>5000 字符）翻译 | 翻译后检测：连续 >50 个英文字符的段落数为 0 | [ ] |
| 短行正确翻译 | 翻译包含短标题、列表项的文档 | 所有包含中英文字符的行均被翻译（无跳过） | [ ] |
| API 调用不 sleep（无 API 调用时） | 翻译 10 篇无翻译文件的文章（只检查是否需要翻译） | 总耗时 < 20 秒（无 API 调用时不 sleep） | [ ] |
| 翻译后自检生效 | 人为构造未翻译段落（>50 英文字符），运行翻译 | 检测到未翻译，重试或标记 `needs_review` | [ ] |
| 重试逻辑生效 | 模拟 API 失败（临时改 endpoint），运行翻译 | 在 3 次重试后失败，或成功重试 | [ ] |

---

**Plan complete and saved to `docs/superpowers/plans/2026-05-04-translation-quality-phase1a.md`.**

Which execution approach?
1. **Subagent-Driven (recommended)** - I dispatch a fresh subagent per task, review between tasks, fast iteration
2. **Inline Execution** - Execute tasks in this session using executing-plans, batch execution with checkpoints
