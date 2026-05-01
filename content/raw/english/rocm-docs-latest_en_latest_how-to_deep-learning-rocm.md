---
title: "Deep learning frameworks for ROCm"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/deep-learning-rocm.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-01
---

::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

::::::::::::::::::::::::::::::: bd-content
:::::::::::::::::::::::::::::: bd-article-container
:::::::::: {.bd-header-article .d-print-none}
::::::::: {.header-article-items .header-article__inner}
::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}
:::

::: header-article-item
- [](../index.html){.nav-link aria-label="Home"}
- Deep\...
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
# Deep learning frameworks for ROCm

:::: {#print-main-content}
::: {#jb-print-toc}
:::
::::
:::::

::: {#searchbox}
:::

:::::::::::::: {#deep-learning-frameworks-for-rocm .section}
# Deep learning frameworks for ROCm[\#](#deep-learning-frameworks-for-rocm "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-03-31
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

Deep learning frameworks provide environments for machine learning, training, fine-tuning, inference, and performance optimization.

ROCm offers a complete ecosystem for developing and running deep learning applications efficiently. It also provides ROCm-compatible versions of popular frameworks and libraries, such as PyTorch, TensorFlow, JAX, and others.

The AMD ROCm organization actively contributes to open-source development and collaborates closely with framework organizations. This collaboration ensures that framework-specific optimizations effectively leverage AMD GPUs.

The table below summarizes information about ROCm-enabled deep learning frameworks. It includes details on ROCm compatibility and third-party tool support, installation steps and options, and links to GitHub resources. For a complete list of supported framework versions on ROCm, see the [[Compatibility matrix]{.doc}](../compatibility/compatibility-matrix.html){.reference .internal} topic.

::: pst-scrollable-table-container
+-------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+-------------------------------------------------+
| Framework                                                                                                   | Installation guide                                                                                                                                                                                    | Installation options     | GitHub                                          |
+=============================================================================================================+=======================================================================================================================================================================================================+==========================+=================================================+
| [[PyTorch]{.doc}](../compatibility/ml-compatibility/pytorch-compatibility.html){.reference .internal}       | [[link]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/pytorch-install.html "(in ROCm installation on Linux v7.2.2)"){.reference .external}    | - Docker image           | [](https://github.com/ROCm/pytorch)             |
|                                                                                                             |                                                                                                                                                                                                       |                          |                                                 |
|                                                                                                             |                                                                                                                                                                                                       | - Wheels package         |                                                 |
|                                                                                                             |                                                                                                                                                                                                       |                          |                                                 |
|                                                                                                             |                                                                                                                                                                                                       | - ROCm Base Docker image |                                                 |
|                                                                                                             |                                                                                                                                                                                                       |                          |                                                 |
|                                                                                                             |                                                                                                                                                                                                       | - Upstream Docker file   |                                                 |
+-------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+-------------------------------------------------+
| [[TensorFlow]{.doc}](../compatibility/ml-compatibility/tensorflow-compatibility.html){.reference .internal} | [[link]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/tensorflow-install.html "(in ROCm installation on Linux v7.2.2)"){.reference .external} | - Docker image           | [](https://github.com/ROCm/tensorflow-upstream) |
|                                                                                                             |                                                                                                                                                                                                       |                          |                                                 |
|                                                                                                             |                                                                                                                                                                                                       | - Wheels package         |                                                 |
+-------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+-------------------------------------------------+
| [[JAX]{.doc}](../compatibility/ml-compatibility/jax-compatibility.html){.reference .internal}               | [[link]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/jax-install.html "(in ROCm installation on Linux v7.2.2)"){.reference .external}        | - Docker image           | [](https://github.com/ROCm/jax)                 |
+-------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+-------------------------------------------------+
| [[DGL]{.doc}](../compatibility/ml-compatibility/dgl-compatibility.html){.reference .internal}               | [[link]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/dgl-install.html "(in ROCm installation on Linux v7.2.2)"){.reference .external}        | - Docker image           | [](https://github.com/ROCm/dgl)                 |
+-------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+-------------------------------------------------+
:::

Learn how to use your ROCm deep learning environment for training, fine-tuning, inference, and performance optimization through the following guides.

- [[Use ROCm for AI]{.doc}](rocm-for-ai/index.html){.reference .internal}

- [[Use ROCm for training]{.doc}](rocm-for-ai/training/index.html){.reference .internal}

- [[Use ROCm for fine-tuning LLMs]{.doc}](rocm-for-ai/fine-tuning/index.html){.reference .internal}

- [[Use ROCm for AI inference]{.doc}](rocm-for-ai/inference/index.html){.reference .internal}

- [[Use ROCm for AI inference optimization]{.doc}](rocm-for-ai/inference-optimization/index.html){.reference .internal}

::: {.toctree-wrapper .compound}
:::
::::::::::::::

::::: prev-next-area
[](../compatibility/compatibility-matrix.html "previous page"){.left-prev}

::: prev-next-info
previous

Compatibility matrix
:::

[](../compatibility/ml-compatibility/pytorch-compatibility.html "next page"){.right-next}

::: prev-next-info
next

PyTorch compatibility
:::
:::::
::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::
