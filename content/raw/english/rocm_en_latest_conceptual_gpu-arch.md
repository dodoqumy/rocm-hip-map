---
title: "GPU architecture documentation"
source_url: "https://rocm.docs.amd.com/en/latest/conceptual/gpu-arch.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-03
---

::::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

::::::::::::::::::::::::::::::::::::::::::::::: bd-content
:::::::::::::::::::::::::::::::::::::::::::::: bd-article-container
:::::::::: {.bd-header-article .d-print-none}
::::::::: {.header-article-items .header-article__inner}
::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}
:::

::: header-article-item
- [](../index.html){.nav-link aria-label="Home"}
- GPU\...
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
# GPU architecture documentation

:::: {#print-main-content}
::: {#jb-print-toc}
:::
::::
:::::

::: {#searchbox}
:::

:::::::::::::::::::::::::::::: {#gpu-architecture-documentation .section .tex2jax_ignore .mathjax_ignore}
[]{#gpu-arch-documentation}

# GPU architecture documentation[\#](#gpu-architecture-documentation "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-02-17
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 3 min read time
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

::::::::::::::::::: {.sd-container-fluid .sd-sphinx-override .sd-mb-4 .docutils}
:::::::::::::::::: {.sd-row .sd-row-cols-1 .sd-row-cols-xs-1 .sd-row-cols-sm-1 .sd-row-cols-md-2 .sd-row-cols-lg-2 .sd-g-1 .sd-g-xs-1 .sd-g-sm-1 .sd-g-md-1 .sd-g-lg-1 .docutils}
::::: {.sd-col .sd-d-flex-row .docutils}
:::: {.sd-card .sd-sphinx-override .sd-w-100 .sd-shadow-sm .docutils}
::: {.sd-card-body .docutils}
**AMD Instinct MI300 Series**

Review hardware aspects of the AMD Instinct™ MI300 Series GPUs and the CDNA™ 3 architecture.

- [[AMD Instinct™ MI300 microarchitecture]{.std .std-doc}](gpu-arch/mi300.html){.reference .internal}

- [AMD Instinct MI300/CDNA3 ISA](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/amd-instinct-mi300-cdna3-instruction-set-architecture.pdf){.reference .external}

- [White paper](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/white-papers/amd-cdna-3-white-paper.pdf){.reference .external}

- [[MI300 performance counters]{.std .std-doc}](gpu-arch/mi300-mi200-performance-counters.html){.reference .internal}

- [[MI350 Series performance counters]{.std .std-doc}](gpu-arch/mi350-performance-counters.html){.reference .internal}
:::
::::
:::::

::::: {.sd-col .sd-d-flex-row .docutils}
:::: {.sd-card .sd-sphinx-override .sd-w-100 .sd-shadow-sm .docutils}
::: {.sd-card-body .docutils}
**AMD Instinct MI200 Series**

Review hardware aspects of the AMD Instinct™ MI200 Series GPUs and the CDNA™ 2 architecture.

- [[AMD Instinct™ MI250 microarchitecture]{.std .std-doc}](gpu-arch/mi250.html){.reference .internal}

- [AMD Instinct MI200/CDNA2 ISA](https://www.amd.com/system/files/TechDocs/instinct-mi200-cdna2-instruction-set-architecture.pdf){.reference .external}

- [White paper](https://www.amd.com/content/dam/amd/en/documents/instinct-business-docs/white-papers/amd-cdna2-white-paper.pdf){.reference .external}

- [[Performance counters]{.std .std-doc}](gpu-arch/mi300-mi200-performance-counters.html){.reference .internal}
:::
::::
:::::

::::: {.sd-col .sd-d-flex-row .docutils}
:::: {.sd-card .sd-sphinx-override .sd-w-100 .sd-shadow-sm .docutils}
::: {.sd-card-body .docutils}
**AMD Instinct MI100**

Review hardware aspects of the AMD Instinct™ MI100 Series GPUs and the CDNA™ 1 architecture.

- [[AMD Instinct™ MI100 microarchitecture]{.std .std-doc}](gpu-arch/mi100.html){.reference .internal}

- [AMD Instinct MI100/CDNA1 ISA](https://www.amd.com/system/files/TechDocs/instinct-mi100-cdna1-shader-instruction-set-architecture%C2%A0.pdf){.reference .external}

- [White paper](https://www.amd.com/content/dam/amd/en/documents/instinct-business-docs/white-papers/amd-cdna-white-paper.pdf){.reference .external}
:::
::::
:::::

::::: {.sd-col .sd-d-flex-row .docutils}
:::: {.sd-card .sd-sphinx-override .sd-w-100 .sd-shadow-sm .docutils}
::: {.sd-card-body .docutils}
**RDNA**

- [AMD RDNA4 ISA](https://www.amd.com/content/dam/amd/en/documents/radeon-tech-docs/instruction-set-architectures/rdna4-instruction-set-architecture.pdf){.reference .external}

- [AMD RDNA3 ISA](https://www.amd.com/system/files/TechDocs/rdna3-shader-instruction-set-architecture-feb-2023_0.pdf){.reference .external}

- [AMD RDNA2 ISA](https://www.amd.com/system/files/TechDocs/rdna2-shader-instruction-set-architecture.pdf){.reference .external}

- [AMD RDNA ISA](https://www.amd.com/system/files/TechDocs/rdna-shader-instruction-set-architecture.pdf){.reference .external}
:::
::::
:::::

::::: {.sd-col .sd-d-flex-row .docutils}
:::: {.sd-card .sd-sphinx-override .sd-w-100 .sd-shadow-sm .docutils}
::: {.sd-card-body .docutils}
**Older architectures**

- [AMD Instinct MI50/Vega 7nm ISA](https://www.amd.com/system/files/TechDocs/vega-7nm-shader-instruction-set-architecture.pdf){.reference .external}

- [AMD Instinct MI25/Vega ISA](https://www.amd.com/system/files/TechDocs/vega-shader-instruction-set-architecture.pdf){.reference .external}

- [AMD GCN3 ISA](https://www.amd.com/system/files/TechDocs/gcn3-instruction-set-architecture.pdf){.reference .external}

- AMD Vega Architecture White Paper
:::
::::
:::::
::::::::::::::::::
:::::::::::::::::::

::: {.toctree-wrapper .compound}
:::
::::::::::::::::::::::::::::::

::::: prev-next-area
[](../how-to/Bar-Memory.html "previous page"){.left-prev}

::: prev-next-info
previous

Troubleshoot BAR access limitation
:::

[](gpu-arch/mi300.html "next page"){.right-next}

::: prev-next-info
next

AMD Instinct™ MI300 Series microarchitecture
:::
:::::
::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::
