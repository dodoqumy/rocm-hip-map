---
title: "rocFFT 1.0.34 for ROCm 7.0.0"
source_url: https://github.com/ROCm/rocFFT/releases/tag/rocm-7.0.0
source_type: github-release
source_org: ROCm
published_date: 2025-09-16
credibility: 4
lifecycle: latest
tags: [github-release, rocm-7.0.0]
---

# rocFFT 1.0.34 for ROCm 7.0.0

> 📦 **Release:** [rocm-7.0.0](https://github.com/ROCm/rocFFT/releases/tag/rocm-7.0.0)
> **发布:** 2025-09-16


### Added

* Added gfx950 support.

### Removed

* Removed rocfft-rider legacy compatibility from clients
* Removed support for the gfx940 and gfx941 targets from the client programs.
* Removed backward compatibility symlink for include directories.

### Optimized

* Removed unnecessary HIP event/stream allocation and synchronization during MPI transforms.
* Implemented single-precision 1D kernels for lengths:
  - 4704
  - 5488
  - 6144
  - 6561
  - 8192
* Implemented single-kernel plans for some large 1D problem sizes, on devices with at least 160KiB of LDS.

### Resolved issues

* Fixed kernel faults on multi-device transforms that gather to a single device, when the input/output bricks are not 
  contiguous.

