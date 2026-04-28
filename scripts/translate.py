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
CONTENT_RAW_EN = PROJECT_ROOT / "content" / "raw" / "english"
CONTENT_TRANSLATED_ZH = PROJECT_ROOT / "content" / "translated" / "zh"
GLOSSARY_PATH = PROJECT_ROOT / "glossary" / "rocm-terms.yaml"
DOCS_BILINGUAL = PROJECT_ROOT / "docs" / "bilingual" / "en-zh"

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
                      base_url: str = "https://api.deepseek.com/v1") -> Optional[str]:
    """DeepSeek / OpenAI-compatible 翻译（支持自定义 base_url）。"""
    try:
        payload = json.dumps({
            "model": model,
            "messages": [
                {"role": "system", "content": (
                    "You are a technical translator specialized in GPU/ROCm/HIP documentation. "
                    "Translate the following English text to Simplified Chinese (zh-CN). "
                    "Rules:\n"
                    "1. Preserve ALL markdown formatting, code blocks, inline code, and links unchanged.\n"
                    "2. Keep technical terms like ROCm, HIP, GPU, CUDA, AMD, PyTorch, TensorFlow in their original English form.\n"
                    "3. Keep API names, function names, file paths, commands unchanged.\n"
                    "4. Output ONLY the translation — no explanations, no notes, no preamble.\n"
                    "5. Use technical Chinese that a GPU developer would expect."
                )},
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


def translate(text: str, glossary: dict) -> Optional[str]:
    """统一翻译入口，自动选择后端。

    环境变量：
      TRANSLATE_PROVIDER   deepseek | openai | opencode | deepl
      TRANSLATE_API_KEY    API 密钥
      TRANSLATE_MODEL      模型名（deepseek 默认 deepseek-chat，
                           opencode 默认 deepseek-v4-pro）
      TRANSLATE_BASE_URL   自定义端点（opencode 需要设置为
                           https://opencode.ai/zen/go/v1）
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
        return translate_deepseek(text, api_key, model=model, base_url=base_url)
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


def translate_markdown_file(filepath: Path, glossary: dict, dry_run: bool = False) -> bool:
    """翻译单个 Markdown 文件。"""
    with open(filepath) as f:
        content = f.read()

    segments = split_markdown(content)

    translated_parts = []
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
                translated = translate(text, glossary)
                if translated:
                    translated_parts.append(translated)
                else:
                    translated_parts.append(seg["content"])
        else:
            translated_parts.append(seg["content"])

    result = "\n\n".join(translated_parts)

    # 保存翻译结果
    rel_path = filepath.relative_to(CONTENT_RAW_EN) if CONTENT_RAW_EN in filepath.parents else filepath
    out_path = CONTENT_TRANSLATED_ZH / rel_path.with_name(rel_path.stem + "_zh.md")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if not dry_run:
        with open(out_path, "w") as f:
            f.write(result)

    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="Single file to translate")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    print("🌐 rocm-hip-map translate.py")
    print(f"   Provider: {os.environ.get('TRANSLATE_PROVIDER', 'not set')}")
    print(f"   {'DRY RUN' if args.dry_run else 'LIVE MODE'}")

    glossary = load_glossary()
    print(f"   Glossary: {len(glossary.get('terms',[]))} terms")

    if args.file:
        path = Path(args.file)
        translate_markdown_file(path, glossary, dry_run=args.dry_run)
        print(f"   ✅ Translated: {path.name}")
    else:
        if not CONTENT_RAW_EN.exists():
            print("   No raw English content found. Run fetch-official.py first.")
            return
        count = 0
        for md_file in sorted(CONTENT_RAW_EN.glob("*.md")):
            print(f"  📝 {md_file.name}")
            translate_markdown_file(md_file, glossary, dry_run=args.dry_run)
            count += 1
        print(f"\n📊 {count} files translated")


if __name__ == "__main__":
    main()
