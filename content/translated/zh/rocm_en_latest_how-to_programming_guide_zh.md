---
title: "Programming guide"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/programming_guide.html"
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
- [](../index.html){.nav-link aria-label="Home"}
- 编程指南

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons

# 编程指南

# 编程指南[\#](#programming-guide "Link to this heading"){.headerlink}

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 3 分钟阅读时间

适用于 Linux 和 Windows

ROCm（ROCm（Radeon 开放计算平台））为运行在 CPU 和 AMD GPU 上的异构程序提供了一个强大的环境。ROCm（ROCm（Radeon 开放计算平台））支持多种编程语言和框架，以帮助开发者利用 AMD GPU 的强大性能。原生支持的编程语言是 HIP（HIP（异构接口可移植性））(Heterogeneous-Compute Interface for Portability) 和 OpenCL，但 HIP（HIP（异构接口可移植性））绑定可用于 Python 和 Fortran。

HIP（HIP（异构接口可移植性））是一个基于 C++ 的 API，为 GPU 编程提供运行时和内核语言，并且是 ROCm（ROCm（Radeon 开放计算平台））的基本编程语言。HIP（HIP（异构接口可移植性））也被设计为一种转换语言，允许为 NVIDIA CUDA（CUDA（统一计算设备架构））编写的代码容易地移植到在 AMD GPU 上运行。开发者可以使用 HIP（HIP（异构接口可移植性））编写在 AMD GPU 上执行的内核，同时保持与基于 CUDA（CUDA（统一计算设备架构））的系统的兼容性。

OpenCL (Open Computing Language) is an open standard for cross-platform, parallel programming of diverse processors. ROCm supports OpenCL for developers who want to use standard frameworks across different hardware platforms, including CPUs, GPUs, and APUs. For more information, see [OpenCL](https://www.khronos.org/opencl/){.reference .external}.

Python bindings can be found at [ROCm/hip-python](https://github.com/ROCm/hip-python){.github .reference .external}. Python is popular in AI and machine learning applications due to available frameworks like TensorFlow and PyTorch.

Fortran bindings can be found at [ROCm/hipfort](https://github.com/ROCm/hipfort){.github .reference .external}. It enables scientific, academic, and legacy applications, particularly those in high-performance computing, to run on AMD GPUs via HIP.

For a complete description of the HIP programming language, see the [[HIP programming guide]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/HIP/en/latest/index.html "(in HIP Documentation v7.2.53211)"){.reference .external}.

::: prev-next-area