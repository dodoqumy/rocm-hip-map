---
title: "SGLang distributed inference with Mooncake"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference/benchmark-docker/sglang-distributed.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-01
---

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-content
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-article-container
:::::::::: {.bd-header-article .d-print-none}
::::::::: {.header-article-items .header-article__inner}
::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}
:::

::: header-article-item
- [](../../../../index.html){.nav-link aria-label="Home"}
- [Use ROCm for AI](../../index.html){.nav-link}
- [Use ROCm for AI inference](../index.html){.nav-link}
- SGLang\...
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
# SGLang distributed inference with Mooncake

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [Prerequisites](#prerequisites){.reference .internal .nav-link}
- [Supported models](#supported-models){.reference .internal .nav-link}
  - [Build the Docker image](#build-the-docker-image){.reference .internal .nav-link}
- [Benchmarking](#benchmarking){.reference .internal .nav-link}
  - [Launch the service](#launch-the-service){.reference .internal .nav-link}
  - [Post-run logs and testing](#post-run-logs-and-testing){.reference .internal .nav-link}
- [Known issues](#known-issues){.reference .internal .nav-link}
- [Further reading](#further-reading){.reference .internal .nav-link}
- [Previous versions](#previous-versions){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#sglang-distributed-inference-with-mooncake .section}
# SGLang distributed inference with Mooncake[\#](#sglang-distributed-inference-with-mooncake "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 10 min read time
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

As LLM inference increasingly demands handling massive models and dynamic workloads, efficient distributed inference becomes essential. Traditional co-located architectures face bottlenecks due to tightly coupled memory and compute resources, which limits scalability and flexibility. Disaggregated inference refers to the process of splitting the inference of LLMs into distinct phases. This architecture, facilitated by libraries like Mooncake, uses high-bandwidth RDMA to transfer the Key-Value (KV) cache between prefill and decode nodes. This allows for independent resource scaling and optimization, resulting in improved efficiency and throughput.

[SGLang](https://docs.sglang.ai){.reference .external} is a high-performance inference and serving engine for large language models (LLMs) and vision models. The ROCm-enabled [SGLang base Docker image](https://hub.docker.com/layers/lmsysorg/sglang/v0.5.2rc1-rocm700-mi30x/images/sha256-10c4ee502ddba44dd8c13325e6e03868bfe7f43d23d0a44780a8ee8b393f4729){.reference .external} bundles SGLang with PyTorch, which is optimized for AMD Instinct MI300X Series GPUs. It includes the following software components:

::: pst-scrollable-table-container
  Software component    Version
  --------------------- -----------------------------
  ROCm                  7.0.0
  SGLang                v0.5.2rc1
  pytorch-triton-rocm   3.4.0+rocm7.0.0.gitf9e5bf54
:::

The following guides on setting up and running SGLang and Mooncake for disaggregated distributed inference on a Slurm cluster using AMD Instinct MI300X Series GPUs backed by Mellanox CX-7 NICs.

::: {#prerequisites .section}
## Prerequisites[\#](#prerequisites "Link to this heading"){.headerlink}

Before starting, ensure you have:

- A Slurm cluster with at least three nodes: one for the proxy, one for prefill ([`xP`{.docutils .literal .notranslate}]{.pre}), and one for decode ([`yD`{.docutils .literal .notranslate}]{.pre}).

  [`Nodes`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`->`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`xP`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`+`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`yD`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`+`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`1`{.docutils .literal .notranslate}]{.pre}

- A Dockerized environment with SGLang, Mooncake, etcd, and NIC drivers built in. See [[Build the Docker image]{.std .std-ref}](#sglang-disagg-inf-build-docker-image){.reference .internal} for instructions.

- A shared filesystem for storing models, scripts, and logs (cluster-specific).
:::

::::::::::::::::::::::::::::::::: {#supported-models .section}
## Supported models[\#](#supported-models "Link to this heading"){.headerlink}

The following models are supported for SGLang disaggregated prefill/decode inference. Some instructions, commands, and recommendations in this documentation might vary by selected model.

::::::::::::::::: {#vllm-benchmark-ud-params-picker .container-fluid}
::::::: {.row .gx-0}
::: {.col-2 .me-1 .px-2 .model-param-head}
Model type
:::

::::: {.row .col-10 .pe-0}
::: {.col-6 .px-2 .model-param param-k="model-group" param-v="dense-models" tabindex="0"}
Dense models
:::

::: {.col-6 .px-2 .model-param param-k="model-group" param-v="small-experts-models" tabindex="0"}
Small experts models
:::
:::::
:::::::

::::::::::: {.row .gx-0 .pt-1}
::: {.col-2 .me-1 .px-2 .model-param-head}
Model
:::

::::::::: {.row .col-10 .pe-0}
::: {.col-6 .px-2 .model-param param-group="dense-models" param-k="model" param-v="llama-3.1-8b-instruct" tabindex="0"}
Llama 3.1 8B Instruct
:::

::: {.col-6 .px-2 .model-param param-group="dense-models" param-k="model" param-v="llama-3.1-405b-instruct-fp8-kv" tabindex="0"}
Llama 3.1 405B FP8 KV
:::

::: {.col-6 .px-2 .model-param param-group="dense-models" param-k="model" param-v="amd-llama-3.3-70b-instruct-fp8-kv" tabindex="0"}
Llama 3.3 70B FP8 KV
:::

::: {.col-6 .px-2 .model-param param-group="dense-models" param-k="model" param-v="qwen3-32b" tabindex="0"}
Qwen3 32B
:::

::: {.col-6 .px-2 .model-param param-group="small-experts-models" param-k="model" param-v="deepseek-v3" tabindex="0"}
DeepSeek V3
:::

::: {.col-6 .px-2 .model-param param-group="small-experts-models" param-k="model" param-v="mixtral-8x7b-v0.1" tabindex="0"}
Mixtral 8x7B v0.1
:::
:::::::::
:::::::::::
:::::::::::::::::

:::: {.model-doc .llama-3-1-8b-instruct .docutils .container}
::: {.admonition .note}
Note

See the [Llama 3.1 8B Instruct model card on Hugging Face](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct){.reference .external} to learn more about this model. Some models require access authorization prior to use through an external license agreement with a third party.
:::
::::

:::: {.model-doc .llama-3-1-405b-instruct-fp8-kv .docutils .container}
::: {.admonition .note}
Note

See the [Llama 3.1 405B FP8 KV model card on Hugging Face](https://huggingface.co/amd/Llama-3.1-405B-Instruct-FP8-KV){.reference .external} to learn more about this model. Some models require access authorization prior to use through an external license agreement with a third party.
:::
::::

:::: {.model-doc .amd-llama-3-3-70b-instruct-fp8-kv .docutils .container}
::: {.admonition .note}
Note

See the [Llama 3.3 70B FP8 KV model card on Hugging Face](https://huggingface.co/amd/Llama-3.3-70B-Instruct-FP8-KV){.reference .external} to learn more about this model. Some models require access authorization prior to use through an external license agreement with a third party.
:::
::::

:::: {.model-doc .qwen3-32b .docutils .container}
::: {.admonition .note}
Note

See the [Qwen3 32B model card on Hugging Face](https://huggingface.co/Qwen/Qwen3-32B){.reference .external} to learn more about this model. Some models require access authorization prior to use through an external license agreement with a third party.
:::
::::

:::: {.model-doc .deepseek-v3 .docutils .container}
::: {.admonition .note}
Note

See the [DeepSeek V3 model card on Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-V3){.reference .external} to learn more about this model. Some models require access authorization prior to use through an external license agreement with a third party.
:::
::::

:::: {.model-doc .mixtral-8x7b-v0-1 .docutils .container}
::: {.admonition .note}
Note

See the [Mixtral 8x7B v0.1 model card on Hugging Face](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1){.reference .external} to learn more about this model. Some models require access authorization prior to use through an external license agreement with a third party.
:::
::::

::::: {#build-the-docker-image .section}
[]{#sglang-disagg-inf-build-docker-image}

### Build the Docker image[\#](#build-the-docker-image "Link to this heading"){.headerlink}

Get the Dockerfile located in [ROCm/MAD](https://github.com/ROCm/MAD/blob/develop/docker/sglang_disagg_inference.ubuntu.amd.Dockerfile){.github .reference .external}. It uses [lmsysorg/sglang:v0.5.2rc1-rocm700-mi30x](https://hub.docker.com/layers/lmsysorg/sglang/v0.4.9.post1-rocm630/images/sha256-2f6b1748e4bcc70717875a7da76c87795fd8aa46a9646e08d38aa7232fc78538){.reference .external} as the base Docker image and installs the necessary components for Mooncake, etcd, and Mellanox network drivers.

:::: {.highlight-shell .notranslate}
::: highlight
    git clone https://github.com/ROCm/MAD.git
    cd MAD/docker
    docker build \
        -t sglang_disagg_pd_image \
        -f sglang_disagg_inference.ubuntu.amd.Dockerfile .
:::
::::
:::::
:::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::: {#benchmarking .section}
## Benchmarking[\#](#benchmarking "Link to this heading"){.headerlink}

The [ROCm/MAD](https://github.com/ROCm/MAD/tree/develop/scripts/sglang_disagg){.github .reference .external} repository contains scripts to launch SGLang inference with prefill/decode disaggregation via Mooncake for supported models.

- [scripts/sglang_dissag/run_xPyD_models.slurm](https://github.com/ROCm/MAD/blob/develop/scripts/sglang_disagg/run_xPyD_models.slurm){.reference .external} -- the main Slurm batch script to launch Docker containers on all nodes using [`sbatch`{.docutils .literal .notranslate}]{.pre} or [`salloc`{.docutils .literal .notranslate}]{.pre}.

- [scripts/sglang_dissag/sglang_disagg_server.sh](https://github.com/ROCm/MAD/blob/develop/scripts/sglang_disagg/sglang_disagg_server.sh){.reference .external} -- the entrypoint script that runs inside each container to start the correct service -- proxy, prefill, or decode.

- [scripts/sglang_dissag/benchmark_xPyD.sh](https://github.com/ROCm/MAD/blob/develop/scripts/sglang_disagg/benchmark_xPyD.sh){.reference .external} -- the benchmark script to run the GSM8K accuracy benchmark and the SGLang benchmarking tool for performance measurement.

- [scripts/sglang_dissag/benchmark_parser.py](https://github.com/ROCm/MAD/blob/develop/scripts/sglang_disagg/benchmark_parser.py){.reference .external} -- the log parser script to be run on the concurrency benchmark log file to generate tabulated data.

::::::::::::::::::::: {#launch-the-service .section}
### Launch the service[\#](#launch-the-service "Link to this heading"){.headerlink}

The service is deployed using a Slurm batch script that orchestrates the containers across the allocated nodes.

::::: {.model-doc .llama-3-1-8b-instruct .docutils .container}
:::: {.highlight-shell .notranslate}
::: highlight
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
:::
::::
:::::

::::: {.model-doc .llama-3-1-405b-instruct-fp8-kv .docutils .container}
:::: {.highlight-shell .notranslate}
::: highlight
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
:::
::::
:::::

::::: {.model-doc .amd-llama-3-3-70b-instruct-fp8-kv .docutils .container}
:::: {.highlight-shell .notranslate}
::: highlight
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
:::
::::
:::::

::::: {.model-doc .qwen3-32b .docutils .container}
:::: {.highlight-shell .notranslate}
::: highlight
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
:::
::::
:::::

::::: {.model-doc .deepseek-v3 .docutils .container}
:::: {.highlight-shell .notranslate}
::: highlight
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
:::
::::
:::::

::::: {.model-doc .mixtral-8x7b-v0-1 .docutils .container}
:::: {.highlight-shell .notranslate}
::: highlight
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
:::
::::
:::::
:::::::::::::::::::::

::::::: {#post-run-logs-and-testing .section}
### Post-run logs and testing[\#](#post-run-logs-and-testing "Link to this heading"){.headerlink}

Logs are stored in your shared filesystem in the directory specified by the [`LOG_PATH`{.docutils .literal .notranslate}]{.pre} variable in the Slurm script. A new directory named after the Slurm job ID is created for each run.

Inside that directory, you can access various logs:

- [`pd_sglang_bench_serving.sh_NODE<...>.log`{.docutils .literal .notranslate}]{.pre} -- the main log for each server node.

- [`etcd_NODE<...>.log`{.docutils .literal .notranslate}]{.pre} -- logs for etcd services.

- [`prefill_NODE<...>.log`{.docutils .literal .notranslate}]{.pre} -- logs for the prefill services.

- [`decode_NODE<...>.log`{.docutils .literal .notranslate}]{.pre} -- logs for the decode services.

Use the benchmark parser script for concurrency logs to tabulate different data.

:::: {.highlight-shell .notranslate}
::: highlight
    python3 benchmark_parser.py <log_path/benchmark_XXX_CONCURRENCY.log>
:::
::::

To verify the service is responsive, you can try sending a [`curl`{.docutils .literal .notranslate}]{.pre} request to test the launched server from the Docker container on the proxy node. For example:

:::: {.highlight-shell .notranslate}
::: highlight
    curl -X POST http://127.0.0.1:30000/generate \
        -H "Content-Type: application/json" \
        -d '{ "text": "Let me tell you a story ", "sampling_params": { "temperature": 0.3 } }'
:::
::::
:::::::
:::::::::::::::::::::::::::

::::: {#known-issues .section}
## Known issues[\#](#known-issues "Link to this heading"){.headerlink}

When running larger models, such as DeepSeek-V3 and Llama-3.1-405B-Instruct-FP8-KV, at higher concurrency levels (512+), the following error might occur:

:::: {.highlight-shell-session .notranslate}
::: highlight
    <TransferEncodingError: 400, message:
     Not enough data to satisfy transfer length header.

    The above exception was the direct cause of the following exception:

    Traceback (most recent call last):
    ...
:::
::::

This leads to dropping requests and lower throughput.
:::::

::: {#further-reading .section}
## Further reading[\#](#further-reading "Link to this heading"){.headerlink}

- To learn about Mooncake, see [Welcome to Mooncake](https://kvcache-ai.github.io/Mooncake/){.reference .external}.

- To learn more about the options for latency and throughput benchmark scripts, see [sgl-project/sglang](https://github.com/sgl-project/sglang/tree/main/benchmark/blog_v0_2){.github .reference .external}.

- See the base upstream Docker image on [Docker Hub](https://hub.docker.com/layers/lmsysorg/sglang/v0.5.2rc1-rocm700-mi30x/images/sha256-10c4ee502ddba44dd8c13325e6e03868bfe7f43d23d0a44780a8ee8b393f4729){.reference .external}.

- To learn more about system settings and management practices to configure your system for MI300X Series GPUs, see [AMD Instinct MI300X system optimization](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi300x.html){.reference .external}.

- For application performance optimization strategies for HPC and AI workloads, including inference with vLLM, see [[AMD Instinct MI300X workload optimization]{.doc}](../../inference-optimization/workload.html){.reference .internal}.

- To learn how to run community models from Hugging Face on AMD GPUs, see [[Running models from Hugging Face]{.doc}](../hugging-face-models.html){.reference .internal}.

- To learn how to fine-tune LLMs and optimize inference, see [[Fine-tuning LLMs and inference optimization]{.doc}](../../fine-tuning/fine-tuning-and-inference.html){.reference .internal}.

- For a list of other ready-made Docker images for AI with ROCm, see [AMD Infinity Hub](https://www.amd.com/en/developer/resources/infinity-hub.html#f-amd_hub_category=AI%20%26%20ML%20Models){.reference .external}.
:::

::: {#previous-versions .section}
## Previous versions[\#](#previous-versions "Link to this heading"){.headerlink}

See [[SGLang inference performance testing version history]{.doc}](previous-versions/sglang-history.html){.reference .internal} to find documentation for previous releases of SGLang inference performance testing.
:::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::: prev-next-area
[](sglang-mori-distributed.html "previous page"){.left-prev}

::: prev-next-info
previous

SGLang distributed inference with MoRI
:::

[](../xdit-diffusion-inference.html "next page"){.right-next}

::: prev-next-info
next

xDiT diffusion inference
:::
:::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::: {.bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {.page-toc .tocsection .onthispage}
Contents
:::

- [Prerequisites](#prerequisites){.reference .internal .nav-link}
- [Supported models](#supported-models){.reference .internal .nav-link}
  - [Build the Docker image](#build-the-docker-image){.reference .internal .nav-link}
- [Benchmarking](#benchmarking){.reference .internal .nav-link}
  - [Launch the service](#launch-the-service){.reference .internal .nav-link}
  - [Post-run logs and testing](#post-run-logs-and-testing){.reference .internal .nav-link}
- [Known issues](#known-issues){.reference .internal .nav-link}
- [Further reading](#further-reading){.reference .internal .nav-link}
- [Previous versions](#previous-versions){.reference .internal .nav-link}
::::
:::::
::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
