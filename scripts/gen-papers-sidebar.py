#!/usr/bin/env python3
"""为论文生成侧边栏条目，按 arxiv 分类组织。

使用实际生成的 MDX 文件名（并非 papers.json 中的 arxiv_id），
因为部分论文 raw markdown 缺失导致未生成 MDX。
"""
import json, os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PAPERS_DIR = (PROJECT_ROOT / "website" / "docs" / "papers").resolve()
PAPERS_JSON = (PROJECT_ROOT / "data" / "papers.json").resolve()
SIDEBARS_TS = (PROJECT_ROOT / "website" / "sidebars.ts").resolve()

# 获取实际 MDX 文件
mdx_files = {f.replace('.mdx', '') for f in os.listdir(PAPERS_DIR) if f.endswith('.mdx')}

# 分类映射
AREA_MAP = {
    'cs.DC': ('Distributed/Systems', '⚡ 分布式与系统'),
    'cs.AR': ('Architecture/Hardware', '🔧 架构与硬件'),
    'cs.AI': ('AI/ML', '🤖 AI/ML'),
    'cs.LG': ('AI/ML', '🤖 AI/ML'),
    'cs.CV': ('AI/ML', '🤖 AI/ML'),
    'cs.CL': ('AI/ML', '🤖 AI/ML'),
    'cs.PL': ('PL/Compilers', '📝 编程语言与编译器'),
    'cs.PF': ('Performance', '📊 性能优化'),
    'cs.MS': ('Modeling/Sim', '🔬 建模与仿真'),
    'cs.SE': ('Other', '📄 其他'),
    'cs.DB': ('Other', '📄 其他'),
    'cs.IR': ('Other', '📄 其他'),
    'stat.ML': ('AI/ML', '🤖 AI/ML'),
    'q-bio': ('Bio', '🧬 生物信息'),
}

with open(PAPERS_JSON) as f:
    papers = json.load(f)
data = papers if isinstance(papers, list) else papers.get('papers', [])

# 按区域分组
areas = {}
for p in data:
    aid = p.get('arxiv_id', p.get('id', ''))
    # 找到匹配的 MDX 文件名（可能带或不带版本后缀）
    matched = aid if aid in mdx_files else None
    if not matched:
        for mf in mdx_files:
            if mf.startswith(aid.rstrip('v0123456789')):
                matched = mf
                break
    if not matched:
        continue  # 无 MDX 文件，跳过
    
    area_key = 'Other'
    area_label = '📄 其他'
    for c in p.get('categories', []):
        if c in AREA_MAP:
            area_key, area_label = AREA_MAP[c]
            break
        for prefix, (ak, al) in AREA_MAP.items():
            if c.startswith(prefix):
                area_key, area_label = ak, al
                break
        if area_key != 'Other':
            break
    
    if area_key not in areas:
        areas[area_key] = {'label': area_label, 'papers': []}
    
    title = p.get('title', matched)[:80]
    areas[area_key]['papers'].append({
        'id': f"papers/{matched}",
        'title': title,
    })

# 排序：Distributed > Arch > AI/ML > Perf > PL > Modeling > Bio > Other
ORDER = ['Distributed/Systems', 'Architecture/Hardware', 'AI/ML', 'Performance', 'PL/Compilers', 'Modeling/Sim', 'Bio', 'Other']

# 生成 TypeScript 代码
lines = []
lines.append('    {')
lines.append('      type: "category",')
lines.append('      label: "📜 技术论文",')
lines.append('      collapsible: true,')
lines.append('      collapsed: true,')
lines.append('      items: [')

for area_key in ORDER:
    if area_key not in areas:
        continue
    area = areas[area_key]
    papers_list = sorted(area['papers'], key=lambda x: x['title'])
    
    lines.append('        {')
    lines.append(f'          type: "category",')
    lines.append(f'          label: "{area["label"]} ({len(papers_list)})",')
    lines.append('          collapsible: true,')
    lines.append('          collapsed: true,')
    lines.append('          items: [')
    
    for p in papers_list:
        safe_title = p['title'].replace('"', "'").replace('\\', '')
        lines.append(f'            "{p["id"]}",  // {safe_title[:60]}')
    
    lines.append('          ],')
    lines.append('        },')

lines.append('      ],')
lines.append('    },')

print('\n'.join(lines))
