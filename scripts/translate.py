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
import yaml
from pathlib import Path
from typing import Optional

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONTENT_RAW_EN = (PROJECT_ROOT / "content" / "raw" / "english").resolve()
CONTENT_RAW_PAPERS = (PROJECT_ROOT / "content" / "raw" / "papers").resolve()
CONTENT_TRANSLATED_ZH = (PROJECT_ROOT / "content" / "translated" / "zh").resolve()
GLOSSARY_PATH = (PROJECT_ROOT / "glossary" / "rocm-terms.yaml").resolve()
DOCS_BILINGUAL = (PROJECT_ROOT / "docs" / "bilingual" / "en-zh").resolve()

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
                           mode: str = "doc") -> bool:
    """翻译单个 Markdown 文件。

    mode: "doc" = 技术文档, "paper" = 学术论文
    """
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
            return True

    # 跳过超大文件（>500KB）—— 内容太多，翻译耗时数小时
    MAX_SIZE = 500 * 1024
    if filepath.stat().st_size > MAX_SIZE:
        print(f"  ⏭ Skipped (too large: {filepath.stat().st_size // 1024}KB): {filepath.name}")
        return True
    with open(filepath) as f:
        content = f.read()

    segments = split_markdown(content)

    translated_parts = []
    failed_count = 0  # 跟踪翻译失败次数
    for seg in segments:
        if seg["type"] in ("frontmatter", "code"):
            translated_parts.append(seg["content"])
        elif seg["type"] == "paragraph":
            text = seg["content"].strip()
            if not text or text.startswith(">") and len(text) < 60:
                # 短引用不翻译
                translated_parts.append(seg["content"])
                continue
            if dry_run:
                translated_parts.append(f"[ZH-TRANSLATED] {text[:80]}...")
            else:
                translated = translate(text, glossary, mode=mode)
                if translated:
                    translated_parts.append(translated)
                else:
                    failed_count += 1
                    # 翻译失败不写入原文，保持空白让 is_valid_translation 检测出问题
        else:
            translated_parts.append(seg["content"])

    result = "\n\n".join(translated_parts)

    # 如果有段落翻译失败，不写入文件（下次会重试）
    if failed_count > 0:
        print(f"  ⚠ Failed segments: {failed_count}, keeping checkpoint for retry")

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

    return True


def is_valid_translation(path: Path) -> bool:
    """检查翻译文件是否有效（含有中文）。

    规则：
    1. 文件存在
    2. 大于 200 bytes
    3. 含中文字符
    4. 中文占比 > 3%
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

    # 检查是否含中文
    chinese_chars = len(re.findall(r"[\u4e00-\u9fff]", content))
    if chinese_chars == 0:
        return False

    # 检查中文占比
    total_chars = len(re.sub(r"\s", "", content))
    if total_chars > 0 and (chinese_chars / total_chars) < 0.03:
        return False

    return True


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
    args = parser.parse_args()

    print("🌐 rocm-hip-map translate.py")
    print(f"   Provider: {os.environ.get('TRANSLATE_PROVIDER', 'not set')}")
    print(f"   Mode: {args.mode}")
    print(f"   {'DRY RUN' if args.dry_run else 'LIVE MODE'}")
    print(f"   {'INCREMENTAL' if args.incremental else 'FULL'}")

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
            translate_markdown_file(md_file, glossary, dry_run=args.dry_run, mode="paper")
            count += 1
        print(f"\n📊 {count} papers translated")
    elif args.file:
        path = Path(args.file)
        if not path.is_absolute():
            path = (PROJECT_ROOT / path).resolve()

        if not path.exists():
            print(f"   ❌ Input file not found: {path}")
            sys.exit(1)

        ok = translate_markdown_file(path, glossary, dry_run=args.dry_run, mode=args.mode)
        if not ok:
            sys.exit(1)

        print(f"   ✅ Translated: {path.name}")
    elif args.incremental:
        # 增量模式：只翻译未完成/失败的文件
        # 断点续传逻辑：_zh.md 存在且 > MIN_VALID_SIZE 则跳过
        MIN_VALID_SIZE = 200  # bytes — 低于此值视为失败断点，重新翻译

        if not CONTENT_RAW_EN.exists():
            print("   No raw English content found. Run fetch-official.py first.")
            return

        all_files = sorted(CONTENT_RAW_EN.glob("*.md"))
        skipped = 0
        failed_resume = 0
        count = 0

        for md_file in all_files:
            zh_file = CONTENT_TRANSLATED_ZH / (md_file.stem + "_zh.md")

            # 使用 is_valid_translation 判断是否真正完成
            if is_valid_translation(zh_file):
                skipped += 1
                continue  # ✅ 已完成，跳过

            if zh_file.exists():
                # 存在但无效，视为失败断点
                print(f"  🔄 Resume (invalid translation, {zh_file.stat().st_size}B): {md_file.name}")
                failed_resume += 1
            else:
                print(f"  📝 {md_file.name}")

            translate_markdown_file(md_file, glossary, dry_run=args.dry_run, mode=args.mode)
            count += 1

            if args.max_files > 0 and count >= args.max_files:
                remaining = len(all_files) - skipped - failed_resume - count
                print(f"\n  ⏸ Reached --max-files={args.max_files}")
                if remaining > 0:
                    print(f"     {remaining} file(s) remain for next run")
                break

        print(f"\n📊 Success: {count}, Failed: {failed_resume}, Skipped(valid): {skipped}, "
              f"Remaining: {len(all_files) - skipped - failed_resume - count}")
    else:
        if not CONTENT_RAW_EN.exists():
            print("   No raw English content found. Run fetch-official.py first.")
            return
        count = 0
        for md_file in sorted(CONTENT_RAW_EN.glob("*.md")):
            print(f"  📝 {md_file.name}")
            translate_markdown_file(md_file, glossary, dry_run=args.dry_run, mode=args.mode)
            count += 1
        print(f"\n📊 {count} files translated")


if __name__ == "__main__":
    main()
