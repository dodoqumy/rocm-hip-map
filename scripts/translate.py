#!/usr/bin/env python3
"""translate.py — AI 翻译管道。

将英文 ROCm 文档翻译为中文，保持术语一致性。

特性：
  - 术语表保证专业术语翻译一致
  - 段落级翻译（保留代码块和链接）
  - 多后端支持（通过 TRANSLATE_PROVIDER 环境变量切换）

配置（环境变量）：
  TRANSLATE_PROVIDER  deepseek | opencode | openai | deepl
  TRANSLATE_API_KEY   API 密钥
  TRANSLATE_MODEL     模型名（可选，deepseek 默认 deepseek-chat，
                      opencode 默认 deepseek-v4-pro）
  TRANSLATE_BASE_URL  自定义 API 端点（可选，opencode 需设置
                      为 https://opencode.ai/zen/go/v1）

用法：
  python3 scripts/translate.py                     # 翻译所有
  python3 scripts/translate.py --file <path>        # 单文件
  python3 scripts/translate.py --dry-run            # 预览
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time
import yaml
from pathlib import Path
from typing import Optional

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONTENT_RAW_EN = (PROJECT_ROOT / "content" / "raw" / "english").resolve()
CONTENT_RAW_PAPERS = (PROJECT_ROOT / "content" / "raw" / "papers").resolve()
CONTENT_TRANSLATED_ZH = (PROJECT_ROOT / "content" / "translated" / "zh").resolve()
GLOSSARY_PATH = (PROJECT_ROOT / "glossary" / "rocm-terms.yaml").resolve()
DOCS_BILINGUAL = (PROJECT_ROOT / "docs" / "bilingual" / "en-zh").resolve()

# 翻译不完整标记 — 段落级失败时写入，下次会被 is_valid_translation 检测为无效并重试
TRANSLATION_INCOMPLETE_MARKER = "<!-- TRANSLATION_INCOMPLETE -->"

# ── 术语表 ──────────────────────────────────────────

def load_glossary() -> dict:
    """加载术语表，构建 en→zh 映射。"""
    if not GLOSSARY_PATH.exists():
        return {"terms": [], "mapping": {}}
    with open(GLOSSARY_PATH) as f:
        data = yaml.safe_load(f)
    mapping = {}
    for term in data.get("terms", []):
        en = term["en"]
        mapping[en] = {
            "zh": term["zh"],
            "keep_original": term.get("keep_original", False),
        }
    return {"terms": data.get("terms", []), "mapping": mapping}


def apply_glossary(text: str, glossary: dict) -> str:
    """在文本中应用术语表替换，保持术语一致。

    策略：对于 keep_original=True 的术语，
    保留英文 + 添加中文注释。
    """
    mapping = glossary.get("mapping", {})
    for en_term, info in sorted(mapping.items(), key=lambda x: -len(x[0])):
        zh = info["zh"]
        if info.get("keep_original"):
            replacement = f"{en_term}（{zh}）"
        else:
            replacement = zh
        # 单词边界替换
        text = re.sub(r'\b' + re.escape(en_term) + r'\b', replacement, text)
    return text


# ── 翻译后端 ──────────────────────────────────────────

def translate_deepl(text: str, api_key: str) -> Optional[str]:
    """DeepL 翻译。"""
    try:
        result = subprocess.run(
            ["curl", "-s", "--max-time", "30",
             "-X", "POST", "https://api-free.deepl.com/v2/translate",
             "-H", f"Authorization: DeepL-Auth-Key {api_key}",
             "-d", f"text={text}",
             "-d", "target_lang=ZH"],
            capture_output=True, text=True, timeout=35,
        )
        data = json.loads(result.stdout)
        return data.get("translations", [{}])[0].get("text")
    except Exception as e:
        print(f"  ⚠ DeepL: {e}")
        return None


def translate_openai(text: str, api_key: str, model: str = "gpt-4o-mini") -> Optional[str]:
    """OpenAI GPT 翻译。"""
    try:
        payload = json.dumps({
            "model": model,
            "messages": [
                {"role": "system", "content": "You are a technical translator. Translate the following English text to Simplified Chinese. Preserve code blocks, markdown links, and technical terms in their original form. Output ONLY the translation, no explanation."},
                {"role": "user", "content": text},
            ],
            "temperature": 0.1,
            "max_tokens": 4096,
        })
        result = subprocess.run(
            ["curl", "-s", "--max-time", "60",
             "https://api.openai.com/v1/chat/completions",
             "-H", f"Authorization: Bearer {api_key}",
             "-H", "Content-Type: application/json",
             "-d", payload],
            capture_output=True, text=True, timeout=65,
        )
        data = json.loads(result.stdout)
        return data.get("choices", [{}])[0].get("message", {}).get("content")
    except Exception as e:
        print(f"  ⚠ OpenAI: {e}")
        return None


def translate_deepseek(text: str, api_key: str, model: str = "deepseek-chat",
                      base_url: str = "https://api.deepseek.com/v1",
                      mode: str = "doc") -> Optional[str]:
    """DeepSeek / OpenAI-compatible 翻译（支持自定义 base_url）。

    mode: "doc" = 技术文档翻译, "paper" = 学术论文翻译
    """
    try:
        # 选择系统提示
        if mode == "paper":
            system_prompt = (
                "You are a technical translator specialized in academic papers "
                "on GPU computing, deep learning, and parallel computing. "
                "Translate the following English academic text to Simplified Chinese (zh-CN). "
                "Rules:\n"
                "1. Preserve ALL mathematical notation, equations, variables unchanged.\n"
                "2. Keep ALL citations like [42], [1,2,3] in their original form.\n"
                "3. Keep ALL figure/table references like 'Figure 1', 'Table 2' unchanged.\n"
                "4. Keep technical terms like ROCm, HIP, GPU, CUDA, AMD, PyTorch, CUDA unchanged.\n"
                "5. Keep ALL markdown formatting, code blocks, inline code, and links unchanged.\n"
                "6. For section headings, translate naturally but keep the numbering.\n"
                "7. Translate academic prose into formal technical Chinese.\n"
                "8. Output ONLY the translation — no explanations, no notes, no preamble."
            )
        else:
            system_prompt = (
                "You are a technical translator specialized in GPU/ROCm/HIP documentation. "
                "Translate the following English text to Simplified Chinese (zh-CN). "
                "Rules:\n"
                "1. Preserve ALL markdown formatting, code blocks, inline code, and links unchanged.\n"
                "2. Keep technical terms like ROCm, HIP, GPU, CUDA, AMD, PyTorch, TensorFlow in their original English form.\n"
                "3. Keep API names, function names, file paths, commands unchanged.\n"
                "4. Output ONLY the translation — no explanations, no notes, no preamble.\n"
                "5. Use technical Chinese that a GPU developer would expect."
            )
        payload = json.dumps({
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text},
            ],
            "temperature": 0.1,
            "max_tokens": 4096,
        })
        result = subprocess.run(
            ["curl", "-s", "--max-time", "60",
             f"{base_url}/chat/completions",
             "-H", f"Authorization: Bearer {api_key}",
             "-H", "Content-Type: application/json",
             "-d", payload],
            capture_output=True, text=True, timeout=65,
        )
        data = json.loads(result.stdout)
        content = data.get("choices", [{}])[0].get("message", {}).get("content")
        if not content and "error" in data:
            print(f"  ⚠ DeepSeek API error: {data['error']}")
        return content
    except Exception as e:
        print(f"  ⚠ DeepSeek: {e}")
        return None


def translate(text: str, glossary: dict, mode: str = "doc") -> Optional[str]:
    """统一翻译入口，自动选择后端。

    环境变量：
      TRANSLATE_PROVIDER   deepseek | openai | opencode | deepl
      TRANSLATE_API_KEY    API 密钥
      TRANSLATE_MODEL      模型名（deepseek 默认 deepseek-chat，
                           opencode 默认 deepseek-v4-pro）
      TRANSLATE_BASE_URL   自定义端点（opencode 需要设置为
                           https://opencode.ai/zen/go/v1）

    mode: "doc" = 技术文档, "paper" = 学术论文
    """
    provider = os.environ.get("TRANSLATE_PROVIDER", "deepseek")
    api_key = os.environ.get("TRANSLATE_API_KEY", "")

    if not api_key:
        print("  ⚠ No TRANSLATE_API_KEY set — skipping translation")
        return None

    # 先应用术语表
    text = apply_glossary(text, glossary)

    if provider == "deepl":
        return translate_deepl(text, api_key)
    elif provider == "openai":
        model = os.environ.get("TRANSLATE_MODEL", "gpt-4o-mini")
        return translate_openai(text, api_key, model)
    elif provider in ("deepseek", "opencode"):
        model = os.environ.get("TRANSLATE_MODEL",
            "deepseek-chat" if provider == "deepseek" else "deepseek-v4-pro")
        base_url = os.environ.get("TRANSLATE_BASE_URL",
            "https://api.deepseek.com/v1" if provider == "deepseek"
            else "https://opencode.ai/zen/go/v1")
        return translate_deepseek(text, api_key, model=model, base_url=base_url, mode=mode)
    else:
        print(f"  ⚠ Unknown provider: {provider}")
        return None


# ── Markdown 处理 ────────────────────────────────────

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

        if i == 0 and line.strip() == "---":
            # Frontmatter
            buffer = [line]
            i += 1
            while i < len(lines):
                buffer.append(lines[i])
                if lines[i].strip() == "---":
                    segments.append({"type": "frontmatter", "content": "\n".join(buffer)})
                    buffer = []
                    i += 1
                    break
                i += 1
            continue

        if line.strip().startswith("```"):
            if buffer:
                segments.append({"type": "paragraph", "content": "\n".join(buffer)})
                buffer = []
            if in_code:
                buffer.append(line)
                segments.append({"type": "code", "content": "\n".join(buffer)})
                buffer = []
                in_code = False
            else:
                buffer = [line]
                in_code = True
            i += 1
            continue

        if in_code:
            buffer.append(line)
            i += 1
            continue

        if line.strip() == "" and buffer:
            if any(l.strip() for l in buffer):
                segments.append({"type": "paragraph", "content": "\n".join(buffer)})
            buffer = []
        elif line.strip():
            buffer.append(line)

        i += 1

    if buffer and any(l.strip() for l in buffer):
        if in_code:
            segments.append({"type": "code", "content": "\n".join(buffer)})
        else:
            segments.append({"type": "paragraph", "content": "\n".join(buffer)})

    return segments


def translate_markdown_file(filepath: Path, glossary: dict, dry_run: bool = False,
                           mode: str = "doc", verbose: bool = False) -> dict:
    """翻译单个 Markdown 文件。

    mode: "doc" = 技术文档, "paper" = 学术论文
    verbose: True = 打印每段翻译进度

    Returns: dict with keys:
        success (bool): 函数正常执行
        skipped (bool): 文件被跳过
        skip_reason (str): 跳过原因
        failed_count (int): 翻译失败的段落数
        total_paragraphs (int): 可翻译段落总数
        out_path (Path): 输出文件路径，跳过时为 None
    """
    ret = {
        "success": True,
        "skipped": False,
        "skip_reason": "",
        "failed_count": 0,
        "total_paragraphs": 0,
        "out_path": None,
    }
    # 跳过不适合翻译的文件
    SKIP_PATTERNS = [
        "changelog",       # 版本日志，纯列表无翻译价值
        "versions",        # 版本号列表
        "release-notes",   # 发布说明
        "compatibility-matrix",  # 兼容性矩阵（表格为主）
    ]
    fname_lower = filepath.name.lower()
    for pat in SKIP_PATTERNS:
        if pat in fname_lower:
            print(f"  ⏭ Skipped (SKIP_PATTERNS: {pat}): {filepath.name}")
            ret["skipped"] = True
            ret["skip_reason"] = f"SKIP_PATTERNS: {pat}"
            return ret

    # 跳过超大文件（>500KB）—— 内容太多，翻译耗时数小时
    MAX_SIZE = 500 * 1024
    if filepath.stat().st_size > MAX_SIZE:
        print(f"  ⏭ Skipped (too large: {filepath.stat().st_size // 1024}KB): {filepath.name}")
        ret["skipped"] = True
        ret["skip_reason"] = f"too large: {filepath.stat().st_size // 1024}KB"
        return ret

    with open(filepath) as f:
        content = f.read()

    segments = split_markdown(content)

    # 先统计可翻译段落总数（用于进度显示）
    total_paras = 0
    for seg in segments:
        if seg["type"] == "paragraph":
            text = seg["content"].strip()
            if text and not (text.startswith(">") and len(text) < 60):
                total_paras += 1

    ret["total_paragraphs"] = total_paras
    if verbose and total_paras > 0:
        print(f"     📑 Translating {total_paras} paragraph(s)…")

    translated_parts = []
    failed_count = 0  # 跟踪翻译失败次数
    para_idx = 0
    for seg in segments:
        if seg["type"] in ("frontmatter", "code"):
            translated_parts.append(seg["content"])
        elif seg["type"] == "paragraph":
            text = seg["content"].strip()
            if not text or (text.startswith(">") and len(text) < 60):
                # 短引用不翻译
                translated_parts.append(seg["content"])
                continue
            para_idx += 1
            if verbose:
                char_len = len(text)
                pct = para_idx / total_paras * 100
                print(f"     📝 Paragraph {para_idx}/{total_paras} ({char_len:,} chars, {pct:.0f}%)")
            if dry_run:
                translated_parts.append(f"[ZH-TRANSLATED] {text[:80]}...")
                if verbose:
                    print(f"     ✅ [DRY RUN]")
            else:
                start = time.time()
                translated = translate(text, glossary, mode=mode)
                elapsed = time.time() - start
                if translated:
                    translated_parts.append(translated)
                    if verbose:
                        print(f"     ✅ Paragraph {para_idx}/{total_paras} ({elapsed:.1f}s, {char_len:,} → {len(translated):,} chars)")
                else:
                    failed_count += 1
                    if verbose:
                        print(f"     ⚠ Paragraph {para_idx}/{total_paras} FAILED")
                    # 翻译失败不写入原文，保持空白让 is_valid_translation 检测出问题
        else:
            translated_parts.append(seg["content"])

    result = "\n\n".join(translated_parts)

    # 如果有段落翻译失败，追加 INCOMPLETE 标记，下次 CI 会重新翻译
    if failed_count > 0:
        print(f"  ⚠ Failed segments: {failed_count}, marking INCOMPLETE")
        # 追加到 frontmatter 之后（如果存在），否则追加到文件开头
        marker_line = f"\n\n{TRANSLATION_INCOMPLETE_MARKER}\n"
        # 找到 frontmatter 结束位置
        fm_match = re.search(r'^---\s*\n.*?\n---\s*\n', result, re.DOTALL)
        if fm_match:
            result = result[:fm_match.end()] + marker_line + result[fm_match.end():]
        else:
            result = marker_line + result

    # 保存翻译结果
    rel_path = None
    if CONTENT_RAW_EN in filepath.parents:
        rel_path = filepath.relative_to(CONTENT_RAW_EN)
        out_path = CONTENT_TRANSLATED_ZH / rel_path.with_name(rel_path.stem + "_zh.md")
    elif CONTENT_RAW_PAPERS in filepath.parents:
        rel_path = filepath.relative_to(CONTENT_RAW_PAPERS)
        out_path = CONTENT_TRANSLATED_ZH / "papers" / rel_path.with_name(rel_path.stem + "_zh.md")
    else:
        rel_path = filepath
        out_path = CONTENT_TRANSLATED_ZH / rel_path.with_name(rel_path.stem + "_zh.md")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if not dry_run:
        with open(out_path, "w") as f:
            f.write(result)

    # 更新 ret
    ret["failed_count"] = failed_count
    ret["out_path"] = out_path
    if failed_count > 0:
        if verbose:
            print(f"     ⚠ {failed_count}/{total_paras} paragraphs failed — marked INCOMPLETE")
    elif verbose:
        print(f"     ✅ File done: {total_paras}/{total_paras} paragraphs translated")

    return ret


def is_translatable_paragraph(line: str) -> bool:
    """判断是否为可翻译段落（需要翻译的内容）。
    
    规则：
    - 长度 > 50 非空白字符
    - 不是 frontmatter 行 (---)
    - 不是代码/HTML行 (::: / {: .[! / [![] / !![ / data:image/)
    - 不是导航链接 (- [...][...])
    - 不是元数据行 (source_url: / tags: / title: 等)
    """
    # 去除空白后长度检查
    stripped = line.strip()
    non_whitespace = re.sub(r"\s", "", stripped)
    if len(non_whitespace) <= 50:
        return False
    
    # 排除 frontmatter
    if stripped.startswith("---"):
        return False
    
    # 排除代码/HTML标记行
    code_patterns = [
        r"^:::",           # 代码块开始
        r"^```",           # 代码块
        r"^{:",            # 属性列表
        r"^\.\[!",         # 提示块
        r"^\[!\[",         # 图片引用
        r"!!\[",           # 警告块
        r"^\[.*\]\(data:", # 图片 (...[](data:image/...)
        r"^- \[",          # 链接列表项
        r"^\* \[",         # 无序链接
        r"^\d+\.\s",       # 有序列表 (1. 2. )
    ]
    for pattern in code_patterns:
        if re.match(pattern, stripped):
            return False
    
    # 排除元数据行 (YAML frontmatter 或 markdown metadata)
    metadata_patterns = [
        r"^(source_|original_|article_)",  # 自定义元数据
        r"^(title|author|date|tags|category|description):\s",  # 标准元数据
    ]
    for pattern in metadata_patterns:
        if re.match(pattern, stripped):
            return False
    
    return True


def has_chinese(text: str) -> bool:
    """检查文本是否包含中文字符。"""
    return bool(re.search(r"[\u4e00-\u9fff]", text))


def find_untranslated_paragraphs(content: str) -> list[dict]:
    """找出所有未翻译的段落。
    
    返回: list of {"line_num": int, "text": str}
    """
    lines = content.split("\n")
    untranslated = []
    
    for i, line in enumerate(lines, 1):
        if is_translatable_paragraph(line):
            if not has_chinese(line):
                untranslated.append({"line_num": i, "text": line[:100]})
    
    return untranslated


def is_valid_translation(path: Path) -> bool:
    """检查翻译文件是否有效（per-paragraph 检测）。

    规则：
    1. 文件存在
    2. 大于 200 bytes
    3. 含有中文
    4. >70% body paragraphs have Chinese (>30% untranslated = invalid)
    5. 包含 INCOMPLETE 标记 → 无效（下次重试）
    """
    if not path.exists():
        return False

    size = path.stat().st_size
    if size <= 200:
        return False

    try:
        content = path.read_text(encoding="utf-8")
    except Exception:
        return False

    # INCOMPLETE 标记检测 — 必须优先判断
    if TRANSLATION_INCOMPLETE_MARKER in content:
        return False

    # 检查是否含中文
    chinese_chars = len(re.findall(r"[\u4e00-\u9fff]", content))
    if chinese_chars == 0:
        return False

    # Per-paragraph 检测
    untranslated = find_untranslated_paragraphs(content)
    lines = content.split("\n")
    
    # 统计可翻译段落数量
    translatable_count = sum(1 for line in lines if is_translatable_paragraph(line))
    untranslated_count = len(untranslated)
    
    # 计算翻译率
    if translatable_count > 0:
        translated_ratio = 1.0 - (untranslated_count / translatable_count)
    else:
        # 如果没有可翻译段落，检查整体中文比例
        total_chars = len(re.sub(r"\s", "", content))
        translated_ratio = chinese_chars / total_chars if total_chars > 0 else 0
    
    # >30% untranslated = invalid
    return translated_ratio >= 0.70


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="Single file to translate")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--mode", choices=["doc", "paper"], default="doc",
                       help="Translation mode: doc (default) or paper")
    parser.add_argument("--papers-dir", type=str, default="",
                       help="Translate all papers in content/raw/papers/")
    parser.add_argument("--incremental", action="store_true",
                       help="Incremental: only translate files without _zh.md or with failed output")
    parser.add_argument("--max-files", type=int, default=5,
                       help="Max files per run in incremental mode (0=unlimited, default: 5)")
    parser.add_argument("--commit-per-file", action="store_true",
                       help="Git add+commit+push each file after successful translation (CI use)")
    args = parser.parse_args()

    print("🌐 rocm-hip-map translate.py")
    print(f"   Provider: {os.environ.get('TRANSLATE_PROVIDER', 'not set')}")
    print(f"   Mode: {args.mode}")
    print(f"   {'DRY RUN' if args.dry_run else 'LIVE MODE'}")
    print(f"   {'INCREMENTAL' if args.incremental else 'FULL'}")
    if args.commit_per_file:
        print(f"   COMMIT-PER-FILE: yes")

    glossary = load_glossary()
    print(f"   Glossary: {len(glossary.get('terms',[]))} terms")

    if args.papers_dir:
        # 批量论文翻译模式
        papers_dir = Path(args.papers_dir)
        if not papers_dir.exists():
            print(f"   No papers found at {papers_dir}")
            return
        md_files = sorted(papers_dir.glob("*.md"))
        count = 0
        for md_file in md_files:
            print(f"  📜 {md_file.name}")
            translate_markdown_file(md_file, glossary, dry_run=args.dry_run, mode="paper",
                                     verbose=True)
            count += 1
        print(f"\n📊 {count} papers translated")
    elif args.file:
        path = Path(args.file)
        if not path.is_absolute():
            path = (PROJECT_ROOT / path).resolve()

        if not path.exists():
            print(f"   ❌ Input file not found: {path}")
            sys.exit(1)

        r = translate_markdown_file(path, glossary, dry_run=args.dry_run, mode=args.mode,
                                     verbose=True)
        if r.get("skipped", False):
            print(f"   ⏭ Skipped: {r['skip_reason']}")
        elif r.get("failed_count", 0) > 0:
            print(f"   ⚠ Translated with {r['failed_count']} failed paragraphs: {path.name}")
            if not args.dry_run:
                print(f"   💾 Saved to: {r['out_path']}")
            sys.exit(1)
        else:
            print(f"   ✅ Translated: {path.name}")
            if not args.dry_run and r.get("out_path"):
                print(f"   💾 Saved to: {r['out_path']}")
    elif args.incremental:
        # 增量模式：只翻译未完成/失败的文件
        # 断点续传逻辑：_zh.md 存在且 is_valid_translation 返回 True 则跳过
        MIN_VALID_SIZE = 200  # bytes — 低于此值视为失败断点，重新翻译

        if not CONTENT_RAW_EN.exists():
            print("   No raw English content found. Run fetch-official.py first.")
            return

        all_files = sorted(CONTENT_RAW_EN.glob("*.md"))
        skipped = 0
        failed_resume = 0
        count = 0
        max_files = args.max_files

        for md_file in all_files:
            zh_file = CONTENT_TRANSLATED_ZH / (md_file.stem + "_zh.md")

            # 使用 is_valid_translation 判断是否真正完成
            if is_valid_translation(zh_file):
                skipped += 1
                continue  # ✅ 已完成，跳过

            # ── 达到上限后不再处理更多文件 ──
            if max_files > 0 and count >= max_files:
                remaining = len(all_files) - skipped - failed_resume - count
                if count > 0:
                    print(f"  ⏸ Reached --max-files={max_files}")
                if remaining > 0:
                    print(f"     {remaining} file(s) remain for next run")
                break

            # ── 文件头日志（CI 可见的工作状态）──
            fsize = md_file.stat().st_size
            with open(md_file) as fh:
                raw = fh.read()
            fchars = len(raw)
            fwords = len(raw.split())

            print(f"\n{'═'*60}")
            print(f"  📄 [{count + 1}/{max_files or '∞'}] {md_file.name}")
            print(f"     📏 {fsize/1024:.1f} KB | {fchars:,} chars | {fwords:,} words")
            if zh_file.exists():
                print(f"     🔄 Resume (prev: {zh_file.stat().st_size}B)")
            print(f"{'─'*60}")

            r = translate_markdown_file(md_file, glossary, dry_run=args.dry_run,
                                         mode=args.mode, verbose=True)

            if r.get("skipped", False):
                # 文件被 translate_markdown_file 内部跳过（SKIP_PATTERNS/超大）
                # 不消耗 max-files 配额，不计入 count
                continue

            if zh_file.exists():
                failed_resume += 1

            # ── 提交（--commit-per-file）──
            # 只有完全成功的文件才 commit（无 failed_count）
            if args.commit_per_file and not args.dry_run and r.get("out_path") \
                    and r.get("failed_count", 0) == 0:
                zh_out = r["out_path"]
                committed = False
                if zh_out.exists():
                    g_add = subprocess.run(["git", "add", str(zh_out)],
                                           capture_output=True, text=True)
                    g_commit = subprocess.run(
                        ["git", "commit", "-m", f"translate: {md_file.name}"],
                        capture_output=True, text=True)
                    if g_commit.returncode == 0:
                        # rebase 前自动 stash 脏修改（续传 failed 文件留下的）
                        # 避免 "cannot pull with rebase: You have unstaged changes"
                        g_pull = subprocess.run(
                            ["git", "pull", "--rebase", "--autostash", "origin", "main"],
                            capture_output=True, text=True)
                        if g_pull.returncode != 0:
                            print(f"     ⚠ git pull --rebase failed: {g_pull.stderr.strip()[:120]}")
                            # rebase 冲突时 abort 并跳过 push
                            subprocess.run(["git", "rebase", "--abort"],
                                           capture_output=True)
                        else:
                            g_push = subprocess.run(["git", "push"],
                                                    capture_output=True, text=True)
                            if g_push.returncode == 0:
                                print(f"     ✅ Committed & pushed: translate: {md_file.name}")
                                committed = True
                            else:
                                print(f"     ⚠ git push failed: {g_push.stderr.strip()[:120]}")
                    elif "nothing to commit" in (g_commit.stdout + g_commit.stderr).lower():
                        print(f"     ℹ  Nothing to commit (no changes)")
                        committed = True  # not an error
                    else:
                        print(f"     ⚠ git commit error ({g_commit.returncode}): {g_commit.stderr.strip()[:120]}")
                if committed:
                    print(f"     💾 {zh_out.name}")

            count += 1

        print(f"\n📊 Success: {count}, Failed: {failed_resume}, Skipped(valid): {skipped}, "
              f"Remaining: {len(all_files) - skipped - failed_resume - count}")
    else:
        if not CONTENT_RAW_EN.exists():
            print("   No raw English content found. Run fetch-official.py first.")
            return
        count = 0
        for md_file in sorted(CONTENT_RAW_EN.glob("*.md")):
            print(f"  📝 {md_file.name}")
            r = translate_markdown_file(md_file, glossary, dry_run=args.dry_run,
                                         mode=args.mode, verbose=True)
            if not args.dry_run and r.get("out_path"):
                print(f"     💾 {r['out_path'].name}")
            count += 1
        print(f"\n📊 {count} files translated")


if __name__ == "__main__":
    main()
