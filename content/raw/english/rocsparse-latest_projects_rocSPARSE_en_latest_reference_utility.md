---
title: "Sparse utility functions &#8212; rocSPARSE 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocSPARSE/en/latest/reference/utility.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:16:49.796950+00:00
content_hash: "86e0d73d8a70e887"
---

# Sparse utility functions[#](#sparse-utility-functions)

This module contains all sparse utility routines.

The sparse utility routines allow for testing whether matrix data is valid for different matrix formats.
These routines do not support execution in a `hipGraph`

context.

## rocsparse_check_matrix_csr_buffer_size()[#](#rocsparse-check-matrix-csr-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scheck_matrix_csr_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const float *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage, size_t *buffer_size)[#](#_CPPv439rocsparse_scheck_matrix_csr_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcheck_matrix_csr_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const double *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage, size_t *buffer_size)[#](#_CPPv439rocsparse_dcheck_matrix_csr_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPKdPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccheck_matrix_csr_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage, size_t *buffer_size)[#](#_CPPv439rocsparse_ccheck_matrix_csr_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcheck_matrix_csr_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage, size_t *buffer_size)[#](#_CPPv439rocsparse_zcheck_matrix_csr_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP6size_t) `rocsparse_check_matrix_csr_buffer_size`

computes the required buffer size needed when calling[rocsparse_Xcheck_matrix_csr()](#rocsparse__check__matrix__csr_8h_1adbf80660b58abffcae4909bbc0195b51).Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix.**n**–**[in]**number of columns of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**csr_val**–**[in]**array of`nnz`

elements of the sparse CSR matrix.**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csr_col_ind**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**matrix_type**–**[in]**[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03),[rocsparse_matrix_type_symmetric](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8340a3909d43b5b6bedd8ecc928605a5),[rocsparse_matrix_type_hermitian](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75aa30592e2cccfda6e1d66dc3a484fc7a8)or[rocsparse_matrix_type_triangular](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a73d9ef5e5e18209f9f10a5885d3e15ba).**uplo**–**[in]**[rocsparse_fill_mode_lower](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a1eb644f6f2701329635e07d91919d37e)or[rocsparse_fill_mode_upper](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a905f490c7fc5a59e8a635938cec0d004).**storage**–**[in]**[rocsparse_storage_mode_sorted](enumerations.html#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13ea73d28ef281d17b58cf46a846fd515fff)or[rocsparse_storage_mode_sorted](enumerations.html#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13ea73d28ef281d17b58cf46a846fd515fff).**buffer_size**–**[out]**number of bytes of the temporary storage buffer required by[rocsparse_scheck_matrix_csr()](#rocsparse__check__matrix__csr_8h_1adbf80660b58abffcae4909bbc0195b51),[rocsparse_dcheck_matrix_csr()](#rocsparse__check__matrix__csr_8h_1a50c5dca1fd1c2cf2bd134a43c61412e6),[rocsparse_ccheck_matrix_csr()](#rocsparse__check__matrix__csr_8h_1a735d48e0edef8177e77c651ec714b345)and[rocsparse_zcheck_matrix_csr()](#rocsparse__check__matrix__csr_8h_1a996f103ed6d56087d2c8d3aa8aa38bcb).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_value**–`idx_base`

or`matrix_type`

or`uplo`

or`storage`

is invalid.**rocsparse_status_invalid_size**–`m`

`n`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`csr_val`

,`csr_row_ptr`

,`csr_col_ind`

or`buffer_size`

pointer is invalid.



## rocsparse_check_matrix_csr()[#](#rocsparse-check-matrix-csr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scheck_matrix_csr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const float *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage,[rocsparse_data_status](enumerations.html#_CPPv421rocsparse_data_status)*data_status, void *temp_buffer)[#](#_CPPv427rocsparse_scheck_matrix_csr16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP21rocsparse_data_statusPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcheck_matrix_csr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const double *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage,[rocsparse_data_status](enumerations.html#_CPPv421rocsparse_data_status)*data_status, void *temp_buffer)[#](#_CPPv427rocsparse_dcheck_matrix_csr16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPKdPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP21rocsparse_data_statusPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccheck_matrix_csr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage,[rocsparse_data_status](enumerations.html#_CPPv421rocsparse_data_status)*data_status, void *temp_buffer)[#](#_CPPv427rocsparse_ccheck_matrix_csr16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP21rocsparse_data_statusPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcheck_matrix_csr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage,[rocsparse_data_status](enumerations.html#_CPPv421rocsparse_data_status)*data_status, void *temp_buffer)[#](#_CPPv427rocsparse_zcheck_matrix_csr16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP21rocsparse_data_statusPv) Check matrix to see if it is valid.

`rocsparse_check_matrix_csr`

checks if the input CSR matrix is valid. It performs basic sanity checks on the input matrix and tries to detect issues in the data. This includes looking for ‘nan’ or ‘inf’ values in the data arrays, invalid column indices or row offsets, whether the matrix is triangular or not, whether there are duplicate indices or whether the column indices are not sorted when they should be. If an issue is found, it is written to the`data_status`

parameter.Performing the above checks involves two steps. First the user calls

`rocsparse_Xcheck_matrix_csr_buffer_size`

in order to determine the required buffer size. The user then allocates this buffer and passes it to`rocsparse_Xcheck_matrix_csr`

. Any issues detected will be written to the`data_status`

parameter which is always a host variable regardless of pointer mode.// 1 2 0 0 // 0 3 4 0 // 2 0 1 1 // 0 3 0 2 std::vector<int> hcsr_row_ptr = {0, 2, -1, 7, 9}; // <---- invalid ptr array std::vector<int> hcsr_col_ind = {0, 1, 1, 2, 0, 2, 3, 1, 3}; std::vector<float> hcsr_val = {1, 2, 3, 4, 2, 1, 1, 3, 2}; int m = 4; int n = 4; int nnz = 9; int* dcsr_row_ptr = nullptr; int* dcsr_col_ind = nullptr; float* dcsr_val = nullptr; hipMalloc((void**)&dcsr_row_ptr, sizeof(int) * (m + 1)); hipMalloc((void**)&dcsr_col_ind, sizeof(int) * nnz); hipMalloc((void**)&dcsr_val, sizeof(float) * nnz); hipMemcpy(dcsr_row_ptr, hcsr_row_ptr.data(), sizeof(int) * (m + 1), hipMemcpyHostToDevice); hipMemcpy(dcsr_col_ind, hcsr_col_ind.data(), sizeof(int) * nnz, hipMemcpyHostToDevice); hipMemcpy(dcsr_val, hcsr_val.data(), sizeof(float) * nnz, hipMemcpyHostToDevice); rocsparse_handle handle; rocsparse_create_handle(&handle); const rocsparse_index_base idx_base = rocsparse_index_base_zero; const rocsparse_fill_mode fill_mode = rocsparse_fill_mode_upper; const rocsparse_matrix_type matrix_type = rocsparse_matrix_type_general; const rocsparse_storage_mode storage_mode = rocsparse_storage_mode_sorted; rocsparse_data_status data_status; size_t buffer_size; rocsparse_scheck_matrix_csr_buffer_size(handle, m, n, nnz, dcsr_val, dcsr_row_ptr, dcsr_col_ind, idx_base, matrix_type, fill_mode, storage_mode, &buffer_size); void* dbuffer = nullptr; hipMalloc((void**)&dbuffer, buffer_size); rocsparse_scheck_matrix_csr(handle, m, n, nnz, dcsr_val, dcsr_row_ptr, dcsr_col_ind, idx_base, matrix_type, fill_mode, storage_mode, &data_status, dbuffer); std::cout << "data_status: " << data_status << std::endl; hipFree(dbuffer); rocsparse_destroy_handle(handle); hipFree(dcsr_row_ptr); hipFree(dcsr_col_ind); hipFree(dcsr_val);

**Example**In this example we want to check whether a CSR matrix has correct row pointer array. The matrix passed is invalid because it contains a -1 entry in the row pointer array.


Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix.**n**–**[in]**number of columns of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**csr_val**–**[in]**array of`nnz`

elements of the sparse CSR matrix.**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csr_col_ind**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**matrix_type**–**[in]**[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03),[rocsparse_matrix_type_symmetric](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8340a3909d43b5b6bedd8ecc928605a5),[rocsparse_matrix_type_hermitian](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75aa30592e2cccfda6e1d66dc3a484fc7a8)or[rocsparse_matrix_type_triangular](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a73d9ef5e5e18209f9f10a5885d3e15ba).**uplo**–**[in]**[rocsparse_fill_mode_lower](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a1eb644f6f2701329635e07d91919d37e)or[rocsparse_fill_mode_upper](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a905f490c7fc5a59e8a635938cec0d004).**storage**–**[in]**[rocsparse_storage_mode_sorted](enumerations.html#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13ea73d28ef281d17b58cf46a846fd515fff)or[rocsparse_storage_mode_sorted](enumerations.html#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13ea73d28ef281d17b58cf46a846fd515fff).**data_status**–**[out]**modified to indicate the status of the data**temp_buffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_value**–`idx_base`

or`matrix_type`

or`uplo`

or`storage`

is invalid.**rocsparse_status_invalid_size**–`m`

`n`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`csr_val`

,`csr_row_ptr`

,`csr_col_ind`

,`temp_buffer`

or`data_status`

pointer is invalid.



## rocsparse_check_matrix_csc_buffer_size()[#](#rocsparse-check-matrix-csc-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scheck_matrix_csc_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const float *csc_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_col_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_row_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage, size_t *buffer_size)[#](#_CPPv439rocsparse_scheck_matrix_csc_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcheck_matrix_csc_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const double *csc_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_col_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_row_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage, size_t *buffer_size)[#](#_CPPv439rocsparse_dcheck_matrix_csc_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPKdPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccheck_matrix_csc_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csc_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_col_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_row_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage, size_t *buffer_size)[#](#_CPPv439rocsparse_ccheck_matrix_csc_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcheck_matrix_csc_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csc_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_col_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_row_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage, size_t *buffer_size)[#](#_CPPv439rocsparse_zcheck_matrix_csc_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP6size_t) `rocsparse_check_matrix_csc_buffer_size`

computes the required buffer size needed when calling[rocsparse_Xcheck_matrix_csc()](#rocsparse__check__matrix__csc_8h_1a82441727662d54cfa6143d6de8a5aaf8).Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the sparse CSC matrix.**n**–**[in]**number of columns of the sparse CSC matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSC matrix.**csc_val**–**[in]**array of`nnz`

elements of the sparse CSC matrix.**csc_col_ptr**–**[in]**array of`m+1`

elements that point to the start of every column of the sparse CSC matrix.**csc_row_ind**–**[in]**array of`nnz`

elements containing the row indices of the sparse CSC matrix.**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**matrix_type**–**[in]**[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03),[rocsparse_matrix_type_symmetric](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8340a3909d43b5b6bedd8ecc928605a5),[rocsparse_matrix_type_hermitian](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75aa30592e2cccfda6e1d66dc3a484fc7a8)or[rocsparse_matrix_type_triangular](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a73d9ef5e5e18209f9f10a5885d3e15ba).**uplo**–**[in]**[rocsparse_fill_mode_lower](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a1eb644f6f2701329635e07d91919d37e)or[rocsparse_fill_mode_upper](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a905f490c7fc5a59e8a635938cec0d004).**storage**–**[in]**[rocsparse_storage_mode_sorted](enumerations.html#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13ea73d28ef281d17b58cf46a846fd515fff)or[rocsparse_storage_mode_sorted](enumerations.html#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13ea73d28ef281d17b58cf46a846fd515fff).**buffer_size**–**[out]**number of bytes of the temporary storage buffer required by[rocsparse_Xcheck_matrix_csc()](#rocsparse__check__matrix__csc_8h_1a82441727662d54cfa6143d6de8a5aaf8).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_value**–`idx_base`

or`matrix_type`

or`uplo`

or`storage`

is invalid.**rocsparse_status_invalid_size**–`m`

`n`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`csc_val`

,`csc_col_ptr`

,`csc_row_ind`

or`buffer_size`

pointer is invalid.



## rocsparse_check_matrix_csc()[#](#rocsparse-check-matrix-csc)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scheck_matrix_csc([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const float *csc_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_col_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_row_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage,[rocsparse_data_status](enumerations.html#_CPPv421rocsparse_data_status)*data_status, void *temp_buffer)[#](#_CPPv427rocsparse_scheck_matrix_csc16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP21rocsparse_data_statusPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcheck_matrix_csc([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const double *csc_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_col_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_row_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage,[rocsparse_data_status](enumerations.html#_CPPv421rocsparse_data_status)*data_status, void *temp_buffer)[#](#_CPPv427rocsparse_dcheck_matrix_csc16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPKdPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP21rocsparse_data_statusPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccheck_matrix_csc([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csc_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_col_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_row_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage,[rocsparse_data_status](enumerations.html#_CPPv421rocsparse_data_status)*data_status, void *temp_buffer)[#](#_CPPv427rocsparse_ccheck_matrix_csc16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP21rocsparse_data_statusPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcheck_matrix_csc([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csc_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_col_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csc_row_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage,[rocsparse_data_status](enumerations.html#_CPPv421rocsparse_data_status)*data_status, void *temp_buffer)[#](#_CPPv427rocsparse_zcheck_matrix_csc16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP21rocsparse_data_statusPv) Check matrix to see if it is valid.

`rocsparse_check_matrix_csc`

checks if the input CSC matrix is valid. It performs basic sanity checks on the input matrix and tries to detect issues in the data. This includes looking for ‘nan’ or ‘inf’ values in the data arrays, invalid row indices or invalid column offsets, whether the matrix is triangular or not, whether there are duplicate row indices or whether the row indices are not sorted when they should be. If an issue is found, it is written to the`data_status`

parameter.Performing the above checks involves two steps. First the user calls

`rocsparse_Xcheck_matrix_csc_buffer_size`

in order to determine the required buffer size. The user then allocates this buffer and passes it to`rocsparse_Xcheck_matrix_csc`

. Any issues detected will be written to the`data_status`

parameter which is always a host variable regardless of pointer mode.// 1 2 0 0 // 0 3 4 0 // 2 0 1 1 // 0 3 0 2 std::vector<int> hcsc_row_ind = {0, 2, 0, 1, 1, 1, 2, 2, 3}; //<---duplicate row index in second column std::vector<int> hcsc_col_ptr = {0, 2, 5, 7, 9}; std::vector<float> hcsc_val = {1, 2, 2, 3, 3, 4, 1, 1, 2}; int m = 4; int n = 4; int nnz = 9; int* dcsc_row_ind = nullptr; int* dcsc_col_ptr = nullptr; float* dcsc_val = nullptr; hipMalloc((void**)&dcsc_row_ind, sizeof(int) * nnz); hipMalloc((void**)&dcsc_col_ptr, sizeof(int) * (n + 1)); hipMalloc((void**)&dcsc_val, sizeof(float) * nnz); hipMemcpy(dcsc_row_ind, hcsc_row_ind.data(), sizeof(int) * nnz, hipMemcpyHostToDevice); hipMemcpy(dcsc_col_ptr, hcsc_col_ptr.data(), sizeof(int) * (n + 1), hipMemcpyHostToDevice); hipMemcpy(dcsc_val, hcsc_val.data(), sizeof(float) * nnz, hipMemcpyHostToDevice); rocsparse_handle handle; rocsparse_create_handle(&handle); const rocsparse_index_base idx_base = rocsparse_index_base_zero; const rocsparse_fill_mode fill_mode = rocsparse_fill_mode_upper; const rocsparse_matrix_type matrix_type = rocsparse_matrix_type_general; const rocsparse_storage_mode storage_mode = rocsparse_storage_mode_sorted; rocsparse_data_status data_status; size_t buffer_size; rocsparse_scheck_matrix_csc_buffer_size(handle, m, n, nnz, dcsc_val, dcsc_col_ptr, dcsc_row_ind, idx_base, matrix_type, fill_mode, storage_mode, &buffer_size); void* dbuffer = nullptr; hipMalloc((void**)&dbuffer, buffer_size); rocsparse_scheck_matrix_csc(handle, m, n, nnz, dcsc_val, dcsc_col_ptr, dcsc_row_ind, idx_base, matrix_type, fill_mode, storage_mode, &data_status, dbuffer); std::cout << "data_status: " << data_status << std::endl; hipFree(dbuffer); rocsparse_destroy_handle(handle); hipFree(dcsc_row_ind); hipFree(dcsc_col_ptr); hipFree(dcsc_val);

**Example**In this example we want to check whether a CSC matrix has correct row indices. The matrix passed is invalid because it contains a duplicate entry in the row indices array.


Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the sparse CSC matrix.**n**–**[in]**number of columns of the sparse CSC matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSC matrix.**csc_val**–**[in]**array of`nnz`

elements of the sparse CSC matrix.**csc_col_ptr**–**[in]**array of`m+1`

elements that point to the start of every column of the sparse CSC matrix.**csc_row_ind**–**[in]**array of`nnz`

elements containing the row indices of the sparse CSC matrix.**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**matrix_type**–**[in]**[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03),[rocsparse_matrix_type_symmetric](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8340a3909d43b5b6bedd8ecc928605a5),[rocsparse_matrix_type_hermitian](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75aa30592e2cccfda6e1d66dc3a484fc7a8)or[rocsparse_matrix_type_triangular](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a73d9ef5e5e18209f9f10a5885d3e15ba).**uplo**–**[in]**[rocsparse_fill_mode_lower](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a1eb644f6f2701329635e07d91919d37e)or[rocsparse_fill_mode_upper](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a905f490c7fc5a59e8a635938cec0d004).**storage**–**[in]**[rocsparse_storage_mode_sorted](enumerations.html#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13ea73d28ef281d17b58cf46a846fd515fff)or[rocsparse_storage_mode_sorted](enumerations.html#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13ea73d28ef281d17b58cf46a846fd515fff).**data_status**–**[out]**modified to indicate the status of the data**temp_buffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_value**–`idx_base`

or`matrix_type`

or`uplo`

or`storage`

is invalid.**rocsparse_status_invalid_size**–`m`

`n`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`csc_val`

,`csc_col_ptr`

,`csc_row_ind`

,`temp_buffer`

or`data_status`

pointer is invalid.



## rocsparse_check_matrix_coo_buffer_size()[#](#rocsparse-check-matrix-coo-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scheck_matrix_coo_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const float *coo_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_row_ind, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_col_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage, size_t *buffer_size)[#](#_CPPv439rocsparse_scheck_matrix_coo_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcheck_matrix_coo_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const double *coo_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_row_ind, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_col_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage, size_t *buffer_size)[#](#_CPPv439rocsparse_dcheck_matrix_coo_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPKdPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccheck_matrix_coo_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*coo_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_row_ind, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_col_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage, size_t *buffer_size)[#](#_CPPv439rocsparse_ccheck_matrix_coo_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcheck_matrix_coo_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*coo_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_row_ind, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_col_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage, size_t *buffer_size)[#](#_CPPv439rocsparse_zcheck_matrix_coo_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP6size_t) `rocsparse_check_matrix_coo_buffer_size`

computes the required buffer size needed when calling[rocsparse_Xcheck_matrix_coo()](#rocsparse__check__matrix__coo_8h_1a733174d6846a6c021be8adb9aabb888a).Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix.**n**–**[in]**number of columns of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**coo_val**–**[in]**array of`nnz`

elements of the sparse COO matrix.**coo_row_ind**–**[in]**array of`nnz`

elements containing the row indices of the sparse COO matrix.**coo_col_ind**–**[in]**array of`nnz`

elements containing the column indices of the sparse COO matrix.**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**matrix_type**–**[in]**[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03),[rocsparse_matrix_type_symmetric](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8340a3909d43b5b6bedd8ecc928605a5),[rocsparse_matrix_type_hermitian](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75aa30592e2cccfda6e1d66dc3a484fc7a8)or[rocsparse_matrix_type_triangular](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a73d9ef5e5e18209f9f10a5885d3e15ba).**uplo**–**[in]**[rocsparse_fill_mode_lower](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a1eb644f6f2701329635e07d91919d37e)or[rocsparse_fill_mode_upper](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a905f490c7fc5a59e8a635938cec0d004).**storage**–**[in]**[rocsparse_storage_mode_sorted](enumerations.html#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13ea73d28ef281d17b58cf46a846fd515fff)or[rocsparse_storage_mode_sorted](enumerations.html#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13ea73d28ef281d17b58cf46a846fd515fff).**buffer_size**–**[out]**number of bytes of the temporary storage buffer required by[rocsparse_Xcheck_matrix_coo()](#rocsparse__check__matrix__coo_8h_1a733174d6846a6c021be8adb9aabb888a).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_value**–`idx_base`

or`matrix_type`

or`uplo`

or`storage`

is invalid.**rocsparse_status_invalid_size**–`m`

`n`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`coo_val`

,`coo_row_ind`

,`coo_col_ind`

or`buffer_size`

pointer is invalid.



## rocsparse_check_matrix_coo()[#](#rocsparse-check-matrix-coo)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scheck_matrix_coo([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const float *coo_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_row_ind, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_col_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage,[rocsparse_data_status](enumerations.html#_CPPv421rocsparse_data_status)*data_status, void *temp_buffer)[#](#_CPPv427rocsparse_scheck_matrix_coo16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP21rocsparse_data_statusPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcheck_matrix_coo([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const double *coo_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_row_ind, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_col_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage,[rocsparse_data_status](enumerations.html#_CPPv421rocsparse_data_status)*data_status, void *temp_buffer)[#](#_CPPv427rocsparse_dcheck_matrix_coo16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPKdPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP21rocsparse_data_statusPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccheck_matrix_coo([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*coo_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_row_ind, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_col_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage,[rocsparse_data_status](enumerations.html#_CPPv421rocsparse_data_status)*data_status, void *temp_buffer)[#](#_CPPv427rocsparse_ccheck_matrix_coo16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP21rocsparse_data_statusPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcheck_matrix_coo([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*coo_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_row_ind, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_col_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage,[rocsparse_data_status](enumerations.html#_CPPv421rocsparse_data_status)*data_status, void *temp_buffer)[#](#_CPPv427rocsparse_zcheck_matrix_coo16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP21rocsparse_data_statusPv) Check matrix to see if it is valid.

`rocsparse_check_matrix_coo`

checks if the input COO matrix is valid. It performs basic sanity checks on the input matrix and tries to detect issues in the data. This includes looking for ‘nan’ or ‘inf’ values in the data arrays, invalid row/column indices, whether the matrix is triangular or not, whether there are duplicate row/column indices or whether the row/column indices are not sorted when they should be. If an issue is found, it is written to the`data_status`

parameter.Performing the above checks involves two steps. First the user calls

`rocsparse_Xcheck_matrix_coo_buffer_size`

in order to determine the required buffer size. The user then allocates this buffer and passes it to`rocsparse_Xcheck_matrix_coo`

. Any issues detected will be written to the`data_status`

parameter which is always a host variable regardless of pointer mode.// 1 2 0 0 // 0 3 4 0 // 0 0 1 1 // 0 0 0 2 std::vector<int> hcoo_row_ind = {0, 0, -1, 1, 2, 2, 3}; // <---- invalid row index std::vector<int> hcoo_col_ind = {0, 1, 1, 2, 2, 3, 3}; std::vector<float> hcoo_val = {1, 2, 3, 4, 1, 1, 2}; int m = 4; int n = 4; int nnz = 7; int* dcoo_row_ind = nullptr; int* dcoo_col_ind = nullptr; float* dcoo_val = nullptr; hipMalloc((void**)&dcoo_row_ind, sizeof(int) * nnz); hipMalloc((void**)&dcoo_col_ind, sizeof(int) * nnz); hipMalloc((void**)&dcoo_val, sizeof(float) * nnz); hipMemcpy(dcoo_row_ind, hcoo_row_ind.data(), sizeof(int) * nnz, hipMemcpyHostToDevice); hipMemcpy(dcoo_col_ind, hcoo_col_ind.data(), sizeof(int) * nnz, hipMemcpyHostToDevice); hipMemcpy(dcoo_val, hcoo_val.data(), sizeof(float) * nnz, hipMemcpyHostToDevice); rocsparse_handle handle; rocsparse_create_handle(&handle); const rocsparse_index_base idx_base = rocsparse_index_base_zero; const rocsparse_fill_mode fill_mode = rocsparse_fill_mode_upper; const rocsparse_matrix_type matrix_type = rocsparse_matrix_type_triangular; const rocsparse_storage_mode storage_mode = rocsparse_storage_mode_sorted; rocsparse_data_status data_status; size_t buffer_size; rocsparse_scheck_matrix_coo_buffer_size(handle, m, n, nnz, dcoo_val, dcoo_row_ind, dcoo_col_ind, idx_base, matrix_type, fill_mode, storage_mode, &buffer_size); void* dbuffer = nullptr; hipMalloc((void**)&dbuffer, buffer_size); rocsparse_scheck_matrix_coo(handle, m, n, nnz, dcoo_val, dcoo_row_ind, dcoo_col_ind, idx_base, matrix_type, fill_mode, storage_mode, &data_status, dbuffer); std::cout << "data_status: " << data_status << std::endl; hipFree(dbuffer); rocsparse_destroy_handle(handle); hipFree(dcoo_row_ind); hipFree(dcoo_col_ind); hipFree(dcoo_val);

**Example**In this example we want to check whether a COO matrix has correct row indices. The matrix passed is invalid because it contains a -1 entry in the row indices array.


Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the sparse COO matrix.**n**–**[in]**number of columns of the sparse COO matrix.**nnz**–**[in]**number of non-zero entries of the sparse COO matrix.**coo_val**–**[in]**array of`nnz`

elements of the sparse COO matrix.**coo_row_ind**–**[in]**array of`nnz`

elements containing the row indices of the sparse COO matrix.**coo_col_ind**–**[in]**array of`nnz`

elements containing the column indices of the sparse COO matrix.**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**matrix_type**–**[in]**[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03),[rocsparse_matrix_type_symmetric](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8340a3909d43b5b6bedd8ecc928605a5),[rocsparse_matrix_type_hermitian](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75aa30592e2cccfda6e1d66dc3a484fc7a8)or[rocsparse_matrix_type_triangular](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a73d9ef5e5e18209f9f10a5885d3e15ba).**uplo**–**[in]**[rocsparse_fill_mode_lower](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a1eb644f6f2701329635e07d91919d37e)or[rocsparse_fill_mode_upper](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a905f490c7fc5a59e8a635938cec0d004).**storage**–**[in]**[rocsparse_storage_mode_sorted](enumerations.html#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13ea73d28ef281d17b58cf46a846fd515fff)or[rocsparse_storage_mode_sorted](enumerations.html#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13ea73d28ef281d17b58cf46a846fd515fff).**data_status**–**[out]**modified to indicate the status of the data**temp_buffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_value**–`idx_base`

or`matrix_type`

or`uplo`

or`storage`

is invalid.**rocsparse_status_invalid_size**–`m`

`n`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`coo_val`

,`coo_row_ind`

,`coo_col_ind`

,`temp_buffer`

or`data_status`

pointer is invalid.



## rocsparse_check_matrix_gebsr_buffer_size()[#](#rocsparse-check-matrix-gebsr-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scheck_matrix_gebsr_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, const float *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage, size_t *buffer_size)[#](#_CPPv441rocsparse_scheck_matrix_gebsr_buffer_size16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcheck_matrix_gebsr_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, const double *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage, size_t *buffer_size)[#](#_CPPv441rocsparse_dcheck_matrix_gebsr_buffer_size16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPKdPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccheck_matrix_gebsr_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage, size_t *buffer_size)[#](#_CPPv441rocsparse_ccheck_matrix_gebsr_buffer_size16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcheck_matrix_gebsr_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage, size_t *buffer_size)[#](#_CPPv441rocsparse_zcheck_matrix_gebsr_buffer_size16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP6size_t) Check matrix to see if it is valid.

`rocsparse_check_matrix_gebsr_buffer_size`

computes the required buffer size needed when calling[rocsparse_Xcheck_matrix_gebsr()](#rocsparse__check__matrix__gebsr_8h_1a0fb69daff0e887c5577090f8d9970fa8).Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dir**–**[in]**matrix storage of GEBSR blocks.**mb**–**[in]**number of block rows of the sparse GEBSR matrix.**nb**–**[in]**number of block columns of the sparse GEBSR matrix.**nnzb**–**[in]**number of non-zero blocks of the sparse GEBSR matrix.**row_block_dim**–**[in]**row block dimension of the sparse GEBSR matrix.**col_block_dim**–**[in]**column block dimension of the sparse GEBSR matrix.**bsr_val**–**[in]**array of`nnzb`

elements of the sparse GEBSR matrix.**bsr_row_ptr**–**[in]**array of`mb+1`

elements that point to the start of every row of the sparse GEBSR matrix.**bsr_col_ind**–**[in]**array of`nnzb`

elements containing the column indices of the sparse GEBSR matrix.**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**matrix_type**–**[in]**[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03),[rocsparse_matrix_type_symmetric](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8340a3909d43b5b6bedd8ecc928605a5),[rocsparse_matrix_type_hermitian](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75aa30592e2cccfda6e1d66dc3a484fc7a8)or[rocsparse_matrix_type_triangular](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a73d9ef5e5e18209f9f10a5885d3e15ba).**uplo**–**[in]**[rocsparse_fill_mode_lower](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a1eb644f6f2701329635e07d91919d37e)or[rocsparse_fill_mode_upper](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a905f490c7fc5a59e8a635938cec0d004).**storage**–**[in]**[rocsparse_storage_mode_sorted](enumerations.html#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13ea73d28ef281d17b58cf46a846fd515fff)or[rocsparse_storage_mode_sorted](enumerations.html#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13ea73d28ef281d17b58cf46a846fd515fff).**buffer_size**–**[out]**number of bytes of the temporary storage buffer required by[rocsparse_scheck_matrix_gebsr()](#rocsparse__check__matrix__gebsr_8h_1a0fb69daff0e887c5577090f8d9970fa8),[rocsparse_dcheck_matrix_gebsr()](#rocsparse__check__matrix__gebsr_8h_1aee7d77a6748962f21f8ab21d08f65f72),[rocsparse_ccheck_matrix_gebsr()](#rocsparse__check__matrix__gebsr_8h_1a70e23322edfebe46e92e09ecd58f5b94)and[rocsparse_zcheck_matrix_gebsr()](#rocsparse__check__matrix__gebsr_8h_1aa9103d42acd9688019cb420a71c50cc1).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_value**–`dir`

or`idx_base`

or`matrix_type`

or`uplo`

or`storage`

is invalid.**rocsparse_status_invalid_size**–`mb`

`nb`

`nnzb`

`row_block_dim`

or`col_block_dim`

is invalid.**rocsparse_status_invalid_pointer**–`bsr_val`

,`bsr_row_ptr`

,`bsr_col_ind`

or`buffer_size`

pointer is invalid.



## rocsparse_check_matrix_gebsr()[#](#rocsparse-check-matrix-gebsr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scheck_matrix_gebsr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, const float *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage,[rocsparse_data_status](enumerations.html#_CPPv421rocsparse_data_status)*data_status, void *temp_buffer)[#](#_CPPv429rocsparse_scheck_matrix_gebsr16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP21rocsparse_data_statusPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcheck_matrix_gebsr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, const double *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage,[rocsparse_data_status](enumerations.html#_CPPv421rocsparse_data_status)*data_status, void *temp_buffer)[#](#_CPPv429rocsparse_dcheck_matrix_gebsr16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPKdPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP21rocsparse_data_statusPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccheck_matrix_gebsr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage,[rocsparse_data_status](enumerations.html#_CPPv421rocsparse_data_status)*data_status, void *temp_buffer)[#](#_CPPv429rocsparse_ccheck_matrix_gebsr16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP21rocsparse_data_statusPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcheck_matrix_gebsr([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage,[rocsparse_data_status](enumerations.html#_CPPv421rocsparse_data_status)*data_status, void *temp_buffer)[#](#_CPPv429rocsparse_zcheck_matrix_gebsr16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP21rocsparse_data_statusPv) Check matrix to see if it is valid.

`rocsparse_check_matrix_gebsr`

checks if the input GEBSR matrix is valid. It performs basic sanity checks on the input matrix and tries to detect issues in the data. This includes looking for ‘nan’ or ‘inf’ values in the data arrays, invalid column indices and row offsets, whether the matrix is triangular or not, whether there are duplicate indices or whether the column indices are not sorted when they should be. If an issue is found, it is written to the`data_status`

parameter.Performing the above checks involves two steps. First the user calls

`rocsparse_Xcheck_matrix_gebsr_buffer_size`

in order to determine the required buffer size. The user then allocates this buffer and passes it to`rocsparse_Xcheck_matrix_gebsr`

. Any issues detected will be written to the`data_status`

parameter which is always a host variable regardless of pointer mode.// 1 2 | 0 0 // 0 3 | 0 0 // --------- // 4 5 | 7 8 // 0 6 | 0 9 std::vector<int> hbsr_row_ptr = {0, 1, 3}; std::vector<int> hbsr_col_ind = {0, 0, 1}; std::vector<float> hbsr_val = {1, 2, 0, 3, 4, 5, 0, 6, 7, 8, std::numeric_limits<double>::quiet_NaN(), 9}; //<---contains nan int mb = 2; int nb = 2; int nnzb = 3; int block_dim = 2; int* dbsr_row_ptr = nullptr; int* dbsr_col_ind = nullptr; float* dbsr_val = nullptr; hipMalloc((void**)&dbsr_row_ptr, sizeof(int) * (mb + 1)); hipMalloc((void**)&dbsr_col_ind, sizeof(int) * nnzb); hipMalloc((void**)&dbsr_val, sizeof(float) * nnzb * block_dim * block_dim); hipMemcpy(dbsr_row_ptr, hbsr_row_ptr.data(), sizeof(int) * (mb + 1), hipMemcpyHostToDevice); hipMemcpy(dbsr_col_ind, hbsr_col_ind.data(), sizeof(int) * nnzb, hipMemcpyHostToDevice); hipMemcpy(dbsr_val, hbsr_val.data(), sizeof(float) * nnzb * block_dim * block_dim, hipMemcpyHostToDevice); rocsparse_handle handle; rocsparse_create_handle(&handle); const rocsparse_direction direction = rocsparse_direction_row; const rocsparse_index_base idx_base = rocsparse_index_base_zero; const rocsparse_fill_mode fill_mode = rocsparse_fill_mode_upper; const rocsparse_matrix_type matrix_type = rocsparse_matrix_type_triangular; const rocsparse_storage_mode storage_mode = rocsparse_storage_mode_sorted; rocsparse_data_status data_status; size_t buffer_size; rocsparse_scheck_matrix_gebsr_buffer_size(handle, direction, mb, nb, nnzb, block_dim, block_dim, dbsr_val, dbsr_row_ptr, dbsr_col_ind, idx_base, matrix_type, fill_mode, storage_mode, &buffer_size); void* dbuffer = nullptr; hipMalloc((void**)&dbuffer, buffer_size); rocsparse_scheck_matrix_gebsr(handle, direction, mb, nb, nnzb, block_dim, block_dim, dbsr_val, dbsr_row_ptr, dbsr_col_ind, idx_base, matrix_type, fill_mode, storage_mode, &data_status, dbuffer); std::cout << "data_status: " << data_status << std::endl; hipFree(dbuffer); rocsparse_destroy_handle(handle); hipFree(dbsr_row_ptr); hipFree(dbsr_col_ind); hipFree(dbsr_val);

**Example**In this example we want to check whether a GEBSR matrix has valid values. The matrix passed is invalid because it contains a nan entry in the values array.


Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dir**–**[in]**matrix storage of GEBSR blocks.**mb**–**[in]**number of block rows of the sparse GEBSR matrix.**nb**–**[in]**number of block columns of the sparse GEBSR matrix.**nnzb**–**[in]**number of non-zero blocks of the sparse GEBSR matrix.**row_block_dim**–**[in]**row block dimension of the sparse GEBSR matrix.**col_block_dim**–**[in]**column block dimension of the sparse GEBSR matrix.**bsr_val**–**[in]**array of`nnzb`

elements of the sparse GEBSR matrix.**bsr_row_ptr**–**[in]**array of`mb+1`

elements that point to the start of every row of the sparse GEBSR matrix.**bsr_col_ind**–**[in]**array of`nnzb`

elements containing the column indices of the sparse GEBSR matrix.**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**matrix_type**–**[in]**[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03),[rocsparse_matrix_type_symmetric](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8340a3909d43b5b6bedd8ecc928605a5),[rocsparse_matrix_type_hermitian](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75aa30592e2cccfda6e1d66dc3a484fc7a8)or[rocsparse_matrix_type_triangular](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a73d9ef5e5e18209f9f10a5885d3e15ba).**uplo**–**[in]**[rocsparse_fill_mode_lower](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a1eb644f6f2701329635e07d91919d37e)or[rocsparse_fill_mode_upper](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a905f490c7fc5a59e8a635938cec0d004).**storage**–**[in]**[rocsparse_storage_mode_sorted](enumerations.html#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13ea73d28ef281d17b58cf46a846fd515fff)or[rocsparse_storage_mode_sorted](enumerations.html#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13ea73d28ef281d17b58cf46a846fd515fff).**data_status**–**[out]**modified to indicate the status of the data**temp_buffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_value**–`dir`

or`idx_base`

or`matrix_type`

or`uplo`

or`storage`

is invalid.**rocsparse_status_invalid_size**–`mb`

`nb`

`nnzb`

`row_block_dim`

or`col_block_dim`

is invalid.**rocsparse_status_invalid_pointer**–`bsr_val`

,`bsr_row_ptr`

,`bsr_col_ind`

,`temp_buffer`

or`data_status`

pointer is invalid.



## rocsparse_check_matrix_gebsc_buffer_size()[#](#rocsparse-check-matrix-gebsc-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scheck_matrix_gebsc_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, const float *bsc_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsc_col_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsc_row_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage, size_t *buffer_size)[#](#_CPPv441rocsparse_scheck_matrix_gebsc_buffer_size16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcheck_matrix_gebsc_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, const double *bsc_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsc_col_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsc_row_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage, size_t *buffer_size)[#](#_CPPv441rocsparse_dcheck_matrix_gebsc_buffer_size16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPKdPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccheck_matrix_gebsc_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsc_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsc_col_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsc_row_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage, size_t *buffer_size)[#](#_CPPv441rocsparse_ccheck_matrix_gebsc_buffer_size16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcheck_matrix_gebsc_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsc_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsc_col_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsc_row_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage, size_t *buffer_size)[#](#_CPPv441rocsparse_zcheck_matrix_gebsc_buffer_size16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP6size_t) `rocsparse_check_matrix_gebsc_buffer_size`

computes the required buffer size needed when calling[rocsparse_Xcheck_matrix_gebsc()](#rocsparse__check__matrix__gebsc_8h_1ad55671481469a76b58bb2f23f27e4d1b).Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dir**–**[in]**matrix storage of GEBSC blocks.**mb**–**[in]**number of block rows of the sparse GEBSC matrix.**nb**–**[in]**number of block columns of the sparse GEBSC matrix.**nnzb**–**[in]**number of non-zero blocks of the sparse GEBSC matrix.**row_block_dim**–**[in]**row block dimension of the sparse GEBSC matrix.**col_block_dim**–**[in]**column block dimension of the sparse GEBSC matrix.**bsc_val**–**[in]**array of`nnzb`

elements of the sparse GEBSC matrix.**bsc_col_ptr**–**[in]**array of`nb+1`

elements that point to the start of every column of the sparse GEBSC matrix.**bsc_row_ind**–**[in]**array of`nnzb`

elements containing the row indices of the sparse GEBSC matrix.**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**matrix_type**–**[in]**[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03),[rocsparse_matrix_type_symmetric](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8340a3909d43b5b6bedd8ecc928605a5),[rocsparse_matrix_type_hermitian](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75aa30592e2cccfda6e1d66dc3a484fc7a8)or[rocsparse_matrix_type_triangular](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a73d9ef5e5e18209f9f10a5885d3e15ba).**uplo**–**[in]**[rocsparse_fill_mode_lower](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a1eb644f6f2701329635e07d91919d37e)or[rocsparse_fill_mode_upper](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a905f490c7fc5a59e8a635938cec0d004).**storage**–**[in]**[rocsparse_storage_mode_sorted](enumerations.html#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13ea73d28ef281d17b58cf46a846fd515fff)or[rocsparse_storage_mode_sorted](enumerations.html#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13ea73d28ef281d17b58cf46a846fd515fff).**buffer_size**–**[out]**number of bytes of the temporary storage buffer required by[rocsparse_scheck_matrix_gebsc()](#rocsparse__check__matrix__gebsc_8h_1ad55671481469a76b58bb2f23f27e4d1b),[rocsparse_dcheck_matrix_gebsc()](#rocsparse__check__matrix__gebsc_8h_1a3697e6b402bb56858509ff820a82efaa),[rocsparse_ccheck_matrix_gebsc()](#rocsparse__check__matrix__gebsc_8h_1a4e18e6cae838ce9daa8d835f605f6cc1)and[rocsparse_zcheck_matrix_gebsc()](#rocsparse__check__matrix__gebsc_8h_1a3aeaf357fa4d8954c62ee5768cf886cb).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_value**–`dir`

or`idx_base`

or`matrix_type`

or`uplo`

or`storage`

is invalid.**rocsparse_status_invalid_size**–`mb`

`nb`

`nnzb`

`row_block_dim`

or`col_block_dim`

is invalid.**rocsparse_status_invalid_pointer**–`bsc_val`

,`bsc_col_ptr`

,`bsc_row_ind`

or`buffer_size`

pointer is invalid.



## rocsparse_check_matrix_gebsc()[#](#rocsparse-check-matrix-gebsc)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scheck_matrix_gebsc([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, const float *bsc_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsc_col_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsc_row_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage,[rocsparse_data_status](enumerations.html#_CPPv421rocsparse_data_status)*data_status, void *temp_buffer)[#](#_CPPv429rocsparse_scheck_matrix_gebsc16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP21rocsparse_data_statusPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcheck_matrix_gebsc([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, const double *bsc_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsc_col_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsc_row_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage,[rocsparse_data_status](enumerations.html#_CPPv421rocsparse_data_status)*data_status, void *temp_buffer)[#](#_CPPv429rocsparse_dcheck_matrix_gebsc16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPKdPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP21rocsparse_data_statusPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccheck_matrix_gebsc([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsc_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsc_col_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsc_row_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage,[rocsparse_data_status](enumerations.html#_CPPv421rocsparse_data_status)*data_status, void *temp_buffer)[#](#_CPPv429rocsparse_ccheck_matrix_gebsc16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP21rocsparse_data_statusPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcheck_matrix_gebsc([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsc_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsc_col_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsc_row_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage,[rocsparse_data_status](enumerations.html#_CPPv421rocsparse_data_status)*data_status, void *temp_buffer)[#](#_CPPv429rocsparse_zcheck_matrix_gebsc16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP21rocsparse_data_statusPv) Check matrix to see if it is valid.

`rocsparse_check_matrix_gebsc`

checks if the input GEBSC matrix is valid. It performs basic sanity checks on the input matrix and tries to detect issues in the data. This includes looking for ‘nan’ or ‘inf’ values in the data arrays, invalid row indices or column offsets, whether the matrix is triangular or not, whether there are duplicate indices or whether the row indices are not sorted when they should be. If an issue is found, it is written to the`data_status`

parameter.Performing the above checks involves two steps. First the user calls

`rocsparse_Xcheck_matrix_gebsr_buffer_size`

in order to determine the required buffer size. The user then allocates this buffer and passes it to`rocsparse_Xcheck_matrix_gebsr`

. Any issues detected will be written to the`data_status`

parameter which is always a host variable regardless of pointer mode.Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dir**–**[in]**matrix storage of GEBSC blocks.**mb**–**[in]**number of block rows of the sparse GEBSC matrix.**nb**–**[in]**number of block columns of the sparse GEBSC matrix.**nnzb**–**[in]**number of non-zero blocks of the sparse GEBSC matrix.**row_block_dim**–**[in]**row block dimension of the sparse GEBSC matrix.**col_block_dim**–**[in]**column block dimension of the sparse GEBSC matrix.**bsc_val**–**[in]**array of`nnzb`

elements of the sparse GEBSC matrix.**bsc_col_ptr**–**[in]**array of`nb+1`

elements that point to the start of every column of the sparse GEBSC matrix.**bsc_row_ind**–**[in]**array of`nnzb`

elements containing the row indices of the sparse GEBSC matrix.**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**matrix_type**–**[in]**[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03),[rocsparse_matrix_type_symmetric](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8340a3909d43b5b6bedd8ecc928605a5),[rocsparse_matrix_type_hermitian](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75aa30592e2cccfda6e1d66dc3a484fc7a8)or[rocsparse_matrix_type_triangular](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a73d9ef5e5e18209f9f10a5885d3e15ba).**uplo**–**[in]**[rocsparse_fill_mode_lower](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a1eb644f6f2701329635e07d91919d37e)or[rocsparse_fill_mode_upper](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a905f490c7fc5a59e8a635938cec0d004).**storage**–**[in]**[rocsparse_storage_mode_sorted](enumerations.html#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13ea73d28ef281d17b58cf46a846fd515fff)or[rocsparse_storage_mode_sorted](enumerations.html#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13ea73d28ef281d17b58cf46a846fd515fff).**data_status**–**[out]**modified to indicate the status of the data**temp_buffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_value**–`dir`

or`idx_base`

or`matrix_type`

or`uplo`

or`storage`

is invalid.**rocsparse_status_invalid_size**–`mb`

`nb`

`nnzb`

`row_block_dim`

or`col_block_dim`

is invalid.**rocsparse_status_invalid_pointer**–`bsc_val`

,`bsc_col_ptr`

,`bsc_row_ind`

,`temp_buffer`

or`data_status`

pointer is invalid.



## rocsparse_check_matrix_ell_buffer_size()[#](#rocsparse-check-matrix-ell-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scheck_matrix_ell_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)ell_width, const float *ell_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*ell_col_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage, size_t *buffer_size)[#](#_CPPv439rocsparse_scheck_matrix_ell_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPKfPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcheck_matrix_ell_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)ell_width, const double *ell_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*ell_col_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage, size_t *buffer_size)[#](#_CPPv439rocsparse_dcheck_matrix_ell_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPKdPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccheck_matrix_ell_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)ell_width, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*ell_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*ell_col_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage, size_t *buffer_size)[#](#_CPPv439rocsparse_ccheck_matrix_ell_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPK23rocsparse_float_complexPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcheck_matrix_ell_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)ell_width, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*ell_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*ell_col_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage, size_t *buffer_size)[#](#_CPPv439rocsparse_zcheck_matrix_ell_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPK24rocsparse_double_complexPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP6size_t) `rocsparse_check_matrix_ell_buffer_size`

computes the required buffer size needed when calling[rocsparse_Xcheck_matrix_ell()](#rocsparse__check__matrix__ell_8h_1a98e8ae4ec7120ce229c99e1a6617797c).Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the sparse ELL matrix.**n**–**[in]**number of columns of the sparse ELL matrix.**ell_width**–**[in]**number of non-zero elements per row of the sparse ELL matrix.**ell_val**–**[in]**array that contains the elements of the sparse ELL matrix. Padded elements should be zero.**ell_col_ind**–**[in]**array that contains the column indices of the sparse ELL matrix. Padded column indices should be -1.**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**matrix_type**–**[in]**[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03),[rocsparse_matrix_type_symmetric](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8340a3909d43b5b6bedd8ecc928605a5),[rocsparse_matrix_type_hermitian](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75aa30592e2cccfda6e1d66dc3a484fc7a8)or[rocsparse_matrix_type_triangular](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a73d9ef5e5e18209f9f10a5885d3e15ba).**uplo**–**[in]**[rocsparse_fill_mode_lower](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a1eb644f6f2701329635e07d91919d37e)or[rocsparse_fill_mode_upper](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a905f490c7fc5a59e8a635938cec0d004).**storage**–**[in]**[rocsparse_storage_mode_sorted](enumerations.html#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13ea73d28ef281d17b58cf46a846fd515fff)or[rocsparse_storage_mode_sorted](enumerations.html#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13ea73d28ef281d17b58cf46a846fd515fff).**buffer_size**–**[out]**number of bytes of the temporary storage buffer required by[rocsparse_scheck_matrix_ell()](#rocsparse__check__matrix__ell_8h_1a98e8ae4ec7120ce229c99e1a6617797c),[rocsparse_dcheck_matrix_ell()](#rocsparse__check__matrix__ell_8h_1abc318fb37b7c9977f9d62220910e244f),[rocsparse_ccheck_matrix_ell()](#rocsparse__check__matrix__ell_8h_1afe29e9cd7d0a242ccec3cf7682e3a0fe)and[rocsparse_zcheck_matrix_ell()](#rocsparse__check__matrix__ell_8h_1af689a07a25e7aa17fa48860b4fcd1fa8).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_value**–`idx_base`

or`matrix_type`

or`uplo`

or`storage`

is invalid.**rocsparse_status_invalid_size**–`m`

`n`

or`ell_width`

is invalid.**rocsparse_status_invalid_pointer**–`ell_val`

,`ell_col_ind`

or`buffer_size`

pointer is invalid.



## rocsparse_check_matrix_ell()[#](#rocsparse-check-matrix-ell)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scheck_matrix_ell([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)ell_width, const float *ell_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*ell_col_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage,[rocsparse_data_status](enumerations.html#_CPPv421rocsparse_data_status)*data_status, void *temp_buffer)[#](#_CPPv427rocsparse_scheck_matrix_ell16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPKfPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP21rocsparse_data_statusPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcheck_matrix_ell([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)ell_width, const double *ell_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*ell_col_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage,[rocsparse_data_status](enumerations.html#_CPPv421rocsparse_data_status)*data_status, void *temp_buffer)[#](#_CPPv427rocsparse_dcheck_matrix_ell16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPKdPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP21rocsparse_data_statusPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccheck_matrix_ell([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)ell_width, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*ell_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*ell_col_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage,[rocsparse_data_status](enumerations.html#_CPPv421rocsparse_data_status)*data_status, void *temp_buffer)[#](#_CPPv427rocsparse_ccheck_matrix_ell16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPK23rocsparse_float_complexPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP21rocsparse_data_statusPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcheck_matrix_ell([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)ell_width, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*ell_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*ell_col_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage,[rocsparse_data_status](enumerations.html#_CPPv421rocsparse_data_status)*data_status, void *temp_buffer)[#](#_CPPv427rocsparse_zcheck_matrix_ell16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPK24rocsparse_double_complexPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP21rocsparse_data_statusPv) Check matrix to see if it is valid.

`rocsparse_check_matrix_ell`

checks if the input ELL matrix is valid. It performs basic sanity checks on the input matrix and tries to detect issues in the data. This includes looking for ‘nan’ or ‘inf’ values in the data arrays, invalid column indices, whether there are duplicate indices or whether the column indices are not sorted when they should be. If an issue is found, it is written to the`data_status`

parameter.Performing the above checks involves two steps. First the user calls

`rocsparse_Xcheck_matrix_ell_buffer_size`

in order to determine the required buffer size. The user then allocates this buffer and passes it to`rocsparse_Xcheck_matrix_ell`

. Any issues detected will be written to the`data_status`

parameter which is always a host variable regardless of pointer mode.Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the sparse ELL matrix.**n**–**[in]**number of columns of the sparse ELL matrix.**ell_width**–**[in]**number of non-zero elements per row of the sparse ELL matrix.**ell_val**–**[in]**array that contains the elements of the sparse ELL matrix. Padded elements should be zero.**ell_col_ind**–**[in]**array that contains the column indices of the sparse ELL matrix. Padded column indices should be -1.**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**matrix_type**–**[in]**[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03),[rocsparse_matrix_type_symmetric](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8340a3909d43b5b6bedd8ecc928605a5),[rocsparse_matrix_type_hermitian](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75aa30592e2cccfda6e1d66dc3a484fc7a8)or[rocsparse_matrix_type_triangular](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a73d9ef5e5e18209f9f10a5885d3e15ba).**uplo**–**[in]**[rocsparse_fill_mode_lower](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a1eb644f6f2701329635e07d91919d37e)or[rocsparse_fill_mode_upper](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a905f490c7fc5a59e8a635938cec0d004).**storage**–**[in]**[rocsparse_storage_mode_sorted](enumerations.html#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13ea73d28ef281d17b58cf46a846fd515fff)or[rocsparse_storage_mode_sorted](enumerations.html#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13ea73d28ef281d17b58cf46a846fd515fff).**data_status**–**[out]**modified to indicate the status of the data**temp_buffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_value**–`idx_base`

or`matrix_type`

or`uplo`

or`storage`

is invalid.**rocsparse_status_invalid_size**–`m`

`n`

or`ell_width`

is invalid.**rocsparse_status_invalid_pointer**–`ell_val`

,`ell_col_ind`

,`temp_buffer`

or`data_status`

pointer is invalid.



## rocsparse_check_matrix_hyb_buffer_size()[#](#rocsparse-check-matrix-hyb-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_check_matrix_hyb_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, const[rocsparse_hyb_mat](types.html#_CPPv417rocsparse_hyb_mat)hyb,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage, size_t *buffer_size)[#](#_CPPv438rocsparse_check_matrix_hyb_buffer_size16rocsparse_handleK17rocsparse_hyb_mat20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP6size_t) Check matrix to see if it is valid.

`rocsparse_check_matrix_hyb_buffer_size`

computes the required buffer size needed when calling[rocsparse_check_matrix_hyb](#rocsparse__check__matrix__hyb_8h_1af80b3b0dbcd26862e1dc777119b55f05).Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**hyb**–**[in]**matrix in HYB storage format.**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**matrix_type**–**[in]**[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03),[rocsparse_matrix_type_symmetric](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8340a3909d43b5b6bedd8ecc928605a5),[rocsparse_matrix_type_hermitian](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75aa30592e2cccfda6e1d66dc3a484fc7a8)or[rocsparse_matrix_type_triangular](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a73d9ef5e5e18209f9f10a5885d3e15ba).**uplo**–**[in]**[rocsparse_fill_mode_lower](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a1eb644f6f2701329635e07d91919d37e)or[rocsparse_fill_mode_upper](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a905f490c7fc5a59e8a635938cec0d004).**storage**–**[in]**[rocsparse_storage_mode_sorted](enumerations.html#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13ea73d28ef281d17b58cf46a846fd515fff)or[rocsparse_storage_mode_sorted](enumerations.html#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13ea73d28ef281d17b58cf46a846fd515fff).**buffer_size**–**[out]**number of bytes of the temporary storage buffer required by[rocsparse_check_matrix_hyb()](#rocsparse__check__matrix__hyb_8h_1af80b3b0dbcd26862e1dc777119b55f05).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_value**–`idx_base`

or`matrix_type`

or`uplo`

or`storage`

is invalid.**rocsparse_status_invalid_pointer**–`hyb`

or`buffer_size`

pointer is invalid.



## rocsparse_check_matrix_hyb()[#](#rocsparse-check-matrix-hyb)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_check_matrix_hyb([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, const[rocsparse_hyb_mat](types.html#_CPPv417rocsparse_hyb_mat)hyb,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)matrix_type,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)uplo,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage,[rocsparse_data_status](enumerations.html#_CPPv421rocsparse_data_status)*data_status, void *temp_buffer)[#](#_CPPv426rocsparse_check_matrix_hyb16rocsparse_handleK17rocsparse_hyb_mat20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP21rocsparse_data_statusPv) Check matrix to see if it is valid.

`rocsparse_check_matrix_hyb`

checks if the input HYB matrix is valid. It performs basic sanity checks on the input matrix and tries to detect issues in the data. This includes looking for ‘nan’ or ‘inf’ values in the data arrays, invalid row/column indices, whether the matrix is triangular or not, whether there are duplicate indices or whether the row/column indices are not sorted when they should be. If an issue is found, it is written to the`data_status`

parameter.Performing the above checks involves two steps. First the user calls

`rocsparse_Xcheck_matrix_hyb_buffer_size`

in order to determine the required buffer size. The user then allocates this buffer and passes it to`rocsparse_Xcheck_matrix_hyb`

. Any issues detected will be written to the`data_status`

parameter which is always a host variable regardless of pointer mode.Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**hyb**–**[in]**matrix in HYB storage format.**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**matrix_type**–**[in]**[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03),[rocsparse_matrix_type_symmetric](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8340a3909d43b5b6bedd8ecc928605a5),[rocsparse_matrix_type_hermitian](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75aa30592e2cccfda6e1d66dc3a484fc7a8)or[rocsparse_matrix_type_triangular](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a73d9ef5e5e18209f9f10a5885d3e15ba).**uplo**–**[in]**[rocsparse_fill_mode_lower](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a1eb644f6f2701329635e07d91919d37e)or[rocsparse_fill_mode_upper](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a905f490c7fc5a59e8a635938cec0d004).**storage**–**[in]**[rocsparse_storage_mode_sorted](enumerations.html#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13ea73d28ef281d17b58cf46a846fd515fff)or[rocsparse_storage_mode_sorted](enumerations.html#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13ea73d28ef281d17b58cf46a846fd515fff).**data_status**–**[out]**modified to indicate the status of the data**temp_buffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_value**–`idx_base`

or`matrix_type`

or`uplo`

or`storage`

is invalid.**rocsparse_status_invalid_pointer**–`hyb`

or`data_status`

pointer is invalid.
