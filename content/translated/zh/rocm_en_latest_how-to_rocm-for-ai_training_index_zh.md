---
title: "Use ROCm for training"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/training/index.html"
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
- [](../../../index.html){.nav-link aria-label="Home"}
- [Use ROCm for AI](../index.html){.nav-link}
- Use ROCm\...

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons

# Use ROCm for training

# Use ROCm for training[\#](#use-rocm-for-training "Link to this heading"){.headerlink}

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 3 min read time

Applies to Linux

Training models is the process of teaching a computer program to recognize patterns in data. This involves providing the computer with large amounts of labeled data and allowing it to learn from that data, adjusting the model's parameters.

The process of training models is computationally intensive, requiring specialized hardware like GPUs to accelerate computations and reduce training time. Training models on AMD GPUs involves leveraging the parallel processing capabilities of these GPUs to significantly speed up the model training process in machine learning and deep learning tasks.

Training models on AMD GPUs with the ROCm™ software platform allows you to use the powerful parallel processing capabilities and efficient compute resource management, significantly improving training time and overall performance in machine learning applications.

The ROCm software platform makes it easier to train models on AMD GPUs while maintaining compatibility with existing code and tools. The platform also provides features like multi-GPU support, allowing for scaling and parallelization of model training across multiple GPUs to enhance performance.

The AI Developer Hub contains [AMD ROCm tutorials](https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/){.reference .external} for training, fine-tuning, and inference. It leverages popular machine learning frameworks on AMD GPUs.

In this guide, you'll learn about:

- Training a model

  - [[With Primus (Megatron-LM backend)]{.doc}](benchmark-docker/primus-megatron.html){.reference .internal}

  - [[With Megatron-LM]{.doc}](benchmark-docker/megatron-lm.html){.reference .internal}

  - [[With PyTorch]{.doc}](benchmark-docker/pytorch-training.html){.reference .internal}

  - [[With JAX MaxText]{.doc}](benchmark-docker/jax-maxtext.html){.reference .internal}

  - [[With LLM Foundry]{.doc}](benchmark-docker/mpt-llm-foundry.html){.reference .internal}

- [[Scaling model training]{.doc}](scale-model-training.html){.reference .internal}

::::: prev-next-area
[](../system-setup/system-health-check.html "previous page"){.left-prev}

::: prev-next-info
previous

System health benchmarks for AI workloads

[](benchmark-docker/primus-megatron.html "next page"){.right-next}

::: prev-next-info
next

Training a model with Primus and Megatron-LM