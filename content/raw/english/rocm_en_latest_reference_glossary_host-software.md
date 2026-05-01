---
title: "Host software glossary"
source_url: "https://rocm.docs.amd.com/en/latest/reference/glossary/host-software.html"
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
- Host\...
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
# Host software glossary

:::: {#print-main-content}
::: {#jb-print-toc}
:::
::::
:::::

::: {#searchbox}
:::

:::::::::::: {#host-software-glossary .section}
[]{#glossary-host-software}

# Host software glossary[\#](#host-software-glossary "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-02-20
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 4 min read time
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

This section provides brief definitions of development tools, compilers, libraries, and runtime environments for programming AMD GPUs.

AMD SMI[\#](#term-AMD-SMI "Link to this term"){.headerlink}

:   The [`amd-smi`{.docutils .literal .notranslate}]{.pre} command-line utility queries, monitors, and manages AMD GPU state, providing hardware information and performance metrics. See [AMD SMI documentation](https://rocm.docs.amd.com/projects/amdsmi/en/latest/index.html "(in AMD SMI v26.2.2)"){.reference .external} for detailed usage.

HIP C++ language extension[\#](#term-HIP-C-language-extension "Link to this term"){.headerlink}

:   HIP extends the C++ language with additional features designed for programming heterogeneous applications. These extensions mostly relate to the kernel language, but some can also be applied to host functionality. See [HIP C++ language extensions](https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_cpp_language_extensions.html "(in HIP Documentation v7.2.53211)"){.reference .external} for language fundamentals.

HIP compiler[\#](#term-HIP-compiler "Link to this term"){.headerlink}

:   The HIP compiler [`amdclang++`{.docutils .literal .notranslate}]{.pre} compiles HIP C++ programs into binaries that contain both host CPU and device GPU code. See [ROCm compiler reference](https://rocm.docs.amd.com/projects/llvm-project/en/latest/reference/rocmcc.html "(in llvm-project Documentation v22.0.0)"){.reference .external} for compiler flags and options.

HIP runtime API[\#](#term-HIP-runtime-API "Link to this term"){.headerlink}

:   The HIP runtime API provides an interface for GPU programming, offering functions for memory management, kernel launches, and synchronization. See [Using HIP runtime API](https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_runtime_api.html#hip-runtime-api-how-to "(in HIP Documentation v7.2.53211)"){.reference .external} for API overview.

HIP runtime compiler[\#](#term-HIP-runtime-compiler "Link to this term"){.headerlink}

:   The HIP Runtime Compiler (HIPRTC) compiles HIP source code at runtime into [[AMDGPU]{.xref .std .std-term}](device-software.html#term-AMDGPU-assembly){.reference .internal} binary code objects, enabling just-in-time kernel generation, device-specific optimization, and dynamic code creation for different GPUs. See [Programming for HIP runtime compiler (RTC)](https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_rtc.html#hip-runtime-compiler-how-to "(in HIP Documentation v7.2.53211)"){.reference .external} for API details.

ROCgdb[\#](#term-ROCgdb "Link to this term"){.headerlink}

:   ROCgdb is AMD's source-level debugger for HIP and ROCm applications, enabling debugging of both host CPU and GPU device code, including kernel breakpoints, stepping, and variable inspection. See [ROCgdb documentation](https://rocm.docs.amd.com/projects/ROCgdb/en/latest/index.html "(in ROCgdb Documentation v16.3)"){.reference .external} for usage and command reference.

ROCm and LLVM binary utilities[\#](#term-ROCm-and-LLVM-binary-utilities "Link to this term"){.headerlink}

:   ROCm and LLVM binary utilities are command-line tools for examining and manipulating GPU binaries and code objects. See [ROCm binary utilities](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/compilers.html#binary-utilities "(in HIP Documentation v7.2.53211)"){.reference .external} for utility details.

ROCm software platform[\#](#term-ROCm-software-platform "Link to this term"){.headerlink}

:   ROCm is AMD's GPU software stack, providing compiler toolchains, runtime environments, and performance libraries for HPC and AI applications. See [[What is ROCm?]{.doc}](../../what-is-rocm.html){.reference .internal} for a complete component overview.

rocprofv3[\#](#term-rocprofv3 "Link to this term"){.headerlink}

:   [`rocprofv3`{.docutils .literal .notranslate}]{.pre} is AMD's primary performance analysis tool, providing profiling, tracing, and performance counter collection. See [Using rocprofv3](https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/how-to/using-rocprofv3.html#using-rocprofv3 "(in Rocprofiler SDK v1.1.0)"){.reference .external} for profiling workflows.
::::::::::::

::::: prev-next-area
[](device-software.html "previous page"){.left-prev}

::: prev-next-info
previous

Device software glossary
:::

[](performance.html "next page"){.right-next}

::: prev-next-info
next

Performance analysis glossary
:::
:::::
::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::
