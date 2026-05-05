---
title: "What is rocBLAS? &#8212; rocBLAS 5.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocBLAS/en/latest/what-is-rocblas.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:04:58.846996+00:00
content_hash: "9767be926c06c568"
---

# What is rocBLAS?[#](#what-is-rocblas)

rocBLAS is the AMD library for Basic Linear Algebra Subprograms (BLAS) on the [ROCm platform](https://rocm.docs.amd.com/en/latest/index.html).
It is implemented in the [HIP C++](https://rocm.docs.amd.com/projects/HIP/en/latest/index.html) and optimized for AMD GPUs.
For more detailed component information, see [rocBLAS design notes](conceptual/rocblas-design-notes.html).

rocBLAS aims to provide the following:

Functionality similar to legacy BLAS, adapted to run on AMD GPUs

A high-performance, robust implementation


rocBLAS is written in HIP C++ (using C++17 features) and it uses the HIP runtime.

The rocBLAS API is a thin C99 API that uses the hourglass pattern. It contains:

[rocBLAS Level-1 functions](reference/level-1.html#level-1),[rocBLAS Level-2 functions](reference/level-2.html#level-2), and[rocBLAS Level-3 functions](reference/level-3.html#level-3)with batched and strided_batched versionsExtensions to legacy BLAS, including functions for mixed precision

Auxiliary functions

Device memory functions


Note

The official rocBLAS API is the C99 API defined in

`rocblas.h`

. Therefore, the use of any other public symbols is discouraged. Other C/C++ interfaces might not follow a deprecation model and could change without warning from one release to the next.The rocBLAS array storage format is column major and one-based. This is to maintain compatibility with the legacy BLAS Fortran code.

rocBLAS calls the AMD

[Tensile](https://rocm.docs.amd.com/projects/Tensile/en/latest/src/index.html)and[hipBLASLt](https://rocm.docs.amd.com/projects/hipBLASLt/en/latest/index.html)libraries for Level-3 GEMMs (matrix matrix multiplication).
