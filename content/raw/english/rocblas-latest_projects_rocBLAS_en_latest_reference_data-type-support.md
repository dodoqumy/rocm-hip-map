---
title: "Data type support &#8212; rocBLAS 5.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/data-type-support.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:09:35.295771+00:00
content_hash: "8dfecc10de9a34b8"
---

# Data type support[#](#data-type-support)

This topic lists the data type support for the rocBLAS library on AMD GPUs for
different levels of BLAS operations [Level 1](level-1.html#level-1),
[2](level-2.html#level-2), and [3](level-3.html#level-3).

The rocBLAS library functions are also available with ILP64 interfaces. With
these interfaces, all `rocblas_int`

arguments are replaced by the type name
`int64_t`

. For more information on these `_64`

functions, see the
[ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

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

## Level 1 functions - vector operations[#](#level-1-functions-vector-operations)

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

## Level 2 functions - matrix-vector operations[#](#level-2-functions-matrix-vector-operations)

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
⚠️ |
⚠️ |
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
❌ |
❌ |
❌ |
❌ |
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
❌ |
❌ |
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

## Level 3 functions - matrix-matrix operations[#](#level-3-functions-matrix-matrix-operations)

Level-3 functions perform matix-matrix operations. rocBLAS calls the AMD
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
❌ |
❌ |

## Extensions[#](#extensions)

The extension function data type support is listed for every function separately
on the [Extensions reference page](extension.html#extension).

Footnotes
