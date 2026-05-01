---
title: "vLLM inference performance testing"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference/benchmark-docker/previous-versions/vllm-0.10.2-20251006.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-01
---

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-content
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-article-container
:::::::::: {.bd-header-article .d-print-none}
::::::::: {.header-article-items .header-article__inner}
::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}
:::

::: header-article-item
- [](../../../../../index.html){.nav-link aria-label="Home"}
- vLLM\...
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
# vLLM inference performance testing

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [What's new](#what-s-new){.reference .internal .nav-link}
- [Supported models](#supported-models){.reference .internal .nav-link}
- [Performance measurements](#performance-measurements){.reference .internal .nav-link}
- [System validation](#system-validation){.reference .internal .nav-link}
- [Pull the Docker image](#pull-the-docker-image){.reference .internal .nav-link}
- [Benchmarking](#benchmarking){.reference .internal .nav-link}
- [Advanced usage](#advanced-usage){.reference .internal .nav-link}
  - [Reproducing the Docker image](#reproducing-the-docker-image){.reference .internal .nav-link}
- [Further reading](#further-reading){.reference .internal .nav-link}
- [Previous versions](#previous-versions){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#vllm-inference-performance-testing .section}
# vLLM inference performance testing[\#](#vllm-inference-performance-testing "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-04-21
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 96 min read time
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils style="color:gray;"}
Applies to Linux
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
:::
:::::::
::::::::
:::::::::
::::::::::
:::::::::::

::: {.admonition .caution}
Caution

This documentation does not reflect the latest version of ROCm vLLM inference performance documentation. See [[vLLM inference]{.doc}](../vllm.html){.reference .internal} for the latest version.
:::

The [ROCm vLLM Docker](https://hub.docker.com/layers/rocm/vllm/rocm7.0.0_vllm_0.10.2_20251006/images/sha256-94fd001964e1cf55c3224a445b1fb5be31a7dac302315255db8422d813edd7f5){.reference .external} image offers a prebuilt, optimized environment for validating large language model (LLM) inference performance on AMD Instinct™ MI355X, MI350X, MI325X and MI300X GPUs. This ROCm vLLM Docker image integrates vLLM and PyTorch tailored specifically for AMD data center GPUs and includes the following components:

::::: {.sd-tab-set .docutils}
rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006

:::: {.sd-tab-content .docutils}
::: pst-scrollable-table-container
  Software component   Version
  -------------------- ----------------------------------------------
  ROCm                 7.0.0
  vLLM                 0.10.2 (0.11.0rc2.dev160+g790d22168.rocm700)
  PyTorch              2.9.0a0+git1c57644
  hipBLASLt            1.0.0
:::
::::
:::::

With this Docker image, you can quickly test the [[expected inference performance numbers]{.std .std-ref}](#vllm-benchmark-performance-measurements-930){.reference .internal} for AMD Instinct GPUs.

::: {#what-s-new .section}
## What's new[\#](#what-s-new "Link to this heading"){.headerlink}

The following is summary of notable changes since the [[previous ROCm/vLLM Docker release]{.doc}](vllm-history.html){.reference .internal}.

- Added support for AMD Instinct MI355X and MI350X GPUs.

- Added support and benchmarking instructions for the following models. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal}.

  - Llama 4 Scout and Maverick

  - DeepSeek R1 0528 FP8

  - MXFP4 models (MI355X and MI350X only): Llama 3.3 70B MXFP4 and Llama 3.1 405B MXFP4

  - GPT OSS 20B and 120B

  - Qwen 3 32B, 30B-A3B, and 235B-A22B

- Removed the deprecated [`--max-seq-len-to-capture`{.docutils .literal .notranslate}]{.pre} flag.

- [`--gpu-memory-utilization`{.docutils .literal .notranslate}]{.pre} is now configurable via the [configuration files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs){.reference .external} in the MAD repository.
:::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#supported-models .section}
[]{#vllm-benchmark-supported-models-930}

## Supported models[\#](#supported-models "Link to this heading"){.headerlink}

The following models are supported for inference performance benchmarking with vLLM and ROCm. Some instructions, commands, and recommendations in this documentation might vary by model -- select one to get started. MXFP4 models are only supported on MI355X and MI350X GPUs.

::::::::::::::::::::::::::::::::::::::::: {#vllm-benchmark-ud-params-picker .container-fluid}
::::::::::: {.row .gx-0}
::: {.col-2 .me-1 .px-2 .model-param-head}
Model
:::

::::::::: {.row .col-10 .pe-0}
::: {.col-4 .px-2 .model-param param-k="model-group" param-v="llama" tabindex="0"}
Meta Llama
:::

::: {.col-4 .px-2 .model-param param-k="model-group" param-v="deepseek" tabindex="0"}
DeepSeek
:::

::: {.col-4 .px-2 .model-param param-k="model-group" param-v="gpt-oss" tabindex="0"}
OpenAI GPT OSS
:::

::: {.col-4 .px-2 .model-param param-k="model-group" param-v="mistral" tabindex="0"}
Mistral AI
:::

::: {.col-4 .px-2 .model-param param-k="model-group" param-v="qwen" tabindex="0"}
Qwen
:::

::: {.col-4 .px-2 .model-param param-k="model-group" param-v="phi" tabindex="0"}
Microsoft Phi
:::
:::::::::
:::::::::::

::::::::::::::::::::::::::::::: {.row .gx-0 .pt-1}
::: {.col-2 .me-1 .px-2 .model-param-head}
Variant
:::

::::::::::::::::::::::::::::: {.row .col-10 .pe-0}
::: {.col-4 .px-2 .model-param param-group="llama" param-k="model" param-v="pyt_vllm_llama-2-70b" tabindex="0"}
Llama 2 70B
:::

::: {.col-4 .px-2 .model-param param-group="llama" param-k="model" param-v="pyt_vllm_llama-3.1-8b" tabindex="0"}
Llama 3.1 8B
:::

::: {.col-4 .px-2 .model-param param-group="llama" param-k="model" param-v="pyt_vllm_llama-3.1-8b_fp8" tabindex="0"}
Llama 3.1 8B FP8
:::

::: {.col-4 .px-2 .model-param param-group="llama" param-k="model" param-v="pyt_vllm_llama-3.1-405b" tabindex="0"}
Llama 3.1 405B
:::

::: {.col-4 .px-2 .model-param param-group="llama" param-k="model" param-v="pyt_vllm_llama-3.1-405b_fp8" tabindex="0"}
Llama 3.1 405B FP8
:::

::: {.col-4 .px-2 .model-param param-group="llama" param-k="model" param-v="pyt_vllm_llama-3.1-405b_fp4" tabindex="0"}
Llama 3.1 405B MXFP4
:::

::: {.col-4 .px-2 .model-param param-group="llama" param-k="model" param-v="pyt_vllm_llama-3.3-70b" tabindex="0"}
Llama 3.3 70B
:::

::: {.col-4 .px-2 .model-param param-group="llama" param-k="model" param-v="pyt_vllm_llama-3.3-70b_fp8" tabindex="0"}
Llama 3.3 70B FP8
:::

::: {.col-4 .px-2 .model-param param-group="llama" param-k="model" param-v="pyt_vllm_llama-3.3-70b_fp4" tabindex="0"}
Llama 3.3 70B MXFP4
:::

::: {.col-4 .px-2 .model-param param-group="llama" param-k="model" param-v="pyt_vllm_llama-4-scout-17b-16e" tabindex="0"}
Llama 4 Scout 17Bx16E
:::

::: {.col-4 .px-2 .model-param param-group="llama" param-k="model" param-v="pyt_vllm_llama-4-maverick-17b-128e" tabindex="0"}
Llama 4 Maverick 17Bx128E
:::

::: {.col-4 .px-2 .model-param param-group="llama" param-k="model" param-v="pyt_vllm_llama-4-maverick-17b-128e_fp8" tabindex="0"}
Llama 4 Maverick 17Bx128E FP8
:::

::: {.col-6 .px-2 .model-param param-group="deepseek" param-k="model" param-v="pyt_vllm_deepseek-r1" tabindex="0"}
DeepSeek R1 0528 FP8
:::

::: {.col-6 .px-2 .model-param param-group="gpt-oss" param-k="model" param-v="pyt_vllm_gpt-oss-20b" tabindex="0"}
GPT OSS 20B
:::

::: {.col-6 .px-2 .model-param param-group="gpt-oss" param-k="model" param-v="pyt_vllm_gpt-oss-120b" tabindex="0"}
GPT OSS 120B
:::

::: {.col-6 .px-2 .model-param param-group="mistral" param-k="model" param-v="pyt_vllm_mixtral-8x7b" tabindex="0"}
Mixtral MoE 8x7B
:::

::: {.col-6 .px-2 .model-param param-group="mistral" param-k="model" param-v="pyt_vllm_mixtral-8x7b_fp8" tabindex="0"}
Mixtral MoE 8x7B FP8
:::

::: {.col-6 .px-2 .model-param param-group="mistral" param-k="model" param-v="pyt_vllm_mixtral-8x22b" tabindex="0"}
Mixtral MoE 8x22B
:::

::: {.col-6 .px-2 .model-param param-group="mistral" param-k="model" param-v="pyt_vllm_mixtral-8x22b_fp8" tabindex="0"}
Mixtral MoE 8x22B FP8
:::

::: {.col-4 .px-2 .model-param param-group="qwen" param-k="model" param-v="pyt_vllm_qwen3-8b" tabindex="0"}
Qwen3 8B
:::

::: {.col-4 .px-2 .model-param param-group="qwen" param-k="model" param-v="pyt_vllm_qwen3-32b" tabindex="0"}
Qwen3 32B
:::

::: {.col-4 .px-2 .model-param param-group="qwen" param-k="model" param-v="pyt_vllm_qwen3-30b-a3b" tabindex="0"}
Qwen3 30B A3B
:::

::: {.col-4 .px-2 .model-param param-group="qwen" param-k="model" param-v="pyt_vllm_qwen3-30b-a3b_fp8" tabindex="0"}
Qwen3 30B A3B FP8
:::

::: {.col-4 .px-2 .model-param param-group="qwen" param-k="model" param-v="pyt_vllm_qwen3-235b-a22b" tabindex="0"}
Qwen3 235B A22B
:::

::: {.col-4 .px-2 .model-param param-group="qwen" param-k="model" param-v="pyt_vllm_qwen3-235b-a22b_fp8" tabindex="0"}
Qwen3 235B A22B FP8
:::

::: {.col-6 .px-2 .model-param param-group="phi" param-k="model" param-v="pyt_vllm_phi-4" tabindex="0"}
Phi-4
:::
:::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::

:::: {#vllm-benchmark-vllm-930 .model-doc .pyt-vllm-llama-2-70b .docutils .container}
::: {.admonition .note}
Note

See the [Llama 2 70B model card on Hugging Face](https://huggingface.co/meta-llama/Llama-2-70b-chat-hf){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.
:::
::::

:::: {.model-doc .pyt-vllm-llama-3-1-8b .docutils .container}
::: {.admonition .note}
Note

See the [Llama 3.1 8B model card on Hugging Face](https://huggingface.co/meta-llama/Llama-3.1-8B){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.
:::
::::

:::: {.model-doc .pyt-vllm-llama-3-1-8b-fp8 .docutils .container}
::: {.admonition .note}
Note

See the [Llama 3.1 8B FP8 model card on Hugging Face](https://huggingface.co/amd/Llama-3.1-8B-Instruct-FP8-KV){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.

This model uses FP8 quantization via [AMD Quark](https://quark.docs.amd.com/latest/){.reference .external} for efficient inference on AMD GPUs.
:::
::::

:::: {.model-doc .pyt-vllm-llama-3-1-405b .docutils .container}
::: {.admonition .note}
Note

See the [Llama 3.1 405B model card on Hugging Face](https://huggingface.co/meta-llama/Llama-3.1-405B-Instruct){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.
:::
::::

:::: {.model-doc .pyt-vllm-llama-3-1-405b-fp8 .docutils .container}
::: {.admonition .note}
Note

See the [Llama 3.1 405B FP8 model card on Hugging Face](https://huggingface.co/amd/Llama-3.1-405B-Instruct-FP8-KV){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.

This model uses FP8 quantization via [AMD Quark](https://quark.docs.amd.com/latest/){.reference .external} for efficient inference on AMD GPUs.
:::
::::

::::: {.model-doc .pyt-vllm-llama-3-1-405b-fp4 .docutils .container}
::: {.admonition .important}
Important

MXFP4 is supported only on MI355X and MI350X GPUs.
:::

::: {.admonition .note}
Note

See the [Llama 3.1 405B MXFP4 model card on Hugging Face](https://huggingface.co/amd/Llama-3.1-405B-Instruct-MXFP4-Preview){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.

This model uses FP4 quantization via [AMD Quark](https://quark.docs.amd.com/latest/){.reference .external} for efficient inference on AMD GPUs.
:::
:::::

:::: {.model-doc .pyt-vllm-llama-3-3-70b .docutils .container}
::: {.admonition .note}
Note

See the [Llama 3.3 70B model card on Hugging Face](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.
:::
::::

:::: {.model-doc .pyt-vllm-llama-3-3-70b-fp8 .docutils .container}
::: {.admonition .note}
Note

See the [Llama 3.3 70B FP8 model card on Hugging Face](https://huggingface.co/amd/Llama-3.3-70B-Instruct-FP8-KV){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.

This model uses FP8 quantization via [AMD Quark](https://quark.docs.amd.com/latest/){.reference .external} for efficient inference on AMD GPUs.
:::
::::

::::: {.model-doc .pyt-vllm-llama-3-3-70b-fp4 .docutils .container}
::: {.admonition .important}
Important

MXFP4 is supported only on MI355X and MI350X GPUs.
:::

::: {.admonition .note}
Note

See the [Llama 3.3 70B MXFP4 model card on Hugging Face](https://huggingface.co/amd/Llama-3.3-70B-Instruct-MXFP4-Preview){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.

This model uses FP4 quantization via [AMD Quark](https://quark.docs.amd.com/latest/){.reference .external} for efficient inference on AMD GPUs.
:::
:::::

:::: {.model-doc .pyt-vllm-llama-4-scout-17b-16e .docutils .container}
::: {.admonition .note}
Note

See the [Llama 4 Scout 17Bx16E model card on Hugging Face](https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.
:::
::::

:::: {.model-doc .pyt-vllm-llama-4-maverick-17b-128e .docutils .container}
::: {.admonition .note}
Note

See the [Llama 4 Maverick 17Bx128E model card on Hugging Face](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.
:::
::::

:::: {.model-doc .pyt-vllm-llama-4-maverick-17b-128e-fp8 .docutils .container}
::: {.admonition .note}
Note

See the [Llama 4 Maverick 17Bx128E FP8 model card on Hugging Face](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.
:::
::::

:::: {.model-doc .pyt-vllm-deepseek-r1 .docutils .container}
::: {.admonition .note}
Note

See the [DeepSeek R1 0528 FP8 model card on Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.
:::
::::

:::: {.model-doc .pyt-vllm-gpt-oss-20b .docutils .container}
::: {.admonition .note}
Note

See the [GPT OSS 20B model card on Hugging Face](https://huggingface.co/openai/gpt-oss-20b){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.
:::
::::

:::: {.model-doc .pyt-vllm-gpt-oss-120b .docutils .container}
::: {.admonition .note}
Note

See the [GPT OSS 120B model card on Hugging Face](https://huggingface.co/openai/gpt-oss-120b){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.
:::
::::

:::: {.model-doc .pyt-vllm-mixtral-8x7b .docutils .container}
::: {.admonition .note}
Note

See the [Mixtral MoE 8x7B model card on Hugging Face](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.
:::
::::

:::: {.model-doc .pyt-vllm-mixtral-8x7b-fp8 .docutils .container}
::: {.admonition .note}
Note

See the [Mixtral MoE 8x7B FP8 model card on Hugging Face](https://huggingface.co/amd/Mixtral-8x7B-Instruct-v0.1-FP8-KV){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.

This model uses FP8 quantization via [AMD Quark](https://quark.docs.amd.com/latest/){.reference .external} for efficient inference on AMD GPUs.
:::
::::

:::: {.model-doc .pyt-vllm-mixtral-8x22b .docutils .container}
::: {.admonition .note}
Note

See the [Mixtral MoE 8x22B model card on Hugging Face](https://huggingface.co/mistralai/Mixtral-8x22B-Instruct-v0.1){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.
:::
::::

:::: {.model-doc .pyt-vllm-mixtral-8x22b-fp8 .docutils .container}
::: {.admonition .note}
Note

See the [Mixtral MoE 8x22B FP8 model card on Hugging Face](https://huggingface.co/amd/Mixtral-8x22B-Instruct-v0.1-FP8-KV){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.

This model uses FP8 quantization via [AMD Quark](https://quark.docs.amd.com/latest/){.reference .external} for efficient inference on AMD GPUs.
:::
::::

:::: {.model-doc .pyt-vllm-qwen3-8b .docutils .container}
::: {.admonition .note}
Note

See the [Qwen3 8B model card on Hugging Face](https://huggingface.co/Qwen/Qwen3-8B){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.
:::
::::

:::: {.model-doc .pyt-vllm-qwen3-32b .docutils .container}
::: {.admonition .note}
Note

See the [Qwen3 32B model card on Hugging Face](https://huggingface.co/Qwen/Qwen3-32B){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.
:::
::::

:::: {.model-doc .pyt-vllm-qwen3-30b-a3b .docutils .container}
::: {.admonition .note}
Note

See the [Qwen3 30B A3B model card on Hugging Face](https://huggingface.co/Qwen/Qwen3-30B-A3B){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.
:::
::::

:::: {.model-doc .pyt-vllm-qwen3-30b-a3b-fp8 .docutils .container}
::: {.admonition .note}
Note

See the [Qwen3 30B A3B FP8 model card on Hugging Face](https://huggingface.co/Qwen/Qwen3-30B-A3B-FP8){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.
:::
::::

:::: {.model-doc .pyt-vllm-qwen3-235b-a22b .docutils .container}
::: {.admonition .note}
Note

See the [Qwen3 235B A22B model card on Hugging Face](https://huggingface.co/Qwen/Qwen3-235B-A22B){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.
:::
::::

:::: {.model-doc .pyt-vllm-qwen3-235b-a22b-fp8 .docutils .container}
::: {.admonition .note}
Note

See the [Qwen3 235B A22B FP8 model card on Hugging Face](https://huggingface.co/Qwen/Qwen3-235B-A22B-FP8){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.
:::
::::

:::: {.model-doc .pyt-vllm-phi-4 .docutils .container}
::: {.admonition .note}
Note

See the [Phi-4 model card on Hugging Face](https://huggingface.co/microsoft/phi-4){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.
:::
::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::: {#performance-measurements .section}
[]{#vllm-benchmark-performance-measurements-930}

## Performance measurements[\#](#performance-measurements "Link to this heading"){.headerlink}

To evaluate performance, the [Performance results with AMD ROCm software](https://www.amd.com/en/developer/resources/rocm-hub/dev-ai/performance-results.html){.reference .external} page provides reference throughput and serving measurements for inferencing popular AI models.

::: {.admonition .important}
Important

The performance data presented in [Performance results with AMD ROCm software](https://www.amd.com/en/developer/resources/rocm-hub/dev-ai/performance-results.html){.reference .external} only reflects the latest version of this inference benchmarking environment. The listed measurements should not be interpreted as the peak performance achievable by AMD Instinct GPUs or ROCm software.
:::
::::

::: {#system-validation .section}
## System validation[\#](#system-validation "Link to this heading"){.headerlink}

Before running AI workloads, it's important to validate that your AMD hardware is configured correctly and performing optimally.

If you have already validated your system settings, including aspects like NUMA auto-balancing, you can skip this step. Otherwise, complete the procedures in the [[System validation and optimization]{.std .std-ref}](../../../system-setup/prerequisite-system-validation.html#rocm-for-ai-system-optimization){.reference .internal} guide to properly configure your system settings before starting training.

To test for optimal performance, consult the recommended [[System health benchmarks]{.std .std-ref}](../../../system-setup/system-health-check.html#rocm-for-ai-system-health-bench){.reference .internal}. This suite of tests will help you verify and fine-tune your system's configuration.
:::

::::: {#pull-the-docker-image .section}
## Pull the Docker image[\#](#pull-the-docker-image "Link to this heading"){.headerlink}

Download the [ROCm vLLM Docker image](https://hub.docker.com/layers/rocm/vllm/rocm7.0.0_vllm_0.10.2_20251006/images/sha256-94fd001964e1cf55c3224a445b1fb5be31a7dac302315255db8422d813edd7f5){.reference .external}. Use the following command to pull the Docker image from Docker Hub.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
:::
::::
:::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#benchmarking .section}
## Benchmarking[\#](#benchmarking "Link to this heading"){.headerlink}

Once the setup is complete, choose between two options to reproduce the benchmark results:

::::::::::::::: {#vllm-benchmark-mad-930 .model-doc .pyt-vllm-llama-2-70b .docutils .container}
:::::::::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to Llama 2 70B. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  On the host machine, use this command to run the performance benchmark test on the [Llama 2 70B](https://huggingface.co/meta-llama/Llama-2-70b-chat-hf){.reference .external} model using one node with the [`float16`{.docutils .literal .notranslate}]{.pre} data type.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_vllm_llama-2-70b \
            --keep-model-dir \
            --live-output
    :::
    ::::

MAD launches a Docker container with the name [`container_ci-pyt_vllm_llama-2-70b`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_vllm_llama-2-70b_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_vllm_llama-2-70b_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-930){.reference .internal} are preconfigured to collect offline throughput and online serving performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
:::

Standalone benchmarking

:::::::::::: {.sd-tab-content .docutils}
The following commands are optimized for Llama 2 70B. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

::: {.admonition .seealso}
See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs){.reference .external} in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs){.reference .external} for descriptions of available configuration options and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md){.reference .external} for additional benchmarking information.
:::

Launch the container

You can run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm7.0.0_vllm_0.10.2_20251006/images/sha256-94fd001964e1cf55c3224a445b1fb5be31a7dac302315255db8422d813edd7f5){.reference .external} as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
    docker run -it \
        --device=/dev/kfd \
        --device=/dev/dri \
        --group-add video \
        --shm-size 16G \
        --security-opt seccomp=unconfined \
        --security-opt apparmor=unconfined \
        --cap-add=SYS_PTRACE \
        -v $(pwd):/workspace \
        --env HUGGINGFACE_HUB_CACHE=/workspace \
        --name test \
        rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
:::
::::

Throughput command

Use the following command to start the throughput benchmark.

:::: {.highlight-shell .notranslate}
::: highlight
    model=meta-llama/Llama-2-70b-chat-hf
    tp=8
    num_prompts=1024
    in=128
    out=128
    dtype=auto
    kv_cache_dtype=auto
    max_num_seqs=1024
    max_num_batched_tokens=4096
    max_model_len=4096

    vllm bench throughput --model $model \
        -tp $tp \
        --num-prompts $num_prompts \
        --input-len $in \
        --output-len $out \
        --dtype $dtype \
        --kv-cache-dtype $kv_cache_dtype \
        --max-num-seqs $max_num_seqs \
        --max-num-batched-tokens $max_num_batched_tokens \
        --max-model-len $max_model_len \
        --trust-remote-code \
        --output-json ${model}_throughput.json \
        --gpu-memory-utilization 0.9
:::
::::

Serving command

1.  Start the server using the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        model=meta-llama/Llama-2-70b-chat-hf
        tp=8
        dtype=auto
        kv_cache_dtype=auto
        max_num_seqs=256
        max_num_batched_tokens=4096
        max_model_len=4096

        vllm serve $model \
            -tp $tp \
            --dtype $dtype \
            --kv-cache-dtype $kv_cache_dtype \
            --max-num-seqs $max_num_seqs \
            --max-num-batched-tokens $max_num_batched_tokens \
            --max-model-len $max_model_len \
            --no-enable-prefix-caching \
            --swap-space 16 \
            --disable-log-requests \
            --trust-remote-code \
            --gpu-memory-utilization 0.9
    :::
    ::::

    Wait until the model has loaded and the server is ready to accept requests.

2.  On another terminal on the same machine, run the benchmark:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # Connect to the container
        docker exec -it test bash

        # Wait for the server to start
        until curl -s http://localhost:8000/v1/models; do sleep 30; done

        # Run the benchmark
        model=meta-llama/Llama-2-70b-chat-hf
        max_concurrency=1
        num_prompts=10
        in=128
        out=128
        vllm bench serve --model $model \
            --percentile-metrics "ttft,tpot,itl,e2el" \
            --dataset-name random \
            --ignore-eos \
            --max-concurrency $max_concurrency \
            --num-prompts $num_prompts \
            --random-input-len $in \
            --random-output-len $out \
            --trust-remote-code \
            --save-result \
            --result-filename ${model}_serving.json
    :::
    ::::

::::: {.admonition .note}
Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B, try adding [`export`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre} to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:::: {.highlight-default .notranslate}
::: highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token
:::
::::
:::::

`<style>
mjx-container[jax="CHTML"][display="true"] {
   text-align: left;
   margin: 0;
}
</style>`{=html}

::: {.admonition .note}
Note

Throughput is calculated as:

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  :::

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  :::
:::
::::::::::::
::::::::::::::
:::::::::::::::

::::::::::::::: {.model-doc .pyt-vllm-llama-3-1-8b .docutils .container}
:::::::::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to Llama 3.1 8B. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  On the host machine, use this command to run the performance benchmark test on the [Llama 3.1 8B](https://huggingface.co/meta-llama/Llama-3.1-8B){.reference .external} model using one node with the [`float16`{.docutils .literal .notranslate}]{.pre} data type.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_vllm_llama-3.1-8b \
            --keep-model-dir \
            --live-output
    :::
    ::::

MAD launches a Docker container with the name [`container_ci-pyt_vllm_llama-3.1-8b`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_vllm_llama-3.1-8b_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_vllm_llama-3.1-8b_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-930){.reference .internal} are preconfigured to collect offline throughput and online serving performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
:::

Standalone benchmarking

:::::::::::: {.sd-tab-content .docutils}
The following commands are optimized for Llama 3.1 8B. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

::: {.admonition .seealso}
See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs){.reference .external} in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs){.reference .external} for descriptions of available configuration options and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md){.reference .external} for additional benchmarking information.
:::

Launch the container

You can run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm7.0.0_vllm_0.10.2_20251006/images/sha256-94fd001964e1cf55c3224a445b1fb5be31a7dac302315255db8422d813edd7f5){.reference .external} as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
    docker run -it \
        --device=/dev/kfd \
        --device=/dev/dri \
        --group-add video \
        --shm-size 16G \
        --security-opt seccomp=unconfined \
        --security-opt apparmor=unconfined \
        --cap-add=SYS_PTRACE \
        -v $(pwd):/workspace \
        --env HUGGINGFACE_HUB_CACHE=/workspace \
        --name test \
        rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
:::
::::

Throughput command

Use the following command to start the throughput benchmark.

:::: {.highlight-shell .notranslate}
::: highlight
    model=meta-llama/Llama-3.1-8B-Instruct
    tp=1
    num_prompts=1024
    in=128
    out=128
    dtype=auto
    kv_cache_dtype=auto
    max_num_seqs=1024
    max_num_batched_tokens=131072
    max_model_len=8192

    vllm bench throughput --model $model \
        -tp $tp \
        --num-prompts $num_prompts \
        --input-len $in \
        --output-len $out \
        --dtype $dtype \
        --kv-cache-dtype $kv_cache_dtype \
        --max-num-seqs $max_num_seqs \
        --max-num-batched-tokens $max_num_batched_tokens \
        --max-model-len $max_model_len \
        --trust-remote-code \
        --output-json ${model}_throughput.json \
        --gpu-memory-utilization 0.9
:::
::::

Serving command

1.  Start the server using the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        model=meta-llama/Llama-3.1-8B-Instruct
        tp=1
        dtype=auto
        kv_cache_dtype=auto
        max_num_seqs=256
        max_num_batched_tokens=131072
        max_model_len=8192

        vllm serve $model \
            -tp $tp \
            --dtype $dtype \
            --kv-cache-dtype $kv_cache_dtype \
            --max-num-seqs $max_num_seqs \
            --max-num-batched-tokens $max_num_batched_tokens \
            --max-model-len $max_model_len \
            --no-enable-prefix-caching \
            --swap-space 16 \
            --disable-log-requests \
            --trust-remote-code \
            --gpu-memory-utilization 0.9
    :::
    ::::

    Wait until the model has loaded and the server is ready to accept requests.

2.  On another terminal on the same machine, run the benchmark:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # Connect to the container
        docker exec -it test bash

        # Wait for the server to start
        until curl -s http://localhost:8000/v1/models; do sleep 30; done

        # Run the benchmark
        model=meta-llama/Llama-3.1-8B-Instruct
        max_concurrency=1
        num_prompts=10
        in=128
        out=128
        vllm bench serve --model $model \
            --percentile-metrics "ttft,tpot,itl,e2el" \
            --dataset-name random \
            --ignore-eos \
            --max-concurrency $max_concurrency \
            --num-prompts $num_prompts \
            --random-input-len $in \
            --random-output-len $out \
            --trust-remote-code \
            --save-result \
            --result-filename ${model}_serving.json
    :::
    ::::

::::: {.admonition .note}
Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B, try adding [`export`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre} to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:::: {.highlight-default .notranslate}
::: highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token
:::
::::
:::::

`<style>
mjx-container[jax="CHTML"][display="true"] {
   text-align: left;
   margin: 0;
}
</style>`{=html}

::: {.admonition .note}
Note

Throughput is calculated as:

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  :::

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  :::
:::
::::::::::::
::::::::::::::
:::::::::::::::

::::::::::::::: {.model-doc .pyt-vllm-llama-3-1-8b-fp8 .docutils .container}
:::::::::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to Llama 3.1 8B FP8. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  On the host machine, use this command to run the performance benchmark test on the [Llama 3.1 8B FP8](https://huggingface.co/amd/Llama-3.1-8B-Instruct-FP8-KV){.reference .external} model using one node with the [`float8`{.docutils .literal .notranslate}]{.pre} data type.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_vllm_llama-3.1-8b_fp8 \
            --keep-model-dir \
            --live-output
    :::
    ::::

MAD launches a Docker container with the name [`container_ci-pyt_vllm_llama-3.1-8b_fp8`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_vllm_llama-3.1-8b_fp8_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_vllm_llama-3.1-8b_fp8_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-930){.reference .internal} are preconfigured to collect offline throughput and online serving performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
:::

Standalone benchmarking

:::::::::::: {.sd-tab-content .docutils}
The following commands are optimized for Llama 3.1 8B FP8. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

::: {.admonition .seealso}
See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs){.reference .external} in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs){.reference .external} for descriptions of available configuration options and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md){.reference .external} for additional benchmarking information.
:::

Launch the container

You can run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm7.0.0_vllm_0.10.2_20251006/images/sha256-94fd001964e1cf55c3224a445b1fb5be31a7dac302315255db8422d813edd7f5){.reference .external} as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
    docker run -it \
        --device=/dev/kfd \
        --device=/dev/dri \
        --group-add video \
        --shm-size 16G \
        --security-opt seccomp=unconfined \
        --security-opt apparmor=unconfined \
        --cap-add=SYS_PTRACE \
        -v $(pwd):/workspace \
        --env HUGGINGFACE_HUB_CACHE=/workspace \
        --name test \
        rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
:::
::::

Throughput command

Use the following command to start the throughput benchmark.

:::: {.highlight-shell .notranslate}
::: highlight
    model=amd/Llama-3.1-8B-Instruct-FP8-KV
    tp=1
    num_prompts=1024
    in=128
    out=128
    dtype=auto
    kv_cache_dtype=fp8
    max_num_seqs=1024
    max_num_batched_tokens=131072
    max_model_len=8192

    vllm bench throughput --model $model \
        -tp $tp \
        --num-prompts $num_prompts \
        --input-len $in \
        --output-len $out \
        --dtype $dtype \
        --kv-cache-dtype $kv_cache_dtype \
        --max-num-seqs $max_num_seqs \
        --max-num-batched-tokens $max_num_batched_tokens \
        --max-model-len $max_model_len \
        --trust-remote-code \
        --output-json ${model}_throughput.json \
        --gpu-memory-utilization 0.9
:::
::::

Serving command

1.  Start the server using the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        model=amd/Llama-3.1-8B-Instruct-FP8-KV
        tp=1
        dtype=auto
        kv_cache_dtype=fp8
        max_num_seqs=256
        max_num_batched_tokens=131072
        max_model_len=8192

        vllm serve $model \
            -tp $tp \
            --dtype $dtype \
            --kv-cache-dtype $kv_cache_dtype \
            --max-num-seqs $max_num_seqs \
            --max-num-batched-tokens $max_num_batched_tokens \
            --max-model-len $max_model_len \
            --no-enable-prefix-caching \
            --swap-space 16 \
            --disable-log-requests \
            --trust-remote-code \
            --gpu-memory-utilization 0.9
    :::
    ::::

    Wait until the model has loaded and the server is ready to accept requests.

2.  On another terminal on the same machine, run the benchmark:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # Connect to the container
        docker exec -it test bash

        # Wait for the server to start
        until curl -s http://localhost:8000/v1/models; do sleep 30; done

        # Run the benchmark
        model=amd/Llama-3.1-8B-Instruct-FP8-KV
        max_concurrency=1
        num_prompts=10
        in=128
        out=128
        vllm bench serve --model $model \
            --percentile-metrics "ttft,tpot,itl,e2el" \
            --dataset-name random \
            --ignore-eos \
            --max-concurrency $max_concurrency \
            --num-prompts $num_prompts \
            --random-input-len $in \
            --random-output-len $out \
            --trust-remote-code \
            --save-result \
            --result-filename ${model}_serving.json
    :::
    ::::

::::: {.admonition .note}
Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B, try adding [`export`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre} to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:::: {.highlight-default .notranslate}
::: highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token
:::
::::
:::::

`<style>
mjx-container[jax="CHTML"][display="true"] {
   text-align: left;
   margin: 0;
}
</style>`{=html}

::: {.admonition .note}
Note

Throughput is calculated as:

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  :::

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  :::
:::
::::::::::::
::::::::::::::
:::::::::::::::

::::::::::::::: {.model-doc .pyt-vllm-llama-3-1-405b .docutils .container}
:::::::::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to Llama 3.1 405B. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  On the host machine, use this command to run the performance benchmark test on the [Llama 3.1 405B](https://huggingface.co/meta-llama/Llama-3.1-405B-Instruct){.reference .external} model using one node with the [`float16`{.docutils .literal .notranslate}]{.pre} data type.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_vllm_llama-3.1-405b \
            --keep-model-dir \
            --live-output
    :::
    ::::

MAD launches a Docker container with the name [`container_ci-pyt_vllm_llama-3.1-405b`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_vllm_llama-3.1-405b_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_vllm_llama-3.1-405b_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-930){.reference .internal} are preconfigured to collect offline throughput and online serving performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
:::

Standalone benchmarking

:::::::::::: {.sd-tab-content .docutils}
The following commands are optimized for Llama 3.1 405B. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

::: {.admonition .seealso}
See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs){.reference .external} in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs){.reference .external} for descriptions of available configuration options and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md){.reference .external} for additional benchmarking information.
:::

Launch the container

You can run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm7.0.0_vllm_0.10.2_20251006/images/sha256-94fd001964e1cf55c3224a445b1fb5be31a7dac302315255db8422d813edd7f5){.reference .external} as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
    docker run -it \
        --device=/dev/kfd \
        --device=/dev/dri \
        --group-add video \
        --shm-size 16G \
        --security-opt seccomp=unconfined \
        --security-opt apparmor=unconfined \
        --cap-add=SYS_PTRACE \
        -v $(pwd):/workspace \
        --env HUGGINGFACE_HUB_CACHE=/workspace \
        --name test \
        rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
:::
::::

Throughput command

Use the following command to start the throughput benchmark.

:::: {.highlight-shell .notranslate}
::: highlight
    model=meta-llama/Llama-3.1-405B-Instruct
    tp=8
    num_prompts=1024
    in=128
    out=128
    dtype=auto
    kv_cache_dtype=auto
    max_num_seqs=1024
    max_num_batched_tokens=131072
    max_model_len=8192

    vllm bench throughput --model $model \
        -tp $tp \
        --num-prompts $num_prompts \
        --input-len $in \
        --output-len $out \
        --dtype $dtype \
        --kv-cache-dtype $kv_cache_dtype \
        --max-num-seqs $max_num_seqs \
        --max-num-batched-tokens $max_num_batched_tokens \
        --max-model-len $max_model_len \
        --trust-remote-code \
        --output-json ${model}_throughput.json \
        --gpu-memory-utilization 0.9
:::
::::

Serving command

1.  Start the server using the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        model=meta-llama/Llama-3.1-405B-Instruct
        tp=8
        dtype=auto
        kv_cache_dtype=auto
        max_num_seqs=256
        max_num_batched_tokens=131072
        max_model_len=8192

        vllm serve $model \
            -tp $tp \
            --dtype $dtype \
            --kv-cache-dtype $kv_cache_dtype \
            --max-num-seqs $max_num_seqs \
            --max-num-batched-tokens $max_num_batched_tokens \
            --max-model-len $max_model_len \
            --no-enable-prefix-caching \
            --swap-space 16 \
            --disable-log-requests \
            --trust-remote-code \
            --gpu-memory-utilization 0.9
    :::
    ::::

    Wait until the model has loaded and the server is ready to accept requests.

2.  On another terminal on the same machine, run the benchmark:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # Connect to the container
        docker exec -it test bash

        # Wait for the server to start
        until curl -s http://localhost:8000/v1/models; do sleep 30; done

        # Run the benchmark
        model=meta-llama/Llama-3.1-405B-Instruct
        max_concurrency=1
        num_prompts=10
        in=128
        out=128
        vllm bench serve --model $model \
            --percentile-metrics "ttft,tpot,itl,e2el" \
            --dataset-name random \
            --ignore-eos \
            --max-concurrency $max_concurrency \
            --num-prompts $num_prompts \
            --random-input-len $in \
            --random-output-len $out \
            --trust-remote-code \
            --save-result \
            --result-filename ${model}_serving.json
    :::
    ::::

::::: {.admonition .note}
Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B, try adding [`export`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre} to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:::: {.highlight-default .notranslate}
::: highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token
:::
::::
:::::

`<style>
mjx-container[jax="CHTML"][display="true"] {
   text-align: left;
   margin: 0;
}
</style>`{=html}

::: {.admonition .note}
Note

Throughput is calculated as:

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  :::

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  :::
:::
::::::::::::
::::::::::::::
:::::::::::::::

::::::::::::::: {.model-doc .pyt-vllm-llama-3-1-405b-fp8 .docutils .container}
:::::::::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to Llama 3.1 405B FP8. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  On the host machine, use this command to run the performance benchmark test on the [Llama 3.1 405B FP8](https://huggingface.co/amd/Llama-3.1-405B-Instruct-FP8-KV){.reference .external} model using one node with the [`float8`{.docutils .literal .notranslate}]{.pre} data type.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_vllm_llama-3.1-405b_fp8 \
            --keep-model-dir \
            --live-output
    :::
    ::::

MAD launches a Docker container with the name [`container_ci-pyt_vllm_llama-3.1-405b_fp8`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_vllm_llama-3.1-405b_fp8_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_vllm_llama-3.1-405b_fp8_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-930){.reference .internal} are preconfigured to collect offline throughput and online serving performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
:::

Standalone benchmarking

:::::::::::: {.sd-tab-content .docutils}
The following commands are optimized for Llama 3.1 405B FP8. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

::: {.admonition .seealso}
See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs){.reference .external} in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs){.reference .external} for descriptions of available configuration options and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md){.reference .external} for additional benchmarking information.
:::

Launch the container

You can run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm7.0.0_vllm_0.10.2_20251006/images/sha256-94fd001964e1cf55c3224a445b1fb5be31a7dac302315255db8422d813edd7f5){.reference .external} as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
    docker run -it \
        --device=/dev/kfd \
        --device=/dev/dri \
        --group-add video \
        --shm-size 16G \
        --security-opt seccomp=unconfined \
        --security-opt apparmor=unconfined \
        --cap-add=SYS_PTRACE \
        -v $(pwd):/workspace \
        --env HUGGINGFACE_HUB_CACHE=/workspace \
        --name test \
        rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
:::
::::

Throughput command

Use the following command to start the throughput benchmark.

:::: {.highlight-shell .notranslate}
::: highlight
    model=amd/Llama-3.1-405B-Instruct-FP8-KV
    tp=8
    num_prompts=1024
    in=128
    out=128
    dtype=auto
    kv_cache_dtype=fp8
    max_num_seqs=1024
    max_num_batched_tokens=131072
    max_model_len=8192

    vllm bench throughput --model $model \
        -tp $tp \
        --num-prompts $num_prompts \
        --input-len $in \
        --output-len $out \
        --dtype $dtype \
        --kv-cache-dtype $kv_cache_dtype \
        --max-num-seqs $max_num_seqs \
        --max-num-batched-tokens $max_num_batched_tokens \
        --max-model-len $max_model_len \
        --trust-remote-code \
        --output-json ${model}_throughput.json \
        --gpu-memory-utilization 0.9
:::
::::

Serving command

1.  Start the server using the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        model=amd/Llama-3.1-405B-Instruct-FP8-KV
        tp=8
        dtype=auto
        kv_cache_dtype=fp8
        max_num_seqs=256
        max_num_batched_tokens=131072
        max_model_len=8192

        vllm serve $model \
            -tp $tp \
            --dtype $dtype \
            --kv-cache-dtype $kv_cache_dtype \
            --max-num-seqs $max_num_seqs \
            --max-num-batched-tokens $max_num_batched_tokens \
            --max-model-len $max_model_len \
            --no-enable-prefix-caching \
            --swap-space 16 \
            --disable-log-requests \
            --trust-remote-code \
            --gpu-memory-utilization 0.9
    :::
    ::::

    Wait until the model has loaded and the server is ready to accept requests.

2.  On another terminal on the same machine, run the benchmark:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # Connect to the container
        docker exec -it test bash

        # Wait for the server to start
        until curl -s http://localhost:8000/v1/models; do sleep 30; done

        # Run the benchmark
        model=amd/Llama-3.1-405B-Instruct-FP8-KV
        max_concurrency=1
        num_prompts=10
        in=128
        out=128
        vllm bench serve --model $model \
            --percentile-metrics "ttft,tpot,itl,e2el" \
            --dataset-name random \
            --ignore-eos \
            --max-concurrency $max_concurrency \
            --num-prompts $num_prompts \
            --random-input-len $in \
            --random-output-len $out \
            --trust-remote-code \
            --save-result \
            --result-filename ${model}_serving.json
    :::
    ::::

::::: {.admonition .note}
Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B, try adding [`export`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre} to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:::: {.highlight-default .notranslate}
::: highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token
:::
::::
:::::

`<style>
mjx-container[jax="CHTML"][display="true"] {
   text-align: left;
   margin: 0;
}
</style>`{=html}

::: {.admonition .note}
Note

Throughput is calculated as:

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  :::

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  :::
:::
::::::::::::
::::::::::::::
:::::::::::::::

::::::::::::::: {.model-doc .pyt-vllm-llama-3-1-405b-fp4 .docutils .container}
:::::::::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to Llama 3.1 405B MXFP4. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  On the host machine, use this command to run the performance benchmark test on the [Llama 3.1 405B MXFP4](https://huggingface.co/amd/Llama-3.1-405B-Instruct-MXFP4-Preview){.reference .external} model using one node with the [`float4`{.docutils .literal .notranslate}]{.pre} data type.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_vllm_llama-3.1-405b_fp4 \
            --keep-model-dir \
            --live-output
    :::
    ::::

MAD launches a Docker container with the name [`container_ci-pyt_vllm_llama-3.1-405b_fp4`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_vllm_llama-3.1-405b_fp4_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_vllm_llama-3.1-405b_fp4_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-930){.reference .internal} are preconfigured to collect offline throughput and online serving performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
:::

Standalone benchmarking

:::::::::::: {.sd-tab-content .docutils}
The following commands are optimized for Llama 3.1 405B MXFP4. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

::: {.admonition .seealso}
See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs){.reference .external} in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs){.reference .external} for descriptions of available configuration options and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md){.reference .external} for additional benchmarking information.
:::

Launch the container

You can run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm7.0.0_vllm_0.10.2_20251006/images/sha256-94fd001964e1cf55c3224a445b1fb5be31a7dac302315255db8422d813edd7f5){.reference .external} as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
    docker run -it \
        --device=/dev/kfd \
        --device=/dev/dri \
        --group-add video \
        --shm-size 16G \
        --security-opt seccomp=unconfined \
        --security-opt apparmor=unconfined \
        --cap-add=SYS_PTRACE \
        -v $(pwd):/workspace \
        --env HUGGINGFACE_HUB_CACHE=/workspace \
        --name test \
        rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
:::
::::

Throughput command

Use the following command to start the throughput benchmark.

:::: {.highlight-shell .notranslate}
::: highlight
    model=amd/Llama-3.1-405B-Instruct-MXFP4-Preview
    tp=8
    num_prompts=1024
    in=128
    out=128
    dtype=auto
    kv_cache_dtype=fp8
    max_num_seqs=1024
    max_num_batched_tokens=131072
    max_model_len=8192

    vllm bench throughput --model $model \
        -tp $tp \
        --num-prompts $num_prompts \
        --input-len $in \
        --output-len $out \
        --dtype $dtype \
        --kv-cache-dtype $kv_cache_dtype \
        --max-num-seqs $max_num_seqs \
        --max-num-batched-tokens $max_num_batched_tokens \
        --max-model-len $max_model_len \
        --trust-remote-code \
        --output-json ${model}_throughput.json \
        --gpu-memory-utilization 0.9
:::
::::

Serving command

1.  Start the server using the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        model=amd/Llama-3.1-405B-Instruct-MXFP4-Preview
        tp=8
        dtype=auto
        kv_cache_dtype=fp8
        max_num_seqs=256
        max_num_batched_tokens=131072
        max_model_len=8192

        vllm serve $model \
            -tp $tp \
            --dtype $dtype \
            --kv-cache-dtype $kv_cache_dtype \
            --max-num-seqs $max_num_seqs \
            --max-num-batched-tokens $max_num_batched_tokens \
            --max-model-len $max_model_len \
            --no-enable-prefix-caching \
            --swap-space 16 \
            --disable-log-requests \
            --trust-remote-code \
            --gpu-memory-utilization 0.9
    :::
    ::::

    Wait until the model has loaded and the server is ready to accept requests.

2.  On another terminal on the same machine, run the benchmark:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # Connect to the container
        docker exec -it test bash

        # Wait for the server to start
        until curl -s http://localhost:8000/v1/models; do sleep 30; done

        # Run the benchmark
        model=amd/Llama-3.1-405B-Instruct-MXFP4-Preview
        max_concurrency=1
        num_prompts=10
        in=128
        out=128
        vllm bench serve --model $model \
            --percentile-metrics "ttft,tpot,itl,e2el" \
            --dataset-name random \
            --ignore-eos \
            --max-concurrency $max_concurrency \
            --num-prompts $num_prompts \
            --random-input-len $in \
            --random-output-len $out \
            --trust-remote-code \
            --save-result \
            --result-filename ${model}_serving.json
    :::
    ::::

::::: {.admonition .note}
Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B, try adding [`export`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre} to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:::: {.highlight-default .notranslate}
::: highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token
:::
::::
:::::

`<style>
mjx-container[jax="CHTML"][display="true"] {
   text-align: left;
   margin: 0;
}
</style>`{=html}

::: {.admonition .note}
Note

Throughput is calculated as:

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  :::

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  :::
:::
::::::::::::
::::::::::::::
:::::::::::::::

::::::::::::::: {.model-doc .pyt-vllm-llama-3-3-70b .docutils .container}
:::::::::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to Llama 3.3 70B. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  On the host machine, use this command to run the performance benchmark test on the [Llama 3.3 70B](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct){.reference .external} model using one node with the [`float16`{.docutils .literal .notranslate}]{.pre} data type.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_vllm_llama-3.3-70b \
            --keep-model-dir \
            --live-output
    :::
    ::::

MAD launches a Docker container with the name [`container_ci-pyt_vllm_llama-3.3-70b`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_vllm_llama-3.3-70b_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_vllm_llama-3.3-70b_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-930){.reference .internal} are preconfigured to collect offline throughput and online serving performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
:::

Standalone benchmarking

:::::::::::: {.sd-tab-content .docutils}
The following commands are optimized for Llama 3.3 70B. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

::: {.admonition .seealso}
See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs){.reference .external} in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs){.reference .external} for descriptions of available configuration options and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md){.reference .external} for additional benchmarking information.
:::

Launch the container

You can run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm7.0.0_vllm_0.10.2_20251006/images/sha256-94fd001964e1cf55c3224a445b1fb5be31a7dac302315255db8422d813edd7f5){.reference .external} as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
    docker run -it \
        --device=/dev/kfd \
        --device=/dev/dri \
        --group-add video \
        --shm-size 16G \
        --security-opt seccomp=unconfined \
        --security-opt apparmor=unconfined \
        --cap-add=SYS_PTRACE \
        -v $(pwd):/workspace \
        --env HUGGINGFACE_HUB_CACHE=/workspace \
        --name test \
        rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
:::
::::

Throughput command

Use the following command to start the throughput benchmark.

:::: {.highlight-shell .notranslate}
::: highlight
    model=meta-llama/Llama-3.3-70B-Instruct
    tp=8
    num_prompts=1024
    in=128
    out=128
    dtype=auto
    kv_cache_dtype=auto
    max_num_seqs=1024
    max_num_batched_tokens=131072
    max_model_len=8192

    vllm bench throughput --model $model \
        -tp $tp \
        --num-prompts $num_prompts \
        --input-len $in \
        --output-len $out \
        --dtype $dtype \
        --kv-cache-dtype $kv_cache_dtype \
        --max-num-seqs $max_num_seqs \
        --max-num-batched-tokens $max_num_batched_tokens \
        --max-model-len $max_model_len \
        --trust-remote-code \
        --output-json ${model}_throughput.json \
        --gpu-memory-utilization 0.9
:::
::::

Serving command

1.  Start the server using the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        model=meta-llama/Llama-3.3-70B-Instruct
        tp=8
        dtype=auto
        kv_cache_dtype=auto
        max_num_seqs=256
        max_num_batched_tokens=131072
        max_model_len=8192

        vllm serve $model \
            -tp $tp \
            --dtype $dtype \
            --kv-cache-dtype $kv_cache_dtype \
            --max-num-seqs $max_num_seqs \
            --max-num-batched-tokens $max_num_batched_tokens \
            --max-model-len $max_model_len \
            --no-enable-prefix-caching \
            --swap-space 16 \
            --disable-log-requests \
            --trust-remote-code \
            --gpu-memory-utilization 0.9
    :::
    ::::

    Wait until the model has loaded and the server is ready to accept requests.

2.  On another terminal on the same machine, run the benchmark:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # Connect to the container
        docker exec -it test bash

        # Wait for the server to start
        until curl -s http://localhost:8000/v1/models; do sleep 30; done

        # Run the benchmark
        model=meta-llama/Llama-3.3-70B-Instruct
        max_concurrency=1
        num_prompts=10
        in=128
        out=128
        vllm bench serve --model $model \
            --percentile-metrics "ttft,tpot,itl,e2el" \
            --dataset-name random \
            --ignore-eos \
            --max-concurrency $max_concurrency \
            --num-prompts $num_prompts \
            --random-input-len $in \
            --random-output-len $out \
            --trust-remote-code \
            --save-result \
            --result-filename ${model}_serving.json
    :::
    ::::

::::: {.admonition .note}
Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B, try adding [`export`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre} to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:::: {.highlight-default .notranslate}
::: highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token
:::
::::
:::::

`<style>
mjx-container[jax="CHTML"][display="true"] {
   text-align: left;
   margin: 0;
}
</style>`{=html}

::: {.admonition .note}
Note

Throughput is calculated as:

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  :::

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  :::
:::
::::::::::::
::::::::::::::
:::::::::::::::

::::::::::::::: {.model-doc .pyt-vllm-llama-3-3-70b-fp8 .docutils .container}
:::::::::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to Llama 3.3 70B FP8. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  On the host machine, use this command to run the performance benchmark test on the [Llama 3.3 70B FP8](https://huggingface.co/amd/Llama-3.3-70B-Instruct-FP8-KV){.reference .external} model using one node with the [`float8`{.docutils .literal .notranslate}]{.pre} data type.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_vllm_llama-3.3-70b_fp8 \
            --keep-model-dir \
            --live-output
    :::
    ::::

MAD launches a Docker container with the name [`container_ci-pyt_vllm_llama-3.3-70b_fp8`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_vllm_llama-3.3-70b_fp8_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_vllm_llama-3.3-70b_fp8_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-930){.reference .internal} are preconfigured to collect offline throughput and online serving performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
:::

Standalone benchmarking

:::::::::::: {.sd-tab-content .docutils}
The following commands are optimized for Llama 3.3 70B FP8. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

::: {.admonition .seealso}
See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs){.reference .external} in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs){.reference .external} for descriptions of available configuration options and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md){.reference .external} for additional benchmarking information.
:::

Launch the container

You can run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm7.0.0_vllm_0.10.2_20251006/images/sha256-94fd001964e1cf55c3224a445b1fb5be31a7dac302315255db8422d813edd7f5){.reference .external} as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
    docker run -it \
        --device=/dev/kfd \
        --device=/dev/dri \
        --group-add video \
        --shm-size 16G \
        --security-opt seccomp=unconfined \
        --security-opt apparmor=unconfined \
        --cap-add=SYS_PTRACE \
        -v $(pwd):/workspace \
        --env HUGGINGFACE_HUB_CACHE=/workspace \
        --name test \
        rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
:::
::::

Throughput command

Use the following command to start the throughput benchmark.

:::: {.highlight-shell .notranslate}
::: highlight
    model=amd/Llama-3.3-70B-Instruct-FP8-KV
    tp=8
    num_prompts=1024
    in=128
    out=128
    dtype=auto
    kv_cache_dtype=fp8
    max_num_seqs=1024
    max_num_batched_tokens=131072
    max_model_len=8192

    vllm bench throughput --model $model \
        -tp $tp \
        --num-prompts $num_prompts \
        --input-len $in \
        --output-len $out \
        --dtype $dtype \
        --kv-cache-dtype $kv_cache_dtype \
        --max-num-seqs $max_num_seqs \
        --max-num-batched-tokens $max_num_batched_tokens \
        --max-model-len $max_model_len \
        --trust-remote-code \
        --output-json ${model}_throughput.json \
        --gpu-memory-utilization 0.9
:::
::::

Serving command

1.  Start the server using the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        model=amd/Llama-3.3-70B-Instruct-FP8-KV
        tp=8
        dtype=auto
        kv_cache_dtype=fp8
        max_num_seqs=256
        max_num_batched_tokens=131072
        max_model_len=8192

        vllm serve $model \
            -tp $tp \
            --dtype $dtype \
            --kv-cache-dtype $kv_cache_dtype \
            --max-num-seqs $max_num_seqs \
            --max-num-batched-tokens $max_num_batched_tokens \
            --max-model-len $max_model_len \
            --no-enable-prefix-caching \
            --swap-space 16 \
            --disable-log-requests \
            --trust-remote-code \
            --gpu-memory-utilization 0.9
    :::
    ::::

    Wait until the model has loaded and the server is ready to accept requests.

2.  On another terminal on the same machine, run the benchmark:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # Connect to the container
        docker exec -it test bash

        # Wait for the server to start
        until curl -s http://localhost:8000/v1/models; do sleep 30; done

        # Run the benchmark
        model=amd/Llama-3.3-70B-Instruct-FP8-KV
        max_concurrency=1
        num_prompts=10
        in=128
        out=128
        vllm bench serve --model $model \
            --percentile-metrics "ttft,tpot,itl,e2el" \
            --dataset-name random \
            --ignore-eos \
            --max-concurrency $max_concurrency \
            --num-prompts $num_prompts \
            --random-input-len $in \
            --random-output-len $out \
            --trust-remote-code \
            --save-result \
            --result-filename ${model}_serving.json
    :::
    ::::

::::: {.admonition .note}
Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B, try adding [`export`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre} to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:::: {.highlight-default .notranslate}
::: highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token
:::
::::
:::::

`<style>
mjx-container[jax="CHTML"][display="true"] {
   text-align: left;
   margin: 0;
}
</style>`{=html}

::: {.admonition .note}
Note

Throughput is calculated as:

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  :::

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  :::
:::
::::::::::::
::::::::::::::
:::::::::::::::

::::::::::::::: {.model-doc .pyt-vllm-llama-3-3-70b-fp4 .docutils .container}
:::::::::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to Llama 3.3 70B MXFP4. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  On the host machine, use this command to run the performance benchmark test on the [Llama 3.3 70B MXFP4](https://huggingface.co/amd/Llama-3.3-70B-Instruct-MXFP4-Preview){.reference .external} model using one node with the [`float4`{.docutils .literal .notranslate}]{.pre} data type.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_vllm_llama-3.3-70b_fp4 \
            --keep-model-dir \
            --live-output
    :::
    ::::

MAD launches a Docker container with the name [`container_ci-pyt_vllm_llama-3.3-70b_fp4`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_vllm_llama-3.3-70b_fp4_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_vllm_llama-3.3-70b_fp4_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-930){.reference .internal} are preconfigured to collect offline throughput and online serving performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
:::

Standalone benchmarking

:::::::::::: {.sd-tab-content .docutils}
The following commands are optimized for Llama 3.3 70B MXFP4. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

::: {.admonition .seealso}
See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs){.reference .external} in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs){.reference .external} for descriptions of available configuration options and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md){.reference .external} for additional benchmarking information.
:::

Launch the container

You can run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm7.0.0_vllm_0.10.2_20251006/images/sha256-94fd001964e1cf55c3224a445b1fb5be31a7dac302315255db8422d813edd7f5){.reference .external} as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
    docker run -it \
        --device=/dev/kfd \
        --device=/dev/dri \
        --group-add video \
        --shm-size 16G \
        --security-opt seccomp=unconfined \
        --security-opt apparmor=unconfined \
        --cap-add=SYS_PTRACE \
        -v $(pwd):/workspace \
        --env HUGGINGFACE_HUB_CACHE=/workspace \
        --name test \
        rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
:::
::::

Throughput command

Use the following command to start the throughput benchmark.

:::: {.highlight-shell .notranslate}
::: highlight
    model=amd/Llama-3.3-70B-Instruct-MXFP4-Preview
    tp=8
    num_prompts=1024
    in=128
    out=128
    dtype=auto
    kv_cache_dtype=fp8
    max_num_seqs=1024
    max_num_batched_tokens=131072
    max_model_len=8192

    vllm bench throughput --model $model \
        -tp $tp \
        --num-prompts $num_prompts \
        --input-len $in \
        --output-len $out \
        --dtype $dtype \
        --kv-cache-dtype $kv_cache_dtype \
        --max-num-seqs $max_num_seqs \
        --max-num-batched-tokens $max_num_batched_tokens \
        --max-model-len $max_model_len \
        --trust-remote-code \
        --output-json ${model}_throughput.json \
        --gpu-memory-utilization 0.9
:::
::::

Serving command

1.  Start the server using the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        model=amd/Llama-3.3-70B-Instruct-MXFP4-Preview
        tp=8
        dtype=auto
        kv_cache_dtype=fp8
        max_num_seqs=256
        max_num_batched_tokens=131072
        max_model_len=8192

        vllm serve $model \
            -tp $tp \
            --dtype $dtype \
            --kv-cache-dtype $kv_cache_dtype \
            --max-num-seqs $max_num_seqs \
            --max-num-batched-tokens $max_num_batched_tokens \
            --max-model-len $max_model_len \
            --no-enable-prefix-caching \
            --swap-space 16 \
            --disable-log-requests \
            --trust-remote-code \
            --gpu-memory-utilization 0.9
    :::
    ::::

    Wait until the model has loaded and the server is ready to accept requests.

2.  On another terminal on the same machine, run the benchmark:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # Connect to the container
        docker exec -it test bash

        # Wait for the server to start
        until curl -s http://localhost:8000/v1/models; do sleep 30; done

        # Run the benchmark
        model=amd/Llama-3.3-70B-Instruct-MXFP4-Preview
        max_concurrency=1
        num_prompts=10
        in=128
        out=128
        vllm bench serve --model $model \
            --percentile-metrics "ttft,tpot,itl,e2el" \
            --dataset-name random \
            --ignore-eos \
            --max-concurrency $max_concurrency \
            --num-prompts $num_prompts \
            --random-input-len $in \
            --random-output-len $out \
            --trust-remote-code \
            --save-result \
            --result-filename ${model}_serving.json
    :::
    ::::

::::: {.admonition .note}
Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B, try adding [`export`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre} to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:::: {.highlight-default .notranslate}
::: highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token
:::
::::
:::::

`<style>
mjx-container[jax="CHTML"][display="true"] {
   text-align: left;
   margin: 0;
}
</style>`{=html}

::: {.admonition .note}
Note

Throughput is calculated as:

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  :::

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  :::
:::
::::::::::::
::::::::::::::
:::::::::::::::

::::::::::::::: {.model-doc .pyt-vllm-llama-4-scout-17b-16e .docutils .container}
:::::::::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to Llama 4 Scout 17Bx16E. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  On the host machine, use this command to run the performance benchmark test on the [Llama 4 Scout 17Bx16E](https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct){.reference .external} model using one node with the [`float16`{.docutils .literal .notranslate}]{.pre} data type.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_vllm_llama-4-scout-17b-16e \
            --keep-model-dir \
            --live-output
    :::
    ::::

MAD launches a Docker container with the name [`container_ci-pyt_vllm_llama-4-scout-17b-16e`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_vllm_llama-4-scout-17b-16e_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_vllm_llama-4-scout-17b-16e_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-930){.reference .internal} are preconfigured to collect offline throughput and online serving performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
:::

Standalone benchmarking

:::::::::::: {.sd-tab-content .docutils}
The following commands are optimized for Llama 4 Scout 17Bx16E. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

::: {.admonition .seealso}
See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs){.reference .external} in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs){.reference .external} for descriptions of available configuration options and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md){.reference .external} for additional benchmarking information.
:::

Launch the container

You can run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm7.0.0_vllm_0.10.2_20251006/images/sha256-94fd001964e1cf55c3224a445b1fb5be31a7dac302315255db8422d813edd7f5){.reference .external} as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
    docker run -it \
        --device=/dev/kfd \
        --device=/dev/dri \
        --group-add video \
        --shm-size 16G \
        --security-opt seccomp=unconfined \
        --security-opt apparmor=unconfined \
        --cap-add=SYS_PTRACE \
        -v $(pwd):/workspace \
        --env HUGGINGFACE_HUB_CACHE=/workspace \
        --name test \
        rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
:::
::::

Throughput command

Use the following command to start the throughput benchmark.

:::: {.highlight-shell .notranslate}
::: highlight
    model=meta-llama/Llama-4-Scout-17B-16E-Instruct
    tp=8
    num_prompts=1024
    in=128
    out=128
    dtype=auto
    kv_cache_dtype=auto
    max_num_seqs=1024
    max_num_batched_tokens=32768
    max_model_len=8192

    vllm bench throughput --model $model \
        -tp $tp \
        --num-prompts $num_prompts \
        --input-len $in \
        --output-len $out \
        --dtype $dtype \
        --kv-cache-dtype $kv_cache_dtype \
        --max-num-seqs $max_num_seqs \
        --max-num-batched-tokens $max_num_batched_tokens \
        --max-model-len $max_model_len \
        --trust-remote-code \
        --output-json ${model}_throughput.json \
        --gpu-memory-utilization 0.9
:::
::::

Serving command

1.  Start the server using the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        model=meta-llama/Llama-4-Scout-17B-16E-Instruct
        tp=8
        dtype=auto
        kv_cache_dtype=auto
        max_num_seqs=256
        max_num_batched_tokens=32768
        max_model_len=8192

        vllm serve $model \
            -tp $tp \
            --dtype $dtype \
            --kv-cache-dtype $kv_cache_dtype \
            --max-num-seqs $max_num_seqs \
            --max-num-batched-tokens $max_num_batched_tokens \
            --max-model-len $max_model_len \
            --no-enable-prefix-caching \
            --swap-space 16 \
            --disable-log-requests \
            --trust-remote-code \
            --gpu-memory-utilization 0.9
    :::
    ::::

    Wait until the model has loaded and the server is ready to accept requests.

2.  On another terminal on the same machine, run the benchmark:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # Connect to the container
        docker exec -it test bash

        # Wait for the server to start
        until curl -s http://localhost:8000/v1/models; do sleep 30; done

        # Run the benchmark
        model=meta-llama/Llama-4-Scout-17B-16E-Instruct
        max_concurrency=1
        num_prompts=10
        in=128
        out=128
        vllm bench serve --model $model \
            --percentile-metrics "ttft,tpot,itl,e2el" \
            --dataset-name random \
            --ignore-eos \
            --max-concurrency $max_concurrency \
            --num-prompts $num_prompts \
            --random-input-len $in \
            --random-output-len $out \
            --trust-remote-code \
            --save-result \
            --result-filename ${model}_serving.json
    :::
    ::::

::::: {.admonition .note}
Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B, try adding [`export`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre} to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:::: {.highlight-default .notranslate}
::: highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token
:::
::::
:::::

`<style>
mjx-container[jax="CHTML"][display="true"] {
   text-align: left;
   margin: 0;
}
</style>`{=html}

::: {.admonition .note}
Note

Throughput is calculated as:

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  :::

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  :::
:::
::::::::::::
::::::::::::::
:::::::::::::::

::::::::::::::: {.model-doc .pyt-vllm-llama-4-maverick-17b-128e .docutils .container}
:::::::::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to Llama 4 Maverick 17Bx128E. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  On the host machine, use this command to run the performance benchmark test on the [Llama 4 Maverick 17Bx128E](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct){.reference .external} model using one node with the [`float16`{.docutils .literal .notranslate}]{.pre} data type.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_vllm_llama-4-maverick-17b-128e \
            --keep-model-dir \
            --live-output
    :::
    ::::

MAD launches a Docker container with the name [`container_ci-pyt_vllm_llama-4-maverick-17b-128e`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_vllm_llama-4-maverick-17b-128e_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_vllm_llama-4-maverick-17b-128e_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-930){.reference .internal} are preconfigured to collect offline throughput and online serving performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
:::

Standalone benchmarking

:::::::::::: {.sd-tab-content .docutils}
The following commands are optimized for Llama 4 Maverick 17Bx128E. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

::: {.admonition .seealso}
See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs){.reference .external} in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs){.reference .external} for descriptions of available configuration options and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md){.reference .external} for additional benchmarking information.
:::

Launch the container

You can run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm7.0.0_vllm_0.10.2_20251006/images/sha256-94fd001964e1cf55c3224a445b1fb5be31a7dac302315255db8422d813edd7f5){.reference .external} as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
    docker run -it \
        --device=/dev/kfd \
        --device=/dev/dri \
        --group-add video \
        --shm-size 16G \
        --security-opt seccomp=unconfined \
        --security-opt apparmor=unconfined \
        --cap-add=SYS_PTRACE \
        -v $(pwd):/workspace \
        --env HUGGINGFACE_HUB_CACHE=/workspace \
        --name test \
        rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
:::
::::

Throughput command

Use the following command to start the throughput benchmark.

:::: {.highlight-shell .notranslate}
::: highlight
    model=meta-llama/Llama-4-Maverick-17B-128E-Instruct
    tp=8
    num_prompts=1024
    in=128
    out=128
    dtype=auto
    kv_cache_dtype=auto
    max_num_seqs=1024
    max_num_batched_tokens=32768
    max_model_len=8192

    vllm bench throughput --model $model \
        -tp $tp \
        --num-prompts $num_prompts \
        --input-len $in \
        --output-len $out \
        --dtype $dtype \
        --kv-cache-dtype $kv_cache_dtype \
        --max-num-seqs $max_num_seqs \
        --max-num-batched-tokens $max_num_batched_tokens \
        --max-model-len $max_model_len \
        --trust-remote-code \
        --output-json ${model}_throughput.json \
        --gpu-memory-utilization 0.9
:::
::::

Serving command

1.  Start the server using the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        model=meta-llama/Llama-4-Maverick-17B-128E-Instruct
        tp=8
        dtype=auto
        kv_cache_dtype=auto
        max_num_seqs=256
        max_num_batched_tokens=32768
        max_model_len=8192

        vllm serve $model \
            -tp $tp \
            --dtype $dtype \
            --kv-cache-dtype $kv_cache_dtype \
            --max-num-seqs $max_num_seqs \
            --max-num-batched-tokens $max_num_batched_tokens \
            --max-model-len $max_model_len \
            --no-enable-prefix-caching \
            --swap-space 16 \
            --disable-log-requests \
            --trust-remote-code \
            --gpu-memory-utilization 0.9
    :::
    ::::

    Wait until the model has loaded and the server is ready to accept requests.

2.  On another terminal on the same machine, run the benchmark:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # Connect to the container
        docker exec -it test bash

        # Wait for the server to start
        until curl -s http://localhost:8000/v1/models; do sleep 30; done

        # Run the benchmark
        model=meta-llama/Llama-4-Maverick-17B-128E-Instruct
        max_concurrency=1
        num_prompts=10
        in=128
        out=128
        vllm bench serve --model $model \
            --percentile-metrics "ttft,tpot,itl,e2el" \
            --dataset-name random \
            --ignore-eos \
            --max-concurrency $max_concurrency \
            --num-prompts $num_prompts \
            --random-input-len $in \
            --random-output-len $out \
            --trust-remote-code \
            --save-result \
            --result-filename ${model}_serving.json
    :::
    ::::

::::: {.admonition .note}
Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B, try adding [`export`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre} to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:::: {.highlight-default .notranslate}
::: highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token
:::
::::
:::::

`<style>
mjx-container[jax="CHTML"][display="true"] {
   text-align: left;
   margin: 0;
}
</style>`{=html}

::: {.admonition .note}
Note

Throughput is calculated as:

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  :::

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  :::
:::
::::::::::::
::::::::::::::
:::::::::::::::

::::::::::::::: {.model-doc .pyt-vllm-llama-4-maverick-17b-128e-fp8 .docutils .container}
:::::::::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to Llama 4 Maverick 17Bx128E FP8. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  On the host machine, use this command to run the performance benchmark test on the [Llama 4 Maverick 17Bx128E FP8](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8){.reference .external} model using one node with the [`float8`{.docutils .literal .notranslate}]{.pre} data type.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_vllm_llama-4-maverick-17b-128e_fp8 \
            --keep-model-dir \
            --live-output
    :::
    ::::

MAD launches a Docker container with the name [`container_ci-pyt_vllm_llama-4-maverick-17b-128e_fp8`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_vllm_llama-4-maverick-17b-128e_fp8_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_vllm_llama-4-maverick-17b-128e_fp8_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-930){.reference .internal} are preconfigured to collect offline throughput and online serving performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
:::

Standalone benchmarking

:::::::::::: {.sd-tab-content .docutils}
The following commands are optimized for Llama 4 Maverick 17Bx128E FP8. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

::: {.admonition .seealso}
See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs){.reference .external} in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs){.reference .external} for descriptions of available configuration options and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md){.reference .external} for additional benchmarking information.
:::

Launch the container

You can run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm7.0.0_vllm_0.10.2_20251006/images/sha256-94fd001964e1cf55c3224a445b1fb5be31a7dac302315255db8422d813edd7f5){.reference .external} as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
    docker run -it \
        --device=/dev/kfd \
        --device=/dev/dri \
        --group-add video \
        --shm-size 16G \
        --security-opt seccomp=unconfined \
        --security-opt apparmor=unconfined \
        --cap-add=SYS_PTRACE \
        -v $(pwd):/workspace \
        --env HUGGINGFACE_HUB_CACHE=/workspace \
        --name test \
        rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
:::
::::

Throughput command

Use the following command to start the throughput benchmark.

:::: {.highlight-shell .notranslate}
::: highlight
    model=meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8
    tp=8
    num_prompts=1024
    in=128
    out=128
    dtype=auto
    kv_cache_dtype=fp8
    max_num_seqs=1024
    max_num_batched_tokens=131072
    max_model_len=8192

    vllm bench throughput --model $model \
        -tp $tp \
        --num-prompts $num_prompts \
        --input-len $in \
        --output-len $out \
        --dtype $dtype \
        --kv-cache-dtype $kv_cache_dtype \
        --max-num-seqs $max_num_seqs \
        --max-num-batched-tokens $max_num_batched_tokens \
        --max-model-len $max_model_len \
        --trust-remote-code \
        --output-json ${model}_throughput.json \
        --gpu-memory-utilization 0.9
:::
::::

Serving command

1.  Start the server using the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        model=meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8
        tp=8
        dtype=auto
        kv_cache_dtype=fp8
        max_num_seqs=256
        max_num_batched_tokens=131072
        max_model_len=8192

        vllm serve $model \
            -tp $tp \
            --dtype $dtype \
            --kv-cache-dtype $kv_cache_dtype \
            --max-num-seqs $max_num_seqs \
            --max-num-batched-tokens $max_num_batched_tokens \
            --max-model-len $max_model_len \
            --no-enable-prefix-caching \
            --swap-space 16 \
            --disable-log-requests \
            --trust-remote-code \
            --gpu-memory-utilization 0.9
    :::
    ::::

    Wait until the model has loaded and the server is ready to accept requests.

2.  On another terminal on the same machine, run the benchmark:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # Connect to the container
        docker exec -it test bash

        # Wait for the server to start
        until curl -s http://localhost:8000/v1/models; do sleep 30; done

        # Run the benchmark
        model=meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8
        max_concurrency=1
        num_prompts=10
        in=128
        out=128
        vllm bench serve --model $model \
            --percentile-metrics "ttft,tpot,itl,e2el" \
            --dataset-name random \
            --ignore-eos \
            --max-concurrency $max_concurrency \
            --num-prompts $num_prompts \
            --random-input-len $in \
            --random-output-len $out \
            --trust-remote-code \
            --save-result \
            --result-filename ${model}_serving.json
    :::
    ::::

::::: {.admonition .note}
Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B, try adding [`export`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre} to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:::: {.highlight-default .notranslate}
::: highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token
:::
::::
:::::

`<style>
mjx-container[jax="CHTML"][display="true"] {
   text-align: left;
   margin: 0;
}
</style>`{=html}

::: {.admonition .note}
Note

Throughput is calculated as:

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  :::

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  :::
:::
::::::::::::
::::::::::::::
:::::::::::::::

::::::::::::::: {.model-doc .pyt-vllm-deepseek-r1 .docutils .container}
:::::::::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to DeepSeek R1 0528 FP8. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  On the host machine, use this command to run the performance benchmark test on the [DeepSeek R1 0528 FP8](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528){.reference .external} model using one node with the [`float8`{.docutils .literal .notranslate}]{.pre} data type.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_vllm_deepseek-r1 \
            --keep-model-dir \
            --live-output
    :::
    ::::

MAD launches a Docker container with the name [`container_ci-pyt_vllm_deepseek-r1`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_vllm_deepseek-r1_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_vllm_deepseek-r1_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-930){.reference .internal} are preconfigured to collect offline throughput and online serving performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
:::

Standalone benchmarking

:::::::::::: {.sd-tab-content .docutils}
The following commands are optimized for DeepSeek R1 0528 FP8. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

::: {.admonition .seealso}
See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs){.reference .external} in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs){.reference .external} for descriptions of available configuration options and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md){.reference .external} for additional benchmarking information.
:::

Launch the container

You can run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm7.0.0_vllm_0.10.2_20251006/images/sha256-94fd001964e1cf55c3224a445b1fb5be31a7dac302315255db8422d813edd7f5){.reference .external} as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
    docker run -it \
        --device=/dev/kfd \
        --device=/dev/dri \
        --group-add video \
        --shm-size 16G \
        --security-opt seccomp=unconfined \
        --security-opt apparmor=unconfined \
        --cap-add=SYS_PTRACE \
        -v $(pwd):/workspace \
        --env HUGGINGFACE_HUB_CACHE=/workspace \
        --name test \
        rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
:::
::::

Throughput command

Use the following command to start the throughput benchmark.

:::: {.highlight-shell .notranslate}
::: highlight
    model=deepseek-ai/DeepSeek-R1-0528
    tp=8
    num_prompts=1024
    in=128
    out=128
    dtype=auto
    kv_cache_dtype=fp8
    max_num_seqs=1024
    max_num_batched_tokens=131072
    max_model_len=8192

    vllm bench throughput --model $model \
        -tp $tp \
        --num-prompts $num_prompts \
        --input-len $in \
        --output-len $out \
        --dtype $dtype \
        --kv-cache-dtype $kv_cache_dtype \
        --max-num-seqs $max_num_seqs \
        --max-num-batched-tokens $max_num_batched_tokens \
        --max-model-len $max_model_len \
        --trust-remote-code \
        --output-json ${model}_throughput.json \
        --gpu-memory-utilization 0.9
:::
::::

Serving command

1.  Start the server using the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        model=deepseek-ai/DeepSeek-R1-0528
        tp=8
        dtype=auto
        kv_cache_dtype=fp8
        max_num_seqs=256
        max_num_batched_tokens=131072
        max_model_len=8192

        vllm serve $model \
            -tp $tp \
            --dtype $dtype \
            --kv-cache-dtype $kv_cache_dtype \
            --max-num-seqs $max_num_seqs \
            --max-num-batched-tokens $max_num_batched_tokens \
            --max-model-len $max_model_len \
            --no-enable-prefix-caching \
            --swap-space 16 \
            --disable-log-requests \
            --trust-remote-code \
            --gpu-memory-utilization 0.9
    :::
    ::::

    Wait until the model has loaded and the server is ready to accept requests.

2.  On another terminal on the same machine, run the benchmark:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # Connect to the container
        docker exec -it test bash

        # Wait for the server to start
        until curl -s http://localhost:8000/v1/models; do sleep 30; done

        # Run the benchmark
        model=deepseek-ai/DeepSeek-R1-0528
        max_concurrency=1
        num_prompts=10
        in=128
        out=128
        vllm bench serve --model $model \
            --percentile-metrics "ttft,tpot,itl,e2el" \
            --dataset-name random \
            --ignore-eos \
            --max-concurrency $max_concurrency \
            --num-prompts $num_prompts \
            --random-input-len $in \
            --random-output-len $out \
            --trust-remote-code \
            --save-result \
            --result-filename ${model}_serving.json
    :::
    ::::

::::: {.admonition .note}
Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B, try adding [`export`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre} to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:::: {.highlight-default .notranslate}
::: highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token
:::
::::
:::::

`<style>
mjx-container[jax="CHTML"][display="true"] {
   text-align: left;
   margin: 0;
}
</style>`{=html}

::: {.admonition .note}
Note

Throughput is calculated as:

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  :::

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  :::
:::
::::::::::::
::::::::::::::
:::::::::::::::

::::::::::::::: {.model-doc .pyt-vllm-gpt-oss-20b .docutils .container}
:::::::::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to GPT OSS 20B. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  On the host machine, use this command to run the performance benchmark test on the [GPT OSS 20B](https://huggingface.co/openai/gpt-oss-20b){.reference .external} model using one node with the [`bfloat16`{.docutils .literal .notranslate}]{.pre} data type.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_vllm_gpt-oss-20b \
            --keep-model-dir \
            --live-output
    :::
    ::::

MAD launches a Docker container with the name [`container_ci-pyt_vllm_gpt-oss-20b`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_vllm_gpt-oss-20b_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_vllm_gpt-oss-20b_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-930){.reference .internal} are preconfigured to collect offline throughput and online serving performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
:::

Standalone benchmarking

:::::::::::: {.sd-tab-content .docutils}
The following commands are optimized for GPT OSS 20B. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

::: {.admonition .seealso}
See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs){.reference .external} in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs){.reference .external} for descriptions of available configuration options and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md){.reference .external} for additional benchmarking information.
:::

Launch the container

You can run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm7.0.0_vllm_0.10.2_20251006/images/sha256-94fd001964e1cf55c3224a445b1fb5be31a7dac302315255db8422d813edd7f5){.reference .external} as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
    docker run -it \
        --device=/dev/kfd \
        --device=/dev/dri \
        --group-add video \
        --shm-size 16G \
        --security-opt seccomp=unconfined \
        --security-opt apparmor=unconfined \
        --cap-add=SYS_PTRACE \
        -v $(pwd):/workspace \
        --env HUGGINGFACE_HUB_CACHE=/workspace \
        --name test \
        rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
:::
::::

Throughput command

Use the following command to start the throughput benchmark.

:::: {.highlight-shell .notranslate}
::: highlight
    model=openai/gpt-oss-20b
    tp=1
    num_prompts=1024
    in=128
    out=128
    dtype=auto
    kv_cache_dtype=auto
    max_num_seqs=1024
    max_num_batched_tokens=8192
    max_model_len=8192

    vllm bench throughput --model $model \
        -tp $tp \
        --num-prompts $num_prompts \
        --input-len $in \
        --output-len $out \
        --dtype $dtype \
        --kv-cache-dtype $kv_cache_dtype \
        --max-num-seqs $max_num_seqs \
        --max-num-batched-tokens $max_num_batched_tokens \
        --max-model-len $max_model_len \
        --trust-remote-code \
        --output-json ${model}_throughput.json \
        --gpu-memory-utilization 0.9
:::
::::

Serving command

1.  Start the server using the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        model=openai/gpt-oss-20b
        tp=1
        dtype=auto
        kv_cache_dtype=auto
        max_num_seqs=256
        max_num_batched_tokens=8192
        max_model_len=8192

        vllm serve $model \
            -tp $tp \
            --dtype $dtype \
            --kv-cache-dtype $kv_cache_dtype \
            --max-num-seqs $max_num_seqs \
            --max-num-batched-tokens $max_num_batched_tokens \
            --max-model-len $max_model_len \
            --no-enable-prefix-caching \
            --swap-space 16 \
            --disable-log-requests \
            --trust-remote-code \
            --gpu-memory-utilization 0.9
    :::
    ::::

    Wait until the model has loaded and the server is ready to accept requests.

2.  On another terminal on the same machine, run the benchmark:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # Connect to the container
        docker exec -it test bash

        # Wait for the server to start
        until curl -s http://localhost:8000/v1/models; do sleep 30; done

        # Run the benchmark
        model=openai/gpt-oss-20b
        max_concurrency=1
        num_prompts=10
        in=128
        out=128
        vllm bench serve --model $model \
            --percentile-metrics "ttft,tpot,itl,e2el" \
            --dataset-name random \
            --ignore-eos \
            --max-concurrency $max_concurrency \
            --num-prompts $num_prompts \
            --random-input-len $in \
            --random-output-len $out \
            --trust-remote-code \
            --save-result \
            --result-filename ${model}_serving.json
    :::
    ::::

::::: {.admonition .note}
Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B, try adding [`export`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre} to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:::: {.highlight-default .notranslate}
::: highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token
:::
::::
:::::

`<style>
mjx-container[jax="CHTML"][display="true"] {
   text-align: left;
   margin: 0;
}
</style>`{=html}

::: {.admonition .note}
Note

Throughput is calculated as:

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  :::

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  :::
:::
::::::::::::
::::::::::::::
:::::::::::::::

::::::::::::::: {.model-doc .pyt-vllm-gpt-oss-120b .docutils .container}
:::::::::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to GPT OSS 120B. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  On the host machine, use this command to run the performance benchmark test on the [GPT OSS 120B](https://huggingface.co/openai/gpt-oss-120b){.reference .external} model using one node with the [`bfloat16`{.docutils .literal .notranslate}]{.pre} data type.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_vllm_gpt-oss-120b \
            --keep-model-dir \
            --live-output
    :::
    ::::

MAD launches a Docker container with the name [`container_ci-pyt_vllm_gpt-oss-120b`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_vllm_gpt-oss-120b_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_vllm_gpt-oss-120b_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-930){.reference .internal} are preconfigured to collect offline throughput and online serving performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
:::

Standalone benchmarking

:::::::::::: {.sd-tab-content .docutils}
The following commands are optimized for GPT OSS 120B. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

::: {.admonition .seealso}
See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs){.reference .external} in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs){.reference .external} for descriptions of available configuration options and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md){.reference .external} for additional benchmarking information.
:::

Launch the container

You can run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm7.0.0_vllm_0.10.2_20251006/images/sha256-94fd001964e1cf55c3224a445b1fb5be31a7dac302315255db8422d813edd7f5){.reference .external} as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
    docker run -it \
        --device=/dev/kfd \
        --device=/dev/dri \
        --group-add video \
        --shm-size 16G \
        --security-opt seccomp=unconfined \
        --security-opt apparmor=unconfined \
        --cap-add=SYS_PTRACE \
        -v $(pwd):/workspace \
        --env HUGGINGFACE_HUB_CACHE=/workspace \
        --name test \
        rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
:::
::::

Throughput command

Use the following command to start the throughput benchmark.

:::: {.highlight-shell .notranslate}
::: highlight
    model=openai/gpt-oss-120b
    tp=8
    num_prompts=1024
    in=128
    out=128
    dtype=auto
    kv_cache_dtype=auto
    max_num_seqs=1024
    max_num_batched_tokens=8192
    max_model_len=8192

    vllm bench throughput --model $model \
        -tp $tp \
        --num-prompts $num_prompts \
        --input-len $in \
        --output-len $out \
        --dtype $dtype \
        --kv-cache-dtype $kv_cache_dtype \
        --max-num-seqs $max_num_seqs \
        --max-num-batched-tokens $max_num_batched_tokens \
        --max-model-len $max_model_len \
        --trust-remote-code \
        --output-json ${model}_throughput.json \
        --gpu-memory-utilization 0.9
:::
::::

Serving command

1.  Start the server using the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        model=openai/gpt-oss-120b
        tp=8
        dtype=auto
        kv_cache_dtype=auto
        max_num_seqs=256
        max_num_batched_tokens=8192
        max_model_len=8192

        vllm serve $model \
            -tp $tp \
            --dtype $dtype \
            --kv-cache-dtype $kv_cache_dtype \
            --max-num-seqs $max_num_seqs \
            --max-num-batched-tokens $max_num_batched_tokens \
            --max-model-len $max_model_len \
            --no-enable-prefix-caching \
            --swap-space 16 \
            --disable-log-requests \
            --trust-remote-code \
            --gpu-memory-utilization 0.9
    :::
    ::::

    Wait until the model has loaded and the server is ready to accept requests.

2.  On another terminal on the same machine, run the benchmark:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # Connect to the container
        docker exec -it test bash

        # Wait for the server to start
        until curl -s http://localhost:8000/v1/models; do sleep 30; done

        # Run the benchmark
        model=openai/gpt-oss-120b
        max_concurrency=1
        num_prompts=10
        in=128
        out=128
        vllm bench serve --model $model \
            --percentile-metrics "ttft,tpot,itl,e2el" \
            --dataset-name random \
            --ignore-eos \
            --max-concurrency $max_concurrency \
            --num-prompts $num_prompts \
            --random-input-len $in \
            --random-output-len $out \
            --trust-remote-code \
            --save-result \
            --result-filename ${model}_serving.json
    :::
    ::::

::::: {.admonition .note}
Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B, try adding [`export`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre} to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:::: {.highlight-default .notranslate}
::: highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token
:::
::::
:::::

`<style>
mjx-container[jax="CHTML"][display="true"] {
   text-align: left;
   margin: 0;
}
</style>`{=html}

::: {.admonition .note}
Note

Throughput is calculated as:

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  :::

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  :::
:::
::::::::::::
::::::::::::::
:::::::::::::::

::::::::::::::: {.model-doc .pyt-vllm-mixtral-8x7b .docutils .container}
:::::::::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to Mixtral MoE 8x7B. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  On the host machine, use this command to run the performance benchmark test on the [Mixtral MoE 8x7B](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1){.reference .external} model using one node with the [`float16`{.docutils .literal .notranslate}]{.pre} data type.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_vllm_mixtral-8x7b \
            --keep-model-dir \
            --live-output
    :::
    ::::

MAD launches a Docker container with the name [`container_ci-pyt_vllm_mixtral-8x7b`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_vllm_mixtral-8x7b_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_vllm_mixtral-8x7b_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-930){.reference .internal} are preconfigured to collect offline throughput and online serving performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
:::

Standalone benchmarking

:::::::::::: {.sd-tab-content .docutils}
The following commands are optimized for Mixtral MoE 8x7B. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

::: {.admonition .seealso}
See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs){.reference .external} in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs){.reference .external} for descriptions of available configuration options and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md){.reference .external} for additional benchmarking information.
:::

Launch the container

You can run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm7.0.0_vllm_0.10.2_20251006/images/sha256-94fd001964e1cf55c3224a445b1fb5be31a7dac302315255db8422d813edd7f5){.reference .external} as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
    docker run -it \
        --device=/dev/kfd \
        --device=/dev/dri \
        --group-add video \
        --shm-size 16G \
        --security-opt seccomp=unconfined \
        --security-opt apparmor=unconfined \
        --cap-add=SYS_PTRACE \
        -v $(pwd):/workspace \
        --env HUGGINGFACE_HUB_CACHE=/workspace \
        --name test \
        rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
:::
::::

Throughput command

Use the following command to start the throughput benchmark.

:::: {.highlight-shell .notranslate}
::: highlight
    model=mistralai/Mixtral-8x7B-Instruct-v0.1
    tp=8
    num_prompts=1024
    in=128
    out=128
    dtype=auto
    kv_cache_dtype=auto
    max_num_seqs=1024
    max_num_batched_tokens=32768
    max_model_len=8192

    vllm bench throughput --model $model \
        -tp $tp \
        --num-prompts $num_prompts \
        --input-len $in \
        --output-len $out \
        --dtype $dtype \
        --kv-cache-dtype $kv_cache_dtype \
        --max-num-seqs $max_num_seqs \
        --max-num-batched-tokens $max_num_batched_tokens \
        --max-model-len $max_model_len \
        --trust-remote-code \
        --output-json ${model}_throughput.json \
        --gpu-memory-utilization 0.9
:::
::::

Serving command

1.  Start the server using the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        model=mistralai/Mixtral-8x7B-Instruct-v0.1
        tp=8
        dtype=auto
        kv_cache_dtype=auto
        max_num_seqs=256
        max_num_batched_tokens=32768
        max_model_len=8192

        vllm serve $model \
            -tp $tp \
            --dtype $dtype \
            --kv-cache-dtype $kv_cache_dtype \
            --max-num-seqs $max_num_seqs \
            --max-num-batched-tokens $max_num_batched_tokens \
            --max-model-len $max_model_len \
            --no-enable-prefix-caching \
            --swap-space 16 \
            --disable-log-requests \
            --trust-remote-code \
            --gpu-memory-utilization 0.9
    :::
    ::::

    Wait until the model has loaded and the server is ready to accept requests.

2.  On another terminal on the same machine, run the benchmark:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # Connect to the container
        docker exec -it test bash

        # Wait for the server to start
        until curl -s http://localhost:8000/v1/models; do sleep 30; done

        # Run the benchmark
        model=mistralai/Mixtral-8x7B-Instruct-v0.1
        max_concurrency=1
        num_prompts=10
        in=128
        out=128
        vllm bench serve --model $model \
            --percentile-metrics "ttft,tpot,itl,e2el" \
            --dataset-name random \
            --ignore-eos \
            --max-concurrency $max_concurrency \
            --num-prompts $num_prompts \
            --random-input-len $in \
            --random-output-len $out \
            --trust-remote-code \
            --save-result \
            --result-filename ${model}_serving.json
    :::
    ::::

::::: {.admonition .note}
Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B, try adding [`export`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre} to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:::: {.highlight-default .notranslate}
::: highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token
:::
::::
:::::

`<style>
mjx-container[jax="CHTML"][display="true"] {
   text-align: left;
   margin: 0;
}
</style>`{=html}

::: {.admonition .note}
Note

Throughput is calculated as:

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  :::

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  :::
:::
::::::::::::
::::::::::::::
:::::::::::::::

::::::::::::::: {.model-doc .pyt-vllm-mixtral-8x7b-fp8 .docutils .container}
:::::::::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to Mixtral MoE 8x7B FP8. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  On the host machine, use this command to run the performance benchmark test on the [Mixtral MoE 8x7B FP8](https://huggingface.co/amd/Mixtral-8x7B-Instruct-v0.1-FP8-KV){.reference .external} model using one node with the [`float8`{.docutils .literal .notranslate}]{.pre} data type.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_vllm_mixtral-8x7b_fp8 \
            --keep-model-dir \
            --live-output
    :::
    ::::

MAD launches a Docker container with the name [`container_ci-pyt_vllm_mixtral-8x7b_fp8`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_vllm_mixtral-8x7b_fp8_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_vllm_mixtral-8x7b_fp8_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-930){.reference .internal} are preconfigured to collect offline throughput and online serving performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
:::

Standalone benchmarking

:::::::::::: {.sd-tab-content .docutils}
The following commands are optimized for Mixtral MoE 8x7B FP8. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

::: {.admonition .seealso}
See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs){.reference .external} in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs){.reference .external} for descriptions of available configuration options and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md){.reference .external} for additional benchmarking information.
:::

Launch the container

You can run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm7.0.0_vllm_0.10.2_20251006/images/sha256-94fd001964e1cf55c3224a445b1fb5be31a7dac302315255db8422d813edd7f5){.reference .external} as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
    docker run -it \
        --device=/dev/kfd \
        --device=/dev/dri \
        --group-add video \
        --shm-size 16G \
        --security-opt seccomp=unconfined \
        --security-opt apparmor=unconfined \
        --cap-add=SYS_PTRACE \
        -v $(pwd):/workspace \
        --env HUGGINGFACE_HUB_CACHE=/workspace \
        --name test \
        rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
