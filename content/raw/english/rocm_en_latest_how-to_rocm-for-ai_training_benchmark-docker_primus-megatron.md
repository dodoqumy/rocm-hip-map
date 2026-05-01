---
title: "Training a model with Primus and Megatron-LM"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/training/benchmark-docker/primus-megatron.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-01
---

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-content
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-article-container
:::::::::: {.bd-header-article .d-print-none}
::::::::: {.header-article-items .header-article__inner}
::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}
:::

::: header-article-item
- [](../../../../index.html){.nav-link aria-label="Home"}
- [Use ROCm for AI](../../index.html){.nav-link}
- [Use ROCm for training](../index.html){.nav-link}
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

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#training-a-model-with-primus-and-megatron-lm .section}
# Training a model with Primus and Megatron-LM[\#](#training-a-model-with-primus-and-megatron-lm "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-03-25
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 24 min read time
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

[Primus](https://github.com/AMD-AGI/Primus){.reference .external} is a unified and flexible training framework for AMD Instinct GPUs designed to support multiple training engine backends -- including Megatron -- to deliver scalable, high-performance model training. Performance acceleration is powered by [Primus Turbo](https://github.com/AMD-AGI/Primus-Turbo){.reference .external} and ROCm libraries.

::: {.admonition .note}
Note

For a unified training solution on AMD GPUs with ROCm, the [rocm/megatron-lm](https://hub.docker.com/r/rocm/megatron-lm/){.reference .external} Docker Hub registry will be deprecated soon in favor of [rocm/primus](https://hub.docker.com/r/rocm/primus){.reference .external}. The [`rocm/primus`{.docutils .literal .notranslate}]{.pre} Docker containers will cover PyTorch training ecosystem frameworks, including Megatron-LM and [[torchtitan]{.doc}](primus-pytorch.html){.reference .internal}.

Primus with Megatron is designed to replace the [[ROCm Megatron-LM training]{.doc}](megatron-lm.html){.reference .internal} workflow. To learn how to migrate workloads from Megatron-LM to Primus with Megatron, see [[Migrating workloads to Primus (Megatron backend) from Megatron-LM]{.doc}](previous-versions/megatron-lm-primus-migration-guide.html){.reference .internal}.
:::

AMD provides a ready-to-use Docker images for MI355X, MI350X, MI325X, and MI300X GPUs containing essential components for Primus, ROCm, and Megatron-LM.

::::: {.sd-tab-set .docutils}
rocm/primus:v26.2

:::: {.sd-tab-content .docutils}
::: pst-scrollable-table-container
  Software component   Version
  -------------------- ---------------------
  ROCm                 7.2.0
  PyTorch              2.10.0a0+git449b176
  Python               3.12.3
  Transformer Engine   2.8.0.dev0+51f74fa7
  Flash Attention      2.8.3
  hipBLASLt            1.2.0-de5c1aebb6
  Triton               3.6.0
  RCCL                 2.27.7
:::
::::
:::::

:::::::::::::::::::::::::::::::: {#supported-models .section}
[]{#amd-primus-megatron-lm-model-support-v26-2}

## Supported models[\#](#supported-models "Link to this heading"){.headerlink}

The following models are pre-optimized for performance on AMD Instinct GPUs. Some instructions, commands, and training examples in this documentation might vary by model -- select one to get started.

:::::::::::::::::::::::::::::: {#vllm-benchmark-ud-params-picker .container-fluid}
:::::::::: {.row .gx-0}
::: {.col-2 .me-1 .px-2 .model-param-head}
Model
:::

:::::::: {.row .col-10 .pe-0}
::: {.col-6 .px-2 .model-param param-k="model-group" param-v="llama" tabindex="0"}
Meta Llama
:::

::: {.col-6 .px-2 .model-param param-k="model-group" param-v="zebra-llama" tabindex="0"}
AMD Zebra-Llama
:::

::: {.col-4 .px-2 .model-param param-k="model-group" param-v="deepseek" tabindex="0"}
DeepSeek
:::

::: {.col-4 .px-2 .model-param param-k="model-group" param-v="mistral" tabindex="0"}
Mistral AI
:::

::: {.col-4 .px-2 .model-param param-k="model-group" param-v="qwen" tabindex="0"}
Qwen
:::
::::::::
::::::::::

::::::::::::::::::::: {.row .gx-0 .pt-1}
::: {.col-2 .me-1 .px-2 .model-param-head}
Variant
:::

::::::::::::::::::: {.row .col-10 .pe-0}
::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="primus_pyt_megatron_lm_train_llama-3.3-70b" tabindex="0"}
Llama 3.3 70B
:::

::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="primus_pyt_megatron_lm_train_llama-3.1-8b" tabindex="0"}
Llama 3.1 8B
:::

::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="primus_pyt_megatron_lm_train_llama-3.1-70b" tabindex="0"}
Llama 3.1 70B
:::

::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="primus_pyt_megatron_lm_train_llama-2-7b" tabindex="0"}
Llama 2 7B
:::

::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="primus_pyt_megatron_lm_train_llama-2-70b" tabindex="0"}
Llama 2 70B
:::

::: {.col-4 .px-2 .model-param param-group="zebra-llama" param-k="model" param-v="primus_pyt_megatron_lm_train_zebra-llama-1b" tabindex="0"}
Zebra-Llama 1B
:::

::: {.col-4 .px-2 .model-param param-group="zebra-llama" param-k="model" param-v="primus_pyt_megatron_lm_train_zebra-llama-3b" tabindex="0"}
Zebra-Llama 3B
:::

::: {.col-4 .px-2 .model-param param-group="zebra-llama" param-k="model" param-v="primus_pyt_megatron_lm_train_zebra-llama-8b" tabindex="0"}
Zebra-Llama 8B
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

::: {.col-6 .px-2 .model-param param-group="qwen" param-k="model" param-v="primus_pyt_megatron_lm_train_qwen3-32b-sft" tabindex="0"}
Qwen 3 32B SFT
:::

::: {.col-6 .px-2 .model-param param-group="qwen" param-k="model" param-v="primus_pyt_megatron_lm_train_qwen3-32b-lora" tabindex="0"}
Qwen 3 32B LoRA
:::

::: {.col-6 .px-2 .model-param param-group="qwen" param-k="model" param-v="primus_pyt_megatron_lm_train_qwen2.5-7b" tabindex="0"}
Qwen 2.5 7B
:::

