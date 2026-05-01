---
title: "rocBLAS Level-2 functions &#8212; rocBLAS 5.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/level-2.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:11:08.458670+00:00
content_hash: "60ce03067ea0fee5"
---

# rocBLAS Level-2 functions[#](#rocblas-level-2-functions)

rocBLAS Level-2 functions perform matrix-vector operations. [[Level2]](references.html#level2)

Level-2 functions support the ILP64 API. For more information on these `_64`

functions, see the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xgbmv + batched, strided_batched[#](#rocblas-xgbmv-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sgbmv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)kl,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ku, const float *alpha, const float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const float *beta, float *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy)[#](#_CPPv413rocblas_sgbmv14rocblas_handle17rocblas_operation11rocblas_int11rocblas_int11rocblas_int11rocblas_intPKfPKf11rocblas_intPKf11rocblas_intPKfPf11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dgbmv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)kl,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ku, const double *alpha, const double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const double *beta, double *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy)[#](#_CPPv413rocblas_dgbmv14rocblas_handle17rocblas_operation11rocblas_int11rocblas_int11rocblas_int11rocblas_intPKdPKd11rocblas_intPKd11rocblas_intPKdPd11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cgbmv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)kl,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ku, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy)[#](#_CPPv413rocblas_cgbmv14rocblas_handle17rocblas_operation11rocblas_int11rocblas_int11rocblas_int11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_intPK21rocblas_float_complex11rocblas_intPK21rocblas_float_complexP21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zgbmv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)kl,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ku, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy)[#](#_CPPv413rocblas_zgbmv14rocblas_handle17rocblas_operation11rocblas_int11rocblas_int11rocblas_int11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_intPK22rocblas_double_complex11rocblas_intPK22rocblas_double_complexP22rocblas_double_complex11rocblas_int) **BLAS Level 2 API**gbmv performs one of the matrix-vector operations:

y := alpha*A*x + beta*y, or y := alpha*A**T*x + beta*y, or y := alpha*A**H*x + beta*y, where alpha and beta are scalars, x and y are vectors and A is an m by n banded matrix with kl sub-diagonals and ku super-diagonals.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**trans**–**[in]**[rocblas_operation] indicates whether matrix A is tranposed (conjugated) or not.**m**–**[in]**[rocblas_int] number of rows of matrix A.**n**–**[in]**[rocblas_int] number of columns of matrix A.**kl**–**[in]**[rocblas_int] number of sub-diagonals of A.**ku**–**[in]**[rocblas_int] number of super-diagonals of A.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**A**–**[in]**device pointer storing banded matrix A. Leading (kl + ku + 1) by n part of the matrix contains the coefficients of the banded matrix. The leading diagonal resides in row (ku + 1) with the first super-diagonal above on the RHS of row ku. The first sub-diagonal resides below on the LHS of row ku + 2. This propagates up and down across sub/super-diagonals.Note that the empty elements which do not correspond to data will not be referenced.Ex: (m = n = 7; ku = 2, kl = 2) 1 2 3 0 0 0 0 0 0 3 3 3 3 3 4 1 2 3 0 0 0 0 2 2 2 2 2 2 5 4 1 2 3 0 0 ----> 1 1 1 1 1 1 1 0 5 4 1 2 3 0 4 4 4 4 4 4 0 0 0 5 4 1 2 3 5 5 5 5 5 0 0 0 0 0 5 4 1 2 0 0 0 0 0 0 0 0 0 0 0 5 4 1 0 0 0 0 0 0 0

**lda**–**[in]**[rocblas_int] specifies the leading dimension of A. Must be >= (kl + ku + 1).**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of x.**beta**–**[in]**device pointer or host pointer to scalar beta.**y**–**[inout]**device pointer storing vector y.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of y.



`gbmv`

functions support the `_64`

interface. Parameters `m`

, `n`

, `kl`

, and `ku`

larger than `int32_t`

max value are not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sgbmv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)kl,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ku, const float *alpha, const float *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const float *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const float *beta, float *const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_sgbmv_batched14rocblas_handle17rocblas_operation11rocblas_int11rocblas_int11rocblas_int11rocblas_intPKfA_PCKf11rocblas_intA_PCKf11rocblas_intPKfA_PCf11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dgbmv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)kl,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ku, const double *alpha, const double *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const double *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const double *beta, double *const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_dgbmv_batched14rocblas_handle17rocblas_operation11rocblas_int11rocblas_int11rocblas_int11rocblas_intPKdA_PCKd11rocblas_intA_PCKd11rocblas_intPKdA_PCd11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cgbmv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)kl,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ku, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_cgbmv_batched14rocblas_handle17rocblas_operation11rocblas_int11rocblas_int11rocblas_int11rocblas_intPK21rocblas_float_complexA_PCK21rocblas_float_complex11rocblas_intA_PCK21rocblas_float_complex11rocblas_intPK21rocblas_float_complexA_PC21rocblas_float_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zgbmv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)kl,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ku, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_zgbmv_batched14rocblas_handle17rocblas_operation11rocblas_int11rocblas_int11rocblas_int11rocblas_intPK22rocblas_double_complexA_PCK22rocblas_double_complex11rocblas_intA_PCK22rocblas_double_complex11rocblas_intPK22rocblas_double_complexA_PC22rocblas_double_complex11rocblas_int11rocblas_int) **BLAS Level 2 API**gbmv_batched performs one of the matrix-vector operations:

y_i := alpha*A_i*x_i + beta*y_i, or y_i := alpha*A_i**T*x_i + beta*y_i, or y_i := alpha*A_i**H*x_i + beta*y_i, where (A_i, x_i, y_i) is the i-th instance of the batch. alpha and beta are scalars, x_i and y_i are vectors and A_i is an m by n banded matrix with kl sub-diagonals and ku super-diagonals, for i = 1, ..., batch_count.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**trans**–**[in]**[rocblas_operation] indicates whether matrix A is tranposed (conjugated) or not.**m**–**[in]**[rocblas_int] number of rows of each matrix A_i.**n**–**[in]**[rocblas_int] number of columns of each matrix A_i.**kl**–**[in]**[rocblas_int] number of sub-diagonals of each A_i.**ku**–**[in]**[rocblas_int] number of super-diagonals of each A_i.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**A**–**[in]**device array of device pointers storing each banded matrix A_i. Leading (kl + ku + 1) by n part of the matrix contains the coefficients of the banded matrix. The leading diagonal resides in row (ku + 1) with the first super-diagonal above on the RHS of row ku. The first sub-diagonal resides below on the LHS of row ku + 2. This propagates up and down across sub/super-diagonals.Note that the empty elements which do not correspond to data will not be referenced.Ex: (m = n = 7; ku = 2, kl = 2) 1 2 3 0 0 0 0 0 0 3 3 3 3 3 4 1 2 3 0 0 0 0 2 2 2 2 2 2 5 4 1 2 3 0 0 ----> 1 1 1 1 1 1 1 0 5 4 1 2 3 0 4 4 4 4 4 4 0 0 0 5 4 1 2 3 5 5 5 5 5 0 0 0 0 0 5 4 1 2 0 0 0 0 0 0 0 0 0 0 0 5 4 1 0 0 0 0 0 0 0

**lda**–**[in]**[rocblas_int] specifies the leading dimension of each A_i. Must be >= (kl + ku + 1)**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i.**beta**–**[in]**device pointer or host pointer to scalar beta.**y**–**[inout]**device array of device pointers storing each vector y_i.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of each y_i.**batch_count**–**[in]**[rocblas_int] specifies the number of instances in the batch.



`gbmv_batched`

functions support the `_64`

interface. Parameters `m`

, `n`

, `kl`

, and `ku`

larger than `int32_t`

max value are not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sgbmv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)kl,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ku, const float *alpha, const float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x, const float *beta, float *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_sgbmv_strided_batched14rocblas_handle17rocblas_operation11rocblas_int11rocblas_int11rocblas_int11rocblas_intPKfPKf11rocblas_int14rocblas_stridePKf11rocblas_int14rocblas_stridePKfPf11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dgbmv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)kl,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ku, const double *alpha, const double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x, const double *beta, double *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_dgbmv_strided_batched14rocblas_handle17rocblas_operation11rocblas_int11rocblas_int11rocblas_int11rocblas_intPKdPKd11rocblas_int14rocblas_stridePKd11rocblas_int14rocblas_stridePKdPd11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cgbmv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)kl,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ku, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_cgbmv_strided_batched14rocblas_handle17rocblas_operation11rocblas_int11rocblas_int11rocblas_int11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_int14rocblas_stridePK21rocblas_float_complex11rocblas_int14rocblas_stridePK21rocblas_float_complexP21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zgbmv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)kl,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ku, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_zgbmv_strided_batched14rocblas_handle17rocblas_operation11rocblas_int11rocblas_int11rocblas_int11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_int14rocblas_stridePK22rocblas_double_complex11rocblas_int14rocblas_stridePK22rocblas_double_complexP22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_int) **BLAS Level 2 API**gbmv_strided_batched performs one of the matrix-vector operations:

y_i := alpha*A_i*x_i + beta*y_i, or y_i := alpha*A_i**T*x_i + beta*y_i, or y_i := alpha*A_i**H*x_i + beta*y_i, where (A_i, x_i, y_i) is the i-th instance of the batch. alpha and beta are scalars, x_i and y_i are vectors and A_i is an m by n banded matrix with kl sub-diagonals and ku super-diagonals, for i = 1, ..., batch_count.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**trans**–**[in]**[rocblas_operation] indicates whether matrix A is tranposed (conjugated) or not.**m**–**[in]**[rocblas_int] number of rows of matrix A.**n**–**[in]**[rocblas_int] number of columns of matrix A.**kl**–**[in]**[rocblas_int] number of sub-diagonals of A.**ku**–**[in]**[rocblas_int] number of super-diagonals of A.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**A**–**[in]**device pointer to first banded matrix (A_1). Leading (kl + ku + 1) by n part of the matrix contains the coefficients of the banded matrix. The leading diagonal resides in row (ku + 1) with the first super-diagonal above on the RHS of row ku. The first sub-diagonal resides below on the LHS of row ku + 2. This propagates up and down across sub/super-diagonals.Note that the empty elements which do not correspond to data will not be referenced.Ex: (m = n = 7; ku = 2, kl = 2) 1 2 3 0 0 0 0 0 0 3 3 3 3 3 4 1 2 3 0 0 0 0 2 2 2 2 2 2 5 4 1 2 3 0 0 ----> 1 1 1 1 1 1 1 0 5 4 1 2 3 0 4 4 4 4 4 4 0 0 0 5 4 1 2 3 5 5 5 5 5 0 0 0 0 0 5 4 1 2 0 0 0 0 0 0 0 0 0 0 0 5 4 1 0 0 0 0 0 0 0

**lda**–**[in]**[rocblas_int] specifies the leading dimension of A. Must be >= (kl + ku + 1).**stride_A**–**[in]**[rocblas_stride] stride from the start of one matrix (A_i) and the next one (A_i+1).**x**–**[in]**device pointer to first vector (x_1).**incx**–**[in]**[rocblas_int] specifies the increment for the elements of x.**stride_x**–**[in]**[rocblas_stride] stride from the start of one vector (x_i) and the next one (x_i+1).**beta**–**[in]**device pointer or host pointer to scalar beta.**y**–**[inout]**device pointer to first vector (y_1).**incy**–**[in]**[rocblas_int] specifies the increment for the elements of y.**stride_y**–**[in]**[rocblas_stride] stride from the start of one vector (y_i) and the next one (x_i+1).**batch_count**–**[in]**[rocblas_int] specifies the number of instances in the batch.



`gbmv_strided_batched`

functions support the `_64`

interface. Parameters `m`

, `n`

, `kl`

, and `ku`

larger than `int32_t`