:::
::::

Throughput command

Use the following command to start the throughput benchmark.

:::: {.highlight-shell .notranslate}
::: highlight
    model=amd/Mixtral-8x7B-Instruct-v0.1-FP8-KV
    tp=8
    num_prompts=1024
    in=128
    out=128
    dtype=auto
    kv_cache_dtype=fp8
    max_num_seqs=1024
    max_num_batched_tokens=32768
    max_model_len=8192

    vllm bench throughput --model $model \
        -tp $tp \
        --num-prompts $num_prompts \
        --input-len $in \
        --output-len $out \
        --dtype $dtype \
        --kv-cache-dtype $kv_cache_dtype \
        --max-num-seqs $max_num_seqs \
        --max-num-batched-tokens $max_num_batched_tokens \
        --max-model-len $max_model_len \
        --trust-remote-code \
        --output-json ${model}_throughput.json \
        --gpu-memory-utilization 0.9
:::
::::

Serving command

1.  Start the server using the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        model=amd/Mixtral-8x7B-Instruct-v0.1-FP8-KV
        tp=8
        dtype=auto
        kv_cache_dtype=fp8
        max_num_seqs=256
        max_num_batched_tokens=32768
        max_model_len=8192

        vllm serve $model \
            -tp $tp \
            --dtype $dtype \
            --kv-cache-dtype $kv_cache_dtype \
            --max-num-seqs $max_num_seqs \
            --max-num-batched-tokens $max_num_batched_tokens \
            --max-model-len $max_model_len \
            --no-enable-prefix-caching \
            --swap-space 16 \
            --disable-log-requests \
            --trust-remote-code \
            --gpu-memory-utilization 0.9
    :::
    ::::

    Wait until the model has loaded and the server is ready to accept requests.

