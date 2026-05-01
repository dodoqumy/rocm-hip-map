---
title: "Training a model with MaxText for ROCm"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/training/benchmark-docker/previous-versions/jax-maxtext-v25.5.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-01
---

:::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

:::::::::::::::::::::::::::::::::::::::::::::: bd-content
::::::::::::::::::::::::::::::::::::::::: bd-article-container
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
# Training a model with MaxText for ROCm

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [Supported features and models](#supported-features-and-models){.reference .internal .nav-link}
  - [Unsupported features](#unsupported-features){.reference .internal .nav-link}
- [System validation](#system-validation){.reference .internal .nav-link}
- [Environment setup](#environment-setup){.reference .internal .nav-link}
  - [Multi-node setup](#multi-node-setup){.reference .internal .nav-link}
  - [Pull the Docker image](#pull-the-docker-image){.reference .internal .nav-link}
- [Getting started](#getting-started){.reference .internal .nav-link}
  - [Single node training benchmarking examples](#single-node-training-benchmarking-examples){.reference .internal .nav-link}
  - [Multi-node training benchmarking examples](#multi-node-training-benchmarking-examples){.reference .internal .nav-link}
- [Previous versions](#previous-versions){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

:::::::::::::::::::::::::: {#training-a-model-with-maxtext-for-rocm .section}
# Training a model with MaxText for ROCm[\#](#training-a-model-with-maxtext-for-rocm "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-04-21
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 10 min read time
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

MaxText is a high-performance, open-source framework built on the Google JAX machine learning library to train LLMs at scale. The MaxText framework for ROCm is an optimized fork of the upstream [AI-Hypercomputer/maxtext](https://github.com/AI-Hypercomputer/maxtext){.github .reference .external} enabling efficient AI workloads on AMD MI300X Series GPUs.

The MaxText for ROCm training Docker ([`rocm/jax-training:maxtext-v25.5`{.docutils .literal .notranslate}]{.pre}) image provides a prebuilt environment for training on AMD Instinct MI300X and MI325X GPUs, including essential components like JAX, XLA, ROCm libraries, and MaxText utilities. It includes the following software components:

::: pst-scrollable-table-container
  Software component   Version
  -------------------- ---------------------
  ROCm                 6.3.4
  JAX                  0.4.35
  Python               3.10.12
  Transformer Engine   1.12.0.dev0+b8b92dc
  hipBLASLt            0.13.0-ae9c477a
:::

::::: {#supported-features-and-models .section}
## Supported features and models[\#](#supported-features-and-models "Link to this heading"){.headerlink}

MaxText provides the following key features to train large language models efficiently:

- Transformer Engine (TE)

- Flash Attention (FA) 3

- GEMM tuning

- Multi-node support

The following models are pre-optimized for performance on AMD Instinct MI300X Series GPUs.

- Llama 3.3 70B

- Llama 3.1 8B

- Llama 3.1 70B

- Llama 3 8B

- Llama 3 70B

- Llama 2 7B

- Llama 2 70B

- DeepSeek-V2-Lite

::: {.admonition .note}
Note

Some models, such as Llama 3, require an external license agreement through a third party (for example, Meta).
:::

::: {#unsupported-features .section}
### Unsupported features[\#](#unsupported-features "Link to this heading"){.headerlink}

Currently, MaxText's default packed input format is not supported. Using this format with the current Docker image results in incorrect attention calculations across different input sequences. Support for packed input format is planned for a future release.
:::
:::::

::: {#system-validation .section}
## System validation[\#](#system-validation "Link to this heading"){.headerlink}

Before running AI workloads, it's important to validate that your AMD hardware is configured correctly and performing optimally.

If you have already validated your system settings, including aspects like NUMA auto-balancing, you can skip this step. Otherwise, complete the procedures in the [[System validation and optimization]{.std .std-ref}](../../../system-setup/prerequisite-system-validation.html#rocm-for-ai-system-optimization){.reference .internal} guide to properly configure your system settings before starting training.

To test for optimal performance, consult the recommended [[System health benchmarks]{.std .std-ref}](../../../system-setup/system-health-check.html#rocm-for-ai-system-health-bench){.reference .internal}. This suite of tests will help you verify and fine-tune your system's configuration.
:::

::::: {#environment-setup .section}
## Environment setup[\#](#environment-setup "Link to this heading"){.headerlink}

This Docker image is optimized for specific model configurations outlined as follows. Performance can vary for other training workloads, as AMD doesn't validate configurations and run conditions outside those described.

::: {#multi-node-setup .section}
[]{#amd-maxtext-multi-node-setup-v255}

### Multi-node setup[\#](#multi-node-setup "Link to this heading"){.headerlink}

For multi-node environments, ensure you have all the necessary packages for your network device, such as, RDMA. If you're not using a multi-node setup with RDMA, skip ahead to [[Pull the Docker image]{.std .std-ref}](#amd-maxtext-download-docker-v255){.reference .internal}.

1.  Install the following packages to build and install the RDMA driver.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        sudo apt install iproute2 -y
        sudo apt install -y linux-headers-"$(uname-r)" libelf-dev
        sudo apt install -y gcc make libtool autoconf librdmacm-dev rdmacm-utils infiniband-diags ibverbs-utils perftest ethtool libibverbs-dev rdma-core strace libibmad5 libibnetdisc5 ibverbs-providers libibumad-dev libibumad3 libibverbs1 libnl-3-dev libnl-route-3-dev
    :::
    ::::

    Refer to your NIC manufacturer's documentation for further steps on compiling and installing the RoCE driver. For example, for Broadcom, see [Compiling Broadcom NIC software from source](https://docs.broadcom.com/doc/957608-AN2XX#G3.484341){.reference .external} in [Ethernet networking guide for AMD Instinct MI300X GPU clusters](https://docs.broadcom.com/doc/957608-AN2XX){.reference .external}.

2.  Set the following environment variables.

    1.  Master address

        Change [`localhost`{.docutils .literal .notranslate}]{.pre} to the master node's resolvable hostname or IP address:

        :::: {.highlight-bash .notranslate}
        ::: highlight
            export MASTER_ADDR="${MASTER_ADDR:-localhost}"
        :::
        ::::

    2.  Number of nodes

        Set the number of nodes you want to train on (for example, [`2`{.docutils .literal .notranslate}]{.pre}, [`4`{.docutils .literal .notranslate}]{.pre}, or [`8`{.docutils .literal .notranslate}]{.pre}):

        :::: {.highlight-bash .notranslate}
        ::: highlight
            export NNODES="${NNODES:-1}"
        :::
        ::::

    3.  Node ranks

        Set the rank of each node ([`0`{.docutils .literal .notranslate}]{.pre} for master, [`1`{.docutils .literal .notranslate}]{.pre} for the first worker node, and so on) Node ranks should be unique across all nodes in the cluster.

        :::: {.highlight-bash .notranslate}
        ::: highlight
            export NODE_RANK="${NODE_RANK:-0}"
        :::
        ::::

    4.  Network interface

        Update the network interface in the script to match your system's network interface. To find your network interface, run the following (outside of any Docker container):

        :::: {.highlight-bash .notranslate}
        ::: highlight
            ip a
        :::
        ::::

        Look for an active interface with an IP address in the same subnet as your other nodes. Then, update the following variable in the script, for example:

        :::: {.highlight-bash .notranslate}
        ::: highlight
            export NCCL_SOCKET_IFNAME=ens50f0np0
        :::
        ::::

        This variable specifies which network interface to use for inter-node communication. Setting this variable to the incorrect interface can result in communication failures or significantly reduced performance.

    5.  RDMA interface

        Ensure the [[required packages]{.std .std-ref}](#amd-maxtext-multi-node-setup-v255){.reference .internal} are installed on all nodes. Then, set the RDMA interfaces to use for communication.

        :::: {.highlight-bash .notranslate}
        ::: highlight
            # If using Broadcom NIC
            export NCCL_IB_HCA=rdma0,rdma1,rdma2,rdma3,rdma4,rdma5,rdma6,rdma7
            # If using Mellanox NIC
            export NCCL_IB_HCA=mlx5_0,mlx5_1,mlx5_2,mlx5_3,mlx5_4,mlx5_5,mlx5_8,mlx5_9
        :::
        ::::
:::

::: {#pull-the-docker-image .section}
[]{#amd-maxtext-download-docker-v255}

### Pull the Docker image[\#](#pull-the-docker-image "Link to this heading"){.headerlink}

1.  Use the following command to pull the Docker image from Docker Hub.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker pull rocm/jax-training:maxtext-v25.5
    :::
    ::::

2.  Use the following command to launch the Docker container. Note that the benchmarking scripts used in the [[following section]{.std .std-ref}](#amd-maxtext-get-started-v255){.reference .internal} automatically launch the Docker container and execute the benchmark.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker run -it --device /dev/dri --device /dev/kfd --network host --ipc host --group-add video --cap-add SYS_PTRACE --security-opt seccomp=unconfined --privileged -v $HOME/.ssh:/root/.ssh --shm-size 128G --name maxtext_training rocm/jax-training:maxtext-v25.5
    :::
    ::::
:::
:::::

:::::: {#getting-started .section}
[]{#amd-maxtext-get-started-v255}

## Getting started[\#](#getting-started "Link to this heading"){.headerlink}

The following examples demonstrate how to get started with single node and multi-node training using the benchmarking scripts provided at [ROCm/maxtext](https://github.com/ROCm/maxtext/){.github .reference .external}.

::: {.admonition .important}
Important

The provided scripts launch a Docker container and execute a benchmark. Ensure you run these commands outside of any existing Docker container.
:::

Before running any benchmarks, ensure the [`$HF_HOME`{.docutils .literal .notranslate}]{.pre} environment variable is set correctly and points to your Hugging Face cache directory.

::: {#single-node-training-benchmarking-examples .section}
### Single node training benchmarking examples[\#](#single-node-training-benchmarking-examples "Link to this heading"){.headerlink}

- Example 1: Single node training with Llama 2 7B

  Download the benchmarking script:

  :::: {.highlight-shell .notranslate}
  ::: highlight
      wget https://raw.githubusercontent.com/ROCm/maxtext/refs/heads/main/benchmarks/gpu-rocm/llama2_7b.sh
  :::
  ::::

  Run the single node training benchmark:

  :::: {.highlight-shell .notranslate}
  ::: highlight
      IMAGE="rocm/jax-training:maxtext-v25.5" bash ./llama2_7b.sh
  :::
  ::::

- Example 2: Single node training with Llama 2 70B

  Download the benchmarking script:

  :::: {.highlight-shell .notranslate}
  ::: highlight
      wget https://raw.githubusercontent.com/ROCm/maxtext/refs/heads/main/benchmarks/gpu-rocm/llama2_70b.sh
  :::
  ::::

  Run the single node training benchmark:

  :::: {.highlight-shell .notranslate}
  ::: highlight
      IMAGE="rocm/jax-training:maxtext-v25.5" bash ./llama2_70b.sh
  :::
  ::::

- Example 3: Single node training with Llama 3 8B

  Download the benchmarking script:

  :::: {.highlight-shell .notranslate}
  ::: highlight
      wget https://raw.githubusercontent.com/ROCm/maxtext/refs/heads/main/benchmarks/gpu-rocm/llama3_8b.sh
  :::
  ::::

  Run the single node training benchmark:

  :::: {.highlight-shell .notranslate}
  ::: highlight
      IMAGE="rocm/jax-training:maxtext-v25.5" bash ./llama3_8b.sh
  :::
  ::::

- Example 4: Single node training with Llama 3 70B

  Download the benchmarking script:

  :::: {.highlight-shell .notranslate}
  ::: highlight
      wget https://raw.githubusercontent.com/ROCm/maxtext/refs/heads/main/benchmarks/gpu-rocm/llama3_70b.sh
  :::
  ::::

  Run the single node training benchmark:

  :::: {.highlight-shell .notranslate}
  ::: highlight
      IMAGE="rocm/jax-training:maxtext-v25.5" bash ./llama3_70b.sh
  :::
  ::::

- Example 5: Single node training with Llama 3.3 70B

  Download the benchmarking script:

  :::: {.highlight-shell .notranslate}
  ::: highlight
      wget https://raw.githubusercontent.com/ROCm/maxtext/refs/heads/main/benchmarks/gpu-rocm/llama3.3_70b.sh
  :::
  ::::

  Run the single node training benchmark:

  :::: {.highlight-shell .notranslate}
  ::: highlight
      IMAGE="rocm/jax-training:maxtext-v25.5" bash ./llama3.3_70b.sh
  :::
  ::::

- Example 6: Single node training with DeepSeek V2 16B

  Download the benchmarking script:

  :::: {.highlight-shell .notranslate}
  ::: highlight
      wget https://raw.githubusercontent.com/ROCm/maxtext/refs/heads/main/benchmarks/gpu-rocm/deepseek_v2_16b.sh
  :::
  ::::

  Run the single node training benchmark:

  :::: {.highlight-shell .notranslate}
  ::: highlight
      IMAGE="rocm/jax-training:maxtext-v25.5" bash ./deepseek_v2_16b.sh
  :::
  ::::

  ::: {.admonition .note}
  Note

  The reported TFLOP/s by MaxText for DeepSeek is not accurate. Use the tokens/s as a performance indicator.
  :::
:::

::: {#multi-node-training-benchmarking-examples .section}
### Multi-node training benchmarking examples[\#](#multi-node-training-benchmarking-examples "Link to this heading"){.headerlink}

The following examples use SLURM for running on multiple nodes -- the commands might need to be adjusted for your own cluster setup.

- Example 1: Multi-node training with Llama 2 7B

  Download the benchmarking script:

  :::: {.highlight-shell .notranslate}
  ::: highlight
      wget https://raw.githubusercontent.com/ROCm/maxtext/refs/heads/main/benchmarks/gpu-rocm/llama2_7b_multinode.sh
  :::
  ::::

  Run the multi-node training benchmark. For example:

  :::: {.highlight-shell .notranslate}
  ::: highlight
      sbatch -N <num_nodes> llama2_7b_multinode.sh
  :::
  ::::

- Example 2: Multi-node training with Llama 2 70B

  Download the benchmarking script:

  :::: {.highlight-shell .notranslate}
  ::: highlight
      wget https://raw.githubusercontent.com/ROCm/maxtext/refs/heads/main/benchmarks/gpu-rocm/llama2_70b_multinode.sh
  :::
  ::::

  Run the multi-node training benchmark. For example:

  :::: {.highlight-shell .notranslate}
  ::: highlight
      sbatch -N <num_nodes> llama2_70b_multinode.sh
  :::
  ::::

- Example 3: Multi-node training with Llama 3 8B model

  Download the benchmarking script:

  :::: {.highlight-shell .notranslate}
  ::: highlight
      wget https://raw.githubusercontent.com/ROCm/maxtext/refs/heads/main/benchmarks/gpu-rocm/llama3_8b_multinode.sh
  :::
  ::::

  Run the multi-node training benchmark. For example:

  :::: {.highlight-shell .notranslate}
  ::: highlight
      sbatch -N <num_nodes> llama3_8b_multinode.sh
  :::
  ::::

- Example 4: Multi-node training with Llama 3 70B model

  Download the benchmarking script:

  :::: {.highlight-shell .notranslate}
  ::: highlight
      wget https://raw.githubusercontent.com/ROCm/maxtext/refs/heads/main/benchmarks/gpu-rocm/llama3_70b_multinode.sh
  :::
  ::::

  Run the multi-node training benchmark. For example:

  :::: {.highlight-shell .notranslate}
  ::: highlight
      sbatch -N <num_nodes> llama3_70b_multinode.sh
  :::
  ::::
:::
::::::

::: {#previous-versions .section}
## Previous versions[\#](#previous-versions "Link to this heading"){.headerlink}

See [[JAX MaxText training performance testing version history]{.doc}](jax-maxtext-history.html){.reference .internal} to find documentation for previous releases of the [`ROCm/jax-training`{.docutils .literal .notranslate}]{.pre} Docker image.
:::
::::::::::::::::::::::::::

::: prev-next-area
:::
:::::::::::::::::::::::::::::::::::::::::

:::::: {.bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {.page-toc .tocsection .onthispage}
Contents
:::

- [Supported features and models](#supported-features-and-models){.reference .internal .nav-link}
  - [Unsupported features](#unsupported-features){.reference .internal .nav-link}
- [System validation](#system-validation){.reference .internal .nav-link}
- [Environment setup](#environment-setup){.reference .internal .nav-link}
  - [Multi-node setup](#multi-node-setup){.reference .internal .nav-link}
  - [Pull the Docker image](#pull-the-docker-image){.reference .internal .nav-link}
- [Getting started](#getting-started){.reference .internal .nav-link}
  - [Single node training benchmarking examples](#single-node-training-benchmarking-examples){.reference .internal .nav-link}
  - [Multi-node training benchmarking examples](#multi-node-training-benchmarking-examples){.reference .internal .nav-link}
- [Previous versions](#previous-versions){.reference .internal .nav-link}
::::
:::::
::::::
::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::
