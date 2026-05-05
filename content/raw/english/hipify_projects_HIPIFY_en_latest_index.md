---
title: "HIPIFY documentation"
source_url: "https://rocm.docs.amd.com/projects/HIPIFY/en/latest/index.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-03
---

::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

::::::::::::::::::::::::::::::::::::: bd-content
:::::::::::::::::::::::::::::::::::: bd-article-container
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
# HIPIFY documentation

:::: {#print-main-content}
::: {#jb-print-toc}
:::
::::
:::::

::: {#searchbox}
:::

:::::::::::::::::::::: {#hipify-documentation .section}
[]{#index}

# HIPIFY documentation[\#](#hipify-documentation "Link to this heading"){.headerlink}

HIPIFY is a ROCm tool to help developers migrate GPU programming from NVIDIA's CUDA language to AMD's HIP C++ programming language for use on AMD GPUs. HIPIFY includes two tools offering different levels of capability:

- [`hipify-clang`{.docutils .literal .notranslate}]{.pre}: A clang-based tool that parses CUDA code and converts it to HIP code. It handles syntax changes, API calls, and kernel launch differences.

- [`hipify-perl`{.docutils .literal .notranslate}]{.pre}: A simpler tool generated from [`hipify-clang`{.docutils .literal .notranslate}]{.pre} that replaces CUDA API calls with HIP equivalents for basic code translation needs. [`hipify-perl`{.docutils .literal .notranslate}]{.pre} is useful for simple CUDA programs, but offers less error detection when running into issues during translation.

::: {.admonition .note}
Note

[hipify_torch](https://github.com/ROCm/hipify_torch){.reference .external} is a related tool that also translates CUDA source code into portable HIP C++. It was developed as part of the PyTorch project to cater to the project's unique requirements, was found to be useful for PyTorch-related projects, and released as an independent utility.
:::

HIPIFY does not automatically convert all CUDA code into HIP code seamlessly. While it is a powerful tool for translating CUDA code to HIP, there are some limitations and areas where manual intervention is often required. HIPIFY can automatically convert many CUDA runtime API calls, kernel launch syntax, standard CUDA library functions where there is a HIP library equivalent, specific keywords like [`__global__`{.docutils .literal .notranslate}]{.pre} and [`__device__`{.docutils .literal .notranslate}]{.pre}. However, HIP is not a complete replacement for CUDA, and HIPIFY cannot automatically translate all code. CUDA libraries, or third-party libraries that have no HIP equivalent cannot be translated. In addition, code which is optimized for performance on NVIDIA GPUs might require additional rework to optimize performance on AMD GPUs.

After migrating code through HIPIFY, you should perform a code review to ensure functional correctness, replace any unsupported libraries or constructs with HIP or ROCm features. Debug and test the new HIP program, and optimize the performance on the target AMD GPUs.

HIPIFY is open-source and freely available as part of the ROCm ecosystem. You can find the HIPIFY code on AMD's [GitHub HIPIFY repository](https://github.com/ROCm/HIPIFY){.reference .external}.

The documentation is structured as follows:

:::::::::::::::: {.sd-container-fluid .sd-sphinx-override .sd-mb-4 .docutils}
::::::::::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-2 .sd-row-cols-md-2 .sd-row-cols-lg-2 .sd-g-3 .sd-g-xs-3 .sd-g-sm-3 .sd-g-md-3 .sd-g-lg-3 .docutils}
:::::: {.sd-col .sd-d-flex-row .docutils}
::::: {.sd-card .sd-sphinx-override .sd-w-100 .sd-shadow-sm .docutils}
:::: {.sd-card-body .docutils}
::: {.sd-card-title .sd-font-weight-bold .docutils}
Building
:::

- [[Building hipify-clang on Linux]{.doc}](building/build-hipify-clang-linux.html){.reference .internal}

- [[Building hipify-clang on Windows]{.doc}](building/build-hipify-clang-windows.html){.reference .internal}

- [[Building hipify-perl]{.doc}](building/build-hipify-perl.html){.reference .internal}
::::
:::::
::::::

:::::: {.sd-col .sd-d-flex-row .docutils}
::::: {.sd-card .sd-sphinx-override .sd-w-100 .sd-shadow-sm .docutils}
:::: {.sd-card-body .docutils}
::: {.sd-card-title .sd-font-weight-bold .docutils}
How to
:::

- [[Use hipify-clang]{.doc}](how-to/hipify-clang.html){.reference .internal}

- [[Use hipify-perl]{.doc}](how-to/hipify-perl.html){.reference .internal}
::::
:::::
::::::

:::::: {.sd-col .sd-d-flex-row .docutils}
::::: {.sd-card .sd-sphinx-override .sd-w-100 .sd-shadow-sm .docutils}
:::: {.sd-card-body .docutils}
::: {.sd-card-title .sd-font-weight-bold .docutils}
API reference
:::

- [[hipify-clang commands]{.doc}](reference/hipify-clang-cmd.html){.reference .internal}

- [[hipify-perl commands]{.doc}](reference/hipify-perl-cmd.html){.reference .internal}

- [[Supported APIs]{.doc}](reference/supported_apis.html){.reference .internal}

- [[HIP supported APIs]{.doc}](reference/hip_supported_apis.html){.reference .internal}

- [[ROC supported APIs]{.doc}](reference/roc_supported_apis.html){.reference .internal}

- [[HIP and ROC supported APIs]{.doc}](reference/hip_roc_supported_apis.html){.reference .internal}
::::
:::::
::::::
:::::::::::::::
::::::::::::::::

To contribute to the documentation, refer to [Contributing to ROCm](https://rocm.docs.amd.com/en/latest/contribute/contributing.html){.reference .external}.

You can find licensing information on the [Licensing](https://rocm.docs.amd.com/en/latest/about/license.html){.reference .external} page.

::: {.toctree-wrapper .compound}
:::

::: {.toctree-wrapper .compound}
:::

::: {.toctree-wrapper .compound}
:::

::: {.toctree-wrapper .compound}
:::
::::::::::::::::::::::

:::: prev-next-area
[](building/build-hipify-clang-linux.html "next page"){.right-next}

::: prev-next-info
next

Building hipify-clang on Linux
:::
::::
::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::
