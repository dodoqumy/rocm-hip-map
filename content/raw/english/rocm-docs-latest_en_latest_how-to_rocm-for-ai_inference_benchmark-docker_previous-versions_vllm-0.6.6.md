---
title: "LLM inference performance validation on AMD Instinct MI300X"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference/benchmark-docker/previous-versions/vllm-0.6.6.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-03T15:00:43.367897+00:00
content_hash: "40b4e781834cb869"
---

# LLM inference performance validation on AMD Instinct MI300X[#](#llm-inference-performance-validation-on-amd-instinct-mi300x)

2026-04-21

10 min read time

Caution

This documentation does not reflect the latest version of ROCm vLLM
inference performance documentation. See [vLLM inference](../vllm.html) for the latest version.

The [ROCm vLLM Docker](https://hub.docker.com/r/rocm/vllm/tags) image offers
a prebuilt, optimized environment for validating large language model (LLM)
inference performance on the AMD Instinct™ MI300X GPU. This ROCm vLLM
Docker image integrates vLLM and PyTorch tailored specifically for the MI300X
GPU and includes the following components:

With this Docker image, you can quickly validate the expected inference
performance numbers for the MI300X GPU. This topic also provides tips on
optimizing performance with popular AI models. For more information, see the lists of
[available models for MAD-integrated benchmarking](#vllm-benchmark-mad-v066-models)
and [standalone benchmarking](#vllm-benchmark-standalone-v066-options).

Note

vLLM is a toolkit and library for LLM inference and serving. AMD implements
high-performance custom kernels and modules in vLLM to enhance performance.
See [vLLM inference](../../llm-inference-frameworks.html#fine-tuning-llms-vllm) and [vLLM V1 performance optimization](../../../inference-optimization/vllm-optimization.html#mi300x-vllm-optimization) for
more information.

## Getting started[#](#getting-started)

Use the following procedures to reproduce the benchmark results on an MI300X GPU with the prebuilt vLLM Docker image.

Disable NUMA auto-balancing.

To optimize performance, disable automatic NUMA balancing. Otherwise, the GPU might hang until the periodic balancing is finalized. For more information, see the

[system validation steps](../../../system-setup/prerequisite-system-validation.html#rocm-for-ai-system-optimization).# disable automatic NUMA balancing sh -c 'echo 0 > /proc/sys/kernel/numa_balancing' # check if NUMA balancing is disabled (returns 0 if disabled) cat /proc/sys/kernel/numa_balancing 0

Download the

[ROCm vLLM Docker image](vllm-0.9.0.1-20250605.html#vllm-benchmark-unified-docker).Use the following command to pull the Docker image from Docker Hub.

pull rocm/vllm:rocm6.3.1_mi300_ubuntu22.04_py3.12_vllm_0.6.6


Once the setup is complete, choose between two options to reproduce the benchmark results:

## MAD-integrated benchmarking[#](#mad-integrated-benchmarking)

Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local
directory and install the required packages on the host machine.

```
clone https://github.com/ROCm/MAD
cd MAD
pip install -r requirements.txt
```

Use this command to run a performance benchmark test of the Llama 3.1 8B model
on one GPU with `float16`

data type in the host machine.

```
export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
python3 tools/run_models.py --tags pyt_vllm_llama-3.1-8b --keep-model-dir --live-output --timeout 28800
```

ROCm MAD launches a Docker container with the name
`container_ci-pyt_vllm_llama-3.1-8b`

. The latency and throughput reports of the
model are collected in the following path: `~/MAD/reports_float16/`

.

Although the following models are preconfigured to collect latency and
throughput performance data, you can also change the benchmarking parameters.
Refer to the [Standalone benchmarking](#vllm-benchmark-standalone-v066) section.

### Available models[#](#available-models)

Model name |
Tag |
|---|---|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|

## Standalone benchmarking[#](#standalone-benchmarking)

You can run the vLLM benchmark tool independently by starting the
[Docker container](vllm-0.7.3-20250325.html#vllm-benchmark-get-started) as shown in the following
snippet.


In the Docker container, clone the ROCm MAD repository and navigate to the
benchmark scripts directory at `~/MAD/scripts/vllm`

.

```
git clone https://github.com/ROCm/MAD
cd MAD/scripts/vllm
```

### Command[#](#command)

To start the benchmark, use the following command with the appropriate options.
See [Options](#vllm-benchmark-standalone-v066-options) for the list of
options and their descriptions.

```
-s $test_option -m $model_repo -g $num_gpu -d $datatype
```

See the [examples](#vllm-benchmark-run-benchmark-v066) for more information.

Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don’t need to specify them with this script.

Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

```
You are trying to access a gated repo.
# pass your HF_TOKEN
export HF_TOKEN=$your_personal_hf_token
```

### Options and available models[#](#options-and-available-models)

Name |
Options |
Description |
|---|---|---|
|
latency |
Measure decoding token latency |
throughput |
Measure token generation throughput |
|
all |
Measure both throughput and latency |
|
|
|
|
( |
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
||
|
||
|
||
|
||
|
||
|
||
|
||
|
||
|
||
|
||
|
||
|
|
|
( |
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
||
|
1 or 8 |
Number of GPUs |
|
|
Data type |

### Running the benchmark on the MI300X GPU[#](#running-the-benchmark-on-the-mi300x-gpu)

Here are some examples of running the benchmark with various options.
See [Options](#vllm-benchmark-standalone-v066-options) for the list of
options and their descriptions.

#### Example 1: latency benchmark[#](#example-1-latency-benchmark)

Use this command to benchmark the latency of the Llama 3.1 70B model on eight GPUs with the `float16`

and `float8`

data types.

```
./vllm_benchmark_report.sh -s latency -m meta-llama/Llama-3.1-70B-Instruct -g 8 -d float16
./vllm_benchmark_report.sh -s latency -m amd/Llama-3.1-70B-Instruct-FP8-KV -g 8 -d float8
```

Find the latency reports at:

`./reports_float16/summary/Llama-3.1-70B-Instruct_latency_report.csv`

`./reports_float8/summary/Llama-3.1-70B-Instruct-FP8-KV_latency_report.csv`


#### Example 2: throughput benchmark[#](#example-2-throughput-benchmark)

Use this command to benchmark the throughput of the Llama 3.1 70B model on eight GPUs with the `float16`

and `float8`

data types.

```
-s throughput -m meta-llama/Llama-3.1-70B-Instruct -g 8 -d float16
./vllm_benchmark_report.sh -s throughput -m amd/Llama-3.1-70B-Instruct-FP8-KV -g 8 -d float8
```

Find the throughput reports at:

`./reports_float16/summary/Llama-3.1-70B-Instruct_throughput_report.csv`

`./reports_float8/summary/Llama-3.1-70B-Instruct-FP8-KV_throughput_report.csv`


Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

## Further reading[#](#further-reading)

For application performance optimization strategies for HPC and AI workloads, including inference with vLLM, see

[AMD Instinct MI300X workload optimization](../../../inference-optimization/workload.html).To learn more about the options for latency and throughput benchmark scripts, see

[ROCm/vllm](https://github.com/ROCm/vllm/tree/main/benchmarks).To learn more about system settings and management practices to configure your system for MI300X Series GPUs, see

[AMD Instinct MI300X system optimization](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi300x.html)To learn how to run community models from Hugging Face on AMD GPUs, see

[Running models from Hugging Face](../../hugging-face-models.html).To learn how to fine-tune LLMs and optimize inference, see

[Fine-tuning LLMs and inference optimization](../../../fine-tuning/fine-tuning-and-inference.html).For a list of other ready-made Docker images for AI with ROCm, see

[AMD Infinity Hub](https://www.amd.com/en/developer/resources/infinity-hub.html#f-amd_hub_category=AI%20%26%20ML%20Models).

## Previous versions[#](#previous-versions)

See [vLLM inference performance testing version history](vllm-history.html) to find documentation for previous releases
of the `ROCm/vllm`

Docker image.
