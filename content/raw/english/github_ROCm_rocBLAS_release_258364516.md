---
title: "rocBLAS 5.1.0 for ROCm 7.1.0"
source_url: https://github.com/ROCm/rocBLAS/releases/tag/rocm-7.1.0
source_type: github-release
source_org: ROCm
published_date: 2025-10-30
credibility: 4
lifecycle: latest
tags: [github-release, rocm-7.1.0]
---

# rocBLAS 5.1.0 for ROCm 7.1.0

> 📦 **Release:** [rocm-7.1.0](https://github.com/ROCm/rocBLAS/releases/tag/rocm-7.1.0)
> **发布:** 2025-10-30


### Added
* Sample for clients using OpenMP threads calling rocBLAS functions.
* gfx1103, gfx1150, and gfx1151 enabled.

### Changed
* By default, the Tensile build is no longer based on `tensile_tag.txt` but uses the same commit from shared/tensile in the rocm-libraries repository. The rmake or install `-t` option can build from another local path with a different commit.

### Optimized

* Improved the performance of Level 2 gemv transposed (`TransA != N`) for the problem sizes where `m` is small and `n` is large on gfx90a and gfx942.

