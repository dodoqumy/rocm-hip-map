---
title: "hipSOLVER compatibility API: dense matrices &#8212; hipSOLVER 3.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/dense-api/index.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:20:40.399803+00:00
content_hash: "edf66028a9cda4c4"
---

# hipSOLVER compatibility API: dense matrices[#](#hipsolver-compatibility-api-dense-matrices)

Here are the method signatures for the wrapper functions that hipSOLVER implements.
For a complete description of the behavior and arguments of the functions, see the corresponding backend documentation
at [cuSOLVER API](https://docs.nvidia.com/cuda/cusolver/) and [rocSOLVER API](https://rocm.docs.amd.com/projects/rocSOLVER/en/latest/reference/intro.html).

For ease of porting from existing cuSOLVER applications to hipSOLVER, functions in the hipsolverDn compatibility API are designed to have
method signatures that are consistent with the cusolverDn interface. However, [performance issues](../../howto/usage.html#dense-performance) might arise when
using the rocSOLVER backend due to differing workspace requirements. If you are interested in achieving the best performance with
the rocSOLVER backend, review the [regular API documentation](../api/index.html#library-api) and transition from the compatibility API to
the regular API at the earliest convenience. See [Using hipSOLVER](../../howto/usage.html#usage-label) for additional [considerations regarding the use of
the compatibility API](../../howto/usage.html#dense-api-differences).
