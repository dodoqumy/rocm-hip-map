---
title: "rocBLAS 4.3.0 for ROCm 6.3.0"
source_url: https://github.com/ROCm/rocBLAS/releases/tag/rocm-6.3.0
source_type: github-release
source_org: ROCm
published_date: 2024-12-03
credibility: 4
lifecycle: latest
tags: [github-release, rocm-6.3.0]
---

# rocBLAS 4.3.0 for ROCm 6.3.0

> 📦 **Release:** [rocm-6.3.0](https://github.com/ROCm/rocBLAS/releases/tag/rocm-6.3.0)
> **发布:** 2024-12-03


### Added

* Level 3 and EX functions have an additional ILP64 API for both C and FORTRAN (_64 name suffix) with int64_t function arguments

### Changed

* amdclang is used as the default compiler instead of hipcc
* Internal performance scripts use amd-smi instead of the deprecated rocm-smi

### Optimized

* Improved performance of Level 2 gbmv
* Improved performance of Level 2 gemv for float and double precisions for problem sizes (TransA == N && m==n && m % 128 == 0) measured on a gfx942 GPU

### Resolved issues

* Fixed stbsv_strided_batched_64 Fortran binding

### Upcoming changes

* rocblas_Xgemm_kernel_name APIs are deprecated

