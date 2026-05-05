---
title: "Training a model with PyTorch for ROCm"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/training/benchmark-docker/previous-versions/pytorch-training-v25.4.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:01:35.457800+00:00
content_hash: "478222c0d8436470"
---

# Training a model with PyTorch for ROCm[#](#training-a-model-with-pytorch-for-rocm)

2026-04-21

9 min read time

Caution

This documentation does not reflect the latest version of ROCm PyTorch
training performance documentation. See [Training a model with PyTorch on ROCm](../pytorch-training.html) for the latest version.

PyTorch is an open-source machine learning framework that is widely used for model training with GPU-optimized components for transformer-based models.

The PyTorch for ROCm training Docker (`rocm/pytorch-training:v25.4`

) image
provides a prebuilt optimized environment for fine-tuning and pretraining a
model on AMD Instinct MI325X and MI300X GPUs. It includes the following
software components to accelerate training workloads:

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

## Supported models[#](#supported-models)

The following models are pre-optimized for performance on the AMD Instinct MI325X and MI300X GPUs.

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

## System validation[#](#system-validation)

If you have already validated your system settings, including NUMA
auto-balancing, skip this step. Otherwise, complete the [system validation
and optimization steps](../../../system-setup/prerequisite-system-validation.html#train-a-model-system-validation) to set up your system
before starting training.

## Environment setup[#](#environment-setup)

This Docker image is optimized for specific model configurations outlined below. Performance can vary for other training workloads, as AMD doesn’t validate configurations and run conditions outside those described.

### Download the Docker image[#](#download-the-docker-image)

Use the following command to pull the Docker image from Docker Hub.

pull rocm/pytorch-training:v25.4

Run the Docker container.

run -it --device /dev/dri --device /dev/kfd --network host --ipc host --group-add video --cap-add SYS_PTRACE --security-opt seccomp=unconfined --privileged -v $HOME:$HOME -v $HOME/.ssh:/root/.ssh --shm-size 64G --name training_env rocm/pytorch-training:v25.4

Use these commands if you exit the

`training_env`

container and need to return to it.start training_env docker exec -it training_env bash

In the Docker container, clone the

[ROCm/MAD](https://github.com/ROCm/MAD)repository and navigate to the benchmark scripts directory`/workspace/MAD/scripts/pytorch_train`

.clone https://github.com/ROCm/MAD cd MAD/scripts/pytorch_train


### Prepare training datasets and dependencies[#](#prepare-training-datasets-and-dependencies)

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

## Getting started[#](#getting-started)

The prebuilt PyTorch with ROCm training environment allows users to quickly validate system performance, conduct training benchmarks, and achieve superior performance for models like Llama 3.1 and Llama 2. This container should not be expected to provide generalized performance across all training workloads. You can expect the container to perform in the model configurations described in the following section, but other configurations are not validated by AMD.

Use the following instructions to set up the environment, configure the script to train models, and reproduce the benchmark results on MI325X and MI300X GPUs with the AMD PyTorch training Docker image.

Once your environment is set up, use the following commands and examples to start benchmarking.

### Pretraining[#](#pretraining)

To start the pretraining benchmark, use the following command with the appropriate options. See the following list of options and their descriptions.

```
-t $training_mode -m $model_repo -p $datatype -s $sequence_length
```

#### Options and available models[#](#options-and-available-models)

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
Sequence length for the language model. |
Between 2048 and 8192. 8192 by default. |

Note

Occasionally, downloading the Flux dataset might fail. In the event of this
error, manually download it from Hugging Face at
[black-forest-labs/FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev)
and save it to /workspace/FluxBenchmark. This ensures that the test script can access
the required dataset.

### Fine-tuning[#](#fine-tuning)

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

### Benchmarking examples[#](#benchmarking-examples)

Here are some examples of how to use the command.

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

Example 6: Hugging Face PEFT LoRA fine-tuning with Llama 2 70B

-t HF_finetune_lora -p BF16 -m Llama-2-70B


## Previous versions[#](#previous-versions)

See [PyTorch training performance testing version history](pytorch-training-history.html) to find documentation for previous releases
of the `ROCm/pytorch-training`

Docker image.
