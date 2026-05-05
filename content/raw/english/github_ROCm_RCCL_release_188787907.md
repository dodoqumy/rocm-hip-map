---
title: "RCCL 2.21.5 for ROCm 6.3.0"
source_url: https://github.com/ROCm/rccl/releases/tag/rocm-6.3.0
source_type: github-release
source_org: ROCm
published_date: 2024-12-03
credibility: 4
lifecycle: latest
tags: [github-release, rocm-6.3.0]
---

# RCCL 2.21.5 for ROCm 6.3.0

> 📦 **Release:** [rocm-6.3.0](https://github.com/ROCm/rccl/releases/tag/rocm-6.3.0)
> **发布:** 2024-12-03


### Added

* MSCCL++ integration for specific contexts
* Performance collection to rccl_replayer
* Tuner Plugin example for MI300
* Tuning table for large number of nodes
* Support for amdclang++
* New Rome model

### Changed

* Compatibility with NCCL 2.21.5
* Increased channel count for MI300X multi-node
* Enabled MSCCL for single-process multi-threaded contexts
* Enabled gfx12
* Enabled CPX mode for MI300X
* Enabled tracing with rocprof
* Improved version reporting
* Enabled GDRDMA for Linux kernel 6.4.0+

### Resolved issues

* Fixed model matching with PXN enable

### Known issues

* MSCCL is temporarily disabled for AllGather collectives.
  - This can impact in-place messages (< 2 MB) with ~2x latency.
  - Older RCCL versions are not impacted.
  - This issue will be addressed in a future ROCm release.
* Unit tests do not exit gracefully when running on a single GPU.
  - This issue will be addressed in a future ROCm release.