max value are not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xgemv + batched, strided_batched[#](#rocblas-xgemv-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sgemv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const float *beta, float *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy)[#](#_CPPv413rocblas_sgemv14rocblas_handle17rocblas_operation11rocblas_int11rocblas_intPKfPKf11rocblas_intPKf11rocblas_intPKfPf11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dgemv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const double *beta, double *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy)[#](#_CPPv413rocblas_dgemv14rocblas_handle17rocblas_operation11rocblas_int11rocblas_intPKdPKd11rocblas_intPKd11rocblas_intPKdPd11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cgemv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy)[#](#_CPPv413rocblas_cgemv14rocblas_handle17rocblas_operation11rocblas_int11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_intPK21rocblas_float_complex11rocblas_intPK21rocblas_float_complexP21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zgemv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy)[#](#_CPPv413rocblas_zgemv14rocblas_handle17rocblas_operation11rocblas_int11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_intPK22rocblas_double_complex11rocblas_intPK22rocblas_double_complexP22rocblas_double_complex11rocblas_int) **BLAS Level 2 API**gemv performs one of the matrix-vector operations:

y := alpha*A*x + beta*y, or y := alpha*A**T*x + beta*y, or y := alpha*A**H*x + beta*y, where alpha and beta are scalars, x and y are vectors and A is an m by n matrix.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**trans**–**[in]**[rocblas_operation] indicates whether matrix A is tranposed (conjugated) or not.**m**–**[in]**[rocblas_int] number of rows of matrix A.**n**–**[in]**[rocblas_int] number of columns of matrix A.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**A**–**[in]**device pointer storing matrix A.**lda**–**[in]**[rocblas_int] specifies the leading dimension of A.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of x.**beta**–**[in]**device pointer or host pointer to scalar beta.**y**–**[inout]**device pointer storing vector y.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of y.



`gemv`

functions have an implementation which uses atomic operations. See the [Atomic operations](../conceptual/rocblas-design-notes.html#atomic-operations) section for more information.
The `gemv`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sgemv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const float *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const float *beta, float *const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_sgemv_batched14rocblas_handle17rocblas_operation11rocblas_int11rocblas_intPKfA_PCKf11rocblas_intA_PCKf11rocblas_intPKfA_PCf11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dgemv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const double *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const double *beta, double *const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_dgemv_batched14rocblas_handle17rocblas_operation11rocblas_int11rocblas_intPKdA_PCKd11rocblas_intA_PCKd11rocblas_intPKdA_PCd11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cgemv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_cgemv_batched14rocblas_handle17rocblas_operation11rocblas_int11rocblas_intPK21rocblas_float_complexA_PCK21rocblas_float_complex11rocblas_intA_PCK21rocblas_float_complex11rocblas_intPK21rocblas_float_complexA_PC21rocblas_float_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zgemv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_zgemv_batched14rocblas_handle17rocblas_operation11rocblas_int11rocblas_intPK22rocblas_double_complexA_PCK22rocblas_double_complex11rocblas_intA_PCK22rocblas_double_complex11rocblas_intPK22rocblas_double_complexA_PC22rocblas_double_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_hshgemv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const[rocblas_half](datatypes.html#_CPPv412rocblas_half)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_half](datatypes.html#_CPPv412rocblas_half)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const float *beta,[rocblas_half](datatypes.html#_CPPv412rocblas_half)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv423rocblas_hshgemv_batched14rocblas_handle17rocblas_operation11rocblas_int11rocblas_intPKfA_PCK12rocblas_half11rocblas_intA_PCK12rocblas_half11rocblas_intPKfA_PC12rocblas_half11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_hssgemv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const[rocblas_half](datatypes.html#_CPPv412rocblas_half)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_half](datatypes.html#_CPPv412rocblas_half)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const float *beta, float *const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv423rocblas_hssgemv_batched14rocblas_handle17rocblas_operation11rocblas_int11rocblas_intPKfA_PCK12rocblas_half11rocblas_intA_PCK12rocblas_half11rocblas_intPKfA_PCf11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_tstgemv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const[rocblas_bfloat16](datatypes.html#_CPPv416rocblas_bfloat16)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_bfloat16](datatypes.html#_CPPv416rocblas_bfloat16)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const float *beta,[rocblas_bfloat16](datatypes.html#_CPPv416rocblas_bfloat16)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv423rocblas_tstgemv_batched14rocblas_handle17rocblas_operation11rocblas_int11rocblas_intPKfA_PCK16rocblas_bfloat1611rocblas_intA_PCK16rocblas_bfloat1611rocblas_intPKfA_PC16rocblas_bfloat1611rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_tssgemv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const[rocblas_bfloat16](datatypes.html#_CPPv416rocblas_bfloat16)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_bfloat16](datatypes.html#_CPPv416rocblas_bfloat16)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const float *beta, float *const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv423rocblas_tssgemv_batched14rocblas_handle17rocblas_operation11rocblas_int11rocblas_intPKfA_PCK16rocblas_bfloat1611rocblas_intA_PCK16rocblas_bfloat1611rocblas_intPKfA_PCf11rocblas_int11rocblas_int) **BLAS Level 2 API**gemv_batched performs a batch of matrix-vector operations:

y_i := alpha*A_i*x_i + beta*y_i, or y_i := alpha*A_i**T*x_i + beta*y_i, or y_i := alpha*A_i**H*x_i + beta*y_i, where (A_i, x_i, y_i) is the i-th instance of the batch. alpha and beta are scalars, x_i and y_i are vectors and A_i is an m by n matrix, for i = 1, ..., batch_count.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**trans**–**[in]**[rocblas_operation] indicates whether matrices A_i are tranposed (conjugated) or not.**m**–**[in]**[rocblas_int] number of rows of each matrix A_i.**n**–**[in]**[rocblas_int] number of columns of each matrix A_i.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**A**–**[in]**device array of device pointers storing each matrix A_i.**lda**–**[in]**[rocblas_int] specifies the leading dimension of each matrix A_i.**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each vector x_i.**beta**–**[in]**device pointer or host pointer to scalar beta.**y**–**[inout]**device array of device pointers storing each vector y_i.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of each vector y_i.**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



`gemv_batched`

functions have an implementation which uses atomic operations. See the [Atomic operations](../conceptual/rocblas-design-notes.html#atomic-operations) section for more information.
The `gemv_batched`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sgemv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)strideA, const float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, const float *beta, float *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_sgemv_strided_batched14rocblas_handle17rocblas_operation11rocblas_int11rocblas_intPKfPKf11rocblas_int14rocblas_stridePKf11rocblas_int14rocblas_stridePKfPf11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dgemv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)strideA, const double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, const double *beta, double *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_dgemv_strided_batched14rocblas_handle17rocblas_operation11rocblas_int11rocblas_intPKdPKd11rocblas_int14rocblas_stridePKd11rocblas_int14rocblas_stridePKdPd11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cgemv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)strideA, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_cgemv_strided_batched14rocblas_handle17rocblas_operation11rocblas_int11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_int14rocblas_stridePK21rocblas_float_complex11rocblas_int14rocblas_stridePK21rocblas_float_complexP21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zgemv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)strideA, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_zgemv_strided_batched14rocblas_handle17rocblas_operation11rocblas_int11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_int14rocblas_stridePK22rocblas_double_complex11rocblas_int14rocblas_stridePK22rocblas_double_complexP22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_hshgemv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const[rocblas_half](datatypes.html#_CPPv412rocblas_half)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)strideA, const[rocblas_half](datatypes.html#_CPPv412rocblas_half)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, const float *beta,[rocblas_half](datatypes.html#_CPPv412rocblas_half)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv431rocblas_hshgemv_strided_batched14rocblas_handle17rocblas_operation11rocblas_int11rocblas_intPKfPK12rocblas_half11rocblas_int14rocblas_stridePK12rocblas_half11rocblas_int14rocblas_stridePKfP12rocblas_half11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_hssgemv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const[rocblas_half](datatypes.html#_CPPv412rocblas_half)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)strideA, const[rocblas_half](datatypes.html#_CPPv412rocblas_half)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, const float *beta, float *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv431rocblas_hssgemv_strided_batched14rocblas_handle17rocblas_operation11rocblas_int11rocblas_intPKfPK12rocblas_half11rocblas_int14rocblas_stridePK12rocblas_half11rocblas_int14rocblas_stridePKfPf11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_tstgemv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const[rocblas_bfloat16](datatypes.html#_CPPv416rocblas_bfloat16)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)strideA, const[rocblas_bfloat16](datatypes.html#_CPPv416rocblas_bfloat16)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, const float *beta,[rocblas_bfloat16](datatypes.html#_CPPv416rocblas_bfloat16)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv431rocblas_tstgemv_strided_batched14rocblas_handle17rocblas_operation11rocblas_int11rocblas_intPKfPK16rocblas_bfloat1611rocblas_int14rocblas_stridePK16rocblas_bfloat1611rocblas_int14rocblas_stridePKfP16rocblas_bfloat1611rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_tssgemv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const[rocblas_bfloat16](datatypes.html#_CPPv416rocblas_bfloat16)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)strideA, const[rocblas_bfloat16](datatypes.html#_CPPv416rocblas_bfloat16)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, const float *beta, float *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv431rocblas_tssgemv_strided_batched14rocblas_handle17rocblas_operation11rocblas_int11rocblas_intPKfPK16rocblas_bfloat1611rocblas_int14rocblas_stridePK16rocblas_bfloat1611rocblas_int14rocblas_stridePKfPf11rocblas_int14rocblas_stride11rocblas_int) **BLAS Level 2 API**gemv_strided_batched performs a batch of matrix-vector operations:

y_i := alpha*A_i*x_i + beta*y_i, or y_i := alpha*A_i**T*x_i + beta*y_i, or y_i := alpha*A_i**H*x_i + beta*y_i, where (A_i, x_i, y_i) is the i-th instance of the batch. alpha and beta are scalars, x_i and y_i are vectors and A_i is an m by n matrix, for i = 1, ..., batch_count.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**transA**–**[in]**[rocblas_operation] indicates whether matrices A_i are tranposed (conjugated) or not.**m**–**[in]**[rocblas_int] number of rows of matrices A_i.**n**–**[in]**[rocblas_int] number of columns of matrices A_i.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**A**–**[in]**device pointer to the first matrix (A_1) in the batch.**lda**–**[in]**[rocblas_int] specifies the leading dimension of matrices A_i.**strideA**–**[in]**[rocblas_stride] stride from the start of one matrix (A_i) and the next one (A_i+1).**x**–**[in]**device pointer to the first vector (x_1) in the batch.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of vectors x_i.**stridex**–**[in]**[rocblas_stride] stride from the start of one vector (x_i) and the next one (x_i+1). There are no restrictions placed on stride_x. However, ensure that stride_x is of appropriate size. When trans equals rocblas_operation_none this typically means stride_x >= n * incx, otherwise stride_x >= m * incx.**beta**–**[in]**device pointer or host pointer to scalar beta.**y**–**[inout]**device pointer to the first vector (y_1) in the batch.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of vectors y_i.**stridey**–**[in]**[rocblas_stride] stride from the start of one vector (y_i) and the next one (y_i+1). There are no restrictions placed on stride_y. However, ensure that stride_y is of appropriate size. When trans equals rocblas_operation_none this typically means stride_y >= m * incy, otherwise stride_y >= n * incy. stridey should be non zero.**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



`gemv_strided_batched`

functions have an implementation which uses atomic operations. See the [Atomic operations](../conceptual/rocblas-design-notes.html#atomic-operations) section for more information.
The `gemv_strided_batched`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xger + batched, strided_batched[#](#rocblas-xger-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sger([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const float *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy, float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda)[#](#_CPPv412rocblas_sger14rocblas_handle11rocblas_int11rocblas_intPKfPKf11rocblas_intPKf11rocblas_intPf11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dger([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const double *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy, double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda)[#](#_CPPv412rocblas_dger14rocblas_handle11rocblas_int11rocblas_intPKdPKd11rocblas_intPKd11rocblas_intPd11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cgeru([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda)[#](#_CPPv413rocblas_cgeru14rocblas_handle11rocblas_int11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_intPK21rocblas_float_complex11rocblas_intP21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zgeru([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda)[#](#_CPPv413rocblas_zgeru14rocblas_handle11rocblas_int11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_intPK22rocblas_double_complex11rocblas_intP22rocblas_double_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cgerc([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda)[#](#_CPPv413rocblas_cgerc14rocblas_handle11rocblas_int11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_intPK21rocblas_float_complex11rocblas_intP21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zgerc([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda)[#](#_CPPv413rocblas_zgerc14rocblas_handle11rocblas_int11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_intPK22rocblas_double_complex11rocblas_intP22rocblas_double_complex11rocblas_int) **BLAS Level 2 API**ger,geru,gerc performs the matrix-vector operations:

A := A + alpha*x*y**T , OR A := A + alpha*x*y**H for gerc where alpha is a scalar, x and y are vectors, and A is an m by n matrix.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**m**–**[in]**[rocblas_int] the number of rows of the matrix A.**n**–**[in]**[rocblas_int] the number of columns of the matrix A.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of x.**y**–**[in]**device pointer storing vector y.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of y.**A**–**[inout]**device pointer storing matrix A.**lda**–**[in]**[rocblas_int] specifies the leading dimension of A.



The `ger`

, `geru`

, and `gerc`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sger_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const float *const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy, float *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv420rocblas_sger_batched14rocblas_handle11rocblas_int11rocblas_intPKfA_PCKf11rocblas_intA_PCKf11rocblas_intA_PCf11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dger_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const double *const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy, double *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv420rocblas_dger_batched14rocblas_handle11rocblas_int11rocblas_intPKdA_PCKd11rocblas_intA_PCKd11rocblas_intA_PCd11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cgeru_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_cgeru_batched14rocblas_handle11rocblas_int11rocblas_intPK21rocblas_float_complexA_PCK21rocblas_float_complex11rocblas_intA_PCK21rocblas_float_complex11rocblas_intA_PC21rocblas_float_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zgeru_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_zgeru_batched14rocblas_handle11rocblas_int11rocblas_intPK22rocblas_double_complexA_PCK22rocblas_double_complex11rocblas_intA_PCK22rocblas_double_complex11rocblas_intA_PC22rocblas_double_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cgerc_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_cgerc_batched14rocblas_handle11rocblas_int11rocblas_intPK21rocblas_float_complexA_PCK21rocblas_float_complex11rocblas_intA_PCK21rocblas_float_complex11rocblas_intA_PC21rocblas_float_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zgerc_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_zgerc_batched14rocblas_handle11rocblas_int11rocblas_intPK22rocblas_double_complexA_PCK22rocblas_double_complex11rocblas_intA_PCK22rocblas_double_complex11rocblas_intA_PC22rocblas_double_complex11rocblas_int11rocblas_int) **BLAS Level 2 API**ger_batched,geru_batched,gerc_batched perform a batch of the matrix-vector operations:

A := A + alpha*x*y**T , OR A := A + alpha*x*y**H for gerc where (A_i, x_i, y_i) is the i-th instance of the batch. alpha is a scalar, x_i and y_i are vectors and A_i is an m by n matrix, for i = 1, ..., batch_count.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**m**–**[in]**[rocblas_int] the number of rows of each matrix A_i.**n**–**[in]**[rocblas_int] the number of columns of each matrix A_i.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each vector x_i.**y**–**[in]**device array of device pointers storing each vector y_i.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of each vector y_i.**A**–**[inout]**device array of device pointers storing each matrix A_i.**lda**–**[in]**[rocblas_int] specifies the leading dimension of each A_i.**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `ger`

, `geru`

, and `gerc_batched`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sger_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, const float *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey, float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)strideA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv428rocblas_sger_strided_batched14rocblas_handle11rocblas_int11rocblas_intPKfPKf11rocblas_int14rocblas_stridePKf11rocblas_int14rocblas_stridePf11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dger_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, const double *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey, double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)strideA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv428rocblas_dger_strided_batched14rocblas_handle11rocblas_int11rocblas_intPKdPKd11rocblas_int14rocblas_stridePKd11rocblas_int14rocblas_stridePd11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cgeru_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)strideA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_cgeru_strided_batched14rocblas_handle11rocblas_int11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_int14rocblas_stridePK21rocblas_float_complex11rocblas_int14rocblas_strideP21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zgeru_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)strideA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_zgeru_strided_batched14rocblas_handle11rocblas_int11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_int14rocblas_stridePK22rocblas_double_complex11rocblas_int14rocblas_strideP22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cgerc_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)strideA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_cgerc_strided_batched14rocblas_handle11rocblas_int11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_int14rocblas_stridePK21rocblas_float_complex11rocblas_int14rocblas_strideP21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zgerc_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)strideA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_zgerc_strided_batched14rocblas_handle11rocblas_int11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_int14rocblas_stridePK22rocblas_double_complex11rocblas_int14rocblas_strideP22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_int) **BLAS Level 2 API**ger_strided_batched,geru_strided_batched,gerc_strided_batched performs the matrix-vector operations:

A_i := A_i + alpha*x_i*y_i**T, OR A_i := A_i + alpha*x_i*y_i**H for gerc where (A_i, x_i, y_i) is the i-th instance of the batch. alpha is a scalar, x_i and y_i are vectors and A_i is an m by n matrix, for i = 1, ..., batch_count.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**m**–**[in]**[rocblas_int] the number of rows of each matrix A_i.**n**–**[in]**[rocblas_int] the number of columns of each matrix A_i.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device pointer to the first vector (x_1) in the batch.**incx**–**[in]**[rocblas_int] specifies the increments for the elements of each vector x_i.**stridex**–**[in]**[rocblas_stride] stride from the start of one vector (x_i) and the next one (x_i+1). There are no restrictions placed on stride_x. However, ensure that stride_x is of appropriate size. For a typical case this means stride_x >= m * incx.**y**–**[inout]**device pointer to the first vector (y_1) in the batch.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of each vector y_i.**stridey**–**[in]**[rocblas_stride] stride from the start of one vector (y_i) and the next one (y_i+1). There are no restrictions placed on stride_y. However, ensure that stride_y is of appropriate size. For a typical case this means stride_y >= n * incy.**A**–**[inout]**device pointer to the first matrix (A_1) in the batch.**lda**–**[in]**[rocblas_int] specifies the leading dimension of each A_i.**strideA**–**[in]**[rocblas_stride] stride from the start of one matrix (A_i) and the next one (A_i+1)**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `ger`

, `geru`

, and `gerc_strided_batched`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xsbmv + batched, strided_batched[#](#rocblas-xsbmv-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ssbmv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const float *alpha, const float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const float *beta, float *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy)[#](#_CPPv413rocblas_ssbmv14rocblas_handle12rocblas_fill11rocblas_int11rocblas_intPKfPKf11rocblas_intPKf11rocblas_intPKfPf11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dsbmv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const double *alpha, const double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const double *beta, double *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy)[#](#_CPPv413rocblas_dsbmv14rocblas_handle12rocblas_fill11rocblas_int11rocblas_intPKdPKd11rocblas_intPKd11rocblas_intPKdPd11rocblas_int) **BLAS Level 2 API**sbmv performs the matrix-vector operation:

y := alpha*A*x + beta*y where alpha and beta are scalars, x and y are n element vectors and A should contain an upper or lower triangular n by n symmetric banded matrix.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**rocblas_fill specifies whether the upper ‘rocblas_fill_upper’ or lower ‘rocblas_fill_lower’if rocblas_fill_upper, the lower part of A is not referenced

if rocblas_fill_lower, the upper part of A is not referenced


**n**–**[in]**[rocblas_int]**k**–**[in]**[rocblas_int] specifies the number of sub- and super-diagonals.**alpha**–**[in]**specifies the scalar alpha.**A**–**[in]**pointer storing matrix A on the GPU.**lda**–**[in]**[rocblas_int] specifies the leading dimension of matrix A.**x**–**[in]**pointer storing vector x on the GPU.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of x.**beta**–**[in]**specifies the scalar beta.**y**–**[out]**pointer storing vector y on the GPU.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of y.



The `sbmv`

functions support the `_64`

interface. Parameters `n`

and `k`

larger than `int32_t`

max value are not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ssbmv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const float *alpha, const float *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const float *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const float *beta, float *const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_ssbmv_batched14rocblas_handle12rocblas_fill11rocblas_int11rocblas_intPKfA_PCKf11rocblas_intA_PCKf11rocblas_intPKfA_PCf11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dsbmv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const double *alpha, const double *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const double *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const double *beta, double *const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_dsbmv_batched14rocblas_handle12rocblas_fill11rocblas_int11rocblas_intPKdA_PCKd11rocblas_intA_PCKd11rocblas_intPKdA_PCd11rocblas_int11rocblas_int) **BLAS Level 2 API**sbmv_batched performs the matrix-vector operation:

y_i := alpha*A_i*x_i + beta*y_i where (A_i, x_i, y_i) is the i-th instance of the batch. alpha and beta are scalars, x_i and y_i are vectors and A_i is an n by n symmetric banded matrix, for i = 1, ..., batch_count. A should contain an upper or lower triangular n by n symmetric banded matrix.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill] specifies whether the upper ‘rocblas_fill_upper’ or lower ‘rocblas_fill_lower’if rocblas_fill_upper, the lower part of A is not referenced

if rocblas_fill_lower, the upper part of A is not referenced


**n**–**[in]**[rocblas_int] number of rows and columns of each matrix A_i.**k**–**[in]**[rocblas_int] specifies the number of sub- and super-diagonals.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**A**–**[in]**device array of device pointers storing each matrix A_i.**lda**–**[in]**[rocblas_int] specifies the leading dimension of each matrix A_i.**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each vector x_i.**beta**–**[in]**device pointer or host pointer to scalar beta.**y**–**[out]**device array of device pointers storing each vector y_i.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of each vector y_i.**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `sbmv_batched`

functions support the `_64`

interface. Parameters `n`

and `k`

larger than `int32_t`

max value are not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ssbmv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const float *alpha, const float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)strideA, const float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, const float *beta, float *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_ssbmv_strided_batched14rocblas_handle12rocblas_fill11rocblas_int11rocblas_intPKfPKf11rocblas_int14rocblas_stridePKf11rocblas_int14rocblas_stridePKfPf11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dsbmv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const double *alpha, const double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)strideA, const double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, const double *beta, double *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_dsbmv_strided_batched14rocblas_handle12rocblas_fill11rocblas_int11rocblas_intPKdPKd11rocblas_int14rocblas_stridePKd11rocblas_int14rocblas_stridePKdPd11rocblas_int14rocblas_stride11rocblas_int) **BLAS Level 2 API**sbmv_strided_batched performs the matrix-vector operation:

y_i := alpha*A_i*x_i + beta*y_i where (A_i, x_i, y_i) is the i-th instance of the batch. alpha and beta are scalars, x_i and y_i are vectors and A_i is an n by n symmetric banded matrix, for i = 1, ..., batch_count. A should contain an upper or lower triangular n by n symmetric banded matrix.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill] specifies whether the upper ‘rocblas_fill_upper’ or lower ‘rocblas_fill_lower’if rocblas_fill_upper, the lower part of A is not referenced

if rocblas_fill_lower, the upper part of A is not referenced


**n**–**[in]**[rocblas_int] number of rows and columns of each matrix A_i.**k**–**[in]**[rocblas_int] specifies the number of sub- and super-diagonals.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**A**–**[in]**Device pointer to the first matrix A_1 on the GPU.**lda**–**[in]**[rocblas_int] specifies the leading dimension of each matrix A_i.**strideA**–**[in]**[rocblas_stride] stride from the start of one matrix (A_i) and the next one (A_i+1).**x**–**[in]**Device pointer to the first vector x_1 on the GPU.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each vector x_i.**stridex**–**[in]**[rocblas_stride] stride from the start of one vector (x_i) and the next one (x_i+1). There are no restrictions placed on stridex. However, ensure that stridex is of appropriate size. This typically means stridex >= n * incx. stridex should be non zero.**beta**–**[in]**device pointer or host pointer to scalar beta.**y**–**[out]**Device pointer to the first vector y_1 on the GPU.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of each vector y_i.**stridey**–**[in]**[rocblas_stride] stride from the start of one vector (y_i) and the next one (y_i+1). There are no restrictions placed on stridey. However, ensure that stridey is of appropriate size. This typically means stridey >= n * incy. stridey should be non zero.**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `sbmv_strided_batched`

functions support the `_64`

interface. Parameters `n`

and `k`

larger than `int32_t`

max value are not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xspmv + batched, strided_batched[#](#rocblas-xspmv-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sspmv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *A, const float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const float *beta, float *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy)[#](#_CPPv413rocblas_sspmv14rocblas_handle12rocblas_fill11rocblas_intPKfPKfPKf11rocblas_intPKfPf11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dspmv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *A, const double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const double *beta, double *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy)[#](#_CPPv413rocblas_dspmv14rocblas_handle12rocblas_fill11rocblas_intPKdPKdPKd11rocblas_intPKdPd11rocblas_int) **BLAS Level 2 API**spmv performs the matrix-vector operation:

y := alpha*A*x + beta*y where alpha and beta are scalars, x and y are n element vectors and A should contain an upper or lower triangular n by n packed symmetric matrix.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**rocblas_fill specifies whether the upper ‘rocblas_fill_upper’ or lower ‘rocblas_fill_lower’if rocblas_fill_upper, the lower part of A is not referenced

if rocblas_fill_lower, the upper part of A is not referenced


**n**–**[in]**[rocblas_int]**alpha**–**[in]**specifies the scalar alpha.**A**–**[in]**pointer storing matrix A on the GPU.**x**–**[in]**pointer storing vector x on the GPU.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of x.**beta**–**[in]**specifies the scalar beta.**y**–**[out]**pointer storing vector y on the GPU.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of y.



The `spmv`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sspmv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *const A[], const float *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const float *beta, float *const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_sspmv_batched14rocblas_handle12rocblas_fill11rocblas_intPKfA_PCKfA_PCKf11rocblas_intPKfA_PCf11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dspmv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *const A[], const double *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const double *beta, double *const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_dspmv_batched14rocblas_handle12rocblas_fill11rocblas_intPKdA_PCKdA_PCKd11rocblas_intPKdA_PCd11rocblas_int11rocblas_int) **BLAS Level 2 API**spmv_batched performs the matrix-vector operation:

y_i := alpha*A_i*x_i + beta*y_i where (A_i, x_i, y_i) is the i-th instance of the batch. alpha and beta are scalars, x_i and y_i are vectors and A_i is an n by n symmetric matrix, for i = 1, ..., batch_count. A should contain an upper or lower triangular n by n packed symmetric matrix.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill] specifies whether the upper ‘rocblas_fill_upper’ or lower ‘rocblas_fill_lower’if rocblas_fill_upper, the lower part of A is not referenced

if rocblas_fill_lower, the upper part of A is not referenced


