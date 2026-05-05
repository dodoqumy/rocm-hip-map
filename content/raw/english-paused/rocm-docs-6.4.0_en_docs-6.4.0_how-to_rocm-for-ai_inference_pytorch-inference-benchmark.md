---
title: "PyTorch inference performance testing"
source_url: "https://rocm.docs.amd.com/en/docs-6.4.0/how-to/rocm-for-ai/inference/pytorch-inference-benchmark.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:21:27.672541+00:00
content_hash: "51c81f96d35c47a7"
---

# PyTorch inference performance testing[#](#pytorch-inference-performance-testing)

2025-05-13

6 min read time

The [ROCm PyTorch Docker](https://hub.docker.com/r/rocm/pytorch/tags) image offers a prebuilt,
optimized environment for testing model inference performance on AMD Instinct™ MI300X series
accelerators. This guide demonstrates how to use the AMD Model Automation and Dashboarding (MAD)
tool with the ROCm PyTorch container to test inference performance on various models efficiently.

## Supported models[#](#supported-models)

## System validation[#](#system-validation)

Before running AI workloads, it’s important to validate that your AMD hardware is configured correctly and performing optimally.

To optimize performance, disable automatic NUMA balancing. Otherwise, the GPU
might hang until the periodic balancing is finalized. For more information,
see the [system validation steps](../training/prerequisite-system-validation.html#rocm-for-ai-system-optimization).

```
# disable automatic NUMA balancing
sh -c 'echo 0 > /proc/sys/kernel/numa_balancing'
# check if NUMA balancing is disabled (returns 0 if disabled)
cat /proc/sys/kernel/numa_balancing
0
```

To test for optimal performance, consult the recommended [System health benchmarks](../system-health-check.html#rocm-for-ai-system-health-bench). This suite of tests will help you verify and fine-tune your
system’s configuration.

## Pull the Docker image[#](#pull-the-docker-image)

Use the following command to pull the [ROCm PyTorch Docker image](https://hub.docker.com/layers/rocm/pytorch/rocm6.2.3_ubuntu22.04_py3.10_pytorch_release_2.3.0_triton_llvm_reg_issue/images/sha256-b736a4239ab38a9d0e448af6d4adca83b117debed00bfbe33846f99c4540f79b) from Docker Hub.

```
pull rocm/pytorch:rocm6.2.3_ubuntu22.04_py3.10_pytorch_release_2.3.0_triton_llvm_reg_issue
```

Note

The Chai-1 benchmark uses a specifically selected Docker image using ROCm 6.2.3 and PyTorch 2.3.0 to address an accuracy issue.

## Benchmarking[#](#benchmarking)

To simplify performance testing, the ROCm Model Automation and Dashboarding
([ROCm/MAD](https://github.com/ROCm/MAD)) project provides ready-to-use scripts and configuration.
To start, clone the MAD repository to a local directory and install the required packages on the
host machine.

```
clone https://github.com/ROCm/MAD
cd MAD
pip install -r requirements.txt
```

Use this command to run the performance benchmark test on the [CLIP](https://huggingface.co/laion/CLIP-ViT-B-32-laion2B-s34B-b79K) model
using one GPU with the `float16`

data type on the host machine.

```
export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
python3 tools/run_models.py --tags pyt_clip_inference --keep-model-dir --live-output --timeout 28800
```

MAD launches a Docker container with the name
`container_ci-pyt_clip_inference`

. The latency and throughput reports of the
model are collected in `perf.csv`

.

Note

For improved performance, consider enabling TunableOp. By default,
`pyt_clip_inference`

runs with TunableOp disabled (see
[ROCm/MAD](https://github.com/ROCm/MAD/blob/develop/models.json)). To enable
it, edit the default run behavior in the `tools/run_models.py`

– update the model’s
run `args`

by changing `--tunableop off`

to `--tunableop on`

.

Enabling TunableOp triggers a two-pass run – a warm-up followed by the performance-collection run. Although this might increase the initial training time, it can result in a performance gain.

To simplify performance testing, the ROCm Model Automation and Dashboarding
([ROCm/MAD](https://github.com/ROCm/MAD)) project provides ready-to-use scripts and configuration.
To start, clone the MAD repository to a local directory and install the required packages on the
host machine.

```
clone https://github.com/ROCm/MAD
cd MAD
pip install -r requirements.txt
```

Use this command to run the performance benchmark test on the [Chai-1](https://huggingface.co/chaidiscovery/chai-1) model
using one GPU with the `float16`

data type on the host machine.

```
export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
python3 tools/run_models.py --tags pyt_chai1_inference --keep-model-dir --live-output --timeout 28800
```

MAD launches a Docker container with the name
`container_ci-pyt_chai1_inference`

. The latency and throughput reports of the
model are collected in `perf.csv`

.

Note

For improved performance, consider enabling TunableOp. By default,
`pyt_chai1_inference`

runs with TunableOp disabled (see
[ROCm/MAD](https://github.com/ROCm/MAD/blob/develop/models.json)). To enable
it, edit the default run behavior in the `tools/run_models.py`

– update the model’s
run `args`

by changing `--tunableop off`

to `--tunableop on`

.

Enabling TunableOp triggers a two-pass run – a warm-up followed by the performance-collection run. Although this might increase the initial training time, it can result in a performance gain.

## Further reading[#](#further-reading)

To learn more about system settings and management practices to configure your system for MI300X accelerators, see

[AMD Instinct MI300X system optimization](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi300x.html).To learn how to run LLM models from Hugging Face or your model, see

[Running models from Hugging Face](hugging-face-models.html).To learn how to optimize inference on LLMs, see

[Inference optimization](../inference-optimization/index.html).To learn how to fine-tune LLMs, see

[Fine-tuning LLMs](../fine-tuning/index.html).
