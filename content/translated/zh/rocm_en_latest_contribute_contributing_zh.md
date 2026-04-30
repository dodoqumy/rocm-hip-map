---
title: "Contributing to the ROCm documentation"
source_url: "https://rocm.docs.amd.com/en/latest/contribute/contributing.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-04-28
---

[]{.fa-solid .fa-angle-right}



```markdown
::: header-article-item
- [](../index.html){.nav-link aria-label="首页"}
- 贡献指南...
```

```
::::: header-article-items__end
:::: header-article-item
::: article-header-buttons
[]{.fa-solid .fa-list}
```

# 为 ROCm（Radeon 开放计算平台）文档做贡献

## 目录

- [ROCm 仓库（ROCm（Radeon 开放计算平台））](#the-rocm-repositories){.reference .internal .nav-link}
- [编辑和添加文档](#editing-and-adding-to-the-documentation){.reference .internal .nav-link}

# 为 ROCm 文档做贡献[\#](#contributing-to-the-rocm-documentation "Link to this heading"){.headerlink}



2026年1月23日

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS73NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 5 分钟阅读时间

适用于 Linux 和 Windows

ROCm（Radeon 开放计算平台）文档，与所有 ROCm（Radeon 开放计算平台）内容一样，是开源的，可在 GitHub 上获取。您可以通过派生相应的仓库、进行更改，然后提交拉取请求来为 ROCm（Radeon 开放计算平台）文档做出贡献。

要提供关于 ROCm 文档的反馈，包括提交问题或建议功能，请参阅[[提供关于 ROCm 文档的反馈]{.std .std-doc}](feedback.html){.reference .internal}。

## ROCm 仓库[\#](#the-rocm-repositories "链接到此标题"){.headerlink}

ROCm（Radeon 开放计算平台）及其所有组件的代码仓库均可在 GitHub 上获取。

::: pst-scrollable-table-container
  模块                                    文档位置
  --------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------
  ROCm（Radeon 开放计算平台）框架                                    [ROCm/ROCm](https://github.com/ROCm/ROCm/tree/develop/docs){.github .reference .external}
  ROCm（Radeon 开放计算平台）Linux 安装                              [ROCm/rocm-install-on-linux](https://github.com/ROCm/rocm-install-on-linux/tree/develop/docs){.github .reference .external}
  ROCm（Radeon 开放计算平台）HIP（异构接口可移植性）SDK Windows 安装                  [ROCm/rocm-install-on-windows](https://github.com/ROCm/rocm-install-on-windows/tree/develop/docs){.github .reference .external}

各独立组件拥有各自的仓库，文档位于各自的 [`docs`{.docutils .literal .notranslate}]{.pre} 文件夹中。

ROCm（ROCm（Radeon 开放计算平台））各 [`docs`{.docutils .literal .notranslate}]{.pre} 文件夹中的子文件夹通常如下结构：

::: pst-scrollable-table-container
  子文件夹名称                                           文档类型
  ------------------------------------------------------- ------------------------------------------------------------------
  [`install`{.docutils .literal .notranslate}]{.pre}      安装说明、构建说明和先决条件
  [`conceptual`{.docutils .literal .notranslate}]{.pre}   重要概念
  [`how-to`{.docutils .literal .notranslate}]{.pre}       如何实现特定用例
  [`tutorials`{.docutils .literal .notranslate}]{.pre}    教程
  [`reference`{.docutils .literal .notranslate}]{.pre}   API 参考和其他参考资源

## 编辑和添加文档[\#](#editing-and-adding-to-the-documentation "Link to this heading"){.headerlink}

ROCm（ROCm（Radeon 开放计算平台））文档遵循 [Google 开发者文档样式指南](https://developers.google.com/style/highlights){.reference .external}。



ROCm（ROCm（ Radeon 开放计算平台））文档中的大多数主题使用 [reStructuredText (rst)](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html){.reference .external} 编写，部分主题使用 Markdown 编写。仅在所编辑的主题本身已采用 Markdown 时，才使用 Markdown。

要编辑或添加文档：



1. Fork 你想要添加或编辑的仓库。

2. 在本地克隆你的 fork。

3.  从仓库的 [`develop`{.docutils .literal .notranslate}]{.pre} 分支创建一个新的本地分支。

4. 修改文档

5. 可选地，在创建拉取请求之前，通过从 [`docs`{.docutils .literal .notranslate}] 文件夹内运行以下命令来本地构建文档：

::: highlight
         pip3 install -r sphinx/requirements.txt  # 你只需要运行此命令一次
         python3 -m sphinx -T -E -b html -d _build/doctrees -D language=en . _build/html

    The output files will be located in the [`docs/_build`{.docutils .literal .notranslate}]{.pre} folder. Open [`docs/_build/html/index.html`{.docutils .literal .notranslate}]{.pre} to view the documentation.

有关 ROCm（Radeon 开放计算平台）构建工具的更多信息，请参阅 [[Documentation toolchain]{.std .std-doc}](toolchain.html){.reference .internal}。

6. 推送您的更改。GitHub 链接将会在 `git push` 命令的输出中返回。在浏览器中打开此链接以创建 pull 请求。

文档的构建作为 pull request 检查的一部分，包括拼写检查和 linting。滚动到你的 pull request 底部查看所有检查。

验证 linting 和拼写检查已通过，并且文档已成功构建。新词或缩写词可以添加到[词表文件](https://github.com/ROCm/rocm-docs-core/blob/develop/.wordlist.txt){.reference .external}。词表需要获得 ROCm 文档团队的批准。

您可以通过点击拉取请求的 Read The Docs 构建检查旁边的 Details 链接来访问构建。验证您的更改已包含在构建中且显示符合预期。



GitHub 检查项默认折叠，可以通过点击"显示所有检查"来访问。

Read The Docs 构建可从 Read The Docs 检查中的详情链接访问。

您的拉取请求将由 ROCm 文档团队的一名成员进行审核。

请参阅 [GitHub 文档](https://docs.github.com/en){.reference .external}，了解如何复刻（fork）和克隆仓库，以及如何创建和推送本地分支。



重要



通过创建拉取请求（PR），您同意使您的贡献能够根据相应仓库中 LICENSE.txt 文件规定的条款进行许可。不同仓库可以使用不同的许可证。



::::: prev-next-area
[](../reference/glossary/performance.html "上一页"){.left-prev}
:::::

::: prev-next-info
上一页



性能分析术语表

[](toolchain.html "下一页"){.right-next}

::: prev-next-info
next

ROCm 文档工具链

目录

- [ROCm 仓库](#the-rocm-repositories){.reference .internal .nav-link}
- [编辑和添加文档](#editing-and-adding-to-the-documentation){.reference .internal .nav-link}