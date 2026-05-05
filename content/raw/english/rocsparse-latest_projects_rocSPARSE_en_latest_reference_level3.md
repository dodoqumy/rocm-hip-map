---
title: "Sparse level 3 functions &#8212; rocSPARSE 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocSPARSE/en/latest/reference/level3.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:16:58.599619+00:00
content_hash: "5366e057996875a2"
---

# Sparse level 3 functions[#](#sparse-level-3-functions)

This module contains all sparse level 3 routines.

The sparse level 3 routines describe operations between a matrix in sparse format and multiple vectors in dense format that can also be seen as a dense matrix.

## rocsparse_bsrmm()[#](#rocsparse-bsrmm)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sbsrmm([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)kb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const float *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim, const float *B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb, const float *beta, float *C,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldc)[#](#_CPPv416rocsparse_sbsrmm16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_intPKf13rocsparse_intPKfPf13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dbsrmm([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)kb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const double *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim, const double *B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb, const double *beta, double *C,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldc)[#](#_CPPv416rocsparse_dbsrmm16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPKdK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_int13rocsparse_intPKd13rocsparse_intPKdPd13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cbsrmm([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)kb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*beta,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*C,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldc)[#](#_CPPv416rocsparse_cbsrmm16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPK23rocsparse_float_complexK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_intPK23rocsparse_float_complex13rocsparse_intPK23rocsparse_float_complexP23rocsparse_float_complex13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zbsrmm([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)kb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*beta,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*C,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldc)[#](#_CPPv416rocsparse_zbsrmm16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPK24rocsparse_double_complexK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_intPK24rocsparse_double_complex13rocsparse_intPK24rocsparse_double_complexP24rocsparse_double_complex13rocsparse_int) Sparse matrix dense matrix multiplication using BSR storage format.

`rocsparse_bsrmm`

