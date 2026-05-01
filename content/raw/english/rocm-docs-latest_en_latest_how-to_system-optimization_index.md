---
title: "System optimization"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/system-optimization/index.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-01
---

::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

::::::::::::::::::::::::::::::::::::::: bd-content
:::::::::::::::::::::::::::::::::::::: bd-article-container
:::::::::: {.bd-header-article .d-print-none}
::::::::: {.header-article-items .header-article__inner}
::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}
:::

::: header-article-item
- [](../../index.html){.nav-link aria-label="Home"}
- System optimization
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
# System optimization

:::: {#print-main-content}
::: {#jb-print-toc}
:::
::::
:::::

::: {#searchbox}
:::

:::::::::::::::::::::: {#system-optimization .section}
# System optimization[\#](#system-optimization "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-04-08
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 2 min read time
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

This guide outlines system setup and tuning suggestions for AMD hardware to optimize performance for specific types of workloads or use-cases. The contents are structured according to the hardware:

:::::::::::: {.sd-container-fluid .sd-sphinx-override .sd-mb-4 .docutils}
::::::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-2 .sd-row-cols-md-2 .sd-row-cols-lg-2 .docutils}
:::::: {.sd-col .sd-d-flex-row .docutils}
::::: {.sd-card .sd-sphinx-override .sd-w-100 .sd-shadow-sm .docutils}
:::: {.sd-card-body .docutils}
::: {.sd-card-title .sd-font-weight-bold .docutils}
AMD RDNA
:::

- [[AMD RDNA3.5 system optimization]{.doc}](rdna3-5.html){.reference .internal}

- [[AMD RDNA2 system optimization]{.doc}](w6000-v620.html){.reference .internal}
::::
:::::
::::::

:::::: {.sd-col .sd-d-flex-row .docutils}
::::: {.sd-card .sd-sphinx-override .sd-w-100 .sd-shadow-sm .docutils}
:::: {.sd-card-body .docutils}
::: {.sd-card-title .sd-font-weight-bold .docutils}
AMD Instinct
:::

- [AMD Instinct MI300X](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi300x.html){.reference .external}

- [AMD Instinct MI300A](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi300a.html){.reference .external}

- [AMD Instinct MI200](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi200.html){.reference .external}

- [AMD Instinct MI100](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi100.html){.reference .external}
::::
:::::
::::::
:::::::::::
::::::::::::
::::::::::::::::::::::

::::: prev-next-area
[](../rocm-for-hpc/index.html "previous page"){.left-prev}

::: prev-next-info
previous

Using ROCm for HPC
:::

[](../gpu-performance/mi300x.html "next page"){.right-next}

::: prev-next-info
next

AMD Instinct MI300X performance guides
:::
:::::
::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::
