---
title: "rocSPARSE 4.1.0 for ROCm 7.1.0"
source_url: https://github.com/ROCm/rocSPARSE/releases/tag/rocm-7.1.0
source_type: github-release
source_org: ROCm
published_date: 2025-10-30
credibility: 4
lifecycle: latest
tags: [github-release, rocm-7.1.0]
---

# rocSPARSE 4.1.0 for ROCm 7.1.0

> 📦 **Release:** [rocm-7.1.0](https://github.com/ROCm/rocSPARSE/releases/tag/rocm-7.1.0)
> **发布:** 2025-10-30


### Added

* Added brain half float mixed precision to `rocsparse_axpby` where X and Y use bfloat16 and result and the compute type use float.
* Added brain half float mixed precision to `rocsparse_spvv` where X and Y use bfloat16 and result and the compute type use float.
* Added brain half float mixed precision to `rocsparse_spmv` where A and X use bfloat16 and Y and the compute type use float.
* Added brain half float mixed precision to `rocsparse_spmm` where A and B use bfloat16 and C and the compute type use float.
* Added brain half float mixed precision to `rocsparse_sddmm` where A and B use bfloat16 and C and the compute type use float.
* Added brain half float mixed precision to `rocsparse_sddmm` where A and B and C use bfloat16 and the compute type use float.
* Added half float mixed precision to `rocsparse_sddmm` where A and B and C use float16 and the compute type use float.
* Added brain half float uniform precision to `rocsparse_scatter` and `rocsparse_gather` routines.

### Optimized

* Improved the user documentation.

### Upcoming changes

* Deprecate trace, debug, and bench logging using environment variable `ROCSPARSE_LAYER`.

