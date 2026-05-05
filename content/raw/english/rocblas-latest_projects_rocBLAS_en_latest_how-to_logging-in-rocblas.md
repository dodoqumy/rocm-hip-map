---
title: "rocBLAS logging &#8212; rocBLAS 5.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocBLAS/en/latest/how-to/logging-in-rocblas.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:05:21.299397+00:00
content_hash: "c0a0d3cd0bbb3ca6"
---

# rocBLAS logging[#](#rocblas-logging)

You can set five environment variables to control logging:

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

Caution

Performance will degrade when logging is enabled.

See the `rocblas_layer_mode`

enumeration for these values as constants.

Trace logging outputs a line each time a rocBLAS function is called. The line contains the function name and the values of arguments.

Bench logging outputs a line each time a rocBLAS function is called. The
line can be used with the executable `rocblas-bench`

to call the
function with the same arguments.

Profile logging, at the end of program execution, outputs a YAML
description of each rocBLAS function called, the values of its
performance-critical arguments, and the number of times it was called
with those arguments (the `call_count`

). Some arguments, such as
`alpha`

and `beta`

in GEMM, are recorded with a value representing
the category that the argument falls into, such as `-1`

, `0`

, `1`

,
or `2`

. The number of categories and the values representing them
might change over time, depending on how many categories are needed to
adequately represent all the values that can affect the performance
of the function.

Internal API logging outputs information like the GEMM backend used for a particular GEMM call. Not all internal APIs are logged. The log output goes to the same stream as trace logging.

The default stream for logging output is standard error. [Four
environment variables](#rocblas-logging-env) can set the full path name for a
log file.

For example, in a Bash shell, use the following to output bench logging to the file
`bench_logging.txt`

in your present working directory:

```
export ROCBLAS_LOG_BENCH_PATH=$PWD/bench_logging.txt
```

A full path is required, not a relative path. In the command above,
`$PWD`

expands to the full path of your present working directory.
If the paths are not set, then the logging output is streamed to standard error.

When profile logging is enabled, memory usage increases. If the program exits abnormally, it is possible that profile logging will not sent to the output before the program exits.

## GEMM backend logging[#](#gemm-backend-logging)

To generate additional logging to analyze non-success return codes, you can enable verbose error messages for the two backend systems used to perform GEMMs.

```
export ROCBLAS_VERBOSE_TENSILE_ERROR=1
export ROCBLAS_VERBOSE_HIPBLASLT_ERROR=1
```

These can be used in conjunction with `ROCBLAS_LAYER=8`

for a better understanding of an error,
or even with a success status to understand why a backend was not used.

## rocTX support in rocBLAS[#](#roctx-support-in-rocblas)

The [rocTX](https://rocm.docs.amd.com/projects/roctracer/en/latest/reference/roctx-spec.html) library contains application code
instrumentation APIs to support high-level correlation of runtime API or activity events.
When integrated with rocBLAS, rocTX enables users to capture detailed logs, like `ROCBLAS_TRACE`

or `ROCBLAS_BENCH`

, and view
them in profiling tools such as rocProf,
offering better insights into runtime behavior and performance bottlenecks.

The following steps describe how to enable logging:

```
# To view trace logging
export ROCBLAS_LAYER=1
rocprof --hip-trace --roctx-trace ./rocblas-bench -f geam
# To view bench logging
export ROCBLAS_LAYER=2
rocprof --hip-trace --roctx-trace ./rocblas-bench -f geam
```

These settings activate the corresponding logging layers in rocBLAS, allowing users to capture either trace-level information (for function calls) or bench-level information (for benchmarking purposes) during profiling.

Note

rocTX support in rocBLAS is unavailable on Windows and is not supported in the static library version on Linux.
