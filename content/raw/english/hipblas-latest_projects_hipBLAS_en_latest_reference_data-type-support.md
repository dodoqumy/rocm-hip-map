---
title: "Data type support &#8212; hipBLAS 3.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipBLAS/en/latest/reference/data-type-support.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:19:08.127866+00:00
content_hash: "06ade43d48e90b43"
---

# Data type support[#](#data-type-support)

This topic lists the data type support for the hipBLAS library on AMD GPUs for
different levels of BLAS operations [Level 1](hipblas-api-functions.html#level-1),
[Level 2](hipblas-api-functions.html#level-2), and [Level 3](hipblas-api-functions.html#level-3).

The hipBLAS library functions are also available with ILP64 interfaces. With
these interfaces, all `int`

arguments are replaced by the type name
`int64_t`

. For more information on these `_64`

functions, see the
[ILP64 interfaces](hipblas-api-functions.html#ilp64-api) section.

The icons representing different levels of support are explained in the following table.

Icon |
Definition |
|---|---|
NA |
Not applicable |
❌ |
Not supported |
⚠️ |
Partial support |
✅ |
Full support |

For more information about data type support for the other ROCm libraries, see
[Data types and precision support page](https://rocm.docs.amd.com/en/latest/reference/precision-support.html).

## Custom types[#](#custom-types)

hipBlas defines the `hipblasBfloat16`

and uses the HIP types `hipComplex`

and `hipDoubleComplex`

.

### The bfloat 16 data type[#](#the-bfloat-16-data-type)

hipBLAS defines a `hipblasBfloat16`

data type. This type is exposed as a
struct containing 16 bits of data. There is also a C++ `hipblasBfloat16`

class
defined which provides slightly more functionality, including conversion to and
from a 32-bit float data type.
This class can be used in C++11 or newer by defining `HIPBLAS_BFLOAT16_CLASS`

before including the header file `<hipblas.h>`

.

There is also an option to interpret the API as using the `hip_bfloat16`

data
type. This is provided to avoid casting when using the `hip_bfloat16`

data
type. To expose the API using `hip_bfloat16`

, define
`HIPBLAS_USE_HIP_BFLOAT16`

before including the header file `<hipblas.h>`

.

Note

The `hip_bfloat16`

data type is only supported on AMD platforms.

### Complex data types[#](#complex-data-types)

hipBLAS uses the HIP types `hipComplex`

and `hipDoubleComplex`

in its API.

## Functions data type support[#](#functions-data-type-support)

This section collects the data type support tables of BLAS functions and
solver functions. The cuBLAS backend does not support all the functions and all
the types. For more information, see [cuBLAS backend](hipblas-api-functions.html#hipblas-backend).

### Level 1 functions - vector operations[#](#level-1-functions-vector-operations)

Level-1 functions perform scalar, vector, and vector-vector operations.

Function |
Description |
float16 |
bfloat16 |
float |
double |
|---|---|---|---|---|---|
Finds the first index of the element of minimum or maximum magnitude of a vector x or computes the sum of the magnitudes of elements of a real vector x. |
❌ |
❌ |
✅ |
✅ |
|
Scales a vector and adds it to another: \(y = \alpha x + y\) |
✅ |
❌ |
✅ |
✅ |
|
Copies vector x to y: \(y = x\) |
❌ |
❌ |
✅ |
✅ |
|
Computes the dot product: \(result = x^T y\) |
✅ |
✅ |
✅ |
✅ |
|
Computes the Euclidean norm of a vector. |
❌ |
❌ |
✅ |
✅ |
|
Applies and generates a Givens rotation matrix. |
❌ |
❌ |
✅ |
✅ |
|
Applies and generates a modified Givens rotation matrix. |
❌ |
❌ |
✅ |
✅ |
|
Scales a vector by a scalar: \(x = \alpha x\) |
❌ |
❌ |
✅ |
✅ |
|
Swaps corresponding elements of two vectors x and y: \(x_i \leftrightarrow y_i \quad \text{for} \quad i = 0, 1, 2, \ldots, n - 1\) |
❌ |
❌ |
✅ |
✅ |

Function |
Description |
complex |
double complex |
|---|---|---|---|
Finds the first index of the element of minimum or maximum magnitude of a vector x or computes the sum of the magnitudes of elements of a real vector x. |
✅ |
✅ |
|
Scales a vector and adds it to another: \(y = \alpha x + y\) |
✅ |
✅ |
|
Copies vector x to y: \(y = x\) |
✅ |
✅ |
|
Computes the dot product: \(result = x^T y\) |
✅ |
✅ |
|
Computes the Euclidean norm of a vector. |
✅ |
✅ |
|
Applies and generates a Givens rotation matrix. |
✅ |
✅ |
|
Applies and generates a modified Givens rotation matrix. |
❌ |
❌ |
|
Scales a vector by a scalar: \(x = \alpha x\) |
✅ |
✅ |
|
Swaps corresponding elements of two vectors x and y: \(x_i \leftrightarrow y_i \quad \text{for} \quad i = 0, 1, 2, \ldots, n - 1\) |
✅ |
✅ |

### Level 2 functions - matrix-vector operations[#](#level-2-functions-matrix-vector-operations)

Level-2 functions perform matrix-vector operations.

Function |
Description |
float16 |
bfloat16 |
float |
double |
|---|---|---|---|---|---|
General band matrix-vector multiplication: \(y = \alpha A x + \beta y\) |
❌ |
❌ |
✅ |
✅ |
|
General matrix-vector multiplication: \(y = \alpha A x + \beta y\) |
❌ |
❌ |
✅ |
✅ |
|
Generalized rank-1 update: \(A = \alpha x y^T + A\) |
❌ |
❌ |
✅ |
✅ |
|
Generalized rank-1 update for unconjugated or conjugated complex numbers: \(A = \alpha x y^T + A\) |
NA |
NA |
NA |
NA |
|
Symmetric Band matrix-vector multiplication: \(y = \alpha A x + \beta y\) |
❌ |
❌ |
✅ |
✅ |
|
Symmetric packed rank-1 update. |
❌ |
❌ |
✅ |
✅ |
|
Symmetric packed rank-2 update. |
❌ |
❌ |
✅ |
✅ |
|
Symmetric matrix-vector multiplication: \(y = \alpha A x + \beta y\) |
❌ |
❌ |
✅ |
✅ |
|
Symmetric matrix rank-1 or rank-2 update. |
❌ |
❌ |
✅ |
✅ |
|
Triangular band matrix-vector multiplication, triangular band solve. |
❌ |
❌ |
✅ |
✅ |
|
Triangular packed matrix-vector multiplication, triangular packed solve. |
❌ |
❌ |
✅ |
✅ |
|
Triangular matrix-vector multiplication, triangular solve. |
❌ |
❌ |
✅ |
✅ |
|
Hermitian matrix-vector multiplication. |
NA |
NA |
NA |
NA |
|
Hermitian rank-1 and rank-2 update. |
NA |
NA |
NA |
NA |
|
Hermitian packed rank-1 and rank-2 update of packed. |
NA |
NA |
NA |
NA |

Function |
Description |
complex |
double complex |
|---|---|---|---|
General band matrix-vector multiplication: \(y = \alpha A x + \beta y\) |
✅ |
✅ |
|
General matrix-vector multiplication: \(y = \alpha A x + \beta y\) |
✅ |
✅ |
|
Generalized rank-1 update: \(A = \alpha x y^T + A\) |
NA |
NA |
|
Generalized rank-1 update for unconjugated or conjugated complex numbers: \(A = \alpha x y^T + A\) |
✅ |
✅ |
|
Symmetric Band matrix-vector multiplication: \(y = \alpha A x + \beta y\) |
❌ |
❌ |
|
Symmetric packed rank-1 update. |
✅ |
✅ |
|
Symmetric packed rank-2 update. |
❌ |
❌ |
|
Symmetric matrix-vector multiplication: \(y = \alpha A x + \beta y\) |
✅ |
✅ |
|
Symmetric matrix rank-1 or rank-2 update. |
✅ |
✅ |
|
Triangular band matrix-vector multiplication, triangular band solve. |
✅ |
✅ |
|
Triangular packed matrix-vector multiplication, triangular packed solve. |
✅ |
✅ |
|
Triangular matrix-vector multiplication, triangular solve. |
✅ |
✅ |
|
Hermitian matrix-vector multiplication. |
✅ |
✅ |
|
Hermitian rank-1 and rank-2 update. |
✅ |
✅ |
|
Hermitian packed rank-1 and rank-2 update. |
✅ |
✅ |

### Level 3 functions - matrix-matrix operations[#](#level-3-functions-matrix-matrix-operations)

Level-3 functions perform matix-matrix operations. hipBLAS calls the AMD
[Tensile](https://rocm.docs.amd.com/projects/Tensile/en/latest/src/index.html) and [hipBLASLt](https://rocm.docs.amd.com/projects/hipBLASLt/en/latest/index.html)
libraries for Level-3 GEMMs (matrix matrix multiplication).

Function |
Description |
float16 |
bfloat16 |
float |
double |
|---|---|---|---|---|---|
General matrix-matrix multiplication: \(C = \alpha A B + \beta C\) |
✅ |
❌ |
✅ |
✅ |
|
Symmetric matrix-matrix multiplication: \(C = \alpha A B + \beta C\) |
❌ |
❌ |
✅ |
✅ |
|
Update symmetric matrix with one matrix product or by using two matrices. |
❌ |
❌ |
✅ |
✅ |
|
SYRKX adds an extra matrix multiplication step before updating the symmetric matrix. |
❌ |
❌ |
✅ |
✅ |
|
Triangular matrix-matrix multiplication. |
❌ |
❌ |
✅ |
✅ |
|
Triangular solve with multiple right-hand sides. |
❌ |
❌ |
✅ |
✅ |
|
Hermitian matrix-matrix multiplication. |
NA |
NA |
NA |
NA |
|
Update Hermitian matrix with one matrix product or by using two matrices. |
NA |
NA |
NA |
NA |
|
HERKX adds an extra matrix multiplication step before updating the Hermitian matrix. |
NA |
NA |
NA |
NA |
|
Triangular matrix inversion. |
❌ |
❌ |
✅ |
✅ |
|
Diagonal matrix matrix multiplication. |
❌ |
❌ |
✅ |
✅ |

Function |
Description |
complex |
double complex |
|---|---|---|---|
General matrix-matrix multiplication: \(C = \alpha A B + \beta C\) |
✅ |
✅ |
|
Symmetric matrix-matrix multiplication: \(C = \alpha A B + \beta C\) |
✅ |
✅ |
|
Update symmetric matrix with one matrix product or by using two matrices. |
✅ |
✅ |
|
SYRKX adds an extra matrix multiplication step before updating the symmetric matrix. |
✅ |
✅ |
|
Triangular matrix-matrix multiplication. |
✅ |
✅ |
|
Triangular solve with multiple right-hand sides. |
✅ |
✅ |
|
Hermitian matrix-matrix multiplication. |
✅ |
✅ |
|
Update Hermitian matrix with one matrix product or by using two matrices. |
✅ |
✅ |
|
HERKX adds an extra matrix multiplication step before updating the Hermitian matrix. |
✅ |
✅ |
|
Triangular matrix inversion. |
✅ |
✅ |
|
Diagonal matrix matrix multiplication. |
✅ |
✅ |

### Extensions[#](#extensions)

The [extension functions](hipblas-api-functions.html#hipblas-extension) data type support is listed
separately for every function for the different backends in the
[rocBLAS extensions](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/extension.html#extension) and
[cuBLAS extensions](https://docs.nvidia.com/cuda/cublas/index.html#blas-like-extension)
documentation.

### SOLVER API[#](#solver-api)

[Solver API](hipblas-api-functions.html#solver-api) is for solving linear systems, computing matrix
inverses, and performing matrix factorizations.

Function |
Description |
float16 |
bfloat16 |
float |
double |
|---|---|---|---|---|---|
Compute the LU factorization of a general matrix using partial pivoting with row interchanges. |
❌ |
❌ |
✅ |
✅ |
|
Solve a system of linear equations \(AxX=B\) after performing an LU factorization using GETRF. |
❌ |
❌ |
✅ |
✅ |
|
Compute the inverse of a matrix using its LU factorization. |
❌ |
❌ |
⚠️ |
⚠️ |
|
QR factorization of a general matrix. |
❌ |
❌ |
✅ |
✅ |
|
Solve overdetermined or underdetermined linear systems using the QR factorization of a matrix. |
❌ |
❌ |
✅ |
✅ |

Function |
Description |
complex |
double complex |
|---|---|---|---|
Compute the LU factorization of a general matrix using partial pivoting with row interchanges. |
✅ |
✅ |
|
Solve a system of linear equations \(AxX=B\) after performing an LU factorization using GETRF. |
✅ |
✅ |
|
Compute the inverse of a matrix using its LU factorization. |
⚠️ |
⚠️ |
|
QR factorization of a general matrix. |
✅ |
✅ |
|
Solve overdetermined or underdetermined linear systems using the QR factorization of a matrix. |
✅ |
✅ |

Footnotes
