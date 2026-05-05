---
title: "rocSPARSE 3.3.0 for ROCm 6.3.0"
source_url: https://github.com/ROCm/rocSPARSE/releases/tag/rocm-6.3.0
source_type: github-release
source_org: ROCm
published_date: 2024-12-04
credibility: 4
lifecycle: latest
tags: [github-release, rocm-6.3.0]
---

# rocSPARSE 3.3.0 for ROCm 6.3.0

> 📦 **Release:** [rocm-6.3.0](https://github.com/ROCm/rocSPARSE/releases/tag/rocm-6.3.0)
> **发布:** 2024-12-04

### Added

* Add `rocsparse_create_extract_descr`, `rocsparse_destroy_extract_descr`, `rocsparse_extract_buffer_size`, `rocsparse_extract_nnz`, and `rocsparse_extract` APIs to allow extraction of the upper or lower part of sparse CSR or CSC matrices.
* Support for the gfx1151, gfx1200, and gfx1201 architectures.

### Changed

* Change the default compiler from hipcc to amdclang in install script and cmake files.
* Change address sanitizer build targets so that only gfx908:xnack+, gfx90a:xnack+, gfx940:xnack+, gfx941:xnack+, and gfx942:xnack+ are built when `BUILD_ADDRESS_SANITIZER=ON` is configured.

### Optimized

* Improved user documentation

### Resolved issues

* Fixed the `csrmm` merge path algorithm so that diagonal is clamped to the correct range.
* Fixed a race condition in `bsrgemm` that could on rare occasions cause incorrect results.
* Fixed an issue in `hyb2csr` where the CSR row pointer array was not being properly filled when `n=0`, `coo_nnz=0`, or `ell_nnz=0`. 
* Fixed scaling in `rocsparse_Xhybmv` when only performing `y=beta*y`, for example, where `alpha==0` in `y=alpha*Ax+beta*y`.
* Fixed `rocsparse_Xgemmi` failures when the y grid dimension is too large. This occured when n >= 65536.
* Fixed the gfortran dependency for the `azurelinux` operating system.