**n**–**[in]**[rocblas_int] number of rows and columns of each matrix A_i.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**A**–**[in]**device array of device pointers storing each matrix A_i.**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each vector x_i.**beta**–**[in]**device pointer or host pointer to scalar beta.**y**–**[out]**device array of device pointers storing each vector y_i.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of each vector y_i.**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `spmv_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sspmv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *A,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)strideA, const float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, const float *beta, float *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_sspmv_strided_batched14rocblas_handle12rocblas_fill11rocblas_intPKfPKf14rocblas_stridePKf11rocblas_int14rocblas_stridePKfPf11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dspmv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *A,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)strideA, const double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, const double *beta, double *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_dspmv_strided_batched14rocblas_handle12rocblas_fill11rocblas_intPKdPKd14rocblas_stridePKd11rocblas_int14rocblas_stridePKdPd11rocblas_int14rocblas_stride11rocblas_int) **BLAS Level 2 API**spmv_strided_batched performs the matrix-vector operation:

y_i := alpha*A_i*x_i + beta*y_i where (A_i, x_i, y_i) is the i-th instance of the batch. alpha and beta are scalars, x_i and y_i are vectors and A_i is an n by n symmetric matrix, for i = 1, ..., batch_count. A should contain an upper or lower triangular n by n packed symmetric matrix.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill] specifies whether the upper ‘rocblas_fill_upper’ or lower ‘rocblas_fill_lower’if rocblas_fill_upper, the lower part of A is not referenced

if rocblas_fill_lower, the upper part of A is not referenced


**n**–**[in]**[rocblas_int] number of rows and columns of each matrix A_i.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**A**–**[in]**Device pointer to the first matrix A_1 on the GPU.**strideA**–**[in]**[rocblas_stride] stride from the start of one matrix (A_i) and the next one (A_i+1).**x**–**[in]**Device pointer to the first vector x_1 on the GPU.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each vector x_i.**stridex**–**[in]**[rocblas_stride] stride from the start of one vector (x_i) and the next one (x_i+1). There are no restrictions placed on stridex. However, ensure that stridex is of appropriate size. This typically means stridex >= n * incx. stridex should be non zero.**beta**–**[in]**device pointer or host pointer to scalar beta.**y**–**[out]**Device pointer to the first vector y_1 on the GPU.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of each vector y_i.**stridey**–**[in]**[rocblas_stride] stride from the start of one vector (y_i) and the next one (y_i+1). There are no restrictions placed on stridey. However, ensure that stridey is of appropriate size. This typically means stridey >= n * incy. stridey should be non zero.**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `spmv_strided_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xspr + batched, strided_batched[#](#rocblas-xspr-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sspr([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, float *AP)[#](#_CPPv412rocblas_sspr14rocblas_handle12rocblas_fill11rocblas_intPKfPKf11rocblas_intPf)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dspr([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, double *AP)[#](#_CPPv412rocblas_dspr14rocblas_handle12rocblas_fill11rocblas_intPKdPKd11rocblas_intPd)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cspr([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*AP)[#](#_CPPv412rocblas_cspr14rocblas_handle12rocblas_fill11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_intP21rocblas_float_complex)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zspr([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*AP)[#](#_CPPv412rocblas_zspr14rocblas_handle12rocblas_fill11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_intP22rocblas_double_complex) **BLAS Level 2 API**spr performs the matrix-vector operations:

A := A + alpha*x*x**T where alpha is a scalar, x is a vector, and A is an n by n symmetric matrix, supplied in packed form.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill] specifies whether the upper ‘rocblas_fill_upper’ or lower ‘rocblas_fill_lower’rocblas_fill_upper: The upper triangular part of A is supplied in AP.

rocblas_fill_lower: The lower triangular part of A is supplied in AP.


**n**–**[in]**[rocblas_int] the number of rows and columns of matrix A. Must be at least 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of x.**AP**–**[inout]**device pointer storing the packed version of the specified triangular portion of the symmetric matrix A. Of at least size ((n * (n + 1)) / 2).if uplo == rocblas_fill_upper: The upper triangular portion of the symmetric matrix A is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(0,1) AP(2) = A(1,1), etc. Ex: (rocblas_fill_upper; n = 4) 1 2 4 7 2 3 5 8 -----> [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] 4 5 6 9 7 8 9 0 if uplo == rocblas_fill_lower: The lower triangular portion of the symmetric matrix A is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(1,0) AP(2) = A(2,1), etc. Ex: (rocblas_fill_lower; n = 4) 1 2 3 4 2 5 6 7 -----> [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] 3 6 8 9 4 7 9 0




The `spr`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sspr_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, float *const AP[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv420rocblas_sspr_batched14rocblas_handle12rocblas_fill11rocblas_intPKfA_PCKf11rocblas_intA_PCf11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dspr_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, double *const AP[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv420rocblas_dspr_batched14rocblas_handle12rocblas_fill11rocblas_intPKdA_PCKd11rocblas_intA_PCd11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cspr_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const AP[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv420rocblas_cspr_batched14rocblas_handle12rocblas_fill11rocblas_intPK21rocblas_float_complexA_PCK21rocblas_float_complex11rocblas_intA_PC21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zspr_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const AP[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv420rocblas_zspr_batched14rocblas_handle12rocblas_fill11rocblas_intPK22rocblas_double_complexA_PCK22rocblas_double_complex11rocblas_intA_PC22rocblas_double_complex11rocblas_int) **BLAS Level 2 API**spr_batched performs the matrix-vector operations:

A_i := A_i + alpha*x_i*x_i**T where alpha is a scalar, x_i is a vector, and A_i is an n by n symmetric matrix, supplied in packed form, for i = 1, ..., batch_count.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill] specifies whether the upper ‘rocblas_fill_upper’ or lower ‘rocblas_fill_lower’rocblas_fill_upper: The upper triangular part of each A_i is supplied in AP.

rocblas_fill_lower: The lower triangular part of each A_i is supplied in AP.


**n**–**[in]**[rocblas_int] the number of rows and columns of each matrix A_i. Must be at least 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i.**AP**–**[inout]**device array of device pointers storing the packed version of the specified triangular portion of each symmetric matrix A_i of at least size ((n * (n + 1)) / 2). Array is of at least size batch_count.if uplo == rocblas_fill_upper: The upper triangular portion of each symmetric matrix A_i is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(0,1) AP(2) = A(1,1), etc. Ex: (rocblas_fill_upper; n = 4) 1 2 4 7 2 3 5 8 -----> [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] 4 5 6 9 7 8 9 0 if uplo == rocblas_fill_lower: The lower triangular portion of each symmetric matrix A_i is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(1,0) AP(2) = A(2,1), etc. Ex: (rocblas_fill_lower; n = 4) 1 2 3 4 2 5 6 7 -----> [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] 3 6 8 9 4 7 9 0

**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `spr_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sspr_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x, float *AP,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv428rocblas_sspr_strided_batched14rocblas_handle12rocblas_fill11rocblas_intPKfPKf11rocblas_int14rocblas_stridePf14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dspr_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x, double *AP,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv428rocblas_dspr_strided_batched14rocblas_handle12rocblas_fill11rocblas_intPKdPKd11rocblas_int14rocblas_stridePd14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cspr_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*AP,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv428rocblas_cspr_strided_batched14rocblas_handle12rocblas_fill11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_int14rocblas_strideP21rocblas_float_complex14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zspr_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*AP,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv428rocblas_zspr_strided_batched14rocblas_handle12rocblas_fill11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_int14rocblas_strideP22rocblas_double_complex14rocblas_stride11rocblas_int) **BLAS Level 2 API**spr_strided_batched performs the matrix-vector operations:

A_i := A_i + alpha*x_i*x_i**T where alpha is a scalar, x_i is a vector, and A_i is an n by n symmetric matrix, supplied in packed form, for i = 1, ..., batch_count.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill] specifies whether the upper ‘rocblas_fill_upper’ or lower ‘rocblas_fill_lower’rocblas_fill_upper: The upper triangular part of each A_i is supplied in AP.

rocblas_fill_lower: The lower triangular part of each A_i is supplied in AP.


**n**–**[in]**[rocblas_int] the number of rows and columns of each matrix A_i. Must be at least 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device pointer pointing to the first vector (x_1).**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i.**stride_x**–**[in]**[rocblas_stride] stride from the start of one vector (x_i) and the next one (x_i+1).**AP**–**[inout]**device pointer storing the packed version of the specified triangular portion of each symmetric matrix A_i. Points to the first A_1.if uplo == rocblas_fill_upper: The upper triangular portion of each symmetric matrix A_i is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(0,1) AP(2) = A(1,1), etc. Ex: (rocblas_fill_upper; n = 4) 1 2 4 7 2 3 5 8 -----> [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] 4 5 6 9 7 8 9 0 if uplo == rocblas_fill_lower: The lower triangular portion of each symmetric matrix A_i is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(1,0) AP(2) = A(2,1), etc. Ex: (rocblas_fill_lower; n = 4) 1 2 3 4 2 5 6 7 -----> [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] 3 6 8 9 4 7 9 0

**stride_A**–**[in]**[rocblas_stride] stride from the start of one (A_i) and the next (A_i+1).**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `spr_strided_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xspr2 + batched, strided_batched[#](#rocblas-xspr2-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sspr2([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const float *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy, float *AP)[#](#_CPPv413rocblas_sspr214rocblas_handle12rocblas_fill11rocblas_intPKfPKf11rocblas_intPKf11rocblas_intPf)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dspr2([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const double *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy, double *AP)[#](#_CPPv413rocblas_dspr214rocblas_handle12rocblas_fill11rocblas_intPKdPKd11rocblas_intPKd11rocblas_intPd) **BLAS Level 2 API**spr2 performs the matrix-vector operation:

A := A + alpha*x*y**T + alpha*y*x**T where alpha is a scalar, x and y are vectors, and A is an n by n symmetric matrix, supplied in packed form.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill] specifies whether the upper ‘rocblas_fill_upper’ or lower ‘rocblas_fill_lower’rocblas_fill_upper: The upper triangular part of A is supplied in AP.

rocblas_fill_lower: The lower triangular part of A is supplied in AP.


**n**–**[in]**[rocblas_int] the number of rows and columns of matrix A. Must be at least 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of x.**y**–**[in]**device pointer storing vector y.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of y.**AP**–**[inout]**device pointer storing the packed version of the specified triangular portion of the symmetric matrix A. Of at least size ((n * (n + 1)) / 2).if uplo == rocblas_fill_upper: The upper triangular portion of the symmetric matrix A is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(0,1) AP(2) = A(1,1), etc. Ex: (rocblas_fill_upper; n = 4) 1 2 4 7 2 3 5 8 -----> [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] 4 5 6 9 7 8 9 0 if uplo == rocblas_fill_lower: The lower triangular portion of the symmetric matrix A is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(1,0) AP(n) = A(2,1), etc. Ex: (rocblas_fill_lower; n = 4) 1 2 3 4 2 5 6 7 -----> [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] 3 6 8 9 4 7 9 0




The `spr2`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sspr2_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const float *const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy, float *const AP[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_sspr2_batched14rocblas_handle12rocblas_fill11rocblas_intPKfA_PCKf11rocblas_intA_PCKf11rocblas_intA_PCf11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dspr2_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const double *const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy, double *const AP[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_dspr2_batched14rocblas_handle12rocblas_fill11rocblas_intPKdA_PCKd11rocblas_intA_PCKd11rocblas_intA_PCd11rocblas_int) **BLAS Level 2 API**spr2_batched performs the matrix-vector operation:

A_i := A_i + alpha*x_i*y_i**T + alpha*y_i*x_i**T where alpha is a scalar, x_i and y_i are vectors, and A_i is an n by n symmetric matrix, supplied in packed form, for i = 1, ..., batch_count.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill] specifies whether the upper ‘rocblas_fill_upper’ or lower ‘rocblas_fill_lower’rocblas_fill_upper: The upper triangular part of each A_i is supplied in AP.

rocblas_fill_lower: The lower triangular part of each A_i is supplied in AP.


**n**–**[in]**[rocblas_int] the number of rows and columns of each matrix A_i. Must be at least 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i.**y**–**[in]**device array of device pointers storing each vector y_i.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of each y_i.**AP**–**[inout]**device array of device pointers storing the packed version of the specified triangular portion of each symmetric matrix A_i of at least size ((n * (n + 1)) / 2). Array is of at least size batch_count.if uplo == rocblas_fill_upper: The upper triangular portion of each symmetric matrix A_i is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(0,1) AP(2) = A(1,1), etc. Ex: (rocblas_fill_upper; n = 4) 1 2 4 7 2 3 5 8 -----> [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] 4 5 6 9 7 8 9 0 if uplo == rocblas_fill_lower: The lower triangular portion of each symmetric matrix A_i is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(1,0) AP(n) = A(2,1), etc. Ex: (rocblas_fill_lower; n = 4) 1 2 3 4 2 5 6 7 -----> [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] 3 6 8 9 4 7 9 0

**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `spr2_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sspr2_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x, const float *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_y, float *AP,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_sspr2_strided_batched14rocblas_handle12rocblas_fill11rocblas_intPKfPKf11rocblas_int14rocblas_stridePKf11rocblas_int14rocblas_stridePf14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dspr2_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x, const double *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_y, double *AP,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_dspr2_strided_batched14rocblas_handle12rocblas_fill11rocblas_intPKdPKd11rocblas_int14rocblas_stridePKd11rocblas_int14rocblas_stridePd14rocblas_stride11rocblas_int) **BLAS Level 2 API**spr2_strided_batched performs the matrix-vector operation:

A_i := A_i + alpha*x_i*y_i**T + alpha*y_i*x_i**T where alpha is a scalar, x_i and y_i are vectors, and A_i is an n by n symmetric matrix, supplied in packed form, for i = 1, ..., batch_count.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill] specifies whether the upper ‘rocblas_fill_upper’ or lower ‘rocblas_fill_lower’rocblas_fill_upper: The upper triangular part of each A_i is supplied in AP.

rocblas_fill_lower: The lower triangular part of each A_i is supplied in AP.


**n**–**[in]**[rocblas_int] the number of rows and columns of each matrix A_i. Must be at least 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device pointer pointing to the first vector (x_1).**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i.**stride_x**–**[in]**[rocblas_stride] stride from the start of one vector (x_i) and the next one (x_i+1).**y**–**[in]**device pointer pointing to the first vector (y_1).**incy**–**[in]**[rocblas_int] specifies the increment for the elements of each y_i.**stride_y**–**[in]**[rocblas_stride] stride from the start of one vector (y_i) and the next one (y_i+1).**AP**–**[inout]**device pointer storing the packed version of the specified triangular portion of each symmetric matrix A_i. Points to the first A_1.if uplo == rocblas_fill_upper: The upper triangular portion of each symmetric matrix A_i is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(0,1) AP(2) = A(1,1), etc. Ex: (rocblas_fill_upper; n = 4) 1 2 4 7 2 3 5 8 -----> [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] 4 5 6 9 7 8 9 0 if uplo == rocblas_fill_lower: The lower triangular portion of each symmetric matrix A_i is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(1,0) AP(n) = A(2,1), etc. Ex: (rocblas_fill_lower; n = 4) 1 2 3 4 2 5 6 7 -----> [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] 3 6 8 9 4 7 9 0

**stride_A**–**[in]**[rocblas_stride] stride from the start of one (A_i) and the next (A_i+1).**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `spr2_strided_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xsymv + batched, strided_batched[#](#rocblas-xsymv-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ssymv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const float *beta, float *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy)[#](#_CPPv413rocblas_ssymv14rocblas_handle12rocblas_fill11rocblas_intPKfPKf11rocblas_intPKf11rocblas_intPKfPf11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dsymv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const double *beta, double *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy)[#](#_CPPv413rocblas_dsymv14rocblas_handle12rocblas_fill11rocblas_intPKdPKd11rocblas_intPKd11rocblas_intPKdPd11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_csymv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy)[#](#_CPPv413rocblas_csymv14rocblas_handle12rocblas_fill11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_intPK21rocblas_float_complex11rocblas_intPK21rocblas_float_complexP21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zsymv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy)[#](#_CPPv413rocblas_zsymv14rocblas_handle12rocblas_fill11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_intPK22rocblas_double_complex11rocblas_intPK22rocblas_double_complexP22rocblas_double_complex11rocblas_int) **BLAS Level 2 API**symv performs the matrix-vector operation:

symv has an implementation which uses atomic operations. See Atomic Operations in the API Reference Guide for more information.y := alpha*A*x + beta*y where alpha and beta are scalars, x and y are n element vectors and A should contain an upper or lower triangular n by n symmetric matrix.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill] specifies whether the upper ‘rocblas_fill_upper’ or lower ‘rocblas_fill_lower’if rocblas_fill_upper, the lower part of A is not referenced.

if rocblas_fill_lower, the upper part of A is not referenced.


**n**–**[in]**[rocblas_int]**alpha**–**[in]**specifies the scalar alpha.**A**–**[in]**pointer storing matrix A on the GPU**lda**–**[in]**[rocblas_int] specifies the leading dimension of A.**x**–**[in]**pointer storing vector x on the GPU.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of x.**beta**–**[in]**specifies the scalar beta**y**–**[out]**pointer storing vector y on the GPU.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of y.



The `symv`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ssymv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const float *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const float *beta, float *const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_ssymv_batched14rocblas_handle12rocblas_fill11rocblas_intPKfA_PCKf11rocblas_intA_PCKf11rocblas_intPKfA_PCf11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dsymv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const double *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const double *beta, double *const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_dsymv_batched14rocblas_handle12rocblas_fill11rocblas_intPKdA_PCKd11rocblas_intA_PCKd11rocblas_intPKdA_PCd11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_csymv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_csymv_batched14rocblas_handle12rocblas_fill11rocblas_intPK21rocblas_float_complexA_PCK21rocblas_float_complex11rocblas_intA_PCK21rocblas_float_complex11rocblas_intPK21rocblas_float_complexA_PC21rocblas_float_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zsymv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_zsymv_batched14rocblas_handle12rocblas_fill11rocblas_intPK22rocblas_double_complexA_PCK22rocblas_double_complex11rocblas_intA_PCK22rocblas_double_complex11rocblas_intPK22rocblas_double_complexA_PC22rocblas_double_complex11rocblas_int11rocblas_int) **BLAS Level 2 API**symv_batched performs the matrix-vector operation:

y_i := alpha*A_i*x_i + beta*y_i where (A_i, x_i, y_i) is the i-th instance of the batch. alpha and beta are scalars, x_i and y_i are vectors and A_i is an n by n symmetric matrix, for i = 1, ..., batch_count. A a should contain an upper or lower triangular symmetric matrix and the opposing triangular part of A is not referenced.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue**uplo**–**[in]**[rocblas_fill] specifies whether the upper ‘rocblas_fill_upper’ or lower ‘rocblas_fill_lower’if rocblas_fill_upper, the lower part of A is not referenced.

if rocblas_fill_lower, the upper part of A is not referenced.


**n**–**[in]**[rocblas_int] number of rows and columns of each matrix A_i.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**A**–**[in]**device array of device pointers storing each matrix A_i.**lda**–**[in]**[rocblas_int] specifies the leading dimension of each matrix A_i.**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each vector x_i.**beta**–**[in]**device pointer or host pointer to scalar beta.**y**–**[out]**device array of device pointers storing each vector y_i.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of each vector y_i.**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `symv_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ssymv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)strideA, const float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, const float *beta, float *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_ssymv_strided_batched14rocblas_handle12rocblas_fill11rocblas_intPKfPKf11rocblas_int14rocblas_stridePKf11rocblas_int14rocblas_stridePKfPf11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dsymv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)strideA, const double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, const double *beta, double *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_dsymv_strided_batched14rocblas_handle12rocblas_fill11rocblas_intPKdPKd11rocblas_int14rocblas_stridePKd11rocblas_int14rocblas_stridePKdPd11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_csymv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)strideA, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_csymv_strided_batched14rocblas_handle12rocblas_fill11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_int14rocblas_stridePK21rocblas_float_complex11rocblas_int14rocblas_stridePK21rocblas_float_complexP21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zsymv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)strideA, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_zsymv_strided_batched14rocblas_handle12rocblas_fill11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_int14rocblas_stridePK22rocblas_double_complex11rocblas_int14rocblas_stridePK22rocblas_double_complexP22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_int) **BLAS Level 2 API**symv_strided_batched performs the matrix-vector operation:

y_i := alpha*A_i*x_i + beta*y_i where (A_i, x_i, y_i) is the i-th instance of the batch. alpha and beta are scalars, x_i and y_i are vectors and A_i is an n by n symmetric matrix, for i = 1, ..., batch_count. A a should contain an upper or lower triangular symmetric matrix and the opposing triangular part of A is not referenced.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue**uplo**–**[in]**[rocblas_fill] specifies whether the upper ‘rocblas_fill_upper’ or lower ‘rocblas_fill_lower’if rocblas_fill_upper, the lower part of A is not referenced

if rocblas_fill_lower, the upper part of A is not referenced


**n**–**[in]**[rocblas_int] number of rows and columns of each matrix A_i.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**A**–**[in]**Device pointer to the first matrix A_1 on the GPU.**lda**–**[in]**[rocblas_int] specifies the leading dimension of each matrix A_i.**strideA**–**[in]**[rocblas_stride] stride from the start of one matrix (A_i) and the next one (A_i+1).**x**–**[in]**Device pointer to the first vector x_1 on the GPU.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each vector x_i.**stridex**–**[in]**[rocblas_stride] stride from the start of one vector (x_i) and the next one (x_i+1). There are no restrictions placed on stride_x. However, ensure that stridex is of appropriate size. This typically means stridex >= n * incx. stridex should be non zero.**beta**–**[in]**device pointer or host pointer to scalar beta.**y**–**[out]**Device pointer to the first vector y_1 on the GPU.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of each vector y_i.**stridey**–**[in]**[rocblas_stride] stride from the start of one vector (y_i) and the next one (y_i+1). There are no restrictions placed on stride_y. However, ensure that stridey is of appropriate size. This typically means stridey >= n * incy. stridey should be non zero.**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `symv_strided_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xsyr + batched, strided_batched[#](#rocblas-xsyr-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ssyr([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda)[#](#_CPPv412rocblas_ssyr14rocblas_handle12rocblas_fill11rocblas_intPKfPKf11rocblas_intPf11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dsyr([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda)[#](#_CPPv412rocblas_dsyr14rocblas_handle12rocblas_fill11rocblas_intPKdPKd11rocblas_intPd11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_csyr([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda)[#](#_CPPv412rocblas_csyr14rocblas_handle12rocblas_fill11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_intP21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zsyr([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda)[#](#_CPPv412rocblas_zsyr14rocblas_handle12rocblas_fill11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_intP22rocblas_double_complex11rocblas_int) **BLAS Level 2 API**syr performs the matrix-vector operations:

A := A + alpha*x*x**T where alpha is a scalar, x is a vector, and A is an n by n symmetric matrix.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill] specifies whether the upper ‘rocblas_fill_upper’ or lower ‘rocblas_fill_lower’if rocblas_fill_upper, the lower part of A is not referenced

if rocblas_fill_lower, the upper part of A is not referenced


**n**–**[in]**[rocblas_int] the number of rows and columns of matrix A.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of x.**A**–**[inout]**device pointer storing matrix A.**lda**–**[in]**[rocblas_int] specifies the leading dimension of A.



The `syr`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ssyr_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, float *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv420rocblas_ssyr_batched14rocblas_handle12rocblas_fill11rocblas_intPKfA_PCKf11rocblas_intA_PCf11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dsyr_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, double *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv420rocblas_dsyr_batched14rocblas_handle12rocblas_fill11rocblas_intPKdA_PCKd11rocblas_intA_PCd11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_csyr_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv420rocblas_csyr_batched14rocblas_handle12rocblas_fill11rocblas_intPK21rocblas_float_complexA_PCK21rocblas_float_complex11rocblas_intA_PC21rocblas_float_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zsyr_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv420rocblas_zsyr_batched14rocblas_handle12rocblas_fill11rocblas_intPK22rocblas_double_complexA_PCK22rocblas_double_complex11rocblas_intA_PC22rocblas_double_complex11rocblas_int11rocblas_int) **BLAS Level 2 API**syr_batched performs a batch of matrix-vector operations:

