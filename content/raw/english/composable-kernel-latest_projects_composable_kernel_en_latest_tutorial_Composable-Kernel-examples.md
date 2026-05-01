---
title: "Composable Kernel examples and tests &#8212; Composable Kernel 1.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/composable_kernel/en/latest/tutorial/Composable-Kernel-examples.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:16:35.430890+00:00
content_hash: "d4fe211c66b23a1b"
---

# Composable Kernel examples and tests[#](#composable-kernel-examples-and-tests)

After [building and installing Composable Kernel](../install/Composable-Kernel-install.html), the examples and tests will be moved to `/opt/rocm/bin/`

.

All tests have the prefix `test`

and all examples have the prefix `example`

.

Use `ctest`

with no arguments to run all examples and tests, or use `ctest -R`

to run a single test. For example:

```
-R test_gemm_fp16
```

Examples can be run individually as well. For example:

```
1 1 1
```

For instructions on how to run individual examples and tests, see their README files in the [ example](https://github.com/ROCm/rocm-libraries/tree/develop/projects/composablekernel/example) and

[GitHub folders.](https://github.com/ROCm/rocm-libraries/tree/develop/projects/composablekernel/test)

`test`

To run smoke tests, use `make smoke`

.

To run regression tests, use `make regression`

.

In general, tests that run for under thirty seconds are included in the smoke tests and tests that run for over thirty seconds are included in the regression tests.
