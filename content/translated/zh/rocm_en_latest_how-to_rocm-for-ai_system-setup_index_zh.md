---
title: "System setup for AI workloads on ROCm"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/system-setup/index.html"
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
- System\...

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons
[]{.fa-solid .fa-list}

# System setup for AI workloads on ROCm

## Contents

- [Prerequisite system validation](#prerequisite-system-validation){.reference .internal .nav-link}
- [Docker images for AMD Instinct GPUs](#docker-images-for-amd-instinct-gpus){.reference .internal .nav-link}
  - [Multi-node training](#multi-node-training){.reference .internal .nav-link}
- [System optimization and validation](#system-optimization-and-validation){.reference .internal .nav-link}

# System setup for AI workloads on ROCm[\#](#system-setup-for-ai-workloads-on-rocm "Link to this heading"){.headerlink}

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 3 min read time

Applies to Linux

Before you begin training or inference on AMD Instinct™ GPUs, complete the following system setup and validation steps to ensure optimal performance.

## Prerequisite system validation[\#](#prerequisite-system-validation "Link to this heading"){.headerlink}

First, confirm that your system meets all software and hardware prerequisites. See [[Prerequisite system validation before running AI workloads]{.doc}](prerequisite-system-validation.html){.reference .internal}.

## Docker images for AMD Instinct GPUs[\#](#docker-images-for-amd-instinct-gpus "Link to this heading"){.headerlink}

AMD provides prebuilt Docker images for AMD Instinct™ MI300X and MI325X GPUs. These images include ROCm-enabled deep learning frameworks and essential software components. They support single-node and multi-node configurations and are ready for training and inference workloads out of the box.

### Multi-node training[\#](#multi-node-training "Link to this heading"){.headerlink}

For instructions on enabling multi-node training, see [[Multi-node setup for AI workloads]{.doc}](multi-node-setup.html){.reference .internal}.

## System optimization and validation[\#](#system-optimization-and-validation "Link to this heading"){.headerlink}

Before running workloads, verify that the system is configured correctly and operating at peak efficiency. Recommended steps include:

- Disabling NUMA auto-balancing

- Running system benchmarks to validate hardware performance

For details on running system health checks, see [[System health benchmarks for AI workloads]{.doc}](system-health-check.html){.reference .internal}.

::::: prev-next-area
[](../install.html "previous page"){.left-prev}

::: prev-next-info
previous

Installing ROCm and deep learning frameworks

[](prerequisite-system-validation.html "next page"){.right-next}

::: prev-next-info
next

Prerequisite system validation before running AI workloads

:::: sidebar-secondary-item
Contents

- [Prerequisite system validation](#prerequisite-system-validation){.reference .internal .nav-link}
- [Docker images for AMD Instinct GPUs](#docker-images-for-amd-instinct-gpus){.reference .internal .nav-link}
  - [Multi-node training](#multi-node-training){.reference .internal .nav-link}
- [System optimization and validation](#system-optimization-and-validation){.reference .internal .nav-link}