multiplies the scalar \(\alpha\) with a sparse \(m \times k\) matrix \(A\), defined in BSR storage format, and the column-oriented dense \(k \times n\) matrix \(B\) and adds the result to the column-oriented dense \(m \times n\) matrix \(C\) that is multiplied by the scalar \(\beta\), such that\[ C := \alpha \cdot op(A) \cdot op(B) + \beta \cdot C, \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if trans_A == rocsparse_operation_none} \\ \end{array} \right. \end{split}\]and\[\begin{split} op(B) = \left\{ \begin{array}{ll} B, & \text{if trans_B == rocsparse_operation_none} \\ B^T, & \text{if trans_B == rocsparse_operation_transpose} \\ \end{array} \right. \end{split}\]and where \(k = block\_dim \times kb\) and \(m = block\_dim \times mb\).**Example**This example multiplies a BSR matrix with a column-oriented dense matrix.

int main() { // 1 2 0 3 0 0 // A = 0 4 5 0 0 0 // 0 0 0 7 8 0 // 0 0 1 2 4 1 rocsparse_int block_dim = 2; rocsparse_int mb = 2; rocsparse_int kb = 3; rocsparse_int nnzb = 4; rocsparse_direction dir = rocsparse_direction_row; // alpha and beta float alpha = 1.0f; float beta = 0.0f; std::vector<rocsparse_int> hbsr_row_ptr = {0, 2, 4}; std::vector<rocsparse_int> hbsr_col_ind = {0, 1, 1, 2}; std::vector<float> hbsr_val = {1, 2, 0, 4, 0, 3, 5, 0, 0, 7, 1, 2, 8, 0, 4, 1}; // Set dimension n of B rocsparse_int n = 64; rocsparse_int m = mb * block_dim; rocsparse_int k = kb * block_dim; // Allocate and generate column-oriented dense matrix B std::vector<float> hB(k * n); for(rocsparse_int i = 0; i < k * n; ++i) { hB[i] = static_cast<float>(rand()) / static_cast<float>(RAND_MAX); } std::vector<float> hC(m * n); int* dbsr_row_ptr; int* dbsr_col_ind; float* dbsr_val; float* dB; float* dC; HIP_CHECK(hipMalloc(&dbsr_row_ptr, sizeof(int) * (mb + 1))); HIP_CHECK(hipMalloc(&dbsr_col_ind, sizeof(int) * nnzb)); HIP_CHECK(hipMalloc(&dbsr_val, sizeof(float) * nnzb * block_dim * block_dim)); HIP_CHECK(hipMalloc(&dB, sizeof(float) * k * n)); HIP_CHECK(hipMalloc(&dC, sizeof(float) * m * n)); HIP_CHECK(hipMemcpy( dbsr_row_ptr, hbsr_row_ptr.data(), sizeof(int) * (mb + 1), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dbsr_col_ind, hbsr_col_ind.data(), sizeof(int) * nnzb, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dbsr_val, hbsr_val.data(), sizeof(float) * nnzb * block_dim * block_dim, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dB, hB.data(), sizeof(float) * k * n, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dC, hC.data(), sizeof(float) * m * n, hipMemcpyHostToDevice)); // Create rocSPARSE handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Create matrix descriptor rocsparse_mat_descr descr; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr)); // Perform the matrix multiplication ROCSPARSE_CHECK(rocsparse_sbsrmm(handle, dir, rocsparse_operation_none, rocsparse_operation_none, mb, n, kb, nnzb, &alpha, descr, dbsr_val, dbsr_row_ptr, dbsr_col_ind, block_dim, dB, k, &beta, dC, m)); HIP_CHECK(hipMemcpy(hC.data(), dC, sizeof(float) * m * n, hipMemcpyDeviceToHost)); std::cout << "hC" << std::endl; for(size_t i = 0; i < hC.size(); i++) { std::cout << hC[i] << " "; } std::cout << "" << std::endl; // Clean up ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); // Clear up on device HIP_CHECK(hipFree(dbsr_row_ptr)); HIP_CHECK(hipFree(dbsr_col_ind)); HIP_CHECK(hipFree(dbsr_val)); HIP_CHECK(hipFree(dB)); HIP_CHECK(hipFree(dC)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dir**–**[in]**the storage format of the blocks. Can be[rocsparse_direction_row](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca40d95f05d0cd4ad3c89465959c58943e)or[rocsparse_direction_column](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca23355bb7b606c550ba61c781bcecfc5b).**trans_A**–**[in]**matrix \(A\) operation type. Currently, only[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528)is supported.**trans_B**–**[in]**matrix \(B\) operation type. Currently, only[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528)and rocsparse_operation_transpose are supported.**mb**–**[in]**number of block rows of the sparse BSR matrix \(A\).**n**–**[in]**number of columns of the column-oriented dense matrix \(op(B)\) and \(C\).**kb**–**[in]**number of block columns of the sparse BSR matrix \(A\).**nnzb**–**[in]**number of non-zero blocks of the sparse BSR matrix \(A\).**alpha**–**[in]**scalar \(\alpha\).**descr**–**[in]**descriptor of the sparse BSR matrix \(A\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**bsr_val**–**[in]**array of`nnzb*block_dim*block_dim`

elements of the sparse BSR matrix \(A\).**bsr_row_ptr**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix \(A\).**bsr_col_ind**–**[in]**array of`nnzb`

elements containing the block column indices of the sparse BSR matrix \(A\).**block_dim**–**[in]**size of the blocks in the sparse BSR matrix.**B**–**[in]**column-oriented dense matrix of dimension \(ldb \times n\) ( \(op(B) == B\)), \(ldb \times k\) otherwise.**ldb**–**[in]**leading dimension of \(B\), must be at least \(\max{(1, k)}\) ( \( op(B) == B\)) where \(k = block\_dim \times kb\), \(\max{(1, n)}\) otherwise.**beta**–**[in]**scalar \(\beta\).**C**–**[inout]**column-oriented dense matrix of dimension \(ldc \times n\).**ldc**–**[in]**leading dimension of \(C\), must be at least \(\max{(1, m)}\) ( \( op(A) == A\)) where \(m = block\_dim \times mb\), \(\max{(1, k)}\) where \(k = block\_dim \times kb\) otherwise.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`mb`

,`n`

,`kb`

,`nnzb`

,`ldb`

or`ldc`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`alpha`

,`bsr_val`

,`bsr_row_ptr`

,`bsr_col_ind`

,`B`

,`beta`

or`C`

pointer is invalid.**rocsparse_status_arch_mismatch**– the device is not supported.**rocsparse_status_not_implemented**–`trans_A`

!=[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528)or`trans_B`

==[rocsparse_operation_conjugate_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a6920c1aa5f80005eee4b66ea6f25330f)or[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_gebsrmm()[#](#rocsparse-gebsrmm)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sgebsrmm([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)kb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const float *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, const float *B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb, const float *beta, float *C,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldc)[#](#_CPPv418rocsparse_sgebsrmm16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intPKf13rocsparse_intPKfPf13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dgebsrmm([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)kb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const double *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, const double *B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb, const double *beta, double *C,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldc)[#](#_CPPv418rocsparse_dgebsrmm16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPKdK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intPKd13rocsparse_intPKdPd13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cgebsrmm([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)kb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*beta,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*C,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldc)[#](#_CPPv418rocsparse_cgebsrmm16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPK23rocsparse_float_complexK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intPK23rocsparse_float_complex13rocsparse_intPK23rocsparse_float_complexP23rocsparse_float_complex13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zgebsrmm([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)kb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*beta,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*C,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldc)[#](#_CPPv418rocsparse_zgebsrmm16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPK24rocsparse_double_complexK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intPK24rocsparse_double_complex13rocsparse_intPK24rocsparse_double_complexP24rocsparse_double_complex13rocsparse_int) Sparse matrix dense matrix multiplication using GEneral BSR storage format.

`rocsparse_gebsrmm`

multiplies the scalar \(\alpha\) with a sparse \(m \times k\) matrix \(A\), defined in GEneral BSR storage format, and the column-oriented dense \(k \times n\) matrix \(B\) and adds the result to the column-oriented dense \(m \times n\) matrix \(C\) that is multiplied by the scalar \(\beta\), such that\[ C := \alpha \cdot op(A) \cdot op(B) + \beta \cdot C, \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if trans_A == rocsparse_operation_none} \\ \end{array} \right. \end{split}\]and\[\begin{split} op(B) = \left\{ \begin{array}{ll} B, & \text{if trans_B == rocsparse_operation_none} \\ B^T, & \text{if trans_B == rocsparse_operation_transpose} \\ \end{array} \right. \end{split}\]and where \(k = col\_block\_dim \times kb\) and \(m = row\_block\_dim \times mb\).**Example**This example multiplies a GEneral BSR matrix with a column-oriented dense matrix.

int main() { // 1 2 0 3 0 0 // A = 0 4 5 0 0 0 // 0 0 0 7 8 0 // 0 0 1 2 4 1 rocsparse_int row_block_dim = 2; rocsparse_int col_block_dim = 3; rocsparse_int mb = 2; rocsparse_int kb = 2; rocsparse_int nnzb = 4; rocsparse_direction dir = rocsparse_direction_row; // alpha and beta float alpha = 1.0f; float beta = 0.0f; std::vector<rocsparse_int> hbsr_row_ptr = {0, 2, 4}; std::vector<rocsparse_int> hbsr_col_ind = {0, 1, 0, 1}; std::vector<float> hbsr_val = {1, 2, 0, 0, 4, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 7, 8, 0, 2, 4, 1}; // Set dimension n of B rocsparse_int n = 64; rocsparse_int m = mb * row_block_dim; rocsparse_int k = kb * col_block_dim; // Allocate and generate column-oriented dense matrix B std::vector<float> hB(k * n); for(rocsparse_int i = 0; i < k * n; ++i) { hB[i] = static_cast<float>(rand()) / static_cast<float>(RAND_MAX); } std::vector<float> hC(m * n); int* dbsr_row_ptr; int* dbsr_col_ind; float* dbsr_val; float* dB; float* dC; HIP_CHECK(hipMalloc(&dbsr_row_ptr, sizeof(int) * (mb + 1))); HIP_CHECK(hipMalloc(&dbsr_col_ind, sizeof(int) * nnzb)); HIP_CHECK(hipMalloc(&dbsr_val, sizeof(float) * nnzb * row_block_dim * col_block_dim)); HIP_CHECK(hipMalloc(&dB, sizeof(float) * k * n)); HIP_CHECK(hipMalloc(&dC, sizeof(float) * m * n)); HIP_CHECK(hipMemcpy( dbsr_row_ptr, hbsr_row_ptr.data(), sizeof(int) * (mb + 1), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dbsr_col_ind, hbsr_col_ind.data(), sizeof(int) * nnzb, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dbsr_val, hbsr_val.data(), sizeof(float) * nnzb * row_block_dim * col_block_dim, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dB, hB.data(), sizeof(float) * k * n, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dC, hC.data(), sizeof(float) * m * n, hipMemcpyHostToDevice)); // Create rocSPARSE handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Create matrix descriptor rocsparse_mat_descr descr; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr)); // Perform the matrix multiplication ROCSPARSE_CHECK(rocsparse_sgebsrmm(handle, dir, rocsparse_operation_none, rocsparse_operation_none, mb, n, kb, nnzb, &alpha, descr, dbsr_val, dbsr_row_ptr, dbsr_col_ind, row_block_dim, col_block_dim, dB, k, &beta, dC, m)); HIP_CHECK(hipMemcpy(hC.data(), dC, sizeof(float) * m * n, hipMemcpyDeviceToHost)); std::cout << "hC" << std::endl; for(size_t i = 0; i < hC.size(); i++) { std::cout << hC[i] << " "; } std::cout << "" << std::endl; // Clean up ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); // Clear up on device HIP_CHECK(hipFree(dbsr_row_ptr)); HIP_CHECK(hipFree(dbsr_col_ind)); HIP_CHECK(hipFree(dbsr_val)); HIP_CHECK(hipFree(dB)); HIP_CHECK(hipFree(dC)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dir**–**[in]**the storage format of the blocks. Can be[rocsparse_direction_row](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca40d95f05d0cd4ad3c89465959c58943e)or[rocsparse_direction_column](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca23355bb7b606c550ba61c781bcecfc5b).**trans_A**–**[in]**matrix \(A\) operation type. Currently, only[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528)is supported.**trans_B**–**[in]**matrix \(B\) operation type. Currently, only[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528)and rocsparse_operation_transpose are supported.**mb**–**[in]**number of block rows of the sparse GEneral BSR matrix \(A\).**n**–**[in]**number of columns of the column-oriented dense matrix \(op(B)\) and \(C\).**kb**–**[in]**number of block columns of the sparse GEneral BSR matrix \(A\).**nnzb**–**[in]**number of non-zero blocks of the sparse GEneral BSR matrix \(A\).**alpha**–**[in]**scalar \(\alpha\).**descr**–**[in]**descriptor of the sparse GEneral BSR matrix \(A\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**bsr_val**–**[in]**array of`nnzb*row_block_dim*col_block_dim`

elements of the sparse GEneral BSR matrix \(A\).**bsr_row_ptr**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse GEneral BSR matrix \(A\).**bsr_col_ind**–**[in]**array of`nnzb`

elements containing the block column indices of the sparse GEneral BSR matrix \(A\).**row_block_dim**–**[in]**row size of the blocks in the sparse GEneral BSR matrix.**col_block_dim**–**[in]**column size of the blocks in the sparse GEneral BSR matrix.**B**–**[in]**column-oriented dense matrix of dimension \(ldb \times n\) ( \(op(B) == B\)), \(ldb \times k\) otherwise.**ldb**–**[in]**leading dimension of \(B\), must be at least \(\max{(1, k)}\) ( \( op(B) == B\)) where \(k = col\_block\_dim \times kb\), \(\max{(1, n)}\) otherwise.**beta**–**[in]**scalar \(\beta\).**C**–**[inout]**column-oriented dense matrix of dimension \(ldc \times n\).**ldc**–**[in]**leading dimension of \(C\), must be at least \(\max{(1, m)}\) ( \( op(A) == A\)) where \(m = row\_block\_dim \times mb\), \(\max{(1, k)}\) where \(k = col\_block\_dim \times kb\) otherwise.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`mb`

,`n`

,`kb`

,`nnzb`

,`ldb`

,`ldc`

,`row_block_dim`

or`col_block_dim`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`alpha`

,`bsr_val`

,`bsr_row_ptr`

,`bsr_col_ind`

,`B`

,`beta`

or`C`

pointer is invalid.**rocsparse_status_arch_mismatch**– the device is not supported.**rocsparse_status_not_implemented**–`trans_A`

!=[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528)or`trans_B`

==[rocsparse_operation_conjugate_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a6920c1aa5f80005eee4b66ea6f25330f)or[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_csrmm()[#](#rocsparse-csrmm)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scsrmm([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)k,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const float *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, const float *B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb, const float *beta, float *C,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldc)[#](#_CPPv416rocsparse_scsrmm16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intPKf13rocsparse_intPKfPf13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcsrmm([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)k,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const double *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, const double *B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb, const double *beta, double *C,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldc)[#](#_CPPv416rocsparse_dcsrmm16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPKdK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_intPKd13rocsparse_intPKdPd13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccsrmm([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)k,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*beta,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*C,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldc)[#](#_CPPv416rocsparse_ccsrmm16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPK23rocsparse_float_complexK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_intPK23rocsparse_float_complex13rocsparse_intPK23rocsparse_float_complexP23rocsparse_float_complex13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcsrmm([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)k,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*beta,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*C,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldc)[#](#_CPPv416rocsparse_zcsrmm16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPK24rocsparse_double_complexK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_intPK24rocsparse_double_complex13rocsparse_intPK24rocsparse_double_complexP24rocsparse_double_complex13rocsparse_int) Sparse matrix dense matrix multiplication using CSR storage format.

`rocsparse_csrmm`

multiplies the scalar \(\alpha\) with a sparse \(m \times k\) matrix \(A\), defined in CSR storage format, and the column-oriented dense \(k \times n\) matrix \(B\) and adds the result to the column-oriented dense \(m \times n\) matrix \(C\) that is multiplied by the scalar \(\beta\), such that\[ C := \alpha \cdot op(A) \cdot op(B) + \beta \cdot C, \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if trans_A == rocsparse_operation_none} \\ A^T, & \text{if trans_A == rocsparse_operation_transpose} \\ A^H, & \text{if trans_A == rocsparse_operation_conjugate_transpose} \end{array} \right. \end{split}\]and\[\begin{split} op(B) = \left\{ \begin{array}{ll} B, & \text{if trans_B == rocsparse_operation_none} \\ B^T, & \text{if trans_B == rocsparse_operation_transpose} \\ B^H, & \text{if trans_B == rocsparse_operation_conjugate_transpose} \end{array} \right. \end{split}\]for(i = 0; i < ldc; ++i) { for(j = 0; j < n; ++j) { C[i][j] = beta * C[i][j]; for(k = csr_row_ptr[i]; k < csr_row_ptr[i + 1]; ++k) { C[i][j] += alpha * csr_val[k] * B[csr_col_ind[k]][j]; } } }

**Example**This example multiplies a CSR matrix with a column-oriented dense matrix.

int main() { // 1 2 0 3 0 // A = 0 4 5 0 0 // 6 0 0 7 8 rocsparse_int m = 3; rocsparse_int k = 5; rocsparse_int nnz = 8; // alpha and beta float alpha = 1.0f; float beta = 0.0f; std::vector<int> hcsr_row_ptr = {0, 3, 5, 8}; std::vector<int> hcsr_col_ind = {0, 1, 3, 1, 2, 0, 3, 4}; std::vector<float> hcsr_val = {1, 2, 3, 4, 5, 6, 7, 8}; // Set dimension n of B rocsparse_int n = 64; // Allocate and generate column-oriented dense matrix B std::vector<float> hB(k * n); for(rocsparse_int i = 0; i < k * n; ++i) { hB[i] = static_cast<float>(rand()) / static_cast<float>(RAND_MAX); } std::vector<float> hC(m * n); int* dcsr_row_ptr; int* dcsr_col_ind; float* dcsr_val; float* dB; float* dC; HIP_CHECK(hipMalloc(&dcsr_row_ptr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc(&dcsr_col_ind, sizeof(int) * nnz)); HIP_CHECK(hipMalloc(&dcsr_val, sizeof(float) * nnz)); HIP_CHECK(hipMalloc(&dB, sizeof(float) * k * n)); HIP_CHECK(hipMalloc(&dC, sizeof(float) * m * n)); HIP_CHECK( hipMemcpy(dcsr_row_ptr, hcsr_row_ptr.data(), sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsr_col_ind, hcsr_col_ind.data(), sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsr_val, hcsr_val.data(), sizeof(float) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dB, hB.data(), sizeof(float) * k * n, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dC, hC.data(), sizeof(float) * m * n, hipMemcpyHostToDevice)); // Create rocSPARSE handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Create matrix descriptor rocsparse_mat_descr descr; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr)); // Perform the matrix multiplication ROCSPARSE_CHECK(rocsparse_scsrmm(handle, rocsparse_operation_none, rocsparse_operation_none, m, n, k, nnz, &alpha, descr, dcsr_val, dcsr_row_ptr, dcsr_col_ind, dB, k, &beta, dC, m)); HIP_CHECK(hipMemcpy(hC.data(), dC, sizeof(float) * m * n, hipMemcpyDeviceToHost)); std::cout << "hC" << std::endl; for(size_t i = 0; i < hC.size(); i++) { std::cout << hC[i] << " "; } std::cout << "" << std::endl; // Clean up ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); // Clear up on device HIP_CHECK(hipFree(dcsr_row_ptr)); HIP_CHECK(hipFree(dcsr_col_ind)); HIP_CHECK(hipFree(dcsr_val)); HIP_CHECK(hipFree(dB)); HIP_CHECK(hipFree(dC)); return 0; }


Note

This function does not produce deterministic results when A is transposed.

Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**trans_A**–**[in]**matrix \(A\) operation type.**trans_B**–**[in]**matrix \(B\) operation type.**m**–**[in]**number of rows of the sparse CSR matrix \(A\).**n**–**[in]**number of columns of the column-oriented dense matrix \(op(B)\) and \(C\).**k**–**[in]**number of columns of the sparse CSR matrix \(A\).**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix \(A\).**alpha**–**[in]**scalar \(\alpha\).**descr**–**[in]**descriptor of the sparse CSR matrix \(A\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**csr_val**–**[in]**array of`nnz`

elements of the sparse CSR matrix \(A\).**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(A\).**csr_col_ind**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix \(A\).**B**–**[in]**column-oriented dense matrix of dimension \(ldb \times n\) ( \(op(B) == B\)), \(ldb \times k\) otherwise.**ldb**–**[in]**leading dimension of \(B\), must be at least \(\max{(1, k)}\) ( \(op(B) == B\)), \(\max{(1, n)}\) otherwise.**beta**–**[in]**scalar \(\beta\).**C**–**[inout]**column-oriented dense matrix of dimension \(ldc \times n\).**ldc**–**[in]**leading dimension of \(C\), must be at least \(\max{(1, m)}\) ( \(op(A) == A\)), \(\max{(1, k)}\) otherwise.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`n`

,`k`

,`nnz`

,`ldb`

or`ldc`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`alpha`

,`csr_val`

,`csr_row_ptr`

,`csr_col_ind`

,`B`

,`beta`

or`C`

pointer is invalid.**rocsparse_status_arch_mismatch**– the device is not supported.**rocsparse_status_not_implemented**–[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_csrsm_zero_pivot()[#](#rocsparse-csrsm-zero-pivot)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_csrsm_zero_pivot([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_int](types.html#_CPPv413rocsparse_int)*position)[#](#_CPPv426rocsparse_csrsm_zero_pivot16rocsparse_handle18rocsparse_mat_infoP13rocsparse_int) `rocsparse_csrsm_zero_pivot`

returns[rocsparse_status_zero_pivot](enumerations.html#rocsparse-types_8h_1a578f8c5c1b08f358bf4605b0031006a8a01fe264830c8ce6451ce6888bc8d3e80), if either a structural or numerical zero has been found during[rocsparse_Xcsrsm_solve()](#rocsparse__csrsm_8h_1aeb1fac99b8b77aa9e3f406df562fdfec)computation. The first zero pivot \(j\) at \(A_{j,j}\) is stored in`position`

, using same index base as the CSR matrix.`position`

can be in host or device memory. If no zero pivot has been found,`position`

is set to -1 and[rocsparse_status_success](enumerations.html#rocsparse-types_8h_1a578f8c5c1b08f358bf4605b0031006a8a96462a9361cfceb6cf9354e10fdc671b)is returned instead.Note

`rocsparse_csrsm_zero_pivot`

is a blocking function. It might influence performance negatively.Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**info**–**[in]**structure that holds the information collected during the analysis step.**position**–**[inout]**pointer to zero pivot \(j\), can be in host or device memory.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`info`

or`position`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_zero_pivot**– zero pivot has been found.



## rocsparse_csrsm_buffer_size()[#](#rocsparse-csrsm-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scsrsm_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nrhs,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const float *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, const float *B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, size_t *buffer_size)[#](#_CPPv428rocsparse_scsrsm_buffer_size16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intPKf13rocsparse_int18rocsparse_mat_info22rocsparse_solve_policyP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcsrsm_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nrhs,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const double *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, const double *B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, size_t *buffer_size)[#](#_CPPv428rocsparse_dcsrsm_buffer_size16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKdK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_intPKd13rocsparse_int18rocsparse_mat_info22rocsparse_solve_policyP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccsrsm_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nrhs,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, size_t *buffer_size)[#](#_CPPv428rocsparse_ccsrsm_buffer_size16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPK23rocsparse_float_complexK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_intPK23rocsparse_float_complex13rocsparse_int18rocsparse_mat_info22rocsparse_solve_policyP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcsrsm_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nrhs,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, size_t *buffer_size)[#](#_CPPv428rocsparse_zcsrsm_buffer_size16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPK24rocsparse_double_complexK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_intPK24rocsparse_double_complex13rocsparse_int18rocsparse_mat_info22rocsparse_solve_policyP6size_t) `rocsparse_csrsm_buffer_size`

returns the size of the temporary storage buffer that is required by[rocsparse_Xcsrsm_analysis()](#rocsparse__csrsm_8h_1ac8e943e992641859efdfea49a267133b)and[rocsparse_Xcsrsm_solve()](#rocsparse__csrsm_8h_1aeb1fac99b8b77aa9e3f406df562fdfec). The temporary storage buffer must be allocated by the user.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**trans_A**–**[in]**matrix A operation type.**trans_B**–**[in]**matrix B operation type.**m**–**[in]**number of rows of the sparse CSR matrix A.**nrhs**–**[in]**number of columns of the column-oriented dense matrix op(B).**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix A.**alpha**–**[in]**scalar \(\alpha\).**descr**–**[in]**descriptor of the sparse CSR matrix A.**csr_val**–**[in]**array of`nnz`

elements of the sparse CSR matrix A.**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix A.**csr_col_ind**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix A.**B**–**[in]**column-oriented dense matrix of dimension`m`

\(\times\)`nrhs`

elements of the rhs matrix B.**ldb**–**[in]**leading dimension of rhs matrix B.**info**–**[in]**structure that holds the information collected during the analysis step.**policy**–**[in]**[rocsparse_solve_policy_auto](enumerations.html#rocsparse-types_8h_1a5a3e261123e81a9e8b267c6109e26957a9c6bdf97e192d429ca536d5ab98ea866).**buffer_size**–**[out]**number of bytes of the temporary storage buffer required by[rocsparse_scsrsm_analysis()](#rocsparse__csrsm_8h_1ac8e943e992641859efdfea49a267133b),[rocsparse_dcsrsm_analysis()](#rocsparse__csrsm_8h_1a5db0418dbcf0d190bbc9a39383262249),[rocsparse_ccsrsm_analysis()](#rocsparse__csrsm_8h_1afb0c5ac8815449d79751b14f1d46a12e),[rocsparse_zcsrsm_analysis()](#rocsparse__csrsm_8h_1a723ab688ac65d4c28e517815c915a4d3),[rocsparse_scsrsm_solve()](#rocsparse__csrsm_8h_1aeb1fac99b8b77aa9e3f406df562fdfec),[rocsparse_dcsrsm_solve()](#rocsparse__csrsm_8h_1a8b3df909132dc8529c0356e665648139),[rocsparse_ccsrsm_solve()](#rocsparse__csrsm_8h_1a4cc8fbccf13bbcc36c0a612abdc9a2d4)and[rocsparse_zcsrsm_solve()](#rocsparse__csrsm_8h_1ab1a7360e8d47486d5716675ed6cf15de).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`nrhs`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`alpha`

,`descr`

,`csr_val`

,`csr_row_ptr`

,`csr_col_ind`

,`B`

,`info`

or`buffer_size`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_not_implemented**–`trans_A`

==[rocsparse_operation_conjugate_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a6920c1aa5f80005eee4b66ea6f25330f),`trans_B`

==[rocsparse_operation_conjugate_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a6920c1aa5f80005eee4b66ea6f25330f)or[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_csrsm_analysis()[#](#rocsparse-csrsm-analysis)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scsrsm_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nrhs,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const float *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, const float *B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_analysis_policy](enumerations.html#_CPPv425rocsparse_analysis_policy)analysis,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)solve, void *temp_buffer)[#](#_CPPv425rocsparse_scsrsm_analysis16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intPKf13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcsrsm_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nrhs,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const double *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, const double *B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_analysis_policy](enumerations.html#_CPPv425rocsparse_analysis_policy)analysis,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)solve, void *temp_buffer)[#](#_CPPv425rocsparse_dcsrsm_analysis16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKdK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_intPKd13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccsrsm_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nrhs,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_analysis_policy](enumerations.html#_CPPv425rocsparse_analysis_policy)analysis,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)solve, void *temp_buffer)[#](#_CPPv425rocsparse_ccsrsm_analysis16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPK23rocsparse_float_complexK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_intPK23rocsparse_float_complex13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcsrsm_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nrhs,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_analysis_policy](enumerations.html#_CPPv425rocsparse_analysis_policy)analysis,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)solve, void *temp_buffer)[#](#_CPPv425rocsparse_zcsrsm_analysis16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPK24rocsparse_double_complexK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_intPK24rocsparse_double_complex13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv) `rocsparse_csrsm_analysis`

performs the analysis step for[rocsparse_Xcsrsm_solve()](#rocsparse__csrsm_8h_1aeb1fac99b8b77aa9e3f406df562fdfec). It is expected that this function will be executed only once for a given matrix and particular operation type. The analysis meta data can be cleared by[rocsparse_csrsm_clear()](#rocsparse__csrsm_8h_1adc2df5dc12bee94c0a0f4484ca392ce4).`rocsparse_csrsm_analysis`

can share its meta data with[rocsparse_Xcsrilu0_analysis()](precond.html#rocsparse__csrilu0_8h_1a8b0496cb644c23fe65176e70315e431c),[rocsparse_Xcsric0_analysis()](precond.html#rocsparse__csric0_8h_1a00bf19a537e0d46b1c55826a9c23e23c), and[rocsparse_Xcsrsv_analysis()](level2.html#rocsparse__csrsv_8h_1af710dcbc752ca8203389907bcbe74273). Selecting[rocsparse_analysis_policy_reuse](enumerations.html#rocsparse-types_8h_1a43b20aa4bb19623a91b5952422fbe35ca658466413f4005c0c103d20d5e352078)policy can greatly improve computation performance of meta data. However, the user needs to make sure that the sparsity pattern remains unchanged. If this cannot be assured,[rocsparse_analysis_policy_force](enumerations.html#rocsparse-types_8h_1a43b20aa4bb19623a91b5952422fbe35cac66b70c4f519ddd03dcbe0f3a973401a)has to be used.Note

If the matrix sparsity pattern changes, the gathered information will become invalid.

Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**trans_A**–**[in]**matrix A operation type.**trans_B**–**[in]**matrix B operation type.**m**–**[in]**number of rows of the sparse CSR matrix A.**nrhs**–**[in]**number of columns of the column-oriented dense matrix op(B).**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix A.**alpha**–**[in]**scalar \(\alpha\).**descr**–**[in]**descriptor of the sparse CSR matrix A.**csr_val**–**[in]**array of`nnz`

elements of the sparse CSR matrix A.**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix A.**csr_col_ind**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix A.**B**–**[in]**column-oriented dense matrix of dimension`m`

\(\times\)`nrhs`

elements of the rhs matrix B.**ldb**–**[in]**leading dimension of rhs matrix B.**info**–**[out]**structure that holds the information collected during the analysis step.**analysis**–**[in]**[rocsparse_analysis_policy_reuse](enumerations.html#rocsparse-types_8h_1a43b20aa4bb19623a91b5952422fbe35ca658466413f4005c0c103d20d5e352078)or[rocsparse_analysis_policy_force](enumerations.html#rocsparse-types_8h_1a43b20aa4bb19623a91b5952422fbe35cac66b70c4f519ddd03dcbe0f3a973401a).**solve**–**[in]**[rocsparse_solve_policy_auto](enumerations.html#rocsparse-types_8h_1a5a3e261123e81a9e8b267c6109e26957a9c6bdf97e192d429ca536d5ab98ea866).**temp_buffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`nrhs`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`alpha`

,`descr`

,`csr_val`

,`csr_row_ptr`

,`csr_col_ind`

,`B`

,`info`

or`temp_buffer`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_not_implemented**–`trans_A`

==[rocsparse_operation_conjugate_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a6920c1aa5f80005eee4b66ea6f25330f),`trans_B`

==[rocsparse_operation_conjugate_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a6920c1aa5f80005eee4b66ea6f25330f)or[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_csrsm_solve()[#](#rocsparse-csrsm-solve)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scsrsm_solve([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nrhs,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const float *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, float *B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv422rocsparse_scsrsm_solve16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intPf13rocsparse_int18rocsparse_mat_info22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcsrsm_solve([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nrhs,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const double *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, double *B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv422rocsparse_dcsrsm_solve16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKdK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_intPd13rocsparse_int18rocsparse_mat_info22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccsrsm_solve([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nrhs,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv422rocsparse_ccsrsm_solve16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPK23rocsparse_float_complexK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_intP23rocsparse_float_complex13rocsparse_int18rocsparse_mat_info22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcsrsm_solve([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nrhs,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv422rocsparse_zcsrsm_solve16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPK24rocsparse_double_complexK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_intP24rocsparse_double_complex13rocsparse_int18rocsparse_mat_info22rocsparse_solve_policyPv) Sparse triangular system solve using CSR storage format.

`rocsparse_csrsm_solve`

solves a sparse triangular linear system of a sparse \(m \times m\) matrix, defined in CSR storage format, a column-oriented dense solution matrix \(X\) and the column-oriented dense right-hand side matrix \(B\) that is multiplied by \(\alpha\), such that\[ op(A) \cdot op(X) = \alpha \cdot op(B), \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if trans_A == rocsparse_operation_none} \\ A^T, & \text{if trans_A == rocsparse_operation_transpose} \\ A^H, & \text{if trans_A == rocsparse_operation_conjugate_transpose} \end{array} \right. \end{split}\],\[\begin{split} op(B) = \left\{ \begin{array}{ll} B, & \text{if trans_B == rocsparse_operation_none} \\ B^T, & \text{if trans_B == rocsparse_operation_transpose} \\ B^H, & \text{if trans_B == rocsparse_operation_conjugate_transpose} \end{array} \right. \end{split}\]and\[\begin{split} op(X) = \left\{ \begin{array}{ll} X, & \text{if trans_B == rocsparse_operation_none} \\ X^T, & \text{if trans_B == rocsparse_operation_transpose} \\ X^H, & \text{if trans_B == rocsparse_operation_conjugate_transpose} \end{array} \right. \end{split}\]The solution is performed inplace meaning that the matrix B is overwritten with the solution X after calling

`rocsparse_csrsm_solve`

. Given that the sparse matrix A is a square matrix, its size is \(m \times m\) regardless of whether A is transposed or not. The size of the column-oriented dense matrices B and X have size that depends on the value of`trans_B:`

\[\begin{split} op(B)/op(X) = \left\{ \begin{array}{ll} ldb \times nrhs, \text{ } ldb \ge m, & \text{if trans_B == rocsparse_operation_none} \\ ldb \times m, \text{ } ldb \ge nrhs, & \text{if trans_B == rocsparse_operation_transpose} \\ ldb \times m, \text{ } ldb \ge nrhs, & \text{if trans_B == rocsparse_operation_conjugate_transpose} \end{array} \right. \end{split}\]`rocsparse_csrsm_solve`

requires a user allocated temporary buffer. Its size is returned by[rocsparse_Xcsrsm_buffer_size()](#rocsparse__csrsm_8h_1aa378a95abfb5186809ba5a45bee986a6). The size of the required buffer is larger when`trans_A`

equals[rocsparse_operation_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a1ea3194d0c7bdb9e500d6faeead8ebf5)or[rocsparse_operation_conjugate_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a6920c1aa5f80005eee4b66ea6f25330f)and when`trans_B`

is[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528). The subsequent solve will also be faster when \(A\) is non-transposed and \(B\) is transposed (or conjugate transposed). For example, instead of solving:\[\begin{split} \begin{bmatrix} a_{00} & 0 & 0 \\ a_{10} & a_{11} & 0 \\ a_{20} & a_{21} & a_{22} \\ \end{bmatrix} \cdot \begin{bmatrix} x_{00} & x_{01} \\ x_{10} & x_{11} \\ x_{20} & x_{21} \\ \end{bmatrix} = \begin{bmatrix} b_{00} & b_{01} \\ b_{10} & b_{11} \\ b_{20} & b_{21} \\ \end{bmatrix} \end{split}\]Consider solving:

\[\begin{split} \begin{bmatrix} a_{00} & 0 & 0 \\ a_{10} & a_{11} & 0 \\ a_{20} & a_{21} & a_{22} \end{bmatrix} \cdot \begin{bmatrix} x_{00} & x_{10} & x_{20} \\ x_{01} & x_{11} & x_{21} \end{bmatrix}^{T} = \begin{bmatrix} b_{00} & b_{10} & b_{20} \\ b_{01} & b_{11} & b_{21} \end{bmatrix}^{T} \end{split}\]Once the temporary storage buffer has been allocated, analysis meta data is required. It can be obtained by

[rocsparse_Xcsrsm_analysis()](#rocsparse__csrsm_8h_1ac8e943e992641859efdfea49a267133b).Solving a triangular system involves division by the diagonal elements. This means that if the sparse matrix is missing the diagonal entry (referred to as a structural zero) or the diagonal entry is zero (referred to as a numerical zero) then a division by zero would occur.

`rocsparse_csrsm_solve`

tracks the location of the first zero pivot (either numerical or structural zero). The zero pivot status can be checked calling[rocsparse_csrsm_zero_pivot()](#rocsparse__csrsm_8h_1a8d4ac10da1f6af5e32894bc57a736058). If[rocsparse_csrsm_zero_pivot()](#rocsparse__csrsm_8h_1a8d4ac10da1f6af5e32894bc57a736058)returns[rocsparse_status_success](enumerations.html#rocsparse-types_8h_1a578f8c5c1b08f358bf4605b0031006a8a96462a9361cfceb6cf9354e10fdc671b), then no zero pivot was found and therefore the matrix does not have a structural or numerical zero.The user can specify that the sparse matrix should be interpreted as having ones on the diagonal by setting the diagonal type on the descriptor

`descr`

to[rocsparse_diag_type_unit](enumerations.html#rocsparse-types_8h_1a6e8e038adcd3fa03168a1cb4a7da1bc5ac14545fb3bf8773d5f6b8e258c9576f4)using[rocsparse_set_mat_diag_type](auxiliary.html#rocsparse-auxiliary_8h_1a61f894d80e4da74c7e8cd43f61f9215c). If[rocsparse_diag_type](enumerations.html#rocsparse-types_8h_1a6e8e038adcd3fa03168a1cb4a7da1bc5)==[rocsparse_diag_type_unit](enumerations.html#rocsparse-types_8h_1a6e8e038adcd3fa03168a1cb4a7da1bc5ac14545fb3bf8773d5f6b8e258c9576f4), no zero pivot will be reported, even if \(A_{j,j} = 0\) for some \(j\).The sparse CSR matrix passed to

`rocsparse_csrsm_solve`

does not actually have to be a triangular matrix. Instead the triangular upper or lower part of the sparse matrix is solved based on[rocsparse_fill_mode](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1)set on the descriptor`descr`

. If the fill mode is set to[rocsparse_fill_mode_lower](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a1eb644f6f2701329635e07d91919d37e), then the lower triangular matrix is solved. If the fill mode is set to[rocsparse_fill_mode_upper](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a905f490c7fc5a59e8a635938cec0d004)then the upper triangular matrix is solved.**Example**Consider the lower triangular \(m \times m\) matrix \(L\), stored in CSR storage format with unit diagonal. The following example solves \(L \cdot X = B\).

int main() { // 1 2 0 3 0 // A = 0 4 5 0 0 // 6 0 0 7 8 rocsparse_int m = 3; rocsparse_int k = 5; rocsparse_int nnz = 8; // alpha and beta float alpha = 1.0f; float beta = 0.0f; std::vector<int> hcsr_row_ptr = {0, 3, 5, 8}; std::vector<int> hcsr_col_ind = {0, 1, 3, 1, 2, 0, 3, 4}; std::vector<float> hcsr_val = {1, 2, 3, 4, 5, 6, 7, 8}; // Set dimension n of B rocsparse_int n = 64; // Allocate and generate column-oriented dense matrix B std::vector<float> hB(k * n); for(rocsparse_int i = 0; i < k * n; ++i) { hB[i] = static_cast<float>(rand()) / static_cast<float>(RAND_MAX); } std::vector<float> hC(m * n); int* dcsr_row_ptr; int* dcsr_col_ind; float* dcsr_val; float* dB; float* dC; HIP_CHECK(hipMalloc(&dcsr_row_ptr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc(&dcsr_col_ind, sizeof(int) * nnz)); HIP_CHECK(hipMalloc(&dcsr_val, sizeof(float) * nnz)); HIP_CHECK(hipMalloc(&dB, sizeof(float) * k * n)); HIP_CHECK(hipMalloc(&dC, sizeof(float) * m * n)); HIP_CHECK( hipMemcpy(dcsr_row_ptr, hcsr_row_ptr.data(), sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsr_col_ind, hcsr_col_ind.data(), sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsr_val, hcsr_val.data(), sizeof(float) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dB, hB.data(), sizeof(float) * k * n, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dC, hC.data(), sizeof(float) * m * n, hipMemcpyHostToDevice)); // Create rocSPARSE handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Create matrix descriptor rocsparse_mat_descr descr; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr)); // Perform the matrix multiplication ROCSPARSE_CHECK(rocsparse_scsrmm(handle, rocsparse_operation_none, rocsparse_operation_none, m, n, k, nnz, &alpha, descr, dcsr_val, dcsr_row_ptr, dcsr_col_ind, dB, k, &beta, dC, m)); HIP_CHECK(hipMemcpy(hC.data(), dC, sizeof(float) * m * n, hipMemcpyDeviceToHost)); std::cout << "hC" << std::endl; for(size_t i = 0; i < hC.size(); i++) { std::cout << hC[i] << " "; } std::cout << "" << std::endl; // Clean up ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); // Clear up on device HIP_CHECK(hipFree(dcsr_row_ptr)); HIP_CHECK(hipFree(dcsr_col_ind)); HIP_CHECK(hipFree(dcsr_val)); HIP_CHECK(hipFree(dB)); HIP_CHECK(hipFree(dC)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

Currently, only

`trans_A`

!=[rocsparse_operation_conjugate_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a6920c1aa5f80005eee4b66ea6f25330f)and`trans_B`

!=[rocsparse_operation_conjugate_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a6920c1aa5f80005eee4b66ea6f25330f)is supported.Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**trans_A**–**[in]**matrix A operation type.**trans_B**–**[in]**matrix B operation type.**m**–**[in]**number of rows of the sparse CSR matrix A.**nrhs**–**[in]**number of columns of the column-oriented dense matrix op(B).**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix A.**alpha**–**[in]**scalar \(\alpha\).**descr**–**[in]**descriptor of the sparse CSR matrix A.**csr_val**–**[in]**array of`nnz`

elements of the sparse CSR matrix A.**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix A.**csr_col_ind**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix A.**B**–**[inout]**column-oriented dense matrix of dimension`m`

\(\times\)`nrhs`

elements of the rhs matrix B.**ldb**–**[in]**leading dimension of rhs matrix B.**info**–**[in]**structure that holds the information collected during the analysis step.**policy**–**[in]**[rocsparse_solve_policy_auto](enumerations.html#rocsparse-types_8h_1a5a3e261123e81a9e8b267c6109e26957a9c6bdf97e192d429ca536d5ab98ea866).**temp_buffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`nrhs`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`alpha`

,`descr`

,`csr_val`

,`csr_row_ptr`

,`csr_col_ind`

,`B`

,`info`

or`temp_buffer`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_not_implemented**–`trans_A`

==[rocsparse_operation_conjugate_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a6920c1aa5f80005eee4b66ea6f25330f),`trans_B`

==[rocsparse_operation_conjugate_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a6920c1aa5f80005eee4b66ea6f25330f)or[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_csrsm_clear()[#](#rocsparse-csrsm-clear)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_csrsm_clear([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info)[#](#_CPPv421rocsparse_csrsm_clear16rocsparse_handle18rocsparse_mat_info) `rocsparse_csrsm_clear`

deallocates all memory that was allocated by[rocsparse_Xcsrsm_analysis()](#rocsparse__csrsm_8h_1ac8e943e992641859efdfea49a267133b). This is especially useful, if memory is an issue and the analysis data is not required for further computation, e.g. when switching to another sparse matrix format. Calling`rocsparse_csrsm_clear`

is optional. All allocated resources will be cleared when the opaque[rocsparse_mat_info](types.html#rocsparse-types_8h_1a3347be72f6e4f3c55318c32b46dcaa92)struct is destroyed using[rocsparse_destroy_mat_info()](auxiliary.html#rocsparse-auxiliary_8h_1a9c143f65076a10ebafcffc633ad5d87b).Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**info**–**[inout]**structure that holds the information collected during the analysis step.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`info`

pointer is invalid.**rocsparse_status_memory_error**– the buffer holding the meta data could not be deallocated.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_bsrsm_zero_pivot()[#](#rocsparse-bsrsm-zero-pivot)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_bsrsm_zero_pivot([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_int](types.html#_CPPv413rocsparse_int)*position)[#](#_CPPv426rocsparse_bsrsm_zero_pivot16rocsparse_handle18rocsparse_mat_infoP13rocsparse_int) `rocsparse_bsrsm_zero_pivot`

returns[rocsparse_status_zero_pivot](enumerations.html#rocsparse-types_8h_1a578f8c5c1b08f358bf4605b0031006a8a01fe264830c8ce6451ce6888bc8d3e80), if either a structural or numerical zero has been found during[rocsparse_Xbsrsm_solve()](#rocsparse__bsrsm_8h_1a632a2440f04fcfb49ed1e0ebcaee1390)computation. The first zero pivot \(j\) at \(A_{j,j}\) is stored in`position`

, using same index base as the BSR matrix.`position`

can be in host or device memory. If no zero pivot has been found,`position`

is set to -1 and[rocsparse_status_success](enumerations.html#rocsparse-types_8h_1a578f8c5c1b08f358bf4605b0031006a8a96462a9361cfceb6cf9354e10fdc671b)is returned instead.Note

`rocsparse_bsrsm_zero_pivot`

is a blocking function. It might influence performance negatively.Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**info**–**[in]**structure that holds the information collected during the analysis step.**position**–**[inout]**pointer to zero pivot \(j\), can be in host or device memory.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`info`

or`position`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_zero_pivot**– zero pivot has been found.



## rocsparse_bsrsm_buffer_size()[#](#rocsparse-bsrsm-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sbsrsm_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_X,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nrhs,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, size_t *buffer_size)[#](#_CPPv428rocsparse_sbsrsm_buffer_size16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_infoP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dbsrsm_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_X,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nrhs,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, size_t *buffer_size)[#](#_CPPv428rocsparse_dbsrsm_buffer_size16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_infoP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cbsrsm_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_X,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nrhs,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, size_t *buffer_size)[#](#_CPPv428rocsparse_cbsrsm_buffer_size16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_infoP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zbsrsm_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_X,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nrhs,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, size_t *buffer_size)[#](#_CPPv428rocsparse_zbsrsm_buffer_size16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_infoP6size_t) `rocsparse_bsrsm_buffer_size`

returns the size of the temporary storage buffer that is required by[rocsparse_Xbsrsm_analysis()](#rocsparse__bsrsm_8h_1aa7c3da4c56f9dcf7aaae3e65dd35110f)and[rocsparse_Xbsrsm_solve()](#rocsparse__bsrsm_8h_1a632a2440f04fcfb49ed1e0ebcaee1390). The temporary storage buffer must be allocated by the user.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dir**–**[in]**matrix storage of BSR blocks.**trans_A**–**[in]**matrix A operation type.**trans_X**–**[in]**matrix X operation type.**mb**–**[in]**number of block rows of the sparse BSR matrix A.**nrhs**–**[in]**number of columns of the column-oriented dense matrix op(X).**nnzb**–**[in]**number of non-zero blocks of the sparse BSR matrix A.**descr**–**[in]**descriptor of the sparse BSR matrix A.**bsr_val**–**[in]**array of`nnzb`

blocks of the sparse BSR matrix.**bsr_row_ptr**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix.**bsr_col_ind**–**[in]**array of`nnzb`

containing the block column indices of the sparse BSR matrix.**block_dim**–**[in]**block dimension of the sparse BSR matrix.**info**–**[in]**structure that holds the information collected during the analysis step.**buffer_size**–**[out]**number of bytes of the temporary storage buffer required by[rocsparse_Xbsrsm_analysis()](#rocsparse__bsrsm_8h_1aa7c3da4c56f9dcf7aaae3e65dd35110f)and[rocsparse_Xbsrsm_solve()](#rocsparse__bsrsm_8h_1a632a2440f04fcfb49ed1e0ebcaee1390).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`mb`

,`nrhs`

,`nnzb`

or`block_dim`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`bsr_val`

,`bsr_row_ptr`

,`bsr_col_ind`

,`info`

or`buffer_size`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_not_implemented**–`trans_A`

==[rocsparse_operation_conjugate_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a6920c1aa5f80005eee4b66ea6f25330f),`trans_X`

==[rocsparse_operation_conjugate_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a6920c1aa5f80005eee4b66ea6f25330f)or[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_bsrsm_analysis()[#](#rocsparse-bsrsm-analysis)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sbsrsm_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_X,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nrhs,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_analysis_policy](enumerations.html#_CPPv425rocsparse_analysis_policy)analysis,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)solve, void *temp_buffer)[#](#_CPPv425rocsparse_sbsrsm_analysis16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dbsrsm_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_X,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nrhs,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_analysis_policy](enumerations.html#_CPPv425rocsparse_analysis_policy)analysis,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)solve, void *temp_buffer)[#](#_CPPv425rocsparse_dbsrsm_analysis16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cbsrsm_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_X,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nrhs,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_analysis_policy](enumerations.html#_CPPv425rocsparse_analysis_policy)analysis,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)solve, void *temp_buffer)[#](#_CPPv425rocsparse_cbsrsm_analysis16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zbsrsm_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_X,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nrhs,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_analysis_policy](enumerations.html#_CPPv425rocsparse_analysis_policy)analysis,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)solve, void *temp_buffer)[#](#_CPPv425rocsparse_zbsrsm_analysis16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv) `rocsparse_bsrsm_analysis`

performs the analysis step for[rocsparse_Xbsrsm_solve()](#rocsparse__bsrsm_8h_1a632a2440f04fcfb49ed1e0ebcaee1390). It is expected that this function will be executed only once for a given matrix and particular operation type. The analysis meta data can be cleared by[rocsparse_bsrsm_clear()](#rocsparse__bsrsm_8h_1ad34a5b834ac7ab76b657b1104fa6dc9c).`rocsparse_bsrsm_analysis`

can share its meta data with[rocsparse_Xbsrilu0_analysis()](precond.html#rocsparse__bsrilu0_8h_1ac20c3e0a79507660dea8895f4111f170),[rocsparse_Xbsric0_analysis()](precond.html#rocsparse__bsric0_8h_1a9cfb58036bb689f2becba8c0baa9d716),[rocsparse_Xbsrsv_analysis()](level2.html#rocsparse__bsrsv_8h_1aade89276269f88cd50e357c0a3504c87). Selecting[rocsparse_analysis_policy_reuse](enumerations.html#rocsparse-types_8h_1a43b20aa4bb19623a91b5952422fbe35ca658466413f4005c0c103d20d5e352078)policy can greatly improve computation performance of meta data. However, the user needs to make sure that the sparsity pattern remains unchanged. If this cannot be assured,[rocsparse_analysis_policy_force](enumerations.html#rocsparse-types_8h_1a43b20aa4bb19623a91b5952422fbe35cac66b70c4f519ddd03dcbe0f3a973401a)has to be used.Note

If the matrix sparsity pattern changes, the gathered information will become invalid.

Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dir**–**[in]**matrix storage of BSR blocks.**trans_A**–**[in]**matrix A operation type.**trans_X**–**[in]**matrix X operation type.**mb**–**[in]**number of block rows of the sparse BSR matrix A.**nrhs**–**[in]**number of columns of the column-oriented dense matrix op(X).**nnzb**–**[in]**number of non-zero blocks of the sparse BSR matrix A.**descr**–**[in]**descriptor of the sparse BSR matrix A.**bsr_val**–**[in]**array of`nnzb`

blocks of the sparse BSR matrix A.**bsr_row_ptr**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix A.**bsr_col_ind**–**[in]**array of`nnzb`

containing the block column indices of the sparse BSR matrix A.**block_dim**–**[in]**block dimension of the sparse BSR matrix A.**info**–**[out]**structure that holds the information collected during the analysis step.**analysis**–**[in]**[rocsparse_analysis_policy_reuse](enumerations.html#rocsparse-types_8h_1a43b20aa4bb19623a91b5952422fbe35ca658466413f4005c0c103d20d5e352078)or[rocsparse_analysis_policy_force](enumerations.html#rocsparse-types_8h_1a43b20aa4bb19623a91b5952422fbe35cac66b70c4f519ddd03dcbe0f3a973401a).**solve**–**[in]**[rocsparse_solve_policy_auto](enumerations.html#rocsparse-types_8h_1a5a3e261123e81a9e8b267c6109e26957a9c6bdf97e192d429ca536d5ab98ea866).**temp_buffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`mb`

,`nrhs`

,`nnzb`

or`block_dim`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`bsr_val`

,`bsr_row_ptr`

,`bsr_col_ind`

,`info`

or`temp_buffer`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_not_implemented**–`trans_A`

==[rocsparse_operation_conjugate_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a6920c1aa5f80005eee4b66ea6f25330f),`trans_X`

==[rocsparse_operation_conjugate_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a6920c1aa5f80005eee4b66ea6f25330f)or[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_bsrsm_solve()[#](#rocsparse-bsrsm-solve)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sbsrsm_solve([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_X,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nrhs,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const float *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, const float *B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb, float *X,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldx,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv422rocsparse_sbsrsm_solve16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_infoPKf13rocsparse_intPf13rocsparse_int22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dbsrsm_solve([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_X,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nrhs,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const double *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, const double *B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb, double *X,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldx,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv422rocsparse_dbsrsm_solve16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKdK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_infoPKd13rocsparse_intPd13rocsparse_int22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cbsrsm_solve([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_X,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nrhs,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*X,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldx,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv422rocsparse_cbsrsm_solve16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPK23rocsparse_float_complexK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_infoPK23rocsparse_float_complex13rocsparse_intP23rocsparse_float_complex13rocsparse_int22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zbsrsm_solve([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_X,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nrhs,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*X,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldx,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv422rocsparse_zbsrsm_solve16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPK24rocsparse_double_complexK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_infoPK24rocsparse_double_complex13rocsparse_intP24rocsparse_double_complex13rocsparse_int22rocsparse_solve_policyPv) Sparse triangular system solve using BSR storage format.

`rocsparse_bsrsm_solve`

solves a sparse triangular linear system of a sparse \(m \times m\) matrix, defined in BSR storage format, a column-oriented dense solution matrix \(X\) and the column-oriented dense right-hand side matrix \(B\) that is multiplied by \(\alpha\), such that\[ op(A) \cdot op(X) = \alpha \cdot op(B), \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if trans_A == rocsparse_operation_none} \\ A^T, & \text{if trans_A == rocsparse_operation_transpose} \\ A^H, & \text{if trans_A == rocsparse_operation_conjugate_transpose} \end{array} \right. \end{split}\],\[\begin{split} op(B) = \left\{ \begin{array}{ll} B, & \text{if trans_X == rocsparse_operation_none} \\ B^T, & \text{if trans_X == rocsparse_operation_transpose} \\ B^H, & \text{if trans_X == rocsparse_operation_conjugate_transpose} \end{array} \right. \end{split}\]and\[\begin{split} op(X) = \left\{ \begin{array}{ll} X, & \text{if trans_X == rocsparse_operation_none} \\ X^T, & \text{if trans_X == rocsparse_operation_transpose} \\ X^H, & \text{if trans_X == rocsparse_operation_conjugate_transpose} \end{array} \right. \end{split}\]and where \(m = block\_dim \times mb\).Note that as indicated above, the operation type of both \(op(B)\) and \(op(X)\) is specified by the

`trans_X`

parameter and that the operation type of B and X must match. For example, if \(op(B)=B\) then \(op(X)=X\). Likewise, if \(op(B)=B^T\) then \(op(X)=X^T\).Given that the sparse matrix A is a square matrix, its size is \(m \times m\) regardless of whether A is transposed or not. The size of the column-oriented dense matrices B and X have size that depends on the value of

`trans_X:`

\[\begin{split} op(B) = \left\{ \begin{array}{ll} ldb \times nrhs, \text{ } ldb \ge m, & \text{if trans_X == rocsparse_operation_none} \\ ldb \times m, \text{ } ldb \ge nrhs, & \text{if trans_X == rocsparse_operation_transpose} \\ ldb \times m, \text{ } ldb \ge nrhs, & \text{if trans_X == rocsparse_operation_conjugate_transpose} \end{array} \right. \end{split}\]and\[\begin{split} op(X) = \left\{ \begin{array}{ll} ldb \times nrhs, \text{ } ldb \ge m, & \text{if trans_X == rocsparse_operation_none} \\ ldb \times m, \text{ } ldb \ge nrhs, & \text{if trans_X == rocsparse_operation_transpose} \\ ldb \times m, \text{ } ldb \ge nrhs, & \text{if trans_X == rocsparse_operation_conjugate_transpose} \end{array} \right. \end{split}\]`rocsparse_bsrsm_solve`

requires a user allocated temporary buffer. Its size is returned by[rocsparse_Xbsrsm_buffer_size()](#rocsparse__bsrsm_8h_1ac0468f507d5f0e26bcb6314f1fd35ff2). The size of the required buffer is larger when`trans_A`

equals[rocsparse_operation_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a1ea3194d0c7bdb9e500d6faeead8ebf5)or[rocsparse_operation_conjugate_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a6920c1aa5f80005eee4b66ea6f25330f)and when`trans_X`

is[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528). The subsequent solve will also be faster when \(A\) is non-transposed and \(B\) is transposed (or conjugate transposed). For example, instead of solving:\[\begin{split} \left[ \begin{array}{c | c} \begin{array}{c c} a_{00} & a_{01} \\ a_{10} & a_{11} \end{array} & \begin{array}{c c} 0 & 0 \\ 0 & 0 \end{array} \\ \hline \begin{array}{c c} a_{20} & a_{21} \\ a_{30} & a_{31} \end{array} & \begin{array}{c c} a_{22} & a_{23} \\ a_{32} & a_{33} \end{array} \\ \end{array} \right] \cdot \begin{bmatrix} x_{00} & x_{01} \\ x_{10} & x_{11} \\ x_{20} & x_{21} \\ x_{30} & x_{31} \\ \end{bmatrix} = \begin{bmatrix} b_{00} & b_{01} \\ b_{10} & b_{11} \\ b_{20} & b_{21} \\ b_{30} & b_{31} \\ \end{bmatrix} \end{split}\]Consider solving:

\[\begin{split} \left[ \begin{array}{c | c} \begin{array}{c c} a_{00} & a_{01} \\ a_{10} & a_{11} \end{array} & \begin{array}{c c} 0 & 0 \\ 0 & 0 \end{array} \\ \hline \begin{array}{c c} a_{20} & a_{21} \\ a_{30} & a_{31} \end{array} & \begin{array}{c c} a_{22} & a_{23} \\ a_{32} & a_{33} \end{array} \\ \end{array} \right] \cdot \begin{bmatrix} x_{00} & x_{10} & x_{20} & x_{30} \\ x_{01} & x_{11} & x_{21} & x_{31} \end{bmatrix}^{T} = \begin{bmatrix} b_{00} & b_{10} & b_{20} & b_{30} \\ b_{01} & b_{11} & b_{21} & b_{31} \end{bmatrix}^{T} \end{split}\]Once the temporary storage buffer has been allocated, analysis meta data is required. It can be obtained by rocsparse_sbsrsm_analysis “rocsparse_Xbsrsm_analysis()”.

Solving a triangular system involves inverting the diagonal blocks. This means that if the sparse matrix is missing the diagonal block (referred to as a structural zero) or the diagonal block is not invertible (referred to as a numerical zero) then a solution is not possible.

`rocsparse_bsrsm_solve`

tracks the location of the first zero pivot (either numerical or structural zero). The zero pivot status can be checked calling[rocsparse_bsrsm_zero_pivot()](#rocsparse__bsrsm_8h_1ad434081ea9ce56bc0ffa44c3f6666769). If[rocsparse_bsrsm_zero_pivot()](#rocsparse__bsrsm_8h_1ad434081ea9ce56bc0ffa44c3f6666769)returns[rocsparse_status_success](enumerations.html#rocsparse-types_8h_1a578f8c5c1b08f358bf4605b0031006a8a96462a9361cfceb6cf9354e10fdc671b), then no zero pivot was found and therefore the matrix does not have a structural or numerical zero.The user can specify that the sparse matrix should be interpreted as having identity blocks on the diagonal by setting the diagonal type on the descriptor

`descr`

to[rocsparse_diag_type_unit](enumerations.html#rocsparse-types_8h_1a6e8e038adcd3fa03168a1cb4a7da1bc5ac14545fb3bf8773d5f6b8e258c9576f4)using[rocsparse_set_mat_diag_type](auxiliary.html#rocsparse-auxiliary_8h_1a61f894d80e4da74c7e8cd43f61f9215c). If[rocsparse_diag_type](enumerations.html#rocsparse-types_8h_1a6e8e038adcd3fa03168a1cb4a7da1bc5)==[rocsparse_diag_type_unit](enumerations.html#rocsparse-types_8h_1a6e8e038adcd3fa03168a1cb4a7da1bc5ac14545fb3bf8773d5f6b8e258c9576f4), no zero pivot will be reported, even if the diagonal block \(A_{j,j}\) for some \(j\) is not invertible.The sparse CSR matrix passed to

`rocsparse_bsrsm_solve`

does not actually have to be a triangular matrix. Instead the triangular upper or lower part of the sparse matrix is solved based on[rocsparse_fill_mode](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1)set on the descriptor`descr`

. If the fill mode is set to[rocsparse_fill_mode_lower](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a1eb644f6f2701329635e07d91919d37e), then the lower triangular matrix is solved. If the fill mode is set to[rocsparse_fill_mode_upper](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a905f490c7fc5a59e8a635938cec0d004)then the upper triangular matrix is solved.**Example**Consider the lower triangular \(m \times m\) matrix \(L\), stored in BSR storage format with non-unit diagonal. The following example solves \(L \cdot X = B\).

int main() { // rocSPARSE handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // A = ( 1.0 0.0 0.0 0.0 ) // ( 2.0 3.0 0.0 0.0 ) // ( 4.0 5.0 6.0 0.0 ) // ( 7.0 0.0 8.0 9.0 ) // // with bsr_dim = 2 // // ------------------- // = | 1.0 0.0 | 0.0 0.0 | // | 2.0 3.0 | 0.0 0.0 | // ------------------- // | 4.0 5.0 | 6.0 0.0 | // | 7.0 0.0 | 8.0 9.0 | // ------------------- // Number of rows and columns rocsparse_int m = 4; // Number of block rows and block columns rocsparse_int mb = 2; rocsparse_int nb = 2; // BSR block dimension rocsparse_int bsr_dim = 2; // Number of right-hand-sides rocsparse_int nrhs = 4; // Number of non-zero blocks rocsparse_int nnzb = 3; // BSR row pointers rocsparse_int hbsr_row_ptr[3] = {0, 1, 3}; // BSR column indices rocsparse_int hbsr_col_ind[3] = {0, 0, 1}; // BSR values double hbsr_val[12] = {1.0, 2.0, 0.0, 3.0, 4.0, 7.0, 5.0, 0.0, 6.0, 8.0, 0.0, 9.0}; // Storage scheme of the BSR blocks rocsparse_direction dir = rocsparse_direction_column; // Transposition of the matrix and rhs matrix rocsparse_operation transA = rocsparse_operation_none; rocsparse_operation transX = rocsparse_operation_none; // Analysis policy rocsparse_analysis_policy analysis_policy = rocsparse_analysis_policy_reuse; // Solve policy rocsparse_solve_policy solve_policy = rocsparse_solve_policy_auto; // Scalar alpha and beta double alpha = 3.7; // rhs and solution matrix rocsparse_int ldb = nb * bsr_dim; rocsparse_int ldx = mb * bsr_dim; double hB[16] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}; double hX[16]; // Offload data to device rocsparse_int* dbsr_row_ptr; rocsparse_int* dbsr_col_ind; double* dbsr_val; double* dB; double* dX; HIP_CHECK(hipMalloc(&dbsr_row_ptr, sizeof(rocsparse_int) * (mb + 1))); HIP_CHECK(hipMalloc(&dbsr_col_ind, sizeof(rocsparse_int) * nnzb)); HIP_CHECK(hipMalloc(&dbsr_val, sizeof(double) * nnzb * bsr_dim * bsr_dim)); HIP_CHECK(hipMalloc(&dB, sizeof(double) * nb * bsr_dim * nrhs)); HIP_CHECK(hipMalloc(&dX, sizeof(double) * mb * bsr_dim * nrhs)); HIP_CHECK(hipMemcpy( dbsr_row_ptr, hbsr_row_ptr, sizeof(rocsparse_int) * (mb + 1), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dbsr_col_ind, hbsr_col_ind, sizeof(rocsparse_int) * nnzb, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( dbsr_val, hbsr_val, sizeof(double) * nnzb * bsr_dim * bsr_dim, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dB, hB, sizeof(double) * nb * bsr_dim * nrhs, hipMemcpyHostToDevice)); // Matrix descriptor rocsparse_mat_descr descr; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr)); // Matrix fill mode ROCSPARSE_CHECK(rocsparse_set_mat_fill_mode(descr, rocsparse_fill_mode_lower)); // Matrix diagonal type ROCSPARSE_CHECK(rocsparse_set_mat_diag_type(descr, rocsparse_diag_type_non_unit)); // Matrix info structure rocsparse_mat_info info; ROCSPARSE_CHECK(rocsparse_create_mat_info(&info)); // Obtain required buffer size size_t buffer_size; ROCSPARSE_CHECK(rocsparse_dbsrsm_buffer_size(handle, dir, transA, transX, mb, nrhs, nnzb, descr, dbsr_val, dbsr_row_ptr, dbsr_col_ind, bsr_dim, info, &buffer_size)); // Allocate temporary buffer void* temp_buffer; HIP_CHECK(hipMalloc(&temp_buffer, buffer_size)); // Perform analysis step ROCSPARSE_CHECK(rocsparse_dbsrsm_analysis(handle, dir, transA, transX, mb, nrhs, nnzb, descr, dbsr_val, dbsr_row_ptr, dbsr_col_ind, bsr_dim, info, analysis_policy, solve_policy, temp_buffer)); // Call dbsrsm to perform lower triangular solve LX = B ROCSPARSE_CHECK(rocsparse_dbsrsm_solve(handle, dir, transA, transX, mb, nrhs, nnzb, &alpha, descr, dbsr_val, dbsr_row_ptr, dbsr_col_ind, bsr_dim, info, dB, ldb, dX, ldx, solve_policy, temp_buffer)); // Check for zero pivots rocsparse_int pivot; rocsparse_status status = rocsparse_bsrsm_zero_pivot(handle, info, &pivot); if(status == rocsparse_status_zero_pivot) { std::cout << "Found zero pivot in matrix row " << pivot << std::endl; } // Copy result back to host HIP_CHECK(hipMemcpy(hX, dX, sizeof(double) * mb * bsr_dim * nrhs, hipMemcpyDeviceToHost)); std::cout << "hX" << std::endl; for(rocsparse_int i = 0; i < mb * bsr_dim * nrhs; i++) { std::cout << hX[i] << " "; } std::cout << "" << std::endl; // Clear rocSPARSE ROCSPARSE_CHECK(rocsparse_destroy_mat_info(info)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); // Clear device memory HIP_CHECK(hipFree(dbsr_row_ptr)); HIP_CHECK(hipFree(dbsr_col_ind)); HIP_CHECK(hipFree(dbsr_val)); HIP_CHECK(hipFree(dB)); HIP_CHECK(hipFree(dX)); HIP_CHECK(hipFree(temp_buffer)); return 0; }


Note

The sparse BSR matrix has to be sorted.

Note

Operation type of B and X must match, for example if \(op(B)=B\) then \(op(X)=X\).

Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

Currently, only

`trans_A`

!=[rocsparse_operation_conjugate_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a6920c1aa5f80005eee4b66ea6f25330f)and`trans_X`

!=[rocsparse_operation_conjugate_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a6920c1aa5f80005eee4b66ea6f25330f)is supported.Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dir**–**[in]**matrix storage of BSR blocks.**trans_A**–**[in]**matrix A operation type.**trans_X**–**[in]**matrix X operation type.**mb**–**[in]**number of block rows of the sparse BSR matrix A.**nrhs**–**[in]**number of columns of the column-oriented dense matrix op(X).**nnzb**–**[in]**number of non-zero blocks of the sparse BSR matrix A.**alpha**–**[in]**scalar \(\alpha\).**descr**–**[in]**descriptor of the sparse BSR matrix A.**bsr_val**–**[in]**array of`nnzb`

blocks of the sparse BSR matrix.**bsr_row_ptr**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix.**bsr_col_ind**–**[in]**array of`nnzb`

containing the block column indices of the sparse BSR matrix.**block_dim**–**[in]**block dimension of the sparse BSR matrix.**info**–**[in]**structure that holds the information collected during the analysis step.**B**–**[in]**column-oriented dense matrix B with leading dimension`ldb`

.**ldb**–**[in]**leading dimension of rhs matrix B.**X**–**[out]**column-oriented dense solution matrix X with leading dimension`ldx`

.**ldx**–**[in]**leading dimension of solution matrix X.**policy**–**[in]**[rocsparse_solve_policy_auto](enumerations.html#rocsparse-types_8h_1a5a3e261123e81a9e8b267c6109e26957a9c6bdf97e192d429ca536d5ab98ea866).**temp_buffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`mb`

,`nrhs`

,`nnzb`

or`block_dim`

is invalid.**rocsparse_status_invalid_pointer**–`alpha`

,`descr`

,`bsr_val`

,`bsr_row_ptr`

,`bsr_col_ind`

,`B`

,`X`

`info`

or`temp_buffer`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_not_implemented**–`trans_A`

==[rocsparse_operation_conjugate_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a6920c1aa5f80005eee4b66ea6f25330f),`trans_X`

==[rocsparse_operation_conjugate_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a6920c1aa5f80005eee4b66ea6f25330f)or[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_bsrsm_clear()[#](#rocsparse-bsrsm-clear)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_bsrsm_clear([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info)[#](#_CPPv421rocsparse_bsrsm_clear16rocsparse_handle18rocsparse_mat_info) `rocsparse_bsrsm_clear`

deallocates all memory that was allocated by[rocsparse_Xbsrsm_analysis()](#rocsparse__bsrsm_8h_1aa7c3da4c56f9dcf7aaae3e65dd35110f). This is especially useful, if memory is an issue and the analysis data is not required for further computation, e.g. when switching to another sparse matrix format. Calling`rocsparse_bsrsm_clear`

is optional. All allocated resources will be cleared when the opaque[rocsparse_mat_info](types.html#rocsparse-types_8h_1a3347be72f6e4f3c55318c32b46dcaa92)struct is destroyed using[rocsparse_destroy_mat_info()](auxiliary.html#rocsparse-auxiliary_8h_1a9c143f65076a10ebafcffc633ad5d87b).Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**info**–**[inout]**structure that holds the information collected during the analysis step.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`info`

pointer is invalid.**rocsparse_status_memory_error**– the buffer holding the meta data could not be deallocated.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_gemmi()[#](#rocsparse-gemmi)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sgemmi([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)k,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const float *alpha, const float *A,[rocsparse_int](types.html#_CPPv413rocsparse_int)lda, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, const float *beta, float *C,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldc)[#](#_CPPv416rocsparse_sgemmi16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPKfPKf13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intPKfPf13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dgemmi([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)k,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const double *alpha, const double *A,[rocsparse_int](types.html#_CPPv413rocsparse_int)lda, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, const double *beta, double *C,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldc)[#](#_CPPv416rocsparse_dgemmi16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPKdPKd13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_intPKdPd13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cgemmi([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)k,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*alpha, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*A,[rocsparse_int](types.html#_CPPv413rocsparse_int)lda, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*beta,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*C,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldc)[#](#_CPPv416rocsparse_cgemmi16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPK23rocsparse_float_complexPK23rocsparse_float_complex13rocsparse_intK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_intPK23rocsparse_float_complexP23rocsparse_float_complex13rocsparse_int)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zgemmi([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_A,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans_B,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)k,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*alpha, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*A,[rocsparse_int](types.html#_CPPv413rocsparse_int)lda, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*beta,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*C,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldc)[#](#_CPPv416rocsparse_zgemmi16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPK24rocsparse_double_complexPK24rocsparse_double_complex13rocsparse_intK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_intPK24rocsparse_double_complexP24rocsparse_double_complex13rocsparse_int) Dense matrix sparse matrix multiplication using CSR storage format.

`rocsparse_gemmi`

multiplies the scalar \(\alpha\) with a column-oriented dense \(m \times k\) matrix \(op(A)\) and the sparse \(k \times n\) matrix \(op(B)\), defined in CSR storage format and adds the result to the column-oriented dense \(m \times n\) matrix \(C\) that is multiplied by the scalar \(\beta\), such that\[ C := \alpha \cdot op(A) \cdot op(B) + \beta \cdot C \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if trans_A == rocsparse_operation_none} \\ A^T, & \text{if trans_A == rocsparse_operation_transpose} \\ A^H, & \text{if trans_A == rocsparse_operation_conjugate_transpose} \end{array} \right. \end{split}\]and\[\begin{split} op(B) = \left\{ \begin{array}{ll} B, & \text{if trans_B == rocsparse_operation_none} \\ B^T, & \text{if trans_B == rocsparse_operation_transpose} \\ B^H, & \text{if trans_B == rocsparse_operation_conjugate_transpose} \end{array} \right. \end{split}\]**Example**This example multiplies a column-oriented dense matrix with a CSC matrix.

int main() { rocsparse_int m = 2; rocsparse_int n = 5; rocsparse_int k = 3; rocsparse_int nnz = 8; rocsparse_int lda = m; rocsparse_int ldc = m; // alpha and beta float alpha = 1.0f; float beta = 0.0f; // Matrix A (m x k) // ( 9.0 10.0 11.0 ) // ( 12.0 13.0 14.0 ) // Matrix B (k x n) // ( 1.0 2.0 0.0 3.0 0.0 ) // ( 0.0 4.0 5.0 0.0 0.0 ) // ( 6.0 0.0 0.0 7.0 8.0 ) // Matrix C (m x n) // ( 15.0 16.0 17.0 18.0 19.0 ) // ( 20.0 21.0 22.0 23.0 24.0 ) std::vector<float> hA = {9.0, 12.0, 10.0, 13.0, 11.0, 14.0}; std::vector<int> hcsc_col_ptr_B = {0, 2, 4, 5, 7, 8}; std::vector<int> hcsc_row_ind_B = {0, 2, 0, 1, 1, 0, 2, 2}; std::vector<float> hcsc_val_B = {1.0, 6.0, 2.0, 4.0, 5.0, 3.0, 7.0, 8.0}; std::vector<float> hC = {15.0, 20.0, 16.0, 21.0, 17.0, 22.0, 18.0, 23.0, 19.0, 24.0}; float* dA; int* dcsc_col_ptr_B; int* dcsc_row_ind_B; float* dcsc_val_B; float* dC; HIP_CHECK(hipMalloc(&dA, sizeof(float) * lda * k)); HIP_CHECK(hipMalloc(&dcsc_col_ptr_B, sizeof(int) * (n + 1))); HIP_CHECK(hipMalloc(&dcsc_row_ind_B, sizeof(int) * nnz)); HIP_CHECK(hipMalloc(&dcsc_val_B, sizeof(float) * nnz)); HIP_CHECK(hipMalloc(&dC, sizeof(float) * ldc * n)); HIP_CHECK(hipMemcpy(dA, hA.data(), sizeof(float) * lda * k, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( dcsc_col_ptr_B, hcsc_col_ptr_B.data(), sizeof(int) * (n + 1), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsc_row_ind_B, hcsc_row_ind_B.data(), sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsc_val_B, hcsc_val_B.data(), sizeof(float) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dC, hC.data(), sizeof(float) * ldc * n, hipMemcpyHostToDevice)); // Create rocSPARSE handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Create matrix descriptor rocsparse_mat_descr descr_B; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr_B)); // Perform the matrix multiplication ROCSPARSE_CHECK(rocsparse_sgemmi(handle, rocsparse_operation_none, rocsparse_operation_transpose, m, n, k, nnz, &alpha, dA, lda, descr_B, dcsc_val_B, dcsc_col_ptr_B, dcsc_row_ind_B, &beta, dC, ldc)); HIP_CHECK(hipMemcpy(hC.data(), dC, sizeof(float) * ldc * n, hipMemcpyDeviceToHost)); std::cout << "hC" << std::endl; for(size_t i = 0; i < hC.size(); i++) { std::cout << hC[i] << " "; } std::cout << "" << std::endl; // Clean up ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr_B)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); // Clear up on device HIP_CHECK(hipFree(dA)); HIP_CHECK(hipFree(dcsc_col_ptr_B)); HIP_CHECK(hipFree(dcsc_row_ind_B)); HIP_CHECK(hipFree(dcsc_val_B)); HIP_CHECK(hipFree(dC)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**trans_A**–**[in]**matrix \(A\) operation type.**trans_B**–**[in]**matrix \(B\) operation type.**m**–**[in]**number of rows of the column-oriented dense matrix \(A\).**n**–**[in]**number of columns of the sparse CSR matrix \(op(B)\) and \(C\).**k**–**[in]**number of columns of the column-oriented dense matrix \(A\).**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix \(B\).**alpha**–**[in]**scalar \(\alpha\).**A**–**[in]**array of dimension \(lda \times k\) ( \(op(A) == A\)) or \(lda \times m\) ( \(op(A) == A^T\) or \(op(A) == A^H\)).**lda**–**[in]**leading dimension of \(A\), must be at least \(m\) ( \(op(A) == A\)) or \(k\) ( \(op(A) == A^T\) or \(op(A) == A^H\)).**descr**–**[in]**descriptor of the sparse CSR matrix \(B\). Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**csr_val**–**[in]**array of`nnz`

elements of the sparse CSR matrix \(B\).**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(B\).**csr_col_ind**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix \(B\).**beta**–**[in]**scalar \(\beta\).**C**–**[inout]**column-oriented dense matrix of dimension \(ldc \times n\) that holds the values of \(C\).**ldc**–**[in]**leading dimension of \(C\), must be at least \(m\).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`n`

,`k`

,`nnz`

,`lda`

or`ldc`

is invalid.**rocsparse_status_invalid_pointer**–`alpha`

,`A`

,`csr_val`

,`csr_row_ptr`

,`csr_col_ind`

,`beta`

or`C`

pointer is invalid.
