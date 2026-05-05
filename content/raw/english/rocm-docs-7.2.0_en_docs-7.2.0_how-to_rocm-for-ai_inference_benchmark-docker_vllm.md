---
title: "vLLM inference"
source_url: "https://rocm.docs.amd.com/en/docs-7.2.0/how-to/rocm-for-ai/inference/benchmark-docker/vllm.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:02:15.795124+00:00
content_hash: "415ce3d2dd51a67d"
---

# vLLM inference[#](#vllm-inference)

2026-02-25

4 min read time

The [ROCm-enabled vLLM Docker image](https://hub.docker.com/r/vllm/vllm-openai-rocm/tags) offers a prebuilt,
optimized environment for large language model (LLM) inference on AMD Instinct
MI355X, MI350X, MI325X and MI300X GPUs. This ROCm vLLM Docker image integrates
vLLM and PyTorch tailored specifically for AMD Instinct data center GPUs.

This container integrates ROCm, PyTorch, and vLLM with optimizations tailored for AMD Instinct data center GPUs, enabling consistent and reproducible inference deployments.

## What’s new[#](#what-s-new)

For vLLM release notes on model support, hardware and performance improvements, and other highlights, see the

[vLLM Releases page](https://github.com/vllm-project/vllm/releases)on GitHub.It’s now recommended to use the upstream vLLM documentation at

[docs.vllm.ai](https://docs.vllm.ai)for the latest inference and deployment guides.

## Get started[#](#get-started)

For a consistent and portable inference environment, it’s recommended to use Docker. vLLM
offers a Docker image [vllm/vllm-openai-rocm](https://hub.docker.com/r/vllm/vllm-openai-rocm/tags) for deployment on AMD
GPUs. Use the following command to pull the latest Docker image from Docker Hub.

```
pull vllm/vllm-openai-rocm:latest
```

After pulling the Docker image, follow the vLLM usage documentation: [Using
vLLM](https://docs.vllm.ai/en/latest/usage/).

## Further reading[#](#further-reading)

See

[vLLM inference](../llm-inference-frameworks.html#fine-tuning-llms-vllm)and[vLLM V1 performance optimization](../../inference-optimization/vllm-optimization.html#mi300x-vllm-optimization)for a brief introduction to vLLM and optimization strategies.For a list of other ready-made Docker images for AI with ROCm, see

[AMD Infinity Hub](https://www.amd.com/en/developer/resources/infinity-hub.html#f-amd_hub_category=AI%20%26%20ML%20Models).

## Previous versions[#](#previous-versions)

It’s now recommended to use the upstream vLLM documentation at [docs.vllm.ai](https://docs.vllm.ai) for the latest deployment guides.

You can find legacy versions of this documentation at
[vLLM inference performance testing version history](previous-versions/vllm-history.html) which provide instructions for
inference performance testing for select models. See the [Use AMD’s Docker
images](https://docs.vllm.ai/en/stable/deployment/docker/#use-amds-docker-images)
note in the vLLM documentation for more information.
