---
title: "Training a model with Primus and JAX MaxText"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/training/benchmark-docker/jax-maxtext.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-01
---

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-content
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-article-container
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
# Training a model with Primus and JAX MaxText

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
- [Known issues](#known-issues){.reference .internal .nav-link}
- [Further reading](#further-reading){.reference .internal .nav-link}
- [Previous versions](#previous-versions){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#training-a-model-with-primus-and-jax-maxtext .section}
# Training a model with Primus and JAX MaxText[\#](#training-a-model-with-primus-and-jax-maxtext "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-02-24
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 41 min read time
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

The JAX MaxText for ROCm training Docker image provides a prebuilt environment for training on AMD Instinct MI355X, MI350X, MI325X, and MI300X GPUs, with essential components such as JAX, XLA, ROCm libraries, and MaxText utilities.

The image also integrates with [Primus](https://github.com/AMD-AGI/Primus){.reference .external}, a high-level training framework that supports multiple backends. You can use the unified [`primus-cli`{.docutils .literal .notranslate}]{.pre} to run training jobs using the JAX MaxText backend.

It includes the following software components:

::::: {.sd-tab-set .docutils}
[`rocm/jax-training:maxtext-v26.2`{.docutils .literal .notranslate}]{.pre}

:::: {.sd-tab-content .docutils}
::: pst-scrollable-table-container
  Software component   Version
  -------------------- ---------------------
  ROCm                 7.1.1
  JAX                  0.8.2
  Python               3.12
  Transformer Engine   2.8.0.dev0+aec00a7f
  hipBLASLt            1.2.x
:::
::::
:::::

MaxText with on ROCm provides the following key features to train large language models efficiently:

- Transformer Engine (TE)

- Flash Attention (FA) 3 -- with or without sequence input packing

- GEMM tuning

- Multi-node support

- NANOO FP8 (for MI300X series GPUs) and FP8 (for MI355X and MI350X) quantization support

:::::::::::::::::::::::: {#supported-models .section}
[]{#amd-maxtext-model-support-v26-2}

## Supported models[\#](#supported-models "Link to this heading"){.headerlink}

The following models are pre-optimized for performance on AMD Instinct GPUs. Some instructions, commands, and available training configurations in this documentation might vary by model -- select one to get started.

:::::::::::::::::::::: {#vllm-benchmark-ud-params-picker .container-fluid}
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

::::::::::::::: {.row .gx-0 .pt-1}
::: {.col-2 .me-1 .px-2 .model-param-head}
Variant
:::

::::::::::::: {.row .col-10 .pe-0}
::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="jax_maxtext_train_llama-2-7b" tabindex="0"}
Llama 2 7B
:::

::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="jax_maxtext_train_llama-2-70b" tabindex="0"}
Llama 2 70B
:::

::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="jax_maxtext_train_llama-3-8b" tabindex="0"}
Llama 3 8B
:::

::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="jax_maxtext_train_llama-3-70b" tabindex="0"}
Llama 3 70B
:::

::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="jax_maxtext_train_llama-3.1-8b" tabindex="0"}
Llama 3.1 8B
:::

::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="jax_maxtext_train_llama-3.1-70b" tabindex="0"}
Llama 3.1 70B
:::

::: {.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="jax_maxtext_train_llama-3.1-405b" tabindex="0"}
Llama 3.1 405B (multi-node)
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
:::::::::::::
:::::::::::::::
::::::::::::::::::::::

::: {.admonition .note}
Note

Some models, such as Llama 3, require an external license agreement through a third party (for example, Meta).
:::
::::::::::::::::::::::::

::: {#system-validation .section}
## System validation[\#](#system-validation "Link to this heading"){.headerlink}

Before running AI workloads, it's important to validate that your AMD hardware is configured correctly and performing optimally.

If you have already validated your system settings, including aspects like NUMA auto-balancing, you can skip this step. Otherwise, complete the procedures in the [[System validation and optimization]{.std .std-ref}](../../system-setup/prerequisite-system-validation.html#rocm-for-ai-system-optimization){.reference .internal} guide to properly configure your system settings before starting training.

To test for optimal performance, consult the recommended [[System health benchmarks]{.std .std-ref}](../../system-setup/system-health-check.html#rocm-for-ai-system-health-bench){.reference .internal}. This suite of tests will help you verify and fine-tune your system's configuration.
:::

::::::: {#environment-setup .section}
## Environment setup[\#](#environment-setup "Link to this heading"){.headerlink}

This Docker image is optimized for specific model configurations outlined as follows. Performance can vary for other training workloads, as AMD doesn't validate configurations and run conditions outside those described.

::::: {#pull-the-docker-image .section}
### Pull the Docker image[\#](#pull-the-docker-image "Link to this heading"){.headerlink}

Use the following command to pull the Docker image from Docker Hub.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/jax-training:maxtext-v26.2
:::
::::
:::::

::: {#multi-node-configuration .section}
[]{#amd-maxtext-multi-node-setup-v26-2}

### Multi-node configuration[\#](#multi-node-configuration "Link to this heading"){.headerlink}

See [[Multi-node setup for AI workloads]{.doc}](../../system-setup/multi-node-setup.html){.reference .internal} to configure your environment for multi-node training.
:::
:::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#benchmarking .section}
[]{#amd-maxtext-get-started-v26-2}

## Benchmarking[\#](#benchmarking "Link to this heading"){.headerlink}

Once the setup is complete, choose between two options to reproduce the benchmark results:

::::::::::::::::::: {#vllm-benchmark-mad .model-doc .jax-maxtext-train-llama-2-7b .docutils .container}
:::::::::::::::::: {.sd-tab-set .docutils}
Primus benchmarking

:::: {.sd-tab-content .docutils}
::: {.model-doc .jax-maxtext-train-llama-2-7b .docutils .container}
The following run commands are tailored to Llama 2 7B. See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v26-2){.reference .internal} to switch to another available model.

Download the Docker image and required packages

1.  Pull the [`rocm/jax-training:maxtext-v26.2`{.docutils .literal .notranslate}]{.pre} Docker image from Docker Hub.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker pull rocm/jax-training:maxtext-v26.2
    :::
    ::::

2.  Run the Docker container.

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
            -v $HF_HOME:/hf_cache \
            -e HF_HOME=/hf_cache \
            -e MAD_SECRETS_HFTOKEN=$MAD_SECRETS_HFTOKEN
            --shm-size 64G \
            --name training_env \
            rocm/jax-training:maxtext-v26.2
    :::
    ::::

    Use these commands if you exit the [`training_env`{.docutils .literal .notranslate}]{.pre} container and need to return to it.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker start training_env
        docker exec -it training_env bash
    :::
    ::::

3.  Clone the Primus repository.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/AMD-AIG-AIMA/Primus.git
        cd Primus
        git checkout dev/fuyuajin/maxtext-backend-test
        git submodule update --init third_party/maxtext/
    :::
    ::::

Run the training job with primus-cli

For detailed usage instructions for [`primus-cli`{.docutils .literal .notranslate}]{.pre}, see the [Primus CLI User Guide](https://github.com/AMD-AGI/Primus/blob/main/docs/cli/PRIMUS-CLI-GUIDE.md){.reference .external}.

Use the following examples to run training with [`primus-cli`{.docutils .literal .notranslate}]{.pre}:

- Direct mode: run directly on the current host or within an existing Docker container

  ::::::::: {.sd-tab-set .docutils}
  MI355X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      ./primus-cli direct \
        -- train pretrain \
        --config examples/maxtext/configs/MI355X/llama2_7B-pretrain.yaml
  :::
  ::::
  :::::

  MI300X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      ./primus-cli direct \
        -- train pretrain \
        --config examples/maxtext/configs/MI300X/llama2_7B-pretrain.yaml
  :::
  ::::
  :::::
  :::::::::

- Container mode: run in Docker containers

  ::::::::: {.sd-tab-set .docutils}
  MI355X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      ./primus-cli container --image rocm/jax-training:maxtext-v26.2 \
        -- train pretrain \
        --config examples/maxtext/configs/MI355X/llama2_7B-pretrain.yaml
  :::
  ::::
  :::::

  MI300X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      ./primus-cli container --image rocm/jax-training:maxtext-v26.2 \
        -- train pretrain \
        --config examples/maxtext/configs/MI300X/llama2_7B-pretrain.yaml
  :::
  ::::
  :::::
  :::::::::

- Slurm mode: run distributed training on a Slurm cluster

  ::::::::: {.sd-tab-set .docutils}
  MI355X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      # Use a custom config file, where you can specify
      # the Docker image and set environment variables.
      ./primus-cli --config my_maxtext_config.yaml slurm srun -N 8 \
        -- train pretrain \
        --config examples/maxtext/configs/MI355X/llama2_7B-pretrain.yaml
  :::
  ::::
  :::::

  MI300X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      # Use a custom config file, where you can specify
      # the Docker image and set environment variables.
      ./primus-cli --config my_maxtext_config.yaml slurm srun -N 8 \
        -- train pretrain \
        --config examples/maxtext/configs/MI300X/llama2_7B-pretrain.yaml
  :::
  ::::
  :::::
  :::::::::
:::
::::

MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to Llama 2 7B. See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v26-2){.reference .internal} to switch to another available model.

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

:::::::::::::: {.sd-tab-content .docutils}
The following commands are optimized for Llama 2 7B. See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v26-2){.reference .internal} to switch to another available model. Some instructions and resources might not be available for all models and configurations.

Download the Docker image and required scripts

Run the JAX MaxText benchmark tool independently by starting the Docker container as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/jax-training:maxtext-v26.2
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
            rocm/jax-training:maxtext-v26.2
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

The following SLURM scripts will launch the Docker container and run the benchmark. Run them outside of any Docker container. The unified multi-node benchmark script accepts a configuration file that specifies the model and training parameters.

:::: {.highlight-shell .notranslate}
::: highlight
    sbatch -N <NUM_NODES> jax_maxtext_multinode_benchmark.sh <config_file.yml> [docker_image]
:::
::::

\<NUM_NODES\>

:   The number of nodes to use for training (for example, 2, 4, 8).

\<config_file.yml\>

:   Path to the YAML configuration file containing model and training parameters. Configuration files are available in the [`scripts/jax-maxtext/env_scripts/`{.docutils .literal .notranslate}]{.pre} directory for different models and GPU architectures.

\[docker_image\] (optional)

:   The Docker image to use. If not specified, it defaults to [`rocm/jax-training:maxtext-v26.2`{.docutils .literal .notranslate}]{.pre}.

For example, to run a multi-node training benchmark on Llama 2 7B:

::::::::: {.sd-tab-set .docutils}
MI355X and MI350X (gfx950)

::::: {.sd-tab-content .docutils}
:::: {.highlight-bash .notranslate}
::: highlight
    sbatch -N 4 jax_maxtext_multinode_benchmark.sh env_scripts/gfx950_llama2_7b.yml
:::
::::
:::::

MI325X and MI300X (gfx942)

::::: {.sd-tab-content .docutils}
:::: {.highlight-bash .notranslate}
::: highlight
    sbatch -N 4 jax_maxtext_multinode_benchmark.sh env_scripts/llama2_7b.yml
:::
::::
:::::
:::::::::
::::::::::::::
::::::::::::::::::
:::::::::::::::::::

::::::::::::::::::: {.model-doc .jax-maxtext-train-llama-2-70b .docutils .container}
:::::::::::::::::: {.sd-tab-set .docutils}
Primus benchmarking

:::: {.sd-tab-content .docutils}
::: {.model-doc .jax-maxtext-train-llama-2-70b .docutils .container}
The following run commands are tailored to Llama 2 70B. See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v26-2){.reference .internal} to switch to another available model.

Download the Docker image and required packages

1.  Pull the [`rocm/jax-training:maxtext-v26.2`{.docutils .literal .notranslate}]{.pre} Docker image from Docker Hub.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker pull rocm/jax-training:maxtext-v26.2
    :::
    ::::

2.  Run the Docker container.

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
            -v $HF_HOME:/hf_cache \
            -e HF_HOME=/hf_cache \
            -e MAD_SECRETS_HFTOKEN=$MAD_SECRETS_HFTOKEN
            --shm-size 64G \
            --name training_env \
            rocm/jax-training:maxtext-v26.2
    :::
    ::::

    Use these commands if you exit the [`training_env`{.docutils .literal .notranslate}]{.pre} container and need to return to it.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker start training_env
        docker exec -it training_env bash
    :::
    ::::

3.  Clone the Primus repository.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/AMD-AIG-AIMA/Primus.git
        cd Primus
        git checkout dev/fuyuajin/maxtext-backend-test
        git submodule update --init third_party/maxtext/
    :::
    ::::

Run the training job with primus-cli

For detailed usage instructions for [`primus-cli`{.docutils .literal .notranslate}]{.pre}, see the [Primus CLI User Guide](https://github.com/AMD-AGI/Primus/blob/main/docs/cli/PRIMUS-CLI-GUIDE.md){.reference .external}.

Use the following examples to run training with [`primus-cli`{.docutils .literal .notranslate}]{.pre}:

- Direct mode: run directly on the current host or within an existing Docker container

  ::::::::: {.sd-tab-set .docutils}
  MI355X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      ./primus-cli direct \
        -- train pretrain \
        --config examples/maxtext/configs/MI355X/llama2_70B-pretrain.yaml
  :::
  ::::
  :::::

  MI300X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      ./primus-cli direct \
        -- train pretrain \
        --config examples/maxtext/configs/MI300X/llama2_70B-pretrain.yaml
  :::
  ::::
  :::::
  :::::::::

- Container mode: run in Docker containers

  ::::::::: {.sd-tab-set .docutils}
  MI355X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      ./primus-cli container --image rocm/jax-training:maxtext-v26.2 \
        -- train pretrain \
        --config examples/maxtext/configs/MI355X/llama2_70B-pretrain.yaml
  :::
  ::::
  :::::

  MI300X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      ./primus-cli container --image rocm/jax-training:maxtext-v26.2 \
        -- train pretrain \
        --config examples/maxtext/configs/MI300X/llama2_70B-pretrain.yaml
  :::
  ::::
  :::::
  :::::::::

- Slurm mode: run distributed training on a Slurm cluster

  ::::::::: {.sd-tab-set .docutils}
  MI355X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      # Use a custom config file, where you can specify
      # the Docker image and set environment variables.
      ./primus-cli --config my_maxtext_config.yaml slurm srun -N 8 \
        -- train pretrain \
        --config examples/maxtext/configs/MI355X/llama2_70B-pretrain.yaml
  :::
  ::::
  :::::

  MI300X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      # Use a custom config file, where you can specify
      # the Docker image and set environment variables.
      ./primus-cli --config my_maxtext_config.yaml slurm srun -N 8 \
        -- train pretrain \
        --config examples/maxtext/configs/MI300X/llama2_70B-pretrain.yaml
  :::
  ::::
  :::::
  :::::::::
:::
::::

MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to Llama 2 70B. See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v26-2){.reference .internal} to switch to another available model.

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

:::::::::::::: {.sd-tab-content .docutils}
The following commands are optimized for Llama 2 70B. See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v26-2){.reference .internal} to switch to another available model. Some instructions and resources might not be available for all models and configurations.

Download the Docker image and required scripts

Run the JAX MaxText benchmark tool independently by starting the Docker container as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/jax-training:maxtext-v26.2
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
            rocm/jax-training:maxtext-v26.2
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

The following SLURM scripts will launch the Docker container and run the benchmark. Run them outside of any Docker container. The unified multi-node benchmark script accepts a configuration file that specifies the model and training parameters.

:::: {.highlight-shell .notranslate}
::: highlight
    sbatch -N <NUM_NODES> jax_maxtext_multinode_benchmark.sh <config_file.yml> [docker_image]
:::
::::

\<NUM_NODES\>

:   The number of nodes to use for training (for example, 2, 4, 8).

\<config_file.yml\>

:   Path to the YAML configuration file containing model and training parameters. Configuration files are available in the [`scripts/jax-maxtext/env_scripts/`{.docutils .literal .notranslate}]{.pre} directory for different models and GPU architectures.

\[docker_image\] (optional)

:   The Docker image to use. If not specified, it defaults to [`rocm/jax-training:maxtext-v26.2`{.docutils .literal .notranslate}]{.pre}.

For example, to run a multi-node training benchmark on Llama 2 70B:

::::::::: {.sd-tab-set .docutils}
MI355X and MI350X (gfx950)

::::: {.sd-tab-content .docutils}
:::: {.highlight-bash .notranslate}
::: highlight
    sbatch -N 4 jax_maxtext_multinode_benchmark.sh env_scripts/gfx950_llama2_70b.yml
:::
::::
:::::

MI325X and MI300X (gfx942)

::::: {.sd-tab-content .docutils}
:::: {.highlight-bash .notranslate}
::: highlight
    sbatch -N 4 jax_maxtext_multinode_benchmark.sh env_scripts/llama2_70b.yml
:::
::::
:::::
:::::::::
::::::::::::::
::::::::::::::::::
:::::::::::::::::::

:::::::::::::::::: {.model-doc .jax-maxtext-train-llama-3-8b .docutils .container}
::::::::::::::::: {.sd-tab-set .docutils}
Primus benchmarking

:::: {.sd-tab-content .docutils}
::: {.model-doc .jax-maxtext-train-llama-3-8b .docutils .container}
The following run commands are tailored to Llama 3 8B. See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v26-2){.reference .internal} to switch to another available model.

Download the Docker image and required packages

1.  Pull the [`rocm/jax-training:maxtext-v26.2`{.docutils .literal .notranslate}]{.pre} Docker image from Docker Hub.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker pull rocm/jax-training:maxtext-v26.2
    :::
    ::::

2.  Run the Docker container.

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
            -v $HF_HOME:/hf_cache \
            -e HF_HOME=/hf_cache \
            -e MAD_SECRETS_HFTOKEN=$MAD_SECRETS_HFTOKEN
            --shm-size 64G \
            --name training_env \
            rocm/jax-training:maxtext-v26.2
    :::
    ::::

    Use these commands if you exit the [`training_env`{.docutils .literal .notranslate}]{.pre} container and need to return to it.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker start training_env
        docker exec -it training_env bash
    :::
    ::::

3.  Clone the Primus repository.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/AMD-AIG-AIMA/Primus.git
        cd Primus
        git checkout dev/fuyuajin/maxtext-backend-test
        git submodule update --init third_party/maxtext/
    :::
    ::::

Run the training job with primus-cli

For detailed usage instructions for [`primus-cli`{.docutils .literal .notranslate}]{.pre}, see the [Primus CLI User Guide](https://github.com/AMD-AGI/Primus/blob/main/docs/cli/PRIMUS-CLI-GUIDE.md){.reference .external}.

Use the following examples to run training with [`primus-cli`{.docutils .literal .notranslate}]{.pre}:

- Direct mode: run directly on the current host or within an existing Docker container

  ::::::::: {.sd-tab-set .docutils}
  MI355X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      ./primus-cli direct \
        -- train pretrain \
        --config examples/maxtext/configs/MI355X/llama3_8B-pretrain.yaml
  :::
  ::::
  :::::

  MI300X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      ./primus-cli direct \
        -- train pretrain \
        --config examples/maxtext/configs/MI300X/llama3_8B-pretrain.yaml
  :::
  ::::
  :::::
  :::::::::

- Container mode: run in Docker containers

  ::::::::: {.sd-tab-set .docutils}
  MI355X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      ./primus-cli container --image rocm/jax-training:maxtext-v26.2 \
        -- train pretrain \
        --config examples/maxtext/configs/MI355X/llama3_8B-pretrain.yaml
  :::
  ::::
  :::::

  MI300X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      ./primus-cli container --image rocm/jax-training:maxtext-v26.2 \
        -- train pretrain \
        --config examples/maxtext/configs/MI300X/llama3_8B-pretrain.yaml
  :::
  ::::
  :::::
  :::::::::

- Slurm mode: run distributed training on a Slurm cluster

  ::::::::: {.sd-tab-set .docutils}
  MI355X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      # Use a custom config file, where you can specify
      # the Docker image and set environment variables.
      ./primus-cli --config my_maxtext_config.yaml slurm srun -N 8 \
        -- train pretrain \
        --config examples/maxtext/configs/MI355X/llama3_8B-pretrain.yaml
  :::
  ::::
  :::::

  MI300X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      # Use a custom config file, where you can specify
      # the Docker image and set environment variables.
      ./primus-cli --config my_maxtext_config.yaml slurm srun -N 8 \
        -- train pretrain \
        --config examples/maxtext/configs/MI300X/llama3_8B-pretrain.yaml
  :::
  ::::
  :::::
  :::::::::
:::
::::

Standalone benchmarking

:::::::::::::: {.sd-tab-content .docutils}
The following commands are optimized for Llama 3 8B. See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v26-2){.reference .internal} to switch to another available model. Some instructions and resources might not be available for all models and configurations.

Download the Docker image and required scripts

Run the JAX MaxText benchmark tool independently by starting the Docker container as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/jax-training:maxtext-v26.2
:::
::::

Multi-node training

The following SLURM scripts will launch the Docker container and run the benchmark. Run them outside of any Docker container. The unified multi-node benchmark script accepts a configuration file that specifies the model and training parameters.

:::: {.highlight-shell .notranslate}
::: highlight
    sbatch -N <NUM_NODES> jax_maxtext_multinode_benchmark.sh <config_file.yml> [docker_image]
:::
::::

\<NUM_NODES\>

:   The number of nodes to use for training (for example, 2, 4, 8).

\<config_file.yml\>

:   Path to the YAML configuration file containing model and training parameters. Configuration files are available in the [`scripts/jax-maxtext/env_scripts/`{.docutils .literal .notranslate}]{.pre} directory for different models and GPU architectures.

\[docker_image\] (optional)

:   The Docker image to use. If not specified, it defaults to [`rocm/jax-training:maxtext-v26.2`{.docutils .literal .notranslate}]{.pre}.

For example, to run a multi-node training benchmark on Llama 3 8B:

::::::::: {.sd-tab-set .docutils}
MI355X and MI350X (gfx950)

::::: {.sd-tab-content .docutils}
:::: {.highlight-bash .notranslate}
::: highlight
    sbatch -N 4 jax_maxtext_multinode_benchmark.sh env_scripts/gfx950_llama3_8b.yml
:::
::::
:::::

MI325X and MI300X (gfx942)

::::: {.sd-tab-content .docutils}
:::: {.highlight-bash .notranslate}
::: highlight
    sbatch -N 4 jax_maxtext_multinode_benchmark.sh env_scripts/llama3_8b.yml
:::
::::
:::::
:::::::::
::::::::::::::
:::::::::::::::::
::::::::::::::::::

:::::::::::::::::: {.model-doc .jax-maxtext-train-llama-3-70b .docutils .container}
::::::::::::::::: {.sd-tab-set .docutils}
Primus benchmarking

:::: {.sd-tab-content .docutils}
::: {.model-doc .jax-maxtext-train-llama-3-70b .docutils .container}
The following run commands are tailored to Llama 3 70B. See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v26-2){.reference .internal} to switch to another available model.

Download the Docker image and required packages

1.  Pull the [`rocm/jax-training:maxtext-v26.2`{.docutils .literal .notranslate}]{.pre} Docker image from Docker Hub.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker pull rocm/jax-training:maxtext-v26.2
    :::
    ::::

2.  Run the Docker container.

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
            -v $HF_HOME:/hf_cache \
            -e HF_HOME=/hf_cache \
            -e MAD_SECRETS_HFTOKEN=$MAD_SECRETS_HFTOKEN
            --shm-size 64G \
            --name training_env \
            rocm/jax-training:maxtext-v26.2
    :::
    ::::

    Use these commands if you exit the [`training_env`{.docutils .literal .notranslate}]{.pre} container and need to return to it.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker start training_env
        docker exec -it training_env bash
    :::
    ::::

3.  Clone the Primus repository.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/AMD-AIG-AIMA/Primus.git
        cd Primus
        git checkout dev/fuyuajin/maxtext-backend-test
        git submodule update --init third_party/maxtext/
    :::
    ::::

Run the training job with primus-cli

For detailed usage instructions for [`primus-cli`{.docutils .literal .notranslate}]{.pre}, see the [Primus CLI User Guide](https://github.com/AMD-AGI/Primus/blob/main/docs/cli/PRIMUS-CLI-GUIDE.md){.reference .external}.

Use the following examples to run training with [`primus-cli`{.docutils .literal .notranslate}]{.pre}:

- Direct mode: run directly on the current host or within an existing Docker container

  ::::::::: {.sd-tab-set .docutils}
  MI355X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      ./primus-cli direct \
        -- train pretrain \
        --config examples/maxtext/configs/MI355X/llama3_70B-pretrain.yaml
  :::
  ::::
  :::::

  MI300X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      ./primus-cli direct \
        -- train pretrain \
        --config examples/maxtext/configs/MI300X/llama3_70B-pretrain.yaml
  :::
  ::::
  :::::
  :::::::::

- Container mode: run in Docker containers

  ::::::::: {.sd-tab-set .docutils}
  MI355X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      ./primus-cli container --image rocm/jax-training:maxtext-v26.2 \
        -- train pretrain \
        --config examples/maxtext/configs/MI355X/llama3_70B-pretrain.yaml
  :::
  ::::
  :::::

  MI300X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      ./primus-cli container --image rocm/jax-training:maxtext-v26.2 \
        -- train pretrain \
        --config examples/maxtext/configs/MI300X/llama3_70B-pretrain.yaml
  :::
  ::::
  :::::
  :::::::::

- Slurm mode: run distributed training on a Slurm cluster

  ::::::::: {.sd-tab-set .docutils}
  MI355X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      # Use a custom config file, where you can specify
      # the Docker image and set environment variables.
      ./primus-cli --config my_maxtext_config.yaml slurm srun -N 8 \
        -- train pretrain \
        --config examples/maxtext/configs/MI355X/llama3_70B-pretrain.yaml
  :::
  ::::
  :::::

  MI300X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      # Use a custom config file, where you can specify
      # the Docker image and set environment variables.
      ./primus-cli --config my_maxtext_config.yaml slurm srun -N 8 \
        -- train pretrain \
        --config examples/maxtext/configs/MI300X/llama3_70B-pretrain.yaml
  :::
  ::::
  :::::
  :::::::::
:::
::::

Standalone benchmarking

:::::::::::::: {.sd-tab-content .docutils}
The following commands are optimized for Llama 3 70B. See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v26-2){.reference .internal} to switch to another available model. Some instructions and resources might not be available for all models and configurations.

Download the Docker image and required scripts

Run the JAX MaxText benchmark tool independently by starting the Docker container as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/jax-training:maxtext-v26.2
:::
::::

Multi-node training

The following SLURM scripts will launch the Docker container and run the benchmark. Run them outside of any Docker container. The unified multi-node benchmark script accepts a configuration file that specifies the model and training parameters.

:::: {.highlight-shell .notranslate}
::: highlight
    sbatch -N <NUM_NODES> jax_maxtext_multinode_benchmark.sh <config_file.yml> [docker_image]
:::
::::

\<NUM_NODES\>

:   The number of nodes to use for training (for example, 2, 4, 8).

\<config_file.yml\>

:   Path to the YAML configuration file containing model and training parameters. Configuration files are available in the [`scripts/jax-maxtext/env_scripts/`{.docutils .literal .notranslate}]{.pre} directory for different models and GPU architectures.

\[docker_image\] (optional)

:   The Docker image to use. If not specified, it defaults to [`rocm/jax-training:maxtext-v26.2`{.docutils .literal .notranslate}]{.pre}.

For example, to run a multi-node training benchmark on Llama 3 70B:

::::::::: {.sd-tab-set .docutils}
MI355X and MI350X (gfx950)

::::: {.sd-tab-content .docutils}
:::: {.highlight-bash .notranslate}
::: highlight
    sbatch -N 4 jax_maxtext_multinode_benchmark.sh env_scripts/gfx950_llama3_70b.yml
:::
::::
:::::

MI325X and MI300X (gfx942)

::::: {.sd-tab-content .docutils}
:::: {.highlight-bash .notranslate}
::: highlight
    sbatch -N 4 jax_maxtext_multinode_benchmark.sh env_scripts/llama3_70b.yml
:::
::::
:::::
:::::::::
::::::::::::::
:::::::::::::::::
::::::::::::::::::

:::::::: {.model-doc .jax-maxtext-train-llama-3-1-8b .docutils .container}
::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to Llama 3.1 8B. See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v26-2){.reference .internal} to switch to another available model.

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
The following commands are optimized for Llama 3.1 8B. See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v26-2){.reference .internal} to switch to another available model. Some instructions and resources might not be available for all models and configurations.

Download the Docker image and required scripts

Run the JAX MaxText benchmark tool independently by starting the Docker container as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/jax-training:maxtext-v26.2
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
            rocm/jax-training:maxtext-v26.2
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

For multi-node training examples, choose a model from [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v26-2){.reference .internal} with an available [multi-node training script](https://github.com/ROCm/MAD/tree/develop/scripts/jax-maxtext/env_scripts){.reference .external}.
:::::
:::::::
::::::::

:::::::: {.model-doc .jax-maxtext-train-llama-3-1-70b .docutils .container}
::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to Llama 3.1 70B. See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v26-2){.reference .internal} to switch to another available model.

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
The following commands are optimized for Llama 3.1 70B. See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v26-2){.reference .internal} to switch to another available model. Some instructions and resources might not be available for all models and configurations.

Download the Docker image and required scripts

Run the JAX MaxText benchmark tool independently by starting the Docker container as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/jax-training:maxtext-v26.2
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
            rocm/jax-training:maxtext-v26.2
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

For multi-node training examples, choose a model from [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v26-2){.reference .internal} with an available [multi-node training script](https://github.com/ROCm/MAD/tree/develop/scripts/jax-maxtext/env_scripts){.reference .external}.
:::::
:::::::
::::::::

::::::::::::: {.model-doc .jax-maxtext-train-llama-3-1-405b .docutils .container}
:::::::::::: {.sd-tab-set .docutils}
Standalone benchmarking

::::::::::: {.sd-tab-content .docutils}
The following commands are optimized for Llama 3.1 405B (multi-node). See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v26-2){.reference .internal} to switch to another available model. Some instructions and resources might not be available for all models and configurations.

Download the Docker image and required scripts

Run the JAX MaxText benchmark tool independently by starting the Docker container as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/jax-training:maxtext-v26.2
:::
::::

Multi-node training

The following SLURM scripts will launch the Docker container and run the benchmark. Run them outside of any Docker container. The unified multi-node benchmark script accepts a configuration file that specifies the model and training parameters.

:::: {.highlight-shell .notranslate}
::: highlight
    sbatch -N <NUM_NODES> jax_maxtext_multinode_benchmark.sh <config_file.yml> [docker_image]
:::
::::

\<NUM_NODES\>

:   The number of nodes to use for training (for example, 2, 4, 8).

\<config_file.yml\>

:   Path to the YAML configuration file containing model and training parameters. Configuration files are available in the [`scripts/jax-maxtext/env_scripts/`{.docutils .literal .notranslate}]{.pre} directory for different models and GPU architectures.

\[docker_image\] (optional)

:   The Docker image to use. If not specified, it defaults to [`rocm/jax-training:maxtext-v26.2`{.docutils .literal .notranslate}]{.pre}.

For example, to run a multi-node training benchmark on Llama 3.1 405B (multi-node):

:::::: {.sd-tab-set .docutils}
MI355X and MI350X (gfx950)

::::: {.sd-tab-content .docutils}
:::: {.highlight-bash .notranslate}
::: highlight
    sbatch -N 4 jax_maxtext_multinode_benchmark.sh env_scripts/gfx950_llama3_405b.yml
:::
::::
:::::
::::::
:::::::::::
::::::::::::
:::::::::::::

::::::::::::::::::: {.model-doc .jax-maxtext-train-llama-3-3-70b .docutils .container}
:::::::::::::::::: {.sd-tab-set .docutils}
Primus benchmarking

:::: {.sd-tab-content .docutils}
::: {.model-doc .jax-maxtext-train-llama-3-3-70b .docutils .container}
The following run commands are tailored to Llama 3.3 70B. See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v26-2){.reference .internal} to switch to another available model.

