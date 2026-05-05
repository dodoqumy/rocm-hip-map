---
title: "Prerequisite system validation before running AI workloads"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/system-setup/prerequisite-system-validation.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:01:50.274304+00:00
content_hash: "67b926e836e3fb46"
---

# Prerequisite system validation before running AI workloads[#](#prerequisite-system-validation-before-running-ai-workloads)

2026-01-23

6 min read time

Complete the following system validation and optimization steps to set up your system before starting training and inference.

## Disable NUMA auto-balancing[#](#disable-numa-auto-balancing)

Generally, application performance can benefit from disabling NUMA auto-balancing. However, it might be detrimental to performance with certain types of workloads.

Run the command `cat /proc/sys/kernel/numa_balancing`

to check your current NUMA (Non-Uniform
Memory Access) settings. Output `0`

indicates this setting is disabled. If there is no output or
the output is `1`

, run the following command to disable NUMA auto-balancing.

```
sh -c 'echo 0 > /proc/sys/kernel/numa_balancing'
```

See [Disable NUMA auto-balancing](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi300x.html#disable-numa-auto-balancing)
in the Instinct documentation for more information.

## Hardware verification with ROCm[#](#hardware-verification-with-rocm)

Use the command `amd-smi set --perf-determinism 1900`

to set the max clock speed up to 1900 MHz
instead of the default 2100 MHz. This can reduce the chance of a PCC event lowering the attainable
GPU clocks. This setting will not be required for new IFWI releases with the production PRC feature.
You can restore this setting to its default value with the `amd-smi reset --clocks`

command.

Run the command:

```
set --perf-determinism 1900
```

See [Hardware verfication for ROCm](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi300x.html#hardware-verification-with-rocm)
in the Instinct documentation for more information.

## RCCL Bandwidth Test for multi-node setups[#](#rccl-bandwidth-test-for-multi-node-setups)

ROCm Collective Communications Library (RCCL) is a standalone library of standard collective communication
routines for GPUs. See the [RCCL documentation](https://rocm.docs.amd.com/projects/rccl/en/latest/index.html) for more information. Before starting
pretraining, running a RCCL bandwidth test helps ensure that the multi-GPU or multi-node setup is optimized
for efficient distributed training.

Running the RCCL bandwidth test helps verify that:

The GPUs can communicate across nodes or within a single node.

The interconnect (such as InfiniBand, Ethernet, or Infinite fabric) is functioning as expected and provides adequate bandwidth for communication.

No hardware setup or cabling issues could affect the communication between GPUs


### Tuning and optimizing hyperparameters[#](#tuning-and-optimizing-hyperparameters)

In distributed training, specific hyperparameters related to distributed communication can be tuned based on the results of the RCCL bandwidth test. These variables are already set in the Docker image:

```
# force all RCCL streams to be high priority
export TORCH_NCCL_HIGH_PRIORITY=1
# specify which RDMA interfaces to use for communication
export NCCL_IB_HCA=rdma0,rdma1,rdma2,rdma3,rdma4,rdma5,rdma6,rdma7
# define the Global ID index used in RoCE mode
export NCCL_IB_GID_INDEX=3
# avoid data corruption/mismatch issue that existed in past releases
export RCCL_MSCCL_ENABLE=0
```

### Running the RCCL Bandwidth Test[#](#running-the-rccl-bandwidth-test)

It’s recommended you run the RCCL bandwidth test before launching training. It ensures system
performance is sufficient to launch training. RCCL is not included in the AMD Megatron-LM Docker
image; follow the instructions in [ROCm/rccl-tests](https://github.com/ROCm/rccl-tests) to get started.
See [RCCL](../inference-optimization/workload.html#mi300x-rccl) for more information.

Run on 8 GPUs (`-g 8`

), scanning from 8 bytes to 10 GB:

```
-b 8 -e 10G -f 2 -g 8
```


Using one MPI process per GPU and `-g 1`

for performance-oriented runs on both single-node and multi-node is
recommended. So, a run on 8 GPUs looks something like:

```
-np 8 --bind-to numa ./build/all_reduce_perf -b 8 -e 10G -f 2 -g 1
```


Running with one MPI process per GPU ensures a one-to-one mapping for CPUs and GPUs, which can be beneficial for smaller message sizes. This better represents the real-world use of RCCL in deep learning frameworks like PyTorch and TensorFlow.

Use the following script to run the RCCL test for four MI300X GPU nodes. Modify paths and node addresses as needed.
