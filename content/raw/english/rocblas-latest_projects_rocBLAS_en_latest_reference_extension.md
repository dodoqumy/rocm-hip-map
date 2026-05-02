---
title: "rocBLAS extension &#8212; rocBLAS 5.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/extension.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:05:15.793699+00:00
content_hash: "c18043555df29d9f"
---

# rocBLAS extension[#](#rocblas-extension)

Level-1 Extension functions support the ILP64 API. For more information on these `_64`

functions, see the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_axpy_ex + batched, strided_batched[#](#rocblas-axpy-ex-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_axpy_ex([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const void *alpha,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)alpha_type, const void *x,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)x_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, void *y,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)y_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)execution_type)[#](#_CPPv415rocblas_axpy_ex14rocblas_handle11rocblas_intPKv16rocblas_datatypePKv16rocblas_datatype11rocblas_intPv16rocblas_datatype11rocblas_int16rocblas_datatype)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_axpy_batched_ex([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const void *alpha,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)alpha_type, const void *x,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)x_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, void *y,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)y_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)execution_type)[#](#_CPPv423rocblas_axpy_batched_ex14rocblas_handle11rocblas_intPKv16rocblas_datatypePKv16rocblas_datatype11rocblas_intPv16rocblas_datatype11rocblas_int11rocblas_int16rocblas_datatype)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_axpy_strided_batched_ex([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const void *alpha,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)alpha_type, const void *x,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)x_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex, void *y,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)y_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridey,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)execution_type)[#](#_CPPv431rocblas_axpy_strided_batched_ex14rocblas_handle11rocblas_intPKv16rocblas_datatypePKv16rocblas_datatype11rocblas_int14rocblas_stridePv16rocblas_datatype11rocblas_int14rocblas_stride11rocblas_int16rocblas_datatype) **BLAS EX API**axpy_strided_batched_ex computes constant alpha multiplied by vector x, plus vector y over a set of strided batched vectors.

Currently supported datatypes are as follows:y := alpha * x + y

alpha_type

x_type

y_type

execution_type

bf16_r

bf16_r

bf16_r

f32_r

f32_r

bf16_r

bf16_r

f32_r

f16_r

f16_r

f16_r

f16_r

f16_r

f16_r

f16_r

f32_r

f32_r

f16_r

f16_r

f32_r

f32_r

f32_r

f32_r

f32_r

f64_r

f64_r

f64_r

f64_r

f32_c

f32_c

f32_c

f32_c

f64_c

f64_c

f64_c

f64_c

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**n**–**[in]**[rocblas_int] the number of elements in each x_i and y_i.**alpha**–**[in]**device pointer or host pointer to specify the scalar alpha.**alpha_type**–**[in]**[rocblas_datatype] specifies the datatype of alpha.**x**–**[in]**device pointer to the first vector x_1.**x_type**–**[in]**[rocblas_datatype] specifies the datatype of each vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i.**stridex**–**[in]**[rocblas_stride] stride from the start of one vector (x_i) to the next one (x_i+1). There are no restrictions placed on stridex. However, ensure that stridex is of appropriate size. For a typical case this means stridex >= n * incx.**y**–**[inout]**device pointer to the first vector y_1.**y_type**–**[in]**[rocblas_datatype] specifies the datatype of each vector y_i.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of each y_i.**stridey**–**[in]**[rocblas_stride] stride from the start of one vector (y_i) to the next one (y_i+1). There are no restrictions placed on stridey. However, ensure that stridey is of appropriate size. For a typical case this means stridey >= n * incy.**batch_count**–**[in]**[rocblas_int] number of instances in the batch.**execution_type**–**[in]**[rocblas_datatype] specifies the datatype of computation.



`axpy_ex`

, `axpy_batched_ex`

, and `axpy_strided_batched_ex functions`

support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_dot_ex + batched, strided_batched[#](#rocblas-dot-ex-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dot_ex([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const void *x,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)x_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const void *y,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)y_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy, void *result,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)result_type,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)execution_type)[#](#_CPPv414rocblas_dot_ex14rocblas_handle11rocblas_intPKv16rocblas_datatype11rocblas_intPKv16rocblas_datatype11rocblas_intPv16rocblas_datatype16rocblas_datatype)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dot_batched_ex([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const void *x,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)x_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const void *y,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)y_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count, void *result,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)result_type,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)execution_type)[#](#_CPPv422rocblas_dot_batched_ex14rocblas_handle11rocblas_intPKv16rocblas_datatype11rocblas_intPKv16rocblas_datatype11rocblas_int11rocblas_intPv16rocblas_datatype16rocblas_datatype)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dot_strided_batched_ex([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const void *x,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)x_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x, const void *y,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)y_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count, void *result,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)result_type,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)execution_type)[#](#_CPPv430rocblas_dot_strided_batched_ex14rocblas_handle11rocblas_intPKv16rocblas_datatype11rocblas_int14rocblas_stridePKv16rocblas_datatype11rocblas_int14rocblas_stride11rocblas_intPv16rocblas_datatype16rocblas_datatype) **BLAS EX API**dot_strided_batched_ex performs a batch of dot products of vectors x and y.

dotc_strided_batched_ex performs a batch of dot products of the conjugate of complex vector x and complex vector yresult_i = x_i * y_i;

where (x_i, y_i) is the i-th instance of the batch. x_i and y_i are vectors, for i = 1, …, batch_countresult_i = conjugate (x_i) * y_i;

Currently supported datatypes are as follows:

x_type

y_type

result_type

execution_type

f16_r

f16_r

f16_r

f16_r

f16_r

f16_r

f16_r

f32_r

bf16_r

bf16_r

bf16_r

f32_r

f32_r

f32_r

f32_r

f32_r

f32_r

f32_r

f64_r

f64_r

f64_r

f64_r

f64_r

f64_r

f32_c

f32_c

f32_c

f32_c

f64_c

f64_c

f64_c

f64_c

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**n**–**[in]**[rocblas_int] the number of elements in each x_i and y_i.**x**–**[in]**device pointer to the first vector (x_1) in the batch.**x_type**–**[in]**[rocblas_datatype] specifies the datatype of each vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i.**stride_x**–**[in]**[rocblas_stride] stride from the start of one vector (x_i) and the next one (x_i+1)**y**–**[in]**device pointer to the first vector (y_1) in the batch.**y_type**–**[in]**[rocblas_datatype] specifies the datatype of each vector y_i.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of each y_i.**stride_y**–**[in]**[rocblas_stride] stride from the start of one vector (y_i) and the next one (y_i+1)**batch_count**–**[in]**[rocblas_int] number of instances in the batch.**result**–**[inout]**device array or host array of batch_count size to store the dot products of each batch. return 0.0 for each element if n <= 0.**result_type**–**[in]**[rocblas_datatype] specifies the datatype of the result.**execution_type**–**[in]**[rocblas_datatype] specifies the datatype of computation.



`dot_ex`

, `dot_batched_ex`

, and `dot_strided_batched_ex`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_dotc_ex + batched, strided_batched[#](#rocblas-dotc-ex-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dotc_ex([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const void *x,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)x_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const void *y,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)y_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy, void *result,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)result_type,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)execution_type)[#](#_CPPv415rocblas_dotc_ex14rocblas_handle11rocblas_intPKv16rocblas_datatype11rocblas_intPKv16rocblas_datatype11rocblas_intPv16rocblas_datatype16rocblas_datatype)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dotc_batched_ex([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const void *x,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)x_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, const void *y,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)y_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count, void *result,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)result_type,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)execution_type)[#](#_CPPv423rocblas_dotc_batched_ex14rocblas_handle11rocblas_intPKv16rocblas_datatype11rocblas_intPKv16rocblas_datatype11rocblas_int11rocblas_intPv16rocblas_datatype16rocblas_datatype)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dotc_strided_batched_ex([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const void *x,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)x_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x, const void *y,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)y_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count, void *result,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)result_type,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)execution_type)[#](#_CPPv431rocblas_dotc_strided_batched_ex14rocblas_handle11rocblas_intPKv16rocblas_datatype11rocblas_int14rocblas_stridePKv16rocblas_datatype11rocblas_int14rocblas_stride11rocblas_intPv16rocblas_datatype16rocblas_datatype) **BLAS EX API**dot_strided_batched_ex performs a batch of dot products of vectors x and y.

dotc_strided_batched_ex performs a batch of dot products of the conjugate of complex vector x and complex vector yresult_i = x_i * y_i;

where (x_i, y_i) is the i-th instance of the batch. x_i and y_i are vectors, for i = 1, …, batch_countresult_i = conjugate (x_i) * y_i;

Currently supported datatypes are as follows:

x_type

y_type

result_type

execution_type

f16_r

f16_r

f16_r

f16_r

f16_r

f16_r

f16_r

f32_r

bf16_r

bf16_r

bf16_r

f32_r

f32_r

f32_r

f32_r

f32_r

f32_r

f32_r

f64_r

f64_r

f64_r

f64_r

f64_r

f64_r

f32_c

f32_c

f32_c

f32_c

f64_c

f64_c

f64_c

f64_c

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**n**–**[in]**[rocblas_int] the number of elements in each x_i and y_i.**x**–**[in]**device pointer to the first vector (x_1) in the batch.**x_type**–**[in]**[rocblas_datatype] specifies the datatype of each vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i.**stride_x**–**[in]**[rocblas_stride] stride from the start of one vector (x_i) and the next one (x_i+1)**y**–**[in]**device pointer to the first vector (y_1) in the batch.**y_type**–**[in]**[rocblas_datatype] specifies the datatype of each vector y_i.**incy**–**[in]**[rocblas_int] specifies the increment for the elements of each y_i.**stride_y**–**[in]**[rocblas_stride] stride from the start of one vector (y_i) and the next one (y_i+1)**batch_count**–**[in]**[rocblas_int] number of instances in the batch.**result**–**[inout]**device array or host array of batch_count size to store the dot products of each batch. return 0.0 for each element if n <= 0.**result_type**–**[in]**[rocblas_datatype] specifies the datatype of the result.**execution_type**–**[in]**[rocblas_datatype] specifies the datatype of computation.



`dotc_ex`

, `dotc_batched_ex`

, and `dotc_strided_batched_ex`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_nrm2_ex + batched, strided_batched[#](#rocblas-nrm2-ex-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_nrm2_ex([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const void *x,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)x_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, void *results,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)result_type,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)execution_type)[#](#_CPPv415rocblas_nrm2_ex14rocblas_handle11rocblas_intPKv16rocblas_datatype11rocblas_intPv16rocblas_datatype16rocblas_datatype)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_nrm2_batched_ex([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const void *x,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)x_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count, void *results,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)result_type,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)execution_type)[#](#_CPPv423rocblas_nrm2_batched_ex14rocblas_handle11rocblas_intPKv16rocblas_datatype11rocblas_int11rocblas_intPv16rocblas_datatype16rocblas_datatype)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_nrm2_strided_batched_ex([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const void *x,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)x_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count, void *results,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)result_type,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)execution_type)[#](#_CPPv431rocblas_nrm2_strided_batched_ex14rocblas_handle11rocblas_intPKv16rocblas_datatype11rocblas_int14rocblas_stride11rocblas_intPv16rocblas_datatype16rocblas_datatype) BLAS_EX API.

nrm2_strided_batched_ex computes the euclidean norm over a batch of real or complex vectors.

Currently supported datatypes are as follows:result := sqrt( x_i'*x_i ) for real vectors x, for i = 1, ..., batch_count result := sqrt( x_i**H*x_i ) for complex vectors, for i = 1, ..., batch_count

x_type

result

execution_type

bf16_r

bf16_r

f32_r

f16_r

f16_r

f32_r

f32_r

f32_r

f32_r

f64_r

f64_r

f64_r

f32_c

f32_r

f32_r

f64_c

f64_r

f64_r

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**n**–**[in]**[rocblas_int] number of elements in each x_i.**x**–**[in]**device pointer to the first vector x_1.**x_type**–**[in]**[rocblas_datatype] specifies the datatype of each vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i. incx must be > 0.**stride_x**–**[in]**[rocblas_stride] stride from the start of one vector (x_i) and the next one (x_i+1). There are no restrictions placed on stride_x. However, ensure that stride_x is of appropriate size. For a typical case this means stride_x >= n * incx.**batch_count**–**[in]**[rocblas_int] number of instances in the batch.**results**–**[out]**device pointer or host pointer to array for storing contiguous batch_count results. return is 0.0 for each element if n <= 0, incx<=0.**result_type**–**[in]**[rocblas_datatype] specifies the datatype of the result.**execution_type**–**[in]**[rocblas_datatype] specifies the datatype of computation.



`nrm2_ex`

, `nrm2_batched_ex`

, and `nrm2_strided_batched_ex`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_rot_ex + batched, strided_batched[#](#rocblas-rot-ex-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_rot_ex([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, void *x,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)x_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, void *y,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)y_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy, const void *c, const void *s,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)cs_type,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)execution_type)[#](#_CPPv414rocblas_rot_ex14rocblas_handle11rocblas_intPv16rocblas_datatype11rocblas_intPv16rocblas_datatype11rocblas_intPKvPKv16rocblas_datatype16rocblas_datatype)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_rot_batched_ex([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, void *x,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)x_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, void *y,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)y_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy, const void *c, const void *s,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)cs_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)execution_type)[#](#_CPPv422rocblas_rot_batched_ex14rocblas_handle11rocblas_intPv16rocblas_datatype11rocblas_intPv16rocblas_datatype11rocblas_intPKvPKv16rocblas_datatype11rocblas_int16rocblas_datatype)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_rot_strided_batched_ex([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, void *x,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)x_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x, void *y,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)y_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_y, const void *c, const void *s,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)cs_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)execution_type)[#](#_CPPv430rocblas_rot_strided_batched_ex14rocblas_handle11rocblas_intPv16rocblas_datatype11rocblas_int14rocblas_stridePv16rocblas_datatype11rocblas_int14rocblas_stridePKvPKv16rocblas_datatype11rocblas_int16rocblas_datatype) **BLAS Level 1 API**rot_strided_batched_ex applies the Givens rotation matrix defined by c=cos(alpha) and s=sin(alpha) to strided batched vectors x_i and y_i, for i = 1, …, batch_count. Scalars c and s may be stored in either host or device memory. Location is specified by calling rocblas_set_pointer_mode.

In the case where cs_type is real:

In the case where cs_type is complex, the imaginary part of c is ignored:x := c * x + s * y y := c * y - s * x

Currently supported datatypes are as follows:x := real(c) * x + s * y y := real(c) * y - conj(s) * x

x_type

y_type

cs_type

execution_type

bf16_r

bf16_r

bf16_r

f32_r

f16_r

f16_r

f16_r

f32_r

f32_r

f32_r

f32_r

f32_r

f64_r

f64_r

f64_r

f64_r

f32_c

f32_c

f32_c

f32_c

f32_c

f32_c

f32_r

f32_c

f64_c

f64_c

f64_c

f64_c

f64_c

f64_c

f64_r

f64_c

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**n**–**[in]**[rocblas_int] number of elements in each x_i and y_i vectors.**x**–**[inout]**device pointer to the first vector x_1.**x_type**–**[in]**[rocblas_datatype] specifies the datatype of each vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment between elements of each x_i.**stride_x**–**[in]**[rocblas_stride] specifies the increment from the beginning of x_i to the beginning of x_(i+1)**y**–**[inout]**device pointer to the first vector y_1.**y_type**–**[in]**[rocblas_datatype] specifies the datatype of each vector y_i.**incy**–**[in]**[rocblas_int] specifies the increment between elements of each y_i.**stride_y**–**[in]**[rocblas_stride] specifies the increment from the beginning of y_i to the beginning of y_(i+1)**c**–**[in]**device pointer or host pointer to scalar cosine component of the rotation matrix.**s**–**[in]**device pointer or host pointer to scalar sine component of the rotation matrix.**cs_type**–**[in]**[rocblas_datatype] specifies the datatype of c and s.**batch_count**–**[in]**[rocblas_int] the number of x and y arrays, the number of batches.**execution_type**–**[in]**[rocblas_datatype] specifies the datatype of computation.



`rot_ex`

, `rot_batched_ex`

, and `rot_strided_batched_ex`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_scal_ex + batched, strided_batched[#](#rocblas-scal-ex-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_scal_ex([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const void *alpha,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)alpha_type, void *x,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)x_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)execution_type)[#](#_CPPv415rocblas_scal_ex14rocblas_handle11rocblas_intPKv16rocblas_datatypePv16rocblas_datatype11rocblas_int16rocblas_datatype)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_scal_batched_ex([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const void *alpha,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)alpha_type, void *x,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)x_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)execution_type)[#](#_CPPv423rocblas_scal_batched_ex14rocblas_handle11rocblas_intPKv16rocblas_datatypePv16rocblas_datatype11rocblas_int11rocblas_int16rocblas_datatype)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_scal_strided_batched_ex([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const void *alpha,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)alpha_type, void *x,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)x_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stridex,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)execution_type)[#](#_CPPv431rocblas_scal_strided_batched_ex14rocblas_handle11rocblas_intPKv16rocblas_datatypePv16rocblas_datatype11rocblas_int14rocblas_stride11rocblas_int16rocblas_datatype) **BLAS EX API**scal_strided_batched_ex scales each element of vector x with scalar alpha over a set of strided batched vectors.

Currently supported datatypes are as follows:x := alpha * x

alpha_type

x_type

execution_type

f32_r

bf16_r

f32_r

bf16_r

bf16_r

f32_r

f16_r

f16_r

f16_r

f16_r

f16_r

f32_r

f32_r

f16_r

f32_r

f32_r

f32_r

f32_r

f64_r

f64_r

f64_r

f32_c

f32_c

f32_c

f64_c

f64_c

f64_c

f32_r

f32_c

f32_c

f64_r

f64_c

f64_c

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**n**–**[in]**[rocblas_int] the number of elements in x.**alpha**–**[in]**device pointer or host pointer for the scalar alpha.**alpha_type**–**[in]**[rocblas_datatype] specifies the datatype of alpha.**x**–**[inout]**device pointer to the first vector x_1.**x_type**–**[in]**[rocblas_datatype] specifies the datatype of each vector x_i.**incx**–**[in]**[rocblas_int] specifies the increment for the elements of each x_i.**stridex**–**[in]**[rocblas_stride] stride from the start of one vector (x_i) to the next one (x_i+1). There are no restrictions placed on stridex. However, ensure that stridex is of appropriate size. For a typical case this means stridex >= n * incx.**batch_count**–**[in]**[rocblas_int] number of instances in the batch.**execution_type**–**[in]**[rocblas_datatype] specifies the datatype of computation.



`scal_ex`

, `scal_batched_ex`

, and `scal_strided_batched_ex`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_gemm_ex + batched, strided_batched[#](#rocblas-gemm-ex-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_gemm_ex([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const void *alpha, const void *a,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)a_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const void *b,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)b_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const void *beta, const void *c,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)c_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc, void *d,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)d_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldd,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)compute_type,[rocblas_gemm_algo](enumerations.html#_CPPv417rocblas_gemm_algo)algo, int32_t solution_index, uint32_t flags)[#](#_CPPv415rocblas_gemm_ex14rocblas_handle17rocblas_operation17rocblas_operation11rocblas_int11rocblas_int11rocblas_intPKvPKv16rocblas_datatype11rocblas_intPKv16rocblas_datatype11rocblas_intPKvPKv16rocblas_datatype11rocblas_intPv16rocblas_datatype11rocblas_int16rocblas_datatype17rocblas_gemm_algo7int32_t8uint32_t) **BLAS EX API**gemm_ex performs one of the matrix-matrix operations:

where op( X ) is one ofD = alpha*op( A )*op( B ) + beta*C,

alpha and beta are scalars, and A, B, C, and D are matrices, with op( A ) an m by k matrix, op( B ) a k by n matrix and C and D are m by n matrices. C and D may point to the same matrix if their parameters are identical.op( X ) = X or op( X ) = X**T or op( X ) = X**H,

Supported types are as follows:

rocblas_datatype_f64_r = a_type = b_type = c_type = d_type = compute_type

rocblas_datatype_f32_r = a_type = b_type = c_type = d_type = compute_type

rocblas_datatype_f16_r = a_type = b_type = c_type = d_type = compute_type

rocblas_datatype_f16_r = a_type = b_type = c_type = d_type; rocblas_datatype_f32_r = compute_type

rocblas_datatype_f16_r = a_type = b_type; rocblas_datatype_f32_r = c_type = d_type = compute_type

rocblas_datatype_bf16_r = a_type = b_type = c_type = d_type; rocblas_datatype_f32_r = compute_type

rocblas_datatype_bf16_r = a_type = b_type; rocblas_datatype_f32_r = c_type = d_type = compute_type

rocblas_datatype_i8_r = a_type = b_type; rocblas_datatype_i32_r = c_type = d_type = compute_type

rocblas_datatype_f32_c = a_type = b_type = c_type = d_type = compute_type

rocblas_datatype_f64_c = a_type = b_type = c_type = d_type = compute_type


Although not widespread, some gemm kernels used by gemm_ex may use atomic operations. See Atomic Operations in the API Reference Guide for more information.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**transA**–**[in]**[rocblas_operation] specifies the form of op( A ).**transB**–**[in]**[rocblas_operation] specifies the form of op( B ).**m**–**[in]**[rocblas_int] matrix dimension m.**n**–**[in]**[rocblas_int] matrix dimension n.**k**–**[in]**[rocblas_int] matrix dimension k.**alpha**–**[in]**[const void *] device pointer or host pointer specifying the scalar alpha. Same datatype as compute_type.**a**–**[in]**[void *] device pointer storing matrix A.**a_type**–**[in]**[rocblas_datatype] specifies the datatype of matrix A.**lda**–**[in]**[rocblas_int] specifies the leading dimension of A.**b**–**[in]**[void *] device pointer storing matrix B.**b_type**–**[in]**[rocblas_datatype] specifies the datatype of matrix B.**ldb**–**[in]**[rocblas_int] specifies the leading dimension of B.**beta**–**[in]**[const void *] device pointer or host pointer specifying the scalar beta. Same datatype as compute_type.**c**–**[in]**[void *] device pointer storing matrix C.**c_type**–**[in]**[rocblas_datatype] specifies the datatype of matrix C.**ldc**–**[in]**[rocblas_int] specifies the leading dimension of C.**d**–**[out]**[void *] device pointer storing matrix D. If d and c pointers are to the same matrix then d_type must equal c_type and ldd must equal ldc or the respective invalid status will be returned.**d_type**–**[in]**[rocblas_datatype] specifies the datatype of matrix D.**ldd**–**[in]**[rocblas_int] specifies the leading dimension of D.**compute_type**–**[in]**[rocblas_datatype] specifies the datatype of computation.**algo**–**[in]**[rocblas_gemm_algo] enumerant specifying the algorithm type.**solution_index**–**[in]**[int32_t] if algo is rocblas_gemm_algo_solution_index, this controls which solution is used. When algo is not rocblas_gemm_algo_solution_index, or if solution_index = 0, the default solution is used. Passing rocblas_gemm_algo_solution_index and solution_index < 0 to use the default solution is deprecated.**flags**–**[in]**[uint32_t] optional gemm flags.



`gemm_ex`

functions support the `_64`

interface. However, no arguments larger than `(int32_t max value * 16)`

are currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_gemm_batched_ex([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const void *alpha, const void *a,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)a_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const void *b,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)b_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const void *beta, const void *c,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)c_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc, void *d,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)d_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldd,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)compute_type,[rocblas_gemm_algo](enumerations.html#_CPPv417rocblas_gemm_algo)algo, int32_t solution_index, uint32_t flags)[#](#_CPPv423rocblas_gemm_batched_ex14rocblas_handle17rocblas_operation17rocblas_operation11rocblas_int11rocblas_int11rocblas_intPKvPKv16rocblas_datatype11rocblas_intPKv16rocblas_datatype11rocblas_intPKvPKv16rocblas_datatype11rocblas_intPv16rocblas_datatype11rocblas_int11rocblas_int16rocblas_datatype17rocblas_gemm_algo7int32_t8uint32_t) **BLAS EX API**gemm_batched_ex performs one of the batched matrix-matrix operations: D_i = alpha*op(A_i)*op(B_i) + beta*C_i, for i = 1, …, batch_count. where op( X ) is one of op( X ) = X or op( X ) = X**T or op( X ) = X**H, alpha and beta are scalars, and A, B, C, and D are batched pointers to matrices, with op( A ) an m by k by batch_count batched matrix, op( B ) a k by n by batch_count batched matrix and C and D are m by n by batch_count batched matrices. The batched matrices are an array of pointers to matrices. The number of pointers to matrices is batch_count. C and D may point to the same matrices if their parameters are identical.

Supported types are as follows:

rocblas_datatype_f64_r = a_type = b_type = c_type = d_type = compute_type

rocblas_datatype_f32_r = a_type = b_type = c_type = d_type = compute_type

rocblas_datatype_f16_r = a_type = b_type = c_type = d_type = compute_type

rocblas_datatype_f16_r = a_type = b_type = c_type = d_type; rocblas_datatype_f32_r = compute_type

rocblas_datatype_bf16_r = a_type = b_type = c_type = d_type; rocblas_datatype_f32_r = compute_type

rocblas_datatype_i8_r = a_type = b_type; rocblas_datatype_i32_r = c_type = d_type = compute_type

rocblas_datatype_f32_c = a_type = b_type = c_type = d_type = compute_type

rocblas_datatype_f64_c = a_type = b_type = c_type = d_type = compute_type


- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**transA**–**[in]**[rocblas_operation] specifies the form of op( A ).**transB**–**[in]**[rocblas_operation] specifies the form of op( B ).**m**–**[in]**[rocblas_int] matrix dimension m.**n**–**[in]**[rocblas_int] matrix dimension n.**k**–**[in]**[rocblas_int] matrix dimension k.**alpha**–**[in]**[const void *] device pointer or host pointer specifying the scalar alpha. Same datatype as compute_type.**a**–**[in]**[void *] device pointer storing array of pointers to each matrix A_i.**a_type**–**[in]**[rocblas_datatype] specifies the datatype of each matrix A_i.**lda**–**[in]**[rocblas_int] specifies the leading dimension of each A_i.**b**–**[in]**[void *] device pointer storing array of pointers to each matrix B_i.**b_type**–**[in]**[rocblas_datatype] specifies the datatype of each matrix B_i.**ldb**–**[in]**[rocblas_int] specifies the leading dimension of each B_i.**beta**–**[in]**[const void *] device pointer or host pointer specifying the scalar beta. Same datatype as compute_type.**c**–**[in]**[void *] device array of device pointers to each matrix C_i.**c_type**–**[in]**[rocblas_datatype] specifies the datatype of each matrix C_i.**ldc**–**[in]**[rocblas_int] specifies the leading dimension of each C_i.**d**–**[out]**[void *] device array of device pointers to each matrix D_i. If d and c are the same array of matrix pointers then d_type must equal c_type and ldd must equal ldc or the respective invalid status will be returned.**d_type**–**[in]**[rocblas_datatype] specifies the datatype of each matrix D_i.**ldd**–**[in]**[rocblas_int] specifies the leading dimension of each D_i.**batch_count**–**[in]**[rocblas_int] number of gemm operations in the batch.**compute_type**–**[in]**[rocblas_datatype] specifies the datatype of computation.**algo**–**[in]**[rocblas_gemm_algo] enumerant specifying the algorithm type.**solution_index**–**[in]**[int32_t] if algo is rocblas_gemm_algo_solution_index, this controls which solution is used. When algo is not rocblas_gemm_algo_solution_index, or if solution_index = 0, the default solution is used. Passing rocblas_gemm_algo_solution_index and solution_index < 0 to use the default solution is deprecated.**flags**–**[in]**[uint32_t] optional gemm flags.



`gemm_batched_ex`

functions support the `_64`

interface. Only the parameter `batch_count`

larger than `(int32_t max value * 16)`

is currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_gemm_strided_batched_ex([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const void *alpha, const void *a,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)a_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_a, const void *b,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)b_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_b, const void *beta, const void *c,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)c_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_c, void *d,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)d_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldd,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_d,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)compute_type,[rocblas_gemm_algo](enumerations.html#_CPPv417rocblas_gemm_algo)algo, int32_t solution_index, uint32_t flags)[#](#_CPPv431rocblas_gemm_strided_batched_ex14rocblas_handle17rocblas_operation17rocblas_operation11rocblas_int11rocblas_int11rocblas_intPKvPKv16rocblas_datatype11rocblas_int14rocblas_stridePKv16rocblas_datatype11rocblas_int14rocblas_stridePKvPKv16rocblas_datatype11rocblas_int14rocblas_stridePv16rocblas_datatype11rocblas_int14rocblas_stride11rocblas_int16rocblas_datatype17rocblas_gemm_algo7int32_t8uint32_t) **BLAS EX API**gemm_strided_batched_ex performs one of the strided_batched matrix-matrix operations:

where op( X ) is one ofD_i = alpha*op(A_i)*op(B_i) + beta*C_i, for i = 1, ..., batch_count

alpha and beta are scalars, and A, B, C, and D are strided_batched matrices, with op( A ) an m by k by batch_count strided_batched matrix, op( B ) a k by n by batch_count strided_batched matrix and C and D are m by n by batch_count strided_batched matrices. C and D may point to the same matrices if their parameters are identical.op( X ) = X or op( X ) = X**T or op( X ) = X**H,

The strided_batched matrices are multiple matrices separated by a constant stride. The number of matrices is batch_count.

Supported types are as follows:

rocblas_datatype_f64_r = a_type = b_type = c_type = d_type = compute_type

rocblas_datatype_f32_r = a_type = b_type = c_type = d_type = compute_type

rocblas_datatype_f16_r = a_type = b_type = c_type = d_type = compute_type

rocblas_datatype_f16_r = a_type = b_type = c_type = d_type; rocblas_datatype_f32_r = compute_type

rocblas_datatype_bf16_r = a_type = b_type = c_type = d_type; rocblas_datatype_f32_r = compute_type

rocblas_datatype_i8_r = a_type = b_type; rocblas_datatype_i32_r = c_type = d_type = compute_type

rocblas_datatype_f32_c = a_type = b_type = c_type = d_type = compute_type

rocblas_datatype_f64_c = a_type = b_type = c_type = d_type = compute_type


- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**transA**–**[in]**[rocblas_operation] specifies the form of op( A ).**transB**–**[in]**[rocblas_operation] specifies the form of op( B ).**m**–**[in]**[rocblas_int] matrix dimension m.**n**–**[in]**[rocblas_int] matrix dimension n.**k**–**[in]**[rocblas_int] matrix dimension k.**alpha**–**[in]**[const void *] device pointer or host pointer specifying the scalar alpha. Same datatype as compute_type.**a**–**[in]**[void *] device pointer pointing to first matrix A_1.**a_type**–**[in]**[rocblas_datatype] specifies the datatype of each matrix A_i.**lda**–**[in]**[rocblas_int] specifies the leading dimension of each A_i.**stride_a**–**[in]**[rocblas_stride] specifies stride from start of one A_i matrix to the next A_(i + 1).**b**–**[in]**[void *] device pointer pointing to first matrix B_1.**b_type**–**[in]**[rocblas_datatype] specifies the datatype of each matrix B_i.**ldb**–**[in]**[rocblas_int] specifies the leading dimension of each B_i.**stride_b**–**[in]**[rocblas_stride] specifies stride from start of one B_i matrix to the next B_(i + 1).**beta**–**[in]**[const void *] device pointer or host pointer specifying the scalar beta. Same datatype as compute_type.**c**–**[in]**[void *] device pointer pointing to first matrix C_1.**c_type**–**[in]**[rocblas_datatype] specifies the datatype of each matrix C_i.**ldc**–**[in]**[rocblas_int] specifies the leading dimension of each C_i.**stride_c**–**[in]**[rocblas_stride] specifies stride from start of one C_i matrix to the next C_(i + 1).**d**–**[out]**[void *] device pointer storing each matrix D_i. If d and c pointers are to the same matrix then d_type must equal c_type and ldd must equal ldc and stride_d must equal stride_c or the respective invalid status will be returned.**d_type**–**[in]**[rocblas_datatype] specifies the datatype of each matrix D_i.**ldd**–**[in]**[rocblas_int] specifies the leading dimension of each D_i.**stride_d**–**[in]**[rocblas_stride] specifies stride from start of one D_i matrix to the next D_(i + 1).**batch_count**–**[in]**[rocblas_int] number of gemm operations in the batch.**compute_type**–**[in]**[rocblas_datatype] specifies the datatype of computation.**algo**–**[in]**[rocblas_gemm_algo] enumerant specifying the algorithm type.**solution_index**–**[in]**[int32_t] if algo is rocblas_gemm_algo_solution_index, this controls which solution is used. When algo is not rocblas_gemm_algo_solution_index, or if solution_index = 0, the default solution is used. Passing rocblas_gemm_algo_solution_index and solution_index < 0 to use the default solution is deprecated.**flags**–**[in]**[uint32_t] optional gemm flags.



`gemm_strided_batched_ex`

functions support the `_64`

interface. Only the parameter `batch_count`

larger than `(int32_t max value * 16)`

is currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_syrk_ex[#](#rocblas-syrk-ex)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_syrk_ex([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const void *alpha, const void *A,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)a_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const void *beta, void *C,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)c_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)execution_type)[#](#_CPPv415rocblas_syrk_ex14rocblas_handle12rocblas_fill17rocblas_operation11rocblas_int11rocblas_intPKvPKv16rocblas_datatype11rocblas_intPKvPv16rocblas_datatype11rocblas_int16rocblas_datatype) **BLAS EX API**syrk_ex performs one of the matrix-matrix operations for a symmetric rank-k update:

Currently supported datatypes are as follows:C := alpha*op( A )*op( A )^T + beta*C, where alpha and beta are scalars, op(A) is an n by k matrix, and C is a symmetric n x n matrix stored as either upper or lower. op( A ) = A, and A is n by k if transA == rocblas_operation_none op( A ) = A^T and A is k by n if transA == rocblas_operation_transpose

a_type

c_type

execution_type

bf16_r

bf16_r

f32_r

bf16_r

f32_r

f32_r

f16_r

f16_r

f32_r

f16_r

f32_r

f32_r

f32_r

f32_r

f64_r

f32_r

f64_r

f64_r

rocblas_operation_conjugate_transpose is not supported for complex types. See cherk and zherk.

if transA = rocblas_operation_none, lda >= max( 1, n ), otherwise lda >= max( 1, k ).

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: C is an upper triangular matrix

rocblas_fill_lower: C is a lower triangular matrix


**transA**–**[in]**[rocblas_operation]rocblas_operation_transpose: op(A) = A^T

rocblas_operation_none: op(A) = A

rocblas_operation_conjugate_transpose: op(A) = A^T


**n**–**[in]**[rocblas_int] n specifies the number of rows and columns of C. n >= 0.**k**–**[in]**[rocblas_int] k specifies the number of columns of op(A). k >= 0.**alpha**–**[in]**[const void *] device pointer or host pointer specifying the scalar alpha. When alpha is zero then A is not referenced and A need not be set before entry. Same datatype as compute_type.**A**–**[in]**pointer storing matrix A on the GPU. Matrix dimension is ( lda, k ) when if transA = rocblas_operation_none, otherwise (lda, n)**a_type**–**[in]**[rocblas_datatype] specifies the datatype of matrix A.**lda**–**[in]**[rocblas_int] lda specifies the first dimension of A.**beta**–**[in]**[const void *] device pointer or host pointer specifying the scalar beta. When beta is zero then C need not be set before entry. Same datatype as compute_type.**C**–**[in]**pointer storing matrix C on the GPU. only the upper/lower triangular part is accessed.**c_type**–**[in]**[rocblas_datatype] specifies the datatype of matrix C.**ldc**–**[in]**[rocblas_int] ldc specifies the first dimension of C. ldc >= max( 1, n ).**execution_type**–**[in]**[rocblas_datatype] specifies the datatype of computation.



## rocblas_trsm_ex + batched, strided_batched[#](#rocblas-trsm-ex-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_trsm_ex([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const void *alpha, const void *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, void *B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const void *invA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)invA_size,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)compute_type)[#](#_CPPv415rocblas_trsm_ex14rocblas_handle12rocblas_side12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPKvPKv11rocblas_intPv11rocblas_intPKv11rocblas_int16rocblas_datatype)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_trsm_batched_ex([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const void *alpha, const void *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, void *B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count, const void *invA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)invA_size,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)compute_type)[#](#_CPPv423rocblas_trsm_batched_ex14rocblas_handle12rocblas_side12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPKvPKv11rocblas_intPv11rocblas_int11rocblas_intPKv11rocblas_int16rocblas_datatype)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_trsm_strided_batched_ex([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_diagonal](enumerations.html#_CPPv416rocblas_diagonal)diag,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const void *alpha, const void *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, void *B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count, const void *invA,[rocblas_int](datatypes.html#_CPPv411rocblas_int)invA_size,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_invA,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)compute_type)[#](#_CPPv431rocblas_trsm_strided_batched_ex14rocblas_handle12rocblas_side12rocblas_fill17rocblas_operation16rocblas_diagonal11rocblas_int11rocblas_intPKvPKv11rocblas_int14rocblas_stridePv11rocblas_int14rocblas_stride11rocblas_intPKv11rocblas_int14rocblas_stride16rocblas_datatype) **BLAS EX API**trsm_strided_batched_ex solves:

for i = 1, …, batch_count; and where alpha is a scalar, X and B are strided batched m by n matrices, A is a strided batched triangular matrix and op(A_i) is one ofop(A_i)*X_i = alpha*B_i or X_i*op(A_i) = alpha*B_i,

Each matrix X_i is overwritten on B_i.op( A_i ) = A_i or op( A_i ) = A_i^T or op( A_i ) = A_i^H.

This function gives the user the ability to reuse each invA_i matrix between runs. If invA == NULL, rocblas_trsm_batched_ex will automatically calculate each invA_i on every run.

Setting up invA: Each accepted invA_i matrix consists of the packed 128x128 inverses of the diagonal blocks of matrix A_i, followed by any smaller diagonal block that remains. To set up invA_i it is recommended that rocblas_trtri_batched be used with matrix A_i as the input. invA is a contiguous piece of memory holding each invA_i.

Device memory of size 128 x k should be allocated for each invA_i ahead of time, where k is m when rocblas_side_left and is n when rocblas_side_right. The actual number of elements in each invA_i should be passed as invA_size.

To begin, rocblas_trtri_batched must be called on the full 128x128-sized diagonal blocks of each matrix A_i. Below are the restricted parameters:

n = 128

ldinvA = 128

stride_invA = 128x128

batch_count = k / 128


Then any remaining block may be added:

n = k % 128

invA = invA + stride_invA * previous_batch_count

ldinvA = 128

batch_count = 1


- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**side**–**[in]**[rocblas_side]rocblas_side_left: op(A)*X = alpha*B

rocblas_side_right: X*op(A) = alpha*B


**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: each A_i is an upper triangular matrix.

rocblas_fill_lower: each A_i is a lower triangular matrix.


**transA**–**[in]**[rocblas_operation]transB: op(A) = A.

rocblas_operation_transpose: op(A) = A^T

rocblas_operation_conjugate_transpose: op(A) = A^H


**diag**–**[in]**[rocblas_diagonal]rocblas_diagonal_unit: each A_i is assumed to be unit triangular.

rocblas_diagonal_non_unit: each A_i is not assumed to be unit triangular.


**m**–**[in]**[rocblas_int] m specifies the number of rows of each B_i. m >= 0.**n**–**[in]**[rocblas_int] n specifies the number of columns of each B_i. n >= 0.**alpha**–**[in]**[void *] device pointer or host pointer specifying the scalar alpha. When alpha is &zero then A is not referenced, and B need not be set before entry.**A**–**[in]**[void *] device pointer storing matrix A. of dimension ( lda, k ), where k is m when rocblas_side_left and is n when rocblas_side_right only the upper/lower triangular part is accessed.**lda**–**[in]**[rocblas_int] lda specifies the first dimension of A.if side = rocblas_side_left, lda >= max( 1, m ), if side = rocblas_side_right, lda >= max( 1, n ).

**stride_A**–**[in]**[rocblas_stride] The stride between each A matrix.**B**–**[inout]**[void *] device pointer pointing to first matrix B_i. each B_i is of dimension ( ldb, n ). Before entry, the leading m by n part of each array B_i must contain the right-hand side of matrix B_i, and on exit is overwritten by the solution matrix X_i.**ldb**–**[in]**[rocblas_int] ldb specifies the first dimension of each B_i. ldb >= max( 1, m ).**stride_B**–**[in]**[rocblas_stride] The stride between each B_i matrix.**batch_count**–**[in]**[rocblas_int] specifies how many batches.**invA**–**[in]**[void *] device pointer storing the inverse diagonal blocks of each A_i. invA points to the first invA_1. each invA_i is of dimension ( ld_invA, k ), where k is m when rocblas_side_left and is n when rocblas_side_right. ld_invA must be equal to 128.**invA_size**–**[in]**[rocblas_int] invA_size specifies the number of elements of device memory in each invA_i.**stride_invA**–**[in]**[rocblas_stride] The stride between each invA matrix.**compute_type**–**[in]**[rocblas_datatype] specifies the datatype of computation.



## rocblas_Xgeam + batched, strided_batched[#](#rocblas-xgeam-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sgeam([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const float *beta, const float *B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, float *C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv413rocblas_sgeam14rocblas_handle17rocblas_operation17rocblas_operation11rocblas_int11rocblas_intPKfPKf11rocblas_intPKfPKf11rocblas_intPf11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dgeam([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const double *beta, const double *B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, double *C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv413rocblas_dgeam14rocblas_handle17rocblas_operation17rocblas_operation11rocblas_int11rocblas_intPKdPKd11rocblas_intPKdPKd11rocblas_intPd11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cgeam([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv413rocblas_cgeam14rocblas_handle17rocblas_operation17rocblas_operation11rocblas_int11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_intP21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zgeam([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv413rocblas_zgeam14rocblas_handle17rocblas_operation17rocblas_operation11rocblas_int11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_intP22rocblas_double_complex11rocblas_int) **BLAS Level 3 API**geam performs one of the matrix-matrix operations:

C = alpha*op( A ) + beta*op( B ), where op( X ) is one of op( X ) = X or op( X ) = X**T or op( X ) = X**H, alpha and beta are scalars, and A, B and C are matrices, with op( A ) an m by n matrix, op( B ) an m by n matrix, and C an m by n matrix.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**transA**–**[in]**[rocblas_operation] specifies the form of op( A ).**transB**–**[in]**[rocblas_operation] specifies the form of op( B ).**m**–**[in]**[rocblas_int] matrix dimension m.**n**–**[in]**[rocblas_int] matrix dimension n.**alpha**–**[in]**device pointer or host pointer specifying the scalar alpha.**A**–**[in]**device pointer storing matrix A.**lda**–**[in]**[rocblas_int] specifies the leading dimension of A.**beta**–**[in]**device pointer or host pointer specifying the scalar beta.**B**–**[in]**device pointer storing matrix B.**ldb**–**[in]**[rocblas_int] specifies the leading dimension of B.**C**–**[inout]**device pointer storing matrix C.**ldc**–**[in]**[rocblas_int] specifies the leading dimension of C.



The `geam`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sgeam_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const float *beta, const float *const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, float *const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_sgeam_batched14rocblas_handle17rocblas_operation17rocblas_operation11rocblas_int11rocblas_intPKfA_PCKf11rocblas_intPKfA_PCKf11rocblas_intA_PCf11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dgeam_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const double *beta, const double *const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, double *const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_dgeam_batched14rocblas_handle17rocblas_operation17rocblas_operation11rocblas_int11rocblas_intPKdA_PCKd11rocblas_intPKdA_PCKd11rocblas_intA_PCd11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cgeam_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_cgeam_batched14rocblas_handle17rocblas_operation17rocblas_operation11rocblas_int11rocblas_intPK21rocblas_float_complexA_PCK21rocblas_float_complex11rocblas_intPK21rocblas_float_complexA_PCK21rocblas_float_complex11rocblas_intA_PC21rocblas_float_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zgeam_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_zgeam_batched14rocblas_handle17rocblas_operation17rocblas_operation11rocblas_int11rocblas_intPK22rocblas_double_complexA_PCK22rocblas_double_complex11rocblas_intPK22rocblas_double_complexA_PCK22rocblas_double_complex11rocblas_intA_PC22rocblas_double_complex11rocblas_int11rocblas_int) **BLAS Level 3 API**geam_batched performs one of the batched matrix-matrix operations:

C_i = alpha*op( A_i ) + beta*op( B_i ) for i = 0, 1, ... batch_count - 1, where alpha and beta are scalars, and op(A_i), op(B_i) and C_i are m by n matrices and op( X ) is one of op( X ) = X or op( X ) = X**T

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**transA**–**[in]**[rocblas_operation] specifies the form of op( A ).**transB**–**[in]**[rocblas_operation] specifies the form of op( B ).**m**–**[in]**[rocblas_int] matrix dimension m.**n**–**[in]**[rocblas_int] matrix dimension n.**alpha**–**[in]**device pointer or host pointer specifying the scalar alpha.**A**–**[in]**device array of device pointers storing each matrix A_i on the GPU. Each A_i is of dimension ( lda, k ), where k is m when transA == rocblas_operation_none and is n when transA == rocblas_operation_transpose.**lda**–**[in]**[rocblas_int] specifies the leading dimension of A.**beta**–**[in]**device pointer or host pointer specifying the scalar beta.**B**–**[in]**device array of device pointers storing each matrix B_i on the GPU. Each B_i is of dimension ( ldb, k ), where k is m when transB == rocblas_operation_none and is n when transB == rocblas_operation_transpose.**ldb**–**[in]**[rocblas_int] specifies the leading dimension of B.**C**–**[inout]**device array of device pointers storing each matrix C_i on the GPU. Each C_i is of dimension ( ldc, n ).**ldc**–**[in]**[rocblas_int] specifies the leading dimension of C.**batch_count**–**[in]**[rocblas_int] number of instances i in the batch.



The `geam_batched`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sgeam_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *alpha, const float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const float *beta, const float *B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_B, float *C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_sgeam_strided_batched14rocblas_handle17rocblas_operation17rocblas_operation11rocblas_int11rocblas_intPKfPKf11rocblas_int14rocblas_stridePKfPKf11rocblas_int14rocblas_stridePf11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dgeam_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *alpha, const double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const double *beta, const double *B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_B, double *C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_dgeam_strided_batched14rocblas_handle17rocblas_operation17rocblas_operation11rocblas_int11rocblas_intPKdPKd11rocblas_int14rocblas_stridePKdPKd11rocblas_int14rocblas_stridePd11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cgeam_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_B,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_cgeam_strided_batched14rocblas_handle17rocblas_operation17rocblas_operation11rocblas_int11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_int14rocblas_stridePK21rocblas_float_complexPK21rocblas_float_complex11rocblas_int14rocblas_strideP21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zgeam_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_B,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_zgeam_strided_batched14rocblas_handle17rocblas_operation17rocblas_operation11rocblas_int11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_int14rocblas_stridePK22rocblas_double_complexPK22rocblas_double_complex11rocblas_int14rocblas_strideP22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_int) **BLAS Level 3 API**geam_strided_batched performs one of the batched matrix-matrix operations:

C_i = alpha*op( A_i ) + beta*op( B_i ) for i = 0, 1, ... batch_count - 1, where alpha and beta are scalars, and op(A_i), op(B_i) and C_i are m by n matrices and op( X ) is one of op( X ) = X or op( X ) = X**T

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**transA**–**[in]**[rocblas_operation] specifies the form of op( A ).**transB**–**[in]**[rocblas_operation] specifies the form of op( B ).**m**–**[in]**[rocblas_int] matrix dimension m.**n**–**[in]**[rocblas_int] matrix dimension n.**alpha**–**[in]**device pointer or host pointer specifying the scalar alpha.**A**–**[in]**device pointer to the first matrix A_0 on the GPU. Each A_i is of dimension ( lda, k ), where k is m when transA == rocblas_operation_none and is n when transA == rocblas_operation_transpose.**lda**–**[in]**[rocblas_int] specifies the leading dimension of A.**stride_A**–**[in]**[rocblas_stride] stride from the start of one matrix (A_i) and the next one (A_i+1).**beta**–**[in]**device pointer or host pointer specifying the scalar beta.**B**–**[in]**pointer to the first matrix B_0 on the GPU. Each B_i is of dimension ( ldb, k ), where k is m when transB == rocblas_operation_none and is n when transB == rocblas_operation_transpose.**ldb**–**[in]**[rocblas_int] specifies the leading dimension of B.**stride_B**–**[in]**[rocblas_stride] stride from the start of one matrix (B_i) and the next one (B_i+1)**C**–**[inout]**pointer to the first matrix C_0 on the GPU. Each C_i is of dimension ( ldc, n ).**ldc**–**[in]**[rocblas_int] specifies the leading dimension of C.**stride_C**–**[in]**[rocblas_stride] stride from the start of one matrix (C_i) and the next one (C_i+1).**batch_count**–**[in]**[rocblas_int] number of instances i in the batch.



The `geam_strided_batched`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_geam_ex[#](#rocblas-geam-ex)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_geam_ex([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const void *alpha, const void *A,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)a_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const void *B,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)b_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const void *beta, const void *C,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)c_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc, void *D,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)d_type,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldd,[rocblas_datatype](enumerations.html#_CPPv416rocblas_datatype)compute_type, rocblas_geam_ex_operation geam_ex_op)[#](#_CPPv415rocblas_geam_ex14rocblas_handle17rocblas_operation17rocblas_operation11rocblas_int11rocblas_int11rocblas_intPKvPKv16rocblas_datatype11rocblas_intPKv16rocblas_datatype11rocblas_intPKvPKv16rocblas_datatype11rocblas_intPv16rocblas_datatype11rocblas_int16rocblas_datatype25rocblas_geam_ex_operation) **BLAS EX API**geam_ex performs one of the matrix-matrix operations:

alpha and beta are scalars, and A, B, C, and D are matrices, with op( A ) an m by k matrix, op( B ) a k by n matrix and C and D are m by n matrices. C and D may point to the same matrix if their type and leading dimensions are identical.Dij = min(alpha * (Aik + Bkj), beta * Cij) Dij = min(alpha * Aik, alpha * Bkj) + beta * Cij

Aik refers to the element at the i-th row and k-th column of op( A ), Bkj refers to the element at the k-th row and j-th column of op( B ), and Cij/Dij refers to the element at the i-th row and j-th column of C/D.

Supported types are as follows:

rocblas_datatype_f64_r = a_type = b_type = c_type = d_type = compute_type

rocblas_datatype_f32_r = a_type = b_type = c_type = d_type = compute_type

rocblas_datatype_f16_r = a_type = b_type = c_type = d_type = compute_type


if transA == N, must have lda >= max(1, m) otherwise, must have lda >= max(1, k)

if transB == N, must have ldb >= max(1, k) otherwise, must have ldb >= max(1, n)

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**transA**–**[in]**[rocblas_operation] specifies the form of op( A ).**transB**–**[in]**[rocblas_operation] specifies the form of op( B ).**m**–**[in]**[rocblas_int] matrix dimension m.**n**–**[in]**[rocblas_int] matrix dimension n.**k**–**[in]**[rocblas_int] matrix dimension k.**alpha**–**[in]**[const void *] device pointer or host pointer specifying the scalar alpha. Same datatype as compute_type.**A**–**[in]**[void *] device pointer storing matrix A.**a_type**–**[in]**[rocblas_datatype] specifies the datatype of matrix A.**lda**–**[in]**[rocblas_int] specifies the leading dimension of A**B**–**[in]**[void *] device pointer storing matrix B.**b_type**–**[in]**[rocblas_datatype] specifies the datatype of matrix B.**ldb**–**[in]**[rocblas_int] specifies the leading dimension of B**beta**–**[in]**[const void *] device pointer or host pointer specifying the scalar beta. Same datatype as compute_type.**C**–**[in]**[void *] device pointer storing matrix C.**c_type**–**[in]**[rocblas_datatype] specifies the datatype of matrix C.**ldc**–**[in]**[rocblas_int] specifies the leading dimension of C, must have ldc >= max(1, m).**D**–**[out]**[void *] device pointer storing matrix D. If D and C pointers are to the same matrix then d_type must equal c_type and ldd must equal ldc or the respective invalid status will be returned.**d_type**–**[in]**[rocblas_datatype] specifies the datatype of matrix D.**ldd**–**[in]**[rocblas_int] specifies the leading dimension of D, must have ldd >= max(1, m).**compute_type**–**[in]**[rocblas_datatype] specifies the datatype of computation.**geam_ex_op**–**[in]**[rocblas_geam_ex_operation] enumerant specifying the operation type, support for rocblas_geam_ex_operation_min_plus and rocblas_geam_ex_operation_plus_min.



## rocblas_Xdgmm + batched, strided_batched[#](#rocblas-xdgmm-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sdgmm([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, float *C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv413rocblas_sdgmm14rocblas_handle12rocblas_side11rocblas_int11rocblas_intPKf11rocblas_intPKf11rocblas_intPf11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ddgmm([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, double *C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv413rocblas_ddgmm14rocblas_handle12rocblas_side11rocblas_int11rocblas_intPKd11rocblas_intPKd11rocblas_intPd11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cdgmm([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv413rocblas_cdgmm14rocblas_handle12rocblas_side11rocblas_int11rocblas_intPK21rocblas_float_complex11rocblas_intPK21rocblas_float_complex11rocblas_intP21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zdgmm([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv413rocblas_zdgmm14rocblas_handle12rocblas_side11rocblas_int11rocblas_intPK22rocblas_double_complex11rocblas_intPK22rocblas_double_complex11rocblas_intP22rocblas_double_complex11rocblas_int) **BLAS Level 3 API**dgmm performs one of the matrix-matrix operations:

C = A * diag(x) if side == rocblas_side_right C = diag(x) * A if side == rocblas_side_left where C and A are m by n dimensional matrices. diag( x ) is a diagonal matrix and x is vector of dimension n if side == rocblas_side_right and dimension m if side == rocblas_side_left.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**side**–**[in]**[rocblas_side] specifies the side of diag(x).**m**–**[in]**[rocblas_int] matrix dimension m.**n**–**[in]**[rocblas_int] matrix dimension n.**A**–**[in]**device pointer storing matrix A.**lda**–**[in]**[rocblas_int] specifies the leading dimension of A.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[rocblas_int] specifies the increment between values of x**C**–**[inout]**device pointer storing matrix C.**ldc**–**[in]**[rocblas_int] specifies the leading dimension of C.



The `dgmm`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sdgmm_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const float *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, float *const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_sdgmm_batched14rocblas_handle12rocblas_side11rocblas_int11rocblas_intA_PCKf11rocblas_intA_PCKf11rocblas_intA_PCf11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ddgmm_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const double *const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, double *const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_ddgmm_batched14rocblas_handle12rocblas_side11rocblas_int11rocblas_intA_PCKd11rocblas_intA_PCKd11rocblas_intA_PCd11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cdgmm_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_cdgmm_batched14rocblas_handle12rocblas_side11rocblas_int11rocblas_intA_PCK21rocblas_float_complex11rocblas_intA_PCK21rocblas_float_complex11rocblas_intA_PC21rocblas_float_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zdgmm_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const x[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv421rocblas_zdgmm_batched14rocblas_handle12rocblas_side11rocblas_int11rocblas_intA_PCK22rocblas_double_complex11rocblas_intA_PCK22rocblas_double_complex11rocblas_intA_PC22rocblas_double_complex11rocblas_int11rocblas_int) **BLAS Level 3 API**dgmm_batched performs one of the batched matrix-matrix operations:

C_i = A_i * diag(x_i) for i = 0, 1, ... batch_count-1 if side == rocblas_side_right C_i = diag(x_i) * A_i for i = 0, 1, ... batch_count-1 if side == rocblas_side_left, where C_i and A_i are m by n dimensional matrices. diag(x_i) is a diagonal matrix and x_i is vector of dimension n if side == rocblas_side_right and dimension m if side == rocblas_side_left.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**side**–**[in]**[rocblas_side] specifies the side of diag(x).**m**–**[in]**[rocblas_int] matrix dimension m.**n**–**[in]**[rocblas_int] matrix dimension n.**A**–**[in]**device array of device pointers storing each matrix A_i on the GPU. Each A_i is of dimension ( lda, n ).**lda**–**[in]**[rocblas_int] specifies the leading dimension of A_i.**x**–**[in]**device array of device pointers storing each vector x_i on the GPU. Each x_i is of dimension n if side == rocblas_side_right and dimension m if side == rocblas_side_left.**incx**–**[in]**[rocblas_int] specifies the increment between values of x_i.**C**–**[inout]**device array of device pointers storing each matrix C_i on the GPU. Each C_i is of dimension ( ldc, n ).**ldc**–**[in]**[rocblas_int] specifies the leading dimension of C_i.**batch_count**–**[in]**[rocblas_int] number of instances in the batch.



The `dgmm_batched`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sdgmm_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const float *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x, float *C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_sdgmm_strided_batched14rocblas_handle12rocblas_side11rocblas_int11rocblas_intPKf11rocblas_int14rocblas_stridePKf11rocblas_int14rocblas_stridePf11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_ddgmm_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const double *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x, double *C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_ddgmm_strided_batched14rocblas_handle12rocblas_side11rocblas_int11rocblas_intPKd11rocblas_int14rocblas_stridePKd11rocblas_int14rocblas_stridePd11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cdgmm_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_cdgmm_strided_batched14rocblas_handle12rocblas_side11rocblas_int11rocblas_intPK21rocblas_float_complex11rocblas_int14rocblas_stridePK21rocblas_float_complex11rocblas_int14rocblas_strideP21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zdgmm_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_side](enumerations.html#_CPPv412rocblas_side)side,[rocblas_int](datatypes.html#_CPPv411rocblas_int)m,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_A, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_x,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv429rocblas_zdgmm_strided_batched14rocblas_handle12rocblas_side11rocblas_int11rocblas_intPK22rocblas_double_complex11rocblas_int14rocblas_stridePK22rocblas_double_complex11rocblas_int14rocblas_strideP22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_int) **BLAS Level 3 API**dgmm_strided_batched performs one of the batched matrix-matrix operations:

C_i = A_i * diag(x_i) if side == rocblas_side_right for i = 0, 1, ... batch_count-1 C_i = diag(x_i) * A_i if side == rocblas_side_left for i = 0, 1, ... batch_count-1, where C_i and A_i are m by n dimensional matrices. diag(x_i) is a diagonal matrix and x_i is vector of dimension n if side == rocblas_side_right and dimension m if side == rocblas_side_left.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**side**–**[in]**[rocblas_side] specifies the side of diag(x).**m**–**[in]**[rocblas_int] matrix dimension m.**n**–**[in]**[rocblas_int] matrix dimension n.**A**–**[in]**device pointer to the first matrix A_0 on the GPU. Each A_i is of dimension ( lda, n ).**lda**–**[in]**[rocblas_int] specifies the leading dimension of A.**stride_A**–**[in]**[rocblas_stride] stride from the start of one matrix (A_i) and the next one (A_i+1).**x**–**[in]**pointer to the first vector x_0 on the GPU. Each x_i is of dimension n if side == rocblas_side_right and dimension m if side == rocblas_side_left.**incx**–**[in]**[rocblas_int] specifies the increment between values of x.**stride_x**–**[in]**[rocblas_stride] stride from the start of one vector(x_i) and the next one (x_i+1).**C**–**[inout]**device pointer to the first matrix C_0 on the GPU. Each C_i is of dimension ( ldc, n ).**ldc**–**[in]**[rocblas_int] specifies the leading dimension of C.**stride_C**–**[in]**[rocblas_stride] stride from the start of one matrix (C_i) and the next one (C_i+1).**batch_count**–**[in]**[rocblas_int] number of instances i in the batch.



The `dgmm_strided_batched`

functions support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## rocblas_Xgemmt + batched, strided_batched[#](#rocblas-xgemmt-batched-strided-batched)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sgemmt([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const float *alpha, const float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const float *B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const float *beta, float *C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv414rocblas_sgemmt14rocblas_handle12rocblas_fill17rocblas_operation17rocblas_operation11rocblas_int11rocblas_intPKfPKf11rocblas_intPKf11rocblas_intPKfPf11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dgemmt([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const double *alpha, const double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const double *B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const double *beta, double *C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv414rocblas_dgemmt14rocblas_handle12rocblas_fill17rocblas_operation17rocblas_operation11rocblas_int11rocblas_intPKdPKd11rocblas_intPKd11rocblas_intPKdPd11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cgemmt([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv414rocblas_cgemmt14rocblas_handle12rocblas_fill17rocblas_operation17rocblas_operation11rocblas_int11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_intPK21rocblas_float_complex11rocblas_intPK21rocblas_float_complexP21rocblas_float_complex11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zgemmt([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc)[#](#_CPPv414rocblas_zgemmt14rocblas_handle12rocblas_fill17rocblas_operation17rocblas_operation11rocblas_int11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_intPK22rocblas_double_complex11rocblas_intPK22rocblas_double_complexP22rocblas_double_complex11rocblas_int) **BLAS Level 3 API**gemmt performs matrix-matrix operations and updates the upper or lower triangular part of the result matrix:

C = alpha*op( A )*op( B ) + beta*C, where op( X ) is one of op( X ) = X or op( X ) = X**T or op( X ) = X**H, alpha and beta are scalars. A, B are general matrices and C is either an upper or lower triangular matrix, with op( A ) an n by k matrix, op( B ) a k by n matrix and C an n by n matrix.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: C is an upper triangular matrix

rocblas_fill_lower: C is a lower triangular matrix


**transA**–**[in]**[rocblas_operation]rocblas_operation_none: op(A) = A.

rocblas_operation_transpose: op(A) = A^T

rocblas_operation_conjugate_transpose: op(A) = A^H


**transB**–**[in]**[rocblas_operation]rocblas_operation_none: op(B) = B.

rocblas_operation_transpose: op(B) = B^T

rocblas_operation_conjugate_transpose: op(B) = B^H


**n**–**[in]**[rocblas_int] number or rows of matrices op( A ), columns of op( B ), and (rows, columns) of C.**k**–**[in]**[rocblas_int] number of rows of matrices op( B ) and columns of op( A ).**alpha**–**[in]**device pointer or host pointer specifying the scalar alpha.**A**–**[in]**device pointer storing matrix A. If transa = rocblas_operation_none, then, the leading n-by-k part of the array contains the matrix A, otherwise the leading k-by-n part of the array contains the matrix A.**lda**–**[in]**[rocblas_int] specifies the leading dimension of A. If transA == rocblas_operation_none, must have lda >= max(1, n), otherwise, must have lda >= max(1, k).**B**–**[in]**device pointer storing matrix B. If transB = rocblas_operation_none, then, the leading k-by-n part of the array contains the matrix B, otherwise the leading n-by-k part of the array contains the matrix B.**ldb**–**[in]**[rocblas_int] specifies the leading dimension of B. If transB == rocblas_operation_none, must have ldb >= max(1, k), otherwise, must have ldb >= max(1, n)**beta**–**[in]**device pointer or host pointer specifying the scalar beta.**C**–**[inout]**device pointer storing matrix C on the GPU. If uplo == rocblas_fill_upper, the upper triangular part of the leading n-by-n array contains the matrix C, otherwise the lower triangular part of the leading n-by-n array contains the matrix C.**ldc**–**[in]**[rocblas_int] specifies the leading dimension of C. Must have ldc >= max(1, n).



The `gemmt`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sgemmt_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const float *alpha, const float *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const float *const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const float *beta, float *const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv422rocblas_sgemmt_batched14rocblas_handle12rocblas_fill17rocblas_operation17rocblas_operation11rocblas_int11rocblas_intPKfA_PCKf11rocblas_intA_PCKf11rocblas_intPKfA_PCf11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dgemmt_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const double *alpha, const double *const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const double *const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const double *beta, double *const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv422rocblas_dgemmt_batched14rocblas_handle12rocblas_fill17rocblas_operation17rocblas_operation11rocblas_int11rocblas_intPKdA_PCKd11rocblas_intA_PCKd11rocblas_intPKdA_PCd11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cgemmt_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv422rocblas_cgemmt_batched14rocblas_handle12rocblas_fill17rocblas_operation17rocblas_operation11rocblas_int11rocblas_intPK21rocblas_float_complexA_PCK21rocblas_float_complex11rocblas_intA_PCK21rocblas_float_complex11rocblas_intPK21rocblas_float_complexA_PC21rocblas_float_complex11rocblas_int11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zgemmt_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const A[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const B[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*const C[],[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv422rocblas_zgemmt_batched14rocblas_handle12rocblas_fill17rocblas_operation17rocblas_operation11rocblas_int11rocblas_intPK22rocblas_double_complexA_PCK22rocblas_double_complex11rocblas_intA_PCK22rocblas_double_complex11rocblas_intPK22rocblas_double_complexA_PC22rocblas_double_complex11rocblas_int11rocblas_int) **BLAS Level 3 API**gemmt_batched performs matrix-matrix operations and updates the upper or lower triangular part of the result matrix:

C_i = alpha*op( A_i )*op( B_i ) + beta*C_i, for i = 1, ..., batch_count, where op( X ) is one of op( X ) = X or op( X ) = X**T or op( X ) = X**H, alpha and beta are scalars. A, B are general matrices and C is either an upper or lower triangular matrix, with op( A ) an n by k by batch_count matrices, op( B ) an k by n by batch_count matrices and C an n by n by batch_count matrices.

- Parameters:
**handle**–**[in]**[rocblas_handle handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: C is an upper triangular matrix

rocblas_fill_lower: C is a lower triangular matrix


**transA**–**[in]**[rocblas_operation]rocblas_operation_none: op(A_i) = A_i.

rocblas_operation_transpose: op(A_i) = A_i^T

rocblas_operation_conjugate_transpose: op(A_i) = A_i^H


**transB**–**[in]**[rocblas_operation]rocblas_operation_none: op(B_i) = B_i.

rocblas_operation_transpose: op(B_i) = B_i^T

rocblas_operation_conjugate_transpose: op(B_i) = B_i^H


**n**–**[in]**[rocblas_int] number or rows of matrices op( A_i ), columns of op( B_i ), and (rows, columns) of C_i.**k**–**[in]**[rocblas_int] number of rows of matrices op( B_i ) and columns of op( A_i ).**alpha**–**[in]**device pointer or host pointer specifying the scalar alpha.**A**–**[in]**device array of device pointers storing each matrix A_i. If transa = rocblas_operation_none, then, the leading n-by-k part of the array contains each matrix A_i, otherwise the leading k-by-n part of the array contains each matrix A_i.**lda**–**[in]**[rocblas_int] specifies the leading dimension of each A_i. If transA == rocblas_operation_none, must have lda >= max(1, n), otherwise, must have lda >= max(1, k).**B**–**[in]**device array of device pointers storing each matrix B_i. If transB = rocblas_operation_none, then, the leading k-by-n part of the array contains each matrix B_i, otherwise the leading n-by-k part of the array contains each matrix B_i.**ldb**–**[in]**[rocblas_int] specifies the leading dimension of each B_i. If transB == rocblas_operation_none, must have ldb >= max(1, k), otherwise, must have ldb >= max(1, n).**beta**–**[in]**device pointer or host pointer specifying the scalar beta.**C**–**[inout]**device array of device pointers storing each matrix C_i. If uplo == rocblas_fill_upper, the upper triangular part of the leading n-by-n array contains each matrix C_i, otherwise the lower triangular part of the leading n-by-n array contains each matrix C_i.**ldc**–**[in]**[rocblas_int] specifies the leading dimension of each C_i. Must have ldc >= max(1, n).**batch_count**–**[in]**[rocblas_int] number of gemm operations in the batch.



The `gemmt_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_sgemmt_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const float *alpha, const float *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_a, const float *B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_b, const float *beta, float *C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_c,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv430rocblas_sgemmt_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation17rocblas_operation11rocblas_int11rocblas_intPKfPKf11rocblas_int14rocblas_stridePKf11rocblas_int14rocblas_stridePKfPf11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_dgemmt_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const double *alpha, const double *A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_a, const double *B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_b, const double *beta, double *C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_c,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv430rocblas_dgemmt_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation17rocblas_operation11rocblas_int11rocblas_intPKdPKd11rocblas_int14rocblas_stridePKd11rocblas_int14rocblas_stridePKdPd11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_cgemmt_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*alpha, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_a, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_b, const[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*beta,[rocblas_float_complex](datatypes.html#_CPPv421rocblas_float_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_c,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv430rocblas_cgemmt_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation17rocblas_operation11rocblas_int11rocblas_intPK21rocblas_float_complexPK21rocblas_float_complex11rocblas_int14rocblas_stridePK21rocblas_float_complex11rocblas_int14rocblas_stridePK21rocblas_float_complexP21rocblas_float_complex11rocblas_int14rocblas_stride11rocblas_int)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_zgemmt_strided_batched([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_fill](enumerations.html#_CPPv412rocblas_fill)uplo,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transA,[rocblas_operation](enumerations.html#_CPPv417rocblas_operation)transB,[rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)k, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*alpha, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*A,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_a, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*B,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_b, const[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*beta,[rocblas_double_complex](datatypes.html#_CPPv422rocblas_double_complex)*C,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldc,[rocblas_stride](datatypes.html#_CPPv414rocblas_stride)stride_c,[rocblas_int](datatypes.html#_CPPv411rocblas_int)batch_count)[#](#_CPPv430rocblas_zgemmt_strided_batched14rocblas_handle12rocblas_fill17rocblas_operation17rocblas_operation11rocblas_int11rocblas_intPK22rocblas_double_complexPK22rocblas_double_complex11rocblas_int14rocblas_stridePK22rocblas_double_complex11rocblas_int14rocblas_stridePK22rocblas_double_complexP22rocblas_double_complex11rocblas_int14rocblas_stride11rocblas_int) **BLAS Level 3 API**gemmt_strided_batched performs matrix-matrix operations and updates the upper or lower triangular part of the result matrix:

C_i = alpha*op( A_i )*op( B_i ) + beta*C_i, for i = 1, ..., batch_count, where op( X ) is one of op( X ) = X or op( X ) = X**T or op( X ) = X**H, alpha and beta are scalars. A, B are general matrices and C is either an upper or lower triangular matrix, with op( A ) an n by k by batch_count strided_batched matrix, op( B ) an k by n by batch_count strided_batched matrix and C an n by n by batch_count strided_batched matrix.

- Parameters:
**handle**–**[in]**[rocblas_handle] handle to the rocblas library context queue.**uplo**–**[in]**[rocblas_fill]rocblas_fill_upper: C is an upper triangular matrix

rocblas_fill_lower: C is a lower triangular matrix


**transA**–**[in]**[rocblas_operation]rocblas_operation_none: op(A_i) = A_i.

rocblas_operation_transpose: op(A_i) = A_i^T

rocblas_operation_conjugate_transpose: op(A_i) = A_i^H


**transB**–**[in]**[rocblas_operation]rocblas_operation_none: op(B_i) = B_i.

rocblas_operation_transpose: op(B_i) = B_i^T

rocblas_operation_conjugate_transpose: op(B_i) = B_i^H


**n**–**[in]**[rocblas_int] number or rows of matrices op( A_i ), columns of op( B_i ), and (rows, columns) of C_i.**k**–**[in]**[rocblas_int] number of rows of matrices op( B_i ) and columns of op( A_i ).**alpha**–**[in]**device pointer or host pointer specifying the scalar alpha.**A**–**[in]**device array of device pointers storing each matrix A_i. If transa = rocblas_operation_none, then, the leading n-by-k part of the array contains each matrix A_i, otherwise the leading k-by-n part of the array contains each matrix A_i.**lda**–**[in]**[rocblas_int] specifies the leading dimension of each A_i. If transA == rocblas_operation_none, must have lda >= max(1, n), otherwise, must have lda >= max(1, k).**stride_a**–**[in]**[rocblas_stride] stride from the start of one A_i matrix to the next A_(i + 1).**B**–**[in]**device array of device pointers storing each matrix B_i. If transB = rocblas_operation_none, then, the leading k-by-n part of the array contains each matrix B_i, otherwise the leading n-by-k part of the array contains each matrix B_i.**ldb**–**[in]**[rocblas_int] specifies the leading dimension of each B_i. If transB == rocblas_operation_none, must have ldb >= max(1, k), otherwise, must have ldb >= max(1, n).**stride_b**–**[in]**[rocblas_stride] stride from the start of one B_i matrix to the next B_(i + 1).**beta**–**[in]**device pointer or host pointer specifying the scalar beta.**C**–**[inout]**device array of device pointers storing each matrix C_i. If uplo == rocblas_fill_upper, the upper triangular part of the leading n-by-n array contains each matrix C_i, otherwise the lower triangular part of the leading n-by-n array contains each matrix C_i.**ldc**–**[in]**[rocblas_int] specifies the leading dimension of each C_i. Must have ldc >= max(1, n).**stride_c**–**[in]**[rocblas_stride] stride from the start of one C_i matrix to the next C_(i + 1).**batch_count**–**[in]**[rocblas_int] number of gemm operatons in the batch.



The `gemmt_strided_batched`

functions support the `_64`

interface. Parameter `n`

larger than `int32_t`

max value is not currently supported.
See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.