Download the Docker image and required packages

1.  Pull the [`rocm/jax-training:maxtext-v26.2`{.docutils .literal .notranslate}]{.pre} Docker image from Docker Hub.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker pull rocm/jax-training:maxtext-v26.2
    :::
    ::::

2.  Run the Docker container.

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
            -v $HF_HOME:/hf_cache \
            -e HF_HOME=/hf_cache \
            -e MAD_SECRETS_HFTOKEN=$MAD_SECRETS_HFTOKEN
            --shm-size 64G \
            --name training_env \
            rocm/jax-training:maxtext-v26.2
    :::
    ::::

    Use these commands if you exit the [`training_env`{.docutils .literal .notranslate}]{.pre} container and need to return to it.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker start training_env
        docker exec -it training_env bash
    :::
    ::::

3.  Clone the Primus repository.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/AMD-AIG-AIMA/Primus.git
        cd Primus
        git checkout dev/fuyuajin/maxtext-backend-test
        git submodule update --init third_party/maxtext/
    :::
    ::::

Run the training job with primus-cli

For detailed usage instructions for [`primus-cli`{.docutils .literal .notranslate}]{.pre}, see the [Primus CLI User Guide](https://github.com/AMD-AGI/Primus/blob/main/docs/cli/PRIMUS-CLI-GUIDE.md){.reference .external}.

Use the following examples to run training with [`primus-cli`{.docutils .literal .notranslate}]{.pre}:

- Direct mode: run directly on the current host or within an existing Docker container

  ::::::::: {.sd-tab-set .docutils}
  MI355X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      ./primus-cli direct \
        -- train pretrain \
        --config examples/maxtext/configs/MI355X/llama3.3_70B-pretrain.yaml
  :::
  ::::
  :::::

  MI300X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      ./primus-cli direct \
        -- train pretrain \
        --config examples/maxtext/configs/MI300X/llama3.3_70B-pretrain.yaml
  :::
  ::::
  :::::
  :::::::::

- Container mode: run in Docker containers

  ::::::::: {.sd-tab-set .docutils}
  MI355X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      ./primus-cli container --image rocm/jax-training:maxtext-v26.2 \
        -- train pretrain \
        --config examples/maxtext/configs/MI355X/llama3.3_70B-pretrain.yaml
  :::
  ::::
  :::::

  MI300X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      ./primus-cli container --image rocm/jax-training:maxtext-v26.2 \
        -- train pretrain \
        --config examples/maxtext/configs/MI300X/llama3.3_70B-pretrain.yaml
  :::
  ::::
  :::::
  :::::::::

- Slurm mode: run distributed training on a Slurm cluster

  ::::::::: {.sd-tab-set .docutils}
  MI355X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      # Use a custom config file, where you can specify
      # the Docker image and set environment variables.
      ./primus-cli --config my_maxtext_config.yaml slurm srun -N 8 \
        -- train pretrain \
        --config examples/maxtext/configs/MI355X/llama3.3_70B-pretrain.yaml
  :::
  ::::
  :::::

  MI300X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      # Use a custom config file, where you can specify
      # the Docker image and set environment variables.
      ./primus-cli --config my_maxtext_config.yaml slurm srun -N 8 \
        -- train pretrain \
        --config examples/maxtext/configs/MI300X/llama3.3_70B-pretrain.yaml
  :::
  ::::
  :::::
  :::::::::
:::
::::

MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to Llama 3.3 70B. See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v26-2){.reference .internal} to switch to another available model.

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

