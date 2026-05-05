---
title: "System debugging"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/system-debugging.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-03
---

::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

::::::::::::::::::::::::::::::::::::::::::: bd-content
:::::::::::::::::::::::::::::::::::::: bd-article-container
:::::::::: {.bd-header-article .d-print-none}
::::::::: {.header-article-items .header-article__inner}
::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}
:::

::: header-article-item
- [](../index.html){.nav-link aria-label="Home"}
- System debugging
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
# System debugging

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [ROCm language and system-level debug, flags, and environment variables](#rocm-language-and-system-level-debug-flags-and-environment-variables){.reference .internal .nav-link}
- [ROCr error code](#rocr-error-code){.reference .internal .nav-link}
- [Command to dump firmware version and get Linux kernel version](#command-to-dump-firmware-version-and-get-linux-kernel-version){.reference .internal .nav-link}
- [Debug flags](#debug-flags){.reference .internal .nav-link}
- [ROCr level environment variables for debug](#rocr-level-environment-variables-for-debug){.reference .internal .nav-link}
- [Turn off page retry on GFX9/Vega devices](#turn-off-page-retry-on-gfx9-vega-devices){.reference .internal .nav-link}
- [HIP environment variables 3.x](#hip-environment-variables-3-x){.reference .internal .nav-link}
  - [OpenCL debug flags](#opencl-debug-flags){.reference .internal .nav-link}
- [PCIe-debug](#pcie-debug){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

::::::::::::::::::::: {#system-debugging .section .tex2jax_ignore .mathjax_ignore}
# System debugging[\#](#system-debugging "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 4 min read time
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

::: {#rocm-language-and-system-level-debug-flags-and-environment-variables .section}
## ROCm language and system-level debug, flags, and environment variables[\#](#rocm-language-and-system-level-debug-flags-and-environment-variables "Link to this heading"){.headerlink}

Kernel options to avoid: the Ethernet port getting renamed every time you change graphics cards, [`net.ifnames=0`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`biosdevname=0`{.docutils .literal .notranslate}]{.pre}
:::

::: {#rocr-error-code .section}
## ROCr error code[\#](#rocr-error-code "Link to this heading"){.headerlink}

- 2 Invalid Dimension

- 4 Invalid Group Memory

- 8 Invalid (or Null) Code

- 32 Invalid Format

- 64 Group is too large

- 128 Out of VGPRs

- 0x80000000 Debug Options
:::

::: {#command-to-dump-firmware-version-and-get-linux-kernel-version .section}
## Command to dump firmware version and get Linux kernel version[\#](#command-to-dump-firmware-version-and-get-linux-kernel-version "Link to this heading"){.headerlink}

[`sudo`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`cat`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`/sys/kernel/debug/dri/1/amdgpu_firmware_info`{.docutils .literal .notranslate}]{.pre}

[`uname`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-a`{.docutils .literal .notranslate}]{.pre}
:::

::: {#debug-flags .section}
## Debug flags[\#](#debug-flags "Link to this heading"){.headerlink}

Debug messages when developing/debugging base ROCm driver. You could enable the printing from [`libhsakmt.so`{.docutils .literal .notranslate}]{.pre} by setting an environment variable, [`HSAKMT_DEBUG_LEVEL`{.docutils .literal .notranslate}]{.pre}. Available debug levels are 3-7. The higher level you set, the more messages will print.

- [`export`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`HSAKMT_DEBUG_LEVEL=3`{.docutils .literal .notranslate}]{.pre} : Only pr_err() prints.

- [`export`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`HSAKMT_DEBUG_LEVEL=4`{.docutils .literal .notranslate}]{.pre} : pr_err() and pr_warn() print.

- [`export`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`HSAKMT_DEBUG_LEVEL=5`{.docutils .literal .notranslate}]{.pre} : We currently do not implement "notice". Setting to 5 is same as setting to 4.

- [`export`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`HSAKMT_DEBUG_LEVEL=6`{.docutils .literal .notranslate}]{.pre} : pr_err(), pr_warn(), and pr_info print.

- [`export`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`HSAKMT_DEBUG_LEVEL=7`{.docutils .literal .notranslate}]{.pre} : Everything including pr_debug prints.
:::

::: {#rocr-level-environment-variables-for-debug .section}
## ROCr level environment variables for debug[\#](#rocr-level-environment-variables-for-debug "Link to this heading"){.headerlink}

[`HSA_ENABLE_SDMA=0`{.docutils .literal .notranslate}]{.pre}

[`HSA_ENABLE_INTERRUPT=0`{.docutils .literal .notranslate}]{.pre}

[`HSA_SVM_GUARD_PAGES=0`{.docutils .literal .notranslate}]{.pre}

[`HSA_DISABLE_CACHE=1`{.docutils .literal .notranslate}]{.pre}
:::

::: {#turn-off-page-retry-on-gfx9-vega-devices .section}
## Turn off page retry on GFX9/Vega devices[\#](#turn-off-page-retry-on-gfx9-vega-devices "Link to this heading"){.headerlink}

[`sudo`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-s`{.docutils .literal .notranslate}]{.pre}

[`echo`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`1`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`>`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`/sys/module/amdkfd/parameters/noretry`{.docutils .literal .notranslate}]{.pre}
:::

:::: {#hip-environment-variables-3-x .section}
## HIP environment variables 3.x[\#](#hip-environment-variables-3-x "Link to this heading"){.headerlink}

::: {#opencl-debug-flags .section}
### OpenCL debug flags[\#](#opencl-debug-flags "Link to this heading"){.headerlink}

[`AMD_OCL_WAIT_COMMAND=1`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`(0`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`=`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`OFF,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`1`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`=`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`On)`{.docutils .literal .notranslate}]{.pre}
:::
::::

::: {#pcie-debug .section}
## PCIe-debug[\#](#pcie-debug "Link to this heading"){.headerlink}

For information on how to debug and profile HIP applications, see [Debugging with HIP](https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/debugging.html "(in HIP Documentation v7.2.53211)"){.reference .external}
:::
:::::::::::::::::::::

::::: prev-next-area
[](gpu-performance/mi300x.html "previous page"){.left-prev}

::: prev-next-info
previous

AMD Instinct MI300X performance guides
:::

[](../conceptual/compiler-topics.html "next page"){.right-next}

::: prev-next-info
next

Using compiler features
:::
:::::
::::::::::::::::::::::::::::::::::::::

:::::: {.bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {.page-toc .tocsection .onthispage}
Contents
:::

- [ROCm language and system-level debug, flags, and environment variables](#rocm-language-and-system-level-debug-flags-and-environment-variables){.reference .internal .nav-link}
- [ROCr error code](#rocr-error-code){.reference .internal .nav-link}
- [Command to dump firmware version and get Linux kernel version](#command-to-dump-firmware-version-and-get-linux-kernel-version){.reference .internal .nav-link}
- [Debug flags](#debug-flags){.reference .internal .nav-link}
- [ROCr level environment variables for debug](#rocr-level-environment-variables-for-debug){.reference .internal .nav-link}
- [Turn off page retry on GFX9/Vega devices](#turn-off-page-retry-on-gfx9-vega-devices){.reference .internal .nav-link}
- [HIP environment variables 3.x](#hip-environment-variables-3-x){.reference .internal .nav-link}
  - [OpenCL debug flags](#opencl-debug-flags){.reference .internal .nav-link}
- [PCIe-debug](#pcie-debug){.reference .internal .nav-link}
::::
:::::
::::::
:::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::
