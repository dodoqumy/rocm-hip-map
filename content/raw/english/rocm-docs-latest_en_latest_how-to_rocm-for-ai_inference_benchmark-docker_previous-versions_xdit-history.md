---
title: "xDiT diffusion inference performance testing version history"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference/benchmark-docker/previous-versions/xdit-history.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-01
---

:::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

:::::::::::::::::::::::::::: bd-content
::::::::::::::::::::::::::: bd-article-container
:::::::::: {.bd-header-article .d-print-none}
::::::::: {.header-article-items .header-article__inner}
::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}
:::

::: header-article-item
- [](../../../../../index.html){.nav-link aria-label="Home"}
- xDiT\...
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
# xDiT diffusion inference performance testing version history

:::: {#print-main-content}
::: {#jb-print-toc}
:::
::::
:::::

::: {#searchbox}
:::

::::::::::::: {#xdit-diffusion-inference-performance-testing-version-history .section}
# xDiT diffusion inference performance testing version history[\#](#xdit-diffusion-inference-performance-testing-version-history "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-04-08
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

This table lists previous versions of the ROCm xDiT diffusion inference performance testing environment. For detailed information about available models for benchmarking, see the version-specific documentation.

::: pst-scrollable-table-container
+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Docker image tag                                                            | Components                                                                                                          | Resources                                                                                                                                                                   |
+=============================================================================+=====================================================================================================================+=============================================================================================================================================================================+
| [`rocm/pytorch-xdit:v26.4`{.docutils .literal .notranslate}]{.pre} (latest) | - [ROCm 7.12.0 preview](https://rocm.docs.amd.com/en/7.12.0-preview/about/release-notes.html){.reference .external} | - [[Documentation]{.doc}](../../xdit-diffusion-inference.html){.reference .internal}                                                                                        |
|                                                                             |                                                                                                                     |                                                                                                                                                                             |
|                                                                             | - TheRock 9b611c6                                                                                                   | - [Docker Hub](https://hub.docker.com/layers/rocm/pytorch-xdit/v26.4/images/sha256-b4296a638eb8dc7ebcafc808e180b78a3c44177580c21986082ec9539496067c){.reference .external}  |
+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`rocm/pytorch-xdit:v26.3`{.docutils .literal .notranslate}]{.pre}          | - [ROCm 7.12.0 preview](https://rocm.docs.amd.com/en/7.12.0-preview/about/release-notes.html){.reference .external} | - [[Documentation]{.doc}](xdit-26.3.html){.reference .internal}                                                                                                             |
|                                                                             |                                                                                                                     |                                                                                                                                                                             |
|                                                                             | - TheRock e40a6da                                                                                                   | - [Docker Hub](https://hub.docker.com/layers/rocm/pytorch-xdit/v26.3/images/sha256-ac78a03d2911bf1b49c001d3be2e8bd745c1bc455cb49ae972825a7986880902){.reference .external}  |
+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`rocm/pytorch-xdit:v26.2`{.docutils .literal .notranslate}]{.pre}          | - [ROCm 7.11.0 preview](https://rocm.docs.amd.com/en/7.11.0-preview/about/release-notes.html){.reference .external} | - [[Documentation]{.doc}](xdit-26.2.html){.reference .internal}                                                                                                             |
|                                                                             |                                                                                                                     |                                                                                                                                                                             |
|                                                                             | - TheRock 1728a81                                                                                                   | - [Docker Hub](https://hub.docker.com/layers/rocm/pytorch-xdit/v26.2/images/sha256-e2c504af438bb9cf60e3869c499baa5102b3d3f62141b99c49743e755ae44008){.reference .external}  |
+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`rocm/pytorch-xdit:v26.1`{.docutils .literal .notranslate}]{.pre}          | - [ROCm 7.11.0 preview](https://rocm.docs.amd.com/en/7.11.0-preview/about/release-notes.html){.reference .external} | - [[Documentation]{.doc}](xdit-26.1.html){.reference .internal}                                                                                                             |
|                                                                             |                                                                                                                     |                                                                                                                                                                             |
|                                                                             | - TheRock 1728a81                                                                                                   | - [Docker Hub](https://hub.docker.com/layers/rocm/pytorch-xdit/v26.1/images/sha256-4e35ebcad47042a41389b992ecb3489b3b0a922e4c34c7a0dd1098733a3db513){.reference .external}  |
+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`rocm/pytorch-xdit:v25.13`{.docutils .literal .notranslate}]{.pre}         | - [ROCm 7.11.0 preview](https://rocm.docs.amd.com/en/7.11.0-preview/about/release-notes.html){.reference .external} | - [[Documentation]{.doc}](xdit-25.13.html){.reference .internal}                                                                                                            |
|                                                                             |                                                                                                                     |                                                                                                                                                                             |
|                                                                             | - TheRock 1728a81                                                                                                   | - [Docker Hub](https://hub.docker.com/layers/rocm/pytorch-xdit/v25.13/images/sha256-81954713070d67bde08595e03f62110c8a3dd66a9ae17a77d611e01f83f0f4ef){.reference .external} |
+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`rocm/pytorch-xdit:v25.12`{.docutils .literal .notranslate}]{.pre}         | - [ROCm 7.10.0 preview](https://rocm.docs.amd.com/en/7.10.0-preview/about/release-notes.html){.reference .external} | - [[Documentation]{.doc}](xdit-25.12.html){.reference .internal}                                                                                                            |
|                                                                             |                                                                                                                     |                                                                                                                                                                             |
|                                                                             | - TheRock 3e3f834                                                                                                   | - [Docker Hub](https://hub.docker.com/layers/rocm/pytorch-xdit/v25.12/images/sha256-e06895132316bf3c393366b70a91eaab6755902dad0100e6e2b38310547d9256){.reference .external} |
+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`rocm/pytorch-xdit:v25.11`{.docutils .literal .notranslate}]{.pre}         | - [ROCm 7.10.0 preview](https://rocm.docs.amd.com/en/7.10.0-preview/about/release-notes.html){.reference .external} | - [[Documentation]{.doc}](xdit-25.11.html){.reference .internal}                                                                                                            |
|                                                                             |                                                                                                                     |                                                                                                                                                                             |
|                                                                             | - TheRock 3e3f834                                                                                                   | - [Docker Hub](https://hub.docker.com/layers/rocm/pytorch-xdit/v25.11/images/sha256-c9fa659439bb024f854b4d5eea598347251b02c341c55f66c98110832bde4216){.reference .external} |
+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`rocm/pytorch-xdit:v25.10`{.docutils .literal .notranslate}]{.pre}         | - [ROCm 7.9.0 preview](https://rocm.docs.amd.com/en/7.9.0-preview/about/release-notes.html){.reference .external}   | - [[Documentation]{.doc}](xdit-25.10.html){.reference .internal}                                                                                                            |
|                                                                             |                                                                                                                     |                                                                                                                                                                             |
|                                                                             | - TheRock 7afbe45                                                                                                   | - [Docker Hub](https://hub.docker.com/layers/rocm/pytorch-xdit/v25.10/images/sha256-d79715ff18a9470e3f907cec8a9654d6b783c63370b091446acffc0de4d7070e){.reference .external} |
+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
:::
:::::::::::::

::: prev-next-area
:::
:::::::::::::::::::::::::::
::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::
