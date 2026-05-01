---
title: "rocFFT 1.0.32 for ROCm 6.4.0"
source_url: https://github.com/ROCm/rocFFT/releases/tag/rocm-6.4.0
source_type: github-release
source_org: ROCm
published_date: 2025-04-11
credibility: 4
lifecycle: latest
tags: [github-release, rocm-6.4.0]
---

# rocFFT 1.0.32 for ROCm 6.4.0

> 📦 **Release:** [rocm-6.4.0](https://github.com/ROCm/rocFFT/releases/tag/rocm-6.4.0)
> **发布:** 2025-04-11


### Changed

* Building with the address sanitizer option sets xnack+ on relevant GPU
  architectures and adds address-sanitizer support to runtime-compiled
  kernels.
* The `AMDGPU_TARGETS` build variable should be replaced with `GPU_TARGETS`. `AMDGPU_TARGETS` is deprecated.

### Removed

* Removed ahead-of-time compiled kernels for the gfx906, gfx940, and gfx941 architectures. These architectures still
  function the same, but kernels for them are now compiled at runtime.
* Removed consumer GPU architectures from the precompiled kernel cache that ships with
  rocFFT. rocFFT continues to ship with a cache of precompiled RTC kernels for data-center
  and workstation architectures. As before, user-level caches can be enabled by setting the
  environment variable ROCFFT_RTC_CACHE_PATH to a writeable file location.

### Optimized

* Improved MPI transform performance by using all-to-all communication for global transpose operations.  
  Point-to-point communications are still used when all-to-all is not possible.
* Improved the performance of unit-strided, complex interleaved, forward and inverse, length (64,64,64) FFTs.

### Resolved issues

* Fixed incorrect results from 2-kernel 3D FFT plans that used non-default output strides. For more information, see the [rocFFT GitHub issue](https://github.com/ROCm/rocFFT/issues/507).
* Plan descriptions can be reused with different strides for different plans. For more information, see the [rocFFT GitHub issue](https://github.com/ROCm/rocFFT/issues/504).
* Fixed client packages to depend on hipRAND instead of rocRAND.
* Fixed potential integer overflows during large MPI transforms.