2.  On another terminal on the same machine, run the benchmark:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # Connect to the container
        docker exec -it test bash

        # Wait for the server to start
        until curl -s http://localhost:8000/v1/models; do sleep 30; done

        # Run the benchmark
        model=amd/Mixtral-8x7B-Instruct-v0.1-FP8-KV
        max_concurrency=1
        num_prompts=10
        in=128
        out=128
        vllm bench serve --model $model \
            --percentile-metrics "ttft,tpot,itl,e2el" \
            --dataset-name random \
            --ignore-eos \
            --max-concurrency $max_concurrency \
            --num-prompts $num_prompts \
            --random-input-len $in \
            --random-output-len $out \
            --trust-remote-code \
            --save-result \
            --result-filename ${model}_serving.json
    :::
    ::::

::::: {.admonition .note}
Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B, try adding [`export`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre} to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:::: {.highlight-default .notranslate}
::: highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token
:::
::::
:::::

`<style>
mjx-container[jax="CHTML"][display="true"] {
   text-align: left;
   margin: 0;
}
</style>`{=html}

::: {.admonition .note}
Note

Throughput is calculated as:

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  :::

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  :::
:::
::::::::::::
::::::::::::::
:::::::::::::::

::::::::::::::: {.model-doc .pyt-vllm-mixtral-8x22b .docutils .container}
:::::::::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to Mixtral MoE 8x22B. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  On the host machine, use this command to run the performance benchmark test on the [Mixtral MoE 8x22B](https://huggingface.co/mistralai/Mixtral-8x22B-Instruct-v0.1){.reference .external} model using one node with the [`float16`{.docutils .literal .notranslate}]{.pre} data type.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_vllm_mixtral-8x22b \
            --keep-model-dir \
            --live-output
    :::
    ::::

MAD launches a Docker container with the name [`container_ci-pyt_vllm_mixtral-8x22b`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_vllm_mixtral-8x22b_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_vllm_mixtral-8x22b_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-930){.reference .internal} are preconfigured to collect offline throughput and online serving performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
:::

Standalone benchmarking

:::::::::::: {.sd-tab-content .docutils}
The following commands are optimized for Mixtral MoE 8x22B. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

::: {.admonition .seealso}
See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs){.reference .external} in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs){.reference .external} for descriptions of available configuration options and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md){.reference .external} for additional benchmarking information.
:::

