---
title: "hipSOLVER compatibility API: refactorization &#8212; hipSOLVER 3.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/refactor-api/index.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:08:16.943398+00:00
content_hash: "923b9e1bc9363be9"
---

# hipSOLVER compatibility API: refactorization[#](#hipsolver-compatibility-api-refactorization)

This section lists the method signatures for the wrapper functions that hipSOLVER implements.
For a complete description of the behavior and arguments of the functions, see the corresponding backend documentation
at [cuSOLVER API](https://docs.nvidia.com/cuda/cusolver/index.html#cuds-api) and [rocSOLVER API](https://rocm.docs.amd.com/projects/rocSOLVER/en/latest/reference/intro.html).

For ease of porting from existing cuSOLVER applications to hipSOLVER, functions in the hipsolverRf compatibility API are designed to have method signatures that are consistent with the cusolverRf interface. Equivalent functions have not yet been added to the regular hipSOLVER API.
