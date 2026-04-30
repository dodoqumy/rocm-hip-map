---
title: "AMD Instinct™ MI100 microarchitecture"
source_url: "https://rocm.docs.amd.com/en/latest/conceptual/gpu-arch/mi100.html"
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
- [](../../index.html){.nav-link aria-label="首页"}
- [GPU 架构文档](../gpu-arch.html){.nav-link}
- AMD...

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons
[]{.fa-solid .fa-list}

# AMD Instinct（AMD 数据中心 GPU 系列）™ MI100 微架构

## 目录



- [微架构](#microarchitecture){.reference .internal .nav-link}



# AMD Instinct（Instinct（AMD 数据中心 GPU 系列））™ MI100 微架构[\#](#amd-instinct-mi100-微架构 "Link to this heading"){.headerlink}



2026年1月23日

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS73NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 6 分钟阅读时间

适用于 Linux 和 Windows

下图展示了一个系统的节点级架构，该系统包含两个 AMD EPYC™ 处理器和（最多）八个 AMD Instinct™ GPU。两个 EPYC 处理器通过 AMD Infinity™ 互连技术相连，该技术提供高带宽（最高 18 GT/秒）的一致性链路，使每个处理器都能以非均匀内存架构（NUMA）方式访问节点中可用的内存作为单一共享内存域。在 2P（双插槽）配置中，有三个 AMD Infinity™ 互连链路可用于连接处理器，另外每个处理器还提供一个 PCIe Gen 4 x16 链路，可用于连接额外的 I/O 设备，如网络互连的主机适配器。

![AMD Instinct（AMD 数据中心 GPU 系列）MI100 GPU 中单个 GCD 的结构](../../_images/image004.png)

在典型的节点配置中，每个处理器可容纳多达四个 AMD Instinct™ GPU，这些GPU通过PCIe Gen 4链路连接，传输速率为16 GT/秒，对应32 GB/秒的峰值双向链路带宽。每组四个GPU可以通过全连接、一致的AMD Infinity Fabric™互连，该互连使用23 GT/秒的AMD Infinity Fabric链路，运行频率高于处理器间链路。如果GPU安装在相邻的PCIe插槽中，则可以通过为AMD Instinct™ GPU安装AMD Infinity Fabric™桥接器在认证服务器系统中建立此GPU互连。

## Microarchitecture[\#](#microarchitecture "Link to this heading"){.headerlink}

AMD Instinct（AMD 数据中心 GPU 系列）GPU 的微架构基于 AMD CDNA（计算 DNA 架构）架构，该架构面向高性能计算（HPC）及 AI 与机器学习（ML）等计算应用，可运行于从单台服务器到全球最大型百亿亿次超级计算机的各种计算环境。整体系统架构专为极致可扩展性和计算性能而设计。

![AMD Instinct（AMD 数据中心 GPU 系列）GPU (MI100 代) 结构图](../../_images/image005.png)

上图展示了 AMD Instinct（AMD 数据中心 GPU 系列）GPU 及其配备的 PCIe Gen 4 x16 链路（16 GT/秒，位于底部），该链路将 GPU 连接到（其中一个）主机处理器。同时也展示了三个 AMD Infinity Fabric（AMD 高速互联总线）端口，这些端口提供高速链路（23 GT/秒，同样位于底部），用于连接本地集群中的其他 GPU。



在平面图的左侧和右侧，高带宽存储器（HBM）通过GPU内存控制器连接。MI100代AMD Instinct（AMD 数据中心 GPU 系列）GPU提供四个HBM2堆栈（共32GB），内存接口宽度为4,096位。HBM2的峰值内存带宽为1.228 TB/秒，内存时钟频率为1.2 GHz。

GPU的执行单元如上图所示，为计算单元（Compute Units，CU）。共计120个计算单元，物理上分为八个着色引擎（Shader Engines，SE），每个着色引擎包含十五个计算单元。每个计算单元又进一步细分为四个SIMD单元，每个SIMD单元处理包含16个数据元素的SIMD指令。这使得CU能够以1.5 GHz的峰值时钟频率处理64个数据元素（所谓的"wavefront"波前）。因此，理论最大FP64峰值性能为11.5 TFLOPS（[`4`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`[SIMD`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`units]`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`x`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`16`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`[elements`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`per`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`instruction]`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`x`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`120`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`[CU]`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`x`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`1.5`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`[GHz]`{.docutils .literal .notranslate}]{.pre}）。



![MI100 计算单元框图，包含 AMD CDNA（计算 DNA 架构）详细 SIMD 视图](../../_images/image006.png)

上图展示了 AMD Instinct™ MI100 GPU 单个计算单元（CU）的框图，概述了指令如何在执行引擎中流动。计算单元通过 32KB 指令缓存获取指令，并通过分发器将其发送到执行单元。计算单元最多可同时处理十个波前，并将它们的指令送入执行单元。执行单元包含 256 个向量通用寄存器（VGPR）和 800 个标量通用寄存器（SGPR）。VGPR 和 SGPR 动态分配给正在执行的波前。一个波前最多可访问 102 个标量寄存器。过度使用标量寄存器会导致寄存器溢出，从而可能影响执行性能。

一个 wavefront 可以占用 0 到 256 个 VGPR 中的任意数量，直接影响 occupancy（即 CU 中同时活跃的 wavefront 数量）。例如，当使用 119 个 VGPR 时，最多只能有两个 wavefront 在 CU 中同时活跃。由于每条 SIMD 指令的延迟为四个周期，occupancy 应该尽可能高，以便计算单元可以通过调度多个 wavefront 的指令来提高执行效率。

::: pst-scrollable-table-container
  计算和数据类型                FLOPS/CLOCK/CU   峰值 TFLOPS
  --------------------------- ---------------- -------------
  向量 FP64                  64               11.5
  矩阵 FP32                  256              46.1
  向量 FP32                  128              23.1
  矩阵 FP16                  1024             184.6
  矩阵 BF16                  512              92.3



::::: prev-next-area
[](mi250.html "上一页"){.left-prev}

::: prev-next-info
上一页

AMD Instinct（AMD 数据中心 GPU 系列）™ MI250 微架构

[](../file-reorg.html "next page"){.right-next}

::: prev-next-info
next

ROCm（Radeon开放计算平台）Linux文件系统层次结构标准重组

:::: sidebar-secondary-item
目录



- [微架构](#microarchitecture){.reference .internal .nav-link}