:::::::::::::: {.sd-tab-content .docutils}
The following commands are optimized for Llama 3.3 70B. See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v26-2){.reference .internal} to switch to another available model. Some instructions and resources might not be available for all models and configurations.

Download the Docker image and required scripts

Run the JAX MaxText benchmark tool independently by starting the Docker container as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/jax-training:maxtext-v26.2
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
            rocm/jax-training:maxtext-v26.2
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

The following SLURM scripts will launch the Docker container and run the benchmark. Run them outside of any Docker container. The unified multi-node benchmark script accepts a configuration file that specifies the model and training parameters.

:::: {.highlight-shell .notranslate}
::: highlight
    sbatch -N <NUM_NODES> jax_maxtext_multinode_benchmark.sh <config_file.yml> [docker_image]
:::
::::

\<NUM_NODES\>

:   The number of nodes to use for training (for example, 2, 4, 8).

\<config_file.yml\>

:   Path to the YAML configuration file containing model and training parameters. Configuration files are available in the [`scripts/jax-maxtext/env_scripts/`{.docutils .literal .notranslate}]{.pre} directory for different models and GPU architectures.

\[docker_image\] (optional)

:   The Docker image to use. If not specified, it defaults to [`rocm/jax-training:maxtext-v26.2`{.docutils .literal .notranslate}]{.pre}.

