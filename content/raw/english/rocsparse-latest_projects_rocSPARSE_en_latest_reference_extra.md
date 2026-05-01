---
title: "Sparse extra functions &#8212; rocSPARSE 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocSPARSE/en/latest/reference/extra.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:17:01.063538+00:00
content_hash: "fbde4588b48fd6e1"
---

# Sparse extra functions[#](#sparse-extra-functions)

This module contains all sparse extra routines.

The sparse extra routines describe operations that manipulate sparse matrices.

The routines in this module do not support execution in a `hipGraph`

context.

## rocsparse_bsrgeam_nnzb()[#](#rocsparse-bsrgeam-nnzb)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_bsrgeam_nnzb([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_B, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnzb_C)[#](#_CPPv422rocsparse_bsrgeam_nnzb16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descrP13rocsparse_intP13rocsparse_int) `rocsparse_bsrgeam_nnzb`

computes the total BSR non-zero elements and the BSR row offsets, that point to the start of every row of the sparse BSR matrix, of the resulting matrix C. It is assumed that`bsr_row_ptr_C`

has been allocated with size`mb+1`

.Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dir**–**[in]**direction that specifies whether to count nonzero elements by[rocsparse_direction_row](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca40d95f05d0cd4ad3c89465959c58943e)or by[rocsparse_direction_column](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca23355bb7b606c550ba61c781bcecfc5b)in the BSR matrices \(A\), \(B\), and \(C\).**mb**–**[in]**number of block rows in the sparse BSR matrix \(op(A)\) and \(C\).**nb**–**[in]**number of block columns of the sparse BSR matrix \(op(B)\) and \(C\).**block_dim**–**[in]**the block dimension of the BSR matrix \(A\). Between 1 and m where`m=mb*block_dim`