Launch the container

You can run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm7.0.0_vllm_0.10.2_20251006/images/sha256-94fd001964e1cf55c3224a445b1fb5be31a7dac302315255db8422d813edd7f5){.reference .external} as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
    docker run -it \
        --device=/dev/kfd \
        --device=/dev/dri \
        --group-add video \
        --shm-size 16G \
        --security-opt seccomp=unconfined \
        --security-opt apparmor=unconfined \
        --cap-add=SYS_PTRACE \
        -v $(pwd):/workspace \
        --env HUGGINGFACE_HUB_CACHE=/workspace \
        --name test \
        rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
:::
::::

Throughput command

Use the following command to start the throughput benchmark.

:::: {.highlight-shell .notranslate}
::: highlight
    model=mistralai/Mixtral-8x22B-Instruct-v0.1
    tp=8
    num_prompts=1024
    in=128
    out=128
    dtype=auto
    kv_cache_dtype=auto
    max_num_seqs=1024
    max_num_batched_tokens=65536
    max_model_len=8192

    vllm bench throughput --model $model \
        -tp $tp \
        --num-prompts $num_prompts \
        --input-len $in \
        --output-len $out \
        --dtype $dtype \
        --kv-cache-dtype $kv_cache_dtype \
        --max-num-seqs $max_num_seqs \
        --max-num-batched-tokens $max_num_batched_tokens \
        --max-model-len $max_model_len \
        --trust-remote-code \
        --output-json ${model}_throughput.json \
        --gpu-memory-utilization 0.9
