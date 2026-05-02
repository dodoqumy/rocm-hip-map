---
title: "Training a model with Primus and PyTorch"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/training/benchmark-docker/previous-versions/primus-pytorch-v25.8.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T12:03:56.321958+00:00
content_hash: "a8bfd2ad899b2873"
---

# Training a model with Primus and PyTorch[#](#training-a-model-with-primus-and-pytorch)

2026-04-21

9 min read time

Caution

This documentation does not reflect the latest version of ROCm Primus PyTorch training
performance benchmark documentation. See [Training a model with Primus and PyTorch](../primus-pytorch.html) for the latest version.

[Primus](https://github.com/AMD-AGI/Primus) is a unified and flexible
LLM training framework designed to streamline training. It streamlines LLM
training on AMD Instinct GPUs using a modular, reproducible configuration paradigm.
Primus now supports the PyTorch torchtitan backend.

Note

Primus with the PyTorch torchtitan backend is designed to replace the [ROCm PyTorch training](../pytorch-training.html) workflow.
See [Training a model with PyTorch on ROCm](../pytorch-training.html) to see steps to run workloads without Primus.

For ease of use, AMD provides a ready-to-use Docker image – `rocm/pytorch-training:v25.8`

– for MI300X series GPUs containing essential
components for Primus and PyTorch training with
Primus Turbo optimizations.

Software component |
Version |
|---|---|
ROCm |
6.4.3 |
PyTorch |
2.8.0a0+gitd06a406 |
Python |
3.10.18 |
Transformer Engine |
2.2.0.dev0+a1e66aae |
Flash Attention |
3.0.0.post1 |
hipBLASLt |
1.1.0-d1b517fc7a |

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

### Pull the Docker image[#](#pull-the-docker-image)

Use the following command to pull the [Docker image](https://hub.docker.com/layers/rocm/pytorch-training/v25.8/images/sha256-5082ae01d73fec6972b0d84e5dad78c0926820dcf3c19f301d6c8eb892e573c5) from Docker Hub.

```
pull rocm/pytorch-training:v25.8
```

### Run training[#](#run-training)

Once the setup is complete, choose between the following two workflows to start benchmarking training.
For fine-tuning workloads and multi-node training examples, see [Training a model with PyTorch on ROCm](../pytorch-training.html) (without Primus).

The following run command is tailored to Llama 3.1 8B.
See [Supported models](#amd-primus-pytorch-model-support-v258) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

For example, use this command to run the performance benchmark test on the Llama 3.1 8B model using one node with the BF16 data type on the host machine.

export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags primus_pyt_train_llama-3.1-8b \ --keep-model-dir \ --live-output \ --timeout 28800

MAD launches a Docker container with the name

`container_ci-primus_pyt_train_llama-3.1-8b`

. The latency and throughput reports of the model are collected in`~/MAD/perf.csv`

.

The following run command is tailored to Llama 3.1 70B.
See [Supported models](#amd-primus-pytorch-model-support-v258) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

For example, use this command to run the performance benchmark test on the Llama 3.1 70B model using one node with the BF16 data type on the host machine.

export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags primus_pyt_train_llama-3.1-70b \ --keep-model-dir \ --live-output \ --timeout 28800

MAD launches a Docker container with the name

`container_ci-primus_pyt_train_llama-3.1-70b`

. The latency and throughput reports of the model are collected in`~/MAD/perf.csv`

.

The following run commands are tailored to Llama 3.1 8B.
See [Supported models](#amd-primus-pytorch-model-support-v258) to switch to another available model.

Download the Docker image and required packages

Use the following command to pull the Docker image from Docker Hub.

pull rocm/pytorch-training:v25.8

Run the Docker container.

run -it \ --device /dev/dri \ --device /dev/kfd \ --network host \ --ipc host \ --group-add video \ --cap-add SYS_PTRACE \ --security-opt seccomp=unconfined \ --privileged \ -v $HOME:$HOME \ -v $HOME/.ssh:/root/.ssh \ --shm-size 64G \ --name training_env \ rocm/pytorch-training:v25.8

Use these commands if you exit the

`training_env`

container and need to return to it.start training_env docker exec -it training_env bash

In the Docker container, clone the

[ROCm/MAD](https://github.com/ROCm/MAD)repository and navigate to the benchmark scripts directory`/workspace/MAD/scripts/pytorch_train`

.clone https://github.com/ROCm/MAD cd MAD/scripts/pytorch_train


Prepare training datasets and dependencies

The following benchmarking examples require downloading models and datasets from Hugging Face. To ensure successful access to gated repos, set your

`HF_TOKEN`

.export HF_TOKEN=$your_personal_hugging_face_access_token

Run the setup script to install libraries and datasets needed for benchmarking.


Pretraining

To start the pretraining benchmark, use the following command with the appropriate options. See the following list of options and their descriptions.

```
-t pretrain \
-m Llama-3.1-8B \
-p $datatype \
-s $sequence_length
```

Name |
Options |
Description |
|---|---|---|
|
|
Currently, only Llama 3.1 8B supports FP8 precision. |
|
Sequence length for the language model. |
Between 2048 and 8192. 8192 by default. |

Benchmarking examples

Use the following command to run train Llama 3.1 8B with BF16 precision using Primus torchtitan.

```
-m Llama-3.1-8B
```

To train Llama 3.1 8B with FP8 precision, use the following command.

```
-m Llama-3.1-8B -p FP8
```

The following run commands are tailored to Llama 3.1 70B.
See [Supported models](#amd-primus-pytorch-model-support-v258) to switch to another available model.

Download the Docker image and required packages

Use the following command to pull the Docker image from Docker Hub.

pull rocm/pytorch-training:v25.8

Run the Docker container.

run -it \ --device /dev/dri \ --device /dev/kfd \ --network host \ --ipc host \ --group-add video \ --cap-add SYS_PTRACE \ --security-opt seccomp=unconfined \ --privileged \ -v $HOME:$HOME \ -v $HOME/.ssh:/root/.ssh \ --shm-size 64G \ --name training_env \ rocm/pytorch-training:v25.8

Use these commands if you exit the

`training_env`

container and need to return to it.start training_env docker exec -it training_env bash

In the Docker container, clone the

[ROCm/MAD](https://github.com/ROCm/MAD)repository and navigate to the benchmark scripts directory`/workspace/MAD/scripts/pytorch_train`

.clone https://github.com/ROCm/MAD cd MAD/scripts/pytorch_train


Prepare training datasets and dependencies

The following benchmarking examples require downloading models and datasets from Hugging Face. To ensure successful access to gated repos, set your

`HF_TOKEN`

.export HF_TOKEN=$your_personal_hugging_face_access_token

Run the setup script to install libraries and datasets needed for benchmarking.


Pretraining

To start the pretraining benchmark, use the following command with the appropriate options. See the following list of options and their descriptions.

```
-t pretrain \
-m Llama-3.1-70B \
-p $datatype \
-s $sequence_length
```

Name |
Options |
Description |
|---|---|---|
|
|
Currently, only Llama 3.1 8B supports FP8 precision. |
|
Sequence length for the language model. |
Between 2048 and 8192. 8192 by default. |

Benchmarking examples

Use the following command to run train Llama 3.1 70B with BF16 precision using Primus torchtitan.

```
-m Llama-3.1-70B
```

To train Llama 3.1 70B with FP8 precision, use the following command.

```
-m Llama-3.1-70B -p FP8
```

## Further reading[#](#further-reading)

For an introduction to Primus, see

[Primus: A Lightweight, Unified Training Framework for Large Models on AMD GPUs](https://rocm.blogs.amd.com/software-tools-optimization/primus/README.html).To learn more about MAD and the

`madengine`

CLI, see the[MAD usage guide](https://github.com/ROCm/MAD?tab=readme-ov-file#usage-guide).To learn more about system settings and management practices to configure your system for AMD Instinct MI300X series GPUs, see

[AMD Instinct MI300X system optimization](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi300x.html).For a list of other ready-made Docker images for AI with ROCm, see

[AMD Infinity Hub](https://www.amd.com/en/developer/resources/infinity-hub.html#f-amd_hub_category=AI%20%26%20ML%20Models).

## Previous versions[#](#previous-versions)

See [PyTorch training performance testing version history](pytorch-training-history.html) to find documentation for previous releases
of the `ROCm/pytorch-training`

Docker image.
