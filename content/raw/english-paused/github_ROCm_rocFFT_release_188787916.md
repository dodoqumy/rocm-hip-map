---
title: "rocFFT 1.0.31 for ROCm 6.3.0"
source_url: https://github.com/ROCm/rocFFT/releases/tag/rocm-6.3.0
source_type: github-release
source_org: ROCm
published_date: 2024-12-03
credibility: 4
lifecycle: latest
tags: [github-release, rocm-6.3.0]
---

# rocFFT 1.0.31 for ROCm 6.3.0

> 📦 **Release:** [rocm-6.3.0](https://github.com/ROCm/rocFFT/releases/tag/rocm-6.3.0)
> **发布:** 2024-12-03


### Added

* rocfft-test now includes a --smoketest option.
* Support for the gfx1151, gfx1200, and gfx1201 architectures.
* Implemented experimental APIs to allow computing FFTs on data
  distributed across multiple MPI ranks. These APIS can be enabled with the
  `ROCFFT_MPI_ENABLE` CMake option.  This option defaults to `OFF`.

  When `ROCFFT_MPI_ENABLE` is `ON`:

  * `rocfft_plan_description_set_comm` can be called to provide an
    MPI communicator to a plan description, which can then be passed
    to `rocfft_plan_create`.  Each rank calls
    `rocfft_field_add_brick` to specify the layout of data bricks on
    that rank.

  * An MPI library with ROCm acceleration enabled is required at
    build time and at runtime.

### Changed

* Compilation uses amdclang++ instead of hipcc.
* CLI11 replaces Boost Program Options as the command line parser for clients and samples.
* Building with the address sanitizer option sets xnack+ on relevant GPU
  architectures and address-sanitizer support is added to runtime-compiled
  kernels.

