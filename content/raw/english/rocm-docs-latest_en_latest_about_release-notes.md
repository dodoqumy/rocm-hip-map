---
title: "ROCm 7.2.2 release notes"
source_url: "https://rocm.docs.amd.com/en/latest/about/release-notes.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-01
---

::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

::::::::::::::::::::::::::::::: bd-content
:::::::::::::::::::::::::::::: bd-article-container
:::::::::: {.bd-header-article .d-print-none}
::::::::: {.header-article-items .header-article__inner}
::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}
:::

::: header-article-item
- [](../index.html){.nav-link aria-label="Home"}
- ROCm 7.2.2\...
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
# ROCm 7.2.2 release notes

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [Release highlights](#release-highlights){.reference .internal .nav-link}
  - [ROCTracer failure to report kernel operations is fixed](#roctracer-failure-to-report-kernel-operations-is-fixed){.reference .internal .nav-link}
  - [User space, driver, and firmware dependent changes](#user-space-driver-and-firmware-dependent-changes){.reference .internal .nav-link}
  - [ROCm documentation updates](#rocm-documentation-updates){.reference .internal .nav-link}
- [ROCm 7.2.1 release notes](#rocm-7-2-1-release-notes){.reference .internal .nav-link}
  - [Release highlights](#id1){.reference .internal .nav-link}
    - [Supported hardware, operating system, and virtualization changes](#supported-hardware-operating-system-and-virtualization-changes){.reference .internal .nav-link}
      - [Virtualization support](#virtualization-support){.reference .internal .nav-link}
    - [User space, driver, and firmware dependent changes](#id2){.reference .internal .nav-link}
    - [hipBLASLt updates](#hipblaslt-updates){.reference .internal .nav-link}
    - [Deep learning and AI framework updates](#deep-learning-and-ai-framework-updates){.reference .internal .nav-link}
      - [JAX](#jax){.reference .internal .nav-link}
  - [ROCm Offline Installer Creator discontinuation](#rocm-offline-installer-creator-discontinuation){.reference .internal .nav-link}
    - [ROCm documentation updates](#id3){.reference .internal .nav-link}
  - [ROCm components](#rocm-components){.reference .internal .nav-link}
  - [Detailed component changes](#detailed-component-changes){.reference .internal .nav-link}
    - [**AMD SMI** (26.2.2)](#amd-smi-26-2-2){.reference .internal .nav-link}
      - [Added](#added){.reference .internal .nav-link}
      - [Resolved issues](#resolved-issues){.reference .internal .nav-link}
    - [**HIP** (7.2.1)](#hip-7-2-1){.reference .internal .nav-link}
      - [Resolved issues](#id4){.reference .internal .nav-link}
      - [Changed](#changed){.reference .internal .nav-link}
    - [**hipBLASLt** (1.2.2)](#hipblaslt-1-2-2){.reference .internal .nav-link}
      - [Changed](#id5){.reference .internal .nav-link}
    - [**rocDecode** (1.7.0)](#rocdecode-1-7-0){.reference .internal .nav-link}
      - [Upcoming changes](#upcoming-changes){.reference .internal .nav-link}
    - [**rocJPEG** (1.4.0)](#rocjpeg-1-4-0){.reference .internal .nav-link}
      - [Changed](#id6){.reference .internal .nav-link}
      - [Upcoming changes](#id7){.reference .internal .nav-link}
    - [**rocSHMEM** (3.2.0)](#rocshmem-3-2-0){.reference .internal .nav-link}
      - [Added](#id8){.reference .internal .nav-link}
      - [Resolved issues](#id9){.reference .internal .nav-link}
      - [Known issues](#known-issues){.reference .internal .nav-link}
    - [**RPP** (2.2.1)](#rpp-2-2-1){.reference .internal .nav-link}
      - [Added](#id10){.reference .internal .nav-link}
      - [Optimized](#optimized){.reference .internal .nav-link}
  - [ROCm known issues](#rocm-known-issues){.reference .internal .nav-link}
    - [hipBLASLt performance regression for specific GEMM configurations](#hipblaslt-performance-regression-for-specific-gemm-configurations){.reference .internal .nav-link}
      - [AMD Instinct MI300X and MI325X GPUs](#amd-instinct-mi300x-and-mi325x-gpus){.reference .internal .nav-link}
      - [AMD Instinct MI350 Series GPUs](#amd-instinct-mi350-series-gpus){.reference .internal .nav-link}
  - [Longer runtime for hipBLASLt GEMM operations on Instinct MI300X GPUs in partitioned mode](#longer-runtime-for-hipblaslt-gemm-operations-on-instinct-mi300x-gpus-in-partitioned-mode){.reference .internal .nav-link}
  - [ROCTracer might fail to report kernel operations](#roctracer-might-fail-to-report-kernel-operations){.reference .internal .nav-link}
    - [Longer runtime for hipBLASLt GEMM operations on Instinct MI300X GPUs in partitioned mode](#id11){.reference .internal .nav-link}
    - [ROCTracer might fail to report kernel operations](#id12){.reference .internal .nav-link}
  - [ROCm resolved issues](#rocm-resolved-issues){.reference .internal .nav-link}
    - [Increased runtime latency of the HIP hipStreamCreate API](#increased-runtime-latency-of-the-hip-hipstreamcreate-api){.reference .internal .nav-link}
  - [ROCm upcoming changes](#rocm-upcoming-changes){.reference .internal .nav-link}
    - [ROCTracer, ROCProfiler, rocprof, and rocprofv2 deprecation](#roctracer-rocprofiler-rocprof-and-rocprofv2-deprecation){.reference .internal .nav-link}
    - [ROCm SMI deprecation](#rocm-smi-deprecation){.reference .internal .nav-link}
    - [Changes to ROCm Object Tooling](#changes-to-rocm-object-tooling){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

:::::::::::::::: {#rocm-7-2-2-release-notes .section .tex2jax_ignore .mathjax_ignore}
# ROCm 7.2.2 release notes[\#](#rocm-7-2-2-release-notes "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-04-14
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 19 min read time
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils style="color:gray;"}
Applies to Linux
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
:::
:::::::
::::::::
:::::::::
::::::::::
:::::::::::

ROCm 7.2.2 is a quality release that resolves the issue listed in the Release highlights.

:::::: {#release-highlights .section}
## Release highlights[\#](#release-highlights "Link to this heading"){.headerlink}

The following are the notable changes in ROCm 7.2.2.

::: {#roctracer-failure-to-report-kernel-operations-is-fixed .section}
### ROCTracer failure to report kernel operations is fixed[\#](#roctracer-failure-to-report-kernel-operations-is-fixed "Link to this heading"){.headerlink}

In ROCm 7.2.1, applications using [ROCTracer](https://rocm.docs.amd.com/projects/roctracer/en/latest/index.html){.reference .external} failed to receive some or all kernel operation events due to a ROCTracer reporting failure. This issue has been resolved, and the fix has been applied to ROCTracer.
:::

:::: {#user-space-driver-and-firmware-dependent-changes .section}
### User space, driver, and firmware dependent changes[\#](#user-space-driver-and-firmware-dependent-changes "Link to this heading"){.headerlink}

The software for AMD Data Center GPU products requires maintaining a hardware and software stack with interdependencies among the GPU and baseboard firmware, AMD GPU drivers, and the ROCm user space software. While AMD publishes drivers and ROCm user space components, your server or infrastructure provider publishes the GPU and baseboard firmware by bundling AMD firmware releases via an AMD Platform Level Data Model (PLDM) bundle, which includes the Integrated Firmware Image (IFWI).

GPU and baseboard firmware versioning might differ across GPU families.

::: pst-scrollable-table-container
ROCm Version
:::
::::
::::::
::::::::::::::::
::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::
