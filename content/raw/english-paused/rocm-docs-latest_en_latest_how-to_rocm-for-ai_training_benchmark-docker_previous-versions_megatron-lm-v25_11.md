---
title: "Training a model with Megatron-LM on ROCm"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/training/benchmark-docker/previous-versions/megatron-lm-v25.11.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-01
---

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-content
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-article-container
:::::::::: {.bd-header-article .d-print-none}
::::::::: {.header-article-items .header-article__inner}
::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}
:::

::: header-article-item
- [](../../../../../index.html){.nav-link aria-label="Home"}
- Training a\...
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
# Training a model with Megatron-LM on ROCm

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [Supported models](#supported-models){.reference .internal .nav-link}
- [Performance measurements](#performance-measurements){.reference .internal .nav-link}
- [System validation](#system-validation){.reference .internal .nav-link}
- [Environment setup](#environment-setup){.reference .internal .nav-link}
  - [Download the Docker image](#download-the-docker-image){.reference .internal .nav-link}
- [Configuration](#configuration){.reference .internal .nav-link}
  - [Multi-node configuration](#multi-node-configuration){.reference .internal .nav-link}
  - [Tokenizer](#tokenizer){.reference .internal .nav-link}
  - [Dataset options](#dataset-options){.reference .internal .nav-link}
    - [Download the dataset](#download-the-dataset){.reference .internal .nav-link}
- [Run training](#run-training){.reference .internal .nav-link}
  - [Single node training](#single-node-training){.reference .internal .nav-link}
  - [Multi-node training examples](#multi-node-training-examples){.reference .internal .nav-link}
  - [Key options](#key-options){.reference .internal .nav-link}
- [Previous versions](#previous-versions){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#training-a-model-with-megatron-lm-on-rocm .section}
# Training a model with Megatron-LM on ROCm[\#](#training-a-model-with-megatron-lm-on-rocm "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-04-21
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 20 min read time
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

This documentation does not reflect the latest version of ROCm Megatron-LM training performance documentation. See [[Training a model with Megatron-LM on ROCm]{.doc}](../megatron-lm.html){.reference .internal} for the latest version.

For a unified training solution on AMD GPUs with ROCm, the [rocm/megatron-lm](https://hub.docker.com/r/rocm/megatron-lm/){.reference .external} Docker Hub registry will be deprecated soon in favor of [rocm/primus](https://hub.docker.com/r/rocm/primus){.reference .external}. The [`rocm/primus`{.docutils .literal .notranslate}]{.pre} Docker containers will cover PyTorch training ecosystem frameworks, including Megatron-LM and [[torchtitan]{.doc}](../primus-pytorch.html){.reference .internal}.

Primus with Megatron is designed to replace this ROCm Megatron-LM training workflow. To learn how to migrate workloads from Megatron-LM to Primus with Megatron, see [[Migrating workloads to Primus (Megatron backend) from Megatron-LM]{.doc}](megatron-lm-primus-migration-guide.html){.reference .internal}.
:::

The [Megatron-LM framework for ROCm](https://github.com/ROCm/Megatron-LM){.reference .external} is a specialized fork of the robust Megatron-LM, designed to enable efficient training of large-scale language models on AMD GPUs. By leveraging AMD Instinct™ GPUs, Megatron-LM delivers enhanced scalability, performance, and resource utilization for AI workloads. It is purpose-built to support models like Llama, DeepSeek, and Mixtral, enabling developers to train next-generation AI models more efficiently.

AMD provides ready-to-use Docker images for MI355X, MI350X, MI325X, and MI300X GPUs containing essential components, including PyTorch, ROCm libraries, and Megatron-LM utilities. It contains the following software components to accelerate training workloads:

::::: {.sd-tab-set .docutils}
rocm/primus:v25.11

:::: {.sd-tab-content .docutils}
::: pst-scrollable-table-container
  Software component   Version
  -------------------- ----------------------------
  ROCm                 7.1.0
  PyTorch              2.10.0.dev20251112+rocm7.1
  Python               3.10
  Transformer Engine   2.4.0.dev0+32e2d1d4
  Flash Attention      2.8.3
  hipBLASLt            1.2.0-09ab7153e2
  Triton               3.4.0
  RCCL                 2.27.7
:::
::::
:::::

::::::::::::::::::::::::: {#supported-models .section}
[]{#amd-megatron-lm-model-support-v25-11}

## Supported models[\#](#supported-models "Link to this heading"){.headerlink}

The following models are supported for training performance benchmarking with Megatron-LM and ROCm on AMD Instinct MI300X Series GPUs. Some instructions, commands, and training recommendations in this documentation might vary by model -- select one to get started.

:::::::::::::::::::::::: {#vllm-benchmark-ud-params-picker .container-fluid}
::::::::: {.row .gx-0}
::: {.col-2 .me-1 .px-2 .model-param-head}
Model
:::

::::::: {.row .col-10 .pe-0}
::: {.col-3 .px-2 .model-param param-k="model-group" param-v="llama" tabindex="0"}
Meta Llama
:::

::: {.col-3 .px-2 .model-param param-k="model-group" param-v="deepseek" tabindex="0"}
DeepSeek
:::

::: {.col-3 .px-2 .model-param param-k="model-group" param-v="mistral" tabindex="0"}
Mistral AI
:::

::: {.col-3 .px-2 .model-param param-k="model-group" param-v="qwen" tabindex="0"}
Qwen
:::
:::::::
:::::::::

:::::::::::::::: {.row .gx-0 .pt-1}
::: {.col-2 .me-1 .px-2 .model-param-head}
Variant
:::

:::::::::::::: {.row .col-10 .pe-0}
::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="pyt_megatron_lm_train_llama-3.3-70b" tabindex="0"}
Llama 3.3 70B
:::

::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="pyt_megatron_lm_train_llama-3.1-8b" tabindex="0"}
Llama 3.1 8B
:::

::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="pyt_megatron_lm_train_llama-3.1-70b" tabindex="0"}
Llama 3.1 70B
:::

::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="pyt_megatron_lm_train_llama-2-7b" tabindex="0"}
Llama 2 7B
:::

::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="pyt_megatron_lm_train_llama-2-70b" tabindex="0"}
Llama 2 70B
:::

::: {.col-6 .px-2 .model-param param-group="deepseek" param-k="model" param-v="pyt_megatron_lm_train_deepseek-v3-proxy" tabindex="0"}
DeepSeek-V3 (proxy)
:::

::: {.col-6 .px-2 .model-param param-group="deepseek" param-k="model" param-v="pyt_megatron_lm_train_deepseek-v2-lite-16b" tabindex="0"}
DeepSeek-V2-Lite
:::

::: {.col-6 .px-2 .model-param param-group="mistral" param-k="model" param-v="pyt_megatron_lm_train_mixtral-8x7b" tabindex="0"}
Mixtral 8x7B
:::

::: {.col-6 .px-2 .model-param param-group="mistral" param-k="model" param-v="pyt_megatron_lm_train_mixtral-8x22b-proxy" tabindex="0"}
Mixtral 8x22B (proxy)
:::

::: {.col-6 .px-2 .model-param param-group="qwen" param-k="model" param-v="pyt_megatron_lm_train_qwen2.5-7b" tabindex="0"}
Qwen 2.5 7B
:::

::: {.col-6 .px-2 .model-param param-group="qwen" param-k="model" param-v="pyt_megatron_lm_train_qwen2.5-72b" tabindex="0"}
Qwen 2.5 72B
:::
::::::::::::::
::::::::::::::::
::::::::::::::::::::::::
:::::::::::::::::::::::::

::: {.admonition .note}
Note

Some models, such as Llama, require an external license agreement through a third party (for example, Meta).
:::

:::: {#performance-measurements .section}
[]{#amd-megatron-lm-performance-measurements-v25-11}

## Performance measurements[\#](#performance-measurements "Link to this heading"){.headerlink}

To evaluate performance, the [Performance results with AMD ROCm software](https://www.amd.com/en/developer/resources/rocm-hub/dev-ai/performance-results.html#tabs-a8deaeb413-item-21cea50186-tab){.reference .external} page provides reference throughput and latency measurements for training popular AI models.

::: {.admonition .important}
Important

The performance data presented in [Performance results with AMD ROCm software](https://www.amd.com/en/developer/resources/rocm-hub/dev-ai/performance-results.html){.reference .external} only reflects the latest version of this training benchmarking environment. The listed measurements should not be interpreted as the peak performance achievable by AMD Instinct MI325X and MI300X GPUs or ROCm software.
:::
::::

::: {#system-validation .section}
## System validation[\#](#system-validation "Link to this heading"){.headerlink}

Before running AI workloads, it's important to validate that your AMD hardware is configured correctly and performing optimally.

If you have already validated your system settings, including aspects like NUMA auto-balancing, you can skip this step. Otherwise, complete the procedures in the [[System validation and optimization]{.std .std-ref}](../../../system-setup/prerequisite-system-validation.html#rocm-for-ai-system-optimization){.reference .internal} guide to properly configure your system settings before starting training.

To test for optimal performance, consult the recommended [[System health benchmarks]{.std .std-ref}](../../../system-setup/system-health-check.html#rocm-for-ai-system-health-bench){.reference .internal}. This suite of tests will help you verify and fine-tune your system's configuration.
:::

:::: {#environment-setup .section}
[]{#mi300x-amd-megatron-lm-training-v25-11}

## Environment setup[\#](#environment-setup "Link to this heading"){.headerlink}

Use the following instructions to set up the environment, configure the script to train models, and reproduce the benchmark results on MI300X Series GPUs with the AMD Megatron-LM Docker image.

::: {#download-the-docker-image .section}
[]{#amd-megatron-lm-requirements-v25-11}

### Download the Docker image[\#](#download-the-docker-image "Link to this heading"){.headerlink}

1.  Use the following command to pull the Docker image from Docker Hub.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker pull rocm/primus:v25.11
    :::
    ::::

2.  Launch the Docker container.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker run -it \
            --device /dev/dri \
            --device /dev/kfd \
            --device /dev/infiniband \
            --network host --ipc host \
            --group-add video \
            --cap-add SYS_PTRACE \
            --security-opt seccomp=unconfined \
            --privileged \
            -v $HOME:$HOME \
            -v $HOME/.ssh:/root/.ssh \
            --shm-size 128G \
            --name megatron_training_env \
            rocm/primus:v25.11
    :::
    ::::

<!-- -->

3.  Use these commands if you exit the [`megatron_training_env`{.docutils .literal .notranslate}]{.pre} container and need to return to it.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker start megatron_training_env
        docker exec -it megatron_training_env bash
    :::
    ::::

4.  **Megatron-LM backward compatibility setup** -- this Docker is primarily intended for use with Primus, but it maintains Megatron-LM compatibility with limited support. To roll back to using Megatron-LM, follow these steps:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        cd /workspace/Megatron-LM/
        pip uninstall megatron-core
        pip install -e .
    :::
    ::::

The Docker container hosts a verified commit of [ROCm/Megatron-LM](https://github.com/ROCm/Megatron-LM/tree/rocm_dev){.github .reference .external}.
:::
::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#configuration .section}
[]{#amd-megatron-lm-environment-setup-v25-11}

## Configuration[\#](#configuration "Link to this heading"){.headerlink}

::: {.model-doc .pyt-megatron-lm-train-llama-3-3-70b .pyt-megatron-lm-train-llama-3-1-8b .pyt-megatron-lm-train-llama-3-1-70b .docutils .container}
Update the [`train_llama3.sh`{.docutils .literal .notranslate}]{.pre} configuration script in the [`examples/llama`{.docutils .literal .notranslate}]{.pre} directory of [ROCm/Megatron-LM](https://github.com/ROCm/Megatron-LM/tree/rocm_dev/examples/llama){.github .reference .external} to configure your training run. Options can also be passed as command line arguments as described in [[Run training]{.std .std-ref}](#amd-megatron-lm-run-training-v25-11){.reference .internal}.
:::

::: {.model-doc .pyt-megatron-lm-train-llama-2-7b .pyt-megatron-lm-train-llama-2-70b .docutils .container}
Update the [`train_llama2.sh`{.docutils .literal .notranslate}]{.pre} configuration script in the [`examples/llama`{.docutils .literal .notranslate}]{.pre} directory of [ROCm/Megatron-LM](https://github.com/ROCm/Megatron-LM/tree/rocm_dev/examples/llama){.github .reference .external} to configure your training run. Options can also be passed as command line arguments as described in [[Run training]{.std .std-ref}](#amd-megatron-lm-run-training-v25-11){.reference .internal}.
:::

::: {.model-doc .pyt-megatron-lm-train-deepseek-v3-proxy .docutils .container}
Update the [`train_deepseekv3.sh`{.docutils .literal .notranslate}]{.pre} configuration script in the [`examples/deepseek_v3`{.docutils .literal .notranslate}]{.pre} directory of [ROCm/Megatron-LM](https://github.com/ROCm/Megatron-LM/tree/rocm_dev/examples/deepseek_v3){.github .reference .external} to configure your training run. Options can also be passed as command line arguments as described in [[Run training]{.std .std-ref}](#amd-megatron-lm-run-training-v25-11){.reference .internal}.
:::

::: {.model-doc .pyt-megatron-lm-train-deepseek-v2-lite-16b .docutils .container}
Update the [`train_deepseekv2.sh`{.docutils .literal .notranslate}]{.pre} configuration script in the [`examples/deepseek_v2`{.docutils .literal .notranslate}]{.pre} directory of [ROCm/Megatron-LM](https://github.com/ROCm/Megatron-LM/tree/rocm_dev/examples/deepseek_v2){.github .reference .external} to configure your training run. Options can also be passed as command line arguments as described in [[Run training]{.std .std-ref}](#amd-megatron-lm-run-training-v25-11){.reference .internal}.
:::

::: {.model-doc .pyt-megatron-lm-train-mixtral-8x7b .pyt-megatron-lm-train-mixtral-8x22b-proxy .docutils .container}
Update the [`train_mixtral_moe.sh`{.docutils .literal .notranslate}]{.pre} configuration script in the [`examples/mixtral`{.docutils .literal .notranslate}]{.pre} directory of [ROCm/Megatron-LM](https://github.com/ROCm/Megatron-LM/tree/rocm_dev/examples/mixtral){.github .reference .external} to configure your training run. Options can also be passed as command line arguments as described in [[Run training]{.std .std-ref}](#amd-megatron-lm-run-training-v25-11){.reference .internal}.
:::

::: {.admonition .note}
Note

See [[Key options]{.std .std-ref}](#amd-megatron-lm-benchmark-test-vars-v25-11){.reference .internal} for more information on configuration options.
:::

::: {#multi-node-configuration .section}
### Multi-node configuration[\#](#multi-node-configuration "Link to this heading"){.headerlink}

Refer to [[Multi-node setup for AI workloads]{.doc}](../../../system-setup/multi-node-setup.html){.reference .internal} to configure your environment for multi-node training. See [[Multi-node training examples]{.std .std-ref}](megatron-lm-v25.9.html#amd-megatron-lm-multi-node-examples){.reference .internal} for example run commands.
:::

:::::::::::::::::::::::::::::::: {#tokenizer .section}
[]{#amd-megatron-lm-tokenizer-v25-11}

### Tokenizer[\#](#tokenizer "Link to this heading"){.headerlink}

You can assign the path of an existing tokenizer to the [`TOKENIZER_MODEL`{.docutils .literal .notranslate}]{.pre} as shown in the following examples. If the tokenizer is not found, it'll be downloaded if publicly available.

::::::: {.model-doc .pyt-megatron-lm-train-llama-3-3-70b .docutils .container}
If you do not have Llama 3.3 tokenizer locally, you need to use your personal Hugging Face access token [`HF_TOKEN`{.docutils .literal .notranslate}]{.pre} to download the tokenizer. See [Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct){.reference .external}. After you are authorized, use your [`HF_TOKEN`{.docutils .literal .notranslate}]{.pre} to download the tokenizer and set the variable [`TOKENIZER_MODEL`{.docutils .literal .notranslate}]{.pre} to the tokenizer path.

:::: {.highlight-shell .notranslate}
::: highlight
    export HF_TOKEN=<Your personal Hugging Face access token>
:::
::::

The training script uses the [`HuggingFaceTokenizer`{.docutils .literal .notranslate}]{.pre}. Set [`TOKENIZER_MODEL`{.docutils .literal .notranslate}]{.pre} to the appropriate Hugging Face model path.

:::: {.highlight-shell .notranslate}
::: highlight
    TOKENIZER_MODEL="meta-llama/Llama-3.3-70B-Instruct"
:::
::::
:::::::

::::: {.model-doc .pyt-megatron-lm-train-llama-3-1-8b .docutils .container}
The training script uses the [`HuggingFaceTokenizer`{.docutils .literal .notranslate}]{.pre}. Set [`TOKENIZER_MODEL`{.docutils .literal .notranslate}]{.pre} to the appropriate Hugging Face model path.

:::: {.highlight-shell .notranslate}
::: highlight
    TOKENIZER_MODEL="meta-llama/Llama-3.1-8B"
:::
::::
:::::

::::: {.model-doc .pyt-megatron-lm-train-llama-3-1-70b .docutils .container}
The training script uses the [`HuggingFaceTokenizer`{.docutils .literal .notranslate}]{.pre}. Set [`TOKENIZER_MODEL`{.docutils .literal .notranslate}]{.pre} to the appropriate Hugging Face model path.

:::: {.highlight-shell .notranslate}
::: highlight
    TOKENIZER_MODEL="meta-llama/Llama-3.1-70B"
:::
::::
:::::

::: {.model-doc .pyt-megatron-lm-train-llama-2-7b .pyt-megatron-lm-train-llama-2-70b .docutils .container}
The training script uses either the [`Llama2Tokenizer`{.docutils .literal .notranslate}]{.pre} or [`HuggingFaceTokenizer`{.docutils .literal .notranslate}]{.pre} by default.
:::

::::: {.model-doc .pyt-megatron-lm-train-deepseek-v3-proxy .docutils .container}
The training script uses the [`HuggingFaceTokenizer`{.docutils .literal .notranslate}]{.pre}. Set [`TOKENIZER_MODEL`{.docutils .literal .notranslate}]{.pre} to the appropriate Hugging Face model path.

:::: {.highlight-shell .notranslate}
::: highlight
    TOKENIZER_MODEL="deepseek-ai/DeepSeek-V3"
:::
::::
:::::

::::: {.model-doc .pyt-megatron-lm-train-deepseek-v2-lite-16b .docutils .container}
The training script uses the [`HuggingFaceTokenizer`{.docutils .literal .notranslate}]{.pre}. Set [`TOKENIZER_MODEL`{.docutils .literal .notranslate}]{.pre} to the appropriate Hugging Face model path.

:::: {.highlight-shell .notranslate}
::: highlight
    TOKENIZER_MODEL="deepseek-ai/DeepSeek-V2-Lite"
:::
::::
:::::

::::::: {.model-doc .pyt-megatron-lm-train-mixtral-8x7b .pyt-megatron-lm-train-mixtral-8x22b-proxy .docutils .container}
Download the Mixtral tokenizer.

:::: {.highlight-shell .notranslate}
::: highlight
    mkdir tokenizer
    cd tokenizer
    export HF_TOKEN=<Your personal Hugging Face access token>
    wget --header="Authorization: Bearer $HF_TOKEN" -O ./tokenizer.model https://huggingface.co/mistralai/Mixtral-8x7B-v0.1/resolve/main/tokenizer.model
:::
::::

Use the [`HuggingFaceTokenizer`{.docutils .literal .notranslate}]{.pre}. Set [`TOKENIZER_MODEL`{.docutils .literal .notranslate}]{.pre} to the appropriate Hugging Face model path.

:::: {.highlight-shell .notranslate}
::: highlight
    TOKENIZER_MODEL=tokenizer/tokenizer.model
:::
::::
:::::::

::::: {.model-doc .pyt-megatron-lm-train-qwen2-5-7b .docutils .container}
The training script uses the [`HuggingFaceTokenizer`{.docutils .literal .notranslate}]{.pre}. Set [`TOKENIZER_MODEL`{.docutils .literal .notranslate}]{.pre} to the appropriate Hugging Face model path.

:::: {.highlight-shell .notranslate}
::: highlight
    TOKENIZER_MODEL="Qwen/Qwen2.5-7B"
:::
::::
:::::

::::: {.model-doc .pyt-megatron-lm-train-qwen2-5-72b .docutils .container}
The training script uses the [`HuggingFaceTokenizer`{.docutils .literal .notranslate}]{.pre}. Set [`TOKENIZER_MODEL`{.docutils .literal .notranslate}]{.pre} to the appropriate Hugging Face model path.

:::: {.highlight-shell .notranslate}
::: highlight
    TOKENIZER_MODEL="Qwen/Qwen2.5-72B"
:::
::::
:::::
::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::: {#dataset-options .section}
### Dataset options[\#](#dataset-options "Link to this heading"){.headerlink}

You can use either mock data or real data for training.

- Mock data can be useful for testing and validation. Use the [`MOCK_DATA`{.docutils .literal .notranslate}]{.pre} variable to toggle between mock and real data. The default value is [`1`{.docutils .literal .notranslate}]{.pre} for enabled.

  :::: {.highlight-bash .notranslate}
  ::: highlight
      MOCK_DATA=1
  :::
  ::::

- If you're using a real dataset, update the [`DATA_PATH`{.docutils .literal .notranslate}]{.pre} variable to point to the location of your dataset.

  :::: {.highlight-bash .notranslate}
  ::: highlight
      MOCK_DATA=0

      DATA_PATH="/data/bookcorpus_text_sentence"  # Change to where your dataset is stored
  :::
  ::::

  Ensure that the files are accessible inside the Docker container.

::::::::::::::::::::::::::::: {#download-the-dataset .section}
#### Download the dataset[\#](#download-the-dataset "Link to this heading"){.headerlink}

:::::::: {.model-doc .pyt-megatron-lm-train-llama-3-3-70b .pyt-megatron-lm-train-llama-3-1-8b .pyt-megatron-lm-train-llama-3-1-70b .pyt-megatron-lm-train-llama-2-7b .pyt-megatron-lm-train-llama-2-70b .pyt-megatron-lm-train-llama-3-1-70b-proxy .docutils .container}
For Llama models, use the [prepare_dataset.sh](https://github.com/ROCm/Megatron-LM/tree/rocm_dev/examples/llama){.reference .external} script to prepare your dataset. To download the dataset, set the [`DATASET`{.docutils .literal .notranslate}]{.pre} variable to the dataset you'd like to use. Three datasets are supported: [`DATASET=wiki`{.docutils .literal .notranslate}]{.pre}, [`DATASET=fineweb`{.docutils .literal .notranslate}]{.pre}, and [`DATASET=bookcorpus`{.docutils .literal .notranslate}]{.pre}.

:::: {.highlight-shell .notranslate}
::: highlight
    DATASET=wiki TOKENIZER_MODEL=NousResearch/Llama-2-7b-chat-hf bash examples/llama/prepare_dataset.sh #for wiki-en dataset
    DATASET=bookcorpus TOKENIZER_MODEL=NousResearch/Llama-2-7b-chat-hf bash examples/llama/prepare_dataset.sh #for bookcorpus dataset
:::
::::

[`TOKENIZER_MODEL`{.docutils .literal .notranslate}]{.pre} can be any accessible Hugging Face tokenizer. Remember to either pre-download the tokenizer or setup Hugging Face access otherwise when needed -- see the [[Tokenizer]{.std .std-ref}](#amd-megatron-lm-tokenizer-v25-11){.reference .internal} section.

::::: {.admonition .note}
Note

When training set [`DATA_PATH`{.docutils .literal .notranslate}]{.pre} to the specific file name prefix pointing to the [`.bin`{.docutils .literal .notranslate}]{.pre} or [`.idx`{.docutils .literal .notranslate}]{.pre} as in the following example:

:::: {.highlight-shell .notranslate}
::: highlight
    DATA_PATH="data/bookcorpus_text_sentence" # Change to where your dataset is stored.
:::
::::
:::::
::::::::

::::::: {.model-doc .pyt-megatron-lm-train-deepseek-v3-proxy .docutils .container}
If you don't already have the dataset, download the DeepSeek dataset using the following commands:

:::: {.highlight-shell .notranslate}
::: highlight
    mkdir deepseek-datasets
    cd deepseek-datasets
    wget https://atp-modelzoo-wlcb-pai.oss-cn-wulanchabu.aliyuncs.com/release/models/pai-megatron-patch/deepseek-datasets/SlimPajama.json
    wget https://atp-modelzoo-wlcb-pai.oss-cn-wulanchabu.aliyuncs.com/release/models/pai-megatron-patch/deepseek-datasets/alpaca_zh-train.json
    wget https://atp-modelzoo-wlcb-pai.oss-cn-wulanchabu.aliyuncs.com/release/models/pai-megatron-patch/deepseek-datasets/alpaca_zh-valid.json
    cd ..
    bash tools/run_make_pretraining_dataset_megatron.sh deepseek-datasets/SlimPajama.json DeepSeekV3Tokenizer text deepseek-datasets deepseek-ai/DeepSeek-V3
:::
::::

To train on this data, update the [`DATA_DIR`{.docutils .literal .notranslate}]{.pre} variable to point to the location of your dataset.

:::: {.highlight-bash .notranslate}
::: highlight
    MOCK_DATA=0 # Train on real data

    DATA_DIR="<path-to>/deepseek-datasets"  # Change to where your dataset is stored

    Ensure that the files are accessible inside the Docker container.
:::
::::
:::::::

::::::: {.model-doc .pyt-megatron-lm-train-deepseek-v2-lite-16b .docutils .container}
If you don't already have the dataset, download the DeepSeek dataset using the following commands:

:::: {.highlight-shell .notranslate}
::: highlight
    mkdir deepseek-datasets
    cd deepseek-datasets
    wget https://atp-modelzoo-wlcb-pai.oss-cn-wulanchabu.aliyuncs.com/release/models/pai-megatron-patch/deepseek-datasets/SlimPajama.json
    wget https://atp-modelzoo-wlcb-pai.oss-cn-wulanchabu.aliyuncs.com/release/models/pai-megatron-patch/deepseek-datasets/alpaca_zh-train.json
    wget https://atp-modelzoo-wlcb-pai.oss-cn-wulanchabu.aliyuncs.com/release/models/pai-megatron-patch/deepseek-datasets/alpaca_zh-valid.json
    cd ..
    bash tools/run_make_pretraining_dataset_megatron.sh deepseek-datasets/SlimPajama.json DeepSeekV3Tokenizer text deepseek-datasets deepseek-ai/DeepSeek-V3
:::
::::

To train on this data, update the [`DATA_DIR`{.docutils .literal .notranslate}]{.pre} variable to point to the location of your dataset.

:::: {.highlight-bash .notranslate}
::: highlight
    MOCK_DATA=0 # Train on real data

    DATA_DIR="<path-to>/deepseek-datasets"  # Change to where your dataset is stored
:::
::::
:::::::

::::::: {.model-doc .pyt-megatron-lm-train-mixtral-8x7b .pyt-megatron-lm-train-mixtral-8x22b-proxy .docutils .container}
If you don't already have the dataset, download the Mixtral dataset using the following commands:

:::: {.highlight-shell .notranslate}
::: highlight
    mkdir mixtral-datasets
    cd mixtral-datasets
    wget https://atp-modelzoo-wlcb-pai.oss-cn-wulanchabu.aliyuncs.com/release/models/pai-megatron-patch/mistral-datasets/wudao_mistralbpe_content_document.bin
    wget https://atp-modelzoo-wlcb-pai.oss-cn-wulanchabu.aliyuncs.com/release/models/pai-megatron-patch/mistral-datasets/wudao_mistralbpe_content_document.idx
:::
::::

To train on this data, update the [`DATA_DIR`{.docutils .literal .notranslate}]{.pre} variable to point to the location of your dataset.

:::: {.highlight-bash .notranslate}
::: highlight
    MOCK_DATA=0 # Train on real data

    DATA_DIR="<path-to>/mixtral-datasets"  # Change to where your dataset is stored
:::
::::

Ensure that the files are accessible inside the Docker container.
:::::::

::::::: {.model-doc .pyt-megatron-lm-train-qwen2-5-7b .pyt-megatron-lm-train-qwen2-5-72b .docutils .container}
If you don't already have the dataset, download the Mixtral dataset using the following commands:

:::: {.highlight-shell .notranslate}
::: highlight
    mkdir -p temp/qwen-datasets
    wget https://atp-modelzoo-wlcb-pai.oss-cn-wulanchabu.aliyuncs.com/release/models/pai-megatron-patch/qwen-datasets/wudao_qwenbpe_text_document.bin
    wget https://atp-modelzoo-wlcb-pai.oss-cn-wulanchabu.aliyuncs.com/release/models/pai-megatron-patch/qwen-datasets/wudao_qwenbpe_text_document.idx
:::
::::

To train on this data, update the [`DATA_DIR`{.docutils .literal .notranslate}]{.pre} variable to point to the location of your dataset.

:::: {.highlight-bash .notranslate}
::: highlight
    MOCK_DATA=0 # Train on real data

    DATA_DIR="<path-to>/qwen-datasets"  # Change to where your dataset is stored
:::
::::

Ensure that the files are accessible inside the Docker container.
:::::::
:::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#run-training .section}
[]{#amd-megatron-lm-run-training-v25-11}

## Run training[\#](#run-training "Link to this heading"){.headerlink}

Use the following example commands to set up the environment, configure [[key options]{.std .std-ref}](#amd-megatron-lm-benchmark-test-vars-v25-11){.reference .internal}, and run training on MI300X Series GPUs with the AMD Megatron-LM environment.

Before starting training, export the following environment variables.

::::::::: {.sd-tab-set .docutils}
MI355X and MI350X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    export HSA_NO_SCRATCH_RECLAIM=1
    export NVTE_CK_USES_BWD_V3=1
    export NVTE_CK_USES_BWD_V3=1
:::
::::
:::::

MI325X and MI300X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    export HSA_NO_SCRATCH_RECLAIM=1
    export NVTE_CK_USES_BWD_V3=1
    export NVTE_CK_USES_BWD_V3=1

    # Set this on MI325X/MI300X only
    export NVTE_CK_IS_V3_ATOMIC_FP32=1
:::
::::
:::::
:::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#single-node-training .section}
### Single node training[\#](#single-node-training "Link to this heading"){.headerlink}

:::::: {.model-doc .pyt-megatron-lm-train-llama-3-3-70b .docutils .container}
To run the training on a single node for Llama 3.3 70B BF16 with FSDP-v2 enabled, add the [`FSDP=1`{.docutils .literal .notranslate}]{.pre} argument. For example, use the following command:

:::: {.highlight-shell .notranslate}
::: highlight
    TOKENIZER_MODEL=meta-llama/Llama-3.3-70B-Instruct \
    CKPT_FORMAT=torch_dist \
    TEE_OUTPUT=1 \
    RECOMPUTE=1 \
    SEQ_LENGTH=8192 \
    MBS=2 \
    BS=16 \
    TE_FP8=0 \
    TP=1 \
    PP=1 \
    FSDP=1 \
    MODEL_SIZE=70 \
    TOTAL_ITERS=50 \
    bash examples/llama/train_llama3.sh
:::
::::

::: {.admonition .note}
Note

It is suggested to use [`TP=1`{.docutils .literal .notranslate}]{.pre} when FSDP is enabled for higher throughput. FSDP-v2 is not supported with pipeline parallelism, expert parallelism, MCore's distributed optimizer, gradient accumulation fusion, or FP16.
:::
::::::

::::::::::::::::: {.model-doc .pyt-megatron-lm-train-llama-3-1-8b .docutils .container}
To run training on a single node for Llama 3.1 8B FP8, navigate to the Megatron-LM folder and use the following command.

::::::::: {.sd-tab-set .docutils}
MI355X and MI350X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    TEE_OUTPUT=1 \
    MBS=4 \
    BS=512 \
    TP=1 \
    TE_FP8=1 \
    SEQ_LENGTH=8192 \
    MODEL_SIZE=8 \
    TOTAL_ITERS=10 \
    GEMM_TUNING=0 \
    bash examples/llama/train_llama3.sh
:::
::::
:::::

MI300X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    TEE_OUTPUT=1 \
    MBS=2 \
    BS=128 \
    TP=1 \
    TE_FP8=1 \
    SEQ_LENGTH=8192 \
    MODEL_SIZE=8 \
    TOTAL_ITERS=50 \
    bash examples/llama/train_llama3.sh
:::
::::
:::::
:::::::::

For Llama 3.1 8B BF16, use the following command:

::::::::: {.sd-tab-set .docutils}
MI355X and MI350X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    TEE_OUTPUT=1 \
    MBS=4 \
    BS=512 \
    TP=1 \
    TE_FP8=0 \
    SEQ_LENGTH=8192 \
    MODEL_SIZE=8 \
    TOTAL_ITERS=10 \
    GEMM_TUNING=1 \
    bash examples/llama/train_llama3.sh
:::
::::
:::::

MI300X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    TEE_OUTPUT=1 \
    MBS=2 \
    BS=128 \
    TP=1 \
    TE_FP8=0 \
    SEQ_LENGTH=8192 \
    MODEL_SIZE=8 \
    TOTAL_ITERS=50 \
    bash examples/llama/train_llama3.sh
:::
::::
:::::
:::::::::
:::::::::::::::::

:::::::::::::::: {.model-doc .pyt-megatron-lm-train-llama-3-1-70b .docutils .container}
To run the training on a single node for Llama 3.1 70B BF16 with FSDP-v2 enabled, add the [`FSDP=1`{.docutils .literal .notranslate}]{.pre} argument. For example, use the following command:

:::: {.highlight-shell .notranslate}
::: highlight
    CKPT_FORMAT=torch_dist \
    TEE_OUTPUT=1 \
    MBS=3 \
    BS=24 \
    TP=1 \
    TE_FP8=0 \
    FSDP=1 \
    RECOMPUTE=1 \
    SEQ_LENGTH=8192 \
    MODEL_SIZE=70 \
    TOTAL_ITERS=50 \
    bash examples/llama/train_llama3.sh
:::
::::

::: {.admonition .note}
Note

It is suggested to use [`TP=1`{.docutils .literal .notranslate}]{.pre} when FSDP is enabled for higher throughput. FSDP-v2 is not supported with pipeline parallelism, expert parallelism, MCore's distributed optimizer, gradient accumulation fusion, or FP16.
:::

To run the training on a single node for Llama 3.1 70B FP8, use the following command.

::: {.admonition .note}
Note

The MI300X configuration uses a proxy model. On MI300X GPUs, use two or more nodes to run the full Llama 3.1 70B model with FP8 precision. MI355X and MI350X GPUs can support the full 70B model with FP8 precision on a single node.
:::

::::::::: {.sd-tab-set .docutils}
MI355X and MI350X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    CKPT_FORMAT=torch_dist \
    TEE_OUTPUT=1 \
    RECOMPUTE=1 \
    MBS=3 \
    BS=24 \
    TP=1 \
    TE_FP8=1 \
    SEQ_LENGTH=8192 \
    MODEL_SIZE=70 \
    FSDP=1 \
    TOTAL_ITERS=10 \
    bash examples/llama/train_llama3.sh
:::
::::
:::::

MI300X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    FP8_WEIGHT_TRANSPOSE_CACHE=0 \
    CKPT_FORMAT=torch_dist \
    TEE_OUTPUT=1 \
    RECOMPUTE=1 \
    MBS=3 \
    BS=24 \
    TP=1 \
    TE_FP8=1 \
    SEQ_LENGTH=8192 \
    MODEL_SIZE=70 \
    FSDP=1 \
    TOTAL_ITERS=10 \
    NUM_LAYERS=40 \
    bash examples/llama/train_llama3.sh
:::
::::
:::::
:::::::::

::: {.admonition .note}
Note

The MI300X configuration uses a proxy model. On MI300X GPUs, use two or more nodes to run the full Llama 3.1 70B model with FP8 precision. MI355X and MI350X GPUs can support the full 70B model with FP8 precision on a single node.
:::

::: {.admonition .note}
Note

It is suggested to use [`TP=1`{.docutils .literal .notranslate}]{.pre} when FSDP is enabled for higher throughput. FSDP-v2 is not supported with pipeline parallelism, expert parallelism, MCore's distributed optimizer, gradient accumulation fusion, or FP16.
:::
::::::::::::::::

::::::: {.model-doc .pyt-megatron-lm-train-llama-2-7b .docutils .container}
To run training on a single node for Llama 2 7B FP8, navigate to the Megatron-LM folder and use the following command.

:::: {.highlight-shell .notranslate}
::: highlight
    TEE_OUTPUT=1 \
    MBS=4 \
    BS=256 \
    TP=1 \
    TE_FP8=1 \
    SEQ_LENGTH=4096 \
    MODEL_SIZE=7 \
    TOTAL_ITERS=50 \
    bash examples/llama/train_llama2.sh
:::
::::

For Llama 2 7B BF16, use the following command:

:::: {.highlight-shell .notranslate}
::: highlight
    TEE_OUTPUT=1 \
    MBS=4 \
    BS=256 \
    TP=1 \
    TE_FP8=0 \
    SEQ_LENGTH=4096 \
    MODEL_SIZE=7 \
    TOTAL_ITERS=50 \
    bash examples/llama/train_llama2.sh
:::
::::
:::::::

:::::: {.model-doc .pyt-megatron-lm-train-llama-2-70b .docutils .container}
To run the training on a single node for Llama 2 70B BF16 with FSDP-v2 enabled, add the [`FSDP=1`{.docutils .literal .notranslate}]{.pre} argument. For example, use the following command:

:::: {.highlight-shell .notranslate}
::: highlight
    CKPT_FORMAT=torch_dist \
    TEE_OUTPUT=1 \
    MBS=7 \
    BS=56 \
    TP=1 \
    TE_FP8=0 \
    FSDP=1 \
    RECOMPUTE=1 \
    SEQ_LENGTH=4096 \
    MODEL_SIZE=70 \
    TOTAL_ITERS=50 \
    bash examples/llama/train_llama2.sh
:::
::::

::: {.admonition .note}
Note

It is suggested to use [`TP=1`{.docutils .literal .notranslate}]{.pre} when FSDP is enabled for higher throughput. FSDP-v2 is not supported with pipeline parallelism, expert parallelism, MCore's distributed optimizer, gradient accumulation fusion, or FP16.
:::
::::::

::::: {.model-doc .pyt-megatron-lm-train-deepseek-v3-proxy .docutils .container}
To run training on a single node for DeepSeek-V3 (MoE with expert parallel) with 3-layer proxy, navigate to the Megatron-LM folder and use the following command.

:::: {.highlight-shell .notranslate}
::: highlight
    export NVTE_FUSED_ATTN_CK=0
    FORCE_BALANCE=true \
    RUN_ENV=cluster \
    MODEL_SIZE=671B \
    TRAIN_ITERS=50 \
    SEQ_LEN=4096 \
    NUM_LAYERS=3 \
    MICRO_BATCH_SIZE=1 GLOBAL_BATCH_SIZE=32 \
    PR=bf16 \
    TP=1 PP=1 ETP=1 EP=8 \
    GEMM_TUNING=1 \
    NVTE_CK_USES_BWD_V3=1 \
    USE_GROUPED_GEMM=true MOE_USE_LEGACY_GROUPED_GEMM=true \
    GPT_LAYER_IN_TE=true \
    bash examples/deepseek_v3/train_deepseekv3.sh
:::
::::
:::::

:::::: {.model-doc .pyt-megatron-lm-train-deepseek-v2-lite-16b .docutils .container}
To run training on a single node for DeepSeek-V2-Lite (MoE with expert parallel), navigate to the Megatron-LM folder and use the following command.

:::: {.highlight-shell .notranslate}
::: highlight
    export NVTE_FUSED_ATTN_CK=0
    GEMM_TUNING=1 \
    PR=bf16 \
    MBS=4 \
    AC=none \
    SEQ_LEN=4096 \
    PAD_LEN=4096 \
    TRAIN_ITERS=20 \
    bash examples/deepseek_v2/train_deepseekv2.sh
:::
::::

::: {.admonition .note}
Note

Note that DeepSeek-V2-Lite is experiencing instability due to GPU memory access fault for large iterations. For stability, it's recommended to use Primus for this workload. See [[Training a model with Primus and Megatron-LM]{.doc}](../primus-megatron.html){.reference .internal}.
:::
::::::

::::: {.model-doc .pyt-megatron-lm-train-mixtral-8x7b .docutils .container}
To run training on a single node for Mixtral 8x7B (MoE with expert parallel), navigate to the Megatron-LM folder and use the following command.

:::: {.highlight-shell .notranslate}
::: highlight
    TOKENIZER_MODEL=<path/to/tokenizer/model>
    RECOMPUTE_NUM_LAYERS=0 \
    TEE_OUTPUT=1 \
    MBS=1 \
    GBS=16 \
    TP_SIZE=1 \
    PP_SIZE=1 \
    AC=none \
    PR=bf16 \
    EP_SIZE=8 \
    ETP_SIZE=1 \
    SEQLEN=4096 \
    FORCE_BALANCE=true \
    MOCK_DATA=1 \
    RUN_ENV=cluster \
    MODEL_SIZE=8x7B \
    TRAIN_ITERS=50 \
    bash examples/mixtral/train_mixtral_moe.sh
:::
::::
:::::

::::: {.model-doc .pyt-megatron-lm-train-mixtral-8x22b-proxy .docutils .container}
To run training on a single node for Mixtral 8x7B (MoE with expert parallel) with 4-layer proxy, navigate to the Megatron-LM folder and use the following command.

:::: {.highlight-shell .notranslate}
::: highlight
    TOKENIZER_MODEL=<path/to/tokenizer/model>
    RECOMPUTE_NUM_LAYERS=4 \
    TEE_OUTPUT=1 \
    MBS=1 \
    GBS=16 \
    TP_SIZE=1 \
    PP_SIZE=1 \
    AC=full \
    NUM_LAYERS=4 \
    PR=bf16 \
    EP_SIZE=8 \
    ETP_SIZE=1 \
    SEQLEN=8192 \
    FORCE_BALANCE=true \
    MOCK_DATA=1 \
    RUN_ENV=cluster \
    MODEL_SIZE=8x22B \
    TRAIN_ITERS=50 \
    bash examples/mixtral/train_mixtral_moe.sh
:::
::::
:::::

::::::: {.model-doc .pyt-megatron-lm-train-qwen2-5-7b .docutils .container}
To run training on a single node for Qwen 2.5 7B BF16, use the following command.

:::: {.highlight-shell .notranslate}
::: highlight
    bash examples/qwen/train_qwen2.sh TP=1 \
        CP=1 \
        PP=1 \
        MBS=10 \
        BS=640 \
        TE_FP8=0 \
        MODEL_SIZE=7 \
        SEQ_LENGTH=2048 \
        TOTAL_ITERS=50 \
        MOCK_DATA=1 \
        TOKENIZER_MODEL=Qwen/Qwen2.5-7B
:::
::::

For FP8, use the following command.

:::: {.highlight-shell .notranslate}
::: highlight
    bash examples/qwen/train_qwen2.sh \
        TP=1 \
        CP=1 \
        PP=1 \
        MBS=10 \
        BS=640 \
        TE_FP8=1 \
        MODEL_SIZE=7 \
        SEQ_LENGTH=2048 \
        TOTAL_ITERS=50 \
        MOCK_DATA=1 \
        TOKENIZER_MODEL=Qwen/Qwen2.5-7B
:::
::::
:::::::

::::: {.model-doc .pyt-megatron-lm-train-qwen2-5-72b .docutils .container}
To run the training on a single node for Qwen 2.5 72B BF16, use the following command.

:::: {.highlight-shell .notranslate}
::: highlight
    bash examples/qwen/train_qwen2.sh \
        FSDP=1 \
        CP=1 \
        PP=1 \
        MBS=3 \
        BS=24 \
        TE_FP8=0 \
        MODEL_SIZE=72 \
        SEQ_LENGTH=2048 \
        TOTAL_ITERS=50 \
        MOCK_DATA=1 \
        TOKENIZER_MODEL=Qwen/Qwen2.5-72B \
        RECOMPUTE_ACTIVATIONS=full \
        CKPT_FORMAT=torch_dist
:::
::::
:::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::: {#multi-node-training-examples .section}
[]{#amd-megatron-lm-multi-node-examples-v25-11}

### Multi-node training examples[\#](#multi-node-training-examples "Link to this heading"){.headerlink}

To run training on multiple nodes, launch the Docker container on each node. For example, for Llama 3 using a two node setup ([`NODE0`{.docutils .literal .notranslate}]{.pre} as the master node), use these commands.

- On the master node [`NODE0`{.docutils .literal .notranslate}]{.pre}:

  :::: {.highlight-shell .notranslate}
  ::: highlight
      TEE_OUTPUT=1 \
      MBS=2 \
      BS=256 \
      TP=1 \
      TE_FP8=1 \
      SEQ_LENGTH=8192 \
      MODEL_SIZE=8  \
      MASTER_ADDR=IP_NODE0 \
      NNODES=2 \
      NODE_RANK=0 \
      bash examples/llama/train_llama3.sh
  :::
  ::::

- On the worker node [`NODE1`{.docutils .literal .notranslate}]{.pre}:

  :::: {.highlight-shell .notranslate}
  ::: highlight
      TEE_OUTPUT=1 \
      MBS=2 \
      BS=256 \
      TP=1 \
      TE_FP8=1 \
      SEQ_LENGTH=8192 \
      MODEL_SIZE=8  \
      MASTER_ADDR=IP_NODE0 \
      NNODES=2 \
      NODE_RANK=1 \
      bash examples/llama/train_llama3.sh
  :::
  ::::

Or, for DeepSeek-V3, an example script [`train_deepseek_v3_slurm.sh`{.docutils .literal .notranslate}]{.pre} is provided in [ROCm/Megatron-LM](https://github.com/ROCm/Megatron-LM/tree/rocm_dev/examples/deepseek_v3){.github .reference .external} to enable training at scale under a SLURM environment. For example, to run training on 16 nodes, try the following command:

:::: {.highlight-shell .notranslate}
::: highlight
    sbatch examples/deepseek_v3/train_deepseek_v3_slurm.sh
:::
::::
:::::

::: {#key-options .section}
[]{#amd-megatron-lm-benchmark-test-vars-v25-11}

### Key options[\#](#key-options "Link to this heading"){.headerlink}

The benchmark tests support the following sets of variables.

[`TEE_OUTPUT`{.docutils .literal .notranslate}]{.pre}

:   [`1`{.docutils .literal .notranslate}]{.pre} to enable training logs or [`0`{.docutils .literal .notranslate}]{.pre} to disable.

[`TE_FP8`{.docutils .literal .notranslate}]{.pre}

:   [`0`{.docutils .literal .notranslate}]{.pre} for B16 or [`1`{.docutils .literal .notranslate}]{.pre} for FP8 -- [`0`{.docutils .literal .notranslate}]{.pre} by default.

[`GEMM_TUNING`{.docutils .literal .notranslate}]{.pre}

:   [`1`{.docutils .literal .notranslate}]{.pre} to enable GEMM tuning, which boosts performance by using the best GEMM kernels.

[`USE_FLASH_ATTN`{.docutils .literal .notranslate}]{.pre}

:   [`1`{.docutils .literal .notranslate}]{.pre} to enable Flash Attention.

[`FSDP`{.docutils .literal .notranslate}]{.pre}

:   [`1`{.docutils .literal .notranslate}]{.pre} to enable PyTorch FSDP2. If FSDP is enabled, [`--use-distributed-optimizer`{.docutils .literal .notranslate}]{.pre}, [`--overlap-param-gather`{.docutils .literal .notranslate}]{.pre}, and [`--sequence-parallel`{.docutils .literal .notranslate}]{.pre} are automatically disabled.

[`ENABLE_PROFILING`{.docutils .literal .notranslate}]{.pre}

:   [`1`{.docutils .literal .notranslate}]{.pre} to enable PyTorch profiling for performance analysis.

[`transformer-impl`{.docutils .literal .notranslate}]{.pre}

:   [`transformer_engine`{.docutils .literal .notranslate}]{.pre} to use the Transformer Engine (TE) or [`local`{.docutils .literal .notranslate}]{.pre} to disable TE.

[`MODEL_SIZE`{.docutils .literal .notranslate}]{.pre}

:   [`8B`{.docutils .literal .notranslate}]{.pre} or [`70B`{.docutils .literal .notranslate}]{.pre} for Llama 3 and 3.1. [`7B`{.docutils .literal .notranslate}]{.pre} or [`70B`{.docutils .literal .notranslate}]{.pre} for Llama 2, for example.

[`TOTAL_ITERS`{.docutils .literal .notranslate}]{.pre}

:   The total number of iterations -- [`10`{.docutils .literal .notranslate}]{.pre} by default.

[`MOCK_DATA`{.docutils .literal .notranslate}]{.pre}

:   [`1`{.docutils .literal .notranslate}]{.pre} to use mock data or [`0`{.docutils .literal .notranslate}]{.pre} to use real data you provide.

[`MBS`{.docutils .literal .notranslate}]{.pre}

:   Micro batch size.

[`BS`{.docutils .literal .notranslate}]{.pre}

:   Global batch size.

[`TP`{.docutils .literal .notranslate}]{.pre} / [`TP_SIZE`{.docutils .literal .notranslate}]{.pre}

:   Tensor parallel ([`1`{.docutils .literal .notranslate}]{.pre}, [`2`{.docutils .literal .notranslate}]{.pre}, [`4`{.docutils .literal .notranslate}]{.pre}, [`8`{.docutils .literal .notranslate}]{.pre}). [`TP`{.docutils .literal .notranslate}]{.pre} is disabled when [`FSDP`{.docutils .literal .notranslate}]{.pre} is turned on.

[`EP`{.docutils .literal .notranslate}]{.pre} / [`EP_SIZE`{.docutils .literal .notranslate}]{.pre}

:   Expert parallel for MoE models.

[`SEQ_LENGTH`{.docutils .literal .notranslate}]{.pre}

:   Input sequence length.

[`PR`{.docutils .literal .notranslate}]{.pre}

:   Precision for training. [`bf16`{.docutils .literal .notranslate}]{.pre} for BF16 (default) or [`fp8`{.docutils .literal .notranslate}]{.pre} for FP8 GEMMs.

[`AC`{.docutils .literal .notranslate}]{.pre}

:   Activation checkpointing ([`none`{.docutils .literal .notranslate}]{.pre}, [`sel`{.docutils .literal .notranslate}]{.pre}, or [`full`{.docutils .literal .notranslate}]{.pre}) -- [`sel`{.docutils .literal .notranslate}]{.pre} by default.

[`NUM_LAYERS`{.docutils .literal .notranslate}]{.pre}

:   Use reduced number of layers as a proxy model.

[`RECOMPUTE_NUM_LAYERS`{.docutils .literal .notranslate}]{.pre}

:   Number of layers used for checkpointing recompute.
:::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: {#previous-versions .section}
## Previous versions[\#](#previous-versions "Link to this heading"){.headerlink}

See [[Megatron-LM training performance testing version history]{.doc}](megatron-lm-history.html){.reference .internal} to find documentation for previous releases of the [`ROCm/megatron-lm`{.docutils .literal .notranslate}]{.pre} Docker image.
:::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: prev-next-area
:::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::: {.bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {.page-toc .tocsection .onthispage}
Contents
:::

- [Supported models](#supported-models){.reference .internal .nav-link}
- [Performance measurements](#performance-measurements){.reference .internal .nav-link}
- [System validation](#system-validation){.reference .internal .nav-link}
- [Environment setup](#environment-setup){.reference .internal .nav-link}
  - [Download the Docker image](#download-the-docker-image){.reference .internal .nav-link}
- [Configuration](#configuration){.reference .internal .nav-link}
  - [Multi-node configuration](#multi-node-configuration){.reference .internal .nav-link}
  - [Tokenizer](#tokenizer){.reference .internal .nav-link}
  - [Dataset options](#dataset-options){.reference .internal .nav-link}
    - [Download the dataset](#download-the-dataset){.reference .internal .nav-link}
- [Run training](#run-training){.reference .internal .nav-link}
  - [Single node training](#single-node-training){.reference .internal .nav-link}
  - [Multi-node training examples](#multi-node-training-examples){.reference .internal .nav-link}
  - [Key options](#key-options){.reference .internal .nav-link}
- [Previous versions](#previous-versions){.reference .internal .nav-link}
::::
:::::
::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