For example, to run a multi-node training benchmark on Llama 3.3 70B:

::::::::: {.sd-tab-set .docutils}
MI355X and MI350X (gfx950)

::::: {.sd-tab-content .docutils}
:::: {.highlight-bash .notranslate}
::: highlight
    sbatch -N 4 jax_maxtext_multinode_benchmark.sh env_scripts/gfx950_llama3.3_70b.yml
:::
::::
:::::

MI325X and MI300X (gfx942)

::::: {.sd-tab-content .docutils}
:::: {.highlight-bash .notranslate}
::: highlight
    sbatch -N 4 jax_maxtext_multinode_benchmark.sh env_scripts/llama3.3_70b.yml
:::
::::
:::::
:::::::::
::::::::::::::
::::::::::::::::::
:::::::::::::::::::

::::::::::::::::::: {.model-doc .jax-maxtext-train-deepseek-v2-lite-16b .docutils .container}
:::::::::::::::::: {.sd-tab-set .docutils}
Primus benchmarking

:::: {.sd-tab-content .docutils}
::: {.model-doc .jax-maxtext-train-deepseek-v2-lite-16b .docutils .container}
The following run commands are tailored to DeepSeek-V2-Lite (16B). See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v26-2){.reference .internal} to switch to another available model.

Download the Docker image and required packages

