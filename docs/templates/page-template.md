# MDX 页面模板 — rocm-hip-map

> **用途：** `scripts/generate-docs.py` 读取此模板生成 Docusaurus MDX 页面。
> **最后更新：** 2026-04-28

---

## 模板变量

| 变量 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `{{title}}` | string | ✅ | 文章标题 |
| `{{description}}` | string | ✅ | 摘要（≤160 字符） |
| `{{source_url}}` | string | ✅ | 原文链接 |
| `{{source_type}}` | string | ✅ | `official` / `github-issue` / `github-pr` / `blog` / `paper` / `community` |
| `{{source_org}}` | string | ✅ | `amd` / `rocm` / `pytorch` / `tensorflow` / ... |
| `{{credibility}}` | int | ✅ | 1-5 星可信度 |
| `{{lifecycle}}` | string | ✅ | `latest` / `outdated` / `deprecating` / `deprecated` |
| `{{version}}` | string | | ROCm 版本（如 `7.2.2`） |
| `{{rocm_versions}}` | list | | 兼容的 ROCm 版本列表 |
| `{{os}}` | list | | 适用操作系统：`linux` / `ubuntu-22.04` / `wsl2` / `docker` |
| `{{gpu}}` | list | | 适用 GPU：`mi250x` / `mi300x` / `rx7900xtx` |
| `{{gpu_arch}}` | list | | GPU 架构：`cdna2` / `cdna3` / `rdna3` |
| `{{driver}}` | list | | 驱动版本：`amdgpu-5.x` / `amdgpu-6.x` |
| `{{frameworks}}` | list | | 相关框架：`pytorch` / `tensorflow` / `jax` / `onnx` |
| `{{difficulty}}` | string | | 难度：`beginner` / `intermediate` / `advanced` / `reference` |
| `{{tags}}` | list | | 自定义标签（≤8 个） |
| `{{published_date}}` | string | | 原文发布日期 |
| `{{synced_date}}` | string | | 同步日期 |
| `{{is_issue}}` | bool | | 是否为 Issue/故障排查类文章 |
| `{{generated_at}}` | string | | 生成时间戳 |

---

## MDX 输出模板

```mdx
---
title: "{{title}}"
description: "{{description}}"
source_url: {{source_url}}
source_type: {{source_type}}
source_org: {{source_org}}
credibility: {{credibility}}
lifecycle: {{lifecycle}}
version: {{version}}
rocm_versions: {{rocm_versions}}
os: {{os}}
gpu: {{gpu}}
gpu_arch: {{gpu_arch}}
driver: {{driver}}
frameworks: {{frameworks}}
difficulty: {{difficulty}}
tags: {{tags}}
published_date: {{published_date}}
synced_date: {{synced_date}}
generated_at: {{generated_at}}
---

import { ArticleHeader } from "@site/src/components/ArticleHeader";
{{#is_issue}}
import IssueNotice from "@site/src/components/IssueNotice";

<IssueNotice />
{{/is_issue}}

<ArticleHeader />

> 📄 **原文链接：** [{{source_url}}]({{source_url}})
> 🏷 **来源：** AMD 官方文档 · 可信度：{{credibility_stars}}

---

{{body}}
```

---

## 合法值参考

### source_type

| 值 | 显示 |
|----|------|
| `official` | 📄 官方文档 |
| `github-issue` | 🐛 GitHub Issue |
| `github-pr` | 🔧 GitHub PR |
| `blog` | 📝 官方博客 |
| `paper` | 📜 学术论文 |
| `community` | 💬 社区讨论 |

### source_org

| 值 | 显示 |
|----|------|
| `amd` | AMD |
| `rocm` | ROCm |
| `pytorch` | PyTorch |
| `tensorflow` | TensorFlow |
| `paddle` | PaddlePaddle |
| `llvm` | LLVM |
| `mesa` | Mesa |
| `linux` | Linux Kernel |

### lifecycle

| 值 | 颜色 |
|----|------|
| `latest` | 🟢 最新 |
| `outdated` | 🟡 过时 |
| `deprecating` | 🟠 即将弃用 |
| `deprecated` | 🔴 已弃用 |

### os

| 值 | 显示 |
|----|------|
| `linux` | Linux |
| `windows` | Windows |
| `ubuntu-20.04` | Ubuntu 20.04 |
| `ubuntu-22.04` | Ubuntu 22.04 |
| `ubuntu-24.04` | Ubuntu 24.04 |
| `rhel` | RHEL |
| `arch` | Arch |
| `wsl2` | WSL2 |
| `docker` | Docker |
| `kubernetes` | K8s |

### gpu / gpu_arch / driver / frameworks / difficulty

详见 `website/src/components/ArticleMeta/index.tsx` 中的 label 映射表。

---

## 变更记录

| 日期 | 变更 | 触发需求 |
|------|------|---------|
| 2026-04-28 | 初始版本，从 `generate-docs.py` 硬编码模板提取 | 文章页面功能需求：环境分类、驱动版本等 |