::: {.col-6 .px-2 .model-param param-group="qwen" param-k="model" param-v="primus_pyt_megatron_lm_train_qwen2.5-72b" tabindex="0"}
Qwen 2.5 72B
:::
:::::::::::::::::::
:::::::::::::::::::::
::::::::::::::::::::::::::::::

::: {.admonition .note}
Note

Some models, such as Llama, require an external license agreement through a third party (for example, Meta).
:::
::::::::::::::::::::::::::::::::

::: {#system-validation .section}
## System validation[\#](#system-validation "Link to this heading"){.headerlink}

Before running AI workloads, it's important to validate that your AMD hardware is configured correctly and performing optimally.

If you have already validated your system settings, including aspects like NUMA auto-balancing, you can skip this step. Otherwise, complete the procedures in the [[System validation and optimization]{.std .std-ref}](../../system-setup/prerequisite-system-validation.html#rocm-for-ai-system-optimization){.reference .internal} guide to properly configure your system settings before starting training.

To test for optimal performance, consult the recommended [[System health benchmarks]{.std .std-ref}](../../system-setup/system-health-check.html#rocm-for-ai-system-health-bench){.reference .internal}. This suite of tests will help you verify and fine-tune your system's configuration.
:::

::: {#environment-setup .section}
[]{#mi300x-amd-primus-megatron-lm-training-v26-2}

## Environment setup[\#](#environment-setup "Link to this heading"){.headerlink}

Use the following instructions to set up the environment, configure the script to train models, and reproduce the benchmark results on AMD Instinct GPUs.

Pull the Docker image

1.  Pull the [`rocm/primus:v26.2`{.docutils .literal .notranslate}]{.pre} Docker image from Docker Hub.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker pull rocm/primus:v26.2
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
            rocm/primus:v26.2
    :::
    ::::

    Use these commands if you exit the [`primus_training_env`{.docutils .literal .notranslate}]{.pre} container and need to return to it.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker start primus_training_env
        docker exec -it primus_training_env bash
    :::
    ::::

The Docker container hosts verified commit [`9c529cd4`{.docutils .literal .notranslate}]{.pre} of the [Primus](https://github.com/AMD-AGI/Primus/tree/9c529cd4a934a68a880ede036c3e97b792e38167){.reference .external} repository.
:::

:::::::::::::::::::::::: {#configuration .section}
[]{#amd-primus-megatron-lm-environment-setup-v26-2}

## Configuration[\#](#configuration "Link to this heading"){.headerlink}

Primus defines a training configuration in YAML for each model in [examples/megatron/configs](https://github.com/AMD-AGI/Primus/tree/9c529cd4a934a68a880ede036c3e97b792e38167/examples/megatron/configs){.reference .external}.

::: {.model-doc .primus-pyt-megatron-lm-train-llama-3-3-70b .docutils .container}
For example, to update training parameters for Llama 3.3 70B, you can update [`examples/megatron/configs/llama3.3_70B-pretrain.yaml`{.docutils .literal .notranslate}]{.pre}. Training configuration YAML files for other models follow this naming convention.
:::

::: {.model-doc .primus-pyt-megatron-lm-train-llama-3-1-8b .docutils .container}
For example, to update training parameters for Llama 3.1 8B, you can update [`examples/megatron/configs/llama3.1_8B-pretrain.yaml`{.docutils .literal .notranslate}]{.pre}. Training configuration YAML files for other models follow this naming convention.
:::

::: {.model-doc .primus-pyt-megatron-lm-train-llama-3-1-70b .docutils .container}
For example, to update training parameters for Llama 3.1 70B, you can update [`examples/megatron/configs/llama3.1_70B-pretrain.yaml`{.docutils .literal .notranslate}]{.pre}. Training configuration YAML files for other models follow this naming convention.
:::

::: {.model-doc .primus-pyt-megatron-lm-train-llama-2-7b .docutils .container}
For example, to update training parameters for Llama 2 7B, you can update [`examples/megatron/configs/llama2_7B-pretrain.yaml`{.docutils .literal .notranslate}]{.pre}. Training configuration YAML files for other models follow this naming convention.
:::

::: {.model-doc .primus-pyt-megatron-lm-train-llama-2-70b .docutils .container}
For example, to update training parameters for Llama 2 70B, you can update [`examples/megatron/configs/llama2_70B-pretrain.yaml`{.docutils .literal .notranslate}]{.pre}. Training configuration YAML files for other models follow this naming convention.
:::

::: {.model-doc .primus-pyt-megatron-lm-train-zebra-llama-1b .docutils .container}
For example, to update training parameters for Zebra-Llama 1B, you can update [`examples/megatron/configs/zebra_llama_1b-pretrain.yaml`{.docutils .literal .notranslate}]{.pre}. Training configuration YAML files for other models follow this naming convention.
:::

::: {.model-doc .primus-pyt-megatron-lm-train-zebra-llama-3b .docutils .container}
For example, to update training parameters for Zebra-Llama 3B, you can update [`examples/megatron/configs/zebra_llama_3b-pretrain.yaml`{.docutils .literal .notranslate}]{.pre}. Training configuration YAML files for other models follow this naming convention.
:::

::: {.model-doc .primus-pyt-megatron-lm-train-zebra-llama-8b .docutils .container}
For example, to update training parameters for Zebra-Llama 8B, you can update [`examples/megatron/configs/zebra_llama_8b-pretrain.yaml`{.docutils .literal .notranslate}]{.pre}. Training configuration YAML files for other models follow this naming convention.
:::

::: {.model-doc .primus-pyt-megatron-lm-train-deepseek-v3-proxy .docutils .container}
For example, to update training parameters for DeepSeek-V3 (proxy), you can update [`examples/megatron/configs/deepseek_v3-pretrain.yaml`{.docutils .literal .notranslate}]{.pre}. Training configuration YAML files for other models follow this naming convention.
:::

::: {.model-doc .primus-pyt-megatron-lm-train-deepseek-v2-lite-16b .docutils .container}
For example, to update training parameters for DeepSeek-V2-Lite, you can update [`examples/megatron/configs/deepseek_v2_lite-pretrain.yaml`{.docutils .literal .notranslate}]{.pre}. Training configuration YAML files for other models follow this naming convention.
:::

::: {.model-doc .primus-pyt-megatron-lm-train-mixtral-8x7b .docutils .container}
For example, to update training parameters for Mixtral 8x7B, you can update [`examples/megatron/configs/mixtral_8x7B_v0.1-pretrain.yaml`{.docutils .literal .notranslate}]{.pre}. Training configuration YAML files for other models follow this naming convention.
:::

::: {.model-doc .primus-pyt-megatron-lm-train-mixtral-8x22b-proxy .docutils .container}
For example, to update training parameters for Mixtral 8x22B (proxy), you can update [`examples/megatron/configs/mixtral_8x22B_v0.1-pretrain.yaml`{.docutils .literal .notranslate}]{.pre}. Training configuration YAML files for other models follow this naming convention.
:::

::: {.model-doc .primus-pyt-megatron-lm-train-qwen3-32b-sft .docutils .container}
For example, to update training parameters for Qwen 3 32B SFT, you can update [`examples/megatron/configs/`{.docutils .literal .notranslate}]{.pre}. Training configuration YAML files for other models follow this naming convention.
:::

::: {.model-doc .primus-pyt-megatron-lm-train-qwen3-32b-lora .docutils .container}
For example, to update training parameters for Qwen 3 32B LoRA, you can update [`examples/megatron/configs/primus_qwen2.5_7B-pretrain.yaml`{.docutils .literal .notranslate}]{.pre}. Training configuration YAML files for other models follow this naming convention.
:::

::: {.model-doc .primus-pyt-megatron-lm-train-qwen2-5-7b .docutils .container}
For example, to update training parameters for Qwen 2.5 7B, you can update [`examples/megatron/configs/primus_qwen2.5_7B-pretrain.yaml`{.docutils .literal .notranslate}]{.pre}. Training configuration YAML files for other models follow this naming convention.
:::

::: {.model-doc .primus-pyt-megatron-lm-train-qwen2-5-72b .docutils .container}
For example, to update training parameters for Qwen 2.5 72B, you can update [`examples/megatron/configs/qwen2.5_72B-pretrain.yaml`{.docutils .literal .notranslate}]{.pre}. Training configuration YAML files for other models follow this naming convention.
:::

::: {.admonition .note}
Note

See [[Key options]{.std .std-ref}](previous-versions/primus-megatron-v25.8.html#amd-primus-megatron-lm-benchmark-test-vars){.reference .internal} for more information on configuration options.
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

::::: {#tokenizer .section}
[]{#amd-primus-megatron-lm-tokenizer-v26-2}

### Tokenizer[\#](#tokenizer "Link to this heading"){.headerlink}

Set the [`HF_TOKEN`{.docutils .literal .notranslate}]{.pre} environment variable with right permissions to access the tokenizer for each model.

:::: {.highlight-bash .notranslate}
::: highlight
    # Export your HF_TOKEN in the workspace
    export HF_TOKEN=<your_hftoken>
:::
::::
:::::
::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#run-training .section}
[]{#amd-primus-megatron-lm-run-training-v26-2}

## Run training[\#](#run-training "Link to this heading"){.headerlink}

Use the following example commands to set up the environment, configure [[key options]{.std .std-ref}](previous-versions/primus-megatron-v25.8.html#amd-primus-megatron-lm-benchmark-test-vars){.reference .internal}, and run training on AMD Instinct GPUs using Primus with the Megatron backend.

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#single-node-training .section}
### Single node training[\#](#single-node-training "Link to this heading"){.headerlink}

To run training on a single node, navigate to [`/workspace/Primus`{.docutils .literal .notranslate}]{.pre} and use the following setup command:

:::: {.highlight-shell .notranslate}
::: highlight
    pip install -r requirements.txt
:::
::::

:::::::::: {.model-doc .primus-pyt-megatron-lm-train-llama-3-3-70b .docutils .container}
Once setup is complete, run the appropriate training command. The following run commands are tailored to Llama 3.3 70B. See [[Supported models]{.std .std-ref}](#amd-primus-megatron-lm-model-support-v26-2){.reference .internal} to switch to another available model.

To run pre-training for Llama 3.3 70B BF16, run:

::::::::: {.sd-tab-set .docutils}
MI355X and MI350X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    bash runner/primus-cli direct \
      --log_file /tmp/primus_llama3.3_70B.log \
      -- train pretrain \
      --config examples/megatron/configs/MI355X/llama3.3_70B-BF16-pretrain.yaml
:::
::::
:::::

MI300X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    # Set the variables for better performance
    # only on MI325X and MI300X
    export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
    export NVTE_CK_IS_V3_ATOMIC_FP32=1

    bash runner/primus-cli direct \
      --log_file /tmp/primus_llama3.3_70B.log \
      -- train pretrain \
      --config examples/megatron/configs/MI300X/llama3.3_70B-BF16-pretrain.yaml
:::
::::
:::::
:::::::::
::::::::::

::::::::::::::::: {.model-doc .primus-pyt-megatron-lm-train-llama-3-1-8b .docutils .container}
Once setup is complete, run the appropriate training command. The following run commands are tailored to Llama 3.1 8B. See [[Supported models]{.std .std-ref}](#amd-primus-megatron-lm-model-support-v26-2){.reference .internal} to switch to another available model.

To run pre-training for Llama 3.1 8B FP8, run:

::::::::: {.sd-tab-set .docutils}
MI355X and MI350X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    bash runner/primus-cli direct \
      --log_file /tmp/primus_llama3.1_8B_fp8.log \
      -- train pretrain \
      --config examples/megatron/configs/MI355X/llama3.1_8B-FP8-pretrain.yaml
:::
::::
:::::

MI300X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    # Set the variables for better performance
    # only on MI325X and MI300X
    export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
    export NVTE_CK_IS_V3_ATOMIC_FP32=1

    bash runner/primus-cli direct \
      --log_file /tmp/primus_llama3.1_8B_fp8.log \
      -- train pretrain \
      --config examples/megatron/configs/MI300X/llama3.1_8B-FP8-pretrain.yaml
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
    bash runner/primus-cli direct \
      --log_file /tmp/primus_llama3.1_8B.log \
      -- train pretrain \
      --config examples/megatron/configs/MI355X/llama3.1_8B-BF16-pretrain.yaml
:::
::::
:::::

MI300X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    # Set the variables for better performance
    # only on MI325X and MI300X
    export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
    export NVTE_CK_IS_V3_ATOMIC_FP32=1

    bash runner/primus-cli direct \
      --log_file /tmp/primus_llama3.1_8B.log \
      -- train pretrain \
      --config examples/megatron/configs/MI300X/llama3.1_8B-BF16-pretrain.yaml
:::
::::
:::::
:::::::::
:::::::::::::::::

:::::::::::::::::: {.model-doc .primus-pyt-megatron-lm-train-llama-3-1-70b .docutils .container}
Once setup is complete, run the appropriate training command. The following run commands are tailored to Llama 3.1 70B. See [[Supported models]{.std .std-ref}](#amd-primus-megatron-lm-model-support-v26-2){.reference .internal} to switch to another available model.

To run pre-training for Llama 3.1 70B BF16, run:

::::::::: {.sd-tab-set .docutils}
MI355X and MI350X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    bash runner/primus-cli direct \
      --log_file /tmp/primus_llama3.1_70B.log \
      -- train pretrain \
      --config examples/megatron/configs/MI355X/llama3.1_70B-BF16-pretrain.yaml \
      --micro_batch_size 8 \
      --global_batch_size 128
:::
::::
:::::

MI300X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    # Set the variables for better performance
    # only on MI325X and MI300X
    export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
    export NVTE_CK_IS_V3_ATOMIC_FP32=1

    bash runner/primus-cli direct \
      --log_file /tmp/primus_llama3.1_70B.log \
      -- train pretrain \
      --config examples/megatron/configs/MI300X/llama3.1_70B-BF16-pretrain.yaml
:::
::::
:::::
:::::::::

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
    bash runner/primus-cli direct \
      --log_file /tmp/primus_llama3.1_70B_fp8.log \
      -- train pretrain \
      --config examples/megatron/configs/MI355X/llama3.1_70B-FP8-pretrain.yaml
:::
::::
:::::

MI300X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    # Set the variables for better performance
    # only on MI325X and MI300X
    export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
    export NVTE_CK_IS_V3_ATOMIC_FP32=1

    bash runner/primus-cli direct \
      --log_file /tmp/primus_llama3.1_70B_fp8_proxy.log \
      -- train pretrain \
      --config examples/megatron/configs/MI300X/llama3.1_70B-FP8-pretrain.yaml \
      --train_iters 50 \
      --num_layers 40 \
      --fp8 hybrid \
      --no_fp8_weight_transpose_cache true
:::
::::
:::::
:::::::::
::::::::::::::::::

::::::::::::::::: {.model-doc .primus-pyt-megatron-lm-train-llama-2-7b .docutils .container}
Once setup is complete, run the appropriate training command. The following run commands are tailored to Llama 2 7B. See [[Supported models]{.std .std-ref}](#amd-primus-megatron-lm-model-support-v26-2){.reference .internal} to switch to another available model.

To run pre-training for Llama 2 7B FP8, run:

::::::::: {.sd-tab-set .docutils}
MI355X and MI350X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    bash runner/primus-cli direct \
      --log_file /tmp/primus_llama2_7B_fp8.log \
      -- train pretrain \
      --config examples/megatron/configs/MI355X/llama2_7B-FP8-pretrain.yaml
:::
::::
:::::

MI300X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    # Set the variables for better performance
    # only on MI325X and MI300X
    export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
    export NVTE_CK_IS_V3_ATOMIC_FP32=1

    bash runner/primus-cli direct \
      --log_file /tmp/primus_llama2_7B_fp8.log \
      -- train pretrain \
      --config examples/megatron/configs/MI300X/llama2_7B-FP8-pretrain.yaml
:::
::::
:::::
:::::::::

To run pre-training for Llama 2 7B BF16, run:

::::::::: {.sd-tab-set .docutils}
MI355X and MI350X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    bash runner/primus-cli direct \
      --log_file /tmp/primus_llama2_7B.log \
      -- train pretrain \
      --config examples/megatron/configs/MI355X/llama2_7B-BF16-pretrain.yaml
:::
::::
:::::

MI300X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    # Set the variables for better performance
    # only on MI325X and MI300X
    export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
    export NVTE_CK_IS_V3_ATOMIC_FP32=1

    bash runner/primus-cli direct \
      --log_file /tmp/primus_llama2_7B.log \
      -- train pretrain \
      --config examples/megatron/configs/MI300X/llama2_7B-BF16-pretrain.yaml
:::
::::
:::::
:::::::::
:::::::::::::::::

:::::::::: {.model-doc .primus-pyt-megatron-lm-train-llama-2-70b .docutils .container}
Once setup is complete, run the appropriate training command. The following run commands are tailored to Llama 2 70B. See [[Supported models]{.std .std-ref}](#amd-primus-megatron-lm-model-support-v26-2){.reference .internal} to switch to another available model.

To run pre-training for Llama 2 70B BF16, run:

::::::::: {.sd-tab-set .docutils}
MI355X and MI350X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    bash runner/primus-cli direct \
      --log_file /tmp/primus_llama2_70B.log \
      -- train pretrain \
      --config examples/megatron/configs/MI355X/llama2_70B-BF16-pretrain.yaml
:::
::::
:::::

MI300X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    # Set the variables for better performance
    # only on MI325X and MI300X
    export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
    export NVTE_CK_IS_V3_ATOMIC_FP32=1

    bash runner/primus-cli direct \
      --log_file /tmp/primus_llama2_70B.log \
      -- train pretrain \
      --config examples/megatron/configs/MI300X/llama2_70B-BF16-pretrain.yaml
:::
::::
:::::
:::::::::
::::::::::

:::::::::: {.model-doc .primus-pyt-megatron-lm-train-deepseek-v3-proxy .docutils .container}
Once setup is complete, run the appropriate training command. The following run commands are tailored to DeepSeek-V3. See [[Supported models]{.std .std-ref}](#amd-primus-megatron-lm-model-support-v26-2){.reference .internal} to switch to another available model.

To run training on a single node for DeepSeek-V3 (MoE with expert parallel) BF16 with 3-layer proxy, use the following command:

::::::::: {.sd-tab-set .docutils}
MI355X and MI350X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    bash runner/primus-cli direct \
      --log_file /tmp/primus_deepseek_v3_proxy.log \
      -- train pretrain \
      --config examples/megatron/configs/MI355X/deepseek_v3-BF16-pretrain.yaml \
      --num_layers 3 \
      --moe_layer_freq 1 \
      --train_iters 50 \
      --micro_batch_size 8 \
      --global_batch_size 64 \
      --moe_use_fused_router_with_aux_score True \
      --moe_permute_fusion True
:::
::::
:::::

MI300X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    # Set the variables for better performance
    # only on MI325X and MI300X
    export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
    export NVTE_CK_IS_V3_ATOMIC_FP32=1

    bash runner/primus-cli direct \
      --log_file /tmp/primus_deepseek_v3_proxy.log \
      -- train pretrain \
      --config examples/megatron/configs/MI300X/deepseek_v3-BF16-pretrain.yaml \
      --num_layers 3 \
      --moe_layer_freq 1 \
      --micro_batch_size 3 \
      --global_batch_size 192 \
      --train_iters 50
:::
::::
:::::
:::::::::
::::::::::

:::::::::: {.model-doc .primus-pyt-megatron-lm-train-deepseek-v2-lite-16b .docutils .container}
Once setup is complete, run the appropriate training command. The following run commands are tailored to DeepSeek-V2-Lite. See [[Supported models]{.std .std-ref}](#amd-primus-megatron-lm-model-support-v26-2){.reference .internal} to switch to another available model.

To run training on a single node for DeepSeek-V2-Lite (MoE with expert parallel) BF16, use the following command:

::::::::: {.sd-tab-set .docutils}
MI355X and MI350X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    bash runner/primus-cli direct \
      --log_file /tmp/primus_deepseek_v2_lite.log \
      -- train pretrain \
      --config examples/megatron/configs//MI355X/deepseek_v2_lite-BF16-pretrain.yaml \
      --use_turbo_grouped_mlp False \
      --moe_use_legacy_grouped_gemm True \
      --moe_use_fused_router_with_aux_score True \
      --moe_permute_fusion True
:::
::::
:::::

MI300X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    # Set the variables for better performance
    # only on MI325X and MI300X
    export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
    export NVTE_CK_IS_V3_ATOMIC_FP32=1

    bash runner/primus-cli direct \
      --log_file /tmp/primus_deepseek_v2_lite.log \
      -- train pretrain \
      --config examples/megatron/configs/MI300X/deepseek_v2_lite-BF16-pretrain.yaml
:::
::::
:::::
:::::::::
::::::::::

:::::::::: {.model-doc .primus-pyt-megatron-lm-train-mixtral-8x7b .docutils .container}
Once setup is complete, run the appropriate training command. The following run commands are tailored to Mixtral 8x7B. See [[Supported models]{.std .std-ref}](#amd-primus-megatron-lm-model-support-v26-2){.reference .internal} to switch to another available model.

To run training on a single node for Mixtral 8x7B (MoE with expert parallel), use the following command:

::::::::: {.sd-tab-set .docutils}
MI355X and MI350X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    bash runner/primus-cli direct \
      --log_file /tmp/primus_mixtral_8x7B.log \
      -- train pretrain \
      --config examples/megatron/configs/MI355X/mixtral_8x7B_v0.1-BF16-pretrain.yaml
:::
::::
:::::

MI300X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    # Set the variables for better performance
    # only on MI325X and MI300X
    export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
    export NVTE_CK_IS_V3_ATOMIC_FP32=1

    bash runner/primus-cli direct \
      --log_file /tmp/primus_mixtral_8x7B.log \
      -- train pretrain \
      --config examples/megatron/configs/MI300X/mixtral_8x7B_v0.1-BF16-pretrain.yaml
:::
::::
:::::
:::::::::
::::::::::

:::::::::: {.model-doc .primus-pyt-megatron-lm-train-mixtral-8x22b-proxy .docutils .container}
Once setup is complete, run the appropriate training command. The following run commands are tailored to Mixtral 8x22B. See [[Supported models]{.std .std-ref}](#amd-primus-megatron-lm-model-support-v26-2){.reference .internal} to switch to another available model.

To run training on a single node for Mixtral 8x22B BF16 (MoE with expert parallel) 4-layer proxy, use the following command:

::::::::: {.sd-tab-set .docutils}
MI355X and MI350X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    bash runner/primus-cli direct \
      --log_file /tmp/primus_mixtral_8x22B_proxy.log \
      -- train pretrain \
      --config examples/megatron/configs/MI355X/mixtral_8x22B_v0.1-BF16-pretrain.yaml
:::
::::
:::::

MI300X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    # Set the variables for better performance
    # only on MI325X and MI300X
    export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
    export NVTE_CK_IS_V3_ATOMIC_FP32=1

    bash runner/primus-cli direct \
      --log_file /tmp/primus_mixtral_8x22B_proxy.log \
      -- train pretrain \
      --config examples/megatron/configs/MI300X/mixtral_8x22B_v0.1-BF16-pretrain.yaml \
      --num_layers 4 \
      --pipeline_model_parallel_size 1 \
      --micro_batch_size 1 \
      --global_batch_size 16 \
      --train_iters 50
:::
::::
:::::
:::::::::
::::::::::

:::::::::: {.model-doc .primus-pyt-megatron-lm-train-qwen3-32b-lora .docutils .container}
Once setup is complete, run the appropriate training command. The following run commands are tailored to post-training Qwen 3 32B (LoRA). See [[Supported models]{.std .std-ref}](#amd-primus-megatron-lm-model-support-v26-2){.reference .internal} to switch to another available model.

To run training on a single node for Qwen 3 32B BF16 (SFT), use the following command:

::::::::: {.sd-tab-set .docutils}
MI355X and MI350X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    bash runner/primus-cli direct \
      --log_file /tmp/primus_qwen3_32b.log \
      -- train posttrain \
      --config examples/megatron_bridge/configs/MI355X/qwen3_32b_lora_posttrain.yaml
:::
::::
:::::

MI300X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    # Set the variables for better performance
    # only on MI325X and MI300X
    export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
    export NVTE_CK_IS_V3_ATOMIC_FP32=1

    bash runner/primus-cli direct \
      --log_file /tmp/primus_qwen3_32b.log \
      -- train posttrain \
      --config examples/megatron_bridge/configs/MI300X/qwen3_32b_lora_posttrain.yaml
:::
::::
:::::
:::::::::
::::::::::

:::::::::: {.model-doc .primus-pyt-megatron-lm-train-qwen3-32b-sft .docutils .container}
Once setup is complete, run the appropriate training command. The following run commands are tailored to post-training Qwen 3 32B (SFT). See [[Supported models]{.std .std-ref}](#amd-primus-megatron-lm-model-support-v26-2){.reference .internal} to switch to another available model.

To run training on a single node for Qwen 3 32B BF16 (SFT), use the following command:

::::::::: {.sd-tab-set .docutils}
MI355X and MI350X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    bash runner/primus-cli direct \
      --log_file /tmp/primus_qwen3_32b_sft.log \
      -- train posttrain \
      --config examples/megatron_bridge/configs/MI355X/qwen3_32b_sft_posttrain.yaml
:::
::::
:::::

MI300X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    # Set the variables for better performance
    # only on MI325X and MI300X
    export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
    export NVTE_CK_IS_V3_ATOMIC_FP32=1

    bash runner/primus-cli direct \
      --log_file /tmp/primus_qwen3_32b_sft.log \
      -- train posttrain \
      --config examples/megatron_bridge/configs/MI300X/qwen3_32b_sft_posttrain.yaml
:::
::::
:::::
:::::::::
::::::::::

::::::::::::::::: {.model-doc .primus-pyt-megatron-lm-train-qwen2-5-7b .docutils .container}
Once setup is complete, run the appropriate training command. The following run commands are tailored to Qwen 2.5 7B. See [[Supported models]{.std .std-ref}](#amd-primus-megatron-lm-model-support-v26-2){.reference .internal} to switch to another available model.

To run training on a single node for Qwen 2.5 7B BF16, use the following command:

::::::::: {.sd-tab-set .docutils}
MI355X and MI350X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    bash runner/primus-cli direct \
      --log_file /tmp/primus_qwen2.5_7B.log \
      -- train pretrain \
      --config examples/megatron/configs/MI355X/qwen2.5_7B-BF16-pretrain.yaml
:::
::::
:::::

MI300X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    # Set the variables for better performance
    # only on MI325X and MI300X
    export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
    export NVTE_CK_IS_V3_ATOMIC_FP32=1

    bash runner/primus-cli direct \
      --log_file /tmp/primus_qwen2.5_7B.log \
      -- train pretrain \
      --config examples/megatron/configs/MI300X/qwen2.5_7B-BF16-pretrain.yaml
:::
::::
:::::
:::::::::

For FP8, use the following command.

::::::::: {.sd-tab-set .docutils}
MI355X and MI350X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    bash runner/primus-cli direct \
      --log_file /tmp/primus_qwen2.5_7B_fp8.log \
      -- train pretrain \
      --config examples/megatron/configs/MI355X/qwen2.5_7B-FP8-pretrain.yaml
:::
::::
:::::

MI300X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    # Set the variables for better performance
    # only on MI325X and MI300X
    export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
    export NVTE_CK_IS_V3_ATOMIC_FP32=1

    bash runner/primus-cli direct \
      --log_file /tmp/primus_qwen2.5_7B_fp8.log \
      -- train pretrain \
      --config examples/megatron/configs/MI300X/qwen2.5_7B-FP8-pretrain.yaml
:::
::::
:::::
:::::::::
:::::::::::::::::

:::::::::: {.model-doc .primus-pyt-megatron-lm-train-qwen2-5-72b .docutils .container}
Once setup is complete, run the appropriate training command. The following run commands are tailored to Qwen 2.5 72B. See [[Supported models]{.std .std-ref}](#amd-primus-megatron-lm-model-support-v26-2){.reference .internal} to switch to another available model.

To run the training on a single node for Qwen 2.5 72B BF16, use the following command.

::::::::: {.sd-tab-set .docutils}
MI355X and MI350X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    bash runner/primus-cli direct \
      --log_file /tmp/primus_qwen2.5_72B.log \
      -- train pretrain \
      --config examples/megatron/configs/MI355X/qwen2.5_72B-BF16-pretrain.yaml
:::
::::
:::::

MI300X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    # Set the variables for better performance
    # only on MI325X and MI300X
    export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
    export NVTE_CK_IS_V3_ATOMIC_FP32=1

    bash runner/primus-cli direct \
      --log_file /tmp/primus_qwen2.5_72B.log \
      -- train pretrain \
      --config examples/megatron/configs/MI300X/qwen2.5_72B-BF16-pretrain.yaml
:::
::::
:::::
:::::::::
::::::::::

:::::::::: {.model-doc .primus-pyt-megatron-lm-train-zebra-llama-1b .docutils .container}
Once setup is complete, run the appropriate training command. The following run commands are tailored to Zebra-Llama 1B. See [[Supported models]{.std .std-ref}](#amd-primus-megatron-lm-model-support-v26-2){.reference .internal} to switch to another available model.

To run the training on a single node for AMD Zebra-Llama 1B BF16, use the following command.

::::::::: {.sd-tab-set .docutils}
MI355X and MI350X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    PRIMUS_TRAIN_RUNTIME=legacy bash runner/primus-cli direct \
      --log_file /tmp/primus_zebra_llama_1B.log \
      -- train pretrain \
      --config examples/megatron/configs/MI355X/zebra_llama_1B-pretrain.yaml
:::
::::
:::::

MI300X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    # Set the variables for better performance
    # only on MI325X and MI300X
    export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
    export NVTE_CK_IS_V3_ATOMIC_FP32=1

    PRIMUS_TRAIN_RUNTIME=legacy bash runner/primus-cli direct \
      --log_file /tmp/primus_zebra_llama_1B.log \
      -- train pretrain \
      --config examples/megatron/configs/MI300X/zebra_llama_1B-pretrain.yaml
:::
::::
:::::
:::::::::
::::::::::

:::::::::: {.model-doc .primus-pyt-megatron-lm-train-zebra-llama-3b .docutils .container}
Once setup is complete, run the appropriate training command. The following run commands are tailored to Zebra-Llama 3B. See [[Supported models]{.std .std-ref}](#amd-primus-megatron-lm-model-support-v26-2){.reference .internal} to switch to another available model.

To run the training on a single node for AMD Zebra-Llama 3B BF16, use the following command.

::::::::: {.sd-tab-set .docutils}
MI355X and MI350X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    PRIMUS_TRAIN_RUNTIME=legacy bash runner/primus-cli direct \
      --log_file /tmp/primus_zebra_llama_3B.log \
      -- train pretrain \
      --config examples/megatron/configs/MI355X/zebra_llama_3B-pretrain.yaml
:::
::::
:::::

MI300X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    # Set the variables for better performance
    # only on MI325X and MI300X
    export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
    export NVTE_CK_IS_V3_ATOMIC_FP32=1

    PRIMUS_TRAIN_RUNTIME=legacy bash runner/primus-cli direct \
      --log_file /tmp/primus_zebra_llama_3B.log \
      -- train pretrain \
      --config examples/megatron/configs/MI300X/zebra_llama_3B-pretrain.yaml
:::
::::
:::::
:::::::::
::::::::::

:::::::::: {.model-doc .primus-pyt-megatron-lm-train-zebra-llama-8b .docutils .container}
Once setup is complete, run the appropriate training command. The following run commands are tailored to Zebra Llama 8B. See [[Supported models]{.std .std-ref}](#amd-primus-megatron-lm-model-support-v26-2){.reference .internal} to switch to another available model.

To run the training on a single node for AMD Zebra-Llama 8B BF16, use the following command.

::::::::: {.sd-tab-set .docutils}
MI355X and MI350X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    PRIMUS_TRAIN_RUNTIME=legacy bash runner/primus-cli direct \
      --log_file /tmp/primus_zebra_llama_8B.log \
      -- train pretrain \
      --config examples/megatron/configs/MI355X/zebra_llama_8B-pretrain.yaml
:::
::::
:::::

MI300X

::::: {.sd-tab-content .docutils}
:::: {.highlight-shell .notranslate}
::: highlight
    # Set the variables for better performance
    # only on MI325X and MI300X
    export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
    export NVTE_CK_IS_V3_ATOMIC_FP32=1

    PRIMUS_TRAIN_RUNTIME=legacy bash runner/primus-cli direct \
      --log_file /tmp/primus_zebra_llama_8B.log \
      -- train pretrain \
      --config examples/megatron/configs/MI300X/zebra_llama_8B-pretrain.yaml
:::
::::
:::::
:::::::::
::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::: {#multi-node-training-examples .section}
[]{#amd-primus-megatron-multi-node-examples-v26-2}

### Multi-node training examples[\#](#multi-node-training-examples "Link to this heading"){.headerlink}

Refer to [[Multi-node setup for AI workloads]{.doc}](../../system-setup/multi-node-setup.html){.reference .internal} to configure your environment for multi-node training.

To run training on multiple nodes, you can use the [run_slurm_pretrain.sh](https://github.com/AMD-AGI/Primus/blob/9c529cd4a934a68a880ede036c3e97b792e38167/examples/run_slurm_pretrain.sh){.reference .external} to launch the multi-node workload. Use the following steps to setup your environment:

:::: {.highlight-shell .notranslate}
::: highlight
    git clone --recurse-submodules https://github.com/AMD-AGI/Primus.git
    cd Primus/
    git checkout 44f780d
    git submodule update --init --recursive
    export DOCKER_IMAGE=rocm/primus:v26.2
    export HF_TOKEN=<your_HF_token>
    export NCCL_IB_HCA=<your_NCCL_IB_HCA> # specify which RDMA interfaces to use for communication
    export NCCL_SOCKET_IFNAME=<your_NCCL_SOCKET_IFNAME> # your Network Interface
    export GLOO_SOCKET_IFNAME=<your_GLOO_SOCKET_IFNAME> # your Network Interface
    export NCCL_IB_GID_INDEX=3 # Set InfiniBand GID index for NCCL communication. Default is 3 for ROCE

    # Set the variables for better performance
    # only on MI325X and MI300X
    export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
    export NVTE_CK_IS_V3_ATOMIC_FP32=1
:::
::::

::: {.admonition .note}
Note

- Make sure correct network drivers are installed on the nodes. If inside a Docker, either install the drivers inside the Docker container or pass the network drivers from the host while creating Docker container.

- If [`NCCL_IB_HCA`{.docutils .literal .notranslate}]{.pre} and [`NCCL_SOCKET_IFNAME`{.docutils .literal .notranslate}]{.pre} are not set, Primus will try to auto-detect. However, since NICs can vary accross different cluster, it is encouraged to explicitly export your NCCL parameters for the cluster.

- To find your network interface, you can use [`ip`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`a`{.docutils .literal .notranslate}]{.pre}.

- To find RDMA interfaces, you can use [`ibv_devices`{.docutils .literal .notranslate}]{.pre} to get the list of all the RDMA/IB devices.

- Remember to set [`DOCKER_IMAGE`{.docutils .literal .notranslate}]{.pre} and [`HF_TOKEN`{.docutils .literal .notranslate}]{.pre} (see [[Tokenizer]{.std .std-ref}](#amd-primus-megatron-lm-tokenizer-v26-2){.reference .internal}) as appropriate.
:::

::::: {.model-doc .primus-pyt-megatron-lm-train-llama-3-1-8b .docutils .container}
Once setup is complete, run the appropriate training command. The following run commands are tailored to Llama 3.1 8B. See [[Supported models]{.std .std-ref}](#amd-primus-megatron-lm-model-support-v26-2){.reference .internal} to switch to another available model.

To train Llama 3.1 8B FP8 on 8 nodes, run:

:::: {.highlight-shell .notranslate}
::: highlight
    # Adjust the training parameters.
    # For example, `global_batch_size: 8 * #single_node_bs` for 8 nodes in this case.
    NNODES=8 \
    EXP=examples/megatron/configs/MI300X/llama3.1_8B-FP8-pretrain.yaml \
    bash ./examples/run_slurm_pretrain.sh \
        --global_batch_size 1024 \
:::
::::
:::::

::::: {.model-doc .primus-pyt-megatron-lm-train-llama-2-7b .docutils .container}
Once setup is complete, run the appropriate training command. The following run commands are tailored to Llama 2 7B. See [[Supported models]{.std .std-ref}](#amd-primus-megatron-lm-model-support-v26-2){.reference .internal} to switch to another available model.

To train Llama 2 7B FP8 on 8 nodes, run:

:::: {.highlight-shell .notranslate}
::: highlight
    # Adjust the training parameters.
    # For example, `global_batch_size: 8 * #single_node_bs` for 8 nodes in this case.
    NNODES=8 \
    EXP=examples/megatron/configs/MI300X/llama2_7B-FP8-pretrain.yaml \
    bash ./examples/run_slurm_pretrain.sh \
        --global_batch_size 2048 \
:::
::::
:::::

::::::: {.model-doc .primus-pyt-megatron-lm-train-llama-3-1-70b .docutils .container}
Once setup is complete, run the appropriate training command. The following run commands are tailored to Llama 3.1 70B. See [[Supported models]{.std .std-ref}](#amd-primus-megatron-lm-model-support-v26-2){.reference .internal} to switch to another available model.

To train Llama 3.1 70B FP8 on 8 nodes, run:

:::: {.highlight-shell .notranslate}
::: highlight
    # Adjust the training parameters.
    # For example, `global_batch_size: 8 * #single_node_bs` for 8 nodes in this case.
    NNODES=8 \
    EXP=examples/megatron/configs/MI300X/llama3.1_70B-FP8-pretrain.yaml \
    bash examples/run_slurm_pretrain.sh \
        --micro_batch_size 4 \
        --global_batch_size 256 \
        --recompute_num_layers 80 \
:::
::::

To train Llama 3.1 70B BF16 on 8 nodes, run:

:::: {.highlight-shell .notranslate}
::: highlight
    NNODES=8 \
    EXP=examples/megatron/configs/MI300X/llama3.1_70B-BF16-pretrain.yaml \
    bash examples/run_slurm_pretrain.sh \
        --micro_batch_size 1 \
        --global_batch_size 256 \
        --recompute_num_layers 12
:::
::::
:::::::

::::::: {.model-doc .primus-pyt-megatron-lm-train-llama-2-70b .docutils .container}
Once setup is complete, run the appropriate training command. The following run commands are tailored to Llama 2 70B. See [[Supported models]{.std .std-ref}](#amd-primus-megatron-lm-model-support-v26-2){.reference .internal} to switch to another available model.

To train Llama 2 70B FP8 on 8 nodes, run:

:::: {.highlight-shell .notranslate}
::: highlight
    # Adjust the training parameters.
    # For example, `global_batch_size: 8 * #single_node_bs` for 8 nodes in this case.
    NNODES=8 \
    EXP=examples/megatron/configs/MI300X/llama2_70B-FP8-pretrain.yaml \
    bash examples/run_slurm_pretrain.sh \
        --micro_batch_size 10 \
        --global_batch_size 640 \
        --recompute_num_layers 80 \
:::
::::

To train Llama 2 70B BF16 on 8 nodes, run:

:::: {.highlight-shell .notranslate}
::: highlight
    NNODES=8 \
    EXP=examples/megatron/configs/MI300X/llama2_70B-BF16-pretrain.yaml \
    bash ./examples/run_slurm_pretrain.sh \
        --micro_batch_size 2 \
        --global_batch_size 1536 \
        --recompute_num_layers 12
:::
::::
:::::::

::::::: {.model-doc .primus-pyt-megatron-lm-train-llama-3-3-70b .docutils .container}
Once setup is complete, run the appropriate training command. The following run commands are tailored to Llama 3.3 70B. See [[Supported models]{.std .std-ref}](#amd-primus-megatron-lm-model-support-v26-2){.reference .internal} to switch to another available model.

To train Llama 3.3 70B FP8 on 8 nodes, run:

:::: {.highlight-shell .notranslate}
::: highlight
    # Adjust the training parameters.
    # For example, `global_batch_size: 8 * #single_node_bs` for 8 nodes in this case
    NNODES=8 \
    EXP=examples/megatron/configs/MI300X/llama3.3_70B-FP8-pretrain.yaml \
    bash examples/run_slurm_pretrain.sh \
        --micro_batch_size 4 \
        --global_batch_size 256 \
        --recompute_num_layers 80 \
:::
::::

To train Llama 3.3 70B BF16 on 8 nodes, run:

:::: {.highlight-shell .notranslate}
::: highlight
    NNODES=8 \
    EXP=examples/megatron/configs/MI300X/llama3.3_70B-BF16-pretrain.yaml \
    bash examples/run_slurm_pretrain.sh \
        --micro_batch_size 1 \
        --global_batch_size 256 \
        --recompute_num_layers 12
:::
::::
:::::::

::::: {.model-doc .primus-pyt-megatron-lm-train-mixtral-8x7b .docutils .container}
Once setup is complete, run the appropriate training command. The following run commands are tailored to Llama 2 70B. See [[Supported models]{.std .std-ref}](#amd-primus-megatron-lm-model-support-v26-2){.reference .internal} to switch to another available model.

To train Mixtral 8x7B BF16 on 8 nodes, run:

:::: {.highlight-shell .notranslate}
::: highlight
    # Adjust the training parameters.
    # For example, `global_batch_size: 8 * #single_node_bs` for 8 nodes in this case
    NNODES=8 \
    EXP=examples/megatron/configs/MI300X/mixtral_8x7B_v0.1-BF16-pretrain.yaml \
    bash examples/run_slurm_pretrain.sh \
        --micro_batch_size 2 \
        --global_batch_size 256
:::
::::
:::::

::::: {.model-doc .primus-pyt-megatron-lm-train-qwen2-5-72b .docutils .container}
Once setup is complete, run the appropriate training command. The following run commands are tailored to Llama 2 70B. See [[Supported models]{.std .std-ref}](#amd-primus-megatron-lm-model-support-v26-2){.reference .internal} to switch to another available model.

To train Qwen2.5 72B FP8 on 8 nodes, run:

:::: {.highlight-shell .notranslate}
::: highlight
    # Adjust the training parameters.
    # For example, `global_batch_size: 8 * #single_node_bs` for 8 nodes in this case
    NNODES=8 \
    EXP=examples/megatron/configs/qwen2.5_72B-FP8-pretrain.yaml \
    bash examples/run_slurm_pretrain.sh \
        --micro_batch_size 8 \
        --global_batch_size 512 \
        --recompute_num_layers 80 \
:::
::::
:::::
:::::::::::::::::::::::::::::::::

::: {#key-options .section}
[]{#amd-primus-megatron-lm-benchmark-test-vars-v26-2}

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
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: {#further-reading .section}
## Further reading[\#](#further-reading "Link to this heading"){.headerlink}

- For an introduction to Primus, see [Primus: A Lightweight, Unified Training Framework for Large Models on AMD GPUs](https://rocm.blogs.amd.com/software-tools-optimization/primus/README.html){.reference .external}.

- To learn more about system settings and management practices to configure your system for AMD Instinct MI300X Series GPUs, see [AMD Instinct MI300X system optimization](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi300x.html){.reference .external}.

- For a list of other ready-made Docker images for AI with ROCm, see [AMD Infinity Hub](https://www.amd.com/en/developer/resources/infinity-hub.html#f-amd_hub_category=AI%20%26%20ML%20Models){.reference .external}.
:::

::: {#previous-versions .section}
## Previous versions[\#](#previous-versions "Link to this heading"){.headerlink}

See [[Megatron-LM training performance testing version history]{.doc}](previous-versions/megatron-lm-history.html){.reference .internal} to find documentation for previous releases of the [`ROCm/megatron-lm`{.docutils .literal .notranslate}]{.pre} Docker image.

This training environment now uses Primus with Megatron as the primary configuration. Limited support for the legacy ROCm Megatron-LM is still available; see the [[Training a model with Megatron-LM on ROCm]{.doc}](megatron-lm.html){.reference .internal} documentation.
:::

::: {.toctree-wrapper .compound}
:::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::: prev-next-area
[](../index.html "previous page"){.left-prev}

::: prev-next-info
previous

Use ROCm for training
:::

[](megatron-lm.html "next page"){.right-next}

::: prev-next-info
next

Training a model with Megatron-LM on ROCm
:::
:::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::: {.bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {.page-toc .tocsection .onthispage}
Contents
:::

- [Supported models](#supported-models){.reference .internal .nav-link}
- [System validation](#system-validation){.reference .internal .nav-link}
- [Environment setup](#environment-setup){.reference .internal .nav-link}
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
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
