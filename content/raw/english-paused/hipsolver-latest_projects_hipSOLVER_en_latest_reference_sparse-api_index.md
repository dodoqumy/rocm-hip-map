---
title: "hipSOLVER compatibility API: sparse matrices &#8212; hipSOLVER 3.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/sparse-api/index.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:21:05.273996+00:00
content_hash: "d565faf99d7fc987"
---

# hipSOLVER compatibility API: sparse matrices[#](#hipsolver-compatibility-api-sparse-matrices)

Here are the method signatures for the wrapper functions that hipSOLVER implements.
For a complete description of the behavior and arguments of the functions,
see the corresponding backend documentation
at [cuSOLVER API](https://docs.nvidia.com/cuda/cusolver/index.html#cuds-api) and [rocSOLVER API](https://rocm.docs.amd.com/projects/rocSOLVER/en/latest/reference/intro.html).

For ease of porting from existing cuSOLVER applications to hipSOLVER, functions in the hipsolverSp compatibility API are designed to have method signatures that are consistent with the cusolverSp interface. The equivalent functions have not been added to the regular hipSOLVER API.

Note

There are [some performance limitations](../../howto/usage.html#sparse-performance) when using the rocSOLVER backend because not all
functionality required for optimal performance has been implemented yet.