:::
::::

Serving command

1.  Start the server using the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        model=mistralai/Mixtral-8x22B-Instruct-v0.1
        tp=8
        dtype=auto
        kv_cache_dtype=auto
        max_num_seqs=256
        max_num_batched_tokens=65536
        max_model_len=8192

        vllm serve $model \
            -tp $tp \
            --dtype $dtype \
            --kv-cache-dtype $kv_cache_dtype \
            --max-num-seqs $max_num_seqs \
            --max-num-batched-tokens $max_num_batched_tokens \
            --max-model-len $max_model_len \
            --no-enable-prefix-caching \
            --swap-space 16 \
            --disable-log-requests \
            --trust-remote-code \
            --gpu-memory-utilization 0.9
    :::
    ::::

    Wait until the model has loaded and the server is ready to accept requests.

2.  On another terminal on the same machine, run the benchmark:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # Connect to the container
        docker exec -it test bash

        # Wait for the server to start
        until curl -s http://localhost:8000/v1/models; do sleep 30; done

        # Run the benchmark
        model=mistralai/Mixtral-8x22B-Instruct-v0.1
        max_concurrency=1
        num_prompts=10
        in=128
        out=128
        vllm bench serve --model $model \
            --percentile-metrics "ttft,tpot,itl,e2el" \
            --dataset-name random \
            --ignore-eos \
            --max-concurrency $max_concurrency \
            --num-prompts $num_prompts \
            --random-input-len $in \
            --random-output-len $out \
            --trust-remote-code \
            --save-result \
            --result-filename ${model}_serving.json
    :::
    ::::

