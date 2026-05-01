---
title: "HIPIFY tools for ROCm 6.4.0"
source_url: https://github.com/ROCm/HIPIFY/releases/tag/rocm-6.4.0
source_type: github-release
source_org: ROCm
published_date: 2025-04-11
credibility: 4
lifecycle: latest
tags: [github-release, rocm-6.4.0]
---

# HIPIFY tools for ROCm 6.4.0

> 📦 **Release:** [rocm-6.4.0](https://github.com/ROCm/HIPIFY/releases/tag/rocm-6.4.0)
> **发布:** 2025-04-11

### Added

* CUDA 12.6.3 support
* cuDNN 9.7.0 support
* cuTENSOR 2.0.2.1 support
* LLVM 19.1.7 support
* Full support for direct hipification of `cuRAND` into `rocRAND` under the `--roc` option
* [#1617](https://github.com/ROCm/HIPIFY/issues/1617) Support for `fp8` math device/host API

### Resolved issues

* `MIOpen` support in hipify-perl under the `-miopen` option
* Use `const_cast<const char**>` for the last arguments in the `hiprtcCreateProgram` and `hiprtcCompileProgram` function calls, as in CUDA, they are of the `const char* const*` type
* [#1769](https://github.com/ROCm/HIPIFY/issues/1769) Support for `fp16` device/host API
* [#1800](https://github.com/ROCm/HIPIFY/issues/1800) Fix instructions on building LLVM for HIPIFY on Linux

### Known issues

* [#833](https://github.com/ROCm/HIPIFY/issues/833) `hipify-clang` build failure against LLVM 15-18 on `Ubuntu`, `CentOS`, and `Fedora`

