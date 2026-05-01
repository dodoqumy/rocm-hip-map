---
title: "Training a model with PyTorch on ROCm"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/training/benchmark-docker/previous-versions/pytorch-training-v25.10.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-01
---

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-content
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-article-container
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
# Training a model with PyTorch on ROCm

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [Supported models](#supported-models){.reference .internal .nav-link}
- [Performance measurements](#performance-measurements){.reference .internal .nav-link}
- [System validation](#system-validation){.reference .internal .nav-link}
- [Run training](#run-training){.reference .internal .nav-link}
  - [Multi-node training](#multi-node-training){.reference .internal .nav-link}
    - [Pre-training](#pre-training){.reference .internal .nav-link}
    - [Fine-tuning](#fine-tuning){.reference .internal .nav-link}
- [Further reading](#further-reading){.reference .internal .nav-link}
- [Previous versions](#previous-versions){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#training-a-model-with-pytorch-on-rocm .section}
# Training a model with PyTorch on ROCm[\#](#training-a-model-with-pytorch-on-rocm "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-04-21
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 43 min read time
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

This documentation does not reflect the latest version of ROCm PyTorch training performance benchmark documentation. See [[Training a model with PyTorch on ROCm]{.doc}](../pytorch-training.html){.reference .internal} for the latest version.
:::

::: {.admonition .note}
Note

For a unified training solution on AMD GPUs with ROCm, the [rocm/pytorch-training](https://hub.docker.com/r/rocm/pytorch-training/){.reference .external} Docker Hub registry will be deprecated soon in favor of [rocm/primus](https://hub.docker.com/r/rocm/primus){.reference .external}. The [`rocm/primus`{.docutils .literal .notranslate}]{.pre} Docker containers will cover PyTorch training ecosystem frameworks, including torchtitan and [[Megatron-LM]{.doc}](../primus-megatron.html){.reference .internal}.

See [[Training a model with Primus and PyTorch]{.doc}](../primus-pytorch.html){.reference .internal} for details.
:::

PyTorch is an open-source machine learning framework that is widely used for model training with GPU-optimized components for transformer-based models. The PyTorch for ROCm training Docker image provides a prebuilt optimized environment for fine-tuning and pretraining a model on AMD Instinct MI325X and MI300X GPUs. It includes the following software components to accelerate training workloads:

::::: {.sd-tab-set .docutils}
rocm/primus:v25.10

:::: {.sd-tab-content .docutils}
::: pst-scrollable-table-container
  Software component   Version
  -------------------- ----------------------------
  ROCm                 7.1.0
  Primus               0.3.0
  Primus Turbo         0.1.1
  PyTorch              2.10.0.dev20251112+rocm7.1
  Python               3.10
  Transformer Engine   2.4.0.dev0+32e2d1d4
  Flash Attention      2.8.3
  hipBLASLt            1.2.0-09ab7153e2
:::
::::
:::::

:::::::::::::::::::::::::::::::::::::::::::::::: {#supported-models .section}
[]{#amd-pytorch-training-model-support-v2510}

## Supported models[\#](#supported-models "Link to this heading"){.headerlink}

The following models are pre-optimized for performance on the AMD Instinct MI355X, MI350X, MI325X, and MI300X GPUs. Some instructions, commands, and training recommendations in this documentation might vary by model -- select one to get started.

:::::::::::::::::::::::::::::::::::::::::::: {#vllm-benchmark-ud-params-picker .container-fluid}
::::::::::::: {.row .gx-0}
::: {.col-2 .me-1 .px-2 .model-param-head}
Model
:::

::::::::::: {.row .col-10 .pe-0}
::: {.col-4 .px-2 .model-param param-k="model-group" param-v="llama" tabindex="0"}
Meta Llama
:::

::: {.col-4 .px-2 .model-param param-k="model-group" param-v="openai" tabindex="0"}
OpenAI
:::

::: {.col-4 .px-2 .model-param param-k="model-group" param-v="deepseek" tabindex="0"}
DeepSeek
:::

::: {.col-4 .px-2 .model-param param-k="model-group" param-v="qwen" tabindex="0"}
Qwen
:::

::: {.col-4 .px-2 .model-param param-k="model-group" param-v="sd" tabindex="0"}
Stable Diffusion
:::

::: {.col-4 .px-2 .model-param param-k="model-group" param-v="flux" tabindex="0"}
Flux
:::

::: {.col-4 .px-2 .model-param param-k="model-group" param-v="ncf" tabindex="0"}
NCF
:::

::: {.col-4 .px-2 .model-param param-k="model-group" param-v="dlrm" tabindex="0"}
DLRM
:::
:::::::::::
:::::::::::::

:::::::::::::::::::::::::::::::: {.row .gx-0 .pt-1}
::: {.col-2 .me-1 .px-2 .model-param-head}
Variant
:::

:::::::::::::::::::::::::::::: {.row .col-10 .pe-0}
::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="pyt_train_llama-4-scout-17b-16e" tabindex="0"}
Llama 4 Scout 17B-16E
:::

::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="pyt_train_llama-3.3-70b" tabindex="0"}
Llama 3.3 70B
:::

::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="pyt_train_llama-3.2-1b" tabindex="0"}
Llama 3.2 1B
:::

::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="pyt_train_llama-3.2-3b" tabindex="0"}
Llama 3.2 3B
:::

::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="pyt_train_llama-3.2-vision-11b" tabindex="0"}
Llama 3.2 Vision 11B
:::

::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="pyt_train_llama-3.2-vision-90b" tabindex="0"}
Llama 3.2 Vision 90B
:::

::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="pyt_train_llama-3.1-8b" tabindex="0"}
Llama 3.1 8B
:::

::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="pyt_train_llama-3.1-70b" tabindex="0"}
Llama 3.1 70B
:::

::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="pyt_train_llama-3.1-405b" tabindex="0"}
Llama 3.1 405B
:::

::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="pyt_train_llama-3-8b" tabindex="0"}
Llama 3 8B
:::

::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="pyt_train_llama-3-70b" tabindex="0"}
Llama 3 70B
:::

::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="pyt_train_llama-2-7b" tabindex="0"}
Llama 2 7B
:::

::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="pyt_train_llama-2-13b" tabindex="0"}
Llama 2 13B
:::

::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="pyt_train_llama-2-70b" tabindex="0"}
Llama 2 70B
:::

::: {.col-6 .px-2 .model-param param-group="openai" param-k="model" param-v="pyt_train_gpt_oss_20b" tabindex="0"}
GPT OSS 20B
:::

::: {.col-6 .px-2 .model-param param-group="openai" param-k="model" param-v="pyt_train_gpt_oss_120b" tabindex="0"}
GPT OSS 120B
:::

::: {.col-6 .px-2 .model-param param-group="deepseek" param-k="model" param-v="primus_pyt_train_deepseek-v2" tabindex="0"}
DeepSeek V2 16B
:::

::: {.col-4 .px-2 .model-param param-group="qwen" param-k="model" param-v="pyt_train_qwen3-8b" tabindex="0"}
Qwen 3 8B
:::

::: {.col-4 .px-2 .model-param param-group="qwen" param-k="model" param-v="pyt_train_qwen3-32b" tabindex="0"}
Qwen 3 32B
:::

::: {.col-4 .px-2 .model-param param-group="qwen" param-k="model" param-v="pyt_train_qwen2.5-32b" tabindex="0"}
Qwen 2.5 32B
:::

::: {.col-4 .px-2 .model-param param-group="qwen" param-k="model" param-v="pyt_train_qwen2.5-72b" tabindex="0"}
Qwen 2.5 72B
:::

::: {.col-4 .px-2 .model-param param-group="qwen" param-k="model" param-v="pyt_train_qwen2-1.5b" tabindex="0"}
Qwen 2 1.5B
:::

::: {.col-4 .px-2 .model-param param-group="qwen" param-k="model" param-v="pyt_train_qwen2-7b" tabindex="0"}
Qwen 2 7B
:::

::: {.col-6 .px-2 .model-param param-group="sd" param-k="model" param-v="pyt_huggingface_stable_diffusion_xl_2k_lora_finetuning" tabindex="0"}
Stable Diffusion XL
:::

::: {.col-6 .px-2 .model-param param-group="flux" param-k="model" param-v="pyt_train_flux" tabindex="0"}
FLUX.1-dev
:::

::: {.col-6 .px-2 .model-param param-group="ncf" param-k="model" param-v="pyt_ncf_training" tabindex="0"}
NCF
:::

::: {.col-6 .px-2 .model-param param-group="dlrm" param-k="model" param-v="pyt_train_dlrm" tabindex="0"}
DLRM v2
:::
::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::

The following table lists supported training modes per model.