::::: {.admonition .note}
Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B, try adding [`export`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre} to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:::: {.highlight-default .notranslate}
::: highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token
:::
::::
:::::

`<style>
mjx-container[jax="CHTML"][display="true"] {
   text-align: left;
   margin: 0;
}
</style>`{=html}

::: {.admonition .note}
Note

Throughput is calculated as:

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  :::

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  :::
:::
::::::::::::
::::::::::::::
:::::::::::::::

::::::::::::::: {.model-doc .pyt-vllm-mixtral-8x22b-fp8 .docutils .container}
:::::::::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to Mixtral MoE 8x22B FP8. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  On the host machine, use this command to run the performance benchmark test on the [Mixtral MoE 8x22B FP8](https://huggingface.co/amd/Mixtral-8x22B-Instruct-v0.1-FP8-KV){.reference .external} model using one node with the [`float8`{.docutils .literal .notranslate}]{.pre} data type.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_vllm_mixtral-8x22b_fp8 \
            --keep-model-dir \
            --live-output
    :::
    ::::

MAD launches a Docker container with the name [`container_ci-pyt_vllm_mixtral-8x22b_fp8`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_vllm_mixtral-8x22b_fp8_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_vllm_mixtral-8x22b_fp8_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-930){.reference .internal} are preconfigured to collect offline throughput and online serving performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
:::

Standalone benchmarking

:::::::::::: {.sd-tab-content .docutils}
The following commands are optimized for Mixtral MoE 8x22B FP8. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

::: {.admonition .seealso}
See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs){.reference .external} in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs){.reference .external} for descriptions of available configuration options and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md){.reference .external} for additional benchmarking information.
:::

Launch the container

You can run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm7.0.0_vllm_0.10.2_20251006/images/sha256-94fd001964e1cf55c3224a445b1fb5be31a7dac302315255db8422d813edd7f5){.reference .external} as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
    docker run -it \
        --device=/dev/kfd \
        --device=/dev/dri \
        --group-add video \
        --shm-size 16G \
        --security-opt seccomp=unconfined \
        --security-opt apparmor=unconfined \
        --cap-add=SYS_PTRACE \
        -v $(pwd):/workspace \
        --env HUGGINGFACE_HUB_CACHE=/workspace \
        --name test \
        rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
:::
::::

Throughput command

Use the following command to start the throughput benchmark.

:::: {.highlight-shell .notranslate}
::: highlight
    model=amd/Mixtral-8x22B-Instruct-v0.1-FP8-KV
    tp=8
    num_prompts=1024
    in=128
    out=128
    dtype=auto
    kv_cache_dtype=fp8
    max_num_seqs=1024
    max_num_batched_tokens=65536
    max_model_len=8192

    vllm bench throughput --model $model \
        -tp $tp \
        --num-prompts $num_prompts \
        --input-len $in \
        --output-len $out \
        --dtype $dtype \
        --kv-cache-dtype $kv_cache_dtype \
        --max-num-seqs $max_num_seqs \
        --max-num-batched-tokens $max_num_batched_tokens \
        --max-model-len $max_model_len \
        --trust-remote-code \
        --output-json ${model}_throughput.json \
        --gpu-memory-utilization 0.9
:::
::::

Serving command

1.  Start the server using the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        model=amd/Mixtral-8x22B-Instruct-v0.1-FP8-KV
        tp=8
        dtype=auto
        kv_cache_dtype=fp8
        max_num_seqs=256
        max_num_batched_tokens=65536
        max_model_len=8192

        vllm serve $model \
            -tp $tp \
            --dtype $dtype \
            --kv-cache-dtype $kv_cache_dtype \
            --max-num-seqs $max_num_seqs \
            --max-num-batched-tokens $max_num_batched_tokens \
            --max-model-len $max_model_len \
            --no-enable-prefix-caching \
            --swap-space 16 \
            --disable-log-requests \
            --trust-remote-code \
            --gpu-memory-utilization 0.9
    :::
    ::::

    Wait until the model has loaded and the server is ready to accept requests.

2.  On another terminal on the same machine, run the benchmark:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # Connect to the container
        docker exec -it test bash

        # Wait for the server to start
        until curl -s http://localhost:8000/v1/models; do sleep 30; done

        # Run the benchmark
        model=amd/Mixtral-8x22B-Instruct-v0.1-FP8-KV
        max_concurrency=1
        num_prompts=10
        in=128
        out=128
        vllm bench serve --model $model \
            --percentile-metrics "ttft,tpot,itl,e2el" \
            --dataset-name random \
            --ignore-eos \
            --max-concurrency $max_concurrency \
            --num-prompts $num_prompts \
            --random-input-len $in \
            --random-output-len $out \
            --trust-remote-code \
            --save-result \
            --result-filename ${model}_serving.json
    :::
    ::::

