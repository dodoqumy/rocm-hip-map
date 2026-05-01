---
title: "rocBLAS 5.0.0 for ROCm 7.0.0"
source_url: https://github.com/ROCm/rocBLAS/releases/tag/rocm-7.0.0
source_type: github-release
source_org: ROCm
published_date: 2025-09-16
credibility: 4
lifecycle: latest
tags: [github-release, rocm-7.0.0]
---

# rocBLAS 5.0.0 for ROCm 7.0.0

> 📦 **Release:** [rocm-7.0.0](https://github.com/ROCm/rocBLAS/releases/tag/rocm-7.0.0)
> **发布:** 2025-09-16


### Added

* gfx950 support
* `ROCBLAS_LAYER = 8` internal API logging for `gemm` debugging
* Support for AOCL 5.0 gcc build as a client reference library
* Allow `PkgConfig` for client reference library fallback detection

### Changed

* `CMAKE_CXX_COMPILER` is now passed on during compilation for a Tensile build
* Change default atomics mode from `allowed` to `not allowed`

### Removed

* Support code for non-production gfx targets
* `rocblas_hgemm_kernel_name`, `rocblas_sgemm_kernel_name`, and `rocblas_dgemm_kernel_name` API functions
* Use of `warpSize` as a constexpr
* Use of deprecated behavior of `hipPeekLastError`
* `rocblas_float8.h` and `rocblas_hip_f8_impl.h` files
* `rocblas_gemm_ex3`, `rocblas_gemm_batched_ex3`, `rocblas_gemm_strided_batched_ex3` API functions

### Optimized

* Optimized `gemm` by using `gemv` kernels when applicable
* Optimized `gemv` for small `m` and `n` with a large batch count on gfx942
* Improved the performance of Level 1 `dot` for all precisions and variants when `N > 100000000` on gfx942
* Improved the performance of Level 1 `asum` and `nrm2` for all precisions and variants on gfx942
* Improved the performance of Level 2 `sger` (single precision) on gfx942
* Improved the performance of Level 3 `dgmm` for all precisions and variants on gfx942

### Resolved issues

* Fixed environment variable path-based logging to append multiple handle output to the same file
* Support numerics when `trsm` is running with `rocblas_status_perf_degraded`
* Fixed the build dependency installation of `joblib` on some operating systems
* Return `rocblas_status_internal_error` when `rocblas_[set,get]_ [matrix,vector]` is called with a host pointer in place of a device pointer
* Reduced the default verbosity level for internal GEMM backend information
* Updated from the deprecated rocm-cmake to ROCmCMakeBuildTools
* Corrected AlmaLinux gfortran package dependencies

### Upcoming changes

* Deprecated the use of negative indices to indicate the default solution is being used for `gemm_ex` with `rocblas_gemm_algo_solution_index`

