---
title: "Multi-node setup for AI workloads"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/system-setup/multi-node-setup.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-01
---

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-content
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-article-container
:::::::::: {.bd-header-article .d-print-none}
::::::::: {.header-article-items .header-article__inner}
::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}
:::

::: header-article-item
- [](../../../index.html){.nav-link aria-label="Home"}
- [Use ROCm for AI](../index.html){.nav-link}
- [System setup for AI workloads on ROCm](index.html){.nav-link}
- Multi-node\...
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
# Multi-node setup for AI workloads

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [Prerequisites](#prerequisites){.reference .internal .nav-link}
- [Install required packages](#install-required-packages){.reference .internal .nav-link}
  - [Compile and install the RoCE library](#compile-and-install-the-roce-library){.reference .internal .nav-link}
- [Environment setup](#environment-setup){.reference .internal .nav-link}
  - [Master address](#master-address){.reference .internal .nav-link}
  - [Number of nodes](#number-of-nodes){.reference .internal .nav-link}
  - [Node ranks](#node-ranks){.reference .internal .nav-link}
  - [Network interface](#network-interface){.reference .internal .nav-link}
  - [RDMA/IB interface](#rdma-ib-interface){.reference .internal .nav-link}
  - [Global ID index](#global-id-index){.reference .internal .nav-link}
- [Multi-node training examples](#multi-node-training-examples){.reference .internal .nav-link}
  - [JAX MaxText](#jax-maxtext){.reference .internal .nav-link}
  - [PyTorch training](#pytorch-training){.reference .internal .nav-link}
  - [Megatron-LM](#megatron-lm){.reference .internal .nav-link}
- [Further reading](#further-reading){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#multi-node-setup-for-ai-workloads .section}
[]{#rocm-for-ai-multi-node-setup}

# Multi-node setup for AI workloads[\#](#multi-node-setup-for-ai-workloads "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 9 min read time
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

AMD provides ready-to-use Docker images for AMD Instinct™ MI300X and MI325X GPUs containing ROCm-capable deep learning frameworks and essential software components. These Docker images can run and leverage multiple nodes if they are available. This page describes how to enable the multi-node training of AI workloads on AMD Instinct GPUs.

::: {#prerequisites .section}
## Prerequisites[\#](#prerequisites "Link to this heading"){.headerlink}

Before starting, ensure your environment meets the following requirements:

- Multi-node networking: your cluster should have a configured multi-node network. For setup instructions, see the [Multi-node network configuration for AMD Instinct GPUs](https://instinct.docs.amd.com/projects/gpu-cluster-networking/en/latest/how-to/multi-node-config.html){.reference .external} guide in the Instinct documentation.

- ROCm Docker container to simplify environment setup for AI workloads. See the following resources to get started:

  - [[Training a model with Megatron-LM and ROCm]{.doc}](../training/benchmark-docker/megatron-lm.html){.reference .internal}

  - [[Training a model with PyTorch and ROCm]{.doc}](../training/benchmark-docker/pytorch-training.html){.reference .internal}

  - [[Training a model with JAX MaxText and ROCm]{.doc}](../training/benchmark-docker/jax-maxtext.html){.reference .internal}

- Slurm workload manager to run the [[provided examples]{.std .std-ref}](#multi-node-setup-training-examples){.reference .internal}.
:::

::::::: {#install-required-packages .section}
## Install required packages[\#](#install-required-packages "Link to this heading"){.headerlink}

To run multi-node workloads, ensure you have all the required packages installed based on your network device. For example, on Ubuntu systems:

:::: {.highlight-shell .notranslate}
::: highlight
    apt install -y iproute2

    apt install -y linux-headers-"$(uname -r)" libelf-dev

    apt install -y gcc make libtool autoconf librdmacm-dev rdmacm-utils infiniband-diags ibverbs-utils perftest ethtool libibverbs-dev rdma-core strace libibmad5 libibnetdisc5 ibverbs-providers libibumad-dev libibumad3 libibverbs1 libnl-3-dev libnl-route-3-dev
:::
::::

:::: {#compile-and-install-the-roce-library .section}
### Compile and install the RoCE library[\#](#compile-and-install-the-roce-library "Link to this heading"){.headerlink}

If you're using Broadcom NICs, you need to compile and install the RoCE (RDMA over Converged Ethernet) library. See [RoCE cluster network configuration guide for AMD Instinct GPUs](https://instinct.docs.amd.com/projects/gpu-cluster-networking/en/latest/how-to/roce-network-config.html){.reference .external} for more information.

See the [Ethernet networking guide for AMD Instinct MI300X GPU clusters: Compiling Broadcom NIC software from source](https://docs.broadcom.com/doc/957608-AN2XX#page=81){.reference .external} for more details.

::: {.admonition .important}
Important

It is crucial to install the exact same version of the RoCE library that is installed on your host system. Also, ensure that the path to these libraries on the host is correctly mounted into your Docker container. Failure to do so can lead to compatibility issues and communication failures.
:::

1.  Set [`BUILD_DIR`{.docutils .literal .notranslate}]{.pre} to the path on the host system where the Broadcom drivers and [`bnxt_rocelib`{.docutils .literal .notranslate}]{.pre} source are located. Then, navigate to the [`bnxt_rocelib`{.docutils .literal .notranslate}]{.pre} directory.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export BUILD_DIR=/path/to/your/broadcom_drivers_on_host
        cd $BUILD_DIR/drivers_linux/bnxt_rocelib/
    :::
    ::::

2.  The [`bnxt_rocelib`{.docutils .literal .notranslate}]{.pre} directory contains a version of [`libbnxt_re`{.docutils .literal .notranslate}]{.pre} in a zipped [`.tar.gz`{.docutils .literal .notranslate}]{.pre} file.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        tar -xf libbnxt_re-a.b.c.d.tar.gz
        cd libbnxt_re-a.b.c.d
    :::
    ::::

3.  Compile and install the RoCE library.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        sh autogen.sh
        ./configure
        make
        find /usr/lib64/ /usr/lib -name "libbnxt_re-rdmav*.so" -exec mv {} {}.inbox \;
        make install all
        sh -c "echo /usr/local/lib >> /etc/ld.so.conf"
        ldconfig
        cp -f bnxt_re.driver /etc/libibverbs.d/
        find . -name "*.so" -exec md5sum {} \;
        BUILT_MD5SUM=$(find . -name "libbnxt_re-rdmav*.so" -exec md5sum {} \; | cut -d " " -f 1)
    :::
    ::::
::::
:::::::

::::::::::::::::::::::::::::::: {#environment-setup .section}
## Environment setup[\#](#environment-setup "Link to this heading"){.headerlink}

Before running multi-node workloads, set these essential environment variables:

::::: {#master-address .section}
### Master address[\#](#master-address "Link to this heading"){.headerlink}

By default, [`localhost`{.docutils .literal .notranslate}]{.pre} is used for single-node configurations. Change [`localhost`{.docutils .literal .notranslate}]{.pre} to the master node's resolvable hostname or IP address:

:::: {.highlight-bash .notranslate}
::: highlight
    export MASTER_ADDR="${MASTER_ADDR:-localhost}"
:::
::::
:::::

::::: {#number-of-nodes .section}
### Number of nodes[\#](#number-of-nodes "Link to this heading"){.headerlink}

Set the number of nodes you want to train on (for example, [`2`{.docutils .literal .notranslate}]{.pre}, [`4`{.docutils .literal .notranslate}]{.pre}, or [`8`{.docutils .literal .notranslate}]{.pre}):

:::: {.highlight-bash .notranslate}
::: highlight
    export NNODES="${NNODES:-<num_nodes>}"
:::
::::
:::::

::::: {#node-ranks .section}
### Node ranks[\#](#node-ranks "Link to this heading"){.headerlink}

Set the rank of each node ([`0`{.docutils .literal .notranslate}]{.pre} for master, [`1`{.docutils .literal .notranslate}]{.pre} for the first worker node, and so on). Node ranks should be unique across all nodes in the cluster.

:::: {.highlight-bash .notranslate}
::: highlight
    export NODE_RANK="${NODE_RANK:-<node_rank>}"
:::
::::
:::::

:::::::::: {#network-interface .section}
### Network interface[\#](#network-interface "Link to this heading"){.headerlink}

Update the network interface in the script to match your system's network interface. To find your network interface, run the following (outside of any Docker container):

:::: {.highlight-bash .notranslate}
::: highlight
    ip a
:::
::::

Look for an active interface (status "UP") with an IP address in the same subnet as your other nodes. Then, update the following variable in the script, for example:

:::: {.highlight-bash .notranslate}
::: highlight
    export NCCL_SOCKET_IFNAME=ens50f0np0
:::
::::

This variable specifies which network interface to use for inter-node communication. Setting this variable to the incorrect interface can result in communication failures or significantly reduced performance.

::::: {.admonition .tip}
Tip

This command sets [`NCCL_SOCKET_IFNAME`{.docutils .literal .notranslate}]{.pre}'s value to the last RDMA interface.

:::: {.highlight-bash .notranslate}
::: highlight
    export NCCL_SOCKET_IFNAME=$(rdma link show | awk '{print $NF}' | sort | tail -n1)
:::
::::
:::::
::::::::::

:::::::::: {#rdma-ib-interface .section}
### RDMA/IB interface[\#](#rdma-ib-interface "Link to this heading"){.headerlink}

Set the RDMA interfaces to be used for communication. NICs can come from different vendors and the names of the RDMA interface can be different. To get the list of all the RDMA/IB devices, run:

:::: {.highlight-bash .notranslate}
::: highlight
    ibv_devices
:::
::::

The command below gets the list of all RDMA/IB devices and puts them in a comma-separated format. If ([`rdma0,rdma1,rdma2,rdma3,rdma4,rdma5,rdma6,rdma7`{.docutils .literal .notranslate}]{.pre}) are your RDMA interfaces, then set:

:::: {.highlight-bash .notranslate}
::: highlight
    # If using Broadcom NIC
    export NCCL_IB_HCA=rdma0,rdma1,rdma2,rdma3,rdma4,rdma5,rdma6,rdma7
    # If using Mellanox NIC
    # export NCCL_IB_HCA=mlx5_0,mlx5_1,mlx5_2,mlx5_3,mlx5_4,mlx5_5,mlx5_8,mlx5_9
:::
::::

::::: {.admonition .tip}
Tip

Alternatively, if you want to choose the RDMA interface automatically, you can use the following. This command will sort the RDMA interfaces and then select the first eight RDMA interfaces.

:::: {.highlight-bash .notranslate}
::: highlight
    export NCCL_IB_HCA=$(ibv_devices | awk 'NR>2 {print $1}' | sort | head -n 8 | paste -sd,)
:::
::::
:::::
::::::::::

::::: {#global-id-index .section}
### Global ID index[\#](#global-id-index "Link to this heading"){.headerlink}

Update the global ID index if you're using RoCE.

:::: {.highlight-bash .notranslate}
::: highlight
    export NCCL_IB_GID_INDEX=3
:::
::::
:::::
:::::::::::::::::::::::::::::::

::::::::: {#multi-node-training-examples .section}
[]{#multi-node-setup-training-examples}

## Multi-node training examples[\#](#multi-node-training-examples "Link to this heading"){.headerlink}

The following examples use the Slurm workload manager to launch jobs on multiple nodes. To run these scripts as-is, you must have a Slurm environment configured. The scripts are designed to work with both Broadcom Thor 2 and Mellanox NICs by automatically installing the required libraries and setting the necessary environment variables. For systems with Broadcom NICs, the scripts assume the host's RoCE library is located in the [`/opt`{.docutils .literal .notranslate}]{.pre} directory.

The following benchmarking examples demonstrate the training of a Llama 3 8B model across multiple 8-GPU nodes, using FSDP for intra-node parallelism and DP for inter-node parallelism.

::: {#jax-maxtext .section}
[]{#rocm-for-ai-multi-node-setup-jax-train-example}

### JAX MaxText[\#](#jax-maxtext "Link to this heading"){.headerlink}

1.  Download the desired multi-node benchmarking script from [ROCm/MAD](https://github.com/ROCm/MAD/tree/develop/scripts/jax-maxtext/gpu-rocm){.github .reference .external}.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        wget https://raw.githubusercontent.com/ROCm/MAD/refs/heads/develop/scripts/jax-maxtext/gpu-rocm/llama3_8b_multinode.sh
    :::
    ::::

    Or clone the [ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external} repository.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd scripts/jax-maxtext/gpu-rocm
    :::
    ::::

2.  Run the benchmark for multi-node training.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        sbatch -N <num_nodes> llama3_8b_multinode.sh
    :::
    ::::
:::

::::: {#pytorch-training .section}
[]{#rocm-for-ai-multi-node-setup-pyt-train-example}

### PyTorch training[\#](#pytorch-training "Link to this heading"){.headerlink}

::: {.admonition .note}
Note

The ROCm PyTorch Training Docker image now focuses on [[Training a model with Primus and PyTorch]{.doc}](../training/benchmark-docker/primus-pytorch.html){.reference .internal}. The following example refers to the legacy workflow [[Training a model with PyTorch]{.std .std-ref}](../training/benchmark-docker/previous-versions/pytorch-training-v25.9.html#amd-pytorch-training-multinode-examples-v259){.reference .internal}.
:::

1.  Download the [`run_multinode_train.sh`{.docutils .literal .notranslate}]{.pre} benchmarking script from [ROCm/MAD](https://github.com/ROCm/MAD/tree/develop/scripts/pytorch_train){.github .reference .external}.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        wget https://raw.githubusercontent.com/ROCm/MAD/refs/heads/develop/scripts/pytorch_train/run_multinode_train.sh
    :::
    ::::

    Or clone the [ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external} repository.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd scripts/pytorch_train
    :::
    ::::

2.  Run the benchmark for multi-node training.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        sbatch -N <num_nodes> run_multinode_train.sh
    :::
    ::::

::: {.admonition .seealso}
See also

See [[Training a model with PyTorch]{.std .std-ref}](../training/benchmark-docker/previous-versions/pytorch-training-v25.9.html#amd-pytorch-training-multinode-examples-v259){.reference .internal} for more examples and information.
:::
:::::

:::: {#megatron-lm .section}
### Megatron-LM[\#](#megatron-lm "Link to this heading"){.headerlink}

::: {.admonition .note}
Note

The Megatron-LM Docker image now focuses on [[Training a model with Primus and Megatron]{.std .std-ref}](../training/benchmark-docker/previous-versions/primus-megatron-v25.8.html#amd-primus-megatron-multi-node-examples){.reference .internal}. The following example refers to the legacy Megatron-LM [[Training a model with Megatron-LM]{.std .std-ref}](../training/benchmark-docker/previous-versions/megatron-lm-v25.9.html#amd-megatron-lm-multi-node-examples){.reference .internal} and might have limited support.
:::

1.  Download the [`train_llama_slurm.sh`{.docutils .literal .notranslate}]{.pre} benchmarking script from [ROCm/Megatron-LM](https://github.com/ROCm/Megatron-LM/blob/rocm_dev/examples/llama/train_llama_slurm.sh){.github .reference .external}.

2.  Set the network interface parameters as per the above guidelines and run the script.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        cd </path/to/your/Megatron-LM>
        export NETWORK_INTERFACE=$NCCL_SOCKET_IFNAME
        export NCCL_IB_HCA=$NCCL_IB_HCA
        export IMAGE=docker.io/rocm/megatron-lm:latest OR your preferred image
        export DATA_CACHE_PATH=/nfs/mounted/repo

        sbatch –N <num_nodes> examples/llama/train_llama_slurm.sh <MODEL_SIZE> <MBS> <GBS> <SEQ_LENGTH> <FSDP> <RECOMPUTE>
    :::
    ::::

<!-- -->

2.  For example, to run a Llama 3 8B workload in BF16 precision, use the following command.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        MODEL_NAME=llama3 sbatch –N 8 examples/llama/train_llama_slurm.sh 8 2 128 8192 0 0
        # Other parameters, such as TP, FP8 datatype, can be adjusted in the script.
    :::
    ::::
::::
:::::::::

::: {#further-reading .section}
## Further reading[\#](#further-reading "Link to this heading"){.headerlink}

- [Multi-node network configuration for AMD Instinct GPUs](https://instinct.docs.amd.com/projects/gpu-cluster-networking/en/latest/how-to/multi-node-config.html){.reference .external}

- [Ethernet networking guide for AMD Instinct MI300X GPU clusters: Compiling Broadcom NIC software from source](https://docs.broadcom.com/doc/957608-AN2XX#page=81){.reference .external}
:::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::: prev-next-area
[](prerequisite-system-validation.html "previous page"){.left-prev}

::: prev-next-info
previous

Prerequisite system validation before running AI workloads
:::

[](system-health-check.html "next page"){.right-next}

::: prev-next-info
next

System health benchmarks for AI workloads
:::
:::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::: {.bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {.page-toc .tocsection .onthispage}
Contents
:::

- [Prerequisites](#prerequisites){.reference .internal .nav-link}
- [Install required packages](#install-required-packages){.reference .internal .nav-link}
  - [Compile and install the RoCE library](#compile-and-install-the-roce-library){.reference .internal .nav-link}
- [Environment setup](#environment-setup){.reference .internal .nav-link}
  - [Master address](#master-address){.reference .internal .nav-link}
  - [Number of nodes](#number-of-nodes){.reference .internal .nav-link}
  - [Node ranks](#node-ranks){.reference .internal .nav-link}
  - [Network interface](#network-interface){.reference .internal .nav-link}
  - [RDMA/IB interface](#rdma-ib-interface){.reference .internal .nav-link}
  - [Global ID index](#global-id-index){.reference .internal .nav-link}
- [Multi-node training examples](#multi-node-training-examples){.reference .internal .nav-link}
  - [JAX MaxText](#jax-maxtext){.reference .internal .nav-link}
  - [PyTorch training](#pytorch-training){.reference .internal .nav-link}
  - [Megatron-LM](#megatron-lm){.reference .internal .nav-link}
- [Further reading](#further-reading){.reference .internal .nav-link}
::::
:::::
::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
