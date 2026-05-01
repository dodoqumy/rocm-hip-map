---
title: "Training a model with JAX MaxText on ROCm"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/training/benchmark-docker/previous-versions/jax-maxtext-v25.9.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-01
---

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-content
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-article-container
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
# Training a model with JAX MaxText on ROCm

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [Supported models](#supported-models){.reference .internal .nav-link}
- [System validation](#system-validation){.reference .internal .nav-link}
- [Environment setup](#environment-setup){.reference .internal .nav-link}
  - [Pull the Docker image](#pull-the-docker-image){.reference .internal .nav-link}
  - [Multi-node configuration](#multi-node-configuration){.reference .internal .nav-link}
- [Benchmarking](#benchmarking){.reference .internal .nav-link}
- [Further reading](#further-reading){.reference .internal .nav-link}
- [Previous versions](#previous-versions){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#training-a-model-with-jax-maxtext-on-rocm .section}
# Training a model with JAX MaxText on ROCm[\#](#training-a-model-with-jax-maxtext-on-rocm "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-04-21
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

::: {.admonition .caution}
Caution

This documentation does not reflect the latest version of ROCm JAX MaxText training performance documentation. See [[Training a model with Primus and JAX MaxText]{.doc}](../jax-maxtext.html){.reference .internal} for the latest version.
:::

::: {.admonition .note}
Note

We have refreshed the [`rocm/jax-training:maxtext-v25.9`{.docutils .literal .notranslate}]{.pre} image as rocm/jax-training:maxtext-v25.9.1. This should include a fix to address segmentation fault issues during launch.
:::

The MaxText for ROCm training Docker image provides a prebuilt environment for training on AMD Instinct MI355X, MI350X, MI325X, and MI300X GPUs, including essential components like JAX, XLA, ROCm libraries, and MaxText utilities. It includes the following software components:

::::: {.sd-tab-set .docutils}
[`rocm/jax-training:maxtext-v25.9.1`{.docutils .literal .notranslate}]{.pre}

:::: {.sd-tab-content .docutils}
::: pst-scrollable-table-container
  Software component   Version
  -------------------- ---------------------
  ROCm                 7.0.0
  JAX                  0.6.2
  Python               3.10.18
  Transformer Engine   2.2.0.dev0+c91bac54
  hipBLASLt            1.x.x
:::
::::
:::::

MaxText with on ROCm provides the following key features to train large language models efficiently:

- Transformer Engine (TE)

- Flash Attention (FA) 3 -- with or without sequence input packing

- GEMM tuning

- Multi-node support

- NANOO FP8 (for MI300X series GPUs) and FP8 (for MI355X and MI350X) quantization support

::::::::::::::::::::::: {#supported-models .section}
[]{#amd-maxtext-model-support-v259}

## Supported models[\#](#supported-models "Link to this heading"){.headerlink}

The following models are pre-optimized for performance on AMD Instinct GPUs. Some instructions, commands, and available training configurations in this documentation might vary by model -- select one to get started.

::::::::::::::::::::: {#vllm-benchmark-ud-params-picker .container-fluid}
:::::::: {.row .gx-0}
::: {.col-2 .me-1 .px-2 .model-param-head}
Model
:::

:::::: {.row .col-10 .pe-0}
::: {.col-4 .px-2 .model-param param-k="model-group" param-v="llama" tabindex="0"}
Meta Llama
:::

::: {.col-4 .px-2 .model-param param-k="model-group" param-v="deepseek" tabindex="0"}
DeepSeek
:::

::: {.col-4 .px-2 .model-param param-k="model-group" param-v="mistral" tabindex="0"}
Mistral AI
:::
::::::
::::::::

:::::::::::::: {.row .gx-0 .pt-1}
::: {.col-2 .me-1 .px-2 .model-param-head}
Variant
:::

:::::::::::: {.row .col-10 .pe-0}
::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="jax_maxtext_train_llama-2-7b" tabindex="0"}
Llama 2 7B
:::

::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="jax_maxtext_train_llama-2-70b" tabindex="0"}
Llama 2 70B
:::

::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="jax_maxtext_train_llama-3-8b" tabindex="0"}
Llama 3 8B (multi-node)
:::

::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="jax_maxtext_train_llama-3-70b" tabindex="0"}
Llama 3 70B (multi-node)
:::

::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="jax_maxtext_train_llama-3.1-8b" tabindex="0"}
Llama 3.1 8B
:::

::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="jax_maxtext_train_llama-3.1-70b" tabindex="0"}
Llama 3.1 70B
:::

::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="jax_maxtext_train_llama-3.3-70b" tabindex="0"}
Llama 3.3 70B
:::

::: {.col-6 .px-2 .model-param param-group="deepseek" param-k="model" param-v="jax_maxtext_train_deepseek-v2-lite-16b" tabindex="0"}
DeepSeek-V2-Lite (16B)
:::

::: {.col-6 .px-2 .model-param param-group="mistral" param-k="model" param-v="jax_maxtext_train_mixtral-8x7b" tabindex="0"}
Mixtral 8x7B
:::
::::::::::::
::::::::::::::
:::::::::::::::::::::

::: {.admonition .note}
Note

Some models, such as Llama 3, require an external license agreement through a third party (for example, Meta).
:::
:::::::::::::::::::::::

::: {#system-validation .section}
## System validation[\#](#system-validation "Link to this heading"){.headerlink}

Before running AI workloads, it's important to validate that your AMD hardware is configured correctly and performing optimally.

If you have already validated your system settings, including aspects like NUMA auto-balancing, you can skip this step. Otherwise, complete the procedures in the [[System validation and optimization]{.std .std-ref}](../../../system-setup/prerequisite-system-validation.html#rocm-for-ai-system-optimization){.reference .internal} guide to properly configure your system settings before starting training.

To test for optimal performance, consult the recommended [[System health benchmarks]{.std .std-ref}](../../../system-setup/system-health-check.html#rocm-for-ai-system-health-bench){.reference .internal}. This suite of tests will help you verify and fine-tune your system's configuration.
:::

::::::: {#environment-setup .section}
## Environment setup[\#](#environment-setup "Link to this heading"){.headerlink}

This Docker image is optimized for specific model configurations outlined as follows. Performance can vary for other training workloads, as AMD doesn't validate configurations and run conditions outside those described.

::::: {#pull-the-docker-image .section}
### Pull the Docker image[\#](#pull-the-docker-image "Link to this heading"){.headerlink}

Use the following command to pull the Docker image from Docker Hub.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/jax-training:maxtext-v25.9.1
:::
::::
:::::

::: {#multi-node-configuration .section}
[]{#amd-maxtext-multi-node-setup-v259}

### Multi-node configuration[\#](#multi-node-configuration "Link to this heading"){.headerlink}

See [[Multi-node setup for AI workloads]{.doc}](../../../system-setup/multi-node-setup.html){.reference .internal} to configure your environment for multi-node training.
:::
:::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#benchmarking .section}
[]{#amd-maxtext-get-started-v259}

## Benchmarking[\#](#benchmarking "Link to this heading"){.headerlink}

Once the setup is complete, choose between two options to reproduce the benchmark results:

::::::::: {#vllm-benchmark-mad .model-doc .jax-maxtext-train-llama-2-7b .docutils .container}
:::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to Llama 2 7B. See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v259){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  Use this command to run the performance benchmark test on the Llama 2 7B model using one GPU with the [`bf16`{.docutils .literal .notranslate}]{.pre} data type on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags jax_maxtext_train_llama-2-7b \
            --keep-model-dir \
            --live-output \
            --timeout 28800
    :::
    ::::

MAD launches a Docker container with the name [`container_ci-jax_maxtext_train_llama-2-7b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in the following path: [`~/MAD/perf.csv/`{.docutils .literal .notranslate}]{.pre}.
:::

Standalone benchmarking

:::::: {.sd-tab-content .docutils}
The following commands are optimized for Llama 2 7B. See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v259){.reference .internal} to switch to another available model. Some instructions and resources might not be available for all models and configurations.

Download the Docker image and required scripts

Run the JAX MaxText benchmark tool independently by starting the Docker container as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/jax-training:maxtext-v25.9.1
:::
::::

Single node training

1.  Set up environment variables.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN=<Your Hugging Face token>
        export HF_HOME=<Location of saved/cached Hugging Face models>
    :::
    ::::

    [`MAD_SECRETS_HFTOKEN`{.docutils .literal .notranslate}]{.pre} is your Hugging Face access token to access models, tokenizers, and data. See [User access tokens](https://huggingface.co/docs/hub/en/security-tokens){.reference .external}.

    [`HF_HOME`{.docutils .literal .notranslate}]{.pre} is where [`huggingface_hub`{.docutils .literal .notranslate}]{.pre} will store local data. See [huggingface_hub CLI](https://huggingface.co/docs/huggingface_hub/main/en/guides/cli#huggingface-cli-download){.reference .external}. If you already have downloaded or cached Hugging Face artifacts, set this variable to that path. Downloaded files typically get cached to [`~/.cache/huggingface`{.docutils .literal .notranslate}]{.pre}.

2.  Launch the Docker container.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker run -it \
            --device=/dev/dri \
            --device=/dev/kfd \
            --network host \
            --ipc host \
            --group-add video \
            --cap-add=SYS_PTRACE \
            --security-opt seccomp=unconfined \
            --privileged \
            -v $HOME:$HOME \
            -v $HOME/.ssh:/root/.ssh \
            -v $HF_HOME:/hf_cache \
            -e HF_HOME=/hf_cache \
            -e MAD_SECRETS_HFTOKEN=$MAD_SECRETS_HFTOKEN
            --shm-size 64G \
            --name training_env \
            rocm/jax-training:maxtext-v25.9.1
    :::
    ::::

3.  In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at [`MAD/scripts/jax-maxtext`{.docutils .literal .notranslate}]{.pre}.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD/scripts/jax-maxtext
    :::
    ::::

4.  Run the setup scripts to install libraries and datasets needed for benchmarking.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        ./jax-maxtext_benchmark_setup.sh -m Llama-2-7B
    :::
    ::::

5.  To run the training benchmark without quantization, use the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        ./jax-maxtext_benchmark_report.sh -m Llama-2-7B
    :::
    ::::

    For quantized training, run the script with the appropriate option for your Instinct GPU.

    ::::::::: {.sd-tab-set .docutils}
    MI355X and MI350X

    ::::: {.sd-tab-content .docutils}
    For [`fp8`{.docutils .literal .notranslate}]{.pre} quantized training on MI355X and MI350X GPUs, use the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        ./jax-maxtext_benchmark_report.sh -m Llama-2-7B -q fp8
    :::
    ::::
    :::::

    MI325X and MI300X

    ::::: {.sd-tab-content .docutils}
    For [`nanoo_fp8`{.docutils .literal .notranslate}]{.pre} quantized training on MI300X series GPUs, use the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        ./jax-maxtext_benchmark_report.sh -m Llama-2-7B -q nanoo_fp8
    :::
    ::::
    :::::
    :::::::::

Multi-node training

The following examples use SLURM to run on multiple nodes.

::: {.admonition .note}
Note

The following scripts will launch the Docker container and run the benchmark. Run them outside of any Docker container.
:::

1.  Make sure [`$HF_HOME`{.docutils .literal .notranslate}]{.pre} is set before running the test. See [ROCm benchmarking](https://github.com/ROCm/MAD/blob/develop/scripts/jax-maxtext/gpu-rocm/readme.md){.reference .external} for more details on downloading the Llama models before running the benchmark.

2.  To run multi-node training for Llama 2 7B, use the [multi-node training script](https://github.com/ROCm/MAD/blob/develop/scripts/jax-maxtext/gpu-rocm/llama2_7b_multinode.sh){.reference .external} under the [`scripts/jax-maxtext/gpu-rocm/`{.docutils .literal .notranslate}]{.pre} directory.

3.  Run the multi-node training benchmark script.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        sbatch -N <num_nodes> llama2_7b_multinode.sh
    :::
    ::::
::::::
::::::::
:::::::::

::::::::: {.model-doc .jax-maxtext-train-llama-2-70b .docutils .container}
:::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to Llama 2 70B. See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v259){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  Use this command to run the performance benchmark test on the Llama 2 70B model using one GPU with the [`bf16`{.docutils .literal .notranslate}]{.pre} data type on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags jax_maxtext_train_llama-2-70b \
            --keep-model-dir \
            --live-output \
            --timeout 28800
    :::
    ::::

MAD launches a Docker container with the name [`container_ci-jax_maxtext_train_llama-2-70b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in the following path: [`~/MAD/perf.csv/`{.docutils .literal .notranslate}]{.pre}.
:::

Standalone benchmarking

:::::: {.sd-tab-content .docutils}
The following commands are optimized for Llama 2 70B. See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v259){.reference .internal} to switch to another available model. Some instructions and resources might not be available for all models and configurations.

Download the Docker image and required scripts

Run the JAX MaxText benchmark tool independently by starting the Docker container as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/jax-training:maxtext-v25.9.1
:::
::::

Single node training

1.  Set up environment variables.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN=<Your Hugging Face token>
        export HF_HOME=<Location of saved/cached Hugging Face models>
    :::
    ::::

    [`MAD_SECRETS_HFTOKEN`{.docutils .literal .notranslate}]{.pre} is your Hugging Face access token to access models, tokenizers, and data. See [User access tokens](https://huggingface.co/docs/hub/en/security-tokens){.reference .external}.

    [`HF_HOME`{.docutils .literal .notranslate}]{.pre} is where [`huggingface_hub`{.docutils .literal .notranslate}]{.pre} will store local data. See [huggingface_hub CLI](https://huggingface.co/docs/huggingface_hub/main/en/guides/cli#huggingface-cli-download){.reference .external}. If you already have downloaded or cached Hugging Face artifacts, set this variable to that path. Downloaded files typically get cached to [`~/.cache/huggingface`{.docutils .literal .notranslate}]{.pre}.

2.  Launch the Docker container.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker run -it \
            --device=/dev/dri \
            --device=/dev/kfd \
            --network host \
            --ipc host \
            --group-add video \
            --cap-add=SYS_PTRACE \
            --security-opt seccomp=unconfined \
            --privileged \
            -v $HOME:$HOME \
            -v $HOME/.ssh:/root/.ssh \
            -v $HF_HOME:/hf_cache \
            -e HF_HOME=/hf_cache \
            -e MAD_SECRETS_HFTOKEN=$MAD_SECRETS_HFTOKEN
            --shm-size 64G \
            --name training_env \
            rocm/jax-training:maxtext-v25.9.1
    :::
    ::::

3.  In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at [`MAD/scripts/jax-maxtext`{.docutils .literal .notranslate}]{.pre}.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD/scripts/jax-maxtext
    :::
    ::::

4.  Run the setup scripts to install libraries and datasets needed for benchmarking.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        ./jax-maxtext_benchmark_setup.sh -m Llama-2-70B
    :::
    ::::

5.  To run the training benchmark without quantization, use the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        ./jax-maxtext_benchmark_report.sh -m Llama-2-70B
    :::
    ::::

    For quantized training, run the script with the appropriate option for your Instinct GPU.

    ::::::::: {.sd-tab-set .docutils}
    MI355X and MI350X

    ::::: {.sd-tab-content .docutils}
    For [`fp8`{.docutils .literal .notranslate}]{.pre} quantized training on MI355X and MI350X GPUs, use the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        ./jax-maxtext_benchmark_report.sh -m Llama-2-70B -q fp8
    :::
    ::::
    :::::

    MI325X and MI300X

    ::::: {.sd-tab-content .docutils}
    For [`nanoo_fp8`{.docutils .literal .notranslate}]{.pre} quantized training on MI300X series GPUs, use the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        ./jax-maxtext_benchmark_report.sh -m Llama-2-70B -q nanoo_fp8
    :::
    ::::
    :::::
    :::::::::

Multi-node training

The following examples use SLURM to run on multiple nodes.

::: {.admonition .note}
Note

The following scripts will launch the Docker container and run the benchmark. Run them outside of any Docker container.
:::

1.  Make sure [`$HF_HOME`{.docutils .literal .notranslate}]{.pre} is set before running the test. See [ROCm benchmarking](https://github.com/ROCm/MAD/blob/develop/scripts/jax-maxtext/gpu-rocm/readme.md){.reference .external} for more details on downloading the Llama models before running the benchmark.

2.  To run multi-node training for Llama 2 70B, use the [multi-node training script](https://github.com/ROCm/MAD/blob/develop/scripts/jax-maxtext/gpu-rocm/llama2_70b_multinode.sh){.reference .external} under the [`scripts/jax-maxtext/gpu-rocm/`{.docutils .literal .notranslate}]{.pre} directory.

3.  Run the multi-node training benchmark script.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        sbatch -N <num_nodes> llama2_70b_multinode.sh
    :::
    ::::
::::::
::::::::
:::::::::

:::::::: {.model-doc .jax-maxtext-train-llama-3-8b .docutils .container}
::::::: {.sd-tab-set .docutils}
Standalone benchmarking

:::::: {.sd-tab-content .docutils}
The following commands are optimized for Llama 3 8B (multi-node). See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v259){.reference .internal} to switch to another available model. Some instructions and resources might not be available for all models and configurations.

Download the Docker image and required scripts

Run the JAX MaxText benchmark tool independently by starting the Docker container as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/jax-training:maxtext-v25.9.1
:::
::::

Multi-node training

The following examples use SLURM to run on multiple nodes.

::: {.admonition .note}
Note

The following scripts will launch the Docker container and run the benchmark. Run them outside of any Docker container.
:::

1.  Make sure [`$HF_HOME`{.docutils .literal .notranslate}]{.pre} is set before running the test. See [ROCm benchmarking](https://github.com/ROCm/MAD/blob/develop/scripts/jax-maxtext/gpu-rocm/readme.md){.reference .external} for more details on downloading the Llama models before running the benchmark.

2.  To run multi-node training for Llama 3 8B (multi-node), use the [multi-node training script](https://github.com/ROCm/MAD/blob/develop/scripts/jax-maxtext/gpu-rocm/llama3_8b_multinode.sh){.reference .external} under the [`scripts/jax-maxtext/gpu-rocm/`{.docutils .literal .notranslate}]{.pre} directory.

3.  Run the multi-node training benchmark script.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        sbatch -N <num_nodes> llama3_8b_multinode.sh
    :::
    ::::
::::::
:::::::
::::::::

:::::::: {.model-doc .jax-maxtext-train-llama-3-70b .docutils .container}
::::::: {.sd-tab-set .docutils}
Standalone benchmarking

:::::: {.sd-tab-content .docutils}
The following commands are optimized for Llama 3 70B (multi-node). See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v259){.reference .internal} to switch to another available model. Some instructions and resources might not be available for all models and configurations.

Download the Docker image and required scripts

Run the JAX MaxText benchmark tool independently by starting the Docker container as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/jax-training:maxtext-v25.9.1
:::
::::

Multi-node training

The following examples use SLURM to run on multiple nodes.

::: {.admonition .note}
Note

The following scripts will launch the Docker container and run the benchmark. Run them outside of any Docker container.
:::

1.  Make sure [`$HF_HOME`{.docutils .literal .notranslate}]{.pre} is set before running the test. See [ROCm benchmarking](https://github.com/ROCm/MAD/blob/develop/scripts/jax-maxtext/gpu-rocm/readme.md){.reference .external} for more details on downloading the Llama models before running the benchmark.

2.  To run multi-node training for Llama 3 70B (multi-node), use the [multi-node training script](https://github.com/ROCm/MAD/blob/develop/scripts/jax-maxtext/gpu-rocm/llama3_70b_multinode.sh){.reference .external} under the [`scripts/jax-maxtext/gpu-rocm/`{.docutils .literal .notranslate}]{.pre} directory.

3.  Run the multi-node training benchmark script.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        sbatch -N <num_nodes> llama3_70b_multinode.sh
    :::
    ::::
::::::
:::::::
::::::::

:::::::: {.model-doc .jax-maxtext-train-llama-3-1-8b .docutils .container}
::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to Llama 3.1 8B. See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v259){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  Use this command to run the performance benchmark test on the Llama 3.1 8B model using one GPU with the [`bf16`{.docutils .literal .notranslate}]{.pre} data type on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags jax_maxtext_train_llama-3.1-8b \
            --keep-model-dir \
            --live-output \
            --timeout 28800
    :::
    ::::

MAD launches a Docker container with the name [`container_ci-jax_maxtext_train_llama-3.1-8b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in the following path: [`~/MAD/perf.csv/`{.docutils .literal .notranslate}]{.pre}.
:::

Standalone benchmarking

::::: {.sd-tab-content .docutils}
The following commands are optimized for Llama 3.1 8B. See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v259){.reference .internal} to switch to another available model. Some instructions and resources might not be available for all models and configurations.

Download the Docker image and required scripts

Run the JAX MaxText benchmark tool independently by starting the Docker container as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/jax-training:maxtext-v25.9.1
:::
::::

Single node training

1.  Set up environment variables.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN=<Your Hugging Face token>
        export HF_HOME=<Location of saved/cached Hugging Face models>
    :::
    ::::

    [`MAD_SECRETS_HFTOKEN`{.docutils .literal .notranslate}]{.pre} is your Hugging Face access token to access models, tokenizers, and data. See [User access tokens](https://huggingface.co/docs/hub/en/security-tokens){.reference .external}.

    [`HF_HOME`{.docutils .literal .notranslate}]{.pre} is where [`huggingface_hub`{.docutils .literal .notranslate}]{.pre} will store local data. See [huggingface_hub CLI](https://huggingface.co/docs/huggingface_hub/main/en/guides/cli#huggingface-cli-download){.reference .external}. If you already have downloaded or cached Hugging Face artifacts, set this variable to that path. Downloaded files typically get cached to [`~/.cache/huggingface`{.docutils .literal .notranslate}]{.pre}.

2.  Launch the Docker container.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker run -it \
            --device=/dev/dri \
            --device=/dev/kfd \
            --network host \
            --ipc host \
            --group-add video \
            --cap-add=SYS_PTRACE \
            --security-opt seccomp=unconfined \
            --privileged \
            -v $HOME:$HOME \
            -v $HOME/.ssh:/root/.ssh \
            -v $HF_HOME:/hf_cache \
            -e HF_HOME=/hf_cache \
            -e MAD_SECRETS_HFTOKEN=$MAD_SECRETS_HFTOKEN
            --shm-size 64G \
            --name training_env \
            rocm/jax-training:maxtext-v25.9.1
    :::
    ::::

3.  In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at [`MAD/scripts/jax-maxtext`{.docutils .literal .notranslate}]{.pre}.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD/scripts/jax-maxtext
    :::
    ::::

4.  Run the setup scripts to install libraries and datasets needed for benchmarking.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        ./jax-maxtext_benchmark_setup.sh -m Llama-3.1-8B
    :::
    ::::

5.  To run the training benchmark without quantization, use the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        ./jax-maxtext_benchmark_report.sh -m Llama-3.1-8B
    :::
    ::::

    For quantized training, run the script with the appropriate option for your Instinct GPU.

    ::::::::: {.sd-tab-set .docutils}
    MI355X and MI350X

    ::::: {.sd-tab-content .docutils}
    For [`fp8`{.docutils .literal .notranslate}]{.pre} quantized training on MI355X and MI350X GPUs, use the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        ./jax-maxtext_benchmark_report.sh -m Llama-3.1-8B -q fp8
    :::
    ::::
    :::::

    MI325X and MI300X

    ::::: {.sd-tab-content .docutils}
    For [`nanoo_fp8`{.docutils .literal .notranslate}]{.pre} quantized training on MI300X series GPUs, use the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        ./jax-maxtext_benchmark_report.sh -m Llama-3.1-8B -q nanoo_fp8
    :::
    ::::
    :::::
    :::::::::

Multi-node training

For multi-node training examples, choose a model from [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v259){.reference .internal} with an available [multi-node training script](https://github.com/ROCm/MAD/tree/develop/scripts/jax-maxtext/gpu-rocm){.reference .external}.
:::::
:::::::
::::::::

:::::::: {.model-doc .jax-maxtext-train-llama-3-1-70b .docutils .container}
::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to Llama 3.1 70B. See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v259){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  Use this command to run the performance benchmark test on the Llama 3.1 70B model using one GPU with the [`bf16`{.docutils .literal .notranslate}]{.pre} data type on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags jax_maxtext_train_llama-3.1-70b \
            --keep-model-dir \
            --live-output \
            --timeout 28800
    :::
    ::::

MAD launches a Docker container with the name [`container_ci-jax_maxtext_train_llama-3.1-70b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in the following path: [`~/MAD/perf.csv/`{.docutils .literal .notranslate}]{.pre}.
:::

Standalone benchmarking

::::: {.sd-tab-content .docutils}
The following commands are optimized for Llama 3.1 70B. See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v259){.reference .internal} to switch to another available model. Some instructions and resources might not be available for all models and configurations.

Download the Docker image and required scripts

Run the JAX MaxText benchmark tool independently by starting the Docker container as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/jax-training:maxtext-v25.9.1
:::
::::

Single node training

1.  Set up environment variables.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN=<Your Hugging Face token>
        export HF_HOME=<Location of saved/cached Hugging Face models>
    :::
    ::::

    [`MAD_SECRETS_HFTOKEN`{.docutils .literal .notranslate}]{.pre} is your Hugging Face access token to access models, tokenizers, and data. See [User access tokens](https://huggingface.co/docs/hub/en/security-tokens){.reference .external}.

    [`HF_HOME`{.docutils .literal .notranslate}]{.pre} is where [`huggingface_hub`{.docutils .literal .notranslate}]{.pre} will store local data. See [huggingface_hub CLI](https://huggingface.co/docs/huggingface_hub/main/en/guides/cli#huggingface-cli-download){.reference .external}. If you already have downloaded or cached Hugging Face artifacts, set this variable to that path. Downloaded files typically get cached to [`~/.cache/huggingface`{.docutils .literal .notranslate}]{.pre}.

2.  Launch the Docker container.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker run -it \
            --device=/dev/dri \
            --device=/dev/kfd \
            --network host \
            --ipc host \
            --group-add video \
            --cap-add=SYS_PTRACE \
            --security-opt seccomp=unconfined \
            --privileged \
            -v $HOME:$HOME \
            -v $HOME/.ssh:/root/.ssh \
            -v $HF_HOME:/hf_cache \
            -e HF_HOME=/hf_cache \
            -e MAD_SECRETS_HFTOKEN=$MAD_SECRETS_HFTOKEN
            --shm-size 64G \
            --name training_env \
            rocm/jax-training:maxtext-v25.9.1
    :::
    ::::

3.  In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at [`MAD/scripts/jax-maxtext`{.docutils .literal .notranslate}]{.pre}.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD/scripts/jax-maxtext
    :::
    ::::

4.  Run the setup scripts to install libraries and datasets needed for benchmarking.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        ./jax-maxtext_benchmark_setup.sh -m Llama-3.1-70B
    :::
    ::::

5.  To run the training benchmark without quantization, use the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        ./jax-maxtext_benchmark_report.sh -m Llama-3.1-70B
    :::
    ::::

    For quantized training, run the script with the appropriate option for your Instinct GPU.

    :::::: {.sd-tab-set .docutils}
    MI355X and MI350X

    ::::: {.sd-tab-content .docutils}
    For [`fp8`{.docutils .literal .notranslate}]{.pre} quantized training on MI355X and MI350X GPUs, use the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        ./jax-maxtext_benchmark_report.sh -m Llama-3.1-70B -q fp8
    :::
    ::::
    :::::
    ::::::

Multi-node training

For multi-node training examples, choose a model from [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v259){.reference .internal} with an available [multi-node training script](https://github.com/ROCm/MAD/tree/develop/scripts/jax-maxtext/gpu-rocm){.reference .external}.
:::::
:::::::
::::::::

:::::::: {.model-doc .jax-maxtext-train-llama-3-3-70b .docutils .container}
::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to Llama 3.3 70B. See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v259){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  Use this command to run the performance benchmark test on the Llama 3.3 70B model using one GPU with the [`bf16`{.docutils .literal .notranslate}]{.pre} data type on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags jax_maxtext_train_llama-3.3-70b \
            --keep-model-dir \
            --live-output \
            --timeout 28800
    :::
    ::::

MAD launches a Docker container with the name [`container_ci-jax_maxtext_train_llama-3.3-70b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in the following path: [`~/MAD/perf.csv/`{.docutils .literal .notranslate}]{.pre}.
:::

Standalone benchmarking

::::: {.sd-tab-content .docutils}
The following commands are optimized for Llama 3.3 70B. See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v259){.reference .internal} to switch to another available model. Some instructions and resources might not be available for all models and configurations.

Download the Docker image and required scripts

Run the JAX MaxText benchmark tool independently by starting the Docker container as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/jax-training:maxtext-v25.9.1
:::
::::

Single node training

1.  Set up environment variables.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN=<Your Hugging Face token>
        export HF_HOME=<Location of saved/cached Hugging Face models>
    :::
    ::::

    [`MAD_SECRETS_HFTOKEN`{.docutils .literal .notranslate}]{.pre} is your Hugging Face access token to access models, tokenizers, and data. See [User access tokens](https://huggingface.co/docs/hub/en/security-tokens){.reference .external}.

    [`HF_HOME`{.docutils .literal .notranslate}]{.pre} is where [`huggingface_hub`{.docutils .literal .notranslate}]{.pre} will store local data. See [huggingface_hub CLI](https://huggingface.co/docs/huggingface_hub/main/en/guides/cli#huggingface-cli-download){.reference .external}. If you already have downloaded or cached Hugging Face artifacts, set this variable to that path. Downloaded files typically get cached to [`~/.cache/huggingface`{.docutils .literal .notranslate}]{.pre}.

2.  Launch the Docker container.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker run -it \
            --device=/dev/dri \
            --device=/dev/kfd \
            --network host \
            --ipc host \
            --group-add video \
            --cap-add=SYS_PTRACE \
            --security-opt seccomp=unconfined \
            --privileged \
            -v $HOME:$HOME \
            -v $HOME/.ssh:/root/.ssh \
            -v $HF_HOME:/hf_cache \
            -e HF_HOME=/hf_cache \
            -e MAD_SECRETS_HFTOKEN=$MAD_SECRETS_HFTOKEN
            --shm-size 64G \
            --name training_env \
            rocm/jax-training:maxtext-v25.9.1
    :::
    ::::

3.  In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at [`MAD/scripts/jax-maxtext`{.docutils .literal .notranslate}]{.pre}.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD/scripts/jax-maxtext
    :::
    ::::

4.  Run the setup scripts to install libraries and datasets needed for benchmarking.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        ./jax-maxtext_benchmark_setup.sh -m Llama-3.3-70B
    :::
    ::::

5.  To run the training benchmark without quantization, use the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        ./jax-maxtext_benchmark_report.sh -m Llama-3.3-70B
    :::
    ::::

    For quantized training, run the script with the appropriate option for your Instinct GPU.

    :::::: {.sd-tab-set .docutils}
    MI355X and MI350X

    ::::: {.sd-tab-content .docutils}
    For [`fp8`{.docutils .literal .notranslate}]{.pre} quantized training on MI355X and MI350X GPUs, use the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        ./jax-maxtext_benchmark_report.sh -m Llama-3.3-70B -q fp8
    :::
    ::::
    :::::
    ::::::

Multi-node training

For multi-node training examples, choose a model from [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v259){.reference .internal} with an available [multi-node training script](https://github.com/ROCm/MAD/tree/develop/scripts/jax-maxtext/gpu-rocm){.reference .external}.
:::::
:::::::
::::::::

:::::::: {.model-doc .jax-maxtext-train-deepseek-v2-lite-16b .docutils .container}
::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to DeepSeek-V2-Lite (16B). See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v259){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  Use this command to run the performance benchmark test on the DeepSeek-V2-Lite (16B) model using one GPU with the [`bf16`{.docutils .literal .notranslate}]{.pre} data type on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags jax_maxtext_train_deepseek-v2-lite-16b \
            --keep-model-dir \
            --live-output \
            --timeout 28800
    :::
    ::::

MAD launches a Docker container with the name [`container_ci-jax_maxtext_train_deepseek-v2-lite-16b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in the following path: [`~/MAD/perf.csv/`{.docutils .literal .notranslate}]{.pre}.
:::

Standalone benchmarking

::::: {.sd-tab-content .docutils}
The following commands are optimized for DeepSeek-V2-Lite (16B). See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v259){.reference .internal} to switch to another available model. Some instructions and resources might not be available for all models and configurations.

Download the Docker image and required scripts

Run the JAX MaxText benchmark tool independently by starting the Docker container as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/jax-training:maxtext-v25.9.1
:::
::::

Single node training

1.  Set up environment variables.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN=<Your Hugging Face token>
        export HF_HOME=<Location of saved/cached Hugging Face models>
    :::
    ::::

    [`MAD_SECRETS_HFTOKEN`{.docutils .literal .notranslate}]{.pre} is your Hugging Face access token to access models, tokenizers, and data. See [User access tokens](https://huggingface.co/docs/hub/en/security-tokens){.reference .external}.

    [`HF_HOME`{.docutils .literal .notranslate}]{.pre} is where [`huggingface_hub`{.docutils .literal .notranslate}]{.pre} will store local data. See [huggingface_hub CLI](https://huggingface.co/docs/huggingface_hub/main/en/guides/cli#huggingface-cli-download){.reference .external}. If you already have downloaded or cached Hugging Face artifacts, set this variable to that path. Downloaded files typically get cached to [`~/.cache/huggingface`{.docutils .literal .notranslate}]{.pre}.

2.  Launch the Docker container.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker run -it \
            --device=/dev/dri \
            --device=/dev/kfd \
            --network host \
            --ipc host \
            --group-add video \
            --cap-add=SYS_PTRACE \
            --security-opt seccomp=unconfined \
            --privileged \
            -v $HOME:$HOME \
            -v $HOME/.ssh:/root/.ssh \
            -v $HF_HOME:/hf_cache \
            -e HF_HOME=/hf_cache \
            -e MAD_SECRETS_HFTOKEN=$MAD_SECRETS_HFTOKEN
            --shm-size 64G \
            --name training_env \
            rocm/jax-training:maxtext-v25.9.1
    :::
    ::::

3.  In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at [`MAD/scripts/jax-maxtext`{.docutils .literal .notranslate}]{.pre}.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD/scripts/jax-maxtext
    :::
    ::::

4.  Run the setup scripts to install libraries and datasets needed for benchmarking.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        ./jax-maxtext_benchmark_setup.sh -m DeepSeek-V2-lite
    :::
    ::::

5.  To run the training benchmark without quantization, use the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        ./jax-maxtext_benchmark_report.sh -m DeepSeek-V2-lite
    :::
    ::::

    For quantized training, run the script with the appropriate option for your Instinct GPU.

    ::::::::: {.sd-tab-set .docutils}
    MI355X and MI350X

    ::::: {.sd-tab-content .docutils}
    For [`fp8`{.docutils .literal .notranslate}]{.pre} quantized training on MI355X and MI350X GPUs, use the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        ./jax-maxtext_benchmark_report.sh -m DeepSeek-V2-lite -q fp8
    :::
    ::::
    :::::

    MI325X and MI300X

    ::::: {.sd-tab-content .docutils}
    For [`nanoo_fp8`{.docutils .literal .notranslate}]{.pre} quantized training on MI300X series GPUs, use the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        ./jax-maxtext_benchmark_report.sh -m DeepSeek-V2-lite -q nanoo_fp8
    :::
    ::::
    :::::
    :::::::::

Multi-node training

For multi-node training examples, choose a model from [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v259){.reference .internal} with an available [multi-node training script](https://github.com/ROCm/MAD/tree/develop/scripts/jax-maxtext/gpu-rocm){.reference .external}.
:::::
:::::::
::::::::

:::::::: {.model-doc .jax-maxtext-train-mixtral-8x7b .docutils .container}
::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to Mixtral 8x7B. See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v259){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  Use this command to run the performance benchmark test on the Mixtral 8x7B model using one GPU with the [`bf16`{.docutils .literal .notranslate}]{.pre} data type on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags jax_maxtext_train_mixtral-8x7b \
            --keep-model-dir \
            --live-output \
            --timeout 28800
    :::
    ::::

MAD launches a Docker container with the name [`container_ci-jax_maxtext_train_mixtral-8x7b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in the following path: [`~/MAD/perf.csv/`{.docutils .literal .notranslate}]{.pre}.
:::

Standalone benchmarking

::::: {.sd-tab-content .docutils}
The following commands are optimized for Mixtral 8x7B. See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v259){.reference .internal} to switch to another available model. Some instructions and resources might not be available for all models and configurations.

Download the Docker image and required scripts

Run the JAX MaxText benchmark tool independently by starting the Docker container as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/jax-training:maxtext-v25.9.1
:::
::::

Single node training

1.  Set up environment variables.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN=<Your Hugging Face token>
        export HF_HOME=<Location of saved/cached Hugging Face models>
    :::
    ::::

    [`MAD_SECRETS_HFTOKEN`{.docutils .literal .notranslate}]{.pre} is your Hugging Face access token to access models, tokenizers, and data. See [User access tokens](https://huggingface.co/docs/hub/en/security-tokens){.reference .external}.

    [`HF_HOME`{.docutils .literal .notranslate}]{.pre} is where [`huggingface_hub`{.docutils .literal .notranslate}]{.pre} will store local data. See [huggingface_hub CLI](https://huggingface.co/docs/huggingface_hub/main/en/guides/cli#huggingface-cli-download){.reference .external}. If you already have downloaded or cached Hugging Face artifacts, set this variable to that path. Downloaded files typically get cached to [`~/.cache/huggingface`{.docutils .literal .notranslate}]{.pre}.

2.  Launch the Docker container.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker run -it \
            --device=/dev/dri \
            --device=/dev/kfd \
            --network host \
            --ipc host \
            --group-add video \
            --cap-add=SYS_PTRACE \
            --security-opt seccomp=unconfined \
            --privileged \
            -v $HOME:$HOME \
            -v $HOME/.ssh:/root/.ssh \
            -v $HF_HOME:/hf_cache \
            -e HF_HOME=/hf_cache \
            -e MAD_SECRETS_HFTOKEN=$MAD_SECRETS_HFTOKEN
            --shm-size 64G \
            --name training_env \
            rocm/jax-training:maxtext-v25.9.1
    :::
    ::::

3.  In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at [`MAD/scripts/jax-maxtext`{.docutils .literal .notranslate}]{.pre}.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD/scripts/jax-maxtext
    :::
    ::::

4.  Run the setup scripts to install libraries and datasets needed for benchmarking.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        ./jax-maxtext_benchmark_setup.sh -m Mixtral-8x7B
    :::
    ::::

5.  To run the training benchmark without quantization, use the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        ./jax-maxtext_benchmark_report.sh -m Mixtral-8x7B
    :::
    ::::

    For quantized training, run the script with the appropriate option for your Instinct GPU.

    ::::::::: {.sd-tab-set .docutils}
    MI355X and MI350X

    ::::: {.sd-tab-content .docutils}
    For [`fp8`{.docutils .literal .notranslate}]{.pre} quantized training on MI355X and MI350X GPUs, use the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        ./jax-maxtext_benchmark_report.sh -m Mixtral-8x7B -q fp8
    :::
    ::::
    :::::

    MI325X and MI300X

    ::::: {.sd-tab-content .docutils}
    For [`nanoo_fp8`{.docutils .literal .notranslate}]{.pre} quantized training on MI300X series GPUs, use the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        ./jax-maxtext_benchmark_report.sh -m Mixtral-8x7B -q nanoo_fp8
    :::
    ::::
    :::::
    :::::::::

Multi-node training

For multi-node training examples, choose a model from [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v259){.reference .internal} with an available [multi-node training script](https://github.com/ROCm/MAD/tree/develop/scripts/jax-maxtext/gpu-rocm){.reference .external}.
:::::
:::::::
::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: {#further-reading .section}
## Further reading[\#](#further-reading "Link to this heading"){.headerlink}

- To learn more about MAD and the [`madengine`{.docutils .literal .notranslate}]{.pre} CLI, see the [MAD usage guide](https://github.com/ROCm/MAD?tab=readme-ov-file#usage-guide){.reference .external}.

- To learn more about system settings and management practices to configure your system for AMD Instinct MI300X Series GPUs, see [AMD Instinct MI300X system optimization](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi300x.html){.reference .external}.

- For a list of other ready-made Docker images for AI with ROCm, see [AMD Infinity Hub](https://www.amd.com/en/developer/resources/infinity-hub.html#f-amd_hub_category=AI%20%26%20ML%20Models){.reference .external}.
:::

::: {#previous-versions .section}
## Previous versions[\#](#previous-versions "Link to this heading"){.headerlink}

See [[JAX MaxText training performance testing version history]{.doc}](jax-maxtext-history.html){.reference .internal} to find documentation for previous releases of the [`ROCm/jax-training`{.docutils .literal .notranslate}]{.pre} Docker image.
:::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: prev-next-area
:::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::: {.bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {.page-toc .tocsection .onthispage}
Contents
:::

- [Supported models](#supported-models){.reference .internal .nav-link}
- [System validation](#system-validation){.reference .internal .nav-link}
- [Environment setup](#environment-setup){.reference .internal .nav-link}
  - [Pull the Docker image](#pull-the-docker-image){.reference .internal .nav-link}
  - [Multi-node configuration](#multi-node-configuration){.reference .internal .nav-link}
- [Benchmarking](#benchmarking){.reference .internal .nav-link}
- [Further reading](#further-reading){.reference .internal .nav-link}
- [Previous versions](#previous-versions){.reference .internal .nav-link}
::::
:::::
::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
