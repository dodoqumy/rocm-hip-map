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
- [在 AI 中使用 ROCm（Radeon 开放计算平台）](../index.html){.nav-link}
- 在 AI 中使用 ROCm（Radeon 开放计算平台）\...

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons

# 使用 ROCm（Radeon 开放计算平台）进行 AI 推理优化



# 使用 ROCm（Radeon 开放计算平台）进行 AI 推理优化[\#](#use-rocm-for-ai-inference-optimization "Link to this heading"){.headerlink}



2026年1月23日



[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 3 分钟阅读时间

适用于 Linux

AI推理优化是提高机器学习模型性能并加速推理过程的技术。它包括：

- **量化**：这涉及在保持可接受的精度水平的同时，降低模型权重和激活值的精度。降低精度可提高推理效率，因为低精度数据需要更少的存储空间，并能更好地利用硬件的计算能力。

- **内核函数 (Kernel) 优化**：这是一种优化计算内核函数以充分利用底层硬件能力的技术。例如，可以优化内核函数以使用多个 GPU 核心，或利用 tensor cores 等专用硬件来加速计算。

- **Libraries**: 库（如 Flash Attention、xFormers 和 PyTorch TunableOp）用于加速深度学习模型并提升推理工作负载的性能。

- **硬件加速**：硬件加速技术（如用于AI推理的GPU）可利用其并行处理能力显著提升性能。

- **剪枝**：这涉及从一个预训练模型中移除不必要的连接、层或权重，同时保持可接受的精度水平，从而得到一个更小的模型，需要更少的计算资源来运行推理。

结合使用这些优化技术与 ROCm（Radeon 开放计算平台）™ 软件平台，可显著缩短推理时间、提升性能并降低 AI 应用的成本。



在本指南的以下各主题中，讨论了针对推理工作负载的优化技术。



- [[模型量化]{.doc}](model-quantization.html){.reference .internal}



- [[模型加速库]{.doc}](model-acceleration-libraries.html){.reference .internal}

- [[使用可组合内核进行优化 内核函数 (Kernel)]{.doc}](optimizing-with-composable-kernel.html){.reference .internal}

- [[优化 Triton 内核]{.doc}](optimizing-triton-kernel.html){.reference .internal}

- [[性能分析]{.doc}](profiling-and-debugging.html){.reference .internal}

- [[工作负载调优]{.doc}](workload.html){.reference .internal}

::::: prev-next-area
[](../inference/deploy-your-model.html "上一页"){.left-prev}

::: prev-next-info

部署您的模型

[](model-quantization.html "下一页"){.right-next}

下一页

模型量化技术