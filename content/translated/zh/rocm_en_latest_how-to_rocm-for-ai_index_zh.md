---
title: "Use ROCm for AI"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/index.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-04-28
---



header-article-items__start
header-article-item
[]{.fa-solid .fa-angle-right}

::: header-article-item
- [](../../index.html){.nav-link aria-label="首页"}
- 使用 ROCm（Radeon 开放计算平台）进行 AI 开发

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons

# 使用 ROCm（Radeon 开放计算平台）进行 AI

# 将 ROCm（Radeon 开放计算平台）用于 AI[\#](#use-rocm-for-ai "Link to this heading"){.headerlink}



[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026年1月29日



[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 3 分钟阅读时间



适用于 Linux

ROCm（ROCm（Radeon 开放计算平台））是一个开源软件平台，能够实现高性能计算和机器学习应用。它具有加速AI应用开发的训练、微调和推理能力。通过ROCm（ROCm（Radeon 开放计算平台）），您可以充分发挥AMD GPU的全部能力，从而显著提升AI工作负载的性能和效率。

您可以使用 ROCm（Radeon 开放计算平台）执行分布式训练，这样可以让您同时在多个 GPU 或节点上训练模型。此外，ROCm（Radeon 开放计算平台）支持混合精度训练，有助于减少训练工作负载的内存和计算需求。对于微调，ROCm（Radeon 开放计算平台）提供了各种算法和优化技术的访问。在推理方面，ROCm（Radeon 开放计算平台）提供了几种技术，可帮助您优化模型以进行部署，例如量化、GEMM 调优和可组合内核优化。

总体而言，ROCm（Radeon 开放计算平台）可用于提升 AI 应用的性能和效率。凭借对训练、微调和推理的全面支持，ROCm（Radeon 开放计算平台）为优化 AI 工作流程并在 AMD GPU 上获得最佳效果提供了完整解决方案。

AI Developer Hub 包含 [AMD ROCm（Radeon Open Compute Platform）教程](https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/){.reference .external}，用于训练、微调和推理。它利用 AMD GPU 上的流行机器学习框架。

在本指南中，您将学习如何使用 ROCm（Radeon 开放计算平台）进行人工智能开发：

- [[训练]{.doc}](training/index.html){.reference .internal}

- [[微调 LLM]{.doc}](fine-tuning/index.html){.reference .internal}



- [[推理]{.doc}](inference/index.html){.reference .internal}

- [[推理优化]{.doc}](inference-optimization/index.html){.reference .internal}

要了解 ROCm（Radeon 开放计算平台）在 HPC 应用和科学计算中的应用，请参阅 [[Using ROCm（ROCm（Radeon 开放计算平台）） for HPC]{.doc}](../rocm-for-hpc/index.html){.reference .internal}。

[](../build-rocm.html "上一页"){.left-prev}

::: prev-next-info
上一页

从源码构建 ROCm（ROCm（Radeon 开放计算平台））

[](install.html "下一页"){.right-next}

::: prev-next-info

安装 ROCm（ROCm（Radeon 开放计算平台））和深度学习框架