[Supported training modes]{.sd-summary-text}[![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jaGV2cm9uLXJpZ2h0IiBoZWlnaHQ9IjEuNWVtIiB2ZXJzaW9uPSIxLjEiIHZpZXdib3g9IjAgMCAyNCAyNCIgd2lkdGg9IjEuNWVtIj48cGF0aCBkPSJNOC43MiAxOC43OGEuNzUuNzUgMCAwIDEgMC0xLjA2TDE0LjQ0IDEyIDguNzIgNi4yOGEuNzUxLjc1MSAwIDAgMSAuMDE4LTEuMDQyLjc1MS43NTEgMCAwIDEgMS4wNDItLjAxOGw2LjI1IDYuMjVhLjc1Ljc1IDAgMCAxIDAgMS4wNmwtNi4yNSA2LjI1YS43NS43NSAwIDAgMS0xLjA2IDBaIiAvPjwvc3ZnPg==){.sd-octicon .sd-octicon-chevron-right}]{.sd-summary-state-marker .sd-summary-chevron-right}

::::: {.sd-summary-content .sd-card-body .docutils}
::: pst-scrollable-table-container
  Model                   Supported training modes
  ----------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Llama 4 Scout 17B-16E   [`finetune_fw`{.docutils .literal .notranslate}]{.pre}, [`finetune_lora`{.docutils .literal .notranslate}]{.pre}
  Llama 3.3 70B           [`finetune_fw`{.docutils .literal .notranslate}]{.pre}, [`finetune_lora`{.docutils .literal .notranslate}]{.pre}, [`finetune_qlora`{.docutils .literal .notranslate}]{.pre}
  Llama 3.2 1B            [`finetune_fw`{.docutils .literal .notranslate}]{.pre}, [`finetune_lora`{.docutils .literal .notranslate}]{.pre}
  Llama 3.2 3B            [`finetune_fw`{.docutils .literal .notranslate}]{.pre}, [`finetune_lora`{.docutils .literal .notranslate}]{.pre}
  Llama 3.2 Vision 11B    [`finetune_fw`{.docutils .literal .notranslate}]{.pre}
  Llama 3.2 Vision 90B    [`finetune_fw`{.docutils .literal .notranslate}]{.pre}
  Llama 3.1 8B            [`pretrain`{.docutils .literal .notranslate}]{.pre}, [`finetune_fw`{.docutils .literal .notranslate}]{.pre}, [`finetune_lora`{.docutils .literal .notranslate}]{.pre}, [`HF_pretrain`{.docutils .literal .notranslate}]{.pre}
  Llama 3.1 70B           [`pretrain`{.docutils .literal .notranslate}]{.pre}, [`finetune_fw`{.docutils .literal .notranslate}]{.pre}, [`finetune_lora`{.docutils .literal .notranslate}]{.pre}
  Llama 3.1 405B          [`finetune_qlora`{.docutils .literal .notranslate}]{.pre}
  Llama 3 8B              [`finetune_fw`{.docutils .literal .notranslate}]{.pre}, [`finetune_lora`{.docutils .literal .notranslate}]{.pre}
  Llama 3 70B             [`finetune_fw`{.docutils .literal .notranslate}]{.pre}, [`finetune_lora`{.docutils .literal .notranslate}]{.pre}
  Llama 2 7B              [`finetune_fw`{.docutils .literal .notranslate}]{.pre}, [`finetune_lora`{.docutils .literal .notranslate}]{.pre}, [`finetune_qlora`{.docutils .literal .notranslate}]{.pre}
  Llama 2 13B             [`finetune_fw`{.docutils .literal .notranslate}]{.pre}, [`finetune_lora`{.docutils .literal .notranslate}]{.pre}
  Llama 2 70B             [`finetune_lora`{.docutils .literal .notranslate}]{.pre}, [`finetune_qlora`{.docutils .literal .notranslate}]{.pre}
  GPT OSS 20B             [`HF_finetune_lora`{.docutils .literal .notranslate}]{.pre}
  GPT OSS 120B            [`HF_finetune_lora`{.docutils .literal .notranslate}]{.pre}
  DeepSeek V2 16B         [`pretrain`{.docutils .literal .notranslate}]{.pre}
  Qwen 3 8B               [`finetune_fw`{.docutils .literal .notranslate}]{.pre}, [`finetune_lora`{.docutils .literal .notranslate}]{.pre}
  Qwen 3 32B              [`finetune_lora`{.docutils .literal .notranslate}]{.pre}
  Qwen 2.5 32B            [`finetune_lora`{.docutils .literal .notranslate}]{.pre}
  Qwen 2.5 72B            [`finetune_lora`{.docutils .literal .notranslate}]{.pre}
  Qwen 2 1.5B             [`finetune_fw`{.docutils .literal .notranslate}]{.pre}, [`finetune_lora`{.docutils .literal .notranslate}]{.pre}
  Qwen 2 7B               [`finetune_fw`{.docutils .literal .notranslate}]{.pre}, [`finetune_lora`{.docutils .literal .notranslate}]{.pre}
  Stable Diffusion XL     [`posttrain`{.docutils .literal .notranslate}]{.pre}
  FLUX.1-dev              [`posttrain`{.docutils .literal .notranslate}]{.pre}
  DLRM v2                 [`pretrain`{.docutils .literal .notranslate}]{.pre}
:::

::: {.admonition .note}
Note

