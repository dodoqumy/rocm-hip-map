---
title: "System health benchmarks for AI workloads"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/system-setup/system-health-check.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-01
---

:::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

:::::::::::::::::::::::::::::::::::::::::: bd-content
::::::::::::::::::::::::::::::::::::: bd-article-container
:::::::::: {.bd-header-article .d-print-none}
::::::::: {.header-article-items .header-article__inner}
::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}
:::

::: header-article-item
- [](../../../index.html){.nav-link aria-label="Home"}
- [Use ROCm for AI](../index.html){.nav-link}
- [System setup for AI workloads on ROCm](index.html){.nav-link}
- System\...
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
# System health benchmarks for AI workloads

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [ROCm Validation Suite (RVS) tests](#rocm-validation-suite-rvs-tests){.reference .internal .nav-link}
  - [Install ROCm Validation Suite](#install-rocm-validation-suite){.reference .internal .nav-link}
  - [Benchmark, stress, and qualification tests](#benchmark-stress-and-qualification-tests){.reference .internal .nav-link}
  - [BabelStream test](#babelstream-test){.reference .internal .nav-link}
- [RCCL tests](#rccl-tests){.reference .internal .nav-link}
- [TransferBench test](#transferbench-test){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

:::::::::::::::::::: {#system-health-benchmarks-for-ai-workloads .section}
[]{#rocm-for-ai-system-health-bench}

# System health benchmarks for AI workloads[\#](#system-health-benchmarks-for-ai-workloads "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 5 min read time
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

Before running AI workloads, it is important to validate that your AMD hardware is configured correctly and is performing optimally. This topic outlines several system health benchmarks you can use to test key aspects like GPU compute capabilities (FLOPS), memory bandwidth, and interconnect performance. Many of these tests are part of the ROCm Validation Suite (RVS).

:::::::: {#rocm-validation-suite-rvs-tests .section}
## ROCm Validation Suite (RVS) tests[\#](#rocm-validation-suite-rvs-tests "Link to this heading"){.headerlink}

RVS provides a collection of tests, benchmarks, and qualification tools, each targeting a specific subsystem of the system under test. It includes tests for GPU stress and memory bandwidth.

::::: {#install-rocm-validation-suite .section}
[]{#healthcheck-install-rvs}

### Install ROCm Validation Suite[\#](#install-rocm-validation-suite "Link to this heading"){.headerlink}

To get started, install RVS. For example, on an Ubuntu system with ROCm already installed, run the following command:

:::: {.highlight-shell .notranslate}
::: highlight
    sudo apt update
    sudo apt install rocm-validation-suite
:::
::::

See the [ROCm Validation Suite installation instructions](https://rocm.docs.amd.com/projects/ROCmValidationSuite/en/latest/install/installation.html){.reference .external}, and [System validation tests](https://instinct.docs.amd.com/projects/system-acceptance/en/latest/common/system-validation.html){.reference .external} in the Instinct documentation for more detailed instructions.
:::::

::: {#benchmark-stress-and-qualification-tests .section}
### Benchmark, stress, and qualification tests[\#](#benchmark-stress-and-qualification-tests "Link to this heading"){.headerlink}

The GPU stress test runs various GEMM computations as workloads to stress the GPU FLOPS performance and check whether it meets the configured target GFLOPS.

Run the benchmark, stress, and qualification tests included with RVS. See the [Benchmark, stress, qualification](https://instinct.docs.amd.com/projects/system-acceptance/en/latest/common/system-validation.html#benchmark-stress-qualification){.reference .external} section of the Instinct documentation for usage instructions.
:::

::: {#babelstream-test .section}
### BabelStream test[\#](#babelstream-test "Link to this heading"){.headerlink}

BabelStream is a synthetic GPU benchmark based on the STREAM benchmark for CPUs, measuring memory transfer rates to and from global device memory. BabelStream tests are included with the RVS package as part of the [BABEL module](https://rocm.docs.amd.com/projects/ROCmValidationSuite/en/latest/conceptual/rvs-modules.html#babel-benchmark-test-babel-module){.reference .external}.

For more information, see [Performance benchmarking](https://instinct.docs.amd.com/projects/system-acceptance/en/latest/common/system-validation.html#babelstream){.reference .external} in the Instinct documentation.
:::
::::::::

::: {#rccl-tests .section}
## RCCL tests[\#](#rccl-tests "Link to this heading"){.headerlink}

The ROCm Communication Collectives Library (RCCL) enables efficient multi-GPU communication. The [ROCm/rccl-tests](https://github.com/ROCm/rccl-tests){.github .reference .external} suite benchmarks the performance and verifies the correctness of these collective operations. This helps ensure optimal scaling for multi-GPU tasks.

1.  To get started, build RCCL-tests using the official instructions in the README at [ROCm/rccl-tests](https://github.com/ROCm/rccl-tests?tab=readme-ov-file#build){.github .reference .external} or use the following commands:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/rccl-tests.git
        cd rccl-tests
        make
    :::
    ::::

2.  Run the suggested RCCL tests -- see [RCCL benchmarking](https://instinct.docs.amd.com/projects/system-acceptance/en/latest/network/rdma-benchmarking.html#rccl-benchmarking-results){.reference .external} in the AMD Instinct customer acceptance guide.
:::

::: {#transferbench-test .section}
## TransferBench test[\#](#transferbench-test "Link to this heading"){.headerlink}

TransferBench is a standalone utility for benchmarking simultaneous data transfer performance between various devices in the system, including CPU-to-GPU and GPU-to-GPU (peer-to-peer). This helps identify potential bottlenecks in data movement between the host system and the GPUs, or between GPUs, which can impact end-to-end latency.

1.  To get started, use the instructions in the [TransferBench documentation](https://rocm.docs.amd.com/projects/TransferBench/en/latest/install/install.html#install-transferbench){.reference .external} or use the following commands:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        git clone https://github.com/ROCm/TransferBench.git
        cd TransferBench
        CC=hipcc make
    :::
    ::::

2.  Run the suggested TransferBench tests -- see [TransferBench benchmarking](https://instinct.docs.amd.com/projects/system-acceptance/en/latest/common/system-validation.html#transferbench){.reference .external} in the Instinct performance benchmarking documentation for instructions.
:::
::::::::::::::::::::

::::: prev-next-area
[](multi-node-setup.html "previous page"){.left-prev}

::: prev-next-info
previous

Multi-node setup for AI workloads
:::

[](../training/index.html "next page"){.right-next}

::: prev-next-info
next

Use ROCm for training
:::
:::::
:::::::::::::::::::::::::::::::::::::

:::::: {.bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {.page-toc .tocsection .onthispage}
Contents
:::

- [ROCm Validation Suite (RVS) tests](#rocm-validation-suite-rvs-tests){.reference .internal .nav-link}
  - [Install ROCm Validation Suite](#install-rocm-validation-suite){.reference .internal .nav-link}
  - [Benchmark, stress, and qualification tests](#benchmark-stress-and-qualification-tests){.reference .internal .nav-link}
  - [BabelStream test](#babelstream-test){.reference .internal .nav-link}
- [RCCL tests](#rccl-tests){.reference .internal .nav-link}
- [TransferBench test](#transferbench-test){.reference .internal .nav-link}
::::
:::::
::::::
::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::
