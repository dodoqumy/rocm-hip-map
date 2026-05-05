---
title: "Using hipify-clang &#8212; HIPIFY Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIPIFY/en/latest/how-to/hipify-clang.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-03T03:10:35.395406+00:00
content_hash: "177102b15a7c6943"
---

# Using hipify-clang[#](#using-hipify-clang)

`hipify-clang`

is a Clang-based tool for translating NVIDIA CUDA sources into HIP sources.

It translates CUDA source into an Abstract Syntax Tree (AST), which is traversed by transformation matchers. After applying all the matchers, the output HIP source is produced.

**Advantages:**

`hipify-clang`

is a translator. It parses complex constructs successfully or reports an error.It supports Clang options such as

[-I](https://clang.llvm.org/docs/ClangCommandLineReference.html#include-path-management),[-D](https://clang.llvm.org/docs/ClangCommandLineReference.html#preprocessor-options), and[–cuda-path](https://clang.llvm.org/docs/ClangCommandLineReference.html#cmdoption-clang-cuda-path).The support for new CUDA versions is seamless, as the Clang front-end is statically linked into

`hipify-clang`

and does all the syntactical parsing of a CUDA source to HIPIFY.It is very well supported as a compiler extension.


**Disadvantages:**

You must ensure that the input CUDA code is correct as incorrect code can’t be translated to HIP.

You must install CUDA, and in case of multiple installations specify the needed version using

`--cuda-path`

option.You must provide all the

`includes`

and`defines`

to successfully translate the code.

## Release Dependencies[#](#release-dependencies)

`hipify-clang`

requires:

[CUDA](https://developer.nvidia.com/cuda-downloads), the latest supported version is[12.9.1](https://developer.nvidia.com/cuda-12-9-1-download-archive), but requires at least version[7.0](https://developer.nvidia.com/cuda-toolkit-70).[LLVM+Clang](http://releases.llvm.org)version is determined at least partially by the CUDA version you are using, as shown in the table below. The recommended Clang release is the latest stable release[21.1.6](https://github.com/llvm/llvm-project/releases/tag/llvmorg-21.1.6), or at least version[4.0.0](http://releases.llvm.org/download.html#4.0.0).

CUDA version |
supported LLVM release versions |
Windows |
Linux |
✅ |
✅ |
||
|
✅ |
✅ |
|
|
✅ |
✅ |
|
|
✅ |
✅ |
|
✅ |
✅ |
||
|
✅ |
✅ |
|
Works only with patch due to Clang bug |
✅ |
||
✅ |
✅ |
||
✅ |
✅ |
||
Works only with patch due to Clang bug |
Works only with patch due to Clang bug |
||
✅ |
✅ |
||
Works only with patch due to Clang bug |
Works only with patch due to Clang bug |
||
✅ |
✅ |
||
✅ |
✅ |
||
Works only with patch due to Clang bug |
✅ |
||
Works only with patch due to Clang bug |
❌ due to Clang bug |
||
✅ |
✅ |
||
✅ |
✅ |
||
✅ |
✅ |

1 Represents the latest supported and recommended configuration.

2 Download the patch and unpack it into your `LLVM distributive directory`

. This overwrites a few header files. You don’t need to rebuild `LLVM`

.

3 Download the patch and unpack it into your `LLVM source directory`

. This overwrites the `Cuda.cpp`

file. You need to rebuild `LLVM`

.

4 `LLVM 3.x`

is no longer supported (but might still work).

In most cases, you can get a suitable version of `LLVM+Clang`

with your package manager. However, you can also
[download a release archive](http://releases.llvm.org/) and build or install it. In case of multiple versions of `LLVM`

installed, set
[CMAKE_PREFIX_PATH](https://cmake.org/cmake/help/latest/variable/CMAKE_PREFIX_PATH.html) so that
`CMake`

can find the desired version of `LLVM`

. For example, `-DCMAKE_PREFIX_PATH=D:\LLVM\21.1.6\dist`

.

## Usage[#](#usage)

Note

For additional details on the following `hipify-clang`

command options, see [hipify-clang commands](../reference/hipify-clang-cmd.html#hipify-clang-cmd)

To process a file, `hipify-clang`

needs access to the same headers that are required to compile it
with `Clang`

:

```
square.cu --cuda-path=/usr/local/cuda-12.9 -I /usr/local/cuda-12.9/samples/common/inc
```

`hipify-clang`

arguments are supplied first, followed by a separator `--`

and the arguments to be
passed to Clang for compiling the input file:

```
cpp17.cu --cuda-path=/usr/local/cuda-12.9 -- -std=c++17
```

`hipify-clang`

also supports the hipification of multiple files that can be specified in a single
command with absolute or relative paths:

```
cpp17.cu ../../square.cu /home/user/cuda/intro.cu --cuda-path=/usr/local/cuda-12.9 -- -std=c++17
```

To use a specific version of LLVM during hipification, specify the `hipify-clang`

option
`--clang-resource-directory=`

to point to the Clang resource directory, which is the
parent directory for the `include`

folder that contains `__clang_cuda_runtime_wrapper.h`

and other
header files used during the hipification process:

```
square.cu --cuda-path=/usr/local/cuda-12.9 --clang-resource-directory=/usr/llvm/21.1.6/dist/lib/clang/21
```

For more information, refer to the [Clang manual for compiling CUDA](https://llvm.org/docs/CompileCudaWithLLVM.html#compiling-cuda-code).

## Using JSON compilation database[#](#using-json-compilation-database)

For some hipification automation (starting from Clang 8.0.0), you can provide a
[Compilation Database in JSON format](https://clang.llvm.org/docs/JSONCompilationDatabase.html)
in the `compile_commands.json`

file:

```
<folder containing compile_commands.json>
- or -
-p=<folder containing compile_commands.json>
```

You can provide the compilation database in the `compile_commands.json`

file or generate using
Clang based on CMake. You can specify multiple source files as well.

To provide Clang options, use `compile_commands.json`

file, whereas to provide `hipify-clang`

options, use the `hipify-clang`

command line.

Note

Don’t use the options separator `--`

to avoid compilation error caused due to the `hipify-clang`

options being
provided before the separator.

Here’s an
[example](https://github.com/ROCm/HIPIFY/blob/amd-staging/tests/unit_tests/compilation_database/compilation_database_before_13000/compile_commands.json.in)
demonstrating the `compile_commands.json`

usage:

```
[
{
"directory": "<test dir>",
"command": "hipify-clang \"<CUDA dir>\" -I./include -v",
"file": "cd_intro.cu"
}
]
```

## Hipification statistics[#](#hipification-statistics)

The options `--print-stats`

and `--print-stats-csv`

provide an overview of what is hipified and what is not, as well as the hipification statistics. Use the `--print-stats`

command to return the statistics as text to the terminal, or the `--print-stats-csv`

command to create a CSV file to open in a spreadsheet.

Note

When multiple source files are specified on the command-line, the statistics are provided per file and in total.

### Print statistics[#](#print-statistics)

```
hipify-clang intro.cu -cuda-path="C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v12.9" --print-stats
```

```
[HIPIFY] info: file 'intro.cu' statistics:
CONVERTED refs count: 40
UNCONVERTED refs count: 0
CONVERSION %: 100.0
REPLACED bytes: 604
[HIPIFY] info: file 'intro.cu' statistics:
CONVERTED refs count: 40
UNCONVERTED refs count: 0
CONVERSION %: 100.0
REPLACED bytes: 604
TOTAL bytes: 5794
CHANGED lines of code: 34
TOTAL lines of code: 174
CODE CHANGED (in bytes) %: 10.4
CODE CHANGED (in lines) %: 19.5
TIME ELAPSED s: 0.41
[HIPIFY] info: CONVERTED refs by type:
error: 2
device: 2
memory: 16
event: 9
thread: 1
include_cuda_main_header: 1
type: 2
numeric_literal: 7
[HIPIFY] info: CONVERTED refs by API:
CUDA Driver API: 1
CUDA RT API: 39
[HIPIFY] info: CONVERTED refs by names:
cuda.h: 1
cudaDeviceReset: 1
cudaError_t: 1
cudaEventCreate: 2
cudaEventElapsedTime: 1
cudaEventRecord: 3
cudaEventSynchronize: 3
cudaEvent_t: 1
cudaFree: 4
cudaFreeHost: 3
cudaGetDeviceCount: 1
cudaGetErrorString: 1
cudaGetLastError: 1
cudaMalloc: 3
cudaMemcpy: 6
cudaMemcpyDeviceToHost: 3
cudaMemcpyHostToDevice: 3
cudaSuccess: 1
cudaThreadSynchronize: 1
```

### Print CSV statistics[#](#print-csv-statistics)

```
hipify-clang intro.cu -cuda-path="C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v12.9" --print-stats-csv
```

This generates `intro.cu.csv`

file with statistics:
