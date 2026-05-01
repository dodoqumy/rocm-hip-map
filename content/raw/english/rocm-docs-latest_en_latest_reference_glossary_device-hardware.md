---
title: "Device hardware glossary"
source_url: "https://rocm.docs.amd.com/en/latest/reference/glossary/device-hardware.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-01
---

::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

::::::::::::::::::::::::::::: bd-content
:::::::::::::::::::::::::::: bd-article-container
:::::::::: {.bd-header-article .d-print-none}
::::::::: {.header-article-items .header-article__inner}
::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}
:::

::: header-article-item
- [](../../index.html){.nav-link aria-label="Home"}
- [ROCm glossary](../glossary.html){.nav-link}
- Device\...
:::
:::::

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons
:::
::::
:::::
:::::::::
::::::::::

::::: {#jb-print-docs-body .onlyprint}
# Device hardware glossary

:::: {#print-main-content}
::: {#jb-print-toc}
:::
::::
:::::

::: {#searchbox}
:::

:::::::::::: {#device-hardware-glossary .section}
[]{#glossary-device-hardware}

# Device hardware glossary[\#](#device-hardware-glossary "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-02-20
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 9 min read time
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils style="color:gray;"}
Applies to Linux and Windows
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
:::
:::::::
::::::::
:::::::::
::::::::::
:::::::::::

This section provides concise definitions of hardware components and architectural features of AMD GPUs.

AccVGPR[\#](#term-AccVGPR "Link to this term"){.headerlink}

:   Accumulation General Purpose Vector Registers (AccVGPRs) are a special type of [[VGPRs]{.xref .std .std-term}](#term-VGPR){.reference .internal} used exclusively for matrix operations.

ALU[\#](#term-ALU "Link to this term"){.headerlink}

:   Arithmetic logic units (ALUs) are the primary arithmetic engines that execute mathematical and logical operations within [[compute units]{.xref .std .std-term}](#term-Compute-units){.reference .internal}. See [Vector arithmetic logic unit (VALU)](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/hardware_implementation.html#valu "(in HIP Documentation v7.2.53211)"){.reference .external} for details.

AMD device architecture[\#](#term-AMD-device-architecture "Link to this term"){.headerlink}

:   AMD device architecture is based on unified, programmable compute engines known as [[compute units (CUs)]{.xref .std .std-term}](#term-Compute-units){.reference .internal}. See [Hardware implementation](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/hardware_implementation.html#hardware-implementation "(in HIP Documentation v7.2.53211)"){.reference .external} for details.

Compute unit versioning[\#](#term-Compute-unit-versioning "Link to this term"){.headerlink}

:   [[Compute units]{.xref .std .std-term}](#term-Compute-units){.reference .internal} are versioned with [[GFX IP]{.xref .std .std-term}](#term-GFX-IP){.reference .internal} identifiers that define their microarchitectural features and instruction set compatibility. See [Target GPU architectures (GFX IP)](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/compilers.html#gfx-ip "(in HIP Documentation v7.2.53211)"){.reference .external} for details.

Compute units[\#](#term-Compute-units "Link to this term"){.headerlink}

:   Compute units (CUs) are the fundamental programmable execution engines in AMD GPUs capable of running complex programs. See [Compute unit architecture](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/hardware_implementation.html#compute-unit "(in HIP Documentation v7.2.53211)"){.reference .external} for details.

Data movement engine[\#](#term-Data-movement-engine "Link to this term"){.headerlink}

:   Data movement engines (DMEs) are specialized hardware units in AMD Instinct MI300 and MI350 series GPUs that accelerate multi-dimensional tensor data copies between global memory and on-chip memory. See [Data movement engine (CDNA 3 / CDNA 4)](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/hardware_implementation.html#dme "(in HIP Documentation v7.2.53211)"){.reference .external} for details.

GCD[\#](#term-GCD "Link to this term"){.headerlink}

:   On AMD Instinct MI100 and MI250 series GPUs and AMD Radeon GPUs, the Graphics Compute Die (GCD) contains the GPU's computational elements and lower levels of the cache hierarchy. See [[AMD Instinct™ MI250 microarchitecture]{.doc}](../../conceptual/gpu-arch/mi250.html){.reference .internal} for details.

GFX IP[\#](#term-GFX-IP "Link to this term"){.headerlink}

:   GFX IP (Graphics IP) versions are identifiers that specify which instruction formats, memory models, and compute features are supported by each AMD GPU generation. See [Target GPU architectures (GFX IP)](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/compilers.html#gfx-ip "(in HIP Documentation v7.2.53211)"){.reference .external} for versioning information.

GFX IP major version[\#](#term-GFX-IP-major-version "Link to this term"){.headerlink}

:   The [[GFX IP]{.xref .std .std-term}](#term-GFX-IP){.reference .internal} major version represents the GPU's core instruction set and architecture. For example, a GFX IP 11 major version corresponds to the RDNA3 architecture, influencing driver support and available compute features. See [Target GPU architectures (GFX IP)](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/compilers.html#gfx-ip "(in HIP Documentation v7.2.53211)"){.reference .external} for versioning information.

GFX IP minor version[\#](#term-GFX-IP-minor-version "Link to this term"){.headerlink}

:   The [[GFX IP]{.xref .std .std-term}](#term-GFX-IP){.reference .internal} minor version represents specific variations within a [[GFX IP]{.xref .std .std-term}](#term-GFX-IP){.reference .internal} major version and affects feature sets, optimizations, and driver behavior. Different GPU models within the same major version can have unique capabilities, impacting performance and supported instructions. See [Target GPU architectures (GFX IP)](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/compilers.html#gfx-ip "(in HIP Documentation v7.2.53211)"){.reference .external} for versioning information.

GPU RAM (VRAM)[\#](#term-GPU-RAM-VRAM "Link to this term"){.headerlink}

:   GPU RAM, also known as [[global memory]{.xref .std .std-term}](device-software.html#term-Global-memory){.reference .internal} in the HIP programming model, is the large, high-capacity off-chip memory subsystem accessible by all [[compute units]{.xref .std .std-term}](#term-Compute-units){.reference .internal}, forming the foundation of the device's [[memory hierarchy]{.xref .std .std-ref}](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/hardware_implementation.html#hbm "(in HIP Documentation v7.2.53211)"){.reference .external}.

Graphics L1 cache[\#](#term-Graphics-L1-cache "Link to this term"){.headerlink}

:   On AMD Radeon GPUs, the read-only graphics level 1 (L1) cache is local to groups of [[WGPs]{.xref .std .std-term}](#term-WGP){.reference .internal} called shader arrays, providing fast access to recently used data. AMD Instinct GPUs do not feature the graphics L1 cache.

Infinity Cache (L3 cache)[\#](#term-Infinity-Cache-L3-cache "Link to this term"){.headerlink}

:   On AMD Instinct MI300 and MI350 series GPUs and AMD Radeon GPUs, the Infinity Cache is the last level cache of the cache hierarchy. It is shared by all [[compute units]{.xref .std .std-term}](#term-Compute-units){.reference .internal} and [[WGPs]{.xref .std .std-term}](#term-WGP){.reference .internal} on the GPU.

L0 instruction cache[\#](#term-L0-instruction-cache "Link to this term"){.headerlink}

:   On AMD Radeon GPUs, the level 0 (L0) instruction cache is local to each [[WGP]{.xref .std .std-term}](#term-WGP){.reference .internal} and thus shared between the WGP's [[compute units]{.xref .std .std-term}](#term-Compute-units){.reference .internal}.

L0 scalar cache[\#](#term-L0-scalar-cache "Link to this term"){.headerlink}

:   On AMD Radeon GPUs, the level 0 (L0) scalar data cache is local to each [[WGP]{.xref .std .std-term}](#term-WGP){.reference .internal} and thus shared between the WGP's [[compute units]{.xref .std .std-term}](#term-Compute-units){.reference .internal}. It provides the [[scalar ALU]{.xref .std .std-term}](#term-SALU){.reference .internal} with fast access to recently used data.

L0 vector cache[\#](#term-L0-vector-cache "Link to this term"){.headerlink}

:   On AMD Radeon GPUs, the level 0 (L0) vector data cache is local to each [[WGP]{.xref .std .std-term}](#term-WGP){.reference .internal} and thus shared between the WGP's [[compute units]{.xref .std .std-term}](#term-Compute-units){.reference .internal}. It provides the [[vector ALU]{.xref .std .std-term}](#term-VALU){.reference .internal} with fast access to recently used data.

L1 instruction cache[\#](#term-L1-instruction-cache "Link to this term"){.headerlink}

:   On AMD Instinct GPUs, the level 1 (L1) instruction cache is local to each [[compute unit]{.xref .std .std-term}](#term-Compute-units){.reference .internal}. On AMD Radeon GPUs, the L1 instruction cache does not exist as a separate cache level, and instructions are stored in the [[L0 instruction cache]{.xref .std .std-term}](#term-L0-instruction-cache){.reference .internal}.

L1 scalar cache[\#](#term-L1-scalar-cache "Link to this term"){.headerlink}

:   On AMD Instinct GPUs, the level 1 (L1) scalar data cache is local to each [[compute unit]{.xref .std .std-term}](#term-Compute-units){.reference .internal}, providing the [[scalar ALU]{.xref .std .std-term}](#term-SALU){.reference .internal} with fast access to recently used data. On AMD Radeon GPUs, the L1 scalar cache does not exist as a separate cache level, and recently used scalar data is stored in the [[L0 scalar cache]{.xref .std .std-term}](#term-L0-scalar-cache){.reference .internal}.

L1 vector cache[\#](#term-L1-vector-cache "Link to this term"){.headerlink}

:   On AMD Instinct GPUs, the level 1 (L1) vector data cache is local to each [[compute unit]{.xref .std .std-term}](#term-Compute-units){.reference .internal}, providing the [[vector ALU]{.xref .std .std-term}](#term-VALU){.reference .internal} with fast access to recently used data. On AMD Radeon GPUs, the L1 vector cache does not exist as a separate cache level, and recently used vector data is stored in the [[L0 vector cache]{.xref .std .std-term}](#term-L0-vector-cache){.reference .internal}.

L2 cache[\#](#term-L2-cache "Link to this term"){.headerlink}

:   On AMD Instinct MI100 series GPUs, the L2 cache is shared across the entire chip, while for all other AMD GPUs the L2 caches are shared by the [[compute units]{.xref .std .std-term}](#term-Compute-units){.reference .internal} on the same [[GCD]{.xref .std .std-term}](#term-GCD){.reference .internal} or [[XCD]{.xref .std .std-term}](#term-XCD){.reference .internal}.

Load/store unit[\#](#term-Load-store-unit "Link to this term"){.headerlink}

:   Load/store units (LSUs) handle data transfer between [[compute units]{.xref .std .std-term}](#term-Compute-units){.reference .internal} and the GPU's memory subsystems, managing thousands of concurrent memory operations. See [Load/store unit (LSU)](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/hardware_implementation.html#lsu "(in HIP Documentation v7.2.53211)"){.reference .external} for details.

Local data share[\#](#term-Local-data-share "Link to this term"){.headerlink}

:   Local data share (LDS) is fast on-chip memory local to each [[compute unit]{.xref .std .std-term}](#term-Compute-units){.reference .internal} and shared among [[work-items]{.xref .std .std-term}](#term-Work-item-Thread){.reference .internal} in a [[work-group]{.xref .std .std-term}](#term-Work-group-Block){.reference .internal}, enabling efficient coordination and data reuse. In the HIP programming model, the LDS is known as shared memory. See [Local data share (LDS)](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/hardware_implementation.html#lds "(in HIP Documentation v7.2.53211)"){.reference .external} for LDS programming details.

Matrix cores (MFMA units)[\#](#term-Matrix-cores-MFMA-units "Link to this term"){.headerlink}

:   Matrix cores (MFMA units) are specialized execution units that perform large-scale matrix operations in a single instruction, delivering high throughput for AI and HPC workloads. See [Matrix fused multiply-add (MFMA)](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/hardware_implementation.html#mfma-units "(in HIP Documentation v7.2.53211)"){.reference .external} for details.

Register file[\#](#term-Register-file "Link to this term"){.headerlink}

:   The register file is the primary on-chip memory store in each [[compute unit]{.xref .std .std-term}](#term-Compute-units){.reference .internal}, holding data between arithmetic and memory operations. See [Memory model](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/programming_model.html#memory-hierarchy "(in HIP Documentation v7.2.53211)"){.reference .external} for details.

Registers[\#](#term-Registers "Link to this term"){.headerlink}

:   Registers are the lowest level of the memory hierarchy, storing per-thread temporary variables and intermediate results. See [Memory model](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/programming_model.html#memory-hierarchy "(in HIP Documentation v7.2.53211)"){.reference .external} for register usage details.

SALU[\#](#term-SALU "Link to this term"){.headerlink}

:   Scalar [[ALUs]{.xref .std .std-term}](#term-ALU){.reference .internal} (SALUs) operate on a single value per [[wavefront]{.xref .std .std-term}](https://rocm.docs.amd.com/projects/rocPRIM/en/latest/reference/rocPRIM-glossary.html#term-Wavefront "(in rocPRIM Documentation v4.2.0)"){.reference .external} and manage all control flow.

SGPR[\#](#term-SGPR "Link to this term"){.headerlink}

:   Scalar general-purpose [[registers]{.xref .std .std-term}](#term-Registers){.reference .internal} (SGPRs) hold data produced and consumed by a [[compute unit]{.xref .std .std-term}](#term-Compute-units){.reference .internal}'s [[scalar ALU]{.xref .std .std-term}](#term-SALU){.reference .internal}.

SGPR file[\#](#term-SGPR-file "Link to this term"){.headerlink}

:   The [[SGPR]{.xref .std .std-term}](#term-SGPR){.reference .internal} file is the [[register file]{.xref .std .std-term}](#term-Register-file){.reference .internal} that holds data used by the [[scalar ALU]{.xref .std .std-term}](#term-SALU){.reference .internal}.

SIMD core[\#](#term-SIMD-core "Link to this term"){.headerlink}

:   SIMD cores are execution lanes that perform scalar and vector arithmetic operations inside each [[compute unit]{.xref .std .std-term}](https://rocm.docs.amd.com/projects/composable_kernel/en/latest/reference/Composable-Kernel-Glossary.html#term-compute-unit "(in Composable Kernel Documentation v1.2.0)"){.reference .external}. See [CDNA architecture](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/hardware_implementation.html#cdna-architecture "(in HIP Documentation v7.2.53211)"){.reference .external} and [RDNA architecture](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/hardware_implementation.html#rdna-architecture "(in HIP Documentation v7.2.53211)"){.reference .external} for details.

Special function unit[\#](#term-Special-function-unit "Link to this term"){.headerlink}

:   Special function units (SFUs) accelerate transcendental and reciprocal mathematical functions such as [`exp`{.docutils .literal .notranslate}]{.pre}, [`log`{.docutils .literal .notranslate}]{.pre}, [`sin`{.docutils .literal .notranslate}]{.pre}, and [`cos`{.docutils .literal .notranslate}]{.pre}. See [Special function unit (SFU)](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/hardware_implementation.html#sfu "(in HIP Documentation v7.2.53211)"){.reference .external} for details.

VALU[\#](#term-VALU "Link to this term"){.headerlink}

:   Vector [[ALUs]{.xref .std .std-term}](#term-ALU){.reference .internal} (VALUs) perform an arithmetic or logical operation on data for each [[work-item]{.xref .std .std-term}](#term-Work-item-Thread){.reference .internal} in a [[wavefront]{.xref .std .std-term}](https://rocm.docs.amd.com/projects/rocPRIM/en/latest/reference/rocPRIM-glossary.html#term-Wavefront "(in rocPRIM Documentation v4.2.0)"){.reference .external}, enabling data-parallel execution.

VGPR[\#](#term-VGPR "Link to this term"){.headerlink}

:   Vector general-purpose [[registers]{.xref .std .std-term}](#term-Registers){.reference .internal} (VGPRs) hold data produced and consumed by a [[compute unit]{.xref .std .std-term}](#term-Compute-units){.reference .internal}'s [[vector ALU]{.xref .std .std-term}](#term-VALU){.reference .internal}.

VGPR file[\#](#term-VGPR-file "Link to this term"){.headerlink}

:   The [[VGPR]{.xref .std .std-term}](#term-VGPR){.reference .internal} file is the [[register file]{.xref .std .std-term}](#term-Register-file){.reference .internal} that holds data used by the [[vector ALU]{.xref .std .std-term}](#term-VALU){.reference .internal}. GPUs with [[matrix cores]{.xref .std .std-term}](#term-Matrix-cores-MFMA-units){.reference .internal} also have [[AccVGPR]{.xref .std .std-term}](#term-AccVGPR){.reference .internal} files, used specifically for matrix instructions.

Wavefront (Warp)[\#](#term-Wavefront-Warp "Link to this term"){.headerlink}

:   A wavefront (also called a warp) is a group of [[work-items]{.xref .std .std-term}](#term-Work-item-Thread){.reference .internal} that execute in parallel on a single [[compute unit]{.xref .std .std-term}](#term-Compute-units){.reference .internal}, sharing one instruction stream. See [Warp (or Wavefront)](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/programming_model.html#wavefront "(in HIP Documentation v7.2.53211)"){.reference .external} for execution details.

Wavefront scheduler[\#](#term-Wavefront-scheduler "Link to this term"){.headerlink}

:   The wavefront scheduler in each [[compute unit]{.xref .std .std-term}](#term-Compute-units){.reference .internal} decides which [[wavefront]{.xref .std .std-term}](https://rocm.docs.amd.com/projects/composable_kernel/en/latest/reference/Composable-Kernel-Glossary.html#term-wavefront "(in Composable Kernel Documentation v1.2.0)"){.reference .external} to execute each clock cycle, enabling rapid context switching for latency hiding. See [Sequencer and scheduling](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/hardware_implementation.html#wave-scheduling "(in HIP Documentation v7.2.53211)"){.reference .external} for details.

Wavefront size[\#](#term-Wavefront-size "Link to this term"){.headerlink}

:   The wavefront size is the number of [[work-items]{.xref .std .std-term}](#term-Work-item-Thread){.reference .internal} that execute together in a single [[wavefront]{.xref .std .std-term}](#term-Wavefront-Warp){.reference .internal}. For AMD Instinct GPUs, the wavefront size is 64 threads, while AMD Radeon GPUs have a wavefront size of 32 threads. See [Warp (or Wavefront)](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/programming_model.html#wavefront "(in HIP Documentation v7.2.53211)"){.reference .external} for details.

WGP[\#](#term-WGP "Link to this term"){.headerlink}

:   A Workgroup Processor (WGP) is a hardware unit on AMD Radeon GPUs that contains two [[compute units]{.xref .std .std-term}](#term-Compute-units){.reference .internal} and their associated resources, enabling efficient scheduling and execution of [[wavefronts]{.xref .std .std-term}](https://rocm.docs.amd.com/projects/composable_kernel/en/latest/reference/Composable-Kernel-Glossary.html#term-wavefront "(in Composable Kernel Documentation v1.2.0)"){.reference .external}. See [RDNA architecture](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/hardware_implementation.html#rdna-architecture "(in HIP Documentation v7.2.53211)"){.reference .external} for details.

Work-group (Block)[\#](#term-Work-group-Block "Link to this term"){.headerlink}

:   A work-group (also called a block) is a collection of [[wavefronts]{.xref .std .std-term}](#term-Wavefront-Warp){.reference .internal} scheduled together on a single [[compute unit]{.xref .std .std-term}](#term-Compute-units){.reference .internal} that can coordinate through [[Local data share]{.xref .std .std-term}](#term-Local-data-share){.reference .internal} memory. See [Block (Work-group)](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/programming_model.html#inherent-thread-hierarchy-block "(in HIP Documentation v7.2.53211)"){.reference .external} for work-group details.

Work-item (Thread)[\#](#term-Work-item-Thread "Link to this term"){.headerlink}

:   A work-item (also called a thread) is the smallest unit of execution on an AMD GPU and represents a single element of work. See [Thread (Work-item)](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/programming_model.html#work-item "(in HIP Documentation v7.2.53211)"){.reference .external} for thread hierarchy details.

XCD[\#](#term-XCD "Link to this term"){.headerlink}

:   On AMD Instinct MI300 and MI350 series GPUs, the Accelerator Complex Die (XCD) contains the GPU's computational elements and lower levels of the cache hierarchy. See [[AMD Instinct™ MI300 Series microarchitecture]{.doc}](../../conceptual/gpu-arch/mi300.html){.reference .internal} for details.
::::::::::::

::::: prev-next-area
[](../glossary.html "previous page"){.left-prev}

::: prev-next-info
previous

ROCm glossary
:::

[](device-software.html "next page"){.right-next}

::: prev-next-info
next

Device software glossary
:::
:::::
::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::
