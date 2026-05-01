---
title: "RCCL 2.27.7 for ROCm 7.1.0"
source_url: https://github.com/ROCm/rccl/releases/tag/rocm-7.1.0
source_type: github-release
source_org: ROCm
published_date: 2025-10-30
credibility: 4
lifecycle: latest
tags: [github-release, rocm-7.1.0]
---

# RCCL 2.27.7 for ROCm 7.1.0

> 📦 **Release:** [rocm-7.1.0](https://github.com/ROCm/rccl/releases/tag/rocm-7.1.0)
> **发布:** 2025-10-30


### Added
* Added `RCCL_P2P_BATCH_THRESHOLD` to set the message size limit for batching P2P operations. This mainly affects small message performance for alltoall at a large scale but also applies to alltoallv.
* Added `RCCL_P2P_BATCH_ENABLE` to enable batching P2P operations to receive performance gains for smaller messages up to 4MB for alltoall when the workload requires it. This is to avoid performance dips for larger messages.

### Changed

* The MSCCL++ feature is now disabled by default. The `--disable-mscclpp` build flag is replaced with `--enable-mscclpp` in the `rccl/install.sh` script.
* Compatibility with NCCL 2.27.7

### Resolved issues
* Improve small message performance for alltoall by enabling and optimizing batched P2P operations. 

### Known issues
* Symmetric memory kernels are currently disabled due to ongoing CUMEM enablement work.

