---
title: "Training a model with JAX MaxText on ROCm"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/training/benchmark-docker/previous-versions/jax-maxtext-v25.9.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:01:38.660399+00:00
content_hash: "f7afcfe26ea5621b"
---

# Training a model with JAX MaxText on ROCm[#](#training-a-model-with-jax-maxtext-on-rocm)

2026-04-21

24 min read time

Caution

This documentation does not reflect the latest version of ROCm JAX MaxText
training performance documentation. See [Training a model with Primus and JAX MaxText](../jax-maxtext.html) for the latest version.

Note

We have refreshed the `rocm/jax-training:maxtext-v25.9`

image as
rocm/jax-training:maxtext-v25.9.1. This should include a fix to address
segmentation fault issues during launch.

The MaxText for ROCm training Docker image provides a prebuilt environment for training on AMD Instinct MI355X, MI350X, MI325X, and MI300X GPUs, including essential components like JAX, XLA, ROCm libraries, and MaxText utilities. It includes the following software components:

Software component |
Version |
|---|---|
ROCm |
7.0.0 |
JAX |
0.6.2 |
Python |
3.10.18 |
Transformer Engine |
2.2.0.dev0+c91bac54 |
hipBLASLt |
1.x.x |

MaxText with on ROCm provides the following key features to train large language models efficiently:

Transformer Engine (TE)

Flash Attention (FA) 3 – with or without sequence input packing

GEMM tuning

Multi-node support

NANOO FP8 (for MI300X series GPUs) and FP8 (for MI355X and MI350X) quantization support


## Supported models[#](#supported-models)

The following models are pre-optimized for performance on AMD Instinct GPUs. Some instructions, commands, and available training configurations in this documentation might vary by model – select one to get started.

Note

Some models, such as Llama 3, require an external license agreement through a third party (for example, Meta).

## System validation[#](#system-validation)

Before running AI workloads, it’s important to validate that your AMD hardware is configured correctly and performing optimally.

