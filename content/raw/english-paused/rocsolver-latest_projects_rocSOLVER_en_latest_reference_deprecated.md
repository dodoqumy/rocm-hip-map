---
title: "Deprecated rocSOLVER components &#8212; rocSOLVER 3.32.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocSOLVER/en/latest/reference/deprecated.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:10:49.502992+00:00
content_hash: "5d5869331fa16498"
---

# Deprecated rocSOLVER components[#](#deprecated-rocsolver-components)

rocSOLVER originally maintained its own types and helpers as aliases to those of rocBLAS.
These aliases are now deprecated. See the [rocBLAS types](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html)
and [rocBLAS auxiliary functions](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/helper-functions.html)
documentation for information on the suggested replacements.

Deprecated

[Types](#deptypes).Deprecated

[Auxiliary functions](#dephelpers).

## Types[#](#types)

-
typedef
[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)rocsolver_int[#](#_CPPv413rocsolver_int) -
*Deprecated:* Use

`rocblas_int`

.

-

Deprecated since version 3.5: Use `rocblas_int`

.

-
typedef
[rocblas_handle](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv414rocblas_handle)rocsolver_handle[#](#_CPPv416rocsolver_handle) -
*Deprecated:* Use

`rocblas_handle`

.

-

Deprecated since version 3.5: Use `rocblas_handle`

.

-
typedef
[rocblas_direct](types.html#_CPPv414rocblas_direct)rocsolver_direction[#](#_CPPv419rocsolver_direction) -
*Deprecated:* Use

`rocblas_direct`


-

Deprecated since version 3.5: Use `rocblas_direct`

.

-
typedef
[rocblas_storev](types.html#_CPPv414rocblas_storev)rocsolver_storev[#](#_CPPv416rocsolver_storev) -
*Deprecated:* Use

`rocblas_storev`

.

-

Deprecated since version 3.5: Use `rocblas_storev`

.

-
typedef
[rocblas_operation](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/enumerations.html#_CPPv417rocblas_operation)rocsolver_operation[#](#_CPPv419rocsolver_operation) -
*Deprecated:* Use

`rocblas_operation`

.

-

Deprecated since version 3.5: Use `rocblas_operation`

.

-
typedef
[rocblas_fill](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/enumerations.html#_CPPv412rocblas_fill)rocsolver_fill[#](#_CPPv414rocsolver_fill) -
*Deprecated:* Use

`rocblas_fill`

.

-

Deprecated since version 3.5: Use `rocblas_fill`

.

-
typedef
[rocblas_diagonal](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/enumerations.html#_CPPv416rocblas_diagonal)rocsolver_diagonal[#](#_CPPv418rocsolver_diagonal) -
*Deprecated:* Use

`rocblas_diagonal`

.

-

Deprecated since version 3.5: Use `rocblas_diagonal`

.

-
typedef
[rocblas_side](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/enumerations.html#_CPPv412rocblas_side)rocsolver_side[#](#_CPPv414rocsolver_side) -
*Deprecated:* Use

`rocblas_side`

.

-

Deprecated since version 3.5: Use `rocblas_side`

.

-
typedef
[rocblas_status](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/enumerations.html#_CPPv414rocblas_status)rocsolver_status[#](#_CPPv416rocsolver_status) -
*Deprecated:* Use

`rocblas_status`

.

-

Deprecated since version 3.5: Use `rocblas_status`

.

## Auxiliary functions[#](#auxiliary-functions)

-
[rocsolver_status](#_CPPv416rocsolver_status)rocsolver_create_handle([rocsolver_handle](#_CPPv416rocsolver_handle)*handle)[#](#_CPPv423rocsolver_create_handleP16rocsolver_handle) -
*Deprecated:* Use

`rocblas_create_handle`

.

-

Deprecated since version 3.5: Use `rocblas_create_handle()`

.

-
[rocsolver_status](#_CPPv416rocsolver_status)rocsolver_destroy_handle([rocsolver_handle](#_CPPv416rocsolver_handle)handle)[#](#_CPPv424rocsolver_destroy_handle16rocsolver_handle) -
*Deprecated:* Use

`rocblas_destroy_handle`

.

-

Deprecated since version 3.5: Use `rocblas_destroy_handle()`

.

-
[rocsolver_status](#_CPPv416rocsolver_status)rocsolver_set_stream([rocsolver_handle](#_CPPv416rocsolver_handle)handle, hipStream_t stream)[#](#_CPPv420rocsolver_set_stream16rocsolver_handle11hipStream_t) -
*Deprecated:* Use

`rocblas_set_stream`

.

-

Deprecated since version 3.5: Use `rocblas_set_stream()`

.

-
[rocsolver_status](#_CPPv416rocsolver_status)rocsolver_get_stream([rocsolver_handle](#_CPPv416rocsolver_handle)handle, hipStream_t *stream)[#](#_CPPv420rocsolver_get_stream16rocsolver_handleP11hipStream_t) -
*Deprecated:* Use

`rocblas_get_stream`

.

-

Deprecated since version 3.5: Use `rocblas_get_stream()`

.

-
[rocsolver_status](#_CPPv416rocsolver_status)rocsolver_set_vector([rocsolver_int](#_CPPv413rocsolver_int)n,[rocsolver_int](#_CPPv413rocsolver_int)elem_size, const void *x,[rocsolver_int](#_CPPv413rocsolver_int)incx, void *y,[rocsolver_int](#_CPPv413rocsolver_int)incy)[#](#_CPPv420rocsolver_set_vector13rocsolver_int13rocsolver_intPKv13rocsolver_intPv13rocsolver_int) -
*Deprecated:* Use

`rocblas_set_vector`

.

-

Deprecated since version 3.5: Use `rocblas_set_vector()`

.

-
[rocsolver_status](#_CPPv416rocsolver_status)rocsolver_get_vector([rocsolver_int](#_CPPv413rocsolver_int)n,[rocsolver_int](#_CPPv413rocsolver_int)elem_size, const void *x,[rocsolver_int](#_CPPv413rocsolver_int)incx, void *y,[rocsolver_int](#_CPPv413rocsolver_int)incy)[#](#_CPPv420rocsolver_get_vector13rocsolver_int13rocsolver_intPKv13rocsolver_intPv13rocsolver_int) -
*Deprecated:* Use

`rocblas_get_vector`

.

-

Deprecated since version 3.5: Use `rocblas_get_vector()`

.

-
[rocsolver_status](#_CPPv416rocsolver_status)rocsolver_set_matrix([rocsolver_int](#_CPPv413rocsolver_int)rows,[rocsolver_int](#_CPPv413rocsolver_int)cols,[rocsolver_int](#_CPPv413rocsolver_int)elem_size, const void *a,[rocsolver_int](#_CPPv413rocsolver_int)lda, void *b,[rocsolver_int](#_CPPv413rocsolver_int)ldb)[#](#_CPPv420rocsolver_set_matrix13rocsolver_int13rocsolver_int13rocsolver_intPKv13rocsolver_intPv13rocsolver_int) -
*Deprecated:* Use

`rocblas_set_matrix`

.

-

Deprecated since version 3.5: Use `rocblas_set_matrix()`

.

-
[rocsolver_status](#_CPPv416rocsolver_status)rocsolver_get_matrix([rocsolver_int](#_CPPv413rocsolver_int)rows,[rocsolver_int](#_CPPv413rocsolver_int)cols,[rocsolver_int](#_CPPv413rocsolver_int)elem_size, const void *a,[rocsolver_int](#_CPPv413rocsolver_int)lda, void *b,[rocsolver_int](#_CPPv413rocsolver_int)ldb)[#](#_CPPv420rocsolver_get_matrix13rocsolver_int13rocsolver_int13rocsolver_intPKv13rocsolver_intPv13rocsolver_int) -
*Deprecated:* Use

`rocblas_get_matrix`

.

-

Deprecated since version 3.5: Use `rocblas_get_matrix()`

.
