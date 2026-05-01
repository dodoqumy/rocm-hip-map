---
title: "Installing and building rocWMMA &#8212; rocWMMA 2.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocWMMA/en/latest/install/installation.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:18:59.778080+00:00
content_hash: "383d9b9ee667546c"
---

# Installing and building rocWMMA[#](#installing-and-building-rocwmma)

This topic provides instructions for installing and configuring the rocWMMA library. The quickest way to install rocWMMA is to use the prebuilt packages that are released with ROCm. Alternatively, there are instructions to build the component from the source code.

The available ROCm packages are:

rocwmma-dev (source files for development)

rocwmma-samples (sample executables)

rocwmma-samples-dbgsym (sample executables with debug symbols)

rocwmma-tests (test executables)

rocwmma-tests-dbgsym (test executables with debug symbols)

rocwmma-clients (samples, tests, and benchmarks executables)


## Prerequisites[#](#prerequisites)

rocWMMA requires the following prerequisites:

A ROCm-enabled platform, using ROCm version 6.4 or later. For more information, see

[ROCm installation](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/index.html).[rocBLAS](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/index.html)version 4.3.0 for ROCm version 6.3 or later. (Optional: only required if rocWMMA is configured to use rocBLAS for validation. See below for more information.)

## Installing prebuilt packages[#](#installing-prebuilt-packages)

To install rocWMMA on Ubuntu or Debian, use these commands:

```
apt-get update
sudo apt-get install rocwmma-dev rocwmma-samples rocwmma-tests
```

To install rocWMMA on RHEL-based platforms, use:

```
yum update
sudo yum install rocwmma-dev rocwmma-samples rocwmma-tests
```

To install rocWMMA on SLES, use:

```
dnf upgrade
sudo dnf install rocwmma-dev rocwmma-samples rocwmma-tests
```

After rocWMMA is installed, it can be used just like any other library with a C++ API.

Note

The prebuilt package client executables support the gfx908, gfx90a, gfx942, gfx950, gfx1100, gfx1101, gfx1102, gfx1200, and gfx1201 targets.

After rocWMMA is installed, you can find the `rocwmma.hpp`

header file in the `/opt/rocm/include/rocwmma`

directory.
To make calls into rocWMMA, ensure you only include the `rocwmma.hpp`

, `rocwmma_coop.hpp`

, and `rocwmma_transforms.hpp`

files in the user code.
Don’t directly include any other rocWMMA files from `/opt/rocm/include/internal`

.

## Building and installing rocWMMA from source[#](#building-and-installing-rocwmma-from-source)

It isn’t necessary to build rocWMMA from source because it’s ready to use after installing the prebuilt packages, as described above. To build rocWMMA from source, follow the instructions in this section.

### System requirements[#](#system-requirements)

8GB of system memory is required for a full rocWMMA build. This value might be lower if rocWMMA is built without tests.

### GPU support[#](#gpu-support)

rocWMMA is supported on the following GPUs.

AMD CDNA class GPUs featuring matrix core support, including the gfx908, gfx90a, gfx942, and gfx950 GPUs (collectively labeled as gfx9).

Note

Double precision

`FP64`

data type support requires the gfx90a, gfx942, or gfx950.`F8`

and`BF8`

data type support requires the gfx942 or gfx950.AMD RDNA class GPUs featuring AI acceleration support, including the gfx1100, gfx1101, and gfx1102 (collectively known as gfx11), and the gfx1200 and gfx1201 (collectively known as gfx12).

Note

`F8`

and`BF8`

data type support requires the gfx1200 or gfx1201.

### Dependencies[#](#dependencies)

rocWMMA is designed to have minimal external dependencies so it’s lightweight and portable. The following dependencies are required:

