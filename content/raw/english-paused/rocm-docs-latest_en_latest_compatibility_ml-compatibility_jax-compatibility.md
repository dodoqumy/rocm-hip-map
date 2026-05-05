---
title: "JAX compatibility"
source_url: "https://rocm.docs.amd.com/en/latest/compatibility/ml-compatibility/jax-compatibility.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-01
---

:::::::::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

:::::::::::::::::::::::::::::::::::::::::::::::::::: bd-content
::::::::::::::::::::::::::::::::::::::::::::::: bd-article-container
:::::::::: {.bd-header-article .d-print-none}
::::::::: {.header-article-items .header-article__inner}
::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}
:::

::: header-article-item
- [](../../index.html){.nav-link aria-label="Home"}
- [Deep learning frameworks for ROCm](../../how-to/deep-learning-rocm.html){.nav-link}
- JAX compatibility
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
# JAX compatibility

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [Support overview](#support-overview){.reference .internal .nav-link}
  - [Version support](#version-support){.reference .internal .nav-link}
- [JAX Plugin-PJRT with JAX/JAXLIB compatibility](#jax-plugin-pjrt-with-jax-jaxlib-compatibility){.reference .internal .nav-link}
- [Use cases and recommendations](#use-cases-and-recommendations){.reference .internal .nav-link}
- [Docker image compatibility](#docker-image-compatibility){.reference .internal .nav-link}
- [Key ROCm libraries for JAX](#key-rocm-libraries-for-jax){.reference .internal .nav-link}
- [Supported data types and modules](#supported-data-types-and-modules){.reference .internal .nav-link}
  - [Supported data types](#supported-data-types){.reference .internal .nav-link}
  - [Supported modules](#supported-modules){.reference .internal .nav-link}
- [Key features and enhancements for ROCm 7.1](#key-features-and-enhancements-for-rocm-7-1){.reference .internal .nav-link}
- [Key features and enhancements for ROCm 7.0](#key-features-and-enhancements-for-rocm-7-0){.reference .internal .nav-link}
- [Known issues and notes for ROCm 7.0](#known-issues-and-notes-for-rocm-7-0){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

:::::::::::::::::::::::::::::: {#jax-compatibility .section}
# JAX compatibility[\#](#jax-compatibility "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-02-25
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 10 min read time
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

[JAX](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html){.reference .external} is a library for array-oriented numerical computation (similar to NumPy), with automatic differentiation and just-in-time (JIT) compilation to enable high-performance machine learning research.

JAX provides an API that combines automatic differentiation and the Accelerated Linear Algebra (XLA) compiler to achieve high-performance machine learning at scale. JAX uses composable transformations of Python and NumPy through JIT compilation, automatic vectorization, and parallelization.

:::: {#support-overview .section}
## Support overview[\#](#support-overview "Link to this heading"){.headerlink}

- The ROCm-supported version of JAX is maintained in the official [ROCm/rocm-jax](https://github.com/ROCm/rocm-jax){.github .reference .external} repository, which differs from the [jax-ml/jax](https://github.com/jax-ml/jax){.github .reference .external} upstream repository.

- To get started and install JAX on ROCm, use the prebuilt [[Docker images]{.std .std-ref}](#jax-docker-compat){.reference .internal}, which include ROCm, JAX, and all required dependencies.

  - See the [[ROCm JAX installation guide]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/jax-install.html "(in ROCm installation on Linux v7.2.2)"){.reference .external} for installation and setup instructions.

  - You can also consult the upstream [Installation guide](https://jax.readthedocs.io/en/latest/installation.html#amd-gpu-linux){.reference .external} for additional context.

::: {#version-support .section}
### Version support[\#](#version-support "Link to this heading"){.headerlink}

AMD releases official [ROCm JAX Docker images](https://hub.docker.com/r/rocm/jax/tags){.reference .external} quarterly alongside new ROCm releases. These images undergo full AMD testing. [Community ROCm JAX Docker images](https://hub.docker.com/r/rocm/jax-community/tags){.reference .external} follow upstream JAX releases and use the latest available ROCm version.
:::
::::

:::: {#jax-plugin-pjrt-with-jax-jaxlib-compatibility .section}
## JAX Plugin-PJRT with JAX/JAXLIB compatibility[\#](#jax-plugin-pjrt-with-jax-jaxlib-compatibility "Link to this heading"){.headerlink}

Portable JIT Runtime (PJRT) is an open, stable interface for device runtime and compiler. The following table details the ROCm version compatibility matrix between JAX Plugin--PJRT and JAX/JAXLIB.

::: pst-scrollable-table-container
  JAX Plugin-PJRT   JAX/JAXLIB   ROCm
  ----------------- ------------ --------------
  0.8.2             0.8.2        7.2.1
  0.8.0             0.8.0        7.2.0
  0.7.1             0.7.1        7.1.1, 7.1.0
:::
::::

::: {#use-cases-and-recommendations .section}
## Use cases and recommendations[\#](#use-cases-and-recommendations "Link to this heading"){.headerlink}

- The [nanoGPT in JAX](https://rocm.blogs.amd.com/artificial-intelligence/nanoGPT-JAX/README.html){.reference .external} blog explores the implementation and training of a Generative Pre-trained Transformer (GPT) model in JAX, inspired by Andrej Karpathy's JAX-based nanoGPT. Comparing how essential GPT components---such as self-attention mechanisms and optimizers---are realized in JAX and JAX, also highlights JAX's unique features.

- The [Optimize GPT Training: Enabling Mixed Precision Training in JAX using ROCm on AMD GPUs](https://rocm.blogs.amd.com/artificial-intelligence/jax-mixed-precision/README.html){.reference .external} blog post provides a comprehensive guide on enhancing the training efficiency of GPT models by implementing mixed precision techniques in JAX, specifically tailored for AMD GPUs utilizing the ROCm platform.

- The [Supercharging JAX with Triton Kernels on AMD GPUs](https://rocm.blogs.amd.com/artificial-intelligence/jax-triton/README.html){.reference .external} blog demonstrates how to develop a custom fused dropout-activation kernel for matrices using Triton, integrate it with JAX, and benchmark its performance using ROCm.

- The [Distributed fine-tuning with JAX on AMD GPUs](https://rocm.blogs.amd.com/artificial-intelligence/distributed-sft-jax/README.html){.reference .external} outlines the process of fine-tuning a Bidirectional Encoder Representations from Transformers (BERT)-based large language model (LLM) using JAX for a text classification task. The blog post discusses techniques for parallelizing the fine-tuning across multiple AMD GPUs and assess the model's performance on a holdout dataset. During the fine-tuning, a BERT-base-cased transformer model and the General Language Understanding Evaluation (GLUE) benchmark dataset was used on a multi-GPU setup.

- The [MI300X workload optimization guide](https://rocm.docs.amd.com/en/latest/how-to/tuning-guides/mi300x/workload.html){.reference .external} provides detailed guidance on optimizing workloads for the AMD Instinct MI300X GPU using ROCm. The page is aimed at helping users achieve optimal performance for deep learning and other high-performance computing tasks on the MI300X GPU.

For more use cases and recommendations, see [ROCm JAX blog posts](https://rocm.blogs.amd.com/blog/tag/jax.html){.reference .external}.
:::

::: {#docker-image-compatibility .section}
[]{#jax-docker-compat}

## Docker image compatibility[\#](#docker-image-compatibility "Link to this heading"){.headerlink}

AMD validates and publishes [JAX images](https://hub.docker.com/r/rocm/jax/tags){.reference .external} with ROCm backends on Docker Hub.

For [`jax-community`{.docutils .literal .notranslate}]{.pre} images, see [rocm/jax-community](https://hub.docker.com/r/rocm/jax-community/tags){.reference .external} on Docker Hub.

To find the right image tag, see the [[JAX on ROCm installation documentation]{.xref .std .std-ref}](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/jax-install.html#jax-docker-support "(in ROCm installation on Linux v7.2.2)"){.reference .external} for a list of available [`rocm/jax`{.docutils .literal .notranslate}]{.pre} images.
:::

::::: {#key-rocm-libraries-for-jax .section}
[]{#key-rocm-libraries}

## Key ROCm libraries for JAX[\#](#key-rocm-libraries-for-jax "Link to this heading"){.headerlink}

The following ROCm libraries represent potential targets that could be utilized by JAX on ROCm for various computational tasks. The actual libraries used will depend on the specific implementation and operations performed.

::: pst-scrollable-table-container
  ROCm library                                                               Version                        Purpose
  -------------------------------------------------------------------------- ------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------
  [hipBLAS](https://github.com/ROCm/hipBLAS){.reference .external}           [3.2.0]{.version-reference}    Provides GPU-accelerated Basic Linear Algebra Subprograms (BLAS) for matrix and vector operations.
  [hipBLASLt](https://github.com/ROCm/hipBLASLt){.reference .external}       [1.2.2]{.version-reference}    hipBLASLt is an extension of hipBLAS, providing additional features like epilogues fused into the matrix multiplication kernel or use of integer tensor cores.
  [hipCUB](https://github.com/ROCm/hipCUB){.reference .external}             [4.2.0]{.version-reference}    Provides a C++ template library for parallel algorithms for reduction, scan, sort and select.
  [hipFFT](https://github.com/ROCm/hipFFT){.reference .external}             [1.0.22]{.version-reference}   Provides GPU-accelerated Fast Fourier Transform (FFT) operations.
  [hipRAND](https://github.com/ROCm/hipRAND){.reference .external}           [3.1.0]{.version-reference}    Provides fast random number generation for GPUs.
  [hipSOLVER](https://github.com/ROCm/hipSOLVER){.reference .external}       [3.2.0]{.version-reference}    Provides GPU-accelerated solvers for linear systems, eigenvalues, and singular value decompositions (SVD).
  [hipSPARSE](https://github.com/ROCm/hipSPARSE){.reference .external}       [4.2.0]{.version-reference}    Accelerates operations on sparse matrices, such as sparse matrix-vector or matrix-matrix products.
  [hipSPARSELt](https://github.com/ROCm/hipSPARSELt){.reference .external}   [0.2.6]{.version-reference}    Accelerates operations on sparse matrices, such as sparse matrix-vector or matrix-matrix products.
  [MIOpen](https://github.com/ROCm/MIOpen){.reference .external}             [3.5.1]{.version-reference}    Optimized for deep learning primitives such as convolutions, pooling, normalization, and activation functions.
  [RCCL](https://github.com/ROCm/rccl){.reference .external}                 [2.27.7]{.version-reference}   Optimized for multi-GPU communication for operations like all-reduce, broadcast, and scatter.
  [rocThrust](https://github.com/ROCm/rocThrust){.reference .external}       [4.2.0]{.version-reference}    Provides a C++ template library for parallel algorithms like sorting, reduction, and scanning.
:::

::: {.admonition .note}
Note

This table shows ROCm libraries that could potentially be utilized by JAX. Not all libraries may be used in every configuration, and the actual library usage will depend on the specific operations and implementation details.
:::
:::::

:::::::: {#supported-data-types-and-modules .section}
## Supported data types and modules[\#](#supported-data-types-and-modules "Link to this heading"){.headerlink}

The following tables lists the supported public JAX API data types and modules.

::::: {#supported-data-types .section}
### Supported data types[\#](#supported-data-types "Link to this heading"){.headerlink}

ROCm supports all the JAX data types of [jax.dtypes](https://docs.jax.dev/en/latest/jax.dtypes.html){.reference .external} module, [jax.numpy.dtype](https://docs.jax.dev/en/latest/_autosummary/jax.numpy.dtype.html){.reference .external} and [default_dtype](https://docs.jax.dev/en/latest/default_dtypes.html){.reference .external} . The ROCm supported data types in JAX are collected in the following table.

::: pst-scrollable-table-container
  Data type                                               Description
  ------------------------------------------------------- -------------------------------------------
  [`bfloat16`{.docutils .literal .notranslate}]{.pre}     16-bit bfloat (brain floating point).
  [`bool`{.docutils .literal .notranslate}]{.pre}         Boolean.
  [`complex128`{.docutils .literal .notranslate}]{.pre}   128-bit complex.
  [`complex64`{.docutils .literal .notranslate}]{.pre}    64-bit complex.
  [`float16`{.docutils .literal .notranslate}]{.pre}      16-bit (half precision) floating-point.
  [`float32`{.docutils .literal .notranslate}]{.pre}      32-bit (single precision) floating-point.
  [`float64`{.docutils .literal .notranslate}]{.pre}      64-bit (double precision) floating-point.
  [`half`{.docutils .literal .notranslate}]{.pre}         16-bit (half precision) floating-point.
  [`int16`{.docutils .literal .notranslate}]{.pre}        Signed 16-bit integer.
  [`int32`{.docutils .literal .notranslate}]{.pre}        Signed 32-bit integer.
  [`int64`{.docutils .literal .notranslate}]{.pre}        Signed 64-bit integer.
  [`int8`{.docutils .literal .notranslate}]{.pre}         Signed 8-bit integer.
  [`uint16`{.docutils .literal .notranslate}]{.pre}       Unsigned 16-bit (word) integer.
  [`uint32`{.docutils .literal .notranslate}]{.pre}       Unsigned 32-bit (dword) integer.
  [`uint64`{.docutils .literal .notranslate}]{.pre}       Unsigned 64-bit (qword) integer.
  [`uint8`{.docutils .literal .notranslate}]{.pre}        Unsigned 8-bit (byte) integer.
:::

::: {.admonition .note}
Note

JAX data type support is affected by the [[Key ROCm libraries for JAX]{.std .std-ref}](#key-rocm-libraries){.reference .internal} and it's collected on [[ROCm data types and precision support]{.xref .std .std-doc}](https://rocm.docs.amd.com/en/latest/reference/precision-support.html "(in ROCm Documentation v7.2.2)"){.reference .external} page.
:::
:::::

:::: {#supported-modules .section}
### Supported modules[\#](#supported-modules "Link to this heading"){.headerlink}

For a complete and up-to-date list of JAX public modules (for example, [`jax.numpy`{.docutils .literal .notranslate}]{.pre}, [`jax.scipy`{.docutils .literal .notranslate}]{.pre}, [`jax.lax`{.docutils .literal .notranslate}]{.pre}), their descriptions, and usage, please refer directly to the [official JAX API documentation](https://jax.readthedocs.io/en/latest/jax.html){.reference .external}.

::: {.admonition .note}
Note

Since version 0.1.56, JAX has full support for ROCm, and the [[Known issues and important notes]{.std .std-ref}](#jax-comp-known-issues){.reference .internal} section contains details about limitations specific to the ROCm backend. The list of JAX API modules are maintained by the JAX project and is subject to change. Refer to the official Jax documentation for the most up-to-date information.
:::
::::
::::::::

::: {#key-features-and-enhancements-for-rocm-7-1 .section}
## Key features and enhancements for ROCm 7.1[\#](#key-features-and-enhancements-for-rocm-7-1 "Link to this heading"){.headerlink}

- Enabled compilation of multihost HLO runner Python bindings.

  - Backported multihost HLO runner bindings and some related changes to [`FunctionalHloRunner`{.code .docutils .literal .notranslate}]{.pre}.

  - Added [`requirements_lock_3_12`{.code .docutils .literal .notranslate}]{.pre} to enable building for Python 3.12.

- Removed hardcoded NHWC convolution layout for [`fp16`{.docutils .literal .notranslate}]{.pre} precision to address the performance drops for [`fp16`{.docutils .literal .notranslate}]{.pre} precision on gfx12xx GPUs.

- ROCprofiler-SDK integration:

  - Integrated ROCprofiler-SDK (v3) to XLA to improve profiling of GPU events, support both time-based and step-based profiling.

  - Added unit tests for [`rocm_collector`{.code .docutils .literal .notranslate}]{.pre} and [`rocm_tracer`{.code .docutils .literal .notranslate}]{.pre}.

- Added Triton unsupported conversion from [`f8E4M3FNUZ`{.docutils .literal .notranslate}]{.pre} to [`fp16`{.docutils .literal .notranslate}]{.pre} with rounding mode.

- Introduced [`CudnnFusedConvDecomposer`{.code .docutils .literal .notranslate}]{.pre} to revert fused convolutions when [`ConvAlgorithmPicker`{.code .docutils .literal .notranslate}]{.pre} fails to find a fused algorithm, and removed unfused fallback paths from [`RocmFusedConvRunner`{.code .docutils .literal .notranslate}]{.pre}.
:::

::: {#key-features-and-enhancements-for-rocm-7-0 .section}
## Key features and enhancements for ROCm 7.0[\#](#key-features-and-enhancements-for-rocm-7-0 "Link to this heading"){.headerlink}

- Upgraded XLA backend: Integrates a newer XLA version, enabling better optimizations, broader operator support, and potential performance gains.

- RNN support: Native RNN support (including LSTMs via [`jax.experimental.rnn`{.docutils .literal .notranslate}]{.pre}) now available on ROCm, aiding sequence model development.

- Comprehensive linear algebra capabilities: Offers robust [`jax.linalg`{.docutils .literal .notranslate}]{.pre} operations, essential for scientific and machine learning tasks.

- Expanded AMD GPU architecture support: Provides ongoing support for gfx1101 GPUs and introduces support for gfx950 and gfx12xx GPUs.

- Mixed FP8 precision support: Enables [`lax.dot_general`{.docutils .literal .notranslate}]{.pre} operations with mixed FP8 types, offering pathways for memory and compute efficiency.

- Streamlined PyPi packaging: Provides reliable PyPi wheels for JAX on ROCm, simplifying the installation process.

- Pallas experimental kernel development: Continued Pallas framework enhancements for custom GPU kernels, including new intrinsics (specific kernel behaviors under review).

- Improved build system and CI: Enhanced ROCm build system and CI for greater reliability and maintainability.

- Enhanced distributed computing setup: Improved JAX setup in multi-GPU distributed environments.
:::

::: {#known-issues-and-notes-for-rocm-7-0 .section}
[]{#jax-comp-known-issues}

## Known issues and notes for ROCm 7.0[\#](#known-issues-and-notes-for-rocm-7-0 "Link to this heading"){.headerlink}

- [`nn.dot_product_attention`{.docutils .literal .notranslate}]{.pre}: Certain configurations of [`jax.nn.dot_product_attention`{.docutils .literal .notranslate}]{.pre} may cause segmentation faults, though the majority of use cases work correctly.

- SVD with dynamic shapes: SVD on inputs with dynamic/symbolic shapes might result in an error. SVD with static shapes is unaffected.

- QR decomposition with symbolic shapes: QR decomposition operations may fail when using symbolic/dynamic shapes in shape polymorphic contexts.

- Pallas kernels: Specific advanced Pallas kernels may exhibit variations in numerical output or resource usage. These are actively reviewed as part of Pallas's experimental development.
:::
::::::::::::::::::::::::::::::

::::: prev-next-area
[](tensorflow-compatibility.html "previous page"){.left-prev}

::: prev-next-info
previous

TensorFlow compatibility
:::

[](dgl-compatibility.html "next page"){.right-next}

::: prev-next-info
next

DGL compatibility
:::
:::::
:::::::::::::::::::::::::::::::::::::::::::::::

:::::: {.bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {.page-toc .tocsection .onthispage}
Contents
:::

- [Support overview](#support-overview){.reference .internal .nav-link}
  - [Version support](#version-support){.reference .internal .nav-link}
- [JAX Plugin-PJRT with JAX/JAXLIB compatibility](#jax-plugin-pjrt-with-jax-jaxlib-compatibility){.reference .internal .nav-link}
- [Use cases and recommendations](#use-cases-and-recommendations){.reference .internal .nav-link}
- [Docker image compatibility](#docker-image-compatibility){.reference .internal .nav-link}
- [Key ROCm libraries for JAX](#key-rocm-libraries-for-jax){.reference .internal .nav-link}
- [Supported data types and modules](#supported-data-types-and-modules){.reference .internal .nav-link}
  - [Supported data types](#supported-data-types){.reference .internal .nav-link}
  - [Supported modules](#supported-modules){.reference .internal .nav-link}
- [Key features and enhancements for ROCm 7.1](#key-features-and-enhancements-for-rocm-7-1){.reference .internal .nav-link}
- [Key features and enhancements for ROCm 7.0](#key-features-and-enhancements-for-rocm-7-0){.reference .internal .nav-link}
- [Known issues and notes for ROCm 7.0](#known-issues-and-notes-for-rocm-7-0){.reference .internal .nav-link}
::::
:::::
::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::
