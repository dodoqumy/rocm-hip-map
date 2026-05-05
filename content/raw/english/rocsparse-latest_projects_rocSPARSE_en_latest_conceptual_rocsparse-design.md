---
title: "rocSPARSE design notes &#8212; rocSPARSE 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocSPARSE/en/latest/conceptual/rocsparse-design.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:08:58.759966+00:00
content_hash: "2ad7dc4dab10e3dc"
---

# rocSPARSE design notes[#](#rocsparse-design-notes)

This topic is intended for advanced developers who want to understand, modify, or extend the functionality of the rocSPARSE library.

The rocSPARSE library is developed using the “Hourglass API” approach. This provides a thin C89 API which retains all the convenience of C++. As a side effect, this avoids API-related binary compatibility issues. This approach also allows rocSPARSE routines to be used by other programming languages.

In public API header files, rocSPARSE only relies on functions, pointers, forward declared structs, enumerations, and type definitions. rocSPARSE introduces multiple library and object handles by using opaque types to hide layout and implementation details from the user.

## Temporary device memory[#](#temporary-device-memory)

Many routines exposed by the rocSPARSE API require a temporary storage buffer on the device.
You are responsible for buffer allocation and deallocation.
The allocated buffers can be reused and do not need to be regularly freed and re-allocated for every single API call.
For this purpose, routines that require a temporary storage buffer offer a special API function
to query for the storage buffer size, for example, [ rocsparse_scsrsv_buffer_size()](../reference/level2.html#_CPPv428rocsparse_scsrsv_buffer_size16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoP6size_t).

## Library source code organization[#](#library-source-code-organization)

This section discusses the structure of the rocSPARSE library in the [rocSPARSE GitHub repository](https://github.com/ROCm/rocm-libraries/tree/develop/projects/rocsparse).

### The library/include directory[#](#the-library-include-directory)

The `library/include`

directory contains all files that are exposed to the user.
The rocSPARSE API is declared here.

File |
Description |
|---|---|
|
Includes all other API-related rocSPARSE header files. |
|
Declares all rocSPARSE auxiliary functions, such as handle and descriptor management. |
|
Defines the rocSPARSE complex data types |
|
Declares all rocSPARSE Sparse Linear Algebra Subroutines of types level 1, level 2, level 3, extra, preconditioner, format conversion, reordering, generic, and utility. This is achieved by including headers from the |
|
Defines all data types used by rocSPARSE. |
|
Provides the configured version and settings that are initially set by CMake during compilation. |

The `library/include/internal`

directory contains the public API for all rocSPARSE sparse linear algebra subroutines,
organized into `level1`

, `level2`

, `level3`

, `extra`

, `precond`

, `conversion`

, `reordering`

, `generic`

, and `utility`

directories.

### The library/src directory[#](#the-library-src-directory)

This directory contains all rocSPARSE library source files.
The root of the `library/src/`

directory hosts the implementation of the library handle and auxiliary functions.
Each subdirectory is responsible for a specific class of sparse linear algebra subroutines.
The `library/src/include`

directory defines the following categories:

File |
Description |
|---|---|
|
Implementation of opaque handle structures. |
|
Implementation of auxiliary functions, for example, create and destroy handles. |
|
Implementation of the |
|
Commonly used functions among several rocSPARSE routines. See |
|
Definition of status-flag macros. See |
|
Declaration of opaque handle structures. |
|
Implementation of the different rocSPARSE logging helper functions. |
|
Declaration of the |
|
Implementation of the different rocSPARSE logging functions. |

### The clients directory[#](#the-clients-directory)

The `clients`

directory contains all clients, for example, samples, unit tests, and benchmarks.
For more details, see [Clients](#rocsparse-clients).

### Sparse linear algebra subroutines[#](#sparse-linear-algebra-subroutines)

Each sparse linear algebra subroutine is implemented in a set of source files in the
corresponding directory: `rocsparse_<subroutine>.cpp`

, `rocsparse_<subroutine>.hpp`

, and `<subroutine>_device.h`

,
where `<subroutine>`

indicates any of the rocSPARSE library functions.

`rocsparse_<subroutine>.cpp`

implements the C wrapper and API functionality for each supported precision.
`rocsparse_<subroutine>.hpp`

implements the API functionality, using the precision as template parameter.
Finally, `<subroutine>_device.h`

implements the device code required for the computation of the subroutine.

Note

Each subroutine exposed in the API is expected to return a [ rocsparse_status](../reference/enumerations.html#_CPPv416rocsparse_status).
Additionally, each device function is expected to use a specified stream which is accessible through the libraries handle.

The following code block contains a sample for `rocsparse_<subroutine>.cpp`

, `rocsparse_<subroutine>.hpp`

,
and `<subroutine>_device.h`

.

```
#include "rocsparse.h"
#include "rocsparse_subroutine.hpp"
/*
* ===========================
* C wrapper
* ===========================
*/
extern "C" rocsparse_status rocsparse_ssubroutine(rocsparse_handle handle,
rocsparse_int m,
const float* alpha,
float* val)
{
return rocsparse_subroutine_template(handle, m, alpha, val);
}
extern "C" rocsparse_status rocsparse_dsubroutine(rocsparse_handle handle,
rocsparse_int m,
const double* alpha,
double* val)
{
return rocsparse_subroutine_template(handle, m, alpha, val);
}
extern "C" rocsparse_status rocsparse_csubroutine(rocsparse_handle handle,
rocsparse_int m,
const rocsparse_float_complex* alpha,
rocsparse_float_complex* val)
{
return rocsparse_subroutine_template(handle, m, alpha, val);
}
extern "C" rocsparse_status rocsparse_zsubroutine(rocsparse_handle handle,
rocsparse_int m,
const rocsparse_double_complex* alpha,
rocsparse_double_complex* val)
{
return rocsparse_subroutine_template(handle, m, alpha, val);
}
```

```
#pragma once
#ifndef ROCSPARSE_SUBROUTINE_HPP
#define ROCSPARSE_SUBROUTINE_HPP
#include "definitions.h"
#include "handle.h"
#include "rocsparse.h"
#include "subroutine_device.h"
#include "utility.h"
#include <hip/hip_runtime.h>
template <typename T>
__global__ void subroutine_kernel_host_pointer(rocsparse_int m, T alpha, T* val)
{
subroutine_device(m, alpha, val);
}
template <typename T>
__global__ void subroutine_kernel_device_pointer(rocsparse_int m, const T* alpha, T* val)
{
subroutine_device(m, *alpha, val);
}
template <typename T>
rocsparse_status rocsparse_subroutine_template(rocsparse_handle handle,
rocsparse_int m,
const T* alpha,
T* val)
{
// Check for valid handle
if(handle == nullptr)
{
return rocsparse_status_invalid_handle;
}
// Check size
if(m < 0)
{
return rocsparse_status_invalid_size;
}
// Quick return if possible
if(m == 0)
{
return rocsparse_status_success;
}
// Check pointer arguments
if(alpha == nullptr || val == nullptr)
{
return rocsparse_status_invalid_pointer;
}
// Differentiate between the pointer modes
if(handle->pointer_mode == rocsparse_pointer_mode_device)
{
// Launch kernel
hipLaunchKernelGGL((subroutine_kernel_device_pointer<T>),
dim3(...),
dim3(...),
0,
handle->stream,
m,
alpha,
val);
}
else
{
// Launch kernel
hipLaunchKernelGGL((subroutine_kernel_host_pointer<T>),
dim3(...),
dim3(...),
0,
handle->stream,
m,
*alpha,
val);
}
return rocsparse_status_success;
}
#endif // ROCSPARSE_SUBROUTINE_HPP
```

```
#pragma once
#ifndef SUBROUTINE_DEVICE_H
#define SUBROUTINE_DEVICE_H
#include <hip/hip_runtime.h>
template <typename T>
__device__ void subroutine_device(rocsparse_int m, T alpha, T* val)
{
...
}
#endif // SUBROUTINE_DEVICE_H
```

## Important functions and data structures[#](#important-functions-and-data-structures)

This section describes the important rocSPARSE functions and data structures.

### Status-flag macros[#](#status-flag-macros)

The following table lists the status-flag macros available in rocSPARSE and their purpose.

Macro |
Description |
|---|---|
|
Returns if |
|
Throws an exception if |
|
Prints an error message if |
|
Returns if |

### The rocsparse_mat_info structure[#](#the-rocsparse-mat-info-structure)

The rocSPARSE [ rocsparse_mat_info](../reference/types.html#_CPPv418rocsparse_mat_info) structure contains all matrix meta information that is collected during the analysis routines.

The following table lists all the internal metadata structures:

Meta data structure |
Description |
|---|---|
|
Structure to hold analysis metadata for sparse matrix and vector multiplication in CSR format. |
|
Structure to hold analysis metadata for operations on sparse triangular matrices, for example, the dependency graph. |
|
Structure to hold analysis metadata for sparse matrix and sparse matrix multiplication in CSR format. |

#### Cross-Routine Data Sharing[#](#cross-routine-data-sharing)

Metadata that has already been collected, such as the dependency graph of a sparse matrix, can be shared among multiple routines.
For example, if the incomplete LU factorization of a sparse matrix is computed,
the gathered analysis data can be shared for subsequent lower triangular solves of the same matrix.
This behavior can be specified by the [rocsparse_analysis_policy](../reference/enumerations.html#rocsparse-analysis-policy) parameter.

The following table lists subroutines that can, in some cases, share metadata:

Subroutine |
Shares metadata with |
|---|---|

Note

This functionality can be further expanded on rocSPARSE extensions to significantly improve metadata collection performance.

## Clients[#](#clients)

rocSPARSE clients host a variety of different examples, as well as a unit test and benchmarking package.
For detailed instructions on how to build rocSPARSE with clients, see the [Linux Install](../install/Linux_Install_Guide.html)
or [Windows Install](../install/Windows_Install_Guide.html) guides.

### Samples[#](#samples)

The `clients/samples`

collection offers sample implementations of the rocSPARSE API.
The following table lists the available examples along with a description.

Sample |
Description |
|---|---|
|
Performs sparse matrix vector multiplication in COO format. |
|
Performs sparse matrix vector multiplication in CSR format. |
|
Performs sparse matrix vector multiplication in ELL format. |
|
Demonstrates rocSPARSE handle initialization and finalization. |
|
Performs sparse matrix vector multiplication in HYB format. |

### Unit tests[#](#unit-tests)

Multiple unit tests are available to test for bad arguments, invalid parameters, and sparse routine functionality.
The unit tests are based on [GoogleTest](https://github.com/google/googletest).
The tests cover all routines that are exposed by the API, including all available floating-point precision.

### Benchmarks[#](#benchmarks)

rocSPARSE offers a benchmarking tool that can be compiled with the clients package. The benchmark tool can perform time measurements for any routine exposed by the API. To set up a benchmark run, multiple options are available.

Command-line option |
Description |
|---|---|
|
Prints the help message |
|
Specify the |
|
Specify the |
|
Specify the |
|
Specify the |
|
Specify the |
|
Specify the |
|
Specify the |
|
Specify the |
|
Specify the |
|
Specify the |
|
Read from |
|
Read from |
|
Assemble a 2D/3D Laplacian matrix with dimensions |
|
Specify the scalar \(\alpha\). |
|
Specify the scalar \(\beta\). |
|
Specify whether matrix A is (conjugate) transposed or not. See |
|
Specify whether matrix B is (conjugate) transposed or not. See |
|
Specify the index base of matrix A. See |
|
Specify the index base of matrix B. See |
|
Specify the index base of matrix C. See |
|
Specify the index base of matrix D. See |
|
Specify whether the operation is performed symbolically or numerically. See |
|
Specify the HYB partitioning type. See |
|
Specify the diagonal type of a sparse matrix. See |
|
Specify the fill mode of a sparse matrix. See |
|
Specify the storage mode of a sparse matrix. See |
|
Specify the analysis policy. See |
|
Specify the API-exposed subroutine to benchmark. |
|
Index precision: integer 32 bit or integer 64 bit. |
|
Floating-point precision: single real, double real, single complex, or double complex. |
|
Specify whether the results should be validated with the host reference implementation. |
|
Iterations to run inside the timing loop. |
|
Set the device to be used for subsequent benchmark runs. |
|
Specify whether BSR blocks should be laid out in row-major storage or column-major storage. |
|
Specify whether a dense matrix is laid out in column-major or row-major storage. |
|
Specify whether a sparse matrix is laid out in coo, coo_aos, csr, csc, or ell format. |
|
Specify the leading dimension of a dense matrix. |
|
Specify the batch count for batched routines. |
|
Specify the batch count for batched routines. |
|
Specify the batch count for batched routines. |
|
Specify the batch count for batched routines. |
|
Specify the batch stride for batched routines. |
|
Specify the output filename for the memory report. |
|
Specify the algorithm to use when running SpMV. |
|
Specify the algorithm to use when running SpMM. |
|
Specify the algorithm to use when running the gtsv interleaved batch routine. |

For example, to benchmark the `csrmv`

routine using double precision, run the following command:

```
-f csrmv --precision d --alpha 1 --beta 0 --iters 1000 --rocalution <path to .csr matrix file>
```

### Python plotting scripts[#](#python-plotting-scripts)

rocSPARSE also contains some useful Python plotting scripts that work in conjunction with the `rocsparse-bench`

executable. To use these
plotting scripts to, for example, plot the performance of the csrmv routine with multiple matrices, first call:

```
-f csrmv --precision d --alpha 1 --beta 0 --iters 1000 --bench-x --rocalution /path/to/matrix/files/*.csr --bench-o name_of_output_file.json
```

This produces the JSON file `name_of_output_file.json`

, which contains all the performance data. This file can be passed to the Python plotting script
`rocSPARSE/scripts/rocsparse-bench-plot.py`

using the following command:

```
rocsparse-bench-plot.py /path/to/json/file/name_of_output_file.json
```

This generates pdf files that plot the following information:

GB/s

GFLOPS/s

milliseconds


Note

The parameter that follows the `--bench-x`

option for `rocsparse-bench`

specifies the values to use on the x-axis.
An earlier example passed `--bench-x --rocalution /path/to/matrix/files/*.csr`

, which means that each entry in the
x-axis of the generated plot is a matrix found in the directory `/path/to/matrix/files/`

.

rocSPARSE also provides plotting scripts that let you generate plots comparing two or more rocsparse-bench performance runs. For example, to compare the performance of csrmv with single precision and double precision, first run:

```
-f csrmv --precision s --alpha 1 --beta 0 --iters 1000 --bench-x --rocalution /path/to/matrix/files/*.csr --bench-o scsrmv_output_file.json
./rocsparse-bench -f csrmv --precision d --alpha 1 --beta 0 --iters 1000 --bench-x --rocalution /path/to/matrix/files/*.csr --bench-o dcsrmv_output_file.json
```

Doing this generates two JSON output files: `scsrmv_output_file.json`

and `dcsrmv_output_file.json`

. These files can then be
passed to the Python plotting script `rocSPARSE/scripts/rocsparse-bench-compare.py`

:

```
rocsparse-bench-compare.py /path/to/json/file/scsrmv_output_file.json /path/to/json/file/dcsrmv_output_file.json
```

This generates pdf files plotting the following comparisons between the two runs:

GB/s

GFLOPS/s

milliseconds

GB/s ratio

GFLOPS/s ratio


In both Python scripts, the y axis defaults to log scaling. To use linear scaling for the y axis, pass
the `--linear`

option to either of the Python plotting scripts. To see a full list of options, use the `-h`

or `--help`

option.

### Helper scripts for downloading matrices[#](#helper-scripts-for-downloading-matrices)

rocSPARSE contains some helper scripts for downloading matrices from the [sparse suite collection](http://sparse.tamu.edu/).
These matrices can be useful for additional testing and performance measurement. The scripts are found in the
`rocSPARSE/scripts/performance/matrices`

directory. To use these scripts to download matrices, run the following commands:










This downloads the matrices and converts them to .csr format so rocsparse-bench can use them when
the `--rocalution`

option is provided.
