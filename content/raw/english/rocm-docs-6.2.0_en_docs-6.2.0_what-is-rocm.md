---
title: "What is ROCm?"
source_url: "https://rocm.docs.amd.com/en/docs-6.2.0/what-is-rocm.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T16:23:19.388658+00:00
content_hash: "8d979390be1b20b9"
---

# What is ROCm?[#](#what-is-rocm)



ROCm is an open-source stack, composed primarily of open-source software, designed for graphics processing unit (GPU) computation. ROCm consists of a collection of drivers, development tools, and APIs that enable GPU programming from low-level kernel to end-user applications.


ROCm is powered by
[Heterogeneous-computing Interface for Portability (HIP)](https://rocm.docs.amd.com/projects/HIP/en/docs-6.2.0/index.html);
it supports programming models, such as OpenMP and OpenCL, and includes all necessary open
source software compilers, debuggers, and libraries. It’s fully integrated into machine learning (ML)
frameworks, such as PyTorch and TensorFlow.

Tip

If you’re using Radeon GPUs, refer to the Radeon-specific ROCm documentation.

## ROCm components[#](#rocm-components)

ROCm consists of the following components. For information on the license associated with each component,
see [ROCm licensing](about/license.html).

### Libraries[#](#libraries)

#### Machine Learning & Computer Vision[#](#machine-learning-computer-vision)

Component |
Description |
|---|---|
Provides a programming model for writing performance critical kernels for machine learning workloads across multiple architectures |
|
Graph inference engine that accelerates machine learning model inference |
|
An open source deep-learning library |
|
Set of comprehensive computer vision and machine learning libraries, utilities, and applications |
|
Comprehensive high-performance computer vision library for AMD processors with HIP/OpenCL/CPU back-ends |
|
An augmentation library designed to decode and process images and videos |
|
High-performance SDK for access to video decoding features on AMD GPUs |
|
Provides access to rocDecode APIs in both Python and C/C++ languages |

#### Communication[#](#communication)

#### Math[#](#math)

Component |
Description |
|---|---|
C++ header-only library that provides an IEEE 754 conformant, 16-bit half-precision floating-point type, along with corresponding arithmetic operators, type conversions, and common mathematical functions |
|
BLAS-marshaling library that supports |
|
Provides general matrix-matrix operations with a flexible API and extends functionalities beyond traditional BLAS library |
|
Fast Fourier transforms (FFT)-marshalling library that supports rocFFT or cuFFT backends |
|
Fortran interface library for accessing GPU Kernels |
|
Ports CUDA applications that use the cuRAND library into the HIP layer |
|
An LAPACK-marshalling library that supports |
|
SPARSE-marshalling library that supports |
|
SPARSE-marshalling library with multiple supported backends |
|
Sparse linear algebra library for exploring fine-grained parallelism on ROCm runtime and toolchains |
|
BLAS implementation (in the HIP programming language) on the ROCm runtime and toolchains |
|
Software library for computing fast Fourier transforms (FFTs) written in HIP |
|
Provides functions that generate pseudorandom and quasirandom numbers |
|
An implementation of LAPACK routines on ROCm software, implemented in the HIP programming language and optimized for AMD’s latest discrete GPUs |
|
Exposes a common interface that provides BLAS for sparse computation implemented on ROCm runtime and toolchains (in the HIP programming language) |
|
C++ library for accelerating mixed-precision matrix multiply-accumulate (MMA) operations |
|
Creates benchmark-driven backend libraries for GEMMs, GEMM-like problems, and general N-dimensional tensor contractions |

#### Primitives[#](#primitives)

Component |
Description |
|---|---|
Thin header-only wrapper library on top of |
|
AMD’s C++ library for accelerating tensor primitives based on the composable kernel library |
|
Header-only library for HIP parallel primitives |
|
Parallel algorithm library |

### Tools[#](#tools)

#### System Management[#](#system-management)

Component |
Description |
|---|---|
C library for Linux that provides a user space interface for applications to monitor and control AMD devices |
|
Simplifies administration and addresses key infrastructure challenges in AMD GPUs in cluster and data-center environments |
|
Reports system information |
|
C library for Linux that provides a user space interface for applications to monitor and control GPU applications |
|
Detects and troubleshoots common problems affecting AMD GPUs running in a high-performance computing environment |

#### Performance[#](#performance)

Component |
Description |
|---|---|
System performance profiling tool for machine learning and HPC workloads |
|
Comprehensive profiling and tracing tool for HIP applications |
|
Captures the performance characteristics of buffer copying and kernel read/write operations |
|
Profiling tool for HIP applications |
|
Toolkit for developing analysis tools for profiling and tracing GPU compute applications. This toolkit is in beta and subject to change |
|
Intercepts runtime API calls and traces asynchronous activity |

#### Development[#](#development)

Component |
Description |
|---|---|
Translates CUDA source code into portable HIP C++ |
|
Collection of CMake modules for common build and development tasks |
|
ROCm debugger API library |
|
Source-level debugger for Linux, based on the GNU Debugger (GDB) |
|
Prints the state of all AMD GPU wavefronts that caused a queue error by sending a SIGQUIT signal to the process while the program is running |

### Compilers[#](#compilers)

Component |
Description |
|---|---|
Compiler driver utility that calls Clang or NVCC and passes the appropriate include and library options for the target compiler and HIP infrastructure |
|
ROCm LLVM compiler infrastructure |
|
An out-of-tree Fortran compiler targeting LLVM |

### Runtimes[#](#runtimes)

Component |
Description |
|---|---|
Contains source code for AMD’s common language runtimes: HIP and OpenCL |
|
AMD’s GPU programming language extension and the GPU runtime |
|
User-mode API interfaces and libraries necessary for host applications to launch compute kernels on available HSA ROCm kernel agents |
