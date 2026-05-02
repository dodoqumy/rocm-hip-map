---
title: "rocBLAS helper functions &#8212; rocBLAS 5.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/helper-functions.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:05:31.345670+00:00
content_hash: "6deaadc980b6ebe0"
---

# rocBLAS helper functions[#](#rocblas-helper-functions)

## Auxiliary functions[#](#auxiliary-functions)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_create_handle([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)*handle)[#](#_CPPv421rocblas_create_handleP14rocblas_handle) Create handle.


-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_destroy_handle([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle)[#](#_CPPv422rocblas_destroy_handle14rocblas_handle) Destroy handle.


-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_set_stream([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle, hipStream_t stream)[#](#_CPPv418rocblas_set_stream14rocblas_handle11hipStream_t) Set stream for handle.


-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_get_stream([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle, hipStream_t *stream)[#](#_CPPv418rocblas_get_stream14rocblas_handleP11hipStream_t) Get stream [0] from handle.


-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_set_pointer_mode([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_pointer_mode](enumerations.html#_CPPv420rocblas_pointer_mode)pointer_mode)[#](#_CPPv424rocblas_set_pointer_mode14rocblas_handle20rocblas_pointer_mode) Set rocblas_pointer_mode.


-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_get_pointer_mode([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_pointer_mode](enumerations.html#_CPPv420rocblas_pointer_mode)*pointer_mode)[#](#_CPPv424rocblas_get_pointer_mode14rocblas_handleP20rocblas_pointer_mode) Get rocblas_pointer_mode.


-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_set_atomics_mode([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_atomics_mode](enumerations.html#_CPPv420rocblas_atomics_mode)atomics_mode)[#](#_CPPv424rocblas_set_atomics_mode14rocblas_handle20rocblas_atomics_mode) Set rocblas_atomics_mode.

Some rocBLAS functions may have implementations which use atomic operations to increase performance. By using atomic operations, results are not guaranteed to be identical between multiple runs. Results will be accurate with or without atomic operations. Atomic operations in rocBLAS are turned off by default. They can be turned on or off for a handle by calling rocblas_set_atomics_mode.


-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_get_atomics_mode([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle,[rocblas_atomics_mode](enumerations.html#_CPPv420rocblas_atomics_mode)*atomics_mode)[#](#_CPPv424rocblas_get_atomics_mode14rocblas_handleP20rocblas_atomics_mode) Get rocblas_atomics_mode.


-
[rocblas_pointer_mode](enumerations.html#_CPPv420rocblas_pointer_mode)rocblas_pointer_to_mode(void *ptr)[#](#_CPPv423rocblas_pointer_to_modePv) Indicates whether the pointer is on the host or device.


-
void rocblas_initialize(void)
[#](#_CPPv418rocblas_initializev) Initialize rocBLAS on the current HIP device, to avoid costly startup time at the first call on that device.

Calling


allows upfront initialization including device specific kernel setup. Otherwise this function is automatically called on the first function call that requires these initializations (mainly GEMM).[rocblas_initialize()](#rocblas-functions_8h_1a46196e7facb57320a4518920b7c75b20)

-
const char *rocblas_status_to_string(
[rocblas_status](enumerations.html#_CPPv414rocblas_status)status)[#](#_CPPv424rocblas_status_to_string14rocblas_status) BLAS Auxiliary API

rocblas_status_to_string

Returns string representing rocblas_status value

- Parameters:
**status**–**[in]**[rocblas_status] rocBLAS status to convert to string


-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_set_vector([rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)elem_size, const void *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, void *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy)[#](#_CPPv418rocblas_set_vector11rocblas_int11rocblas_intPKv11rocblas_intPv11rocblas_int) Copy vector from host to device.

- Parameters:
**n**–**[in]**[rocblas_int] number of elements in the vector**elem_size**–**[in]**[rocblas_int] number of bytes per element in the matrix**x**–**[in]**pointer to vector on the host**incx**–**[in]**[rocblas_int] specifies the increment for the elements of the vector**y**–**[out]**pointer to vector on the device**incy**–**[in]**[rocblas_int] specifies the increment for the elements of the vector



-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_get_vector([rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)elem_size, const void *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, void *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy)[#](#_CPPv418rocblas_get_vector11rocblas_int11rocblas_intPKv11rocblas_intPv11rocblas_int) Copy vector from device to host.

- Parameters:
**n**–**[in]**[rocblas_int] number of elements in the vector**elem_size**–**[in]**[rocblas_int] number of bytes per element in the matrix**x**–**[in]**pointer to vector on the device**incx**–**[in]**[rocblas_int] specifies the increment for the elements of the vector**y**–**[out]**pointer to vector on the host**incy**–**[in]**[rocblas_int] specifies the increment for the elements of the vector



-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_set_vector_async([rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)elem_size, const void *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, void *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy, hipStream_t stream)[#](#_CPPv424rocblas_set_vector_async11rocblas_int11rocblas_intPKv11rocblas_intPv11rocblas_int11hipStream_t) Asynchronously copy vector from host to device.

rocblas_set_vector_async copies a vector from pinned host memory to device memory asynchronously. Memory on the host must be allocated with hipHostMalloc or the transfer will be synchronous.

- Parameters:
**n**–**[in]**[rocblas_int] number of elements in the vector**elem_size**–**[in]**[rocblas_int] number of bytes per element in the matrix**x**–**[in]**pointer to vector on the host**incx**–**[in]**[rocblas_int] specifies the increment for the elements of the vector**y**–**[out]**pointer to vector on the device**incy**–**[in]**[rocblas_int] specifies the increment for the elements of the vector**stream**–**[in]**specifies the stream into which this transfer request is queued



-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_get_vector_async([rocblas_int](datatypes.html#_CPPv411rocblas_int)n,[rocblas_int](datatypes.html#_CPPv411rocblas_int)elem_size, const void *x,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incx, void *y,[rocblas_int](datatypes.html#_CPPv411rocblas_int)incy, hipStream_t stream)[#](#_CPPv424rocblas_get_vector_async11rocblas_int11rocblas_intPKv11rocblas_intPv11rocblas_int11hipStream_t) Asynchronously copy vector from device to host.

rocblas_get_vector_async copies a vector from pinned host memory to device memory asynchronously. Memory on the host must be allocated with hipHostMalloc or the transfer will be synchronous.

- Parameters:
**n**–**[in]**[rocblas_int] number of elements in the vector**elem_size**–**[in]**[rocblas_int] number of bytes per element in the matrix**x**–**[in]**pointer to vector on the device**incx**–**[in]**[rocblas_int] specifies the increment for the elements of the vector**y**–**[out]**pointer to vector on the host**incy**–**[in]**[rocblas_int] specifies the increment for the elements of the vector**stream**–**[in]**specifies the stream into which this transfer request is queued



-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_set_matrix([rocblas_int](datatypes.html#_CPPv411rocblas_int)rows,[rocblas_int](datatypes.html#_CPPv411rocblas_int)cols,[rocblas_int](datatypes.html#_CPPv411rocblas_int)elem_size, const void *a,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, void *b,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb)[#](#_CPPv418rocblas_set_matrix11rocblas_int11rocblas_int11rocblas_intPKv11rocblas_intPv11rocblas_int) Copy matrix from host to device.

- Parameters:
**rows**–**[in]**[rocblas_int] number of rows in matrices**cols**–**[in]**[rocblas_int] number of columns in matrices**elem_size**–**[in]**[rocblas_int] number of bytes per element in the matrix**a**–**[in]**pointer to matrix on the host**lda**–**[in]**[rocblas_int] specifies the leading dimension of A, lda >= rows**b**–**[out]**pointer to matrix on the GPU**ldb**–**[in]**[rocblas_int] specifies the leading dimension of B, ldb >= rows



-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_get_matrix([rocblas_int](datatypes.html#_CPPv411rocblas_int)rows,[rocblas_int](datatypes.html#_CPPv411rocblas_int)cols,[rocblas_int](datatypes.html#_CPPv411rocblas_int)elem_size, const void *a,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, void *b,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb)[#](#_CPPv418rocblas_get_matrix11rocblas_int11rocblas_int11rocblas_intPKv11rocblas_intPv11rocblas_int) Copy matrix from device to host.

- Parameters:
**rows**–**[in]**[rocblas_int] number of rows in matrices**cols**–**[in]**[rocblas_int] number of columns in matrices**elem_size**–**[in]**[rocblas_int] number of bytes per element in the matrix**a**–**[in]**pointer to matrix on the GPU**lda**–**[in]**[rocblas_int] specifies the leading dimension of A, lda >= rows**b**–**[out]**pointer to matrix on the host**ldb**–**[in]**[rocblas_int] specifies the leading dimension of B, ldb >= rows



-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_set_matrix_async([rocblas_int](datatypes.html#_CPPv411rocblas_int)rows,[rocblas_int](datatypes.html#_CPPv411rocblas_int)cols,[rocblas_int](datatypes.html#_CPPv411rocblas_int)elem_size, const void *a,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, void *b,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, hipStream_t stream)[#](#_CPPv424rocblas_set_matrix_async11rocblas_int11rocblas_int11rocblas_intPKv11rocblas_intPv11rocblas_int11hipStream_t) Asynchronously copy matrix from host to device.

rocblas_set_matrix_async copies a matrix from pinned host memory to device memory asynchronously. Memory on the host must be allocated with hipHostMalloc or the transfer will be synchronous.

- Parameters:
**rows**–**[in]**[rocblas_int] number of rows in matrices**cols**–**[in]**[rocblas_int] number of columns in matrices**elem_size**–**[in]**[rocblas_int] number of bytes per element in the matrix**a**–**[in]**pointer to matrix on the host**lda**–**[in]**[rocblas_int] specifies the leading dimension of A, lda >= rows**b**–**[out]**pointer to matrix on the GPU**ldb**–**[in]**[rocblas_int] specifies the leading dimension of B, ldb >= rows**stream**–**[in]**specifies the stream into which this transfer request is queued



-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_get_matrix_async([rocblas_int](datatypes.html#_CPPv411rocblas_int)rows,[rocblas_int](datatypes.html#_CPPv411rocblas_int)cols,[rocblas_int](datatypes.html#_CPPv411rocblas_int)elem_size, const void *a,[rocblas_int](datatypes.html#_CPPv411rocblas_int)lda, void *b,[rocblas_int](datatypes.html#_CPPv411rocblas_int)ldb, hipStream_t stream)[#](#_CPPv424rocblas_get_matrix_async11rocblas_int11rocblas_int11rocblas_intPKv11rocblas_intPv11rocblas_int11hipStream_t) asynchronously copy matrix from device to host

rocblas_get_matrix_async copies a matrix from device memory to pinned host memory asynchronously. Memory on the host must be allocated with hipHostMalloc or the transfer will be synchronous.

- Parameters:
**rows**–**[in]**[rocblas_int] number of rows in matrices**cols**–**[in]**[rocblas_int] number of columns in matrices**elem_size**–**[in]**[rocblas_int] number of bytes per element in the matrix**a**–**[in]**pointer to matrix on the GPU**lda**–**[in]**[rocblas_int] specifies the leading dimension of A, lda >= rows**b**–**[out]**pointer to matrix on the host**ldb**–**[in]**[rocblas_int] specifies the leading dimension of B, ldb >= rows**stream**–**[in]**specifies the stream into which this transfer request is queued



The set/get_vector and set/get_matrix functions including their async forms support the `_64`

interface. See the [ILP64 interface](../conceptual/rocblas-design-notes.html#ilp64-api) section.

## Device memory allocation functions[#](#device-memory-allocation-functions)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_start_device_memory_size_query([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle)[#](#_CPPv438rocblas_start_device_memory_size_query14rocblas_handle) Indicates that subsequent rocBLAS kernel calls should collect the optimal device memory size in bytes for their given kernel arguments and keep track of the maximum. Each kernel call can reuse temporary device memory on the same stream so the maximum is collected. Returns rocblas_status_size_query_mismatch if another size query is already in progress; returns rocblas_status_success otherwise

- Parameters:
**handle**–**[in]**rocblas handle


-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_stop_device_memory_size_query([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle, size_t *size)[#](#_CPPv437rocblas_stop_device_memory_size_query14rocblas_handleP6size_t) Stops collecting optimal device memory size information. Returns rocblas_status_size_query_mismatch if a collection is not underway; rocblas_status_invalid_handle if handle is nullptr; rocblas_status_invalid_pointer if size is nullptr; rocblas_status_success otherwise

- Parameters:
**handle**–**[in]**rocblas handle**size**–**[out]**maximum of the optimal sizes collected



-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_get_device_memory_size([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle, size_t *size)[#](#_CPPv430rocblas_get_device_memory_size14rocblas_handleP6size_t) Gets the current device memory size for the handle. Returns rocblas_status_invalid_handle if handle is nullptr; rocblas_status_invalid_pointer if size is nullptr; rocblas_status_success otherwise

- Parameters:
**handle**–**[in]**rocblas handle**size**–**[out]**current device memory size for the handle



-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_set_workspace([rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle, void *addr, size_t size)[#](#_CPPv421rocblas_set_workspace14rocblas_handlePv6size_t) Sets the device workspace for the handle to use.

Any previously allocated device memory managed by the handle is freed.

Returns rocblas_status_invalid_handle if handle is nullptr; rocblas_status_success otherwise

- Parameters:
**handle**–**[in]**rocblas handle**addr**–**[in]**address of workspace memory**size**–**[in]**size of workspace memory



-
bool rocblas_is_managing_device_memory(
[rocblas_handle](datatypes.html#_CPPv414rocblas_handle)handle)[#](#_CPPv433rocblas_is_managing_device_memory14rocblas_handle) Returns true when device memory in handle is managed by rocBLAS

- Parameters:
**handle**–**[in]**rocblas handle


For more detailed information, see the [Device memory allocation in rocBLAS](memory-alloc.html#device-memory-allocation-usage) and [Device memory allocation](../how-to/Programmers_Guide.html#device-memory-allocation-in-detail) sections.

## Build information functions[#](#build-information-functions)

-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_get_version_string_size(size_t *len)[#](#_CPPv431rocblas_get_version_string_sizeP6size_t) Queries the minimum buffer size for a successful call to

[rocblas_get_version_string](#rocblas-functions_8h_1ac4be6138c305ffe1c42ec3816f527466).- Parameters:
**len**–**[out]**pointer to size_t for storing the length


-
[rocblas_status](enumerations.html#_CPPv414rocblas_status)rocblas_get_version_string(char *buf, size_t len)[#](#_CPPv426rocblas_get_version_stringPc6size_t) Loads char* buf with the rocblas library version. size_t len is the maximum length of char* buf.

- Parameters:
**buf**–**[inout]**pointer to buffer for version string**len**–**[in]**length of buf
