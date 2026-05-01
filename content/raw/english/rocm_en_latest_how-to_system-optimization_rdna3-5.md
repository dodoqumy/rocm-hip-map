---
title: "AMD RDNA3.5 system optimization"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/system-optimization/rdna3-5.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-01
---

::::::::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

::::::::::::::::::::::::::::::::::::::::::::::::::: bd-content
:::::::::::::::::::::::::::::::::::::::::::::: bd-article-container
:::::::::: {.bd-header-article .d-print-none}
::::::::: {.header-article-items .header-article__inner}
::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}
:::

::: header-article-item
- [](../../index.html){.nav-link aria-label="Home"}
- AMD RDNA3.5\...
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
# AMD RDNA3.5 system optimization

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [Memory settings](#memory-settings){.reference .internal .nav-link}
  - [Configuring shared memory limits on Linux](#configuring-shared-memory-limits-on-linux){.reference .internal .nav-link}
    - [Example with output](#example-with-output){.reference .internal .nav-link}
- [Operating system support](#operating-system-support){.reference .internal .nav-link}
  - [Required kernel version](#required-kernel-version){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

::::::::::::::::::::::::::::::: {#amd-rdna3-5-system-optimization .section}
[]{#strix-halo-optimization}

# AMD RDNA3.5 system optimization[\#](#amd-rdna3-5-system-optimization "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-04-08
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 8 min read time
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

This topic describes how to optimize systems powered by AMD Ryzen APUs with RDNA3.5 architecture. These APUs combine high-performance CPU cores with integrated RDNA3.5 graphics, and support LPDDR5X-8000 or DDR5 memory, making them particularly well-suited for:

- LLM development and inference systems

- High-performance workstations

- Virtualization hosts running multiple VMs

- GPU compute and parallel processing

- Gaming systems

- Home servers and AI development platforms

:::::::::::::::: {#memory-settings .section}
[]{#id1}

## Memory settings[\#](#memory-settings "Link to this heading"){.headerlink}

AMD Ryzen APUs with RDNA3.5 architecture (gfx1150, gfx1151, and gfx1152 LLVM targets) memory access is handled through GPU Virtual Memory (GPUVM), which provides per-process GPU virtual address spaces (VMIDs) rather than a separate, discrete VRAM pool.

As a result, memory on RDNA3.5 APUs is mapped rather than physically partitioned. The terms Graphics Address Remapping Table (GART) and Graphics Translation Table (GTT) describe limits on how much system memory can be mapped into GPU address spaces and who can use it, rather than distinct types of physical memory.

- **GART**

  Defines the amount of platform address space (system RAM or Memory-Mapped I/O) that can be mapped into the GPU virtual address space used by the kernel driver. On systems with physically shared CPU and GPU memory, such as RDNA3.5-based systems, this mapped system memory effectively serves as VRAM for the GPU. GART is typically kept relatively small to limit GPU page-table size and is primarily used for driver-internal operations.

- **GTT**

  Defines the amount of system RAM that can be mapped into GPU virtual address spaces for user processes. This is the memory pool used by applications such as PyTorch and other AI/compute workloads. GTT allocations are dynamic and not permanently reserved, allowing the operating system to reclaim memory when the GPU isn't actively using it. By default, the GTT limit is set to approximately 50 percent of total system RAM.

::: {.admonition .note}
Note

On systems with physically shared CPU and GPU memory, such as RDNA3.5-based systems, several terms are often used interchangeably in firmware menus, documentation, and community discussions:

- VRAM

- Carve-out

- GART

- Dedicated GPU memory

- Firmware-reserved GPU memory

In this topic, VRAM will be used going forward.
:::

You can adjust the amount of memory available to the GPU by:

- Increasing the VRAM in BIOS, or

- Reducing the configured GTT size to be smaller than the reserved amount.

If the GTT size is larger than the VRAM, the AMD GPU driver performs VRAM allocations using GTT (GTT-backed allocations), as described in the [torvalds/linux@759e764](https://github.com/torvalds/linux/commit/759e764f7d587283b4e0b01ff930faca64370e59){.reference .external} GitHub commit.

Because memory is physically shared, there's no performance distinction like that of discrete GPUs where dedicated VRAM is significantly faster than system memory. Firmware may optionally reserve some memory exclusively for GPU use, but this provides little benefit for most workloads while permanently reducing available system memory.

For this reason, AI frameworks work more efficiently with GTT-backed allocations. GTT allows large, flexible mappings without permanently reserving memory, resulting in better overall system utilization on unified memory systems.

:::::::::::::: {#configuring-shared-memory-limits-on-linux .section}
### Configuring shared memory limits on Linux[\#](#configuring-shared-memory-limits-on-linux "Link to this heading"){.headerlink}

The maximum amount of shared GPU-accessible memory can be increased by changing the kernel **Translation Table Manager (TTM)** page limit. This setting controls how many system memory pages can be mapped for GPU use and is exposed at:

:::: {.highlight-default .notranslate}
::: highlight
    /sys/module/ttm/parameters/pages_limit
:::
::::

The value is expressed in **pages**, and not bytes or gigabytes (GB).

::: {.admonition .note}
Note

It's recommended to keep the dedicated VRAM reservation in BIOS small (for example, 0.5 GB) and increasing the shared (TTM/GTT) limit instead.
:::

A helper utility is available to simplify configuration.

1.  Install [`pipx`{.docutils .literal .notranslate}]{.pre}:

    :::: {.highlight-default .notranslate}
    ::: highlight
        sudo apt install pipx
        pipx ensurepath
    :::
    ::::

2.  Install the AMD debug tools:

    :::: {.highlight-default .notranslate}
    ::: highlight
        pipx install amd-debug-tools
    :::
    ::::

3.  Query the current shared memory configuration:

    :::: {.highlight-default .notranslate}
    ::: highlight
        amd-ttm
    :::
    ::::

4.  Set the usable shared memory (in GB):

    :::: {.highlight-default .notranslate}
    ::: highlight
        amd-ttm --set <NUM>
    :::
    ::::

5.  Reboot for changes to take effect.

::: {.admonition .note}
Note

The amd-ttm convert the pages to GB to help the users.
:::

::::::::: {#example-with-output .section}
#### Example with output[\#](#example-with-output "Link to this heading"){.headerlink}

Check the current settings:

:::: {.highlight-default .notranslate}
::: highlight
    amd-ttm
    💻 Current TTM pages limit: 16469033 pages (62.82 GB)
    💻 Total system memory: 125.65 GB
:::
::::

Change the usable shared memory:

:::: {.highlight-default .notranslate}
::: highlight
    ❯ amd-ttm --set 100
    🐧 Successfully set TTM pages limit to 26214400 pages (100.00 GB)
    🐧 Configuration written to /etc/modprobe.d/ttm.conf
    ○ NOTE: You need to reboot for changes to take effect.
    Would you like to reboot the system now? (y/n): y
:::
::::

Revert to kernel defaults:

:::: {.highlight-default .notranslate}
::: highlight
     ❯ amd-ttm --clear
    🐧 Configuration /etc/modprobe.d/ttm.conf removed
     Would you like to reboot the system now? (y/n): y
:::
::::
:::::::::
::::::::::::::
::::::::::::::::

::::::: {#operating-system-support .section}
[]{#id2}

## Operating system support[\#](#operating-system-support "Link to this heading"){.headerlink}

The ROCm compatibility tables can be found at the following links:

- [System requirements (Linux)](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html){.reference .external}

- [System requirements (Microsoft Windows)](https://rocm.docs.amd.com/projects/install-on-windows/en/latest/reference/system-requirements.html){.reference .external}

AMD Ryzen AI Max series APUs (gfx1151) have additional kernel version requirements, as described in the following section.

:::::: {#required-kernel-version .section}
### Required kernel version[\#](#required-kernel-version "Link to this heading"){.headerlink}

Support for AMD Ryzen AI Max series APUs requires specific Linux kernel fixes that update internal limits in the AMD KFD driver to ensure correct queue creation and memory availability checks. Without these updates, GPU compute workloads might fail to initialize or exhibit unpredictable behavior.

The following commits are required for AMD Ryzen AI Max series support:

- [gregkh/linux@7f26af7](https://github.com/gregkh/linux/commit/7f26af7bf9b76c2c2a1a761aab5803e52be21eea){.reference .external}

- [gregkh/linux@7445db6](https://github.com/gregkh/linux/commit/7445db6a7d5a0242d8214582b480600b266cba9e){.reference .external}

These patches are available in the following minimum kernel versions:

- Ubuntu 24.04 Hardware Enablement (HWE): [`6.17.0-19.19~24.04.2`{.docutils .literal .notranslate}]{.pre} or later

- Ubuntu 24.04 Original Equipment Manufacturer (OEM): [`6.14.0-1018`{.docutils .literal .notranslate}]{.pre} or later

- All other distributions: Linux kernel [`6.18.4`{.docutils .literal .notranslate}]{.pre} or later

The table below reflects compatibility for AMD-released pre-built ROCm binaries only. Distributions that ship native ROCm packaging might provide different support levels.

::: pst-scrollable-table-container
+------+---------------------------------------------------------------+
| ❌   | Unsupported combination                                       |
+------+---------------------------------------------------------------+
| ⚠️   | Unstable/experimental combination                             |
+------+---------------------------------------------------------------+
| ✅   | Stable and supported combination                              |
+------+---------------------------------------------------------------+
:::

::: pst-scrollable-table-container
+------------------+-----------------------------------------------+--------------------------------+-------------------------------+
| ROCm Release     | ::: line                                      | Other distributions \>= 6.18.4 | Other distributions \< 6.18.4 |
|                  | Ubuntu 24.04 HWE (\>= 6.17.0-19.19\~24.04.2), |                                |                               |
|                  | :::                                           |                                |                               |
|                  |                                               |                                |                               |
|                  | ::: line                                      |                                |                               |
|                  | Ubuntu 24.04 OEM (\>= 6.14.0-1018) or         |                                |                               |
|                  | :::                                           |                                |                               |
|                  |                                               |                                |                               |
|                  | ::: line                                      |                                |                               |
|                  | Ubuntu 26.04 Generic                          |                                |                               |
|                  | :::                                           |                                |                               |
+==================+===============================================+================================+===============================+
| 7.11.0 or 7.12.0 | ✅                                            | ✅                             | ⚠️                            |
+------------------+-----------------------------------------------+--------------------------------+-------------------------------+
| 7.10.0 or 7.9.0  | ❌                                            | ❌                             | ⚠️                            |
+------------------+-----------------------------------------------+--------------------------------+-------------------------------+
| 7.2.1            | ✅                                            | ✅                             | ⚠️                            |
+------------------+-----------------------------------------------+--------------------------------+-------------------------------+
| 7.2.0            | ✅                                            | ✅                             | ❌                            |
+------------------+-----------------------------------------------+--------------------------------+-------------------------------+
| 7.1.x            | ❌                                            | ❌                             | ⚠️                            |
+------------------+-----------------------------------------------+--------------------------------+-------------------------------+
| 6.4.x            | ❌                                            | ❌                             | ⚠️                            |
+------------------+-----------------------------------------------+--------------------------------+-------------------------------+
:::

::: {.admonition .note}
Note

Ubuntu 24.04 HWE kernels earlier than [`6.17.0-19.19~24.04.2`{.docutils .literal .notranslate}]{.pre} and Ubuntu 24.04 OEM kernels earlier than [`6.14.0-1018`{.docutils .literal .notranslate}]{.pre} are not supported for RDNA3.5 APUs.

The following distributions include the required fixes in their native packaging, independent of AMD pre-built binaries:

- Fedora 43

- Ubuntu 26.04

- Arch Linux 2026.02.01
:::
::::::
:::::::
:::::::::::::::::::::::::::::::

::: prev-next-area
:::
::::::::::::::::::::::::::::::::::::::::::::::

:::::: {.bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {.page-toc .tocsection .onthispage}
Contents
:::

- [Memory settings](#memory-settings){.reference .internal .nav-link}
  - [Configuring shared memory limits on Linux](#configuring-shared-memory-limits-on-linux){.reference .internal .nav-link}
    - [Example with output](#example-with-output){.reference .internal .nav-link}
- [Operating system support](#operating-system-support){.reference .internal .nav-link}
  - [Required kernel version](#required-kernel-version){.reference .internal .nav-link}
::::
:::::
::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::
