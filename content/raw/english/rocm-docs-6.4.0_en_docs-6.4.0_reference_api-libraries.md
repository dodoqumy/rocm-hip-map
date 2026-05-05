---
title: "ROCm libraries"
source_url: "https://rocm.docs.amd.com/en/docs-6.4.0/reference/api-libraries.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:21:30.059937+00:00
content_hash: "4f040d568665de20"
---

---
description: ROCm API libraries & tools
keywords: ROCm, API, libraries, tools, artificial intelligence, development, Communications, C++ primitives, Fast Fourier transforms, FFTs, random number generators, linear algebra, AMD
readthedocs-http-status: 200
readthedocs-project-slug: advanced-micro-devices-demo
readthedocs-resolver-filename: /reference/api-libraries.html
readthedocs-version-slug: docs-6.4.0
---

::: sbt-scroll-pixel-helper

:::::::::::::::::::::::::::::::::::::::::::: bd-content
::::::::::::::::::::::::::::::::::::::::::: bd-article-container
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
# ROCm libraries

:::: {#print-main-content}
::: {#jb-print-toc}

::: {#searchbox}

:::::::::::::::::::::::::::::: {#rocm-libraries .section .tex2jax_ignore .mathjax_ignore}
# ROCm libraries[\#](#rocm-libraries "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2025-05-22

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 2 min read time

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils style="color:gray;"}
Applies to Linux and Windows

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}

:::::::::::::::::::: {.sd-container-fluid .sd-sphinx-override .sd-mb-4 .rocm-doc-grid .docutils}
::::::::::::::::::: {.sd-row .sd-row-cols-1 .sd-row-cols-xs-1 .sd-row-cols-sm-2 .sd-row-cols-md-2 .sd-row-cols-lg-2 .sd-g-3 .sd-g-xs-3 .sd-g-sm-3 .sd-g-md-3 .sd-g-lg-3 .docutils}
:::::: {.sd-col .sd-d-flex-row .docutils}
::::: {.sd-card .sd-sphinx-override .sd-w-100 .sd-shadow-sm .docutils}
:::: {.sd-card-body .rocm-card-banner .rocm-hue-3 .docutils}
::: {.sd-card-title .sd-font-weight-bold .docutils}
Machine Learning and Computer Vision

- [[Composable Kernel]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/composable_kernel/en/docs-6.4.0/index.html "(in Composable Kernel Documentation v1.1.0)"){.reference .external}

- [[MIGraphX]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/AMDMIGraphX/en/docs-6.4.0/index.html "(in MIGraphX v2.12.0)"){.reference .external}

- [[MIOpen]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/MIOpen/en/docs-6.4.0/index.html "(in MIOpen Documentation v3.4.0)"){.reference .external}

- [[MIVisionX]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/MIVisionX/en/docs-6.4.0/index.html "(in MIVisionX Documentation v3.2.0)"){.reference .external}

- [[rocAL]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocAL/en/docs-6.4.0/index.html "(in rocAL Documentation v2.2.0)"){.reference .external}

- [[rocDecode]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocDecode/en/docs-6.4.0/index.html "(in rocDecode documentation v0.10.0)"){.reference .external}

- [[rocPyDecode]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocPyDecode/en/docs-6.4.0/index.html "(in rocPyDecode v0.3.1)"){.reference .external}

- [[rocJPEG]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocJPEG/en/docs-6.4.0/index.html "(in rocJPEG Documentation v0.8.0)"){.reference .external}

- [[ROCm Performance Primitives (RPP)]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rpp/en/docs-6.4.0/index.html "(in RPP documentation v1.9.10)"){.reference .external}

:::::: {.sd-col .sd-d-flex-row .docutils}
::::: {.sd-card .sd-sphinx-override .sd-w-100 .sd-shadow-sm .docutils}
:::: {.sd-card-body .rocm-card-banner .rocm-hue-12 .docutils}
::: {.sd-card-title .sd-font-weight-bold .docutils}

- [[hipCUB]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/hipCUB/en/docs-6.4.0/index.html "(in hipCUB Documentation v3.4.0)"){.reference .external}

- [[hipTensor]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/hipTensor/en/docs-6.4.0/index.html "(in hipTensor Documentation v1.5.0)"){.reference .external}

- [[rocPRIM]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocPRIM/en/docs-6.4.0/index.html "(in rocPRIM Documentation v3.4.0)"){.reference .external}

- [[rocThrust]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocThrust/en/docs-6.4.0/index.html "(in rocThrust Documentation v3.3.0)"){.reference .external}

:::::: {.sd-col .sd-d-flex-row .docutils}
::::: {.sd-card .sd-sphinx-override .sd-w-100 .sd-shadow-sm .docutils}
:::: {.sd-card-body .rocm-card-banner .rocm-hue-7 .docutils}
::: {.sd-card-title .sd-font-weight-bold .docutils}

- [[RCCL]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rccl/en/docs-6.4.0/index.html "(in RCCL Documentation v2.22.3)"){.reference .external}

- [rocSHMEM]{.xref .std .std-doc}

:::::: {.sd-col .sd-d-flex-row .docutils}
::::: {.sd-card .sd-sphinx-override .sd-w-100 .sd-shadow-sm .docutils}
:::: {.sd-card-body .rocm-card-banner .rocm-hue-6 .docutils}
::: {.sd-card-title .sd-font-weight-bold .docutils}
Math

- - [[hipBLAS]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/hipBLAS/en/docs-6.4.0/index.html "(in hipBLAS Documentation v2.4.0)"){.reference .external} / [[rocBLAS]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocBLAS/en/docs-6.4.0/index.html "(in rocBLAS Documentation v4.4.0)"){.reference .external}

- [[hipBLASLt]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/hipBLASLt/en/docs-6.4.0/index.html "(in hipBLASLt Documentation v0.12.0)"){.reference .external}

- [[hipFFT]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/hipFFT/en/docs-6.4.0/index.html "(in hipFFT Documentation v1.0.18)"){.reference .external} / [[rocFFT]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocFFT/en/docs-6.4.0/index.html "(in rocFFT Documentation v1.0.32)"){.reference .external}

- [[hipfort]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/hipfort/en/docs-6.4.0/index.html "(in hipfort Documentation v0.6.0)"){.reference .external}

- [[hipRAND]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/hipRAND/en/docs-6.4.0/index.html "(in hipRAND Documentation v2.12.0)"){.reference .external} / [[rocRAND]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocRAND/en/docs-6.4.0/index.html "(in rocRAND Documentation v3.3.0)"){.reference .external}

- [[hipSOLVER]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/hipSOLVER/en/docs-6.4.0/index.html "(in hipSOLVER Documentation v2.4.0)"){.reference .external} / [[rocSOLVER]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocSOLVER/en/docs-6.4.0/index.html "(in rocSOLVER Documentation v3.28.0)"){.reference .external}

- [[hipSPARSE]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/hipSPARSE/en/docs-6.4.0/index.html "(in hipSPARSE Documentation v3.2.0)"){.reference .external} / [[rocSPARSE]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocSPARSE/en/docs-6.4.0/index.html "(in rocSPARSE Documentation v3.4.0)"){.reference .external}

- [[hipSPARSELt]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/hipSPARSELt/en/docs-6.4.0/index.html "(in hipSPARSELt Documentation v0.2.3)"){.reference .external}

- [[rocALUTION]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocALUTION/en/docs-6.4.0/index.html "(in rocALUTION Documentation v3.2.2)"){.reference .external}

- [[rocWMMA]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocWMMA/en/docs-6.4.0/index.html "(in rocWMMA Documentation v1.7.0)"){.reference .external}

- [[Tensile]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/Tensile/en/docs-6.4.0/src/index.html "(in Tensile Documentation v4.43.0)"){.reference .external}
