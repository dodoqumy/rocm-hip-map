---
title: "Sparse conversion functions &#8212; rocSPARSE 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocSPARSE/en/latest/reference/conversion.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:16:38.699744+00:00
content_hash: "bb5e93c3a5f6265d"
---

# Sparse conversion functions[#](#sparse-conversion-functions)

This module contains all sparse conversion routines.

The sparse conversion routines describe operations on a matrix in sparse format to obtain a matrix in a different sparse format.

## rocsparse_csr2coo()[#](#rocsparse-csr2coo)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_csr2coo([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_row_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base)[#](#_CPPv417rocsparse_csr2coo16rocsparse_handlePK13rocsparse_int13rocsparse_int13rocsparse_intP13rocsparse_int20rocsparse_index_base) Convert a sparse CSR matrix into a sparse COO matrix.

`rocsparse_csr2coo`

converts the CSR array containing the row offsets, that point to the start of every row, into a COO array of row indices.`rocsparse_csr2coo`

can also be used to convert a CSC array containing the column offsets into a COO array of column indices.**Example**This example converts a CSR matrix into a COO matrix.

int main() { // Initialize rocSPARSE rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // 1 2 0 3 0 // A = 0 4 5 0 0 // 6 0 0 7 8 rocsparse_int m = 3; rocsparse_int n = 5; rocsparse_int nnz = 8; // Define host arrays rocsparse_int h_csr_row_ptr[] = {0, 3, 5, 8}; rocsparse_int h_csr_col_ind[] = {0, 1, 3, 1, 2, 0, 3, 4}; float h_csr_val[] = {1, 2, 3, 4, 5, 6, 7, 8}; // Allocate and initialize device memory rocsparse_int* d_csr_row_ptr; rocsparse_int* d_csr_col_ind; float* d_csr_val; HIP_CHECK(hipMalloc((void**)&d_csr_row_ptr, sizeof(rocsparse_int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&d_csr_col_ind, sizeof(rocsparse_int) * nnz)); HIP_CHECK(hipMalloc((void**)&d_csr_val, sizeof(float) * nnz)); HIP_CHECK(hipMemcpy( d_csr_row_ptr, h_csr_row_ptr, sizeof(rocsparse_int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( d_csr_col_ind, h_csr_col_ind, sizeof(rocsparse_int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(d_csr_val, h_csr_val, sizeof(float) * nnz, hipMemcpyHostToDevice)); // Allocate COO matrix arrays rocsparse_int* d_coo_row_ind; rocsparse_int* d_coo_col_ind; float* d_coo_val; HIP_CHECK(hipMalloc((void**)&d_coo_row_ind, sizeof(rocsparse_int) * nnz)); HIP_CHECK(hipMalloc((void**)&d_coo_col_ind, sizeof(rocsparse_int) * nnz)); HIP_CHECK(hipMalloc((void**)&d_coo_val, sizeof(float) * nnz)); // Convert the CSR row offsets into COO row indices ROCSPARSE_CHECK( rocsparse_csr2coo(handle, d_csr_row_ptr, nnz, m, d_coo_row_ind, rocsparse_index_base_zero)); // Copy the column and value arrays HIP_CHECK(hipMemcpy( d_coo_col_ind, d_csr_col_ind, sizeof(rocsparse_int) * nnz, hipMemcpyDeviceToDevice)); HIP_CHECK(hipMemcpy(d_coo_val, d_csr_val, sizeof(float) * nnz, hipMemcpyDeviceToDevice)); // Clean up HIP_CHECK(hipFree(d_csr_row_ptr)); HIP_CHECK(hipFree(d_csr_col_ind)); HIP_CHECK(hipFree(d_csr_val)); HIP_CHECK(hipFree(d_coo_row_ind)); HIP_CHECK(hipFree(d_coo_col_ind)); HIP_CHECK(hipFree(d_coo_val)); // Destroy rocSPARSE handle ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**m**–**[in]**number of rows of the sparse CSR matrix.**coo_row_ind**–**[out]**array of`nnz`

elements containing the row indices of the sparse COO matrix.**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`csr_row_ptr`

or`coo_row_ind`

pointer is invalid.**rocsparse_status_arch_mismatch**– the device is not supported.



## rocsparse_coo2csr()[#](#rocsparse-coo2csr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_coo2csr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_row_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base)[#](#_CPPv417rocsparse_coo2csr16rocsparse_handlePK13rocsparse_int13rocsparse_int13rocsparse_intP13rocsparse_int20rocsparse_index_base) Convert a sparse COO matrix into a sparse CSR matrix.

`rocsparse_coo2csr`

converts the COO array containing the row indices into a CSR array of row offsets that point to the start of every row. It is assumed that the COO row index array is sorted.`rocsparse_coo2csr`

can also be used, to convert a COO array containing the column indices into a CSC array of column offsets that point to the start of every column. In this case it is assumed that the COO column index array is sorted instead.**Example**This example converts a COO matrix into a CSR matrix.

int main() { // 1 2 0 3 0 // A = 0 4 5 0 0 // 6 0 0 7 8 rocsparse_int m = 3; rocsparse_int n = 5; rocsparse_int nnz = 8; std::vector<rocsparse_int> hcoo_row_ind = {0, 0, 0, 1, 1, 2, 2, 2}; std::vector<rocsparse_int> hcoo_col_ind = {0, 1, 3, 1, 2, 0, 3, 4}; std::vector<float> hcoo_val = {1, 2, 3, 4, 5, 6, 7, 8}; // Allocate COO matrix arrays rocsparse_int* dcoo_row_ind; rocsparse_int* dcoo_col_ind; float* dcoo_val; HIP_CHECK(hipMalloc(&dcoo_row_ind, sizeof(rocsparse_int) * nnz)); HIP_CHECK(hipMalloc(&dcoo_col_ind, sizeof(rocsparse_int) * nnz)); HIP_CHECK(hipMalloc(&dcoo_val, sizeof(float) * nnz)); HIP_CHECK(hipMemcpy( dcoo_row_ind, hcoo_row_ind.data(), sizeof(rocsparse_int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( dcoo_col_ind, hcoo_col_ind.data(), sizeof(rocsparse_int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcoo_val, hcoo_val.data(), sizeof(float) * nnz, hipMemcpyHostToDevice)); // Allocate CSR matrix arrays rocsparse_int* dcsr_row_ptr; rocsparse_int* dcsr_col_ind; float* dcsr_val; HIP_CHECK(hipMalloc(&dcsr_row_ptr, sizeof(rocsparse_int) * (m + 1))); HIP_CHECK(hipMalloc(&dcsr_col_ind, sizeof(rocsparse_int) * nnz)); HIP_CHECK(hipMalloc(&dcsr_val, sizeof(float) * nnz)); // Create rocsparse handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Convert the coo row indices into csr row offsets ROCSPARSE_CHECK( rocsparse_coo2csr(handle, dcoo_row_ind, nnz, m, dcsr_row_ptr, rocsparse_index_base_zero)); // Copy the column and value arrays HIP_CHECK(hipMemcpy( dcsr_col_ind, dcoo_col_ind, sizeof(rocsparse_int) * nnz, hipMemcpyDeviceToDevice)); HIP_CHECK(hipMemcpy(dcsr_val, dcoo_val, sizeof(float) * nnz, hipMemcpyDeviceToDevice)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); HIP_CHECK(hipFree(dcoo_row_ind)); HIP_CHECK(hipFree(dcoo_col_ind)); HIP_CHECK(hipFree(dcoo_val)); HIP_CHECK(hipFree(dcsr_row_ptr)); HIP_CHECK(hipFree(dcsr_col_ind)); HIP_CHECK(hipFree(dcsr_val)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**coo_row_ind**–**[in]**array of`nnz`

elements containing the row indices of the sparse COO matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**m**–**[in]**number of rows of the sparse CSR matrix.**csr_row_ptr**–**[out]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`coo_row_ind`

or`csr_row_ptr`

pointer is invalid.



## rocsparse_csr2csc_buffer_size()[#](#rocsparse-csr2csc-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_csr2csc_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_action](enumerations.html#_CPPv416rocsparse_action)copy_values, size_t *buffer_size)[#](#_CPPv429rocsparse_csr2csc_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPK13rocsparse_intPK13rocsparse_int16rocsparse_actionP6size_t) `rocsparse_csr2csc_buffer_size`

returns the size of the temporary storage buffer required by[rocsparse_Xcsr2csc()](#rocsparse__csr2csc_8h_1aa3e360d8361fe70c1cc22ff95bf544bc).Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix.**n**–**[in]**number of columns of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csr_col_ind**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**copy_values**–**[in]**[rocsparse_action_symbolic](enumerations.html#rocsparse-types_8h_1a1ec75a33f6cf43e19b2b4e254213c465a8e396adaad286c3fd887ace34ac95333)or[rocsparse_action_numeric](enumerations.html#rocsparse-types_8h_1a1ec75a33f6cf43e19b2b4e254213c465a87bdd4fa932567a61306494cc31759eb).**buffer_size**–**[out]**number of bytes of the temporary storage buffer required by[rocsparse_Xcsr2csc()](#rocsparse__csr2csc_8h_1aa3e360d8361fe70c1cc22ff95bf544bc).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`n`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`csr_row_ptr`

,`csr_col_ind`

or`buffer_size`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_csr2csc()[#](#rocsparse-csr2csc)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scsr2csc([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const float *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, float *csc_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_row_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_col_ptr,[rocsparse_action](enumerations.html#_CPPv416rocsparse_action)copy_values,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base, void *temp_buffer)[#](#_CPPv418rocsparse_scsr2csc16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_intPfP13rocsparse_intP13rocsparse_int16rocsparse_action20rocsparse_index_basePv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcsr2csc([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const double *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, double *csc_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_row_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_col_ptr,[rocsparse_action](enumerations.html#_CPPv416rocsparse_action)copy_values,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base, void *temp_buffer)[#](#_CPPv418rocsparse_dcsr2csc16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPKdPK13rocsparse_intPK13rocsparse_intPdP13rocsparse_intP13rocsparse_int16rocsparse_action20rocsparse_index_basePv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccsr2csc([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csc_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_row_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_col_ptr,[rocsparse_action](enumerations.html#_CPPv416rocsparse_action)copy_values,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base, void *temp_buffer)[#](#_CPPv418rocsparse_ccsr2csc16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_intP23rocsparse_float_complexP13rocsparse_intP13rocsparse_int16rocsparse_action20rocsparse_index_basePv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcsr2csc([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csc_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_row_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_col_ptr,[rocsparse_action](enumerations.html#_CPPv416rocsparse_action)copy_values,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base, void *temp_buffer)[#](#_CPPv418rocsparse_zcsr2csc16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_intP24rocsparse_double_complexP13rocsparse_intP13rocsparse_int16rocsparse_action20rocsparse_index_basePv) Convert a sparse CSR matrix into a sparse CSC matrix.

`rocsparse_csr2csc`

converts a CSR matrix into a CSC matrix. The resulting matrix can also be seen as the transpose of the input matrix.`rocsparse_csr2csc`

can also be used to convert a CSC matrix into a CSR matrix.The conversion of a sparse matrix from CSR to CSC format involves two steps. First, the user calls

[rocsparse_csr2csc_buffer_size](#rocsparse__csr2csc_8h_1ad724ad5a28d297b3f3f259d6d8c5057d)in order to determine the size of the required tempory storage buffer. The user then allocates this buffer. Secondly, the user calls`rocsparse_csr2csc`

to complete the conversion. Once the conversion is complete, the user must free the temporary buffer.Both

[rocsparse_csr2csc_buffer_size](#rocsparse__csr2csc_8h_1ad724ad5a28d297b3f3f259d6d8c5057d)and`rocsparse_csr2csc`

take a[rocsparse_action](enumerations.html#rocsparse-types_8h_1a1ec75a33f6cf43e19b2b4e254213c465)parameter as input. This`copy_values`

parameter decides whether`csc_row_ind`

and`csc_val`

are filled during conversion ([rocsparse_action_numeric](enumerations.html#rocsparse-types_8h_1a1ec75a33f6cf43e19b2b4e254213c465a87bdd4fa932567a61306494cc31759eb)) or whether only`csc_row_ind`

is filled ([rocsparse_action_symbolic](enumerations.html#rocsparse-types_8h_1a1ec75a33f6cf43e19b2b4e254213c465a8e396adaad286c3fd887ace34ac95333)). Using[rocsparse_action_symbolic](enumerations.html#rocsparse-types_8h_1a1ec75a33f6cf43e19b2b4e254213c465a8e396adaad286c3fd887ace34ac95333)is useful for example if only the sparsity pattern is required.**Example**This example computes the transpose of a CSR matrix.

// 1 2 0 3 0 // A = 0 4 5 0 0 // 6 0 0 7 8 rocsparse_int m_A = 3; rocsparse_int n_A = 5; rocsparse_int nnz_A = 8; csr_row_ptr_A[m_A + 1] = {0, 3, 5, 8}; // device memory csr_col_ind_A[nnz_A] = {0, 1, 3, 1, 2, 0, 3, 4}; // device memory csr_val_A[nnz_A] = {1, 2, 3, 4, 5, 6, 7, 8}; // device memory // Allocate memory for transposed CSR matrix rocsparse_int m_T = n_A; rocsparse_int n_T = m_A; rocsparse_int nnz_T = nnz_A; rocsparse_int* csr_row_ptr_T; rocsparse_int* csr_col_ind_T; float* csr_val_T; hipMalloc((void**)&csr_row_ptr_T, sizeof(rocsparse_int) * (m_T + 1)); hipMalloc((void**)&csr_col_ind_T, sizeof(rocsparse_int) * nnz_T); hipMalloc((void**)&csr_val_T, sizeof(float) * nnz_T); // Obtain the temporary buffer size size_t buffer_size; rocsparse_csr2csc_buffer_size(handle, m_A, n_A, nnz_A, csr_row_ptr_A, csr_col_ind_A, rocsparse_action_numeric, &buffer_size); // Allocate temporary buffer void* temp_buffer; hipMalloc(&temp_buffer, buffer_size); rocsparse_scsr2csc(handle, m_A, n_A, nnz_A, csr_val_A, csr_row_ptr_A, csr_col_ind_A, csr_val_T, csr_col_ind_T, csr_row_ptr_T, rocsparse_action_numeric, rocsparse_index_base_zero, temp_buffer);

**Example**This example computes the symbolic transpose of A

int main() { // Initialize rocSPARSE rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // 1 2 0 3 0 // A = 0 4 5 0 0 // 6 0 0 7 8 rocsparse_int m_A = 3; rocsparse_int n_A = 5; rocsparse_int nnz_A = 8; // Define host arrays rocsparse_int h_csr_row_ptr_A[] = {0, 3, 5, 8}; rocsparse_int h_csr_col_ind_A[] = {0, 1, 3, 1, 2, 0, 3, 4}; float h_csr_val_A[] = {1, 2, 3, 4, 5, 6, 7, 8}; // Allocate and initialize device memory for matrix A rocsparse_int* d_csr_row_ptr_A; rocsparse_int* d_csr_col_ind_A; float* d_csr_val_A; HIP_CHECK(hipMalloc((void**)&d_csr_row_ptr_A, sizeof(rocsparse_int) * (m_A + 1))); HIP_CHECK(hipMalloc((void**)&d_csr_col_ind_A, sizeof(rocsparse_int) * nnz_A)); HIP_CHECK(hipMalloc((void**)&d_csr_val_A, sizeof(float) * nnz_A)); HIP_CHECK(hipMemcpy(d_csr_row_ptr_A, h_csr_row_ptr_A, sizeof(rocsparse_int) * (m_A + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( d_csr_col_ind_A, h_csr_col_ind_A, sizeof(rocsparse_int) * nnz_A, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(d_csr_val_A, h_csr_val_A, sizeof(float) * nnz_A, hipMemcpyHostToDevice)); // Allocate memory for transposed CSR matrix rocsparse_int m_T = n_A; rocsparse_int n_T = m_A; rocsparse_int nnz_T = nnz_A; rocsparse_int* d_csr_row_ptr_T; rocsparse_int* d_csr_col_ind_T; float* d_csr_val_T; HIP_CHECK(hipMalloc((void**)&d_csr_row_ptr_T, sizeof(rocsparse_int) * (m_T + 1))); HIP_CHECK(hipMalloc((void**)&d_csr_col_ind_T, sizeof(rocsparse_int) * nnz_T)); HIP_CHECK(hipMalloc((void**)&d_csr_val_T, sizeof(float) * nnz_T)); // Obtain the temporary buffer size size_t buffer_size; ROCSPARSE_CHECK(rocsparse_csr2csc_buffer_size(handle, m_A, n_A, nnz_A, d_csr_row_ptr_A, d_csr_col_ind_A, rocsparse_action_numeric, &buffer_size)); void* temp_buffer; HIP_CHECK(hipMalloc(&temp_buffer, buffer_size)); // Perform the CSR to CSC conversion ROCSPARSE_CHECK(rocsparse_scsr2csc(handle, m_A, n_A, nnz_A, d_csr_val_A, d_csr_row_ptr_A, d_csr_col_ind_A, d_csr_val_T, d_csr_col_ind_T, d_csr_row_ptr_T, rocsparse_action_numeric, rocsparse_index_base_zero, temp_buffer)); // Clean up HIP_CHECK(hipFree(d_csr_row_ptr_A)); HIP_CHECK(hipFree(d_csr_col_ind_A)); HIP_CHECK(hipFree(d_csr_val_A)); HIP_CHECK(hipFree(d_csr_row_ptr_T)); HIP_CHECK(hipFree(d_csr_col_ind_T)); HIP_CHECK(hipFree(d_csr_val_T)); HIP_CHECK(hipFree(temp_buffer)); // Destroy rocSPARSE handle ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix.**n**–**[in]**number of columns of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**csr_val**–**[in]**array of`nnz`

elements of the sparse CSR matrix.**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csr_col_ind**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**csc_val**–**[out]**array of`nnz`

elements of the sparse CSC matrix.**csc_row_ind**–**[out]**array of`nnz`

elements containing the row indices of the sparse CSC matrix.**csc_col_ptr**–**[out]**array of`n+1`

elements that point to the start of every column of the sparse CSC matrix.**copy_values**–**[in]**[rocsparse_action_symbolic](enumerations.html#rocsparse-types_8h_1a1ec75a33f6cf43e19b2b4e254213c465a8e396adaad286c3fd887ace34ac95333)or[rocsparse_action_numeric](enumerations.html#rocsparse-types_8h_1a1ec75a33f6cf43e19b2b4e254213c465a87bdd4fa932567a61306494cc31759eb).**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**temp_buffer**–**[in]**temporary storage buffer allocated by the user, size is returned by[rocsparse_csr2csc_buffer_size()](#rocsparse__csr2csc_8h_1ad724ad5a28d297b3f3f259d6d8c5057d).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`n`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`csr_val`

,`csr_row_ptr`

,`csr_col_ind`

,`csc_val`

,`csc_row_ind`

,`csc_col_ptr`

or`temp_buffer`

pointer is invalid.**rocsparse_status_arch_mismatch**– the device is not supported.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_gebsr2gebsc_buffer_size()[#](#rocsparse-gebsr2gebsc-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sgebsr2gebsc_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const float *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, size_t *p_buffer_size)[#](#_CPPv434rocsparse_sgebsr2gebsc_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dgebsr2gebsc_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const double *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, size_t *p_buffer_size)[#](#_CPPv434rocsparse_dgebsr2gebsc_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPKdPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cgebsr2gebsc_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, size_t *p_buffer_size)[#](#_CPPv434rocsparse_cgebsr2gebsc_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zgebsr2gebsc_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, size_t *p_buffer_size)[#](#_CPPv434rocsparse_zgebsr2gebsc_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intP6size_t) `rocsparse_gebsr2gebsc_buffer_size`

returns the size of the temporary storage buffer required by[rocsparse_Xgebsr2gebsc()](#rocsparse__gebsr2gebsc_8h_1a1c6770406fa5d4b83bffd856ca1dcfbf). The temporary storage buffer must be allocated by the user.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**mb**–**[in]**number of rows of the sparse GEneral BSR matrix.**nb**–**[in]**number of columns of the sparse GEneral BSR matrix.**nnzb**–**[in]**number of non-zero entries of the sparse GEneral BSR matrix.**bsr_val**–**[in]**array of`nnzb*row_block_dim*col_block_dim`

containing the values of the sparse GEneral BSR matrix.**bsr_row_ptr**–**[in]**array of`mb+1`

elements that point to the start of every row of the sparse GEneral BSR matrix.**bsr_col_ind**–**[in]**array of`nnzb`

elements containing the column indices of the sparse GEneral BSR matrix.**row_block_dim**–**[in]**row size of the blocks in the sparse general BSR matrix.**col_block_dim**–**[in]**col size of the blocks in the sparse general BSR matrix.**p_buffer_size**–**[out]**number of bytes of the temporary storage buffer required by[rocsparse_sgebsr2gebsc()](#rocsparse__gebsr2gebsc_8h_1a1c6770406fa5d4b83bffd856ca1dcfbf),[rocsparse_dgebsr2gebsc()](#rocsparse__gebsr2gebsc_8h_1a4e28d858192b3ff729871163968a6e04),[rocsparse_cgebsr2gebsc()](#rocsparse__gebsr2gebsc_8h_1a5fb3db1d27816e19ed03511481fb3c52)and[rocsparse_zgebsr2gebsc()](#rocsparse__gebsr2gebsc_8h_1abd3fef9cd68abc3e65245cabf98bc578).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`mb`

,`nb`

or`nnzb`

is invalid.**rocsparse_status_invalid_pointer**–`bsr_row_ptr`

,`bsr_col_ind`

or`p_buffer_size`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_gebsr2gebsc()[#](#rocsparse-gebsr2gebsc)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sgebsr2gebsc([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const float *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, float *bsc_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsc_row_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsc_col_ptr,[rocsparse_action](enumerations.html#_CPPv416rocsparse_action)copy_values,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base, void *temp_buffer)[#](#_CPPv422rocsparse_sgebsr2gebsc16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intPfP13rocsparse_intP13rocsparse_int16rocsparse_action20rocsparse_index_basePv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dgebsr2gebsc([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const double *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, double *bsc_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsc_row_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsc_col_ptr,[rocsparse_action](enumerations.html#_CPPv416rocsparse_action)copy_values,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base, void *temp_buffer)[#](#_CPPv422rocsparse_dgebsr2gebsc16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPKdPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intPdP13rocsparse_intP13rocsparse_int16rocsparse_action20rocsparse_index_basePv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cgebsr2gebsc([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsc_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsc_row_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsc_col_ptr,[rocsparse_action](enumerations.html#_CPPv416rocsparse_action)copy_values,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base, void *temp_buffer)[#](#_CPPv422rocsparse_cgebsr2gebsc16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intP23rocsparse_float_complexP13rocsparse_intP13rocsparse_int16rocsparse_action20rocsparse_index_basePv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zgebsr2gebsc([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsc_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsc_row_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsc_col_ptr,[rocsparse_action](enumerations.html#_CPPv416rocsparse_action)copy_values,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base, void *temp_buffer)[#](#_CPPv422rocsparse_zgebsr2gebsc16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intP24rocsparse_double_complexP13rocsparse_intP13rocsparse_int16rocsparse_action20rocsparse_index_basePv) Convert a sparse GEneral BSR matrix into a sparse GEneral BSC matrix.

`rocsparse_gebsr2gebsc`

converts a GEneral BSR matrix into a GEneral BSC matrix. The resulting matrix can also be seen as the transpose of the input matrix.`rocsparse_gebsr2gebsc`

can also be used to convert a GEneral BSC matrix into a GEneral BSR matrix.The conversion of a sparse matrix from GEneral BSR to GEneral BSC format involves two steps. First, the user calls

[rocsparse_Xgebsr2gebsc_buffer_size()](#rocsparse__gebsr2gebsc_8h_1a2558f414e78e053a86f66cfab64ca539)in order to determine the size of the required tempory storage buffer. The user then allocates this buffer. Secondly, the user calls`rocsparse_gebsr2gebsc`

to complete the conversion. Once the conversion is complete, the user must free the temporary buffer.`rocsparse_gebsr2gebsc`

takes a[rocsparse_action](enumerations.html#rocsparse-types_8h_1a1ec75a33f6cf43e19b2b4e254213c465)parameter as input. This`copy_values`

parameter decides whether`bsc_row_ind`

and`bsc_val`

are filled during conversion ([rocsparse_action_numeric](enumerations.html#rocsparse-types_8h_1a1ec75a33f6cf43e19b2b4e254213c465a87bdd4fa932567a61306494cc31759eb)) or whether only`bsc_row_ind`

is filled ([rocsparse_action_symbolic](enumerations.html#rocsparse-types_8h_1a1ec75a33f6cf43e19b2b4e254213c465a8e396adaad286c3fd887ace34ac95333)). Using[rocsparse_action_symbolic](enumerations.html#rocsparse-types_8h_1a1ec75a33f6cf43e19b2b4e254213c465a8e396adaad286c3fd887ace34ac95333)is useful for example if only the sparsity pattern is required.**Example**This example computes the transpose of a GEneral BSR matrix.

int main() { // 1 2 0 3 // A = 0 4 5 0 // 6 0 0 7 // 1 2 3 4 rocsparse_int mb_A = 2; rocsparse_int nb_A = 2; rocsparse_int nnzb_A = 4; rocsparse_int row_block_dim = 2; rocsparse_int col_block_dim = 2; std::vector<rocsparse_int> hbsr_row_ptr_A = {0, 2, 4}; std::vector<rocsparse_int> hbsr_col_ind_A = {0, 1, 0, 1}; std::vector<float> hbsr_val_A = {1, 2, 0, 4, 0, 3, 5, 0, 6, 0, 1, 2, 0, 7, 3, 4}; rocsparse_int* dbsr_row_ptr_A = nullptr; rocsparse_int* dbsr_col_ind_A = nullptr; float* dbsr_val_A = nullptr; HIP_CHECK(hipMalloc((void**)&dbsr_row_ptr_A, sizeof(rocsparse_int) * (mb_A + 1))); HIP_CHECK(hipMalloc((void**)&dbsr_col_ind_A, sizeof(rocsparse_int) * nnzb_A)); HIP_CHECK( hipMalloc((void**)&dbsr_val_A, sizeof(float) * nnzb_A * row_block_dim * col_block_dim)); HIP_CHECK(hipMemcpy(dbsr_row_ptr_A, hbsr_row_ptr_A.data(), sizeof(rocsparse_int) * (mb_A + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dbsr_col_ind_A, hbsr_col_ind_A.data(), sizeof(rocsparse_int) * nnzb_A, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dbsr_val_A, hbsr_val_A.data(), sizeof(float) * nnzb_A * row_block_dim * col_block_dim, hipMemcpyHostToDevice)); // Allocate memory for transposed BSR matrix rocsparse_int mb_T = nb_A; rocsparse_int nb_T = mb_A; rocsparse_int nnzb_T = nnzb_A; rocsparse_int* dbsr_row_ptr_T = nullptr; rocsparse_int* dbsr_col_ind_T = nullptr; float* dbsr_val_T = nullptr; HIP_CHECK(hipMalloc((void**)&dbsr_row_ptr_T, sizeof(rocsparse_int) * (mb_T + 1))); HIP_CHECK(hipMalloc((void**)&dbsr_col_ind_T, sizeof(rocsparse_int) * nnzb_T)); HIP_CHECK( hipMalloc((void**)&dbsr_val_T, sizeof(float) * nnzb_A * row_block_dim * col_block_dim)); rocsparse_handle handle; rocsparse_create_handle(&handle); // Obtain the temporary buffer size size_t buffer_size; ROCSPARSE_CHECK(rocsparse_sgebsr2gebsc_buffer_size(handle, mb_A, nb_A, nnzb_A, dbsr_val_A, dbsr_row_ptr_A, dbsr_col_ind_A, row_block_dim, col_block_dim, &buffer_size)); // Allocate temporary buffer void* temp_buffer; HIP_CHECK(hipMalloc(&temp_buffer, buffer_size)); ROCSPARSE_CHECK(rocsparse_sgebsr2gebsc(handle, mb_A, nb_A, nnzb_A, dbsr_val_A, dbsr_row_ptr_A, dbsr_col_ind_A, row_block_dim, col_block_dim, dbsr_val_T, dbsr_col_ind_T, dbsr_row_ptr_T, rocsparse_action_numeric, rocsparse_index_base_zero, temp_buffer)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); HIP_CHECK(hipFree(temp_buffer)); HIP_CHECK(hipFree(dbsr_row_ptr_A)); HIP_CHECK(hipFree(dbsr_col_ind_A)); HIP_CHECK(hipFree(dbsr_val_A)); HIP_CHECK(hipFree(dbsr_row_ptr_T)); HIP_CHECK(hipFree(dbsr_col_ind_T)); HIP_CHECK(hipFree(dbsr_val_T)); return 0; }


Note

The resulting matrix can also be seen as the transpose of the input matrix.

Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**mb**–**[in]**number of rows of the sparse GEneral BSR matrix.**nb**–**[in]**number of columns of the sparse GEneral BSR matrix.**nnzb**–**[in]**number of non-zero entries of the sparse GEneral BSR matrix.**bsr_val**–**[in]**array of`nnzb`

*`row_block_dim`

*`col_block_dim`

elements of the sparse GEneral BSR matrix.**bsr_row_ptr**–**[in]**array of`mb+1`

elements that point to the start of every row of the sparse GEneral BSR matrix.**bsr_col_ind**–**[in]**array of`nnz`

elements containing the column indices of the sparse GEneral BSR matrix.**row_block_dim**–**[in]**row size of the blocks in the sparse general BSR matrix.**col_block_dim**–**[in]**col size of the blocks in the sparse general BSR matrix.**bsc_val**–**[out]**array of`nnz`

elements of the sparse BSC matrix.**bsc_row_ind**–**[out]**array of`nnz`

elements containing the row indices of the sparse BSC matrix.**bsc_col_ptr**–**[out]**array of`nb+1`

elements that point to the start of every column of the sparse BSC matrix.**copy_values**–**[in]**[rocsparse_action_symbolic](enumerations.html#rocsparse-types_8h_1a1ec75a33f6cf43e19b2b4e254213c465a8e396adaad286c3fd887ace34ac95333)or[rocsparse_action_numeric](enumerations.html#rocsparse-types_8h_1a1ec75a33f6cf43e19b2b4e254213c465a87bdd4fa932567a61306494cc31759eb).**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**temp_buffer**–**[in]**temporary storage buffer allocated by the user, size is returned by[rocsparse_Xgebsr2gebsc_buffer_size()](#rocsparse__gebsr2gebsc_8h_1a2558f414e78e053a86f66cfab64ca539).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`mb`

,`nb`

or`nnzb`

is invalid.**rocsparse_status_invalid_pointer**–`bsr_val`

,`bsr_row_ptr`

,`bsr_col_ind`

,`bsc_val`

,`bsc_row_ind`

,`bsc_col_ptr`

or`temp_buffer`

pointer is invalid.**rocsparse_status_arch_mismatch**– the device is not supported.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_csr2ell_width()[#](#rocsparse-csr2ell-width)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_csr2ell_width([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)ell_descr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*ell_width)[#](#_CPPv423rocsparse_csr2ell_width16rocsparse_handle13rocsparse_intK19rocsparse_mat_descrPK13rocsparse_intK19rocsparse_mat_descrP13rocsparse_int) `rocsparse_csr2ell_width`

computes the maximum of the per row non-zero elements over all rows, the`ell_width`

, for a given CSR matrix.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix.**csr_descr**–**[in]**descriptor of the sparse CSR matrix. Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**ell_descr**–**[in]**descriptor of the sparse ELL matrix. Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**ell_width**–**[out]**pointer to the number of non-zero elements per row in ELL storage format.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

is invalid.**rocsparse_status_invalid_pointer**–`csr_descr`

,`csr_row_ptr`

, or`ell_width`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_not_implemented**–[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_csr2ell()[#](#rocsparse-csr2ell)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scsr2ell([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr, const float *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)ell_descr,[rocsparse_int](types.html#_CPPv413rocsparse_int)ell_width, float *ell_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*ell_col_ind)[#](#_CPPv418rocsparse_scsr2ell16rocsparse_handle13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPfP13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcsr2ell([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr, const double *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)ell_descr,[rocsparse_int](types.html#_CPPv413rocsparse_int)ell_width, double *ell_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*ell_col_ind)[#](#_CPPv418rocsparse_dcsr2ell16rocsparse_handle13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPdP13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccsr2ell([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)ell_descr,[rocsparse_int](types.html#_CPPv413rocsparse_int)ell_width,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*ell_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*ell_col_ind)[#](#_CPPv418rocsparse_ccsr2ell16rocsparse_handle13rocsparse_intK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intP23rocsparse_float_complexP13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcsr2ell([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)ell_descr,[rocsparse_int](types.html#_CPPv413rocsparse_int)ell_width,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*ell_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*ell_col_ind)[#](#_CPPv418rocsparse_zcsr2ell16rocsparse_handle13rocsparse_intK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intP24rocsparse_double_complexP13rocsparse_int) Convert a sparse CSR matrix into a sparse ELL matrix.

`rocsparse_csr2ell`

converts a CSR matrix into an ELL matrix. It is assumed, that`ell_val`

and`ell_col_ind`

are allocated. Allocation size is computed by the number of rows times the number of ELL non-zero elements per row, such that \(\text{nnz}_{\text{ELL}} = m \cdot \text{ell_width}\). The number of ELL non-zero elements per row is obtained by[rocsparse_csr2ell_width()](#rocsparse__csr2ell_8h_1a69bd3b583a009ebc1254516afcc724cd).**Example**This example converts a CSR matrix into an ELL matrix.

int main() { // Initialize rocSPARSE rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // 1 2 0 3 0 // A = 0 4 5 0 0 // 6 0 0 7 8 rocsparse_int m = 3; rocsparse_int n = 5; rocsparse_int nnz = 8; // Define host arrays rocsparse_int h_csr_row_ptr[] = {0, 3, 5, 8}; rocsparse_int h_csr_col_ind[] = {0, 1, 3, 1, 2, 0, 3, 4}; float h_csr_val[] = {1, 2, 3, 4, 5, 6, 7, 8}; // Allocate and initialize device memory for CSR matrix rocsparse_int* d_csr_row_ptr; rocsparse_int* d_csr_col_ind; float* d_csr_val; HIP_CHECK(hipMalloc((void**)&d_csr_row_ptr, sizeof(rocsparse_int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&d_csr_col_ind, sizeof(rocsparse_int) * nnz)); HIP_CHECK(hipMalloc((void**)&d_csr_val, sizeof(float) * nnz)); HIP_CHECK(hipMemcpy( d_csr_row_ptr, h_csr_row_ptr, sizeof(rocsparse_int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( d_csr_col_ind, h_csr_col_ind, sizeof(rocsparse_int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(d_csr_val, h_csr_val, sizeof(float) * nnz, hipMemcpyHostToDevice)); // Create CSR matrix descriptor rocsparse_mat_descr csr_descr; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&csr_descr)); // Create ELL matrix descriptor rocsparse_mat_descr ell_descr; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&ell_descr)); // Obtain the ELL width rocsparse_int ell_width; ROCSPARSE_CHECK( rocsparse_csr2ell_width(handle, m, csr_descr, d_csr_row_ptr, ell_descr, &ell_width)); // Compute ELL non-zero entries rocsparse_int ell_nnz = m * ell_width; // Allocate ELL column and value arrays rocsparse_int* d_ell_col_ind; float* d_ell_val; HIP_CHECK(hipMalloc((void**)&d_ell_col_ind, sizeof(rocsparse_int) * ell_nnz)); HIP_CHECK(hipMalloc((void**)&d_ell_val, sizeof(float) * ell_nnz)); // Format conversion ROCSPARSE_CHECK(rocsparse_scsr2ell(handle, m, csr_descr, d_csr_val, d_csr_row_ptr, d_csr_col_ind, ell_descr, ell_width, d_ell_val, d_ell_col_ind)); // Clean up HIP_CHECK(hipFree(d_csr_row_ptr)); HIP_CHECK(hipFree(d_csr_col_ind)); HIP_CHECK(hipFree(d_csr_val)); HIP_CHECK(hipFree(d_ell_col_ind)); HIP_CHECK(hipFree(d_ell_val)); // Destroy matrix descriptors and rocSPARSE handle ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(csr_descr)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(ell_descr)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix.**csr_descr**–**[in]**descriptor of the sparse CSR matrix. Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**csr_val**–**[in]**array containing the values of the sparse CSR matrix.**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csr_col_ind**–**[in]**array containing the column indices of the sparse CSR matrix.**ell_descr**–**[in]**descriptor of the sparse ELL matrix. Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**ell_width**–**[in]**number of non-zero elements per row in ELL storage format.**ell_val**–**[out]**array of`m`

times`ell_width`

elements of the sparse ELL matrix.**ell_col_ind**–**[out]**array of`m`

times`ell_width`

elements containing the column indices of the sparse ELL matrix.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`ell_width`

is invalid.**rocsparse_status_invalid_pointer**–`csr_descr`

,`csr_val`

,`csr_row_ptr`

,`csr_col_ind`

,`ell_descr`

,`ell_val`

or`ell_col_ind`

pointer is invalid.**rocsparse_status_not_implemented**–[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_ell2csr_nnz()[#](#rocsparse-ell2csr-nnz)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ell2csr_nnz([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)ell_descr,[rocsparse_int](types.html#_CPPv413rocsparse_int)ell_width, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*ell_col_ind, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_nnz)[#](#_CPPv421rocsparse_ell2csr_nnz16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descrP13rocsparse_intP13rocsparse_int) This function takes a sparse ELL matrix as input and computes the row offset array,

`csr_row_ptr`

, and the total number of nonzeros,`csr_nnz`

, that will result from converting the ELL format input matrix to a CSR format output matrix. This function is the first step in the conversion and is used in conjunction with[rocsparse_Xell2csr()](#rocsparse__ell2csr_8h_1abbc4cd79b7ba99f3a59847f9ad6b1144). It is assumed that`csr_row_ptr`

has been allocated with size`m+1`

.Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the sparse ELL matrix.**n**–**[in]**number of columns of the sparse ELL matrix.**ell_descr**–**[in]**descriptor of the sparse ELL matrix. Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**ell_width**–**[in]**number of non-zero elements per row in ELL storage format.**ell_col_ind**–**[in]**array of`m`

times`ell_width`

elements containing the column indices of the sparse ELL matrix.**csr_descr**–**[in]**descriptor of the sparse CSR matrix. Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**csr_row_ptr**–**[out]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csr_nnz**–**[out]**pointer to the total number of non-zero elements in CSR storage format.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`n`

or`ell_width`

is invalid.**rocsparse_status_invalid_pointer**–`ell_descr`

,`ell_col_ind`

,`csr_descr`

,`csr_row_ptr`

or`csr_nnz`

pointer is invalid.**rocsparse_status_not_implemented**–[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_ell2csr()[#](#rocsparse-ell2csr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sell2csr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)ell_descr,[rocsparse_int](types.html#_CPPv413rocsparse_int)ell_width, const float *ell_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*ell_col_ind, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr, float *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind)[#](#_CPPv418rocsparse_sell2csr16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPKfPK13rocsparse_intK19rocsparse_mat_descrPfPK13rocsparse_intP13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dell2csr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)ell_descr,[rocsparse_int](types.html#_CPPv413rocsparse_int)ell_width, const double *ell_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*ell_col_ind, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr, double *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind)[#](#_CPPv418rocsparse_dell2csr16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPKdPK13rocsparse_intK19rocsparse_mat_descrPdPK13rocsparse_intP13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cell2csr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)ell_descr,[rocsparse_int](types.html#_CPPv413rocsparse_int)ell_width, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*ell_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*ell_col_ind, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind)[#](#_CPPv418rocsparse_cell2csr16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK23rocsparse_float_complexPK13rocsparse_intK19rocsparse_mat_descrP23rocsparse_float_complexPK13rocsparse_intP13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zell2csr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)ell_descr,[rocsparse_int](types.html#_CPPv413rocsparse_int)ell_width, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*ell_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*ell_col_ind, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind)[#](#_CPPv418rocsparse_zell2csr16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK24rocsparse_double_complexPK13rocsparse_intK19rocsparse_mat_descrP24rocsparse_double_complexPK13rocsparse_intP13rocsparse_int) Convert a sparse ELL matrix into a sparse CSR matrix.

`rocsparse_ell2csr`

converts a ELL matrix into a CSR matrix. It is assumed that`csr_row_ptr`

has already been filled and that`csr_val`

and`csr_col_ind`

are allocated by the user. Allocation size for`csr_row_ptr`

is computed as`m+1`

. Allocation size for`csr_val`

and`csr_col_ind`

is computed using[rocsparse_ell2csr_nnz()](#rocsparse__ell2csr_8h_1a1b4888c724e8b3bcbcc11cdeb2ce1806)which also fills in`csr_row_ptr`

.**Example**This example converts an ELL matrix into a CSR matrix.

int main() { // 1 2 0 3 0 // A = 0 4 5 0 0 // 6 0 0 7 8 rocsparse_int m = 3; rocsparse_int n = 5; rocsparse_int nnz = 8; rocsparse_int ell_width = 3; std::vector<rocsparse_int> hell_col_ind = {0, 1, 0, 1, 2, 3, 3, -1, 4}; std::vector<float> hell_val = {1, 4, 6, 2, 5, 7, 3, 0, 8}; rocsparse_int* dell_col_ind = nullptr; float* dell_val = nullptr; HIP_CHECK(hipMalloc((void**)&dell_col_ind, sizeof(rocsparse_int) * m * ell_width)); HIP_CHECK(hipMalloc((void**)&dell_val, sizeof(float) * m * ell_width)); HIP_CHECK(hipMemcpy(dell_col_ind, hell_col_ind.data(), sizeof(rocsparse_int) * m * ell_width, hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dell_val, hell_val.data(), sizeof(float) * m * ell_width, hipMemcpyHostToDevice)); rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Create ELL matrix descriptor rocsparse_mat_descr ell_descr; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&ell_descr)); // Create CSR matrix descriptor rocsparse_mat_descr csr_descr; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&csr_descr)); // Allocate csr_row_ptr array for row offsets rocsparse_int* dcsr_row_ptr; HIP_CHECK(hipMalloc((void**)&dcsr_row_ptr, sizeof(rocsparse_int) * (m + 1))); // Obtain the number of CSR non-zero entries // and fill csr_row_ptr array with row offsets rocsparse_int csr_nnz; ROCSPARSE_CHECK(rocsparse_ell2csr_nnz( handle, m, n, ell_descr, ell_width, dell_col_ind, csr_descr, dcsr_row_ptr, &csr_nnz)); // Allocate CSR column and value arrays rocsparse_int* dcsr_col_ind = nullptr; float* dcsr_val = nullptr; HIP_CHECK(hipMalloc((void**)&dcsr_col_ind, sizeof(rocsparse_int) * csr_nnz)); HIP_CHECK(hipMalloc((void**)&dcsr_val, sizeof(float) * csr_nnz)); // Format conversion ROCSPARSE_CHECK(rocsparse_sell2csr(handle, m, n, ell_descr, ell_width, dell_val, dell_col_ind, csr_descr, dcsr_val, dcsr_row_ptr, dcsr_col_ind)); HIP_CHECK(hipFree(dell_col_ind)); HIP_CHECK(hipFree(dell_val)); HIP_CHECK(hipFree(dcsr_row_ptr)); HIP_CHECK(hipFree(dcsr_col_ind)); HIP_CHECK(hipFree(dcsr_val)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(ell_descr)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(csr_descr)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the sparse ELL matrix.**n**–**[in]**number of columns of the sparse ELL matrix.**ell_descr**–**[in]**descriptor of the sparse ELL matrix. Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**ell_width**–**[in]**number of non-zero elements per row in ELL storage format.**ell_val**–**[in]**array of`m`

times`ell_width`

elements of the sparse ELL matrix.**ell_col_ind**–**[in]**array of`m`

times`ell_width`

elements containing the column indices of the sparse ELL matrix.**csr_descr**–**[in]**descriptor of the sparse CSR matrix. Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**csr_val**–**[out]**array containing the values of the sparse CSR matrix.**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csr_col_ind**–**[out]**array containing the column indices of the sparse CSR matrix.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`n`

or`ell_width`

is invalid.**rocsparse_status_invalid_pointer**–`csr_descr`

,`csr_val`

,`csr_row_ptr`

,`csr_col_ind`

,`ell_descr`

,`ell_val`

or`ell_col_ind`

pointer is invalid.**rocsparse_status_not_implemented**–[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_csr2hyb()[#](#rocsparse-csr2hyb)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scsr2hyb([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_hyb_mat](types.html#_CPPv417rocsparse_hyb_mat)hyb,[rocsparse_int](types.html#_CPPv413rocsparse_int)user_ell_width,[rocsparse_hyb_partition](enumerations.html#_CPPv423rocsparse_hyb_partition)partition_type)[#](#_CPPv418rocsparse_scsr2hyb16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int17rocsparse_hyb_mat13rocsparse_int23rocsparse_hyb_partition)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcsr2hyb([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_hyb_mat](types.html#_CPPv417rocsparse_hyb_mat)hyb,[rocsparse_int](types.html#_CPPv413rocsparse_int)user_ell_width,[rocsparse_hyb_partition](enumerations.html#_CPPv423rocsparse_hyb_partition)partition_type)[#](#_CPPv418rocsparse_dcsr2hyb16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_int17rocsparse_hyb_mat13rocsparse_int23rocsparse_hyb_partition)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccsr2hyb([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_hyb_mat](types.html#_CPPv417rocsparse_hyb_mat)hyb,[rocsparse_int](types.html#_CPPv413rocsparse_int)user_ell_width,[rocsparse_hyb_partition](enumerations.html#_CPPv423rocsparse_hyb_partition)partition_type)[#](#_CPPv418rocsparse_ccsr2hyb16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int17rocsparse_hyb_mat13rocsparse_int23rocsparse_hyb_partition)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcsr2hyb([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_hyb_mat](types.html#_CPPv417rocsparse_hyb_mat)hyb,[rocsparse_int](types.html#_CPPv413rocsparse_int)user_ell_width,[rocsparse_hyb_partition](enumerations.html#_CPPv423rocsparse_hyb_partition)partition_type)[#](#_CPPv418rocsparse_zcsr2hyb16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int17rocsparse_hyb_mat13rocsparse_int23rocsparse_hyb_partition) Convert a sparse CSR matrix into a sparse HYB matrix.

`rocsparse_csr2hyb`

converts a CSR matrix into a HYB matrix. It is assumed that`hyb`

has been initialized with[rocsparse_create_hyb_mat()](auxiliary.html#rocsparse-auxiliary_8h_1a0b8464ef21c90b80ad8c870bf0a66ce0).**Example**This example converts a CSR matrix into a HYB matrix using user defined partitioning.

int main() { // 1 2 3 4 0 0 // A = 3 4 0 0 0 0 // 6 5 3 4 0 0 // 1 2 0 0 0 0 rocsparse_int m = 4; rocsparse_int n = 6; rocsparse_int nnz = 12; std::vector<rocsparse_int> hcsr_row_ptr = {0, 4, 6, 10, 12}; std::vector<rocsparse_int> hcsr_col_ind = {0, 1, 2, 3, 0, 1, 0, 1, 2, 3, 0, 1}; std::vector<float> hcsr_val = {1, 2, 3, 4, 3, 4, 6, 5, 3, 4, 1, 2}; rocsparse_int* dcsr_row_ptr = nullptr; rocsparse_int* dcsr_col_ind = nullptr; float* dcsr_val = nullptr; HIP_CHECK(hipMalloc((void**)&dcsr_row_ptr, sizeof(rocsparse_int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&dcsr_col_ind, sizeof(rocsparse_int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcsr_val, sizeof(float) * nnz)); HIP_CHECK(hipMemcpy( dcsr_row_ptr, hcsr_row_ptr.data(), sizeof(rocsparse_int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( dcsr_col_ind, hcsr_col_ind.data(), sizeof(rocsparse_int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsr_val, hcsr_val.data(), sizeof(float) * nnz, hipMemcpyHostToDevice)); rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); rocsparse_mat_descr descr; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr)); rocsparse_hyb_mat hyb; ROCSPARSE_CHECK(rocsparse_create_hyb_mat(&hyb)); rocsparse_int user_ell_width = 3; rocsparse_hyb_partition partition_type = rocsparse_hyb_partition_user; ROCSPARSE_CHECK(rocsparse_scsr2hyb(handle, m, n, descr, dcsr_val, dcsr_row_ptr, dcsr_col_ind, hyb, user_ell_width, partition_type)); rocsparse_int* dcsr_row_ptr2 = nullptr; rocsparse_int* dcsr_col_ind2 = nullptr; float* dcsr_val2 = nullptr; HIP_CHECK(hipMalloc((void**)&dcsr_row_ptr2, sizeof(rocsparse_int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&dcsr_col_ind2, sizeof(rocsparse_int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcsr_val2, sizeof(float) * nnz)); // Obtain the temporary buffer size size_t buffer_size; ROCSPARSE_CHECK(rocsparse_hyb2csr_buffer_size(handle, descr, hyb, dcsr_row_ptr2, &buffer_size)); // Allocate temporary buffer void* temp_buffer; HIP_CHECK(hipMalloc(&temp_buffer, buffer_size)); ROCSPARSE_CHECK(rocsparse_shyb2csr( handle, descr, hyb, dcsr_val2, dcsr_row_ptr2, dcsr_col_ind2, temp_buffer)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr)); ROCSPARSE_CHECK(rocsparse_destroy_hyb_mat(hyb)); HIP_CHECK(hipFree(temp_buffer)); HIP_CHECK(hipFree(dcsr_row_ptr)); HIP_CHECK(hipFree(dcsr_col_ind)); HIP_CHECK(hipFree(dcsr_val)); HIP_CHECK(hipFree(dcsr_row_ptr2)); HIP_CHECK(hipFree(dcsr_col_ind2)); HIP_CHECK(hipFree(dcsr_val2)); return 0; }


Note

This function requires a significant amount of storage for the HYB matrix, depending on the matrix structure.

Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix.**n**–**[in]**number of columns of the sparse CSR matrix.**descr**–**[in]**descriptor of the sparse CSR matrix. Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**csr_val**–**[in]**array containing the values of the sparse CSR matrix.**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csr_col_ind**–**[in]**array containing the column indices of the sparse CSR matrix.**hyb**–**[out]**sparse matrix in HYB format.**user_ell_width**–**[in]**width of the ELL part of the HYB matrix (only required if`partition_type`

==[rocsparse_hyb_partition_user](enumerations.html#rocsparse-types_8h_1a756fd5aab6f202ce45cbf151fc1a46a6a1fab46e61eb120731fcce2f3a0ddc85e)).**partition_type**–**[in]**[rocsparse_hyb_partition_auto](enumerations.html#rocsparse-types_8h_1a756fd5aab6f202ce45cbf151fc1a46a6a16c98963b39ca0f7c300531b418455b1)(recommended),[rocsparse_hyb_partition_user](enumerations.html#rocsparse-types_8h_1a756fd5aab6f202ce45cbf151fc1a46a6a1fab46e61eb120731fcce2f3a0ddc85e)or[rocsparse_hyb_partition_max](enumerations.html#rocsparse-types_8h_1a756fd5aab6f202ce45cbf151fc1a46a6a35eb173683e0cc9ed5a0e4bf083e17a4).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`n`

or`user_ell_width`

is invalid.**rocsparse_status_invalid_value**–`partition_type`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`hyb`

,`csr_val`

,`csr_row_ptr`

or`csr_col_ind`

pointer is invalid.**rocsparse_status_memory_error**– the buffer for the HYB matrix could not be allocated.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_not_implemented**–[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_hyb2csr_buffer_size()[#](#rocsparse-hyb2csr-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_hyb2csr_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_hyb_mat](types.html#_CPPv417rocsparse_hyb_mat)hyb, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, size_t *buffer_size)[#](#_CPPv429rocsparse_hyb2csr_buffer_size16rocsparse_handleK19rocsparse_mat_descrK17rocsparse_hyb_matPK13rocsparse_intP6size_t) `rocsparse_hyb2csr_buffer_size`

returns the size of the temporary storage buffer required by[rocsparse_Xhyb2csr()](#rocsparse__hyb2csr_8h_1a6e0f53adbeeb4455bdc5f6f35a6f3978). The temporary storage buffer must be allocated by the user.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**descr**–**[in]**descriptor of the sparse HYB matrix. Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**hyb**–**[in]**sparse matrix in HYB format.**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**buffer_size**–**[out]**number of bytes of the temporary storage buffer required by[rocsparse_Xhyb2csr()](#rocsparse__hyb2csr_8h_1a6e0f53adbeeb4455bdc5f6f35a6f3978).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`descr`

,`hyb`

,`csr_row_ptr`

or`buffer_size`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_not_implemented**–[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_hyb2csr()[#](#rocsparse-hyb2csr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_shyb2csr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_hyb_mat](types.html#_CPPv417rocsparse_hyb_mat)hyb, float *csr_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, void *temp_buffer)[#](#_CPPv418rocsparse_shyb2csr16rocsparse_handleK19rocsparse_mat_descrK17rocsparse_hyb_matPfP13rocsparse_intP13rocsparse_intPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dhyb2csr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_hyb_mat](types.html#_CPPv417rocsparse_hyb_mat)hyb, double *csr_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, void *temp_buffer)[#](#_CPPv418rocsparse_dhyb2csr16rocsparse_handleK19rocsparse_mat_descrK17rocsparse_hyb_matPdP13rocsparse_intP13rocsparse_intPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_chyb2csr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_hyb_mat](types.html#_CPPv417rocsparse_hyb_mat)hyb,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, void *temp_buffer)[#](#_CPPv418rocsparse_chyb2csr16rocsparse_handleK19rocsparse_mat_descrK17rocsparse_hyb_matP23rocsparse_float_complexP13rocsparse_intP13rocsparse_intPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zhyb2csr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_hyb_mat](types.html#_CPPv417rocsparse_hyb_mat)hyb,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, void *temp_buffer)[#](#_CPPv418rocsparse_zhyb2csr16rocsparse_handleK19rocsparse_mat_descrK17rocsparse_hyb_matP24rocsparse_double_complexP13rocsparse_intP13rocsparse_intPv) Convert a sparse HYB matrix into a sparse CSR matrix.

`rocsparse_hyb2csr`

converts a HYB matrix into a CSR matrix. This requires a HYB input structure,[rocsparse_hyb_mat](types.html#rocsparse-types_8h_1a919d9ad6075d1abf3cd007f13cbb4ddb), which is created using[rocsparse_create_hyb_mat](auxiliary.html#rocsparse-auxiliary_8h_1a0b8464ef21c90b80ad8c870bf0a66ce0)and is filled with data using the conversion routine[rocsparse_Xcsr2hyb()](#rocsparse__csr2hyb_8h_1af7847f79a1a545ab6284c1e5a73464cf).Converting back to a sparse CSR matrix from a sparse HYB matrix requires two steps. First, the user calls

[rocsparse_hyb2csr_buffer_size](#rocsparse__hyb2csr_8h_1a14ec7cc0d59fc97c56bcaa4235934604)in order to determine the size of the required temporary storage buffer. Once this is determined, the user allocates this buffer. Finally, the user calls[rocsparse_Xhyb2csr()](#rocsparse__hyb2csr_8h_1a6e0f53adbeeb4455bdc5f6f35a6f3978)to complete the conversion.**Example**This example converts a HYB matrix into a CSR matrix.

int main() { // 1 2 3 4 0 0 // A = 3 4 0 0 0 0 // 6 5 3 4 0 0 // 1 2 0 0 0 0 rocsparse_int m = 4; rocsparse_int n = 6; rocsparse_int nnz = 12; std::vector<rocsparse_int> hcsr_row_ptr = {0, 4, 6, 10, 12}; std::vector<rocsparse_int> hcsr_col_ind = {0, 1, 2, 3, 0, 1, 0, 1, 2, 3, 0, 1}; std::vector<float> hcsr_val = {1, 2, 3, 4, 3, 4, 6, 5, 3, 4, 1, 2}; rocsparse_int* dcsr_row_ptr = nullptr; rocsparse_int* dcsr_col_ind = nullptr; float* dcsr_val = nullptr; HIP_CHECK(hipMalloc((void**)&dcsr_row_ptr, sizeof(rocsparse_int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&dcsr_col_ind, sizeof(rocsparse_int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcsr_val, sizeof(float) * nnz)); HIP_CHECK(hipMemcpy( dcsr_row_ptr, hcsr_row_ptr.data(), sizeof(rocsparse_int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( dcsr_col_ind, hcsr_col_ind.data(), sizeof(rocsparse_int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsr_val, hcsr_val.data(), sizeof(float) * nnz, hipMemcpyHostToDevice)); rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); rocsparse_mat_descr descr; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr)); rocsparse_hyb_mat hyb; ROCSPARSE_CHECK(rocsparse_create_hyb_mat(&hyb)); rocsparse_int user_ell_width = 3; rocsparse_hyb_partition partition_type = rocsparse_hyb_partition_user; ROCSPARSE_CHECK(rocsparse_scsr2hyb(handle, m, n, descr, dcsr_val, dcsr_row_ptr, dcsr_col_ind, hyb, user_ell_width, partition_type)); rocsparse_int* dcsr_row_ptr2 = nullptr; rocsparse_int* dcsr_col_ind2 = nullptr; float* dcsr_val2 = nullptr; HIP_CHECK(hipMalloc((void**)&dcsr_row_ptr2, sizeof(rocsparse_int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&dcsr_col_ind2, sizeof(rocsparse_int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcsr_val2, sizeof(float) * nnz)); // Obtain the temporary buffer size size_t buffer_size; ROCSPARSE_CHECK(rocsparse_hyb2csr_buffer_size(handle, descr, hyb, dcsr_row_ptr2, &buffer_size)); // Allocate temporary buffer void* temp_buffer; HIP_CHECK(hipMalloc(&temp_buffer, buffer_size)); ROCSPARSE_CHECK(rocsparse_shyb2csr( handle, descr, hyb, dcsr_val2, dcsr_row_ptr2, dcsr_col_ind2, temp_buffer)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr)); ROCSPARSE_CHECK(rocsparse_destroy_hyb_mat(hyb)); HIP_CHECK(hipFree(temp_buffer)); HIP_CHECK(hipFree(dcsr_row_ptr)); HIP_CHECK(hipFree(dcsr_col_ind)); HIP_CHECK(hipFree(dcsr_val)); HIP_CHECK(hipFree(dcsr_row_ptr2)); HIP_CHECK(hipFree(dcsr_col_ind2)); HIP_CHECK(hipFree(dcsr_val2)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**descr**–**[in]**descriptor of the sparse HYB matrix. Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**hyb**–**[in]**sparse matrix in HYB format.**csr_val**–**[out]**array containing the values of the sparse CSR matrix.**csr_row_ptr**–**[out]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csr_col_ind**–**[out]**array containing the column indices of the sparse CSR matrix.**temp_buffer**–**[in]**temporary storage buffer allocated by the user, size is returned by[rocsparse_hyb2csr_buffer_size()](#rocsparse__hyb2csr_8h_1a14ec7cc0d59fc97c56bcaa4235934604).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`descr`

,`hyb`

,`csr_val`

,`csr_row_ptr`

,`csr_col_ind`

or`temp_buffer`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_not_implemented**–[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_bsr2csr()[#](#rocsparse-bsr2csr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sbsr2csr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)bsr_descr, const float *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr, float *csr_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind)[#](#_CPPv418rocsparse_sbsr2csr16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPfP13rocsparse_intP13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dbsr2csr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)bsr_descr, const double *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr, double *csr_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind)[#](#_CPPv418rocsparse_dbsr2csr16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPdP13rocsparse_intP13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cbsr2csr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)bsr_descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind)[#](#_CPPv418rocsparse_cbsr2csr16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_intK19rocsparse_mat_descrP23rocsparse_float_complexP13rocsparse_intP13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zbsr2csr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)bsr_descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind)[#](#_CPPv418rocsparse_zbsr2csr16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_intK19rocsparse_mat_descrP24rocsparse_double_complexP13rocsparse_intP13rocsparse_int) Convert a sparse BSR matrix into a sparse CSR matrix.

`rocsparse_bsr2csr`

converts a BSR matrix into a CSR matrix. It is assumed, that`csr_val`

,`csr_col_ind`

and`csr_row_ptr`

are allocated. Allocation size for`csr_row_ptr`

is`m+1`

where:\[\begin{split} m = mb * block\_dim \\ n = nb * block\_dim \end{split}\]Allocation for`csr_val`

and`csr_col_ind`

is computed by the the number of blocks in the BSR matrix multiplied by the block dimension squared:\[ nnz = nnzb * block\_dim * block\_dim \]**Example**This example converts a BSR matrix into an CSR matrix.

int main() { // 1 4 2 1 0 0 // A = 0 2 3 5 0 0 // 5 2 2 7 8 6 // 9 3 9 1 6 1 rocsparse_int mb = 2; rocsparse_int nb = 3; rocsparse_int block_dim = 2; rocsparse_int m = mb * block_dim; rocsparse_int n = nb * block_dim; rocsparse_int nnzb = 5; rocsparse_int nnz = nnzb * block_dim * block_dim; std::vector<rocsparse_int> hbsr_row_ptr = {0, 2, 5}; std::vector<rocsparse_int> hbsr_col_ind = {0, 1, 0, 1, 2}; std::vector<float> hbsr_val = {1.0f, 0.0f, 4.0f, 2.0f, 2.0f, 3.0f, 1.0f, 5.0f, 5.0f, 9.0f, 2.0f, 3.0f, 2.0f, 9.0f, 7.0f, 1.0f, 8.0f, 6.0f, 6.0f, 1.0f}; rocsparse_int* dbsr_row_ptr = nullptr; rocsparse_int* dbsr_col_ind = nullptr; float* dbsr_val = nullptr; HIP_CHECK(hipMalloc((void**)&dbsr_row_ptr, sizeof(rocsparse_int) * (mb + 1))); HIP_CHECK(hipMalloc((void**)&dbsr_col_ind, sizeof(rocsparse_int) * nnzb)); HIP_CHECK(hipMalloc((void**)&dbsr_val, sizeof(float) * nnzb * block_dim * block_dim)); HIP_CHECK(hipMemcpy(dbsr_row_ptr, hbsr_row_ptr.data(), sizeof(rocsparse_int) * (mb + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( dbsr_col_ind, hbsr_col_ind.data(), sizeof(rocsparse_int) * nnzb, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dbsr_val, hbsr_val.data(), sizeof(float) * nnzb * block_dim * block_dim, hipMemcpyHostToDevice)); // Create CSR arrays on device rocsparse_int* dcsr_row_ptr = nullptr; rocsparse_int* dcsr_col_ind = nullptr; float* dcsr_val = nullptr; HIP_CHECK(hipMalloc((void**)&dcsr_row_ptr, sizeof(rocsparse_int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&dcsr_col_ind, sizeof(rocsparse_int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcsr_val, sizeof(float) * nnz)); // Create rocsparse handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); rocsparse_mat_descr bsr_descr = nullptr; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&bsr_descr)); rocsparse_mat_descr csr_descr = nullptr; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&csr_descr)); ROCSPARSE_CHECK(rocsparse_set_mat_index_base(bsr_descr, rocsparse_index_base_zero)); ROCSPARSE_CHECK(rocsparse_set_mat_index_base(csr_descr, rocsparse_index_base_zero)); // Format conversion ROCSPARSE_CHECK(rocsparse_sbsr2csr(handle, rocsparse_direction_column, mb, nb, bsr_descr, dbsr_val, dbsr_row_ptr, dbsr_col_ind, block_dim, csr_descr, dcsr_val, dcsr_row_ptr, dcsr_col_ind)); // Copy to host std::vector<rocsparse_int> hcsr_row_ptr(m + 1); std::vector<rocsparse_int> hcsr_col_ind(nnz); std::vector<float> hcsr_val(nnz); HIP_CHECK(hipMemcpy( hcsr_row_ptr.data(), dcsr_row_ptr, sizeof(rocsparse_int) * (m + 1), hipMemcpyDeviceToHost)); HIP_CHECK(hipMemcpy( hcsr_col_ind.data(), dcsr_col_ind, sizeof(rocsparse_int) * nnz, hipMemcpyDeviceToHost)); HIP_CHECK(hipMemcpy(hcsr_val.data(), dcsr_val, sizeof(float) * nnz, hipMemcpyDeviceToHost)); std::cout << "CSR" << std::endl; for(rocsparse_int i = 0; i < m; i++) { rocsparse_int start = hcsr_row_ptr[i]; rocsparse_int end = hcsr_row_ptr[i + 1]; std::vector<float> temp(n, 0.0f); for(rocsparse_int j = start; j < end; j++) { temp[hcsr_col_ind[j]] = hcsr_val[j]; } for(rocsparse_int j = 0; j < n; j++) { std::cout << temp[j] << " "; } std::cout << "" << std::endl; } std::cout << "" << std::endl; ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(csr_descr)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(bsr_descr)); HIP_CHECK(hipFree(dbsr_row_ptr)); HIP_CHECK(hipFree(dbsr_col_ind)); HIP_CHECK(hipFree(dbsr_val)); HIP_CHECK(hipFree(dcsr_row_ptr)); HIP_CHECK(hipFree(dcsr_col_ind)); HIP_CHECK(hipFree(dcsr_val)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dir**–**[in]**the storage format of the blocks,[rocsparse_direction_row](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca40d95f05d0cd4ad3c89465959c58943e)or[rocsparse_direction_column](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca23355bb7b606c550ba61c781bcecfc5b)**mb**–**[in]**number of block rows in the sparse BSR matrix.**nb**–**[in]**number of block columns in the sparse BSR matrix.**bsr_descr**–**[in]**descriptor of the sparse BSR matrix. Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**bsr_val**–**[in]**array of`nnzb*block_dim*block_dim`

containing the values of the sparse BSR matrix.**bsr_row_ptr**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix.**bsr_col_ind**–**[in]**array of`nnzb`

elements containing the block column indices of the sparse BSR matrix.**block_dim**–**[in]**size of the blocks in the sparse BSR matrix.**csr_descr**–**[in]**descriptor of the sparse CSR matrix. Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**csr_val**–**[out]**array of`nnzb*block_dim*block_dim`

elements containing the values of the sparse CSR matrix.**csr_row_ptr**–**[out]**array of`m+1`

where`m=mb*block_dim`

elements that point to the start of every row of the sparse CSR matrix.**csr_col_ind**–**[out]**array of`nnzb*block_dim*block_dim`

elements containing the column indices of the sparse CSR matrix.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`mb`

or`nb`

or`block_dim`

is invalid.**rocsparse_status_invalid_pointer**–`bsr_val`

,`bsr_row_ptr`

,`bsr_col_ind`

,`csr_val`

,`csr_row_ptr`

or`csr_col_ind`

pointer is invalid.



## rocsparse_gebsr2csr()[#](#rocsparse-gebsr2csr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sgebsr2csr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)bsr_descr, const float *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr, float *csr_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind)[#](#_CPPv420rocsparse_sgebsr2csr16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPfP13rocsparse_intP13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dgebsr2csr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)bsr_descr, const double *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr, double *csr_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind)[#](#_CPPv420rocsparse_dgebsr2csr16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPdP13rocsparse_intP13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cgebsr2csr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)bsr_descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind)[#](#_CPPv420rocsparse_cgebsr2csr16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrP23rocsparse_float_complexP13rocsparse_intP13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zgebsr2csr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)bsr_descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind)[#](#_CPPv420rocsparse_zgebsr2csr16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrP24rocsparse_double_complexP13rocsparse_intP13rocsparse_int) Convert a sparse general BSR matrix into a sparse CSR matrix.

`rocsparse_gebsr2csr`

converts a BSR matrix into a CSR matrix. The input matrix is assumed to be allocated such that array`bsr_row_ptr`

has length`mb+1`

,`bsr_col_ind`

has length`nnzb`

, and`bsr_val`

has length`nnzb*row_block_dim*col_block_dim`

. The output matrix is assumed to be allocated such that array`csr_row_ptr`

has length`m+1`

,`csr_col_ind`

has length`nnz`

, and`csr_val`

has length`nnz`

where:\[\begin{split} m = mb * row\_block\_dim \\ n = nb * col\_block\_dim \\ nnz = nnzb * row\_block\_dim * col\_block\_dim \end{split}\]**Example**This example converts a general BSR matrix into an CSR matrix.

int main() { // 1 4 0 0 0 0 // A = 0 2 3 0 0 0 // 5 0 0 7 8 0 // 0 0 9 0 6 0 rocsparse_int mb = 2; rocsparse_int nb = 2; rocsparse_int row_block_dim = 2; rocsparse_int col_block_dim = 3; rocsparse_int m = mb * row_block_dim; rocsparse_int n = nb * col_block_dim; // Define host arrays rocsparse_int h_bsr_row_ptr[] = {0, 1, 3}; rocsparse_int h_bsr_col_ind[] = {0, 0, 1}; float h_bsr_val[] = {1, 0, 4, 2, 0, 3, 5, 0, 0, 0, 0, 9, 7, 0, 8, 6, 0, 0}; rocsparse_int nnzb = h_bsr_row_ptr[mb] - h_bsr_row_ptr[0]; // Allocate device memory for BSR matrix rocsparse_int* d_bsr_row_ptr; rocsparse_int* d_bsr_col_ind; float* d_bsr_val; HIP_CHECK(hipMalloc((void**)&d_bsr_row_ptr, sizeof(rocsparse_int) * (mb + 1))); HIP_CHECK(hipMalloc((void**)&d_bsr_col_ind, sizeof(rocsparse_int) * nnzb)); HIP_CHECK(hipMalloc((void**)&d_bsr_val, sizeof(float) * nnzb * row_block_dim * col_block_dim)); HIP_CHECK(hipMemcpy( d_bsr_row_ptr, h_bsr_row_ptr, sizeof(rocsparse_int) * (mb + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( d_bsr_col_ind, h_bsr_col_ind, sizeof(rocsparse_int) * nnzb, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(d_bsr_val, h_bsr_val, sizeof(float) * nnzb * row_block_dim * col_block_dim, hipMemcpyHostToDevice)); // Create CSR arrays on device rocsparse_int* d_csr_row_ptr; rocsparse_int* d_csr_col_ind; float* d_csr_val; HIP_CHECK(hipMalloc((void**)&d_csr_row_ptr, sizeof(rocsparse_int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&d_csr_col_ind, sizeof(rocsparse_int) * nnzb * row_block_dim * col_block_dim)); HIP_CHECK(hipMalloc((void**)&d_csr_val, sizeof(float) * nnzb * row_block_dim * col_block_dim)); // Create rocsparse handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); rocsparse_mat_descr bsr_descr = nullptr; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&bsr_descr)); rocsparse_mat_descr csr_descr = nullptr; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&csr_descr)); ROCSPARSE_CHECK(rocsparse_set_mat_index_base(bsr_descr, rocsparse_index_base_zero)); ROCSPARSE_CHECK(rocsparse_set_mat_index_base(csr_descr, rocsparse_index_base_zero)); // Format conversion ROCSPARSE_CHECK(rocsparse_sgebsr2csr(handle, rocsparse_direction_column, mb, nb, bsr_descr, d_bsr_val, d_bsr_row_ptr, d_bsr_col_ind, row_block_dim, col_block_dim, csr_descr, d_csr_val, d_csr_row_ptr, d_csr_col_ind)); // Clean up HIP_CHECK(hipFree(d_bsr_row_ptr)); HIP_CHECK(hipFree(d_bsr_col_ind)); HIP_CHECK(hipFree(d_bsr_val)); HIP_CHECK(hipFree(d_csr_row_ptr)); HIP_CHECK(hipFree(d_csr_col_ind)); HIP_CHECK(hipFree(d_csr_val)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(bsr_descr)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(csr_descr)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dir**–**[in]**the storage format of the blocks,[rocsparse_direction_row](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca40d95f05d0cd4ad3c89465959c58943e)or[rocsparse_direction_column](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca23355bb7b606c550ba61c781bcecfc5b)**mb**–**[in]**number of block rows in the sparse general BSR matrix.**nb**–**[in]**number of block columns in the sparse general BSR matrix.**bsr_descr**–**[in]**descriptor of the sparse general BSR matrix. Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**bsr_val**–**[in]**array of`nnzb*row_block_dim*col_block_dim`

containing the values of the sparse BSR matrix.**bsr_row_ptr**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix.**bsr_col_ind**–**[in]**array of`nnzb`

elements containing the block column indices of the sparse BSR matrix.**row_block_dim**–**[in]**row size of the blocks in the sparse general BSR matrix.**col_block_dim**–**[in]**column size of the blocks in the sparse general BSR matrix.**csr_descr**–**[in]**descriptor of the sparse CSR matrix. Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**csr_val**–**[out]**array of`nnzb*row_block_dim*col_block_dim`

elements containing the values of the sparse CSR matrix.**csr_row_ptr**–**[out]**array of`m+1`

where`m=mb*row_block_dim`

elements that point to the start of every row of the sparse CSR matrix.**csr_col_ind**–**[out]**array of`nnzb*block_dim*block_dim`

elements containing the column indices of the sparse CSR matrix.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`mb`

or`nb`

or`block_dim`

is invalid.**rocsparse_status_invalid_pointer**–`bsr_val`

,`bsr_row_ptr`

,`bsr_col_ind`

,`csr_val`

,`csr_row_ptr`

or`csr_col_ind`

pointer is invalid.



## rocsparse_gebsr2gebsr_buffer_size()[#](#rocsparse-gebsr2gebsr-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sgebsr2gebsr_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A, const float *bsr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim_C, size_t *buffer_size)[#](#_CPPv434rocsparse_sgebsr2gebsr_buffer_size16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dgebsr2gebsr_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A, const double *bsr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim_C, size_t *buffer_size)[#](#_CPPv434rocsparse_dgebsr2gebsr_buffer_size16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cgebsr2gebsr_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim_C, size_t *buffer_size)[#](#_CPPv434rocsparse_cgebsr2gebsr_buffer_size16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zgebsr2gebsr_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim_C, size_t *buffer_size)[#](#_CPPv434rocsparse_zgebsr2gebsr_buffer_size16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intP6size_t) `rocsparse_gebsr2gebsr_buffer_size`

returns the size of the temporary storage buffer that is required by[rocsparse_gebsr2gebsr_nnz()](#rocsparse__gebsr2gebsr_8h_1abf1cad481733b5d3dab2c714c8f21c87)and[rocsparse_Xgebsr2gebsr()](#rocsparse__gebsr2gebsr_8h_1a953018ef91b4fbf2acd9c8bc1929d2c0). The temporary storage buffer must be allocated by the user.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dir**–**[in]**the storage format of the blocks,[rocsparse_direction_row](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca40d95f05d0cd4ad3c89465959c58943e)or[rocsparse_direction_column](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca23355bb7b606c550ba61c781bcecfc5b)**mb**–**[in]**number of block rows of the general BSR sparse matrix \(A\).**nb**–**[in]**number of block columns of the general BSR sparse matrix \(A\).**nnzb**–**[in]**number of blocks in the general BSR sparse matrix \(A\).**descr_A**–**[in]**the descriptor of the general BSR sparse matrix \(A\), the supported matrix type is[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)and also any valid value of the[rocsparse_index_base](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060d).**bsr_val_A**–**[in]**array of`nnzb*row_block_dim_A*col_block_dim_A`

containing the values of the sparse general BSR matrix \(A\).**bsr_row_ptr_A**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse general BSR matrix \(A\).**bsr_col_ind_A**–**[in]**array of`nnzb`

elements containing the block column indices of the sparse general BSR matrix \(A\).**row_block_dim_A**–**[in]**row size of the blocks in the sparse general BSR matrix \(A\).**col_block_dim_A**–**[in]**column size of the blocks in the sparse general BSR matrix \(A\).**row_block_dim_C**–**[in]**row size of the blocks in the sparse general BSR matrix \(C\).**col_block_dim_C**–**[in]**column size of the blocks in the sparse general BSR matrix \(C\).**buffer_size**–**[out]**number of bytes of the temporary storage buffer required by[rocsparse_gebsr2gebsr_nnz()](#rocsparse__gebsr2gebsr_8h_1abf1cad481733b5d3dab2c714c8f21c87)and[rocsparse_Xgebsr2gebsr()](#rocsparse__gebsr2gebsr_8h_1a953018ef91b4fbf2acd9c8bc1929d2c0).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`mb`

or`nb`

or`nnzb`

or`row_block_dim_A`

or`col_block_dim_A`

or`row_block_dim_C`

or`col_block_dim_C`

is invalid.**rocsparse_status_invalid_pointer**–`bsr_row_ptr_A`

or`bsr_col_ind_A`

or`descr_A`

or`buffer_size`

pointer is invalid.



## rocsparse_gebsr2gebsr_nnz()[#](#rocsparse-gebsr2gebsr-nnz)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_gebsr2gebsr_nnz([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_total_dev_host_ptr, void *temp_buffer)[#](#_CPPv425rocsparse_gebsr2gebsr_nnz16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrP13rocsparse_int13rocsparse_int13rocsparse_intP13rocsparse_intPv) This function takes a sparse GEneral BSR matrix as input and computes the block row offset array,

`bsr_row_ptr_C`

, and the total number of nonzero blocks,`nnz_total_dev_host_ptr`

, that will result from converting the GEneral BSR format input matrix to a GEneral BSR format output matrix. The input and output matrices can have different row and column block dimensions.`rocsparse_gebsr2gebsr_nnz`

is the second step in the conversion and is used in conjunction with[rocsparse_Xgebsr2gebsr_buffer_size()](#rocsparse__gebsr2gebsr_8h_1ab5d3695bb9fb4b141166bd61dd436bad)and[rocsparse_Xgebsr2gebsr()](#rocsparse__gebsr2gebsr_8h_1a953018ef91b4fbf2acd9c8bc1929d2c0).`rocsparse_gebsr2gebsr_nnz`

accepts both host and device pointers for`nnz_total_dev_host_ptr`

which can be set by calling[rocsparse_set_pointer_mode](auxiliary.html#rocsparse-auxiliary_8h_1ae46f13354bf790cc26756c227bff7e64)prior to calling`rocsparse_gebsr2gebsr_nnz`

.Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dir**–**[in]**the storage format of the blocks,[rocsparse_direction_row](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca40d95f05d0cd4ad3c89465959c58943e)or[rocsparse_direction_column](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca23355bb7b606c550ba61c781bcecfc5b)**mb**–**[in]**number of block rows of the general BSR sparse matrix \(A\).**nb**–**[in]**number of block columns of the general BSR sparse matrix \(A\).**nnzb**–**[in]**number of blocks in the general BSR sparse matrix \(A\).**descr_A**–**[in]**the descriptor of the general BSR sparse matrix \(A\), the supported matrix type is[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)and also any valid value of the[rocsparse_index_base](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060d).**bsr_row_ptr_A**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse general BSR matrix \(A\).**bsr_col_ind_A**–**[in]**array of`nnzb`

elements containing the block column indices of the sparse general BSR matrix \(A\).**row_block_dim_A**–**[in]**row size of the blocks in the sparse general BSR matrix \(A\).**col_block_dim_A**–**[in]**column size of the blocks in the sparse general BSR matrix \(A\).**descr_C**–**[in]**the descriptor of the general BSR sparse matrix \(C\), the supported matrix type is[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)and also any valid value of the[rocsparse_index_base](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060d).**bsr_row_ptr_C**–**[in]**array of`mb_C+1`

elements that point to the start of every block row of the sparse general BSR matrix \(C\) where`mb_C=`

(m+row_block_dim_C-1)/row_block_dim_C.**row_block_dim_C**–**[in]**row size of the blocks in the sparse general BSR matrix \(C\).**col_block_dim_C**–**[in]**column size of the blocks in the sparse general BSR matrix \(C\).**nnz_total_dev_host_ptr**–**[out]**total number of nonzero blocks in general BSR sparse matrix \(C\) stored using device or host memory.**temp_buffer**–**[out]**buffer allocated by the user whose size is determined by calling[rocsparse_Xgebsr2gebsr_buffer_size()](#rocsparse__gebsr2gebsr_8h_1ab5d3695bb9fb4b141166bd61dd436bad).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`mb`

or`nb`

or`nnzb`

or`row_block_dim_A`

or`col_block_dim_A`

or`row_block_dim_C`

or`col_block_dim_C`

is invalid.**rocsparse_status_invalid_pointer**–`bsr_row_ptr_A`

or`bsr_col_ind_A`

or`bsr_row_ptr_C`

or`descr_A`

or`descr_C`

or`temp_buffer`

pointer is invalid.



## rocsparse_gebsr2gebsr()[#](#rocsparse-gebsr2gebsr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sgebsr2gebsr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A, const float *bsr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_C, float *bsr_val_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim_C, void *temp_buffer)[#](#_CPPv422rocsparse_sgebsr2gebsr16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPfP13rocsparse_intP13rocsparse_int13rocsparse_int13rocsparse_intPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dgebsr2gebsr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A, const double *bsr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_C, double *bsr_val_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim_C, void *temp_buffer)[#](#_CPPv422rocsparse_dgebsr2gebsr16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPdP13rocsparse_intP13rocsparse_int13rocsparse_int13rocsparse_intPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cgebsr2gebsr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_C,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsr_val_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim_C, void *temp_buffer)[#](#_CPPv422rocsparse_cgebsr2gebsr16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrP23rocsparse_float_complexP13rocsparse_intP13rocsparse_int13rocsparse_int13rocsparse_intPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zgebsr2gebsr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_C,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsr_val_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim_C, void *temp_buffer)[#](#_CPPv422rocsparse_zgebsr2gebsr16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrP24rocsparse_double_complexP13rocsparse_intP13rocsparse_int13rocsparse_int13rocsparse_intPv) This function converts the general BSR sparse matrix \(A\) to another general BSR sparse matrix \(C\).

`rocsparse_gebsr2gebsr`

converts a GEneral BSR matrix \(A\) into a GEneral BSR matrix \(C\). The input and output matrices can have different row and column block dimensions. The input matrix \(A\) is assumed to be allocated such that array`bsr_row_ptr_A`

has length`mb+1`

,`bsr_col_ind_A`

has length`nnzb`

, and`bsr_val_A`

has length`nnzb*row_block_dim_A*col_block_dim_A`

. The output matrix \(C\) is assumed to be allocated such that array`bsr_row_ptr_C`

has length`mb_C+1`

,`bsr_col_ind_C`

has length`nnzb_C`

, and`bsr_val_C`

has length`nnzb_C*row_block_dim_C*col_block_dim_C`

where:\[\begin{split} m = mb * row\_block\_dim\_A \\ n = nb * col\_block\_dim\_A \end{split}\]and\[\begin{split} mb\_C = (m + row\_block\_dim\_C - 1) / row\_block\_dim\_C \\ nb\_C = (n + col\_block\_dim\_C - 1) / col\_block\_dim\_C \end{split}\]The number of non-zero blocks in the output sparse \(C\) matrix (i.e.`nnzb_C`

) is computed using[rocsparse_gebsr2gebsr_nnz()](#rocsparse__gebsr2gebsr_8h_1abf1cad481733b5d3dab2c714c8f21c87)which also fills in`bsr_row_ptr_C`

array.Converting from a sparse GEneral BSR matrix to a sparse GEneral BSR matrix requires three steps. First, the user calls

[rocsparse_Xgebsr2gebsr_buffer_size()](#rocsparse__gebsr2gebsr_8h_1ab5d3695bb9fb4b141166bd61dd436bad)in order to determine the size of the required temporary storage buffer. Once this has been determined, the user allocates this buffer. The user also now allocates the`bsr_row_ptr_C`

array to have length`mb_C+1`

and passes this to the function[rocsparse_gebsr2gebsr_nnz](#rocsparse__gebsr2gebsr_8h_1abf1cad481733b5d3dab2c714c8f21c87). This will fill the`bsr_row_ptr_C`

array and also compute the total number of nonzero blocks in the GEneral BSR output \(C\) matrix. Now that the total number of nonzero blocks is known, the user can allocate the`bsr_col_ind_C`

and`bsr_val_C`

arrays. Finally, the user calls`rocsparse_gebsr2gebsr`

to complete the conversion. Once the conversion is complete, the temporary storage buffer can be deallocated. See example below.**Example**This example converts a GEneral BSR matrix into an GEneral BSR matrix.

int main() { // 1 2 0 0 5 6 // A = 3 4 0 0 7 8 // 6 5 3 4 0 0 // 1 2 5 4 0 0 rocsparse_int mb_A = 2; rocsparse_int nb_A = 2; rocsparse_int nnzb_A = 4; rocsparse_int row_block_dim_A = 2; rocsparse_int col_block_dim_A = 2; rocsparse_int m = mb_A * row_block_dim_A; rocsparse_int n = nb_A * col_block_dim_A; rocsparse_direction dir = rocsparse_direction_row; std::vector<rocsparse_int> hbsr_row_ptr_A = {0, 2, 4}; std::vector<rocsparse_int> hbsr_col_ind_A = {0, 2, 0, 1}; std::vector<float> hbsr_val_A = {1, 2, 3, 4, 5, 6, 7, 8, 6, 5, 1, 2, 3, 4, 5, 4}; rocsparse_int* dbsr_row_ptr_A = nullptr; rocsparse_int* dbsr_col_ind_A = nullptr; float* dbsr_val_A = nullptr; HIP_CHECK(hipMalloc((void**)&dbsr_row_ptr_A, sizeof(rocsparse_int) * (mb_A + 1))); HIP_CHECK(hipMalloc((void**)&dbsr_col_ind_A, sizeof(rocsparse_int) * nnzb_A)); HIP_CHECK( hipMalloc((void**)&dbsr_val_A, sizeof(float) * nnzb_A * row_block_dim_A * col_block_dim_A)); HIP_CHECK(hipMemcpy(dbsr_row_ptr_A, hbsr_row_ptr_A.data(), sizeof(rocsparse_int) * (mb_A + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dbsr_col_ind_A, hbsr_col_ind_A.data(), sizeof(rocsparse_int) * nnzb_A, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dbsr_val_A, hbsr_val_A.data(), sizeof(float) * nnzb_A * row_block_dim_A * col_block_dim_A, hipMemcpyHostToDevice)); rocsparse_int row_block_dim_C = 2; rocsparse_int col_block_dim_C = 3; rocsparse_int mb_C = (m + row_block_dim_C - 1) / row_block_dim_C; rocsparse_int nb_C = (m + row_block_dim_C - 1) / row_block_dim_C; rocsparse_int* dbsr_row_ptr_C = nullptr; HIP_CHECK(hipMalloc((void**)&dbsr_row_ptr_C, sizeof(rocsparse_int) * (mb_C + 1))); rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); rocsparse_mat_descr descr_A; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr_A)); rocsparse_mat_descr descr_C; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr_C)); // Obtain the temporary buffer size size_t buffer_size; ROCSPARSE_CHECK(rocsparse_sgebsr2gebsr_buffer_size(handle, dir, mb_A, nb_A, nnzb_A, descr_A, dbsr_val_A, dbsr_row_ptr_A, dbsr_col_ind_A, row_block_dim_A, col_block_dim_A, row_block_dim_C, col_block_dim_C, &buffer_size)); // Allocate temporary buffer void* temp_buffer; HIP_CHECK(hipMalloc(&temp_buffer, buffer_size)); rocsparse_int nnzb_C; ROCSPARSE_CHECK(rocsparse_gebsr2gebsr_nnz(handle, dir, mb_A, nb_A, nnzb_A, descr_A, dbsr_row_ptr_A, dbsr_col_ind_A, row_block_dim_A, col_block_dim_A, descr_C, dbsr_row_ptr_C, row_block_dim_C, col_block_dim_C, &nnzb_C, temp_buffer)); rocsparse_int* dbsr_col_ind_C = nullptr; float* dbsr_val_C = nullptr; HIP_CHECK(hipMalloc((void**)&dbsr_col_ind_C, sizeof(rocsparse_int) * nnzb_C)); HIP_CHECK( hipMalloc((void**)&dbsr_val_C, sizeof(float) * nnzb_C * row_block_dim_C * col_block_dim_C)); ROCSPARSE_CHECK(rocsparse_sgebsr2gebsr(handle, dir, mb_A, nb_A, nnzb_A, descr_A, dbsr_val_A, dbsr_row_ptr_A, dbsr_col_ind_A, row_block_dim_A, col_block_dim_A, descr_C, dbsr_val_C, dbsr_row_ptr_C, dbsr_col_ind_C, row_block_dim_C, col_block_dim_C, temp_buffer)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr_A)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr_C)); HIP_CHECK(hipFree(temp_buffer)); HIP_CHECK(hipFree(dbsr_row_ptr_A)); HIP_CHECK(hipFree(dbsr_col_ind_A)); HIP_CHECK(hipFree(dbsr_val_A)); HIP_CHECK(hipFree(dbsr_row_ptr_C)); HIP_CHECK(hipFree(dbsr_col_ind_C)); HIP_CHECK(hipFree(dbsr_val_C)); return 0; }


Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dir**–**[in]**the storage format of the blocks,[rocsparse_direction_row](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca40d95f05d0cd4ad3c89465959c58943e)or[rocsparse_direction_column](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca23355bb7b606c550ba61c781bcecfc5b)**mb**–**[in]**number of block rows of the general BSR sparse matrix \(A\).**nb**–**[in]**number of block columns of the general BSR sparse matrix \(A\).**nnzb**–**[in]**number of blocks in the general BSR sparse matrix \(A\).**descr_A**–**[in]**the descriptor of the general BSR sparse matrix \(A\), the supported matrix type is[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)and also any valid value of the[rocsparse_index_base](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060d).**bsr_val_A**–**[in]**array of`nnzb*row_block_dim_A*col_block_dim_A`

containing the values of the sparse general BSR matrix \(A\).**bsr_row_ptr_A**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse general BSR matrix \(A\).**bsr_col_ind_A**–**[in]**array of`nnzb`

elements containing the block column indices of the sparse general BSR matrix \(A\).**row_block_dim_A**–**[in]**row size of the blocks in the sparse general BSR matrix \(A\).**col_block_dim_A**–**[in]**column size of the blocks in the sparse general BSR matrix \(A\).**descr_C**–**[in]**the descriptor of the general BSR sparse matrix \(C\), the supported matrix type is[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)and also any valid value of the[rocsparse_index_base](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060d).**bsr_val_C**–**[in]**array of`nnzb_C*row_block_dim_C*col_block_dim_C`

containing the values of the sparse general BSR matrix \(C\).**bsr_row_ptr_C**–**[in]**array of`mb_C+1`

elements that point to the start of every block row of the sparse general BSR matrix \(C\).**bsr_col_ind_C**–**[in]**array of`nnzb_C`

elements containing the block column indices of the sparse general BSR matrix \(C\).**row_block_dim_C**–**[in]**row size of the blocks in the sparse general BSR matrix \(C\).**col_block_dim_C**–**[in]**column size of the blocks in the sparse general BSR matrix \(C\).**temp_buffer**–**[out]**buffer allocated by the user whose size is determined by calling[rocsparse_Xgebsr2gebsr_buffer_size()](#rocsparse__gebsr2gebsr_8h_1ab5d3695bb9fb4b141166bd61dd436bad).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`mb`

or`nb`

or`nnzb`

or`row_block_dim_A`

or`col_block_dim_A`

or`row_block_dim_C`

or`col_block_dim_C`

is invalid.**rocsparse_status_invalid_pointer**–`bsr_row_ptr_A`

or`bsr_col_ind_A`

or`bsr_val_A`

or`bsr_row_ptr_C`

or`bsr_col_ind_C`

or`bsr_val_C`

or`descr_A`

or`descr_C`

or`temp_buffer`

pointer is invalid.



## rocsparse_csr2bsr_nnz()[#](#rocsparse-csr2bsr-nnz)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_csr2bsr_nnz([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)bsr_descr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_nnz)[#](#_CPPv421rocsparse_csr2bsr_nnz16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK13rocsparse_intPK13rocsparse_int13rocsparse_intK19rocsparse_mat_descrP13rocsparse_intP13rocsparse_int) This function takes a sparse CSR matrix as input and computes the block row offset array,

`bsr_row_ptr`

, and the total number of nonzero blocks,`bsr_nnz`

, that will result from converting the CSR format input matrix to a BSR format output matrix. This function is the first step in the conversion and is used in conjunction with[rocsparse_Xcsr2bsr()](#rocsparse__csr2bsr_8h_1a0c83d56763b8502116413483148a9c32).Note

The routine does support asynchronous execution if the pointer mode is set to device.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dir**–**[in]**direction that specified whether to count nonzero elements by[rocsparse_direction_row](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca40d95f05d0cd4ad3c89465959c58943e)or by[rocsparse_direction_column](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca23355bb7b606c550ba61c781bcecfc5b).**m**–**[in]**number of rows of the sparse CSR matrix.**n**–**[in]**number of columns of the sparse CSR matrix.**csr_descr**–**[in]**descriptor of the sparse CSR matrix. Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**csr_row_ptr**–**[in]**integer array containing`m+1`

elements that point to the start of each row of the CSR matrix**csr_col_ind**–**[in]**integer array of the column indices for each non-zero element in the CSR matrix**block_dim**–**[in]**the block dimension of the BSR matrix. Between 1 and min(m, n)**bsr_descr**–**[in]**descriptor of the sparse BSR matrix. Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**bsr_row_ptr**–**[out]**integer array containing`mb+1`

elements that point to the start of each block row of the BSR matrix**bsr_nnz**–**[out]**total number of nonzero elements in device or host memory.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`n`

or`block_dim`

is invalid.**rocsparse_status_invalid_pointer**–`csr_row_ptr`

or`csr_col_ind`

or`bsr_row_ptr`

or`bsr_nnz`

pointer is invalid.



## rocsparse_csr2bsr()[#](#rocsparse-csr2bsr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scsr2bsr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr, const float *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)bsr_descr, float *bsr_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind)[#](#_CPPv418rocsparse_scsr2bsr16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPfP13rocsparse_intP13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcsr2bsr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr, const double *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)bsr_descr, double *bsr_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind)[#](#_CPPv418rocsparse_dcsr2bsr16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPdP13rocsparse_intP13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccsr2bsr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)bsr_descr,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsr_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind)[#](#_CPPv418rocsparse_ccsr2bsr16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_intK19rocsparse_mat_descrP23rocsparse_float_complexP13rocsparse_intP13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcsr2bsr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)bsr_descr,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsr_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind)[#](#_CPPv418rocsparse_zcsr2bsr16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_intK19rocsparse_mat_descrP24rocsparse_double_complexP13rocsparse_intP13rocsparse_int) Convert a sparse CSR matrix into a sparse BSR matrix.

`rocsparse_csr2bsr`

converts a CSR matrix into a BSR matrix. It is assumed, that`bsr_val`

,`bsr_col_ind`

and`bsr_row_ptr`

are allocated. Allocation size for`bsr_row_ptr`

is computed as`mb+1`

where`mb`

is the number of block rows and`nb`

is the number of block columns in the BSR matrix:\[\begin{split} mb = (m + block\_dim - 1) / block\_dim \\ nb = (n + block\_dim - 1) / block\_dim \end{split}\]Allocation size for`bsr_val`

and`bsr_col_ind`

is computed using[rocsparse_csr2bsr_nnz()](#rocsparse__csr2bsr_8h_1a49119cf912b60d0d1ba9eb63c253e6d3)which also fills in`bsr_row_ptr`

.Converting from a sparse CSR matrix to a sparse BSR matrix requires two steps. First, the user allocates the

`bsr_row_ptr`

array to have length`mb+1`

and passes this to the function[rocsparse_csr2bsr_nnz](#rocsparse__csr2bsr_8h_1a49119cf912b60d0d1ba9eb63c253e6d3). This will fill the`bsr_row_ptr`

array and also compute the total number of nonzero blocks in the BSR matrix. Now that the total number of nonzero blocks is known, the user can allocate the`bsr_col_ind`

and`bsr_val`

arrays. Finally, the user calls`rocsparse_csr2bsr`

to complete the conversion. See example below.`rocsparse_csr2bsr`

requires extra temporary storage that is allocated internally if`block_dim>16`

**Example**This example converts a CSR matrix into an BSR matrix.

int main() { // Initialize rocSPARSE rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // 1 4 0 0 0 0 // A = 0 2 3 0 0 0 // 5 0 0 7 8 0 // 0 0 9 0 6 0 rocsparse_int m = 4; rocsparse_int n = 6; rocsparse_int block_dim = 2; rocsparse_int nnz = 9; rocsparse_int mb = (m + block_dim - 1) / block_dim; rocsparse_int nb = (n + block_dim - 1) / block_dim; // Define host arrays rocsparse_int h_csr_row_ptr[] = {0, 2, 4, 7, 9}; rocsparse_int h_csr_col_ind[] = {0, 1, 1, 2, 0, 3, 4, 2, 4}; float h_csr_val[] = {1, 4, 2, 3, 5, 7, 8, 9, 6}; // Allocate and initialize device memory rocsparse_int* d_csr_row_ptr; rocsparse_int* d_csr_col_ind; float* d_csr_val; HIP_CHECK(hipMalloc((void**)&d_csr_row_ptr, sizeof(rocsparse_int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&d_csr_col_ind, sizeof(rocsparse_int) * nnz)); HIP_CHECK(hipMalloc((void**)&d_csr_val, sizeof(float) * nnz)); HIP_CHECK(hipMemcpy( d_csr_row_ptr, h_csr_row_ptr, sizeof(rocsparse_int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( d_csr_col_ind, h_csr_col_ind, sizeof(rocsparse_int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(d_csr_val, h_csr_val, sizeof(float) * nnz, hipMemcpyHostToDevice)); // Create matrix descriptors rocsparse_mat_descr csr_descr; rocsparse_mat_descr bsr_descr; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&csr_descr)); ROCSPARSE_CHECK(rocsparse_create_mat_descr(&bsr_descr)); // Allocate BSR row pointer array rocsparse_int* d_bsr_row_ptr; HIP_CHECK(hipMalloc((void**)&d_bsr_row_ptr, sizeof(rocsparse_int) * (mb + 1))); // Compute the number of non-zero block entries rocsparse_int nnzb; rocsparse_int* nnzTotalDevHostPtr = &nnzb; ROCSPARSE_CHECK(rocsparse_csr2bsr_nnz(handle, rocsparse_direction_row, m, n, csr_descr, d_csr_row_ptr, d_csr_col_ind, block_dim, bsr_descr, d_bsr_row_ptr, nnzTotalDevHostPtr)); // Allocate BSR column indices and values arrays rocsparse_int* d_bsr_col_ind; float* d_bsr_val; HIP_CHECK(hipMalloc((void**)&d_bsr_col_ind, sizeof(rocsparse_int) * nnzb)); HIP_CHECK(hipMalloc((void**)&d_bsr_val, sizeof(float) * (block_dim * block_dim) * nnzb)); // Convert CSR to BSR ROCSPARSE_CHECK(rocsparse_scsr2bsr(handle, rocsparse_direction_row, m, n, csr_descr, d_csr_val, d_csr_row_ptr, d_csr_col_ind, block_dim, bsr_descr, d_bsr_val, d_bsr_row_ptr, d_bsr_col_ind)); // Clean up HIP_CHECK(hipFree(d_csr_row_ptr)); HIP_CHECK(hipFree(d_csr_col_ind)); HIP_CHECK(hipFree(d_csr_val)); HIP_CHECK(hipFree(d_bsr_row_ptr)); HIP_CHECK(hipFree(d_bsr_col_ind)); HIP_CHECK(hipFree(d_bsr_val)); // Destroy matrix descriptors and rocSPARSE handle ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(csr_descr)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(bsr_descr)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); return 0; }


Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dir**–**[in]**the storage format of the blocks,[rocsparse_direction_row](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca40d95f05d0cd4ad3c89465959c58943e)or[rocsparse_direction_column](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca23355bb7b606c550ba61c781bcecfc5b)**m**–**[in]**number of rows in the sparse CSR matrix.**n**–**[in]**number of columns in the sparse CSR matrix.**csr_descr**–**[in]**descriptor of the sparse CSR matrix. Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**csr_val**–**[in]**array of`nnz`

elements containing the values of the sparse CSR matrix.**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csr_col_ind**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**block_dim**–**[in]**size of the blocks in the sparse BSR matrix.**bsr_descr**–**[in]**descriptor of the sparse BSR matrix. Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**bsr_val**–**[out]**array of`nnzb*block_dim*block_dim`

containing the values of the sparse BSR matrix.**bsr_row_ptr**–**[out]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix.**bsr_col_ind**–**[out]**array of`nnzb`

elements containing the block column indices of the sparse BSR matrix.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`n`

or`block_dim`

is invalid.**rocsparse_status_invalid_pointer**–`bsr_val`

,`bsr_row_ptr`

,`bsr_col_ind`

,`csr_val`

,`csr_row_ptr`

or`csr_col_ind`

pointer is invalid.



## rocsparse_csr2gebsr_nnz()[#](#rocsparse-csr2gebsr-nnz)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_csr2gebsr_nnz([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)bsr_descr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_nnz_devhost, void *temp_buffer)[#](#_CPPv423rocsparse_csr2gebsr_nnz16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descrP13rocsparse_int13rocsparse_int13rocsparse_intP13rocsparse_intPv) This function takes a sparse CSR matrix as input and computes the block row offset array,

`bsr_row_ptr`

, and the total number of nonzero blocks,`bsr_nnz_devhost`

, that will result from converting the CSR format input matrix to a GEneral BSR format output matrix. This function is the second step in the conversion and is used in conjunction with[rocsparse_Xcsr2gebsr_buffer_size()](#rocsparse__csr2gebsr_8h_1a1f1e58605a8acdbc89687982022d1b60)and[rocsparse_Xcsr2gebsr()](#rocsparse__csr2gebsr_8h_1a68f14b88aabb8289dcdf2f1753a5c838).`rocsparse_csr2gebsr_nnz`

accepts both host and device pointers for`bsr_nnz_devhost`

which can be set by calling[rocsparse_set_pointer_mode](auxiliary.html#rocsparse-auxiliary_8h_1ae46f13354bf790cc26756c227bff7e64)prior to calling`rocsparse_csr2gebsr_nnz`

.Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dir**–**[in]**direction that specified whether to count nonzero elements by[rocsparse_direction_row](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca40d95f05d0cd4ad3c89465959c58943e)or by[rocsparse_direction_column](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca23355bb7b606c550ba61c781bcecfc5b).**m**–**[in]**number of rows of the sparse CSR matrix.**n**–**[in]**number of columns of the sparse CSR matrix.**csr_descr**–**[in]**descriptor of the sparse CSR matrix. Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**csr_row_ptr**–**[in]**integer array containing`m+1`

elements that point to the start of each row of the CSR matrix**csr_col_ind**–**[in]**integer array of the column indices for each non-zero element in the CSR matrix**bsr_descr**–**[in]**descriptor of the sparse GEneral BSR matrix. Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**bsr_row_ptr**–**[out]**integer array containing`mb+1`

elements that point to the start of each block row of the General BSR matrix**row_block_dim**–**[in]**the row block dimension of the GEneral BSR matrix. Between \(1\) and \(\min(m, n)\)**col_block_dim**–**[in]**the col block dimension of the GEneral BSR matrix. Between \(1\) and \(\min(m, n)\)**bsr_nnz_devhost**–**[out]**total number of nonzero elements in device or host memory.**temp_buffer**–**[in]**buffer allocated by the user whose size is determined by calling[rocsparse_Xcsr2gebsr_buffer_size()](#rocsparse__csr2gebsr_8h_1a1f1e58605a8acdbc89687982022d1b60).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`n`

or`row_block_dim`

`col_block_dim`

is invalid.**rocsparse_status_invalid_pointer**–`csr_row_ptr`

or`csr_col_ind`

or`bsr_row_ptr`

or`bsr_nnz_devhost`

pointer is invalid.



## rocsparse_csr2gebsr_buffer_size()[#](#rocsparse-csr2gebsr-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scsr2gebsr_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr, const float *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, size_t *buffer_size)[#](#_CPPv432rocsparse_scsr2gebsr_buffer_size16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcsr2gebsr_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr, const double *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, size_t *buffer_size)[#](#_CPPv432rocsparse_dcsr2gebsr_buffer_size16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccsr2gebsr_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, size_t *buffer_size)[#](#_CPPv432rocsparse_ccsr2gebsr_buffer_size16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcsr2gebsr_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, size_t *buffer_size)[#](#_CPPv432rocsparse_zcsr2gebsr_buffer_size16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intP6size_t) `rocsparse_csr2gebsr_buffer_size`

returns the size of the temporary buffer that is required by[rocsparse_csr2gebsr_nnz](#rocsparse__csr2gebsr_8h_1ae711daa792b64d20adcb394f3931e64c)and[rocsparse_Xcsr2gebsr()](#rocsparse__csr2gebsr_8h_1a68f14b88aabb8289dcdf2f1753a5c838). The temporary storage buffer must be allocated by the user.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dir**–**[in]**direction that specified whether to count nonzero elements by[rocsparse_direction_row](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca40d95f05d0cd4ad3c89465959c58943e)or by[rocsparse_direction_column](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca23355bb7b606c550ba61c781bcecfc5b).**m**–**[in]**number of rows of the sparse CSR matrix.**n**–**[in]**number of columns of the sparse CSR matrix.**csr_descr**–**[in]**descriptor of the sparse CSR matrix. Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**csr_val**–**[in]**array of`nnz`

elements containing the values of the sparse CSR matrix.**csr_row_ptr**–**[in]**integer array containing`m+1`

elements that point to the start of each row of the CSR matrix**csr_col_ind**–**[in]**integer array of the column indices for each non-zero element in the CSR matrix**row_block_dim**–**[in]**the row block dimension of the GEneral BSR matrix. Between 1 and`m`

**col_block_dim**–**[in]**the col block dimension of the GEneral BSR matrix. Between 1 and`n`

**buffer_size**–**[out]**number of bytes of the temporary storage buffer required by[rocsparse_csr2gebsr_nnz](#rocsparse__csr2gebsr_8h_1ae711daa792b64d20adcb394f3931e64c)and[rocsparse_Xcsr2gebsr()](#rocsparse__csr2gebsr_8h_1a68f14b88aabb8289dcdf2f1753a5c838).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`n`

or`row_block_dim`

`col_block_dim`

is invalid.**rocsparse_status_invalid_pointer**–`csr_val`

or`csr_row_ptr`

or`csr_col_ind`

or`buffer_size`

pointer is invalid.



## rocsparse_csr2gebsr()[#](#rocsparse-csr2gebsr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scsr2gebsr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr, const float *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)bsr_descr, float *bsr_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, void *temp_buffer)[#](#_CPPv420rocsparse_scsr2gebsr16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descrPfP13rocsparse_intP13rocsparse_int13rocsparse_int13rocsparse_intPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcsr2gebsr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr, const double *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)bsr_descr, double *bsr_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, void *temp_buffer)[#](#_CPPv420rocsparse_dcsr2gebsr16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descrPdP13rocsparse_intP13rocsparse_int13rocsparse_int13rocsparse_intPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccsr2gebsr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)bsr_descr,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsr_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, void *temp_buffer)[#](#_CPPv420rocsparse_ccsr2gebsr16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descrP23rocsparse_float_complexP13rocsparse_intP13rocsparse_int13rocsparse_int13rocsparse_intPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcsr2gebsr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)bsr_descr,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsr_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, void *temp_buffer)[#](#_CPPv420rocsparse_zcsr2gebsr16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descrP24rocsparse_double_complexP13rocsparse_intP13rocsparse_int13rocsparse_int13rocsparse_intPv) Convert a sparse CSR matrix into a sparse GEneral BSR matrix.

`rocsparse_csr2gebsr`

converts a CSR matrix into a GEneral BSR matrix. It is assumed, that`bsr_val`

,`bsr_col_ind`

and`bsr_row_ptr`

are allocated. Allocation size for`bsr_row_ptr`

is computed as`mb+1`

where`mb`

is the number of block rows and`nb`

is the number of block columns in the GEneral BSR matrix:\[\begin{split} mb = (m + row\_block\_dim - 1) / row\_block\_dim \\ nb = (n + col\_block\_dim - 1) / col\_block\_dim \end{split}\]Allocation size for`bsr_val`

and`bsr_col_ind`

is computed using[rocsparse_csr2bsr_nnz()](#rocsparse__csr2bsr_8h_1a49119cf912b60d0d1ba9eb63c253e6d3)which also fills in`bsr_row_ptr`

.Converting from a sparse CSR matrix to a sparse GEneral BSR matrix requires three steps. First, the user calls

[rocsparse_Xcsr2gebsr_buffer_size()](#rocsparse__csr2gebsr_8h_1a1f1e58605a8acdbc89687982022d1b60)in order to determine the size of the required temporary storage buffer. Once this has been determined, the user allocates this buffer. The user also now allocates the`bsr_row_ptr`

array to have length`mb+1`

and passes this to the function[rocsparse_csr2gebsr_nnz](#rocsparse__csr2gebsr_8h_1ae711daa792b64d20adcb394f3931e64c). This will fill the`bsr_row_ptr`

array and also compute the total number of nonzero blocks in the GEneral BSR matrix. Now that the total number of nonzero blocks is known, the user can allocate the`bsr_col_ind`

and`bsr_val`

arrays. Finally, the user calls`rocsparse_csr2gebsr`

to complete the conversion. See example below.**Example**This example converts a CSR matrix into an BSR matrix.

int main() { // 1 4 0 0 0 0 // A = 0 2 3 0 0 0 // 5 0 0 7 8 0 // 0 0 9 0 6 0 rocsparse_int m = 4; rocsparse_int n = 6; rocsparse_int row_block_dim = 2; rocsparse_int col_block_dim = 3; rocsparse_int nnz = 9; rocsparse_int mb = (m + row_block_dim - 1) / row_block_dim; rocsparse_int nb = (n + col_block_dim - 1) / col_block_dim; rocsparse_direction dir = rocsparse_direction_row; std::vector<rocsparse_int> hcsr_row_ptr = {0, 2, 4, 7, 9}; std::vector<rocsparse_int> hcsr_col_ind = {0, 1, 1, 2, 0, 3, 4, 2, 4}; std::vector<float> hcsr_val = {1, 4, 2, 3, 5, 7, 8, 9, 6}; rocsparse_int* dcsr_row_ptr = nullptr; rocsparse_int* dcsr_col_ind = nullptr; float* dcsr_val = nullptr; HIP_CHECK(hipMalloc((void**)&dcsr_row_ptr, sizeof(rocsparse_int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&dcsr_col_ind, sizeof(rocsparse_int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcsr_val, sizeof(float) * nnz)); HIP_CHECK(hipMemcpy( dcsr_row_ptr, hcsr_row_ptr.data(), sizeof(rocsparse_int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( dcsr_col_ind, hcsr_col_ind.data(), sizeof(rocsparse_int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsr_val, hcsr_val.data(), sizeof(float) * nnz, hipMemcpyHostToDevice)); rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); rocsparse_mat_descr csr_descr; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&csr_descr)); rocsparse_mat_descr bsr_descr; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&bsr_descr)); size_t buffer_size; ROCSPARSE_CHECK(rocsparse_scsr2gebsr_buffer_size(handle, dir, m, n, csr_descr, dcsr_val, dcsr_row_ptr, dcsr_col_ind, row_block_dim, col_block_dim, &buffer_size)); void* buffer = nullptr; HIP_CHECK(hipMalloc((void**)&buffer, buffer_size)); rocsparse_int* dbsr_row_ptr = nullptr; HIP_CHECK(hipMalloc(&dbsr_row_ptr, sizeof(rocsparse_int) * (mb + 1))); rocsparse_int nnzb; ROCSPARSE_CHECK(rocsparse_csr2gebsr_nnz(handle, dir, m, n, csr_descr, dcsr_row_ptr, dcsr_col_ind, bsr_descr, dbsr_row_ptr, row_block_dim, col_block_dim, &nnzb, buffer)); rocsparse_int* dbsr_col_ind = nullptr; float* dbsr_val = nullptr; HIP_CHECK(hipMalloc((void**)&dbsr_col_ind, sizeof(rocsparse_int) * nnzb)); HIP_CHECK(hipMalloc((void**)&dbsr_val, sizeof(float) * nnzb * row_block_dim * col_block_dim)); ROCSPARSE_CHECK(rocsparse_scsr2gebsr(handle, dir, m, n, csr_descr, dcsr_val, dcsr_row_ptr, dcsr_col_ind, bsr_descr, dbsr_val, dbsr_row_ptr, dbsr_col_ind, row_block_dim, col_block_dim, buffer)); HIP_CHECK(hipFree(buffer)); HIP_CHECK(hipFree(dcsr_row_ptr)); HIP_CHECK(hipFree(dcsr_col_ind)); HIP_CHECK(hipFree(dcsr_val)); HIP_CHECK(hipFree(dbsr_row_ptr)); HIP_CHECK(hipFree(dbsr_col_ind)); HIP_CHECK(hipFree(dbsr_val)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(csr_descr)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(bsr_descr)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); return 0; }


Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dir**–**[in]**the storage format of the blocks,[rocsparse_direction_row](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca40d95f05d0cd4ad3c89465959c58943e)or[rocsparse_direction_column](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca23355bb7b606c550ba61c781bcecfc5b)**m**–**[in]**number of rows in the sparse CSR matrix.**n**–**[in]**number of columns in the sparse CSR matrix.**csr_descr**–**[in]**descriptor of the sparse CSR matrix. Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**csr_val**–**[in]**array of`nnz`

elements containing the values of the sparse CSR matrix.**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csr_col_ind**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**bsr_descr**–**[in]**descriptor of the sparse BSR matrix. Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**bsr_val**–**[out]**array of`nnzb*`

`row_block_dim*`

`col_block_dim`

containing the values of the sparse BSR matrix.**bsr_row_ptr**–**[out]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix.**bsr_col_ind**–**[out]**array of`nnzb`

elements containing the block column indices of the sparse BSR matrix.**row_block_dim**–**[in]**row size of the blocks in the sparse GEneral BSR matrix.**col_block_dim**–**[in]**col size of the blocks in the sparse GEneral BSR matrix.**temp_buffer**–**[in]**buffer allocated by the user whose size is determined by calling[rocsparse_Xcsr2gebsr_buffer_size()](#rocsparse__csr2gebsr_8h_1a1f1e58605a8acdbc89687982022d1b60).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`n`

or`row_block_dim`

or`col_block_dim`

is invalid.**rocsparse_status_invalid_pointer**–`bsr_val`

,`bsr_row_ptr`

,`bsr_col_ind`

,`csr_val`

,`csr_row_ptr`

or`csr_col_ind`

pointer is invalid.



## rocsparse_csr2csr_compress()[#](#rocsparse-csr2csr-compress)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scsr2csr_compress([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A, const float *csr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_per_row, float *csr_val_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_C, float tol)[#](#_CPPv427rocsparse_scsr2csr_compress16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_intPK13rocsparse_intPfP13rocsparse_intP13rocsparse_intf)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcsr2csr_compress([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A, const double *csr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_per_row, double *csr_val_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_C, double tol)[#](#_CPPv427rocsparse_dcsr2csr_compress16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_int13rocsparse_intPK13rocsparse_intPdP13rocsparse_intP13rocsparse_intd)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccsr2csr_compress([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_per_row,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_C,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)tol)[#](#_CPPv427rocsparse_ccsr2csr_compress16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_intPK13rocsparse_intP23rocsparse_float_complexP13rocsparse_intP13rocsparse_int23rocsparse_float_complex)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcsr2csr_compress([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_per_row,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_C,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)tol)[#](#_CPPv427rocsparse_zcsr2csr_compress16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_intPK13rocsparse_intP24rocsparse_double_complexP13rocsparse_intP13rocsparse_int24rocsparse_double_complex) Convert a sparse CSR matrix into a compressed sparse CSR matrix.

`rocsparse_csr2csr_compress`

converts a CSR matrix into a compressed CSR matrix by removing entries in the input CSR matrix that are below a non-negative threshold`tol`

Compressing a CSR matrix involves two steps. First we use

[rocsparse_Xnnz_compress()](#rocsparse__nnz__compress_8h_1a3bdb0aca6a9862dc2ba425866c58f2e0)to determine how many entries will be in the final compressed CSR matrix. Then we call`rocsparse_csr2csr_compress`

to finish the compression and fill in the column indices and values arrays of the compressed CSR matrix.**Example**This example demonstrates how to compress a CSR matrix.

int main() { // Initialize rocSPARSE rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // 1 2 0 3 0 // A = 0 4 5 0 0 // 6 0 0 7 8 float tol = 0.0f; rocsparse_int m = 3; rocsparse_int n = 5; rocsparse_int nnz_A = 8; // Define host arrays rocsparse_int h_csr_row_ptr_A[] = {0, 3, 5, 8}; rocsparse_int h_csr_col_ind_A[] = {0, 1, 3, 1, 2, 0, 3, 4}; float h_csr_val_A[] = {1, 0, 3, 4, 0, 6, 7, 0}; // Allocate and initialize device memory for matrix A rocsparse_int* d_csr_row_ptr_A; rocsparse_int* d_csr_col_ind_A; float* d_csr_val_A; HIP_CHECK(hipMalloc((void**)&d_csr_row_ptr_A, sizeof(rocsparse_int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&d_csr_col_ind_A, sizeof(rocsparse_int) * nnz_A)); HIP_CHECK(hipMalloc((void**)&d_csr_val_A, sizeof(float) * nnz_A)); HIP_CHECK(hipMemcpy( d_csr_row_ptr_A, h_csr_row_ptr_A, sizeof(rocsparse_int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( d_csr_col_ind_A, h_csr_col_ind_A, sizeof(rocsparse_int) * nnz_A, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(d_csr_val_A, h_csr_val_A, sizeof(float) * nnz_A, hipMemcpyHostToDevice)); // Allocate memory for the row pointer array of the compressed CSR matrix rocsparse_int* d_csr_row_ptr_C; HIP_CHECK(hipMalloc((void**)&d_csr_row_ptr_C, sizeof(rocsparse_int) * (m + 1))); // Allocate memory for the nnz_per_row array rocsparse_int* d_nnz_per_row; HIP_CHECK(hipMalloc((void**)&d_nnz_per_row, sizeof(rocsparse_int) * m)); rocsparse_mat_descr descr = nullptr; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr)); // Call nnz_compress() which fills in nnz_per_row array and finds the number // of entries that will be in the compressed CSR matrix rocsparse_int nnz_C; ROCSPARSE_CHECK(rocsparse_snnz_compress( handle, m, descr, d_csr_val_A, d_csr_row_ptr_A, d_nnz_per_row, &nnz_C, tol)); // Allocate column indices and values array for the compressed CSR matrix rocsparse_int* d_csr_col_ind_C; float* d_csr_val_C; HIP_CHECK(hipMalloc((void**)&d_csr_col_ind_C, sizeof(rocsparse_int) * nnz_C)); HIP_CHECK(hipMalloc((void**)&d_csr_val_C, sizeof(float) * nnz_C)); // Finish compression by calling csr2csr_compress() ROCSPARSE_CHECK(rocsparse_scsr2csr_compress(handle, m, n, descr, d_csr_val_A, d_csr_row_ptr_A, d_csr_col_ind_A, nnz_A, d_nnz_per_row, d_csr_val_C, d_csr_row_ptr_C, d_csr_col_ind_C, tol)); // Clean up HIP_CHECK(hipFree(d_csr_row_ptr_A)); HIP_CHECK(hipFree(d_csr_col_ind_A)); HIP_CHECK(hipFree(d_csr_val_A)); HIP_CHECK(hipFree(d_csr_row_ptr_C)); HIP_CHECK(hipFree(d_csr_col_ind_C)); HIP_CHECK(hipFree(d_csr_val_C)); HIP_CHECK(hipFree(d_nnz_per_row)); // Destroy rocSPARSE handle ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr)); return 0; }


Note

In the case of complex matrices only the magnitude of the real part of

`tol`

is used.Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix.**n**–**[in]**number of columns of the sparse CSR matrix.**descr_A**–**[in]**matrix descriptor for the CSR matrix**csr_val_A**–**[in]**array of`nnz_A`

elements of the sparse CSR matrix.**csr_row_ptr_A**–**[in]**array of`m+1`

elements that point to the start of every row of the uncompressed sparse CSR matrix.**csr_col_ind_A**–**[in]**array of`nnz_A`

elements containing the column indices of the uncompressed sparse CSR matrix.**nnz_A**–**[in]**number of elements in the column indices and values arrays of the uncompressed sparse CSR matrix.**nnz_per_row**–**[in]**array of length`m`

containing the number of entries that will be kept per row in the final compressed CSR matrix.**csr_val_C**–**[out]**array of`nnz_C`

elements of the compressed sparse CSC matrix.**csr_row_ptr_C**–**[out]**array of`m+1`

elements that point to the start of every column of the compressed sparse CSR matrix.**csr_col_ind_C**–**[out]**array of`nnz_C`

elements containing the row indices of the compressed sparse CSR matrix.**tol**–**[in]**the non-negative tolerance used for compression. If`tol`

is complex then only the magnitude of the real part is used. Entries in the input uncompressed CSR array that are below the tolerance are removed in output compressed CSR matrix.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`n`

or`nnz_A`

is invalid.**rocsparse_status_invalid_value**–`tol`

is invalid.**rocsparse_status_invalid_pointer**–`csr_val_A`

,`csr_row_ptr_A`

,`csr_col_ind_A`

,`csr_val_C`

,`csr_row_ptr_C`

,`csr_col_ind_C`

or`nnz_per_row`

pointer is invalid.



## rocsparse_inverse_permutation()[#](#rocsparse-inverse-permutation)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_inverse_permutation([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*p,[rocsparse_int](types.html#_CPPv413rocsparse_int)*q,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)base)[#](#_CPPv429rocsparse_inverse_permutation16rocsparse_handle13rocsparse_intPK13rocsparse_intP13rocsparse_int20rocsparse_index_base) Inverse a permutation vector.

`rocsparse_inverse_permutation`

computesfor(i = 0; i < n; ++i) { q[p[i]- base] = i + base; }

Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**n**–**[in]**size of the permutation vector`p`

.**p**–**[in]**array of`n`

integers containing the permutation vector to inverse.**q**–**[out]**array of`n`

integers containing the invsrse of the permutation vector.**base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`n`

is invalid.**rocsparse_status_invalid_pointer**–`p`

pointer is invalid or`q`

pointer is invalid.**rocsparse_status_invalid_value**–`base`

is invalid.



## rocsparse_create_identity_permutation()[#](#rocsparse-create-identity-permutation)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_create_identity_permutation([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)*p)[#](#_CPPv437rocsparse_create_identity_permutation16rocsparse_handle13rocsparse_intP13rocsparse_int) Create the identity map.

`rocsparse_create_identity_permutation`

stores the identity map in`p`

, such that \(p = 0:1:(n-1)\).for(i = 0; i < n; ++i) { p[i] = i; }

**Example**The following example creates an identity permutation.

int main() { rocsparse_int size = 200; // Create rocsparse handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Allocate memory to hold the identity map rocsparse_int* perm; HIP_CHECK(hipMalloc((void**)&perm, sizeof(rocsparse_int) * size)); // Fill perm with the identity permutation ROCSPARSE_CHECK(rocsparse_create_identity_permutation(handle, size, perm)); // Clean up HIP_CHECK(hipFree(perm)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**n**–**[in]**size of the map`p`

.**p**–**[out]**array of`n`

integers containing the map.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`n`

is invalid.**rocsparse_status_invalid_pointer**–`p`

pointer is invalid.



## rocsparse_csrsort_buffer_size()[#](#rocsparse-csrsort-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_csrsort_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, size_t *buffer_size)[#](#_CPPv429rocsparse_csrsort_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPK13rocsparse_intPK13rocsparse_intP6size_t) `rocsparse_csrsort_buffer_size`

returns the size of the temporary storage buffer required by[rocsparse_csrsort()](#rocsparse__csrsort_8h_1a8f583b4d048ffb35301a099a062ec33e). The temporary storage buffer must be allocated by the user.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix.**n**–**[in]**number of columns of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csr_col_ind**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**buffer_size**–**[out]**number of bytes of the temporary storage buffer required by[rocsparse_csrsort()](#rocsparse__csrsort_8h_1a8f583b4d048ffb35301a099a062ec33e).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`n`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`csr_row_ptr`

,`csr_col_ind`

or`buffer_size`

pointer is invalid.



## rocsparse_csrsort()[#](#rocsparse-csrsort)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_csrsort([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)*perm, void *temp_buffer)[#](#_CPPv417rocsparse_csrsort16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK13rocsparse_intP13rocsparse_intP13rocsparse_intPv) Sort a sparse CSR matrix.

`rocsparse_csrsort`

sorts a matrix in CSR format. The sorted permutation vector`perm`

can be used to obtain sorted`csr_val`

array. In this case,`perm`

must be initialized as the identity permutation, see[rocsparse_create_identity_permutation()](#rocsparse__inverse__permutation_8h_1a4d7334156f34dcb8136785b3933db13e).`rocsparse_csrsort`

requires extra temporary storage buffer that has to be allocated by the user. Storage buffer size can be determined by[rocsparse_csrsort_buffer_size()](#rocsparse__csrsort_8h_1a8ffe7541f5b4ed8744bd43cf47419cf7).**Example**The following example sorts a \(3 \times 3\) CSR matrix.

int main() { // Initialize rocSPARSE rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // 1 2 3 // A = 4 5 6 // 7 8 9 rocsparse_int m = 3; rocsparse_int n = 3; rocsparse_int nnz = 9; // Define host arrays rocsparse_int h_csr_row_ptr[] = {0, 3, 6, 9}; rocsparse_int h_csr_col_ind[] = {2, 0, 1, 0, 1, 2, 0, 2, 1}; float h_csr_val[] = {3, 1, 2, 4, 5, 6, 7, 9, 8}; // Allocate and initialize device memory for CSR matrix rocsparse_int* d_csr_row_ptr; rocsparse_int* d_csr_col_ind; float* d_csr_val; HIP_CHECK(hipMalloc((void**)&d_csr_row_ptr, sizeof(rocsparse_int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&d_csr_col_ind, sizeof(rocsparse_int) * nnz)); HIP_CHECK(hipMalloc((void**)&d_csr_val, sizeof(float) * nnz)); HIP_CHECK(hipMemcpy( d_csr_row_ptr, h_csr_row_ptr, sizeof(rocsparse_int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( d_csr_col_ind, h_csr_col_ind, sizeof(rocsparse_int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(d_csr_val, h_csr_val, sizeof(float) * nnz, hipMemcpyHostToDevice)); // Create matrix descriptor rocsparse_mat_descr descr; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr)); // Create permutation vector perm as the identity map rocsparse_int* perm; HIP_CHECK(hipMalloc((void**)&perm, sizeof(rocsparse_int) * nnz)); ROCSPARSE_CHECK(rocsparse_create_identity_permutation(handle, nnz, perm)); // Allocate temporary buffer size_t buffer_size; void* temp_buffer; ROCSPARSE_CHECK(rocsparse_csrsort_buffer_size( handle, m, n, nnz, d_csr_row_ptr, d_csr_col_ind, &buffer_size)); HIP_CHECK(hipMalloc(&temp_buffer, buffer_size)); // Sort the CSR matrix ROCSPARSE_CHECK(rocsparse_csrsort( handle, m, n, nnz, descr, d_csr_row_ptr, d_csr_col_ind, perm, temp_buffer)); // Gather sorted csr_val array float* d_csr_val_sorted; HIP_CHECK(hipMalloc((void**)&d_csr_val_sorted, sizeof(float) * nnz)); ROCSPARSE_CHECK( rocsparse_sgthr(handle, nnz, d_csr_val, d_csr_val_sorted, perm, rocsparse_index_base_zero)); // Clean up HIP_CHECK(hipFree(temp_buffer)); HIP_CHECK(hipFree(perm)); HIP_CHECK(hipFree(d_csr_val)); HIP_CHECK(hipFree(d_csr_val_sorted)); HIP_CHECK(hipFree(d_csr_row_ptr)); HIP_CHECK(hipFree(d_csr_col_ind)); // Destroy matrix descriptor and rocSPARSE handle ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); return 0; }


Note

`perm`

can be`NULL`

if a sorted permutation vector is not required.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix.**n**–**[in]**number of columns of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**descr**–**[in]**descriptor of the sparse CSR matrix. Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csr_col_ind**–**[inout]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**perm**–**[inout]**array of`nnz`

integers containing the unsorted map indices, can be`NULL`

.**temp_buffer**–**[in]**temporary storage buffer allocated by the user, size is returned by[rocsparse_csrsort_buffer_size()](#rocsparse__csrsort_8h_1a8ffe7541f5b4ed8744bd43cf47419cf7).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`n`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`csr_row_ptr`

,`csr_col_ind`

or`temp_buffer`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_not_implemented**–[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_cscsort_buffer_size()[#](#rocsparse-cscsort-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cscsort_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_col_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_row_ind, size_t *buffer_size)[#](#_CPPv429rocsparse_cscsort_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPK13rocsparse_intPK13rocsparse_intP6size_t) `rocsparse_cscsort_buffer_size`

returns the size of the temporary storage buffer required by[rocsparse_cscsort()](#rocsparse__cscsort_8h_1ab801c14ee9d57c0971b34933521e6615). The temporary storage buffer must be allocated by the user.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the sparse CSC matrix.**n**–**[in]**number of columns of the sparse CSC matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSC matrix.**csc_col_ptr**–**[in]**array of`n+1`

elements that point to the start of every column of the sparse CSC matrix.**csc_row_ind**–**[in]**array of`nnz`

elements containing the row indices of the sparse CSC matrix.**buffer_size**–**[out]**number of bytes of the temporary storage buffer required by[rocsparse_cscsort()](#rocsparse__cscsort_8h_1ab801c14ee9d57c0971b34933521e6615).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`n`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`csc_col_ptr`

,`csc_row_ind`

or`buffer_size`

pointer is invalid.



## rocsparse_cscsort()[#](#rocsparse-cscsort)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cscsort([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_col_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_row_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)*perm, void *temp_buffer)[#](#_CPPv417rocsparse_cscsort16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK13rocsparse_intP13rocsparse_intP13rocsparse_intPv) Sort a sparse CSC matrix.

`rocsparse_cscsort`

sorts a matrix in CSC format. The sorted permutation vector`perm`

can be used to obtain sorted`csc_val`

array. In this case,`perm`

must be initialized as the identity permutation, see[rocsparse_create_identity_permutation()](#rocsparse__inverse__permutation_8h_1a4d7334156f34dcb8136785b3933db13e).`rocsparse_cscsort`

requires extra temporary storage buffer that has to be allocated by the user. Storage buffer size can be determined by[rocsparse_cscsort_buffer_size()](#rocsparse__cscsort_8h_1a10975d84b3196a42154037436b82a912).**Example**The following example sorts a \(3 \times 3\) CSC matrix.

int main() { // Initialize rocSPARSE rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // 1 2 3 // A = 4 5 6 // 7 8 9 rocsparse_int m = 3; rocsparse_int n = 3; rocsparse_int nnz = 9; // Define host arrays rocsparse_int h_csc_col_ptr[] = {0, 3, 6, 9}; rocsparse_int h_csc_row_ind[] = {2, 0, 1, 0, 1, 2, 0, 2, 1}; float h_csc_val[] = {7, 1, 4, 2, 5, 8, 3, 9, 6}; // Allocate and initialize device memory rocsparse_int* d_csc_col_ptr; rocsparse_int* d_csc_row_ind; float* d_csc_val; HIP_CHECK(hipMalloc((void**)&d_csc_col_ptr, sizeof(rocsparse_int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&d_csc_row_ind, sizeof(rocsparse_int) * nnz)); HIP_CHECK(hipMalloc((void**)&d_csc_val, sizeof(float) * nnz)); HIP_CHECK(hipMemcpy( d_csc_col_ptr, h_csc_col_ptr, sizeof(rocsparse_int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( d_csc_row_ind, h_csc_row_ind, sizeof(rocsparse_int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(d_csc_val, h_csc_val, sizeof(float) * nnz, hipMemcpyHostToDevice)); // Create permutation vector perm as the identity map rocsparse_int* d_perm; HIP_CHECK(hipMalloc((void**)&d_perm, sizeof(rocsparse_int) * nnz)); ROCSPARSE_CHECK(rocsparse_create_identity_permutation(handle, nnz, d_perm)); // Allocate temporary buffer size_t buffer_size; void* d_temp_buffer; ROCSPARSE_CHECK(rocsparse_cscsort_buffer_size( handle, m, n, nnz, d_csc_col_ptr, d_csc_row_ind, &buffer_size)); HIP_CHECK(hipMalloc(&d_temp_buffer, buffer_size)); // Create matrix descriptor rocsparse_mat_descr descr; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr)); // Sort the CSC matrix ROCSPARSE_CHECK(rocsparse_cscsort( handle, m, n, nnz, descr, d_csc_col_ptr, d_csc_row_ind, d_perm, d_temp_buffer)); // Gather sorted csc_val array float* d_csc_val_sorted; HIP_CHECK(hipMalloc((void**)&d_csc_val_sorted, sizeof(float) * nnz)); ROCSPARSE_CHECK(rocsparse_sgthr( handle, nnz, d_csc_val, d_csc_val_sorted, d_perm, rocsparse_index_base_zero)); // Clean up HIP_CHECK(hipFree(d_temp_buffer)); HIP_CHECK(hipFree(d_perm)); HIP_CHECK(hipFree(d_csc_val)); HIP_CHECK(hipFree(d_csc_val_sorted)); HIP_CHECK(hipFree(d_csc_col_ptr)); HIP_CHECK(hipFree(d_csc_row_ind)); // Destroy matrix descriptor and rocSPARSE handle ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); return 0; }


Note

`perm`

can be`NULL`

if a sorted permutation vector is not required.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the sparse CSC matrix.**n**–**[in]**number of columns of the sparse CSC matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSC matrix.**descr**–**[in]**descriptor of the sparse CSC matrix. Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**csc_col_ptr**–**[in]**array of`n+1`

elements that point to the start of every column of the sparse CSC matrix.**csc_row_ind**–**[inout]**array of`nnz`

elements containing the row indices of the sparse CSC matrix.**perm**–**[inout]**array of`nnz`

integers containing the unsorted map indices, can be`NULL`

.**temp_buffer**–**[in]**temporary storage buffer allocated by the user, size is returned by[rocsparse_cscsort_buffer_size()](#rocsparse__cscsort_8h_1a10975d84b3196a42154037436b82a912).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`n`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`csc_col_ptr`

,`csc_row_ind`

or`temp_buffer`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_not_implemented**–[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_coosort_buffer_size()[#](#rocsparse-coosort-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_coosort_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_row_ind, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_col_ind, size_t *buffer_size)[#](#_CPPv429rocsparse_coosort_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPK13rocsparse_intPK13rocsparse_intP6size_t) `rocsparse_coosort_buffer_size`

returns the size of the temporary storage buffer that is required by[rocsparse_coosort_by_row()](#rocsparse__coosort_8h_1a3df99893a1ceb0aae76f89068369a731)and[rocsparse_coosort_by_column()](#rocsparse__coosort_8h_1abff67fda9a8b17eacd36ee2ce37904a2). The temporary storage buffer has to be allocated by the user.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the sparse COO matrix.**n**–**[in]**number of columns of the sparse COO matrix.**nnz**–**[in]**number of non-zero entries of the sparse COO matrix.**coo_row_ind**–**[in]**array of`nnz`

elements containing the row indices of the sparse COO matrix.**coo_col_ind**–**[in]**array of`nnz`

elements containing the column indices of the sparse COO matrix.**buffer_size**–**[out]**number of bytes of the temporary storage buffer required by[rocsparse_coosort_by_row()](#rocsparse__coosort_8h_1a3df99893a1ceb0aae76f89068369a731)and[rocsparse_coosort_by_column()](#rocsparse__coosort_8h_1abff67fda9a8b17eacd36ee2ce37904a2).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`n`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`coo_row_ind`

,`coo_col_ind`

or`buffer_size`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_coosort_by_row()[#](#rocsparse-coosort-by-row)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_coosort_by_row([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz,[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_row_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)*perm, void *temp_buffer)[#](#_CPPv424rocsparse_coosort_by_row16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intP13rocsparse_intP13rocsparse_intP13rocsparse_intPv) Sort a sparse COO matrix by row.

`rocsparse_coosort_by_row`

sorts a matrix in COO format by row. The sorted permutation vector`perm`

can be used to obtain sorted`coo_val`

array. In this case,`perm`

must be initialized as the identity permutation, see[rocsparse_create_identity_permutation()](#rocsparse__inverse__permutation_8h_1a4d7334156f34dcb8136785b3933db13e).`rocsparse_coosort_by_row`

requires extra temporary storage buffer that has to be allocated by the user. Storage buffer size can be determined by[rocsparse_coosort_buffer_size()](#rocsparse__coosort_8h_1a7fb57592e335a86859b4d83c56e25d81).**Example**The following example sorts a \(3 \times 3\) COO matrix by row indices.

int main() { // 1 2 3 // A = 4 5 6 // 7 8 9 rocsparse_int m = 3; rocsparse_int n = 3; rocsparse_int nnz = 9; std::vector<rocsparse_int> hcoo_row_ind = {0, 1, 2, 0, 1, 2, 0, 1, 2}; std::vector<rocsparse_int> hcoo_col_ind = {0, 0, 0, 1, 1, 1, 2, 2, 2}; std::vector<float> hcoo_val = {1, 4, 7, 2, 5, 8, 3, 6, 9}; rocsparse_int* dcoo_row_ind; rocsparse_int* dcoo_col_ind; float* dcoo_val; HIP_CHECK(hipMalloc(&dcoo_row_ind, sizeof(rocsparse_int) * nnz)); HIP_CHECK(hipMalloc(&dcoo_col_ind, sizeof(rocsparse_int) * nnz)); HIP_CHECK(hipMalloc(&dcoo_val, sizeof(float) * nnz)); HIP_CHECK(hipMemcpy( dcoo_row_ind, hcoo_row_ind.data(), sizeof(rocsparse_int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( dcoo_col_ind, hcoo_col_ind.data(), sizeof(rocsparse_int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcoo_val, hcoo_val.data(), sizeof(rocsparse_int) * nnz, hipMemcpyHostToDevice)); // Create rocsparse handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Create permutation vector perm as the identity map rocsparse_int* perm; HIP_CHECK(hipMalloc((void**)&perm, sizeof(rocsparse_int) * nnz)); ROCSPARSE_CHECK(rocsparse_create_identity_permutation(handle, nnz, perm)); // Allocate temporary buffer size_t buffer_size; void* temp_buffer; ROCSPARSE_CHECK( rocsparse_coosort_buffer_size(handle, m, n, nnz, dcoo_row_ind, dcoo_col_ind, &buffer_size)); HIP_CHECK(hipMalloc(&temp_buffer, buffer_size)); // Sort the COO matrix ROCSPARSE_CHECK( rocsparse_coosort_by_row(handle, m, n, nnz, dcoo_row_ind, dcoo_col_ind, perm, temp_buffer)); // Gather sorted coo_val array float* dcoo_val_sorted; HIP_CHECK(hipMalloc((void**)&dcoo_val_sorted, sizeof(float) * nnz)); ROCSPARSE_CHECK( rocsparse_sgthr(handle, nnz, dcoo_val, dcoo_val_sorted, perm, rocsparse_index_base_zero)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); // Clean up HIP_CHECK(hipFree(temp_buffer)); HIP_CHECK(hipFree(perm)); HIP_CHECK(hipFree(dcoo_row_ind)); HIP_CHECK(hipFree(dcoo_col_ind)); HIP_CHECK(hipFree(dcoo_val)); HIP_CHECK(hipFree(dcoo_val_sorted)); return 0; }


Note

`perm`

can be`NULL`

if a sorted permutation vector is not required.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the sparse COO matrix.**n**–**[in]**number of columns of the sparse COO matrix.**nnz**–**[in]**number of non-zero entries of the sparse COO matrix.**coo_row_ind**–**[inout]**array of`nnz`

elements containing the row indices of the sparse COO matrix.**coo_col_ind**–**[inout]**array of`nnz`

elements containing the column indices of the sparse COO matrix.**perm**–**[inout]**array of`nnz`

integers containing the unsorted map indices, can be`NULL`

.**temp_buffer**–**[in]**temporary storage buffer allocated by the user, size is returned by[rocsparse_coosort_buffer_size()](#rocsparse__coosort_8h_1a7fb57592e335a86859b4d83c56e25d81).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`n`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`coo_row_ind`

,`coo_col_ind`

or`temp_buffer`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_coosort_by_column()[#](#rocsparse-coosort-by-column)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_coosort_by_column([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz,[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_row_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)*perm, void *temp_buffer)[#](#_CPPv427rocsparse_coosort_by_column16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intP13rocsparse_intP13rocsparse_intP13rocsparse_intPv) Sort a sparse COO matrix by column.

`rocsparse_coosort_by_column`

sorts a matrix in COO format by column. The sorted permutation vector`perm`

can be used to obtain sorted`coo_val`

array. In this case,`perm`

must be initialized as the identity permutation, see[rocsparse_create_identity_permutation()](#rocsparse__inverse__permutation_8h_1a4d7334156f34dcb8136785b3933db13e).`rocsparse_coosort_by_column`

requires extra temporary storage buffer that has to be allocated by the user. Storage buffer size can be determined by[rocsparse_coosort_buffer_size()](#rocsparse__coosort_8h_1a7fb57592e335a86859b4d83c56e25d81).**Example**The following example sorts a \(3 \times 3\) COO matrix by column indices.

int main() { // 1 2 3 // A = 4 5 6 // 7 8 9 rocsparse_int m = 3; rocsparse_int n = 3; rocsparse_int nnz = 9; rocsparse_int hcoo_row_ind[] = {0, 0, 0, 1, 1, 1, 2, 2, 2}; rocsparse_int hcoo_col_ind[] = {0, 1, 2, 0, 1, 2, 0, 1, 2}; float hcoo_val[] = {1, 2, 3, 4, 5, 6, 7, 8, 9}; // Allocate and initialize device memory rocsparse_int* dcoo_row_ind; rocsparse_int* dcoo_col_ind; float* dcoo_val; HIP_CHECK(hipMalloc((void**)&dcoo_row_ind, sizeof(rocsparse_int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcoo_col_ind, sizeof(rocsparse_int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcoo_val, sizeof(float) * nnz)); HIP_CHECK( hipMemcpy(dcoo_row_ind, hcoo_row_ind, sizeof(rocsparse_int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcoo_col_ind, hcoo_col_ind, sizeof(rocsparse_int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcoo_val, hcoo_val, sizeof(float) * nnz, hipMemcpyHostToDevice)); // Initialize rocSPARSE rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Create permutation vector perm as the identity map rocsparse_int* perm; HIP_CHECK(hipMalloc((void**)&perm, sizeof(rocsparse_int) * nnz)); ROCSPARSE_CHECK(rocsparse_create_identity_permutation(handle, nnz, perm)); // Allocate temporary buffer size_t buffer_size; void* temp_buffer; ROCSPARSE_CHECK( rocsparse_coosort_buffer_size(handle, m, n, nnz, dcoo_row_ind, dcoo_col_ind, &buffer_size)); HIP_CHECK(hipMalloc(&temp_buffer, buffer_size)); // Sort the COO matrix ROCSPARSE_CHECK(rocsparse_coosort_by_column( handle, m, n, nnz, dcoo_row_ind, dcoo_col_ind, perm, temp_buffer)); // Gather sorted coo_val array float* dcoo_val_sorted; HIP_CHECK(hipMalloc((void**)&dcoo_val_sorted, sizeof(float) * nnz)); ROCSPARSE_CHECK( rocsparse_sgthr(handle, nnz, dcoo_val, dcoo_val_sorted, perm, rocsparse_index_base_zero)); // Clean up HIP_CHECK(hipFree(temp_buffer)); HIP_CHECK(hipFree(perm)); HIP_CHECK(hipFree(dcoo_val)); HIP_CHECK(hipFree(dcoo_val_sorted)); HIP_CHECK(hipFree(dcoo_row_ind)); HIP_CHECK(hipFree(dcoo_col_ind)); // Destroy rocSPARSE handle ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); return 0; }


Note

`perm`

can be`NULL`

if a sorted permutation vector is not required.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the sparse COO matrix.**n**–**[in]**number of columns of the sparse COO matrix.**nnz**–**[in]**number of non-zero entries of the sparse COO matrix.**coo_row_ind**–**[inout]**array of`nnz`

elements containing the row indices of the sparse COO matrix.**coo_col_ind**–**[inout]**array of`nnz`

elements containing the column indices of the sparse COO matrix.**perm**–**[inout]**array of`nnz`

integers containing the unsorted map indices, can be`NULL`

.**temp_buffer**–**[in]**temporary storage buffer allocated by the user, size is returned by[rocsparse_coosort_buffer_size()](#rocsparse__coosort_8h_1a7fb57592e335a86859b4d83c56e25d81).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`n`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`coo_row_ind`

,`coo_col_ind`

or`temp_buffer`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_nnz_compress()[#](#rocsparse-nnz-compress)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_snnz_compress([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A, const float *csr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_per_row,[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_C, float tol)[#](#_CPPv423rocsparse_snnz_compress16rocsparse_handle13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intP13rocsparse_intP13rocsparse_intf)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dnnz_compress([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A, const double *csr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_per_row,[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_C, double tol)[#](#_CPPv423rocsparse_dnnz_compress16rocsparse_handle13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intP13rocsparse_intP13rocsparse_intd)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cnnz_compress([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_per_row,[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_C,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)tol)[#](#_CPPv423rocsparse_cnnz_compress16rocsparse_handle13rocsparse_intK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intP13rocsparse_intP13rocsparse_int23rocsparse_float_complex)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_znnz_compress([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_per_row,[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_C,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)tol)[#](#_CPPv423rocsparse_znnz_compress16rocsparse_handle13rocsparse_intK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intP13rocsparse_intP13rocsparse_int24rocsparse_double_complex) Given a sparse CSR matrix and a non-negative tolerance, this function computes how many entries would be left in each row of the matrix if elements less than the tolerance were removed. It also computes the total number of remaining elements in the matrix.

**Example**int main() { // rocSPARSE handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Matrix descriptor rocsparse_mat_descr descr_A; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr_A)); // 1 2 0 3 0 // A = 0 4 5 0 0 // 6 0 0 7 8 float tol = 4.2f; rocsparse_int m = 3; rocsparse_int n = 5; rocsparse_int nnz_A = 8; rocsparse_int hcsr_row_ptr_A[4] = {0, 3, 5, 8}; float hcsr_val_A[8] = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f}; rocsparse_int* dcsr_row_ptr_A = nullptr; float* dcsr_val_A = nullptr; HIP_CHECK(hipMalloc((void**)&dcsr_row_ptr_A, sizeof(rocsparse_int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&dcsr_val_A, sizeof(float) * nnz_A)); HIP_CHECK(hipMemcpy( dcsr_row_ptr_A, hcsr_row_ptr_A, sizeof(rocsparse_int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsr_val_A, hcsr_val_A, sizeof(float) * nnz_A, hipMemcpyHostToDevice)); // Allocate memory for the nnz_per_row array rocsparse_int* dnnz_per_row; HIP_CHECK(hipMalloc((void**)&dnnz_per_row, sizeof(rocsparse_int) * m)); // Call snnz_compress() which fills in nnz_per_row array and finds the number // of entries that will be in the compressed CSR matrix rocsparse_int nnz_C; ROCSPARSE_CHECK(rocsparse_snnz_compress( handle, m, descr_A, dcsr_val_A, dcsr_row_ptr_A, dnnz_per_row, &nnz_C, tol)); // Copy result back to host rocsparse_int hnnz_per_row[3]; HIP_CHECK( hipMemcpy(hnnz_per_row, dnnz_per_row, sizeof(rocsparse_int) * m, hipMemcpyDeviceToHost)); HIP_CHECK(hipFree(dcsr_row_ptr_A)); HIP_CHECK(hipFree(dcsr_val_A)); HIP_CHECK(hipFree(dnnz_per_row)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr_A)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); return 0; }


Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix.**descr_A**–**[in]**the descriptor of the sparse CSR matrix.**csr_val_A**–**[in]**array of`nnz_A`

elements of the sparse CSR matrix.**csr_row_ptr_A**–**[in]**array of`m+1`

elements that point to the start of every row of the uncompressed sparse CSR matrix.**nnz_per_row**–**[out]**array of length`m`

containing the number of entries that will be kept per row in the final compressed CSR matrix.**nnz_C**–**[out]**number of elements in the column indices and values arrays of the compressed sparse CSR matrix. Can be either host or device pointer.**tol**–**[in]**the non-negative tolerance used for compression. If`tol`

is complex then only the magnitude of the real part is used. Entries in the input uncompressed CSR array that are below the tolerance are removed in output compressed CSR matrix.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`n`

is invalid.**rocsparse_status_invalid_value**–`tol`

is invalid.**rocsparse_status_invalid_pointer**–`csr_val_A`

or`csr_row_ptr_A`

or`nnz_per_row`

or`nnz_C`

pointer is invalid.



## rocsparse_nnz()[#](#rocsparse-nnz)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_snnz([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *A,[rocsparse_int](types.html#_CPPv413rocsparse_int)ld,[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_per_row_columns,[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_total_dev_host_ptr)[#](#_CPPv414rocsparse_snnz16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKf13rocsparse_intP13rocsparse_intP13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dnnz([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *A,[rocsparse_int](types.html#_CPPv413rocsparse_int)ld,[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_per_row_columns,[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_total_dev_host_ptr)[#](#_CPPv414rocsparse_dnnz16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKd13rocsparse_intP13rocsparse_intP13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cnnz([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*A,[rocsparse_int](types.html#_CPPv413rocsparse_int)ld,[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_per_row_columns,[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_total_dev_host_ptr)[#](#_CPPv414rocsparse_cnnz16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK23rocsparse_float_complex13rocsparse_intP13rocsparse_intP13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_znnz([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*A,[rocsparse_int](types.html#_CPPv413rocsparse_int)ld,[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_per_row_columns,[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_total_dev_host_ptr)[#](#_CPPv414rocsparse_znnz16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK24rocsparse_double_complex13rocsparse_intP13rocsparse_intP13rocsparse_int) This function computes the number of nonzero elements per row or column and the total number of nonzero elements in a dense matrix.

**Example**int main() { // rocSPARSE handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Matrix descriptor rocsparse_mat_descr descr; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr)); // Dense matrix in column order // 1 2 0 3 0 // A = 0 4 5 0 0 // 6 0 0 7 8 float hdense_A[15] = { 1.0f, 0.0f, 6.0f, 2.0f, 4.0f, 0.0f, 0.0f, 5.0f, 0.0f, 3.0f, 0.0f, 7.0f, 0.0f, 0.0f, 8.0f}; rocsparse_int m = 3; rocsparse_int n = 5; rocsparse_direction dir = rocsparse_direction_row; float* ddense_A = nullptr; HIP_CHECK(hipMalloc((void**)&ddense_A, sizeof(float) * m * n)); HIP_CHECK(hipMemcpy(ddense_A, hdense_A, sizeof(float) * m * n, hipMemcpyHostToDevice)); // Allocate memory for the nnz_per_row_columns array rocsparse_int* dnnz_per_row; HIP_CHECK(hipMalloc((void**)&dnnz_per_row, sizeof(rocsparse_int) * m)); rocsparse_int nnz_A; ROCSPARSE_CHECK(rocsparse_snnz(handle, dir, m, n, descr, ddense_A, m, dnnz_per_row, &nnz_A)); // Copy result back to host rocsparse_int hnnz_per_row[3]; HIP_CHECK( hipMemcpy(hnnz_per_row, dnnz_per_row, sizeof(rocsparse_int) * m, hipMemcpyDeviceToHost)); HIP_CHECK(hipFree(ddense_A)); HIP_CHECK(hipFree(dnnz_per_row)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); return 0; }


Note

The routine does support asynchronous execution if the pointer mode is set to device.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dir**–**[in]**direction that specified whether to count nonzero elements by[rocsparse_direction_row](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca40d95f05d0cd4ad3c89465959c58943e)or by[rocsparse_direction_column](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca23355bb7b606c550ba61c781bcecfc5b).**m**–**[in]**number of rows of the dense matrix`A`

.**n**–**[in]**number of columns of the dense matrix`A`

.**descr**–**[in]**the descriptor of the dense matrix`A`

.**A**–**[in]**array of dimensions (`ld`

,`n`

)**ld**–**[in]**leading dimension of dense array`A`

.**nnz_per_row_columns**–**[out]**array of size`m`

or`n`

containing the number of nonzero elements per row or column, respectively.**nnz_total_dev_host_ptr**–**[out]**total number of nonzero elements in device or host memory.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`n`

or`ld`

is invalid.**rocsparse_status_invalid_pointer**–`A`

or`nnz_per_row_columns`

or`nnz_total_dev_host_ptr`

pointer is invalid.



## rocsparse_dense2csr()[#](#rocsparse-dense2csr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sdense2csr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *A,[rocsparse_int](types.html#_CPPv413rocsparse_int)ld, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_per_rows, float *csr_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind)[#](#_CPPv420rocsparse_sdense2csr16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKf13rocsparse_intPK13rocsparse_intPfP13rocsparse_intP13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ddense2csr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *A,[rocsparse_int](types.html#_CPPv413rocsparse_int)ld, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_per_rows, double *csr_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind)[#](#_CPPv420rocsparse_ddense2csr16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKd13rocsparse_intPK13rocsparse_intPdP13rocsparse_intP13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cdense2csr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*A,[rocsparse_int](types.html#_CPPv413rocsparse_int)ld, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_per_rows,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind)[#](#_CPPv420rocsparse_cdense2csr16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK23rocsparse_float_complex13rocsparse_intPK13rocsparse_intP23rocsparse_float_complexP13rocsparse_intP13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zdense2csr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*A,[rocsparse_int](types.html#_CPPv413rocsparse_int)ld, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_per_rows,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind)[#](#_CPPv420rocsparse_zdense2csr16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK24rocsparse_double_complex13rocsparse_intPK13rocsparse_intP24rocsparse_double_complexP13rocsparse_intP13rocsparse_int) This function converts the matrix \(A\) in column-oriented dense format into a sparse matrix in CSR format. All the parameters are assumed to have been pre-allocated by the user and the arrays are filled in based on nnz_per_row, which can be pre-computed with

[rocsparse_Xnnz()](#rocsparse__nnz_8h_1a5cd8bc28f0080f0700ce5f2b825635df).**Example**int main() { // rocSPARSE handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Matrix descriptor rocsparse_mat_descr descr; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr)); // Column-Oriented Dense matrix in column order // 1 2 0 3 0 // A = 0 4 5 0 0 // 6 0 0 7 8 float hdense_A[15] = { 1.0f, 0.0f, 6.0f, 2.0f, 4.0f, 0.0f, 0.0f, 5.0f, 0.0f, 3.0f, 0.0f, 7.0f, 0.0f, 0.0f, 8.0f}; rocsparse_int m = 3; rocsparse_int n = 5; rocsparse_direction dir = rocsparse_direction_row; float* ddense_A = nullptr; HIP_CHECK(hipMalloc((void**)&ddense_A, sizeof(float) * m * n)); HIP_CHECK(hipMemcpy(ddense_A, hdense_A, sizeof(float) * m * n, hipMemcpyHostToDevice)); // Allocate memory for the nnz_per_row_columns array rocsparse_int* dnnz_per_row; HIP_CHECK(hipMalloc((void**)&dnnz_per_row, sizeof(rocsparse_int) * m)); rocsparse_int nnz_A; ROCSPARSE_CHECK(rocsparse_snnz(handle, dir, m, n, descr, ddense_A, m, dnnz_per_row, &nnz_A)); // Allocate sparse CSR matrix rocsparse_int* dcsr_row_ptr = nullptr; rocsparse_int* dcsr_col_ind = nullptr; float* dcsr_val = nullptr; HIP_CHECK(hipMalloc((void**)&dcsr_row_ptr, sizeof(rocsparse_int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&dcsr_col_ind, sizeof(rocsparse_int) * nnz_A)); HIP_CHECK(hipMalloc((void**)&dcsr_val, sizeof(float) * nnz_A)); ROCSPARSE_CHECK(rocsparse_sdense2csr( handle, m, n, descr, ddense_A, m, dnnz_per_row, dcsr_val, dcsr_row_ptr, dcsr_col_ind)); HIP_CHECK(hipFree(dcsr_row_ptr)); HIP_CHECK(hipFree(dcsr_col_ind)); HIP_CHECK(hipFree(dcsr_val)); HIP_CHECK(hipFree(dnnz_per_row)); rocsparse_destroy_mat_descr(descr); rocsparse_destroy_handle(handle); return 0; }


Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the column-oriented dense matrix`A`

.**n**–**[in]**number of columns of the column-oriented dense dense matrix`A`

.**descr**–**[in]**the descriptor of the column-oriented dense matrix`A`

, the supported matrix type is[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)and also any valid value of the[rocsparse_index_base](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060d).**A**–**[in]**column-oriented dense matrix of dimensions (`ld`

,`n`

)**ld**–**[in]**leading dimension of column-oriented dense matrix`A`

.**nnz_per_rows**–**[in]**array of size`n`

containing the number of non-zero elements per row.**csr_val**–**[out]**array of nnz ( =`csr_row_ptr`

[m] -`csr_row_ptr`

[0] ) nonzero elements of matrix`A`

.**csr_row_ptr**–**[out]**integer array of`m+1`

elements that contains the start of every row and the end of the last row plus one.**csr_col_ind**–**[out]**integer array of nnz ( =`csr_row_ptr`

[m] -`csr_row_ptr`

[0] ) column indices of the non-zero elements of matrix`A`

.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`n`

or`ld`

is invalid.**rocsparse_status_invalid_pointer**–`A`

or`nnz_per_rows`

or`csr_val`

`csr_row_ptr`

or`csr_col_ind`

pointer is invalid.



## rocsparse_dense2csc()[#](#rocsparse-dense2csc)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sdense2csc([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *A,[rocsparse_int](types.html#_CPPv413rocsparse_int)ld, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_per_columns, float *csc_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_col_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_row_ind)[#](#_CPPv420rocsparse_sdense2csc16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKf13rocsparse_intPK13rocsparse_intPfP13rocsparse_intP13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ddense2csc([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *A,[rocsparse_int](types.html#_CPPv413rocsparse_int)ld, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_per_columns, double *csc_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_col_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_row_ind)[#](#_CPPv420rocsparse_ddense2csc16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKd13rocsparse_intPK13rocsparse_intPdP13rocsparse_intP13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cdense2csc([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*A,[rocsparse_int](types.html#_CPPv413rocsparse_int)ld, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_per_columns,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csc_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_col_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_row_ind)[#](#_CPPv420rocsparse_cdense2csc16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK23rocsparse_float_complex13rocsparse_intPK13rocsparse_intP23rocsparse_float_complexP13rocsparse_intP13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zdense2csc([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*A,[rocsparse_int](types.html#_CPPv413rocsparse_int)ld, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_per_columns,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csc_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_col_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_row_ind)[#](#_CPPv420rocsparse_zdense2csc16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK24rocsparse_double_complex13rocsparse_intPK13rocsparse_intP24rocsparse_double_complexP13rocsparse_intP13rocsparse_int) This function converts the matrix \(A\) in column-oriented dense format into a sparse matrix in CSC format. All the parameters are assumed to have been pre-allocated by the user and the arrays are filled in based on nnz_per_columns, which can be pre-computed with

[rocsparse_Xnnz()](#rocsparse__nnz_8h_1a5cd8bc28f0080f0700ce5f2b825635df).**Example**int main() { // Initialize rocSPARSE rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Define a dense matrix int m = 3; int n = 3; rocsparse_direction dir = rocsparse_direction_column; std::vector<float> hdense = {1, 2, 3, 4, 5, 6, 7, 8, 9}; // Allocate device memory for the dense matrix float* ddense; HIP_CHECK(hipMalloc((void**)&ddense, sizeof(float) * m * n)); HIP_CHECK(hipMemcpy(ddense, hdense.data(), sizeof(float) * m * n, hipMemcpyHostToDevice)); // Create matrix descriptor rocsparse_mat_descr descr; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr)); rocsparse_int* dnnz_per_column; HIP_CHECK(hipMalloc(&dnnz_per_column, sizeof(rocsparse_int) * n)); rocsparse_int nnz_A; ROCSPARSE_CHECK(rocsparse_snnz(handle, dir, m, n, descr, ddense, m, dnnz_per_column, &nnz_A)); // Allocate device memory for CSC format rocsparse_int* dcsc_col_ptr; rocsparse_int* dcsc_row_ind; float* dcsc_val; HIP_CHECK(hipMalloc((void**)&dcsc_col_ptr, sizeof(rocsparse_int) * (n + 1))); HIP_CHECK(hipMalloc((void**)&dcsc_row_ind, sizeof(rocsparse_int) * nnz_A)); HIP_CHECK(hipMalloc((void**)&dcsc_val, sizeof(float) * nnz_A)); // Convert dense matrix to CSC format ROCSPARSE_CHECK(rocsparse_sdense2csc( handle, m, n, descr, ddense, m, dnnz_per_column, dcsc_val, dcsc_col_ptr, dcsc_row_ind)); // Copy result back to host std::vector<int> hcsc_col_ptr(n + 1); std::vector<int> hcsc_row_ind(nnz_A); std::vector<float> hcsc_val(nnz_A); HIP_CHECK( hipMemcpy(hcsc_col_ptr.data(), dcsc_col_ptr, sizeof(int) * (n + 1), hipMemcpyDeviceToHost)); HIP_CHECK( hipMemcpy(hcsc_row_ind.data(), dcsc_row_ind, sizeof(int) * nnz_A, hipMemcpyDeviceToHost)); HIP_CHECK(hipMemcpy(hcsc_val.data(), dcsc_val, sizeof(float) * nnz_A, hipMemcpyDeviceToHost)); // Print the CSC matrix std::cout << "CSC format:" << std::endl; for(int i = 0; i < n; ++i) { for(int j = hcsc_col_ptr[i]; j < hcsc_col_ptr[i + 1]; ++j) { std::cout << "Col: " << i << ", Row: " << hcsc_row_ind[j] << ", Val: " << hcsc_val[j] << std::endl; } } // Clean up HIP_CHECK(hipFree(ddense)); HIP_CHECK(hipFree(dnnz_per_column)); HIP_CHECK(hipFree(dcsc_col_ptr)); HIP_CHECK(hipFree(dcsc_row_ind)); HIP_CHECK(hipFree(dcsc_val)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); return 0; }


Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the column-oriented dense matrix`A`

.**n**–**[in]**number of columns of the column-oriented dense matrix`A`

.**descr**–**[in]**the descriptor of the column-oriented dense matrix`A`

, the supported matrix type is[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)and also any valid value of the[rocsparse_index_base](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060d).**A**–**[in]**column-oriented dense matrix of dimensions (`ld`

,`n`

)**ld**–**[in]**leading dimension of the column-oriented dense matrix`A`

.**nnz_per_columns**–**[in]**array of size`n`

containing the number of non-zero elements per column.**csc_val**–**[out]**array of nnz ( =`csc_col_ptr`

[n] -`csc_col_ptr`

[0] ) nonzero elements of matrix`A`

.**csc_col_ptr**–**[out]**integer array of`n+1`

elements that contains the start of every column and the end of the last column plus one.**csc_row_ind**–**[out]**integer array of nnz ( =`csc_col_ptr`

[n] -`csc_col_ptr`

[0] ) column indices of the non-zero elements of matrix`A`

.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`n`

or`ld`

is invalid.**rocsparse_status_invalid_pointer**–`A`

or`nnz_per_columns`

or`csc_val`

`csc_col_ptr`

or`csc_row_ind`

pointer is invalid.



## rocsparse_dense2coo()[#](#rocsparse-dense2coo)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sdense2coo([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *A,[rocsparse_int](types.html#_CPPv413rocsparse_int)ld, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_per_rows, float *coo_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_row_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_col_ind)[#](#_CPPv420rocsparse_sdense2coo16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKf13rocsparse_intPK13rocsparse_intPfP13rocsparse_intP13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ddense2coo([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *A,[rocsparse_int](types.html#_CPPv413rocsparse_int)ld, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_per_rows, double *coo_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_row_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_col_ind)[#](#_CPPv420rocsparse_ddense2coo16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKd13rocsparse_intPK13rocsparse_intPdP13rocsparse_intP13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cdense2coo([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*A,[rocsparse_int](types.html#_CPPv413rocsparse_int)ld, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_per_rows,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*coo_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_row_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_col_ind)[#](#_CPPv420rocsparse_cdense2coo16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK23rocsparse_float_complex13rocsparse_intPK13rocsparse_intP23rocsparse_float_complexP13rocsparse_intP13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zdense2coo([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*A,[rocsparse_int](types.html#_CPPv413rocsparse_int)ld, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_per_rows,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*coo_val,[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_row_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_col_ind)[#](#_CPPv420rocsparse_zdense2coo16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK24rocsparse_double_complex13rocsparse_intPK13rocsparse_intP24rocsparse_double_complexP13rocsparse_intP13rocsparse_int) This function converts the matrix \(A\) in column-oriented dense format into a sparse matrix in COO format. All the parameters are assumed to have been pre-allocated by the user and the arrays are filled in based on nnz_per_rows, which can be pre-computed with

[rocsparse_Xnnz()](#rocsparse__nnz_8h_1a5cd8bc28f0080f0700ce5f2b825635df).**Example**int main() { // Initialize rocSPARSE rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Define a dense matrix // 1 4 7 // A = 2 5 8 // 3 6 9 int m = 3; int n = 3; rocsparse_direction dir = rocsparse_direction_row; std::vector<float> hdense = {1, 2, 3, 4, 5, 6, 7, 8, 9}; // Allocate device memory for the dense matrix float* ddense; HIP_CHECK(hipMalloc((void**)&ddense, sizeof(float) * m * n)); HIP_CHECK(hipMemcpy(ddense, hdense.data(), sizeof(float) * m * n, hipMemcpyHostToDevice)); // Create matrix descriptor rocsparse_mat_descr descr; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr)); rocsparse_int* dnnz_per_row; HIP_CHECK(hipMalloc(&dnnz_per_row, sizeof(rocsparse_int) * m)); rocsparse_int nnz_A; ROCSPARSE_CHECK(rocsparse_snnz(handle, dir, m, n, descr, ddense, m, dnnz_per_row, &nnz_A)); // Allocate device memory for COO format rocsparse_int* dcoo_row_ind; rocsparse_int* dcoo_col_ind; float* dcoo_val; HIP_CHECK(hipMalloc(&dcoo_row_ind, sizeof(rocsparse_int) * nnz_A)); HIP_CHECK(hipMalloc(&dcoo_col_ind, sizeof(rocsparse_int) * nnz_A)); HIP_CHECK(hipMalloc(&dcoo_val, sizeof(float) * nnz_A)); // Convert dense matrix to COO format ROCSPARSE_CHECK(rocsparse_sdense2coo( handle, m, n, descr, ddense, m, dnnz_per_row, dcoo_val, dcoo_row_ind, dcoo_col_ind)); // Copy result back to host std::vector<int> hcoo_row_ind(nnz_A); std::vector<int> hcoo_col_ind(nnz_A); std::vector<float> hcoo_val(nnz_A); HIP_CHECK( hipMemcpy(hcoo_row_ind.data(), dcoo_row_ind, sizeof(int) * nnz_A, hipMemcpyDeviceToHost)); HIP_CHECK( hipMemcpy(hcoo_col_ind.data(), dcoo_col_ind, sizeof(int) * nnz_A, hipMemcpyDeviceToHost)); HIP_CHECK(hipMemcpy(hcoo_val.data(), dcoo_val, sizeof(float) * nnz_A, hipMemcpyDeviceToHost)); // Print the COO matrix std::cout << "COO format:" << std::endl; for(int i = 0; i < nnz_A; ++i) { std::cout << "Row: " << hcoo_row_ind[i] << ", Col: " << hcoo_col_ind[i] << ", Val: " << hcoo_val[i] << std::endl; } // Clean up HIP_CHECK(hipFree(ddense)); HIP_CHECK(hipFree(dnnz_per_row)); HIP_CHECK(hipFree(dcoo_row_ind)); HIP_CHECK(hipFree(dcoo_col_ind)); HIP_CHECK(hipFree(dcoo_val)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); return 0; }


Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the column-oriented dense matrix`A`

.**n**–**[in]**number of columns of the column-oriented dense matrix`A`

.**descr**–**[in]**the descriptor of the column-oriented dense matrix`A`

, the supported matrix type is[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)and also any valid value of the[rocsparse_index_base](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060d).**A**–**[in]**column-oriented dense matrix of dimensions (`ld`

,`n`

)**ld**–**[in]**leading dimension of column-oriented dense matrix`A`

.**nnz_per_rows**–**[in]**array of size`n`

containing the number of non-zero elements per row.**coo_val**–**[out]**array of nnz nonzero elements of matrix`A`

.**coo_row_ind**–**[out]**integer array of nnz row indices of the non-zero elements of matrix`A`

.**coo_col_ind**–**[out]**integer array of nnz column indices of the non-zero elements of matrix`A`

.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`n`

or`ld`

is invalid.**rocsparse_status_invalid_pointer**–`A`

or`nnz_per_rows`

or`coo_val`

`coo_col_ind`

or`coo_row_ind`

pointer is invalid.



## rocsparse_csr2dense()[#](#rocsparse-csr2dense)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scsr2dense([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, float *A,[rocsparse_int](types.html#_CPPv413rocsparse_int)ld)[#](#_CPPv420rocsparse_scsr2dense16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intPf13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcsr2dense([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, double *A,[rocsparse_int](types.html#_CPPv413rocsparse_int)ld)[#](#_CPPv420rocsparse_dcsr2dense16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_intPd13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccsr2dense([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*A,[rocsparse_int](types.html#_CPPv413rocsparse_int)ld)[#](#_CPPv420rocsparse_ccsr2dense16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_intP23rocsparse_float_complex13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcsr2dense([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*A,[rocsparse_int](types.html#_CPPv413rocsparse_int)ld)[#](#_CPPv420rocsparse_zcsr2dense16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_intP24rocsparse_double_complex13rocsparse_int) This function converts the sparse matrix in CSR format into a column-oriented dense matrix.

**Example**int main() { // 1 2 3 0 // 0 0 4 5 // 0 6 0 0 // 7 0 0 8 rocsparse_int m = 4; rocsparse_int n = 4; rocsparse_int nnz = 8; rocsparse_int ld = m; std::vector<rocsparse_int> hcsr_row_ptr = {0, 3, 5, 6, 8}; std::vector<rocsparse_int> hcsr_col_ind = {0, 1, 2, 2, 3, 1, 0, 3}; std::vector<float> hcsr_val = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f}; rocsparse_int* dcsr_row_ptr = nullptr; rocsparse_int* dcsr_col_ind = nullptr; float* dcsr_val = nullptr; HIP_CHECK(hipMalloc((void**)&dcsr_row_ptr, sizeof(rocsparse_int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&dcsr_col_ind, sizeof(rocsparse_int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcsr_val, sizeof(float) * nnz)); HIP_CHECK(hipMemcpy( dcsr_row_ptr, hcsr_row_ptr.data(), sizeof(rocsparse_int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( dcsr_col_ind, hcsr_col_ind.data(), sizeof(rocsparse_int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsr_val, hcsr_val.data(), sizeof(float) * nnz, hipMemcpyHostToDevice)); float* ddense = nullptr; HIP_CHECK(hipMalloc((void**)&ddense, sizeof(float) * ld * n)); rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); rocsparse_mat_descr descr; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr)); ROCSPARSE_CHECK(rocsparse_scsr2dense( handle, m, n, descr, dcsr_val, dcsr_row_ptr, dcsr_col_ind, ddense, ld)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr)); HIP_CHECK(hipFree(dcsr_row_ptr)); HIP_CHECK(hipFree(dcsr_col_ind)); HIP_CHECK(hipFree(dcsr_val)); HIP_CHECK(hipFree(ddense)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the column-oriented dense matrix`A`

.**n**–**[in]**number of columns of the column-oriented dense matrix`A`

.**descr**–**[in]**the descriptor of the column-oriented dense matrix`A`

, the supported matrix type is[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)and also any valid value of the[rocsparse_index_base](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060d).**csr_val**–**[in]**array of nnz ( =`csr_row_ptr`

[m] -`csr_row_ptr`

[0] ) nonzero elements of matrix`A`

.**csr_row_ptr**–**[in]**integer array of`m+1`

elements that contains the start of every row and the end of the last row plus one.**csr_col_ind**–**[in]**integer array of nnz ( =`csr_row_ptr`

[m] -`csr_row_ptr`

[0] ) column indices of the non-zero elements of matrix`A`

.**A**–**[out]**array of dimensions (`ld`

,`n`

)**ld**–**[out]**leading dimension of column-oriented dense matrix`A`

.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`n`

or`ld`

is invalid.**rocsparse_status_invalid_pointer**–`A`

or`csr_val`

`csr_row_ptr`

or`csr_col_ind`

pointer is invalid.



## rocsparse_csc2dense()[#](#rocsparse-csc2dense)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scsc2dense([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *csc_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_col_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_row_ind, float *A,[rocsparse_int](types.html#_CPPv413rocsparse_int)ld)[#](#_CPPv420rocsparse_scsc2dense16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intPf13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcsc2dense([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *csc_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_col_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_row_ind, double *A,[rocsparse_int](types.html#_CPPv413rocsparse_int)ld)[#](#_CPPv420rocsparse_dcsc2dense16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_intPd13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccsc2dense([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csc_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_col_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_row_ind,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*A,[rocsparse_int](types.html#_CPPv413rocsparse_int)ld)[#](#_CPPv420rocsparse_ccsc2dense16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_intP23rocsparse_float_complex13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcsc2dense([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csc_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_col_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_row_ind,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*A,[rocsparse_int](types.html#_CPPv413rocsparse_int)ld)[#](#_CPPv420rocsparse_zcsc2dense16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_intP24rocsparse_double_complex13rocsparse_int) This function converts the sparse matrix in CSC format into a column-oriented dense matrix.

**Example**int main() { // 1 2 3 0 // 0 0 4 5 // 0 6 0 0 // 7 0 0 8 rocsparse_int m = 4; rocsparse_int n = 4; rocsparse_int nnz = 8; rocsparse_int ld = m; std::vector<rocsparse_int> hcsc_col_ptr = {0, 2, 4, 6, 8}; std::vector<rocsparse_int> hcsc_row_ind = {0, 3, 0, 2, 0, 1, 1, 3}; std::vector<float> hcsc_val = {1.0f, 7.0f, 2.0f, 6.0f, 3.0f, 4.0f, 5.0f, 8.0f}; rocsparse_int* dcsc_col_ptr = nullptr; rocsparse_int* dcsc_row_ind = nullptr; float* dcsc_val = nullptr; HIP_CHECK(hipMalloc((void**)&dcsc_col_ptr, sizeof(rocsparse_int) * (n + 1))); HIP_CHECK(hipMalloc((void**)&dcsc_row_ind, sizeof(rocsparse_int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcsc_val, sizeof(float) * nnz)); HIP_CHECK(hipMemcpy( dcsc_col_ptr, hcsc_col_ptr.data(), sizeof(rocsparse_int) * (n + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( dcsc_row_ind, hcsc_row_ind.data(), sizeof(rocsparse_int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsc_val, hcsc_val.data(), sizeof(float) * nnz, hipMemcpyHostToDevice)); float* ddense = nullptr; HIP_CHECK(hipMalloc((void**)&ddense, sizeof(float) * ld * n)); rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); rocsparse_mat_descr descr; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr)); ROCSPARSE_CHECK(rocsparse_scsc2dense( handle, m, n, descr, dcsc_val, dcsc_col_ptr, dcsc_row_ind, ddense, ld)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr)); HIP_CHECK(hipFree(dcsc_col_ptr)); HIP_CHECK(hipFree(dcsc_row_ind)); HIP_CHECK(hipFree(dcsc_val)); HIP_CHECK(hipFree(ddense)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the column-oriented dense matrix`A`

.**n**–**[in]**number of columns of the column-oriented dense matrix`A`

.**descr**–**[in]**the descriptor of the column-oriented dense matrix`A`

, the supported matrix type is[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)and also any valid value of the[rocsparse_index_base](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060d).**csc_val**–**[in]**array of nnz ( =`csc_col_ptr`

[n] -`csc_col_ptr`

[0] ) nonzero elements of matrix`A`

.**csc_col_ptr**–**[in]**integer array of`n+1`

elements that contains the start of every column and the end of the last column plus one.**csc_row_ind**–**[in]**integer array of nnz ( =`csc_col_ptr`

[n] -`csc_col_ptr`

[0] ) column indices of the non-zero elements of matrix`A`

.**A**–**[out]**array of dimensions (`ld`

,`n`

)**ld**–**[out]**leading dimension of column-oriented dense matrix`A`

.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`n`

or`ld`

is invalid.**rocsparse_status_invalid_pointer**–`A`

or`csc_val`

`csc_col_ptr`

or`csc_row_ind`

pointer is invalid.



## rocsparse_coo2dense()[#](#rocsparse-coo2dense)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scoo2dense([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *coo_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_row_ind, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_col_ind, float *A,[rocsparse_int](types.html#_CPPv413rocsparse_int)ld)[#](#_CPPv420rocsparse_scoo2dense16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intPf13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcoo2dense([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *coo_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_row_ind, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_col_ind, double *A,[rocsparse_int](types.html#_CPPv413rocsparse_int)ld)[#](#_CPPv420rocsparse_dcoo2dense16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_intPd13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccoo2dense([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*coo_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_row_ind, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_col_ind,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*A,[rocsparse_int](types.html#_CPPv413rocsparse_int)ld)[#](#_CPPv420rocsparse_ccoo2dense16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_intP23rocsparse_float_complex13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcoo2dense([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*coo_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_row_ind, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_col_ind,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*A,[rocsparse_int](types.html#_CPPv413rocsparse_int)ld)[#](#_CPPv420rocsparse_zcoo2dense16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_intP24rocsparse_double_complex13rocsparse_int) This function converts the sparse matrix in COO format into a column-oriented dense matrix.

**Example**int main() { // 1 2 3 0 // 0 0 4 5 // 0 6 0 0 // 7 0 0 8 rocsparse_int m = 4; rocsparse_int n = 4; rocsparse_int nnz = 8; rocsparse_int ld = m; std::vector<rocsparse_int> hcoo_row_ind = {0, 0, 0, 1, 1, 2, 3, 3}; std::vector<rocsparse_int> hcoo_col_ind = {0, 1, 2, 2, 3, 1, 0, 3}; std::vector<float> hcoo_val = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f}; rocsparse_int* dcoo_row_ind = nullptr; rocsparse_int* dcoo_col_ind = nullptr; float* dcoo_val = nullptr; HIP_CHECK(hipMalloc((void**)&dcoo_row_ind, sizeof(rocsparse_int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcoo_col_ind, sizeof(rocsparse_int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcoo_val, sizeof(float) * nnz)); HIP_CHECK(hipMemcpy( dcoo_row_ind, hcoo_row_ind.data(), sizeof(rocsparse_int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( dcoo_col_ind, hcoo_col_ind.data(), sizeof(rocsparse_int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcoo_val, hcoo_val.data(), sizeof(float) * nnz, hipMemcpyHostToDevice)); float* ddense = nullptr; HIP_CHECK(hipMalloc((void**)&ddense, sizeof(float) * ld * n)); rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); rocsparse_mat_descr descr; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr)); ROCSPARSE_CHECK(rocsparse_scoo2dense( handle, m, n, nnz, descr, dcoo_val, dcoo_row_ind, dcoo_col_ind, ddense, ld)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr)); HIP_CHECK(hipFree(dcoo_row_ind)); HIP_CHECK(hipFree(dcoo_col_ind)); HIP_CHECK(hipFree(dcoo_val)); HIP_CHECK(hipFree(ddense)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the column-oriented dense matrix`A`

.**n**–**[in]**number of columns of the column-oriented dense matrix`A`

.**nnz**–**[in]**number of non-zero entries of the sparse COO matrix.**descr**–**[in]**the descriptor of the column-oriented dense matrix`A`

, the supported matrix type is[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)and also any valid value of the[rocsparse_index_base](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060d).**coo_val**–**[in]**array of nnz nonzero elements of matrix`A`

.**coo_row_ind**–**[in]**integer array of nnz row indices of the non-zero elements of matrix`A`

.**coo_col_ind**–**[in]**integer array of nnz column indices of the non-zero elements of matrix`A`

.**A**–**[out]**array of dimensions (`ld`

,`n`

)**ld**–**[out]**leading dimension of column-oriented dense matrix`A`

.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`n`

or`nnz`

or`ld`

is invalid.**rocsparse_status_invalid_pointer**–`A`

or`coo_val`

`coo_col_ind`

or`coo_row_ind`

pointer is invalid.



## rocsparse_prune_dense2csr_buffer_size()[#](#rocsparse-prune-dense2csr-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sprune_dense2csr_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const float *A,[rocsparse_int](types.html#_CPPv413rocsparse_int)lda, const float *threshold, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, size_t *buffer_size)[#](#_CPPv438rocsparse_sprune_dense2csr_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_intPKf13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dprune_dense2csr_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const double *A,[rocsparse_int](types.html#_CPPv413rocsparse_int)lda, const double *threshold, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, size_t *buffer_size)[#](#_CPPv438rocsparse_dprune_dense2csr_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_intPKd13rocsparse_intPKdK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_intP6size_t) `rocsparse_prune_dense2csr_buffer_size`

returns the size of the temporary buffer that is required by[rocsparse_Xprune_dense2csr_nnz()](#rocsparse__prune__dense2csr_8h_1a1ccbfda7195c022a9f09c5529a0510eb)and[rocsparse_Xprune_dense2csr()](#rocsparse__prune__dense2csr_8h_1afac8859947829464c6223a5731ef1aa8). The temporary storage buffer must be allocated by the user.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the dense matrix`A`

.**n**–**[in]**number of columns of the dense matrix`A`

.**A**–**[in]**array of dimensions (`lda`

,`n`

)**lda**–**[in]**leading dimension of dense array`A`

.**threshold**–**[in]**pointer to the pruning non-negative threshold which can exist in either host or device memory.**descr**–**[in]**the descriptor of the dense matrix`A`

, the supported matrix type is[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)and also any valid value of the[rocsparse_index_base](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060d).**csr_val**–**[in]**array of nnz ( =`csr_row_ptr`

[m] -`csr_row_ptr`

[0] ) nonzero elements of matrix`A`

.**csr_row_ptr**–**[in]**integer array of`m+1`

elements that contains the start of every row and the end of the last row plus one.**csr_col_ind**–**[in]**integer array of nnz ( =`csr_row_ptr`

[m] -`csr_row_ptr`

[0] ) column indices of the non-zero elements of matrix`A`

.**buffer_size**–**[out]**number of bytes of the temporary storage buffer required by[rocsparse_Xprune_dense2csr_nnz()](#rocsparse__prune__dense2csr_8h_1a1ccbfda7195c022a9f09c5529a0510eb)and[rocsparse_Xprune_dense2csr()](#rocsparse__prune__dense2csr_8h_1afac8859947829464c6223a5731ef1aa8).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`buffer_size`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_prune_dense2csr_nnz()[#](#rocsparse-prune-dense2csr-nnz)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sprune_dense2csr_nnz([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const float *A,[rocsparse_int](types.html#_CPPv413rocsparse_int)lda, const float *threshold, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_total_dev_host_ptr, void *temp_buffer)[#](#_CPPv430rocsparse_sprune_dense2csr_nnz16rocsparse_handle13rocsparse_int13rocsparse_intPKf13rocsparse_intPKfK19rocsparse_mat_descrP13rocsparse_intP13rocsparse_intPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dprune_dense2csr_nnz([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const double *A,[rocsparse_int](types.html#_CPPv413rocsparse_int)lda, const double *threshold, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_total_dev_host_ptr, void *temp_buffer)[#](#_CPPv430rocsparse_dprune_dense2csr_nnz16rocsparse_handle13rocsparse_int13rocsparse_intPKd13rocsparse_intPKdK19rocsparse_mat_descrP13rocsparse_intP13rocsparse_intPv) `rocsparse_prune_dense2csr_nnz`

computes the number of nonzero elements per row and the total number of nonzero elements in a sparse CSR matrix once elements less than the threshold are pruned from the matrix.Note

The routine does support asynchronous execution if the pointer mode is set to device.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the dense matrix`A`

.**n**–**[in]**number of columns of the dense matrix`A`

.**A**–**[in]**array of dimensions (`lda`

,`n`

)**lda**–**[in]**leading dimension of dense array`A`

.**threshold**–**[in]**pointer to the pruning non-negative threshold which can exist in either host or device memory.**descr**–**[in]**the descriptor of the dense matrix`A`

.**csr_row_ptr**–**[out]**integer array of`m+1`

elements that contains the start of every row and the end of the last row plus one.**nnz_total_dev_host_ptr**–**[out]**total number of nonzero elements in device or host memory.**temp_buffer**–**[out]**buffer allocated by the user whose size is determined by calling[rocsparse_Xprune_dense2csr_buffer_size()](#rocsparse__prune__dense2csr_8h_1ad5db15c51c167e6e398bb6099d654e5a).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`n`

or`lda`

is invalid.**rocsparse_status_invalid_pointer**–`A`

or`threshold`

or`descr`

or`csr_row_ptr`

or`nnz_total_dev_host_ptr`

or`temp_buffer`

pointer is invalid.



## rocsparse_prune_dense2csr()[#](#rocsparse-prune-dense2csr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sprune_dense2csr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const float *A,[rocsparse_int](types.html#_CPPv413rocsparse_int)lda, const float *threshold, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, float *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, void *temp_buffer)[#](#_CPPv426rocsparse_sprune_dense2csr16rocsparse_handle13rocsparse_int13rocsparse_intPKf13rocsparse_intPKfK19rocsparse_mat_descrPfPK13rocsparse_intP13rocsparse_intPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dprune_dense2csr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const double *A,[rocsparse_int](types.html#_CPPv413rocsparse_int)lda, const double *threshold, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, double *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, void *temp_buffer)[#](#_CPPv426rocsparse_dprune_dense2csr16rocsparse_handle13rocsparse_int13rocsparse_intPKd13rocsparse_intPKdK19rocsparse_mat_descrPdPK13rocsparse_intP13rocsparse_intPv) Convert and prune dense matrix \(A\) into a sparse CSR matrix \(C\).

This function converts the dense matrix \(A\) into a sparse CSR matrix \(C\) by pruning values in \(A\) that are less than a threshold.

The conversion involves three steps. The user first calls

[rocsparse_Xprune_dense2csr_buffer_size()](#rocsparse__prune__dense2csr_8h_1ad5db15c51c167e6e398bb6099d654e5a)to determine the size of the temporary storage buffer. The user allocates this buffer as well as the array`csr_row_ptr`

to have`m+1`

elements. The user then calls[rocsparse_Xprune_dense2csr_nnz()](#rocsparse__prune__dense2csr_8h_1a1ccbfda7195c022a9f09c5529a0510eb)which fills in the`csr_row_ptr`

array and stores the number of elements that are larger than the pruning`threshold`

in`nnz_total_dev_host_ptr`

. Now that the number of nonzeros larger than the pruning`threshold`

is known, the user uses this information to allocate the`csr_col_ind`

and`csr_val`

arrays and then calls`rocsparse_prune_dense2csr`

to complete the conversion. Once the conversion is complete, the temporary storage buffer can be freed.**Example**int main() { // 1 2 0 7 // A = 3 0 0 4 // 5 6 0 4 // 0 4 2 5 rocsparse_int m = 4; rocsparse_int n = 4; rocsparse_int lda = m; float threshold = 3.0f; std::vector<float> hdense = {1.0f, 3.0f, 5.0f, 0.0f, 2.0f, 0.0f, 6.0f, 4.0f, 0.0f, 0.0f, 0.0f, 2.0f, 7.0f, 4.0f, 4.0f, 5.0f}; rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); rocsparse_mat_descr descr; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr)); rocsparse_mat_info info; ROCSPARSE_CHECK(rocsparse_create_mat_info(&info)); float* ddense = nullptr; HIP_CHECK(hipMalloc((void**)&ddense, sizeof(float) * lda * n)); HIP_CHECK(hipMemcpy(ddense, hdense.data(), sizeof(float) * lda * n, hipMemcpyHostToDevice)); rocsparse_int* dcsr_row_ptr = nullptr; HIP_CHECK(hipMalloc((void**)&dcsr_row_ptr, sizeof(rocsparse_int) * (m + 1))); // Obtain the temporary buffer size size_t buffer_size; ROCSPARSE_CHECK(rocsparse_sprune_dense2csr_buffer_size(handle, m, n, ddense, lda, &threshold, descr, nullptr, dcsr_row_ptr, nullptr, &buffer_size)); // Allocate temporary buffer void* temp_buffer; HIP_CHECK(hipMalloc(&temp_buffer, buffer_size)); rocsparse_int nnz; ROCSPARSE_CHECK(rocsparse_sprune_dense2csr_nnz( handle, m, n, ddense, lda, &threshold, descr, dcsr_row_ptr, &nnz, temp_buffer)); rocsparse_int* dcsr_col_ind = nullptr; float* dcsr_val = nullptr; HIP_CHECK(hipMalloc((void**)&dcsr_col_ind, sizeof(rocsparse_int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcsr_val, sizeof(float) * nnz)); ROCSPARSE_CHECK(rocsparse_sprune_dense2csr(handle, m, n, ddense, lda, &threshold, descr, dcsr_val, dcsr_row_ptr, dcsr_col_ind, temp_buffer)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr)); ROCSPARSE_CHECK(rocsparse_destroy_mat_info(info)); HIP_CHECK(hipFree(temp_buffer)); HIP_CHECK(hipFree(ddense)); HIP_CHECK(hipFree(dcsr_row_ptr)); HIP_CHECK(hipFree(dcsr_col_ind)); HIP_CHECK(hipFree(dcsr_val)); return 0; }


Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the dense matrix`A`

.**n**–**[in]**number of columns of the dense matrix`A`

.**A**–**[in]**array of dimensions (`lda`

,`n`

)**lda**–**[in]**leading dimension of dense array`A`

.**threshold**–**[in]**pointer to the non-negative pruning threshold which can exist in either host or device memory.**descr**–**[in]**the descriptor of the dense matrix`A`

, the supported matrix type is[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)and also any valid value of the[rocsparse_index_base](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060d).**csr_val**–**[out]**array of nnz ( =`csr_row_ptr`

[m] -`csr_row_ptr`

[0] ) nonzero elements of matrix`A`

.**csr_row_ptr**–**[in]**integer array of`m+1`

elements that contains the start of every row and the end of the last row plus one.**csr_col_ind**–**[out]**integer array of nnz ( =`csr_row_ptr`

[m] -`csr_row_ptr`

[0] ) column indices of the non-zero elements of matrix`A`

.**temp_buffer**–**[in]**temporary storage buffer allocated by the user, size is returned by[rocsparse_Xprune_dense2csr_buffer_size()](#rocsparse__prune__dense2csr_8h_1ad5db15c51c167e6e398bb6099d654e5a).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`n`

or`lda`

is invalid.**rocsparse_status_invalid_pointer**–`A`

or`descr`

or`threshold`

or`csr_val`

or`csr_row_ptr`

or`csr_col_ind`

or`temp_buffer`

pointer is invalid.



## rocsparse_prune_csr2csr_buffer_size()[#](#rocsparse-prune-csr2csr-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sprune_csr2csr_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr_A, const float *csr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_A, const float *threshold, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr_C, const float *csr_val_C, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_C, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_C, size_t *buffer_size)[#](#_CPPv436rocsparse_sprune_csr2csr_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dprune_csr2csr_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr_A, const double *csr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_A, const double *threshold, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr_C, const double *csr_val_C, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_C, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_C, size_t *buffer_size)[#](#_CPPv436rocsparse_dprune_csr2csr_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_intPKdK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_intP6size_t) `rocsparse_prune_csr2csr_buffer_size`

returns the size of the temporary buffer that is required by[rocsparse_Xprune_csr2csr_nnz()](#rocsparse__prune__csr2csr_8h_1a9029c79f7e01fae3587c3513035ed653)and[rocsparse_Xprune_csr2csr()](#rocsparse__prune__csr2csr_8h_1a964f74e36a52e0d2c4c251fc9ec3c7e6). The temporary storage buffer must be allocated by the user.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows in the sparse CSR matrix.**n**–**[in]**number of columns in the sparse CSR matrix.**nnz_A**–**[in]**number of non-zeros in the sparse CSR matrix \(A\).**csr_descr_A**–**[in]**descriptor of the sparse CSR matrix \(A\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**csr_val_A**–**[in]**array of`nnz_A`

elements containing the values of the sparse CSR matrix \(A\).**csr_row_ptr_A**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(A\).**csr_col_ind_A**–**[in]**array of`nnz_A`

elements containing the column indices of the sparse CSR matrix \(A\).**threshold**–**[in]**pointer to the non-negative pruning threshold which can exist in either host or device memory.**csr_descr_C**–**[in]**descriptor of the sparse CSR matrix \(C\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**csr_val_C**–**[in]**array of`nnz_C`

elements containing the values of the sparse CSR matrix \(C\).**csr_row_ptr_C**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(C\).**csr_col_ind_C**–**[in]**array of`nnz_C`

elements containing the column indices of the sparse CSR matrix \(C\).**buffer_size**–**[out]**number of bytes of the temporary storage buffer required by[rocsparse_Xprune_csr2csr_nnz()](#rocsparse__prune__csr2csr_8h_1a9029c79f7e01fae3587c3513035ed653)and[rocsparse_Xprune_csr2csr()](#rocsparse__prune__csr2csr_8h_1a964f74e36a52e0d2c4c251fc9ec3c7e6).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`buffer_size`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_prune_csr2csr_nnz()[#](#rocsparse-prune-csr2csr-nnz)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sprune_csr2csr_nnz([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr_A, const float *csr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_A, const float *threshold, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_total_dev_host_ptr, void *temp_buffer)[#](#_CPPv428rocsparse_sprune_csr2csr_nnz16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intPKfK19rocsparse_mat_descrP13rocsparse_intP13rocsparse_intPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dprune_csr2csr_nnz([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr_A, const double *csr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_A, const double *threshold, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_total_dev_host_ptr, void *temp_buffer)[#](#_CPPv428rocsparse_dprune_csr2csr_nnz16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_intPKdK19rocsparse_mat_descrP13rocsparse_intP13rocsparse_intPv) `rocsparse_prune_csr2csr_nnz`

computes the number of nonzero elements per row and the total number of nonzero elements in a sparse CSR matrix once elements less than the threshold are pruned from the matrix.Note

The routine does support asynchronous execution if the pointer mode is set to device.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows in the sparse CSR matrix.**n**–**[in]**number of columns in the sparse CSR matrix.**nnz_A**–**[in]**number of non-zeros in the sparse CSR matrix \(A\).**csr_descr_A**–**[in]**descriptor of the sparse CSR matrix \(A\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**csr_val_A**–**[in]**array of`nnz_A`

elements containing the values of the sparse CSR matrix \(A\).**csr_row_ptr_A**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(A\).**csr_col_ind_A**–**[in]**array of`nnz_A`

elements containing the column indices of the sparse CSR matrix \(A\).**threshold**–**[in]**pointer to the non-negative pruning threshold which can exist in either host or device memory.**csr_descr_C**–**[in]**descriptor of the sparse CSR matrix \(C\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**csr_row_ptr_C**–**[out]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(C\).**nnz_total_dev_host_ptr**–**[out]**total number of nonzero elements in device or host memory.**temp_buffer**–**[out]**buffer allocated by the user whose size is determined by calling[rocsparse_Xprune_csr2csr_buffer_size()](#rocsparse__prune__csr2csr_8h_1a95a4c7f9c8e5bc8e4b5d29e9ca87a924).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`n`

or`nnz_A`

is invalid.**rocsparse_status_invalid_pointer**–`threshold`

or`csr_descr_A`

or`csr_descr_C`

or`csr_val_A`

or`csr_row_ptr_A`

or`csr_col_ind_A`

or`csr_row_ptr_C`

or`nnz_total_dev_host_ptr`

or`temp_buffer`

pointer is invalid.



## rocsparse_prune_csr2csr()[#](#rocsparse-prune-csr2csr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sprune_csr2csr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr_A, const float *csr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_A, const float *threshold, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr_C, float *csr_val_C, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_C, void *temp_buffer)[#](#_CPPv424rocsparse_sprune_csr2csr16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intPKfK19rocsparse_mat_descrPfPK13rocsparse_intP13rocsparse_intPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dprune_csr2csr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr_A, const double *csr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_A, const double *threshold, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr_C, double *csr_val_C, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_C, void *temp_buffer)[#](#_CPPv424rocsparse_dprune_csr2csr16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_intPKdK19rocsparse_mat_descrPdPK13rocsparse_intP13rocsparse_intPv) Convert and prune sparse CSR matrix \(A\) into a sparse CSR matrix \(C\).

This function converts the sparse CSR matrix \(A\) into a sparse CSR matrix \(C\) by pruning values in \(A\) that are less than a threshold.

The conversion involves three steps. The user first calls

[rocsparse_Xprune_csr2csr_buffer_size()](#rocsparse__prune__csr2csr_8h_1a95a4c7f9c8e5bc8e4b5d29e9ca87a924)to determine the size of the temporary storage buffer. The user allocates this buffer as well as the array`csr_row_ptr_C`

to have`m+1`

elements. The user then calls[rocsparse_Xprune_csr2csr_nnz()](#rocsparse__prune__csr2csr_8h_1a9029c79f7e01fae3587c3513035ed653)which fills in the`csr_row_ptr_C`

array and stores the number of elements that are larger than the pruning threshold in`nnz_total_dev_host_ptr`

. Now that the number of nonzeros larger than the pruning threshold is known, the user uses this information to allocate the`csr_col_ind_C`

and`csr_val_C`

arrays and then calls`rocsparse_prune_csr2csr`

to complete the conversion. Once the conversion is complete, the temporary storage buffer can be freed.**Example**int main() { // 1 2 0 0 // A = 3 0 0 4 // 5 6 0 4 // 7 4 2 5 rocsparse_int m = 4; rocsparse_int n = 4; rocsparse_int nnz_A = 11; float threshold = 5.0f; std::vector<rocsparse_int> hcsr_row_ptr_A = {0, 2, 4, 7, 11}; std::vector<rocsparse_int> hcsr_col_ind_A = {0, 1, 0, 3, 0, 1, 3, 0, 1, 2, 3}; std::vector<float> hcsr_val_A = {1, 2, 3, 4, 5, 6, 4, 7, 4, 2, 5}; rocsparse_int* dcsr_row_ptr_A = nullptr; rocsparse_int* dcsr_col_ind_A = nullptr; float* dcsr_val_A = nullptr; HIP_CHECK(hipMalloc((void**)&dcsr_row_ptr_A, sizeof(rocsparse_int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&dcsr_col_ind_A, sizeof(rocsparse_int) * nnz_A)); HIP_CHECK(hipMalloc((void**)&dcsr_val_A, sizeof(float) * nnz_A)); HIP_CHECK(hipMemcpy(dcsr_row_ptr_A, hcsr_row_ptr_A.data(), sizeof(rocsparse_int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsr_col_ind_A, hcsr_col_ind_A.data(), sizeof(rocsparse_int) * nnz_A, hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsr_val_A, hcsr_val_A.data(), sizeof(float) * nnz_A, hipMemcpyHostToDevice)); rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); rocsparse_mat_descr descr_A; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr_A)); rocsparse_mat_descr descr_C; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr_C)); rocsparse_mat_info info; ROCSPARSE_CHECK(rocsparse_create_mat_info(&info)); rocsparse_int* dcsr_row_ptr_C = nullptr; HIP_CHECK(hipMalloc((void**)&dcsr_row_ptr_C, sizeof(rocsparse_int) * (m + 1))); // Obtain the temporary buffer size size_t buffer_size; ROCSPARSE_CHECK(rocsparse_sprune_csr2csr_buffer_size(handle, m, n, nnz_A, descr_A, dcsr_val_A, dcsr_row_ptr_A, dcsr_col_ind_A, &threshold, descr_C, nullptr, dcsr_row_ptr_C, nullptr, &buffer_size)); // Allocate temporary buffer void* temp_buffer; HIP_CHECK(hipMalloc(&temp_buffer, buffer_size)); rocsparse_int nnz_C; ROCSPARSE_CHECK(rocsparse_sprune_csr2csr_nnz(handle, m, n, nnz_A, descr_A, dcsr_val_A, dcsr_row_ptr_A, dcsr_col_ind_A, &threshold, descr_C, dcsr_row_ptr_C, &nnz_C, temp_buffer)); rocsparse_int* dcsr_col_ind_C = nullptr; float* dcsr_val_C = nullptr; HIP_CHECK(hipMalloc((void**)&dcsr_col_ind_C, sizeof(rocsparse_int) * nnz_C)); HIP_CHECK(hipMalloc((void**)&dcsr_val_C, sizeof(float) * nnz_C)); ROCSPARSE_CHECK(rocsparse_sprune_csr2csr(handle, m, n, nnz_A, descr_A, dcsr_val_A, dcsr_row_ptr_A, dcsr_col_ind_A, &threshold, descr_C, dcsr_val_C, dcsr_row_ptr_C, dcsr_col_ind_C, temp_buffer)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr_A)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr_C)); HIP_CHECK(hipFree(temp_buffer)); HIP_CHECK(hipFree(dcsr_row_ptr_A)); HIP_CHECK(hipFree(dcsr_col_ind_A)); HIP_CHECK(hipFree(dcsr_val_A)); HIP_CHECK(hipFree(dcsr_row_ptr_C)); HIP_CHECK(hipFree(dcsr_col_ind_C)); HIP_CHECK(hipFree(dcsr_val_C)); return 0; }


Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows in the sparse CSR matrix.**n**–**[in]**number of columns in the sparse CSR matrix.**nnz_A**–**[in]**number of non-zeros in the sparse CSR matrix \(A\).**csr_descr_A**–**[in]**descriptor of the sparse CSR matrix \(A\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**csr_val_A**–**[in]**array of`nnz_A`

elements containing the values of the sparse CSR matrix \(A\).**csr_row_ptr_A**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(A\).**csr_col_ind_A**–**[in]**array of`nnz_A`

elements containing the column indices of the sparse CSR matrix \(A\).**threshold**–**[in]**pointer to the non-negative pruning threshold which can exist in either host or device memory.**csr_descr_C**–**[in]**descriptor of the sparse CSR matrix \(C\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**csr_val_C**–**[out]**array of`nnz_C`

elements containing the values of the sparse CSR matrix \(C\).**csr_row_ptr_C**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(C\).**csr_col_ind_C**–**[out]**array of`nnz_C`

elements containing the column indices of the sparse CSR matrix \(C\).**temp_buffer**–**[in]**buffer allocated by the user whose size is determined by calling[rocsparse_Xprune_csr2csr_buffer_size()](#rocsparse__prune__csr2csr_8h_1a95a4c7f9c8e5bc8e4b5d29e9ca87a924).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`n`

or`nnz_A`

is invalid.**rocsparse_status_invalid_pointer**–`threshold`

or`csr_descr_A`

or`csr_descr_C`

or`csr_val_A`

or`csr_row_ptr_A`

or`csr_col_ind_A`

or`csr_val_C`

or`csr_row_ptr_C`

or`csr_col_ind_C`

or`temp_buffer`

pointer is invalid.



## rocsparse_prune_dense2csr_by_percentage_buffer_size()[#](#rocsparse-prune-dense2csr-by-percentage-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sprune_dense2csr_by_percentage_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const float *A,[rocsparse_int](types.html#_CPPv413rocsparse_int)lda, float percentage, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, size_t *buffer_size)[#](#_CPPv452rocsparse_sprune_dense2csr_by_percentage_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_intPKf13rocsparse_intfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dprune_dense2csr_by_percentage_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const double *A,[rocsparse_int](types.html#_CPPv413rocsparse_int)lda, double percentage, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, size_t *buffer_size)[#](#_CPPv452rocsparse_dprune_dense2csr_by_percentage_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_intPKd13rocsparse_intdK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoP6size_t) `rocsparse_prune_dense2csr_by_percentage_buffer_size`

returns the size of the temporary buffer that is required by[rocsparse_Xprune_dense2csr_nnz_by_percentage()](#rocsparse__prune__dense2csr__by__percentage_8h_1a11a2a9286857e1897f3e09d07677d3db)and[rocsparse_Xprune_dense2csr_by_percentage()](#rocsparse__prune__dense2csr__by__percentage_8h_1a6fa3794356534a645e67e3e02818719f). The temporary storage buffer must be allocated by the user.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the dense matrix`A`

.**n**–**[in]**number of columns of the dense matrix`A`

.**A**–**[in]**array of dimensions (`lda`

,`n`

)**lda**–**[in]**leading dimension of dense array`A`

.**percentage**–**[in]**`percentage>=0`

and`percentage<=100`

.**descr**–**[in]**the descriptor of the dense matrix`A`

, the supported matrix type is[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)and also any valid value of the[rocsparse_index_base](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060d).**csr_val**–**[in]**array of nnz ( =`csr_row_ptr`

[m] -`csr_row_ptr`

[0] ) nonzero elements of matrix`A`

.**csr_row_ptr**–**[in]**integer array of`m+1`

elements that contains the start of every row and the end of the last row plus one.**csr_col_ind**–**[in]**integer array of nnz ( =`csr_row_ptr`

[m] -`csr_row_ptr`

[0] ) column indices of the non-zero elements of matrix`A`

.**info**–**[in]**prune information structure**buffer_size**–**[out]**number of bytes of the temporary storage buffer required by[rocsparse_Xprune_dense2csr_nnz_by_percentage()](#rocsparse__prune__dense2csr__by__percentage_8h_1a11a2a9286857e1897f3e09d07677d3db)and[rocsparse_Xprune_dense2csr_by_percentage()](#rocsparse__prune__dense2csr__by__percentage_8h_1a6fa3794356534a645e67e3e02818719f).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`buffer_size`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_prune_dense2csr_nnz_by_percentage()[#](#rocsparse-prune-dense2csr-nnz-by-percentage)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sprune_dense2csr_nnz_by_percentage([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const float *A,[rocsparse_int](types.html#_CPPv413rocsparse_int)lda, float percentage, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_total_dev_host_ptr,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, void *temp_buffer)[#](#_CPPv444rocsparse_sprune_dense2csr_nnz_by_percentage16rocsparse_handle13rocsparse_int13rocsparse_intPKf13rocsparse_intfK19rocsparse_mat_descrP13rocsparse_intP13rocsparse_int18rocsparse_mat_infoPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dprune_dense2csr_nnz_by_percentage([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const double *A,[rocsparse_int](types.html#_CPPv413rocsparse_int)lda, double percentage, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_total_dev_host_ptr,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, void *temp_buffer)[#](#_CPPv444rocsparse_dprune_dense2csr_nnz_by_percentage16rocsparse_handle13rocsparse_int13rocsparse_intPKd13rocsparse_intdK19rocsparse_mat_descrP13rocsparse_intP13rocsparse_int18rocsparse_mat_infoPv) `rocsparse_sprune_dense2csr_nnz_by_percentage`

computes the number of nonzero elements per row and the total number of nonzero elements in a sparse CSR matrix once a`percentage`

of the smallest magnitude elements have been pruned from the dense input matrix. See[rocsparse_sprune_dense2csr_by_percentage()](#rocsparse__prune__dense2csr__by__percentage_8h_1a6fa3794356534a645e67e3e02818719f)for a more detailed description of how this pruning based on`percentage`

works.Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the dense matrix`A`

.**n**–**[in]**number of columns of the dense matrix`A`

.**A**–**[in]**array of dimensions (`lda`

,`n`

)**lda**–**[in]**leading dimension of dense array`A`

.**percentage**–**[in]**`percentage>=0`

and`percentage<=100`

.**descr**–**[in]**the descriptor of the dense matrix`A`

.**csr_row_ptr**–**[out]**integer array of`m+1`

elements that contains the start of every row and the end of the last row plus one.**nnz_total_dev_host_ptr**–**[out]**total number of nonzero elements in device or host memory.**info**–**[in]**prune information structure**temp_buffer**–**[out]**buffer allocated by the user whose size is determined by calling[rocsparse_Xprune_dense2csr_by_percentage_buffer_size()](#rocsparse__prune__dense2csr__by__percentage_8h_1a303ec787755f025322dd7c976a5c0742)..

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`n`

or`lda`

or`percentage`

is invalid.**rocsparse_status_invalid_pointer**–`A`

or`descr`

or`info`

or`csr_row_ptr`

or`nnz_total_dev_host_ptr`

or`temp_buffer`

pointer is invalid.



## rocsparse_prune_dense2csr_by_percentage()[#](#rocsparse-prune-dense2csr-by-percentage)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sprune_dense2csr_by_percentage([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const float *A,[rocsparse_int](types.html#_CPPv413rocsparse_int)lda, float percentage, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, float *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, void *temp_buffer)[#](#_CPPv440rocsparse_sprune_dense2csr_by_percentage16rocsparse_handle13rocsparse_int13rocsparse_intPKf13rocsparse_intfK19rocsparse_mat_descrPfPK13rocsparse_intP13rocsparse_int18rocsparse_mat_infoPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dprune_dense2csr_by_percentage([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const double *A,[rocsparse_int](types.html#_CPPv413rocsparse_int)lda, double percentage, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, double *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, void *temp_buffer)[#](#_CPPv440rocsparse_dprune_dense2csr_by_percentage16rocsparse_handle13rocsparse_int13rocsparse_intPKd13rocsparse_intdK19rocsparse_mat_descrPdPK13rocsparse_intP13rocsparse_int18rocsparse_mat_infoPv) This function converts the matrix \(A\) in dense format into a sparse matrix in CSR format while pruning values based on percentage.

This function converts the dense column oriented matrix \(A\) into a sparse CSR matrix \(C\) by pruning values in \(A\) that are less than a threshold. This threshold is determined by using a

`percentage`

and the following steps:**Step 1**: First the`A`

array is sorted in ascending order using the absolute value of each entry:\[ A\_sorted = sort(abs(A)) \]**Step 2**: Next we use the`percentage`

parameter to determine the threshold:\[\begin{split} pos = ceil(m \times n \times (percentage/100)) - 1 \\ pos = \min(pos, m \times n - 1) \\ pos = \max(pos, 0) \\ threshold = A\_sorted[pos] \end{split}\]**Step 3**: Finally, we use this threshold with the routine[rocsparse_Xprune_dense2csr()](#rocsparse__prune__dense2csr_8h_1afac8859947829464c6223a5731ef1aa8)to complete the conversion.The conversion involves three steps. The user first calls

[rocsparse_Xprune_dense2csr_by_percentage_buffer_size()](#rocsparse__prune__dense2csr__by__percentage_8h_1a303ec787755f025322dd7c976a5c0742)to determine the size of the temporary storage buffer. The user allocates this buffer as well as the array`csr_row_ptr`

to have`m+1`

elements. The user then calls[rocsparse_Xprune_dense2csr_nnz_by_percentage()](#rocsparse__prune__dense2csr__by__percentage_8h_1a11a2a9286857e1897f3e09d07677d3db)which fills in the`csr_row_ptr`

array and stores the number of elements that are larger than the pruning threshold in`nnz_total_dev_host_ptr`

. Now that the number of nonzeros larger than the pruning threshold is known, the user uses this information to allocate the`csr_col_ind`

and`csr_val`

arrays and then calls`rocsparse_prune_dense2csr_by_percentage`

to complete the conversion. Once the conversion is complete, the temporary storage buffer can be freed.**Example**int main() { // 1 2 0 7 // A = 3 0 0 4 // 5 6 0 4 // 0 4 2 5 rocsparse_int m = 4; rocsparse_int n = 4; rocsparse_int lda = m; float percentage = 50.0f; std::vector<float> hdense = {1.0f, 3.0f, 5.0f, 0.0f, 2.0f, 0.0f, 6.0f, 4.0f, 0.0f, 0.0f, 0.0f, 2.0f, 7.0f, 4.0f, 4.0f, 5.0f}; rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); rocsparse_mat_descr descr; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr)); rocsparse_mat_info info; ROCSPARSE_CHECK(rocsparse_create_mat_info(&info)); float* ddense = nullptr; HIP_CHECK(hipMalloc((void**)&ddense, sizeof(float) * lda * n)); HIP_CHECK(hipMemcpy(ddense, hdense.data(), sizeof(float) * lda * n, hipMemcpyHostToDevice)); rocsparse_int* dcsr_row_ptr = nullptr; HIP_CHECK(hipMalloc((void**)&dcsr_row_ptr, sizeof(rocsparse_int) * (m + 1))); // Obtain the temporary buffer size size_t buffer_size; ROCSPARSE_CHECK(rocsparse_sprune_dense2csr_by_percentage_buffer_size(handle, m, n, ddense, lda, percentage, descr, nullptr, dcsr_row_ptr, nullptr, info, &buffer_size)); // Allocate temporary buffer void* temp_buffer; HIP_CHECK(hipMalloc(&temp_buffer, buffer_size)); rocsparse_int nnz; ROCSPARSE_CHECK(rocsparse_sprune_dense2csr_nnz_by_percentage( handle, m, n, ddense, lda, percentage, descr, dcsr_row_ptr, &nnz, info, temp_buffer)); rocsparse_int* dcsr_col_ind = nullptr; float* dcsr_val = nullptr; HIP_CHECK(hipMalloc((void**)&dcsr_col_ind, sizeof(rocsparse_int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcsr_val, sizeof(float) * nnz)); ROCSPARSE_CHECK(rocsparse_sprune_dense2csr_by_percentage(handle, m, n, ddense, lda, percentage, descr, dcsr_val, dcsr_row_ptr, dcsr_col_ind, info, temp_buffer)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr)); ROCSPARSE_CHECK(rocsparse_destroy_mat_info(info)); HIP_CHECK(hipFree(temp_buffer)); HIP_CHECK(hipFree(ddense)); HIP_CHECK(hipFree(dcsr_row_ptr)); HIP_CHECK(hipFree(dcsr_col_ind)); HIP_CHECK(hipFree(dcsr_val)); return 0; }


Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the dense matrix`A`

.**n**–**[in]**number of columns of the dense matrix`A`

.**A**–**[in]**array of dimensions (`lda`

,`n`

)**lda**–**[in]**leading dimension of dense array`A`

.**percentage**–**[in]**`percentage>=0`

and`percentage<=100`

.**descr**–**[in]**the descriptor of the dense matrix`A`

, the supported matrix type is[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)and also any valid value of the[rocsparse_index_base](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060d).**csr_val**–**[out]**array of nnz ( =`csr_row_ptr`

[m] -`csr_row_ptr`

[0] ) nonzero elements of matrix`A`

.**csr_row_ptr**–**[in]**integer array of`m+1`

elements that contains the start of every row and the end of the last row plus one.**csr_col_ind**–**[out]**integer array of nnz ( =`csr_row_ptr`

[m] -`csr_row_ptr`

[0] ) column indices of the non-zero elements of matrix`A`

.**info**–**[in]**prune information structure**temp_buffer**–**[in]**temporary storage buffer allocated by the user, size is returned by[rocsparse_Xprune_dense2csr_by_percentage_buffer_size()](#rocsparse__prune__dense2csr__by__percentage_8h_1a303ec787755f025322dd7c976a5c0742).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`n`

or`lda`

or`percentage`

is invalid.**rocsparse_status_invalid_pointer**–`A`

or`descr`

or`info`

or`csr_val`

or`csr_row_ptr`

or`csr_col_ind`

or`temp_buffer`

pointer is invalid.



## rocsparse_prune_csr2csr_by_percentage_buffer_size()[#](#rocsparse-prune-csr2csr-by-percentage-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sprune_csr2csr_by_percentage_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr_A, const float *csr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_A, float percentage, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr_C, const float *csr_val_C, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_C, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_C,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, size_t *buffer_size)[#](#_CPPv450rocsparse_sprune_csr2csr_by_percentage_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dprune_csr2csr_by_percentage_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr_A, const double *csr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_A, double percentage, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr_C, const double *csr_val_C, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_C, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_C,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, size_t *buffer_size)[#](#_CPPv450rocsparse_dprune_csr2csr_by_percentage_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_intdK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoP6size_t) `rocsparse_prune_csr2csr_by_percentage_buffer_size`

returns the size of the temporary buffer that is required by[rocsparse_Xprune_csr2csr_nnz_by_percentage()](#rocsparse__prune__csr2csr__by__percentage_8h_1a4c59d040984e26e7610719240f1cefd5)and[rocsparse_Xprune_csr2csr_by_percentage()](#rocsparse__prune__csr2csr__by__percentage_8h_1aaae3e5c987d8b2a49a76ccaab8e991ff). The temporary storage buffer must be allocated by the user.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows in the sparse CSR matrix.**n**–**[in]**number of columns in the sparse CSR matrix.**nnz_A**–**[in]**number of non-zeros in the sparse CSR matrix \(A\).**csr_descr_A**–**[in]**descriptor of the sparse CSR matrix \(A\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**csr_val_A**–**[in]**array of`nnz_A`

elements containing the values of the sparse CSR matrix \(A\).**csr_row_ptr_A**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(A\).**csr_col_ind_A**–**[in]**array of`nnz_A`

elements containing the column indices of the sparse CSR matrix \(A\).**percentage**–**[in]**`percentage>=0`

and`percentage<=100`

.**csr_descr_C**–**[in]**descriptor of the sparse CSR matrix \(C\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**csr_val_C**–**[in]**array of`nnz_C`

elements containing the values of the sparse CSR matrix \(C\).**csr_row_ptr_C**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(C\).**csr_col_ind_C**–**[in]**array of`nnz_C`

elements containing the column indices of the sparse CSR matrix \(C\).**info**–**[in]**prune info structure.**buffer_size**–**[out]**number of bytes of the temporary storage buffer required by[rocsparse_Xprune_csr2csr_nnz_by_percentage()](#rocsparse__prune__csr2csr__by__percentage_8h_1a4c59d040984e26e7610719240f1cefd5)and[rocsparse_Xprune_csr2csr_by_percentage()](#rocsparse__prune__csr2csr__by__percentage_8h_1aaae3e5c987d8b2a49a76ccaab8e991ff)

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`buffer_size`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_prune_csr2csr_nnz_by_percentage()[#](#rocsparse-prune-csr2csr-nnz-by-percentage)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sprune_csr2csr_nnz_by_percentage([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr_A, const float *csr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_A, float percentage, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_total_dev_host_ptr,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, void *temp_buffer)[#](#_CPPv442rocsparse_sprune_csr2csr_nnz_by_percentage16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intfK19rocsparse_mat_descrP13rocsparse_intP13rocsparse_int18rocsparse_mat_infoPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dprune_csr2csr_nnz_by_percentage([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr_A, const double *csr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_A, double percentage, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_total_dev_host_ptr,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, void *temp_buffer)[#](#_CPPv442rocsparse_dprune_csr2csr_nnz_by_percentage16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_intdK19rocsparse_mat_descrP13rocsparse_intP13rocsparse_int18rocsparse_mat_infoPv) `rocsparse_prune_csr2csr_nnz_by_percentage`

computes the number of nonzero elements per row and the total number of nonzero elements in a sparse CSR matrix once a`percentage`

of the smallest magnitude elements have been pruned from the sparse CSR input matrix. See[rocsparse_sprune_csr2csr_by_percentage()](#rocsparse__prune__csr2csr__by__percentage_8h_1aaae3e5c987d8b2a49a76ccaab8e991ff)for a more detailed description of how this pruning based on`percentage`

works.Note

The routine does support asynchronous execution if the pointer mode is set to device.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows in the sparse CSR matrix.**n**–**[in]**number of columns in the sparse CSR matrix.**nnz_A**–**[in]**number of non-zeros in the sparse CSR matrix \(A\).**csr_descr_A**–**[in]**descriptor of the sparse CSR matrix \(A\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**csr_val_A**–**[in]**array of`nnz_A`

elements containing the values of the sparse CSR matrix \(A\).**csr_row_ptr_A**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(A\).**csr_col_ind_A**–**[in]**array of`nnz_A`

elements containing the column indices of the sparse CSR matrix \(A\).**percentage**–**[in]**`percentage>=0`

and`percentage<=100`

.**csr_descr_C**–**[in]**descriptor of the sparse CSR matrix \(C\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**csr_row_ptr_C**–**[out]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(C\).**nnz_total_dev_host_ptr**–**[out]**total number of nonzero elements in device or host memory.**info**–**[in]**prune info structure.**temp_buffer**–**[out]**buffer allocated by the user whose size is determined by calling[rocsparse_Xprune_csr2csr_by_percentage_buffer_size()](#rocsparse__prune__csr2csr__by__percentage_8h_1a1ed53847a44eba293a62ffe1ccf52ae5).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`n`

or`nnz_A`

or`percentage`

is invalid.**rocsparse_status_invalid_pointer**–`csr_descr_A`

or`csr_descr_C`

or`info`

or`csr_val_A`

or`csr_row_ptr_A`

or`csr_col_ind_A`

or`csr_row_ptr_C`

or`nnz_total_dev_host_ptr`

or`temp_buffer`

pointer is invalid.



## rocsparse_prune_csr2csr_by_percentage()[#](#rocsparse-prune-csr2csr-by-percentage)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sprune_csr2csr_by_percentage([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr_A, const float *csr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_A, float percentage, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr_C, float *csr_val_C, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_C,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, void *temp_buffer)[#](#_CPPv438rocsparse_sprune_csr2csr_by_percentage16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intfK19rocsparse_mat_descrPfPK13rocsparse_intP13rocsparse_int18rocsparse_mat_infoPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dprune_csr2csr_by_percentage([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr_A, const double *csr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_A, double percentage, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)csr_descr_C, double *csr_val_C, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_C,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, void *temp_buffer)[#](#_CPPv438rocsparse_dprune_csr2csr_by_percentage16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_intdK19rocsparse_mat_descrPdPK13rocsparse_intP13rocsparse_int18rocsparse_mat_infoPv) Convert and prune by percentage a sparse CSR matrix \(A\) into a sparse CSR matrix \(C\).

This function converts the sparse CSR matrix \(A\) into a sparse CSR matrix \(C\) by pruning values in \(A\) that are less than a threshold. This threshold is determined by using a

`percentage`

and the following steps:**Step 1**: First the`csr_val_A`

array is sorted in ascending order using the absolute value of each entry:\[ csr\_val\_A\_sorted = sort(abs(csr\_val\_A)) \]**Step 2**: Next we use the`percentage`

parameter to determine the threshold:\[\begin{split} pos = ceil(nnz\_A \times (percentage/100)) - 1 \\ pos = \min(pos, nnz\_A - 1) \\ pos = \max(pos, 0) \\ threshold = csr\_val\_A\_sorted[pos] \end{split}\]**Step 3**: Finally, we use this threshold with the routine[rocsparse_Xprune_csr2csr()](#rocsparse__prune__csr2csr_8h_1a964f74e36a52e0d2c4c251fc9ec3c7e6)to complete the conversion.The conversion involves three steps. The user first calls

[rocsparse_Xprune_csr2csr_by_percentage_buffer_size()](#rocsparse__prune__csr2csr__by__percentage_8h_1a1ed53847a44eba293a62ffe1ccf52ae5)to determine the size of the temporary storage buffer. The user allocates this buffer as well as the array`csr_row_ptr_C`

to have`m+1`

elements. The user then calls[rocsparse_Xprune_csr2csr_nnz_by_percentage()](#rocsparse__prune__csr2csr__by__percentage_8h_1a4c59d040984e26e7610719240f1cefd5)which fills in the`csr_row_ptr_C`

array and stores the number of elements that are larger than the pruning threshold in`nnz_total_dev_host_ptr`

. Now that the number of nonzeros larger than the pruning threshold is known, the user uses this information to allocate the`csr_col_ind_C`

and`csr_val_C`

arrays and then calls`rocsparse_prune_csr2csr_by_percentage`

to complete the conversion. Once the conversion is complete, the temporary storage buffer can be freed.**Example**int main() { // 1 2 0 0 // A = 3 0 0 4 // 5 6 0 4 // 7 4 2 5 rocsparse_int m = 4; rocsparse_int n = 4; rocsparse_int nnz_A = 11; float percentage = 50.0f; std::vector<rocsparse_int> hcsr_row_ptr_A = {0, 2, 4, 7, 11}; std::vector<rocsparse_int> hcsr_col_ind_A = {0, 1, 0, 3, 0, 1, 3, 0, 1, 2, 3}; std::vector<float> hcsr_val_A = {1, 2, 3, 4, 5, 6, 4, 7, 4, 2, 5}; rocsparse_int* dcsr_row_ptr_A = nullptr; rocsparse_int* dcsr_col_ind_A = nullptr; float* dcsr_val_A = nullptr; HIP_CHECK(hipMalloc((void**)&dcsr_row_ptr_A, sizeof(rocsparse_int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&dcsr_col_ind_A, sizeof(rocsparse_int) * nnz_A)); HIP_CHECK(hipMalloc((void**)&dcsr_val_A, sizeof(float) * nnz_A)); HIP_CHECK(hipMemcpy(dcsr_row_ptr_A, hcsr_row_ptr_A.data(), sizeof(rocsparse_int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsr_col_ind_A, hcsr_col_ind_A.data(), sizeof(rocsparse_int) * nnz_A, hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsr_val_A, hcsr_val_A.data(), sizeof(float) * nnz_A, hipMemcpyHostToDevice)); rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); rocsparse_mat_descr descr_A; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr_A)); rocsparse_mat_descr descr_C; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr_C)); rocsparse_mat_info info; ROCSPARSE_CHECK(rocsparse_create_mat_info(&info)); rocsparse_int* dcsr_row_ptr_C = nullptr; HIP_CHECK(hipMalloc((void**)&dcsr_row_ptr_C, sizeof(rocsparse_int) * (m + 1))); // Obtain the temporary buffer size size_t buffer_size; ROCSPARSE_CHECK(rocsparse_sprune_csr2csr_by_percentage_buffer_size(handle, m, n, nnz_A, descr_A, dcsr_val_A, dcsr_row_ptr_A, dcsr_col_ind_A, percentage, descr_C, nullptr, dcsr_row_ptr_C, nullptr, info, &buffer_size)); // Allocate temporary buffer void* temp_buffer; HIP_CHECK(hipMalloc(&temp_buffer, buffer_size)); rocsparse_int nnz_C; ROCSPARSE_CHECK(rocsparse_sprune_csr2csr_nnz_by_percentage(handle, m, n, nnz_A, descr_A, dcsr_val_A, dcsr_row_ptr_A, dcsr_col_ind_A, percentage, descr_C, dcsr_row_ptr_C, &nnz_C, info, temp_buffer)); rocsparse_int* dcsr_col_ind_C = nullptr; float* dcsr_val_C = nullptr; HIP_CHECK(hipMalloc((void**)&dcsr_col_ind_C, sizeof(rocsparse_int) * nnz_C)); HIP_CHECK(hipMalloc((void**)&dcsr_val_C, sizeof(float) * nnz_C)); ROCSPARSE_CHECK(rocsparse_sprune_csr2csr_by_percentage(handle, m, n, nnz_A, descr_A, dcsr_val_A, dcsr_row_ptr_A, dcsr_col_ind_A, percentage, descr_C, dcsr_val_C, dcsr_row_ptr_C, dcsr_col_ind_C, info, temp_buffer)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr_A)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr_C)); ROCSPARSE_CHECK(rocsparse_destroy_mat_info(info)); HIP_CHECK(hipFree(temp_buffer)); HIP_CHECK(hipFree(dcsr_row_ptr_A)); HIP_CHECK(hipFree(dcsr_col_ind_A)); HIP_CHECK(hipFree(dcsr_val_A)); HIP_CHECK(hipFree(dcsr_row_ptr_C)); HIP_CHECK(hipFree(dcsr_col_ind_C)); HIP_CHECK(hipFree(dcsr_val_C)); return 0; }


Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows in the sparse CSR matrix.**n**–**[in]**number of columns in the sparse CSR matrix.**nnz_A**–**[in]**number of non-zeros in the sparse CSR matrix \(A\).**csr_descr_A**–**[in]**descriptor of the sparse CSR matrix \(A\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**csr_val_A**–**[in]**array of`nnz_A`

elements containing the values of the sparse CSR matrix \(A\).**csr_row_ptr_A**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(A\).**csr_col_ind_A**–**[in]**array of`nnz_A`

elements containing the column indices of the sparse CSR matrix \(A\).**percentage**–**[in]**`percentage>=0`

and`percentage<=100`

.**csr_descr_C**–**[in]**descriptor of the sparse CSR matrix \(C\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**csr_val_C**–**[out]**array of`nnz_C`

elements containing the values of the sparse CSR matrix \(C\).**csr_row_ptr_C**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(C\).**csr_col_ind_C**–**[out]**array of`nnz_C`

elements containing the column indices of the sparse CSR matrix \(C\).**info**–**[in]**prune info structure.**temp_buffer**–**[in]**buffer allocated by the user whose size is determined by calling[rocsparse_Xprune_csr2csr_buffer_size()](#rocsparse__prune__csr2csr_8h_1a95a4c7f9c8e5bc8e4b5d29e9ca87a924).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`n`

or`nnz_A`

or`percentage`

is invalid.**rocsparse_status_invalid_pointer**–`csr_descr_A`

or`csr_descr_C`

or`info`

or`csr_val_A`

or`csr_row_ptr_A`

or`csr_col_ind_A`

or`csr_val_C`

or`csr_row_ptr_C`

or`csr_col_ind_C`

or`temp_buffer`

pointer is invalid.



## rocsparse_rocsparse_bsrpad_value()[#](#rocsparse-rocsparse-bsrpad-value)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sbsrpad_value([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim, float value, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)bsr_descr, float *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind)[#](#_CPPv423rocsparse_sbsrpad_value16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intfK19rocsparse_mat_descrPfPK13rocsparse_intPK13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dbsrpad_value([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim, double value, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)bsr_descr, double *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind)[#](#_CPPv423rocsparse_dbsrpad_value16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intdK19rocsparse_mat_descrPdPK13rocsparse_intPK13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cbsrpad_value([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)value, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)bsr_descr,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind)[#](#_CPPv423rocsparse_cbsrpad_value16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_int23rocsparse_float_complexK19rocsparse_mat_descrP23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zbsrpad_value([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)value, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)bsr_descr,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind)[#](#_CPPv423rocsparse_zbsrpad_value16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_int24rocsparse_double_complexK19rocsparse_mat_descrP24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int) Pads a value to the diagonal of the last block (if the last block is a diagonal block) in the sparse BSR matrix when the matrix expands outside m x m.

When converting from a CSR matrix to a BSR matrix the resulting BSR matrix will be larger when m < mb * block_dim. In these situations, the CSR to BSR conversion will expand the BSR matrix to have zeros when outside m x m. This routine converts the resulting BSR matrix to one that has a value on the last diagonal blocks diagonal if this last block is a diagonal block in the BSR matrix.

Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the sparse BSR matrix.**mb**–**[in]**number of block rows of the sparse BSR matrix.**nnzb**–**[in]**number of non-zero blocks of the sparse BSR matrix.**block_dim**–**[in]**block dimension of the sparse BSR matrix.**value**–**[in]**scalar value that is set on the diagonal of the last block when the matrix expands outside of`m`

x`m`

**bsr_descr**–**[in]**descriptor of the sparse BSR matrix. Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**bsr_val**–**[inout]**array of`nnzb`

blocks of the sparse BSR matrix.**bsr_row_ptr**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix.**bsr_col_ind**–**[in]**array of`nnzb`

elements containing the block column indices of the sparse BSR matrix.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`mb`

,`nnzb`

or`block_dim`

is invalid.**rocsparse_status_invalid_pointer**–`bsr_descr`

,`bsr_val`

,`bsr_row_ind`

,`bsr_col_ind`

, pointer is invalid.
