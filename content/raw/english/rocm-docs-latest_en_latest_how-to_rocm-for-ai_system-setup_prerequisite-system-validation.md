---
title: "Prerequisite system validation before running AI workloads"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/system-setup/prerequisite-system-validation.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-01
---

::::::::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

::::::::::::::::::::::::::::::::::::::::::::::::::: bd-content
:::::::::::::::::::::::::::::::::::::::::::::: bd-article-container
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
- Prerequisite\...
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
# Prerequisite system validation before running AI workloads

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [Disable NUMA auto-balancing](#disable-numa-auto-balancing){.reference .internal .nav-link}
- [Hardware verification with ROCm](#hardware-verification-with-rocm){.reference .internal .nav-link}
- [RCCL Bandwidth Test for multi-node setups](#rccl-bandwidth-test-for-multi-node-setups){.reference .internal .nav-link}
  - [Tuning and optimizing hyperparameters](#tuning-and-optimizing-hyperparameters){.reference .internal .nav-link}
  - [Running the RCCL Bandwidth Test](#running-the-rccl-bandwidth-test){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

::::::::::::::::::::::::::::: {#prerequisite-system-validation-before-running-ai-workloads .section}
[]{#rocm-for-ai-system-optimization}[]{#train-a-model-system-validation}

# Prerequisite system validation before running AI workloads[\#](#prerequisite-system-validation-before-running-ai-workloads "Link to this heading"){.headerlink}

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

Complete the following system validation and optimization steps to set up your system before starting training and inference.

::::: {#disable-numa-auto-balancing .section}
## Disable NUMA auto-balancing[\#](#disable-numa-auto-balancing "Link to this heading"){.headerlink}

Generally, application performance can benefit from disabling NUMA auto-balancing. However, it might be detrimental to performance with certain types of workloads.

Run the command [`cat`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`/proc/sys/kernel/numa_balancing`{.docutils .literal .notranslate}]{.pre} to check your current NUMA (Non-Uniform Memory Access) settings. Output [`0`{.docutils .literal .notranslate}]{.pre} indicates this setting is disabled. If there is no output or the output is [`1`{.docutils .literal .notranslate}]{.pre}, run the following command to disable NUMA auto-balancing.

:::: {.highlight-shell .notranslate}
::: highlight
    sudo sh -c 'echo 0 > /proc/sys/kernel/numa_balancing'
:::
::::

See [Disable NUMA auto-balancing](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi300x.html#disable-numa-auto-balancing){.reference .external} in the Instinct documentation for more information.
:::::

::::: {#hardware-verification-with-rocm .section}
## Hardware verification with ROCm[\#](#hardware-verification-with-rocm "Link to this heading"){.headerlink}

Use the command [`amd-smi`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`set`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--perf-determinism`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`1900`{.docutils .literal .notranslate}]{.pre} to set the max clock speed up to 1900 MHz instead of the default 2100 MHz. This can reduce the chance of a PCC event lowering the attainable GPU clocks. This setting will not be required for new IFWI releases with the production PRC feature. You can restore this setting to its default value with the [`amd-smi`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`reset`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--clocks`{.docutils .literal .notranslate}]{.pre} command.

Run the command:

:::: {.highlight-shell .notranslate}
::: highlight
    amd-smi set --perf-determinism 1900
:::
::::

See [Hardware verfication for ROCm](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi300x.html#hardware-verification-with-rocm){.reference .external} in the Instinct documentation for more information.
:::::

::::::::::::: {#rccl-bandwidth-test-for-multi-node-setups .section}
## RCCL Bandwidth Test for multi-node setups[\#](#rccl-bandwidth-test-for-multi-node-setups "Link to this heading"){.headerlink}

ROCm Collective Communications Library (RCCL) is a standalone library of standard collective communication routines for GPUs. See the [[RCCL documentation]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rccl/en/latest/index.html "(in RCCL Documentation v2.27.7)"){.reference .external} for more information. Before starting pretraining, running a RCCL bandwidth test helps ensure that the multi-GPU or multi-node setup is optimized for efficient distributed training.

Running the RCCL bandwidth test helps verify that:

- The GPUs can communicate across nodes or within a single node.

- The interconnect (such as InfiniBand, Ethernet, or Infinite fabric) is functioning as expected and provides adequate bandwidth for communication.

- No hardware setup or cabling issues could affect the communication between GPUs

::::: {#tuning-and-optimizing-hyperparameters .section}
### Tuning and optimizing hyperparameters[\#](#tuning-and-optimizing-hyperparameters "Link to this heading"){.headerlink}

In distributed training, specific hyperparameters related to distributed communication can be tuned based on the results of the RCCL bandwidth test. These variables are already set in the Docker image:

:::: {.highlight-shell .notranslate}
::: highlight
    # force all RCCL streams to be high priority
    export TORCH_NCCL_HIGH_PRIORITY=1

    # specify which RDMA interfaces to use for communication
    export NCCL_IB_HCA=rdma0,rdma1,rdma2,rdma3,rdma4,rdma5,rdma6,rdma7

    # define the Global ID index used in RoCE mode
    export NCCL_IB_GID_INDEX=3

    # avoid data corruption/mismatch issue that existed in past releases
    export RCCL_MSCCL_ENABLE=0
:::
::::
:::::

::::::::: {#running-the-rccl-bandwidth-test .section}
### Running the RCCL Bandwidth Test[\#](#running-the-rccl-bandwidth-test "Link to this heading"){.headerlink}

It's recommended you run the RCCL bandwidth test before launching training. It ensures system performance is sufficient to launch training. RCCL is not included in the AMD Megatron-LM Docker image; follow the instructions in [ROCm/rccl-tests](https://github.com/ROCm/rccl-tests){.github .reference .external} to get started. See [[RCCL]{.std .std-ref}](../inference-optimization/workload.html#mi300x-rccl){.reference .internal} for more information.

Run on 8 GPUs ([`-g`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`8`{.docutils .literal .notranslate}]{.pre}), scanning from 8 bytes to 10 GB:

:::: {.highlight-shell .notranslate}
::: highlight
    ./build/all_reduce_perf -b 8 -e 10G -f 2 -g 8
:::
::::

[![](../../../_images/rccl-tests-8-gpu.png){style="width: 800px;"}](../../../_images/rccl-tests-8-gpu.png){.reference .internal .image-reference}

Using one MPI process per GPU and [`-g`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`1`{.docutils .literal .notranslate}]{.pre} for performance-oriented runs on both single-node and multi-node is recommended. So, a run on 8 GPUs looks something like:

:::: {.highlight-shell .notranslate}
::: highlight
    mpirun -np 8 --bind-to numa ./build/all_reduce_perf -b 8 -e 10G -f 2 -g 1
:::
::::

[![](../../../_images/rccl-tests-1-mpi-process-per-gpu.png){style="width: 800px;"}](../../../_images/rccl-tests-1-mpi-process-per-gpu.png){.reference .internal .image-reference}

Running with one MPI process per GPU ensures a one-to-one mapping for CPUs and GPUs, which can be beneficial for smaller message sizes. This better represents the real-world use of RCCL in deep learning frameworks like PyTorch and TensorFlow.

Use the following script to run the RCCL test for four MI300X GPU nodes. Modify paths and node addresses as needed.

:::: {.highlight-default .notranslate}
::: highlight
    /home/$USER/ompi_for_gpu/ompi/bin/mpirun -np 32 -H tw022:8,tw024:8,tw010:8, tw015:8 \
    --mca pml ucx \
    --mca btl ^openib \
    -x NCCL_SOCKET_IFNAME=ens50f0np0 \
    -x NCCL_IB_HCA=rdma0:1,rdma1:1,rdma2:1,rdma3:1,rdma4:1,rdma5:1,rdma6:1,rdma7:1 \
    -x NCCL_IB_GID_INDEX=3 \
    -x NCCL_MIN_NCHANNELS=40 \
    -x NCCL_DEBUG=version \
    $HOME/rccl-tests/build/all_reduce_perf -b 8 -e 8g -f 2 -g 1
:::
::::

[![](../../../_images/rccl-tests-4-mi300x-gpu-nodes.png){style="width: 800px;"}](../../../_images/rccl-tests-4-mi300x-gpu-nodes.png){.reference .internal .image-reference}
:::::::::
:::::::::::::
:::::::::::::::::::::::::::::

::::: prev-next-area
[](index.html "previous page"){.left-prev}

::: prev-next-info
previous

System setup for AI workloads on ROCm
:::

[](multi-node-setup.html "next page"){.right-next}

::: prev-next-info
next

Multi-node setup for AI workloads
:::
:::::
::::::::::::::::::::::::::::::::::::::::::::::

:::::: {.bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {.page-toc .tocsection .onthispage}
Contents
:::

- [Disable NUMA auto-balancing](#disable-numa-auto-balancing){.reference .internal .nav-link}
- [Hardware verification with ROCm](#hardware-verification-with-rocm){.reference .internal .nav-link}
- [RCCL Bandwidth Test for multi-node setups](#rccl-bandwidth-test-for-multi-node-setups){.reference .internal .nav-link}
  - [Tuning and optimizing hyperparameters](#tuning-and-optimizing-hyperparameters){.reference .internal .nav-link}
  - [Running the RCCL Bandwidth Test](#running-the-rccl-bandwidth-test){.reference .internal .nav-link}
::::
:::::
::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::
