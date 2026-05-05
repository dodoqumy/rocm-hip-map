---
title: "hipSOLVER regular API &#8212; hipSOLVER 3.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/index.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:20:36.192529+00:00
content_hash: "3f32d6c9d611eda5"
---

# hipSOLVER regular API[#](#hipsolver-regular-api)

This topic provides the method signatures for the wrapper functions that hipSOLVER implements.
For a complete description of the behavior and arguments of the functions, see the corresponding backend documentation
at [cuSOLVER API](https://docs.nvidia.com/cuda/cusolver/) and [rocSOLVER API](https://rocm.docs.amd.com/projects/rocSOLVER/en/latest/reference/intro.html).

The hipSOLVER API is designed to be similar to the cuSOLVER and rocSOLVER interfaces, but it requires some minor adjustments to ensure
the best performance out of both backends. This involves the addition of workspace parameters and some additional API methods.
See [Using hipSOLVER](../../howto/usage.html#usage-label) for a complete list of [API differences](../../howto/usage.html#api-differences).

If you’re interested in using hipSOLVER without these adjustments, so that the interface matches cuSOLVER, consult the
[Compatibility API documentation](../dense-api/index.html#library-dense) instead. See [the porting section](../../howto/usage.html#porting) for more details.