1.  Pull the [`rocm/jax-training:maxtext-v26.2`{.docutils .literal .notranslate}]{.pre} Docker image from Docker Hub.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker pull rocm/jax-training:maxtext-v26.2
    :::
    ::::

2.  Run the Docker container.

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
            -v $HF_HOME:/hf_cache \
            -e HF_HOME=/hf_cache \
            -e MAD_SECRETS_HFTOKEN=$MAD_SECRETS_HFTOKEN
            --shm-size 64G \
            --name training_env \
            rocm/jax-training:maxtext-v26.2
    :::
    ::::

    Use these commands if you exit the [`training_env`{.docutils .literal .notranslate}]{.pre} container and need to return to it.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker start training_env
        docker exec -it training_env bash
    :::
    ::::

3.  Clone the Primus repository.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/AMD-AIG-AIMA/Primus.git
        cd Primus
        git checkout dev/fuyuajin/maxtext-backend-test
        git submodule update --init third_party/maxtext/
    :::
    ::::

Run the training job with primus-cli

For detailed usage instructions for [`primus-cli`{.docutils .literal .notranslate}]{.pre}, see the [Primus CLI User Guide](https://github.com/AMD-AGI/Primus/blob/main/docs/cli/PRIMUS-CLI-GUIDE.md){.reference .external}.

Use the following examples to run training with [`primus-cli`{.docutils .literal .notranslate}]{.pre}:

- Direct mode: run directly on the current host or within an existing Docker container

  ::::::::: {.sd-tab-set .docutils}
  MI355X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      ./primus-cli direct \
        -- train pretrain \
        --config examples/maxtext/configs/MI355X/deepseek_v2_16B-pretrain.yaml
  :::
  ::::
  :::::

  MI300X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      ./primus-cli direct \
        -- train pretrain \
        --config examples/maxtext/configs/MI300X/deepseek_v2_16B-pretrain.yaml
  :::
  ::::
  :::::
  :::::::::

- Container mode: run in Docker containers

  ::::::::: {.sd-tab-set .docutils}
  MI355X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      ./primus-cli container --image rocm/jax-training:maxtext-v26.2 \
        -- train pretrain \
        --config examples/maxtext/configs/MI355X/deepseek_v2_16B-pretrain.yaml
  :::
  ::::
  :::::

  MI300X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      ./primus-cli container --image rocm/jax-training:maxtext-v26.2 \
        -- train pretrain \
        --config examples/maxtext/configs/MI300X/deepseek_v2_16B-pretrain.yaml
  :::
  ::::
  :::::
  :::::::::

- Slurm mode: run distributed training on a Slurm cluster

  ::::::::: {.sd-tab-set .docutils}
  MI355X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      # Use a custom config file, where you can specify
      # the Docker image and set environment variables.
      ./primus-cli --config my_maxtext_config.yaml slurm srun -N 8 \
        -- train pretrain \
        --config examples/maxtext/configs/MI355X/deepseek_v2_16B-pretrain.yaml
  :::
  ::::
  :::::

  MI300X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      # Use a custom config file, where you can specify
      # the Docker image and set environment variables.
      ./primus-cli --config my_maxtext_config.yaml slurm srun -N 8 \
        -- train pretrain \
        --config examples/maxtext/configs/MI300X/deepseek_v2_16B-pretrain.yaml
  :::
  ::::
  :::::
  :::::::::
:::
::::

MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to DeepSeek-V2-Lite (16B). See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v26-2){.reference .internal} to switch to another available model.

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

:::::::::::::: {.sd-tab-content .docutils}
The following commands are optimized for DeepSeek-V2-Lite (16B). See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v26-2){.reference .internal} to switch to another available model. Some instructions and resources might not be available for all models and configurations.

Download the Docker image and required scripts

Run the JAX MaxText benchmark tool independently by starting the Docker container as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/jax-training:maxtext-v26.2
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
            rocm/jax-training:maxtext-v26.2
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

The following SLURM scripts will launch the Docker container and run the benchmark. Run them outside of any Docker container. The unified multi-node benchmark script accepts a configuration file that specifies the model and training parameters.

:::: {.highlight-shell .notranslate}
::: highlight
    sbatch -N <NUM_NODES> jax_maxtext_multinode_benchmark.sh <config_file.yml> [docker_image]
:::
::::

\<NUM_NODES\>

:   The number of nodes to use for training (for example, 2, 4, 8).

\<config_file.yml\>

:   Path to the YAML configuration file containing model and training parameters. Configuration files are available in the [`scripts/jax-maxtext/env_scripts/`{.docutils .literal .notranslate}]{.pre} directory for different models and GPU architectures.

\[docker_image\] (optional)

:   The Docker image to use. If not specified, it defaults to [`rocm/jax-training:maxtext-v26.2`{.docutils .literal .notranslate}]{.pre}.