.**descr_A**–**[in]**descriptor of the sparse BSR matrix \(A\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**nnzb_A**–**[in]**number of non-zero block entries of the sparse BSR matrix \(A\).**bsr_row_ptr_A**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix \(A\).**bsr_col_ind_A**–**[in]**array of`nnzb_A`

elements containing the column indices of the sparse BSR matrix \(A\).**descr_B**–**[in]**descriptor of the sparse BSR matrix \(B\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**nnzb_B**–**[in]**number of non-zero block entries of the sparse BSR matrix \(B\).**bsr_row_ptr_B**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix \(B\).**bsr_col_ind_B**–**[in]**array of`nnzb_B`

elements containing the block column indices of the sparse BSR matrix \(B\).**descr_C**–**[in]**descriptor of the sparse BSR matrix \(C\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**bsr_row_ptr_C**–**[out]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix \(C\).**nnzb_C**–**[out]**pointer to the number of non-zero block entries of the sparse BSR matrix \(C\).`nnzb_C`

can be a host or device pointer.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`mb`

,`nb`

,`kb`

,`nnzb_A`

or`nnzb_B`

is invalid.**rocsparse_status_invalid_pointer**–`descr_A`

,`bsr_row_ptr_A`

,`bsr_col_ind_A`

,`descr_B`

,`bsr_row_ptr_B`

,`bsr_col_ind_B`

,`descr_C`

,`bsr_row_ptr_C`

or`nnzb_C`

is invalid.**rocsparse_status_not_implemented**–`rocsparse_matrix_type`

!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_bsrgeam()[#](#rocsparse-bsrgeam)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sbsrgeam([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim, const float *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb_A, const float *bsr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_A, const float *beta, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb_B, const float *bsr_val_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_B, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_C, float *bsr_val_C, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_C)[#](#_CPPv418rocsparse_sbsrgeam16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descr13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_intPKfK19rocsparse_mat_descr13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descrPfPK13rocsparse_intP13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dbsrgeam([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim, const double *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb_A, const double *bsr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_A, const double *beta, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb_B, const double *bsr_val_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_B, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_C, double *bsr_val_C, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_C)[#](#_CPPv418rocsparse_dbsrgeam16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_intPKdK19rocsparse_mat_descr13rocsparse_intPKdPK13rocsparse_intPK13rocsparse_intPKdK19rocsparse_mat_descr13rocsparse_intPKdPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descrPdPK13rocsparse_intP13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cbsrgeam([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb_A, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_A, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*beta, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb_B, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsr_val_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_B, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_C,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsr_val_C, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_C)[#](#_CPPv418rocsparse_cbsrgeam16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_intPK23rocsparse_float_complexK19rocsparse_mat_descr13rocsparse_intPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_intPK23rocsparse_float_complexK19rocsparse_mat_descr13rocsparse_intPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descrP23rocsparse_float_complexPK13rocsparse_intP13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zbsrgeam([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb_A, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_A, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*beta, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb_B, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsr_val_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_B, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_C,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsr_val_C, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_C)[#](#_CPPv418rocsparse_zbsrgeam16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_intPK24rocsparse_double_complexK19rocsparse_mat_descr13rocsparse_intPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_intPK24rocsparse_double_complexK19rocsparse_mat_descr13rocsparse_intPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descrP24rocsparse_double_complexPK13rocsparse_intP13rocsparse_int) Sparse matrix sparse matrix addition using BSR storage format.

`rocsparse_bsrgeam`

multiplies the scalar \(\alpha\) with the sparse \(m \times n\) matrix \(A\), defined in BSR storage format, multiplies the scalar \(\beta\) with the sparse \(mb \times nb\) matrix \(B\), defined in BSR storage format, and adds both resulting matrices to obtain the sparse \(mb \times nb\) matrix \(C\), defined in BSR storage format, such that\[ C := \alpha \cdot A + \beta \cdot B. \]It is assumed that

`bsr_row_ptr_C`

has already been filled and that`bsr_val_C`

and`bsr_col_ind_C`

are allocated by the user.`bsr_row_ptr_C`

and allocation size of`bsr_col_ind_C`

and`bsr_val_C`

is defined by the number of non-zero block elements of the sparse BSR matrix C. Both can be obtained by[rocsparse_bsrgeam_nnzb()](#rocsparse__bsrgeam_8h_1af1b68a1d0cf3a226de10e3b8a54d0303).**Example**This example adds two CSR matrices.

int main() { // Initialize scalar multipliers float alpha = 1.0f; float beta = 1.0f; // Define matrix dimensions and block size rocsparse_int mb = 2; // Number of block rows rocsparse_int nb = 2; // Number of block columns rocsparse_int block_dim = 2; // Block dimension // Create rocsparse handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Create matrix descriptors rocsparse_mat_descr descr_A; rocsparse_mat_descr descr_B; rocsparse_mat_descr descr_C; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr_A)); ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr_B)); ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr_C)); // Set pointer mode ROCSPARSE_CHECK(rocsparse_set_pointer_mode(handle, rocsparse_pointer_mode_host)); // Define host arrays for BSR matrices A and B rocsparse_int nnzb_A = 3; // Number of non-zero blocks in A rocsparse_int nnzb_B = 3; // Number of non-zero blocks in B rocsparse_int h_bsr_row_ptr_A[] = {0, 1, 3}; rocsparse_int h_bsr_col_ind_A[] = {0, 0, 1}; float h_bsr_val_A[] = {1, 0, 4, 2, 0, 3, 5, 0, 0, 0, 0, 9}; rocsparse_int h_bsr_row_ptr_B[] = {0, 1, 3}; rocsparse_int h_bsr_col_ind_B[] = {0, 0, 1}; float h_bsr_val_B[] = {0, 0, 0, 0, 0, 0, 7, 0, 8, 6, 0, 0}; // Allocate device memory for BSR matrices A and B rocsparse_int* d_bsr_row_ptr_A; rocsparse_int* d_bsr_col_ind_A; float* d_bsr_val_A; HIP_CHECK(hipMalloc((void**)&d_bsr_row_ptr_A, sizeof(rocsparse_int) * (mb + 1))); HIP_CHECK(hipMalloc((void**)&d_bsr_col_ind_A, sizeof(rocsparse_int) * nnzb_A)); HIP_CHECK(hipMalloc((void**)&d_bsr_val_A, sizeof(float) * nnzb_A * block_dim * block_dim)); HIP_CHECK(hipMemcpy( d_bsr_row_ptr_A, h_bsr_row_ptr_A, sizeof(rocsparse_int) * (mb + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( d_bsr_col_ind_A, h_bsr_col_ind_A, sizeof(rocsparse_int) * nnzb_A, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(d_bsr_val_A, h_bsr_val_A, sizeof(float) * nnzb_A * block_dim * block_dim, hipMemcpyHostToDevice)); rocsparse_int* d_bsr_row_ptr_B; rocsparse_int* d_bsr_col_ind_B; float* d_bsr_val_B; HIP_CHECK(hipMalloc((void**)&d_bsr_row_ptr_B, sizeof(rocsparse_int) * (mb + 1))); HIP_CHECK(hipMalloc((void**)&d_bsr_col_ind_B, sizeof(rocsparse_int) * nnzb_B)); HIP_CHECK(hipMalloc((void**)&d_bsr_val_B, sizeof(float) * nnzb_B * block_dim * block_dim)); HIP_CHECK(hipMemcpy( d_bsr_row_ptr_B, h_bsr_row_ptr_B, sizeof(rocsparse_int) * (mb + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( d_bsr_col_ind_B, h_bsr_col_ind_B, sizeof(rocsparse_int) * nnzb_B, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(d_bsr_val_B, h_bsr_val_B, sizeof(float) * nnzb_B * block_dim * block_dim, hipMemcpyHostToDevice)); // Allocate memory for the row pointer array of the compressed CSR matrix rocsparse_int* d_bsr_row_ptr_C; HIP_CHECK(hipMalloc((void**)&d_bsr_row_ptr_C, sizeof(rocsparse_int) * (mb + 1))); // Obtain number of total non-zero block entries in C and block row pointers of C rocsparse_int nnzb_C; ROCSPARSE_CHECK(rocsparse_bsrgeam_nnzb(handle, rocsparse_direction_column, mb, nb, block_dim, descr_A, nnzb_A, d_bsr_row_ptr_A, d_bsr_col_ind_A, descr_B, nnzb_B, d_bsr_row_ptr_B, d_bsr_col_ind_B, descr_C, d_bsr_row_ptr_C, &nnzb_C)); // Compute block column indices and block values of C rocsparse_int* d_bsr_col_ind_C; float* d_bsr_val_C; HIP_CHECK(hipMalloc((void**)&d_bsr_col_ind_C, sizeof(rocsparse_int) * nnzb_C)); HIP_CHECK(hipMalloc((void**)&d_bsr_val_C, sizeof(float) * nnzb_C * block_dim * block_dim)); ROCSPARSE_CHECK(rocsparse_sbsrgeam(handle, rocsparse_direction_column, mb, nb, block_dim, &alpha, descr_A, nnzb_A, d_bsr_val_A, d_bsr_row_ptr_A, d_bsr_col_ind_A, &beta, descr_B, nnzb_B, d_bsr_val_B, d_bsr_row_ptr_B, d_bsr_col_ind_B, descr_C, d_bsr_val_C, d_bsr_row_ptr_C, d_bsr_col_ind_C)); // Clean up HIP_CHECK(hipFree(d_bsr_row_ptr_A)); HIP_CHECK(hipFree(d_bsr_col_ind_A)); HIP_CHECK(hipFree(d_bsr_val_A)); HIP_CHECK(hipFree(d_bsr_row_ptr_B)); HIP_CHECK(hipFree(d_bsr_col_ind_B)); HIP_CHECK(hipFree(d_bsr_val_B)); return 0; }


Note

Both scalars \(\alpha\) and \(beta\) have to be valid.

Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dir**–**[in]**direction that specifies whether to count nonzero elements by[rocsparse_direction_row](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca40d95f05d0cd4ad3c89465959c58943e)or by[rocsparse_direction_column](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca23355bb7b606c550ba61c781bcecfc5b)in the BSR matrices \(A\), \(B\), and \(C\).**mb**–**[in]**number of rows of the sparse BSR matrix \(A\), \(B\) and \(C\).**nb**–**[in]**number of columns of the sparse BSR matrix \(A\), \(B\) and \(C\).**block_dim**–**[in]**the block dimension of the BSR matrix \(A\). Between 1 and m where`m=mb*block_dim`

.**alpha**–**[in]**scalar \(\alpha\).**descr_A**–**[in]**descriptor of the sparse CSR matrix \(A\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**nnzb_A**–**[in]**number of non-zero block entries of the sparse BSR matrix \(A\).**bsr_val_A**–**[in]**array of`nnzb_A`

block elements of the sparse BSR matrix \(A\).**bsr_row_ptr_A**–**[in]**array of`mb+1`

block elements that point to the start of every block row of the sparse BSR matrix \(A\).**bsr_col_ind_A**–**[in]**array of`nnzb_A`

block elements containing the block column indices of the sparse BSR matrix \(A\).**beta**–**[in]**scalar \(\beta\).**descr_B**–**[in]**descriptor of the sparse BSR matrix \(B\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**nnzb_B**–**[in]**number of non-zero block entries of the sparse BSR matrix \(B\).**bsr_val_B**–**[in]**array of`nnzb_B`

block elements of the sparse BSR matrix \(B\).**bsr_row_ptr_B**–**[in]**array of`mb+1`

block elements that point to the start of every block row of the sparse BSR matrix \(B\).**bsr_col_ind_B**–**[in]**array of`nnzb_B`

block elements containing the block column indices of the sparse BSR matrix \(B\).**descr_C**–**[in]**descriptor of the sparse BSR matrix \(C\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**bsr_val_C**–**[out]**array of block elements of the sparse BSR matrix \(C\).**bsr_row_ptr_C**–**[in]**array of`mb+1`

block elements that point to the start of every block row of the sparse BSR matrix \(C\).**bsr_col_ind_C**–**[out]**array of block elements containing the block column indices of the sparse BSR matrix \(C\).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`mb`

,`nb`

,`nnzb_A`

or`nnzb_B`

is invalid.**rocsparse_status_invalid_pointer**–`alpha`

,`descr_A`

,`bsr_val_A`

,`bsr_row_ptr_A`

,`bsr_col_ind_A`

,`beta`

,`descr_B`

,`bsr_val_B`

,`bsr_row_ptr_B`

,`bsr_col_ind_B`

,`descr_C`

,`csr_val_C`

,`bsr_row_ptr_C`

or`bsr_col_ind_C`

is invalid.**rocsparse_status_not_implemented**–`rocsparse_matrix_type`

!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_bsrgemm_buffer_size()[#](#rocsparse-bsrgemm-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sbsrgemm_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)kb,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim, const float *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_B, const float *beta, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_D,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_D,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info_C, size_t *buffer_size)[#](#_CPPv430rocsparse_sbsrgemm_buffer_size16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intPKfK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dbsrgemm_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)kb,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim, const double *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_B, const double *beta, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_D,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_D,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info_C, size_t *buffer_size)[#](#_CPPv430rocsparse_dbsrgemm_buffer_size16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPKdK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intPKdK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cbsrgemm_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)kb,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_B, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*beta, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_D,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_D,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info_C, size_t *buffer_size)[#](#_CPPv430rocsparse_cbsrgemm_buffer_size16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPK23rocsparse_float_complexK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intPK23rocsparse_float_complexK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zbsrgemm_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)kb,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_B, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*beta, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_D,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_D,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info_C, size_t *buffer_size)[#](#_CPPv430rocsparse_zbsrgemm_buffer_size16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPK24rocsparse_double_complexK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intPK24rocsparse_double_complexK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoP6size_t) `rocsparse_bsrgemm_buffer_size`

returns the size of the temporary storage buffer that is required by[rocsparse_bsrgemm_nnzb()](#rocsparse__bsrgemm_8h_1abf7a602f42c180ccd79e7fecea044cd4)and[rocsparse_Xbsrgemm()](#rocsparse__bsrgemm_8h_1af5df0b8b4ed7dd34fd0ae7d195fa0040). The temporary storage buffer must be allocated by the user.Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dir**–**[in]**direction that specifies whether to count nonzero elements by[rocsparse_direction_row](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca40d95f05d0cd4ad3c89465959c58943e)or by[rocsparse_direction_column](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca23355bb7b606c550ba61c781bcecfc5b)in the BSR matrices \(A\), \(B\), \(C\), and \(D\).**trans_A**–**[in]**matrix \(A\) operation type.**trans_B**–**[in]**matrix \(B\) operation type.**mb**–**[in]**number of block rows in the sparse BSR matrix \(op(A)\) and \(C\).**nb**–**[in]**number of block columns of the sparse BSR matrix \(op(B)\) and \(C\).**kb**–**[in]**number of block columns of the sparse BSR matrix \(op(A)\) and number of rows of the sparse BSR matrix \(op(B)\).**block_dim**–**[in]**the block dimension of the BSR matrix \(A\), \(B\), \(C\), and \(D\).**alpha**–**[in]**scalar \(\alpha\).**descr_A**–**[in]**descriptor of the sparse BSR matrix \(A\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**nnzb_A**–**[in]**number of non-zero block entries of the sparse BSR matrix \(A\).**bsr_row_ptr_A**–**[in]**array of`mb+1`

elements ( \(op(A) == A\),`kb+1`

otherwise) that point to the start of every block row of the sparse BSR matrix \(op(A)\).**bsr_col_ind_A**–**[in]**array of`nnzb_A`

elements containing the block column indices of the sparse BSR matrix \(A\).**descr_B**–**[in]**descriptor of the sparse BSR matrix \(B\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**nnzb_B**–**[in]**number of non-zero block entries of the sparse BSR matrix \(B\).**bsr_row_ptr_B**–**[in]**array of`kb+1`

elements ( \(op(B) == B\),`mb+1`

otherwise) that point to the start of every block row of the sparse BSR matrix \(op(B)\).**bsr_col_ind_B**–**[in]**array of`nnzb_B`

elements containing the block column indices of the sparse BSR matrix \(B\).**beta**–**[in]**scalar \(\beta\).**descr_D**–**[in]**descriptor of the sparse BSR matrix \(D\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**nnzb_D**–**[in]**number of non-zero block entries of the sparse BSR matrix \(D\).**bsr_row_ptr_D**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix \(D\).**bsr_col_ind_D**–**[in]**array of`nnzb_D`

elements containing the block column indices of the sparse BSR matrix \(D\).**info_C**–**[inout]**structure that holds meta data for the sparse BSR matrix \(C\).**buffer_size**–**[out]**number of bytes of the temporary storage buffer required by[rocsparse_bsrgemm_nnzb()](#rocsparse__bsrgemm_8h_1abf7a602f42c180ccd79e7fecea044cd4),[rocsparse_sbsrgemm()](#rocsparse__bsrgemm_8h_1af5df0b8b4ed7dd34fd0ae7d195fa0040),[rocsparse_dbsrgemm()](#rocsparse__bsrgemm_8h_1ad1daa2274f53f1c436678334ebf1acec),[rocsparse_cbsrgemm()](#rocsparse__bsrgemm_8h_1a6b3f2cef88dfe80a02c6ce88284a124e)and[rocsparse_zbsrgemm()](#rocsparse__bsrgemm_8h_1a8f6a615196e512065f3a4347dcffe0d0).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`mb`

,`nb`

,`kb`

,`block_dim`

,`nnzb_A`

,`nnzb_B`

or`nnzb_D`

is invalid.**rocsparse_status_invalid_pointer**–`alpha`

and`beta`

are invalid,`descr_A`

,`bsr_row_ptr_A`

,`bsr_col_ind_A`

,`descr_B`

,`bsr_row_ptr_B`

or`bsr_col_ind_B`

are invalid if`alpha`

is valid,`descr_D`

,`bsr_row_ptr_D`

or`bsr_col_ind_D`

is invalid if`beta`

is valid,`info_C`

or`buffer_size`

is invalid.**rocsparse_status_not_implemented**–`trans_A`

!=[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528),`trans_B`

!=[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528), or`rocsparse_matrix_type`

!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_bsrgemm_nnzb()[#](#rocsparse-bsrgemm-nnzb)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_bsrgemm_nnzb([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)kb,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_B, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_D,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_D, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnzb_C, const[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info_C, void *temp_buffer)[#](#_CPPv422rocsparse_bsrgemm_nnzb16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descrP13rocsparse_intP13rocsparse_intK18rocsparse_mat_infoPv) `rocsparse_bsrgemm_nnzb`

computes the total BSR non-zero block elements and the BSR block row offsets, that point to the start of every block row of the sparse BSR matrix, of the resulting multiplied matrix C. It is assumed that`bsr_row_ptr_C`

has been allocated with size`mb+1`

. The required buffer size can be obtained by[rocsparse_Xbsrgemm_buffer_size()](#rocsparse__bsrgemm_8h_1a7a1d7e873e161063fe0acdf2ac91fd81).Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dir**–**[in]**direction that specifies whether to count nonzero elements by[rocsparse_direction_row](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca40d95f05d0cd4ad3c89465959c58943e)or by[rocsparse_direction_column](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca23355bb7b606c550ba61c781bcecfc5b)in the BSR matrices \(A\), \(B\), \(C\), and \(D\).**trans_A**–**[in]**matrix \(A\) operation type.**trans_B**–**[in]**matrix \(B\) operation type.**mb**–**[in]**number of block rows in the sparse BSR matrix \(op(A)\) and \(C\).**nb**–**[in]**number of block columns of the sparse BSR matrix \(op(B)\) and \(C\).**kb**–**[in]**number of block columns of the sparse BSR matrix \(op(A)\) and number of rows of the sparse BSR matrix \(op(B)\).**block_dim**–**[in]**the block dimension of the BSR matrix \(A\), \(B\), \(C\), and \(D\).**descr_A**–**[in]**descriptor of the sparse BSR matrix \(A\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**nnzb_A**–**[in]**number of non-zero block entries of the sparse BSR matrix \(A\).**bsr_row_ptr_A**–**[in]**array of`mb+1`

block elements ( \(op(A) == A\),`kb+1`

otherwise) that point to the start of every row of the sparse BSR matrix \(op(A)\).**bsr_col_ind_A**–**[in]**array of`nnzb_A`

block elements containing the block column indices of the sparse BSR matrix \(A\).**descr_B**–**[in]**descriptor of the sparse BSR matrix \(B\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**nnzb_B**–**[in]**number of non-zero block entries of the sparse BSR matrix \(B\).**bsr_row_ptr_B**–**[in]**array of`kb+1`

block elements ( \(op(B) == B\),`mb+1`

otherwise) that point to the start of every block row of the sparse BSR matrix \(op(B)\).**bsr_col_ind_B**–**[in]**array of`nnzb_B`

block elements containing the block column indices of the sparse BSR matrix \(B\).**descr_D**–**[in]**descriptor of the sparse BSR matrix \(D\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**nnzb_D**–**[in]**number of non-zero block entries of the sparse BSR matrix \(D\).**bsr_row_ptr_D**–**[in]**array of`mb+1`

block elements that point to the start of every block row of the sparse BSR matrix \(D\).**bsr_col_ind_D**–**[in]**array of`nnzb_D`

block elements containing the block column indices of the sparse BSR matrix \(D\).**descr_C**–**[in]**descriptor of the sparse BSR matrix \(C\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**bsr_row_ptr_C**–**[out]**array of`mb+1`

block elements that point to the start of every block row of the sparse BSR matrix \(C\).**nnzb_C**–**[out]**pointer to the number of non-zero block entries of the sparse BSR matrix \(C\).**info_C**–**[in]**structure that holds meta data for the sparse BSR matrix \(C\).**temp_buffer**–**[in]**temporary storage buffer allocated by the user, size is returned by[rocsparse_sbsrgemm_buffer_size()](#rocsparse__bsrgemm_8h_1a7a1d7e873e161063fe0acdf2ac91fd81),[rocsparse_dbsrgemm_buffer_size()](#rocsparse__bsrgemm_8h_1a2170fa3df577477e802d87bba6669411),[rocsparse_cbsrgemm_buffer_size()](#rocsparse__bsrgemm_8h_1acafc2461dfce36e271f8198a95f682a9)or[rocsparse_zbsrgemm_buffer_size()](#rocsparse__bsrgemm_8h_1abfdb2160b49a335b08aac61752feb18c).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`mb`

,`nb`

,`kb`

,`block_dim`

,`nnzb_A`

,`nnzb_B`

or`nnzb_D`

is invalid.**rocsparse_status_invalid_pointer**–`descr_A`

,`bsr_row_ptr_A`

,`bsr_col_ind_A`

,`descr_B`

,`bsr_row_ptr_B`

,`bsr_col_ind_B`

,`descr_D`

,`bsr_row_ptr_D`

,`bsr_col_ind_D`

,`descr_C`

,`bsr_row_ptr_C`

,`nnzb_C`

,`info_C`

or`temp_buffer`

is invalid.**rocsparse_status_memory_error**– additional buffer for long rows could not be allocated.**rocsparse_status_not_implemented**–`trans_A`

!=[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528),`trans_B`

!=[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528), or`rocsparse_matrix_type`

!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_bsrgemm()[#](#rocsparse-bsrgemm)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sbsrgemm([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)kb,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim, const float *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb_A, const float *bsr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb_B, const float *bsr_val_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_B, const float *beta, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_D,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb_D, const float *bsr_val_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_D, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_C, float *bsr_val_C, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_C, const[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info_C, void *temp_buffer)[#](#_CPPv418rocsparse_sbsrgemm16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descr13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_intPKfK19rocsparse_mat_descr13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descrPfPK13rocsparse_intP13rocsparse_intK18rocsparse_mat_infoPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dbsrgemm([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)kb,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim, const double *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb_A, const double *bsr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb_B, const double *bsr_val_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_B, const double *beta, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_D,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb_D, const double *bsr_val_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_D, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_C, double *bsr_val_C, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_C, const[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info_C, void *temp_buffer)[#](#_CPPv418rocsparse_dbsrgemm16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPKdK19rocsparse_mat_descr13rocsparse_intPKdPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPKdPK13rocsparse_intPK13rocsparse_intPKdK19rocsparse_mat_descr13rocsparse_intPKdPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descrPdPK13rocsparse_intP13rocsparse_intK18rocsparse_mat_infoPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cbsrgemm([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)kb,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb_A, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb_B, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsr_val_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_B, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*beta, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_D,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb_D, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsr_val_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_D, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_C,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsr_val_C, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_C, const[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info_C, void *temp_buffer)[#](#_CPPv418rocsparse_cbsrgemm16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPK23rocsparse_float_complexK19rocsparse_mat_descr13rocsparse_intPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_intPK23rocsparse_float_complexK19rocsparse_mat_descr13rocsparse_intPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descrP23rocsparse_float_complexPK13rocsparse_intP13rocsparse_intK18rocsparse_mat_infoPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zbsrgemm([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)kb,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb_A, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb_B, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsr_val_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_B, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*beta, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_D,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb_D, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsr_val_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_D, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_C,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsr_val_C, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind_C, const[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info_C, void *temp_buffer)[#](#_CPPv418rocsparse_zbsrgemm16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPK24rocsparse_double_complexK19rocsparse_mat_descr13rocsparse_intPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_intPK24rocsparse_double_complexK19rocsparse_mat_descr13rocsparse_intPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descrP24rocsparse_double_complexPK13rocsparse_intP13rocsparse_intK18rocsparse_mat_infoPv) Sparse matrix sparse matrix multiplication using BSR storage format.

`rocsparse_bsrgemm`

multiplies the scalar \(\alpha\) with the sparse \(mb \times kb\) matrix \(A\), defined in BSR storage format, and the sparse \(kb \times nb\) matrix \(B\), defined in BSR storage format, and adds the result to the sparse \(mb \times nb\) matrix \(D\) that is multiplied by \(\beta\). The final result is stored in the sparse \(mb \times nb\) matrix \(C\), defined in BSR storage format, such that\[ C := \alpha \cdot op(A) \cdot op(B) + \beta \cdot D, \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if trans_A == rocsparse_operation_none} \\ A^T, & \text{if trans_A == rocsparse_operation_transpose} \\ A^H, & \text{if trans_A == rocsparse_operation_conjugate_transpose} \end{array} \right. \end{split}\]and\[\begin{split} op(B) = \left\{ \begin{array}{ll} B, & \text{if trans_B == rocsparse_operation_none} \\ B^T, & \text{if trans_B == rocsparse_operation_transpose} \\ B^H, & \text{if trans_B == rocsparse_operation_conjugate_transpose} \end{array} \right. \end{split}\]It is assumed that

`bsr_row_ptr_C`

has already been filled and that`bsr_val_C`

and`bsr_col_ind_C`

are allocated by the user.`bsr_row_ptr_C`

and allocation size of`bsr_col_ind_C`

and`bsr_val_C`

is defined by the number of non-zero elements of the sparse BSR matrix C. Both can be obtained by[rocsparse_bsrgemm_nnzb()](#rocsparse__bsrgemm_8h_1abf7a602f42c180ccd79e7fecea044cd4). The required buffer size for the computation can be obtained by[rocsparse_Xbsrgemm_buffer_size()](#rocsparse__bsrgemm_8h_1a7a1d7e873e161063fe0acdf2ac91fd81).**Example**This example multiplies two BSR matrices with a scalar alpha and adds the result to another BSR matrix.

int main() { // Initialize scalar multipliers float alpha = 2.0f; float beta = 1.0f; // Define matrix dimensions and block size rocsparse_int mb = 2; // Number of block rows rocsparse_int nb = 2; // Number of block columns rocsparse_int kb = 2; // Number of block columns in B rocsparse_int block_dim = 2; // Block dimension // Create rocsparse handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Create matrix descriptors rocsparse_mat_descr descr_A; rocsparse_mat_descr descr_B; rocsparse_mat_descr descr_C; rocsparse_mat_descr descr_D; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr_A)); ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr_B)); ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr_C)); ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr_D)); // Create matrix info structure rocsparse_mat_info info_C; ROCSPARSE_CHECK(rocsparse_create_mat_info(&info_C)); // Set pointer mode ROCSPARSE_CHECK(rocsparse_set_pointer_mode(handle, rocsparse_pointer_mode_host)); // Define host arrays for BSR matrices A, B, and D rocsparse_int nnzb_A = 3; // Number of non-zero blocks in A rocsparse_int nnzb_B = 3; // Number of non-zero blocks in B rocsparse_int nnzb_D = 3; // Number of non-zero blocks in D rocsparse_int h_bsr_row_ptr_A[] = {0, 1, 3}; rocsparse_int h_bsr_col_ind_A[] = {0, 0, 1}; float h_bsr_val_A[] = {1, 0, 4, 2, 0, 3, 5, 0, 0, 0, 0, 9}; rocsparse_int h_bsr_row_ptr_B[] = {0, 1, 3}; rocsparse_int h_bsr_col_ind_B[] = {0, 0, 1}; float h_bsr_val_B[] = {0, 0, 0, 0, 0, 0, 7, 0, 8, 6, 0, 0}; rocsparse_int h_bsr_row_ptr_D[] = {0, 1, 3}; rocsparse_int h_bsr_col_ind_D[] = {0, 0, 1}; float h_bsr_val_D[] = {0, 0, 0, 0, 0, 0, 7, 0, 8, 6, 0, 0}; // Allocate device memory for BSR matrices A, B, and D rocsparse_int* d_bsr_row_ptr_A; rocsparse_int* d_bsr_col_ind_A; float* d_bsr_val_A; HIP_CHECK(hipMalloc((void**)&d_bsr_row_ptr_A, sizeof(rocsparse_int) * (mb + 1))); HIP_CHECK(hipMalloc((void**)&d_bsr_col_ind_A, sizeof(rocsparse_int) * nnzb_A)); HIP_CHECK(hipMalloc((void**)&d_bsr_val_A, sizeof(float) * nnzb_A * block_dim * block_dim)); HIP_CHECK(hipMemcpy( d_bsr_row_ptr_A, h_bsr_row_ptr_A, sizeof(rocsparse_int) * (mb + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( d_bsr_col_ind_A, h_bsr_col_ind_A, sizeof(rocsparse_int) * nnzb_A, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(d_bsr_val_A, h_bsr_val_A, sizeof(float) * nnzb_A * block_dim * block_dim, hipMemcpyHostToDevice)); rocsparse_int* d_bsr_row_ptr_B; rocsparse_int* d_bsr_col_ind_B; float* d_bsr_val_B; HIP_CHECK(hipMalloc((void**)&d_bsr_row_ptr_B, sizeof(rocsparse_int) * (mb + 1))); HIP_CHECK(hipMalloc((void**)&d_bsr_col_ind_B, sizeof(rocsparse_int) * nnzb_B)); HIP_CHECK(hipMalloc((void**)&d_bsr_val_B, sizeof(float) * nnzb_B * block_dim * block_dim)); HIP_CHECK(hipMemcpy( d_bsr_row_ptr_B, h_bsr_row_ptr_B, sizeof(rocsparse_int) * (mb + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( d_bsr_col_ind_B, h_bsr_col_ind_B, sizeof(rocsparse_int) * nnzb_B, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(d_bsr_val_B, h_bsr_val_B, sizeof(float) * nnzb_B * block_dim * block_dim, hipMemcpyHostToDevice)); rocsparse_int* d_bsr_row_ptr_D; rocsparse_int* d_bsr_col_ind_D; float* d_bsr_val_D; HIP_CHECK(hipMalloc((void**)&d_bsr_row_ptr_D, sizeof(rocsparse_int) * (mb + 1))); HIP_CHECK(hipMalloc((void**)&d_bsr_col_ind_D, sizeof(rocsparse_int) * nnzb_D)); HIP_CHECK(hipMalloc((void**)&d_bsr_val_D, sizeof(float) * nnzb_D * block_dim * block_dim)); HIP_CHECK(hipMemcpy( d_bsr_row_ptr_D, h_bsr_row_ptr_D, sizeof(rocsparse_int) * (mb + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( d_bsr_col_ind_D, h_bsr_col_ind_D, sizeof(rocsparse_int) * nnzb_D, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(d_bsr_val_D, h_bsr_val_D, sizeof(float) * nnzb_D * block_dim * block_dim, hipMemcpyHostToDevice)); // Query rocsparse for the required buffer size size_t buffer_size; ROCSPARSE_CHECK(rocsparse_sbsrgemm_buffer_size(handle, rocsparse_direction_row, rocsparse_operation_none, rocsparse_operation_none, mb, nb, kb, block_dim, &alpha, descr_A, nnzb_A, d_bsr_row_ptr_A, d_bsr_col_ind_A, descr_B, nnzb_B, d_bsr_row_ptr_B, d_bsr_col_ind_B, &beta, descr_D, nnzb_D, d_bsr_row_ptr_D, d_bsr_col_ind_D, info_C, &buffer_size)); // Allocate buffer void* buffer; HIP_CHECK(hipMalloc(&buffer, buffer_size)); // Obtain number of total non-zero block entries in C and block row pointers of C rocsparse_int nnzb_C; rocsparse_int* d_bsr_row_ptr_C; HIP_CHECK(hipMalloc((void**)&d_bsr_row_ptr_C, sizeof(rocsparse_int) * (mb + 1))); ROCSPARSE_CHECK(rocsparse_bsrgemm_nnzb(handle, rocsparse_direction_row, rocsparse_operation_none, rocsparse_operation_none, mb, nb, kb, block_dim, descr_A, nnzb_A, d_bsr_row_ptr_A, d_bsr_col_ind_A, descr_B, nnzb_B, d_bsr_row_ptr_B, d_bsr_col_ind_B, descr_D, nnzb_D, d_bsr_row_ptr_D, d_bsr_col_ind_D, descr_C, d_bsr_row_ptr_C, &nnzb_C, info_C, buffer)); // Compute block column indices and values of C rocsparse_int* d_bsr_col_ind_C; float* d_bsr_val_C; HIP_CHECK(hipMalloc((void**)&d_bsr_col_ind_C, sizeof(rocsparse_int) * nnzb_C)); HIP_CHECK(hipMalloc((void**)&d_bsr_val_C, sizeof(float) * block_dim * block_dim * nnzb_C)); ROCSPARSE_CHECK(rocsparse_sbsrgemm(handle, rocsparse_direction_row, rocsparse_operation_none, rocsparse_operation_none, mb, nb, kb, block_dim, &alpha, descr_A, nnzb_A, d_bsr_val_A, d_bsr_row_ptr_A, d_bsr_col_ind_A, descr_B, nnzb_B, d_bsr_val_B, d_bsr_row_ptr_B, d_bsr_col_ind_B, &beta, descr_D, nnzb_D, d_bsr_val_D, d_bsr_row_ptr_D, d_bsr_col_ind_D, descr_C, d_bsr_val_C, d_bsr_row_ptr_C, d_bsr_col_ind_C, info_C, buffer)); HIP_CHECK(hipFree(d_bsr_row_ptr_A)); HIP_CHECK(hipFree(d_bsr_col_ind_A)); HIP_CHECK(hipFree(d_bsr_val_A)); HIP_CHECK(hipFree(d_bsr_row_ptr_B)); HIP_CHECK(hipFree(d_bsr_col_ind_B)); HIP_CHECK(hipFree(d_bsr_val_B)); HIP_CHECK(hipFree(d_bsr_row_ptr_C)); HIP_CHECK(hipFree(d_bsr_col_ind_C)); HIP_CHECK(hipFree(d_bsr_val_C)); HIP_CHECK(hipFree(d_bsr_row_ptr_D)); HIP_CHECK(hipFree(d_bsr_col_ind_D)); HIP_CHECK(hipFree(d_bsr_val_D)); HIP_CHECK(hipFree(buffer)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr_A)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr_B)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr_C)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr_D)); ROCSPARSE_CHECK(rocsparse_destroy_mat_info(info_C)); // Destroy rocSPARSE handle ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); return 0; }


Note

This function does not produce deterministic results.

Note

If \(\alpha == 0\), then \(C = \beta \cdot D\) will be computed.

Note

If \(\beta == 0\), then \(C = \alpha \cdot op(A) \cdot op(B)\) will be computed.

Note

\(\alpha == beta == 0\) is invalid.

Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dir**–**[in]**direction that specifies whether to count nonzero elements by[rocsparse_direction_row](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca40d95f05d0cd4ad3c89465959c58943e)or by[rocsparse_direction_column](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca23355bb7b606c550ba61c781bcecfc5b)in the BSR matrices \(A\), \(B\), \(C\), and \(D\).**trans_A**–**[in]**matrix \(A\) operation type.**trans_B**–**[in]**matrix \(B\) operation type.**mb**–**[in]**number of block rows of the sparse BSR matrix \(op(A)\) and \(C\).**nb**–**[in]**number of block columns of the sparse BSR matrix \(op(B)\) and \(C\).**kb**–**[in]**number of block columns of the sparse BSR matrix \(op(A)\) and number of block rows of the sparse BSR matrix \(op(B)\).**block_dim**–**[in]**the block dimension of the BSR matrix \(A\), \(B\), \(C\), and \(D\).**alpha**–**[in]**scalar \(\alpha\).**descr_A**–**[in]**descriptor of the sparse BSR matrix \(A\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**nnzb_A**–**[in]**number of non-zero block entries of the sparse BSR matrix \(A\).**bsr_val_A**–**[in]**array of`nnzb_A`

block elements of the sparse BSR matrix \(A\).**bsr_row_ptr_A**–**[in]**array of`mb+1`

block elements ( \(op(A) == A\),`kb+1`

otherwise) that point to the start of every block row of the sparse BSR matrix \(op(A)\).**bsr_col_ind_A**–**[in]**array of`nnzb_A`

block elements containing the block column indices of the sparse BSR matrix \(A\).**descr_B**–**[in]**descriptor of the sparse BSR matrix \(B\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**nnzb_B**–**[in]**number of non-zero block entries of the sparse BSR matrix \(B\).**bsr_val_B**–**[in]**array of`nnzb_B`

block elements of the sparse BSR matrix \(B\).**bsr_row_ptr_B**–**[in]**array of`kb+1`

block elements ( \(op(B) == B\),`mb+1`

otherwise) that point to the start of every block row of the sparse BSR matrix \(op(B)\).**bsr_col_ind_B**–**[in]**array of`nnzb_B`

block elements containing the block column indices of the sparse BSR matrix \(B\).**beta**–**[in]**scalar \(\beta\).**descr_D**–**[in]**descriptor of the sparse BSR matrix \(D\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**nnzb_D**–**[in]**number of non-zero block entries of the sparse BSR matrix \(D\).**bsr_val_D**–**[in]**array of`nnzb_D`

block elements of the sparse BSR matrix \(D\).**bsr_row_ptr_D**–**[in]**array of`mb+1`

block elements that point to the start of every block row of the sparse BSR matrix \(D\).**bsr_col_ind_D**–**[in]**array of`nnzb_D`

block elements containing the block column indices of the sparse BSR matrix \(D\).**descr_C**–**[in]**descriptor of the sparse BSR matrix \(C\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**bsr_val_C**–**[out]**array of`nnzb_C`

elements of the sparse BSR matrix \(C\).**bsr_row_ptr_C**–**[in]**array of`mb+1`

block elements that point to the start of every block row of the sparse BSR matrix \(C\).**bsr_col_ind_C**–**[out]**array of`nnzb_C`

block elements containing the block column indices of the sparse BSR matrix \(C\).**info_C**–**[in]**structure that holds meta data for the sparse BSR matrix \(C\).**temp_buffer**–**[in]**temporary storage buffer allocated by the user, size is returned by[rocsparse_sbsrgemm_buffer_size()](#rocsparse__bsrgemm_8h_1a7a1d7e873e161063fe0acdf2ac91fd81),[rocsparse_dbsrgemm_buffer_size()](#rocsparse__bsrgemm_8h_1a2170fa3df577477e802d87bba6669411),[rocsparse_cbsrgemm_buffer_size()](#rocsparse__bsrgemm_8h_1acafc2461dfce36e271f8198a95f682a9)or[rocsparse_zbsrgemm_buffer_size()](#rocsparse__bsrgemm_8h_1abfdb2160b49a335b08aac61752feb18c).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`mb`

,`nb`

,`kb`

,`block_dim`

,`nnzb_A`

,`nnzb_B`

or`nnzb_D`

is invalid.**rocsparse_status_invalid_pointer**–`alpha`

and`beta`

are invalid,`descr_A`

,`bsr_val_A`

,`bsr_row_ptr_A`

,`bsr_col_ind_A`

,`descr_B`

,`bsr_val_B`

,`bsr_row_ptr_B`

or`bsr_col_ind_B`

are invalid if`alpha`

is valid,`descr_D`

,`bsr_val_D`

,`bsr_row_ptr_D`

or`bsr_col_ind_D`

is invalid if`beta`

is valid,`bsr_val_C`

,`bsr_row_ptr_C`

,`bsr_col_ind_C`

,`info_C`

or`temp_buffer`

is invalid.**rocsparse_status_memory_error**– additional buffer for long rows could not be allocated.**rocsparse_status_not_implemented**–`trans_A`

!=[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528),`trans_B`

!=[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528), or`rocsparse_matrix_type`

!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_csrgeam_nnz()[#](#rocsparse-csrgeam-nnz)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_csrgeam_nnz([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_B, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_C)[#](#_CPPv421rocsparse_csrgeam_nnz16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descrP13rocsparse_intP13rocsparse_int) `rocsparse_csrgeam_nnz`

computes the total CSR non-zero elements and the CSR row offsets, that point to the start of every row of the sparse CSR matrix, of the resulting matrix C. It is assumed that`csr_row_ptr_C`

has been allocated with size`m+1`

.Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix \(A\), \(B\) and \(C\).**n**–**[in]**number of columns of the sparse CSR matrix \(A\), \(B\) and \(C\).**descr_A**–**[in]**descriptor of the sparse CSR matrix \(A\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**nnz_A**–**[in]**number of non-zero entries of the sparse CSR matrix \(A\).**csr_row_ptr_A**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(A\).**csr_col_ind_A**–**[in]**array of`nnz_A`

elements containing the column indices of the sparse CSR matrix \(A\).**descr_B**–**[in]**descriptor of the sparse CSR matrix \(B\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**nnz_B**–**[in]**number of non-zero entries of the sparse CSR matrix \(B\).**csr_row_ptr_B**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(B\).**csr_col_ind_B**–**[in]**array of`nnz_B`

elements containing the column indices of the sparse CSR matrix \(B\).**descr_C**–**[in]**descriptor of the sparse CSR matrix \(C\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**csr_row_ptr_C**–**[out]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(C\).**nnz_C**–**[out]**pointer to the number of non-zero entries of the sparse CSR matrix \(C\).`nnz_C`

can be a host or device pointer.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`n`

,`nnz_A`

or`nnz_B`

is invalid.**rocsparse_status_invalid_pointer**–`descr_A`

,`csr_row_ptr_A`

,`csr_col_ind_A`

,`descr_B`

,`csr_row_ptr_B`

,`csr_col_ind_B`

,`descr_C`

,`csr_row_ptr_C`

or`nnz_C`

is invalid.**rocsparse_status_not_implemented**–`rocsparse_matrix_type`

!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_csrgeam()[#](#rocsparse-csrgeam)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scsrgeam([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const float *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_A, const float *csr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_A, const float *beta, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_B, const float *csr_val_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_B, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_C, float *csr_val_C, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_C)[#](#_CPPv418rocsparse_scsrgeam16rocsparse_handle13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descr13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_intPKfK19rocsparse_mat_descr13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descrPfPK13rocsparse_intP13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcsrgeam([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const double *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_A, const double *csr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_A, const double *beta, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_B, const double *csr_val_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_B, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_C, double *csr_val_C, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_C)[#](#_CPPv418rocsparse_dcsrgeam16rocsparse_handle13rocsparse_int13rocsparse_intPKdK19rocsparse_mat_descr13rocsparse_intPKdPK13rocsparse_intPK13rocsparse_intPKdK19rocsparse_mat_descr13rocsparse_intPKdPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descrPdPK13rocsparse_intP13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccsrgeam([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_A, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_A, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*beta, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_B, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_B, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_C,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val_C, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_C)[#](#_CPPv418rocsparse_ccsrgeam16rocsparse_handle13rocsparse_int13rocsparse_intPK23rocsparse_float_complexK19rocsparse_mat_descr13rocsparse_intPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_intPK23rocsparse_float_complexK19rocsparse_mat_descr13rocsparse_intPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descrP23rocsparse_float_complexPK13rocsparse_intP13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcsrgeam([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_A, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_A, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*beta, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_B, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_B, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_C,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val_C, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_C)[#](#_CPPv418rocsparse_zcsrgeam16rocsparse_handle13rocsparse_int13rocsparse_intPK24rocsparse_double_complexK19rocsparse_mat_descr13rocsparse_intPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_intPK24rocsparse_double_complexK19rocsparse_mat_descr13rocsparse_intPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descrP24rocsparse_double_complexPK13rocsparse_intP13rocsparse_int) Sparse matrix sparse matrix addition using CSR storage format.

`rocsparse_csrgeam`

multiplies the scalar \(\alpha\) with the sparse \(m \times n\) matrix \(A\), defined in CSR storage format, multiplies the scalar \(\beta\) with the sparse \(m \times n\) matrix \(B\), defined in CSR storage format, and adds both resulting matrices to obtain the sparse \(m \times n\) matrix \(C\), defined in CSR storage format, such that\[ C := \alpha \cdot A + \beta \cdot B. \]It is assumed that

`csr_row_ptr_C`

has already been filled and that`csr_val_C`

and`csr_col_ind_C`

are allocated by the user.`csr_row_ptr_C`

and allocation size of`csr_col_ind_C`

and`csr_val_C`

is defined by the number of non-zero elements of the sparse CSR matrix C. Both can be obtained by[rocsparse_csrgeam_nnz()](#rocsparse__csrgeam_8h_1a0f5dbcd04ed0682406a5ce4a5acbf376).**Example**This example adds two CSR matrices.

int main() { // Initialize scalar multipliers float alpha = 1.0f; float beta = 1.0f; // Define matrix dimensions rocsparse_int m = 3; // Number of rows rocsparse_int n = 3; // Number of columns // Create rocsparse handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Create matrix descriptors rocsparse_mat_descr descr_A; rocsparse_mat_descr descr_B; rocsparse_mat_descr descr_C; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr_A)); ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr_B)); ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr_C)); // Set pointer mode ROCSPARSE_CHECK(rocsparse_set_pointer_mode(handle, rocsparse_pointer_mode_host)); // Define host arrays for CSR matrices A and B rocsparse_int nnz_A = 4; // Number of non-zero entries in A rocsparse_int nnz_B = 4; // Number of non-zero entries in B rocsparse_int h_csr_row_ptr_A[] = {0, 2, 3, 4}; rocsparse_int h_csr_col_ind_A[] = {0, 1, 2, 2}; float h_csr_val_A[] = {1.0f, 2.0f, 3.0f, 4.0f}; rocsparse_int h_csr_row_ptr_B[] = {0, 1, 3, 4}; rocsparse_int h_csr_col_ind_B[] = {0, 1, 2, 2}; float h_csr_val_B[] = {5.0f, 6.0f, 7.0f, 8.0f}; // Allocate device memory for CSR matrices A and B rocsparse_int* d_csr_row_ptr_A; rocsparse_int* d_csr_col_ind_A; float* d_csr_val_A; HIP_CHECK(hipMalloc((void**)&d_csr_row_ptr_A, sizeof(rocsparse_int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&d_csr_col_ind_A, sizeof(rocsparse_int) * nnz_A)); HIP_CHECK(hipMalloc((void**)&d_csr_val_A, sizeof(float) * nnz_A)); HIP_CHECK(hipMemcpy( d_csr_row_ptr_A, h_csr_row_ptr_A, sizeof(rocsparse_int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( d_csr_col_ind_A, h_csr_col_ind_A, sizeof(rocsparse_int) * nnz_A, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(d_csr_val_A, h_csr_val_A, sizeof(float) * nnz_A, hipMemcpyHostToDevice)); rocsparse_int* d_csr_row_ptr_B; rocsparse_int* d_csr_col_ind_B; float* d_csr_val_B; HIP_CHECK(hipMalloc((void**)&d_csr_row_ptr_B, sizeof(rocsparse_int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&d_csr_col_ind_B, sizeof(rocsparse_int) * nnz_B)); HIP_CHECK(hipMalloc((void**)&d_csr_val_B, sizeof(float) * nnz_B)); HIP_CHECK(hipMemcpy( d_csr_row_ptr_B, h_csr_row_ptr_B, sizeof(rocsparse_int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( d_csr_col_ind_B, h_csr_col_ind_B, sizeof(rocsparse_int) * nnz_B, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(d_csr_val_B, h_csr_val_B, sizeof(float) * nnz_B, hipMemcpyHostToDevice)); // Obtain number of total non-zero entries in C and row pointers of C rocsparse_int nnz_C; rocsparse_int* d_csr_row_ptr_C; HIP_CHECK(hipMalloc((void**)&d_csr_row_ptr_C, sizeof(rocsparse_int) * (m + 1))); ROCSPARSE_CHECK(rocsparse_csrgeam_nnz(handle, m, n, descr_A, nnz_A, d_csr_row_ptr_A, d_csr_col_ind_A, descr_B, nnz_B, d_csr_row_ptr_B, d_csr_col_ind_B, descr_C, d_csr_row_ptr_C, &nnz_C)); // Compute column indices and values of C rocsparse_int* d_csr_col_ind_C; float* d_csr_val_C; HIP_CHECK(hipMalloc((void**)&d_csr_col_ind_C, sizeof(rocsparse_int) * nnz_C)); HIP_CHECK(hipMalloc((void**)&d_csr_val_C, sizeof(float) * nnz_C)); ROCSPARSE_CHECK(rocsparse_scsrgeam(handle, m, n, &alpha, descr_A, nnz_A, d_csr_val_A, d_csr_row_ptr_A, d_csr_col_ind_A, &beta, descr_B, nnz_B, d_csr_val_B, d_csr_row_ptr_B, d_csr_col_ind_B, descr_C, d_csr_val_C, d_csr_row_ptr_C, d_csr_col_ind_C)); // Clean up HIP_CHECK(hipFree(d_csr_row_ptr_A)); HIP_CHECK(hipFree(d_csr_col_ind_A)); HIP_CHECK(hipFree(d_csr_val_A)); HIP_CHECK(hipFree(d_csr_row_ptr_B)); HIP_CHECK(hipFree(d_csr_col_ind_B)); HIP_CHECK(hipFree(d_csr_val_B)); HIP_CHECK(hipFree(d_csr_row_ptr_C)); HIP_CHECK(hipFree(d_csr_col_ind_C)); HIP_CHECK(hipFree(d_csr_val_C)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr_A)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr_B)); return 0; }


Note

Both scalars \(\alpha\) and \(beta\) have to be valid.

Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix \(A\), \(B\) and \(C\).**n**–**[in]**number of columns of the sparse CSR matrix \(A\), \(B\) and \(C\).**alpha**–**[in]**scalar \(\alpha\).**descr_A**–**[in]**descriptor of the sparse CSR matrix \(A\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**nnz_A**–**[in]**number of non-zero entries of the sparse CSR matrix \(A\).**csr_val_A**–**[in]**array of`nnz_A`

elements of the sparse CSR matrix \(A\).**csr_row_ptr_A**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(A\).**csr_col_ind_A**–**[in]**array of`nnz_A`

elements containing the column indices of the sparse CSR matrix \(A\).**beta**–**[in]**scalar \(\beta\).**descr_B**–**[in]**descriptor of the sparse CSR matrix \(B\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**nnz_B**–**[in]**number of non-zero entries of the sparse CSR matrix \(B\).**csr_val_B**–**[in]**array of`nnz_B`

elements of the sparse CSR matrix \(B\).**csr_row_ptr_B**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(B\).**csr_col_ind_B**–**[in]**array of`nnz_B`

elements containing the column indices of the sparse CSR matrix \(B\).**descr_C**–**[in]**descriptor of the sparse CSR matrix \(C\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**csr_val_C**–**[out]**array of elements of the sparse CSR matrix \(C\).**csr_row_ptr_C**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(C\).**csr_col_ind_C**–**[out]**array of elements containing the column indices of the sparse CSR matrix \(C\).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`n`

,`nnz_A`

or`nnz_B`

is invalid.**rocsparse_status_invalid_pointer**–`alpha`

,`descr_A`

,`csr_val_A`

,`csr_row_ptr_A`

,`csr_col_ind_A`

,`beta`

,`descr_B`

,`csr_val_B`

,`csr_row_ptr_B`

,`csr_col_ind_B`

,`descr_C`

,`csr_val_C`

,`csr_row_ptr_C`

or`csr_col_ind_C`

is invalid.**rocsparse_status_not_implemented**–`rocsparse_matrix_type`

!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_csrgemm_buffer_size()[#](#rocsparse-csrgemm-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scsrgemm_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)k, const float *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_B, const float *beta, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_D,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_D,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info_C, size_t *buffer_size)[#](#_CPPv430rocsparse_scsrgemm_buffer_size16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intPKfK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcsrgemm_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)k, const double *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_B, const double *beta, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_D,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_D,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info_C, size_t *buffer_size)[#](#_CPPv430rocsparse_dcsrgemm_buffer_size16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKdK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intPKdK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccsrgemm_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)k, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_B, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*beta, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_D,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_D,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info_C, size_t *buffer_size)[#](#_CPPv430rocsparse_ccsrgemm_buffer_size16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPK23rocsparse_float_complexK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intPK23rocsparse_float_complexK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcsrgemm_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)k, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_B, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*beta, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_D,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_D,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info_C, size_t *buffer_size)[#](#_CPPv430rocsparse_zcsrgemm_buffer_size16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPK24rocsparse_double_complexK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intPK24rocsparse_double_complexK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoP6size_t) `rocsparse_csrgemm_buffer_size`

returns the size of the temporary storage buffer that is required by[rocsparse_csrgemm_nnz()](#rocsparse__csrgemm_8h_1a09cb61e11e4808b1b01d96fa311fb021)and[rocsparse_Xcsrgemm()](#rocsparse__csrgemm_8h_1a58f234545a387b56f9c9a58f68d15561). The temporary storage buffer must be allocated by the user.Note

Please note, that for matrix products with more than 4096 non-zero entries per row, additional temporary storage buffer is allocated by the algorithm.

Note

Please note, that for matrix products with more than 8192 intermediate products per row, additional temporary storage buffer is allocated by the algorithm.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**trans_A**–**[in]**matrix \(A\) operation type.**trans_B**–**[in]**matrix \(B\) operation type.**m**–**[in]**number of rows of the sparse CSR matrix \(op(A)\) and \(C\).**n**–**[in]**number of columns of the sparse CSR matrix \(op(B)\) and \(C\).**k**–**[in]**number of columns of the sparse CSR matrix \(op(A)\) and number of rows of the sparse CSR matrix \(op(B)\).**alpha**–**[in]**scalar \(\alpha\).**descr_A**–**[in]**descriptor of the sparse CSR matrix \(A\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**nnz_A**–**[in]**number of non-zero entries of the sparse CSR matrix \(A\).**csr_row_ptr_A**–**[in]**array of`m+1`

elements ( \(op(A) == A\),`k+1`

otherwise) that point to the start of every row of the sparse CSR matrix \(op(A)\).**csr_col_ind_A**–**[in]**array of`nnz_A`

elements containing the column indices of the sparse CSR matrix \(A\).**descr_B**–**[in]**descriptor of the sparse CSR matrix \(B\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**nnz_B**–**[in]**number of non-zero entries of the sparse CSR matrix \(B\).**csr_row_ptr_B**–**[in]**array of`k+1`

elements ( \(op(B) == B\),`m+1`

otherwise) that point to the start of every row of the sparse CSR matrix \(op(B)\).**csr_col_ind_B**–**[in]**array of`nnz_B`

elements containing the column indices of the sparse CSR matrix \(B\).**beta**–**[in]**scalar \(\beta\).**descr_D**–**[in]**descriptor of the sparse CSR matrix \(D\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**nnz_D**–**[in]**number of non-zero entries of the sparse CSR matrix \(D\).**csr_row_ptr_D**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(D\).**csr_col_ind_D**–**[in]**array of`nnz_D`

elements containing the column indices of the sparse CSR matrix \(D\).**info_C**–**[inout]**structure that holds meta data for the sparse CSR matrix \(C\).**buffer_size**–**[out]**number of bytes of the temporary storage buffer required by[rocsparse_csrgemm_nnz()](#rocsparse__csrgemm_8h_1a09cb61e11e4808b1b01d96fa311fb021)and[rocsparse_Xcsrgemm()](#rocsparse__csrgemm_8h_1a58f234545a387b56f9c9a58f68d15561).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`n`

,`k`

,`nnz_A`

,`nnz_B`

or`nnz_D`

is invalid.**rocsparse_status_invalid_pointer**–`alpha`

and`beta`

are invalid,`descr_A`

,`csr_row_ptr_A`

,`csr_col_ind_A`

,`descr_B`

,`csr_row_ptr_B`

or`csr_col_ind_B`

are invalid if`alpha`

is valid,`descr_D`

,`csr_row_ptr_D`

or`csr_col_ind_D`

is invalid if`beta`

is valid,`info_C`

or`buffer_size`

is invalid.**rocsparse_status_not_implemented**–`trans_A`

!=[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528),`trans_B`

!=[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528), or`rocsparse_matrix_type`

!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_csrgemm_nnz()[#](#rocsparse-csrgemm-nnz)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_csrgemm_nnz([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)k, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_B, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_D,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_D, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*nnz_C, const[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info_C, void *temp_buffer)[#](#_CPPv421rocsparse_csrgemm_nnz16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descrP13rocsparse_intP13rocsparse_intK18rocsparse_mat_infoPv) Sparse matrix sparse matrix multiplication using CSR storage format.

`rocsparse_csrgemm_nnz`

computes the total CSR non-zero elements and the CSR row offsets, that point to the start of every row of the sparse CSR matrix, of the resulting multiplied matrix C. It is assumed that`csr_row_ptr_C`

has been allocated with size`m+1`

. The required buffer size can be obtained by[rocsparse_scsrgemm_buffer_size()](#rocsparse__csrgemm_8h_1af8812530a35660e6241d7080ec2c60d5),[rocsparse_dcsrgemm_buffer_size()](#rocsparse__csrgemm_8h_1a576c60db08b539352a068f71fd756b89),[rocsparse_ccsrgemm_buffer_size()](#rocsparse__csrgemm_8h_1a3a6a040cdfd0471f8cb3801369255e59)and[rocsparse_zcsrgemm_buffer_size()](#rocsparse__csrgemm_8h_1a28bc7bb2b05f03fca05ee63fb94a7c40), respectively.Note

Please note, that for matrix products with more than 8192 intermediate products per row, additional temporary storage buffer is allocated by the algorithm.

Note

This function supports unsorted CSR matrices as input, while output will be sorted. Please note that matrices B and D can only be unsorted up to 8192 intermediate products per row. If this number is exceeded,

[rocsparse_status_requires_sorted_storage](enumerations.html#rocsparse-types_8h_1a578f8c5c1b08f358bf4605b0031006a8ac43738a03526c1aa8f217aaa26d8cbe8)will be returned.Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**trans_A**–**[in]**matrix \(A\) operation type.**trans_B**–**[in]**matrix \(B\) operation type.**m**–**[in]**number of rows of the sparse CSR matrix \(op(A)\) and \(C\).**n**–**[in]**number of columns of the sparse CSR matrix \(op(B)\) and \(C\).**k**–**[in]**number of columns of the sparse CSR matrix \(op(A)\) and number of rows of the sparse CSR matrix \(op(B)\).**descr_A**–**[in]**descriptor of the sparse CSR matrix \(A\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**nnz_A**–**[in]**number of non-zero entries of the sparse CSR matrix \(A\).**csr_row_ptr_A**–**[in]**array of`m+1`

elements ( \(op(A) == A\),`k+1`

otherwise) that point to the start of every row of the sparse CSR matrix \(op(A)\).**csr_col_ind_A**–**[in]**array of`nnz_A`

elements containing the column indices of the sparse CSR matrix \(A\).**descr_B**–**[in]**descriptor of the sparse CSR matrix \(B\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**nnz_B**–**[in]**number of non-zero entries of the sparse CSR matrix \(B\).**csr_row_ptr_B**–**[in]**array of`k+1`

elements ( \(op(B) == B\),`m+1`

otherwise) that point to the start of every row of the sparse CSR matrix \(op(B)\).**csr_col_ind_B**–**[in]**array of`nnz_B`

elements containing the column indices of the sparse CSR matrix \(B\).**descr_D**–**[in]**descriptor of the sparse CSR matrix \(D\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**nnz_D**–**[in]**number of non-zero entries of the sparse CSR matrix \(D\).**csr_row_ptr_D**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(D\).**csr_col_ind_D**–**[in]**array of`nnz_D`

elements containing the column indices of the sparse CSR matrix \(D\).**descr_C**–**[in]**descriptor of the sparse CSR matrix \(C\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**csr_row_ptr_C**–**[out]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(C\).**nnz_C**–**[out]**pointer to the number of non-zero entries of the sparse CSR matrix \(C\).**info_C**–**[in]**structure that holds meta data for the sparse CSR matrix \(C\).**temp_buffer**–**[in]**temporary storage buffer allocated by the user, size is returned by[rocsparse_scsrgemm_buffer_size()](#rocsparse__csrgemm_8h_1af8812530a35660e6241d7080ec2c60d5),[rocsparse_dcsrgemm_buffer_size()](#rocsparse__csrgemm_8h_1a576c60db08b539352a068f71fd756b89),[rocsparse_ccsrgemm_buffer_size()](#rocsparse__csrgemm_8h_1a3a6a040cdfd0471f8cb3801369255e59)or[rocsparse_zcsrgemm_buffer_size()](#rocsparse__csrgemm_8h_1a28bc7bb2b05f03fca05ee63fb94a7c40).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`n`

,`k`

,`nnz_A`

,`nnz_B`

or`nnz_D`

is invalid.**rocsparse_status_invalid_pointer**–`descr_A`

,`csr_row_ptr_A`

,`csr_col_ind_A`

,`descr_B`

,`csr_row_ptr_B`

,`csr_col_ind_B`

,`descr_D`

,`csr_row_ptr_D`

,`csr_col_ind_D`

,`descr_C`

,`csr_row_ptr_C`

,`nnz_C`

,`info_C`

or`temp_buffer`

is invalid.**rocsparse_status_memory_error**– additional buffer for long rows could not be allocated.**rocsparse_status_not_implemented**–`trans_A`

!=[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528),`trans_B`

!=[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528), or`rocsparse_matrix_type`

!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_csrgemm_symbolic()[#](#rocsparse-csrgemm-symbolic)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_csrgemm_symbolic([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)k, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_B, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_D,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_D, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_C, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_C, const[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info_C, void *temp_buffer)[#](#_CPPv426rocsparse_csrgemm_symbolic16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intP13rocsparse_intK18rocsparse_mat_infoPv) Sparse matrix sparse matrix symbolic multiplication using CSR storage format.

`rocsparse_csrgemm_symbolic`

multiplies two sparsity patterns and add an extra one:\[ opA \cdot op(B) + D \]with \(m \times k\) matrix \(A\), defined in CSR storage format, the sparse \(k \times n\) matrix \(B\), defined in CSR storage format and the sparse \(m \times n\) matrix \(D\). The * final result is stored in the sparse \(m \times n\) matrix \(C\), defined in CSR storage format, such that\[ C := op(A) \cdot op(B) + D, \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if trans_A == rocsparse_operation_none} \\ A^T, & \text{if trans_A == rocsparse_operation_transpose} \\ A^H, & \text{if trans_A == rocsparse_operation_conjugate_transpose} \end{array} \right. \end{split}\]and\[\begin{split} op(B) = \left\{ \begin{array}{ll} B, & \text{if trans_B == rocsparse_operation_none} \\ B^T, & \text{if trans_B == rocsparse_operation_transpose} \\ B^H, & \text{if trans_B == rocsparse_operation_conjugate_transpose} \end{array} \right. \end{split}\]It is assumed that

`csr_row_ptr_C`

has already been filled and that and`csr_col_ind_C`

is allocated by the user.`csr_row_ptr_C`

and allocation size of`csr_col_ind_C`

is defined by the number of non-zero elements of the sparse CSR matrix C. Both can be obtained by[rocsparse_csrgemm_nnz()](#rocsparse__csrgemm_8h_1a09cb61e11e4808b1b01d96fa311fb021). The required buffer size for the computation can be obtained by[rocsparse_scsrgemm_buffer_size()](#rocsparse__csrgemm_8h_1af8812530a35660e6241d7080ec2c60d5),[rocsparse_dcsrgemm_buffer_size()](#rocsparse__csrgemm_8h_1a576c60db08b539352a068f71fd756b89),[rocsparse_ccsrgemm_buffer_size()](#rocsparse__csrgemm_8h_1a3a6a040cdfd0471f8cb3801369255e59)and[rocsparse_zcsrgemm_buffer_size()](#rocsparse__csrgemm_8h_1a28bc7bb2b05f03fca05ee63fb94a7c40), respectively.**Example**This example multiplies symbolically two CSR matrices and adds the result to another CSR matrix.

// Initialize scalar multipliers float alpha = 2.0f; float beta = 1.0f; // Create matrix descriptors rocsparse_mat_descr descr_A; rocsparse_mat_descr descr_B; rocsparse_mat_descr descr_C; rocsparse_mat_descr descr_D; rocsparse_create_mat_descr(&descr_A); rocsparse_create_mat_descr(&descr_B); rocsparse_create_mat_descr(&descr_C); rocsparse_create_mat_descr(&descr_D); // Create matrix info structure rocsparse_mat_info info_C; rocsparse_create_mat_info(&info_C); // Set pointer mode rocsparse_set_pointer_mode(handle, rocsparse_pointer_mode_host); // Query rocsparse for the required buffer size size_t buffer_size; rocsparse_scsrgemm_buffer_size(handle, rocsparse_operation_none, rocsparse_operation_none, m, n, k, &alpha, descr_A, nnz_A, csr_row_ptr_A, csr_col_ind_A, descr_B, nnz_B, csr_row_ptr_B, csr_col_ind_B, &beta, descr_D, nnz_D, csr_row_ptr_D, csr_col_ind_D, info_C, &buffer_size); // Allocate buffer void* buffer; hipMalloc(&buffer, buffer_size); // Obtain number of total non-zero entries in C and row pointers of C rocsparse_int nnz_C; hipMalloc((void**)&csr_row_ptr_C, sizeof(rocsparse_int) * (m + 1)); rocsparse_csrgemm_nnz(handle, rocsparse_operation_none, rocsparse_operation_none, m, n, k, descr_A, nnz_A, csr_row_ptr_A, csr_col_ind_A, descr_B, nnz_B, csr_row_ptr_B, csr_col_ind_B, descr_D, nnz_D, csr_row_ptr_D, csr_col_ind_D, descr_C, csr_row_ptr_C, &nnz_C, info_C, buffer); // Compute column indices of C hipMalloc((void**)&csr_col_ind_C, sizeof(rocsparse_int) * nnz_C); rocsparse_csrgemm_symbolic(handle, rocsparse_operation_none, rocsparse_operation_none, m, n, k, descr_A, nnz_A, csr_row_ptr_A, csr_col_ind_A, descr_B, nnz_B, csr_row_ptr_B, csr_col_ind_B, descr_D, nnz_D, csr_row_ptr_D, csr_col_ind_D, descr_C, nnz_C, csr_row_ptr_C, csr_col_ind_C, info_C, buffer);


Note

Please note, that for matrix products with more than 4096 non-zero entries per row, additional temporary storage buffer is allocated by the algorithm.

Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**trans_A**–**[in]**matrix \(A\) operation type.**trans_B**–**[in]**matrix \(B\) operation type.**m**–**[in]**number of rows of the sparse CSR matrix \(op(A)\) and \(C\).**n**–**[in]**number of columns of the sparse CSR matrix \(op(B)\) and \(C\).**k**–**[in]**number of columns of the sparse CSR matrix \(op(A)\) and number of rows of the sparse CSR matrix \(op(B)\).**descr_A**–**[in]**descriptor of the sparse CSR matrix \(A\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**nnz_A**–**[in]**number of non-zero entries of the sparse CSR matrix \(A\).**csr_row_ptr_A**–**[in]**array of`m+1`

elements ( \(op(A) == A\),`k+1`

otherwise) that point to the start of every row of the sparse CSR matrix \(op(A)\).**csr_col_ind_A**–**[in]**array of`nnz_A`

elements containing the column indices of the sparse CSR matrix \(A\).**descr_B**–**[in]**descriptor of the sparse CSR matrix \(B\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**nnz_B**–**[in]**number of non-zero entries of the sparse CSR matrix \(B\).**csr_row_ptr_B**–**[in]**array of`k+1`

elements ( \(op(B) == B\),`m+1`

otherwise) that point to the start of every row of the sparse CSR matrix \(op(B)\).**csr_col_ind_B**–**[in]**array of`nnz_B`

elements containing the column indices of the sparse CSR matrix \(B\).**descr_D**–**[in]**descriptor of the sparse CSR matrix \(D\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**nnz_D**–**[in]**number of non-zero entries of the sparse CSR matrix \(D\).**csr_row_ptr_D**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(D\).**csr_col_ind_D**–**[in]**array of`nnz_D`

elements containing the column indices of the sparse CSR matrix \(D\).**descr_C**–**[in]**descriptor of the sparse CSR matrix \(C\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**nnz_C**–**[in]**number of non-zero entries of the sparse CSR matrix \(C\).**csr_row_ptr_C**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(C\).**csr_col_ind_C**–**[out]**array of`nnz_C`

elements containing the column indices of the sparse CSR matrix \(C\).**info_C**–**[in]**structure that holds meta data for the sparse CSR matrix \(C\).**temp_buffer**–**[in]**temporary storage buffer allocated by the user, size is returned by[rocsparse_scsrgemm_buffer_size()](#rocsparse__csrgemm_8h_1af8812530a35660e6241d7080ec2c60d5),[rocsparse_dcsrgemm_buffer_size()](#rocsparse__csrgemm_8h_1a576c60db08b539352a068f71fd756b89),[rocsparse_ccsrgemm_buffer_size()](#rocsparse__csrgemm_8h_1a3a6a040cdfd0471f8cb3801369255e59)or[rocsparse_zcsrgemm_buffer_size()](#rocsparse__csrgemm_8h_1a28bc7bb2b05f03fca05ee63fb94a7c40).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`n`

,`k`

,`nnz_A`

,`nnz_B`

or`nnz_D`

is invalid.**rocsparse_status_invalid_pointer**–`descr_A`

,`csr_row_ptr_A`

,`csr_col_ind_A`

,`descr_B`

,`csr_row_ptr_B`

or`csr_col_ind_B`

,`descr_D`

,`csr_row_ptr_D`

,`csr_col_ind_D`

`csr_row_ptr_C`

,`csr_col_ind_C`

,`info_C`

or`temp_buffer`

is invalid.**rocsparse_status_memory_error**– additional buffer for long rows could not be allocated.**rocsparse_status_not_implemented**–`trans_A`

!=[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528),`trans_B`

!=[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528), or`rocsparse_matrix_type`

!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_csrgemm()[#](#rocsparse-csrgemm)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scsrgemm([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)k, const float *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_A, const float *csr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_B, const float *csr_val_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_B, const float *beta, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_D,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_D, const float *csr_val_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_D, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_C, float *csr_val_C, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_C, const[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info_C, void *temp_buffer)[#](#_CPPv418rocsparse_scsrgemm16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descr13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_intPKfK19rocsparse_mat_descr13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descrPfPK13rocsparse_intP13rocsparse_intK18rocsparse_mat_infoPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcsrgemm([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)k, const double *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_A, const double *csr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_B, const double *csr_val_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_B, const double *beta, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_D,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_D, const double *csr_val_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_D, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_C, double *csr_val_C, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_C, const[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info_C, void *temp_buffer)[#](#_CPPv418rocsparse_dcsrgemm16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKdK19rocsparse_mat_descr13rocsparse_intPKdPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPKdPK13rocsparse_intPK13rocsparse_intPKdK19rocsparse_mat_descr13rocsparse_intPKdPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descrPdPK13rocsparse_intP13rocsparse_intK18rocsparse_mat_infoPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccsrgemm([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)k, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_A, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_B, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_B, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*beta, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_D,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_D, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_D, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_C,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val_C, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_C, const[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info_C, void *temp_buffer)[#](#_CPPv418rocsparse_ccsrgemm16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPK23rocsparse_float_complexK19rocsparse_mat_descr13rocsparse_intPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_intPK23rocsparse_float_complexK19rocsparse_mat_descr13rocsparse_intPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descrP23rocsparse_float_complexPK13rocsparse_intP13rocsparse_intK18rocsparse_mat_infoPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcsrgemm([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)k, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_A, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_B, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_B, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*beta, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_D,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_D, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_D, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_C,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val_C, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_C, const[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info_C, void *temp_buffer)[#](#_CPPv418rocsparse_zcsrgemm16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPK24rocsparse_double_complexK19rocsparse_mat_descr13rocsparse_intPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_intPK24rocsparse_double_complexK19rocsparse_mat_descr13rocsparse_intPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descrP24rocsparse_double_complexPK13rocsparse_intP13rocsparse_intK18rocsparse_mat_infoPv) Sparse matrix sparse matrix multiplication using CSR storage format.

`rocsparse_csrgemm`

multiplies the scalar \(\alpha\) with the sparse \(m \times k\) matrix \(A\), defined in CSR storage format, and the sparse \(k \times n\) matrix \(B\), defined in CSR storage format, and adds the result to the sparse \(m \times n\) matrix \(D\) that is multiplied by \(\beta\). The final result is stored in the sparse \(m \times n\) matrix \(C\), defined in CSR storage format, such that\[ C := \alpha \cdot op(A) \cdot op(B) + \beta \cdot D, \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if trans_A == rocsparse_operation_none} \\ A^T, & \text{if trans_A == rocsparse_operation_transpose} \\ A^H, & \text{if trans_A == rocsparse_operation_conjugate_transpose} \end{array} \right. \end{split}\]and\[\begin{split} op(B) = \left\{ \begin{array}{ll} B, & \text{if trans_B == rocsparse_operation_none} \\ B^T, & \text{if trans_B == rocsparse_operation_transpose} \\ B^H, & \text{if trans_B == rocsparse_operation_conjugate_transpose} \end{array} \right. \end{split}\]It is assumed that

`csr_row_ptr_C`

has already been filled and that`csr_val_C`

and`csr_col_ind_C`

are allocated by the user.`csr_row_ptr_C`

and allocation size of`csr_col_ind_C`

and`csr_val_C`

is defined by the number of non-zero elements of the sparse CSR matrix C. Both can be obtained by[rocsparse_csrgemm_nnz()](#rocsparse__csrgemm_8h_1a09cb61e11e4808b1b01d96fa311fb021). The required buffer size for the computation can be obtained by[rocsparse_scsrgemm_buffer_size()](#rocsparse__csrgemm_8h_1af8812530a35660e6241d7080ec2c60d5),[rocsparse_dcsrgemm_buffer_size()](#rocsparse__csrgemm_8h_1a576c60db08b539352a068f71fd756b89),[rocsparse_ccsrgemm_buffer_size()](#rocsparse__csrgemm_8h_1a3a6a040cdfd0471f8cb3801369255e59)and[rocsparse_zcsrgemm_buffer_size()](#rocsparse__csrgemm_8h_1a28bc7bb2b05f03fca05ee63fb94a7c40), respectively.**Example**This example multiplies two CSR matrices with a scalar alpha and adds the result to another CSR matrix.

// Initialize scalar multipliers float alpha = 2.0f; float beta = 1.0f; // Create matrix descriptors rocsparse_mat_descr descr_A; rocsparse_mat_descr descr_B; rocsparse_mat_descr descr_C; rocsparse_mat_descr descr_D; rocsparse_create_mat_descr(&descr_A); rocsparse_create_mat_descr(&descr_B); rocsparse_create_mat_descr(&descr_C); rocsparse_create_mat_descr(&descr_D); // Create matrix info structure rocsparse_mat_info info_C; rocsparse_create_mat_info(&info_C); // Set pointer mode rocsparse_set_pointer_mode(handle, rocsparse_pointer_mode_host); // Query rocsparse for the required buffer size size_t buffer_size; rocsparse_scsrgemm_buffer_size(handle, rocsparse_operation_none, rocsparse_operation_none, m, n, k, &alpha, descr_A, nnz_A, csr_row_ptr_A, csr_col_ind_A, descr_B, nnz_B, csr_row_ptr_B, csr_col_ind_B, &beta, descr_D, nnz_D, csr_row_ptr_D, csr_col_ind_D, info_C, &buffer_size); // Allocate buffer void* buffer; hipMalloc(&buffer, buffer_size); // Obtain number of total non-zero entries in C and row pointers of C rocsparse_int nnz_C; hipMalloc((void**)&csr_row_ptr_C, sizeof(rocsparse_int) * (m + 1)); rocsparse_csrgemm_nnz(handle, rocsparse_operation_none, rocsparse_operation_none, m, n, k, descr_A, nnz_A, csr_row_ptr_A, csr_col_ind_A, descr_B, nnz_B, csr_row_ptr_B, csr_col_ind_B, descr_D, nnz_D, csr_row_ptr_D, csr_col_ind_D, descr_C, csr_row_ptr_C, &nnz_C, info_C, buffer); // Compute column indices and values of C hipMalloc((void**)&csr_col_ind_C, sizeof(rocsparse_int) * nnz_C); hipMalloc((void**)&csr_val_C, sizeof(float) * nnz_C); rocsparse_scsrgemm(handle, rocsparse_operation_none, rocsparse_operation_none, m, n, k, &alpha, descr_A, nnz_A, csr_val_A, csr_row_ptr_A, csr_col_ind_A, descr_B, nnz_B, csr_val_B, csr_row_ptr_B, csr_col_ind_B, &beta, descr_D, nnz_D, csr_val_D, csr_row_ptr_D, csr_col_ind_D, descr_C, csr_val_C, csr_row_ptr_C, csr_col_ind_C, info_C, buffer);


Note

This function does not produce deterministic results.

Note

If \(\alpha == 0\), then \(C = \beta \cdot D\) will be computed.

Note

If \(\beta == 0\), then \(C = \alpha \cdot op(A) \cdot op(B)\) will be computed.

Note

\(\alpha == beta == 0\) is invalid.

Note

Please note, that for matrix products with more than 4096 non-zero entries per row, additional temporary storage buffer is allocated by the algorithm.

Note

This function supports unsorted CSR matrices as input, while output will be sorted. Please note that matrices B and D can only be unsorted up to 4096 non-zero entries per row. If this number is exceeded,

[rocsparse_status_requires_sorted_storage](enumerations.html#rocsparse-types_8h_1a578f8c5c1b08f358bf4605b0031006a8ac43738a03526c1aa8f217aaa26d8cbe8)will be returned.Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**trans_A**–**[in]**matrix \(A\) operation type.**trans_B**–**[in]**matrix \(B\) operation type.**m**–**[in]**number of rows of the sparse CSR matrix \(op(A)\) and \(C\).**n**–**[in]**number of columns of the sparse CSR matrix \(op(B)\) and \(C\).**k**–**[in]**number of columns of the sparse CSR matrix \(op(A)\) and number of rows of the sparse CSR matrix \(op(B)\).**alpha**–**[in]**scalar \(\alpha\).**descr_A**–**[in]**descriptor of the sparse CSR matrix \(A\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**nnz_A**–**[in]**number of non-zero entries of the sparse CSR matrix \(A\).**csr_val_A**–**[in]**array of`nnz_A`

elements of the sparse CSR matrix \(A\).**csr_row_ptr_A**–**[in]**array of`m+1`

elements ( \(op(A) == A\),`k+1`

otherwise) that point to the start of every row of the sparse CSR matrix \(op(A)\).**csr_col_ind_A**–**[in]**array of`nnz_A`

elements containing the column indices of the sparse CSR matrix \(A\).**descr_B**–**[in]**descriptor of the sparse CSR matrix \(B\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**nnz_B**–**[in]**number of non-zero entries of the sparse CSR matrix \(B\).**csr_val_B**–**[in]**array of`nnz_B`

elements of the sparse CSR matrix \(B\).**csr_row_ptr_B**–**[in]**array of`k+1`

elements ( \(op(B) == B\),`m+1`

otherwise) that point to the start of every row of the sparse CSR matrix \(op(B)\).**csr_col_ind_B**–**[in]**array of`nnz_B`

elements containing the column indices of the sparse CSR matrix \(B\).**beta**–**[in]**scalar \(\beta\).**descr_D**–**[in]**descriptor of the sparse CSR matrix \(D\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**nnz_D**–**[in]**number of non-zero entries of the sparse CSR matrix \(D\).**csr_val_D**–**[in]**array of`nnz_D`

elements of the sparse CSR matrix \(D\).**csr_row_ptr_D**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(D\).**csr_col_ind_D**–**[in]**array of`nnz_D`

elements containing the column indices of the sparse CSR matrix \(D\).**descr_C**–**[in]**descriptor of the sparse CSR matrix \(C\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**csr_val_C**–**[out]**array of`nnz_C`

elements of the sparse CSR matrix \(C\).**csr_row_ptr_C**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(C\).**csr_col_ind_C**–**[out]**array of`nnz_C`

elements containing the column indices of the sparse CSR matrix \(C\).**info_C**–**[in]**structure that holds meta data for the sparse CSR matrix \(C\).**temp_buffer**–**[in]**temporary storage buffer allocated by the user, size is returned by[rocsparse_scsrgemm_buffer_size()](#rocsparse__csrgemm_8h_1af8812530a35660e6241d7080ec2c60d5),[rocsparse_dcsrgemm_buffer_size()](#rocsparse__csrgemm_8h_1a576c60db08b539352a068f71fd756b89),[rocsparse_ccsrgemm_buffer_size()](#rocsparse__csrgemm_8h_1a3a6a040cdfd0471f8cb3801369255e59)or[rocsparse_zcsrgemm_buffer_size()](#rocsparse__csrgemm_8h_1a28bc7bb2b05f03fca05ee63fb94a7c40).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`n`

,`k`

,`nnz_A`

,`nnz_B`

or`nnz_D`

is invalid.**rocsparse_status_invalid_pointer**–`alpha`

and`beta`

are invalid,`descr_A`

,`csr_val_A`

,`csr_row_ptr_A`

,`csr_col_ind_A`

,`descr_B`

,`csr_val_B`

,`csr_row_ptr_B`

or`csr_col_ind_B`

are invalid if`alpha`

is valid,`descr_D`

,`csr_val_D`

,`csr_row_ptr_D`

or`csr_col_ind_D`

is invalid if`beta`

is valid,`csr_val_C`

,`csr_row_ptr_C`

,`csr_col_ind_C`

,`info_C`

or`temp_buffer`

is invalid.**rocsparse_status_memory_error**– additional buffer for long rows could not be allocated.**rocsparse_status_not_implemented**–`trans_A`

!=[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528),`trans_B`

!=[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528), or`rocsparse_matrix_type`

!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_csrgemm_numeric()[#](#rocsparse-csrgemm-numeric)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scsrgemm_numeric([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)k, const float *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_A, const float *csr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_B, const float *csr_val_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_B, const float *beta, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_D,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_D, const float *csr_val_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_D, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_C, float *csr_val_C, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_C, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_C, const[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info_C, void *temp_buffer)[#](#_CPPv426rocsparse_scsrgemm_numeric16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descr13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_intPKfK19rocsparse_mat_descr13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPfPK13rocsparse_intPK13rocsparse_intK18rocsparse_mat_infoPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcsrgemm_numeric([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)k, const double *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_A, const double *csr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_B, const double *csr_val_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_B, const double *beta, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_D,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_D, const double *csr_val_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_D, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_C, double *csr_val_C, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_C, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_C, const[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info_C, void *temp_buffer)[#](#_CPPv426rocsparse_dcsrgemm_numeric16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKdK19rocsparse_mat_descr13rocsparse_intPKdPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPKdPK13rocsparse_intPK13rocsparse_intPKdK19rocsparse_mat_descr13rocsparse_intPKdPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPdPK13rocsparse_intPK13rocsparse_intK18rocsparse_mat_infoPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccsrgemm_numeric([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)k, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_A, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_B, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_B, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*beta, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_D,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_D, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_D, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_C,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val_C, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_C, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_C, const[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info_C, void *temp_buffer)[#](#_CPPv426rocsparse_ccsrgemm_numeric16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPK23rocsparse_float_complexK19rocsparse_mat_descr13rocsparse_intPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_intPK23rocsparse_float_complexK19rocsparse_mat_descr13rocsparse_intPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intP23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_intK18rocsparse_mat_infoPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcsrgemm_numeric([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)k, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_A,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_A, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_A, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_A, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_B, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_B, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_B, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*beta, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_D,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_D, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_D, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_D, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr_C,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz_C,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val_C, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr_C, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind_C, const[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info_C, void *temp_buffer)[#](#_CPPv426rocsparse_zcsrgemm_numeric16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPK24rocsparse_double_complexK19rocsparse_mat_descr13rocsparse_intPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_intPK24rocsparse_double_complexK19rocsparse_mat_descr13rocsparse_intPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intP24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_intK18rocsparse_mat_infoPv) Sparse matrix sparse matrix numeric multiplication using CSR storage format.

`rocsparse_csrgemm_numeric`

multiplies the scalar \(\alpha\) with the sparse \(m \times k\) matrix \(A\), defined in CSR storage format, and the sparse \(k \times n\) matrix \(B\), defined in CSR storage format, and adds the result to the sparse \(m \times n\) matrix \(D\) that is multiplied by \(\beta\). The final result is stored in the sparse \(m \times n\) matrix \(C\), predefined in CSR storage format, such that\[ C := \alpha \cdot op(A) \cdot op(B) + \beta \cdot D, \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if trans_A == rocsparse_operation_none} \\ A^T, & \text{if trans_A == rocsparse_operation_transpose} \\ A^H, & \text{if trans_A == rocsparse_operation_conjugate_transpose} \end{array} \right. \end{split}\]and\[\begin{split} op(B) = \left\{ \begin{array}{ll} B, & \text{if trans_B == rocsparse_operation_none} \\ B^T, & \text{if trans_B == rocsparse_operation_transpose} \\ B^H, & \text{if trans_B == rocsparse_operation_conjugate_transpose} \end{array} \right. \end{split}\]The symbolic part of the csr matrix C can be obtained by

[rocsparse_csrgemm_symbolic()](#rocsparse__csrgemm_8h_1a15d8b8c0ec32752992bc22494d7988bc). It is assumed that`csr_row_ptr_C`

and`csr_col_ind_C`

have already been filled and that`csr_val_C`

is allocated by the user.`csr_row_ptr_C`

and allocation size of`csr_col_ind_C`

and`csr_val_C`

is defined by the number of non-zero elements of the sparse CSR matrix C. Both can be obtained by[rocsparse_csrgemm_nnz()](#rocsparse__csrgemm_8h_1a09cb61e11e4808b1b01d96fa311fb021). The required buffer size for the computation can be obtained by[rocsparse_scsrgemm_buffer_size()](#rocsparse__csrgemm_8h_1af8812530a35660e6241d7080ec2c60d5),[rocsparse_dcsrgemm_buffer_size()](#rocsparse__csrgemm_8h_1a576c60db08b539352a068f71fd756b89),[rocsparse_ccsrgemm_buffer_size()](#rocsparse__csrgemm_8h_1a3a6a040cdfd0471f8cb3801369255e59)and[rocsparse_zcsrgemm_buffer_size()](#rocsparse__csrgemm_8h_1a28bc7bb2b05f03fca05ee63fb94a7c40), respectively.**Example**This example multiplies two CSR matrices with a scalar alpha and adds the result to another CSR matrix.

// Initialize scalar multipliers float alpha = 2.0f; float beta = 1.0f; // Create matrix descriptors rocsparse_mat_descr descr_A; rocsparse_mat_descr descr_B; rocsparse_mat_descr descr_C; rocsparse_mat_descr descr_D; rocsparse_create_mat_descr(&descr_A); rocsparse_create_mat_descr(&descr_B); rocsparse_create_mat_descr(&descr_C); rocsparse_create_mat_descr(&descr_D); // Create matrix info structure rocsparse_mat_info info_C; rocsparse_create_mat_info(&info_C); // Set pointer mode rocsparse_set_pointer_mode(handle, rocsparse_pointer_mode_host); // Query rocsparse for the required buffer size size_t buffer_size; rocsparse_scsrgemm_buffer_size(handle, rocsparse_operation_none, rocsparse_operation_none, m, n, k, &alpha, descr_A, nnz_A, csr_row_ptr_A, csr_col_ind_A, descr_B, nnz_B, csr_row_ptr_B, csr_col_ind_B, &beta, descr_D, nnz_D, csr_row_ptr_D, csr_col_ind_D, info_C, &buffer_size); // Allocate buffer void* buffer; hipMalloc(&buffer, buffer_size); // Obtain number of total non-zero entries in C and row pointers of C rocsparse_int nnz_C; hipMalloc((void**)&csr_row_ptr_C, sizeof(rocsparse_int) * (m + 1)); rocsparse_csrgemm_nnz(handle, rocsparse_operation_none, rocsparse_operation_none, m, n, k, descr_A, nnz_A, csr_row_ptr_A, csr_col_ind_A, descr_B, nnz_B, csr_row_ptr_B, csr_col_ind_B, descr_D, nnz_D, csr_row_ptr_D, csr_col_ind_D, descr_C, csr_row_ptr_C, &nnz_C, info_C, buffer); // Compute column indices and values of C hipMalloc((void**)&csr_col_ind_C, sizeof(rocsparse_int) * nnz_C); rocsparse_csrgemm_symbolic(handle, rocsparse_operation_none, rocsparse_operation_none, m, n, k, descr_A, nnz_A, csr_row_ptr_A, csr_col_ind_A, descr_B, nnz_B, csr_row_ptr_B, csr_col_ind_B, descr_D, nnz_D, csr_row_ptr_D, csr_col_ind_D, descr_C, nnz_C, csr_row_ptr_C, csr_col_ind_C, info_C, buffer); hipMalloc((void**)&csr_val_C, sizeof(float) * nnz_C); rocsparse_scsrgemm_numeric(handle, rocsparse_operation_none, rocsparse_operation_none, m, n, k, &alpha, descr_A, nnz_A, csr_val_A, csr_row_ptr_A, csr_col_ind_A, descr_B, nnz_B, csr_val_B, csr_row_ptr_B, csr_col_ind_B, &beta, descr_D, nnz_D, csr_val_D, csr_row_ptr_D, csr_col_ind_D, descr_C, nnz_C, csr_val_C, csr_row_ptr_C, csr_col_ind_C, info_C, buffer);


Note

This function does not produce deterministic results.

Note

If \(\alpha == 0\), then \(C = \beta \cdot D\) will be computed.

Note

If \(\beta == 0\), then \(C = \alpha \cdot op(A) \cdot op(B)\) will be computed.

Note

\(\alpha == beta == 0\) is invalid.

Note

Please note, that for matrix products with more than 4096 non-zero entries per row, additional temporary storage buffer is allocated by the algorithm.

Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**trans_A**–**[in]**matrix \(A\) operation type.**trans_B**–**[in]**matrix \(B\) operation type.**m**–**[in]**number of rows of the sparse CSR matrix \(op(A)\) and \(C\).**n**–**[in]**number of columns of the sparse CSR matrix \(op(B)\) and \(C\).**k**–**[in]**number of columns of the sparse CSR matrix \(op(A)\) and number of rows of the sparse CSR matrix \(op(B)\).**alpha**–**[in]**scalar \(\alpha\).**descr_A**–**[in]**descriptor of the sparse CSR matrix \(A\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**nnz_A**–**[in]**number of non-zero entries of the sparse CSR matrix \(A\).**csr_val_A**–**[in]**array of`nnz_A`

elements of the sparse CSR matrix \(A\).**csr_row_ptr_A**–**[in]**array of`m+1`

elements ( \(op(A) == A\),`k+1`

otherwise) that point to the start of every row of the sparse CSR matrix \(op(A)\).**csr_col_ind_A**–**[in]**array of`nnz_A`

elements containing the column indices of the sparse CSR matrix \(A\).**descr_B**–**[in]**descriptor of the sparse CSR matrix \(B\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**nnz_B**–**[in]**number of non-zero entries of the sparse CSR matrix \(B\).**csr_val_B**–**[in]**array of`nnz_B`

elements of the sparse CSR matrix \(B\).**csr_row_ptr_B**–**[in]**array of`k+1`

elements ( \(op(B) == B\),`m+1`

otherwise) that point to the start of every row of the sparse CSR matrix \(op(B)\).**csr_col_ind_B**–**[in]**array of`nnz_B`

elements containing the column indices of the sparse CSR matrix \(B\).**beta**–**[in]**scalar \(\beta\).**descr_D**–**[in]**descriptor of the sparse CSR matrix \(D\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**nnz_D**–**[in]**number of non-zero entries of the sparse CSR matrix \(D\).**csr_val_D**–**[in]**array of`nnz_D`

elements of the sparse CSR matrix \(D\).**csr_row_ptr_D**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(D\).**csr_col_ind_D**–**[in]**array of`nnz_D`

elements containing the column indices of the sparse CSR matrix \(D\).**descr_C**–**[in]**descriptor of the sparse CSR matrix \(C\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**nnz_C**–**[in]**number of non-zero entries of the sparse CSR matrix \(C\).**csr_val_C**–**[out]**array of`nnz_C`

elements of the sparse CSR matrix \(C\).**csr_row_ptr_C**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(C\).**csr_col_ind_C**–**[in]**array of`nnz_C`

elements containing the column indices of the sparse CSR matrix \(C\).**info_C**–**[in]**structure that holds meta data for the sparse CSR matrix \(C\).**temp_buffer**–**[in]**temporary storage buffer allocated by the user, size is returned by[rocsparse_scsrgemm_buffer_size()](#rocsparse__csrgemm_8h_1af8812530a35660e6241d7080ec2c60d5),[rocsparse_dcsrgemm_buffer_size()](#rocsparse__csrgemm_8h_1a576c60db08b539352a068f71fd756b89),[rocsparse_ccsrgemm_buffer_size()](#rocsparse__csrgemm_8h_1a3a6a040cdfd0471f8cb3801369255e59)or[rocsparse_zcsrgemm_buffer_size()](#rocsparse__csrgemm_8h_1a28bc7bb2b05f03fca05ee63fb94a7c40).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`n`

,`k`

,`nnz_A`

,`nnz_B`

or`nnz_D`

is invalid.**rocsparse_status_invalid_pointer**–`alpha`

and`beta`

are invalid,`descr_A`

,`csr_val_A`

,`csr_row_ptr_A`

,`csr_col_ind_A`

,`descr_B`

,`csr_val_B`

,`csr_row_ptr_B`

or`csr_col_ind_B`

are invalid if`alpha`

is valid,`descr_D`

,`csr_val_D`

,`csr_row_ptr_D`

or`csr_col_ind_D`

is invalid if`beta`

is valid,`csr_val_C`

,`csr_row_ptr_C`

,`csr_col_ind_C`

,`info_C`

or`temp_buffer`

is invalid.**rocsparse_status_memory_error**– additional buffer for long rows could not be allocated.**rocsparse_status_not_implemented**–`trans_A`

!=[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528),`trans_B`

!=[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528), or`rocsparse_matrix_type`

!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).
