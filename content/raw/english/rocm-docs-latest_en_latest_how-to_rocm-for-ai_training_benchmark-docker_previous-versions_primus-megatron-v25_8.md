---
title: "Training a model with Primus and Megatron-LM"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/training/benchmark-docker/previous-versions/primus-megatron-v25.8.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-01
---

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-content
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-article-container
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
# Training a model with Primus and Megatron-LM

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [Supported models](#supported-models){.reference .internal .nav-link}
- [System validation](#system-validation){.reference .internal .nav-link}
  - [Environment setup](#environment-setup){.reference .internal .nav-link}
    - [Download the Docker image](#download-the-docker-image){.reference .internal .nav-link}
- [Configuration](#configuration){.reference .internal .nav-link}
  - [Dataset options](#dataset-options){.reference .internal .nav-link}
  - [Tokenizer](#tokenizer){.reference .internal .nav-link}
- [Run training](#run-training){.reference .internal .nav-link}
  - [Single node training](#single-node-training){.reference .internal .nav-link}
  - [Multi-node training examples](#multi-node-training-examples){.reference .internal .nav-link}
  - [Key options](#key-options){.reference .internal .nav-link}
- [Further reading](#further-reading){.reference .internal .nav-link}
- [Previous versions](#previous-versions){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#training-a-model-with-primus-and-megatron-lm .section}
# Training a model with Primus and Megatron-LM[\#](#training-a-model-with-primus-and-megatron-lm "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-04-21
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 16 min read time
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

This documentation does not reflect the latest version of ROCm Megatron-LM training performance documentation. See [[Training a model with Primus and Megatron-LM]{.doc}](../primus-megatron.html){.reference .internal} for the latest version.
:::

[Primus](https://github.com/AMD-AGI/Primus){.reference .external} is a unified and flexible LLM training framework designed to streamline training. It streamlines LLM training on AMD Instinct GPUs using a modular, reproducible configuration paradigm. Primus is backend-agnostic and supports multiple training engines -- including Megatron.

::: {.admonition .note}
Note

Primus with Megatron is designed to replace the [[ROCm Megatron-LM training]{.doc}](../megatron-lm.html){.reference .internal} workflow. To learn how to migrate workloads from Megatron-LM to Primus with Megatron, see [[Migrating workloads to Primus (Megatron backend) from Megatron-LM]{.doc}](megatron-lm-primus-migration-guide.html){.reference .internal}.
:::

For ease of use, AMD provides a ready-to-use Docker image for MI300 series GPUs containing essential components for Primus and Megatron-LM. This Docker is powered by Primus Turbo optimizations for performance; this release adds support for Primus Turbo with optimized attention and grouped GEMM kernels.

::: {.admonition .note}
Note

This Docker environment is based on Python 3.10 and Ubuntu 22.04. For an alternative environment with Python 3.12 and Ubuntu 24.04, see the [[previous ROCm Megatron-LM v25.6 Docker release]{.doc}](megatron-lm-v25.6.html){.reference .internal}.
:::

::: pst-scrollable-table-container
  Software component   Version
  -------------------- ---------------------
  ROCm                 6.4.3
  Primus               927a717
  PyTorch              2.8.0a0+gitd06a406
  Python               3.10
  Transformer Engine   2.2.0.dev0+54dd2bdc
  hipBLASLt            d1b517fc7a
  Triton               3.3.0
  RCCL                 2.22.3
:::

:::::::::::::::::::::::::: {#supported-models .section}
[]{#amd-primus-megatron-lm-model-support}

## Supported models[\#](#supported-models "Link to this heading"){.headerlink}

The following models are pre-optimized for performance on AMD Instinct MI300X series GPUs. Some instructions, commands, and training examples in this documentation might vary by model -- select one to get started.

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
::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="primus_pyt_megatron_lm_train_llama-3.3-70b" tabindex="0"}
Llama 3.3 70B
:::

::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="primus_pyt_megatron_lm_train_llama-3.1-70b" tabindex="0"}
Llama 3.1 70B
:::

::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="primus_pyt_megatron_lm_train_llama-3.1-8b" tabindex="0"}
Llama 3.1 8B
:::

::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="primus_pyt_megatron_lm_train_llama-2-7b" tabindex="0"}
Llama 2 7B
:::

::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="primus_pyt_megatron_lm_train_llama-2-70b" tabindex="0"}
Llama 2 70B
:::

::: {.col-6 .px-2 .model-param param-group="deepseek" param-k="model" param-v="primus_pyt_megatron_lm_train_deepseek-v3-proxy" tabindex="0"}
DeepSeek-V3 (proxy)
:::

::: {.col-6 .px-2 .model-param param-group="deepseek" param-k="model" param-v="primus_pyt_megatron_lm_train_deepseek-v2-lite-16b" tabindex="0"}
DeepSeek-V2-Lite
:::

::: {.col-6 .px-2 .model-param param-group="mistral" param-k="model" param-v="primus_pyt_megatron_lm_train_mixtral-8x7b" tabindex="0"}
Mixtral 8x7B
:::

::: {.col-6 .px-2 .model-param param-group="mistral" param-k="model" param-v="primus_pyt_megatron_lm_train_mixtral-8x22b-proxy" tabindex="0"}
Mixtral 8x22B (proxy)
:::

::: {.col-6 .px-2 .model-param param-group="qwen" param-k="model" param-v="primus_pyt_megatron_lm_train_qwen2.5-7b" tabindex="0"}
Qwen 2.5 7B
:::

::: {.col-6 .px-2 .model-param param-group="qwen" param-k="model" param-v="primus_pyt_megatron_lm_train_qwen2.5-72b" tabindex="0"}
Qwen 2.5 72B
:::
::::::::::::::
::::::::::::::::
::::::::::::::::::::::::

::: {.admonition .note}
Note

Some models, such as Llama, require an external license agreement through a third party (for example, Meta).
:::
::::::::::::::::::::::::::

::::: {#system-validation .section}
## System validation[\#](#system-validation "Link to this heading"){.headerlink}

Before running AI workloads, it's important to validate that your AMD hardware is configured correctly and performing optimally.

If you have already validated your system settings, including aspects like NUMA auto-balancing, you can skip this step. Otherwise, complete the procedures in the [[System validation and optimization]{.std .std-ref}](../../../system-setup/prerequisite-system-validation.html#rocm-for-ai-system-optimization){.reference .internal} guide to properly configure your system settings before starting training.

To test for optimal performance, consult the recommended [[System health benchmarks]{.std .std-ref}](../../../system-setup/system-health-check.html#rocm-for-ai-system-health-bench){.reference .internal}. This suite of tests will help you verify and fine-tune your system's configuration.

:::: {#environment-setup .section}
[]{#mi300x-amd-primus-megatron-lm-training}

### Environment setup[\#](#environment-setup "Link to this heading"){.headerlink}

Use the following instructions to set up the environment, configure the script to train models, and reproduce the benchmark results on MI300X series GPUs with the [`rocm/megatron-lm:v25.8_py310`{.docutils .literal .notranslate}]{.pre} image.

::: {#download-the-docker-image .section}
[]{#amd-primus-megatron-lm-requirements}

#### Download the Docker image[\#](#download-the-docker-image "Link to this heading"){.headerlink}

1.  Use the following command to pull the Docker image from Docker Hub.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker pull rocm/megatron-lm:v25.8_py310
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
            --shm-size 128G \
            --name primus_training_env \
            rocm/megatron-lm:v25.8_py310
    :::
    ::::
:::
::::

3.  Use these commands if you exit the [`primus_training_env`{.docutils .literal .notranslate}]{.pre} container and need to return to it.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker start primus_training_env
        docker exec -it primus_training_env bash
    :::
    ::::

The Docker container hosts verified commit [`927a717`{.docutils .literal .notranslate}]{.pre} of the [Primus](https://github.com/AMD-AGI/Primus/tree/927a71702784347a311ca48fd45f0f308c6ef6dd){.reference .external} repository.
:::::

:::::::::::::::::::: {#configuration .section}
[]{#amd-primus-megatron-lm-environment-setup}

## Configuration[\#](#configuration "Link to this heading"){.headerlink}

Primus defines a training configuration in YAML for each model in [examples/megatron/configs](https://github.com/AMD-AGI/Primus/tree/927a71702784347a311ca48fd45f0f308c6ef6dd/examples/megatron/configs){.reference .external}.

::: {.model-doc .primus-pyt-megatron-lm-train-llama-3-3-70b .docutils .container}
To update training parameters for Llama 3.3 70B, you can update [`examples/megatron/configs/llama3.3_70B-pretrain.yaml`{.docutils .literal .notranslate}]{.pre}. Note that training configuration YAML files for other models follow this naming convention.
:::

::: {.model-doc .primus-pyt-megatron-lm-train-llama-3-1-70b .docutils .container}
To update training parameters for Llama 3.1 70B, you can update [`examples/megatron/configs/llama3.1_70B-pretrain.yaml`{.docutils .literal .notranslate}]{.pre}. Note that training configuration YAML files for other models follow this naming convention.
:::

::: {.model-doc .primus-pyt-megatron-lm-train-llama-3-1-8b .docutils .container}
To update training parameters for Llama 3.1 8B, you can update [`examples/megatron/configs/llama3.1_8B-pretrain.yaml`{.docutils .literal .notranslate}]{.pre}. Note that training configuration YAML files for other models follow this naming convention.
:::

::: {.model-doc .primus-pyt-megatron-lm-train-llama-2-7b .docutils .container}
To update training parameters for Llama 2 7B, you can update [`examples/megatron/configs/llama2_7B-pretrain.yaml`{.docutils .literal .notranslate}]{.pre}. Note that training configuration YAML files for other models follow this naming convention.
:::

::: {.model-doc .primus-pyt-megatron-lm-train-llama-2-70b .docutils .container}
To update training parameters for Llama 2 70B, you can update [`examples/megatron/configs/llama2_70B-pretrain.yaml`{.docutils .literal .notranslate}]{.pre}. Note that training configuration YAML files for other models follow this naming convention.
:::

::: {.model-doc .primus-pyt-megatron-lm-train-deepseek-v3-proxy .docutils .container}
To update training parameters for DeepSeek-V3 (proxy), you can update [`examples/megatron/configs/deepseek_v3-pretrain.yaml`{.docutils .literal .notranslate}]{.pre}. Note that training configuration YAML files for other models follow this naming convention.
:::

::: {.model-doc .primus-pyt-megatron-lm-train-deepseek-v2-lite-16b .docutils .container}
To update training parameters for DeepSeek-V2-Lite, you can update [`examples/megatron/configs/deepseek_v2_lite-pretrain.yaml`{.docutils .literal .notranslate}]{.pre}. Note that training configuration YAML files for other models follow this naming convention.
:::

::: {.model-doc .primus-pyt-megatron-lm-train-mixtral-8x7b .docutils .container}
To update training parameters for Mixtral 8x7B, you can update [`examples/megatron/configs/mixtral_8x7B_v0.1-pretrain.yaml`{.docutils .literal .notranslate}]{.pre}. Note that training configuration YAML files for other models follow this naming convention.
:::

::: {.model-doc .primus-pyt-megatron-lm-train-mixtral-8x22b-proxy .docutils .container}
To update training parameters for Mixtral 8x22B (proxy), you can update [`examples/megatron/configs/mixtral_8x22B_v0.1-pretrain.yaml`{.docutils .literal .notranslate}]{.pre}. Note that training configuration YAML files for other models follow this naming convention.
:::

::: {.model-doc .primus-pyt-megatron-lm-train-qwen2-5-7b .docutils .container}
To update training parameters for Qwen 2.5 7B, you can update [`examples/megatron/configs/primus_qwen2.5_7B-pretrain.yaml`{.docutils .literal .notranslate}]{.pre}. Note that training configuration YAML files for other models follow this naming convention.
:::

::: {.model-doc .primus-pyt-megatron-lm-train-qwen2-5-72b .docutils .container}
To update training parameters for Qwen 2.5 72B, you can update [`examples/megatron/configs/qwen2.5_72B-pretrain.yaml`{.docutils .literal .notranslate}]{.pre}. Note that training configuration YAML files for other models follow this naming convention.
:::

::: {.admonition .note}
Note

See [[Key options]{.std .std-ref}](#amd-primus-megatron-lm-benchmark-test-vars){.reference .internal} for more information on configuration options.
:::

::: {#dataset-options .section}
### Dataset options[\#](#dataset-options "Link to this heading"){.headerlink}

You can use either mock data or real data for training.

- Mock data can be useful for testing and validation. Use the [`mock_data`{.docutils .literal .notranslate}]{.pre} field to toggle between mock and real data. The default value is [`true`{.docutils .literal .notranslate}]{.pre} for enabled.

  :::: {.highlight-yaml .notranslate}
  ::: highlight
      mock_data: true
  :::
  ::::

- If you're using a real dataset, update the [`train_data_path`{.docutils .literal .notranslate}]{.pre} field to point to the location of your dataset.

  :::: {.highlight-bash .notranslate}
  ::: highlight
      mock_data: false
      train_data_path: /path/to/your/dataset
  :::
  ::::

  Ensure that the files are accessible inside the Docker container.
:::

:::::: {#tokenizer .section}
[]{#amd-primus-megatron-lm-tokenizer}

### Tokenizer[\#](#tokenizer "Link to this heading"){.headerlink}

Set the [`HF_TOKEN`{.docutils .literal .notranslate}]{.pre} environment variable with right permissions to access the tokenizer for each model.

:::: {.highlight-bash .notranslate}
::: highlight
    # Export your HF_TOKEN in the workspace
    export HF_TOKEN=<your_hftoken>
:::
::::

::: {.admonition .note}
Note

In Primus, each model uses a tokenizer from Hugging Face. For example, Llama 3.1 8B model uses [`tokenizer_model:`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`meta-llama/Llama-3.1-8B`{.docutils .literal .notranslate}]{.pre} and [`tokenizer_type:`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`Llama3Tokenizer`{.docutils .literal .notranslate}]{.pre} defined in the [llama3.1-8B model](https://github.com/AMD-AGI/Primus/blob/927a71702784347a311ca48fd45f0f308c6ef6dd/examples/megatron/configs/llama3.1_8B-pretrain.yaml){.reference .external} definition.
:::
::::::
::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#run-training .section}
[]{#amd-primus-megatron-lm-run-training}

## Run training[\#](#run-training "Link to this heading"){.headerlink}

Use the following example commands to set up the environment, configure [[key options]{.std .std-ref}](#amd-primus-megatron-lm-benchmark-test-vars){.reference .internal}, and run training on MI300X series GPUs with the AMD Megatron-LM environment.

::::::::::::::::::::::::::::::::::::::::::::::: {#single-node-training .section}
### Single node training[\#](#single-node-training "Link to this heading"){.headerlink}

To run training on a single node, navigate to [`/workspace/Primus`{.docutils .literal .notranslate}]{.pre} and use the following setup command:

:::: {.highlight-shell .notranslate}
::: highlight
    pip install -r requirements.txt
    export HSA_NO_SCRATCH_RECLAIM=1
    export NVTE_CK_USES_BWD_V3=1
:::
::::

::::: {.model-doc .primus-pyt-megatron-lm-train-llama-3-3-70b .docutils .container}
Once setup is complete, run the appropriate training command. The following run commands are tailored to Llama 3.3 70B. See [[Supported models]{.std .std-ref}](#amd-primus-megatron-lm-model-support){.reference .internal} to switch to another available model.

To run pre-training for Llama 3.3 70B BF16, run:

:::: {.highlight-shell .notranslate}
::: highlight
    EXP=examples/megatron/configs/llama3.3_70B-pretrain.yaml \
    bash ./examples/run_pretrain.sh \
        --micro_batch_size 2 \
        --global_batch_size 16 \
        --train_iters 50
:::
::::
:::::

::::::: {.model-doc .primus-pyt-megatron-lm-train-llama-3-1-8b .docutils .container}
Once setup is complete, run the appropriate training command. The following run commands are tailored to Llama 3.1 8B. See [[Supported models]{.std .std-ref}](#amd-primus-megatron-lm-model-support){.reference .internal} to switch to another available model.

To run pre-training for Llama 3.1 8B FP8, run:

:::: {.highlight-shell .notranslate}
::: highlight
    EXP=examples/megatron/configs/llama3.1_8B-pretrain.yaml \
    bash ./examples/run_pretrain.sh \
        --train_iters 50 \
        --fp8 hybrid
:::
::::

For Llama 3.1 8B BF16, use the following command:

:::: {.highlight-shell .notranslate}
::: highlight
    EXP=examples/megatron/configs/llama3.1_8B-pretrain.yaml \
    bash ./examples/run_pretrain.sh --train_iters 50
:::
::::
:::::::

:::::::: {.model-doc .primus-pyt-megatron-lm-train-llama-3-1-70b .docutils .container}
Once setup is complete, run the appropriate training command. The following run commands are tailored to Llama 3.1 70B. See [[Supported models]{.std .std-ref}](#amd-primus-megatron-lm-model-support){.reference .internal} to switch to another available model.

To run pre-training for Llama 3.1 70B BF16, run:

:::: {.highlight-shell .notranslate}
::: highlight
    EXP=examples/megatron/configs/llama3.1_70B-pretrain.yaml \
    bash ./examples/run_pretrain.sh \
         --train_iters 50
:::
::::

To run the training on a single node for Llama 3.1 70B FP8 with proxy, use the following command:

:::: {.highlight-shell .notranslate}
::: highlight
    EXP=examples/megatron/configs/llama3.1_70B-pretrain.yaml \
    bash ./examples/run_pretrain.sh \
        --train_iters 50 \
        --num_layers 40 \
        --fp8 hybrid
:::
::::

::: {.admonition .note}
Note

Use two or more nodes to run the *full* Llama 70B model with FP8 precision.
:::
::::::::

::::::: {.model-doc .primus-pyt-megatron-lm-train-llama-2-7b .docutils .container}
Once setup is complete, run the appropriate training command. The following run commands are tailored to Llama 2 7B. See [[Supported models]{.std .std-ref}](#amd-primus-megatron-lm-model-support){.reference .internal} to switch to another available model.

To run pre-training for Llama 2 7B FP8, run:

:::: {.highlight-shell .notranslate}
::: highlight
    EXP=examples/megatron/configs/llama2_7B-pretrain.yaml \
    bash ./examples/run_pretrain.sh \
        --train_iters 50 \
        --fp8 hybrid
:::
::::

To run pre-training for Llama 2 7B BF16, run:

:::: {.highlight-shell .notranslate}
::: highlight
    EXP=examples/megatron/configs/llama2_7B-pretrain.yaml \
    bash ./examples/run_pretrain.sh --train_iters 50
:::
::::
:::::::

::::: {.model-doc .primus-pyt-megatron-lm-train-llama-2-70b .docutils .container}
Once setup is complete, run the appropriate training command. The following run commands are tailored to Llama 2 70B. See [[Supported models]{.std .std-ref}](#amd-primus-megatron-lm-model-support){.reference .internal} to switch to another available model.

To run pre-training for Llama 2 70B BF16, run:

:::: {.highlight-shell .notranslate}
::: highlight
    EXP=examples/megatron/configs/llama2_70B-pretrain.yaml \
    bash ./examples/run_pretrain.sh --train_iters 50
:::
::::
:::::

::::: {.model-doc .primus-pyt-megatron-lm-train-deepseek-v3-proxy .docutils .container}
Once setup is complete, run the appropriate training command. The following run commands are tailored to DeepSeek-V3. See [[Supported models]{.std .std-ref}](#amd-primus-megatron-lm-model-support){.reference .internal} to switch to another available model.

To run training on a single node for DeepSeek-V3 (MoE with expert parallel) with 3-layer proxy, use the following command:

:::: {.highlight-shell .notranslate}
::: highlight
    EXP=examples/megatron/configs/deepseek_v3-pretrain.yaml \
    bash examples/run_pretrain.sh \
        --num_layers 3 \
        --moe_layer_freq 1 \
        --train_iters 50
:::
::::
:::::

::::: {.model-doc .primus-pyt-megatron-lm-train-deepseek-v2-lite-16b .docutils .container}
Once setup is complete, run the appropriate training command. The following run commands are tailored to DeepSeek-V2-Lite. See [[Supported models]{.std .std-ref}](#amd-primus-megatron-lm-model-support){.reference .internal} to switch to another available model.

To run training on a single node for DeepSeek-V2-Lite (MoE with expert parallel), use the following command:

:::: {.highlight-shell .notranslate}
::: highlight
    EXP=examples/megatron/configs/deepseek_v2_lite-pretrain.yaml \
    bash examples/run_pretrain.sh \
        --global_batch_size 256 \
        --train_iters 50
:::
::::
:::::

::::: {.model-doc .primus-pyt-megatron-lm-train-mixtral-8x7b .docutils .container}
Once setup is complete, run the appropriate training command. The following run commands are tailored to Mixtral 8x7B. See [[Supported models]{.std .std-ref}](#amd-primus-megatron-lm-model-support){.reference .internal} to switch to another available model.

To run training on a single node for Mixtral 8x7B (MoE with expert parallel), use the following command:

:::: {.highlight-shell .notranslate}
::: highlight
    EXP=examples/megatron/configs/mixtral_8x7B_v0.1-pretrain.yaml \
    bash examples/run_pretrain.sh --train_iters 50
:::
::::
:::::

::::: {.model-doc .primus-pyt-megatron-lm-train-mixtral-8x22b-proxy .docutils .container}
Once setup is complete, run the appropriate training command. The following run commands are tailored to Mixtral 8x22B. See [[Supported models]{.std .std-ref}](#amd-primus-megatron-lm-model-support){.reference .internal} to switch to another available model.

To run training on a single node for Mixtral 8x22B (MoE with expert parallel) with 4-layer proxy, use the following command:

:::: {.highlight-shell .notranslate}
::: highlight
    EXP=examples/megatron/configs/mixtral_8x22B_v0.1-pretrain.yaml \
    bash examples/run_pretrain.sh \
        --num_layers 4 \
        --pipeline_model_parallel_size 1 \
        --micro_batch_size 1 \
        --global_batch_size 16 \
        --train_iters 50
:::
::::
:::::

::::::: {.model-doc .primus-pyt-megatron-lm-train-qwen2-5-7b .docutils .container}
Once setup is complete, run the appropriate training command. The following run commands are tailored to Qwen 2.5 7B. See [[Supported models]{.std .std-ref}](#amd-primus-megatron-lm-model-support){.reference .internal} to switch to another available model.

To run training on a single node for Qwen 2.5 7B BF16, use the following command:

:::: {.highlight-shell .notranslate}
::: highlight
    EXP=examples/megatron/configs/qwen2.5_7B-pretrain.yaml \
    bash examples/run_pretrain.sh --train_iters 50
:::
::::

For FP8, use the following command.

:::: {.highlight-shell .notranslate}
::: highlight
    EXP=examples/megatron/configs/qwen2.5_7B-pretrain.yaml \
    bash examples/run_pretrain.sh \
        --train_iters 50 \
        --fp8 hybrid
:::
::::
:::::::

::::: {.model-doc .primus-pyt-megatron-lm-train-qwen2-5-72b .docutils .container}
Once setup is complete, run the appropriate training command. The following run commands are tailored to Qwen 2.5 72B. See [[Supported models]{.std .std-ref}](#amd-primus-megatron-lm-model-support){.reference .internal} to switch to another available model.

To run the training on a single node for Qwen 2.5 72B BF16, use the following command.

:::: {.highlight-shell .notranslate}
::: highlight
    EXP=examples/megatron/configs/qwen2.5_72B-pretrain.yaml \
    bash examples/run_pretrain.sh --train_iters 50
:::
::::
:::::
:::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::: {#multi-node-training-examples .section}
[]{#amd-primus-megatron-multi-node-examples}

### Multi-node training examples[\#](#multi-node-training-examples "Link to this heading"){.headerlink}

Refer to [[Multi-node setup for AI workloads]{.doc}](../../../system-setup/multi-node-setup.html){.reference .internal} to configure your environment for multi-node training.

To run training on multiple nodes, you can use the [run_slurm_pretrain.sh](https://github.com/AMD-AGI/Primus/blob/927a71702784347a311ca48fd45f0f308c6ef6dd/examples/run_slurm_pretrain.sh){.reference .external} to launch the multi-node workload. Use the following steps to setup your environment:

:::: {.highlight-shell .notranslate}
::: highlight
    cd /workspace/Primus/
    export DOCKER_IMAGE=rocm/megatron-lm:v25.8_py310
    export HF_TOKEN=<your_HF_token>
    export HSA_NO_SCRATCH_RECLAIM=1
    export NVTE_CK_USES_BWD_V3=1
    export NCCL_IB_HCA=<your_NCCL_IB_HCA> # specify which RDMA interfaces to use for communication
    export NCCL_SOCKET_IFNAME=<your_NCCL_SOCKET_IFNAME> # your Network Interface
    export GLOO_SOCKET_IFNAME=<your_GLOO_SOCKET_IFNAME> # your Network Interface
    export NCCL_IB_GID_INDEX=3 # Set InfiniBand GID index for NCCL communication. Default is 3 for ROCE
:::
::::

::: {.admonition .note}
Note

- Make sure correct network drivers are installed on the nodes. If inside a Docker, either install the drivers inside the Docker container or pass the network drivers from the host while creating Docker container.

- If [`NCCL_IB_HCA`{.docutils .literal .notranslate}]{.pre} and [`NCCL_SOCKET_IFNAME`{.docutils .literal .notranslate}]{.pre} are not set, Primus will try to auto-detect. However, since NICs can vary accross different cluster, it is encouraged to explicitly export your NCCL parameters for the cluster.

- To find your network interface, you can use [`ip`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`a`{.docutils .literal .notranslate}]{.pre}.

- To find RDMA interfaces, you can use [`ibv_devices`{.docutils .literal .notranslate}]{.pre} to get the list of all the RDMA/IB devices.
:::

::::::: {.model-doc .primus-pyt-megatron-lm-train-llama-3-3-70b .docutils .container}
To train Llama 3.3 70B FP8 on 8 nodes, run:

:::: {.highlight-shell .notranslate}
::: highlight
    NNODES=8 EXP=examples/megatron/configs/llama3.3_70B-pretrain.yaml \
    bash examples/run_slurm_pretrain.sh \
        --micro_batch_size 1 \
        --global_batch_size 256 \
        --recompute_num_layers 80 \
        --fp8 hybrid
:::
::::

To train Llama 3.3 70B BF16 on 8 nodes, run:

:::: {.highlight-shell .notranslate}
::: highlight
    NNODES=8 EXP=examples/megatron/configs/llama3.3_70B-pretrain.yaml \
    bash examples/run_slurm_pretrain.sh \
        --micro_batch_size 1 \
        --global_batch_size 256 \
        --recompute_num_layers 12
:::
::::
:::::::

::::: {.model-doc .primus-pyt-megatron-lm-train-llama-3-1-8b .docutils .container}
To train Llama 3.1 8B FP8 on 8 nodes, run:

:::: {.highlight-shell .notranslate}
::: highlight
    # Adjust the training parameters. For e.g., `global_batch_size: 8 * #single_node_bs` for 8 nodes in this case
    NNODES=8 EXP=examples/megatron/configs/llama3.1_8B-pretrain.yaml \
    bash ./examples/run_slurm_pretrain.sh \
        --global_batch_size 1024 \
        --fp8 hybrid
:::
::::
:::::

::::::: {.model-doc .primus-pyt-megatron-lm-train-llama-3-1-70b .docutils .container}
To train Llama 3.1 70B FP8 on 8 nodes, run:

:::: {.highlight-shell .notranslate}
::: highlight
    NNODES=8 EXP=examples/megatron/configs/llama3.1_70B-pretrain.yaml \
    bash examples/run_slurm_pretrain.sh \
        --micro_batch_size 1 \
        --global_batch_size 256 \
        --recompute_num_layers 80 \
        --fp8 hybrid
:::
::::

To train Llama 3.1 70B BF16 on 8 nodes, run:

:::: {.highlight-shell .notranslate}
::: highlight
    NNODES=8 EXP=examples/megatron/configs/llama3.1_70B-pretrain.yaml \
    bash examples/run_slurm_pretrain.sh \
        --micro_batch_size 1 \
        --global_batch_size 256 \
        --recompute_num_layers 12
:::
::::
:::::::

::::: {.model-doc .primus-pyt-megatron-lm-train-llama-2-7b .docutils .container}
To train Llama 2 8B FP8 on 8 nodes, run:

:::: {.highlight-shell .notranslate}
::: highlight
    # Adjust the training parameters. For e.g., `global_batch_size: 8 * #single_node_bs` for 8 nodes in this case
    NNODES=8 EXP=examples/megatron/configs/llama2_7B-pretrain.yaml bash ./examples/run_slurm_pretrain.sh --global_batch_size 2048 --fp8 hybrid
:::
::::
:::::

::::::: {.model-doc .primus-pyt-megatron-lm-train-llama-2-70b .docutils .container}
To train Llama 2 70B FP8 on 8 nodes, run:

:::: {.highlight-shell .notranslate}
::: highlight
    NNODES=8 EXP=examples/megatron/configs/llama2_70B-pretrain.yaml \
    bash examples/run_slurm_pretrain.sh \
        --micro_batch_size 2 \
        --global_batch_size 256 \
        --recompute_num_layers 80 \
        --fp8 hybrid
:::
::::

To train Llama 2 70B BF16 on 8 nodes, run:

:::: {.highlight-shell .notranslate}
::: highlight
    NNODES=8 EXP=examples/megatron/configs/llama2_70B-pretrain.yaml \
    bash ./examples/run_slurm_pretrain.sh \
        --micro_batch_size 2 \
        --global_batch_size 1536 \
        --recompute_num_layers 12
:::
::::
:::::::

::::: {.model-doc .primus-pyt-megatron-lm-train-mixtral-8x7b .docutils .container}
To train Mixtral 8x7B BF16 on 8 nodes, run:

:::: {.highlight-shell .notranslate}
::: highlight
    NNODES=8 EXP=examples/megatron/configs/mixtral_8x7B_v0.1-pretrain.yaml \
    bash examples/run_slurm_pretrain.sh \
        --micro_batch_size 2 \
        --global_batch_size 256
:::
::::
:::::

::::: {.model-doc .primus-pyt-megatron-lm-train-qwen2-5-72b .docutils .container}
To train Qwen2.5 72B FP8 on 8 nodes, run:

:::: {.highlight-shell .notranslate}
::: highlight
    NNODES=8 EXP=examples/megatron/configs/qwen2.5_72B-pretrain.yaml \
    bash examples/run_slurm_pretrain.sh \
        --micro_batch_size 4 \
        --global_batch_size 256 \
        --recompute_num_layers 80 \
        --fp8 hybrid
:::
::::
:::::
:::::::::::::::::::::::::::::::::

::: {#key-options .section}
[]{#amd-primus-megatron-lm-benchmark-test-vars}

### Key options[\#](#key-options "Link to this heading"){.headerlink}

The following are key options to take note of

fp8

:   [`hybrid`{.docutils .literal .notranslate}]{.pre} enables FP8 GEMMs.

use_torch_fsdp2

:   [`use_torch_fsdp2:`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`1`{.docutils .literal .notranslate}]{.pre} enables torch fsdp-v2. If FSDP is enabled, set [`use_distributed_optimizer`{.docutils .literal .notranslate}]{.pre} and [`overlap_param_gather`{.docutils .literal .notranslate}]{.pre} to [`false`{.docutils .literal .notranslate}]{.pre}.

profile

:   To enable PyTorch profiling, set these parameters:

    :::: {.highlight-yaml .notranslate}
    ::: highlight
        profile: true
        use_pytorch_profiler: true
        profile_step_end: 7
        profile_step_start: 6
    :::
    ::::

train_iters

:   The total number of iterations (default: 50).

mock_data

:   True by default.

micro_batch_size

:   Micro batch size.

global_batch_size

:   Global batch size.

recompute_granularity

:   For activation checkpointing.

num_layers

:   For using a reduced number of layers as with proxy models.
:::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: {#further-reading .section}
## Further reading[\#](#further-reading "Link to this heading"){.headerlink}

- For an introduction to Primus, see [Primus: A Lightweight, Unified Training Framework for Large Models on AMD GPUs](https://rocm.blogs.amd.com/software-tools-optimization/primus/README.html){.reference .external}.

- To learn more about system settings and management practices to configure your system for AMD Instinct MI300X series GPUs, see [AMD Instinct MI300X system optimization](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi300x.html){.reference .external}.

- For a list of other ready-made Docker images for AI with ROCm, see [AMD Infinity Hub](https://www.amd.com/en/developer/resources/infinity-hub.html#f-amd_hub_category=AI%20%26%20ML%20Models){.reference .external}.
:::

::: {#previous-versions .section}
## Previous versions[\#](#previous-versions "Link to this heading"){.headerlink}

See [[Megatron-LM training performance testing version history]{.doc}](megatron-lm-history.html){.reference .internal} to find documentation for previous releases of the [`ROCm/megatron-lm`{.docutils .literal .notranslate}]{.pre} Docker image.

This training environment now uses Primus with Megatron as the primary configuration. Limited support for the legacy ROCm Megatron-LM is still available; see the [[Training a model with Megatron-LM on ROCm]{.doc}](../megatron-lm.html){.reference .internal} documentation.
:::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: prev-next-area
:::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::: {.bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {.page-toc .tocsection .onthispage}
Contents
:::

- [Supported models](#supported-models){.reference .internal .nav-link}
- [System validation](#system-validation){.reference .internal .nav-link}
  - [Environment setup](#environment-setup){.reference .internal .nav-link}
    - [Download the Docker image](#download-the-docker-image){.reference .internal .nav-link}
- [Configuration](#configuration){.reference .internal .nav-link}
  - [Dataset options](#dataset-options){.reference .internal .nav-link}
  - [Tokenizer](#tokenizer){.reference .internal .nav-link}
- [Run training](#run-training){.reference .internal .nav-link}
  - [Single node training](#single-node-training){.reference .internal .nav-link}
  - [Multi-node training examples](#multi-node-training-examples){.reference .internal .nav-link}
  - [Key options](#key-options){.reference .internal .nav-link}
- [Further reading](#further-reading){.reference .internal .nav-link}
- [Previous versions](#previous-versions){.reference .internal .nav-link}
::::
:::::
::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