A[i] := A[i] + alpha*x[i]*x[i]**T where alpha is a scalar, x is an array of vectors, and A is an array of n by n symmetric matrices, for i = 1 , ... , batch_count.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill] specifies whether the upper ‘rocblas_fill_upper’ or lower ‘rocblas_fill_lower’if rocblas_fill_upper, the lower part of A is not referenced

if rocblas_fill_lower, the upper part of A is not referenced


**n**–**[in]**[rocblas_int] the number of rows and columns of matrix A.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i.**A**–**[inout]**device array of device pointers storing each matrix A_i.**lda**–**[in]**[rocblas_int] specifies the leading dimension of each A_i.**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `syr_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ssyr_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)strideA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv428rocblas_ssyr_strided_batched14rocblas_handle12rocblas_fill11rocblas_intPKfPKf11rocblas_int14rocblas_stridePf11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dsyr_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)strideA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv428rocblas_dsyr_strided_batched14rocblas_handle12rocblas_fill11rocblas_intPKdPKd11rocblas_int14rocblas_stridePd11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_csyr_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)strideA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv428rocblas_csyr_strided_batched14rocblas_handle12rocblas_fill11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_int14rocblas_strideP21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zsyr_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)strideA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv428rocblas_zsyr_strided_batched14rocblas_handle12rocblas_fill11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_int14rocblas_strideP22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_int) **BLAS Level 2 API**syr_strided_batched performs the matrix-vector operations:

A[i] := A[i] + alpha*x[i]*x[i]**T where alpha is a scalar, vectors, and A is an array of n by n symmetric matrices, for i = 1 , ... , batch_count.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill] specifies whether the upper ‘rocblas_fill_upper’ or lower ‘rocblas_fill_lower’if rocblas_fill_upper, the lower part of A is not referenced

if rocblas_fill_lower, the upper part of A is not referenced


**n**–**[in]**[rocblas_int] the number of rows and columns of each matrix A.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device pointer to the first vector x_1.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i.**stridex**–**[in]**[rocblas_stride] specifies the pointer increment between vectors (x_i) and (x_i+1).**A**–**[inout]**device pointer to the first matrix A_1.**lda**–**[in]**[rocblas_int] specifies the leading dimension of each A_i.**strideA**–**[in]**[rocblas_stride] stride from the start of one matrix (A_i) and the next one (A_i+1).**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `syr_strided_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xsyr2 + batched, strided_batched[#](#rocblas-xsyr2-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ssyr2([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const float *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy, float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda)[#](#_CPPv413rocblas_ssyr214rocblas_handle12rocblas_fill11rocblas_intPKfPKf11rocblas_intPKf11rocblas_intPf11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dsyr2([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const double *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy, double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda)[#](#_CPPv413rocblas_dsyr214rocblas_handle12rocblas_fill11rocblas_intPKdPKd11rocblas_intPKd11rocblas_intPd11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_csyr2([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda)[#](#_CPPv413rocblas_csyr214rocblas_handle12rocblas_fill11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_intPK21rocblas_float_complex11rocblas_intP21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zsyr2([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda)[#](#_CPPv413rocblas_zsyr214rocblas_handle12rocblas_fill11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_intPK22rocblas_double_complex11rocblas_intP22rocblas_double_complex11rocblas_int) **BLAS Level 2 API**syr2 performs the matrix-vector operations:

A := A + alpha*x*y**T + alpha*y*x**T where alpha is a scalar, x and y are vectors, and A is an n by n symmetric matrix.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill] specifies whether the upper ‘rocblas_fill_upper’ or lower ‘rocblas_fill_lower’if rocblas_fill_upper, the lower part of A is not referenced

if rocblas_fill_lower, the upper part of A is not referenced


**n**–**[in]**[rocblas_int] the number of rows and columns of matrix A.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of x.**y**–**[in]**device pointer storing vector y.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of y.**A**–**[inout]**device pointer storing matrix A.**lda**–**[in]**[rocblas_int] specifies the leading dimension of A.



The `syr2`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ssyr2_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const float *const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy, float *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_ssyr2_batched14rocblas_handle12rocblas_fill11rocblas_intPKfA_PCKf11rocblas_intA_PCKf11rocblas_intA_PCf11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dsyr2_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const double *const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy, double *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_dsyr2_batched14rocblas_handle12rocblas_fill11rocblas_intPKdA_PCKd11rocblas_intA_PCKd11rocblas_intA_PCd11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_csyr2_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_csyr2_batched14rocblas_handle12rocblas_fill11rocblas_intPK21rocblas_float_complexA_PCK21rocblas_float_complex11rocblas_intA_PCK21rocblas_float_complex11rocblas_intA_PC21rocblas_float_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zsyr2_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_zsyr2_batched14rocblas_handle12rocblas_fill11rocblas_intPK22rocblas_double_complexA_PCK22rocblas_double_complex11rocblas_intA_PCK22rocblas_double_complex11rocblas_intA_PC22rocblas_double_complex11rocblas_int11rocblas_int) **BLAS Level 2 API**syr2_batched performs a batch of matrix-vector operations:

A[i] := A[i] + alpha*x[i]*y[i]**T + alpha*y[i]*x[i]**T where alpha is a scalar, x[i] and y[i] are vectors, and A[i] is a n by n symmetric matrix, for i = 1 , ... , batch_count.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill] specifies whether the upper ‘rocblas_fill_upper’ or lower ‘rocblas_fill_lower’if rocblas_fill_upper, the lower part of A is not referenced

if rocblas_fill_lower, the upper part of A is not referenced


**n**–**[in]**[rocblas_int] the number of rows and columns of matrix A.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i.**y**–**[in]**device array of device pointers storing each vector y_i.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of each y_i.**A**–**[inout]**device array of device pointers storing each matrix A_i.**lda**–**[in]**[rocblas_int] specifies the leading dimension of each A_i.**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `syr2_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ssyr2_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, const float *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey, float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)strideA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_ssyr2_strided_batched14rocblas_handle12rocblas_fill11rocblas_intPKfPKf11rocblas_int14rocblas_stridePKf11rocblas_int14rocblas_stridePf11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dsyr2_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, const double *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey, double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)strideA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_dsyr2_strided_batched14rocblas_handle12rocblas_fill11rocblas_intPKdPKd11rocblas_int14rocblas_stridePKd11rocblas_int14rocblas_stridePd11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_csyr2_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)strideA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_csyr2_strided_batched14rocblas_handle12rocblas_fill11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_int14rocblas_stridePK21rocblas_float_complex11rocblas_int14rocblas_strideP21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zsyr2_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)strideA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_zsyr2_strided_batched14rocblas_handle12rocblas_fill11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_int14rocblas_stridePK22rocblas_double_complex11rocblas_int14rocblas_strideP22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_int) **BLAS Level 2 API**syr2_strided_batched the matrix-vector operations:

A[i] := A[i] + alpha*x[i]*y[i]**T + alpha*y[i]*x[i]**T where alpha is a scalar, x[i] and y[i] are vectors, and A[i] is a n by n symmetric matrices, for i = 1 , ... , batch_count

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill] specifies whether the upper ‘rocblas_fill_upper’ or lower ‘rocblas_fill_lower’if rocblas_fill_upper, the lower part of A is not referenced

if rocblas_fill_lower, the upper part of A is not referenced


**n**–**[in]**[rocblas_int] the number of rows and columns of each matrix A.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device pointer to the first vector x_1.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i.**stridex**–**[in]**[rocblas_stride] specifies the pointer increment between vectors (x_i) and (x_i+1).**y**–**[in]**device pointer to the first vector y_1.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of each y_i.**stridey**–**[in]**[rocblas_stride] specifies the pointer increment between vectors (y_i) and (y_i+1).**A**–**[inout]**device pointer to the first matrix A_1.**lda**–**[in]**[rocblas_int] specifies the leading dimension of each A_i.**strideA**–**[in]**[rocblas_stride] stride from the start of one matrix (A_i) and the next one (A_i+1).**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `syr2_strided_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xtbmv + batched, strided_batched[#](#rocblas-xtbmv-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_stbmv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx)[#](#_CPPv413rocblas_stbmv14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPKf11rocblas_intPf11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dtbmv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx)[#](#_CPPv413rocblas_dtbmv14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPKd11rocblas_intPd11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ctbmv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx)[#](#_CPPv413rocblas_ctbmv14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPK21rocblas_float_complex11rocblas_intP21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ztbmv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx)[#](#_CPPv413rocblas_ztbmv14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPK22rocblas_double_complex11rocblas_intP22rocblas_double_complex11rocblas_int) **BLAS Level 2 API**tbmv performs one of the matrix-vector operations:

x := A*x or x := A**T*x or x := A**H*x, x is a vectors and A is a banded n by n matrix (see description below).

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: A is an upper banded triangular matrix.

rocblas_fill_lower: A is a lower banded triangular matrix.


**trans**–**[in]**[rocblas_operation] indicates whether matrix A is tranposed (conjugated) or not.**diag**–**[in]**[rocblas_diagonal]rocblas_diagonal_unit: The main diagonal of A is assumed to consist of only 1’s and is not referenced.

rocblas_diagonal_non_unit: No assumptions are made of A’s main diagonal.


**n**–**[in]**[rocblas_int] the number of rows and columns of the matrix represented by A.**k**–**[in]**[rocblas_int]if uplo == rocblas_fill_upper, k specifies the number of super-diagonals of the matrix A. if uplo == rocblas_fill_lower, k specifies the number of sub-diagonals of the matrix A. k must satisfy k > 0 && k < lda.

**A**–**[in]**device pointer storing banded triangular matrix A.if uplo == rocblas_fill_upper: The matrix represented is an upper banded triangular matrix with the main diagonal and k super-diagonals, everything else can be assumed to be 0. The matrix is compacted so that the main diagonal resides on the k'th row, the first super diagonal resides on the RHS of the k-1'th row, etc, with the k'th diagonal on the RHS of the 0'th row. Ex: (rocblas_fill_upper; n = 5; k = 2) 1 6 9 0 0 0 0 9 8 7 0 2 7 8 0 0 6 7 8 9 0 0 3 8 7 ----> 1 2 3 4 5 0 0 0 4 9 0 0 0 0 0 0 0 0 0 5 0 0 0 0 0 if uplo == rocblas_fill_lower: The matrix represnted is a lower banded triangular matrix with the main diagonal and k sub-diagonals, everything else can be assumed to be 0. The matrix is compacted so that the main diagonal resides on the 0'th row, working up to the k'th diagonal residing on the LHS of the k'th row. Ex: (rocblas_fill_lower; n = 5; k = 2) 1 0 0 0 0 1 2 3 4 5 6 2 0 0 0 6 7 8 9 0 9 7 3 0 0 ----> 9 8 7 0 0 0 8 8 4 0 0 0 0 0 0 0 0 7 9 5 0 0 0 0 0

**lda**–**[in]**[rocblas_int] specifies the leading dimension of A. lda must satisfy lda > k.**x**–**[inout]**device pointer storing vector x.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of x.



The `tbmv`

functions support the `_64`

interface. Parameters `n`

and `k`

larger than `int32_t`

max value are not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_stbmv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const float *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, float *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_stbmv_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intA_PCKf11rocblas_intA_PCf11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dtbmv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const double *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, double *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_dtbmv_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intA_PCKd11rocblas_intA_PCd11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ctbmv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_ctbmv_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intA_PCK21rocblas_float_complex11rocblas_intA_PC21rocblas_float_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ztbmv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_ztbmv_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intA_PCK22rocblas_double_complex11rocblas_intA_PC22rocblas_double_complex11rocblas_int11rocblas_int) **BLAS Level 2 API**tbmv_batched performs one of the matrix-vector operations:

x_i := A_i*x_i or x_i := A_i**T*x_i or x_i := A_i**H*x_i, where (A_i, x_i) is the i-th instance of the batch. x_i is a vector and A_i is an n by n matrix, for i = 1, ..., batch_count.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: each A_i is an upper banded triangular matrix.

rocblas_fill_lower: each A_i is a lower banded triangular matrix.


**trans**–**[in]**[rocblas_operation] indicates whether each matrix A_i is tranposed (conjugated) or not.**diag**–**[in]**[rocblas_diagonal]rocblas_diagonal_unit: The main diagonal of each A_i is assumed to consist of only 1’s and is not referenced.

rocblas_diagonal_non_unit: No assumptions are made of each A_i’s main diagonal.


**n**–**[in]**[rocblas_int] the number of rows and columns of the matrix represented by each A_i.**k**–**[in]**[rocblas_int]if uplo == rocblas_fill_upper, k specifies the number of super-diagonals of each matrix A_i. if uplo == rocblas_fill_lower, k specifies the number of sub-diagonals of each matrix A_i. k must satisfy k > 0 && k < lda.

**A**–**[in]**device array of device pointers storing each banded triangular matrix A_i.if uplo == rocblas_fill_upper: The matrix represented is an upper banded triangular matrix with the main diagonal and k super-diagonals, everything else can be assumed to be 0. The matrix is compacted so that the main diagonal resides on the k'th row, the first super diagonal resides on the RHS of the k-1'th row, etc, with the k'th diagonal on the RHS of the 0'th row. Ex: (rocblas_fill_upper; n = 5; k = 2) 1 6 9 0 0 0 0 9 8 7 0 2 7 8 0 0 6 7 8 9 0 0 3 8 7 ----> 1 2 3 4 5 0 0 0 4 9 0 0 0 0 0 0 0 0 0 5 0 0 0 0 0 if uplo == rocblas_fill_lower: The matrix represnted is a lower banded triangular matrix with the main diagonal and k sub-diagonals, everything else can be assumed to be 0. The matrix is compacted so that the main diagonal resides on the 0'th row, working up to the k'th diagonal residing on the LHS of the k'th row. Ex: (rocblas_fill_lower; n = 5; k = 2) 1 0 0 0 0 1 2 3 4 5 6 2 0 0 0 6 7 8 9 0 9 7 3 0 0 ----> 9 8 7 0 0 0 8 8 4 0 0 0 0 0 0 0 0 7 9 5 0 0 0 0 0

**lda**–**[in]**[rocblas_int] specifies the leading dimension of each A_i. lda must satisfy lda > k.**x**–**[inout]**device array of device pointer storing each vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i.**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `tbmv_batched`

functions support the `_64`

interface. Parameters `n`

and `k`

larger than `int32_t`

max value are not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_stbmv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_stbmv_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPKf11rocblas_int14rocblas_stridePf11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dtbmv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_dtbmv_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPKd11rocblas_int14rocblas_stridePd11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ctbmv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_ctbmv_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPK21rocblas_float_complex11rocblas_int14rocblas_strideP21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ztbmv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)trans,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_ztbmv_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPK22rocblas_double_complex11rocblas_int14rocblas_strideP22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_int) **BLAS Level 2 API**tbmv_strided_batched performs one of the matrix-vector operations:

x_i := A_i*x_i or x_i := A_i**T*x_i or x_i := A_i**H*x_i, where (A_i, x_i) is the i-th instance of the batch. x_i is a vector and A_i is an n by n matrix, for i = 1, ..., batch_count.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: each A_i is an upper banded triangular matrix.

rocblas_fill_lower: each A_i is a lower banded triangular matrix.


**trans**–**[in]**[rocblas_operation] indicates whether each matrix A_i is tranposed (conjugated) or not.**diag**–**[in]**[rocblas_diagonal]rocblas_diagonal_unit: The main diagonal of each A_i is assumed to consist of only 1’s and is not referenced.

rocblas_diagonal_non_unit: No assumptions are made of each A_i’s main diagonal.


**n**–**[in]**[rocblas_int] the number of rows and columns of the matrix represented by each A_i.**k**–**[in]**[rocblas_int]if uplo == rocblas_fill_upper, k specifies the number of super-diagonals of each matrix A_i. if uplo == rocblas_fill_lower, k specifies the number of sub-diagonals of each matrix A_i. k must satisfy k > 0 && k < lda.

