---
title: "rocBLAS deprecations by version &#8212; rocBLAS 5.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/deprecations.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:10:47.882113+00:00
content_hash: "35f12c9303f73e77"
---

# rocBLAS deprecations by version[#](#rocblas-deprecations-by-version)

The following sections list the features deprecation by release version.

## Removed in rocBLAS 5.0[#](#removed-in-rocblas-5-0)

### rocblas_gemm_ex3, gemm_batched_ex3 and gemm_strided_batched_ex3 removed[#](#rocblas-gemm-ex3-gemm-batched-ex3-and-gemm-strided-batched-ex3-removed)

`rocblas_gemm_ex3`

, `gemm_batched_ex3`

, and `gemm_strided_batched_ex3`

API functions were removed in 5.0.

### rocblas_Xgemm_kernel_name removed[#](#rocblas-xgemm-kernel-name-removed)

`rocblas_Xgemm_kernel_name`

API functions were removed in 5.0.

## Announced in rocBLAS 4.3[#](#announced-in-rocblas-4-3)

### rocblas_Xgemm_kernel_name APIs deprecated[#](#rocblas-xgemm-kernel-name-apis-deprecated)

`rocblas_Xgemm_kernel_name`

APIs are deprecated and will be removed in the next major release of rocBLAS.

## Announced in rocBLAS 4.2[#](#announced-in-rocblas-4-2)

### gemm_ex3 deprecation for all 8 bit float API[#](#gemm-ex3-deprecation-for-all-8-bit-float-api)

`rocblas_gemm_ex3`

, `gemm_batched_ex3`

, and `gemm_strided_batched_ex3`

are deprecated and will be removed in the next
major release of rocBLAS. See [hipBLASLt](https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipblaslt) for future 8-bit float usage.

## Announced in rocBLAS 4.0[#](#announced-in-rocblas-4-0)

### Atomic operations will be disabled by default[#](#atomic-operations-will-be-disabled-by-default)

