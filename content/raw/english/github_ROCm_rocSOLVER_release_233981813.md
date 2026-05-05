---
title: "rocSOLVER 3.28.2 for ROCm 6.4.2"
source_url: https://github.com/ROCm/rocSOLVER/releases/tag/rocm-6.4.2
source_type: github-release
source_org: ROCm
published_date: 2025-07-21
credibility: 4
lifecycle: latest
tags: [github-release, rocm-6.4.2]
---

# rocSOLVER 3.28.2 for ROCm 6.4.2

> 📦 **Release:** [rocm-6.4.2](https://github.com/ROCm/rocSOLVER/releases/tag/rocm-6.4.2)
> **发布:** 2025-07-21


### Added

* Hybrid computation support for existing routines:
    - STERF
* SVD for general matrices based on Cuppen's Divide and Conquer algorithm:
    - GESDD (with batched and strided\_batched versions)

### Optimized

* Reduced the device memory requirements for STEDC, SYEVD/HEEVD, and SYGVD/HEGVD
* Improved the performance of STEDC and divide and conquer Eigensolvers
* Improved the performance of SYTRD, the initial step of the Eigensolvers that start with the tridiagonalization of the input matrix


