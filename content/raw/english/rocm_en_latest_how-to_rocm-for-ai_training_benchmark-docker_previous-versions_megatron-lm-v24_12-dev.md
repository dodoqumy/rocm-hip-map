---
title: "Training a model with ROCm Megatron-LM"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/training/benchmark-docker/previous-versions/megatron-lm-v24.12-dev.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-01
---

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-content
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-article-container
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
# Training a model with ROCm Megatron-LM

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [Supported features and models](#supported-features-and-models){.reference .internal .nav-link}
- [Prerequisite system validation steps](#prerequisite-system-validation-steps){.reference .internal .nav-link}
  - [Disable NUMA auto-balancing](#disable-numa-auto-balancing){.reference .internal .nav-link}
  - [Hardware verification with ROCm](#hardware-verification-with-rocm){.reference .internal .nav-link}
  - [RCCL Bandwidth Test](#rccl-bandwidth-test){.reference .internal .nav-link}
    - [Tuning and optimizing hyperparameters](#tuning-and-optimizing-hyperparameters){.reference .internal .nav-link}
    - [Running the RCCL Bandwidth Test](#running-the-rccl-bandwidth-test){.reference .internal .nav-link}
- [Start training on MI300X GPUs](#start-training-on-mi300x-gpus){.reference .internal .nav-link}
  - [Download the Docker image and required packages](#download-the-docker-image-and-required-packages){.reference .internal .nav-link}
  - [Prepare training datasets](#prepare-training-datasets){.reference .internal .nav-link}
  - [Environment setup](#environment-setup){.reference .internal .nav-link}
    - [Network interface](#network-interface){.reference .internal .nav-link}
    - [Dataset options](#dataset-options){.reference .internal .nav-link}
    - [Tokenizer](#tokenizer){.reference .internal .nav-link}
  - [Run benchmark tests](#run-benchmark-tests){.reference .internal .nav-link}
    - [Benchmarking examples](#benchmarking-examples){.reference .internal .nav-link}
- [Previous versions](#previous-versions){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#training-a-model-with-rocm-megatron-lm .section}
# Training a model with ROCm Megatron-LM[\#](#training-a-model-with-rocm-megatron-lm "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-04-21
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 13 min read time
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

The ROCm Megatron-LM framework is a specialized fork of the robust Megatron-LM, designed to enable efficient training of large-scale language models on AMD GPUs. By leveraging AMD Instinct™ MI300X GPUs, AMD Megatron-LM delivers enhanced scalability, performance, and resource utilization for AI workloads. It is purpose-built to [[support models]{.std .std-ref}](#amd-megatron-lm-model-support-24-12){.reference .internal} like Meta's Llama 2, Llama 3, and Llama 3.1, enabling developers to train next-generation AI models with greater efficiency. See the GitHub repository at [ROCm/Megatron-LM](https://github.com/ROCm/Megatron-LM){.github .reference .external}.

For ease of use, AMD provides a ready-to-use Docker image for MI300X GPUs containing essential components, including PyTorch, PyTorch Lightning, ROCm libraries, and Megatron-LM utilities. It contains the following software to accelerate training workloads:

::: pst-scrollable-table-container
  Software component   Version
  -------------------- ---------
  ROCm                 6.1
  PyTorch              2.4.0
  PyTorch Lightning    2.4.0
  Megatron Core        0.9.0
  Transformer Engine   1.5.0
  Flash Attention      v2.6
  Transformers         4.44.0
:::

::: {#supported-features-and-models .section}
## Supported features and models[\#](#supported-features-and-models "Link to this heading"){.headerlink}

Megatron-LM provides the following key features to train large language models efficiently:

- Transformer Engine (TE)

- APEX

- GEMM tuning

- Torch.compile

- 3D parallelism: TP + SP + CP

- Distributed optimizer

- Flash Attention (FA) 2

- Fused kernels

- Pre-training

The following models are pre-optimized for performance on the AMD Instinct MI300X GPU.

- Llama 2 7B

- Llama 2 70B

- Llama 3 8B

- Llama 3 70B

- Llama 3.1 8B

- Llama 3.1 70B
:::

:::::::::::::::::::: {#prerequisite-system-validation-steps .section}
## Prerequisite system validation steps[\#](#prerequisite-system-validation-steps "Link to this heading"){.headerlink}

Complete the following system validation and optimization steps to set up your system before starting training.

::::: {#disable-numa-auto-balancing .section}
### Disable NUMA auto-balancing[\#](#disable-numa-auto-balancing "Link to this heading"){.headerlink}

Generally, application performance can benefit from disabling NUMA auto-balancing. However, it might be detrimental to performance with certain types of workloads.

Run the command [`cat`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`/proc/sys/kernel/numa_balancing`{.docutils .literal .notranslate}]{.pre} to check your current NUMA (Non-Uniform Memory Access) settings. Output [`0`{.docutils .literal .notranslate}]{.pre} indicates this setting is disabled. If there is no output or the output is [`1`{.docutils .literal .notranslate}]{.pre}, run the following command to disable NUMA auto-balancing.

:::: {.highlight-shell .notranslate}
::: highlight
    sudo sh -c 'echo 0 > /proc/sys/kernel/numa_balancing'
:::
::::

See [[System validation and optimization]{.std .std-ref}](../../../system-setup/prerequisite-system-validation.html#rocm-for-ai-system-optimization){.reference .internal} for more information.
:::::

::::: {#hardware-verification-with-rocm .section}
### Hardware verification with ROCm[\#](#hardware-verification-with-rocm "Link to this heading"){.headerlink}

Use the command [`amd-smi`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`set`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--perf-determinism`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`1900`{.docutils .literal .notranslate}]{.pre} to set the max clock speed up to 1900 MHz instead of the default 2100 MHz. This can reduce the chance of a PCC event lowering the attainable GPU clocks. This setting will not be required for new IFWI releases with the production PRC feature. You can restore this setting to its default value with the [`amd-smi`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`reset`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--clocks`{.docutils .literal .notranslate}]{.pre} command.

Run the command:

:::: {.highlight-shell .notranslate}
::: highlight
    amd-smi set --perf-determinism 1900
:::
::::

See [Hardware verification with ROCm](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi300x.html#hardware-verification-with-rocm){.reference .external} for more information.
:::::

::::::::::::: {#rccl-bandwidth-test .section}
### RCCL Bandwidth Test[\#](#rccl-bandwidth-test "Link to this heading"){.headerlink}

ROCm Collective Communications Library (RCCL) is a standalone library of standard collective communication routines for GPUs. See the [[RCCL documentation]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rccl/en/latest/index.html "(in RCCL Documentation v2.27.7)"){.reference .external} for more information. Before starting pre-training, running a RCCL bandwidth test helps ensure that the multi-GPU or multi-node setup is optimized for efficient distributed training.

Running the RCCL bandwidth test helps verify that:

- The GPUs can communicate across nodes or within a single node.

- The interconnect (such as InfiniBand, Ethernet, or Infinite fabric) is functioning as expected and provides adequate bandwidth for communication.

- No hardware setup or cabling issues could affect the communication between GPUs

::::: {#tuning-and-optimizing-hyperparameters .section}
#### Tuning and optimizing hyperparameters[\#](#tuning-and-optimizing-hyperparameters "Link to this heading"){.headerlink}

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
#### Running the RCCL Bandwidth Test[\#](#running-the-rccl-bandwidth-test "Link to this heading"){.headerlink}

It's recommended you run the RCCL bandwidth test before launching training. It ensures system performance is sufficient to launch training. RCCL is not included in the AMD Megatron-LM Docker image; follow the instructions in [ROCm/rccl-tests](https://github.com/ROCm/rccl-tests){.github .reference .external} to get started. See [[RCCL]{.std .std-ref}](../../../inference-optimization/workload.html#mi300x-rccl){.reference .internal} for more information.

Run on 8 GPUs ([`-g`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`8`{.docutils .literal .notranslate}]{.pre}), scanning from 8 bytes to 10 GB:

:::: {.highlight-shell .notranslate}
::: highlight
    ./build/all_reduce_perf -b 8 -e 10G -f 2 -g 8
:::
::::

[![](../../../../../_images/rccl-tests-8-gpu.png){style="width: 800px;"}](../../../../../_images/rccl-tests-8-gpu.png){.reference .internal .image-reference}

Using one MPI process per GPU and [`-g`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`1`{.docutils .literal .notranslate}]{.pre} for performance-oriented runs on both single-node and multi-node is recommended. So, a run on 8 GPUs looks something like:

:::: {.highlight-shell .notranslate}
::: highlight
    mpirun -np 8 --bind-to numa ./build/all_reduce_perf -b 8 -e 10G -f 2 -g 1
:::
::::

[![](../../../../../_images/rccl-tests-1-mpi-process-per-gpu.png){style="width: 800px;"}](../../../../../_images/rccl-tests-1-mpi-process-per-gpu.png){.reference .internal .image-reference}

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

[![](../../../../../_images/rccl-tests-4-mi300x-gpu-nodes.png){style="width: 800px;"}](../../../../../_images/rccl-tests-4-mi300x-gpu-nodes.png){.reference .internal .image-reference}
:::::::::
:::::::::::::
::::::::::::::::::::

:::::::::::::::::::::::::: {#start-training-on-mi300x-gpus .section}
[]{#mi300x-amd-megatron-lm-training-v2412}

## Start training on MI300X GPUs[\#](#start-training-on-mi300x-gpus "Link to this heading"){.headerlink}

The pre-built ROCm Megatron-LM environment allows users to quickly validate system performance, conduct training benchmarks, and achieve superior performance for models like Llama 2 and Llama 3.1.

Use the following instructions to set up the environment, configure the script to train models, and reproduce the benchmark results on the MI300X GPUs with the AMD Megatron-LM Docker image.

::: {#download-the-docker-image-and-required-packages .section}
[]{#amd-megatron-lm-requirements-v2412}

### Download the Docker image and required packages[\#](#download-the-docker-image-and-required-packages "Link to this heading"){.headerlink}

1.  Use the following command to pull the Docker image from Docker Hub.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker pull rocm/megatron-lm:24.12-dev
    :::
    ::::

2.  Launch the Docker container.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker run -it --device /dev/dri --device /dev/kfd --network host --ipc host --group-add video --cap-add SYS_PTRACE --security-opt seccomp=unconfined --privileged -v $CACHE_DIR:/root/.cache --name megatron-dev-env rocm/megatron-lm:24.12-dev /bin/bash
    :::
    ::::

3.  Clone the ROCm Megatron-LM repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/Megatron-LM
        cd Megatron-LM
    :::
    ::::

    ::::: {.admonition .note}
    Note

    This release is validated with [`ROCm/Megatron-LM`{.docutils .literal .notranslate}]{.pre} commit [bb93ccb](https://github.com/ROCm/Megatron-LM/tree/bb93ccbfeae6363c67b361a97a27c74ab86e7e92){.reference .external}. Checking out this specific commit is recommended for a stable and reproducible environment.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git checkout bb93ccbfeae6363c67b361a97a27c74ab86e7e92
    :::
    ::::
    :::::
:::

::::: {#prepare-training-datasets .section}
### Prepare training datasets[\#](#prepare-training-datasets "Link to this heading"){.headerlink}

If you already have the preprocessed data, you can skip this section.

Use the following command to process datasets. We use GPT data as an example. You may change the merge table, use an end-of-document token, remove sentence splitting, and use the tokenizer type.

:::: {.highlight-shell .notranslate}
::: highlight
    python tools/preprocess_data.py \
        --input my-corpus.json \
        --output-prefix my-gpt2 \
        --vocab-file gpt2-vocab.json \
        --tokenizer-type GPT2BPETokenizer \
        --merge-file gpt2-merges.txt \
        --append-eod
:::
::::

In this case, the automatically generated output files are named [`my-gpt2_text_document.bin`{.docutils .literal .notranslate}]{.pre} and [`my-gpt2_text_document.idx`{.docutils .literal .notranslate}]{.pre}.

[![](../../../../../_images/prep-training-datasets-my-gpt2-text-document.png){style="width: 800px;"}](../../../../../_images/prep-training-datasets-my-gpt2-text-document.png){.reference .internal .image-reference}
:::::

:::::::: {#environment-setup .section}
[]{#amd-megatron-lm-environment-setup-v2412}

### Environment setup[\#](#environment-setup "Link to this heading"){.headerlink}

In the [`examples/llama`{.docutils .literal .notranslate}]{.pre} directory of Megatron-LM, if you're working with Llama 2 7B or Llama 2 70 B, use the [`train_llama2.sh`{.docutils .literal .notranslate}]{.pre} configuration script. Likewise, if you're working with Llama 3 or Llama 3.1, then use [`train_llama3.sh`{.docutils .literal .notranslate}]{.pre} and update the configuration script accordingly.

::: {#network-interface .section}
#### Network interface[\#](#network-interface "Link to this heading"){.headerlink}

To avoid connectivity issues, ensure the correct network interface is set in your training scripts.

1.  Run the following command to find the active network interface on your system.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        ip a
    :::
    ::::

2.  Update the [`NCCL_SOCKET_IFNAME`{.docutils .literal .notranslate}]{.pre} and [`GLOO_SOCKET_IFNAME`{.docutils .literal .notranslate}]{.pre} variables with your system's network interface. For example:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export NCCL_SOCKET_IFNAME=ens50f0np0

        export GLOO_SOCKET_IFNAME=ens50f0np0
    :::
    ::::
:::

::: {#dataset-options .section}
#### Dataset options[\#](#dataset-options "Link to this heading"){.headerlink}

You can use either mock data or real data for training.

- If you're using a real dataset, update the [`DATA_PATH`{.docutils .literal .notranslate}]{.pre} variable to point to the location of your dataset.

  :::: {.highlight-shell .notranslate}
  ::: highlight
      DATA_DIR="/root/.cache/data" # Change to where your dataset is stored

      DATA_PATH=${DATA_DIR}/bookcorpus_text_sentence
  :::
  ::::

  :::: {.highlight-shell .notranslate}
  ::: highlight
      --data-path $DATA_PATH
  :::
  ::::

  Ensure that the files are accessible inside the Docker container.

- Mock data can be useful for testing and validation. If you're using mock data, replace [`--data-path`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`$DATA_PATH`{.docutils .literal .notranslate}]{.pre} with the [`--mock-data`{.docutils .literal .notranslate}]{.pre} option.

  :::: {.highlight-shell .notranslate}
  ::: highlight
      --mock-data
  :::
  ::::
:::

::::: {#tokenizer .section}
#### Tokenizer[\#](#tokenizer "Link to this heading"){.headerlink}

Tokenization is the process of converting raw text into tokens that can be processed by the model. For Llama models, this typically involves sub-word tokenization, where words are broken down into smaller units based on a fixed vocabulary. The tokenizer is trained along with the model on a large corpus of text, and it learns a fixed vocabulary that can represent a wide range of text from different domains. This allows Llama models to handle a variety of input sequences, including unseen words or domain-specific terms.

To train any of the Llama 2 models that this Docker image supports, use the [`Llama2Tokenizer`{.docutils .literal .notranslate}]{.pre}.

To train any of Llama 3 and Llama 3.1 models that this Docker image supports, use the [`HuggingFaceTokenizer`{.docutils .literal .notranslate}]{.pre}. Set the Hugging Face model link in the [`TOKENIZER_MODEL`{.docutils .literal .notranslate}]{.pre} variable.

For example, if you're using the Llama 3.1 8B model:

:::: {.highlight-shell .notranslate}
::: highlight
    TOKENIZER_MODEL=meta-llama/Llama-3.1-8B
:::
::::
:::::
::::::::

::::::::::::::: {#run-benchmark-tests .section}
### Run benchmark tests[\#](#run-benchmark-tests "Link to this heading"){.headerlink}

::: {.admonition .note}
Note

If you're running **multi node training**, update the following environment variables. They can also be passed as command line arguments.

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
:::

- Use this command to run a performance benchmark test of any of the Llama 2 models that this Docker image supports (see [[variables]{.std .std-ref}](#amd-megatron-lm-benchmark-test-vars-v2412){.reference .internal}).

  :::: {.highlight-shell .notranslate}
  ::: highlight
      {variables} bash examples/llama/train_llama2.sh
  :::
  ::::

- Use this command to run a performance benchmark test of any of the Llama 3 and Llama 3.1 models that this Docker image supports (see [[variables]{.std .std-ref}](#amd-megatron-lm-benchmark-test-vars-v2412){.reference .internal}).

  :::: {.highlight-shell .notranslate}
  ::: highlight
      {variables} bash examples/llama/train_llama3.sh
  :::
  ::::

The benchmark tests support the same set of variables:

::: pst-scrollable-table-container
+-------------------------------------------------------------+-----------------------------+----------------------------------------------------+
| Name                                                        | Options                     | Description                                        |
+=============================================================+=============================+====================================================+
| [`TEE_OUTPUT`{.docutils .literal .notranslate}]{.pre}       | 0 or 1                      | 0: disable training log                            |
|                                                             |                             |                                                    |
|                                                             |                             | 1: enable training log                             |
+-------------------------------------------------------------+-----------------------------+----------------------------------------------------+
| [`MBS`{.docutils .literal .notranslate}]{.pre}              |                             | Micro batch size                                   |
+-------------------------------------------------------------+-----------------------------+----------------------------------------------------+
| [`BS`{.docutils .literal .notranslate}]{.pre}               |                             | Batch size                                         |
+-------------------------------------------------------------+-----------------------------+----------------------------------------------------+
| [`TP`{.docutils .literal .notranslate}]{.pre}               | 1, 2, 4, 8                  | Tensor parallel                                    |
+-------------------------------------------------------------+-----------------------------+----------------------------------------------------+
| [`TE_FP8`{.docutils .literal .notranslate}]{.pre}           | 0 or 1                      | Datatype. If it is set to 1, FP8.                  |
|                                                             |                             |                                                    |
|                                                             |                             | If it is set to 0. BP16                            |
+-------------------------------------------------------------+-----------------------------+----------------------------------------------------+
| [`NO_TORCH_COMPILE`{.docutils .literal .notranslate}]{.pre} | 0 or 1                      | If it is set to 1, enable torch.compile.           |
|                                                             |                             |                                                    |
|                                                             |                             | If it is set to 0. Disable torch.compile (default) |
+-------------------------------------------------------------+-----------------------------+----------------------------------------------------+
| [`SEQ_LENGTH`{.docutils .literal .notranslate}]{.pre}       |                             | Input sequence length                              |
+-------------------------------------------------------------+-----------------------------+----------------------------------------------------+
| [`GEMM_TUNING`{.docutils .literal .notranslate}]{.pre}      | 0 or 1                      | If it is set to 1, enable gemm tuning.             |
|                                                             |                             |                                                    |
|                                                             |                             | If it is set to 0, disable gemm tuning             |
+-------------------------------------------------------------+-----------------------------+----------------------------------------------------+
| [`USE_FLASH_ATTN`{.docutils .literal .notranslate}]{.pre}   | 0 or 1                      | 0: disable flash attention                         |
|                                                             |                             |                                                    |
|                                                             |                             | 1: enable flash attention                          |
+-------------------------------------------------------------+-----------------------------+----------------------------------------------------+
| [`ENABLE_PROFILING`{.docutils .literal .notranslate}]{.pre} | 0 or 1                      | 0: disable torch profiling                         |
|                                                             |                             |                                                    |
|                                                             |                             | 1: enable torch profiling                          |
+-------------------------------------------------------------+-----------------------------+----------------------------------------------------+
| [`MODEL_SIZE`{.docutils .literal .notranslate}]{.pre}       |                             | The size of the mode: 7B/70B, etc.                 |
+-------------------------------------------------------------+-----------------------------+----------------------------------------------------+
| [`TOTAL_ITERS`{.docutils .literal .notranslate}]{.pre}      |                             | Total number of iterations                         |
+-------------------------------------------------------------+-----------------------------+----------------------------------------------------+
| [`transformer-impl`{.docutils .literal .notranslate}]{.pre} | transformer_engine or local | Enable transformer engine by default               |
+-------------------------------------------------------------+-----------------------------+----------------------------------------------------+
:::

:::::::::::: {#benchmarking-examples .section}
#### Benchmarking examples[\#](#benchmarking-examples "Link to this heading"){.headerlink}

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

You can find the training logs at the location defined in [`$TRAIN_LOG`{.docutils .literal .notranslate}]{.pre} in the [[configuration script]{.std .std-ref}](#amd-megatron-lm-environment-setup-v2412){.reference .internal}.

See the sample output:

[![](../../../../../_images/llama2-7b-training-log-sample.png){style="width: 800px;"}](../../../../../_images/llama2-7b-training-log-sample.png){.reference .internal .image-reference}
:::::

Multi node training

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

You can find the training logs at the location defined in [`$TRAIN_LOG`{.docutils .literal .notranslate}]{.pre} in the [[configuration script]{.std .std-ref}](#amd-megatron-lm-environment-setup-v2412){.reference .internal}.

Sample output for 2-node training:

Master node:

[![](../../../../../_images/2-node-training-master.png){style="width: 800px;"}](../../../../../_images/2-node-training-master.png){.reference .internal .image-reference}

Worker node:

[![](../../../../../_images/2-node-training-worker.png){style="width: 800px;"}](../../../../../_images/2-node-training-worker.png){.reference .internal .image-reference}
:::::::
:::::::::::
::::::::::::
:::::::::::::::
::::::::::::::::::::::::::

::: {#previous-versions .section}
## Previous versions[\#](#previous-versions "Link to this heading"){.headerlink}

See [[Megatron-LM training performance testing version history]{.doc}](megatron-lm-history.html){.reference .internal} to find documentation for previous releases of the [`ROCm/megatron-lm`{.docutils .literal .notranslate}]{.pre} Docker image.
:::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: prev-next-area
:::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::: {.bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {.page-toc .tocsection .onthispage}
Contents
:::

- [Supported features and models](#supported-features-and-models){.reference .internal .nav-link}
- [Prerequisite system validation steps](#prerequisite-system-validation-steps){.reference .internal .nav-link}
  - [Disable NUMA auto-balancing](#disable-numa-auto-balancing){.reference .internal .nav-link}
  - [Hardware verification with ROCm](#hardware-verification-with-rocm){.reference .internal .nav-link}
  - [RCCL Bandwidth Test](#rccl-bandwidth-test){.reference .internal .nav-link}
    - [Tuning and optimizing hyperparameters](#tuning-and-optimizing-hyperparameters){.reference .internal .nav-link}
    - [Running the RCCL Bandwidth Test](#running-the-rccl-bandwidth-test){.reference .internal .nav-link}
- [Start training on MI300X GPUs](#start-training-on-mi300x-gpus){.reference .internal .nav-link}
  - [Download the Docker image and required packages](#download-the-docker-image-and-required-packages){.reference .internal .nav-link}
  - [Prepare training datasets](#prepare-training-datasets){.reference .internal .nav-link}
  - [Environment setup](#environment-setup){.reference .internal .nav-link}
    - [Network interface](#network-interface){.reference .internal .nav-link}
    - [Dataset options](#dataset-options){.reference .internal .nav-link}
    - [Tokenizer](#tokenizer){.reference .internal .nav-link}
  - [Run benchmark tests](#run-benchmark-tests){.reference .internal .nav-link}
    - [Benchmarking examples](#benchmarking-examples){.reference .internal .nav-link}
- [Previous versions](#previous-versions){.reference .internal .nav-link}
::::
:::::
::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
