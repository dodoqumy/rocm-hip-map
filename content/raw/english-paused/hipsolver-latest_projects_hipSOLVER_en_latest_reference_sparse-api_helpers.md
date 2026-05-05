---
title: "Sparse matrix helper functions &#8212; hipSOLVER 3.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/sparse-api/helpers.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:20:46.878075+00:00
content_hash: "3d92cfe966cdbc2d"
---

# Sparse matrix helper functions[#](#sparse-matrix-helper-functions)

These helper functions control aspects of the hipSOLVER library. They are divided into the following categories:

[Handle setup and teardown](#sparse-initialize): Functions to initialize and cleanup the library handle.[Stream manipulation](#sparse-stream): Functions to manipulate streams.

## Handle setup and teardown[#](#handle-setup-and-teardown)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverSpCreate([hipsolverSpHandle_t](types.html#_CPPv419hipsolverSpHandle_t)*handle)[#](#_CPPv417hipsolverSpCreateP19hipsolverSpHandle_t)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverSpDestroy([hipsolverSpHandle_t](types.html#_CPPv419hipsolverSpHandle_t)handle)[#](#_CPPv418hipsolverSpDestroy19hipsolverSpHandle_t)

## Stream manipulation[#](#stream-manipulation)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverSpSetStream([hipsolverSpHandle_t](types.html#_CPPv419hipsolverSpHandle_t)handle, hipStream_t streamId)[#](#_CPPv420hipsolverSpSetStream19hipsolverSpHandle_t11hipStream_t)