The default [ rocblas_atomics_mode](enumerations.html#_CPPv420rocblas_atomics_mode) in

[will change in the future to](datatypes.html#_CPPv414rocblas_handle)

`rocblas_handle`

[from the current](enumerations.html#_CPPv4N20rocblas_atomics_mode27rocblas_atomics_not_allowedE)

`rocblas_atomics_not_allowed`

[. Thus the default will allow for improved determinism over performance. Users can add explicit control and not be affected by this change by calling the function](enumerations.html#_CPPv4N20rocblas_atomics_mode23rocblas_atomics_allowedE)

`rocblas_atomics_allowed`

[.](helper-functions.html#_CPPv424rocblas_set_atomics_mode14rocblas_handle20rocblas_atomics_mode)

`rocblas_set_atomics_mode()`

## Removed in rocBLAS 4.0[#](#removed-in-rocblas-4-0)

### rocblas_gemm_ext2 removed[#](#rocblas-gemm-ext2-removed)

`rocblas_gemm_ext2`

API function was removed in 4.0.

### rocblas_gemm_flags_pack_int8x4 gemm support removed[#](#rocblas-gemm-flags-pack-int8x4-gemm-support-removed)

Packed int8x4 support was removed as support for arbitrary dimensioned int8_t data is a superset of this functionality:

`rocblas_gemm_flags_pack_int8x4`

enum value in`rocblas_gemm_flags`

was removedstruct

`rocblas_int8x4`

was removedfunction

`rocblas_query_int8_layout_flag`

was removedenum

`rocblas_int8_type_for_hipblas`

type was removed

### Legacy BLAS in-place trmm API removed[#](#legacy-blas-in-place-trmm-api-removed)

The Legacy BLAS in-place trmm API is removed. It is replaced by an API that supports both in-place and out-of-place trmm. The Legacy BLAS in-place trmm calculated

```
B <- alpha * op(A) * B
```

The in-place and out-of-place trmm API calculates

```
C <- alpha * op(A) * B
```

The in-place functionality is available by setting C the same as B and `ldb = ldc`

. For out-of-place functionality C and B are different.

### Removal of __STDC_WANT_IEC_60559_TYPES_EXT__ define[#](#removal-of-stdc-want-iec-60559-types-ext-define)

The #define `__STDC_WANT_IEC_60559_TYPES_EXT__`

has been removed from `rocblas-types.h`

. Users who want ISO/IEC TS 18661-3:2015 functionality
must define `__STDC_WANT_IEC_60559_TYPES_EXT__`

before including `float.h`

, `math.h`

, and `rocblas.h`

.

## Announced in rocBLAS 3.1[#](#announced-in-rocblas-3-1)

### Removal of __STDC_WANT_IEC_60559_TYPES_EXT__ define[#](#id1)

Prior to rocBLAS 4.0, `__STDC_WANT_IEC_60559_TYPES_EXT__`

was defined in `rocblas.h`

, or more specifically `rocblas-types.h`

, before including `float.h`

. From rocBLAS 4.0, this
define will be removed. Users who want ISO/IEC TS 18661-3:2015 functionality must define `__STDC_WANT_IEC_60559_TYPES_EXT__`

before including `float.h`

and `rocblas.h`

.

## Announced in rocBLAS 3.0[#](#announced-in-rocblas-3-0)

### Replace Legacy BLAS in-place trmm functions with trmm functions that support both in-place and out-of-place functionality[#](#replace-legacy-blas-in-place-trmm-functions-with-trmm-functions-that-support-both-in-place-and-out-of-place-functionality)

Use of the deprecated Legacy BLAS in-place `trmm`

functions will give deprecation warnings telling
you to compile with `-DROCBLAS_V3`

and use the new in-place and out-of-place trmm functions.

Note that there are no deprecation warnings for the rocBLAS Fortran API.

The Legacy BLAS in-place `trmm`

calculates `B <- alpha * op(A) * B`

. Matrix B is replaced in-place by
triangular matrix A multiplied by matrix B. The prototype in the include file `rocblas-functions.h`

is:

```
rocblas_status rocblas_strmm(rocblas_handle handle,
rocblas_side side,
rocblas_fill uplo,
rocblas_operation transA,
rocblas_diagonal diag,
rocblas_int m,
rocblas_int n,
const float* alpha,
const float* A,
rocblas_int lda,
float* B,
rocblas_int ldb);
```

rocBLAS 3.0 deprecates the legacy BLAS `trmm`

functionality and replaces it with `C <- alpha * op(A) * B`

. The prototype is:

```
rocblas_status rocblas_strmm(rocblas_handle handle,
rocblas_side side,
rocblas_fill uplo,
rocblas_operation transA,
rocblas_diagonal diag,
rocblas_int m,
rocblas_int n,
const float* alpha,
const float* A,
rocblas_int lda,
const float* B,
rocblas_int ldb,
float* C,
rocblas_int ldc);
```

The new API provides the legacy BLAS in-place functionality if you set pointer C equal to pointer B and ldc equal to ldb.

There are similar deprecations for the _batched and _strided_batched versions of `trmm`

.

### Remove rocblas_gemm_ext2[#](#remove-rocblas-gemm-ext2)

`rocblas_gemm_ext2`

is deprecated and it will be removed in the next major release of rocBLAS.

### Removal of rocblas_query_int8_layout_flag[#](#removal-of-rocblas-query-int8-layout-flag)

`rocblas_query_int8_layout_flag`

will be removed and support will end for the `rocblas_gemm_flags_pack_int8x4`

enum in `rocblas_gemm_flags`

in a future release. `rocblas_int8_type_for_hipblas`

will remain until `rocblas_query_int8_layout_flag`

is removed.

### Remove user_managed mode from rocblas_handle[#](#remove-user-managed-mode-from-rocblas-handle)

From rocBLAS 4.0, the schemes for allocating temporary device memory would be reduced to two from four.

Existing four schemes are:

rocblas_managed

user_managed, preallocate

user_managed, manual

user_owned


From rocBLAS 4.0, the two schemes would be rocblas_managed and user_owned. The functionality of user_managed ( both preallocate and manual) would be combined into rocblas_managed scheme.

Due to this the following APIs would be affected:

`rocblas_is_user_managing_device_memory()`

will be removed.`rocblas_set_device_memory_size()`

will be replaced by a future function`rocblas_increase_device_memory_size()`

, this new API would allow users to increase the device memory pool size at runtime.

## Announced in rocBLAS 2.46[#](#announced-in-rocblas-2-46)

### Remove ability for hipBLAS to set rocblas_int8_type_for_hipblas[#](#remove-ability-for-hipblas-to-set-rocblas-int8-type-for-hipblas)

From rocBLAS 3.0, remove `enum rocblas_int8_type_for_hipblas`

and the functions `rocblas_get_int8_type_for_hipblas`

and
`rocblas_set_int8_type_for_hipblas`

. These are used by hipBLAS to select either `int8_t`

or `packed_int8x4`

datatype.
In hipBLAS the option to use `packed_int8x4`

will be removed, only `int8_t`

will be available.

## Announced in rocBLAS 2.45[#](#announced-in-rocblas-2-45)

### Replace is_complex by rocblas_is_complex[#](#replace-is-complex-by-rocblas-is-complex)

From rocBLAS 3.0 the trait `is_complex`

for rocblas complex types has been removed. Replace with `rocblas_is_complex`

.

### Replace truncate with rocblas_truncate[#](#replace-truncate-with-rocblas-truncate)

From rocBLAS 3.0 enum `truncate_t`

and the value truncate has been removed and replaced by `rocblas_truncate_t`

and `rocblas_truncate`

, respectively.
