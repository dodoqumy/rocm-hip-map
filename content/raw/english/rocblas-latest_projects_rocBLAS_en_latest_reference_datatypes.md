---
title: "rocBLAS datatypes &#8212; rocBLAS 5.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:10:54.784425+00:00
content_hash: "b90e03e914523ebd"
---

# rocBLAS datatypes[#](#rocblas-datatypes)

## rocblas_handle[#](#rocblas-handle)

-
typedef struct _rocblas_handle *rocblas_handle
[#](#_CPPv414rocblas_handle) rocblas_handle is a structure holding the rocblas library context. It must be initialized using

[rocblas_create_handle()](helper-functions.html#rocblas-auxiliary_8h_1ab158b3ae4dfecd4e151cb122697aae64), and the returned handle must be passed to all subsequent library function calls. It should be destroyed at the end using[rocblas_destroy_handle()](helper-functions.html#rocblas-auxiliary_8h_1a770a77925623df894aae6a89f2736cfb).

## rocblas_int[#](#rocblas-int)

-
typedef int32_t rocblas_int
[#](#_CPPv411rocblas_int) To specify whether int32 is used for LP64 or int64 is used for ILP64. This define should be considered deprecated as being supplanted by additional interfaces and was never tested.


## rocblas_stride[#](#rocblas-stride)

-
typedef int64_t rocblas_stride
[#](#_CPPv414rocblas_stride) Stride between matrices or vectors in strided_batched functions.


## rocblas_half[#](#rocblas-half)

-
struct rocblas_half
[#](#_CPPv412rocblas_half) Structure definition for

[rocblas_half](#structrocblas__half).

## rocblas_bfloat16[#](#rocblas-bfloat16)

-
struct rocblas_bfloat16
[#](#_CPPv416rocblas_bfloat16) Struct to represent a 16 bit Brain floating-point number.


## rocblas_float_complex[#](#rocblas-float-complex)

-
struct rocblas_float_complex
[#](#_CPPv421rocblas_float_complex) Struct to represent a complex number with single precision real and imaginary parts.


## rocblas_double_complex[#](#rocblas-double-complex)

-
struct rocblas_double_complex
[#](#_CPPv422rocblas_double_complex) Struct to represent a complex number with double precision real and imaginary parts.
