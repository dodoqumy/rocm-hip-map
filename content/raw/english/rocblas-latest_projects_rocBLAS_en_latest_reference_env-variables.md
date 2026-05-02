---
title: "Environment variables &#8212; rocBLAS 5.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/env-variables.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:04:56.866692+00:00
content_hash: "f5987a8c40593904"
---

# Environment variables[#](#environment-variables)

The rocBLAS environment variables are collected in the following tables.

|
|
|
|
|---|---|---|---|
`ROCBLAS_USE_HIPBLASLT` Provides manual control over which GEMM backend is used.
|
Unset by default. |
Unset: GEMM backend is automatically selected.0: Tensile is always used as the GEMM backend.1: hipBLASLt is preferred as the GEMM backend, but will fallback to Tensile on problems for which hipBLASLt does not provide a solution or when errors are encountered using the hipBLASLt backend. |
|
`ROCBLAS_USE_HIPBLASLT_BATCHED` Manual control to selectively disable the use of hipBlasLt only for the batched GEMMs.
`ROCBLAS_USE_HIPBLASLT=0` disables the `ROCBLAS_USE_HIPBLASLT_BATCHED` variable, because hipBlasLt would not be enabled. |
1 |
Unset: GEMM batched default backend.0: Tensile is always used as the GEMM batched backend.1: hipBLASLt will be used as the GEMM batched backend when applicable, but will fallback to Tensile on problems for which hipBLASLt does not provide a solution or when errors are encountered using the hipBLASLt backend. |
|
`ROCBLAS_DEVICE_MEMORY_SIZE` Sets how much memory to preallocate.
|
Unset by default. |
0 or unset: Lets rocBLAS manage the device memory.Bigger than 0: Sets the default handle device memory size to the specified size (in bytes). |
|
`ROCBLAS_DEFAULT_ATOMICS_MODE` Sets the default atomics mode during the creation of
`rocblas_handle` . |
Unset by default. |
||
`ROCBLAS_STREAM_ORDER_ALLOC` Allows memory allocation and deallocation to be stream ordered.
|
0 |
0: Disable1: Enable |
|
`ROCBLAS_BENCH_STREAM_SYNC` Benchmark timing based on
`hipStreamSynchronize` , otherwise uses default `hipEvent_t` based timing. |
0 |
0: Disable1: Enable |

## Logging environment variables[#](#logging-environment-variables)

The logging environment variables in rocBLAS are collected in the following
table. For information on how to use these variables, see [rocBLAS logging](../how-to/logging-in-rocblas.html#logging).

|
|
|---|---|
`ROCBLAS_LAYER` A bit mask to control the different types of logging.
|
`ROCBLAS_LAYER == 0` : Logging is disabled.`ROCBLAS_LAYER & 1 == 1` : Trace logging is enabled.`ROCBLAS_LAYER & 2 == 1` : Bench logging is enabled.`ROCBLAS_LAYER & 4 == 1` : Profile logging is enabled.`ROCBLAS_LAYER & 8 == 1` : Internal API logging is enabled. |
`ROCBLAS_LOG_PATH` Sets the full path for logging.
|
Example: |
`ROCBLAS_LOG_TRACE_PATH` Specifies the full path for trace logging. If this environment variable is set, the
`ROCBLAS_LOG_PATH` environment variable is ignored for trace logs. |
Example: |
`ROCBLAS_LOG_BENCH_PATH` Specifies the full path for bench logging. If this environment variable is set, the
`ROCBLAS_LOG_PATH` environment variable is ignored for bench logs. |
Example: |
`ROCBLAS_LOG_PROFILE_PATH` Specifies the full path for profile logging. If this environment variable is set, the
`ROCBLAS_LOG_PATH` environment variable is ignored for profile logs. |
Example: |
