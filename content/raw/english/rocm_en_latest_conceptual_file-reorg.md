---
title: "ROCm Linux Filesystem Hierarchy Standard reorganization"
source_url: "https://rocm.docs.amd.com/en/latest/conceptual/file-reorg.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-03
---

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-content
::::::::::::::::::::::::::::::::::::::::::::::::::: bd-article-container
:::::::::: {.bd-header-article .d-print-none}
::::::::: {.header-article-items .header-article__inner}
::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}
:::

::: header-article-item
- [](../index.html){.nav-link aria-label="Home"}
- ROCm Linux\...
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
# ROCm Linux Filesystem Hierarchy Standard reorganization

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [Introduction](#introduction){.reference .internal .nav-link}
- [Adopting the FHS](#adopting-the-fhs){.reference .internal .nav-link}
- [Changes from earlier ROCm versions](#changes-from-earlier-rocm-versions){.reference .internal .nav-link}
- [ROCm FHS reorganization: backward compatibility](#rocm-fhs-reorganization-backward-compatibility){.reference .internal .nav-link}
  - [Wrapper header files](#wrapper-header-files){.reference .internal .nav-link}
  - [Executable files](#executable-files){.reference .internal .nav-link}
  - [Library files](#library-files){.reference .internal .nav-link}
  - [CMake config files](#cmake-config-files){.reference .internal .nav-link}
- [Changes required in applications using ROCm](#changes-required-in-applications-using-rocm){.reference .internal .nav-link}
- [Changes in versioning specifications](#changes-in-versioning-specifications){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

:::::::::::::::::::::::::::::::::: {#rocm-linux-filesystem-hierarchy-standard-reorganization .section .tex2jax_ignore .mathjax_ignore}
# ROCm Linux Filesystem Hierarchy Standard reorganization[\#](#rocm-linux-filesystem-hierarchy-standard-reorganization "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 7 min read time
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

::: {#introduction .section}
## Introduction[\#](#introduction "Link to this heading"){.headerlink}

The ROCm Software has adopted the Linux Filesystem Hierarchy Standard (FHS) [https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html){.reference .external} in order to to ensure ROCm is consistent with standard open source conventions. The following sections specify how current and future releases of ROCm adhere to FHS, how the previous ROCm file system is supported, and how improved versioning specifications are applied to ROCm.
:::

::::: {#adopting-the-fhs .section}
## Adopting the FHS[\#](#adopting-the-fhs "Link to this heading"){.headerlink}

In order to standardize ROCm directory structure and directory content layout ROCm has adopted the [FHS](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html){.reference .external}, adhering to open source conventions for Linux-based distribution. FHS ensures internal consistency within the ROCm stack, as well as external consistency with other systems and distributions. The ROCm proposed file structure is outlined below:

:::: {.highlight-none .notranslate}
::: highlight
    /opt/rocm-<ver>
        | -- bin
             | -- all public binaries
        | -- lib
             | -- lib<soname>.so->lib<soname>.so.major->lib<soname>.so.major.minor.patch
                  (public libaries to link with applications)
             | -- <component>
                  | -- architecture dependent libraries and binaries used internally by components
             | -- cmake
                  | -- <component>
                       | --<component>-config.cmake
        | -- libexec
             | -- <component>
                  | -- non ISA/architecture independent executables used internally by components
        | -- include
             | -- <component>
                  | -- public header files
        | -- share
             | -- html
                  | -- <component>
                       | -- html documentation
             | -- info
                  | -- <component>
                       | -- info files
             | -- man
                  | -- <component>
                       | -- man pages
             | -- doc
                  | -- <component>
                       | -- license files
             | -- <component>
                  | -- samples
                  | -- architecture independent misc files
:::
::::
:::::

::::: {#changes-from-earlier-rocm-versions .section}
## Changes from earlier ROCm versions[\#](#changes-from-earlier-rocm-versions "Link to this heading"){.headerlink}

The following table provides a brief overview of the new ROCm FHS layout, compared to the layout of earlier ROCm versions. Note that /opt/ is used to denote the default rocm-installation-path and should be replaced in case of a non-standard installation location of the ROCm distribution.

:::: {.highlight-none .notranslate}
::: highlight
     ______________________________________________________
    |  New ROCm Layout            |  Previous ROCm Layout  |
    |_____________________________|________________________|
    | /opt/rocm-<ver>             | /opt/rocm-<ver>        |
    |     | -- bin                |     | -- bin           |
    |     | -- lib                |     | -- lib           |
    |          | -- cmake         |     | -- include       |
    |     | -- libexec            |     | -- <component_1> |
    |     | -- include            |          | -- bin      |
    |          | -- <component_1> |          | -- cmake    |
    |     | -- share              |          | -- doc      |
    |          | -- html          |          | -- lib      |
    |          | -- info          |          | -- include  |
    |          | -- man           |          | -- samples  |
    |          | -- doc           |     | -- <component_n> |
    |          | -- <component_1> |          | -- bin      |
    |               | -- samples  |          | -- cmake    |
    |               | -- ..       |          | -- doc      |
    |          | -- <component_n> |          | -- lib      |
    |               | -- samples  |          | -- include  |
    |               | -- ..       |          | -- samples  |
    |______________________________________________________|
:::
::::
:::::

::::::::::::::: {#rocm-fhs-reorganization-backward-compatibility .section}
## ROCm FHS reorganization: backward compatibility[\#](#rocm-fhs-reorganization-backward-compatibility "Link to this heading"){.headerlink}

The FHS file organization for ROCm was first introduced in the release of ROCm 5.2 . Backward compatibility was implemented to make sure users could still run their ROCm applications while transitioning to the new FHS. ROCm has moved header files and libraries to their new locations as indicated in the above structure, and included symbolic-links and wrapper header files in their old location for backward compatibility. The following sections detail ROCm backward compatibility implementation for wrapper header files, executable files, library files and CMake config files.

::::: {#wrapper-header-files .section}
### Wrapper header files[\#](#wrapper-header-files "Link to this heading"){.headerlink}

Wrapper header files are placed in the old location ( [`/opt/rocm-<ver>/<component>/include`{.docutils .literal .notranslate}]{.pre}) with a warning message to include files from the new location ([`/opt/rocm-<ver>/include`{.docutils .literal .notranslate}]{.pre}) as shown in the example below.

:::: {.highlight-cpp .notranslate}
::: highlight
    #pragma message "This file is deprecated. Use file from include path /opt/rocm-ver/include/ and prefix with hip."
    #include <hip/hip_runtime.h>
:::
::::

- Starting at ROCm 5.2 release, the deprecation for backward compatibility wrapper header files is: [`#pragma`{.docutils .literal .notranslate}]{.pre} message announcing [`#warning`{.docutils .literal .notranslate}]{.pre}.

- Starting from ROCm 6.0 (tentatively) backward compatibility for wrapper header files will be removed, and the [`#pragma`{.docutils .literal .notranslate}]{.pre} message will be announcing [`#error`{.docutils .literal .notranslate}]{.pre}.
:::::

::::: {#executable-files .section}
### Executable files[\#](#executable-files "Link to this heading"){.headerlink}

Executable files are available in the [`/opt/rocm-<ver>/bin`{.docutils .literal .notranslate}]{.pre} folder. For backward compatibility, the old library location ([`/opt/rocm-<ver>/<component>/bin`{.docutils .literal .notranslate}]{.pre}) has a soft link to the library at the new location. Soft links will be removed in a future release, tentatively ROCm v6.0.

:::: {.highlight-bash .notranslate}
::: highlight
    $ ls -l /opt/rocm/hip/bin/
    lrwxrwxrwx 1 root root   24 Jan 1 23:32 hipcc -> ../../bin/hipcc
:::
::::
:::::

::::: {#library-files .section}
### Library files[\#](#library-files "Link to this heading"){.headerlink}

Library files are available in the [`/opt/rocm-<ver>/lib`{.docutils .literal .notranslate}]{.pre} folder. For backward compatibility, the old library location ([`/opt/rocm-<ver>/<component>/lib`{.docutils .literal .notranslate}]{.pre}) has a soft link to the library at the new location. Soft links will be removed in a future release, tentatively ROCm v6.0.

:::: {.highlight-shell .notranslate}
::: highlight
    $ ls -l /opt/rocm/hip/lib/
    drwxr-xr-x 4 root root 4096 Jan 1 10:45 cmake
    lrwxrwxrwx 1 root root   24 Jan 1 23:32 libamdhip64.so -> ../../lib/libamdhip64.so
:::
::::
:::::

::::: {#cmake-config-files .section}
### CMake config files[\#](#cmake-config-files "Link to this heading"){.headerlink}

All CMake configuration files are available in the [`/opt/rocm-<ver>/lib/cmake/<component>`{.docutils .literal .notranslate}]{.pre} folder. For backward compatibility, the old CMake locations ([`/opt/rocm-<ver>/<component>/lib/cmake`{.docutils .literal .notranslate}]{.pre}) consist of a soft link to the new CMake config. Soft links will be removed in a future release, tentatively ROCm v6.0.

:::: {.highlight-shell .notranslate}
::: highlight
    $ ls -l /opt/rocm/hip/lib/cmake/hip/
    lrwxrwxrwx 1 root root 42 Jan 1 23:32 hip-config.cmake -> ../../../../lib/cmake/hip/hip-config.cmake
:::
::::
:::::
:::::::::::::::

::: {#changes-required-in-applications-using-rocm .section}
## Changes required in applications using ROCm[\#](#changes-required-in-applications-using-rocm "Link to this heading"){.headerlink}

Applications using ROCm are advised to use the new file paths. As the old files will be deprecated in a future release. Applications have to make sure to include correct header file and use correct search paths.

1.  [`#include<header_file.h>`{.docutils .literal .notranslate}]{.pre} needs to be changed to [`#include`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`<component/header_file.h>`{.docutils .literal .notranslate}]{.pre}

    For example: [`#include`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`<hip.h>`{.docutils .literal .notranslate}]{.pre} needs to change to [`#include`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`<hip/hip.h>`{.docutils .literal .notranslate}]{.pre}

2.  Any variable in CMake or Makefiles pointing to component folder needs to changed.

    For example: [`VAR1=/opt/rocm/hip`{.docutils .literal .notranslate}]{.pre} needs to be changed to [`VAR1=/opt/rocm`{.docutils .literal .notranslate}]{.pre} [`VAR2=/opt/rocm/hsa`{.docutils .literal .notranslate}]{.pre} needs to be changed to [`VAR2=/opt/rocm`{.docutils .literal .notranslate}]{.pre}

3.  Any reference to [`/opt/rocm/<component>/bin`{.docutils .literal .notranslate}]{.pre} or [`/opt/rocm/<component>/lib`{.docutils .literal .notranslate}]{.pre} needs to be changed to [`/opt/rocm/bin`{.docutils .literal .notranslate}]{.pre} and [`/opt/rocm/lib/`{.docutils .literal .notranslate}]{.pre}, respectively.
:::

::: {#changes-in-versioning-specifications .section}
## Changes in versioning specifications[\#](#changes-in-versioning-specifications "Link to this heading"){.headerlink}

In order to better manage ROCm dependencies specification and allow smoother releases of ROCm while avoiding dependency conflicts, ROCm software shall adhere to the following scheme when numbering and incrementing ROCm files versions:

rocm-\<ver\>, where \<ver\> = \<x.y.z\>

x.y.z denote: MAJOR.MINOR.PATCH

z: PATCH - increment z when implementing backward compatible bug fixes.

y: MINOR - increment y when implementing minor changes that add functionality but are still backward compatible.

x: MAJOR - increment x when implementing major changes that are not backward compatible.
:::
::::::::::::::::::::::::::::::::::

::::: prev-next-area
[](gpu-arch/mi100.html "previous page"){.left-prev}

::: prev-next-info
previous

AMD Instinct™ MI100 microarchitecture
:::

[](gpu-isolation.html "next page"){.right-next}

::: prev-next-info
next

GPU isolation techniques
:::
:::::
:::::::::::::::::::::::::::::::::::::::::::::::::::

:::::: {.bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {.page-toc .tocsection .onthispage}
Contents
:::

- [Introduction](#introduction){.reference .internal .nav-link}
- [Adopting the FHS](#adopting-the-fhs){.reference .internal .nav-link}
- [Changes from earlier ROCm versions](#changes-from-earlier-rocm-versions){.reference .internal .nav-link}
- [ROCm FHS reorganization: backward compatibility](#rocm-fhs-reorganization-backward-compatibility){.reference .internal .nav-link}
  - [Wrapper header files](#wrapper-header-files){.reference .internal .nav-link}
  - [Executable files](#executable-files){.reference .internal .nav-link}
  - [Library files](#library-files){.reference .internal .nav-link}
  - [CMake config files](#cmake-config-files){.reference .internal .nav-link}
- [Changes required in applications using ROCm](#changes-required-in-applications-using-rocm){.reference .internal .nav-link}
- [Changes in versioning specifications](#changes-in-versioning-specifications){.reference .internal .nav-link}
::::
:::::
::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
