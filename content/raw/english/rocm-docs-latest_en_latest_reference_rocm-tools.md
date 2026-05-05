---
title: "ROCm tools, compilers, and runtime API"
source_url: "https://rocm.docs.amd.com/en/latest/reference/rocm-tools.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:01:18.199408+00:00
content_hash: "248e7a7bd98f98a7"
---

---
description: ROCm API libraries & tools
keywords: ROCm, API, libraries, tools, AI, artificial intelligence, development, Communications, C++ primitives, Fast Fourier transforms, FFTs, random number generators, linear algebra, AMD
readthedocs-http-status: 200
readthedocs-project-slug: advanced-micro-devices-demo
readthedocs-resolver-filename: /reference/rocm-tools.html
readthedocs-version-slug: latest
---

::: sbt-scroll-pixel-helper

:::::::::::::::::::::::::::::::::::::::::::::::: bd-content
::::::::::::::::::::::::::::::::::::::::::::::: bd-article-container
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
# ROCm tools, compilers, and runtime API

:::: {#print-main-content}
::: {#jb-print-toc}

::: {#searchbox}

:::::::::::::::::::::::::::::::::: {#rocm-tools-compilers-and-runtime-api .section .tex2jax_ignore .mathjax_ignore}
# ROCm tools, compilers, and runtime API[\#](#rocm-tools-compilers-and-runtime-api "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-03-10

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 2 min read time

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils style="color:gray;"}
Applies to Linux

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}

:::::::::::::::::::::::: {.sd-container-fluid .sd-sphinx-override .sd-mb-4 .rocm-doc-grid .docutils}
::::::::::::::::::::::: {.sd-row .sd-row-cols-1 .sd-row-cols-xs-1 .sd-row-cols-sm-2 .sd-row-cols-md-2 .sd-row-cols-lg-2 .sd-g-3 .sd-g-xs-3 .sd-g-sm-3 .sd-g-md-3 .sd-g-lg-3 .docutils}
:::::: {.sd-col .sd-d-flex-row .docutils}
::::: {.sd-card .sd-sphinx-override .sd-w-100 .sd-shadow-sm .docutils}
:::: {.sd-card-body .rocm-card-banner .rocm-hue-1 .docutils}
::: {.sd-card-title .sd-font-weight-bold .docutils}
System Management

- [[AMD SMI]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/amdsmi/en/latest/index.html "(in AMD SMI v26.2.2)"){.reference .external}

- [[ROCm Data Center Tool]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rdc/en/latest/index.html "(in ROCm Data Center tool)"){.reference .external}

- [[rocminfo]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocminfo/en/latest/index.html "(in rocminfo v1.0.0)"){.reference .external}

- [[ROCm SMI]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocm_smi_lib/en/latest/index.html "(in ROCm SMI LIB Documentation v7.8.0)"){.reference .external}

- [[ROCm Validation Suite]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/ROCmValidationSuite/en/latest/index.html "(in RVS Documentation v1.3.0)"){.reference .external}

:::::: {.sd-col .sd-d-flex-row .docutils}
::::: {.sd-card .sd-sphinx-override .sd-w-100 .sd-shadow-sm .docutils}
:::: {.sd-card-body .rocm-card-banner .rocm-hue-6 .docutils}
::: {.sd-card-title .sd-font-weight-bold .docutils}

- [[ROCm Bandwidth Test]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocm_bandwidth_test/en/latest/index.html "(in rocm_bandwidth_test)"){.reference .external}

- [[ROCm Compute Profiler]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocprofiler-compute/en/latest/index.html "(in ROCm Compute Profiler v3.4.0)"){.reference .external}

- [[ROCm Systems Profiler]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocprofiler-systems/en/latest/index.html "(in rocprofiler-systems v1.3.0)"){.reference .external}

- [[ROCProfiler]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocprofiler/en/latest/index.html "(in rocprofiler Documentation v2.0.0)"){.reference .external}

- [[ROCprofiler-SDK]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/index.html "(in Rocprofiler SDK v1.1.0)"){.reference .external}

- [[ROCTracer]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/roctracer/en/latest/index.html "(in ROCTracer Documentation v4.1.0)"){.reference .external}

:::::: {.sd-col .sd-d-flex-row .docutils}
::::: {.sd-card .sd-sphinx-override .sd-w-100 .sd-shadow-sm .docutils}
:::: {.sd-card-body .rocm-card-banner .rocm-hue-1 .docutils}
::: {.sd-card-title .sd-font-weight-bold .docutils}

- [[ROCm CMake]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/ROCmCMakeBuildTools/en/latest/index.html "(in ROCm CMake Build Tools v0.14.0)"){.reference .external}

- [[HIPIFY]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/HIPIFY/en/latest/index.html "(in HIPIFY Documentation)"){.reference .external}

- [[ROCdbgapi]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/ROCdbgapi/en/latest/index.html "(in ROCdbgapi Documentation v0.77.4)"){.reference .external}

- [[ROCm Debugger (ROCgdb)]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/ROCgdb/en/latest/index.html "(in ROCgdb Documentation v16.3)"){.reference .external}

- [[ROCr Debug Agent]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocr_debug_agent/en/latest/index.html "(in rocr_debug_agent v2.1.0)"){.reference .external}

:::::: {.sd-col .sd-d-flex-row .docutils}
::::: {.sd-card .sd-sphinx-override .sd-w-100 .sd-shadow-sm .docutils}
:::: {.sd-card-body .rocm-card-banner .rocm-hue-8 .docutils}
::: {.sd-card-title .sd-font-weight-bold .docutils}

- [[ROCm Compilers]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/llvm-project/en/latest/index.html "(in llvm-project Documentation v22.0.0)"){.reference .external}

- [[HIPCC]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/HIPCC/en/latest/index.html "(in HIPCC Documentation v1.1.1)"){.reference .external}

- :::::

:::::: {.sd-col .sd-d-flex-row .docutils}
::::: {.sd-card .sd-sphinx-override .sd-w-100 .sd-shadow-sm .docutils}
:::: {.sd-card-body .rocm-card-banner .rocm-hue-12 .docutils}
::: {.sd-card-title .sd-font-weight-bold .docutils}
Runtime API

- [[HIP]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/HIP/en/latest/index.html "(in HIP Documentation v7.2.53211)"){.reference .external}