**A**–**[in]**device array to the first matrix A_i of the batch. Stores each banded triangular matrix A_i.if uplo == rocblas_fill_upper: The matrix represented is an upper banded triangular matrix with the main diagonal and k super-diagonals, everything else can be assumed to be 0. The matrix is compacted so that the main diagonal resides on the k'th row, the first super diagonal resides on the RHS of the k-1'th row, etc, with the k'th diagonal on the RHS of the 0'th row. Ex: (rocblas_fill_upper; n = 5; k = 2) 1 6 9 0 0 0 0 9 8 7 0 2 7 8 0 0 6 7 8 9 0 0 3 8 7 ----> 1 2 3 4 5 0 0 0 4 9 0 0 0 0 0 0 0 0 0 5 0 0 0 0 0 if uplo == rocblas_fill_lower: The matrix represnted is a lower banded triangular matrix with the main diagonal and k sub-diagonals, everything else can be assumed to be 0. The matrix is compacted so that the main diagonal resides on the 0'th row, working up to the k'th diagonal residing on the LHS of the k'th row. Ex: (rocblas_fill_lower; n = 5; k = 2) 1 0 0 0 0 1 2 3 4 5 6 2 0 0 0 6 7 8 9 0 9 7 3 0 0 ----> 9 8 7 0 0 0 8 8 4 0 0 0 0 0 0 0 0 7 9 5 0 0 0 0 0

**lda**–**[in]**[rocblas_int] specifies the leading dimension of each A_i. lda must satisfy lda > k.**stride_A**–**[in]**[rocblas_stride] stride from the start of one A_i matrix to the next A_(i + 1).**x**–**[inout]**device array to the first vector x_i of the batch.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i.**stride_x**–**[in]**[rocblas_stride] stride from the start of one x_i matrix to the next x_(i + 1).**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `tbmv_strided_batched`

functions support the `_64`

interface. Parameters `n`

and `k`

larger than `int32_t`

max value are not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xtbsv + batched, strided_batched[#](#rocblas-xtbsv-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_stbsv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx)[#](#_CPPv413rocblas_stbsv14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPKf11rocblas_intPf11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dtbsv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx)[#](#_CPPv413rocblas_dtbsv14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPKd11rocblas_intPd11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ctbsv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx)[#](#_CPPv413rocblas_ctbsv14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPK21rocblas_float_complex11rocblas_intP21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ztbsv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx)[#](#_CPPv413rocblas_ztbsv14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPK22rocblas_double_complex11rocblas_intP22rocblas_double_complex11rocblas_int) **BLAS Level 2 API**tbsv solves:

A*x = b or A**T*x = b or A**H*x = b where x and b are vectors and A is a banded triangular matrix.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: A is an upper triangular matrix.

rocblas_fill_lower: A is a lower triangular matrix.


**transA**–**[in]**[rocblas_operation]rocblas_operation_none: Solves A*x = b

rocblas_operation_transpose: Solves A**T*x = b

rocblas_operation_conjugate_transpose: Solves A**H*x = b


**diag**–**[in]**[rocblas_diagonal]rocblas_diagonal_unit: A is assumed to be unit triangular (i.e. the diagonal elements of A are not used in computations).

rocblas_diagonal_non_unit: A is not assumed to be unit triangular.


**n**–**[in]**[rocblas_int] n specifies the number of rows of b. n >= 0.**k**–**[in]**[rocblas_int]if(uplo == rocblas_fill_upper) k specifies the number of super-diagonals of A. if(uplo == rocblas_fill_lower) k specifies the number of sub-diagonals of A. k >= 0.

**A**–**[in]**device pointer storing the matrix A in banded format.**lda**–**[in]**[rocblas_int] specifies the leading dimension of A. lda >= (k + 1).**x**–**[inout]**device pointer storing input vector b. Overwritten by the output vector x.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of x.



The `tbsv`

functions support the `_64`

interface. Parameters `n`

and `k`

larger than `int32_t`

max value are not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_stbsv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const float *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, float *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_stbsv_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intA_PCKf11rocblas_intA_PCf11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dtbsv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const double *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, double *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_dtbsv_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intA_PCKd11rocblas_intA_PCd11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ctbsv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_ctbsv_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intA_PCK21rocblas_float_complex11rocblas_intA_PC21rocblas_float_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ztbsv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_ztbsv_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intA_PCK22rocblas_double_complex11rocblas_intA_PC22rocblas_double_complex11rocblas_int11rocblas_int) **BLAS Level 2 API**tbsv_batched solves:

The input vectors b_i are overwritten by the output vectors x_i.A_i*x_i = b_i or A_i**T*x_i = b_i or A_i**H*x_i = b_i where x_i and b_i are vectors and A_i is a banded triangular matrix, for i = [1, batch_count].

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: A_i is an upper triangular matrix.

rocblas_fill_lower: A_i is a lower triangular matrix.


**transA**–**[in]**[rocblas_operation]rocblas_operation_none: Solves A_i*x_i = b_i

rocblas_operation_transpose: Solves A_i**T*x_i = b_i

rocblas_operation_conjugate_transpose: Solves A_i**H*x_i = b_i


**diag**–**[in]**[rocblas_diagonal]rocblas_diagonal_unit: each A_i is assumed to be unit triangular (i.e. the diagonal elements of each A_i are not used in computations).

rocblas_diagonal_non_unit: each A_i is not assumed to be unit triangular.


**n**–**[in]**[rocblas_int] n specifies the number of rows of each b_i. n >= 0.**k**–**[in]**[rocblas_int]if(uplo == rocblas_fill_upper) k specifies the number of super-diagonals of each A_i. if(uplo == rocblas_fill_lower) k specifies the number of sub-diagonals of each A_i. k >= 0.

**A**–**[in]**device vector of device pointers storing each matrix A_i in banded format.**lda**–**[in]**[rocblas_int] specifies the leading dimension of each A_i. lda >= (k + 1).**x**–**[inout]**device vector of device pointers storing each input vector b_i. Overwritten by each output vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i.**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `tbsv_batched`

functions support the `_64`

interface. Parameters `n`

and `k`

larger than `int32_t`

max value are not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_stbsv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_stbsv_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPKf11rocblas_int14rocblas_stridePf11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dtbsv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_dtbsv_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPKd11rocblas_int14rocblas_stridePd11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ctbsv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_ctbsv_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPK21rocblas_float_complex11rocblas_int14rocblas_strideP21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ztbsv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_ztbsv_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPK22rocblas_double_complex11rocblas_int14rocblas_strideP22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_int) **BLAS Level 2 API**tbsv_strided_batched solves:

The input vectors b_i are overwritten by the output vectors x_i.A_i*x_i = b_i or A_i**T*x_i = b_i or A_i**H*x_i = b_i where x_i and b_i are vectors and A_i is a banded triangular matrix, for i = [1, batch_count].

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: A_i is an upper triangular matrix.

rocblas_fill_lower: A_i is a lower triangular matrix.


**transA**–**[in]**[rocblas_operation]rocblas_operation_none: Solves A_i*x_i = b_i

rocblas_operation_transpose: Solves A_i**T*x_i = b_i

rocblas_operation_conjugate_transpose: Solves A_i**H*x_i = b_i


**diag**–**[in]**[rocblas_diagonal]rocblas_diagonal_unit: each A_i is assumed to be unit triangular (i.e. the diagonal elements of each A_i are not used in computations).

rocblas_diagonal_non_unit: each A_i is not assumed to be unit triangular.


**n**–**[in]**[rocblas_int] n specifies the number of rows of each b_i. n >= 0.**k**–**[in]**[rocblas_int]if(uplo == rocblas_fill_upper) k specifies the number of super-diagonals of each A_i. if(uplo == rocblas_fill_lower) k specifies the number of sub-diagonals of each A_i. k >= 0.

**A**–**[in]**device pointer pointing to the first banded matrix A_1.**lda**–**[in]**[rocblas_int] specifies the leading dimension of each A_i. lda >= (k + 1).**stride_A**–**[in]**[rocblas_stride] specifies the distance between the start of one matrix (A_i) and the next (A_i+1).**x**–**[inout]**device pointer pointing to the first input vector b_1. Overwritten by output vectors x.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i.**stride_x**–**[in]**[rocblas_stride] specifies the distance between the start of one vector (x_i) and the next (x_i+1).**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `tbsv_strided_batched`

functions support the `_64`

interface. Parameters `n`

and `k`

larger than `int32_t`

max value are not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xtpmv + batched, strided_batched[#](#rocblas-xtpmv-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_stpmv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *A, float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx)[#](#_CPPv413rocblas_stpmv14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPKfPf11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dtpmv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *A, double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx)[#](#_CPPv413rocblas_dtpmv14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPKdPd11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ctpmv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx)[#](#_CPPv413rocblas_ctpmv14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPK21rocblas_float_complexP21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ztpmv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx)[#](#_CPPv413rocblas_ztpmv14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPK22rocblas_double_complexP22rocblas_double_complex11rocblas_int) **BLAS Level 2 API**tpmv performs one of the matrix-vector operations:

x = A*x or x = A**T*x or x = A**H*x where x is an n element vector and A is an n by n unit, or non-unit, upper or lower triangular matrix, supplied in the pack form. The vector x is overwritten.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: A is an upper triangular matrix.

rocblas_fill_lower: A is a lower triangular matrix.


**transA**–**[in]**[rocblas_operation]rocblas_operation_none: op(A) = A.

rocblas_operation_transpose: op(A) = A^T

rocblas_operation_conjugate_transpose: op(A) = A^H


**diag**–**[in]**[rocblas_diagonal]rocblas_diagonal_unit: A is assumed to be unit triangular.

rocblas_diagonal_non_unit: A is not assumed to be unit triangular.


**n**–**[in]**[rocblas_int] n specifies the number of rows of A. n >= 0.**A**–**[in]**device pointer storing matrix A, of dimension at leat ( n * ( n + 1 ) / 2 ).Before entry with uplo = rocblas_fill_upper, the array A must contain the upper triangular matrix packed sequentially, column by column, so that A[0] contains a_{0,0}, A[1] and A[2] contain a_{0,1} and a_{1, 1}, respectively, and so on.

Before entry with uplo = rocblas_fill_lower, the array A must contain the lower triangular matrix packed sequentially, column by column, so that A[0] contains a_{0,0}, A[1] and A[2] contain a_{1,0} and a_{2,0}, respectively, and so on.

Note that when DIAG = rocblas_diagonal_unit, the diagonal elements of A are not referenced, but are assumed to be unity.


**x**–**[inout]**device pointer storing vector x. On exit, x is overwritten with the transformed vector x.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of x. incx must not be zero.



The `tpmv`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_stpmv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *const *A, float *const *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_stpmv_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPPCKfPPCf11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dtpmv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *const *A, double *const *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_dtpmv_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPPCKdPPCd11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ctpmv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const *A,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_ctpmv_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPPCK21rocblas_float_complexPPC21rocblas_float_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ztpmv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const *A,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_ztpmv_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPPCK22rocblas_double_complexPPC22rocblas_double_complex11rocblas_int11rocblas_int) **BLAS Level 2 API**tpmv_batched performs one of the matrix-vector operations:

x_i = A_i*x_i or x_i = A_i**T*x_i or x_i = A_i**H*x_i, 0 < i < batch_count where x_i is an n element vector and A_i is an n by n (unit, or non-unit, upper or lower triangular matrix) The vectors x_i are overwritten.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: A_i is an upper triangular matrix.

rocblas_fill_lower: A_i is a lower triangular matrix.


**transA**–**[in]**[rocblas_operation]rocblas_operation_none: op(A) = A.

rocblas_operation_transpose: op(A) = A^T

rocblas_operation_conjugate_transpose: op(A) = A^H


**diag**–**[in]**[rocblas_diagonal]rocblas_diagonal_unit: A_i is assumed to be unit triangular.

rocblas_diagonal_non_unit: A_i is not assumed to be unit triangular.


**n**–**[in]**[rocblas_int] n specifies the number of rows of matrices A_i. n >= 0.**A**–**[in]**device pointer to an array of device pointers to the A_i matrices, of dimension ( lda, n ). If uplo == rocblas_fill_upper, the upper triangular part of the leading n-by-n array contains the matrix A_i, otherwise the lower triangular part of the leading n-by-n array contains the matrix A_i.**x**–**[inout]**device pointer to an array of device pointers to the x_i vectors. On exit, each x_i is overwritten with the transformed vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of vectors x_i.**batch_count**–**[in]**[rocblas_int] The number of batched matrices/vectors.



