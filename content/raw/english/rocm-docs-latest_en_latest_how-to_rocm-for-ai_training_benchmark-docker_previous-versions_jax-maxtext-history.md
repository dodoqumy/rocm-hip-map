---
title: "JAX MaxText training performance testing version history"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/training/benchmark-docker/previous-versions/jax-maxtext-history.html"
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
- JAX MaxText\...
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
# JAX MaxText training performance testing version history

:::: {#print-main-content}
::: {#jb-print-toc}
:::
::::
:::::

::: {#searchbox}
:::

::::::::::::: {#jax-maxtext-training-performance-testing-version-history .section}
# JAX MaxText training performance testing version history[\#](#jax-maxtext-training-performance-testing-version-history "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-02-24
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 3 min read time
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

This table lists previous versions of the ROCm JAX MaxText Docker image for training performance testing. For detailed information about available models for benchmarking, see the version-specific documentation. You can find tagged previous releases of the [`ROCm/jax-training`{.docutils .literal .notranslate}]{.pre} Docker image on [Docker Hub](https://hub.docker.com/r/rocm/jax-training/tags){.reference .external}.

::: pst-scrollable-table-container
+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Image version         | Components            | Resources                                                                                                                                                                                             |
+=======================+=======================+=======================================================================================================================================================================================================+
| 26.2 (latest)         | - ROCm 7.1.1          | - [[Documentation]{.doc}](../jax-maxtext.html){.reference .internal}                                                                                                                                  |
|                       |                       |                                                                                                                                                                                                       |
|                       | - JAX 0.8.2           | - [Docker Hub](https://hub.docker.com/layers/rocm/jax-training/maxtext-v26.2/images/sha256-a89643388487b1e2fc6b6ef7bd3c44378c05d217309c977a1c18c72d05ebcaeb){.reference .external}                    |
+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 26.1                  | - ROCm 7.1.1          | - [[Documentation]{.doc}](jax-maxtext-v26.1.html){.reference .internal}                                                                                                                               |
|                       |                       |                                                                                                                                                                                                       |
|                       | - JAX 0.8.2           | - [Docker Hub](https://hub.docker.com/layers/rocm/jax-training/maxtext-v26.1/images/sha256-901083bde353fe6362ada3036e452c792b2c96124e5900f4e9b5946c02ff9d6a){.reference .external}                    |
+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 25.11                 | - ROCm 7.1.0          | - [[Documentation]{.doc}](jax-maxtext-v25.11.html){.reference .internal}                                                                                                                              |
|                       |                       |                                                                                                                                                                                                       |
|                       | - JAX 0.7.1           | - [Docker Hub](https://hub.docker.com/layers/rocm/jax-training/maxtext-v25.11/images/sha256-18e4d8f0b8ce7a7422c58046940dd5f32249960449fca09a562b65fb8eb1562a){.reference .external}                   |
+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 25.9.1                | - ROCm 7.0.0          | - [[Documentation]{.doc}](jax-maxtext-v25.9.html){.reference .internal}                                                                                                                               |
|                       |                       |                                                                                                                                                                                                       |
|                       | - JAX 0.6.2           | - [Docker Hub (25.9.1)](https://hub.docker.com/layers/rocm/jax-training/maxtext-v25.9.1/images/sha256-60946cfbd470f6ee361fc9da740233a4fb2e892727f01719145b1f7627a1cff6){.reference .external}         |
|                       |                       |                                                                                                                                                                                                       |
|                       |                       | - [Docker Hub (25.9)](https://hub.docker.com/layers/rocm/jax-training/maxtext-v25.9/images/sha256-4bb16ab58279ef09cb7a5e362c38e3fe3f901de44d8dbac5d0cb3bac5686441e){.reference .external}             |
+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 25.7                  | - ROCm 6.4.1          | - [[Documentation]{.doc}](jax-maxtext-v25.7.html){.reference .internal}                                                                                                                               |
|                       |                       |                                                                                                                                                                                                       |
|                       | - JAX 0.6.0, 0.5.0    | - [Docker Hub (JAX 0.6.0)](https://hub.docker.com/layers/rocm/jax-training/maxtext-v25.7-jax060/images/sha256-7352212ae033a76dca2b9dceffc23c1b5f1a61a7a560082cf747a9bf1acfc9ce){.reference .external} |
|                       |                       |                                                                                                                                                                                                       |
|                       |                       | - [Docker Hub (JAX 0.5.0)](https://hub.docker.com/layers/rocm/jax-training/maxtext-v25.7/images/sha256-45f4c727d4019a63fc47313d3a5f5a5105569539294ddfd2d742218212ae9025){.reference .external}        |
+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 25.5                  | - ROCm 6.3.4          | - [[Documentation]{.doc}](jax-maxtext-v25.5.html){.reference .internal}                                                                                                                               |
|                       |                       |                                                                                                                                                                                                       |
|                       | - JAX 0.4.35          | - [Docker Hub](https://hub.docker.com/layers/rocm/jax-training/maxtext-v25.5/images/sha256-4e0516358a227cae8f552fb866ec07e2edcf244756f02e7b40212abfbab5217b){.reference .external}                    |
+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 25.4                  | - ROCm 6.3.0          | - [[Documentation]{.doc}](jax-maxtext-v25.4.html){.reference .internal}                                                                                                                               |
|                       |                       |                                                                                                                                                                                                       |
|                       | - JAX 0.4.31          | - [Docker Hub](https://hub.docker.com/layers/rocm/jax-training/maxtext-v25.4/images/sha256-fb3eb71cd74298a7b3044b7130cf84113f14d518ff05a2cd625c11ea5f6a7b01){.reference .external}                    |
+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
:::
:::::::::::::

::: prev-next-area
:::
:::::::::::::::::::::::::::
::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::
