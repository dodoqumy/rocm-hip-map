---
title: "Training a model with MaxText for ROCm"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/training/benchmark-docker/previous-versions/jax-maxtext-v25.4.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:02:16.762498+00:00
content_hash: "91db17d3238ef764"
---

# Training a model with MaxText for ROCm[#](#training-a-model-with-maxtext-for-rocm)

2026-04-21

9 min read time

Caution

This documentation does not reflect the latest version of ROCm JAX MaxText
training performance documentation. See [Training a model with Primus and JAX MaxText](../jax-maxtext.html) for the latest version.

MaxText is a high-performance, open-source framework built on the Google JAX
machine learning library to train LLMs at scale. The MaxText framework for
ROCm is an optimized fork of the upstream
[AI-Hypercomputer/maxtext](https://github.com/AI-Hypercomputer/maxtext) enabling efficient AI workloads
on AMD MI300X Series GPUs.

The MaxText for ROCm training Docker (`rocm/jax-training:maxtext-v25.4`

) image
provides a prebuilt environment for training on AMD Instinct MI300X and MI325X GPUs,
including essential components like JAX, XLA, ROCm libraries, and MaxText utilities.
It includes the following software components:

Software component |
Version |
|---|---|
ROCm |
6.3.0 |
JAX |
0.4.31 |
Python |
3.10 |
Transformer Engine |
1.12.0.dev0+f81a3eb |
hipBLASLt |
git78ec8622 |

## Supported features and models[#](#supported-features-and-models)

MaxText provides the following key features to train large language models efficiently:

Transformer Engine (TE)

Flash Attention (FA) 3

GEMM tuning

Multi-node support


The following models are pre-optimized for performance on AMD Instinct MI300X Series GPUs.

Llama 3.1 8B

Llama 3.1 70B

Llama 3 8B

Llama 3 70B

Llama 2 7B

Llama 2 70B

DeepSeek-V2-Lite


Note

Some models, such as Llama 3, require an external license agreement through a third party (for example, Meta).

### Unsupported features[#](#unsupported-features)

Currently, MaxText’s default packed input format is not supported. Using this format with the current Docker image results in incorrect attention calculations across different input sequences. Support for packed input format is planned for a future release.

## System validation[#](#system-validation)

If you have already validated your system settings, including NUMA
auto-balancing, skip this step. Otherwise, complete the [system validation
and optimization steps](../../../system-setup/prerequisite-system-validation.html#train-a-model-system-validation) to set up your system
before starting training.

## Environment setup[#](#environment-setup)

This Docker image is optimized for specific model configurations outlined as follows. Performance can vary for other training workloads, as AMD doesn’t validate configurations and run conditions outside those described.

### Multi-node setup[#](#multi-node-setup)

For multi-node environments, ensure you have all the necessary packages for
your network device, such as, RDMA. If you’re not using a multi-node setup
with RDMA, skip ahead to [Download the Docker image](#amd-maxtext-download-docker-v254).

Install the following packages to build and install the RDMA driver.

apt install iproute2 -y sudo apt install -y linux-headers-"$(uname-r)" libelf-dev sudo apt install -y gcc make libtool autoconf librdmacm-dev rdmacm-utils infiniband-diags ibverbs-utils perftest ethtool libibverbs-dev rdma-core strace libibmad5 libibnetdisc5 ibverbs-providers libibumad-dev libibumad3 libibverbs1 libnl-3-dev libnl-route-3-dev

Refer to your NIC manufacturer’s documentation for further steps on compiling and installing the RoCE driver. For example, for Broadcom, see

[Compiling Broadcom NIC software from source](https://docs.broadcom.com/doc/957608-AN2XX#G3.484341)in[Ethernet networking guide for AMD Instinct MI300X GPU clusters](https://docs.broadcom.com/doc/957608-AN2XX).Set the following environment variables.

Master address

Change localhost to the master node’s resolvable hostname or IP address:

export MASTER_ADDR="${MASTER_ADDR:-localhost}"

Number of nodes

Set the number of nodes you want to train on (for example,

`2`

,`4`

, or`8`

):export NNODES="${NNODES:-1}"

Node ranks

Set the rank of each node (

`0`

for master,`1`

for the first worker node, and so on) Node ranks should be unique across all nodes in the cluster.export NODE_RANK="${NODE_RANK:-0}"

Network interface

Update the network interface in the script to match your system’s network interface. To find your network interface, run the following (outside of any Docker container):

`a`

Look for an active interface with an IP address in the same subnet as your other nodes. Then, update the following variable in the script, for example:

export NCCL_SOCKET_IFNAME=ens50f0np0

This variable specifies which network interface to use for inter-node communication. Setting this variable to the incorrect interface can result in communication failures or significantly reduced performance.

RDMA interface

Ensure the

[required packages](#amd-maxtext-multi-node-setup-v254)are installed on all nodes. Then, set the RDMA interfaces to use for communication.# If using Broadcom NIC export NCCL_IB_HCA=rdma0,rdma1,rdma2,rdma3,rdma4,rdma5,rdma6,rdma7 # If using Mellanox NIC export NCCL_IB_HCA=mlx5_0,mlx5_1,mlx5_2,mlx5_3,mlx5_4,mlx5_5,mlx5_8,mlx5_9



### Download the Docker image[#](#download-the-docker-image)

Use the following command to pull the Docker image from Docker Hub.

pull rocm/jax-training:maxtext-v25.4

Run the Docker container.

run -it --device /dev/dri --device /dev/kfd --network host --ipc host --group-add video --cap-add SYS_PTRACE --security-opt seccomp=unconfined --privileged -v $HOME/.ssh:/root/.ssh --shm-size 128G --name maxtext_training rocm/jax-training:maxtext-v25.4


## Getting started[#](#getting-started)

The following examples demonstrate how to get started with single node
and multi-node training using the benchmarking scripts provided at
[ROCm/maxtext](https://github.com/ROCm/maxtext/).

Important

The provided scripts launch a Docker container and execute a benchmark. Ensure you run these commands outside of any existing Docker container.

Before running any benchmarks, ensure the `$HF_HOME`

environment variable is
set correctly and points to your Hugging Face cache directory.

### Single node training benchmarking examples[#](#single-node-training-benchmarking-examples)

Example 1: Single node training with Llama 2 7B

Download the benchmarking script:

`https://raw.githubusercontent.com/ROCm/maxtext/refs/heads/main/benchmarks/gpu-rocm/llama2_7b.sh`

Run the single node training benchmark:

IMAGE=”rocm/jax-training:maxtext-v25.4” bash ./llama2_7b.sh

Example 2: Single node training with Llama 2 70B

Download the benchmarking script:

`https://raw.githubusercontent.com/ROCm/maxtext/refs/heads/main/benchmarks/gpu-rocm/llama2_70b.sh`

Run the single node training benchmark:

IMAGE="rocm/jax-training:maxtext-v25.4" bash ./llama2_70b.sh

Example 3: Single node training with Llama 3 8B

Download the benchmarking script:

`https://raw.githubusercontent.com/ROCm/maxtext/refs/heads/main/benchmarks/gpu-rocm/llama3_8b.sh`

Run the single node training benchmark:

IMAGE="rocm/jax-training:maxtext-v25.4" bash ./llama3_8b.sh

Example 4: Single node training with Llama 3 70B

Download the benchmarking script:

`https://raw.githubusercontent.com/ROCm/maxtext/refs/heads/main/benchmarks/gpu-rocm/llama3_70b.sh`

Run the single node training benchmark:

IMAGE="rocm/jax-training:maxtext-v25.4" bash ./llama3_70b.sh

Example 5: Single node training with DeepSeek V2 16B

Download the benchmarking script:

`https://raw.githubusercontent.com/ROCm/maxtext/refs/heads/main/benchmarks/gpu-rocm/deepseek_v2_16b.sh`

Run the single node training benchmark:

IMAGE="rocm/jax-training:maxtext-v25.4" bash ./deepseek_v2_16b.sh

Note

The reported TFLOP/s by MaxText for DeepSeek is not accurate. Use the tokens/s as a performance indicator.


### Multi-node training benchmarking examples[#](#multi-node-training-benchmarking-examples)

The following examples use SLURM for running on multiple nodes – the commands might need to be adjusted for your own cluster setup.

Example 1: Multi-node training with Llama 2 7B

Download the benchmarking script:

`https://raw.githubusercontent.com/ROCm/maxtext/refs/heads/main/benchmarks/gpu-rocm/llama2_7b_multinode.sh`

Run the multi-node training benchmark. For example:

-N <num_nodes> llama2_7b_multinode.sh

Example 2: Multi-node training with Llama 2 70B

Download the benchmarking script:

`https://raw.githubusercontent.com/ROCm/maxtext/refs/heads/main/benchmarks/gpu-rocm/llama2_70b_multinode.sh`

Run the multi-node training benchmark. For example:

-N <num_nodes> llama2_70b_multinode.sh

Example 3: Multi-node training with Llama 3 8B model

Download the benchmarking script:

`https://raw.githubusercontent.com/ROCm/maxtext/refs/heads/main/benchmarks/gpu-rocm/llama3_8b_multinode.sh`

Run the multi-node training benchmark. For example:

-N <num_nodes> llama3_8b_multinode.sh

Example 4: Multi-node training with Llama 3 70B model

Download the benchmarking script:

`https://raw.githubusercontent.com/ROCm/maxtext/refs/heads/main/benchmarks/gpu-rocm/llama3_70b_multinode.sh`

Run the multi-node training benchmark. For example:

-N <num_nodes> llama3_70b_multinode.sh


## Previous versions[#](#previous-versions)

See [JAX MaxText training performance testing version history](jax-maxtext-history.html) to find documentation for previous releases
of the `ROCm/jax-training`

Docker image.
