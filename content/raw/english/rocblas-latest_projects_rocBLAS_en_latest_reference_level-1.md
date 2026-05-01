---
title: "rocBLAS Level-1 functions &#8212; rocBLAS 5.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/level-1.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:10:34.374710+00:00
content_hash: "053aec7310d98c53"
---

# rocBLAS Level-1 functions[#](#rocblas-level-1-functions)

rocBLAS Level-1 functions perform scalar, vector, and vector-vector operations. [[Level1]](references.html#level1)

Level-1 functions support the ILP64 API. For more information on these `_64`

functions, see the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_iXamax + batched, strided_batched[#](#rocblas-ixamax-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_isamax([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)*result)[#](#_CPPv414rocblas_isamax14rocblas_handle11rocblas_intPKf11rocblas_intP11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_idamax([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)*result)[#](#_CPPv414rocblas_idamax14rocblas_handle11rocblas_intPKd11rocblas_intP11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_icamax([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)*result)[#](#_CPPv414rocblas_icamax14rocblas_handle11rocblas_intPK21rocblas_float_complex11rocblas_intP11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_izamax([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)*result)[#](#_CPPv414rocblas_izamax14rocblas_handle11rocblas_intPK22rocblas_double_complex11rocblas_intP11rocblas_int) **BLAS Level 1 API**amax finds the first index of the element of maximum magnitude of a vector x.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**n**–**[in]**[rocblas_int] the number of elements in x.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of y.**result**–**[inout]**device pointer or host pointer to store the amax index. return is 0.0 if n, incx<=0.



The `amax`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_isamax_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count,[rocblas_int](datatypes.html#_CPPv411rocblas_int)*result)[#](#_CPPv422rocblas_isamax_batched14rocblas_handle11rocblas_intA_PCKf11rocblas_int11rocblas_intP11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_idamax_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count,[rocblas_int](datatypes.html#_CPPv411rocblas_int)*result)[#](#_CPPv422rocblas_idamax_batched14rocblas_handle11rocblas_intA_PCKd11rocblas_int11rocblas_intP11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_icamax_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count,[rocblas_int](datatypes.html#_CPPv411rocblas_int)*result)[#](#_CPPv422rocblas_icamax_batched14rocblas_handle11rocblas_intA_PCK21rocblas_float_complex11rocblas_int11rocblas_intP11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_izamax_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count,[rocblas_int](datatypes.html#_CPPv411rocblas_int)*result)[#](#_CPPv422rocblas_izamax_batched14rocblas_handle11rocblas_intA_PCK22rocblas_double_complex11rocblas_int11rocblas_intP11rocblas_int) **BLAS Level 1 API**amax_batched finds the first index of the element of maximum magnitude of each vector x_i in a batch, for i = 1, …, batch_count.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**n**–**[in]**[rocblas_int] number of elements in each vector x_i.**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i. incx must be > 0.**batch_count**–**[in]**[rocblas_int] number of instances in the batch. Must be > 0.**result**–**[out]**device or host array of pointers of batch_count size for results. return is 0 if n, incx<=0.



The `amax_batched`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_isamax_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count,[rocblas_int](datatypes.html#_CPPv411rocblas_int)*result)[#](#_CPPv430rocblas_isamax_strided_batched14rocblas_handle11rocblas_intPKf11rocblas_int14rocblas_stride11rocblas_intP11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_idamax_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count,[rocblas_int](datatypes.html#_CPPv411rocblas_int)*result)[#](#_CPPv430rocblas_idamax_strided_batched14rocblas_handle11rocblas_intPKd11rocblas_int14rocblas_stride11rocblas_intP11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_icamax_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count,[rocblas_int](datatypes.html#_CPPv411rocblas_int)*result)[#](#_CPPv430rocblas_icamax_strided_batched14rocblas_handle11rocblas_intPK21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_intP11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_izamax_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count,[rocblas_int](datatypes.html#_CPPv411rocblas_int)*result)[#](#_CPPv430rocblas_izamax_strided_batched14rocblas_handle11rocblas_intPK22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_intP11rocblas_int) **BLAS Level 1 API**amax_strided_batched finds the first index of the element of maximum magnitude of each vector x_i in a batch, for i = 1, …, batch_count.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**n**–**[in]**[rocblas_int] number of elements in each vector x_i.**x**–**[in]**device pointer to the first vector x_1.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i. incx must be > 0.**stridex**–**[in]**[rocblas_stride] specifies the pointer increment between one x_i and the next x_(i + 1).**batch_count**–**[in]**[rocblas_int] number of instances in the batch.**result**–**[out]**device or host pointer for storing contiguous batch_count results. return is 0 if n <= 0, incx<=0.



The `amax_strided_batched`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_iXamin + batched, strided_batched[#](#rocblas-ixamin-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_isamin([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)*result)[#](#_CPPv414rocblas_isamin14rocblas_handle11rocblas_intPKf11rocblas_intP11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_idamin([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)*result)[#](#_CPPv414rocblas_idamin14rocblas_handle11rocblas_intPKd11rocblas_intP11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_icamin([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)*result)[#](#_CPPv414rocblas_icamin14rocblas_handle11rocblas_intPK21rocblas_float_complex11rocblas_intP11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_izamin([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)*result)[#](#_CPPv414rocblas_izamin14rocblas_handle11rocblas_intPK22rocblas_double_complex11rocblas_intP11rocblas_int) **BLAS Level 1 API**amin finds the first index of the element of minimum magnitude of a vector x.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**n**–**[in]**[rocblas_int] the number of elements in x.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of y.**result**–**[inout]**device pointer or host pointer to store the amin index. return is 0.0 if n, incx<=0.



The `amin`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_isamin_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count,[rocblas_int](datatypes.html#_CPPv411rocblas_int)*result)[#](#_CPPv422rocblas_isamin_batched14rocblas_handle11rocblas_intA_PCKf11rocblas_int11rocblas_intP11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_idamin_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count,[rocblas_int](datatypes.html#_CPPv411rocblas_int)*result)[#](#_CPPv422rocblas_idamin_batched14rocblas_handle11rocblas_intA_PCKd11rocblas_int11rocblas_intP11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_icamin_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count,[rocblas_int](datatypes.html#_CPPv411rocblas_int)*result)[#](#_CPPv422rocblas_icamin_batched14rocblas_handle11rocblas_intA_PCK21rocblas_float_complex11rocblas_int11rocblas_intP11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_izamin_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count,[rocblas_int](datatypes.html#_CPPv411rocblas_int)*result)[#](#_CPPv422rocblas_izamin_batched14rocblas_handle11rocblas_intA_PCK22rocblas_double_complex11rocblas_int11rocblas_intP11rocblas_int) **BLAS Level 1 API**amin_batched finds the first index of the element of minimum magnitude of each vector x_i in a batch, for i = 1, …, batch_count.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**n**–**[in]**[rocblas_int] number of elements in each vector x_i.**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i. incx must be > 0.**batch_count**–**[in]**[rocblas_int] number of instances in the batch. Must be > 0.**result**–**[out]**device or host pointers to array of batch_count size for results. return is 0 if n, incx<=0.



The `amin_batched`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_isamin_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count,[rocblas_int](datatypes.html#_CPPv411rocblas_int)*result)[#](#_CPPv430rocblas_isamin_strided_batched14rocblas_handle11rocblas_intPKf11rocblas_int14rocblas_stride11rocblas_intP11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_idamin_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count,[rocblas_int](datatypes.html#_CPPv411rocblas_int)*result)[#](#_CPPv430rocblas_idamin_strided_batched14rocblas_handle11rocblas_intPKd11rocblas_int14rocblas_stride11rocblas_intP11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_icamin_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count,[rocblas_int](datatypes.html#_CPPv411rocblas_int)*result)[#](#_CPPv430rocblas_icamin_strided_batched14rocblas_handle11rocblas_intPK21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_intP11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_izamin_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count,[rocblas_int](datatypes.html#_CPPv411rocblas_int)*result)[#](#_CPPv430rocblas_izamin_strided_batched14rocblas_handle11rocblas_intPK22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_intP11rocblas_int) **BLAS Level 1 API**amin_strided_batched finds the first index of the element of minimum magnitude of each vector x_i in a batch, for i = 1, …, batch_count.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**n**–**[in]**[rocblas_int] number of elements in each vector x_i.**x**–**[in]**device pointer to the first vector x_1.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i. incx must be > 0.**stridex**–**[in]**[rocblas_stride] specifies the pointer increment between one x_i and the next x_(i + 1).**batch_count**–**[in]**[rocblas_int] number of instances in the batch.**result**–**[out]**device or host pointer to array for storing contiguous batch_count results. return is 0 if n <= 0, incx<=0.



The `amin_strided_batched`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xasum + batched, strided_batched[#](#rocblas-xasum-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sasum([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, float *result)[#](#_CPPv413rocblas_sasum14rocblas_handle11rocblas_intPKf11rocblas_intPf)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dasum([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, double *result)[#](#_CPPv413rocblas_dasum14rocblas_handle11rocblas_intPKd11rocblas_intPd)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_scasum([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, float *result)[#](#_CPPv414rocblas_scasum14rocblas_handle11rocblas_intPK21rocblas_float_complex11rocblas_intPf)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dzasum([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, double *result)[#](#_CPPv414rocblas_dzasum14rocblas_handle11rocblas_intPK22rocblas_double_complex11rocblas_intPd) **BLAS Level 1 API**asum computes the sum of the magnitudes of elements of a real vector x, or the sum of magnitudes of the real and imaginary parts of elements if x is a complex vector.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**n**–**[in]**[rocblas_int] the number of elements in x and y.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of x. incx must be > 0.**result**–**[inout]**device pointer or host pointer to store the asum product. return is 0.0 if n <= 0.



The `asum`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sasum_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count, float *results)[#](#_CPPv421rocblas_sasum_batched14rocblas_handle11rocblas_intA_PCKf11rocblas_int11rocblas_intPf)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dasum_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count, double *results)[#](#_CPPv421rocblas_dasum_batched14rocblas_handle11rocblas_intA_PCKd11rocblas_int11rocblas_intPd)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_scasum_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count, float *results)[#](#_CPPv422rocblas_scasum_batched14rocblas_handle11rocblas_intA_PCK21rocblas_float_complex11rocblas_int11rocblas_intPf)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dzasum_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count, double *results)[#](#_CPPv422rocblas_dzasum_batched14rocblas_handle11rocblas_intA_PCK22rocblas_double_complex11rocblas_int11rocblas_intPd) **BLAS Level 1 API**asum_batched computes the sum of the magnitudes of the elements in a batch of real vectors x_i, or the sum of magnitudes of the real and imaginary parts of elements if x_i is a complex vector, for i = 1, …, batch_count.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**n**–**[in]**[rocblas_int] number of elements in each vector x_i.**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i. incx must be > 0.**batch_count**–**[in]**[rocblas_int] number of instances in the batch.**results**–**[out]**device array or host array of batch_count size for results. return is 0.0 if n, incx<=0.



The `asum_batched`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sasum_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count, float *results)[#](#_CPPv429rocblas_sasum_strided_batched14rocblas_handle11rocblas_intPKf11rocblas_int14rocblas_stride11rocblas_intPf)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dasum_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count, double *results)[#](#_CPPv429rocblas_dasum_strided_batched14rocblas_handle11rocblas_intPKd11rocblas_int14rocblas_stride11rocblas_intPd)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_scasum_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count, float *results)[#](#_CPPv430rocblas_scasum_strided_batched14rocblas_handle11rocblas_intPK21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_intPf)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dzasum_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count, double *results)[#](#_CPPv430rocblas_dzasum_strided_batched14rocblas_handle11rocblas_intPK22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_intPd) **BLAS Level 1 API**asum_strided_batched computes the sum of the magnitudes of elements of a real vectors x_i, or the sum of magnitudes of the real and imaginary parts of elements if x_i is a complex vector, for i = 1, …, batch_count.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**n**–**[in]**[rocblas_int] number of elements in each vector x_i.**x**–**[in]**device pointer to the first vector x_1.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i. incx must be > 0.**stridex**–**[in]**[rocblas_stride] stride from the start of one vector (x_i) and the next one (x_i+1). There are no restrictions placed on stride_x. However, ensure that stride_x is of appropriate size. For a typical case this means stride_x >= n * incx.**results**–**[out]**device pointer or host pointer to array for storing contiguous batch_count results. return is 0.0 if n, incx<=0.**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `asum_strided_batched`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xaxpy + batched, strided_batched[#](#rocblas-xaxpy-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_saxpy([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, float *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy)[#](#_CPPv413rocblas_saxpy14rocblas_handle11rocblas_intPKfPKf11rocblas_intPf11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_daxpy([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, double *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy)[#](#_CPPv413rocblas_daxpy14rocblas_handle11rocblas_intPKdPKd11rocblas_intPd11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_haxpy([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_half](datatypes.html#_CPPv412rocblas_half)*alpha, const[rocblas_half](datatypes.html#_CPPv412rocblas_half)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_half](datatypes.html#_CPPv412rocblas_half)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy)[#](#_CPPv413rocblas_haxpy14rocblas_handle11rocblas_intPK12rocblas_halfPK12rocblas_half11rocblas_intP12rocblas_half11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_caxpy([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy)[#](#_CPPv413rocblas_caxpy14rocblas_handle11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_intP21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zaxpy([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy)[#](#_CPPv413rocblas_zaxpy14rocblas_handle11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_intP22rocblas_double_complex11rocblas_int) **BLAS Level 1 API**axpy computes constant alpha multiplied by vector x, plus vector y:

y := alpha * x + y

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**n**–**[in]**[rocblas_int] the number of elements in x and y.**alpha**–**[in]**device pointer or host pointer to specify the scalar alpha.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of x.**y**–**[out]**device pointer storing vector y.**incy**–**[inout]**[rocblas_int] specifies the increment for the elements of y.



The `axpy`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_saxpy_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, float *const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_saxpy_batched14rocblas_handle11rocblas_intPKfA_PCKf11rocblas_intA_PCf11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_daxpy_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, double *const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_daxpy_batched14rocblas_handle11rocblas_intPKdA_PCKd11rocblas_intA_PCd11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_haxpy_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_half](datatypes.html#_CPPv412rocblas_half)*alpha, const[rocblas_half](datatypes.html#_CPPv412rocblas_half)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_half](datatypes.html#_CPPv412rocblas_half)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_haxpy_batched14rocblas_handle11rocblas_intPK12rocblas_halfA_PCK12rocblas_half11rocblas_intA_PC12rocblas_half11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_caxpy_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_caxpy_batched14rocblas_handle11rocblas_intPK21rocblas_float_complexA_PCK21rocblas_float_complex11rocblas_intA_PC21rocblas_float_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zaxpy_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_zaxpy_batched14rocblas_handle11rocblas_intPK22rocblas_double_complexA_PCK22rocblas_double_complex11rocblas_intA_PC22rocblas_double_complex11rocblas_int11rocblas_int) **BLAS Level 1 API**axpy_batched compute y := alpha * x + y over a set of batched vectors.

- Parameters:
**handle**–**[in]**rocblas_handle handle to the rocblas library context queue.**n**–**[in]**rocblas_int**alpha**–**[in]**specifies the scalar alpha.**x**–**[in]**pointer storing vector x on the GPU.**incx**–**[in]**rocblas_int specifies the increment for the elements of x.**y**–**[out]**pointer storing vector y on the GPU.**incy**–**[inout]**rocblas_int specifies the increment for the elements of y.**batch_count**–**[in]**rocblas_int number of instances in the batch.



The `axpy_batched`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_saxpy_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, float *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_saxpy_strided_batched14rocblas_handle11rocblas_intPKfPKf11rocblas_int14rocblas_stridePf11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_daxpy_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, double *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_daxpy_strided_batched14rocblas_handle11rocblas_intPKdPKd11rocblas_int14rocblas_stridePd11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_haxpy_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_half](datatypes.html#_CPPv412rocblas_half)*alpha, const[rocblas_half](datatypes.html#_CPPv412rocblas_half)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex,[rocblas_half](datatypes.html#_CPPv412rocblas_half)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_haxpy_strided_batched14rocblas_handle11rocblas_intPK12rocblas_halfPK12rocblas_half11rocblas_int14rocblas_strideP12rocblas_half11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_caxpy_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_caxpy_strided_batched14rocblas_handle11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_int14rocblas_strideP21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zaxpy_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_zaxpy_strided_batched14rocblas_handle11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_int14rocblas_strideP22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_int) **BLAS Level 1 API**axpy_strided_batched compute y := alpha * x + y over a set of strided batched vectors.

- Parameters:
**handle**–**[in]**rocblas_handle handle to the rocblas library context queue.**n**–**[in]**rocblas_int.**alpha**–**[in]**specifies the scalar alpha.**x**–**[in]**pointer storing vector x on the GPU.**incx**–**[in]**rocblas_int specifies the increment for the elements of x.**stridex**–**[in]**rocblas_stride specifies the increment between vectors of x.**y**–**[out]**pointer storing vector y on the GPU.**incy**–**[inout]**rocblas_int specifies the increment for the elements of y.**stridey**–**[in]**rocblas_stride specifies the increment between vectors of y.**batch_count**–**[in]**rocblas_int number of instances in the batch.



The `axpy_strided_batched`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xcopy + batched, strided_batched[#](#rocblas-xcopy-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_scopy([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, float *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy)[#](#_CPPv413rocblas_scopy14rocblas_handle11rocblas_intPKf11rocblas_intPf11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dcopy([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, double *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy)[#](#_CPPv413rocblas_dcopy14rocblas_handle11rocblas_intPKd11rocblas_intPd11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ccopy([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy)[#](#_CPPv413rocblas_ccopy14rocblas_handle11rocblas_intPK21rocblas_float_complex11rocblas_intP21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zcopy([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy)[#](#_CPPv413rocblas_zcopy14rocblas_handle11rocblas_intPK22rocblas_double_complex11rocblas_intP22rocblas_double_complex11rocblas_int) **BLAS Level 1 API**copy copies each element x[i] into y[i], for i = 1 , … , n:

y := x

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**n**–**[in]**[rocblas_int] the number of elements in x to be copied to y.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of x.**y**–**[out]**device pointer storing vector y.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of y.



The `copy`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_scopy_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, float *const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_scopy_batched14rocblas_handle11rocblas_intA_PCKf11rocblas_intA_PCf11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dcopy_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, double *const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_dcopy_batched14rocblas_handle11rocblas_intA_PCKd11rocblas_intA_PCd11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ccopy_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_ccopy_batched14rocblas_handle11rocblas_intA_PCK21rocblas_float_complex11rocblas_intA_PC21rocblas_float_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zcopy_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_zcopy_batched14rocblas_handle11rocblas_intA_PCK22rocblas_double_complex11rocblas_intA_PC22rocblas_double_complex11rocblas_int11rocblas_int) **BLAS Level 1 API**copy_batched copies each element x_i[j] into y_i[j], for j = 1 , … , n; i = 1 , … , batch_count:

y_i := x_i, where (x_i, y_i) is the i-th instance of the batch. x_i and y_i are vectors.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**n**–**[in]**[rocblas_int] the number of elements in each x_i to be copied to y_i.**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each vector x_i.**y**–**[out]**device array of device pointers storing each vector y_i.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of each vector y_i.**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `copy_batched`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_scopy_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, float *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_scopy_strided_batched14rocblas_handle11rocblas_intPKf11rocblas_int14rocblas_stridePf11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dcopy_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, double *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_dcopy_strided_batched14rocblas_handle11rocblas_intPKd11rocblas_int14rocblas_stridePd11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ccopy_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_ccopy_strided_batched14rocblas_handle11rocblas_intPK21rocblas_float_complex11rocblas_int14rocblas_strideP21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zcopy_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_zcopy_strided_batched14rocblas_handle11rocblas_intPK22rocblas_double_complex11rocblas_int14rocblas_strideP22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_int) **BLAS Level 1 API**copy_strided_batched copies each element x_i[j] into y_i[j], for j = 1 , … , n; i = 1 , … , batch_count:

y_i := x_i, where (x_i, y_i) is the i-th instance of the batch. x_i and y_i are vectors.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**n**–**[in]**[rocblas_int] the number of elements in each x_i to be copied to y_i.**x**–**[in]**device pointer to the first vector (x_1) in the batch.**incx**–**[in]**[rocblas_int] specifies the increments for the elements of vectors x_i.**stridex**–**[in]**[rocblas_stride] stride from the start of one vector (x_i) and the next one (x_i+1). There are no restrictions placed on stride_x. However, the user should take care to ensure that stride_x is of appropriate size. For a typical case, this means stride_x >= n * incx.**y**–**[out]**device pointer to the first vector (y_1) in the batch.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of vectors y_i.**stridey**–**[in]**[rocblas_stride] stride from the start of one vector (y_i) and the next one (y_i+1). There are no restrictions placed on stride_y, However, ensure that stride_y is of appropriate size, for a typical case this means stride_y >= n * incy. stridey should be non zero.**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `copy_strided_batched`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xdot + batched, strided_batched[#](#rocblas-xdot-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sdot([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const float *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy, float *result)[#](#_CPPv412rocblas_sdot14rocblas_handle11rocblas_intPKf11rocblas_intPKf11rocblas_intPf)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ddot([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const double *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy, double *result)[#](#_CPPv412rocblas_ddot14rocblas_handle11rocblas_intPKd11rocblas_intPKd11rocblas_intPd)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_hdot([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_half](datatypes.html#_CPPv412rocblas_half)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_half](datatypes.html#_CPPv412rocblas_half)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_half](datatypes.html#_CPPv412rocblas_half)*result)[#](#_CPPv412rocblas_hdot14rocblas_handle11rocblas_intPK12rocblas_half11rocblas_intPK12rocblas_half11rocblas_intP12rocblas_half)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_bfdot([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_bfloat16](datatypes.html#_CPPv416rocblas_bfloat16)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_bfloat16](datatypes.html#_CPPv416rocblas_bfloat16)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_bfloat16](datatypes.html#_CPPv416rocblas_bfloat16)*result)[#](#_CPPv413rocblas_bfdot14rocblas_handle11rocblas_intPK16rocblas_bfloat1611rocblas_intPK16rocblas_bfloat1611rocblas_intP16rocblas_bfloat16)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cdotu([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*result)[#](#_CPPv413rocblas_cdotu14rocblas_handle11rocblas_intPK21rocblas_float_complex11rocblas_intPK21rocblas_float_complex11rocblas_intP21rocblas_float_complex)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cdotc([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*result)[#](#_CPPv413rocblas_cdotc14rocblas_handle11rocblas_intPK21rocblas_float_complex11rocblas_intPK21rocblas_float_complex11rocblas_intP21rocblas_float_complex)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zdotu([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*result)[#](#_CPPv413rocblas_zdotu14rocblas_handle11rocblas_intPK22rocblas_double_complex11rocblas_intPK22rocblas_double_complex11rocblas_intP22rocblas_double_complex)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zdotc([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*result)[#](#_CPPv413rocblas_zdotc14rocblas_handle11rocblas_intPK22rocblas_double_complex11rocblas_intPK22rocblas_double_complex11rocblas_intP22rocblas_double_complex) **BLAS Level 1 API**dot(u) performs the dot product of vectors x and y:

dotc performs the dot product of the conjugate of complex vector x and complex vector y.result = x * y;

result = conjugate (x) * y;

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**n**–**[in]**[rocblas_int] the number of elements in x and y.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of y.**y**–**[in]**device pointer storing vector y.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of y.**result**–**[inout]**device pointer or host pointer to store the dot product. return is 0.0 if n <= 0.



The `dot/c/u`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sdot_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const float *const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count, float *result)[#](#_CPPv420rocblas_sdot_batched14rocblas_handle11rocblas_intA_PCKf11rocblas_intA_PCKf11rocblas_int11rocblas_intPf)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ddot_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const double *const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count, double *result)[#](#_CPPv420rocblas_ddot_batched14rocblas_handle11rocblas_intA_PCKd11rocblas_intA_PCKd11rocblas_int11rocblas_intPd)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_hdot_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_half](datatypes.html#_CPPv412rocblas_half)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_half](datatypes.html#_CPPv412rocblas_half)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count,[rocblas_half](datatypes.html#_CPPv412rocblas_half)*result)[#](#_CPPv420rocblas_hdot_batched14rocblas_handle11rocblas_intA_PCK12rocblas_half11rocblas_intA_PCK12rocblas_half11rocblas_int11rocblas_intP12rocblas_half)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_bfdot_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_bfloat16](datatypes.html#_CPPv416rocblas_bfloat16)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_bfloat16](datatypes.html#_CPPv416rocblas_bfloat16)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count,[rocblas_bfloat16](datatypes.html#_CPPv416rocblas_bfloat16)*result)[#](#_CPPv421rocblas_bfdot_batched14rocblas_handle11rocblas_intA_PCK16rocblas_bfloat1611rocblas_intA_PCK16rocblas_bfloat1611rocblas_int11rocblas_intP16rocblas_bfloat16)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cdotu_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*result)[#](#_CPPv421rocblas_cdotu_batched14rocblas_handle11rocblas_intA_PCK21rocblas_float_complex11rocblas_intA_PCK21rocblas_float_complex11rocblas_int11rocblas_intP21rocblas_float_complex)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cdotc_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*result)[#](#_CPPv421rocblas_cdotc_batched14rocblas_handle11rocblas_intA_PCK21rocblas_float_complex11rocblas_intA_PCK21rocblas_float_complex11rocblas_int11rocblas_intP21rocblas_float_complex)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zdotu_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*result)[#](#_CPPv421rocblas_zdotu_batched14rocblas_handle11rocblas_intA_PCK22rocblas_double_complex11rocblas_intA_PCK22rocblas_double_complex11rocblas_int11rocblas_intP22rocblas_double_complex)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zdotc_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*result)[#](#_CPPv421rocblas_zdotc_batched14rocblas_handle11rocblas_intA_PCK22rocblas_double_complex11rocblas_intA_PCK22rocblas_double_complex11rocblas_int11rocblas_intP22rocblas_double_complex) **BLAS Level 1 API**dot_batched(u) performs a batch of dot products of vectors x and y:

dotc_batched performs a batch of dot products of the conjugate of complex vector x and complex vector yresult_i = x_i * y_i;

result_i = conjugate (x_i) * y_i; where (x_i, y_i) is the i-th instance of the batch. x_i and y_i are vectors, for i = 1, ..., batch_count.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**n**–**[in]**[rocblas_int] the number of elements in each x_i and y_i.**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i.**y**–**[in]**device array of device pointers storing each vector y_i.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of each y_i.**batch_count**–**[in]**[rocblas_int] number of instances in the batch.**result**–**[inout]**device array or host array of batch_count size to store the dot products of each batch. return 0.0 for each element if n <= 0.



The `dot/c/u_batched`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sdot_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, const float *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count, float *result)[#](#_CPPv428rocblas_sdot_strided_batched14rocblas_handle11rocblas_intPKf11rocblas_int14rocblas_stridePKf11rocblas_int14rocblas_stride11rocblas_intPf)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ddot_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, const double *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count, double *result)[#](#_CPPv428rocblas_ddot_strided_batched14rocblas_handle11rocblas_intPKd11rocblas_int14rocblas_stridePKd11rocblas_int14rocblas_stride11rocblas_intPd)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_hdot_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_half](datatypes.html#_CPPv412rocblas_half)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, const[rocblas_half](datatypes.html#_CPPv412rocblas_half)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count,[rocblas_half](datatypes.html#_CPPv412rocblas_half)*result)[#](#_CPPv428rocblas_hdot_strided_batched14rocblas_handle11rocblas_intPK12rocblas_half11rocblas_int14rocblas_stridePK12rocblas_half11rocblas_int14rocblas_stride11rocblas_intP12rocblas_half)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_bfdot_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_bfloat16](datatypes.html#_CPPv416rocblas_bfloat16)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, const[rocblas_bfloat16](datatypes.html#_CPPv416rocblas_bfloat16)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count,[rocblas_bfloat16](datatypes.html#_CPPv416rocblas_bfloat16)*result)[#](#_CPPv429rocblas_bfdot_strided_batched14rocblas_handle11rocblas_intPK16rocblas_bfloat1611rocblas_int14rocblas_stridePK16rocblas_bfloat1611rocblas_int14rocblas_stride11rocblas_intP16rocblas_bfloat16)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cdotu_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*result)[#](#_CPPv429rocblas_cdotu_strided_batched14rocblas_handle11rocblas_intPK21rocblas_float_complex11rocblas_int14rocblas_stridePK21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_intP21rocblas_float_complex)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cdotc_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*result)[#](#_CPPv429rocblas_cdotc_strided_batched14rocblas_handle11rocblas_intPK21rocblas_float_complex11rocblas_int14rocblas_stridePK21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_intP21rocblas_float_complex)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zdotu_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*result)[#](#_CPPv429rocblas_zdotu_strided_batched14rocblas_handle11rocblas_intPK22rocblas_double_complex11rocblas_int14rocblas_stridePK22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_intP22rocblas_double_complex)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zdotc_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*result)[#](#_CPPv429rocblas_zdotc_strided_batched14rocblas_handle11rocblas_intPK22rocblas_double_complex11rocblas_int14rocblas_stridePK22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_intP22rocblas_double_complex) **BLAS Level 1 API**dot_strided_batched(u) performs a batch of dot products of vectors x and y:

dotc_strided_batched performs a batch of dot products of the conjugate of complex vector x and complex vector yresult_i = x_i * y_i;

result_i = conjugate (x_i) * y_i; where (x_i, y_i) is the i-th instance of the batch. x_i and y_i are vectors, for i = 1, ..., batch_count.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**n**–**[in]**[rocblas_int] the number of elements in each x_i and y_i.**x**–**[in]**device pointer to the first vector (x_1) in the batch.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i.**stridex**–**[in]**[rocblas_stride] stride from the start of one vector (x_i) and the next one (x_i+1).**y**–**[in]**device pointer to the first vector (y_1) in the batch.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of each y_i.**stridey**–**[in]**[rocblas_stride] stride from the start of one vector (y_i) and the next one (y_i+1).**batch_count**–**[in]**[rocblas_int] number of instances in the batch.**result**–**[inout]**device array or host array of batch_count size to store the dot products of each batch. return 0.0 for each element if n <= 0.



The `dot/c/u_strided_batched`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xnrm2 + batched, strided_batched[#](#rocblas-xnrm2-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_snrm2([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, float *result)[#](#_CPPv413rocblas_snrm214rocblas_handle11rocblas_intPKf11rocblas_intPf)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dnrm2([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, double *result)[#](#_CPPv413rocblas_dnrm214rocblas_handle11rocblas_intPKd11rocblas_intPd)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_scnrm2([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, float *result)[#](#_CPPv414rocblas_scnrm214rocblas_handle11rocblas_intPK21rocblas_float_complex11rocblas_intPf)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dznrm2([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, double *result)[#](#_CPPv414rocblas_dznrm214rocblas_handle11rocblas_intPK22rocblas_double_complex11rocblas_intPd) **BLAS Level 1 API**nrm2 computes the euclidean norm of a real or complex vector:

result := sqrt( x'*x ) for real vectors result := sqrt( x**H*x ) for complex vectors

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**n**–**[in]**[rocblas_int] the number of elements in x.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of y.**result**–**[inout]**device pointer or host pointer to store the nrm2 product. return is 0.0 if n, incx<=0.



The `nrm2`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_snrm2_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count, float *results)[#](#_CPPv421rocblas_snrm2_batched14rocblas_handle11rocblas_intA_PCKf11rocblas_int11rocblas_intPf)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dnrm2_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count, double *results)[#](#_CPPv421rocblas_dnrm2_batched14rocblas_handle11rocblas_intA_PCKd11rocblas_int11rocblas_intPd)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_scnrm2_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count, float *results)[#](#_CPPv422rocblas_scnrm2_batched14rocblas_handle11rocblas_intA_PCK21rocblas_float_complex11rocblas_int11rocblas_intPf)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dznrm2_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count, double *results)[#](#_CPPv422rocblas_dznrm2_batched14rocblas_handle11rocblas_intA_PCK22rocblas_double_complex11rocblas_int11rocblas_intPd) **BLAS Level 1 API**nrm2_batched computes the euclidean norm over a batch of real or complex vectors:

result := sqrt( x_i'*x_i ) for real vectors x, for i = 1, ..., batch_count result := sqrt( x_i**H*x_i ) for complex vectors x, for i = 1, ..., batch_count

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**n**–**[in]**[rocblas_int] number of elements in each x_i.**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i. incx must be > 0.**batch_count**–**[in]**[rocblas_int] number of instances in the batch.**results**–**[out]**device pointer or host pointer to array of batch_count size for nrm2 results. return is 0.0 for each element if n <= 0, incx<=0.



The `nrm2_batched`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_snrm2_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count, float *results)[#](#_CPPv429rocblas_snrm2_strided_batched14rocblas_handle11rocblas_intPKf11rocblas_int14rocblas_stride11rocblas_intPf)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dnrm2_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count, double *results)[#](#_CPPv429rocblas_dnrm2_strided_batched14rocblas_handle11rocblas_intPKd11rocblas_int14rocblas_stride11rocblas_intPd)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_scnrm2_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count, float *results)[#](#_CPPv430rocblas_scnrm2_strided_batched14rocblas_handle11rocblas_intPK21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_intPf)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dznrm2_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count, double *results)[#](#_CPPv430rocblas_dznrm2_strided_batched14rocblas_handle11rocblas_intPK22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_intPd) **BLAS Level 1 API**nrm2_strided_batched computes the euclidean norm over a batch of real or complex vectors:

result := sqrt( x_i'*x_i ) for real vectors x, for i = 1, ..., batch_count result := sqrt( x_i**H*x_i ) for complex vectors, for i = 1, ..., batch_count

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**n**–**[in]**[rocblas_int] number of elements in each x_i.**x**–**[in]**device pointer to the first vector x_1.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i. incx must be > 0.**stridex**–**[in]**[rocblas_stride] stride from the start of one vector (x_i) and the next one (x_i+1). There are no restrictions placed on stride_x. However, ensure that stride_x is of appropriate size. For a typical case this means stride_x >= n * incx.**batch_count**–**[in]**[rocblas_int] number of instances in the batch.**results**–**[out]**device pointer or host pointer to array for storing contiguous batch_count results. return is 0.0 for each element if n <= 0, incx<=0.



The `nrm2_strided_batched`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xrot + batched, strided_batched[#](#rocblas-xrot-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_srot([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, float *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy, const float *c, const float *s)[#](#_CPPv412rocblas_srot14rocblas_handle11rocblas_intPf11rocblas_intPf11rocblas_intPKfPKf)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_drot([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, double *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy, const double *c, const double *s)[#](#_CPPv412rocblas_drot14rocblas_handle11rocblas_intPd11rocblas_intPd11rocblas_intPKdPKd)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_crot([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy, const float *c, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*s)[#](#_CPPv412rocblas_crot14rocblas_handle11rocblas_intP21rocblas_float_complex11rocblas_intP21rocblas_float_complex11rocblas_intPKfPK21rocblas_float_complex)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_csrot([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy, const float *c, const float *s)[#](#_CPPv413rocblas_csrot14rocblas_handle11rocblas_intP21rocblas_float_complex11rocblas_intP21rocblas_float_complex11rocblas_intPKfPKf)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zrot([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy, const double *c, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*s)[#](#_CPPv412rocblas_zrot14rocblas_handle11rocblas_intP22rocblas_double_complex11rocblas_intP22rocblas_double_complex11rocblas_intPKdPK22rocblas_double_complex)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zdrot([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy, const double *c, const double *s)[#](#_CPPv413rocblas_zdrot14rocblas_handle11rocblas_intP22rocblas_double_complex11rocblas_intP22rocblas_double_complex11rocblas_intPKdPKd) **BLAS Level 1 API**rot applies the Givens rotation matrix defined by c=cos(alpha) and s=sin(alpha) to vectors x and y. Scalars c and s may be stored in either host or device memory. Location is specified by calling rocblas_set_pointer_mode.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**n**–**[in]**[rocblas_int] number of elements in the x and y vectors.**x**–**[inout]**device pointer storing vector x.**incx**–**[in]**[rocblas_int] specifies the increment between elements of x.**y**–**[inout]**device pointer storing vector y.**incy**–**[in]**[rocblas_int] specifies the increment between elements of y.**c**–**[in]**device pointer or host pointer storing scalar cosine component of the rotation matrix.**s**–**[in]**device pointer or host pointer storing scalar sine component of the rotation matrix.



The `rot`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_srot_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, float *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, float *const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy, const float *c, const float *s,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv420rocblas_srot_batched14rocblas_handle11rocblas_intA_PCf11rocblas_intA_PCf11rocblas_intPKfPKf11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_drot_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, double *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, double *const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy, const double *c, const double *s,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv420rocblas_drot_batched14rocblas_handle11rocblas_intA_PCd11rocblas_intA_PCd11rocblas_intPKdPKd11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_crot_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy, const float *c, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*s,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv420rocblas_crot_batched14rocblas_handle11rocblas_intA_PC21rocblas_float_complex11rocblas_intA_PC21rocblas_float_complex11rocblas_intPKfPK21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_csrot_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy, const float *c, const float *s,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_csrot_batched14rocblas_handle11rocblas_intA_PC21rocblas_float_complex11rocblas_intA_PC21rocblas_float_complex11rocblas_intPKfPKf11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zrot_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy, const double *c, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*s,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv420rocblas_zrot_batched14rocblas_handle11rocblas_intA_PC22rocblas_double_complex11rocblas_intA_PC22rocblas_double_complex11rocblas_intPKdPK22rocblas_double_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zdrot_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy, const double *c, const double *s,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_zdrot_batched14rocblas_handle11rocblas_intA_PC22rocblas_double_complex11rocblas_intA_PC22rocblas_double_complex11rocblas_intPKdPKd11rocblas_int) **BLAS Level 1 API**rot_batched applies the Givens rotation matrix defined by c=cos(alpha) and s=sin(alpha) to batched vectors x_i and y_i, for i = 1, …, batch_count. Scalars c and s may be stored in either host or device memory. Location is specified by calling rocblas_set_pointer_mode.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**n**–**[in]**[rocblas_int] number of elements in each x_i and y_i vectors.**x**–**[inout]**device array of deivce pointers storing each vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment between elements of each x_i.**y**–**[inout]**device array of device pointers storing each vector y_i.**incy**–**[in]**[rocblas_int] specifies the increment between elements of each y_i.**c**–**[in]**device pointer or host pointer to scalar cosine component of the rotation matrix.**s**–**[in]**device pointer or host pointer to scalar sine component of the rotation matrix.**batch_count**–**[in]**[rocblas_int] the number of x and y arrays, i.e. the number of batches.



The `rot_batched`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_srot_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x, float *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_y, const float *c, const float *s,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv428rocblas_srot_strided_batched14rocblas_handle11rocblas_intPf11rocblas_int14rocblas_stridePf11rocblas_int14rocblas_stridePKfPKf11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_drot_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x, double *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_y, const double *c, const double *s,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv428rocblas_drot_strided_batched14rocblas_handle11rocblas_intPd11rocblas_int14rocblas_stridePd11rocblas_int14rocblas_stridePKdPKd11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_crot_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_y, const float *c, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*s,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv428rocblas_crot_strided_batched14rocblas_handle11rocblas_intP21rocblas_float_complex11rocblas_int14rocblas_strideP21rocblas_float_complex11rocblas_int14rocblas_stridePKfPK21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_csrot_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_y, const float *c, const float *s,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_csrot_strided_batched14rocblas_handle11rocblas_intP21rocblas_float_complex11rocblas_int14rocblas_strideP21rocblas_float_complex11rocblas_int14rocblas_stridePKfPKf11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zrot_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_y, const double *c, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*s,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv428rocblas_zrot_strided_batched14rocblas_handle11rocblas_intP22rocblas_double_complex11rocblas_int14rocblas_strideP22rocblas_double_complex11rocblas_int14rocblas_stridePKdPK22rocblas_double_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zdrot_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_y, const double *c, const double *s,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_zdrot_strided_batched14rocblas_handle11rocblas_intP22rocblas_double_complex11rocblas_int14rocblas_strideP22rocblas_double_complex11rocblas_int14rocblas_stridePKdPKd11rocblas_int) **BLAS Level 1 API**rot_strided_batched applies the Givens rotation matrix defined by c=cos(alpha) and s=sin(alpha) to strided batched vectors x_i and y_i, for i = 1, …, batch_count. Scalars c and s may be stored in either host or device memory, location is specified by calling rocblas_set_pointer_mode.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**n**–**[in]**[rocblas_int] number of elements in each x_i and y_i vectors.**x**–**[inout]**device pointer to the first vector x_1.**incx**–**[in]**[rocblas_int] specifies the increment between elements of each x_i.**stride_x**–**[in]**[rocblas_stride] specifies the increment from the beginning of x_i to the beginning of x_(i+1).**y**–**[inout]**device pointer to the first vector y_1.**incy**–**[in]**[rocblas_int] specifies the increment between elements of each y_i.**stride_y**–**[in]**[rocblas_stride] specifies the increment from the beginning of y_i to the beginning of y_(i+1)**c**–**[in]**device pointer or host pointer to scalar cosine component of the rotation matrix.**s**–**[in]**device pointer or host pointer to scalar sine component of the rotation matrix.**batch_count**–**[in]**[rocblas_int] the number of x and y arrays, i.e. the number of batches.



The `rot_strided_batched`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xrotg + batched, strided_batched[#](#rocblas-xrotg-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_srotg([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle, float *a, float *b, float *c, float *s)[#](#_CPPv413rocblas_srotg14rocblas_handlePfPfPfPf)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_drotg([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle, double *a, double *b, double *c, double *s)[#](#_CPPv413rocblas_drotg14rocblas_handlePdPdPdPd)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_crotg([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*a,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*b, float *c,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*s)[#](#_CPPv413rocblas_crotg14rocblas_handleP21rocblas_float_complexP21rocblas_float_complexPfP21rocblas_float_complex)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zrotg([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*a,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*b, double *c,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*s)[#](#_CPPv413rocblas_zrotg14rocblas_handleP22rocblas_double_complexP22rocblas_double_complexPdP22rocblas_double_complex) **BLAS Level 1 API**rotg creates the Givens rotation matrix for the vector (a b). Scalars a, b, c, and s may be stored in either host or device memory, location is specified by calling rocblas_set_pointer_mode. The computation uses the formulas

The subroutine also computessigma = sgn(a) if |a| > |b| = sgn(b) if |b| >= |a| r = sigma*sqrt( a**2 + b**2 ) c = 1; s = 0 if r = 0 c = a/r; s = b/r if r != 0

This allows c and s to be reconstructed from z as follows:z = s if |a| > |b|, = 1/c if |b| >= |a| and c != 0 = 1 if c = 0

If z = 1, set c = 0, s = 1. If |z| < 1, set c = sqrt(1 - z**2) and s = z. If |z| > 1, set c = 1/z and s = sqrt( 1 - c**2).

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**a**–**[inout]**pointer to a, an element in vector (a,b), overwritten with r.**b**–**[inout]**pointer to b, an element in vector (a,b), overwritten with z.**c**–**[out]**pointer to c, cosine element of Givens rotation.**s**–**[out]**pointer to s, sine element of Givens rotation.



The `rotg`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_srotg_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle, float *const a[], float *const b[], float *const c[], float *const s[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_srotg_batched14rocblas_handleA_PCfA_PCfA_PCfA_PCf11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_drotg_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle, double *const a[], double *const b[], double *const c[], double *const s[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_drotg_batched14rocblas_handleA_PCdA_PCdA_PCdA_PCd11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_crotg_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const a[],[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const b[], float *const c[],[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const s[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_crotg_batched14rocblas_handleA_PC21rocblas_float_complexA_PC21rocblas_float_complexA_PCfA_PC21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zrotg_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const a[],[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const b[], double *const c[],[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const s[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_zrotg_batched14rocblas_handleA_PC22rocblas_double_complexA_PC22rocblas_double_complexA_PCdA_PC22rocblas_double_complex11rocblas_int) **BLAS Level 1 API**rotg_batched creates the Givens rotation matrix for the batched vectors (a_i b_i), for i = 1, …, batch_count. a, b, c, and s are host pointers to an array of device pointers on the device, where each device pointer points to a scalar value of a_i, b_i, c_i, or s_i.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**a**–**[inout]**a, overwritten with r.**b**–**[inout]**b overwritten with z.**c**–**[out]**cosine element of Givens rotation for the batch.**s**–**[out]**sine element of Givens rotation for the batch.**batch_count**–**[in]**[rocblas_int] number of batches (length of arrays a, b, c, and s).



The `rotg_batched`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_srotg_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle, float *a,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_a, float *b,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_b, float *c,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_c, float *s,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_s,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_srotg_strided_batched14rocblas_handlePf14rocblas_stridePf14rocblas_stridePf14rocblas_stridePf14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_drotg_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle, double *a,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_a, double *b,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_b, double *c,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_c, double *s,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_s,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_drotg_strided_batched14rocblas_handlePd14rocblas_stridePd14rocblas_stridePd14rocblas_stridePd14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_crotg_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*a,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_a,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*b,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_b, float *c,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_c,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*s,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_s,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_crotg_strided_batched14rocblas_handleP21rocblas_float_complex14rocblas_strideP21rocblas_float_complex14rocblas_stridePf14rocblas_strideP21rocblas_float_complex14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zrotg_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*a,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_a,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*b,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_b, double *c,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_c,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*s,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_s,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_zrotg_strided_batched14rocblas_handleP22rocblas_double_complex14rocblas_strideP22rocblas_double_complex14rocblas_stridePd14rocblas_strideP22rocblas_double_complex14rocblas_stride11rocblas_int) **BLAS Level 1 API**rotg_strided_batched creates the Givens rotation matrix for the strided batched vectors (a_i b_i), for i = 1, …, batch_count. a, b, c, and s are host pointers to arrays a, b, c, s on the device.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**a**–**[inout]**host pointer to first single input vector element a_1 on the device, overwritten with r.**stride_a**–**[in]**[rocblas_stride] distance between elements of a in batch (distance between a_i and a_(i + 1)).**b**–**[inout]**host pointer to first single input vector element b_1 on the device, overwritten with z.**stride_b**–**[in]**[rocblas_stride] distance between elements of b in batch (distance between b_i and b_(i + 1)).**c**–**[out]**host pointer to first single cosine element of Givens rotations c_1 on the device.**stride_c**–**[in]**[rocblas_stride] distance between elements of c in batch (distance between c_i and c_(i + 1)).**s**–**[out]**host pointer to first single sine element of Givens rotations s_1 on the device.**stride_s**–**[in]**[rocblas_stride] distance between elements of s in batch (distance between s_i and s_(i + 1)).**batch_count**–**[in]**[rocblas_int] number of batches (length of arrays a, b, c, and s).



The `rotg_strided_batched`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xrotm + batched, strided_batched[#](#rocblas-xrotm-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_srotm([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, float *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy, const float *param)[#](#_CPPv413rocblas_srotm14rocblas_handle11rocblas_intPf11rocblas_intPf11rocblas_intPKf)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_drotm([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, double *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy, const double *param)[#](#_CPPv413rocblas_drotm14rocblas_handle11rocblas_intPd11rocblas_intPd11rocblas_intPKd) **BLAS Level 1 API**rotm applies the modified Givens rotation matrix defined by param to vectors x and y.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**n**–**[in]**[rocblas_int] number of elements in the x and y vectors.**x**–**[inout]**device pointer storing vector x.**incx**–**[in]**[rocblas_int] specifies the increment between elements of x.**y**–**[inout]**device pointer storing vector y.**incy**–**[in]**[rocblas_int] specifies the increment between elements of y.**param**–**[in]**device vector or host vector of 5 elements defining the rotation.param[0] = flag param[1] = H11 param[2] = H21 param[3] = H12 param[4] = H22 The flag parameter defines the form of H: flag = -1 => H = ( H11 H12 H21 H22 ) flag = 0 => H = ( 1.0 H12 H21 1.0 ) flag = 1 => H = ( H11 1.0 -1.0 H22 ) flag = -2 => H = ( 1.0 0.0 0.0 1.0 ) param may be stored in either host or device memory, location is specified by calling rocblas_set_pointer_mode.




The `rotm`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_srotm_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, float *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, float *const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy, const float *const param[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_srotm_batched14rocblas_handle11rocblas_intA_PCf11rocblas_intA_PCf11rocblas_intA_PCKf11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_drotm_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, double *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, double *const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy, const double *const param[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_drotm_batched14rocblas_handle11rocblas_intA_PCd11rocblas_intA_PCd11rocblas_intA_PCKd11rocblas_int) **BLAS Level 1 API**rotm_batched applies the modified Givens rotation matrix defined by param_i to batched vectors x_i and y_i, for i = 1, …, batch_count.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**n**–**[in]**[rocblas_int] number of elements in the x and y vectors.**x**–**[inout]**device array of device pointers storing each vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment between elements of each x_i.**y**–**[inout]**device array of device pointers storing each vector y_1.**incy**–**[in]**[rocblas_int] specifies the increment between elements of each y_i.**param**–**[in]**device array of device vectors of 5 elements defining the rotation.param[0] = flag param[1] = H11 param[2] = H21 param[3] = H12 param[4] = H22 The flag parameter defines the form of H: flag = -1 => H = ( H11 H12 H21 H22 ) flag = 0 => H = ( 1.0 H12 H21 1.0 ) flag = 1 => H = ( H11 1.0 -1.0 H22 ) flag = -2 => H = ( 1.0 0.0 0.0 1.0 ) param may ONLY be stored on the device for the batched version of this function.

**batch_count**–**[in]**[rocblas_int] the number of x and y arrays, i.e. the number of batches.



The `rotm_batched`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_srotm_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x, float *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_y, const float *param,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_param,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_srotm_strided_batched14rocblas_handle11rocblas_intPf11rocblas_int14rocblas_stridePf11rocblas_int14rocblas_stridePKf14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_drotm_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x, double *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_y, const double *param,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_param,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_drotm_strided_batched14rocblas_handle11rocblas_intPd11rocblas_int14rocblas_stridePd11rocblas_int14rocblas_stridePKd14rocblas_stride11rocblas_int) **BLAS Level 1 API**rotm_strided_batched applies the modified Givens rotation matrix defined by param_i to strided batched vectors x_i and y_i, for i = 1, …, batch_count

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**n**–**[in]**[rocblas_int] number of elements in the x and y vectors.**x**–**[inout]**device pointer pointing to first strided batched vector x_1.**incx**–**[in]**[rocblas_int] specifies the increment between elements of each x_i.**stride_x**–**[in]**[rocblas_stride] specifies the increment between the beginning of x_i and x_(i + 1)**y**–**[inout]**device pointer pointing to first strided batched vector y_1.**incy**–**[in]**[rocblas_int] specifies the increment between elements of each y_i.**stride_y**–**[in]**[rocblas_stride] specifies the increment between the beginning of y_i and y_(i + 1).**param**–**[in]**device pointer pointing to first array of 5 elements defining the rotation (param_1).param[0] = flag param[1] = H11 param[2] = H21 param[3] = H12 param[4] = H22 The flag parameter defines the form of H: flag = -1 => H = ( H11 H12 H21 H22 ) flag = 0 => H = ( 1.0 H12 H21 1.0 ) flag = 1 => H = ( H11 1.0 -1.0 H22 ) flag = -2 => H = ( 1.0 0.0 0.0 1.0 ) param may ONLY be stored on the device for the strided_batched version of this function.

**stride_param**–**[in]**[rocblas_stride] specifies the increment between the beginning of param_i and param_(i + 1).**batch_count**–**[in]**[rocblas_int] the number of x and y arrays, i.e. the number of batches.



The `rotm_strided_batched`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xrotmg + batched, strided_batched[#](#rocblas-xrotmg-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_srotmg([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle, float *d1, float *d2, float *x1, const float *y1, float *param)[#](#_CPPv414rocblas_srotmg14rocblas_handlePfPfPfPKfPf)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_drotmg([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle, double *d1, double *d2, double *x1, const double *y1, double *param)[#](#_CPPv414rocblas_drotmg14rocblas_handlePdPdPdPKdPd) **BLAS Level 1 API**rotmg creates the modified Givens rotation matrix for the vector (d1 * x1, d2 * y1). Parameters may be stored in either host or device memory. Location is specified by calling rocblas_set_pointer_mode:

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**d1**–**[inout]**device pointer or host pointer to input scalar that is overwritten.**d2**–**[inout]**device pointer or host pointer to input scalar that is overwritten.**x1**–**[inout]**device pointer or host pointer to input scalar that is overwritten.**y1**–**[in]**device pointer or host pointer to input scalar.**param**–**[out]**device vector or host vector of five elements defining the rotation.param[0] = flag param[1] = H11 param[2] = H21 param[3] = H12 param[4] = H22 The flag parameter defines the form of H: flag = -1 => H = ( H11 H12 H21 H22 ) flag = 0 => H = ( 1.0 H12 H21 1.0 ) flag = 1 => H = ( H11 1.0 -1.0 H22 ) flag = -2 => H = ( 1.0 0.0 0.0 1.0 ) param may be stored in either host or device memory. Location is specified by calling rocblas_set_pointer_mode.




The `rotmg`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_srotmg_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle, float *const d1[], float *const d2[], float *const x1[], const float *const y1[], float *const param[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv422rocblas_srotmg_batched14rocblas_handleA_PCfA_PCfA_PCfA_PCKfA_PCf11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_drotmg_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle, double *const d1[], double *const d2[], double *const x1[], const double *const y1[], double *const param[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv422rocblas_drotmg_batched14rocblas_handleA_PCdA_PCdA_PCdA_PCKdA_PCd11rocblas_int) **BLAS Level 1 API**rotmg_batched creates the modified Givens rotation matrix for the batched vectors (d1_i * x1_i, d2_i * y1_i), for i = 1, …, batch_count. Parameters may be stored in either host or device memory. Location is specified by calling rocblas_set_pointer_mode:

If the pointer mode is set to rocblas_pointer_mode_host, then this function blocks the CPU until the GPU has finished and the results are available in host memory.

If the pointer mode is set to rocblas_pointer_mode_device, then this function returns immediately and synchronization is required to read the results.


- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**d1**–**[inout]**device batched array or host batched array of input scalars that is overwritten.**d2**–**[inout]**device batched array or host batched array of input scalars that is overwritten.**x1**–**[inout]**device batched array or host batched array of input scalars that is overwritten.**y1**–**[in]**device batched array or host batched array of input scalars.**param**–**[out]**device batched array or host batched array of vectors of 5 elements defining the rotation.param[0] = flag param[1] = H11 param[2] = H21 param[3] = H12 param[4] = H22 The flag parameter defines the form of H: flag = -1 => H = ( H11 H12 H21 H22 ) flag = 0 => H = ( 1.0 H12 H21 1.0 ) flag = 1 => H = ( H11 1.0 -1.0 H22 ) flag = -2 => H = ( 1.0 0.0 0.0 1.0 ) param may be stored in either host or device memory. Location is specified by calling rocblas_set_pointer_mode.

**batch_count**–**[in]**[rocblas_int] the number of instances in the batch.



The `rotmg_batched`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_srotmg_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle, float *d1,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_d1, float *d2,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_d2, float *x1,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x1, const float *y1,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_y1, float *param,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_param,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv430rocblas_srotmg_strided_batched14rocblas_handlePf14rocblas_stridePf14rocblas_stridePf14rocblas_stridePKf14rocblas_stridePf14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_drotmg_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle, double *d1,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_d1, double *d2,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_d2, double *x1,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x1, const double *y1,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_y1, double *param,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_param,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv430rocblas_drotmg_strided_batched14rocblas_handlePd14rocblas_stridePd14rocblas_stridePd14rocblas_stridePKd14rocblas_stridePd14rocblas_stride11rocblas_int) **BLAS Level 1 API**rotmg_strided_batched creates the modified Givens rotation matrix for the strided batched vectors (d1_i * x1_i, d2_i * y1_i), for i = 1, …, batch_count. Parameters may be stored in either host or device memory. Location is specified by calling rocblas_set_pointer_mode:

If the pointer mode is set to rocblas_pointer_mode_host, then this function blocks the CPU until the GPU has finished and the results are available in host memory.

If the pointer mode is set to rocblas_pointer_mode_device, then this function returns immediately and synchronization is required to read the results.


- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**d1**–**[inout]**device strided_batched array or host strided_batched array of input scalars that is overwritten.**stride_d1**–**[in]**[rocblas_stride] specifies the increment between the beginning of d1_i and d1_(i+1).**d2**–**[inout]**device strided_batched array or host strided_batched array of input scalars that is overwritten.**stride_d2**–**[in]**[rocblas_stride] specifies the increment between the beginning of d2_i and d2_(i+1).**x1**–**[inout]**device strided_batched array or host strided_batched array of input scalars that is overwritten.**stride_x1**–**[in]**[rocblas_stride] specifies the increment between the beginning of x1_i and x1_(i+1).**y1**–**[in]**device strided_batched array or host strided_batched array of input scalars.**stride_y1**–**[in]**[rocblas_stride] specifies the increment between the beginning of y1_i and y1_(i+1).**param**–**[out]**device strided_batched array or host strided_batched array of vectors of 5 elements defining the rotation.param[0] = flag param[1] = H11 param[2] = H21 param[3] = H12 param[4] = H22 The flag parameter defines the form of H: flag = -1 => H = ( H11 H12 H21 H22 ) flag = 0 => H = ( 1.0 H12 H21 1.0 ) flag = 1 => H = ( H11 1.0 -1.0 H22 ) flag = -2 => H = ( 1.0 0.0 0.0 1.0 ) param may be stored in either host or device memory. Location is specified by calling rocblas_set_pointer_mode.

**stride_param**–**[in]**[rocblas_stride] specifies the increment between the beginning of param_i and param_(i + 1).**batch_count**–**[in]**[rocblas_int] the number of instances in the batch.



The `rotmg_strided_batched`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xscal + batched, strided_batched[#](#rocblas-xscal-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sscal([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx)[#](#_CPPv413rocblas_sscal14rocblas_handle11rocblas_intPKfPf11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dscal([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx)[#](#_CPPv413rocblas_dscal14rocblas_handle11rocblas_intPKdPd11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cscal([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx)[#](#_CPPv413rocblas_cscal14rocblas_handle11rocblas_intPK21rocblas_float_complexP21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zscal([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx)[#](#_CPPv413rocblas_zscal14rocblas_handle11rocblas_intPK22rocblas_double_complexP22rocblas_double_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_csscal([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx)[#](#_CPPv414rocblas_csscal14rocblas_handle11rocblas_intPKfP21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zdscal([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx)[#](#_CPPv414rocblas_zdscal14rocblas_handle11rocblas_intPKdP22rocblas_double_complex11rocblas_int) **BLAS Level 1 API**scal scales each element of vector x with scalar alpha:

x := alpha * x

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**n**–**[in]**[rocblas_int] the number of elements in x.**alpha**–**[in]**device pointer or host pointer for the scalar alpha.**x**–**[inout]**device pointer storing vector x.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of x.



The `scal`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sscal_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, float *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_sscal_batched14rocblas_handle11rocblas_intPKfA_PCf11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dscal_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, double *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_dscal_batched14rocblas_handle11rocblas_intPKdA_PCd11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cscal_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_cscal_batched14rocblas_handle11rocblas_intPK21rocblas_float_complexA_PC21rocblas_float_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zscal_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_zscal_batched14rocblas_handle11rocblas_intPK22rocblas_double_complexA_PC22rocblas_double_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_csscal_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv422rocblas_csscal_batched14rocblas_handle11rocblas_intPKfA_PC21rocblas_float_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zdscal_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv422rocblas_zdscal_batched14rocblas_handle11rocblas_intPKdA_PC22rocblas_double_complex11rocblas_int11rocblas_int) **BLAS Level 1 API**scal_batched scales each element of vector x_i with scalar alpha, for i = 1, … , batch_count:

x_i := alpha * x_i, where (x_i) is the i-th instance of the batch.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**n**–**[in]**[rocblas_int] the number of elements in each x_i.**alpha**–**[in]**host pointer or device pointer for the scalar alpha.**x**–**[inout]**device array of device pointers storing each vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i.**batch_count**–**[in]**[rocblas_int] specifies the number of batches in x.



The `scal_batched`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sscal_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_sscal_strided_batched14rocblas_handle11rocblas_intPKfPf11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dscal_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_dscal_strided_batched14rocblas_handle11rocblas_intPKdPd11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cscal_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_cscal_strided_batched14rocblas_handle11rocblas_intPK21rocblas_float_complexP21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zscal_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_zscal_strided_batched14rocblas_handle11rocblas_intPK22rocblas_double_complexP22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_csscal_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv430rocblas_csscal_strided_batched14rocblas_handle11rocblas_intPKfP21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zdscal_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv430rocblas_zdscal_strided_batched14rocblas_handle11rocblas_intPKdP22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_int) **BLAS Level 1 API**scal_strided_batched scales each element of vector x_i with scalar alpha, for i = 1, … , batch_count:

x_i := alpha * x_i, where (x_i) is the i-th instance of the batch.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**n**–**[in]**[rocblas_int] the number of elements in each x_i.**alpha**–**[in]**host pointer or device pointer for the scalar alpha.**x**–**[inout]**device pointer to the first vector (x_1) in the batch.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of x.**stride_x**–**[in]**[rocblas_stride] stride from the start of one vector (x_i) and the next one (x_i+1). There are no restrictions placed on stride_x. However, ensure that stride_x is of appropriate size, for a typical case this means stride_x >= n * incx.**batch_count**–**[in]**[rocblas_int] specifies the number of batches in x.



The `scal_strided_batched`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xswap + batched, strided_batched[#](#rocblas-xswap-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sswap([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, float *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy)[#](#_CPPv413rocblas_sswap14rocblas_handle11rocblas_intPf11rocblas_intPf11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dswap([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, double *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy)[#](#_CPPv413rocblas_dswap14rocblas_handle11rocblas_intPd11rocblas_intPd11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cswap([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy)[#](#_CPPv413rocblas_cswap14rocblas_handle11rocblas_intP21rocblas_float_complex11rocblas_intP21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zswap([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy)[#](#_CPPv413rocblas_zswap14rocblas_handle11rocblas_intP22rocblas_double_complex11rocblas_intP22rocblas_double_complex11rocblas_int) **BLAS Level 1 API**swap interchanges vectors x and y:

y := x; x := y

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**n**–**[in]**[rocblas_int] the number of elements in x and y.**x**–**[inout]**device pointer storing vector x.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of x.**y**–**[inout]**device pointer storing vector y.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of y.



The `swap`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sswap_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, float *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, float *const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_sswap_batched14rocblas_handle11rocblas_intA_PCf11rocblas_intA_PCf11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dswap_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, double *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, double *const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_dswap_batched14rocblas_handle11rocblas_intA_PCd11rocblas_intA_PCd11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cswap_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_cswap_batched14rocblas_handle11rocblas_intA_PC21rocblas_float_complex11rocblas_intA_PC21rocblas_float_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zswap_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const y[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_zswap_batched14rocblas_handle11rocblas_intA_PC22rocblas_double_complex11rocblas_intA_PC22rocblas_double_complex11rocblas_int11rocblas_int) **BLAS Level 1 API**swap_batched interchanges vectors x_i and y_i, for i = 1 , … , batch_count:

y_i := x_i; x_i := y_i

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**n**–**[in]**[rocblas_int] the number of elements in each x_i and y_i.**x**–**[inout]**device array of device pointers storing each vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i.**y**–**[inout]**device array of device pointers storing each vector y_i.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of each y_i.**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `swap_batched`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sswap_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, float *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_sswap_strided_batched14rocblas_handle11rocblas_intPf11rocblas_int14rocblas_stridePf11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dswap_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, double *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_dswap_strided_batched14rocblas_handle11rocblas_intPd11rocblas_int14rocblas_stridePd11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cswap_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_cswap_strided_batched14rocblas_handle11rocblas_intP21rocblas_float_complex11rocblas_int14rocblas_strideP21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zswap_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_zswap_strided_batched14rocblas_handle11rocblas_intP22rocblas_double_complex11rocblas_int14rocblas_strideP22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_int) **BLAS Level 1 API**swap_strided_batched interchanges vectors x_i and y_i, for i = 1 , … , batch_count:

y_i := x_i; x_i := y_i

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**n**–**[in]**[rocblas_int] the number of elements in each x_i and y_i.**x**–**[inout]**device pointer to the first vector x_1.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of x.**stridex**–**[in]**[rocblas_stride] stride from the start of one vector (x_i) and the next one (x_i+1). There are no restrictions placed on stride_x. However, ensure that stride_x is of appropriate size. For a typical case this means stride_x >= n * incx.**y**–**[inout]**device pointer to the first vector y_1.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of y.**stridey**–**[in]**[rocblas_stride] stride from the start of one vector (y_i) and the next one (y_i+1). There are no restrictions placed on stride_x. However, ensure that stride_y is of appropriate size. For a typical case this means stride_y >= n * incy. stridey should be non zero.**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `swap_strided_batched`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.
