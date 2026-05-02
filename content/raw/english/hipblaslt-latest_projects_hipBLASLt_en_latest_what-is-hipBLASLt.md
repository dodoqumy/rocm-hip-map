---
title: "What is hipBLASLt? &#8212; hipBLASLt 1.2.2 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipBLASLt/en/latest/what-is-hipBLASLt.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:06:41.534014+00:00
content_hash: "7ff922c8e8897616"
---

# What is hipBLASLt?[#](#what-is-hipblaslt)

hipBLASLt is a library that provides GEMM operations with flexible APIs and extends functionality beyond the traditional BLAS library.
hipBLASLt provides APIs in the [HIP programming language](https://rocm.docs.amd.com/projects/HIP/en/latest/index.html) with an underlying optimized generator as a backend kernel provider.

The library adds flexibility for matrix data layouts, input types, and compute types and for choosing the algorithmic implementations and heuristics through parameter programmability. After identifying a set of options for the intended GEMM operations, you can repeatedly use these options for different inputs.

The GEMM operation of hipBLASLt is performed by [hipblasLtMatmul()](reference/api-reference.html#hipblasltmatmul) using this equation:

where \(op(A)/op(B)\) refers to in-place operations such as transpose/non-transpose and \(alpha\) and \(beta\) are the scalars. The \(Activation\) function supports Gelu, Relu, Swish (SiLU), and Clamp. The \(Bias\) vector matches matrix \(D\) rows and broadcasts to all \(D\) columns.
