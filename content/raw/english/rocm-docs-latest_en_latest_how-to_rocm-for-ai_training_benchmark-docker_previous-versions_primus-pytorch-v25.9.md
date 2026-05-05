---
title: "Training a model with Primus and PyTorch"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/training/benchmark-docker/previous-versions/primus-pytorch-v25.9.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:02:23.688004+00:00
content_hash: "113ea8e32e6bd663"
---

# Training a model with Primus and PyTorch[#](#training-a-model-with-primus-and-pytorch)

2026-04-21

16 min read time

Caution

This documentation does not reflect the latest version of ROCm Primus PyTorch training
performance benchmark documentation. See [Training a model with Primus and PyTorch](../primus-pytorch.html) for the latest version.

[Primus](https://github.com/AMD-AGI/Primus) is a unified and flexible
LLM training framework designed to streamline training. It streamlines LLM
training on AMD Instinct GPUs using a modular, reproducible configuration paradigm.
Primus now supports the PyTorch torchtitan backend.

Note

For a unified training solution on AMD GPUs with ROCm, the [rocm/pytorch-training](https://hub.docker.com/r/rocm/pytorch-training/) Docker Hub registry will be
deprecated soon in favor of [rocm/primus](https://hub.docker.com/r/rocm/primus).
The `rocm/primus`

Docker containers will cover PyTorch training ecosystem frameworks,
including torchtitan and [Megatron-LM](../primus-megatron.html).

Primus with the PyTorch torchtitan backend is designed to replace the
[ROCm PyTorch training](../pytorch-training.html) workflow. See
[Training a model with PyTorch on ROCm](../pytorch-training.html) to see steps to run workloads without Primus.

AMD provides a ready-to-use Docker image for MI355X, MI350X, MI325X, and MI300X GPUs containing essential components for Primus and PyTorch training with Primus Turbo optimizations.

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

The following models are pre-optimized for performance on the AMD Instinct MI325X and MI300X GPUs. Some instructions, commands, and training recommendations in this documentation might vary by model – select one to get started.

## System validation[#](#system-validation)

Before running AI workloads, it’s important to validate that your AMD hardware is configured correctly and performing optimally.

If you have already validated your system settings, including aspects like NUMA auto-balancing, you
can skip this step. Otherwise, complete the procedures in the [System validation and
optimization](../../../system-setup/prerequisite-system-validation.html#rocm-for-ai-system-optimization) guide to properly configure your system settings
before starting training.

To test for optimal performance, consult the recommended [System health benchmarks](../../../system-setup/system-health-check.html#rocm-for-ai-system-health-bench). This suite of tests will help you verify and fine-tune your
system’s configuration.

This Docker image is optimized for specific model configurations outlined below. Performance can vary for other training workloads, as AMD doesn’t test configurations and run conditions outside those described.

## Pull the Docker image[#](#pull-the-docker-image)

Use the following command to pull the Docker image from Docker Hub.

```
pull rocm/primus:v25.9_gfx950
```

```
pull rocm/primus:v25.9_gfx942
```

## Run training[#](#run-training)

Once the setup is complete, choose between the following two workflows to start benchmarking training.
For fine-tuning workloads and multi-node training examples, see [Training a model with PyTorch on ROCm](../pytorch-training.html) (without Primus).
For best performance on MI325X, MI350X, and MI355X GPUs, you might need to
tweak some configurations (such as batch sizes).

The following run command is tailored to Llama 3.1 8B.
See [Supported models](#amd-primus-pytorch-model-support-v259) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

For example, use this command to run the performance benchmark test on the Llama 3.1 8B model using one node with the BF16 data type on the host machine.

export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags primus_pyt_train_llama-3.1-8b \ --keep-model-dir \ --live-output \ --timeout 28800

MAD launches a Docker container with the name

`container_ci-primus_pyt_train_llama-3.1-8b`

. The latency and throughput reports of the model are collected in`~/MAD/perf.csv`

.Note

Currently, Primus torchtitan models are run with Primus Turbo enabled for enhanced performance. To disable Primus Turbo, modify respective configuration file

`scripts/primus/pytorch_train/primus_torchtitan_scripts/llama3_[8B|70B]-[BF16|FP8].yaml`

.

The following run command is tailored to Llama 3.1 70B.
See [Supported models](#amd-primus-pytorch-model-support-v259) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

For example, use this command to run the performance benchmark test on the Llama 3.1 70B model using one node with the BF16 data type on the host machine.

export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags primus_pyt_train_llama-3.1-70b \ --keep-model-dir \ --live-output \ --timeout 28800

MAD launches a Docker container with the name

`container_ci-primus_pyt_train_llama-3.1-70b`

. The latency and throughput reports of the model are collected in`~/MAD/perf.csv`

.Note

Currently, Primus torchtitan models are run with Primus Turbo enabled for enhanced performance. To disable Primus Turbo, modify respective configuration file

`scripts/primus/pytorch_train/primus_torchtitan_scripts/llama3_[8B|70B]-[BF16|FP8].yaml`

.

The following run commands are tailored to Llama 3.1 8B.
See [Supported models](#amd-primus-pytorch-model-support-v259) to switch to another available model.

Download the Docker image and required packages

Pull the appropriate Docker image for your AMD GPU architecture from Docker Hub.

pull rocm/primus:v25.9_gfx950

pull rocm/primus:v25.9_gfx942

Run the Docker container.

run -it \ --device /dev/dri \ --device /dev/kfd \ --network host \ --ipc host \ --group-add video \ --cap-add SYS_PTRACE \ --security-opt seccomp=unconfined \ --privileged \ -v $HOME:$HOME \ -v $HOME/.ssh:/root/.ssh \ --shm-size 64G \ --name training_env \ rocm/primus:v25.9_gfx950

run -it \ --device /dev/dri \ --device /dev/kfd \ --network host \ --ipc host \ --group-add video \ --cap-add SYS_PTRACE \ --security-opt seccomp=unconfined \ --privileged \ -v $HOME:$HOME \ -v $HOME/.ssh:/root/.ssh \ --shm-size 64G \ --name training_env \ rocm/primus:v25.9_gfx942

Use these commands if you exit the

`training_env`

container and need to return to it.start training_env docker exec -it training_env bash


Prepare training datasets and dependencies

The following benchmarking examples require downloading models and datasets
from Hugging Face. To ensure successful access to gated repos, set your
`HF_TOKEN`

.

```
export HF_TOKEN=$your_personal_hugging_face_access_token
```

Pretraining

To get started, navigate to the `Primus`

directory in your container.

```
cd /workspace/Primus
```

Now, to start the pretraining benchmark, use the `run_pretrain.sh`

script
included with Primus with the appropriate options.

Benchmarking examples

Use the following command to run train Llama 3.1 8B with BF16 precision using Primus torchtitan.

```
EXP=examples/torchtitan/configs/llama3.1_8B-BF16-pretrain.yaml \
bash examples/run_pretrain.sh \
--metrics.enable_tensorboard false \
--profiling.enable_profiling false \
--training.batch_size 5
```

```
EXP=examples/torchtitan/configs/llama3.1_8B-BF16-pretrain.yaml \
bash examples/run_pretrain.sh \
--metrics.enable_tensorboard false \
--profiling.enable_profiling false \
--training.batch_size 6
```

```
EXP=examples/torchtitan/configs/llama3.1_8B-BF16-pretrain.yaml \
bash examples/run_pretrain.sh \
--metrics.enable_tensorboard false \
--profiling.enable_profiling false \
--training.batch_size 4
```

To train Llama 3.1 8B with FP8 precision, use the following command.

```
EXP=examples/torchtitan/configs/llama3.1_8B-BF16-pretrain.yaml \
bash examples/run_pretrain.sh \
--metrics.enable_tensorboard false \
--profiling.enable_profiling false \
--training.batch_size 8
```

```
EXP=examples/torchtitan/configs/llama3.1_8B-FP8-pretrain.yaml \
bash examples/run_pretrain.sh \
--metrics.enable_tensorboard false \
--profiling.enable_profiling false \
--training.batch_size 7
```

```
EXP=examples/torchtitan/configs/llama3.1_8B-FP8-pretrain.yaml \
bash examples/run_pretrain.sh \
--metrics.enable_tensorboard false \
--profiling.enable_profiling false \
--training.batch_size 5
```

Use the following command to run train Llama 3.1 70B with BF16 precision using Primus torchtitan.

```
EXP=examples/torchtitan/configs/llama3.1_70B-BF16-pretrain.yaml \
bash examples/run_pretrain.sh \
--metrics.enable_tensorboard false \
--profiling.enable_profiling false \
--training.batch_size 8
```

```
EXP=examples/torchtitan/configs/llama3.1_70B-BF16-pretrain.yaml \
bash examples/run_pretrain.sh \
--metrics.enable_tensorboard false \
--profiling.enable_profiling false \
--training.batch_size 6
```

```
EXP=examples/torchtitan/configs/llama3.1_70B-BF16-pretrain.yaml \
bash examples/run_pretrain.sh \
--metrics.enable_tensorboard false \
--profiling.enable_profiling false \
--training.batch_size 4
```

To train Llama 3.1 70B with FP8 precision, use the following command.

```
EXP=examples/torchtitan/configs/llama3.1_70B-FP8-pretrain.yaml \
bash examples/run_pretrain.sh \
--metrics.enable_tensorboard false \
--profiling.enable_profiling false \
--training.batch_size 6
```

```
EXP=examples/torchtitan/configs/llama3.1_70B-FP8-pretrain.yaml \
bash examples/run_pretrain.sh \
--metrics.enable_tensorboard false \
--profiling.enable_profiling false \
--training.batch_size 5
```

```
EXP=examples/torchtitan/configs/llama3.1_70B-FP8-pretrain.yaml \
bash examples/run_pretrain.sh \
--metrics.enable_tensorboard false \
--profiling.enable_profiling false \
--training.batch_size 3
```

The following run commands are tailored to Llama 3.1 70B.
See [Supported models](#amd-primus-pytorch-model-support-v259) to switch to another available model.

Download the Docker image and required packages

Pull the appropriate Docker image for your AMD GPU architecture from Docker Hub.

pull rocm/primus:v25.9_gfx950

pull rocm/primus:v25.9_gfx942

Run the Docker container.

run -it \ --device /dev/dri \ --device /dev/kfd \ --network host \ --ipc host \ --group-add video \ --cap-add SYS_PTRACE \ --security-opt seccomp=unconfined \ --privileged \ -v $HOME:$HOME \ -v $HOME/.ssh:/root/.ssh \ --shm-size 64G \ --name training_env \ rocm/primus:v25.9_gfx950

run -it \ --device /dev/dri \ --device /dev/kfd \ --network host \ --ipc host \ --group-add video \ --cap-add SYS_PTRACE \ --security-opt seccomp=unconfined \ --privileged \ -v $HOME:$HOME \ -v $HOME/.ssh:/root/.ssh \ --shm-size 64G \ --name training_env \ rocm/primus:v25.9_gfx942

Use these commands if you exit the

`training_env`

container and need to return to it.start training_env docker exec -it training_env bash


Prepare training datasets and dependencies

The following benchmarking examples require downloading models and datasets
from Hugging Face. To ensure successful access to gated repos, set your
`HF_TOKEN`

.

```
export HF_TOKEN=$your_personal_hugging_face_access_token
```

Pretraining

To get started, navigate to the `Primus`

directory in your container.

```
cd /workspace/Primus
```

Now, to start the pretraining benchmark, use the `run_pretrain.sh`

script
included with Primus with the appropriate options.

Benchmarking examples

Use the following command to run train Llama 3.1 8B with BF16 precision using Primus torchtitan.

```
EXP=examples/torchtitan/configs/llama3.1_8B-BF16-pretrain.yaml \
bash examples/run_pretrain.sh \
--metrics.enable_tensorboard false \
--profiling.enable_profiling false \
--training.batch_size 5
```

```
EXP=examples/torchtitan/configs/llama3.1_8B-BF16-pretrain.yaml \
bash examples/run_pretrain.sh \
--metrics.enable_tensorboard false \
--profiling.enable_profiling false \
--training.batch_size 6
```

```
EXP=examples/torchtitan/configs/llama3.1_8B-BF16-pretrain.yaml \
bash examples/run_pretrain.sh \
--metrics.enable_tensorboard false \
--profiling.enable_profiling false \
--training.batch_size 4
```

To train Llama 3.1 8B with FP8 precision, use the following command.

```
EXP=examples/torchtitan/configs/llama3.1_8B-BF16-pretrain.yaml \
bash examples/run_pretrain.sh \
--metrics.enable_tensorboard false \
--profiling.enable_profiling false \
--training.batch_size 8
```

```
EXP=examples/torchtitan/configs/llama3.1_8B-FP8-pretrain.yaml \
bash examples/run_pretrain.sh \
--metrics.enable_tensorboard false \
--profiling.enable_profiling false \
--training.batch_size 7
```

```
EXP=examples/torchtitan/configs/llama3.1_8B-FP8-pretrain.yaml \
bash examples/run_pretrain.sh \
--metrics.enable_tensorboard false \
--profiling.enable_profiling false \
--training.batch_size 5
```

Use the following command to run train Llama 3.1 70B with BF16 precision using Primus torchtitan.

```
EXP=examples/torchtitan/configs/llama3.1_70B-BF16-pretrain.yaml \
bash examples/run_pretrain.sh \
--metrics.enable_tensorboard false \
--profiling.enable_profiling false \
--training.batch_size 8
```

```
EXP=examples/torchtitan/configs/llama3.1_70B-BF16-pretrain.yaml \
bash examples/run_pretrain.sh \
--metrics.enable_tensorboard false \
--profiling.enable_profiling false \
--training.batch_size 6
```

```
EXP=examples/torchtitan/configs/llama3.1_70B-BF16-pretrain.yaml \
bash examples/run_pretrain.sh \
--metrics.enable_tensorboard false \
--profiling.enable_profiling false \
--training.batch_size 4
```

To train Llama 3.1 70B with FP8 precision, use the following command.

```
EXP=examples/torchtitan/configs/llama3.1_70B-FP8-pretrain.yaml \
bash examples/run_pretrain.sh \
--metrics.enable_tensorboard false \
--profiling.enable_profiling false \
--training.batch_size 6
```

```
EXP=examples/torchtitan/configs/llama3.1_70B-FP8-pretrain.yaml \
bash examples/run_pretrain.sh \
--metrics.enable_tensorboard false \
--profiling.enable_profiling false \
--training.batch_size 5
```

```
EXP=examples/torchtitan/configs/llama3.1_70B-FP8-pretrain.yaml \
bash examples/run_pretrain.sh \
--metrics.enable_tensorboard false \
--profiling.enable_profiling false \
--training.batch_size 3
```

The following run commands are tailored to Llama 3.1 8B.
See [Supported models](#amd-primus-pytorch-model-support-v259) to switch to another available model.

Download the Docker image and required packages

Pull the appropriate Docker image for your AMD GPU architecture from Docker Hub.

pull rocm/primus:v25.9_gfx950

pull rocm/primus:v25.9_gfx942

Run the Docker container.

run -it \ --device /dev/dri \ --device /dev/kfd \ --network host \ --ipc host \ --group-add video \ --cap-add SYS_PTRACE \ --security-opt seccomp=unconfined \ --privileged \ -v $HOME:$HOME \ -v $HOME/.ssh:/root/.ssh \ --shm-size 64G \ --name training_env \ rocm/primus:v25.9_gfx950

run -it \ --device /dev/dri \ --device /dev/kfd \ --network host \ --ipc host \ --group-add video \ --cap-add SYS_PTRACE \ --security-opt seccomp=unconfined \ --privileged \ -v $HOME:$HOME \ -v $HOME/.ssh:/root/.ssh \ --shm-size 64G \ --name training_env \ rocm/primus:v25.9_gfx942

Use these commands if you exit the

`training_env`

container and need to return to it.start training_env docker exec -it training_env bash

Navigate to the

`torchtitan`

workspace directory.cd /workspace/torchtitan


Download the tokenizer

The following benchmarking examples require downloading models and datasets from Hugging Face. To ensure successful access to gated repos, set your

`HF_TOKEN`

.export HF_TOKEN=$your_personal_hugging_face_access_token

Download the tokenizer for your model.

scripts/download_tokenizer.py \ --repo_id meta-llama/Llama-3.1-8B \ --tokenizer_path "original" \ --hf_token=${HF_TOKEN}


Pretraining examples

Run the training script with the appropriate configuration file.

For train with BF16 precicion, use the following command:

```
CONFIG_FILE=./llama3_8b_fsdp_bf16.toml \
.run_train.sh
```

For train with BF16 precicion, use the following command:

```
CONFIG_FILE=./llama3_8b_fsdp_fp8.toml \
.run_train.sh
```

The following run commands are tailored to Llama 3.1 70B.
See [Supported models](#amd-primus-pytorch-model-support-v259) to switch to another available model.

Download the Docker image and required packages

Pull the appropriate Docker image for your AMD GPU architecture from Docker Hub.

pull rocm/primus:v25.9_gfx950

pull rocm/primus:v25.9_gfx942

Run the Docker container.

run -it \ --device /dev/dri \ --device /dev/kfd \ --network host \ --ipc host \ --group-add video \ --cap-add SYS_PTRACE \ --security-opt seccomp=unconfined \ --privileged \ -v $HOME:$HOME \ -v $HOME/.ssh:/root/.ssh \ --shm-size 64G \ --name training_env \ rocm/primus:v25.9_gfx950

run -it \ --device /dev/dri \ --device /dev/kfd \ --network host \ --ipc host \ --group-add video \ --cap-add SYS_PTRACE \ --security-opt seccomp=unconfined \ --privileged \ -v $HOME:$HOME \ -v $HOME/.ssh:/root/.ssh \ --shm-size 64G \ --name training_env \ rocm/primus:v25.9_gfx942

Use these commands if you exit the

`training_env`

container and need to return to it.start training_env docker exec -it training_env bash

Navigate to the

`torchtitan`

workspace directory.cd /workspace/torchtitan


Download the tokenizer

The following benchmarking examples require downloading models and datasets from Hugging Face. To ensure successful access to gated repos, set your

`HF_TOKEN`

.export HF_TOKEN=$your_personal_hugging_face_access_token

Download the tokenizer for your model.

scripts/download_tokenizer.py \ --repo_id meta-llama/Llama-3.1-70B \ --tokenizer_path "original" \ --hf_token=${HF_TOKEN}


Pretraining examples

Run the training script with the appropriate configuration file.

For train with BF16 precicion, use the following command:

```
CONFIG_FILE=./llama3_70b_fsdp_bf16.toml \
.run_train.sh
```

For train with BF16 precicion, use the following command:

```
CONFIG_FILE=./llama3_70b_fsdp_fp8.toml \
.run_train.sh
```

## Known issues[#](#known-issues)

PyTorch Profiler may produce inaccurate traces when CPU activity profiling is enabled.

## Further reading[#](#further-reading)

For an introduction to Primus, see

[Primus: A Lightweight, Unified Training Framework for Large Models on AMD GPUs](https://rocm.blogs.amd.com/software-tools-optimization/primus/README.html).To learn more about MAD and the

`madengine`

CLI, see the[MAD usage guide](https://github.com/ROCm/MAD?tab=readme-ov-file#usage-guide).To learn more about system settings and management practices to configure your system for AMD Instinct MI300X Series GPUs, see

[AMD Instinct MI300X system optimization](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi300x.html).For a list of other ready-made Docker images for AI with ROCm, see

[AMD Infinity Hub](https://www.amd.com/en/developer/resources/infinity-hub.html#f-amd_hub_category=AI%20%26%20ML%20Models).

## Previous versions[#](#previous-versions)

See [PyTorch training performance testing version history](pytorch-training-history.html) to find documentation for previous releases
of the `ROCm/pytorch-training`

Docker image.
