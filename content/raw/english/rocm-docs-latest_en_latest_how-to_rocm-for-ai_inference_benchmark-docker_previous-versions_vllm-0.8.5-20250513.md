---
title: "vLLM inference performance testing"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference/benchmark-docker/previous-versions/vllm-0.8.5-20250513.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:02:14.094434+00:00
content_hash: "dc3616353c263050"
---

# vLLM inference performance testing[#](#vllm-inference-performance-testing)

2026-04-21

72 min read time

Caution

This documentation does not reflect the latest version of ROCm vLLM
inference performance documentation. See [vLLM inference](../vllm.html) for the latest version.

The [ROCm vLLM Docker](https://hub.docker.com/layers/rocm/vllm/rocm6.3.1_vllm_0.8.5_20250513/images/sha256-5c8b4436dd0464119d9df2b44c745fadf81512f18ffb2f4b5dc235c71ebe26b4) image offers
a prebuilt, optimized environment for validating large language model (LLM)
inference performance on AMD Instinct™ MI300X Series GPUs. This ROCm vLLM
Docker image integrates vLLM and PyTorch tailored specifically for MI300X Series
GPUs and includes the following components:

With this Docker image, you can quickly test the [expected
inference performance numbers](#vllm-benchmark-performance-measurements-v085-20250513) for
MI300X Series GPUs.

## Supported models[#](#supported-models)

The following models are supported for inference performance benchmarking with vLLM and ROCm. Some instructions, commands, and recommendations in this documentation might vary by model – select one to get started.

Note

See the [Llama 3.1 8B model card on Hugging Face](https://huggingface.co/meta-llama/Llama-3.1-8B) to learn more about your selected model.
Some models require access authorization prior to use via an external license agreement through a third party.

Note

See the [Llama 3.1 70B model card on Hugging Face](https://huggingface.co/meta-llama/Llama-3.1-70B-Instruct) to learn more about your selected model.
Some models require access authorization prior to use via an external license agreement through a third party.

Note

See the [Llama 3.1 405B model card on Hugging Face](https://huggingface.co/meta-llama/Llama-3.1-405B-Instruct) to learn more about your selected model.
Some models require access authorization prior to use via an external license agreement through a third party.

Note

See the [Llama 3.2 11B Vision model card on Hugging Face](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct) to learn more about your selected model.
Some models require access authorization prior to use via an external license agreement through a third party.

Note

See the [Llama 2 7B model card on Hugging Face](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf) to learn more about your selected model.
Some models require access authorization prior to use via an external license agreement through a third party.

Note

See the [Llama 2 70B model card on Hugging Face](https://huggingface.co/meta-llama/Llama-2-70b-chat-hf) to learn more about your selected model.
Some models require access authorization prior to use via an external license agreement through a third party.

Note

See the [Llama 3.1 8B FP8 model card on Hugging Face](https://huggingface.co/amd/Llama-3.1-8B-Instruct-FP8-KV) to learn more about your selected model.
Some models require access authorization prior to use via an external license agreement through a third party.

Note

See the [Llama 3.1 70B FP8 model card on Hugging Face](https://huggingface.co/amd/Llama-3.1-70B-Instruct-FP8-KV) to learn more about your selected model.
Some models require access authorization prior to use via an external license agreement through a third party.

Note

See the [Llama 3.1 405B FP8 model card on Hugging Face](https://huggingface.co/amd/Llama-3.1-405B-Instruct-FP8-KV) to learn more about your selected model.
Some models require access authorization prior to use via an external license agreement through a third party.

Note

See the [Mixtral MoE 8x7B model card on Hugging Face](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1) to learn more about your selected model.
Some models require access authorization prior to use via an external license agreement through a third party.

Note

See the [Mixtral MoE 8x22B model card on Hugging Face](https://huggingface.co/mistralai/Mixtral-8x22B-Instruct-v0.1) to learn more about your selected model.
Some models require access authorization prior to use via an external license agreement through a third party.

Note

See the [Mistral 7B model card on Hugging Face](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3) to learn more about your selected model.
Some models require access authorization prior to use via an external license agreement through a third party.

Note

See the [Mixtral MoE 8x7B FP8 model card on Hugging Face](https://huggingface.co/amd/Mixtral-8x7B-Instruct-v0.1-FP8-KV) to learn more about your selected model.
Some models require access authorization prior to use via an external license agreement through a third party.

Note

See the [Mixtral MoE 8x22B FP8 model card on Hugging Face](https://huggingface.co/amd/Mixtral-8x22B-Instruct-v0.1-FP8-KV) to learn more about your selected model.
Some models require access authorization prior to use via an external license agreement through a third party.

Note

See the [Mistral 7B FP8 model card on Hugging Face](https://huggingface.co/amd/Mistral-7B-v0.1-FP8-KV) to learn more about your selected model.
Some models require access authorization prior to use via an external license agreement through a third party.

Note

See the [Qwen2 7B model card on Hugging Face](https://huggingface.co/Qwen/Qwen2-7B-Instruct) to learn more about your selected model.
Some models require access authorization prior to use via an external license agreement through a third party.

Note

See the [Qwen2 72B model card on Hugging Face](https://huggingface.co/Qwen/Qwen2-72B-Instruct) to learn more about your selected model.
Some models require access authorization prior to use via an external license agreement through a third party.

Note

See the [DBRX Instruct model card on Hugging Face](https://huggingface.co/databricks/dbrx-instruct) to learn more about your selected model.
Some models require access authorization prior to use via an external license agreement through a third party.

Note

See the [DBRX Instruct FP8 model card on Hugging Face](https://huggingface.co/amd/dbrx-instruct-FP8-KV) to learn more about your selected model.
Some models require access authorization prior to use via an external license agreement through a third party.

Note

See the [Gemma 2 27B model card on Hugging Face](https://huggingface.co/google/gemma-2-27b) to learn more about your selected model.
Some models require access authorization prior to use via an external license agreement through a third party.

Note

See the [C4AI Command R+ 08-2024 model card on Hugging Face](https://huggingface.co/CohereForAI/c4ai-command-r-plus-08-2024) to learn more about your selected model.
Some models require access authorization prior to use via an external license agreement through a third party.

Note

See the [C4AI Command R+ 08-2024 FP8 model card on Hugging Face](https://huggingface.co/amd/c4ai-command-r-plus-FP8-KV) to learn more about your selected model.
Some models require access authorization prior to use via an external license agreement through a third party.

Note

See the [DeepSeek MoE 16B model card on Hugging Face](https://huggingface.co/deepseek-ai/deepseek-moe-16b-chat) to learn more about your selected model.
Some models require access authorization prior to use via an external license agreement through a third party.

Note

vLLM is a toolkit and library for LLM inference and serving. AMD implements
high-performance custom kernels and modules in vLLM to enhance performance.
See [vLLM inference](../../llm-inference-frameworks.html#fine-tuning-llms-vllm) and [vLLM V1 performance optimization](../../../inference-optimization/vllm-optimization.html#mi300x-vllm-optimization) for
more information.

## Performance measurements[#](#performance-measurements)

To evaluate performance, the
[Performance results with AMD ROCm software](https://www.amd.com/en/developer/resources/rocm-hub/dev-ai/performance-results.html)
page provides reference throughput and latency measurements for inferencing
popular AI models.

Important

The performance data presented in
[Performance results with AMD ROCm software](https://www.amd.com/en/developer/resources/rocm-hub/dev-ai/performance-results.html)
only reflects the [latest version of this inference benchmarking environment](../vllm.html).
The listed measurements should not be interpreted as the peak performance achievable by AMD Instinct MI325X and MI300X GPUs or ROCm software.

## Advanced features and known issues[#](#advanced-features-and-known-issues)

For information on experimental features and known issues related to ROCm optimization efforts on vLLM,
see the developer’s guide at [ROCm/vllm](https://github.com/ROCm/vllm/tree/16d2b92ebcf90fe55cf73fa0b9329a6c9d3dede8/docs/dev-docker).

## System validation[#](#system-validation)

Before running AI workloads, it’s important to validate that your AMD hardware is configured correctly and performing optimally.

To optimize performance, disable automatic NUMA balancing. Otherwise, the GPU
might hang until the periodic balancing is finalized. For more information,
see the [system validation steps](../../../system-setup/prerequisite-system-validation.html#rocm-for-ai-system-optimization).

```
# disable automatic NUMA balancing
sh -c 'echo 0 > /proc/sys/kernel/numa_balancing'
# check if NUMA balancing is disabled (returns 0 if disabled)
cat /proc/sys/kernel/numa_balancing
0
```

To test for optimal performance, consult the recommended [System health benchmarks](../../../system-setup/system-health-check.html#rocm-for-ai-system-health-bench). This suite of tests will help you verify and fine-tune your
system’s configuration.

## Pull the Docker image[#](#pull-the-docker-image)

Download the [ROCm vLLM Docker image](https://hub.docker.com/layers/rocm/vllm/rocm6.3.1_vllm_0.8.5_20250513/images/sha256-5c8b4436dd0464119d9df2b44c745fadf81512f18ffb2f4b5dc235c71ebe26b4).
Use the following command to pull the Docker image from Docker Hub.

```
pull rocm/vllm:rocm6.3.1_vllm0.8.5_20250513
```

## Benchmarking[#](#benchmarking)

Once the setup is complete, choose between two options to reproduce the benchmark results:

Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local
directory and install the required packages on the host machine.

```
clone https://github.com/ROCm/MAD
cd MAD
pip install -r requirements.txt
```

Use this command to run the performance benchmark test on the [Llama 3.1 8B](https://huggingface.co/meta-llama/Llama-3.1-8B) model
using one GPU with the `float16`

data type on the host machine.

```
export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
python3 tools/run_models.py --tags pyt_vllm_llama-3.1-8b --keep-model-dir --live-output --timeout 28800
```

MAD launches a Docker container with the name
`container_ci-pyt_vllm_llama-3.1-8b`

. The latency and throughput reports of the
model are collected in the following path: `~/MAD/reports_float16/`

.

Although the [available models](#vllm-benchmark-available-models-v085-20250513) are preconfigured
to collect latency and throughput performance data, you can also change the benchmarking
parameters. See the standalone benchmarking tab for more information.

Run the vLLM benchmark tool independently by starting the
[Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.3.1_vllm_0.8.5_20250513/images/sha256-5c8b4436dd0464119d9df2b44c745fadf81512f18ffb2f4b5dc235c71ebe26b4)
as shown in the following snippet.


In the Docker container, clone the ROCm MAD repository and navigate to the
benchmark scripts directory at `~/MAD/scripts/vllm`

.

```
git clone https://github.com/ROCm/MAD
cd MAD/scripts/vllm
```

To start the benchmark, use the following command with the appropriate options.


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
1 or 8 |
Number of GPUs |
|
|
Data type |

Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don’t need to specify them with this script.

Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.


Here are some examples of running the benchmark with various options.

Latency benchmark

Use this command to benchmark the latency of the Llama 3.1 8B model on eight GPUs with

`float16`

precision../vllm_benchmark_report.sh -s latency -m meta-llama/Llama-3.1-8B-Instruct -g 8 -d float16

Find the latency report at

`./reports_float16_vllm_rocm6.3.1/summary/Llama-3.1-8B-Instruct_latency_report.csv`

.Throughput benchmark

Use this command to benchmark the throughput of the Llama 3.1 8B model on eight GPUs with

`float16`

precision.-s throughput -m meta-llama/Llama-3.1-8B-Instruct -g 8 -d float16

Find the throughput report at

`./reports_float16_vllm_rocm6.3.1/summary/Llama-3.1-8B-Instruct_throughput_report.csv`

.

Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local
directory and install the required packages on the host machine.

```
clone https://github.com/ROCm/MAD
cd MAD
pip install -r requirements.txt
```

Use this command to run the performance benchmark test on the [Llama 3.1 70B](https://huggingface.co/meta-llama/Llama-3.1-70B-Instruct) model
using one GPU with the `float16`

data type on the host machine.

```
export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
python3 tools/run_models.py --tags pyt_vllm_llama-3.1-70b --keep-model-dir --live-output --timeout 28800
```

MAD launches a Docker container with the name
`container_ci-pyt_vllm_llama-3.1-70b`

. The latency and throughput reports of the
model are collected in the following path: `~/MAD/reports_float16/`

.

Although the [available models](#vllm-benchmark-available-models-v085-20250513) are preconfigured
to collect latency and throughput performance data, you can also change the benchmarking
parameters. See the standalone benchmarking tab for more information.

Run the vLLM benchmark tool independently by starting the
[Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.3.1_vllm_0.8.5_20250513/images/sha256-5c8b4436dd0464119d9df2b44c745fadf81512f18ffb2f4b5dc235c71ebe26b4)
as shown in the following snippet.


In the Docker container, clone the ROCm MAD repository and navigate to the
benchmark scripts directory at `~/MAD/scripts/vllm`

.

```
git clone https://github.com/ROCm/MAD
cd MAD/scripts/vllm
```

To start the benchmark, use the following command with the appropriate options.


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
1 or 8 |
Number of GPUs |
|
|
Data type |

Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don’t need to specify them with this script.

Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.


Here are some examples of running the benchmark with various options.

Latency benchmark

Use this command to benchmark the latency of the Llama 3.1 70B model on eight GPUs with

`float16`

precision../vllm_benchmark_report.sh -s latency -m meta-llama/Llama-3.1-70B-Instruct -g 8 -d float16

Find the latency report at

`./reports_float16_vllm_rocm6.3.1/summary/Llama-3.1-70B-Instruct_latency_report.csv`

.Throughput benchmark

Use this command to benchmark the throughput of the Llama 3.1 70B model on eight GPUs with

`float16`

precision.-s throughput -m meta-llama/Llama-3.1-70B-Instruct -g 8 -d float16

Find the throughput report at

`./reports_float16_vllm_rocm6.3.1/summary/Llama-3.1-70B-Instruct_throughput_report.csv`

.

Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local
directory and install the required packages on the host machine.

```
clone https://github.com/ROCm/MAD
cd MAD
pip install -r requirements.txt
```

Use this command to run the performance benchmark test on the [Llama 3.1 405B](https://huggingface.co/meta-llama/Llama-3.1-405B-Instruct) model
using one GPU with the `float16`

data type on the host machine.

```
export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
python3 tools/run_models.py --tags pyt_vllm_llama-3.1-405b --keep-model-dir --live-output --timeout 28800
```

MAD launches a Docker container with the name
`container_ci-pyt_vllm_llama-3.1-405b`

. The latency and throughput reports of the
model are collected in the following path: `~/MAD/reports_float16/`

.

Although the [available models](#vllm-benchmark-available-models-v085-20250513) are preconfigured
to collect latency and throughput performance data, you can also change the benchmarking
parameters. See the standalone benchmarking tab for more information.

Run the vLLM benchmark tool independently by starting the
[Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.3.1_vllm_0.8.5_20250513/images/sha256-5c8b4436dd0464119d9df2b44c745fadf81512f18ffb2f4b5dc235c71ebe26b4)
as shown in the following snippet.


In the Docker container, clone the ROCm MAD repository and navigate to the
benchmark scripts directory at `~/MAD/scripts/vllm`

.

```
git clone https://github.com/ROCm/MAD
cd MAD/scripts/vllm
```

To start the benchmark, use the following command with the appropriate options.


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
1 or 8 |
Number of GPUs |
|
|
Data type |

Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don’t need to specify them with this script.

Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.


Here are some examples of running the benchmark with various options.

Latency benchmark

Use this command to benchmark the latency of the Llama 3.1 405B model on eight GPUs with

`float16`

precision../vllm_benchmark_report.sh -s latency -m meta-llama/Llama-3.1-405B-Instruct -g 8 -d float16

Find the latency report at

`./reports_float16_vllm_rocm6.3.1/summary/Llama-3.1-405B-Instruct_latency_report.csv`

.Throughput benchmark

Use this command to benchmark the throughput of the Llama 3.1 405B model on eight GPUs with

`float16`

precision.-s throughput -m meta-llama/Llama-3.1-405B-Instruct -g 8 -d float16

Find the throughput report at

`./reports_float16_vllm_rocm6.3.1/summary/Llama-3.1-405B-Instruct_throughput_report.csv`

.

Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local
directory and install the required packages on the host machine.

```
clone https://github.com/ROCm/MAD
cd MAD
pip install -r requirements.txt
```

Use this command to run the performance benchmark test on the [Llama 3.2 11B Vision](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct) model
using one GPU with the `float16`

data type on the host machine.

```
export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
python3 tools/run_models.py --tags pyt_vllm_llama-3.2-11b-vision-instruct --keep-model-dir --live-output --timeout 28800
```

MAD launches a Docker container with the name
`container_ci-pyt_vllm_llama-3.2-11b-vision-instruct`

. The latency and throughput reports of the
model are collected in the following path: `~/MAD/reports_float16/`

.

Although the [available models](#vllm-benchmark-available-models-v085-20250513) are preconfigured
to collect latency and throughput performance data, you can also change the benchmarking
parameters. See the standalone benchmarking tab for more information.

Run the vLLM benchmark tool independently by starting the
[Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.3.1_vllm_0.8.5_20250513/images/sha256-5c8b4436dd0464119d9df2b44c745fadf81512f18ffb2f4b5dc235c71ebe26b4)
as shown in the following snippet.


In the Docker container, clone the ROCm MAD repository and navigate to the
benchmark scripts directory at `~/MAD/scripts/vllm`

.

```
git clone https://github.com/ROCm/MAD
cd MAD/scripts/vllm
```

To start the benchmark, use the following command with the appropriate options.


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
1 or 8 |
Number of GPUs |
|
|
Data type |

Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don’t need to specify them with this script.

Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.


Here are some examples of running the benchmark with various options.

Latency benchmark

Use this command to benchmark the latency of the Llama 3.2 11B Vision model on eight GPUs with

`float16`

precision../vllm_benchmark_report.sh -s latency -m meta-llama/Llama-3.2-11B-Vision-Instruct -g 8 -d float16

Find the latency report at

`./reports_float16_vllm_rocm6.3.1/summary/Llama-3.2-11B-Vision-Instruct_latency_report.csv`

.Throughput benchmark

Use this command to benchmark the throughput of the Llama 3.2 11B Vision model on eight GPUs with

`float16`

precision.-s throughput -m meta-llama/Llama-3.2-11B-Vision-Instruct -g 8 -d float16

Find the throughput report at

`./reports_float16_vllm_rocm6.3.1/summary/Llama-3.2-11B-Vision-Instruct_throughput_report.csv`

.

Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local
directory and install the required packages on the host machine.

```
clone https://github.com/ROCm/MAD
cd MAD
pip install -r requirements.txt
```

Use this command to run the performance benchmark test on the [Llama 2 7B](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf) model
using one GPU with the `float16`

data type on the host machine.

```
export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
python3 tools/run_models.py --tags pyt_vllm_llama-2-7b --keep-model-dir --live-output --timeout 28800
```

MAD launches a Docker container with the name
`container_ci-pyt_vllm_llama-2-7b`

. The latency and throughput reports of the
model are collected in the following path: `~/MAD/reports_float16/`

.

Although the [available models](#vllm-benchmark-available-models-v085-20250513) are preconfigured
to collect latency and throughput performance data, you can also change the benchmarking
parameters. See the standalone benchmarking tab for more information.

Run the vLLM benchmark tool independently by starting the
[Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.3.1_vllm_0.8.5_20250513/images/sha256-5c8b4436dd0464119d9df2b44c745fadf81512f18ffb2f4b5dc235c71ebe26b4)
as shown in the following snippet.


In the Docker container, clone the ROCm MAD repository and navigate to the
benchmark scripts directory at `~/MAD/scripts/vllm`

.

```
git clone https://github.com/ROCm/MAD
cd MAD/scripts/vllm
```

To start the benchmark, use the following command with the appropriate options.


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
1 or 8 |
Number of GPUs |
|
|
Data type |

Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don’t need to specify them with this script.

Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.


Here are some examples of running the benchmark with various options.

Latency benchmark

Use this command to benchmark the latency of the Llama 2 7B model on eight GPUs with

`float16`

precision../vllm_benchmark_report.sh -s latency -m meta-llama/Llama-2-7b-chat-hf -g 8 -d float16

Find the latency report at

`./reports_float16_vllm_rocm6.3.1/summary/Llama-2-7b-chat-hf_latency_report.csv`

.Throughput benchmark

Use this command to benchmark the throughput of the Llama 2 7B model on eight GPUs with

`float16`

precision.-s throughput -m meta-llama/Llama-2-7b-chat-hf -g 8 -d float16

Find the throughput report at

`./reports_float16_vllm_rocm6.3.1/summary/Llama-2-7b-chat-hf_throughput_report.csv`

.

Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local
directory and install the required packages on the host machine.

```
clone https://github.com/ROCm/MAD
cd MAD
pip install -r requirements.txt
```

Use this command to run the performance benchmark test on the [Llama 2 70B](https://huggingface.co/meta-llama/Llama-2-70b-chat-hf) model
using one GPU with the `float16`

data type on the host machine.

```
export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
python3 tools/run_models.py --tags pyt_vllm_llama-2-70b --keep-model-dir --live-output --timeout 28800
```

MAD launches a Docker container with the name
`container_ci-pyt_vllm_llama-2-70b`

. The latency and throughput reports of the
model are collected in the following path: `~/MAD/reports_float16/`

.

Although the [available models](#vllm-benchmark-available-models-v085-20250513) are preconfigured
to collect latency and throughput performance data, you can also change the benchmarking
parameters. See the standalone benchmarking tab for more information.

Run the vLLM benchmark tool independently by starting the
[Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.3.1_vllm_0.8.5_20250513/images/sha256-5c8b4436dd0464119d9df2b44c745fadf81512f18ffb2f4b5dc235c71ebe26b4)
as shown in the following snippet.


In the Docker container, clone the ROCm MAD repository and navigate to the
benchmark scripts directory at `~/MAD/scripts/vllm`

.

```
git clone https://github.com/ROCm/MAD
cd MAD/scripts/vllm
```

To start the benchmark, use the following command with the appropriate options.


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
1 or 8 |
Number of GPUs |
|
|
Data type |

Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don’t need to specify them with this script.

Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.


Here are some examples of running the benchmark with various options.

Latency benchmark

Use this command to benchmark the latency of the Llama 2 70B model on eight GPUs with

`float16`

precision../vllm_benchmark_report.sh -s latency -m meta-llama/Llama-2-70b-chat-hf -g 8 -d float16

Find the latency report at

`./reports_float16_vllm_rocm6.3.1/summary/Llama-2-70b-chat-hf_latency_report.csv`

.Throughput benchmark

Use this command to benchmark the throughput of the Llama 2 70B model on eight GPUs with

`float16`

precision.-s throughput -m meta-llama/Llama-2-70b-chat-hf -g 8 -d float16

Find the throughput report at

`./reports_float16_vllm_rocm6.3.1/summary/Llama-2-70b-chat-hf_throughput_report.csv`

.

Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local
directory and install the required packages on the host machine.

```
clone https://github.com/ROCm/MAD
cd MAD
pip install -r requirements.txt
```

Use this command to run the performance benchmark test on the [Llama 3.1 8B FP8](https://huggingface.co/amd/Llama-3.1-8B-Instruct-FP8-KV) model
using one GPU with the `float8`

data type on the host machine.

```
export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
python3 tools/run_models.py --tags pyt_vllm_llama-3.1-8b_fp8 --keep-model-dir --live-output --timeout 28800
```

MAD launches a Docker container with the name
`container_ci-pyt_vllm_llama-3.1-8b_fp8`

. The latency and throughput reports of the
model are collected in the following path: `~/MAD/reports_float8/`

.

Although the [available models](#vllm-benchmark-available-models-v085-20250513) are preconfigured
to collect latency and throughput performance data, you can also change the benchmarking
parameters. See the standalone benchmarking tab for more information.

Run the vLLM benchmark tool independently by starting the
[Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.3.1_vllm_0.8.5_20250513/images/sha256-5c8b4436dd0464119d9df2b44c745fadf81512f18ffb2f4b5dc235c71ebe26b4)
as shown in the following snippet.


In the Docker container, clone the ROCm MAD repository and navigate to the
benchmark scripts directory at `~/MAD/scripts/vllm`

.

```
git clone https://github.com/ROCm/MAD
cd MAD/scripts/vllm
```

To start the benchmark, use the following command with the appropriate options.


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
1 or 8 |
Number of GPUs |
|
|
Data type |

Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don’t need to specify them with this script.

Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.


Here are some examples of running the benchmark with various options.

Latency benchmark

Use this command to benchmark the latency of the Llama 3.1 8B FP8 model on eight GPUs with

`float8`

precision../vllm_benchmark_report.sh -s latency -m amd/Llama-3.1-8B-Instruct-FP8-KV -g 8 -d float8

Find the latency report at

`./reports_float8_vllm_rocm6.3.1/summary/Llama-3.1-8B-Instruct-FP8-KV_latency_report.csv`

.Throughput benchmark

Use this command to benchmark the throughput of the Llama 3.1 8B FP8 model on eight GPUs with

`float8`

precision.-s throughput -m amd/Llama-3.1-8B-Instruct-FP8-KV -g 8 -d float8

Find the throughput report at

`./reports_float8_vllm_rocm6.3.1/summary/Llama-3.1-8B-Instruct-FP8-KV_throughput_report.csv`

.

Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local
directory and install the required packages on the host machine.

```
clone https://github.com/ROCm/MAD
cd MAD
pip install -r requirements.txt
```

Use this command to run the performance benchmark test on the [Llama 3.1 70B FP8](https://huggingface.co/amd/Llama-3.1-70B-Instruct-FP8-KV) model
using one GPU with the `float8`

data type on the host machine.

```
export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
python3 tools/run_models.py --tags pyt_vllm_llama-3.1-70b_fp8 --keep-model-dir --live-output --timeout 28800
```

MAD launches a Docker container with the name
`container_ci-pyt_vllm_llama-3.1-70b_fp8`

. The latency and throughput reports of the
model are collected in the following path: `~/MAD/reports_float8/`

.

Although the [available models](#vllm-benchmark-available-models-v085-20250513) are preconfigured
to collect latency and throughput performance data, you can also change the benchmarking
parameters. See the standalone benchmarking tab for more information.

Run the vLLM benchmark tool independently by starting the
[Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.3.1_vllm_0.8.5_20250513/images/sha256-5c8b4436dd0464119d9df2b44c745fadf81512f18ffb2f4b5dc235c71ebe26b4)
as shown in the following snippet.


In the Docker container, clone the ROCm MAD repository and navigate to the
benchmark scripts directory at `~/MAD/scripts/vllm`

.

```
git clone https://github.com/ROCm/MAD
cd MAD/scripts/vllm
```

To start the benchmark, use the following command with the appropriate options.


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
1 or 8 |
Number of GPUs |
|
|
Data type |

Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don’t need to specify them with this script.

Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.


Here are some examples of running the benchmark with various options.

Latency benchmark

Use this command to benchmark the latency of the Llama 3.1 70B FP8 model on eight GPUs with

`float8`

precision../vllm_benchmark_report.sh -s latency -m amd/Llama-3.1-70B-Instruct-FP8-KV -g 8 -d float8

Find the latency report at

`./reports_float8_vllm_rocm6.3.1/summary/Llama-3.1-70B-Instruct-FP8-KV_latency_report.csv`

.Throughput benchmark

Use this command to benchmark the throughput of the Llama 3.1 70B FP8 model on eight GPUs with

`float8`

precision.-s throughput -m amd/Llama-3.1-70B-Instruct-FP8-KV -g 8 -d float8

Find the throughput report at

`./reports_float8_vllm_rocm6.3.1/summary/Llama-3.1-70B-Instruct-FP8-KV_throughput_report.csv`

.

Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local
directory and install the required packages on the host machine.

```
clone https://github.com/ROCm/MAD
cd MAD
pip install -r requirements.txt
```

Use this command to run the performance benchmark test on the [Llama 3.1 405B FP8](https://huggingface.co/amd/Llama-3.1-405B-Instruct-FP8-KV) model
using one GPU with the `float8`

data type on the host machine.

```
export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
python3 tools/run_models.py --tags pyt_vllm_llama-3.1-405b_fp8 --keep-model-dir --live-output --timeout 28800
```

MAD launches a Docker container with the name
`container_ci-pyt_vllm_llama-3.1-405b_fp8`

. The latency and throughput reports of the
model are collected in the following path: `~/MAD/reports_float8/`

.

Although the [available models](#vllm-benchmark-available-models-v085-20250513) are preconfigured
to collect latency and throughput performance data, you can also change the benchmarking
parameters. See the standalone benchmarking tab for more information.

Run the vLLM benchmark tool independently by starting the
[Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.3.1_vllm_0.8.5_20250513/images/sha256-5c8b4436dd0464119d9df2b44c745fadf81512f18ffb2f4b5dc235c71ebe26b4)
as shown in the following snippet.


In the Docker container, clone the ROCm MAD repository and navigate to the
benchmark scripts directory at `~/MAD/scripts/vllm`

.

```
git clone https://github.com/ROCm/MAD
cd MAD/scripts/vllm
```

To start the benchmark, use the following command with the appropriate options.


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
1 or 8 |
Number of GPUs |
|
|
Data type |

Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don’t need to specify them with this script.

Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.


Here are some examples of running the benchmark with various options.

Latency benchmark

Use this command to benchmark the latency of the Llama 3.1 405B FP8 model on eight GPUs with

`float8`

precision../vllm_benchmark_report.sh -s latency -m amd/Llama-3.1-405B-Instruct-FP8-KV -g 8 -d float8

Find the latency report at

`./reports_float8_vllm_rocm6.3.1/summary/Llama-3.1-405B-Instruct-FP8-KV_latency_report.csv`

.Throughput benchmark

Use this command to benchmark the throughput of the Llama 3.1 405B FP8 model on eight GPUs with

`float8`

precision.-s throughput -m amd/Llama-3.1-405B-Instruct-FP8-KV -g 8 -d float8

Find the throughput report at

`./reports_float8_vllm_rocm6.3.1/summary/Llama-3.1-405B-Instruct-FP8-KV_throughput_report.csv`

.

Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local
directory and install the required packages on the host machine.

```
clone https://github.com/ROCm/MAD
cd MAD
pip install -r requirements.txt
```

Use this command to run the performance benchmark test on the [Mixtral MoE 8x7B](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1) model
using one GPU with the `float16`

data type on the host machine.

```
export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
python3 tools/run_models.py --tags pyt_vllm_mixtral-8x7b --keep-model-dir --live-output --timeout 28800
```

MAD launches a Docker container with the name
`container_ci-pyt_vllm_mixtral-8x7b`

. The latency and throughput reports of the
model are collected in the following path: `~/MAD/reports_float16/`

.

Although the [available models](#vllm-benchmark-available-models-v085-20250513) are preconfigured
to collect latency and throughput performance data, you can also change the benchmarking
parameters. See the standalone benchmarking tab for more information.

Run the vLLM benchmark tool independently by starting the
[Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.3.1_vllm_0.8.5_20250513/images/sha256-5c8b4436dd0464119d9df2b44c745fadf81512f18ffb2f4b5dc235c71ebe26b4)
as shown in the following snippet.


In the Docker container, clone the ROCm MAD repository and navigate to the
benchmark scripts directory at `~/MAD/scripts/vllm`

.

```
git clone https://github.com/ROCm/MAD
cd MAD/scripts/vllm
```

To start the benchmark, use the following command with the appropriate options.


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
1 or 8 |
Number of GPUs |
|
|
Data type |

Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don’t need to specify them with this script.

Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.


Here are some examples of running the benchmark with various options.

Latency benchmark

Use this command to benchmark the latency of the Mixtral MoE 8x7B model on eight GPUs with

`float16`

precision../vllm_benchmark_report.sh -s latency -m mistralai/Mixtral-8x7B-Instruct-v0.1 -g 8 -d float16

Find the latency report at

`./reports_float16_vllm_rocm6.3.1/summary/Mixtral-8x7B-Instruct-v0.1_latency_report.csv`

.Throughput benchmark

Use this command to benchmark the throughput of the Mixtral MoE 8x7B model on eight GPUs with

`float16`

precision.-s throughput -m mistralai/Mixtral-8x7B-Instruct-v0.1 -g 8 -d float16

Find the throughput report at

`./reports_float16_vllm_rocm6.3.1/summary/Mixtral-8x7B-Instruct-v0.1_throughput_report.csv`

.

Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local
directory and install the required packages on the host machine.

```
clone https://github.com/ROCm/MAD
cd MAD
pip install -r requirements.txt
```

Use this command to run the performance benchmark test on the [Mixtral MoE 8x22B](https://huggingface.co/mistralai/Mixtral-8x22B-Instruct-v0.1) model
using one GPU with the `float16`

data type on the host machine.

```
export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
python3 tools/run_models.py --tags pyt_vllm_mixtral-8x22b --keep-model-dir --live-output --timeout 28800
```

MAD launches a Docker container with the name
`container_ci-pyt_vllm_mixtral-8x22b`

. The latency and throughput reports of the
model are collected in the following path: `~/MAD/reports_float16/`

.

Although the [available models](#vllm-benchmark-available-models-v085-20250513) are preconfigured
to collect latency and throughput performance data, you can also change the benchmarking
parameters. See the standalone benchmarking tab for more information.

Run the vLLM benchmark tool independently by starting the
[Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.3.1_vllm_0.8.5_20250513/images/sha256-5c8b4436dd0464119d9df2b44c745fadf81512f18ffb2f4b5dc235c71ebe26b4)
as shown in the following snippet.


In the Docker container, clone the ROCm MAD repository and navigate to the
benchmark scripts directory at `~/MAD/scripts/vllm`

.

```
git clone https://github.com/ROCm/MAD
cd MAD/scripts/vllm
```

To start the benchmark, use the following command with the appropriate options.


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
1 or 8 |
Number of GPUs |
|
|
Data type |

Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don’t need to specify them with this script.

Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.


Here are some examples of running the benchmark with various options.

Latency benchmark

Use this command to benchmark the latency of the Mixtral MoE 8x22B model on eight GPUs with

`float16`

precision../vllm_benchmark_report.sh -s latency -m mistralai/Mixtral-8x22B-Instruct-v0.1 -g 8 -d float16

Find the latency report at

`./reports_float16_vllm_rocm6.3.1/summary/Mixtral-8x22B-Instruct-v0.1_latency_report.csv`

.Throughput benchmark

Use this command to benchmark the throughput of the Mixtral MoE 8x22B model on eight GPUs with

`float16`

precision.-s throughput -m mistralai/Mixtral-8x22B-Instruct-v0.1 -g 8 -d float16

Find the throughput report at

`./reports_float16_vllm_rocm6.3.1/summary/Mixtral-8x22B-Instruct-v0.1_throughput_report.csv`

.

Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local
directory and install the required packages on the host machine.

```
clone https://github.com/ROCm/MAD
cd MAD
pip install -r requirements.txt
```

Use this command to run the performance benchmark test on the [Mistral 7B](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3) model
using one GPU with the `float16`

data type on the host machine.

```
export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
python3 tools/run_models.py --tags pyt_vllm_mistral-7b --keep-model-dir --live-output --timeout 28800
```

MAD launches a Docker container with the name
`container_ci-pyt_vllm_mistral-7b`

. The latency and throughput reports of the
model are collected in the following path: `~/MAD/reports_float16/`

.

Although the [available models](#vllm-benchmark-available-models-v085-20250513) are preconfigured
to collect latency and throughput performance data, you can also change the benchmarking
parameters. See the standalone benchmarking tab for more information.

Run the vLLM benchmark tool independently by starting the
[Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.3.1_vllm_0.8.5_20250513/images/sha256-5c8b4436dd0464119d9df2b44c745fadf81512f18ffb2f4b5dc235c71ebe26b4)
as shown in the following snippet.


In the Docker container, clone the ROCm MAD repository and navigate to the
benchmark scripts directory at `~/MAD/scripts/vllm`

.

```
git clone https://github.com/ROCm/MAD
cd MAD/scripts/vllm
```

To start the benchmark, use the following command with the appropriate options.


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
1 or 8 |
Number of GPUs |
|
|
Data type |

Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don’t need to specify them with this script.

Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.


Here are some examples of running the benchmark with various options.

Latency benchmark

Use this command to benchmark the latency of the Mistral 7B model on eight GPUs with

`float16`

precision../vllm_benchmark_report.sh -s latency -m mistralai/Mistral-7B-Instruct-v0.3 -g 8 -d float16

Find the latency report at

`./reports_float16_vllm_rocm6.3.1/summary/Mistral-7B-Instruct-v0.3_latency_report.csv`

.Throughput benchmark

Use this command to benchmark the throughput of the Mistral 7B model on eight GPUs with

`float16`

precision.-s throughput -m mistralai/Mistral-7B-Instruct-v0.3 -g 8 -d float16

Find the throughput report at

`./reports_float16_vllm_rocm6.3.1/summary/Mistral-7B-Instruct-v0.3_throughput_report.csv`

.

Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local
directory and install the required packages on the host machine.

```
clone https://github.com/ROCm/MAD
cd MAD
pip install -r requirements.txt
```

Use this command to run the performance benchmark test on the [Mixtral MoE 8x7B FP8](https://huggingface.co/amd/Mixtral-8x7B-Instruct-v0.1-FP8-KV) model
using one GPU with the `float8`

data type on the host machine.

```
export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
python3 tools/run_models.py --tags pyt_vllm_mixtral-8x7b_fp8 --keep-model-dir --live-output --timeout 28800
```

MAD launches a Docker container with the name
`container_ci-pyt_vllm_mixtral-8x7b_fp8`

. The latency and throughput reports of the
model are collected in the following path: `~/MAD/reports_float8/`

.

Although the [available models](#vllm-benchmark-available-models-v085-20250513) are preconfigured
to collect latency and throughput performance data, you can also change the benchmarking
parameters. See the standalone benchmarking tab for more information.

Run the vLLM benchmark tool independently by starting the
[Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.3.1_vllm_0.8.5_20250513/images/sha256-5c8b4436dd0464119d9df2b44c745fadf81512f18ffb2f4b5dc235c71ebe26b4)
as shown in the following snippet.


In the Docker container, clone the ROCm MAD repository and navigate to the
benchmark scripts directory at `~/MAD/scripts/vllm`

.

```
git clone https://github.com/ROCm/MAD
cd MAD/scripts/vllm
```

To start the benchmark, use the following command with the appropriate options.


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
1 or 8 |
Number of GPUs |
|
|
Data type |

Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don’t need to specify them with this script.

Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.


Here are some examples of running the benchmark with various options.

Latency benchmark

Use this command to benchmark the latency of the Mixtral MoE 8x7B FP8 model on eight GPUs with

`float8`

precision../vllm_benchmark_report.sh -s latency -m amd/Mixtral-8x7B-Instruct-v0.1-FP8-KV -g 8 -d float8

Find the latency report at

`./reports_float8_vllm_rocm6.3.1/summary/Mixtral-8x7B-Instruct-v0.1-FP8-KV_latency_report.csv`

.Throughput benchmark

Use this command to benchmark the throughput of the Mixtral MoE 8x7B FP8 model on eight GPUs with

`float8`

precision.-s throughput -m amd/Mixtral-8x7B-Instruct-v0.1-FP8-KV -g 8 -d float8

Find the throughput report at

`./reports_float8_vllm_rocm6.3.1/summary/Mixtral-8x7B-Instruct-v0.1-FP8-KV_throughput_report.csv`

.

Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local
directory and install the required packages on the host machine.

```
clone https://github.com/ROCm/MAD
cd MAD
pip install -r requirements.txt
```

Use this command to run the performance benchmark test on the [Mixtral MoE 8x22B FP8](https://huggingface.co/amd/Mixtral-8x22B-Instruct-v0.1-FP8-KV) model
using one GPU with the `float8`

data type on the host machine.

```
export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
python3 tools/run_models.py --tags pyt_vllm_mixtral-8x22b_fp8 --keep-model-dir --live-output --timeout 28800
```

MAD launches a Docker container with the name
`container_ci-pyt_vllm_mixtral-8x22b_fp8`

. The latency and throughput reports of the
model are collected in the following path: `~/MAD/reports_float8/`

.

Although the [available models](#vllm-benchmark-available-models-v085-20250513) are preconfigured
to collect latency and throughput performance data, you can also change the benchmarking
parameters. See the standalone benchmarking tab for more information.

Run the vLLM benchmark tool independently by starting the
[Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.3.1_vllm_0.8.5_20250513/images/sha256-5c8b4436dd0464119d9df2b44c745fadf81512f18ffb2f4b5dc235c71ebe26b4)
as shown in the following snippet.


In the Docker container, clone the ROCm MAD repository and navigate to the
benchmark scripts directory at `~/MAD/scripts/vllm`

.

```
git clone https://github.com/ROCm/MAD
cd MAD/scripts/vllm
```

To start the benchmark, use the following command with the appropriate options.


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
1 or 8 |
Number of GPUs |
|
|
Data type |

Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don’t need to specify them with this script.

Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.


Here are some examples of running the benchmark with various options.

Latency benchmark

Use this command to benchmark the latency of the Mixtral MoE 8x22B FP8 model on eight GPUs with

`float8`

precision../vllm_benchmark_report.sh -s latency -m amd/Mixtral-8x22B-Instruct-v0.1-FP8-KV -g 8 -d float8

Find the latency report at

`./reports_float8_vllm_rocm6.3.1/summary/Mixtral-8x22B-Instruct-v0.1-FP8-KV_latency_report.csv`

.Throughput benchmark

Use this command to benchmark the throughput of the Mixtral MoE 8x22B FP8 model on eight GPUs with

`float8`

precision.-s throughput -m amd/Mixtral-8x22B-Instruct-v0.1-FP8-KV -g 8 -d float8

Find the throughput report at

`./reports_float8_vllm_rocm6.3.1/summary/Mixtral-8x22B-Instruct-v0.1-FP8-KV_throughput_report.csv`

.

Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local
directory and install the required packages on the host machine.

```
clone https://github.com/ROCm/MAD
cd MAD
pip install -r requirements.txt
```

Use this command to run the performance benchmark test on the [Mistral 7B FP8](https://huggingface.co/amd/Mistral-7B-v0.1-FP8-KV) model
using one GPU with the `float8`

data type on the host machine.

```
export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
python3 tools/run_models.py --tags pyt_vllm_mistral-7b_fp8 --keep-model-dir --live-output --timeout 28800
```

MAD launches a Docker container with the name
`container_ci-pyt_vllm_mistral-7b_fp8`

. The latency and throughput reports of the
model are collected in the following path: `~/MAD/reports_float8/`

.

Although the [available models](#vllm-benchmark-available-models-v085-20250513) are preconfigured
to collect latency and throughput performance data, you can also change the benchmarking
parameters. See the standalone benchmarking tab for more information.

Run the vLLM benchmark tool independently by starting the
[Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.3.1_vllm_0.8.5_20250513/images/sha256-5c8b4436dd0464119d9df2b44c745fadf81512f18ffb2f4b5dc235c71ebe26b4)
as shown in the following snippet.


In the Docker container, clone the ROCm MAD repository and navigate to the
benchmark scripts directory at `~/MAD/scripts/vllm`

.

```
git clone https://github.com/ROCm/MAD
cd MAD/scripts/vllm
```

To start the benchmark, use the following command with the appropriate options.


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
1 or 8 |
Number of GPUs |
|
|
Data type |

Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don’t need to specify them with this script.

Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.


Here are some examples of running the benchmark with various options.

Latency benchmark

Use this command to benchmark the latency of the Mistral 7B FP8 model on eight GPUs with

`float8`

precision../vllm_benchmark_report.sh -s latency -m amd/Mistral-7B-v0.1-FP8-KV -g 8 -d float8

Find the latency report at

`./reports_float8_vllm_rocm6.3.1/summary/Mistral-7B-v0.1-FP8-KV_latency_report.csv`

.Throughput benchmark

Use this command to benchmark the throughput of the Mistral 7B FP8 model on eight GPUs with

`float8`

precision.-s throughput -m amd/Mistral-7B-v0.1-FP8-KV -g 8 -d float8

Find the throughput report at

`./reports_float8_vllm_rocm6.3.1/summary/Mistral-7B-v0.1-FP8-KV_throughput_report.csv`

.

Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local
directory and install the required packages on the host machine.

```
clone https://github.com/ROCm/MAD
cd MAD
pip install -r requirements.txt
```

Use this command to run the performance benchmark test on the [Qwen2 7B](https://huggingface.co/Qwen/Qwen2-7B-Instruct) model
using one GPU with the `float16`

data type on the host machine.

```
export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
python3 tools/run_models.py --tags pyt_vllm_qwen2-7b --keep-model-dir --live-output --timeout 28800
```

MAD launches a Docker container with the name
`container_ci-pyt_vllm_qwen2-7b`

. The latency and throughput reports of the
model are collected in the following path: `~/MAD/reports_float16/`

.

Although the [available models](#vllm-benchmark-available-models-v085-20250513) are preconfigured
to collect latency and throughput performance data, you can also change the benchmarking
parameters. See the standalone benchmarking tab for more information.

Run the vLLM benchmark tool independently by starting the
[Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.3.1_vllm_0.8.5_20250513/images/sha256-5c8b4436dd0464119d9df2b44c745fadf81512f18ffb2f4b5dc235c71ebe26b4)
as shown in the following snippet.


In the Docker container, clone the ROCm MAD repository and navigate to the
benchmark scripts directory at `~/MAD/scripts/vllm`

.

```
git clone https://github.com/ROCm/MAD
cd MAD/scripts/vllm
```

To start the benchmark, use the following command with the appropriate options.


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
1 or 8 |
Number of GPUs |
|
|
Data type |

Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don’t need to specify them with this script.

Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.


Here are some examples of running the benchmark with various options.

Latency benchmark

Use this command to benchmark the latency of the Qwen2 7B model on eight GPUs with

`float16`

precision../vllm_benchmark_report.sh -s latency -m Qwen/Qwen2-7B-Instruct -g 8 -d float16

Find the latency report at

`./reports_float16_vllm_rocm6.3.1/summary/Qwen2-7B-Instruct_latency_report.csv`

.Throughput benchmark

Use this command to benchmark the throughput of the Qwen2 7B model on eight GPUs with

`float16`

precision.-s throughput -m Qwen/Qwen2-7B-Instruct -g 8 -d float16

Find the throughput report at

`./reports_float16_vllm_rocm6.3.1/summary/Qwen2-7B-Instruct_throughput_report.csv`

.

Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local
directory and install the required packages on the host machine.

```
clone https://github.com/ROCm/MAD
cd MAD
pip install -r requirements.txt
```

Use this command to run the performance benchmark test on the [Qwen2 72B](https://huggingface.co/Qwen/Qwen2-72B-Instruct) model
using one GPU with the `float16`

data type on the host machine.

```
export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
python3 tools/run_models.py --tags pyt_vllm_qwen2-72b --keep-model-dir --live-output --timeout 28800
```

MAD launches a Docker container with the name
`container_ci-pyt_vllm_qwen2-72b`

. The latency and throughput reports of the
model are collected in the following path: `~/MAD/reports_float16/`

.

Although the [available models](#vllm-benchmark-available-models-v085-20250513) are preconfigured
to collect latency and throughput performance data, you can also change the benchmarking
parameters. See the standalone benchmarking tab for more information.

Run the vLLM benchmark tool independently by starting the
[Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.3.1_vllm_0.8.5_20250513/images/sha256-5c8b4436dd0464119d9df2b44c745fadf81512f18ffb2f4b5dc235c71ebe26b4)
as shown in the following snippet.


In the Docker container, clone the ROCm MAD repository and navigate to the
benchmark scripts directory at `~/MAD/scripts/vllm`

.

```
git clone https://github.com/ROCm/MAD
cd MAD/scripts/vllm
```

To start the benchmark, use the following command with the appropriate options.


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
1 or 8 |
Number of GPUs |
|
|
Data type |

Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don’t need to specify them with this script.

Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.


Here are some examples of running the benchmark with various options.

Latency benchmark

Use this command to benchmark the latency of the Qwen2 72B model on eight GPUs with

`float16`

precision../vllm_benchmark_report.sh -s latency -m Qwen/Qwen2-72B-Instruct -g 8 -d float16

Find the latency report at

`./reports_float16_vllm_rocm6.3.1/summary/Qwen2-72B-Instruct_latency_report.csv`

.Throughput benchmark

Use this command to benchmark the throughput of the Qwen2 72B model on eight GPUs with

`float16`

precision.-s throughput -m Qwen/Qwen2-72B-Instruct -g 8 -d float16

Find the throughput report at

`./reports_float16_vllm_rocm6.3.1/summary/Qwen2-72B-Instruct_throughput_report.csv`

.

Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local
directory and install the required packages on the host machine.

```
clone https://github.com/ROCm/MAD
cd MAD
pip install -r requirements.txt
```

Use this command to run the performance benchmark test on the [QwQ-32B](https://huggingface.co/Qwen/QwQ-32B) model
using one GPU with the `float16`

data type on the host machine.

```
export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
python3 tools/run_models.py --tags pyt_vllm_qwq-32b --keep-model-dir --live-output --timeout 28800
```

MAD launches a Docker container with the name
`container_ci-pyt_vllm_qwq-32b`

. The latency and throughput reports of the
model are collected in the following path: `~/MAD/reports_float16/`

.

Although the [available models](#vllm-benchmark-available-models-v085-20250513) are preconfigured
to collect latency and throughput performance data, you can also change the benchmarking
parameters. See the standalone benchmarking tab for more information.

Note

For improved performance, consider enabling [PyTorch TunableOp](../../../inference-optimization/workload.html#mi300x-tunableop).
TunableOp automatically explores different implementations and configurations of certain PyTorch
operators to find the fastest one for your hardware.

By default, `pyt_vllm_qwq-32b`

runs with TunableOp disabled
(see
[ROCm/MAD](https://github.com/ROCm/MAD/blob/develop/models.json)). To
enable it, edit the default run behavior in the `models.json`

configuration before running inference – update the model’s run
`args`

by changing `--tunableop off`

to `--tunableop on`

.

Enabling TunableOp triggers a two-pass run – a warm-up followed by the performance-collection run.

Run the vLLM benchmark tool independently by starting the
[Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.3.1_vllm_0.8.5_20250513/images/sha256-5c8b4436dd0464119d9df2b44c745fadf81512f18ffb2f4b5dc235c71ebe26b4)
as shown in the following snippet.


In the Docker container, clone the ROCm MAD repository and navigate to the
benchmark scripts directory at `~/MAD/scripts/vllm`

.

```
git clone https://github.com/ROCm/MAD
cd MAD/scripts/vllm
```

To start the benchmark, use the following command with the appropriate options.


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
1 or 8 |
Number of GPUs |
|
|
Data type |

Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don’t need to specify them with this script.

Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.


Here are some examples of running the benchmark with various options.

Latency benchmark

Use this command to benchmark the latency of the QwQ-32B model on eight GPUs with

`float16`

precision../vllm_benchmark_report.sh -s latency -m Qwen/QwQ-32B -g 8 -d float16

Find the latency report at

`./reports_float16_vllm_rocm6.3.1/summary/QwQ-32B_latency_report.csv`

.Throughput benchmark

Use this command to benchmark the throughput of the QwQ-32B model on eight GPUs with

`float16`

precision.-s throughput -m Qwen/QwQ-32B -g 8 -d float16

Find the throughput report at

`./reports_float16_vllm_rocm6.3.1/summary/QwQ-32B_throughput_report.csv`

.

Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local
directory and install the required packages on the host machine.

```
clone https://github.com/ROCm/MAD
cd MAD
pip install -r requirements.txt
```

Use this command to run the performance benchmark test on the [DBRX Instruct](https://huggingface.co/databricks/dbrx-instruct) model
using one GPU with the `float16`

data type on the host machine.

```
export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
python3 tools/run_models.py --tags pyt_vllm_dbrx-instruct --keep-model-dir --live-output --timeout 28800
```

MAD launches a Docker container with the name
`container_ci-pyt_vllm_dbrx-instruct`

. The latency and throughput reports of the
model are collected in the following path: `~/MAD/reports_float16/`

.

Although the [available models](#vllm-benchmark-available-models-v085-20250513) are preconfigured
to collect latency and throughput performance data, you can also change the benchmarking
parameters. See the standalone benchmarking tab for more information.

Run the vLLM benchmark tool independently by starting the
[Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.3.1_vllm_0.8.5_20250513/images/sha256-5c8b4436dd0464119d9df2b44c745fadf81512f18ffb2f4b5dc235c71ebe26b4)
as shown in the following snippet.


In the Docker container, clone the ROCm MAD repository and navigate to the
benchmark scripts directory at `~/MAD/scripts/vllm`

.

```
git clone https://github.com/ROCm/MAD
cd MAD/scripts/vllm
```

To start the benchmark, use the following command with the appropriate options.


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
1 or 8 |
Number of GPUs |
|
|
Data type |

Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don’t need to specify them with this script.

Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.


Here are some examples of running the benchmark with various options.

Latency benchmark

Use this command to benchmark the latency of the DBRX Instruct model on eight GPUs with

`float16`

precision../vllm_benchmark_report.sh -s latency -m databricks/dbrx-instruct -g 8 -d float16

Find the latency report at

`./reports_float16_vllm_rocm6.3.1/summary/dbrx-instruct_latency_report.csv`

.Throughput benchmark

Use this command to benchmark the throughput of the DBRX Instruct model on eight GPUs with

`float16`

precision.-s throughput -m databricks/dbrx-instruct -g 8 -d float16

Find the throughput report at

`./reports_float16_vllm_rocm6.3.1/summary/dbrx-instruct_throughput_report.csv`

.

Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local
directory and install the required packages on the host machine.

```
clone https://github.com/ROCm/MAD
cd MAD
pip install -r requirements.txt
```

Use this command to run the performance benchmark test on the [DBRX Instruct FP8](https://huggingface.co/amd/dbrx-instruct-FP8-KV) model
using one GPU with the `float8`

data type on the host machine.

```
export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
python3 tools/run_models.py --tags pyt_vllm_dbrx_fp8 --keep-model-dir --live-output --timeout 28800
```

MAD launches a Docker container with the name
`container_ci-pyt_vllm_dbrx_fp8`

. The latency and throughput reports of the
model are collected in the following path: `~/MAD/reports_float8/`

.

Although the [available models](#vllm-benchmark-available-models-v085-20250513) are preconfigured
to collect latency and throughput performance data, you can also change the benchmarking
parameters. See the standalone benchmarking tab for more information.

Run the vLLM benchmark tool independently by starting the
[Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.3.1_vllm_0.8.5_20250513/images/sha256-5c8b4436dd0464119d9df2b44c745fadf81512f18ffb2f4b5dc235c71ebe26b4)
as shown in the following snippet.


In the Docker container, clone the ROCm MAD repository and navigate to the
benchmark scripts directory at `~/MAD/scripts/vllm`

.

```
git clone https://github.com/ROCm/MAD
cd MAD/scripts/vllm
```

To start the benchmark, use the following command with the appropriate options.


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
1 or 8 |
Number of GPUs |
|
|
Data type |

Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don’t need to specify them with this script.

Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.


Here are some examples of running the benchmark with various options.

Latency benchmark

Use this command to benchmark the latency of the DBRX Instruct FP8 model on eight GPUs with

`float8`

precision../vllm_benchmark_report.sh -s latency -m amd/dbrx-instruct-FP8-KV -g 8 -d float8

Find the latency report at

`./reports_float8_vllm_rocm6.3.1/summary/dbrx-instruct-FP8-KV_latency_report.csv`

.Throughput benchmark

Use this command to benchmark the throughput of the DBRX Instruct FP8 model on eight GPUs with

`float8`

precision.-s throughput -m amd/dbrx-instruct-FP8-KV -g 8 -d float8

Find the throughput report at

`./reports_float8_vllm_rocm6.3.1/summary/dbrx-instruct-FP8-KV_throughput_report.csv`

.

Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local
directory and install the required packages on the host machine.

```
clone https://github.com/ROCm/MAD
cd MAD
pip install -r requirements.txt
```

Use this command to run the performance benchmark test on the [Gemma 2 27B](https://huggingface.co/google/gemma-2-27b) model
using one GPU with the `float16`

data type on the host machine.

```
export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
python3 tools/run_models.py --tags pyt_vllm_gemma-2-27b --keep-model-dir --live-output --timeout 28800
```

MAD launches a Docker container with the name
`container_ci-pyt_vllm_gemma-2-27b`

. The latency and throughput reports of the
model are collected in the following path: `~/MAD/reports_float16/`

.

Although the [available models](#vllm-benchmark-available-models-v085-20250513) are preconfigured
to collect latency and throughput performance data, you can also change the benchmarking
parameters. See the standalone benchmarking tab for more information.

Run the vLLM benchmark tool independently by starting the
[Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.3.1_vllm_0.8.5_20250513/images/sha256-5c8b4436dd0464119d9df2b44c745fadf81512f18ffb2f4b5dc235c71ebe26b4)
as shown in the following snippet.


In the Docker container, clone the ROCm MAD repository and navigate to the
benchmark scripts directory at `~/MAD/scripts/vllm`

.

```
git clone https://github.com/ROCm/MAD
cd MAD/scripts/vllm
```

To start the benchmark, use the following command with the appropriate options.


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
1 or 8 |
Number of GPUs |
|
|
Data type |

Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don’t need to specify them with this script.

Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.


Here are some examples of running the benchmark with various options.

Latency benchmark

Use this command to benchmark the latency of the Gemma 2 27B model on eight GPUs with

`float16`

precision../vllm_benchmark_report.sh -s latency -m google/gemma-2-27b -g 8 -d float16

Find the latency report at

`./reports_float16_vllm_rocm6.3.1/summary/gemma-2-27b_latency_report.csv`

.Throughput benchmark

Use this command to benchmark the throughput of the Gemma 2 27B model on eight GPUs with

`float16`

precision.-s throughput -m google/gemma-2-27b -g 8 -d float16

Find the throughput report at

`./reports_float16_vllm_rocm6.3.1/summary/gemma-2-27b_throughput_report.csv`

.

Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local
directory and install the required packages on the host machine.

```
clone https://github.com/ROCm/MAD
cd MAD
pip install -r requirements.txt
```

Use this command to run the performance benchmark test on the [C4AI Command R+ 08-2024](https://huggingface.co/CohereForAI/c4ai-command-r-plus-08-2024) model
using one GPU with the `float16`

data type on the host machine.

```
export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
python3 tools/run_models.py --tags pyt_vllm_c4ai-command-r-plus-08-2024 --keep-model-dir --live-output --timeout 28800
```

MAD launches a Docker container with the name
`container_ci-pyt_vllm_c4ai-command-r-plus-08-2024`

. The latency and throughput reports of the
model are collected in the following path: `~/MAD/reports_float16/`

.

Although the [available models](#vllm-benchmark-available-models-v085-20250513) are preconfigured
to collect latency and throughput performance data, you can also change the benchmarking
parameters. See the standalone benchmarking tab for more information.

Run the vLLM benchmark tool independently by starting the
[Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.3.1_vllm_0.8.5_20250513/images/sha256-5c8b4436dd0464119d9df2b44c745fadf81512f18ffb2f4b5dc235c71ebe26b4)
as shown in the following snippet.


In the Docker container, clone the ROCm MAD repository and navigate to the
benchmark scripts directory at `~/MAD/scripts/vllm`

.

```
git clone https://github.com/ROCm/MAD
cd MAD/scripts/vllm
```

To start the benchmark, use the following command with the appropriate options.


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
1 or 8 |
Number of GPUs |
|
|
Data type |

Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don’t need to specify them with this script.

Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.


Here are some examples of running the benchmark with various options.

Latency benchmark

Use this command to benchmark the latency of the C4AI Command R+ 08-2024 model on eight GPUs with

`float16`

precision../vllm_benchmark_report.sh -s latency -m CohereForAI/c4ai-command-r-plus-08-2024 -g 8 -d float16

Find the latency report at

`./reports_float16_vllm_rocm6.3.1/summary/c4ai-command-r-plus-08-2024_latency_report.csv`

.Throughput benchmark

Use this command to benchmark the throughput of the C4AI Command R+ 08-2024 model on eight GPUs with

`float16`

precision.-s throughput -m CohereForAI/c4ai-command-r-plus-08-2024 -g 8 -d float16

Find the throughput report at

`./reports_float16_vllm_rocm6.3.1/summary/c4ai-command-r-plus-08-2024_throughput_report.csv`

.

Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local
directory and install the required packages on the host machine.

```
clone https://github.com/ROCm/MAD
cd MAD
pip install -r requirements.txt
```

Use this command to run the performance benchmark test on the [C4AI Command R+ 08-2024 FP8](https://huggingface.co/amd/c4ai-command-r-plus-FP8-KV) model
using one GPU with the `float8`

data type on the host machine.

```
export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
python3 tools/run_models.py --tags pyt_vllm_command-r-plus_fp8 --keep-model-dir --live-output --timeout 28800
```

MAD launches a Docker container with the name
`container_ci-pyt_vllm_command-r-plus_fp8`

. The latency and throughput reports of the
model are collected in the following path: `~/MAD/reports_float8/`

.

Although the [available models](#vllm-benchmark-available-models-v085-20250513) are preconfigured
to collect latency and throughput performance data, you can also change the benchmarking
parameters. See the standalone benchmarking tab for more information.

Run the vLLM benchmark tool independently by starting the
[Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.3.1_vllm_0.8.5_20250513/images/sha256-5c8b4436dd0464119d9df2b44c745fadf81512f18ffb2f4b5dc235c71ebe26b4)
as shown in the following snippet.


In the Docker container, clone the ROCm MAD repository and navigate to the
benchmark scripts directory at `~/MAD/scripts/vllm`

.

```
git clone https://github.com/ROCm/MAD
cd MAD/scripts/vllm
```

To start the benchmark, use the following command with the appropriate options.


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
1 or 8 |
Number of GPUs |
|
|
Data type |

Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don’t need to specify them with this script.

Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.


Here are some examples of running the benchmark with various options.

Latency benchmark

Use this command to benchmark the latency of the C4AI Command R+ 08-2024 FP8 model on eight GPUs with

`float8`

precision../vllm_benchmark_report.sh -s latency -m amd/c4ai-command-r-plus-FP8-KV -g 8 -d float8

Find the latency report at

`./reports_float8_vllm_rocm6.3.1/summary/c4ai-command-r-plus-FP8-KV_latency_report.csv`

.Throughput benchmark

Use this command to benchmark the throughput of the C4AI Command R+ 08-2024 FP8 model on eight GPUs with

`float8`

precision.-s throughput -m amd/c4ai-command-r-plus-FP8-KV -g 8 -d float8

Find the throughput report at

`./reports_float8_vllm_rocm6.3.1/summary/c4ai-command-r-plus-FP8-KV_throughput_report.csv`

.

Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local
directory and install the required packages on the host machine.

```
clone https://github.com/ROCm/MAD
cd MAD
pip install -r requirements.txt
```

Use this command to run the performance benchmark test on the [DeepSeek MoE 16B](https://huggingface.co/deepseek-ai/deepseek-moe-16b-chat) model
using one GPU with the `float16`

data type on the host machine.

```
export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
python3 tools/run_models.py --tags pyt_vllm_deepseek-moe-16b-chat --keep-model-dir --live-output --timeout 28800
```

MAD launches a Docker container with the name
`container_ci-pyt_vllm_deepseek-moe-16b-chat`

. The latency and throughput reports of the
model are collected in the following path: `~/MAD/reports_float16/`

.

Although the [available models](#vllm-benchmark-available-models-v085-20250513) are preconfigured
to collect latency and throughput performance data, you can also change the benchmarking
parameters. See the standalone benchmarking tab for more information.

Run the vLLM benchmark tool independently by starting the
[Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.3.1_vllm_0.8.5_20250513/images/sha256-5c8b4436dd0464119d9df2b44c745fadf81512f18ffb2f4b5dc235c71ebe26b4)
as shown in the following snippet.


In the Docker container, clone the ROCm MAD repository and navigate to the
benchmark scripts directory at `~/MAD/scripts/vllm`

.

```
git clone https://github.com/ROCm/MAD
cd MAD/scripts/vllm
```

To start the benchmark, use the following command with the appropriate options.


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
1 or 8 |
Number of GPUs |
|
|
Data type |

Note

The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don’t need to specify them with this script.

Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.


Here are some examples of running the benchmark with various options.

Latency benchmark

Use this command to benchmark the latency of the DeepSeek MoE 16B model on eight GPUs with

`float16`

precision../vllm_benchmark_report.sh -s latency -m deepseek-ai/deepseek-moe-16b-chat -g 8 -d float16

Find the latency report at

`./reports_float16_vllm_rocm6.3.1/summary/deepseek-moe-16b-chat_latency_report.csv`

.Throughput benchmark

Use this command to benchmark the throughput of the DeepSeek MoE 16B model on eight GPUs with

`float16`

precision.-s throughput -m deepseek-ai/deepseek-moe-16b-chat -g 8 -d float16

Find the throughput report at

`./reports_float16_vllm_rocm6.3.1/summary/deepseek-moe-16b-chat_throughput_report.csv`

.

Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

## Further reading[#](#further-reading)

To learn more about the options for latency and throughput benchmark scripts, see

[ROCm/vllm](https://github.com/ROCm/vllm/tree/main/benchmarks).To learn more about system settings and management practices to configure your system for MI300X Series GPUs, see

[AMD Instinct MI300X system optimization](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi300x.html)For application performance optimization strategies for HPC and AI workloads, including inference with vLLM, see

[AMD Instinct MI300X workload optimization](../../../inference-optimization/workload.html).To learn how to run community models from Hugging Face on AMD GPUs, see

[Running models from Hugging Face](../../hugging-face-models.html).To learn how to fine-tune LLMs and optimize inference, see

[Fine-tuning LLMs and inference optimization](../../../fine-tuning/fine-tuning-and-inference.html).For a list of other ready-made Docker images for AI with ROCm, see

[AMD Infinity Hub](https://www.amd.com/en/developer/resources/infinity-hub.html#f-amd_hub_category=AI%20%26%20ML%20Models).

## Previous versions[#](#previous-versions)

See [vLLM inference performance testing version history](vllm-history.html) to find documentation for previous releases
of the `ROCm/vllm`

Docker image.
