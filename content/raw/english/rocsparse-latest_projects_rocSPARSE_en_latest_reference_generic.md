---
title: "Sparse generic functions &#8212; rocSPARSE 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocSPARSE/en/latest/reference/generic.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:17:10.526830+00:00
content_hash: "80e71ad49345526c"
---

# Sparse generic functions[#](#sparse-generic-functions)

This module contains all sparse generic routines.

The sparse generic routines describe some of the most common operations that manipulate sparse matrices and vectors. The generic API is more flexible than the other rocSPARSE APIs because it is easy to set different index types, data types, and compute types. For some generic routines, for example, SpMV, the generic API also lets users select different algorithms which have different performance characteristics depending on the sparse matrix being operated on.

## rocsparse_axpby()[#](#rocsparse-axpby)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_axpby([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, const void *alpha,[rocsparse_const_spvec_descr](types.html#_CPPv427rocsparse_const_spvec_descr)x, const void *beta,[rocsparse_dnvec_descr](types.html#_CPPv421rocsparse_dnvec_descr)y)[#](#_CPPv415rocsparse_axpby16rocsparse_handlePKv27rocsparse_const_spvec_descrPKv21rocsparse_dnvec_descr) Scale a sparse vector and add it to a scaled dense vector.

`rocsparse_axpby`

multiplies the sparse vector \(x\) with scalar \(\alpha\) and adds the result to the dense vector \(y\) that is multiplied with scalar \(\beta\), such that\[ y := \alpha \cdot x + \beta \cdot y \]for(i = 0; i < size; ++i) { y[i] = beta * y[i] } for(i = 0; i < nnz; ++i) { y[x_ind[i]] += alpha * x_val[i] }

`rocsparse_axpby`

supports the following uniform precision data types for the sparse and dense vectors x and y and compute types for the scalars \(\alpha\) and \(\beta\).**Uniform Precisions:**X / Y / compute_type

rocsparse_datatype_f32_r

rocsparse_datatype_f64_r

rocsparse_datatype_f32_c

rocsparse_datatype_f64_c

**Mixed precisions:**X / Y

compute_type

rocsparse_datatype_f16_r

rocsparse_datatype_f32_r

rocsparse_datatype_bf16_r

rocsparse_datatype_f32_r

