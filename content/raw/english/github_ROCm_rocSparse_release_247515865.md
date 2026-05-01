---
title: "rocSPARSE 4.0.2 for ROCm 7.0.0"
source_url: https://github.com/ROCm/rocSPARSE/releases/tag/rocm-7.0.0
source_type: github-release
source_org: ROCm
published_date: 2025-09-16
credibility: 4
lifecycle: latest
tags: [github-release, rocm-7.0.0]
---

# rocSPARSE 4.0.2 for ROCm 7.0.0

> 📦 **Release:** [rocm-7.0.0](https://github.com/ROCm/rocSPARSE/releases/tag/rocm-7.0.0)
> **发布:** 2025-09-16


### Added

* Adds `SpGEAM` generic routine for computing sparse matrix addition in CSR format
* Adds `v2_SpMV` generic routine for computing sparse matrix vector multiplication. As opposed to the deprecated `rocsparse_spmv` routine, this routine does not use a fallback algorithm if a non-implemented configuration is encountered and will return an error in such a case. For the deprecated routine `rocsparse_spmv`, the user can enable warning messages in situations where a fallback algorithm is used by either calling upfront the routine `rocsparse_enable_debug` or exporting the variable `ROCSPARSE_DEBUG` (with the shell command `export ROCSPARSE_DEBUG=1`).
* Adds half float mixed precision to `rocsparse_axpby` where X and Y use float16 and result and the compute type use float
* Adds half float mixed precision to `rocsparse_spvv` where X and Y use float16 and result and the compute type use float
* Adds half float mixed precision to `rocsparse_spmv` where A and X use float16 and Y and the compute type use float
* Adds half float mixed precision to `rocsparse_spmm` where A and B use float16 and C and the compute type use float
* Adds half float mixed precision to `rocsparse_sddmm` where A and B use float16 and C and the compute type use float
* Adds half float uniform precision to `rocsparse_scatter` and `rocsparse_gather` routines
* Adds half float uniform precision to `rocsparse_sddmm` routine
* Added `rocsparse_spmv_alg_csr_rowsplit` algorithm.
* Added support for gfx950
* Add ROC-TX instrumentation support in rocSPARSE (not available on Windows or in the static library version on Linux).
* Added the `almalinux` OS name to correct the gfortran dependency

### Changed

* Switch to defaulting to C++17 when building rocSPARSE from source. Previously rocSPARSE was using C++14 by default.

### Optimized

* Reduced the number of template instantiations in the library to further reduce the shared library binary size and improve compile times
* Allow SpGEMM routines to use more shared memory when available. This can speed up performance for matrices with a large number of intermediate products.
* Use of the `rocsparse_spmv_alg_csr_adaptive` or `rocsparse_spmv_alg_csr_default` algorithms in `rocsparse_spmv` to perform transposed sparse matrix multiplication (`C=alpha*A^T*x+beta*y`) resulted in unnecessary analysis on A and needless slowdown during the analysis phase. This has been fixed by skipping the analysis when performing the transposed sparse matrix multiplication.
* Improved the user documentation

### Resolved issues

* Fixed an issue in the public headers where `extern "C"` was not wrapped by `#ifdef __cplusplus`, which caused failures when building C programs with rocSPARSE.
* Fixed a memory access fault in the `rocsparse_Xbsrilu0` routines.
* Fixed failures that could occur in `rocsparse_Xbsrsm_solve` or `rocsparse_spsm` with BSR format when using host pointer mode.
* Fixed ASAN compilation failures
* Fixed failure that occurred when using const descriptor `rocsparse_create_const_csr_descr` with the generic routine `rocsparse_sparse_to_sparse`. Issue was not observed when using non-const descriptor `rocsparse_create_csr_descr` with `rocsparse_sparse_to_sparse`.
* Fixed a memory leak in the rocsparse handle

### Removed

* The deprecated `rocsparse_spmv_ex` routine
* The deprecated `rocsparse_sbsrmv_ex`, `rocsparse_dbsrmv_ex`, `rocsparse_cbsrmv_ex`, and `rocsparse_zbsrmv_ex`  routines
* The deprecated `rocsparse_sbsrmv_ex_analysis`, `rocsparse_dbsrmv_ex_analysis`, `rocsparse_cbsrmv_ex_analysis`, and `rocsparse_zbsrmv_ex_analysis`  routines

### Upcoming changes

* Deprecated the `rocsparse_spmv` routine. Users should use the `rocsparse_v2_spmv` routine going forward.
* Deprecated `rocsparse_spmv_alg_csr_stream` algorithm. Users should use the `rocsparse_spmv_alg_csr_rowsplit` algorithm going forward.
* Deprecated the `rocsparse_itilu0_alg_sync_split_fusion` algorithm. Users should use one of `rocsparse_itilu0_alg_async_inplace`, `rocsparse_itilu0_alg_async_split`, or `rocsparse_itilu0_alg_sync_split` going forward.

