---
title: "Setting the number of compute units"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/setting-cus.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-04-28
---

::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}

::: header-article-item
- [](../index.html){.nav-link aria-label="Home"}
- Setting the\...

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons

# Setting the number of compute units




# Setting the number of compute units[\#](#setting-the-number-of-compute-units "Link to this heading"){.headerlink}

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 4 min read time

Applies to Linux and Windows


The GPU driver provides two environment variables to set the number of CUs used:

- [`HSA_CU_MASK`{.docutils .literal .notranslate}]{.pre}

- [`ROC_GLOBAL_CU_MASK`{.docutils .literal .notranslate}]{.pre}

The [`ROC_GLOBAL_CU_MASK`{.docutils .literal .notranslate}]{.pre} variable sets the CU mask on queues created by HIP or OpenCL runtimes. The [`HSA_CU_MASK`{.docutils .literal .notranslate}]{.pre} variable sets the mask on a lower level of queue creation in the driver. It also sets the mask on the queues being profiled.

Tip

When using GPUs to accelerate compute workloads, it sometimes becomes necessary to configure the hardware's usage of compute units (CU). This is a more advanced option, so please read this page before experimentation.

The environment variables have the following syntax:

::: highlight
    ID = [0-9][0-9]*                         ex. base 10 numbers
    ID_list = (ID | ID-ID)[, (ID | ID-ID)]*  ex. 0,2-4,7
    GPU_list = ID_list                       ex. 0,2-4,7
    CU_list = 0x[0-F]* | ID_list             ex. 0x337F OR 0,2-4,7
    CU_Set = GPU_list : CU_list              ex. 0,2-4,7:0-15,32-47 OR 0,2-4,7:0x337F
    HSA_CU_MASK = CU_Set [; CU_Set]*         ex. 0,2-4,7:0-15,32-47; 3-9:0x337F

The GPU indices are taken post [`ROCR_VISIBLE_DEVICES`{.docutils .literal .notranslate}]{.pre} reordering. The listed or masked CUs are enabled for listed GPUs, and the others are disabled. Unlisted GPUs are not be affected, and their CUs are enabled.

The variable parsing stops when a syntax error occurs. The erroneous set and the following are ignored. Repeating GPU or CU IDs results in a syntax error. Specifying a mask with no usable CUs (CU_list is 0x0) results in a syntax error. To exclude GPU devices, use [`ROCR_VISIBLE_DEVICES`{.docutils .literal .notranslate}]{.pre}.

Note

These environment variables only affect ROCm software, not graphics applications.

Not all CU configurations are valid on all devices. For example, on devices where two CUs can be combined into a WGP (for kernels running in WGP mode), it's not valid to disable only a single CU in a WGP.

::::: prev-next-area
[](../conceptual/compiler-topics.html "previous page"){.left-prev}

::: prev-next-info
previous

Using compiler features

[](Bar-Memory.html "next page"){.right-next}

::: prev-next-info
next

Troubleshoot BAR access limitation
