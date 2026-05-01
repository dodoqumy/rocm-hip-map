---
title: "LLM inference performance validation on AMD Instinct MI300X"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference/benchmark-docker/previous-versions/vllm-0.6.6.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-01
---

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-content
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-article-container
:::::::::: {.bd-header-article .d-print-none}
::::::::: {.header-article-items .header-article__inner}
::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}
:::

::: header-article-item
- [](../../../../../index.html){.nav-link aria-label="Home"}
- LLM\...
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
# LLM inference performance validation on AMD Instinct MI300X

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [Getting started](#getting-started){.reference .internal .nav-link}
- [MAD-integrated benchmarking](#mad-integrated-benchmarking){.reference .internal .nav-link}
  - [Available models](#available-models){.reference .internal .nav-link}
- [Standalone benchmarking](#standalone-benchmarking){.reference .internal .nav-link}
  - [Command](#command){.reference .internal .nav-link}
  - [Options and available models](#options-and-available-models){.reference .internal .nav-link}
  - [Running the benchmark on the MI300X GPU](#running-the-benchmark-on-the-mi300x-gpu){.reference .internal .nav-link}
    - [Example 1: latency benchmark](#example-1-latency-benchmark){.reference .internal .nav-link}
    - [Example 2: throughput benchmark](#example-2-throughput-benchmark){.reference .internal .nav-link}
- [Further reading](#further-reading){.reference .internal .nav-link}
- [Previous versions](#previous-versions){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

:::::::::::::::::::::::::::::::::::::::::::::: {#llm-inference-performance-validation-on-amd-instinct-mi300x .section}
# LLM inference performance validation on AMD Instinct MI300X[\#](#llm-inference-performance-validation-on-amd-instinct-mi300x "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-04-21
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 10 min read time
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

The [ROCm vLLM Docker](https://hub.docker.com/r/rocm/vllm/tags){.reference .external} image offers a prebuilt, optimized environment for validating large language model (LLM) inference performance on the AMD Instinct™ MI300X GPU. This ROCm vLLM Docker image integrates vLLM and PyTorch tailored specifically for the MI300X GPU and includes the following components:

- [ROCm 6.3.1](https://github.com/ROCm/ROCm){.reference .external}

- [vLLM 0.6.6](https://docs.vllm.ai/en/latest){.reference .external}

- [PyTorch 2.7.0 (2.7.0a0+git3a58512)](https://github.com/pytorch/pytorch){.reference .external}

With this Docker image, you can quickly validate the expected inference performance numbers for the MI300X GPU. This topic also provides tips on optimizing performance with popular AI models. For more information, see the lists of [[available models for MAD-integrated benchmarking]{.std .std-ref}](#vllm-benchmark-mad-v066-models){.reference .internal} and [[standalone benchmarking]{.std .std-ref}](#vllm-benchmark-standalone-v066-options){.reference .internal}.

::: {#vllm-benchmark-vllm .admonition .note}
Note

vLLM is a toolkit and library for LLM inference and serving. AMD implements high-performance custom kernels and modules in vLLM to enhance performance. See [[vLLM inference]{.std .std-ref}](../../llm-inference-frameworks.html#fine-tuning-llms-vllm){.reference .internal} and [[vLLM V1 performance optimization]{.std .std-ref}](../../../inference-optimization/vllm-optimization.html#mi300x-vllm-optimization){.reference .internal} for more information.
:::

::: {#getting-started .section}
## Getting started[\#](#getting-started "Link to this heading"){.headerlink}

Use the following procedures to reproduce the benchmark results on an MI300X GPU with the prebuilt vLLM Docker image.

1.  Disable NUMA auto-balancing.

    To optimize performance, disable automatic NUMA balancing. Otherwise, the GPU might hang until the periodic balancing is finalized. For more information, see the [[system validation steps]{.std .std-ref}](../../../system-setup/prerequisite-system-validation.html#rocm-for-ai-system-optimization){.reference .internal}.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # disable automatic NUMA balancing
        sh -c 'echo 0 > /proc/sys/kernel/numa_balancing'
        # check if NUMA balancing is disabled (returns 0 if disabled)
        cat /proc/sys/kernel/numa_balancing
        0
    :::
    ::::

2.  Download the [[ROCm vLLM Docker image]{.std .std-ref}](vllm-0.9.0.1-20250605.html#vllm-benchmark-unified-docker){.reference .internal}.

    Use the following command to pull the Docker image from Docker Hub.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker pull rocm/vllm:rocm6.3.1_mi300_ubuntu22.04_py3.12_vllm_0.6.6
    :::
    ::::

Once the setup is complete, choose between two options to reproduce the benchmark results:

- [[MAD-integrated benchmarking]{.std .std-ref}](#vllm-benchmark-mad-v066){.reference .internal}

- [[Standalone benchmarking]{.std .std-ref}](#vllm-benchmark-standalone-v066){.reference .internal}
:::

::::::::: {#mad-integrated-benchmarking .section}
[]{#vllm-benchmark-mad-v066}

## MAD-integrated benchmarking[\#](#mad-integrated-benchmarking "Link to this heading"){.headerlink}

Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

:::: {.highlight-shell .notranslate}
::: highlight
    git clone https://github.com/ROCm/MAD
    cd MAD
    pip install -r requirements.txt
:::
::::

Use this command to run a performance benchmark test of the Llama 3.1 8B model on one GPU with [`float16`{.docutils .literal .notranslate}]{.pre} data type in the host machine.

:::: {.highlight-shell .notranslate}
::: highlight
    export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
    python3 tools/run_models.py --tags pyt_vllm_llama-3.1-8b --keep-model-dir --live-output --timeout 28800
:::
::::

ROCm MAD launches a Docker container with the name [`container_ci-pyt_vllm_llama-3.1-8b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in the following path: [`~/MAD/reports_float16/`{.docutils .literal .notranslate}]{.pre}.

Although the following models are preconfigured to collect latency and throughput performance data, you can also change the benchmarking parameters. Refer to the [[Standalone benchmarking]{.std .std-ref}](#vllm-benchmark-standalone-v066){.reference .internal} section.

:::: {#available-models .section}
[]{#vllm-benchmark-mad-v066-models}

### Available models[\#](#available-models "Link to this heading"){.headerlink}

::: pst-scrollable-table-container
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| Model name                                                                                                      | Tag                                                                               |
+=================================================================================================================+===================================================================================+
| [Llama 3.1 8B](https://huggingface.co/meta-llama/Llama-3.1-8B){.reference .external}                            | [`pyt_vllm_llama-3.1-8b`{.docutils .literal .notranslate}]{.pre}                  |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| [Llama 3.1 70B](https://huggingface.co/meta-llama/Llama-3.1-70B-Instruct){.reference .external}                 | [`pyt_vllm_llama-3.1-70b`{.docutils .literal .notranslate}]{.pre}                 |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| [Llama 3.1 405B](https://huggingface.co/meta-llama/Llama-3.1-405B-Instruct){.reference .external}               | [`pyt_vllm_llama-3.1-405b`{.docutils .literal .notranslate}]{.pre}                |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| [Llama 3.2 11B Vision](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct){.reference .external}   | [`pyt_vllm_llama-3.2-11b-vision-instruct`{.docutils .literal .notranslate}]{.pre} |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| [Llama 2 7B](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf){.reference .external}                        | [`pyt_vllm_llama-2-7b`{.docutils .literal .notranslate}]{.pre}                    |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| [Llama 2 70B](https://huggingface.co/meta-llama/Llama-2-70b-chat-hf){.reference .external}                      | [`pyt_vllm_llama-2-70b`{.docutils .literal .notranslate}]{.pre}                   |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| [Mixtral MoE 8x7B](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1){.reference .external}           | [`pyt_vllm_mixtral-8x7b`{.docutils .literal .notranslate}]{.pre}                  |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| [Mixtral MoE 8x22B](https://huggingface.co/mistralai/Mixtral-8x22B-Instruct-v0.1){.reference .external}         | [`pyt_vllm_mixtral-8x22b`{.docutils .literal .notranslate}]{.pre}                 |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| [Mistral 7B](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3){.reference .external}                   | [`pyt_vllm_mistral-7b`{.docutils .literal .notranslate}]{.pre}                    |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| [Qwen2 7B](https://huggingface.co/Qwen/Qwen2-7B-Instruct){.reference .external}                                 | [`pyt_vllm_qwen2-7b`{.docutils .literal .notranslate}]{.pre}                      |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| [Qwen2 72B](https://huggingface.co/Qwen/Qwen2-72B-Instruct){.reference .external}                               | [`pyt_vllm_qwen2-72b`{.docutils .literal .notranslate}]{.pre}                     |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| [JAIS 13B](https://huggingface.co/core42/jais-13b-chat){.reference .external}                                   | [`pyt_vllm_jais-13b`{.docutils .literal .notranslate}]{.pre}                      |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| [JAIS 30B](https://huggingface.co/core42/jais-30b-chat-v3){.reference .external}                                | [`pyt_vllm_jais-30b`{.docutils .literal .notranslate}]{.pre}                      |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| [DBRX Instruct](https://huggingface.co/databricks/dbrx-instruct){.reference .external}                          | [`pyt_vllm_dbrx-instruct`{.docutils .literal .notranslate}]{.pre}                 |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| [Gemma 2 27B](https://huggingface.co/google/gemma-2-27b){.reference .external}                                  | [`pyt_vllm_gemma-2-27b`{.docutils .literal .notranslate}]{.pre}                   |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| [C4AI Command R+ 08-2024](https://huggingface.co/CohereForAI/c4ai-command-r-plus-08-2024){.reference .external} | [`pyt_vllm_c4ai-command-r-plus-08-2024`{.docutils .literal .notranslate}]{.pre}   |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| [DeepSeek MoE 16B](https://huggingface.co/deepseek-ai/deepseek-moe-16b-chat){.reference .external}              | [`pyt_vllm_deepseek-moe-16b-chat`{.docutils .literal .notranslate}]{.pre}         |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| [Llama 3.1 70B FP8](https://huggingface.co/amd/Llama-3.1-70B-Instruct-FP8-KV){.reference .external}             | [`pyt_vllm_llama-3.1-70b_fp8`{.docutils .literal .notranslate}]{.pre}             |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| [Llama 3.1 405B FP8](https://huggingface.co/amd/Llama-3.1-405B-Instruct-FP8-KV){.reference .external}           | [`pyt_vllm_llama-3.1-405b_fp8`{.docutils .literal .notranslate}]{.pre}            |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| [Mixtral MoE 8x7B FP8](https://huggingface.co/amd/Mixtral-8x7B-Instruct-v0.1-FP8-KV){.reference .external}      | [`pyt_vllm_mixtral-8x7b_fp8`{.docutils .literal .notranslate}]{.pre}              |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| [Mixtral MoE 8x22B FP8](https://huggingface.co/amd/Mixtral-8x22B-Instruct-v0.1-FP8-KV){.reference .external}    | [`pyt_vllm_mixtral-8x22b_fp8`{.docutils .literal .notranslate}]{.pre}             |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| [Mistral 7B FP8](https://huggingface.co/amd/Mistral-7B-v0.1-FP8-KV){.reference .external}                       | [`pyt_vllm_mistral-7b_fp8`{.docutils .literal .notranslate}]{.pre}                |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| [DBRX Instruct FP8](https://huggingface.co/amd/dbrx-instruct-FP8-KV){.reference .external}                      | [`pyt_vllm_dbrx_fp8`{.docutils .literal .notranslate}]{.pre}                      |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| [C4AI Command R+ 08-2024 FP8](https://huggingface.co/amd/c4ai-command-r-plus-FP8-KV){.reference .external}      | [`pyt_vllm_command-r-plus_fp8`{.docutils .literal .notranslate}]{.pre}            |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
:::
::::
:::::::::

:::::::::::::::::::::::: {#standalone-benchmarking .section}
[]{#vllm-benchmark-standalone-v066}

## Standalone benchmarking[\#](#standalone-benchmarking "Link to this heading"){.headerlink}

You can run the vLLM benchmark tool independently by starting the [[Docker container]{.std .std-ref}](vllm-0.7.3-20250325.html#vllm-benchmark-get-started){.reference .internal} as shown in the following snippet.

:::: {.highlight-default .notranslate}
::: highlight
    docker pull rocm/vllm:rocm6.3.1_mi300_ubuntu22.04_py3.12_vllm_0.6.6
    docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --shm-size 16G --security-opt seccomp=unconfined --security-opt apparmor=unconfined --cap-add=SYS_PTRACE -v $(pwd):/workspace --env HUGGINGFACE_HUB_CACHE=/workspace --name vllm_v0.6.6 rocm/vllm:rocm6.3.1_mi300_ubuntu22.04_py3.12_vllm_0.6.6
:::
::::

In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at [`~/MAD/scripts/vllm`{.docutils .literal .notranslate}]{.pre}.

:::: {.highlight-default .notranslate}
::: highlight
    git clone https://github.com/ROCm/MAD
    cd MAD/scripts/vllm
:::
::::

::::::::: {#command .section}
### Command[\#](#command "Link to this heading"){.headerlink}

To start the benchmark, use the following command with the appropriate options. See [[Options]{.std .std-ref}](#vllm-benchmark-standalone-v066-options){.reference .internal} for the list of options and their descriptions.

:::: {.highlight-shell .notranslate}
::: highlight
    ./vllm_benchmark_report.sh -s $test_option -m $model_repo -g $num_gpu -d $datatype
:::
::::

See the [[examples]{.std .std-ref}](#vllm-benchmark-run-benchmark-v066){.reference .internal} for more information.

::: {.admonition .note}
Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don't need to specify them with this script.
:::

::::: {.admonition .note}
Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:::: {.highlight-shell .notranslate}
::: highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token
:::
::::
:::::
:::::::::

:::: {#options-and-available-models .section}
[]{#vllm-benchmark-standalone-v066-options}

### Options and available models[\#](#options-and-available-models "Link to this heading"){.headerlink}

::: pst-scrollable-table-container
  Name                                                      Options                                                                                                   Description
  --------------------------------------------------------- --------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------
  [`$test_option`{.docutils .literal .notranslate}]{.pre}   latency                                                                                                   Measure decoding token latency
                                                            throughput                                                                                                Measure token generation throughput
                                                            all                                                                                                       Measure both throughput and latency
  [`$model_repo`{.docutils .literal .notranslate}]{.pre}    [`meta-llama/Llama-3.1-8B-Instruct`{.docutils .literal .notranslate}]{.pre}                               [Llama 3.1 8B](https://huggingface.co/meta-llama/Llama-3.1-8B){.reference .external}
  ([`float16`{.docutils .literal .notranslate}]{.pre})      [`meta-llama/Llama-3.1-70B-Instruct`{.docutils .literal .notranslate}]{.pre}                              [Llama 3.1 70B](https://huggingface.co/meta-llama/Llama-3.1-70B-Instruct){.reference .external}
                                                            [`meta-llama/Llama-3.1-405B-Instruct`{.docutils .literal .notranslate}]{.pre}                             [Llama 3.1 405B](https://huggingface.co/meta-llama/Llama-3.1-405B-Instruct){.reference .external}
                                                            [`meta-llama/Llama-3.2-11B-Vision-Instruct`{.docutils .literal .notranslate}]{.pre}                       [Llama 3.2 11B Vision](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct){.reference .external}
                                                            [`meta-llama/Llama-2-7b-chat-hf`{.docutils .literal .notranslate}]{.pre}                                  [Llama 2 7B](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf){.reference .external}
                                                            [`meta-llama/Llama-2-70b-chat-hf`{.docutils .literal .notranslate}]{.pre}                                 [Llama 2 70B](https://huggingface.co/meta-llama/Llama-2-70b-chat-hf){.reference .external}
                                                            [`mistralai/Mixtral-8x7B-Instruct-v0.1`{.docutils .literal .notranslate}]{.pre}                           [Mixtral MoE 8x7B](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1){.reference .external}
                                                            [`mistralai/Mixtral-8x22B-Instruct-v0.1`{.docutils .literal .notranslate}]{.pre}                          [Mixtral MoE 8x22B](https://huggingface.co/mistralai/Mixtral-8x22B-Instruct-v0.1){.reference .external}
                                                            [`mistralai/Mistral-7B-Instruct-v0.3`{.docutils .literal .notranslate}]{.pre}                             [Mistral 7B](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3){.reference .external}
                                                            [`Qwen/Qwen2-7B-Instruct`{.docutils .literal .notranslate}]{.pre}                                         [Qwen2 7B](https://huggingface.co/Qwen/Qwen2-7B-Instruct){.reference .external}
                                                            [`Qwen/Qwen2-72B-Instruct`{.docutils .literal .notranslate}]{.pre}                                        [Qwen2 72B](https://huggingface.co/Qwen/Qwen2-72B-Instruct){.reference .external}
                                                            [`core42/jais-13b-chat`{.docutils .literal .notranslate}]{.pre}                                           [JAIS 13B](https://huggingface.co/core42/jais-13b-chat){.reference .external}
                                                            [`core42/jais-30b-chat-v3`{.docutils .literal .notranslate}]{.pre}                                        [JAIS 30B](https://huggingface.co/core42/jais-30b-chat-v3){.reference .external}
                                                            [`databricks/dbrx-instruct`{.docutils .literal .notranslate}]{.pre}                                       [DBRX Instruct](https://huggingface.co/databricks/dbrx-instruct){.reference .external}
                                                            [`google/gemma-2-27b`{.docutils .literal .notranslate}]{.pre}                                             [Gemma 2 27B](https://huggingface.co/google/gemma-2-27b){.reference .external}
                                                            [`CohereForAI/c4ai-command-r-plus-08-2024`{.docutils .literal .notranslate}]{.pre}                        [C4AI Command R+ 08-2024](https://huggingface.co/CohereForAI/c4ai-command-r-plus-08-2024){.reference .external}
                                                            [`deepseek-ai/deepseek-moe-16b-chat`{.docutils .literal .notranslate}]{.pre}                              [DeepSeek MoE 16B](https://huggingface.co/deepseek-ai/deepseek-moe-16b-chat){.reference .external}
  [`$model_repo`{.docutils .literal .notranslate}]{.pre}    [`amd/Llama-3.1-70B-Instruct-FP8-KV`{.docutils .literal .notranslate}]{.pre}                              [Llama 3.1 70B FP8](https://huggingface.co/amd/Llama-3.1-70B-Instruct-FP8-KV){.reference .external}
  ([`float8`{.docutils .literal .notranslate}]{.pre})       [`amd/Llama-3.1-405B-Instruct-FP8-KV`{.docutils .literal .notranslate}]{.pre}                             [Llama 3.1 405B FP8](https://huggingface.co/amd/Llama-3.1-405B-Instruct-FP8-KV){.reference .external}
                                                            [`amd/Mixtral-8x7B-Instruct-v0.1-FP8-KV`{.docutils .literal .notranslate}]{.pre}                          [Mixtral MoE 8x7B FP8](https://huggingface.co/amd/Mixtral-8x7B-Instruct-v0.1-FP8-KV){.reference .external}
                                                            [`amd/Mixtral-8x22B-Instruct-v0.1-FP8-KV`{.docutils .literal .notranslate}]{.pre}                         [Mixtral MoE 8x22B FP8](https://huggingface.co/amd/Mixtral-8x22B-Instruct-v0.1-FP8-KV){.reference .external}
                                                            [`amd/Mistral-7B-v0.1-FP8-KV`{.docutils .literal .notranslate}]{.pre}                                     [Mistral 7B FP8](https://huggingface.co/amd/Mistral-7B-v0.1-FP8-KV){.reference .external}
                                                            [`amd/dbrx-instruct-FP8-KV`{.docutils .literal .notranslate}]{.pre}                                       [DBRX Instruct FP8](https://huggingface.co/amd/dbrx-instruct-FP8-KV){.reference .external}
                                                            [`amd/c4ai-command-r-plus-FP8-KV`{.docutils .literal .notranslate}]{.pre}                                 [C4AI Command R+ 08-2024 FP8](https://huggingface.co/amd/c4ai-command-r-plus-FP8-KV){.reference .external}
  [`$num_gpu`{.docutils .literal .notranslate}]{.pre}       1 or 8                                                                                                    Number of GPUs
  [`$datatype`{.docutils .literal .notranslate}]{.pre}      [`float16`{.docutils .literal .notranslate}]{.pre} or [`float8`{.docutils .literal .notranslate}]{.pre}   Data type
:::
::::

:::::::::: {#running-the-benchmark-on-the-mi300x-gpu .section}
[]{#vllm-benchmark-run-benchmark-v066}

### Running the benchmark on the MI300X GPU[\#](#running-the-benchmark-on-the-mi300x-gpu "Link to this heading"){.headerlink}

Here are some examples of running the benchmark with various options. See [[Options]{.std .std-ref}](#vllm-benchmark-standalone-v066-options){.reference .internal} for the list of options and their descriptions.

::::: {#example-1-latency-benchmark .section}
#### Example 1: latency benchmark[\#](#example-1-latency-benchmark "Link to this heading"){.headerlink}

Use this command to benchmark the latency of the Llama 3.1 70B model on eight GPUs with the [`float16`{.docutils .literal .notranslate}]{.pre} and [`float8`{.docutils .literal .notranslate}]{.pre} data types.

:::: {.highlight-default .notranslate}
::: highlight
    ./vllm_benchmark_report.sh -s latency -m meta-llama/Llama-3.1-70B-Instruct -g 8 -d float16
    ./vllm_benchmark_report.sh -s latency -m amd/Llama-3.1-70B-Instruct-FP8-KV -g 8 -d float8
:::
::::

Find the latency reports at:

- [`./reports_float16/summary/Llama-3.1-70B-Instruct_latency_report.csv`{.docutils .literal .notranslate}]{.pre}

- [`./reports_float8/summary/Llama-3.1-70B-Instruct-FP8-KV_latency_report.csv`{.docutils .literal .notranslate}]{.pre}
:::::

:::::: {#example-2-throughput-benchmark .section}
#### Example 2: throughput benchmark[\#](#example-2-throughput-benchmark "Link to this heading"){.headerlink}

Use this command to benchmark the throughput of the Llama 3.1 70B model on eight GPUs with the [`float16`{.docutils .literal .notranslate}]{.pre} and [`float8`{.docutils .literal .notranslate}]{.pre} data types.

:::: {.highlight-shell .notranslate}
::: highlight
    ./vllm_benchmark_report.sh -s throughput -m meta-llama/Llama-3.1-70B-Instruct -g 8 -d float16
    ./vllm_benchmark_report.sh -s throughput -m amd/Llama-3.1-70B-Instruct-FP8-KV -g 8 -d float8
:::
::::

Find the throughput reports at:

- [`./reports_float16/summary/Llama-3.1-70B-Instruct_throughput_report.csv`{.docutils .literal .notranslate}]{.pre}

- [`./reports_float8/summary/Llama-3.1-70B-Instruct-FP8-KV_throughput_report.csv`{.docutils .literal .notranslate}]{.pre}

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
::::::
::::::::::
::::::::::::::::::::::::

::: {#further-reading .section}
## Further reading[\#](#further-reading "Link to this heading"){.headerlink}

- For application performance optimization strategies for HPC and AI workloads, including inference with vLLM, see [[AMD Instinct MI300X workload optimization]{.doc}](../../../inference-optimization/workload.html){.reference .internal}.

- To learn more about the options for latency and throughput benchmark scripts, see [ROCm/vllm](https://github.com/ROCm/vllm/tree/main/benchmarks){.github .reference .external}.

- To learn more about system settings and management practices to configure your system for MI300X Series GPUs, see [AMD Instinct MI300X system optimization](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi300x.html){.reference .external}

- To learn how to run community models from Hugging Face on AMD GPUs, see [[Running models from Hugging Face]{.doc}](../../hugging-face-models.html){.reference .internal}.

- To learn how to fine-tune LLMs and optimize inference, see [[Fine-tuning LLMs and inference optimization]{.doc}](../../../fine-tuning/fine-tuning-and-inference.html){.reference .internal}.

- For a list of other ready-made Docker images for AI with ROCm, see [AMD Infinity Hub](https://www.amd.com/en/developer/resources/infinity-hub.html#f-amd_hub_category=AI%20%26%20ML%20Models){.reference .external}.
:::

::: {#previous-versions .section}
## Previous versions[\#](#previous-versions "Link to this heading"){.headerlink}

See [[vLLM inference performance testing version history]{.doc}](vllm-history.html){.reference .internal} to find documentation for previous releases of the [`ROCm/vllm`{.docutils .literal .notranslate}]{.pre} Docker image.
:::
::::::::::::::::::::::::::::::::::::::::::::::

::: prev-next-area
:::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::: {.bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {.page-toc .tocsection .onthispage}
Contents
:::

- [Getting started](#getting-started){.reference .internal .nav-link}
- [MAD-integrated benchmarking](#mad-integrated-benchmarking){.reference .internal .nav-link}
  - [Available models](#available-models){.reference .internal .nav-link}
- [Standalone benchmarking](#standalone-benchmarking){.reference .internal .nav-link}
  - [Command](#command){.reference .internal .nav-link}
  - [Options and available models](#options-and-available-models){.reference .internal .nav-link}
  - [Running the benchmark on the MI300X GPU](#running-the-benchmark-on-the-mi300x-gpu){.reference .internal .nav-link}
    - [Example 1: latency benchmark](#example-1-latency-benchmark){.reference .internal .nav-link}
    - [Example 2: throughput benchmark](#example-2-throughput-benchmark){.reference .internal .nav-link}
- [Further reading](#further-reading){.reference .internal .nav-link}
- [Previous versions](#previous-versions){.reference .internal .nav-link}
::::
:::::
::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
