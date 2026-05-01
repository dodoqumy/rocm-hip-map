---
title: "DGL compatibility"
source_url: "https://rocm.docs.amd.com/en/latest/compatibility/ml-compatibility/dgl-compatibility.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-01
---

:::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

:::::::::::::::::::::::::::::::::::::::::::: bd-content
::::::::::::::::::::::::::::::::::::::: bd-article-container
:::::::::: {.bd-header-article .d-print-none}
::::::::: {.header-article-items .header-article__inner}
::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}
:::

::: header-article-item
- [](../../index.html){.nav-link aria-label="Home"}
- [Deep learning frameworks for ROCm](../../how-to/deep-learning-rocm.html){.nav-link}
- DGL compatibility
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
# DGL compatibility

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [Support overview](#support-overview){.reference .internal .nav-link}
- [Compatibility matrix](#compatibility-matrix){.reference .internal .nav-link}
- [Key ROCm libraries for DGL](#key-rocm-libraries-for-dgl){.reference .internal .nav-link}
- [Supported features with ROCm 7.0.0](#supported-features-with-rocm-7-0-0){.reference .internal .nav-link}
- [Unsupported features with ROCm 7.0.0](#unsupported-features-with-rocm-7-0-0){.reference .internal .nav-link}
- [Unsupported functions with ROCm 7.0.0](#unsupported-functions-with-rocm-7-0-0){.reference .internal .nav-link}
- [Use cases and recommendations](#use-cases-and-recommendations){.reference .internal .nav-link}
- [Previous versions](#previous-versions){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

:::::::::::::::::::::: {#dgl-compatibility .section}
# DGL compatibility[\#](#dgl-compatibility "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 9 min read time
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

Deep Graph Library ([DGL](https://www.dgl.ai/){.reference .external}) is an easy-to-use, high-performance, and scalable Python package for deep learning on graphs. DGL is framework agnostic, meaning that if a deep graph model is a component in an end-to-end application, the rest of the logic is implemented using PyTorch.

DGL provides a high-performance graph object that can reside on either CPUs or GPUs. It bundles structural data features for better control and provides a variety of functions for computing with graph objects, including efficient and customizable message passing primitives for Graph Neural Networks.

::: {#support-overview .section}
## Support overview[\#](#support-overview "Link to this heading"){.headerlink}

- The ROCm-supported version of DGL is maintained in the official [ROCm/dgl](https://github.com/ROCm/dgl){.github .reference .external} repository, which differs from the [dmlc/dgl](https://github.com/dmlc/dgl){.github .reference .external} upstream repository.

- To get started and install DGL on ROCm, use the prebuilt [[Docker images]{.std .std-ref}](#dgl-docker-compat){.reference .internal}, which include ROCm, DGL, and all required dependencies.

  - See the [[ROCm DGL installation guide]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/dgl-install.html "(in ROCm installation on Linux v7.2.2)"){.reference .external} for installation and setup instructions.

  - You can also consult the upstream [Installation guide](https://www.dgl.ai/pages/start.html){.reference .external} for additional context.
:::

:::: {#compatibility-matrix .section}
[]{#dgl-docker-compat}

## Compatibility matrix[\#](#compatibility-matrix "Link to this heading"){.headerlink}

AMD validates and publishes [DGL images](https://hub.docker.com/r/rocm/dgl/tags){.reference .external} with ROCm backends on Docker Hub. The following Docker image tags and associated inventories represent the latest available DGL version from the official Docker Hub. Click the to view the image on Docker Hub.

::: pst-scrollable-table-container
  Docker image                                                                                                                                                                                   ROCm                                                                     DGL                                                                              PyTorch                                                                                 Ubuntu   Python                                                                                    GPU
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------ -------------------------------------------------------------------------------- --------------------------------------------------------------------------------------- -------- ----------------------------------------------------------------------------------------- ----------------
  [ rocm/dgl](https://hub.docker.com/layers/rocm/dgl/dgl-2.4.0.amd0_rocm7.0.0_ubuntu24.04_py3.12_pytorch_2.8.0/images/sha256-943698ddf54c22a7bcad2e5b4ff467752e29e4ba6d0c926789ae7b242cbd92dd)   [7.0.0](https://repo.radeon.com/rocm/apt/7.0/){.reference .external}     [2.4.0](https://github.com/dmlc/dgl/releases/tag/v2.4.0){.reference .external}   [2.8.0](https://github.com/pytorch/pytorch/releases/tag/v2.8.0){.reference .external}   24.04    [3.12.9](https://www.python.org/downloads/release/python-3129/){.reference .external}     MI300X, MI250X
  [ rocm/dgl](https://hub.docker.com/layers/rocm/dgl/dgl-2.4.0.amd0_rocm7.0.0_ubuntu24.04_py3.12_pytorch_2.6.0/images/sha256-b2ec286a035eb7d0a6aab069561914d21a3cac462281e9c024501ba5ccedfbf7)   [7.0.0](https://repo.radeon.com/rocm/apt/7.0/){.reference .external}     [2.4.0](https://github.com/dmlc/dgl/releases/tag/v2.4.0){.reference .external}   [2.6.0](https://github.com/pytorch/pytorch/releases/tag/v2.6.0){.reference .external}   24.04    [3.12.9](https://www.python.org/downloads/release/python-3129/){.reference .external}     MI300X, MI250X
  [ rocm/dgl](https://hub.docker.com/layers/rocm/dgl/dgl-2.4.0.amd0_rocm7.0.0_ubuntu22.04_py3.10_pytorch_2.7.1/images/sha256-d27aee16df922ccf0bcd9107bfcb6d20d34235445d456c637e33ca6f19d11a51)   [7.0.0](https://repo.radeon.com/rocm/apt/7.0/){.reference .external}     [2.4.0](https://github.com/dmlc/dgl/releases/tag/v2.4.0){.reference .external}   [2.7.1](https://github.com/pytorch/pytorch/releases/tag/v2.7.1){.reference .external}   22.04    [3.10.16](https://www.python.org/downloads/release/python-31016/){.reference .external}   MI300X, MI250X
  [ rocm/dgl](https://hub.docker.com/layers/rocm/dgl/dgl-2.4.0.amd0_rocm6.4.3_ubuntu24.04_py3.12_pytorch_2.6.0/images/sha256-f3ba6a3c9ec9f6c1cde28449dc9780e0c4c16c4140f4b23f158565fbfd422d6b)   [6.4.3](https://repo.radeon.com/rocm/apt/6.4.3/){.reference .external}   [2.4.0](https://github.com/dmlc/dgl/releases/tag/v2.4.0){.reference .external}   [2.6.0](https://github.com/pytorch/pytorch/releases/tag/v2.6.0){.reference .external}   24.04    [3.12.9](https://www.python.org/downloads/release/python-3129/){.reference .external}     MI300X, MI250X
  [ rocm/dgl](https://hub.docker.com/layers/rocm/dgl/dgl-2.4_rocm6.4_ubuntu24.04_py3.12_pytorch_release_2.6.0/images/sha256-8ce2c3bcfaa137ab94a75f9e2ea711894748980f57417739138402a542dd5564)    [6.4.0](https://repo.radeon.com/rocm/apt/6.4/){.reference .external}     [2.4.0](https://github.com/dmlc/dgl/releases/tag/v2.4.0){.reference .external}   [2.6.0](https://github.com/pytorch/pytorch/releases/tag/v2.6.0){.reference .external}   24.04    [3.12.9](https://www.python.org/downloads/release/python-3129/){.reference .external}     MI300X, MI250X
  [ rocm/dgl](https://hub.docker.com/layers/rocm/dgl/dgl-2.4_rocm6.4_ubuntu24.04_py3.12_pytorch_release_2.4.1/images/sha256-cf1683283b8eeda867b690229c8091c5bbf1edb9f52e8fb3da437c49a612ebe4)    [6.4.0](https://repo.radeon.com/rocm/apt/6.4/){.reference .external}     [2.4.0](https://github.com/dmlc/dgl/releases/tag/v2.4.0){.reference .external}   [2.4.1](https://github.com/pytorch/pytorch/releases/tag/v2.4.1){.reference .external}   24.04    [3.12.9](https://www.python.org/downloads/release/python-3129/){.reference .external}     MI300X, MI250X
  [ rocm/dgl](https://hub.docker.com/layers/rocm/dgl/dgl-2.4_rocm6.4_ubuntu22.04_py3.10_pytorch_release_2.4.1/images/sha256-4834f178c3614e2d09e89e32041db8984c456d45dfd20286e377ca8635686554)    [6.4.0](https://repo.radeon.com/rocm/apt/6.4/){.reference .external}     [2.4.0](https://github.com/dmlc/dgl/releases/tag/v2.4.0){.reference .external}   [2.4.1](https://github.com/pytorch/pytorch/releases/tag/v2.4.1){.reference .external}   22.04    [3.10.16](https://www.python.org/downloads/release/python-31016/){.reference .external}   MI300X, MI250X
  [ rocm/dgl](https://hub.docker.com/layers/rocm/dgl/dgl-2.4_rocm6.4_ubuntu22.04_py3.10_pytorch_release_2.3.0/images/sha256-88740a2c8ab4084b42b10c3c6ba984cab33dd3a044f479c6d7618e2b2cb05e69)    [6.4.0](https://repo.radeon.com/rocm/apt/6.4/){.reference .external}     [2.4.0](https://github.com/dmlc/dgl/releases/tag/v2.4.0){.reference .external}   [2.3.0](https://github.com/pytorch/pytorch/releases/tag/v2.3.0){.reference .external}   22.04    [3.10.16](https://www.python.org/downloads/release/python-31016/){.reference .external}   MI300X, MI250X
:::
::::

:::: {#key-rocm-libraries-for-dgl .section}
[]{#dgl-key-rocm-libraries}

## Key ROCm libraries for DGL[\#](#key-rocm-libraries-for-dgl "Link to this heading"){.headerlink}

DGL on ROCm depends on specific libraries that affect its features and performance. Using the DGL Docker container or building it with the provided Docker file or a ROCm base image is recommended. If you prefer to build it yourself, ensure the following dependencies are installed:

::: pst-scrollable-table-container
  ROCm library                                                                           ROCm 7.0.0 Version   ROCm 6.4.x Version   Purpose
  -------------------------------------------------------------------------------------- -------------------- -------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [Composable Kernel](https://github.com/ROCm/composable_kernel){.reference .external}   1.1.0                1.1.0                Enables faster execution of core operations like matrix multiplication (GEMM), convolutions and transformations.
  [hipBLAS](https://github.com/ROCm/hipBLAS){.reference .external}                       3.0.0                2.4.0                Provides GPU-accelerated Basic Linear Algebra Subprograms (BLAS) for matrix and vector operations.
  [hipBLASLt](https://github.com/ROCm/hipBLASLt){.reference .external}                   1.0.0                0.12.0               hipBLASLt is an extension of the hipBLAS library, providing additional features like epilogues fused into the matrix multiplication kernel or use of integer tensor cores.
  [hipCUB](https://github.com/ROCm/hipCUB){.reference .external}                         4.0.0                3.4.0                Provides a C++ template library for parallel algorithms for reduction, scan, sort and select.
  [hipFFT](https://github.com/ROCm/hipFFT){.reference .external}                         1.0.20               1.0.18               Provides GPU-accelerated Fast Fourier Transform (FFT) operations.
  [hipRAND](https://github.com/ROCm/hipRAND){.reference .external}                       3.0.0                2.12.0               Provides fast random number generation for GPUs.
  [hipSOLVER](https://github.com/ROCm/hipSOLVER){.reference .external}                   3.0.0                2.4.0                Provides GPU-accelerated solvers for linear systems, eigenvalues, and singular value decompositions (SVD).
  [hipSPARSE](https://github.com/ROCm/hipSPARSE){.reference .external}                   4.0.1                3.2.0                Accelerates operations on sparse matrices, such as sparse matrix-vector or matrix-matrix products.
  [hipSPARSELt](https://github.com/ROCm/hipSPARSELt){.reference .external}               0.2.4                0.2.3                Accelerates operations on sparse matrices, such as sparse matrix-vector or matrix-matrix products.
  [hipTensor](https://github.com/ROCm/hipTensor){.reference .external}                   2.0.0                1.5.0                Optimizes for high-performance tensor operations, such as contractions.
  [MIOpen](https://github.com/ROCm/MIOpen){.reference .external}                         3.5.0                3.4.0                Optimizes deep learning primitives such as convolutions, pooling, normalization, and activation functions.
  [MIGraphX](https://github.com/ROCm/AMDMIGraphX){.reference .external}                  2.13.0               2.12.0               Adds graph-level optimizations, ONNX models and mixed precision support and enable Ahead-of-Time (AOT) Compilation.
  [MIVisionX](https://github.com/ROCm/MIVisionX){.reference .external}                   3.3.0                3.2.0                Optimizes acceleration for computer vision and AI workloads like preprocessing, augmentation, and inferencing.
  [rocAL](https://github.com/ROCm/rocAL){.reference .external}                           3.3.0                2.2.0                Accelerates the data pipeline by offloading intensive preprocessing and augmentation tasks. rocAL is part of MIVisionX.
  [RCCL](https://github.com/ROCm/rccl){.reference .external}                             2.26.6               2.22.3               Optimizes for multi-GPU communication for operations like AllReduce and Broadcast.
  [rocDecode](https://github.com/ROCm/rocDecode){.reference .external}                   1.0.0                0.10.0               Provides hardware-accelerated data decoding capabilities, particularly for image, video, and other dataset formats.
  [rocJPEG](https://github.com/ROCm/rocJPEG){.reference .external}                       1.1.0                0.8.0                Provides hardware-accelerated JPEG image decoding and encoding.
  [RPP](https://github.com/ROCm/RPP){.reference .external}                               2.0.0                1.9.10               Speeds up data augmentation, transformation, and other preprocessing steps.
  [rocThrust](https://github.com/ROCm/rocThrust){.reference .external}                   4.0.0                3.3.0                Provides a C++ template library for parallel algorithms like sorting, reduction, and scanning.
  [rocWMMA](https://github.com/ROCm/rocWMMA){.reference .external}                       2.0.0                1.7.0                Accelerates warp-level matrix-multiply and matrix-accumulate to speed up matrix multiplication (GEMM) and accumulation operations with mixed precision support.
:::
::::

::: {#supported-features-with-rocm-7-0-0 .section}
[]{#dgl-supported-features-latest}

## Supported features with ROCm 7.0.0[\#](#supported-features-with-rocm-7-0-0 "Link to this heading"){.headerlink}

Many functions and methods available upstream are also supported in DGL on ROCm. Instead of listing them all, support is grouped into the following categories to provide a general overview.

- DGL Base

- DGL Backend

- DGL Data

- DGL Dataloading

- DGL Graph

- DGL Function

- DGL Ops

- DGL Sampling

- DGL Transforms

- DGL Utils

- DGL Distributed

- DGL Geometry

- DGL Mpops

- DGL NN

- DGL Optim

- DGL Sparse

- GraphBolt
:::

::: {#unsupported-features-with-rocm-7-0-0 .section}
[]{#dgl-unsupported-features-latest}

## Unsupported features with ROCm 7.0.0[\#](#unsupported-features-with-rocm-7-0-0 "Link to this heading"){.headerlink}

- TF32 Support (only supported for PyTorch 2.7 and above)

- Kineto/ROCTracer integration
:::

::: {#unsupported-functions-with-rocm-7-0-0 .section}
[]{#dgl-unsupported-functions}

## Unsupported functions with ROCm 7.0.0[\#](#unsupported-functions-with-rocm-7-0-0 "Link to this heading"){.headerlink}

- [`bfs`{.docutils .literal .notranslate}]{.pre}

- [`format`{.docutils .literal .notranslate}]{.pre}

- [`multiprocess_sparse_adam_state_dict`{.docutils .literal .notranslate}]{.pre}

- [`half_spmm`{.docutils .literal .notranslate}]{.pre}

- [`segment_mm`{.docutils .literal .notranslate}]{.pre}

- [`gather_mm_idx_b`{.docutils .literal .notranslate}]{.pre}

- [`sample_labors_prob`{.docutils .literal .notranslate}]{.pre}

- [`sample_labors_noprob`{.docutils .literal .notranslate}]{.pre}

- [`sparse_admin`{.docutils .literal .notranslate}]{.pre}
:::

::: {#use-cases-and-recommendations .section}
[]{#dgl-recommendations}

## Use cases and recommendations[\#](#use-cases-and-recommendations "Link to this heading"){.headerlink}

DGL can be used for Graph Learning, and building popular graph models like GAT, GCN, and GraphSage. Using these models, a variety of use cases are supported:

- Recommender systems

- Network Optimization and Analysis

- 1D (Temporal) and 2D (Image) Classification

- Drug Discovery

For use cases and recommendations, refer to the [AMD ROCm blog](https://rocm.blogs.amd.com/){.reference .external}, where you can search for DGL examples and best practices to optimize your workloads on AMD GPUs.

- Although multiple use cases of DGL have been tested and verified, a few have been outlined in the [DGL in the Real World: Running GNNs on Real Use Cases](https://rocm.blogs.amd.com/artificial-intelligence/dgl_blog2/README.html){.reference .external} blog post, which walks through four real-world graph neural network (GNN) workloads implemented with the Deep Graph Library on ROCm. It covers tasks ranging from heterogeneous e-commerce graphs and multiplex networks (GATNE) to molecular graph regression (GNN-FiLM) and EEG-based neurological diagnosis (EEG-GCNN). For each use case, the authors detail: the dataset and task, how DGL is used, and their experience porting to ROCm. It is shown that DGL codebases often run without modification, with seamless integration of graph operations, message passing, sampling, and convolution.

- The [Graph Neural Networks (GNNs) at Scale: DGL with ROCm on AMD Hardware](https://rocm.blogs.amd.com/artificial-intelligence/why-graph-neural/README.html){.reference .external} blog post introduces the Deep Graph Library (DGL) and its enablement on the AMD ROCm platform, bringing high-performance graph neural network (GNN) training to AMD GPUs. DGL bridges the gap between dense tensor frameworks and the irregular nature of graph data through a graph-first, message-passing abstraction. Its design ensures scalability, flexibility, and interoperability across frameworks like PyTorch and TensorFlow. AMD's ROCm integration enables DGL to run efficiently on HIP-based GPUs, supported by prebuilt Docker containers and open-source repositories. This marks a major step in AMD's mission to advance open, scalable AI ecosystems beyond traditional architectures.

You can pre-process datasets and begin training on AMD GPUs through:

- Single-GPU training/inference

- Multi-GPU training
:::

::: {#previous-versions .section}
## Previous versions[\#](#previous-versions "Link to this heading"){.headerlink}

See [DGL version history](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/previous-versions/dgl-history.html "(in ROCm installation on Linux v7.2.2)"){.reference .external} to find documentation for previous releases of the [`ROCm/dgl`{.docutils .literal .notranslate}]{.pre} Docker image.
:::
::::::::::::::::::::::

::::: prev-next-area
[](jax-compatibility.html "previous page"){.left-prev}

::: prev-next-info
previous

JAX compatibility
:::

[](../../how-to/build-rocm.html "next page"){.right-next}

::: prev-next-info
next

Build ROCm from source
:::
:::::
:::::::::::::::::::::::::::::::::::::::

:::::: {.bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {.page-toc .tocsection .onthispage}
Contents
:::

- [Support overview](#support-overview){.reference .internal .nav-link}
- [Compatibility matrix](#compatibility-matrix){.reference .internal .nav-link}
- [Key ROCm libraries for DGL](#key-rocm-libraries-for-dgl){.reference .internal .nav-link}
- [Supported features with ROCm 7.0.0](#supported-features-with-rocm-7-0-0){.reference .internal .nav-link}
- [Unsupported features with ROCm 7.0.0](#unsupported-features-with-rocm-7-0-0){.reference .internal .nav-link}
- [Unsupported functions with ROCm 7.0.0](#unsupported-functions-with-rocm-7-0-0){.reference .internal .nav-link}
- [Use cases and recommendations](#use-cases-and-recommendations){.reference .internal .nav-link}
- [Previous versions](#previous-versions){.reference .internal .nav-link}
::::
:::::
::::::
::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::
