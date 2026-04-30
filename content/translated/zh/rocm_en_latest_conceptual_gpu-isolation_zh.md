---
title: "GPU isolation techniques"
source_url: "https://rocm.docs.amd.com/en/latest/conceptual/gpu-isolation.html"
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
- [](../index.html){.nav-link aria-label="首页"}
- GPU...

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons
[]{.fa-solid .fa-list}



# GPU 隔离技术

## 目录

- [环境变量](#environment-variables){.reference .internal .nav-link}
  - [[`ROCR_VISIBLE_DEVICES`{.docutils .literal .notranslate}]{.pre}](#rocr-visible-devices){.reference .internal .nav-link}
  - [[`GPU_DEVICE_ORDINAL`{.docutils .literal .notranslate}]{.pre}](#gpu-device-ordinal){.reference .internal .nav-link}
  - [[`HIP_VISIBLE_DEVICES`{.docutils .literal .notranslate}]{.pre}](#hip-visible-devices){.reference .internal .nav-link}
  - [[`CUDA_VISIBLE_DEVICES`{.docutils .literal .notranslate}]{.pre}](#cuda-visible-devices){.reference .internal .nav-link}
  - [[`OMP_DEFAULT_DEVICE`{.docutils .literal .notranslate}]{.pre}](#omp-default-device){.reference .internal .nav-link}
- [Docker](#docker){.reference .internal .nav-link}
- [GPU直通到虚拟机](#gpu-passthrough-to-virtual-machines){.reference .internal .nav-link}



# GPU 隔离技术 {#gpu-isolation-techniques}



```svg
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23
```

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS73NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 5 分钟阅读时间

适用于 Linux 和 Windows



限制应用程序对部分GPU的访问（即GPU隔离）允许用户向程序隐藏GPU资源。默认情况下，程序只会使用“暴露的”GPU，而忽略系统中其他（隐藏的）GPU。

在 ROCm 软件栈中有多种方法可以实现 GPU 隔离，它们在适用场景和安全性方面有所不同。本页作为这些技术的概述。

## 环境变量[\#](#environment-variables "Link to this heading"){.headerlink}

ROCm 软件堆栈中的运行时环境会读取这些环境变量，以选择要呈现给使用它们的应用程序的可见设备或默认设备。

环境变量不应该被用于隔离不可信的应用程序，因为应用程序可以在初始化运行时之前重置它们。

### [`ROCR_VISIBLE_DEVICES`{.docutils .literal .notranslate}]{.pre}[\#](#rophot-visible-devices "跳转至此标题"){.headerlink}



将暴露给应用程序的设备索引或 [UUID]{.abbr title="universally unique identifier"}}列表。

Runtime：ROCm 软件运行时。适用于所有使用用户模式 ROCm 软件栈的应用程序。

::: code-block-caption
[示例展示 1. 设备以及基于 UUID 的设备]{.caption-text}[\#](#id2 "Link to this code"){.headerlink}

::: highlight
    export ROCR_VISIBLE_DEVICES="0,GPU-4b2c1a9f-8d3e-6f7a-b5c9-2e4d8a1f6c3b"



### [`GPU_DEVICE_ORDINAL`{.docutils .literal .notranslate}]{.pre}[\#](#gpu-device-ordinal "Link to this heading"){.headerlink}

设备索引暴露给 OpenCL 和 HIP（异构接口可移植性）应用程序。



运行时：ROCm Compute Language Runtime（[`ROCclr`{.docutils .literal .notranslate}]{.pre}）。适用于使用 [`ROCclr`{.docutils .literal .notranslate}]{.pre} 抽象层的应用程序和运行时，包括 HIP 和 OpenCL 应用程序。

::: code-block-caption
[示例：暴露系统中的第1和第3个设备]{.caption-text}[\#](#id3 "链接到此代码"){.headerlink}:::



```bash
export GPU_DEVICE_ORDINAL="0,2"
```



### [`HIP_VISIBLE_DEVICES`{.docutils .literal .notranslate}]{.pre}[\#](#hip-visible-devices "链接到此标题"){.headerlink}



暴露给 HIP 应用程序的设备索引



运行时：HIP（异构接口可移植性）运行时。仅适用于在 AMD 平台上使用 HIP（异构接口可移植性）的应用程序。

::: code-block-caption
[展示系统中第1个和第3个设备的示例。]{.caption-text}[\#](#id4 "Link to this code"){.headerlink}



```yaml
::: highlight
    export HIP_VISIBLE_DEVICES="0,2"
```

### [`CUDA_VISIBLE_DEVICES`{.docutils .literal .notranslate}]{.pre}[#](#cuda-visible-devices "链接到此标题"){.headerlink}

为提供 CUDA（CUDA（统一计算设备架构））兼容性，与 [`HIP_VISIBLE_DEVICES`{.docutils .literal .notranslate}]{.pre} 在 AMD 平台上具有相同效果。

运行时：HIP（异构接口可移植性）或 CUDA（统一计算设备架构）运行时。适用于 AMD 或 NVIDIA 平台上的 HIP（异构接口可移植性）应用程序以及 CUDA（统一计算设备架构）应用程序。

### [`OMP_DEFAULT_DEVICE`{.docutils .literal .notranslate}]{.pre}[\#](#omp-default-device "Link to this heading"){.headerlink}

OpenMP 目标卸载所使用的默认设备。

运行时：OpenMP 运行时。仅适用于使用 OpenMP 卸载的应用程序。

::: code-block-caption
[设置默认设备为第三个设备的示例。]{.caption-text}[\#](#id5 "Link to this code"){.headerlink}

```
export OMP_DEFAULT_DEVICE="2"
```

## Docker[\#](#docker "Link to this heading"){.headerlink}



Docker 使用 Linux 内核命名空间为应用程序提供隔离环境。此隔离默认应用于大多数设备，包括 GPU。若要在容器中访问它们，必须显式授予访问权限，详情请参阅 [在容器中访问 GPU](https://rocm.docs.ROCm.com/projects/ROCm/en/latest/how-to/docker.html#docker-access-gpus-in-container "(in ROCm installation on Linux v7.2.2)"){.reference .external}。具体请参阅 [限制 GPU 访问](https://rocm.docs.ROCm.com/projects/ROCm/en/latest/how-to/docker.html#docker-restrict-gpus "(in ROCm installation on Linux v7.2.2)"){.reference .external}，了解如何仅暴露所有 GPU 的一个子集。

Docker 隔离比环境变量更安全，适用于所有使用 [`amdgpu（amdgpu（AMD GPU 内核驱动））`{.docutils .literal .notranslate}]{.pre} 内核模块接口的程序。即使是不使用 ROCm 运行时的程序（如使用 OpenGL 或 Vulkan 的图形应用程序），也只能访问暴露给容器的 GPU。



## GPU 直通到虚拟机[\#](#gpu-直通到虚拟机 "Link to this heading"){.headerlink}

虚拟机实现了最高级别的隔离，因为即使虚拟机内核也与主机隔离。安装在主机系统中的物理设备可以通过 PCIe passthrough 传递给虚拟机。这允许在不同的操作系统上使用 GPU，例如在 Linux 主机上运行 Windows 客户机。

设置 PCIe 直通取决于所使用的虚拟机监控程序。ROCm（Radeon 开放计算平台）正式支持 [VMware ESXi](https://www.vmware.com/products/esxi-and-esx.html){: .reference .external} 针对特定 GPU。

[](file-reorg.html "上一页"){.left-prev}

::: prev-next-info
上一页

ROCm（Radeon 开放计算平台）Linux 文件系统层次结构标准重组

[](cmake-packages.html "下一页"){.right-next}

::: prev-next-info
next

使用 CMake

目录

- [环境变量](#environment-variables){.reference .internal .nav-link}
  - [[`ROCR_VISIBLE_DEVICES`{.docutils .literal .notranslate}]{.pre}](#rocr-visible-devices){.reference .internal .nav-link}
  - [[`GPU_DEVICE_ORDINAL`{.docutils .literal .notranslate}]{.pre}](#gpu-device-ordinal){.reference .internal .nav-link}
  - [[`HIP_VISIBLE_DEVICES`{.docutils .literal .notranslate}]{.pre}](#hip-visible-devices){.reference .internal .nav-link}
  - [[`CUDA_VISIBLE_DEVICES`{.docutils .literal .notranslate}]{.pre}](#cuda-visible-devices){.reference .internal .nav-link}
  - [[`OMP_DEFAULT_DEVICE`{.docutils .literal .notranslate}]{.pre}](#omp-default-device){.reference .internal .nav-link}
- [Docker](#docker){.reference .internal .nav-link}
- [GPU 透传至虚拟机](#gpu-passthrough-to-virtual-machines){.reference .internal .nav-link}