---
title: "ROCm documentation toolchain"
source_url: "https://rocm.docs.amd.com/en/latest/contribute/toolchain.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-01
---

:::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

:::::::::::::::::::::::::::::::::::::::::: bd-content
::::::::::::::::::::::::::::::::::::: bd-article-container
:::::::::: {.bd-header-article .d-print-none}
::::::::: {.header-article-items .header-article__inner}
::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}
:::

::: header-article-item
- [](../index.html){.nav-link aria-label="Home"}
- [Contributing to the ROCm documentation](contributing.html){.nav-link}
- ROCm\...
:::
:::::

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons
[]{.fa-solid .fa-list}
:::
::::
:::::
:::::::::
::::::::::

:::::: {#jb-print-docs-body .onlyprint}
# ROCm documentation toolchain

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [rocm-docs-core](#rocm-docs-core){.reference .internal .nav-link}
- [Sphinx](#sphinx){.reference .internal .nav-link}
  - [Sphinx External ToC](#sphinx-external-toc){.reference .internal .nav-link}
  - [Sphinx-book-theme](#sphinx-book-theme){.reference .internal .nav-link}
  - [Sphinx Design](#sphinx-design){.reference .internal .nav-link}
- [Doxygen](#doxygen){.reference .internal .nav-link}
- [Breathe](#breathe){.reference .internal .nav-link}
- [Read the Docs](#read-the-docs){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

:::::::::::::::::::: {#rocm-documentation-toolchain .section .tex2jax_ignore .mathjax_ignore}
# ROCm documentation toolchain[\#](#rocm-documentation-toolchain "Link to this heading"){.headerlink}

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
Applies to Linux and Windows
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
:::
:::::::
::::::::
:::::::::
::::::::::
:::::::::::

The ROCm documentation relies on several open source toolchains and sites.

::: {#rocm-docs-core .section}
## rocm-docs-core[\#](#rocm-docs-core "Link to this heading"){.headerlink}

[rocm-docs-core](https://github.com/ROCm/rocm-docs-core){.reference .external} is an AMD-maintained project that applies customizations for the ROCm documentation. This project is the tool most ROCm repositories use as part of their documentation build pipeline. It is available as a [pip package on PyPI](https://pypi.org/project/rocm-docs-core/){.reference .external}.

See the user and developer guides for rocm-docs-core at [[rocm-docs-core documentation]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocm-docs-core/en/latest/index.html "(in ROCm Docs Core v1.33.1)"){.reference .external}.
:::

:::::: {#sphinx .section}
## Sphinx[\#](#sphinx "Link to this heading"){.headerlink}

[Sphinx](https://www.sphinx-doc.org/en/master/){.reference .external} is a documentation generator originally used for Python. It is now widely used in the open source community.

::: {#sphinx-external-toc .section}
### Sphinx External ToC[\#](#sphinx-external-toc "Link to this heading"){.headerlink}

[Sphinx External ToC](https://sphinx-external-toc.readthedocs.io/en/latest/intro.html){.reference .external} is a Sphinx extension used for ROCm documentation navigation. This tool generates a navigation menu on the left based on a YAML file ([`_toc.yml.in`{.docutils .literal .notranslate}]{.pre}) that contains the table of contents.
:::

::: {#sphinx-book-theme .section}
### Sphinx-book-theme[\#](#sphinx-book-theme "Link to this heading"){.headerlink}

[Sphinx-book-theme](https://sphinx-book-theme.readthedocs.io/en/latest/){.reference .external} is a Sphinx theme that defines the base appearance for ROCm documentation. ROCm documentation applies some customization, such as a custom header and footer, on top of the Sphinx Book Theme.
:::

::: {#sphinx-design .section}
### Sphinx Design[\#](#sphinx-design "Link to this heading"){.headerlink}

[Sphinx design](https://sphinx-design.readthedocs.io/en/latest/index.html){.reference .external} is a Sphinx extension that adds design functionality. ROCm documentation uses Sphinx Design for grids, cards, and synchronized tabs.
:::
::::::

::: {#doxygen .section}
## Doxygen[\#](#doxygen "Link to this heading"){.headerlink}

[Doxygen](https://www.doxygen.nl/){.reference .external} is a documentation generator that extracts information from in-code comments. It is used for API documentation.
:::

::: {#breathe .section}
## Breathe[\#](#breathe "Link to this heading"){.headerlink}

[Breathe](https://www.breathe-doc.org/){.reference .external} is a Sphinx plugin for integrating Doxygen content.
:::

::: {#read-the-docs .section}
## Read the Docs[\#](#read-the-docs "Link to this heading"){.headerlink}

[Read the Docs](https://docs.readthedocs.io/en/stable/){.reference .external} is the service that builds and hosts the HTML version of the ROCm documentation.
:::
::::::::::::::::::::

::::: prev-next-area
[](contributing.html "previous page"){.left-prev}

::: prev-next-info
previous

Contributing to the ROCm documentation
:::

[](building.html "next page"){.right-next}

::: prev-next-info
next

Building documentation
:::
:::::
:::::::::::::::::::::::::::::::::::::

:::::: {.bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {.page-toc .tocsection .onthispage}
Contents
:::

- [rocm-docs-core](#rocm-docs-core){.reference .internal .nav-link}
- [Sphinx](#sphinx){.reference .internal .nav-link}
  - [Sphinx External ToC](#sphinx-external-toc){.reference .internal .nav-link}
  - [Sphinx-book-theme](#sphinx-book-theme){.reference .internal .nav-link}
  - [Sphinx Design](#sphinx-design){.reference .internal .nav-link}
- [Doxygen](#doxygen){.reference .internal .nav-link}
- [Breathe](#breathe){.reference .internal .nav-link}
- [Read the Docs](#read-the-docs){.reference .internal .nav-link}
::::
:::::
::::::
::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::
