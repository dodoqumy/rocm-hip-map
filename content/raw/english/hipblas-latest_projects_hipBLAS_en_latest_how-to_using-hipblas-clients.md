---
title: "Using hipBLAS clients &#8212; hipBLAS 3.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipBLAS/en/latest/how-to/using-hipblas-clients.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:19:16.124582+00:00
content_hash: "983c292a5f14f56c"
---

# Using hipBLAS clients[#](#using-hipblas-clients)

There are two client executables that can be used with hipBLAS. They are:

hipblas-bench

hipblas-test


These two clients can be built by following the instructions in [Installing and building for Linux](../install/Linux_Install_Guide.html).
After building, the hipBLAS clients can be found in the `hipBLAS/build/release/clients/staging`

directory.
See the next two sections for a brief explanation and usage notes for each hipBLAS client.

## hipblas-bench[#](#hipblas-bench)

hipblas-bench is used to measure performance and verify the correctness of hipBLAS functions.

It has a command line interface. For usage information, run this command:

```
--help
```

This example measures the performance of SGEMM:

```
-f gemm -r f32_r --transposeA N --transposeB N -m 4096 -n 4096 -k 4096 --alpha 1 --lda 4096 --ldb 4096 --beta 0 --ldc 4096
```

On a system using an AMD Vega 20 GPU, the previous command displays a performance of 11941.5 Gflops, as shown in the output below:


A helpful way of finding the parameters that can be used with `./hipblas-bench -f gemm`

is to turn on logging
by setting the environment variable `ROCBLAS_LAYER=2`

. For example, if you run this command:

```
ROCBLAS_LAYER=2 ./hipblas-bench -f gemm -i 1 -j 0
```

It logs the following information:

```
-f gemm -r f32_r --transposeA N --transposeB N -m 128 -n 128 -k 128 --alpha 1 --lda 128 --ldb 128 --beta 0 --ldc 128
```

You can copy and change the above command. For example, to change the datatype to IEEE 64-bit and the size to 2048, follow this example:

```
-f gemm -r f64_r --transposeA N --transposeB N -m 2048 -n 2048 -k 2048 --alpha 1 --lda 2048 --ldb 2048 --beta 0 --ldc 2048
```

Logging affects performance, so only use it to log the command of interest, then run the command without logging enabled to measure performance.

Note

hipblas-bench also provides the flag `-v 1`

for correctness checks.

If multiple arguments or functions need to be benchmarked, hipblas-bench supports data-driven benchmarks using a YAML-format specification file.

```
--yaml <file>.yaml
```

For example, `hipblas_smoke.yaml`

is a YAML file used to run a smoke test.
However, other examples can be found in the [rocBLAS](https://github.com/ROCm/rocm-libraries/tree/develop/projects/rocblas) GitHub repository.

## hipblas-test[#](#hipblas-test)

hipblas-test is used to perform hipBLAS unit tests. It uses the GoogleTest framework.

To run the hipBLAS tests, use this command:


To run a subset of tests, provide an optional filter. For example,
to run only the `axpy`

function tests from the command line, use:

```
--gtest_filter=*axpy*
```

The pattern for `--gtest_filter`

is:

```
=POSTIVE_PATTERNS[-NEGATIVE_PATTERNS]
```

If specific function arguments or multiple functions need to be tested, hipblas-test provides support for data-driven testing using a YAML-format test specification file.

```
--yaml <file>.yaml
```

As an example, `hipblas_smoke.yaml`

is a YAML file that is used to run a smoke test.
Other examples can be found in the [rocBLAS](https://github.com/ROCm/rocm-libraries/tree/develop/projects/rocblas) GitHub repository.
YAML-based tests list function parameter values in the test name, which can be also used for
test filtering using the `gtest_filter`

argument.
To run the provided smoke test, use this command:

```
--yaml hipblas_smoke.yaml
```
