---
title: "HIPIFY tools for ROCm 7.0.0"
source_url: https://github.com/ROCm/HIPIFY/releases/tag/rocm-7.0.0
source_type: github-release
source_org: ROCm
published_date: 2025-09-16
credibility: 4
lifecycle: latest
tags: [github-release, rocm-7.0.0]
---

# HIPIFY tools for ROCm 7.0.0

> 📦 **Release:** [rocm-7.0.0](https://github.com/ROCm/HIPIFY/releases/tag/rocm-7.0.0)
> **发布:** 2025-09-16

### Added

* CUDA 12.9.1 support
* cuDNN 9.11.0 support
* cuTENSOR 2.2.0.0 support
* LLVM 20.1.8 support

### Resolved issues

* `hipDNN` support is removed by default
* [#1859](https://github.com/ROCm/HIPIFY/issues/1859) [hipify-perl] Fix warnings on unsupported Driver or Runtime APIs which were erroneously not reported
* [#1930](https://github.com/ROCm/HIPIFY/issues/1930) Revise `JIT API`
* [#1962](https://github.com/ROCm/HIPIFY/issues/1962) Support for cuda-samples helper headers
* [#2035](https://github.com/ROCm/HIPIFY/issues/2035) Remove `const_cast<const char**>` in `hiprtcCreateProgram` and `hiprtcCompileProgram`