[ROCm](https://github.com/ROCm/ROCm)(Version 6.4 or later)[CMake](https://cmake.org/)(Version 3.14 or later)[rocm-cmake](https://github.com/ROCm/rocm-cmake)(Version 0.8.0 or later)[HIP runtime](https://github.com/ROCm/rocm-systems/tree/develop/projects/hip)(Version 6.4.0 or later) (Or the ROCm hip-runtime-amd package)[LLVM OpenMP](https://openmp.llvm.org/)runtime dev package (Version 10.0 or later) (Also available as the ROCm rocm-llvm-dev package)(Optional, only required to use rocBLAS for validation)

[rocBLAS](https://github.com/ROCm/rocm-libraries/tree/develop/projects/rocblas)(Version 4.3.0 for ROCm 6.3 or later) (Or the ROCm rocblas and rocblas-dev packages).

Note

It’s best to use ROCm packages from the same release where applicable.

### Downloading rocWMMA[#](#downloading-rocwmma)

The rocWMMA source code is available from the [rocWMMA GitHub](https://github.com/ROCm/rocm-libraries/tree/develop/projects/rocwmma).
ROCm version 6.4 or later is required.

To verify the ROCm version installed on an Ubuntu system, use this command:

```
show rocm-libs -a
```

On a RHEL-based system, use:

```
info rocm-libs
```

The ROCm version has major, minor, and patch fields, possibly followed by a build-specific identifier.
For example, a ROCm version of `6.0.0.40000-23`

corresponds to major release = `6`

, minor release = `0`

,
patch = `0`

, and build identifier `40000-23`

.
The rocWMMA GitHub repository has branches with names like `rocm-major.minor.x`

,
where `major`

and `minor`

are the same as for the ROCm version.
To download rocWMMA on ROCm version `x.y`

, use this command:

```
clone -b release/rocm-rel-x.y https://github.com/ROCm/rocm-libraries.git
cd projects/rocwmma
```

Alternatively, you can use `sparse-checkout`

to clone only the rocWMMA project from the `rocm-libraries`

monorepo. For more information, see [Contributing to the ROCm Libraries](https://github.com/ROCm/rocm-libraries/blob/develop/CONTRIBUTING.md#option-b-clone-the-monorepo-with-sparse-checkout).

```
clone -b release/rocm-rel-x.y https://github.com/ROCm/rocWMMA.git
cd rocWMMA
```

Replace `x.y`

in the above command with the version of ROCm installed on your machine.
For example, if you have ROCm 6.0 installed, then replace `release/rocm-rel-x.y`

with `release/rocm-rel-6.0`

.

### Build configuration[#](#build-configuration)

You can choose to build any of the following combinations:

The rocWMMA library only

The library and samples

The library and tests (validation and benchmarks)

The library, samples, tests, and (optionally) assembly


rocWMMA is a header library, so you only need the header includes to call rocWMMA from your code. The client contains the tests, samples, and benchmark code.

Here are the available options to build the rocWMMA library, with or without clients.

|
|
|
|
Build code for specific GPU target(s) |
|
|
Build the tests |
|
|
Build the samples |
|
|
Generate assembly files |
|
|
Build validation tests |
|
|
Build benchmark tests |
|
|
Build extended testing coverage |
|
|
Use rocBLAS for validation tests |
|
|
Include rocBLAS benchmarking data |
|
|
Use the system GoogleTest library instead of downloading and building it |
|

#### Building the library alone[#](#building-the-library-alone)

By default, the project is configured in Release mode.

To build the library alone, run this command:

```
CC=/opt/rocm/bin/amdclang CXX=/opt/rocm/bin/amdclang++ cmake -B <build_dir> . -DROCWMMA_BUILD_TESTS=OFF -DROCWMMA_BUILD_SAMPLES=OFF
```

Here are some other example project configurations:

Configuration |
Command |
|---|---|
Basic |
|
Targeting gfx908 |
|
Debug build |
|
Build without rocBLAS (default |
|

After configuration, build the library using this command:

```
--build <build_dir> -- -j<nproc>
```

Note

It’s recommended to use a minimum of 16 threads to build rocWMMA with any tests, for example, using `-j16`

.

#### Building the library and samples[#](#building-the-library-and-samples)

To build the library and samples, run the following command:

```
CC=/opt/rocm/bin/amdclang CXX=/opt/rocm/bin/amdclang++ cmake -B <build_dir> . -DROCWMMA_BUILD_TESTS=OFF -DROCWMMA_BUILD_SAMPLES=ON
```

After configuration, build using this command:

```
--build <build_dir> -- -j<nproc>
```

The samples folder in `<build_dir>`

contains the executables in the table below.

Executable name |
Description |
|---|---|
|
A simple GEMM operation [D = alpha * (A x B) + beta * C] using the rocWMMA API for single-precision floating point types |
|
A simple GEMM operation [D = alpha * (A x B) + beta * C] using the rocWMMA API for double-precision floating point types |
|
A simple GEMM operation [D = alpha * (A x B) + beta * C] using the rocWMMA API for half-precision floating point types |
|
An optimized GEMM operation [D = alpha * (A x B) + beta * C] using the rocWMMA API for single-precision floating point types |
|
An optimized GEMM operation [D = alpha * (A x B) + beta * C] using the rocWMMA API for double-precision floating point types |
|
An optimized GEMM operation [D = alpha * (A x B) + beta * C] using the rocWMMA API for half-precision floating point types |
|
A simple GEMV operation [y = alpha * (A) * x + beta * y] using the rocWMMA API for single-precision floating point types |
|
A simple GEMV operation [y = alpha * (A) * x + beta * y] using the rocWMMA API for double-precision floating point types |
|
A simple DLRM operation using the rocWMMA API |
|
A simple GEMM operation [D = alpha * (A x B) + beta * C] demonstrating runtime compilation (hipRTC) compatibility |

#### Building the library and tests[#](#building-the-library-and-tests)

rocWMMA provides the following test suites:

**DLRM tests**: Cover the dot product interactions between embeddings used in the Deep Learning Recommendation Model (DLRM) implemented with rocWMMA.**GEMM tests**: Cover block-wise Generalized Matrix Multiplication (GEMM) implemented with rocWMMA.**Unit tests**: Cover various aspects of the rocWMMA API and internal functionality.

rocWMMA can build both validation and benchmark tests. Validation tests verify the rocWMMA
implementations against a reference model, providing a `PASS`

or `FAIL`

result. Benchmark tests invoke the tests multiple times. They return
the average compute throughput in teraflops/sec (TFLOPS/sec) and, in some cases, gauge the efficiency
as a percentage of the expected peak performance. The library uses
CPU or rocBLAS methods for validation, when available and benchmarks
comparisons based on the selected project configurations provided.
By default, the project is linked with rocBLAS to validate results more efficiently.

To build the library and tests, run this command:

```
CC=/opt/rocm/bin/amdclang CXX=/opt/rocm/bin/amdclang++ cmake -B <build_dir> . -DROCWMMA_BUILD_TESTS=ON
```

After configuration, build using this command:

```
--build <build_dir> -- -j<nproc>
```

The tests in `<build_dir>`

contain executables, as shown in the table below.

Executable name |
Description |
|---|---|
|
A DLRM implementation using the rocWMMA API |
|
A DLRM implementation using the rocWMMA API with LDS shared memory |
|
A simple GEMM operation [D = alpha * (A x B) + beta * C] using the rocWMMA API |
|
A modified GEMM operation where each wave targets a sub-grid of output blocks using the rocWMMA API |
|
A modified GEMM operation where each wave targets a sub-grid of output blocks using LDS memory, the rocWMMA API, and block-level collaboration |
|
A modified GEMM operation where each wave targets a sub-grid of output blocks using LDS memory, the rocWMMA API, and wave-level collaboration |
|
A modified GEMM operation where each wave targets a sub-grid of output blocks using LDS memory, the rocWMMA API, and workgroup-level collaboration |
|
An adhoc version of |
|
An adhoc version of |
|
An adhoc version of |
|
An adhoc version of |
|
An adhoc version of |
|
Tests against contamination of pristine data for loads and stores |
|
Tests the cross-lane vector operations |
|
Tests the |
|
Tests input and output shape meta data |
|
Tests input and output logistical meta data |
|
Tests the accuracy of internal matrix layout patterns |
|
Tests the accuracy of internal matrix layout traits |
|
Tests the |
|
Tests the |
|
Tests the mapping utilities used in rocWMMA implementations |
|
Tests the vector packing utilities used in rocWMMA implementations |
|
Tests the transform utilities used in rocWMMA implementations |
|
Tests the additional transform utilities used in rocWMMA implementations |
|
Tests the vector unpacking utilities used in rocWMMA implementations |
|
Tests the internal vector storage iteration implementation |
|
Tests the internal vector storage implementation |
|
Tests the internal vector manipulation utilities implementation |

Note

*= validate: Executables that compare outputs for correctness against reference sources such as CPU or rocBLAS calculations.

*= bench: Executables that measure kernel execution speeds, which might be compared against the rocBLAS references.

#### Build the library, tests, and assembly[#](#build-the-library-tests-and-assembly)

To build the library and tests with assembly code generation, run the following command:

```
CC=/opt/rocm/bin/amdclang CXX=/opt/rocm/bin/amdclang++ cmake -B <build_dir> . -DROCWMMA_BUILD_ASSEMBLY=ON -DROCWMMA_BUILD_TESTS=ON
```

After configuration, build using this command:

```
--build <build_dir> -- -j<nproc>
```

Note

The `assembly`

folder within the `<build_dir>`

contains a hierarchy of assembly files
generated by the executables in the format `test_executable_name.s`

.
These files can be viewed in a text editor.

#### Make targets list[#](#make-targets-list)

When building rocWMMA during the `make`

step,
you can specify the Make targets instead of defaulting to `make all`

.
The following table highlights the relationships between high-level grouped targets and individual targets.

Group target |
Individual targets |
|---|---|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|

### Build performance[#](#build-performance)

Depending on the resources available to the build machine and the selected build configuration, rocWMMA build times can take an hour or more. Here are some things you can do to reduce build times:

Target a specific GPU, for instance, with

`-D GPU_TARGETS=gfx908:xnack-`

.Use a large number of threads, for instance,

`-j32`

.Select

`ROCWMMA_BUILD_ASSEMBLY=OFF`

.Select

`ROCWMMA_BUILD_DOCS=OFF`

.Select

`ROCWMMA_BUILD_EXTENDED_TESTS=OFF`

.Specify one of

`ROCWMMA_BUILD_VALIDATION_TESTS`

or`ROCWMMA_BUILD_BENCHMARK_TESTS`

as`ON`

and the other as`OFF`

instead of building both.During the

`make`

command, build a specific target, for instance,`rocwmma_gemm_tests`

.

### Test runtimes[#](#test-runtimes)

Depending on the resources available to the machine running the selected tests, rocWMMA test runtimes can last an hour or more. Here are some things you can do to reduce test runtimes:

CTest runs the entire test suite, but you can invoke tests individually by name.

Use GoogleTest filters to target specific test cases:

--gtest_filter=\*name_filter\*

Use ad hoc tests to focus on a specific set of parameters.

Manually adjust the test case coverage.


### Test verbosity and output redirection[#](#test-verbosity-and-output-redirection)

GEMM tests support logging arguments to control verbosity and output redirection.

```
--output_stream "output.csv" --omit 1
```

Compact |
Verbose |
Description |
|---|---|---|
|
|
redirect GEMM testing output to CSV file |
|
code = 1: Omit gtest SKIPPED tests |
|
code = 2: Omit gtest FAILED tests |
||
code = 4: Omit gtest PASSED tests |
||
code = 8: Omit all gtest output |
||
code = <N>: OR’d combination of 1, 2, 4 |
