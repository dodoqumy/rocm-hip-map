---
title: "rocBLAS 4.4.0 for ROCm 6.4.0"
source_url: https://github.com/ROCm/rocBLAS/releases/tag/rocm-6.4.0
source_type: github-release
source_org: ROCm
published_date: 2025-04-11
credibility: 4
lifecycle: latest
tags: [github-release, rocm-6.4.0]
---

# rocBLAS 4.4.0 for ROCm 6.4.0

> 📦 **Release:** [rocm-6.4.0](https://github.com/ROCm/rocBLAS/releases/tag/rocm-6.4.0)
> **发布:** 2025-04-11


### Added

* rocTX support in rocBLAS (not available on Windows or in the static library version on Linux)
* On gfx12, all functions now support full `rocblas_int` dynamic range for `batch_count`
* `--ninja` build option
* Support for GPU_TARGETS cmake variable

### Changed

* rocblas-test client removes the stress tests unless YAML-based testing or `gtest_filter` adds them
* rocblas clients OpenMP default threading is reduced to be less than the logical core count
* `gemm_ex` testing and timing reuses device memory
* `gemm_ex` timing initializes matrices on device

### Optimized

* Significantly reduced workspace memory requirements for Level 1 ILP64: `iamax` and `iamin`
* Reduced workspace memory requirements for Level 1 ILP64: `dot`, `asum`, `nrm2`
* Improved the performance of Level 2 gemv for the problem sizes (`TransA == N && m > 2*n`) and (`TransA == T`)
* Improved the performance of Level 3 syrk and herk for the problem size (`k > 500 && n < 4000`)

### Resolved issues

* gfx12: `ger`, `geam`, `geam_ex`, `dgmm`, `trmm`, `symm`, `hemm`, ILP64 `gemm`, and larger data support
* Added a `gfortran` package dependency for Azure Linux OS
* Outdated SLES OS package dependencies (`cxxtools` and `joblib`) in `install.sh -d`
* Code object stripping for RPM packages

### Upcoming changes

* Deprecated the cmake variable `AMDGPU_TARGETS`. Use `GPU_TARGETS` instead.

