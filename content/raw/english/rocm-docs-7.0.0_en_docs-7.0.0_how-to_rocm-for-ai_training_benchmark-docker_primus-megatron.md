---
title: "Training a model with Primus and Megatron-Core"
source_url: "https://rocm.docs.amd.com/en/docs-7.0.0/how-to/rocm-for-ai/training/benchmark-docker/primus-megatron.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-03T00:03:23.613697+00:00
content_hash: "6becc97fa3c4387b"
---

# Training a model with Primus and Megatron-Core[#](#training-a-model-with-primus-and-megatron-core)

2025-09-11

13 min read time

[Primus](https://github.com/AMD-AIG-AIMA/Primus) is a unified and flexible
LLM training framework designed to streamline training. It streamlines LLM
training on AMD Instinct accelerators using a modular, reproducible configuration paradigm.
Primus is backend-agnostic and supports multiple training engines – including Megatron-Core.

Note

Primus with the Megatron-Core backend is intended to replace ROCm
Megatron-LM in this Dockerized training environment. To learn how to migrate
workloads from Megatron-LM to Primus with Megatron-Core, see
[Migrating workloads to Primus (Megatron-Core backend) from Megatron-LM](previous-versions/megatron-lm-primus-migration-guide.html).

For ease of use, AMD provides a ready-to-use Docker image for MI300 series accelerators containing essential components for Primus and Megatron-Core.

Note

This Docker environment is based on Python 3.10 and Ubuntu 22.04. For an alternative environment with
Python 3.12 and Ubuntu 24.04, see the [previous ROCm Megatron-LM v25.6 Docker release](previous-versions/megatron-lm-v25.6.html).

Software component |
Version |
|---|---|
ROCm |
6.4.2 |
Primus |
v0.1.0-rc1 |
PyTorch |
2.8.0a0+gitd06a406 |
Python |
3.10 |
Transformer Engine |
2.1.0.dev0+ba586519 |
hipBLASLt |
37ba1d36 |
Triton |
3.3.0 |
RCCL |
2.22.3 |

## Supported models[#](#supported-models)

The following models are pre-optimized for performance on AMD Instinct MI300X series accelerators. Some instructions, commands, and training examples in this documentation might vary by model – select one to get started.

Note

Some models, such as Llama, require an external license agreement through a third party (for example, Meta).

## System validation[#](#system-validation)

Before running AI workloads, it’s important to validate that your AMD hardware is configured correctly and performing optimally.

If you have already validated your system settings, including aspects like NUMA auto-balancing, you
can skip this step. Otherwise, complete the procedures in the [System validation and
optimization](../prerequisite-system-validation.html#rocm-for-ai-system-optimization) guide to properly configure your system settings
before starting training.

To test for optimal performance, consult the recommended [System health benchmarks](../../system-health-check.html#rocm-for-ai-system-health-bench). This suite of tests will help you verify and fine-tune your
system’s configuration.

### Environment setup[#](#environment-setup)

Use the following instructions to set up the environment, configure the script to train models, and
reproduce the benchmark results on MI300X series accelerators with the `rocm/megatron-lm:v25.7_py310`

image.

#### Download the Docker image[#](#download-the-docker-image)

Use the following command to pull the Docker image from Docker Hub.

pull rocm/megatron-lm:v25.7_py310

Launch the Docker container.

run -it \ --device /dev/dri \ --device /dev/kfd \ --device /dev/infiniband \ --network host --ipc host \ --group-add video \ --cap-add SYS_PTRACE \ --security-opt seccomp=unconfined \ --privileged \ -v $HOME:$HOME \ --shm-size 128G \ --name primus_training_env \ rocm/megatron-lm:v25.7_py310


Use these commands if you exit the

`primus_training_env`

container and need to return to it.start primus_training_env docker exec -it primus_training_env bash


The Docker container hosts verified release tag `v0.1.0-rc1`

of the [Primus](https://github.com/AMD-AIG-AIMA/Primus/tree/v0.1.0-rc1) repository.

## Configuration[#](#configuration)

Primus defines a training configuration in YAML for each model in
[examples/megatron/configs](https://github.com/AMD-AIG-AIMA/Primus/tree/v0.1.0-rc1/examples/megatron/configs).

To update training parameters for Llama 3.3 70B, you can update `examples/megatron/configs/llama3.3_70B-pretrain.yaml`

.
Note that training configuration YAML files for other models follow this naming convention.

To update training parameters for Llama 3.1 70B, you can update `examples/megatron/configs/llama3.1_70B-pretrain.yaml`

.
Note that training configuration YAML files for other models follow this naming convention.

To update training parameters for Llama 3.1 8B, you can update `examples/megatron/configs/llama3.1_8B-pretrain.yaml`

.
Note that training configuration YAML files for other models follow this naming convention.

To update training parameters for Llama 2 7B, you can update `examples/megatron/configs/llama2_7B-pretrain.yaml`

.
Note that training configuration YAML files for other models follow this naming convention.

To update training parameters for Llama 2 70B, you can update `examples/megatron/configs/llama2_70B-pretrain.yaml`

.
Note that training configuration YAML files for other models follow this naming convention.

To update training parameters for DeepSeek-V3 (proxy), you can update `examples/megatron/configs/deepseek_v3-pretrain.yaml`

.
Note that training configuration YAML files for other models follow this naming convention.

To update training parameters for DeepSeek-V2-Lite, you can update `examples/megatron/configs/deepseek_v2_lite-pretrain.yaml`

.
Note that training configuration YAML files for other models follow this naming convention.

To update training parameters for Mixtral 8x7B, you can update `examples/megatron/configs/mixtral_8x7B_v0.1-pretrain.yaml`

.
Note that training configuration YAML files for other models follow this naming convention.

To update training parameters for Mixtral 8x22B (proxy), you can update `examples/megatron/configs/mixtral_8x22B_v0.1-pretrain.yaml`

.
Note that training configuration YAML files for other models follow this naming convention.

To update training parameters for Qwen 2.5 7B, you can update `examples/megatron/configs/primus_qwen2.5_7B-pretrain.yaml`

.
Note that training configuration YAML files for other models follow this naming convention.

To update training parameters for Qwen 2.5 72B, you can update `examples/megatron/configs/qwen2.5_72B-pretrain.yaml`

.
Note that training configuration YAML files for other models follow this naming convention.

### Dataset options[#](#dataset-options)

You can use either mock data or real data for training.

Mock data can be useful for testing and validation. Use the

`mock_data`

field to toggle between mock and real data. The default value is`true`

for enabled.mock_data: true

If you’re using a real dataset, update the

`train_data_path`

field to point to the location of your dataset.false train_data_path: /path/to/your/dataset

Ensure that the files are accessible inside the Docker container.


### Tokenizer[#](#tokenizer)

In Primus, each model uses a tokenizer from Hugging Face. For example, Llama
3.1 8B model uses `tokenizer_model: meta-llama/Llama-3.1-8B`

and
`tokenizer_type: Llama3Tokenizer`

defined in the [llama3.1-8B model](https://github.com/AMD-AIG-AIMA/Primus/tree/v0.1.0-rc1/primus/configs/models/megatron/llama3.1_8B.yaml)
definition. As such, you need to set the `HF_TOKEN`

environment variable with
right permissions to access the tokenizer for each model.

```
# Export your HF_TOKEN in the workspace
export HF_TOKEN=<your_hftoken>
```

## Run training[#](#run-training)

Use the following example commands to set up the environment, configure
[key options](#amd-primus-megatron-lm-benchmark-test-vars), and run training on
MI300X series accelerators with the AMD Megatron-LM environment.

### Single node training[#](#single-node-training)

To run training on a single node, navigate to `/workspace/Primus`

and use the following setup command:

```
install -r requirements.txt
export HSA_NO_SCRATCH_RECLAIM=1
export NVTE_CK_USES_BWD_V3=1
```

Once setup is complete, run the appropriate training command.

To run pre-training for Llama 3.3 70B BF16, run:

```
EXP=examples/megatron/configs/llama3.3_70B-pretrain.yaml \
bash ./examples/run_pretrain.sh \
--micro_batch_size 2 \
--global_batch_size 16 \
--train_iters 50
```

To run pre-training for Llama 3.1 8B FP8, run:

```
EXP=examples/megatron/configs/llama3.1_8B-pretrain.yaml \
bash ./examples/run_pretrain.sh \
--train_iters 50 \
--fp8 hybrid
```

For Llama 3.1 8B BF16, use the following command:

```
EXP=examples/megatron/configs/llama3.1_8B-pretrain.yaml \
bash ./examples/run_pretrain.sh --train_iters 50
```

To run pre-training for Llama 3.1 70B BF16, run:

```
EXP=examples/megatron/configs/llama3.1_70B-pretrain.yaml \
bash ./examples/run_pretrain.sh \
--train_iters 50
```

To run the training on a single node for Llama 3.1 70B FP8 with proxy, use the following command:

```
EXP=examples/megatron/configs/llama3.1_70B-pretrain.yaml \
bash ./examples/run_pretrain.sh \
--train_iters 50 \
--num_layers 40 \
--fp8 hybrid \
--no_fp8_weight_transpose_cache true
```

Note

Use two or more nodes to run the *full* Llama 70B model with FP8 precision.

To run pre-training for Llama 2 7B FP8, run:

```
EXP=examples/megatron/configs/llama2_7B-pretrain.yaml \
bash ./examples/run_pretrain.sh \
--train_iters 50 \
--fp8 hybrid
```

To run pre-training for Llama 2 7B BF16, run:

```
EXP=examples/megatron/configs/llama2_7B-pretrain.yaml \
bash ./examples/run_pretrain.sh --train_iters 50
```

To run pre-training for Llama 2 70B BF16, run:

```
EXP=examples/megatron/configs/llama2_70B-pretrain.yaml \
bash ./examples/run_pretrain.sh --train_iters 50
```

To run training on a single node for DeepSeek-V3 (MoE with expert parallel) with 3-layer proxy, use the following command:

```
EXP=examples/megatron/configs/deepseek_v3-pretrain.yaml \
bash examples/run_pretrain.sh \
--num_layers 3 \
--moe_layer_freq 1 \
--train_iters 50
```

To run training on a single node for DeepSeek-V2-Lite (MoE with expert parallel), use the following command:

```
EXP=examples/megatron/configs/deepseek_v2_lite-pretrain.yaml \
bash examples/run_pretrain.sh \
--global_batch_size 256 \
--train_iters 50
```

To run training on a single node for Mixtral 8x7B (MoE with expert parallel), use the following command:

```
EXP=examples/megatron/configs/mixtral_8x7B_v0.1-pretrain.yaml \
bash examples/run_pretrain.sh --train_iters 50
```

To run training on a single node for Mixtral 8x7B (MoE with expert parallel) with 4-layer proxy, use the following command:

```
EXP=examples/megatron/configs/mixtral_8x22B_v0.1-pretrain.yaml \
bash examples/run_pretrain.sh \
--num_layers 4 \
--pipeline_model_parallel_size 1 \
--micro_batch_size 1 \
--global_batch_size 16 \
--train_iters 50
```

To run training on a single node for Qwen 2.5 7B BF16, use the following command:

```
EXP=examples/megatron/configs/qwen2.5_7B-pretrain.yaml \
bash examples/run_pretrain.sh --train_iters 50
```

For FP8, use the following command.

```
EXP=examples/megatron/configs/qwen2.5_7B-pretrain.yaml \
bash examples/run_pretrain.sh \
--train_iters 50 \
--fp8 hybrid
```

To run the training on a single node for Qwen 2.5 72B BF16, use the following command.

```
EXP=examples/megatron/configs/qwen2.5_72B-pretrain.yaml \
bash examples/run_pretrain.sh --train_iters 50
```

### Multi-node training examples[#](#multi-node-training-examples)

To run training on multiple nodes, you can use the
[run_slurm_pretrain.sh](https://github.com/AMD-AIG-AIMA/Primus/tree/v0.1.0-rc1/examples/run_slurm_pretrain.sh)
to launch the multi-node workload. Use the following steps to setup your environment:

```
cd /workspace/Primus/
export DOCKER_IMAGE=rocm/megatron-lm:v25.7_py310
export HF_TOKEN=<your_HF_token>
export HSA_NO_SCRATCH_RECLAIM=1
export NVTE_CK_USES_BWD_V3=1
export NCCL_IB_HCA=<your_NCCL_IB_HCA> # specify which RDMA interfaces to use for communication
export NCCL_SOCKET_IFNAME=<your_NCCL_SOCKET_IFNAME> # your Network Interface
export GLOO_SOCKET_IFNAME=<your_GLOO_SOCKET_IFNAME> # your Network Interface
export NCCL_IB_GID_INDEX=3 # Set InfiniBand GID index for NCCL communication. Default is 3 for ROCE
```

Note

Make sure correct network drivers are installed on the nodes. If inside a Docker, either install the drivers inside the Docker container or pass the network drivers from the host while creating Docker container.

If

`NCCL_IB_HCA`

and`NCCL_SOCKET_IFNAME`

are not set, Primus will try to auto-detect. However, since NICs can vary accross different cluster, it is encouraged to explicitly export your NCCL parameters for the cluster.To find your network interface, you can use

`ip a`

.To find RDMA interfaces, you can use

`ibv_devices`

to get the list of all the RDMA/IB devices.

To train Llama 3.3 70B FP8 on 8 nodes, run:

```
NNODES=8 EXP=examples/megatron/configs/llama3.3_70B-pretrain.yaml \
bash examples/run_slurm_pretrain.sh \
--micro_batch_size 4 \
--global_batch_size 256 \
--recompute_num_layers 80 \
--no_fp8_weight_transpose_cache true \
--fp8 hybrid
```

To train Llama 3.3 70B BF16 on 8 nodes, run:

```
NNODES=8 EXP=examples/megatron/configs/llama3.3_70B-pretrain.yaml \
bash examples/run_slurm_pretrain.sh \
--micro_batch_size 1 \
--global_batch_size 256 \
--recompute_num_layers 12
```

To train Llama 3.1 8B FP8 on 8 nodes, run:

```
# Adjust the training parameters. For e.g., `global_batch_size: 8 * #single_node_bs` for 8 nodes in this case
NNODES=8 EXP=examples/megatron/configs/llama3.1_8B-pretrain.yaml \
bash ./examples/run_slurm_pretrain.sh \
--global_batch_size 1024 \
--fp8 hybrid
```

To train Llama 3.1 70B FP8 on 8 nodes, run:

```
NNODES=8 EXP=examples/megatron/configs/llama3.1_70B-pretrain.yaml \
bash examples/run_slurm_pretrain.sh \
--micro_batch_size 4 \
--global_batch_size 256 \
--recompute_num_layers 80 \
--no_fp8_weight_transpose_cache true \
--fp8 hybrid
```

To train Llama 3.1 70B BF16 on 8 nodes, run:

```
NNODES=8 EXP=examples/megatron/configs/llama3.1_70B-pretrain.yaml \
bash examples/run_slurm_pretrain.sh \
--micro_batch_size 1 \
--global_batch_size 256 \
--recompute_num_layers 12
```

To train Llama 2 8B FP8 on 8 nodes, run:

```
# Adjust the training parameters. For e.g., `global_batch_size: 8 * #single_node_bs` for 8 nodes in this case
NNODES=8 EXP=examples/megatron/configs/llama2_7B-pretrain.yaml bash ./examples/run_slurm_pretrain.sh --global_batch_size 2048 --fp8 hybrid
```

To train Llama 2 70B FP8 on 8 nodes, run:

```
NNODES=8 EXP=examples/megatron/configs/llama2_70B-pretrain.yaml \
bash examples/run_slurm_pretrain.sh \
--micro_batch_size 10 \
--global_batch_size 640 \
--recompute_num_layers 80 \
--no_fp8_weight_transpose_cache true \
--fp8 hybrid
```

To train Llama 2 70B BF16 on 8 nodes, run:

```
NNODES=8 EXP=examples/megatron/configs/llama2_70B-pretrain.yaml \
bash ./examples/run_slurm_pretrain.sh \
--micro_batch_size 2 \
--global_batch_size 1536 \
--recompute_num_layers 12
```

To train Mixtral 8x7B BF16 on 8 nodes, run:

```
NNODES=8 EXP=examples/megatron/configs/mixtral_8x7B_v0.1-pretrain.yaml \
bash examples/run_slurm_pretrain.sh \
--micro_batch_size 2 \
--global_batch_size 256
```

To train Qwen2.5 72B FP8 on 8 nodes, run:

```
NNODES=8 EXP=examples/megatron/configs/qwen2.5_72B-pretrain.yaml \
bash examples/run_slurm_pretrain.sh \
--micro_batch_size 8 \
--global_batch_size 512 \
--recompute_num_layers 80 \
--no_fp8_weight_transpose_cache true \
--fp8 hybrid
```

### Key options[#](#key-options)

The following are key options to take note of

- fp8
`hybrid`

enables FP8 GEMMs.- use_torch_fsdp2
`use_torch_fsdp2: 1`

enables torch fsdp-v2. If FSDP is enabled, set`use_distributed_optimizer`

and`overlap_param_gather`

to`false`

.- profile
To enable PyTorch profiling, set these parameters:

profile: true use_pytorch_profiler: true profile_step_end: 7 profile_step_start: 6

- train_iters
The total number of iterations (default: 50).

- mock_data
True by default.

- micro_batch_size
Micro batch size.

- global_batch_size
Global batch size.

- recompute_granularity
For activation checkpointing.

- num_layers
For using a reduced number of layers as with proxy models.


## Previous versions[#](#previous-versions)

See [Megatron-LM training performance testing version history](previous-versions/megatron-lm-history.html) to find documentation for previous releases
of the `ROCm/megatron-lm`

Docker image.

This training environment now uses Primus with Megatron as the primary
configuration. Limited support for the legacy ROCm Megatron-LM is still
available. For instructions on using ROCm Megatron-LM, see the
[Training a model with Megatron-LM on ROCm](megatron-lm.html) document.
