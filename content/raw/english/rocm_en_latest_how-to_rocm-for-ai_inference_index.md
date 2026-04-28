---
title: "Use ROCm for AI inference"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference/index.html"
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

# Use ROCm for AI inference



# Use ROCm for AI inference[\#](#use-rocm-for-ai-inference "Link to this heading"){.headerlink}

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-04-08

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 3 min read time

Applies to Linux


AI inference is a process of deploying a trained machine learning model to make predictions or classifications on new data. This commonly involves using the model with real-time data and making quick decisions based on the predictions made by the model.

Understanding the ROCm™ software platform's architecture and capabilities is vital for running AI inference. By leveraging the ROCm platform's capabilities, you can harness the power of high-performance computing and efficient resource management to run inference workloads, leading to faster predictions and classifications on real-time data.

Throughout the following topics, this section provides a comprehensive guide to setting up and deploying AI inference on AMD GPUs. This includes instructions on how to install ROCm, how to use Hugging Face Transformers to manage pre-trained models for natural language processing (NLP) tasks, how to validate vLLM on AMD Instinct™ MI300X GPUs and illustrate how to deploy trained models in production environments.

The AI Developer Hub contains [AMD ROCm tutorials](https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/){.reference .external} for training, fine-tuning, and inference. It leverages popular machine learning frameworks on AMD GPUs.

- [[Installing ROCm and machine learning frameworks]{.doc}](../install.html){.reference .internal}

- [[Running models from Hugging Face]{.doc}](hugging-face-models.html){.reference .internal}

- [[LLM inference frameworks]{.doc}](llm-inference-frameworks.html){.reference .internal}

- [[vLLM inference]{.doc}](benchmark-docker/vllm.html){.reference .internal}

- [[PyTorch inference performance testing]{.doc}](benchmark-docker/pytorch-inference.html){.reference .internal}

- [[SGLang inference performance testing]{.doc}](benchmark-docker/sglang.html){.reference .internal}

- [[vLLM distributed inference with MoRI]{.doc}](benchmark-docker/vllm-mori-distributed.html){.reference .internal}

- [[SGLang distributed inference with MoRI]{.doc}](benchmark-docker/sglang-mori-distributed.html){.reference .internal}

- [[SGLang distributed inference with Mooncake]{.doc}](benchmark-docker/sglang-distributed.html){.reference .internal}

- [[xDiT diffusion inference]{.doc}](xdit-diffusion-inference.html){.reference .internal}

- [[Deploying your model]{.doc}](deploy-your-model.html){.reference .internal}

- [[xDiT diffusion inference]{.doc}](xdit-diffusion-inference.html){.reference .internal}


::::: prev-next-area
[](../fine-tuning/multi-gpu-fine-tuning-and-inference.html "previous page"){.left-prev}

::: prev-next-info
previous

Fine-tuning and inference using multiple GPUs

[](hugging-face-models.html "next page"){.right-next}

::: prev-next-info
next

Running models from Hugging Face
