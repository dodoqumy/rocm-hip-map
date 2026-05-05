---
title: "Training a model with Megatron-LM for ROCm"
source_url: "https://rocm.docs.amd.com/en/docs-6.4.0/how-to/rocm-for-ai/training/benchmark-docker/megatron-lm.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T21:18:36.035412+00:00
content_hash: "fd7ef75125f66236"
---

# Training a model with Megatron-LM for ROCm[#](#training-a-model-with-megatron-lm-for-rocm)

2025-05-13

14 min read time

The Megatron-LM framework for ROCm is a specialized fork of the robust Megatron-LM,
designed to enable efficient training of large-scale language models on AMD
GPUs. By leveraging AMD Instinct™ MI300X series accelerators, Megatron-LM delivers
enhanced scalability, performance, and resource utilization for AI workloads.
It is purpose-built to support models like Llama 2, Llama 3, Llama 3.1, and
DeepSeek, enabling developers to train next-generation AI models more
efficiently. See the GitHub repository at [ROCm/Megatron-LM](https://github.com/ROCm/Megatron-LM).

AMD provides a ready-to-use Docker image for MI300X series accelerators containing essential components, including PyTorch, ROCm libraries, and Megatron-LM utilities. It contains the following software components to accelerate training workloads:

Software component |
Version |
|---|---|
ROCm |
6.3.0 |
PyTorch |
2.7.0a0+git637433 |
Python |
3.10 |
Transformer Engine |
1.11 |
Flash Attention |
3.0.0 |
hipBLASLt |
git258a2162 |
Triton |
3.1 |

## Supported features and models[#](#supported-features-and-models)

Megatron-LM provides the following key features to train large language models efficiently:

Transformer Engine (TE)

APEX

GEMM tuning

Torch.compile

3D parallelism: TP + SP + CP

Distributed optimizer

Flash Attention (FA) 3

Fused kernels

Pre-training


The following models are pre-optimized for performance on AMD Instinct MI300X series accelerators.

Llama 3.1 8B

Llama 3.1 70B

Llama 3 8B

Llama 3 70B

Llama 2 7B

Llama 2 70B

DeepSeek-V2-Lite


Note

Some models, such as Llama, require an external license agreement through a third party (for example, Meta).

## Performance measurements[#](#performance-measurements)

To evaluate performance, the
[Performance results with AMD ROCm software](https://www.amd.com/en/developer/resources/rocm-hub/dev-ai/performance-results.html#tabs-a8deaeb413-item-21cea50186-tab)
page provides reference throughput and latency measurements for training
popular AI models.

Note

The performance data presented in
[Performance results with AMD ROCm software](https://www.amd.com/en/developer/resources/rocm-hub/dev-ai/performance-results.html#tabs-a8deaeb413-item-21cea50186-tab)
should not be interpreted as the peak performance achievable by AMD
Instinct MI325X and MI300X accelerators or ROCm software.

## System validation[#](#system-validation)

Before running AI workloads, it’s important to validate that your AMD hardware is configured correctly and performing optimally.

If you have already validated your system settings, including aspects like NUMA auto-balancing, you
can skip this step. Otherwise, complete the procedures in the [System validation and
optimization](../prerequisite-system-validation.html#rocm-for-ai-system-optimization) guide to properly configure your system settings
before starting training.

To test for optimal performance, consult the recommended [System health benchmarks](../../system-health-check.html#rocm-for-ai-system-health-bench). This suite of tests will help you verify and fine-tune your
system’s configuration.

## Environment setup[#](#environment-setup)

The prebuilt ROCm Megatron-LM environment allows users to quickly validate system performance, conduct training benchmarks, and achieve superior performance for models like Llama 3.1, Llama 2, and DeepSeek V2.

Use the following instructions to set up the environment, configure the script to train models, and reproduce the benchmark results on MI300X series accelerators with the AMD Megatron-LM Docker image.

### Download the Docker image[#](#download-the-docker-image)

Use the following command to pull the Docker image from Docker Hub.

pull rocm/megatron-lm:v25.4

Launch the Docker container.

run -it --device /dev/dri --device /dev/kfd --device /dev/infiniband --network host --ipc host --group-add video --cap-add SYS_PTRACE --security-opt seccomp=unconfined --privileged -v $HOME:$HOME -v $HOME/.ssh:/root/.ssh --shm-size 64G --name megatron_training_env rocm/megatron-lm:v25.4

Use these commands if you exit the

`megatron_training_env`

container and need to return to it.start megatron_training_env docker exec -it megatron_training_env bash


The Docker container includes a pre-installed, verified version of the ROCm Megatron-LM development branch [ROCm/Megatron-LM](https://github.com/ROCm/Megatron-LM/tree/rocm_dev)
(commit [fd6f01](https://github.com/ROCm/Megatron-LM/tree/fd6f0d11d7f9480ace32f22eb7e4dab5314fa350)).

### Configuration scripts[#](#configuration-scripts)

If you’re working with Llama 2 7B or Llama 2 70 B, use the `train_llama2.sh`

configuration
script in the `examples/llama`

directory of
[ROCm/Megatron-LM](https://github.com/ROCm/Megatron-LM/tree/rocm_dev/examples/llama).
Likewise, if you’re working with Llama 3 or Llama 3.1, use `train_llama3.sh`

and update
the configuration script accordingly.

#### Network interface[#](#network-interface)

Update the network interface in the script to match your system’s network interface. To find your network interface, run the following (outside of any Docker container):

```
a
```

Look for an active interface that has an IP address in the same subnet as your other nodes. Then, update the following variables in the script, for example:

```
export NCCL_SOCKET_IFNAME=ens50f0np0
export GLOO_SOCKET_IFNAME=ens50f0np0
```

#### Dataset options[#](#dataset-options)

You can use either mock data or real data for training.

Mock data can be useful for testing and validation. Use the

`MOCK_DATA`

variable to toggle between mock and real data. The default value is`1`

for enabled.MOCK_DATA=1

If you’re using a real dataset, update the

`DATA_PATH`

variable to point to the location of your dataset.MOCK_DATA=0 DATA_PATH="/data/bookcorpus_text_sentence" # Change to where your dataset is stored

Ensure that the files are accessible inside the Docker container.

To download the dataset, set the

`DATASET`

variable to the dataset you’d like to use. Two datasets are supported:`DATASET=wiki`

and`DATASET=bookcorpus`

. Use the following command to download the dataset.DATASET=wiki bash examples/llama/prepare_dataset.sh # For wiki-en dataset DATASET=bookcorpus bash examples/llama/prepare_dataset.sh # For bookcorpus dataset


If you don’t already have the dataset, download the DeepSeek dataset using the following commands:

```
deepseek-datasets
cd deepseek-datasets
wget https://atp-modelzoo-wlcb-pai.oss-cn-wulanchabu.aliyuncs.com/release/models/pai-megatron-patch/deepseek-datasets/SlimPajama.json
wget https://atp-modelzoo-wlcb-pai.oss-cn-wulanchabu.aliyuncs.com/release/models/pai-megatron-patch/deepseek-datasets/alpaca_zh-train.json
wget https://atp-modelzoo-wlcb-pai.oss-cn-wulanchabu.aliyuncs.com/release/models/pai-megatron-patch/deepseek-datasets/alpaca_zh-valid.json
wget https://atp-modelzoo-wlcb-pai.oss-cn-wulanchabu.aliyuncs.com/release/models/pai-megatron-patch/deepseek-datasets/mmap_deepseekv2_datasets_text_document.bin
wget https://atp-modelzoo-wlcb-pai.oss-cn-wulanchabu.aliyuncs.com/release/models/pai-megatron-patch/deepseek-datasets/mmap_deepseekv2_datasets_text_document.idx
```

You can use either mock data or real data for training.

Mock data can be useful for testing and validation. Use the

`MOCK_DATA`

variable to toggle between mock and real data. The default value is`1`

for enabled.MOCK_DATA=1

If you’re using a real dataset, update the

`DATA_DIR`

variable to point to the location of your dataset.MOCK_DATA=0 DATA_DIR="/root/data/deepseek-datasets" # Change to where your dataset is stored

Ensure that the files are accessible inside the Docker container.


#### Tokenizer[#](#tokenizer)

Tokenization is the process of converting raw text into tokens that can be processed by the model. For Llama models, this typically involves sub-word tokenization, where words are broken down into smaller units based on a fixed vocabulary. The tokenizer is trained along with the model on a large corpus of text, and it learns a fixed vocabulary that can represent a wide range of text from different domains. This allows Llama models to handle a variety of input sequences, including unseen words or domain-specific terms.

You can assign the path of an existing tokenizer to the `TOKENIZER_MODEL`

as shown in the following examples.
If the tokenizer is not found, it’ll be downloaded to the default tokenizer model path: `${DATA_DIR}/tokenizer_llama3`

or `${DATA_DIR}/tokenizer_llama2`

.

To train any of the Llama 2 models that [this Docker image supports](#amd-megatron-lm-model-support), use the `Llama2Tokenizer`

or the default `HuggingFaceTokenizer`

.

To train any of Llama 3 and Llama 3.1 models that this Docker image supports, use the `HuggingFaceTokenizer`

.
Set the Hugging Face model path in the `TOKENIZER_MODEL`

variable.

For example, if you’re using the Llama 3.1 8B model:

```
TOKENIZER_MODEL=meta-llama/Llama-3.1-8B
```

Note

If you don’t already have the Llama 3.1 tokenizer locally, set your
personal Hugging Face access token `HF_TOKEN`

to download the
tokenizer. If you encounter the following error, set `HF_TOKEN`

to
your access-authorized Hugging Face token.

```
You are trying to access a gated repo.
# pass your HF_TOKEN
export HF_TOKEN=$your_personal_hf_token
```

#### Multi-node training[#](#multi-node-training)

If you’re running multi-node training, update the following environment variables. They can also be passed as command line arguments.

Change

`localhost`

to the master node’s hostname:MASTER_ADDR="${MASTER_ADDR:-localhost}"

Set the number of nodes you want to train on (for instance,

`2`

,`4`

,`8`

):NNODES="${NNODES:-1}"

Set the rank of each node (0 for master, 1 for the first worker node, and so on):

NODE_RANK="${NODE_RANK:-0}"

Set

`DATA_CACHE_PATH`

to a common directory accessible by all the nodes (for example, an NFS directory) for multi-node runs:DATA_CACHE_PATH=/root/cache # Set to a common directory for multi-node runs

For multi-node runs, make sure the correct network drivers are installed on the nodes. If inside a Docker container, either install the drivers inside the Docker container or pass the network drivers from the host while creating the Docker container.

# Specify which RDMA interfaces to use for communication export NCCL_IB_HCA=rdma0,rdma1,rdma2,rdma3,rdma4,rdma5,rdma6,rdma7


## Start training on AMD Instinct accelerators[#](#start-training-on-amd-instinct-accelerators)

The prebuilt Megatron-LM with ROCm training environment allows users to quickly validate system performance, conduct training benchmarks, and achieve superior performance for models like Llama 3.1 and Llama 2. This container should not be expected to provide generalized performance across all training workloads. You can expect the container to perform in the model configurations described in the following section, but other configurations are not validated by AMD.

Use the following instructions to set up the environment, configure the script to train models, and reproduce the benchmark results on MI300X series accelerators with the AMD Megatron-LM Docker image.

To run training on a single node, navigate to the Megatron-LM folder and use one of the following commands.

For Llama 3.1 8B FP8:

TEE_OUTPUT=1 MBS=2 BS=128 TP=1 TE_FP8=1 SEQ_LENGTH=8192 MODEL_SIZE=8 TOTAL_ITERS=50 bash examples/llama/train_llama3.sh

For Llama 3.1 8B BF16:

TEE_OUTPUT=1 MBS=2 BS=128 TP=1 TE_FP8=0 SEQ_LENGTH=8192 MODEL_SIZE=8 TOTAL_ITERS=50 bash examples/llama/train_llama3.sh

For Llama 2 7B FP8:

TEE_OUTPUT=1 MBS=4 BS=256 TP=1 TE_FP8=1 SEQ_LENGTH=4096 MODEL_SIZE=7 TOTAL_ITERS=50 bash examples/llama/train_llama2.sh

For Llama 2 7B BF16:

TEE_OUTPUT=1 MBS=4 BS=256 TP=1 TE_FP8=0 SEQ_LENGTH=4096 MODEL_SIZE=7 TOTAL_ITERS=50 bash examples/llama/train_llama2.sh


To run training with FSDP2 enabled, add the `FSDP=1`

argument. For example:

For Llama 3 70B BF16:

TEE_OUTPUT=1 MBS=3 BS=24 TP=1 TE_FP8=0 FSDP=1 RECOMPUTE=1 SEQ_LENGTH=8192 MODEL_SIZE=70 TOTAL_ITERS=50 bash examples/llama/train_llama3.sh

For Llama 2 70B BF16:

TEE_OUTPUT=1 MBS=3 BS=56 TP=1 TE_FP8=0 FSDP=1 RECOMPUTE=1 SEQ_LENGTH=4096 MODEL_SIZE=70 TOTAL_ITERS=50 bash examples/llama/train_llama2.sh


Note

It’s suggested to use `TP=1`

when FSDP is enabled for higher throughput. FSDP2 is not supported with pipeline parallelism,
expert parallelism, MCore’s distributed optimizer, gradient accumulation fusion, and `FP16`

precision.

To run training on multiple nodes, launch the Docker container on each node. For example, for a two node setup (`NODE0`

as the master node), use these commands.

On the master node

`NODE0`

:TEE_OUTPUT=1 MBS=2 BS=256 TP=1 TE_FP8=1 SEQ_LENGTH=8192 MODEL_SIZE=8 MASTER_ADDR=IP_NODE0 NNODES=2 NODE_RANK=0 bash examples/llama/train_llama3.sh

On the worker node

`NODE1`

:TEE_OUTPUT=1 MBS=2 BS=256 TP=1 TE_FP8=1 SEQ_LENGTH=8192 MODEL_SIZE=8 MASTER_ADDR=IP_NODE0 NNODES=2 NODE_RANK=1 bash examples/llama/train_llama3.sh


To run the training on a single node, go to `/Megatron-LM`

folder and use the following command:

```
cd /workspace/Megatron-LM
GEMM_TUNING=1 PR=bf16 MBS=4 AC=none SEQ_LEN=4096 PAD_LEN=4096 TRAIN_ITERS=50 bash examples/deepseek_v2/train_deepseekv2.sh
```

### Key options[#](#key-options)

The benchmark tests support the following sets of variables:

`TEE_OUTPUT`

`1`

to enable training logs or`0`

to disable.`TE_FP8`

`0`

for B16 or`1`

for FP8 –`0`

by default.`GEMM_TUNING`

`1`

to enable GEMM tuning, which boosts performance by using the best GEMM kernels.`USE_FLASH_ATTN`

`1`

to enable Flash Attention.`FSDP`

`1`

to enable PyTorch FSDP2. If FSDP is enabled,`--use-distributed-optimizer`

,`--overlap-param-gather`

, and`--sequence-parallel`

are automaticallyu disabled.`ENABLE_PROFILING`

`1`

to enable PyTorch profiling for performance analysis.`transformer-impl`

`transformer_engine`

to use the Transformer Engine (TE) or`local`

to disable TE.`MODEL_SIZE`

`8B`

or`70B`

for Llama 3 and 3.1.`7B`

or`70B`

for Llama 2.`TOTAL_ITERS`

The total number of iterations –

`10`

by default.`MOCK_DATA`

`1`

to use mock data or`0`

to use real data you provide.`MBS`

Micro batch size.

`BS`

Global batch size.

`TP`

Tensor parallel (

`1`

,`2`

,`4`

,`8`

).`TP`

is disabled when`FSDP`

is turned on.`SEQ_LENGTH`

Input sequence length.


`PR`

Precision for training.

`bf16`

for BF16 (default) or`fp8`

for FP8 GEMMs.`GEMM_TUNING`

`1`

to enable GEMM tuning, which boosts performance by using the best GEMM kernels.`TRAIN_ITERS`

The total number of iterations.

`MOCK_DATA`

`1`

to use mock data or`0`

to use real data you provide.`MBS`

Micro batch size.

`GBS`

Global batch size.

`SEQ_LEN`

Input sequence length.

`AC`

Activation checkpointing (

`none`

,`sel`

, or`full`

) –`sel`

by default.

### Benchmarking examples[#](#benchmarking-examples)

Use this command to run training with Llama 2 7B model on a single node. You can specify MBS, BS, FP, datatype, and so on.

```
TEE_OUTPUT=1 MBS=5 BS=120 TP=8 TE_FP8=0 NO_TORCH_COMPILE=1
SEQ_LENGTH=4096 bash examples/llama/train_llama2.sh
```

You can find the training logs at the location defined in `$TRAIN_LOG`

in the [configuration script](#amd-megatron-lm-environment-setup).

See the sample output:


Launch the Docker container on each node.

In this example, run training with Llama 2 7B model on 2 nodes with specific MBS, BS, FP, datatype, and so on.

On the master node:

```
TEE_OUTPUT=1 MBS=4 BS=64 TP=8 TE_FP8=0 NO_TORCH_COMPILE=1
SEQ_LENGTH=4096 bash examples/llama/train_llama2.sh
```

On the worker node:

```
TEE_OUTPUT=1 MBS=4 BS=64 TP=8 TE_FP8=0 NO_TORCH_COMPILE=1
SEQ_LENGTH=4096 bash examples/llama/train_llama2.sh
```

You can find the training logs at the location defined in `$TRAIN_LOG`

in the [configuration script](#amd-megatron-lm-environment-setup).

Sample output for 2-node training:

Master node:


Worker node:


## Previous versions[#](#previous-versions)

This table lists previous versions of the ROCm Megatron-LM Docker image for training performance testing. For detailed information about available models for benchmarking, see the version-specific documentation.
