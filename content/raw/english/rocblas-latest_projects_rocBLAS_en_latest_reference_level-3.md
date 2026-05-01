---
title: "rocBLAS Level-3 functions &#8212; rocBLAS 5.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/level-3.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:11:11.069063+00:00
content_hash: "e05cd5138db0b085"
---

# rocBLAS Level-3 functions[#](#rocblas-level-3-functions)

rocBLAS Level-3 functions perform matix-matrix operations. [[Level3]](references.html#level3)

Level-3 functions support the ILP64 API. For more information on these `_64`

functions, see the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xgemm + batched, strided_batched[#](#rocblas-xgemm-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sgemm([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const float *alpha, const float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const float *B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const float *beta, float *C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv413rocblas_sgemm14rocblas_handle17rocblas_operation17rocblas_operation11rocblas_int11rocblas_int11rocblas_intPKfPKf11rocblas_intPKf11rocblas_intPKfPf11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dgemm([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const double *alpha, const double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const double *B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const double *beta, double *C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv413rocblas_dgemm14rocblas_handle17rocblas_operation17rocblas_operation11rocblas_int11rocblas_int11rocblas_intPKdPKd11rocblas_intPKd11rocblas_intPKdPd11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_hgemm([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_half](datatypes.html#_CPPv412rocblas_half)*alpha, const[rocblas_half](datatypes.html#_CPPv412rocblas_half)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_half](datatypes.html#_CPPv412rocblas_half)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const[rocblas_half](datatypes.html#_CPPv412rocblas_half)*beta,[rocblas_half](datatypes.html#_CPPv412rocblas_half)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv413rocblas_hgemm14rocblas_handle17rocblas_operation17rocblas_operation11rocblas_int11rocblas_int11rocblas_intPK12rocblas_halfPK12rocblas_half11rocblas_intPK12rocblas_half11rocblas_intPK12rocblas_halfP12rocblas_half11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cgemm([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv413rocblas_cgemm14rocblas_handle17rocblas_operation17rocblas_operation11rocblas_int11rocblas_int11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_intPK21rocblas_float_complex11rocblas_intPK21rocblas_float_complexP21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zgemm([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv413rocblas_zgemm14rocblas_handle17rocblas_operation17rocblas_operation11rocblas_int11rocblas_int11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_intPK22rocblas_double_complex11rocblas_intPK22rocblas_double_complexP22rocblas_double_complex11rocblas_int) **BLAS Level 3 API**gemm performs one of the matrix-matrix operations:

Although not widespread, some gemm kernels may use atomic operations. See Atomic Operations in the API Reference Guide for more information.C = alpha*op( A )*op( B ) + beta*C, where op( X ) is one of op( X ) = X or op( X ) = X**T or op( X ) = X**H, alpha and beta are scalars, and A, B and C are matrices, with op( A ) an m by k matrix, op( B ) a k by n matrix and C an m by n matrix.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**transA**–**[in]**[rocblas_operation] specifies the form of op( A ).**transB**–**[in]**[rocblas_operation] specifies the form of op( B ).**m**–**[in]**[rocblas_int] number or rows of matrices op( A ) and C.**n**–**[in]**[rocblas_int] number of columns of matrices op( B ) and C.**k**–**[in]**[rocblas_int] number of columns of matrix op( A ) and number of rows of matrix op( B ).**alpha**–**[in]**device pointer or host pointer specifying the scalar alpha.**A**–**[in]**device pointer storing matrix A.**lda**–**[in]**[rocblas_int] specifies the leading dimension of A.**B**–**[in]**device pointer storing matrix B.**ldb**–**[in]**[rocblas_int] specifies the leading dimension of B.**beta**–**[in]**device pointer or host pointer specifying the scalar beta.**C**–**[inout]**device pointer storing matrix C on the GPU.**ldc**–**[in]**[rocblas_int] specifies the leading dimension of C.



`gemm`

functions support the `_64`

interface. However, no arguments larger than `(int32_t max value * 16)`

are currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sgemm_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const float *alpha, const float *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const float *const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const float *beta, float *const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_sgemm_batched14rocblas_handle17rocblas_operation17rocblas_operation11rocblas_int11rocblas_int11rocblas_intPKfA_PCKf11rocblas_intA_PCKf11rocblas_intPKfA_PCf11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dgemm_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const double *alpha, const double *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const double *const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const double *beta, double *const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_dgemm_batched14rocblas_handle17rocblas_operation17rocblas_operation11rocblas_int11rocblas_int11rocblas_intPKdA_PCKd11rocblas_intA_PCKd11rocblas_intPKdA_PCd11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_hgemm_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_half](datatypes.html#_CPPv412rocblas_half)*alpha, const[rocblas_half](datatypes.html#_CPPv412rocblas_half)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_half](datatypes.html#_CPPv412rocblas_half)*const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const[rocblas_half](datatypes.html#_CPPv412rocblas_half)*beta,[rocblas_half](datatypes.html#_CPPv412rocblas_half)*const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_hgemm_batched14rocblas_handle17rocblas_operation17rocblas_operation11rocblas_int11rocblas_int11rocblas_intPK12rocblas_halfA_PCK12rocblas_half11rocblas_intA_PCK12rocblas_half11rocblas_intPK12rocblas_halfA_PC12rocblas_half11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cgemm_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_cgemm_batched14rocblas_handle17rocblas_operation17rocblas_operation11rocblas_int11rocblas_int11rocblas_intPK21rocblas_float_complexA_PCK21rocblas_float_complex11rocblas_intA_PCK21rocblas_float_complex11rocblas_intPK21rocblas_float_complexA_PC21rocblas_float_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zgemm_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_zgemm_batched14rocblas_handle17rocblas_operation17rocblas_operation11rocblas_int11rocblas_int11rocblas_intPK22rocblas_double_complexA_PCK22rocblas_double_complex11rocblas_intA_PCK22rocblas_double_complex11rocblas_intPK22rocblas_double_complexA_PC22rocblas_double_complex11rocblas_int11rocblas_int) **BLAS Level 3 API**gemm_batched performs one of the batched matrix-matrix operations:

C_i = alpha*op( A_i )*op( B_i ) + beta*C_i, for i = 1, ..., batch_count, where op( X ) is one of op( X ) = X or op( X ) = X**T or op( X ) = X**H, alpha and beta are scalars, and A, B and C are strided batched matrices, with op( A ) an m by k by batch_count matrices, op( B ) an k by n by batch_count matrices and C an m by n by batch_count matrices.

- Parameters:
**handle**–**[in]**[rocblas_handle handle to the rocblas library context queue.**transA**–**[in]**[rocblas_operation] specifies the form of op( A ).**transB**–**[in]**[rocblas_operation] specifies the form of op( B ).**m**–**[in]**[rocblas_int] matrix dimention m.**n**–**[in]**[rocblas_int] matrix dimention n.**k**–**[in]**[rocblas_int] matrix dimention k.**alpha**–**[in]**device pointer or host pointer specifying the scalar alpha.**A**–**[in]**device array of device pointers storing each matrix A_i.**lda**–**[in]**[rocblas_int] specifies the leading dimension of each A_i.**B**–**[in]**device array of device pointers storing each matrix B_i.**ldb**–**[in]**[rocblas_int] specifies the leading dimension of each B_i.**beta**–**[in]**device pointer or host pointer specifying the scalar beta.**C**–**[inout]**device array of device pointers storing each matrix C_i.**ldc**–**[in]**[rocblas_int] specifies the leading dimension of each C_i.**batch_count**–**[in]**[rocblas_int] number of gemm operations in the batch.



`gemm_batched`

functions support the `_64`

interface. Only the parameter `batch_count`

larger than `(int32_t max value * 16)`

is currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sgemm_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const float *alpha, const float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_a, const float *B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_b, const float *beta, float *C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_c,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_sgemm_strided_batched14rocblas_handle17rocblas_operation17rocblas_operation11rocblas_int11rocblas_int11rocblas_intPKfPKf11rocblas_int14rocblas_stridePKf11rocblas_int14rocblas_stridePKfPf11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dgemm_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const double *alpha, const double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_a, const double *B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_b, const double *beta, double *C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_c,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_dgemm_strided_batched14rocblas_handle17rocblas_operation17rocblas_operation11rocblas_int11rocblas_int11rocblas_intPKdPKd11rocblas_int14rocblas_stridePKd11rocblas_int14rocblas_stridePKdPd11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_hgemm_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_half](datatypes.html#_CPPv412rocblas_half)*alpha, const[rocblas_half](datatypes.html#_CPPv412rocblas_half)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_a, const[rocblas_half](datatypes.html#_CPPv412rocblas_half)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_b, const[rocblas_half](datatypes.html#_CPPv412rocblas_half)*beta,[rocblas_half](datatypes.html#_CPPv412rocblas_half)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_c,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_hgemm_strided_batched14rocblas_handle17rocblas_operation17rocblas_operation11rocblas_int11rocblas_int11rocblas_intPK12rocblas_halfPK12rocblas_half11rocblas_int14rocblas_stridePK12rocblas_half11rocblas_int14rocblas_stridePK12rocblas_halfP12rocblas_half11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cgemm_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_a, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_b, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_c,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_cgemm_strided_batched14rocblas_handle17rocblas_operation17rocblas_operation11rocblas_int11rocblas_int11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_int14rocblas_stridePK21rocblas_float_complex11rocblas_int14rocblas_stridePK21rocblas_float_complexP21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zgemm_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_a, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_b, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_c,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_zgemm_strided_batched14rocblas_handle17rocblas_operation17rocblas_operation11rocblas_int11rocblas_int11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_int14rocblas_stridePK22rocblas_double_complex11rocblas_int14rocblas_stridePK22rocblas_double_complexP22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_int) **BLAS Level 3 API**gemm_strided_batched performs one of the strided batched matrix-matrix operations:

C_i = alpha*op( A_i )*op( B_i ) + beta*C_i, for i = 1, ..., batch_count, where op( X ) is one of op( X ) = X or op( X ) = X**T or op( X ) = X**H, alpha and beta are scalars, and A, B and C are strided batched matrices, with op( A ) an m by k by batch_count strided_batched matrix, op( B ) an k by n by batch_count strided_batched matrix and C an m by n by batch_count strided_batched matrix.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**transA**–**[in]**[rocblas_operation] specifies the form of op( A ).**transB**–**[in]**[rocblas_operation] specifies the form of op( B ).**m**–**[in]**[rocblas_int] matrix dimention m.**n**–**[in]**[rocblas_int] matrix dimention n.**k**–**[in]**[rocblas_int] matrix dimention k.**alpha**–**[in]**device pointer or host pointer specifying the scalar alpha.**A**–**[in]**device pointer pointing to the first matrix A_1.**lda**–**[in]**[rocblas_int] specifies the leading dimension of each A_i.**stride_a**–**[in]**[rocblas_stride] stride from the start of one A_i matrix to the next A_(i + 1).**B**–**[in]**device pointer pointing to the first matrix B_1.**ldb**–**[in]**[rocblas_int] specifies the leading dimension of each B_i.**stride_b**–**[in]**[rocblas_stride] stride from the start of one B_i matrix to the next B_(i + 1).**beta**–**[in]**device pointer or host pointer specifying the scalar beta.**C**–**[inout]**device pointer pointing to the first matrix C_1.**ldc**–**[in]**[rocblas_int] specifies the leading dimension of each C_i.**stride_c**–**[in]**[rocblas_stride] stride from the start of one C_i matrix to the next C_(i + 1).**batch_count**–**[in]**[rocblas_int] number of gemm operatons in the batch.



`gemm_strided_batched`

functions support the `_64`

interface. Only the parameter `batch_count`

larger than `(int32_t max value * 16)`

is currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xsymm + batched, strided_batched[#](#rocblas-xsymm-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ssymm([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const float *B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const float *beta, float *C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv413rocblas_ssymm14rocblas_handle12rocblas_side12rocblas_fill11rocblas_int11rocblas_intPKfPKf11rocblas_intPKf11rocblas_intPKfPf11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dsymm([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const double *B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const double *beta, double *C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv413rocblas_dsymm14rocblas_handle12rocblas_side12rocblas_fill11rocblas_int11rocblas_intPKdPKd11rocblas_intPKd11rocblas_intPKdPd11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_csymm([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv413rocblas_csymm14rocblas_handle12rocblas_side12rocblas_fill11rocblas_int11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_intPK21rocblas_float_complex11rocblas_intPK21rocblas_float_complexP21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zsymm([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv413rocblas_zsymm14rocblas_handle12rocblas_side12rocblas_fill11rocblas_int11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_intPK22rocblas_double_complex11rocblas_intPK22rocblas_double_complexP22rocblas_double_complex11rocblas_int) **BLAS Level 3 API**symm performs one of the matrix-matrix operations:

C := alpha*A*B + beta*C if side == rocblas_side_left, C := alpha*B*A + beta*C if side == rocblas_side_right, where alpha and beta are scalars, B and C are m by n matrices, and A is a symmetric matrix stored as either upper or lower.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**side**–**[in]**[rocblas_side]rocblas_side_left: C := alpha*A*B + beta*C

rocblas_side_right: C := alpha*B*A + beta*C


**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: A is an upper triangular matrix

rocblas_fill_lower: A is a lower triangular matrix


**m**–**[in]**[rocblas_int] m specifies the number of rows of B and C. m >= 0.**n**–**[in]**[rocblas_int] n specifies the number of columns of B and C. n >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A and B are not referenced.**A**–**[in]**pointer storing matrix A on the GPU.A is m by m if side == rocblas_side_left

A is n by n if side == rocblas_side_right only the upper/lower triangular part is accessed.


**lda**–**[in]**[rocblas_int] lda specifies the first dimension of A.if side = rocblas_side_left, lda >= max( 1, m ), otherwise lda >= max( 1, n ).

**B**–**[in]**pointer storing matrix B on the GPU. Matrix dimension is m by n**ldb**–**[in]**[rocblas_int] ldb specifies the first dimension of B. ldb >= max( 1, m ).**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**C**–**[in]**pointer storing matrix C on the GPU. Matrix dimension is m by n**ldc**–**[in]**[rocblas_int] ldc specifies the first dimension of C. ldc >= max( 1, m ).



The `symm`

functions support the `_64`

interface. Parameter `m`

for left side, or `n`

with right side, larger than `int32_t`

max value are not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ssymm_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const float *const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const float *beta, float *const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_ssymm_batched14rocblas_handle12rocblas_side12rocblas_fill11rocblas_int11rocblas_intPKfA_PCKf11rocblas_intA_PCKf11rocblas_intPKfA_PCf11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dsymm_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const double *const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const double *beta, double *const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_dsymm_batched14rocblas_handle12rocblas_side12rocblas_fill11rocblas_int11rocblas_intPKdA_PCKd11rocblas_intA_PCKd11rocblas_intPKdA_PCd11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_csymm_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_csymm_batched14rocblas_handle12rocblas_side12rocblas_fill11rocblas_int11rocblas_intPK21rocblas_float_complexA_PCK21rocblas_float_complex11rocblas_intA_PCK21rocblas_float_complex11rocblas_intPK21rocblas_float_complexA_PC21rocblas_float_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zsymm_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_zsymm_batched14rocblas_handle12rocblas_side12rocblas_fill11rocblas_int11rocblas_intPK22rocblas_double_complexA_PCK22rocblas_double_complex11rocblas_intA_PCK22rocblas_double_complex11rocblas_intPK22rocblas_double_complexA_PC22rocblas_double_complex11rocblas_int11rocblas_int) **BLAS Level 3 API**symm_batched performs a batch of the matrix-matrix operations:

C_i := alpha*A_i*B_i + beta*C_i if side == rocblas_side_left, C_i := alpha*B_i*A_i + beta*C_i if side == rocblas_side_right, where alpha and beta are scalars, B_i and C_i are m by n matrices, and A_i is a symmetric matrix stored as either upper or lower.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**side**–**[in]**[rocblas_side]rocblas_side_left: C_i := alpha*A_i*B_i + beta*C_i

rocblas_side_right: C_i := alpha*B_i*A_i + beta*C_i


**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: A_i is an upper triangular matrix

rocblas_fill_lower: A_i is a lower triangular matrix


**m**–**[in]**[rocblas_int] m specifies the number of rows of B_i and C_i. m >= 0.**n**–**[in]**[rocblas_int] n specifies the number of columns of B_i and C_i. n >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A_i and B_i are not referenced.**A**–**[in]**device array of device pointers storing each matrix A_i on the GPU.A_i is m by m if side == rocblas_side_left

A_i is n by n if side == rocblas_side_right only the upper/lower triangular part is accessed.


**lda**–**[in]**[rocblas_int] lda specifies the first dimension of A_i.if side = rocblas_side_left, lda >= max( 1, m ), otherwise lda >= max( 1, n ).

**B**–**[in]**device array of device pointers storing each matrix B_i on the GPU. Matrix dimension is m by n**ldb**–**[in]**[rocblas_int] ldb specifies the first dimension of B_i. ldb >= max( 1, m ).**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C_i need not be set before entry.**C**–**[in]**device array of device pointers storing each matrix C_i on the GPU. Matrix dimension is m by n.**ldc**–**[in]**[rocblas_int] ldc specifies the first dimension of C_i. ldc >= max( 1, m ).**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `symm_batched`

functions support the `_64`

interface. Parameter `m`

for left side, or `n`

with right side, larger than `int32_t`

max value are not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ssymm_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const float *B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_B, const float *beta, float *C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_ssymm_strided_batched14rocblas_handle12rocblas_side12rocblas_fill11rocblas_int11rocblas_intPKfPKf11rocblas_int14rocblas_stridePKf11rocblas_int14rocblas_stridePKfPf11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dsymm_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const double *B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_B, const double *beta, double *C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_dsymm_strided_batched14rocblas_handle12rocblas_side12rocblas_fill11rocblas_int11rocblas_intPKdPKd11rocblas_int14rocblas_stridePKd11rocblas_int14rocblas_stridePKdPd11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_csymm_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_B, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_csymm_strided_batched14rocblas_handle12rocblas_side12rocblas_fill11rocblas_int11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_int14rocblas_stridePK21rocblas_float_complex11rocblas_int14rocblas_stridePK21rocblas_float_complexP21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zsymm_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_B, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_zsymm_strided_batched14rocblas_handle12rocblas_side12rocblas_fill11rocblas_int11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_int14rocblas_stridePK22rocblas_double_complex11rocblas_int14rocblas_stridePK22rocblas_double_complexP22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_int) **BLAS Level 3 API**symm_strided_batched performs a batch of the matrix-matrix operations:

C_i := alpha*A_i*B_i + beta*C_i if side == rocblas_side_left, C_i := alpha*B_i*A_i + beta*C_i if side == rocblas_side_right, where alpha and beta are scalars, B_i and C_i are m by n matrices, and A_i is a symmetric matrix stored as either upper or lower.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**side**–**[in]**[rocblas_side]rocblas_side_left: C_i := alpha*A_i*B_i + beta*C_i

rocblas_side_right: C_i := alpha*B_i*A_i + beta*C_i


**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: A_i is an upper triangular matrix

rocblas_fill_lower: A_i is a lower triangular matrix


**m**–**[in]**[rocblas_int] m specifies the number of rows of B_i and C_i. m >= 0.**n**–**[in]**[rocblas_int] n specifies the number of columns of B_i and C_i. n >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A_i and B_i are not referenced.**A**–**[in]**device pointer to first matrix A_1A_i is m by m if side == rocblas_side_left

A_i is n by n if side == rocblas_side_right only the upper/lower triangular part is accessed.


**lda**–**[in]**[rocblas_int] lda specifies the first dimension of A_i.if side = rocblas_side_left, lda >= max( 1, m ), otherwise lda >= max( 1, n ).

**stride_A**–**[in]**[rocblas_stride] stride from the start of one matrix (A_i) and the next one (A_i+1).**B**–**[in]**device pointer to first matrix B_1 of dimension (ldb, n) on the GPU.**ldb**–**[in]**[rocblas_int] ldb specifies the first dimension of B_i. ldb >= max( 1, m ).**stride_B**–**[in]**[rocblas_stride] stride from the start of one matrix (B_i) and the next one (B_i+1).**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**C**–**[in]**device pointer to first matrix C_1 of dimension (ldc, n) on the GPU.**ldc**–**[in]**[rocblas_int] ldc specifies the first dimension of C. ldc >= max( 1, m ).**stride_C**–**[inout]**[rocblas_stride] stride from the start of one matrix (C_i) and the next one (C_i+1).**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `symm_strided_batched`

functions support the `_64`

interface. Parameter `m`

for left side, or `n`

with right side, larger than `int32_t`

max value are not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xsyrk + batched, strided_batched[#](#rocblas-xsyrk-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ssyrk([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const float *alpha, const float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const float *beta, float *C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv413rocblas_ssyrk14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPKfPKf11rocblas_intPKfPf11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dsyrk([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const double *alpha, const double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const double *beta, double *C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv413rocblas_dsyrk14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPKdPKd11rocblas_intPKdPd11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_csyrk([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv413rocblas_csyrk14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_intPK21rocblas_float_complexP21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zsyrk([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv413rocblas_zsyrk14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_intPK22rocblas_double_complexP22rocblas_double_complex11rocblas_int) **BLAS Level 3 API**syrk performs one of the matrix-matrix operations for a symmetric rank-k update:

rocblas_operation_conjugate_transpose is not supported for complex types. See cherk and zherk.C := alpha*op( A )*op( A )^T + beta*C, where alpha and beta are scalars, op(A) is an n by k matrix, and C is a symmetric n x n matrix stored as either upper or lower. op( A ) = A, and A is n by k if transA == rocblas_operation_none op( A ) = A^T and A is k by n if transA == rocblas_operation_transpose

if transA = rocblas_operation_none, lda >= max( 1, n ), otherwise lda >= max( 1, k ).

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: C is an upper triangular matrix

rocblas_fill_lower: C is a lower triangular matrix


**transA**–**[in]**[rocblas_operation]rocblas_operation_transpose: op(A) = A^T

rocblas_operation_none: op(A) = A

rocblas_operation_conjugate_transpose: op(A) = A^T


**n**–**[in]**[rocblas_int] n specifies the number of rows and columns of C. n >= 0.**k**–**[in]**[rocblas_int] k specifies the number of columns of op(A). k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A is not referenced and A need not be set before entry.**A**–**[in]**pointer storing matrix A on the GPU. Matrix dimension is ( lda, k ) when if transA = rocblas_operation_none, otherwise (lda, n)**lda**–**[in]**[rocblas_int] lda specifies the first dimension of A.**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**C**–**[in]**pointer storing matrix C on the GPU. only the upper/lower triangular part is accessed.**ldc**–**[in]**[rocblas_int] ldc specifies the first dimension of C. ldc >= max( 1, n ).



The `syrk`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ssyrk_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const float *alpha, const float *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const float *beta, float *const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_ssyrk_batched14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPKfA_PCKf11rocblas_intPKfA_PCf11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dsyrk_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const double *alpha, const double *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const double *beta, double *const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_dsyrk_batched14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPKdA_PCKd11rocblas_intPKdA_PCd11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_csyrk_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_csyrk_batched14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPK21rocblas_float_complexA_PCK21rocblas_float_complex11rocblas_intPK21rocblas_float_complexA_PC21rocblas_float_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zsyrk_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_zsyrk_batched14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPK22rocblas_double_complexA_PCK22rocblas_double_complex11rocblas_intPK22rocblas_double_complexA_PC22rocblas_double_complex11rocblas_int11rocblas_int) **BLAS Level 3 API**syrk_batched performs a batch of the matrix-matrix operations for a symmetric rank-k update:

rocblas_operation_conjugate_transpose is not supported for complex types. See cherk and zherk.C_i := alpha*op( A_i )*op( A_i )^T + beta*C_i, where alpha and beta are scalars, op(A_i) is an n by k matrix, and C_i is a symmetric n x n matrix stored as either upper or lower. op( A_i ) = A_i, and A_i is n by k if transA == rocblas_operation_none op( A_i ) = A_i^T and A_i is k by n if transA == rocblas_operation_transpose

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: C_i is an upper triangular matrix

rocblas_fill_lower: C_i is a lower triangular matrix


**transA**–**[in]**[rocblas_operation]rocblas_operation_transpose: op(A) = A^T

rocblas_operation_none: op(A) = A

rocblas_operation_conjugate_transpose: op(A) = A^T


**n**–**[in]**[rocblas_int] n specifies the number of rows and columns of C_i. n >= 0.**k**–**[in]**[rocblas_int] k specifies the number of columns of op(A). k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A is not referenced and A need not be set before entry.**A**–**[in]**device array of device pointers storing each matrix_i A of dimension (lda, k) when transA is rocblas_operation_none, otherwise of dimension (lda, n).**lda**–**[in]**[rocblas_int] lda specifies the first dimension of A_i.if transA = rocblas_operation_none, lda >= max( 1, n ), otherwise lda >= max( 1, k ).

**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**C**–**[in]**device array of device pointers storing each matrix C_i on the GPU. only the upper/lower triangular part of each C_i is accessed.**ldc**–**[in]**[rocblas_int] ldc specifies the first dimension of C. ldc >= max( 1, n ).**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `syrk_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ssyrk_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const float *alpha, const float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const float *beta, float *C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_ssyrk_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPKfPKf11rocblas_int14rocblas_stridePKfPf11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dsyrk_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const double *alpha, const double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const double *beta, double *C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_dsyrk_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPKdPKd11rocblas_int14rocblas_stridePKdPd11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_csyrk_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_csyrk_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_int14rocblas_stridePK21rocblas_float_complexP21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zsyrk_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_zsyrk_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_int14rocblas_stridePK22rocblas_double_complexP22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_int) **BLAS Level 3 API**syrk_strided_batched performs a batch of the matrix-matrix operations for a symmetric rank-k update:

rocblas_operation_conjugate_transpose is not supported for complex types. See cherk and zherk.C_i := alpha*op( A_i )*op( A_i )^T + beta*C_i, where alpha and beta are scalars, op(A_i) is an n by k matrix, and C_i is a symmetric n x n matrix stored as either upper or lower. op( A_i ) = A_i, and A_i is n by k if transA == rocblas_operation_none op( A_i ) = A_i^T and A_i is k by n if transA == rocblas_operation_transpose

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: C_i is an upper triangular matrix

rocblas_fill_lower: C_i is a lower triangular matrix


**transA**–**[in]**[rocblas_operation]rocblas_operation_transpose: op(A) = A^T

rocblas_operation_none: op(A) = A

rocblas_operation_conjugate_transpose: op(A) = A^T


**n**–**[in]**[rocblas_int] n specifies the number of rows and columns of C_i. n >= 0.**k**–**[in]**[rocblas_int] k specifies the number of columns of op(A). k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A is not referenced and A need not be set before entry.**A**–**[in]**Device pointer to the first matrix A_1 on the GPU of dimension (lda, k) when transA is rocblas_operation_none, otherwise of dimension (lda, n).**lda**–**[in]**[rocblas_int] lda specifies the first dimension of A_i.if transA = rocblas_operation_none, lda >= max( 1, n ), otherwise lda >= max( 1, k ).

**stride_A**–**[in]**[rocblas_stride] stride from the start of one matrix (A_i) and the next one (A_i+1).**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**C**–**[in]**Device pointer to the first matrix C_1 on the GPU. on the GPU. only the upper/lower triangular part of each C_i is accessed.**ldc**–**[in]**[rocblas_int] ldc specifies the first dimension of C. ldc >= max( 1, n ).**stride_C**–**[inout]**[rocblas_stride] stride from the start of one matrix (C_i) and the next one (C_i+1)**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `syrk_strided_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xsyr2k + batched, strided_batched[#](#rocblas-xsyr2k-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ssyr2k([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const float *alpha, const float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const float *B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const float *beta, float *C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv414rocblas_ssyr2k14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPKfPKf11rocblas_intPKf11rocblas_intPKfPf11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dsyr2k([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const double *alpha, const double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const double *B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const double *beta, double *C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv414rocblas_dsyr2k14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPKdPKd11rocblas_intPKd11rocblas_intPKdPd11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_csyr2k([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv414rocblas_csyr2k14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_intPK21rocblas_float_complex11rocblas_intPK21rocblas_float_complexP21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zsyr2k([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv414rocblas_zsyr2k14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_intPK22rocblas_double_complex11rocblas_intPK22rocblas_double_complexP22rocblas_double_complex11rocblas_int) **BLAS Level 3 API**syr2k performs one of the matrix-matrix operations for a symmetric rank-2k update:

rocblas_operation_conjugate_transpose is not supported for complex types in csyr2k and zsyr2k.C := alpha*(op( A )*op( B )^T + op( B )*op( A )^T) + beta*C, where alpha and beta are scalars, op(A) and op(B) are n by k matrix, and C is a symmetric n x n matrix stored as either upper or lower. op( A ) = A, op( B ) = B, and A and B are n by k if trans == rocblas_operation_none op( A ) = A^T, op( B ) = B^T, and A and B are k by n if trans == rocblas_operation_transpose or for ssyr2k and dsyr2k when trans == rocblas_operation_conjugate_transpose

if trans = rocblas_operation_none, lda >= max( 1, n ), otherwise lda >= max( 1, k ).

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: C is an upper triangular matrix

rocblas_fill_lower: C is a lower triangular matrix


**trans**–**[in]**[rocblas_operation]rocblas_operation_transpose: op( A ) = A^T, op( B ) = B^T

rocblas_operation_none: op( A ) = A, op( B ) = B

rocblas_operation_conjugate_transpose: op( A ) = A^T, op( B ) = B^T


**n**–**[in]**[rocblas_int] n specifies the number of rows and columns of C. n >= 0.**k**–**[in]**[rocblas_int] k specifies the number of columns of op(A) and op(B). k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A is not referenced and A need not be set before entry.**A**–**[in]**pointer storing matrix A on the GPU. Matrix dimension is ( lda, k ) when if trans = rocblas_operation_none, otherwise (lda, n) only the upper/lower triangular part is accessed.**lda**–**[in]**[rocblas_int] lda specifies the first dimension of A.**B**–**[in]**pointer storing matrix B on the GPU. Matrix dimension is ( ldb, k ) when if trans = rocblas_operation_none, otherwise (ldb, n) only the upper/lower triangular part is accessed.**ldb**–**[in]**[rocblas_int] ldb specifies the first dimension of B. if trans = rocblas_operation_none, ldb >= max( 1, n ), otherwise ldb >= max( 1, k ).**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**C**–**[in]**pointer storing matrix C on the GPU.**ldc**–**[in]**[rocblas_int] ldc specifies the first dimension of C. ldc >= max( 1, n ).



The `syr2k`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ssyr2k_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const float *alpha, const float *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const float *const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const float *beta, float *const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv422rocblas_ssyr2k_batched14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPKfA_PCKf11rocblas_intA_PCKf11rocblas_intPKfA_PCf11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dsyr2k_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const double *alpha, const double *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const double *const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const double *beta, double *const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv422rocblas_dsyr2k_batched14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPKdA_PCKd11rocblas_intA_PCKd11rocblas_intPKdA_PCd11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_csyr2k_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv422rocblas_csyr2k_batched14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPK21rocblas_float_complexA_PCK21rocblas_float_complex11rocblas_intA_PCK21rocblas_float_complex11rocblas_intPK21rocblas_float_complexA_PC21rocblas_float_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zsyr2k_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv422rocblas_zsyr2k_batched14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPK22rocblas_double_complexA_PCK22rocblas_double_complex11rocblas_intA_PCK22rocblas_double_complex11rocblas_intPK22rocblas_double_complexA_PC22rocblas_double_complex11rocblas_int11rocblas_int) **BLAS Level 3 API**syr2k_batched performs a batch of the matrix-matrix operations for a symmetric rank-2k update:

rocblas_operation_conjugate_transpose is not supported for complex types in csyr2k_batched and zsyr2k_batched.C_i := alpha*(op( A_i )*op( B_i )^T + op( B_i )*op( A_i )^T) + beta*C_i, where alpha and beta are scalars, op(A_i) and op(B_i) are n by k matrix, and C_i is a symmetric n x n matrix stored as either upper or lower. op( A_i ) = A_i, op( B_i ) = B_i, and A_i and B_i are n by k if trans == rocblas_operation_none op( A_i ) = A_i^T, op( B_i ) = B_i^T, and A_i and B_i are k by n if trans == rocblas_operation_transpose or for ssyr2k_batched and dsyr2k_batched when trans == rocblas_operation_conjugate_transpose

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: C_i is an upper triangular matrix

rocblas_fill_lower: C_i is a lower triangular matrix


**trans**–**[in]**[rocblas_operation]rocblas_operation_transpose: op( A_i ) = A_i^T, op( B_i ) = B_i^T

rocblas_operation_none: op( A_i ) = A_i, op( B_i ) = B_i

rocblas_operation_conjugate_transpose: op( A_i ) = A_i^T, op( B_i ) = B_i^T


**n**–**[in]**[rocblas_int] n specifies the number of rows and columns of C_i. n >= 0.**k**–**[in]**[rocblas_int] k specifies the number of columns of op(A). k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A is not referenced and A need not be set before entry.**A**–**[in]**device array of device pointers storing each matrix_i A of dimension (lda, k) when trans is rocblas_operation_none, otherwise of dimension (lda, n).**lda**–**[in]**[rocblas_int] lda specifies the first dimension of A_i. if trans = rocblas_operation_none, lda >= max( 1, n ), otherwise lda >= max( 1, k ).**B**–**[in]**device array of device pointers storing each matrix_i B of dimension (ldb, k) when trans is rocblas_operation_none, otherwise of dimension (ldb, n).**ldb**–**[in]**[rocblas_int] ldb specifies the first dimension of B.if trans = rocblas_operation_none, ldb >= max( 1, n ), otherwise ldb >= max( 1, k ).

**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**C**–**[in]**device array of device pointers storing each matrix C_i on the GPU.**ldc**–**[in]**[rocblas_int] ldc specifies the first dimension of C. ldc >= max( 1, n ).**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `syr2k_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ssyr2k_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const float *alpha, const float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const float *B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_B, const float *beta, float *C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv430rocblas_ssyr2k_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPKfPKf11rocblas_int14rocblas_stridePKf11rocblas_int14rocblas_stridePKfPf11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dsyr2k_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const double *alpha, const double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const double *B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_B, const double *beta, double *C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv430rocblas_dsyr2k_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPKdPKd11rocblas_int14rocblas_stridePKd11rocblas_int14rocblas_stridePKdPd11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_csyr2k_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_B, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv430rocblas_csyr2k_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_int14rocblas_stridePK21rocblas_float_complex11rocblas_int14rocblas_stridePK21rocblas_float_complexP21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zsyr2k_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_B, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv430rocblas_zsyr2k_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_int14rocblas_stridePK22rocblas_double_complex11rocblas_int14rocblas_stridePK22rocblas_double_complexP22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_int) **BLAS Level 3 API**syr2k_strided_batched performs a batch of the matrix-matrix operations for a symmetric rank-2k update:

rocblas_operation_conjugate_transpose is not supported for complex types in csyr2k_strided_batched and zsyr2k_strided_batched.C_i := alpha*(op( A_i )*op( B_i )^T + op( B_i )*op( A_i )^T) + beta*C_i, where alpha and beta are scalars, op(A_i) and op(B_i) are n by k matrix, and C_i is a symmetric n x n matrix stored as either upper or lower. op( A_i ) = A_i, op( B_i ) = B_i, and A_i and B_i are n by k if trans == rocblas_operation_none op( A_i ) = A_i^T, op( B_i ) = B_i^T, and A_i and B_i are k by n if trans == rocblas_operation_transpose or for ssyr2k_strided_batched and dsyr2k_strided_batched when trans == rocblas_operation_conjugate_transpose

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: C_i is an upper triangular matrix

rocblas_fill_lower: C_i is a lower triangular matrix


**trans**–**[in]**[rocblas_operation]rocblas_operation_transpose: op( A_i ) = A_i^T, op( B_i ) = B_i^T

rocblas_operation_none: op( A_i ) = A_i, op( B_i ) = B_i

rocblas_operation_conjugate_transpose: op( A_i ) = A_i^T, op( B_i ) = B_i^T


**n**–**[in]**[rocblas_int] n specifies the number of rows and columns of C_i. n >= 0.**k**–**[in]**[rocblas_int] k specifies the number of columns of op(A). k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A is not referenced and A need not be set before entry.**A**–**[in]**Device pointer to the first matrix A_1 on the GPU of dimension (lda, k) when trans is rocblas_operation_none, otherwise of dimension (lda, n).**lda**–**[in]**[rocblas_int] lda specifies the first dimension of A_i.if trans = rocblas_operation_none, lda >= max( 1, n ), otherwise lda >= max( 1, k ).

**stride_A**–**[in]**[rocblas_stride] stride from the start of one matrix (A_i) and the next one (A_i+1)**B**–**[in]**Device pointer to the first matrix B_1 on the GPU of dimension (ldb, k) when trans is rocblas_operation_none, otherwise of dimension (ldb, n)**ldb**–**[in]**[rocblas_int] ldb specifies the first dimension of B_i.if trans = rocblas_operation_none, ldb >= max( 1, n ), otherwise ldb >= max( 1, k ).

**stride_B**–**[in]**[rocblas_stride] stride from the start of one matrix (B_i) and the next one (B_i+1)**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**C**–**[in]**Device pointer to the first matrix C_1 on the GPU.**ldc**–**[in]**[rocblas_int] ldc specifies the first dimension of C. ldc >= max( 1, n ).**stride_C**–**[inout]**[rocblas_stride] stride from the start of one matrix (C_i) and the next one (C_i+1).**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `syr2k_strided_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xsyrkx + batched, strided_batched[#](#rocblas-xsyrkx-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ssyrkx([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const float *alpha, const float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const float *B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const float *beta, float *C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv414rocblas_ssyrkx14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPKfPKf11rocblas_intPKf11rocblas_intPKfPf11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dsyrkx([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const double *alpha, const double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const double *B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const double *beta, double *C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv414rocblas_dsyrkx14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPKdPKd11rocblas_intPKd11rocblas_intPKdPd11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_csyrkx([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv414rocblas_csyrkx14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_intPK21rocblas_float_complex11rocblas_intPK21rocblas_float_complexP21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zsyrkx([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv414rocblas_zsyrkx14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_intPK22rocblas_double_complex11rocblas_intPK22rocblas_double_complexP22rocblas_double_complex11rocblas_int) **BLAS Level 3 API**syrkx performs one of the matrix-matrix operations for a symmetric rank-k update:

This routine should only be used when the caller can guarantee that the result of op( A )*op( B )^T will be symmetric.C := alpha*op( A )*op( B )^T + beta*C, where alpha and beta are scalars, op(A) and op(B) are n by k matrix, and C is a symmetric n x n matrix stored as either upper or lower.

rocblas_operation_conjugate_transpose is not supported for complex types in csyrkx and zsyrkx.op( A ) = A, op( B ) = B, and A and B are n by k if trans == rocblas_operation_none op( A ) = A^T, op( B ) = B^T, and A and B are k by n if trans == rocblas_operation_transpose or for ssyrkx and dsyrkx when trans == rocblas_operation_conjugate_transpose

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: C is an upper triangular matrix

rocblas_fill_lower: C is a lower triangular matrix


**trans**–**[in]**[rocblas_operation]rocblas_operation_transpose: op( A ) = A^T, op( B ) = B^T

rocblas_operation_none: op( A ) = A, op( B ) = B

rocblas_operation_conjugate_transpose: op( A ) = A^T, op( B ) = B^T


**n**–**[in]**[rocblas_int] n specifies the number of rows and columns of C. n >= 0.**k**–**[in]**[rocblas_int] k specifies the number of columns of op(A) and op(B). k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A is not referenced and A need not be set before entry.**A**–**[in]**pointer storing matrix A on the GPU. Matrix dimension is ( lda, k ) when if trans = rocblas_operation_none, otherwise (lda, n)**lda**–**[in]**[rocblas_int] lda specifies the first dimension of A.if trans = rocblas_operation_none, lda >= max( 1, n ), otherwise lda >= max( 1, k ).

**B**–**[in]**pointer storing matrix B on the GPU. Matrix dimension is ( ldb, k ) when if trans = rocblas_operation_none, otherwise (ldb, n)**ldb**–**[in]**[rocblas_int] ldb specifies the first dimension of B.if trans = rocblas_operation_none, ldb >= max( 1, n ), otherwise ldb >= max( 1, k ).

**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**C**–**[in]**pointer storing matrix C on the GPU. only the upper/lower triangular part is accessed.**ldc**–**[in]**[rocblas_int] ldc specifies the first dimension of C. ldc >= max( 1, n ).



The `syrkx`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ssyrkx_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const float *alpha, const float *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const float *const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const float *beta, float *const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv422rocblas_ssyrkx_batched14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPKfA_PCKf11rocblas_intA_PCKf11rocblas_intPKfA_PCf11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dsyrkx_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const double *alpha, const double *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const double *const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const double *beta, double *const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv422rocblas_dsyrkx_batched14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPKdA_PCKd11rocblas_intA_PCKd11rocblas_intPKdA_PCd11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_csyrkx_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv422rocblas_csyrkx_batched14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPK21rocblas_float_complexA_PCK21rocblas_float_complex11rocblas_intA_PCK21rocblas_float_complex11rocblas_intPK21rocblas_float_complexA_PC21rocblas_float_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zsyrkx_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv422rocblas_zsyrkx_batched14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPK22rocblas_double_complexA_PCK22rocblas_double_complex11rocblas_intA_PCK22rocblas_double_complex11rocblas_intPK22rocblas_double_complexA_PC22rocblas_double_complex11rocblas_int11rocblas_int) **BLAS Level 3 API**syrkx_batched performs a batch of the matrix-matrix operations for a symmetric rank-k update:

This routine should only be used when the caller can guarantee that the result of op( A_i )*op( B_i )^T will be symmetric.C_i := alpha*op( A_i )*op( B_i )^T + beta*C_i, where alpha and beta are scalars, op(A_i) and op(B_i) are n by k matrix, and C_i is a symmetric n x n matrix stored as either upper or lower.

rocblas_operation_conjugate_transpose is not supported for complex types in csyrkx_batched and zsyrkx_batched.op( A_i ) = A_i, op( B_i ) = B_i, and A_i and B_i are n by k if trans == rocblas_operation_none op( A_i ) = A_i^T, op( B_i ) = B_i^T, and A_i and B_i are k by n if trans == rocblas_operation_transpose or for ssyrkx_batched and dsyrkx_batched when trans == rocblas_operation_conjugate_transpose

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: C_i is an upper triangular matrix

rocblas_fill_lower: C_i is a lower triangular matrix


**trans**–**[in]**[rocblas_operation]rocblas_operation_transpose: op( A_i ) = A_i^T, op( B_i ) = B_i^T

rocblas_operation_none: op( A_i ) = A_i, op( B_i ) = B_i

rocblas_operation_conjugate_transpose: op( A_i ) = A_i^T, op( B_i ) = B_i^T


**n**–**[in]**[rocblas_int] n specifies the number of rows and columns of C_i. n >= 0.**k**–**[in]**[rocblas_int] k specifies the number of columns of op(A). k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A is not referenced and A need not be set before entry.**A**–**[in]**device array of device pointers storing each matrix_i A of dimension (lda, k) when trans is rocblas_operation_none, otherwise of dimension (lda, n)**lda**–**[in]**[rocblas_int] lda specifies the first dimension of A_i.if trans = rocblas_operation_none, lda >= max( 1, n ), otherwise lda >= max( 1, k ).

**B**–**[in]**device array of device pointers storing each matrix_i B of dimension (ldb, k) when trans is rocblas_operation_none, otherwise of dimension (ldb, n)**ldb**–**[in]**[rocblas_int] ldb specifies the first dimension of B.if trans = rocblas_operation_none, ldb >= max( 1, n ), otherwise ldb >= max( 1, k ).

**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**C**–**[in]**device array of device pointers storing each matrix C_i on the GPU. only the upper/lower triangular part of each C_i is accessed.**ldc**–**[in]**[rocblas_int] ldc specifies the first dimension of C. ldc >= max( 1, n ).**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `syrkx_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ssyrkx_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const float *alpha, const float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const float *B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_B, const float *beta, float *C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv430rocblas_ssyrkx_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPKfPKf11rocblas_int14rocblas_stridePKf11rocblas_int14rocblas_stridePKfPf11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dsyrkx_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const double *alpha, const double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const double *B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_B, const double *beta, double *C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv430rocblas_dsyrkx_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPKdPKd11rocblas_int14rocblas_stridePKd11rocblas_int14rocblas_stridePKdPd11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_csyrkx_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_B, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv430rocblas_csyrkx_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_int14rocblas_stridePK21rocblas_float_complex11rocblas_int14rocblas_stridePK21rocblas_float_complexP21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zsyrkx_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_B, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv430rocblas_zsyrkx_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_int14rocblas_stridePK22rocblas_double_complex11rocblas_int14rocblas_stridePK22rocblas_double_complexP22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_int) **BLAS Level 3 API**syrkx_strided_batched performs a batch of the matrix-matrix operations for a symmetric rank-k update:

This routine should only be used when the caller can guarantee that the result of op( A_i )*op( B_i )^T will be symmetric.C_i := alpha*op( A_i )*op( B_i )^T + beta*C_i, where alpha and beta are scalars, op(A_i) and op(B_i) are n by k matrix, and C_i is a symmetric n x n matrix stored as either upper or lower.

rocblas_operation_conjugate_transpose is not supported for complex types in csyrkx_strided_batched and zsyrkx_strided_batched.op( A_i ) = A_i, op( B_i ) = B_i, and A_i and B_i are n by k if trans == rocblas_operation_none op( A_i ) = A_i^T, op( B_i ) = B_i^T, and A_i and B_i are k by n if trans == rocblas_operation_transpose or for ssyrkx_strided_batched and dsyrkx_strided_batched when trans == rocblas_operation_conjugate_transpose

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: C_i is an upper triangular matrix

rocblas_fill_lower: C_i is a lower triangular matrix


**trans**–**[in]**[rocblas_operation]rocblas_operation_transpose: op( A_i ) = A_i^T, op( B_i ) = B_i^T

rocblas_operation_none: op( A_i ) = A_i, op( B_i ) = B_i

rocblas_operation_conjugate_transpose: op( A_i ) = A_i^T, op( B_i ) = B_i^T


**n**–**[in]**[rocblas_int] n specifies the number of rows and columns of C_i. n >= 0.**k**–**[in]**[rocblas_int] k specifies the number of columns of op(A). k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A is not referenced and A need not be set before entry.**A**–**[in]**Device pointer to the first matrix A_1 on the GPU of dimension (lda, k) when trans is rocblas_operation_none, otherwise of dimension (lda, n)**lda**–**[in]**[rocblas_int] lda specifies the first dimension of A_i.if trans = rocblas_operation_none, lda >= max( 1, n ), otherwise lda >= max( 1, k ).

**stride_A**–**[in]**[rocblas_stride] stride from the start of one matrix (A_i) and the next one (A_i+1).**B**–**[in]**Device pointer to the first matrix B_1 on the GPU of dimension (ldb, k) when trans is rocblas_operation_none, otherwise of dimension (ldb, n).**ldb**–**[in]**[rocblas_int] ldb specifies the first dimension of B_i.if trans = rocblas_operation_none, ldb >= max( 1, n ), otherwise ldb >= max( 1, k ).

**stride_B**–**[in]**[rocblas_stride] stride from the start of one matrix (B_i) and the next one (B_i+1).**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**C**–**[in]**Device pointer to the first matrix C_1 on the GPU. only the upper/lower triangular part of each C_i is accessed.**ldc**–**[in]**[rocblas_int] ldc specifies the first dimension of C. ldc >= max( 1, n ).**stride_C**–**[inout]**[rocblas_stride] stride from the start of one matrix (C_i) and the next one (C_i+1).**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `syrkx_strided_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xtrmm + batched, strided_batched[#](#rocblas-xtrmm-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_strmm([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const float *B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, float *C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv413rocblas_strmm14rocblas_handle12rocblas_side12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPKfPKf11rocblas_intPKf11rocblas_intPf11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dtrmm([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const double *B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, double *C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv413rocblas_dtrmm14rocblas_handle12rocblas_side12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPKdPKd11rocblas_intPKd11rocblas_intPd11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ctrmm([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv413rocblas_ctrmm14rocblas_handle12rocblas_side12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_intPK21rocblas_float_complex11rocblas_intP21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ztrmm([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv413rocblas_ztrmm14rocblas_handle12rocblas_side12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_intPK22rocblas_double_complex11rocblas_intP22rocblas_double_complex11rocblas_int) **BLAS Level 3 API**trmm performs one of the matrix-matrix operations:

The Legacy BLAS in-place trmm functionality,C := alpha*op( A )*B, or C := alpha*B*op( A ),

is available by setting pointer C equal to pointer B, and ldc equal to ldb.B := alpha*op( A )*B, or B := alpha*B*op( A ),

alpha is a scalar, B is an m by n matrix, C is an m by n matrix, A is a unit, or non-unit, upper or lower triangular matrix and op( A ) is one of op( A ) = A or op( A ) = A^T or op( A ) = A^H. When uplo == rocblas_fill_upper the leading k by k upper triangular part of the array A must contain the upper triangular matrix and the strictly lower triangular part of A is not referenced. Here k is m when side == rocblas_side_left and is n when side == rocblas_side_right. When uplo == rocblas_fill_lower the leading k by k lower triangular part of the array A must contain the lower triangular matrix and the strictly upper triangular part of A is not referenced. Here k is m when side == rocblas_side_left and is n when side == rocblas_side_right. Note that when diag == rocblas_diagonal_unit the diagonal elements of A are not referenced either, but are assumed to be unity.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**side**–**[in]**[rocblas_side] Specifies whether op(A) multiplies B from the left or right as follows:rocblas_side_left: C := alpha*op( A )*B

rocblas_side_right: C := alpha*B*op( A )


**uplo**–**[in]**[rocblas_fill] Specifies whether the matrix A is an upper or lower triangular matrix as follows:rocblas_fill_upper: A is an upper triangular matrix.

rocblas_fill_lower: A is a lower triangular matrix.


**transA**–**[in]**[rocblas_operation] Specifies the form of op(A) to be used in the matrix multiplication as follows:rocblas_operation_none: op(A) = A

rocblas_operation_transpose: op(A) = A^T

rocblas_operation_conjugate_transpose: op(A) = A^H


**diag**–**[in]**[rocblas_diagonal] Specifies whether or not A is unit triangular as follows:rocblas_diagonal_unit: A is assumed to be unit triangular.

rocblas_diagonal_non_unit: A is not assumed to be unit triangular.


**m**–**[in]**[rocblas_int] m specifies the number of rows of B. m >= 0.**n**–**[in]**[rocblas_int] n specifies the number of columns of B. n >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A is not referenced and B need not be set before entry.**A**–**[in]**Device pointer to matrix A on the GPU. A has dimension ( lda, k ), where k is m when side == rocblas_side_left and is n when side == rocblas_side_right.Note that when diag == rocblas_diagonal_unit the diagonal elements of A are not referenced either, but are assumed to be unity.When uplo == rocblas_fill_upper the leading k by k upper triangular part of the array A must contain the upper triangular matrix and the strictly lower triangular part of A is not referenced. When uplo == rocblas_fill_lower the leading k by k lower triangular part of the array A must contain the lower triangular matrix and the strictly upper triangular part of A is not referenced.

**lda**–**[in]**[rocblas_int] lda specifies the first dimension of A.if side == rocblas_side_left, lda >= max( 1, m ), if side == rocblas_side_right, lda >= max( 1, n ).

**B**–**[in]**Device pointer to the matrix B on the GPU.**ldb**–**[in]**[rocblas_int] ldb specifies the first dimension of B. ldb >= max( 1, m ).**C**–**[out]**Device pointer to the matrix C on the GPU.**ldc**–**[in]**[rocblas_int] ldc specifies the first dimension of C. ldc >= max( 1, m). If B and C are pointers to the same matrix then ldc must equal ldb or rocblas_status_invalid_value will be returned.



The `trmm`

functions support the `_64`

interface. Parameter `m`

for left side, or `n`

with right side, larger than `2^28`

not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_strmm_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const float *const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, float *const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_strmm_batched14rocblas_handle12rocblas_side12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPKfA_PCKf11rocblas_intA_PCKf11rocblas_intA_PCf11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dtrmm_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const double *const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, double *const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_dtrmm_batched14rocblas_handle12rocblas_side12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPKdA_PCKd11rocblas_intA_PCKd11rocblas_intA_PCd11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ctrmm_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_ctrmm_batched14rocblas_handle12rocblas_side12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPK21rocblas_float_complexA_PCK21rocblas_float_complex11rocblas_intA_PCK21rocblas_float_complex11rocblas_intA_PC21rocblas_float_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ztrmm_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_ztrmm_batched14rocblas_handle12rocblas_side12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPK22rocblas_double_complexA_PCK22rocblas_double_complex11rocblas_intA_PCK22rocblas_double_complex11rocblas_intA_PC22rocblas_double_complex11rocblas_int11rocblas_int) **BLAS Level 3 API**trmm_batched performs one of the matrix-matrix operations:

The Legacy BLAS in-place trmm_batched functionality,C_i := alpha*op( A_i )*B_i, or C_i := alpha*B_i*op( A_i ) for i = 0, 1, ... batch_count -1,

is available by setting pointer C equal to pointer B and ldc equal to ldb.B_i := alpha*op( A_i )*B_i, or B_i := alpha*B_i*op( A_i ) for i = 0, 1, ... batch_count -1,

When uplo == rocblas_fill_upper the leading k by k upper triangular part of the array A must contain the upper triangular matrix and the strictly lower triangular part of A is not referenced.alpha is a scalar, B_i is an m by n matrix, C_i is an m by n matrix, A_i is a unit, or non-unit, upper or lower triangular matrix and op( A_i ) is one of op( A_i ) = A_i or op( A_i ) = A_i^T or op( A_i ) = A_i^H. When uplo == rocblas_fill_upper the leading k by k upper triangular part of the array A must contain the upper triangular matrix and the strictly lower triangular part of A is not referenced. Here k is m when side == rocblas_side_left and is n when side == rocblas_side_right. When uplo == rocblas_fill_lower the leading k by k lower triangular part of the array A must contain the lower triangular matrix and the strictly upper triangular part of A is not referenced. Here k is m when side == rocblas_side_left and is n when side == rocblas_side_right. Note that when diag == rocblas_diagonal_unit the diagonal elements of A are not referenced either, but are assumed to be unity.

When uplo == rocblas_fill_lower the leading k by k lower triangular part of the array A must contain the lower triangular matrix and the strictly upper triangular part of A is not referenced.

Note that when diag == rocblas_diagonal_unit the diagonal elements of A_i are not referenced either, but are assumed to be unity.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**side**–**[in]**[rocblas_side] Specifies whether op(A_i) multiplies B_i from the left or right as follows:rocblas_side_left: C_i := alpha*op( A_i )*B_i

rocblas_side_right: C_i := alpha*B_i*op( A_i )


**uplo**–**[in]**[rocblas_fill] Specifies whether the matrix A is an upper or lower triangular matrix as follows:rocblas_fill_upper: A is an upper triangular matrix.

rocblas_fill_lower: A is a lower triangular matrix.


**transA**–**[in]**[rocblas_operation] Specifies the form of op(A_i) to be used in the matrix multiplication as follows:rocblas_operation_none: op(A_i) = A_i

rocblas_operation_transpose: op(A_i) = A_i^T

rocblas_operation_conjugate_transpose: op(A_i) = A_i^H


**diag**–**[in]**[rocblas_diagonal] Specifies whether or not A_i is unit triangular as follows:rocblas_diagonal_unit: A_i is assumed to be unit triangular.

rocblas_diagonal_non_unit: A_i is not assumed to be unit triangular.


**m**–**[in]**[rocblas_int] m specifies the number of rows of B_i. m >= 0.**n**–**[in]**[rocblas_int] n specifies the number of columns of B_i. n >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A_i is not referenced and B_i need not be set before entry.**A**–**[in]**Device array of device pointers storing each matrix A_i on the GPU. Each A_i is of dimension ( lda, k ), where k is m when side == rocblas_side_left and is n when side == rocblas_side_right.**lda**–**[in]**[rocblas_int] lda specifies the first dimension of A.if side == rocblas_side_left, lda >= max( 1, m ), if side == rocblas_side_right, lda >= max( 1, n ).

**B**–**[in]**device array of device pointers storing each matrix B_i on the GPU.**ldb**–**[in]**[rocblas_int] ldb specifies the first dimension of B_i. ldb >= max( 1, m ).**C**–**[out]**device array of device pointers storing each matrix C_i on the GPU.**ldc**–**[in]**[rocblas_int] ldc specifies the first dimension of C. ldc >= max( 1, m). If B and C are pointers to the same array of pointers then ldc must equal ldb or rocblas_status_invalid_value will be returned.**batch_count**–**[in]**[rocblas_int] number of instances i in the batch.



The `trmm_batched`

functions support the `_64`

interface. Parameter `m`

for left side, or `n`

with right side, larger than `2^28`

are not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_strmm_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const float *B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_B, float *C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_strmm_strided_batched14rocblas_handle12rocblas_side12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPKfPKf11rocblas_int14rocblas_stridePKf11rocblas_int14rocblas_stridePf11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dtrmm_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const double *B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_B, double *C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_dtrmm_strided_batched14rocblas_handle12rocblas_side12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPKdPKd11rocblas_int14rocblas_stridePKd11rocblas_int14rocblas_stridePd11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ctrmm_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_B,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_ctrmm_strided_batched14rocblas_handle12rocblas_side12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_int14rocblas_stridePK21rocblas_float_complex11rocblas_int14rocblas_strideP21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ztrmm_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_B,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_ztrmm_strided_batched14rocblas_handle12rocblas_side12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_int14rocblas_stridePK22rocblas_double_complex11rocblas_int14rocblas_strideP22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_int) **BLAS Level 3 API**trmm_strided_batched performs one of the matrix-matrix operations:

The Legacy BLAS in-place trmm_strided_batched functionality,C_i := alpha*op( A_i )*B_i, or C_i := alpha*B_i*op( A_i ) for i = 0, 1, ... batch_count -1,

is available by setting pointer C equal to pointer B, ldc equal to ldb, and stride_C equal to stride_B.B_i := alpha*op( A_i )*B_i, or B_i := alpha*B_i*op( A_i ) for i = 0, 1, ... batch_count -1,

When uplo == rocblas_fill_upper the leading k by k upper triangular part of the array A must contain the upper triangular matrix and the strictly lower triangular part of A is not referenced.alpha is a scalar, B_i is an m by n matrix, C_i is an m by n matrix, A_i is a unit, or non-unit, upper or lower triangular matrix and op( A_i ) is one of op( A_i ) = A_i or op( A_i ) = A_i^T or op( A_i ) = A_i^H. When uplo == rocblas_fill_upper the leading k by k upper triangular part of the array A must contain the upper triangular matrix and the strictly lower triangular part of A is not referenced. Here k is m when side == rocblas_side_left and is n when side == rocblas_side_right. When uplo == rocblas_fill_lower the leading k by k lower triangular part of the array A must contain the lower triangular matrix and the strictly upper triangular part of A is not referenced. Here k is m when side == rocblas_side_left and is n when side == rocblas_side_right. Note that when diag == rocblas_diagonal_unit the diagonal elements of A are not referenced either, but are assumed to be unity.

When uplo == rocblas_fill_lower the leading k by k lower triangular part of the array A must contain the lower triangular matrix and the strictly upper triangular part of A is not referenced.

Note that when diag == rocblas_diagonal_unit the diagonal elements of A_i are not referenced either, but are assumed to be unity.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**side**–**[in]**[rocblas_side] Specifies whether op(A_i) multiplies B_i from the left or right as follows:rocblas_side_left: C_i := alpha*op( A_i )*B_i

rocblas_side_right: C_i := alpha*B_i*op( A_i )


**uplo**–**[in]**[rocblas_fill] Specifies whether the matrix A is an upper or lower triangular matrix as follows:rocblas_fill_upper: A is an upper triangular matrix.

rocblas_fill_lower: A is a lower triangular matrix.


**transA**–**[in]**[rocblas_operation] Specifies the form of op(A_i) to be used in the matrix multiplication as follows:rocblas_operation_none: op(A_i) = A_i

rocblas_operation_transpose: op(A_i) = A_i^T

rocblas_operation_conjugate_transpose: op(A_i) = A_i^H


**diag**–**[in]**[rocblas_diagonal] Specifies whether or not A_i is unit triangular as follows:rocblas_diagonal_unit: A_i is assumed to be unit triangular.

rocblas_diagonal_non_unit: A_i is not assumed to be unit triangular.


**m**–**[in]**[rocblas_int] m specifies the number of rows of B_i. m >= 0.**n**–**[in]**[rocblas_int] n specifies the number of columns of B_i. n >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A_i is not referenced and B_i need not be set before entry.**A**–**[in]**Device pointer to the first matrix A_0 on the GPU. Each A_i is of dimension ( lda, k ), where k is m when side == rocblas_side_left and is n when side == rocblas_side_right.**lda**–**[in]**[rocblas_int] lda specifies the first dimension of A.if side == rocblas_side_left, lda >= max( 1, m ), if side == rocblas_side_right, lda >= max( 1, n ).

**stride_A**–**[in]**[rocblas_stride] stride from the start of one matrix (A_i) and the next one (A_i+1).**B**–**[in]**Device pointer to the first matrix B_0 on the GPU.**ldb**–**[in]**[rocblas_int] ldb specifies the first dimension of B_i. ldb >= max( 1, m ).**stride_B**–**[in]**[rocblas_stride] stride from the start of one matrix (B_i) and the next one (B_i+1).**C**–**[out]**Device pointer to the first matrix C_0 on the GPU.**ldc**–**[in]**[rocblas_int] ldc specifies the first dimension of C_i. ldc >= max( 1, m). If B and C pointers are to the same matrix then ldc must equal ldb or rocblas_status_invalid_size will be returned.**stride_C**–**[in]**[rocblas_stride] stride from the start of one matrix (C_i) and the next one (C_i+1). If B == C and ldb == ldc then stride_C should equal stride_B or behavior is undefined.**batch_count**–**[in]**[rocblas_int] number of instances i in the batch.



The `trmm_strided_batched`

functions support the `_64`

interface. Parameter `m`

for left side, or `n`

with right side, larger than `2^28`

are not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xtrsm + batched, strided_batched[#](#rocblas-xtrsm-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_strsm([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, float *B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb)[#](#_CPPv413rocblas_strsm14rocblas_handle12rocblas_side12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPKfPKf11rocblas_intPf11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dtrsm([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, double *B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb)[#](#_CPPv413rocblas_dtrsm14rocblas_handle12rocblas_side12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPKdPKd11rocblas_intPd11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ctrsm([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb)[#](#_CPPv413rocblas_ctrsm14rocblas_handle12rocblas_side12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_intP21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ztrsm([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb)[#](#_CPPv413rocblas_ztrsm14rocblas_handle12rocblas_side12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_intP22rocblas_double_complex11rocblas_int) **BLAS Level 3 API**trsm solves:

Note about memory allocation: When trsm is launched with a k evenly divisible by the internal block size of 128, and is no larger than 10 of these blocks, the API takes advantage of utilizing pre-allocated memory found in the handle to increase overall performance (where k is m when rocblas_side_left and is n when rocblas_side_right).op(A)*X = alpha*B or X*op(A) = alpha*B, where alpha is a scalar, X and B are m by n matrices, A is triangular matrix and op(A) is one of op( A ) = A or op( A ) = A^T or op( A ) = A^H. The matrix X is overwritten on B.

Although not widespread, some gemm kernels used by trsm may use atomic operations. See Atomic Operations in the API Reference Guide for more information.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**side**–**[in]**[rocblas_side]rocblas_side_left: op(A)*X = alpha*B

rocblas_side_right: X*op(A) = alpha*B


**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: A is an upper triangular matrix.

rocblas_fill_lower: A is a lower triangular matrix.


**transA**–**[in]**[rocblas_operation]transB: op(A) = A.

rocblas_operation_transpose: op(A) = A^T

rocblas_operation_conjugate_transpose: op(A) = A^H


**diag**–**[in]**[rocblas_diagonal]rocblas_diagonal_unit: A is assumed to be unit triangular.

rocblas_diagonal_non_unit: A is not assumed to be unit triangular.


**m**–**[in]**[rocblas_int] m specifies the number of rows of B. m >= 0.**n**–**[in]**[rocblas_int] n specifies the number of columns of B. n >= 0.**alpha**–**[in]**device pointer or host pointer specifying the scalar alpha. When alpha is &zero then A is not referenced and B need not be set before entry.**A**–**[in]**device pointer storing matrix A. of dimension ( lda, k ), where k is m when rocblas_side_left and is n when rocblas_side_right only the upper/lower triangular part is accessed.**lda**–**[in]**[rocblas_int] lda specifies the first dimension of A.if side = rocblas_side_left, lda >= max( 1, m ), if side = rocblas_side_right, lda >= max( 1, n ).

**B**–**[inout]**device pointer storing matrix B.**ldb**–**[in]**[rocblas_int] ldb specifies the first dimension of B. ldb >= max( 1, m ).



The `trsm`

functions support the `_64`

interface. Parameter `m`

for left side, or `n`

with right side, larger than `int32_t`

max value are not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

For more information on pre-allocated memory in the handle, see the
[Device Memory Allocation](memory-alloc.html#device-memory-allocation-usage).

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_strsm_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, float *const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_strsm_batched14rocblas_handle12rocblas_side12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPKfA_PCKf11rocblas_intA_PCf11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dtrsm_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, double *const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_dtrsm_batched14rocblas_handle12rocblas_side12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPKdA_PCKd11rocblas_intA_PCd11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ctrsm_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_ctrsm_batched14rocblas_handle12rocblas_side12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPK21rocblas_float_complexA_PCK21rocblas_float_complex11rocblas_intA_PC21rocblas_float_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ztrsm_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_ztrsm_batched14rocblas_handle12rocblas_side12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPK22rocblas_double_complexA_PCK22rocblas_double_complex11rocblas_intA_PC22rocblas_double_complex11rocblas_int11rocblas_int) **BLAS Level 3 API**trsm_batched performs the following batched operation:

Note about memory allocation: When trsm is launched with a k evenly divisible by the internal block size of 128, and is no larger than 10 of these blocks, the API takes advantage of utilizing pre-allocated memory found in the handle to increase overall performance (where k is m when rocblas_side_left and is n when rocblas_side_right).op(A_i)*X_i = alpha*B_i or X_i*op(A_i) = alpha*B_i, for i = 1, ..., batch_count, where alpha is a scalar, X and B are batched m by n matrices, A is triangular batched matrix and op(A) is one of op( A ) = A or op( A ) = A^T or op( A ) = A^H. Each matrix X_i is overwritten on B_i for i = 1, ..., batch_count.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**side**–**[in]**[rocblas_side]rocblas_side_left: op(A)*X = alpha*B

rocblas_side_right: X*op(A) = alpha*B


**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: each A_i is an upper triangular matrix.

rocblas_fill_lower: each A_i is a lower triangular matrix.


**transA**–**[in]**[rocblas_operation]transB: op(A) = A

rocblas_operation_transpose: op(A) = A^T

rocblas_operation_conjugate_transpose: op(A) = A^H


**diag**–**[in]**[rocblas_diagonal]rocblas_diagonal_unit: each A_i is assumed to be unit triangular.

rocblas_diagonal_non_unit: each A_i is not assumed to be unit triangular.


**m**–**[in]**[rocblas_int] m specifies the number of rows of each B_i. m >= 0.**n**–**[in]**[rocblas_int] n specifies the number of columns of each B_i. n >= 0.**alpha**–**[in]**device pointer or host pointer specifying the scalar alpha. When alpha is &zero then A is not referenced and B need not be set before entry.**A**–**[in]**device array of device pointers storing each matrix A_i on the GPU. Matricies are of dimension ( lda, k ), where k is m when rocblas_side_left and is n when rocblas_side_right only the upper/lower triangular part is accessed.**lda**–**[in]**[rocblas_int] lda specifies the first dimension of each A_i.if side = rocblas_side_left, lda >= max( 1, m ), if side = rocblas_side_right, lda >= max( 1, n ).

**B**–**[inout]**device array of device pointers storing each matrix B_i on the GPU.**ldb**–**[in]**[rocblas_int] ldb specifies the first dimension of each B_i. ldb >= max( 1, m ).**batch_count**–**[in]**[rocblas_int] number of trsm operatons in the batch.



The `trsm_batched`

functions support the `_64`

interface. Parameter `m`

for left side, or `n`

with right side, larger than `int32_t`

max value are not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

For more information on pre-allocated memory in the handle, see the
[Device Memory Allocation](memory-alloc.html#device-memory-allocation-usage).

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_strsm_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_a, float *B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_b,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_strsm_strided_batched14rocblas_handle12rocblas_side12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPKfPKf11rocblas_int14rocblas_stridePf11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dtrsm_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_a, double *B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_b,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_dtrsm_strided_batched14rocblas_handle12rocblas_side12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPKdPKd11rocblas_int14rocblas_stridePd11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ctrsm_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_a,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_b,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_ctrsm_strided_batched14rocblas_handle12rocblas_side12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_int14rocblas_strideP21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ztrsm_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_a,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_b,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_ztrsm_strided_batched14rocblas_handle12rocblas_side12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_int14rocblas_strideP22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_int) **BLAS Level 3 API**trsm_srided_batched performs the following strided batched operation:

Note about memory allocation: When trsm is launched with a k evenly divisible by the internal block size of 128, and is no larger than 10 of these blocks, the API takes advantage of utilizing pre-allocated memory found in the handle to increase overall performance (where k is m when HIPBLAS_SIDE_LEFT and is n when HIPBLAS_SIDE_RIGHT).op(A_i)*X_i = alpha*B_i or X_i*op(A_i) = alpha*B_i, for i = 1, ..., batch_count, where alpha is a scalar, X and B are strided batched m by n matrices, A is triangular strided batched matrix and op(A) is one of op( A ) = A or op( A ) = A^T or op( A ) = A^H. Each matrix X_i is overwritten on B_i for i = 1, ..., batch_count.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**side**–**[in]**[rocblas_side]rocblas_side_left: op(A)*X = alpha*B.

rocblas_side_right: X*op(A) = alpha*B.


**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: each A_i is an upper triangular matrix.

rocblas_fill_lower: each A_i is a lower triangular matrix.


**transA**–**[in]**[rocblas_operation]transB: op(A) = A.

rocblas_operation_transpose: op(A) = A^T.

rocblas_operation_conjugate_transpose: op(A) = A^H.


**diag**–**[in]**[rocblas_diagonal]rocblas_diagonal_unit: each A_i is assumed to be unit triangular.

rocblas_diagonal_non_unit: each A_i is not assumed to be unit triangular.


**m**–**[in]**[rocblas_int] m specifies the number of rows of each B_i. m >= 0.**n**–**[in]**[rocblas_int] n specifies the number of columns of each B_i. n >= 0.**alpha**–**[in]**device pointer or host pointer specifying the scalar alpha. When alpha is &zero then A is not referenced and B need not be set before entry.**A**–**[in]**device pointer pointing to the first matrix A_1. of dimension ( lda, k ), where k is m when rocblas_side_left and is n when rocblas_side_right only the upper/lower triangular part is accessed.**lda**–**[in]**[rocblas_int] lda specifies the first dimension of each A_i.if side = rocblas_side_left, lda >= max( 1, m ). if side = rocblas_side_right, lda >= max( 1, n ).

**stride_a**–**[in]**[rocblas_stride] stride from the start of one A_i matrix to the next A_(i + 1).**B**–**[inout]**device pointer pointing to the first matrix B_1.**ldb**–**[in]**[rocblas_int] ldb specifies the first dimension of each B_i. ldb >= max( 1, m ).**stride_b**–**[in]**[rocblas_stride] stride from the start of one B_i matrix to the next B_(i + 1).**batch_count**–**[in]**[rocblas_int] number of trsm operatons in the batch.



The `trsm_strided_batched`

functions support the `_64`

interface. Parameter `m`

for left side, or `n`

with right side, larger than `int32_t`

max value are not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

For more information on pre-allocated memory in the handle, see the
[Device Memory Allocation](memory-alloc.html#device-memory-allocation-usage).

## rocblas_Xhemm + batched, strided_batched[#](#rocblas-xhemm-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_chemm([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv413rocblas_chemm14rocblas_handle12rocblas_side12rocblas_fill11rocblas_int11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_intPK21rocblas_float_complex11rocblas_intPK21rocblas_float_complexP21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zhemm([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv413rocblas_zhemm14rocblas_handle12rocblas_side12rocblas_fill11rocblas_int11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_intPK22rocblas_double_complex11rocblas_intPK22rocblas_double_complexP22rocblas_double_complex11rocblas_int) **BLAS Level 3 API**hemm performs one of the matrix-matrix operations:

C := alpha*A*B + beta*C if side == rocblas_side_left, C := alpha*B*A + beta*C if side == rocblas_side_right, where alpha and beta are scalars, B and C are m by n matrices, and A is a Hermitian matrix stored as either upper or lower.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**side**–**[in]**[rocblas_side]rocblas_side_left: C := alpha*A*B + beta*C

rocblas_side_right: C := alpha*B*A + beta*C


**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: A is an upper triangular matrix

rocblas_fill_lower: A is a lower triangular matrix


**m**–**[in]**[rocblas_int] m specifies the number of rows of B and C. m >= 0.**n**–**[in]**[rocblas_int] n specifies the number of columns of B and C. n >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A and B are not referenced.**A**–**[in]**pointer storing matrix A on the GPU.A is m by m if side == rocblas_side_left

A is n by n if side == rocblas_side_right Only the upper/lower triangular part is accessed. The imaginary component of the diagonal elements is not used.


**lda**–**[in]**[rocblas_int] lda specifies the first dimension of A.if side = rocblas_side_left, lda >= max( 1, m ), otherwise lda >= max( 1, n ).

**B**–**[in]**pointer storing matrix B on the GPU. Matrix dimension is m by n**ldb**–**[in]**[rocblas_int] ldb specifies the first dimension of B. ldb >= max( 1, m ).**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**C**–**[in]**pointer storing matrix C on the GPU. Matrix dimension is m by n**ldc**–**[in]**[rocblas_int] ldc specifies the first dimension of C. ldc >= max( 1, m ).



The `hemm`

functions support the `_64`

interface. Parameter `m`

for left side, or `n`

with right side, larger than `int32_t`

max value are not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_chemm_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_chemm_batched14rocblas_handle12rocblas_side12rocblas_fill11rocblas_int11rocblas_intPK21rocblas_float_complexA_PCK21rocblas_float_complex11rocblas_intA_PCK21rocblas_float_complex11rocblas_intPK21rocblas_float_complexA_PC21rocblas_float_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zhemm_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_zhemm_batched14rocblas_handle12rocblas_side12rocblas_fill11rocblas_int11rocblas_intPK22rocblas_double_complexA_PCK22rocblas_double_complex11rocblas_intA_PCK22rocblas_double_complex11rocblas_intPK22rocblas_double_complexA_PC22rocblas_double_complex11rocblas_int11rocblas_int) **BLAS Level 3 API**hemm_batched performs a batch of the matrix-matrix operations:

C_i := alpha*A_i*B_i + beta*C_i if side == rocblas_side_left, C_i := alpha*B_i*A_i + beta*C_i if side == rocblas_side_right, where alpha and beta are scalars, B_i and C_i are m by n matrices, and A_i is a Hermitian matrix stored as either upper or lower.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**side**–**[in]**[rocblas_side]rocblas_side_left: C_i := alpha*A_i*B_i + beta*C_i

rocblas_side_right: C_i := alpha*B_i*A_i + beta*C_i


**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: A_i is an upper triangular matrix

rocblas_fill_lower: A_i is a lower triangular matrix


**m**–**[in]**[rocblas_int] m specifies the number of rows of B_i and C_i. m >= 0.**n**–**[in]**[rocblas_int] n specifies the number of columns of B_i and C_i. n >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A_i and B_i are not referenced.**A**–**[in]**device array of device pointers storing each matrix A_i on the GPU.A_i is m by m if side == rocblas_side_left

A_i is n by n if side == rocblas_side_right Only the upper/lower triangular part is accessed. The imaginary component of the diagonal elements is not used.


**lda**–**[in]**[rocblas_int] lda specifies the first dimension of A_i.if side = rocblas_side_left, lda >= max( 1, m ), otherwise lda >= max( 1, n ).

**B**–**[in]**device array of device pointers storing each matrix B_i on the GPU. Matrix dimension is m by n**ldb**–**[in]**[rocblas_int] ldb specifies the first dimension of B_i. ldb >= max( 1, m ).**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C_i need not be set before entry.**C**–**[in]**device array of device pointers storing each matrix C_i on the GPU. Matrix dimension is m by n**ldc**–**[in]**[rocblas_int] ldc specifies the first dimension of C_i. ldc >= max( 1, m ).**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `hemm_batched`

functions support the `_64`

interface. Parameter `m`

for left side, or `n`

with right side, larger than `int32_t`

max value are not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_chemm_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_B, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_chemm_strided_batched14rocblas_handle12rocblas_side12rocblas_fill11rocblas_int11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_int14rocblas_stridePK21rocblas_float_complex11rocblas_int14rocblas_stridePK21rocblas_float_complexP21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zhemm_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_B, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_zhemm_strided_batched14rocblas_handle12rocblas_side12rocblas_fill11rocblas_int11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_int14rocblas_stridePK22rocblas_double_complex11rocblas_int14rocblas_stridePK22rocblas_double_complexP22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_int) **BLAS Level 3 API**hemm_strided_batched performs a batch of the matrix-matrix operations:

C_i := alpha*A_i*B_i + beta*C_i if side == rocblas_side_left, C_i := alpha*B_i*A_i + beta*C_i if side == rocblas_side_right, where alpha and beta are scalars, B_i and C_i are m by n matrices, and A_i is a Hermitian matrix stored as either upper or lower.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**side**–**[in]**[rocblas_side]rocblas_side_left: C_i := alpha*A_i*B_i + beta*C_i

rocblas_side_right: C_i := alpha*B_i*A_i + beta*C_i


**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: A_i is an upper triangular matrix

rocblas_fill_lower: A_i is a lower triangular matrix


**m**–**[in]**[rocblas_int] m specifies the number of rows of B_i and C_i. m >= 0.**n**–**[in]**[rocblas_int] n specifies the number of columns of B_i and C_i. n >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A_i and B_i are not referenced.**A**–**[in]**device pointer to first matrix A_1A_i is m by m if side == rocblas_side_left

A_i is n by n if side == rocblas_side_right Only the upper/lower triangular part is accessed. The imaginary component of the diagonal elements is not used.


**lda**–**[in]**[rocblas_int] lda specifies the first dimension of A_i.if side = rocblas_side_left, lda >= max( 1, m ), otherwise lda >= max( 1, n ).

**stride_A**–**[in]**[rocblas_stride] stride from the start of one matrix (A_i) and the next one (A_i+1).**B**–**[in]**device pointer to first matrix B_1 of dimension (ldb, n) on the GPU**ldb**–**[in]**[rocblas_int] ldb specifies the first dimension of B_i.if side = rocblas_operation_none, ldb >= max( 1, m ), otherwise ldb >= max( 1, n ).

**stride_B**–**[in]**[rocblas_stride] stride from the start of one matrix (B_i) and the next one (B_i+1).**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**C**–**[in]**device pointer to first matrix C_1 of dimension (ldc, n) on the GPU.**ldc**–**[in]**[rocblas_int] ldc specifies the first dimension of C. ldc >= max( 1, m ).**stride_C**–**[inout]**[rocblas_stride] stride from the start of one matrix (C_i) and the next one (C_i+1).**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `hemm_strided_batched`

functions support the `_64`

interface. Parameter `m`

for left side, or `n`

with right side, larger than `int32_t`

max value are not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xherk + batched, strided_batched[#](#rocblas-xherk-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cherk([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const float *alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const float *beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv413rocblas_cherk14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPKfPK21rocblas_float_complex11rocblas_intPKfP21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zherk([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const double *alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const double *beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv413rocblas_zherk14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPKdPK22rocblas_double_complex11rocblas_intPKdP22rocblas_double_complex11rocblas_int) **BLAS Level 3 API**herk performs one of the matrix-matrix operations for a Hermitian rank-k update:

C := alpha*op( A )*op( A )^H + beta*C, where alpha and beta are scalars, op(A) is an n by k matrix, and C is a n x n Hermitian matrix stored as either upper or lower. op( A ) = A, and A is n by k if transA == rocblas_operation_none op( A ) = A^H and A is k by n if transA == rocblas_operation_conjugate_transpose

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: C is an upper triangular matrix

rocblas_fill_lower: C is a lower triangular matrix


**transA**–**[in]**[rocblas_operation]rocblas_operation_conjugate_transpose: op(A) = A^H

rocblas_operation_none: op(A) = A


**n**–**[in]**[rocblas_int] n specifies the number of rows and columns of C. n >= 0.**k**–**[in]**[rocblas_int] k specifies the number of columns of op(A). k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A is not referenced and A need not be set before entry.**A**–**[in]**pointer storing matrix A on the GPU. Matrix dimension is ( lda, k ) when if transA = rocblas_operation_none, otherwise (lda, n)**lda**–**[in]**[rocblas_int] lda specifies the first dimension of A.if transA = rocblas_operation_none, lda >= max( 1, n ), otherwise lda >= max( 1, k ).

**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**C**–**[in]**pointer storing matrix C on the GPU. The imaginary component of the diagonal elements are not used but are set to zero unless quick return. only the upper/lower triangular part is accessed.**ldc**–**[in]**[rocblas_int] ldc specifies the first dimension of C. ldc >= max( 1, n ).



The `herk`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cherk_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const float *alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const float *beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_cherk_batched14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPKfA_PCK21rocblas_float_complex11rocblas_intPKfA_PC21rocblas_float_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zherk_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const double *alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const double *beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_zherk_batched14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPKdA_PCK22rocblas_double_complex11rocblas_intPKdA_PC22rocblas_double_complex11rocblas_int11rocblas_int) **BLAS Level 3 API**herk_batched performs a batch of the matrix-matrix operations for a Hermitian rank-k update:

C_i := alpha*op( A_i )*op( A_i )^H + beta*C_i, where alpha and beta are scalars, op(A) is an n by k matrix, and C_i is a n x n Hermitian matrix stored as either upper or lower. op( A_i ) = A_i, and A_i is n by k if transA == rocblas_operation_none op( A_i ) = A_i^H and A_i is k by n if transA == rocblas_operation_conjugate_transpose

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: C_i is an upper triangular matrix

rocblas_fill_lower: C_i is a lower triangular matrix


**transA**–**[in]**[rocblas_operation]rocblas_operation_conjugate_transpose: op(A) = A^H

rocblas_operation_none: op(A) = A


**n**–**[in]**[rocblas_int] n specifies the number of rows and columns of C_i. n >= 0.**k**–**[in]**[rocblas_int] k specifies the number of columns of op(A). k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A is not referenced and A need not be set before entry.**A**–**[in]**device array of device pointers storing each matrix_i A of dimension (lda, k) when transA is rocblas_operation_none, otherwise of dimension (lda, n).**lda**–**[in]**[rocblas_int] lda specifies the first dimension of A_i.if transA = rocblas_operation_none, lda >= max( 1, n ), otherwise lda >= max( 1, k ).

**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**C**–**[in]**device array of device pointers storing each matrix C_i on the GPU. The imaginary component of the diagonal elements are not used but are set to zero unless quick return. only the upper/lower triangular part of each C_i is accessed.**ldc**–**[in]**[rocblas_int] ldc specifies the first dimension of C. ldc >= max( 1, n ).**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `herk_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cherk_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const float *alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const float *beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_cherk_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPKfPK21rocblas_float_complex11rocblas_int14rocblas_stridePKfP21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zherk_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const double *alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const double *beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_zherk_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPKdPK22rocblas_double_complex11rocblas_int14rocblas_stridePKdP22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_int) **BLAS Level 3 API**herk_strided_batched performs a batch of the matrix-matrix operations for a Hermitian rank-k update:

C_i := alpha*op( A_i )*op( A_i )^H + beta*C_i, where alpha and beta are scalars, op(A) is an n by k matrix, and C_i is a n x n Hermitian matrix stored as either upper or lower. op( A_i ) = A_i, and A_i is n by k if transA == rocblas_operation_none op( A_i ) = A_i^H and A_i is k by n if transA == rocblas_operation_conjugate_transpose

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: C_i is an upper triangular matrix

rocblas_fill_lower: C_i is a lower triangular matrix


**transA**–**[in]**[rocblas_operation]rocblas_operation_conjugate_transpose: op(A) = A^H

rocblas_operation_none: op(A) = A


**n**–**[in]**[rocblas_int] n specifies the number of rows and columns of C_i. n >= 0.**k**–**[in]**[rocblas_int] k specifies the number of columns of op(A). k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A is not referenced and A need not be set before entry.**A**–**[in]**Device pointer to the first matrix A_1 on the GPU of dimension (lda, k) when transA is rocblas_operation_none, otherwise of dimension (lda, n)**lda**–**[in]**[rocblas_int] lda specifies the first dimension of A_i.if transA = rocblas_operation_none, lda >= max( 1, n ), otherwise lda >= max( 1, k ).

**stride_A**–**[in]**[rocblas_stride] stride from the start of one matrix (A_i) and the next one (A_i+1).**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**C**–**[in]**Device pointer to the first matrix C_1 on the GPU. The imaginary component of the diagonal elements are not used but are set to zero unless quick return. only the upper/lower triangular part of each C_i is accessed.**ldc**–**[in]**[rocblas_int] ldc specifies the first dimension of C. ldc >= max( 1, n ).**stride_C**–**[inout]**[rocblas_stride] stride from the start of one matrix (C_i) and the next one (C_i+1).**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `herk_strided_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xher2k + batched, strided_batched[#](#rocblas-xher2k-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cher2k([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const float *beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv414rocblas_cher2k14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_intPK21rocblas_float_complex11rocblas_intPKfP21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zher2k([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const double *beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv414rocblas_zher2k14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_intPK22rocblas_double_complex11rocblas_intPKdP22rocblas_double_complex11rocblas_int) **BLAS Level 3 API**her2k performs one of the matrix-matrix operations for a Hermitian rank-2k update:

C := alpha*op( A )*op( B )^H + conj(alpha)*op( B )*op( A )^H + beta*C, where alpha and beta are scalars, op(A) and op(B) are n by k matrices, and C is a n x n Hermitian matrix stored as either upper or lower. op( A ) = A, op( B ) = B, and A and B are n by k if trans == rocblas_operation_none op( A ) = A^H, op( B ) = B^H, and A and B are k by n if trans == rocblas_operation_conjugate_transpose

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: C is an upper triangular matrix

rocblas_fill_lower: C is a lower triangular matrix


**trans**–**[in]**[rocblas_operation]rocblas_operation_conjugate_transpose: op( A ) = A^H, op( B ) = B^H

rocblas_operation_none: op( A ) = A, op( B ) = B


**n**–**[in]**[rocblas_int] n specifies the number of rows and columns of C. n >= 0.**k**–**[in]**[rocblas_int] k specifies the number of columns of op(A). k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A is not referenced and A need not be set before entry.**A**–**[in]**pointer storing matrix A on the GPU. Matrix dimension is ( lda, k ) when if trans = rocblas_operation_none, otherwise (lda, n)**lda**–**[in]**[rocblas_int] lda specifies the first dimension of A.if trans = rocblas_operation_none, lda >= max( 1, n ), otherwise lda >= max( 1, k ).

**B**–**[in]**pointer storing matrix B on the GPU. Matrix dimension is ( ldb, k ) when if trans = rocblas_operation_none, otherwise (ldb, n)**ldb**–**[in]**[rocblas_int] ldb specifies the first dimension of B.if trans = rocblas_operation_none, ldb >= max( 1, n ), otherwise ldb >= max( 1, k ).

**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**C**–**[in]**pointer storing matrix C on the GPU. The imaginary component of the diagonal elements are not used but are set to zero unless quick return. only the upper/lower triangular part is accessed.**ldc**–**[in]**[rocblas_int] ldc specifies the first dimension of C. ldc >= max( 1, n ).



The `her2k`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cher2k_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const float *beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv422rocblas_cher2k_batched14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPK21rocblas_float_complexA_PCK21rocblas_float_complex11rocblas_intA_PCK21rocblas_float_complex11rocblas_intPKfA_PC21rocblas_float_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zher2k_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const double *beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv422rocblas_zher2k_batched14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPK22rocblas_double_complexA_PCK22rocblas_double_complex11rocblas_intA_PCK22rocblas_double_complex11rocblas_intPKdA_PC22rocblas_double_complex11rocblas_int11rocblas_int) **BLAS Level 3 API**her2k_batched performs a batch of the matrix-matrix operations for a Hermitian rank-2k update:

C_i := alpha*op( A_i )*op( B_i )^H + conj(alpha)*op( B_i )*op( A_i )^H + beta*C_i, where alpha and beta are scalars, op(A_i) and op(B_i) are n by k matrices, and C_i is a n x n Hermitian matrix stored as either upper or lower. op( A_i ) = A_i, op( B_i ) = B_i, and A_i and B_i are n by k if trans == rocblas_operation_none op( A_i ) = A_i^H, op( B_i ) = B_i^H, and A_i and B_i are k by n if trans == rocblas_operation_conjugate_transpose

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: C_i is an upper triangular matrix

rocblas_fill_lower: C_i is a lower triangular matrix


**trans**–**[in]**[rocblas_operation]rocblas_operation_conjugate_transpose: op(A) = A^H

rocblas_operation_none: op(A) = A


**n**–**[in]**[rocblas_int] n specifies the number of rows and columns of C_i. n >= 0.**k**–**[in]**[rocblas_int] k specifies the number of columns of op(A). k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A is not referenced and A need not be set before entry.**A**–**[in]**device array of device pointers storing each matrix_i A of dimension (lda, k) when trans is rocblas_operation_none, otherwise of dimension (lda, n).**lda**–**[in]**[rocblas_int] lda specifies the first dimension of A_i.if trans = rocblas_operation_none, lda >= max( 1, n ), otherwise lda >= max( 1, k ).

**B**–**[in]**device array of device pointers storing each matrix_i B of dimension (ldb, k) when trans is rocblas_operation_none, otherwise of dimension (ldb, n).**ldb**–**[in]**[rocblas_int] ldb specifies the first dimension of B_i.if trans = rocblas_operation_none, ldb >= max( 1, n ), otherwise ldb >= max( 1, k ).

**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**C**–**[in]**device array of device pointers storing each matrix C_i on the GPU. The imaginary component of the diagonal elements are not used but are set to zero unless quick return. only the upper/lower triangular part of each C_i is accessed.**ldc**–**[in]**[rocblas_int] ldc specifies the first dimension of C. ldc >= max( 1, n ).**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `her2k_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cher2k_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_B, const float *beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv430rocblas_cher2k_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_int14rocblas_stridePK21rocblas_float_complex11rocblas_int14rocblas_stridePKfP21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zher2k_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_B, const double *beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv430rocblas_zher2k_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_int14rocblas_stridePK22rocblas_double_complex11rocblas_int14rocblas_stridePKdP22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_int) **BLAS Level 3 API**her2k_strided_batched performs a batch of the matrix-matrix operations for a Hermitian rank-2k update:

C_i := alpha*op( A_i )*op( B_i )^H + conj(alpha)*op( B_i )*op( A_i )^H + beta*C_i, where alpha and beta are scalars, op(A_i) and op(B_i) are n by k matrices, and C_i is a n x n Hermitian matrix stored as either upper or lower. op( A_i ) = A_i, op( B_i ) = B_i, and A_i and B_i are n by k if trans == rocblas_operation_none op( A_i ) = A_i^H, op( B_i ) = B_i^H, and A_i and B_i are k by n if trans == rocblas_operation_conjugate_transpose

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: C_i is an upper triangular matrix

rocblas_fill_lower: C_i is a lower triangular matrix


**trans**–**[in]**[rocblas_operation]rocblas_operation_conjugate_transpose: op( A_i ) = A_i^H, op( B_i ) = B_i^H

rocblas_operation_none: op( A_i ) = A_i, op( B_i ) = B_i


**n**–**[in]**[rocblas_int] n specifies the number of rows and columns of C_i. n >= 0.**k**–**[in]**[rocblas_int] k specifies the number of columns of op(A). k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A is not referenced and A need not be set before entry.**A**–**[in]**Device pointer to the first matrix A_1 on the GPU of dimension (lda, k) when trans is rocblas_operation_none, otherwise of dimension (lda, n).**lda**–**[in]**[rocblas_int] lda specifies the first dimension of A_i.if trans = rocblas_operation_none, lda >= max( 1, n ), otherwise lda >= max( 1, k ).

**stride_A**–**[in]**[rocblas_stride] stride from the start of one matrix (A_i) and the next one (A_i+1).**B**–**[in]**Device pointer to the first matrix B_1 on the GPU of dimension (ldb, k) when trans is rocblas_operation_none, otherwise of dimension (ldb, n).**ldb**–**[in]**[rocblas_int] ldb specifies the first dimension of B_i.if trans = rocblas_operation_none, ldb >= max( 1, n ), otherwise ldb >= max( 1, k ).

**stride_B**–**[in]**[rocblas_stride] stride from the start of one matrix (B_i) and the next one (B_i+1).**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**C**–**[in]**Device pointer to the first matrix C_1 on the GPU. The imaginary component of the diagonal elements are not used but are set to zero unless quick return. only the upper/lower triangular part of each C_i is accessed.**ldc**–**[in]**[rocblas_int] ldc specifies the first dimension of C. ldc >= max( 1, n ).**stride_C**–**[inout]**[rocblas_stride] stride from the start of one matrix (C_i) and the next one (C_i+1).**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `her2k_strided_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xherkx + batched, strided_batched[#](#rocblas-xherkx-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cherkx([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const float *beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv414rocblas_cherkx14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_intPK21rocblas_float_complex11rocblas_intPKfP21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zherkx([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const double *beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv414rocblas_zherkx14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_intPK22rocblas_double_complex11rocblas_intPKdP22rocblas_double_complex11rocblas_int) **BLAS Level 3 API**herkx performs one of the matrix-matrix operations for a Hermitian rank-k update:

This routine should only be used when the caller can guarantee that the result of op( A )*op( B )^T will be Hermitian.C := alpha*op( A )*op( B )^H + beta*C, where alpha and beta are scalars, op(A) and op(B) are n by k matrices, and C is a n x n Hermitian matrix stored as either upper or lower.

op( A ) = A, op( B ) = B, and A and B are n by k if trans == rocblas_operation_none op( A ) = A^H, op( B ) = B^H, and A and B are k by n if trans == rocblas_operation_conjugate_transpose

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: C is an upper triangular matrix

rocblas_fill_lower: C is a lower triangular matrix


**trans**–**[in]**[rocblas_operation]rocblas_operation_conjugate_transpose: op( A ) = A^H, op( B ) = B^H

rocblas_operation_none: op( A ) = A, op( B ) = B


**n**–**[in]**[rocblas_int] n specifies the number of rows and columns of C. n >= 0.**k**–**[in]**[rocblas_int] k specifies the number of columns of op(A). k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A is not referenced and A need not be set before entry.**A**–**[in]**pointer storing matrix A on the GPU. Matrix dimension is ( lda, k ) when if trans = rocblas_operation_none, otherwise (lda, n)**lda**–**[in]**[rocblas_int] lda specifies the first dimension of A.if trans = rocblas_operation_none, lda >= max( 1, n ), otherwise lda >= max( 1, k ).

**B**–**[in]**pointer storing matrix B on the GPU. Matrix dimension is ( ldb, k ) when if trans = rocblas_operation_none, otherwise (ldb, n)**ldb**–**[in]**[rocblas_int] ldb specifies the first dimension of B.if trans = rocblas_operation_none, ldb >= max( 1, n ), otherwise ldb >= max( 1, k ).

**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**C**–**[in]**pointer storing matrix C on the GPU. The imaginary component of the diagonal elements are not used but are set to zero unless quick return. only the upper/lower triangular part is accessed.**ldc**–**[in]**[rocblas_int] ldc specifies the first dimension of C. ldc >= max( 1, n ).



The `herkx`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cherkx_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const float *beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv422rocblas_cherkx_batched14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPK21rocblas_float_complexA_PCK21rocblas_float_complex11rocblas_intA_PCK21rocblas_float_complex11rocblas_intPKfA_PC21rocblas_float_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zherkx_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const double *beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv422rocblas_zherkx_batched14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPK22rocblas_double_complexA_PCK22rocblas_double_complex11rocblas_intA_PCK22rocblas_double_complex11rocblas_intPKdA_PC22rocblas_double_complex11rocblas_int11rocblas_int) **BLAS Level 3 API**herkx_batched performs a batch of the matrix-matrix operations for a Hermitian rank-k update:

This routine should only be used when the caller can guarantee that the result of op( A )*op( B )^T will be Hermitian.C_i := alpha*op( A_i )*op( B_i )^H + beta*C_i, where alpha and beta are scalars, op(A_i) and op(B_i) are n by k matrices, and C_i is a n x n Hermitian matrix stored as either upper or lower.

op( A_i ) = A_i, op( B_i ) = B_i, and A_i and B_i are n by k if trans == rocblas_operation_none op( A_i ) = A_i^H, op( B_i ) = B_i^H, and A_i and B_i are k by n if trans == rocblas_operation_conjugate_transpose

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: C_i is an upper triangular matrix

rocblas_fill_lower: C_i is a lower triangular matrix


**trans**–**[in]**[rocblas_operation]rocblas_operation_conjugate_transpose: op(A) = A^H

rocblas_operation_none: op(A) = A


**n**–**[in]**[rocblas_int] n specifies the number of rows and columns of C_i. n >= 0.**k**–**[in]**[rocblas_int] k specifies the number of columns of op(A). k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A is not referenced and A need not be set before entry.**A**–**[in]**device array of device pointers storing each matrix_i A of dimension (lda, k) when trans is rocblas_operation_none, otherwise of dimension (lda, n)**lda**–**[in]**[rocblas_int] lda specifies the first dimension of A_i.if trans = rocblas_operation_none, lda >= max( 1, n ), otherwise lda >= max( 1, k ).

**B**–**[in]**device array of device pointers storing each matrix_i B of dimension (ldb, k) when trans is rocblas_operation_none, otherwise of dimension (ldb, n)**ldb**–**[in]**[rocblas_int] ldb specifies the first dimension of B_i.if trans = rocblas_operation_none, ldb >= max( 1, n ), otherwise ldb >= max( 1, k ).

**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**C**–**[in]**device array of device pointers storing each matrix C_i on the GPU. The imaginary component of the diagonal elements are not used but are set to zero unless quick return. only the upper/lower triangular part of each C_i is accessed.**ldc**–**[in]**[rocblas_int] ldc specifies the first dimension of C. ldc >= max( 1, n ).**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `herkx_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cherkx_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_B, const float *beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv430rocblas_cherkx_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_int14rocblas_stridePK21rocblas_float_complex11rocblas_int14rocblas_stridePKfP21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zherkx_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_B, const double *beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv430rocblas_zherkx_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_int14rocblas_stridePK22rocblas_double_complex11rocblas_int14rocblas_stridePKdP22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_int) **BLAS Level 3 API**herkx_strided_batched performs a batch of the matrix-matrix operations for a Hermitian rank-k update:

This routine should only be used when the caller can guarantee that the result of op( A )*op( B )^T will be Hermitian.C_i := alpha*op( A_i )*op( B_i )^H + beta*C_i, where alpha and beta are scalars, op(A_i) and op(B_i) are n by k matrices, and C_i is a n x n Hermitian matrix stored as either upper or lower.

op( A_i ) = A_i, op( B_i ) = B_i, and A_i and B_i are n by k if trans == rocblas_operation_none op( A_i ) = A_i^H, op( B_i ) = B_i^H, and A_i and B_i are k by n if trans == rocblas_operation_conjugate_transpose

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: C_i is an upper triangular matrix

rocblas_fill_lower: C_i is a lower triangular matrix


**trans**–**[in]**[rocblas_operation]rocblas_operation_conjugate_transpose: op( A_i ) = A_i^H, op( B_i ) = B_i^H

rocblas_operation_none: op( A_i ) = A_i, op( B_i ) = B_i


**n**–**[in]**[rocblas_int] n specifies the number of rows and columns of C_i. n >= 0.**k**–**[in]**[rocblas_int] k specifies the number of columns of op(A). k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A is not referenced and A need not be set before entry.**A**–**[in]**Device pointer to the first matrix A_1 on the GPU of dimension (lda, k) when trans is rocblas_operation_none, otherwise of dimension (lda, n).**lda**–**[in]**[rocblas_int] lda specifies the first dimension of A_i.if trans = rocblas_operation_none, lda >= max( 1, n ), otherwise lda >= max( 1, k ).

**stride_A**–**[in]**[rocblas_stride] stride from the start of one matrix (A_i) and the next one (A_i+1)**B**–**[in]**Device pointer to the first matrix B_1 on the GPU of dimension (ldb, k) when trans is rocblas_operation_none, otherwise of dimension (ldb, n).**ldb**–**[in]**[rocblas_int] ldb specifies the first dimension of B_i.if trans = rocblas_operation_none, ldb >= max( 1, n ), otherwise ldb >= max( 1, k ).

**stride_B**–**[in]**[rocblas_stride] stride from the start of one matrix (B_i) and the next one (B_i+1)**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**C**–**[in]**Device pointer to the first matrix C_1 on the GPU. The imaginary component of the diagonal elements are not used but are set to zero unless quick return. only the upper/lower triangular part of each C_i is accessed.**ldc**–**[in]**[rocblas_int] ldc specifies the first dimension of C. ldc >= max( 1, n ).**stride_C**–**[inout]**[rocblas_stride] stride from the start of one matrix (C_i) and the next one (C_i+1).**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `herkx_strided_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xtrtri + batched, strided_batched[#](#rocblas-xtrtri-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_strtri([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, float *invA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldinvA)[#](#_CPPv414rocblas_strtri14rocblas_handle12rocblas_fill16rocblas_diagonal11rocblas_intPKf11rocblas_intPf11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dtrtri([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, double *invA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldinvA)[#](#_CPPv414rocblas_dtrtri14rocblas_handle12rocblas_fill16rocblas_diagonal11rocblas_intPKd11rocblas_intPd11rocblas_int) **BLAS Level 3 API**trtri compute the inverse of a matrix A, namely, invA and write the result into invA;

if rocblas_fill_upper, the lower part of A is not referenced if rocblas_fill_lower, the upper part of A is not referenced

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill] specifies whether the upper ‘rocblas_fill_upper’ or lower ‘rocblas_fill_lower’**diag**–**[in]**[rocblas_diagonal]’rocblas_diagonal_non_unit’, A is non-unit triangular;

’rocblas_diagonal_unit’, A is unit triangular;


**n**–**[in]**[rocblas_int] size of matrix A and invA.**A**–**[in]**device pointer storing matrix A.**lda**–**[in]**[rocblas_int] specifies the leading dimension of A.**invA**–**[out]**device pointer storing matrix invA. Partial inplace operation is supported. See below: -If UPLO = ‘U’, the leading N-by-N upper triangular part of the invA will store the inverse of the upper triangular matrix, and the strictly lower triangular part of invA may be cleared.If UPLO = ‘L’, the leading N-by-N lower triangular part of the invA will store the inverse of the lower triangular matrix, and the strictly upper triangular part of invA may be cleared.


**ldinvA**–**[in]**[rocblas_int] specifies the leading dimension of invA.



-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_strtri_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, float *const invA[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldinvA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv422rocblas_strtri_batched14rocblas_handle12rocblas_fill16rocblas_diagonal11rocblas_intA_PCKf11rocblas_intA_PCf11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dtrtri_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, double *const invA[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldinvA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv422rocblas_dtrtri_batched14rocblas_handle12rocblas_fill16rocblas_diagonal11rocblas_intA_PCKd11rocblas_intA_PCd11rocblas_int11rocblas_int) **BLAS Level 3 API**trtri_batched compute the inverse of A_i and write into invA_i where A_i and invA_i are the i-th matrices in the batch, for i = 1, …, batch_count.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill] specifies whether the upper ‘rocblas_fill_upper’ or lower ‘rocblas_fill_lower’**diag**–**[in]**[rocblas_diagonal]’rocblas_diagonal_non_unit’, A is non-unit triangular;

’rocblas_diagonal_unit’, A is unit triangular;


**n**–**[in]**[rocblas_int]**A**–**[in]**device array of device pointers storing each matrix A_i.**lda**–**[in]**[rocblas_int] specifies the leading dimension of each A_i.**invA**–**[out]**device array of device pointers storing the inverse of each matrix A_i. Partial inplace operation is supported. See below: -If UPLO = ‘U’, the leading N-by-N upper triangular part of the invA will store the inverse of the upper triangular matrix, and the strictly lower triangular part of invA may be cleared.If UPLO = ‘L’, the leading N-by-N lower triangular part of the invA will store the inverse of the lower triangular matrix, and the strictly upper triangular part of invA may be cleared.


**ldinvA**–**[in]**[rocblas_int] specifies the leading dimension of each invA_i.**batch_count**–**[in]**[rocblas_int] numbers of matrices in the batch.



-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_strtri_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_a, float *invA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldinvA,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_invA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv430rocblas_strtri_strided_batched14rocblas_handle12rocblas_fill16rocblas_diagonal11rocblas_intPKf11rocblas_int14rocblas_stridePf11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dtrtri_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_a, double *invA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldinvA,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_invA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv430rocblas_dtrtri_strided_batched14rocblas_handle12rocblas_fill16rocblas_diagonal11rocblas_intPKd11rocblas_int14rocblas_stridePd11rocblas_int14rocblas_stride11rocblas_int) **BLAS Level 3 API**trtri_strided_batched compute the inverse of A_i and write into invA_i where A_i and invA_i are the i-th matrices in the batch, for i = 1, …, batch_count.

