---
title: "PyTorch training performance testing version history"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/training/benchmark-docker/previous-versions/pytorch-training-history.html"
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
- PyTorch\...
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
# PyTorch training performance testing version history

:::: {#print-main-content}
::: {#jb-print-toc}
:::
::::
:::::

::: {#searchbox}
:::

::::::::::::: {#pytorch-training-performance-testing-version-history .section}
# PyTorch training performance testing version history[\#](#pytorch-training-performance-testing-version-history "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-03-25
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

This table lists previous versions of the ROCm PyTorch training Docker image for inference performance testing. For detailed information about available models for benchmarking, see the version-specific documentation. You can find tagged previous releases of the [`ROCm/primus`{.docutils .literal .notranslate}]{.pre} Docker image on [Docker Hub](https://hub.docker.com/r/rocm/pytorch-training/tags){.reference .external}.

::: pst-scrollable-table-container
+-----------------------+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Image version         | Components                                           | Resources                                                                                                                                                                            |
+=======================+======================================================+======================================================================================================================================================================================+
| v26.2 (latest)        | - ROCm 7.2.0                                         | - [[Primus PyTorch training documentation]{.doc}](../primus-pytorch.html){.reference .internal}                                                                                      |
|                       |                                                      |                                                                                                                                                                                      |
|                       | - PyTorch 2.10.0+git94c6e04                          | - [Docker Hub](https://hub.docker.com/layers/rocm/primus/v26.2/images/sha256-9148d1bfcd579bf92f44bd89090e0d8c958f149c134b4b34b9674ab559244585){.reference .external}                 |
+-----------------------+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v26.1                 | - ROCm 7.1.0                                         | - [[Primus PyTorch training documentation]{.doc}](primus-pytorch-v26.1.html){.reference .internal}                                                                                   |
|                       |                                                      |                                                                                                                                                                                      |
|                       | - PyTorch 2.10.0.dev20251112+rocm7.1                 | - [Docker Hub](https://hub.docker.com/layers/rocm/primus/v26.1/images/sha256-4fc8808bdb14117c6af7f38d79c809056e6fdbfd530c1fabbb61d097ddaf820d){.reference .external}                 |
+-----------------------+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v25.11                | - ROCm 7.1.0                                         | - [[Primus PyTorch training documentation]{.doc}](primus-pytorch-v25.11.html){.reference .internal}                                                                                  |
|                       |                                                      |                                                                                                                                                                                      |
|                       | - PyTorch 2.10.0.dev20251112+rocm7.1                 | - [[PyTorch training (legacy) documentation]{.doc}](pytorch-training-v25.11.html){.reference .internal}                                                                              |
|                       |                                                      |                                                                                                                                                                                      |
|                       |                                                      | - [Docker Hub](https://hub.docker.com/layers/rocm/primus/v25.11/images/sha256-71aa65a9bfc8e9dd18bce5b68c81caff864f223e9afa75dc1b719671a1f4a3c3){.reference .external}                |
+-----------------------+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v25.10                | - ROCm 7.1.0                                         | - [[Primus PyTorch training documentation]{.doc}](primus-pytorch-v25.10.html){.reference .internal}                                                                                  |
|                       |                                                      |                                                                                                                                                                                      |
|                       | - PyTorch 2.10.0.dev20251112+rocm7.1                 | - [[PyTorch training (legacy) documentation]{.doc}](pytorch-training-v25.10.html){.reference .internal}                                                                              |
|                       |                                                      |                                                                                                                                                                                      |
|                       |                                                      | - [Docker Hub](https://hub.docker.com/layers/rocm/primus/v25.10/images/sha256-140c37cd2eeeb183759b9622543fc03cc210dc97cbfa18eeefdcbda84420c197){.reference .external}                |
+-----------------------+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v25.9                 | - ROCm 7.0.0                                         | - [[Primus PyTorch training documentation]{.doc}](primus-pytorch-v25.9.html){.reference .internal}                                                                                   |
|                       |                                                      |                                                                                                                                                                                      |
|                       | - Primus 0.3.0                                       | - [[PyTorch training (legacy) documentation]{.doc}](pytorch-training-v25.9.html){.reference .internal}                                                                               |
|                       |                                                      |                                                                                                                                                                                      |
|                       | - PyTorch 2.9.0.dev20250821+rocm7.0.0.lw.git125803b7 | - [Docker Hub (gfx950)](https://hub.docker.com/layers/rocm/primus/v25.9_gfx950/images/sha256-1a198be32f49efd66d0ff82066b44bd99b3e6b04c8e0e9b36b2c481e13bff7b6){.reference .external} |
|                       |                                                      |                                                                                                                                                                                      |
|                       |                                                      | - [Docker Hub (gfx942)](https://hub.docker.com/layers/rocm/primus/v25.9_gfx942/images/sha256-df6ab8f45b4b9ceb100fb24e19b2019a364e351ee3b324dbe54466a1d67f8357){.reference .external} |
+-----------------------+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v25.8                 | - ROCm 6.4.3                                         | - [[Primus PyTorch training documentation]{.doc}](primus-pytorch-v25.8.html){.reference .internal}                                                                                   |
|                       |                                                      |                                                                                                                                                                                      |
|                       | - PyTorch 2.8.0a0+gitd06a406                         | - [[PyTorch training (legacy) documentation]{.doc}](pytorch-training-v25.8.html){.reference .internal}                                                                               |
|                       |                                                      |                                                                                                                                                                                      |
|                       |                                                      | - [Docker Hub](https://hub.docker.com/layers/rocm/pytorch-training/v25.8/images/sha256-5082ae01d73fec6972b0d84e5dad78c0926820dcf3c19f301d6c8eb892e573c5){.reference .external}       |
+-----------------------+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v25.7                 | - ROCm 6.4.2                                         | - [[Documentation]{.doc}](pytorch-training-v25.7.html){.reference .internal}                                                                                                         |
|                       |                                                      |                                                                                                                                                                                      |
|                       | - PyTorch 2.8.0a0+gitd06a406                         | - [Docker Hub](https://hub.docker.com/layers/rocm/pytorch-training/v25.7/images/sha256-cc6fd840ab89cb81d926fc29eca6d075aee9875a55a522675a4b9231c9a0a712){.reference .external}       |
+-----------------------+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v25.6                 | - ROCm 6.3.4                                         | - [[Documentation]{.doc}](pytorch-training-v25.6.html){.reference .internal}                                                                                                         |
|                       |                                                      |                                                                                                                                                                                      |
|                       | - PyTorch 2.8.0a0+git7d205b2                         | - [Docker Hub](https://hub.docker.com/layers/rocm/pytorch-training/v25.6/images/sha256-a4cea3c493a4a03d199a3e81960ac071d79a4a7a391aa9866add3b30a7842661){.reference .external}       |
+-----------------------+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v25.5                 | - ROCm 6.3.4                                         | - [[Documentation]{.doc}](pytorch-training-v25.5.html){.reference .internal}                                                                                                         |
|                       |                                                      |                                                                                                                                                                                      |
|                       | - PyTorch 2.7.0a0+git637433                          | - [Docker Hub](https://hub.docker.com/layers/rocm/pytorch-training/v25.5/images/sha256-d47850a9b25b4a7151f796a8d24d55ea17bba545573f0d50d54d3852f96ecde5){.reference .external}       |
+-----------------------+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v25.4                 | - ROCm 6.3.0                                         | - [[Documentation]{.doc}](pytorch-training-v25.4.html){.reference .internal}                                                                                                         |
|                       |                                                      |                                                                                                                                                                                      |
|                       | - PyTorch 2.7.0a0+git637433                          | - [Docker Hub](https://hub.docker.com/layers/rocm/pytorch-training/v25.4/images/sha256-fa98a9aa69968e654466c06f05aaa12730db79b48b113c1ab4f7a5fe6920a20b){.reference .external}       |
+-----------------------+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v25.3                 | - ROCm 6.3.0                                         | - [[Documentation]{.doc}](pytorch-training-v25.3.html){.reference .internal}                                                                                                         |
|                       |                                                      |                                                                                                                                                                                      |
|                       | - PyTorch 2.7.0a0+git637433                          | - [Docker Hub](https://hub.docker.com/layers/rocm/pytorch-training/v25.3/images/sha256-0ffdde1b590fd2787b1c7adf5686875b100980b0f314090901387c44253e709b){.reference .external}       |
+-----------------------+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
:::
:::::::::::::

::: prev-next-area
:::
:::::::::::::::::::::::::::
::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::
