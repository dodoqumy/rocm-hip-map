---
title: "rocSOLVER client applications &#8212; rocSOLVER 3.32.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocSOLVER/en/latest/howto/clients.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:10:45.710050+00:00
content_hash: "43a532d9c8356d9c"
---

# rocSOLVER client applications[#](#rocsolver-client-applications)

rocSOLVER provides infrastructure for testing and benchmarking similar to the
[rocBLAS utilities](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/Programmers_Guide.html#rocblas-benchmarking-and-testing),
as well as sample code illustrating basic use of the library.

Client binaries are not built by default. They require specific flags to be passed to the install script
or CMake system. If the `-c`

flag is passed to `install.sh`

, the client binaries can be found in the
`<rocsolverDIR>/build/release/clients/staging`

directory. If both the `-c`

and `-g`

flags are passed to
`install.sh`

, the client binaries can be found in `<rocsolverDIR>/build/debug/clients/staging`

.
If you pass any combination of the `-DBUILD_CLIENTS_TESTS=ON`

, `-DBUILD_CLIENTS_BENCHMARKS=ON`

, or
`-DBUILD_CLIENTS_SAMPLES=ON`

flags to the CMake system, the relevant client binaries can normally
be found in the `<rocsolverDIR>/build/clients/staging`

directory. See the [Installation guide](../installation/installlinux.html)
for more information on building the library and its clients.

## Testing rocSOLVER[#](#testing-rocsolver)

The `rocsolver-test`

client executes a [GoogleTest](https://github.com/google/googletest) (gtest) suite to
verify the correct functioning of the library. The results computed by rocSOLVER on random input data
are normally compared with the results computed by [NETLib LAPACK](https://www.netlib.org/lapack/) on the CPU or tested implicitly
in the context of the solved problem. This client is built if the `-c`

flag is passed to `install.sh`

or if the `-DBUILD_CLIENTS_TESTS=ON`

flag is
passed to the CMake system.

Call the rocSOLVER test client with the `--help`

flag to get information on the different flags that control the test behavior.

```
--help
```

One of the most useful flags is the `--gtest_filter`

flag, which lets you choose which tests to run
from the suite. For example, the following command only runs the tests for `geqrf`

:

```
--gtest_filter=*GEQRF*
```

The rocSOLVER tests are divided into two separate groups: `checkin_lapack`

and `daily_lapack`

.
Tests in the `checkin_lapack`

group are small and quick to execute. They verify basic correctness and error
handling. Tests in the `daily_lapack`

group are large and slow to execute. They verify the correctness of
large problem sizes. You can run one test group or the other using `--gtest_filter`

, for example:

```
--gtest_filter=*checkin_lapack*
./rocsolver-test --gtest_filter=*daily_lapack*
```

## Benchmarking rocSOLVER[#](#benchmarking-rocsolver)

The `rocsolver-bench`

client runs any rocSOLVER function with random data of the specified dimensions. It compares basic
performance information, such as execution times, between [NETLib LAPACK](https://www.netlib.org/lapack/) on the
CPU and rocSOLVER on the GPU. The client is built if the `-c`

flag is passed to `install.sh`

or if the
`-DBUILD_CLIENTS_BENCHMARKS=ON`

flag is passed to the CMake system.

Call the rocSOLVER bench client with the `--help`

flag to obtain information on the different parameters and flags that control the behavior of the benchmark client.

```
--help
```

Two of the most important flags for `rocsolver-bench`

are the `-f`

and `-r`

flags. The `-f`

(or
`--function`

) flag lets you select which function to benchmark. The `-r`

(or `--precision`

)
flag lets you select the data precision for the function. It can be one of `s`

(single precision),
`d`

(double precision), `c`

(single precision complex), or `z`

(double precision complex).

The non-pointer arguments for a function can be passed to `rocsolver-bench`

by using the argument name as
a flag. See the [Reference](../reference/intro.html) sections for more information on the function arguments and
names. For example, the function `rocsolver_dgeqrf_strided_batched`

has the following method signature:

```
rocblas_status
rocsolver_dgeqrf_strided_batched(rocblas_handle handle,
const rocblas_int m,
const rocblas_int n,
double* A,
const rocblas_int lda,
const rocblas_stride strideA,
double* ipiv,
const rocblas_stride strideP,
const rocblas_int batch_count);
```

A call to `rocsolver-bench`

to run this function on a batch of one hundred 30x30 matrices might look like this:

```
-f geqrf_strided_batched -r d -m 30 -n 30 --lda 30 --strideA 900 --strideP 30 --batch_count 100
```

`rocsolver-bench`

generally attempts to provide or calculate a suitable default value for these arguments,
although you must always specify at least one size argument. Functions that take `m`

and `n`

as arguments
typically require that `m`

be provided and assume a square matrix. For example, the previous command is
equivalent to:

```
-f geqrf_strided_batched -r d -m 30 --batch_count 100
```

Other useful benchmarking options include:

`--perf`

: Disables the LAPACK computation and only times and prints the rocSOLVER performance result.`-i`

: (or`--iters`

) Specifies the number of times to run the GPU timing loop. The performance result is the average of all runs.`--profile`

: Enables[profile logging](logging.html#log-profile), indicating the maximum depth of the nested output.

```
-f geqrf_strided_batched -r d -m 30 --batch_count 100 --perf 1
./rocsolver-bench -f geqrf_strided_batched -r d -m 30 --batch_count 100 --iters 20
./rocsolver-bench -f geqrf_strided_batched -r d -m 30 --batch_count 100 --profile 5
```

In addition to the benchmarking functionality, the rocSOLVER bench client can also provide the norm of the error in the
computations when the `-v`

(or `--verify`

) flag is used. If the
`--mem_query`

flag is passed, it returns the amount of device memory required for the workspace by the specified function.

```
-f geqrf_strided_batched -r d -m 30 --batch_count 100 --verify 1
./rocsolver-bench -f geqrf_strided_batched -r d -m 30 --batch_count 100 --mem_query 1
```

## rocSOLVER sample code[#](#rocsolver-sample-code)

The rocSOLVER sample programs provide examples of how to work with the rocSOLVER library. They are
built if the `-c`

flag is passed to `install.sh`

or if the `-DBUILD_CLIENTS_SAMPLES=ON`

flag is passed to the
CMake system.

Currently, sample code is available to demonstrate the following:

Basic use of rocSOLVER in C and C++ using

[rocsolver_geqrf](../reference/lapack.html#geqrf)as an exampleUse of batched and strided_batched functions using

[rocsolver_geqrf_batched](../reference/lapack.html#geqrf-batched)and[rocsolver_geqrf_strided_batched](../reference/lapack.html#geqrf-strided-batched)as examplesUse of rocSOLVER with the Heterogeneous Memory Management (HMM) model

Use of the rocSOLVER

[multi-level logging](logging.html#logging-label)functionality
