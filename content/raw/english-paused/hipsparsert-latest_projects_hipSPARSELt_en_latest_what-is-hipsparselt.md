---
title: "What is hipSPARSELt? &#8212; hipSPARSELt 0.2.6 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipSPARSELt/en/latest/what-is-hipsparselt.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:07:18.767806+00:00
content_hash: "ecedd67c74733aa2"
---

# What is hipSPARSELt?[#](#what-is-hipsparselt)

hipSPARSELt is a SPARSE marshalling library with multiple supported backends. It presents a common interface that provides Basic Linear Algebra Subroutines (BLAS) for sparse computation, implemented on top of the AMD ROCm runtime and toolchains.

The hipSPARSELt library is created using the [HIP](https://rocm.docs.amd.com/projects/HIP/en/latest/index.html)
programming language and is optimized for the latest AMD discrete GPUs.

hipSPARSELt sits between the application and a “worker” SPARSE library, marshalling inputs into the
backend library and results back to the application. It exports an interface that doesn’t
require the client to change, regardless of the chosen backend. The supported backends are:
[rocSPARSELt](https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipsparselt/library/src/hcc_detail/rocsparselt)
and NVIDIA CUDA [cuSPARSELt v0.6.3](https://docs.nvidia.com/cuda/cusparselt).
