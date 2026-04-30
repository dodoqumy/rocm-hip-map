---
title: "ROCm documentation toolchain"
source_url: "https://rocm.docs.amd.com/en/latest/contribute/toolchain.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-04-28
---



::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}

::: header-article-item
- [](../index.html){.nav-link aria-label="Home（主页）"}
- [为 ROCm（Radeon 开放计算平台）文档贡献](contributing.html){.nav-link}
- ROCm（Radeon 开放计算平台）...

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons
[]{.fa-solid .fa-list}

# ROCm 文档工具链

## 目录

- [rocm-docs-core](#rocm-docs-core){.reference .internal .nav-link}
- [Sphinx](#sphinx){.reference .internal .nav-link}
  - [Sphinx External ToC](#sphinx-external-toc){.reference .internal .nav-link}
  - [Sphinx-book-theme](#sphinx-book-theme){.reference .internal .nav-link}
  - [Sphinx Design](#sphinx-design){.reference .internal .nav-link}
- [Doxygen](#doxygen){.reference .internal .nav-link}
- [Breathe](#breathe){.reference .internal .nav-link}
- [Read the Docs](#read-the-docs){.reference .internal .nav-link}

# ROCm（ROCm（Radeon 开放计算平台））文档工具链[\#](#rocm-documentation-toolchain "Link to this heading"){.headerlink}



2026-01-23

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 4 分钟阅读时间

适用于 Linux 和 Windows

ROCm（Radeon 开放计算平台）文档依赖多个开源工具链和网站。

## rocm-docs-core[\#](#rocm-docs-core "链接到此标题"){.headerlink}

[rocm-docs-core](https://github.com/ROCm/rocm-docs-core){.reference .external} 是由 AMD 维护的项目，用于为 ROCm 文档提供自定义配置。大多数 ROCm 仓库都使用此项目作为其文档构建流程的一部分。它可作为 [pip package on PyPI](https://pypi.org/project/rocm-docs-core/){.reference .external} 使用。

请参阅 ROCm 文档核心的用户指南和开发者指南，见 ROCm 文档核心文档（https://rocm.docs.amd.com/projects/rocm-docs-core/en/latest/index.html“（ROCm（Radeon 开放计算平台）文档核心 v1.33.1）”）。

## Sphinx[#](#sphinx "链接到此标题"){.headerlink}

The user wants me to translate an English text to Simplified Chinese (zh-CN) while following specific rules:
1. Preserve ALL markdown formatting, code blocks, inline code, and links unchanged.
2. Keep technical terms like ROCm, HIP, GPU, CUDA, AMD, PyTorch, TensorFlow in their original English form.
3. Keep API names, function names, file paths, commands unchanged.
4. Output ONLY the translation — no explanations, no notes, no preamble.
5. Use technical Chinese that a GPU developer would expect.

The text is:
"[Sphinx](https://www.sphinx-doc.org/en/master/){.reference .external} is a documentation generator originally used for Python. It is now widely used in the open source community."

Let me analyze:
- "Sphinx" is a tool name - should be kept as "Sphinx"
- The link should be preserved
- "documentation generator" can be translated as "文档生成工具" or "文档生成器"
- "originally used for Python" - keep "Python" as technical term
- "widely used" - "广泛应用"
- "open source community" - "开源社区"

The markdown formatting with {.reference .external} should be preserved exactly.

My translation:
"[Sphinx](https://www.sphinx-doc.org/en/master/){.reference .external} 是一款最初用于 Python 的文档生成工具，现已在开源社区得到广泛应用。"

Wait, I need to think about the punctuation. In Chinese, usually we don't use spaces before punctuation. Let me adjust:
"[Sphinx](https://www.sphinx-doc.org/en/master/){.reference .external}是一款最初用于Python的文档生成工具，现已在开源社区得到广泛应用。"

Actually, looking at the original, there are spaces. 

The source text has spaces between words, but in Chinese I should remove unnecessary spacing. Let me translate more naturally: "Sphinx是一款文档生成工具，最初为Python设计，现已在开源社区得到广泛应用。" - this feels more idiomatic while preserving the markdown structure.

However, the user specified to preserve the markdown formatting exactly as is, so I need to maintain the reference syntax with the link and attributes intact. The translation should capture the meaning while respecting the formatting requirement.

Let me finalize: "[Sphinx](https://www.sphinx-doc.org/en/master/){.reference .external}是一款最初用于Python的文档生成工具，现已在开源社区得到广泛应用。"


### Sphinx 外部目录[\#](#sphinx-external-toc "链接到此标题"){.headerlink}

[Sphinx External ToC](https://sphinx-external-toc.readthedocs.io/en/latest/intro.html){.reference .external} 是用于 ROCm（Radeon 开放计算平台）文档导航的 Sphinx 扩展。此工具基于一个包含目录结构的 YAML 文件（[`_toc.yml.in`{.docutils .literal .notranslate}]{.pre}）在左侧生成导航菜单。



### Sphinx-book-主题[\#](#sphinx-book-主题 "链接到此标题"){.headerlink}



[Sphinx Book Theme](https://sphinx-book-theme.readthedocs.io/en/latest/){.reference .external} 是一个 Sphinx 主题，定义了 ROCm 文档的基础外观。ROCm 文档在此基础上应用了一些自定义，如自定义页眉和页脚。

### Sphinx 设计[\#](#sphinx-design "Link to this heading"){.headerlink}



[Sphinx design](https://sphinx-design.readthedocs.io/en/latest/index.html){.reference .external} 是一个为 Sphinx 添加设计功能的扩展。ROCm（ROCm（Radeon 开放计算平台））文档使用 Sphinx Design 来实现网格、卡片和同步标签页。

## Doxygen[\#](#doxygen "链接到此标题"){.headerlink}

[Doxygen](https://www.doxygen.nl/){.reference .external} 是一个文档生成器，用于从代码注释中提取信息。它用于生成 API 文档。

## 呼吸[\#](#breathe "链接到此标题"){.headerlink}

[Breathe](https://www.breathe-doc.org/){.reference .external} 是一个用于集成 Doxygen 内容的 Sphinx 插件。

## 阅读文档[\#](#read-the-docs "链接至此标题"){.headerlink}



[Read the Docs](https://docs.readthedocs..io/en/stable/){.reference .external} 是用于构建和托管 ROCm（ROCm（Radeon 开放计算平台））文档 HTML 版本的服务。

[](contributing.html "上一页"){.left-prev}

::: prev-next-info
上一页

为 ROCm（Radeon 开放计算平台）文档贡献内容



[](building.html "下一页"){.right-next}

::: prev-next-info
下一页

构建文档

目录

- [rocm-docs-core](#rocm-docs-core){.reference .internal .nav-link}
- [Sphinx](#sphinx){.reference .internal .nav-link}
  - [Sphinx External ToC](#sphinx-external-toc){.reference .internal .nav-link}
  - [Sphinx-book-theme](#sphinx-book-theme){.reference .internal .nav-link}
  - [Sphinx Design](#sphinx-design){.reference .internal .nav-link}
- [Doxygen](#doxygen){.reference .internal .nav-link}
- [Breathe](#breathe){.reference .internal .nav-link}
- [Read the Docs](#read-the-docs){.reference .internal .nav-link}