---
title: "Data type support &#8212; hipBLASLt 1.2.2 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipBLASLt/en/latest/reference/data-type-support.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:20:49.705450+00:00
content_hash: "c421c7dba40df286"
---

# Data type support[#](#data-type-support)

This topic lists the supported data types for the hipBLASLt GEMM operation,
which is performed by [hipblasLtMatmul()](api-reference.html#hipblasltmatmul).

The `hipDataType`

enumeration defines data precision types and is primarily
used when the data reference itself does not include type information, such as
in `void*`

pointers. This enumeration is mainly utilized in BLAS libraries.

The hipBLASLt input and output types are listed in the following table.

hipDataType |
hipBLASLt type |
Description |
|---|---|---|
|
|
8-bit real signed integer. |
|
|
32-bit real signed integer. |
|
N/A |
4-bit real float4 precision floating-point |
|
N/A |
6-bit real float6 precision floating-point |
|
N/A |
6-bit real bfloat6 precision floating-point |
|
|
8-bit real float8 precision floating-point |
|
|
8-bit real bfloat8 precision floating-point |
|
|
8-bit real float8 precision floating-point |
|
|
8-bit real bfloat8 precision floating-point |
|
|
16-bit real half precision floating-point |
|
|
16-bit real bfloat16 precision floating-point |
|
|
32-bit real single precision floating-point |

Note

The `hipblaslt_f8_fnuz`

and `hipblaslt_bf8_fnuz`

data types are only
supported on the gfx942 platform. The `hipblaslt_f8`

and `hipblaslt_bf8`

data types are only
supported on the gfx950 and gfx12 platforms.

The hipBLASLt compute modes are listed in the following table.

hipDataType |
Description |
|---|---|
|
32-bit integer compute mode. |
|
16-bit half precision floating-point compute mode. |
|
32-bit singple precision floating-point compute mode. |
|
64-bit double precision floating-point compute mode. |
|
Enables the library to utilize Tensor Cores with 32-bit float computation for matrices with 16-bit half precision input and output. |
|
Enables the library to utilize Tensor Cores with 32-bit float computation for matrices with 16-bit bfloat16 precision input and output. |
|
Enables the library to utilize Tensor Cores with TF32 computation for matrices with 32-bit input and output. |

## Data type combinations[#](#data-type-combinations)

hipBLASLt supports various combinations of input (A, B), accumulation (C), output (D), and compute data types for GEMM operations. The library enables mixed-precision operations, allowing you to use lower precision inputs with higher precision compute for optimal performance while maintaining accuracy where needed.

The GEMM operation follows this equation:

Where \(op( )\) refers to in-place operations, such as transpose and non-transpose, and \(alpha\) and \(beta\) are scalars.

For complete details on supported data type combinations, including specific
compute types, scale types, and bias configurations, see the
[hipBLASLt API reference page](api-reference.html#api-reference).

For more information about data type support for the other ROCm libraries, see
[Data types and precision support page](https://rocm.docs.amd.com/en/latest/reference/precision-support.html).