For example, to run a multi-node training benchmark on DeepSeek-V2-Lite (16B):

::::::::: {.sd-tab-set .docutils}
MI355X and MI350X (gfx950)

::::: {.sd-tab-content .docutils}
:::: {.highlight-bash .notranslate}
::: highlight
    sbatch -N 4 jax_maxtext_multinode_benchmark.sh env_scripts/gfx950_deepseek2_16b.yml
:::
::::
:::::

MI325X and MI300X (gfx942)

::::: {.sd-tab-content .docutils}
:::: {.highlight-bash .notranslate}
::: highlight
    sbatch -N 4 jax_maxtext_multinode_benchmark.sh env_scripts/deepseek2_16b.yml
:::
::::
:::::
:::::::::
::::::::::::::
::::::::::::::::::
:::::::::::::::::::

::::::::::::::::::: {.model-doc .jax-maxtext-train-mixtral-8x7b .docutils .container}
:::::::::::::::::: {.sd-tab-set .docutils}
Primus benchmarking

:::: {.sd-tab-content .docutils}
::: {.model-doc .jax-maxtext-train-mixtral-8x7b .docutils .container}
The following run commands are tailored to Mixtral 8x7B. See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v26-2){.reference .internal} to switch to another available model.

Download the Docker image and required packages

1.  Pull the [`rocm/jax-training:maxtext-v26.2`{.docutils .literal .notranslate}]{.pre} Docker image from Docker Hub.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker pull rocm/jax-training:maxtext-v26.2
    :::
    ::::

2.  Run the Docker container.

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
            -v $HF_HOME:/hf_cache \
            -e HF_HOME=/hf_cache \
            -e MAD_SECRETS_HFTOKEN=$MAD_SECRETS_HFTOKEN
            --shm-size 64G \
            --name training_env \
            rocm/jax-training:maxtext-v26.2
    :::
    ::::

    Use these commands if you exit the [`training_env`{.docutils .literal .notranslate}]{.pre} container and need to return to it.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker start training_env
        docker exec -it training_env bash
    :::
    ::::

3.  Clone the Primus repository.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/AMD-AIG-AIMA/Primus.git
        cd Primus
        git checkout dev/fuyuajin/maxtext-backend-test
        git submodule update --init third_party/maxtext/
    :::
    ::::

Run the training job with primus-cli

