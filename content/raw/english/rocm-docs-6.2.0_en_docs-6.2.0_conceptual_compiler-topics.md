---
title: "Using compiler features"
source_url: "https://rocm.docs.amd.com/en/docs-6.2.0/conceptual/compiler-topics.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T16:23:29.297404+00:00
content_hash: "4dbdd86a731e44e8"
---

---
description: AMD ROCm documentation
keywords: documentation, guides, installation, compatibility, support, reference, ROCm, AMD
readthedocs-http-status: 200
readthedocs-project-slug: advanced-micro-devices-demo
readthedocs-resolver-filename: /conceptual/compiler-topics.html
readthedocs-version-slug: docs-6.2.0
---

::: sbt-scroll-pixel-helper

::::::::::::::::::::::::::: bd-content
:::::::::::::::::::::::::: bd-article-container
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
# Using compiler features

:::: {#print-main-content}
::: {#jb-print-toc}

::: {#searchbox}

::::::::::::: {#using-compiler-features .section .tex2jax_ignore .mathjax_ignore}
# Using compiler features[\#](#using-compiler-features "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils style="color:gray;"}
Applies to Linux and Windows

:::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
:::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij48cGF0aCBkPSJNNC43NSAwYS43NS43NSAwIDAxLjc1Ljc1VjJoNVYuNzVhLjc1Ljc1IDAgMDExLjUgMFYyaDEuMjVjLjk2NiAwIDEuNzUuNzg0IDEuNzUgMS43NXYxMC41QTEuNzUgMS43NSAwIDAxMTMuMjUgMTZIMi43NUExLjc1IDEuNzUgMCAwMTEgMTQuMjVWMy43NUMxIDIuNzg0IDEuNzg0IDIgMi43NSAySDRWLjc1QS43NS43NSAwIDAxNC43NSAwem0wIDMuNWg4LjVhLjI1LjI1IDAgMDEuMjUuMjVWNmgtMTFWMy43NWEuMjUuMjUgMCAwMS4yNS0uMjVoMnptLTIuMjUgNHY2Ljc1YzAgLjEzOC4xMTIuMjUuMjUuMjVoMTAuNWEuMjUuMjUgMCAwMC4yNS0uMjVWNy41aC0xMXoiIGZpbGwtcnVsZT0iZXZlbm9kZCIgLz48L3N2Zz4=){.sd-octicon .sd-octicon-calendar}]{.sd-pr-2}2024-07-04

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij48cGF0aCBkPSJNMS41IDhhNi41IDYuNSAwIDExMTMgMCA2LjUgNi41IDAgMDEtMTMgMHpNOCAwYTggOCAwIDEwMCAxNkE4IDggMCAwMDggMHptLjUgNC43NWEuNzUuNzUgMCAwMC0xLjUgMHYzLjVhLjc1Ljc1IDAgMDAuNDcxLjY5NmwyLjUgMWEuNzUuNzUgMCAwMC41NTctMS4zOTJMOC41IDcuNzQyVjQuNzV6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+PC9zdmc+){.sd-octicon .sd-octicon-clock}]{.sd-pr-2}3 min read time

The following topics describe using specific features of the compilation tools:

- [ROCm compiler infrastructure](https://rocm.docs.amd.com/projects/llvm-project/en/latest/index.html){.reference .external}

- [Using AddressSanitizer](https://rocm.docs.amd.com/projects/llvm-project/en/latest/conceptual/using-gpu-sanitizer.html){.reference .external}

- [OpenMP support](https://rocm.docs.amd.com/projects/llvm-project/en/latest/conceptual/openmp.html){.reference .external}

::: {.toctree-wrapper .compound}
