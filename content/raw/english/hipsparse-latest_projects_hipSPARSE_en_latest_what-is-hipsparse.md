---
title: "What is hipSPARSE &#8212; hipSPARSE 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipSPARSE/en/latest/what-is-hipsparse.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:10:01.307340+00:00
content_hash: "1cd1b289cd123a4e"
---

# What is hipSPARSE[#](#what-is-hipsparse)

hipSPARSE is a library that contains basic linear algebra subroutines for sparse matrices and vectors,
written in [HIP](https://rocm.docs.amd.com/projects/HIP/en/latest/index.html) for GPU devices.
It is designed to be called from C and C++ code.

hipSPARSE is a SPARSE marshalling library, with multiple supported backends.
It lies between the application and a “worker” SPARSE library,
marshalling inputs into the backend library and results back to the application.
hipSPARSE exports a common interface that does not require the client to change, regardless of the chosen backend.
It supports [rocSPARSE](https://rocm.docs.amd.com/projects/rocSPARSE/en/latest/index.html) and NVIDIA CUDA cuSPARSE as backends.

The hipSPARSE functionality is organized into the following categories:

[Sparse auxiliary functions](reference/auxiliary.html#hipsparse-auxiliary-functions): Available helper functions that are required for subsequent library calls.[Sparse level 1 functions](reference/level1.html#hipsparse-level1-functions): Operations between a vector in sparse format and a vector in dense format.[Sparse level 2 functions](reference/level2.html#hipsparse-level2-functions): Operations between a matrix in sparse format and a vector in dense format.[Sparse level 3 functions](reference/level3.html#hipsparse-level3-functions): Operations between a matrix in sparse format and multiple vectors in dense format.[Sparse extra functions](reference/extra.html#hipsparse-extra-functions): Operations that manipulate sparse matrices.[Preconditioner functions](reference/precond.html#hipsparse-precond-functions): Operations that manipulate a matrix in sparse format to obtain a preconditioner.[Sparse conversion functions](reference/conversion.html#hipsparse-conversion-functions): Operations on a matrix in sparse format to obtain a different matrix format.[Sparse reordering functions](reference/reorder.html#hipsparse-reordering-functions): Operations on a matrix in sparse format to obtain a reordering.[Sparse generic functions](reference/generic.html#hipsparse-generic-functions): Operations that manipulate sparse matrices.

The source code can be found at [ROCm/rocm-libraries](https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipsparse).
