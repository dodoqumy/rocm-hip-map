---
title: "Training a model with Megatron-LM for ROCm"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/training/benchmark-docker/previous-versions/megatron-lm-v25.4.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-01
---

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-content
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-article-container
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
# Training a model with Megatron-LM for ROCm

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [Supported features and models](#supported-features-and-models){.reference .internal .nav-link}
- [Performance measurements](#performance-measurements){.reference .internal .nav-link}
- [System validation](#system-validation){.reference .internal .nav-link}
- [Environment setup](#environment-setup){.reference .internal .nav-link}
  - [Download the Docker image](#download-the-docker-image){.reference .internal .nav-link}
  - [Configuration scripts](#configuration-scripts){.reference .internal .nav-link}
    - [Network interface](#network-interface){.reference .internal .nav-link}
    - [Dataset options](#dataset-options){.reference .internal .nav-link}
    - [Tokenizer](#tokenizer){.reference .internal .nav-link}
    - [Multi-node training](#multi-node-training){.reference .internal .nav-link}
- [Start training on AMD Instinct GPUs](#start-training-on-amd-instinct-gpus){.reference .internal .nav-link}
  - [Key options](#key-options){.reference .internal .nav-link}
  - [Benchmarking examples](#benchmarking-examples){.reference .internal .nav-link}
- [Previous versions](#previous-versions){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#training-a-model-with-megatron-lm-for-rocm .section}
# Training a model with Megatron-LM for ROCm[\#](#training-a-model-with-megatron-lm-for-rocm "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-04-21
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 15 min read time
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
:::

The Megatron-LM framework for ROCm is a specialized fork of the robust Megatron-LM, designed to enable efficient training of large-scale language models on AMD GPUs. By leveraging AMD Instinct™ MI300X Series GPUs, Megatron-LM delivers enhanced scalability, performance, and resource utilization for AI workloads. It is purpose-built to support models like Llama 2, Llama 3, Llama 3.1, and DeepSeek, enabling developers to train next-generation AI models more efficiently. See the GitHub repository at [ROCm/Megatron-LM](https://github.com/ROCm/Megatron-LM){.github .reference .external}.

AMD provides a ready-to-use Docker image for MI300X Series GPUs containing essential components, including PyTorch, ROCm libraries, and Megatron-LM utilities. It contains the following software components to accelerate training workloads:

::: pst-scrollable-table-container
  Software component   Version
  -------------------- -------------------
  ROCm                 6.3.0
  PyTorch              2.7.0a0+git637433
  Python               3.10
  Transformer Engine   1.11
  Flash Attention      3.0.0
  hipBLASLt            git258a2162
  Triton               3.1
:::

:::: {#supported-features-and-models .section}
## Supported features and models[\#](#supported-features-and-models "Link to this heading"){.headerlink}

Megatron-LM provides the following key features to train large language models efficiently:

- Transformer Engine (TE)

- APEX

- GEMM tuning

- Torch.compile

- 3D parallelism: TP + SP + CP

- Distributed optimizer

- Flash Attention (FA) 3

- Fused kernels

- Pre-training

The following models are pre-optimized for performance on AMD Instinct MI300X Series GPUs.

- Llama 3.1 8B

- Llama 3.1 70B

- Llama 3 8B

- Llama 3 70B

- Llama 2 7B

- Llama 2 70B

- DeepSeek-V2-Lite

::: {.admonition .note}
Note

Some models, such as Llama, require an external license agreement through a third party (for example, Meta).
:::
::::

:::: {#performance-measurements .section}
[]{#amd-megatron-lm-performance-measurements-v254}

## Performance measurements[\#](#performance-measurements "Link to this heading"){.headerlink}

To evaluate performance, the [Performance results with AMD ROCm software](https://www.amd.com/en/developer/resources/rocm-hub/dev-ai/performance-results.html#tabs-a8deaeb413-item-21cea50186-tab){.reference .external} page provides reference throughput and latency measurements for training popular AI models.

::: {.admonition .important}
Important

The performance data presented in [Performance results with AMD ROCm software](https://www.amd.com/en/developer/resources/rocm-hub/dev-ai/performance-results.html){.reference .external} only reflects the [[latest version of this training benchmarking environment]{.doc}](../megatron-lm.html){.reference .internal}. The listed measurements should not be interpreted as the peak performance achievable by AMD Instinct MI325X and MI300X GPUs or ROCm software.
:::
::::

::: {#system-validation .section}
## System validation[\#](#system-validation "Link to this heading"){.headerlink}

If you have already validated your system settings, including NUMA auto-balancing, skip this step. Otherwise, complete the [[system validation and optimization steps]{.std .std-ref}](../../../system-setup/prerequisite-system-validation.html#train-a-model-system-validation){.reference .internal} to set up your system before starting training.
:::

::::::::::::::::::::::::::::::::: {#environment-setup .section}
[]{#mi300x-amd-megatron-lm-training-v254}

## Environment setup[\#](#environment-setup "Link to this heading"){.headerlink}

The prebuilt ROCm Megatron-LM environment allows users to quickly validate system performance, conduct training benchmarks, and achieve superior performance for models like Llama 3.1, Llama 2, and DeepSeek V2.

Use the following instructions to set up the environment, configure the script to train models, and reproduce the benchmark results on MI300X Series GPUs with the AMD Megatron-LM Docker image.

::: {#download-the-docker-image .section}
[]{#amd-megatron-lm-requirements-v254}

### Download the Docker image[\#](#download-the-docker-image "Link to this heading"){.headerlink}

1.  Use the following command to pull the Docker image from Docker Hub.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker pull rocm/megatron-lm:v25.4
    :::
    ::::

2.  Launch the Docker container.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker run -it --device /dev/dri --device /dev/kfd --device /dev/infiniband --network host --ipc host --group-add video --cap-add SYS_PTRACE --security-opt seccomp=unconfined --privileged -v $HOME:$HOME -v  $HOME/.ssh:/root/.ssh --shm-size 64G --name megatron_training_env rocm/megatron-lm:v25.4
    :::
    ::::

3.  Use these commands if you exit the [`megatron_training_env`{.docutils .literal .notranslate}]{.pre} container and need to return to it.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker start megatron_training_env
        docker exec -it megatron_training_env bash
    :::
    ::::

The Docker container includes a pre-installed, verified version of the ROCm Megatron-LM development branch [ROCm/Megatron-LM](https://github.com/ROCm/Megatron-LM/tree/rocm_dev){.github .reference .external} (commit [fd6f01](https://github.com/ROCm/Megatron-LM/tree/fd6f0d11d7f9480ace32f22eb7e4dab5314fa350){.reference .external}).
:::

::::::::::::::::::::::::::::::: {#configuration-scripts .section}
[]{#amd-megatron-lm-environment-setup-v254}

### Configuration scripts[\#](#configuration-scripts "Link to this heading"){.headerlink}

::::: {.sd-tab-set .docutils}
Llama

::: {.sd-tab-content .docutils}
If you're working with Llama 2 7B or Llama 2 70 B, use the [`train_llama2.sh`{.docutils .literal .notranslate}]{.pre} configuration script in the [`examples/llama`{.docutils .literal .notranslate}]{.pre} directory of [ROCm/Megatron-LM](https://github.com/ROCm/Megatron-LM/tree/rocm_dev/examples/llama){.github .reference .external}. Likewise, if you're working with Llama 3 or Llama 3.1, use [`train_llama3.sh`{.docutils .literal .notranslate}]{.pre} and update the configuration script accordingly.
:::

DeepSeek V2

::: {.sd-tab-content .docutils}
Use the [`train_deepseek_v2.sh`{.docutils .literal .notranslate}]{.pre} configuration script in the [`examples/deepseek_v2`{.docutils .literal .notranslate}]{.pre} directory of [ROCm/Megatron-LM](https://github.com/ROCm/Megatron-LM/tree/rocm_dev/examples/deepseek_v2){.github .reference .external} and update the configuration script accordingly.
:::
:::::

::::::::: {#network-interface .section}
#### Network interface[\#](#network-interface "Link to this heading"){.headerlink}

:::::::: {.sd-tab-set .docutils}
Llama

::::::: {.sd-tab-content .docutils}
Update the network interface in the script to match your system's network interface. To find your network interface, run the following (outside of any Docker container):

:::: {.highlight-bash .notranslate}
::: highlight
    ip a
:::
::::

Look for an active interface that has an IP address in the same subnet as your other nodes. Then, update the following variables in the script, for example:

:::: {.highlight-bash .notranslate}
::: highlight
    export NCCL_SOCKET_IFNAME=ens50f0np0

    export GLOO_SOCKET_IFNAME=ens50f0np0
:::
::::
:::::::
::::::::
:::::::::

:::::::: {#dataset-options .section}
#### Dataset options[\#](#dataset-options "Link to this heading"){.headerlink}

::::::: {.sd-tab-set .docutils}
Llama

::: {.sd-tab-content .docutils}
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

  To download the dataset, set the [`DATASET`{.docutils .literal .notranslate}]{.pre} variable to the dataset you'd like to use. Two datasets are supported: [`DATASET=wiki`{.docutils .literal .notranslate}]{.pre} and [`DATASET=bookcorpus`{.docutils .literal .notranslate}]{.pre}. Use the following command to download the dataset.

  :::: {.highlight-shell .notranslate}
  ::: highlight
      DATASET=wiki bash examples/llama/prepare_dataset.sh # For wiki-en dataset
      DATASET=bookcorpus bash examples/llama/prepare_dataset.sh # For bookcorpus dataset
  :::
  ::::
:::

DeepSeek V2

::::: {.sd-tab-content .docutils}
If you don't already have the dataset, download the DeepSeek dataset using the following commands:

:::: {.highlight-shell .notranslate}
::: highlight
    mkdir deepseek-datasets
    cd deepseek-datasets
    wget https://atp-modelzoo-wlcb-pai.oss-cn-wulanchabu.aliyuncs.com/release/models/pai-megatron-patch/deepseek-datasets/SlimPajama.json
    wget https://atp-modelzoo-wlcb-pai.oss-cn-wulanchabu.aliyuncs.com/release/models/pai-megatron-patch/deepseek-datasets/alpaca_zh-train.json
    wget https://atp-modelzoo-wlcb-pai.oss-cn-wulanchabu.aliyuncs.com/release/models/pai-megatron-patch/deepseek-datasets/alpaca_zh-valid.json
    wget https://atp-modelzoo-wlcb-pai.oss-cn-wulanchabu.aliyuncs.com/release/models/pai-megatron-patch/deepseek-datasets/mmap_deepseekv2_datasets_text_document.bin
    wget https://atp-modelzoo-wlcb-pai.oss-cn-wulanchabu.aliyuncs.com/release/models/pai-megatron-patch/deepseek-datasets/mmap_deepseekv2_datasets_text_document.idx
:::
::::

You can use either mock data or real data for training.

- Mock data can be useful for testing and validation. Use the [`MOCK_DATA`{.docutils .literal .notranslate}]{.pre} variable to toggle between mock and real data. The default value is [`1`{.docutils .literal .notranslate}]{.pre} for enabled.

  :::: {.highlight-bash .notranslate}
  ::: highlight
      MOCK_DATA=1
  :::
  ::::

- If you're using a real dataset, update the [`DATA_DIR`{.docutils .literal .notranslate}]{.pre} variable to point to the location of your dataset.

  :::: {.highlight-bash .notranslate}
  ::: highlight
      MOCK_DATA=0

      DATA_DIR="/root/data/deepseek-datasets"  # Change to where your dataset is stored
  :::
  ::::

  Ensure that the files are accessible inside the Docker container.
:::::
:::::::
::::::::

::::::::::: {#tokenizer .section}
#### Tokenizer[\#](#tokenizer "Link to this heading"){.headerlink}

Tokenization is the process of converting raw text into tokens that can be processed by the model. For Llama models, this typically involves sub-word tokenization, where words are broken down into smaller units based on a fixed vocabulary. The tokenizer is trained along with the model on a large corpus of text, and it learns a fixed vocabulary that can represent a wide range of text from different domains. This allows Llama models to handle a variety of input sequences, including unseen words or domain-specific terms.

You can assign the path of an existing tokenizer to the [`TOKENIZER_MODEL`{.docutils .literal .notranslate}]{.pre} as shown in the following examples. If the tokenizer is not found, it'll be downloaded to the default tokenizer model path: [`${DATA_DIR}/tokenizer_llama3`{.docutils .literal .notranslate}]{.pre} or [`${DATA_DIR}/tokenizer_llama2`{.docutils .literal .notranslate}]{.pre}.

:::::::::: {.sd-tab-set .docutils}
Llama

:::::::: {.sd-tab-content .docutils}
To train any of the Llama 2 models that [[this Docker image supports]{.std .std-ref}](#amd-megatron-lm-model-support-25-4){.reference .internal}, use the [`Llama2Tokenizer`{.docutils .literal .notranslate}]{.pre} or the default [`HuggingFaceTokenizer`{.docutils .literal .notranslate}]{.pre}.

To train any of Llama 3 and Llama 3.1 models that this Docker image supports, use the [`HuggingFaceTokenizer`{.docutils .literal .notranslate}]{.pre}. Set the Hugging Face model path in the [`TOKENIZER_MODEL`{.docutils .literal .notranslate}]{.pre} variable.

For example, if you're using the Llama 3.1 8B model:

:::: {.highlight-shell .notranslate}
::: highlight
    TOKENIZER_MODEL=meta-llama/Llama-3.1-8B
:::
::::

::::: {.admonition .note}
Note

If you don't already have the Llama 3.1 tokenizer locally, set your personal Hugging Face access token [`HF_TOKEN`{.docutils .literal .notranslate}]{.pre} to download the tokenizer. If you encounter the following error, set [`HF_TOKEN`{.docutils .literal .notranslate}]{.pre} to your access-authorized Hugging Face token.

:::: {.highlight-shell .notranslate}
::: highlight
    OSError: You are trying to access a gated repo.

    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token
:::
::::
:::::
::::::::

DeepSeek V2

::: {.sd-tab-content .docutils}
To train any of the DeepSeek V2 models that [[this Docker image supports]{.std .std-ref}](#amd-megatron-lm-model-support-25-4){.reference .internal}, use the [`DeepSeekV2Tokenizer`{.docutils .literal .notranslate}]{.pre}.
:::
::::::::::
:::::::::::

::::: {#multi-node-training .section}
#### Multi-node training[\#](#multi-node-training "Link to this heading"){.headerlink}

:::: {.sd-tab-set .docutils}
Llama

::: {.sd-tab-content .docutils}
If you're running multi-node training, update the following environment variables. They can also be passed as command line arguments.

- Change [`localhost`{.docutils .literal .notranslate}]{.pre} to the master node's hostname:

  :::: {.highlight-shell .notranslate}
  ::: highlight
      MASTER_ADDR="${MASTER_ADDR:-localhost}"
  :::
  ::::

- Set the number of nodes you want to train on (for instance, [`2`{.docutils .literal .notranslate}]{.pre}, [`4`{.docutils .literal .notranslate}]{.pre}, [`8`{.docutils .literal .notranslate}]{.pre}):

  :::: {.highlight-shell .notranslate}
  ::: highlight
      NNODES="${NNODES:-1}"
  :::
  ::::

- Set the rank of each node (0 for master, 1 for the first worker node, and so on):

  :::: {.highlight-shell .notranslate}
  ::: highlight
      NODE_RANK="${NODE_RANK:-0}"
  :::
  ::::

- Set [`DATA_CACHE_PATH`{.docutils .literal .notranslate}]{.pre} to a common directory accessible by all the nodes (for example, an NFS directory) for multi-node runs:

  :::: {.highlight-shell .notranslate}
  ::: highlight
      DATA_CACHE_PATH=/root/cache # Set to a common directory for multi-node runs
  :::
  ::::

- For multi-node runs, make sure the correct network drivers are installed on the nodes. If inside a Docker container, either install the drivers inside the Docker container or pass the network drivers from the host while creating the Docker container.

  :::: {.highlight-shell .notranslate}
  ::: highlight
      # Specify which RDMA interfaces to use for communication
      export NCCL_IB_HCA=rdma0,rdma1,rdma2,rdma3,rdma4,rdma5,rdma6,rdma7
  :::
  ::::
:::
::::
:::::
:::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::: {#start-training-on-amd-instinct-gpus .section}
## Start training on AMD Instinct GPUs[\#](#start-training-on-amd-instinct-gpus "Link to this heading"){.headerlink}

The prebuilt Megatron-LM with ROCm training environment allows users to quickly validate system performance, conduct training benchmarks, and achieve superior performance for models like Llama 3.1 and Llama 2. This container should not be expected to provide generalized performance across all training workloads. You can expect the container to perform in the model configurations described in the following section, but other configurations are not validated by AMD.

Use the following instructions to set up the environment, configure the script to train models, and reproduce the benchmark results on MI300X Series GPUs with the AMD Megatron-LM Docker image.

::::::::::: {.sd-tab-set .docutils}
Llama

::::::: {.sd-tab-content .docutils}
:::::: {.sd-tab-set .docutils}
Single node training

:::: {.sd-tab-content .docutils}
To run training on a single node, navigate to the Megatron-LM folder and use one of the following commands.

- For Llama 3.1 8B FP8:

  :::: {.highlight-shell .notranslate}
  ::: highlight
      TEE_OUTPUT=1 MBS=2 BS=128 TP=1 TE_FP8=1 SEQ_LENGTH=8192 MODEL_SIZE=8 TOTAL_ITERS=50 bash examples/llama/train_llama3.sh
  :::
  ::::

- For Llama 3.1 8B BF16:

  :::: {.highlight-shell .notranslate}
  ::: highlight
      TEE_OUTPUT=1 MBS=2 BS=128 TP=1 TE_FP8=0 SEQ_LENGTH=8192 MODEL_SIZE=8 TOTAL_ITERS=50 bash examples/llama/train_llama3.sh
  :::
  ::::

- For Llama 2 7B FP8:

  :::: {.highlight-shell .notranslate}
  ::: highlight
      TEE_OUTPUT=1 MBS=4 BS=256 TP=1 TE_FP8=1 SEQ_LENGTH=4096 MODEL_SIZE=7 TOTAL_ITERS=50 bash examples/llama/train_llama2.sh
  :::
  ::::

- For Llama 2 7B BF16:

  :::: {.highlight-shell .notranslate}
  ::: highlight
      TEE_OUTPUT=1 MBS=4 BS=256 TP=1 TE_FP8=0 SEQ_LENGTH=4096 MODEL_SIZE=7 TOTAL_ITERS=50 bash examples/llama/train_llama2.sh
  :::
  ::::

To run training with FSDP2 enabled, add the [`FSDP=1`{.docutils .literal .notranslate}]{.pre} argument. For example:

- For Llama 3 70B BF16:

  :::: {.highlight-shell .notranslate}
  ::: highlight
      TEE_OUTPUT=1 MBS=3 BS=24 TP=1 TE_FP8=0 FSDP=1 RECOMPUTE=1 SEQ_LENGTH=8192 MODEL_SIZE=70 TOTAL_ITERS=50 bash examples/llama/train_llama3.sh
  :::
  ::::

- For Llama 2 70B BF16:

  :::: {.highlight-shell .notranslate}
  ::: highlight
      TEE_OUTPUT=1 MBS=3 BS=56 TP=1 TE_FP8=0 FSDP=1 RECOMPUTE=1 SEQ_LENGTH=4096 MODEL_SIZE=70 TOTAL_ITERS=50 bash examples/llama/train_llama2.sh
  :::
  ::::

::: {.admonition .note}
Note

It's suggested to use [`TP=1`{.docutils .literal .notranslate}]{.pre} when FSDP is enabled for higher throughput. FSDP2 is not supported with pipeline parallelism, expert parallelism, MCore's distributed optimizer, gradient accumulation fusion, and [`FP16`{.docutils .literal .notranslate}]{.pre} precision.
:::
::::

Multi-node training

::: {.sd-tab-content .docutils}
To run training on multiple nodes, launch the Docker container on each node. For example, for a two node setup ([`NODE0`{.docutils .literal .notranslate}]{.pre} as the master node), use these commands.

- On the master node [`NODE0`{.docutils .literal .notranslate}]{.pre}:

  :::: {.highlight-shell .notranslate}
  ::: highlight
      TEE_OUTPUT=1 MBS=2 BS=256 TP=1 TE_FP8=1 SEQ_LENGTH=8192 MODEL_SIZE=8 MASTER_ADDR=IP_NODE0 NNODES=2 NODE_RANK=0 bash examples/llama/train_llama3.sh
  :::
  ::::

- On the worker node [`NODE1`{.docutils .literal .notranslate}]{.pre}:

  :::: {.highlight-shell .notranslate}
  ::: highlight
      TEE_OUTPUT=1 MBS=2 BS=256 TP=1 TE_FP8=1 SEQ_LENGTH=8192 MODEL_SIZE=8 MASTER_ADDR=IP_NODE0 NNODES=2 NODE_RANK=1 bash examples/llama/train_llama3.sh
  :::
  ::::
:::
::::::
:::::::

DeepSeek V2

::::: {.sd-tab-content .docutils}
To run the training on a single node, go to [`/Megatron-LM`{.docutils .literal .notranslate}]{.pre} folder and use the following command:

:::: {.highlight-shell .notranslate}
::: highlight
    cd /workspace/Megatron-LM
    GEMM_TUNING=1 PR=bf16 MBS=4 AC=none SEQ_LEN=4096 PAD_LEN=4096 TRAIN_ITERS=50 bash examples/deepseek_v2/train_deepseekv2.sh
:::
::::
:::::
:::::::::::

:::::: {#key-options .section}
### Key options[\#](#key-options "Link to this heading"){.headerlink}

The benchmark tests support the following sets of variables:

::::: {.sd-tab-set .docutils}
Llama

::: {.sd-tab-content .docutils}

[`TEE_OUTPUT`{.docutils .literal .notranslate}]{.pre}

:   [`1`{.docutils .literal .notranslate}]{.pre} to enable training logs or [`0`{.docutils .literal .notranslate}]{.pre} to disable.

[`TE_FP8`{.docutils .literal .notranslate}]{.pre}

:   [`0`{.docutils .literal .notranslate}]{.pre} for B16 or [`1`{.docutils .literal .notranslate}]{.pre} for FP8 -- [`0`{.docutils .literal .notranslate}]{.pre} by default.

[`GEMM_TUNING`{.docutils .literal .notranslate}]{.pre}

:   [`1`{.docutils .literal .notranslate}]{.pre} to enable GEMM tuning, which boosts performance by using the best GEMM kernels.

[`USE_FLASH_ATTN`{.docutils .literal .notranslate}]{.pre}

:   [`1`{.docutils .literal .notranslate}]{.pre} to enable Flash Attention.

[`FSDP`{.docutils .literal .notranslate}]{.pre}

:   [`1`{.docutils .literal .notranslate}]{.pre} to enable PyTorch FSDP2. If FSDP is enabled, [`--use-distributed-optimizer`{.docutils .literal .notranslate}]{.pre}, [`--overlap-param-gather`{.docutils .literal .notranslate}]{.pre}, and [`--sequence-parallel`{.docutils .literal .notranslate}]{.pre} are automaticallyu disabled.

[`ENABLE_PROFILING`{.docutils .literal .notranslate}]{.pre}

:   [`1`{.docutils .literal .notranslate}]{.pre} to enable PyTorch profiling for performance analysis.

[`transformer-impl`{.docutils .literal .notranslate}]{.pre}

:   [`transformer_engine`{.docutils .literal .notranslate}]{.pre} to use the Transformer Engine (TE) or [`local`{.docutils .literal .notranslate}]{.pre} to disable TE.

[`MODEL_SIZE`{.docutils .literal .notranslate}]{.pre}

:   [`8B`{.docutils .literal .notranslate}]{.pre} or [`70B`{.docutils .literal .notranslate}]{.pre} for Llama 3 and 3.1. [`7B`{.docutils .literal .notranslate}]{.pre} or [`70B`{.docutils .literal .notranslate}]{.pre} for Llama 2.

[`TOTAL_ITERS`{.docutils .literal .notranslate}]{.pre}

:   The total number of iterations -- [`10`{.docutils .literal .notranslate}]{.pre} by default.

[`MOCK_DATA`{.docutils .literal .notranslate}]{.pre}

:   [`1`{.docutils .literal .notranslate}]{.pre} to use mock data or [`0`{.docutils .literal .notranslate}]{.pre} to use real data you provide.

[`MBS`{.docutils .literal .notranslate}]{.pre}

:   Micro batch size.

[`BS`{.docutils .literal .notranslate}]{.pre}

:   Global batch size.

[`TP`{.docutils .literal .notranslate}]{.pre}

:   Tensor parallel ([`1`{.docutils .literal .notranslate}]{.pre}, [`2`{.docutils .literal .notranslate}]{.pre}, [`4`{.docutils .literal .notranslate}]{.pre}, [`8`{.docutils .literal .notranslate}]{.pre}). [`TP`{.docutils .literal .notranslate}]{.pre} is disabled when [`FSDP`{.docutils .literal .notranslate}]{.pre} is turned on.

[`SEQ_LENGTH`{.docutils .literal .notranslate}]{.pre}

:   Input sequence length.
:::

DeepSeek V2

::: {.sd-tab-content .docutils}

[`PR`{.docutils .literal .notranslate}]{.pre}

:   Precision for training. [`bf16`{.docutils .literal .notranslate}]{.pre} for BF16 (default) or [`fp8`{.docutils .literal .notranslate}]{.pre} for FP8 GEMMs.

[`GEMM_TUNING`{.docutils .literal .notranslate}]{.pre}

:   [`1`{.docutils .literal .notranslate}]{.pre} to enable GEMM tuning, which boosts performance by using the best GEMM kernels.

[`TRAIN_ITERS`{.docutils .literal .notranslate}]{.pre}

:   The total number of iterations.

[`MOCK_DATA`{.docutils .literal .notranslate}]{.pre}

:   [`1`{.docutils .literal .notranslate}]{.pre} to use mock data or [`0`{.docutils .literal .notranslate}]{.pre} to use real data you provide.

[`MBS`{.docutils .literal .notranslate}]{.pre}

:   Micro batch size.

[`GBS`{.docutils .literal .notranslate}]{.pre}

:   Global batch size.

[`SEQ_LEN`{.docutils .literal .notranslate}]{.pre}

:   Input sequence length.

[`AC`{.docutils .literal .notranslate}]{.pre}

:   Activation checkpointing ([`none`{.docutils .literal .notranslate}]{.pre}, [`sel`{.docutils .literal .notranslate}]{.pre}, or [`full`{.docutils .literal .notranslate}]{.pre}) -- [`sel`{.docutils .literal .notranslate}]{.pre} by default.
:::
:::::
::::::

:::::::::::::: {#benchmarking-examples .section}
### Benchmarking examples[\#](#benchmarking-examples "Link to this heading"){.headerlink}

::::::::::::: {.sd-tab-set .docutils}
Llama

:::::::::::: {.sd-tab-content .docutils}
::::::::::: {.sd-tab-set .docutils}
Single node training

::::: {.sd-tab-content .docutils}
Use this command to run training with Llama 2 7B model on a single node. You can specify MBS, BS, FP, datatype, and so on.

:::: {.highlight-bash .notranslate}
::: highlight
    TEE_OUTPUT=1 MBS=5 BS=120 TP=8 TE_FP8=0 NO_TORCH_COMPILE=1
    SEQ_LENGTH=4096 bash examples/llama/train_llama2.sh
:::
::::

You can find the training logs at the location defined in [`$TRAIN_LOG`{.docutils .literal .notranslate}]{.pre} in the [[configuration script]{.std .std-ref}](#amd-megatron-lm-environment-setup-v254){.reference .internal}.

See the sample output:

[![](../../../../../_images/llama2-7b-training-log-sample.png){style="width: 800px;"}](../../../../../_images/llama2-7b-training-log-sample.png){.reference .internal .image-reference}
:::::

Multi-node training

::::::: {.sd-tab-content .docutils}
Launch the Docker container on each node.

In this example, run training with Llama 2 7B model on 2 nodes with specific MBS, BS, FP, datatype, and so on.

On the master node:

:::: {.highlight-bash .notranslate}
::: highlight
    TEE_OUTPUT=1 MBS=4 BS=64 TP=8 TE_FP8=0 NO_TORCH_COMPILE=1
    SEQ_LENGTH=4096 bash examples/llama/train_llama2.sh
:::
::::

On the worker node:

:::: {.highlight-bash .notranslate}
::: highlight
    TEE_OUTPUT=1 MBS=4 BS=64 TP=8 TE_FP8=0 NO_TORCH_COMPILE=1
    SEQ_LENGTH=4096 bash examples/llama/train_llama2.sh
:::
::::

You can find the training logs at the location defined in [`$TRAIN_LOG`{.docutils .literal .notranslate}]{.pre} in the [[configuration script]{.std .std-ref}](#amd-megatron-lm-environment-setup-v254){.reference .internal}.

Sample output for 2-node training:

Master node:

[![](../../../../../_images/2-node-training-master.png){style="width: 800px;"}](../../../../../_images/2-node-training-master.png){.reference .internal .image-reference}

Worker node:

[![](../../../../../_images/2-node-training-worker.png){style="width: 800px;"}](../../../../../_images/2-node-training-worker.png){.reference .internal .image-reference}
:::::::
:::::::::::
::::::::::::
:::::::::::::
::::::::::::::
::::::::::::::::::::::::::::

::: {#previous-versions .section}
## Previous versions[\#](#previous-versions "Link to this heading"){.headerlink}

See [[Megatron-LM training performance testing version history]{.doc}](megatron-lm-history.html){.reference .internal} to find documentation for previous releases of the [`ROCm/megatron-lm`{.docutils .literal .notranslate}]{.pre} Docker image.
:::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: prev-next-area
:::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::: {.bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {.page-toc .tocsection .onthispage}
Contents
:::

- [Supported features and models](#supported-features-and-models){.reference .internal .nav-link}
- [Performance measurements](#performance-measurements){.reference .internal .nav-link}
- [System validation](#system-validation){.reference .internal .nav-link}
- [Environment setup](#environment-setup){.reference .internal .nav-link}
  - [Download the Docker image](#download-the-docker-image){.reference .internal .nav-link}
  - [Configuration scripts](#configuration-scripts){.reference .internal .nav-link}
    - [Network interface](#network-interface){.reference .internal .nav-link}
    - [Dataset options](#dataset-options){.reference .internal .nav-link}
    - [Tokenizer](#tokenizer){.reference .internal .nav-link}
    - [Multi-node training](#multi-node-training){.reference .internal .nav-link}
- [Start training on AMD Instinct GPUs](#start-training-on-amd-instinct-gpus){.reference .internal .nav-link}
  - [Key options](#key-options){.reference .internal .nav-link}
  - [Benchmarking examples](#benchmarking-examples){.reference .internal .nav-link}
- [Previous versions](#previous-versions){.reference .internal .nav-link}
::::
:::::
::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