For detailed usage instructions for [`primus-cli`{.docutils .literal .notranslate}]{.pre}, see the [Primus CLI User Guide](https://github.com/AMD-AGI/Primus/blob/main/docs/cli/PRIMUS-CLI-GUIDE.md){.reference .external}.

Use the following examples to run training with [`primus-cli`{.docutils .literal .notranslate}]{.pre}:

- Direct mode: run directly on the current host or within an existing Docker container

  ::::::::: {.sd-tab-set .docutils}
  MI355X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      ./primus-cli direct \
        -- train pretrain \
        --config examples/maxtext/configs/MI355X/mixtral_8x7B-pretrain.yaml
  :::
  ::::
  :::::

  MI300X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      ./primus-cli direct \
        -- train pretrain \
        --config examples/maxtext/configs/MI300X/mixtral_8x7B-pretrain.yaml
  :::
  ::::
  :::::
  :::::::::

- Container mode: run in Docker containers

  ::::::::: {.sd-tab-set .docutils}
  MI355X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      ./primus-cli container --image rocm/jax-training:maxtext-v26.2 \
        -- train pretrain \
        --config examples/maxtext/configs/MI355X/mixtral_8x7B-pretrain.yaml
  :::
  ::::
  :::::

  MI300X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      ./primus-cli container --image rocm/jax-training:maxtext-v26.2 \
        -- train pretrain \
        --config examples/maxtext/configs/MI300X/mixtral_8x7B-pretrain.yaml
  :::
  ::::
  :::::
  :::::::::

- Slurm mode: run distributed training on a Slurm cluster

  ::::::::: {.sd-tab-set .docutils}
  MI355X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      # Use a custom config file, where you can specify
      # the Docker image and set environment variables.
      ./primus-cli --config my_maxtext_config.yaml slurm srun -N 8 \
        -- train pretrain \
        --config examples/maxtext/configs/MI355X/mixtral_8x7B-pretrain.yaml
  :::
  ::::
  :::::

  MI300X

  ::::: {.sd-tab-content .docutils}
  :::: {.highlight-shell .notranslate}
  ::: highlight
      # Use a custom config file, where you can specify
      # the Docker image and set environment variables.
      ./primus-cli --config my_maxtext_config.yaml slurm srun -N 8 \
        -- train pretrain \
        --config examples/maxtext/configs/MI300X/mixtral_8x7B-pretrain.yaml
  :::
  ::::
  :::::
  :::::::::
:::
::::

MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
The following run command is tailored to Mixtral 8x7B. See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v26-2){.reference .internal} to switch to another available model.

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

:::::::::::::: {.sd-tab-content .docutils}
The following commands are optimized for Mixtral 8x7B. See [[Supported models]{.std .std-ref}](#amd-maxtext-model-support-v26-2){.reference .internal} to switch to another available model. Some instructions and resources might not be available for all models and configurations.

Download the Docker image and required scripts

Run the JAX MaxText benchmark tool independently by starting the Docker container as shown in the following snippet.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull rocm/jax-training:maxtext-v26.2
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
            rocm/jax-training:maxtext-v26.2
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

The following SLURM scripts will launch the Docker container and run the benchmark. Run them outside of any Docker container. The unified multi-node benchmark script accepts a configuration file that specifies the model and training parameters.

:::: {.highlight-shell .notranslate}
::: highlight
    sbatch -N <NUM_NODES> jax_maxtext_multinode_benchmark.sh <config_file.yml> [docker_image]
:::
::::

\<NUM_NODES\>

:   The number of nodes to use for training (for example, 2, 4, 8).

\<config_file.yml\>

:   Path to the YAML configuration file containing model and training parameters. Configuration files are available in the [`scripts/jax-maxtext/env_scripts/`{.docutils .literal .notranslate}]{.pre} directory for different models and GPU architectures.

\[docker_image\] (optional)

:   The Docker image to use. If not specified, it defaults to [`rocm/jax-training:maxtext-v26.2`{.docutils .literal .notranslate}]{.pre}.

For example, to run a multi-node training benchmark on Mixtral 8x7B:

::::::::: {.sd-tab-set .docutils}
MI355X and MI350X (gfx950)

::::: {.sd-tab-content .docutils}
:::: {.highlight-bash .notranslate}
::: highlight
    sbatch -N 4 jax_maxtext_multinode_benchmark.sh env_scripts/gfx950_mixtral_8x7b.yml
:::
::::
:::::

MI325X and MI300X (gfx942)

::::: {.sd-tab-content .docutils}
:::: {.highlight-bash .notranslate}
::: highlight
    sbatch -N 4 jax_maxtext_multinode_benchmark.sh env_scripts/llama3_8x7b.yml
:::
::::
:::::
:::::::::
::::::::::::::
::::::::::::::::::
:::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: {#known-issues .section}
## Known issues[\#](#known-issues "Link to this heading"){.headerlink}

- You might see NaNs in the losses when setting [`packing=True`{.docutils .literal .notranslate}]{.pre}. As a workaround, turn off input sequence packing ([`packing=False`{.docutils .literal .notranslate}]{.pre}). This will be fixed in a future release.
:::

::: {#further-reading .section}
## Further reading[\#](#further-reading "Link to this heading"){.headerlink}

- To learn more about MAD and the [`madengine`{.docutils .literal .notranslate}]{.pre} CLI, see the [MAD usage guide](https://github.com/ROCm/MAD?tab=readme-ov-file#usage-guide){.reference .external}.

- To learn more about system settings and management practices to configure your system for AMD Instinct MI300X Series GPUs, see [AMD Instinct MI300X system optimization](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi300x.html){.reference .external}.

- For a list of other ready-made Docker images for AI with ROCm, see [AMD Infinity Hub](https://www.amd.com/en/developer/resources/infinity-hub.html#f-amd_hub_category=AI%20%26%20ML%20Models){.reference .external}.
:::

::: {#previous-versions .section}
## Previous versions[\#](#previous-versions "Link to this heading"){.headerlink}

See [[JAX MaxText training performance testing version history]{.doc}](previous-versions/jax-maxtext-history.html){.reference .internal} to find documentation for previous releases of the [`ROCm/jax-training`{.docutils .literal .notranslate}]{.pre} Docker image.
:::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::: prev-next-area
[](pytorch-training.html "previous page"){.left-prev}

::: prev-next-info
previous

Training a model with PyTorch on ROCm
:::

[](mpt-llm-foundry.html "next page"){.right-next}

::: prev-next-info
next

Training MPT-30B with LLM Foundry on ROCm
:::
:::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

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
- [Known issues](#known-issues){.reference .internal .nav-link}
- [Further reading](#further-reading){.reference .internal .nav-link}
- [Previous versions](#previous-versions){.reference .internal .nav-link}
::::
:::::
::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
