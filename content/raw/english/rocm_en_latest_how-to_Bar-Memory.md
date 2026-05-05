---
title: "Troubleshoot BAR access limitation"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/Bar-Memory.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-03
---

:::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

:::::::::::::::::::::::::::::::::::::::: bd-content
::::::::::::::::::::::::::::::::::: bd-article-container
:::::::::: {.bd-header-article .d-print-none}
::::::::: {.header-article-items .header-article__inner}
::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}
:::

::: header-article-item
- [](../index.html){.nav-link aria-label="Home"}
- Troubleshoot\...
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
# Troubleshoot BAR access limitation

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [Handling physical address limitation](#handling-physical-address-limitation){.reference .internal .nav-link}
- [BAR configuration for AMD GPUs](#bar-configuration-for-amd-gpus){.reference .internal .nav-link}
  - [Example of BAR usage on AMD GPUs](#example-of-bar-usage-on-amd-gpus){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

:::::::::::::::::: {#troubleshoot-bar-access-limitation .section}
# Troubleshoot BAR access limitation[\#](#troubleshoot-bar-access-limitation "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23
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

Direct Memory Access (DMA) to PCIe devices using Base Address Registers (BARs) can be restricted due to physical addressing limits. These restrictions can result in data access failures between the system components. Peer-to-peer (P2P) DMA is used to access resources such as registers and memory between devices. PCIe devices need memory-mapped input/output (MMIO) space for DMA, and these MMIO spaces are defined in the PCIe BARs.

These BARs are a set of 32-bit or 64-bit registers that are used to define the resources that PCIe devices provide. The CPU and other system devices also use these to access the resources of the PCIe devices. P2P DMA only works when one device can directly access the local BAR memory of another. If the memory address of a BAR memory exceeds the physical addressing limit of a device, the device will not be able to access that BAR. This could be the device's own BAR or the BAR of another device in the system.

If the BAR memory exceeds than the physical addressing limit of the device, the device will not be able to access the remote BAR.

To handle any BAR access issues that might occur, you need to be aware of the physical address limitations of the devices and understand the [[BAR configuration of AMD GPUs]{.std .std-ref}](#bar-configuration){.reference .internal}. This information is important when setting up additional MMIO apertures for PCIe devices in the system's physical address space.

::: {#handling-physical-address-limitation .section}
## Handling physical address limitation[\#](#handling-physical-address-limitation "Link to this heading"){.headerlink}

When a system boots, the system BIOS allocates the physical address space for the components in the system, including system memory and MMIO apertures. On modern 64-bit platforms, there are generally two or more MMIO apertures: one located below 4 GB of physical address space for 32-bit compatibility, and one or more above 4 GB for devices needing more space.

You can control the memory address of the high MMIO aperture from the system BIOS configuration options. This lets you configure the additional MMIO space to align with the physical addressing limit and allows P2P DMA between the devices. For example, if a PCIe device is limited to 44-bit of physical addressing, you should ensure that the MMIO aperture is set below 44-bit in the system physical address space.

There are two ways to handle this:

- Ensure that the high MMIO aperture is within the physical addressing limits of the devices in the system. For example, if the devices have a 44-bit physical addressing limit, set the [`MMIO`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`High`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`Base`{.docutils .literal .notranslate}]{.pre} and [`MMIO`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`High`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`size`{.docutils .literal .notranslate}]{.pre} options in the BIOS such that the aperture is within the 44-bit address range, and ensure that the [`Above`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`4G`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`Decoding`{.docutils .literal .notranslate}]{.pre} option is Enabled.

- Enable the Input-Output Memory Management Unit (IOMMU). When the IOMMU is enabled in non-passthrough mode, it will create a virtual I/O address space for each device on the system. It also ensures that all virtual addresses created in that space are within the physical addressing limits of the device. For more information on IOMMU, see [Input-Output Memory Management Unit (IOMMU)](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/conceptual/iommu.html){.reference .external}.
:::

::::::: {#bar-configuration-for-amd-gpus .section}
[]{#bar-configuration}

## BAR configuration for AMD GPUs[\#](#bar-configuration-for-amd-gpus "Link to this heading"){.headerlink}

The following table shows how the BARs are configured for AMD GPUs.

::: pst-scrollable-table-container
+------------------+----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| BAR Type         | Value                            | Description                                                                                                                                                                                                                                                                                                                                       |
+==================+==================================+===================================================================================================================================================================================================================================================================================================================================================+
| BAR0-1 registers | 64-bit, Prefetchable, GPU memory | 8 GB or 16 GB depending on GPU. Set to less than 2\^44 to support P2P access from other GPUs with a 44-bit physical address limit. Prefetchable memory enables faster read operation for high-performance computing (HPC) by fetching the contiguous data from the same data source even before requested as an anticipation of a future request. |
+------------------+----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| BAR2-3 registers | 64-bit, Prefetchable, Doorbell   | Set to less than 2\^44 to support P2P access from other GPUs with a 44-bit physical address limit. As a Doorbell BAR, it indicates to the GPU that a new operation is in its queue to be processed.                                                                                                                                               |
+------------------+----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| BAR4 register    | Optional                         | Not a boot device                                                                                                                                                                                                                                                                                                                                 |
+------------------+----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| BAR5 register    | 32-bit, Non-prefetchable, MMIO   | Is set to less than 4 GB.                                                                                                                                                                                                                                                                                                                         |
+------------------+----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
:::

::::: {#example-of-bar-usage-on-amd-gpus .section}
### Example of BAR usage on AMD GPUs[\#](#example-of-bar-usage-on-amd-gpus "Link to this heading"){.headerlink}

Following is an example configuration of BARs set by the system BIOS on GFX8 GPUs with the 40-bit physical addressing limit:

:::: {.highlight-shell .notranslate}
::: highlight
    11:00.0 Display controller: Advanced Micro Devices, Inc. [AMD/ATI] Fiji [Radeon R9 FURY / NANO
    Series] (rev c1)

    Subsystem: Advanced Micro Devices, Inc. [AMD/ATI] Device 0b35

    Flags: bus master, fast devsel, latency 0, IRQ 119

    Memory at bf40000000 (64-bit, prefetchable) [size=256M]

    Memory at bf50000000 (64-bit, prefetchable) [size=2M]

    I/O ports at 3000 [size=256]

    Memory at c7400000 (32-bit, non-prefetchable) [size=256K]

    Expansion ROM at c7440000 [disabled] [size=128K]
:::
::::

Details of the BARs configured in the example are:

**GPU Frame Buffer BAR:** [`Memory`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`at`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`bf40000000`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`(64-bit,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`prefetchable)`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`[size=256M]`{.docutils .literal .notranslate}]{.pre}

The size of the BAR in the example is 256 MB. Generally, it will be the size of the GPU memory (typically 4 GB+). Depending upon the physical address limit and generation of AMD GPUs, the BAR can be set below 2\^40, 2\^44, or 2\^48.

**Doorbell BAR:** [`Memory`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`at`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`bf50000000`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`(64-bit,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`prefetchable)`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`[size=2M]`{.docutils .literal .notranslate}]{.pre}

The size of the BAR should typically be less than 10 MB for this generation of GPUs and has been set to 2 MB in the example. This BAR is placed less than 2\^40 to allow peer-to-peer access from other generations of AMD GPUs.

**I/O BAR:** [`I/O`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`ports`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`at`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`3000`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`[size=256]`{.docutils .literal .notranslate}]{.pre}

This is for legacy VGA and boot device support. Because the GPUs used are not connected to a display (VGA devices), this is not a concern, even if it isn't set up in the system BIOS.

**MMIO BAR:** [`Memory`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`at`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`c7400000`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`(32-bit,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`non-prefetchable)`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`[size=256K]`{.docutils .literal .notranslate}]{.pre}

The AMD Driver requires this to access the configuration registers. Since the reminder of the BAR available is only 1 DWORD (32-bit), this is set less than 4 GB. In the example, it is fixed at 256 KB.

**Expansion ROM:** [`Expansion`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`ROM`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`at`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`c7440000`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`[disabled]`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`[size=128K]`{.docutils .literal .notranslate}]{.pre}

This is required by the AMD Driver to access the GPU video-BIOS. In the example, it is fixed at 128 KB.
:::::
:::::::
::::::::::::::::::

::::: prev-next-area
[](setting-cus.html "previous page"){.left-prev}

::: prev-next-info
previous

Setting the number of compute units
:::

[](../conceptual/gpu-arch.html "next page"){.right-next}

::: prev-next-info
next

GPU architecture documentation
:::
:::::
:::::::::::::::::::::::::::::::::::

:::::: {.bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {.page-toc .tocsection .onthispage}
Contents
:::

- [Handling physical address limitation](#handling-physical-address-limitation){.reference .internal .nav-link}
- [BAR configuration for AMD GPUs](#bar-configuration-for-amd-gpus){.reference .internal .nav-link}
  - [Example of BAR usage on AMD GPUs](#example-of-bar-usage-on-amd-gpus){.reference .internal .nav-link}
::::
:::::
::::::
::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::
