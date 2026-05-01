---
title: "Model acceleration libraries"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference-optimization/model-acceleration-libraries.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-01
---

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-content
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-article-container
:::::::::: {.bd-header-article .d-print-none}
::::::::: {.header-article-items .header-article__inner}
::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}
:::

::: header-article-item
- [](../../../index.html){.nav-link aria-label="Home"}
- [Use ROCm for AI](../index.html){.nav-link}
- [Use ROCm for AI inference optimization](index.html){.nav-link}
- Model\...
:::
:::::

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons
[]{.fa-solid .fa-list}
:::
::::
:::::
:::::::::
::::::::::

:::::: {#jb-print-docs-body .onlyprint}
# Model acceleration libraries

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [Flash Attention 2](#flash-attention-2){.reference .internal .nav-link}
  - [Installation prerequisites](#installation-prerequisites){.reference .internal .nav-link}
  - [Installing Flash Attention 2](#installing-flash-attention-2){.reference .internal .nav-link}
  - [Benchmarking Flash Attention 2](#benchmarking-flash-attention-2){.reference .internal .nav-link}
  - [Using Flash Attention 2](#using-flash-attention-2){.reference .internal .nav-link}
- [xFormers](#xformers){.reference .internal .nav-link}
  - [Installing CK xFormers](#installing-ck-xformers){.reference .internal .nav-link}
- [PyTorch built-in acceleration](#pytorch-built-in-acceleration){.reference .internal .nav-link}
  - [PyTorch compilation](#pytorch-compilation){.reference .internal .nav-link}
  - [PyTorch TunableOp](#pytorch-tunableop){.reference .internal .nav-link}
- [FBGEMM and FBGEMM_GPU](#fbgemm-and-fbgemm-gpu){.reference .internal .nav-link}
  - [Installing FBGEMM_GPU](#installing-fbgemm-gpu){.reference .internal .nav-link}
    - [Set up the Miniconda environment](#set-up-the-miniconda-environment){.reference .internal .nav-link}
    - [Install the ROCm components](#install-the-rocm-components){.reference .internal .nav-link}
    - [Install PyTorch](#install-pytorch){.reference .internal .nav-link}
    - [Perform the prebuild and build](#perform-the-prebuild-and-build){.reference .internal .nav-link}
  - [Post-build validation](#post-build-validation){.reference .internal .nav-link}
  - [Testing FBGEMM](#testing-fbgemm){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#model-acceleration-libraries .section}
# Model acceleration libraries[\#](#model-acceleration-libraries "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 15 min read time
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils style="color:gray;"}
Applies to Linux
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
:::
:::::::
::::::::
:::::::::
::::::::::
:::::::::::

This section discusses model acceleration techniques and libraries to improve memory efficiency and performance.

::::::::::::::::: {#flash-attention-2 .section}
[]{#acceleration-flash-attention}

## Flash Attention 2[\#](#flash-attention-2 "Link to this heading"){.headerlink}

Flash Attention is a technique designed to reduce memory movements between GPU SRAM and high-bandwidth memory (HBM). By using a tiling approach, Flash Attention 2 improves memory locality in the nested loops of query, key, and value computations within the Attention modules of LLMs. These modules include Multi-Head Attention (MHA), Group-Query Attention (GQA), and Multi-Query Attention (MQA). This reduction in memory movements significantly decreases the time-to-first-token (TTFT) latency for large batch sizes and long prompt sequences, thereby enhancing overall performance.

![Attention module of a large language module utilizing tiling](../../../_images/attention-module.png){.align-center}

::: {#installation-prerequisites .section}
### Installation prerequisites[\#](#installation-prerequisites "Link to this heading"){.headerlink}

Before installing Flash Attention 2, ensure the following are available:

- ROCm-enabled PyTorch

- Triton

These can be installed by following the official [PyTorch installation guide](https://pytorch.org/get-started/locally/){.reference .external}. Alternatively, for a simpler setup, you can use a preconfigured [[ROCm PyTorch Docker image]{.xref .std .std-ref}](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/pytorch-install.html#using-docker-with-pytorch-pre-installed "(in ROCm installation on Linux v7.2.2)"){.reference .external}, which already includes the required libraries.
:::

::::: {#installing-flash-attention-2 .section}
### Installing Flash Attention 2[\#](#installing-flash-attention-2 "Link to this heading"){.headerlink}

[Flash Attention](https://github.com/Dao-AILab/flash-attention){.reference .external} supports two backend implementations on AMD GPUs.

- [Composable Kernel (CK)](https://github.com/ROCm/composable_kernel){.reference .external} - the default backend

- [OpenAI Triton](https://github.com/triton-lang/triton){.reference .external} - an alternative backend

You can switch between these backends using the environment variable [`FLASH_ATTENTION_TRITON_AMD_ENABLE`{.docutils .literal .notranslate}]{.pre}:

[`FLASH_ATTENTION_TRITON_AMD_ENABLE="FALSE"`{.docutils .literal .notranslate}]{.pre} → Use Composable Kernel (CK) backend (Flash Attention 2)

[`FLASH_ATTENTION_TRITON_AMD_ENABLE="TRUE"`{.docutils .literal .notranslate}]{.pre} → Use OpenAI Triton backend (Flash Attention 2)

To install Flash Attention 2, use the following commands:

:::: {.highlight-shell .notranslate}
::: highlight
    git clone https://github.com/Dao-AILab/flash-attention.git
    cd flash-attention/
    pip install ninja

    # To install the CK backend flash attention
    python setup.py install

    # To install the Triton backend flash attention
    FLASH_ATTENTION_TRITON_AMD_ENABLE="TRUE" python setup.py install

    # To install both CK and Triton backend flash attention
    FLASH_ATTENTION_TRITON_AMD_ENABLE=TRUE && FLASH_ATTENTION_SKIP_CK_BUILD=FALSE python setup.py install
:::
::::

For detailed installation instructions, see [Flash Attention](https://github.com/Dao-AILab/flash-attention){.reference .external}.
:::::

::::::: {#benchmarking-flash-attention-2 .section}
### Benchmarking Flash Attention 2[\#](#benchmarking-flash-attention-2 "Link to this heading"){.headerlink}

Benchmark scripts to evaluate the performance of Flash Attention 2 are stored in the [`flash-attention/benchmarks/`{.docutils .literal .notranslate}]{.pre} directory.

To benchmark the CK backend

:::: {.highlight-shell .notranslate}
::: highlight
    cd flash-attention/benchmarks
    pip install transformers einops ninja

    python3 benchmark_flash_attention.py
:::
::::

To benchmark the Triton backend

:::: {.highlight-shell .notranslate}
::: highlight
    FLASH_ATTENTION_TRITON_AMD_ENABLE="TRUE" python3 benchmark_flash_attention.py
:::
::::
:::::::

::::::: {#using-flash-attention-2 .section}
### Using Flash Attention 2[\#](#using-flash-attention-2 "Link to this heading"){.headerlink}

:::: {.highlight-python .notranslate}
::: highlight
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    model_name = "NousResearch/Llama-3.2-1B"

    tokenizer = AutoTokenizer.from_pretrained(model_name, dtype=torch.bfloat16, use_fast=False)
    inputs = tokenizer('Today is', return_tensors='pt').to(device)

    model_eager = AutoModelForCausalLM.from_pretrained(model_name, dtype=torch.bfloat16, attn_implementation="eager").cuda(device)
    model_ckFAv2 = AutoModelForCausalLM.from_pretrained(model_name, dtype=torch.bfloat16, attn_implementation="flash_attention_2").cuda(device)
    model_eager.generation_config.pad_token_id = model_eager.generation_config.eos_token_id
    model_ckFAv2.generation_config.pad_token_id = model_ckFAv2.generation_config.eos_token_id

    print("eager\n GQA: ", tokenizer.decode(model_eager.generate(**inputs, max_new_tokens=22)[0], skip_special_tokens=True, do_sample=False, num_beams=1))
    print("ckFAv2\n GQA: ", tokenizer.decode(model_ckFAv2.generate(**inputs, max_new_tokens=22)[0], skip_special_tokens=True, do_sample=False, num_beams=1))
:::
::::

The outputs from eager mode and FlashAttention-2 are identical, although their performance behavior differs.

:::: {.highlight-shell .notranslate}
::: highlight
    eager
    GQA:  Today is the 10th anniversary of the 9/11 attacks. I remember that day like it was yesterday.
    ckFAv2
    GQA:  Today is the 10th anniversary of the 9/11 attacks. I remember that day like it was yesterday.
:::
::::
:::::::
:::::::::::::::::

:::::: {#xformers .section}
## xFormers[\#](#xformers "Link to this heading"){.headerlink}

xFormers also improves the performance of attention modules. Although xFormers attention performs very similarly to Flash Attention 2 due to its tiling behavior of query, key, and value, it's widely used for LLMs and Stable Diffusion models with the Hugging Face Diffusers library.

::::: {#installing-ck-xformers .section}
### Installing CK xFormers[\#](#installing-ck-xformers "Link to this heading"){.headerlink}

Use the following commands to install CK xFormers.

:::: {.highlight-shell .notranslate}
::: highlight
    # Install from source
    git clone https://github.com/ROCm/xformers.git
    cd xformers/
    git submodule update --init --recursive
    PYTORCH_ROCM_ARCH=gfx942 python setup.py install #Instinct MI300-series
:::
::::
:::::
::::::

::::::::: {#pytorch-built-in-acceleration .section}
## PyTorch built-in acceleration[\#](#pytorch-built-in-acceleration "Link to this heading"){.headerlink}

[PyTorch compilation mode](https://pytorch.org/tutorials/intermediate/torch_compile_tutorial.html){.reference .external} synthesizes the model into a graph and then lowers it to prime operators. These operators are compiled using TorchInductor, which uses OpenAI Triton as a building block for GPU acceleration. One advantage of PyTorch compilation mode is that its GPU kernels are written in Python, making modifying and extending them easier. PyTorch compilation mode often delivers higher performance, as model operations are fused before runtime, which allows for easy deployment of high-performance kernels.

::::: {#pytorch-compilation .section}
### PyTorch compilation[\#](#pytorch-compilation "Link to this heading"){.headerlink}

To utilize the PyTorch compilation mode, specific layers of the model must be explicitly assigned as compilation targets. In the case of LLM, where autoregressive token decoding generates dynamically changing key/value sizes, limiting the key/value size to a static dimension, [`max_cache_length`{.docutils .literal .notranslate}]{.pre}, is necessary to utilize the performance benefits of the PyTorch compilation.

:::: {.highlight-python .notranslate}
::: highlight
    # Sample script to run LLM with the static key-value cache and PyTorch compilation
    from transformers import AutoModelForCausalLM, AutoTokenizer, StaticCache
    import torch
    from typing import Optional
    import os
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    model_name = "NousResearch/Meta-Llama-3-8B"
    prompts = []

    for b in range(1):
        prompts.append("New york city is where "
    )

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16).to(device).eval()
    inputs = tokenizer(prompts, return_tensors="pt").to(model.device)

    def decode_one_tokens(model, cur_token, input_pos, cache_position):
        logits = model(cur_token, position_ids=input_pos, cache_position=cache_position, return_dict=False, use_cache=True)[0]
        new_token = torch.argmax(logits[:, -1], dim=-1)[:, None]
        return new_token

    batch_size, seq_length = inputs["input_ids"].shape

    # Static key-value cache
    max_cache_length = 1024
    max_new_tokens = 10
    model._setup_cache(StaticCache, batch_size, max_cache_len=max_cache_length)
    cache_position = torch.arange(seq_length, device=device)
    generated_ids = torch.zeros(batch_size, seq_length + max_new_tokens + 1, dtype=torch.int, device=device)
    generated_ids[:, cache_position] = inputs["input_ids"].to(device).to(torch.int)

    logits = model(**inputs, cache_position=cache_position, return_dict=False, use_cache=True)[0]
    next_token = torch.argmax(logits[:, -1], dim=-1)[:, None]

    # torch compilation
    decode_one_tokens = torch.compile(decode_one_tokens, mode="max-autotune-no-cudagraphs",fullgraph=True)

    generated_ids[:, seq_length] = next_token[:, 0]
    cache_position = torch.tensor([seq_length + 1], device=device)

    with torch.no_grad():
        for _ in range(1, max_new_tokens):
            with torch.backends.cuda.sdp_kernel(enable_flash=False, enable_mem_efficient=False, enable_math=True):
                next_token = decode_one_tokens(model, next_token.clone(), None, cache_position)
                generated_ids[:, cache_position] = next_token.int()
            cache_position += 1
:::
::::
:::::

::::: {#pytorch-tunableop .section}
[]{#fine-tuning-llms-pytorch-tunableop}

### PyTorch TunableOp[\#](#pytorch-tunableop "Link to this heading"){.headerlink}

ROCm PyTorch (2.2.0 and later) allows users to use high-performance ROCm GEMM kernel libraries through PyTorch's built-in TunableOp options. This enables users to automatically pick up the best-performing GEMM kernels from [[rocBLAS]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/index.html "(in rocBLAS Documentation v5.2.0)"){.reference .external} and [[hipBLASLt]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/hipBLASLt/en/latest/index.html "(in hipBLASLt Documentation v1.2.2)"){.reference .external} libraries during runtime.

During warm-up runs or offline profiling steps, users can create a GEMM Table that enumerates the kernel information. During the model's run, the best-performing kernel substitutes [`torch.nn.functional.linear(input,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`weight,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`bias=None)`{.docutils .literal .notranslate}]{.pre} with the kernel specified in the GEMM table. The [Tunable GitHub](https://github.com/pytorch/pytorch/blob/main/aten/src/ATen/cuda/tunable/README.md){.reference .external} page describes the options.

:::: {.highlight-python .notranslate}
::: highlight
    # To turn on TunableOp, simply set this environment variable
    export PYTORCH_TUNABLEOP_ENABLED=1

    # Python
    import torch
    import torch.nn as nn
    import torch.nn.functional as F
    A = torch.rand(100, 20, device="cuda")
    W = torch.rand(200, 20, device="cuda")
    Out = F.linear(A, W)
    print(Out.size())

    # tunableop_results0.csv
    Validator,PT_VERSION,2.4.0
    Validator,ROCM_VERSION,6.1.0.0-82-5fabb4c
    Validator,HIPBLASLT_VERSION,0.7.0-1549b021
    Validator,GCN_ARCH_NAME,gfx942:sramecc+:xnack-
    Validator,ROCBLAS_VERSION,4.1.0-cefa4a9b-dirty
    GemmTunableOp_float_TN,tn_200_100_20,Gemm_Rocblas_32323,0.00669595
:::
::::

![GEMM and TunableOp](../../../_images/tunableop.png){.align-center}

Learn more about optimizing kernels with TunableOp in [[Optimizing Triton kernels]{.std .std-ref}](workload.html#mi300x-tunableop){.reference .internal}.
:::::
:::::::::

:::::::::::::::::::: {#fbgemm-and-fbgemm-gpu .section}
## FBGEMM and FBGEMM_GPU[\#](#fbgemm-and-fbgemm-gpu "Link to this heading"){.headerlink}

FBGEMM (Facebook General Matrix Multiplication) is a low-precision, high-performance CPU kernel library for matrix-matrix multiplications and convolutions. It is used for server-side inference and as a back end for PyTorch quantized operators. FBGEMM offers optimized on-CPU performance for reduced precision calculations, strong performance on native tensor formats, and the ability to generate high-performance shape- and size-specific kernels at runtime.

FBGEMM_GPU collects several high-performance PyTorch GPU operator libraries for use in training and inference. It provides efficient table-batched embedding functionality, data layout transformation, and quantization support.

For more information about FBGEMM and FBGEMM_GPU, see the [PyTorch FBGEMM GitHub](https://github.com/pytorch/FBGEMM){.reference .external} and the [PyTorch FBGEMM documentation](https://pytorch.org/FBGEMM/){.reference .external}. The [Meta blog post about FBGEMM](https://engineering.fb.com/2018/11/07/ml-applications/fbgemm/){.reference .external} provides additional background about the library.

::::::::::::: {#installing-fbgemm-gpu .section}
### Installing FBGEMM_GPU[\#](#installing-fbgemm-gpu "Link to this heading"){.headerlink}

Installing FBGEMM_GPU consists of the following steps:

- Set up an isolated Miniconda environment

- Install ROCm using Docker or the [[package manager]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/install-methods/package-manager-index.html "(in ROCm installation on Linux v7.2.2)"){.reference .external}

- Install the nightly [PyTorch](https://pytorch.org/){.reference .external} build

- Complete the pre-build and build tasks

::: {.admonition .note}
Note

FBGEMM_GPU doesn't require the installation of FBGEMM. To optionally install FBGEMM, see the [FBGEMM install instructions](https://pytorch.org/FBGEMM/fbgemm/development/BuildInstructions.html){.reference .external}.
:::

::: {#set-up-the-miniconda-environment .section}
#### Set up the Miniconda environment[\#](#set-up-the-miniconda-environment "Link to this heading"){.headerlink}

To install Miniconda, use the following commands.

1.  Install a [Miniconda environment](https://docs.anaconda.com/miniconda/){.reference .external} for reproducible builds. All subsequent commands run inside this environment.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export PLATFORM_NAME="$(uname -s)-$(uname -m)"

        # Set the Miniconda prefix directory
        miniconda_prefix=$HOME/miniconda

        # Download the Miniconda installer
        wget -q "https://repo.anaconda.com/miniconda/Miniconda3-latest-${PLATFORM_NAME}.sh" -O miniconda.sh

        # Run the installer
        bash miniconda.sh -b -p "$miniconda_prefix" -u

        # Load the shortcuts
        . ~/.bashrc

        # Run updates
        conda update -n base -c defaults -y conda
    :::
    ::::

2.  Create a Miniconda environment with Python 3.12:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        env_name=<ENV NAME>
        python_version=3.12

        # Create the environment
        conda create -y --name ${env_name} python="${python_version}"

        # Upgrade PIP and pyOpenSSL package
        conda run -n ${env_name} pip install --upgrade pip
        conda run -n ${env_name} python -m pip install pyOpenSSL>22.1.0
    :::
    ::::

3.  Install additional build tools:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        conda install -n ${env_name} -y \
           click \
           cmake \
           hypothesis \
           jinja2 \
           make \
           ncurses \
           ninja \
           numpy \
           scikit-build \
           wheel
    :::
    ::::
:::

:::::::: {#install-the-rocm-components .section}
#### Install the ROCm components[\#](#install-the-rocm-components "Link to this heading"){.headerlink}

FBGEMM_GPU can run in a ROCm Docker container or in conjunction with the full ROCm installation. The Docker method is recommended because it requires fewer steps and provides a stable environment.

To run FBGEMM_GPU in the Docker container, pull the [Minimal Docker image for ROCm](https://hub.docker.com/r/rocm/rocm-terminal){.reference .external}. This image includes all preinstalled ROCm packages required to integrate FBGEMM. To pull and run the ROCm Docker image, use this command:

:::: {.highlight-shell .notranslate}
::: highlight
    # Run for ROCm 6.2.0
    docker run -it --network=host --shm-size 16G --device=/dev/kfd --device=/dev/dri --group-add video \
    --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --ipc=host rocm/rocm-terminal:6.2 /bin/bash
:::
::::

::: {.admonition .note}
Note

The [Full Docker image for ROCm](https://hub.docker.com/r/rocm/dev-ubuntu-20.04){.reference .external}, which includes all ROCm packages, can also be used. However, it results in a very large container, so the minimal Docker image is recommended.
:::

You can also install ROCm using the package manager. FBGEMM_GPU requires the installation of the full ROCm package. For more information, see [[the ROCm installation guide]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/detailed-install.html "(in ROCm installation on Linux v7.2.2)"){.reference .external}. The ROCm package also requires the [[MIOpen]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/MIOpen/en/latest/index.html "(in MIOpen Documentation v3.5.1)"){.reference .external} component as a dependency. To install MIOpen, use the [`apt`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`install`{.docutils .literal .notranslate}]{.pre} command.

:::: {.highlight-shell .notranslate}
::: highlight
    apt install hipify-clang miopen-hip miopen-hip-dev
:::
::::
::::::::

::: {#install-pytorch .section}
#### Install PyTorch[\#](#install-pytorch "Link to this heading"){.headerlink}

Install [PyTorch](https://pytorch.org/){.reference .external} using [`pip`{.docutils .literal .notranslate}]{.pre} for the most reliable and consistent results.

1.  Install the nightly PyTorch build using [`pip`{.docutils .literal .notranslate}]{.pre}.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # Install the latest nightly, ROCm variant
        conda run -n ${env_name} pip install --pre torch --index-url https://download.pytorch.org/whl/nightly/rocm6.2/
    :::
    ::::

2.  Ensure PyTorch loads correctly. Verify the version and variant of the installation using an [`import`{.docutils .literal .notranslate}]{.pre} test.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # Ensure that the package loads properly
        conda run -n ${env_name} python -c "import torch.distributed"

        # Verify the version and variant of the installation
        conda run -n ${env_name} python -c "import torch; print(torch.__version__)"
    :::
    ::::
:::

::: {#perform-the-prebuild-and-build .section}
#### Perform the prebuild and build[\#](#perform-the-prebuild-and-build "Link to this heading"){.headerlink}

1.  Clone the FBGEMM repository and the relevant submodules. Use [`pip`{.docutils .literal .notranslate}]{.pre} to install the components in [`requirements.txt`{.docutils .literal .notranslate}]{.pre}. Run the following commands inside the Miniconda environment.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # Select a version tag
        FBGEMM_VERSION=v0.8.0

        # Clone the repo along with its submodules
        git clone https://github.com/pytorch/FBGEMM.git --branch=v0.8.0 --recursive fbgemm_${FBGEMM_VERSION}

        # Install additional required packages for building and testing
        cd fbgemm_${FBGEMM_VERSION}/fbgemm_gpu
        pip install requirements.txt
    :::
    ::::

2.  Clear the build cache to remove stale build information.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # !! Run in fbgemm_gpu/ directory inside the Conda environment !!

        python setup.py clean
    :::
    ::::

3.  Set the wheel build variables, including the package name, Python version tag, and Python platform name.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # Set the package name depending on the build variant
        export package_name=fbgemm_gpu_rocm

        # Set the Python version tag.  It should follow the convention `py<major><minor>`,
        # for example, Python 3.12 --> py312
        export python_tag=py312

        # Determine the processor architecture
        export ARCH=$(uname -m)

        # Set the Python platform name for the Linux case
        export python_plat_name="manylinux2014_${ARCH}"
    :::
    ::::

4.  Build FBGEMM_GPU for the ROCm platform. Set [`ROCM_PATH`{.docutils .literal .notranslate}]{.pre} to the path to your ROCm installation. Run these commands from the [`fbgemm_gpu/`{.docutils .literal .notranslate}]{.pre} directory inside the Miniconda environment.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # !! Run in the fbgemm_gpu/ directory inside the Conda environment !!

        export ROCM_PATH=</path/to/rocm>

        # Build for the target architecture of the ROCm device installed on the machine (for example, 'gfx942;gfx90a')
        # See :doc:`The Linux system requirements <../../reference/system-requirements>` for a list of supported GPUs.
        export PYTORCH_ROCM_ARCH=$(${ROCM_PATH}/bin/rocminfo | grep -o -m 1 'gfx.*')

        # Build the wheel artifact only
        python setup.py bdist_wheel \
           --package_variant=rocm \
           --python-tag="${python_tag}" \
           --plat-name="${python_plat_name}" \
           -DHIP_ROOT_DIR="${ROCM_PATH}" \
           -DCMAKE_C_FLAGS="-DTORCH_USE_HIP_DSA" \
           -DCMAKE_CXX_FLAGS="-DTORCH_USE_HIP_DSA"

        # Build and install the library into the Conda environment
        python setup.py install \
           --package_variant=rocm \
           -DHIP_ROOT_DIR="${ROCM_PATH}" \
           -DCMAKE_C_FLAGS="-DTORCH_USE_HIP_DSA" \
           -DCMAKE_CXX_FLAGS="-DTORCH_USE_HIP_DSA"
    :::
    ::::
:::
:::::::::::::

::: {#post-build-validation .section}
### Post-build validation[\#](#post-build-validation "Link to this heading"){.headerlink}

After building FBGEMM_GPU, run some verification checks to ensure the build is correct. Continue to run all commands inside the [`fbgemm_gpu/`{.docutils .literal .notranslate}]{.pre} directory inside the Miniconda environment.

1.  The build process generates many build artifacts and C++ templates, so it is important to confirm no undefined symbols remain.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # !! Run in fbgemm_gpu/ directory inside the Conda environment !!

        # Locate the built .SO file
        fbgemm_gpu_lib_path=$(find . -name fbgemm_gpu_py.so)

        # Check that the undefined symbols don't include fbgemm_gpu-defined functions
        nm -gDCu "${fbgemm_gpu_lib_path}" | sort
    :::
    ::::

2.  Verify the referenced version number of [`GLIBCXX`{.docutils .literal .notranslate}]{.pre} and the presence of certain function symbols:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # !! Run in fbgemm_gpu/ directory inside the Conda environment !!

        # Locate the built .SO file
        fbgemm_gpu_lib_path=$(find . -name fbgemm_gpu_py.so)

        # Note the versions of GLIBCXX referenced by the .SO
        # The libstdc++.so.6 available on the install target must support these versions
        objdump -TC "${fbgemm_gpu_lib_path}" | grep GLIBCXX | sed 's/.*GLIBCXX_\([.0-9]*\).*/GLIBCXX_\1/g' | sort -Vu | cat

        # Test for the existence of a given function symbol in the .SO
        nm -gDC "${fbgemm_gpu_lib_path}" | grep " fbgemm_gpu::merge_pooled_embeddings("
        nm -gDC "${fbgemm_gpu_lib_path}" | grep " fbgemm_gpu::jagged_2d_to_dense("
    :::
    ::::
:::

::::::: {#testing-fbgemm .section}
### Testing FBGEMM[\#](#testing-fbgemm "Link to this heading"){.headerlink}

FBGEMM includes tests and benchmarks to validate performance. To run these tests, you must use ROCm 5.7 or a more recent version on the host and container. To run FBGEMM tests, follow these instructions:

:::: {.highlight-shell .notranslate}
::: highlight
    # !! Run inside the Conda environment !!

    # From the /fbgemm_gpu/ directory
    cd test

    export FBGEMM_TEST_WITH_ROCM=1
    # Enable for debugging failed kernel executions
    export HIP_LAUNCH_BLOCKING=1

    # Run the test
    python -m pytest -v -rsx -s -W ignore::pytest.PytestCollectionWarning split_table_batched_embeddings_test.py
:::
::::

To run the FBGEMM_GPU [`uvm`{.docutils .literal .notranslate}]{.pre} test, use these commands. These tests only support the AMD MI210 and more recent GPUs.

:::: {.highlight-shell .notranslate}
::: highlight
    # Run this inside the Conda environment from the /fbgemm_gpu/ directory
    export HSA_XNACK=1
    cd test

    python -m pytest -v -rsx -s -W ignore::pytest.PytestCollectionWarning ./uvm/uvm_test.py
:::
::::
:::::::
::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::: prev-next-area
[](model-quantization.html "previous page"){.left-prev}

::: prev-next-info
previous

Model quantization techniques
:::

[](optimizing-with-composable-kernel.html "next page"){.right-next}

::: prev-next-info
next

Optimizing with Composable Kernel
:::
:::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::: {.bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {.page-toc .tocsection .onthispage}
Contents
:::

- [Flash Attention 2](#flash-attention-2){.reference .internal .nav-link}
  - [Installation prerequisites](#installation-prerequisites){.reference .internal .nav-link}
  - [Installing Flash Attention 2](#installing-flash-attention-2){.reference .internal .nav-link}
  - [Benchmarking Flash Attention 2](#benchmarking-flash-attention-2){.reference .internal .nav-link}
  - [Using Flash Attention 2](#using-flash-attention-2){.reference .internal .nav-link}
- [xFormers](#xformers){.reference .internal .nav-link}
  - [Installing CK xFormers](#installing-ck-xformers){.reference .internal .nav-link}
- [PyTorch built-in acceleration](#pytorch-built-in-acceleration){.reference .internal .nav-link}
  - [PyTorch compilation](#pytorch-compilation){.reference .internal .nav-link}
  - [PyTorch TunableOp](#pytorch-tunableop){.reference .internal .nav-link}
- [FBGEMM and FBGEMM_GPU](#fbgemm-and-fbgemm-gpu){.reference .internal .nav-link}
  - [Installing FBGEMM_GPU](#installing-fbgemm-gpu){.reference .internal .nav-link}
    - [Set up the Miniconda environment](#set-up-the-miniconda-environment){.reference .internal .nav-link}
    - [Install the ROCm components](#install-the-rocm-components){.reference .internal .nav-link}
    - [Install PyTorch](#install-pytorch){.reference .internal .nav-link}
    - [Perform the prebuild and build](#perform-the-prebuild-and-build){.reference .internal .nav-link}
  - [Post-build validation](#post-build-validation){.reference .internal .nav-link}
  - [Testing FBGEMM](#testing-fbgemm){.reference .internal .nav-link}
::::
:::::
::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