**Example**int main() { // Number of non-zeros of the sparse vector int nnz = 3; // Size of sparse and dense vector int size = 9; // Sparse index vector std::vector<int> hx_ind = {0, 3, 5}; // Sparse value vector std::vector<float> hx_val = {1.0f, 2.0f, 3.0f}; // Dense vector std::vector<float> hy = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f, 9.0f}; // Scalar alpha float alpha = 3.7f; // Scalar beta float beta = 1.2f; // Offload data to device int* dx_ind; float* dx_val; float* dy; HIP_CHECK(hipMalloc(&dx_ind, sizeof(int) * nnz)); HIP_CHECK(hipMalloc(&dx_val, sizeof(float) * nnz)); HIP_CHECK(hipMalloc(&dy, sizeof(float) * size)); HIP_CHECK(hipMemcpy(dx_ind, hx_ind.data(), sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dx_val, hx_val.data(), sizeof(float) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dy, hy.data(), sizeof(float) * size, hipMemcpyHostToDevice)); rocsparse_handle handle; rocsparse_spvec_descr vecX; rocsparse_dnvec_descr vecY; rocsparse_indextype idx_type = rocsparse_indextype_i32; rocsparse_datatype data_type = rocsparse_datatype_f32_r; rocsparse_index_base idx_base = rocsparse_index_base_zero; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Create sparse vector X ROCSPARSE_CHECK(rocsparse_create_spvec_descr( &vecX, size, nnz, dx_ind, dx_val, idx_type, idx_base, data_type)); // Create dense vector Y ROCSPARSE_CHECK(rocsparse_create_dnvec_descr(&vecY, size, dy, data_type)); // Call axpby to perform y = beta * y + alpha * x ROCSPARSE_CHECK(rocsparse_axpby(handle, &alpha, vecX, &beta, vecY)); ROCSPARSE_CHECK(rocsparse_dnvec_get_values(vecY, (void**)&dy)); // Copy result back to host HIP_CHECK(hipMemcpy(hy.data(), dy, sizeof(float) * size, hipMemcpyDeviceToHost)); std::cout << "y" << std::endl; for(size_t i = 0; i < hy.size(); ++i) { std::cout << hy[i] << " "; } std::cout << std::endl; // Clear rocSPARSE ROCSPARSE_CHECK(rocsparse_destroy_spvec_descr(vecX)); ROCSPARSE_CHECK(rocsparse_destroy_dnvec_descr(vecY)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); // Clear device memory HIP_CHECK(hipFree(dx_ind)); HIP_CHECK(hipFree(dx_val)); HIP_CHECK(hipFree(dy)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**alpha**–**[in]**scalar \(\alpha\).**x**–**[in]**sparse matrix descriptor.**beta**–**[in]**scalar \(\beta\).**y**–**[inout]**dense matrix descriptor.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`alpha`

,`x`

,`beta`

or`y`

pointer is invalid.



## rocsparse_gather()[#](#rocsparse-gather)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_gather([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_const_dnvec_descr](types.html#_CPPv427rocsparse_const_dnvec_descr)y,[rocsparse_spvec_descr](types.html#_CPPv421rocsparse_spvec_descr)x)[#](#_CPPv416rocsparse_gather16rocsparse_handle27rocsparse_const_dnvec_descr21rocsparse_spvec_descr) Gather elements from a dense vector and store them into a sparse vector.

`rocsparse_gather`

gathers the elements from the dense vector \(y\) and stores them in the sparse vector \(x\).for(i = 0; i < nnz; ++i) { x_val[i] = y[x_ind[i]]; }

`rocsparse_gather`

supports the following uniform precision data types for the sparse and dense vectors x and y.**Uniform Precisions:**X / Y

rocsparse_datatype_i8_r

rocsparse_datatype_f16_r

rocsparse_datatype_bf16_r

rocsparse_datatype_f32_r

rocsparse_datatype_f64_r

rocsparse_datatype_f32_c

rocsparse_datatype_f64_c

**Example**int main() { // Number of non-zeros of the sparse vector int nnz = 3; // Size of sparse and dense vector int size = 9; // Sparse index vector std::vector<int> hx_ind = {0, 3, 5}; // Dense vector std::vector<float> hy = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f, 9.0f}; // Offload data to device int* dx_ind; float* dx_val; float* dy; HIP_CHECK(hipMalloc(&dx_ind, sizeof(int) * nnz)); HIP_CHECK(hipMalloc(&dx_val, sizeof(float) * nnz)); HIP_CHECK(hipMalloc(&dy, sizeof(float) * size)); HIP_CHECK(hipMemcpy(dx_ind, hx_ind.data(), sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dy, hy.data(), sizeof(float) * size, hipMemcpyHostToDevice)); rocsparse_handle handle; rocsparse_spvec_descr vecX; rocsparse_dnvec_descr vecY; rocsparse_indextype idx_type = rocsparse_indextype_i32; rocsparse_datatype data_type = rocsparse_datatype_f32_r; rocsparse_index_base idx_base = rocsparse_index_base_zero; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Create sparse vector X ROCSPARSE_CHECK(rocsparse_create_spvec_descr( &vecX, size, nnz, dx_ind, dx_val, idx_type, idx_base, data_type)); // Create dense vector Y ROCSPARSE_CHECK(rocsparse_create_dnvec_descr(&vecY, size, dy, data_type)); // Call axpby to perform gather ROCSPARSE_CHECK(rocsparse_gather(handle, vecY, vecX)); ROCSPARSE_CHECK(rocsparse_spvec_get_values(vecX, (void**)&dx_val)); // Copy result back to host std::vector<float> hx_val(nnz, 0.0f); HIP_CHECK(hipMemcpy(hx_val.data(), dx_val, sizeof(float) * nnz, hipMemcpyDeviceToHost)); std::cout << "x" << std::endl; for(size_t i = 0; i < hx_val.size(); ++i) { std::cout << hx_val[i] << " "; } std::cout << std::endl; // Clear rocSPARSE ROCSPARSE_CHECK(rocsparse_destroy_spvec_descr(vecX)); ROCSPARSE_CHECK(rocsparse_destroy_dnvec_descr(vecY)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); // Clear device memory HIP_CHECK(hipFree(dx_ind)); HIP_CHECK(hipFree(dx_val)); HIP_CHECK(hipFree(dy)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**y**–**[in]**dense vector \(y\).**x**–**[out]**sparse vector \(x\).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`x`

or`y`

pointer is invalid.



## rocsparse_scatter()[#](#rocsparse-scatter)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scatter([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_const_spvec_descr](types.html#_CPPv427rocsparse_const_spvec_descr)x,[rocsparse_dnvec_descr](types.html#_CPPv421rocsparse_dnvec_descr)y)[#](#_CPPv417rocsparse_scatter16rocsparse_handle27rocsparse_const_spvec_descr21rocsparse_dnvec_descr) Scatter elements from a sparse vector into a dense vector.

`rocsparse_scatter`

scatters the elements from the sparse vector \(x\) in the dense vector \(y\).for(i = 0; i < nnz; ++i) { y[x_ind[i]] = x_val[i]; }

`rocsparse_scatter`

supports the following uniform precision data types for the sparse and dense vectors x and y.**Uniform Precisions:**X / Y

rocsparse_datatype_i8_r

rocsparse_datatype_f16_r

rocsparse_datatype_bf16_r

rocsparse_datatype_f32_r

rocsparse_datatype_f64_r

rocsparse_datatype_f32_c

rocsparse_datatype_f64_c

**Example**int main() { // Number of non-zeros of the sparse vector int nnz = 3; // Size of sparse and dense vector int size = 9; // Sparse index vector std::vector<int> hx_ind = {0, 3, 5}; // Sparse value vector std::vector<float> hx_val = {1.0f, 2.0f, 3.0f}; // Dense vector std::vector<float> hy = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f, 9.0f}; // Offload data to device int* dx_ind; float* dx_val; float* dy; HIP_CHECK(hipMalloc(&dx_ind, sizeof(int) * nnz)); HIP_CHECK(hipMalloc(&dx_val, sizeof(float) * nnz)); HIP_CHECK(hipMalloc(&dy, sizeof(float) * size)); HIP_CHECK(hipMemcpy(dx_ind, hx_ind.data(), sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dx_val, hx_val.data(), sizeof(float) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dy, hy.data(), sizeof(float) * size, hipMemcpyHostToDevice)); rocsparse_handle handle; rocsparse_spvec_descr vecX; rocsparse_dnvec_descr vecY; rocsparse_indextype idx_type = rocsparse_indextype_i32; rocsparse_datatype data_type = rocsparse_datatype_f32_r; rocsparse_index_base idx_base = rocsparse_index_base_zero; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Create sparse vector X ROCSPARSE_CHECK(rocsparse_create_spvec_descr( &vecX, size, nnz, dx_ind, dx_val, idx_type, idx_base, data_type)); // Create dense vector Y ROCSPARSE_CHECK(rocsparse_create_dnvec_descr(&vecY, size, dy, data_type)); // Call axpby to perform scatter ROCSPARSE_CHECK(rocsparse_scatter(handle, vecX, vecY)); ROCSPARSE_CHECK(rocsparse_dnvec_get_values(vecY, (void**)&dy)); // Copy result back to host HIP_CHECK(hipMemcpy(hy.data(), dy, sizeof(float) * size, hipMemcpyDeviceToHost)); std::cout << "y" << std::endl; for(size_t i = 0; i < hy.size(); ++i) { std::cout << hy[i] << " "; } std::cout << std::endl; // Clear rocSPARSE ROCSPARSE_CHECK(rocsparse_destroy_spvec_descr(vecX)); ROCSPARSE_CHECK(rocsparse_destroy_dnvec_descr(vecY)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); // Clear device memory HIP_CHECK(hipFree(dx_ind)); HIP_CHECK(hipFree(dx_val)); HIP_CHECK(hipFree(dy)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**x**–**[in]**sparse vector \(x\).**y**–**[out]**dense vector \(y\).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`x`

or`y`

pointer is invalid.



## rocsparse_rot()[#](#rocsparse-rot)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_rot([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, const void *c, const void *s,[rocsparse_spvec_descr](types.html#_CPPv421rocsparse_spvec_descr)x,[rocsparse_dnvec_descr](types.html#_CPPv421rocsparse_dnvec_descr)y)[#](#_CPPv413rocsparse_rot16rocsparse_handlePKvPKv21rocsparse_spvec_descr21rocsparse_dnvec_descr) Apply Givens rotation to a dense and a sparse vector.

`rocsparse_rot`

applies the Givens rotation matrix \(G\) to the sparse vector \(x\) and the dense vector \(y\), where\[\begin{split} G = \begin{pmatrix} c & s \\ -s & c \end{pmatrix} \end{split}\]for(i = 0; i < nnz; ++i) { x_tmp = x_val[i]; y_tmp = y[x_ind[i]]; x_val[i] = c * x_tmp + s * y_tmp; y[x_ind[i]] = c * y_tmp - s * x_tmp; }

`rocsparse_rot`

supports the following uniform precision data types for the sparse and dense vectors x and y and compute types for the scalars \(c\) and \(s\).**Uniform Precisions:**X / Y / compute_type

rocsparse_datatype_f32_r

rocsparse_datatype_f64_r

rocsparse_datatype_f32_c

rocsparse_datatype_f64_c

**Example**int main() { // Number of non-zeros of the sparse vector int nnz = 3; // Size of sparse and dense vector int size = 9; // Sparse index vector std::vector<int> hx_ind = {0, 3, 5}; // Sparse value vector std::vector<float> hx_val = {1.0f, 2.0f, 3.0f}; // Dense vector std::vector<float> hy = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f, 9.0f}; // Scalar c float c = 3.7f; // Scalar s float s = 1.2f; // Offload data to device int* dx_ind; float* dx_val; float* dy; HIP_CHECK(hipMalloc(&dx_ind, sizeof(int) * nnz)); HIP_CHECK(hipMalloc(&dx_val, sizeof(float) * nnz)); HIP_CHECK(hipMalloc(&dy, sizeof(float) * size)); HIP_CHECK(hipMemcpy(dx_ind, hx_ind.data(), sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dx_val, hx_val.data(), sizeof(float) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dy, hy.data(), sizeof(float) * size, hipMemcpyHostToDevice)); rocsparse_handle handle; rocsparse_spvec_descr vecX; rocsparse_dnvec_descr vecY; rocsparse_indextype idx_type = rocsparse_indextype_i32; rocsparse_datatype data_type = rocsparse_datatype_f32_r; rocsparse_index_base idx_base = rocsparse_index_base_zero; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Create sparse vector X ROCSPARSE_CHECK(rocsparse_create_spvec_descr( &vecX, size, nnz, dx_ind, dx_val, idx_type, idx_base, data_type)); // Create dense vector Y ROCSPARSE_CHECK(rocsparse_create_dnvec_descr(&vecY, size, dy, data_type)); // Call rot ROCSPARSE_CHECK(rocsparse_rot(handle, (void*)&c, (void*)&s, vecX, vecY)); ROCSPARSE_CHECK(rocsparse_spvec_get_values(vecX, (void**)&dx_val)); ROCSPARSE_CHECK(rocsparse_dnvec_get_values(vecY, (void**)&dy)); // Copy result back to host HIP_CHECK(hipMemcpy(hx_val.data(), dx_val, sizeof(float) * nnz, hipMemcpyDeviceToHost)); HIP_CHECK(hipMemcpy(hy.data(), dy, sizeof(float) * size, hipMemcpyDeviceToHost)); std::cout << "x" << std::endl; for(size_t i = 0; i < hx_val.size(); ++i) { std::cout << hx_val[i] << " "; } std::cout << std::endl; std::cout << "y" << std::endl; for(size_t i = 0; i < hy.size(); ++i) { std::cout << hy[i] << " "; } std::cout << std::endl; // Clear rocSPARSE ROCSPARSE_CHECK(rocsparse_destroy_spvec_descr(vecX)); ROCSPARSE_CHECK(rocsparse_destroy_dnvec_descr(vecY)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); // Clear device memory HIP_CHECK(hipFree(dx_ind)); HIP_CHECK(hipFree(dx_val)); HIP_CHECK(hipFree(dy)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**c**–**[in]**pointer to the cosine element of \(G\), can be on host or device.**s**–**[in]**pointer to the sine element of \(G\), can be on host or device.**x**–**[inout]**sparse vector \(x\).**y**–**[inout]**dense vector \(y\).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`c`

,`s`

,`x`

or`y`

pointer is invalid.



## rocsparse_spvv()[#](#rocsparse-spvv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_spvv([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_const_spvec_descr](types.html#_CPPv427rocsparse_const_spvec_descr)x,[rocsparse_const_dnvec_descr](types.html#_CPPv427rocsparse_const_dnvec_descr)y, void *result,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)compute_type, size_t *buffer_size, void *temp_buffer)[#](#_CPPv414rocsparse_spvv16rocsparse_handle19rocsparse_operation27rocsparse_const_spvec_descr27rocsparse_const_dnvec_descrPv18rocsparse_datatypeP6size_tPv) Sparse vector inner dot product.

`rocsparse_spvv`

computes the inner dot product of the sparse vector \(x\) with the dense vector \(y\), such that\[ \text{result} := op(x) \cdot y, \]with\[\begin{split} op(x) = \left\{ \begin{array}{ll} x, & \text{if trans == rocsparse_operation_none} \\ \bar{x}, & \text{if trans == rocsparse_operation_conjugate_transpose} \\ \end{array} \right. \end{split}\]result = 0; for(i = 0; i < nnz; ++i) { result += x_val[i] * y[x_ind[i]]; }

Performing the above operation involves two steps. First, the user calls

`rocsparse_spvv`

with`temp_buffer`

set to`nullptr`

which will return the required temporary buffer size in the parameter`buffer_size`

. The user then allocates this buffer. Finally, the user then completes the computation by calling`rocsparse_spvv`

a second time with the newly allocated buffer. Once the computation is complete, the user is free to deallocate the buffer.`rocsparse_spvv`

supports the following uniform and mixed precision data types for the sparse and dense vectors \(x\) and \(y\) and compute types for the scalar \(result\).**Uniform Precisions:**X / Y / compute_type

rocsparse_datatype_f32_r

rocsparse_datatype_f64_r

rocsparse_datatype_f32_c

rocsparse_datatype_f64_c

**Mixed precisions:**X / Y

compute_type / result

rocsparse_datatype_i8_r

rocsparse_datatype_i32_r

rocsparse_datatype_i8_r

rocsparse_datatype_f32_r

rocsparse_datatype_f16_r

rocsparse_datatype_f32_r

rocsparse_datatype_bf16_r

rocsparse_datatype_f32_r

**Example**int main() { // Number of non-zeros of the sparse vector int nnz = 3; // Size of sparse and dense vector int size = 9; // Sparse index vector std::vector<int> hx_ind = {0, 3, 5}; // Sparse value vector std::vector<float> hx_val = {1.0f, 2.0f, 3.0f}; // Dense vector std::vector<float> hy = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f, 9.0f}; // Offload data to device int* dx_ind; float* dx_val; float* dy; HIP_CHECK(hipMalloc(&dx_ind, sizeof(int) * nnz)); HIP_CHECK(hipMalloc(&dx_val, sizeof(float) * nnz)); HIP_CHECK(hipMalloc(&dy, sizeof(float) * size)); HIP_CHECK(hipMemcpy(dx_ind, hx_ind.data(), sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dx_val, hx_val.data(), sizeof(float) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dy, hy.data(), sizeof(float) * size, hipMemcpyHostToDevice)); rocsparse_handle handle; rocsparse_spvec_descr vecX; rocsparse_dnvec_descr vecY; rocsparse_indextype idx_type = rocsparse_indextype_i32; rocsparse_datatype data_type = rocsparse_datatype_f32_r; rocsparse_datatype compute_type = rocsparse_datatype_f32_r; rocsparse_operation trans = rocsparse_operation_none; rocsparse_index_base idx_base = rocsparse_index_base_zero; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Create sparse vector X ROCSPARSE_CHECK(rocsparse_create_spvec_descr( &vecX, size, nnz, dx_ind, dx_val, idx_type, idx_base, data_type)); // Create dense vector Y ROCSPARSE_CHECK(rocsparse_create_dnvec_descr(&vecY, size, dy, data_type)); // Obtain buffer size float hresult = 0.0f; size_t buffer_size; ROCSPARSE_CHECK( rocsparse_spvv(handle, trans, vecX, vecY, &hresult, compute_type, &buffer_size, nullptr)); void* temp_buffer; HIP_CHECK(hipMalloc(&temp_buffer, buffer_size)); // SpVV ROCSPARSE_CHECK(rocsparse_spvv( handle, trans, vecX, vecY, &hresult, compute_type, &buffer_size, temp_buffer)); HIP_CHECK(hipDeviceSynchronize()); // Clear rocSPARSE ROCSPARSE_CHECK(rocsparse_destroy_spvec_descr(vecX)); ROCSPARSE_CHECK(rocsparse_destroy_dnvec_descr(vecY)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); // Clear device memory HIP_CHECK(hipFree(dx_ind)); HIP_CHECK(hipFree(dx_val)); HIP_CHECK(hipFree(dy)); HIP_CHECK(hipFree(temp_buffer)); return 0; }


Note

This function writes the required allocation size (in bytes) to

`buffer_size`

and returns without performing the SpVV operation, when a nullptr is passed for`temp_buffer`

.Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**trans**–**[in]**sparse vector operation type.**x**–**[in]**sparse vector descriptor.**y**–**[in]**dense vector descriptor.**result**–**[out]**pointer to the result, can be host or device memory**compute_type**–**[in]**floating point precision for the SpVV computation.**buffer_size**–**[out]**number of bytes of the temporary storage buffer. buffer_size is set when`temp_buffer`

is nullptr.**temp_buffer**–**[in]**temporary storage buffer allocated by the user. When a nullptr is passed, the required allocation size (in bytes) is written to`buffer_size`

and function returns without performing the SpVV operation.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`x`

,`y`

,`result`

or`buffer_size`

pointer is invalid.**rocsparse_status_not_implemented**–`compute_type`

is currently not supported.



## rocsparse_spmv()[#](#rocsparse-spmv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_spmv([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans, const void *alpha,[rocsparse_const_spmat_descr](types.html#_CPPv427rocsparse_const_spmat_descr)mat,[rocsparse_const_dnvec_descr](types.html#_CPPv427rocsparse_const_dnvec_descr)x, const void *beta, const[rocsparse_dnvec_descr](types.html#_CPPv421rocsparse_dnvec_descr)y,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)compute_type,[rocsparse_spmv_alg](enumerations.html#_CPPv418rocsparse_spmv_alg)alg,[rocsparse_spmv_stage](enumerations.html#_CPPv420rocsparse_spmv_stage)stage, size_t *buffer_size, void *temp_buffer)[#](#_CPPv414rocsparse_spmv16rocsparse_handle19rocsparse_operationPKv27rocsparse_const_spmat_descr27rocsparse_const_dnvec_descrPKvK21rocsparse_dnvec_descr18rocsparse_datatype18rocsparse_spmv_alg20rocsparse_spmv_stageP6size_tPv) Sparse matrix vector multiplication.

`rocsparse_spmv`

multiplies the scalar \(\alpha\) with a sparse \(m \times n\) matrix \(op(A)\), defined in CSR, CSC, COO, COO (AoS), BSR, or ELL format, with the dense vector \(x\) and adds the result to the dense vector \(y\) that is multiplied by the scalar \(\beta\), such that\[ y := \alpha \cdot op(A) \cdot x + \beta \cdot y, \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if trans == rocsparse_operation_none} \\ A^T, & \text{if trans == rocsparse_operation_transpose} \\ A^H, & \text{if trans == rocsparse_operation_conjugate_transpose} \end{array} \right. \end{split}\]Performing the above operation involves multiple steps. First the user calls

`rocsparse_spmv`

with the stage parameter set to[rocsparse_spmv_stage_buffer_size](enumerations.html#rocsparse-types_8h_1ab2e40217ed05ec81a46674ecc91ce7bfafe51d3958904161b4b88990374760359)to determine the size of the required temporary storage buffer. The user then allocates this buffer and calls`rocsparse_spmv`

with the stage parameter set to[rocsparse_spmv_stage_preprocess](enumerations.html#rocsparse-types_8h_1ab2e40217ed05ec81a46674ecc91ce7bfaf2b1eae60f0e1ebfb31f6af522a7b4ab). Depending on the algorithm and sparse matrix format, this will perform analysis on the sparsity pattern of \(op(A)\). Finally the user completes the operation by calling`rocsparse_spmv`

with the stage parmeter set to[rocsparse_spmv_stage_compute](enumerations.html#rocsparse-types_8h_1ab2e40217ed05ec81a46674ecc91ce7bfad920d865c566abca9171faade375ba67). The buffer size, buffer allocation, and preprecess stages only need to be called once for a given sparse matrix \(op(A)\) while the computation stage can be repeatedly used with different \(x\) and \(y\) vectors. Once all calls to`rocsparse_spmv`

are complete, the temporary buffer can be deallocated.`rocsparse_spmv`

supports multiple different algorithms. These algorithms have different trade offs depending on the sparsity pattern of the matrix, whether or not the results need to be deterministic, and how many times the sparse-vector product will be performed.Algorithm

Deterministic

Preprocessing

Notes

rocsparse_spmv_alg_csr_rowsplit

Yes

No

Is best suited for matrices with all rows having a similar number of non-zeros. Can out perform adaptive and LRB algorithms in certain sparsity patterns. Will perform very poorly if some rows have few non-zeros and some rows have many non-zeros.

rocsparse_spmv_alg_csr_stream

Yes

No

[Deprecated] old name for rocsparse_spmv_alg_csr_rowsplit.

rocsparse_spmv_alg_csr_adaptive

No

Yes

Generally the fastest algorithm across all matrix sparsity patterns. This includes matrices that have some rows with many non-zeros and some rows with few non-zeros. Requires a lengthy preprocessing that needs to be amortized over many subsequent sparse vector products.

rocsparse_spmv_alg_csr_lrb

No

Yes

Like adaptive algorithm, generally performs well across all matrix sparsity patterns. Generally not as fast as adaptive algorithm, however uses a much faster pre-processing step. Good for when only a few number of sparse vector products will be performed.

rocsparse_spmv_alg_csr_nnzsplit

No

Yes

Like adaptive algorithm, generally performs well across all matrix sparsity patterns. Generally not as fast as adaptive algorithm but faster than LRB algorithm. It uses a much faster pre-processing step than LRB. Good for when the number of sparse vector products that will be performed is less than one hundred. If more products need to be computed, the adaptive algorithm is probably faster.

COO Algorithms

Deterministic

Preprocessing

Notes

rocsparse_spmv_alg_coo

Yes

Yes

Generally not as fast as atomic algorithm but is deterministic

rocsparse_spmv_alg_coo_atomic

No

No

Generally the fastest COO algorithm

ELL Algorithms

Deterministic

Preprocessing

Notes

rocsparse_spmv_alg_ell

Yes

No

BSR Algorithm

Deterministic

Preprocessing

Notes

rocsparse_spmv_alg_bsr

Yes

No

`rocsparse_spmv`

supports multiple combinations of data types and compute types. The tables below indicate the currently supported different data types that can be used for for the sparse matrix \(op(A)\) and the dense vectors \(x\) and \(y\) and the compute type for \(\alpha\) and \(\beta\). The advantage of using different data types is to save on memory bandwidth and storage when a user application allows while performing the actual computation in a higher precision.`rocsparse_spmv`

supports[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)and[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4)index precisions for storing the row pointer and column indices arrays of the sparse matrices.**Uniform Precisions:**A / X / Y / compute_type

rocsparse_datatype_f32_r

rocsparse_datatype_f64_r

rocsparse_datatype_f32_c

rocsparse_datatype_f64_c

**Mixed precisions:**A / X

Y

compute_type

rocsparse_datatype_i8_r

rocsparse_datatype_i32_r

rocsparse_datatype_i32_r

rocsparse_datatype_i8_r

rocsparse_datatype_f32_r

rocsparse_datatype_f32_r

rocsparse_datatype_f16_r

rocsparse_datatype_f32_r

rocsparse_datatype_f32_r

rocsparse_datatype_bf16_r

rocsparse_datatype_f32_r

rocsparse_datatype_f32_r

**Mixed-regular real precisions**A

X / Y / compute_type

rocsparse_datatype_f32_r

rocsparse_datatype_f64_r

rocsparse_datatype_f32_c

rocsparse_datatype_f64_c

**Mixed-regular Complex precisions**A

X / Y / compute_type

rocsparse_datatype_f32_r

rocsparse_datatype_f32_c

rocsparse_datatype_f64_r

rocsparse_datatype_f64_c


**Example**int main() { // 1 4 0 0 0 0 // A = 0 2 3 0 0 0 // 5 0 0 7 8 0 // 0 0 9 0 6 0 int m = 4; int n = 6; std::vector<int> hcsr_row_ptr = {0, 2, 4, 7, 9}; std::vector<int> hcsr_col_ind = {0, 1, 1, 2, 0, 3, 4, 2, 4}; std::vector<float> hcsr_val = {1, 4, 2, 3, 5, 7, 8, 9, 6}; std::vector<float> hx(n, 1.0f); std::vector<float> hy(m, 0.0f); // Scalar alpha float alpha = 3.7f; // Scalar beta float beta = 0.0f; int nnz = hcsr_row_ptr[m] - hcsr_row_ptr[0]; // Offload data to device int* dcsr_row_ptr; int* dcsr_col_ind; float* dcsr_val; float* dx; float* dy; HIP_CHECK(hipMalloc(&dcsr_row_ptr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc(&dcsr_col_ind, sizeof(int) * nnz)); HIP_CHECK(hipMalloc(&dcsr_val, sizeof(float) * nnz)); HIP_CHECK(hipMalloc(&dx, sizeof(float) * n)); HIP_CHECK(hipMalloc(&dy, sizeof(float) * m)); HIP_CHECK( hipMemcpy(dcsr_row_ptr, hcsr_row_ptr.data(), sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsr_col_ind, hcsr_col_ind.data(), sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsr_val, hcsr_val.data(), sizeof(float) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dx, hx.data(), sizeof(float) * n, hipMemcpyHostToDevice)); rocsparse_handle handle; rocsparse_spmat_descr matA; rocsparse_dnvec_descr vecX; rocsparse_dnvec_descr vecY; rocsparse_indextype row_idx_type = rocsparse_indextype_i32; rocsparse_indextype col_idx_type = rocsparse_indextype_i32; rocsparse_datatype data_type = rocsparse_datatype_f32_r; rocsparse_datatype compute_type = rocsparse_datatype_f32_r; rocsparse_index_base idx_base = rocsparse_index_base_zero; rocsparse_operation trans = rocsparse_operation_none; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Create sparse matrix A ROCSPARSE_CHECK(rocsparse_create_csr_descr(&matA, m, n, nnz, dcsr_row_ptr, dcsr_col_ind, dcsr_val, row_idx_type, col_idx_type, idx_base, data_type)); // Create dense vector X ROCSPARSE_CHECK(rocsparse_create_dnvec_descr(&vecX, n, dx, data_type)); // Create dense vector Y ROCSPARSE_CHECK(rocsparse_create_dnvec_descr(&vecY, m, dy, data_type)); // Call spmv to get buffer size size_t buffer_size; ROCSPARSE_CHECK(rocsparse_spmv(handle, trans, &alpha, matA, vecX, &beta, vecY, compute_type, rocsparse_spmv_alg_csr_adaptive, rocsparse_spmv_stage_buffer_size, &buffer_size, nullptr)); void* temp_buffer; HIP_CHECK(hipMalloc(&temp_buffer, buffer_size)); // Call spmv to perform analysis ROCSPARSE_CHECK(rocsparse_spmv(handle, trans, &alpha, matA, vecX, &beta, vecY, compute_type, rocsparse_spmv_alg_csr_adaptive, rocsparse_spmv_stage_preprocess, &buffer_size, temp_buffer)); // Call spmv to perform computation ROCSPARSE_CHECK(rocsparse_spmv(handle, trans, &alpha, matA, vecX, &beta, vecY, compute_type, rocsparse_spmv_alg_csr_adaptive, rocsparse_spmv_stage_compute, &buffer_size, temp_buffer)); // Copy result back to host HIP_CHECK(hipMemcpy(hy.data(), dy, sizeof(float) * m, hipMemcpyDeviceToHost)); // Clear rocSPARSE ROCSPARSE_CHECK(rocsparse_destroy_spmat_descr(matA)); ROCSPARSE_CHECK(rocsparse_destroy_dnvec_descr(vecX)); ROCSPARSE_CHECK(rocsparse_destroy_dnvec_descr(vecY)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); // Clear device memory HIP_CHECK(hipFree(dcsr_row_ptr)); HIP_CHECK(hipFree(dcsr_col_ind)); HIP_CHECK(hipFree(dcsr_val)); HIP_CHECK(hipFree(dx)); HIP_CHECK(hipFree(dy)); HIP_CHECK(hipFree(temp_buffer)); return 0; }


Note

None of the algorithms above are deterministic when \(A\) is transposed.

Note

The sparse matrix formats currently supported are:

[rocsparse_format_bsr](enumerations.html#rocsparse-types_8h_1ae1c0b9de06f3772ed14403400320b378a4c2ead89d182bd7d7bb7bc6eccbc9bb6),[rocsparse_format_coo](enumerations.html#rocsparse-types_8h_1ae1c0b9de06f3772ed14403400320b378a11b2282b2de9242f0b9a8607cf835423),[rocsparse_format_coo_aos](enumerations.html#rocsparse-types_8h_1ae1c0b9de06f3772ed14403400320b378affaa78f83b090b976f77765f259e0981),[rocsparse_format_csr](enumerations.html#rocsparse-types_8h_1ae1c0b9de06f3772ed14403400320b378a26160296ec3d447960cf2f5958a2f84d),[rocsparse_format_csc](enumerations.html#rocsparse-types_8h_1ae1c0b9de06f3772ed14403400320b378af8fdd82ccbbc7b2f7386eae16f284e08)and[rocsparse_format_ell](enumerations.html#rocsparse-types_8h_1ae1c0b9de06f3772ed14403400320b378a37a77201d206121094dacef57666d80b).Note

Only the

[rocsparse_spmv_stage_buffer_size](enumerations.html#rocsparse-types_8h_1ab2e40217ed05ec81a46674ecc91ce7bfafe51d3958904161b4b88990374760359)stage and the[rocsparse_spmv_stage_compute](enumerations.html#rocsparse-types_8h_1ab2e40217ed05ec81a46674ecc91ce7bfad920d865c566abca9171faade375ba67)stage are non blocking and executed asynchronously with respect to the host. They may return before the actual computation has finished. The[rocsparse_spmv_stage_preprocess](enumerations.html#rocsparse-types_8h_1ab2e40217ed05ec81a46674ecc91ce7bfaf2b1eae60f0e1ebfb31f6af522a7b4ab)stage is blocking with respect to the host.Note

Only the

[rocsparse_spmv_stage_buffer_size](enumerations.html#rocsparse-types_8h_1ab2e40217ed05ec81a46674ecc91ce7bfafe51d3958904161b4b88990374760359)stage and the[rocsparse_spmv_stage_compute](enumerations.html#rocsparse-types_8h_1ab2e40217ed05ec81a46674ecc91ce7bfad920d865c566abca9171faade375ba67)stage support execution in a hipGraph context. The[rocsparse_spmv_stage_preprocess](enumerations.html#rocsparse-types_8h_1ab2e40217ed05ec81a46674ecc91ce7bfaf2b1eae60f0e1ebfb31f6af522a7b4ab)stage does not support hipGraph.- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**trans**–**[in]**matrix operation type.**alpha**–**[in]**scalar \(\alpha\).**mat**–**[in]**matrix descriptor.**x**–**[in]**vector descriptor.**beta**–**[in]**scalar \(\beta\).**y**–**[inout]**vector descriptor.**compute_type**–**[in]**floating point precision for the SpMV computation.**alg**–**[in]**SpMV algorithm for the SpMV computation.**stage**–**[in]**SpMV stage for the SpMV computation.**buffer_size**–**[out]**number of bytes of the temporary storage buffer. buffer_size is set when`temp_buffer`

is nullptr.**temp_buffer**–**[in]**temporary storage buffer allocated by the user. When the[rocsparse_spmv_stage_buffer_size](enumerations.html#rocsparse-types_8h_1ab2e40217ed05ec81a46674ecc91ce7bfafe51d3958904161b4b88990374760359)stage is passed, the required allocation size (in bytes) is written to`buffer_size`

and function returns without performing the SpMV operation.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context`handle`

was not initialized.**rocsparse_status_invalid_pointer**–`alpha`

,`mat`

,`x`

,`beta`

,`y`

or`buffer_size`

pointer is invalid.**rocsparse_status_invalid_value**– the value of`trans`

,`compute_type`

,`alg`

, or`stage`

is incorrect.**rocsparse_status_not_implemented**–`compute_type`

or`alg`

is currently not supported.



## rocsparse_v2_spmv_buffer_size()[#](#rocsparse-v2-spmv-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_v2_spmv_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, rocsparse_spmv_descr descr,[rocsparse_const_spmat_descr](types.html#_CPPv427rocsparse_const_spmat_descr)mat,[rocsparse_const_dnvec_descr](types.html#_CPPv427rocsparse_const_dnvec_descr)x,[rocsparse_const_dnvec_descr](types.html#_CPPv427rocsparse_const_dnvec_descr)y,[rocsparse_v2_spmv_stage](enumerations.html#_CPPv423rocsparse_v2_spmv_stage)stage, size_t *buffer_size_in_bytes,[rocsparse_error](types.html#_CPPv415rocsparse_error)*error)[#](#_CPPv429rocsparse_v2_spmv_buffer_size16rocsparse_handle20rocsparse_spmv_descr27rocsparse_const_spmat_descr27rocsparse_const_dnvec_descr27rocsparse_const_dnvec_descr23rocsparse_v2_spmv_stageP6size_tP15rocsparse_error) `rocsparse_v2_spmv_buffer_size`

returns the size of the required buffer to execute the given stage of the Version 2 SpMV operation. This routine is used in conjunction with[rocsparse_v2_spmv()](#rocsparse__v2__spmv_8h_1a82054ad1c5ba87b41b757948d23d30fc). See[rocsparse_v2_spmv](#rocsparse__v2__spmv_8h_1a82054ad1c5ba87b41b757948d23d30fc)for full description and example.Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**descr**–**[in]**SpMV descriptor**mat**–**[in]**sparse matrix descriptor.**x**–**[in]**dense vector descriptor.**y**–**[in]**dense vector descriptor.**stage**–**[in]**Version 2 SpMV stage for the SpMV computation.**buffer_size_in_bytes**–**[out]**number of bytes of the buffer.**error**–**[out]**error descriptor created if the returned status is not[rocsparse_status_success](enumerations.html#rocsparse-types_8h_1a578f8c5c1b08f358bf4605b0031006a8a96462a9361cfceb6cf9354e10fdc671b). A null pointer can be passed if the user is not interested in obtaining an error descriptor.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_value**– the`stage`

value is invalid.**rocsparse_status_invalid_pointer**–`mat`

,`x`

,`y`

,`descr`

or`buffer_size_in_bytes`

pointer is invalid.



## rocsparse_v2_spmv()[#](#rocsparse-v2-spmv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_v2_spmv([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, rocsparse_spmv_descr descr, const void *alpha,[rocsparse_const_spmat_descr](types.html#_CPPv427rocsparse_const_spmat_descr)mat,[rocsparse_const_dnvec_descr](types.html#_CPPv427rocsparse_const_dnvec_descr)x, const void *beta,[rocsparse_dnvec_descr](types.html#_CPPv421rocsparse_dnvec_descr)y,[rocsparse_v2_spmv_stage](enumerations.html#_CPPv423rocsparse_v2_spmv_stage)stage, size_t buffer_size_in_bytes, void *buffer,[rocsparse_error](types.html#_CPPv415rocsparse_error)*error)[#](#_CPPv417rocsparse_v2_spmv16rocsparse_handle20rocsparse_spmv_descrPKv27rocsparse_const_spmat_descr27rocsparse_const_dnvec_descrPKv21rocsparse_dnvec_descr23rocsparse_v2_spmv_stage6size_tPvP15rocsparse_error) Sparse matrix vector multiplication.

`rocsparse_v2_spmv`

multiplies the scalar \(\alpha\) with a sparse \(m \times n\) matrix \(op(A)\) with the dense vector \(x\) and adds the result to the dense vector \(y\) that is multiplied by the scalar \(\beta\), such that\[ y := \alpha \cdot op(A) \cdot x + \beta \cdot y, \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if trans == rocsparse_operation_none} \\ A^T, & \text{if trans == rocsparse_operation_transpose} \\ A^H, & \text{if trans == rocsparse_operation_conjugate_transpose} \end{array} \right. \end{split}\]Performing the above operation involves two stages. The first stage is

[rocsparse_v2_spmv_stage_analysis](enumerations.html#rocsparse-types_8h_1af89d10217fa903e0d165bf446ed3b163a65472eccece26ab6587256c60b3857ff). This will perform an analysis of the symbolic information of \(op(A)\). The second stage is[rocsparse_v2_spmv_stage_compute](enumerations.html#rocsparse-types_8h_1af89d10217fa903e0d165bf446ed3b163acbf55517bf440ea55cae707b43916812)which corresponds to the actual calculation. The size of the buffer required for each stage is determined with calling the routine[rocsparse_v2_spmv_buffer_size](#rocsparse__v2__spmv_8h_1ac9b01de6fbc79a5a98e1c69dd9708ccd). The stage[rocsparse_v2_spmv_stage_analysis](enumerations.html#rocsparse-types_8h_1af89d10217fa903e0d165bf446ed3b163a65472eccece26ab6587256c60b3857ff)only needs to be called once for a given sparse matrix \(op(A)\) while the computation stage can be repeatedly used with different \(x\) and \(y\) vectors.`rocsparse_v2_spmv`

supports multiple algorithms. These algorithms have different trade offs depending on the sparsity pattern of the matrix, whether or not the results need to be deterministic, and how many times the sparse-vector product will be performed.Algorithm

Deterministic

Notes

rocsparse_spmv_alg_csr_rowsplit

Yes

Is best suited for matrices with all rows having a similar number of non-zeros. Can out perform adaptive and LRB algorithms in certain sparsity patterns. Will perform very poorly if some rows have few non-zeros and some rows have many non-zeros.

rocsparse_spmv_alg_csr_stream

Yes

[Deprecated] old name for rocsparse_spmv_alg_csr_rowsplit.

rocsparse_spmv_alg_csr_adaptive

No

Generally the fastest algorithm across all matrix sparsity patterns. This includes matrices that have some rows with many non-zeros and some rows with few non-zeros. Requires a lengthy preprocessing that needs to be amortized over many subsequent sparse vector products.

rocsparse_spmv_alg_csr_lrb

No

Like adaptive algorithm, generally performs well across all matrix sparsity patterns. Generally not as fast as adaptive algorithm, however uses a much faster pre-processing step. Good for when only a few number of sparse vector products will be performed.

rocsparse_spmv_alg_csr_nnzsplit

No

Like adaptive algorithm, generally performs well across all matrix sparsity patterns. Generally not as fast as adaptive algorithm but faster than LRB algorithm. It uses a much faster pre-processing step than LRB. Good for when the number of sparse vector products that will be performed is less than one hundred. If more products need to be computed, the adaptive algorithm is probably faster.

COO Algorithms

Deterministic

Notes

rocsparse_spmv_alg_coo

Yes

Generally not as fast as atomic algorithm but is deterministic

rocsparse_spmv_alg_coo_atomic

No

Generally the fastest COO algorithm

ELL Algorithms

Deterministic

Notes

rocsparse_spmv_alg_ell

Yes

ELL Algorithms

Deterministic

Notes

rocsparse_spmv_alg_sell

Yes

BSR Algorithm

Deterministic

Notes

rocsparse_spmv_alg_bsr

Yes

`rocsparse_v2_spmv`

supports multiple combinations of data types and compute types. The tables below indicate the currently supported different data types that can be used for for the sparse matrix \(op(A)\) and the dense vectors \(x\) and \(y\) and the compute type for \(\alpha\) and \(\beta\). The advantage of using different data types is to save on memory bandwidth and storage when a user application allows while performing the actual computation in a higher precision.`rocsparse_v2_spmv`

supports[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)and[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4)index precisions for storing the row pointer and column indices arrays of the sparse matrices.**Uniform Precisions:**A / X / Y / compute_type

rocsparse_datatype_f32_r

rocsparse_datatype_f64_r

rocsparse_datatype_f32_c

rocsparse_datatype_f64_c

**Mixed precisions:**A / X

Y

compute_type

rocsparse_datatype_i8_r

rocsparse_datatype_i32_r

rocsparse_datatype_i32_r

rocsparse_datatype_i8_r

rocsparse_datatype_f32_r

rocsparse_datatype_f32_r

rocsparse_datatype_f16_r

rocsparse_datatype_f32_r

rocsparse_datatype_f32_r

**Mixed-regular real precisions**A

X / Y / compute_type

rocsparse_datatype_f32_r

rocsparse_datatype_f64_r

rocsparse_datatype_f32_c

rocsparse_datatype_f64_c

**Mixed-regular Complex precisions**A

X / Y / compute_type

rocsparse_datatype_f32_r

rocsparse_datatype_f32_c

rocsparse_datatype_f64_r

rocsparse_datatype_f64_c


**Example**int main() { // 1 4 0 0 0 0 // A = 0 2 3 0 0 0 // 5 0 0 7 8 0 // 0 0 9 0 6 0 int m = 4; int n = 6; std::vector<int> hcsr_row_ptr = {0, 2, 4, 7, 9}; std::vector<int> hcsr_col_ind = {0, 1, 1, 2, 0, 3, 4, 2, 4}; std::vector<float> hcsr_val = {1, 4, 2, 3, 5, 7, 8, 9, 6}; std::vector<double> hx(n, 1.0f); std::vector<double> hy(m, 0.0f); // Scalar alpha double alpha = 3.7f; // Scalar beta double beta = 0.0f; int nnz = hcsr_row_ptr[m] - hcsr_row_ptr[0]; // Offload data to device int* dcsr_row_ptr; int* dcsr_col_ind; float* dcsr_val; double* dx; double* dy; HIP_CHECK(hipMalloc(&dcsr_row_ptr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc(&dcsr_col_ind, sizeof(int) * nnz)); HIP_CHECK(hipMalloc(&dcsr_val, sizeof(float) * nnz)); HIP_CHECK(hipMalloc(&dx, sizeof(double) * n)); HIP_CHECK(hipMalloc(&dy, sizeof(double) * m)); HIP_CHECK( hipMemcpy(dcsr_row_ptr, hcsr_row_ptr.data(), sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsr_col_ind, hcsr_col_ind.data(), sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsr_val, hcsr_val.data(), sizeof(float) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dx, hx.data(), sizeof(double) * n, hipMemcpyHostToDevice)); rocsparse_handle handle; rocsparse_error p_error[1] = {}; rocsparse_spmat_descr matA; rocsparse_dnvec_descr vecX; rocsparse_dnvec_descr vecY; rocsparse_indextype row_idx_type = rocsparse_indextype_i32; rocsparse_indextype col_idx_type = rocsparse_indextype_i32; rocsparse_datatype data_type = rocsparse_datatype_f32_r; rocsparse_index_base idx_base = rocsparse_index_base_zero; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Create sparse matrix A ROCSPARSE_CHECK(rocsparse_create_csr_descr(&matA, m, n, nnz, dcsr_row_ptr, dcsr_col_ind, dcsr_val, row_idx_type, col_idx_type, idx_base, data_type)); // Create dense vector X ROCSPARSE_CHECK(rocsparse_create_dnvec_descr(&vecX, n, dx, rocsparse_datatype_f64_r)); // Create dense vector Y ROCSPARSE_CHECK(rocsparse_create_dnvec_descr(&vecY, m, dy, rocsparse_datatype_f64_r)); rocsparse_spmv_descr spmv_descr; ROCSPARSE_CHECK(rocsparse_create_spmv_descr(&spmv_descr)); const rocsparse_spmv_alg spmv_alg = rocsparse_spmv_alg_csr_adaptive; ROCSPARSE_CHECK(rocsparse_spmv_set_input( handle, spmv_descr, rocsparse_spmv_input_alg, &spmv_alg, sizeof(spmv_alg), p_error)); const rocsparse_operation spmv_operation = rocsparse_operation_none; ROCSPARSE_CHECK(rocsparse_spmv_set_input(handle, spmv_descr, rocsparse_spmv_input_operation, &spmv_operation, sizeof(spmv_operation), p_error)); const rocsparse_datatype spmv_scalar_datatype = rocsparse_datatype_f64_r; ROCSPARSE_CHECK(rocsparse_spmv_set_input(handle, spmv_descr, rocsparse_spmv_input_scalar_datatype, &spmv_scalar_datatype, sizeof(spmv_scalar_datatype), p_error)); const rocsparse_datatype spmv_compute_datatype = rocsparse_datatype_f64_r; ROCSPARSE_CHECK(rocsparse_spmv_set_input(handle, spmv_descr, rocsparse_spmv_input_compute_datatype, &spmv_compute_datatype, sizeof(spmv_compute_datatype), p_error)); // Call spmv to get buffer size size_t buffer_size; ROCSPARSE_CHECK(rocsparse_v2_spmv_buffer_size(handle, spmv_descr, matA, vecX, vecY, rocsparse_v2_spmv_stage_analysis, &buffer_size, p_error)); void* buffer; HIP_CHECK(hipMalloc(&buffer, buffer_size)); // Call spmv to perform analysis ROCSPARSE_CHECK(rocsparse_v2_spmv(handle, spmv_descr, &alpha, matA, vecX, &beta, vecY, rocsparse_v2_spmv_stage_analysis, buffer_size, buffer, p_error)); HIP_CHECK(hipFree(buffer)); ROCSPARSE_CHECK(rocsparse_v2_spmv_buffer_size(handle, spmv_descr, matA, vecX, vecY, rocsparse_v2_spmv_stage_compute, &buffer_size, p_error)); HIP_CHECK(hipMalloc(&buffer, buffer_size)); // Call spmv to perform computation ROCSPARSE_CHECK(rocsparse_v2_spmv(handle, spmv_descr, &alpha, matA, vecX, &beta, vecY, rocsparse_v2_spmv_stage_compute, buffer_size, buffer, p_error)); HIP_CHECK(hipFree(buffer)); ROCSPARSE_CHECK(rocsparse_destroy_error(p_error[0])); ROCSPARSE_CHECK(rocsparse_destroy_spmv_descr(spmv_descr)); // Copy result back to host HIP_CHECK(hipMemcpy(hy.data(), dy, sizeof(double) * m, hipMemcpyDeviceToHost)); // Clear rocSPARSE ROCSPARSE_CHECK(rocsparse_destroy_spmat_descr(matA)); ROCSPARSE_CHECK(rocsparse_destroy_dnvec_descr(vecX)); ROCSPARSE_CHECK(rocsparse_destroy_dnvec_descr(vecY)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); // Clear device memory HIP_CHECK(hipFree(dcsr_row_ptr)); HIP_CHECK(hipFree(dcsr_col_ind)); HIP_CHECK(hipFree(dcsr_val)); HIP_CHECK(hipFree(dx)); HIP_CHECK(hipFree(dy)); return 0; }


Note

The stage

[rocsparse_v2_spmv_stage_analysis](enumerations.html#rocsparse-types_8h_1af89d10217fa903e0d165bf446ed3b163a65472eccece26ab6587256c60b3857ff)is mandatory, an error will be returned if that stage was not executed before the stage[rocsparse_v2_spmv_stage_compute](enumerations.html#rocsparse-types_8h_1af89d10217fa903e0d165bf446ed3b163acbf55517bf440ea55cae707b43916812).Note

None of the algorithms above are deterministic when \(A\) is transposed.

Note

The

[rocsparse_v2_spmv_stage_compute](enumerations.html#rocsparse-types_8h_1af89d10217fa903e0d165bf446ed3b163acbf55517bf440ea55cae707b43916812)stage is non blocking and executed asynchronously with respect to the host. They may return before the actual computation has finished. The stage[rocsparse_v2_spmv_stage_analysis](enumerations.html#rocsparse-types_8h_1af89d10217fa903e0d165bf446ed3b163a65472eccece26ab6587256c60b3857ff)is blocking with respect to the host.Note

Only the stage

[rocsparse_v2_spmv_stage_compute](enumerations.html#rocsparse-types_8h_1af89d10217fa903e0d165bf446ed3b163acbf55517bf440ea55cae707b43916812)supports execution in a hipGraph context. The[rocsparse_v2_spmv_stage_analysis](enumerations.html#rocsparse-types_8h_1af89d10217fa903e0d165bf446ed3b163a65472eccece26ab6587256c60b3857ff)stage does not support hipGraph.- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**descr**–**[in]**spmv descriptor.**alpha**–**[in]**scalar \(\alpha\).**mat**–**[in]**matrix descriptor.**x**–**[in]**vector descriptor.**beta**–**[in]**scalar \(\beta\).**y**–**[inout]**vector descriptor.**stage**–**[in]**SpMV stage of the SpMV algorithm.**buffer_size_in_bytes**–**[in]**size in bytes of the buffer, must be greater or equal to the buffer size obtained from[rocsparse_v2_spmv_buffer_size](#rocsparse__v2__spmv_8h_1ac9b01de6fbc79a5a98e1c69dd9708ccd).**buffer**–**[in]**temporary buffer allocated by the user.**error**–**[out]**error descriptor created if the returned status is not[rocsparse_status_success](enumerations.html#rocsparse-types_8h_1a578f8c5c1b08f358bf4605b0031006a8a96462a9361cfceb6cf9354e10fdc671b). A null pointer can be passed if the user is not interested in obtaining an error descriptor.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context`handle`

was not initialized.**rocsparse_status_invalid_pointer**–`alpha`

,`mat`

,`x`

,`beta`

,`y`

or`buffer`

pointer is invalid.**rocsparse_status_invalid_value**– the value of`stage`

is invalid.**rocsparse_status_not_implemented**– if`alg`

is not supported or if the mixed precision configuration is not supported.



## rocsparse_spsv()[#](#rocsparse-spsv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_spsv([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans, const void *alpha,[rocsparse_const_spmat_descr](types.html#_CPPv427rocsparse_const_spmat_descr)mat,[rocsparse_const_dnvec_descr](types.html#_CPPv427rocsparse_const_dnvec_descr)x, const[rocsparse_dnvec_descr](types.html#_CPPv421rocsparse_dnvec_descr)y,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)compute_type,[rocsparse_spsv_alg](enumerations.html#_CPPv418rocsparse_spsv_alg)alg,[rocsparse_spsv_stage](enumerations.html#_CPPv420rocsparse_spsv_stage)stage, size_t *buffer_size, void *temp_buffer)[#](#_CPPv414rocsparse_spsv16rocsparse_handle19rocsparse_operationPKv27rocsparse_const_spmat_descr27rocsparse_const_dnvec_descrK21rocsparse_dnvec_descr18rocsparse_datatype18rocsparse_spsv_alg20rocsparse_spsv_stageP6size_tPv) Sparse triangular system solve.

`rocsparse_spsv`

solves a triangular linear system of equations defined by a sparse \(m \times m\) square matrix \(op(A)\), given in CSR or COO storage format, such that\[ op(A) \cdot y = \alpha \cdot x, \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if trans == rocsparse_operation_none} \\ A^T, & \text{if trans == rocsparse_operation_transpose} \end{array} \right. \end{split}\]and where \(y\) is the dense solution vector and \(x\) is the dense right-hand side vector.Performing the above operation requires three stages. First,

`rocsparse_spsv`

must be called with the stage[rocsparse_spsv_stage_buffer_size](enumerations.html#rocsparse-types_8h_1ada24ab514fc13a1d817d15d529e55dd2a7bb19094a3a9afafb2e95809f9e1b9ef)which will determine the size of the required temporary storage buffer. The user then allocates this buffer and calls`rocsparse_spsv`

with the stage[rocsparse_spsv_stage_preprocess](enumerations.html#rocsparse-types_8h_1ada24ab514fc13a1d817d15d529e55dd2ad074073d1146296a5e1f9d7fde7f2bf1)which will perform analysis on the sparse matrix \(op(A)\). Finally, the user completes the computation by calling`rocsparse_spsv`

with the stage[rocsparse_spsv_stage_compute](enumerations.html#rocsparse-types_8h_1ada24ab514fc13a1d817d15d529e55dd2a80386cc729d7f6610023e3853b65c5a1). The buffer size, buffer allocation, and preprecess stages only need to be called once for a given sparse matrix \(op(A)\) while the computation stage can be repeatedly used with different \(x\) and \(y\) vectors.`rocsparse_spsv`

supports[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)and[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4)index types for storing the row pointer and column indices arrays of the sparse matrices.`rocsparse_spsv`

supports the following data types for \(op(A)\), \(x\), \(y\) and compute types for \(\alpha\):**Uniform Precisions:**A / X / Y / compute_type

rocsparse_datatype_f32_r

rocsparse_datatype_f64_r

rocsparse_datatype_f32_c

rocsparse_datatype_f64_c

**Example**int main() { // 1 0 0 0 // A = 4 2 0 0 // 0 3 7 0 // 0 0 0 1 int m = 4; std::vector<int> hcsr_row_ptr = {0, 1, 3, 5, 6}; std::vector<int> hcsr_col_ind = {0, 0, 1, 1, 2, 3}; std::vector<float> hcsr_val = {1, 4, 2, 3, 7, 1}; std::vector<float> hx(m, 1.0f); std::vector<float> hy(m, 0.0f); // Scalar alpha float alpha = 1.0f; int nnz = hcsr_row_ptr[m] - hcsr_row_ptr[0]; // Offload data to device int* dcsr_row_ptr; int* dcsr_col_ind; float* dcsr_val; float* dx; float* dy; HIP_CHECK(hipMalloc(&dcsr_row_ptr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc(&dcsr_col_ind, sizeof(int) * nnz)); HIP_CHECK(hipMalloc(&dcsr_val, sizeof(float) * nnz)); HIP_CHECK(hipMalloc(&dx, sizeof(float) * m)); HIP_CHECK(hipMalloc(&dy, sizeof(float) * m)); HIP_CHECK( hipMemcpy(dcsr_row_ptr, hcsr_row_ptr.data(), sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsr_col_ind, hcsr_col_ind.data(), sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsr_val, hcsr_val.data(), sizeof(float) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dx, hx.data(), sizeof(float) * m, hipMemcpyHostToDevice)); rocsparse_handle handle; rocsparse_spmat_descr matA; rocsparse_dnvec_descr vecX; rocsparse_dnvec_descr vecY; rocsparse_indextype row_idx_type = rocsparse_indextype_i32; rocsparse_indextype col_idx_type = rocsparse_indextype_i32; rocsparse_datatype data_type = rocsparse_datatype_f32_r; rocsparse_datatype compute_type = rocsparse_datatype_f32_r; rocsparse_index_base idx_base = rocsparse_index_base_zero; rocsparse_operation trans = rocsparse_operation_none; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Create sparse matrix A ROCSPARSE_CHECK(rocsparse_create_csr_descr(&matA, m, m, nnz, dcsr_row_ptr, dcsr_col_ind, dcsr_val, row_idx_type, col_idx_type, idx_base, data_type)); // Create dense vector X ROCSPARSE_CHECK(rocsparse_create_dnvec_descr(&vecX, m, dx, data_type)); // Create dense vector Y ROCSPARSE_CHECK(rocsparse_create_dnvec_descr(&vecY, m, dy, data_type)); // Call spsv to get buffer size size_t buffer_size; ROCSPARSE_CHECK(rocsparse_spsv(handle, trans, &alpha, matA, vecX, vecY, compute_type, rocsparse_spsv_alg_default, rocsparse_spsv_stage_buffer_size, &buffer_size, nullptr)); void* temp_buffer; HIP_CHECK(hipMalloc(&temp_buffer, buffer_size)); // Call spsv to perform analysis ROCSPARSE_CHECK(rocsparse_spsv(handle, trans, &alpha, matA, vecX, vecY, compute_type, rocsparse_spsv_alg_default, rocsparse_spsv_stage_preprocess, &buffer_size, temp_buffer)); // Call spsv to perform computation ROCSPARSE_CHECK(rocsparse_spsv(handle, trans, &alpha, matA, vecX, vecY, compute_type, rocsparse_spsv_alg_default, rocsparse_spsv_stage_compute, &buffer_size, temp_buffer)); // Copy result back to host HIP_CHECK(hipMemcpy(hy.data(), dy, sizeof(float) * m, hipMemcpyDeviceToHost)); // Clear rocSPARSE ROCSPARSE_CHECK(rocsparse_destroy_spmat_descr(matA)); ROCSPARSE_CHECK(rocsparse_destroy_dnvec_descr(vecX)); ROCSPARSE_CHECK(rocsparse_destroy_dnvec_descr(vecY)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); // Clear device memory HIP_CHECK(hipFree(dcsr_row_ptr)); HIP_CHECK(hipFree(dcsr_col_ind)); HIP_CHECK(hipFree(dcsr_val)); HIP_CHECK(hipFree(dx)); HIP_CHECK(hipFree(dy)); HIP_CHECK(hipFree(temp_buffer)); return 0; }


Note

The sparse matrix formats currently supported are:

[rocsparse_format_coo](enumerations.html#rocsparse-types_8h_1ae1c0b9de06f3772ed14403400320b378a11b2282b2de9242f0b9a8607cf835423)and[rocsparse_format_csr](enumerations.html#rocsparse-types_8h_1ae1c0b9de06f3772ed14403400320b378a26160296ec3d447960cf2f5958a2f84d).Note

Only the

[rocsparse_spsv_stage_buffer_size](enumerations.html#rocsparse-types_8h_1ada24ab514fc13a1d817d15d529e55dd2a7bb19094a3a9afafb2e95809f9e1b9ef)stage and the[rocsparse_spsv_stage_compute](enumerations.html#rocsparse-types_8h_1ada24ab514fc13a1d817d15d529e55dd2a80386cc729d7f6610023e3853b65c5a1)stage are non blocking and executed asynchronously with respect to the host. They may return before the actual computation has finished. The[rocsparse_spsv_stage_preprocess](enumerations.html#rocsparse-types_8h_1ada24ab514fc13a1d817d15d529e55dd2ad074073d1146296a5e1f9d7fde7f2bf1)stage is blocking with respect to the host.Note

Currently, only

`trans`

==[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528)and`trans`

==[rocsparse_operation_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a1ea3194d0c7bdb9e500d6faeead8ebf5)is supported.Note

Only the

[rocsparse_spsv_stage_buffer_size](enumerations.html#rocsparse-types_8h_1ada24ab514fc13a1d817d15d529e55dd2a7bb19094a3a9afafb2e95809f9e1b9ef)stage and the[rocsparse_spsv_stage_compute](enumerations.html#rocsparse-types_8h_1ada24ab514fc13a1d817d15d529e55dd2a80386cc729d7f6610023e3853b65c5a1)stage support execution in a hipGraph context. The[rocsparse_spsv_stage_preprocess](enumerations.html#rocsparse-types_8h_1ada24ab514fc13a1d817d15d529e55dd2ad074073d1146296a5e1f9d7fde7f2bf1)stage does not support hipGraph.- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**trans**–**[in]**matrix operation type.**alpha**–**[in]**scalar \(\alpha\).**mat**–**[in]**matrix descriptor.**x**–**[in]**vector descriptor.**y**–**[inout]**vector descriptor.**compute_type**–**[in]**floating point precision for the SpSV computation.**alg**–**[in]**SpSV algorithm for the SpSV computation.**stage**–**[in]**SpSV stage for the SpSV computation.**buffer_size**–**[out]**number of bytes of the temporary storage buffer.**temp_buffer**–**[in]**temporary storage buffer allocated by the user. When the[rocsparse_spsv_stage_buffer_size](enumerations.html#rocsparse-types_8h_1ada24ab514fc13a1d817d15d529e55dd2a7bb19094a3a9afafb2e95809f9e1b9ef)stage is passed, the required allocation size (in bytes) is written to`buffer_size`

and function returns without performing the SpSV operation. This buffer is non-persistent, no data are stored in it; therefore, this memory can be freed or reuse for other tasks between the analysis phase and the compute phase.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`alpha`

,`mat`

,`x`

,`y`

or`buffer_size`

pointer is invalid.**rocsparse_status_not_implemented**–`trans`

,`compute_type`

,`stage`

or`alg`

is currently not supported.



## rocsparse_sptrsv_buffer_size()[#](#rocsparse-sptrsv-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sptrsv_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, rocsparse_sptrsv_descr sptrsv_descr,[rocsparse_const_spmat_descr](types.html#_CPPv427rocsparse_const_spmat_descr)spmat_descr,[rocsparse_const_dnvec_descr](types.html#_CPPv427rocsparse_const_dnvec_descr)x,[rocsparse_const_dnvec_descr](types.html#_CPPv427rocsparse_const_dnvec_descr)y,[rocsparse_sptrsv_stage](enumerations.html#_CPPv422rocsparse_sptrsv_stage)sptrsv_stage, size_t *buffer_size_in_bytes,[rocsparse_error](types.html#_CPPv415rocsparse_error)*p_error)[#](#_CPPv428rocsparse_sptrsv_buffer_size16rocsparse_handle22rocsparse_sptrsv_descr27rocsparse_const_spmat_descr27rocsparse_const_dnvec_descr27rocsparse_const_dnvec_descr22rocsparse_sptrsv_stageP6size_tP15rocsparse_error) `rocsparse_sptrsv_buffer_size`

returns the size of the required buffer to execute the given stage of the SpTrSV operation. This routine is used in conjunction with[rocsparse_sptrsv()](#rocsparse__sptrsv_8h_1ac01897deba4d0d8449c4d52f475857b7). See[rocsparse_sptrsv](#rocsparse__sptrsv_8h_1ac01897deba4d0d8449c4d52f475857b7)for full description and example.Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**sptrsv_descr**–**[in]**SpTrSV descriptor**spmat_descr**–**[in]**sparse matrix descriptor.**x**–**[in]**dense vector descriptor.**y**–**[in]**dense vector descriptor.**sptrsv_stage**–**[in]**stage for the SpTrSV computation.**buffer_size_in_bytes**–**[out]**number of bytes of the buffer.**p_error**–**[out]**error descriptor created if the returned status is not[rocsparse_status_success](enumerations.html#rocsparse-types_8h_1a578f8c5c1b08f358bf4605b0031006a8a96462a9361cfceb6cf9354e10fdc671b). A null pointer can be passed if the user is not interested in obtaining an error descriptor.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_value**– the`sptrsv_stage`

value is invalid.**rocsparse_status_invalid_pointer**–`sptrsv_descr`

,`spmat_descr`

,`x`

,`y`

, or`buffer_size_in_bytes`

pointer is invalid.



## rocsparse_sptrsv()[#](#rocsparse-sptrsv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sptrsv([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, rocsparse_sptrsv_descr sptrsv_descr,[rocsparse_const_spmat_descr](types.html#_CPPv427rocsparse_const_spmat_descr)A,[rocsparse_const_dnvec_descr](types.html#_CPPv427rocsparse_const_dnvec_descr)x,[rocsparse_dnvec_descr](types.html#_CPPv421rocsparse_dnvec_descr)y,[rocsparse_sptrsv_stage](enumerations.html#_CPPv422rocsparse_sptrsv_stage)sptrsv_stage, size_t buffer_size_in_bytes, void *buffer,[rocsparse_error](types.html#_CPPv415rocsparse_error)*p_error)[#](#_CPPv416rocsparse_sptrsv16rocsparse_handle22rocsparse_sptrsv_descr27rocsparse_const_spmat_descr27rocsparse_const_dnvec_descr21rocsparse_dnvec_descr22rocsparse_sptrsv_stage6size_tPvP15rocsparse_error) Sparse Triangular solve.

`rocsparse_sptrsv`

solves a triangular linear system of equations defined by a sparse \(m \times m\) square matrix \(op(A)\), such that\[ op(A) \cdot y = \alpha \cdot x, \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if op == rocsparse_operation_none} \\ A^T, & \text{if op == rocsparse_operation_transpose} \\ A^H, & \text{if op == rocsparse_operation_conjugate_transpose} \\ \end{array} \right. \end{split}\]and where \(y\) is the dense solution vector and \(x\) is the dense right-hand side vector.Performing the above operation requires two stages, the stage

[rocsparse_sptrsv_stage_analysis](enumerations.html#rocsparse-types_8h_1a3ba3bb99e7f72c9a0bb3cbba336b77b9a0f270df4f58f7d945b927df83f595453)and the stage[rocsparse_sptrsv_stage_compute](enumerations.html#rocsparse-types_8h_1a3ba3bb99e7f72c9a0bb3cbba336b77b9af42bb99497117fe75281a567338f6d8b). The stage[rocsparse_sptrsv_stage_analysis](enumerations.html#rocsparse-types_8h_1a3ba3bb99e7f72c9a0bb3cbba336b77b9a0f270df4f58f7d945b927df83f595453)is required to perform the stage[rocsparse_sptrsv_stage_compute](enumerations.html#rocsparse-types_8h_1a3ba3bb99e7f72c9a0bb3cbba336b77b9af42bb99497117fe75281a567338f6d8b)and only need to be called once for a given sparse matrix \(op(A)\) while the stage[rocsparse_sptrsv_stage_compute](enumerations.html#rocsparse-types_8h_1a3ba3bb99e7f72c9a0bb3cbba336b77b9af42bb99497117fe75281a567338f6d8b)can be repeatedly used with different \(x\) and \(y\) vectors.`rocsparse_sptrsv`

supports the following data types for \(op(A)\), \(x\), \(y\), and scalar \(\alpha\):**Uniform Precisions:**A / X / Y / scalar

rocsparse_datatype_f32_r

rocsparse_datatype_f64_r

rocsparse_datatype_f32_c

rocsparse_datatype_f64_c

**Example**int main() { // 1 0 0 0 // A = 4 2 0 0 // 0 3 7 0 // 0 0 0 1 int m = 4; std::vector<int> hcsr_row_ptr = {0, 1, 3, 5, 6}; std::vector<int> hcsr_col_ind = {0, 0, 1, 1, 2, 3}; std::vector<float> hcsr_val = {1, 4, 2, 3, 7, 1}; std::vector<float> hx(m, 1.0f); std::vector<float> hy(m, 0.0f); // Scalar alpha float alpha = 1.0f; int nnz = hcsr_row_ptr[m] - hcsr_row_ptr[0]; // Offload data to device int* dcsr_row_ptr; int* dcsr_col_ind; float* dcsr_val; float* dx; float* dy; HIP_CHECK(hipMalloc(&dcsr_row_ptr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc(&dcsr_col_ind, sizeof(int) * nnz)); HIP_CHECK(hipMalloc(&dcsr_val, sizeof(float) * nnz)); HIP_CHECK(hipMalloc(&dx, sizeof(float) * m)); HIP_CHECK(hipMalloc(&dy, sizeof(float) * m)); HIP_CHECK( hipMemcpy(dcsr_row_ptr, hcsr_row_ptr.data(), sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsr_col_ind, hcsr_col_ind.data(), sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsr_val, hcsr_val.data(), sizeof(float) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dx, hx.data(), sizeof(float) * m, hipMemcpyHostToDevice)); rocsparse_handle handle; rocsparse_spmat_descr matA; rocsparse_dnvec_descr vecX; rocsparse_dnvec_descr vecY; rocsparse_indextype row_idx_type = rocsparse_indextype_i32; rocsparse_indextype col_idx_type = rocsparse_indextype_i32; rocsparse_datatype data_type = rocsparse_datatype_f32_r; rocsparse_datatype compute_type = rocsparse_datatype_f32_r; rocsparse_index_base idx_base = rocsparse_index_base_zero; rocsparse_operation trans = rocsparse_operation_none; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Create sparse matrix A ROCSPARSE_CHECK(rocsparse_create_csr_descr(&matA, m, m, nnz, dcsr_row_ptr, dcsr_col_ind, dcsr_val, row_idx_type, col_idx_type, idx_base, data_type)); // Create dense vector X ROCSPARSE_CHECK(rocsparse_create_dnvec_descr(&vecX, m, dx, data_type)); // Create dense vector Y ROCSPARSE_CHECK(rocsparse_create_dnvec_descr(&vecY, m, dy, data_type)); rocsparse_sptrsv_descr sptrsv_descr; ROCSPARSE_CHECK(rocsparse_create_sptrsv_descr(&sptrsv_descr)); const rocsparse_sptrsv_alg sptrsv_alg = rocsparse_sptrsv_alg_default; ROCSPARSE_CHECK(rocsparse_sptrsv_set_input(handle, sptrsv_descr, rocsparse_sptrsv_input_alg, &sptrsv_alg, sizeof(sptrsv_alg), nullptr)); const rocsparse_operation sptrsv_operation = rocsparse_operation_none; ROCSPARSE_CHECK(rocsparse_sptrsv_set_input(handle, sptrsv_descr, rocsparse_sptrsv_input_operation, &sptrsv_operation, sizeof(sptrsv_operation), nullptr)); const rocsparse_datatype sptrsv_scalar_datatype = rocsparse_datatype_f32_r; ROCSPARSE_CHECK(rocsparse_sptrsv_set_input(handle, sptrsv_descr, rocsparse_sptrsv_input_scalar_datatype, &sptrsv_scalar_datatype, sizeof(sptrsv_scalar_datatype), nullptr)); const rocsparse_datatype sptrsv_compute_datatype = rocsparse_datatype_f32_r; ROCSPARSE_CHECK(rocsparse_sptrsv_set_input(handle, sptrsv_descr, rocsparse_sptrsv_input_compute_datatype, &sptrsv_compute_datatype, sizeof(sptrsv_compute_datatype), nullptr)); const rocsparse_analysis_policy sptrsv_analysis_policy = rocsparse_analysis_policy_reuse; ROCSPARSE_CHECK(rocsparse_sptrsv_set_input(handle, sptrsv_descr, rocsparse_sptrsv_input_analysis_policy, &sptrsv_analysis_policy, sizeof(sptrsv_analysis_policy), nullptr)); size_t buffer_size; void* temp_buffer; // Analysis phase ROCSPARSE_CHECK(rocsparse_sptrsv_buffer_size(handle, sptrsv_descr, matA, vecX, vecY, rocsparse_sptrsv_stage_analysis, &buffer_size, nullptr)); HIP_CHECK(hipMalloc(&temp_buffer, buffer_size)); ROCSPARSE_CHECK(rocsparse_sptrsv(handle, sptrsv_descr, matA, vecX, vecY, rocsparse_sptrsv_stage_analysis, buffer_size, temp_buffer, nullptr)); HIP_CHECK(hipFree(temp_buffer)); temp_buffer = nullptr; int64_t zero_pivot; ROCSPARSE_CHECK(rocsparse_sptrsv_get_output(handle, sptrsv_descr, rocsparse_sptrsv_output_zero_pivot_position, &zero_pivot, sizeof(zero_pivot), nullptr)); if(zero_pivot != -1) { std::cout << "zero pivot detected during analysis at position " << zero_pivot << std::endl; } // // Compute phase. // ROCSPARSE_CHECK(rocsparse_sptrsv_set_input(handle, sptrsv_descr, rocsparse_sptrsv_input_scalar_alpha, &alpha, sizeof(&alpha), nullptr)); ROCSPARSE_CHECK(rocsparse_sptrsv_buffer_size(handle, sptrsv_descr, matA, vecX, vecY, rocsparse_sptrsv_stage_compute, &buffer_size, nullptr)); HIP_CHECK(hipMalloc(&temp_buffer, buffer_size)); ROCSPARSE_CHECK(rocsparse_sptrsv(handle, sptrsv_descr, matA, vecX, vecY, rocsparse_sptrsv_stage_compute, buffer_size, temp_buffer, nullptr)); // Device synchronization hipStream_t stream; ROCSPARSE_CHECK(rocsparse_get_stream(handle, &stream)); HIP_CHECK(hipStreamSynchronize(stream)); ROCSPARSE_CHECK(rocsparse_sptrsv_get_output(handle, sptrsv_descr, rocsparse_sptrsv_output_zero_pivot_position, &zero_pivot, sizeof(zero_pivot), nullptr)); if(zero_pivot != -1) { std::cout << "zero pivot detected during compute phase at position " << zero_pivot << std::endl; } // Clear rocSPARSE ROCSPARSE_CHECK(rocsparse_destroy_spmat_descr(matA)); ROCSPARSE_CHECK(rocsparse_destroy_dnvec_descr(vecX)); ROCSPARSE_CHECK(rocsparse_destroy_dnvec_descr(vecY)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); ROCSPARSE_CHECK(rocsparse_destroy_sptrsv_descr(sptrsv_descr)); // Copy result back to host HIP_CHECK(hipMemcpy(hy.data(), dy, sizeof(float) * m, hipMemcpyDeviceToHost)); // Clear device memory HIP_CHECK(hipFree(dcsr_row_ptr)); HIP_CHECK(hipFree(dcsr_col_ind)); HIP_CHECK(hipFree(dcsr_val)); HIP_CHECK(hipFree(dx)); HIP_CHECK(hipFree(dy)); HIP_CHECK(hipFree(temp_buffer)); return 0; }


Note

The descriptor

`rocsparse_sptrsv_descr`

needs to be configured with rocsparse_sptrsv_set_input.Note

The sparse matrix formats currently supported are:

[rocsparse_format_coo](enumerations.html#rocsparse-types_8h_1ae1c0b9de06f3772ed14403400320b378a11b2282b2de9242f0b9a8607cf835423)and[rocsparse_format_csr](enumerations.html#rocsparse-types_8h_1ae1c0b9de06f3772ed14403400320b378a26160296ec3d447960cf2f5958a2f84d).Note

the

[rocsparse_sptrsv_stage_compute](enumerations.html#rocsparse-types_8h_1a3ba3bb99e7f72c9a0bb3cbba336b77b9af42bb99497117fe75281a567338f6d8b)stage is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished. The[rocsparse_sptrsv_stage_analysis](enumerations.html#rocsparse-types_8h_1a3ba3bb99e7f72c9a0bb3cbba336b77b9a0f270df4f58f7d945b927df83f595453)stage is blocking with respect to the host.Note

Currently, only

`trans`

==[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528)and`trans`

==[rocsparse_operation_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a1ea3194d0c7bdb9e500d6faeead8ebf5)is supported. Only the[rocsparse_sptrsv_stage_compute](enumerations.html#rocsparse-types_8h_1a3ba3bb99e7f72c9a0bb3cbba336b77b9af42bb99497117fe75281a567338f6d8b)stage supports execution in a hipGraph context. The[rocsparse_sptrsv_stage_analysis](enumerations.html#rocsparse-types_8h_1a3ba3bb99e7f72c9a0bb3cbba336b77b9a0f270df4f58f7d945b927df83f595453)stage does not support hipGraph.- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**sptrsv_descr**–**[in]**descriptor of the routine.**A**–**[in]**matrix descriptor.**x**–**[in]**vector descriptor.**y**–**[inout]**vector descriptor.**sptrsv_stage**–**[in]**stage for the SpTRSV computation.**buffer_size_in_bytes**–**[in]**number of bytes of the buffer.**buffer**–**[in]**buffer allocated by the user.**p_error**–**[out]**error descriptor created if the returned status is not[rocsparse_status_success](enumerations.html#rocsparse-types_8h_1a578f8c5c1b08f358bf4605b0031006a8a96462a9361cfceb6cf9354e10fdc671b). A null pointer can be passed if the user is not interested in obtaining an error descriptor.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`sptrsv_descr`

,`A`

,`x`

, or`y`

is invalid, or if`buffer`

is null and`buffer_size_in_bytes`

is non zero, or if`buffer`

is non null and`buffer_size_in_bytes`

is zero.**rocsparse_status_invalid_value**–`sptrsv_stage`

is invalid.



## rocsparse_spsm()[#](#rocsparse-spsm)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_spsm([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B, const void *alpha,[rocsparse_const_spmat_descr](types.html#_CPPv427rocsparse_const_spmat_descr)matA,[rocsparse_const_dnmat_descr](types.html#_CPPv427rocsparse_const_dnmat_descr)matB, const[rocsparse_dnmat_descr](types.html#_CPPv421rocsparse_dnmat_descr)matC,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)compute_type,[rocsparse_spsm_alg](enumerations.html#_CPPv418rocsparse_spsm_alg)alg,[rocsparse_spsm_stage](enumerations.html#_CPPv420rocsparse_spsm_stage)stage, size_t *buffer_size, void *temp_buffer)[#](#_CPPv414rocsparse_spsm16rocsparse_handle19rocsparse_operation19rocsparse_operationPKv27rocsparse_const_spmat_descr27rocsparse_const_dnmat_descrK21rocsparse_dnmat_descr18rocsparse_datatype18rocsparse_spsm_alg20rocsparse_spsm_stageP6size_tPv) Sparse triangular system solve with multiple right-hand sides.

`rocsparse_spsm`

solves a triangular linear system of equations defined by a sparse \(m \times m\) square matrix \(op(A)\), given in CSR or COO storage format, such that\[ op(A) \cdot C = \alpha \cdot op(B), \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if trans == rocsparse_operation_none} \\ A^T, & \text{if trans == rocsparse_operation_transpose} \end{array} \right. \end{split}\]and\[\begin{split} op(B) = \left\{ \begin{array}{ll} B, & \text{if trans_B == rocsparse_operation_none} \\ B^T, & \text{if trans_B == rocsparse_operation_transpose} \end{array} \right. \end{split}\]and where \(C\) is the dense solution matrix and \(B\) is the dense right-hand side matrix. Both \(B\) and \(C\) can be in row or column order.Performing the above operation requires three stages. First,

`rocsparse_spsm`

must be called with the stage[rocsparse_spsm_stage_buffer_size](enumerations.html#rocsparse-types_8h_1a69fa113206a9a3f650499469165d14acab21141ce4717eda3904c15f49090d728)which will determine the size of the required temporary storage buffer. The user then allocates this buffer and calls`rocsparse_spsm`

with the stage[rocsparse_spsm_stage_preprocess](enumerations.html#rocsparse-types_8h_1a69fa113206a9a3f650499469165d14aca5251f8721c5114001d2ce9d4f7d826c1)which will perform analysis on the sparse matrix \(op(A)\). Finally, the user completes the computation by calling`rocsparse_spsm`

with the stage[rocsparse_spsm_stage_compute](enumerations.html#rocsparse-types_8h_1a69fa113206a9a3f650499469165d14acad526329c59dca9ab138a4286c795b8a9). The buffer size, buffer allocation, and preprecess stages only need to be called once for a given sparse triangular matrix \(op(A)\) while the computation stage can be repeatedly used with different \(B\) and \(C\) matrices.As noted above, both \(B\) and \(C\) can be in row or column order (this includes mixing the order so that \(B\) is row order and \(C\) is column order and vice versa). Internally however, rocSPARSE kernels solve the system assuming the matrices \(B\) and \(C\) are in row order as this provides the best memory access. This means that if the matrix \(C\) is not in row order and/or the matrix \(B\) is not row order (or \(B^{T}\) is not column order as this is equivalent to being in row order), then internally memory copies and/or transposing of data may be performed to get them into the correct order (possbily using extra buffer size). Once computation is completed, additional memory copies and/or transposing of data may be performed to get them back into the user arrays. For best performance and smallest required temporary storage buffers, use row order for the matrix \(C\) and row order for the matrix \(B\) (or column order if \(B\) is being transposed).

`rocsparse_spsm`

supports[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)and[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4)index precisions for storing the row pointer and column indices arrays of the sparse matrices.`rocsparse_spsm`

supports the following data types for \(op(A)\), \(op(B)\), \(C\) and compute types for \(\alpha\):**Uniform Precisions:**A / B / C / compute_type

rocsparse_datatype_f32_r

rocsparse_datatype_f64_r

rocsparse_datatype_f32_c

rocsparse_datatype_f64_c

**Example**int main() { // 1 0 0 0 // A = 4 2 0 0 // 0 3 7 0 // 0 0 0 1 int m = 4; int n = 2; std::vector<int> hcsr_row_ptr = {0, 1, 3, 5, 6}; std::vector<int> hcsr_col_ind = {0, 0, 1, 1, 2, 3}; std::vector<float> hcsr_val = {1, 4, 2, 3, 7, 1}; std::vector<float> hB(m * n); std::vector<float> hC(m * n); for(int i = 0; i < n; i++) { for(int j = 0; j < m; j++) { hB[m * i + j] = static_cast<float>(i + 1); } } // Scalar alpha float alpha = 1.0f; int nnz = hcsr_row_ptr[m] - hcsr_row_ptr[0]; // Offload data to device int* dcsr_row_ptr; int* dcsr_col_ind; float* dcsr_val; float* dB; float* dC; HIP_CHECK(hipMalloc(&dcsr_row_ptr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc(&dcsr_col_ind, sizeof(int) * nnz)); HIP_CHECK(hipMalloc(&dcsr_val, sizeof(float) * nnz)); HIP_CHECK(hipMalloc(&dB, sizeof(float) * m * n)); HIP_CHECK(hipMalloc(&dC, sizeof(float) * m * n)); HIP_CHECK( hipMemcpy(dcsr_row_ptr, hcsr_row_ptr.data(), sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsr_col_ind, hcsr_col_ind.data(), sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsr_val, hcsr_val.data(), sizeof(float) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dB, hB.data(), sizeof(float) * m * n, hipMemcpyHostToDevice)); rocsparse_handle handle; rocsparse_spmat_descr matA; rocsparse_dnmat_descr matB; rocsparse_dnmat_descr matC; rocsparse_indextype row_idx_type = rocsparse_indextype_i32; rocsparse_indextype col_idx_type = rocsparse_indextype_i32; rocsparse_datatype data_type = rocsparse_datatype_f32_r; rocsparse_datatype compute_type = rocsparse_datatype_f32_r; rocsparse_index_base idx_base = rocsparse_index_base_zero; rocsparse_operation trans_A = rocsparse_operation_none; rocsparse_operation trans_B = rocsparse_operation_none; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Create sparse matrix A ROCSPARSE_CHECK(rocsparse_create_csr_descr(&matA, m, m, nnz, dcsr_row_ptr, dcsr_col_ind, dcsr_val, row_idx_type, col_idx_type, idx_base, data_type)); // Create dense matrix B ROCSPARSE_CHECK( rocsparse_create_dnmat_descr(&matB, m, n, m, dB, data_type, rocsparse_order_column)); // Create dense matrix C ROCSPARSE_CHECK( rocsparse_create_dnmat_descr(&matC, m, n, m, dC, data_type, rocsparse_order_column)); // Call spsv to get buffer size size_t buffer_size; ROCSPARSE_CHECK(rocsparse_spsm(handle, trans_A, trans_B, &alpha, matA, matB, matC, compute_type, rocsparse_spsm_alg_default, rocsparse_spsm_stage_buffer_size, &buffer_size, nullptr)); void* temp_buffer; HIP_CHECK(hipMalloc(&temp_buffer, buffer_size)); // Call spsv to perform analysis ROCSPARSE_CHECK(rocsparse_spsm(handle, trans_A, trans_B, &alpha, matA, matB, matC, compute_type, rocsparse_spsm_alg_default, rocsparse_spsm_stage_preprocess, &buffer_size, temp_buffer)); // Call spsv to perform computation ROCSPARSE_CHECK(rocsparse_spsm(handle, trans_A, trans_B, &alpha, matA, matB, matC, compute_type, rocsparse_spsm_alg_default, rocsparse_spsm_stage_compute, &buffer_size, temp_buffer)); // Copy result back to host HIP_CHECK(hipMemcpy(hC.data(), dC, sizeof(float) * m * n, hipMemcpyDeviceToHost)); std::cout << "hC" << std::endl; for(size_t i = 0; i < hC.size(); ++i) { std::cout << hC[i] << " "; } std::cout << std::endl; // Clear rocSPARSE ROCSPARSE_CHECK(rocsparse_destroy_spmat_descr(matA)); ROCSPARSE_CHECK(rocsparse_destroy_dnmat_descr(matB)); ROCSPARSE_CHECK(rocsparse_destroy_dnmat_descr(matC)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); // Clear device memory HIP_CHECK(hipFree(dcsr_row_ptr)); HIP_CHECK(hipFree(dcsr_col_ind)); HIP_CHECK(hipFree(dcsr_val)); HIP_CHECK(hipFree(dB)); HIP_CHECK(hipFree(dC)); HIP_CHECK(hipFree(temp_buffer)); return 0; }


Note

The sparse matrix formats currently supported are:

[rocsparse_format_coo](enumerations.html#rocsparse-types_8h_1ae1c0b9de06f3772ed14403400320b378a11b2282b2de9242f0b9a8607cf835423)and[rocsparse_format_csr](enumerations.html#rocsparse-types_8h_1ae1c0b9de06f3772ed14403400320b378a26160296ec3d447960cf2f5958a2f84d).Note

Only the

[rocsparse_spsm_stage_buffer_size](enumerations.html#rocsparse-types_8h_1a69fa113206a9a3f650499469165d14acab21141ce4717eda3904c15f49090d728)stage and the[rocsparse_spsm_stage_compute](enumerations.html#rocsparse-types_8h_1a69fa113206a9a3f650499469165d14acad526329c59dca9ab138a4286c795b8a9)stage are non blocking and executed asynchronously with respect to the host. They may return before the actual computation has finished. The[rocsparse_spsm_stage_preprocess](enumerations.html#rocsparse-types_8h_1a69fa113206a9a3f650499469165d14aca5251f8721c5114001d2ce9d4f7d826c1)stage is blocking with respect to the host.Note

Currently, only

`trans_A`

==[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528)and`trans_A`

==[rocsparse_operation_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a1ea3194d0c7bdb9e500d6faeead8ebf5)is supported. Currently, only`trans_B`

==[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528)and`trans_B`

==[rocsparse_operation_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a1ea3194d0c7bdb9e500d6faeead8ebf5)is supported.Note

Only the

[rocsparse_spsm_stage_buffer_size](enumerations.html#rocsparse-types_8h_1a69fa113206a9a3f650499469165d14acab21141ce4717eda3904c15f49090d728)stage and the[rocsparse_spsm_stage_compute](enumerations.html#rocsparse-types_8h_1a69fa113206a9a3f650499469165d14acad526329c59dca9ab138a4286c795b8a9)stage support execution in a hipGraph context. The[rocsparse_spsm_stage_preprocess](enumerations.html#rocsparse-types_8h_1a69fa113206a9a3f650499469165d14aca5251f8721c5114001d2ce9d4f7d826c1)stage does not support hipGraph.- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**trans_A**–**[in]**matrix operation type for the sparse matrix \(op(A)\).**trans_B**–**[in]**matrix operation type for the dense matrix \(op(B)\).**alpha**–**[in]**scalar \(\alpha\).**matA**–**[in]**sparse matrix descriptor.**matB**–**[in]**dense matrix descriptor.**matC**–**[inout]**dense matrix descriptor.**compute_type**–**[in]**floating point precision for the SpSM computation.**alg**–**[in]**SpSM algorithm for the SpSM computation.**stage**–**[in]**SpSM stage for the SpSM computation.**buffer_size**–**[out]**number of bytes of the temporary storage buffer.**temp_buffer**–**[in]**temporary storage buffer allocated by the user. When the[rocsparse_spsm_stage_buffer_size](enumerations.html#rocsparse-types_8h_1a69fa113206a9a3f650499469165d14acab21141ce4717eda3904c15f49090d728)stage is passed, the required allocation size (in bytes) is written to`buffer_size`

and function returns without performing the SpSM operation.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`alpha`

,`matA`

,`matB`

,`matC`

,`descr`

or`buffer_size`

pointer is invalid.**rocsparse_status_not_implemented**–`trans_A`

,`trans_B`

,`compute_type`

,`stage`

or`alg`

is currently not supported.



## rocsparse_sptrsm_buffer_size()[#](#rocsparse-sptrsm-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sptrsm_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, rocsparse_sptrsm_descr sptrsm_descr,[rocsparse_const_spmat_descr](types.html#_CPPv427rocsparse_const_spmat_descr)A,[rocsparse_const_dnmat_descr](types.html#_CPPv427rocsparse_const_dnmat_descr)X,[rocsparse_const_dnmat_descr](types.html#_CPPv427rocsparse_const_dnmat_descr)Y,[rocsparse_sptrsm_stage](enumerations.html#_CPPv422rocsparse_sptrsm_stage)sptrsm_stage, size_t *buffer_size_in_bytes,[rocsparse_error](types.html#_CPPv415rocsparse_error)*p_error)[#](#_CPPv428rocsparse_sptrsm_buffer_size16rocsparse_handle22rocsparse_sptrsm_descr27rocsparse_const_spmat_descr27rocsparse_const_dnmat_descr27rocsparse_const_dnmat_descr22rocsparse_sptrsm_stageP6size_tP15rocsparse_error) `rocsparse_sptrsm_buffer_size`

returns the size of the required buffer to execute the given stage of the SpTrSM operation. This routine is used in conjunction with[rocsparse_sptrsm()](#rocsparse__sptrsm_8h_1aa192a5047738bab3eb48f9a8e2953e41). See[rocsparse_sptrsm](#rocsparse__sptrsm_8h_1aa192a5047738bab3eb48f9a8e2953e41)for full description and example.Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**sptrsm_descr**–**[in]**SpTrSM descriptor**A**–**[in]**sparse matrix descriptor.**X**–**[in]**dense matrix descriptor.**Y**–**[in]**dense matrix descriptor.**sptrsm_stage**–**[in]**stage for the SpTrSM computation.**buffer_size_in_bytes**–**[out]**number of bytes of the buffer.**p_error**–**[out]**error descriptor created if the returned status is not[rocsparse_status_success](enumerations.html#rocsparse-types_8h_1a578f8c5c1b08f358bf4605b0031006a8a96462a9361cfceb6cf9354e10fdc671b). A null pointer can be passed if the user is not interested in obtaining an error descriptor.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_value**– the`sptrsm_stage`

value is invalid.**rocsparse_status_invalid_pointer**–`A`

,`X`

,`Y`

,`sptrsm_descr`

or`buffer_size_in_bytes`

pointer is invalid.



## rocsparse_sptrsm()[#](#rocsparse-sptrsm)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sptrsm([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, rocsparse_sptrsm_descr sptrsm_descr,[rocsparse_const_spmat_descr](types.html#_CPPv427rocsparse_const_spmat_descr)A,[rocsparse_const_dnmat_descr](types.html#_CPPv427rocsparse_const_dnmat_descr)X,[rocsparse_dnmat_descr](types.html#_CPPv421rocsparse_dnmat_descr)Y,[rocsparse_sptrsm_stage](enumerations.html#_CPPv422rocsparse_sptrsm_stage)sptrsm_stage, size_t buffer_size_in_bytes, void *buffer,[rocsparse_error](types.html#_CPPv415rocsparse_error)*p_error)[#](#_CPPv416rocsparse_sptrsm16rocsparse_handle22rocsparse_sptrsm_descr27rocsparse_const_spmat_descr27rocsparse_const_dnmat_descr21rocsparse_dnmat_descr22rocsparse_sptrsm_stage6size_tPvP15rocsparse_error) Sparse triangular system solve with multiple right-hand sides.

`rocsparse_sptrsm`

solves a triangular linear system of equations defined by a sparse \(m \times m\) square matrix \(op(A)\), given in CSR or COO storage format, such that\[ op(A) \cdot Y = \alpha \cdot op(X), \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if trans == rocsparse_operation_none} \\ A^T, & \text{if trans == rocsparse_operation_transpose} \end{array} \right. \end{split}\]and\[\begin{split} op(X) = \left\{ \begin{array}{ll} X, & \text{if trans_B == rocsparse_operation_none} \\ X^T, & \text{if trans_B == rocsparse_operation_transpose} \end{array} \right. \end{split}\]and where \(Y\) is the dense solution matrix and \(X\) is the dense right-hand side matrix. Both \(X\) and \(Y\) can be in row or column order.Performing the above operation requires two stages, the stage

[rocsparse_sptrsm_stage_analysis](enumerations.html#rocsparse-types_8h_1ad753300bd78ba91de2a3f48871194292a2b3ad7b026dd45caf4f8a0d0da61a08e)and the stage[rocsparse_sptrsm_stage_compute](enumerations.html#rocsparse-types_8h_1ad753300bd78ba91de2a3f48871194292a8b79ce196c0731a714f468591666b7cb). The stage[rocsparse_sptrsm_stage_analysis](enumerations.html#rocsparse-types_8h_1ad753300bd78ba91de2a3f48871194292a2b3ad7b026dd45caf4f8a0d0da61a08e)is required to perform the stage[rocsparse_sptrsm_stage_compute](enumerations.html#rocsparse-types_8h_1ad753300bd78ba91de2a3f48871194292a8b79ce196c0731a714f468591666b7cb)and only need to be called once for a given sparse matrix \(op(A)\) while the stage[rocsparse_sptrsm_stage_compute](enumerations.html#rocsparse-types_8h_1ad753300bd78ba91de2a3f48871194292a8b79ce196c0731a714f468591666b7cb)can be repeatedly used with different \(X\) and \(Y\) matrices.As noted above, both \(X\) and \(Y\) can be in row or column order (this includes mixing the order so that \(X\) is row order and \(Y\) is column order and vice versa). Internally however, rocSPARSE kernels solve the system assuming the matrices \(X\) and \(Y\) are in row order as this provides the best memory access. This means that if the matrix \(Y\) is not in row order and/or the matrix \(X\) is not row order (or \(X^{T}\) is not column order as this is equivalent to being in row order), then internally memory copies and/or transposing of data may be performed to get them into the correct order (possbily using extra buffer size). Once computation is completed, additional memory copies and/or transposing of data may be performed to get them back into the user arrays. For best performance and smallest required temporary storage buffers, use row order for the matrix \(Y\) and row order for the matrix \(X\) (or column order if \(X\) is being transposed).

`rocsparse_sptrsm`

supports[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)and[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4)index precisions for storing the row pointer and column indices arrays of the sparse matrices.`rocsparse_sptrsm`

supports the following data types for \(op(A)\), \(op(X)\), \(Y\) and compute types for \(\alpha\):**Uniform Precisions:**A / X / Y / compute_type

rocsparse_datatype_f32_r

rocsparse_datatype_f64_r

rocsparse_datatype_f32_c

rocsparse_datatype_f64_c

**Example**int main() { // 1 0 0 0 // A = 4 2 0 0 // 0 3 7 0 // 0 0 0 1 int m = 4; int n = 2; std::vector<int> hcsr_row_ptr = {0, 1, 3, 5, 6}; std::vector<int> hcsr_col_ind = {0, 0, 1, 1, 2, 3}; std::vector<float> hcsr_val = {1, 4, 2, 3, 7, 1}; std::vector<float> hB(m * n); std::vector<float> hC(m * n); for(int i = 0; i < n; i++) { for(int j = 0; j < m; j++) { hB[m * i + j] = static_cast<float>(i + 1); } } // Scalar alpha float alpha = 1.0f; int nnz = hcsr_row_ptr[m] - hcsr_row_ptr[0]; // Offload data to device int* dcsr_row_ptr; int* dcsr_col_ind; float* dcsr_val; float* dB; float* dC; HIP_CHECK(hipMalloc(&dcsr_row_ptr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc(&dcsr_col_ind, sizeof(int) * nnz)); HIP_CHECK(hipMalloc(&dcsr_val, sizeof(float) * nnz)); HIP_CHECK(hipMalloc(&dB, sizeof(float) * m * n)); HIP_CHECK(hipMalloc(&dC, sizeof(float) * m * n)); HIP_CHECK( hipMemcpy(dcsr_row_ptr, hcsr_row_ptr.data(), sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsr_col_ind, hcsr_col_ind.data(), sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsr_val, hcsr_val.data(), sizeof(float) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dB, hB.data(), sizeof(float) * m * n, hipMemcpyHostToDevice)); rocsparse_handle handle; rocsparse_spmat_descr matA; rocsparse_dnmat_descr matB; rocsparse_dnmat_descr matC; rocsparse_indextype row_idx_type = rocsparse_indextype_i32; rocsparse_indextype col_idx_type = rocsparse_indextype_i32; rocsparse_datatype data_type = rocsparse_datatype_f32_r; rocsparse_datatype compute_type = rocsparse_datatype_f32_r; rocsparse_index_base idx_base = rocsparse_index_base_zero; rocsparse_operation trans_A = rocsparse_operation_none; rocsparse_operation trans_X = rocsparse_operation_none; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Create sparse matrix A ROCSPARSE_CHECK(rocsparse_create_csr_descr(&matA, m, m, nnz, dcsr_row_ptr, dcsr_col_ind, dcsr_val, row_idx_type, col_idx_type, idx_base, data_type)); // Create dense matrix B ROCSPARSE_CHECK( rocsparse_create_dnmat_descr(&matB, m, n, m, dB, data_type, rocsparse_order_column)); // Create dense matrix C ROCSPARSE_CHECK( rocsparse_create_dnmat_descr(&matC, m, n, m, dC, data_type, rocsparse_order_column)); rocsparse_sptrsm_descr sptrsm_descr; ROCSPARSE_CHECK(rocsparse_create_sptrsm_descr(&sptrsm_descr)); const rocsparse_sptrsm_alg sptrsm_alg = rocsparse_sptrsm_alg_default; ROCSPARSE_CHECK(rocsparse_sptrsm_set_input(handle, sptrsm_descr, rocsparse_sptrsm_input_alg, &sptrsm_alg, sizeof(sptrsm_alg), nullptr)); ROCSPARSE_CHECK(rocsparse_sptrsm_set_input(handle, sptrsm_descr, rocsparse_sptrsm_input_operation_A, &trans_A, sizeof(trans_A), nullptr)); ROCSPARSE_CHECK(rocsparse_sptrsm_set_input(handle, sptrsm_descr, rocsparse_sptrsm_input_operation_X, &trans_X, sizeof(trans_X), nullptr)); const rocsparse_datatype sptrsm_scalar_datatype = rocsparse_datatype_f32_r; ROCSPARSE_CHECK(rocsparse_sptrsm_set_input(handle, sptrsm_descr, rocsparse_sptrsm_input_scalar_datatype, &sptrsm_scalar_datatype, sizeof(sptrsm_scalar_datatype), nullptr)); const rocsparse_datatype sptrsm_compute_datatype = rocsparse_datatype_f32_r; ROCSPARSE_CHECK(rocsparse_sptrsm_set_input(handle, sptrsm_descr, rocsparse_sptrsm_input_compute_datatype, &sptrsm_compute_datatype, sizeof(sptrsm_compute_datatype), nullptr)); const rocsparse_analysis_policy sptrsm_analysis_policy = rocsparse_analysis_policy_reuse; ROCSPARSE_CHECK(rocsparse_sptrsm_set_input(handle, sptrsm_descr, rocsparse_sptrsm_input_analysis_policy, &sptrsm_analysis_policy, sizeof(sptrsm_analysis_policy), nullptr)); size_t buffer_size; void* temp_buffer; // Analysis phase ROCSPARSE_CHECK(rocsparse_sptrsm_buffer_size(handle, sptrsm_descr, matA, matB, matC, rocsparse_sptrsm_stage_analysis, &buffer_size, nullptr)); HIP_CHECK(hipMalloc(&temp_buffer, buffer_size)); ROCSPARSE_CHECK(rocsparse_sptrsm(handle, sptrsm_descr, matA, matB, matC, rocsparse_sptrsm_stage_analysis, buffer_size, temp_buffer, nullptr)); HIP_CHECK(hipFree(temp_buffer)); temp_buffer = nullptr; int64_t zero_pivot; ROCSPARSE_CHECK(rocsparse_sptrsm_get_output(handle, sptrsm_descr, rocsparse_sptrsm_output_zero_pivot_position, &zero_pivot, sizeof(zero_pivot), nullptr)); if(zero_pivot != -1) { std::cout << "zero pivot detected during analysis at position " << zero_pivot << std::endl; } // // Compute phase. // ROCSPARSE_CHECK(rocsparse_sptrsm_set_input(handle, sptrsm_descr, rocsparse_sptrsm_input_scalar_alpha, &alpha, sizeof(&alpha), nullptr)); ROCSPARSE_CHECK(rocsparse_sptrsm_buffer_size(handle, sptrsm_descr, matA, matB, matC, rocsparse_sptrsm_stage_compute, &buffer_size, nullptr)); HIP_CHECK(hipMalloc(&temp_buffer, buffer_size)); ROCSPARSE_CHECK(rocsparse_sptrsm(handle, sptrsm_descr, matA, matB, matC, rocsparse_sptrsm_stage_compute, buffer_size, temp_buffer, nullptr)); // Device synchronization hipStream_t stream; ROCSPARSE_CHECK(rocsparse_get_stream(handle, &stream)); HIP_CHECK(hipStreamSynchronize(stream)); ROCSPARSE_CHECK(rocsparse_sptrsm_get_output(handle, sptrsm_descr, rocsparse_sptrsm_output_zero_pivot_position, &zero_pivot, sizeof(zero_pivot), nullptr)); if(zero_pivot != -1) { std::cout << "zero pivot detected during compute phase at position " << zero_pivot << std::endl; } // Clear rocSPARSE ROCSPARSE_CHECK(rocsparse_destroy_spmat_descr(matA)); ROCSPARSE_CHECK(rocsparse_destroy_dnmat_descr(matB)); ROCSPARSE_CHECK(rocsparse_destroy_dnmat_descr(matC)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); ROCSPARSE_CHECK(rocsparse_destroy_sptrsm_descr(sptrsm_descr)); // Copy result back to host HIP_CHECK(hipMemcpy(hC.data(), dC, sizeof(float) * m * n, hipMemcpyDeviceToHost)); std::cout << "hC" << std::endl; for(size_t i = 0; i < hC.size(); ++i) { std::cout << hC[i] << " "; } std::cout << std::endl; // Clear device memory HIP_CHECK(hipFree(dcsr_row_ptr)); HIP_CHECK(hipFree(dcsr_col_ind)); HIP_CHECK(hipFree(dcsr_val)); HIP_CHECK(hipFree(dB)); HIP_CHECK(hipFree(dC)); HIP_CHECK(hipFree(temp_buffer)); return 0; }


Note

The sparse matrix formats currently supported are:

[rocsparse_format_coo](enumerations.html#rocsparse-types_8h_1ae1c0b9de06f3772ed14403400320b378a11b2282b2de9242f0b9a8607cf835423)and[rocsparse_format_csr](enumerations.html#rocsparse-types_8h_1ae1c0b9de06f3772ed14403400320b378a26160296ec3d447960cf2f5958a2f84d).Note

Only the

[rocsparse_sptrsm_stage_compute](enumerations.html#rocsparse-types_8h_1ad753300bd78ba91de2a3f48871194292a8b79ce196c0731a714f468591666b7cb)stage are non blocking and executed asynchronously with respect to the host. They may return before the actual computation has finished. The[rocsparse_sptrsm_stage_analysis](enumerations.html#rocsparse-types_8h_1ad753300bd78ba91de2a3f48871194292a2b3ad7b026dd45caf4f8a0d0da61a08e)stage is blocking with respect to the host.Note

Currently, only

`trans_A`

==[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528)and`trans_A`

==[rocsparse_operation_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a1ea3194d0c7bdb9e500d6faeead8ebf5)is supported. Currently, only`trans_X`

==[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528)and`trans_X`

==[rocsparse_operation_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a1ea3194d0c7bdb9e500d6faeead8ebf5)is supported.Note

Only the stage

[rocsparse_sptrsm_stage_compute](enumerations.html#rocsparse-types_8h_1ad753300bd78ba91de2a3f48871194292a8b79ce196c0731a714f468591666b7cb)support execution in a hipGraph context. The[rocsparse_sptrsm_stage_analysis](enumerations.html#rocsparse-types_8h_1ad753300bd78ba91de2a3f48871194292a2b3ad7b026dd45caf4f8a0d0da61a08e)stage does not support hipGraph.- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**sptrsm_descr**–**[in]**sptrsm routine descriptor.**A**–**[in]**sparse matrix descriptor.**X**–**[in]**dense matrix descriptor.**Y**–**[inout]**dense matrix descriptor.**sptrsm_stage**–**[in]**Sptrsm stage for the Sptrsm computation.**buffer_size_in_bytes**–**[out]**number of bytes of the temporary storage buffer.**buffer**–**[in]**temporary storage buffer allocated by the user.**p_error**–**[out]**error descriptor created if the returned status is not[rocsparse_status_success](enumerations.html#rocsparse-types_8h_1a578f8c5c1b08f358bf4605b0031006a8a96462a9361cfceb6cf9354e10fdc671b). A null pointer can be passed if the user is not interested in obtaining an error descriptor.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`A`

, X,`Y`

,`sptrsm_descr`

or`buffer_size`

pointer is invalid.**rocsparse_status_not_implemented**– the configuration of the descriptor`sptrsm_descr`

is currently not supported.



## rocsparse_spmm()[#](#rocsparse-spmm)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_spmm([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B, const void *alpha,[rocsparse_const_spmat_descr](types.html#_CPPv427rocsparse_const_spmat_descr)mat_A,[rocsparse_const_dnmat_descr](types.html#_CPPv427rocsparse_const_dnmat_descr)mat_B, const void *beta, const[rocsparse_dnmat_descr](types.html#_CPPv421rocsparse_dnmat_descr)mat_C,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)compute_type,[rocsparse_spmm_alg](enumerations.html#_CPPv418rocsparse_spmm_alg)alg,[rocsparse_spmm_stage](enumerations.html#_CPPv420rocsparse_spmm_stage)stage, size_t *buffer_size, void *temp_buffer)[#](#_CPPv414rocsparse_spmm16rocsparse_handle19rocsparse_operation19rocsparse_operationPKv27rocsparse_const_spmat_descr27rocsparse_const_dnmat_descrPKvK21rocsparse_dnmat_descr18rocsparse_datatype18rocsparse_spmm_alg20rocsparse_spmm_stageP6size_tPv) Sparse matrix dense matrix multiplication.

`rocsparse_spmm`

multiplies the scalar \(\alpha\) with a sparse \(m \times k\) matrix \(op(A)\), defined in CSR, COO, BSR or Blocked ELL storage format, and the dense \(k \times n\) matrix \(op(B)\) and adds the result to the dense \(m \times n\) matrix \(C\) that is multiplied by the scalar \(\beta\), such that\[ C := \alpha \cdot op(A) \cdot op(B) + \beta \cdot C, \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if trans_A == rocsparse_operation_none} \\ A^T, & \text{if trans_A == rocsparse_operation_transpose} \\ A^H, & \text{if trans_A == rocsparse_operation_conjugate_transpose} \end{array} \right. \end{split}\]and\[\begin{split} op(B) = \left\{ \begin{array}{ll} B, & \text{if trans_B == rocsparse_operation_none} \\ B^T, & \text{if trans_B == rocsparse_operation_transpose} \\ B^H, & \text{if trans_B == rocsparse_operation_conjugate_transpose} \end{array} \right. \end{split}\]Both \(B\) and \(C\) can be in row or column order.`rocsparse_spmm`

requires three stages to complete. First, the user passes the[rocsparse_spmm_stage_buffer_size](enumerations.html#rocsparse-types_8h_1a28daf89fa49ded50158dcda6e5045aafaef94fe80b7c181dd56d06df7eca379a1)stage to determine the size of the required temporary storage buffer. Next, the user allocates this buffer and calls`rocsparse_spmm`

again with the[rocsparse_spmm_stage_preprocess](enumerations.html#rocsparse-types_8h_1a28daf89fa49ded50158dcda6e5045aaface910c4e7024c7fff1c8749849126f2e)stage which will perform analysis on the sparse matrix \(op(A)\). Finally, the user calls`rocsparse_spmm`

with the[rocsparse_spmm_stage_compute](enumerations.html#rocsparse-types_8h_1a28daf89fa49ded50158dcda6e5045aafaeb9be614ccccf840f3f529786e037259)stage to perform the actual computation. The buffer size, buffer allocation, and preprecess stages only need to be called once for a given sparse matrix \(op(A)\) while the computation stage can be repeatedly used with different \(B\) and \(C\) matrices. Once all calls to`rocsparse_spmm`

are complete, the temporary buffer can be deallocated.As noted above, both \(B\) and \(C\) can be in row or column order (this includes mixing the order so that \(B\) is row order and \(C\) is column order and vice versa). For best performance, use row order for both \(B\) and \(C\) as this provides the best memory access.

`rocsparse_spmm`

supports multiple different algorithms. These algorithms have different trade offs depending on the sparsity pattern of the matrix, whether or not the results need to be deterministic, and how many times the sparse-matrix product will be performed.CSR Algorithms

Deterministic

Preprocessing

Notes

rocsparse_spmm_alg_csr

Yes

No

Default algorithm.

rocsparse_spmm_alg_csr_row_split

Yes

No

Assigns a fixed number of threads per row regardless of the number of non-zeros in each row. This can perform well when each row in the matrix has roughly the same number of non-zeros

rocsparse_spmm_alg_csr_nnz_split

No

Yes

Distributes work by having each thread block work on a fixed number of non-zeros regardless of the number of rows that might be involved. This can perform well when the matrix has some rows with few non-zeros and some rows with many non-zeros

rocsparse_spmm_alg_csr_merge_path

No

Yes

Attempts to combine the approaches of row-split and non-zero split by having each block work on a fixed amount of work which can be either non-zeros or rows

COO Algorithms

Deterministic

Preprocessing

Notes

rocsparse_spmm_alg_coo_segmented

Yes

No

Generally not as fast as atomic algorithm but is deterministic

rocsparse_spmm_alg_coo_atomic

No

No

Generally the fastest COO algorithm. Is the default algorithm

rocsparse_spmm_alg_coo_segmented_atomic

No

No

ELL Algorithms

Deterministic

Preprocessing

Notes

rocsparse_spmm_alg_bell

Yes

No

BSR Algorithms

Deterministic

Preprocessing

Notes

rocsparse_spmm_alg_bsr

Yes

No

One can also pass

[rocsparse_spmm_alg_default](enumerations.html#rocsparse-types_8h_1afe9381434c79b9de70070cf8693ac441a7188a7ac6e62502dc6a0bc0576e56021)which will automatically select from the algorithms listed above based on the sparse matrix format. In the case of CSR matrices this will set the algorithm to be[rocsparse_spmm_alg_csr](enumerations.html#rocsparse-types_8h_1afe9381434c79b9de70070cf8693ac441a0f91116261acd02b19bfd53017cebcf5), in the case of Blocked ELL matrices this will set the algorithm to be[rocsparse_spmm_alg_bell](enumerations.html#rocsparse-types_8h_1afe9381434c79b9de70070cf8693ac441a8979995e5ca065c4fb41bc7245e7e8c7), in the case of BSR matrix this will set the algorithm to be[rocsparse_spmm_alg_bsr](enumerations.html#rocsparse-types_8h_1afe9381434c79b9de70070cf8693ac441a33357935f5cc297a7192708b4cfdb61e)and for COO matrices it will set the algorithm to be[rocsparse_spmm_alg_coo_atomic](enumerations.html#rocsparse-types_8h_1afe9381434c79b9de70070cf8693ac441aed084d671c780b67f8f1b1ec6f7f420e).When A is transposed,

`rocsparse_spmm`

will revert to using[rocsparse_spmm_alg_csr](enumerations.html#rocsparse-types_8h_1afe9381434c79b9de70070cf8693ac441a0f91116261acd02b19bfd53017cebcf5)for CSR format and[rocsparse_spmm_alg_coo_atomic](enumerations.html#rocsparse-types_8h_1afe9381434c79b9de70070cf8693ac441aed084d671c780b67f8f1b1ec6f7f420e)for COO format regardless of algorithm selected.`rocsparse_spmm`

supports multiple combinations of data types and compute types. The tables below indicate the currently supported different data types that can be used for for the sparse matrix \(op(A)\) and the dense matrices \(op(B)\) and \(C\) and the compute type for \(\alpha\) and \(\beta\). The advantage of using different data types is to save on memory bandwidth and storage when a user application allows while performing the actual computation in a higher precision.`rocsparse_spmm`

supports[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)and[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4)index precisions for storing the row pointer and column indices arrays of the sparse matrices.**Uniform Precisions:**A / B / C / compute_type

rocsparse_datatype_f32_r

rocsparse_datatype_f64_r

rocsparse_datatype_f32_c

rocsparse_datatype_f64_c

**Mixed precisions:**A / B

C

compute_type

rocsparse_datatype_i8_r

rocsparse_datatype_i32_r

rocsparse_datatype_i32_r

rocsparse_datatype_i8_r

rocsparse_datatype_f32_r

rocsparse_datatype_f32_r

rocsparse_datatype_f16_r

rocsparse_datatype_f32_r

rocsparse_datatype_f32_r

rocsparse_datatype_bf16_r

rocsparse_datatype_f32_r

rocsparse_datatype_f32_r


`rocsparse_spmm`

also supports batched computation for CSR and COO matrices. There are three supported batch modes:\[\begin{split} C_i = A \times B_i \\ C_i = A_i \times B \\ C_i = A_i \times B_i \end{split}\]The batch mode is determined by the batch count and stride passed for each matrix. For example to use the first batch mode ( \(C_i = A \times B_i\)) with 100 batches for non-transposed \(A\), \(B\), and \(C\), one passes:

\[\begin{split} batch\_count\_A=1 \\ batch\_count\_B=100 \\ batch\_count\_C=100 \\ offsets\_batch\_stride\_A=0 \\ columns\_values\_batch\_stride\_A=0 \\ batch\_stride\_B=k*n \\ batch\_stride\_C=m*n \end{split}\]To use the second batch mode ( \(C_i = A_i \times B\)) one could use:\[\begin{split} batch\_count\_A=100 \\ batch\_count\_B=1 \\ batch\_count\_C=100 \\ offsets\_batch\_stride\_A=m+1 \\ columns\_values\_batch\_stride\_A=nnz \\ batch\_stride\_B=0 \\ batch\_stride\_C=m*n \end{split}\]And to use the third batch mode ( \(C_i = A_i \times B_i\)) one could use:\[\begin{split} batch\_count\_A=100 \\ batch\_count\_B=100 \\ batch\_count\_C=100 \\ offsets\_batch\_stride\_A=m+1 \\ columns\_values\_batch\_stride_A=nnz \\ batch\_stride_B=k*n \\ batch\_stride_C=m*n \end{split}\]See examples below.**Example**This example performs sparse matrix-dense matrix multiplication, \(C := \alpha \cdot A \cdot B + \beta \cdot C\)

int main() { // 1 4 0 0 0 0 // A = 0 2 3 0 0 0 // 5 0 0 7 8 0 // 0 0 9 0 6 0 // 1 4 2 // 1 2 3 // B = 5 4 0 // 3 1 9 // 1 2 2 // 0 3 0 // 1 1 5 // C = 1 2 1 // 1 3 1 // 6 2 4 int m = 4; int k = 6; int n = 3; std::vector<int> hcsr_row_ptr = {0, 2, 4, 7, 9}; std::vector<int> hcsr_col_ind = {0, 1, 1, 2, 0, 3, 4, 2, 4}; std::vector<float> hcsr_val = {1, 4, 2, 3, 5, 7, 8, 9, 6}; std::vector<float> hB(k * n, 1.0f); std::vector<float> hC(m * n, 1.0f); int nnz = hcsr_row_ptr[m] - hcsr_row_ptr[0]; float alpha = 1.0f; float beta = 0.0f; // Create CSR arrays on device int* dcsr_row_ptr; int* dcsr_col_ind; float* dcsr_val; float* dB; float* dC; HIP_CHECK(hipMalloc(&dcsr_row_ptr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc(&dcsr_col_ind, sizeof(int) * nnz)); HIP_CHECK(hipMalloc(&dcsr_val, sizeof(float) * nnz)); HIP_CHECK(hipMalloc(&dB, sizeof(float) * k * n)); HIP_CHECK(hipMalloc(&dC, sizeof(float) * m * n)); HIP_CHECK( hipMemcpy(dcsr_row_ptr, hcsr_row_ptr.data(), sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsr_col_ind, hcsr_col_ind.data(), sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsr_val, hcsr_val.data(), sizeof(float) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dB, hB.data(), sizeof(float) * k * n, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dC, hC.data(), sizeof(float) * m * n, hipMemcpyHostToDevice)); // Create rocsparse handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Types rocsparse_indextype itype = rocsparse_indextype_i32; rocsparse_indextype jtype = rocsparse_indextype_i32; rocsparse_datatype ttype = rocsparse_datatype_f32_r; // Create descriptors rocsparse_spmat_descr mat_A; rocsparse_dnmat_descr mat_B; rocsparse_dnmat_descr mat_C; ROCSPARSE_CHECK(rocsparse_create_csr_descr(&mat_A, m, k, nnz, dcsr_row_ptr, dcsr_col_ind, dcsr_val, itype, jtype, rocsparse_index_base_zero, ttype)); ROCSPARSE_CHECK( rocsparse_create_dnmat_descr(&mat_B, k, n, k, dB, ttype, rocsparse_order_column)); ROCSPARSE_CHECK( rocsparse_create_dnmat_descr(&mat_C, m, n, m, dC, ttype, rocsparse_order_column)); // Query SpMM buffer size_t buffer_size; ROCSPARSE_CHECK(rocsparse_spmm(handle, rocsparse_operation_none, rocsparse_operation_none, &alpha, mat_A, mat_B, &beta, mat_C, ttype, rocsparse_spmm_alg_default, rocsparse_spmm_stage_buffer_size, &buffer_size, nullptr)); // Allocate buffer void* buffer; HIP_CHECK(hipMalloc(&buffer, buffer_size)); ROCSPARSE_CHECK(rocsparse_spmm(handle, rocsparse_operation_none, rocsparse_operation_none, &alpha, mat_A, mat_B, &beta, mat_C, ttype, rocsparse_spmm_alg_default, rocsparse_spmm_stage_preprocess, &buffer_size, buffer)); // Pointer mode host ROCSPARSE_CHECK(rocsparse_spmm(handle, rocsparse_operation_none, rocsparse_operation_none, &alpha, mat_A, mat_B, &beta, mat_C, ttype, rocsparse_spmm_alg_default, rocsparse_spmm_stage_compute, &buffer_size, buffer)); // Clear up on device HIP_CHECK(hipFree(dcsr_row_ptr)); HIP_CHECK(hipFree(dcsr_col_ind)); HIP_CHECK(hipFree(dcsr_val)); HIP_CHECK(hipFree(dB)); HIP_CHECK(hipFree(dC)); HIP_CHECK(hipFree(buffer)); ROCSPARSE_CHECK(rocsparse_destroy_spmat_descr(mat_A)); ROCSPARSE_CHECK(rocsparse_destroy_dnmat_descr(mat_B)); ROCSPARSE_CHECK(rocsparse_destroy_dnmat_descr(mat_C)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); return 0; }

**Example**An example of the first batch mode ( \(C_i = A \times B_i\)) is provided below.

int main() { // 1 4 0 0 0 0 // A = 0 2 3 0 0 0 // 5 0 0 7 8 0 // 0 0 9 0 6 0 int m = 4; int k = 6; int n = 3; int batch_count_A = 1; int batch_count_B = 100; int batch_count_C = 100; std::vector<int> hcsr_row_ptr = {0, 2, 4, 7, 9}; std::vector<int> hcsr_col_ind = {0, 1, 1, 2, 0, 3, 4, 2, 4}; std::vector<float> hcsr_val = {1, 4, 2, 3, 5, 7, 8, 9, 6}; std::vector<float> hB(batch_count_B * k * n, 1.0f); std::vector<float> hC(batch_count_C * m * n, 1.0f); int nnz = hcsr_row_ptr[m] - hcsr_row_ptr[0]; int offsets_batch_stride_A = 0; int columns_values_batch_stride_A = 0; int batch_stride_B = k * n; int batch_stride_C = m * n; float alpha = 1.0f; float beta = 0.0f; // Create CSR arrays on device int* dcsr_row_ptr; int* dcsr_col_ind; float* dcsr_val; float* dB; float* dC; HIP_CHECK(hipMalloc(&dcsr_row_ptr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc(&dcsr_col_ind, sizeof(int) * nnz)); HIP_CHECK(hipMalloc(&dcsr_val, sizeof(float) * nnz)); HIP_CHECK(hipMalloc(&dB, sizeof(float) * batch_count_B * k * n)); HIP_CHECK(hipMalloc(&dC, sizeof(float) * batch_count_C * m * n)); HIP_CHECK( hipMemcpy(dcsr_row_ptr, hcsr_row_ptr.data(), sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsr_col_ind, hcsr_col_ind.data(), sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsr_val, hcsr_val.data(), sizeof(float) * nnz, hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dB, hB.data(), sizeof(float) * batch_count_B * k * n, hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dC, hC.data(), sizeof(float) * batch_count_C * m * n, hipMemcpyHostToDevice)); // Create rocsparse handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Types rocsparse_indextype itype = rocsparse_indextype_i32; rocsparse_indextype jtype = rocsparse_indextype_i32; rocsparse_datatype ttype = rocsparse_datatype_f32_r; // Create descriptors rocsparse_spmat_descr mat_A; rocsparse_dnmat_descr mat_B; rocsparse_dnmat_descr mat_C; ROCSPARSE_CHECK(rocsparse_create_csr_descr(&mat_A, m, k, nnz, dcsr_row_ptr, dcsr_col_ind, dcsr_val, itype, jtype, rocsparse_index_base_zero, ttype)); ROCSPARSE_CHECK( rocsparse_create_dnmat_descr(&mat_B, k, n, k, dB, ttype, rocsparse_order_column)); ROCSPARSE_CHECK( rocsparse_create_dnmat_descr(&mat_C, m, n, m, dC, ttype, rocsparse_order_column)); ROCSPARSE_CHECK(rocsparse_csr_set_strided_batch( mat_A, batch_count_A, offsets_batch_stride_A, columns_values_batch_stride_A)); ROCSPARSE_CHECK(rocsparse_dnmat_set_strided_batch(mat_B, batch_count_B, batch_stride_B)); ROCSPARSE_CHECK(rocsparse_dnmat_set_strided_batch(mat_C, batch_count_C, batch_stride_C)); // Query SpMM buffer size_t buffer_size; ROCSPARSE_CHECK(rocsparse_spmm(handle, rocsparse_operation_none, rocsparse_operation_none, &alpha, mat_A, mat_B, &beta, mat_C, ttype, rocsparse_spmm_alg_default, rocsparse_spmm_stage_buffer_size, &buffer_size, nullptr)); // Allocate buffer void* buffer; HIP_CHECK(hipMalloc(&buffer, buffer_size)); ROCSPARSE_CHECK(rocsparse_spmm(handle, rocsparse_operation_none, rocsparse_operation_none, &alpha, mat_A, mat_B, &beta, mat_C, ttype, rocsparse_spmm_alg_default, rocsparse_spmm_stage_preprocess, &buffer_size, buffer)); // Pointer mode host ROCSPARSE_CHECK(rocsparse_spmm(handle, rocsparse_operation_none, rocsparse_operation_none, &alpha, mat_A, mat_B, &beta, mat_C, ttype, rocsparse_spmm_alg_default, rocsparse_spmm_stage_compute, &buffer_size, buffer)); // Clear up on device HIP_CHECK(hipFree(dcsr_row_ptr)); HIP_CHECK(hipFree(dcsr_col_ind)); HIP_CHECK(hipFree(dcsr_val)); HIP_CHECK(hipFree(dB)); HIP_CHECK(hipFree(dC)); HIP_CHECK(hipFree(buffer)); ROCSPARSE_CHECK(rocsparse_destroy_spmat_descr(mat_A)); ROCSPARSE_CHECK(rocsparse_destroy_dnmat_descr(mat_B)); ROCSPARSE_CHECK(rocsparse_destroy_dnmat_descr(mat_C)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); return 0; }


Note

None of the algorithms above are deterministic when \(A\) is transposed or conjugate transposed.

Note

All algorithms perform best when using row ordering for the dense \(B\) and \(C\) matrices

Note

The sparse matrix formats currently supported are:

[rocsparse_format_coo](enumerations.html#rocsparse-types_8h_1ae1c0b9de06f3772ed14403400320b378a11b2282b2de9242f0b9a8607cf835423),[rocsparse_format_csr](enumerations.html#rocsparse-types_8h_1ae1c0b9de06f3772ed14403400320b378a26160296ec3d447960cf2f5958a2f84d),[rocsparse_format_csc](enumerations.html#rocsparse-types_8h_1ae1c0b9de06f3772ed14403400320b378af8fdd82ccbbc7b2f7386eae16f284e08),[rocsparse_format_bsr](enumerations.html#rocsparse-types_8h_1ae1c0b9de06f3772ed14403400320b378a4c2ead89d182bd7d7bb7bc6eccbc9bb6), and[rocsparse_format_bell](enumerations.html#rocsparse-types_8h_1ae1c0b9de06f3772ed14403400320b378a5371fc95604a0eca8059d7160f440741).Note

Mixed precisions only supported for BSR, CSR, CSC, and COO matrix formats.

Note

Only the

[rocsparse_spmm_stage_buffer_size](enumerations.html#rocsparse-types_8h_1a28daf89fa49ded50158dcda6e5045aafaef94fe80b7c181dd56d06df7eca379a1)stage and the[rocsparse_spmm_stage_compute](enumerations.html#rocsparse-types_8h_1a28daf89fa49ded50158dcda6e5045aafaeb9be614ccccf840f3f529786e037259)stage are non blocking and executed asynchronously with respect to the host. They may return before the actual computation has finished. The[rocsparse_spmm_stage_preprocess](enumerations.html#rocsparse-types_8h_1a28daf89fa49ded50158dcda6e5045aaface910c4e7024c7fff1c8749849126f2e)stage is blocking with respect to the host.Note

Currently, only

`trans_A`

==[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528)is supported for COO and Blocked ELL formats.Note

Only the

[rocsparse_spmm_stage_buffer_size](enumerations.html#rocsparse-types_8h_1a28daf89fa49ded50158dcda6e5045aafaef94fe80b7c181dd56d06df7eca379a1)stage and the[rocsparse_spmm_stage_compute](enumerations.html#rocsparse-types_8h_1a28daf89fa49ded50158dcda6e5045aafaeb9be614ccccf840f3f529786e037259)stage support execution in a hipGraph context. The[rocsparse_spmm_stage_preprocess](enumerations.html#rocsparse-types_8h_1a28daf89fa49ded50158dcda6e5045aaface910c4e7024c7fff1c8749849126f2e)stage does not support hipGraph.Note

Currently, only CSR, COO, BSR and Blocked ELL sparse formats are supported.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**trans_A**–**[in]**matrix operation type.**trans_B**–**[in]**matrix operation type.**alpha**–**[in]**scalar \(\alpha\).**mat_A**–**[in]**matrix descriptor.**mat_B**–**[in]**matrix descriptor.**beta**–**[in]**scalar \(\beta\).**mat_C**–**[in]**matrix descriptor.**compute_type**–**[in]**floating point precision for the SpMM computation.**alg**–**[in]**SpMM algorithm for the SpMM computation.**stage**–**[in]**SpMM stage for the SpMM computation.**buffer_size**–**[out]**number of bytes of the temporary storage buffer.**temp_buffer**–**[in]**temporary storage buffer allocated by the user. When the[rocsparse_spmm_stage_buffer_size](enumerations.html#rocsparse-types_8h_1a28daf89fa49ded50158dcda6e5045aafaef94fe80b7c181dd56d06df7eca379a1)stage is passed, the required allocation size (in bytes) is written to`buffer_size`

and function returns without performing the SpMM operation.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`alpha`

,`mat_A`

,`mat_B`

,`mat_C`

,`beta`

, or`buffer_size`

pointer is invalid.**rocsparse_status_not_implemented**–`trans_A`

,`trans_B`

,`compute_type`

or`alg`

is currently not supported.



## rocsparse_spgemm()[#](#rocsparse-spgemm)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_spgemm([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B, const void *alpha,[rocsparse_const_spmat_descr](types.html#_CPPv427rocsparse_const_spmat_descr)A,[rocsparse_const_spmat_descr](types.html#_CPPv427rocsparse_const_spmat_descr)B, const void *beta,[rocsparse_const_spmat_descr](types.html#_CPPv427rocsparse_const_spmat_descr)D,[rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)C,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)compute_type,[rocsparse_spgemm_alg](enumerations.html#_CPPv420rocsparse_spgemm_alg)alg,[rocsparse_spgemm_stage](enumerations.html#_CPPv422rocsparse_spgemm_stage)stage, size_t *buffer_size, void *temp_buffer)[#](#_CPPv416rocsparse_spgemm16rocsparse_handle19rocsparse_operation19rocsparse_operationPKv27rocsparse_const_spmat_descr27rocsparse_const_spmat_descrPKv27rocsparse_const_spmat_descr21rocsparse_spmat_descr18rocsparse_datatype20rocsparse_spgemm_alg22rocsparse_spgemm_stageP6size_tPv) Sparse matrix sparse matrix multiplication.

`rocsparse_spgemm`

multiplies the scalar \(\alpha\) with the sparse \(m \times k\) matrix \(op(A)\) and the sparse \(k \times n\) matrix \(op(B)\) and adds the result to the sparse \(m \times n\) matrix \(D\) that is multiplied by \(\beta\). The final result is stored in the sparse \(m \times n\) matrix \(C\), such that\[ C := \alpha \cdot op(A) \cdot op(B) + \beta \cdot D, \]with\[ op(A) = \left\{ \begin{array}{ll} A, & \text{if trans_A == rocsparse_operation_none} \end{array} \right. \]and\[ op(B) = \left\{ \begin{array}{ll} B, & \text{if trans_B == rocsparse_operation_none} \end{array} \right. \]`rocsparse_spgemm`

requires three stages to complete. First, the user passes the[rocsparse_spgemm_stage_buffer_size](enumerations.html#rocsparse-types_8h_1a66732fbd958d714d7cf5f57250d550b0ad8ea174ec74b7e7596847c5e3864fa28)stage to determine the size of the required temporary storage buffer. Next, the user allocates this buffer and calls`rocsparse_spgemm`

again with the[rocsparse_spgemm_stage_nnz](enumerations.html#rocsparse-types_8h_1a66732fbd958d714d7cf5f57250d550b0afd089e430f158fd2fb18c900345a1f32)stage which will determine the number of non-zeros in \(C\). This stage will also fill in the row pointer array of \(C\). Now that the number of non-zeros in \(C\) is known, the user allocates space for the column indices and values arrays of \(C\). Finally, the user calls`rocsparse_spgemm`

with the[rocsparse_spgemm_stage_compute](enumerations.html#rocsparse-types_8h_1a66732fbd958d714d7cf5f57250d550b0afac1ee9c06823f6cb6e92ee682e83369)stage to perform the actual computation which fills in the column indices and values arrays of \(C\). Once all calls to`rocsparse_spgemm`

are complete, the temporary buffer can be deallocated.Alternatively, the user may also want to perform sparse matrix products multiple times with matrices having the same sparsity pattern, but whose values differ. In this scenario, the process begins like before. First, the user calls

`rocsparse_spgemm`

with stage[rocsparse_spgemm_stage_buffer_size](enumerations.html#rocsparse-types_8h_1a66732fbd958d714d7cf5f57250d550b0ad8ea174ec74b7e7596847c5e3864fa28)to determine the required buffer size. The user again allocates this buffer and calls`rocsparse_spgemm`

with the stage[rocsparse_spgemm_stage_nnz](enumerations.html#rocsparse-types_8h_1a66732fbd958d714d7cf5f57250d550b0afd089e430f158fd2fb18c900345a1f32)to determine the number of non-zeros in \(C\). The user allocates the \(C\) column indices and values arrays. Now, however, the user calls`rocsparse_spgemm`

with the[rocsparse_spgemm_stage_symbolic](enumerations.html#rocsparse-types_8h_1a66732fbd958d714d7cf5f57250d550b0a4b045900ab0476f3c2f52001464da7fe)stage which will fill in the column indices array of \(C\) but not the values array. The user is then free to repeatedly change the values of \(A\), \(B\), and \(D\) and call`rocsparse_spgemm`

with the[rocsparse_spgemm_stage_numeric](enumerations.html#rocsparse-types_8h_1a66732fbd958d714d7cf5f57250d550b0a3ffc422431f5388cb851b30c86c394fc)stage which fill the values array of \(C\). The use of the extra[rocsparse_spgemm_stage_symbolic](enumerations.html#rocsparse-types_8h_1a66732fbd958d714d7cf5f57250d550b0a4b045900ab0476f3c2f52001464da7fe)and[rocsparse_spgemm_stage_numeric](enumerations.html#rocsparse-types_8h_1a66732fbd958d714d7cf5f57250d550b0a3ffc422431f5388cb851b30c86c394fc)stages allows the user to compute sparsity pattern of \(C\) once, but compute the values multiple times.`rocsparse_spgemm`

supports multiple combinations of data types and compute types. The tables below indicate the currently supported different data types that can be used for for the sparse matrices \(op(A)\), \(op(B)\), \(C\), and \(D\) and the compute type for \(\alpha\) and \(\beta\). The advantage of using different data types is to save on memory bandwidth and storage when a user application allows while performing the actual computation in a higher precision.`rocsparse_spgemm`

supports[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)and[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4)index precisions for storing the row pointer and column indices arrays of the sparse matrices.**Uniform Precisions:**A / B / C / D / compute_type

rocsparse_datatype_f32_r

rocsparse_datatype_f64_r

rocsparse_datatype_f32_c

rocsparse_datatype_f64_c


In general, when multiplying two sparse matrices together, it is entirely possible that the resulting matrix will require a larger index representation to store correctly. For example, when multiplying \(A \times B\) using

[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)index types for the row pointer and column indices arrays, it may be the case that the row pointer of the resulting \(C\) matrix would require index precision[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4). This is currently not supported. In this scenario, the user would need to store the \(A\) and \(B\) matrices using the higher index precision.**Example**int main() { // A - m x k // B - k x n // C - m x n int m = 4; int n = 4; int k = 3; // A // 1 2 3 // 0 1 0 // 2 0 0 // 0 0 3 // B // 0 1 2 0 // 0 0 0 1 // 1 2 3 4 std::vector<int> hcsr_row_ptr_A = {0, 3, 4, 5}; std::vector<int> hcsr_col_ind_A = {0, 1, 2, 1, 0, 2}; std::vector<float> hcsr_val_A = {1.0f, 2.0f, 3.0f, 1.0f, 2.0f, 3.0f}; std::vector<int> hcsr_row_ptr_B = {0, 2, 3, 7}; std::vector<int> hcsr_col_ind_B = {1, 2, 3, 0, 1, 2, 3}; std::vector<float> hcsr_val_B = {1.0f, 2.0f, 1.0f, 1.0f, 2.0f, 3.0f, 4.0f}; int nnz_A = hcsr_val_A.size(); int nnz_B = hcsr_val_B.size(); float alpha = 1.0f; float beta = 0.0f; int* dcsr_row_ptr_A; int* dcsr_col_ind_A; float* dcsr_val_A; int* dcsr_row_ptr_B; int* dcsr_col_ind_B; float* dcsr_val_B; int* dcsr_row_ptr_C; HIP_CHECK(hipMalloc(&dcsr_row_ptr_A, (m + 1) * sizeof(int))); HIP_CHECK(hipMalloc(&dcsr_col_ind_A, nnz_A * sizeof(int))); HIP_CHECK(hipMalloc(&dcsr_val_A, nnz_A * sizeof(float))); HIP_CHECK(hipMalloc(&dcsr_row_ptr_B, (k + 1) * sizeof(int))); HIP_CHECK(hipMalloc(&dcsr_col_ind_B, nnz_B * sizeof(int))); HIP_CHECK(hipMalloc(&dcsr_val_B, nnz_B * sizeof(float))); HIP_CHECK(hipMalloc(&dcsr_row_ptr_C, (m + 1) * sizeof(int))); HIP_CHECK(hipMemcpy( dcsr_row_ptr_A, hcsr_row_ptr_A.data(), (m + 1) * sizeof(int), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( dcsr_col_ind_A, hcsr_col_ind_A.data(), nnz_A * sizeof(int), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsr_val_A, hcsr_val_A.data(), nnz_A * sizeof(float), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( dcsr_row_ptr_B, hcsr_row_ptr_B.data(), (k + 1) * sizeof(int), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( dcsr_col_ind_B, hcsr_col_ind_B.data(), nnz_B * sizeof(int), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsr_val_B, hcsr_val_B.data(), nnz_B * sizeof(float), hipMemcpyHostToDevice)); rocsparse_handle handle; rocsparse_spmat_descr matA, matB, matC, matD; void* temp_buffer; size_t buffer_size = 0; rocsparse_operation trans_A = rocsparse_operation_none; rocsparse_operation trans_B = rocsparse_operation_none; rocsparse_index_base index_base = rocsparse_index_base_zero; rocsparse_indextype itype = rocsparse_indextype_i32; rocsparse_indextype jtype = rocsparse_indextype_i32; rocsparse_datatype ttype = rocsparse_datatype_f32_r; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Create sparse matrix A in CSR format ROCSPARSE_CHECK(rocsparse_create_csr_descr(&matA, m, k, nnz_A, dcsr_row_ptr_A, dcsr_col_ind_A, dcsr_val_A, itype, jtype, index_base, ttype)); // Create sparse matrix B in CSR format ROCSPARSE_CHECK(rocsparse_create_csr_descr(&matB, k, n, nnz_B, dcsr_row_ptr_B, dcsr_col_ind_B, dcsr_val_B, itype, jtype, index_base, ttype)); // Create sparse matrix C in CSR format ROCSPARSE_CHECK(rocsparse_create_csr_descr( &matC, m, n, 0, dcsr_row_ptr_C, nullptr, nullptr, itype, jtype, index_base, ttype)); // Create sparse matrix D in CSR format ROCSPARSE_CHECK(rocsparse_create_csr_descr( &matD, 0, 0, 0, nullptr, nullptr, nullptr, itype, jtype, index_base, ttype)); // Determine buffer size ROCSPARSE_CHECK(rocsparse_spgemm(handle, trans_A, trans_B, &alpha, matA, matB, &beta, matD, matC, ttype, rocsparse_spgemm_alg_default, rocsparse_spgemm_stage_buffer_size, &buffer_size, nullptr)); HIP_CHECK(hipMalloc(&temp_buffer, buffer_size)); // Determine number of non-zeros in C matrix ROCSPARSE_CHECK(rocsparse_spgemm(handle, trans_A, trans_B, &alpha, matA, matB, &beta, matD, matC, ttype, rocsparse_spgemm_alg_default, rocsparse_spgemm_stage_nnz, &buffer_size, temp_buffer)); int64_t rows_C; int64_t cols_C; int64_t nnz_C; // Extract number of non-zeros in C matrix so we can allocate the column indices and values arrays ROCSPARSE_CHECK(rocsparse_spmat_get_size(matC, &rows_C, &cols_C, &nnz_C)); std::cout << "rows_C: " << rows_C << " cols_C: " << cols_C << " nnz_C: " << nnz_C << std::endl; int* dcsr_col_ind_C; float* dcsr_val_C; HIP_CHECK(hipMalloc(&dcsr_col_ind_C, sizeof(int) * nnz_C)); HIP_CHECK(hipMalloc(&dcsr_val_C, sizeof(float) * nnz_C)); // Set C matrix pointers ROCSPARSE_CHECK(rocsparse_csr_set_pointers(matC, dcsr_row_ptr_C, dcsr_col_ind_C, dcsr_val_C)); // SpGEMM computation ROCSPARSE_CHECK(rocsparse_spgemm(handle, trans_A, trans_B, &alpha, matA, matB, &beta, matD, matC, ttype, rocsparse_spgemm_alg_default, rocsparse_spgemm_stage_compute, &buffer_size, temp_buffer)); // Copy C matrix result back to host std::vector<int> hcsr_row_ptr_C(m + 1); std::vector<int> hcsr_col_ind_C(nnz_C); std::vector<float> hcsr_val_C(nnz_C); HIP_CHECK(hipMemcpy( hcsr_row_ptr_C.data(), dcsr_row_ptr_C, sizeof(int) * (m + 1), hipMemcpyDeviceToHost)); HIP_CHECK(hipMemcpy( hcsr_col_ind_C.data(), dcsr_col_ind_C, sizeof(int) * nnz_C, hipMemcpyDeviceToHost)); HIP_CHECK( hipMemcpy(hcsr_val_C.data(), dcsr_val_C, sizeof(float) * nnz_C, hipMemcpyDeviceToHost)); // Destroy matrix descriptors ROCSPARSE_CHECK(rocsparse_destroy_spmat_descr(matA)); ROCSPARSE_CHECK(rocsparse_destroy_spmat_descr(matB)); ROCSPARSE_CHECK(rocsparse_destroy_spmat_descr(matC)); ROCSPARSE_CHECK(rocsparse_destroy_spmat_descr(matD)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); // Free device arrays HIP_CHECK(hipFree(temp_buffer)); HIP_CHECK(hipFree(dcsr_row_ptr_A)); HIP_CHECK(hipFree(dcsr_col_ind_A)); HIP_CHECK(hipFree(dcsr_val_A)); HIP_CHECK(hipFree(dcsr_row_ptr_B)); HIP_CHECK(hipFree(dcsr_col_ind_B)); HIP_CHECK(hipFree(dcsr_val_B)); HIP_CHECK(hipFree(dcsr_row_ptr_C)); HIP_CHECK(hipFree(dcsr_col_ind_C)); HIP_CHECK(hipFree(dcsr_val_C)); return 0; }


Note

This function does not produce deterministic results.

Note

SpGEMM requires three stages to complete. The first stage

[rocsparse_spgemm_stage_buffer_size](enumerations.html#rocsparse-types_8h_1a66732fbd958d714d7cf5f57250d550b0ad8ea174ec74b7e7596847c5e3864fa28)will return the size of the temporary storage buffer that is required for subsequent calls to[rocsparse_spgemm](#rocsparse__spgemm_8h_1ae7cd34d753355b52546dd1bb29e58381). The second stage[rocsparse_spgemm_stage_nnz](enumerations.html#rocsparse-types_8h_1a66732fbd958d714d7cf5f57250d550b0afd089e430f158fd2fb18c900345a1f32)will determine the number of non-zero elements of the resulting \(C\) matrix. If the sparsity pattern of \(C\) is already known, this stage can be skipped. In the final stage[rocsparse_spgemm_stage_compute](enumerations.html#rocsparse-types_8h_1a66732fbd958d714d7cf5f57250d550b0afac1ee9c06823f6cb6e92ee682e83369), the actual computation is performed.Note

If \(\alpha == 0\), then \(C = \beta \cdot D\) will be computed.

Note

If \(\beta == 0\), then \(C = \alpha \cdot op(A) \cdot op(B)\) will be computed.

Note

Currently only CSR and BSR formats are supported.

Note

If

[rocsparse_spgemm_stage_symbolic](enumerations.html#rocsparse-types_8h_1a66732fbd958d714d7cf5f57250d550b0a4b045900ab0476f3c2f52001464da7fe)is selected then the symbolic computation is performed only.Note

For the

[rocsparse_spgemm_stage_symbolic](enumerations.html#rocsparse-types_8h_1a66732fbd958d714d7cf5f57250d550b0a4b045900ab0476f3c2f52001464da7fe)and[rocsparse_spgemm_stage_numeric](enumerations.html#rocsparse-types_8h_1a66732fbd958d714d7cf5f57250d550b0a3ffc422431f5388cb851b30c86c394fc)stages, only CSR matrix format is currently supported.Note

\(\alpha == beta == 0\) is invalid.

Note

It is allowed to pass the same sparse matrix for \(C\) and \(D\), if both matrices have the same sparsity pattern.

Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

Please note, that for rare matrix products with more than 4096 non-zero entries per row, additional temporary storage buffer is allocated by the algorithm.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**trans_A**–**[in]**sparse matrix \(A\) operation type.**trans_B**–**[in]**sparse matrix \(B\) operation type.**alpha**–**[in]**scalar \(\alpha\).**A**–**[in]**sparse matrix \(A\) descriptor.**B**–**[in]**sparse matrix \(B\) descriptor.**beta**–**[in]**scalar \(\beta\).**D**–**[in]**sparse matrix \(D\) descriptor.**C**–**[out]**sparse matrix \(C\) descriptor.**compute_type**–**[in]**floating point precision for the SpGEMM computation.**alg**–**[in]**SpGEMM algorithm for the SpGEMM computation.**stage**–**[in]**SpGEMM stage for the SpGEMM computation.**buffer_size**–**[out]**number of bytes of the temporary storage buffer. buffer_size is set when`temp_buffer`

is nullptr.**temp_buffer**–**[in]**temporary storage buffer allocated by the user. When a nullptr is passed, the required allocation size (in bytes) is written to`buffer_size`

and function returns without performing the SpGEMM operation.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`alpha`

and`beta`

are invalid,`A`

,`B`

,`D`

,`C`

or`buffer_size`

pointer is invalid.**rocsparse_status_memory_error**– additional buffer for long rows could not be allocated.**rocsparse_status_not_implemented**–`trans_A`

!=[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528)or`trans_B`

!=[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528).



## rocsparse_spgeam_buffer_size()[#](#rocsparse-spgeam-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_spgeam_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, rocsparse_spgeam_descr descr,[rocsparse_const_spmat_descr](types.html#_CPPv427rocsparse_const_spmat_descr)mat_A,[rocsparse_const_spmat_descr](types.html#_CPPv427rocsparse_const_spmat_descr)mat_B,[rocsparse_const_spmat_descr](types.html#_CPPv427rocsparse_const_spmat_descr)mat_C,[rocsparse_spgeam_stage](enumerations.html#_CPPv422rocsparse_spgeam_stage)stage, size_t *buffer_size,[rocsparse_error](types.html#_CPPv415rocsparse_error)*error)[#](#_CPPv428rocsparse_spgeam_buffer_size16rocsparse_handle22rocsparse_spgeam_descr27rocsparse_const_spmat_descr27rocsparse_const_spmat_descr27rocsparse_const_spmat_descr22rocsparse_spgeam_stageP6size_tP15rocsparse_error) `rocsparse_spgeam_buffer_size`

returns the size of the required buffer to execute the given stage of the SpGEAM operation. This routine is used in conjunction with[rocsparse_spgeam()](#rocsparse__spgeam_8h_1ac6994d8e5bbf8af3b275d193de933f92). See[rocsparse_spgeam](#rocsparse__spgeam_8h_1ac6994d8e5bbf8af3b275d193de933f92)for full description and example.Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**descr**–**[in]**SpGEAM descriptor**mat_A**–**[in]**sparse matrix \(A\) descriptor.**mat_B**–**[in]**sparse matrix \(B\) descriptor.**mat_C**–**[in]**sparse matrix \(C\) descriptor.**stage**–**[in]**SpGEAM stage for the SpGEAM computation.**buffer_size**–**[out]**number of bytes of the temporary storage buffer.**error**–**[out]**error descriptor created if the returned status is not[rocsparse_status_success](enumerations.html#rocsparse-types_8h_1a578f8c5c1b08f358bf4605b0031006a8a96462a9361cfceb6cf9354e10fdc671b). A null pointer can be passed if the user is not interested in obtaining an error descriptor.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`mat_A`

,`mat_B`

,`descr`

or`buffer_size`

pointer is invalid.



## rocsparse_spgeam()[#](#rocsparse-spgeam)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_spgeam([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, rocsparse_spgeam_descr descr,[rocsparse_const_spmat_descr](types.html#_CPPv427rocsparse_const_spmat_descr)mat_A,[rocsparse_const_spmat_descr](types.html#_CPPv427rocsparse_const_spmat_descr)mat_B,[rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)mat_C,[rocsparse_spgeam_stage](enumerations.html#_CPPv422rocsparse_spgeam_stage)stage, size_t buffer_size, void *temp_buffer,[rocsparse_error](types.html#_CPPv415rocsparse_error)*error)[#](#_CPPv416rocsparse_spgeam16rocsparse_handle22rocsparse_spgeam_descr27rocsparse_const_spmat_descr27rocsparse_const_spmat_descr21rocsparse_spmat_descr22rocsparse_spgeam_stage6size_tPvP15rocsparse_error) Sparse matrix sparse matrix addition.

`rocsparse_spgeam`

multiplies the scalar \(\alpha\) with the sparse \(m \times n\) CSR matrix \(op(A)\) and adds it to \(\beta\) multiplied by the sparse \(m \times n\) matrix \(op(B)\). The final result is stored in the sparse \(m \times n\) matrix \(C\), such that\[ C := \alpha op(A) + \beta op(B), \]with\[ op(A) = \left\{ \begin{array}{ll} A, & \text{if trans_A == rocsparse_operation_none} \end{array} \right. \]and\[ op(B) = \left\{ \begin{array}{ll} B, & \text{if trans_B == rocsparse_operation_none} \end{array} \right. \]`rocsparse_spgeam`

requires multiple steps to complete. First, the user must create a rocsparse_spgeam_descr by calling[rocsparse_create_spgeam_descr](auxiliary.html#rocsparse-auxiliary_8h_1ac2ffc31c2f2d3eb4e3ec50be1f53930c). The user sets the SpGEAM algorithm (currently only[rocsparse_spgeam_alg_default](enumerations.html#rocsparse-types_8h_1a8adf9059fb87b3047c50bd347c8c4e13a560b366e01843ccf4d362952e86cd793)supported) as well as the compute type and the transpose operation type for the sparse matrices \(op(A)\) and \(op(B)\) using[rocsparse_spgeam_set_input](auxiliary.html#rocsparse-auxiliary_8h_1aac76dcc7137f24777fa7042572be1de4). Next, the user must calculate the total nonzeros that will exist in the sparse matrix \(C\). To do so, the user calls[rocsparse_spgeam_buffer_size](#rocsparse__spgeam_8h_1aefc21d68d17849c7efef71b3347a0427)with the stage set to[rocsparse_spgeam_stage_analysis](enumerations.html#rocsparse-types_8h_1a5ccf6f0e1c8b62b7a85fdf6dac13d221a46d29d5d2b8f9c8fc244676b0d5785f4). This will fill the`buffer_size`

parameter allowing the user to then allocate this buffer. Once the buffer has been allocated, the user calls`rocsparse_spgeam`

with the same stage[rocsparse_spgeam_stage_analysis](enumerations.html#rocsparse-types_8h_1a5ccf6f0e1c8b62b7a85fdf6dac13d221a46d29d5d2b8f9c8fc244676b0d5785f4). The total nonzeros and the row offset array for \(C\) has now been calculated and is stored internally in the rocsparse_spgeam_descr. The user now needs to retrieve the nonzero count using[rocsparse_spgeam_get_output](auxiliary.html#rocsparse-auxiliary_8h_1a77096be6022a4424ab0ce98049dc8b77)and then allocate the \(C\) matrix. To complete the computation, the user repeats the process (this time passing the stage[rocsparse_spgeam_stage_compute](enumerations.html#rocsparse-types_8h_1a5ccf6f0e1c8b62b7a85fdf6dac13d221ad116559840a8c98322f7776e0ddad822)) by calling[rocsparse_spgeam_buffer_size](#rocsparse__spgeam_8h_1aefc21d68d17849c7efef71b3347a0427)to determine the required buffer size, then allocating the buffer, and finally calling`rocsparse_spgeam`

. The user allocated buffers can be freed after each call to`rocsparse_spgeam`

. Once the computation is complete and the SpGEAM descriptor is no longer needed, the user must call[rocsparse_destroy_spgeam_descr](auxiliary.html#rocsparse-auxiliary_8h_1ac42912b876ff984b693a50d322193529). See full code example below.The stage

[rocsparse_spgeam_stage_compute](enumerations.html#rocsparse-types_8h_1a5ccf6f0e1c8b62b7a85fdf6dac13d221ad116559840a8c98322f7776e0ddad822)computes the symbolic part and the numeric of the resulting matrix C. If the user wants to perform multiple operations involving matrices of same sparsity patterns but with different numerical values, then the symbolic stages ([rocsparse_spgeam_stage_symbolic_analysis](enumerations.html#rocsparse-types_8h_1a5ccf6f0e1c8b62b7a85fdf6dac13d221aa0cd71a8bfd9030ffd62a8a8b2cc6493)and[rocsparse_spgeam_stage_symbolic_compute](enumerations.html#rocsparse-types_8h_1a5ccf6f0e1c8b62b7a85fdf6dac13d221adc466c3ed3432910266e40d352fe4ef1)) and the numeric stages ([rocsparse_spgeam_stage_numeric_analysis](enumerations.html#rocsparse-types_8h_1a5ccf6f0e1c8b62b7a85fdf6dac13d221a3f59bb753d58f155b9d5822724924f84)and[rocsparse_spgeam_stage_numeric_compute](enumerations.html#rocsparse-types_8h_1a5ccf6f0e1c8b62b7a85fdf6dac13d221a0f45ba1e5caacfca0ea8fdde666f0bce)) can be used to separate the symbolic calculation from the numeric calculation.`rocsparse_spgeam`

supports multiple combinations of index types, data types, and compute types. The tables below indicate the currently supported different index and data types that can be used for the sparse matrices \(op(A)\), \(op(B)\), and \(C\), and the compute type for \(\alpha\) and \(\beta\). The advantage of using different index and data types is to save on memory bandwidth and storage when a user application allows while performing the actual computation in a higher precision.In general, when adding two sparse matrices together, it is entirely possible that the resulting matrix will require a a larger index representation to store correctly. For example, when adding \(A + B\) using

[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)index types for the row pointer and column indices arrays, it may be the case that the row pointer of the resulting \(C\) matrix would require index type[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4). This is currently not supported. In this scenario, the user would need to store the \(A\), \(B\), and \(C\) matrices using the higher index precision.**Uniform Precisions:**A / B / C / compute_type

rocsparse_datatype_f32_r

rocsparse_datatype_f64_r

rocsparse_datatype_f32_c

rocsparse_datatype_f64_c

**Uniform Index Types:**CSR Row offset

CSR Column indices

rocsparse_datatype_f32_r

rocsparse_datatype_f32_r

rocsparse_datatype_f64_r

rocsparse_datatype_f64_r

**Mixed Index Types:**CSR Row offset

CSR Column indices

rocsparse_datatype_f64_r

rocsparse_datatype_f32_r


Additionally, all three matrices \(A\), \(B\), and \(C\) must use the same index types. For example, if \(A\) uses the index type

[rocsparse_datatype_f32_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edaa62d4737b4cdb93a7f60715db0d01520)for the row offset array and the index type[rocsparse_datatype_f32_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edaa62d4737b4cdb93a7f60715db0d01520)for the column indices array, then both \(B\) and \(C\) must also use these same index types for their respective row offset and column index arrays. In the scenario where \(C\) requires a larger index type for the row offset array, the user would need to store all three matrices using the larger index type[rocsparse_datatype_f64_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda2ca573746a15c391064033943edcebdb)for the row offsets array.**First Example**int main() { // A - m x n // B - m x n // C - m x n int m = 4; int n = 6; // 1 2 0 0 3 7 // 0 0 1 4 6 8 // 0 2 0 4 0 0 // 9 8 0 0 2 0 std::vector<int> hcsr_row_ptr_A = {0, 4, 8, 10, 13}; // host A m x n matrix std::vector<int> hcsr_col_ind_A = {0, 1, 4, 5, 2, 3, 4, 5, 1, 3, 0, 1, 4}; // host A m x n matrix std::vector<float> hcsr_val_A = {1, 2, 3, 7, 1, 4, 6, 8, 2, 4, 9, 8, 2}; // host A m x n matrix // 0 2 1 0 0 5 // 0 1 1 3 0 2 // 0 0 0 0 0 0 // 1 2 3 4 5 6 std::vector<int> hcsr_row_ptr_B = {0, 3, 7, 7, 13}; // host B m x n matrix std::vector<int> hcsr_col_ind_B = {1, 2, 5, 1, 2, 3, 5, 0, 1, 2, 3, 4, 5}; // host B m x n matrix std::vector<float> hcsr_val_B = {2, 1, 5, 1, 1, 3, 2, 1, 2, 3, 4, 5, 6}; // host B m x n matrix int nnz_A = hcsr_val_A.size(); int nnz_B = hcsr_val_B.size(); float alpha = 1.0f; float beta = 1.0f; int* dcsr_row_ptr_A; int* dcsr_col_ind_A; float* dcsr_val_A; int* dcsr_row_ptr_B; int* dcsr_col_ind_B; float* dcsr_val_B; HIP_CHECK(hipMalloc(&dcsr_row_ptr_A, (m + 1) * sizeof(int))); HIP_CHECK(hipMalloc(&dcsr_col_ind_A, nnz_A * sizeof(int))); HIP_CHECK(hipMalloc(&dcsr_val_A, nnz_A * sizeof(float))); HIP_CHECK(hipMalloc(&dcsr_row_ptr_B, (m + 1) * sizeof(int))); HIP_CHECK(hipMalloc(&dcsr_col_ind_B, nnz_B * sizeof(int))); HIP_CHECK(hipMalloc(&dcsr_val_B, nnz_B * sizeof(float))); HIP_CHECK(hipMemcpy( dcsr_row_ptr_A, hcsr_row_ptr_A.data(), (m + 1) * sizeof(int), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( dcsr_col_ind_A, hcsr_col_ind_A.data(), nnz_A * sizeof(int), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsr_val_A, hcsr_val_A.data(), nnz_A * sizeof(float), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( dcsr_row_ptr_B, hcsr_row_ptr_B.data(), (m + 1) * sizeof(int), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( dcsr_col_ind_B, hcsr_col_ind_B.data(), nnz_B * sizeof(int), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsr_val_B, hcsr_val_B.data(), nnz_B * sizeof(float), hipMemcpyHostToDevice)); rocsparse_handle handle; rocsparse_error p_error[1] = {}; rocsparse_spmat_descr matA, matB, matC; rocsparse_index_base index_base = rocsparse_index_base_zero; rocsparse_indextype itype = rocsparse_indextype_i32; rocsparse_indextype jtype = rocsparse_indextype_i32; rocsparse_datatype ttype = rocsparse_datatype_f32_r; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); hipStream_t stream; ROCSPARSE_CHECK(rocsparse_get_stream(handle, &stream)); // Create sparse matrix A in CSR format ROCSPARSE_CHECK(rocsparse_create_csr_descr(&matA, m, n, nnz_A, dcsr_row_ptr_A, dcsr_col_ind_A, dcsr_val_A, itype, jtype, index_base, ttype)); // Create sparse matrix B in CSR format ROCSPARSE_CHECK(rocsparse_create_csr_descr(&matB, m, n, nnz_B, dcsr_row_ptr_B, dcsr_col_ind_B, dcsr_val_B, itype, jtype, index_base, ttype)); // Create SpGEAM descriptor. rocsparse_spgeam_descr descr; ROCSPARSE_CHECK(rocsparse_create_spgeam_descr(&descr)); // Set the algorithm on the descriptor const rocsparse_spgeam_alg alg = rocsparse_spgeam_alg_default; ROCSPARSE_CHECK(rocsparse_spgeam_set_input( handle, descr, rocsparse_spgeam_input_alg, &alg, sizeof(alg), p_error)); // Set the transpose operation for sparses matrix A and B on the descriptor const rocsparse_operation trans_A = rocsparse_operation_none; const rocsparse_operation trans_B = rocsparse_operation_none; ROCSPARSE_CHECK(rocsparse_spgeam_set_input( handle, descr, rocsparse_spgeam_input_operation_A, &trans_A, sizeof(trans_A), p_error)); ROCSPARSE_CHECK(rocsparse_spgeam_set_input( handle, descr, rocsparse_spgeam_input_operation_B, &trans_B, sizeof(trans_B), p_error)); // Set the scalar type on the descriptor const rocsparse_datatype scalar_datatype = rocsparse_datatype_f32_r; ROCSPARSE_CHECK(rocsparse_spgeam_set_input(handle, descr, rocsparse_spgeam_input_scalar_datatype, &scalar_datatype, sizeof(scalar_datatype), p_error)); // Set the compute type on the descriptor const rocsparse_datatype compute_datatype = rocsparse_datatype_f32_r; ROCSPARSE_CHECK(rocsparse_spgeam_set_input(handle, descr, rocsparse_spgeam_input_compute_datatype, &compute_datatype, sizeof(compute_datatype), p_error)); // Calculate NNZ phase size_t buffer_size_in_bytes; void* buffer; ROCSPARSE_CHECK(rocsparse_spgeam_buffer_size(handle, descr, matA, matB, nullptr, rocsparse_spgeam_stage_analysis, &buffer_size_in_bytes, p_error)); HIP_CHECK(hipMalloc(&buffer, buffer_size_in_bytes)); ROCSPARSE_CHECK(rocsparse_spgeam(handle, descr, matA, matB, nullptr, rocsparse_spgeam_stage_analysis, buffer_size_in_bytes, buffer, p_error)); HIP_CHECK(hipFree(buffer)); // Ensure analysis stage is complete before grabbing C non-zero count HIP_CHECK(hipStreamSynchronize(stream)); int64_t nnz_C; ROCSPARSE_CHECK(rocsparse_spgeam_get_output( handle, descr, rocsparse_spgeam_output_nnz, &nnz_C, sizeof(int64_t), p_error)); // Compute column indices and values of C int* dcsr_row_ptr_C; int* dcsr_col_ind_C; float* dcsr_val_C; HIP_CHECK(hipMalloc(&dcsr_row_ptr_C, (m + 1) * sizeof(int))); HIP_CHECK(hipMalloc(&dcsr_col_ind_C, sizeof(int32_t) * nnz_C)); HIP_CHECK(hipMalloc(&dcsr_val_C, sizeof(float) * nnz_C)); // Create sparse matrix C in CSR format ROCSPARSE_CHECK(rocsparse_create_csr_descr(&matC, m, n, nnz_C, dcsr_row_ptr_C, dcsr_col_ind_C, dcsr_val_C, itype, jtype, index_base, ttype)); // Compute phase ROCSPARSE_CHECK(rocsparse_spgeam_buffer_size(handle, descr, matA, matB, matC, rocsparse_spgeam_stage_compute, &buffer_size_in_bytes, p_error)); // Set alpha and beta ROCSPARSE_CHECK(rocsparse_spgeam_set_input( handle, descr, rocsparse_spgeam_input_scalar_alpha, &alpha, sizeof(&alpha), p_error)); ROCSPARSE_CHECK(rocsparse_spgeam_set_input( handle, descr, rocsparse_spgeam_input_scalar_beta, &beta, sizeof(&beta), p_error)); HIP_CHECK(hipMalloc(&buffer, buffer_size_in_bytes)); ROCSPARSE_CHECK(rocsparse_spgeam(handle, descr, matA, matB, matC, rocsparse_spgeam_stage_compute, buffer_size_in_bytes, buffer, p_error)); HIP_CHECK(hipFree(buffer)); // Copy C matrix result back to host std::vector<int> hcsr_row_ptr_C(m + 1); std::vector<int> hcsr_col_ind_C(nnz_C); std::vector<float> hcsr_val_C(nnz_C); HIP_CHECK(hipMemcpy( hcsr_row_ptr_C.data(), dcsr_row_ptr_C, sizeof(int) * (m + 1), hipMemcpyDeviceToHost)); HIP_CHECK(hipMemcpy( hcsr_col_ind_C.data(), dcsr_col_ind_C, sizeof(int) * nnz_C, hipMemcpyDeviceToHost)); HIP_CHECK( hipMemcpy(hcsr_val_C.data(), dcsr_val_C, sizeof(float) * nnz_C, hipMemcpyDeviceToHost)); std::cout << "C" << std::endl; for(int i = 0; i < m; i++) { int start = hcsr_row_ptr_C[i]; int end = hcsr_row_ptr_C[i + 1]; std::vector<float> htemp(n, 0.0f); for(int j = start; j < end; j++) { htemp[hcsr_col_ind_C[j]] = hcsr_val_C[j]; } for(int j = 0; j < n; j++) { std::cout << htemp[j] << " "; } std::cout << "" << std::endl; } std::cout << "" << std::endl; // Destroy matrix descriptors ROCSPARSE_CHECK(rocsparse_destroy_spmat_descr(matA)); ROCSPARSE_CHECK(rocsparse_destroy_spmat_descr(matB)); ROCSPARSE_CHECK(rocsparse_destroy_spmat_descr(matC)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); ROCSPARSE_CHECK(rocsparse_destroy_error(p_error[0])); // Free device arrays HIP_CHECK(hipFree(dcsr_row_ptr_A)); HIP_CHECK(hipFree(dcsr_col_ind_A)); HIP_CHECK(hipFree(dcsr_val_A)); HIP_CHECK(hipFree(dcsr_row_ptr_B)); HIP_CHECK(hipFree(dcsr_col_ind_B)); HIP_CHECK(hipFree(dcsr_val_B)); HIP_CHECK(hipFree(dcsr_row_ptr_C)); HIP_CHECK(hipFree(dcsr_col_ind_C)); HIP_CHECK(hipFree(dcsr_val_C)); return 0; }

**Second Example**int main() { // A - m x n // B - m x n // C - m x n int m = 4; int n = 6; // 1 2 0 0 3 7 // 0 0 1 4 6 8 // 0 2 0 4 0 0 // 9 8 0 0 2 0 std::vector<int> hcsr_row_ptr_A = {0, 4, 8, 10, 13}; // host A m x n matrix std::vector<int> hcsr_col_ind_A = {0, 1, 4, 5, 2, 3, 4, 5, 1, 3, 0, 1, 4}; // host A m x n matrix std::vector<float> hcsr_val_A = {1, 2, 3, 7, 1, 4, 6, 8, 2, 4, 9, 8, 2}; // host A m x n matrix // 0 2 1 0 0 5 // 0 1 1 3 0 2 // 0 0 0 0 0 0 // 1 2 3 4 5 6 std::vector<int> hcsr_row_ptr_B = {0, 3, 7, 7, 13}; // host B m x n matrix std::vector<int> hcsr_col_ind_B = {1, 2, 5, 1, 2, 3, 5, 0, 1, 2, 3, 4, 5}; // host B m x n matrix std::vector<float> hcsr_val_B = {2, 1, 5, 1, 1, 3, 2, 1, 2, 3, 4, 5, 6}; // host B m x n matrix int nnz_A = hcsr_val_A.size(); int nnz_B = hcsr_val_B.size(); float alpha = 1.0f; float beta = 1.0f; int* dcsr_row_ptr_A; int* dcsr_col_ind_A; float* dcsr_val_A; int* dcsr_row_ptr_B; int* dcsr_col_ind_B; float* dcsr_val_B; HIP_CHECK(hipMalloc(&dcsr_row_ptr_A, (m + 1) * sizeof(int))); HIP_CHECK(hipMalloc(&dcsr_col_ind_A, nnz_A * sizeof(int))); HIP_CHECK(hipMalloc(&dcsr_val_A, nnz_A * sizeof(float))); HIP_CHECK(hipMalloc(&dcsr_row_ptr_B, (m + 1) * sizeof(int))); HIP_CHECK(hipMalloc(&dcsr_col_ind_B, nnz_B * sizeof(int))); HIP_CHECK(hipMalloc(&dcsr_val_B, nnz_B * sizeof(float))); HIP_CHECK(hipMemcpy( dcsr_row_ptr_A, hcsr_row_ptr_A.data(), (m + 1) * sizeof(int), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( dcsr_col_ind_A, hcsr_col_ind_A.data(), nnz_A * sizeof(int), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsr_val_A, hcsr_val_A.data(), nnz_A * sizeof(float), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( dcsr_row_ptr_B, hcsr_row_ptr_B.data(), (m + 1) * sizeof(int), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( dcsr_col_ind_B, hcsr_col_ind_B.data(), nnz_B * sizeof(int), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsr_val_B, hcsr_val_B.data(), nnz_B * sizeof(float), hipMemcpyHostToDevice)); rocsparse_handle handle; rocsparse_error p_error[1] = {}; rocsparse_spmat_descr matA, matB, matC; rocsparse_index_base index_base = rocsparse_index_base_zero; rocsparse_indextype itype = rocsparse_indextype_i32; rocsparse_indextype jtype = rocsparse_indextype_i32; rocsparse_datatype ttype = rocsparse_datatype_f32_r; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); hipStream_t stream; ROCSPARSE_CHECK(rocsparse_get_stream(handle, &stream)); // Create sparse matrix A in CSR format ROCSPARSE_CHECK(rocsparse_create_csr_descr(&matA, m, n, nnz_A, dcsr_row_ptr_A, dcsr_col_ind_A, dcsr_val_A, itype, jtype, index_base, ttype)); // Create sparse matrix B in CSR format ROCSPARSE_CHECK(rocsparse_create_csr_descr(&matB, m, n, nnz_B, dcsr_row_ptr_B, dcsr_col_ind_B, dcsr_val_B, itype, jtype, index_base, ttype)); // Create SpGEAM descriptor. rocsparse_spgeam_descr descr; ROCSPARSE_CHECK(rocsparse_create_spgeam_descr(&descr)); // Set the algorithm on the descriptor const rocsparse_spgeam_alg alg = rocsparse_spgeam_alg_default; ROCSPARSE_CHECK(rocsparse_spgeam_set_input( handle, descr, rocsparse_spgeam_input_alg, &alg, sizeof(alg), p_error)); // Set the transpose operation for sparses matrix A and B on the descriptor const rocsparse_operation trans_A = rocsparse_operation_none; const rocsparse_operation trans_B = rocsparse_operation_none; ROCSPARSE_CHECK(rocsparse_spgeam_set_input( handle, descr, rocsparse_spgeam_input_operation_A, &trans_A, sizeof(trans_A), p_error)); ROCSPARSE_CHECK(rocsparse_spgeam_set_input( handle, descr, rocsparse_spgeam_input_operation_B, &trans_B, sizeof(trans_B), p_error)); // Set the scalar type on the descriptor const rocsparse_datatype scalar_datatype = rocsparse_datatype_f32_r; ROCSPARSE_CHECK(rocsparse_spgeam_set_input(handle, descr, rocsparse_spgeam_input_scalar_datatype, &scalar_datatype, sizeof(scalar_datatype), p_error)); // Set alpha and beta. ROCSPARSE_CHECK(rocsparse_spgeam_set_input( handle, descr, rocsparse_spgeam_input_scalar_alpha, &alpha, sizeof(&alpha), p_error)); ROCSPARSE_CHECK(rocsparse_spgeam_set_input( handle, descr, rocsparse_spgeam_input_scalar_beta, &beta, sizeof(&beta), p_error)); // Set the compute type on the descriptor const rocsparse_datatype compute_datatype = rocsparse_datatype_f32_r; ROCSPARSE_CHECK(rocsparse_spgeam_set_input(handle, descr, rocsparse_spgeam_input_compute_datatype, &compute_datatype, sizeof(compute_datatype), p_error)); // Calculate NNZ phase size_t buffer_size_in_bytes; void* buffer; ROCSPARSE_CHECK(rocsparse_spgeam_buffer_size(handle, descr, matA, matB, nullptr, rocsparse_spgeam_stage_symbolic_analysis, &buffer_size_in_bytes, p_error)); HIP_CHECK(hipMalloc(&buffer, buffer_size_in_bytes)); ROCSPARSE_CHECK(rocsparse_spgeam(handle, descr, matA, matB, nullptr, rocsparse_spgeam_stage_symbolic_analysis, buffer_size_in_bytes, buffer, p_error)); HIP_CHECK(hipFree(buffer)); // Ensure analysis stage is complete before grabbing C non-zero count HIP_CHECK(hipStreamSynchronize(stream)); int64_t nnz_C; ROCSPARSE_CHECK(rocsparse_spgeam_get_output( handle, descr, rocsparse_spgeam_output_nnz, &nnz_C, sizeof(int64_t), p_error)); // Compute column indices and values of C int* dcsr_row_ptr_C; int* dcsr_col_ind_C; float* dcsr_val_C; HIP_CHECK(hipMalloc(&dcsr_row_ptr_C, (m + 1) * sizeof(int))); HIP_CHECK(hipMalloc(&dcsr_col_ind_C, sizeof(int32_t) * nnz_C)); HIP_CHECK(hipMalloc(&dcsr_val_C, sizeof(float) * nnz_C)); // Create sparse matrix C in CSR format ROCSPARSE_CHECK(rocsparse_create_csr_descr(&matC, m, n, nnz_C, dcsr_row_ptr_C, dcsr_col_ind_C, dcsr_val_C, itype, jtype, index_base, ttype)); // Symbolic compute phase ROCSPARSE_CHECK(rocsparse_spgeam_buffer_size(handle, descr, matA, matB, matC, rocsparse_spgeam_stage_symbolic_compute, &buffer_size_in_bytes, p_error)); HIP_CHECK(hipMalloc(&buffer, buffer_size_in_bytes)); ROCSPARSE_CHECK(rocsparse_spgeam(handle, descr, matA, matB, matC, rocsparse_spgeam_stage_symbolic_compute, buffer_size_in_bytes, buffer, p_error)); HIP_CHECK(hipFree(buffer)); ROCSPARSE_CHECK(rocsparse_spgeam_buffer_size(handle, descr, matA, matB, matC, rocsparse_spgeam_stage_numeric_analysis, &buffer_size_in_bytes, p_error)); HIP_CHECK(hipMalloc(&buffer, buffer_size_in_bytes)); ROCSPARSE_CHECK(rocsparse_spgeam(handle, descr, matA, matB, matC, rocsparse_spgeam_stage_numeric_analysis, buffer_size_in_bytes, buffer, p_error)); HIP_CHECK(hipFree(buffer)); // First Numeric compute phase ROCSPARSE_CHECK(rocsparse_spgeam_buffer_size(handle, descr, matA, matB, matC, rocsparse_spgeam_stage_numeric_compute, &buffer_size_in_bytes, p_error)); HIP_CHECK(hipMalloc(&buffer, buffer_size_in_bytes)); ROCSPARSE_CHECK(rocsparse_spgeam(handle, descr, matA, matB, matC, rocsparse_spgeam_stage_numeric_compute, buffer_size_in_bytes, buffer, p_error)); HIP_CHECK(hipFree(buffer)); // Second numeric compute phase hcsr_val_B[0] += 0.125; hcsr_val_B[1] += 0.5; HIP_CHECK( hipMemcpy(dcsr_val_B, hcsr_val_B.data(), nnz_B * sizeof(float), hipMemcpyHostToDevice)); HIP_CHECK(hipMalloc(&buffer, buffer_size_in_bytes)); ROCSPARSE_CHECK(rocsparse_spgeam(handle, descr, matA, matB, matC, rocsparse_spgeam_stage_numeric_compute, buffer_size_in_bytes, buffer, p_error)); HIP_CHECK(hipFree(buffer)); // Copy C matrix result back to host std::vector<int> hcsr_row_ptr_C(m + 1); std::vector<int> hcsr_col_ind_C(nnz_C); std::vector<float> hcsr_val_C(nnz_C); HIP_CHECK(hipMemcpy( hcsr_row_ptr_C.data(), dcsr_row_ptr_C, sizeof(int) * (m + 1), hipMemcpyDeviceToHost)); HIP_CHECK(hipMemcpy( hcsr_col_ind_C.data(), dcsr_col_ind_C, sizeof(int) * nnz_C, hipMemcpyDeviceToHost)); HIP_CHECK( hipMemcpy(hcsr_val_C.data(), dcsr_val_C, sizeof(float) * nnz_C, hipMemcpyDeviceToHost)); // Destroy matrix descriptors ROCSPARSE_CHECK(rocsparse_destroy_spmat_descr(matA)); ROCSPARSE_CHECK(rocsparse_destroy_spmat_descr(matB)); ROCSPARSE_CHECK(rocsparse_destroy_spmat_descr(matC)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); ROCSPARSE_CHECK(rocsparse_destroy_error(p_error[0])); // Free device arrays HIP_CHECK(hipFree(dcsr_row_ptr_A)); HIP_CHECK(hipFree(dcsr_col_ind_A)); HIP_CHECK(hipFree(dcsr_val_A)); HIP_CHECK(hipFree(dcsr_row_ptr_B)); HIP_CHECK(hipFree(dcsr_col_ind_B)); HIP_CHECK(hipFree(dcsr_val_B)); HIP_CHECK(hipFree(dcsr_row_ptr_C)); HIP_CHECK(hipFree(dcsr_col_ind_C)); HIP_CHECK(hipFree(dcsr_val_C)); return 0; }


Note

The stages

[rocsparse_spgeam_stage_analysis](enumerations.html#rocsparse-types_8h_1a5ccf6f0e1c8b62b7a85fdf6dac13d221a46d29d5d2b8f9c8fc244676b0d5785f4)and[rocsparse_spgeam_stage_compute](enumerations.html#rocsparse-types_8h_1a5ccf6f0e1c8b62b7a85fdf6dac13d221ad116559840a8c98322f7776e0ddad822)cannot be mixed with the stages[rocsparse_spgeam_stage_symbolic_analysis](enumerations.html#rocsparse-types_8h_1a5ccf6f0e1c8b62b7a85fdf6dac13d221aa0cd71a8bfd9030ffd62a8a8b2cc6493),[rocsparse_spgeam_stage_symbolic_compute](enumerations.html#rocsparse-types_8h_1a5ccf6f0e1c8b62b7a85fdf6dac13d221adc466c3ed3432910266e40d352fe4ef1),[rocsparse_spgeam_stage_numeric_analysis](enumerations.html#rocsparse-types_8h_1a5ccf6f0e1c8b62b7a85fdf6dac13d221a3f59bb753d58f155b9d5822724924f84), and[rocsparse_spgeam_stage_numeric_compute](enumerations.html#rocsparse-types_8h_1a5ccf6f0e1c8b62b7a85fdf6dac13d221a0f45ba1e5caacfca0ea8fdde666f0bce).Note

The stage

[rocsparse_spgeam_stage_analysis](enumerations.html#rocsparse-types_8h_1a5ccf6f0e1c8b62b7a85fdf6dac13d221a46d29d5d2b8f9c8fc244676b0d5785f4)must precede the stage[rocsparse_spgeam_stage_compute](enumerations.html#rocsparse-types_8h_1a5ccf6f0e1c8b62b7a85fdf6dac13d221ad116559840a8c98322f7776e0ddad822).Note

The stage

[rocsparse_spgeam_stage_symbolic_analysis](enumerations.html#rocsparse-types_8h_1a5ccf6f0e1c8b62b7a85fdf6dac13d221aa0cd71a8bfd9030ffd62a8a8b2cc6493)must precede the stage[rocsparse_spgeam_stage_symbolic_compute](enumerations.html#rocsparse-types_8h_1a5ccf6f0e1c8b62b7a85fdf6dac13d221adc466c3ed3432910266e40d352fe4ef1).Note

The stage

[rocsparse_spgeam_stage_numeric_analysis](enumerations.html#rocsparse-types_8h_1a5ccf6f0e1c8b62b7a85fdf6dac13d221a3f59bb753d58f155b9d5822724924f84)must precede the stage[rocsparse_spgeam_stage_numeric_compute](enumerations.html#rocsparse-types_8h_1a5ccf6f0e1c8b62b7a85fdf6dac13d221a0f45ba1e5caacfca0ea8fdde666f0bce).Note

The symbolic stages are not required to perform the numeric stages.

Note

The stage

[rocsparse_spgeam_stage_numeric_analysis](enumerations.html#rocsparse-types_8h_1a5ccf6f0e1c8b62b7a85fdf6dac13d221a3f59bb753d58f155b9d5822724924f84)must be re-applied if the numeric values of the input matrices`mat_A`

and`mat_B`

have changed between subsquent calls of the stage[rocsparse_spgeam_stage_numeric_compute](enumerations.html#rocsparse-types_8h_1a5ccf6f0e1c8b62b7a85fdf6dac13d221a0f45ba1e5caacfca0ea8fdde666f0bce).Note

Currently only CSR format is supported.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**descr**–**[in]**SpGEAM descriptor**mat_A**–**[in]**sparse matrix \(A\) descriptor.**mat_B**–**[in]**sparse matrix \(B\) descriptor.**mat_C**–**[out]**sparse matrix \(C\) descriptor.**stage**–**[in]**SpGEAM stage for the SpGEAM computation.**buffer_size**–**[out]**number of bytes of the temporary storage buffer.`buffer_size`

is determined by calling[rocsparse_spgeam_buffer_size](#rocsparse__spgeam_8h_1aefc21d68d17849c7efef71b3347a0427).**temp_buffer**–**[in]**temporary storage buffer allocated by the user.**error**–**[out]**error descriptor created if the returned status is not[rocsparse_status_success](enumerations.html#rocsparse-types_8h_1a578f8c5c1b08f358bf4605b0031006a8a96462a9361cfceb6cf9354e10fdc671b). A null pointer can be passed if the user is not interested in obtaining an error descriptor.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`mat_A`

,`mat_B`

,`mat_C`

,`descr`

or`buffer_size`

pointer is invalid.



## rocsparse_sddmm_buffer_size()[#](#rocsparse-sddmm-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sddmm_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)opA,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)opB, const void *alpha,[rocsparse_const_dnmat_descr](types.html#_CPPv427rocsparse_const_dnmat_descr)mat_A,[rocsparse_const_dnmat_descr](types.html#_CPPv427rocsparse_const_dnmat_descr)mat_B, const void *beta,[rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)mat_C,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)compute_type,[rocsparse_sddmm_alg](enumerations.html#_CPPv419rocsparse_sddmm_alg)alg, size_t *buffer_size)[#](#_CPPv427rocsparse_sddmm_buffer_size16rocsparse_handle19rocsparse_operation19rocsparse_operationPKv27rocsparse_const_dnmat_descr27rocsparse_const_dnmat_descrPKv21rocsparse_spmat_descr18rocsparse_datatype19rocsparse_sddmm_algP6size_t) `rocsparse_sddmm_buffer_size`

returns the size of the required buffer to execute the SDDMM operation from a given configuration. This routine is used in conjunction with[rocsparse_sddmm_preprocess()](#rocsparse__sddmm_8h_1a6c37829dbed3ac1e19f20296809cbf91)and[rocsparse_sddmm()](#rocsparse__sddmm_8h_1a4f0ff822b49bc8d4e02da483231e2f84).Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**opA**–**[in]**dense matrix \(A\) operation type.**opB**–**[in]**dense matrix \(B\) operation type.**alpha**–**[in]**scalar \(\alpha\).**mat_A**–**[in]**dense matrix \(A\) descriptor.**mat_B**–**[in]**dense matrix \(B\) descriptor.**beta**–**[in]**scalar \(\beta\).**mat_C**–**[inout]**sparse matrix \(C\) descriptor.**compute_type**–**[in]**floating point precision for the SDDMM computation.**alg**–**[in]**specification of the algorithm to use.**buffer_size**–**[out]**number of bytes of the temporary storage buffer.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_value**– the value of`opA`

or`opB`

is incorrect.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`alpha`

and`beta`

are invalid,`mat_A`

,`mat_B`

,`mat_C`

or`buffer_size`

pointer is invalid.**rocsparse_status_not_implemented**–`opA`

==[rocsparse_operation_conjugate_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a6920c1aa5f80005eee4b66ea6f25330f)or`opB`

==[rocsparse_operation_conjugate_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a6920c1aa5f80005eee4b66ea6f25330f).



## rocsparse_sddmm_preprocess()[#](#rocsparse-sddmm-preprocess)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sddmm_preprocess([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)opA,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)opB, const void *alpha,[rocsparse_const_dnmat_descr](types.html#_CPPv427rocsparse_const_dnmat_descr)mat_A,[rocsparse_const_dnmat_descr](types.html#_CPPv427rocsparse_const_dnmat_descr)mat_B, const void *beta,[rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)mat_C,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)compute_type,[rocsparse_sddmm_alg](enumerations.html#_CPPv419rocsparse_sddmm_alg)alg, void *temp_buffer)[#](#_CPPv426rocsparse_sddmm_preprocess16rocsparse_handle19rocsparse_operation19rocsparse_operationPKv27rocsparse_const_dnmat_descr27rocsparse_const_dnmat_descrPKv21rocsparse_spmat_descr18rocsparse_datatype19rocsparse_sddmm_algPv) `rocsparse_sddmm_preprocess`

executes a part of the algorithm that can be calculated once in the context of multiple calls of the[rocsparse_sddmm](#rocsparse__sddmm_8h_1a4f0ff822b49bc8d4e02da483231e2f84)with the same sparsity pattern.Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**opA**–**[in]**dense matrix \(A\) operation type.**opB**–**[in]**dense matrix \(B\) operation type.**alpha**–**[in]**scalar \(\alpha\).**mat_A**–**[in]**dense matrix \(A\) descriptor.**mat_B**–**[in]**dense matrix \(B\) descriptor.**beta**–**[in]**scalar \(\beta\).**mat_C**–**[inout]**sparse matrix \(C\) descriptor.**compute_type**–**[in]**floating point precision for the SDDMM computation.**alg**–**[in]**specification of the algorithm to use.**temp_buffer**–**[in]**temporary storage buffer allocated by the user. The size must be greater or equal to the size obtained with[rocsparse_sddmm_buffer_size](#rocsparse__sddmm_8h_1a0451c2922d3ff5768528766f11c48203).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_value**– the value of`opA`

or`opB`

is incorrect.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`alpha`

and`beta`

are invalid,`mat_A`

,`mat_B`

,`mat_C`

or`temp_buffer`

pointer is invalid.**rocsparse_status_not_implemented**–`opA`

==[rocsparse_operation_conjugate_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a6920c1aa5f80005eee4b66ea6f25330f)or`opB`

==[rocsparse_operation_conjugate_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a6920c1aa5f80005eee4b66ea6f25330f).



## rocsparse_sddmm()[#](#rocsparse-sddmm)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sddmm([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)opA,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)opB, const void *alpha,[rocsparse_const_dnmat_descr](types.html#_CPPv427rocsparse_const_dnmat_descr)mat_A,[rocsparse_const_dnmat_descr](types.html#_CPPv427rocsparse_const_dnmat_descr)mat_B, const void *beta,[rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)mat_C,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)compute_type,[rocsparse_sddmm_alg](enumerations.html#_CPPv419rocsparse_sddmm_alg)alg, void *temp_buffer)[#](#_CPPv415rocsparse_sddmm16rocsparse_handle19rocsparse_operation19rocsparse_operationPKv27rocsparse_const_dnmat_descr27rocsparse_const_dnmat_descrPKv21rocsparse_spmat_descr18rocsparse_datatype19rocsparse_sddmm_algPv) Sampled Dense-Dense Matrix Multiplication.

`rocsparse_sddmm`

multiplies the scalar \(\alpha\) with the dense \(m \times k\) matrix \(op(A)\), the dense \(k \times n\) matrix \(op(B)\), filtered by the sparsity pattern of the \(m \times n\) sparse matrix \(C\) and adds the result to \(C\) scaled by \(\beta\). The final result is stored in the sparse \(m \times n\) matrix \(C\), such that\[ C := \alpha ( op(A) \cdot op(B) ) \circ spy(C) + \beta C, \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if op(A) == rocsparse_operation_none} \\ A^T, & \text{if op(A) == rocsparse_operation_transpose} \\ \end{array} \right. \end{split}\],\[\begin{split} op(B) = \left\{ \begin{array}{ll} B, & \text{if op(B) == rocsparse_operation_none} \\ B^T, & \text{if op(B) == rocsparse_operation_transpose} \\ \end{array} \right. \end{split}\]and\[\begin{split} spy(C)_{ij} = \left\{ \begin{array}{ll} 1, & \text{ if C_{ij} != 0} \\ 0, & \text{ otherwise} \\ \end{array} \right. \end{split}\]Computing the above sampled dense-dense multiplication requires three steps to complete. First, the user calls

[rocsparse_sddmm_buffer_size](#rocsparse__sddmm_8h_1a0451c2922d3ff5768528766f11c48203)to determine the size of the required temporary storage buffer. Next, the user allocates this buffer and calls[rocsparse_sddmm_preprocess](#rocsparse__sddmm_8h_1a6c37829dbed3ac1e19f20296809cbf91)which performs any analysis of the input matrices that may be required. Finally, the user calls`rocsparse_sddmm`

to complete the computation. Once all calls to`rocsparse_sddmm`

are complete, the temporary buffer can be deallocated.`rocsparse_sddmm`

supports different algorithms which can provide better performance for different matrices.CSR/CSC Algorithms

Deterministic

Preprocessing

Notes

rocsparse_sddmm_alg_default

Yes

No

Uses the sparsity pattern of matrix C to perform a limited set of dot products

rocsparse_sddmm_alg_dense

Yes

No

Explicitly converts the matrix C into a dense matrix to perform a dense matrix multiply and add

Currently,

`rocsparse_sddmm`

only supports the uniform precisions indicated in the table below. For the sparse matrix \(C\),`rocsparse_sddmm`

supports the index types[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)and[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4).**Uniform Precisions:**A / B / C / compute_type

rocsparse_datatype_f16_r

rocsparse_datatype_f32_r

rocsparse_datatype_f64_r

rocsparse_datatype_f32_c

rocsparse_datatype_f64_c

**Mixed precisions:**A / B

C

compute_type

rocsparse_datatype_f16_r

rocsparse_datatype_f32_r

rocsparse_datatype_f32_r

rocsparse_datatype_f16_r

rocsparse_datatype_f16_r

rocsparse_datatype_f32_r

rocsparse_datatype_bf16_r

rocsparse_datatype_f32_r

rocsparse_datatype_f32_r

rocsparse_datatype_bf16_r

rocsparse_datatype_bf16_r

rocsparse_datatype_f32_r

**Example**This example performs sampled dense-dense matrix product, \(C := \alpha ( A \cdot B ) \circ spy(C) + \beta C\) where \(\circ\) is the hadamard product

int main() { // rocSPARSE handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); float halpha = 1.0f; float hbeta = -1.0f; // A, B, and C are mxk, kxn, and mxn int m = 4; int k = 3; int n = 2; int nnzC = 5; // 2 3 -1 // A = 0 2 1 // 0 0 5 // 0 -2 0.5 // 0 4 // B = 1 0 // -2 0.5 // 1 0 1 0 // C = 2 3 spy(C) = 1 1 // 0 0 0 0 // 4 5 1 1 std::vector<float> hA = {2.0f, 3.0f, -1.0f, 0.0, 2.0f, 1.0f, 0.0f, 0.0f, 5.0f, 0.0f, -2.0f, 0.5f}; std::vector<float> hB = {0.0f, 4.0f, 1.0f, 0.0, -2.0f, 0.5f}; std::vector<int> hcsr_row_ptrC = {0, 1, 3, 3, 5}; std::vector<int> hcsr_col_indC = {0, 0, 1, 0, 1}; std::vector<float> hcsr_valC = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f}; float* dA; float* dB; HIP_CHECK(hipMalloc(&dA, sizeof(float) * m * k)); HIP_CHECK(hipMalloc(&dB, sizeof(float) * k * n)); int* dcsr_row_ptrC; int* dcsr_col_indC; float* dcsr_valC; HIP_CHECK(hipMalloc(&dcsr_row_ptrC, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc(&dcsr_col_indC, sizeof(int) * nnzC)); HIP_CHECK(hipMalloc(&dcsr_valC, sizeof(float) * nnzC)); HIP_CHECK(hipMemcpy(dA, hA.data(), sizeof(float) * m * k, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dB, hB.data(), sizeof(float) * k * n, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( dcsr_row_ptrC, hcsr_row_ptrC.data(), sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsr_col_indC, hcsr_col_indC.data(), sizeof(int) * nnzC, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsr_valC, hcsr_valC.data(), sizeof(float) * nnzC, hipMemcpyHostToDevice)); rocsparse_dnmat_descr matA; ROCSPARSE_CHECK(rocsparse_create_dnmat_descr( &matA, m, k, k, dA, rocsparse_datatype_f32_r, rocsparse_order_row)); rocsparse_dnmat_descr matB; ROCSPARSE_CHECK(rocsparse_create_dnmat_descr( &matB, k, n, n, dB, rocsparse_datatype_f32_r, rocsparse_order_row)); rocsparse_spmat_descr matC; ROCSPARSE_CHECK(rocsparse_create_csr_descr(&matC, m, n, nnzC, dcsr_row_ptrC, dcsr_col_indC, dcsr_valC, rocsparse_indextype_i32, rocsparse_indextype_i32, rocsparse_index_base_zero, rocsparse_datatype_f32_r)); size_t buffer_size = 0; ROCSPARSE_CHECK(rocsparse_sddmm_buffer_size(handle, rocsparse_operation_none, rocsparse_operation_none, &halpha, matA, matB, &hbeta, matC, rocsparse_datatype_f32_r, rocsparse_sddmm_alg_default, &buffer_size)); void* dbuffer; HIP_CHECK(hipMalloc(&dbuffer, buffer_size)); ROCSPARSE_CHECK(rocsparse_sddmm_preprocess(handle, rocsparse_operation_none, rocsparse_operation_none, &halpha, matA, matB, &hbeta, matC, rocsparse_datatype_f32_r, rocsparse_sddmm_alg_default, dbuffer)); ROCSPARSE_CHECK(rocsparse_sddmm(handle, rocsparse_operation_none, rocsparse_operation_none, &halpha, matA, matB, &hbeta, matC, rocsparse_datatype_f32_r, rocsparse_sddmm_alg_default, dbuffer)); HIP_CHECK(hipMemcpy( hcsr_row_ptrC.data(), dcsr_row_ptrC, sizeof(int) * (m + 1), hipMemcpyDeviceToHost)); HIP_CHECK( hipMemcpy(hcsr_col_indC.data(), dcsr_col_indC, sizeof(int) * nnzC, hipMemcpyDeviceToHost)); HIP_CHECK(hipMemcpy(hcsr_valC.data(), dcsr_valC, sizeof(float) * nnzC, hipMemcpyDeviceToHost)); std::cout << "hcsr_row_ptrC" << std::endl; for(size_t i = 0; i < hcsr_row_ptrC.size(); i++) { std::cout << hcsr_row_ptrC[i] << " "; } std::cout << "" << std::endl; std::cout << "hcsr_col_indC" << std::endl; for(size_t i = 0; i < hcsr_col_indC.size(); i++) { std::cout << hcsr_col_indC[i] << " "; } std::cout << "" << std::endl; std::cout << "hcsr_valC" << std::endl; for(size_t i = 0; i < hcsr_valC.size(); i++) { std::cout << hcsr_valC[i] << " "; } std::cout << "" << std::endl; ROCSPARSE_CHECK(rocsparse_destroy_dnmat_descr(matA)); ROCSPARSE_CHECK(rocsparse_destroy_dnmat_descr(matB)); ROCSPARSE_CHECK(rocsparse_destroy_spmat_descr(matC)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); HIP_CHECK(hipFree(dA)); HIP_CHECK(hipFree(dB)); HIP_CHECK(hipFree(dcsr_row_ptrC)); HIP_CHECK(hipFree(dcsr_col_indC)); HIP_CHECK(hipFree(dcsr_valC)); HIP_CHECK(hipFree(dbuffer)); return 0; }


Note

This routine supports execution in a hipGraph context only when

`alg`

==[rocsparse_sddmm_alg_default](enumerations.html#rocsparse-types_8h_1ac8fbc731ff97c543c29c8c9a08f8ba63adfdbb214c06ab417cf4d33e075d850a8).- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**opA**–**[in]**dense matrix \(A\) operation type.**opB**–**[in]**dense matrix \(B\) operation type.**alpha**–**[in]**scalar \(\alpha\).**mat_A**–**[in]**dense matrix \(A\) descriptor.**mat_B**–**[in]**dense matrix \(B\) descriptor.**beta**–**[in]**scalar \(\beta\).**mat_C**–**[inout]**sparse matrix \(C\) descriptor.**compute_type**–**[in]**floating point precision for the SDDMM computation.**alg**–**[in]**specification of the algorithm to use.**temp_buffer**–**[in]**temporary storage buffer allocated by the user. The size must be greater or equal to the size obtained with[rocsparse_sddmm_buffer_size](#rocsparse__sddmm_8h_1a0451c2922d3ff5768528766f11c48203).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_value**– the value of`opA`

,`opB`

,`compute_type`

or alg is incorrect.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`alpha`

and`beta`

are invalid,`mat_A`

,`mat_B`

,`mat_C`

or`temp_buffer`

pointer is invalid.**rocsparse_status_not_implemented**–`opA`

==[rocsparse_operation_conjugate_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a6920c1aa5f80005eee4b66ea6f25330f)or`opB`

==[rocsparse_operation_conjugate_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a6920c1aa5f80005eee4b66ea6f25330f).



## rocsparse_dense_to_sparse()[#](#rocsparse-dense-to-sparse)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dense_to_sparse([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_const_dnmat_descr](types.html#_CPPv427rocsparse_const_dnmat_descr)mat_A,[rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)mat_B,[rocsparse_dense_to_sparse_alg](enumerations.html#_CPPv429rocsparse_dense_to_sparse_alg)alg, size_t *buffer_size, void *temp_buffer)[#](#_CPPv425rocsparse_dense_to_sparse16rocsparse_handle27rocsparse_const_dnmat_descr21rocsparse_spmat_descr29rocsparse_dense_to_sparse_algP6size_tPv) Dense matrix to sparse matrix conversion.

`rocsparse_dense_to_sparse`

performs the conversion of a dense matrix to a sparse matrix in CSR, CSC, or COO format.`rocsparse_dense_to_sparse`

requires multiple steps to complete. First, the user calls`rocsparse_dense_to_sparse`

with`nullptr`

passed into`temp_buffer:`

After this is called, the// Call dense_to_sparse to get required buffer size size_t buffer_size = 0; rocsparse_dense_to_sparse(handle, matA, matB, rocsparse_dense_to_sparse_alg_default, &buffer_size, nullptr);

`buffer_size`

will be filled with the size of the required buffer that must be then allocated by the user. Next the user calls`rocsparse_dense_to_sparse`

with the newly allocated`temp_buffer`

and`nullptr`

passed into`buffer_size:`

This will determine the number of non-zeros that will exist in the sparse matrix which can be queried using// Call dense_to_sparse to perform analysis rocsparse_dense_to_sparse(handle, matA, matB, rocsparse_dense_to_sparse_alg_default, nullptr, temp_buffer);

[rocsparse_spmat_get_size](auxiliary.html#rocsparse-auxiliary_8h_1ae0af1141c78f6e52b64dc15bbe6af0b1)routine. With this, the user can allocate the sparse matrix device arrays and set them on the sparse matrix descriptor using[rocsparse_csr_set_pointers](auxiliary.html#rocsparse-auxiliary_8h_1a7dd00d556b589d53e7fa97712e309eed)(CSR format),[rocsparse_csc_set_pointers](auxiliary.html#rocsparse-auxiliary_8h_1a0de3ca95b78d3adf237a8ff1815700dc)(for CSC format), or[rocsparse_coo_set_pointers](auxiliary.html#rocsparse-auxiliary_8h_1ab6d28bc9de332fdf26e77c2e4e826cdd)(for COO format). Finally, the conversion is completed by calling`rocsparse_dense_to_sparse`

with both the`buffer_size`

and`temp_buffer:`

Currently,// Call dense_to_sparse to complete conversion rocsparse_dense_to_sparse(handle, matA, matB, rocsparse_dense_to_sparse_alg_default, &buffer_size, temp_buffer);

`rocsparse_dense_to_sparse`

only supports the algorithm[rocsparse_dense_to_sparse_alg_default](enumerations.html#rocsparse-types_8h_1aa5befb67d77c1c17652d3cf5d23a1127a3e0cf2bc95d6ea00c6fd9db0acae2671). See full example below.`rocsparse_dense_to_sparse`

supports[rocsparse_datatype_f16_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edad1cfc57acb782705135ed34bb44038fc),[rocsparse_datatype_f32_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edaa62d4737b4cdb93a7f60715db0d01520),[rocsparse_datatype_f64_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda2ca573746a15c391064033943edcebdb),[rocsparse_datatype_f32_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda680bfd1bcdda1c2e2c23a885fef0d86e), and[rocsparse_datatype_f64_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edadd4150f1dee0d44da9568294d6b11aa2)for values arrays in the sparse matrix (stored in CSR, CSC, or COO format) and the dense matrix. For the row/column offset and row/column index arrays of the sparse matrix,`rocsparse_dense_to_sparse`

supports the precisions[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)and[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4).**Uniform Precisions:**A / B

rocsparse_datatype_f16_r

rocsparse_datatype_bf16_r

rocsparse_datatype_f32_r

rocsparse_datatype_f64_r

rocsparse_datatype_f32_c

rocsparse_datatype_f64_c

**Example**int main() { // 1 4 0 0 0 0 // A = 0 2 3 0 0 0 // 5 0 0 7 8 0 // 0 0 9 0 6 0 int m = 4; int n = 6; std::vector<float> hdense = {1, 0, 5, 0, 4, 2, 0, 0, 0, 3, 0, 9, 0, 0, 7, 0, 0, 0, 8, 6, 0, 0, 0, 0}; // Offload data to device int* dcsr_row_ptr; float* ddense; HIP_CHECK(hipMalloc(&dcsr_row_ptr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc(&ddense, sizeof(float) * m * n)); HIP_CHECK(hipMemcpy(ddense, hdense.data(), sizeof(float) * m * n, hipMemcpyHostToDevice)); rocsparse_handle handle; rocsparse_dnmat_descr matA; rocsparse_spmat_descr matB; rocsparse_indextype row_idx_type = rocsparse_indextype_i32; rocsparse_indextype col_idx_type = rocsparse_indextype_i32; rocsparse_datatype data_type = rocsparse_datatype_f32_r; rocsparse_index_base idx_base = rocsparse_index_base_zero; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Create sparse matrix A ROCSPARSE_CHECK( rocsparse_create_dnmat_descr(&matA, m, n, m, ddense, data_type, rocsparse_order_column)); // Create dense matrix B ROCSPARSE_CHECK(rocsparse_create_csr_descr(&matB, m, n, 0, dcsr_row_ptr, nullptr, nullptr, row_idx_type, col_idx_type, idx_base, data_type)); // Call dense_to_sparse to get required buffer size size_t buffer_size = 0; ROCSPARSE_CHECK(rocsparse_dense_to_sparse( handle, matA, matB, rocsparse_dense_to_sparse_alg_default, &buffer_size, nullptr)); void* temp_buffer; HIP_CHECK(hipMalloc(&temp_buffer, buffer_size)); // Call dense_to_sparse to perform analysis ROCSPARSE_CHECK(rocsparse_dense_to_sparse( handle, matA, matB, rocsparse_dense_to_sparse_alg_default, nullptr, temp_buffer)); int64_t num_rows_tmp, num_cols_tmp, nnz; ROCSPARSE_CHECK(rocsparse_spmat_get_size(matB, &num_rows_tmp, &num_cols_tmp, &nnz)); int* dcsr_col_ind; float* dcsr_val; HIP_CHECK(hipMalloc(&dcsr_col_ind, sizeof(int) * nnz)); HIP_CHECK(hipMalloc(&dcsr_val, sizeof(float) * nnz)); ROCSPARSE_CHECK(rocsparse_csr_set_pointers(matB, dcsr_row_ptr, dcsr_col_ind, dcsr_val)); // Call dense_to_sparse to complete conversion ROCSPARSE_CHECK(rocsparse_dense_to_sparse( handle, matA, matB, rocsparse_dense_to_sparse_alg_default, &buffer_size, temp_buffer)); std::vector<int> hcsr_row_ptr(m + 1, 0); std::vector<int> hcsr_col_ind(nnz, 0); std::vector<float> hcsr_val(nnz, 0); // Copy result back to host HIP_CHECK( hipMemcpy(hcsr_row_ptr.data(), dcsr_row_ptr, sizeof(int) * (m + 1), hipMemcpyDeviceToHost)); HIP_CHECK( hipMemcpy(hcsr_col_ind.data(), dcsr_col_ind, sizeof(int) * nnz, hipMemcpyDeviceToHost)); HIP_CHECK(hipMemcpy(hcsr_val.data(), dcsr_val, sizeof(float) * nnz, hipMemcpyDeviceToHost)); std::cout << "hcsr_row_ptr" << std::endl; for(size_t i = 0; i < hcsr_row_ptr.size(); i++) { std::cout << hcsr_row_ptr[i] << " "; } std::cout << "" << std::endl; std::cout << "hcsr_col_ind" << std::endl; for(size_t i = 0; i < hcsr_col_ind.size(); i++) { std::cout << hcsr_col_ind[i] << " "; } std::cout << "" << std::endl; std::cout << "hcsr_val" << std::endl; for(size_t i = 0; i < hcsr_val.size(); i++) { std::cout << hcsr_val[i] << " "; } std::cout << "" << std::endl; // Clear rocSPARSE ROCSPARSE_CHECK(rocsparse_destroy_dnmat_descr(matA)); ROCSPARSE_CHECK(rocsparse_destroy_spmat_descr(matB)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); // Clear device memory HIP_CHECK(hipFree(dcsr_row_ptr)); HIP_CHECK(hipFree(dcsr_col_ind)); HIP_CHECK(hipFree(dcsr_val)); HIP_CHECK(hipFree(ddense)); return 0; }


Note

This function writes the required allocation size (in bytes) to

`buffer_size`

and returns without performing the dense to sparse operation, when a nullptr is passed for`temp_buffer`

.Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**mat_A**–**[in]**dense matrix descriptor.**mat_B**–**[in]**sparse matrix descriptor.**alg**–**[in]**algorithm for the dense to sparse computation.**buffer_size**–**[out]**number of bytes of the temporary storage buffer. buffer_size is set when`temp_buffer`

is nullptr.**temp_buffer**–**[in]**temporary storage buffer allocated by the user. When a nullptr is passed, the required allocation size (in bytes) is written to`buffer_size`

and function returns without performing the dense to sparse operation.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`mat_A`

,`mat_B`

, or`buffer_size`

pointer is invalid.



## rocsparse_sparse_to_dense()[#](#rocsparse-sparse-to-dense)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sparse_to_dense([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_const_spmat_descr](types.html#_CPPv427rocsparse_const_spmat_descr)mat_A,[rocsparse_dnmat_descr](types.html#_CPPv421rocsparse_dnmat_descr)mat_B,[rocsparse_sparse_to_dense_alg](enumerations.html#_CPPv429rocsparse_sparse_to_dense_alg)alg, size_t *buffer_size, void *temp_buffer)[#](#_CPPv425rocsparse_sparse_to_dense16rocsparse_handle27rocsparse_const_spmat_descr21rocsparse_dnmat_descr29rocsparse_sparse_to_dense_algP6size_tPv) Sparse matrix to dense matrix conversion.

`rocsparse_sparse_to_dense`

performs the conversion of a sparse matrix in CSR, CSC, or COO format to a dense matrix`rocsparse_sparse_to_dense`

requires multiple steps to complete. First, the user calls`rocsparse_sparse_to_dense`

with`nullptr`

passed into`temp_buffer:`

After this is called, the// Call sparse_to_dense to get required buffer size size_t buffer_size = 0; rocsparse_sparse_to_dense(handle, matA, matB, rocsparse_sparse_to_dense_alg_default, &buffer_size, nullptr);

`buffer_size`

will be filled with the size of the required buffer that must be then allocated by the user. Finally, the conversion is completed by calling`rocsparse_sparse_to_dense`

with both the`buffer_size`

and`temp_buffer:`

Currently,// Call dense_to_sparse to complete conversion rocsparse_sparse_to_dense(handle, matA, matB, rocsparse_sparse_to_dense_alg_default, &buffer_size, temp_buffer);

`rocsparse_sparse_to_dense`

only supports the algorithm[rocsparse_sparse_to_dense_alg_default](enumerations.html#rocsparse-types_8h_1a20425e827ea9be6bde28db1538e007eaa973f10a09487bca289e1a9e6791360bc). See full example below.`rocsparse_sparse_to_dense`

supports[rocsparse_datatype_f16_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edad1cfc57acb782705135ed34bb44038fc),[rocsparse_datatype_f32_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edaa62d4737b4cdb93a7f60715db0d01520),[rocsparse_datatype_f64_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda2ca573746a15c391064033943edcebdb),[rocsparse_datatype_f32_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda680bfd1bcdda1c2e2c23a885fef0d86e), and[rocsparse_datatype_f64_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edadd4150f1dee0d44da9568294d6b11aa2)for values arrays in the sparse matrix (stored in CSR, CSC, or COO format) and the dense matrix. For the row/column offset and row/column index arrays of the sparse matrix,`rocsparse_sparse_to_dense`

supports the precisions[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)and[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4).**Uniform Precisions:**A / B

rocsparse_datatype_f16_r

rocsparse_datatype_bf16_r

rocsparse_datatype_f32_r

rocsparse_datatype_f64_r

rocsparse_datatype_f32_c

rocsparse_datatype_f64_c

**Example**int main() { // 1 4 0 0 0 0 // A = 0 2 3 0 0 0 // 5 0 0 7 8 0 // 0 0 9 0 6 0 int m = 4; int n = 6; std::vector<int> hcsr_row_ptr = {0, 2, 4, 7, 9}; std::vector<int> hcsr_col_ind = {0, 1, 1, 2, 0, 3, 4, 2, 4}; std::vector<float> hcsr_val = {1, 4, 2, 3, 5, 7, 8, 9, 6}; std::vector<float> hdense(m * n, 0.0f); int nnz = hcsr_row_ptr[m] - hcsr_row_ptr[0]; // Offload data to device int* dcsr_row_ptr; int* dcsr_col_ind; float* dcsr_val; float* ddense; HIP_CHECK(hipMalloc(&dcsr_row_ptr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc(&dcsr_col_ind, sizeof(int) * nnz)); HIP_CHECK(hipMalloc(&dcsr_val, sizeof(float) * nnz)); HIP_CHECK(hipMalloc(&ddense, sizeof(float) * m * n)); HIP_CHECK( hipMemcpy(dcsr_row_ptr, hcsr_row_ptr.data(), sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsr_col_ind, hcsr_col_ind.data(), sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsr_val, hcsr_val.data(), sizeof(float) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(ddense, hdense.data(), sizeof(float) * m * n, hipMemcpyHostToDevice)); rocsparse_handle handle; rocsparse_spmat_descr matA; rocsparse_dnmat_descr matB; rocsparse_indextype row_idx_type = rocsparse_indextype_i32; rocsparse_indextype col_idx_type = rocsparse_indextype_i32; rocsparse_datatype data_type = rocsparse_datatype_f32_r; rocsparse_index_base idx_base = rocsparse_index_base_zero; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Create sparse matrix A ROCSPARSE_CHECK(rocsparse_create_csr_descr(&matA, m, n, nnz, dcsr_row_ptr, dcsr_col_ind, dcsr_val, row_idx_type, col_idx_type, idx_base, data_type)); // Create dense matrix B ROCSPARSE_CHECK( rocsparse_create_dnmat_descr(&matB, m, n, m, ddense, data_type, rocsparse_order_column)); // Call sparse_to_dense size_t buffer_size = 0; ROCSPARSE_CHECK(rocsparse_sparse_to_dense( handle, matA, matB, rocsparse_sparse_to_dense_alg_default, &buffer_size, nullptr)); void* temp_buffer; HIP_CHECK(hipMalloc(&temp_buffer, buffer_size)); ROCSPARSE_CHECK(rocsparse_sparse_to_dense( handle, matA, matB, rocsparse_sparse_to_dense_alg_default, &buffer_size, temp_buffer)); // Copy result back to host HIP_CHECK(hipMemcpy(hdense.data(), ddense, sizeof(float) * m * n, hipMemcpyDeviceToHost)); // Clear rocSPARSE ROCSPARSE_CHECK(rocsparse_destroy_spmat_descr(matA)); ROCSPARSE_CHECK(rocsparse_destroy_dnmat_descr(matB)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); // Clear device memory HIP_CHECK(hipFree(dcsr_row_ptr)); HIP_CHECK(hipFree(dcsr_col_ind)); HIP_CHECK(hipFree(dcsr_val)); HIP_CHECK(hipFree(ddense)); return 0; }


Note

This function writes the required allocation size (in bytes) to

`buffer_size`

and returns without performing the sparse to dense operation, when a nullptr is passed for`temp_buffer`

.Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**mat_A**–**[in]**sparse matrix descriptor.**mat_B**–**[in]**dense matrix descriptor.**alg**–**[in]**algorithm for the sparse to dense computation.**buffer_size**–**[out]**number of bytes of the temporary storage buffer. buffer_size is set when`temp_buffer`

is nullptr.**temp_buffer**–**[in]**temporary storage buffer allocated by the user. When a nullptr is passed, the required allocation size (in bytes) is written to`buffer_size`

and function returns without performing the sparse to dense operation.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`mat_A`

,`mat_B`

, or`buffer_size`

pointer is invalid.



## rocsparse_sparse_to_sparse_buffer_size()[#](#rocsparse-sparse-to-sparse-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sparse_to_sparse_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_sparse_to_sparse_descr](types.html#_CPPv432rocsparse_sparse_to_sparse_descr)descr,[rocsparse_const_spmat_descr](types.html#_CPPv427rocsparse_const_spmat_descr)source,[rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)target,[rocsparse_sparse_to_sparse_stage](enumerations.html#_CPPv432rocsparse_sparse_to_sparse_stage)stage, size_t *buffer_size_in_bytes)[#](#_CPPv438rocsparse_sparse_to_sparse_buffer_size16rocsparse_handle32rocsparse_sparse_to_sparse_descr27rocsparse_const_spmat_descr21rocsparse_spmat_descr32rocsparse_sparse_to_sparse_stageP6size_t) `rocsparse_sparse_to_sparse_buffer_size`

calculates the required buffer size in bytes for a given stage`stage`

.- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**descr**–**[in]**descriptor of the sparse_to_sparse algorithm.**source**–**[in]**source sparse matrix descriptor.**target**–**[in]**target sparse matrix descriptor.**stage**–**[in]**stage of the sparse_to_sparse computation.**buffer_size_in_bytes**–**[out]**size in bytes of the`buffer`


- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_value**– if any required enumeration is invalid.**rocsparse_status_invalid_pointer**–`mat_A`

,`mat_B`

, or`buffer_size_in_bytes`

pointer is invalid.



## rocsparse_sparse_to_sparse()[#](#rocsparse-sparse-to-sparse)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sparse_to_sparse([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_sparse_to_sparse_descr](types.html#_CPPv432rocsparse_sparse_to_sparse_descr)descr,[rocsparse_const_spmat_descr](types.html#_CPPv427rocsparse_const_spmat_descr)source,[rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)target,[rocsparse_sparse_to_sparse_stage](enumerations.html#_CPPv432rocsparse_sparse_to_sparse_stage)stage, size_t buffer_size_in_bytes, void *buffer)[#](#_CPPv426rocsparse_sparse_to_sparse16rocsparse_handle32rocsparse_sparse_to_sparse_descr27rocsparse_const_spmat_descr21rocsparse_spmat_descr32rocsparse_sparse_to_sparse_stage6size_tPv) Sparse matrix to sparse matrix conversion.

`rocsparse_sparse_to_sparse`

performs the conversion of a sparse matrix to a sparse matrix.**Example**This example converts a CSR matrix into an ELL matrix.

int main() { // 4 2 0 1 0 // 2 4 2 0 1 // 0 2 4 2 0 // 1 0 2 4 2 // 0 1 0 2 4 int m = 5; int n = 5; int nnz = 17; std::vector<int> hcsr_row_ptr = {0, 3, 7, 10, 14, 17}; std::vector<int> hcsr_col_ind = {0, 1, 3, 0, 1, 2, 4, 1, 2, 3, 0, 2, 3, 4, 1, 3, 4}; std::vector<double> hcsr_val = {4.0, 2.0, 1.0, 2.0, 4.0, 2.0, 1.0, 2.0, 4.0, 2.0, 1.0, 2.0, 4.0, 2.0, 1.0, 2.0, 4.0}; // rocSPARSE handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); int* dcsr_row_ptr = nullptr; int* dcsr_col_ind = nullptr; double* dcsr_val = nullptr; HIP_CHECK(hipMalloc((void**)&dcsr_row_ptr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&dcsr_col_ind, sizeof(int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcsr_val, sizeof(double) * nnz)); HIP_CHECK( hipMemcpy(dcsr_row_ptr, hcsr_row_ptr.data(), sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsr_col_ind, hcsr_col_ind.data(), sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsr_val, hcsr_val.data(), sizeof(double) * nnz, hipMemcpyHostToDevice)); // It assumes the CSR arrays (ptr, ind, val) have already been allocated and filled. // Build Source rocsparse_spmat_descr source; ROCSPARSE_CHECK(rocsparse_create_csr_descr(&source, m, n, nnz, dcsr_row_ptr, dcsr_col_ind, dcsr_val, rocsparse_indextype_i32, rocsparse_indextype_i32, rocsparse_index_base_zero, rocsparse_datatype_f64_r)); // Build target void * dell_ind, *dell_val; int64_t ell_width = 0; rocsparse_spmat_descr target; ROCSPARSE_CHECK(rocsparse_create_ell_descr(&target, m, n, dell_ind, dell_val, ell_width, rocsparse_indextype_i32, rocsparse_index_base_zero, rocsparse_datatype_f64_r)); // Create descriptor rocsparse_sparse_to_sparse_descr descr; ROCSPARSE_CHECK(rocsparse_create_sparse_to_sparse_descr( &descr, source, target, rocsparse_sparse_to_sparse_alg_default)); // Analysis phase size_t buffer_size; ROCSPARSE_CHECK(rocsparse_sparse_to_sparse_buffer_size( handle, descr, source, target, rocsparse_sparse_to_sparse_stage_analysis, &buffer_size)); void* buffer = nullptr; HIP_CHECK(hipMalloc(&buffer, buffer_size)); ROCSPARSE_CHECK(rocsparse_sparse_to_sparse(handle, descr, source, target, rocsparse_sparse_to_sparse_stage_analysis, buffer_size, buffer)); HIP_CHECK(hipFree(buffer)); // the user is responsible to allocate target arrays after the analysis phase. int64_t rows, cols; void * ind, *val; rocsparse_indextype idx_type; rocsparse_index_base idx_base; rocsparse_datatype data_type; // Get ell_width ROCSPARSE_CHECK(rocsparse_ell_get( target, &rows, &cols, &ind, &val, &ell_width, &idx_type, &idx_base, &data_type)); std::cout << "rows: " << rows << " cols: " << cols << " ell_width: " << ell_width << std::endl; // Allocate device arrays for ELL format HIP_CHECK(hipMalloc(&dell_ind, sizeof(int) * ell_width * m)); HIP_CHECK(hipMalloc(&dell_val, sizeof(double) * ell_width * m)); ROCSPARSE_CHECK(rocsparse_ell_set_pointers(target, dell_ind, dell_val)); // Calculation phase ROCSPARSE_CHECK(rocsparse_sparse_to_sparse_buffer_size( handle, descr, source, target, rocsparse_sparse_to_sparse_stage_compute, &buffer_size)); HIP_CHECK(hipMalloc(&buffer, buffer_size)); ROCSPARSE_CHECK(rocsparse_sparse_to_sparse(handle, descr, source, target, rocsparse_sparse_to_sparse_stage_compute, buffer_size, buffer)); HIP_CHECK(hipFree(buffer)); std::vector<int> hell_ind(ell_width * m); std::vector<double> hell_val(ell_width * m); HIP_CHECK( hipMemcpy(hell_ind.data(), dell_ind, sizeof(int) * ell_width * m, hipMemcpyDeviceToHost)); HIP_CHECK(hipMemcpy( hell_val.data(), dell_val, sizeof(double) * ell_width * m, hipMemcpyDeviceToHost)); std::cout << "hell_ind" << std::endl; for(size_t i = 0; i < hell_ind.size(); i++) { std::cout << hell_ind[i] << " "; } std::cout << "" << std::endl; std::cout << "hell_val" << std::endl; for(size_t i = 0; i < hell_val.size(); i++) { std::cout << hell_val[i] << " "; } std::cout << "" << std::endl; HIP_CHECK(hipFree(dcsr_row_ptr)); HIP_CHECK(hipFree(dcsr_col_ind)); HIP_CHECK(hipFree(dcsr_val)); HIP_CHECK(hipFree(dell_ind)); HIP_CHECK(hipFree(dell_val)); return 0; }


Note

The required allocation size (in bytes) to

`buffer_size_in_bytes`

must be obtained from[rocsparse_sparse_to_sparse_buffer_size](#rocsparse__sparse__to__sparse_8h_1a1b77eccccc0f7ba44e20e240ead4fc0b)for each stage, indeed the required buffer size can be different between stages.- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**descr**–**[in]**descriptor of the sparse_to_sparse algorithm.**source**–**[in]**sparse matrix descriptor.**target**–**[in]**sparse matrix descriptor.**stage**–**[in]**stage of the sparse_to_sparse computation.**buffer_size_in_bytes**–**[in]**size in bytes of the`buffer`

**buffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**rocsparse_status_success**– the operation completed successfully.


## rocsparse_extract_buffer_size()[#](#rocsparse-extract-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_extract_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_extract_descr](types.html#_CPPv423rocsparse_extract_descr)descr,[rocsparse_const_spmat_descr](types.html#_CPPv427rocsparse_const_spmat_descr)source,[rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)target,[rocsparse_extract_stage](enumerations.html#_CPPv423rocsparse_extract_stage)stage, size_t *buffer_size_in_bytes)[#](#_CPPv429rocsparse_extract_buffer_size16rocsparse_handle23rocsparse_extract_descr27rocsparse_const_spmat_descr21rocsparse_spmat_descr23rocsparse_extract_stageP6size_t) `rocsparse_extract_buffer_size`

calculates the required buffer size in bytes for a given stage`stage`

. This routine is used in conjunction with[rocsparse_extract_nnz](#rocsparse__extract_8h_1ad890c96b5d903448b8d83c5397e168c8)and[rocsparse_extract](#rocsparse__extract_8h_1ad9110cab48a4ebbc6e04dc4e22b1f0f3)to extract a lower or upper triangular sparse matrix from an input sparse matrix. See[rocsparse_extract](#rocsparse__extract_8h_1ad9110cab48a4ebbc6e04dc4e22b1f0f3)for more details.Note

This routine is asynchronous with respect to the host. This routine does support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**descr**–**[in]**descriptor of the extract algorithm.**source**–**[in]**source sparse matrix descriptor.**target**–**[in]**target sparse matrix descriptor.**stage**–**[in]**stage of the extract computation.**buffer_size_in_bytes**–**[out]**size in bytes of the buffer.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_value**– if`stage`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`source`

,`target`

, or`buffer_size_in_bytes`

pointer is invalid.



## rocsparse_extract_nnz[#](#rocsparse-extract-nnz)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_extract_nnz([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_extract_descr](types.html#_CPPv423rocsparse_extract_descr)descr, int64_t *nnz)[#](#_CPPv421rocsparse_extract_nnz16rocsparse_handle23rocsparse_extract_descrP7int64_t) `rocsparse_extract_nnz`

returns the number of non-zeros in the extracted matrix. The value is available after the analysis phase[rocsparse_extract_stage_analysis](enumerations.html#rocsparse-types_8h_1a884a4bd3e6b822da9a23b56f89a2e594ae083d0e64809b25bca57ce146d3d080f)has been executed. This routine is used in conjunction with[rocsparse_extract_buffer_size](#rocsparse__extract_8h_1a44a25427da37a434b5d894638c003552)and[rocsparse_extract](#rocsparse__extract_8h_1ad9110cab48a4ebbc6e04dc4e22b1f0f3)to extract a lower or upper triangular sparse matrix from an input sparse matrix. See[rocsparse_extract](#rocsparse__extract_8h_1ad9110cab48a4ebbc6e04dc4e22b1f0f3)for more details.Note

This routine is asynchronous with respect to the host. This routine does support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**descr**–**[in]**descriptor of the extract algorithm.**nnz**–**[out]**the number of non-zeros.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`descr`

or`nnz`

pointer is invalid.



## rocsparse_extract()[#](#rocsparse-extract)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_extract([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_extract_descr](types.html#_CPPv423rocsparse_extract_descr)descr,[rocsparse_const_spmat_descr](types.html#_CPPv427rocsparse_const_spmat_descr)source,[rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)target,[rocsparse_extract_stage](enumerations.html#_CPPv423rocsparse_extract_stage)stage, size_t buffer_size_in_bytes, void *buffer)[#](#_CPPv417rocsparse_extract16rocsparse_handle23rocsparse_extract_descr27rocsparse_const_spmat_descr21rocsparse_spmat_descr23rocsparse_extract_stage6size_tPv) Sparse matrix extraction.

`rocsparse_extract`

performs the extraction of the lower or upper part of a sparse matrix into a new matrix.`rocsparse_extract`

requires multiple steps to complete. First, the user creates the source and target sparse matrix descriptors. For example, in the case of CSR matrix format this might look like:Next, the user creates the extraction descriptor and calls// Build Source rocsparse_spmat_descr source; rocsparse_create_csr_descr(&source, M, N, nnz, dsource_row_ptr, dsource_col_ind, dsource_val, rocsparse_indextype_i32, rocsparse_indextype_i32, rocsparse_index_base_zero, rocsparse_datatype_f32_r); // Build target void * dtarget_row_ptr; hipMalloc(&dtarget_row_ptr, sizeof(int32_t) * (M + 1)); rocsparse_spmat_descr target; rocsparse_create_csr_descr(&target, M, N, 0, dtarget_row_ptr, nullptr, nullptr, rocsparse_indextype_i32, rocsparse_indextype_i32, rocsparse_index_base_zero, rocsparse_datatype_f32_r);

[rocsparse_extract_buffer_size](#rocsparse__extract_8h_1a44a25427da37a434b5d894638c003552)with the stage[rocsparse_extract_stage_analysis](enumerations.html#rocsparse-types_8h_1a884a4bd3e6b822da9a23b56f89a2e594ae083d0e64809b25bca57ce146d3d080f)in order to determine the amount of temporary storage required. The user allocates this temporary storage buffer and passes it to`rocsparse_extract`

with the stage[rocsparse_extract_stage_analysis](enumerations.html#rocsparse-types_8h_1a884a4bd3e6b822da9a23b56f89a2e594ae083d0e64809b25bca57ce146d3d080f)The user then calls// Create descriptor rocsparse_extract_descr descr; rocsparse_create_extract_descr(&descr, source, target, rocsparse_extract_alg_default); // Analysis phase size_t buffer_size; rocsparse_extract_buffer_size(handle, descr, source, target, rocsparse_extract_stage_analysis, &buffer_size); void* dbuffer = nullptr; hipMalloc(&dbuffer, buffer_size); rocsparse_extract(handle, descr, source, target, rocsparse_extract_stage_analysis, buffer_size, dbuffer); hipFree(dbuffer);

[rocsparse_extract_nnz](#rocsparse__extract_8h_1ad890c96b5d903448b8d83c5397e168c8)in order to determine the number of non-zeros that will exist in the target matrix. Once determined, the user can allocate the column indices and values arrays of the target sparse matrix:Finally, the user callsint64_t target_nnz; rocsparse_extract_nnz(handle, descr, &target_nnz); void* dtarget_col_ind, void* dtarget_val; hipMalloc(&dtarget_col_ind, sizeof(int32_t) * target_nnz); hipMalloc(&dtarget_val, sizeof(float) * target_nnz); rocsparse_csr_set_pointers(target, dtarget_row_ptr, dtarget_col_ind, dtarget_val);

[rocsparse_extract_buffer_size](#rocsparse__extract_8h_1a44a25427da37a434b5d894638c003552)with the stage[rocsparse_extract_stage_compute](enumerations.html#rocsparse-types_8h_1a884a4bd3e6b822da9a23b56f89a2e594a80bf2aa6b71ba18c1ee7b1c591c05b3c)in order to determine the size of the temporary user allocated storage needed for the computation of the column indices and values in the sparse target. The user allocates this buffer and completes the conversion by calling`rocsparse_extract`

using the[rocsparse_extract_stage_compute](enumerations.html#rocsparse-types_8h_1a884a4bd3e6b822da9a23b56f89a2e594a80bf2aa6b71ba18c1ee7b1c591c05b3c)stage:The target row pointer, column indices, and values arrays will now be filled with the upper or lower part of the source matrix.// Calculation phase rocsparse_extract_buffer_size(handle, descr, source, target, rocsparse_extract_stage_compute, &buffer_size); hipMalloc(&dbuffer, buffer_size); rocsparse_extract(handle, descr, source, target, rocsparse_extract_stage_compute, buffer_size, dbuffer); hipFree(dbuffer);

The source and the target matrices must have the same format (see

[rocsparse_format](enumerations.html#rocsparse-types_8h_1ae1c0b9de06f3772ed14403400320b378)) and the same storage mode (see[rocsparse_storage_mode](enumerations.html#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13e)). The attributes of the target matrix, the fill mode[rocsparse_fill_mode](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1)and the diagonal type[rocsparse_diag_type](enumerations.html#rocsparse-types_8h_1a6e8e038adcd3fa03168a1cb4a7da1bc5)are used to parametrise the algorithm. These can be set on the target matrix using[rocsparse_spmat_set_attribute](auxiliary.html#rocsparse-auxiliary_8h_1a8531deaf78ab046aa608d00b7bb78c4c). See full example below.**Example**This example extracts the lower part of CSR matrix into a CSR matrix.

int main() { // 1 2 3 0 0 0 4 5 // 0 1 3 5 7 0 0 0 // 0 0 0 1 0 3 0 9 // 1 2 3 0 0 0 0 4 // 0 0 0 0 0 0 0 0 // 1 2 1 0 0 5 8 0 // 0 1 2 3 0 0 0 4 // 0 0 0 1 2 0 1 2 int32_t M = 8; int32_t N = 8; int32_t nnz = 29; std::vector<int32_t> hsource_row_ptr = {0, 5, 9, 12, 16, 16, 21, 25, 29}; std::vector<int32_t> hsource_col_ind = {0, 1, 2, 6, 7, 1, 2, 3, 4, 3, 5, 7, 0, 1, 2, 7, 0, 1, 2, 5, 6, 1, 2, 3, 7, 3, 4, 6, 7}; std::vector<float> hsource_val = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 1.0f, 3.0f, 5.0f, 7.0f, 1.0f, 3.0f, 9.0f, 1.0f, 2.0f, 3.0f, 4.0f, 1.0f, 2.0f, 1.0f, 5.0f, 8.0f, 1.0f, 2.0f, 3.0f, 4.0f, 1.0f, 2.0f, 1.0f, 2.0f}; int32_t* dsource_row_ptr; int32_t* dsource_col_ind; float* dsource_val; HIP_CHECK(hipMalloc(&dsource_row_ptr, sizeof(int32_t) * (M + 1))); HIP_CHECK(hipMalloc(&dsource_col_ind, sizeof(int32_t) * nnz)); HIP_CHECK(hipMalloc(&dsource_val, sizeof(float) * nnz)); HIP_CHECK(hipMemcpy( dsource_row_ptr, hsource_row_ptr.data(), sizeof(int32_t) * (M + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( dsource_col_ind, hsource_col_ind.data(), sizeof(int32_t) * nnz, hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dsource_val, hsource_val.data(), sizeof(float) * nnz, hipMemcpyHostToDevice)); rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Build Source rocsparse_spmat_descr source; ROCSPARSE_CHECK(rocsparse_create_csr_descr(&source, M, N, nnz, dsource_row_ptr, dsource_col_ind, dsource_val, rocsparse_indextype_i32, rocsparse_indextype_i32, rocsparse_index_base_zero, rocsparse_datatype_f32_r)); // Build target void* dtarget_row_ptr; HIP_CHECK(hipMalloc(&dtarget_row_ptr, sizeof(int32_t) * (M + 1))); rocsparse_spmat_descr target; ROCSPARSE_CHECK(rocsparse_create_csr_descr(&target, M, N, 0, dtarget_row_ptr, nullptr, nullptr, rocsparse_indextype_i32, rocsparse_indextype_i32, rocsparse_index_base_zero, rocsparse_datatype_f32_r)); const rocsparse_fill_mode fill_mode = rocsparse_fill_mode_lower; const rocsparse_diag_type diag_type = rocsparse_diag_type_non_unit; ROCSPARSE_CHECK(rocsparse_spmat_set_attribute( target, rocsparse_spmat_fill_mode, &fill_mode, sizeof(fill_mode))); ROCSPARSE_CHECK(rocsparse_spmat_set_attribute( target, rocsparse_spmat_diag_type, &diag_type, sizeof(diag_type))); // Create descriptor rocsparse_extract_descr descr; ROCSPARSE_CHECK( rocsparse_create_extract_descr(&descr, source, target, rocsparse_extract_alg_default)); // Analysis phase size_t buffer_size; ROCSPARSE_CHECK(rocsparse_extract_buffer_size( handle, descr, source, target, rocsparse_extract_stage_analysis, &buffer_size)); void* dbuffer; HIP_CHECK(hipMalloc(&dbuffer, buffer_size)); ROCSPARSE_CHECK(rocsparse_extract( handle, descr, source, target, rocsparse_extract_stage_analysis, buffer_size, dbuffer)); HIP_CHECK(hipFree(dbuffer)); // The user is responsible to allocate target arrays after the analysis phase. int64_t target_nnz; ROCSPARSE_CHECK(rocsparse_extract_nnz(handle, descr, &target_nnz)); std::cout << "target_nnz: " << target_nnz << std::endl; void* dtarget_col_ind; void* dtarget_val; HIP_CHECK(hipMalloc(&dtarget_col_ind, sizeof(int32_t) * target_nnz)); HIP_CHECK(hipMalloc(&dtarget_val, sizeof(float) * target_nnz)); ROCSPARSE_CHECK( rocsparse_csr_set_pointers(target, dtarget_row_ptr, dtarget_col_ind, dtarget_val)); // Calculation phase ROCSPARSE_CHECK(rocsparse_extract_buffer_size( handle, descr, source, target, rocsparse_extract_stage_compute, &buffer_size)); HIP_CHECK(hipMalloc(&dbuffer, buffer_size)); ROCSPARSE_CHECK(rocsparse_extract( handle, descr, source, target, rocsparse_extract_stage_compute, buffer_size, dbuffer)); HIP_CHECK(hipFree(dbuffer)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); HIP_CHECK(hipFree(dsource_row_ptr)); HIP_CHECK(hipFree(dsource_col_ind)); HIP_CHECK(hipFree(dsource_val)); HIP_CHECK(hipFree(dtarget_row_ptr)); HIP_CHECK(hipFree(dtarget_col_ind)); HIP_CHECK(hipFree(dtarget_val)); return 0; }


Note

This routine is asynchronous with respect to the host. This routine does support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**descr**–**[in]**descriptor of the extract algorithm.**source**–**[in]**sparse matrix descriptor.**target**–**[in]**sparse matrix descriptor.**stage**–**[in]**stage of the extract computation.**buffer_size_in_bytes**–**[in]**size in bytes of the`buffer`

**buffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_value**– if`stage`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`source`

,`target`

, or`buffer`

pointer is invalid.



## rocsparse_check_spmat[#](#rocsparse-check-spmat)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_check_spmat([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_const_spmat_descr](types.html#_CPPv427rocsparse_const_spmat_descr)mat,[rocsparse_data_status](enumerations.html#_CPPv421rocsparse_data_status)*data_status,[rocsparse_check_spmat_stage](enumerations.html#_CPPv427rocsparse_check_spmat_stage)stage, size_t *buffer_size, void *temp_buffer)[#](#_CPPv421rocsparse_check_spmat16rocsparse_handle27rocsparse_const_spmat_descrP21rocsparse_data_status27rocsparse_check_spmat_stageP6size_tPv) Check matrix to see if it is valid.

`rocsparse_check_spmat`

checks if the input matrix is valid.`rocsparse_check_spmat`

requires two steps to complete. First the user calls`rocsparse_check_spmat`

with the stage parameter set to[rocsparse_check_spmat_stage_buffer_size](enumerations.html#rocsparse-types_8h_1a0b7629347a648269b10b4dd9dce70a53abc8ebc05a32fffffcc61b0673b3f82d9)which determines the size of the temporary buffer needed in the second step. The user allocates this buffer and calls`rocsparse_check_spmat`

with the stage parameter set to[rocsparse_check_spmat_stage_compute](enumerations.html#rocsparse-types_8h_1a0b7629347a648269b10b4dd9dce70a53a638b6aab287a6b9177ed7740db0b2b95)which checks the input matrix for errors. Any detected errors in the input matrix are reported in the`data_status`

(passed to the function as a host pointer).**Uniform Precisions:**A

rocsparse_datatype_f32_r

rocsparse_datatype_f64_r

rocsparse_datatype_f32_c

rocsparse_datatype_f64_c

**Example**In this example we want to check whether a matrix is upper triangular. The matrix passed to

[rocsparse_check_spmat](#rocsparse__check__spmat_8h_1ad1ac73dbf7365e03bbcf7c4316d973bc)is invalid because it contains an entry in the lower triangular part of the matrix.int main() { // 1 2 0 0 // 3 0 4 0 // <-------contains a "3" in the lower part of matrix // 0 0 1 1 // 0 0 0 2 std::vector<int> hcsr_row_ptr = {0, 2, 4, 6, 7}; std::vector<int> hcsr_col_ind = {0, 1, 0, 2, 2, 3, 3}; std::vector<float> hcsr_val = {1, 2, 3, 4, 1, 1, 2}; int M = 4; int N = 4; int nnz = 7; int* dcsr_row_ptr; int* dcsr_col_ind; float* dcsr_val; HIP_CHECK(hipMalloc(&dcsr_row_ptr, sizeof(int) * (M + 1))); HIP_CHECK(hipMalloc(&dcsr_col_ind, sizeof(int) * nnz)); HIP_CHECK(hipMalloc(&dcsr_val, sizeof(float) * nnz)); HIP_CHECK( hipMemcpy(dcsr_row_ptr, hcsr_row_ptr.data(), sizeof(int) * (M + 1), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsr_col_ind, hcsr_col_ind.data(), sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsr_val, hcsr_val.data(), sizeof(float) * nnz, hipMemcpyHostToDevice)); rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); rocsparse_spmat_descr matA; ROCSPARSE_CHECK(rocsparse_create_csr_descr(&matA, M, N, nnz, dcsr_row_ptr, dcsr_col_ind, dcsr_val, rocsparse_indextype_i32, rocsparse_indextype_i32, rocsparse_index_base_zero, rocsparse_datatype_f32_r)); const rocsparse_fill_mode fill_mode = rocsparse_fill_mode_upper; const rocsparse_matrix_type matrix_type = rocsparse_matrix_type_triangular; ROCSPARSE_CHECK(rocsparse_spmat_set_attribute( matA, rocsparse_spmat_fill_mode, &fill_mode, sizeof(fill_mode))); ROCSPARSE_CHECK(rocsparse_spmat_set_attribute( matA, rocsparse_spmat_matrix_type, &matrix_type, sizeof(matrix_type))); rocsparse_data_status data_status; size_t buffer_size; ROCSPARSE_CHECK(rocsparse_check_spmat(handle, matA, &data_status, rocsparse_check_spmat_stage_buffer_size, &buffer_size, nullptr)); void* dbuffer; HIP_CHECK(hipMalloc(&dbuffer, buffer_size)); ROCSPARSE_CHECK(rocsparse_check_spmat( handle, matA, &data_status, rocsparse_check_spmat_stage_compute, &buffer_size, dbuffer)); std::cout << "data_status: " << data_status << std::endl; ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); ROCSPARSE_CHECK(rocsparse_destroy_spmat_descr(matA)); HIP_CHECK(hipFree(dbuffer)); HIP_CHECK(hipFree(dcsr_row_ptr)); HIP_CHECK(hipFree(dcsr_col_ind)); HIP_CHECK(hipFree(dcsr_val)); return 0; }


Note

This function writes the required allocation size (in bytes) to

`buffer_size`

and returns without performing the checking operation, when stage is equal to[rocsparse_check_spmat_stage_buffer_size](enumerations.html#rocsparse-types_8h_1a0b7629347a648269b10b4dd9dce70a53abc8ebc05a32fffffcc61b0673b3f82d9).Note

The sparse matrix formats currently supported are: rocsparse_format_coo, rocsparse_format_csr, rocsparse_format_csc and rocsparse_format_ell.

Note

check_spmat requires two stages to complete. The first stage

[rocsparse_check_spmat_stage_buffer_size](enumerations.html#rocsparse-types_8h_1a0b7629347a648269b10b4dd9dce70a53abc8ebc05a32fffffcc61b0673b3f82d9)will return the size of the temporary storage buffer that is required for subsequent calls to[rocsparse_check_spmat](#rocsparse__check__spmat_8h_1ad1ac73dbf7365e03bbcf7c4316d973bc). In the final stage[rocsparse_check_spmat_stage_compute](enumerations.html#rocsparse-types_8h_1a0b7629347a648269b10b4dd9dce70a53a638b6aab287a6b9177ed7740db0b2b95), the actual computation is performed.Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**mat**–**[in]**matrix descriptor.**data_status**–**[out]**modified to indicate the status of the data**stage**–**[in]**check_matrix stage for the matrix computation.**buffer_size**–**[out]**number of bytes of the temporary storage buffer. buffer_size is set when`temp_buffer`

is nullptr.**temp_buffer**–**[in]**temporary storage buffer allocated by the user. When a nullptr is passed, the required allocation size (in bytes) is written to`buffer_size`

and function returns without performing the checking operation.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`mat`

,`buffer_size`

,`temp_buffer`

or`data_status`

pointer is invalid.**rocsparse_status_invalid_value**– the value of stage is incorrect.



## rocsparse_spitsv[#](#rocsparse-spitsv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_spitsv([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)*host_nmaxiter, const void *host_tol, void *host_history,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans, const void *alpha, const[rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)mat, const[rocsparse_dnvec_descr](types.html#_CPPv421rocsparse_dnvec_descr)x, const[rocsparse_dnvec_descr](types.html#_CPPv421rocsparse_dnvec_descr)y,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)compute_type,[rocsparse_spitsv_alg](enumerations.html#_CPPv420rocsparse_spitsv_alg)alg,[rocsparse_spitsv_stage](enumerations.html#_CPPv422rocsparse_spitsv_stage)stage, size_t *buffer_size, void *temp_buffer)[#](#_CPPv416rocsparse_spitsv16rocsparse_handleP13rocsparse_intPKvPv19rocsparse_operationPKvK21rocsparse_spmat_descrK21rocsparse_dnvec_descrK21rocsparse_dnvec_descr18rocsparse_datatype20rocsparse_spitsv_alg22rocsparse_spitsv_stageP6size_tPv) Sparse iterative triangular solve.

`rocsparse_spitsv`

solves, using the Jacobi iterative method, a sparse triangular linear system of a sparse \(m \times m\) matrix, defined in CSR format, a dense solution vector \(y\) and the right-hand side \(x\) that is multiplied by \(\alpha\), such that\[ op(A) y = \alpha x, \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if trans == rocsparse_operation_none} \\ A^T, & \text{if trans == rocsparse_operation_transpose} \\ A^H, & \text{if trans == rocsparse_operation_conjugate_transpose} \end{array} \right. \end{split}\]The Jacobi method applied to the sparse triangular linear system above gives

\[ y_{k+1} = y_{k} + D^{-1} ( \alpha x - (D + T) y_{k} ) \]with \(A = D + T\), \(D\) the diagonal of \(A\) and \(T\) the strict triangular part of \(A\).The above equation can be also written as

\[ y_{k+1} = y_{k} + D^{-1} r_k \]where\[ r_k = \alpha x - (D + T) y_k. \]Starting with \(y_0 = \)`y`

, the method iterates while \( k \lt \)`host_nmaxiter`

and until\[ \Vert r_k \Vert_{\infty} \le \epsilon, \]with \(\epsilon\) =`host_tol`

.`rocsparse_spitsv`

requires three stages to complete. First, the user passes the[rocsparse_spitsv_stage_buffer_size](enumerations.html#rocsparse-types_8h_1ae307fdb92148195e71d428b7a62dea0cad5b8b6e106eb2c922a5c6f62851e4115)stage to determine the size of the required temporary storage buffer. Next, the user allocates this buffer and calls`rocsparse_spitsv`

again with the[rocsparse_spitsv_stage_preprocess](enumerations.html#rocsparse-types_8h_1ae307fdb92148195e71d428b7a62dea0cabf1b8852b5312a0762b3ff0a66cf578d)stage which will preprocess data and store it in the temporary buffer. Finally, the user calls`rocsparse_spitsv`

with the[rocsparse_spitsv_stage_compute](enumerations.html#rocsparse-types_8h_1ae307fdb92148195e71d428b7a62dea0ca955c9f450615646ed6b9f378c9693405)stage to perform the actual computation. Once all calls to`rocsparse_spitsv`

are complete, the temporary buffer can be deallocated.`rocsparse_spitsv`

supports[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)and[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4)index precisions for storing the row pointer and column indices arrays of the sparse matrix.`rocsparse_spitsv`

supports the following data types for \(op(A)\), \(x\), \(y\) and compute types for \(\alpha\):**Uniform Precisions:**A / X / Y / compute_type

rocsparse_datatype_f32_r

rocsparse_datatype_f64_r

rocsparse_datatype_f32_c

rocsparse_datatype_f64_c

**Example**int main() { // 1 0 0 0 // A = 0 2 0 0 // 5 0 3 0 // 0 0 9 4 int m = 4; int n = 4; int nnz = 6; float halpha = 1.0f; std::vector<int> hcsr_row_ptr = {0, 1, 2, 4, 6}; std::vector<int> hcsr_col_ind = {0, 1, 0, 2, 2, 3}; std::vector<float> hcsr_val = {1.0f, 2.0f, 5.0f, 3.0f, 9.0f, 4.0f}; std::vector<float> hx(m, 1.0f); std::vector<float> hy(m, 1.0f); // Offload data to device int* dcsr_row_ptr; int* dcsr_col_ind; float* dcsr_val; float* dx; float* dy; HIP_CHECK(hipMalloc(&dcsr_row_ptr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc(&dcsr_col_ind, sizeof(int) * nnz)); HIP_CHECK(hipMalloc(&dcsr_val, sizeof(float) * nnz)); HIP_CHECK(hipMalloc(&dx, sizeof(float) * m)); HIP_CHECK(hipMalloc(&dy, sizeof(float) * m)); HIP_CHECK( hipMemcpy(dcsr_row_ptr, hcsr_row_ptr.data(), sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsr_col_ind, hcsr_col_ind.data(), sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsr_val, hcsr_val.data(), sizeof(float) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dx, hx.data(), sizeof(float) * m, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dy, hy.data(), sizeof(float) * m, hipMemcpyHostToDevice)); rocsparse_handle handle; rocsparse_spmat_descr matA; rocsparse_dnvec_descr vecX; rocsparse_dnvec_descr vecY; rocsparse_indextype row_ptr_type = rocsparse_indextype_i32; rocsparse_indextype col_idx_type = rocsparse_indextype_i32; rocsparse_datatype data_type = rocsparse_datatype_f32_r; rocsparse_datatype compute_type = rocsparse_datatype_f32_r; rocsparse_index_base idx_base = rocsparse_index_base_zero; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Create sparse matrix A ROCSPARSE_CHECK(rocsparse_create_csr_descr(&matA, m, m, nnz, dcsr_row_ptr, dcsr_col_ind, dcsr_val, row_ptr_type, col_idx_type, idx_base, data_type)); ROCSPARSE_CHECK(rocsparse_create_dnvec_descr(&vecX, m, dx, data_type)); ROCSPARSE_CHECK(rocsparse_create_dnvec_descr(&vecY, m, dy, data_type)); rocsparse_int host_nmaxiter[1] = {200}; float host_tol[1] = {1.0e-6}; float host_history[200]; size_t buffer_size = 0; ROCSPARSE_CHECK(rocsparse_spitsv(handle, &host_nmaxiter[0], &host_tol[0], &host_history[0], rocsparse_operation_none, &halpha, matA, vecX, vecY, compute_type, rocsparse_spitsv_alg_default, rocsparse_spitsv_stage_buffer_size, &buffer_size, nullptr)); void* temp_buffer; HIP_CHECK(hipMalloc(&temp_buffer, buffer_size)); ROCSPARSE_CHECK(rocsparse_spitsv(handle, &host_nmaxiter[0], &host_tol[0], &host_history[0], rocsparse_operation_none, &halpha, matA, vecX, vecY, compute_type, rocsparse_spitsv_alg_default, rocsparse_spitsv_stage_preprocess, nullptr, temp_buffer)); ROCSPARSE_CHECK(rocsparse_spitsv(handle, &host_nmaxiter[0], &host_tol[0], &host_history[0], rocsparse_operation_none, &halpha, matA, vecX, vecY, compute_type, rocsparse_spitsv_alg_default, rocsparse_spitsv_stage_compute, &buffer_size, temp_buffer)); HIP_CHECK(hipMemcpy(hy.data(), dy, sizeof(float) * m, hipMemcpyDeviceToHost)); // Clear rocSPARSE ROCSPARSE_CHECK(rocsparse_destroy_spmat_descr(matA)); ROCSPARSE_CHECK(rocsparse_destroy_dnvec_descr(vecX)); ROCSPARSE_CHECK(rocsparse_destroy_dnvec_descr(vecY)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); // Clear device memory HIP_CHECK(hipFree(dcsr_row_ptr)); HIP_CHECK(hipFree(dcsr_col_ind)); HIP_CHECK(hipFree(dcsr_val)); HIP_CHECK(hipFree(dx)); HIP_CHECK(hipFree(dy)); return 0; }


Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**host_nmaxiter**–**[inout]**maximum number of iteration on input and number of iteration on output. If the output number of iterations is strictly less than the input maximum number of iterations, then the algorithm converged.**host_tol**–**[in]**if the pointer is null then loop will execute`nmaxiter`

[0] iterations. The precision is float for f32 based calculation (including the complex case) and double for f64 based calculation (including the complex case).**host_history**–**[out]**Optional array to record the norm of the residual before each iteration. The precision is float for f32 based calculation (including the complex case) and double for f64 based calculation (including the complex case).**trans**–**[in]**matrix operation type.**alpha**–**[in]**scalar \(\alpha\).**mat**–**[in]**matrix descriptor.**x**–**[in]**vector descriptor.**y**–**[inout]**vector descriptor.**compute_type**–**[in]**floating point precision for the SpITSV computation.**alg**–**[in]**SpITSV algorithm for the SpITSV computation.**stage**–**[in]**SpITSV stage for the SpITSV computation.**buffer_size**–**[out]**number of bytes of the temporary storage buffer.**temp_buffer**–**[in]**temporary storage buffer allocated by the user. When a nullptr is passed, the required allocation size (in bytes) is written to`buffer_size`

and function returns without performing the SpITSV operation.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`alpha`

,`mat`

,`x`

,`y`

,`descr`

or`buffer_size`

pointer is invalid.**rocsparse_status_not_implemented**–`trans`

,`compute_type`

,`stage`

or`alg`

is currently not supported.
