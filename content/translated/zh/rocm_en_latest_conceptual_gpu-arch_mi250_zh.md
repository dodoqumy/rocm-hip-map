---
title: "AMD Instinct™ MI250 microarchitecture"
source_url: "https://rocm.docs.amd.com/en/latest/conceptual/gpu-arch/mi250.html"
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
- [首页](../../index.html){.nav-link aria-label="首页"}
- [GPU 架构文档](../gpu-arch.html){.nav-link}
- AMD...

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons
[]{.fa-solid .fa-list}



# AMD Instinct（Instinct（AMD 数据中心 GPU 系列））™ MI250 微架构

## 目录



- [节点级架构](#node-level-architecture){.reference .internal .nav-link}

# AMD Instinct（Instinct（AMD 数据中心 GPU 系列））™ MI250 微架构[\#](#amd-instinct-mi250-microarchitecture "Link to this heading"){.headerlink}



[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-article-article-info-date-svg} 2026年1月23日



[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-itime-svg} 7 分钟阅读时间

适用于 Linux 和 Windows

AMD Instinct MI250 GPU 的微架构基于 AMD CDNA 2 架构，该架构面向高性能计算、人工智能（AI）和机器学习（ML）等计算应用，运行范围从单个服务器到世界上最大的百亿亿次超级计算机。整体系统架构设计为极致的可扩展性和计算性能。

以下图片展示了一个 CDNA 2（计算 DNA 架构）架构中单个 GCD（图形计算芯片）的组件。顶部和底部是 AMD Infinity Fabric 接口及其物理链路，用于将 GPU 芯片连接到节点的其他系统级组件（另见 2.2 节）。两个接口均可驱动四条 AMD Infinity Fabric 链路。底部控制器中的其中一条 AMD Infinity Fabric 链路可配置为 PCIe 链路。GPU 之间的各条 AMD Infinity Fabric 链路最高可达 25 GT/秒，对于 16 位宽链路（每个事务两个字节），这相当于 50 GB/秒的峰值传输带宽。2.2 节详细介绍了 AMD Infinity Fabric 链路的数量以及系统级组件之间的传输速率。



左右两侧是内存控制器，负责将高带宽内存（HBM）模块连接到 GCD。AMD Instinct（AMD 数据中心 GPU 系列）MI250 GPU 采用 HBM2e，每个 GCD 可提供 1.6 TB/秒的峰值内存带宽。

GPU的执行单元在下图所示为计算单元(CU)。MI250 GCD有104个活跃的计算单元。每个计算单元进一步细分为四个SIMD单元，每个SIMD单元处理SIMD指令，每条指令处理16个数据元素(针对FP64数据类型)。这使得每个计算单元能够以1.7 GHz的峰值时钟频率处理64个工作项(所谓的"wavefront")。因此，每个GCD的理论最大FP64峰值性能为向量指令22.6 TFLOPS。相当于两个GCD合计的向量指令45.3 TFLOPS。MI250计算单元还提供专用的执行单元(也称为矩阵核心)，专门用于执行矩阵运算，如矩阵-矩阵乘法。针对FP64，这些单元的峰值性能为90.5 TFLOPS。

![单个 GCD 在 AMD Instinct（AMD 数据中心 GPU 系列）MI250 GPU 中的结构。](../../_images/image001.png)



::: pst-scrollable-table-container
  计算和数据类型               FLOPS/CLOCK/CU   峰值 TFLOPS
  --------------------------- ---------------- -------------
  矩阵 FP64                   256              90.5
  向量 FP64                   128              45.3
  矩阵 FP32                   256              90.5
  压缩 FP32                   256              90.5
  向量 FP32                   128              45.3
  矩阵 FP16                   1024             362.1
  矩阵 BF16                   1024             362.1
  矩阵 INT8                   1024             362.1



上述表格总结了 AMD Instinct（AMD 数据中心 GPU 系列）MI250 Open Compute Platform (OCP) Open Accelerator Modules (OAMs) 及其两个 GCD 在不同数据类型和执行单元下的聚合峰值性能。中间列列出了单个计算单元的峰值性能（单个指令中处理的数据元素数量），前提是每个时钟周期都有一条 SIMD（或矩阵）指令完成执行。第三列列出了 OAM 模块的理论峰值性能。GPU 的理论聚合峰值内存带宽为 3.2 TB/秒（每个 GCD 为 1.6 TB/秒）。



AMD Instinct（AMD 数据中心 GPU 系列）MI250 GPU 的双 GCD 架构



下图展示了 OAM 模组的框图，该模组由两个 GCD 组成，每个 GCD 在系统中构成一个 GPU 设备。OAM 模组中的两个 GCD 通过四条 AMD Infinity Fabric（AMD 高速互联总线）链路连接，理论峰值传输速率为 25 GT/秒，使得 OAM 两个 GCD 之间的峰值传输带宽达到 200 GB/秒，或者在双向传输情况下达到 400 GB/秒的峰值传输带宽。

## 节点级架构[\#](#node-level-architecture "Link to this heading"){.headerlink}

以下图片展示了基于 AMD Instinct（AMD 数据中心 GPU 系列）MI250 GPU 的系统节点级架构。MI250 OAM 通过 PCIe Gen 4 x16 链路（黄色线条）连接到主机系统。每个 GCD 保持其自身与系统主机部分的 PCIe x16 链路。根据服务器平台的不同，GCD 可以直接连接到 AMD EPYC 处理器，或通过可选的 PCIe 交换机连接。请注意，某些平台可能为 GCD 提供 x8 接口，这会降低可用的主机到 GPU 带宽。

![AMD Instinct（AMD 数据中心 GPU 系列）MI250 GPU 与第3代 AMD EPYC 处理器框图](../../_images/image003.png)

上面的图像展示了一个采用双插槽配置的 AMD EPYC 处理器和四个 AMD Instinct（AMD 数据中心 GPU 系列）MI250 GPU 的系统节点级架构。MI250 OAM 通过 PCIe Gen 4 x16 链路（黄色线）连接到主机处理器系统。根据系统设计，可能存在 PCIe 交换机，以为网络接口和/或存储设备等附加组件提供更多 PCIe 通道。每个 GCD 保持其自身的 PCIe x16 链路，连接到系统的主机部分或 PCIe 交换机。请注意，某些平台可能提供 x8 接口到 GCD，这将降低可用的主机到 GPU 带宽。

在 OAM 及其相应的 GCD 之间，P2P 网络允许通过 AMD Infinity Fabric（Infinity Fabric（AMD 高速互联总线））链路（黑色、绿色和红色线条表示）在 GPU dies 之间直接进行数据交换。这些 16 通道链路分别连接到 MI250 OAM 中的两个 GPU dies 之一，运行速率为 25 GT/sec，对应于每条链路 50 GB/sec 的理论峰值传输速率（或 100 GB/sec 的双向峰值传输带宽）。GCD 对 2 和 6 以及 GCD 0 和 4 通过两条 XGMI 链路连接，如前图中较粗的红色线条所示。

::::: prev-next-area
[](mi350-performance-counters.html "上一页"){.left-prev}

上一页



MI350 Series 性能计数器



[](mi100.html "下一页"){.right-next}

::: prev-next-info
下一页

AMD Instinct（Instinct（AMD 数据中心 GPU 系列））™ MI100 微架构

目录

- [节点级架构](#node-level-architecture){.reference .internal .nav-link}