The `tpmv_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_stpmv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *A,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_stpmv_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPKf14rocblas_stridePf11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dtpmv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *A,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_dtpmv_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPKd14rocblas_stridePd11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ctpmv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_ctpmv_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPK21rocblas_float_complex14rocblas_strideP21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ztpmv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_ztpmv_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPK22rocblas_double_complex14rocblas_strideP22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_int) **BLAS Level 2 API**tpmv_strided_batched performs one of the matrix-vector operations:

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: A_i is an upper triangular matrix.

rocblas_fill_lower: A_i is a lower triangular matrix.


**transA**–**[in]**[rocblas_operation]rocblas_operation_none: op(A) = A.

rocblas_operation_transpose: op(A) = A^T

rocblas_operation_conjugate_transpose: op(A) = A^H


**diag**–**[in]**[rocblas_diagonal]rocblas_diagonal_unit: A_i is assumed to be unit triangular.

rocblas_diagonal_non_unit: A_i is not assumed to be unit triangular.


**n**–**[in]**[rocblas_int] n specifies the number of rows of matrices A_i. n >= 0.**A**–**[in]**device pointer to the matrix A_1 of the batch, of dimension ( lda, n ). If uplo == rocblas_fill_upper, the upper triangular part of the leading n-by-n array contains the matrix A_i, otherwise the lower triangular part of the leading n-by-n array contains the matrix A_i.**stride_A**–**[in]**[rocblas_stride] stride from the start of one A_i matrix to the next A_{i + 1}.**x**–**[inout]**device pointer to the vector x_1 of the batch. On exit, each x_i is overwritten with the transformed vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of one vector x.**stride_x**–**[in]**[rocblas_stride] stride from the start of one x_i vector to the next x_{i + 1}.**batch_count**–**[in]**[rocblas_int] The number of batched matrices/vectors.



The `tpmv_strided_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xtpsv + batched, strided_batched[#](#rocblas-xtpsv-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_stpsv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *AP, float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx)[#](#_CPPv413rocblas_stpsv14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPKfPf11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dtpsv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *AP, double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx)[#](#_CPPv413rocblas_dtpsv14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPKdPd11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ctpsv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*AP,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx)[#](#_CPPv413rocblas_ctpsv14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPK21rocblas_float_complexP21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ztpsv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*AP,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx)[#](#_CPPv413rocblas_ztpsv14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPK22rocblas_double_complexP22rocblas_double_complex11rocblas_int) **BLAS Level 2 API**tpsv solves:

The input vector b is overwritten by the output vector x.A*x = b or A**T*x = b or A**H*x = b where x and b are vectors and A is a triangular matrix stored in the packed format.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: A is an upper triangular matrix.

rocblas_fill_lower: A is a lower triangular matrix.


**transA**–**[in]**[rocblas_operation]rocblas_operation_none: Solves A*x = b

rocblas_operation_transpose: Solves A**T*x = b

rocblas_operation_conjugate_transpose: Solves A**H*x = b


**diag**–**[in]**[rocblas_diagonal]rocblas_diagonal_unit: A is assumed to be unit triangular (i.e. the diagonal elements of A are not used in computations).

rocblas_diagonal_non_unit: A is not assumed to be unit triangular.


**n**–**[in]**[rocblas_int] n specifies the number of rows of b. n >= 0.**AP**–**[in]**device pointer storing the packed version of matrix A, of dimension >= (n * (n + 1) / 2).**x**–**[inout]**device pointer storing vector b on input, overwritten by x on output.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of x.



The `tpsv`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_stpsv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *const AP[], float *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_stpsv_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intA_PCKfA_PCf11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dtpsv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *const AP[], double *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_dtpsv_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intA_PCKdA_PCd11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ctpsv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const AP[],[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_ctpsv_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intA_PCK21rocblas_float_complexA_PC21rocblas_float_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ztpsv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const AP[],[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_ztpsv_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intA_PCK22rocblas_double_complexA_PC22rocblas_double_complex11rocblas_int11rocblas_int) **BLAS Level 2 API**tpsv_batched solves:

The input vectors b_i are overwritten by the output vectors x_i.A_i*x_i = b_i or A_i**T*x_i = b_i or A_i**H*x_i = b_i where x_i and b_i are vectors and A_i is a triangular matrix stored in the packed format, for i in [1, batch_count].

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: each A_i is an upper triangular matrix.

rocblas_fill_lower: each A_i is a lower triangular matrix.


**transA**–**[in]**[rocblas_operation]rocblas_operation_none: Solves A*x = b

rocblas_operation_transpose: Solves A**T*x = b

rocblas_operation_conjugate_transpose: Solves A**H*x = b


**diag**–**[in]**[rocblas_diagonal]rocblas_diagonal_unit: Each A_i is assumed to be unit triangular (i.e. the diagonal elements of each A_i are not used in computations).

rocblas_diagonal_non_unit: each A_i is not assumed to be unit triangular.


**n**–**[in]**[rocblas_int] n specifies the number of rows of each b_i. n >= 0.**AP**–**[in]**device array of device pointers storing the packed versions of each matrix A_i, of dimension >= (n * (n + 1) / 2).**x**–**[inout]**device array of device pointers storing each input vector b_i, overwritten by x_i on output.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i.**batch_count**–**[in]**[rocblas_int] specifies the number of instances in the batch.



The `tpsv_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_stpsv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *AP,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_stpsv_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPKf14rocblas_stridePf11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dtpsv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *AP,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_dtpsv_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPKd14rocblas_stridePd11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ctpsv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*AP,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_ctpsv_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPK21rocblas_float_complex14rocblas_strideP21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ztpsv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*AP,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_ztpsv_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPK22rocblas_double_complex14rocblas_strideP22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_int) **BLAS Level 2 API**tpsv_strided_batched solves:

The input vectors b_i are overwritten by the output vectors x_i.A_i*x_i = b_i or A_i**T*x_i = b_i or A_i**H*x_i = b_i where x_i and b_i are vectors and A_i is a triangular matrix stored in the packed format, for i in [1, batch_count].

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: each A_i is an upper triangular matrix.

rocblas_fill_lower: each A_i is a lower triangular matrix.


**transA**–**[in]**[rocblas_operation]rocblas_operation_none: Solves A*x = b

rocblas_operation_transpose: Solves A**T*x = b

rocblas_operation_conjugate_transpose: Solves A**H*x = b


**diag**–**[in]**[rocblas_diagonal]rocblas_diagonal_unit: each A_i is assumed to be unit triangular (i.e. the diagonal elements of each A_i are not used in computations).

rocblas_diagonal_non_unit: each A_i is not assumed to be unit triangular.


**n**–**[in]**[rocblas_int] n specifies the number of rows of each b_i. n >= 0.**AP**–**[in]**device pointer pointing to the first packed matrix A_1, of dimension >= (n * (n + 1) / 2).**stride_A**–**[in]**[rocblas_stride] stride from the beginning of one packed matrix (AP_i) and the next (AP_i+1).**x**–**[inout]**device pointer pointing to the first input vector b_1. Overwritten by each x_i on output.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i.**stride_x**–**[in]**[rocblas_stride] stride from the beginning of one vector (x_i) and the next (x_i+1).**batch_count**–**[in]**[rocblas_int] specifies the number of instances in the batch.



The `tpsv_strided_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xtrmv + batched, strided_batched[#](#rocblas-xtrmv-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_strmv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx)[#](#_CPPv413rocblas_strmv14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPKf11rocblas_intPf11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dtrmv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx)[#](#_CPPv413rocblas_dtrmv14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPKd11rocblas_intPd11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ctrmv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx)[#](#_CPPv413rocblas_ctrmv14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPK21rocblas_float_complex11rocblas_intP21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ztrmv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx)[#](#_CPPv413rocblas_ztrmv14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPK22rocblas_double_complex11rocblas_intP22rocblas_double_complex11rocblas_int) **BLAS Level 2 API**trmv performs one of the matrix-vector operations:

x = A*x or x = A**T*x or x = A**H*x where x is an n element vector and A is an n by n unit, or non-unit, upper or lower triangular matrix. The vector x is overwritten.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: A is an upper triangular matrix.

rocblas_fill_lower: A is a lower triangular matrix.


**transA**–**[in]**[rocblas_operation]rocblas_operation_none: op(A) = A.

rocblas_operation_transpose: op(A) = A^T

rocblas_operation_conjugate_transpose: op(A) = A^H


**diag**–**[in]**[rocblas_diagonal]rocblas_diagonal_unit: A is assumed to be unit triangular.

rocblas_diagonal_non_unit: A is not assumed to be unit triangular.


**n**–**[in]**[rocblas_int] n specifies the number of rows of A. n >= 0.**A**–**[in]**device pointer storing matrix A, of dimension ( lda, n ). If uplo == rocblas_fill_upper, the upper triangular part of the leading n-by-n array contains the matrix A, otherwise the lower triangular part of the leading n-by-n array contains the matrix A.**lda**–**[in]**[rocblas_int] specifies the leading dimension of A. lda must be at least max( 1, n ).**x**–**[inout]**device pointer storing vector x. On exit, x is overwritten with the transformed vector x.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of x.



The `trmv`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_strmv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *const *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, float *const *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_strmv_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPPCKf11rocblas_intPPCf11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dtrmv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *const *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, double *const *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_dtrmv_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPPCKd11rocblas_intPPCd11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ctrmv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_ctrmv_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPPCK21rocblas_float_complex11rocblas_intPPC21rocblas_float_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ztrmv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_ztrmv_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPPCK22rocblas_double_complex11rocblas_intPPC22rocblas_double_complex11rocblas_int11rocblas_int) **BLAS Level 2 API**trmv_batched performs one of the matrix-vector operations:

x_i = A_i*x_i or x_i = A_i**T*x_i or x_i = A_i**H*x_i, 0 < i < batch_count where x_i is an n element vector and A_i is an n by n (unit, or non-unit, upper or lower triangular matrix) The vectors x_i are overwritten.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: A_i is an upper triangular matrix.

rocblas_fill_lower: A_i is a lower triangular matrix.


**transA**–**[in]**[rocblas_operation]rocblas_operation_none: op(A) = A.

rocblas_operation_transpose: op(A) = A^T

rocblas_operation_conjugate_transpose: op(A) = A^H


**diag**–**[in]**[rocblas_diagonal]rocblas_diagonal_unit: A_i is assumed to be unit triangular.

rocblas_diagonal_non_unit: A_i is not assumed to be unit triangular.


**n**–**[in]**[rocblas_int] n specifies the number of rows of matrices A_i. n >= 0.**A**–**[in]**device pointer to an array of device pointers to the A_i matrices, of dimension ( lda, n ). If uplo == rocblas_fill_upper, the upper triangular part of the leading n-by-n array contains the matrix A_i, otherwise the lower triangular part of the leading n-by-n array contains the matrix A_i.**lda**–**[in]**[rocblas_int] specifies the leading dimension of A_i. lda must be at least max( 1, n ).**x**–**[inout]**device pointer to an array of device pointers to the x_i vectors. On exit, each x_i is overwritten with the transformed vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of vectors x_i.**batch_count**–**[in]**[rocblas_int] The number of batched matrices/vectors.



The `trmv_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_strmv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_strmv_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPKf11rocblas_int14rocblas_stridePf11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dtrmv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_dtrmv_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPKd11rocblas_int14rocblas_stridePd11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ctrmv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_ctrmv_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPK21rocblas_float_complex11rocblas_int14rocblas_strideP21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ztrmv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_ztrmv_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPK22rocblas_double_complex11rocblas_int14rocblas_strideP22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_int) **BLAS Level 2 API**trmv_strided_batched performs one of the matrix-vector operations:

The vectors x_i are overwritten.- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: A_i is an upper triangular matrix.

rocblas_fill_lower: A_i is a lower triangular matrix.


**transA**–**[in]**[rocblas_operation]rocblas_operation_none: op(A) = A.

rocblas_operation_transpose: op(A) = A^T

rocblas_operation_conjugate_transpose: op(A) = A^H


**diag**–**[in]**[rocblas_diagonal]rocblas_diagonal_unit: A_i is assumed to be unit triangular.

rocblas_diagonal_non_unit: A_i is not assumed to be unit triangular.


**n**–**[in]**[rocblas_int] n specifies the number of rows of matrices A_i. n >= 0.**A**–**[in]**device pointer to the matrix A_1 of the batch, of dimension ( lda, n ). If uplo == rocblas_fill_upper, the upper triangular part of the leading n-by-n array contains the matrix A_i, otherwise the lower triangular part of the leading n-by-n array contains the matrix A_i.**lda**–**[in]**[rocblas_int] specifies the leading dimension of A_i. lda must be at least max( 1, n ).**stride_A**–**[in]**[rocblas_stride] stride from the start of one A_i matrix to the next A_{i + 1}.**x**–**[inout]**device pointer to the vector x_1 of the batch. On exit, each x_i is overwritten with the transformed vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of one vector x.**stride_x**–**[in]**[rocblas_stride] stride from the start of one x_i vector to the next x_{i + 1}.**batch_count**–**[in]**[rocblas_int] The number of batched matrices/vectors.



The `trmv_strided_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xtrsv + batched, strided_batched[#](#rocblas-xtrsv-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_strsv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx)[#](#_CPPv413rocblas_strsv14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPKf11rocblas_intPf11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dtrsv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx)[#](#_CPPv413rocblas_dtrsv14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPKd11rocblas_intPd11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ctrsv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx)[#](#_CPPv413rocblas_ctrsv14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPK21rocblas_float_complex11rocblas_intP21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ztrsv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx)[#](#_CPPv413rocblas_ztrsv14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPK22rocblas_double_complex11rocblas_intP22rocblas_double_complex11rocblas_int) **BLAS Level 2 API**trsv solves:

Although not widespread, some gemm kernels used by trsv may use atomic operations. See Atomic Operations in the API Reference Guide for more information.A*x = b or A**T*x = b or A**H*x = b, where x and b are vectors and A is a triangular matrix. The vector x is overwritten on b.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: A is an upper triangular matrix.

rocblas_fill_lower: A is a lower triangular matrix.


**transA**–**[in]**[rocblas_operation]rocblas_operation_none: op(A) = A.

rocblas_operation_transpose: op(A) = A^T

rocblas_operation_conjugate_transpose: op(A) = A^H


**diag**–**[in]**[rocblas_diagonal]rocblas_diagonal_unit: A is assumed to be unit triangular.

rocblas_diagonal_non_unit: A is not assumed to be unit triangular.


**n**–**[in]**[rocblas_int] n specifies the number of rows of b. n >= 0.**A**–**[in]**device pointer storing matrix A, of dimension ( lda, n ). If uplo == rocblas_fill_upper, the upper triangular part of the leading n-by-n array contains the matrix A, otherwise the lower triangular part of the leading n-by-n array contains the matrix A.**lda**–**[in]**[rocblas_int] specifies the leading dimension of A. lda must be at least max( 1, n ).**x**–**[inout]**device pointer storing vector x. On exit, x is overwritten with the transformed vector x.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of x.



The `trsv`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_strsv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, float *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_strsv_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intA_PCKf11rocblas_intA_PCf11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dtrsv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, double *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_dtrsv_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intA_PCKd11rocblas_intA_PCd11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ctrsv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_ctrsv_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intA_PCK21rocblas_float_complex11rocblas_intA_PC21rocblas_float_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ztrsv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_ztrsv_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intA_PCK22rocblas_double_complex11rocblas_intA_PC22rocblas_double_complex11rocblas_int11rocblas_int) **BLAS Level 2 API**trsv_batched solves:

The vector x is overwritten on b.A_i*x_i = b_i or A_i**T*x_i = b_i or A_i**H*x_i = b_i, where (A_i, x_i, b_i) is the i-th instance of the batch. x_i and b_i are vectors and A_i is an n by n triangular matrix.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: A is an upper triangular matrix.

rocblas_fill_lower: A is a lower triangular matrix.


**transA**–**[in]**[rocblas_operation]rocblas_operation_none: op(A) = A.

rocblas_operation_transpose: op(A) = A^T

rocblas_operation_conjugate_transpose: op(A) = A^H


**diag**–**[in]**[rocblas_diagonal]rocblas_diagonal_unit: A is assumed to be unit triangular.

rocblas_diagonal_non_unit: A is not assumed to be unit triangular.


**n**–**[in]**[rocblas_int] n specifies the number of rows of b. n >= 0.**A**–**[in]**device pointer to an array of device pointers to the A_i matrices, of dimension ( lda, n ). If uplo == rocblas_fill_upper, the upper triangular part of the leading n-by-n array contains the matrix A_i, otherwise the lower triangular part of the leading n-by-n array contains the matrix A_i.**lda**–**[in]**[rocblas_int] specifies the leading dimension of A_i. lda must be at least max( 1, n ).**x**–**[inout]**device pointer to an array of device pointers to the x_i vectors. On exit, each x_i is overwritten with the transformed vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of x.**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `trsv_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_strsv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_strsv_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPKf11rocblas_int14rocblas_stridePf11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dtrsv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_dtrsv_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPKd11rocblas_int14rocblas_stridePd11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ctrsv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_ctrsv_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPK21rocblas_float_complex11rocblas_int14rocblas_strideP21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ztrsv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_ztrsv_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_intPK22rocblas_double_complex11rocblas_int14rocblas_strideP22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_int) **BLAS Level 2 API**trsv_strided_batched solves:

The vector x is overwritten on b.A_i*x_i = b_i or A_i**T*x_i = b_i or A_i**H*x_i = b_i, where (A_i, x_i, b_i) is the i-th instance of the batch. x_i and b_i are vectors and A_i is an n by n triangular matrix, for i = 1, ..., batch_count.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: A is an upper triangular matrix.

rocblas_fill_lower: A is a lower triangular matrix.


**transA**–**[in]**[rocblas_operation]rocblas_operation_none: op(A) = A.

rocblas_operation_transpose: op(A) = A^T

rocblas_operation_conjugate_transpose: op(A) = A^H


**diag**–**[in]**[rocblas_diagonal]rocblas_diagonal_unit: A is assumed to be unit triangular.

rocblas_diagonal_non_unit: A is not assumed to be unit triangular.


**n**–**[in]**[rocblas_int] n specifies the number of rows of each b_i. n >= 0.**A**–**[in]**device pointer to the matrix A_1 of the batch, of dimension ( lda, n ). If uplo == rocblas_fill_upper, the upper triangular part of the leading n-by-n array contains the matrix A_i, otherwise the lower triangular part of the leading n-by-n array contains the matrix A_i.**stride_A**–**[in]**[rocblas_stride] stride from the start of one A_i matrix to the next A_(i + 1).**lda**–**[in]**[rocblas_int] specifies the leading dimension of A_i. lda must be at least max( 1, n ).**x**–**[inout]**device pointer to the vector x_1 of the batch. On exit, each x_i is overwritten with the transformed vector x_i.**stride_x**–**[in]**[rocblas_stride] stride from the start of one x_i vector to the next x_(i + 1)**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i.**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `trsv_strided_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xhemv + batched, strided_batched[#](#rocblas-xhemv-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_chemv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy)[#](#_CPPv413rocblas_chemv14rocblas_handle12rocblas_fill11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_intPK21rocblas_float_complex11rocblas_intPK21rocblas_float_complexP21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zhemv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy)[#](#_CPPv413rocblas_zhemv14rocblas_handle12rocblas_fill11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_intPK22rocblas_double_complex11rocblas_intPK22rocblas_double_complexP22rocblas_double_complex11rocblas_int) **BLAS Level 2 API**hemv performs one of the matrix-vector operations:

y := alpha*A*x + beta*y where alpha and beta are scalars, x and y are n element vectors and A is an n by n Hermitian matrix.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: the upper triangular part of the Hermitian matrix A is supplied.

rocblas_fill_lower: the lower triangular part of the Hermitian matrix A is supplied.


**n**–**[in]**[rocblas_int] the order of the matrix A.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**A**–**[in]**device pointer storing matrix A. Of dimension (lda, n).if uplo == rocblas_fill_upper: The upper triangular part of A must contain the upper triangular part of a Hermitian matrix. The lower triangular part of A will not be referenced. if uplo == rocblas_fill_lower: The lower triangular part of A must contain the lower triangular part of a Hermitian matrix. The upper triangular part of A will not be referenced. As a Hermitian matrix, the imaginary part of the main diagonal of A will not be referenced and is assumed to be == 0.

**lda**–**[in]**[rocblas_int] specifies the leading dimension of A. must be >= max(1, n).**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of x.**beta**–**[in]**device pointer or host pointer to scalar beta.**y**–**[inout]**device pointer storing vector y.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of y.



The `hemv`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_chemv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_chemv_batched14rocblas_handle12rocblas_fill11rocblas_intPK21rocblas_float_complexA_PCK21rocblas_float_complex11rocblas_intA_PCK21rocblas_float_complex11rocblas_intPK21rocblas_float_complexA_PC21rocblas_float_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zhemv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_zhemv_batched14rocblas_handle12rocblas_fill11rocblas_intPK22rocblas_double_complexA_PCK22rocblas_double_complex11rocblas_intA_PCK22rocblas_double_complex11rocblas_intPK22rocblas_double_complexA_PC22rocblas_double_complex11rocblas_int11rocblas_int) **BLAS Level 2 API**hemv_batched performs one of the matrix-vector operations:

y_i := alpha*A_i*x_i + beta*y_i where alpha and beta are scalars, x_i and y_i are n element vectors and A_i is an n by n Hermitian matrix, for each batch in i = [1, batch_count].

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: the upper triangular part of the Hermitian matrix A is supplied.

rocblas_fill_lower: the lower triangular part of the Hermitian matrix A is supplied.


**n**–**[in]**[rocblas_int] the order of each matrix A_i.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**A**–**[in]**device array of device pointers storing each matrix A_i of dimension (lda, n).if uplo == rocblas_fill_upper: The upper triangular part of each A_i must contain the upper triangular part of a Hermitian matrix. The lower triangular part of each A_i will not be referenced. if uplo == rocblas_fill_lower: The lower triangular part of each A_i must contain the lower triangular part of a Hermitian matrix. The upper triangular part of each A_i will not be referenced. As a Hermitian matrix, the imaginary part of the main diagonal of each A_i will not be referenced and is assumed to be == 0.

**lda**–**[in]**[rocblas_int] specifies the leading dimension of each A_i. must be >= max(1, n).**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i.**beta**–**[in]**device pointer or host pointer to scalar beta.**y**–**[inout]**device array of device pointers storing each vector y_i.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of y.**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `hemv_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_chemv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_chemv_strided_batched14rocblas_handle12rocblas_fill11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_int14rocblas_stridePK21rocblas_float_complex11rocblas_int14rocblas_stridePK21rocblas_float_complexP21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zhemv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_zhemv_strided_batched14rocblas_handle12rocblas_fill11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_int14rocblas_stridePK22rocblas_double_complex11rocblas_int14rocblas_stridePK22rocblas_double_complexP22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_int) **BLAS Level 2 API**hemv_strided_batched performs one of the matrix-vector operations:

y_i := alpha*A_i*x_i + beta*y_i where alpha and beta are scalars, x_i and y_i are n element vectors and A_i is an n by n Hermitian matrix, for each batch in i = [1, batch_count].

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: the upper triangular part of the Hermitian matrix A is supplied.

rocblas_fill_lower: the lower triangular part of the Hermitian matrix A is supplied.


**n**–**[in]**[rocblas_int] the order of each matrix A_i.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**A**–**[in]**device array of device pointers storing each matrix A_i of dimension (lda, n).if uplo == rocblas_fill_upper: The upper triangular part of each A_i must contain the upper triangular part of a Hermitian matrix. The lower triangular part of each A_i will not be referenced. if uplo == rocblas_fill_lower: The lower triangular part of each A_i must contain the lower triangular part of a Hermitian matrix. The upper triangular part of each A_i will not be referenced. As a Hermitian matrix, the imaginary part of the main diagonal of each A_i will not be referenced and is assumed to be == 0.

**lda**–**[in]**[rocblas_int] specifies the leading dimension of each A_i. must be >= max(1, n).**stride_A**–**[in]**[rocblas_stride] stride from the start of one (A_i) to the next (A_i+1).**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i.**stride_x**–**[in]**[rocblas_stride] stride from the start of one vector (x_i) and the next one (x_i+1).**beta**–**[in]**device pointer or host pointer to scalar beta.**y**–**[inout]**device array of device pointers storing each vector y_i.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of y.**stride_y**–**[in]**[rocblas_stride] stride from the start of one vector (y_i) and the next one (y_i+1).**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `hemv_strided_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xhbmv + batched, strided_batched[#](#rocblas-xhbmv-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_chbmv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy)[#](#_CPPv413rocblas_chbmv14rocblas_handle12rocblas_fill11rocblas_int11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_intPK21rocblas_float_complex11rocblas_intPK21rocblas_float_complexP21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zhbmv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy)[#](#_CPPv413rocblas_zhbmv14rocblas_handle12rocblas_fill11rocblas_int11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_intPK22rocblas_double_complex11rocblas_intPK22rocblas_double_complexP22rocblas_double_complex11rocblas_int) **BLAS Level 2 API**hbmv performs the matrix-vector operations:

y := alpha*A*x + beta*y where alpha and beta are scalars, x and y are n element vectors and A is an n by n Hermitian band matrix, with k super-diagonals.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: The upper triangular part of A is being supplied.

rocblas_fill_lower: The lower triangular part of A is being supplied.


**n**–**[in]**[rocblas_int] the order of the matrix A.**k**–**[in]**[rocblas_int] the number of super-diagonals of the matrix A. Must be >= 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**A**–**[in]**device pointer storing matrix A. Of dimension (lda, n).if uplo == rocblas_fill_upper: The leading (k + 1) by n part of A must contain the upper triangular band part of the Hermitian matrix, with the leading diagonal in row (k + 1), the first super-diagonal on the RHS of row k, etc. The top left k by x triangle of A will not be referenced. Ex (upper, lda = n = 4, k = 1): A Represented matrix (0,0) (5,9) (6,8) (7,7) (1, 0) (5, 9) (0, 0) (0, 0) (1,0) (2,0) (3,0) (4,0) (5,-9) (2, 0) (6, 8) (0, 0) (0,0) (0,0) (0,0) (0,0) (0, 0) (6,-8) (3, 0) (7, 7) (0,0) (0,0) (0,0) (0,0) (0, 0) (0, 0) (7,-7) (4, 0) if uplo == rocblas_fill_lower: The leading (k + 1) by n part of A must contain the lower triangular band part of the Hermitian matrix, with the leading diagonal in row (1), the first sub-diagonal on the LHS of row 2, etc. The bottom right k by k triangle of A will not be referenced. Ex (lower, lda = 2, n = 4, k = 1): A Represented matrix (1,0) (2,0) (3,0) (4,0) (1, 0) (5,-9) (0, 0) (0, 0) (5,9) (6,8) (7,7) (0,0) (5, 9) (2, 0) (6,-8) (0, 0) (0, 0) (6, 8) (3, 0) (7,-7) (0, 0) (0, 0) (7, 7) (4, 0) As a Hermitian matrix, the imaginary part of the main diagonal of A will not be referenced and is assumed to be == 0.

**lda**–**[in]**[rocblas_int] specifies the leading dimension of A. must be >= k + 1.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of x.**beta**–**[in]**device pointer or host pointer to scalar beta.**y**–**[inout]**device pointer storing vector y.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of y.



The `hbmv`

functions support the `_64`

interface. Parameters `n`

and `k`

larger than `int32_t`

max value are not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_chbmv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_chbmv_batched14rocblas_handle12rocblas_fill11rocblas_int11rocblas_intPK21rocblas_float_complexA_PCK21rocblas_float_complex11rocblas_intA_PCK21rocblas_float_complex11rocblas_intPK21rocblas_float_complexA_PC21rocblas_float_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zhbmv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_zhbmv_batched14rocblas_handle12rocblas_fill11rocblas_int11rocblas_intPK22rocblas_double_complexA_PCK22rocblas_double_complex11rocblas_intA_PCK22rocblas_double_complex11rocblas_intPK22rocblas_double_complexA_PC22rocblas_double_complex11rocblas_int11rocblas_int) **BLAS Level 2 API**hbmv_batched performs one of the matrix-vector operations:

y_i := alpha*A_i*x_i + beta*y_i where alpha and beta are scalars, x_i and y_i are n element vectors and A_i is an n by n Hermitian band matrix with k super-diagonals, for each batch in i = [1, batch_count].

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: The upper triangular part of each A_i is being supplied.

rocblas_fill_lower: The lower triangular part of each A_i is being supplied.


**n**–**[in]**[rocblas_int] the order of each matrix A_i.**k**–**[in]**[rocblas_int] the number of super-diagonals of each matrix A_i. Must be >= 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**A**–**[in]**device array of device pointers storing each matrix_i A of dimension (lda, n).if uplo == rocblas_fill_upper: The leading (k + 1) by n part of each A_i must contain the upper triangular band part of the Hermitian matrix, with the leading diagonal in row (k + 1), the first super-diagonal on the RHS of row k, etc. The top left k by x triangle of each A_i will not be referenced. Ex (upper, lda = n = 4, k = 1): A Represented matrix (0,0) (5,9) (6,8) (7,7) (1, 0) (5, 9) (0, 0) (0, 0) (1,0) (2,0) (3,0) (4,0) (5,-9) (2, 0) (6, 8) (0, 0) (0,0) (0,0) (0,0) (0,0) (0, 0) (6,-8) (3, 0) (7, 7) (0,0) (0,0) (0,0) (0,0) (0, 0) (0, 0) (7,-7) (4, 0) if uplo == rocblas_fill_lower: The leading (k + 1) by n part of each A_i must contain the lower triangular band part of the Hermitian matrix, with the leading diagonal in row (1), the first sub-diagonal on the LHS of row 2, etc. The bottom right k by k triangle of each A_i will not be referenced. Ex (lower, lda = 2, n = 4, k = 1): A Represented matrix (1,0) (2,0) (3,0) (4,0) (1, 0) (5,-9) (0, 0) (0, 0) (5,9) (6,8) (7,7) (0,0) (5, 9) (2, 0) (6,-8) (0, 0) (0, 0) (6, 8) (3, 0) (7,-7) (0, 0) (0, 0) (7, 7) (4, 0) As a Hermitian matrix, the imaginary part of the main diagonal of each A_i will not be referenced and is assumed to be == 0.

**lda**–**[in]**[rocblas_int] specifies the leading dimension of each A_i. must be >= max(1, n).**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i.**beta**–**[in]**device pointer or host pointer to scalar beta.**y**–**[inout]**device array of device pointers storing each vector y_i.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of y.**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `hbmv_batched`

functions support the `_64`

interface. Parameters `n`

and `k`

larger than `int32_t`

max value are not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_chbmv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_chbmv_strided_batched14rocblas_handle12rocblas_fill11rocblas_int11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_int14rocblas_stridePK21rocblas_float_complex11rocblas_int14rocblas_stridePK21rocblas_float_complexP21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zhbmv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_zhbmv_strided_batched14rocblas_handle12rocblas_fill11rocblas_int11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_int14rocblas_stridePK22rocblas_double_complex11rocblas_int14rocblas_stridePK22rocblas_double_complexP22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_int) **BLAS Level 2 API**hbmv_strided_batched performs one of the matrix-vector operations:

y_i := alpha*A_i*x_i + beta*y_i where alpha and beta are scalars, x_i and y_i are n element vectors and A_i is an n by n Hermitian band matrix with k super-diagonals, for each batch in i = [1, batch_count].

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: The upper triangular part of each A_i is being supplied.

rocblas_fill_lower: The lower triangular part of each A_i is being supplied.


**n**–**[in]**[rocblas_int] the order of each matrix A_i.**k**–**[in]**[rocblas_int] the number of super-diagonals of each matrix A_i. Must be >= 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**A**–**[in]**device array pointing to the first matrix A_1. Each A_i is of dimension (lda, n).if uplo == rocblas_fill_upper: The leading (k + 1) by n part of each A_i must contain the upper triangular band part of the Hermitian matrix, with the leading diagonal in row (k + 1), the first super-diagonal on the RHS of row k, etc. The top left k by x triangle of each A_i will not be referenced. Ex (upper, lda = n = 4, k = 1): A Represented matrix (0,0) (5,9) (6,8) (7,7) (1, 0) (5, 9) (0, 0) (0, 0) (1,0) (2,0) (3,0) (4,0) (5,-9) (2, 0) (6, 8) (0, 0) (0,0) (0,0) (0,0) (0,0) (0, 0) (6,-8) (3, 0) (7, 7) (0,0) (0,0) (0,0) (0,0) (0, 0) (0, 0) (7,-7) (4, 0) if uplo == rocblas_fill_lower: The leading (k + 1) by n part of each A_i must contain the lower triangular band part of the Hermitian matrix, with the leading diagonal in row (1), the first sub-diagonal on the LHS of row 2, etc. The bottom right k by k triangle of each A_i will not be referenced. Ex (lower, lda = 2, n = 4, k = 1): A Represented matrix (1,0) (2,0) (3,0) (4,0) (1, 0) (5,-9) (0, 0) (0, 0) (5,9) (6,8) (7,7) (0,0) (5, 9) (2, 0) (6,-8) (0, 0) (0, 0) (6, 8) (3, 0) (7,-7) (0, 0) (0, 0) (7, 7) (4, 0) As a Hermitian matrix, the imaginary part of the main diagonal of each A_i will not be referenced and is assumed to be == 0.

**lda**–**[in]**[rocblas_int] specifies the leading dimension of each A_i. must be >= max(1, n).**stride_A**–**[in]**[rocblas_stride] stride from the start of one matrix (A_i) and the next one (A_i+1).**x**–**[in]**device array pointing to the first vector y_1.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i.**stride_x**–**[in]**[rocblas_stride] stride from the start of one vector (x_i) and the next one (x_i+1).**beta**–**[in]**device pointer or host pointer to scalar beta.**y**–**[inout]**device array pointing to the first vector y_1.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of y.**stride_y**–**[in]**[rocblas_stride] stride from the start of one vector (y_i) and the next one (y_i+1).**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `hbmv_strided_batched`

functions support the `_64`

interface. Parameters `n`

and `k`

larger than `int32_t`

max value are not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xhpmv + batched, strided_batched[#](#rocblas-xhpmv-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_chpmv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*AP, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy)[#](#_CPPv413rocblas_chpmv14rocblas_handle12rocblas_fill11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_intPK21rocblas_float_complexP21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zhpmv([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*AP, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy)[#](#_CPPv413rocblas_zhpmv14rocblas_handle12rocblas_fill11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_intPK22rocblas_double_complexP22rocblas_double_complex11rocblas_int) **BLAS Level 2 API**hpmv performs the matrix-vector operation:

y := alpha*A*x + beta*y where alpha and beta are scalars, x and y are n element vectors and A is an n by n Hermitian matrix, supplied in packed form (see description below).

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: the upper triangular part of the Hermitian matrix A is supplied in AP.

rocblas_fill_lower: the lower triangular part of the Hermitian matrix A is supplied in AP.


**n**–**[in]**[rocblas_int] the order of the matrix A. Must be >= 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**AP**–**[in]**device pointer storing the packed version of the specified triangular portion of the Hermitian matrix A. Of at least size ((n * (n + 1)) / 2).Note that the imaginary part of the diagonal elements are not accessed and are assumed to be 0.if uplo == rocblas_fill_upper: The upper triangular portion of the Hermitian matrix A is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(0,1) AP(2) = A(1,1), etc. Ex: (rocblas_fill_upper; n = 3) (1, 0) (2, 1) (3, 2) (2,-1) (4, 0) (5,-1) ---> [(1,0),(2,1),(4,0),(3,2),(5,-1),(6,0)] (3,-2) (5, 1) (6, 0) if uplo == rocblas_fill_lower: The lower triangular portion of the Hermitian matrix A is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(1,0) AP(2) = A(2,1), etc. Ex: (rocblas_fill_lower; n = 3) (1, 0) (2, 1) (3, 2) (2,-1) (4, 0) (5,-1) ---> [(1,0),(2,-1),(3,-2),(4,0),(5,1),(6,0)] (3,-2) (5, 1) (6, 0)

**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of x.**beta**–**[in]**device pointer or host pointer to scalar beta.**y**–**[inout]**device pointer storing vector y.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of y.



The `hpmv`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_chpmv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const AP[], const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_chpmv_batched14rocblas_handle12rocblas_fill11rocblas_intPK21rocblas_float_complexA_PCK21rocblas_float_complexA_PCK21rocblas_float_complex11rocblas_intPK21rocblas_float_complexA_PC21rocblas_float_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zhpmv_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const AP[], const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_zhpmv_batched14rocblas_handle12rocblas_fill11rocblas_intPK22rocblas_double_complexA_PCK22rocblas_double_complexA_PCK22rocblas_double_complex11rocblas_intPK22rocblas_double_complexA_PC22rocblas_double_complex11rocblas_int11rocblas_int) **BLAS Level 2 API**hpmv_batched performs the matrix-vector operation:

y_i := alpha*A_i*x_i + beta*y_i where alpha and beta are scalars, x_i and y_i are n element vectors and A_i is an n by n Hermitian matrix, supplied in packed form (see description below), for each batch in i = [1, batch_count].

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: the upper triangular part of each Hermitian matrix A_i is supplied in AP.

rocblas_fill_lower: the lower triangular part of each Hermitian matrix A_i is supplied in AP.


**n**–**[in]**[rocblas_int] the order of each matrix A_i.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**AP**–**[in]**device pointer of device pointers storing the packed version of the specified triangular portion of each Hermitian matrix A_i. Each A_i is of at least size ((n * (n + 1)) / 2).if uplo == rocblas_fill_upper: The upper triangular portion of each Hermitian matrix A_i is supplied. The matrix is compacted so that each AP_i contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(0,1) AP(2) = A(1,1), etc. Ex: (rocblas_fill_upper; n = 3) (1, 0) (2, 1) (3, 2) (2,-1) (4, 0) (5,-1) ---> [(1,0),(2,1),(4,0),(3,2),(5,-1),(6,0)] (3,-2) (5, 1) (6, 0) if uplo == rocblas_fill_lower: The lower triangular portion of each Hermitian matrix A_i is supplied. The matrix is compacted so that each AP_i contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(1,0) AP(2) = A(2,1), etc. Ex: (rocblas_fill_lower; n = 3) (1, 0) (2, 1) (3, 2) (2,-1) (4, 0) (5,-1) ---> [(1,0),(2,-1),(3,-2),(4,0),(5,1),(6,0)] (3,-2) (5, 1) (6, 0) Note that the imaginary part of the diagonal elements are not accessed and are assumed to be 0.

**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i.**beta**–**[in]**device pointer or host pointer to scalar beta.**y**–**[inout]**device array of device pointers storing each vector y_i.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of y.**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `hpmv_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_chpmv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*AP,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_chpmv_strided_batched14rocblas_handle12rocblas_fill11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex14rocblas_stridePK21rocblas_float_complex11rocblas_int14rocblas_stridePK21rocblas_float_complexP21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zhpmv_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*AP,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_zhpmv_strided_batched14rocblas_handle12rocblas_fill11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex14rocblas_stridePK22rocblas_double_complex11rocblas_int14rocblas_stridePK22rocblas_double_complexP22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_int) **BLAS Level 2 API**hpmv_strided_batched performs the matrix-vector operation:

y_i := alpha*A_i*x_i + beta*y_i where alpha and beta are scalars, x_i and y_i are n element vectors and A_i is an n by n Hermitian matrix, supplied in packed form (see description below), for each batch in i = [1, batch_count].

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: the upper triangular part of each Hermitian matrix A_i is supplied in AP.

rocblas_fill_lower: the lower triangular part of each Hermitian matrix A_i is supplied in AP.


**n**–**[in]**[rocblas_int] the order of each matrix A_i.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**AP**–**[in]**device pointer pointing to the beginning of the first matrix (AP_1). Stores the packed version of the specified triangular portion of each Hermitian matrix AP_i of size ((n * (n + 1)) / 2).if uplo == rocblas_fill_upper: The upper triangular portion of each Hermitian matrix A_i is supplied. The matrix is compacted so that each AP_i contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(0,1) AP(2) = A(1,1), etc. Ex: (rocblas_fill_upper; n = 3) (1, 0) (2, 1) (3, 2) (2,-1) (4, 0) (5,-1) ---> [(1,0),(2,1),(4,0),(3,2),(5,-1),(6,0)] (3,-2) (5, 1) (6, 0) if uplo == rocblas_fill_lower: The lower triangular portion of each Hermitian matrix A_i is supplied. The matrix is compacted so that each AP_i contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(1,0) AP(2) = A(2,1), etc. Ex: (rocblas_fill_lower; n = 3) (1, 0) (2, 1) (3, 2) (2,-1) (4, 0) (5,-1) ---> [(1,0),(2,-1),(3,-2),(4,0),(5,1),(6,0)] (3,-2) (5, 1) (6, 0) Note that the imaginary part of the diagonal elements are not accessed and are assumed to be 0.

**stride_A**–**[in]**[rocblas_stride] stride from the start of one matrix (AP_i) and the next one (AP_i+1).**x**–**[in]**device array pointing to the beginning of the first vector (x_1).**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i.**stride_x**–**[in]**[rocblas_stride] stride from the start of one vector (x_i) and the next one (x_i+1).**beta**–**[in]**device pointer or host pointer to scalar beta.**y**–**[inout]**device array pointing to the beginning of the first vector (y_1).**incy**–**[in]**[rocblas_int] specifies the increment for the elements of y.**stride_y**–**[in]**[rocblas_stride] stride from the start of one vector (y_i) and the next one (y_i+1).**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `hpmv_strided_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xher + batched, strided_batched[#](#rocblas-xher-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cher([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda)[#](#_CPPv412rocblas_cher14rocblas_handle12rocblas_fill11rocblas_intPKfPK21rocblas_float_complex11rocblas_intP21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zher([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda)[#](#_CPPv412rocblas_zher14rocblas_handle12rocblas_fill11rocblas_intPKdPK22rocblas_double_complex11rocblas_intP22rocblas_double_complex11rocblas_int) **BLAS Level 2 API**her performs the matrix-vector operations:

A := A + alpha*x*x**H where alpha is a real scalar, x is a vector, and A is an n by n Hermitian matrix.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill] specifies whether the upper ‘rocblas_fill_upper’ or lower ‘rocblas_fill_lower’rocblas_fill_upper: The upper triangular part of A is supplied in A.

rocblas_fill_lower: The lower triangular part of A is supplied in A.


**n**–**[in]**[rocblas_int] the number of rows and columns of matrix A. Must be at least 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of x.**A**–**[inout]**device pointer storing the specified triangular portion of the Hermitian matrix A. Of size (lda * n).if uplo == rocblas_fill_upper: The upper triangular portion of the Hermitian matrix A is supplied. The lower triangluar portion will not be touched. if uplo == rocblas_fill_lower: The lower triangular portion of the Hermitian matrix A is supplied. The upper triangular portion will not be touched. Note that the imaginary part of the diagonal elements are not accessed and are assumed to be 0.

**lda**–**[in]**[rocblas_int] specifies the leading dimension of A. Must be at least max(1, n).



The `her`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cher_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv420rocblas_cher_batched14rocblas_handle12rocblas_fill11rocblas_intPKfA_PCK21rocblas_float_complex11rocblas_intA_PC21rocblas_float_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zher_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv420rocblas_zher_batched14rocblas_handle12rocblas_fill11rocblas_intPKdA_PCK22rocblas_double_complex11rocblas_intA_PC22rocblas_double_complex11rocblas_int11rocblas_int) **BLAS Level 2 API**her_batched performs the matrix-vector operations:

