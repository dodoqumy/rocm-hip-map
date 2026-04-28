---
title: "LLM inference frameworks"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference/llm-inference-frameworks.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-04-28
---

::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}

::: header-article-item
- [](../../../index.html){.nav-link aria-label="Home"}
- [Use ROCm for AI](../index.html){.nav-link}
- [Use ROCm for AI inference](index.html){.nav-link}
- LLM\...

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons
[]{.fa-solid .fa-list}

# LLM inference frameworks

## Contents

- [vLLM inference](#vllm-inference){.reference .internal .nav-link}
  - [Installing vLLM](#installing-vllm){.reference .internal .nav-link}
- [Hugging Face TGI](#fine-tuning-llms-tgi){.reference .internal .nav-link}
  - [Install TGI](#install-tgi){.reference .internal .nav-link}


# LLM inference frameworks[\#](#llm-inference-frameworks "Link to this heading"){.headerlink}

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 8 min read time

Applies to Linux


This section discusses how to implement [vLLM](https://docs.vllm.ai/en/latest){.reference .external} and [Hugging Face TGI](https://huggingface.co/docs/text-generation-inference/en/index){.reference .external} using [[single-accelerator]{.doc}](../fine-tuning/single-gpu-fine-tuning-and-inference.html){.reference .internal} and [[multi-accelerator]{.doc}](../fine-tuning/multi-gpu-fine-tuning-and-inference.html){.reference .internal} systems.


## vLLM inference[\#](#vllm-inference "Link to this heading"){.headerlink}

vLLM is renowned for its PagedAttention algorithm that can reduce memory consumption and increase throughput thanks to its paging scheme. Instead of allocating GPU high-bandwidth memory (HBM) for the maximum output token lengths of the models, the paged attention of vLLM allocates GPU HBM dynamically for its actual decoding lengths. This paged attention is also effective when multiple requests share the same key and value contents for a large value of beam search or multiple parallel requests.

vLLM also incorporates many modern LLM acceleration and quantization algorithms, such as Flash Attention, HIP and CUDA graphs, tensor parallel multi-GPU, GPTQ, AWQ, and token speculation.

### Installing vLLM[\#](#installing-vllm "Link to this heading"){.headerlink}

1.  Run the following commands to build a Docker image [`vllm-rocm`{.docutils .literal .notranslate}]{.pre}.

    ::: highlight
        git clone https://github.com/vllm-project/vllm.git
        cd vllm
        docker build -f docker/Dockerfile.rocm -t vllm-rocm .

vLLM on a single-accelerator system

2.  To use vLLM as an API server to serve reference requests, first start a container using the [[vllm-rocm Docker image]{.std .std-ref}](#fine-tuning-llms-vllm-rocm-docker-image){.reference .internal}.

    ::: highlight
        docker run -it \
           --network=host \
           --group-add=video \
           --ipc=host \
           --cap-add=SYS_PTRACE \
           --security-opt seccomp=unconfined \
           --device /dev/kfd \
           --device /dev/dri \
           -v <path/to/model>:/app/model \
           vllm-rocm \
           bash

3.  Inside the container, start the API server to run on a single GPU on port 8000 using the following command.

    ::: highlight
        python -m vllm.entrypoints.api_server --model /app/model --dtype float16 --port 8000 &

    The following log message is displayed in your command line indicates that the server is listening for requests.

    ![vLLM API server log message](../../../_images/vllm-single-gpu-log.png){.align-center}

4.  To test, send it a curl request containing a prompt.

    ::: highlight
        curl http://localhost:8000/generate -H "Content-Type: application/json" -d '{"prompt": "What is AMD Instinct?", "max_tokens": 80, "temperature": 0.0 }'

    You should receive a response like the following.

    ::: highlight
        {"text":["What is AMD Instinct?\nAmd Instinct is a brand new line of high-performance computing (HPC) processors from Advanced Micro Devices (AMD). These processors are designed to deliver unparalleled performance for HPC workloads, including scientific simulations, data analytics, and machine learning.\nThe Instinct lineup includes a range of processors, from the entry-level Inst"]}

vLLM on a multi-accelerator system

2.  To use vLLM as an API server to serve reference requests, first start a container using the [[vllm-rocm Docker image]{.std .std-ref}](#fine-tuning-llms-vllm-rocm-docker-image){.reference .internal}.

    ::: highlight
        docker run -it \
           --network=host \
           --group-add=video \
           --ipc=host \
           --cap-add=SYS_PTRACE \
           --security-opt seccomp=unconfined \
           --device /dev/kfd \
           --device /dev/dri \
           -v <path/to/model>:/app/model \
           vllm-rocm \
           bash

3.  To run API server on multiple GPUs, use the [`-tp`{.docutils .literal .notranslate}]{.pre} or [`--tensor-parallel-size`{.docutils .literal .notranslate}]{.pre} parameter. For example, to use two GPUs, start the API server using the following command.

    ::: highlight
        python -m vllm.entrypoints.api_server --model /app/model --dtype float16 -tp 2 --port 8000 &

4.  To run multiple instances of API Servers, specify different ports for each server, and use [`ROCR_VISIBLE_DEVICES`{.docutils .literal .notranslate}]{.pre} to isolate each instance to a different GPU.

    For example, to run two API servers, one on port 8000 using GPU 0 and 1, one on port 8001 using GPU 2 and 3, use a a command like the following.

    ::: highlight
        ROCR_VISIBLE_DEVICES=0,1 python -m vllm.entrypoints.api_server --model /data/llama-2-7b-chat-hf --dtype float16 –tp 2 --port 8000 &
        ROCR_VISIBLE_DEVICES=2,3 python -m vllm.entrypoints.api_server --model /data/llama-2-7b-chat-hf --dtype float16 –tp 2--port 8001 &

5.  To test, send it a curl request containing a prompt.

    ::: highlight
        curl http://localhost:8000/generate -H "Content-Type: application/json" -d '{"prompt": "What is AMD Instinct?", "max_tokens": 80, "temperature": 0.0 }'

    You should receive a response like the following.

    ::: highlight
        {"text":["What is AMD Instinct?\nAmd Instinct is a brand new line of high-performance computing (HPC) processors from Advanced Micro Devices (AMD). These processors are designed to deliver unparalleled performance for HPC workloads, including scientific simulations, data analytics, and machine learning.\nThe Instinct lineup includes a range of processors, from the entry-level Inst"]}

See also

See [[vLLM V1 performance optimization]{.std .std-ref}](../inference-optimization/vllm-optimization.html#mi300x-vllm-optimization){.reference .internal} for performance optimization tips.

ROCm provides a prebuilt optimized Docker image for validating the performance of LLM inference with vLLM on the MI300X GPU. The Docker image includes ROCm, vLLM, and PyTorch. For more information, see [[vLLM inference]{.doc}](benchmark-docker/vllm.html){.reference .internal}.


## Hugging Face TGI[\#](#fine-tuning-llms-tgi "Link to this heading"){.headerlink}

Text Generation Inference (TGI) is LLM serving framework from Hugging Face, and it also supports the majority of high-performance LLM acceleration algorithms such as Flash Attention, Paged Attention, CUDA/HIP graph, tensor parallel multi-GPU, GPTQ, AWQ, and token speculation.

Tip

In addition to LLM serving capability, TGI also provides the [Text Generation Inference benchmarking tool](https://github.com/huggingface/text-generation-inference/blob/main/benchmark/README.md){.reference .external}.

### Install TGI[\#](#install-tgi "Link to this heading"){.headerlink}

1.  Launch the TGI Docker container in the host machine.

    ::: highlight
        docker run --name tgi --rm -it --cap-add=SYS_PTRACE --security-opt seccomp=unconfined
        --device=/dev/kfd --device=/dev/dri --group-add video --ipc=host --shm-size 256g
        --net host -v $PWD:/data
        --entrypoint "/bin/bash"
        --env HUGGINGFACE_HUB_CACHE=/data
        ghcr.io/huggingface/text-generation-inference:latest-rocm

TGI on a single-accelerator system

2.  Inside the container, launch a model using TGI server on a single GPU.

    ::: highlight
        export ROCM_USE_FLASH_ATTN_V2_TRITON=True
        text-generation-launcher --model-id NousResearch/Meta-Llama-3-70B --dtype float16 --port 8000 &

3.  To test, send it a curl request containing a prompt.

    ::: highlight
        curl http://localhost:8000/generate_stream -X POST -d '{"inputs":"What is AMD Instinct?","parameters":{"max_new_tokens":20}}' -H 'Content-Type: application/json'

    You should receive a response like the following.

    ::: highlight
        data:{"index":20,"token":{"id":304,"text":" in","logprob":-1.2822266,"special":false},"generated_text":" AMD Instinct is a new family of data center GPUs designed to accelerate the most demanding workloads in","details":null}

TGI on a multi-accelerator system

2.  Inside the container, launch a model using TGI server on multiple GPUs (four in this case).

    ::: highlight
        export ROCM_USE_FLASH_ATTN_V2_TRITON=True
        text-generation-launcher --model-id NousResearch/Meta-Llama-3-8B --dtype float16 --port 8000 --num-shard 4 &

3.  To test, send it a curl request containing a prompt.

    ::: highlight
        curl http://localhost:8000/generate_stream -X POST -d '{"inputs":"What is AMD Instinct?","parameters":{"max_new_tokens":20}}' -H 'Content-Type: application/json'

    You should receive a response like the following.

    ::: highlight
        data:{"index":20,"token":{"id":304,"text":" in","logprob":-1.2773438,"special":false},"generated_text":" AMD Instinct is a new family of data center GPUs designed to accelerate the most demanding workloads in","details":null}

::::: prev-next-area
[](hugging-face-models.html "previous page"){.left-prev}

::: prev-next-info
previous

Running models from Hugging Face

[](benchmark-docker/vllm.html "next page"){.right-next}

::: prev-next-info
next

vLLM inference

:::: sidebar-secondary-item
Contents

- [vLLM inference](#vllm-inference){.reference .internal .nav-link}
  - [Installing vLLM](#installing-vllm){.reference .internal .nav-link}
- [Hugging Face TGI](#fine-tuning-llms-tgi){.reference .internal .nav-link}
  - [Install TGI](#install-tgi){.reference .internal .nav-link}
