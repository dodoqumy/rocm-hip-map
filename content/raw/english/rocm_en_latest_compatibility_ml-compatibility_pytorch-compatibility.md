---
title: "PyTorch compatibility"
source_url: "https://rocm.docs.amd.com/en/latest/compatibility/ml-compatibility/pytorch-compatibility.html"
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
- PyTorch\...
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
# PyTorch compatibility

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [Support overview](#support-overview){.reference .internal .nav-link}
  - [Version support](#version-support){.reference .internal .nav-link}
- [Use cases and recommendations](#use-cases-and-recommendations){.reference .internal .nav-link}
- [Docker image compatibility](#docker-image-compatibility){.reference .internal .nav-link}
- [Key ROCm libraries for PyTorch](#key-rocm-libraries-for-pytorch){.reference .internal .nav-link}
- [Supported modules and data types](#supported-modules-and-data-types){.reference .internal .nav-link}
  - [Supported data types](#supported-data-types){.reference .internal .nav-link}
  - [Supported modules](#supported-modules){.reference .internal .nav-link}
  - [Supported domain libraries](#supported-domain-libraries){.reference .internal .nav-link}
- [Key features and enhancements for PyTorch 2.9 with ROCm 7.2.1](#key-features-and-enhancements-for-pytorch-2-9-with-rocm-7-2-1){.reference .internal .nav-link}
- [Key features and enhancements for PyTorch 2.9 with ROCm 7.1.1](#key-features-and-enhancements-for-pytorch-2-9-with-rocm-7-1-1){.reference .internal .nav-link}
- [Key features and enhancements for PyTorch 2.8 with ROCm 7.1](#key-features-and-enhancements-for-pytorch-2-8-with-rocm-7-1){.reference .internal .nav-link}
- [Key features and enhancements for PyTorch 2.7/2.8 with ROCm 7.0](#key-features-and-enhancements-for-pytorch-2-7-2-8-with-rocm-7-0){.reference .internal .nav-link}
- [Known issues and notes for PyTorch 2.7/2.8 with ROCm 7.0 and ROCm 7.1](#known-issues-and-notes-for-pytorch-2-7-2-8-with-rocm-7-0-and-rocm-7-1){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

:::::::::::::::::::::::::::::: {#pytorch-compatibility .section}
# PyTorch compatibility[\#](#pytorch-compatibility "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-03-13
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 16 min read time
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

[PyTorch](https://pytorch.org/){.reference .external} is an open-source tensor library designed for deep learning. PyTorch on ROCm provides mixed-precision and large-scale training using [MIOpen](https://github.com/ROCm/MIOpen){.reference .external} and [RCCL](https://github.com/ROCm/rccl){.reference .external} libraries.

PyTorch provides two high-level features:

- Tensor computation (like NumPy) with strong GPU acceleration

- Deep neural networks built on a tape-based autograd system (rapid computation of multiple partial derivatives or gradients)

:::: {#support-overview .section}
## Support overview[\#](#support-overview "Link to this heading"){.headerlink}

ROCm support for PyTorch is upstreamed into the official PyTorch repository. ROCm development is aligned with the stable release of PyTorch, while upstream PyTorch testing uses the stable release of ROCm to maintain consistency:

- The ROCm-supported version of PyTorch is maintained in the official [ROCm/pytorch](https://github.com/ROCm/pytorch){.github .reference .external} repository, which differs from the [pytorch/pytorch](https://github.com/pytorch/pytorch){.github .reference .external} upstream repository.

- To get started and install PyTorch on ROCm, use the prebuilt [[Docker images]{.std .std-ref}](#pytorch-docker-compat){.reference .internal}, which include ROCm, PyTorch, and all required dependencies.

  - See the [[ROCm PyTorch installation guide]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/pytorch-install.html "(in ROCm installation on Linux v7.2.2)"){.reference .external} for installation and setup instructions.

  - You can also consult the upstream [Installation guide](https://pytorch.org/get-started/locally/){.reference .external} or [Previous versions](https://pytorch.org/get-started/previous-versions/){.reference .external} for additional context.

PyTorch includes tooling that generates HIP source code from the CUDA backend. This approach allows PyTorch to support ROCm without requiring manual code modifications. For more information, see [[HIPIFY]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/HIPIFY/en/latest/index.html "(in HIPIFY Documentation)"){.reference .external}.

::: {#version-support .section}
### Version support[\#](#version-support "Link to this heading"){.headerlink}

AMD releases official [ROCm PyTorch Docker images](https://hub.docker.com/r/rocm/pytorch/tags){.reference .external} quarterly alongside new ROCm releases. These images undergo full AMD testing.
:::
::::

::: {#use-cases-and-recommendations .section}
[]{#pytorch-recommendations}

## Use cases and recommendations[\#](#use-cases-and-recommendations "Link to this heading"){.headerlink}

- [[Using ROCm for AI: training a model]{.doc}](../../how-to/rocm-for-ai/training/benchmark-docker/pytorch-training.html){.reference .internal} guides how to leverage the ROCm platform for training AI models. It covers the steps, tools, and best practices for optimizing training workflows on AMD GPUs using PyTorch features.

- [[Single-GPU fine-tuning and inference]{.doc}](../../how-to/rocm-for-ai/fine-tuning/single-gpu-fine-tuning-and-inference.html){.reference .internal} describes and demonstrates how to use the ROCm platform for the fine-tuning and inference of machine learning models, particularly large language models (LLMs), on systems with a single GPU. This topic provides a detailed guide for setting up, optimizing, and executing fine-tuning and inference workflows in such environments.

- [[Multi-GPU fine-tuning and inference optimization]{.doc}](../../how-to/rocm-for-ai/fine-tuning/multi-gpu-fine-tuning-and-inference.html){.reference .internal} describes and demonstrates the fine-tuning and inference of machine learning models on systems with multiple GPUs.

- The [[Instinct MI300X workload optimization guide]{.doc}](../../how-to/rocm-for-ai/inference-optimization/workload.html){.reference .internal} provides detailed guidance on optimizing workloads for the AMD Instinct MI300X GPU using ROCm. This guide helps users achieve optimal performance for deep learning and other high-performance computing tasks on the MI300X GPU.

- The [[Inception with PyTorch documentation]{.doc}](../../conceptual/ai-pytorch-inception.html){.reference .internal} describes how PyTorch integrates with ROCm for AI workloads. It outlines the use of PyTorch on the ROCm platform and focuses on efficiently leveraging AMD GPU hardware for training and inference tasks in AI applications.

For more use cases and recommendations, see [ROCm PyTorch blog posts](https://rocm.blogs.amd.com/blog/tag/pytorch.html){.reference .external}.
:::

::: {#docker-image-compatibility .section}
[]{#pytorch-docker-compat}

## Docker image compatibility[\#](#docker-image-compatibility "Link to this heading"){.headerlink}

AMD validates and publishes [PyTorch images](https://hub.docker.com/r/rocm/pytorch/tags){.reference .external} with ROCm backends on Docker Hub.

To find the right image tag, see the [[PyTorch on ROCm installation documentation]{.xref .std .std-ref}](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/pytorch-install.html#pytorch-docker-support "(in ROCm installation on Linux v7.2.2)"){.reference .external} for a list of available [`rocm/pytorch`{.docutils .literal .notranslate}]{.pre} images.
:::

:::: {#key-rocm-libraries-for-pytorch .section}
## Key ROCm libraries for PyTorch[\#](#key-rocm-libraries-for-pytorch "Link to this heading"){.headerlink}

PyTorch functionality on ROCm is determined by its underlying library dependencies. These ROCm components affect the capabilities, performance, and feature set available to developers.

::: pst-scrollable-table-container
  ROCm library                                                                           Version                        Purpose                                                                                                                                                                      Used in
  -------------------------------------------------------------------------------------- ------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [Composable Kernel](https://github.com/ROCm/composable_kernel){.reference .external}   [1.2.0]{.version-reference}    Enables faster execution of core operations like matrix multiplication (GEMM), convolutions and transformations.                                                             Speeds up [`torch.permute`{.docutils .literal .notranslate}]{.pre}, [`torch.view`{.docutils .literal .notranslate}]{.pre}, [`torch.matmul`{.docutils .literal .notranslate}]{.pre}, [`torch.mm`{.docutils .literal .notranslate}]{.pre}, [`torch.bmm`{.docutils .literal .notranslate}]{.pre}, [`torch.nn.Conv2d`{.docutils .literal .notranslate}]{.pre}, [`torch.nn.Conv3d`{.docutils .literal .notranslate}]{.pre} and [`torch.nn.MultiheadAttention`{.docutils .literal .notranslate}]{.pre}.
  [hipBLAS](https://github.com/ROCm/hipBLAS){.reference .external}                       [3.2.0]{.version-reference}    Provides GPU-accelerated Basic Linear Algebra Subprograms (BLAS) for matrix and vector operations.                                                                           Supports operations such as matrix multiplication, matrix-vector products, and tensor contractions. Utilized in both dense and batched linear algebra operations.
  [hipBLASLt](https://github.com/ROCm/hipBLASLt){.reference .external}                   [1.2.2]{.version-reference}    hipBLASLt is an extension of the hipBLAS library, providing additional features like epilogues fused into the matrix multiplication kernel or use of integer tensor cores.   Accelerates operations such as [`torch.matmul`{.docutils .literal .notranslate}]{.pre}, [`torch.mm`{.docutils .literal .notranslate}]{.pre}, and the matrix multiplications used in convolutional and linear layers.
  [hipCUB](https://github.com/ROCm/hipCUB){.reference .external}                         [4.2.0]{.version-reference}    Provides a C++ template library for parallel algorithms for reduction, scan, sort and select.                                                                                Supports operations such as [`torch.sum`{.docutils .literal .notranslate}]{.pre}, [`torch.cumsum`{.docutils .literal .notranslate}]{.pre}, [`torch.sort`{.docutils .literal .notranslate}]{.pre} irregular shapes often involve scanning, sorting, and filtering, which hipCUB handles efficiently.
  [hipFFT](https://github.com/ROCm/hipFFT){.reference .external}                         [1.0.22]{.version-reference}   Provides GPU-accelerated Fast Fourier Transform (FFT) operations.                                                                                                            Used in functions like the [`torch.fft`{.docutils .literal .notranslate}]{.pre} module.
  [hipRAND](https://github.com/ROCm/hipRAND){.reference .external}                       [3.1.0]{.version-reference}    Provides fast random number generation for GPUs.                                                                                                                             The [`torch.rand`{.docutils .literal .notranslate}]{.pre}, [`torch.randn`{.docutils .literal .notranslate}]{.pre}, and stochastic layers like [`torch.nn.Dropout`{.docutils .literal .notranslate}]{.pre} rely on hipRAND.
  [hipSOLVER](https://github.com/ROCm/hipSOLVER){.reference .external}                   [3.2.0]{.version-reference}    Provides GPU-accelerated solvers for linear systems, eigenvalues, and singular value decompositions (SVD).                                                                   Supports functions like [`torch.linalg.solve`{.docutils .literal .notranslate}]{.pre}, [`torch.linalg.eig`{.docutils .literal .notranslate}]{.pre}, and [`torch.linalg.svd`{.docutils .literal .notranslate}]{.pre}.
  [hipSPARSE](https://github.com/ROCm/hipSPARSE){.reference .external}                   [4.2.0]{.version-reference}    Accelerates operations on sparse matrices, such as sparse matrix-vector or matrix-matrix products.                                                                           Sparse tensor operations [`torch.sparse`{.docutils .literal .notranslate}]{.pre}.
  [hipSPARSELt](https://github.com/ROCm/hipSPARSELt){.reference .external}               [0.2.6]{.version-reference}    Accelerates operations on sparse matrices, such as sparse matrix-vector or matrix-matrix products.                                                                           Sparse tensor operations [`torch.sparse`{.docutils .literal .notranslate}]{.pre}.
  [hipTensor](https://github.com/ROCm/hipTensor){.reference .external}                   [2.2.0]{.version-reference}    Optimizes for high-performance tensor operations, such as contractions.                                                                                                      Accelerates tensor algebra, especially in deep learning and scientific computing.
  [MIOpen](https://github.com/ROCm/MIOpen){.reference .external}                         [3.5.1]{.version-reference}    Optimizes deep learning primitives such as convolutions, pooling, normalization, and activation functions.                                                                   Speeds up convolutional neural networks (CNNs), recurrent neural networks (RNNs), and other layers. Used in operations like [`torch.nn.Conv2d`{.docutils .literal .notranslate}]{.pre}, [`torch.nn.ReLU`{.docutils .literal .notranslate}]{.pre}, and [`torch.nn.LSTM`{.docutils .literal .notranslate}]{.pre}.
  [MIGraphX](https://github.com/ROCm/AMDMIGraphX){.reference .external}                  [2.15.0]{.version-reference}   Adds graph-level optimizations, ONNX models and mixed precision support and enable Ahead-of-Time (AOT) Compilation.                                                          Speeds up inference models and executes ONNX models for compatibility with other frameworks. [`torch.nn.Conv2d`{.docutils .literal .notranslate}]{.pre}, [`torch.nn.ReLU`{.docutils .literal .notranslate}]{.pre}, and [`torch.nn.LSTM`{.docutils .literal .notranslate}]{.pre}.
  [MIVisionX](https://github.com/ROCm/MIVisionX){.reference .external}                   [3.5.0]{.version-reference}    Optimizes acceleration for computer vision and AI workloads like preprocessing, augmentation, and inferencing.                                                               Faster data preprocessing and augmentation pipelines for datasets like ImageNet or COCO and easy to integrate into PyTorch's [`torch.utils.data`{.docutils .literal .notranslate}]{.pre} and [`torchvision`{.docutils .literal .notranslate}]{.pre} workflows.
  [rocAL](https://github.com/ROCm/rocAL){.reference .external}                           [2.5.0]{.version-reference}    Accelerates the data pipeline by offloading intensive preprocessing and augmentation tasks. rocAL is part of MIVisionX.                                                      Easy to integrate into PyTorch's [`torch.utils.data`{.docutils .literal .notranslate}]{.pre} and [`torchvision`{.docutils .literal .notranslate}]{.pre} data load workloads.
  [RCCL](https://github.com/ROCm/rccl){.reference .external}                             [2.27.7]{.version-reference}   Optimizes for multi-GPU communication for operations like AllReduce and Broadcast.                                                                                           Distributed data parallel training ([`torch.nn.parallel.DistributedDataParallel`{.docutils .literal .notranslate}]{.pre}). Handles communication in multi-GPU setups.
  [rocDecode](https://github.com/ROCm/rocDecode){.reference .external}                   [1.7.0]{.version-reference}    Provides hardware-accelerated data decoding capabilities, particularly for image, video, and other dataset formats.                                                          Can be integrated in [`torch.utils.data`{.docutils .literal .notranslate}]{.pre}, [`torchvision.transforms`{.docutils .literal .notranslate}]{.pre} and [`torch.distributed`{.docutils .literal .notranslate}]{.pre}.
  [rocJPEG](https://github.com/ROCm/rocJPEG){.reference .external}                       [1.4.0]{.version-reference}    Provides hardware-accelerated JPEG image decoding and encoding.                                                                                                              GPU accelerated [`torchvision.io.decode_jpeg`{.docutils .literal .notranslate}]{.pre} and [`torchvision.io.encode_jpeg`{.docutils .literal .notranslate}]{.pre} and can be integrated in [`torch.utils.data`{.docutils .literal .notranslate}]{.pre} and [`torchvision`{.docutils .literal .notranslate}]{.pre}.
  [RPP](https://github.com/ROCm/RPP){.reference .external}                               [2.2.1]{.version-reference}    Speeds up data augmentation, transformation, and other preprocessing steps.                                                                                                  Easy to integrate into PyTorch's [`torch.utils.data`{.docutils .literal .notranslate}]{.pre} and [`torchvision`{.docutils .literal .notranslate}]{.pre} data load workloads to speed up data processing.
  [rocThrust](https://github.com/ROCm/rocThrust){.reference .external}                   [4.2.0]{.version-reference}    Provides a C++ template library for parallel algorithms like sorting, reduction, and scanning.                                                                               Utilized in backend operations for tensor computations requiring parallel processing.
  [rocWMMA](https://github.com/ROCm/rocWMMA){.reference .external}                       [2.2.0]{.version-reference}    Accelerates warp-level matrix-multiply and matrix-accumulate to speed up matrix multiplication (GEMM) and accumulation operations with mixed precision support.              Linear layers ([`torch.nn.Linear`{.docutils .literal .notranslate}]{.pre}), convolutional layers ([`torch.nn.Conv2d`{.docutils .literal .notranslate}]{.pre}), attention layers, general tensor operations that involve matrix products, such as [`torch.matmul`{.docutils .literal .notranslate}]{.pre}, [`torch.bmm`{.docutils .literal .notranslate}]{.pre}, and more.
:::
::::

::::::::: {#supported-modules-and-data-types .section}
## Supported modules and data types[\#](#supported-modules-and-data-types "Link to this heading"){.headerlink}

The following section outlines the supported data types, modules, and domain libraries available in PyTorch on ROCm.

::::: {#supported-data-types .section}
### Supported data types[\#](#supported-data-types "Link to this heading"){.headerlink}

The tensor data type is specified using the [`dtype`{.docutils .literal .notranslate}]{.pre} attribute or argument. PyTorch supports many data types for different use cases.

The following table lists [torch.Tensor](https://pytorch.org/docs/stable/tensors.html){.reference .external} single data types:

::: pst-scrollable-table-container
  Data type                                                                                                                 Description
  ------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------
  [`torch.float8_e4m3fn`{.docutils .literal .notranslate}]{.pre}                                                            8-bit floating point, e4m3
  [`torch.float8_e5m2`{.docutils .literal .notranslate}]{.pre}                                                              8-bit floating point, e5m2
  [`torch.float16`{.docutils .literal .notranslate}]{.pre} or [`torch.half`{.docutils .literal .notranslate}]{.pre}         16-bit floating point
  [`torch.bfloat16`{.docutils .literal .notranslate}]{.pre}                                                                 16-bit floating point
  [`torch.float32`{.docutils .literal .notranslate}]{.pre} or [`torch.float`{.docutils .literal .notranslate}]{.pre}        32-bit floating point
  [`torch.float64`{.docutils .literal .notranslate}]{.pre} or [`torch.double`{.docutils .literal .notranslate}]{.pre}       64-bit floating point
  [`torch.complex32`{.docutils .literal .notranslate}]{.pre} or [`torch.chalf`{.docutils .literal .notranslate}]{.pre}      32-bit complex numbers
  [`torch.complex64`{.docutils .literal .notranslate}]{.pre} or [`torch.cfloat`{.docutils .literal .notranslate}]{.pre}     64-bit complex numbers
  [`torch.complex128`{.docutils .literal .notranslate}]{.pre} or [`torch.cdouble`{.docutils .literal .notranslate}]{.pre}   128-bit complex numbers
  [`torch.uint8`{.docutils .literal .notranslate}]{.pre}                                                                    8-bit integer (unsigned)
  [`torch.uint16`{.docutils .literal .notranslate}]{.pre}                                                                   16-bit integer (unsigned); Not natively supported in ROCm
  [`torch.uint32`{.docutils .literal .notranslate}]{.pre}                                                                   32-bit integer (unsigned); Not natively supported in ROCm
  [`torch.uint64`{.docutils .literal .notranslate}]{.pre}                                                                   64-bit integer (unsigned); Not natively supported in ROCm
  [`torch.int8`{.docutils .literal .notranslate}]{.pre}                                                                     8-bit integer (signed)
  [`torch.int16`{.docutils .literal .notranslate}]{.pre} or [`torch.short`{.docutils .literal .notranslate}]{.pre}          16-bit integer (signed)
  [`torch.int32`{.docutils .literal .notranslate}]{.pre} or [`torch.int`{.docutils .literal .notranslate}]{.pre}            32-bit integer (signed)
  [`torch.int64`{.docutils .literal .notranslate}]{.pre} or [`torch.long`{.docutils .literal .notranslate}]{.pre}           64-bit integer (signed)
  [`torch.bool`{.docutils .literal .notranslate}]{.pre}                                                                     Boolean
  [`torch.quint8`{.docutils .literal .notranslate}]{.pre}                                                                   Quantized 8-bit integer (unsigned)
  [`torch.qint8`{.docutils .literal .notranslate}]{.pre}                                                                    Quantized 8-bit integer (signed)
  [`torch.qint32`{.docutils .literal .notranslate}]{.pre}                                                                   Quantized 32-bit integer (signed)
  [`torch.quint4x2`{.docutils .literal .notranslate}]{.pre}                                                                 Quantized 4-bit integer (unsigned)
:::

::: {.admonition .note}
Note

Unsigned types, except [`uint8`{.docutils .literal .notranslate}]{.pre}, have limited support in eager mode. They primarily exist to assist usage with [`torch.compile`{.docutils .literal .notranslate}]{.pre}.

See [[ROCm precision support]{.xref .std .std-doc}](https://rocm.docs.amd.com/en/latest/reference/precision-support.html "(in ROCm Documentation v7.2.2)"){.reference .external} for the native hardware support of data types.
:::
:::::

::: {#supported-modules .section}
### Supported modules[\#](#supported-modules "Link to this heading"){.headerlink}

For a complete and up-to-date list of PyTorch core modules (for example., [`torch`{.docutils .literal .notranslate}]{.pre}, [`torch.nn`{.docutils .literal .notranslate}]{.pre}, [`torch.cuda`{.docutils .literal .notranslate}]{.pre}, [`torch.backends.cuda`{.docutils .literal .notranslate}]{.pre} and [`torch.backends.cudnn`{.docutils .literal .notranslate}]{.pre}), their descriptions, and usage, please refer directly to the [official PyTorch documentation](https://pytorch.org/docs/stable/index.html){.reference .external}.

Core PyTorch functionality on ROCm includes tensor operations, neural network layers, automatic differentiation, distributed training, mixed-precision training, compilation features, and domain-specific libraries for audio, vision, text processing, and more.
:::

:::: {#supported-domain-libraries .section}
### Supported domain libraries[\#](#supported-domain-libraries "Link to this heading"){.headerlink}

PyTorch offers specialized [domain libraries](https://pytorch.org/domains/){.reference .external} with GPU acceleration that build on its core features to support specific application areas. The table below lists the PyTorch domain libraries that are compatible with ROCm.

::: pst-scrollable-table-container
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Library                                                                                    | Description                                                                                                                                                                                                                                                |
+============================================================================================+============================================================================================================================================================================================================================================================+
| [torchaudio](https://docs.pytorch.org/audio/stable/index.html){.reference .external}       | Audio and signal processing library for PyTorch. Provides utilities for audio I/O, signal and data processing functions, datasets, model implementations, and application components for audio and speech processing tasks.                                |
|                                                                                            |                                                                                                                                                                                                                                                            |
|                                                                                            | **Note:** To ensure GPU-acceleration with [`torchaudio.transforms`{.docutils .literal .notranslate}]{.pre}, you need to explicitly move audio data (waveform tensor) to GPU using [`.to('cuda')`{.docutils .literal .notranslate}]{.pre}.                  |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [torchtune](https://meta-pytorch.org/torchtune/stable/index.html){.reference .external}    | PyTorch-native library designed for fine-tuning large language models (LLMs). Provides supports the full fine-tuning workflow and offers compatibility with popular production inference systems.                                                          |
|                                                                                            |                                                                                                                                                                                                                                                            |
|                                                                                            | **Note:** Only official release exists.                                                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [torchvision](https://docs.pytorch.org/vision/stable/index.html){.reference .external}     | Computer vision library that is part of the PyTorch project. Provides popular datasets, model architectures, and common image transformations for computer vision applications.                                                                            |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [torchdata](https://meta-pytorch.org/data/beta/index.html#torchdata){.reference .external} | Beta library of common modular data loading primitives for easily constructing flexible and performant data pipelines, with features still in prototype stage.                                                                                             |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [torchrec](https://meta-pytorch.org/torchrec/){.reference .external}                       | PyTorch domain library for common sparsity and parallelism primitives needed for large-scale recommender systems, enabling authors to train models with large embedding tables shared across many GPUs.                                                    |
|                                                                                            |                                                                                                                                                                                                                                                            |
|                                                                                            | **Note:** [`torchrec`{.docutils .literal .notranslate}]{.pre} does not implement ROCm-specific kernels. ROCm acceleration is provided through the underlying PyTorch framework and ROCm library integration.                                               |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [torchserve](https://docs.pytorch.org/serve/){.reference .external}                        | Performant, flexible and easy-to-use tool for serving PyTorch models in production, providing features for model management, batch processing, and scalable deployment.                                                                                    |
|                                                                                            |                                                                                                                                                                                                                                                            |
|                                                                                            | **Note:** [torchserve](https://docs.pytorch.org/serve/){.reference .external} is no longer actively maintained. Last official release is sent out with PyTorch 2.4.                                                                                        |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [torchrl](https://docs.pytorch.org/rl/stable/index.html){.reference .external}             | Open-source, Python-first Reinforcement Learning library for PyTorch with a focus on high modularity and good runtime performance, providing low and high-level RL abstractions and reusable functionals for cost functions, returns, and data processing. |
|                                                                                            |                                                                                                                                                                                                                                                            |
|                                                                                            | **Note:** Only official release exists.                                                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [tensordict](https://docs.pytorch.org/tensordict/stable/index.html){.reference .external}  | Dictionary-like class that simplifies operations on batches of tensors, enhancing code readability, compactness, and modularity by abstracting tailored operations and reducing errors through automatic operation dispatching.                            |
|                                                                                            |                                                                                                                                                                                                                                                            |
|                                                                                            | **Note:** Only official release exists.                                                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
:::
::::
:::::::::

::: {#key-features-and-enhancements-for-pytorch-2-9-with-rocm-7-2-1 .section}
## Key features and enhancements for PyTorch 2.9 with ROCm 7.2.1[\#](#key-features-and-enhancements-for-pytorch-2-9-with-rocm-7-2-1 "Link to this heading"){.headerlink}

- Added Triton 3.6.x performance optimization for reduction, POI, and GEMM kernels.

- Updated native reduction kernel config for better performance on AMD GPUs.

- Optimized single-block TopK kernels with warp-level compaction.

- Optimized Radix Select by caching data on shared memory.

- Optimized Flex-Attention occupancy for head_dim=128.

- Enabled hipSOLVER path for linalg operations - cholesky, lstsq, and gels.
:::

::: {#key-features-and-enhancements-for-pytorch-2-9-with-rocm-7-1-1 .section}
## Key features and enhancements for PyTorch 2.9 with ROCm 7.1.1[\#](#key-features-and-enhancements-for-pytorch-2-9-with-rocm-7-1-1 "Link to this heading"){.headerlink}

- Scaled Dot Product Attention (SDPA) upgraded to use AOTriton version 0.11b.

- Default hipBLASLt support enabled for gfx908 architecture on ROCm 6.3 and later.

- MIOpen now supports channels last memory format for 3D convolutions and batch normalization.

- NHWC convolution operations in MIOpen optimized by eliminating unnecessary transpose operations.

- Improved tensor.item() performance by removing redundant synchronization.

- Enhanced performance for element-wise operations and reduction kernels.

- Added support for grouped GEMM operations through fbgemm_gpu generative AI components.

- Resolved device error in Inductor when using CUDA graph trees with HIP.

- Corrected logsumexp scaling in AOTriton-based SDPA implementation.

- Added stream graph capture status validation in memory copy synchronization functions.
:::

::: {#key-features-and-enhancements-for-pytorch-2-8-with-rocm-7-1 .section}
## Key features and enhancements for PyTorch 2.8 with ROCm 7.1[\#](#key-features-and-enhancements-for-pytorch-2-8-with-rocm-7-1 "Link to this heading"){.headerlink}

- MIOpen deep learning optimizations: Further optimized NHWC BatchNorm feature.

- Added float8 support for the DeepSpeed extension, allowing for decreased memory footprint and increased throughput in training and inference workloads.

- [`torch.nn.functional.scaled_dot_product_attention`{.docutils .literal .notranslate}]{.pre} now calling optimized flash attention kernel automatically.
:::

::: {#key-features-and-enhancements-for-pytorch-2-7-2-8-with-rocm-7-0 .section}
## Key features and enhancements for PyTorch 2.7/2.8 with ROCm 7.0[\#](#key-features-and-enhancements-for-pytorch-2-7-2-8-with-rocm-7-0 "Link to this heading"){.headerlink}

- Enhanced TunableOp framework: Introduces [`tensorfloat32`{.docutils .literal .notranslate}]{.pre} support for TunableOp operations, improved offline tuning for ScaledGEMM operations, submatrix offline tuning capabilities, and better logging for BLAS operations without bias vectors.

- Expanded GPU architecture support: Provides optimized support for newer GPU architectures, including gfx1200 and gfx1201 with preferred hipBLASLt backend selection, along with improvements for gfx950 and gfx1100 Series GPUs.

- Advanced Triton Integration: AOTriton 0.10b introduces official support for gfx950 and gfx1201, along with experimental support for gfx1101, gfx1151, gfx1150, and gfx1200.

- Improved element-wise kernel performance: Delivers enhanced vectorized element-wise kernels with better support for heterogeneous tensor types and optimized input vectorization for tensors with mixed data types.

- MIOpen deep learning optimizations: Enables NHWC BatchNorm by default on ROCm 7.0+, provides [`maxpool`{.docutils .literal .notranslate}]{.pre} forward and backward performance improvements targeting ResNet scenarios, and includes updated launch configurations for better performance.

- Enhanced memory and tensor operations: Features fixes for in-place [`aten`{.docutils .literal .notranslate}]{.pre} sum operations with specialized templated kernels, improved 3D tensor performance with NHWC format, and better handling of memory-bound matrix multiplication operations.

- Robust testing and quality improvements: Includes comprehensive test suite updates with improved tolerance handling for Navi3x architectures, generalized ROCm-specific test conditions, and enhanced unit test coverage for Flash Attention and Memory Efficient operations.

- Composable Kernel (CK) updates: Features updated CK submodule integration with the latest optimizations and performance improvements for core mathematical operations.

- Development and debugging enhancements: Includes improved source handling for dynamic compilation, better error handling for atomic operations, and enhanced state checking for trace operations.

- Integrate APEX fused layer normalization, which can have positive impact on text-to-video models.

- Integrate APEX distributed fused LAMB and distributed fused ADAM, which can have positive impact on BERT-L and Llama2-SFT.

- FlashAttention v3 has been integrated for AMD GPUs.

- [Pytorch C++ extensions](https://pytorch.org/tutorials/advanced/cpp_extension.html){.reference .external} provide a mechanism for compiling custom operations that can be used during network training or inference. For AMD platforms, [`amdclang++`{.docutils .literal .notranslate}]{.pre} has been validated as the supported compiler for building these extensions.
:::

::: {#known-issues-and-notes-for-pytorch-2-7-2-8-with-rocm-7-0-and-rocm-7-1 .section}
## Known issues and notes for PyTorch 2.7/2.8 with ROCm 7.0 and ROCm 7.1[\#](#known-issues-and-notes-for-pytorch-2-7-2-8-with-rocm-7-0-and-rocm-7-1 "Link to this heading"){.headerlink}

- The [`matmul.allow_fp16_reduced_precision_reduction`{.docutils .literal .notranslate}]{.pre} and [`matmul.allow_bf16_reduced_precision_reduction`{.docutils .literal .notranslate}]{.pre} options under [`torch.backends.cuda`{.docutils .literal .notranslate}]{.pre} are not supported. As a result, reduced-precision reductions using FP16 or BF16 accumulation types are not available.
:::
::::::::::::::::::::::::::::::

::::: prev-next-area
[](../../how-to/deep-learning-rocm.html "previous page"){.left-prev}

::: prev-next-info
previous

Deep learning frameworks for ROCm
:::

[](tensorflow-compatibility.html "next page"){.right-next}

::: prev-next-info
next

TensorFlow compatibility
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
- [Use cases and recommendations](#use-cases-and-recommendations){.reference .internal .nav-link}
- [Docker image compatibility](#docker-image-compatibility){.reference .internal .nav-link}
- [Key ROCm libraries for PyTorch](#key-rocm-libraries-for-pytorch){.reference .internal .nav-link}
- [Supported modules and data types](#supported-modules-and-data-types){.reference .internal .nav-link}
  - [Supported data types](#supported-data-types){.reference .internal .nav-link}
  - [Supported modules](#supported-modules){.reference .internal .nav-link}
  - [Supported domain libraries](#supported-domain-libraries){.reference .internal .nav-link}
- [Key features and enhancements for PyTorch 2.9 with ROCm 7.2.1](#key-features-and-enhancements-for-pytorch-2-9-with-rocm-7-2-1){.reference .internal .nav-link}
- [Key features and enhancements for PyTorch 2.9 with ROCm 7.1.1](#key-features-and-enhancements-for-pytorch-2-9-with-rocm-7-1-1){.reference .internal .nav-link}
- [Key features and enhancements for PyTorch 2.8 with ROCm 7.1](#key-features-and-enhancements-for-pytorch-2-8-with-rocm-7-1){.reference .internal .nav-link}
- [Key features and enhancements for PyTorch 2.7/2.8 with ROCm 7.0](#key-features-and-enhancements-for-pytorch-2-7-2-8-with-rocm-7-0){.reference .internal .nav-link}
- [Known issues and notes for PyTorch 2.7/2.8 with ROCm 7.0 and ROCm 7.1](#known-issues-and-notes-for-pytorch-2-7-2-8-with-rocm-7-0-and-rocm-7-1){.reference .internal .nav-link}
::::
:::::
::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::
