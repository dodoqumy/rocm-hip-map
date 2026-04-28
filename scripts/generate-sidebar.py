#!/usr/bin/env python3
"""生成 sidebars.ts — 从 website/docs/ 目录结构自动提取文档 ID 并生成侧边栏配置。"""
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "website" / "docs"
OUTPUT = Path(__file__).resolve().parent.parent / "website" / "sidebars.ts"

# 排除的目录
SKIP_DIRS = {"getting-started", "compatibility", "cuda-to-hip", "errors", "issues", "bilingual"}

# 来源 → 侧边栏标签
CAT_LABELS = {
    "rocm-core": "📦 ROCm 核心文档",
    "hip": "💻 HIP 编程",
    "install": "📥 安装指南",
    "hipify": "🔄 HIPIFY 迁移",
}

# rocm-core 子目录的中文标签（用于侧边栏显示）
SUBCAT_LABELS = {
    "兼容性": "兼容性",
    "参考": "参考",
    "性能调优": "性能调优",
    "总览": "总览",
    "操作指南": "操作指南",
    "术语表": "术语表",
    "概念": "概念",
    "版本发布": "版本发布",
    "系统优化": "系统优化",
    "贡献": "贡献",
    "about": "About",
    "rocm-for-ai": "ROCm for AI",
    "rocm-for-hpc": "ROCm for HPC",
    "gpu-性能": "GPU 性能",
    "参考": "参考",
    "安装步骤": "安装步骤",
}

def collect_docs():
    """收集所有文档，按 category/subcategory 组织。"""
    cats = {}
    for mdx in sorted(DOCS.rglob("*.mdx")):
        rel = mdx.relative_to(DOCS)
        parts = rel.parts
        cat = parts[0]
        if cat in SKIP_DIRS:
            continue
        subcat = parts[1] if len(parts) > 2 else "__root__"
        doc_id = str(rel.with_suffix("")).replace("\\", "/")
        cats.setdefault(cat, {}).setdefault(subcat, []).append(doc_id)
    return cats

def render_items(cats):
    """生成侧边栏条目 TypeScript 代码。"""
    lines = []
    for cat in sorted(cats.keys()):
        label = CAT_LABELS.get(cat, cat)
        lines.append("    {")
        lines.append("      type: 'category',")
        lines.append(f"      label: '{label}',")
        lines.append("      collapsible: true,")
        lines.append("      collapsed: false,")
        lines.append("      items: [")
        
        subcats = cats[cat]
        for subcat in sorted(subcats.keys()):
            sub_label = SUBCAT_LABELS.get(subcat, subcat.replace("-", " ").title())
            lines.append("        {")
            lines.append("          type: 'category',")
            lines.append(f"          label: '{sub_label}',")
            lines.append("          collapsible: true,")
            lines.append("          collapsed: true,")
            lines.append("          items: [")
            for did in subcats[subcat]:
                lines.append(f"            '{did}',")
            lines.append("          ],")
            lines.append("        },")
        
        lines.append("      ],")
        lines.append("    },")
    return "\n".join(lines)

def main():
    cats = collect_docs()
    items_code = render_items(cats)
    
    ts = f"""import type {{ SidebarsConfig }} from '@docusaurus/plugin-content-docs';

// 由 scripts/generate-sidebar.py 自动生成
// 手动编辑后运行 python3 scripts/generate-sidebar.py 覆盖

const sidebars: SidebarsConfig = {{
  docs: [
    {{
      type: 'category',
      label: '🚀 入门指南',
      collapsible: true,
      collapsed: false,
      link: {{ type: 'doc', id: 'getting-started/index' }},
      items: ['getting-started/what-is-rocm'],
    }},
{items_code}
    {{
      type: 'category',
      label: '📋 兼容性矩阵',
      collapsible: true,
      collapsed: true,
      link: {{ type: 'doc', id: 'compatibility/overview' }},
      items: [],
    }},
    {{
      type: 'category',
      label: '🔄 CUDA → HIP',
      collapsible: true,
      collapsed: true,
      link: {{ type: 'doc', id: 'cuda-to-hip/api-map' }},
      items: [],
    }},
    {{
      type: 'category',
      label: '❗ 错误码库',
      collapsible: true,
      collapsed: true,
      link: {{ type: 'doc', id: 'errors/index' }},
      items: [],
    }},
    {{
      type: 'category',
      label: '📡 Issue 情报',
      collapsible: true,
      collapsed: true,
      link: {{ type: 'doc', id: 'issues/index' }},
      items: [],
    }},
  ],
}};

export default sidebars;
"""
    with open(OUTPUT, "w") as f:
        f.write(ts)
    print(f"✅ Generated {OUTPUT}")
    print(f"   {len(cats)} categories, {sum(len(sc) for c in cats.values() for sc in c.values())} subcategories")

if __name__ == "__main__":
    main()
