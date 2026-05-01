---
title: "vLLM inference performance testing version history"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference/benchmark-docker/previous-versions/vllm-history.html"
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
- vLLM\...
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
# vLLM inference performance testing version history

:::: {#print-main-content}
::: {#jb-print-toc}
:::
::::
:::::

::: {#searchbox}
:::

::::::::::::: {#vllm-inference-performance-testing-version-history .section}
# vLLM inference performance testing version history[\#](#vllm-inference-performance-testing-version-history "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 4 min read time
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

This table lists previous versions of the ROCm vLLM inference Docker image for inference performance testing. For detailed information about available models for benchmarking, see the version-specific documentation. You can find tagged previous releases of the [`ROCm/vllm`{.docutils .literal .notranslate}]{.pre} Docker image on [Docker Hub](https://hub.docker.com/r/rocm/vllm/tags){.reference .external}.

::: pst-scrollable-table-container
+----------------------------------------------------------------------------------------------------+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Docker image tag                                                                                   | Components               | Resources                                                                                                                                                                                                  |
+====================================================================================================+==========================+============================================================================================================================================================================================================+
| [`rocm/vllm:rocm7.0.0_vllm_0.11.2_20251210`{.docutils .literal .notranslate}]{.pre}                | - ROCm 7.0.0             | - [[Documentation]{.doc}](../vllm.html){.reference .internal}                                                                                                                                              |
|                                                                                                    |                          |                                                                                                                                                                                                            |
|                                                                                                    | - vLLM 0.11.2            | - [Docker Hub](https://hub.docker.com/layers/rocm/vllm/rocm7.0.0_vllm_0.11.2_20251210/images/sha256-e7f02dd2ce3824959658bc0391296f6158638e3ebce164f6c019c4eca8150ec7){.reference .external}                |
|                                                                                                    |                          |                                                                                                                                                                                                            |
|                                                                                                    | - PyTorch 2.9.0          |                                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`rocm/vllm:rocm7.0.0_vllm_0.11.1_20251103`{.docutils .literal .notranslate}]{.pre}                | - ROCm 7.0.0             | - [[Documentation]{.doc}](vllm-0.11.1-20251103.html){.reference .internal}                                                                                                                                 |
|                                                                                                    |                          |                                                                                                                                                                                                            |
|                                                                                                    | - vLLM 0.11.1            | - [Docker Hub](https://hub.docker.com/layers/rocm/vllm/rocm7.0.0_vllm_0.11.1_20251103/images/sha256-8d60429043d4d00958da46039a1de0d9b82df814d45da482497eef26a6076506){.reference .external}                |
|                                                                                                    |                          |                                                                                                                                                                                                            |
|                                                                                                    | - PyTorch 2.9.0          |                                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006`{.docutils .literal .notranslate}]{.pre}                | - ROCm 7.0.0             | - [[Documentation]{.doc}](vllm-0.10.2-20251006.html){.reference .internal}                                                                                                                                 |
|                                                                                                    |                          |                                                                                                                                                                                                            |
|                                                                                                    | - vLLM 0.10.2            | - [Docker Hub](https://hub.docker.com/layers/rocm/vllm/rocm7.0.0_vllm_0.10.2_20251006/images/sha256-94fd001964e1cf55c3224a445b1fb5be31a7dac302315255db8422d813edd7f5){.reference .external}                |
|                                                                                                    |                          |                                                                                                                                                                                                            |
|                                                                                                    | - PyTorch 2.9.0          |                                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`rocm/vllm:rocm6.4.1_vllm_0.10.1_20250909`{.docutils .literal .notranslate}]{.pre}                | - ROCm 6.4.1             | - [[Documentation]{.doc}](vllm-0.10.1-20250909.html){.reference .internal}                                                                                                                                 |
|                                                                                                    |                          |                                                                                                                                                                                                            |
|                                                                                                    | - vLLM 0.10.1            | - [Docker Hub](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.10.1_20250909/images/sha256-1113268572e26d59b205792047bea0e61e018e79aeadceba118b7bf23cb3715c){.reference .external}                |
|                                                                                                    |                          |                                                                                                                                                                                                            |
|                                                                                                    | - PyTorch 2.7.0          |                                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`rocm/vllm:rocm6.4.1_vllm_0.10.0_20250812`{.docutils .literal .notranslate}]{.pre}                | - ROCm 6.4.1             | - [[Documentation]{.doc}](vllm-0.10.0-20250812.html){.reference .internal}                                                                                                                                 |
|                                                                                                    |                          |                                                                                                                                                                                                            |
|                                                                                                    | - vLLM 0.10.0            | - [Docker Hub](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.10.0_20250812/images/sha256-4c277ad39af3a8c9feac9b30bf78d439c74d9b4728e788a419d3f1d0c30cacaa){.reference .external}                |
|                                                                                                    |                          |                                                                                                                                                                                                            |
|                                                                                                    | - PyTorch 2.7.0          |                                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`rocm/vllm:rocm6.4.1_vllm_0.9.1_20250715`{.docutils .literal .notranslate}]{.pre}                 | - ROCm 6.4.1             | - [[Documentation]{.doc}](vllm-0.9.1-20250715.html){.reference .internal}                                                                                                                                  |
|                                                                                                    |                          |                                                                                                                                                                                                            |
|                                                                                                    | - vLLM 0.9.1             | - [Docker Hub](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.9.1_20250715/images/sha256-4a429705fa95a58f6d20aceab43b1b76fa769d57f32d5d28bd3f4e030e2a78ea){.reference .external}                 |
|                                                                                                    |                          |                                                                                                                                                                                                            |
|                                                                                                    | - PyTorch 2.7.0          |                                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`rocm/vllm:rocm6.4.1_vllm_0.9.1_20250702`{.docutils .literal .notranslate}]{.pre}                 | - ROCm 6.4.1             | - [[Documentation]{.doc}](vllm-0.9.1-20250702.html){.reference .internal}                                                                                                                                  |
|                                                                                                    |                          |                                                                                                                                                                                                            |
|                                                                                                    | - vLLM 0.9.1             | - [Docker Hub](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.9.1_20250702/images/sha256-45068a2079cb8df554ed777141bf0c67d6627c470a897256e60c9f262677faab){.reference .external}                 |
|                                                                                                    |                          |                                                                                                                                                                                                            |
|                                                                                                    | - PyTorch 2.7.0          |                                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605`{.docutils .literal .notranslate}]{.pre}               | - ROCm 6.4.1             | - [[Documentation]{.doc}](vllm-0.9.0.1-20250605.html){.reference .internal}                                                                                                                                |
|                                                                                                    |                          |                                                                                                                                                                                                            |
|                                                                                                    | - vLLM 0.9.0.1           | - [Docker Hub](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.9.0.1_20250605/images/sha256-f48beeb3d72663a93c77211eb45273d564451447c097e060befa713d565fa36c){.reference .external}               |
|                                                                                                    |                          |                                                                                                                                                                                                            |
|                                                                                                    | - PyTorch 2.7.0          |                                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`rocm/vllm:rocm6.3.1_vllm_0.8.5_20250521`{.docutils .literal .notranslate}]{.pre}                 | - ROCm 6.3.1             | - [[Documentation]{.doc}](vllm-0.8.5-20250521.html){.reference .internal}                                                                                                                                  |
|                                                                                                    |                          |                                                                                                                                                                                                            |
|                                                                                                    | - 0.8.5 vLLM (0.8.6.dev) | - [Docker Hub](https://hub.docker.com/layers/rocm/vllm/rocm6.3.1_vllm_0.8.5_20250521/images/sha256-38410c51af7208897cd8b737c9bdfc126e9bc8952d4aa6b88c85482f03092a11){.reference .external}                 |
|                                                                                                    |                          |                                                                                                                                                                                                            |
|                                                                                                    | - PyTorch 2.7.0          |                                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`rocm/vllm:rocm6.3.1_vllm_0.8.5_20250513`{.docutils .literal .notranslate}]{.pre}                 | - ROCm 6.3.1             | - [[Documentation]{.doc}](vllm-0.8.5-20250513.html){.reference .internal}                                                                                                                                  |
|                                                                                                    |                          |                                                                                                                                                                                                            |
|                                                                                                    | - vLLM 0.8.5             | - [Docker Hub](https://hub.docker.com/layers/rocm/vllm/rocm6.3.1_vllm_0.8.5_20250513/images/sha256-5c8b4436dd0464119d9df2b44c745fadf81512f18ffb2f4b5dc235c71ebe26b4){.reference .external}                 |
|                                                                                                    |                          |                                                                                                                                                                                                            |
|                                                                                                    | - PyTorch 2.7.0          |                                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`rocm/vllm:rocm6.3.1_instinct_vllm0.8.3_20250415`{.docutils .literal .notranslate}]{.pre}         | - ROCm 6.3.1             | - [[Documentation]{.doc}](vllm-0.8.3-20250415.html){.reference .internal}                                                                                                                                  |
|                                                                                                    |                          |                                                                                                                                                                                                            |
|                                                                                                    | - vLLM 0.8.3             | - [Docker Hub](https://hub.docker.com/layers/rocm/vllm/rocm6.3.1_instinct_vllm0.8.3_20250415/images/sha256-ad9062dea3483d59dedb17c67f7c49f30eebd6eb37c3fac0a171fb19696cc845){.reference .external}         |
|                                                                                                    |                          |                                                                                                                                                                                                            |
|                                                                                                    | - PyTorch 2.7.0          |                                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`rocm/vllm:rocm6.3.1_instinct_vllm0.7.3_20250325`{.docutils .literal .notranslate}]{.pre}         | - ROCm 6.3.1             | - [[Documentation]{.doc}](vllm-0.7.3-20250325.html){.reference .internal}                                                                                                                                  |
|                                                                                                    |                          |                                                                                                                                                                                                            |
|                                                                                                    | - vLLM 0.7.3             | - [Docker Hub](https://hub.docker.com/layers/rocm/vllm/rocm6.3.1_instinct_vllm0.7.3_20250325/images/sha256-25245924f61750b19be6dcd8e787e46088a496c1fe17ee9b9e397f3d84d35640){.reference .external}         |
|                                                                                                    |                          |                                                                                                                                                                                                            |
|                                                                                                    | - PyTorch 2.7.0          |                                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`rocm/vllm:rocm6.3.1_mi300_ubuntu22.04_py3.12_vllm_0.6.6`{.docutils .literal .notranslate}]{.pre} | - ROCm 6.3.1             | - [[Documentation]{.doc}](vllm-0.6.6.html){.reference .internal}                                                                                                                                           |
|                                                                                                    |                          |                                                                                                                                                                                                            |
|                                                                                                    | - vLLM 0.6.6             | - [Docker Hub](https://hub.docker.com/layers/rocm/vllm/rocm6.3.1_mi300_ubuntu22.04_py3.12_vllm_0.6.6/images/sha256-9a12ef62bbbeb5a4c30a01f702c8e025061f575aa129f291a49fbd02d6b4d6c9){.reference .external} |
|                                                                                                    |                          |                                                                                                                                                                                                            |
|                                                                                                    | - PyTorch 2.7.0          |                                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`rocm/vllm:rocm6.2_mi300_ubuntu20.04_py3.9_vllm_0.6.4`{.docutils .literal .notranslate}]{.pre}    | - ROCm 6.2.1             | - [[Documentation]{.doc}](vllm-0.6.4.html){.reference .internal}                                                                                                                                           |
|                                                                                                    |                          |                                                                                                                                                                                                            |
|                                                                                                    | - vLLM 0.6.4             | - [Docker Hub](https://hub.docker.com/layers/rocm/vllm/rocm6.2_mi300_ubuntu20.04_py3.9_vllm_0.6.4/images/sha256-ccbb74cc9e7adecb8f7bdab9555f7ac6fc73adb580836c2a35ca96ff471890d8){.reference .external}    |
|                                                                                                    |                          |                                                                                                                                                                                                            |
|                                                                                                    | - PyTorch 2.5.0          |                                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`rocm/vllm:rocm6.2_mi300_ubuntu22.04_py3.9_vllm_7c5fd50`{.docutils .literal .notranslate}]{.pre}  | - ROCm 6.2.0             | - [[Documentation]{.doc}](vllm-0.4.3.html){.reference .internal}                                                                                                                                           |
|                                                                                                    |                          |                                                                                                                                                                                                            |
|                                                                                                    | - vLLM 0.4.3             | - [Docker Hub](https://hub.docker.com/layers/rocm/vllm/rocm6.2_mi300_ubuntu22.04_py3.9_vllm_7c5fd50/images/sha256-9e4dd4788a794c3d346d7d0ba452ae5e92d39b8dfac438b2af8efdc7f15d22c0){.reference .external}  |
|                                                                                                    |                          |                                                                                                                                                                                                            |
|                                                                                                    | - PyTorch 2.4.0          |                                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
:::
:::::::::::::

::: prev-next-area
:::
:::::::::::::::::::::::::::
::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::
