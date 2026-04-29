---
title: "What is ROCm?"
source_url: "https://rocm.docs.amd.com/en/latest/what-is-rocm.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-04-28
---

::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}

::: header-article-item
- [](index.html){.nav-link aria-label="Home"}
- 什么是 ROCm（ROCm（Radeon 开放计算平台））？

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons
[]{.fa-solid .fa-list}

# 什么是 ROCm（ROCm（Radeon 开放计算平台））?

## 目录

- [ROCm components](#rocm-components){.reference .internal .nav-link}
  - [Libraries](#libraries){.reference .internal .nav-link}
    - [Machine Learning & Computer Vision](#machine-learning-computer-vision){.reference .internal .nav-link}
    - [Communication](#communication){.reference .internal .nav-link}
    - [Math](#math){.reference .internal .nav-link}
    - [Primitives](#primitives){.reference .internal .nav-link}
  - [Tools](#tools){.reference .internal .nav-link}
    - [System Management](#system-management){.reference .internal .nav-link}
    - [Performance](#performance){.reference .internal .nav-link}
    - [Development](#development){.reference .internal .nav-link}
  - [Compilers](#compilers){.reference .internal .nav-link}
  - [Runtime API](#runtime-api){.reference .internal .nav-link}

# 什么是 ROCm（ROCm（Radeon 开放计算平台））?[\#](#what-is-rocm "Link to this heading"){.headerlink}

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-03-10

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 7 分钟阅读时间

适用于 Linux 和 Windows

ROCm（ROCm（Radeon 开放计算平台））是一个主要由开源软件组成的软件栈，为 AMD 图形处理器（GPU）的编程提供工具，覆盖从底层内核到高层终端用户应用程序。

[![AMD 的 ROCm（ROCm（Radeon 开放计算平台））软件栈和赋能技术。](_images/rocm-software-stack-7_2_1.png){.align-center style="width: 800px;"}](_images/rocm-software-stack-7_2_1.png){.reference .internal .image-reference}

具体来说，ROCm（ROCm（Radeon 开放计算平台））提供了用于[[HIP（HIP（异构接口可移植性））]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/HIP（HIP（异构接口可移植性））/en/latest/index.html "(in HIP（HIP（异构接口可移植性）） Documentation v7.2.53211)"){.reference .external}、OpenCL 和 OpenMP 的工具。这些包括编译器、高级函数库、调试器、分析器和运行时。

## ROCm components[\#](#rocm-components "Link to this heading"){.headerlink}

ROCm consists of the following components. For information on the license associated with each component, see [[ROCm licensing]{.doc}](about/license.html){.reference .internal}.

### 库[\#](#libraries "Link to this heading"){.headerlink}

#### 机器学习与计算机视觉[\#](#machine-learning-computer-vision "Link to this heading"){.headerlink}

::: pst-scrollable-table-container
  Component                                                                                                                                                                                   Description
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------
  [[Composable Kernel]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/composable_kernel/en/latest/index.html "(in Composable Kernel Documentation v1.2.0)"){.reference .external}   Provides a programming model for writing performance critical kernels for machine learning workloads across multiple architectures
  [[MIGraphX]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/AMDMIGraphX/en/latest/index.html "(in MIGraphX v2.15.0)"){.reference .external}                                        Graph inference engine that accelerates machine learning model inference
  [[MIOpen]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/MIOpen/en/latest/index.html "(in MIOpen Documentation v3.5.1)"){.reference .external}                                    An open source deep-learning library
  [[MIVisionX]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/MIVisionX/en/latest/index.html "(in MIVisionX Documentation v3.5.0)"){.reference .external}                           Set of comprehensive computer vision and machine learning libraries, utilities, and applications
  [[ROCm Performance Primitives (RPP)]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rpp/en/latest/index.html "(in RPP documentation v2.2.1)"){.reference .external}               Comprehensive high-performance computer vision library for AMD processors with HIP/OpenCL/CPU back-ends
  [[rocAL]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocAL/en/latest/index.html "(in rocAL Documentation v2.5.0)"){.reference .external}                                       An augmentation library designed to decode and process images and videos
  [[rocDecode]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocDecode/en/latest/index.html "(in rocDecode documentation v1.7.0)"){.reference .external}                           High-performance SDK for access to video decoding features on AMD GPUs
  [[rocJPEG]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocJPEG/en/latest/index.html "(in rocJPEG Documentation v1.4.0)"){.reference .external}                                 Library for decoding JPG images on AMD GPUs
  [[rocPyDecode]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocPyDecode/en/latest/index.html "(in rocPyDecode v0.8.0)"){.reference .external}                                   Provides access to rocDecode APIs in both Python and C/C++ languages

注意

[rocCV](https://rocm.docs.amd.com/projects/rocCV/en/latest/index.html){.reference .external} 是一个高效的 GPU 加速库，用于图像预处理和后处理。rocCV 处于早期访问状态，不建议将其用于生产工作负载。

#### 通信[\#](#communication "Link to this heading"){.headerlink}

::: pst-scrollable-table-container
  Component                                                                                                                                             Description
  ----------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------
  [[RCCL（RCCL（ROCm 集合通信库））]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rccl/en/latest/index.html "(in RCCL（RCCL（ROCm 集合通信库）） Documentation v2.27.7)"){.reference .external}   独立的库，提供多GPU和多节点集合通信原语
  [[rocSHMEM]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocSHMEM/en/latest/index.html "(in rocSHMEM v3.2.0)"){.reference .external}      一个内核内网络库，通过类似OpenSHMEM的接口提供以GPU为中心的网络通信

#### 数学[\#](#math "Link to this heading"){.headerlink}

::: pst-scrollable-table-container
  Component                                                                                                                                                                 Description
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [half](https://github.com/ROCm/half/){.reference .external}                                                                                                               C++ header-only library that provides an IEEE 754 conformant, 16-bit half-precision floating-point type, along with corresponding arithmetic operators, type conversions, and common mathematical functions
  [[hipBLAS]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/hipBLAS/en/latest/index.html "(in hipBLAS Documentation v3.2.0)"){.reference .external}               BLAS-marshaling library that supports [[rocBLAS]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/index.html "(in rocBLAS Documentation v5.2.0)"){.reference .external} and cuBLAS backends
  [[hipBLASLt]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/hipBLASLt/en/latest/index.html "(in hipBLASLt Documentation v1.2.2)"){.reference .external}         Provides general matrix-matrix operations with a flexible API and extends functionalities beyond traditional BLAS library
  [[hipFFT]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/hipFFT/en/latest/index.html "(in hipFFT Documentation v1.0.22)"){.reference .external}                 Fast Fourier transforms (FFT)-marshalling library that supports rocFFT or cuFFT backends
  [[hipfort]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/hipfort/en/latest/index.html "(in hipfort Documentation v0.7.1)"){.reference .external}               Fortran interface library for accessing GPU Kernels
  [[hipRAND]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/hipRAND/en/latest/index.html "(in hipRAND Documentation v3.1.0)"){.reference .external}               Ports CUDA applications that use the cuRAND library into the HIP layer
  [[hipSOLVER]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/index.html "(in hipSOLVER Documentation v3.2.0)"){.reference .external}         An LAPACK-marshalling library that supports [[rocSOLVER]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocSOLVER/en/latest/index.html "(in rocSOLVER Documentation v3.32.0)"){.reference .external} and cuSOLVER backends
  [[hipSPARSE]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/hipSPARSE/en/latest/index.html "(in hipSPARSE Documentation v4.2.0)"){.reference .external}         SPARSE-marshalling library that supports [[rocSPARSE]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocSPARSE/en/latest/index.html "(in rocSPARSE Documentation v4.2.0)"){.reference .external} and cuSPARSE backends
  [[hipSPARSELt]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/hipSPARSELt/en/latest/index.html "(in hipSPARSELt Documentation v0.2.6)"){.reference .external}   SPARSE-marshalling library with multiple supported backends
  [[rocALUTION]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocALUTION/en/latest/index.html "(in rocALUTION Documentation v4.1.0)"){.reference .external}      Sparse linear algebra library for exploring fine-grained parallelism on ROCm runtime and toolchains
  [[rocBLAS]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/index.html "(in rocBLAS Documentation v5.2.0)"){.reference .external}               BLAS implementation (in the HIP programming language) on the ROCm runtime and toolchains
  [[rocFFT]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocFFT/en/latest/index.html "(in rocFFT Documentation v1.0.36)"){.reference .external}                 Software library for computing fast Fourier transforms (FFTs) written in HIP
  [[rocRAND]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocRAND/en/latest/index.html "(in rocRAND Documentation v4.2.0)"){.reference .external}               Provides functions that generate pseudorandom and quasirandom numbers
  [[rocSOLVER]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocSOLVER/en/latest/index.html "(in rocSOLVER Documentation v3.32.0)"){.reference .external}        An implementation of LAPACK routines on ROCm software, implemented in the HIP programming language and optimized for AMD's latest discrete GPUs
  [[rocSPARSE]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocSPARSE/en/latest/index.html "(in rocSPARSE Documentation v4.2.0)"){.reference .external}         Exposes a common interface that provides BLAS for sparse computation implemented on ROCm runtime and toolchains (in the HIP programming language)
  [[rocWMMA]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocWMMA/en/latest/index.html "(in rocWMMA Documentation v2.2.0)"){.reference .external}               C++ library for accelerating mixed-precision matrix multiply-accumulate (MMA) operations
  [[Tensile]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/Tensile/en/latest/src/index.html "(in Tensile Documentation v4.45.0)"){.reference .external}          Creates benchmark-driven backend libraries for GEMMs, GEMM-like problems, and general N-dimensional tensor contractions

#### 原语[\#](#primitives "Link to this heading"){.headerlink}

::: pst-scrollable-table-container
  Component                                                                                                                                                           Description
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [[hipCUB]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/hipCUB/en/latest/index.html "(in hipCUB Documentation v4.2.0)"){.reference .external}            Thin header-only wrapper library on top of [[rocPRIM]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocPRIM/en/latest/index.html "(in rocPRIM Documentation v4.2.0)"){.reference .external} or CUB that allows project porting using the CUB library to the HIP layer
  [[hipTensor]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/hipTensor/en/latest/index.html "(in hipTensor Documentation v2.2.0)"){.reference .external}   AMD's C++ library for accelerating tensor primitives based on the composable kernel library
  [[rocPRIM]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocPRIM/en/latest/index.html "(in rocPRIM Documentation v4.2.0)"){.reference .external}         Header-only library for HIP parallel primitives
  [[rocThrust]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocThrust/en/latest/index.html "(in rocThrust Documentation v4.2.0)"){.reference .external}   Parallel algorithm library

### 工具[\#](#tools "Link to this heading"){.headerlink}

#### 系统管理[\#](#system-management "Link to this heading"){.headerlink}

::: pst-scrollable-table-container
  Component                                                                                                                                                                           Description
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------
  [[AMD SMI]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/amdsmi/en/latest/index.html "(in AMD SMI v26.2.2)"){.reference .external}                                       System management interface to control AMD GPU settings, monitor performance, and retrieve device and process information
  [[ROCm Data Center Tool]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rdc/en/latest/index.html "(in ROCm Data Center tool)"){.reference .external}                      Simplifies administration and addresses key infrastructure challenges in AMD GPUs in cluster and data-center environments
  [[rocminfo]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocminfo/en/latest/index.html "(in rocminfo v1.0.0)"){.reference .external}                                    Reports system information
  [[ROCm SMI]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocm_smi_lib/en/latest/index.html "(in ROCm SMI LIB Documentation v7.8.0)"){.reference .external}              C library for Linux that provides a user space interface for applications to monitor and control GPU applications
  [[ROCm Validation Suite]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/ROCmValidationSuite/en/latest/index.html "(in RVS Documentation v1.3.0)"){.reference .external}   Detects and troubleshoots common problems affecting AMD GPUs running in a high-performance computing environment

#### 性能[\#](#performance "Link to this heading"){.headerlink}

::: pst-scrollable-table-container
  Component                                                                                                                                                                               Description
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------
  [[ROCm Bandwidth Test]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocm_bandwidth_test/en/latest/index.html "(in rocm_bandwidth_test)"){.reference .external}              Captures the performance characteristics of buffer copying and kernel read/write operations
  [[ROCm Compute Profiler]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocprofiler-compute/en/latest/index.html "(in ROCm Compute Profiler v3.4.0)"){.reference .external}   Kernel-level profiling for machine learning and high performance computing (HPC) workloads
  [[ROCm Systems Profiler]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocprofiler-systems/en/latest/index.html "(in rocprofiler-systems v1.3.0)"){.reference .external}     Comprehensive profiling and tracing of applications running on the CPU or the CPU and GPU
  [[ROCProfiler]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocprofiler/en/latest/index.html "(in rocprofiler Documentation v2.0.0)"){.reference .external}                 Profiling tool for HIP applications
  [[ROCprofiler-SDK]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/index.html "(in Rocprofiler SDK v1.1.0)"){.reference .external}                   Toolkit for developing analysis tools for profiling and tracing GPU compute applications. This toolkit is in beta and subject to change
  [[ROCTracer]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/roctracer/en/latest/index.html "(in ROCTracer Documentation v4.1.0)"){.reference .external}                       Intercepts runtime API calls and traces asynchronous activity

注意

[ROCprof Compute Viewer](https://rocm.docs.amd.com/projects/rocprof-compute-viewer/en/amd-mainline/){.reference .external} 是一款用于可视化和分析 GPU 线程跟踪数据的工具，这些数据通过 [[rocprofv3]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/index.html "(in Rocprofiler SDK v1.1.0)"){.reference .external} 收集。请注意，[ROCprof Compute Viewer](https://rocm.docs.amd.com/projects/rocprof-compute-viewer/en/amd-mainline/){.reference .external} 目前处于早期访问状态，不建议在生产环境中运行工作负载。

#### 开发[\#](#development "Link to this heading"){.headerlink}

::: pst-scrollable-table-container
  Component                                                                                                                                                                      Description
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------
  [[HIPIFY]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/HIPIFY/en/latest/index.html "(in HIPIFY Documentation)"){.reference .external}                              Translates CUDA source code into portable HIP C++
  [[ROCm CMake]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/ROCmCMakeBuildTools/en/latest/index.html "(in ROCm CMake Build Tools v0.14.0)"){.reference .external}   Collection of CMake modules for common build and development tasks
  [[ROCdbgapi]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/ROCdbgapi/en/latest/index.html "(in ROCdbgapi Documentation v0.77.4)"){.reference .external}             ROCm debugger API library
  [[ROCm Debugger (ROCgdb)]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/ROCgdb/en/latest/index.html "(in ROCgdb Documentation v16.3)"){.reference .external}        Source-level debugger for Linux, based on the GNU Debugger (GDB)
  [[ROCr Debug Agent]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocr_debug_agent/en/latest/index.html "(in rocr_debug_agent v2.1.0)"){.reference .external}       Prints the state of all AMD GPU wavefronts that caused a queue error by sending a SIGQUIT signal to the process while the program is running

### 编译器[\#](#compilers "Link to this heading"){.headerlink}

::: pst-scrollable-table-container
  Component                                                                                                                                                                       Description
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------
  [[HIPCC]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/HIPCC/en/latest/index.html "(in HIPCC Documentation v1.1.1)"){.reference .external}                           Compiler driver utility that calls Clang and passes the appropriate include and library options for the target compiler and HIP infrastructure
  [[ROCm compilers]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/llvm-project/en/latest/index.html "(in llvm-project Documentation v22.0.0)"){.reference .external}   ROCm LLVM compiler infrastructure
  [FLANG](https://github.com/ROCm/flang/){.reference .external}                                                                                                                   An out-of-tree Fortran compiler targeting LLVM

### 运行时 API[\#](#runtime-api "Link to this heading"){.headerlink}

::: pst-scrollable-table-container
  Component                                                                                                                                             Description
  ----------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------
  [[HIP]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/HIP/en/latest/index.html "(in HIP Documentation v7.2.53211)"){.reference .external}   HIP is a C++ runtime API and kernel language for AMD GPUs

::::: prev-next-area
[](index.html "上一页"){.left-prev}

::: prev-next-info
上一页

AMD ROCm（Radeon 开放计算平台）文档

[](about/release-notes.html "下一页"){.right-next}

::: prev-next-info
下一个

ROCm（Radeon 开放计算平台）7.2.2 发行说明

:::: sidebar-secondary-item
目录

- [ROCm components](#rocm-components){.reference .internal .nav-link}
  - [Libraries](#libraries){.reference .internal .nav-link}
    - [Machine Learning & Computer Vision](#machine-learning-computer-vision){.reference .internal .nav-link}
    - [Communication](#communication){.reference .internal .nav-link}
    - [Math](#math){.reference .internal .nav-link}
    - [Primitives](#primitives){.reference .internal .nav-link}
  - [Tools](#tools){.reference .internal .nav-link}
    - [System Management](#system-management){.reference .internal .nav-link}
    - [Performance](#performance){.reference .internal .nav-link}
    - [Development](#development){.reference .internal .nav-link}
  - [Compilers](#compilers){.reference .internal .nav-link}
  - [Runtime API](#runtime-api){.reference .internal .nav-link}