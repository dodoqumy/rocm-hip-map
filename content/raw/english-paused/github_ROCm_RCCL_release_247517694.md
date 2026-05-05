---
title: "RCCL 2.26.6 for ROCm 7.0.0"
source_url: https://github.com/ROCm/rccl/releases/tag/rocm-7.0.0
source_type: github-release
source_org: ROCm
published_date: 2025-09-16
credibility: 4
lifecycle: latest
tags: [github-release, rocm-7.0.0]
---

# RCCL 2.26.6 for ROCm 7.0.0

> 📦 **Release:** [rocm-7.0.0](https://github.com/ROCm/rccl/releases/tag/rocm-7.0.0)
> **发布:** 2025-09-16


### Resolved issues

* Resolved an issue when using more than 64 channels when multiple collectives are used in the same `ncclGroup()` call.
* Fixed unit test failures in tests ending with `ManagedMem` and `ManagedMemGraph` suffixes.
* Suboptimal algorithmic switching point for AllReduce on MI300x.
* Fixed the known issue "When splitting a communicator using `ncclCommSplit` in some GPU configurations, MSCCL initialization can cause a segmentation fault." with a design change to use `comm` instead of `rank` for `mscclStatus`. The Global map for `comm` to `mscclStatus` is still not thread safe but should be explicitly handled by mutexes for read writes. This is tested for correctness, but there is a plan to use a thread-safe map data structure in upcoming changes.

### Added

* Added support for extended fine-grained system memory pool.
* Added new GPU target `gfx950`.
* Added support for `unroll=1` in device-code generation to improve performance.
* Set a default of 112 channels for a single node with `8 * gfx950`.
* Enabled LL128 protocol on `gfx950`.
* Adding ability to choose unroll factor at runtime via `RCCL_UNROLL_FACTOR`.  This can be set at runtime to 1, 2, or 4.  This change currently increases compilation and linking time because it triples the number of kernels generated.
* Added MSCCL support for AllGather multinode gfx942/gfx950 (i.e., 16 and 32 GPUs). To enable, set the environment variable `RCCL_MSCCL_FORCE_ENABLE=1`. Max message size for MSCCL AllGather usage is `12292 * sizeof(datatype) * nGPUs`.
* Thread thresholds for LL/LL128 are selected in Tuning Models for the MI300X. This impacts the number of channels used for AG and RS. Channel tuning model is bypassed if `NCCL_THREAD_THRESHOLDS`, `NCCL_MIN_NCHANNELS', or 'NCCL_MAX_NCHANNELS` are set.
* Multi-node tuning for AllGather, AllReduce, and ReduceScatter that leverages LL/LL64/LL128 protocol to use nontemporal vector load/store for tunable message size ranges.
* LL/LL128 usage ranges for AR, AG, and RS are part of the tuning models, which enable architecture-specific tuning in conjunction with the existing Rome Models scheme in RCCL.
* Two new APIs are exposed as part of an initiative to separate RCCL code. These APIs are `rcclGetAlgoInfo` and `rcclFuncMaxSendRecvCount`. However, user-level invocation requires that RCCL be built with `RCCL_EXPOSE_STATIC` enabled.

### Changed

* Compatibility with NCCL 2.23.4
* Compatibility with NCCL 2.24.3
* Compatibility with NCCL 2.25.1
* Compatibility with NCCL 2.26.6

