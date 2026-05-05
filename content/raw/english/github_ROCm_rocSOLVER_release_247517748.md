---
title: "rocSOLVER 3.30.0 for ROCm 7.0.0"
source_url: https://github.com/ROCm/rocSOLVER/releases/tag/rocm-7.0.0
source_type: github-release
source_org: ROCm
published_date: 2025-09-16
credibility: 4
lifecycle: latest
tags: [github-release, rocm-7.0.0]
---

# rocSOLVER 3.30.0 for ROCm 7.0.0

> 📦 **Release:** [rocm-7.0.0](https://github.com/ROCm/rocSOLVER/releases/tag/rocm-7.0.0)
> **发布:** 2025-09-16


### Added

* Hybrid computation support for existing routines:
    - STEQR

### Optimized

* Improved the performance of BDSQR and downstream functions such as GESVD
* Improved the performance of STEQR and downstream functions such as SYEV/HEEV
* Improved the performance of LARFT and downstream functions such as GEQR2 and GEQRF

### Resolved issues

* Fixed corner cases that can produce NaNs in SYEVD, for valid input matrices


