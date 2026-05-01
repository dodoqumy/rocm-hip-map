---
title: "HIPIFY tools for ROCm 7.2.0"
source_url: https://github.com/ROCm/HIPIFY/releases/tag/rocm-7.2.0
source_type: github-release
source_org: ROCm
published_date: 2026-01-21
credibility: 4
lifecycle: latest
tags: [github-release, rocm-7.2.0]
---

# HIPIFY tools for ROCm 7.2.0

> 📦 **Release:** [rocm-7.2.0](https://github.com/ROCm/HIPIFY/releases/tag/rocm-7.2.0)
> **发布:** 2026-01-21

### Added

* Partial support for CUDA 13.0.0
* cuDNN 9.14.0 support
* cuTENSOR 2.3.1.0 support
* LLVM 21.1.6 support
* Full `hipFFTw` support
* [#2062](https://github.com/ROCm/HIPIFY/issues/2062) Partial hipification support for a particular CUDA API
* [#2073](https://github.com/ROCm/HIPIFY/issues/2073) Detect CUDA version before hipification
* New options:
  * `--local-headers` to enable hipification of quoted local headers (non-recursive)
  * `--local-headers-recursive` to enable hipification of quoted local headers recursively

### Resolved issues

* [#2088](https://github.com/ROCm/HIPIFY/issues/2088) Missing support of `cuda_bf16.h` import in hipification
