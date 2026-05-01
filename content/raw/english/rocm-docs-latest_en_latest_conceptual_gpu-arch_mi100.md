---
title: "AMD Instinct™ MI100 microarchitecture"
source_url: "https://rocm.docs.amd.com/en/latest/conceptual/gpu-arch/mi100.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T06:56:40.438361+00:00
content_hash: "51456db7265b840d"
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
# AMD Instinct™ MI100 microarchitecture

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
{#amd-instinct-mi100-microarchitecture .section .tex2jax_ignore .mathjax_ignore}
# AMD Instinct™ MI100 microarchitecture[\#](#amd-instinct-mi100-microarchitecture "Link to this heading"){.headerlink}

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

The following image shows the node-level architecture of a system that comprises two AMD EPYC™ processors and (up to) eight AMD Instinct™ GPUs. The two EPYC processors are connected to each other with the AMD Infinity™ fabric which provides a high-bandwidth (up to 18 GT/sec) and coherent links such that each processor can access the available node memory as a single shared-memory domain in a non-uniform memory architecture (NUMA) fashion. In a 2P, or dual-socket, configuration, three AMD Infinity™ fabric links are available to connect the processors plus one PCIe Gen 4 x16 link per processor can attach additional I/O devices such as the host adapters for the network fabric.

![Structure of a single GCD in the AMD Instinct MI100 GPU](../../_images/image004.png)

In a typical node configuration, each processor can host up to four AMD Instinct™ GPUs that are attached using PCIe Gen 4 links at 16 GT/sec, which corresponds to a peak bidirectional link bandwidth of 32 GB/sec. Each hive of four GPUs can participate in a fully connected, coherent AMD Instinct™ fabric that connects the four GPUs using 23 GT/sec AMD Infinity fabric links that run at a higher frequency than the inter-processor links. This inter-GPU link can be established in certified server systems if the GPUs are mounted in neighboring PCIe slots by installing the AMD Infinity Fabric™ bridge for the AMD Instinct™ GPUs.

:
{#microarchitecture .section}
## Microarchitecture[\#](#microarchitecture "Link to this heading"){.headerlink}

The microarchitecture of the AMD Instinct GPUs is based on the AMD CDNA architecture, which targets compute applications such as high-performance computing (HPC) and AI & machine learning (ML) that run on everything from individual servers to the world's largest exascale supercomputers. The overall system architecture is designed for extreme scalability and compute performance.

![Structure of the AMD Instinct GPU (MI100 generation)](../../_images/image005.png)

The above image shows the AMD Instinct GPU with its PCIe Gen 4 x16 link (16 GT/sec, at the bottom) that connects the GPU to (one of) the host processor(s). It also shows the three AMD Infinity Fabric ports that provide high-speed links (23 GT/sec, also at the bottom) to the other GPUs of the local hive.

On the left and right of the floor plan, the High Bandwidth Memory (HBM) attaches via the GPU memory controller. The MI100 generation of the AMD Instinct GPU offers four stacks of HBM generation 2 (HBM2) for a total of 32GB with a 4,096bit-wide memory interface. The peak memory bandwidth of the attached HBM2 is 1.228 TB/sec at a memory clock frequency of 1.2 GHz.

The execution units of the GPU are depicted in the above image as Compute Units (CU). There are a total 120 compute units that are physically organized into eight Shader Engines (SE) with fifteen compute units per shader engine. Each compute unit is further sub-divided into four SIMD units that process SIMD instructions of 16 data elements per instruction. This enables the CU to process 64 data elements (a so-called 'wavefront') at a peak clock frequency of 1.5 GHz. Therefore, the theoretical maximum FP64 peak performance is 11.5 TFLOPS ([`4`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`[SIMD`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`units]`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`x`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`16`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`[elements`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`per`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`instruction]`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`x`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`120`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`[CU]`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`x`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`1.5`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`[GHz]`{.docutils .literal .notranslate}]{.pre}).

![Block diagram of an MI100 compute unit with detailed SIMD view of the AMD CDNA architecture](../../_images/image006.png)

The preceding image shows the block diagram of a single CU of an AMD Instinct™ MI100 GPU and summarizes how instructions flow through the execution engines. The CU fetches the instructions via a 32KB instruction cache and moves them forward to execution via a dispatcher. The CU can handle up to ten wavefronts at a time and feed their instructions into the execution unit. The execution unit contains 256 vector general-purpose registers (VGPR) and 800 scalar general-purpose registers (SGPR). The VGPR and SGPR are dynamically allocated to the executing wavefronts. A wavefront can access a maximum of 102 scalar registers. Excess scalar-register usage will cause register spilling and thus may affect execution performance.

A wavefront can occupy any number of VGPRs from 0 to 256, directly affecting occupancy; that is, the number of concurrently active wavefronts in the CU. For instance, with 119 VGPRs used, only two wavefronts can be active in the CU at the same time. With the instruction latency of four cycles per SIMD instruction, the occupancy should be as high as possible such that the compute unit can improve execution efficiency by scheduling instructions from multiple wavefronts.

pst-scrollable-table-container
  Computation and Data Type   FLOPS/CLOCK/CU   Peak TFLOPS
  --------------------------- ---------------- -------------
  Vector FP64                 64               11.5
  Matrix FP32                 256              46.1
  Vector FP32                 128              23.1
  Matrix FP16                 1024             184.6
  Matrix BF16                 512              92.3

  : [Peak-performance capabilities of MI100 for different data types.]{.caption-text}[\#](#mi100-perf "Link to this table"){.headerlink} {#mi100-perf .table}

:

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
