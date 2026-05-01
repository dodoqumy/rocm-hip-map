---
title: "rocFFT 1.0.30 for ROCm 6.2.4"
source_url: https://github.com/ROCm/rocFFT/releases/tag/rocm-6.2.4
source_type: github-release
source_org: ROCm
published_date: 2024-11-06
credibility: 4
lifecycle: latest
tags: [github-release, rocm-6.2.4]
---

# rocFFT 1.0.30 for ROCm 6.2.4

> 📦 **Release:** [rocm-6.2.4](https://github.com/ROCm/rocFFT/releases/tag/rocm-6.2.4)
> **发布:** 2024-11-06


### Added

* GFX1151 Support

### Optimized

* Implemented 1D kernels for factorizable sizes > 1024 and < 2048.

### Resolved issues

* Fixed plan creation failure on some even-length real-complex transforms that use Bluestein's algorithm.

