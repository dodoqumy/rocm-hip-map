---
title: "AMD Instinct™ MI300 Series microarchitecture"
source_url: "https://rocm.docs.amd.com/en/latest/conceptual/gpu-arch/mi300.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T06:57:58.359815+00:00
content_hash: "dcd7dcf8805e6d27"
---

:::::::::::::::::::::::::::::::::
{#main-content .bd-main role="main"}

sbt-scroll-pixel-helper

:::::::::::::::::::::::::::::::
bd-content
::::::::::::::::::::::::::
bd-article-container
:::::::
{.bd-header-article .d-print-none}
::::::
{.header-article-items .header-article__inner}
::
header-article-items__start

header-article-item
[]{.fa-solid .fa-angle-right}

header-article-item

::

::
header-article-items__end
:
header-article-item

article-header-buttons
[]{.fa-solid .fa-list}

:
::
::::::
:::::::

{#jb-print-docs-body .onlyprint}
# AMD Instinct™ MI300 Series microarchitecture

::
{#print-main-content}
:
{#jb-print-toc}

{}
## Contents

:
::

{#searchbox}

::::::::::::
{#amd-instinct-mi300-series-microarchitecture .section .tex2jax_ignore .mathjax_ignore}
# AMD Instinct™ MI300 Series microarchitecture[\#](#amd-instinct-mi300-series-microarchitecture "Link to this heading"){.headerlink}

::::::::
{#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::
{.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::
{.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::
{.sd-container-fluid .sd-sphinx-override .docutils}
::::
{.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}

{.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23

{.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 6 min read time

{.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils style="color:gray;"}
Applies to Linux and Windows

{.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}

::::
:::::
::::::
:::::::
::::::::

The AMD Instinct MI300 Series GPUs are based on the AMD CDNA 3 architecture which was designed to deliver leadership performance for HPC, artificial intelligence (AI), and machine learning (ML) workloads. The AMD Instinct MI300 Series GPUs are well-suited for extreme scalability and compute performance, running on everything from individual servers to the world's largest exascale supercomputers.

With the MI300 Series, AMD is introducing the Accelerator Complex Die (XCD), which contains the GPU computational elements of the processor along with the lower levels of the cache hierarchy.

The following image depicts the structure of a single XCD in the AMD Instinct MI300 GPU Series.

<figure id="mi300-xcd" class="align-center">
<img src="../../_images/xcd-sys-arch.png" alt="../../_images/xcd-sys-arch.png" />
<figcaption><p><span class="caption-text">XCD-level system architecture showing 40 Compute Units, each with 32 KB L1 cache, a Unified Compute System with 4 ACE Compute Accelerators, shared 4MB of L2 cache and an HWS Hardware Scheduler.</span><a href="#mi300-xcd" class="headerlink" title="Link to this image">#</a></p></figcaption>
</figure>

On the XCD, four Asynchronous Compute Engines (ACEs) send compute shader workgroups to the Compute Units (CUs). The XCD has 40 CUs: 38 active CUs at the aggregate level and 2 disabled CUs for yield management. The CUs all share a 4 MB L2 cache that serves to coalesce all memory traffic for the die. With less than half of the CUs of the AMD Instinct MI200 Series compute die, the AMD CDNA™ 3 XCD die is a smaller building block. However, it uses more advanced packaging and the processor can include 6 or 8 XCDs for up to 304 CUs, roughly 40% more than MI250X.

The MI300 Series integrate up to 8 vertically stacked XCDs, 8 stacks of High-Bandwidth Memory 3 (HBM3) and 4 I/O dies (containing system infrastructure) using the AMD Infinity Fabric™ technology as interconnect.

The Matrix Cores inside the CDNA 3 CUs have significant improvements, emphasizing AI and machine learning, enhancing throughput of existing data types while adding support for new data types. CDNA 2 Matrix Cores support FP16 and BF16, while offering INT8 for inference. Compared to MI250X GPUs, CDNA 3 Matrix Cores triple the performance for FP16 and BF16, while providing a performance gain of 6.8 times for INT8. FP8 has a performance gain of 16 times compared to FP32, while TF32 has a gain of 4 times compared to FP32.

pst-scrollable-table-container
  Computation and Data Type   FLOPS/CLOCK/CU   Peak TFLOPS
  --------------------------- ---------------- -------------
  Matrix FP64                 256              163.4
  Vector FP64                 128              81.7
  Matrix FP32                 256              163.4
  Vector FP32                 256              163.4
  Vector TF32                 1024             653.7
  Matrix FP16                 2048             1307.4
  Matrix BF16                 2048             1307.4
  Matrix FP8                  4096             2614.9
  Matrix INT8                 4096             2614.9

  : [Peak-performance capabilities of the MI300X for different data types.]{.caption-text}[\#](#mi300x-perf-table "Link to this table"){.headerlink} {#mi300x-perf-table .table}

The above table summarizes the aggregated peak performance of the AMD Instinct MI300X Open Compute Platform (OCP) Open Accelerator Modules (OAMs) for different data types and command processors. The middle column lists the peak performance (number of data elements processed in a single instruction) of a single compute unit if a SIMD (or matrix) instruction is submitted in each clock cycle. The third column lists the theoretical peak performance of the OAM. The theoretical aggregated peak memory bandwidth of the GPU is 5.3 TB per second.

The following image shows the block diagram of the APU (left) and the OAM package (right) both connected via AMD Infinity Fabric™ network on-chip.

<figure id="mi300-arch" class="align-center">
<img src="../../_images/image008.png" />
<figcaption><p><span class="caption-text">MI300 Series system architecture showing MI300A (left) with 6 XCDs and 3 CCDs, while the MI300X (right) has 8 XCDs.</span><a href="#mi300-arch" class="headerlink" title="Link to this image">#</a></p></figcaption>
</figure>

{#node-level-architecture .section}
## Node-level architecture[\#](#node-level-architecture "Link to this heading"){.headerlink}

<figure id="mi300-node" class="align-center">
<img src="../../_images/mi300-node-level-arch.png" alt="../../_images/mi300-node-level-arch.png" />
<figcaption><p><span class="caption-text">MI300 Series node-level architecture showing 8 fully interconnected MI300X OAM modules connected to (optional) PCIEe switches via retimers and HGX connectors.</span><a href="#mi300-node" class="headerlink" title="Link to this image">#</a></p></figcaption>
</figure>

The image above shows the node-level architecture of a system with AMD EPYC processors in a dual-socket configuration and eight AMD Instinct MI300X GPUs. The MI300X OAMs attach to the host system via PCIe Gen 5 x16 links (yellow lines). The GPUs are using seven high-bandwidth, low-latency AMD Infinity Fabric™ links (red lines) to form a fully connected 8-GPU system.

{.toctree-wrapper .compound}

::::::::::::
::::::::::::::::::::::::::

{.bd-sidebar-secondary .bd-toc}
::
{.sidebar-secondary-items .sidebar-secondary__inner}
:
sidebar-secondary-item

{.page-toc .tocsection .onthispage}
Contents

:
::

:::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::
