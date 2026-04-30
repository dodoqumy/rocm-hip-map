---
title: "Troubleshoot BAR access limitation"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/Bar-Memory.html"
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
- 故障排除...

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons
[]{.fa-solid .fa-list}



# 排查 BAR 访问限制问题

## 目录



- [处理物理地址限制](#handling-physical-address-limitation){.reference .internal .nav-link}
- [AMD GPU 的 BAR 配置](#bar-configuration-for-amd-gpus){.reference .internal .nav-link}
  - [AMD GPU 的 BAR 使用示例](#example-of-bar-usage-on-amd-gpus){.reference .internal .nav-link}

# 故障排除 BAR 访问限制[\#](#troubleshoot-bar-access-limitation "Link to this heading"){.headerlink}



[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9N0aWNvbiBjYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026年1月23日

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 8 min read time

适用于 Linux 和 Windows

使用基址寄存器（BAR）对 PCIe 设备的直接内存访问（DMA）可能因物理寻址限制而受到约束。这些限制可能导致系统组件之间的数据访问失败。对等（P2P）DMA 用于访问设备之间的寄存器和内存等资源。PCIe 设备需要内存映射输入/输出（MMIO）空间进行 DMA，这些 MMIO 空间在 PCIe BAR 中定义。

这些BAR是一组32位或64位寄存器，用于定义PCIe设备提供的资源。CPU和其他系统设备也使用这些寄存器来访问PCIe设备的资源。P2P DMA仅在当一个设备能够直接访问另一个设备的本地BAR内存时才能工作。如果某个BAR内存的地址超出了设备的物理寻址能力范围，该设备将无法访问该BAR。这可能是设备自身的BAR，也可能是系统中其他设备的BAR。

如果BAR内存超过设备的物理寻址限制，该设备将无法访问远程BAR。



要处理可能出现的任何 BAR 访问问题，您需要了解设备的物理地址限制，并理解 [[AMD GPU 的 BAR 配置]{.std .std-ref}](#bar-configuration){.reference .internal}。此信息在设置系统物理地址空间中 PCIe 设备的额外 MMIO 窗口时非常重要。

## 处理物理地址限制[\#](#handling-physical-address-limitation "Link to this heading"){.headerlink}

当系统启动时，系统BIOS会为系统中的组件分配物理地址空间，包括系统内存和MMIO aperture。在现代64位平台上，通常有两个或多个MMIO aperture：一个位于4GB物理地址空间以下，用于32位兼容性；一个或多个位于4GB以上，用于需要更大空间的设备。



你可以通过系统BIOS配置选项控制高端MMIO窗口的内存地址。这允许你配置额外的MMIO空间以与物理寻址限制对齐，并支持设备之间的P2P DMA。例如，如果PCIe设备的物理寻址限制为44位，则应确保MMIO窗口设置在系统物理地址空间的44位以下。



有两种方法可以处理此问题：

- 确保高位 MMIO 窗口位于系统中设备的物理寻址限制范围内。例如，如果设备具有 44 位物理寻址限制，请在 BIOS 中设置 [`MMIO`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`High`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`Base`{.docutils .literal .notranslate}]{.pre} 和 [`MMIO`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`High`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`size`{.docutils .literal .notranslate}]{.pre} 选项，使窗口位于 44 位地址范围内，并确保 [`Above`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`4G`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`Decoding`{.docutils .literal .notranslate}]{.pre} 选项为 Enabled。



- 启用输入输出内存管理单元 (IOMMU)。当 IOMMU 在非直通模式下启用时，它会为系统上的每个设备创建虚拟 I/O 地址空间。它还确保在该空间中创建的所有虚拟地址都在设备的物理寻址范围内。有关 IOMMU 的更多信息，请参阅 [输入输出内存管理单元 (IOMMU)](https://instinct.docs.amd.com/projects/amdgpu-docs/zh_cn/latest/conceptual/iommu.html){.reference .external}。

## BAR 配置（针对 AMD GPU）[\#](#bar-configuration-for-amd-gpus "Link to this heading"){.headerlink}

下表展示了 AMD GPU 的 BAR 配置方式。

::: pst-scrollable-table-container
+------------------+----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| BAR 类型         | 值                              | 描述                                                                                                                                                                                                                                                                                                                                               |
+==================+==================================+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------===================================================================================+
| BAR0-1 寄存器   | 64 位，可预取，GPU 内存         | 8 GB 或 16 GB，取决于 GPU。设置为小于 2\^44 以支持具有 44 位物理地址限制的其他 GPU 进行 P2P 访问。可预取内存通过在请求之前从同一数据源预取连续数据来实现更快的读取操作，从而为高性能计算 (HPC) 提供更高的性能。 |
+------------------+----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| BAR2-3 寄存器   | 64 位，可预取，Doorbell         | 设置为小于 2\^44 以支持具有 44 位物理地址限制的其他 GPU 进行 P2P 访问。作为 Doorbell BAR，它向 GPU 指示其队列中有新的操作等待处理。                                                                                                                                               |
+------------------+----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| BAR4 寄存器     | 可选                           | 非启动设备                                                                                                                                                                                                                                                                                                                                 |
+------------------+----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| BAR5 寄存器     | 32 位，不可预取，MMIO          | 设置为小于 4 GB。                                                                                                                                                                                                                                                                                                                                                                                         |
+------------------+----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

### AMD GPU 上 BAR 使用示例[\#](#example-of-bar-usage-on-amd-gpus "Link to this heading"){.headerlink}



以下为 GFX8 GPU 在 40 位物理寻址限制下由系统 BIOS 设置的 BAR 示例配置：

::: highlight
    11:00.0 显示控制器: Advanced Micro Devices, Inc. [AMD/ATI] Fiji [Radeon（AMD 消费级 GPU 系列）R9 FURY / NANO
    Series] (修订版 c1)



子系统：Advanced Micro Devices, Inc. [AMD/ATI] 设备 0b35

标志：总线主设备，快速设备选择，延迟 0，IRQ 119

内存位于 bf40000000 (64位, 可预取) [大小=256M]

bf50000000 处的内存 (64位, 可预取) [大小=2M]

I/O 端口位于 3000 [大小=256]

内存位于 c7400000 (32位, 不可预取) [大小=256K]

扩展ROM位于c7440000[已禁用][大小=128K]

示例中配置的 BAR 详情如下：



**GPU 帧缓冲器 BAR：** `Memory` `at` `bf40000000` `(64-bit, prefetchable)` `[size=256M]`

本例中BAR的大小为256 MB。通常，它将是GPU内存的大小（通常为4 GB+）。根据AMD GPU的物理地址限制和代际，BAR可以设置为低于2^40、2^44或2^48。

**Doorbell BAR：**`内存`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`位于`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`bf50000000`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`(64位,`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`可预取)`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`[大小=2M]`{.docutils .literal .notranslate}

BAR 的大小通常应小于该代 GPU 的 10 MB，在本示例中已设置为 2 MB。此 BAR 放置在 2^40 以下，以便允许与其他代 AMD GPU 进行点对点访问。



**I/O BAR:** I/O 端口在 3000 [size=256]

这是为了支持传统VGA和启动设备。由于所使用的GPU没有连接到显示器（VGA设备），这并不重要，即使系统BIOS中没有进行相关设置。

**MMIO BAR：**[`内存`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`地址`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`c7400000`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`(32位，`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`不可预取)`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`[大小=256K]`{.docutils .literal .notranslate}]{.pre}



AMD 驱动程序需要此权限才能访问配置寄存器。由于可用 BAR 空间仅剩 1 个 DWORD（32 位），因此设置为小于 4 GB。在示例中，固定为 256 KB。

**扩展ROM：** [`Expansion`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`ROM`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`at`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`c7440000`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`[disabled]`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`[size=128K]`{.docutils .literal .notranslate}]{.pre}

这是AMD Driver访问GPU video-BIOS所需要的。在示例中，它固定为128 KB。



::::: prev-next-area
[](setting-cus.html "previous page"){.left-prev}

::: prev-next-info
上一页

设置计算单元数量

[](../conceptual/gpu-arch.html "下一页"){.right-next}

::: prev-next-info
next

GPU架构文档

:::: sidebar-secondary-item
目录



- [处理物理地址限制](#handling-physical-address-limitation){.reference .internal .nav-link}
- [AMD GPU 的 BAR 配置](#bar-configuration-for-amd-gpus){.reference .internal .nav-link}
  - [AMD GPU 上 BAR 使用示例](#example-of-bar-usage-on-amd-gpus){.reference .internal .nav-link}