---
title: "Sparse level 1 functions &#8212; rocSPARSE 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocSPARSE/en/latest/reference/level1.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:16:54.435822+00:00
content_hash: "021b15e838bfa334"
---

# Sparse level 1 functions[#](#sparse-level-1-functions)

The sparse level 1 routines describe operations between a vector in sparse format and a vector in dense format. This section describes all rocSPARSE level 1 sparse linear algebra functions.

## rocsparse_axpyi()[#](#rocsparse-axpyi)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_saxpyi([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const float *alpha, const float *x_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*x_ind, float *y,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base)[#](#_CPPv416rocsparse_saxpyi16rocsparse_handle13rocsparse_intPKfPKfPK13rocsparse_intPf20rocsparse_index_base)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_daxpyi([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const double *alpha, const double *x_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*x_ind, double *y,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base)[#](#_CPPv416rocsparse_daxpyi16rocsparse_handle13rocsparse_intPKdPKdPK13rocsparse_intPd20rocsparse_index_base)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_caxpyi([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*alpha, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*x_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*x_ind,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*y,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base)[#](#_CPPv416rocsparse_caxpyi16rocsparse_handle13rocsparse_intPK23rocsparse_float_complexPK23rocsparse_float_complexPK13rocsparse_intP23rocsparse_float_complex20rocsparse_index_base)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zaxpyi([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*alpha, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*x_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*x_ind,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*y,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base)[#](#_CPPv416rocsparse_zaxpyi16rocsparse_handle13rocsparse_intPK24rocsparse_double_complexPK24rocsparse_double_complexPK13rocsparse_intP24rocsparse_double_complex20rocsparse_index_base) Scale a sparse vector and add it to a dense vector.

`rocsparse_axpyi`

multiplies the sparse vector \(x\) with scalar \(\alpha\) and adds the result to the dense vector \(y\), such that\[ y := y + \alpha \cdot x \]for(i = 0; i < nnz; ++i) { y[x_ind[i]] = y[x_ind[i]] + alpha * x_val[i]; }

