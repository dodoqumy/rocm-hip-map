---
title: "LLM inference frameworks"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference/llm-inference-frameworks.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-03T00:02:14.463756+00:00
content_hash: "2a08543dec348e60"
---

# LLM inference frameworks[#](#llm-inference-frameworks)

2026-01-23

8 min read time

This section discusses how to implement [vLLM](https://docs.vllm.ai/en/latest) and [Hugging Face TGI](https://huggingface.co/docs/text-generation-inference/en/index) using
[single-accelerator](../fine-tuning/single-gpu-fine-tuning-and-inference.html) and
[multi-accelerator](../fine-tuning/multi-gpu-fine-tuning-and-inference.html) systems.

## vLLM inference[#](#vllm-inference)

vLLM is renowned for its PagedAttention algorithm that can reduce memory consumption and increase throughput thanks to its paging scheme. Instead of allocating GPU high-bandwidth memory (HBM) for the maximum output token lengths of the models, the paged attention of vLLM allocates GPU HBM dynamically for its actual decoding lengths. This paged attention is also effective when multiple requests share the same key and value contents for a large value of beam search or multiple parallel requests.

vLLM also incorporates many modern LLM acceleration and quantization algorithms, such as Flash Attention, HIP and CUDA graphs, tensor parallel multi-GPU, GPTQ, AWQ, and token speculation.

### Installing vLLM[#](#installing-vllm)

Run the following commands to build a Docker image

`vllm-rocm`

.clone https://github.com/vllm-project/vllm.git cd vllm docker build -f docker/Dockerfile.rocm -t vllm-rocm .


To use vLLM as an API server to serve reference requests, first start a container using the

[vllm-rocm Docker image](#fine-tuning-llms-vllm-rocm-docker-image).run -it \ --network=host \ --group-add=video \ --ipc=host \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --device /dev/kfd \ --device /dev/dri \ -v <path/to/model>:/app/model \ vllm-rocm \ bash

Inside the container, start the API server to run on a single GPU on port 8000 using the following command.

-m vllm.entrypoints.api_server --model /app/model --dtype float16 --port 8000 &

The following log message is displayed in your command line indicates that the server is listening for requests.

To test, send it a curl request containing a prompt.

http://localhost:8000/generate -H "Content-Type: application/json" -d '{"prompt": "What is AMD Instinct?", "max_tokens": 80, "temperature": 0.0 }'

You should receive a response like the following.


To use vLLM as an API server to serve reference requests, first start a container using the

[vllm-rocm Docker image](#fine-tuning-llms-vllm-rocm-docker-image).run -it \ --network=host \ --group-add=video \ --ipc=host \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --device /dev/kfd \ --device /dev/dri \ -v <path/to/model>:/app/model \ vllm-rocm \ bash

To run API server on multiple GPUs, use the

`-tp`

or`--tensor-parallel-size`

parameter. For example, to use two GPUs, start the API server using the following command.-m vllm.entrypoints.api_server --model /app/model --dtype float16 -tp 2 --port 8000 &

To run multiple instances of API Servers, specify different ports for each server, and use

`ROCR_VISIBLE_DEVICES`

to isolate each instance to a different GPU.For example, to run two API servers, one on port 8000 using GPU 0 and 1, one on port 8001 using GPU 2 and 3, use a a command like the following.

ROCR_VISIBLE_DEVICES=0,1 python -m vllm.entrypoints.api_server --model /data/llama-2-7b-chat-hf --dtype float16 –tp 2 --port 8000 & ROCR_VISIBLE_DEVICES=2,3 python -m vllm.entrypoints.api_server --model /data/llama-2-7b-chat-hf --dtype float16 –tp 2--port 8001 &

To test, send it a curl request containing a prompt.

http://localhost:8000/generate -H "Content-Type: application/json" -d '{"prompt": "What is AMD Instinct?", "max_tokens": 80, "temperature": 0.0 }'

You should receive a response like the following.


See also

See [vLLM V1 performance optimization](../inference-optimization/vllm-optimization.html#mi300x-vllm-optimization) for performance optimization tips.

ROCm provides a prebuilt optimized Docker image for validating the performance of LLM inference with vLLM
on the MI300X GPU. The Docker image includes ROCm, vLLM, and PyTorch.
For more information, see [vLLM inference](benchmark-docker/vllm.html).

## Hugging Face TGI[#](#fine-tuning-llms-tgi)

Text Generation Inference (TGI) is LLM serving framework from Hugging Face, and it also supports the majority of high-performance LLM acceleration algorithms such as Flash Attention, Paged Attention, CUDA/HIP graph, tensor parallel multi-GPU, GPTQ, AWQ, and token speculation.

Tip

In addition to LLM serving capability, TGI also provides the [Text Generation Inference benchmarking tool](https://github.com/huggingface/text-generation-inference/blob/main/benchmark/README.md).

### Install TGI[#](#install-tgi)

Launch the TGI Docker container in the host machine.

run --name tgi --rm -it --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --device=/dev/kfd --device=/dev/dri --group-add video --ipc=host --shm-size 256g --net host -v $PWD:/data --entrypoint "/bin/bash" --env HUGGINGFACE_HUB_CACHE=/data ghcr.io/huggingface/text-generation-inference:latest-rocm


Inside the container, launch a model using TGI server on a single GPU.

export ROCM_USE_FLASH_ATTN_V2_TRITON=True text-generation-launcher --model-id NousResearch/Meta-Llama-3-70B --dtype float16 --port 8000 &

To test, send it a curl request containing a prompt.

http://localhost:8000/generate_stream -X POST -d '{"inputs":"What is AMD Instinct?","parameters":{"max_new_tokens":20}}' -H 'Content-Type: application/json'

You should receive a response like the following.

{"index":20,"token":{"id":304,"text":" in","logprob":-1.2822266,"special":false},"generated_text":" AMD Instinct is a new family of data center GPUs designed to accelerate the most demanding workloads in","details":null}


Inside the container, launch a model using TGI server on multiple GPUs (four in this case).

export ROCM_USE_FLASH_ATTN_V2_TRITON=True text-generation-launcher --model-id NousResearch/Meta-Llama-3-8B --dtype float16 --port 8000 --num-shard 4 &

To test, send it a curl request containing a prompt.

http://localhost:8000/generate_stream -X POST -d '{"inputs":"What is AMD Instinct?","parameters":{"max_new_tokens":20}}' -H 'Content-Type: application/json'

You should receive a response like the following.

{"index":20,"token":{"id":304,"text":" in","logprob":-1.2773438,"special":false},"generated_text":" AMD Instinct is a new family of data center GPUs designed to accelerate the most demanding workloads in","details":null}
