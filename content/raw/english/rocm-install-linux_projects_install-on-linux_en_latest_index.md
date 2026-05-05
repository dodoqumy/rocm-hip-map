---
title: "ROCm installation for Linux"
source_url: "https://rocm.docs.amd.com/projects/install-on-linux/en/latest/index.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-03
---

:::::::::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

:::::::::::::::::::::::::::::::::::::::::::::::::::: bd-content
::::::::::::::::::::::::::::::::::::::::::::::::::: bd-article-container
::::::::: {.bd-header-article .d-print-none}
:::::::: {.header-article-items .header-article__inner}
:::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}
:::
::::

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons
:::
::::
:::::
::::::::
:::::::::

::::: {#jb-print-docs-body .onlyprint}
# ROCm installation for Linux

:::: {#print-main-content}
::: {#jb-print-toc}
:::
::::
:::::

::: {#searchbox}
:::

::::::::::::::::::::::::::::::::::::: {#rocm-installation-for-linux .section}
[]{#rocm-install-home}

# ROCm installation for Linux[\#](#rocm-installation-for-linux "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-04-17
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

This section describes the ROCm for Linux installation options.

::: {.admonition .note}
Note

- If you're using ROCm with AMD Radeon™ GPUs or Ryzen™ APUs for graphics workloads, see the [Use ROCm on Radeon and Ryzen](https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/index.html){.reference .external} documentation for installation instructions.

- The AMDGPU installer documentation has been removed to encourage the use of the package manager for ROCm installation. While the package manager is the recommended method, you can still install ROCm using the AMDGPU installer by following the [legacy process](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-6.4.1/install/install-methods/amdgpu-installer-index.html){.reference .external}. Ensure to update the command with the intended ROCm version before running it.
:::

:::::::::::: {.sd-container-fluid .sd-sphinx-override .sd-mb-4 .docutils}
::::::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-2 .sd-row-cols-md-2 .sd-row-cols-lg-2 .sd-g-3 .sd-g-xs-3 .sd-g-sm-3 .sd-g-md-3 .sd-g-lg-3 .docutils}
:::::: {.sd-col .sd-d-flex-row .docutils}
::::: {.sd-card .sd-sphinx-override .sd-w-100 .sd-shadow-sm .docutils}
:::: {.sd-card-body .docutils}
::: {.sd-card-title .sd-font-weight-bold .docutils}
Install ROCm
:::

- [[System requirements (Linux)]{.doc}](reference/system-requirements.html){.reference .internal}

- [[User and AMD GPU Driver (amdgpu) support matrix]{.doc}](reference/user-kernel-space-compat-matrix.html){.reference .internal}

- [[Quick start]{.doc}](install/quick-start.html){.reference .internal} - recommended for new users

- [[Detailed install]{.doc}](install/detailed-install.html){.reference .internal} - includes explanations
::::
:::::
::::::

:::::: {.sd-col .sd-d-flex-row .docutils}
::::: {.sd-card .sd-sphinx-override .sd-w-100 .sd-shadow-sm .docutils}
:::: {.sd-card-body .docutils}
::: {.sd-card-title .sd-font-weight-bold .docutils}
Install deep learning frameworks
:::

- [[PyTorch]{.doc}](install/3rd-party/pytorch-install.html){.reference .internal}

- [[TensorFlow]{.doc}](install/3rd-party/tensorflow-install.html){.reference .internal}

- [[JAX]{.doc}](install/3rd-party/jax-install.html){.reference .internal}

- [[DGL]{.doc}](install/3rd-party/dgl-install.html){.reference .internal}
::::
:::::
::::::
:::::::::::
::::::::::::

:::::::::::: {.sd-container-fluid .sd-sphinx-override .sd-mb-4 .docutils}
::::::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-2 .sd-row-cols-md-2 .sd-row-cols-lg-2 .sd-g-3 .sd-g-xs-3 .sd-g-sm-3 .sd-g-md-3 .sd-g-lg-3 .docutils}
:::::: {.sd-col .sd-d-flex-row .docutils}
::::: {.sd-card .sd-sphinx-override .sd-w-100 .sd-shadow-sm .docutils}
:::: {.sd-card-body .docutils}
::: {.sd-card-title .sd-font-weight-bold .docutils}
How to
:::

- [[Run Docker containers]{.doc}](how-to/docker.html){.reference .internal}

- [[Use Spack]{.doc}](how-to/spack.html){.reference .internal}
::::
:::::
::::::

:::::: {.sd-col .sd-d-flex-row .docutils}
::::: {.sd-card .sd-sphinx-override .sd-w-100 .sd-shadow-sm .docutils}
:::: {.sd-card-body .docutils}
::: {.sd-card-title .sd-font-weight-bold .docutils}
Reference
:::

- [[Package details]{.doc}](reference/package-manager-integration.html){.reference .internal}

- [[Troubleshooting]{.doc}](reference/install-faq.html){.reference .internal}
::::
:::::
::::::
:::::::::::
::::::::::::

::: {.toctree-wrapper .compound}
:::

::: {.toctree-wrapper .compound}
:::

::: {.toctree-wrapper .compound}
:::

::: {.toctree-wrapper .compound}
:::
:::::::::::::::::::::::::::::::::::::

:::: prev-next-area
[](reference/system-requirements.html "next page"){.right-next}

::: prev-next-info
next

System requirements (Linux)
:::
::::
:::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::
