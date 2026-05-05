---
title: "ROCm tools, compilers, and runtimes"
source_url: "https://rocm.docs.amd.com/en/docs-6.2.0/reference/rocm-tools.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T18:04:07.890601+00:00
content_hash: "9e5e9c9410f558cb"
---

---
description: ROCm API libraries & tools
keywords: ROCm, API, libraries, tools, artificial intelligence, development, Communications, C++ primitives, Fast Fourier transforms, FFTs, random number generators, linear algebra, AMD
readthedocs-http-status: 200
readthedocs-project-slug: advanced-micro-devices-demo
readthedocs-resolver-filename: /reference/rocm-tools.html
readthedocs-version-slug: docs-6.2.0
---

::: sbt-scroll-pixel-helper

::::::::::::::::::::::::::::::::::::::::::: bd-content
:::::::::::::::::::::::::::::::::::::::::: bd-article-container
:::::::::: {.bd-header-article .d-print-none}
::::::::: {.header-article-items .header-article__inner}
::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}

::: header-article-item

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons

::::: {#jb-print-docs-body .onlyprint}
# ROCm tools, compilers, and runtimes

:::: {#print-main-content}
::: {#jb-print-toc}

::: {#searchbox}

::::::::::::::::::::::::::::: {#rocm-tools-compilers-and-runtimes .section .tex2jax_ignore .mathjax_ignore}
# ROCm tools, compilers, and runtimes[\#](#rocm-tools-compilers-and-runtimes "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils style="color:gray;"}
Applies to Linux and Windows

:::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
:::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij48cGF0aCBkPSJNNC43NSAwYS43NS43NSAwIDAxLjc1Ljc1VjJoNVYuNzVhLjc1Ljc1IDAgMDExLjUgMFYyaDEuMjVjLjk2NiAwIDEuNzUuNzg0IDEuNzUgMS43NXYxMC41QTEuNzUgMS43NSAwIDAxMTMuMjUgMTZIMi43NUExLjc1IDEuNzUgMCAwMTEgMTQuMjVWMy43NUMxIDIuNzg0IDEuNzg0IDIgMi43NSAySDRWLjc1QS43NS43NSAwIDAxNC43NSAwem0wIDMuNWg4LjVhLjI1LjI1IDAgMDEuMjUuMjVWNmgtMTFWMy43NWEuMjUuMjUgMCAwMS4yNS0uMjVoMnptLTIuMjUgNHY2Ljc1YzAgLjEzOC4xMTIuMjUuMjUuMjVoMTAuNWEuMjUuMjUgMCAwMC4yNS0uMjVWNy41aC0xMXoiIGZpbGwtcnVsZT0iZXZlbm9kZCIgLz48L3N2Zz4=){.sd-octicon .sd-octicon-calendar}]{.sd-pr-2}2024-07-31

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij48cGF0aCBkPSJNMS41IDhhNi41IDYuNSAwIDExMTMgMCA2LjUgNi41IDAgMDEtMTMgMHpNOCAwYTggOCAwIDEwMCAxNkE4IDggMCAwMDggMHptLjUgNC43NWEuNzUuNzUgMCAwMC0xLjUgMHYzLjVhLjc1Ljc1IDAgMDAuNDcxLjY5NmwyLjUgMWEuNzUuNzUgMCAwMC41NTctMS4zOTJMOC41IDcuNzQyVjQuNzV6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+PC9zdmc+){.sd-octicon .sd-octicon-clock}]{.sd-pr-2}3 min read time

::::::::::::::::::: {.sd-container-fluid .sd-sphinx-override .sd-mb-4 .rocm-doc-grid .docutils}
:::::::::::::::::: {.sd-row .sd-row-cols-1 .sd-row-cols-xs-1 .sd-row-cols-sm-2 .sd-row-cols-md-2 .sd-row-cols-lg-2 .docutils}
::::: {#system-tools .sd-col .sd-d-flex-row .sd-p-2 .docutils}
:::: {.sd-card .sd-sphinx-override .sd-w-100 .sd-shadow-sm .sd-text-black .docutils}
![System tools](../_images/banner-system.jpg){.sd-card-img-top}

::: {.sd-card-body .docutils}
- [[AMD SMI]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/amdsmi/en/docs-6.2.0/index.html "(in Python)"){.reference .external}

- [[ROCm Data Center Tool]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rdc/en/docs-6.2.0/index.html "(in ROCm Data Center Documentation)"){.reference .external}

- [[rocminfo]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocminfo/en/docs-6.2.0/index.html "(in rocminfo v1.0.0)"){.reference .external}

- [[ROCm SMI]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocm_smi_lib/en/docs-6.2.0/index.html "(in ROCm SMI LIB Documentation v7.3.0)"){.reference .external}

- [[ROCm Validation Suite]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/ROCmValidationSuite/en/docs-6.2.0/index.html "(in RVS Documentation v1.0.0)"){.reference .external}

::::: {#performance-tools .sd-col .sd-d-flex-row .sd-p-2 .docutils}
:::: {.sd-card .sd-sphinx-override .sd-w-100 .sd-shadow-sm .sd-text-black .docutils}
![Performance tools](../_images/banner-performance.jpg){.sd-card-img-top}

::: {.sd-card-body .docutils}
- [[Omniperf]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/omniperf/en/docs-6.2.0/index.html "(in Omniperf v2.0.1)"){.reference .external}

- [[Omnitrace]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/omnitrace/en/docs-6.2.0/index.html "(in omnitrace v1.11.2)"){.reference .external}

- [[ROCm Bandwidth Test]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocm_bandwidth_test/en/docs-6.2.0/index.html "(in rocm_bandwidth_test)"){.reference .external}

- [[ROCProfiler]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocprofiler/en/docs-6.2.0/index.html "(in rocprofiler Documentation v2.0.0)"){.reference .external}

- [[ROCprofiler-SDK]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/docs-6.2.0/index.html "(in Rocprofiler SDK v0.4.0)"){.reference .external}

- [[ROCTracer]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/roctracer/en/docs-6.2.0/index.html "(in roctracer Documentation v4.1.0)"){.reference .external}

::::: {#development-tools .sd-col .sd-d-flex-row .sd-p-2 .docutils}
:::: {.sd-card .sd-sphinx-override .sd-w-100 .sd-shadow-sm .sd-text-black .docutils}
![Development tools](../_images/banner-development.jpg){.sd-card-img-top}

::: {.sd-card-body .docutils}
- [[ROCm CMake]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/ROCmCMakeBuildTools/en/docs-6.2.0/index.html "(in ROCm CMake Build Tools v0.13.0)"){.reference .external}

- [[HIPIFY]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/HIPIFY/en/docs-6.2.0/index.html "(in HIPIFY Documentation)"){.reference .external}

- [[ROCdbgapi]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/ROCdbgapi/en/docs-6.2.0/index.html "(in ROCdbgapi Documentation v0.76.0)"){.reference .external}

- [[ROCm Debugger (ROCgdb)]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/ROCgdb/en/docs-6.2.0/index.html "(in ROCgdb Documentation v1.2.12)"){.reference .external}

- [[ROCr Debug Agent]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocr_debug_agent/en/docs-6.2.0/index.html "(in rocr_debug_agent v2.0.3)"){.reference .external}

::::: {#compilers .sd-col .sd-d-flex-row .sd-p-2 .docutils}
:::: {.sd-card .sd-sphinx-override .sd-w-100 .sd-shadow-sm .sd-text-black .docutils}
!::: {.sd-card-body .docutils}
- [[ROCm Compilers]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/llvm-project/en/docs-6.2.0/index.html "(in llvm-project Documentation v6.2.0)"){.reference .external}

- [[HIPCC]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/HIPCC/en/docs-6.2.0/index.html "(in HIPCC Documentation v1.1.1)"){.reference .external}

- :::::

::::: {#runtimes .sd-col .sd-d-flex-row .sd-p-2 .docutils}
:::: {.sd-card .sd-sphinx-override .sd-w-100 .sd-shadow-sm .sd-text-black .docutils}
!::: {.sd-card-body .docutils}
- [[AMD Common Language Runtime (CLR)]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/HIP/en/docs-6.2.0/understand/amd_clr.html "(in HIP Documentation v6.2.41133)"){.reference .external}

- [[HIP]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/HIP/en/docs-6.2.0/index.html "(in HIP Documentation v6.2.41133)"){.reference .external}

- [[ROCR-Runtime]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/ROCR-Runtime/en/docs-6.2.0/index.html "(in ROCR Documentation v1.14.0)"){.reference .external}
