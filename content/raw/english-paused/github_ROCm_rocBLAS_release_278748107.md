---
title: "rocBLAS 5.2.0 for ROCm 7.2.0"
source_url: https://github.com/ROCm/rocBLAS/releases/tag/rocm-7.2.0
source_type: github-release
source_org: ROCm
published_date: 2026-01-21
credibility: 4
lifecycle: latest
tags: [github-release, rocm-7.2.0]
---

# rocBLAS 5.2.0 for ROCm 7.2.0

> 📦 **Release:** [rocm-7.2.0](https://github.com/ROCm/rocBLAS/releases/tag/rocm-7.2.0)
> **发布:** 2026-01-21


### Added
* Level 3 `syrk_ex` function for both C and FORTRAN but without API support for the ILP64 format.

### Optimized
* Level 2 `tpmv` and `sbmv` functions.

### Resolved issues
* Corrected client memory use counts for the `ROCBLAS_CLIENT_RAM_GB_LIMIT` environment variable.
* Fix to avoid false Clang static analysis warnings.

