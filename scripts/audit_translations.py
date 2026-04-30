#!/usr/bin/env python3
"""audit_translations.py — 翻译诊断脚本。

扫描 content/translated/zh/ 目录，输出诊断报告：
1. 无中文文件
2. 小于200B文件
3. 疑似未翻译段落（per-paragraph 检测）
4. 总数统计
"""
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
TRANSLATED_ZH = (PROJECT_ROOT / "content" / "translated" / "zh").resolve()

# 必须与 translate.py 保持同步
TRANSLATION_INCOMPLETE_MARKER = "<!-- TRANSLATION_INCOMPLETE -->"


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
                untranslated.append({"line_num": i, "text": line[:100]})  # Truncate for display
    
    return untranslated


def is_valid_translation(path: Path) -> dict:
    """检查翻译文件是否有效（per-paragraph 检测）。
    
    返回: {"valid": bool, "stats": dict, "untranslated": list}
    - valid: 是否有足够的翻译（>70% body paragraphs have Chinese）
    - stats: 统计信息
    - untranslated: 未翻译段落列表
    """
    if not path.exists():
        return {"valid": False, "stats": {}, "untranslated": []}

    size = path.stat().st_size
    if size <= 200:
        return {"valid": False, "stats": {"size": size}, "untranslated": []}

    try:
        content = path.read_text(encoding="utf-8")
    except Exception:
        return {"valid": False, "stats": {}, "untranslated": []}

    # INCOMPLETE 标记检测 — 必须优先判断（与 translate.py 保持同步）
    if TRANSLATION_INCOMPLETE_MARKER in content:
        return {"valid": False, "stats": {"incomplete_marker": True}, "untranslated": []}

    # 检查全局是否有中文
    chinese_chars = len(re.findall(r"[\u4e00-\u9fff]", content))
    if chinese_chars == 0:
        return {"valid": False, "stats": {"chinese_chars": 0, "total_lines": len(content.split("\n"))}, "untranslated": []}

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

    stats = {
        "chinese_chars": chinese_chars,
        "total_lines": len(lines),
        "translatable_paragraphs": translatable_count,
        "untranslated_paragraphs": untranslated_count,
        "translated_ratio": translated_ratio,
    }
    
    # >30% untranslated = invalid
    is_valid = translated_ratio >= 0.70
    
    return {
        "valid": is_valid,
        "stats": stats,
        "untranslated": untranslated,
    }


def main():
    if not TRANSLATED_ZH.exists():
        print("❌ No translated directory found")
        return

    files = list(TRANSLATED_ZH.glob("**/*.md"))
    total = len(files)

    print("=" * 50)
    print("🔍 Translation Audit Report")
    print("=" * 50)

    # 分类统计
    invalid_files = []  # 整体无效
    files_with_untranslated = []  # 有未翻译段落

    for f in files:
        result = is_valid_translation(f)
        if not result["valid"]:
            invalid_files.append((f, result))
        if result["untranslated"]:
            files_with_untranslated.append((f, result))

    print(f"\n📊 Total files: {total}")
    print(f"✅ Valid translations: {total - len(invalid_files)}")
    print(f"❌ Invalid translations: {len(invalid_files)}")

    if files_with_untranslated:
        print(f"\n⚠️  Files with untranslated paragraphs ({len(files_with_untranslated)}):")
        # Show top 3 worst files
        files_with_untranslated.sort(
            key=lambda x: x[1]["stats"].get("translated_ratio", 1.0)
        )
        for f, result in files_with_untranslated[:3]:
            ratio = result["stats"].get("translated_ratio", 0) * 100
            untrans = result["stats"].get("untranslated_paragraphs", 0)
            print(f"\n   📄 {f.name}")
            print(f"      翻译率: {ratio:.0f}% | 未翻译段落: {untrans}")
            # Show first 5 untranslated paragraphs
            for para in result["untranslated"][:5]:
                text = para["text"][:60] + "..." if len(para["text"]) > 60 else para["text"]
                print(f"      L{para['line_num']}: {text}")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()