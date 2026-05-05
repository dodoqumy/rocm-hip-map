---
title: "rocFFT 1.0.36 for ROCm 7.2.0"
source_url: https://github.com/ROCm/rocFFT/releases/tag/rocm-7.2.0
source_type: github-release
source_org: ROCm
published_date: 2026-01-21
credibility: 4
lifecycle: latest
tags: [github-release, rocm-7.2.0]
---

# rocFFT 1.0.36 for ROCm 7.2.0

> 📦 **Release:** [rocm-7.2.0](https://github.com/ROCm/rocFFT/releases/tag/rocm-7.2.0)
> **发布:** 2026-01-21


### Optimized

* Removed a potential unnecessary global transpose operation from MPI 3D multi-GPU pencil decompositions.
* Enabled optimization of 3D pencil decompositions for single-process multi-GPU transforms.

### Resolved issues

* Fixed potential division by zero when constructing plans using dimensions of length 1.
* Fixed result scaling on multi-device transforms.
* Fixed callbacks on multi-device transforms.