A_i := A_i + alpha*x_i*x_i**H where alpha is a real scalar, x_i is a vector, and A_i is an n by n symmetric matrix, for i = 1, ..., batch_count.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill] specifies whether the upper ‘rocblas_fill_upper’ or lower ‘rocblas_fill_lower’rocblas_fill_upper: The upper triangular part of each A_i is supplied in A.

rocblas_fill_lower: The lower triangular part of each A_i is supplied in A.


**n**–**[in]**[rocblas_int] the number of rows and columns of each matrix A_i. Must be at least 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i.**A**–**[inout]**device array of device pointers storing the specified triangular portion of each Hermitian matrix A_i of at least size ((n * (n + 1)) / 2). Array is of at least size batch_count.if uplo == rocblas_fill_upper: The upper triangular portion of each Hermitian matrix A_i is supplied. The lower triangular portion of each A_i will not be touched. if uplo == rocblas_fill_lower: The lower triangular portion of each Hermitian matrix A_i is supplied. The upper triangular portion of each A_i will not be touched. Note that the imaginary part of the diagonal elements are not accessed and are assumed to be 0.

**lda**–**[in]**[rocblas_int] specifies the leading dimension of each A_i. Must be at least max(1, n).**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `her_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cher_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv428rocblas_cher_strided_batched14rocblas_handle12rocblas_fill11rocblas_intPKfPK21rocblas_float_complex11rocblas_int14rocblas_strideP21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zher_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv428rocblas_zher_strided_batched14rocblas_handle12rocblas_fill11rocblas_intPKdPK22rocblas_double_complex11rocblas_int14rocblas_strideP22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_int) **BLAS Level 2 API**her_strided_batched performs the matrix-vector operations:

A_i := A_i + alpha*x_i*x_i**H where alpha is a real scalar, x_i is a vector, and A_i is an n by n Hermitian matrix, for i = 1, ..., batch_count.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill] specifies whether the upper ‘rocblas_fill_upper’ or lower ‘rocblas_fill_lower’rocblas_fill_upper: The upper triangular part of each A_i is supplied in A.

rocblas_fill_lower: The lower triangular part of each A_i is supplied in A.


**n**–**[in]**[rocblas_int] the number of rows and columns of each matrix A_i. Must be at least 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device pointer pointing to the first vector (x_1).**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i.**stride_x**–**[in]**[rocblas_stride] stride from the start of one vector (x_i) and the next one (x_i+1).**A**–**[inout]**device array of device pointers storing the specified triangular portion of each Hermitian matrix A_i. Points to the first matrix (A_1).Note that the imaginary part of the diagonal elements are not accessed and are assumed to be 0.if uplo == rocblas_fill_upper: The upper triangular portion of each Hermitian matrix A_i is supplied. The lower triangular portion of each A_i will not be touched. if uplo == rocblas_fill_lower: The lower triangular portion of each Hermitian matrix A_i is supplied. The upper triangular portion of each A_i will not be touched.

**lda**–**[in]**[rocblas_int] specifies the leading dimension of each A_i.**stride_A**–**[in]**[rocblas_stride] stride from the start of one (A_i) and the next (A_i+1).**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `her_strided_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xher2 + batched, strided_batched[#](#rocblas-xher2-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cher2([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda)[#](#_CPPv413rocblas_cher214rocblas_handle12rocblas_fill11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_intPK21rocblas_float_complex11rocblas_intP21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zher2([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda)[#](#_CPPv413rocblas_zher214rocblas_handle12rocblas_fill11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_intPK22rocblas_double_complex11rocblas_intP22rocblas_double_complex11rocblas_int) **BLAS Level 2 API**her2 performs the matrix-vector operations:

A := A + alpha*x*y**H + conj(alpha)*y*x**H where alpha is a complex scalar, x and y are vectors, and A is an n by n Hermitian matrix.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill] specifies whether the upper ‘rocblas_fill_upper’ or lower ‘rocblas_fill_lower’rocblas_fill_upper: The upper triangular part of A is supplied.

