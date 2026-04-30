---
title: "AMD Instinct MI300X performance guides"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/gpu-performance/mi300x.html"
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

```
::: header-article-item
- [](../../index.html){.nav-link aria-label="首页"}
- AMD\...
```

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons



# AMD Instinct（AMD 数据中心 GPU 系列）MI300X 性能指南

# AMD Instinct（AMD 数据中心 GPU 系列）MI300X 性能指南[\#](#amd-instinct-mi300x-performance-guides "Link to this heading"){.headerlink}

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23



[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 阅读时长 3 分钟

适用于 Linux 和 Windows

以下性能指南提供必要的指导，介绍正确为 AMD Instinct（AMD 数据中心 GPU 系列）™ MI300X GPU 配置系统所需的必要步骤。这些指南包含有关系统设置和应用程序 [[workload tuning]{.doc}](../rocm-for-ai/inference-optimization/workload.html){.reference .internal} 的详细说明，帮助您充分利用这些 GPU 的最大能力并实现卓越性能。



- [AMD Instinct MI300X 系统优化](https://instinct. docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi300x.html){.reference .external} 涵盖 essential 系统设置和系统管理实践，用于配置您的 AMD Instinct MI300X 系统以获得最佳性能。



- [[AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） MI300X 工作负载优化]{.doc}](../rocm-for-ai/inference-optimization/workload.html){.reference .internal} 涵盖了针对 HPC 和深度学习操作优化 AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） MI300X 系列 GPU 性能的步骤。



- [[vLLM inference]{.doc}](../rocm-for-ai/inference/benchmark-docker/vllm.html){.reference .internal} 介绍了一个用于 LLM 推理的预配置环境，旨在帮助您使用流行模型在 AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） MI300X Series GPU 上测试性能。

[](../system-optimization/index.html "上一页"){.left-prev}

::: prev-next-info
previous

系统优化



[](../system-debugging.html "下一页"){.right-next}

::: prev-next-info
下一页

系统调试