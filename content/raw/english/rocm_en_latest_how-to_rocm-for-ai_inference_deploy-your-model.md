---
title: "Deploying your model"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference/deploy-your-model.html"
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
- Deploying your model

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons
[]{.fa-solid .fa-list}

# Deploying your model

## Contents

- [Serving using vLLM](#serving-using-vllm){.reference .internal .nav-link}
  - [vLLM installation](#vllm-installation){.reference .internal .nav-link}
  - [vLLM walkthrough](#vllm-walkthrough){.reference .internal .nav-link}
  - [Validating vLLM performance](#validating-vllm-performance){.reference .internal .nav-link}
- [Serving using Hugging Face TGI](#serving-using-hugging-face-tgi){.reference .internal .nav-link}
  - [TGI installation](#tgi-installation){.reference .internal .nav-link}
  - [TGI walkthrough](#tgi-walkthrough){.reference .internal .nav-link}


# Deploying your model[\#](#deploying-your-model "Link to this heading"){.headerlink}

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 5 min read time

Applies to Linux


ROCm enables inference and deployment for various classes of models including CNN, RNN, LSTM, MLP, and transformers. This section focuses on deploying transformers-based LLM models.

ROCm supports vLLM and Hugging Face TGI as major LLM-serving frameworks.


## Serving using vLLM[\#](#serving-using-vllm "Link to this heading"){.headerlink}

vLLM is a fast and easy-to-use library for LLM inference and serving. AMD is actively working with the vLLM team to improve performance and support the latest ROCm versions.

See the [GitHub repository](https://github.com/vllm-project/vllm){.reference .external} and [official vLLM documentation](https://docs.vllm.ai/){.reference .external} for more information.

For guidance on using vLLM with ROCm, refer to [Installation with ROCm](https://docs.vllm.ai/en/stable/getting_started/installation/gpu.html#amd-rocm){.reference .external}.

### vLLM installation[\#](#vllm-installation "Link to this heading"){.headerlink}

vLLM supports two ROCm-capable installation methods. Refer to the official documentation use the following links.

- [Build from source with Docker](https://docs.vllm.ai/en/latest/getting_started/installation/gpu.html?device=rocm#build-image-from-source){.reference .external} (recommended)

- [Build from source](https://docs.vllm.ai/en/latest/getting_started/installation/gpu.html?device=rocm#build-wheel-from-source){.reference .external}

### vLLM walkthrough[\#](#vllm-walkthrough "Link to this heading"){.headerlink}

Refer to this developer blog for guidance on serving with vLLM [Inferencing and serving with vLLM on AMD GPUs --- ROCm Blogs](https://rocm.blogs.amd.com/artificial-intelligence/vllm/README.html){.reference .external}

### Validating vLLM performance[\#](#validating-vllm-performance "Link to this heading"){.headerlink}

ROCm provides a prebuilt optimized Docker image for validating the performance of LLM inference with vLLM on the MI300X GPU. The Docker image includes ROCm, vLLM, PyTorch, and tuning files in the CSV format. For more information, see the guide to [LLM inference performance testing with vLLM on the AMD Instinct™ MI300X GPU](https://github.com/ROCm/MAD/blob/develop/benchmark/vllm/README.md){.reference .external} on the ROCm GitHub repository.


## Serving using Hugging Face TGI[\#](#serving-using-hugging-face-tgi "Link to this heading"){.headerlink}

The [Hugging Face Text Generation Inference](https://huggingface.co/docs/text-generation-inference/index){.reference .external} (TGI) library is optimized for serving LLMs with low latency. Refer to the [Quick tour of TGI](https://huggingface.co/docs/text-generation-inference/quicktour){.reference .external} for more details.

### TGI installation[\#](#tgi-installation "Link to this heading"){.headerlink}

The easiest way to use Hugging Face TGI with ROCm on AMD Instinct GPUs is to use the official Docker image at [huggingface/text-generation-inference](https://github.com/huggingface/text-generation-inference/pkgs/container/text-generation-inference){.github .reference .external}.

### TGI walkthrough[\#](#tgi-walkthrough "Link to this heading"){.headerlink}

1.  Set up the LLM server.

    Deploy the Llama2 7B model with TGI using the official Docker image.

    ::: highlight
        model=TheBloke/Llama-2-7B-fp16
        volume=$PWD
        docker run --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --device=/dev/kfd --device=/dev/dri --group-add video --ipc=host --shm-size 1g -p 8080:80 -v $volume:/data --name tgi_amd ghcr.io/huggingface/text-generation-inference:1.2-rocm --model-id $model

2.  Set up the client.

    1.  Open another shell session and run the following command to access the server with the client URL.

    ::: highlight
        curl 127.0.0.1:8080/generate \\
        -X POST \\
        -d '{"inputs":"What is Deep
        Learning?","parameters":{"max_new_tokens":20}}' \\
        -H 'Content-Type: application/json'

    2.  Access the server with request endpoints.

    ::: highlight
        pip install request
        PYTHONPATH=/usr/lib/python3/dist-packages python requests_model.py

        ``requests_model.py`` should look like:

        .. code-block:: python

           import requests

           headers = {
             "Content-Type": "application/json",
           }

           data = {
              'inputs': 'What is Deep Learning?',
              'parameters': { 'max_new_tokens': 20 },
           }

           response = requests.post('http://127.0.0.1:8080/generate', headers=headers, json=data)

           print(response.json())

vLLM and Hugging Face TGI are robust solutions for anyone looking to deploy LLMs for applications that demand high performance, low latency, and scalability.

Visit the topics in [[Using ROCm for AI]{.doc}](../index.html){.reference .internal} to learn about other ROCm-aware solutions for AI development.

::::: prev-next-area
[](xdit-diffusion-inference.html "previous page"){.left-prev}

::: prev-next-info
previous

xDiT diffusion inference

[](../inference-optimization/index.html "next page"){.right-next}

::: prev-next-info
next

Use ROCm for AI inference optimization

:::: sidebar-secondary-item
Contents

- [Serving using vLLM](#serving-using-vllm){.reference .internal .nav-link}
  - [vLLM installation](#vllm-installation){.reference .internal .nav-link}
  - [vLLM walkthrough](#vllm-walkthrough){.reference .internal .nav-link}
  - [Validating vLLM performance](#validating-vllm-performance){.reference .internal .nav-link}
- [Serving using Hugging Face TGI](#serving-using-hugging-face-tgi){.reference .internal .nav-link}
  - [TGI installation](#tgi-installation){.reference .internal .nav-link}
  - [TGI walkthrough](#tgi-walkthrough){.reference .internal .nav-link}
