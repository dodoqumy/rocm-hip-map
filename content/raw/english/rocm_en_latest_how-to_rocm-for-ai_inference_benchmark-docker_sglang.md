---
title: "SGLang inference performance testing DeepSeek-R1-Distill-Qwen-32B"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference/benchmark-docker/sglang.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-01
---

:::::::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

:::::::::::::::::::::::::::::::::::::::::::::::::: bd-content
::::::::::::::::::::::::::::::::::::::::::::: bd-article-container
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
# SGLang inference performance testing DeepSeek-R1-Distill-Qwen-32B

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [System validation](#system-validation){.reference .internal .nav-link}
  - [Pull the Docker image](#pull-the-docker-image){.reference .internal .nav-link}
  - [Benchmarking](#benchmarking){.reference .internal .nav-link}
- [Further reading](#further-reading){.reference .internal .nav-link}
- [Previous versions](#previous-versions){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

:::::::::::::::::::::::::::: {#sglang-inference-performance-testing-deepseek-r1-distill-qwen-32b .section}
# SGLang inference performance testing DeepSeek-R1-Distill-Qwen-32B[\#](#sglang-inference-performance-testing-deepseek-r1-distill-qwen-32b "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 7 min read time
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

[SGLang](https://docs.sglang.ai){.reference .external} is a high-performance inference and serving engine for large language models (LLMs) and vision models. The ROCm-enabled [SGLang Docker image](https://hub.docker.com/layers/lmsysorg/sglang/v0.4.5-rocm630/images/sha256-63d2cb760a237125daf6612464cfe2f395c0784e21e8b0ea37d551cd10d3c951){.reference .external} bundles SGLang with PyTorch, optimized for AMD Instinct MI300X Series GPUs. It includes the following software components:

::: pst-scrollable-table-container
  Software component   Version
  -------------------- --------------------
  ROCm                 6.3.0
  SGLang               0.4.5 (0.4.5-rocm)
  PyTorch              2.6.0a0+git8d4926e
:::

::::::::::::::: {#system-validation .section}
## System validation[\#](#system-validation "Link to this heading"){.headerlink}

Before running AI workloads, it's important to validate that your AMD hardware is configured correctly and performing optimally.

If you have already validated your system settings, including aspects like NUMA auto-balancing, you can skip this step. Otherwise, complete the procedures in the [[System validation and optimization]{.std .std-ref}](../../system-setup/prerequisite-system-validation.html#rocm-for-ai-system-optimization){.reference .internal} guide to properly configure your system settings before starting training.

To test for optimal performance, consult the recommended [[System health benchmarks]{.std .std-ref}](../../system-setup/system-health-check.html#rocm-for-ai-system-health-bench){.reference .internal}. This suite of tests will help you verify and fine-tune your system's configuration.

::::: {#pull-the-docker-image .section}
### Pull the Docker image[\#](#pull-the-docker-image "Link to this heading"){.headerlink}

Download the [SGLang Docker image](https://hub.docker.com/layers/lmsysorg/sglang/v0.4.5-rocm630/images/sha256-63d2cb760a237125daf6612464cfe2f395c0784e21e8b0ea37d551cd10d3c951){.reference .external}. Use the following command to pull the Docker image from Docker Hub.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull lmsysorg/sglang:v0.4.5-rocm630
:::
::::
:::::

::::::::::: {#benchmarking .section}
### Benchmarking[\#](#benchmarking "Link to this heading"){.headerlink}

Once the setup is complete, choose one of the following methods to benchmark inference performance with [DeepSeek-R1-Distill-Qwen-32B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B){.reference .external}.

:::::::::: {#sglang-benchmark-mad .model-doc .pyt-sglang-deepseek-r1-distill-qwen-32b .docutils .container}
::::::::: {.sd-tab-set .docutils}
MAD-integrated benchmarking

::: {.sd-tab-content .docutils}
1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    :::
    ::::

2.  Use this command to run the performance benchmark test on the [DeepSeek-R1-Distill-Qwen-32B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B){.reference .external} model using one GPU with the [`bfloat16`{.docutils .literal .notranslate}]{.pre} data type on the host machine.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_sglang_deepseek-r1-distill-qwen-32b \
            --keep-model-dir \
            --live-output \
            --timeout 28800
    :::
    ::::

MAD launches a Docker container with the name [`container_ci-pyt_sglang_deepseek-r1-distill-qwen-32b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in the following path: [`~/MAD/perf_DeepSeek-R1-Distill-Qwen-32B.csv`{.docutils .literal .notranslate}]{.pre}.

Although the DeepSeek-R1-Distill-Qwen-32B is preconfigured to collect latency and throughput performance data, you can also change the benchmarking parameters. See the standalone benchmarking tab for more information.
:::

Standalone benchmarking

::::::: {.sd-tab-content .docutils}
Download the Docker image and required scripts

1.  Run the SGLang benchmark script independently by starting the [Docker container](https://hub.docker.com/layers/lmsysorg/sglang/v0.4.5-rocm630/images/sha256-63d2cb760a237125daf6612464cfe2f395c0784e21e8b0ea37d551cd10d3c951){.reference .external} as shown in the following snippet.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        docker pull lmsysorg/sglang:v0.4.5-rocm630
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
            lmsysorg/sglang:v0.4.5-rocm630
    :::
    ::::

2.  In the Docker container, clone the ROCm MAD repository and navigate to the benchmark scripts directory at [`~/MAD/scripts/sglang`{.docutils .literal .notranslate}]{.pre}.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/MAD
        cd MAD/scripts/sglang
    :::
    ::::

3.  To start the benchmark, use the following command with the appropriate options.

    [Benchmark options]{.sd-summary-text}[![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jaGV2cm9uLXJpZ2h0IiBoZWlnaHQ9IjEuNWVtIiB2ZXJzaW9uPSIxLjEiIHZpZXdib3g9IjAgMCAyNCAyNCIgd2lkdGg9IjEuNWVtIj48cGF0aCBkPSJNOC43MiAxOC43OGEuNzUuNzUgMCAwIDEgMC0xLjA2TDE0LjQ0IDEyIDguNzIgNi4yOGEuNzUxLjc1MSAwIDAgMSAuMDE4LTEuMDQyLjc1MS43NTEgMCAwIDEgMS4wNDItLjAxOGw2LjI1IDYuMjVhLjc1Ljc1IDAgMCAxIDAgMS4wNmwtNi4yNSA2LjI1YS43NS43NSAwIDAgMS0xLjA2IDBaIiAvPjwvc3ZnPg==){.sd-octicon .sd-octicon-chevron-right}]{.sd-summary-state-marker .sd-summary-chevron-right}

    :::: {.sd-summary-content .sd-card-body .docutils}
    ::: pst-scrollable-table-container
      Name                                                      Options                                               Description
      --------------------------------------------------------- ----------------------------------------------------- -------------------------------------
      [`$test_option`{.docutils .literal .notranslate}]{.pre}   latency                                               Measure decoding token latency
                                                                throughput                                            Measure token generation throughput
                                                                all                                                   Measure both throughput and latency
      [`$num_gpu`{.docutils .literal .notranslate}]{.pre}       8                                                     Number of GPUs
      [`$datatype`{.docutils .literal .notranslate}]{.pre}      [`bfloat16`{.docutils .literal .notranslate}]{.pre}   Data type
      [`$dataset`{.docutils .literal .notranslate}]{.pre}       random                                                Dataset
    :::

    The input sequence length, output sequence length, and tensor parallel (TP) are already configured. You don't need to specify them with this script.
    ::::

    Command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        ./sglang_benchmark_report.sh -s $test_option -m deepseek-ai/DeepSeek-R1-Distill-Qwen-32B -g $num_gpu -d $datatype [-a $dataset]
    :::
    ::::

::::: {.admonition .note}
Note

If you encounter the following error, pass your access-authorized Hugging Face token to the gated models.

:::: {.highlight-shell-session .notranslate}
::: highlight
    OSError: You are trying to access a gated repo.
    # pass your HF_TOKEN
    export HF_TOKEN=$your_personal_hf_token
:::
::::
:::::

Benchmarking examples

Here are some examples of running the benchmark with various options:

- Latency benchmark

  Use this command to benchmark the latency of the DeepSeek-R1-Distill-Qwen-32B model on eight GPUs with [`bfloat16`{.docutils .literal .notranslate}]{.pre} precision.

  :::: {.highlight-shell .notranslate}
  ::: highlight
      ./sglang_benchmark_report.sh \
          -s latency \
          -m deepseek-ai/DeepSeek-R1-Distill-Qwen-32B \
          -g 8 \
          -d bfloat16
  :::
  ::::

  Find the latency report at [`./reports_bfloat16/summary/DeepSeek-R1-Distill-Qwen-32B_latency_report.csv`{.docutils .literal .notranslate}]{.pre}.

- Throughput benchmark

  Use this command to benchmark the throughput of the DeepSeek-R1-Distill-Qwen-32B model on eight GPUs with [`bfloat16`{.docutils .literal .notranslate}]{.pre} precision.

  :::: {.highlight-shell .notranslate}
  ::: highlight
      ./sglang_benchmark_report.sh \
          -s throughput \
          -m deepseek-ai/DeepSeek-R1-Distill-Qwen-32B \
          -g 8 \
          -d bfloat16 \
          -a random
  :::
  ::::

  Find the throughput report at [`./reports_bfloat16/summary/DeepSeek-R1-Distill-Qwen-32B_throughput_report.csv`{.docutils .literal .notranslate}]{.pre}.

`<style>
mjx-container[jax="CHTML"][display="true"] {
   text-align: left;
   margin: 0;
}
</style>`{=html}

::: {.admonition .note}
Note

Throughput is calculated as:

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_tot = requests \\times (\\mathsf{\\text{input lengths}} + \\mathsf{\\text{output lengths}}) / elapsed\\\_time\\\]
  :::

- ::: {.math .notranslate .nohighlight}
  \\\[throughput\\\_gen = requests \\times \\mathsf{\\text{output lengths}} / elapsed\\\_time\\\]
  :::
:::
:::::::
:::::::::
::::::::::
:::::::::::
:::::::::::::::

::: {#further-reading .section}
## Further reading[\#](#further-reading "Link to this heading"){.headerlink}

- To learn more about the options for latency and throughput benchmark scripts, see [sgl-project/sglang](https://github.com/sgl-project/sglang/tree/main/benchmark/blog_v0_2){.github .reference .external}.

- To learn more about MAD and the [`madengine`{.docutils .literal .notranslate}]{.pre} CLI, see the [MAD usage guide](https://github.com/ROCm/MAD?tab=readme-ov-file#usage-guide){.reference .external}.

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
::::::::::::::::::::::::::::

::::: prev-next-area
[](pytorch-inference.html "previous page"){.left-prev}

::: prev-next-info
previous

PyTorch inference performance testing
:::

[](vllm-mori-distributed.html "next page"){.right-next}

::: prev-next-info
next

vLLM distributed inference with MoRI
:::
:::::
:::::::::::::::::::::::::::::::::::::::::::::

:::::: {.bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {.page-toc .tocsection .onthispage}
Contents
:::

- [System validation](#system-validation){.reference .internal .nav-link}
  - [Pull the Docker image](#pull-the-docker-image){.reference .internal .nav-link}
  - [Benchmarking](#benchmarking){.reference .internal .nav-link}
- [Further reading](#further-reading){.reference .internal .nav-link}
- [Previous versions](#previous-versions){.reference .internal .nav-link}
::::
:::::
::::::
::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::
