---
title: "AMD Instinct™ MI300 Series microarchitecture"
source_url: "https://rocm.docs.amd.com/en/latest/conceptual/gpu-arch/mi300.html"
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
- [](../../index.html){.nav-link aria-label=首页}
- [GPU 架构文档](../gpu-arch.html){.nav-link}
- AMD...

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons
[]{.fa-solid .fa-list}

# AMD Instinct（AMD 数据中心 GPU 系列）™ MI300 Series 微架构

## 目录

- [节点级架构](#node-level-architecture){.reference .internal .nav-link}

# AMD Instinct（AMD 数据中心 GPU 系列）™ MI300 系列微架构[\#](#amd-instinct-mi300-series-microarchitecture "Link to this heading"){.headerlink}



[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026年1月23日

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 6 分钟阅读时间

适用于 Linux 和 Windows

AMD Instinct MI300 系列 GPU 基于 AMD CDNA 3 架构而构建，该架构旨在为 HPC、人工智能 (AI) 和机器学习 (ML) 工作负载提供领先的性能。AMD Instinct MI300 系列 GPU 非常适合极端扩展性和计算性能，从单个服务器到世界上最大的百亿亿级超级计算机都能运行。



随着MI300系列的推出，AMD引入了加速器复合芯片（XCD），其中包含处理器的GPU计算单元以及缓存层次结构的较低层级。

以下图像展示了 AMD Instinct（AMD 数据中心 GPU 系列）MI300 GPU 系列中单个 XCD 的结构。





在 XCD 上，四个异步计算引擎（ACE）向计算单元（CU）发送计算着色器工作组。XCD 具有 40 个 CU：聚合级别上 38 个活动 CU，2 个用于产量管理的禁用 CU。所有 CU 共享一个 4 MB L2 缓存，用于聚合芯片上的所有内存流量。与 AMD Instinct MI200 系列计算芯片的不到一半 CU 数量相比，AMD CDNA 3 XCD 芯片是一个更小的构建块。然而，它使用了更先进的封装工艺，处理器可包含 6 或 8 个 XCD，最多可达 304 个 CU，约比 MI250X 多 40%。

MI300系列集成了最多8个垂直堆叠的XCD芯片、8堆HBM3（高带宽内存3）和4个I/O芯片（包含系统基础设施），使用AMD Infinity Fabric（AMD 高速互联总线）™技术作为互联。



CDNA 3 CU 中的 Matrix Core 有显著改进，强调 AI 和机器学习，增强现有数据类型的吞吐量，同时增加对新数据类型的支持。CDNA 2 Matrix Core 支持 FP16 和 BF16，同时提供用于推理的 INT8。与 MI250X GPU 相比，CDNA 3 Matrix Core 的 FP16 和 BF16 性能提升 3 倍，INT8 性能提升 6.8 倍。FP8 相比 FP32 性能提升 16 倍，TF32 相比 FP32 性能提升 4 倍。



::: pst-scrollable-table-container
| 计算与数据类型 | FLOPS/CLOCK/CU | 峰值 TFLOPS |
|---------------------------|----------------|-------------|
| 矩阵 FP64 | 256 | 163.4 |
| 向量 FP64 | 128 | 81.7 |
| 矩阵 FP32 | 256 | 163.4 |
| 向量 FP32 | 256 | 163.4 |
| 向量 TF32 | 1024 | 653.7 |
| 矩阵 FP16 | 2048 | 1307.4 |
| 矩阵 BF16 | 2048 | 1307.4 |
| 矩阵 FP8 | 4096 | 2614.9 |
| 矩阵 INT8 | 4096 | 2614.9 |



上表总结了 AMD Instinct MI300X Open Compute Platform (OCP) Open Accelerator Modules (OAMs) 在不同数据类型和命令处理器下的聚合峰值性能。中间列列出了单个计算单元的峰值性能（单条指令处理的数据元素数量），前提是每个时钟周期提交一条 SIMD（或矩阵）指令。第三列列出了 OAM 的理论峰值性能。该 GPU 的理论聚合峰值内存带宽为 5.3 TB/s。

下图展示了APU（左）和OAM封装（右）的框图，两者均通过AMD Infinity Fabric（AMD 高速互联总线）™ 片上网络进行连接。

<figure id="mi300-arch" class="align-center">
<img src="../../_images/image008.png" />
<figcaption><p><span class="caption-text">MI300 Series system architecture showing MI300A (left) with 6 XCDs and 3 CCDs, while the MI300X (right) has 8 XCDs.</span><a href="#mi300-arch" class="headerlink" title="Link to this image">#</a></p></figcaption>
</figure>

## 节点级架构[#](#node-level-architecture "Link to this heading"){.headerlink}





上图展示了采用AMD EPYC处理器（双路配置）并配备八个AMD Instinct MI300X GPU的节点级系统架构。MI300X OAM通过PCIe Gen 5 x16链路（黄色线）连接到主机系统。GPU使用七条高带宽、低延迟的AMD Infinity Fabric互联链路（红色线）组成全互联的8-GPU系统。

[](../gpu-arch.html "上一页"){.left-prev}

::: prev-next-info
:::
prev-next

GPU 架构文档

[](mi300-mi200-performance-counters.html "下一页"){.right-next}

下一页

MI300 和 MI200 系列性能计数器与指标

:::: sidebar-secondary-item
目录



- [节点级架构](#node--level-architecture){.reference .internal .nav-link}