---
title: "Use ROCm for AI inference optimization"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference-optimization/index.html"
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

# Use ROCm for AI inference optimization



# Use ROCm for AI inference optimization[\#](#use-rocm-for-ai-inference-optimization "Link to this heading"){.headerlink}

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 3 min read time

Applies to Linux


AI inference optimization is the process of improving the performance of machine learning models and speeding up the inference process. It includes:

- **Quantization**: This involves reducing the precision of model weights and activations while maintaining acceptable accuracy levels. Reduced precision improves inference efficiency because lower precision data requires less storage and better utilizes the hardware's computation power.

- **Kernel optimization**: This technique involves optimizing computation kernels to exploit the underlying hardware capabilities. For example, the kernels can be optimized to use multiple GPU cores or utilize specialized hardware like tensor cores to accelerate the computations.

- **Libraries**: Libraries such as Flash Attention, xFormers, and PyTorch TunableOp are used to accelerate deep learning models and improve the performance of inference workloads.

- **Hardware acceleration**: Hardware acceleration techniques, like GPUs for AI inference, can significantly improve performance due to their parallel processing capabilities.

- **Pruning**: This involves removing unnecessary connections, layers, or weights from a pre-trained model while maintaining acceptable accuracy levels, resulting in a smaller model that requires fewer computational resources to run inference.

Utilizing these optimization techniques with the ROCm™ software platform can significantly reduce inference time, improve performance, and reduce the cost of your AI applications.

Throughout the following topics, this guide discusses optimization techniques for inference workloads.

- [[Model quantization]{.doc}](model-quantization.html){.reference .internal}

- [[Model acceleration libraries]{.doc}](model-acceleration-libraries.html){.reference .internal}

- [[Optimizing with Composable Kernel]{.doc}](optimizing-with-composable-kernel.html){.reference .internal}

- [[Optimizing Triton kernels]{.doc}](optimizing-triton-kernel.html){.reference .internal}

- [[Profiling and debugging]{.doc}](profiling-and-debugging.html){.reference .internal}

- [[Workload tuning]{.doc}](workload.html){.reference .internal}


::::: prev-next-area
[](../inference/deploy-your-model.html "previous page"){.left-prev}

::: prev-next-info
previous

Deploying your model

[](model-quantization.html "next page"){.right-next}

::: prev-next-info
next

Model quantization techniques
