---
title: "vLLM inference"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference/benchmark-docker/vllm.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-01
---

:::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

:::::::::::::::::::::::::::::::::::::::: bd-content
::::::::::::::::::::::::::::::::::: bd-article-container
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
- vLLM inference
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
# vLLM inference

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [What's new](#what-s-new){.reference .internal .nav-link}
- [Get started](#get-started){.reference .internal .nav-link}
- [Further reading](#further-reading){.reference .internal .nav-link}
- [Previous versions](#previous-versions){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

:::::::::::::::::: {#vllm-inference .section}
# vLLM inference[\#](#vllm-inference "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-02-25
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 4 min read time
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

The [ROCm-enabled vLLM Docker image](https://hub.docker.com/r/vllm/vllm-openai-rocm/tags){.reference .external} offers a prebuilt, optimized environment for large language model (LLM) inference on AMD Instinct MI355X, MI350X, MI325X and MI300X GPUs. This ROCm vLLM Docker image integrates vLLM and PyTorch tailored specifically for AMD Instinct data center GPUs.

This container integrates ROCm, PyTorch, and vLLM with optimizations tailored for AMD Instinct data center GPUs, enabling consistent and reproducible inference deployments.

::: {#what-s-new .section}
## What's new[\#](#what-s-new "Link to this heading"){.headerlink}

- For vLLM release notes on model support, hardware and performance improvements, and other highlights, see the [vLLM Releases page](https://github.com/vllm-project/vllm/releases){.reference .external} on GitHub.

- It's now recommended to use the upstream vLLM documentation at [docs.vllm.ai](https://docs.vllm.ai){.reference .external} for the latest inference and deployment guides.
:::

::::: {#get-started .section}
## Get started[\#](#get-started "Link to this heading"){.headerlink}

For a consistent and portable inference environment, it's recommended to use Docker. vLLM offers a Docker image [vllm/vllm-openai-rocm](https://hub.docker.com/r/vllm/vllm-openai-rocm/tags){.reference .external} for deployment on AMD GPUs. Use the following command to pull the latest Docker image from Docker Hub.

:::: {.highlight-shell .notranslate}
::: highlight
    docker pull vllm/vllm-openai-rocm:latest
:::
::::

After pulling the Docker image, follow the vLLM usage documentation: [Using vLLM](https://docs.vllm.ai/en/latest/usage/){.reference .external}.
:::::

::: {#further-reading .section}
## Further reading[\#](#further-reading "Link to this heading"){.headerlink}

- See [[vLLM inference]{.std .std-ref}](../llm-inference-frameworks.html#fine-tuning-llms-vllm){.reference .internal} and [[vLLM V1 performance optimization]{.std .std-ref}](../../inference-optimization/vllm-optimization.html#mi300x-vllm-optimization){.reference .internal} for a brief introduction to vLLM and optimization strategies.

- For a list of other ready-made Docker images for AI with ROCm, see [AMD Infinity Hub](https://www.amd.com/en/developer/resources/infinity-hub.html#f-amd_hub_category=AI%20%26%20ML%20Models){.reference .external}.
:::

::: {#previous-versions .section}
[]{#vllm-inference-previous-versions}

## Previous versions[\#](#previous-versions "Link to this heading"){.headerlink}

It's now recommended to use the upstream vLLM documentation at [docs.vllm.ai](https://docs.vllm.ai){.reference .external} for the latest deployment guides.

You can find legacy versions of this documentation at [[vLLM inference performance testing version history]{.doc}](previous-versions/vllm-history.html){.reference .internal} which provide instructions for inference performance testing for select models. See the [Use AMD's Docker images](https://docs.vllm.ai/en/stable/deployment/docker/#use-amds-docker-images){.reference .external} note in the vLLM documentation for more information.
:::
::::::::::::::::::

::::: prev-next-area
[](../llm-inference-frameworks.html "previous page"){.left-prev}

::: prev-next-info
previous

LLM inference frameworks
:::

[](pytorch-inference.html "next page"){.right-next}

::: prev-next-info
next

PyTorch inference performance testing
:::
:::::
:::::::::::::::::::::::::::::::::::

:::::: {.bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {.page-toc .tocsection .onthispage}
Contents
:::

- [What's new](#what-s-new){.reference .internal .nav-link}
- [Get started](#get-started){.reference .internal .nav-link}
- [Further reading](#further-reading){.reference .internal .nav-link}
- [Previous versions](#previous-versions){.reference .internal .nav-link}
::::
:::::
::::::
::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::
