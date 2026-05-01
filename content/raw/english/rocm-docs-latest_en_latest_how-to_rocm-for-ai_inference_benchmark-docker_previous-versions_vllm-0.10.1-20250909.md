---
title: "vLLM inference performance testing"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference/benchmark-docker/previous-versions/vllm-0.10.1-20250909.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T08:04:56.005832+00:00
content_hash: "6e4255a95aafffb7"
---

# vLLM inference performance testing[#](#vllm-inference-performance-testing)

2026-04-21

55 min read time

Caution

This documentation does not reflect the latest version of ROCm vLLM
inference performance documentation. See [vLLM inference](../vllm.html) for the latest version.

The [ROCm vLLM Docker](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.10.1_20250909/images/sha256-1113268572e26d59b205792047bea0e61e018e79aeadceba118b7bf23cb3715c) image offers
a prebuilt, optimized environment for validating large language model (LLM)
inference performance on AMD Instinct™ MI300X Series accelerators. This ROCm vLLM
Docker image integrates vLLM and PyTorch tailored specifically for MI300X Series
accelerators and includes the following components:

Software component |
Version |
|---|---|
ROCm |
6.4.1 |
vLLM |
0.10.1 (0.10.1rc2.dev409+g0b6bf6691.rocm641) |
PyTorch |
2.7.0+gitf717b2a |
hipBLASLt |
0.15 |

