---
title: "Performance analysis glossary"
source_url: "https://rocm.docs.amd.com/en/latest/reference/glossary/performance.html"
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
- Performance\...
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
# Performance analysis glossary

:::: {#print-main-content}
::: {#jb-print-toc}
:::
::::
:::::

::: {#searchbox}
:::

:::::::::::: {#performance-analysis-glossary .section}
[]{#glossary-performance}

# Performance analysis glossary[\#](#performance-analysis-glossary "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-02-20
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 5 min read time
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

This section provides brief definitions of performance analysis concepts and optimization techniques.

Active cycle[\#](#term-Active-cycle "Link to this term"){.headerlink}

:   An active cycle is a clock cycle in which a [[compute unit]{.xref .std .std-term}](device-hardware.html#term-Compute-units){.reference .internal} has at least one active [[wavefront]{.xref .std .std-term}](https://rocm.docs.amd.com/projects/rocPRIM/en/latest/reference/rocPRIM-glossary.html#term-Wavefront "(in rocPRIM Documentation v4.2.0)"){.reference .external} resident. See [Warp (Wavefront) execution states](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#wavefront-execution "(in HIP Documentation v7.2.53211)"){.reference .external} for details.

Arithmetic bandwidth[\#](#term-Arithmetic-bandwidth "Link to this term"){.headerlink}

:   Arithmetic bandwidth is the peak rate at which arithmetic work can be performed, defining the compute roof in [[roofline models]{.xref .std .std-term}](#term-Roofline-model){.reference .internal}. See [Compute-bound performance](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#compute-bound "(in HIP Documentation v7.2.53211)"){.reference .external} for details.

Arithmetic intensity[\#](#term-Arithmetic-intensity "Link to this term"){.headerlink}

:   Arithmetic intensity is the ratio of arithmetic operations to memory operations in a kernel, and determines performance characteristics. See [Arithmetic intensity](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#arithmetic-intensity "(in HIP Documentation v7.2.53211)"){.reference .external} for intensity analysis.

Bank conflict[\#](#term-Bank-conflict "Link to this term"){.headerlink}

:   A bank conflict occurs when multiple threads simultaneously access different addresses in the same [[LDS bank]{.xref .std .std-term}](device-hardware.html#term-Local-data-share){.reference .internal}, serializing accesses. See [Bank conflict theory](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#bank-conflicts-theory "(in HIP Documentation v7.2.53211)"){.reference .external} for details.

Branch efficiency[\#](#term-Branch-efficiency "Link to this term"){.headerlink}

:   Branch efficiency measures how often all threads within a [[wavefront]{.xref .std .std-term}](https://rocm.docs.amd.com/projects/rocPRIM/en/latest/reference/rocPRIM-glossary.html#term-Wavefront "(in rocPRIM Documentation v4.2.0)"){.reference .external} take the same execution path, quantifying control-flow uniformity. See [Branch efficiency](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#branch-efficiency "(in HIP Documentation v7.2.53211)"){.reference .external} for branch analysis.

Compute-bound[\#](#term-Compute-bound "Link to this term"){.headerlink}

:   Compute-bound kernels are limited by the [[arithmetic bandwidth]{.xref .std .std-term}](#term-Arithmetic-bandwidth){.reference .internal} of the GPU's [[compute units]{.xref .std .std-term}](device-hardware.html#term-Compute-units){.reference .internal} rather than [[memory bandwidth]{.xref .std .std-term}](#term-Memory-bandwidth){.reference .internal}. See [Compute-bound performance](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#compute-bound "(in HIP Documentation v7.2.53211)"){.reference .external} for compute-bound analysis.

CU utilization[\#](#term-CU-utilization "Link to this term"){.headerlink}

:   CU utilization measures the percentage of time that [[compute units]{.xref .std .std-term}](device-hardware.html#term-Compute-units){.reference .internal} are actively executing instructions. See [CU utilization](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#cu-utilization "(in HIP Documentation v7.2.53211)"){.reference .external} for utilization analysis.

Issue efficiency[\#](#term-Issue-efficiency "Link to this term"){.headerlink}

:   Issue efficiency measures how effectively the [[wavefront scheduler]{.xref .std .std-term}](device-hardware.html#term-Wavefront-scheduler){.reference .internal} keeps execution pipelines busy by issuing instructions. See [Issue efficiency](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#issue-efficiency "(in HIP Documentation v7.2.53211)"){.reference .external} for efficiency metrics.

Latency hiding[\#](#term-Latency-hiding "Link to this term"){.headerlink}

:   Latency hiding masks long-latency operations by running many concurrent threads, keeping execution pipelines busy. See [Latency hiding mechanisms](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#latency-hiding "(in HIP Documentation v7.2.53211)"){.reference .external} for details.

Little's Law[\#](#term-Little-s-Law "Link to this term"){.headerlink}

:   Little's Law relates concurrency, latency, and throughput, determining how much independent work must be in flight to hide latency. See [Little's Law](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#littles-law "(in HIP Documentation v7.2.53211)"){.reference .external} for latency hiding details.

Memory bandwidth[\#](#term-Memory-bandwidth "Link to this term"){.headerlink}

:   Memory bandwidth is the maximum rate at which data can be transferred between memory hierarchy levels, typically measured in bytes per second. See [Memory-bound performance](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#memory-bound "(in HIP Documentation v7.2.53211)"){.reference .external} for details.

Memory coalescing[\#](#term-Memory-coalescing "Link to this term"){.headerlink}

:   Memory coalescing improves [[memory bandwidth]{.xref .std .std-term}](#term-Memory-bandwidth){.reference .internal} by servicing many logical loads or stores with fewer physical memory transactions. See [Memory coalescing theory](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#memory-coalescing-theory "(in HIP Documentation v7.2.53211)"){.reference .external} for coalescing patterns.

Memory-bound[\#](#term-Memory-bound "Link to this term"){.headerlink}

:   Memory-bound kernels are limited by [[memory bandwidth]{.xref .std .std-term}](#term-Memory-bandwidth){.reference .internal} rather than [[arithmetic bandwidth]{.xref .std .std-term}](#term-Arithmetic-bandwidth){.reference .internal}, typically due to low [[arithmetic intensity]{.xref .std .std-term}](#term-Arithmetic-intensity){.reference .internal}. See [Memory-bound performance](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#memory-bound "(in HIP Documentation v7.2.53211)"){.reference .external} for memory-bound analysis.

Occupancy[\#](#term-Occupancy "Link to this term"){.headerlink}

:   Occupancy is the ratio of active [[wavefronts]{.xref .std .std-term}](https://rocm.docs.amd.com/projects/rocPRIM/en/latest/reference/rocPRIM-glossary.html#term-Wavefront "(in rocPRIM Documentation v4.2.0)"){.reference .external} to the maximum number of wavefronts that can be active on a [[compute unit]{.xref .std .std-term}](device-hardware.html#term-Compute-units){.reference .internal}. See [Occupancy theory](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#occupancy "(in HIP Documentation v7.2.53211)"){.reference .external} for occupancy analysis.

Overhead[\#](#term-Overhead "Link to this term"){.headerlink}

:   Overhead latency is the time spent with no useful work being done, often due to CPU-side bottlenecks or kernel launch delays. See [Performance bottlenecks](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#performance-bottlenecks "(in HIP Documentation v7.2.53211)"){.reference .external} for details.

Peak rate[\#](#term-Peak-rate "Link to this term"){.headerlink}

:   Peak rate is the theoretical maximum throughput at which a hardware system can complete work under ideal conditions. See [Theoretical performance limits](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#theoretical-performance-limits "(in HIP Documentation v7.2.53211)"){.reference .external} for details.

Pipe utilization[\#](#term-Pipe-utilization "Link to this term"){.headerlink}

:   Pipe utilization measures how effectively a kernel uses the execution pipelines within each [[compute unit]{.xref .std .std-term}](device-hardware.html#term-Compute-units){.reference .internal}. See [Pipe utilization](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#pipe-utilization "(in HIP Documentation v7.2.53211)"){.reference .external} for utilization details.

Register pressure[\#](#term-Register-pressure "Link to this term"){.headerlink}

:   Register pressure occurs when excessive register demand limits the number of active [[wavefronts]{.xref .std .std-term}](https://rocm.docs.amd.com/projects/rocPRIM/en/latest/reference/rocPRIM-glossary.html#term-Wavefront "(in rocPRIM Documentation v4.2.0)"){.reference .external} per [[compute unit]{.xref .std .std-term}](device-hardware.html#term-Compute-units){.reference .internal}, reducing [[occupancy]{.xref .std .std-term}](#term-Occupancy){.reference .internal}. See [Register pressure theory](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#register-pressure-theory "(in HIP Documentation v7.2.53211)"){.reference .external} for details.

Roofline model[\#](#term-Roofline-model "Link to this term"){.headerlink}

:   The roofline model is a visual performance model that determines whether a program is [[compute-bound]{.xref .std .std-term}](#term-Compute-bound){.reference .internal} or [[memory-bound]{.xref .std .std-term}](#term-Memory-bound){.reference .internal}. See [Roofline model](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#roofline-model "(in HIP Documentation v7.2.53211)"){.reference .external} for roofline analysis.

Wavefront divergence[\#](#term-Wavefront-divergence "Link to this term"){.headerlink}

:   Wavefront divergence occurs when threads within a [[wavefront]{.xref .std .std-term}](https://rocm.docs.amd.com/projects/rocPRIM/en/latest/reference/rocPRIM-glossary.html#term-Wavefront "(in rocPRIM Documentation v4.2.0)"){.reference .external} take different execution paths due to conditional statements. See [Branch efficiency](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#branch-efficiency "(in HIP Documentation v7.2.53211)"){.reference .external} for divergence handling details.

Wavefront execution state[\#](#term-Wavefront-execution-state "Link to this term"){.headerlink}

:   Wavefront execution states (*active*, *stalled*, *eligible*, *selected*) describe the scheduling status of [[wavefronts]{.xref .std .std-term}](https://rocm.docs.amd.com/projects/rocPRIM/en/latest/reference/rocPRIM-glossary.html#term-Wavefront "(in rocPRIM Documentation v4.2.0)"){.reference .external} on AMD GPUs. See [Warp (Wavefront) execution states](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#wavefront-execution "(in HIP Documentation v7.2.53211)"){.reference .external} for state definitions.
::::::::::::

::::: prev-next-area
[](host-software.html "previous page"){.left-prev}

::: prev-next-info
previous

Host software glossary
:::

[](../../contribute/contributing.html "next page"){.right-next}

::: prev-next-info
next

Contributing to the ROCm documentation
:::
:::::
::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::
