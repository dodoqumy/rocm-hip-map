---
title: "PyTorch inference performance testing"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference/benchmark-docker/pytorch-inference.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-01
---

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-content
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-article-container
:::::::::: {.bd-header-article .d-print-none}
::::::::: {.header-article-items .header-article__inner}
::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}
:::

::: header-article-item
- [](../../../../index.html){.nav-link aria-label="Home"}
- [Use ROCm for AI](../../index.html){.nav-link}
- [Use ROCm for AI inference](../index.html){.nav-link}
- PyTorch\...
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
# PyTorch inference performance testing

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [Supported models](#supported-models){.reference .internal .nav-link}
- [System validation](#system-validation){.reference .internal .nav-link}
- [Pull the Docker image](#pull-the-docker-image){.reference .internal .nav-link}
- [Benchmarking](#benchmarking){.reference .internal .nav-link}
- [Further reading](#further-reading){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#pytorch-inference-performance-testing .section}
# PyTorch inference performance testing[\#](#pytorch-inference-performance-testing "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 11 min read time
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

The [ROCm PyTorch Docker](https://hub.docker.com/r/rocm/pytorch/tags){.reference .external} image offers a prebuilt, optimized environment for testing model inference performance on AMD Instinct™ MI300X Series GPUs. This guide demonstrates how to use the AMD Model Automation and Dashboarding (MAD) tool with the ROCm PyTorch container to test inference performance on various models efficiently.

:::::::::::::::::::::::::::::::::: {#supported-models .section}
[]{#pytorch-inference-benchmark-available-models}

## Supported models[\#](#supported-models "Link to this heading"){.headerlink}

The following models are supported for inference performance benchmarking with PyTorch and ROCm. Some instructions, commands, and recommendations in this documentation might vary by model -- select one to get started.

::::::::::::::::::::: {#vllm-benchmark-ud-params-picker .container-fluid}
::::::::::: {.row .gx-0}
::: {.col-2 .me-1 .px-2 .model-param-head}
Model
:::

::::::::: {.row .col-10 .pe-0}
::: {.col-3 .px-2 .model-param param-k="model-group" param-v="clip" tabindex="0"}
CLIP
:::

::: {.col-3 .px-2 .model-param param-k="model-group" param-v="chai" tabindex="0"}
Chai-1
:::

::: {.col-3 .px-2 .model-param param-k="model-group" param-v="mochi" tabindex="0"}
Mochi Video
:::

::: {.col-3 .px-2 .model-param param-k="model-group" param-v="wan" tabindex="0"}
Wan2.1
:::

::: {.col-3 .px-2 .model-param param-k="model-group" param-v="janus-pro" tabindex="0"}
Janus Pro
:::

::: {.col-3 .px-2 .model-param param-k="model-group" param-v="hunyuan" tabindex="0"}
Hunyuan Video
:::
:::::::::
:::::::::::

::::::::::: {.row .gx-0 .pt-1 style="display: none;"}
::: {.col-2 .me-1 .px-2 .model-param-head}
Variant
:::

::::::::: {.row .col-10 .pe-0}
::: {.col-6 .px-2 .model-param param-group="clip" param-k="model" param-v="pyt_clip_inference" tabindex="0"}
CLIP
:::

::: {.col-6 .px-2 .model-param param-group="chai" param-k="model" param-v="pyt_chai1_inference" tabindex="0"}
Chai-1
:::

::: {.col-6 .px-2 .model-param param-group="mochi" param-k="model" param-v="pyt_mochi_video_inference" tabindex="0"}
Mochi 1
:::

::: {.col-6 .px-2 .model-param param-group="wan" param-k="model" param-v="pyt_wan2.1_inference" tabindex="0"}
Wan2.1
:::

::: {.col-6 .px-2 .model-param param-group="janus-pro" param-k="model" param-v="pyt_janus_pro_inference" tabindex="0"}
Janus Pro 7B
:::

::: {.col-6 .px-2 .model-param param-group="hunyuan" param-k="model" param-v="pyt_hy_video" tabindex="0"}
Hunyuan Video
:::
:::::::::
:::::::::::
:::::::::::::::::::::

:::: {.model-doc .pyt-clip-inference .docutils .container}
::: {.admonition .note}
Note

See the [CLIP model card on Hugging Face](https://huggingface.co/laion/CLIP-ViT-B-32-laion2B-s34B-b79K){.reference .external} to learn more about your selected model. Some models require access authorization before use via an external license agreement through a third party.
:::
::::

:::: {.model-doc .pyt-chai1-inference .docutils .container}
::: {.admonition .note}
Note

See the [Chai-1 model card on Hugging Face](https://huggingface.co/chaidiscovery/chai-1){.reference .external} to learn more about your selected model. Some models require access authorization before use via an external license agreement through a third party.
:::
::::

:::: {.model-doc .pyt-mochi-video-inference .docutils .container}
::: {.admonition .note}
Note

See the [Mochi 1 model card on Hugging Face](https://huggingface.co/genmo/mochi-1-preview){.reference .external} to learn more about your selected model. Some models require access authorization before use via an external license agreement through a third party.
:::
::::

:::: {.model-doc .pyt-wan2-1-inference .docutils .container}
::: {.admonition .note}
Note

See the [Wan2.1 model card on Hugging Face](https://huggingface.co/Wan-AI/Wan2.1-T2V-14B){.reference .external} to learn more about your selected model. Some models require access authorization before use via an external license agreement through a third party.
:::
::::

:::: {.model-doc .pyt-janus-pro-inference .docutils .container}
::: {.admonition .note}
Note

See the [Janus Pro 7B model card on Hugging Face](https://huggingface.co/deepseek-ai/Janus-Pro-7B){.reference .external} to learn more about your selected model. Some models require access authorization before use via an external license agreement through a third party.
:::
::::

:::: {.model-doc .pyt-hy-video .docutils .container}
::: {.admonition .note}
Note

See the [Hunyuan Video model card on Hugging Face](https://huggingface.co/tencent/HunyuanVideo){.reference .external} to learn more about your selected model. Some models require access authorization before use via an external license agreement through a third party.
:::
::::
::::::::::::::::::::::::::::::::::

::::: {#system-validation .section}
## System validation[\#](#system-validation "Link to this heading"){.headerlink}

Before running AI workloads, it's important to validate that your AMD hardware is configured correctly and performing optimally.

To optimize performance, disable automatic NUMA balancing. Otherwise, the GPU might hang until the periodic balancing is finalized. For more information, see the [[system validation steps]{.std .std-ref}](../../system-setup/prerequisite-system-validation.html#rocm-for-ai-system-optimization){.reference .internal}.

:::: {.highlight-shell .notranslate}
::: highlight
    # disable automatic NUMA balancing
    sh -c 'echo 0 > /proc/sys/kernel/numa_balancing'
    # check if NUMA balancing is disabled (returns 0 if disabled)
    cat /proc/sys/kernel/numa_balancing
    0
:::
::::

To test for optimal performance, consult the recommended [[System health benchmarks]{.std .std-ref}](../../system-setup/system-health-check.html#rocm-for-ai-system-health-bench){.reference .internal}. This suite of tests will help you verify and fine-tune your system's configuration.
:::::

:::::::::: {#pull-the-docker-image .section}
## Pull the Docker image[\#](#pull-the-docker-image "Link to this heading"){.headerlink}

:::::: {.model-doc .pyt-chai1-inference .docutils .container}
Use the following command to pull the [ROCm PyTorch Docker image](https://hub.docker.com/layers/rocm/pytorch/rocm6.2.3_ubuntu22.04_py3.10_pytorch_release_2.3.0_triton_llvm_reg_issue/images/sha256-b736a4239ab38a9d0e448af6d4adca83b117debed00bfbe33846f99c4540f79b){.reference .external} from Docker Hub.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/pytorch:rocm6.2.3_ubuntu22.04_py3.10_pytorch_release_2.3.0_triton_llvm_reg_issue
:::
::::

::: {.admonition .note}
Note

The Chai-1 benchmark uses a specifically selected Docker image using ROCm 6.2.3 and PyTorch 2.3.0 to address an accuracy issue.
:::
::::::

::::: {.model-doc .pyt-clip-inference .pyt-mochi-video-inference .pyt-wan2-1-inference .pyt-janus-pro-inference .pyt-hy-video .docutils .container}
Use the following command to pull the [ROCm PyTorch Docker image](https://hub.docker.com/layers/rocm/pytorch/latest/images/sha256-05b55983e5154f46e7441897d0908d79877370adca4d1fff4899d9539d6c4969){.reference .external} from Docker Hub.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/pytorch:latest
:::
::::
:::::
::::::::::

:::::::::::::::::::::::::::::::::::::: {#benchmarking .section}
[]{#pytorch-benchmark-get-started}

## Benchmarking[\#](#benchmarking "Link to this heading"){.headerlink}

:::::::: {#pytorch-inference-benchmark-mad .model-doc .pyt-clip-inference .docutils .container}
To simplify performance testing, the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) project provides ready-to-use scripts and configuration. To start, clone the MAD repository to a local directory and install the required packages on the host machine.

:::: {.highlight-shell .notranslate}
::: highlight
    git clone https://github.com/ROCm/MAD
    cd MAD
    pip install -r requirements.txt
:::
::::

Use this command to run the performance benchmark test on the [CLIP](https://huggingface.co/laion/CLIP-ViT-B-32-laion2B-s34B-b79K){.reference .external} model using one GPU with the [`float16`{.docutils .literal .notranslate}]{.pre} data type on the host machine.

:::: {.highlight-shell .notranslate}
::: highlight
    export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
    madengine run \
        --tags pyt_clip_inference \
        --keep-model-dir \
        --live-output \
        --timeout 28800
:::
::::

MAD launches a Docker container with the name [`container_ci-pyt_clip_inference`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in [`perf_pyt_clip_inference.csv`{.docutils .literal .notranslate}]{.pre}.

::: {.admonition .note}
Note

For improved performance, consider enabling TunableOp. By default, [`pyt_clip_inference`{.docutils .literal .notranslate}]{.pre} runs with TunableOp disabled (see [ROCm/MAD](https://github.com/ROCm/MAD/blob/develop/models.json){.github .reference .external}). To enable it, include the [`--tunableop`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`on`{.docutils .literal .notranslate}]{.pre} argument in your run.

Enabling TunableOp triggers a two-pass run -- a warm-up followed by the performance-collection run. Although this might increase the initial training time, it can result in a performance gain.
:::
::::::::

:::::::: {.model-doc .pyt-chai1-inference .docutils .container}
To simplify performance testing, the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) project provides ready-to-use scripts and configuration. To start, clone the MAD repository to a local directory and install the required packages on the host machine.

:::: {.highlight-shell .notranslate}
::: highlight
    git clone https://github.com/ROCm/MAD
    cd MAD
    pip install -r requirements.txt
:::
::::

Use this command to run the performance benchmark test on the [Chai-1](https://huggingface.co/chaidiscovery/chai-1){.reference .external} model using one GPU with the [`float16`{.docutils .literal .notranslate}]{.pre} data type on the host machine.

:::: {.highlight-shell .notranslate}
::: highlight
    export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
    madengine run \
        --tags pyt_chai1_inference \
        --keep-model-dir \
        --live-output \
        --timeout 28800
:::
::::

MAD launches a Docker container with the name [`container_ci-pyt_chai1_inference`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in [`perf_pyt_chai1_inference.csv`{.docutils .literal .notranslate}]{.pre}.

::: {.admonition .note}
Note

For improved performance, consider enabling TunableOp. By default, [`pyt_chai1_inference`{.docutils .literal .notranslate}]{.pre} runs with TunableOp disabled (see [ROCm/MAD](https://github.com/ROCm/MAD/blob/develop/models.json){.github .reference .external}). To enable it, include the [`--tunableop`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`on`{.docutils .literal .notranslate}]{.pre} argument in your run.

Enabling TunableOp triggers a two-pass run -- a warm-up followed by the performance-collection run. Although this might increase the initial training time, it can result in a performance gain.
:::
::::::::

:::::::: {.model-doc .pyt-mochi-video-inference .docutils .container}
To simplify performance testing, the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) project provides ready-to-use scripts and configuration. To start, clone the MAD repository to a local directory and install the required packages on the host machine.

:::: {.highlight-shell .notranslate}
::: highlight
    git clone https://github.com/ROCm/MAD
    cd MAD
    pip install -r requirements.txt
:::
::::

Use this command to run the performance benchmark test on the [Mochi 1](https://huggingface.co/genmo/mochi-1-preview){.reference .external} model using one GPU with the [`float16`{.docutils .literal .notranslate}]{.pre} data type on the host machine.

:::: {.highlight-shell .notranslate}
::: highlight
    export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
    madengine run \
        --tags pyt_mochi_video_inference \
        --keep-model-dir \
        --live-output \
        --timeout 28800
:::
::::

MAD launches a Docker container with the name [`container_ci-pyt_mochi_video_inference`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in [`perf_pyt_mochi_video_inference.csv`{.docutils .literal .notranslate}]{.pre}.

::: {.admonition .note}
Note

For improved performance, consider enabling TunableOp. By default, [`pyt_mochi_video_inference`{.docutils .literal .notranslate}]{.pre} runs with TunableOp disabled (see [ROCm/MAD](https://github.com/ROCm/MAD/blob/develop/models.json){.github .reference .external}). To enable it, include the [`--tunableop`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`on`{.docutils .literal .notranslate}]{.pre} argument in your run.

Enabling TunableOp triggers a two-pass run -- a warm-up followed by the performance-collection run. Although this might increase the initial training time, it can result in a performance gain.
:::
::::::::

:::::::: {.model-doc .pyt-wan2-1-inference .docutils .container}
To simplify performance testing, the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) project provides ready-to-use scripts and configuration. To start, clone the MAD repository to a local directory and install the required packages on the host machine.

:::: {.highlight-shell .notranslate}
::: highlight
    git clone https://github.com/ROCm/MAD
    cd MAD
    pip install -r requirements.txt
:::
::::

Use this command to run the performance benchmark test on the [Wan2.1](https://huggingface.co/Wan-AI/Wan2.1-T2V-14B){.reference .external} model using one GPU with the [`bfloat16`{.docutils .literal .notranslate}]{.pre} data type on the host machine.

:::: {.highlight-shell .notranslate}
::: highlight
    export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
    madengine run \
        --tags pyt_wan2.1_inference \
        --keep-model-dir \
        --live-output \
        --timeout 28800
:::
::::

MAD launches a Docker container with the name [`container_ci-pyt_wan2.1_inference`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in [`perf_pyt_wan2.1_inference.csv`{.docutils .literal .notranslate}]{.pre}.

::: {.admonition .note}
Note

For improved performance, consider enabling TunableOp. By default, [`pyt_wan2.1_inference`{.docutils .literal .notranslate}]{.pre} runs with TunableOp disabled (see [ROCm/MAD](https://github.com/ROCm/MAD/blob/develop/models.json){.github .reference .external}). To enable it, include the [`--tunableop`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`on`{.docutils .literal .notranslate}]{.pre} argument in your run.

Enabling TunableOp triggers a two-pass run -- a warm-up followed by the performance-collection run. Although this might increase the initial training time, it can result in a performance gain.
:::
::::::::

::::::: {.model-doc .pyt-janus-pro-inference .docutils .container}
To simplify performance testing, the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) project provides ready-to-use scripts and configuration. To start, clone the MAD repository to a local directory and install the required packages on the host machine.

:::: {.highlight-shell .notranslate}
::: highlight
    git clone https://github.com/ROCm/MAD
    cd MAD
    pip install -r requirements.txt
:::
::::

Use this command to run the performance benchmark test on the [Janus Pro 7B](https://huggingface.co/deepseek-ai/Janus-Pro-7B){.reference .external} model using one GPU with the [`bfloat16`{.docutils .literal .notranslate}]{.pre} data type on the host machine.

:::: {.highlight-shell .notranslate}
::: highlight
    export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
    madengine run \
        --tags pyt_janus_pro_inference \
        --keep-model-dir \
        --live-output \
        --timeout 28800
:::
::::

MAD launches a Docker container with the name [`container_ci-pyt_janus_pro_inference`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in [`perf_pyt_janus_pro_inference.csv`{.docutils .literal .notranslate}]{.pre}.
:::::::

:::::::: {.model-doc .pyt-hy-video .docutils .container}
To simplify performance testing, the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) project provides ready-to-use scripts and configuration. To start, clone the MAD repository to a local directory and install the required packages on the host machine.

:::: {.highlight-shell .notranslate}
::: highlight
    git clone https://github.com/ROCm/MAD
    cd MAD
    pip install -r requirements.txt
:::
::::

Use this command to run the performance benchmark test on the [Hunyuan Video](https://huggingface.co/tencent/HunyuanVideo){.reference .external} model using one GPU with the [`float16`{.docutils .literal .notranslate}]{.pre} data type on the host machine.

:::: {.highlight-shell .notranslate}
::: highlight
    export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
    madengine run \
        --tags pyt_hy_video \
        --keep-model-dir \
        --live-output \
        --timeout 28800
:::
::::

MAD launches a Docker container with the name [`container_ci-pyt_hy_video`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in [`perf_pyt_hy_video.csv`{.docutils .literal .notranslate}]{.pre}.

::: {.admonition .note}
Note

For improved performance, consider enabling TunableOp. By default, [`pyt_hy_video`{.docutils .literal .notranslate}]{.pre} runs with TunableOp disabled (see [ROCm/MAD](https://github.com/ROCm/MAD/blob/develop/models.json){.github .reference .external}). To enable it, include the [`--tunableop`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`on`{.docutils .literal .notranslate}]{.pre} argument in your run.

Enabling TunableOp triggers a two-pass run -- a warm-up followed by the performance-collection run. Although this might increase the initial training time, it can result in a performance gain.
:::
::::::::
::::::::::::::::::::::::::::::::::::::

::: {#further-reading .section}
## Further reading[\#](#further-reading "Link to this heading"){.headerlink}

- To learn more about MAD and the [`madengine`{.docutils .literal .notranslate}]{.pre} CLI, see the [MAD usage guide](https://github.com/ROCm/MAD?tab=readme-ov-file#usage-guide){.reference .external}.

- To learn more about system settings and management practices to configure your system for AMD Instinct MI300X Series GPUs, see [AMD Instinct MI300X system optimization](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi300x.html){.reference .external}.

- For application performance optimization strategies for HPC and AI workloads, including inference with vLLM, see [[AMD Instinct MI300X workload optimization]{.doc}](../../inference-optimization/workload.html){.reference .internal}.

- To learn how to run LLM models from Hugging Face or your model, see [[Running models from Hugging Face]{.doc}](../hugging-face-models.html){.reference .internal}.

- To learn how to optimize inference on LLMs, see [[Inference optimization]{.doc}](../../inference-optimization/index.html){.reference .internal}.

- To learn how to fine-tune LLMs, see [[Fine-tuning LLMs]{.doc}](../../fine-tuning/index.html){.reference .internal}.
:::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::: prev-next-area
[](vllm.html "previous page"){.left-prev}

::: prev-next-info
previous

vLLM inference
:::

[](sglang.html "next page"){.right-next}

::: prev-next-info
next

SGLang inference performance testing DeepSeek-R1-Distill-Qwen-32B
:::
:::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::: {.bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {.page-toc .tocsection .onthispage}
Contents
:::

- [Supported models](#supported-models){.reference .internal .nav-link}
- [System validation](#system-validation){.reference .internal .nav-link}
- [Pull the Docker image](#pull-the-docker-image){.reference .internal .nav-link}
- [Benchmarking](#benchmarking){.reference .internal .nav-link}
- [Further reading](#further-reading){.reference .internal .nav-link}
::::
:::::
::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