With this Docker image, you can quickly test the [expected
inference performance numbers](#vllm-benchmark-performance-measurements-909) for
MI300X Series accelerators.

## What’s new[#](#what-s-new)

The following is summary of notable changes since the [previous ROCm/vLLM Docker release](vllm-history.html).

Upgraded to vLLM v0.10.1.

Set

`VLLM_V1_USE_PREFILL_DECODE_ATTENTION=1`

by default for better performance.Set

`VLLM_ROCM_USE_AITER_RMSNORM=0`

by default to avoid various issues with torch compile.

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

See the [Llama 2 70B model card on Hugging Face](https://huggingface.co/meta-llama/Llama-2-70b-chat-hf) to learn more about your selected model.
Some models require access authorization prior to use via an external license agreement through a third party.

Note

See the [Llama 3.1 8B FP8 model card on Hugging Face](https://huggingface.co/amd/Llama-3.1-8B-Instruct-FP8-KV) to learn more about your selected model.
Some models require access authorization prior to use via an external license agreement through a third party.

This model uses FP8 quantization via [AMD Quark](https://quark.docs.amd.com/latest/) for efficient inference on AMD accelerators.

Note

See the [Llama 3.1 70B FP8 model card on Hugging Face](https://huggingface.co/amd/Llama-3.1-70B-Instruct-FP8-KV) to learn more about your selected model.
Some models require access authorization prior to use via an external license agreement through a third party.

This model uses FP8 quantization via [AMD Quark](https://quark.docs.amd.com/latest/) for efficient inference on AMD accelerators.

Note

See the [Llama 3.1 405B FP8 model card on Hugging Face](https://huggingface.co/amd/Llama-3.1-405B-Instruct-FP8-KV) to learn more about your selected model.
Some models require access authorization prior to use via an external license agreement through a third party.

This model uses FP8 quantization via [AMD Quark](https://quark.docs.amd.com/latest/) for efficient inference on AMD accelerators.

Note

See the [Mixtral MoE 8x7B model card on Hugging Face](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1) to learn more about your selected model.
Some models require access authorization prior to use via an external license agreement through a third party.

Note

See the [Mixtral MoE 8x22B model card on Hugging Face](https://huggingface.co/mistralai/Mixtral-8x22B-Instruct-v0.1) to learn more about your selected model.
Some models require access authorization prior to use via an external license agreement through a third party.

Note

See the [Mixtral MoE 8x7B FP8 model card on Hugging Face](https://huggingface.co/amd/Mixtral-8x7B-Instruct-v0.1-FP8-KV) to learn more about your selected model.
Some models require access authorization prior to use via an external license agreement through a third party.

This model uses FP8 quantization via [AMD Quark](https://quark.docs.amd.com/latest/) for efficient inference on AMD accelerators.

Note

See the [Mixtral MoE 8x22B FP8 model card on Hugging Face](https://huggingface.co/amd/Mixtral-8x22B-Instruct-v0.1-FP8-KV) to learn more about your selected model.
Some models require access authorization prior to use via an external license agreement through a third party.

This model uses FP8 quantization via [AMD Quark](https://quark.docs.amd.com/latest/) for efficient inference on AMD accelerators.

Note

See the [Qwen3 30B A3B model card on Hugging Face](https://huggingface.co/Qwen/Qwen3-30B-A3B) to learn more about your selected model.
Some models require access authorization prior to use via an external license agreement through a third party.

## Performance measurements[#](#performance-measurements)

To evaluate performance, the
[Performance results with AMD ROCm software](https://www.amd.com/en/developer/resources/rocm-hub/dev-ai/performance-results.html)
page provides reference throughput and serving measurements for inferencing popular AI models.

Important

The performance data presented in
[Performance results with AMD ROCm software](https://www.amd.com/en/developer/resources/rocm-hub/dev-ai/performance-results.html)
only reflects the latest version of this inference benchmarking environment.
The listed measurements should not be interpreted as the peak performance achievable by AMD Instinct MI325X and MI300X accelerators or ROCm software.

## System validation[#](#system-validation)

Before running AI workloads, it’s important to validate that your AMD hardware is configured correctly and performing optimally.

If you have already validated your system settings, including aspects like NUMA auto-balancing, you
can skip this step. Otherwise, complete the procedures in the [System validation and
optimization](../../../system-setup/prerequisite-system-validation.html#rocm-for-ai-system-optimization) guide to properly configure your system settings
before starting training.

To test for optimal performance, consult the recommended [System health benchmarks](../../../system-setup/system-health-check.html#rocm-for-ai-system-health-bench). This suite of tests will help you verify and fine-tune your
system’s configuration.

### Pull the Docker image[#](#pull-the-docker-image)

Download the [ROCm vLLM Docker image](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.10.1_20250909/images/sha256-1113268572e26d59b205792047bea0e61e018e79aeadceba118b7bf23cb3715c).
Use the following command to pull the Docker image from Docker Hub.

```
pull rocm/vllm:rocm6.4.1_vllm_0.10.1_20250909
```

### Benchmarking[#](#benchmarking)

Once the setup is complete, choose between two options to reproduce the benchmark results:

The following run command is tailored to Llama 3.1 8B.
See [Supported models](#vllm-benchmark-supported-models-909) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

Use this command to run the performance benchmark test on the

[Llama 3.1 8B](https://huggingface.co/meta-llama/Llama-3.1-8B)model using one GPU with the`float16`

data type on the host machine.export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_vllm_llama-3.1-8b \ --keep-model-dir \ --live-output \ --timeout 28800


MAD launches a Docker container with the name
`container_ci-pyt_vllm_llama-3.1-8b`

. The throughput and serving reports of the
model are collected in the following paths: `pyt_vllm_llama-3.1-8b_throughput.csv`

and `pyt_vllm_llama-3.1-8b_serving.csv`

.

Although the [available models](#vllm-benchmark-available-models-909) are preconfigured to collect
offline throughput and online serving performance data, you can
also change the benchmarking parameters. See the standalone
benchmarking tab for more information.

The following commands are optimized for Llama 3.1 8B.
See [Supported models](#vllm-benchmark-supported-models-909) to switch to another available model.

See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs)
in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs)
for descriptions of available configuration options
and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md) for
additional benchmarking information.

Launch the container

You can run the vLLM benchmark tool independently by starting the
[Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.10.1_20250909/images/sha256-1113268572e26d59b205792047bea0e61e018e79aeadceba118b7bf23cb3715c) as shown
in the following snippet.

```
pull rocm/vllm:rocm6.4.1_vllm_0.10.1_20250909
docker run -it \
--device=/dev/kfd \
--device=/dev/dri \
--group-add video \
--shm-size 16G \
--security-opt seccomp=unconfined \
--security-opt apparmor=unconfined \
--cap-add=SYS_PTRACE \
-v $(pwd):/workspace \
--env HUGGINGFACE_HUB_CACHE=/workspace \
--name test \
rocm/vllm:rocm6.4.1_vllm_0.10.1_20250909
```

Throughput command

Use the following command to start the throughput benchmark.

```
model=meta-llama/Llama-3.1-8B-Instruct
tp=1
num_prompts=1024
in=128
out=128
dtype=auto
kv_cache_dtype=auto
max_num_seqs=1024
max_seq_len_to_capture=131072
max_num_batched_tokens=131072
max_model_len=8192
vllm bench throughput --model $model \
-tp $tp \
--num-prompts $num_prompts \
--input-len $in \
--output-len $out \
--dtype $dtype \
--kv-cache-dtype $kv_cache_dtype \
--max-num-seqs $max_num_seqs \
--max-seq-len-to-capture $max_seq_len_to_capture \
--max-num-batched-tokens $max_num_batched_tokens \
--max-model-len $max_model_len \
--trust-remote-code \
--output-json ${model}_throughput.json \
--gpu-memory-utilization 0.9
```

Serving command

Start the server using the following command:

model=meta-llama/Llama-3.1-8B-Instruct tp=1 dtype=auto kv_cache_dtype=auto max_num_seqs=256 max_seq_len_to_capture=131072 max_num_batched_tokens=131072 max_model_len=8192 vllm serve $model \ -tp $tp \ --dtype $dtype \ --kv-cache-dtype $kv_cache_dtype \ --max-num-seqs $max_num_seqs \ --max-seq-len-to-capture $max_seq_len_to_capture \ --max-num-batched-tokens $max_num_batched_tokens \ --max-model-len $max_model_len \ --no-enable-prefix-caching \ --swap-space 16 \ --disable-log-requests \ --trust-remote-code \ --gpu-memory-utilization 0.9

Wait until the model has loaded and the server is ready to accept requests.

On another terminal on the same machine, run the benchmark:

# Connect to the container docker exec -it test bash # Wait for the server to start until curl -s http://localhost:8000/v1/models; do sleep 30; done # Run the benchmark model=meta-llama/Llama-3.1-8B-Instruct max_concurrency=1 num_prompts=10 in=128 out=128 vllm bench serve --model $model \ --percentile-metrics "ttft,tpot,itl,e2el" \ --dataset-name random \ --ignore-eos \ --max-concurrency $max_concurrency \ --num-prompts $num_prompts \ --random-input-len $in \ --random-output-len $out \ --trust-remote-code \ --save-result \ --result-filename ${model}_serving.json


Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B,
try adding `export VLLM_ROCM_USE_AITER=1`

to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.


Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

The following run command is tailored to Llama 3.1 70B.
See [Supported models](#vllm-benchmark-supported-models-909) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

Use this command to run the performance benchmark test on the

[Llama 3.1 70B](https://huggingface.co/meta-llama/Llama-3.1-70B-Instruct)model using one GPU with the`float16`

data type on the host machine.export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_vllm_llama-3.1-70b \ --keep-model-dir \ --live-output \ --timeout 28800


MAD launches a Docker container with the name
`container_ci-pyt_vllm_llama-3.1-70b`

. The throughput and serving reports of the
model are collected in the following paths: `pyt_vllm_llama-3.1-70b_throughput.csv`

and `pyt_vllm_llama-3.1-70b_serving.csv`

.

Although the [available models](#vllm-benchmark-available-models-909) are preconfigured to collect
offline throughput and online serving performance data, you can
also change the benchmarking parameters. See the standalone
benchmarking tab for more information.

The following commands are optimized for Llama 3.1 70B.
See [Supported models](#vllm-benchmark-supported-models-909) to switch to another available model.

See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs)
in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs)
for descriptions of available configuration options
and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md) for
additional benchmarking information.

Launch the container

You can run the vLLM benchmark tool independently by starting the
[Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.10.1_20250909/images/sha256-1113268572e26d59b205792047bea0e61e018e79aeadceba118b7bf23cb3715c) as shown
in the following snippet.

```
pull rocm/vllm:rocm6.4.1_vllm_0.10.1_20250909
docker run -it \
--device=/dev/kfd \
--device=/dev/dri \
--group-add video \
--shm-size 16G \
--security-opt seccomp=unconfined \
--security-opt apparmor=unconfined \
--cap-add=SYS_PTRACE \
-v $(pwd):/workspace \
--env HUGGINGFACE_HUB_CACHE=/workspace \
--name test \
rocm/vllm:rocm6.4.1_vllm_0.10.1_20250909
```

Throughput command

Use the following command to start the throughput benchmark.

```
model=meta-llama/Llama-3.1-70B-Instruct
tp=8
num_prompts=1024
in=128
out=128
dtype=auto
kv_cache_dtype=auto
max_num_seqs=1024
max_seq_len_to_capture=131072
max_num_batched_tokens=131072
max_model_len=8192
vllm bench throughput --model $model \
-tp $tp \
--num-prompts $num_prompts \
--input-len $in \
--output-len $out \
--dtype $dtype \
--kv-cache-dtype $kv_cache_dtype \
--max-num-seqs $max_num_seqs \
--max-seq-len-to-capture $max_seq_len_to_capture \
--max-num-batched-tokens $max_num_batched_tokens \
--max-model-len $max_model_len \
--trust-remote-code \
--output-json ${model}_throughput.json \
--gpu-memory-utilization 0.9
```

Serving command

Start the server using the following command:

model=meta-llama/Llama-3.1-70B-Instruct tp=8 dtype=auto kv_cache_dtype=auto max_num_seqs=256 max_seq_len_to_capture=131072 max_num_batched_tokens=131072 max_model_len=8192 vllm serve $model \ -tp $tp \ --dtype $dtype \ --kv-cache-dtype $kv_cache_dtype \ --max-num-seqs $max_num_seqs \ --max-seq-len-to-capture $max_seq_len_to_capture \ --max-num-batched-tokens $max_num_batched_tokens \ --max-model-len $max_model_len \ --no-enable-prefix-caching \ --swap-space 16 \ --disable-log-requests \ --trust-remote-code \ --gpu-memory-utilization 0.9

Wait until the model has loaded and the server is ready to accept requests.

On another terminal on the same machine, run the benchmark:

# Connect to the container docker exec -it test bash # Wait for the server to start until curl -s http://localhost:8000/v1/models; do sleep 30; done # Run the benchmark model=meta-llama/Llama-3.1-70B-Instruct max_concurrency=1 num_prompts=10 in=128 out=128 vllm bench serve --model $model \ --percentile-metrics "ttft,tpot,itl,e2el" \ --dataset-name random \ --ignore-eos \ --max-concurrency $max_concurrency \ --num-prompts $num_prompts \ --random-input-len $in \ --random-output-len $out \ --trust-remote-code \ --save-result \ --result-filename ${model}_serving.json


Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B,
try adding `export VLLM_ROCM_USE_AITER=1`

to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.


Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

The following run command is tailored to Llama 3.1 405B.
See [Supported models](#vllm-benchmark-supported-models-909) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

Use this command to run the performance benchmark test on the

[Llama 3.1 405B](https://huggingface.co/meta-llama/Llama-3.1-405B-Instruct)model using one GPU with the`float16`

data type on the host machine.export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_vllm_llama-3.1-405b \ --keep-model-dir \ --live-output \ --timeout 28800


MAD launches a Docker container with the name
`container_ci-pyt_vllm_llama-3.1-405b`

. The throughput and serving reports of the
model are collected in the following paths: `pyt_vllm_llama-3.1-405b_throughput.csv`

and `pyt_vllm_llama-3.1-405b_serving.csv`

.

Although the [available models](#vllm-benchmark-available-models-909) are preconfigured to collect
offline throughput and online serving performance data, you can
also change the benchmarking parameters. See the standalone
benchmarking tab for more information.

The following commands are optimized for Llama 3.1 405B.
See [Supported models](#vllm-benchmark-supported-models-909) to switch to another available model.

See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs)
in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs)
for descriptions of available configuration options
and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md) for
additional benchmarking information.

Launch the container

You can run the vLLM benchmark tool independently by starting the
[Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.10.1_20250909/images/sha256-1113268572e26d59b205792047bea0e61e018e79aeadceba118b7bf23cb3715c) as shown
in the following snippet.

```
pull rocm/vllm:rocm6.4.1_vllm_0.10.1_20250909
docker run -it \
--device=/dev/kfd \
--device=/dev/dri \
--group-add video \
--shm-size 16G \
--security-opt seccomp=unconfined \
--security-opt apparmor=unconfined \
--cap-add=SYS_PTRACE \
-v $(pwd):/workspace \
--env HUGGINGFACE_HUB_CACHE=/workspace \
--name test \
rocm/vllm:rocm6.4.1_vllm_0.10.1_20250909
```

Throughput command

Use the following command to start the throughput benchmark.

```
model=meta-llama/Llama-3.1-405B-Instruct
tp=8
num_prompts=1024
in=128
out=128
dtype=auto
kv_cache_dtype=auto
max_num_seqs=1024
max_seq_len_to_capture=131072
max_num_batched_tokens=131072
max_model_len=8192
vllm bench throughput --model $model \
-tp $tp \
--num-prompts $num_prompts \
--input-len $in \
--output-len $out \
--dtype $dtype \
--kv-cache-dtype $kv_cache_dtype \
--max-num-seqs $max_num_seqs \
--max-seq-len-to-capture $max_seq_len_to_capture \
--max-num-batched-tokens $max_num_batched_tokens \
--max-model-len $max_model_len \
--trust-remote-code \
--output-json ${model}_throughput.json \
--gpu-memory-utilization 0.9
```

Serving command

Start the server using the following command:

model=meta-llama/Llama-3.1-405B-Instruct tp=8 dtype=auto kv_cache_dtype=auto max_num_seqs=256 max_seq_len_to_capture=131072 max_num_batched_tokens=131072 max_model_len=8192 vllm serve $model \ -tp $tp \ --dtype $dtype \ --kv-cache-dtype $kv_cache_dtype \ --max-num-seqs $max_num_seqs \ --max-seq-len-to-capture $max_seq_len_to_capture \ --max-num-batched-tokens $max_num_batched_tokens \ --max-model-len $max_model_len \ --no-enable-prefix-caching \ --swap-space 16 \ --disable-log-requests \ --trust-remote-code \ --gpu-memory-utilization 0.9

Wait until the model has loaded and the server is ready to accept requests.

On another terminal on the same machine, run the benchmark:

# Connect to the container docker exec -it test bash # Wait for the server to start until curl -s http://localhost:8000/v1/models; do sleep 30; done # Run the benchmark model=meta-llama/Llama-3.1-405B-Instruct max_concurrency=1 num_prompts=10 in=128 out=128 vllm bench serve --model $model \ --percentile-metrics "ttft,tpot,itl,e2el" \ --dataset-name random \ --ignore-eos \ --max-concurrency $max_concurrency \ --num-prompts $num_prompts \ --random-input-len $in \ --random-output-len $out \ --trust-remote-code \ --save-result \ --result-filename ${model}_serving.json


Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B,
try adding `export VLLM_ROCM_USE_AITER=1`

to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.


Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

The following run command is tailored to Llama 2 70B.
See [Supported models](#vllm-benchmark-supported-models-909) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

Use this command to run the performance benchmark test on the

[Llama 2 70B](https://huggingface.co/meta-llama/Llama-2-70b-chat-hf)model using one GPU with the`float16`

data type on the host machine.export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_vllm_llama-2-70b \ --keep-model-dir \ --live-output \ --timeout 28800


MAD launches a Docker container with the name
`container_ci-pyt_vllm_llama-2-70b`

. The throughput and serving reports of the
model are collected in the following paths: `pyt_vllm_llama-2-70b_throughput.csv`

and `pyt_vllm_llama-2-70b_serving.csv`

.

Although the [available models](#vllm-benchmark-available-models-909) are preconfigured to collect
offline throughput and online serving performance data, you can
also change the benchmarking parameters. See the standalone
benchmarking tab for more information.

The following commands are optimized for Llama 2 70B.
See [Supported models](#vllm-benchmark-supported-models-909) to switch to another available model.

See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs)
in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs)
for descriptions of available configuration options
and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md) for
additional benchmarking information.

Launch the container

You can run the vLLM benchmark tool independently by starting the
[Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.10.1_20250909/images/sha256-1113268572e26d59b205792047bea0e61e018e79aeadceba118b7bf23cb3715c) as shown
in the following snippet.

```
pull rocm/vllm:rocm6.4.1_vllm_0.10.1_20250909
docker run -it \
--device=/dev/kfd \
--device=/dev/dri \
--group-add video \
--shm-size 16G \
--security-opt seccomp=unconfined \
--security-opt apparmor=unconfined \
--cap-add=SYS_PTRACE \
-v $(pwd):/workspace \
--env HUGGINGFACE_HUB_CACHE=/workspace \
--name test \
rocm/vllm:rocm6.4.1_vllm_0.10.1_20250909
```

Throughput command

Use the following command to start the throughput benchmark.

```
model=meta-llama/Llama-2-70b-chat-hf
tp=8
num_prompts=1024
in=128
out=128
dtype=auto
kv_cache_dtype=auto
max_num_seqs=1024
max_seq_len_to_capture=4096
max_num_batched_tokens=4096
max_model_len=4096
vllm bench throughput --model $model \
-tp $tp \
--num-prompts $num_prompts \
--input-len $in \
--output-len $out \
--dtype $dtype \
--kv-cache-dtype $kv_cache_dtype \
--max-num-seqs $max_num_seqs \
--max-seq-len-to-capture $max_seq_len_to_capture \
--max-num-batched-tokens $max_num_batched_tokens \
--max-model-len $max_model_len \
--trust-remote-code \
--output-json ${model}_throughput.json \
--gpu-memory-utilization 0.9
```

Serving command

Start the server using the following command:

model=meta-llama/Llama-2-70b-chat-hf tp=8 dtype=auto kv_cache_dtype=auto max_num_seqs=256 max_seq_len_to_capture=4096 max_num_batched_tokens=4096 max_model_len=4096 vllm serve $model \ -tp $tp \ --dtype $dtype \ --kv-cache-dtype $kv_cache_dtype \ --max-num-seqs $max_num_seqs \ --max-seq-len-to-capture $max_seq_len_to_capture \ --max-num-batched-tokens $max_num_batched_tokens \ --max-model-len $max_model_len \ --no-enable-prefix-caching \ --swap-space 16 \ --disable-log-requests \ --trust-remote-code \ --gpu-memory-utilization 0.9

Wait until the model has loaded and the server is ready to accept requests.

On another terminal on the same machine, run the benchmark:

# Connect to the container docker exec -it test bash # Wait for the server to start until curl -s http://localhost:8000/v1/models; do sleep 30; done # Run the benchmark model=meta-llama/Llama-2-70b-chat-hf max_concurrency=1 num_prompts=10 in=128 out=128 vllm bench serve --model $model \ --percentile-metrics "ttft,tpot,itl,e2el" \ --dataset-name random \ --ignore-eos \ --max-concurrency $max_concurrency \ --num-prompts $num_prompts \ --random-input-len $in \ --random-output-len $out \ --trust-remote-code \ --save-result \ --result-filename ${model}_serving.json


Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B,
try adding `export VLLM_ROCM_USE_AITER=1`

to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.


Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

The following run command is tailored to Llama 3.1 8B FP8.
See [Supported models](#vllm-benchmark-supported-models-909) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

Use this command to run the performance benchmark test on the

[Llama 3.1 8B FP8](https://huggingface.co/amd/Llama-3.1-8B-Instruct-FP8-KV)model using one GPU with the`float8`

data type on the host machine.export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_vllm_llama-3.1-8b_fp8 \ --keep-model-dir \ --live-output \ --timeout 28800


MAD launches a Docker container with the name
`container_ci-pyt_vllm_llama-3.1-8b_fp8`

. The throughput and serving reports of the
model are collected in the following paths: `pyt_vllm_llama-3.1-8b_fp8_throughput.csv`

and `pyt_vllm_llama-3.1-8b_fp8_serving.csv`

.

Although the [available models](#vllm-benchmark-available-models-909) are preconfigured to collect
offline throughput and online serving performance data, you can
also change the benchmarking parameters. See the standalone
benchmarking tab for more information.

The following commands are optimized for Llama 3.1 8B FP8.
See [Supported models](#vllm-benchmark-supported-models-909) to switch to another available model.

See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs)
in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs)
for descriptions of available configuration options
and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md) for
additional benchmarking information.

Launch the container

You can run the vLLM benchmark tool independently by starting the
[Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.10.1_20250909/images/sha256-1113268572e26d59b205792047bea0e61e018e79aeadceba118b7bf23cb3715c) as shown
in the following snippet.

```
pull rocm/vllm:rocm6.4.1_vllm_0.10.1_20250909
docker run -it \
--device=/dev/kfd \
--device=/dev/dri \
--group-add video \
--shm-size 16G \
--security-opt seccomp=unconfined \
--security-opt apparmor=unconfined \
--cap-add=SYS_PTRACE \
-v $(pwd):/workspace \
--env HUGGINGFACE_HUB_CACHE=/workspace \
--name test \
rocm/vllm:rocm6.4.1_vllm_0.10.1_20250909
```

Throughput command

Use the following command to start the throughput benchmark.

```
model=amd/Llama-3.1-8B-Instruct-FP8-KV
tp=1
num_prompts=1024
in=128
out=128
dtype=auto
kv_cache_dtype=fp8
max_num_seqs=1024
max_seq_len_to_capture=131072
max_num_batched_tokens=131072
max_model_len=8192
vllm bench throughput --model $model \
-tp $tp \
--num-prompts $num_prompts \
--input-len $in \
--output-len $out \
--dtype $dtype \
--kv-cache-dtype $kv_cache_dtype \
--max-num-seqs $max_num_seqs \
--max-seq-len-to-capture $max_seq_len_to_capture \
--max-num-batched-tokens $max_num_batched_tokens \
--max-model-len $max_model_len \
--trust-remote-code \
--output-json ${model}_throughput.json \
--gpu-memory-utilization 0.9
```

Serving command

Start the server using the following command:

model=amd/Llama-3.1-8B-Instruct-FP8-KV tp=1 dtype=auto kv_cache_dtype=fp8 max_num_seqs=256 max_seq_len_to_capture=131072 max_num_batched_tokens=131072 max_model_len=8192 vllm serve $model \ -tp $tp \ --dtype $dtype \ --kv-cache-dtype $kv_cache_dtype \ --max-num-seqs $max_num_seqs \ --max-seq-len-to-capture $max_seq_len_to_capture \ --max-num-batched-tokens $max_num_batched_tokens \ --max-model-len $max_model_len \ --no-enable-prefix-caching \ --swap-space 16 \ --disable-log-requests \ --trust-remote-code \ --gpu-memory-utilization 0.9

Wait until the model has loaded and the server is ready to accept requests.

On another terminal on the same machine, run the benchmark:

# Connect to the container docker exec -it test bash # Wait for the server to start until curl -s http://localhost:8000/v1/models; do sleep 30; done # Run the benchmark model=amd/Llama-3.1-8B-Instruct-FP8-KV max_concurrency=1 num_prompts=10 in=128 out=128 vllm bench serve --model $model \ --percentile-metrics "ttft,tpot,itl,e2el" \ --dataset-name random \ --ignore-eos \ --max-concurrency $max_concurrency \ --num-prompts $num_prompts \ --random-input-len $in \ --random-output-len $out \ --trust-remote-code \ --save-result \ --result-filename ${model}_serving.json


Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B,
try adding `export VLLM_ROCM_USE_AITER=1`

to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.


Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

The following run command is tailored to Llama 3.1 70B FP8.
See [Supported models](#vllm-benchmark-supported-models-909) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

Use this command to run the performance benchmark test on the

[Llama 3.1 70B FP8](https://huggingface.co/amd/Llama-3.1-70B-Instruct-FP8-KV)model using one GPU with the`float8`

data type on the host machine.export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_vllm_llama-3.1-70b_fp8 \ --keep-model-dir \ --live-output \ --timeout 28800


MAD launches a Docker container with the name
`container_ci-pyt_vllm_llama-3.1-70b_fp8`

. The throughput and serving reports of the
model are collected in the following paths: `pyt_vllm_llama-3.1-70b_fp8_throughput.csv`

and `pyt_vllm_llama-3.1-70b_fp8_serving.csv`

.

Although the [available models](#vllm-benchmark-available-models-909) are preconfigured to collect
offline throughput and online serving performance data, you can
also change the benchmarking parameters. See the standalone
benchmarking tab for more information.

The following commands are optimized for Llama 3.1 70B FP8.
See [Supported models](#vllm-benchmark-supported-models-909) to switch to another available model.

See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs)
in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs)
for descriptions of available configuration options
and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md) for
additional benchmarking information.

Launch the container

You can run the vLLM benchmark tool independently by starting the
[Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.10.1_20250909/images/sha256-1113268572e26d59b205792047bea0e61e018e79aeadceba118b7bf23cb3715c) as shown
in the following snippet.

```
pull rocm/vllm:rocm6.4.1_vllm_0.10.1_20250909
docker run -it \
--device=/dev/kfd \
--device=/dev/dri \
--group-add video \
--shm-size 16G \
--security-opt seccomp=unconfined \
--security-opt apparmor=unconfined \
--cap-add=SYS_PTRACE \
-v $(pwd):/workspace \
--env HUGGINGFACE_HUB_CACHE=/workspace \
--name test \
rocm/vllm:rocm6.4.1_vllm_0.10.1_20250909
```

Throughput command

Use the following command to start the throughput benchmark.

```
model=amd/Llama-3.1-70B-Instruct-FP8-KV
tp=8
num_prompts=1024
in=128
out=128
dtype=auto
kv_cache_dtype=fp8
max_num_seqs=1024
max_seq_len_to_capture=131072
max_num_batched_tokens=131072
max_model_len=8192
vllm bench throughput --model $model \
-tp $tp \
--num-prompts $num_prompts \
--input-len $in \
--output-len $out \
--dtype $dtype \
--kv-cache-dtype $kv_cache_dtype \
--max-num-seqs $max_num_seqs \
--max-seq-len-to-capture $max_seq_len_to_capture \
--max-num-batched-tokens $max_num_batched_tokens \
--max-model-len $max_model_len \
--trust-remote-code \
--output-json ${model}_throughput.json \
--gpu-memory-utilization 0.9
```

Serving command

Start the server using the following command:

model=amd/Llama-3.1-70B-Instruct-FP8-KV tp=8 dtype=auto kv_cache_dtype=fp8 max_num_seqs=256 max_seq_len_to_capture=131072 max_num_batched_tokens=131072 max_model_len=8192 vllm serve $model \ -tp $tp \ --dtype $dtype \ --kv-cache-dtype $kv_cache_dtype \ --max-num-seqs $max_num_seqs \ --max-seq-len-to-capture $max_seq_len_to_capture \ --max-num-batched-tokens $max_num_batched_tokens \ --max-model-len $max_model_len \ --no-enable-prefix-caching \ --swap-space 16 \ --disable-log-requests \ --trust-remote-code \ --gpu-memory-utilization 0.9

Wait until the model has loaded and the server is ready to accept requests.

On another terminal on the same machine, run the benchmark:

# Connect to the container docker exec -it test bash # Wait for the server to start until curl -s http://localhost:8000/v1/models; do sleep 30; done # Run the benchmark model=amd/Llama-3.1-70B-Instruct-FP8-KV max_concurrency=1 num_prompts=10 in=128 out=128 vllm bench serve --model $model \ --percentile-metrics "ttft,tpot,itl,e2el" \ --dataset-name random \ --ignore-eos \ --max-concurrency $max_concurrency \ --num-prompts $num_prompts \ --random-input-len $in \ --random-output-len $out \ --trust-remote-code \ --save-result \ --result-filename ${model}_serving.json


Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B,
try adding `export VLLM_ROCM_USE_AITER=1`

to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.


Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

The following run command is tailored to Llama 3.1 405B FP8.
See [Supported models](#vllm-benchmark-supported-models-909) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

Use this command to run the performance benchmark test on the

[Llama 3.1 405B FP8](https://huggingface.co/amd/Llama-3.1-405B-Instruct-FP8-KV)model using one GPU with the`float8`

data type on the host machine.export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_vllm_llama-3.1-405b_fp8 \ --keep-model-dir \ --live-output \ --timeout 28800


MAD launches a Docker container with the name
`container_ci-pyt_vllm_llama-3.1-405b_fp8`

. The throughput and serving reports of the
model are collected in the following paths: `pyt_vllm_llama-3.1-405b_fp8_throughput.csv`

and `pyt_vllm_llama-3.1-405b_fp8_serving.csv`

.

Although the [available models](#vllm-benchmark-available-models-909) are preconfigured to collect
offline throughput and online serving performance data, you can
also change the benchmarking parameters. See the standalone
benchmarking tab for more information.

The following commands are optimized for Llama 3.1 405B FP8.
See [Supported models](#vllm-benchmark-supported-models-909) to switch to another available model.

See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs)
in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs)
for descriptions of available configuration options
and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md) for
additional benchmarking information.

Launch the container

You can run the vLLM benchmark tool independently by starting the
[Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.10.1_20250909/images/sha256-1113268572e26d59b205792047bea0e61e018e79aeadceba118b7bf23cb3715c) as shown
in the following snippet.

```
pull rocm/vllm:rocm6.4.1_vllm_0.10.1_20250909
docker run -it \
--device=/dev/kfd \
--device=/dev/dri \
--group-add video \
--shm-size 16G \
--security-opt seccomp=unconfined \
--security-opt apparmor=unconfined \
--cap-add=SYS_PTRACE \
-v $(pwd):/workspace \
--env HUGGINGFACE_HUB_CACHE=/workspace \
--name test \
rocm/vllm:rocm6.4.1_vllm_0.10.1_20250909
```

Throughput command

Use the following command to start the throughput benchmark.

```
model=amd/Llama-3.1-405B-Instruct-FP8-KV
tp=8
num_prompts=1024
in=128
out=128
dtype=auto
kv_cache_dtype=fp8
max_num_seqs=1024
max_seq_len_to_capture=131072
max_num_batched_tokens=131072
max_model_len=8192
vllm bench throughput --model $model \
-tp $tp \
--num-prompts $num_prompts \
--input-len $in \
--output-len $out \
--dtype $dtype \
--kv-cache-dtype $kv_cache_dtype \
--max-num-seqs $max_num_seqs \
--max-seq-len-to-capture $max_seq_len_to_capture \
--max-num-batched-tokens $max_num_batched_tokens \
--max-model-len $max_model_len \
--trust-remote-code \
--output-json ${model}_throughput.json \
--gpu-memory-utilization 0.9
```

Serving command

Start the server using the following command:

model=amd/Llama-3.1-405B-Instruct-FP8-KV tp=8 dtype=auto kv_cache_dtype=fp8 max_num_seqs=256 max_seq_len_to_capture=131072 max_num_batched_tokens=131072 max_model_len=8192 vllm serve $model \ -tp $tp \ --dtype $dtype \ --kv-cache-dtype $kv_cache_dtype \ --max-num-seqs $max_num_seqs \ --max-seq-len-to-capture $max_seq_len_to_capture \ --max-num-batched-tokens $max_num_batched_tokens \ --max-model-len $max_model_len \ --no-enable-prefix-caching \ --swap-space 16 \ --disable-log-requests \ --trust-remote-code \ --gpu-memory-utilization 0.9

Wait until the model has loaded and the server is ready to accept requests.

On another terminal on the same machine, run the benchmark:

# Connect to the container docker exec -it test bash # Wait for the server to start until curl -s http://localhost:8000/v1/models; do sleep 30; done # Run the benchmark model=amd/Llama-3.1-405B-Instruct-FP8-KV max_concurrency=1 num_prompts=10 in=128 out=128 vllm bench serve --model $model \ --percentile-metrics "ttft,tpot,itl,e2el" \ --dataset-name random \ --ignore-eos \ --max-concurrency $max_concurrency \ --num-prompts $num_prompts \ --random-input-len $in \ --random-output-len $out \ --trust-remote-code \ --save-result \ --result-filename ${model}_serving.json


Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B,
try adding `export VLLM_ROCM_USE_AITER=1`

to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.


Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

The following run command is tailored to Mixtral MoE 8x7B.
See [Supported models](#vllm-benchmark-supported-models-909) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

Use this command to run the performance benchmark test on the

[Mixtral MoE 8x7B](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1)model using one GPU with the`float16`

data type on the host machine.export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_vllm_mixtral-8x7b \ --keep-model-dir \ --live-output \ --timeout 28800


MAD launches a Docker container with the name
`container_ci-pyt_vllm_mixtral-8x7b`

. The throughput and serving reports of the
model are collected in the following paths: `pyt_vllm_mixtral-8x7b_throughput.csv`

and `pyt_vllm_mixtral-8x7b_serving.csv`

.

Although the [available models](#vllm-benchmark-available-models-909) are preconfigured to collect
offline throughput and online serving performance data, you can
also change the benchmarking parameters. See the standalone
benchmarking tab for more information.

The following commands are optimized for Mixtral MoE 8x7B.
See [Supported models](#vllm-benchmark-supported-models-909) to switch to another available model.

See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs)
in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs)
for descriptions of available configuration options
and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md) for
additional benchmarking information.

Launch the container

You can run the vLLM benchmark tool independently by starting the
[Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.10.1_20250909/images/sha256-1113268572e26d59b205792047bea0e61e018e79aeadceba118b7bf23cb3715c) as shown
in the following snippet.

```
pull rocm/vllm:rocm6.4.1_vllm_0.10.1_20250909
docker run -it \
--device=/dev/kfd \
--device=/dev/dri \
--group-add video \
--shm-size 16G \
--security-opt seccomp=unconfined \
--security-opt apparmor=unconfined \
--cap-add=SYS_PTRACE \
-v $(pwd):/workspace \
--env HUGGINGFACE_HUB_CACHE=/workspace \
--name test \
rocm/vllm:rocm6.4.1_vllm_0.10.1_20250909
```

Throughput command

Use the following command to start the throughput benchmark.

```
model=mistralai/Mixtral-8x7B-Instruct-v0.1
tp=8
num_prompts=1024
in=128
out=128
dtype=auto
kv_cache_dtype=auto
max_num_seqs=1024
max_seq_len_to_capture=32768
max_num_batched_tokens=32768
max_model_len=8192
vllm bench throughput --model $model \
-tp $tp \
--num-prompts $num_prompts \
--input-len $in \
--output-len $out \
--dtype $dtype \
--kv-cache-dtype $kv_cache_dtype \
--max-num-seqs $max_num_seqs \
--max-seq-len-to-capture $max_seq_len_to_capture \
--max-num-batched-tokens $max_num_batched_tokens \
--max-model-len $max_model_len \
--trust-remote-code \
--output-json ${model}_throughput.json \
--gpu-memory-utilization 0.9
```

Serving command

Start the server using the following command:

model=mistralai/Mixtral-8x7B-Instruct-v0.1 tp=8 dtype=auto kv_cache_dtype=auto max_num_seqs=256 max_seq_len_to_capture=32768 max_num_batched_tokens=32768 max_model_len=8192 vllm serve $model \ -tp $tp \ --dtype $dtype \ --kv-cache-dtype $kv_cache_dtype \ --max-num-seqs $max_num_seqs \ --max-seq-len-to-capture $max_seq_len_to_capture \ --max-num-batched-tokens $max_num_batched_tokens \ --max-model-len $max_model_len \ --no-enable-prefix-caching \ --swap-space 16 \ --disable-log-requests \ --trust-remote-code \ --gpu-memory-utilization 0.9

Wait until the model has loaded and the server is ready to accept requests.

On another terminal on the same machine, run the benchmark:

# Connect to the container docker exec -it test bash # Wait for the server to start until curl -s http://localhost:8000/v1/models; do sleep 30; done # Run the benchmark model=mistralai/Mixtral-8x7B-Instruct-v0.1 max_concurrency=1 num_prompts=10 in=128 out=128 vllm bench serve --model $model \ --percentile-metrics "ttft,tpot,itl,e2el" \ --dataset-name random \ --ignore-eos \ --max-concurrency $max_concurrency \ --num-prompts $num_prompts \ --random-input-len $in \ --random-output-len $out \ --trust-remote-code \ --save-result \ --result-filename ${model}_serving.json


Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B,
try adding `export VLLM_ROCM_USE_AITER=1`

to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.


Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

The following run command is tailored to Mixtral MoE 8x22B.
See [Supported models](#vllm-benchmark-supported-models-909) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

Use this command to run the performance benchmark test on the

[Mixtral MoE 8x22B](https://huggingface.co/mistralai/Mixtral-8x22B-Instruct-v0.1)model using one GPU with the`float16`

data type on the host machine.export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_vllm_mixtral-8x22b \ --keep-model-dir \ --live-output \ --timeout 28800


MAD launches a Docker container with the name
`container_ci-pyt_vllm_mixtral-8x22b`

. The throughput and serving reports of the
model are collected in the following paths: `pyt_vllm_mixtral-8x22b_throughput.csv`

and `pyt_vllm_mixtral-8x22b_serving.csv`

.

Although the [available models](#vllm-benchmark-available-models-909) are preconfigured to collect
offline throughput and online serving performance data, you can
also change the benchmarking parameters. See the standalone
benchmarking tab for more information.

The following commands are optimized for Mixtral MoE 8x22B.
See [Supported models](#vllm-benchmark-supported-models-909) to switch to another available model.

See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs)
in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs)
for descriptions of available configuration options
and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md) for
additional benchmarking information.

Launch the container

You can run the vLLM benchmark tool independently by starting the
[Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.10.1_20250909/images/sha256-1113268572e26d59b205792047bea0e61e018e79aeadceba118b7bf23cb3715c) as shown
in the following snippet.

```
pull rocm/vllm:rocm6.4.1_vllm_0.10.1_20250909
docker run -it \
--device=/dev/kfd \
--device=/dev/dri \
--group-add video \
--shm-size 16G \
--security-opt seccomp=unconfined \
--security-opt apparmor=unconfined \
--cap-add=SYS_PTRACE \
-v $(pwd):/workspace \
--env HUGGINGFACE_HUB_CACHE=/workspace \
--name test \
rocm/vllm:rocm6.4.1_vllm_0.10.1_20250909
```

Throughput command

Use the following command to start the throughput benchmark.

```
model=mistralai/Mixtral-8x22B-Instruct-v0.1
tp=8
num_prompts=1024
in=128
out=128
dtype=auto
kv_cache_dtype=auto
max_num_seqs=1024
max_seq_len_to_capture=65536
max_num_batched_tokens=65536
max_model_len=8192
vllm bench throughput --model $model \
-tp $tp \
--num-prompts $num_prompts \
--input-len $in \
--output-len $out \
--dtype $dtype \
--kv-cache-dtype $kv_cache_dtype \
--max-num-seqs $max_num_seqs \
--max-seq-len-to-capture $max_seq_len_to_capture \
--max-num-batched-tokens $max_num_batched_tokens \
--max-model-len $max_model_len \
--trust-remote-code \
--output-json ${model}_throughput.json \
--gpu-memory-utilization 0.9
```

Serving command

Start the server using the following command:

model=mistralai/Mixtral-8x22B-Instruct-v0.1 tp=8 dtype=auto kv_cache_dtype=auto max_num_seqs=256 max_seq_len_to_capture=65536 max_num_batched_tokens=65536 max_model_len=8192 vllm serve $model \ -tp $tp \ --dtype $dtype \ --kv-cache-dtype $kv_cache_dtype \ --max-num-seqs $max_num_seqs \ --max-seq-len-to-capture $max_seq_len_to_capture \ --max-num-batched-tokens $max_num_batched_tokens \ --max-model-len $max_model_len \ --no-enable-prefix-caching \ --swap-space 16 \ --disable-log-requests \ --trust-remote-code \ --gpu-memory-utilization 0.9

Wait until the model has loaded and the server is ready to accept requests.

On another terminal on the same machine, run the benchmark:

# Connect to the container docker exec -it test bash # Wait for the server to start until curl -s http://localhost:8000/v1/models; do sleep 30; done # Run the benchmark model=mistralai/Mixtral-8x22B-Instruct-v0.1 max_concurrency=1 num_prompts=10 in=128 out=128 vllm bench serve --model $model \ --percentile-metrics "ttft,tpot,itl,e2el" \ --dataset-name random \ --ignore-eos \ --max-concurrency $max_concurrency \ --num-prompts $num_prompts \ --random-input-len $in \ --random-output-len $out \ --trust-remote-code \ --save-result \ --result-filename ${model}_serving.json


Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B,
try adding `export VLLM_ROCM_USE_AITER=1`

to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.


Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

The following run command is tailored to Mixtral MoE 8x7B FP8.
See [Supported models](#vllm-benchmark-supported-models-909) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

Use this command to run the performance benchmark test on the

[Mixtral MoE 8x7B FP8](https://huggingface.co/amd/Mixtral-8x7B-Instruct-v0.1-FP8-KV)model using one GPU with the`float8`

data type on the host machine.export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_vllm_mixtral-8x7b_fp8 \ --keep-model-dir \ --live-output \ --timeout 28800


MAD launches a Docker container with the name
`container_ci-pyt_vllm_mixtral-8x7b_fp8`

. The throughput and serving reports of the
model are collected in the following paths: `pyt_vllm_mixtral-8x7b_fp8_throughput.csv`

and `pyt_vllm_mixtral-8x7b_fp8_serving.csv`

.

Although the [available models](#vllm-benchmark-available-models-909) are preconfigured to collect
offline throughput and online serving performance data, you can
also change the benchmarking parameters. See the standalone
benchmarking tab for more information.

The following commands are optimized for Mixtral MoE 8x7B FP8.
See [Supported models](#vllm-benchmark-supported-models-909) to switch to another available model.

See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs)
in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs)
for descriptions of available configuration options
and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md) for
additional benchmarking information.

Launch the container

You can run the vLLM benchmark tool independently by starting the
[Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.10.1_20250909/images/sha256-1113268572e26d59b205792047bea0e61e018e79aeadceba118b7bf23cb3715c) as shown
in the following snippet.

```
pull rocm/vllm:rocm6.4.1_vllm_0.10.1_20250909
docker run -it \
--device=/dev/kfd \
--device=/dev/dri \
--group-add video \
--shm-size 16G \
--security-opt seccomp=unconfined \
--security-opt apparmor=unconfined \
--cap-add=SYS_PTRACE \
-v $(pwd):/workspace \
--env HUGGINGFACE_HUB_CACHE=/workspace \
--name test \
rocm/vllm:rocm6.4.1_vllm_0.10.1_20250909
```

Throughput command

Use the following command to start the throughput benchmark.

```
model=amd/Mixtral-8x7B-Instruct-v0.1-FP8-KV
tp=8
num_prompts=1024
in=128
out=128
dtype=auto
kv_cache_dtype=fp8
max_num_seqs=1024
max_seq_len_to_capture=32768
max_num_batched_tokens=32768
max_model_len=8192
vllm bench throughput --model $model \
-tp $tp \
--num-prompts $num_prompts \
--input-len $in \
--output-len $out \
--dtype $dtype \
--kv-cache-dtype $kv_cache_dtype \
--max-num-seqs $max_num_seqs \
--max-seq-len-to-capture $max_seq_len_to_capture \
--max-num-batched-tokens $max_num_batched_tokens \
--max-model-len $max_model_len \
--trust-remote-code \
--output-json ${model}_throughput.json \
--gpu-memory-utilization 0.9
```

Serving command

Start the server using the following command:

model=amd/Mixtral-8x7B-Instruct-v0.1-FP8-KV tp=8 dtype=auto kv_cache_dtype=fp8 max_num_seqs=256 max_seq_len_to_capture=32768 max_num_batched_tokens=32768 max_model_len=8192 vllm serve $model \ -tp $tp \ --dtype $dtype \ --kv-cache-dtype $kv_cache_dtype \ --max-num-seqs $max_num_seqs \ --max-seq-len-to-capture $max_seq_len_to_capture \ --max-num-batched-tokens $max_num_batched_tokens \ --max-model-len $max_model_len \ --no-enable-prefix-caching \ --swap-space 16 \ --disable-log-requests \ --trust-remote-code \ --gpu-memory-utilization 0.9

Wait until the model has loaded and the server is ready to accept requests.

On another terminal on the same machine, run the benchmark:

# Connect to the container docker exec -it test bash # Wait for the server to start until curl -s http://localhost:8000/v1/models; do sleep 30; done # Run the benchmark model=amd/Mixtral-8x7B-Instruct-v0.1-FP8-KV max_concurrency=1 num_prompts=10 in=128 out=128 vllm bench serve --model $model \ --percentile-metrics "ttft,tpot,itl,e2el" \ --dataset-name random \ --ignore-eos \ --max-concurrency $max_concurrency \ --num-prompts $num_prompts \ --random-input-len $in \ --random-output-len $out \ --trust-remote-code \ --save-result \ --result-filename ${model}_serving.json


Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B,
try adding `export VLLM_ROCM_USE_AITER=1`

to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.


Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

The following run command is tailored to Mixtral MoE 8x22B FP8.
See [Supported models](#vllm-benchmark-supported-models-909) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

Use this command to run the performance benchmark test on the

[Mixtral MoE 8x22B FP8](https://huggingface.co/amd/Mixtral-8x22B-Instruct-v0.1-FP8-KV)model using one GPU with the`float8`

data type on the host machine.export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_vllm_mixtral-8x22b_fp8 \ --keep-model-dir \ --live-output \ --timeout 28800


MAD launches a Docker container with the name
`container_ci-pyt_vllm_mixtral-8x22b_fp8`

. The throughput and serving reports of the
model are collected in the following paths: `pyt_vllm_mixtral-8x22b_fp8_throughput.csv`

and `pyt_vllm_mixtral-8x22b_fp8_serving.csv`

.

Although the [available models](#vllm-benchmark-available-models-909) are preconfigured to collect
offline throughput and online serving performance data, you can
also change the benchmarking parameters. See the standalone
benchmarking tab for more information.

The following commands are optimized for Mixtral MoE 8x22B FP8.
See [Supported models](#vllm-benchmark-supported-models-909) to switch to another available model.

See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs)
in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs)
for descriptions of available configuration options
and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md) for
additional benchmarking information.

Launch the container

You can run the vLLM benchmark tool independently by starting the
[Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.10.1_20250909/images/sha256-1113268572e26d59b205792047bea0e61e018e79aeadceba118b7bf23cb3715c) as shown
in the following snippet.

```
pull rocm/vllm:rocm6.4.1_vllm_0.10.1_20250909
docker run -it \
--device=/dev/kfd \
--device=/dev/dri \
--group-add video \
--shm-size 16G \
--security-opt seccomp=unconfined \
--security-opt apparmor=unconfined \
--cap-add=SYS_PTRACE \
-v $(pwd):/workspace \
--env HUGGINGFACE_HUB_CACHE=/workspace \
--name test \
rocm/vllm:rocm6.4.1_vllm_0.10.1_20250909
```

Throughput command

Use the following command to start the throughput benchmark.

```
model=amd/Mixtral-8x22B-Instruct-v0.1-FP8-KV
tp=8
num_prompts=1024
in=128
out=128
dtype=auto
kv_cache_dtype=fp8
max_num_seqs=1024
max_seq_len_to_capture=65536
max_num_batched_tokens=65536
max_model_len=8192
vllm bench throughput --model $model \
-tp $tp \
--num-prompts $num_prompts \
--input-len $in \
--output-len $out \
--dtype $dtype \
--kv-cache-dtype $kv_cache_dtype \
--max-num-seqs $max_num_seqs \
--max-seq-len-to-capture $max_seq_len_to_capture \
--max-num-batched-tokens $max_num_batched_tokens \
--max-model-len $max_model_len \
--trust-remote-code \
--output-json ${model}_throughput.json \
--gpu-memory-utilization 0.9
```

Serving command

Start the server using the following command:

model=amd/Mixtral-8x22B-Instruct-v0.1-FP8-KV tp=8 dtype=auto kv_cache_dtype=fp8 max_num_seqs=256 max_seq_len_to_capture=65536 max_num_batched_tokens=65536 max_model_len=8192 vllm serve $model \ -tp $tp \ --dtype $dtype \ --kv-cache-dtype $kv_cache_dtype \ --max-num-seqs $max_num_seqs \ --max-seq-len-to-capture $max_seq_len_to_capture \ --max-num-batched-tokens $max_num_batched_tokens \ --max-model-len $max_model_len \ --no-enable-prefix-caching \ --swap-space 16 \ --disable-log-requests \ --trust-remote-code \ --gpu-memory-utilization 0.9

Wait until the model has loaded and the server is ready to accept requests.

On another terminal on the same machine, run the benchmark:

# Connect to the container docker exec -it test bash # Wait for the server to start until curl -s http://localhost:8000/v1/models; do sleep 30; done # Run the benchmark model=amd/Mixtral-8x22B-Instruct-v0.1-FP8-KV max_concurrency=1 num_prompts=10 in=128 out=128 vllm bench serve --model $model \ --percentile-metrics "ttft,tpot,itl,e2el" \ --dataset-name random \ --ignore-eos \ --max-concurrency $max_concurrency \ --num-prompts $num_prompts \ --random-input-len $in \ --random-output-len $out \ --trust-remote-code \ --save-result \ --result-filename ${model}_serving.json


Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B,
try adding `export VLLM_ROCM_USE_AITER=1`

to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.


Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

The following run command is tailored to QwQ-32B.
See [Supported models](#vllm-benchmark-supported-models-909) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

Use this command to run the performance benchmark test on the

[QwQ-32B](https://huggingface.co/Qwen/QwQ-32B)model using one GPU with the`float16`

data type on the host machine.export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_vllm_qwq-32b \ --keep-model-dir \ --live-output \ --timeout 28800


MAD launches a Docker container with the name
`container_ci-pyt_vllm_qwq-32b`

. The throughput and serving reports of the
model are collected in the following paths: `pyt_vllm_qwq-32b_throughput.csv`

and `pyt_vllm_qwq-32b_serving.csv`

.

Although the [available models](#vllm-benchmark-available-models-909) are preconfigured to collect
offline throughput and online serving performance data, you can
also change the benchmarking parameters. See the standalone
benchmarking tab for more information.

The following commands are optimized for QwQ-32B.
See [Supported models](#vllm-benchmark-supported-models-909) to switch to another available model.

See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs)
in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs)
for descriptions of available configuration options
and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md) for
additional benchmarking information.

Launch the container

You can run the vLLM benchmark tool independently by starting the
[Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.10.1_20250909/images/sha256-1113268572e26d59b205792047bea0e61e018e79aeadceba118b7bf23cb3715c) as shown
in the following snippet.

```
pull rocm/vllm:rocm6.4.1_vllm_0.10.1_20250909
docker run -it \
--device=/dev/kfd \
--device=/dev/dri \
--group-add video \
--shm-size 16G \
--security-opt seccomp=unconfined \
--security-opt apparmor=unconfined \
--cap-add=SYS_PTRACE \
-v $(pwd):/workspace \
--env HUGGINGFACE_HUB_CACHE=/workspace \
--name test \
rocm/vllm:rocm6.4.1_vllm_0.10.1_20250909
```

Throughput command

Use the following command to start the throughput benchmark.

```
model=Qwen/QwQ-32B
tp=1
num_prompts=1024
in=128
out=128
dtype=auto
kv_cache_dtype=auto
max_num_seqs=1024
max_seq_len_to_capture=131072
max_num_batched_tokens=131072
max_model_len=8192
vllm bench throughput --model $model \
-tp $tp \
--num-prompts $num_prompts \
--input-len $in \
--output-len $out \
--dtype $dtype \
--kv-cache-dtype $kv_cache_dtype \
--max-num-seqs $max_num_seqs \
--max-seq-len-to-capture $max_seq_len_to_capture \
--max-num-batched-tokens $max_num_batched_tokens \
--max-model-len $max_model_len \
--trust-remote-code \
--output-json ${model}_throughput.json \
--gpu-memory-utilization 0.9
```

Serving command

Start the server using the following command:

model=Qwen/QwQ-32B tp=1 dtype=auto kv_cache_dtype=auto max_num_seqs=256 max_seq_len_to_capture=131072 max_num_batched_tokens=131072 max_model_len=8192 vllm serve $model \ -tp $tp \ --dtype $dtype \ --kv-cache-dtype $kv_cache_dtype \ --max-num-seqs $max_num_seqs \ --max-seq-len-to-capture $max_seq_len_to_capture \ --max-num-batched-tokens $max_num_batched_tokens \ --max-model-len $max_model_len \ --no-enable-prefix-caching \ --swap-space 16 \ --disable-log-requests \ --trust-remote-code \ --gpu-memory-utilization 0.9

Wait until the model has loaded and the server is ready to accept requests.

On another terminal on the same machine, run the benchmark:

# Connect to the container docker exec -it test bash # Wait for the server to start until curl -s http://localhost:8000/v1/models; do sleep 30; done # Run the benchmark model=Qwen/QwQ-32B max_concurrency=1 num_prompts=10 in=128 out=128 vllm bench serve --model $model \ --percentile-metrics "ttft,tpot,itl,e2el" \ --dataset-name random \ --ignore-eos \ --max-concurrency $max_concurrency \ --num-prompts $num_prompts \ --random-input-len $in \ --random-output-len $out \ --trust-remote-code \ --save-result \ --result-filename ${model}_serving.json


Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B,
try adding `export VLLM_ROCM_USE_AITER=1`

to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.


Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

The following run command is tailored to Qwen3 30B A3B.
See [Supported models](#vllm-benchmark-supported-models-909) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

Use this command to run the performance benchmark test on the

[Qwen3 30B A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B)model using one GPU with the`float16`

data type on the host machine.export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_vllm_qwen3-30b-a3b \ --keep-model-dir \ --live-output \ --timeout 28800


MAD launches a Docker container with the name
`container_ci-pyt_vllm_qwen3-30b-a3b`

. The throughput and serving reports of the
model are collected in the following paths: `pyt_vllm_qwen3-30b-a3b_throughput.csv`

and `pyt_vllm_qwen3-30b-a3b_serving.csv`

.

Although the [available models](#vllm-benchmark-available-models-909) are preconfigured to collect
offline throughput and online serving performance data, you can
also change the benchmarking parameters. See the standalone
benchmarking tab for more information.

The following commands are optimized for Qwen3 30B A3B.
See [Supported models](#vllm-benchmark-supported-models-909) to switch to another available model.

See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs)
in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs)
for descriptions of available configuration options
and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md) for
additional benchmarking information.

Launch the container

You can run the vLLM benchmark tool independently by starting the
[Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.10.1_20250909/images/sha256-1113268572e26d59b205792047bea0e61e018e79aeadceba118b7bf23cb3715c) as shown
in the following snippet.

```
pull rocm/vllm:rocm6.4.1_vllm_0.10.1_20250909
docker run -it \
--device=/dev/kfd \
--device=/dev/dri \
--group-add video \
--shm-size 16G \
--security-opt seccomp=unconfined \
--security-opt apparmor=unconfined \
--cap-add=SYS_PTRACE \
-v $(pwd):/workspace \
--env HUGGINGFACE_HUB_CACHE=/workspace \
--name test \
rocm/vllm:rocm6.4.1_vllm_0.10.1_20250909
```

Throughput command

Use the following command to start the throughput benchmark.

```
model=Qwen/Qwen3-30B-A3B
tp=1
num_prompts=1024
in=128
out=128
dtype=auto
kv_cache_dtype=auto
max_num_seqs=1024
max_seq_len_to_capture=32768
max_num_batched_tokens=32768
max_model_len=8192
vllm bench throughput --model $model \
-tp $tp \
--num-prompts $num_prompts \
--input-len $in \
--output-len $out \
--dtype $dtype \
--kv-cache-dtype $kv_cache_dtype \
--max-num-seqs $max_num_seqs \
--max-seq-len-to-capture $max_seq_len_to_capture \
--max-num-batched-tokens $max_num_batched_tokens \
--max-model-len $max_model_len \
--trust-remote-code \
--output-json ${model}_throughput.json \
--gpu-memory-utilization 0.9
```

Serving command

Start the server using the following command:

model=Qwen/Qwen3-30B-A3B tp=1 dtype=auto kv_cache_dtype=auto max_num_seqs=256 max_seq_len_to_capture=32768 max_num_batched_tokens=32768 max_model_len=8192 vllm serve $model \ -tp $tp \ --dtype $dtype \ --kv-cache-dtype $kv_cache_dtype \ --max-num-seqs $max_num_seqs \ --max-seq-len-to-capture $max_seq_len_to_capture \ --max-num-batched-tokens $max_num_batched_tokens \ --max-model-len $max_model_len \ --no-enable-prefix-caching \ --swap-space 16 \ --disable-log-requests \ --trust-remote-code \ --gpu-memory-utilization 0.9

Wait until the model has loaded and the server is ready to accept requests.

On another terminal on the same machine, run the benchmark:

# Connect to the container docker exec -it test bash # Wait for the server to start until curl -s http://localhost:8000/v1/models; do sleep 30; done # Run the benchmark model=Qwen/Qwen3-30B-A3B max_concurrency=1 num_prompts=10 in=128 out=128 vllm bench serve --model $model \ --percentile-metrics "ttft,tpot,itl,e2el" \ --dataset-name random \ --ignore-eos \ --max-concurrency $max_concurrency \ --num-prompts $num_prompts \ --random-input-len $in \ --random-output-len $out \ --trust-remote-code \ --save-result \ --result-filename ${model}_serving.json


Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B,
try adding `export VLLM_ROCM_USE_AITER=1`

to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.


Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

The following run command is tailored to Phi-4.
See [Supported models](#vllm-benchmark-supported-models-909) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

Use this command to run the performance benchmark test on the

[Phi-4](https://huggingface.co/microsoft/phi-4)model using one GPU with the :literal:`` data type on the host machine.export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_vllm_phi-4 \ --keep-model-dir \ --live-output \ --timeout 28800


MAD launches a Docker container with the name
`container_ci-pyt_vllm_phi-4`

. The throughput and serving reports of the
model are collected in the following paths: `pyt_vllm_phi-4_throughput.csv`

and `pyt_vllm_phi-4_serving.csv`

.

Although the [available models](#vllm-benchmark-available-models-909) are preconfigured to collect
offline throughput and online serving performance data, you can
also change the benchmarking parameters. See the standalone
benchmarking tab for more information.

The following commands are optimized for Phi-4.
See [Supported models](#vllm-benchmark-supported-models-909) to switch to another available model.

See also

For more information on configuration, see the [config files](https://github.com/ROCm/MAD/tree/develop/scripts/vllm/configs)
in the MAD repository. Refer to the [vLLM engine](https://docs.vllm.ai/en/latest/configuration/engine_args.html#engineargs)
for descriptions of available configuration options
and [Benchmarking vLLM](https://github.com/vllm-project/vllm/blob/main/benchmarks/README.md) for
additional benchmarking information.

Launch the container

You can run the vLLM benchmark tool independently by starting the
[Docker container](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.10.1_20250909/images/sha256-1113268572e26d59b205792047bea0e61e018e79aeadceba118b7bf23cb3715c) as shown
in the following snippet.

```
pull rocm/vllm:rocm6.4.1_vllm_0.10.1_20250909
docker run -it \
--device=/dev/kfd \
--device=/dev/dri \
--group-add video \
--shm-size 16G \
--security-opt seccomp=unconfined \
--security-opt apparmor=unconfined \
--cap-add=SYS_PTRACE \
-v $(pwd):/workspace \
--env HUGGINGFACE_HUB_CACHE=/workspace \
--name test \
rocm/vllm:rocm6.4.1_vllm_0.10.1_20250909
```

Throughput command

Use the following command to start the throughput benchmark.

```
model=microsoft/phi-4
tp=1
num_prompts=1024
in=128
out=128
dtype=auto
kv_cache_dtype=auto
max_num_seqs=1024
max_seq_len_to_capture=16384
max_num_batched_tokens=16384
max_model_len=8192
vllm bench throughput --model $model \
-tp $tp \
--num-prompts $num_prompts \
--input-len $in \
--output-len $out \
--dtype $dtype \
--kv-cache-dtype $kv_cache_dtype \
--max-num-seqs $max_num_seqs \
--max-seq-len-to-capture $max_seq_len_to_capture \
--max-num-batched-tokens $max_num_batched_tokens \
--max-model-len $max_model_len \
--trust-remote-code \
--output-json ${model}_throughput.json \
--gpu-memory-utilization 0.9
```

Serving command

Start the server using the following command:

model=microsoft/phi-4 tp=1 dtype=auto kv_cache_dtype=auto max_num_seqs=256 max_seq_len_to_capture=16384 max_num_batched_tokens=16384 max_model_len=8192 vllm serve $model \ -tp $tp \ --dtype $dtype \ --kv-cache-dtype $kv_cache_dtype \ --max-num-seqs $max_num_seqs \ --max-seq-len-to-capture $max_seq_len_to_capture \ --max-num-batched-tokens $max_num_batched_tokens \ --max-model-len $max_model_len \ --no-enable-prefix-caching \ --swap-space 16 \ --disable-log-requests \ --trust-remote-code \ --gpu-memory-utilization 0.9

Wait until the model has loaded and the server is ready to accept requests.

On another terminal on the same machine, run the benchmark:

# Connect to the container docker exec -it test bash # Wait for the server to start until curl -s http://localhost:8000/v1/models; do sleep 30; done # Run the benchmark model=microsoft/phi-4 max_concurrency=1 num_prompts=10 in=128 out=128 vllm bench serve --model $model \ --percentile-metrics "ttft,tpot,itl,e2el" \ --dataset-name random \ --ignore-eos \ --max-concurrency $max_concurrency \ --num-prompts $num_prompts \ --random-input-len $in \ --random-output-len $out \ --trust-remote-code \ --save-result \ --result-filename ${model}_serving.json


Note

For improved performance with certain Mixture of Experts models, such as Mixtral 8x22B,
try adding `export VLLM_ROCM_USE_AITER=1`

to your commands.

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.


Note

Throughput is calculated as:

- \[throughput\_tot = requests \times (\mathsf{\text{input lengths}} + \mathsf{\text{output lengths}}) / elapsed\_time\]
- \[throughput\_gen = requests \times \mathsf{\text{output lengths}} / elapsed\_time\]

## Advanced usage[#](#advanced-usage)

For information on experimental features and known issues related to ROCm optimization efforts on vLLM,
see the developer’s guide at [ROCm/vllm](https://github.com/ROCm/vllm/blob/documentation/docs/dev-docker/README.md).

### Reproducing the Docker image[#](#reproducing-the-docker-image)

To reproduce this ROCm/vLLM Docker image release, follow these steps:

Clone the

[vLLM repository](https://github.com/ROCm/vllm).clone https://github.com/ROCm/vllm.git

Checkout the specific release commit.

cd vllm git checkout 6663000a391911eba96d7864a26ac42b07f6ef29

Build the Docker image. Replace

`vllm-rocm`

with your desired image tag.build -f docker/Dockerfile.rocm -t vllm-rocm .


## Further reading[#](#further-reading)

To learn more about the options for latency and throughput benchmark scripts, see

[ROCm/vllm](https://github.com/ROCm/vllm/tree/main/benchmarks).To learn more about MAD and the

`madengine`

CLI, see the[MAD usage guide](https://github.com/ROCm/MAD?tab=readme-ov-file#usage-guide).To learn more about system settings and management practices to configure your system for AMD Instinct MI300X Series accelerators, see

[AMD Instinct MI300X system optimization](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi300x.html).See

[vLLM inference](../../llm-inference-frameworks.html#fine-tuning-llms-vllm)and[vLLM V1 performance optimization](../../../inference-optimization/vllm-optimization.html#mi300x-vllm-optimization)for a brief introduction to vLLM and optimization strategies.For application performance optimization strategies for HPC and AI workloads, including inference with vLLM, see

[AMD Instinct MI300X workload optimization](../../../inference-optimization/workload.html).For a list of other ready-made Docker images for AI with ROCm, see

[AMD Infinity Hub](https://www.amd.com/en/developer/resources/infinity-hub.html#f-amd_hub_category=AI%20%26%20ML%20Models).

## Previous versions[#](#previous-versions)

See [vLLM inference performance testing version history](vllm-history.html) to find documentation for previous releases
of the `ROCm/vllm`

Docker image.
