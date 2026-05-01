---
title: "Training MPT-30B with LLM Foundry on ROCm"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/training/benchmark-docker/mpt-llm-foundry.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-01
---

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-content
:::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-article-container
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
- Training\...
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
# Training MPT-30B with LLM Foundry on ROCm

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [System validation](#system-validation){.reference .internal .nav-link}
- [Getting started](#getting-started){.reference .internal .nav-link}
- [Interpreting the output](#interpreting-the-output){.reference .internal .nav-link}
- [Further reading](#further-reading){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

::::::::::::::::::::::::::::::::::::::: {#training-mpt-30b-with-llm-foundry-on-rocm .section}
# Training MPT-30B with LLM Foundry on ROCm[\#](#training-mpt-30b-with-llm-foundry-on-rocm "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 6 min read time
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

MPT-30B is a 30-billion parameter decoder-style transformer-based model from the Mosaic Pretrained Transformer (MPT) family -- learn more about it in MosaicML's research blog [MPT-30B: Raising the bar for open-source foundation models](https://www.databricks.com/blog/mpt-30b){.reference .external}.

ROCm and [ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external} provide a pre-configured training environment for the MPT-30B model using the [`rocm/pytorch-training:v25.5`{.docutils .literal .notranslate}]{.pre} base [Docker image](https://hub.docker.com/layers/rocm/pytorch-training/v25.5/images/sha256-d47850a9b25b4a7151f796a8d24d55ea17bba545573f0d50d54d3852f96ecde5){.reference .external} and the [LLM Foundry](https://github.com/mosaicml/llm-foundry){.reference .external} framework. This environment packages the following software components to train on AMD Instinct MI300X Series GPUs:

::: pst-scrollable-table-container
  Software component   Version
  -------------------- --------------------
  ROCm                 6.3.4
  PyTorch              2.7.0a0+git6374332
  Flash Attention      3.0.0.post1
:::

Using this image, you can build, run, and test the training process for MPT-30B with access to detailed logs and performance metrics.

::: {#system-validation .section}
## System validation[\#](#system-validation "Link to this heading"){.headerlink}

Before running AI workloads, it's important to validate that your AMD hardware is configured correctly and performing optimally.

If you have already validated your system settings, including aspects like NUMA auto-balancing, you can skip this step. Otherwise, complete the procedures in the [[System validation and optimization]{.std .std-ref}](../../system-setup/prerequisite-system-validation.html#rocm-for-ai-system-optimization){.reference .internal} guide to properly configure your system settings before starting training.

To test for optimal performance, consult the recommended [[System health benchmarks]{.std .std-ref}](../../system-setup/system-health-check.html#rocm-for-ai-system-health-bench){.reference .internal}. This suite of tests will help you verify and fine-tune your system's configuration.
:::

::::::::::::::::::::::::: {#getting-started .section}
## Getting started[\#](#getting-started "Link to this heading"){.headerlink}

The following procedures help you set up the training environment in a reproducible Docker container. This training environment is tailored for training MPT-30B using LLM Foundry and the specific model configurations outlined. Other configurations and run conditions outside those described in this document are not validated.

:::::::::::::::::::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

::::::::::: {.sd-tab-content .docutils}
On your host machine, clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages.

:::: {.highlight-shell .notranslate}
::: highlight
    git clone https://github.com/ROCm/MAD
    cd MAD
    pip install -r requirements.txt
:::
::::

Use this command to initiate the MPT-30B training benchmark.

:::: {.highlight-shell .notranslate}
::: highlight
    madengine run \
        --tags pyt_mpt30b_training \
        --keep-model-dir \
        --live-output \
        --clean-docker-cache
:::
::::

::::: {.admonition .tip}
Tip

If you experience data download failures, set the [`MAD_SECRETS_HFTOKEN`{.docutils .literal .notranslate}]{.pre} variable to your Hugging Face access token. See [User access tokens](https://huggingface.co/docs/hub/security-tokens){.reference .external} for details.

:::: {.highlight-shell .notranslate}
::: highlight
    export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
:::
::::
:::::

::: {.admonition .note}
Note

For improved performance (training throughput), consider enabling TunableOp. By default, [`pyt_mpt30b_training`{.docutils .literal .notranslate}]{.pre} runs with TunableOp disabled. To enable it, run [`madengine`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`run`{.docutils .literal .notranslate}]{.pre} with the [`--tunableop`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`on`{.docutils .literal .notranslate}]{.pre} argument or edit the [`models.json`{.docutils .literal .notranslate}]{.pre} configuration before running training.

Although this might increase the initial training time, it can result in a performance gain.
:::
:::::::::::

Standalone benchmarking

:::::::::::::: {.sd-tab-content .docutils}
To set up the training environment, clone the [ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external} repo and build the Docker image. In this snippet, the image is named [`mosaic_mpt30_image`{.docutils .literal .notranslate}]{.pre}.

:::: {.highlight-shell .notranslate}
::: highlight
    git clone https://github.com/ROCm/MAD
    cd MAD

    docker build --build-arg MAD_SYSTEM_GPU_ARCHITECTURE=gfx942 -f docker/pyt_mpt30b_training.ubuntu.amd.Dockerfile -t mosaic_mpt30_image .
:::
::::

Start a [`mosaic_mpt30_image`{.docutils .literal .notranslate}]{.pre} container using the following command.

:::: {.highlight-shell .notranslate}
::: highlight
    docker run -it --device=/dev/kfd --device=/dev/dri --group-add=video --ipc=host --shm-size=8G mosaic_mpt30_image
:::
::::

In the Docker container, clone the [ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external} repository and navigate to the benchmark scripts directory at [`/workspace/MAD/scripts/pyt_mpt30b_training`{.docutils .literal .notranslate}]{.pre}.

:::: {.highlight-shell .notranslate}
::: highlight
    git clone https://github.com/ROCm/MAD
    cd MAD/scripts/pyt_mpt30b_training
:::
::::

To initiate the training process, use the following command. This script uses the hyperparameters defined in [`mpt-30b-instruct.yaml`{.docutils .literal .notranslate}]{.pre}.

:::: {.highlight-shell .notranslate}
::: highlight
    source run.sh
:::
::::

::::: {.admonition .note}
Note

For improved performance (training throughput), consider enabling TunableOp. To enable it, add the [`--tunableop`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`on`{.docutils .literal .notranslate}]{.pre} flag.

:::: {.highlight-shell .notranslate}
::: highlight
    source run.sh --tunableop on
:::
::::

Although this might increase the initial training time, it can result in a performance gain.
:::::
::::::::::::::
::::::::::::::::::::::::
:::::::::::::::::::::::::

::: {#interpreting-the-output .section}
## Interpreting the output[\#](#interpreting-the-output "Link to this heading"){.headerlink}

The training output will be displayed in the terminal and simultaneously saved to the [`output.txt`{.docutils .literal .notranslate}]{.pre} file in the current directory. Key performance metrics will also be extracted and appended to the [`perf_pyt_mpt30b_training.csv`{.docutils .literal .notranslate}]{.pre} file.

Key performance metrics include:

- Training logs: Real-time display of loss metrics, accuracy, and training progress.

- Model checkpoints: Periodically saved model snapshots for potential resume or evaluation.

- Performance metrics: Detailed summaries of training speed and training loss metrics.

  - Performance (throughput/samples_per_sec)

    Overall throughput, measuring the total samples processed per second. Higher values indicate better hardware utilization.

  - Performance per device (throughput/samples_per_sec)

    Throughput on a per-device basis, showing how each GPU or CPU is performing.

  - Language Cross Entropy (metrics/train/LanguageCrossEntropy)

    Measures prediction accuracy. Lower cross entropy suggests the model's output is closer to the expected distribution.

  - Training loss (loss/train/total)

    Overall training loss. A decreasing trend indicates the model is learning effectively.
:::

::: {#further-reading .section}
## Further reading[\#](#further-reading "Link to this heading"){.headerlink}

- To learn more about MAD and the [`madengine`{.docutils .literal .notranslate}]{.pre} CLI, see the [MAD usage guide](https://github.com/ROCm/MAD?tab=readme-ov-file#usage-guide){.reference .external}.

- To learn more about system settings and management practices to configure your system for AMD Instinct MI300X Series GPUs, see [AMD Instinct MI300X system optimization](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi300x.html){.reference .external}.

- For a list of other ready-made Docker images for AI with ROCm, see [AMD Infinity Hub](https://www.amd.com/en/developer/resources/infinity-hub.html#f-amd_hub_category=AI%20%26%20ML%20Models){.reference .external}.
:::
:::::::::::::::::::::::::::::::::::::::

::::: prev-next-area
[](jax-maxtext.html "previous page"){.left-prev}

::: prev-next-info
previous

Training a model with Primus and JAX MaxText
:::

[](../scale-model-training.html "next page"){.right-next}

::: prev-next-info
next

Scaling model training
:::
:::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::: {.bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {.page-toc .tocsection .onthispage}
Contents
:::

- [System validation](#system-validation){.reference .internal .nav-link}
- [Getting started](#getting-started){.reference .internal .nav-link}
- [Interpreting the output](#interpreting-the-output){.reference .internal .nav-link}
- [Further reading](#further-reading){.reference .internal .nav-link}
::::
:::::
::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