::::: {.admonition .note}
Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B, try adding [`export`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre} to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:::: {.highlight-default .notranslate}
::: highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token
:::
::::
:::::

`<style>
mjx-container[jax="CHTML"][display="true"] {
   text-align: left;
   margin: 0;
}
</style>`{=html}

::: {.admonition .note}
Note

Throughput is calculated as:

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  :::

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  :::
:::
::::::::::::
::::::::::::::
:::::::::::::::

::::::::::::::: {.model-doc .pyt-vllm-qwen3-8b .docutils .container}
:::::::::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to Qwen3 8B. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  On the host machine, use this command to run the performance benchmark test on the [Qwen3 8B](https://huggingface.co/Qwen/Qwen3-8B){.reference .external} model using one node with the [`float16`{.docutils .literal .notranslate}]{.pre} data type.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_vllm_qwen3-8b \
            --keep-model-dir \
            --live-output
    :::
    ::::

MAD launches a Docker container with the name [`container_ci-pyt_vllm_qwen3-8b`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_vllm_qwen3-8b_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_vllm_qwen3-8b_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-930){.reference .internal} are preconfigured to collect offline throughput and online serving performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
:::

Standalone benchmarking

:::::::::::: {.sd-tab-content .docutils}
The following commands are optimized for Qwen3 8B. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

::: {.admonition .seealso}
See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs){.reference .external} in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs){.reference .external} for descriptions of available configuration options and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md){.reference .external} for additional benchmarking information.
:::

Launch the container

You can run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm7.0.0_vllm_0.10.2_20251006/images/sha256-94fd001964e1cf55c3224a445b1fb5be31a7dac302315255db8422d813edd7f5){.reference .external} as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
    docker run -it \
        --device=/dev/kfd \
        --device=/dev/dri \
        --group-add video \
        --shm-size 16G \
        --security-opt seccomp=unconfined \
        --security-opt apparmor=unconfined \
        --cap-add=SYS_PTRACE \
        -v $(pwd):/workspace \
        --env HUGGINGFACE_HUB_CACHE=/workspace \
        --name test \
        rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
:::
::::

Throughput command

Use the following command to start the throughput benchmark.

:::: {.highlight-shell .notranslate}
::: highlight
    model=Qwen/Qwen3-8B
    tp=1
    num_prompts=1024
    in=128
    out=128
    dtype=auto
    kv_cache_dtype=auto
    max_num_seqs=1024
    max_num_batched_tokens=40960
    max_model_len=8192

    vllm bench throughput --model $model \
        -tp $tp \
        --num-prompts $num_prompts \
        --input-len $in \
        --output-len $out \
        --dtype $dtype \
        --kv-cache-dtype $kv_cache_dtype \
        --max-num-seqs $max_num_seqs \
        --max-num-batched-tokens $max_num_batched_tokens \
        --max-model-len $max_model_len \
        --trust-remote-code \
        --output-json ${model}_throughput.json \
        --gpu-memory-utilization 0.9
:::
::::

Serving command

1.  Start the server using the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        model=Qwen/Qwen3-8B
        tp=1
        dtype=auto
        kv_cache_dtype=auto
        max_num_seqs=256
        max_num_batched_tokens=40960
        max_model_len=8192

        vllm serve $model \
            -tp $tp \
            --dtype $dtype \
            --kv-cache-dtype $kv_cache_dtype \
            --max-num-seqs $max_num_seqs \
            --max-num-batched-tokens $max_num_batched_tokens \
            --max-model-len $max_model_len \
            --no-enable-prefix-caching \
            --swap-space 16 \
            --disable-log-requests \
            --trust-remote-code \
            --gpu-memory-utilization 0.9
    :::
    ::::

    Wait until the model has loaded and the server is ready to accept requests.

2.  On another terminal on the same machine, run the benchmark:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # Connect to the container
        docker exec -it test bash

        # Wait for the server to start
        until curl -s http://localhost:8000/v1/models; do sleep 30; done

        # Run the benchmark
        model=Qwen/Qwen3-8B
        max_concurrency=1
        num_prompts=10
        in=128
        out=128
        vllm bench serve --model $model \
            --percentile-metrics "ttft,tpot,itl,e2el" \
            --dataset-name random \
            --ignore-eos \
            --max-concurrency $max_concurrency \
            --num-prompts $num_prompts \
            --random-input-len $in \
            --random-output-len $out \
            --trust-remote-code \
            --save-result \
            --result-filename ${model}_serving.json
    :::
    ::::

::::: {.admonition .note}
Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B, try adding [`export`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre} to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:::: {.highlight-default .notranslate}
::: highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token
:::
::::
:::::

`<style>
mjx-container[jax="CHTML"][display="true"] {
   text-align: left;
   margin: 0;
}
</style>`{=html}

::: {.admonition .note}
Note

Throughput is calculated as:

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  :::

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  :::
:::
::::::::::::
::::::::::::::
:::::::::::::::

::::::::::::::: {.model-doc .pyt-vllm-qwen3-32b .docutils .container}
:::::::::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to Qwen3 32B. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  On the host machine, use this command to run the performance benchmark test on the [Qwen3 32B](https://huggingface.co/Qwen/Qwen3-32B){.reference .external} model using one node with the [`float16`{.docutils .literal .notranslate}]{.pre} data type.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_vllm_qwen3-32b \
            --keep-model-dir \
            --live-output
    :::
    ::::

MAD launches a Docker container with the name [`container_ci-pyt_vllm_qwen3-32b`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_vllm_qwen3-32b_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_vllm_qwen3-32b_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-930){.reference .internal} are preconfigured to collect offline throughput and online serving performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
:::

Standalone benchmarking

:::::::::::: {.sd-tab-content .docutils}
The following commands are optimized for Qwen3 32B. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

::: {.admonition .seealso}
See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs){.reference .external} in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs){.reference .external} for descriptions of available configuration options and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md){.reference .external} for additional benchmarking information.
:::

Launch the container

You can run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm7.0.0_vllm_0.10.2_20251006/images/sha256-94fd001964e1cf55c3224a445b1fb5be31a7dac302315255db8422d813edd7f5){.reference .external} as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
    docker run -it \
        --device=/dev/kfd \
        --device=/dev/dri \
        --group-add video \
        --shm-size 16G \
        --security-opt seccomp=unconfined \
        --security-opt apparmor=unconfined \
        --cap-add=SYS_PTRACE \
        -v $(pwd):/workspace \
        --env HUGGINGFACE_HUB_CACHE=/workspace \
        --name test \
        rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
:::
::::

Throughput command

Use the following command to start the throughput benchmark.

:::: {.highlight-shell .notranslate}
::: highlight
    model=Qwen/Qwen3-32b
    tp=1
    num_prompts=1024
    in=128
    out=128
    dtype=auto
    kv_cache_dtype=auto
    max_num_seqs=1024
    max_num_batched_tokens=40960
    max_model_len=8192

    vllm bench throughput --model $model \
        -tp $tp \
        --num-prompts $num_prompts \
        --input-len $in \
        --output-len $out \
        --dtype $dtype \
        --kv-cache-dtype $kv_cache_dtype \
        --max-num-seqs $max_num_seqs \
        --max-num-batched-tokens $max_num_batched_tokens \
        --max-model-len $max_model_len \
        --trust-remote-code \
        --output-json ${model}_throughput.json \
        --gpu-memory-utilization 0.9
:::
::::

Serving command

1.  Start the server using the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        model=Qwen/Qwen3-32b
        tp=1
        dtype=auto
        kv_cache_dtype=auto
        max_num_seqs=256
        max_num_batched_tokens=40960
        max_model_len=8192

        vllm serve $model \
            -tp $tp \
            --dtype $dtype \
            --kv-cache-dtype $kv_cache_dtype \
            --max-num-seqs $max_num_seqs \
            --max-num-batched-tokens $max_num_batched_tokens \
            --max-model-len $max_model_len \
            --no-enable-prefix-caching \
            --swap-space 16 \
            --disable-log-requests \
            --trust-remote-code \
            --gpu-memory-utilization 0.9
    :::
    ::::

    Wait until the model has loaded and the server is ready to accept requests.

2.  On another terminal on the same machine, run the benchmark:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # Connect to the container
        docker exec -it test bash

        # Wait for the server to start
        until curl -s http://localhost:8000/v1/models; do sleep 30; done

        # Run the benchmark
        model=Qwen/Qwen3-32b
        max_concurrency=1
        num_prompts=10
        in=128
        out=128
        vllm bench serve --model $model \
            --percentile-metrics "ttft,tpot,itl,e2el" \
            --dataset-name random \
            --ignore-eos \
            --max-concurrency $max_concurrency \
            --num-prompts $num_prompts \
            --random-input-len $in \
            --random-output-len $out \
            --trust-remote-code \
            --save-result \
            --result-filename ${model}_serving.json
    :::
    ::::

::::: {.admonition .note}
Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B, try adding [`export`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre} to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:::: {.highlight-default .notranslate}
::: highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token
:::
::::
:::::

`<style>
mjx-container[jax="CHTML"][display="true"] {
   text-align: left;
   margin: 0;
}
</style>`{=html}

::: {.admonition .note}
Note

Throughput is calculated as:

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  :::

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  :::
:::
::::::::::::
::::::::::::::
:::::::::::::::

::::::::::::::: {.model-doc .pyt-vllm-qwen3-30b-a3b .docutils .container}
:::::::::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to Qwen3 30B A3B. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  On the host machine, use this command to run the performance benchmark test on the [Qwen3 30B A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B){.reference .external} model using one node with the [`float16`{.docutils .literal .notranslate}]{.pre} data type.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_vllm_qwen3-30b-a3b \
            --keep-model-dir \
            --live-output
    :::
    ::::

MAD launches a Docker container with the name [`container_ci-pyt_vllm_qwen3-30b-a3b`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_vllm_qwen3-30b-a3b_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_vllm_qwen3-30b-a3b_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-930){.reference .internal} are preconfigured to collect offline throughput and online serving performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
:::

Standalone benchmarking

:::::::::::: {.sd-tab-content .docutils}
The following commands are optimized for Qwen3 30B A3B. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

::: {.admonition .seealso}
See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs){.reference .external} in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs){.reference .external} for descriptions of available configuration options and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md){.reference .external} for additional benchmarking information.
:::

Launch the container

You can run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm7.0.0_vllm_0.10.2_20251006/images/sha256-94fd001964e1cf55c3224a445b1fb5be31a7dac302315255db8422d813edd7f5){.reference .external} as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
    docker run -it \
        --device=/dev/kfd \
        --device=/dev/dri \
        --group-add video \
        --shm-size 16G \
        --security-opt seccomp=unconfined \
        --security-opt apparmor=unconfined \
        --cap-add=SYS_PTRACE \
        -v $(pwd):/workspace \
        --env HUGGINGFACE_HUB_CACHE=/workspace \
        --name test \
        rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
:::
::::

Throughput command

Use the following command to start the throughput benchmark.

:::: {.highlight-shell .notranslate}
::: highlight
    model=Qwen/Qwen3-30B-A3B
    tp=1
    num_prompts=1024
    in=128
    out=128
    dtype=auto
    kv_cache_dtype=auto
    max_num_seqs=1024
    max_num_batched_tokens=40960
    max_model_len=8192

    vllm bench throughput --model $model \
        -tp $tp \
        --num-prompts $num_prompts \
        --input-len $in \
        --output-len $out \
        --dtype $dtype \
        --kv-cache-dtype $kv_cache_dtype \
        --max-num-seqs $max_num_seqs \
        --max-num-batched-tokens $max_num_batched_tokens \
        --max-model-len $max_model_len \
        --trust-remote-code \
        --output-json ${model}_throughput.json \
        --gpu-memory-utilization 0.9
:::
::::

Serving command

1.  Start the server using the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        model=Qwen/Qwen3-30B-A3B
        tp=1
        dtype=auto
        kv_cache_dtype=auto
        max_num_seqs=256
        max_num_batched_tokens=40960
        max_model_len=8192

        vllm serve $model \
            -tp $tp \
            --dtype $dtype \
            --kv-cache-dtype $kv_cache_dtype \
            --max-num-seqs $max_num_seqs \
            --max-num-batched-tokens $max_num_batched_tokens \
            --max-model-len $max_model_len \
            --no-enable-prefix-caching \
            --swap-space 16 \
            --disable-log-requests \
            --trust-remote-code \
            --gpu-memory-utilization 0.9
    :::
    ::::

    Wait until the model has loaded and the server is ready to accept requests.

2.  On another terminal on the same machine, run the benchmark:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # Connect to the container
        docker exec -it test bash

        # Wait for the server to start
        until curl -s http://localhost:8000/v1/models; do sleep 30; done

        # Run the benchmark
        model=Qwen/Qwen3-30B-A3B
        max_concurrency=1
        num_prompts=10
        in=128
        out=128
        vllm bench serve --model $model \
            --percentile-metrics "ttft,tpot,itl,e2el" \
            --dataset-name random \
            --ignore-eos \
            --max-concurrency $max_concurrency \
            --num-prompts $num_prompts \
            --random-input-len $in \
            --random-output-len $out \
            --trust-remote-code \
            --save-result \
            --result-filename ${model}_serving.json
    :::
    ::::

::::: {.admonition .note}
Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B, try adding [`export`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre} to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:::: {.highlight-default .notranslate}
::: highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token
:::
::::
:::::

`<style>
mjx-container[jax="CHTML"][display="true"] {
   text-align: left;
   margin: 0;
}
</style>`{=html}

::: {.admonition .note}
Note

Throughput is calculated as:

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  :::

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  :::
:::
::::::::::::
::::::::::::::
:::::::::::::::

::::::::::::::: {.model-doc .pyt-vllm-qwen3-30b-a3b-fp8 .docutils .container}
:::::::::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to Qwen3 30B A3B FP8. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  On the host machine, use this command to run the performance benchmark test on the [Qwen3 30B A3B FP8](https://huggingface.co/Qwen/Qwen3-30B-A3B-FP8){.reference .external} model using one node with the [`float16`{.docutils .literal .notranslate}]{.pre} data type.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_vllm_qwen3-30b-a3b_fp8 \
            --keep-model-dir \
            --live-output
    :::
    ::::

MAD launches a Docker container with the name [`container_ci-pyt_vllm_qwen3-30b-a3b_fp8`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_vllm_qwen3-30b-a3b_fp8_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_vllm_qwen3-30b-a3b_fp8_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-930){.reference .internal} are preconfigured to collect offline throughput and online serving performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
:::

Standalone benchmarking

:::::::::::: {.sd-tab-content .docutils}
The following commands are optimized for Qwen3 30B A3B FP8. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

::: {.admonition .seealso}
See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs){.reference .external} in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs){.reference .external} for descriptions of available configuration options and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md){.reference .external} for additional benchmarking information.
:::

Launch the container

You can run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm7.0.0_vllm_0.10.2_20251006/images/sha256-94fd001964e1cf55c3224a445b1fb5be31a7dac302315255db8422d813edd7f5){.reference .external} as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
    docker run -it \
        --device=/dev/kfd \
        --device=/dev/dri \
        --group-add video \
        --shm-size 16G \
        --security-opt seccomp=unconfined \
        --security-opt apparmor=unconfined \
        --cap-add=SYS_PTRACE \
        -v $(pwd):/workspace \
        --env HUGGINGFACE_HUB_CACHE=/workspace \
        --name test \
        rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
:::
::::

Throughput command

Use the following command to start the throughput benchmark.

:::: {.highlight-shell .notranslate}
::: highlight
    model=Qwen/Qwen3-30B-A3B-FP8
    tp=1
    num_prompts=1024
    in=128
    out=128
    dtype=auto
    kv_cache_dtype=fp8
    max_num_seqs=1024
    max_num_batched_tokens=40960
    max_model_len=8192

    vllm bench throughput --model $model \
        -tp $tp \
        --num-prompts $num_prompts \
        --input-len $in \
        --output-len $out \
        --dtype $dtype \
        --kv-cache-dtype $kv_cache_dtype \
        --max-num-seqs $max_num_seqs \
        --max-num-batched-tokens $max_num_batched_tokens \
        --max-model-len $max_model_len \
        --trust-remote-code \
        --output-json ${model}_throughput.json \
        --gpu-memory-utilization 0.9
:::
::::

Serving command

1.  Start the server using the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        model=Qwen/Qwen3-30B-A3B-FP8
        tp=1
        dtype=auto
        kv_cache_dtype=fp8
        max_num_seqs=256
        max_num_batched_tokens=40960
        max_model_len=8192

        vllm serve $model \
            -tp $tp \
            --dtype $dtype \
            --kv-cache-dtype $kv_cache_dtype \
            --max-num-seqs $max_num_seqs \
            --max-num-batched-tokens $max_num_batched_tokens \
            --max-model-len $max_model_len \
            --no-enable-prefix-caching \
            --swap-space 16 \
            --disable-log-requests \
            --trust-remote-code \
            --gpu-memory-utilization 0.9
    :::
    ::::

    Wait until the model has loaded and the server is ready to accept requests.

2.  On another terminal on the same machine, run the benchmark:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # Connect to the container
        docker exec -it test bash

        # Wait for the server to start
        until curl -s http://localhost:8000/v1/models; do sleep 30; done

        # Run the benchmark
        model=Qwen/Qwen3-30B-A3B-FP8
        max_concurrency=1
        num_prompts=10
        in=128
        out=128
        vllm bench serve --model $model \
            --percentile-metrics "ttft,tpot,itl,e2el" \
            --dataset-name random \
            --ignore-eos \
            --max-concurrency $max_concurrency \
            --num-prompts $num_prompts \
            --random-input-len $in \
            --random-output-len $out \
            --trust-remote-code \
            --save-result \
            --result-filename ${model}_serving.json
    :::
    ::::

::::: {.admonition .note}
Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B, try adding [`export`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre} to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:::: {.highlight-default .notranslate}
::: highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token
:::
::::
:::::

