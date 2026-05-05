---
title: "rocSPARSE 4.2.0 for ROCm 7.2.0"
source_url: https://github.com/ROCm/rocSPARSE/releases/tag/rocm-7.2.0
source_type: github-release
source_org: ROCm
published_date: 2026-01-21
credibility: 4
lifecycle: latest
tags: [github-release, rocm-7.2.0]
---

# rocSPARSE 4.2.0 for ROCm 7.2.0

> 📦 **Release:** [rocm-7.2.0](https://github.com/ROCm/rocSPARSE/releases/tag/rocm-7.2.0)
> **发布:** 2026-01-21


### Added

* Added sliced ELL format support to the `rocsparse_spmv` routine.
* Added the `rocsparse_sptrsv` and `rocsparse_sptrsm` routines for triangular solve.
* Added the `--clients-only` option to the `install.sh` and `rmake.py` scripts to only build the clients for a version of rocSPARSE that is already installed.
* Added nnz split algorithm `rocsparse_spmv_alg_csr_nnzsplit` to `rocsparse_spmv`. This algorithm might be superior to the existing adaptive algorithm `rocsparse_spmv_alg_csr_adaptive` when running the computation a small number of times because it avoids paying the analysis cost of the adaptive algorithm.

### Changed
* Make rocBLAS a requirement when it's requested when building from source. Previously, rocBLAS was not used if it could not be found. To opt out of using rocblas when building from source, use the `--no-rocblas` option with the `install.sh` or `rmake.py` build scripts.

### Optimized
* Significantly improved the `rocsparse_sddmm` routine when using CSR format, especially as the number of columns in the dense `A` matrix (or rows in the dense `B` matrix) increase.
* Improved the user documentation.

### Resolved issues
* Fix the `rmake.py` build script to properly handle `auto` and all options when selecting offload targets.
* Fix building rocSPARSE with the install script on centOS 9.
* Fix `std::fma` casting in host routines to properly deduce types. This could have previously caused compilation failures when building from source.

