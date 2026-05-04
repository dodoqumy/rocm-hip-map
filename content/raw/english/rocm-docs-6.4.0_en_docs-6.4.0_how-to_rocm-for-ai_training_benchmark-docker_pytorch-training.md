---
title: "Training a model with PyTorch for ROCm"
source_url: "https://rocm.docs.amd.com/en/docs-6.4.0/how-to/rocm-for-ai/training/benchmark-docker/pytorch-training.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:22:02.139812+00:00
content_hash: "5569e33cc735aaf4"
---

# Training a model with PyTorch for ROCm[#](#training-a-model-with-pytorch-for-rocm)

2025-05-13

9 min read time

PyTorch is an open-source machine learning framework that is widely used for model training with GPU-optimized components for transformer-based models.

The [PyTorch for ROCm training Docker](https://hub.docker.com/layers/rocm/pytorch-training/v25.5/images/sha256-d47850a9b25b4a7151f796a8d24d55ea17bba545573f0d50d54d3852f96ecde5)
(`rocm/pytorch-training:v25.5`

) image
provides a prebuilt optimized environment for fine-tuning and pretraining a
model on AMD Instinct MI325X and MI300X accelerators. It includes the following
software components to accelerate training workloads:

Software component |
Version |
|---|---|
ROCm |
6.3.4 |
PyTorch |
2.7.0a0+git637433 |
Python |
3.10 |
Transformer Engine |
1.12.0.dev0+25a33da |
Flash Attention |
3.0.0 |
hipBLASLt |
git53b53bf |
Triton |
3.2.0 |

## Supported models[#](#supported-models)

The following models are pre-optimized for performance on the AMD Instinct MI325X and MI300X accelerators.

Llama 3.3 70B

Llama 3.1 8B

Llama 3.1 70B

Llama 2 70B

FLUX.1-dev


Note

Only these models are supported in the following steps.

Some models, such as Llama 3, require an external license agreement through a third party (for example, Meta).

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

This Docker image is optimized for specific model configurations outlined below. Performance can vary for other training workloads, as AMD doesn’t validate configurations and run conditions outside those described.

## Benchmarking[#](#benchmarking)

Once the setup is complete, choose between two options to start benchmarking:

Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local
directory and install the required packages on the host machine.

```
clone https://github.com/ROCm/MAD
cd MAD
pip install -r requirements.txt
```

For example, use this command to run the performance benchmark test on the Llama 3.1 8B model using one GPU with the float16 data type on the host machine.

```
export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
python3 tools/run_models.py --tags pyt_train_llama-3.1-8b --keep-model-dir --live-output --timeout 28800
```

The available models for MAD-integrated benchmarking are:

`pyt_train_llama-3.3-70b`

`pyt_train_llama-3.1-8b`

`pyt_train_llama-3.1-70b`

`pyt_train_flux`


MAD launches a Docker container with the name
`container_ci-pyt_train_llama-3.1-8b`

, for example. The latency and throughput reports of the
model are collected in the following path: `~/MAD/perf.csv`

.

Download the Docker image and required packages

Use the following command to pull the Docker image from Docker Hub.

```
pull rocm/pytorch-training:v25.5
```

Run the Docker container.

```
run -it --device /dev/dri --device /dev/kfd --network host --ipc host --group-add video --cap-add SYS_PTRACE --security-opt seccomp=unconfined --privileged -v $HOME:$HOME -v $HOME/.ssh:/root/.ssh --shm-size 64G --name training_env rocm/pytorch-training:v25.5
```

Use these commands if you exit the `training_env`

container and need to return to it.

```
start training_env
docker exec -it training_env bash
```

In the Docker container, clone the [ROCm/MAD](https://github.com/ROCm/MAD)
repository and navigate to the benchmark scripts directory
`/workspace/MAD/scripts/pytorch_train`

.

```
clone https://github.com/ROCm/MAD
cd MAD/scripts/pytorch_train
```

Prepare training datasets and dependencies

The following benchmarking examples require downloading models and datasets
from Hugging Face. To ensure successful access to gated repos, set your
`HF_TOKEN`

.

```
export HF_TOKEN=$your_personal_hugging_face_access_token
```

Run the setup script to install libraries and datasets needed for benchmarking.


`pytorch_benchmark_setup.sh`

installs the following libraries:

Library |
Benchmark model |
Reference |
|---|---|---|
|
Llama 3.1 8B, FLUX |
|
|
Llama 3.1 8B, 70B, FLUX |
|
|
Llama 3.1 70B |
|
|
Llama 3.1 70B |
|
|
Llama 3.1 70B |
|
|
Llama 3.1 70B |
|
|
Llama 3.1 70B |
|
|
Llama 3.1 70B |
|
|
Llama 3.1 70B, FLUX |
|
|
Llama 3.1 70 B, FLUX |
|
|
FLUX |
|
|
FLUX |
|
|
FLUX |
|
|
FLUX |
|
|
FLUX |
|
|
FLUX |
|
|
FLUX |
|
|
FLUX |
|
|
FLUX |
|
|
FLUX |
|
|
FLUX |
|

`pytorch_benchmark_setup.sh`

downloads the following models from Hugging Face:

Along with the following datasets:

Pretraining

To start the pretraining benchmark, use the following command with the appropriate options. See the following list of options and their descriptions.

```
-t $training_mode -m $model_repo -p $datatype -s $sequence_length
```

Name |
Options |
Description |
|---|---|---|
|
|
Benchmark pretraining |
|
Benchmark full weight fine-tuning (Llama 3.1 70B with BF16) |
|
|
Benchmark LoRA fine-tuning (Llama 3.1 70B with BF16) |
|
|
Benchmark LoRA fine-tuning with Hugging Face PEFT (Llama 2 70B with BF16) |
|
|
|
Only Llama 3.1 8B supports FP8 precision. |
|
|
|
|
||
|
||
|
||
|
||
|
Sequence length for the language model. |
Between 2048 and 8192. 8192 by default. |

Note

Occasionally, downloading the Flux dataset might fail. In the event of this
error, manually download it from Hugging Face at
[black-forest-labs/FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev)
and save it to /workspace/FluxBenchmark. This ensures that the test script can access
the required dataset.

Fine-tuning

To start the fine-tuning benchmark, use the following command. It will run the benchmarking example of Llama 3.1 70B
with the WikiText dataset using the AMD fork of [torchtune](https://github.com/AMD-AIG-AIMA/torchtune).

```
-t {finetune_fw, finetune_lora} -p BF16 -m Llama-3.1-70B
```

Use the following command to run the benchmarking example of Llama 2 70B with the UltraChat 200k dataset using
[Hugging Face PEFT](https://huggingface.co/docs/peft/en/index).

```
-t HF_finetune_lora -p BF16 -m Llama-2-70B
```

Benchmarking examples

Here are some example commands to get started pretraining and fine-tuning with various model configurations.

Example 1: Llama 3.1 70B with BF16 precision with

[torchtitan](https://github.com/ROCm/torchtitan).-t pretrain -p BF16 -m Llama-3.1-70B -s 8192

Example 2: Llama 3.1 8B with FP8 precision using Transformer Engine (TE) and Hugging Face Accelerator.

-t pretrain -p FP8 -m Llama-3.1-70B -s 8192

Example 3: FLUX.1-dev with BF16 precision with FluxBenchmark.

-t pretrain -p BF16 -m Flux

Example 4: Torchtune full weight fine-tuning with Llama 3.1 70B

-t finetune_fw -p BF16 -m Llama-3.1-70B

Example 5: Torchtune LoRA fine-tuning with Llama 3.1 70B

-t finetune_lora -p BF16 -m Llama-3.1-70B

Example 6: Torchtune full weight fine-tuning with Llama-3.3-70B

-t finetune_fw -p BF16 -m Llama-3.3-70B

Example 7: Torchtune LoRA fine-tuning with Llama-3.3-70B

-t finetune_lora -p BF16 -m Llama-3.3-70B

Example 8: Torchtune QLoRA fine-tuning with Llama-3.3-70B

-t finetune_qlora -p BF16 -m Llama-3.3-70B

Example 9: Hugging Face PEFT LoRA fine-tuning with Llama 2 70B

-t HF_finetune_lora -p BF16 -m Llama-2-70B


## Previous versions[#](#previous-versions)

This table lists previous versions of the ROCm PyTorch training Docker image for training performance validation. For detailed information about available models for benchmarking, see the version-specific documentation.