`<style>
mjx-container[jax="CHTML"][display="true"] {
   text-align: left;
   margin: 0;
}
</style>`{=html}

::: {.admonition .note}
Note

Throughput is calculated as:

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  :::

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  :::
:::
::::::::::::
::::::::::::::
:::::::::::::::

::::::::::::::: {.model-doc .pyt-vllm-qwen3-235b-a22b .docutils .container}
:::::::::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to Qwen3 235B A22B. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  On the host machine, use this command to run the performance benchmark test on the [Qwen3 235B A22B](https://huggingface.co/Qwen/Qwen3-235B-A22B){.reference .external} model using one node with the [`float16`{.docutils .literal .notranslate}]{.pre} data type.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_vllm_qwen3-235b-a22b \
            --keep-model-dir \
            --live-output
    :::
    ::::

MAD launches a Docker container with the name [`container_ci-pyt_vllm_qwen3-235b-a22b`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_vllm_qwen3-235b-a22b_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_vllm_qwen3-235b-a22b_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-930){.reference .internal} are preconfigured to collect offline throughput and online serving performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
:::

Standalone benchmarking

:::::::::::: {.sd-tab-content .docutils}
The following commands are optimized for Qwen3 235B A22B. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

::: {.admonition .seealso}
See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs){.reference .external} in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs){.reference .external} for descriptions of available configuration options and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md){.reference .external} for additional benchmarking information.
:::

Launch the container

You can run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm7.0.0_vllm_0.10.2_20251006/images/sha256-94fd001964e1cf55c3224a445b1fb5be31a7dac302315255db8422d813edd7f5){.reference .external} as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
    docker run -it \
        --device=/dev/kfd \
        --device=/dev/dri \
        --group-add video \
        --shm-size 16G \
        --security-opt seccomp=unconfined \
        --security-opt apparmor=unconfined \
        --cap-add=SYS_PTRACE \
        -v $(pwd):/workspace \
        --env HUGGINGFACE_HUB_CACHE=/workspace \
        --name test \
        rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
:::
::::

Throughput command

Use the following command to start the throughput benchmark.

:::: {.highlight-shell .notranslate}
::: highlight
    model=Qwen/Qwen3-235B-A22B
    tp=8
    num_prompts=1024
    in=128
    out=128
    dtype=auto
    kv_cache_dtype=auto
    max_num_seqs=1024
    max_num_batched_tokens=40960
    max_model_len=8192

    vllm bench throughput --model $model \
        -tp $tp \
        --num-prompts $num_prompts \
        --input-len $in \
        --output-len $out \
        --dtype $dtype \
        --kv-cache-dtype $kv_cache_dtype \
        --max-num-seqs $max_num_seqs \
        --max-num-batched-tokens $max_num_batched_tokens \
        --max-model-len $max_model_len \
        --trust-remote-code \
        --output-json ${model}_throughput.json \
        --gpu-memory-utilization 0.9
:::
::::

Serving command

1.  Start the server using the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        model=Qwen/Qwen3-235B-A22B
        tp=8
        dtype=auto
        kv_cache_dtype=auto
        max_num_seqs=256
        max_num_batched_tokens=40960
        max_model_len=8192

        vllm serve $model \
            -tp $tp \
            --dtype $dtype \
            --kv-cache-dtype $kv_cache_dtype \
            --max-num-seqs $max_num_seqs \
            --max-num-batched-tokens $max_num_batched_tokens \
            --max-model-len $max_model_len \
            --no-enable-prefix-caching \
            --swap-space 16 \
            --disable-log-requests \
            --trust-remote-code \
            --gpu-memory-utilization 0.9
    :::
    ::::

    Wait until the model has loaded and the server is ready to accept requests.

2.  On another terminal on the same machine, run the benchmark:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # Connect to the container
        docker exec -it test bash

        # Wait for the server to start
        until curl -s http://localhost:8000/v1/models; do sleep 30; done

        # Run the benchmark
        model=Qwen/Qwen3-235B-A22B
        max_concurrency=1
        num_prompts=10
        in=128
        out=128
        vllm bench serve --model $model \
            --percentile-metrics "ttft,tpot,itl,e2el" \
            --dataset-name random \
            --ignore-eos \
            --max-concurrency $max_concurrency \
            --num-prompts $num_prompts \
            --random-input-len $in \
            --random-output-len $out \
            --trust-remote-code \
            --save-result \
            --result-filename ${model}_serving.json
    :::
    ::::

::::: {.admonition .note}
Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B, try adding [`export`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre} to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:::: {.highlight-default .notranslate}
::: highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token
:::
::::
:::::

`<style>
mjx-container[jax="CHTML"][display="true"] {
   text-align: left;
   margin: 0;
}
</style>`{=html}

::: {.admonition .note}
Note

Throughput is calculated as:

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  :::

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  :::
:::
::::::::::::
::::::::::::::
:::::::::::::::

::::::::::::::: {.model-doc .pyt-vllm-qwen3-235b-a22b-fp8 .docutils .container}
:::::::::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to Qwen3 235B A22B FP8. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  On the host machine, use this command to run the performance benchmark test on the [Qwen3 235B A22B FP8](https://huggingface.co/Qwen/Qwen3-235B-A22B-FP8){.reference .external} model using one node with the [`float8`{.docutils .literal .notranslate}]{.pre} data type.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_vllm_qwen3-235b-a22b_fp8 \
            --keep-model-dir \
            --live-output
    :::
    ::::

MAD launches a Docker container with the name [`container_ci-pyt_vllm_qwen3-235b-a22b_fp8`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_vllm_qwen3-235b-a22b_fp8_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_vllm_qwen3-235b-a22b_fp8_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-930){.reference .internal} are preconfigured to collect offline throughput and online serving performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
:::

Standalone benchmarking

:::::::::::: {.sd-tab-content .docutils}
The following commands are optimized for Qwen3 235B A22B FP8. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

::: {.admonition .seealso}
See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs){.reference .external} in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs){.reference .external} for descriptions of available configuration options and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md){.reference .external} for additional benchmarking information.
:::

Launch the container

You can run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm7.0.0_vllm_0.10.2_20251006/images/sha256-94fd001964e1cf55c3224a445b1fb5be31a7dac302315255db8422d813edd7f5){.reference .external} as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
    docker run -it \
        --device=/dev/kfd \
        --device=/dev/dri \
        --group-add video \
        --shm-size 16G \
        --security-opt seccomp=unconfined \
        --security-opt apparmor=unconfined \
        --cap-add=SYS_PTRACE \
        -v $(pwd):/workspace \
        --env HUGGINGFACE_HUB_CACHE=/workspace \
        --name test \
        rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
:::
::::

Throughput command

Use the following command to start the throughput benchmark.

:::: {.highlight-shell .notranslate}
::: highlight
    model=Qwen/Qwen3-235B-A22B-FP8
    tp=8
    num_prompts=1024
    in=128
    out=128
    dtype=auto
    kv_cache_dtype=fp8
    max_num_seqs=1024
    max_num_batched_tokens=40960
    max_model_len=8192

    vllm bench throughput --model $model \
        -tp $tp \
        --num-prompts $num_prompts \
        --input-len $in \
        --output-len $out \
        --dtype $dtype \
        --kv-cache-dtype $kv_cache_dtype \
        --max-num-seqs $max_num_seqs \
        --max-num-batched-tokens $max_num_batched_tokens \
        --max-model-len $max_model_len \
        --trust-remote-code \
        --output-json ${model}_throughput.json \
        --gpu-memory-utilization 0.9
:::
::::

Serving command

1.  Start the server using the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        model=Qwen/Qwen3-235B-A22B-FP8
        tp=8
        dtype=auto
        kv_cache_dtype=fp8
        max_num_seqs=256
        max_num_batched_tokens=40960
        max_model_len=8192

        vllm serve $model \
            -tp $tp \
            --dtype $dtype \
            --kv-cache-dtype $kv_cache_dtype \
            --max-num-seqs $max_num_seqs \
            --max-num-batched-tokens $max_num_batched_tokens \
            --max-model-len $max_model_len \
            --no-enable-prefix-caching \
            --swap-space 16 \
            --disable-log-requests \
            --trust-remote-code \
            --gpu-memory-utilization 0.9
    :::
    ::::

    Wait until the model has loaded and the server is ready to accept requests.

2.  On another terminal on the same machine, run the benchmark:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # Connect to the container
        docker exec -it test bash

        # Wait for the server to start
        until curl -s http://localhost:8000/v1/models; do sleep 30; done

        # Run the benchmark
        model=Qwen/Qwen3-235B-A22B-FP8
        max_concurrency=1
        num_prompts=10
        in=128
        out=128
        vllm bench serve --model $model \
            --percentile-metrics "ttft,tpot,itl,e2el" \
            --dataset-name random \
            --ignore-eos \
            --max-concurrency $max_concurrency \
            --num-prompts $num_prompts \
            --random-input-len $in \
            --random-output-len $out \
            --trust-remote-code \
            --save-result \
            --result-filename ${model}_serving.json
    :::
    ::::

::::: {.admonition .note}
Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B, try adding [`export`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre} to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:::: {.highlight-default .notranslate}
::: highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token
:::
::::
:::::

`<style>
mjx-container[jax="CHTML"][display="true"] {
   text-align: left;
   margin: 0;
}
</style>`{=html}

::: {.admonition .note}
Note

Throughput is calculated as:

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  :::

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  :::
:::
::::::::::::
::::::::::::::
:::::::::::::::

::::::::::::::: {.model-doc .pyt-vllm-phi-4 .docutils .container}
:::::::::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to Phi-4. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  On the host machine, use this command to run the performance benchmark test on the [Phi-4](https://huggingface.co/microsoft/phi-4){.reference .external} model using one node with the [`float16`{.docutils .literal .notranslate}]{.pre} data type.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_vllm_phi-4 \
            --keep-model-dir \
            --live-output
    :::
    ::::

MAD launches a Docker container with the name [`container_ci-pyt_vllm_phi-4`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_vllm_phi-4_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_vllm_phi-4_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-930){.reference .internal} are preconfigured to collect offline throughput and online serving performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
:::

Standalone benchmarking

:::::::::::: {.sd-tab-content .docutils}
The following commands are optimized for Phi-4. See [[Supported models]{.std .std-ref}](#vllm-benchmark-supported-models-930){.reference .internal} to switch to another available model.

::: {.admonition .seealso}
See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs){.reference .external} in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs){.reference .external} for descriptions of available configuration options and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md){.reference .external} for additional benchmarking information.
:::

Launch the container

You can run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm7.0.0_vllm_0.10.2_20251006/images/sha256-94fd001964e1cf55c3224a445b1fb5be31a7dac302315255db8422d813edd7f5){.reference .external} as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
    docker run -it \
        --device=/dev/kfd \
        --device=/dev/dri \
        --group-add video \
        --shm-size 16G \
        --security-opt seccomp=unconfined \
        --security-opt apparmor=unconfined \
        --cap-add=SYS_PTRACE \
        -v $(pwd):/workspace \
        --env HUGGINGFACE_HUB_CACHE=/workspace \
        --name test \
        rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006
:::
::::

Throughput command

Use the following command to start the throughput benchmark.

:::: {.highlight-shell .notranslate}
::: highlight
    model=microsoft/phi-4
    tp=1
    num_prompts=1024
    in=128
    out=128
    dtype=auto
    kv_cache_dtype=auto
    max_num_seqs=1024
    max_num_batched_tokens=16384
    max_model_len=8192

    vllm bench throughput --model $model \
        -tp $tp \
        --num-prompts $num_prompts \
        --input-len $in \
        --output-len $out \
        --dtype $dtype \
        --kv-cache-dtype $kv_cache_dtype \
        --max-num-seqs $max_num_seqs \
        --max-num-batched-tokens $max_num_batched_tokens \
        --max-model-len $max_model_len \
        --trust-remote-code \
        --output-json ${model}_throughput.json \
        --gpu-memory-utilization 0.9
:::
::::

Serving command

1.  Start the server using the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        model=microsoft/phi-4
        tp=1
        dtype=auto
        kv_cache_dtype=auto
        max_num_seqs=256
        max_num_batched_tokens=16384
        max_model_len=8192

        vllm serve $model \
            -tp $tp \
            --dtype $dtype \
            --kv-cache-dtype $kv_cache_dtype \
            --max-num-seqs $max_num_seqs \
            --max-num-batched-tokens $max_num_batched_tokens \
            --max-model-len $max_model_len \
            --no-enable-prefix-caching \
            --swap-space 16 \
            --disable-log-requests \
            --trust-remote-code \
            --gpu-memory-utilization 0.9
    :::
    ::::

    Wait until the model has loaded and the server is ready to accept requests.

2.  On another terminal on the same machine, run the benchmark:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # Connect to the container
        docker exec -it test bash

        # Wait for the server to start
        until curl -s http://localhost:8000/v1/models; do sleep 30; done

        # Run the benchmark
        model=microsoft/phi-4
        max_concurrency=1
        num_prompts=10
        in=128
        out=128
        vllm bench serve --model $model \
            --percentile-metrics "ttft,tpot,itl,e2el" \
            --dataset-name random \
            --ignore-eos \
            --max-concurrency $max_concurrency \
            --num-prompts $num_prompts \
            --random-input-len $in \
            --random-output-len $out \
            --trust-remote-code \
            --save-result \
            --result-filename ${model}_serving.json
    :::
    ::::

::::: {.admonition .note}
Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B, try adding [`export`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`VLLM_ROCM_USE_AITER=1`{.docutils .literal .notranslate}]{.pre} to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:::: {.highlight-default .notranslate}
::: highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token
:::
::::
:::::

`<style>
mjx-container[jax="CHTML"][display="true"] {
   text-align: left;
   margin: 0;
}
</style>`{=html}

::: {.admonition .note}
Note

Throughput is calculated as:

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  :::

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  :::
:::
::::::::::::
::::::::::::::
:::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::: {#advanced-usage .section}
## Advanced usage[\#](#advanced-usage "Link to this heading"){.headerlink}

For information on experimental features and known issues related to ROCm optimization efforts on vLLM, see the developer's guide at [ROCm/vllm](https://github.com/ROCm/vllm/blob/documentation/docs/dev-docker/README.md){.github .reference .external}.

::: {#reproducing-the-docker-image .section}
### Reproducing the Docker image[\#](#reproducing-the-docker-image "Link to this heading"){.headerlink}

To reproduce this ROCm-enabled vLLM Docker image release, follow these steps:

1.  Clone the [vLLM repository](https://github.com/vllm-project/vllm){.reference .external}.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/vllm-project/vllm.git
        cd vllm
    :::
    ::::

2.  Use the following command to build the image directly from the specified commit.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker build -f docker/Dockerfile.rocm \
            --build-arg REMOTE_VLLM=1 \
            --build-arg VLLM_REPO=https://github.com/ROCm/vllm \
            --build-arg VLLM_BRANCH="790d22168820507f3105fef29596549378cfe399" \
            -t vllm-rocm .
    :::
    ::::

    ::: {.admonition .tip}
    Tip

    Replace [`vllm-rocm`{.docutils .literal .notranslate}]{.pre} with your desired image tag.
    :::
:::
::::

::: {#further-reading .section}
## Further reading[\#](#further-reading "Link to this heading"){.headerlink}

- To learn more about the options for latency and throughput benchmark scripts, see [ROCm/vllm](https://github.com/ROCm/vllm/tree/main/benchmarks){.github .reference .external}.

- To learn more about MAD and the [`madengine`{.docutils .literal .notranslate}]{.pre} CLI, see the [MAD usage guide](https://github.com/ROCm/MAD?tab=readme-ov-file#usage-guide){.reference .external}.

- To learn more about system settings and management practices to configure your system for AMD Instinct MI300X Series GPUs, see [AMD Instinct MI300X system optimization](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi300x.html){.reference .external}.

- See [[vLLM inference]{.std .std-ref}](../../llm-inference-frameworks.html#fine-tuning-llms-vllm){.reference .internal} and [[vLLM V1 performance optimization]{.std .std-ref}](../../../inference-optimization/vllm-optimization.html#mi300x-vllm-optimization){.reference .internal} for a brief introduction to vLLM and optimization strategies.

- For application performance optimization strategies for HPC and AI workloads, including inference with vLLM, see [[AMD Instinct MI300X workload optimization]{.doc}](../../../inference-optimization/workload.html){.reference .internal}.

- For a list of other ready-made Docker images for AI with ROCm, see [AMD Infinity Hub](https://www.amd.com/en/developer/resources/infinity-hub.html#f-amd_hub_category=AI%20%26%20ML%20Models){.reference .external}.
:::

::: {#previous-versions .section}
## Previous versions[\#](#previous-versions "Link to this heading"){.headerlink}

See [[vLLM inference performance testing version history]{.doc}](vllm-history.html){.reference .internal} to find documentation for previous releases of the [`ROCm/vllm`{.docutils .literal .notranslate}]{.pre} Docker image.
:::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: prev-next-area
:::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::: {.bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {.page-toc .tocsection .onthispage}
Contents
:::

- [What's new](#what-s-new){.reference .internal .nav-link}
- [Supported models](#supported-models){.reference .internal .nav-link}
- [Performance measurements](#performance-measurements){.reference .internal .nav-link}
- [System validation](#system-validation){.reference .internal .nav-link}
- [Pull the Docker image](#pull-the-docker-image){.reference .internal .nav-link}
- [Benchmarking](#benchmarking){.reference .internal .nav-link}
- [Advanced usage](#advanced-usage){.reference .internal .nav-link}
  - [Reproducing the Docker image](#reproducing-the-docker-image){.reference .internal .nav-link}
- [Further reading](#further-reading){.reference .internal .nav-link}
- [Previous versions](#previous-versions){.reference .internal .nav-link}
::::
:::::
::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
