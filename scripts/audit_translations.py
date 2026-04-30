#!/usr/bin/env python3
"""audit_translations.py — 翻译诊断脚本。

扫描 content/translated/zh/ 目录，输出诊断报告：
1. 无中文文件
2. 小于200B文件
3. 疑似英文伪翻译文件
4. 总数统计
"""
import re
from pathlib import Path

TRANSLATED_ZH = Path("content/translated/zh")


def is_valid_translation(path: Path) -> bool:
    """检查翻译文件是否有效（含有中文）。"""
    if not path.exists():
        return False

    size = path.stat().st_size
    if size <= 200:
        return False

    try:
        content = path.read_text(encoding="utf-8")
    except Exception:
        return False

    chinese_chars = len(re.findall(r"[\u4e00-\u9fff]", content))
    if chinese_chars == 0:
        return False

    total_chars = len(re.sub(r"\s", "", content))
    if total_chars > 0 and (chinese_chars / total_chars) < 0.03:
        return False

    return True


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
    no_chinese = []  # 无中文
    too_small = []  # 小于200B
    invalid = []  # 整体无效

    for f in files:
        if f.stat().st_size <= 200:
            too_small.append(f)
        elif not is_valid_translation(f):
            invalid.append(f)

    print(f"\n📊 Total files: {total}")
    print(f"✅ Valid translations: {total - len(invalid)}")
    print(f"❌ Invalid translations: {len(invalid)}")

    if no_chinese:
        print(f"\n⚠️  No Chinese detection ({len(no_chinese)}):")
        for f in no_chinese[:5]:
            print(f"   - {f.name}")
        if len(no_chinese) > 5:
            print(f"   ... and {len(no_chinese) - 5} more")

    if too_small:
        print(f"\n⚠️  Too small (<200B, {len(too_small)}):")
        for f in too_small[:5]:
            print(f"   - {f.name} ({f.stat().st_size}B)")
        if len(too_small) > 5:
            print(f"   ... and {len(too_small) - 5} more")

    if invalid:
        print(f"\n⚠️  Suspected fake translations ({len(invalid)}):")
        for f in invalid[:10]:
            print(f"   - {f.name}")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()