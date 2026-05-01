---
title: "vLLM V1 performance optimization"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference-optimization/vllm-optimization.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-01
---

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-content
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-article-container
:::::::::: {.bd-header-article .d-print-none}
::::::::: {.header-article-items .header-article__inner}
::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}
:::

::: header-article-item
- [](../../../index.html){.nav-link aria-label="Home"}
- [Use ROCm for AI](../index.html){.nav-link}
- [Use ROCm for AI inference optimization](index.html){.nav-link}
- vLLM V1\...
:::
:::::

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons
[]{.fa-solid .fa-list}
:::
::::
:::::
:::::::::
::::::::::

:::::: {#jb-print-docs-body .onlyprint}
# vLLM V1 performance optimization

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [Performance environment variables](#performance-environment-variables){.reference .internal .nav-link}
- [AITER (AI Tensor Engine for ROCm) switches](#aiter-ai-tensor-engine-for-rocm-switches){.reference .internal .nav-link}
  - [AITER MoE requirements (Mixtral, DeepSeek-V2/V3, Qwen-MoE models)](#aiter-moe-requirements-mixtral-deepseek-v2-v3-qwen-moe-models){.reference .internal .nav-link}
  - [AITER MLA requirements (DeepSeek-V3/R1 models)](#aiter-mla-requirements-deepseek-v3-r1-models){.reference .internal .nav-link}
  - [Attention backend selection with AITER](#attention-backend-selection-with-aiter){.reference .internal .nav-link}
  - [Backend choice quick recipes](#backend-choice-quick-recipes){.reference .internal .nav-link}
  - [Attention backend technical details](#attention-backend-technical-details){.reference .internal .nav-link}
- [Quick Reduce (large all-reduces on ROCm)](#quick-reduce-large-all-reduces-on-rocm){.reference .internal .nav-link}
- [Parallelism strategies (run vLLM on multiple GPUs)](#parallelism-strategies-run-vllm-on-multiple-gpus){.reference .internal .nav-link}
  - [Tensor parallelism](#tensor-parallelism){.reference .internal .nav-link}
  - [Pipeline parallelism](#pipeline-parallelism){.reference .internal .nav-link}
  - [Data parallelism](#data-parallelism){.reference .internal .nav-link}
    - [Choosing a load balancing strategy](#choosing-a-load-balancing-strategy){.reference .internal .nav-link}
    - [Data Parallel Attention (advanced)](#data-parallel-attention-advanced){.reference .internal .nav-link}
  - [Expert parallelism](#expert-parallelism){.reference .internal .nav-link}
- [Throughput benchmarking](#throughput-benchmarking){.reference .internal .nav-link}
- [Maximizing instances per node](#maximizing-instances-per-node){.reference .internal .nav-link}
- [Configure the gpu-memory-utilization parameter](#configure-the-gpu-memory-utilization-parameter){.reference .internal .nav-link}
- [vLLM engine arguments](#vllm-engine-arguments){.reference .internal .nav-link}
  - [Configure --max-num-seqs](#configure-max-num-seqs){.reference .internal .nav-link}
  - [Configure --max-num-batched-tokens](#configure-max-num-batched-tokens){.reference .internal .nav-link}
  - [Async scheduling](#async-scheduling){.reference .internal .nav-link}
  - [CUDA graphs configuration](#cuda-graphs-configuration){.reference .internal .nav-link}
- [Quantization support](#quantization-support){.reference .internal .nav-link}
  - [Supported quantization methods](#supported-quantization-methods){.reference .internal .nav-link}
  - [Using Pre-quantized Models](#using-pre-quantized-models){.reference .internal .nav-link}
  - [On-the-fly quantization](#on-the-fly-quantization){.reference .internal .nav-link}
  - [GPTQ](#gptq){.reference .internal .nav-link}
  - [AWQ (Activation-aware Weight Quantization)](#awq-activation-aware-weight-quantization){.reference .internal .nav-link}
  - [Quark (AMD quantization toolkit)](#quark-amd-quantization-toolkit){.reference .internal .nav-link}
  - [FP8 kv-cache dtype](#fp8-kv-cache-dtype){.reference .internal .nav-link}
- [Speculative decoding (experimental)](#speculative-decoding-experimental){.reference .internal .nav-link}
- [Multi-node checklist and troubleshooting](#multi-node-checklist-and-troubleshooting){.reference .internal .nav-link}
- [Further reading](#further-reading){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#vllm-v1-performance-optimization .section}
[]{#vllm-optimization}[]{#mi300x-vllm-optimization}

# vLLM V1 performance optimization[\#](#vllm-v1-performance-optimization "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 31 min read time
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils style="color:gray;"}
Applies to Linux and Windows
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
:::
:::::::
::::::::
:::::::::
::::::::::
:::::::::::

This guide helps you maximize vLLM throughput and minimize latency on AMD Instinct MI300X, MI325X, MI350X, and MI355X GPUs. Learn how to:

- Enable AITER (AI Tensor Engine for ROCm) for speedups on LLM models.

- Configure environment variables for optimal HIP, RCCL, and Quick Reduce performance.

- Select the right attention backend for your workload (AITER MHA/MLA vs. Triton).

- Choose parallelism strategies (tensor, pipeline, data, expert) for multi-GPU deployments.

- Apply quantization ([`FP8`{.docutils .literal .notranslate}]{.pre}/[`FP4`{.docutils .literal .notranslate}]{.pre}) to reduce memory usage by 2-4× with minimal accuracy loss.

- Tune engine arguments (batch size, memory utilization, graph modes) for your use case.

- Benchmark and scale across single-node and multi-node configurations.

::: {#performance-environment-variables .section}
## Performance environment variables[\#](#performance-environment-variables "Link to this heading"){.headerlink}

The following variables are generally useful for Instinct MI300X/MI355X GPUs and vLLM:

- **HIP and math libraries**

  - [`export`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`HIP_FORCE_DEV_KERNARG=1`{.docutils .literal .notranslate}]{.pre} --- improves kernel launch performance by forcing device kernel arguments. This is already set by default in [[vLLM ROCm Docker images]{.doc}](../inference/benchmark-docker/vllm.html){.reference .internal}. Bare-metal users should set this manually.

  - [`export`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`TORCH_BLAS_PREFER_HIPBLASLT=1`{.docutils .literal .notranslate}]{.pre} --- explicitly prefers hipBLASLt over hipBLAS for GEMM operations. By default, PyTorch uses heuristics to choose the best BLAS library. Setting this can improve linear layer performance in some workloads.

- **RCCL (collectives for multi-GPU)**

  - [`export`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`NCCL_MIN_NCHANNELS=112`{.docutils .literal .notranslate}]{.pre} --- increases RCCL channels from default (typically 32-64) to 112 on the Instinct MI300X. **Only beneficial for multi-GPU distributed workloads** (tensor parallelism, pipeline parallelism). Single-GPU inference does not need this.
:::

::::::::::::::::::::::::: {#aiter-ai-tensor-engine-for-rocm-switches .section}
[]{#vllm-optimization-aiter-switches}

## AITER (AI Tensor Engine for ROCm) switches[\#](#aiter-ai-tensor-engine-for-rocm-switches "Link to this heading"){.headerlink}

AITER (AI Tensor Engine for ROCm) provides ROCm-specific fused kernels optimized for Instinct MI350 Series and MI300X GPUs in vLLM V1.

How AITER flags work:

- [`VLLM_ROCM_USE_AITER`{.docutils .literal .notranslate}]{.pre} is the master switch (defaults to [`False`{.docutils .literal .notranslate}]{.pre}/[`0`{.docutils .literal .notranslate}]{.pre}).

- Individual feature flags ([`VLLM_ROCM_USE_AITER_LINEAR`{.docutils .literal .notranslate}]{.pre}, [`VLLM_ROCM_USE_AITER_MOE`{.docutils .literal .notranslate}]{.pre}, and so on) default to [`True`{.docutils .literal .notranslate}]{.pre} but only activate when the master switch is enabled.

- To enable a specific AITER feature, you must set both [`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre} and the specific feature flag to [`1`{.docutils .literal .notranslate}]{.pre}.

Quick start examples:

:::: {.highlight-bash .notranslate}
::: highlight
    # Enable all AITER optimizations (recommended for most workloads)
    export VLLM_ROCM_USE_AITER=1
    vllm serve MODEL_NAME

    # Enable AITER Fused MoE and enable Triton Prefill-Decode (split) attention
    export VLLM_ROCM_USE_AITER=1
    export VLLM_V1_USE_PREFILL_DECODE_ATTENTION=1
    export VLLM_ROCM_USE_AITER_MHA=0
    vllm serve MODEL_NAME

    # Disable AITER entirely (i.e, use vLLM Triton Unified Attention Kernel)
    export VLLM_ROCM_USE_AITER=0
    vllm serve MODEL_NAME
:::
::::

::: pst-scrollable-table-container
+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Environment variable                                                             | Description (default behavior)                                                                                                                                                                                                                                                                                                                                                                                                                    |
+==================================================================================+===================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| [`VLLM_ROCM_USE_AITER`{.docutils .literal .notranslate}]{.pre}                   | Master switch to enable AITER kernels ([`0`{.docutils .literal .notranslate}]{.pre}/[`False`{.docutils .literal .notranslate}]{.pre} by default). All other [`VLLM_ROCM_USE_AITER_*`{.docutils .literal .notranslate}]{.pre} flags require this to be set to [`1`{.docutils .literal .notranslate}]{.pre}.                                                                                                                                        |
+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`VLLM_ROCM_USE_AITER_LINEAR`{.docutils .literal .notranslate}]{.pre}            | Use AITER quantization operators + GEMM for linear layers (defaults to [`True`{.docutils .literal .notranslate}]{.pre} when AITER is on). Accelerates matrix multiplications in all transformer layers. **Recommended to keep enabled**.                                                                                                                                                                                                          |
+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`VLLM_ROCM_USE_AITER_MOE`{.docutils .literal .notranslate}]{.pre}               | Use AITER fused-MoE kernels (defaults to [`True`{.docutils .literal .notranslate}]{.pre} when AITER is on). Accelerates Mixture-of-Experts routing and computation. See the note on [[AITER MoE requirements]{.std .std-ref}](#vllm-optimization-aiter-moe-requirements){.reference .internal}.                                                                                                                                                   |
+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`VLLM_ROCM_USE_AITER_RMSNORM`{.docutils .literal .notranslate}]{.pre}           | Use AITER RMSNorm kernels (defaults to [`True`{.docutils .literal .notranslate}]{.pre} when AITER is on). Accelerates normalization layers. **Recommended: keep enabled.**                                                                                                                                                                                                                                                                        |
+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`VLLM_ROCM_USE_AITER_MLA`{.docutils .literal .notranslate}]{.pre}               | Use AITER Multi-head Latent Attention for supported models, for example, DeepSeek-V3/R1 (defaults to [`True`{.docutils .literal .notranslate}]{.pre} when AITER is on). See the section on [[AITER MLA requirements]{.std .std-ref}](#vllm-optimization-aiter-mla-requirements){.reference .internal}.                                                                                                                                            |
+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`VLLM_ROCM_USE_AITER_MHA`{.docutils .literal .notranslate}]{.pre}               | Use AITER Multi-Head Attention kernels (defaults to [`True`{.docutils .literal .notranslate}]{.pre} when AITER is on; set to [`0`{.docutils .literal .notranslate}]{.pre} to use Triton attention backends and Prefill-Decode attention backend instead). See [[attention backend selection]{.std .std-ref}](#vllm-optimization-aiter-backend-selection){.reference .internal}.                                                                   |
+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`VLLM_ROCM_USE_AITER_UNIFIED_ATTENTION`{.docutils .literal .notranslate}]{.pre} | Enable AITER's optimized unified attention kernel (defaults to [`False`{.docutils .literal .notranslate}]{.pre}). Only takes effect when: AITER is enabled; unified attention mode is active ([`VLLM_V1_USE_PREFILL_DECODE_ATTENTION=0`{.docutils .literal .notranslate}]{.pre}); and AITER MHA is disabled ([`VLLM_ROCM_USE_AITER_MHA=0`{.docutils .literal .notranslate}]{.pre}). When disabled, falls back to vLLM's Triton unified attention. |
+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`VLLM_ROCM_USE_AITER_FP8BMM`{.docutils .literal .notranslate}]{.pre}            | Use AITER [`FP8`{.docutils .literal .notranslate}]{.pre} batched matmul (defaults to [`True`{.docutils .literal .notranslate}]{.pre} when AITER is on). Fuses [`FP8`{.docutils .literal .notranslate}]{.pre} per-token quantization with batched GEMM (used in MLA models like DeepSeek-V3). Requires an Instinct MI300X/MI355X GPU.                                                                                                              |
+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`VLLM_ROCM_USE_SKINNY_GEMM`{.docutils .literal .notranslate}]{.pre}             | Prefer skinny-GEMM kernel variants for small batch sizes (defaults to [`True`{.docutils .literal .notranslate}]{.pre}). Improves performance when [`M`{.docutils .literal .notranslate}]{.pre} dimension is small. **Recommended to keep enabled**.                                                                                                                                                                                               |
+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`VLLM_ROCM_FP8_PADDING`{.docutils .literal .notranslate}]{.pre}                 | Pad [`FP8`{.docutils .literal .notranslate}]{.pre} linear weight tensors to improve memory locality (defaults to [`True`{.docutils .literal .notranslate}]{.pre}). Minor memory overhead for better performance.                                                                                                                                                                                                                                  |
+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`VLLM_ROCM_MOE_PADDING`{.docutils .literal .notranslate}]{.pre}                 | Pad MoE weight tensors for better memory access patterns (defaults to [`True`{.docutils .literal .notranslate}]{.pre}). Same memory/performance tradeoff as [`FP8`{.docutils .literal .notranslate}]{.pre} padding.                                                                                                                                                                                                                               |
+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`VLLM_ROCM_CUSTOM_PAGED_ATTN`{.docutils .literal .notranslate}]{.pre}           | Use custom paged-attention decode kernel when Prefill-Decode attention backend is selected (defaults to [`True`{.docutils .literal .notranslate}]{.pre}). See [[Attention backend selection with AITER]{.std .std-ref}](#vllm-optimization-aiter-backend-selection){.reference .internal}.                                                                                                                                                        |
+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
:::

::: {.admonition .note}
Note

When [`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre}, most AITER component flags ([`LINEAR`{.docutils .literal .notranslate}]{.pre}, [`MOE`{.docutils .literal .notranslate}]{.pre}, [`RMSNORM`{.docutils .literal .notranslate}]{.pre}, [`MLA`{.docutils .literal .notranslate}]{.pre}, [`MHA`{.docutils .literal .notranslate}]{.pre}, [`FP8BMM`{.docutils .literal .notranslate}]{.pre}) automatically default to [`True`{.docutils .literal .notranslate}]{.pre}. You typically only need to set the master switch [`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre} to enable all optimizations. ROCm provides a prebuilt optimized Docker image for validating the performance of LLM inference with vLLM on MI300X Series GPUs. The Docker image includes ROCm, vLLM, and PyTorch. For more information, see [[vLLM inference]{.doc}](../inference/benchmark-docker/vllm.html){.reference .internal}.
:::

::::: {#aiter-moe-requirements-mixtral-deepseek-v2-v3-qwen-moe-models .section}
[]{#vllm-optimization-aiter-moe-requirements}

### AITER MoE requirements (Mixtral, DeepSeek-V2/V3, Qwen-MoE models)[\#](#aiter-moe-requirements-mixtral-deepseek-v2-v3-qwen-moe-models "Link to this heading"){.headerlink}

[`VLLM_ROCM_USE_AITER_MOE`{.docutils .literal .notranslate}]{.pre} enables AITER's optimized Mixture-of-Experts kernels, such as expert routing (topk selection) and expert computation for better performance.

Applicable models:

- Mixtral series: for example, Mixtral-8x7B / Mixtral-8x22B

- Llama-4 family: for example, Llama-4-Scout-17B-16E / Llama-4-Maverick-17B-128E

- DeepSeek family: DeepSeek-V2 / DeepSeek-V3 / DeepSeek-R1

- Qwen family: Qwen1.5-MoE / Qwen2-MoE / Qwen2.5-MoE series

- Other MoE architectures

When to enable:

- **Enable (default):** For all MoE models on the Instinct MI300X/MI355X for best throughput

- **Disable:** Only for debugging or if you encounter numerical issues

Example usage:

:::: {.highlight-bash .notranslate}
::: highlight
    # Standard MoE model (Mixtral)
    VLLM_ROCM_USE_AITER=1 vllm serve mistralai/Mixtral-8x7B-Instruct-v0.1

    # Hybrid MoE+MLA model (DeepSeek-V3) - requires both MOE and MLA flags
    VLLM_ROCM_USE_AITER=1 vllm serve deepseek-ai/DeepSeek-V3 \
        --block-size 1 \
        --tensor-parallel-size 8
:::
::::
:::::

:::::: {#aiter-mla-requirements-deepseek-v3-r1-models .section}
[]{#vllm-optimization-aiter-mla-requirements}

### AITER MLA requirements (DeepSeek-V3/R1 models)[\#](#aiter-mla-requirements-deepseek-v3-r1-models "Link to this heading"){.headerlink}

[`VLLM_ROCM_USE_AITER_MLA`{.docutils .literal .notranslate}]{.pre} enables AITER MLA (Multi-head Latent Attention) optimization for supported models. Defaults to **True** when AITER is on.

Critical requirement:

- **Must** explicitly set [`--block-size`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`1`{.docutils .literal .notranslate}]{.pre}

::: {.admonition .important}
Important

If you omit [`--block-size`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`1`{.docutils .literal .notranslate}]{.pre}, vLLM will raise an error rather than defaulting to 1.
:::

Applicable models:

- DeepSeek-V3 / DeepSeek-R1

- DeepSeek-V2

- Other models using multi-head latent attention (MLA) architecture

Example usage:

:::: {.highlight-bash .notranslate}
::: highlight
    # DeepSeek-R1 with AITER MLA (requires 8 GPUs)
    VLLM_ROCM_USE_AITER=1 vllm serve deepseek-ai/DeepSeek-R1 \
        --block-size 1 \
        --tensor-parallel-size 8
:::
::::
::::::

::::::::: {#attention-backend-selection-with-aiter .section}
[]{#vllm-optimization-aiter-backend-selection}

### Attention backend selection with AITER[\#](#attention-backend-selection-with-aiter "Link to this heading"){.headerlink}

Understanding which attention backend to use helps optimize your deployment.

Quick reference: Which attention backend will I get?

Default behavior (no configuration)

Without setting any environment variables, vLLM uses:

- **vLLM Triton Unified Attention** --- A single Triton kernel handling both prefill and decode phases

- Works on all ROCm platforms

- Good baseline performance

**Recommended**: Enable AITER (set [`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre})

When you enable AITER, the backend is automatically selected based on your model:

:::: {.highlight-text .notranslate}
::: highlight
    Is your model using MLA architecture? (DeepSeek-V3/R1/V2)
    ├─ YES → AITER MLA Backend
    │         • Requires --block-size 1
    │         • Best performance for MLA models
    │         • Automatically selected
    │
    └─ NO  → AITER MHA Backend
              • For standard transformer models (Llama, Mistral, etc.)
              • Optimized for Instinct MI300X/MI355X
              • Automatically selected
:::
::::

**Advanced**: Manual backend selection

Most users won't need this, but you can override the defaults:

::: pst-scrollable-table-container
+----------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| To use this backend                                      | Set these flags                                                                                    |
+==========================================================+====================================================================================================+
| AITER MLA (MLA models only)                              | [`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre} (auto-selects for DeepSeek-V3/R1) |
+----------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| AITER MHA (standard models)                              | [`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre} (auto-selects for non-MLA models) |
+----------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| vLLM Triton Unified (default)                            | [`VLLM_ROCM_USE_AITER=0`{.docutils .literal .notranslate}]{.pre} (or unset)                        |
+----------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| Triton Prefill-Decode (split) without AITER              | ::: line                                                                                           |
|                                                          | [`VLLM_V1_USE_PREFILL_DECODE_ATTENTION=1`{.docutils .literal .notranslate}]{.pre}                  |
|                                                          | :::                                                                                                |
+----------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| Triton Prefill-Decode (split) along with AITER Fused-MoE | ::: line                                                                                           |
|                                                          | [`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre}                                   |
|                                                          | :::                                                                                                |
|                                                          |                                                                                                    |
|                                                          | ::: line                                                                                           |
|                                                          | [`VLLM_ROCM_USE_AITER_MHA=0`{.docutils .literal .notranslate}]{.pre}                               |
|                                                          | :::                                                                                                |
|                                                          |                                                                                                    |
|                                                          | ::: line                                                                                           |
|                                                          | [`VLLM_V1_USE_PREFILL_DECODE_ATTENTION=1`{.docutils .literal .notranslate}]{.pre}                  |
|                                                          | :::                                                                                                |
+----------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| AITER Unified Attention                                  | ::: line                                                                                           |
|                                                          | [`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre}                                   |
|                                                          | :::                                                                                                |
|                                                          |                                                                                                    |
|                                                          | ::: line                                                                                           |
|                                                          | [`VLLM_ROCM_USE_AITER_MHA=0`{.docutils .literal .notranslate}]{.pre}                               |
|                                                          | :::                                                                                                |
|                                                          |                                                                                                    |
|                                                          | ::: line                                                                                           |
|                                                          | [`VLLM_ROCM_USE_AITER_UNIFIED_ATTENTION=1`{.docutils .literal .notranslate}]{.pre}                 |
|                                                          | :::                                                                                                |
+----------------------------------------------------------+----------------------------------------------------------------------------------------------------+
:::

**Quick start examples**:

:::: {.highlight-bash .notranslate}
::: highlight
    # Recommended: Standard model with AITER (Llama, Mistral, Qwen, etc.)
    VLLM_ROCM_USE_AITER=1 vllm serve meta-llama/Llama-3.3-70B-Instruct

    # MLA model with AITER (DeepSeek-V3/R1)
    VLLM_ROCM_USE_AITER=1 vllm serve deepseek-ai/DeepSeek-R1 \
        --block-size 1 \
        --tensor-parallel-size 8

    # Advanced: Use Prefill-Decode split (for short input cases) with AITER Fused-MoE
    VLLM_ROCM_USE_AITER=1 \
    VLLM_ROCM_USE_AITER_MHA=0 \
    VLLM_V1_USE_PREFILL_DECODE_ATTENTION=1 \
    vllm serve meta-llama/Llama-4-Scout-17B-16E
:::
::::

**Which backend should I choose?**

::: pst-scrollable-table-container
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Your use case                                                   | Recommended backend                                                                                                                                                                                                                                                                           |
+=================================================================+===============================================================================================================================================================================================================================================================================================+
| **Standard transformer models** (Llama, Mistral, Qwen, Mixtral) | **AITER MHA** ([`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre}) --- **Recommended for most workloads** on Instinct MI300X/MI355X. Provides optimized attention kernels for both prefill and decode phases.                                                                   |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **MLA models** (DeepSeek-V3/R1/V2)                              | **AITER MLA** (auto-selected with [`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre}) --- Required for optimal performance, must use [`--block-size`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`1`{.docutils .literal .notranslate}]{.pre}    |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **gpt-oss models** (gpt-oss-120b/20b)                           | **AITER Unified Attention** ([`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre}, [`VLLM_ROCM_USE_AITER_MHA=0`{.docutils .literal .notranslate}]{.pre}, [`VLLM_ROCM_USE_AITER_UNIFIED_ATTENTION=1`{.docutils .literal .notranslate}]{.pre}) --- Required for optimal performance |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Debugging or compatibility**                                  | **vLLM Triton Unified** (default with [`VLLM_ROCM_USE_AITER=0`{.docutils .literal .notranslate}]{.pre}) --- Generic fallback, works everywhere                                                                                                                                                |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
:::

**Important notes:**

- **AITER MHA and AITER MLA are mutually exclusive** --- vLLM automatically detects MLA models and selects the appropriate backend

- **For 95% of users:** Simply set [`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre} and let vLLM choose the right backend

- When in doubt, start with AITER enabled (the recommended configuration) and profile your specific workload
:::::::::

::::: {#backend-choice-quick-recipes .section}
### Backend choice quick recipes[\#](#backend-choice-quick-recipes "Link to this heading"){.headerlink}

- **Standard transformers (any prompt length):** Start with [`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre} → AITER MHA. For CUDA graph modes, see architecture-specific guidance below (Dense vs MoE models have different optimal modes).

- **Latency-sensitive chat (low TTFT):** keep [`--max-num-batched-tokens`{.docutils .literal .notranslate}]{.pre} ≤ **8k--16k** with AITER.

- **Streaming decode (low ITL):** raise [`--max-num-batched-tokens`{.docutils .literal .notranslate}]{.pre} to **32k--64k**.

- **Offline max throughput:** [`--max-num-batched-tokens`{.docutils .literal .notranslate}]{.pre} ≥ **32k** with [`cudagraph_mode=FULL`{.docutils .literal .notranslate}]{.pre}.

**How to verify which backend is active**

Check vLLM's startup logs to confirm which attention backend is being used:

:::: {.highlight-bash .notranslate}
::: highlight
    # Start vLLM and check logs
    VLLM_ROCM_USE_AITER=1 vllm serve meta-llama/Llama-3.3-70B-Instruct 2>&1 | grep -i attention
:::
::::

**Expected log messages:**

- AITER MHA: [`Using`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`Aiter`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`Flash`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`Attention`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`backend`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`on`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`V1`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`engine.`{.docutils .literal .notranslate}]{.pre}

- AITER MLA: [`Using`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`AITER`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`MLA`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`backend`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`on`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`V1`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`engine.`{.docutils .literal .notranslate}]{.pre}

- vLLM Triton MLA: [`Using`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`Triton`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`MLA`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`backend`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`on`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`V1`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`engine.`{.docutils .literal .notranslate}]{.pre}

- vLLM Triton Unified: [`Using`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`Triton`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`Attention`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`backend`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`on`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`V1`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`engine.`{.docutils .literal .notranslate}]{.pre}

- AITER Triton Unified: [`Using`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`Aiter`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`Unified`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`Attention`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`backend`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`on`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`V1`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`engine.`{.docutils .literal .notranslate}]{.pre}

- AITER Triton Prefill-Decode: [`Using`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`Rocm`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`Attention`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`backend`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`on`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`V1`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`engine.`{.docutils .literal .notranslate}]{.pre}
:::::

::: {#attention-backend-technical-details .section}
### Attention backend technical details[\#](#attention-backend-technical-details "Link to this heading"){.headerlink}

This section provides technical details about vLLM's attention backends on ROCm.

vLLM V1 on ROCm provides these attention implementations:

1.  **vLLM Triton Unified Attention** (default when AITER is **off**)

    - Single unified Triton kernel handling both chunked prefill and decode phases

    - Generic implementation that works across all ROCm platforms

    - Good baseline performance

    - Automatically selected when [`VLLM_ROCM_USE_AITER=0`{.docutils .literal .notranslate}]{.pre} (or unset)

    - Supports GPT-OSS

2.  **AITER Triton Unified Attention** (advanced, requires manual configuration)

    - The AMD optimized unified Triton kernel

    - Enable with [`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre}, [`VLLM_ROCM_USE_AITER_MHA=0`{.docutils .literal .notranslate}]{.pre}, and [`VLLM_ROCM_USE_AITER_UNIFIED_ATTENTION=1`{.docutils .literal .notranslate}]{.pre}.

    - Only useful for specific workloads. Most users should use AITER MHA instead.

    - Recommended this backend when running GPT-OSS.

3.  **AITER Triton Prefill--Decode Attention** (hybrid, Instinct MI300X-optimized)

    - Enable with [`VLLM_V1_USE_PREFILL_DECODE_ATTENTION=1`{.docutils .literal .notranslate}]{.pre}

    - Uses separate kernels for prefill and decode phases:

      - **Prefill**: [`context_attention_fwd`{.docutils .literal .notranslate}]{.pre} Triton kernel

      - **Primary decode**: [`torch.ops._rocm_C.paged_attention`{.docutils .literal .notranslate}]{.pre} (custom ROCm kernel optimized for head sizes 64/128, block sizes 16/32, GQA 1--16, context ≤131k; sliding window not supported)

      - **Fallback decode**: [`kernel_paged_attention_2d`{.docutils .literal .notranslate}]{.pre} Triton kernel when shapes don't meet primary decode requirements

    - Usually better compared to unified Triton kernels

    - Performance vs AITER MHA varies: AITER MHA is typically faster overall, but Prefill-Decode split may win in short input scenarios

    - The custom paged attention decode kernel is controlled by [`VLLM_ROCM_CUSTOM_PAGED_ATTN`{.docutils .literal .notranslate}]{.pre} (default **True**)

4.  **AITER Multi-Head Attention (MHA)** (default when AITER is **on**)

    - Controlled by [`VLLM_ROCM_USE_AITER_MHA`{.docutils .literal .notranslate}]{.pre} (**1** = enabled)

    - Best all-around performance for standard transformer models

    - Automatically selected when [`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre} and model is not MLA

5.  **vLLM Triton Multi-head Latent Attention (MLA)** (for DeepSeek-V3/R1/V2)

    - Automatically selected when [`VLLM_ROCM_USE_AITER=0`{.docutils .literal .notranslate}]{.pre} (or unset)

6.  **AITER Multi-head Latent Attention (MLA)** (for DeepSeek-V3/R1/V2)

    - Controlled by [`VLLM_ROCM_USE_AITER_MLA`{.docutils .literal .notranslate}]{.pre} ([`1`{.docutils .literal .notranslate}]{.pre} = enabled)

    - Required for optimal performance on MLA architecture models

    - Automatically selected when [`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre} and model uses MLA

    - Requires [`--block-size`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`1`{.docutils .literal .notranslate}]{.pre}
:::
:::::::::::::::::::::::::

:::: {#quick-reduce-large-all-reduces-on-rocm .section}
## Quick Reduce (large all-reduces on ROCm)[\#](#quick-reduce-large-all-reduces-on-rocm "Link to this heading"){.headerlink}

**Quick Reduce** is an alternative to RCCL/custom all-reduce for **large** inputs (MI300-class GPUs). It supports FP16/BF16 as well as symmetric INT8/INT6/INT4 quantized all-reduce (group size 32).

::: {.admonition .warning}
Warning

Quantization can affect accuracy. Validate quality before deploying.
:::

Control via:

- [`VLLM_ROCM_QUICK_REDUCE_QUANTIZATION`{.docutils .literal .notranslate}]{.pre} ∈ [`["NONE","FP","INT8","INT6","INT4"]`{.docutils .literal .notranslate}]{.pre} (default [`NONE`{.docutils .literal .notranslate}]{.pre}).

- [`VLLM_ROCM_QUICK_REDUCE_CAST_BF16_TO_FP16`{.docutils .literal .notranslate}]{.pre}: cast BF16 input to FP16 ([`1/True`{.docutils .literal .notranslate}]{.pre} by default for performance).

- [`VLLM_ROCM_QUICK_REDUCE_MAX_SIZE_BYTES_MB`{.docutils .literal .notranslate}]{.pre}: cap the preset buffer (default [`NONE`{.docutils .literal .notranslate}]{.pre} ≈ [`2048`{.docutils .literal .notranslate}]{.pre} MB).

Quick Reduce tends to help **throughput** at higher TP counts (for example, 4--8) with many concurrent requests.
::::

::::::::::::::::::::::::::: {#parallelism-strategies-run-vllm-on-multiple-gpus .section}
## Parallelism strategies (run vLLM on multiple GPUs)[\#](#parallelism-strategies-run-vllm-on-multiple-gpus "Link to this heading"){.headerlink}

vLLM supports the following parallelism strategies:

1.  Tensor parallelism

2.  Pipeline parallelism

3.  Data parallelism

4.  Expert parallelism

For more details, see [Parallelism and scaling](https://docs.vllm.ai/en/stable/serving/parallelism_scaling.html){.reference .external}.

**Choosing the right strategy:**

- **Tensor Parallelism (TP)**: Use when model doesn't fit on one GPU. Prefer staying within a single XGMI island (≤8 GPUs on the Instinct MI300X).

- **Pipeline Parallelism (PP)**: Use for very large models across nodes. Set TP to GPUs per node, scale with PP across nodes.

- **Data Parallelism (DP)**: Use when model fits on single GPU or TP group, and you need higher throughput. Combine with TP/PP for large models.

- **Expert Parallelism (EP)**: Use for MoE models with [`--enable-expert-parallel`{.docutils .literal .notranslate}]{.pre}. More efficient than TP for MoE layers.

::::::: {#tensor-parallelism .section}
### Tensor parallelism[\#](#tensor-parallelism "Link to this heading"){.headerlink}

Tensor parallelism splits each layer of the model weights across multiple GPUs when the model doesn't fit on a single GPU. This is primarily for memory capacity.

**Use tensor parallelism when:**

- Model does not fit on one GPU (OOM)

- Need to enable larger batch sizes by distributing KV cache across GPUs

**Examples:**

:::: {.highlight-bash .notranslate}
::: highlight
    # Tensor parallelism: Split model across 2 GPUs
    vllm serve /path/to/model --dtype float16 --tensor-parallel-size 2

    # Combining TP and two vLLM instance, each split across 2 GPUs (4 GPUs total)
    CUDA_VISIBLE_DEVICES=0,1 vllm serve /path/to/model --dtype float16 --tensor-parallel-size 2 --port 8000
    CUDA_VISIBLE_DEVICES=2,3 vllm serve /path/to/model --dtype float16 --tensor-parallel-size 2 --port 8001
:::
::::

::: {.admonition .note}
Note

**ROCm GPU visibility:** vLLM on ROCm reads [`CUDA_VISIBLE_DEVICES`{.docutils .literal .notranslate}]{.pre}. Keep [`HIP_VISIBLE_DEVICES`{.docutils .literal .notranslate}]{.pre} unset to avoid conflicts.
:::

::: {.admonition .tip}
Tip

For structured data parallelism deployments with load balancing, see [[Data parallelism]{.std .std-ref}](#data-parallelism-section){.reference .internal}.
:::
:::::::

:::::: {#pipeline-parallelism .section}
### Pipeline parallelism[\#](#pipeline-parallelism "Link to this heading"){.headerlink}

Pipeline parallelism splits the model's layers across multiple GPUs or nodes, with each GPU processing different layers sequentially. This is primarily used for multi-node deployments where the model is too large for a single node.

**Use pipeline parallelism when:**

- Model is too large for a single node (combine PP with TP)

- GPUs on a node lack high-speed interconnect (e.g., no NVLink/XGMI) - PP may perform better than TP

- GPU count doesn't evenly divide the model (PP supports uneven splits)

**Common pattern for multi-node:**

:::: {.highlight-bash .notranslate}
::: highlight
    # 2 nodes × 8 GPUs = 16 GPUs total
    # TP=8 per node, PP=2 across nodes
    vllm serve meta-llama/Llama-3.1-405B-Instruct \
        --tensor-parallel-size 8 \
        --pipeline-parallel-size 2
:::
::::

::: {.admonition .note}
Note

**ROCm best practice**: On the Instinct MI300X, prefer staying within a single XGMI island (≤8 GPUs) using TP only. Use PP when scaling beyond eight GPUs or across nodes.
:::
::::::

:::::::::::: {#data-parallelism .section}
[]{#data-parallelism-section}

### Data parallelism[\#](#data-parallelism "Link to this heading"){.headerlink}

Data parallelism replicates model weights across separate instances/GPUs to process independent batches of requests. This approach increases throughput by distributing the workload across multiple replicas.

**Use data parallelism when:**

- Model fits on one GPU, but you need higher request throughput

- Scaling across multiple nodes horizontally

- Combining with tensor parallelism (for example, DP=2 + TP=4 = 8 GPUs total)

**Quick start - single-node:**

:::: {.highlight-bash .notranslate}
::: highlight
    # Model fit in 1 GPU. Creates 2 model replicas (requires 2 GPUs)
    VLLM_ALL2ALL_BACKEND="allgather_reducescatter" vllm serve /path/to/model \
        --data-parallel-size 2 \
        --disable-nccl-for-dp-synchronization
:::
::::

::: {.admonition .tip}
Tip

For ROCm, currently use [`VLLM_ALL2ALL_BACKEND="allgather_reducescatter"`{.docutils .literal .notranslate}]{.pre} and [`--disable-nccl-for-dp-synchronization`{.docutils .literal .notranslate}]{.pre} with data parallelism.
:::

::::: {#choosing-a-load-balancing-strategy .section}
#### Choosing a load balancing strategy[\#](#choosing-a-load-balancing-strategy "Link to this heading"){.headerlink}

vLLM supports two modes for routing requests to DP ranks:

::: pst-scrollable-table-container
+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                        | **Internal LB** (recommended)                                                                                                                                                                              | **External LB**                                                                                                                                                                                                                                                                                                                                                                                              |
+========================+============================================================================================================================================================================================================+==============================================================================================================================================================================================================================================================================================================================================================================================================+
| **HTTP endpoints**     | 1 endpoint, vLLM routes internally                                                                                                                                                                         | N endpoints, you provide external router                                                                                                                                                                                                                                                                                                                                                                     |
+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Single-node config** | [`--data-parallel-size`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`N`{.docutils .literal .notranslate}]{.pre}                                                            | [`--data-parallel-size`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`N`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--data-parallel-rank`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`0..N-1`{.docutils .literal .notranslate}]{.pre} + different ports                                                    |
+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Multi-node config**  | [`--data-parallel-size`{.docutils .literal .notranslate}]{.pre}, [`--data-parallel-size-local`{.docutils .literal .notranslate}]{.pre}, [`--data-parallel-address`{.docutils .literal .notranslate}]{.pre} | [`--data-parallel-size`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`N`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--data-parallel-rank`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`0..N-1`{.docutils .literal .notranslate}]{.pre} + [`--data-parallel-address`{.docutils .literal .notranslate}]{.pre} |
+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Client view**        | Single URL/port                                                                                                                                                                                            | Multiple URLs/ports                                                                                                                                                                                                                                                                                                                                                                                          |
+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Load balancer**      | Built-in (vLLM handles)                                                                                                                                                                                    | External (Nginx, Kong, K8s Service)                                                                                                                                                                                                                                                                                                                                                                          |
+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Coordination**       | DP ranks sync via RPC (for MoE/MLA)                                                                                                                                                                        | DP ranks sync via RPC (for MoE/MLA)                                                                                                                                                                                                                                                                                                                                                                          |
+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Best for**           | Most deployments (simpler)                                                                                                                                                                                 | K8s/cloud environments with existing LB                                                                                                                                                                                                                                                                                                                                                                      |
+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
:::

::: {.admonition .tip}
Tip

**Dense (non-MoE) models only:** You can run fully independent [`vllm`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`serve`{.docutils .literal .notranslate}]{.pre} instances without any DP flags, using your own load balancer. This avoids RPC coordination overhead entirely.
:::

For more technical details, see [vLLM Data Parallel Deployment](https://docs.vllm.ai/en/stable/serving/data_parallel_deployment.html){.reference .external}
:::::

::::: {#data-parallel-attention-advanced .section}
#### Data Parallel Attention (advanced)[\#](#data-parallel-attention-advanced "Link to this heading"){.headerlink}

For models with Multi-head Latent Attention (MLA) architecture like DeepSeek V2, V3, and R1, vLLM supports **Data Parallel Attention**, which provides request-level parallelism instead of model replication. This avoids KV cache duplication across tensor parallel ranks, significantly reducing memory usage and enabling larger batch sizes.

**Key benefits for MLA models:**

- Eliminates KV cache duplication when using tensor parallelism

- Enables higher throughput for high-QPS serving scenarios

- Better memory efficiency for large context windows

**Usage with Expert Parallelism:**

Data parallel attention works seamlessly with Expert Parallelism for MoE models:

:::: {.highlight-bash .notranslate}
::: highlight
    # DeepSeek-R1 with DP attention and expert parallelism
    VLLM_ALL2ALL_BACKEND="allgather_reducescatter" vllm serve deepseek-ai/DeepSeek-R1 \
        --data-parallel-size 8 \
        --enable-expert-parallel \
        --disable-nccl-for-dp-synchronization
:::
::::

For more technical details, see [vLLM RFC #16037](https://github.com/vllm-project/vllm/issues/16037){.reference .external}.
:::::
::::::::::::

::::::: {#expert-parallelism .section}
### Expert parallelism[\#](#expert-parallelism "Link to this heading"){.headerlink}

Expert parallelism (EP) distributes expert layers of Mixture-of-Experts (MoE) models across multiple GPUs, where tokens are routed to the GPUs holding the experts they need.

**Performance considerations:**

Expert parallelism is designed primarily for cross-node MoE deployments where high-bandwidth interconnects (like InfiniBand) between nodes make EP communication efficient. For single-node Instinct MI300X/MI355X deployments with XGMI connectivity, tensor parallelism typically provides better performance due to optimized all-to-all collectives on XGMI.

**When to use EP:**

- Multi-node MoE deployments with fast inter-node networking

- Models with very large numbers of experts that benefit from expert distribution

- Workloads where EP's reduced data movement outweighs communication overhead

**Single-node recommendation:** For Instinct MI300X/MI355X within a single node (≤8 GPUs), prefer tensor parallelism over expert parallelism for MoE models to leverage XGMI's high bandwidth and low latency.

**Basic usage:**

:::: {.highlight-bash .notranslate}
::: highlight
    # Enable expert parallelism for MoE models (DeepSeek example with 8 GPUs)
    vllm serve deepseek-ai/DeepSeek-R1 \
        --tensor-parallel-size 8 \
        --enable-expert-parallel
:::
::::

**Combining with Tensor Parallelism:**

When EP is enabled alongside tensor parallelism:

- Fused MoE layers use expert parallelism

- Non-fused MoE layers use tensor parallelism

**Combining with Data Parallelism:**

EP works seamlessly with Data Parallel Attention for optimal memory efficiency in MLA+MoE models (for example, DeepSeek V3):

:::: {.highlight-bash .notranslate}
::: highlight
    # DP attention + EP for DeepSeek-R1
    VLLM_ALL2ALL_BACKEND="allgather_reducescatter" vllm serve deepseek-ai/DeepSeek-R1 \
        --data-parallel-size 8 \
        --enable-expert-parallel \
        --disable-nccl-for-dp-synchronization
:::
::::
:::::::
:::::::::::::::::::::::::::

:::::: {#throughput-benchmarking .section}
## Throughput benchmarking[\#](#throughput-benchmarking "Link to this heading"){.headerlink}

This guide evaluates LLM inference by tokens per second (TPS). vLLM provides a built-in benchmark:

:::: {.highlight-bash .notranslate}
::: highlight
    # Synthetic or dataset-driven benchmark

    vllm bench throughput --model /path/to/model [other args]
:::
::::

- **Real-world dataset** (ShareGPT) example:

  :::: {.highlight-bash .notranslate}
  ::: highlight
      wget https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered/resolve/main/ShareGPT_V3_unfiltered_cleaned_split.json

      vllm bench throughput --model /path/to/model  --dataset /path/to/ShareGPT_V3_unfiltered_cleaned_split.json
  :::
  ::::

- **Synthetic**: set fixed [`--input-len`{.docutils .literal .notranslate}]{.pre} and [`--output-len`{.docutils .literal .notranslate}]{.pre} for reproducible runs.

::: {.admonition .tip}
Tip

**Profiling checklist (ROCm)**

1.  Fix your prompt distribution (ISL/OSL) and **vary one knob at a time** (graph mode, MBT).

2.  Measure **TTFT**, **ITL**, and **TPS** together; don't optimize one in isolation.

3.  Compare graph modes: **PIECEWISE** (balanced) vs **FULL**/[`FULL_DECODE_ONLY`{.docutils .literal .notranslate}]{.pre} (max throughput).

4.  Sweep [`--max-num-batched-tokens`{.docutils .literal .notranslate}]{.pre} around **8k--64k** to find your latency/throughput balance.
:::
::::::

::: {#maximizing-instances-per-node .section}
## Maximizing instances per node[\#](#maximizing-instances-per-node "Link to this heading"){.headerlink}

To maximize **per-node throughput**, run as many vLLM instances as model memory allows, balancing KV-cache capacity.

- **HBM capacities**: MI300X = 192 GB HBM3; MI355X = 288 GB HBM3E.

- Up to **eight** single-GPU vLLM instances can run in parallel on an 8×GPU node (one per GPU):

  :::: {.highlight-bash .notranslate}
  ::: highlight
      for i in $(seq 0 7); do
         CUDA_VISIBLE_DEVICES="$i" vllm bench throughput
         -tp 1 --model /path/to/model
         --dataset /path/to/ShareGPT_V3_unfiltered_cleaned_split.json &
      done
  :::
  ::::

Total throughput from **N** single-GPU instances usually exceeds one instance stretched across **N** GPUs ([`-tp`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`N`{.docutils .literal .notranslate}]{.pre}).

**Model coverage**: Llama 2 (7B/13B/70B), Llama 3 (8B/70B), Qwen2 (7B/72B), Mixtral-8x7B/8x22B, and others Llama2‑70B and Llama3‑70B can fit a single MI300X/MI355X; Llama3.1‑405B fits on a single 8×MI300X/MI355X node.
:::

::: {#configure-the-gpu-memory-utilization-parameter .section}
## Configure the gpu-memory-utilization parameter[\#](#configure-the-gpu-memory-utilization-parameter "Link to this heading"){.headerlink}

The [`--gpu-memory-utilization`{.docutils .literal .notranslate}]{.pre} parameter controls the fraction of GPU memory reserved for the KV-cache. The default is **0.9** (90%).

There are two strategies:

1.  **Increase** [`--gpu-memory-utilization`{.docutils .literal .notranslate}]{.pre} to maximize throughput for a single instance (up to **0.95**). Example:

    :::: {.highlight-bash .notranslate}
    ::: highlight
        vllm serve meta-llama/Llama-3.3-70B-Instruct \
           --gpu-memory-utilization 0.95 \
           --max-model-len 8192 \
           --port 8000
    :::
    ::::

2.  **Decrease** to pack **multiple** instances on the same GPU (for small models like 7B/8B), keeping KV-cache viable:

    :::: {.highlight-bash .notranslate}
    ::: highlight
        # Instance 1 on GPU 0
        CUDA_VISIBLE_DEVICES=0 vllm serve meta-llama/Llama-3.1-8B-Instruct \
           --gpu-memory-utilization 0.45 \
           --max-model-len 4096 \
           --port 8000

        # Instance 2 on GPU 0
        CUDA_VISIBLE_DEVICES=0 vllm serve meta-llama/Llama-Guard-3-8B \
           --gpu-memory-utilization 0.45 \
           --max-model-len 4096 \
           --port 8001
    :::
    ::::
:::

:::::::::::: {#vllm-engine-arguments .section}
## vLLM engine arguments[\#](#vllm-engine-arguments "Link to this heading"){.headerlink}

Selected arguments that often help on ROCm. See [Engine Arguments](https://docs.vllm.ai/en/stable/configuration/engine_args.html){.reference .external} in the vLLM documentation for the full list.

::::: {#configure-max-num-seqs .section}
### Configure --max-num-seqs[\#](#configure-max-num-seqs "Link to this heading"){.headerlink}

The default value is **1024** in vLLM V1 (increased from **256** in V0). This flag controls the maximum number of sequences processed per batch, directly affecting concurrency and memory usage.

- **To increase throughput**: Raise to **2048** or **4096** if memory allows, enabling more sequences per iteration.

- **To reduce memory usage**: Lower to **256** or **128** for large models or long-context generation. For example, set [`--max-num-seqs`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`128`{.docutils .literal .notranslate}]{.pre} to reduce concurrency and lower memory requirements.

In vLLM V1, KV-cache token requirements are computed as [`max-num-seqs`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`max-model-len`{.docutils .literal .notranslate}]{.pre}.

Example usage:

:::: {.highlight-bash .notranslate}
::: highlight
    vllm serve <model> --max-num-seqs 128 --max-model-len 8192
:::
::::
:::::

::: {#configure-max-num-batched-tokens .section}
### Configure --max-num-batched-tokens[\#](#configure-max-num-batched-tokens "Link to this heading"){.headerlink}

**Chunked prefill is enabled by default** in vLLM V1.

- Lower values improve **ITL** (less prefill interrupting decode).

- Higher values improve **TTFT** (more prefill per batch).

Defaults: **8192** for online serving, **16384** for offline. However, optimal values vary significantly by model size. Smaller models can efficiently handle larger batch sizes. Setting it near [`--max-model-len`{.docutils .literal .notranslate}]{.pre} mimics V0 behavior and often maximizes throughput.

**Guidance:**

- **Interactive (low TTFT)**: keep MBT ≤ **8k--16k**.

- **Streaming (low ITL)**: MBT **16k--32k**.

- **Offline max throughput**: MBT **≥32k** (diminishing TPS returns beyond \~32k).

**Pattern:** Smaller/more efficient models benefit from larger batch sizes. MoE models with expert parallelism can handle very large batches efficiently.

**Rule of thumb**

- Push MBT **up** to trade TTFT↑ for ITL↓ and slightly higher TPS.

- Pull MBT **down** to trade ITL↑ for TTFT↓ (interactive UX).
:::

::: {#async-scheduling .section}
### Async scheduling[\#](#async-scheduling "Link to this heading"){.headerlink}

[`--async-scheduling`{.docutils .literal .notranslate}]{.pre} (replaces deprecated [`num_scheduler_steps`{.docutils .literal .notranslate}]{.pre}) can improve throughput/ITL by trading off TTFT. Prefer **off** for latency-sensitive serving; **on** for offline batch throughput.
:::

:::::: {#cuda-graphs-configuration .section}
### CUDA graphs configuration[\#](#cuda-graphs-configuration "Link to this heading"){.headerlink}

CUDA graphs reduce kernel launch overhead by capturing and replaying GPU operations, improving inference throughput. Configure using [`--compilation-config`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`'{"cudagraph_mode":`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`"MODE"}'`{.docutils .literal .notranslate}]{.pre}.

**Available modes:**

- [`NONE`{.docutils .literal .notranslate}]{.pre} --- CUDA graphs disabled (debugging)

- [`PIECEWISE`{.docutils .literal .notranslate}]{.pre} --- Attention stays eager, other ops use CUDA graphs (most compatible)

- [`FULL`{.docutils .literal .notranslate}]{.pre} --- Full CUDA graphs for all batches (best for small models/prompts)

- [`FULL_DECODE_ONLY`{.docutils .literal .notranslate}]{.pre} --- Full CUDA graphs only for decode (saves memory in prefill/decode split setups)

- [`FULL_AND_PIECEWISE`{.docutils .literal .notranslate}]{.pre} --- **(default)** Full graphs for decode + piecewise for prefill (best performance, highest memory)

**Default behavior:** V1 defaults to [`FULL_AND_PIECEWISE`{.docutils .literal .notranslate}]{.pre} with piecewise compilation enabled; otherwise [`NONE`{.docutils .literal .notranslate}]{.pre}.

**Backend compatibility:** Not all attention backends support all CUDA graph modes. Choose a mode your backend supports:

::: pst-scrollable-table-container
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| Attention backend                                                  | CUDA graph support                                                                                  |
+====================================================================+=====================================================================================================+
| vLLM/AITER Triton Unified Attention, vLLM Prefill-Decode Attention | Full support (prefill + decode)                                                                     |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| AITER MHA, AITER MLA                                               | Uniform batches only                                                                                |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| vLLM Triton MLA                                                    | Must exclude attention from graph --- [`PIECEWISE`{.docutils .literal .notranslate}]{.pre} required |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
:::

**Usage examples:**

:::: {.highlight-bash .notranslate}
::: highlight
    # Default (best performance, highest memory)
    vllm serve meta-llama/Llama-3.1-8B-Instruct

    # Decode-only graphs (lower memory, good for P/D split)
    vllm serve meta-llama/Llama-3.1-8B-Instruct \
      --compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY"}'

    # Full graphs for offline throughput (small models)
    vllm serve meta-llama/Llama-3.1-8B-Instruct \
      --compilation-config '{"cudagraph_mode": "FULL"}'
:::
::::

**Migration from legacy flags:**

- [`use_cudagraph=False`{.docutils .literal .notranslate}]{.pre} → [`NONE`{.docutils .literal .notranslate}]{.pre}

- [`use_cudagraph=True,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`full_cuda_graph=False`{.docutils .literal .notranslate}]{.pre} → [`PIECEWISE`{.docutils .literal .notranslate}]{.pre}

- [`full_cuda_graph=True`{.docutils .literal .notranslate}]{.pre} → [`FULL`{.docutils .literal .notranslate}]{.pre} (with automatic fallback)
::::::
::::::::::::

:::::::::::::::::::::::::::: {#quantization-support .section}
## Quantization support[\#](#quantization-support "Link to this heading"){.headerlink}

vLLM supports FP4/FP8 (4-bit/8-bit floating point) weight and activation quantization using hardware acceleration on the Instinct MI300X and MI355X. Quantization of models with FP4/FP8 allows for a **2x-4x** reduction in model memory requirements and up to a **1.6x** improvement in throughput with minimal impact on accuracy.

vLLM ROCm supports a variety of quantization demands:

- On-the-fly quantization

- Pre-quantized model through Quark and llm-compressor

:::: {#supported-quantization-methods .section}
### Supported quantization methods[\#](#supported-quantization-methods "Link to this heading"){.headerlink}

vLLM on ROCm supports the following quantization methods for the AMD Instinct MI300 series and Instinct MI355X GPUs:

::: pst-scrollable-table-container
+------------------------+-----------------------------------------------------------------------------------------------------+--------------+------------------+-----------------------------------------------------------------------------+
| Method                 | Precision                                                                                           | ROCm support | Memory reduction | Best use case                                                               |
+========================+=====================================================================================================+==============+==================+=============================================================================+
| **FP8** (W8A8)         | 8-bit float                                                                                         | Excellent    | 2× (50%)         | Production, balanced speed/accuracy                                         |
+------------------------+-----------------------------------------------------------------------------------------------------+--------------+------------------+-----------------------------------------------------------------------------+
| **PTPC-FP8**           | 8-bit float                                                                                         | Excellent    | 2× (50%)         | High throughput, better than [`FP8`{.docutils .literal .notranslate}]{.pre} |
+------------------------+-----------------------------------------------------------------------------------------------------+--------------+------------------+-----------------------------------------------------------------------------+
| **AWQ**                | 4-bit int (W4A16)                                                                                   | Good         | 4× (75%)         | Large models, memory-constrained                                            |
+------------------------+-----------------------------------------------------------------------------------------------------+--------------+------------------+-----------------------------------------------------------------------------+
| **GPTQ**               | 4-bit/8-bit int                                                                                     | Good         | 2-4× (50-75%)    | Pre-quantized models available                                              |
+------------------------+-----------------------------------------------------------------------------------------------------+--------------+------------------+-----------------------------------------------------------------------------+
| **FP8 KV-cache**       | 8-bit float                                                                                         | Excellent    | KV cache: 50%    | All inference workloads                                                     |
+------------------------+-----------------------------------------------------------------------------------------------------+--------------+------------------+-----------------------------------------------------------------------------+
| **Quark (AMD)**        | [`FP8`{.docutils .literal .notranslate}]{.pre}/[`MXFP4`{.docutils .literal .notranslate}]{.pre}     | Optimized    | 2-4× (50-75%)    | AMD pre-quantized models                                                    |
+------------------------+-----------------------------------------------------------------------------------------------------+--------------+------------------+-----------------------------------------------------------------------------+
| **compressed-tensors** | W8A8 [`INT8`{.docutils .literal .notranslate}]{.pre}/[`FP8`{.docutils .literal .notranslate}]{.pre} | Good         | 2× (50%)         | LLM Compressor models                                                       |
+------------------------+-----------------------------------------------------------------------------------------------------+--------------+------------------+-----------------------------------------------------------------------------+
:::

**ROCm support key:**

- Excellent: Fully supported with optimized kernels

- Good: Supported, might not have AMD-optimized kernels

- Optimized: AMD-specific optimizations available
::::

::::: {#using-pre-quantized-models .section}
### Using Pre-quantized Models[\#](#using-pre-quantized-models "Link to this heading"){.headerlink}

AMD provides pre-quantized models optimized for ROCm. These models are ready to use with vLLM.

**AMD Quark-quantized models**:

Available on [Hugging Face](https://huggingface.co/models?other=quark){.reference .external}:

- [Llama‑3.1‑8B‑Instruct‑FP8‑KV](https://huggingface.co/amd/Llama-3.1-8B-Instruct-FP8-KV){.reference .external} (FP8 W8A8)

- [Llama‑3.1‑70B‑Instruct‑FP8‑KV](https://huggingface.co/amd/Llama-3.1-70B-Instruct-FP8-KV){.reference .external} (FP8 W8A8)

- [Llama‑3.1‑405B‑Instruct‑FP8‑KV](https://huggingface.co/amd/Llama-3.1-405B-Instruct-FP8-KV){.reference .external} (FP8 W8A8)

- [Mixtral‑8x7B‑Instruct‑v0.1‑FP8‑KV](https://huggingface.co/amd/Mixtral-8x7B-Instruct-v0.1-FP8-KV){.reference .external} (FP8 W8A8)

- [Mixtral‑8x22B‑Instruct‑v0.1‑FP8‑KV](https://huggingface.co/amd/Mixtral-8x22B-Instruct-v0.1-FP8-KV){.reference .external} (FP8 W8A8)

- [Llama-3.3-70B-Instruct-MXFP4-Preview](https://huggingface.co/amd/Llama-3.3-70B-Instruct-MXFP4-Preview){.reference .external} (MXFP4 for MI350/MI355)

- [Llama-3.1-405B-Instruct-MXFP4-Preview](https://huggingface.co/amd/Llama-3.1-405B-Instruct-MXFP4-Preview){.reference .external} (MXFP4 for MI350/MI355)

- [DeepSeek-R1-0528-MXFP4-Preview](https://huggingface.co/amd/DeepSeek-R1-0528-MXFP4-Preview){.reference .external} (MXFP4 for MI350/MI355)

**Quick start**:

:::: {.highlight-bash .notranslate}
::: highlight
    # FP8 W8A8 Quark model
    vllm serve amd/Llama-3.1-8B-Instruct-FP8-KV \
       --dtype auto

    # MXFP4 Quark model for MI350/MI355
    vllm serve amd/Llama-3.3-70B-Instruct-MXFP4-Preview \
       --dtype auto \
       --tensor-parallel-size 1
:::
::::

**Other pre-quantized models**:

- AWQ models: [Hugging Face awq flag](https://huggingface.co/models?other=awq){.reference .external}

- GPTQ models: [Hugging Face gptq flag](https://huggingface.co/models?other=gptq){.reference .external}

- LLM Compressor models: [Hugging Face compressed-tensors flag](https://huggingface.co/models?other=compressed-tensors){.reference .external}
:::::

:::::: {#on-the-fly-quantization .section}
### On-the-fly quantization[\#](#on-the-fly-quantization "Link to this heading"){.headerlink}

For models without pre-quantization, vLLM can quantize [`FP16`{.docutils .literal .notranslate}]{.pre}/[`BF16`{.docutils .literal .notranslate}]{.pre} models at server startup.

**Supported methods**:

- [`fp8`{.docutils .literal .notranslate}]{.pre}: Per-tensor [`FP8`{.docutils .literal .notranslate}]{.pre} weight and activation quantization

- [`ptpc_fp8`{.docutils .literal .notranslate}]{.pre}: Per-token-activation per-channel-weight [`FP8`{.docutils .literal .notranslate}]{.pre} (better accuracy same [`FP8`{.docutils .literal .notranslate}]{.pre} speed). See [PTPC-FP8 on ROCm blog post](https://blog.vllm.ai/2025/02/24/ptpc-fp8-rocm.html){.reference .external} for details

**Usage:**

:::: {.highlight-bash .notranslate}
::: highlight
    # On-the-fly FP8 quantization
    vllm serve meta-llama/Llama-3.1-8B-Instruct \
       --quantization fp8 \
       --dtype auto

    # On-the-fly PTPC-FP8 (recommended as default)
    vllm serve meta-llama/Llama-3.1-70B-Instruct \
       --quantization ptpc_fp8 \
       --dtype auto \
       --tensor-parallel-size 4
:::
::::

::: {.admonition .note}
Note

On-the-fly quantization adds two to five minutes of startup time but eliminates pre-quantization. For production with frequent restarts, use pre-quantized models.
:::
::::::

::::: {#gptq .section}
### GPTQ[\#](#gptq "Link to this heading"){.headerlink}

GPTQ is a 4-bit/8-bit weight quantization method that compresses models with minimal accuracy loss. GPTQ is fully supported on ROCm via HIP-compiled kernels in vLLM.

**ROCm support status**:

- **Fully supported** - GPTQ kernels compile and run on ROCm via HIP

- **Pre-quantized models work** with standard GPTQ kernels

**Recommendation**: For the AMD Instinct MI300X, **AWQ with Triton kernels** or **FP8 quantization** might provide better performance due to ROCm-specific optimizations, but GPTQ is a viable alternative.

**Using pre-quantized GPTQ models**:

:::: {.highlight-bash .notranslate}
::: highlight
    # Using pre-quantized GPTQ model on ROCm
    vllm serve RedHatAI/Meta-Llama-3.1-70B-Instruct-quantized.w4a16 \
       --quantization gptq \
       --dtype auto \
       --tensor-parallel-size 1
:::
::::

**Important notes**:

- **Kernel support:** GPTQ uses standard HIP-compiled kernels on ROCm

- **Performance:** AWQ with Triton kernels might offer better throughput on AMD GPUs due to ROCm optimizations

- **Compatibility:** GPTQ models from Hugging Face work on ROCm with standard performance

- **Use case:** GPTQ is suitable when pre-quantized GPTQ models are readily available
:::::

::::: {#awq-activation-aware-weight-quantization .section}
### AWQ (Activation-aware Weight Quantization)[\#](#awq-activation-aware-weight-quantization "Link to this heading"){.headerlink}

AWQ (Activation-aware Weight Quantization) is a 4-bit weight quantization technique that provides excellent model compression with minimal accuracy loss (\<1%). ROCm supports AWQ quantization on the AMD Instinct MI300 series and MI355X GPUs with vLLM.

**Using pre-quantized AWQ models:**

Many AWQ-quantized models are available on Hugging Face. Use them directly with vLLM:

:::: {.highlight-bash .notranslate}
::: highlight
    # vLLM serve with AWQ model
    VLLM_USE_TRITON_AWQ=1 \
    vllm serve hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 \
       --quantization awq \
       --tensor-parallel-size 1 \
       --dtype auto
:::
::::

**Important Notes:**

- **ROCm requirement:** Set [`VLLM_USE_TRITON_AWQ=1`{.docutils .literal .notranslate}]{.pre} to enable Triton-based AWQ kernels on ROCm

- **dtype parameter:** AWQ requires [`--dtype`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`auto`{.docutils .literal .notranslate}]{.pre} or [`--dtype`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`float16`{.docutils .literal .notranslate}]{.pre}. The [`--dtype`{.docutils .literal .notranslate}]{.pre} flag controls the **activation dtype** ([`FP16`{.docutils .literal .notranslate}]{.pre}/[`BF16`{.docutils .literal .notranslate}]{.pre} for computations), not the weight dtype. AWQ weights remain as INT4 (4-bit integers) as specified in the model's quantization config, but are dequantized to [`FP16`{.docutils .literal .notranslate}]{.pre}/[`BF16`{.docutils .literal .notranslate}]{.pre} during matrix multiplication operations.

- **Group size:** 128 is recommended for optimal performance/accuracy balance

- **Model compatibility:** AWQ is primarily tested on Llama, Mistral, and Qwen model families
:::::

::::: {#quark-amd-quantization-toolkit .section}
### Quark (AMD quantization toolkit)[\#](#quark-amd-quantization-toolkit "Link to this heading"){.headerlink}

AMD Quark is the AMD quantization toolkit optimized for ROCm. It supports [`FP8`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`W8A8`{.docutils .literal .notranslate}]{.pre}, [`MXFP4`{.docutils .literal .notranslate}]{.pre}, [`W8A8`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`INT8`{.docutils .literal .notranslate}]{.pre}, and other quantization formats with native vLLM integration. The quantization format will automatically be inferred from the model config file, so you can omit [`--quantization`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`quark`{.docutils .literal .notranslate}]{.pre}.

**Running Quark Models:**

:::: {.highlight-bash .notranslate}
::: highlight
    # FP8 W8A8: Single GPU
    vllm serve amd/Llama-3.1-8B-Instruct-FP8-KV \
       --dtype auto \
       --max-model-len 8192 \
       --gpu-memory-utilization 0.90

    # MXFP4: Extreme memory efficiency
    vllm serve amd/Llama-3.3-70B-Instruct-MXFP4-Preview \
       --dtype auto \
       --tensor-parallel-size 1 \
       --max-model-len 8192
:::
::::

**Key features:**

- **FP8 models**: \~50% memory reduction, 2× compression

- **MXFP4 models**: \~75% memory reduction, 4× compression

- **Embedded scales**: Quark FP8-KV models include pre-calibrated KV-cache scales

- **Hardware optimized**: Leverages the AMD Instinct MI300 series [`FP8`{.docutils .literal .notranslate}]{.pre} acceleration

For creating your own Quark-quantized models, see [Quark Documentation](https://quark.docs.amd.com/latest/){.reference .external}.
:::::

::::::::: {#fp8-kv-cache-dtype .section}
### FP8 kv-cache dtype[\#](#fp8-kv-cache-dtype "Link to this heading"){.headerlink}

FP8 KV-cache quantization reduces memory footprint by approximately 50%, enabling longer context lengths or higher concurrency. ROCm supports FP8 KV-cache with both [`fp8_e4m3`{.docutils .literal .notranslate}]{.pre} and [`fp8_e5m2`{.docutils .literal .notranslate}]{.pre} formats on AMD Instinct MI300 series and other CDNA™ GPUs.

Use [`--kv-cache-dtype`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`fp8`{.docutils .literal .notranslate}]{.pre} to enable [`FP8`{.docutils .literal .notranslate}]{.pre} KV-cache quantization. For best accuracy, use calibrated scaling factors generated via [LLM Compressor](https://github.com/vllm-project/llm-compressor){.reference .external}. Without calibration, scales are calculated dynamically ([`--calculate-kv-scales`{.docutils .literal .notranslate}]{.pre}) with minimal accuracy impact.

**Quick start (dynamic scaling)**:

:::: {.highlight-bash .notranslate}
::: highlight
    # vLLM serve with dynamic FP8 KV-cache
    vllm serve meta-llama/Llama-3.1-8B-Instruct \
       --kv-cache-dtype fp8 \
       --calculate-kv-scales \
       --gpu-memory-utilization 0.90
:::
::::

**Calibrated scaling (advanced)**:

For optimal accuracy, pre-calibrate KV-cache scales using representative data. The calibration process:

1.  Runs the model on calibration data (512+ samples recommended)

2.  Computes optimal [`FP8`{.docutils .literal .notranslate}]{.pre} quantization scales for key/value cache tensors

3.  Embeds these scales into the saved model as additional parameters

4.  vLLM loads the model and uses the embedded scales automatically when [`--kv-cache-dtype`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`fp8`{.docutils .literal .notranslate}]{.pre} is specified

The quantized model can be used like any other model. The embedded scales are stored as part of the model weights.

**Using pre-calibrated models:**

AMD provides ready-to-use models with pre-calibrated [`FP8`{.docutils .literal .notranslate}]{.pre} KV cache scales:

- [amd/Llama-3.1-8B-Instruct-FP8-KV](https://huggingface.co/amd/Llama-3.1-8B-Instruct-FP8-KV){.reference .external}

- [amd/Llama-3.3-70B-Instruct-FP8-KV](https://huggingface.co/amd/Llama-3.3-70B-Instruct-FP8-KV){.reference .external}

To verify a model has pre-calibrated KV cache scales, check [`config.json`{.docutils .literal .notranslate}]{.pre} for:

:::: {.highlight-json .notranslate}
::: highlight
    "quantization_config": {
      "kv_cache_scheme": "static"  // Indicates pre-calibrated scales are embedded
    }
:::
::::

**Creating your own calibrated model:**

:::: {.highlight-bash .notranslate}
::: highlight
    # 1. Install LLM Compressor
    pip install llmcompressor

    # 2. Run calibration script (see llm-compressor repo for full example)
    python llama3_fp8_kv_example.py

    # 3. Use calibrated model in vLLM
    vllm serve ./Meta-Llama-3-8B-Instruct-FP8-KV \
       --kv-cache-dtype fp8
:::
::::

For detailed instructions and the complete calibration script, see the [FP8 KV Cache Quantization Guide](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_kv_cache/README.md){.reference .external}.

**Format options**:

- [`fp8`{.docutils .literal .notranslate}]{.pre} or [`fp8_e4m3`{.docutils .literal .notranslate}]{.pre}: Higher precision (default, recommended)

- [`fp8_e5m2`{.docutils .literal .notranslate}]{.pre}: Larger dynamic range, slightly lower precision
:::::::::
::::::::::::::::::::::::::::

:::::: {#speculative-decoding-experimental .section}
## Speculative decoding (experimental)[\#](#speculative-decoding-experimental "Link to this heading"){.headerlink}

Recent vLLM versions add support for speculative decoding backends (for example, Eagle‑v3). Evaluate for your model and latency/throughput goals. Speculative decoding is a technique to reduce latency when max number of concurrency is low. Depending on the methods, the effective concurrency varies, for example, from 16 to 64.

Example command:

:::: {.highlight-bash .notranslate}
::: highlight
    vllm serve meta-llama/Llama-3.1-8B-Instruct \
       --trust-remote-code \
       --swap-space 16 \
       --disable-log-requests \
       --tensor-parallel-size 1 \
       --distributed-executor-backend mp \
       --dtype float16 \
       --quantization fp8 \
       --kv-cache-dtype fp8 \
       --no-enable-chunked-prefill \
       --max-num-seqs 300 \
       --max-num-batched-tokens 131072 \
       --gpu-memory-utilization 0.8 \
       --speculative_config '{"method": "eagle3", "model": "yuhuili/EAGLE3-LLaMA3.1-Instruct-8B", "num_speculative_tokens": 2, "draft_tensor_parallel_size": 1, "dtype": "float16"}' \
       --port 8001
:::
::::

::: {.admonition .important}
Important

It has been observed that more [`num_speculative_tokens`{.docutils .literal .notranslate}]{.pre} causes less acceptance rate of draft model tokens and a decline in throughput. As a workaround, set [`num_speculative_tokens`{.docutils .literal .notranslate}]{.pre} to \<= 2.
:::
::::::

::: {#multi-node-checklist-and-troubleshooting .section}
## Multi-node checklist and troubleshooting[\#](#multi-node-checklist-and-troubleshooting "Link to this heading"){.headerlink}

1.  Use [`--distributed-executor-backend`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`ray`{.docutils .literal .notranslate}]{.pre} across nodes to manage HIP-visible ranks and RCCL communicators. ([`ray`{.docutils .literal .notranslate}]{.pre} is the default for multi-node. Explicitly setting this flag is optional.)

2.  Ensure [`/dev/shm`{.docutils .literal .notranslate}]{.pre} is shared across ranks (Docker [`--shm-size`{.docutils .literal .notranslate}]{.pre}, Kubernetes [`emptyDir`{.docutils .literal .notranslate}]{.pre}), as RCCL uses shared memory for rendezvous.

3.  For GPUDirect RDMA, set [`RCCL_NET_GDR_LEVEL=2`{.docutils .literal .notranslate}]{.pre} and verify links ([`ibstat`{.docutils .literal .notranslate}]{.pre}). Requires supported NICs (for example, ConnectX‑6+).

4.  Collect RCCL logs: [`RCCL_DEBUG=INFO`{.docutils .literal .notranslate}]{.pre} and optionally [`RCCL_DEBUG_SUBSYS=INIT,GRAPH`{.docutils .literal .notranslate}]{.pre} for init/graph stalls.
:::

::: {#further-reading .section}
## Further reading[\#](#further-reading "Link to this heading"){.headerlink}

- [[AMD Instinct MI300X workload optimization]{.doc}](workload.html){.reference .internal}

- [[vLLM inference]{.doc}](../inference/benchmark-docker/vllm.html){.reference .internal}
:::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::: prev-next-area
[](workload.html "previous page"){.left-prev}

::: prev-next-info
previous

AMD Instinct MI300X workload optimization
:::

[](../../rocm-for-hpc/index.html "next page"){.right-next}

::: prev-next-info
next

Using ROCm for HPC
:::
:::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::: {.bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {.page-toc .tocsection .onthispage}
Contents
:::

- [Performance environment variables](#performance-environment-variables){.reference .internal .nav-link}
- [AITER (AI Tensor Engine for ROCm) switches](#aiter-ai-tensor-engine-for-rocm-switches){.reference .internal .nav-link}
  - [AITER MoE requirements (Mixtral, DeepSeek-V2/V3, Qwen-MoE models)](#aiter-moe-requirements-mixtral-deepseek-v2-v3-qwen-moe-models){.reference .internal .nav-link}
  - [AITER MLA requirements (DeepSeek-V3/R1 models)](#aiter-mla-requirements-deepseek-v3-r1-models){.reference .internal .nav-link}
  - [Attention backend selection with AITER](#attention-backend-selection-with-aiter){.reference .internal .nav-link}
  - [Backend choice quick recipes](#backend-choice-quick-recipes){.reference .internal .nav-link}
  - [Attention backend technical details](#attention-backend-technical-details){.reference .internal .nav-link}
- [Quick Reduce (large all-reduces on ROCm)](#quick-reduce-large-all-reduces-on-rocm){.reference .internal .nav-link}
- [Parallelism strategies (run vLLM on multiple GPUs)](#parallelism-strategies-run-vllm-on-multiple-gpus){.reference .internal .nav-link}
  - [Tensor parallelism](#tensor-parallelism){.reference .internal .nav-link}
  - [Pipeline parallelism](#pipeline-parallelism){.reference .internal .nav-link}
  - [Data parallelism](#data-parallelism){.reference .internal .nav-link}
    - [Choosing a load balancing strategy](#choosing-a-load-balancing-strategy){.reference .internal .nav-link}
    - [Data Parallel Attention (advanced)](#data-parallel-attention-advanced){.reference .internal .nav-link}
  - [Expert parallelism](#expert-parallelism){.reference .internal .nav-link}
- [Throughput benchmarking](#throughput-benchmarking){.reference .internal .nav-link}
- [Maximizing instances per node](#maximizing-instances-per-node){.reference .internal .nav-link}
- [Configure the gpu-memory-utilization parameter](#configure-the-gpu-memory-utilization-parameter){.reference .internal .nav-link}
- [vLLM engine arguments](#vllm-engine-arguments){.reference .internal .nav-link}
  - [Configure --max-num-seqs](#configure-max-num-seqs){.reference .internal .nav-link}
  - [Configure --max-num-batched-tokens](#configure-max-num-batched-tokens){.reference .internal .nav-link}
  - [Async scheduling](#async-scheduling){.reference .internal .nav-link}
  - [CUDA graphs configuration](#cuda-graphs-configuration){.reference .internal .nav-link}
- [Quantization support](#quantization-support){.reference .internal .nav-link}
  - [Supported quantization methods](#supported-quantization-methods){.reference .internal .nav-link}
  - [Using Pre-quantized Models](#using-pre-quantized-models){.reference .internal .nav-link}
  - [On-the-fly quantization](#on-the-fly-quantization){.reference .internal .nav-link}
  - [GPTQ](#gptq){.reference .internal .nav-link}
  - [AWQ (Activation-aware Weight Quantization)](#awq-activation-aware-weight-quantization){.reference .internal .nav-link}
  - [Quark (AMD quantization toolkit)](#quark-amd-quantization-toolkit){.reference .internal .nav-link}
  - [FP8 kv-cache dtype](#fp8-kv-cache-dtype){.reference .internal .nav-link}
- [Speculative decoding (experimental)](#speculative-decoding-experimental){.reference .internal .nav-link}
- [Multi-node checklist and troubleshooting](#multi-node-checklist-and-troubleshooting){.reference .internal .nav-link}
- [Further reading](#further-reading){.reference .internal .nav-link}
::::
:::::
::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
