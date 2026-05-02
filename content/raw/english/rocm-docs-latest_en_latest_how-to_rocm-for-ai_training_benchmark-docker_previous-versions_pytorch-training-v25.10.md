---
title: "Training a model with PyTorch on ROCm"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/training/benchmark-docker/previous-versions/pytorch-training-v25.10.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T12:03:13.405138+00:00
content_hash: "1c70cd2f59e4bee4"
---

# Training a model with PyTorch on ROCm[#](#training-a-model-with-pytorch-on-rocm)

2026-04-21

43 min read time

Caution

This documentation does not reflect the latest version of ROCm PyTorch training
performance benchmark documentation. See [Training a model with PyTorch on ROCm](../pytorch-training.html) for the latest version.

Note

For a unified training solution on AMD GPUs with ROCm, the [rocm/pytorch-training](https://hub.docker.com/r/rocm/pytorch-training/) Docker Hub registry will be
deprecated soon in favor of [rocm/primus](https://hub.docker.com/r/rocm/primus).
The `rocm/primus`

Docker containers will cover PyTorch training ecosystem frameworks,
including torchtitan and [Megatron-LM](../primus-megatron.html).

See [Training a model with Primus and PyTorch](../primus-pytorch.html) for details.

PyTorch is an open-source machine learning framework that is widely used for model training with GPU-optimized components for transformer-based models. The PyTorch for ROCm training Docker image provides a prebuilt optimized environment for fine-tuning and pretraining a model on AMD Instinct MI325X and MI300X GPUs. It includes the following software components to accelerate training workloads:

Software component |
Version |
|---|---|
ROCm |
7.1.0 |
Primus |
0.3.0 |
Primus Turbo |
0.1.1 |
PyTorch |
2.10.0.dev20251112+rocm7.1 |
Python |
3.10 |
Transformer Engine |
2.4.0.dev0+32e2d1d4 |
Flash Attention |
2.8.3 |
hipBLASLt |
1.2.0-09ab7153e2 |

## Supported models[#](#supported-models)

The following models are pre-optimized for performance on the AMD Instinct MI355X, MI350X, MI325X, and MI300X GPUs. Some instructions, commands, and training recommendations in this documentation might vary by model – select one to get started.

The following table lists supported training modes per model.

## Supported training modes

Model |
Supported training modes |
|---|---|
Llama 4 Scout 17B-16E |
|
Llama 3.3 70B |
|
Llama 3.2 1B |
|
Llama 3.2 3B |
|
Llama 3.2 Vision 11B |
|
Llama 3.2 Vision 90B |
|
Llama 3.1 8B |
|
Llama 3.1 70B |
|
Llama 3.1 405B |
|
Llama 3 8B |
|
Llama 3 70B |
|
Llama 2 7B |
|
Llama 2 13B |
|
Llama 2 70B |
|
GPT OSS 20B |
|
GPT OSS 120B |
|
DeepSeek V2 16B |
|
Qwen 3 8B |
|
Qwen 3 32B |
|
Qwen 2.5 32B |
|
Qwen 2.5 72B |
|
Qwen 2 1.5B |
|
Qwen 2 7B |
|
Stable Diffusion XL |
|
FLUX.1-dev |
|
DLRM v2 |
|

Note

Some model and fine-tuning combinations are not listed. This is
because the [upstream torchtune repository](https://github.com/pytorch/torchtune)
doesn’t provide default YAML configurations for them.
For advanced usage, you can create a custom configuration to enable
unlisted fine-tuning methods by using an existing file in the
`/workspace/torchtune/recipes/configs`

directory as a template.

## Performance measurements[#](#performance-measurements)

To evaluate performance, the
[Performance results with AMD ROCm software](https://www.amd.com/en/developer/resources/rocm-hub/dev-ai/performance-results.html#tabs-a8deaeb413-item-21cea50186-tab)
page provides reference throughput and latency measurements for training
popular AI models.

## System validation[#](#system-validation)

Before running AI workloads, it’s important to validate that your AMD hardware is configured correctly and performing optimally.

If you have already validated your system settings, including aspects like NUMA auto-balancing, you
can skip this step. Otherwise, complete the procedures in the [System validation and
optimization](../../../system-setup/prerequisite-system-validation.html#rocm-for-ai-system-optimization) guide to properly configure your system settings
before starting training.

To test for optimal performance, consult the recommended [System health benchmarks](../../../system-setup/system-health-check.html#rocm-for-ai-system-health-bench). This suite of tests will help you verify and fine-tune your
system’s configuration.

This Docker image is optimized for specific model configurations outlined below. Performance can vary for other training workloads, as AMD doesn’t test configurations and run conditions outside those described.

## Run training[#](#run-training)

Once the setup is complete, choose between two options to start benchmarking training:

The following run command is tailored to Llama 4 Scout 17B-16E.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

For example, use this command to run the performance benchmark test on the Llama 4 Scout 17B-16E model using one node with the BF16 data type on the host machine.

export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_train_llama-4-scout-17b-16e \ --keep-model-dir \ --live-output \ --timeout 28800

MAD launches a Docker container with the name

`container_ci-pyt_train_llama-4-scout-17b-16e`

. The latency and throughput reports of the model are collected in`~/MAD/perf.csv`

.

The following run command is tailored to Llama 3.3 70B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

For example, use this command to run the performance benchmark test on the Llama 3.3 70B model using one node with the BF16 data type on the host machine.

export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_train_llama-3.3-70b \ --keep-model-dir \ --live-output \ --timeout 28800

MAD launches a Docker container with the name

`container_ci-pyt_train_llama-3.3-70b`

. The latency and throughput reports of the model are collected in`~/MAD/perf.csv`

.

The following run command is tailored to Llama 3.2 1B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

For example, use this command to run the performance benchmark test on the Llama 3.2 1B model using one node with the BF16 data type on the host machine.

export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_train_llama-3.2-1b \ --keep-model-dir \ --live-output \ --timeout 28800

MAD launches a Docker container with the name

`container_ci-pyt_train_llama-3.2-1b`

. The latency and throughput reports of the model are collected in`~/MAD/perf.csv`

.

The following run command is tailored to Llama 3.2 3B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

For example, use this command to run the performance benchmark test on the Llama 3.2 3B model using one node with the BF16 data type on the host machine.

export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_train_llama-3.2-3b \ --keep-model-dir \ --live-output \ --timeout 28800

MAD launches a Docker container with the name

`container_ci-pyt_train_llama-3.2-3b`

. The latency and throughput reports of the model are collected in`~/MAD/perf.csv`

.

The following run command is tailored to Llama 3.2 Vision 11B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

For example, use this command to run the performance benchmark test on the Llama 3.2 Vision 11B model using one node with the BF16 data type on the host machine.

export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_train_llama-3.2-vision-11b \ --keep-model-dir \ --live-output \ --timeout 28800

MAD launches a Docker container with the name

`container_ci-pyt_train_llama-3.2-vision-11b`

. The latency and throughput reports of the model are collected in`~/MAD/perf.csv`

.

The following run command is tailored to Llama 3.2 Vision 90B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

For example, use this command to run the performance benchmark test on the Llama 3.2 Vision 90B model using one node with the BF16 data type on the host machine.

export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_train_llama-3.2-vision-90b \ --keep-model-dir \ --live-output \ --timeout 28800

MAD launches a Docker container with the name

`container_ci-pyt_train_llama-3.2-vision-90b`

. The latency and throughput reports of the model are collected in`~/MAD/perf.csv`

.

The following run command is tailored to Llama 3.1 8B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

For example, use this command to run the performance benchmark test on the Llama 3.1 8B model using one node with the BF16 data type on the host machine.

export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_train_llama-3.1-8b \ --keep-model-dir \ --live-output \ --timeout 28800

MAD launches a Docker container with the name

`container_ci-pyt_train_llama-3.1-8b`

. The latency and throughput reports of the model are collected in`~/MAD/perf.csv`

.

The following run command is tailored to Llama 3.1 70B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

For example, use this command to run the performance benchmark test on the Llama 3.1 70B model using one node with the BF16 data type on the host machine.

export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_train_llama-3.1-70b \ --keep-model-dir \ --live-output \ --timeout 28800

MAD launches a Docker container with the name

`container_ci-pyt_train_llama-3.1-70b`

. The latency and throughput reports of the model are collected in`~/MAD/perf.csv`

.

The following run command is tailored to Llama 3.1 405B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

For example, use this command to run the performance benchmark test on the Llama 3.1 405B model using one node with the BF16 data type on the host machine.

export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_train_llama-3.1-405b \ --keep-model-dir \ --live-output \ --timeout 28800

MAD launches a Docker container with the name

`container_ci-pyt_train_llama-3.1-405b`

. The latency and throughput reports of the model are collected in`~/MAD/perf.csv`

.

The following run command is tailored to Llama 3 8B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

For example, use this command to run the performance benchmark test on the Llama 3 8B model using one node with the BF16 data type on the host machine.

export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_train_llama-3-8b \ --keep-model-dir \ --live-output \ --timeout 28800

MAD launches a Docker container with the name

`container_ci-pyt_train_llama-3-8b`

. The latency and throughput reports of the model are collected in`~/MAD/perf.csv`

.

The following run command is tailored to Llama 3 70B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

For example, use this command to run the performance benchmark test on the Llama 3 70B model using one node with the BF16 data type on the host machine.

export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_train_llama-3-70b \ --keep-model-dir \ --live-output \ --timeout 28800

MAD launches a Docker container with the name

`container_ci-pyt_train_llama-3-70b`

. The latency and throughput reports of the model are collected in`~/MAD/perf.csv`

.

The following run command is tailored to Llama 2 7B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

For example, use this command to run the performance benchmark test on the Llama 2 7B model using one node with the BF16 data type on the host machine.

export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_train_llama-2-7b \ --keep-model-dir \ --live-output \ --timeout 28800

MAD launches a Docker container with the name

`container_ci-pyt_train_llama-2-7b`

. The latency and throughput reports of the model are collected in`~/MAD/perf.csv`

.

The following run command is tailored to Llama 2 13B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

For example, use this command to run the performance benchmark test on the Llama 2 13B model using one node with the BF16 data type on the host machine.

export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_train_llama-2-13b \ --keep-model-dir \ --live-output \ --timeout 28800

MAD launches a Docker container with the name

`container_ci-pyt_train_llama-2-13b`

. The latency and throughput reports of the model are collected in`~/MAD/perf.csv`

.

The following run command is tailored to Llama 2 70B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

For example, use this command to run the performance benchmark test on the Llama 2 70B model using one node with the BF16 data type on the host machine.

export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_train_llama-2-70b \ --keep-model-dir \ --live-output \ --timeout 28800

MAD launches a Docker container with the name

`container_ci-pyt_train_llama-2-70b`

. The latency and throughput reports of the model are collected in`~/MAD/perf.csv`

.

The following run command is tailored to GPT OSS 20B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

For example, use this command to run the performance benchmark test on the GPT OSS 20B model using one node with the BF16 data type on the host machine.

export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_train_gpt_oss_20b \ --keep-model-dir \ --live-output \ --timeout 28800

MAD launches a Docker container with the name

`container_ci-pyt_train_gpt_oss_20b`

. The latency and throughput reports of the model are collected in`~/MAD/perf.csv`

.

The following run command is tailored to GPT OSS 120B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

For example, use this command to run the performance benchmark test on the GPT OSS 120B model using one node with the BF16 data type on the host machine.

export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_train_gpt_oss_120b \ --keep-model-dir \ --live-output \ --timeout 28800

MAD launches a Docker container with the name

`container_ci-pyt_train_gpt_oss_120b`

. The latency and throughput reports of the model are collected in`~/MAD/perf.csv`

.

The following run command is tailored to DeepSeek V2 16B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

For example, use this command to run the performance benchmark test on the DeepSeek V2 16B model using one node with the BF16 data type on the host machine.

export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags primus_pyt_train_deepseek-v2 \ --keep-model-dir \ --live-output \ --timeout 28800

MAD launches a Docker container with the name

`container_ci-primus_pyt_train_deepseek-v2`

. The latency and throughput reports of the model are collected in`~/MAD/perf.csv`

.

The following run command is tailored to Qwen 3 8B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

For example, use this command to run the performance benchmark test on the Qwen 3 8B model using one node with the BF16 data type on the host machine.

export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_train_qwen3-8b \ --keep-model-dir \ --live-output \ --timeout 28800

MAD launches a Docker container with the name

`container_ci-pyt_train_qwen3-8b`

. The latency and throughput reports of the model are collected in`~/MAD/perf.csv`

.

The following run command is tailored to Qwen 3 32B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

For example, use this command to run the performance benchmark test on the Qwen 3 32B model using one node with the BF16 data type on the host machine.

export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_train_qwen3-32b \ --keep-model-dir \ --live-output \ --timeout 28800

MAD launches a Docker container with the name

`container_ci-pyt_train_qwen3-32b`

. The latency and throughput reports of the model are collected in`~/MAD/perf.csv`

.

The following run command is tailored to Qwen 2.5 32B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

For example, use this command to run the performance benchmark test on the Qwen 2.5 32B model using one node with the BF16 data type on the host machine.

export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_train_qwen2.5-32b \ --keep-model-dir \ --live-output \ --timeout 28800

MAD launches a Docker container with the name

`container_ci-pyt_train_qwen2.5-32b`

. The latency and throughput reports of the model are collected in`~/MAD/perf.csv`

.

The following run command is tailored to Qwen 2.5 72B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

For example, use this command to run the performance benchmark test on the Qwen 2.5 72B model using one node with the BF16 data type on the host machine.

export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_train_qwen2.5-72b \ --keep-model-dir \ --live-output \ --timeout 28800

MAD launches a Docker container with the name

`container_ci-pyt_train_qwen2.5-72b`

. The latency and throughput reports of the model are collected in`~/MAD/perf.csv`

.

The following run command is tailored to Qwen 2 1.5B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

For example, use this command to run the performance benchmark test on the Qwen 2 1.5B model using one node with the BF16 data type on the host machine.

export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_train_qwen2-1.5b \ --keep-model-dir \ --live-output \ --timeout 28800

MAD launches a Docker container with the name

`container_ci-pyt_train_qwen2-1.5b`

. The latency and throughput reports of the model are collected in`~/MAD/perf.csv`

.

The following run command is tailored to Qwen 2 7B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

For example, use this command to run the performance benchmark test on the Qwen 2 7B model using one node with the BF16 data type on the host machine.

export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_train_qwen2-7b \ --keep-model-dir \ --live-output \ --timeout 28800

MAD launches a Docker container with the name

`container_ci-pyt_train_qwen2-7b`

. The latency and throughput reports of the model are collected in`~/MAD/perf.csv`

.

The following run command is tailored to Stable Diffusion XL.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

For example, use this command to run the performance benchmark test on the Stable Diffusion XL model using one node with the BF16 data type on the host machine.

export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_huggingface_stable_diffusion_xl_2k_lora_finetuning \ --keep-model-dir \ --live-output \ --timeout 28800

MAD launches a Docker container with the name

`container_ci-pyt_huggingface_stable_diffusion_xl_2k_lora_finetuning`

. The latency and throughput reports of the model are collected in`~/MAD/perf.csv`

.

The following run command is tailored to FLUX.1-dev.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

For example, use this command to run the performance benchmark test on the FLUX.1-dev model using one node with the BF16 data type on the host machine.

export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_train_flux \ --keep-model-dir \ --live-output \ --timeout 28800

MAD launches a Docker container with the name

`container_ci-pyt_train_flux`

. The latency and throughput reports of the model are collected in`~/MAD/perf.csv`

.

The following run command is tailored to NCF.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

For example, use this command to run the performance benchmark test on the NCF model using one node with the FP32 data type on the host machine.

export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_ncf_training \ --keep-model-dir \ --live-output \ --timeout 28800

MAD launches a Docker container with the name

`container_ci-pyt_ncf_training`

. The latency and throughput reports of the model are collected in`~/MAD/perf.csv`

.

The following run command is tailored to DLRM v2.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

For example, use this command to run the performance benchmark test on the DLRM v2 model using one node with the data type on the host machine.

export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_train_dlrm \ --keep-model-dir \ --live-output \ --timeout 28800

MAD launches a Docker container with the name

`container_ci-pyt_train_dlrm`

. The latency and throughput reports of the model are collected in`~/MAD/perf.csv`

.

The following commands are tailored to Llama 4 Scout 17B-16E.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

The following commands are tailored to Llama 3.3 70B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

The following commands are tailored to Llama 3.2 1B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

The following commands are tailored to Llama 3.2 3B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

The following commands are tailored to Llama 3.2 Vision 11B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

The following commands are tailored to Llama 3.2 Vision 90B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

The following commands are tailored to Llama 3.1 8B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

The following commands are tailored to Llama 3.1 70B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

The following commands are tailored to Llama 3.1 405B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

The following commands are tailored to Llama 3 8B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

The following commands are tailored to Llama 3 70B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

The following commands are tailored to Llama 2 7B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

The following commands are tailored to Llama 2 13B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

The following commands are tailored to Llama 2 70B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

The following commands are tailored to GPT OSS 20B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

The following commands are tailored to GPT OSS 120B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

The following commands are tailored to DeepSeek V2 16B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

The following commands are tailored to Qwen 3 8B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

The following commands are tailored to Qwen 3 32B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

The following commands are tailored to Qwen 2.5 32B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

The following commands are tailored to Qwen 2.5 72B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

The following commands are tailored to Qwen 2 1.5B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

The following commands are tailored to Qwen 2 7B.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

The following commands are tailored to Stable Diffusion XL.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

The following commands are tailored to FLUX.1-dev.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

The following commands are tailored to NCF.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

The following commands are tailored to DLRM v2.
See [Supported models](#amd-pytorch-training-model-support-v2510) to switch to another available model.

Download the Docker image and required packages

Use the following command to pull the Docker image from Docker Hub.

pull rocm/primus:v25.10

Launch the Docker container.

run -it \ --device /dev/dri \ --device /dev/kfd \ --network host \ --ipc host \ --group-add video \ --cap-add SYS_PTRACE \ --security-opt seccomp=unconfined \ --privileged \ -v $HOME:$HOME \ -v $HOME/.ssh:/root/.ssh \ --shm-size 64G \ --name training_env \ rocm/primus:v25.10

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

`pytorch_benchmark_setup.sh`

installs the following libraries for Llama 3.1 8B:`pytorch_benchmark_setup.sh`

installs the following libraries for Llama 3.1 70B:`pytorch_benchmark_setup.sh`

installs the following libraries for FLUX:Library

Reference

`accelerate`

`datasets`

[Hugging Face Datasets](https://huggingface.co/docs/datasets/v3.2.0/en/index)3.2.0`sentencepiece`

[SentencePiece](https://github.com/google/sentencepiece)0.2.0`tensorboard`

[TensorBoard](https://www.tensorflow.org/tensorboard)2.18.0`csvkit`

[csvkit](https://csvkit.readthedocs.io/en/latest/)2.0.1`deepspeed`

[DeepSpeed](https://github.com/deepspeedai/DeepSpeed)0.16.2`diffusers`

[Hugging Face Diffusers](https://huggingface.co/docs/diffusers/en/index)0.31.0`GitPython`

[GitPython](https://github.com/gitpython-developers/GitPython)3.1.44`opencv-python-headless`

[opencv-python-headless](https://pypi.org/project/opencv-python-headless/)4.10.0.84`peft`

[PEFT](https://huggingface.co/docs/peft/en/index)0.14.0`protobuf`

[Protocol Buffers](https://github.com/protocolbuffers/protobuf)5.29.2`pytest`

[PyTest](https://docs.pytest.org/en/stable/)8.3.4`python-dotenv`

[python-dotenv](https://pypi.org/project/python-dotenv/)1.0.1`seaborn`

[Seaborn](https://seaborn.pydata.org/)0.13.2`transformers`

[Transformers](https://huggingface.co/docs/transformers/en/index)4.47.0`pytorch_benchmark_setup.sh`

downloads the following datasets from Hugging Face:

Fine-tuning

To start the fine-tuning benchmark, use the following command with the
appropriate options. See the following list of options and their descriptions.
See [supported training modes](#amd-pytorch-training-supported-training-modes-v2510).

```
-t $training_mode \
-m Llama-4-17B_16E \
-p $datatype \
-s $sequence_length
```

Name |
Options |
Description |
|---|---|---|
|
|
Full weight fine-tuning (BF16 and FP8 supported). |
|
LoRA fine-tuning (BF16 supported). |
|
|
|
All models support BF16. FP8 is only available for full weight fine-tuning. |
|
Between 2048 and 16384. |
Sequence length for the language model. |

Fine-tuning

To start the fine-tuning benchmark, use the following command with the
appropriate options. See the following list of options and their descriptions.
See [supported training modes](#amd-pytorch-training-supported-training-modes-v2510).

```
-t $training_mode \
-m Llama-3.3-70B \
-p $datatype \
-s $sequence_length
```

Name |
Options |
Description |
|---|---|---|
|
|
Full weight fine-tuning (BF16 and FP8 supported). |
|
LoRA fine-tuning (BF16 supported). |
|
|
QLoRA fine-tuning (BF16 supported). |
|
|
|
All models support BF16. FP8 is only available for full weight fine-tuning. |
|
Between 2048 and 16384. |
Sequence length for the language model. |

Fine-tuning

To start the fine-tuning benchmark, use the following command with the
appropriate options. See the following list of options and their descriptions.
See [supported training modes](#amd-pytorch-training-supported-training-modes-v2510).

```
-t $training_mode \
-m Llama-3.2-1B \
-p $datatype \
-s $sequence_length
```

Name |
Options |
Description |
|---|---|---|
|
|
Full weight fine-tuning (BF16 and FP8 supported). |
|
LoRA fine-tuning (BF16 supported). |
|
|
|
All models support BF16. FP8 is only available for full weight fine-tuning. |
|
Between 2048 and 16384. |
Sequence length for the language model. |

Fine-tuning

To start the fine-tuning benchmark, use the following command with the
appropriate options. See the following list of options and their descriptions.
See [supported training modes](#amd-pytorch-training-supported-training-modes-v2510).

```
-t $training_mode \
-m Llama-3.2-3B \
-p $datatype \
-s $sequence_length
```

Name |
Options |
Description |
|---|---|---|
|
|
Full weight fine-tuning (BF16 and FP8 supported). |
|
LoRA fine-tuning (BF16 supported). |
|
|
|
All models support BF16. FP8 is only available for full weight fine-tuning. |
|
Between 2048 and 16384. |
Sequence length for the language model. |

Fine-tuning

To start the fine-tuning benchmark, use the following command with the
appropriate options. See the following list of options and their descriptions.
See [supported training modes](#amd-pytorch-training-supported-training-modes-v2510).

```
-t $training_mode \
-m Llama-3.2-Vision-11B \
-p $datatype \
-s $sequence_length
```

Name |
Options |
Description |
|---|---|---|
|
|
Full weight fine-tuning (BF16 and FP8 supported). |
|
|
All models support BF16. FP8 is only available for full weight fine-tuning. |
|
Between 2048 and 16384. |
Sequence length for the language model. |

Fine-tuning

To start the fine-tuning benchmark, use the following command with the
appropriate options. See the following list of options and their descriptions.
See [supported training modes](#amd-pytorch-training-supported-training-modes-v2510).

```
-t $training_mode \
-m Llama-3.2-Vision-90B \
-p $datatype \
-s $sequence_length
```

Name |
Options |
Description |
|---|---|---|
|
|
Full weight fine-tuning (BF16 and FP8 supported). |
|
|
All models support BF16. FP8 is only available for full weight fine-tuning. |
|
Between 2048 and 16384. |
Sequence length for the language model. |

Note

For LoRA and QLoRA support with vision models (Llama 3.2 11B and 90B), use the following torchtune commit for compatibility:

```
checkout 48192e23188b1fc524dd6d127725ceb2348e7f0e
```

Pretraining

To start the pre-training benchmark, use the following command with the appropriate options. See the following list of options and their descriptions.

```
-t $training_mode \
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
Benchmark pre-training. |
|
Llama 3.1 8B pre-training with FP8 precision. |
|
|
|
Only Llama 3.1 8B supports FP8 precision. |
|
Sequence length for the language model. |
Between 2048 and 8192. 8192 by default. |

Fine-tuning

To start the fine-tuning benchmark, use the following command with the
appropriate options. See the following list of options and their descriptions.
See [supported training modes](#amd-pytorch-training-supported-training-modes-v2510).

```
-t $training_mode \
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
Full weight fine-tuning (BF16 and FP8 supported). |
|
LoRA fine-tuning (BF16 supported). |
|
|
|
All models support BF16. FP8 is only available for full weight fine-tuning. |
|
Between 2048 and 16384. |
Sequence length for the language model. |

Pretraining

To start the pre-training benchmark, use the following command with the appropriate options. See the following list of options and their descriptions.

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
Benchmark pre-training. |
|
|
Only Llama 3.1 8B supports FP8 precision. |
|
Sequence length for the language model. |
Between 2048 and 8192. 8192 by default. |

Fine-tuning

To start the fine-tuning benchmark, use the following command with the
appropriate options. See the following list of options and their descriptions.
See [supported training modes](#amd-pytorch-training-supported-training-modes-v2510).

```
-t $training_mode \
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
Full weight fine-tuning (BF16 and FP8 supported). |
|
LoRA fine-tuning (BF16 supported). |
|
|
|
All models support BF16. FP8 is only available for full weight fine-tuning. |
|
Between 2048 and 16384. |
Sequence length for the language model. |

Fine-tuning

To start the fine-tuning benchmark, use the following command with the
appropriate options. See the following list of options and their descriptions.
See [supported training modes](#amd-pytorch-training-supported-training-modes-v2510).

```
-t $training_mode \
-m Llama-3.1-405B \
-p $datatype \
-s $sequence_length
```

Name |
Options |
Description |
|---|---|---|
|
|
QLoRA fine-tuning (BF16 supported). |
|
|
All models support BF16. |
|
Between 2048 and 16384. |
Sequence length for the language model. |

Fine-tuning

To start the fine-tuning benchmark, use the following command with the
appropriate options. See the following list of options and their descriptions.
See [supported training modes](#amd-pytorch-training-supported-training-modes-v2510).

```
-t $training_mode \
-m Llama-3-8B \
-p $datatype \
-s $sequence_length
```

Name |
Options |
Description |
|---|---|---|
|
|
Full weight fine-tuning (BF16 and FP8 supported). |
|
LoRA fine-tuning (BF16 supported). |
|
|
|
All models support BF16. FP8 is only available for full weight fine-tuning. |
|
Between 2048 and 16384. |
Sequence length for the language model. |

Fine-tuning

To start the fine-tuning benchmark, use the following command with the
appropriate options. See the following list of options and their descriptions.
See [supported training modes](#amd-pytorch-training-supported-training-modes-v2510).

```
-t $training_mode \
-m Llama-3-70B \
-p $datatype \
-s $sequence_length
```

Name |
Options |
Description |
|---|---|---|
|
|
Full weight fine-tuning (BF16 and FP8 supported). |
|
LoRA fine-tuning (BF16 supported). |
|
|
|
All models support BF16. FP8 is only available for full weight fine-tuning. |
|
Between 2048 and 16384. |
Sequence length for the language model. |

Fine-tuning

To start the fine-tuning benchmark, use the following command with the
appropriate options. See the following list of options and their descriptions.
See [supported training modes](#amd-pytorch-training-supported-training-modes-v2510).

```
-t $training_mode \
-m Llama-2-7B \
-p $datatype \
-s $sequence_length
```

Name |
Options |
Description |
|---|---|---|
|
|
Full weight fine-tuning (BF16 and FP8 supported). |
|
LoRA fine-tuning (BF16 supported). |
|
|
QLoRA fine-tuning (BF16 supported). |
|
|
|
All models support BF16. FP8 is only available for full weight fine-tuning. |
|
Between 2048 and 16384. |
Sequence length for the language model. |

Note

You might encounter the following error with Llama 2: ```
ValueError: seq_len (16384) of
input tensor should be smaller than max_seq_len (4096)
```

.
This error indicates that an input sequence is longer than the model’s maximum context window.

Ensure your tokenized input does not exceed the model’s `max_seq_len`

(4096
tokens in this case). You can resolve this by truncating the input or splitting
it into smaller chunks before passing it to the model.

Note on reproducibility: The results in this guide are based on
commit `b4c98ac`

from the upstream
[pytorch/torchtune](https://github.com/pytorch/torchtune) repository. For the
latest updates, you can use the main branch.

Fine-tuning

To start the fine-tuning benchmark, use the following command with the
appropriate options. See the following list of options and their descriptions.
See [supported training modes](#amd-pytorch-training-supported-training-modes-v2510).

```
-t $training_mode \
-m Llama-2-13B \
-p $datatype \
-s $sequence_length
```

Name |
Options |
Description |
|---|---|---|
|
|
Full weight fine-tuning (BF16 and FP8 supported). |
|
LoRA fine-tuning (BF16 supported). |
|
|
|
All models support BF16. FP8 is only available for full weight fine-tuning. |
|
Between 2048 and 16384. |
Sequence length for the language model. |

Note

You might encounter the following error with Llama 2: ```
ValueError: seq_len (16384) of
input tensor should be smaller than max_seq_len (4096)
```

.
This error indicates that an input sequence is longer than the model’s maximum context window.

Ensure your tokenized input does not exceed the model’s `max_seq_len`

(4096
tokens in this case). You can resolve this by truncating the input or splitting
it into smaller chunks before passing it to the model.

Note on reproducibility: The results in this guide are based on
commit `b4c98ac`

from the upstream
[pytorch/torchtune](https://github.com/pytorch/torchtune) repository. For the
latest updates, you can use the main branch.

Fine-tuning

To start the fine-tuning benchmark, use the following command with the
appropriate options. See the following list of options and their descriptions.
See [supported training modes](#amd-pytorch-training-supported-training-modes-v2510).

```
-t $training_mode \
-m Llama-2-70B \
-p $datatype \
-s $sequence_length
```

Name |
Options |
Description |
|---|---|---|
|
|
LoRA fine-tuning (BF16 supported). |
|
QLoRA fine-tuning (BF16 supported). |
|
|
|
All models support BF16. |
|
Between 2048 and 16384. |
Sequence length for the language model. |

Note

You might encounter the following error with Llama 2: ```
ValueError: seq_len (16384) of
input tensor should be smaller than max_seq_len (4096)
```

.
This error indicates that an input sequence is longer than the model’s maximum context window.

Ensure your tokenized input does not exceed the model’s `max_seq_len`

(4096
tokens in this case). You can resolve this by truncating the input or splitting
it into smaller chunks before passing it to the model.

Note on reproducibility: The results in this guide are based on
commit `b4c98ac`

from the upstream
[pytorch/torchtune](https://github.com/pytorch/torchtune) repository. For the
latest updates, you can use the main branch.

Fine-tuning

To start the fine-tuning benchmark, use the following command with the
appropriate options. See the following list of options and their descriptions.
See [supported training modes](#amd-pytorch-training-supported-training-modes-v2510).

```
-t $training_mode \
-m GPT-OSS-20B \
-p $datatype \
-s $sequence_length
```

Name |
Options |
Description |
|---|---|---|
|
|
LoRA fine-tuning with Hugging Face PEFT. |
|
|
All models support BF16. |
|
Between 2048 and 16384. |
Sequence length for the language model. |

Fine-tuning

To start the fine-tuning benchmark, use the following command with the
appropriate options. See the following list of options and their descriptions.
See [supported training modes](#amd-pytorch-training-supported-training-modes-v2510).

```
-t $training_mode \
-m GPT-OSS-120B \
-p $datatype \
-s $sequence_length
```

Name |
Options |
Description |
|---|---|---|
|
|
LoRA fine-tuning with Hugging Face PEFT. |
|
|
All models support BF16. |
|
Between 2048 and 16384. |
Sequence length for the language model. |

Pretraining

To start the pre-training benchmark, use the following command with the appropriate options. See the following list of options and their descriptions.

```
-t pretrain \
-m DeepSeek-V2 \
-p $datatype \
-s $sequence_length
```

Name |
Options |
Description |
|---|---|---|
|
|
Benchmark pre-training. |
|
|
Only Llama 3.1 8B supports FP8 precision. |
|
Sequence length for the language model. |
Between 2048 and 8192. 8192 by default. |

Fine-tuning

To start the fine-tuning benchmark, use the following command with the
appropriate options. See the following list of options and their descriptions.
See [supported training modes](#amd-pytorch-training-supported-training-modes-v2510).

```
-t $training_mode \
-m Qwen3-8B \
-p $datatype \
-s $sequence_length
```

Name |
Options |
Description |
|---|---|---|
|
|
Full weight fine-tuning (BF16 and FP8 supported). |
|
LoRA fine-tuning (BF16 supported). |
|
|
|
All models support BF16. FP8 is only available for full weight fine-tuning. |
|
Between 2048 and 16384. |
Sequence length for the language model. |

Fine-tuning

To start the fine-tuning benchmark, use the following command with the
appropriate options. See the following list of options and their descriptions.
See [supported training modes](#amd-pytorch-training-supported-training-modes-v2510).

```
-t $training_mode \
-m Qwen3-32 \
-p $datatype \
-s $sequence_length
```

Name |
Options |
Description |
|---|---|---|
|
|
LoRA fine-tuning (BF16 supported). |
|
|
All models support BF16. |
|
Between 2048 and 16384. |
Sequence length for the language model. |

Fine-tuning

To start the fine-tuning benchmark, use the following command with the
appropriate options. See the following list of options and their descriptions.
See [supported training modes](#amd-pytorch-training-supported-training-modes-v2510).

```
-t $training_mode \
-m Qwen2.5-32B \
-p $datatype \
-s $sequence_length
```

Name |
Options |
Description |
|---|---|---|
|
|
LoRA fine-tuning (BF16 supported). |
|
|
All models support BF16. |
|
Between 2048 and 16384. |
Sequence length for the language model. |

Fine-tuning

To start the fine-tuning benchmark, use the following command with the
appropriate options. See the following list of options and their descriptions.
See [supported training modes](#amd-pytorch-training-supported-training-modes-v2510).

```
-t $training_mode \
-m Qwen2.5-72B \
-p $datatype \
-s $sequence_length
```

Name |
Options |
Description |
|---|---|---|
|
|
LoRA fine-tuning (BF16 supported). |
|
|
All models support BF16. |
|
Between 2048 and 16384. |
Sequence length for the language model. |

Fine-tuning

To start the fine-tuning benchmark, use the following command with the
appropriate options. See the following list of options and their descriptions.
See [supported training modes](#amd-pytorch-training-supported-training-modes-v2510).

```
-t $training_mode \
-m Qwen2-1.5B \
-p $datatype \
-s $sequence_length
```

Name |
Options |
Description |
|---|---|---|
|
|
Full weight fine-tuning (BF16 and FP8 supported). |
|
LoRA fine-tuning (BF16 supported). |
|
|
|
All models support BF16. FP8 is only available for full weight fine-tuning. |
|
Between 2048 and 16384. |
Sequence length for the language model. |

Fine-tuning

To start the fine-tuning benchmark, use the following command with the
appropriate options. See the following list of options and their descriptions.
See [supported training modes](#amd-pytorch-training-supported-training-modes-v2510).

```
-t $training_mode \
-m Qwen2-7B \
-p $datatype \
-s $sequence_length
```

Name |
Options |
Description |
|---|---|---|
|
|
Full weight fine-tuning (BF16 and FP8 supported). |
|
LoRA fine-tuning (BF16 supported). |
|
|
|
All models support BF16. FP8 is only available for full weight fine-tuning. |
|
Between 2048 and 16384. |
Sequence length for the language model. |

Post-training

To start the post-training benchmark, use the following command with the appropriate options. See the following list of options and their descriptions.

```
-t posttrain \
-m SDXL \
-p $datatype \
-s $sequence_length
```

Name |
Options |
Description |
|---|---|---|
|
|
Benchmark post-training. |
|
|
Only Llama 3.1 8B supports FP8 precision. |
|
Sequence length for the language model. |
Between 2048 and 8192. 8192 by default. |

Post-training

To start the post-training benchmark, use the following command with the appropriate options. See the following list of options and their descriptions.

```
-t posttrain \
-m Flux \
-p $datatype \
-s $sequence_length
```

Name |
Options |
Description |
|---|---|---|
|
|
Benchmark post-training. |
|
|
Only Llama 3.1 8B supports FP8 precision. |
|
Sequence length for the language model. |
Between 2048 and 8192. 8192 by default. |

Pretraining

To start the pre-training benchmark, use the following command with the appropriate options. See the following list of options and their descriptions.

Go to the DLRM directory.

cd /workspace/DLRMBenchmark

To run the single node training benchmark for DLRM-v2 with TF32 precision, run the following script.

To run with MAD within the Docker container, use the following command.

-t pretrain -m DLRM


Benchmarking examples

For examples of benchmarking commands, see [ROCm/MAD](https://github.com/ROCm/MAD/tree/develop/benchmark/pytorch_train#benchmarking-examples).

### Multi-node training[#](#multi-node-training)

Refer to [Multi-node setup for AI workloads](../../../system-setup/multi-node-setup.html) to configure your environment for multi-node
training. See [PyTorch training](../../../system-setup/multi-node-setup.html#rocm-for-ai-multi-node-setup-pyt-train-example) for example Slurm run commands.

#### Pre-training[#](#pre-training)

Multi-node training with torchtitan is supported. The provided SLURM script is pre-configured for Llama 3 70B.

To launch the training job on a SLURM cluster for Llama 3 70B, run the following commands from the MAD repository.

```
# In the MAD repository
cd scripts/pytorch_train
sbatch run_slurm_train.sh
```

#### Fine-tuning[#](#fine-tuning)

Multi-node training with torchtune is supported. The provided SLURM script is pre-configured for Llama 3.3 70B.

To launch the training job on a SLURM cluster for Llama 3.3 70B, run the following commands from the MAD repository.

```
login # Get access to HF Llama model space
huggingface-cli download meta-llama/Llama-3.3-70B-Instruct --local-dir ./models/Llama-3.3-70B-Instruct # Download the Llama 3.3 model locally
# In the MAD repository
cd scripts/pytorch_train
sbatch Torchtune_Multinode.sh
```

Note

Information regarding benchmark setup:

By default, Llama 3.3 70B is fine-tuned using

`alpaca_dataset`

.You can adjust the torchtune

[YAML configuration file](https://github.com/pytorch/torchtune/blob/main/recipes/configs/llama3_3/70B_full_multinode.yaml)if you’re using a different model.The number of nodes and other parameters can be tuned in the SLURM script

`Torchtune_Multinode.sh`

.Set the

`mounting_paths`

inside the SLURM script.

Once the run is finished, you can find the log files in the `result_torchtune/`

directory.

## Further reading[#](#further-reading)

To learn more about MAD and the

`madengine`

CLI, see the[MAD usage guide](https://github.com/ROCm/MAD?tab=readme-ov-file#usage-guide).To learn more about system settings and management practices to configure your system for AMD Instinct MI300X Series GPUs, see

[AMD Instinct MI300X system optimization](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi300x.html).For a list of other ready-made Docker images for AI with ROCm, see

[AMD Infinity Hub](https://www.amd.com/en/developer/resources/infinity-hub.html#f-amd_hub_category=AI%20%26%20ML%20Models).

## Previous versions[#](#previous-versions)

See [PyTorch training performance testing version history](pytorch-training-history.html) to find documentation for previous releases
of the `ROCm/pytorch-training`

Docker image.
