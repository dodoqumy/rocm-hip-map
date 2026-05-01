---
title: "Training a model with PyTorch for ROCm"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/training/benchmark-docker/previous-versions/pytorch-training-v25.6.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-01
---

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-content
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-article-container
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
# Training a model with PyTorch for ROCm

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [Supported models](#supported-models){.reference .internal .nav-link}
  - [Performance measurements](#performance-measurements){.reference .internal .nav-link}
  - [System validation](#system-validation){.reference .internal .nav-link}
  - [Benchmarking](#benchmarking){.reference .internal .nav-link}
- [Further reading](#further-reading){.reference .internal .nav-link}
- [Previous versions](#previous-versions){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#training-a-model-with-pytorch-for-rocm .section}
# Training a model with PyTorch for ROCm[\#](#training-a-model-with-pytorch-for-rocm "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-04-21
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 26 min read time
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

This documentation does not reflect the latest version of ROCm vLLM performance benchmark documentation. See [[Training a model with PyTorch on ROCm]{.doc}](../pytorch-training.html){.reference .internal} for the latest version.
:::

PyTorch is an open-source machine learning framework that is widely used for model training with GPU-optimized components for transformer-based models.

The [PyTorch for ROCm training Docker](https://hub.docker.com/layers/rocm/pytorch-training/v25.6/images/sha256-a4cea3c493a4a03d199a3e81960ac071d79a4a7a391aa9866add3b30a7842661){.reference .external} ([`rocm/pytorch-training:v25.6`{.docutils .literal .notranslate}]{.pre}) image provides a prebuilt optimized environment for fine-tuning and pretraining a model on AMD Instinct MI325X and MI300X GPUs. It includes the following software components to accelerate training workloads:

::: pst-scrollable-table-container
  Software component   Version
  -------------------- --------------------
  ROCm                 6.3.4
  PyTorch              2.8.0a0+git7d205b2
  Python               3.10.17
  Transformer Engine   1.14.0+2f85f5f2
  Flash Attention      3.0.0.post1
  hipBLASLt            0.15.0-8c6919d
  Triton               3.3.0
:::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#supported-models .section}
[]{#amd-pytorch-training-model-support-v256}

## Supported models[\#](#supported-models "Link to this heading"){.headerlink}

The following models are pre-optimized for performance on the AMD Instinct MI325X and MI300X GPUs.

:::::::::::::::::::::::::::: {#vllm-benchmark-ud-params-picker .container-fluid}
::::::: row
::: {.col-2 .me-2 .model-param-head}
Workload
:::

::::: {.row .col-10}
::: {.col-6 .model-param param-k="model-group" param-v="pre-training" tabindex="0"}
Pre-training
:::

::: {.col-6 .model-param param-k="model-group" param-v="fine-tuning" tabindex="0"}
Fine-tuning
:::
:::::
:::::::

:::::::::::::::::::::: {.row .mt-1}
::: {.col-2 .me-2 .model-param-head}
Model
:::

:::::::::::::::::::: {.row .col-10}
::: {.col-4 .model-param param-group="pre-training" param-k="model" param-v="pyt_train_llama-3.1-8b" tabindex="0"}
Llama 3.1 8B
:::

::: {.col-4 .model-param param-group="pre-training" param-k="model" param-v="pyt_train_llama-3.1-70b" tabindex="0"}
Llama 3.1 70B
:::

::: {.col-4 .model-param param-group="pre-training" param-k="model" param-v="pyt_train_flux" tabindex="0"}
FLUX.1-dev
:::

::: {.col-6 .model-param param-group="fine-tuning" param-k="model" param-v="pyt_train_llama-4-scout-17b-16e" tabindex="0"}
Llama 4 Scout 17B-16E
:::

::: {.col-6 .model-param param-group="fine-tuning" param-k="model" param-v="pyt_train_llama-3.3-70b" tabindex="0"}
Llama 3.3 70B
:::

::: {.col-6 .model-param param-group="fine-tuning" param-k="model" param-v="pyt_train_llama-3.2-1b" tabindex="0"}
Llama 3.2 1B
:::

::: {.col-6 .model-param param-group="fine-tuning" param-k="model" param-v="pyt_train_llama-3.2-3b" tabindex="0"}
Llama 3.2 3B
:::

::: {.col-6 .model-param param-group="fine-tuning" param-k="model" param-v="pyt_train_llama-3.2-vision-11b" tabindex="0"}
Llama 3.2 Vision 11B
:::

::: {.col-6 .model-param param-group="fine-tuning" param-k="model" param-v="pyt_train_llama-3.2-vision-90b" tabindex="0"}
Llama 3.2 Vision 90B
:::

::: {.col-6 .model-param param-group="fine-tuning" param-k="model" param-v="pyt_train_llama-3.1-8b" tabindex="0"}
Llama 3.1 8B
:::

::: {.col-6 .model-param param-group="fine-tuning" param-k="model" param-v="pyt_train_llama-3.1-70b" tabindex="0"}
Llama 3.1 70B
:::

::: {.col-6 .model-param param-group="fine-tuning" param-k="model" param-v="pyt_train_llama-3.1-405b" tabindex="0"}
Llama 3.1 405B
:::

::: {.col-6 .model-param param-group="fine-tuning" param-k="model" param-v="pyt_train_llama-3-8b" tabindex="0"}
Llama 3 8B
:::

::: {.col-6 .model-param param-group="fine-tuning" param-k="model" param-v="pyt_train_llama-3-70b" tabindex="0"}
Llama 3 70B
:::

::: {.col-6 .model-param param-group="fine-tuning" param-k="model" param-v="pyt_train_llama-2-7b" tabindex="0"}
Llama 2 7B
:::

::: {.col-6 .model-param param-group="fine-tuning" param-k="model" param-v="pyt_train_llama-2-13b" tabindex="0"}
Llama 2 13B
:::

::: {.col-6 .model-param param-group="fine-tuning" param-k="model" param-v="pyt_train_llama-2-70b" tabindex="0"}
Llama 2 70B
:::
::::::::::::::::::::
::::::::::::::::::::::
::::::::::::::::::::::::::::

::: {.admonition .note}
Note

Some models require an external license agreement through a third party (for example, Meta).
:::

:::: {#performance-measurements .section}
[]{#amd-pytorch-training-performance-measurements-v256}

### Performance measurements[\#](#performance-measurements "Link to this heading"){.headerlink}

To evaluate performance, the [Performance results with AMD ROCm software](https://www.amd.com/en/developer/resources/rocm-hub/dev-ai/performance-results.html#tabs-a8deaeb413-item-21cea50186-tab){.reference .external} page provides reference throughput and latency measurements for training popular AI models.

::: {.admonition .note}
Note

The performance data presented in [Performance results with AMD ROCm software](https://www.amd.com/en/developer/resources/rocm-hub/dev-ai/performance-results.html#tabs-a8deaeb413-item-21cea50186-tab){.reference .external} should not be interpreted as the peak performance achievable by AMD Instinct MI325X and MI300X GPUs or ROCm software.
:::
::::

::: {#system-validation .section}
### System validation[\#](#system-validation "Link to this heading"){.headerlink}

Before running AI workloads, it's important to validate that your AMD hardware is configured correctly and performing optimally.

If you have already validated your system settings, including aspects like NUMA auto-balancing, you can skip this step. Otherwise, complete the procedures in the [[System validation and optimization]{.std .std-ref}](../../../system-setup/prerequisite-system-validation.html#rocm-for-ai-system-optimization){.reference .internal} guide to properly configure your system settings before starting training.

To test for optimal performance, consult the recommended [[System health benchmarks]{.std .std-ref}](../../../system-setup/system-health-check.html#rocm-for-ai-system-health-bench){.reference .internal}. This suite of tests will help you verify and fine-tune your system's configuration.

This Docker image is optimized for specific model configurations outlined below. Performance can vary for other training workloads, as AMD doesn't validate configurations and run conditions outside those described.
:::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#benchmarking .section}
### Benchmarking[\#](#benchmarking "Link to this heading"){.headerlink}

Once the setup is complete, choose between two options to start benchmarking:

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

:::::::::::::::::::::::::::::::::::::::::::::::::::::::: {.sd-tab-content .docutils}
Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

:::: {.highlight-shell .notranslate}
::: highlight
    git clone https://github.com/ROCm/MAD
    cd MAD
    pip install -r requirements.txt
:::
::::

::::: {.model-doc .pyt-train-llama-3-1-8b .docutils .container}
For example, use this command to run the performance benchmark test on the Llama 3.1 8B model using one GPU with the BF16 data type on the host machine.

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

MAD launches a Docker container with the name [`container_ci-pyt_train_llama-3.1-8b`{.docutils .literal .notranslate}]{.pre}, for example. The latency and throughput reports of the model are collected in the following path: [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::::

::::: {.model-doc .pyt-train-llama-3-1-70b .docutils .container}
For example, use this command to run the performance benchmark test on the Llama 3.1 70B model using one GPU with the BF16 data type on the host machine.

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

MAD launches a Docker container with the name [`container_ci-pyt_train_llama-3.1-70b`{.docutils .literal .notranslate}]{.pre}, for example. The latency and throughput reports of the model are collected in the following path: [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::::

::::: {.model-doc .pyt-train-flux .docutils .container}
For example, use this command to run the performance benchmark test on the FLUX.1-dev model using one GPU with the BF16 data type on the host machine.

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

MAD launches a Docker container with the name [`container_ci-pyt_train_flux`{.docutils .literal .notranslate}]{.pre}, for example. The latency and throughput reports of the model are collected in the following path: [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::::

::::: {.model-doc .pyt-train-llama-4-scout-17b-16e .docutils .container}
For example, use this command to run the performance benchmark test on the Llama 4 Scout 17B-16E model using one GPU with the BF16 data type on the host machine.

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

MAD launches a Docker container with the name [`container_ci-pyt_train_llama-4-scout-17b-16e`{.docutils .literal .notranslate}]{.pre}, for example. The latency and throughput reports of the model are collected in the following path: [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::::

::::: {.model-doc .pyt-train-llama-3-3-70b .docutils .container}
For example, use this command to run the performance benchmark test on the Llama 3.3 70B model using one GPU with the BF16 data type on the host machine.

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

MAD launches a Docker container with the name [`container_ci-pyt_train_llama-3.3-70b`{.docutils .literal .notranslate}]{.pre}, for example. The latency and throughput reports of the model are collected in the following path: [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::::

::::: {.model-doc .pyt-train-llama-3-2-1b .docutils .container}
For example, use this command to run the performance benchmark test on the Llama 3.2 1B model using one GPU with the BF16 data type on the host machine.

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

MAD launches a Docker container with the name [`container_ci-pyt_train_llama-3.2-1b`{.docutils .literal .notranslate}]{.pre}, for example. The latency and throughput reports of the model are collected in the following path: [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::::

::::: {.model-doc .pyt-train-llama-3-2-3b .docutils .container}
For example, use this command to run the performance benchmark test on the Llama 3.2 3B model using one GPU with the BF16 data type on the host machine.

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

MAD launches a Docker container with the name [`container_ci-pyt_train_llama-3.2-3b`{.docutils .literal .notranslate}]{.pre}, for example. The latency and throughput reports of the model are collected in the following path: [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::::

::::: {.model-doc .pyt-train-llama-3-2-vision-11b .docutils .container}
For example, use this command to run the performance benchmark test on the Llama 3.2 Vision 11B model using one GPU with the BF16 data type on the host machine.

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

MAD launches a Docker container with the name [`container_ci-pyt_train_llama-3.2-vision-11b`{.docutils .literal .notranslate}]{.pre}, for example. The latency and throughput reports of the model are collected in the following path: [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::::

::::: {.model-doc .pyt-train-llama-3-2-vision-90b .docutils .container}
For example, use this command to run the performance benchmark test on the Llama 3.2 Vision 90B model using one GPU with the BF16 data type on the host machine.

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

MAD launches a Docker container with the name [`container_ci-pyt_train_llama-3.2-vision-90b`{.docutils .literal .notranslate}]{.pre}, for example. The latency and throughput reports of the model are collected in the following path: [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::::

::::: {.model-doc .pyt-train-llama-3-1-8b .docutils .container}
For example, use this command to run the performance benchmark test on the Llama 3.1 8B model using one GPU with the BF16 data type on the host machine.

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

MAD launches a Docker container with the name [`container_ci-pyt_train_llama-3.1-8b`{.docutils .literal .notranslate}]{.pre}, for example. The latency and throughput reports of the model are collected in the following path: [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::::

::::: {.model-doc .pyt-train-llama-3-1-70b .docutils .container}
For example, use this command to run the performance benchmark test on the Llama 3.1 70B model using one GPU with the BF16 data type on the host machine.

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

MAD launches a Docker container with the name [`container_ci-pyt_train_llama-3.1-70b`{.docutils .literal .notranslate}]{.pre}, for example. The latency and throughput reports of the model are collected in the following path: [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::::

::::: {.model-doc .pyt-train-llama-3-1-405b .docutils .container}
For example, use this command to run the performance benchmark test on the Llama 3.1 405B model using one GPU with the BF16 data type on the host machine.

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

MAD launches a Docker container with the name [`container_ci-pyt_train_llama-3.1-405b`{.docutils .literal .notranslate}]{.pre}, for example. The latency and throughput reports of the model are collected in the following path: [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::::

::::: {.model-doc .pyt-train-llama-3-8b .docutils .container}
For example, use this command to run the performance benchmark test on the Llama 3 8B model using one GPU with the BF16 data type on the host machine.

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

MAD launches a Docker container with the name [`container_ci-pyt_train_llama-3-8b`{.docutils .literal .notranslate}]{.pre}, for example. The latency and throughput reports of the model are collected in the following path: [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::::

::::: {.model-doc .pyt-train-llama-3-70b .docutils .container}
For example, use this command to run the performance benchmark test on the Llama 3 70B model using one GPU with the BF16 data type on the host machine.

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

MAD launches a Docker container with the name [`container_ci-pyt_train_llama-3-70b`{.docutils .literal .notranslate}]{.pre}, for example. The latency and throughput reports of the model are collected in the following path: [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::::

::::: {.model-doc .pyt-train-llama-2-7b .docutils .container}
For example, use this command to run the performance benchmark test on the Llama 2 7B model using one GPU with the BF16 data type on the host machine.

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

MAD launches a Docker container with the name [`container_ci-pyt_train_llama-2-7b`{.docutils .literal .notranslate}]{.pre}, for example. The latency and throughput reports of the model are collected in the following path: [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::::

::::: {.model-doc .pyt-train-llama-2-13b .docutils .container}
For example, use this command to run the performance benchmark test on the Llama 2 13B model using one GPU with the BF16 data type on the host machine.

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

MAD launches a Docker container with the name [`container_ci-pyt_train_llama-2-13b`{.docutils .literal .notranslate}]{.pre}, for example. The latency and throughput reports of the model are collected in the following path: [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::::

::::: {.model-doc .pyt-train-llama-2-70b .docutils .container}
For example, use this command to run the performance benchmark test on the Llama 2 70B model using one GPU with the BF16 data type on the host machine.

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

MAD launches a Docker container with the name [`container_ci-pyt_train_llama-2-70b`{.docutils .literal .notranslate}]{.pre}, for example. The latency and throughput reports of the model are collected in the following path: [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.
:::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Standalone benchmarking

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {.sd-tab-content .docutils}
Download the Docker image and required packages

Use the following command to pull the Docker image from Docker Hub.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/pytorch-training:v25.6
:::
::::

Run the Docker container.

:::: {.highlight-shell .notranslate}
::: highlight
    docker run -it --device /dev/dri --device /dev/kfd --network host --ipc host --group-add video --cap-add SYS_PTRACE --security-opt seccomp=unconfined --privileged -v $HOME:$HOME -v  $HOME/.ssh:/root/.ssh --shm-size 64G --name training_env rocm/pytorch-training:v25.6
:::
::::

Use these commands if you exit the [`training_env`{.docutils .literal .notranslate}]{.pre} container and need to return to it.

:::: {.highlight-shell .notranslate}
::: highlight
    docker start training_env
    docker exec -it training_env bash
:::
::::

In the Docker container, clone the [ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external} repository and navigate to the benchmark scripts directory [`/workspace/MAD/scripts/pytorch_train`{.docutils .literal .notranslate}]{.pre}.

:::: {.highlight-shell .notranslate}
::: highlight
    git clone https://github.com/ROCm/MAD
    cd MAD/scripts/pytorch_train
:::
::::

Prepare training datasets and dependencies

The following benchmarking examples require downloading models and datasets from Hugging Face. To ensure successful access to gated repos, set your [`HF_TOKEN`{.docutils .literal .notranslate}]{.pre}.

:::: {.highlight-shell .notranslate}
::: highlight
    export HF_TOKEN=$your_personal_hugging_face_access_token
:::
::::

Run the setup script to install libraries and datasets needed for benchmarking.

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
  [`torchdata`{.docutils .literal .notranslate}]{.pre}       [TorchData](https://meta-pytorch.org/data/beta/index.html){.reference .external}
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

- [bghira/pseudo-camera-10k](https://huggingface.co/datasets/bghira/pseudo-camera-10k){.reference .external}

:::::: {.model-doc .pyt-train-llama-3-1-8b .docutils .container}
Pretraining

To start the pre-training benchmark, use the following command with the appropriate options. See the following list of options and their descriptions.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t pretrain -m Llama-3.1-8B -p $datatype -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                                                             Description
  ------------------------------------------------------------- --------------------------------------------------------------------------------------------------- -------------------------------------------
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre} or [`FP8`{.docutils .literal .notranslate}]{.pre}   Only Llama 3.1 8B supports FP8 precision.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Sequence length for the language model.                                                             Between 2048 and 8192. 8192 by default.
:::
::::::

:::::: {.model-doc .pyt-train-llama-3-1-70b .docutils .container}
Pretraining

To start the pre-training benchmark, use the following command with the appropriate options. See the following list of options and their descriptions.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t pretrain -m Llama-3.1-70B -p $datatype -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                           Description
  ------------------------------------------------------------- ------------------------------------------------- -------------------------------------------
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre}   Only Llama 3.1 8B supports FP8 precision.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Sequence length for the language model.           Between 2048 and 8192. 8192 by default.
:::
::::::

:::::::: {.model-doc .pyt-train-flux .docutils .container}
Pretraining

To start the pre-training benchmark, use the following command with the appropriate options. See the following list of options and their descriptions.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t pretrain -m Flux -p $datatype -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                           Description
  ------------------------------------------------------------- ------------------------------------------------- -------------------------------------------
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre}   Only Llama 3.1 8B supports FP8 precision.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Sequence length for the language model.           Between 2048 and 8192. 8192 by default.
:::

:::: {.model-doc .pyt-train-flux .docutils .container}
::: {.admonition .note}
Note

Occasionally, downloading the Flux dataset might fail. In the event of this error, manually download it from Hugging Face at [black-forest-labs/FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev){.reference .external} and save it to /workspace/FluxBenchmark. This ensures that the test script can access the required dataset.
:::
::::
::::::::

::::::: {.model-doc .pyt-train-llama-4-scout-17b-16e .docutils .container}
Fine-tuning

To start the fine-tuning benchmark, use the following command with the appropriate options. See the following list of options and their descriptions.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t $training_mode -m Llama-4-17B_16E -p BF16 -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                       Description
  ------------------------------------------------------------- ------------------------------------------------------------- ------------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`finetune_fw`{.docutils .literal .notranslate}]{.pre}        Full weight fine-tuning (BF16 supported)
                                                                [`finetune_lora`{.docutils .literal .notranslate}]{.pre}      LoRA fine-tuning (BF16 supported)
                                                                [`finetune_qlora`{.docutils .literal .notranslate}]{.pre}     QLoRA fine-tuning (BF16 supported)
                                                                [`HF_finetune_lora`{.docutils .literal .notranslate}]{.pre}   LoRA fine-tuning with Hugging Face PEFT
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre}               All models support BF16.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Between 2048 and 16384.                                       Sequence length for the language model.
:::

::: {.admonition .note}
Note

Llama 4 Scout 17B-16E currently supports the following fine-tuning methods:

- [`finetune_fw`{.docutils .literal .notranslate}]{.pre}

- [`finetune_lora`{.docutils .literal .notranslate}]{.pre}

The upstream [torchtune](https://github.com/pytorch/torchtune){.reference .external} repository does not currently provide YAML configuration files for other combinations of model to fine-tuning method However, you can still configure your own YAML files to enable support for fine-tuning methods not listed here by following existing patterns in the [`/workspace/torchtune/recipes/configs`{.docutils .literal .notranslate}]{.pre} directory.
:::
:::::::

::::::: {.model-doc .pyt-train-llama-3-3-70b .docutils .container}
Fine-tuning

To start the fine-tuning benchmark, use the following command with the appropriate options. See the following list of options and their descriptions.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t $training_mode -m Llama-3.3-70B -p BF16 -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                       Description
  ------------------------------------------------------------- ------------------------------------------------------------- ------------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`finetune_fw`{.docutils .literal .notranslate}]{.pre}        Full weight fine-tuning (BF16 supported)
                                                                [`finetune_lora`{.docutils .literal .notranslate}]{.pre}      LoRA fine-tuning (BF16 supported)
                                                                [`finetune_qlora`{.docutils .literal .notranslate}]{.pre}     QLoRA fine-tuning (BF16 supported)
                                                                [`HF_finetune_lora`{.docutils .literal .notranslate}]{.pre}   LoRA fine-tuning with Hugging Face PEFT
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre}               All models support BF16.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Between 2048 and 16384.                                       Sequence length for the language model.
:::

::: {.admonition .note}
Note

Llama 3.3 70B currently supports the following fine-tuning methods:

- [`finetune_fw`{.docutils .literal .notranslate}]{.pre}

- [`finetune_lora`{.docutils .literal .notranslate}]{.pre}

- [`finetune_qlora`{.docutils .literal .notranslate}]{.pre}

The upstream [torchtune](https://github.com/pytorch/torchtune){.reference .external} repository does not currently provide YAML configuration files for other combinations of model to fine-tuning method However, you can still configure your own YAML files to enable support for fine-tuning methods not listed here by following existing patterns in the [`/workspace/torchtune/recipes/configs`{.docutils .literal .notranslate}]{.pre} directory.
:::
:::::::

::::::: {.model-doc .pyt-train-llama-3-2-1b .docutils .container}
Fine-tuning

To start the fine-tuning benchmark, use the following command with the appropriate options. See the following list of options and their descriptions.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t $training_mode -m Llama-3.2-1B -p BF16 -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                       Description
  ------------------------------------------------------------- ------------------------------------------------------------- ------------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`finetune_fw`{.docutils .literal .notranslate}]{.pre}        Full weight fine-tuning (BF16 supported)
                                                                [`finetune_lora`{.docutils .literal .notranslate}]{.pre}      LoRA fine-tuning (BF16 supported)
                                                                [`finetune_qlora`{.docutils .literal .notranslate}]{.pre}     QLoRA fine-tuning (BF16 supported)
                                                                [`HF_finetune_lora`{.docutils .literal .notranslate}]{.pre}   LoRA fine-tuning with Hugging Face PEFT
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre}               All models support BF16.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Between 2048 and 16384.                                       Sequence length for the language model.
:::

::: {.admonition .note}
Note

Llama 3.2 1B currently supports the following fine-tuning methods:

- [`finetune_fw`{.docutils .literal .notranslate}]{.pre}

- [`finetune_lora`{.docutils .literal .notranslate}]{.pre}

The upstream [torchtune](https://github.com/pytorch/torchtune){.reference .external} repository does not currently provide YAML configuration files for other combinations of model to fine-tuning method However, you can still configure your own YAML files to enable support for fine-tuning methods not listed here by following existing patterns in the [`/workspace/torchtune/recipes/configs`{.docutils .literal .notranslate}]{.pre} directory.
:::
:::::::

::::::: {.model-doc .pyt-train-llama-3-2-3b .docutils .container}
Fine-tuning

To start the fine-tuning benchmark, use the following command with the appropriate options. See the following list of options and their descriptions.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t $training_mode -m Llama-3.2-3B -p BF16 -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                       Description
  ------------------------------------------------------------- ------------------------------------------------------------- ------------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`finetune_fw`{.docutils .literal .notranslate}]{.pre}        Full weight fine-tuning (BF16 supported)
                                                                [`finetune_lora`{.docutils .literal .notranslate}]{.pre}      LoRA fine-tuning (BF16 supported)
                                                                [`finetune_qlora`{.docutils .literal .notranslate}]{.pre}     QLoRA fine-tuning (BF16 supported)
                                                                [`HF_finetune_lora`{.docutils .literal .notranslate}]{.pre}   LoRA fine-tuning with Hugging Face PEFT
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre}               All models support BF16.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Between 2048 and 16384.                                       Sequence length for the language model.
:::

::: {.admonition .note}
Note

Llama 3.2 3B currently supports the following fine-tuning methods:

- [`finetune_fw`{.docutils .literal .notranslate}]{.pre}

- [`finetune_lora`{.docutils .literal .notranslate}]{.pre}

The upstream [torchtune](https://github.com/pytorch/torchtune){.reference .external} repository does not currently provide YAML configuration files for other combinations of model to fine-tuning method However, you can still configure your own YAML files to enable support for fine-tuning methods not listed here by following existing patterns in the [`/workspace/torchtune/recipes/configs`{.docutils .literal .notranslate}]{.pre} directory.
:::
:::::::

::::::: {.model-doc .pyt-train-llama-3-2-vision-11b .docutils .container}
Fine-tuning

To start the fine-tuning benchmark, use the following command with the appropriate options. See the following list of options and their descriptions.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t $training_mode -m Llama-3.2-Vision-11B -p BF16 -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                       Description
  ------------------------------------------------------------- ------------------------------------------------------------- ------------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`finetune_fw`{.docutils .literal .notranslate}]{.pre}        Full weight fine-tuning (BF16 supported)
                                                                [`finetune_lora`{.docutils .literal .notranslate}]{.pre}      LoRA fine-tuning (BF16 supported)
                                                                [`finetune_qlora`{.docutils .literal .notranslate}]{.pre}     QLoRA fine-tuning (BF16 supported)
                                                                [`HF_finetune_lora`{.docutils .literal .notranslate}]{.pre}   LoRA fine-tuning with Hugging Face PEFT
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre}               All models support BF16.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Between 2048 and 16384.                                       Sequence length for the language model.
:::

::: {.admonition .note}
Note

Llama 3.2 Vision 11B currently supports the following fine-tuning methods:

- [`finetune_fw`{.docutils .literal .notranslate}]{.pre}

The upstream [torchtune](https://github.com/pytorch/torchtune){.reference .external} repository does not currently provide YAML configuration files for other combinations of model to fine-tuning method However, you can still configure your own YAML files to enable support for fine-tuning methods not listed here by following existing patterns in the [`/workspace/torchtune/recipes/configs`{.docutils .literal .notranslate}]{.pre} directory.
:::
:::::::

::::::: {.model-doc .pyt-train-llama-3-2-vision-90b .docutils .container}
Fine-tuning

To start the fine-tuning benchmark, use the following command with the appropriate options. See the following list of options and their descriptions.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t $training_mode -m Llama-3.2-Vision-90B -p BF16 -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                       Description
  ------------------------------------------------------------- ------------------------------------------------------------- ------------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`finetune_fw`{.docutils .literal .notranslate}]{.pre}        Full weight fine-tuning (BF16 supported)
                                                                [`finetune_lora`{.docutils .literal .notranslate}]{.pre}      LoRA fine-tuning (BF16 supported)
                                                                [`finetune_qlora`{.docutils .literal .notranslate}]{.pre}     QLoRA fine-tuning (BF16 supported)
                                                                [`HF_finetune_lora`{.docutils .literal .notranslate}]{.pre}   LoRA fine-tuning with Hugging Face PEFT
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre}               All models support BF16.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Between 2048 and 16384.                                       Sequence length for the language model.
:::

::: {.admonition .note}
Note

Llama 3.2 Vision 90B currently supports the following fine-tuning methods:

- [`finetune_fw`{.docutils .literal .notranslate}]{.pre}

The upstream [torchtune](https://github.com/pytorch/torchtune){.reference .external} repository does not currently provide YAML configuration files for other combinations of model to fine-tuning method However, you can still configure your own YAML files to enable support for fine-tuning methods not listed here by following existing patterns in the [`/workspace/torchtune/recipes/configs`{.docutils .literal .notranslate}]{.pre} directory.
:::
:::::::

::::::: {.model-doc .pyt-train-llama-3-1-8b .docutils .container}
Fine-tuning

To start the fine-tuning benchmark, use the following command with the appropriate options. See the following list of options and their descriptions.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t $training_mode -m Llama-3.1-8B -p BF16 -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                       Description
  ------------------------------------------------------------- ------------------------------------------------------------- ------------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`finetune_fw`{.docutils .literal .notranslate}]{.pre}        Full weight fine-tuning (BF16 supported)
                                                                [`finetune_lora`{.docutils .literal .notranslate}]{.pre}      LoRA fine-tuning (BF16 supported)
                                                                [`finetune_qlora`{.docutils .literal .notranslate}]{.pre}     QLoRA fine-tuning (BF16 supported)
                                                                [`HF_finetune_lora`{.docutils .literal .notranslate}]{.pre}   LoRA fine-tuning with Hugging Face PEFT
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre}               All models support BF16.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Between 2048 and 16384.                                       Sequence length for the language model.
:::

::: {.admonition .note}
Note

Llama 3.1 8B currently supports the following fine-tuning methods:

- [`finetune_fw`{.docutils .literal .notranslate}]{.pre}

- [`finetune_lora`{.docutils .literal .notranslate}]{.pre}

The upstream [torchtune](https://github.com/pytorch/torchtune){.reference .external} repository does not currently provide YAML configuration files for other combinations of model to fine-tuning method However, you can still configure your own YAML files to enable support for fine-tuning methods not listed here by following existing patterns in the [`/workspace/torchtune/recipes/configs`{.docutils .literal .notranslate}]{.pre} directory.
:::
:::::::

::::::: {.model-doc .pyt-train-llama-3-1-70b .docutils .container}
Fine-tuning

To start the fine-tuning benchmark, use the following command with the appropriate options. See the following list of options and their descriptions.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t $training_mode -m Llama-3.1-70B -p BF16 -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                       Description
  ------------------------------------------------------------- ------------------------------------------------------------- ------------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`finetune_fw`{.docutils .literal .notranslate}]{.pre}        Full weight fine-tuning (BF16 supported)
                                                                [`finetune_lora`{.docutils .literal .notranslate}]{.pre}      LoRA fine-tuning (BF16 supported)
                                                                [`finetune_qlora`{.docutils .literal .notranslate}]{.pre}     QLoRA fine-tuning (BF16 supported)
                                                                [`HF_finetune_lora`{.docutils .literal .notranslate}]{.pre}   LoRA fine-tuning with Hugging Face PEFT
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre}               All models support BF16.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Between 2048 and 16384.                                       Sequence length for the language model.
:::

::: {.admonition .note}
Note

Llama 3.1 70B currently supports the following fine-tuning methods:

- [`finetune_fw`{.docutils .literal .notranslate}]{.pre}

- [`finetune_lora`{.docutils .literal .notranslate}]{.pre}

- [`finetune_qlora`{.docutils .literal .notranslate}]{.pre}

The upstream [torchtune](https://github.com/pytorch/torchtune){.reference .external} repository does not currently provide YAML configuration files for other combinations of model to fine-tuning method However, you can still configure your own YAML files to enable support for fine-tuning methods not listed here by following existing patterns in the [`/workspace/torchtune/recipes/configs`{.docutils .literal .notranslate}]{.pre} directory.
:::
:::::::

::::::: {.model-doc .pyt-train-llama-3-1-405b .docutils .container}
Fine-tuning

To start the fine-tuning benchmark, use the following command with the appropriate options. See the following list of options and their descriptions.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t $training_mode -m Llama-3.1-405B -p BF16 -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                       Description
  ------------------------------------------------------------- ------------------------------------------------------------- ------------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`finetune_fw`{.docutils .literal .notranslate}]{.pre}        Full weight fine-tuning (BF16 supported)
                                                                [`finetune_lora`{.docutils .literal .notranslate}]{.pre}      LoRA fine-tuning (BF16 supported)
                                                                [`finetune_qlora`{.docutils .literal .notranslate}]{.pre}     QLoRA fine-tuning (BF16 supported)
                                                                [`HF_finetune_lora`{.docutils .literal .notranslate}]{.pre}   LoRA fine-tuning with Hugging Face PEFT
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre}               All models support BF16.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Between 2048 and 16384.                                       Sequence length for the language model.
:::

::: {.admonition .note}
Note

Llama 3.1 405B currently supports the following fine-tuning methods:

- [`finetune_qlora`{.docutils .literal .notranslate}]{.pre}

- [`HF_finetune_lora`{.docutils .literal .notranslate}]{.pre}

The upstream [torchtune](https://github.com/pytorch/torchtune){.reference .external} repository does not currently provide YAML configuration files for other combinations of model to fine-tuning method However, you can still configure your own YAML files to enable support for fine-tuning methods not listed here by following existing patterns in the [`/workspace/torchtune/recipes/configs`{.docutils .literal .notranslate}]{.pre} directory.
:::
:::::::

::::::: {.model-doc .pyt-train-llama-3-8b .docutils .container}
Fine-tuning

To start the fine-tuning benchmark, use the following command with the appropriate options. See the following list of options and their descriptions.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t $training_mode -m Llama-3-8B -p BF16 -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                       Description
  ------------------------------------------------------------- ------------------------------------------------------------- ------------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`finetune_fw`{.docutils .literal .notranslate}]{.pre}        Full weight fine-tuning (BF16 supported)
                                                                [`finetune_lora`{.docutils .literal .notranslate}]{.pre}      LoRA fine-tuning (BF16 supported)
                                                                [`finetune_qlora`{.docutils .literal .notranslate}]{.pre}     QLoRA fine-tuning (BF16 supported)
                                                                [`HF_finetune_lora`{.docutils .literal .notranslate}]{.pre}   LoRA fine-tuning with Hugging Face PEFT
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre}               All models support BF16.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Between 2048 and 16384.                                       Sequence length for the language model.
:::

::: {.admonition .note}
Note

Llama 3 8B currently supports the following fine-tuning methods:

- [`finetune_fw`{.docutils .literal .notranslate}]{.pre}

- [`finetune_lora`{.docutils .literal .notranslate}]{.pre}

The upstream [torchtune](https://github.com/pytorch/torchtune){.reference .external} repository does not currently provide YAML configuration files for other combinations of model to fine-tuning method However, you can still configure your own YAML files to enable support for fine-tuning methods not listed here by following existing patterns in the [`/workspace/torchtune/recipes/configs`{.docutils .literal .notranslate}]{.pre} directory.
:::
:::::::

::::::: {.model-doc .pyt-train-llama-3-70b .docutils .container}
Fine-tuning

To start the fine-tuning benchmark, use the following command with the appropriate options. See the following list of options and their descriptions.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t $training_mode -m Llama-3-70B -p BF16 -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                       Description
  ------------------------------------------------------------- ------------------------------------------------------------- ------------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`finetune_fw`{.docutils .literal .notranslate}]{.pre}        Full weight fine-tuning (BF16 supported)
                                                                [`finetune_lora`{.docutils .literal .notranslate}]{.pre}      LoRA fine-tuning (BF16 supported)
                                                                [`finetune_qlora`{.docutils .literal .notranslate}]{.pre}     QLoRA fine-tuning (BF16 supported)
                                                                [`HF_finetune_lora`{.docutils .literal .notranslate}]{.pre}   LoRA fine-tuning with Hugging Face PEFT
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre}               All models support BF16.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Between 2048 and 16384.                                       Sequence length for the language model.
:::

::: {.admonition .note}
Note

Llama 3 70B currently supports the following fine-tuning methods:

- [`finetune_fw`{.docutils .literal .notranslate}]{.pre}

- [`finetune_lora`{.docutils .literal .notranslate}]{.pre}

The upstream [torchtune](https://github.com/pytorch/torchtune){.reference .external} repository does not currently provide YAML configuration files for other combinations of model to fine-tuning method However, you can still configure your own YAML files to enable support for fine-tuning methods not listed here by following existing patterns in the [`/workspace/torchtune/recipes/configs`{.docutils .literal .notranslate}]{.pre} directory.
:::
:::::::

::::::: {.model-doc .pyt-train-llama-2-7b .docutils .container}
Fine-tuning

To start the fine-tuning benchmark, use the following command with the appropriate options. See the following list of options and their descriptions.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t $training_mode -m Llama-2-7B -p BF16 -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                       Description
  ------------------------------------------------------------- ------------------------------------------------------------- ------------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`finetune_fw`{.docutils .literal .notranslate}]{.pre}        Full weight fine-tuning (BF16 supported)
                                                                [`finetune_lora`{.docutils .literal .notranslate}]{.pre}      LoRA fine-tuning (BF16 supported)
                                                                [`finetune_qlora`{.docutils .literal .notranslate}]{.pre}     QLoRA fine-tuning (BF16 supported)
                                                                [`HF_finetune_lora`{.docutils .literal .notranslate}]{.pre}   LoRA fine-tuning with Hugging Face PEFT
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre}               All models support BF16.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Between 2048 and 16384.                                       Sequence length for the language model.
:::

::: {.admonition .note}
Note

Llama 2 7B currently supports the following fine-tuning methods:

- [`finetune_fw`{.docutils .literal .notranslate}]{.pre}

- [`finetune_lora`{.docutils .literal .notranslate}]{.pre}

- [`finetune_qlora`{.docutils .literal .notranslate}]{.pre}

The upstream [torchtune](https://github.com/pytorch/torchtune){.reference .external} repository does not currently provide YAML configuration files for other combinations of model to fine-tuning method However, you can still configure your own YAML files to enable support for fine-tuning methods not listed here by following existing patterns in the [`/workspace/torchtune/recipes/configs`{.docutils .literal .notranslate}]{.pre} directory.
:::
:::::::

::::::: {.model-doc .pyt-train-llama-2-13b .docutils .container}
Fine-tuning

To start the fine-tuning benchmark, use the following command with the appropriate options. See the following list of options and their descriptions.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t $training_mode -m Llama-2-13B -p BF16 -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                       Description
  ------------------------------------------------------------- ------------------------------------------------------------- ------------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`finetune_fw`{.docutils .literal .notranslate}]{.pre}        Full weight fine-tuning (BF16 supported)
                                                                [`finetune_lora`{.docutils .literal .notranslate}]{.pre}      LoRA fine-tuning (BF16 supported)
                                                                [`finetune_qlora`{.docutils .literal .notranslate}]{.pre}     QLoRA fine-tuning (BF16 supported)
                                                                [`HF_finetune_lora`{.docutils .literal .notranslate}]{.pre}   LoRA fine-tuning with Hugging Face PEFT
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre}               All models support BF16.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Between 2048 and 16384.                                       Sequence length for the language model.
:::

::: {.admonition .note}
Note

Llama 2 13B currently supports the following fine-tuning methods:

- [`finetune_fw`{.docutils .literal .notranslate}]{.pre}

- [`finetune_lora`{.docutils .literal .notranslate}]{.pre}

The upstream [torchtune](https://github.com/pytorch/torchtune){.reference .external} repository does not currently provide YAML configuration files for other combinations of model to fine-tuning method However, you can still configure your own YAML files to enable support for fine-tuning methods not listed here by following existing patterns in the [`/workspace/torchtune/recipes/configs`{.docutils .literal .notranslate}]{.pre} directory.
:::
:::::::

::::::: {.model-doc .pyt-train-llama-2-70b .docutils .container}
Fine-tuning

To start the fine-tuning benchmark, use the following command with the appropriate options. See the following list of options and their descriptions.

:::: {.highlight-shell .notranslate}
::: highlight
    ./pytorch_benchmark_report.sh -t $training_mode -m Llama-2-70B -p BF16 -s $sequence_length
:::
::::

::: pst-scrollable-table-container
  Name                                                          Options                                                       Description
  ------------------------------------------------------------- ------------------------------------------------------------- ------------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}     [`finetune_fw`{.docutils .literal .notranslate}]{.pre}        Full weight fine-tuning (BF16 supported)
                                                                [`finetune_lora`{.docutils .literal .notranslate}]{.pre}      LoRA fine-tuning (BF16 supported)
                                                                [`finetune_qlora`{.docutils .literal .notranslate}]{.pre}     QLoRA fine-tuning (BF16 supported)
                                                                [`HF_finetune_lora`{.docutils .literal .notranslate}]{.pre}   LoRA fine-tuning with Hugging Face PEFT
  [`$datatype`{.docutils .literal .notranslate}]{.pre}          [`BF16`{.docutils .literal .notranslate}]{.pre}               All models support BF16.
  [`$sequence_length`{.docutils .literal .notranslate}]{.pre}   Between 2048 and 16384.                                       Sequence length for the language model.
:::

::: {.admonition .note}
Note

Llama 2 70B currently supports the following fine-tuning methods:

- [`finetune_lora`{.docutils .literal .notranslate}]{.pre}

- [`finetune_qlora`{.docutils .literal .notranslate}]{.pre}

- [`HF_finetune_lora`{.docutils .literal .notranslate}]{.pre}

The upstream [torchtune](https://github.com/pytorch/torchtune){.reference .external} repository does not currently provide YAML configuration files for other combinations of model to fine-tuning method However, you can still configure your own YAML files to enable support for fine-tuning methods not listed here by following existing patterns in the [`/workspace/torchtune/recipes/configs`{.docutils .literal .notranslate}]{.pre} directory.

Benchmarking examples

For examples of benchmarking commands, see [ROCm/MAD](https://github.com/ROCm/MAD/tree/develop/benchmark/pytorch_train#benchmarking-examples){.github .reference .external}.
:::
:::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

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
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: prev-next-area
:::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::: {.bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {.page-toc .tocsection .onthispage}
Contents
:::

- [Supported models](#supported-models){.reference .internal .nav-link}
  - [Performance measurements](#performance-measurements){.reference .internal .nav-link}
  - [System validation](#system-validation){.reference .internal .nav-link}
  - [Benchmarking](#benchmarking){.reference .internal .nav-link}
- [Further reading](#further-reading){.reference .internal .nav-link}
- [Previous versions](#previous-versions){.reference .internal .nav-link}
::::
:::::
::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