**Example**int main() { // Number of non-zeros of the sparse vector const rocsparse_int nnz = 3; // Number of entries in the dense vector const rocsparse_int size = 9; // Sparse index vector rocsparse_int hx_ind[nnz] = {0, 3, 5}; // Sparse value vector float hx_val[nnz] = {1.0f, 2.0f, 3.0f}; // Dense vector float hy[size] = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f, 9.0f}; // Scalar alpha float alpha = 3.7f; // Index base rocsparse_index_base idx_base = rocsparse_index_base_zero; // Offload data to device rocsparse_int* dx_ind; float* dx_val; float* dy; HIP_CHECK(hipMalloc(&dx_ind, sizeof(rocsparse_int) * nnz)); HIP_CHECK(hipMalloc(&dx_val, sizeof(float) * nnz)); HIP_CHECK(hipMalloc(&dy, sizeof(float) * size)); HIP_CHECK(hipMemcpy(dx_ind, hx_ind, sizeof(rocsparse_int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dx_val, hx_val, sizeof(float) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dy, hy, sizeof(float) * size, hipMemcpyHostToDevice)); // rocSPARSE handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Call saxpyi to perform y = y + alpha * x ROCSPARSE_CHECK(rocsparse_saxpyi(handle, nnz, &alpha, dx_val, dx_ind, dy, idx_base)); // Copy result back to host HIP_CHECK(hipMemcpy(hy, dy, sizeof(float) * size, hipMemcpyDeviceToHost)); std::cout << "hy" << std::endl; for(rocsparse_int i = 0; i < size; i++) { std::cout << hy[i] << " "; } std::cout << "" << std::endl; // Clear rocSPARSE ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); // Clear device memory HIP_CHECK(hipFree(dx_ind)); HIP_CHECK(hipFree(dx_val)); HIP_CHECK(hipFree(dy)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**nnz**–**[in]**number of non-zero entries of vector \(x\).**alpha**–**[in]**scalar \(\alpha\).**x_val**–**[in]**array of`nnz`

elements containing the values of \(x\).**x_ind**–**[in]**array of`nnz`

elements containing the indices of the non-zero values of \(x\).**y**–**[inout]**array of values in dense format.**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_value**–`idx_base`

is invalid.**rocsparse_status_invalid_size**–`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`alpha`

,`x_val`

,`x_ind`

or`y`

pointer is invalid.



## rocsparse_doti()[#](#rocsparse-doti)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sdoti([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const float *x_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*x_ind, const float *y, float *result,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base)[#](#_CPPv415rocsparse_sdoti16rocsparse_handle13rocsparse_intPKfPK13rocsparse_intPKfPf20rocsparse_index_base)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ddoti([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const double *x_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*x_ind, const double *y, double *result,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base)[#](#_CPPv415rocsparse_ddoti16rocsparse_handle13rocsparse_intPKdPK13rocsparse_intPKdPd20rocsparse_index_base)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cdoti([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*x_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*x_ind, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*y,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*result,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base)[#](#_CPPv415rocsparse_cdoti16rocsparse_handle13rocsparse_intPK23rocsparse_float_complexPK13rocsparse_intPK23rocsparse_float_complexP23rocsparse_float_complex20rocsparse_index_base)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zdoti([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*x_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*x_ind, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*y,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*result,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base)[#](#_CPPv415rocsparse_zdoti16rocsparse_handle13rocsparse_intPK24rocsparse_double_complexPK13rocsparse_intPK24rocsparse_double_complexP24rocsparse_double_complex20rocsparse_index_base) Compute the dot product of a sparse vector with a dense vector.

`rocsparse_doti`

computes the dot product of the sparse vector \(x\) with the dense vector \(y\), such that\[ \text{result} := y^T x \]result = 0 for(i = 0; i < nnz; ++i) { result += x_val[i] * y[x_ind[i]]; }

**Example**int main() { // Number of non-zeros of the sparse vector const rocsparse_int nnz = 3; // Number of entries in the dense vector const rocsparse_int size = 9; // Sparse index vector rocsparse_int hx_ind[nnz] = {0, 3, 5}; // Sparse value vector float hx_val[nnz] = {1.0f, 2.0f, 3.0f}; // Dense vector float hy[size] = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f, 9.0f}; // Index base rocsparse_index_base idx_base = rocsparse_index_base_zero; // Offload data to device rocsparse_int* dx_ind; float* dx_val; float* dy; HIP_CHECK(hipMalloc(&dx_ind, sizeof(rocsparse_int) * nnz)); HIP_CHECK(hipMalloc(&dx_val, sizeof(float) * nnz)); HIP_CHECK(hipMalloc(&dy, sizeof(float) * size)); HIP_CHECK(hipMemcpy(dx_ind, hx_ind, sizeof(rocsparse_int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dx_val, hx_val, sizeof(float) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dy, hy, sizeof(float) * size, hipMemcpyHostToDevice)); // rocSPARSE handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Call sdoti to compute the dot product float dot; ROCSPARSE_CHECK(rocsparse_sdoti(handle, nnz, dx_val, dx_ind, dy, &dot, idx_base)); std::cout << "dot: " << dot << std::endl; // Clear rocSPARSE ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); // Clear device memory HIP_CHECK(hipFree(dx_ind)); HIP_CHECK(hipFree(dx_val)); HIP_CHECK(hipFree(dy)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**nnz**–**[in]**number of non-zero entries of vector \(x\).**x_val**–**[in]**array of`nnz`

values.**x_ind**–**[in]**array of`nnz`

elements containing the indices of the non-zero values of \(x\).**y**–**[in]**array of values in dense format.**result**–**[out]**pointer to the result, can be host or device memory**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_value**–`idx_base`

is invalid.**rocsparse_status_invalid_size**–`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`x_val`

,`x_ind`

,`y`

or`result`

pointer is invalid.**rocsparse_status_memory_error**– the buffer for the dot product reduction could not be allocated.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_dotci()[#](#rocsparse-dotci)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cdotci([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*x_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*x_ind, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*y,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*result,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base)[#](#_CPPv416rocsparse_cdotci16rocsparse_handle13rocsparse_intPK23rocsparse_float_complexPK13rocsparse_intPK23rocsparse_float_complexP23rocsparse_float_complex20rocsparse_index_base)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zdotci([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*x_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*x_ind, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*y,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*result,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base)[#](#_CPPv416rocsparse_zdotci16rocsparse_handle13rocsparse_intPK24rocsparse_double_complexPK13rocsparse_intPK24rocsparse_double_complexP24rocsparse_double_complex20rocsparse_index_base) Compute the dot product of a complex conjugate sparse vector with a dense vector.

`rocsparse_dotci`

computes the dot product of the complex conjugate sparse vector \(x\) with the dense vector \(y\), such that\[ \text{result} := \bar{x}^H y \]result = 0 for(i = 0; i < nnz; ++i) { result += conj(x_val[i]) * y[x_ind[i]]; }

Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**nnz**–**[in]**number of non-zero entries of vector \(x\).**x_val**–**[in]**array of`nnz`

values.**x_ind**–**[in]**array of`nnz`

elements containing the indices of the non-zero values of \(x\).**y**–**[in]**array of values in dense format.**result**–**[out]**pointer to the result, can be host or device memory**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_value**–`idx_base`

is invalid.**rocsparse_status_invalid_size**–`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`x_val`

,`x_ind`

,`y`

or`result`

pointer is invalid.**rocsparse_status_memory_error**– the buffer for the dot product reduction could not be allocated.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_gthr()[#](#rocsparse-gthr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sgthr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const float *y, float *x_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*x_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base)[#](#_CPPv415rocsparse_sgthr16rocsparse_handle13rocsparse_intPKfPfPK13rocsparse_int20rocsparse_index_base)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dgthr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const double *y, double *x_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*x_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base)[#](#_CPPv415rocsparse_dgthr16rocsparse_handle13rocsparse_intPKdPdPK13rocsparse_int20rocsparse_index_base)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cgthr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*y,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*x_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*x_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base)[#](#_CPPv415rocsparse_cgthr16rocsparse_handle13rocsparse_intPK23rocsparse_float_complexP23rocsparse_float_complexPK13rocsparse_int20rocsparse_index_base)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zgthr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*y,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*x_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*x_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base)[#](#_CPPv415rocsparse_zgthr16rocsparse_handle13rocsparse_intPK24rocsparse_double_complexP24rocsparse_double_complexPK13rocsparse_int20rocsparse_index_base) Gather elements from a dense vector and store them into a sparse vector.

`rocsparse_gthr`

gathers the elements that are listed in`x_ind`

from the dense vector \(y\) and stores them in the sparse vector \(x\).for(i = 0; i < nnz; ++i) { x_val[i] = y[x_ind[i]]; }

**Example**int main() { // Number of non-zeros of the sparse vector const rocsparse_int nnz = 3; // Number of entries in the dense vector const rocsparse_int size = 9; // Sparse index vector rocsparse_int hx_ind[nnz] = {0, 3, 5}; // Sparse value vector float hx_val[nnz]; // Dense vector float hy[size] = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0}; // Index base rocsparse_index_base idx_base = rocsparse_index_base_zero; // Offload data to device rocsparse_int* dx_ind; float* dx_val; float* dy; HIP_CHECK(hipMalloc(&dx_ind, sizeof(rocsparse_int) * nnz)); HIP_CHECK(hipMalloc(&dx_val, sizeof(float) * nnz)); HIP_CHECK(hipMalloc(&dy, sizeof(float) * size)); HIP_CHECK(hipMemcpy(dx_ind, hx_ind, sizeof(rocsparse_int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dy, hy, sizeof(float) * size, hipMemcpyHostToDevice)); // rocSPARSE handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Call sgthr ROCSPARSE_CHECK(rocsparse_sgthr(handle, nnz, dy, dx_val, dx_ind, idx_base)); // Copy result back to host HIP_CHECK(hipMemcpy(hx_val, dx_val, sizeof(float) * nnz, hipMemcpyDeviceToHost)); std::cout << "hx_val" << std::endl; for(rocsparse_int i = 0; i < nnz; i++) { std::cout << hx_val[i] << " "; } std::cout << "" << std::endl; // Clear rocSPARSE ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); // Clear device memory HIP_CHECK(hipFree(dx_ind)); HIP_CHECK(hipFree(dx_val)); HIP_CHECK(hipFree(dy)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**nnz**–**[in]**number of non-zero entries of \(x\).**y**–**[in]**array of values in dense format.**x_val**–**[out]**array of`nnz`

elements containing the values of \(x\).**x_ind**–**[in]**array of`nnz`

elements containing the indices of the non-zero values of \(x\).**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_value**–`idx_base`

is invalid.**rocsparse_status_invalid_size**–`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`y`

,`x_val`

or`x_ind`

pointer is invalid.



## rocsparse_gthrz()[#](#rocsparse-gthrz)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sgthrz([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, float *y, float *x_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*x_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base)[#](#_CPPv416rocsparse_sgthrz16rocsparse_handle13rocsparse_intPfPfPK13rocsparse_int20rocsparse_index_base)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dgthrz([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, double *y, double *x_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*x_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base)[#](#_CPPv416rocsparse_dgthrz16rocsparse_handle13rocsparse_intPdPdPK13rocsparse_int20rocsparse_index_base)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cgthrz([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*y,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*x_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*x_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base)[#](#_CPPv416rocsparse_cgthrz16rocsparse_handle13rocsparse_intP23rocsparse_float_complexP23rocsparse_float_complexPK13rocsparse_int20rocsparse_index_base)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zgthrz([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*y,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*x_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*x_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base)[#](#_CPPv416rocsparse_zgthrz16rocsparse_handle13rocsparse_intP24rocsparse_double_complexP24rocsparse_double_complexPK13rocsparse_int20rocsparse_index_base) Gather and zero out elements from a dense vector and store them into a sparse vector.

`rocsparse_gthrz`

gathers the elements that are listed in`x_ind`

from the dense vector \(y\) and stores them in the sparse vector \(x\). The gathered elements in \(y\) are replaced by zero.for(i = 0; i < nnz; ++i) { x_val[i] = y[x_ind[i]]; y[x_ind[i]] = 0; }

Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**nnz**–**[in]**number of non-zero entries of \(x\).**y**–**[inout]**array of values in dense format.**x_val**–**[out]**array of`nnz`

elements containing the non-zero values of \(x\).**x_ind**–**[in]**array of`nnz`

elements containing the indices of the non-zero values of \(x\).**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_value**–`idx_base`

is invalid.**rocsparse_status_invalid_size**–`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`y`

,`x_val`

or`x_ind`

pointer is invalid.



## rocsparse_roti()[#](#rocsparse-roti)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sroti([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, float *x_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*x_ind, float *y, const float *c, const float *s,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base)[#](#_CPPv415rocsparse_sroti16rocsparse_handle13rocsparse_intPfPK13rocsparse_intPfPKfPKf20rocsparse_index_base)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_droti([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, double *x_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*x_ind, double *y, const double *c, const double *s,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base)[#](#_CPPv415rocsparse_droti16rocsparse_handle13rocsparse_intPdPK13rocsparse_intPdPKdPKd20rocsparse_index_base) Apply Givens rotation to a dense and a sparse vector.

`rocsparse_roti`

applies the Givens rotation matrix \(G\) to the sparse vector \(x\) and the dense vector \(y\), where\[\begin{split} G = \begin{pmatrix} c & s \\ -s & c \end{pmatrix} \end{split}\]for(i = 0; i < nnz; ++i) { x_tmp = x_val[i]; y_tmp = y[x_ind[i]]; x_val[i] = c * x_tmp + s * y_tmp; y[x_ind[i]] = c * y_tmp - s * x_tmp; }

**Example**int main() { // Number of non-zeros of the sparse vector const rocsparse_int nnz = 3; // Number of entries in the dense vector const rocsparse_int size = 9; // Sparse index vector rocsparse_int hx_ind[nnz] = {0, 3, 5}; // Sparse value vector float hx_val[nnz] = {1.0f, 2.0f, 3.0f}; // Dense vector float hy[size] = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f, 9.0f}; // c and s float c = 3.7; float s = 1.3; // Index base rocsparse_index_base idx_base = rocsparse_index_base_zero; // Offload data to device rocsparse_int* dx_ind; float* dx_val; float* dy; HIP_CHECK(hipMalloc(&dx_ind, sizeof(rocsparse_int) * nnz)); HIP_CHECK(hipMalloc(&dx_val, sizeof(float) * nnz)); HIP_CHECK(hipMalloc(&dy, sizeof(float) * size)); HIP_CHECK(hipMemcpy(dx_ind, hx_ind, sizeof(rocsparse_int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dx_val, hx_val, sizeof(float) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dy, hy, sizeof(float) * size, hipMemcpyHostToDevice)); // rocSPARSE handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Call sroti ROCSPARSE_CHECK(rocsparse_sroti(handle, nnz, dx_val, dx_ind, dy, &c, &s, idx_base)); // Copy result back to host HIP_CHECK(hipMemcpy(hx_val, dx_val, sizeof(float) * nnz, hipMemcpyDeviceToHost)); HIP_CHECK(hipMemcpy(hy, dy, sizeof(float) * size, hipMemcpyDeviceToHost)); std::cout << "hx_val" << std::endl; for(rocsparse_int i = 0; i < nnz; i++) { std::cout << hx_val[i] << " "; } std::cout << "" << std::endl; std::cout << "hy" << std::endl; for(rocsparse_int i = 0; i < size; i++) { std::cout << hy[i] << " "; } std::cout << "" << std::endl; // Clear rocSPARSE ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); // Clear device memory HIP_CHECK(hipFree(dx_ind)); HIP_CHECK(hipFree(dx_val)); HIP_CHECK(hipFree(dy)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**nnz**–**[in]**number of non-zero entries of \(x\).**x_val**–**[inout]**array of`nnz`

elements containing the non-zero values of \(x\).**x_ind**–**[in]**array of`nnz`

elements containing the indices of the non-zero values of \(x\).**y**–**[inout]**array of values in dense format.**c**–**[in]**pointer to the cosine element of \(G\), can be on host or device.**s**–**[in]**pointer to the sine element of \(G\), can be on host or device.**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_value**–`idx_base`

is invalid.**rocsparse_status_invalid_size**–`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`c`

,`s`

,`x_val`

,`x_ind`

or`y`

pointer is invalid.



## rocsparse_sctr()[#](#rocsparse-sctr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ssctr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const float *x_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*x_ind, float *y,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base)[#](#_CPPv415rocsparse_ssctr16rocsparse_handle13rocsparse_intPKfPK13rocsparse_intPf20rocsparse_index_base)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dsctr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const double *x_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*x_ind, double *y,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base)[#](#_CPPv415rocsparse_dsctr16rocsparse_handle13rocsparse_intPKdPK13rocsparse_intPd20rocsparse_index_base)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_csctr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*x_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*x_ind,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*y,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base)[#](#_CPPv415rocsparse_csctr16rocsparse_handle13rocsparse_intPK23rocsparse_float_complexPK13rocsparse_intP23rocsparse_float_complex20rocsparse_index_base)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zsctr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*x_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*x_ind,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*y,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base)[#](#_CPPv415rocsparse_zsctr16rocsparse_handle13rocsparse_intPK24rocsparse_double_complexPK13rocsparse_intP24rocsparse_double_complex20rocsparse_index_base) Scatter elements from a dense vector across a sparse vector.

`rocsparse_sctr`

scatters the elements that are listed in`x_ind`

from the sparse vector \(x\) into the dense vector \(y\). Indices of \(y\) that are not listed in`x_ind`

remain unchanged.for(i = 0; i < nnz; ++i) { y[x_ind[i]] = x_val[i]; }

**Example**int main() { // Number of non-zeros of the sparse vector const rocsparse_int nnz = 3; // Number of entries in the dense vector const rocsparse_int size = 9; // Sparse index vector rocsparse_int hx_ind[nnz] = {0, 3, 5}; // Sparse value vector float hx_val[nnz] = {9.0, 2.0, 3.0}; // Dense vector float hy[size] = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0}; // Index base rocsparse_index_base idx_base = rocsparse_index_base_zero; // Offload data to device rocsparse_int* dx_ind; float* dx_val; float* dy; HIP_CHECK(hipMalloc(&dx_ind, sizeof(rocsparse_int) * nnz)); HIP_CHECK(hipMalloc(&dx_val, sizeof(float) * nnz)); HIP_CHECK(hipMalloc(&dy, sizeof(float) * size)); HIP_CHECK(hipMemcpy(dx_ind, hx_ind, sizeof(rocsparse_int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dx_val, hx_val, sizeof(float) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dy, hy, sizeof(float) * size, hipMemcpyHostToDevice)); // rocSPARSE handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Call ssctr ROCSPARSE_CHECK(rocsparse_ssctr(handle, nnz, dx_val, dx_ind, dy, idx_base)); // Copy result back to host HIP_CHECK(hipMemcpy(hy, dy, sizeof(float) * size, hipMemcpyDeviceToHost)); std::cout << "hy" << std::endl; for(rocsparse_int i = 0; i < size; i++) { std::cout << hy[i] << " "; } std::cout << "" << std::endl; // Clear rocSPARSE ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); // Clear device memory HIP_CHECK(hipFree(dx_ind)); HIP_CHECK(hipFree(dx_val)); HIP_CHECK(hipFree(dy)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**nnz**–**[in]**number of non-zero entries of \(x\).**x_val**–**[in]**array of`nnz`

elements containing the non-zero values of \(x\).**x_ind**–**[in]**array of`nnz`

elements containing the indices of the non-zero values of x.**y**–**[inout]**array of values in dense format.**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_value**–`idx_base`

is invalid.**rocsparse_status_invalid_size**–`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`x_val`

,`x_ind`

or`y`

pointer is invalid.