rocblas_fill_lower: The lower triangular part of A is supplied.


**n**–**[in]**[rocblas_int] the number of rows and columns of matrix A. Must be at least 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of x.**y**–**[in]**device pointer storing vector y.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of y.**A**–**[inout]**device pointer storing the specified triangular portion of the Hermitian matrix A. Of size (lda, n).Note that the imaginary part of the diagonal elements are not accessed and are assumed to be 0.if uplo == rocblas_fill_upper: The upper triangular portion of the Hermitian matrix A is supplied. The lower triangular portion of A will not be touched. if uplo == rocblas_fill_lower: The lower triangular portion of the Hermitian matrix A is supplied. The upper triangular portion of A will not be touched.

**lda**–**[in]**[rocblas_int] specifies the leading dimension of A. Must be at least max(lda, 1).



The `her2`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cher2_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_cher2_batched14rocblas_handle12rocblas_fill11rocblas_intPK21rocblas_float_complexA_PCK21rocblas_float_complex11rocblas_intA_PCK21rocblas_float_complex11rocblas_intA_PC21rocblas_float_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zher2_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_zher2_batched14rocblas_handle12rocblas_fill11rocblas_intPK22rocblas_double_complexA_PCK22rocblas_double_complex11rocblas_intA_PCK22rocblas_double_complex11rocblas_intA_PC22rocblas_double_complex11rocblas_int11rocblas_int) **BLAS Level 2 API**her2_batched performs the matrix-vector operations:

A_i := A_i + alpha*x_i*y_i**H + conj(alpha)*y_i*x_i**H where alpha is a complex scalar, x_i and y_i are vectors, and A_i is an n by n Hermitian matrix for each batch in i = [1, batch_count].

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill] specifies whether the upper ‘rocblas_fill_upper’ or lower ‘rocblas_fill_lower’rocblas_fill_upper: The upper triangular part of each A_i is supplied.

rocblas_fill_lower: The lower triangular part of each A_i is supplied.


**n**–**[in]**[rocblas_int] the number of rows and columns of each matrix A_i. Must be at least 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of x.**y**–**[in]**device array of device pointers storing each vector y_i.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of each y_i.**A**–**[inout]**device array of device pointers storing the specified triangular portion of each Hermitian matrix A_i of size (lda, n).Note that the imaginary part of the diagonal elements are not accessed and are assumed to be 0.if uplo == rocblas_fill_upper: The upper triangular portion of each Hermitian matrix A_i is supplied. The lower triangular portion of each A_i will not be touched. if uplo == rocblas_fill_lower: The lower triangular portion of each Hermitian matrix A_i is supplied. The upper triangular portion of each A_i will not be touched.

**lda**–**[in]**[rocblas_int] specifies the leading dimension of each A_i. Must be at least max(lda, 1).**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `her2_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cher2_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_y,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_cher2_strided_batched14rocblas_handle12rocblas_fill11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_int14rocblas_stridePK21rocblas_float_complex11rocblas_int14rocblas_strideP21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zher2_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_y,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_zher2_strided_batched14rocblas_handle12rocblas_fill11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_int14rocblas_stridePK22rocblas_double_complex11rocblas_int14rocblas_strideP22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_int) **BLAS Level 2 API**her2_strided_batched performs the matrix-vector operations:

A_i := A_i + alpha*x_i*y_i**H + conj(alpha)*y_i*x_i**H where alpha is a complex scalar, x_i and y_i are vectors, and A_i is an n by n Hermitian matrix for each batch in i = [1, batch_count].

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill] specifies whether the upper ‘rocblas_fill_upper’ or lower ‘rocblas_fill_lower’rocblas_fill_upper: The upper triangular part of each A_i is supplied.

rocblas_fill_lower: The lower triangular part of each A_i is supplied.


**n**–**[in]**[rocblas_int] the number of rows and columns of each matrix A_i. Must be at least 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device pointer pointing to the first vector x_1.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i.**stride_x**–**[in]**[rocblas_stride] specifies the stride between the beginning of one vector (x_i) and the next (x_i+1).**y**–**[in]**device pointer pointing to the first vector y_i.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of each y_i.**stride_y**–**[in]**[rocblas_stride] specifies the stride between the beginning of one vector (y_i) and the next (y_i+1).**A**–**[inout]**device pointer pointing to the first matrix (A_1). Stores the specified triangular portion of each Hermitian matrix A_i.Note that the imaginary part of the diagonal elements are not accessed and are assumed to be 0.if uplo == rocblas_fill_upper: The upper triangular portion of each Hermitian matrix A_i is supplied. The lower triangular portion of each A_i will not be touched. if uplo == rocblas_fill_lower: The lower triangular portion of each Hermitian matrix A_i is supplied. The upper triangular portion of each A_i will not be touched.

**lda**–**[in]**[rocblas_int] specifies the leading dimension of each A_i. Must be at least max(lda, 1).**stride_A**–**[in]**[rocblas_stride] specifies the stride between the beginning of one matrix (A_i) and the next (A_i+1).**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `her2_strided_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xhpr + batched, strided_batched[#](#rocblas-xhpr-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_chpr([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*AP)[#](#_CPPv412rocblas_chpr14rocblas_handle12rocblas_fill11rocblas_intPKfPK21rocblas_float_complex11rocblas_intP21rocblas_float_complex)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zhpr([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*AP)[#](#_CPPv412rocblas_zhpr14rocblas_handle12rocblas_fill11rocblas_intPKdPK22rocblas_double_complex11rocblas_intP22rocblas_double_complex) **BLAS Level 2 API**hpr performs the matrix-vector operations:

A := A + alpha*x*x**H where alpha is a real scalar, x is a vector, and A is an n by n Hermitian matrix, supplied in packed form.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill] specifies whether the upper ‘rocblas_fill_upper’ or lower ‘rocblas_fill_lower’rocblas_fill_upper: The upper triangular part of A is supplied in AP.

rocblas_fill_lower: The lower triangular part of A is supplied in AP.


**n**–**[in]**[rocblas_int] the number of rows and columns of matrix A. Must be at least 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of x.**AP**–**[inout]**device pointer storing the packed version of the specified triangular portion of the Hermitian matrix A. Of at least size ((n * (n + 1)) / 2).if uplo == rocblas_fill_upper: The upper triangular portion of the Hermitian matrix A is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(0,1) AP(2) = A(1,1), etc. Ex: (rocblas_fill_upper; n = 3) (1, 0) (2, 1) (4,9) (2,-1) (3, 0) (5,3) ---> [(1,0),(2,1),(3,0),(4,9),(5,3),(6,0)] (4,-9) (5,-3) (6,0) if uplo == rocblas_fill_lower: The lower triangular portion of the Hermitian matrix A is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(1,0) AP(2) = A(2,1), etc. Ex: (rocblas_fill_lower; n = 3) (1, 0) (2, 1) (4,9) (2,-1) (3, 0) (5,3) ---> [(1,0),(2,-1),(4,-9),(3,0),(5,-3),(6,0)] (4,-9) (5,-3) (6,0) Note that the imaginary part of the diagonal elements are not accessed and are assumed to be 0.




The `hpr`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_chpr_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const AP[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv420rocblas_chpr_batched14rocblas_handle12rocblas_fill11rocblas_intPKfA_PCK21rocblas_float_complex11rocblas_intA_PC21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zhpr_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const AP[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv420rocblas_zhpr_batched14rocblas_handle12rocblas_fill11rocblas_intPKdA_PCK22rocblas_double_complex11rocblas_intA_PC22rocblas_double_complex11rocblas_int) **BLAS Level 2 API**hpr_batched performs the matrix-vector operations:

A_i := A_i + alpha*x_i*x_i**H where alpha is a real scalar, x_i is a vector, and A_i is an n by n symmetric matrix, supplied in packed form, for i = 1, ..., batch_count.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill] specifies whether the upper ‘rocblas_fill_upper’ or lower ‘rocblas_fill_lower’rocblas_fill_upper: The upper triangular part of each A_i is supplied in AP.

rocblas_fill_lower: The lower triangular part of each A_i is supplied in AP.


**n**–**[in]**[rocblas_int] the number of rows and columns of each matrix A_i. Must be at least 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i.**AP**–**[inout]**device array of device pointers storing the packed version of the specified triangular portion of each Hermitian matrix A_i of at least size ((n * (n + 1)) / 2). Array is of at least size batch_count.if uplo == rocblas_fill_upper: The upper triangular portion of each Hermitian matrix A_i is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(0,1) AP(2) = A(1,1), etc. Ex: (rocblas_fill_upper; n = 3) (1, 0) (2, 1) (4,9) (2,-1) (3, 0) (5,3) ---> [(1,0),(2,1),(3,0),(4,9),(5,3),(6,0)] (4,-9) (5,-3) (6,0) if uplo == rocblas_fill_lower: The lower triangular portion of each Hermitian matrix A_i is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(1,0) AP(2) = A(2,1), etc. Ex: (rocblas_fill_lower; n = 3) (1, 0) (2, 1) (4,9) (2,-1) (3, 0) (5,3) ---> [(1,0),(2,-1),(4,-9),(3,0),(5,-3),(6,0)] (4,-9) (5,-3) (6,0) Note that the imaginary part of the diagonal elements are not accessed and are assumed to be 0.

**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `hpr_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_chpr_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*AP,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv428rocblas_chpr_strided_batched14rocblas_handle12rocblas_fill11rocblas_intPKfPK21rocblas_float_complex11rocblas_int14rocblas_strideP21rocblas_float_complex14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zhpr_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*AP,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv428rocblas_zhpr_strided_batched14rocblas_handle12rocblas_fill11rocblas_intPKdPK22rocblas_double_complex11rocblas_int14rocblas_strideP22rocblas_double_complex14rocblas_stride11rocblas_int) **BLAS Level 2 API**hpr_strided_batched performs the matrix-vector operations:

A_i := A_i + alpha*x_i*x_i**H where alpha is a real scalar, x_i is a vector, and A_i is an n by n symmetric matrix, supplied in packed form, for i = 1, ..., batch_count.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill] specifies whether the upper ‘rocblas_fill_upper’ or lower ‘rocblas_fill_lower’rocblas_fill_upper: The upper triangular part of each A_i is supplied in AP.

rocblas_fill_lower: The lower triangular part of each A_i is supplied in AP.


**n**–**[in]**[rocblas_int] the number of rows and columns of each matrix A_i. Must be at least 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device pointer pointing to the first vector (x_1).**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i.**stride_x**–**[in]**[rocblas_stride] stride from the start of one vector (x_i) and the next one (x_i+1).**AP**–**[inout]**device array of device pointers storing the packed version of the specified triangular portion of each Hermitian matrix A_i. Points to the first matrix (A_1).if uplo == rocblas_fill_upper: The upper triangular portion of each Hermitian matrix A_i is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(0,1) AP(2) = A(1,1), etc. Ex: (rocblas_fill_upper; n = 3) (1, 0) (2, 1) (4,9) (2,-1) (3, 0) (5,3) ---> [(1,0),(2,1),(3,0),(4,9),(5,3),(6,0)] (4,-9) (5,-3) (6,0) if uplo == rocblas_fill_lower: The lower triangular portion of each Hermitian matrix A_i is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(1,0) AP(2) = A(2,1), etc. Ex: (rocblas_fill_lower; n = 3) (1, 0) (2, 1) (4,9) (2,-1) (3, 0) (5,3) ---> [(1,0),(2,-1),(4,-9),(3,0),(5,-3),(6,0)] (4,-9) (5,-3) (6,0) Note that the imaginary part of the diagonal elements are not accessed and are assumed to be 0.

**stride_A**–**[in]**[rocblas_stride] stride from the start of one (A_i) and the next (A_i+1).**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `hpr_strided_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xhpr2 + batched, strided_batched[#](#rocblas-xhpr2-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_chpr2([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*AP)[#](#_CPPv413rocblas_chpr214rocblas_handle12rocblas_fill11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_intPK21rocblas_float_complex11rocblas_intP21rocblas_float_complex)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zhpr2([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*AP)[#](#_CPPv413rocblas_zhpr214rocblas_handle12rocblas_fill11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_intPK22rocblas_double_complex11rocblas_intP22rocblas_double_complex) **BLAS Level 2 API**hpr2 performs the matrix-vector operations:

A := A + alpha*x*y**H + conj(alpha)*y*x**H where alpha is a complex scalar, x and y are vectors, and A is an n by n Hermitian matrix, supplied in packed form.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill] specifies whether the upper ‘rocblas_fill_upper’ or lower ‘rocblas_fill_lower’rocblas_fill_upper: The upper triangular part of A is supplied in AP.

rocblas_fill_lower: The lower triangular part of A is supplied in AP.


**n**–**[in]**[rocblas_int] the number of rows and columns of matrix A. Must be at least 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of x.**y**–**[in]**device pointer storing vector y.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of y.**AP**–**[inout]**device pointer storing the packed version of the specified triangular portion of the Hermitian matrix A. Of at least size ((n * (n + 1)) / 2).if uplo == rocblas_fill_upper: The upper triangular portion of the Hermitian matrix A is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(0,1) AP(2) = A(1,1), etc. Ex: (rocblas_fill_upper; n = 3) (1, 0) (2, 1) (4,9) (2,-1) (3, 0) (5,3) ---> [(1,0),(2,1),(3,0),(4,9),(5,3),(6,0)] (4,-9) (5,-3) (6,0) if uplo == rocblas_fill_lower: The lower triangular portion of the Hermitian matrix A is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(1,0) AP(2) = A(2,1), etc. Ex: (rocblas_fill_lower; n = 3) (1, 0) (2, 1) (4,9) (2,-1) (3, 0) (5,3) ---> [(1,0),(2,-1),(4,-9),(3,0),(5,-3),(6,0)] (4,-9) (5,-3) (6,0) Note that the imaginary part of the diagonal elements are not accessed and are assumed to be 0.




The `hpr2`

functions support the `_64`

interface. A parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_chpr2_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const AP[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_chpr2_batched14rocblas_handle12rocblas_fill11rocblas_intPK21rocblas_float_complexA_PCK21rocblas_float_complex11rocblas_intA_PCK21rocblas_float_complex11rocblas_intA_PC21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zhpr2_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const AP[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_zhpr2_batched14rocblas_handle12rocblas_fill11rocblas_intPK22rocblas_double_complexA_PCK22rocblas_double_complex11rocblas_intA_PCK22rocblas_double_complex11rocblas_intA_PC22rocblas_double_complex11rocblas_int) **BLAS Level 2 API**hpr2_batched performs the matrix-vector operations:

A_i := A_i + alpha*x_i*y_i**H + conj(alpha)*y_i*x_i**H where alpha is a complex scalar, x_i and y_i are vectors, and A_i is an n by n symmetric matrix, supplied in packed form, for i = 1, ..., batch_count.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill] specifies whether the upper ‘rocblas_fill_upper’ or lower ‘rocblas_fill_lower’rocblas_fill_upper: The upper triangular part of each A_i is supplied in AP.

rocblas_fill_lower: The lower triangular part of each A_i is supplied in AP.


**n**–**[in]**[rocblas_int] the number of rows and columns of each matrix A_i. Must be at least 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i.**y**–**[in]**device array of device pointers storing each vector y_i.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of each y_i.**AP**–**[inout]**device array of device pointers storing the packed version of the specified triangular portion of each Hermitian matrix A_i of at least size ((n * (n + 1)) / 2). Array is of at least size batch_count.if uplo == rocblas_fill_upper: The upper triangular portion of each Hermitian matrix A_i is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(0,1) AP(2) = A(1,1), etc. Ex: (rocblas_fill_upper; n = 3) (1, 0) (2, 1) (4,9) (2,-1) (3, 0) (5,3) ---> [(1,0),(2,1),(3,0),(4,9),(5,3),(6,0)] (4,-9) (5,-3) (6,0) if uplo == rocblas_fill_lower: The lower triangular portion of each Hermitian matrix A_i is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(1,0) AP(2) = A(2,1), etc. Ex: (rocblas_fill_lower; n = 3) (1, 0) (2, 1) (4,9) (2,-1) (3, 0) (5,3) --> [(1,0),(2,-1),(4,-9),(3,0),(5,-3),(6,0)] (4,-9) (5,-3) (6,0) Note that the imaginary part of the diagonal elements are not accessed and are assumed to be 0.

**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `hpr2_batched`

functions support the `_64`

interface. A parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_chpr2_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_y,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*AP,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_chpr2_strided_batched14rocblas_handle12rocblas_fill11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_int14rocblas_stridePK21rocblas_float_complex11rocblas_int14rocblas_strideP21rocblas_float_complex14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zhpr2_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_y,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*AP,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_zhpr2_strided_batched14rocblas_handle12rocblas_fill11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_int14rocblas_stridePK22rocblas_double_complex11rocblas_int14rocblas_strideP22rocblas_double_complex14rocblas_stride11rocblas_int) **BLAS Level 2 API**hpr2_strided_batched performs the matrix-vector operations:

A_i := A_i + alpha*x_i*y_i**H + conj(alpha)*y_i*x_i**H where alpha is a complex scalar, x_i and y_i are vectors, and A_i is an n by n symmetric matrix, supplied in packed form, for i = 1, ..., batch_count.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill] specifies whether the upper ‘rocblas_fill_upper’ or lower ‘rocblas_fill_lower’rocblas_fill_upper: The upper triangular part of each A_i is supplied in AP.

rocblas_fill_lower: The lower triangular part of each A_i is supplied in AP.


**n**–**[in]**[rocblas_int] the number of rows and columns of each matrix A_i. Must be at least 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device pointer pointing to the first vector (x_1).**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i.**stride_x**–**[in]**[rocblas_stride] stride from the start of one vector (x_i) and the next one (x_i+1).**y**–**[in]**device pointer pointing to the first vector (y_1).**incy**–**[in]**[rocblas_int] specifies the increment for the elements of each y_i.**stride_y**–**[in]**[rocblas_stride] stride from the start of one vector (y_i) and the next one (y_i+1).**AP**–**[inout]**device array of device pointers storing the packed version of the specified triangular portion of each Hermitian matrix A_i. Points to the first matrix (A_1).if uplo == rocblas_fill_upper: The upper triangular portion of each Hermitian matrix A_i is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(0,1) AP(2) = A(1,1), etc. Ex: (rocblas_fill_upper; n = 3) (1, 0) (2, 1) (4,9) (2,-1) (3, 0) (5,3) ---> [(1,0),(2,1),(3,0),(4,9),(5,3),(6,0)] (4,-9) (5,-3) (6,0) if uplo == rocblas_fill_lower: The lower triangular portion of each Hermitian matrix A_i is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(1,0) AP(2) = A(2,1), etc. Ex: (rocblas_fill_lower; n = 3) (1, 0) (2, 1) (4,9) (2,-1) (3, 0) (5,3) ---> [(1,0),(2,-1),(4,-9),(3,0),(5,-3),(6,0)] (4,-9) (5,-3) (6,0) Note that the imaginary part of the diagonal elements are not accessed and are assumed to be 0.

**stride_A**–**[in]**[rocblas_stride] stride from the start of one (A_i) and the next (A_i+1).**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `hpr2_strided_batched`

functions support the `_64`

interface. A parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.
