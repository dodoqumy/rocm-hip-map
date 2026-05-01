---
title: "rocSPARSE 3.4.0 for ROCm 6.4.0"
source_url: https://github.com/ROCm/rocSPARSE/releases/tag/rocm-6.4.0
source_type: github-release
source_org: ROCm
published_date: 2025-04-11
credibility: 4
lifecycle: latest
tags: [github-release, rocm-6.4.0]
---

# rocSPARSE 3.4.0 for ROCm 6.4.0

> 📦 **Release:** [rocm-6.4.0](https://github.com/ROCm/rocSPARSE/releases/tag/rocm-6.4.0)
> **发布:** 2025-04-11


### Added

* Added support for `rocsparse_matrix_type_triangular` in `rocsparse_spsv`
* Added test filters `smoke`, `regression`, and `extended` for emulation tests.
* Added `rocsparse_[s|d|c|z]csritilu0_compute_ex` routines for iterative ILU
* Added `rocsparse_[s|d|c|z]csritsv_solve_ex` routines for iterative triangular solve
* Added `GPU_TARGETS` to replace the now deprecated `AMDGPU_TARGETS` in cmake files
* Added BSR format to the SpMM generic routine `rocsparse_spmm`

### Changed

* By default, build rocsparse shared library using `--offload-compress` compiler option which compresses the fat binary. This significantly reduces the shared library binary size.

### Optimized

* Improved the performance of `rocsparse_spmm` when used with row order for `B` and `C` dense matrices and the row split algorithm, `rocsparse_spmm_alg_csr_row_split`.
* Improved the adaptive CSR sparse matrix-vector multiplication algorithm when the sparse matrix has many empty rows at the beginning or at the end of the matrix. This improves the routines `rocsparse_spmv` and `rocsparse_spmv_ex` when the adaptive algorithm `rocsparse_spmv_alg_csr_adaptive` is used.
* Improved stream CSR sparse matrix-vector multiplication algorithm when the sparse matrix size (number of rows) decreases. This improves the routines `rocsparse_spmv` and `rocsparse_spmv_ex` when the stream algorithm `rocsparse_spmv_alg_csr_stream` is used.
* Compared to `rocsparse_[s|d|c|z]csritilu0_compute`, the routines `rocsparse_[s|d|c|z]csritilu0_compute_ex` introduce a number of free iterations. A free iteration is an iteration that does not compute the evaluation of the stopping criteria, if enabled. This allows the user to tune the algorithm for performance improvements.
* Compared to `rocsparse_[s|d|c|z]csritsv_solve`, the routines `rocsparse_[s|d|c|z]csritsv_solve_ex` introduce a number of free iterations. A free iteration is an iteration that does not compute the evaluation of the stopping criteria. This allows the user to tune the algorithm for performance improvements.
* Improved user documentation

### Resolved issues
* Fixed an issue in `rocsparse_spgemm`, `rocsparse_[s|d|c|z]csrgemm`, and `rocsparse_[s|d|c|z]bsrgemm` where incorrect results could be produced when rocSPARSE was built with optimization level `O0`. This was caused by a bug in the hash tables that could allow keys to be inserted twice.
* Fixed an issue in the routine `rocsparse_spgemm` when using `rocsparse_spgemm_stage_symbolic` and `rocsparse_spgemm_stage_numeric`, where the routine would crash when `alpha` and `beta` were passed as host pointers and where `beta != 0`.
* Fixed an issue in `rocsparse_bsrilu0` where the algorithm was running out of bounds of the `bsr_val` array.

### Upcoming changes

* Deprecated `rocsparse_[s|d|c|z]csritilu0_compute` routines. Users should use the newly added `rocsparse_[s|d|c|z]csritilu0_compute_ex` routines going forward.
* Deprecated `rocsparse_[s|d|c|z]csritsv_solve` routines. Users should use the newly added `rocsparse_[s|d|c|z]csritsv_solve_ex` routines going forward.
* Deprecated `AMDGPU_TARGETS` using in cmake files. Users should use `GPU_TARGETS` going forward.

