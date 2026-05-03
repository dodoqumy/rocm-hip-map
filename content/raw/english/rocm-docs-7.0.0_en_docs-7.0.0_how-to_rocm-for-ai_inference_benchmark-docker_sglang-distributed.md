---
title: "SGLang distributed inference with Mooncake"
source_url: "https://rocm.docs.amd.com/en/docs-7.0.0/how-to/rocm-for-ai/inference/benchmark-docker/sglang-distributed.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-03T00:03:19.709321+00:00
content_hash: "23ea648ee0c3d148"
---

# SGLang distributed inference with Mooncake[#](#sglang-distributed-inference-with-mooncake)

2025-09-16

9 min read time

As LLM inference increasingly demands handling massive models and dynamic workloads, efficient distributed inference becomes essential. Traditional co-located architectures face bottlenecks due to tightly coupled memory and compute resources, which limits scalability and flexibility. Disaggregated inference refers to the process of splitting the inference of LLMs into distinct phases. This architecture, facilitated by libraries like Mooncake, uses high-bandwidth RDMA to transfer the Key-Value (KV) cache between prefill and decode nodes. This allows for independent resource scaling and optimization, resulting in improved efficiency and throughput.

[SGLang](https://docs.sglang.ai) is a high-performance inference and
serving engine for large language models (LLMs) and vision models. The
ROCm-enabled [SGLang base Docker image](https://hub.docker.com/layers/lmsysorg/sglang/v0.5.2rc1-rocm700-mi30x/images/sha256-10c4ee502ddba44dd8c13325e6e03868bfe7f43d23d0a44780a8ee8b393f4729)
bundles SGLang with PyTorch, which is optimized for AMD Instinct MI300X series
accelerators. It includes the following software components:

Software component |
Version |
|---|---|
ROCm |
7.0.0 |
SGLang |
v0.5.2rc1 |
pytorch-triton-rocm |
3.4.0+rocm7.0.0.gitf9e5bf54 |

The following guides on setting up and running SGLang and Mooncake for disaggregated distributed inference on a Slurm cluster using AMD Instinct MI300X series accelerators backed by Mellanox CX-7 NICs.

## Prerequisites[#](#prerequisites)

Before starting, ensure you have:

A Slurm cluster with at least three nodes: one for the proxy, one for prefill (

`xP`

), and one for decode (`yD`

).`Nodes -> xP + yD + 1`

A Dockerized environment with SGLang, Mooncake, etcd, and NIC drivers built in. See

[Build the Docker image](#sglang-disagg-inf-build-docker-image)for instructions.A shared filesystem for storing models, scripts, and logs (cluster-specific).


## Supported models[#](#supported-models)

The following models are supported for SGLang disaggregated prefill/decode inference. Some instructions, commands, and recommendations in this documentation might vary by selected model.

Note

See the [Llama 3.1 8B Instruct model card on Hugging Face](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct) to learn more about this model.
Some models require access authorization prior to use through an external license agreement with a third party.

Note

See the [Llama 3.1 405B FP8 KV model card on Hugging Face](https://huggingface.co/amd/Llama-3.1-405B-Instruct-FP8-KV) to learn more about this model.
Some models require access authorization prior to use through an external license agreement with a third party.

Note

See the [Llama 3.3 70B FP8 KV model card on Hugging Face](https://huggingface.co/amd/Llama-3.3-70B-Instruct-FP8-KV) to learn more about this model.
Some models require access authorization prior to use through an external license agreement with a third party.

Note

See the [Mixtral 8x7B v0.1 model card on Hugging Face](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1) to learn more about this model.
Some models require access authorization prior to use through an external license agreement with a third party.

### Build the Docker image[#](#build-the-docker-image)

Get the Dockerfile located in
[ROCm/MAD](https://github.com/ROCm/MAD/blob/develop/docker/sglang_dissag_inference.ubuntu.amd.Dockerfile).
It uses [lmsysorg/sglang:v0.5.2rc1-rocm700-mi30x](https://hub.docker.com/layers/lmsysorg/sglang/v0.4.9.post1-rocm630/images/sha256-2f6b1748e4bcc70717875a7da76c87795fd8aa46a9646e08d38aa7232fc78538)
as the base Docker image and installs the necessary components for Mooncake, etcd, and Mellanox network
drivers.

```
clone https://github.com/ROCm/MAD.git
cd MAD/docker
docker build \
-t sglang_disagg_pd_image \
-f sglang_disagg_inference.ubuntu.amd.Dockerfile .
```

## Benchmarking[#](#benchmarking)

The [ROCm/MAD](https://github.com/ROCm/MAD/tree/develop/scripts/sglang_dissag)
repository contains scripts to launch SGLang inference with prefill/decode
disaggregation via Mooncake for supported models.

[scripts/sglang_dissag/run_xPyD_models.slurm](https://github.com/ROCm/MAD/blob/develop/scripts/sglang_disagg/run_xPyD_models.slurm)– the main Slurm batch script to launch Docker containers on all nodes using`sbatch`

or`salloc`

.[scripts/sglang_dissag/sglang_disagg_server.sh](https://github.com/ROCm/MAD/blob/develop/scripts/sglang_disagg/sglang_disagg_server.sh)– the entrypoint script that runs inside each container to start the correct service – proxy, prefill, or decode.[scripts/sglang_dissag/benchmark_xPyD.sh](https://github.com/ROCm/MAD/blob/develop/scripts/sglang_disagg/benchmark_xPyD.sh)– the benchmark script to run the GSM8K accuracy benchmark and the SGLang benchmarking tool for performance measurement.[scripts/sglang_dissag/benchmark_parser.py](https://github.com/ROCm/MAD/blob/develop/scripts/sglang_disagg/benchmark_parser.py)– the log parser script to be run on the concurrency benchmark log file to generate tabulated data.

### Launch the service[#](#launch-the-service)

The service is deployed using a Slurm batch script that orchestrates the containers across the allocated nodes.

```
# Clone the MAD repo if you haven't already and
# navigate to the scripts directory
git clone https://github.com/ROCm/MAD.git
cd MAD/scripts/sglang_disagg/
# Slurm sbatch run command
export DOCKER_IMAGE_NAME=sglang_disagg_pd_image
export xP=<num_prefill_nodes>
export yD=<num_decode_nodes>
export MODEL_NAME=Llama-3.1-8B-Instruct
# num_nodes = xP + yD + 1
sbatch -N <num_nodes> -n <num_nodes> --nodelist=<Nodes> run_xPyD_models.slurm
```

```
# Clone the MAD repo if you haven't already and
# navigate to the scripts directory
git clone https://github.com/ROCm/MAD.git
cd MAD/scripts/sglang_disagg/
# Slurm sbatch run command
export DOCKER_IMAGE_NAME=sglang_disagg_pd_image
export xP=<num_prefill_nodes>
export yD=<num_decode_nodes>
export MODEL_NAME=Llama-3.1-405B-Instruct-FP8-KV
# num_nodes = xP + yD + 1
sbatch -N <num_nodes> -n <num_nodes> --nodelist=<Nodes> run_xPyD_models.slurm
```

```
# Clone the MAD repo if you haven't already and
# navigate to the scripts directory
git clone https://github.com/ROCm/MAD.git
cd MAD/scripts/sglang_disagg/
# Slurm sbatch run command
export DOCKER_IMAGE_NAME=sglang_disagg_pd_image
export xP=<num_prefill_nodes>
export yD=<num_decode_nodes>
export MODEL_NAME=amd-Llama-3.3-70B-Instruct-FP8-KV
# num_nodes = xP + yD + 1
sbatch -N <num_nodes> -n <num_nodes> --nodelist=<Nodes> run_xPyD_models.slurm
```

```
# Clone the MAD repo if you haven't already and
# navigate to the scripts directory
git clone https://github.com/ROCm/MAD.git
cd MAD/scripts/sglang_disagg/
# Slurm sbatch run command
export DOCKER_IMAGE_NAME=sglang_disagg_pd_image
export xP=<num_prefill_nodes>
export yD=<num_decode_nodes>
export MODEL_NAME=Qwen3-32B
# num_nodes = xP + yD + 1
sbatch -N <num_nodes> -n <num_nodes> --nodelist=<Nodes> run_xPyD_models.slurm
```

```
# Clone the MAD repo if you haven't already and
# navigate to the scripts directory
git clone https://github.com/ROCm/MAD.git
cd MAD/scripts/sglang_disagg/
# Slurm sbatch run command
export DOCKER_IMAGE_NAME=sglang_disagg_pd_image
export xP=<num_prefill_nodes>
export yD=<num_decode_nodes>
export MODEL_NAME=DeepSeek-V3
# num_nodes = xP + yD + 1
sbatch -N <num_nodes> -n <num_nodes> --nodelist=<Nodes> run_xPyD_models.slurm
```

```
# Clone the MAD repo if you haven't already and
# navigate to the scripts directory
git clone https://github.com/ROCm/MAD.git
cd MAD/scripts/sglang_disagg/
# Slurm sbatch run command
export DOCKER_IMAGE_NAME=sglang_disagg_pd_image
export xP=<num_prefill_nodes>
export yD=<num_decode_nodes>
export MODEL_NAME=Mixtral-8x7B-v0.1
# num_nodes = xP + yD + 1
sbatch -N <num_nodes> -n <num_nodes> --nodelist=<Nodes> run_xPyD_models.slurm
```

### Post-run logs and testing[#](#post-run-logs-and-testing)

Logs are stored in your shared filesystem in the directory specified by the `LOG_PATH`

variable in the Slurm script.
A new directory named after the Slurm job ID is created for each run.

Inside that directory, you can access various logs:

`pd_sglang_bench_serving.sh_NODE<...>.log`

– the main log for each server node.`etcd_NODE<...>.log`

– logs for etcd services.`prefill_NODE<...>.log`

– logs for the prefill services.`decode_NODE<...>.log`

– logs for the decode services.

Use the benchmark parser script for concurrency logs to tabulate different data.

```
benchmark_parser.py <log_path/benchmark_XXX_CONCURRENCY.log>
```

To verify the service is responsive, you can try sending a `curl`

request to test the launched
server from the Docker container on the proxy node. For example:

```
-X POST http://127.0.0.1:30000/generate \
-H "Content-Type: application/json" \
-d '{ "text": "Let me tell you a story ", "sampling_params": { "temperature": 0.3 } }'
```

## Known issues[#](#known-issues)

When running larger models, such as DeepSeek-V3 and Llama-3.1-405B-Instruct-FP8-KV, at higher concurrency levels (512+), the following error might occur:

```
<TransferEncodingError: 400, message:
Not enough data to satisfy transfer length header.
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
...
```

This leads to dropping requests and lower throughput.

## Further reading[#](#further-reading)

To learn about Mooncake, see

[Welcome to Mooncake](https://kvcache-ai.github.io/Mooncake/).To learn more about the options for latency and throughput benchmark scripts, see

[sgl-project/sglang](https://github.com/sgl-project/sglang/tree/main/benchmark/blog_v0_2).See the base upstream Docker image on

[Docker Hub](https://hub.docker.com/layers/lmsysorg/sglang/v0.5.2rc1-rocm700-mi30x/images/sha256-10c4ee502ddba44dd8c13325e6e03868bfe7f43d23d0a44780a8ee8b393f4729).To learn more about system settings and management practices to configure your system for MI300X series accelerators, see

[AMD Instinct MI300X system optimization](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi300x.html).For application performance optimization strategies for HPC and AI workloads, including inference with vLLM, see

[AMD Instinct MI300X workload optimization](../../inference-optimization/workload.html).To learn how to run community models from Hugging Face on AMD GPUs, see

[Running models from Hugging Face](../hugging-face-models.html).To learn how to fine-tune LLMs and optimize inference, see

[Fine-tuning LLMs and inference optimization](../../fine-tuning/fine-tuning-and-inference.html).For a list of other ready-made Docker images for AI with ROCm, see

[AMD Infinity Hub](https://www.amd.com/en/developer/resources/infinity-hub.html#f-amd_hub_category=AI%20%26%20ML%20Models).

## Previous versions[#](#previous-versions)

See [SGLang inference performance testing version history](previous-versions/sglang-history.html) to find documentation for previous releases
of SGLang inference performance testing.
