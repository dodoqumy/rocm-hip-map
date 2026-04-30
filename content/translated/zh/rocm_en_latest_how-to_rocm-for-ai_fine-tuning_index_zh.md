---
title: "Use ROCm for fine-tuning LLMs"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/fine-tuning/index.html"
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
- [](../../../index.html){.nav-link aria-label="主页"}
- [使用 ROCm（ROCm（Radeon 开放计算平台））进行 AI 开发](../index.html){.nav-link}
- [使用 ROCm（ROCm（Radeon 开放计算平台））](../index.html){.nav-link}

::::: 页眉文章项目__结束
:::: 页眉文章项
::: 文章页眉按钮



# 使用 ROCm（Radeon 开放计算平台）微调大语言模型

# 使用 ROCm（Radeon 开放计算平台）微调大语言模型[\#](#use-rocm-for-fine-tuning-llms "Link to this heading"){.headerlink}



[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026年1月23日



[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-true .article-info-read-time-svg} 3分钟阅读时间



适用于 Linux

微调是机器学习中的一项重要技术，通过在大规模数据集上预训练的模型会进一步优化，以获得更好的性能并适应特定任务或目标数据集。

使用 AMD GPU，微调过程受益于其并行处理能力和高效的资源管理，最终实现性能提升和更快的模型适应目标领域。

ROCm™ 软件平台通过支持针对 AMD GPU 定制的各种优化技术，帮助您优化此微调流程。它使大型语言模型的微调变得触手可及且高效，适用于专业任务。ROCm™ 支持更广泛的 AI 生态系统，确保与开放框架、模型和工具的无缝集成。

在以下主题中，本指南将讨论[微调大型语言模型]{.std .std-ref}的挑战，如 Llama 2。在后续章节中，您将找到关于库和工具的实践指南，以加速您的微调工作。

AI Developer Hub 包含 [AMD ROCm（ROCm（Radeon 开放计算平台））教程](https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/){.reference .external}，用于训练、微调和推理。它利用 AMD GPU 上的流行机器学习框架。



- [[LLM微调概念概述]{.doc}](overview.html){.reference .internal}

- [[微调与推理]{.doc}](fine-tuning-and-inference.html){.reference .internal} 使用[[单加速器]{.doc}](single-gpu-fine-tuning-and-inference.html){.reference .internal}或[[多加速器]{.doc}](multi-gpu-fine-tuning-and-inference.html){.reference .internal}系统。

::::: prev-next-area
[](../training/scale-model-training.html "上一页"){.left-prev}

::: prev-next-info 上一页



扩展模型训练



[](overview.html "下一页"){.right-next}

::: prev-next-info
next

大语言模型微调的概念概述