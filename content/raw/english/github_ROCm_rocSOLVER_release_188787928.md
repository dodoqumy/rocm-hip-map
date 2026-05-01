---
title: "rocSOLVER 3.27.0 for ROCm 6.3.0"
source_url: https://github.com/ROCm/rocSOLVER/releases/tag/rocm-6.3.0
source_type: github-release
source_org: ROCm
published_date: 2024-12-03
credibility: 4
lifecycle: latest
tags: [github-release, rocm-6.3.0]
---

# rocSOLVER 3.27.0 for ROCm 6.3.0

> 📦 **Release:** [rocm-6.3.0](https://github.com/ROCm/rocSOLVER/releases/tag/rocm-6.3.0)
> **发布:** 2024-12-03


### Added

* 64-bit APIs for existing functions:
    - LACGV_64
    - LARF_64
    - LARFG_64
    - GEQR2_64 (with batched and strided\_batched versions)
    - GEQRF_64 (with batched and strided\_batched versions)
    - POTF2_64 (with batched and strided\_batched versions)
    - POTRF_64 (with batched and strided\_batched versions)
    - POTRS_64 (with batched and strided\_batched versions)
* Support added for the gfx1151, gfx1200, and gfx1201 architectures

### Changed

* The rocSPARSE library is now an optional dependency at runtime. If rocSPARSE
  is not available, rocSOLVER's sparse refactorization and solvers functions
  will return `rocblas_status_not_implemented`.

### Optimized

* Improved the performance of LARFG, LARF, and downstream functions such as GEQR2 and GEQRF on wave64 architectures
* Improved the performance of BDSQR and GESVD
* Improved the performance of STEDC and divide and conquer Eigensolvers

### Resolved issues

* Fixed a memory allocation issue in SYEVJ that could cause failures on clients that manage their own memory.
* Fixed a synchronizarion issue with SYEVJ that could led to a convergence failure for large matrices.
* Fixed a convergence issue in STEIN stemming from numerical orthogonality of the initial choice of eigenvectors.
* Fixed a synchronization issue in STEIN.

### Known issues

* A known issue in STEBZ can lead to errors in routines based on bisection to compute eigenvalues for symmetric/hermitian matrices (for example, SYEVX/HEEVX and SYGVX/HEGVX), as well as singular values (for example, BDSVDX and GESVDX).


