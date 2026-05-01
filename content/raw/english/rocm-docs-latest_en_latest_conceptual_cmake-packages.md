---
title: "Using CMake"
source_url: "https://rocm.docs.amd.com/en/latest/conceptual/cmake-packages.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T06:56:10.076226+00:00
content_hash: "80f015fc39ffc038"
---

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
{#main-content .bd-main role="main"}

sbt-scroll-pixel-helper

::::::::::::::::::::::::::::::::::::::::::::::::::::::::
bd-content
:::::::::::::::::::::::::::::::::::::::::::::::::::
bd-article-container
:::::::
{.bd-header-article .d-print-none}
::::::
{.header-article-items .header-article__inner}
::
header-article-items__start

header-article-item
[]{.fa-solid .fa-angle-right}

header-article-item

::

::
header-article-items__end
:
header-article-item

article-header-buttons
[]{.fa-solid .fa-list}

:
::
::::::
:::::::

{#jb-print-docs-body .onlyprint}
# Using CMake

::
{#print-main-content}
:
{#jb-print-toc}

{}
## Contents

:
::

{#searchbox}

:::::::::::::::::::::::::::::::::::::
{#using-cmake .section}
# Using CMake[\#](#using-cmake "Link to this heading"){.headerlink}

::::::::
{#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::
{.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::
{.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::
{.sd-container-fluid .sd-sphinx-override .docutils}
::::
{.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}

{.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23

{.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 12 min read time

{.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils style="color:gray;"}
Applies to Linux and Windows

{.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}

::::
:::::
::::::
:::::::
::::::::

Most components in ROCm support CMake. Projects depending on header-only or library components typically require CMake 3.5 or higher whereas those wanting to make use of the CMake HIP language support will require CMake 3.21 or higher.

:
{#finding-dependencies .section}
## Finding dependencies[\#](#finding-dependencies "Link to this heading"){.headerlink}

{.admonition .note}
Note

For a complete reference on how to deal with dependencies in CMake, refer to the CMake docs on [find_package](https://cmake.org/cmake/help/latest/command/find_package.html){.reference .external} and the [Using Dependencies Guide](https://cmake.org/cmake/help/latest/guide/using-dependencies/index.html){.reference .external} to get an overview of CMake related facilities.

In short, CMake supports finding dependencies in two ways:

- In Module mode, it consults a file [`Find<PackageName>.cmake`{.docutils .literal .notranslate}]{.pre} which tries to find the component in typical install locations and layouts. CMake ships a few dozen such scripts, but users and projects may ship them as well.

- In Config mode, it locates a file named [`<packagename>-config.cmake`{.docutils .literal .notranslate}]{.pre} or [`<PackageName>Config.cmake`{.docutils .literal .notranslate}]{.pre} which describes the installed component in all regards needed to consume it.

ROCm predominantly relies on Config mode, one notable exception being the Module driving the compilation of HIP programs on NVIDIA runtimes. As such, when dependencies are not found in standard system locations, one either has to instruct CMake to search for package config files in additional folders using the [`CMAKE_PREFIX_PATH`{.docutils .literal .notranslate}]{.pre} variable (a semi-colon separated list of file system paths), or using [`<PackageName>_ROOT`{.docutils .literal .notranslate}]{.pre} variable on a project-specific basis.

There are nearly a dozen ways to set these variables. One may be more convenient over the other depending on your workflow. Conceptually the simplest is adding it to your CMake configuration command on the command line via [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`CMAKE_PREFIX_PATH=....`{.docutils .literal .notranslate}]{.pre} . AMD packaged ROCm installs can typically be added to the config file search paths such as:

- Windows: [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`CMAKE_PREFIX_PATH=${env:HIP_PATH}`{.docutils .literal .notranslate}]{.pre}

- Linux: [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`CMAKE_PREFIX_PATH=/opt/rocm`{.docutils .literal .notranslate}]{.pre}

ROCm provides the respective *config-file* packages, and this enables [`find_package`{.docutils .literal .notranslate}]{.pre} to be used directly. ROCm does not require any Find module as the *config-file* packages are shipped with the upstream projects, such as rocPRIM and other ROCm libraries.

For a complete guide on where and how ROCm may be installed on a system, refer to the installation guides for [Linux](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/tutorial/quick-start.html){.reference .external} and [Windows](https://rocm.docs.amd.com/projects/install-on-windows/en/latest/index.html){.reference .external}.
:

::::::::::::::::::::
{#using-hip-in-cmake .section}
## Using HIP in CMake[\#](#using-hip-in-cmake "Link to this heading"){.headerlink}

ROCm components providing a C/C++ interface support consumption via any C/C++ toolchain that CMake knows how to drive. ROCm also supports the CMake HIP language features, allowing users to program using the HIP single-source programming model. When a program (or translation-unit) uses the HIP API without compiling any GPU device code, HIP can be treated in CMake as a simple C/C++ library.

:::::
{#using-the-hip-single-source-programming-model .section}
### Using the HIP single-source programming model[\#](#using-the-hip-single-source-programming-model "Link to this heading"){.headerlink}

Source code written in the HIP dialect of C++ typically uses the .hip extension. When the HIP CMake language is enabled, it will automatically associate such source files with the HIP toolchain being used.

:
{.highlight-cmake .notranslate}

highlight
    cmake_minimum_required(VERSION 3.21) # HIP language support requires 3.21
    cmake_policy(VERSION 3.21.3...3.27)
    project(MyProj LANGUAGES HIP)
    add_executable(MyApp Main.hip)

:

Should you have existing CUDA code that is from the source compatible subset of HIP, you can tell CMake that despite their .cu extension, they're HIP sources. Do note that this mostly facilitates compiling kernel code-only source files, as host-side CUDA API won't compile in this fashion.

:
{.highlight-cmake .notranslate}

highlight
    add_library(MyLib MyLib.cu)
    set_source_files_properties(MyLib.cu PROPERTIES LANGUAGE HIP)

:

CMake itself only hosts part of the HIP language support, such as defining HIP-specific properties, etc. while the other half ships with the HIP implementation, such as ROCm. CMake will search for a file hip-lang-config.cmake describing how the the properties defined by CMake translate to toolchain invocations. If one installs ROCm using non-standard methods or layouts and CMake can't locate this file or detect parts of the SDK, there's a catch-all, last resort variable consulted locating this file, [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`CMAKE_HIP_COMPILER_ROCM_ROOT:PATH=`{.docutils .literal .notranslate}]{.pre} which should be set the root of the ROCm installation.

{.admonition .note}
Note

Imported targets defined by hip-lang-config.cmake are for internal use only.

If the user doesn't provide a semi-colon delimited list of device architectures via [`CMAKE_HIP_ARCHITECTURES`{.docutils .literal .notranslate}]{.pre}, CMake will select some sensible default. It is advised though that if a user knows what devices they wish to target, then set this variable explicitly.
:::::

{#consuming-rocm-c-c-libraries .section}
### Consuming ROCm C/C++ libraries[\#](#consuming-rocm-c-c-libraries "Link to this heading"){.headerlink}

Libraries such as rocBLAS, rocFFT, MIOpen, etc. behave as C/C++ libraries. Illustrated in the example below is a C++ application using MIOpen from CMake. It calls [`find_package(miopen)`{.docutils .literal .notranslate}]{.pre}, which provides the [`MIOpen`{.docutils .literal .notranslate}]{.pre} imported target. This can be linked with [`target_link_libraries`{.docutils .literal .notranslate}]{.pre}

:
{.highlight-cmake .notranslate}

highlight
    cmake_minimum_required(VERSION 3.5) # find_package(miopen) requires 3.5
    cmake_policy(VERSION 3.5...3.27)
    project(MyProj LANGUAGES CXX)
    find_package(miopen)
    add_library(MyLib ...)
    target_link_libraries(MyLib PUBLIC MIOpen)

:

{.admonition .note}
Note

Most libraries are designed as host-only API, so using a GPU device compiler is not necessary for downstream projects unless they use GPU device code.

::
{#consuming-the-hip-api-in-c-code .section}
### Consuming the HIP API in C++ code[\#](#consuming-the-hip-api-in-c-code "Link to this heading"){.headerlink}

Consuming the HIP API without compiling single-source GPU device code can be done using any C++ compiler. The [`find_package(hip)`{.docutils .literal .notranslate}]{.pre} provides the [`hip::host`{.docutils .literal .notranslate}]{.pre} imported target to use HIP in this scenario.

:
{.highlight-cmake .notranslate}

highlight
    cmake_minimum_required(VERSION 3.5) # find_package(hip) requires 3.5
    cmake_policy(VERSION 3.5...3.27)
    project(MyProj LANGUAGES CXX)
    find_package(hip REQUIRED)
    add_executable(MyApp ...)
    target_link_libraries(MyApp PRIVATE hip::host)

:

When mixing such [`CXX`{.docutils .literal .notranslate}]{.pre} sources with [`HIP`{.docutils .literal .notranslate}]{.pre} sources holding device-code, link only to hip::host. If HIP sources don't have .hip as their extension, use set_source_files_properties(\<hip_sources\>... PROPERTIES LANGUAGE HIP) on them. Linking to hip::host will set all the necessary flags for the [`CXX`{.docutils .literal .notranslate}]{.pre} sources while [`HIP`{.docutils .literal .notranslate}]{.pre} sources inherit all flags from the built-in language support. Having HIP sources in a target will turn the [[`LINKER_LANGUAGE`{.docutils .literal .notranslate}]{.pre}](https://cmake.org/cmake/help/latest/prop_tgt/LINKER_LANGUAGE.html){.reference .external} into [`HIP`{.docutils .literal .notranslate}]{.pre}.
::

::::
{#compiling-device-code-in-c-language-mode .section}
### Compiling device code in C++ language mode[\#](#compiling-device-code-in-c-language-mode "Link to this heading"){.headerlink}

{.admonition .attention}
Attention

The workflow detailed here is considered legacy and is shown for understanding's sake. It pre-dates the existence of HIP language support in CMake. If source code has HIP device code in it, it is a HIP source file and should be compiled as such. Only resort to the method below if your HIP-enabled CMake code path can't mandate CMake version 3.21.

If code uses the HIP API and compiles GPU device code, it requires using a device compiler. The compiler for CMake can be set using either the [`CMAKE_C_COMPILER`{.docutils .literal .notranslate}]{.pre} and [`CMAKE_CXX_COMPILER`{.docutils .literal .notranslate}]{.pre} variable or using the [`CC`{.docutils .literal .notranslate}]{.pre} and [`CXX`{.docutils .literal .notranslate}]{.pre} environment variables. This can be set when configuring CMake or put into a CMake toolchain file. The device compiler must be set to a compiler that supports AMD GPU targets, which is usually Clang.

The [`find_package(hip)`{.docutils .literal .notranslate}]{.pre} provides the [`hip::device`{.docutils .literal .notranslate}]{.pre} imported target to add all the flags necessary for device compilation.

:
{.highlight-cmake .notranslate}

highlight
    cmake_minimum_required(VERSION 3.8) # cxx_std_11 requires 3.8
    cmake_policy(VERSION 3.8...3.27)
    project(MyProj LANGUAGES CXX)
    find_package(hip REQUIRED)
    add_library(MyLib ...)
    target_link_libraries(MyLib PRIVATE hip::device)
    target_compile_features(MyLib PRIVATE cxx_std_11)

:

{.admonition .note}
Note

Compiling for the GPU device requires at least C++11.

This project can then be configured with the following CMake commands:

- Windows: [`cmake`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`CMAKE_CXX_COMPILER:PATH=${env:HIP_PATH}\bin\clang++.exe`{.docutils .literal .notranslate}]{.pre}

- Linux: [`cmake`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`CMAKE_CXX_COMPILER:PATH=/opt/rocm/bin/amdclang++`{.docutils .literal .notranslate}]{.pre}

Which use the device compiler provided from the binary packages of [ROCm HIP SDK](https://www.amd.com/en/developer/resources/rocm-hub/hip-sdk.html){.reference .external} and [repo.radeon.com](https://repo.radeon.com){.reference .external} respectively.

When using the [`CXX`{.docutils .literal .notranslate}]{.pre} language support to compile HIP device code, selecting the target GPU architectures is done via setting the [`GPU_TARGETS`{.docutils .literal .notranslate}]{.pre} variable. [`CMAKE_HIP_ARCHITECTURES`{.docutils .literal .notranslate}]{.pre} only exists when the HIP language is enabled. By default, this is set to some subset of the currently supported architectures of AMD ROCm. It can be set to the CMake option [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`GPU_TARGETS="gfx1032;gfx1035"`{.docutils .literal .notranslate}]{.pre}.
::::

:
{#rocm-cmake-packages .section}
### ROCm CMake packages[\#](#rocm-cmake-packages "Link to this heading"){.headerlink}

pst-scrollable-table-container
  Component    Package      Targets
  ------------ ------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  HIP          hip          [`hip::host`{.docutils .literal .notranslate}]{.pre}, [`hip::device`{.docutils .literal .notranslate}]{.pre}
  rocPRIM      rocprim      [`roc::rocprim`{.docutils .literal .notranslate}]{.pre}
  rocThrust    rocthrust    [`roc::rocthrust`{.docutils .literal .notranslate}]{.pre}
  hipCUB       hipcub       [`hip::hipcub`{.docutils .literal .notranslate}]{.pre}
  rocRAND      rocrand      [`roc::rocrand`{.docutils .literal .notranslate}]{.pre}
  rocBLAS      rocblas      [`roc::rocblas`{.docutils .literal .notranslate}]{.pre}
  rocSOLVER    rocsolver    [`roc::rocsolver`{.docutils .literal .notranslate}]{.pre}
  hipBLAS      hipblas      [`roc::hipblas`{.docutils .literal .notranslate}]{.pre}
  rocFFT       rocfft       [`roc::rocfft`{.docutils .literal .notranslate}]{.pre}
  hipFFT       hipfft       [`hip::hipfft`{.docutils .literal .notranslate}]{.pre}
  rocSPARSE    rocsparse    [`roc::rocsparse`{.docutils .literal .notranslate}]{.pre}
  hipSPARSE    hipsparse    [`roc::hipsparse`{.docutils .literal .notranslate}]{.pre}
  rocALUTION   rocalution   [`roc::rocalution`{.docutils .literal .notranslate}]{.pre}
  RCCL         rccl         [`rccl`{.docutils .literal .notranslate}]{.pre}
  MIOpen       miopen       [`MIOpen`{.docutils .literal .notranslate}]{.pre}
  MIGraphX     migraphx     [`migraphx::migraphx`{.docutils .literal .notranslate}]{.pre}, [`migraphx::migraphx_c`{.docutils .literal .notranslate}]{.pre}, [`migraphx::migraphx_cpu`{.docutils .literal .notranslate}]{.pre}, [`migraphx::migraphx_gpu`{.docutils .literal .notranslate}]{.pre}, [`migraphx::migraphx_onnx`{.docutils .literal .notranslate}]{.pre}, [`migraphx::migraphx_tf`{.docutils .literal .notranslate}]{.pre}

:
::::::::::::::::::::

::::
{#using-cmake-presets .section}
## Using CMake presets[\#](#using-cmake-presets "Link to this heading"){.headerlink}

CMake command lines depending on how specific users like to be when compiling code can grow to unwieldy lengths. This is the primary reason why projects tend to bake script snippets into their build definitions controlling compiler warning levels, changing CMake defaults ([`CMAKE_BUILD_TYPE`{.docutils .literal .notranslate}]{.pre} or [`BUILD_SHARED_LIBS`{.docutils .literal .notranslate}]{.pre} just to name a few) and all sorts anti-patterns, all in the name of convenience.

Load on the command-line interface (CLI) starts immediately by selecting a toolchain, the set of utilities used to compile programs. To ease some of the toolchain related pains, CMake does consult the [`CC`{.docutils .literal .notranslate}]{.pre} and [`CXX`{.docutils .literal .notranslate}]{.pre} environmental variables when setting a default [`CMAKE_C[XX]_COMPILER`{.docutils .literal .notranslate}]{.pre} respectively, but that is just the tip of the iceberg. There's a fair number of variables related to just the toolchain itself (typically supplied using [toolchain files](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html){.reference .external} ), and then we still haven't talked about user preference or project-specific options.

IDEs supporting CMake (Visual Studio, Visual Studio Code, CLion, etc.) all came up with their own way to register command-line fragments of different purpose in a setup-and-forget fashion for quick assembly using graphical front-ends. This is all nice, but configurations aren't portable, nor can they be reused in Continuous Integration (CI) pipelines. CMake has condensed existing practice into a portable JSON format that works in all IDEs and can be invoked from any command line. This is [CMake Presets](https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html){.reference .external}.

There are two types of preset files: one supplied by the project, called [`CMakePresets.json`{.docutils .literal .notranslate}]{.pre} which is meant to be committed to version control, typically used to drive CI; and one meant for the user to provide, called [`CMakeUserPresets.json`{.docutils .literal .notranslate}]{.pre}, typically used to house user preference and adapting the build to the user's environment. These JSON files are allowed to include other JSON files and the user presets always implicitly includes the non-user variant.

{#using-hip-with-presets .section}
### Using HIP with presets[\#](#using-hip-with-presets "Link to this heading"){.headerlink}

Following is an example [`CMakeUserPresets.json`{.docutils .literal .notranslate}]{.pre} file which actually compiles the [amd/rocm-examples](https://github.com/amd/rocm-examples){.reference .external} suite of sample applications on a typical ROCm installation:

:
{.highlight-json .notranslate}

highlight
    {
      "version": 3,
      "cmakeMinimumRequired": {
        "major": 3,
        "minor": 21,
        "patch": 0
      },
      "configurePresets": [
        {
          "name": "layout",
          "hidden": true,
          "binaryDir": "${sourceDir}/build/${presetName}",
          "installDir": "${sourceDir}/install/${presetName}"
        },
        {
          "name": "generator-ninja-multi-config",
          "hidden": true,
          "generator": "Ninja Multi-Config"
        },
        {
          "name": "toolchain-makefiles-c/c++-amdclang",
          "hidden": true,
          "cacheVariables": {
            "CMAKE_C_COMPILER": "/opt/rocm/bin/amdclang",
            "CMAKE_CXX_COMPILER": "/opt/rocm/bin/amdclang++",
            "CMAKE_HIP_COMPILER": "/opt/rocm/bin/amdclang++"
          }
        },
        {
          "name": "clang-strict-iso-high-warn",
          "hidden": true,
          "cacheVariables": {
            "CMAKE_C_FLAGS": "-Wall -Wextra -pedantic",
            "CMAKE_CXX_FLAGS": "-Wall -Wextra -pedantic",
            "CMAKE_HIP_FLAGS": "-Wall -Wextra -pedantic"
          }
        },
        {
          "name": "ninja-mc-rocm",
          "displayName": "Ninja Multi-Config ROCm",
          "inherits": [
            "layout",
            "generator-ninja-multi-config",
            "toolchain-makefiles-c/c++-amdclang",
            "clang-strict-iso-high-warn"
          ]
        }
      ],
      "buildPresets": [
        {
          "name": "ninja-mc-rocm-debug",
          "displayName": "Debug",
          "configuration": "Debug",
          "configurePreset": "ninja-mc-rocm"
        },
        {
          "name": "ninja-mc-rocm-release",
          "displayName": "Release",
          "configuration": "Release",
          "configurePreset": "ninja-mc-rocm"
        },
        {
          "name": "ninja-mc-rocm-debug-verbose",
          "displayName": "Debug (verbose)",
          "configuration": "Debug",
          "configurePreset": "ninja-mc-rocm",
          "verbose": true
        },
        {
          "name": "ninja-mc-rocm-release-verbose",
          "displayName": "Release (verbose)",
          "configuration": "Release",
          "configurePreset": "ninja-mc-rocm",
          "verbose": true
        }
      ],
      "testPresets": [
        {
          "name": "ninja-mc-rocm-debug",
          "displayName": "Debug",
          "configuration": "Debug",
          "configurePreset": "ninja-mc-rocm",
          "execution": {
            "jobs": 0
          }
        },
        {
          "name": "ninja-mc-rocm-release",
          "displayName": "Release",
          "configuration": "Release",
          "configurePreset": "ninja-mc-rocm",
          "execution": {
            "jobs": 0
          }
        }
      ]
    }

:

{.admonition .note}
Note

Getting presets to work reliably on Windows requires some CMake improvements and/or support from compiler vendors. (Refer to [Add support to the Visual Studio generators](https://gitlab.kitware.com/cmake/cmake/-/issues/24245){.reference .external} and [Sourcing environment scripts](https://gitlab.kitware.com/cmake/cmake/-/issues/21619){.reference .external} .)

::::
:::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::

{.bd-sidebar-secondary .bd-toc}
::
{.sidebar-secondary-items .sidebar-secondary__inner}
:
sidebar-secondary-item

{.page-toc .tocsection .onthispage}
Contents

:
::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
