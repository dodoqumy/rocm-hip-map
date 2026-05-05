---
title: "Training a model with Primus and Megatron-LM"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/training/benchmark-docker/previous-versions/primus-megatron-v25.9.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-03T00:02:05.731465+00:00
content_hash: "122dc38060102023"
---

# Training a model with Primus and Megatron-LM[#](#training-a-model-with-primus-and-megatron-lm)

2026-04-21

20 min read time

Caution

This documentation does not reflect the latest version of ROCm Megatron-LM
training performance documentation. See [Training a model with Primus and Megatron-LM](../primus-megatron.html) for the latest version.

[Primus](https://github.com/AMD-AGI/Primus) is a unified and flexible
training framework for AMD Instinct GPUs designed to support multiple training
engine backends – including Megatron – to deliver scalable, high-performance
model training. Performance acceleration is powered by [Primus Turbo](https://github.com/AMD-AGI/Primus-Turbo) and ROCm libraries.

Note

For a unified training solution on AMD GPUs with ROCm, the [rocm/megatron-lm](https://hub.docker.com/r/rocm/megatron-lm/) Docker Hub registry will be
deprecated soon in favor of [rocm/primus](https://hub.docker.com/r/rocm/primus).
The `rocm/primus`

Docker containers will cover PyTorch training ecosystem frameworks,
including Megatron-LM and [torchtitan](../primus-pytorch.html).

Primus with Megatron is designed to replace the [ROCm Megatron-LM
training](../megatron-lm.html) workflow. To learn how to migrate workloads from
Megatron-LM to Primus with Megatron, see
[Migrating workloads to Primus (Megatron backend) from Megatron-LM](megatron-lm-primus-migration-guide.html).

AMD provides a ready-to-use Docker images for MI355X, MI350X, MI325X, and MI300X GPUs containing essential components for Primus, ROCm, and Megatron-LM.

Software component |
Version |
|---|---|
ROCm |
7.0.0 |
Primus |
0.3.0 |
Primus Turbo |
0.1.1 |
PyTorch |
2.9.0.dev20250821+rocm7.0.0.lw.git125803b7 |
Python |
3.10 |
Transformer Engine |
2.2.0.dev0+54dd2bdc |
Flash Attention |
2.8.3 |
hipBLASLt |
911283acd1 |
Triton |
3.4.0+rocm7.0.0.git56765e8c |
RCCL |
2.26.6 |

Software component |
Version |
|---|---|
ROCm |
7.0.0 |
Primus |
0.3.0 |
Primus Turbo |
0.1.1 |
PyTorch |
2.9.0.dev20250821+rocm7.0.0.lw.git125803b7 |
Python |
3.10 |
Transformer Engine |
2.2.0.dev0+54dd2bdc |
Flash Attention |
2.8.3 |
hipBLASLt |
911283acd1 |
Triton |
3.4.0+rocm7.0.0.git56765e8c |
RCCL |
2.26.6 |

## Supported models[#](#supported-models)

The following models are pre-optimized for performance on AMD Instinct GPUs. Some instructions, commands, and training examples in this documentation might vary by model – select one to get started.

Note

Some models, such as Llama, require an external license agreement through a third party (for example, Meta).

## System validation[#](#system-validation)

Before running AI workloads, it’s important to validate that your AMD hardware is configured correctly and performing optimally.

If you have already validated your system settings, including aspects like NUMA auto-balancing, you
can skip this step. Otherwise, complete the procedures in the [System validation and
optimization](../../../system-setup/prerequisite-system-validation.html#rocm-for-ai-system-optimization) guide to properly configure your system settings
before starting training.

To test for optimal performance, consult the recommended [System health benchmarks](../../../system-setup/system-health-check.html#rocm-for-ai-system-health-bench). This suite of tests will help you verify and fine-tune your
system’s configuration.

## Environment setup[#](#environment-setup)

Use the following instructions to set up the environment, configure the script to train models, and reproduce the benchmark results on AMD Instinct GPUs.

Pull the Docker image

Pull the appropriate Docker image for your AMD GPU architecture from Docker Hub.

pull rocm/primus:v25.9_gfx950

pull rocm/primus:v25.9_gfx942

Launch the Docker container.

run -it \ --device /dev/dri \ --device /dev/kfd \ --device /dev/infiniband \ --network host --ipc host \ --group-add video \ --cap-add SYS_PTRACE \ --security-opt seccomp=unconfined \ --privileged \ -v $HOME:$HOME \ --shm-size 128G \ --name primus_training_env \ rocm/primus:v25.9_gfx950

run -it \ --device /dev/dri \ --device /dev/kfd \ --device /dev/infiniband \ --network host --ipc host \ --group-add video \ --cap-add SYS_PTRACE \ --security-opt seccomp=unconfined \ --privileged \ -v $HOME:$HOME \ --shm-size 128G \ --name primus_training_env \ rocm/primus:v25.9_gfx942


Use these commands if you exit the

`primus_training_env`

container and need to return to it.start primus_training_env docker exec -it primus_training_env bash


The Docker container hosts verified commit `e16b27b`

of the [Primus](https://github.com/AMD-AGI/Primus/tree/e16b27b) repository.

## Configuration[#](#configuration)

Primus defines a training configuration in YAML for each model in
[examples/megatron/configs](https://github.com/AMD-AGI/Primus/tree/e16b27bf6c1b2798f38848fc574fee60d9a9b902/examples/megatron/configs).

For example, to update training parameters for Llama 3.3 70B, you can
update `examples/megatron/configs/llama3.3_70B-pretrain.yaml`

. Training
configuration YAML files for other models follow this naming convention.

For example, to update training parameters for Llama 3.1 70B, you can
update `examples/megatron/configs/llama3.1_70B-pretrain.yaml`

. Training
configuration YAML files for other models follow this naming convention.

For example, to update training parameters for Llama 3.1 8B, you can
update `examples/megatron/configs/llama3.1_8B-pretrain.yaml`

. Training
configuration YAML files for other models follow this naming convention.

For example, to update training parameters for Llama 2 7B, you can
update `examples/megatron/configs/llama2_7B-pretrain.yaml`

. Training
configuration YAML files for other models follow this naming convention.

For example, to update training parameters for Llama 2 70B, you can
update `examples/megatron/configs/llama2_70B-pretrain.yaml`

. Training
configuration YAML files for other models follow this naming convention.

For example, to update training parameters for DeepSeek-V3 (proxy), you can
update `examples/megatron/configs/deepseek_v3-pretrain.yaml`

. Training
configuration YAML files for other models follow this naming convention.

For example, to update training parameters for DeepSeek-V2-Lite, you can
update `examples/megatron/configs/deepseek_v2_lite-pretrain.yaml`

. Training
configuration YAML files for other models follow this naming convention.

For example, to update training parameters for Mixtral 8x7B, you can
update `examples/megatron/configs/mixtral_8x7B_v0.1-pretrain.yaml`

. Training
configuration YAML files for other models follow this naming convention.

For example, to update training parameters for Mixtral 8x22B (proxy), you can
update `examples/megatron/configs/mixtral_8x22B_v0.1-pretrain.yaml`

. Training
configuration YAML files for other models follow this naming convention.

For example, to update training parameters for Qwen 2.5 7B, you can
update `examples/megatron/configs/primus_qwen2.5_7B-pretrain.yaml`

. Training
configuration YAML files for other models follow this naming convention.

For example, to update training parameters for Qwen 2.5 72B, you can
update `examples/megatron/configs/qwen2.5_72B-pretrain.yaml`

. Training
configuration YAML files for other models follow this naming convention.

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

Set the `HF_TOKEN`

environment variable with
right permissions to access the tokenizer for each model.

```
# Export your HF_TOKEN in the workspace
export HF_TOKEN=<your_hftoken>
```

Note

In Primus, each model uses a tokenizer from Hugging Face. For example, Llama
3.1 8B model uses `tokenizer_model: meta-llama/Llama-3.1-8B`

and
`tokenizer_type: Llama3Tokenizer`

defined in the [llama3.1-8B model](https://github.com/AMD-AGI/Primus/blob/e16b27bf6c1b2798f38848fc574fee60d9a9b902/examples/megatron/configs/llama3.1_8B-pretrain.yaml)
definition.

## Run training[#](#run-training)

Use the following example commands to set up the environment, configure
[key options](primus-megatron-v25.8.html#amd-primus-megatron-lm-benchmark-test-vars), and run training on
AMD Instinct GPUs using Primus with the Megatron backend.

### Single node training[#](#single-node-training)

To run training on a single node, navigate to `/workspace/Primus`

and use the following setup command:

```
install -r requirements.txt
export HSA_NO_SCRATCH_RECLAIM=1
export NVTE_CK_USES_BWD_V3=1
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to Llama 3.3 70B.
See [Supported models](#amd-primus-megatron-lm-model-support-v259) to switch to another available model.

To run pre-training for Llama 3.3 70B BF16, run:

```
EXP=examples/megatron/configs/llama3.3_70B-pretrain.yaml \
bash ./examples/run_pretrain.sh \
--train_iters 50 \
--micro_batch_size 6 \
--global_batch_size 48 \
```

```
EXP=examples/megatron/configs/llama3.3_70B-pretrain.yaml \
bash ./examples/run_pretrain.sh \
--train_iters 50 \
--micro_batch_size 2 \
--global_batch_size 16
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to Llama 3.1 8B.
See [Supported models](#amd-primus-megatron-lm-model-support-v259) to switch to another available model.

To run pre-training for Llama 3.1 8B FP8, run:

```
EXP=examples/megatron/configs/llama3.1_8B-pretrain.yaml \
bash ./examples/run_pretrain.sh \
--train_iters 50 \
--fp8 hybrid \
--micro_batch_size 4 \
--global_batch_size 512 \
```

```
EXP=examples/megatron/configs/llama3.1_8B-pretrain.yaml \
bash ./examples/run_pretrain.sh \
--train_iters 50 \
--fp8 hybrid
```

For Llama 3.1 8B BF16, use the following command:

```
EXP=examples/megatron/configs/llama3.1_8B-pretrain.yaml \
bash ./examples/run_pretrain.sh \
--train_iters 50 \
--micro_batch_size 4 \
--global_batch_size 512 \
```

```
EXP=examples/megatron/configs/llama3.1_8B-pretrain.yaml \
bash ./examples/run_pretrain.sh \
--train_iters 50
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to Llama 3.1 70B.
See [Supported models](#amd-primus-megatron-lm-model-support-v259) to switch to another available model.

To run pre-training for Llama 3.1 70B BF16, run:

```
EXP=examples/megatron/configs/llama3.1_70B-pretrain.yaml \
bash ./examples/run_pretrain.sh \
--train_iters 50 \
--micro_batch_size 4 \
--global_batch_size 32
```

```
EXP=examples/megatron/configs/llama3.1_70B-pretrain.yaml \
bash ./examples/run_pretrain.sh \
--train_iters 50
```

To run the training on a single node for Llama 3.1 70B FP8, use the following command.

Note

The MI300X configuration uses a proxy model. On MI300X GPUs, use two or more nodes to run the full Llama 3.1 70B model with FP8 precision. MI355X and MI350X GPUs can support the full 70B model with FP8 precision on a single node.

```
EXP=examples/megatron/configs/llama3.1_70B-pretrain.yaml \
bash ./examples/run_pretrain.sh \
--train_iters 50 \
--fp8 hybrid \
--no_fp8_weight_transpose_cache true \
--micro_batch_size 3 \
--global_batch_size 24
```

```
EXP=examples/megatron/configs/llama3.1_70B-pretrain.yaml \
bash ./examples/run_pretrain.sh \
--train_iters 50 \
--num_layers 40 \
--fp8 hybrid \
--no_fp8_weight_transpose_cache true
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to Llama 2 7B.
See [Supported models](#amd-primus-megatron-lm-model-support-v259) to switch to another available model.

To run pre-training for Llama 2 7B FP8, run:

```
EXP=examples/megatron/configs/llama2_7B-pretrain.yaml \
bash ./examples/run_pretrain.sh \
--train_iters 50 \
--fp8 hybrid \
--micro_batch_size 13 \
--global_batch_size 416
```

```
EXP=examples/megatron/configs/llama2_7B-pretrain.yaml \
bash ./examples/run_pretrain.sh \
--train_iters 50 \
--fp8 hybrid
```

To run pre-training for Llama 2 7B BF16, run:

```
EXP=examples/megatron/configs/llama2_7B-pretrain.yaml \
bash ./examples/run_pretrain.sh \
--train_iters 50 \
--micro_batch_size 10 \
--global_batch_size 640
```

```
EXP=examples/megatron/configs/llama2_7B-pretrain.yaml \
bash ./examples/run_pretrain.sh \
--train_iters 50
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to Llama 2 70B.
See [Supported models](#amd-primus-megatron-lm-model-support-v259) to switch to another available model.

To run pre-training for Llama 2 70B BF16, run:

```
EXP=examples/megatron/configs/llama2_70B-pretrain.yaml \
bash ./examples/run_pretrain.sh \
--train_iters 50 \
--micro_batch_size 17 \
--global_batch_size 272
```

```
EXP=examples/megatron/configs/llama2_70B-pretrain.yaml \
bash ./examples/run_pretrain.sh \
--train_iters 50
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to DeepSeek-V3.
See [Supported models](#amd-primus-megatron-lm-model-support-v259) to switch to another available model.

To run training on a single node for DeepSeek-V3 (MoE with expert parallel) BF16 with 3-layer proxy, use the following command:

```
EXP=examples/megatron/configs/deepseek_v3-pretrain.yaml \
bash examples/run_pretrain.sh \
--num_layers 3 \
--moe_layer_freq 1 \
--train_iters 50 \
--micro_batch_size 8 \
--global_batch_size 64
```

```
EXP=examples/megatron/configs/deepseek_v3-pretrain.yaml \
bash examples/run_pretrain.sh \
--num_layers 3 \
--moe_layer_freq 1 \
--train_iters 50
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to DeepSeek-V2-Lite.
See [Supported models](#amd-primus-megatron-lm-model-support-v259) to switch to another available model.

To run training on a single node for DeepSeek-V2-Lite (MoE with expert parallel) BF16, use the following command:

```
EXP=examples/megatron/configs/deepseek_v2_lite-pretrain.yaml \
bash examples/run_pretrain.sh \
--train_iters 50 \
--micro_batch_size 12 \
--global_batch_size 768
```

```
EXP=examples/megatron/configs/deepseek_v2_lite-pretrain.yaml \
bash examples/run_pretrain.sh \
--train_iters 50 \
--global_batch_size 256
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to Mixtral 8x7B.
See [Supported models](#amd-primus-megatron-lm-model-support-v259) to switch to another available model.

To run training on a single node for Mixtral 8x7B (MoE with expert parallel), use the following command:

```
EXP=examples/megatron/configs/mixtral_8x7B_v0.1-pretrain.yaml \
bash examples/run_pretrain.sh \
--train_iters 50 \
--micro_batch_size 4 \
--global_batch_size 256
```

```
EXP=examples/megatron/configs/mixtral_8x7B_v0.1-pretrain.yaml \
bash examples/run_pretrain.sh \
--train_iters 50
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to Mixtral 8x22B.
See [Supported models](#amd-primus-megatron-lm-model-support-v259) to switch to another available model.

To run training on a single node for Mixtral 8x22B BF16 (MoE with expert parallel) 4-layer proxy, use the following command:

```
EXP=examples/megatron/configs/mixtral_8x22B_v0.1-pretrain.yaml \
bash examples/run_pretrain.sh \
--train_iters 50 \
--num_layers 4 \
--pipeline_model_parallel_size 1 \
--micro_batch_size 2 \
--global_batch_size 16
```

```
EXP=examples/megatron/configs/mixtral_8x22B_v0.1-pretrain.yaml \
bash examples/run_pretrain.sh \
--train_iters 50 \
--num_layers 4 \
--pipeline_model_parallel_size 1 \
--micro_batch_size 1 \
--global_batch_size 16
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to Qwen 2.5 7B.
See [Supported models](#amd-primus-megatron-lm-model-support-v259) to switch to another available model.

To run training on a single node for Qwen 2.5 7B BF16, use the following command:

```
EXP=examples/megatron/configs/qwen2.5_7B-pretrain.yaml \
bash examples/run_pretrain.sh \
--train_iters 50 \
--micro_batch_size 16 \
--global_batch_size 768
```

```
EXP=examples/megatron/configs/qwen2.5_7B-pretrain.yaml \
bash examples/run_pretrain.sh \
--train_iters 50
```

For FP8, use the following command.

```
EXP=examples/megatron/configs/qwen2.5_7B-pretrain.yaml \
bash examples/run_pretrain.sh \
--train_iters 50 \
--fp8 hybrid
--micro_batch_size 20 \
--global_batch_size 800
```

```
EXP=examples/megatron/configs/qwen2.5_7B-pretrain.yaml \
bash examples/run_pretrain.sh \
--train_iters 50 \
--fp8 hybrid
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to Qwen 2.5 72B.
See [Supported models](#amd-primus-megatron-lm-model-support-v259) to switch to another available model.

To run the training on a single node for Qwen 2.5 72B BF16, use the following command.

```
EXP=examples/megatron/configs/qwen2.5_72B-pretrain.yaml \
bash examples/run_pretrain.sh \
--train_iters 50 \
--micro_batch_size 16 \
--global_batch_size 256
```

```
EXP=examples/megatron/configs/qwen2.5_72B-pretrain.yaml \
bash examples/run_pretrain.sh \
--train_iters 50
```

### Multi-node training examples[#](#multi-node-training-examples)

Refer to [Multi-node setup for AI workloads](../../../system-setup/multi-node-setup.html) to configure your environment for multi-node
training.

To run training on multiple nodes, you can use the
[run_slurm_pretrain.sh](https://github.com/AMD-AGI/Primus/blob/main/examples/run_slurm_pretrain.sh)
to launch the multi-node workload. Use the following steps to setup your environment:

```
clone --recurse-submodules https://github.com/AMD-AGI/Primus.git
cd Primus
git checkout e16b27b
export DOCKER_IMAGE=rocm/primus:v25.9_gfx950
export HF_TOKEN=<your_HF_token>
export HSA_NO_SCRATCH_RECLAIM=1
export NVTE_CK_USES_BWD_V3=1
export NCCL_IB_HCA=<your_NCCL_IB_HCA> # specify which RDMA interfaces to use for communication
export NCCL_SOCKET_IFNAME=<your_NCCL_SOCKET_IFNAME> # your Network Interface
export GLOO_SOCKET_IFNAME=<your_GLOO_SOCKET_IFNAME> # your Network Interface
export NCCL_IB_GID_INDEX=3 # Set InfiniBand GID index for NCCL communication. Default is 3 for ROCE
```

```
clone --recurse-submodules https://github.com/AMD-AGI/Primus.git
cd Primus
git checkout e16b27b
export DOCKER_IMAGE=rocm/primus:v25.9_gfx942
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

to get the list of all the RDMA/IB devices.Remember to set

`DOCKER_IMAGE`

and`HF_TOKEN`

(see[Tokenizer](#amd-primus-megatron-lm-tokenizer-v259)) as appropriate.

Once setup is complete, run the appropriate training command.
The following run commands are tailored to Llama 3.1 8B.
See [Supported models](#amd-primus-megatron-lm-model-support-v259) to switch to another available model.

To train Llama 3.1 8B FP8 on 8 nodes, run:

```
# Adjust the training parameters.
# For example, `global_batch_size: 8 * #single_node_bs` for 8 nodes in this case.
NNODES=8 \
EXP=examples/megatron/configs/llama3.1_8B-pretrain.yaml \
bash ./examples/run_slurm_pretrain.sh \
--global_batch_size 1024 \
--fp8 hybrid
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to Llama 2 7B.
See [Supported models](#amd-primus-megatron-lm-model-support-v259) to switch to another available model.

To train Llama 2 7B FP8 on 8 nodes, run:

```
# Adjust the training parameters.
# For example, `global_batch_size: 8 * #single_node_bs` for 8 nodes in this case.
NNODES=8 \
EXP=examples/megatron/configs/llama2_7B-pretrain.yaml \
bash ./examples/run_slurm_pretrain.sh \
--global_batch_size 2048 \
--fp8 hybrid
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to Llama 3.1 70B.
See [Supported models](#amd-primus-megatron-lm-model-support-v259) to switch to another available model.

To train Llama 3.1 70B FP8 on 8 nodes, run:

```
# Adjust the training parameters.
# For example, `global_batch_size: 8 * #single_node_bs` for 8 nodes in this case.
NNODES=8 \
EXP=examples/megatron/configs/llama3.1_70B-pretrain.yaml \
bash examples/run_slurm_pretrain.sh \
--micro_batch_size 4 \
--global_batch_size 256 \
--recompute_num_layers 80 \
--no_fp8_weight_transpose_cache true \
--fp8 hybrid
```

To train Llama 3.1 70B BF16 on 8 nodes, run:

```
NNODES=8 \
EXP=examples/megatron/configs/llama3.1_70B-pretrain.yaml \
bash examples/run_slurm_pretrain.sh \
--micro_batch_size 1 \
--global_batch_size 256 \
--recompute_num_layers 12
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to Llama 2 70B.
See [Supported models](#amd-primus-megatron-lm-model-support-v259) to switch to another available model.

To train Llama 2 70B FP8 on 8 nodes, run:

```
# Adjust the training parameters.
# For example, `global_batch_size: 8 * #single_node_bs` for 8 nodes in this case.
NNODES=8 \
EXP=examples/megatron/configs/llama2_70B-pretrain.yaml \
bash examples/run_slurm_pretrain.sh \
--micro_batch_size 10 \
--global_batch_size 640 \
--recompute_num_layers 80 \
--no_fp8_weight_transpose_cache true \
--fp8 hybrid
```

To train Llama 2 70B BF16 on 8 nodes, run:

```
NNODES=8 \
EXP=examples/megatron/configs/llama2_70B-pretrain.yaml \
bash ./examples/run_slurm_pretrain.sh \
--micro_batch_size 2 \
--global_batch_size 1536 \
--recompute_num_layers 12
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to Llama 3.3 70B.
See [Supported models](#amd-primus-megatron-lm-model-support-v259) to switch to another available model.

To train Llama 3.3 70B FP8 on 8 nodes, run:

```
# Adjust the training parameters.
# For example, `global_batch_size: 8 * #single_node_bs` for 8 nodes in this case
NNODES=8 \
EXP=examples/megatron/configs/llama3.3_70B-pretrain.yaml \
bash examples/run_slurm_pretrain.sh \
--micro_batch_size 4 \
--global_batch_size 256 \
--recompute_num_layers 80 \
--no_fp8_weight_transpose_cache true \
--fp8 hybrid
```

To train Llama 3.3 70B BF16 on 8 nodes, run:

```
NNODES=8 \
EXP=examples/megatron/configs/llama3.3_70B-pretrain.yaml \
bash examples/run_slurm_pretrain.sh \
--micro_batch_size 1 \
--global_batch_size 256 \
--recompute_num_layers 12
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to Llama 2 70B.
See [Supported models](#amd-primus-megatron-lm-model-support-v259) to switch to another available model.

To train Mixtral 8x7B BF16 on 8 nodes, run:

```
# Adjust the training parameters.
# For example, `global_batch_size: 8 * #single_node_bs` for 8 nodes in this case
NNODES=8 \
EXP=examples/megatron/configs/mixtral_8x7B_v0.1-pretrain.yaml \
bash examples/run_slurm_pretrain.sh \
--micro_batch_size 2 \
--global_batch_size 256
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to Llama 2 70B.
See [Supported models](#amd-primus-megatron-lm-model-support-v259) to switch to another available model.

To train Qwen2.5 72B FP8 on 8 nodes, run:

```
# Adjust the training parameters.
# For example, `global_batch_size: 8 * #single_node_bs` for 8 nodes in this case
NNODES=8 \
EXP=examples/megatron/configs/qwen2.5_72B-pretrain.yaml \
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


## Known issues[#](#known-issues)

PyTorch Profiler may produce inaccurate traces when CPU activity profiling is enabled.

## Further reading[#](#further-reading)

For an introduction to Primus, see

[Primus: A Lightweight, Unified Training Framework for Large Models on AMD GPUs](https://rocm.blogs.amd.com/software-tools-optimization/primus/README.html).To learn more about system settings and management practices to configure your system for AMD Instinct MI300X Series GPUs, see

[AMD Instinct MI300X system optimization](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi300x.html).For a list of other ready-made Docker images for AI with ROCm, see

[AMD Infinity Hub](https://www.amd.com/en/developer/resources/infinity-hub.html#f-amd_hub_category=AI%20%26%20ML%20Models).

## Previous versions[#](#previous-versions)

See [Megatron-LM training performance testing version history](megatron-lm-history.html) to find documentation for previous releases
of the `ROCm/megatron-lm`

Docker image.

This training environment now uses Primus with Megatron as the primary
configuration. Limited support for the legacy ROCm Megatron-LM is still
available; see the [Training a model with Megatron-LM on ROCm](../megatron-lm.html) documentation.