If UPLO = ‘U’, the leading N-by-N upper triangular part of the invA will store the inverse of the upper triangular matrix, and the strictly lower triangular part of invA may be cleared.

If UPLO = ‘L’, the leading N-by-N lower triangular part of the invA will store the inverse of the lower triangular matrix, and the strictly upper triangular part of invA may be cleared.


- Parameters:
**ldinvA**–**[in]**[rocblas_int] specifies the leading dimension of each invA_i.**stride_invA**–**[in]**[rocblas_stride] “batch stride invA”: stride from the start of one invA_i matrix to the next invA_(i + 1).**batch_count**–**[in]**[rocblas_int] numbers of matrices in the batch.**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill] specifies whether the upper ‘rocblas_fill_upper’ or lower ‘rocblas_fill_lower’**diag**–**[in]**[rocblas_diagonal]’rocblas_diagonal_non_unit’, A is non-unit triangular;

’rocblas_diagonal_unit’, A is unit triangular;


**n**–**[in]**[rocblas_int]**A**–**[in]**device pointer pointing to address of first matrix A_1.**lda**–**[in]**[rocblas_int] specifies the leading dimension of each A.**stride_a**–**[in]**[rocblas_stride] “batch stride a”: stride from the start of one A_i matrix to the next A_(i + 1).**invA**–**[out]**device pointer storing the inverses of each matrix A_i. Partial inplace operation is supported. See below:
