---
title: "MI300 and MI200 Series performance counters and metrics"
source_url: "https://rocm.docs.amd.com/en/latest/conceptual/gpu-arch/mi300-mi200-performance-counters.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-01
---

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-content
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-article-container
:::::::::: {.bd-header-article .d-print-none}
::::::::: {.header-article-items .header-article__inner}
::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}
:::

::: header-article-item
- [](../../index.html){.nav-link aria-label="Home"}
- [GPU architecture documentation](../gpu-arch.html){.nav-link}
- [AMD Instinct™ MI300 Series microarchitecture](mi300.html){.nav-link}
- MI300 and\...
:::
:::::

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons
[]{.fa-solid .fa-list}
:::
::::
:::::
:::::::::
::::::::::

:::::: {#jb-print-docs-body .onlyprint}
# MI300 and MI200 Series performance counters and metrics

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [MI300 and MI200 Series performance counters](#mi300-and-mi200-series-performance-counters){.reference .internal .nav-link}
  - [Command processor counters](#command-processor-counters){.reference .internal .nav-link}
    - [Command processor-fetcher counters](#command-processor-fetcher-counters){.reference .internal .nav-link}
    - [Command processor-compute counters](#command-processor-compute-counters){.reference .internal .nav-link}
  - [Graphics register bus manager counters](#graphics-register-bus-manager-counters){.reference .internal .nav-link}
  - [Shader processor input counters](#shader-processor-input-counters){.reference .internal .nav-link}
  - [Compute unit counters](#compute-unit-counters){.reference .internal .nav-link}
    - [Instruction mix](#instruction-mix){.reference .internal .nav-link}
    - [Matrix fused multiply-add operation counters](#matrix-fused-multiply-add-operation-counters){.reference .internal .nav-link}
    - [Level counters](#level-counters){.reference .internal .nav-link}
    - [Wavefront counters](#wavefront-counters){.reference .internal .nav-link}
    - [Wavefront cycle counters](#wavefront-cycle-counters){.reference .internal .nav-link}
    - [LDS counters](#lds-counters){.reference .internal .nav-link}
    - [Miscellaneous counters](#miscellaneous-counters){.reference .internal .nav-link}
  - [L1 instruction cache (L1i) and scalar L1 data cache (L1d) counters](#l1-instruction-cache-l1i-and-scalar-l1-data-cache-l1d-counters){.reference .internal .nav-link}
  - [Vector L1 cache subsystem counters](#vector-l1-cache-subsystem-counters){.reference .internal .nav-link}
    - [Texture addressing unit counters](#texture-addressing-unit-counters){.reference .internal .nav-link}
    - [Texture data unit counters](#texture-data-unit-counters){.reference .internal .nav-link}
    - [Texture cache per pipe counters](#texture-cache-per-pipe-counters){.reference .internal .nav-link}
    - [Texture cache arbiter counters](#texture-cache-arbiter-counters){.reference .internal .nav-link}
  - [L2 cache access counters](#l2-cache-access-counters){.reference .internal .nav-link}
- [MI300 and MI200 Series derived metrics list](#mi300-and-mi200-series-derived-metrics-list){.reference .internal .nav-link}
  - [Hardware counters by and over all texture addressing unit instances](#hardware-counters-by-and-over-all-texture-addressing-unit-instances){.reference .internal .nav-link}
  - [Hardware counters over all texture cache per channel instances](#hardware-counters-over-all-texture-cache-per-channel-instances){.reference .internal .nav-link}
  - [Hardware counters by, for, or over all texture cache per pipe instances](#hardware-counters-by-for-or-over-all-texture-cache-per-pipe-instances){.reference .internal .nav-link}
  - [Hardware counter over all texture data unit instances](#hardware-counter-over-all-texture-data-unit-instances){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#mi300-and-mi200-series-performance-counters-and-metrics .section}
# MI300 and MI200 Series performance counters and metrics[\#](#mi300-and-mi200-series-performance-counters-and-metrics "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 39 min read time
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

This document lists and describes the hardware performance counters and derived metrics available for the AMD Instinct™ MI300 and MI200 GPU. You can also access this information using the [[ROCprofiler-SDK]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/how-to/using-rocprofv3.html "(in Rocprofiler SDK v1.1.0)"){.reference .external}.

:::::::::::::::::::::::::::::::::::::::::::::: {#mi300-and-mi200-series-performance-counters .section}
## MI300 and MI200 Series performance counters[\#](#mi300-and-mi200-series-performance-counters "Link to this heading"){.headerlink}

Series performance counters include the following categories:

- [[Command processor counters]{.std .std-ref}](#command-processor-counters){.reference .internal}

- [[Graphics register bus manager counters]{.std .std-ref}](#graphics-register-bus-manager-counters){.reference .internal}

- [[Shader processor input counters]{.std .std-ref}](#spi-counters){.reference .internal}

- [[Compute unit counters]{.std .std-ref}](#compute-unit-counters){.reference .internal}

- [[L1 instruction cache (L1i) and scalar L1 data cache (L1d) counters]{.std .std-ref}](#l1i-and-sl1d-cache-counters){.reference .internal}

- [[Vector L1 cache subsystem counters]{.std .std-ref}](#vector-l1-cache-subsystem-counters){.reference .internal}

- [[L2 cache access counters]{.std .std-ref}](#l2-cache-access-counters){.reference .internal}

The following sections provide additional details for each category.

::: {.admonition .note}
Note

Preliminary validation of all MI300 and MI200 Series performance counters is in progress. Those with an asterisk (\*) require further evaluation.
:::

::::::: {#command-processor-counters .section}
[]{#id1}

### Command processor counters[\#](#command-processor-counters "Link to this heading"){.headerlink}

Command processor counters are further classified into command processor-fetcher and command processor-compute.

:::: {#command-processor-fetcher-counters .section}
#### Command processor-fetcher counters[\#](#command-processor-fetcher-counters "Link to this heading"){.headerlink}

::: pst-scrollable-table-container
  Hardware counter                                                                Unit     Definition
  ------------------------------------------------------------------------------- -------- -------------------------------------------------------------------------------------------------------------------
  [`CPF_CMP_UTCL1_STALL_ON_TRANSLATION`{.docutils .literal .notranslate}]{.pre}   Cycles   Number of cycles one of the compute unified translation caches (L1) is stalled waiting on translation
  [`CPF_CPF_STAT_BUSY`{.docutils .literal .notranslate}]{.pre}                    Cycles   Number of cycles command processor-fetcher is busy
  [`CPF_CPF_STAT_IDLE`{.docutils .literal .notranslate}]{.pre}                    Cycles   Number of cycles command processor-fetcher is idle
  [`CPF_CPF_STAT_STALL`{.docutils .literal .notranslate}]{.pre}                   Cycles   Number of cycles command processor-fetcher is stalled
  [`CPF_CPF_TCIU_BUSY`{.docutils .literal .notranslate}]{.pre}                    Cycles   Number of cycles command processor-fetcher texture cache interface unit interface is busy
  [`CPF_CPF_TCIU_IDLE`{.docutils .literal .notranslate}]{.pre}                    Cycles   Number of cycles command processor-fetcher texture cache interface unit interface is idle
  [`CPF_CPF_TCIU_STALL`{.docutils .literal .notranslate}]{.pre}                   Cycles   Number of cycles command processor-fetcher texture cache interface unit interface is stalled waiting on free tags
:::

The texture cache interface unit is the interface between the command processor and the memory system.
::::

:::: {#command-processor-compute-counters .section}
#### Command processor-compute counters[\#](#command-processor-compute-counters "Link to this heading"){.headerlink}

::: pst-scrollable-table-container
  Hardware counter                                                            Unit     Definition
  --------------------------------------------------------------------------- -------- ------------------------------------------------------------------------------------------------
  [`CPC_ME1_BUSY_FOR_PACKET_DECODE`{.docutils .literal .notranslate}]{.pre}   Cycles   Number of cycles command processor-compute micro engine is busy decoding packets
  [`CPC_UTCL1_STALL_ON_TRANSLATION`{.docutils .literal .notranslate}]{.pre}   Cycles   Number of cycles one of the unified translation caches (L1) is stalled waiting on translation
  [`CPC_CPC_STAT_BUSY`{.docutils .literal .notranslate}]{.pre}                Cycles   Number of cycles command processor-compute is busy
  [`CPC_CPC_STAT_IDLE`{.docutils .literal .notranslate}]{.pre}                Cycles   Number of cycles command processor-compute is idle
  [`CPC_CPC_STAT_STALL`{.docutils .literal .notranslate}]{.pre}               Cycles   Number of cycles command processor-compute is stalled
  [`CPC_CPC_TCIU_BUSY`{.docutils .literal .notranslate}]{.pre}                Cycles   Number of cycles command processor-compute texture cache interface unit interface is busy
  [`CPC_CPC_TCIU_IDLE`{.docutils .literal .notranslate}]{.pre}                Cycles   Number of cycles command processor-compute texture cache interface unit interface is idle
  [`CPC_CPC_UTCL2IU_BUSY`{.docutils .literal .notranslate}]{.pre}             Cycles   Number of cycles command processor-compute unified translation cache (L2) interface is busy
  [`CPC_CPC_UTCL2IU_IDLE`{.docutils .literal .notranslate}]{.pre}             Cycles   Number of cycles command processor-compute unified translation cache (L2) interface is idle
  [`CPC_CPC_UTCL2IU_STALL`{.docutils .literal .notranslate}]{.pre}            Cycles   Number of cycles command processor-compute unified translation cache (L2) interface is stalled
  [`CPC_ME1_DC0_SPI_BUSY`{.docutils .literal .notranslate}]{.pre}             Cycles   Number of cycles command processor-compute micro engine processor is busy
:::

The micro engine runs packet-processing firmware on the command processor-compute counter.
::::
:::::::

:::: {#graphics-register-bus-manager-counters .section}
[]{#id2}

### Graphics register bus manager counters[\#](#graphics-register-bus-manager-counters "Link to this heading"){.headerlink}

::: pst-scrollable-table-container
  Hardware counter                                             Unit     Definition
  ------------------------------------------------------------ -------- -----------------------------------------------------------------------------------
  [`GRBM_COUNT`{.docutils .literal .notranslate}]{.pre}        Cycles   Number of free-running GPU cycles
  [`GRBM_GUI_ACTIVE`{.docutils .literal .notranslate}]{.pre}   Cycles   Number of GPU active cycles
  [`GRBM_CP_BUSY`{.docutils .literal .notranslate}]{.pre}      Cycles   Number of cycles any of the command processor blocks are busy
  [`GRBM_SPI_BUSY`{.docutils .literal .notranslate}]{.pre}     Cycles   Number of cycles any of the shader processor input is busy in the shader engines
  [`GRBM_TA_BUSY`{.docutils .literal .notranslate}]{.pre}      Cycles   Number of cycles any of the texture addressing unit is busy in the shader engines
  [`GRBM_TC_BUSY`{.docutils .literal .notranslate}]{.pre}      Cycles   Number of cycles any of the texture cache blocks are busy
  [`GRBM_CPC_BUSY`{.docutils .literal .notranslate}]{.pre}     Cycles   Number of cycles the command processor-compute is busy
  [`GRBM_CPF_BUSY`{.docutils .literal .notranslate}]{.pre}     Cycles   Number of cycles the command processor-fetcher is busy
  [`GRBM_UTCL2_BUSY`{.docutils .literal .notranslate}]{.pre}   Cycles   Number of cycles the unified translation cache (Level 2 \[L2\]) block is busy
  [`GRBM_EA_BUSY`{.docutils .literal .notranslate}]{.pre}      Cycles   Number of cycles the efficiency arbiter block is busy
:::

Texture cache blocks include:

- Texture cache arbiter

- Texture cache per pipe, also known as vector Level 1 (L1) cache

- Texture cache per channel, also known as known as L2 cache

- Texture cache interface
::::

:::: {#shader-processor-input-counters .section}
[]{#spi-counters}

### Shader processor input counters[\#](#shader-processor-input-counters "Link to this heading"){.headerlink}

::: pst-scrollable-table-container
  Hardware counter                                                       Unit          Definition
  ---------------------------------------------------------------------- ------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------
  [`SPI_CSN_BUSY`{.docutils .literal .notranslate}]{.pre}                Cycles        Number of cycles with outstanding waves
  [`SPI_CSN_WINDOW_VALID`{.docutils .literal .notranslate}]{.pre}        Cycles        Number of cycles enabled by [`perfcounter_start`{.docutils .literal .notranslate}]{.pre} event
  [`SPI_CSN_NUM_THREADGROUPS`{.docutils .literal .notranslate}]{.pre}    Workgroups    Number of dispatched workgroups
  [`SPI_CSN_WAVE`{.docutils .literal .notranslate}]{.pre}                Wavefronts    Number of dispatched wavefronts
  [`SPI_RA_REQ_NO_ALLOC`{.docutils .literal .notranslate}]{.pre}         Cycles        Number of arbiter cycles with requests but no allocation
  [`SPI_RA_REQ_NO_ALLOC_CSN`{.docutils .literal .notranslate}]{.pre}     Cycles        Number of arbiter cycles with compute shader (n^th^ pipe) requests but no compute shader (n^th^ pipe) allocation
  [`SPI_RA_RES_STALL_CSN`{.docutils .literal .notranslate}]{.pre}        Cycles        Number of arbiter stall cycles due to shortage of compute shader (n^th^ pipe) pipeline slots
  [`SPI_RA_TMP_STALL_CSN`{.docutils .literal .notranslate}]{.pre}        Cycles        Number of stall cycles due to shortage of temp space
  [`SPI_RA_WAVE_SIMD_FULL_CSN`{.docutils .literal .notranslate}]{.pre}   SIMD-cycles   Accumulated number of single instruction, multiple data (SIMD) per cycle affected by shortage of wave slots for compute shader (n^th^ pipe) wave dispatch
  [`SPI_RA_VGPR_SIMD_FULL_CSN`{.docutils .literal .notranslate}]{.pre}   SIMD-cycles   Accumulated number of SIMDs per cycle affected by shortage of vector general-purpose register (VGPR) slots for compute shader (n^th^ pipe) wave dispatch
  [`SPI_RA_SGPR_SIMD_FULL_CSN`{.docutils .literal .notranslate}]{.pre}   SIMD-cycles   Accumulated number of SIMDs per cycle affected by shortage of scalar general-purpose register (SGPR) slots for compute shader (n^th^ pipe) wave dispatch
  [`SPI_RA_LDS_CU_FULL_CSN`{.docutils .literal .notranslate}]{.pre}      CU            Number of compute units affected by shortage of local data share (LDS) space for compute shader (n^th^ pipe) wave dispatch
  [`SPI_RA_BAR_CU_FULL_CSN`{.docutils .literal .notranslate}]{.pre}      CU            Number of compute units with compute shader (n^th^ pipe) waves waiting at a BARRIER
  [`SPI_RA_BULKY_CU_FULL_CSN`{.docutils .literal .notranslate}]{.pre}    CU            Number of compute units with compute shader (n^th^ pipe) waves waiting for BULKY resource
  [`SPI_RA_TGLIM_CU_FULL_CSN`{.docutils .literal .notranslate}]{.pre}    Cycles        Number of compute shader (n^th^ pipe) wave stall cycles due to restriction of [`tg_limit`{.docutils .literal .notranslate}]{.pre} for thread group size
  [`SPI_RA_WVLIM_STALL_CSN`{.docutils .literal .notranslate}]{.pre}      Cycles        Number of cycles compute shader (n^th^ pipe) is stalled due to [`WAVE_LIMIT`{.docutils .literal .notranslate}]{.pre}
  [`SPI_VWC_CSC_WR`{.docutils .literal .notranslate}]{.pre}              Qcycles       Number of quad-cycles taken to initialize VGPRs when launching waves
  [`SPI_SWC_CSC_WR`{.docutils .literal .notranslate}]{.pre}              Qcycles       Number of quad-cycles taken to initialize SGPRs when launching waves
:::
::::

:::::::::::::::::: {#compute-unit-counters .section}
[]{#id3}

### Compute unit counters[\#](#compute-unit-counters "Link to this heading"){.headerlink}

The compute unit counters are further classified into instruction mix, matrix fused multiply-add (FMA) operation counters, level counters, wavefront counters, wavefront cycle counters, and LDS counters.

:::: {#instruction-mix .section}
#### Instruction mix[\#](#instruction-mix "Link to this heading"){.headerlink}

::: pst-scrollable-table-container
  Hardware counter                                                     Unit    Definition
  -------------------------------------------------------------------- ------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`SQ_INSTS`{.docutils .literal .notranslate}]{.pre}                  Instr   Number of instructions issued
  [`SQ_INSTS_VALU`{.docutils .literal .notranslate}]{.pre}             Instr   Number of vector arithmetic logic unit (VALU) instructions including matrix FMA issued
  [`SQ_INSTS_VALU_ADD_F16`{.docutils .literal .notranslate}]{.pre}     Instr   Number of VALU half-precision floating-point (F16) [`ADD`{.docutils .literal .notranslate}]{.pre} or [`SUB`{.docutils .literal .notranslate}]{.pre} instructions issued
  [`SQ_INSTS_VALU_MUL_F16`{.docutils .literal .notranslate}]{.pre}     Instr   Number of VALU F16 Multiply instructions issued
  [`SQ_INSTS_VALU_FMA_F16`{.docutils .literal .notranslate}]{.pre}     Instr   Number of VALU F16 FMA or multiply-add instructions issued
  [`SQ_INSTS_VALU_TRANS_F16`{.docutils .literal .notranslate}]{.pre}   Instr   Number of VALU F16 Transcendental instructions issued
  [`SQ_INSTS_VALU_ADD_F32`{.docutils .literal .notranslate}]{.pre}     Instr   Number of VALU full-precision floating-point (F32) [`ADD`{.docutils .literal .notranslate}]{.pre} or [`SUB`{.docutils .literal .notranslate}]{.pre} instructions issued
  [`SQ_INSTS_VALU_MUL_F32`{.docutils .literal .notranslate}]{.pre}     Instr   Number of VALU F32 Multiply instructions issued
  [`SQ_INSTS_VALU_FMA_F32`{.docutils .literal .notranslate}]{.pre}     Instr   Number of VALU F32 FMAor multiply-add instructions issued
  [`SQ_INSTS_VALU_TRANS_F32`{.docutils .literal .notranslate}]{.pre}   Instr   Number of VALU F32 Transcendental instructions issued
  [`SQ_INSTS_VALU_ADD_F64`{.docutils .literal .notranslate}]{.pre}     Instr   Number of VALU F64 [`ADD`{.docutils .literal .notranslate}]{.pre} or [`SUB`{.docutils .literal .notranslate}]{.pre} instructions issued
  [`SQ_INSTS_VALU_MUL_F64`{.docutils .literal .notranslate}]{.pre}     Instr   Number of VALU F64 Multiply instructions issued
  [`SQ_INSTS_VALU_FMA_F64`{.docutils .literal .notranslate}]{.pre}     Instr   Number of VALU F64 FMA or multiply-add instructions issued
  [`SQ_INSTS_VALU_TRANS_F64`{.docutils .literal .notranslate}]{.pre}   Instr   Number of VALU F64 Transcendental instructions issued
  [`SQ_INSTS_VALU_INT32`{.docutils .literal .notranslate}]{.pre}       Instr   Number of VALU 32-bit integer instructions (signed or unsigned) issued
  [`SQ_INSTS_VALU_INT64`{.docutils .literal .notranslate}]{.pre}       Instr   Number of VALU 64-bit integer instructions (signed or unsigned) issued
  [`SQ_INSTS_VALU_CVT`{.docutils .literal .notranslate}]{.pre}         Instr   Number of VALU Conversion instructions issued
  [`SQ_INSTS_VALU_MFMA_I8`{.docutils .literal .notranslate}]{.pre}     Instr   Number of 8-bit Integer matrix FMA instructions issued
  [`SQ_INSTS_VALU_MFMA_F16`{.docutils .literal .notranslate}]{.pre}    Instr   Number of F16 matrix FMA instructions issued
  [`SQ_INSTS_VALU_MFMA_F32`{.docutils .literal .notranslate}]{.pre}    Instr   Number of F32 matrix FMA instructions issued
  [`SQ_INSTS_VALU_MFMA_F64`{.docutils .literal .notranslate}]{.pre}    Instr   Number of F64 matrix FMA instructions issued
  [`SQ_INSTS_MFMA`{.docutils .literal .notranslate}]{.pre}             Instr   Number of matrix FMA instructions issued
  [`SQ_INSTS_VMEM_WR`{.docutils .literal .notranslate}]{.pre}          Instr   Number of vector memory write instructions (including flat) issued
  [`SQ_INSTS_VMEM_RD`{.docutils .literal .notranslate}]{.pre}          Instr   Number of vector memory read instructions (including flat) issued
  [`SQ_INSTS_VMEM`{.docutils .literal .notranslate}]{.pre}             Instr   Number of vector memory instructions issued, including both flat and buffer instructions
  [`SQ_INSTS_SALU`{.docutils .literal .notranslate}]{.pre}             Instr   Number of scalar arithmetic logic unit (SALU) instructions issued
  [`SQ_INSTS_SMEM`{.docutils .literal .notranslate}]{.pre}             Instr   Number of scalar memory instructions issued
  [`SQ_INSTS_SMEM_NORM`{.docutils .literal .notranslate}]{.pre}        Instr   Number of scalar memory instructions normalized to match [`smem_level`{.docutils .literal .notranslate}]{.pre} issued
  [`SQ_INSTS_FLAT`{.docutils .literal .notranslate}]{.pre}             Instr   Number of flat instructions issued
  [`SQ_INSTS_FLAT_LDS_ONLY`{.docutils .literal .notranslate}]{.pre}    Instr   **MI200 Series only** Number of FLAT instructions that read/write only from/to LDS issued. Works only if [`EARLY_TA_DONE`{.docutils .literal .notranslate}]{.pre} is enabled.
  [`SQ_INSTS_LDS`{.docutils .literal .notranslate}]{.pre}              Instr   Number of LDS instructions issued **(MI200: includes flat; MI300: does not include flat)**
  [`SQ_INSTS_GDS`{.docutils .literal .notranslate}]{.pre}              Instr   Number of global data share instructions issued
  [`SQ_INSTS_EXP_GDS`{.docutils .literal .notranslate}]{.pre}          Instr   Number of EXP and global data share instructions excluding skipped export instructions issued
  [`SQ_INSTS_BRANCH`{.docutils .literal .notranslate}]{.pre}           Instr   Number of branch instructions issued
  [`SQ_INSTS_SENDMSG`{.docutils .literal .notranslate}]{.pre}          Instr   Number of [`SENDMSG`{.docutils .literal .notranslate}]{.pre} instructions including [`s_endpgm`{.docutils .literal .notranslate}]{.pre} issued
  [`SQ_INSTS_VSKIPPED`{.docutils .literal .notranslate}]{.pre}         Instr   Number of vector instructions skipped
:::

Flat instructions allow read, write, and atomic access to a generic memory address pointer that can resolve to any of the following physical memories:

- Global Memory

- Scratch ("private")

- LDS ("shared")

- Invalid - [`MEM_VIOL`{.docutils .literal .notranslate}]{.pre} TrapStatus
::::

:::: {#matrix-fused-multiply-add-operation-counters .section}
#### Matrix fused multiply-add operation counters[\#](#matrix-fused-multiply-add-operation-counters "Link to this heading"){.headerlink}

::: pst-scrollable-table-container
  Hardware counter                                                          Unit   Definition
  ------------------------------------------------------------------------- ------ -----------------------------------------------------------
  [`SQ_INSTS_VALU_MFMA_MOPS_I8`{.docutils .literal .notranslate}]{.pre}     IOP    Number of 8-bit integer matrix FMA ops in the unit of 512
  [`SQ_INSTS_VALU_MFMA_MOPS_F16`{.docutils .literal .notranslate}]{.pre}    FLOP   Number of F16 floating matrix FMA ops in the unit of 512
  [`SQ_INSTS_VALU_MFMA_MOPS_BF16`{.docutils .literal .notranslate}]{.pre}   FLOP   Number of BF16 floating matrix FMA ops in the unit of 512
  [`SQ_INSTS_VALU_MFMA_MOPS_F32`{.docutils .literal .notranslate}]{.pre}    FLOP   Number of F32 floating matrix FMA ops in the unit of 512
  [`SQ_INSTS_VALU_MFMA_MOPS_F64`{.docutils .literal .notranslate}]{.pre}    FLOP   Number of F64 floating matrix FMA ops in the unit of 512
:::
::::

::::: {#level-counters .section}
#### Level counters[\#](#level-counters "Link to this heading"){.headerlink}

::: {.admonition .note}
Note

All level counters must be followed by [`SQ_ACCUM_PREV_HIRES`{.docutils .literal .notranslate}]{.pre} counter to measure average latency.
:::

::: pst-scrollable-table-container
  Hardware counter                                                 Unit    Definition
  ---------------------------------------------------------------- ------- ----------------------------------------------------------------------------------------
  [`SQ_ACCUM_PREV`{.docutils .literal .notranslate}]{.pre}         Count   Accumulated counter sample value where accumulation takes place once every four cycles
  [`SQ_ACCUM_PREV_HIRES`{.docutils .literal .notranslate}]{.pre}   Count   Accumulated counter sample value where accumulation takes place once every cycle
  [`SQ_LEVEL_WAVES`{.docutils .literal .notranslate}]{.pre}        Waves   Number of inflight waves
  [`SQ_INST_LEVEL_VMEM`{.docutils .literal .notranslate}]{.pre}    Instr   Number of inflight vector memory (including flat) instructions
  [`SQ_INST_LEVEL_SMEM`{.docutils .literal .notranslate}]{.pre}    Instr   Number of inflight scalar memory instructions
  [`SQ_INST_LEVEL_LDS`{.docutils .literal .notranslate}]{.pre}     Instr   Number of inflight LDS (including flat) instructions
  [`SQ_IFETCH_LEVEL`{.docutils .literal .notranslate}]{.pre}       Instr   Number of inflight instruction fetch requests from the cache
:::

Use the following formulae to calculate latencies:

- Vector memory latency = [`SQ_ACCUM_PREV_HIRES`{.docutils .literal .notranslate}]{.pre} divided by [`SQ_INSTS_VMEM`{.docutils .literal .notranslate}]{.pre}

- Wave latency = [`SQ_ACCUM_PREV_HIRES`{.docutils .literal .notranslate}]{.pre} divided by [`SQ_WAVE`{.docutils .literal .notranslate}]{.pre}

- LDS latency = [`SQ_ACCUM_PREV_HIRES`{.docutils .literal .notranslate}]{.pre} divided by [`SQ_INSTS_LDS`{.docutils .literal .notranslate}]{.pre}

- Scalar memory latency = [`SQ_ACCUM_PREV_HIRES`{.docutils .literal .notranslate}]{.pre} divided by [`SQ_INSTS_SMEM_NORM`{.docutils .literal .notranslate}]{.pre}

- Instruction fetch latency = [`SQ_ACCUM_PREV_HIRES`{.docutils .literal .notranslate}]{.pre} divided by [`SQ_IFETCH`{.docutils .literal .notranslate}]{.pre}
:::::

:::: {#wavefront-counters .section}
#### Wavefront counters[\#](#wavefront-counters "Link to this heading"){.headerlink}

::: pst-scrollable-table-container
  Hardware counter                                               Unit    Definition
  -------------------------------------------------------------- ------- -------------------------------------------------------------------------------------------
  [`SQ_WAVES`{.docutils .literal .notranslate}]{.pre}            Waves   Number of wavefronts dispatched to sequencers, including both new and restored wavefronts
  [`SQ_WAVES_SAVED`{.docutils .literal .notranslate}]{.pre}      Waves   Number of context-saved waves
  [`SQ_WAVES_RESTORED`{.docutils .literal .notranslate}]{.pre}   Waves   Number of context-restored waves sent to sequencers
  [`SQ_WAVES_EQ_64`{.docutils .literal .notranslate}]{.pre}      Waves   Number of wavefronts with exactly 64 active threads sent to sequencers
  [`SQ_WAVES_LT_64`{.docutils .literal .notranslate}]{.pre}      Waves   Number of wavefronts with less than 64 active threads sent to sequencers
  [`SQ_WAVES_LT_48`{.docutils .literal .notranslate}]{.pre}      Waves   Number of wavefronts with less than 48 active threads sent to sequencers
  [`SQ_WAVES_LT_32`{.docutils .literal .notranslate}]{.pre}      Waves   Number of wavefronts with less than 32 active threads sent to sequencers
  [`SQ_WAVES_LT_16`{.docutils .literal .notranslate}]{.pre}      Waves   Number of wavefronts with less than 16 active threads sent to sequencers
:::
::::

:::: {#wavefront-cycle-counters .section}
#### Wavefront cycle counters[\#](#wavefront-cycle-counters "Link to this heading"){.headerlink}

::: pst-scrollable-table-container
  Hardware counter                                                      Unit      Definition
  --------------------------------------------------------------------- --------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`SQ_CYCLES`{.docutils .literal .notranslate}]{.pre}                  Cycles    Clock cycles
  [`SQ_BUSY_CYCLES`{.docutils .literal .notranslate}]{.pre}             Cycles    Number of cycles while sequencers reports it to be busy
  [`SQ_BUSY_CU_CYCLES`{.docutils .literal .notranslate}]{.pre}          Qcycles   Number of quad-cycles each compute unit is busy
  [`SQ_VALU_MFMA_BUSY_CYCLES`{.docutils .literal .notranslate}]{.pre}   Cycles    Number of cycles the matrix FMA arithmetic logic unit (ALU) is busy
  [`SQ_WAVE_CYCLES`{.docutils .literal .notranslate}]{.pre}             Qcycles   Number of quad-cycles spent by waves in the compute units
  [`SQ_WAIT_ANY`{.docutils .literal .notranslate}]{.pre}                Qcycles   Number of quad-cycles spent waiting for anything
  [`SQ_WAIT_INST_ANY`{.docutils .literal .notranslate}]{.pre}           Qcycles   Number of quad-cycles spent waiting for any instruction to be issued
  [`SQ_ACTIVE_INST_ANY`{.docutils .literal .notranslate}]{.pre}         Qcycles   Number of quad-cycles spent by each wave to work on an instruction
  [`SQ_ACTIVE_INST_VMEM`{.docutils .literal .notranslate}]{.pre}        Qcycles   Number of quad-cycles spent by the sequencer instruction arbiter to work on a vector memory instruction
  [`SQ_ACTIVE_INST_LDS`{.docutils .literal .notranslate}]{.pre}         Qcycles   Number of quad-cycles spent by the sequencer instruction arbiter to work on an LDS instruction
  [`SQ_ACTIVE_INST_VALU`{.docutils .literal .notranslate}]{.pre}        Qcycles   Number of quad-cycles spent by the sequencer instruction arbiter to work on a VALU instruction
  [`SQ_ACTIVE_INST_SCA`{.docutils .literal .notranslate}]{.pre}         Qcycles   Number of quad-cycles spent by the sequencer instruction arbiter to work on a SALU or scalar memory instruction
  [`SQ_ACTIVE_INST_EXP_GDS`{.docutils .literal .notranslate}]{.pre}     Qcycles   Number of quad-cycles spent by the sequencer instruction arbiter to work on an [`EXPORT`{.docutils .literal .notranslate}]{.pre} or [`GDS`{.docutils .literal .notranslate}]{.pre} instruction
  [`SQ_ACTIVE_INST_MISC`{.docutils .literal .notranslate}]{.pre}        Qcycles   Number of quad-cycles spent by the sequencer instruction arbiter to work on a [`BRANCH`{.docutils .literal .notranslate}]{.pre} or [`SENDMSG`{.docutils .literal .notranslate}]{.pre} instruction
  [`SQ_ACTIVE_INST_FLAT`{.docutils .literal .notranslate}]{.pre}        Qcycles   Number of quad-cycles spent by the sequencer instruction arbiter to work on a flat instruction
  [`SQ_INST_CYCLES_VMEM_WR`{.docutils .literal .notranslate}]{.pre}     Qcycles   Number of quad-cycles spent to send addr and cmd data for vector memory write instructions
  [`SQ_INST_CYCLES_VMEM_RD`{.docutils .literal .notranslate}]{.pre}     Qcycles   Number of quad-cycles spent to send addr and cmd data for vector memory read instructions
  [`SQ_INST_CYCLES_SMEM`{.docutils .literal .notranslate}]{.pre}        Qcycles   Number of quad-cycles spent to execute scalar memory reads
  [`SQ_INST_CYCLES_SALU`{.docutils .literal .notranslate}]{.pre}        Qcycles   Number of quad-cycles spent to execute non-memory read scalar operations
  [`SQ_THREAD_CYCLES_VALU`{.docutils .literal .notranslate}]{.pre}      Qcycles   Number of quad-cycles spent to execute VALU operations on active threads
  [`SQ_WAIT_INST_LDS`{.docutils .literal .notranslate}]{.pre}           Qcycles   Number of quad-cycles spent waiting for LDS instruction to be issued
:::

[`SQ_THREAD_CYCLES_VALU`{.docutils .literal .notranslate}]{.pre} is similar to [`INST_CYCLES_VALU`{.docutils .literal .notranslate}]{.pre}, but it's multiplied by the number of active threads.
::::

:::: {#lds-counters .section}
#### LDS counters[\#](#lds-counters "Link to this heading"){.headerlink}

::: pst-scrollable-table-container
  Hardware counter                                                    Unit     Definition
  ------------------------------------------------------------------- -------- ------------------------------------------------------------------------------------
  [`SQ_LDS_ATOMIC_RETURN`{.docutils .literal .notranslate}]{.pre}     Cycles   Number of atomic return cycles in LDS
  [`SQ_LDS_BANK_CONFLICT`{.docutils .literal .notranslate}]{.pre}     Cycles   Number of cycles LDS is stalled by bank conflicts
  [`SQ_LDS_ADDR_CONFLICT`{.docutils .literal .notranslate}]{.pre}     Cycles   Number of cycles LDS is stalled by address conflicts
  [`SQ_LDS_UNALIGNED_STALL`{.docutils .literal .notranslate}]{.pre}   Cycles   Number of cycles LDS is stalled processing flat unaligned load or store operations
  [`SQ_LDS_MEM_VIOLATIONS`{.docutils .literal .notranslate}]{.pre}    Count    Number of threads that have a memory violation in the LDS
  [`SQ_LDS_IDX_ACTIVE`{.docutils .literal .notranslate}]{.pre}        Cycles   Number of cycles LDS is used for indexed operations
:::
::::

:::: {#miscellaneous-counters .section}
#### Miscellaneous counters[\#](#miscellaneous-counters "Link to this heading"){.headerlink}

::: pst-scrollable-table-container
  Hardware counter                                       Unit      Definition
  ------------------------------------------------------ --------- -----------------------------------------------------------------
  [`SQ_IFETCH`{.docutils .literal .notranslate}]{.pre}   Count     Number of instruction fetch requests from L1i, in 32-byte width
  [`SQ_ITEMS`{.docutils .literal .notranslate}]{.pre}    Threads   Number of valid items per wave
:::
::::
::::::::::::::::::

:::: {#l1-instruction-cache-l1i-and-scalar-l1-data-cache-l1d-counters .section}
[]{#l1i-and-sl1d-cache-counters}

### L1 instruction cache (L1i) and scalar L1 data cache (L1d) counters[\#](#l1-instruction-cache-l1i-and-scalar-l1-data-cache-l1d-counters "Link to this heading"){.headerlink}

::: pst-scrollable-table-container
  Hardware counter                                                           Unit     Definition
  -------------------------------------------------------------------------- -------- -------------------------------------------------------------------------------------------------------------
  [`SQC_ICACHE_REQ`{.docutils .literal .notranslate}]{.pre}                  Req      Number of L1 instruction (L1i) cache requests
  [`SQC_ICACHE_HITS`{.docutils .literal .notranslate}]{.pre}                 Count    Number of L1i cache hits
  [`SQC_ICACHE_MISSES`{.docutils .literal .notranslate}]{.pre}               Count    Number of non-duplicate L1i cache misses including uncached requests
  [`SQC_ICACHE_MISSES_DUPLICATE`{.docutils .literal .notranslate}]{.pre}     Count    Number of duplicate L1i cache misses whose previous lookup miss on the same cache line is not fulfilled yet
  [`SQC_DCACHE_REQ`{.docutils .literal .notranslate}]{.pre}                  Req      Number of scalar L1d requests
  [`SQC_DCACHE_INPUT_VALID_READYB`{.docutils .literal .notranslate}]{.pre}   Cycles   Number of cycles while sequencer input is valid but scalar L1d is not ready
  [`SQC_DCACHE_HITS`{.docutils .literal .notranslate}]{.pre}                 Count    Number of scalar L1d hits
  [`SQC_DCACHE_MISSES`{.docutils .literal .notranslate}]{.pre}               Count    Number of non-duplicate scalar L1d misses including uncached requests
  [`SQC_DCACHE_MISSES_DUPLICATE`{.docutils .literal .notranslate}]{.pre}     Count    Number of duplicate scalar L1d misses
  [`SQC_DCACHE_REQ_READ_1`{.docutils .literal .notranslate}]{.pre}           Req      Number of constant cache read requests in a single 32-bit data word
  [`SQC_DCACHE_REQ_READ_2`{.docutils .literal .notranslate}]{.pre}           Req      Number of constant cache read requests in two 32-bit data words
  [`SQC_DCACHE_REQ_READ_4`{.docutils .literal .notranslate}]{.pre}           Req      Number of constant cache read requests in four 32-bit data words
  [`SQC_DCACHE_REQ_READ_8`{.docutils .literal .notranslate}]{.pre}           Req      Number of constant cache read requests in eight 32-bit data words
  [`SQC_DCACHE_REQ_READ_16`{.docutils .literal .notranslate}]{.pre}          Req      Number of constant cache read requests in 16 32-bit data words
  [`SQC_DCACHE_ATOMIC`{.docutils .literal .notranslate}]{.pre}               Req      Number of atomic requests
  [`SQC_TC_REQ`{.docutils .literal .notranslate}]{.pre}                      Req      Number of texture cache requests that were issued by instruction and constant caches
  [`SQC_TC_INST_REQ`{.docutils .literal .notranslate}]{.pre}                 Req      Number of instruction requests to the L2 cache
  [`SQC_TC_DATA_READ_REQ`{.docutils .literal .notranslate}]{.pre}            Req      Number of data Read requests to the L2 cache
  [`SQC_TC_DATA_WRITE_REQ`{.docutils .literal .notranslate}]{.pre}           Req      Number of data write requests to the L2 cache
  [`SQC_TC_DATA_ATOMIC_REQ`{.docutils .literal .notranslate}]{.pre}          Req      Number of data atomic requests to the L2 cache
  [`SQC_TC_STALL`{.docutils .literal .notranslate}]{.pre}                    Cycles   Number of cycles while the valid requests to the L2 cache are stalled
:::
::::

::::::::::: {#vector-l1-cache-subsystem-counters .section}
[]{#id4}

### Vector L1 cache subsystem counters[\#](#vector-l1-cache-subsystem-counters "Link to this heading"){.headerlink}

The vector L1 cache subsystem counters are further classified into texture addressing unit, texture data unit, vector L1d or texture cache per pipe, and texture cache arbiter counters.

:::: {#texture-addressing-unit-counters .section}
#### Texture addressing unit counters[\#](#texture-addressing-unit-counters "Link to this heading"){.headerlink}

::: pst-scrollable-table-container
  Hardware counter                                                                 Unit     Definition                                                                              Value range for [`n`{.docutils .literal .notranslate}]{.pre}
  -------------------------------------------------------------------------------- -------- --------------------------------------------------------------------------------------- --------------------------------------------------------------
  [`TA_TA_BUSY[n]`{.docutils .literal .notranslate}]{.pre}                         Cycles   Texture addressing unit busy cycles                                                     0-15
  [`TA_TOTAL_WAVEFRONTS[n]`{.docutils .literal .notranslate}]{.pre}                Instr    Number of wavefronts processed by texture addressing unit                               0-15
  [`TA_BUFFER_WAVEFRONTS[n]`{.docutils .literal .notranslate}]{.pre}               Instr    Number of buffer wavefronts processed by texture addressing unit                        0-15
  [`TA_BUFFER_READ_WAVEFRONTS[n]`{.docutils .literal .notranslate}]{.pre}          Instr    Number of buffer read wavefronts processed by texture addressing unit                   0-15
  [`TA_BUFFER_WRITE_WAVEFRONTS[n]`{.docutils .literal .notranslate}]{.pre}         Instr    Number of buffer write wavefronts processed by texture addressing unit                  0-15
  [`TA_BUFFER_ATOMIC_WAVEFRONTS[n]`{.docutils .literal .notranslate}]{.pre}        Instr    Number of buffer atomic wavefronts processed by texture addressing unit                 0-15
  [`TA_BUFFER_TOTAL_CYCLES[n]`{.docutils .literal .notranslate}]{.pre}             Cycles   Number of buffer cycles (including read and write) issued to texture cache              0-15
  [`TA_BUFFER_COALESCED_READ_CYCLES[n]`{.docutils .literal .notranslate}]{.pre}    Cycles   Number of coalesced buffer read cycles issued to texture cache                          0-15
  [`TA_BUFFER_COALESCED_WRITE_CYCLES[n]`{.docutils .literal .notranslate}]{.pre}   Cycles   Number of coalesced buffer write cycles issued to texture cache                         0-15
  [`TA_ADDR_STALLED_BY_TC_CYCLES[n]`{.docutils .literal .notranslate}]{.pre}       Cycles   Number of cycles texture addressing unit address path is stalled by texture cache       0-15
  [`TA_DATA_STALLED_BY_TC_CYCLES[n]`{.docutils .literal .notranslate}]{.pre}       Cycles   Number of cycles texture addressing unit data path is stalled by texture cache          0-15
  [`TA_ADDR_STALLED_BY_TD_CYCLES[n]`{.docutils .literal .notranslate}]{.pre}       Cycles   Number of cycles texture addressing unit address path is stalled by texture data unit   0-15
  [`TA_FLAT_WAVEFRONTS[n]`{.docutils .literal .notranslate}]{.pre}                 Instr    Number of flat opcode wavefronts processed by texture addressing unit                   0-15
  [`TA_FLAT_READ_WAVEFRONTS[n]`{.docutils .literal .notranslate}]{.pre}            Instr    Number of flat opcode read wavefronts processed by texture addressing unit              0-15
  [`TA_FLAT_WRITE_WAVEFRONTS[n]`{.docutils .literal .notranslate}]{.pre}           Instr    Number of flat opcode write wavefronts processed by texture addressing unit             0-15
  [`TA_FLAT_ATOMIC_WAVEFRONTS[n]`{.docutils .literal .notranslate}]{.pre}          Instr    Number of flat opcode atomic wavefronts processed by texture addressing unit            0-15
:::
::::

:::: {#texture-data-unit-counters .section}
#### Texture data unit counters[\#](#texture-data-unit-counters "Link to this heading"){.headerlink}

::: pst-scrollable-table-container
  Hardware counter                                                         Unit    Definition                                                                     Value range for [`n`{.docutils .literal .notranslate}]{.pre}
  ------------------------------------------------------------------------ ------- ------------------------------------------------------------------------------ --------------------------------------------------------------
  [`TD_TD_BUSY[n]`{.docutils .literal .notranslate}]{.pre}                 Cycle   Texture data unit busy cycles while it is processing or waiting for data       0-15
  [`TD_TC_STALL[n]`{.docutils .literal .notranslate}]{.pre}                Cycle   Number of cycles texture data unit is stalled waiting for texture cache data   0-15
  [`TD_SPI_STALL[n]`{.docutils .literal .notranslate}]{.pre}               Cycle   Number of cycles texture data unit is stalled by shader processor input        0-15
  [`TD_LOAD_WAVEFRONT[n]`{.docutils .literal .notranslate}]{.pre}          Instr   Number of wavefront instructions (read, write, atomic)                         0-15
  [`TD_STORE_WAVEFRONT[n]`{.docutils .literal .notranslate}]{.pre}         Instr   Number of write wavefront instructions                                         0-15
  [`TD_ATOMIC_WAVEFRONT[n]`{.docutils .literal .notranslate}]{.pre}        Instr   Number of atomic wavefront instructions                                        0-15
  [`TD_COALESCABLE_WAVEFRONT[n]`{.docutils .literal .notranslate}]{.pre}   Instr   Number of coalescable wavefronts according to texture addressing unit          0-15
:::
::::

:::: {#texture-cache-per-pipe-counters .section}
#### Texture cache per pipe counters[\#](#texture-cache-per-pipe-counters "Link to this heading"){.headerlink}

::: pst-scrollable-table-container
  Hardware counter                                                                    Unit     Definition                                                                                                                                  Value range for [`n`{.docutils .literal .notranslate}]{.pre}
  ----------------------------------------------------------------------------------- -------- ------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------
  [`TCP_GATE_EN1[n]`{.docutils .literal .notranslate}]{.pre}                          Cycles   Number of cycles vector L1d interface clocks are turned on                                                                                  0-15
  [`TCP_GATE_EN2[n]`{.docutils .literal .notranslate}]{.pre}                          Cycles   Number of cycles vector L1d core clocks are turned on                                                                                       0-15
  [`TCP_TD_TCP_STALL_CYCLES[n]`{.docutils .literal .notranslate}]{.pre}               Cycles   Number of cycles texture data unit stalls vector L1d                                                                                        0-15
  [`TCP_TCR_TCP_STALL_CYCLES[n]`{.docutils .literal .notranslate}]{.pre}              Cycles   Number of cycles texture cache router stalls vector L1d                                                                                     0-15
  [`TCP_READ_TAGCONFLICT_STALL_CYCLES[n]`{.docutils .literal .notranslate}]{.pre}     Cycles   Number of cycles tag RAM conflict stalls on a read                                                                                          0-15
  [`TCP_WRITE_TAGCONFLICT_STALL_CYCLES[n]`{.docutils .literal .notranslate}]{.pre}    Cycles   Number of cycles tag RAM conflict stalls on a write                                                                                         0-15
  [`TCP_ATOMIC_TAGCONFLICT_STALL_CYCLES[n]`{.docutils .literal .notranslate}]{.pre}   Cycles   Number of cycles tag RAM conflict stalls on an atomic                                                                                       0-15
  [`TCP_PENDING_STALL_CYCLES[n]`{.docutils .literal .notranslate}]{.pre}              Cycles   Number of cycles vector L1d is stalled due to data pending from L2 Cache                                                                    0-15
  [`TCP_TCP_TA_DATA_STALL_CYCLES`{.docutils .literal .notranslate}]{.pre}             Cycles   Number of cycles texture cache per pipe stalls texture addressing unit data interface                                                       NA
  [`TCP_TA_TCP_STATE_READ[n]`{.docutils .literal .notranslate}]{.pre}                 Req      Number of state reads                                                                                                                       0-15
  [`TCP_VOLATILE[n]`{.docutils .literal .notranslate}]{.pre}                          Req      Number of L1 volatile pixels or buffers from texture addressing unit                                                                        0-15
  [`TCP_TOTAL_ACCESSES[n]`{.docutils .literal .notranslate}]{.pre}                    Req      Number of vector L1d accesses. Equals [`` TCP_PERF_SEL_TOTAL_READ`+`TCP_PERF_SEL_TOTAL_NONREAD ``{.docutils .literal .notranslate}]{.pre}   0-15
  [`TCP_TOTAL_READ[n]`{.docutils .literal .notranslate}]{.pre}                        Req      Number of vector L1d read accesses                                                                                                          0-15
  [`TCP_TOTAL_WRITE[n]`{.docutils .literal .notranslate}]{.pre}                       Req      Number of vector L1d write accesses                                                                                                         0-15
  [`TCP_TOTAL_ATOMIC_WITH_RET[n]`{.docutils .literal .notranslate}]{.pre}             Req      Number of vector L1d atomic requests with return                                                                                            0-15
  [`TCP_TOTAL_ATOMIC_WITHOUT_RET[n]`{.docutils .literal .notranslate}]{.pre}          Req      Number of vector L1d atomic without return                                                                                                  0-15
  [`TCP_TOTAL_WRITEBACK_INVALIDATES[n]`{.docutils .literal .notranslate}]{.pre}       Count    Total number of vector L1d writebacks and invalidates                                                                                       0-15
  [`TCP_UTCL1_REQUEST[n]`{.docutils .literal .notranslate}]{.pre}                     Req      Number of address translation requests to unified translation cache (L1)                                                                    0-15
  [`TCP_UTCL1_TRANSLATION_HIT[n]`{.docutils .literal .notranslate}]{.pre}             Req      Number of unified translation cache (L1) translation hits                                                                                   0-15
  [`TCP_UTCL1_TRANSLATION_MISS[n]`{.docutils .literal .notranslate}]{.pre}            Req      Number of unified translation cache (L1) translation misses                                                                                 0-15
  [`TCP_UTCL1_PERMISSION_MISS[n]`{.docutils .literal .notranslate}]{.pre}             Req      Number of unified translation cache (L1) permission misses                                                                                  0-15
  [`TCP_TOTAL_CACHE_ACCESSES[n]`{.docutils .literal .notranslate}]{.pre}              Req      Number of vector L1d cache accesses including hits and misses                                                                               0-15
  [`TCP_TCP_LATENCY[n]`{.docutils .literal .notranslate}]{.pre}                       Cycles   **MI200 Series only** Accumulated wave access latency to vL1D over all wavefronts                                                           0-15
  [`TCP_TCC_READ_REQ_LATENCY[n]`{.docutils .literal .notranslate}]{.pre}              Cycles   **MI200 Series only** Total vL1D to L2 request latency over all wavefronts for reads and atomics with return                                0-15
  [`TCP_TCC_WRITE_REQ_LATENCY[n]`{.docutils .literal .notranslate}]{.pre}             Cycles   **MI200 Series only** Total vL1D to L2 request latency over all wavefronts for writes and atomics without return                            0-15
  [`TCP_TCC_READ_REQ[n]`{.docutils .literal .notranslate}]{.pre}                      Req      Number of read requests to L2 cache                                                                                                         0-15
  [`TCP_TCC_WRITE_REQ[n]`{.docutils .literal .notranslate}]{.pre}                     Req      Number of write requests to L2 cache                                                                                                        0-15
  [`TCP_TCC_ATOMIC_WITH_RET_REQ[n]`{.docutils .literal .notranslate}]{.pre}           Req      Number of atomic requests to L2 cache with return                                                                                           0-15
  [`TCP_TCC_ATOMIC_WITHOUT_RET_REQ[n]`{.docutils .literal .notranslate}]{.pre}        Req      Number of atomic requests to L2 cache without return                                                                                        0-15
  [`TCP_TCC_NC_READ_REQ[n]`{.docutils .literal .notranslate}]{.pre}                   Req      Number of non-coherently cached read requests to L2 cache                                                                                   0-15
  [`TCP_TCC_UC_READ_REQ[n]`{.docutils .literal .notranslate}]{.pre}                   Req      Number of uncached read requests to L2 cache                                                                                                0-15
  [`TCP_TCC_CC_READ_REQ[n]`{.docutils .literal .notranslate}]{.pre}                   Req      Number of coherently cached read requests to L2 cache                                                                                       0-15
  [`TCP_TCC_RW_READ_REQ[n]`{.docutils .literal .notranslate}]{.pre}                   Req      Number of coherently cached with write read requests to L2 cache                                                                            0-15
  [`TCP_TCC_NC_WRITE_REQ[n]`{.docutils .literal .notranslate}]{.pre}                  Req      Number of non-coherently cached write requests to L2 cache                                                                                  0-15
  [`TCP_TCC_UC_WRITE_REQ[n]`{.docutils .literal .notranslate}]{.pre}                  Req      Number of uncached write requests to L2 cache                                                                                               0-15
  [`TCP_TCC_CC_WRITE_REQ[n]`{.docutils .literal .notranslate}]{.pre}                  Req      Number of coherently cached write requests to L2 cache                                                                                      0-15
  [`TCP_TCC_RW_WRITE_REQ[n]`{.docutils .literal .notranslate}]{.pre}                  Req      Number of coherently cached with write write requests to L2 cache                                                                           0-15
  [`TCP_TCC_NC_ATOMIC_REQ[n]`{.docutils .literal .notranslate}]{.pre}                 Req      Number of non-coherently cached atomic requests to L2 cache                                                                                 0-15
  [`TCP_TCC_UC_ATOMIC_REQ[n]`{.docutils .literal .notranslate}]{.pre}                 Req      Number of uncached atomic requests to L2 cache                                                                                              0-15
  [`TCP_TCC_CC_ATOMIC_REQ[n]`{.docutils .literal .notranslate}]{.pre}                 Req      Number of coherently cached atomic requests to L2 cache                                                                                     0-15
  [`TCP_TCC_RW_ATOMIC_REQ[n]`{.docutils .literal .notranslate}]{.pre}                 Req      Number of coherently cached with write atomic requests to L2 cache                                                                          0-15
:::

Note that:

- [`TCP_TOTAL_READ[n]`{.docutils .literal .notranslate}]{.pre} = [`TCP_PERF_SEL_TOTAL_HIT_LRU_READ`{.docutils .literal .notranslate}]{.pre} + [`TCP_PERF_SEL_TOTAL_MISS_LRU_READ`{.docutils .literal .notranslate}]{.pre} + [`TCP_PERF_SEL_TOTAL_MISS_EVICT_READ`{.docutils .literal .notranslate}]{.pre}

- [`TCP_TOTAL_WRITE[n]`{.docutils .literal .notranslate}]{.pre} = [``` TCP_PERF_SEL_TOTAL_MISS_LRU_WRITE``+ ```{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[``` ``TCP_PERF_SEL_TOTAL_MISS_EVICT_WRITE ```{.docutils .literal .notranslate}]{.pre}

- [`TCP_TOTAL_WRITEBACK_INVALIDATES[n]`{.docutils .literal .notranslate}]{.pre} = [``` TCP_PERF_SEL_TOTAL_WBINVL1``+ ```{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[``` ``TCP_PERF_SEL_TOTAL_WBINVL1_VOL``+ ```{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[``` ``TCP_PERF_SEL_CP_TCP_INVALIDATE``+ ```{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[``` ``TCP_PERF_SEL_SQ_TCP_INVALIDATE_VOL ```{.docutils .literal .notranslate}]{.pre}
::::

:::: {#texture-cache-arbiter-counters .section}
#### Texture cache arbiter counters[\#](#texture-cache-arbiter-counters "Link to this heading"){.headerlink}

::: pst-scrollable-table-container
  Hardware counter                                          Unit     Definition                                                     Value range for [`n`{.docutils .literal .notranslate}]{.pre}
  --------------------------------------------------------- -------- -------------------------------------------------------------- --------------------------------------------------------------
  [`TCA_CYCLE[n]`{.docutils .literal .notranslate}]{.pre}   Cycles   Number of texture cache arbiter cycles                         0-31
  [`TCA_BUSY[n]`{.docutils .literal .notranslate}]{.pre}    Cycles   Number of cycles texture cache arbiter has a pending request   0-31
:::
::::
:::::::::::

:::::::: {#l2-cache-access-counters .section}
[]{#id5}

### L2 cache access counters[\#](#l2-cache-access-counters "Link to this heading"){.headerlink}

L2 cache is also known as texture cache per channel.

::::::: {.sd-tab-set .docutils}
MI300 hardware counter

:::: {.sd-tab-content .docutils}
::: pst-scrollable-table-container
  Hardware counter                                                                Unit     Definition                                                                                                                                                                                                                                                           Value range for [`n`{.docutils .literal .notranslate}]{.pre}
  ------------------------------------------------------------------------------- -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------
  [`TCC_CYCLE[n]`{.docutils .literal .notranslate}]{.pre}                         Cycles   Number of L2 cache free-running clocks                                                                                                                                                                                                                               0-31
  [`TCC_BUSY[n]`{.docutils .literal .notranslate}]{.pre}                          Cycles   Number of L2 cache busy cycles                                                                                                                                                                                                                                       0-31
  [`TCC_REQ[n]`{.docutils .literal .notranslate}]{.pre}                           Req      Number of L2 cache requests of all types (measured at the tag block)                                                                                                                                                                                                 0-31
  [`TCC_STREAMING_REQ[n]`{.docutils .literal .notranslate}]{.pre}                 Req      Number of L2 cache streaming requests (measured at the tag block)                                                                                                                                                                                                    0-31
  [`TCC_NC_REQ[n]`{.docutils .literal .notranslate}]{.pre}                        Req      Number of non-coherently cached requests (measured at the tag block)                                                                                                                                                                                                 0-31
  [`TCC_UC_REQ[n]`{.docutils .literal .notranslate}]{.pre}                        Req      Number of uncached requests. This is measured at the tag block                                                                                                                                                                                                       0-31
  [`TCC_CC_REQ[n]`{.docutils .literal .notranslate}]{.pre}                        Req      Number of coherently cached requests. This is measured at the tag block                                                                                                                                                                                              0-31
  [`TCC_RW_REQ[n]`{.docutils .literal .notranslate}]{.pre}                        Req      Number of coherently cached with write requests. This is measured at the tag block                                                                                                                                                                                   0-31
  [`TCC_PROBE[n]`{.docutils .literal .notranslate}]{.pre}                         Req      Number of probe requests                                                                                                                                                                                                                                             0-31
  [`TCC_PROBE_ALL[n]`{.docutils .literal .notranslate}]{.pre}                     Req      Number of external probe requests with [`EA_TCC_preq_all`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`==`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`1`{.docutils .literal .notranslate}]{.pre}   0-31
  [`TCC_READ[n]`{.docutils .literal .notranslate}]{.pre}                          Req      Number of L2 cache read requests (includes compressed reads but not metadata reads)                                                                                                                                                                                  0-31
  [`TCC_WRITE[n]`{.docutils .literal .notranslate}]{.pre}                         Req      Number of L2 cache write requests                                                                                                                                                                                                                                    0-31
  [`TCC_ATOMIC[n]`{.docutils .literal .notranslate}]{.pre}                        Req      Number of L2 cache atomic requests of all types                                                                                                                                                                                                                      0-31
  [`TCC_HIT[n]`{.docutils .literal .notranslate}]{.pre}                           Req      Number of L2 cache hits                                                                                                                                                                                                                                              0-31
  [`TCC_MISS[n]`{.docutils .literal .notranslate}]{.pre}                          Req      Number of L2 cache misses                                                                                                                                                                                                                                            0-31
  [`TCC_WRITEBACK[n]`{.docutils .literal .notranslate}]{.pre}                     Req      Number of lines written back to the main memory, including writebacks of dirty lines and uncached write or atomic requests                                                                                                                                           0-31
  [`TCC_EA0_WRREQ[n]`{.docutils .literal .notranslate}]{.pre}                     Req      Number of 32-byte and 64-byte transactions going over the [`TC_EA_wrreq`{.docutils .literal .notranslate}]{.pre} interface (doesn't include probe commands)                                                                                                          0-31
  [`TCC_EA0_WRREQ_64B[n]`{.docutils .literal .notranslate}]{.pre}                 Req      Total number of 64-byte transactions (write or [`CMPSWAP`{.docutils .literal .notranslate}]{.pre}) going over the [`TC_EA_wrreq`{.docutils .literal .notranslate}]{.pre} interface                                                                                   0-31
  [`TCC_EA0_WR_UNCACHED_32B[n]`{.docutils .literal .notranslate}]{.pre}           Req      Number of 32 or 64-byte write or atomic going over the [`TC_EA_wrreq`{.docutils .literal .notranslate}]{.pre} interface due to uncached traffic                                                                                                                      0-31
  [`TCC_EA0_WRREQ_STALL[n]`{.docutils .literal .notranslate}]{.pre}               Cycles   Number of cycles a write request is stalled                                                                                                                                                                                                                          0-31
  [`TCC_EA0_WRREQ_IO_CREDIT_STALL[n]`{.docutils .literal .notranslate}]{.pre}     Cycles   Number of cycles an efficiency arbiter write request is stalled due to the interface running out of input-output (IO) credits                                                                                                                                        0-31
  [`TCC_EA0_WRREQ_GMI_CREDIT_STALL[n]`{.docutils .literal .notranslate}]{.pre}    Cycles   Number of cycles an efficiency arbiter write request is stalled due to the interface running out of GMI credits                                                                                                                                                      0-31
  [`TCC_EA0_WRREQ_DRAM_CREDIT_STALL[n]`{.docutils .literal .notranslate}]{.pre}   Cycles   Number of cycles an efficiency arbiter write request is stalled due to the interface running out of DRAM credits                                                                                                                                                     0-31
  [`TCC_TOO_MANY_EA_WRREQS_STALL[n]`{.docutils .literal .notranslate}]{.pre}      Cycles   Number of cycles the L2 cache is unable to send an efficiency arbiter write request due to it reaching its maximum capacity of pending efficiency arbiter write requests                                                                                             0-31
  [`TCC_EA0_WRREQ_LEVEL[n]`{.docutils .literal .notranslate}]{.pre}               Req      The accumulated number of efficiency arbiter write requests in flight                                                                                                                                                                                                0-31
  [`TCC_EA0_ATOMIC[n]`{.docutils .literal .notranslate}]{.pre}                    Req      Number of 32-byte or 64-byte atomic requests going over the [`TC_EA_wrreq`{.docutils .literal .notranslate}]{.pre} interface                                                                                                                                         0-31
  [`TCC_EA0_ATOMIC_LEVEL[n]`{.docutils .literal .notranslate}]{.pre}              Req      The accumulated number of efficiency arbiter atomic requests in flight                                                                                                                                                                                               0-31
  [`TCC_EA0_RDREQ[n]`{.docutils .literal .notranslate}]{.pre}                     Req      Number of 32-byte or 64-byte read requests to efficiency arbiter                                                                                                                                                                                                     0-31
  [`TCC_EA0_RDREQ_32B[n]`{.docutils .literal .notranslate}]{.pre}                 Req      Number of 32-byte read requests to efficiency arbiter                                                                                                                                                                                                                0-31
  [`TCC_EA0_RD_UNCACHED_32B[n]`{.docutils .literal .notranslate}]{.pre}           Req      Number of 32-byte efficiency arbiter reads due to uncached traffic. A 64-byte request is counted as 2                                                                                                                                                                0-31
  [`TCC_EA0_RDREQ_IO_CREDIT_STALL[n]`{.docutils .literal .notranslate}]{.pre}     Cycles   Number of cycles there is a stall due to the read request interface running out of IO credits                                                                                                                                                                        0-31
  [`TCC_EA0_RDREQ_GMI_CREDIT_STALL[n]`{.docutils .literal .notranslate}]{.pre}    Cycles   Number of cycles there is a stall due to the read request interface running out of GMI credits                                                                                                                                                                       0-31
  [`TCC_EA0_RDREQ_DRAM_CREDIT_STALL[n]`{.docutils .literal .notranslate}]{.pre}   Cycles   Number of cycles there is a stall due to the read request interface running out of DRAM credits                                                                                                                                                                      0-31
  [`TCC_EA0_RDREQ_LEVEL[n]`{.docutils .literal .notranslate}]{.pre}               Req      The accumulated number of efficiency arbiter read requests in flight                                                                                                                                                                                                 0-31
  [`TCC_EA0_RDREQ_DRAM[n]`{.docutils .literal .notranslate}]{.pre}                Req      Number of 32-byte or 64-byte efficiency arbiter read requests to High Bandwidth Memory (HBM)                                                                                                                                                                         0-31
  [`TCC_EA0_WRREQ_DRAM[n]`{.docutils .literal .notranslate}]{.pre}                Req      Number of 32-byte or 64-byte efficiency arbiter write requests to HBM                                                                                                                                                                                                0-31
  [`TCC_TAG_STALL[n]`{.docutils .literal .notranslate}]{.pre}                     Cycles   Number of cycles the normal request pipeline in the tag is stalled for any reason                                                                                                                                                                                    0-31
  [`TCC_NORMAL_WRITEBACK[n]`{.docutils .literal .notranslate}]{.pre}              Req      Number of writebacks due to requests that are not writeback requests                                                                                                                                                                                                 0-31
  [`TCC_ALL_TC_OP_WB_WRITEBACK[n]`{.docutils .literal .notranslate}]{.pre}        Req      Number of writebacks due to all [`TC_OP`{.docutils .literal .notranslate}]{.pre} writeback requests                                                                                                                                                                  0-31
  [`TCC_NORMAL_EVICT[n]`{.docutils .literal .notranslate}]{.pre}                  Req      Number of evictions due to requests that are not invalidate or probe requests                                                                                                                                                                                        0-31
  [`TCC_ALL_TC_OP_INV_EVICT[n]`{.docutils .literal .notranslate}]{.pre}           Req      Number of evictions due to all [`TC_OP`{.docutils .literal .notranslate}]{.pre} invalidate requests                                                                                                                                                                  0-31
:::
::::

MI200 hardware counter

:::: {.sd-tab-content .docutils}
::: pst-scrollable-table-container
  Hardware counter                                                               Unit     Definition                                                                                                                                                                                                                                                           Value range for [`n`{.docutils .literal .notranslate}]{.pre}
  ------------------------------------------------------------------------------ -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------
  [`TCC_CYCLE[n]`{.docutils .literal .notranslate}]{.pre}                        Cycles   Number of L2 cache free-running clocks                                                                                                                                                                                                                               0-31
  [`TCC_BUSY[n]`{.docutils .literal .notranslate}]{.pre}                         Cycles   Number of L2 cache busy cycles                                                                                                                                                                                                                                       0-31
  [`TCC_REQ[n]`{.docutils .literal .notranslate}]{.pre}                          Req      Number of L2 cache requests of all types (measured at the tag block)                                                                                                                                                                                                 0-31
  [`TCC_STREAMING_REQ[n]`{.docutils .literal .notranslate}]{.pre}                Req      Number of L2 cache streaming requests (measured at the tag block)                                                                                                                                                                                                    0-31
  [`TCC_NC_REQ[n]`{.docutils .literal .notranslate}]{.pre}                       Req      Number of non-coherently cached requests (measured at the tag block)                                                                                                                                                                                                 0-31
  [`TCC_UC_REQ[n]`{.docutils .literal .notranslate}]{.pre}                       Req      Number of uncached requests. This is measured at the tag block                                                                                                                                                                                                       0-31
  [`TCC_CC_REQ[n]`{.docutils .literal .notranslate}]{.pre}                       Req      Number of coherently cached requests. This is measured at the tag block                                                                                                                                                                                              0-31
  [`TCC_RW_REQ[n]`{.docutils .literal .notranslate}]{.pre}                       Req      Number of coherently cached with write requests. This is measured at the tag block                                                                                                                                                                                   0-31
  [`TCC_PROBE[n]`{.docutils .literal .notranslate}]{.pre}                        Req      Number of probe requests                                                                                                                                                                                                                                             0-31
  [`TCC_PROBE_ALL[n]`{.docutils .literal .notranslate}]{.pre}                    Req      Number of external probe requests with [`EA_TCC_preq_all`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`==`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`1`{.docutils .literal .notranslate}]{.pre}   0-31
  [`TCC_READ[n]`{.docutils .literal .notranslate}]{.pre}                         Req      Number of L2 cache read requests (includes compressed reads but not metadata reads)                                                                                                                                                                                  0-31
  [`TCC_WRITE[n]`{.docutils .literal .notranslate}]{.pre}                        Req      Number of L2 cache write requests                                                                                                                                                                                                                                    0-31
  [`TCC_ATOMIC[n]`{.docutils .literal .notranslate}]{.pre}                       Req      Number of L2 cache atomic requests of all types                                                                                                                                                                                                                      0-31
  [`TCC_HIT[n]`{.docutils .literal .notranslate}]{.pre}                          Req      Number of L2 cache hits                                                                                                                                                                                                                                              0-31
  [`TCC_MISS[n]`{.docutils .literal .notranslate}]{.pre}                         Req      Number of L2 cache misses                                                                                                                                                                                                                                            0-31
  [`TCC_WRITEBACK[n]`{.docutils .literal .notranslate}]{.pre}                    Req      Number of lines written back to the main memory, including writebacks of dirty lines and uncached write or atomic requests                                                                                                                                           0-31
  [`TCC_EA_WRREQ[n]`{.docutils .literal .notranslate}]{.pre}                     Req      Number of 32-byte and 64-byte transactions going over the [`TC_EA_wrreq`{.docutils .literal .notranslate}]{.pre} interface (doesn't include probe commands)                                                                                                          0-31
  [`TCC_EA_WRREQ_64B[n]`{.docutils .literal .notranslate}]{.pre}                 Req      Total number of 64-byte transactions (write or [`CMPSWAP`{.docutils .literal .notranslate}]{.pre}) going over the [`TC_EA_wrreq`{.docutils .literal .notranslate}]{.pre} interface                                                                                   0-31
  [`TCC_EA_WR_UNCACHED_32B[n]`{.docutils .literal .notranslate}]{.pre}           Req      Number of 32 write or atomic going over the [`TC_EA_wrreq`{.docutils .literal .notranslate}]{.pre} interface due to uncached traffic. A 64-byte request will be counted as 2                                                                                         0-31
  [`TCC_EA_WRREQ_STALL[n]`{.docutils .literal .notranslate}]{.pre}               Cycles   Number of cycles a write request is stalled                                                                                                                                                                                                                          0-31
  [`TCC_EA_WRREQ_IO_CREDIT_STALL[n]`{.docutils .literal .notranslate}]{.pre}     Cycles   Number of cycles an efficiency arbiter write request is stalled due to the interface running out of input-output (IO) credits                                                                                                                                        0-31
  [`TCC_EA_WRREQ_GMI_CREDIT_STALL[n]`{.docutils .literal .notranslate}]{.pre}    Cycles   Number of cycles an efficiency arbiter write request is stalled due to the interface running out of GMI credits                                                                                                                                                      0-31
  [`TCC_EA_WRREQ_DRAM_CREDIT_STALL[n]`{.docutils .literal .notranslate}]{.pre}   Cycles   Number of cycles an efficiency arbiter write request is stalled due to the interface running out of DRAM credits                                                                                                                                                     0-31
  [`TCC_TOO_MANY_EA_WRREQS_STALL[n]`{.docutils .literal .notranslate}]{.pre}     Cycles   Number of cycles the L2 cache is unable to send an efficiency arbiter write request due to it reaching its maximum capacity of pending efficiency arbiter write requests                                                                                             0-31
  [`TCC_EA_WRREQ_LEVEL[n]`{.docutils .literal .notranslate}]{.pre}               Req      The accumulated number of efficiency arbiter write requests in flight                                                                                                                                                                                                0-31
  [`TCC_EA_ATOMIC[n]`{.docutils .literal .notranslate}]{.pre}                    Req      Number of 32-byte or 64-byte atomic requests going over the [`TC_EA_wrreq`{.docutils .literal .notranslate}]{.pre} interface                                                                                                                                         0-31
  [`TCC_EA_ATOMIC_LEVEL[n]`{.docutils .literal .notranslate}]{.pre}              Req      The accumulated number of efficiency arbiter atomic requests in flight                                                                                                                                                                                               0-31
  [`TCC_EA_RDREQ[n]`{.docutils .literal .notranslate}]{.pre}                     Req      Number of 32-byte or 64-byte read requests to efficiency arbiter                                                                                                                                                                                                     0-31
  [`TCC_EA_RDREQ_32B[n]`{.docutils .literal .notranslate}]{.pre}                 Req      Number of 32-byte read requests to efficiency arbiter                                                                                                                                                                                                                0-31
  [`TCC_EA_RD_UNCACHED_32B[n]`{.docutils .literal .notranslate}]{.pre}           Req      Number of 32-byte efficiency arbiter reads due to uncached traffic. A 64-byte request is counted as 2                                                                                                                                                                0-31
  [`TCC_EA_RDREQ_IO_CREDIT_STALL[n]`{.docutils .literal .notranslate}]{.pre}     Cycles   Number of cycles there is a stall due to the read request interface running out of IO credits                                                                                                                                                                        0-31
  [`TCC_EA_RDREQ_GMI_CREDIT_STALL[n]`{.docutils .literal .notranslate}]{.pre}    Cycles   Number of cycles there is a stall due to the read request interface running out of GMI credits                                                                                                                                                                       0-31
  [`TCC_EA_RDREQ_DRAM_CREDIT_STALL[n]`{.docutils .literal .notranslate}]{.pre}   Cycles   Number of cycles there is a stall due to the read request interface running out of DRAM credits                                                                                                                                                                      0-31
  [`TCC_EA_RDREQ_LEVEL[n]`{.docutils .literal .notranslate}]{.pre}               Req      The accumulated number of efficiency arbiter read requests in flight                                                                                                                                                                                                 0-31
  [`TCC_EA_RDREQ_DRAM[n]`{.docutils .literal .notranslate}]{.pre}                Req      Number of 32-byte or 64-byte efficiency arbiter read requests to High Bandwidth Memory (HBM)                                                                                                                                                                         0-31
  [`TCC_EA_WRREQ_DRAM[n]`{.docutils .literal .notranslate}]{.pre}                Req      Number of 32-byte or 64-byte efficiency arbiter write requests to HBM                                                                                                                                                                                                0-31
  [`TCC_TAG_STALL[n]`{.docutils .literal .notranslate}]{.pre}                    Cycles   Number of cycles the normal request pipeline in the tag is stalled for any reason                                                                                                                                                                                    0-31
  [`TCC_NORMAL_WRITEBACK[n]`{.docutils .literal .notranslate}]{.pre}             Req      Number of writebacks due to requests that are not writeback requests                                                                                                                                                                                                 0-31
  [`TCC_ALL_TC_OP_WB_WRITEBACK[n]`{.docutils .literal .notranslate}]{.pre}       Req      Number of writebacks due to all [`TC_OP`{.docutils .literal .notranslate}]{.pre} writeback requests                                                                                                                                                                  0-31
  [`TCC_NORMAL_EVICT[n]`{.docutils .literal .notranslate}]{.pre}                 Req      Number of evictions due to requests that are not invalidate or probe requests                                                                                                                                                                                        0-31
  [`TCC_ALL_TC_OP_INV_EVICT[n]`{.docutils .literal .notranslate}]{.pre}          Req      Number of evictions due to all [`TC_OP`{.docutils .literal .notranslate}]{.pre} invalidate requests                                                                                                                                                                  0-31
:::
::::
:::::::

Note the following:

- [`TCC_REQ[n]`{.docutils .literal .notranslate}]{.pre} may be more than the number of requests arriving at the texture cache per channel, but it's a good indication of the total amount of work that needs to be performed.

- For [`TCC_EA0_WRREQ[n]`{.docutils .literal .notranslate}]{.pre}, atomics may travel over the same interface and are generally classified as write requests.

- CC mtypes can produce uncached requests, and those are included in [`TCC_EA0_WR_UNCACHED_32B[n]`{.docutils .literal .notranslate}]{.pre}

- [`TCC_EA0_WRREQ_LEVEL[n]`{.docutils .literal .notranslate}]{.pre} is primarily intended to measure average efficiency arbiter write latency.

  - Average write latency = [`TCC_PERF_SEL_EA0_WRREQ_LEVEL`{.docutils .literal .notranslate}]{.pre} divided by [`TCC_PERF_SEL_EA0_WRREQ`{.docutils .literal .notranslate}]{.pre}

- [`TCC_EA0_ATOMIC_LEVEL[n]`{.docutils .literal .notranslate}]{.pre} is primarily intended to measure average efficiency arbiter atomic latency

  - Average atomic latency = [`TCC_PERF_SEL_EA0_WRREQ_ATOMIC_LEVEL`{.docutils .literal .notranslate}]{.pre} divided by [`TCC_PERF_SEL_EA0_WRREQ_ATOMIC`{.docutils .literal .notranslate}]{.pre}

- [`TCC_EA0_RDREQ_LEVEL[n]`{.docutils .literal .notranslate}]{.pre} is primarily intended to measure average efficiency arbiter read latency.

  - Average read latency = [`TCC_PERF_SEL_EA0_RDREQ_LEVEL`{.docutils .literal .notranslate}]{.pre} divided by [`TCC_PERF_SEL_EA0_RDREQ`{.docutils .literal .notranslate}]{.pre}

- Stalls can occur regardless of the need for a read to be performed

- Normally, stalls are measured exactly at one point in the pipeline however in the case of [`TCC_TAG_STALL[n]`{.docutils .literal .notranslate}]{.pre}, probes can stall the pipeline at a variety of places. There is no single point that can accurately measure the total stalls
::::::::
::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::: {#mi300-and-mi200-series-derived-metrics-list .section}
## MI300 and MI200 Series derived metrics list[\#](#mi300-and-mi200-series-derived-metrics-list "Link to this heading"){.headerlink}

::: pst-scrollable-table-container
  Hardware counter                                              Definition
  ------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`ALUStalledByLDS`{.docutils .literal .notranslate}]{.pre}    Percentage of GPU time ALU units are stalled due to the LDS input queue being full or the output queue not being ready (value range: 0% (optimal) to 100%)
  [`FetchSize`{.docutils .literal .notranslate}]{.pre}          Total kilobytes fetched from the video memory; measured with all extra fetches and any cache or memory effects taken into account
  [`FlatLDSInsts`{.docutils .literal .notranslate}]{.pre}       Average number of flat instructions that read from or write to LDS, run per work item (affected by flow control)
  [`FlatVMemInsts`{.docutils .literal .notranslate}]{.pre}      Average number of flat instructions that read from or write to the video memory, run per work item (affected by flow control). Includes flat instructions that read from or write to scratch
  [`GDSInsts`{.docutils .literal .notranslate}]{.pre}           Average number of global data share read or write instructions run per work item (affected by flow control)
  [`GPUBusy`{.docutils .literal .notranslate}]{.pre}            Percentage of time GPU is busy
  [`L2CacheHit`{.docutils .literal .notranslate}]{.pre}         Percentage of fetch, write, atomic, and other instructions that hit the data in L2 cache (value range: 0% (no hit) to 100% (optimal))
  [`LDSBankConflict`{.docutils .literal .notranslate}]{.pre}    Percentage of GPU time LDS is stalled by bank conflicts (value range: 0% (optimal) to 100%)
  [`LDSInsts`{.docutils .literal .notranslate}]{.pre}           Average number of LDS read or write instructions run per work item (affected by flow control). Excludes flat instructions that read from or write to LDS.
  [`MemUnitBusy`{.docutils .literal .notranslate}]{.pre}        Percentage of GPU time the memory unit is active, which is measured with all extra fetches and writes and any cache or memory effects taken into account (value range: 0% to 100% (fetch-bound))
  [`MemUnitStalled`{.docutils .literal .notranslate}]{.pre}     Percentage of GPU time the memory unit is stalled (value range: 0% (optimal) to 100%)
  [`MemWrites32B`{.docutils .literal .notranslate}]{.pre}       Total number of effective 32B write transactions to the memory
  [`TCA_BUSY_sum`{.docutils .literal .notranslate}]{.pre}       Total number of cycles texture cache arbiter has a pending request, over all texture cache arbiter instances
  [`TCA_CYCLE_sum`{.docutils .literal .notranslate}]{.pre}      Total number of cycles over all texture cache arbiter instances
  [`SALUBusy`{.docutils .literal .notranslate}]{.pre}           Percentage of GPU time scalar ALU instructions are processed (value range: 0% to 100% (optimal))
  [`SALUInsts`{.docutils .literal .notranslate}]{.pre}          Average number of scalar ALU instructions run per work item (affected by flow control)
  [`SFetchInsts`{.docutils .literal .notranslate}]{.pre}        Average number of scalar fetch instructions from the video memory run per work item (affected by flow control)
  [`VALUBusy`{.docutils .literal .notranslate}]{.pre}           Percentage of GPU time vector ALU instructions are processed (value range: 0% to 100% (optimal))
  [`VALUInsts`{.docutils .literal .notranslate}]{.pre}          Average number of vector ALU instructions run per work item (affected by flow control)
  [`VALUUtilization`{.docutils .literal .notranslate}]{.pre}    Percentage of active vector ALU threads in a wave, where a lower number can mean either more thread divergence in a wave or that the work-group size is not a multiple of 64 (value range: 0%, 100% (optimal - no thread divergence))
  [`VFetchInsts`{.docutils .literal .notranslate}]{.pre}        Average number of vector fetch instructions from the video memory run per work-item (affected by flow control); excludes flat instructions that fetch from video memory
  [`VWriteInsts`{.docutils .literal .notranslate}]{.pre}        Average number of vector write instructions to the video memory run per work-item (affected by flow control); excludes flat instructions that write to video memory
  [`Wavefronts`{.docutils .literal .notranslate}]{.pre}         Total wavefronts
  [`WRITE_REQ_32B`{.docutils .literal .notranslate}]{.pre}      Total number of 32-byte effective memory writes
  [`WriteSize`{.docutils .literal .notranslate}]{.pre}          Total kilobytes written to the video memory; measured with all extra fetches and any cache or memory effects taken into account
  [`WriteUnitStalled`{.docutils .literal .notranslate}]{.pre}   Percentage of GPU time the write unit is stalled (value range: 0% (optimal) to 100%)
:::

You can lower [`ALUStalledByLDS`{.docutils .literal .notranslate}]{.pre} by reducing LDS bank conflicts or number of LDS accesses. You can lower [`MemUnitStalled`{.docutils .literal .notranslate}]{.pre} by reducing the number or size of fetches and writes. [`MemUnitBusy`{.docutils .literal .notranslate}]{.pre} includes the stall time ([`MemUnitStalled`{.docutils .literal .notranslate}]{.pre}).

::::: {#hardware-counters-by-and-over-all-texture-addressing-unit-instances .section}
### Hardware counters by and over all texture addressing unit instances[\#](#hardware-counters-by-and-over-all-texture-addressing-unit-instances "Link to this heading"){.headerlink}

The following table shows the hardware counters *by* all texture addressing unit instances.

::: pst-scrollable-table-container
  Hardware counter                                                                  Definition
  --------------------------------------------------------------------------------- ----------------------------------------------------------------------------------
  [`TA_BUFFER_WAVEFRONTS_sum`{.docutils .literal .notranslate}]{.pre}               Total number of buffer wavefronts processed
  [`TA_BUFFER_READ_WAVEFRONTS_sum`{.docutils .literal .notranslate}]{.pre}          Total number of buffer read wavefronts processed
  [`TA_BUFFER_WRITE_WAVEFRONTS_sum`{.docutils .literal .notranslate}]{.pre}         Total number of buffer write wavefronts processed
  [`TA_BUFFER_ATOMIC_WAVEFRONTS_sum`{.docutils .literal .notranslate}]{.pre}        Total number of buffer atomic wavefronts processed
  [`TA_BUFFER_TOTAL_CYCLES_sum`{.docutils .literal .notranslate}]{.pre}             Total number of buffer cycles (including read and write) issued to texture cache
  [`TA_BUFFER_COALESCED_READ_CYCLES_sum`{.docutils .literal .notranslate}]{.pre}    Total number of coalesced buffer read cycles issued to texture cache
  [`TA_BUFFER_COALESCED_WRITE_CYCLES_sum`{.docutils .literal .notranslate}]{.pre}   Total number of coalesced buffer write cycles issued to texture cache
  [`TA_FLAT_READ_WAVEFRONTS_sum`{.docutils .literal .notranslate}]{.pre}            Sum of flat opcode reads processed
  [`TA_FLAT_WRITE_WAVEFRONTS_sum`{.docutils .literal .notranslate}]{.pre}           Sum of flat opcode writes processed
  [`TA_FLAT_WAVEFRONTS_sum`{.docutils .literal .notranslate}]{.pre}                 Total number of flat opcode wavefronts processed
  [`TA_FLAT_ATOMIC_WAVEFRONTS_sum`{.docutils .literal .notranslate}]{.pre}          Total number of flat opcode atomic wavefronts processed
  [`TA_TOTAL_WAVEFRONTS_sum`{.docutils .literal .notranslate}]{.pre}                Total number of wavefronts processed
:::

The following table shows the hardware counters *over* all texture addressing unit instances.

::: pst-scrollable-table-container
  Hardware counter                                                              Definition
  ----------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------
  [`TA_ADDR_STALLED_BY_TC_CYCLES_sum`{.docutils .literal .notranslate}]{.pre}   Total number of cycles texture addressing unit address path is stalled by texture cache
  [`TA_ADDR_STALLED_BY_TD_CYCLES_sum`{.docutils .literal .notranslate}]{.pre}   Total number of cycles texture addressing unit address path is stalled by texture data unit
  [`TA_BUSY_avr`{.docutils .literal .notranslate}]{.pre}                        Average number of busy cycles
  [`TA_BUSY_max`{.docutils .literal .notranslate}]{.pre}                        Maximum number of texture addressing unit busy cycles
  [`TA_BUSY_min`{.docutils .literal .notranslate}]{.pre}                        Minimum number of texture addressing unit busy cycles
  [`TA_DATA_STALLED_BY_TC_CYCLES_sum`{.docutils .literal .notranslate}]{.pre}   Total number of cycles texture addressing unit data path is stalled by texture cache
  [`TA_TA_BUSY_sum`{.docutils .literal .notranslate}]{.pre}                     Total number of texture addressing unit busy cycles
:::
:::::

:::: {#hardware-counters-over-all-texture-cache-per-channel-instances .section}
### Hardware counters over all texture cache per channel instances[\#](#hardware-counters-over-all-texture-cache-per-channel-instances "Link to this heading"){.headerlink}

::: pst-scrollable-table-container
  Hardware counter                                                                 Definition
  -------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`TCC_ALL_TC_OP_WB_WRITEBACK_sum`{.docutils .literal .notranslate}]{.pre}        Total number of writebacks due to all [`TC_OP`{.docutils .literal .notranslate}]{.pre} writeback requests.
  [`TCC_ALL_TC_OP_INV_EVICT_sum`{.docutils .literal .notranslate}]{.pre}           Total number of evictions due to all [`TC_OP`{.docutils .literal .notranslate}]{.pre} invalidate requests.
  [`TCC_ATOMIC_sum`{.docutils .literal .notranslate}]{.pre}                        Total number of L2 cache atomic requests of all types.
  [`TCC_BUSY_avr`{.docutils .literal .notranslate}]{.pre}                          Average number of L2 cache busy cycles.
  [`TCC_BUSY_sum`{.docutils .literal .notranslate}]{.pre}                          Total number of L2 cache busy cycles.
  [`TCC_CC_REQ_sum`{.docutils .literal .notranslate}]{.pre}                        Total number of coherently cached requests.
  [`TCC_CYCLE_sum`{.docutils .literal .notranslate}]{.pre}                         Total number of L2 cache free running clocks.
  [`TCC_EA0_WRREQ_sum`{.docutils .literal .notranslate}]{.pre}                     Total number of 32-byte and 64-byte transactions going over the [`TC_EA0_wrreq`{.docutils .literal .notranslate}]{.pre} interface. Atomics may travel over the same interface and are generally classified as write requests. This does not include probe commands.
  [`TCC_EA0_WRREQ_64B_sum`{.docutils .literal .notranslate}]{.pre}                 Total number of 64-byte transactions (write or CMPSWAP) going over the [`TC_EA0_wrreq`{.docutils .literal .notranslate}]{.pre} interface.
  [`TCC_EA0_WR_UNCACHED_32B_sum`{.docutils .literal .notranslate}]{.pre}           Total Number of 32-byte write or atomic going over the [`TC_EA0_wrreq`{.docutils .literal .notranslate}]{.pre} interface due to uncached traffic. Note that coherently cached mtypes can produce uncached requests, and those are included in this. A 64-byte request is counted as 2.
  [`TCC_EA0_WRREQ_STALL_sum`{.docutils .literal .notranslate}]{.pre}               Total Number of cycles a write request is stalled, over all instances.
  [`TCC_EA0_WRREQ_IO_CREDIT_STALL_sum`{.docutils .literal .notranslate}]{.pre}     Total number of cycles an efficiency arbiter write request is stalled due to the interface running out of IO credits, over all instances.
  [`TCC_EA0_WRREQ_GMI_CREDIT_STALL_sum`{.docutils .literal .notranslate}]{.pre}    Total number of cycles an efficiency arbiter write request is stalled due to the interface running out of GMI credits, over all instances.
  [`TCC_EA0_WRREQ_DRAM_CREDIT_STALL_sum`{.docutils .literal .notranslate}]{.pre}   Total number of cycles an efficiency arbiter write request is stalled due to the interface running out of DRAM credits, over all instances.
  [`TCC_EA0_WRREQ_LEVEL_sum`{.docutils .literal .notranslate}]{.pre}               Total number of efficiency arbiter write requests in flight.
  [`TCC_EA0_RDREQ_LEVEL_sum`{.docutils .literal .notranslate}]{.pre}               Total number of efficiency arbiter read requests in flight.
  [`TCC_EA0_ATOMIC_sum`{.docutils .literal .notranslate}]{.pre}                    Total Number of 32-byte or 64-byte atomic requests going over the [`TC_EA0_wrreq`{.docutils .literal .notranslate}]{.pre} interface.
  [`TCC_EA0_ATOMIC_LEVEL_sum`{.docutils .literal .notranslate}]{.pre}              Total number of efficiency arbiter atomic requests in flight.
  [`TCC_EA0_RDREQ_sum`{.docutils .literal .notranslate}]{.pre}                     Total number of 32-byte or 64-byte read requests to efficiency arbiter.
  [`TCC_EA0_RDREQ_32B_sum`{.docutils .literal .notranslate}]{.pre}                 Total number of 32-byte read requests to efficiency arbiter.
  [`TCC_EA0_RD_UNCACHED_32B_sum`{.docutils .literal .notranslate}]{.pre}           Total number of 32-byte efficiency arbiter reads due to uncached traffic.
  [`TCC_EA0_RDREQ_IO_CREDIT_STALL_sum`{.docutils .literal .notranslate}]{.pre}     Total number of cycles there is a stall due to the read request interface running out of IO credits.
  [`TCC_EA0_RDREQ_GMI_CREDIT_STALL_sum`{.docutils .literal .notranslate}]{.pre}    Total number of cycles there is a stall due to the read request interface running out of GMI credits.
  [`TCC_EA0_RDREQ_DRAM_CREDIT_STALL_sum`{.docutils .literal .notranslate}]{.pre}   Total number of cycles there is a stall due to the read request interface running out of DRAM credits.
  [`TCC_EA0_RDREQ_DRAM_sum`{.docutils .literal .notranslate}]{.pre}                Total number of 32-byte or 64-byte efficiency arbiter read requests to HBM.
  [`TCC_EA0_WRREQ_DRAM_sum`{.docutils .literal .notranslate}]{.pre}                Total number of 32-byte or 64-byte efficiency arbiter write requests to HBM.
  [`TCC_HIT_sum`{.docutils .literal .notranslate}]{.pre}                           Total number of L2 cache hits.
  [`TCC_MISS_sum`{.docutils .literal .notranslate}]{.pre}                          Total number of L2 cache misses.
  [`TCC_NC_REQ_sum`{.docutils .literal .notranslate}]{.pre}                        Total number of non-coherently cached requests.
  [`TCC_NORMAL_WRITEBACK_sum`{.docutils .literal .notranslate}]{.pre}              Total number of writebacks due to requests that are not writeback requests.
  [`TCC_NORMAL_EVICT_sum`{.docutils .literal .notranslate}]{.pre}                  Total number of evictions due to requests that are not invalidate or probe requests.
  [`TCC_PROBE_sum`{.docutils .literal .notranslate}]{.pre}                         Total number of probe requests.
  [`TCC_PROBE_ALL_sum`{.docutils .literal .notranslate}]{.pre}                     Total number of external probe requests with [`EA0_TCC_preq_all`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`==`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`1`{.docutils .literal .notranslate}]{.pre}.
  [`TCC_READ_sum`{.docutils .literal .notranslate}]{.pre}                          Total number of L2 cache read requests (including compressed reads but not metadata reads).
  [`TCC_REQ_sum`{.docutils .literal .notranslate}]{.pre}                           Total number of all types of L2 cache requests.
  [`TCC_RW_REQ_sum`{.docutils .literal .notranslate}]{.pre}                        Total number of coherently cached with write requests.
  [`TCC_STREAMING_REQ_sum`{.docutils .literal .notranslate}]{.pre}                 Total number of L2 cache streaming requests.
  [`TCC_TAG_STALL_sum`{.docutils .literal .notranslate}]{.pre}                     Total number of cycles the normal request pipeline in the tag is stalled for any reason.
  [`TCC_TOO_MANY_EA0_WRREQS_STALL_sum`{.docutils .literal .notranslate}]{.pre}     Total number of cycles L2 cache is unable to send an efficiency arbiter write request due to it reaching its maximum capacity of pending efficiency arbiter write requests.
  [`TCC_UC_REQ_sum`{.docutils .literal .notranslate}]{.pre}                        Total number of uncached requests.
  [`TCC_WRITE_sum`{.docutils .literal .notranslate}]{.pre}                         Total number of L2 cache write requests.
  [`TCC_WRITEBACK_sum`{.docutils .literal .notranslate}]{.pre}                     Total number of lines written back to the main memory including writebacks of dirty lines and uncached write or atomic requests.
  [`TCC_WRREQ_STALL_max`{.docutils .literal .notranslate}]{.pre}                   Maximum number of cycles a write request is stalled.
:::
::::

:::::: {#hardware-counters-by-for-or-over-all-texture-cache-per-pipe-instances .section}
### Hardware counters by, for, or over all texture cache per pipe instances[\#](#hardware-counters-by-for-or-over-all-texture-cache-per-pipe-instances "Link to this heading"){.headerlink}

The following table shows the hardware counters *by* all texture cache per pipe instances.

::: pst-scrollable-table-container
  Hardware counter                                                            Definition
  --------------------------------------------------------------------------- --------------------------------------------------------------------------------
  [`TCP_TA_TCP_STATE_READ_sum`{.docutils .literal .notranslate}]{.pre}        Total number of state reads by ATCPPI
  [`TCP_TOTAL_CACHE_ACCESSES_sum`{.docutils .literal .notranslate}]{.pre}     Total number of vector L1d accesses (including hits and misses)
  [`TCP_UTCL1_PERMISSION_MISS_sum`{.docutils .literal .notranslate}]{.pre}    Total number of unified translation cache (L1) permission misses
  [`TCP_UTCL1_REQUEST_sum`{.docutils .literal .notranslate}]{.pre}            Total number of address translation requests to unified translation cache (L1)
  [`TCP_UTCL1_TRANSLATION_MISS_sum`{.docutils .literal .notranslate}]{.pre}   Total number of unified translation cache (L1) translation misses
  [`TCP_UTCL1_TRANSLATION_HIT_sum`{.docutils .literal .notranslate}]{.pre}    Total number of unified translation cache (L1) translation hits
:::

The following table shows the hardware counters *for* all texture cache per pipe instances.

::: pst-scrollable-table-container
  Hardware counter                                                           Definition
  -------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------
  [`TCP_TCC_READ_REQ_LATENCY_sum`{.docutils .literal .notranslate}]{.pre}    Total vector L1d to L2 request latency over all wavefronts for reads and atomics with return
  [`TCP_TCC_WRITE_REQ_LATENCY_sum`{.docutils .literal .notranslate}]{.pre}   Total vector L1d to L2 request latency over all wavefronts for writes and atomics without return
  [`TCP_TCP_LATENCY_sum`{.docutils .literal .notranslate}]{.pre}             Total wave access latency to vector L1d over all wavefronts
:::

The following table shows the hardware counters *over* all texture cache per pipe instances.

::: pst-scrollable-table-container
  Hardware counter                                                                     Definition
  ------------------------------------------------------------------------------------ --------------------------------------------------------------------------------------
  [`TCP_ATOMIC_TAGCONFLICT_STALL_CYCLES_sum`{.docutils .literal .notranslate}]{.pre}   Total number of cycles tag RAM conflict stalls on an atomic
  [`TCP_GATE_EN1_sum`{.docutils .literal .notranslate}]{.pre}                          Total number of cycles vector L1d interface clocks are turned on
  [`TCP_GATE_EN2_sum`{.docutils .literal .notranslate}]{.pre}                          Total number of cycles vector L1d core clocks are turned on
  [`TCP_PENDING_STALL_CYCLES_sum`{.docutils .literal .notranslate}]{.pre}              Total number of cycles vector L1d cache is stalled due to data pending from L2 Cache
  [`TCP_READ_TAGCONFLICT_STALL_CYCLES_sum`{.docutils .literal .notranslate}]{.pre}     Total number of cycles tag RAM conflict stalls on a read
  [`TCP_TCC_ATOMIC_WITH_RET_REQ_sum`{.docutils .literal .notranslate}]{.pre}           Total number of atomic requests to L2 cache with return
  [`TCP_TCC_ATOMIC_WITHOUT_RET_REQ_sum`{.docutils .literal .notranslate}]{.pre}        Total number of atomic requests to L2 cache without return
  [`TCP_TCC_CC_READ_REQ_sum`{.docutils .literal .notranslate}]{.pre}                   Total number of coherently cached read requests to L2 cache
  [`TCP_TCC_CC_WRITE_REQ_sum`{.docutils .literal .notranslate}]{.pre}                  Total number of coherently cached write requests to L2 cache
  [`TCP_TCC_CC_ATOMIC_REQ_sum`{.docutils .literal .notranslate}]{.pre}                 Total number of coherently cached atomic requests to L2 cache
  [`TCP_TCC_NC_READ_REQ_sum`{.docutils .literal .notranslate}]{.pre}                   Total number of non-coherently cached read requests to L2 cache
  [`TCP_TCC_NC_WRITE_REQ_sum`{.docutils .literal .notranslate}]{.pre}                  Total number of non-coherently cached write requests to L2 cache
  [`TCP_TCC_NC_ATOMIC_REQ_sum`{.docutils .literal .notranslate}]{.pre}                 Total number of non-coherently cached atomic requests to L2 cache
  [`TCP_TCC_READ_REQ_sum`{.docutils .literal .notranslate}]{.pre}                      Total number of read requests to L2 cache
  [`TCP_TCC_RW_READ_REQ_sum`{.docutils .literal .notranslate}]{.pre}                   Total number of coherently cached with write read requests to L2 cache
  [`TCP_TCC_RW_WRITE_REQ_sum`{.docutils .literal .notranslate}]{.pre}                  Total number of coherently cached with write write requests to L2 cache
  [`TCP_TCC_RW_ATOMIC_REQ_sum`{.docutils .literal .notranslate}]{.pre}                 Total number of coherently cached with write atomic requests to L2 cache
  [`TCP_TCC_UC_READ_REQ_sum`{.docutils .literal .notranslate}]{.pre}                   Total number of uncached read requests to L2 cache
  [`TCP_TCC_UC_WRITE_REQ_sum`{.docutils .literal .notranslate}]{.pre}                  Total number of uncached write requests to L2 cache
  [`TCP_TCC_UC_ATOMIC_REQ_sum`{.docutils .literal .notranslate}]{.pre}                 Total number of uncached atomic requests to L2 cache
  [`TCP_TCC_WRITE_REQ_sum`{.docutils .literal .notranslate}]{.pre}                     Total number of write requests to L2 cache
  [`TCP_TCR_TCP_STALL_CYCLES_sum`{.docutils .literal .notranslate}]{.pre}              Total number of cycles texture cache router stalls vector L1d
  [`TCP_TD_TCP_STALL_CYCLES_sum`{.docutils .literal .notranslate}]{.pre}               Total number of cycles texture data unit stalls vector L1d
  [`TCP_TOTAL_ACCESSES_sum`{.docutils .literal .notranslate}]{.pre}                    Total number of vector L1d accesses
  [`TCP_TOTAL_READ_sum`{.docutils .literal .notranslate}]{.pre}                        Total number of vector L1d read accesses
  [`TCP_TOTAL_WRITE_sum`{.docutils .literal .notranslate}]{.pre}                       Total number of vector L1d write accesses
  [`TCP_TOTAL_ATOMIC_WITH_RET_sum`{.docutils .literal .notranslate}]{.pre}             Total number of vector L1d atomic requests with return
  [`TCP_TOTAL_ATOMIC_WITHOUT_RET_sum`{.docutils .literal .notranslate}]{.pre}          Total number of vector L1d atomic requests without return
  [`TCP_TOTAL_WRITEBACK_INVALIDATES_sum`{.docutils .literal .notranslate}]{.pre}       Total number of vector L1d writebacks and invalidates
  [`TCP_VOLATILE_sum`{.docutils .literal .notranslate}]{.pre}                          Total number of L1 volatile pixels or buffers from texture addressing unit
  [`TCP_WRITE_TAGCONFLICT_STALL_CYCLES_sum`{.docutils .literal .notranslate}]{.pre}    Total number of cycles tag RAM conflict stalls on a write
:::
::::::

:::: {#hardware-counter-over-all-texture-data-unit-instances .section}
### Hardware counter over all texture data unit instances[\#](#hardware-counter-over-all-texture-data-unit-instances "Link to this heading"){.headerlink}

::: pst-scrollable-table-container
  Hardware counter                                                          Definition
  ------------------------------------------------------------------------- ------------------------------------------------------------------------------------------
  [`TD_ATOMIC_WAVEFRONT_sum`{.docutils .literal .notranslate}]{.pre}        Total number of atomic wavefront instructions
  [`TD_COALESCABLE_WAVEFRONT_sum`{.docutils .literal .notranslate}]{.pre}   Total number of coalescable wavefronts according to texture addressing unit
  [`TD_LOAD_WAVEFRONT_sum`{.docutils .literal .notranslate}]{.pre}          Total number of wavefront instructions (read, write, atomic)
  [`TD_SPI_STALL_sum`{.docutils .literal .notranslate}]{.pre}               Total number of cycles texture data unit is stalled by shader processor input
  [`TD_STORE_WAVEFRONT_sum`{.docutils .literal .notranslate}]{.pre}         Total number of write wavefront instructions
  [`TD_TC_STALL_sum`{.docutils .literal .notranslate}]{.pre}                Total number of cycles texture data unit is stalled waiting for texture cache data
  [`TD_TD_BUSY_sum`{.docutils .literal .notranslate}]{.pre}                 Total number of texture data unit busy cycles while it is processing or waiting for data
:::
::::
:::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::: prev-next-area
[](mi300.html "previous page"){.left-prev}

::: prev-next-info
previous

AMD Instinct™ MI300 Series microarchitecture
:::

[](mi350-performance-counters.html "next page"){.right-next}

::: prev-next-info
next

MI350 Series performance counters
:::
:::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::: {.bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {.page-toc .tocsection .onthispage}
Contents
:::

- [MI300 and MI200 Series performance counters](#mi300-and-mi200-series-performance-counters){.reference .internal .nav-link}
  - [Command processor counters](#command-processor-counters){.reference .internal .nav-link}
    - [Command processor-fetcher counters](#command-processor-fetcher-counters){.reference .internal .nav-link}
    - [Command processor-compute counters](#command-processor-compute-counters){.reference .internal .nav-link}
  - [Graphics register bus manager counters](#graphics-register-bus-manager-counters){.reference .internal .nav-link}
  - [Shader processor input counters](#shader-processor-input-counters){.reference .internal .nav-link}
  - [Compute unit counters](#compute-unit-counters){.reference .internal .nav-link}
    - [Instruction mix](#instruction-mix){.reference .internal .nav-link}
    - [Matrix fused multiply-add operation counters](#matrix-fused-multiply-add-operation-counters){.reference .internal .nav-link}
    - [Level counters](#level-counters){.reference .internal .nav-link}
    - [Wavefront counters](#wavefront-counters){.reference .internal .nav-link}
    - [Wavefront cycle counters](#wavefront-cycle-counters){.reference .internal .nav-link}
    - [LDS counters](#lds-counters){.reference .internal .nav-link}
    - [Miscellaneous counters](#miscellaneous-counters){.reference .internal .nav-link}
  - [L1 instruction cache (L1i) and scalar L1 data cache (L1d) counters](#l1-instruction-cache-l1i-and-scalar-l1-data-cache-l1d-counters){.reference .internal .nav-link}
  - [Vector L1 cache subsystem counters](#vector-l1-cache-subsystem-counters){.reference .internal .nav-link}
    - [Texture addressing unit counters](#texture-addressing-unit-counters){.reference .internal .nav-link}
    - [Texture data unit counters](#texture-data-unit-counters){.reference .internal .nav-link}
    - [Texture cache per pipe counters](#texture-cache-per-pipe-counters){.reference .internal .nav-link}
    - [Texture cache arbiter counters](#texture-cache-arbiter-counters){.reference .internal .nav-link}
  - [L2 cache access counters](#l2-cache-access-counters){.reference .internal .nav-link}
- [MI300 and MI200 Series derived metrics list](#mi300-and-mi200-series-derived-metrics-list){.reference .internal .nav-link}
  - [Hardware counters by and over all texture addressing unit instances](#hardware-counters-by-and-over-all-texture-addressing-unit-instances){.reference .internal .nav-link}
  - [Hardware counters over all texture cache per channel instances](#hardware-counters-over-all-texture-cache-per-channel-instances){.reference .internal .nav-link}
  - [Hardware counters by, for, or over all texture cache per pipe instances](#hardware-counters-by-for-or-over-all-texture-cache-per-pipe-instances){.reference .internal .nav-link}
  - [Hardware counter over all texture data unit instances](#hardware-counter-over-all-texture-data-unit-instances){.reference .internal .nav-link}
::::
:::::
::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
