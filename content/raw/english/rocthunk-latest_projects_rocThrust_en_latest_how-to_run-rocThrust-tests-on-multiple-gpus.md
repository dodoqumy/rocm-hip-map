---
title: "How to run tests on multiple GPUs &#8212; rocThrust Documentation 4.2.0 documentation"
source_url: "https://rocm.docs.amd.com/projects/rocThrust/en/latest/how-to/run-rocThrust-tests-on-multiple-gpus.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:19:25.372764+00:00
content_hash: "e6b3efab9366edde"
---

# How to run tests on multiple GPUs[#](#how-to-run-tests-on-multiple-gpus)

To run tests on multiple GPUs, you can configure your tests using the `AMDGPU_TEST_TARGETS`

option or you can use CTest resource allocation.

The `AMDGPU_TEST_TARGETS`

CTest option lets you specify the families of GPUs on which you want to run your tests. For example, if you have two GPUs from the gfx900 family in your system, you can specify `-DAMDGPU_TEST_TARGETS=gfx900`

when you configure your test to specify that you only want that family of GPUs to be tested. If you don’t set `AMDGPU_TEST_TARGETS`

, the tests will be run on the default device in your system.

You can use CTest resource allocation to run tests in a distributed manner across multiple GPUs and test multiple product families from one invocation.

CTest resource allocation requires a resource specification file. You can generate a resource specification file using the `GenerateResourceSpec.cmake`

utility script.

After you have cloned the `rocThrust`

repository and built rocThrust with the `-DBUILD_TESTS=ON`

option, change directory to the `build`

directory and run:


This will generate a `resources.json`

file in the `build`

directory. Use the `resources.json`

file in your call to `ctest`

.

For example, if you have two compatible GPUs in your system, run:

```
--resource-spec-file ./resources.json --parallel 2
```

Note

CTest resource allocation requires CMake 3.16 or later.