If you have already validated your system settings, including aspects like NUMA auto-balancing, you
can skip this step. Otherwise, complete the procedures in the [System validation and
optimization](../../../system-setup/prerequisite-system-validation.html#rocm-for-ai-system-optimization) guide to properly configure your system settings
before starting training.

To test for optimal performance, consult the recommended [System health benchmarks](../../../system-setup/system-health-check.html#rocm-for-ai-system-health-bench). This suite of tests will help you verify and fine-tune your
system’s configuration.

## Environment setup[#](#environment-setup)

This Docker image is optimized for specific model configurations outlined as follows. Performance can vary for other training workloads, as AMD doesn’t validate configurations and run conditions outside those described.

### Pull the Docker image[#](#pull-the-docker-image)

Use the following command to pull the Docker image from Docker Hub.

```
pull rocm/jax-training:maxtext-v25.9.1
```

### Multi-node configuration[#](#multi-node-configuration)

See [Multi-node setup for AI workloads](../../../system-setup/multi-node-setup.html) to configure your
environment for multi-node training.

## Benchmarking[#](#benchmarking)

Once the setup is complete, choose between two options to reproduce the benchmark results:

The following run command is tailored to Llama 2 7B.
See [Supported models](#amd-maxtext-model-support-v259) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

Use this command to run the performance benchmark test on the Llama 2 7B model using one GPU with the

`bf16`

data type on the host machine.export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags jax_maxtext_train_llama-2-7b \ --keep-model-dir \ --live-output \ --timeout 28800


MAD launches a Docker container with the name
`container_ci-jax_maxtext_train_llama-2-7b`

. The latency and throughput reports of the
model are collected in the following path: `~/MAD/perf.csv/`

.

The following commands are optimized for Llama 2 7B. See
[Supported models](#amd-maxtext-model-support-v259) to switch to another
available model. Some instructions and resources might not be
available for all models and configurations.

Download the Docker image and required scripts

Run the JAX MaxText benchmark tool independently by starting the Docker container as shown in the following snippet.

```
pull rocm/jax-training:maxtext-v25.9.1
```

Single node training

Set up environment variables.

export MAD_SECRETS_HFTOKEN=<Your Hugging Face token> export HF_HOME=<Location of saved/cached Hugging Face models>

`MAD_SECRETS_HFTOKEN`

is your Hugging Face access token to access models, tokenizers, and data. See[User access tokens](https://huggingface.co/docs/hub/en/security-tokens).`HF_HOME`

is where`huggingface_hub`

will store local data. See[huggingface_hub CLI](https://huggingface.co/docs/huggingface_hub/main/en/guides/cli#huggingface-cli-download). If you already have downloaded or cached Hugging Face artifacts, set this variable to that path. Downloaded files typically get cached to`~/.cache/huggingface`

.Launch the Docker container.

run -it \ --device=/dev/dri \ --device=/dev/kfd \ --network host \ --ipc host \ --group-add video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --privileged \ -v $HOME:$HOME \ -v $HOME/.ssh:/root/.ssh \ -v $HF_HOME:/hf_cache \ -e HF_HOME=/hf_cache \ -e MAD_SECRETS_HFTOKEN=$MAD_SECRETS_HFTOKEN --shm-size 64G \ --name training_env \ rocm/jax-training:maxtext-v25.9.1

In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at

`MAD/scripts/jax-maxtext`

.clone https://github.com/ROCm/MAD cd MAD/scripts/jax-maxtext

Run the setup scripts to install libraries and datasets needed for benchmarking.

-m Llama-2-7B

To run the training benchmark without quantization, use the following command:

-m Llama-2-7B

For quantized training, run the script with the appropriate option for your Instinct GPU.

For

`fp8`

quantized training on MI355X and MI350X GPUs, use the following command:-m Llama-2-7B -q fp8

For

`nanoo_fp8`

quantized training on MI300X series GPUs, use the following command:-m Llama-2-7B -q nanoo_fp8


Multi-node training

The following examples use SLURM to run on multiple nodes.

Note

The following scripts will launch the Docker container and run the benchmark. Run them outside of any Docker container.

Make sure

`$HF_HOME`

is set before running the test. See[ROCm benchmarking](https://github.com/ROCm/MAD/blob/develop/scripts/jax-maxtext/gpu-rocm/readme.md)for more details on downloading the Llama models before running the benchmark.To run multi-node training for Llama 2 7B, use the

[multi-node training script](https://github.com/ROCm/MAD/blob/develop/scripts/jax-maxtext/gpu-rocm/llama2_7b_multinode.sh)under the`scripts/jax-maxtext/gpu-rocm/`

directory.Run the multi-node training benchmark script.

-N <num_nodes> llama2_7b_multinode.sh


The following run command is tailored to Llama 2 70B.
See [Supported models](#amd-maxtext-model-support-v259) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

Use this command to run the performance benchmark test on the Llama 2 70B model using one GPU with the

`bf16`

data type on the host machine.export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags jax_maxtext_train_llama-2-70b \ --keep-model-dir \ --live-output \ --timeout 28800


MAD launches a Docker container with the name
`container_ci-jax_maxtext_train_llama-2-70b`

. The latency and throughput reports of the
model are collected in the following path: `~/MAD/perf.csv/`

.

The following commands are optimized for Llama 2 70B. See
[Supported models](#amd-maxtext-model-support-v259) to switch to another
available model. Some instructions and resources might not be
available for all models and configurations.

Download the Docker image and required scripts

Run the JAX MaxText benchmark tool independently by starting the Docker container as shown in the following snippet.

```
pull rocm/jax-training:maxtext-v25.9.1
```

Single node training

Set up environment variables.

export MAD_SECRETS_HFTOKEN=<Your Hugging Face token> export HF_HOME=<Location of saved/cached Hugging Face models>

`MAD_SECRETS_HFTOKEN`

is your Hugging Face access token to access models, tokenizers, and data. See[User access tokens](https://huggingface.co/docs/hub/en/security-tokens).`HF_HOME`

is where`huggingface_hub`

will store local data. See[huggingface_hub CLI](https://huggingface.co/docs/huggingface_hub/main/en/guides/cli#huggingface-cli-download). If you already have downloaded or cached Hugging Face artifacts, set this variable to that path. Downloaded files typically get cached to`~/.cache/huggingface`

.Launch the Docker container.

run -it \ --device=/dev/dri \ --device=/dev/kfd \ --network host \ --ipc host \ --group-add video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --privileged \ -v $HOME:$HOME \ -v $HOME/.ssh:/root/.ssh \ -v $HF_HOME:/hf_cache \ -e HF_HOME=/hf_cache \ -e MAD_SECRETS_HFTOKEN=$MAD_SECRETS_HFTOKEN --shm-size 64G \ --name training_env \ rocm/jax-training:maxtext-v25.9.1

In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at

`MAD/scripts/jax-maxtext`

.clone https://github.com/ROCm/MAD cd MAD/scripts/jax-maxtext

Run the setup scripts to install libraries and datasets needed for benchmarking.

-m Llama-2-70B

To run the training benchmark without quantization, use the following command:

-m Llama-2-70B

For quantized training, run the script with the appropriate option for your Instinct GPU.

For

`fp8`

quantized training on MI355X and MI350X GPUs, use the following command:-m Llama-2-70B -q fp8

For

`nanoo_fp8`

quantized training on MI300X series GPUs, use the following command:-m Llama-2-70B -q nanoo_fp8


Multi-node training

The following examples use SLURM to run on multiple nodes.

Note

The following scripts will launch the Docker container and run the benchmark. Run them outside of any Docker container.

Make sure

`$HF_HOME`

is set before running the test. See[ROCm benchmarking](https://github.com/ROCm/MAD/blob/develop/scripts/jax-maxtext/gpu-rocm/readme.md)for more details on downloading the Llama models before running the benchmark.To run multi-node training for Llama 2 70B, use the

[multi-node training script](https://github.com/ROCm/MAD/blob/develop/scripts/jax-maxtext/gpu-rocm/llama2_70b_multinode.sh)under the`scripts/jax-maxtext/gpu-rocm/`

directory.Run the multi-node training benchmark script.

-N <num_nodes> llama2_70b_multinode.sh


The following commands are optimized for Llama 3 8B (multi-node). See
[Supported models](#amd-maxtext-model-support-v259) to switch to another
available model. Some instructions and resources might not be
available for all models and configurations.

Download the Docker image and required scripts

Run the JAX MaxText benchmark tool independently by starting the Docker container as shown in the following snippet.

```
pull rocm/jax-training:maxtext-v25.9.1
```

Multi-node training

The following examples use SLURM to run on multiple nodes.

Note

The following scripts will launch the Docker container and run the benchmark. Run them outside of any Docker container.

Make sure

`$HF_HOME`

is set before running the test. See[ROCm benchmarking](https://github.com/ROCm/MAD/blob/develop/scripts/jax-maxtext/gpu-rocm/readme.md)for more details on downloading the Llama models before running the benchmark.To run multi-node training for Llama 3 8B (multi-node), use the

[multi-node training script](https://github.com/ROCm/MAD/blob/develop/scripts/jax-maxtext/gpu-rocm/llama3_8b_multinode.sh)under the`scripts/jax-maxtext/gpu-rocm/`

directory.Run the multi-node training benchmark script.

-N <num_nodes> llama3_8b_multinode.sh


The following commands are optimized for Llama 3 70B (multi-node). See
[Supported models](#amd-maxtext-model-support-v259) to switch to another
available model. Some instructions and resources might not be
available for all models and configurations.

Download the Docker image and required scripts

Run the JAX MaxText benchmark tool independently by starting the Docker container as shown in the following snippet.

```
pull rocm/jax-training:maxtext-v25.9.1
```

Multi-node training

The following examples use SLURM to run on multiple nodes.

Note

The following scripts will launch the Docker container and run the benchmark. Run them outside of any Docker container.

Make sure

`$HF_HOME`

is set before running the test. See[ROCm benchmarking](https://github.com/ROCm/MAD/blob/develop/scripts/jax-maxtext/gpu-rocm/readme.md)for more details on downloading the Llama models before running the benchmark.To run multi-node training for Llama 3 70B (multi-node), use the

[multi-node training script](https://github.com/ROCm/MAD/blob/develop/scripts/jax-maxtext/gpu-rocm/llama3_70b_multinode.sh)under the`scripts/jax-maxtext/gpu-rocm/`

directory.Run the multi-node training benchmark script.

-N <num_nodes> llama3_70b_multinode.sh


The following run command is tailored to Llama 3.1 8B.
See [Supported models](#amd-maxtext-model-support-v259) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

Use this command to run the performance benchmark test on the Llama 3.1 8B model using one GPU with the

`bf16`

data type on the host machine.export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags jax_maxtext_train_llama-3.1-8b \ --keep-model-dir \ --live-output \ --timeout 28800


MAD launches a Docker container with the name
`container_ci-jax_maxtext_train_llama-3.1-8b`

. The latency and throughput reports of the
model are collected in the following path: `~/MAD/perf.csv/`

.

The following commands are optimized for Llama 3.1 8B. See
[Supported models](#amd-maxtext-model-support-v259) to switch to another
available model. Some instructions and resources might not be
available for all models and configurations.

Download the Docker image and required scripts

Run the JAX MaxText benchmark tool independently by starting the Docker container as shown in the following snippet.

```
pull rocm/jax-training:maxtext-v25.9.1
```

Single node training

Set up environment variables.

export MAD_SECRETS_HFTOKEN=<Your Hugging Face token> export HF_HOME=<Location of saved/cached Hugging Face models>

`MAD_SECRETS_HFTOKEN`

is your Hugging Face access token to access models, tokenizers, and data. See[User access tokens](https://huggingface.co/docs/hub/en/security-tokens).`HF_HOME`

is where`huggingface_hub`

will store local data. See[huggingface_hub CLI](https://huggingface.co/docs/huggingface_hub/main/en/guides/cli#huggingface-cli-download). If you already have downloaded or cached Hugging Face artifacts, set this variable to that path. Downloaded files typically get cached to`~/.cache/huggingface`

.Launch the Docker container.

run -it \ --device=/dev/dri \ --device=/dev/kfd \ --network host \ --ipc host \ --group-add video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --privileged \ -v $HOME:$HOME \ -v $HOME/.ssh:/root/.ssh \ -v $HF_HOME:/hf_cache \ -e HF_HOME=/hf_cache \ -e MAD_SECRETS_HFTOKEN=$MAD_SECRETS_HFTOKEN --shm-size 64G \ --name training_env \ rocm/jax-training:maxtext-v25.9.1

In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at

`MAD/scripts/jax-maxtext`

.clone https://github.com/ROCm/MAD cd MAD/scripts/jax-maxtext

Run the setup scripts to install libraries and datasets needed for benchmarking.

-m Llama-3.1-8B

To run the training benchmark without quantization, use the following command:

-m Llama-3.1-8B

For quantized training, run the script with the appropriate option for your Instinct GPU.

For

`fp8`

quantized training on MI355X and MI350X GPUs, use the following command:-m Llama-3.1-8B -q fp8

For

`nanoo_fp8`

quantized training on MI300X series GPUs, use the following command:-m Llama-3.1-8B -q nanoo_fp8


Multi-node training

For multi-node training examples, choose a model from [Supported models](#amd-maxtext-model-support-v259)
with an available [multi-node training script](https://github.com/ROCm/MAD/tree/develop/scripts/jax-maxtext/gpu-rocm).

The following run command is tailored to Llama 3.1 70B.
See [Supported models](#amd-maxtext-model-support-v259) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

Use this command to run the performance benchmark test on the Llama 3.1 70B model using one GPU with the

`bf16`

data type on the host machine.export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags jax_maxtext_train_llama-3.1-70b \ --keep-model-dir \ --live-output \ --timeout 28800


MAD launches a Docker container with the name
`container_ci-jax_maxtext_train_llama-3.1-70b`

. The latency and throughput reports of the
model are collected in the following path: `~/MAD/perf.csv/`

.

The following commands are optimized for Llama 3.1 70B. See
[Supported models](#amd-maxtext-model-support-v259) to switch to another
available model. Some instructions and resources might not be
available for all models and configurations.

Download the Docker image and required scripts

Run the JAX MaxText benchmark tool independently by starting the Docker container as shown in the following snippet.

```
pull rocm/jax-training:maxtext-v25.9.1
```

Single node training

Set up environment variables.

export MAD_SECRETS_HFTOKEN=<Your Hugging Face token> export HF_HOME=<Location of saved/cached Hugging Face models>

`MAD_SECRETS_HFTOKEN`

is your Hugging Face access token to access models, tokenizers, and data. See[User access tokens](https://huggingface.co/docs/hub/en/security-tokens).`HF_HOME`

is where`huggingface_hub`

will store local data. See[huggingface_hub CLI](https://huggingface.co/docs/huggingface_hub/main/en/guides/cli#huggingface-cli-download). If you already have downloaded or cached Hugging Face artifacts, set this variable to that path. Downloaded files typically get cached to`~/.cache/huggingface`

.Launch the Docker container.

run -it \ --device=/dev/dri \ --device=/dev/kfd \ --network host \ --ipc host \ --group-add video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --privileged \ -v $HOME:$HOME \ -v $HOME/.ssh:/root/.ssh \ -v $HF_HOME:/hf_cache \ -e HF_HOME=/hf_cache \ -e MAD_SECRETS_HFTOKEN=$MAD_SECRETS_HFTOKEN --shm-size 64G \ --name training_env \ rocm/jax-training:maxtext-v25.9.1

In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at

`MAD/scripts/jax-maxtext`

.clone https://github.com/ROCm/MAD cd MAD/scripts/jax-maxtext

Run the setup scripts to install libraries and datasets needed for benchmarking.

-m Llama-3.1-70B

To run the training benchmark without quantization, use the following command:

-m Llama-3.1-70B

For quantized training, run the script with the appropriate option for your Instinct GPU.

For

`fp8`

quantized training on MI355X and MI350X GPUs, use the following command:-m Llama-3.1-70B -q fp8


Multi-node training

For multi-node training examples, choose a model from [Supported models](#amd-maxtext-model-support-v259)
with an available [multi-node training script](https://github.com/ROCm/MAD/tree/develop/scripts/jax-maxtext/gpu-rocm).

The following run command is tailored to Llama 3.3 70B.
See [Supported models](#amd-maxtext-model-support-v259) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

Use this command to run the performance benchmark test on the Llama 3.3 70B model using one GPU with the

`bf16`

data type on the host machine.export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags jax_maxtext_train_llama-3.3-70b \ --keep-model-dir \ --live-output \ --timeout 28800


MAD launches a Docker container with the name
`container_ci-jax_maxtext_train_llama-3.3-70b`

. The latency and throughput reports of the
model are collected in the following path: `~/MAD/perf.csv/`

.

The following commands are optimized for Llama 3.3 70B. See
[Supported models](#amd-maxtext-model-support-v259) to switch to another
available model. Some instructions and resources might not be
available for all models and configurations.

Download the Docker image and required scripts

Run the JAX MaxText benchmark tool independently by starting the Docker container as shown in the following snippet.

```
pull rocm/jax-training:maxtext-v25.9.1
```

Single node training

Set up environment variables.

export MAD_SECRETS_HFTOKEN=<Your Hugging Face token> export HF_HOME=<Location of saved/cached Hugging Face models>

`MAD_SECRETS_HFTOKEN`

is your Hugging Face access token to access models, tokenizers, and data. See[User access tokens](https://huggingface.co/docs/hub/en/security-tokens).`HF_HOME`

is where`huggingface_hub`

will store local data. See[huggingface_hub CLI](https://huggingface.co/docs/huggingface_hub/main/en/guides/cli#huggingface-cli-download). If you already have downloaded or cached Hugging Face artifacts, set this variable to that path. Downloaded files typically get cached to`~/.cache/huggingface`

.Launch the Docker container.

run -it \ --device=/dev/dri \ --device=/dev/kfd \ --network host \ --ipc host \ --group-add video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --privileged \ -v $HOME:$HOME \ -v $HOME/.ssh:/root/.ssh \ -v $HF_HOME:/hf_cache \ -e HF_HOME=/hf_cache \ -e MAD_SECRETS_HFTOKEN=$MAD_SECRETS_HFTOKEN --shm-size 64G \ --name training_env \ rocm/jax-training:maxtext-v25.9.1

In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at

`MAD/scripts/jax-maxtext`

.clone https://github.com/ROCm/MAD cd MAD/scripts/jax-maxtext

Run the setup scripts to install libraries and datasets needed for benchmarking.

-m Llama-3.3-70B

To run the training benchmark without quantization, use the following command:

-m Llama-3.3-70B

For quantized training, run the script with the appropriate option for your Instinct GPU.

For

`fp8`

quantized training on MI355X and MI350X GPUs, use the following command:-m Llama-3.3-70B -q fp8


Multi-node training

For multi-node training examples, choose a model from [Supported models](#amd-maxtext-model-support-v259)
with an available [multi-node training script](https://github.com/ROCm/MAD/tree/develop/scripts/jax-maxtext/gpu-rocm).

The following run command is tailored to DeepSeek-V2-Lite (16B).
See [Supported models](#amd-maxtext-model-support-v259) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

Use this command to run the performance benchmark test on the DeepSeek-V2-Lite (16B) model using one GPU with the

`bf16`

data type on the host machine.export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags jax_maxtext_train_deepseek-v2-lite-16b \ --keep-model-dir \ --live-output \ --timeout 28800


MAD launches a Docker container with the name
`container_ci-jax_maxtext_train_deepseek-v2-lite-16b`

. The latency and throughput reports of the
model are collected in the following path: `~/MAD/perf.csv/`

.

The following commands are optimized for DeepSeek-V2-Lite (16B). See
[Supported models](#amd-maxtext-model-support-v259) to switch to another
available model. Some instructions and resources might not be
available for all models and configurations.

Download the Docker image and required scripts

Run the JAX MaxText benchmark tool independently by starting the Docker container as shown in the following snippet.

```
pull rocm/jax-training:maxtext-v25.9.1
```

Single node training

Set up environment variables.

export MAD_SECRETS_HFTOKEN=<Your Hugging Face token> export HF_HOME=<Location of saved/cached Hugging Face models>

`MAD_SECRETS_HFTOKEN`

is your Hugging Face access token to access models, tokenizers, and data. See[User access tokens](https://huggingface.co/docs/hub/en/security-tokens).`HF_HOME`

is where`huggingface_hub`

will store local data. See[huggingface_hub CLI](https://huggingface.co/docs/huggingface_hub/main/en/guides/cli#huggingface-cli-download). If you already have downloaded or cached Hugging Face artifacts, set this variable to that path. Downloaded files typically get cached to`~/.cache/huggingface`

.Launch the Docker container.

run -it \ --device=/dev/dri \ --device=/dev/kfd \ --network host \ --ipc host \ --group-add video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --privileged \ -v $HOME:$HOME \ -v $HOME/.ssh:/root/.ssh \ -v $HF_HOME:/hf_cache \ -e HF_HOME=/hf_cache \ -e MAD_SECRETS_HFTOKEN=$MAD_SECRETS_HFTOKEN --shm-size 64G \ --name training_env \ rocm/jax-training:maxtext-v25.9.1

In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at

`MAD/scripts/jax-maxtext`

.clone https://github.com/ROCm/MAD cd MAD/scripts/jax-maxtext

Run the setup scripts to install libraries and datasets needed for benchmarking.

-m DeepSeek-V2-lite

To run the training benchmark without quantization, use the following command:

-m DeepSeek-V2-lite

For quantized training, run the script with the appropriate option for your Instinct GPU.

For

`fp8`

quantized training on MI355X and MI350X GPUs, use the following command:-m DeepSeek-V2-lite -q fp8

For

`nanoo_fp8`

quantized training on MI300X series GPUs, use the following command:-m DeepSeek-V2-lite -q nanoo_fp8


Multi-node training

For multi-node training examples, choose a model from [Supported models](#amd-maxtext-model-support-v259)
with an available [multi-node training script](https://github.com/ROCm/MAD/tree/develop/scripts/jax-maxtext/gpu-rocm).

The following run command is tailored to Mixtral 8x7B.
See [Supported models](#amd-maxtext-model-support-v259) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

Use this command to run the performance benchmark test on the Mixtral 8x7B model using one GPU with the

`bf16`

data type on the host machine.export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags jax_maxtext_train_mixtral-8x7b \ --keep-model-dir \ --live-output \ --timeout 28800


MAD launches a Docker container with the name
`container_ci-jax_maxtext_train_mixtral-8x7b`

. The latency and throughput reports of the
model are collected in the following path: `~/MAD/perf.csv/`

.

The following commands are optimized for Mixtral 8x7B. See
[Supported models](#amd-maxtext-model-support-v259) to switch to another
available model. Some instructions and resources might not be
available for all models and configurations.

Download the Docker image and required scripts

Run the JAX MaxText benchmark tool independently by starting the Docker container as shown in the following snippet.

```
pull rocm/jax-training:maxtext-v25.9.1
```

Single node training

Set up environment variables.

export MAD_SECRETS_HFTOKEN=<Your Hugging Face token> export HF_HOME=<Location of saved/cached Hugging Face models>

`MAD_SECRETS_HFTOKEN`

is your Hugging Face access token to access models, tokenizers, and data. See[User access tokens](https://huggingface.co/docs/hub/en/security-tokens).`HF_HOME`

is where`huggingface_hub`

will store local data. See[huggingface_hub CLI](https://huggingface.co/docs/huggingface_hub/main/en/guides/cli#huggingface-cli-download). If you already have downloaded or cached Hugging Face artifacts, set this variable to that path. Downloaded files typically get cached to`~/.cache/huggingface`

.Launch the Docker container.

run -it \ --device=/dev/dri \ --device=/dev/kfd \ --network host \ --ipc host \ --group-add video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --privileged \ -v $HOME:$HOME \ -v $HOME/.ssh:/root/.ssh \ -v $HF_HOME:/hf_cache \ -e HF_HOME=/hf_cache \ -e MAD_SECRETS_HFTOKEN=$MAD_SECRETS_HFTOKEN --shm-size 64G \ --name training_env \ rocm/jax-training:maxtext-v25.9.1

In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at

`MAD/scripts/jax-maxtext`

.clone https://github.com/ROCm/MAD cd MAD/scripts/jax-maxtext

Run the setup scripts to install libraries and datasets needed for benchmarking.

-m Mixtral-8x7B

To run the training benchmark without quantization, use the following command:

-m Mixtral-8x7B

For quantized training, run the script with the appropriate option for your Instinct GPU.

For

`fp8`

quantized training on MI355X and MI350X GPUs, use the following command:-m Mixtral-8x7B -q fp8

For

`nanoo_fp8`

quantized training on MI300X series GPUs, use the following command:-m Mixtral-8x7B -q nanoo_fp8


Multi-node training

For multi-node training examples, choose a model from [Supported models](#amd-maxtext-model-support-v259)
with an available [multi-node training script](https://github.com/ROCm/MAD/tree/develop/scripts/jax-maxtext/gpu-rocm).

## Further reading[#](#further-reading)

To learn more about MAD and the

`madengine`

CLI, see the[MAD usage guide](https://github.com/ROCm/MAD?tab=readme-ov-file#usage-guide).To learn more about system settings and management practices to configure your system for AMD Instinct MI300X Series GPUs, see

[AMD Instinct MI300X system optimization](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi300x.html).For a list of other ready-made Docker images for AI with ROCm, see

[AMD Infinity Hub](https://www.amd.com/en/developer/resources/infinity-hub.html#f-amd_hub_category=AI%20%26%20ML%20Models).

## Previous versions[#](#previous-versions)

See [JAX MaxText training performance testing version history](jax-maxtext-history.html) to find documentation for previous releases
of the `ROCm/jax-training`

Docker image.