Some model and fine-tuning combinations are not listed. This is because the [upstream torchtune repository](https://github.com/pytorch/torchtune){.reference .external} doesn't provide default YAML configurations for them. For advanced usage, you can create a custom configuration to enable unlisted fine-tuning methods by using an existing file in the [`/workspace/torchtune/recipes/configs`{.docutils .literal .notranslate}]{.pre} directory as a template.
:::
:::::
::::::::::::::::::::::::::::::::::::::::::::::::

:::: {#performance-measurements .section}
[]{#amd-pytorch-training-performance-measurements-v2510}

## Performance measurements[\#](#performance-measurements "Link to this heading"){.headerlink}

To evaluate performance, the [Performance results with AMD ROCm software](https://www.amd.com/en/developer/resources/rocm-hub/dev-ai/performance-results.html#tabs-a8deaeb413-item-21cea50186-tab){.reference .external} page provides reference throughput and latency measurements for training popular AI models.

::: {.admonition .note}
Note

The performance data presented in [Performance results with AMD ROCm software](https://www.amd.com/en/developer/resources/rocm-hub/dev-ai/performance-results.html#tabs-a8deaeb413-item-21cea50186-tab){.reference .external} should not be interpreted as the peak performance achievable by AMD Instinct MI325X and MI300X GPUs or ROCm software.
:::
::::

::: {#system-validation .section}
## System validation[\#](#system-validation "Link to this heading"){.headerlink}

Before running AI workloads, it's important to validate that your AMD hardware is configured correctly and performing optimally.

If you have already validated your system settings, including aspects like NUMA auto-balancing, you can skip this step. Otherwise, complete the procedures in the [[System validation and optimization]{.std .std-ref}](../../../system-setup/prerequisite-system-validation.html#rocm-for-ai-system-optimization){.reference .internal} guide to properly configure your system settings before starting training.

To test for optimal performance, consult the recommended [[System health benchmarks]{.std .std-ref}](../../../system-setup/system-health-check.html#rocm-for-ai-system-health-bench){.reference .internal}. This suite of tests will help you verify and fine-tune your system's configuration.

This Docker image is optimized for specific model configurations outlined below. Performance can vary for other training workloads, as AMD doesn't test configurations and run conditions outside those described.
:::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#run-training .section}
## Run training[\#](#run-training "Link to this heading"){.headerlink}

Once the setup is complete, choose between two options to start benchmarking training:

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

:::::::::::::::::::::::::::::: {.sd-tab-content .docutils}
::: {.model-doc .pyt-train-llama-4-scout-17b-16e .docutils .container}
The following run command is tailored to Llama 4 Scout 17B-16E. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  For example, use this command to run the performance benchmark test on the Llama 4 Scout 17B-16E model using one node with the BF16 data type on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_train_llama-4-scout-17b-16e \
            --keep-model-dir \
            --live-output \
            --timeout 28800
    :::
    ::::

    MAD launches a Docker container with the name [`container_ci-pyt_train_llama-4-scout-17b-16e`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::

::: {.model-doc .pyt-train-llama-3-3-70b .docutils .container}
The following run command is tailored to Llama 3.3 70B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  For example, use this command to run the performance benchmark test on the Llama 3.3 70B model using one node with the BF16 data type on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_train_llama-3.3-70b \
            --keep-model-dir \
            --live-output \
            --timeout 28800
    :::
    ::::

    MAD launches a Docker container with the name [`container_ci-pyt_train_llama-3.3-70b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::

::: {.model-doc .pyt-train-llama-3-2-1b .docutils .container}
The following run command is tailored to Llama 3.2 1B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  For example, use this command to run the performance benchmark test on the Llama 3.2 1B model using one node with the BF16 data type on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_train_llama-3.2-1b \
            --keep-model-dir \
            --live-output \
            --timeout 28800
    :::
    ::::

    MAD launches a Docker container with the name [`container_ci-pyt_train_llama-3.2-1b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::

::: {.model-doc .pyt-train-llama-3-2-3b .docutils .container}
The following run command is tailored to Llama 3.2 3B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  For example, use this command to run the performance benchmark test on the Llama 3.2 3B model using one node with the BF16 data type on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_train_llama-3.2-3b \
            --keep-model-dir \
            --live-output \
            --timeout 28800
    :::
    ::::

    MAD launches a Docker container with the name [`container_ci-pyt_train_llama-3.2-3b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::

::: {.model-doc .pyt-train-llama-3-2-vision-11b .docutils .container}
The following run command is tailored to Llama 3.2 Vision 11B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  For example, use this command to run the performance benchmark test on the Llama 3.2 Vision 11B model using one node with the BF16 data type on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_train_llama-3.2-vision-11b \
            --keep-model-dir \
            --live-output \
            --timeout 28800
    :::
    ::::

    MAD launches a Docker container with the name [`container_ci-pyt_train_llama-3.2-vision-11b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::

::: {.model-doc .pyt-train-llama-3-2-vision-90b .docutils .container}
The following run command is tailored to Llama 3.2 Vision 90B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  For example, use this command to run the performance benchmark test on the Llama 3.2 Vision 90B model using one node with the BF16 data type on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_train_llama-3.2-vision-90b \
            --keep-model-dir \
            --live-output \
            --timeout 28800
    :::
    ::::

    MAD launches a Docker container with the name [`container_ci-pyt_train_llama-3.2-vision-90b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::

::: {.model-doc .pyt-train-llama-3-1-8b .docutils .container}
The following run command is tailored to Llama 3.1 8B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  For example, use this command to run the performance benchmark test on the Llama 3.1 8B model using one node with the BF16 data type on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_train_llama-3.1-8b \
            --keep-model-dir \
            --live-output \
            --timeout 28800
    :::
    ::::

    MAD launches a Docker container with the name [`container_ci-pyt_train_llama-3.1-8b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::

::: {.model-doc .pyt-train-llama-3-1-70b .docutils .container}
The following run command is tailored to Llama 3.1 70B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  For example, use this command to run the performance benchmark test on the Llama 3.1 70B model using one node with the BF16 data type on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_train_llama-3.1-70b \
            --keep-model-dir \
            --live-output \
            --timeout 28800
    :::
    ::::

    MAD launches a Docker container with the name [`container_ci-pyt_train_llama-3.1-70b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::

::: {.model-doc .pyt-train-llama-3-1-405b .docutils .container}
The following run command is tailored to Llama 3.1 405B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  For example, use this command to run the performance benchmark test on the Llama 3.1 405B model using one node with the BF16 data type on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_train_llama-3.1-405b \
            --keep-model-dir \
            --live-output \
            --timeout 28800
    :::
    ::::

    MAD launches a Docker container with the name [`container_ci-pyt_train_llama-3.1-405b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::

::: {.model-doc .pyt-train-llama-3-8b .docutils .container}
The following run command is tailored to Llama 3 8B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  For example, use this command to run the performance benchmark test on the Llama 3 8B model using one node with the BF16 data type on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_train_llama-3-8b \
            --keep-model-dir \
            --live-output \
            --timeout 28800
    :::
    ::::

    MAD launches a Docker container with the name [`container_ci-pyt_train_llama-3-8b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::

::: {.model-doc .pyt-train-llama-3-70b .docutils .container}
The following run command is tailored to Llama 3 70B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  For example, use this command to run the performance benchmark test on the Llama 3 70B model using one node with the BF16 data type on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_train_llama-3-70b \
            --keep-model-dir \
            --live-output \
            --timeout 28800
    :::
    ::::

    MAD launches a Docker container with the name [`container_ci-pyt_train_llama-3-70b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::

::: {.model-doc .pyt-train-llama-2-7b .docutils .container}
The following run command is tailored to Llama 2 7B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  For example, use this command to run the performance benchmark test on the Llama 2 7B model using one node with the BF16 data type on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_train_llama-2-7b \
            --keep-model-dir \
            --live-output \
            --timeout 28800
    :::
    ::::

    MAD launches a Docker container with the name [`container_ci-pyt_train_llama-2-7b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::

::: {.model-doc .pyt-train-llama-2-13b .docutils .container}
The following run command is tailored to Llama 2 13B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  For example, use this command to run the performance benchmark test on the Llama 2 13B model using one node with the BF16 data type on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_train_llama-2-13b \
            --keep-model-dir \
            --live-output \
            --timeout 28800
    :::
    ::::

    MAD launches a Docker container with the name [`container_ci-pyt_train_llama-2-13b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::

::: {.model-doc .pyt-train-llama-2-70b .docutils .container}
The following run command is tailored to Llama 2 70B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  For example, use this command to run the performance benchmark test on the Llama 2 70B model using one node with the BF16 data type on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_train_llama-2-70b \
            --keep-model-dir \
            --live-output \
            --timeout 28800
    :::
    ::::

    MAD launches a Docker container with the name [`container_ci-pyt_train_llama-2-70b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::

::: {.model-doc .pyt-train-gpt-oss-20b .docutils .container}
The following run command is tailored to GPT OSS 20B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  For example, use this command to run the performance benchmark test on the GPT OSS 20B model using one node with the BF16 data type on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_train_gpt_oss_20b \
            --keep-model-dir \
            --live-output \
            --timeout 28800
    :::
    ::::

    MAD launches a Docker container with the name [`container_ci-pyt_train_gpt_oss_20b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::

::: {.model-doc .pyt-train-gpt-oss-120b .docutils .container}
The following run command is tailored to GPT OSS 120B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  For example, use this command to run the performance benchmark test on the GPT OSS 120B model using one node with the BF16 data type on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_train_gpt_oss_120b \
            --keep-model-dir \
            --live-output \
            --timeout 28800
    :::
    ::::

    MAD launches a Docker container with the name [`container_ci-pyt_train_gpt_oss_120b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::

::: {.model-doc .primus-pyt-train-deepseek-v2 .docutils .container}
The following run command is tailored to DeepSeek V2 16B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  For example, use this command to run the performance benchmark test on the DeepSeek V2 16B model using one node with the BF16 data type on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags primus_pyt_train_deepseek-v2 \
            --keep-model-dir \
            --live-output \
            --timeout 28800
    :::
    ::::

    MAD launches a Docker container with the name [`container_ci-primus_pyt_train_deepseek-v2`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::

::: {.model-doc .pyt-train-qwen3-8b .docutils .container}
The following run command is tailored to Qwen 3 8B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  For example, use this command to run the performance benchmark test on the Qwen 3 8B model using one node with the BF16 data type on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_train_qwen3-8b \
            --keep-model-dir \
            --live-output \
            --timeout 28800
    :::
    ::::

    MAD launches a Docker container with the name [`container_ci-pyt_train_qwen3-8b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::

::: {.model-doc .pyt-train-qwen3-32b .docutils .container}
The following run command is tailored to Qwen 3 32B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  For example, use this command to run the performance benchmark test on the Qwen 3 32B model using one node with the BF16 data type on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_train_qwen3-32b \
            --keep-model-dir \
            --live-output \
            --timeout 28800
    :::
    ::::

    MAD launches a Docker container with the name [`container_ci-pyt_train_qwen3-32b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::

::: {.model-doc .pyt-train-qwen2-5-32b .docutils .container}
The following run command is tailored to Qwen 2.5 32B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  For example, use this command to run the performance benchmark test on the Qwen 2.5 32B model using one node with the BF16 data type on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_train_qwen2.5-32b \
            --keep-model-dir \
            --live-output \
            --timeout 28800
    :::
    ::::

    MAD launches a Docker container with the name [`container_ci-pyt_train_qwen2.5-32b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::

::: {.model-doc .pyt-train-qwen2-5-72b .docutils .container}
The following run command is tailored to Qwen 2.5 72B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  For example, use this command to run the performance benchmark test on the Qwen 2.5 72B model using one node with the BF16 data type on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_train_qwen2.5-72b \
            --keep-model-dir \
            --live-output \
            --timeout 28800
    :::
    ::::

    MAD launches a Docker container with the name [`container_ci-pyt_train_qwen2.5-72b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::

::: {.model-doc .pyt-train-qwen2-1-5b .docutils .container}
The following run command is tailored to Qwen 2 1.5B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  For example, use this command to run the performance benchmark test on the Qwen 2 1.5B model using one node with the BF16 data type on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_train_qwen2-1.5b \
            --keep-model-dir \
            --live-output \
            --timeout 28800
    :::
    ::::

    MAD launches a Docker container with the name [`container_ci-pyt_train_qwen2-1.5b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::

::: {.model-doc .pyt-train-qwen2-7b .docutils .container}
The following run command is tailored to Qwen 2 7B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  For example, use this command to run the performance benchmark test on the Qwen 2 7B model using one node with the BF16 data type on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_train_qwen2-7b \
            --keep-model-dir \
            --live-output \
            --timeout 28800
    :::
    ::::

    MAD launches a Docker container with the name [`container_ci-pyt_train_qwen2-7b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::

::: {.model-doc .pyt-huggingface-stable-diffusion-xl-2k-lora-finetuning .docutils .container}
The following run command is tailored to Stable Diffusion XL. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  For example, use this command to run the performance benchmark test on the Stable Diffusion XL model using one node with the BF16 data type on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_huggingface_stable_diffusion_xl_2k_lora_finetuning \
            --keep-model-dir \
            --live-output \
            --timeout 28800
    :::
    ::::

    MAD launches a Docker container with the name [`container_ci-pyt_huggingface_stable_diffusion_xl_2k_lora_finetuning`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::

::: {.model-doc .pyt-train-flux .docutils .container}
The following run command is tailored to FLUX.1-dev. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  For example, use this command to run the performance benchmark test on the FLUX.1-dev model using one node with the BF16 data type on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_train_flux \
            --keep-model-dir \
            --live-output \
            --timeout 28800
    :::
    ::::

    MAD launches a Docker container with the name [`container_ci-pyt_train_flux`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::

::: {.model-doc .pyt-ncf-training .docutils .container}
The following run command is tailored to NCF. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  For example, use this command to run the performance benchmark test on the NCF model using one node with the FP32 data type on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_ncf_training \
            --keep-model-dir \
            --live-output \
            --timeout 28800
    :::
    ::::

    MAD launches a Docker container with the name [`container_ci-pyt_ncf_training`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::

::: {.model-doc .pyt-train-dlrm .docutils .container}
The following run command is tailored to DLRM v2. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  For example, use this command to run the performance benchmark test on the DLRM v2 model using one node with the data type on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_train_dlrm \
            --keep-model-dir \
            --live-output \
            --timeout 28800
    :::
    ::::

    MAD launches a Docker container with the name [`container_ci-pyt_train_dlrm`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::
::::::::::::::::::::::::::::::

Standalone benchmarking

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {.sd-tab-content .docutils}
::: {.model-doc .pyt-train-llama-4-scout-17b-16e .docutils .container}
The following commands are tailored to Llama 4 Scout 17B-16E. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.
:::

::: {.model-doc .pyt-train-llama-3-3-70b .docutils .container}
The following commands are tailored to Llama 3.3 70B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.
:::

::: {.model-doc .pyt-train-llama-3-2-1b .docutils .container}
The following commands are tailored to Llama 3.2 1B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.
:::

::: {.model-doc .pyt-train-llama-3-2-3b .docutils .container}
The following commands are tailored to Llama 3.2 3B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.
:::

::: {.model-doc .pyt-train-llama-3-2-vision-11b .docutils .container}
The following commands are tailored to Llama 3.2 Vision 11B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.
:::

::: {.model-doc .pyt-train-llama-3-2-vision-90b .docutils .container}
The following commands are tailored to Llama 3.2 Vision 90B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.
:::

::: {.model-doc .pyt-train-llama-3-1-8b .docutils .container}
The following commands are tailored to Llama 3.1 8B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.
:::

::: {.model-doc .pyt-train-llama-3-1-70b .docutils .container}
The following commands are tailored to Llama 3.1 70B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.
:::

::: {.model-doc .pyt-train-llama-3-1-405b .docutils .container}
The following commands are tailored to Llama 3.1 405B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.
:::

::: {.model-doc .pyt-train-llama-3-8b .docutils .container}
The following commands are tailored to Llama 3 8B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.
:::

::: {.model-doc .pyt-train-llama-3-70b .docutils .container}
The following commands are tailored to Llama 3 70B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.
:::

::: {.model-doc .pyt-train-llama-2-7b .docutils .container}
The following commands are tailored to Llama 2 7B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.
:::

::: {.model-doc .pyt-train-llama-2-13b .docutils .container}
The following commands are tailored to Llama 2 13B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.
:::

::: {.model-doc .pyt-train-llama-2-70b .docutils .container}
The following commands are tailored to Llama 2 70B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.
:::

::: {.model-doc .pyt-train-gpt-oss-20b .docutils .container}
The following commands are tailored to GPT OSS 20B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.
:::

::: {.model-doc .pyt-train-gpt-oss-120b .docutils .container}
The following commands are tailored to GPT OSS 120B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.
:::

::: {.model-doc .primus-pyt-train-deepseek-v2 .docutils .container}
The following commands are tailored to DeepSeek V2 16B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.
:::

::: {.model-doc .pyt-train-qwen3-8b .docutils .container}
The following commands are tailored to Qwen 3 8B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.
:::

::: {.model-doc .pyt-train-qwen3-32b .docutils .container}
The following commands are tailored to Qwen 3 32B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.
:::

::: {.model-doc .pyt-train-qwen2-5-32b .docutils .container}
The following commands are tailored to Qwen 2.5 32B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.
:::

::: {.model-doc .pyt-train-qwen2-5-72b .docutils .container}
The following commands are tailored to Qwen 2.5 72B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.
:::

::: {.model-doc .pyt-train-qwen2-1-5b .docutils .container}
The following commands are tailored to Qwen 2 1.5B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.
:::

::: {.model-doc .pyt-train-qwen2-7b .docutils .container}
The following commands are tailored to Qwen 2 7B. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.
:::

::: {.model-doc .pyt-huggingface-stable-diffusion-xl-2k-lora-finetuning .docutils .container}
The following commands are tailored to Stable Diffusion XL. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.
:::

::: {.model-doc .pyt-train-flux .docutils .container}
The following commands are tailored to FLUX.1-dev. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.
:::

::: {.model-doc .pyt-ncf-training .docutils .container}
The following commands are tailored to NCF. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.
:::

::: {.model-doc .pyt-train-dlrm .docutils .container}
The following commands are tailored to DLRM v2. See [[Supported models]{.std .std-ref}](#amd-pytorch-training-model-support-v2510){.reference .internal} to switch to another available model.
:::

Download the Docker image and required packages

1.  Use the following command to pull the Docker image from Docker Hub.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker pull rocm/primus:v25.10
    :::
    ::::

2.  Launch the Docker container.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker run -it \
            --device /dev/dri \
            --device /dev/kfd \
            --network host \
            --ipc host \
            --group-add video \
            --cap-add SYS_PTRACE \
            --security-opt seccomp=unconfined \
            --privileged \
            -v $HOME:$HOME \
            -v $HOME/.ssh:/root/.ssh \
            --shm-size 64G \
            --name training_env \
            rocm/primus:v25.10
    :::
    ::::

    Use these commands if you exit the [`training_env`{.docutils .literal .notranslate}]{.pre} container and need to return to it.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker start training_env
        docker exec -it training_env bash
    :::
    ::::

3.  In the Docker container, clone the [ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external} repository and navigate to the benchmark scripts directory [`/workspace/MAD/scripts/pytorch_train`{.docutils .literal .notranslate}]{.pre}.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD/scripts/pytorch_train
    :::
    ::::

Prepare training datasets and dependencies

1.  The following benchmarking examples require downloading models and datasets from Hugging Face. To ensure successful access to gated repos, set your [`HF_TOKEN`{.docutils .literal .notranslate}]{.pre}.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export HF_TOKEN=$your_personal_hugging_face_access_token
    :::
    ::::

2.  Run the setup script to install libraries and datasets needed for benchmarking.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        ./pytorch_benchmark_setup.sh
    :::
    ::::

    :::: {.model-doc .pyt-train-llama-3-1-8b .docutils .container}
    [`pytorch_benchmark_setup.sh`{.docutils .literal .notranslate}]{.pre} installs the following libraries for Llama 3.1 8B:

    ::: pst-scrollable-table-container
      Library                                                 Reference
      ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------
      [`accelerate`{.docutils .literal .notranslate}]{.pre}   [Hugging Face Accelerate](https://huggingface.co/docs/accelerate/en/index){.reference .external}
      [`datasets`{.docutils .literal .notranslate}]{.pre}     [Hugging Face Datasets](https://huggingface.co/docs/datasets/v3.2.0/en/index){.reference .external} 3.2.0
    :::
    ::::

    :::: {.model-doc .pyt-train-llama-3-1-70b .docutils .container}
    [`pytorch_benchmark_setup.sh`{.docutils .literal .notranslate}]{.pre} installs the following libraries for Llama 3.1 70B:

    ::: pst-scrollable-table-container
      Library                                                    Reference
      ---------------------------------------------------------- -----------------------------------------------------------------------------------------------------------
      [`datasets`{.docutils .literal .notranslate}]{.pre}        [Hugging Face Datasets](https://huggingface.co/docs/datasets/v3.2.0/en/index){.reference .external} 3.2.0
      [`torchdata`{.docutils .literal .notranslate}]{.pre}       [TorchData](https://meta-pytorch.org/data/beta/index.html#torchdata){.reference .external}
      [`tomli`{.docutils .literal .notranslate}]{.pre}           [Tomli](https://pypi.org/project/tomli/){.reference .external}
      [`tiktoken`{.docutils .literal .notranslate}]{.pre}        [tiktoken](https://github.com/openai/tiktoken){.reference .external}
      [`blobfile`{.docutils .literal .notranslate}]{.pre}        [blobfile](https://pypi.org/project/blobfile/){.reference .external}
      [`tabulate`{.docutils .literal .notranslate}]{.pre}        [tabulate](https://pypi.org/project/tabulate/){.reference .external}
      [`wandb`{.docutils .literal .notranslate}]{.pre}           [Weights & Biases](https://github.com/wandb/wandb){.reference .external}
      [`sentencepiece`{.docutils .literal .notranslate}]{.pre}   [SentencePiece](https://github.com/google/sentencepiece){.reference .external} 0.2.0
      [`tensorboard`{.docutils .literal .notranslate}]{.pre}     [TensorBoard](https://www.tensorflow.org/tensorboard){.reference .external} 2.18.0
    :::
    ::::

    :::: {.model-doc .pyt-train-flux .docutils .container}
    [`pytorch_benchmark_setup.sh`{.docutils .literal .notranslate}]{.pre} installs the following libraries for FLUX:

    ::: pst-scrollable-table-container
      Library                                                             Reference
      ------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------
      [`accelerate`{.docutils .literal .notranslate}]{.pre}               [Hugging Face Accelerate](https://huggingface.co/docs/accelerate/en/index){.reference .external}
      [`datasets`{.docutils .literal .notranslate}]{.pre}                 [Hugging Face Datasets](https://huggingface.co/docs/datasets/v3.2.0/en/index){.reference .external} 3.2.0
      [`sentencepiece`{.docutils .literal .notranslate}]{.pre}            [SentencePiece](https://github.com/google/sentencepiece){.reference .external} 0.2.0
      [`tensorboard`{.docutils .literal .notranslate}]{.pre}              [TensorBoard](https://www.tensorflow.org/tensorboard){.reference .external} 2.18.0
      [`csvkit`{.docutils .literal .notranslate}]{.pre}                   [csvkit](https://csvkit.readthedocs.io/en/latest/){.reference .external} 2.0.1
      [`deepspeed`{.docutils .literal .notranslate}]{.pre}                [DeepSpeed](https://github.com/deepspeedai/DeepSpeed){.reference .external} 0.16.2
      [`diffusers`{.docutils .literal .notranslate}]{.pre}                [Hugging Face Diffusers](https://huggingface.co/docs/diffusers/en/index){.reference .external} 0.31.0
      [`GitPython`{.docutils .literal .notranslate}]{.pre}                [GitPython](https://github.com/gitpython-developers/GitPython){.reference .external} 3.1.44
      [`opencv-python-headless`{.docutils .literal .notranslate}]{.pre}   [opencv-python-headless](https://pypi.org/project/opencv-python-headless/){.reference .external} 4.10.0.84
      [`peft`{.docutils .literal .notranslate}]{.pre}                     [PEFT](https://huggingface.co/docs/peft/en/index){.reference .external} 0.14.0
      [`protobuf`{.docutils .literal .notranslate}]{.pre}                 [Protocol Buffers](https://github.com/protocolbuffers/protobuf){.reference .external} 5.29.2
      [`pytest`{.docutils .literal .notranslate}]{.pre}                   [PyTest](https://docs.pytest.org/en/stable/){.reference .external} 8.3.4
      [`python-dotenv`{.docutils .literal .notranslate}]{.pre}            [python-dotenv](https://pypi.org/project/python-dotenv/){.reference .external} 1.0.1
      [`seaborn`{.docutils .literal .notranslate}]{.pre}                  [Seaborn](https://seaborn.pydata.org/){.reference .external} 0.13.2
      [`transformers`{.docutils .literal .notranslate}]{.pre}             [Transformers](https://huggingface.co/docs/transformers/en/index){.reference .external} 4.47.0
    :::
    ::::

    [`pytorch_benchmark_setup.sh`{.docutils .literal .notranslate}]{.pre} downloads the following datasets from Hugging Face:

    - [frank-chieng/chinese_architecture_siheyuan](https://huggingface.co/datasets/frank-chieng/chinese_architecture_siheyuan){.reference .external}

:::::: {.model-doc .pyt-train-llama-4-scout-17b-16e .docutils .container}
Fine-tuning

To start the fine-tuning benchmark, use the following command with the appropriate options. See the following list of options and their descriptions. See [[supported training modes]{.std .std-ref}](#amd-pytorch-training-supported-training-modes-v2510){.reference .internal}.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t $training_mode \
        -m Llama-4-17B_16E \
        -p $datatype \
        -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                                                             Description
  ------------------------------------------------------------- --------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`finetune_fw`{.docutils .literal .notranslate}]{.pre}                                              Full weight fine-tuning (BF16 and FP8 supported).
                                                                [`finetune_lora`{.docutils .literal .notranslate}]{.pre}                                            LoRA fine-tuning (BF16 supported).
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre} or [`FP8`{.docutils .literal .notranslate}]{.pre}   All models support BF16. FP8 is only available for full weight fine-tuning.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Between 2048 and 16384.                                                                             Sequence length for the language model.
:::
::::::

:::::: {.model-doc .pyt-train-llama-3-3-70b .docutils .container}
Fine-tuning

To start the fine-tuning benchmark, use the following command with the appropriate options. See the following list of options and their descriptions. See [[supported training modes]{.std .std-ref}](#amd-pytorch-training-supported-training-modes-v2510){.reference .internal}.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t $training_mode \
        -m Llama-3.3-70B \
        -p $datatype \
        -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                                                             Description
  ------------------------------------------------------------- --------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`finetune_fw`{.docutils .literal .notranslate}]{.pre}                                              Full weight fine-tuning (BF16 and FP8 supported).
                                                                [`finetune_lora`{.docutils .literal .notranslate}]{.pre}                                            LoRA fine-tuning (BF16 supported).
                                                                [`finetune_qlora`{.docutils .literal .notranslate}]{.pre}                                           QLoRA fine-tuning (BF16 supported).
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre} or [`FP8`{.docutils .literal .notranslate}]{.pre}   All models support BF16. FP8 is only available for full weight fine-tuning.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Between 2048 and 16384.                                                                             Sequence length for the language model.
:::
::::::

:::::: {.model-doc .pyt-train-llama-3-2-1b .docutils .container}
Fine-tuning

To start the fine-tuning benchmark, use the following command with the appropriate options. See the following list of options and their descriptions. See [[supported training modes]{.std .std-ref}](#amd-pytorch-training-supported-training-modes-v2510){.reference .internal}.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t $training_mode \
        -m Llama-3.2-1B \
        -p $datatype \
        -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                                                             Description
  ------------------------------------------------------------- --------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`finetune_fw`{.docutils .literal .notranslate}]{.pre}                                              Full weight fine-tuning (BF16 and FP8 supported).
                                                                [`finetune_lora`{.docutils .literal .notranslate}]{.pre}                                            LoRA fine-tuning (BF16 supported).
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre} or [`FP8`{.docutils .literal .notranslate}]{.pre}   All models support BF16. FP8 is only available for full weight fine-tuning.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Between 2048 and 16384.                                                                             Sequence length for the language model.
:::
::::::

:::::: {.model-doc .pyt-train-llama-3-2-3b .docutils .container}
Fine-tuning

To start the fine-tuning benchmark, use the following command with the appropriate options. See the following list of options and their descriptions. See [[supported training modes]{.std .std-ref}](#amd-pytorch-training-supported-training-modes-v2510){.reference .internal}.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t $training_mode \
        -m Llama-3.2-3B \
        -p $datatype \
        -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                                                             Description
  ------------------------------------------------------------- --------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`finetune_fw`{.docutils .literal .notranslate}]{.pre}                                              Full weight fine-tuning (BF16 and FP8 supported).
                                                                [`finetune_lora`{.docutils .literal .notranslate}]{.pre}                                            LoRA fine-tuning (BF16 supported).
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre} or [`FP8`{.docutils .literal .notranslate}]{.pre}   All models support BF16. FP8 is only available for full weight fine-tuning.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Between 2048 and 16384.                                                                             Sequence length for the language model.
:::
::::::

:::::: {.model-doc .pyt-train-llama-3-2-vision-11b .docutils .container}
Fine-tuning

To start the fine-tuning benchmark, use the following command with the appropriate options. See the following list of options and their descriptions. See [[supported training modes]{.std .std-ref}](#amd-pytorch-training-supported-training-modes-v2510){.reference .internal}.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t $training_mode \
        -m Llama-3.2-Vision-11B \
        -p $datatype \
        -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                                                             Description
  ------------------------------------------------------------- --------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`finetune_fw`{.docutils .literal .notranslate}]{.pre}                                              Full weight fine-tuning (BF16 and FP8 supported).
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre} or [`FP8`{.docutils .literal .notranslate}]{.pre}   All models support BF16. FP8 is only available for full weight fine-tuning.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Between 2048 and 16384.                                                                             Sequence length for the language model.
:::
::::::

::::::::: {.model-doc .pyt-train-llama-3-2-vision-90b .docutils .container}
Fine-tuning

To start the fine-tuning benchmark, use the following command with the appropriate options. See the following list of options and their descriptions. See [[supported training modes]{.std .std-ref}](#amd-pytorch-training-supported-training-modes-v2510){.reference .internal}.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t $training_mode \
        -m Llama-3.2-Vision-90B \
        -p $datatype \
        -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                                                             Description
  ------------------------------------------------------------- --------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`finetune_fw`{.docutils .literal .notranslate}]{.pre}                                              Full weight fine-tuning (BF16 and FP8 supported).
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre} or [`FP8`{.docutils .literal .notranslate}]{.pre}   All models support BF16. FP8 is only available for full weight fine-tuning.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Between 2048 and 16384.                                                                             Sequence length for the language model.
:::

::::: {.admonition .note}
Note

For LoRA and QLoRA support with vision models (Llama 3.2 11B and 90B), use the following torchtune commit for compatibility:

:::: {.highlight-shell .notranslate}
::: highlight
    git checkout 48192e23188b1fc524dd6d127725ceb2348e7f0e
:::
::::
:::::
:::::::::

:::::: {.model-doc .pyt-train-llama-3-1-8b .docutils .container}
Pretraining

To start the pre-training benchmark, use the following command with the appropriate options. See the following list of options and their descriptions.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t $training_mode \
        -m Llama-3.1-8B \
        -p $datatype \
        -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                                                             Description
  ------------------------------------------------------------- --------------------------------------------------------------------------------------------------- -----------------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`pretrain`{.docutils .literal .notranslate}]{.pre}                                                 Benchmark pre-training.
                                                                [`HF_pretrain`{.docutils .literal .notranslate}]{.pre}                                              Llama 3.1 8B pre-training with FP8 precision.
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre} or [`FP8`{.docutils .literal .notranslate}]{.pre}   Only Llama 3.1 8B supports FP8 precision.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Sequence length for the language model.                                                             Between 2048 and 8192. 8192 by default.
:::
::::::

:::::: {.model-doc .pyt-train-llama-3-1-8b .docutils .container}
Fine-tuning

To start the fine-tuning benchmark, use the following command with the appropriate options. See the following list of options and their descriptions. See [[supported training modes]{.std .std-ref}](#amd-pytorch-training-supported-training-modes-v2510){.reference .internal}.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t $training_mode \
        -m Llama-3.1-8B \
        -p $datatype \
        -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                                                             Description
  ------------------------------------------------------------- --------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`finetune_fw`{.docutils .literal .notranslate}]{.pre}                                              Full weight fine-tuning (BF16 and FP8 supported).
                                                                [`finetune_lora`{.docutils .literal .notranslate}]{.pre}                                            LoRA fine-tuning (BF16 supported).
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre} or [`FP8`{.docutils .literal .notranslate}]{.pre}   All models support BF16. FP8 is only available for full weight fine-tuning.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Between 2048 and 16384.                                                                             Sequence length for the language model.
:::
::::::

:::::: {.model-doc .pyt-train-llama-3-1-70b .docutils .container}
Pretraining

To start the pre-training benchmark, use the following command with the appropriate options. See the following list of options and their descriptions.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t pretrain \
        -m Llama-3.1-70B \
        -p $datatype \
        -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                               Description
  ------------------------------------------------------------- ----------------------------------------------------- -------------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`pretrain`{.docutils .literal .notranslate}]{.pre}   Benchmark pre-training.
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre}       Only Llama 3.1 8B supports FP8 precision.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Sequence length for the language model.               Between 2048 and 8192. 8192 by default.
:::
::::::

:::::: {.model-doc .pyt-train-llama-3-1-70b .docutils .container}
Fine-tuning

To start the fine-tuning benchmark, use the following command with the appropriate options. See the following list of options and their descriptions. See [[supported training modes]{.std .std-ref}](#amd-pytorch-training-supported-training-modes-v2510){.reference .internal}.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t $training_mode \
        -m Llama-3.1-70B \
        -p $datatype \
        -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                                                             Description
  ------------------------------------------------------------- --------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`finetune_fw`{.docutils .literal .notranslate}]{.pre}                                              Full weight fine-tuning (BF16 and FP8 supported).
                                                                [`finetune_lora`{.docutils .literal .notranslate}]{.pre}                                            LoRA fine-tuning (BF16 supported).
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre} or [`FP8`{.docutils .literal .notranslate}]{.pre}   All models support BF16. FP8 is only available for full weight fine-tuning.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Between 2048 and 16384.                                                                             Sequence length for the language model.
:::
::::::

:::::: {.model-doc .pyt-train-llama-3-1-405b .docutils .container}
Fine-tuning

To start the fine-tuning benchmark, use the following command with the appropriate options. See the following list of options and their descriptions. See [[supported training modes]{.std .std-ref}](#amd-pytorch-training-supported-training-modes-v2510){.reference .internal}.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t $training_mode \
        -m Llama-3.1-405B \
        -p $datatype \
        -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                     Description
  ------------------------------------------------------------- ----------------------------------------------------------- -----------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`finetune_qlora`{.docutils .literal .notranslate}]{.pre}   QLoRA fine-tuning (BF16 supported).
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre}             All models support BF16.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Between 2048 and 16384.                                     Sequence length for the language model.
:::
::::::

:::::: {.model-doc .pyt-train-llama-3-8b .docutils .container}
Fine-tuning

To start the fine-tuning benchmark, use the following command with the appropriate options. See the following list of options and their descriptions. See [[supported training modes]{.std .std-ref}](#amd-pytorch-training-supported-training-modes-v2510){.reference .internal}.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t $training_mode \
        -m Llama-3-8B \
        -p $datatype \
        -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                                                             Description
  ------------------------------------------------------------- --------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`finetune_fw`{.docutils .literal .notranslate}]{.pre}                                              Full weight fine-tuning (BF16 and FP8 supported).
                                                                [`finetune_lora`{.docutils .literal .notranslate}]{.pre}                                            LoRA fine-tuning (BF16 supported).
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre} or [`FP8`{.docutils .literal .notranslate}]{.pre}   All models support BF16. FP8 is only available for full weight fine-tuning.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Between 2048 and 16384.                                                                             Sequence length for the language model.
:::
::::::

:::::: {.model-doc .pyt-train-llama-3-70b .docutils .container}
Fine-tuning

To start the fine-tuning benchmark, use the following command with the appropriate options. See the following list of options and their descriptions. See [[supported training modes]{.std .std-ref}](#amd-pytorch-training-supported-training-modes-v2510){.reference .internal}.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t $training_mode \
        -m Llama-3-70B \
        -p $datatype \
        -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                                                             Description
  ------------------------------------------------------------- --------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`finetune_fw`{.docutils .literal .notranslate}]{.pre}                                              Full weight fine-tuning (BF16 and FP8 supported).
                                                                [`finetune_lora`{.docutils .literal .notranslate}]{.pre}                                            LoRA fine-tuning (BF16 supported).
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre} or [`FP8`{.docutils .literal .notranslate}]{.pre}   All models support BF16. FP8 is only available for full weight fine-tuning.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Between 2048 and 16384.                                                                             Sequence length for the language model.
:::
::::::

::::::: {.model-doc .pyt-train-llama-2-7b .docutils .container}
Fine-tuning

To start the fine-tuning benchmark, use the following command with the appropriate options. See the following list of options and their descriptions. See [[supported training modes]{.std .std-ref}](#amd-pytorch-training-supported-training-modes-v2510){.reference .internal}.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t $training_mode \
        -m Llama-2-7B \
        -p $datatype \
        -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                                                             Description
  ------------------------------------------------------------- --------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`finetune_fw`{.docutils .literal .notranslate}]{.pre}                                              Full weight fine-tuning (BF16 and FP8 supported).
                                                                [`finetune_lora`{.docutils .literal .notranslate}]{.pre}                                            LoRA fine-tuning (BF16 supported).
                                                                [`finetune_qlora`{.docutils .literal .notranslate}]{.pre}                                           QLoRA fine-tuning (BF16 supported).
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre} or [`FP8`{.docutils .literal .notranslate}]{.pre}   All models support BF16. FP8 is only available for full weight fine-tuning.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Between 2048 and 16384.                                                                             Sequence length for the language model.
:::

::: {.admonition .note}
Note

You might encounter the following error with Llama 2: [`ValueError:`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`seq_len`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`(16384)`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`of`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`input`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`tensor`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`should`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`be`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`smaller`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`than`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`max_seq_len`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`(4096)`{.docutils .literal .notranslate}]{.pre}. This error indicates that an input sequence is longer than the model's maximum context window.

Ensure your tokenized input does not exceed the model's [`max_seq_len`{.docutils .literal .notranslate}]{.pre} (4096 tokens in this case). You can resolve this by truncating the input or splitting it into smaller chunks before passing it to the model.

Note on reproducibility: The results in this guide are based on commit [`b4c98ac`{.docutils .literal .notranslate}]{.pre} from the upstream [pytorch/torchtune](https://github.com/pytorch/torchtune){.github .reference .external} repository. For the latest updates, you can use the main branch.
:::
:::::::

::::::: {.model-doc .pyt-train-llama-2-13b .docutils .container}
Fine-tuning

To start the fine-tuning benchmark, use the following command with the appropriate options. See the following list of options and their descriptions. See [[supported training modes]{.std .std-ref}](#amd-pytorch-training-supported-training-modes-v2510){.reference .internal}.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t $training_mode \
        -m Llama-2-13B \
        -p $datatype \
        -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                                                             Description
  ------------------------------------------------------------- --------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`finetune_fw`{.docutils .literal .notranslate}]{.pre}                                              Full weight fine-tuning (BF16 and FP8 supported).
                                                                [`finetune_lora`{.docutils .literal .notranslate}]{.pre}                                            LoRA fine-tuning (BF16 supported).
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre} or [`FP8`{.docutils .literal .notranslate}]{.pre}   All models support BF16. FP8 is only available for full weight fine-tuning.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Between 2048 and 16384.                                                                             Sequence length for the language model.
:::

::: {.admonition .note}
Note

You might encounter the following error with Llama 2: [`ValueError:`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`seq_len`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`(16384)`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`of`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`input`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`tensor`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`should`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`be`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`smaller`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`than`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`max_seq_len`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`(4096)`{.docutils .literal .notranslate}]{.pre}. This error indicates that an input sequence is longer than the model's maximum context window.

Ensure your tokenized input does not exceed the model's [`max_seq_len`{.docutils .literal .notranslate}]{.pre} (4096 tokens in this case). You can resolve this by truncating the input or splitting it into smaller chunks before passing it to the model.

Note on reproducibility: The results in this guide are based on commit [`b4c98ac`{.docutils .literal .notranslate}]{.pre} from the upstream [pytorch/torchtune](https://github.com/pytorch/torchtune){.github .reference .external} repository. For the latest updates, you can use the main branch.
:::
:::::::

::::::: {.model-doc .pyt-train-llama-2-70b .docutils .container}
Fine-tuning

To start the fine-tuning benchmark, use the following command with the appropriate options. See the following list of options and their descriptions. See [[supported training modes]{.std .std-ref}](#amd-pytorch-training-supported-training-modes-v2510){.reference .internal}.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t $training_mode \
        -m Llama-2-70B \
        -p $datatype \
        -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                     Description
  ------------------------------------------------------------- ----------------------------------------------------------- -----------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`finetune_lora`{.docutils .literal .notranslate}]{.pre}    LoRA fine-tuning (BF16 supported).
                                                                [`finetune_qlora`{.docutils .literal .notranslate}]{.pre}   QLoRA fine-tuning (BF16 supported).
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre}             All models support BF16.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Between 2048 and 16384.                                     Sequence length for the language model.
:::

::: {.admonition .note}
Note

You might encounter the following error with Llama 2: [`ValueError:`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`seq_len`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`(16384)`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`of`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`input`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`tensor`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`should`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`be`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`smaller`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`than`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`max_seq_len`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`(4096)`{.docutils .literal .notranslate}]{.pre}. This error indicates that an input sequence is longer than the model's maximum context window.

Ensure your tokenized input does not exceed the model's [`max_seq_len`{.docutils .literal .notranslate}]{.pre} (4096 tokens in this case). You can resolve this by truncating the input or splitting it into smaller chunks before passing it to the model.

Note on reproducibility: The results in this guide are based on commit [`b4c98ac`{.docutils .literal .notranslate}]{.pre} from the upstream [pytorch/torchtune](https://github.com/pytorch/torchtune){.github .reference .external} repository. For the latest updates, you can use the main branch.
:::
:::::::

:::::: {.model-doc .pyt-train-gpt-oss-20b .docutils .container}
Fine-tuning

To start the fine-tuning benchmark, use the following command with the appropriate options. See the following list of options and their descriptions. See [[supported training modes]{.std .std-ref}](#amd-pytorch-training-supported-training-modes-v2510){.reference .internal}.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t $training_mode \
        -m GPT-OSS-20B \
        -p $datatype \
        -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                       Description
  ------------------------------------------------------------- ------------------------------------------------------------- ------------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`HF_finetune_lora`{.docutils .literal .notranslate}]{.pre}   LoRA fine-tuning with Hugging Face PEFT.
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre}               All models support BF16.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Between 2048 and 16384.                                       Sequence length for the language model.
:::
::::::

:::::: {.model-doc .pyt-train-gpt-oss-120b .docutils .container}
Fine-tuning

To start the fine-tuning benchmark, use the following command with the appropriate options. See the following list of options and their descriptions. See [[supported training modes]{.std .std-ref}](#amd-pytorch-training-supported-training-modes-v2510){.reference .internal}.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t $training_mode \
        -m GPT-OSS-120B \
        -p $datatype \
        -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                       Description
  ------------------------------------------------------------- ------------------------------------------------------------- ------------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`HF_finetune_lora`{.docutils .literal .notranslate}]{.pre}   LoRA fine-tuning with Hugging Face PEFT.
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre}               All models support BF16.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Between 2048 and 16384.                                       Sequence length for the language model.
:::
::::::

:::::: {.model-doc .primus-pyt-train-deepseek-v2 .docutils .container}
Pretraining

To start the pre-training benchmark, use the following command with the appropriate options. See the following list of options and their descriptions.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t pretrain \
        -m DeepSeek-V2 \
        -p $datatype \
        -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                               Description
  ------------------------------------------------------------- ----------------------------------------------------- -------------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`pretrain`{.docutils .literal .notranslate}]{.pre}   Benchmark pre-training.
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre}       Only Llama 3.1 8B supports FP8 precision.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Sequence length for the language model.               Between 2048 and 8192. 8192 by default.
:::
::::::

:::::: {.model-doc .pyt-train-qwen3-8b .docutils .container}
Fine-tuning

To start the fine-tuning benchmark, use the following command with the appropriate options. See the following list of options and their descriptions. See [[supported training modes]{.std .std-ref}](#amd-pytorch-training-supported-training-modes-v2510){.reference .internal}.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t $training_mode \
        -m Qwen3-8B \
        -p $datatype \
        -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                                                             Description
  ------------------------------------------------------------- --------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`finetune_fw`{.docutils .literal .notranslate}]{.pre}                                              Full weight fine-tuning (BF16 and FP8 supported).
                                                                [`finetune_lora`{.docutils .literal .notranslate}]{.pre}                                            LoRA fine-tuning (BF16 supported).
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre} or [`FP8`{.docutils .literal .notranslate}]{.pre}   All models support BF16. FP8 is only available for full weight fine-tuning.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Between 2048 and 16384.                                                                             Sequence length for the language model.
:::
::::::

:::::: {.model-doc .pyt-train-qwen3-32b .docutils .container}
Fine-tuning

To start the fine-tuning benchmark, use the following command with the appropriate options. See the following list of options and their descriptions. See [[supported training modes]{.std .std-ref}](#amd-pytorch-training-supported-training-modes-v2510){.reference .internal}.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t $training_mode \
        -m Qwen3-32 \
        -p $datatype \
        -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                    Description
  ------------------------------------------------------------- ---------------------------------------------------------- -----------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`finetune_lora`{.docutils .literal .notranslate}]{.pre}   LoRA fine-tuning (BF16 supported).
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre}            All models support BF16.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Between 2048 and 16384.                                    Sequence length for the language model.
:::
::::::

:::::: {.model-doc .pyt-train-qwen2-5-32b .docutils .container}
Fine-tuning

To start the fine-tuning benchmark, use the following command with the appropriate options. See the following list of options and their descriptions. See [[supported training modes]{.std .std-ref}](#amd-pytorch-training-supported-training-modes-v2510){.reference .internal}.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t $training_mode \
        -m Qwen2.5-32B \
        -p $datatype \
        -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                    Description
  ------------------------------------------------------------- ---------------------------------------------------------- -----------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`finetune_lora`{.docutils .literal .notranslate}]{.pre}   LoRA fine-tuning (BF16 supported).
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre}            All models support BF16.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Between 2048 and 16384.                                    Sequence length for the language model.
:::
::::::

:::::: {.model-doc .pyt-train-qwen2-5-72b .docutils .container}
Fine-tuning

To start the fine-tuning benchmark, use the following command with the appropriate options. See the following list of options and their descriptions. See [[supported training modes]{.std .std-ref}](#amd-pytorch-training-supported-training-modes-v2510){.reference .internal}.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t $training_mode \
        -m Qwen2.5-72B \
        -p $datatype \
        -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                    Description
  ------------------------------------------------------------- ---------------------------------------------------------- -----------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`finetune_lora`{.docutils .literal .notranslate}]{.pre}   LoRA fine-tuning (BF16 supported).
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre}            All models support BF16.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Between 2048 and 16384.                                    Sequence length for the language model.
:::
::::::

:::::: {.model-doc .pyt-train-qwen2-1-5b .docutils .container}
Fine-tuning

To start the fine-tuning benchmark, use the following command with the appropriate options. See the following list of options and their descriptions. See [[supported training modes]{.std .std-ref}](#amd-pytorch-training-supported-training-modes-v2510){.reference .internal}.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t $training_mode \
        -m Qwen2-1.5B \
        -p $datatype \
        -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                                                             Description
  ------------------------------------------------------------- --------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`finetune_fw`{.docutils .literal .notranslate}]{.pre}                                              Full weight fine-tuning (BF16 and FP8 supported).
                                                                [`finetune_lora`{.docutils .literal .notranslate}]{.pre}                                            LoRA fine-tuning (BF16 supported).
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre} or [`FP8`{.docutils .literal .notranslate}]{.pre}   All models support BF16. FP8 is only available for full weight fine-tuning.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Between 2048 and 16384.                                                                             Sequence length for the language model.
:::
::::::

:::::: {.model-doc .pyt-train-qwen2-7b .docutils .container}
Fine-tuning

To start the fine-tuning benchmark, use the following command with the appropriate options. See the following list of options and their descriptions. See [[supported training modes]{.std .std-ref}](#amd-pytorch-training-supported-training-modes-v2510){.reference .internal}.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t $training_mode \
        -m Qwen2-7B \
        -p $datatype \
        -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                                                             Description
  ------------------------------------------------------------- --------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`finetune_fw`{.docutils .literal .notranslate}]{.pre}                                              Full weight fine-tuning (BF16 and FP8 supported).
                                                                [`finetune_lora`{.docutils .literal .notranslate}]{.pre}                                            LoRA fine-tuning (BF16 supported).
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre} or [`FP8`{.docutils .literal .notranslate}]{.pre}   All models support BF16. FP8 is only available for full weight fine-tuning.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Between 2048 and 16384.                                                                             Sequence length for the language model.
:::
::::::

:::::: {.model-doc .pyt-huggingface-stable-diffusion-xl-2k-lora-finetuning .docutils .container}
Post-training

To start the post-training benchmark, use the following command with the appropriate options. See the following list of options and their descriptions.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t posttrain \
        -m SDXL \
        -p $datatype \
        -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                Description
  ------------------------------------------------------------- ------------------------------------------------------ -------------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`posttrain`{.docutils .literal .notranslate}]{.pre}   Benchmark post-training.
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre}        Only Llama 3.1 8B supports FP8 precision.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Sequence length for the language model.                Between 2048 and 8192. 8192 by default.
:::
::::::

:::::: {.model-doc .pyt-train-flux .docutils .container}
Post-training

To start the post-training benchmark, use the following command with the appropriate options. See the following list of options and their descriptions.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t posttrain \
        -m Flux \
        -p $datatype \
        -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                Description
  ------------------------------------------------------------- ------------------------------------------------------ -------------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`posttrain`{.docutils .literal .notranslate}]{.pre}   Benchmark post-training.
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre}        Only Llama 3.1 8B supports FP8 precision.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Sequence length for the language model.                Between 2048 and 8192. 8192 by default.
:::
::::::

::: {.model-doc .pyt-train-dlrm .docutils .container}
Pretraining

To start the pre-training benchmark, use the following command with the appropriate options. See the following list of options and their descriptions.

1.  Go to the DLRM directory.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        cd /workspace/DLRMBenchmark
    :::
    ::::

2.  To run the single node training benchmark for DLRM-v2 with TF32 precision, run the following script.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        ./launch_training_single_node.sh
    :::
    ::::

    To run with MAD within the Docker container, use the following command.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        ./pytorch_benchmark_report.sh -t pretrain -m DLRM
    :::
    ::::

Benchmarking examples

For examples of benchmarking commands, see [ROCm/MAD](https://github.com/ROCm/MAD/tree/develop/benchmark/pytorch_train#benchmarking-examples){.github .reference .external}.
:::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::: {#multi-node-training .section}
[]{#amd-pytorch-training-multinode-examples-v2510}

### Multi-node training[\#](#multi-node-training "Link to this heading"){.headerlink}

Refer to [[Multi-node setup for AI workloads]{.doc}](../../../system-setup/multi-node-setup.html){.reference .internal} to configure your environment for multi-node training. See [[PyTorch training]{.std .std-ref}](../../../system-setup/multi-node-setup.html#rocm-for-ai-multi-node-setup-pyt-train-example){.reference .internal} for example Slurm run commands.

::::: {#pre-training .section}
#### Pre-training[\#](#pre-training "Link to this heading"){.headerlink}

Multi-node training with torchtitan is supported. The provided SLURM script is pre-configured for Llama 3 70B.

To launch the training job on a SLURM cluster for Llama 3 70B, run the following commands from the MAD repository.

:::: {.highlight-shell .notranslate}
::: highlight
    # In the MAD repository
    cd scripts/pytorch_train
    sbatch run_slurm_train.sh
:::
::::
:::::

:::::: {#fine-tuning .section}
#### Fine-tuning[\#](#fine-tuning "Link to this heading"){.headerlink}

Multi-node training with torchtune is supported. The provided SLURM script is pre-configured for Llama 3.3 70B.

To launch the training job on a SLURM cluster for Llama 3.3 70B, run the following commands from the MAD repository.

:::: {.highlight-shell .notranslate}
::: highlight
    huggingface-cli login # Get access to HF Llama model space
    huggingface-cli download meta-llama/Llama-3.3-70B-Instruct --local-dir ./models/Llama-3.3-70B-Instruct # Download the Llama 3.3 model locally
    # In the MAD repository
    cd scripts/pytorch_train
    sbatch Torchtune_Multinode.sh
:::
::::

::: {.admonition .note}
Note

Information regarding benchmark setup:

- By default, Llama 3.3 70B is fine-tuned using [`alpaca_dataset`{.docutils .literal .notranslate}]{.pre}.

- You can adjust the torchtune [YAML configuration file](https://github.com/pytorch/torchtune/blob/main/recipes/configs/llama3_3/70B_full_multinode.yaml){.reference .external} if you're using a different model.

- The number of nodes and other parameters can be tuned in the SLURM script [`Torchtune_Multinode.sh`{.docutils .literal .notranslate}]{.pre}.

- Set the [`mounting_paths`{.docutils .literal .notranslate}]{.pre} inside the SLURM script.
:::

Once the run is finished, you can find the log files in the [`result_torchtune/`{.docutils .literal .notranslate}]{.pre} directory.
::::::
::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: {#further-reading .section}
## Further reading[\#](#further-reading "Link to this heading"){.headerlink}

- To learn more about MAD and the [`madengine`{.docutils .literal .notranslate}]{.pre} CLI, see the [MAD usage guide](https://github.com/ROCm/MAD?tab=readme-ov-file#usage-guide){.reference .external}.

- To learn more about system settings and management practices to configure your system for AMD Instinct MI300X Series GPUs, see [AMD Instinct MI300X system optimization](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi300x.html){.reference .external}.

- For a list of other ready-made Docker images for AI with ROCm, see [AMD Infinity Hub](https://www.amd.com/en/developer/resources/infinity-hub.html#f-amd_hub_category=AI%20%26%20ML%20Models){.reference .external}.
:::

::: {#previous-versions .section}
## Previous versions[\#](#previous-versions "Link to this heading"){.headerlink}

See [[PyTorch training performance testing version history]{.doc}](pytorch-training-history.html){.reference .internal} to find documentation for previous releases of the [`ROCm/pytorch-training`{.docutils .literal .notranslate}]{.pre} Docker image.
:::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: prev-next-area
:::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::: {.bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {.page-toc .tocsection .onthispage}
Contents
:::

- [Supported models](#supported-models){.reference .internal .nav-link}
- [Performance measurements](#performance-measurements){.reference .internal .nav-link}
- [System validation](#system-validation){.reference .internal .nav-link}
- [Run training](#run-training){.reference .internal .nav-link}
  - [Multi-node training](#multi-node-training){.reference .internal .nav-link}
    - [Pre-training](#pre-training){.reference .internal .nav-link}
    - [Fine-tuning](#fine-tuning){.reference .internal .nav-link}
- [Further reading](#further-reading){.reference .internal .nav-link}
- [Previous versions](#previous-versions){.reference .internal .nav-link}
::::
:::::
::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
