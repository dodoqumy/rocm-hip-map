---
title: "Build HIP from source &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/install/build.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T06:59:34.140588+00:00
content_hash: "58fccc2959f1117e"
---

:::::::::::::::::::::::::::::::::
{#main-content .bd-main role="main"}

sbt-scroll-pixel-helper

:::::::::::::::::::::::::::::::
bd-content
::::::::::::::::::::::::::
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
# Build HIP from source

::
{#print-main-content}
:
{#jb-print-toc}

{}
## Contents

:
::

{#searchbox}

::::::::::::
{#build-hip-from-source .section}
# Build HIP from source[\#](#build-hip-from-source "Link to this heading"){.headerlink}

::::::
{#prerequisites .section}
## Prerequisites[\#](#prerequisites "Link to this heading"){.headerlink}

HIP code can be developed on AMD ROCm platform using HIP-Clang compiler. Before building and running HIP, make sure drivers and prebuilt packages are installed properly on the platform.

You also need to install Python 3, which includes the [`CppHeaderParser`{.docutils .literal .notranslate}]{.pre} package. Install Python 3 using the following command:

:
{.highlight-shell .notranslate}

highlight
    apt-get install python3

:

Check and install [`CppHeaderParser`{.docutils .literal .notranslate}]{.pre} package using the command:

:
{.highlight-shell .notranslate}

highlight
    pip3 install CppHeaderParser

:

Install [`ROCm`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`LLVM`{.docutils .literal .notranslate}]{.pre} package using the command:

:
{.highlight-shell .notranslate}

highlight
    apt-get install rocm-llvm-dev

:
::::::

::
{#building-the-hip-runtime .section}
[]{#id1}

## Building the HIP runtime[\#](#building-the-hip-runtime "Link to this heading"){.headerlink}

In the ROCM 7.1 release, HIP is integrated into the core ROCm projects resides in the [`rocm-systems`{.docutils .literal .notranslate}]{.pre} monorepository. In addition, the following components are also part of the monorepository:

- [`clr`{.docutils .literal .notranslate}]{.pre}, AMD's Compute Language Runtime, includes ROCclr, HIPAMD and OpenCl.

- [`hip-tests`{.docutils .literal .notranslate}]{.pre}, the HIP testing suite.

Set the repository branch using the variable: [`ROCM_BRANCH`{.docutils .literal .notranslate}]{.pre}. For example, for ROCM 7.1, use:

:
{.highlight-shell .notranslate}

highlight
    export ROCM_BRANCH=release/rocm-rel-7.1

:

1.  Get HIP source code.

    :
{.highlight-shell .notranslate}
    
highlight
        git clone -b "$ROCM_BRANCH" git@github.com:ROCm/rocm-systems.git
    
    :

2.  Set the environment variables.

    :
{.highlight-shell .notranslate}
    
highlight
        export CLR_DIR="$(readlink -f rocm-systems/projects/clr)"
        export HIP_DIR="$(readlink -f rocm-systems/projects/hip)"
    
    :

3.  Build HIP.

    :
{.highlight-shell .notranslate}
    
highlight
        cd "$CLR_DIR"
        mkdir -p build; cd build
        cmake -DHIP_COMMON_DIR=$HIP_DIR -DHIP_PLATFORM=amd -DCMAKE_PREFIX_PATH="/opt/rocm/" -DCMAKE_INSTALL_PREFIX=$PWD/install -DCLR_BUILD_HIP=ON -DCLR_BUILD_OCL=OFF ..
        make -j$(nproc)
        sudo make install
    
    :

    
{.admonition .note}
    Note

    If [`CMAKE_INSTALL_PREFIX`{.docutils .literal .notranslate}]{.pre} is not explicitly specified, the HIP runtime will be installed at [`<ROCM_PATH>`{.docutils .literal .notranslate}]{.pre}, which is by default at the path [`/opt/rocm`{.docutils .literal .notranslate}]{.pre}.

    By default, the release version of HIP is built. If you need a debug version, you can put the option [`CMAKE_BUILD_TYPE=Debug`{.docutils .literal .notranslate}]{.pre} in the command line.
    

    Default paths and environment variables:

    - HIP is installed into [`<ROCM_PATH>`{.docutils .literal .notranslate}]{.pre}. This can be overridden by setting the [`INSTALL_PREFIX`{.docutils .literal .notranslate}]{.pre} as the command option.

    - HSA is in [`<ROCM_PATH>`{.docutils .literal .notranslate}]{.pre}. This can be overridden by setting the [`HSA_PATH`{.docutils .literal .notranslate}]{.pre} environment variable.

    - Clang is in [`<ROCM_PATH>/llvm/bin`{.docutils .literal .notranslate}]{.pre}. This can be overridden by setting the [`HIP_CLANG_PATH`{.docutils .literal .notranslate}]{.pre} environment variable.

    - The device library is in [`<ROCM_PATH>/lib`{.docutils .literal .notranslate}]{.pre}. This can be overridden by setting the [`DEVICE_LIB_PATH`{.docutils .literal .notranslate}]{.pre} environment variable.

    - Optionally, you can add [`<ROCM_PATH>/bin`{.docutils .literal .notranslate}]{.pre} to your [`PATH`{.docutils .literal .notranslate}]{.pre}, which can make it easier to use the tools.

    - Optionally, you can set [`HIPCC_VERBOSE=7`{.docutils .literal .notranslate}]{.pre} to output the command line for compilation.

    After you run the [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`install`{.docutils .literal .notranslate}]{.pre} command, HIP is installed to [`<ROCM_PATH>`{.docutils .literal .notranslate}]{.pre} by default, or [`$PWD/install/hip`{.docutils .literal .notranslate}]{.pre} while [`INSTALL_PREFIX`{.docutils .literal .notranslate}]{.pre} is defined.

4.  Generate a profiling header after adding/changing a HIP API.

    When you add or change a HIP API, you may need to generate a new [`hip_prof_str.h`{.docutils .literal .notranslate}]{.pre} header. This header is used by ROCm tools to track HIP APIs, such as [`rocprofiler`{.docutils .literal .notranslate}]{.pre} and [`roctracer`{.docutils .literal .notranslate}]{.pre}.

    To generate the header after your change, use the [`hip_prof_gen.py`{.docutils .literal .notranslate}]{.pre} tool located in [`hipamd/src`{.docutils .literal .notranslate}]{.pre}.

    Usage:

    :
{.highlight-shell .notranslate}
    
highlight
        `hip_prof_gen.py [-v] <input HIP API .h file> <patched srcs path> <previous output> [<output>]`

        Flags:

           * ``-v``: Verbose messages
           * ``-r``: Process source directory recursively
           * ``-t``: API types matching check
           * ``--priv``: Private API check
           * ``-e``: On error exit mode
           * ``-p``: ``HIP_INIT_API`` macro patching mode
    
    :

    Example usage:

    :
{.highlight-shell .notranslate}
    
highlight
        hip_prof_gen.py -v -p -t --priv <hip>/include/hip/hip_runtime_api.h \
        <hipamd>/src <hipamd>/include/hip/amd_detail/hip_prof_str.h \
        <hipamd>/include/hip/amd_detail/hip_prof_str.h.new
    
    :
::

{#build-hip-tests .section}
## Build HIP tests[\#](#build-hip-tests "Link to this heading"){.headerlink}

**Build HIP catch tests.**

HIP catch tests utilize the Catch2 testing framework.

1.  Get HIP tests source code.

    :
{.highlight-shell .notranslate}
    
highlight
        git clone -b "$ROCM_BRANCH" git@github.com:ROCm/rocm-systems.git
        export HIPTESTS_DIR="$(readlink -f rocm-systems/projects/hip-tests)"
    
    :

2.  Build HIP tests from source.

    :
{.highlight-shell .notranslate}
    
highlight
        cd "$HIPTESTS_DIR"
        mkdir -p build; cd build
        cmake ../catch -DHIP_PLATFORM=amd -DHIP_PATH=$CLR_DIR/build/install  # or any path where HIP is installed; for example: ``/opt/rocm``
        export ROCM_PATH=/opt/rocm
        make build_tests
        ctest # run tests
    
    :

    HIP catch tests are built in [`$HIPTESTS_DIR/build`{.docutils .literal .notranslate}]{.pre}.

    To run any single catch test, use this example:

    :
{.highlight-shell .notranslate}
    
highlight
        cd $HIPTESTS_DIR/build/catch_tests/unit/texture
        ./TextureTest
    
    :

3.  Build a HIP Catch2 standalone test.

    :
{.highlight-shell .notranslate}
    
highlight
        cd "$HIPTESTS_DIR"
        hipcc $HIPTESTS_DIR/catch/unit/memory/hipPointerGetAttributes.cc \
        -I ./catch/include ./catch/hipTestMain/standalone_main.cc \
        -I ./catch/external/Catch2 -o hipPointerGetAttributes
        ./hipPointerGetAttributes
        ...

        All tests passed
    
    :

{#run-hip .section}
## Run HIP[\#](#run-hip "Link to this heading"){.headerlink}

After installation and building HIP, you can compile your application and run. Simple examples can be found in the [ROCm-examples repository](https://github.com/ROCm/rocm-examples){.reference .external}.

::::::::::::
::::::::::::::::::::::::::

{.bd-sidebar-secondary .bd-toc}
::
{.sidebar-secondary-items .sidebar-secondary__inner}
:
sidebar-secondary-item

{.page-toc .tocsection .onthispage}
Contents

:
::

:::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::
