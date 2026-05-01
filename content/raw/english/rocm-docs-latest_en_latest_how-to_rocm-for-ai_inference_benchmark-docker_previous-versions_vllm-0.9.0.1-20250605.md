---
title: "vLLM inference performance testing"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference/benchmark-docker/previous-versions/vllm-0.9.0.1-20250605.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T06:57:07.335727+00:00
content_hash: "b837c8e9da72f75f"
---

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
{#main-content .bd-main role="main"}

sbt-scroll-pixel-helper

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
bd-content
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
bd-article-container
:::::::
{.bd-header-article .d-print-none}
::::::
{.header-article-items .header-article__inner}
::
header-article-items__start

header-article-item
[]{.fa-solid .fa-angle-right}

header-article-item

::

::
header-article-items__end
:
header-article-item

article-header-buttons
[]{.fa-solid .fa-list}

:
::
::::::
:::::::

{#jb-print-docs-body .onlyprint}
# vLLM inference performance testing

::
{#print-main-content}
:
{#jb-print-toc}

{}
## Contents

:
::

{#searchbox}

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
{#vllm-inference-performance-testing .section}
# vLLM inference performance testing[\#](#vllm-inference-performance-testing "Link to this heading"){.headerlink}

::::::::
{#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::
{.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::
{.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::
{.sd-container-fluid .sd-sphinx-override .docutils}
::::
{.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}

{.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-04-21

{.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 74 min read time

{.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils style="color:gray;"}
Applies to Linux

{.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}

::::
:::::
::::::
:::::::
::::::::

{.admonition .caution}
Caution

This documentation does not reflect the latest version of ROCm vLLM inference performance documentation. See [[vLLM inference]{.doc}](../vllm.html){.reference .internal} for the latest version.

The [ROCm vLLM Docker](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.9.0.1_20250605/images/sha256-f48beeb3d72663a93c77211eb45273d564451447c097e060befa713d565fa36c){.reference .external} image offers a prebuilt, optimized environment for validating large language model (LLM) inference performance on AMD Instinct™ MI300X Series GPUs. This ROCm vLLM Docker image integrates vLLM and PyTorch tailored specifically for MI300X Series GPUs and includes the following components:

- [ROCm 6.4.1](https://github.com/ROCm/ROCm){.reference .external}

- [vLLM 0.9.0.1 (0.9.0.2.dev108+g71faa1880.rocm641)](https://docs.vllm.ai/en/latest){.reference .external}

- [PyTorch 2.7.0+gitf717b2a](https://github.com/ROCm/pytorch.git){.reference .external}

- [hipBLASLt 0.15](https://github.com/ROCm/hipBLASLt){.reference .external}

With this Docker image, you can quickly test the [[expected inference performance numbers]{.std .std-ref}](#vllm-benchmark-performance-measurements-v0901-20250605){.reference .internal} for MI300X Series GPUs.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
{#supported-models .section}
[]{#vllm-benchmark-available-models-v0901-20250605}

## Supported models[\#](#supported-models "Link to this heading"){.headerlink}

The following models are supported for inference performance benchmarking with vLLM and ROCm. Some instructions, commands, and recommendations in this documentation might vary by model -- select one to get started.

::::::::::::::::::::::::::::::::::::::::
{#vllm-benchmark-ud-params-picker .container-fluid}
:::::::::::
row

{.col-2 .me-2 .model-param-head}
Model group

:::::::::
{.row .col-10}

{.col-3 .model-param param-k="model-group" param-v="llama" tabindex="0"}
Meta Llama

{.col-3 .model-param param-k="model-group" param-v="mistral" tabindex="0"}
Mistral AI

{.col-3 .model-param param-k="model-group" param-v="qwen" tabindex="0"}
Qwen

{.col-3 .model-param param-k="model-group" param-v="dbrx" tabindex="0"}
Databricks DBRX

{.col-3 .model-param param-k="model-group" param-v="gemma" tabindex="0"}
Google Gemma

{.col-3 .model-param param-k="model-group" param-v="cohere" tabindex="0"}
Cohere

{.col-3 .model-param param-k="model-group" param-v="deepseek" tabindex="0"}
DeepSeek

{.col-3 .model-param param-k="model-group" param-v="phi" tabindex="0"}
Microsoft Phi

{.col-3 .model-param param-k="model-group" param-v="falcon" tabindex="0"}
TII Falcon

:::::::::
:::::::::::

:::::::::::::::::::::::::::
{.row .mt-1}

{.col-2 .me-2 .model-param-head}
Model

:::::::::::::::::::::::::
{.row .col-10}

{.col-6 .model-param param-group="llama" param-k="model" param-v="pyt_vllm_llama-3.1-8b" tabindex="0"}
Llama 3.1 8B

{.col-6 .model-param param-group="llama" param-k="model" param-v="pyt_vllm_llama-3.1-70b" tabindex="0"}
Llama 3.1 70B

{.col-6 .model-param param-group="llama" param-k="model" param-v="pyt_vllm_llama-3.1-405b" tabindex="0"}
Llama 3.1 405B

{.col-6 .model-param param-group="llama" param-k="model" param-v="pyt_vllm_llama-2-7b" tabindex="0"}
Llama 2 7B

{.col-6 .model-param param-group="llama" param-k="model" param-v="pyt_vllm_llama-2-70b" tabindex="0"}
Llama 2 70B

{.col-6 .model-param param-group="llama" param-k="model" param-v="pyt_vllm_llama-3.1-8b_fp8" tabindex="0"}
Llama 3.1 8B FP8

{.col-6 .model-param param-group="llama" param-k="model" param-v="pyt_vllm_llama-3.1-70b_fp8" tabindex="0"}
Llama 3.1 70B FP8

{.col-6 .model-param param-group="llama" param-k="model" param-v="pyt_vllm_llama-3.1-405b_fp8" tabindex="0"}
Llama 3.1 405B FP8

{.col-4 .model-param param-group="mistral" param-k="model" param-v="pyt_vllm_mixtral-8x7b" tabindex="0"}
Mixtral MoE 8x7B

{.col-4 .model-param param-group="mistral" param-k="model" param-v="pyt_vllm_mixtral-8x22b" tabindex="0"}
Mixtral MoE 8x22B

{.col-4 .model-param param-group="mistral" param-k="model" param-v="pyt_vllm_mistral-7b" tabindex="0"}
Mistral 7B

{.col-4 .model-param param-group="mistral" param-k="model" param-v="pyt_vllm_mixtral-8x7b_fp8" tabindex="0"}
Mixtral MoE 8x7B FP8

{.col-4 .model-param param-group="mistral" param-k="model" param-v="pyt_vllm_mixtral-8x22b_fp8" tabindex="0"}
Mixtral MoE 8x22B FP8

{.col-4 .model-param param-group="mistral" param-k="model" param-v="pyt_vllm_mistral-7b_fp8" tabindex="0"}
Mistral 7B FP8

{.col-4 .model-param param-group="qwen" param-k="model" param-v="pyt_vllm_qwen2-7b" tabindex="0"}
Qwen2 7B

{.col-4 .model-param param-group="qwen" param-k="model" param-v="pyt_vllm_qwen2-72b" tabindex="0"}
Qwen2 72B

{.col-4 .model-param param-group="qwen" param-k="model" param-v="pyt_vllm_qwq-32b" tabindex="0"}
QwQ-32B

{.col-6 .model-param param-group="dbrx" param-k="model" param-v="pyt_vllm_dbrx-instruct" tabindex="0"}
DBRX Instruct

{.col-6 .model-param param-group="dbrx" param-k="model" param-v="pyt_vllm_dbrx_fp8" tabindex="0"}
DBRX Instruct FP8

{.col-6 .model-param param-group="gemma" param-k="model" param-v="pyt_vllm_gemma-2-27b" tabindex="0"}
Gemma 2 27B

{.col-6 .model-param param-group="cohere" param-k="model" param-v="pyt_vllm_c4ai-command-r-plus-08-2024" tabindex="0"}
C4AI Command R+ 08-2024

{.col-6 .model-param param-group="cohere" param-k="model" param-v="pyt_vllm_command-r-plus_fp8" tabindex="0"}
C4AI Command R+ 08-2024 FP8

{.col-6 .model-param param-group="deepseek" param-k="model" param-v="pyt_vllm_deepseek-moe-16b-chat" tabindex="0"}
DeepSeek MoE 16B

{.col-6 .model-param param-group="phi" param-k="model" param-v="pyt_vllm_phi-4" tabindex="0"}
Phi-4

{.col-6 .model-param param-group="falcon" param-k="model" param-v="pyt_vllm_falcon-180b" tabindex="0"}
Falcon 180B

:::::::::::::::::::::::::
:::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::

:
{#vllm-benchmark-vllm .model-doc .pyt-vllm-llama-3-1-8b .docutils .container}

{.admonition .note}
Note

See the [Llama 3.1 8B model card on Hugging Face](https://huggingface.co/meta-llama/Llama-3.1-8B){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.

:

:
{.model-doc .pyt-vllm-llama-3-1-70b .docutils .container}

{.admonition .note}
Note

See the [Llama 3.1 70B model card on Hugging Face](https://huggingface.co/meta-llama/Llama-3.1-70B-Instruct){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.

:

:
{.model-doc .pyt-vllm-llama-3-1-405b .docutils .container}

{.admonition .note}
Note

See the [Llama 3.1 405B model card on Hugging Face](https://huggingface.co/meta-llama/Llama-3.1-405B-Instruct){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.

:

:
{.model-doc .pyt-vllm-llama-2-7b .docutils .container}

{.admonition .note}
Note

See the [Llama 2 7B model card on Hugging Face](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.

:

:
{.model-doc .pyt-vllm-llama-2-70b .docutils .container}

{.admonition .note}
Note

See the [Llama 2 70B model card on Hugging Face](https://huggingface.co/meta-llama/Llama-2-70b-chat-hf){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.

:

:
{.model-doc .pyt-vllm-llama-3-1-8b-fp8 .docutils .container}

{.admonition .note}
Note

See the [Llama 3.1 8B FP8 model card on Hugging Face](https://huggingface.co/amd/Llama-3.1-8B-Instruct-FP8-KV){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.

:

:
{.model-doc .pyt-vllm-llama-3-1-70b-fp8 .docutils .container}

{.admonition .note}
Note

See the [Llama 3.1 70B FP8 model card on Hugging Face](https://huggingface.co/amd/Llama-3.1-70B-Instruct-FP8-KV){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.

:

:
{.model-doc .pyt-vllm-llama-3-1-405b-fp8 .docutils .container}

{.admonition .note}
Note

See the [Llama 3.1 405B FP8 model card on Hugging Face](https://huggingface.co/amd/Llama-3.1-405B-Instruct-FP8-KV){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.

:

:
{.model-doc .pyt-vllm-mixtral-8x7b .docutils .container}

{.admonition .note}
Note

See the [Mixtral MoE 8x7B model card on Hugging Face](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.

:

:
{.model-doc .pyt-vllm-mixtral-8x22b .docutils .container}

{.admonition .note}
Note

See the [Mixtral MoE 8x22B model card on Hugging Face](https://huggingface.co/mistralai/Mixtral-8x22B-Instruct-v0.1){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.

:

:
{.model-doc .pyt-vllm-mistral-7b .docutils .container}

{.admonition .note}
Note

See the [Mistral 7B model card on Hugging Face](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.

:

:
{.model-doc .pyt-vllm-mixtral-8x7b-fp8 .docutils .container}

{.admonition .note}
Note

See the [Mixtral MoE 8x7B FP8 model card on Hugging Face](https://huggingface.co/amd/Mixtral-8x7B-Instruct-v0.1-FP8-KV){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.

:

:
{.model-doc .pyt-vllm-mixtral-8x22b-fp8 .docutils .container}

{.admonition .note}
Note

See the [Mixtral MoE 8x22B FP8 model card on Hugging Face](https://huggingface.co/amd/Mixtral-8x22B-Instruct-v0.1-FP8-KV){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.

:

:
{.model-doc .pyt-vllm-mistral-7b-fp8 .docutils .container}

{.admonition .note}
Note

See the [Mistral 7B FP8 model card on Hugging Face](https://huggingface.co/amd/Mistral-7B-v0.1-FP8-KV){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.

:

:
{.model-doc .pyt-vllm-qwen2-7b .docutils .container}

{.admonition .note}
Note

See the [Qwen2 7B model card on Hugging Face](https://huggingface.co/Qwen/Qwen2-7B-Instruct){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.

:

:
{.model-doc .pyt-vllm-qwen2-72b .docutils .container}

{.admonition .note}
Note

See the [Qwen2 72B model card on Hugging Face](https://huggingface.co/Qwen/Qwen2-72B-Instruct){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.

:

:
{.model-doc .pyt-vllm-qwq-32b .docutils .container}

{.admonition .note}
Note

See the [QwQ-32B model card on Hugging Face](https://huggingface.co/Qwen/QwQ-32B){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.

:

:
{.model-doc .pyt-vllm-dbrx-instruct .docutils .container}

{.admonition .note}
Note

See the [DBRX Instruct model card on Hugging Face](https://huggingface.co/databricks/dbrx-instruct){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.

:

:
{.model-doc .pyt-vllm-dbrx-fp8 .docutils .container}

{.admonition .note}
Note

See the [DBRX Instruct FP8 model card on Hugging Face](https://huggingface.co/amd/dbrx-instruct-FP8-KV){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.

:

:
{.model-doc .pyt-vllm-gemma-2-27b .docutils .container}

{.admonition .note}
Note

See the [Gemma 2 27B model card on Hugging Face](https://huggingface.co/google/gemma-2-27b){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.

:

:
{.model-doc .pyt-vllm-c4ai-command-r-plus-08-2024 .docutils .container}

{.admonition .note}
Note

See the [C4AI Command R+ 08-2024 model card on Hugging Face](https://huggingface.co/CohereForAI/c4ai-command-r-plus-08-2024){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.

:

:
{.model-doc .pyt-vllm-command-r-plus-fp8 .docutils .container}

{.admonition .note}
Note

See the [C4AI Command R+ 08-2024 FP8 model card on Hugging Face](https://huggingface.co/amd/c4ai-command-r-plus-FP8-KV){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.

:

:
{.model-doc .pyt-vllm-deepseek-moe-16b-chat .docutils .container}

{.admonition .note}
Note

See the [DeepSeek MoE 16B model card on Hugging Face](https://huggingface.co/deepseek-ai/deepseek-moe-16b-chat){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.

:

:
{.model-doc .pyt-vllm-phi-4 .docutils .container}

{.admonition .note}
Note

See the [Phi-4 model card on Hugging Face](https://huggingface.co/microsoft/phi-4){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.

:

:
{.model-doc .pyt-vllm-falcon-180b .docutils .container}

{.admonition .note}
Note

See the [Falcon 180B model card on Hugging Face](https://huggingface.co/tiiuae/falcon-180B){.reference .external} to learn more about your selected model. Some models require access authorization prior to use via an external license agreement through a third party.

:

{.admonition .note}
Note

vLLM is a toolkit and library for LLM inference and serving. AMD implements high-performance custom kernels and modules in vLLM to enhance performance. See [[vLLM inference]{.std .std-ref}](../../llm-inference-frameworks.html#fine-tuning-llms-vllm){.reference .internal} and [[vLLM V1 performance optimization]{.std .std-ref}](../../../inference-optimization/vllm-optimization.html#mi300x-vllm-optimization){.reference .internal} for more information.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:
{#performance-measurements .section}
[]{#vllm-benchmark-performance-measurements-v0901-20250605}

## Performance measurements[\#](#performance-measurements "Link to this heading"){.headerlink}

To evaluate performance, the [Performance results with AMD ROCm software](https://www.amd.com/en/developer/resources/rocm-hub/dev-ai/performance-results.html){.reference .external} page provides reference throughput and latency measurements for inferencing popular AI models.

{.admonition .important}
Important

The performance data presented in [Performance results with AMD ROCm software](https://www.amd.com/en/developer/resources/rocm-hub/dev-ai/performance-results.html){.reference .external} only reflects the latest version of this inference benchmarking environment. The listed measurements should not be interpreted as the peak performance achievable by AMD Instinct MI325X and MI300X GPUs or ROCm software.

:

{#advanced-features-and-known-issues .section}
## Advanced features and known issues[\#](#advanced-features-and-known-issues "Link to this heading"){.headerlink}

For information on experimental features and known issues related to ROCm optimization efforts on vLLM, see the developer's guide at [ROCm/vllm](https://github.com/ROCm/vllm/tree/7bb0618b1fe725b7d4fad9e525aa44da12c94a8b/docs/dev-docker){.github .reference .external}.

::
{#system-validation .section}
## System validation[\#](#system-validation "Link to this heading"){.headerlink}

Before running AI workloads, it's important to validate that your AMD hardware is configured correctly and performing optimally.

To optimize performance, disable automatic NUMA balancing. Otherwise, the GPU might hang until the periodic balancing is finalized. For more information, see the [[system validation steps]{.std .std-ref}](../../../system-setup/prerequisite-system-validation.html#rocm-for-ai-system-optimization){.reference .internal}.

:
{.highlight-shell .notranslate}

highlight
    # disable automatic NUMA balancing
    sh -c 'echo 0 > /proc/sys/kernel/numa_balancing'
    # check if NUMA balancing is disabled (returns 0 if disabled)
    cat /proc/sys/kernel/numa_balancing
    0

:

To test for optimal performance, consult the recommended [[System health benchmarks]{.std .std-ref}](../../../system-setup/system-health-check.html#rocm-for-ai-system-health-bench){.reference .internal}. This suite of tests will help you verify and fine-tune your system's configuration.
::

::
{#pull-the-docker-image .section}
## Pull the Docker image[\#](#pull-the-docker-image "Link to this heading"){.headerlink}

Download the [ROCm vLLM Docker image](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.9.0.1_20250605/images/sha256-f48beeb3d72663a93c77211eb45273d564451447c097e060befa713d565fa36c){.reference .external}. Use the following command to pull the Docker image from Docker Hub.

:
{.highlight-shell .notranslate}

highlight
    docker pull rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605

:
::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
{#benchmarking .section}
## Benchmarking[\#](#benchmarking "Link to this heading"){.headerlink}

Once the setup is complete, choose between two options to reproduce the benchmark results:

:::::::::::::::::::
{#vllm-benchmark-mad .model-doc .pyt-vllm-llama-3-1-8b .docutils .container}
::::::::::::::::::
{.sd-tab-set .docutils}
MAD-integrated benchmarking

::::
{.sd-tab-content .docutils}
Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

:
{.highlight-shell .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD
    pip install -r requirements.txt

:

Use this command to run the performance benchmark test on the [Llama 3.1 8B](https://huggingface.co/meta-llama/Llama-3.1-8B){.reference .external} model using one GPU with the [`float16`{.docutils .literal .notranslate}]{.pre} data type on the host machine.

:
{.highlight-shell .notranslate}

highlight
    export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
    python3 tools/run_models.py --tags pyt_vllm_llama-3.1-8b --keep-model-dir --live-output --timeout 28800

:

MAD launches a Docker container with the name [`container_ci-pyt_vllm_llama-3.1-8b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in the following path: [`~/MAD/reports_float16/`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-v0901-20250605){.reference .internal} are preconfigured to collect latency and throughput performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
::::

Standalone benchmarking

::::::::::::
{.sd-tab-content .docutils}
Run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.9.0.1_20250605/images/sha256-f48beeb3d72663a93c77211eb45273d564451447c097e060befa713d565fa36c){.reference .external} as shown in the following snippet.

:
{.highlight-default .notranslate}

highlight
    docker pull rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605
    docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --shm-size 16G --security-opt seccomp=unconfined --security-opt apparmor=unconfined --cap-add=SYS_PTRACE -v $(pwd):/workspace --env HUGGINGFACE_HUB_CACHE=/workspace --name test rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605

:

In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at [`~/MAD/scripts/vllm`{.docutils .literal .notranslate}]{.pre}.

:
{.highlight-default .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD/scripts/vllm

:

To start the benchmark, use the following command with the appropriate options.

:
{.highlight-default .notranslate}

highlight
    ./vllm_benchmark_report.sh -s $test_option -m meta-llama/Llama-3.1-8B-Instruct -g $num_gpu -d float16

:

pst-scrollable-table-container
  Name                                                      Options                                                                                                   Description
  --------------------------------------------------------- --------------------------------------------------------------------------------------------------------- -------------------------------------
  [`$test_option`{.docutils .literal .notranslate}]{.pre}   latency                                                                                                   Measure decoding token latency
                                                            throughput                                                                                                Measure token generation throughput
                                                            all                                                                                                       Measure both throughput and latency
  [`$num_gpu`{.docutils .literal .notranslate}]{.pre}       1 or 8                                                                                                    Number of GPUs
  [`$datatype`{.docutils .literal .notranslate}]{.pre}      [`float16`{.docutils .literal .notranslate}]{.pre} or [`float8`{.docutils .literal .notranslate}]{.pre}   Data type

{.admonition .note}
Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don't need to specify them with this script.

::
{.admonition .note}
Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:
{.highlight-default .notranslate}

highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token

:
::

Here are some examples of running the benchmark with various options.

- Latency benchmark

  Use this command to benchmark the latency of the Llama 3.1 8B model on eight GPUs with [`float16`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-default .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s latency -m meta-llama/Llama-3.1-8B-Instruct -g 8 -d float16
  
  :

  Find the latency report at [`./reports_float16_vllm_rocm6.4.1/summary/Llama-3.1-8B-Instruct_latency_report.csv`{.docutils .literal .notranslate}]{.pre}.

- Throughput benchmark

  Use this command to benchmark the throughput of the Llama 3.1 8B model on eight GPUs with [`float16`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-shell .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s throughput -m meta-llama/Llama-3.1-8B-Instruct -g 8 -d float16
  
  :

  Find the throughput report at [`./reports_float16_vllm_rocm6.4.1/summary/Llama-3.1-8B-Instruct_throughput_report.csv`{.docutils .literal .notranslate}]{.pre}.

{.admonition .note}
Note

Throughput is calculated as:

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  

::::::::::::
::::::::::::::::::
:::::::::::::::::::

:::::::::::::::::::
{.model-doc .pyt-vllm-llama-3-1-70b .docutils .container}
::::::::::::::::::
{.sd-tab-set .docutils}
MAD-integrated benchmarking

::::
{.sd-tab-content .docutils}
Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

:
{.highlight-shell .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD
    pip install -r requirements.txt

:

Use this command to run the performance benchmark test on the [Llama 3.1 70B](https://huggingface.co/meta-llama/Llama-3.1-70B-Instruct){.reference .external} model using one GPU with the [`float16`{.docutils .literal .notranslate}]{.pre} data type on the host machine.

:
{.highlight-shell .notranslate}

highlight
    export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
    python3 tools/run_models.py --tags pyt_vllm_llama-3.1-70b --keep-model-dir --live-output --timeout 28800

:

MAD launches a Docker container with the name [`container_ci-pyt_vllm_llama-3.1-70b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in the following path: [`~/MAD/reports_float16/`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-v0901-20250605){.reference .internal} are preconfigured to collect latency and throughput performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
::::

Standalone benchmarking

::::::::::::
{.sd-tab-content .docutils}
Run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.9.0.1_20250605/images/sha256-f48beeb3d72663a93c77211eb45273d564451447c097e060befa713d565fa36c){.reference .external} as shown in the following snippet.

:
{.highlight-default .notranslate}

highlight
    docker pull rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605
    docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --shm-size 16G --security-opt seccomp=unconfined --security-opt apparmor=unconfined --cap-add=SYS_PTRACE -v $(pwd):/workspace --env HUGGINGFACE_HUB_CACHE=/workspace --name test rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605

:

In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at [`~/MAD/scripts/vllm`{.docutils .literal .notranslate}]{.pre}.

:
{.highlight-default .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD/scripts/vllm

:

To start the benchmark, use the following command with the appropriate options.

:
{.highlight-default .notranslate}

highlight
    ./vllm_benchmark_report.sh -s $test_option -m meta-llama/Llama-3.1-70B-Instruct -g $num_gpu -d float16

:

pst-scrollable-table-container
  Name                                                      Options                                                                                                   Description
  --------------------------------------------------------- --------------------------------------------------------------------------------------------------------- -------------------------------------
  [`$test_option`{.docutils .literal .notranslate}]{.pre}   latency                                                                                                   Measure decoding token latency
                                                            throughput                                                                                                Measure token generation throughput
                                                            all                                                                                                       Measure both throughput and latency
  [`$num_gpu`{.docutils .literal .notranslate}]{.pre}       1 or 8                                                                                                    Number of GPUs
  [`$datatype`{.docutils .literal .notranslate}]{.pre}      [`float16`{.docutils .literal .notranslate}]{.pre} or [`float8`{.docutils .literal .notranslate}]{.pre}   Data type

{.admonition .note}
Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don't need to specify them with this script.

::
{.admonition .note}
Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:
{.highlight-default .notranslate}

highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token

:
::

Here are some examples of running the benchmark with various options.

- Latency benchmark

  Use this command to benchmark the latency of the Llama 3.1 70B model on eight GPUs with [`float16`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-default .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s latency -m meta-llama/Llama-3.1-70B-Instruct -g 8 -d float16
  
  :

  Find the latency report at [`./reports_float16_vllm_rocm6.4.1/summary/Llama-3.1-70B-Instruct_latency_report.csv`{.docutils .literal .notranslate}]{.pre}.

- Throughput benchmark

  Use this command to benchmark the throughput of the Llama 3.1 70B model on eight GPUs with [`float16`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-shell .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s throughput -m meta-llama/Llama-3.1-70B-Instruct -g 8 -d float16
  
  :

  Find the throughput report at [`./reports_float16_vllm_rocm6.4.1/summary/Llama-3.1-70B-Instruct_throughput_report.csv`{.docutils .literal .notranslate}]{.pre}.

{.admonition .note}
Note

Throughput is calculated as:

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  

::::::::::::
::::::::::::::::::
:::::::::::::::::::

:::::::::::::::::::
{.model-doc .pyt-vllm-llama-3-1-405b .docutils .container}
::::::::::::::::::
{.sd-tab-set .docutils}
MAD-integrated benchmarking

::::
{.sd-tab-content .docutils}
Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

:
{.highlight-shell .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD
    pip install -r requirements.txt

:

Use this command to run the performance benchmark test on the [Llama 3.1 405B](https://huggingface.co/meta-llama/Llama-3.1-405B-Instruct){.reference .external} model using one GPU with the [`float16`{.docutils .literal .notranslate}]{.pre} data type on the host machine.

:
{.highlight-shell .notranslate}

highlight
    export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
    python3 tools/run_models.py --tags pyt_vllm_llama-3.1-405b --keep-model-dir --live-output --timeout 28800

:

MAD launches a Docker container with the name [`container_ci-pyt_vllm_llama-3.1-405b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in the following path: [`~/MAD/reports_float16/`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-v0901-20250605){.reference .internal} are preconfigured to collect latency and throughput performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
::::

Standalone benchmarking

::::::::::::
{.sd-tab-content .docutils}
Run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.9.0.1_20250605/images/sha256-f48beeb3d72663a93c77211eb45273d564451447c097e060befa713d565fa36c){.reference .external} as shown in the following snippet.

:
{.highlight-default .notranslate}

highlight
    docker pull rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605
    docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --shm-size 16G --security-opt seccomp=unconfined --security-opt apparmor=unconfined --cap-add=SYS_PTRACE -v $(pwd):/workspace --env HUGGINGFACE_HUB_CACHE=/workspace --name test rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605

:

In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at [`~/MAD/scripts/vllm`{.docutils .literal .notranslate}]{.pre}.

:
{.highlight-default .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD/scripts/vllm

:

To start the benchmark, use the following command with the appropriate options.

:
{.highlight-default .notranslate}

highlight
    ./vllm_benchmark_report.sh -s $test_option -m meta-llama/Llama-3.1-405B-Instruct -g $num_gpu -d float16

:

pst-scrollable-table-container
  Name                                                      Options                                                                                                   Description
  --------------------------------------------------------- --------------------------------------------------------------------------------------------------------- -------------------------------------
  [`$test_option`{.docutils .literal .notranslate}]{.pre}   latency                                                                                                   Measure decoding token latency
                                                            throughput                                                                                                Measure token generation throughput
                                                            all                                                                                                       Measure both throughput and latency
  [`$num_gpu`{.docutils .literal .notranslate}]{.pre}       1 or 8                                                                                                    Number of GPUs
  [`$datatype`{.docutils .literal .notranslate}]{.pre}      [`float16`{.docutils .literal .notranslate}]{.pre} or [`float8`{.docutils .literal .notranslate}]{.pre}   Data type

{.admonition .note}
Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don't need to specify them with this script.

::
{.admonition .note}
Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:
{.highlight-default .notranslate}

highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token

:
::

Here are some examples of running the benchmark with various options.

- Latency benchmark

  Use this command to benchmark the latency of the Llama 3.1 405B model on eight GPUs with [`float16`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-default .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s latency -m meta-llama/Llama-3.1-405B-Instruct -g 8 -d float16
  
  :

  Find the latency report at [`./reports_float16_vllm_rocm6.4.1/summary/Llama-3.1-405B-Instruct_latency_report.csv`{.docutils .literal .notranslate}]{.pre}.

- Throughput benchmark

  Use this command to benchmark the throughput of the Llama 3.1 405B model on eight GPUs with [`float16`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-shell .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s throughput -m meta-llama/Llama-3.1-405B-Instruct -g 8 -d float16
  
  :

  Find the throughput report at [`./reports_float16_vllm_rocm6.4.1/summary/Llama-3.1-405B-Instruct_throughput_report.csv`{.docutils .literal .notranslate}]{.pre}.

{.admonition .note}
Note

Throughput is calculated as:

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  

::::::::::::
::::::::::::::::::
:::::::::::::::::::

:::::::::::::::::::
{.model-doc .pyt-vllm-llama-2-7b .docutils .container}
::::::::::::::::::
{.sd-tab-set .docutils}
MAD-integrated benchmarking

::::
{.sd-tab-content .docutils}
Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

:
{.highlight-shell .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD
    pip install -r requirements.txt

:

Use this command to run the performance benchmark test on the [Llama 2 7B](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf){.reference .external} model using one GPU with the [`float16`{.docutils .literal .notranslate}]{.pre} data type on the host machine.

:
{.highlight-shell .notranslate}

highlight
    export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
    python3 tools/run_models.py --tags pyt_vllm_llama-2-7b --keep-model-dir --live-output --timeout 28800

:

MAD launches a Docker container with the name [`container_ci-pyt_vllm_llama-2-7b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in the following path: [`~/MAD/reports_float16/`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-v0901-20250605){.reference .internal} are preconfigured to collect latency and throughput performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
::::

Standalone benchmarking

::::::::::::
{.sd-tab-content .docutils}
Run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.9.0.1_20250605/images/sha256-f48beeb3d72663a93c77211eb45273d564451447c097e060befa713d565fa36c){.reference .external} as shown in the following snippet.

:
{.highlight-default .notranslate}

highlight
    docker pull rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605
    docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --shm-size 16G --security-opt seccomp=unconfined --security-opt apparmor=unconfined --cap-add=SYS_PTRACE -v $(pwd):/workspace --env HUGGINGFACE_HUB_CACHE=/workspace --name test rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605

:

In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at [`~/MAD/scripts/vllm`{.docutils .literal .notranslate}]{.pre}.

:
{.highlight-default .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD/scripts/vllm

:

To start the benchmark, use the following command with the appropriate options.

:
{.highlight-default .notranslate}

highlight
    ./vllm_benchmark_report.sh -s $test_option -m meta-llama/Llama-2-7b-chat-hf -g $num_gpu -d float16

:

pst-scrollable-table-container
  Name                                                      Options                                                                                                   Description
  --------------------------------------------------------- --------------------------------------------------------------------------------------------------------- -------------------------------------
  [`$test_option`{.docutils .literal .notranslate}]{.pre}   latency                                                                                                   Measure decoding token latency
                                                            throughput                                                                                                Measure token generation throughput
                                                            all                                                                                                       Measure both throughput and latency
  [`$num_gpu`{.docutils .literal .notranslate}]{.pre}       1 or 8                                                                                                    Number of GPUs
  [`$datatype`{.docutils .literal .notranslate}]{.pre}      [`float16`{.docutils .literal .notranslate}]{.pre} or [`float8`{.docutils .literal .notranslate}]{.pre}   Data type

{.admonition .note}
Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don't need to specify them with this script.

::
{.admonition .note}
Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:
{.highlight-default .notranslate}

highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token

:
::

Here are some examples of running the benchmark with various options.

- Latency benchmark

  Use this command to benchmark the latency of the Llama 2 7B model on eight GPUs with [`float16`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-default .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s latency -m meta-llama/Llama-2-7b-chat-hf -g 8 -d float16
  
  :

  Find the latency report at [`./reports_float16_vllm_rocm6.4.1/summary/Llama-2-7b-chat-hf_latency_report.csv`{.docutils .literal .notranslate}]{.pre}.

- Throughput benchmark

  Use this command to benchmark the throughput of the Llama 2 7B model on eight GPUs with [`float16`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-shell .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s throughput -m meta-llama/Llama-2-7b-chat-hf -g 8 -d float16
  
  :

  Find the throughput report at [`./reports_float16_vllm_rocm6.4.1/summary/Llama-2-7b-chat-hf_throughput_report.csv`{.docutils .literal .notranslate}]{.pre}.

{.admonition .note}
Note

Throughput is calculated as:

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  

::::::::::::
::::::::::::::::::
:::::::::::::::::::

:::::::::::::::::::
{.model-doc .pyt-vllm-llama-2-70b .docutils .container}
::::::::::::::::::
{.sd-tab-set .docutils}
MAD-integrated benchmarking

::::
{.sd-tab-content .docutils}
Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

:
{.highlight-shell .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD
    pip install -r requirements.txt

:

Use this command to run the performance benchmark test on the [Llama 2 70B](https://huggingface.co/meta-llama/Llama-2-70b-chat-hf){.reference .external} model using one GPU with the [`float16`{.docutils .literal .notranslate}]{.pre} data type on the host machine.

:
{.highlight-shell .notranslate}

highlight
    export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
    python3 tools/run_models.py --tags pyt_vllm_llama-2-70b --keep-model-dir --live-output --timeout 28800

:

MAD launches a Docker container with the name [`container_ci-pyt_vllm_llama-2-70b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in the following path: [`~/MAD/reports_float16/`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-v0901-20250605){.reference .internal} are preconfigured to collect latency and throughput performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
::::

Standalone benchmarking

::::::::::::
{.sd-tab-content .docutils}
Run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.9.0.1_20250605/images/sha256-f48beeb3d72663a93c77211eb45273d564451447c097e060befa713d565fa36c){.reference .external} as shown in the following snippet.

:
{.highlight-default .notranslate}

highlight
    docker pull rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605
    docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --shm-size 16G --security-opt seccomp=unconfined --security-opt apparmor=unconfined --cap-add=SYS_PTRACE -v $(pwd):/workspace --env HUGGINGFACE_HUB_CACHE=/workspace --name test rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605

:

In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at [`~/MAD/scripts/vllm`{.docutils .literal .notranslate}]{.pre}.

:
{.highlight-default .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD/scripts/vllm

:

To start the benchmark, use the following command with the appropriate options.

:
{.highlight-default .notranslate}

highlight
    ./vllm_benchmark_report.sh -s $test_option -m meta-llama/Llama-2-70b-chat-hf -g $num_gpu -d float16

:

pst-scrollable-table-container
  Name                                                      Options                                                                                                   Description
  --------------------------------------------------------- --------------------------------------------------------------------------------------------------------- -------------------------------------
  [`$test_option`{.docutils .literal .notranslate}]{.pre}   latency                                                                                                   Measure decoding token latency
                                                            throughput                                                                                                Measure token generation throughput
                                                            all                                                                                                       Measure both throughput and latency
  [`$num_gpu`{.docutils .literal .notranslate}]{.pre}       1 or 8                                                                                                    Number of GPUs
  [`$datatype`{.docutils .literal .notranslate}]{.pre}      [`float16`{.docutils .literal .notranslate}]{.pre} or [`float8`{.docutils .literal .notranslate}]{.pre}   Data type

{.admonition .note}
Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don't need to specify them with this script.

::
{.admonition .note}
Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:
{.highlight-default .notranslate}

highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token

:
::

Here are some examples of running the benchmark with various options.

- Latency benchmark

  Use this command to benchmark the latency of the Llama 2 70B model on eight GPUs with [`float16`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-default .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s latency -m meta-llama/Llama-2-70b-chat-hf -g 8 -d float16
  
  :

  Find the latency report at [`./reports_float16_vllm_rocm6.4.1/summary/Llama-2-70b-chat-hf_latency_report.csv`{.docutils .literal .notranslate}]{.pre}.

- Throughput benchmark

  Use this command to benchmark the throughput of the Llama 2 70B model on eight GPUs with [`float16`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-shell .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s throughput -m meta-llama/Llama-2-70b-chat-hf -g 8 -d float16
  
  :

  Find the throughput report at [`./reports_float16_vllm_rocm6.4.1/summary/Llama-2-70b-chat-hf_throughput_report.csv`{.docutils .literal .notranslate}]{.pre}.

{.admonition .note}
Note

Throughput is calculated as:

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  

::::::::::::
::::::::::::::::::
:::::::::::::::::::

:::::::::::::::::::
{.model-doc .pyt-vllm-llama-3-1-8b-fp8 .docutils .container}
::::::::::::::::::
{.sd-tab-set .docutils}
MAD-integrated benchmarking

::::
{.sd-tab-content .docutils}
Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

:
{.highlight-shell .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD
    pip install -r requirements.txt

:

Use this command to run the performance benchmark test on the [Llama 3.1 8B FP8](https://huggingface.co/amd/Llama-3.1-8B-Instruct-FP8-KV){.reference .external} model using one GPU with the [`float8`{.docutils .literal .notranslate}]{.pre} data type on the host machine.

:
{.highlight-shell .notranslate}

highlight
    export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
    python3 tools/run_models.py --tags pyt_vllm_llama-3.1-8b_fp8 --keep-model-dir --live-output --timeout 28800

:

MAD launches a Docker container with the name [`container_ci-pyt_vllm_llama-3.1-8b_fp8`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in the following path: [`~/MAD/reports_float8/`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-v0901-20250605){.reference .internal} are preconfigured to collect latency and throughput performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
::::

Standalone benchmarking

::::::::::::
{.sd-tab-content .docutils}
Run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.9.0.1_20250605/images/sha256-f48beeb3d72663a93c77211eb45273d564451447c097e060befa713d565fa36c){.reference .external} as shown in the following snippet.

:
{.highlight-default .notranslate}

highlight
    docker pull rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605
    docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --shm-size 16G --security-opt seccomp=unconfined --security-opt apparmor=unconfined --cap-add=SYS_PTRACE -v $(pwd):/workspace --env HUGGINGFACE_HUB_CACHE=/workspace --name test rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605

:

In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at [`~/MAD/scripts/vllm`{.docutils .literal .notranslate}]{.pre}.

:
{.highlight-default .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD/scripts/vllm

:

To start the benchmark, use the following command with the appropriate options.

:
{.highlight-default .notranslate}

highlight
    ./vllm_benchmark_report.sh -s $test_option -m amd/Llama-3.1-8B-Instruct-FP8-KV -g $num_gpu -d float8

:

pst-scrollable-table-container
  Name                                                      Options                                                                                                   Description
  --------------------------------------------------------- --------------------------------------------------------------------------------------------------------- -------------------------------------
  [`$test_option`{.docutils .literal .notranslate}]{.pre}   latency                                                                                                   Measure decoding token latency
                                                            throughput                                                                                                Measure token generation throughput
                                                            all                                                                                                       Measure both throughput and latency
  [`$num_gpu`{.docutils .literal .notranslate}]{.pre}       1 or 8                                                                                                    Number of GPUs
  [`$datatype`{.docutils .literal .notranslate}]{.pre}      [`float16`{.docutils .literal .notranslate}]{.pre} or [`float8`{.docutils .literal .notranslate}]{.pre}   Data type

{.admonition .note}
Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don't need to specify them with this script.

::
{.admonition .note}
Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:
{.highlight-default .notranslate}

highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token

:
::

Here are some examples of running the benchmark with various options.

- Latency benchmark

  Use this command to benchmark the latency of the Llama 3.1 8B FP8 model on eight GPUs with [`float8`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-default .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s latency -m amd/Llama-3.1-8B-Instruct-FP8-KV -g 8 -d float8
  
  :

  Find the latency report at [`./reports_float8_vllm_rocm6.4.1/summary/Llama-3.1-8B-Instruct-FP8-KV_latency_report.csv`{.docutils .literal .notranslate}]{.pre}.

- Throughput benchmark

  Use this command to benchmark the throughput of the Llama 3.1 8B FP8 model on eight GPUs with [`float8`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-shell .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s throughput -m amd/Llama-3.1-8B-Instruct-FP8-KV -g 8 -d float8
  
  :

  Find the throughput report at [`./reports_float8_vllm_rocm6.4.1/summary/Llama-3.1-8B-Instruct-FP8-KV_throughput_report.csv`{.docutils .literal .notranslate}]{.pre}.

{.admonition .note}
Note

Throughput is calculated as:

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  

::::::::::::
::::::::::::::::::
:::::::::::::::::::

:::::::::::::::::::
{.model-doc .pyt-vllm-llama-3-1-70b-fp8 .docutils .container}
::::::::::::::::::
{.sd-tab-set .docutils}
MAD-integrated benchmarking

::::
{.sd-tab-content .docutils}
Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

:
{.highlight-shell .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD
    pip install -r requirements.txt

:

Use this command to run the performance benchmark test on the [Llama 3.1 70B FP8](https://huggingface.co/amd/Llama-3.1-70B-Instruct-FP8-KV){.reference .external} model using one GPU with the [`float8`{.docutils .literal .notranslate}]{.pre} data type on the host machine.

:
{.highlight-shell .notranslate}

highlight
    export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
    python3 tools/run_models.py --tags pyt_vllm_llama-3.1-70b_fp8 --keep-model-dir --live-output --timeout 28800

:

MAD launches a Docker container with the name [`container_ci-pyt_vllm_llama-3.1-70b_fp8`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in the following path: [`~/MAD/reports_float8/`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-v0901-20250605){.reference .internal} are preconfigured to collect latency and throughput performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
::::

Standalone benchmarking

::::::::::::
{.sd-tab-content .docutils}
Run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.9.0.1_20250605/images/sha256-f48beeb3d72663a93c77211eb45273d564451447c097e060befa713d565fa36c){.reference .external} as shown in the following snippet.

:
{.highlight-default .notranslate}

highlight
    docker pull rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605
    docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --shm-size 16G --security-opt seccomp=unconfined --security-opt apparmor=unconfined --cap-add=SYS_PTRACE -v $(pwd):/workspace --env HUGGINGFACE_HUB_CACHE=/workspace --name test rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605

:

In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at [`~/MAD/scripts/vllm`{.docutils .literal .notranslate}]{.pre}.

:
{.highlight-default .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD/scripts/vllm

:

To start the benchmark, use the following command with the appropriate options.

:
{.highlight-default .notranslate}

highlight
    ./vllm_benchmark_report.sh -s $test_option -m amd/Llama-3.1-70B-Instruct-FP8-KV -g $num_gpu -d float8

:

pst-scrollable-table-container
  Name                                                      Options                                                                                                   Description
  --------------------------------------------------------- --------------------------------------------------------------------------------------------------------- -------------------------------------
  [`$test_option`{.docutils .literal .notranslate}]{.pre}   latency                                                                                                   Measure decoding token latency
                                                            throughput                                                                                                Measure token generation throughput
                                                            all                                                                                                       Measure both throughput and latency
  [`$num_gpu`{.docutils .literal .notranslate}]{.pre}       1 or 8                                                                                                    Number of GPUs
  [`$datatype`{.docutils .literal .notranslate}]{.pre}      [`float16`{.docutils .literal .notranslate}]{.pre} or [`float8`{.docutils .literal .notranslate}]{.pre}   Data type

{.admonition .note}
Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don't need to specify them with this script.

::
{.admonition .note}
Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:
{.highlight-default .notranslate}

highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token

:
::

Here are some examples of running the benchmark with various options.

- Latency benchmark

  Use this command to benchmark the latency of the Llama 3.1 70B FP8 model on eight GPUs with [`float8`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-default .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s latency -m amd/Llama-3.1-70B-Instruct-FP8-KV -g 8 -d float8
  
  :

  Find the latency report at [`./reports_float8_vllm_rocm6.4.1/summary/Llama-3.1-70B-Instruct-FP8-KV_latency_report.csv`{.docutils .literal .notranslate}]{.pre}.

- Throughput benchmark

  Use this command to benchmark the throughput of the Llama 3.1 70B FP8 model on eight GPUs with [`float8`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-shell .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s throughput -m amd/Llama-3.1-70B-Instruct-FP8-KV -g 8 -d float8
  
  :

  Find the throughput report at [`./reports_float8_vllm_rocm6.4.1/summary/Llama-3.1-70B-Instruct-FP8-KV_throughput_report.csv`{.docutils .literal .notranslate}]{.pre}.

{.admonition .note}
Note

Throughput is calculated as:

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  

::::::::::::
::::::::::::::::::
:::::::::::::::::::

:::::::::::::::::::
{.model-doc .pyt-vllm-llama-3-1-405b-fp8 .docutils .container}
::::::::::::::::::
{.sd-tab-set .docutils}
MAD-integrated benchmarking

::::
{.sd-tab-content .docutils}
Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

:
{.highlight-shell .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD
    pip install -r requirements.txt

:

Use this command to run the performance benchmark test on the [Llama 3.1 405B FP8](https://huggingface.co/amd/Llama-3.1-405B-Instruct-FP8-KV){.reference .external} model using one GPU with the [`float8`{.docutils .literal .notranslate}]{.pre} data type on the host machine.

:
{.highlight-shell .notranslate}

highlight
    export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
    python3 tools/run_models.py --tags pyt_vllm_llama-3.1-405b_fp8 --keep-model-dir --live-output --timeout 28800

:

MAD launches a Docker container with the name [`container_ci-pyt_vllm_llama-3.1-405b_fp8`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in the following path: [`~/MAD/reports_float8/`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-v0901-20250605){.reference .internal} are preconfigured to collect latency and throughput performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
::::

Standalone benchmarking

::::::::::::
{.sd-tab-content .docutils}
Run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.9.0.1_20250605/images/sha256-f48beeb3d72663a93c77211eb45273d564451447c097e060befa713d565fa36c){.reference .external} as shown in the following snippet.

:
{.highlight-default .notranslate}

highlight
    docker pull rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605
    docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --shm-size 16G --security-opt seccomp=unconfined --security-opt apparmor=unconfined --cap-add=SYS_PTRACE -v $(pwd):/workspace --env HUGGINGFACE_HUB_CACHE=/workspace --name test rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605

:

In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at [`~/MAD/scripts/vllm`{.docutils .literal .notranslate}]{.pre}.

:
{.highlight-default .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD/scripts/vllm

:

To start the benchmark, use the following command with the appropriate options.

:
{.highlight-default .notranslate}

highlight
    ./vllm_benchmark_report.sh -s $test_option -m amd/Llama-3.1-405B-Instruct-FP8-KV -g $num_gpu -d float8

:

pst-scrollable-table-container
  Name                                                      Options                                                                                                   Description
  --------------------------------------------------------- --------------------------------------------------------------------------------------------------------- -------------------------------------
  [`$test_option`{.docutils .literal .notranslate}]{.pre}   latency                                                                                                   Measure decoding token latency
                                                            throughput                                                                                                Measure token generation throughput
                                                            all                                                                                                       Measure both throughput and latency
  [`$num_gpu`{.docutils .literal .notranslate}]{.pre}       1 or 8                                                                                                    Number of GPUs
  [`$datatype`{.docutils .literal .notranslate}]{.pre}      [`float16`{.docutils .literal .notranslate}]{.pre} or [`float8`{.docutils .literal .notranslate}]{.pre}   Data type

{.admonition .note}
Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don't need to specify them with this script.

::
{.admonition .note}
Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:
{.highlight-default .notranslate}

highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token

:
::

Here are some examples of running the benchmark with various options.

- Latency benchmark

  Use this command to benchmark the latency of the Llama 3.1 405B FP8 model on eight GPUs with [`float8`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-default .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s latency -m amd/Llama-3.1-405B-Instruct-FP8-KV -g 8 -d float8
  
  :

  Find the latency report at [`./reports_float8_vllm_rocm6.4.1/summary/Llama-3.1-405B-Instruct-FP8-KV_latency_report.csv`{.docutils .literal .notranslate}]{.pre}.

- Throughput benchmark

  Use this command to benchmark the throughput of the Llama 3.1 405B FP8 model on eight GPUs with [`float8`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-shell .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s throughput -m amd/Llama-3.1-405B-Instruct-FP8-KV -g 8 -d float8
  
  :

  Find the throughput report at [`./reports_float8_vllm_rocm6.4.1/summary/Llama-3.1-405B-Instruct-FP8-KV_throughput_report.csv`{.docutils .literal .notranslate}]{.pre}.

{.admonition .note}
Note

Throughput is calculated as:

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  

::::::::::::
::::::::::::::::::
:::::::::::::::::::

:::::::::::::::::::
{.model-doc .pyt-vllm-mixtral-8x7b .docutils .container}
::::::::::::::::::
{.sd-tab-set .docutils}
MAD-integrated benchmarking

::::
{.sd-tab-content .docutils}
Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

:
{.highlight-shell .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD
    pip install -r requirements.txt

:

Use this command to run the performance benchmark test on the [Mixtral MoE 8x7B](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1){.reference .external} model using one GPU with the [`float16`{.docutils .literal .notranslate}]{.pre} data type on the host machine.

:
{.highlight-shell .notranslate}

highlight
    export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
    python3 tools/run_models.py --tags pyt_vllm_mixtral-8x7b --keep-model-dir --live-output --timeout 28800

:

MAD launches a Docker container with the name [`container_ci-pyt_vllm_mixtral-8x7b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in the following path: [`~/MAD/reports_float16/`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-v0901-20250605){.reference .internal} are preconfigured to collect latency and throughput performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
::::

Standalone benchmarking

::::::::::::
{.sd-tab-content .docutils}
Run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.9.0.1_20250605/images/sha256-f48beeb3d72663a93c77211eb45273d564451447c097e060befa713d565fa36c){.reference .external} as shown in the following snippet.

:
{.highlight-default .notranslate}

highlight
    docker pull rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605
    docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --shm-size 16G --security-opt seccomp=unconfined --security-opt apparmor=unconfined --cap-add=SYS_PTRACE -v $(pwd):/workspace --env HUGGINGFACE_HUB_CACHE=/workspace --name test rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605

:

In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at [`~/MAD/scripts/vllm`{.docutils .literal .notranslate}]{.pre}.

:
{.highlight-default .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD/scripts/vllm

:

To start the benchmark, use the following command with the appropriate options.

:
{.highlight-default .notranslate}

highlight
    ./vllm_benchmark_report.sh -s $test_option -m mistralai/Mixtral-8x7B-Instruct-v0.1 -g $num_gpu -d float16

:

pst-scrollable-table-container
  Name                                                      Options                                                                                                   Description
  --------------------------------------------------------- --------------------------------------------------------------------------------------------------------- -------------------------------------
  [`$test_option`{.docutils .literal .notranslate}]{.pre}   latency                                                                                                   Measure decoding token latency
                                                            throughput                                                                                                Measure token generation throughput
                                                            all                                                                                                       Measure both throughput and latency
  [`$num_gpu`{.docutils .literal .notranslate}]{.pre}       1 or 8                                                                                                    Number of GPUs
  [`$datatype`{.docutils .literal .notranslate}]{.pre}      [`float16`{.docutils .literal .notranslate}]{.pre} or [`float8`{.docutils .literal .notranslate}]{.pre}   Data type

{.admonition .note}
Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don't need to specify them with this script.

::
{.admonition .note}
Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:
{.highlight-default .notranslate}

highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token

:
::

Here are some examples of running the benchmark with various options.

- Latency benchmark

  Use this command to benchmark the latency of the Mixtral MoE 8x7B model on eight GPUs with [`float16`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-default .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s latency -m mistralai/Mixtral-8x7B-Instruct-v0.1 -g 8 -d float16
  
  :

  Find the latency report at [`./reports_float16_vllm_rocm6.4.1/summary/Mixtral-8x7B-Instruct-v0.1_latency_report.csv`{.docutils .literal .notranslate}]{.pre}.

- Throughput benchmark

  Use this command to benchmark the throughput of the Mixtral MoE 8x7B model on eight GPUs with [`float16`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-shell .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s throughput -m mistralai/Mixtral-8x7B-Instruct-v0.1 -g 8 -d float16
  
  :

  Find the throughput report at [`./reports_float16_vllm_rocm6.4.1/summary/Mixtral-8x7B-Instruct-v0.1_throughput_report.csv`{.docutils .literal .notranslate}]{.pre}.

{.admonition .note}
Note

Throughput is calculated as:

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  

::::::::::::
::::::::::::::::::
:::::::::::::::::::

:::::::::::::::::::
{.model-doc .pyt-vllm-mixtral-8x22b .docutils .container}
::::::::::::::::::
{.sd-tab-set .docutils}
MAD-integrated benchmarking

::::
{.sd-tab-content .docutils}
Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

:
{.highlight-shell .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD
    pip install -r requirements.txt

:

Use this command to run the performance benchmark test on the [Mixtral MoE 8x22B](https://huggingface.co/mistralai/Mixtral-8x22B-Instruct-v0.1){.reference .external} model using one GPU with the [`float16`{.docutils .literal .notranslate}]{.pre} data type on the host machine.

:
{.highlight-shell .notranslate}

highlight
    export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
    python3 tools/run_models.py --tags pyt_vllm_mixtral-8x22b --keep-model-dir --live-output --timeout 28800

:

MAD launches a Docker container with the name [`container_ci-pyt_vllm_mixtral-8x22b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in the following path: [`~/MAD/reports_float16/`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-v0901-20250605){.reference .internal} are preconfigured to collect latency and throughput performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
::::

Standalone benchmarking

::::::::::::
{.sd-tab-content .docutils}
Run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.9.0.1_20250605/images/sha256-f48beeb3d72663a93c77211eb45273d564451447c097e060befa713d565fa36c){.reference .external} as shown in the following snippet.

:
{.highlight-default .notranslate}

highlight
    docker pull rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605
    docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --shm-size 16G --security-opt seccomp=unconfined --security-opt apparmor=unconfined --cap-add=SYS_PTRACE -v $(pwd):/workspace --env HUGGINGFACE_HUB_CACHE=/workspace --name test rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605

:

In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at [`~/MAD/scripts/vllm`{.docutils .literal .notranslate}]{.pre}.

:
{.highlight-default .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD/scripts/vllm

:

To start the benchmark, use the following command with the appropriate options.

:
{.highlight-default .notranslate}

highlight
    ./vllm_benchmark_report.sh -s $test_option -m mistralai/Mixtral-8x22B-Instruct-v0.1 -g $num_gpu -d float16

:

pst-scrollable-table-container
  Name                                                      Options                                                                                                   Description
  --------------------------------------------------------- --------------------------------------------------------------------------------------------------------- -------------------------------------
  [`$test_option`{.docutils .literal .notranslate}]{.pre}   latency                                                                                                   Measure decoding token latency
                                                            throughput                                                                                                Measure token generation throughput
                                                            all                                                                                                       Measure both throughput and latency
  [`$num_gpu`{.docutils .literal .notranslate}]{.pre}       1 or 8                                                                                                    Number of GPUs
  [`$datatype`{.docutils .literal .notranslate}]{.pre}      [`float16`{.docutils .literal .notranslate}]{.pre} or [`float8`{.docutils .literal .notranslate}]{.pre}   Data type

{.admonition .note}
Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don't need to specify them with this script.

::
{.admonition .note}
Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:
{.highlight-default .notranslate}

highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token

:
::

Here are some examples of running the benchmark with various options.

- Latency benchmark

  Use this command to benchmark the latency of the Mixtral MoE 8x22B model on eight GPUs with [`float16`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-default .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s latency -m mistralai/Mixtral-8x22B-Instruct-v0.1 -g 8 -d float16
  
  :

  Find the latency report at [`./reports_float16_vllm_rocm6.4.1/summary/Mixtral-8x22B-Instruct-v0.1_latency_report.csv`{.docutils .literal .notranslate}]{.pre}.

- Throughput benchmark

  Use this command to benchmark the throughput of the Mixtral MoE 8x22B model on eight GPUs with [`float16`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-shell .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s throughput -m mistralai/Mixtral-8x22B-Instruct-v0.1 -g 8 -d float16
  
  :

  Find the throughput report at [`./reports_float16_vllm_rocm6.4.1/summary/Mixtral-8x22B-Instruct-v0.1_throughput_report.csv`{.docutils .literal .notranslate}]{.pre}.

{.admonition .note}
Note

Throughput is calculated as:

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  

::::::::::::
::::::::::::::::::
:::::::::::::::::::

:::::::::::::::::::
{.model-doc .pyt-vllm-mistral-7b .docutils .container}
::::::::::::::::::
{.sd-tab-set .docutils}
MAD-integrated benchmarking

::::
{.sd-tab-content .docutils}
Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

:
{.highlight-shell .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD
    pip install -r requirements.txt

:

Use this command to run the performance benchmark test on the [Mistral 7B](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3){.reference .external} model using one GPU with the [`float16`{.docutils .literal .notranslate}]{.pre} data type on the host machine.

:
{.highlight-shell .notranslate}

highlight
    export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
    python3 tools/run_models.py --tags pyt_vllm_mistral-7b --keep-model-dir --live-output --timeout 28800

:

MAD launches a Docker container with the name [`container_ci-pyt_vllm_mistral-7b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in the following path: [`~/MAD/reports_float16/`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-v0901-20250605){.reference .internal} are preconfigured to collect latency and throughput performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
::::

Standalone benchmarking

::::::::::::
{.sd-tab-content .docutils}
Run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.9.0.1_20250605/images/sha256-f48beeb3d72663a93c77211eb45273d564451447c097e060befa713d565fa36c){.reference .external} as shown in the following snippet.

:
{.highlight-default .notranslate}

highlight
    docker pull rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605
    docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --shm-size 16G --security-opt seccomp=unconfined --security-opt apparmor=unconfined --cap-add=SYS_PTRACE -v $(pwd):/workspace --env HUGGINGFACE_HUB_CACHE=/workspace --name test rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605

:

In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at [`~/MAD/scripts/vllm`{.docutils .literal .notranslate}]{.pre}.

:
{.highlight-default .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD/scripts/vllm

:

To start the benchmark, use the following command with the appropriate options.

:
{.highlight-default .notranslate}

highlight
    ./vllm_benchmark_report.sh -s $test_option -m mistralai/Mistral-7B-Instruct-v0.3 -g $num_gpu -d float16

:

pst-scrollable-table-container
  Name                                                      Options                                                                                                   Description
  --------------------------------------------------------- --------------------------------------------------------------------------------------------------------- -------------------------------------
  [`$test_option`{.docutils .literal .notranslate}]{.pre}   latency                                                                                                   Measure decoding token latency
                                                            throughput                                                                                                Measure token generation throughput
                                                            all                                                                                                       Measure both throughput and latency
  [`$num_gpu`{.docutils .literal .notranslate}]{.pre}       1 or 8                                                                                                    Number of GPUs
  [`$datatype`{.docutils .literal .notranslate}]{.pre}      [`float16`{.docutils .literal .notranslate}]{.pre} or [`float8`{.docutils .literal .notranslate}]{.pre}   Data type

{.admonition .note}
Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don't need to specify them with this script.

::
{.admonition .note}
Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:
{.highlight-default .notranslate}

highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token

:
::

Here are some examples of running the benchmark with various options.

- Latency benchmark

  Use this command to benchmark the latency of the Mistral 7B model on eight GPUs with [`float16`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-default .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s latency -m mistralai/Mistral-7B-Instruct-v0.3 -g 8 -d float16
  
  :

  Find the latency report at [`./reports_float16_vllm_rocm6.4.1/summary/Mistral-7B-Instruct-v0.3_latency_report.csv`{.docutils .literal .notranslate}]{.pre}.

- Throughput benchmark

  Use this command to benchmark the throughput of the Mistral 7B model on eight GPUs with [`float16`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-shell .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s throughput -m mistralai/Mistral-7B-Instruct-v0.3 -g 8 -d float16
  
  :

  Find the throughput report at [`./reports_float16_vllm_rocm6.4.1/summary/Mistral-7B-Instruct-v0.3_throughput_report.csv`{.docutils .literal .notranslate}]{.pre}.

{.admonition .note}
Note

Throughput is calculated as:

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  

::::::::::::
::::::::::::::::::
:::::::::::::::::::

:::::::::::::::::::
{.model-doc .pyt-vllm-mixtral-8x7b-fp8 .docutils .container}
::::::::::::::::::
{.sd-tab-set .docutils}
MAD-integrated benchmarking

::::
{.sd-tab-content .docutils}
Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

:
{.highlight-shell .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD
    pip install -r requirements.txt

:

Use this command to run the performance benchmark test on the [Mixtral MoE 8x7B FP8](https://huggingface.co/amd/Mixtral-8x7B-Instruct-v0.1-FP8-KV){.reference .external} model using one GPU with the [`float8`{.docutils .literal .notranslate}]{.pre} data type on the host machine.

:
{.highlight-shell .notranslate}

highlight
    export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
    python3 tools/run_models.py --tags pyt_vllm_mixtral-8x7b_fp8 --keep-model-dir --live-output --timeout 28800

:

MAD launches a Docker container with the name [`container_ci-pyt_vllm_mixtral-8x7b_fp8`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in the following path: [`~/MAD/reports_float8/`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-v0901-20250605){.reference .internal} are preconfigured to collect latency and throughput performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
::::

Standalone benchmarking

::::::::::::
{.sd-tab-content .docutils}
Run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.9.0.1_20250605/images/sha256-f48beeb3d72663a93c77211eb45273d564451447c097e060befa713d565fa36c){.reference .external} as shown in the following snippet.

:
{.highlight-default .notranslate}

highlight
    docker pull rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605
    docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --shm-size 16G --security-opt seccomp=unconfined --security-opt apparmor=unconfined --cap-add=SYS_PTRACE -v $(pwd):/workspace --env HUGGINGFACE_HUB_CACHE=/workspace --name test rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605

:

In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at [`~/MAD/scripts/vllm`{.docutils .literal .notranslate}]{.pre}.

:
{.highlight-default .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD/scripts/vllm

:

To start the benchmark, use the following command with the appropriate options.

:
{.highlight-default .notranslate}

highlight
    ./vllm_benchmark_report.sh -s $test_option -m amd/Mixtral-8x7B-Instruct-v0.1-FP8-KV -g $num_gpu -d float8

:

pst-scrollable-table-container
  Name                                                      Options                                                                                                   Description
  --------------------------------------------------------- --------------------------------------------------------------------------------------------------------- -------------------------------------
  [`$test_option`{.docutils .literal .notranslate}]{.pre}   latency                                                                                                   Measure decoding token latency
                                                            throughput                                                                                                Measure token generation throughput
                                                            all                                                                                                       Measure both throughput and latency
  [`$num_gpu`{.docutils .literal .notranslate}]{.pre}       1 or 8                                                                                                    Number of GPUs
  [`$datatype`{.docutils .literal .notranslate}]{.pre}      [`float16`{.docutils .literal .notranslate}]{.pre} or [`float8`{.docutils .literal .notranslate}]{.pre}   Data type

{.admonition .note}
Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don't need to specify them with this script.

::
{.admonition .note}
Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:
{.highlight-default .notranslate}

highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token

:
::

Here are some examples of running the benchmark with various options.

- Latency benchmark

  Use this command to benchmark the latency of the Mixtral MoE 8x7B FP8 model on eight GPUs with [`float8`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-default .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s latency -m amd/Mixtral-8x7B-Instruct-v0.1-FP8-KV -g 8 -d float8
  
  :

  Find the latency report at [`./reports_float8_vllm_rocm6.4.1/summary/Mixtral-8x7B-Instruct-v0.1-FP8-KV_latency_report.csv`{.docutils .literal .notranslate}]{.pre}.

- Throughput benchmark

  Use this command to benchmark the throughput of the Mixtral MoE 8x7B FP8 model on eight GPUs with [`float8`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-shell .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s throughput -m amd/Mixtral-8x7B-Instruct-v0.1-FP8-KV -g 8 -d float8
  
  :

  Find the throughput report at [`./reports_float8_vllm_rocm6.4.1/summary/Mixtral-8x7B-Instruct-v0.1-FP8-KV_throughput_report.csv`{.docutils .literal .notranslate}]{.pre}.

{.admonition .note}
Note

Throughput is calculated as:

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  

::::::::::::
::::::::::::::::::
:::::::::::::::::::

:::::::::::::::::::
{.model-doc .pyt-vllm-mixtral-8x22b-fp8 .docutils .container}
::::::::::::::::::
{.sd-tab-set .docutils}
MAD-integrated benchmarking

::::
{.sd-tab-content .docutils}
Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

:
{.highlight-shell .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD
    pip install -r requirements.txt

:

Use this command to run the performance benchmark test on the [Mixtral MoE 8x22B FP8](https://huggingface.co/amd/Mixtral-8x22B-Instruct-v0.1-FP8-KV){.reference .external} model using one GPU with the [`float8`{.docutils .literal .notranslate}]{.pre} data type on the host machine.

:
{.highlight-shell .notranslate}

highlight
    export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
    python3 tools/run_models.py --tags pyt_vllm_mixtral-8x22b_fp8 --keep-model-dir --live-output --timeout 28800

:

MAD launches a Docker container with the name [`container_ci-pyt_vllm_mixtral-8x22b_fp8`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in the following path: [`~/MAD/reports_float8/`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-v0901-20250605){.reference .internal} are preconfigured to collect latency and throughput performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
::::

Standalone benchmarking

::::::::::::
{.sd-tab-content .docutils}
Run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.9.0.1_20250605/images/sha256-f48beeb3d72663a93c77211eb45273d564451447c097e060befa713d565fa36c){.reference .external} as shown in the following snippet.

:
{.highlight-default .notranslate}

highlight
    docker pull rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605
    docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --shm-size 16G --security-opt seccomp=unconfined --security-opt apparmor=unconfined --cap-add=SYS_PTRACE -v $(pwd):/workspace --env HUGGINGFACE_HUB_CACHE=/workspace --name test rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605

:

In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at [`~/MAD/scripts/vllm`{.docutils .literal .notranslate}]{.pre}.

:
{.highlight-default .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD/scripts/vllm

:

To start the benchmark, use the following command with the appropriate options.

:
{.highlight-default .notranslate}

highlight
    ./vllm_benchmark_report.sh -s $test_option -m amd/Mixtral-8x22B-Instruct-v0.1-FP8-KV -g $num_gpu -d float8

:

pst-scrollable-table-container
  Name                                                      Options                                                                                                   Description
  --------------------------------------------------------- --------------------------------------------------------------------------------------------------------- -------------------------------------
  [`$test_option`{.docutils .literal .notranslate}]{.pre}   latency                                                                                                   Measure decoding token latency
                                                            throughput                                                                                                Measure token generation throughput
                                                            all                                                                                                       Measure both throughput and latency
  [`$num_gpu`{.docutils .literal .notranslate}]{.pre}       1 or 8                                                                                                    Number of GPUs
  [`$datatype`{.docutils .literal .notranslate}]{.pre}      [`float16`{.docutils .literal .notranslate}]{.pre} or [`float8`{.docutils .literal .notranslate}]{.pre}   Data type

{.admonition .note}
Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don't need to specify them with this script.

::
{.admonition .note}
Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:
{.highlight-default .notranslate}

highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token

:
::

Here are some examples of running the benchmark with various options.

- Latency benchmark

  Use this command to benchmark the latency of the Mixtral MoE 8x22B FP8 model on eight GPUs with [`float8`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-default .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s latency -m amd/Mixtral-8x22B-Instruct-v0.1-FP8-KV -g 8 -d float8
  
  :

  Find the latency report at [`./reports_float8_vllm_rocm6.4.1/summary/Mixtral-8x22B-Instruct-v0.1-FP8-KV_latency_report.csv`{.docutils .literal .notranslate}]{.pre}.

- Throughput benchmark

  Use this command to benchmark the throughput of the Mixtral MoE 8x22B FP8 model on eight GPUs with [`float8`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-shell .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s throughput -m amd/Mixtral-8x22B-Instruct-v0.1-FP8-KV -g 8 -d float8
  
  :

  Find the throughput report at [`./reports_float8_vllm_rocm6.4.1/summary/Mixtral-8x22B-Instruct-v0.1-FP8-KV_throughput_report.csv`{.docutils .literal .notranslate}]{.pre}.

{.admonition .note}
Note

Throughput is calculated as:

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  

::::::::::::
::::::::::::::::::
:::::::::::::::::::

:::::::::::::::::::
{.model-doc .pyt-vllm-mistral-7b-fp8 .docutils .container}
::::::::::::::::::
{.sd-tab-set .docutils}
MAD-integrated benchmarking

::::
{.sd-tab-content .docutils}
Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

:
{.highlight-shell .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD
    pip install -r requirements.txt

:

Use this command to run the performance benchmark test on the [Mistral 7B FP8](https://huggingface.co/amd/Mistral-7B-v0.1-FP8-KV){.reference .external} model using one GPU with the [`float8`{.docutils .literal .notranslate}]{.pre} data type on the host machine.

:
{.highlight-shell .notranslate}

highlight
    export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
    python3 tools/run_models.py --tags pyt_vllm_mistral-7b_fp8 --keep-model-dir --live-output --timeout 28800

:

MAD launches a Docker container with the name [`container_ci-pyt_vllm_mistral-7b_fp8`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in the following path: [`~/MAD/reports_float8/`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-v0901-20250605){.reference .internal} are preconfigured to collect latency and throughput performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
::::

Standalone benchmarking

::::::::::::
{.sd-tab-content .docutils}
Run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.9.0.1_20250605/images/sha256-f48beeb3d72663a93c77211eb45273d564451447c097e060befa713d565fa36c){.reference .external} as shown in the following snippet.

:
{.highlight-default .notranslate}

highlight
    docker pull rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605
    docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --shm-size 16G --security-opt seccomp=unconfined --security-opt apparmor=unconfined --cap-add=SYS_PTRACE -v $(pwd):/workspace --env HUGGINGFACE_HUB_CACHE=/workspace --name test rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605

:

In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at [`~/MAD/scripts/vllm`{.docutils .literal .notranslate}]{.pre}.

:
{.highlight-default .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD/scripts/vllm

:

To start the benchmark, use the following command with the appropriate options.

:
{.highlight-default .notranslate}

highlight
    ./vllm_benchmark_report.sh -s $test_option -m amd/Mistral-7B-v0.1-FP8-KV -g $num_gpu -d float8

:

pst-scrollable-table-container
  Name                                                      Options                                                                                                   Description
  --------------------------------------------------------- --------------------------------------------------------------------------------------------------------- -------------------------------------
  [`$test_option`{.docutils .literal .notranslate}]{.pre}   latency                                                                                                   Measure decoding token latency
                                                            throughput                                                                                                Measure token generation throughput
                                                            all                                                                                                       Measure both throughput and latency
  [`$num_gpu`{.docutils .literal .notranslate}]{.pre}       1 or 8                                                                                                    Number of GPUs
  [`$datatype`{.docutils .literal .notranslate}]{.pre}      [`float16`{.docutils .literal .notranslate}]{.pre} or [`float8`{.docutils .literal .notranslate}]{.pre}   Data type

{.admonition .note}
Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don't need to specify them with this script.

::
{.admonition .note}
Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:
{.highlight-default .notranslate}

highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token

:
::

Here are some examples of running the benchmark with various options.

- Latency benchmark

  Use this command to benchmark the latency of the Mistral 7B FP8 model on eight GPUs with [`float8`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-default .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s latency -m amd/Mistral-7B-v0.1-FP8-KV -g 8 -d float8
  
  :

  Find the latency report at [`./reports_float8_vllm_rocm6.4.1/summary/Mistral-7B-v0.1-FP8-KV_latency_report.csv`{.docutils .literal .notranslate}]{.pre}.

- Throughput benchmark

  Use this command to benchmark the throughput of the Mistral 7B FP8 model on eight GPUs with [`float8`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-shell .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s throughput -m amd/Mistral-7B-v0.1-FP8-KV -g 8 -d float8
  
  :

  Find the throughput report at [`./reports_float8_vllm_rocm6.4.1/summary/Mistral-7B-v0.1-FP8-KV_throughput_report.csv`{.docutils .literal .notranslate}]{.pre}.

{.admonition .note}
Note

Throughput is calculated as:

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  

::::::::::::
::::::::::::::::::
:::::::::::::::::::

:::::::::::::::::::
{.model-doc .pyt-vllm-qwen2-7b .docutils .container}
::::::::::::::::::
{.sd-tab-set .docutils}
MAD-integrated benchmarking

::::
{.sd-tab-content .docutils}
Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

:
{.highlight-shell .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD
    pip install -r requirements.txt

:

Use this command to run the performance benchmark test on the [Qwen2 7B](https://huggingface.co/Qwen/Qwen2-7B-Instruct){.reference .external} model using one GPU with the [`float16`{.docutils .literal .notranslate}]{.pre} data type on the host machine.

:
{.highlight-shell .notranslate}

highlight
    export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
    python3 tools/run_models.py --tags pyt_vllm_qwen2-7b --keep-model-dir --live-output --timeout 28800

:

MAD launches a Docker container with the name [`container_ci-pyt_vllm_qwen2-7b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in the following path: [`~/MAD/reports_float16/`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-v0901-20250605){.reference .internal} are preconfigured to collect latency and throughput performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
::::

Standalone benchmarking

::::::::::::
{.sd-tab-content .docutils}
Run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.9.0.1_20250605/images/sha256-f48beeb3d72663a93c77211eb45273d564451447c097e060befa713d565fa36c){.reference .external} as shown in the following snippet.

:
{.highlight-default .notranslate}

highlight
    docker pull rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605
    docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --shm-size 16G --security-opt seccomp=unconfined --security-opt apparmor=unconfined --cap-add=SYS_PTRACE -v $(pwd):/workspace --env HUGGINGFACE_HUB_CACHE=/workspace --name test rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605

:

In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at [`~/MAD/scripts/vllm`{.docutils .literal .notranslate}]{.pre}.

:
{.highlight-default .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD/scripts/vllm

:

To start the benchmark, use the following command with the appropriate options.

:
{.highlight-default .notranslate}

highlight
    ./vllm_benchmark_report.sh -s $test_option -m Qwen/Qwen2-7B-Instruct -g $num_gpu -d float16

:

pst-scrollable-table-container
  Name                                                      Options                                                                                                   Description
  --------------------------------------------------------- --------------------------------------------------------------------------------------------------------- -------------------------------------
  [`$test_option`{.docutils .literal .notranslate}]{.pre}   latency                                                                                                   Measure decoding token latency
                                                            throughput                                                                                                Measure token generation throughput
                                                            all                                                                                                       Measure both throughput and latency
  [`$num_gpu`{.docutils .literal .notranslate}]{.pre}       1 or 8                                                                                                    Number of GPUs
  [`$datatype`{.docutils .literal .notranslate}]{.pre}      [`float16`{.docutils .literal .notranslate}]{.pre} or [`float8`{.docutils .literal .notranslate}]{.pre}   Data type

{.admonition .note}
Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don't need to specify them with this script.

::
{.admonition .note}
Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:
{.highlight-default .notranslate}

highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token

:
::

Here are some examples of running the benchmark with various options.

- Latency benchmark

  Use this command to benchmark the latency of the Qwen2 7B model on eight GPUs with [`float16`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-default .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s latency -m Qwen/Qwen2-7B-Instruct -g 8 -d float16
  
  :

  Find the latency report at [`./reports_float16_vllm_rocm6.4.1/summary/Qwen2-7B-Instruct_latency_report.csv`{.docutils .literal .notranslate}]{.pre}.

- Throughput benchmark

  Use this command to benchmark the throughput of the Qwen2 7B model on eight GPUs with [`float16`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-shell .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s throughput -m Qwen/Qwen2-7B-Instruct -g 8 -d float16
  
  :

  Find the throughput report at [`./reports_float16_vllm_rocm6.4.1/summary/Qwen2-7B-Instruct_throughput_report.csv`{.docutils .literal .notranslate}]{.pre}.

{.admonition .note}
Note

Throughput is calculated as:

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  

::::::::::::
::::::::::::::::::
:::::::::::::::::::

:::::::::::::::::::
{.model-doc .pyt-vllm-qwen2-72b .docutils .container}
::::::::::::::::::
{.sd-tab-set .docutils}
MAD-integrated benchmarking

::::
{.sd-tab-content .docutils}
Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

:
{.highlight-shell .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD
    pip install -r requirements.txt

:

Use this command to run the performance benchmark test on the [Qwen2 72B](https://huggingface.co/Qwen/Qwen2-72B-Instruct){.reference .external} model using one GPU with the [`float16`{.docutils .literal .notranslate}]{.pre} data type on the host machine.

:
{.highlight-shell .notranslate}

highlight
    export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
    python3 tools/run_models.py --tags pyt_vllm_qwen2-72b --keep-model-dir --live-output --timeout 28800

:

MAD launches a Docker container with the name [`container_ci-pyt_vllm_qwen2-72b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in the following path: [`~/MAD/reports_float16/`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-v0901-20250605){.reference .internal} are preconfigured to collect latency and throughput performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
::::

Standalone benchmarking

::::::::::::
{.sd-tab-content .docutils}
Run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.9.0.1_20250605/images/sha256-f48beeb3d72663a93c77211eb45273d564451447c097e060befa713d565fa36c){.reference .external} as shown in the following snippet.

:
{.highlight-default .notranslate}

highlight
    docker pull rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605
    docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --shm-size 16G --security-opt seccomp=unconfined --security-opt apparmor=unconfined --cap-add=SYS_PTRACE -v $(pwd):/workspace --env HUGGINGFACE_HUB_CACHE=/workspace --name test rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605

:

In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at [`~/MAD/scripts/vllm`{.docutils .literal .notranslate}]{.pre}.

:
{.highlight-default .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD/scripts/vllm

:

To start the benchmark, use the following command with the appropriate options.

:
{.highlight-default .notranslate}

highlight
    ./vllm_benchmark_report.sh -s $test_option -m Qwen/Qwen2-72B-Instruct -g $num_gpu -d float16

:

pst-scrollable-table-container
  Name                                                      Options                                                                                                   Description
  --------------------------------------------------------- --------------------------------------------------------------------------------------------------------- -------------------------------------
  [`$test_option`{.docutils .literal .notranslate}]{.pre}   latency                                                                                                   Measure decoding token latency
                                                            throughput                                                                                                Measure token generation throughput
                                                            all                                                                                                       Measure both throughput and latency
  [`$num_gpu`{.docutils .literal .notranslate}]{.pre}       1 or 8                                                                                                    Number of GPUs
  [`$datatype`{.docutils .literal .notranslate}]{.pre}      [`float16`{.docutils .literal .notranslate}]{.pre} or [`float8`{.docutils .literal .notranslate}]{.pre}   Data type

{.admonition .note}
Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don't need to specify them with this script.

::
{.admonition .note}
Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:
{.highlight-default .notranslate}

highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token

:
::

Here are some examples of running the benchmark with various options.

- Latency benchmark

  Use this command to benchmark the latency of the Qwen2 72B model on eight GPUs with [`float16`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-default .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s latency -m Qwen/Qwen2-72B-Instruct -g 8 -d float16
  
  :

  Find the latency report at [`./reports_float16_vllm_rocm6.4.1/summary/Qwen2-72B-Instruct_latency_report.csv`{.docutils .literal .notranslate}]{.pre}.

- Throughput benchmark

  Use this command to benchmark the throughput of the Qwen2 72B model on eight GPUs with [`float16`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-shell .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s throughput -m Qwen/Qwen2-72B-Instruct -g 8 -d float16
  
  :

  Find the throughput report at [`./reports_float16_vllm_rocm6.4.1/summary/Qwen2-72B-Instruct_throughput_report.csv`{.docutils .literal .notranslate}]{.pre}.

{.admonition .note}
Note

Throughput is calculated as:

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  

::::::::::::
::::::::::::::::::
:::::::::::::::::::

::::::::::::::::::::
{.model-doc .pyt-vllm-qwq-32b .docutils .container}
:::::::::::::::::::
{.sd-tab-set .docutils}
MAD-integrated benchmarking

:::::
{.sd-tab-content .docutils}
Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

:
{.highlight-shell .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD
    pip install -r requirements.txt

:

Use this command to run the performance benchmark test on the [QwQ-32B](https://huggingface.co/Qwen/QwQ-32B){.reference .external} model using one GPU with the [`float16`{.docutils .literal .notranslate}]{.pre} data type on the host machine.

:
{.highlight-shell .notranslate}

highlight
    export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
    python3 tools/run_models.py --tags pyt_vllm_qwq-32b --keep-model-dir --live-output --timeout 28800

:

MAD launches a Docker container with the name [`container_ci-pyt_vllm_qwq-32b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in the following path: [`~/MAD/reports_float16/`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-v0901-20250605){.reference .internal} are preconfigured to collect latency and throughput performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.

{.admonition .note}
Note

For improved performance, consider enabling [[PyTorch TunableOp]{.std .std-ref}](../../../inference-optimization/workload.html#mi300x-tunableop){.reference .internal}. TunableOp automatically explores different implementations and configurations of certain PyTorch operators to find the fastest one for your hardware.

By default, [`pyt_vllm_qwq-32b`{.docutils .literal .notranslate}]{.pre} runs with TunableOp disabled (see [ROCm/MAD](https://github.com/ROCm/MAD/blob/develop/models.json){.github .reference .external}). To enable it, edit the default run behavior in the [`models.json`{.docutils .literal .notranslate}]{.pre} configuration before running inference -- update the model's run [`args`{.docutils .literal .notranslate}]{.pre} by changing [`--tunableop`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`off`{.docutils .literal .notranslate}]{.pre} to [`--tunableop`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`on`{.docutils .literal .notranslate}]{.pre}.

Enabling TunableOp triggers a two-pass run -- a warm-up followed by the performance-collection run.

:::::

Standalone benchmarking

::::::::::::
{.sd-tab-content .docutils}
Run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.9.0.1_20250605/images/sha256-f48beeb3d72663a93c77211eb45273d564451447c097e060befa713d565fa36c){.reference .external} as shown in the following snippet.

:
{.highlight-default .notranslate}

highlight
    docker pull rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605
    docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --shm-size 16G --security-opt seccomp=unconfined --security-opt apparmor=unconfined --cap-add=SYS_PTRACE -v $(pwd):/workspace --env HUGGINGFACE_HUB_CACHE=/workspace --name test rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605

:

In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at [`~/MAD/scripts/vllm`{.docutils .literal .notranslate}]{.pre}.

:
{.highlight-default .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD/scripts/vllm

:

To start the benchmark, use the following command with the appropriate options.

:
{.highlight-default .notranslate}

highlight
    ./vllm_benchmark_report.sh -s $test_option -m Qwen/QwQ-32B -g $num_gpu -d float16

:

pst-scrollable-table-container
  Name                                                      Options                                                                                                   Description
  --------------------------------------------------------- --------------------------------------------------------------------------------------------------------- -------------------------------------
  [`$test_option`{.docutils .literal .notranslate}]{.pre}   latency                                                                                                   Measure decoding token latency
                                                            throughput                                                                                                Measure token generation throughput
                                                            all                                                                                                       Measure both throughput and latency
  [`$num_gpu`{.docutils .literal .notranslate}]{.pre}       1 or 8                                                                                                    Number of GPUs
  [`$datatype`{.docutils .literal .notranslate}]{.pre}      [`float16`{.docutils .literal .notranslate}]{.pre} or [`float8`{.docutils .literal .notranslate}]{.pre}   Data type

{.admonition .note}
Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don't need to specify them with this script.

::
{.admonition .note}
Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:
{.highlight-default .notranslate}

highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token

:
::

Here are some examples of running the benchmark with various options.

- Latency benchmark

  Use this command to benchmark the latency of the QwQ-32B model on eight GPUs with [`float16`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-default .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s latency -m Qwen/QwQ-32B -g 8 -d float16
  
  :

  Find the latency report at [`./reports_float16_vllm_rocm6.4.1/summary/QwQ-32B_latency_report.csv`{.docutils .literal .notranslate}]{.pre}.

- Throughput benchmark

  Use this command to benchmark the throughput of the QwQ-32B model on eight GPUs with [`float16`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-shell .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s throughput -m Qwen/QwQ-32B -g 8 -d float16
  
  :

  Find the throughput report at [`./reports_float16_vllm_rocm6.4.1/summary/QwQ-32B_throughput_report.csv`{.docutils .literal .notranslate}]{.pre}.

{.admonition .note}
Note

Throughput is calculated as:

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  

::::::::::::
:::::::::::::::::::
::::::::::::::::::::

:::::::::::::::::::
{.model-doc .pyt-vllm-dbrx-instruct .docutils .container}
::::::::::::::::::
{.sd-tab-set .docutils}
MAD-integrated benchmarking

::::
{.sd-tab-content .docutils}
Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

:
{.highlight-shell .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD
    pip install -r requirements.txt

:

Use this command to run the performance benchmark test on the [DBRX Instruct](https://huggingface.co/databricks/dbrx-instruct){.reference .external} model using one GPU with the [`float16`{.docutils .literal .notranslate}]{.pre} data type on the host machine.

:
{.highlight-shell .notranslate}

highlight
    export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
    python3 tools/run_models.py --tags pyt_vllm_dbrx-instruct --keep-model-dir --live-output --timeout 28800

:

MAD launches a Docker container with the name [`container_ci-pyt_vllm_dbrx-instruct`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in the following path: [`~/MAD/reports_float16/`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-v0901-20250605){.reference .internal} are preconfigured to collect latency and throughput performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
::::

Standalone benchmarking

::::::::::::
{.sd-tab-content .docutils}
Run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.9.0.1_20250605/images/sha256-f48beeb3d72663a93c77211eb45273d564451447c097e060befa713d565fa36c){.reference .external} as shown in the following snippet.

:
{.highlight-default .notranslate}

highlight
    docker pull rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605
    docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --shm-size 16G --security-opt seccomp=unconfined --security-opt apparmor=unconfined --cap-add=SYS_PTRACE -v $(pwd):/workspace --env HUGGINGFACE_HUB_CACHE=/workspace --name test rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605

:

In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at [`~/MAD/scripts/vllm`{.docutils .literal .notranslate}]{.pre}.

:
{.highlight-default .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD/scripts/vllm

:

To start the benchmark, use the following command with the appropriate options.

:
{.highlight-default .notranslate}

highlight
    ./vllm_benchmark_report.sh -s $test_option -m databricks/dbrx-instruct -g $num_gpu -d float16

:

pst-scrollable-table-container
  Name                                                      Options                                                                                                   Description
  --------------------------------------------------------- --------------------------------------------------------------------------------------------------------- -------------------------------------
  [`$test_option`{.docutils .literal .notranslate}]{.pre}   latency                                                                                                   Measure decoding token latency
                                                            throughput                                                                                                Measure token generation throughput
                                                            all                                                                                                       Measure both throughput and latency
  [`$num_gpu`{.docutils .literal .notranslate}]{.pre}       1 or 8                                                                                                    Number of GPUs
  [`$datatype`{.docutils .literal .notranslate}]{.pre}      [`float16`{.docutils .literal .notranslate}]{.pre} or [`float8`{.docutils .literal .notranslate}]{.pre}   Data type

{.admonition .note}
Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don't need to specify them with this script.

::
{.admonition .note}
Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:
{.highlight-default .notranslate}

highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token

:
::

Here are some examples of running the benchmark with various options.

- Latency benchmark

  Use this command to benchmark the latency of the DBRX Instruct model on eight GPUs with [`float16`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-default .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s latency -m databricks/dbrx-instruct -g 8 -d float16
  
  :

  Find the latency report at [`./reports_float16_vllm_rocm6.4.1/summary/dbrx-instruct_latency_report.csv`{.docutils .literal .notranslate}]{.pre}.

- Throughput benchmark

  Use this command to benchmark the throughput of the DBRX Instruct model on eight GPUs with [`float16`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-shell .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s throughput -m databricks/dbrx-instruct -g 8 -d float16
  
  :

  Find the throughput report at [`./reports_float16_vllm_rocm6.4.1/summary/dbrx-instruct_throughput_report.csv`{.docutils .literal .notranslate}]{.pre}.

{.admonition .note}
Note

Throughput is calculated as:

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  

::::::::::::
::::::::::::::::::
:::::::::::::::::::

:::::::::::::::::::
{.model-doc .pyt-vllm-dbrx-fp8 .docutils .container}
::::::::::::::::::
{.sd-tab-set .docutils}
MAD-integrated benchmarking

::::
{.sd-tab-content .docutils}
Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

:
{.highlight-shell .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD
    pip install -r requirements.txt

:

Use this command to run the performance benchmark test on the [DBRX Instruct FP8](https://huggingface.co/amd/dbrx-instruct-FP8-KV){.reference .external} model using one GPU with the [`float8`{.docutils .literal .notranslate}]{.pre} data type on the host machine.

:
{.highlight-shell .notranslate}

highlight
    export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
    python3 tools/run_models.py --tags pyt_vllm_dbrx_fp8 --keep-model-dir --live-output --timeout 28800

:

MAD launches a Docker container with the name [`container_ci-pyt_vllm_dbrx_fp8`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in the following path: [`~/MAD/reports_float8/`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-v0901-20250605){.reference .internal} are preconfigured to collect latency and throughput performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
::::

Standalone benchmarking

::::::::::::
{.sd-tab-content .docutils}
Run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.9.0.1_20250605/images/sha256-f48beeb3d72663a93c77211eb45273d564451447c097e060befa713d565fa36c){.reference .external} as shown in the following snippet.

:
{.highlight-default .notranslate}

highlight
    docker pull rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605
    docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --shm-size 16G --security-opt seccomp=unconfined --security-opt apparmor=unconfined --cap-add=SYS_PTRACE -v $(pwd):/workspace --env HUGGINGFACE_HUB_CACHE=/workspace --name test rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605

:

In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at [`~/MAD/scripts/vllm`{.docutils .literal .notranslate}]{.pre}.

:
{.highlight-default .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD/scripts/vllm

:

To start the benchmark, use the following command with the appropriate options.

:
{.highlight-default .notranslate}

highlight
    ./vllm_benchmark_report.sh -s $test_option -m amd/dbrx-instruct-FP8-KV -g $num_gpu -d float8

:

pst-scrollable-table-container
  Name                                                      Options                                                                                                   Description
  --------------------------------------------------------- --------------------------------------------------------------------------------------------------------- -------------------------------------
  [`$test_option`{.docutils .literal .notranslate}]{.pre}   latency                                                                                                   Measure decoding token latency
                                                            throughput                                                                                                Measure token generation throughput
                                                            all                                                                                                       Measure both throughput and latency
  [`$num_gpu`{.docutils .literal .notranslate}]{.pre}       1 or 8                                                                                                    Number of GPUs
  [`$datatype`{.docutils .literal .notranslate}]{.pre}      [`float16`{.docutils .literal .notranslate}]{.pre} or [`float8`{.docutils .literal .notranslate}]{.pre}   Data type

{.admonition .note}
Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don't need to specify them with this script.

::
{.admonition .note}
Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:
{.highlight-default .notranslate}

highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token

:
::

Here are some examples of running the benchmark with various options.

- Latency benchmark

  Use this command to benchmark the latency of the DBRX Instruct FP8 model on eight GPUs with [`float8`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-default .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s latency -m amd/dbrx-instruct-FP8-KV -g 8 -d float8
  
  :

  Find the latency report at [`./reports_float8_vllm_rocm6.4.1/summary/dbrx-instruct-FP8-KV_latency_report.csv`{.docutils .literal .notranslate}]{.pre}.

- Throughput benchmark

  Use this command to benchmark the throughput of the DBRX Instruct FP8 model on eight GPUs with [`float8`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-shell .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s throughput -m amd/dbrx-instruct-FP8-KV -g 8 -d float8
  
  :

  Find the throughput report at [`./reports_float8_vllm_rocm6.4.1/summary/dbrx-instruct-FP8-KV_throughput_report.csv`{.docutils .literal .notranslate}]{.pre}.

{.admonition .note}
Note

Throughput is calculated as:

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  

::::::::::::
::::::::::::::::::
:::::::::::::::::::

:::::::::::::::::::
{.model-doc .pyt-vllm-gemma-2-27b .docutils .container}
::::::::::::::::::
{.sd-tab-set .docutils}
MAD-integrated benchmarking

::::
{.sd-tab-content .docutils}
Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

:
{.highlight-shell .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD
    pip install -r requirements.txt

:

Use this command to run the performance benchmark test on the [Gemma 2 27B](https://huggingface.co/google/gemma-2-27b){.reference .external} model using one GPU with the [`float16`{.docutils .literal .notranslate}]{.pre} data type on the host machine.

:
{.highlight-shell .notranslate}

highlight
    export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
    python3 tools/run_models.py --tags pyt_vllm_gemma-2-27b --keep-model-dir --live-output --timeout 28800

:

MAD launches a Docker container with the name [`container_ci-pyt_vllm_gemma-2-27b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in the following path: [`~/MAD/reports_float16/`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-v0901-20250605){.reference .internal} are preconfigured to collect latency and throughput performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
::::

Standalone benchmarking

::::::::::::
{.sd-tab-content .docutils}
Run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.9.0.1_20250605/images/sha256-f48beeb3d72663a93c77211eb45273d564451447c097e060befa713d565fa36c){.reference .external} as shown in the following snippet.

:
{.highlight-default .notranslate}

highlight
    docker pull rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605
    docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --shm-size 16G --security-opt seccomp=unconfined --security-opt apparmor=unconfined --cap-add=SYS_PTRACE -v $(pwd):/workspace --env HUGGINGFACE_HUB_CACHE=/workspace --name test rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605

:

In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at [`~/MAD/scripts/vllm`{.docutils .literal .notranslate}]{.pre}.

:
{.highlight-default .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD/scripts/vllm

:

To start the benchmark, use the following command with the appropriate options.

:
{.highlight-default .notranslate}

highlight
    ./vllm_benchmark_report.sh -s $test_option -m google/gemma-2-27b -g $num_gpu -d float16

:

pst-scrollable-table-container
  Name                                                      Options                                                                                                   Description
  --------------------------------------------------------- --------------------------------------------------------------------------------------------------------- -------------------------------------
  [`$test_option`{.docutils .literal .notranslate}]{.pre}   latency                                                                                                   Measure decoding token latency
                                                            throughput                                                                                                Measure token generation throughput
                                                            all                                                                                                       Measure both throughput and latency
  [`$num_gpu`{.docutils .literal .notranslate}]{.pre}       1 or 8                                                                                                    Number of GPUs
  [`$datatype`{.docutils .literal .notranslate}]{.pre}      [`float16`{.docutils .literal .notranslate}]{.pre} or [`float8`{.docutils .literal .notranslate}]{.pre}   Data type

{.admonition .note}
Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don't need to specify them with this script.

::
{.admonition .note}
Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:
{.highlight-default .notranslate}

highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token

:
::

Here are some examples of running the benchmark with various options.

- Latency benchmark

  Use this command to benchmark the latency of the Gemma 2 27B model on eight GPUs with [`float16`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-default .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s latency -m google/gemma-2-27b -g 8 -d float16
  
  :

  Find the latency report at [`./reports_float16_vllm_rocm6.4.1/summary/gemma-2-27b_latency_report.csv`{.docutils .literal .notranslate}]{.pre}.

- Throughput benchmark

  Use this command to benchmark the throughput of the Gemma 2 27B model on eight GPUs with [`float16`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-shell .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s throughput -m google/gemma-2-27b -g 8 -d float16
  
  :

  Find the throughput report at [`./reports_float16_vllm_rocm6.4.1/summary/gemma-2-27b_throughput_report.csv`{.docutils .literal .notranslate}]{.pre}.

{.admonition .note}
Note

Throughput is calculated as:

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  

::::::::::::
::::::::::::::::::
:::::::::::::::::::

:::::::::::::::::::
{.model-doc .pyt-vllm-c4ai-command-r-plus-08-2024 .docutils .container}
::::::::::::::::::
{.sd-tab-set .docutils}
MAD-integrated benchmarking

::::
{.sd-tab-content .docutils}
Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

:
{.highlight-shell .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD
    pip install -r requirements.txt

:

Use this command to run the performance benchmark test on the [C4AI Command R+ 08-2024](https://huggingface.co/CohereForAI/c4ai-command-r-plus-08-2024){.reference .external} model using one GPU with the [`float16`{.docutils .literal .notranslate}]{.pre} data type on the host machine.

:
{.highlight-shell .notranslate}

highlight
    export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
    python3 tools/run_models.py --tags pyt_vllm_c4ai-command-r-plus-08-2024 --keep-model-dir --live-output --timeout 28800

:

MAD launches a Docker container with the name [`container_ci-pyt_vllm_c4ai-command-r-plus-08-2024`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in the following path: [`~/MAD/reports_float16/`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-v0901-20250605){.reference .internal} are preconfigured to collect latency and throughput performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
::::

Standalone benchmarking

::::::::::::
{.sd-tab-content .docutils}
Run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.9.0.1_20250605/images/sha256-f48beeb3d72663a93c77211eb45273d564451447c097e060befa713d565fa36c){.reference .external} as shown in the following snippet.

:
{.highlight-default .notranslate}

highlight
    docker pull rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605
    docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --shm-size 16G --security-opt seccomp=unconfined --security-opt apparmor=unconfined --cap-add=SYS_PTRACE -v $(pwd):/workspace --env HUGGINGFACE_HUB_CACHE=/workspace --name test rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605

:

In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at [`~/MAD/scripts/vllm`{.docutils .literal .notranslate}]{.pre}.

:
{.highlight-default .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD/scripts/vllm

:

To start the benchmark, use the following command with the appropriate options.

:
{.highlight-default .notranslate}

highlight
    ./vllm_benchmark_report.sh -s $test_option -m CohereForAI/c4ai-command-r-plus-08-2024 -g $num_gpu -d float16

:

pst-scrollable-table-container
  Name                                                      Options                                                                                                   Description
  --------------------------------------------------------- --------------------------------------------------------------------------------------------------------- -------------------------------------
  [`$test_option`{.docutils .literal .notranslate}]{.pre}   latency                                                                                                   Measure decoding token latency
                                                            throughput                                                                                                Measure token generation throughput
                                                            all                                                                                                       Measure both throughput and latency
  [`$num_gpu`{.docutils .literal .notranslate}]{.pre}       1 or 8                                                                                                    Number of GPUs
  [`$datatype`{.docutils .literal .notranslate}]{.pre}      [`float16`{.docutils .literal .notranslate}]{.pre} or [`float8`{.docutils .literal .notranslate}]{.pre}   Data type

{.admonition .note}
Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don't need to specify them with this script.

::
{.admonition .note}
Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:
{.highlight-default .notranslate}

highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token

:
::

Here are some examples of running the benchmark with various options.

- Latency benchmark

  Use this command to benchmark the latency of the C4AI Command R+ 08-2024 model on eight GPUs with [`float16`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-default .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s latency -m CohereForAI/c4ai-command-r-plus-08-2024 -g 8 -d float16
  
  :

  Find the latency report at [`./reports_float16_vllm_rocm6.4.1/summary/c4ai-command-r-plus-08-2024_latency_report.csv`{.docutils .literal .notranslate}]{.pre}.

- Throughput benchmark

  Use this command to benchmark the throughput of the C4AI Command R+ 08-2024 model on eight GPUs with [`float16`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-shell .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s throughput -m CohereForAI/c4ai-command-r-plus-08-2024 -g 8 -d float16
  
  :

  Find the throughput report at [`./reports_float16_vllm_rocm6.4.1/summary/c4ai-command-r-plus-08-2024_throughput_report.csv`{.docutils .literal .notranslate}]{.pre}.

{.admonition .note}
Note

Throughput is calculated as:

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  

::::::::::::
::::::::::::::::::
:::::::::::::::::::

:::::::::::::::::::
{.model-doc .pyt-vllm-command-r-plus-fp8 .docutils .container}
::::::::::::::::::
{.sd-tab-set .docutils}
MAD-integrated benchmarking

::::
{.sd-tab-content .docutils}
Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

:
{.highlight-shell .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD
    pip install -r requirements.txt

:

Use this command to run the performance benchmark test on the [C4AI Command R+ 08-2024 FP8](https://huggingface.co/amd/c4ai-command-r-plus-FP8-KV){.reference .external} model using one GPU with the [`float8`{.docutils .literal .notranslate}]{.pre} data type on the host machine.

:
{.highlight-shell .notranslate}

highlight
    export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
    python3 tools/run_models.py --tags pyt_vllm_command-r-plus_fp8 --keep-model-dir --live-output --timeout 28800

:

MAD launches a Docker container with the name [`container_ci-pyt_vllm_command-r-plus_fp8`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in the following path: [`~/MAD/reports_float8/`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-v0901-20250605){.reference .internal} are preconfigured to collect latency and throughput performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
::::

Standalone benchmarking

::::::::::::
{.sd-tab-content .docutils}
Run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.9.0.1_20250605/images/sha256-f48beeb3d72663a93c77211eb45273d564451447c097e060befa713d565fa36c){.reference .external} as shown in the following snippet.

:
{.highlight-default .notranslate}

highlight
    docker pull rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605
    docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --shm-size 16G --security-opt seccomp=unconfined --security-opt apparmor=unconfined --cap-add=SYS_PTRACE -v $(pwd):/workspace --env HUGGINGFACE_HUB_CACHE=/workspace --name test rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605

:

In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at [`~/MAD/scripts/vllm`{.docutils .literal .notranslate}]{.pre}.

:
{.highlight-default .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD/scripts/vllm

:

To start the benchmark, use the following command with the appropriate options.

:
{.highlight-default .notranslate}

highlight
    ./vllm_benchmark_report.sh -s $test_option -m amd/c4ai-command-r-plus-FP8-KV -g $num_gpu -d float8

:

pst-scrollable-table-container
  Name                                                      Options                                                                                                   Description
  --------------------------------------------------------- --------------------------------------------------------------------------------------------------------- -------------------------------------
  [`$test_option`{.docutils .literal .notranslate}]{.pre}   latency                                                                                                   Measure decoding token latency
                                                            throughput                                                                                                Measure token generation throughput
                                                            all                                                                                                       Measure both throughput and latency
  [`$num_gpu`{.docutils .literal .notranslate}]{.pre}       1 or 8                                                                                                    Number of GPUs
  [`$datatype`{.docutils .literal .notranslate}]{.pre}      [`float16`{.docutils .literal .notranslate}]{.pre} or [`float8`{.docutils .literal .notranslate}]{.pre}   Data type

{.admonition .note}
Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don't need to specify them with this script.

::
{.admonition .note}
Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:
{.highlight-default .notranslate}

highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token

:
::

Here are some examples of running the benchmark with various options.

- Latency benchmark

  Use this command to benchmark the latency of the C4AI Command R+ 08-2024 FP8 model on eight GPUs with [`float8`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-default .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s latency -m amd/c4ai-command-r-plus-FP8-KV -g 8 -d float8
  
  :

  Find the latency report at [`./reports_float8_vllm_rocm6.4.1/summary/c4ai-command-r-plus-FP8-KV_latency_report.csv`{.docutils .literal .notranslate}]{.pre}.

- Throughput benchmark

  Use this command to benchmark the throughput of the C4AI Command R+ 08-2024 FP8 model on eight GPUs with [`float8`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-shell .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s throughput -m amd/c4ai-command-r-plus-FP8-KV -g 8 -d float8
  
  :

  Find the throughput report at [`./reports_float8_vllm_rocm6.4.1/summary/c4ai-command-r-plus-FP8-KV_throughput_report.csv`{.docutils .literal .notranslate}]{.pre}.

{.admonition .note}
Note

Throughput is calculated as:

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  

::::::::::::
::::::::::::::::::
:::::::::::::::::::

:::::::::::::::::::
{.model-doc .pyt-vllm-deepseek-moe-16b-chat .docutils .container}
::::::::::::::::::
{.sd-tab-set .docutils}
MAD-integrated benchmarking

::::
{.sd-tab-content .docutils}
Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

:
{.highlight-shell .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD
    pip install -r requirements.txt

:

Use this command to run the performance benchmark test on the [DeepSeek MoE 16B](https://huggingface.co/deepseek-ai/deepseek-moe-16b-chat){.reference .external} model using one GPU with the [`float16`{.docutils .literal .notranslate}]{.pre} data type on the host machine.

:
{.highlight-shell .notranslate}

highlight
    export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
    python3 tools/run_models.py --tags pyt_vllm_deepseek-moe-16b-chat --keep-model-dir --live-output --timeout 28800

:

MAD launches a Docker container with the name [`container_ci-pyt_vllm_deepseek-moe-16b-chat`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in the following path: [`~/MAD/reports_float16/`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-v0901-20250605){.reference .internal} are preconfigured to collect latency and throughput performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
::::

Standalone benchmarking

::::::::::::
{.sd-tab-content .docutils}
Run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.9.0.1_20250605/images/sha256-f48beeb3d72663a93c77211eb45273d564451447c097e060befa713d565fa36c){.reference .external} as shown in the following snippet.

:
{.highlight-default .notranslate}

highlight
    docker pull rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605
    docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --shm-size 16G --security-opt seccomp=unconfined --security-opt apparmor=unconfined --cap-add=SYS_PTRACE -v $(pwd):/workspace --env HUGGINGFACE_HUB_CACHE=/workspace --name test rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605

:

In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at [`~/MAD/scripts/vllm`{.docutils .literal .notranslate}]{.pre}.

:
{.highlight-default .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD/scripts/vllm

:

To start the benchmark, use the following command with the appropriate options.

:
{.highlight-default .notranslate}

highlight
    ./vllm_benchmark_report.sh -s $test_option -m deepseek-ai/deepseek-moe-16b-chat -g $num_gpu -d float16

:

pst-scrollable-table-container
  Name                                                      Options                                                                                                   Description
  --------------------------------------------------------- --------------------------------------------------------------------------------------------------------- -------------------------------------
  [`$test_option`{.docutils .literal .notranslate}]{.pre}   latency                                                                                                   Measure decoding token latency
                                                            throughput                                                                                                Measure token generation throughput
                                                            all                                                                                                       Measure both throughput and latency
  [`$num_gpu`{.docutils .literal .notranslate}]{.pre}       1 or 8                                                                                                    Number of GPUs
  [`$datatype`{.docutils .literal .notranslate}]{.pre}      [`float16`{.docutils .literal .notranslate}]{.pre} or [`float8`{.docutils .literal .notranslate}]{.pre}   Data type

{.admonition .note}
Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don't need to specify them with this script.

::
{.admonition .note}
Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:
{.highlight-default .notranslate}

highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token

:
::

Here are some examples of running the benchmark with various options.

- Latency benchmark

  Use this command to benchmark the latency of the DeepSeek MoE 16B model on eight GPUs with [`float16`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-default .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s latency -m deepseek-ai/deepseek-moe-16b-chat -g 8 -d float16
  
  :

  Find the latency report at [`./reports_float16_vllm_rocm6.4.1/summary/deepseek-moe-16b-chat_latency_report.csv`{.docutils .literal .notranslate}]{.pre}.

- Throughput benchmark

  Use this command to benchmark the throughput of the DeepSeek MoE 16B model on eight GPUs with [`float16`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-shell .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s throughput -m deepseek-ai/deepseek-moe-16b-chat -g 8 -d float16
  
  :

  Find the throughput report at [`./reports_float16_vllm_rocm6.4.1/summary/deepseek-moe-16b-chat_throughput_report.csv`{.docutils .literal .notranslate}]{.pre}.

{.admonition .note}
Note

Throughput is calculated as:

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  

::::::::::::
::::::::::::::::::
:::::::::::::::::::

:::::::::::::::::::
{.model-doc .pyt-vllm-phi-4 .docutils .container}
::::::::::::::::::
{.sd-tab-set .docutils}
MAD-integrated benchmarking

::::
{.sd-tab-content .docutils}
Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

:
{.highlight-shell .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD
    pip install -r requirements.txt

:

Use this command to run the performance benchmark test on the [Phi-4](https://huggingface.co/microsoft/phi-4){.reference .external} model using one GPU with the :literal:\`\` data type on the host machine.

:
{.highlight-shell .notranslate}

highlight
    export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
    python3 tools/run_models.py --tags pyt_vllm_phi-4 --keep-model-dir --live-output --timeout 28800

:

MAD launches a Docker container with the name [`container_ci-pyt_vllm_phi-4`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in the following path: [`~/MAD/reports_/`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-v0901-20250605){.reference .internal} are preconfigured to collect latency and throughput performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
::::

Standalone benchmarking

::::::::::::
{.sd-tab-content .docutils}
Run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.9.0.1_20250605/images/sha256-f48beeb3d72663a93c77211eb45273d564451447c097e060befa713d565fa36c){.reference .external} as shown in the following snippet.

:
{.highlight-default .notranslate}

highlight
    docker pull rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605
    docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --shm-size 16G --security-opt seccomp=unconfined --security-opt apparmor=unconfined --cap-add=SYS_PTRACE -v $(pwd):/workspace --env HUGGINGFACE_HUB_CACHE=/workspace --name test rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605

:

In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at [`~/MAD/scripts/vllm`{.docutils .literal .notranslate}]{.pre}.

:
{.highlight-default .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD/scripts/vllm

:

To start the benchmark, use the following command with the appropriate options.

:
{.highlight-default .notranslate}

highlight
    ./vllm_benchmark_report.sh -s $test_option -m microsoft/phi-4 -g $num_gpu -d 

:

pst-scrollable-table-container
  Name                                                      Options                                                                                                   Description
  --------------------------------------------------------- --------------------------------------------------------------------------------------------------------- -------------------------------------
  [`$test_option`{.docutils .literal .notranslate}]{.pre}   latency                                                                                                   Measure decoding token latency
                                                            throughput                                                                                                Measure token generation throughput
                                                            all                                                                                                       Measure both throughput and latency
  [`$num_gpu`{.docutils .literal .notranslate}]{.pre}       1 or 8                                                                                                    Number of GPUs
  [`$datatype`{.docutils .literal .notranslate}]{.pre}      [`float16`{.docutils .literal .notranslate}]{.pre} or [`float8`{.docutils .literal .notranslate}]{.pre}   Data type

{.admonition .note}
Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don't need to specify them with this script.

::
{.admonition .note}
Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:
{.highlight-default .notranslate}

highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token

:
::

Here are some examples of running the benchmark with various options.

- Latency benchmark

  Use this command to benchmark the latency of the Phi-4 model on eight GPUs with :literal:\`\` precision.

  :
{.highlight-default .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s latency -m microsoft/phi-4 -g 8 -d 
  
  :

  Find the latency report at [`./reports__vllm_rocm6.4.1/summary/phi-4_latency_report.csv`{.docutils .literal .notranslate}]{.pre}.

- Throughput benchmark

  Use this command to benchmark the throughput of the Phi-4 model on eight GPUs with :literal:\`\` precision.

  :
{.highlight-shell .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s throughput -m microsoft/phi-4 -g 8 -d 
  
  :

  Find the throughput report at [`./reports__vllm_rocm6.4.1/summary/phi-4_throughput_report.csv`{.docutils .literal .notranslate}]{.pre}.

{.admonition .note}
Note

Throughput is calculated as:

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  

::::::::::::
::::::::::::::::::
:::::::::::::::::::

:::::::::::::::::::
{.model-doc .pyt-vllm-falcon-180b .docutils .container}
::::::::::::::::::
{.sd-tab-set .docutils}
MAD-integrated benchmarking

::::
{.sd-tab-content .docutils}
Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

:
{.highlight-shell .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD
    pip install -r requirements.txt

:

Use this command to run the performance benchmark test on the [Falcon 180B](https://huggingface.co/tiiuae/falcon-180B){.reference .external} model using one GPU with the [`float16`{.docutils .literal .notranslate}]{.pre} data type on the host machine.

:
{.highlight-shell .notranslate}

highlight
    export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
    python3 tools/run_models.py --tags pyt_vllm_falcon-180b --keep-model-dir --live-output --timeout 28800

:

MAD launches a Docker container with the name [`container_ci-pyt_vllm_falcon-180b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in the following path: [`~/MAD/reports_float16/`{.docutils .literal .notranslate}]{.pre}.

Although the [[available models]{.std .std-ref}](#vllm-benchmark-available-models-v0901-20250605){.reference .internal} are preconfigured to collect latency and throughput performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
::::

Standalone benchmarking

::::::::::::
{.sd-tab-content .docutils}
Run the vLLM benchmark tool independently by starting the [Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.9.0.1_20250605/images/sha256-f48beeb3d72663a93c77211eb45273d564451447c097e060befa713d565fa36c){.reference .external} as shown in the following snippet.

:
{.highlight-default .notranslate}

highlight
    docker pull rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605
    docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --shm-size 16G --security-opt seccomp=unconfined --security-opt apparmor=unconfined --cap-add=SYS_PTRACE -v $(pwd):/workspace --env HUGGINGFACE_HUB_CACHE=/workspace --name test rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605

:

In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at [`~/MAD/scripts/vllm`{.docutils .literal .notranslate}]{.pre}.

:
{.highlight-default .notranslate}

highlight
    git clone https://github.com/ROCm/MAD
    cd MAD/scripts/vllm

:

To start the benchmark, use the following command with the appropriate options.

:
{.highlight-default .notranslate}

highlight
    ./vllm_benchmark_report.sh -s $test_option -m tiiuae/falcon-180B -g $num_gpu -d float16

:

pst-scrollable-table-container
  Name                                                      Options                                                                                                   Description
  --------------------------------------------------------- --------------------------------------------------------------------------------------------------------- -------------------------------------
  [`$test_option`{.docutils .literal .notranslate}]{.pre}   latency                                                                                                   Measure decoding token latency
                                                            throughput                                                                                                Measure token generation throughput
                                                            all                                                                                                       Measure both throughput and latency
  [`$num_gpu`{.docutils .literal .notranslate}]{.pre}       1 or 8                                                                                                    Number of GPUs
  [`$datatype`{.docutils .literal .notranslate}]{.pre}      [`float16`{.docutils .literal .notranslate}]{.pre} or [`float8`{.docutils .literal .notranslate}]{.pre}   Data type

{.admonition .note}
Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don't need to specify them with this script.

::
{.admonition .note}
Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:
{.highlight-default .notranslate}

highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token

:
::

Here are some examples of running the benchmark with various options.

- Latency benchmark

  Use this command to benchmark the latency of the Falcon 180B model on eight GPUs with [`float16`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-default .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s latency -m tiiuae/falcon-180B -g 8 -d float16
  
  :

  Find the latency report at [`./reports_float16_vllm_rocm6.4.1/summary/falcon-180B_latency_report.csv`{.docutils .literal .notranslate}]{.pre}.

- Throughput benchmark

  Use this command to benchmark the throughput of the Falcon 180B model on eight GPUs with [`float16`{.docutils .literal .notranslate}]{.pre} precision.

  :
{.highlight-shell .notranslate}
  
highlight
      ./vllm_benchmark_report.sh -s throughput -m tiiuae/falcon-180B -g 8 -d float16
  
  :

  Find the throughput report at [`./reports_float16_vllm_rocm6.4.1/summary/falcon-180B_throughput_report.csv`{.docutils .literal .notranslate}]{.pre}.

{.admonition .note}
Note

Throughput is calculated as:

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  

- 
{.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  

::::::::::::
::::::::::::::::::
:::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

{#further-reading .section}
## Further reading[\#](#further-reading "Link to this heading"){.headerlink}

- To learn more about the options for latency and throughput benchmark scripts, see [ROCm/vllm](https://github.com/ROCm/vllm/tree/main/benchmarks){.github .reference .external}.

- To learn more about system settings and management practices to configure your system for MI300X GPUs, see [AMD Instinct MI300X system optimization](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi300x.html){.reference .external}

- For application performance optimization strategies for HPC and AI workloads, including inference with vLLM, see [[AMD Instinct MI300X workload optimization]{.doc}](../../../inference-optimization/workload.html){.reference .internal}.

- To learn how to run community models from Hugging Face on AMD GPUs, see [[Running models from Hugging Face]{.doc}](../../hugging-face-models.html){.reference .internal}.

- To learn how to fine-tune LLMs and optimize inference, see [[Fine-tuning LLMs and inference optimization]{.doc}](../../../fine-tuning/fine-tuning-and-inference.html){.reference .internal}.

- For a list of other ready-made Docker images for AI with ROCm, see [AMD Infinity Hub](https://www.amd.com/en/developer/resources/infinity-hub.html#f-amd_hub_category=AI%20%26%20ML%20Models){.reference .external}.

{#previous-versions .section}
## Previous versions[\#](#previous-versions "Link to this heading"){.headerlink}

See [[vLLM inference performance testing version history]{.doc}](vllm-history.html){.reference .internal} to find documentation for previous releases of the [`ROCm/vllm`{.docutils .literal .notranslate}]{.pre} Docker image.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

{.bd-sidebar-secondary .bd-toc}
::
{.sidebar-secondary-items .sidebar-secondary__inner}
:
sidebar-secondary-item

{.page-toc .tocsection .onthispage}
Contents

:
::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
