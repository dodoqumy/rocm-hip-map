---
title: "Sparse level 2 functions &#8212; rocSPARSE 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocSPARSE/en/latest/reference/level2.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:16:47.596862+00:00
content_hash: "896e641a94761f87"
---

# Sparse level 2 functions[#](#sparse-level-2-functions)

This module contains all sparse level 2 routines.

The sparse level 2 routines describe operations between a matrix in sparse format and a vector in dense format.

## rocsparse_bsrmv_analysis()[#](#rocsparse-bsrmv-analysis)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sbsrmv_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info)[#](#_CPPv425rocsparse_sbsrmv_analysis16rocsparse_handle19rocsparse_direction19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_info)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dbsrmv_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info)[#](#_CPPv425rocsparse_dbsrmv_analysis16rocsparse_handle19rocsparse_direction19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_info)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cbsrmv_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info)[#](#_CPPv425rocsparse_cbsrmv_analysis16rocsparse_handle19rocsparse_direction19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_info)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zbsrmv_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info)[#](#_CPPv425rocsparse_zbsrmv_analysis16rocsparse_handle19rocsparse_direction19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_info) `rocsparse_bsrmv_analysis`

performs the analysis step for[rocsparse_Xbsrmv()](#rocsparse__bsrmv_8h_1a70ab34b4fda46e16fca420eab8186a53). It is expected that this function will be executed only once for a given sparsity pattern and particular operation type. The gathered analysis meta data is stored in the[rocsparse_mat_info](types.html#rocsparse-types_8h_1a3347be72f6e4f3c55318c32b46dcaa92)object and can be cleared by[rocsparse_bsrmv_clear()](#rocsparse__bsrmv_8h_1a0a6146bc8e079f2a2ea719fa30421ea4).If the matrix sparsity pattern changes, the gathered information will become invalid. In order to perform another sparse matrix multiplication with a matrix having a different sparsity pattern, the user would need to either destroy the old

`info`

object and create a new one or the user would need to clear the existing`info`

object using[rocsparse_bsrmv_clear()](#rocsparse__bsrmv_8h_1a0a6146bc8e079f2a2ea719fa30421ea4). In both cases, the analysis will need to be called again.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dir**–**[in]**matrix storage of BSR blocks.**trans**–**[in]**matrix operation type.**mb**–**[in]**number of block rows of the sparse BSR matrix.**nb**–**[in]**number of block columns of the sparse BSR matrix.**nnzb**–**[in]**number of non-zero blocks of the sparse BSR matrix.**descr**–**[in]**descriptor of the sparse BSR matrix. Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**bsr_val**–**[in]**array of`nnzb`

blocks of the sparse BSR matrix.**bsr_row_ptr**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix.**bsr_col_ind**–**[in]**array of`nnzb`

elements containing the block column indices of the sparse BSR matrix.**block_dim**–**[in]**block dimension of the sparse BSR matrix.**info**–**[out]**structure that holds the information collected during the analysis step.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`mb`

,`nb`

or`nnzb`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`bsr_val`

,`bsr_row_ptr`

,`bsr_col_ind`

or`info`

pointer is invalid.**rocsparse_status_memory_error**– the buffer for the gathered information could not be allocated.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_not_implemented**–`trans`

!=[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528)or[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_bsrmv()[#](#rocsparse-bsrmv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sbsrmv([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const float *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, const float *x, const float *beta, float *y)[#](#_CPPv416rocsparse_sbsrmv16rocsparse_handle19rocsparse_direction19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_infoPKfPKfPf)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dbsrmv([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const double *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, const double *x, const double *beta, double *y)[#](#_CPPv416rocsparse_dbsrmv16rocsparse_handle19rocsparse_direction19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKdK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_infoPKdPKdPd)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cbsrmv([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*x, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*beta,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*y)[#](#_CPPv416rocsparse_cbsrmv16rocsparse_handle19rocsparse_direction19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPK23rocsparse_float_complexK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_infoPK23rocsparse_float_complexPK23rocsparse_float_complexP23rocsparse_float_complex)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zbsrmv([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*x, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*beta,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*y)[#](#_CPPv416rocsparse_zbsrmv16rocsparse_handle19rocsparse_direction19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPK24rocsparse_double_complexK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_infoPK24rocsparse_double_complexPK24rocsparse_double_complexP24rocsparse_double_complex) Sparse matrix vector multiplication using BSR storage format.

`rocsparse_bsrmv`

multiplies the scalar \(\alpha\) with a sparse \(m \times n\) matrix, defined in BSR storage format, and the dense vector \(x\) and adds the result to the dense vector \(y\) that is multiplied by the scalar \(\beta\), such that\[ y := \alpha \cdot op(A) \cdot x + \beta \cdot y, \]with\[ op(A) = \left\{ \begin{array}{ll} A, & \text{if trans == rocsparse_operation_none} \end{array} \right. \]and where \(m = mb \times block\_dim\) and \(n= nb \times block\_dim\).Performing the above operation can be done with or without analysis. Running with analysis may result in better performance when computing the matrix vector product but will also incur a performance cost attributed to the additional analysis step. For this reason, running with analysis makes sense when a user plans on computing the matrix vector product many times and therefore can amortize the analysis cost.

To run without analysis, performing the above operation involves simply calling the

`rocsparse_bsrmv`

routine while passing`NULL`

for the`info`

parameter.To run with analysis, performing the above operation involves two steps. First, the user creates a

[rocsparse_mat_info](types.html#rocsparse-types_8h_1a3347be72f6e4f3c55318c32b46dcaa92)object by calling[rocsparse_create_mat_info](auxiliary.html#rocsparse-auxiliary_8h_1a23eb2202356ebb8506136b4898abdeaf)and then passes this to[rocsparse_Xbsrmv_analysis()](#rocsparse__bsrmv_8h_1afbc9ad599f9c1bed1a8763d67dd05a48)which will perform analysis on the sparsity pattern of the matrix \(op(A)\). The user then completes the operation by calling`rocsparse_bsrmv`

. The creation of the`info`

object and the call to the analysis routine only need to be performed once for a given sparsity pattern while the computation can be performed repeatedly as long as the sparsity pattern has not changed. Once all calls to`rocsparse_bsrmv`

have been made, the`info`

object can be destroyed with a call to[rocsparse_destroy_mat_info](auxiliary.html#rocsparse-auxiliary_8h_1a9c143f65076a10ebafcffc633ad5d87b).When running with analysis, a user may find themselves in the situation where they wish to perform multiple sparse matrix multiplications with each sparse matrix having a different sparsity pattern. Instead of creating and destroying multiple

[rocsparse_mat_info](types.html#rocsparse-types_8h_1a3347be72f6e4f3c55318c32b46dcaa92)objects for each unique sparsity pattern, the user can instead create the`info`

object once and then call[rocsparse_bsrmv_clear](#rocsparse__bsrmv_8h_1a0a6146bc8e079f2a2ea719fa30421ea4)followed by re-running the analysis in between each sparse matrix multiplication.**Example**This example performs a sparse matrix vector multiplication in BSR format.

int main() { // rocSPARSE handle rocsparse_handle handle; rocsparse_create_handle(&handle); // alpha * ( 1.0 0.0 2.0 ) * ( 1.0 ) + beta * ( 4.0 ) = ( 31.1 ) // ( 3.0 0.0 4.0 ) * ( 2.0 ) ( 5.0 ) = ( 62.0 ) // ( 5.0 6.0 0.0 ) * ( 3.0 ) ( 6.0 ) = ( 70.7 ) // ( 7.0 0.0 8.0 ) * ( 7.0 ) = ( 123.8 ) // BSR block dimension rocsparse_int bsr_dim = 2; // Number of block rows and columns rocsparse_int mb = 2; rocsparse_int nb = 2; // Number of non-zero blocks rocsparse_int nnzb = 4; // BSR row pointers rocsparse_int hbsr_row_ptr[3] = {0, 2, 4}; // BSR column indices rocsparse_int hbsr_col_ind[4] = {0, 1, 0, 1}; // BSR values double hbsr_val[16] = {1.0, 3.0, 0.0, 0.0, 2.0, 4.0, 0.0, 0.0, 5.0, 7.0, 6.0, 0.0, 0.0, 8.0, 0.0, 0.0}; // Block storage in column major rocsparse_direction dir = rocsparse_direction_column; // Transposition of the matrix rocsparse_operation trans = rocsparse_operation_none; // Scalar alpha and beta double alpha = 3.7; double beta = 1.3; // x and y double hx[4] = {1.0, 2.0, 3.0, 0.0}; double hy[4] = {4.0, 5.0, 6.0, 7.0}; // Matrix descriptor rocsparse_mat_descr descr; rocsparse_create_mat_descr(&descr); // Offload data to device rocsparse_int* dbsr_row_ptr; rocsparse_int* dbsr_col_ind; double* dbsr_val; double* dx; double* dy; HIP_CHECK(hipMalloc(&dbsr_row_ptr, sizeof(rocsparse_int) * (mb + 1))); HIP_CHECK(hipMalloc(&dbsr_col_ind, sizeof(rocsparse_int) * nnzb)); HIP_CHECK(hipMalloc(&dbsr_val, sizeof(double) * nnzb * bsr_dim * bsr_dim)); HIP_CHECK(hipMalloc(&dx, sizeof(double) * nb * bsr_dim)); HIP_CHECK(hipMalloc(&dy, sizeof(double) * mb * bsr_dim)); HIP_CHECK(hipMemcpy( dbsr_row_ptr, hbsr_row_ptr, sizeof(rocsparse_int) * (mb + 1), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dbsr_col_ind, hbsr_col_ind, sizeof(rocsparse_int) * nnzb, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( dbsr_val, hbsr_val, sizeof(double) * nnzb * bsr_dim * bsr_dim, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dx, hx, sizeof(double) * nb * bsr_dim, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dy, hy, sizeof(double) * mb * bsr_dim, hipMemcpyHostToDevice)); rocsparse_mat_info info; ROCSPARSE_CHECK(rocsparse_create_mat_info(&info)); // Call dbsrmv_analysis (Optional) ROCSPARSE_CHECK(rocsparse_dbsrmv_analysis(handle, dir, trans, mb, nb, nnzb, descr, dbsr_val, dbsr_row_ptr, dbsr_col_ind, bsr_dim, info)); // Call dbsrmv to perform y = alpha * A x + beta * y ROCSPARSE_CHECK(rocsparse_dbsrmv(handle, dir, trans, mb, nb, nnzb, &alpha, descr, dbsr_val, dbsr_row_ptr, dbsr_col_ind, bsr_dim, info, dx, &beta, dy)); // Copy result back to host HIP_CHECK(hipMemcpy(hy, dy, sizeof(double) * mb * bsr_dim, hipMemcpyDeviceToHost)); std::cout << "hy" << std::endl; for(rocsparse_int i = 0; i < mb * bsr_dim; i++) { std::cout << hy[i] << " "; } std::cout << "" << std::endl; // Clear rocSPARSE ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); ROCSPARSE_CHECK(rocsparse_destroy_mat_info(info)); // Clear device memory HIP_CHECK(hipFree(dbsr_row_ptr)); HIP_CHECK(hipFree(dbsr_col_ind)); HIP_CHECK(hipFree(dbsr_val)); HIP_CHECK(hipFree(dx)); HIP_CHECK(hipFree(dy)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dir**–**[in]**matrix storage of BSR blocks.**trans**–**[in]**matrix operation type.**mb**–**[in]**number of block rows of the sparse BSR matrix.**nb**–**[in]**number of block columns of the sparse BSR matrix.**nnzb**–**[in]**number of non-zero blocks of the sparse BSR matrix.**alpha**–**[in]**scalar \(\alpha\).**descr**–**[in]**descriptor of the sparse BSR matrix. Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**bsr_val**–**[in]**array of`nnzb`

blocks of the sparse BSR matrix.**bsr_row_ptr**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix.**bsr_col_ind**–**[in]**array of`nnzb`

elements containing the block column indices of the sparse BSR matrix.**block_dim**–**[in]**block dimension of the sparse BSR matrix.**x**–**[in]**array of`nb*block_dim`

elements ( \(op(A) = A\)) or`mb*block_dim`

elements ( \(op(A) = A^T\) or \(op(A) = A^H\)).**beta**–**[in]**scalar \(\beta\).**y**–**[inout]**array of`mb*block_dim`

elements ( \(op(A) = A\)) or`nb*block_dim`

elements ( \(op(A) = A^T\) or \(op(A) = A^H\)).**info**–**[out]**structure that holds the information collected during the analysis step.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`mb`

,`nb`

,`nnzb`

or`block_dim`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`alpha`

,`bsr_val`

,`bsr_row_ind`

,`bsr_col_ind`

,`x`

,`beta`

or`y`

pointer is invalid.**rocsparse_status_arch_mismatch**– the device is not supported.**rocsparse_status_not_implemented**–`trans`

!=[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528)or[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_bsrmv_clear()[#](#rocsparse-bsrmv-clear)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_bsrmv_clear([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info)[#](#_CPPv421rocsparse_bsrmv_clear16rocsparse_handle18rocsparse_mat_info) `rocsparse_bsrmv_clear`

deallocates all memory that was allocated by[rocsparse_Xbsrmv_analysis()](#rocsparse__bsrmv_8h_1afbc9ad599f9c1bed1a8763d67dd05a48). This is especially useful if memory is an issue and the analysis data is not required anymore for further computation, e.g. when switching to another sparse matrix format.Calling

`rocsparse_bsrmv_clear`

is optional. All allocated resources will be cleared, when the opaque[rocsparse_mat_info](types.html#rocsparse-types_8h_1a3347be72f6e4f3c55318c32b46dcaa92)object is destroyed using[rocsparse_destroy_mat_info()](auxiliary.html#rocsparse-auxiliary_8h_1a9c143f65076a10ebafcffc633ad5d87b).Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**info**–**[inout]**structure that holds the information collected during analysis step.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`info`

pointer is invalid.**rocsparse_status_memory_error**– the buffer for the gathered information could not be deallocated.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_bsrxmv()[#](#rocsparse-bsrxmv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sbsrxmv([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)size_of_mask,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const float *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_mask_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_end_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim, const float *x, const float *beta, float *y)[#](#_CPPv417rocsparse_sbsrxmv16rocsparse_handle19rocsparse_direction19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intPK13rocsparse_intPK13rocsparse_int13rocsparse_intPKfPKfPf)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dbsrxmv([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)size_of_mask,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const double *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_mask_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_end_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim, const double *x, const double *beta, double *y)[#](#_CPPv417rocsparse_dbsrxmv16rocsparse_handle19rocsparse_direction19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPKdK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_intPK13rocsparse_intPK13rocsparse_int13rocsparse_intPKdPKdPd)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cbsrxmv([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)size_of_mask,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_mask_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_end_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*x, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*beta,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*y)[#](#_CPPv417rocsparse_cbsrxmv16rocsparse_handle19rocsparse_direction19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPK23rocsparse_float_complexK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_intPK13rocsparse_intPK13rocsparse_int13rocsparse_intPK23rocsparse_float_complexPK23rocsparse_float_complexP23rocsparse_float_complex)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zbsrxmv([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)size_of_mask,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_mask_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_end_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*x, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*beta,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*y)[#](#_CPPv417rocsparse_zbsrxmv16rocsparse_handle19rocsparse_direction19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPK24rocsparse_double_complexK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_intPK13rocsparse_intPK13rocsparse_int13rocsparse_intPK24rocsparse_double_complexPK24rocsparse_double_complexP24rocsparse_double_complex) Sparse matrix vector multiplication with mask operation using BSR storage format.

`rocsparse_bsrxmv`

multiplies the scalar \(\alpha\) with a sparse \(m \times n\) modified matrix, defined in BSR storage format, and the dense vector \(x\) and adds the result to the dense vector \(y\) that is multiplied by the scalar \(\beta\), such that\[ y := \left( \alpha \cdot op(A) \cdot x + \beta \cdot y \right)\left( \text{mask} \right), \]with\[ op(A) = \left\{ \begin{array}{ll} A, & \text{if trans == rocsparse_operation_none} \end{array} \right. \]and where \(m = mb \times block\_dim\) and \(n = nb \times block\_dim\).The \(\text{mask}\) is defined as an array of block row indices. The input sparse matrix is defined with a modified BSR storage format where the beginning and the end of each row is defined with two arrays,

`bsr_row_ptr`

and`bsr_end_ptr`

(both of size`mb`

), rather the usual`bsr_row_ptr`

of size`mb+1`

.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

Currently, only

`trans`

==[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528)is supported. Currently,`block_dim==1`

is not supported.Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dir**–**[in]**matrix storage of BSR blocks.**trans**–**[in]**matrix operation type.**size_of_mask**–**[in]**number of updated block rows of the array`y`

.**mb**–**[in]**number of block rows of the sparse BSR matrix.**nb**–**[in]**number of block columns of the sparse BSR matrix.**nnzb**–**[in]**number of non-zero blocks of the sparse BSR matrix.**alpha**–**[in]**scalar \(\alpha\).**descr**–**[in]**descriptor of the sparse BSR matrix. Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**bsr_val**–**[in]**array of`nnzb`

blocks of the sparse BSR matrix.**bsr_mask_ptr**–**[in]**array of`size_of_mask`

elements that give the indices of the updated block rows.**bsr_row_ptr**–**[in]**array of`mb`

elements that point to the start of every block row of the sparse BSR matrix.**bsr_end_ptr**–**[in]**array of`mb`

elements that point to the end of every block row of the sparse BSR matrix.**bsr_col_ind**–**[in]**array of`nnzb`

elements containing the block column indices of the sparse BSR matrix.**block_dim**–**[in]**block dimension of the sparse BSR matrix.**x**–**[in]**array of`nb*block_dim`

elements ( \(op(A) = A\)) or`mb*block_dim`

elements ( \(op(A) = A^T\) or \(op(A) = A^H\)).**beta**–**[in]**scalar \(\beta\).**y**–**[inout]**array of`mb*block_dim`

elements ( \(op(A) = A\)) or`nb*block_dim`

elements ( \(op(A) = A^T\) or \(op(A) = A^H\)).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`mb`

,`nb`

,`nnzb`

,`block_dim`

or`size_of_mask`

is invalid.**rocsparse_status_invalid_value**–`size_of_mask`

is greater than`mb`

.**rocsparse_status_invalid_pointer**–`descr`

,`alpha`

,`bsr_val`

,`bsr_row_ind`

,`bsr_col_ind`

,`x`

,`beta`

or`y`

pointer is invalid.**rocsparse_status_arch_mismatch**– the device is not supported.**rocsparse_status_not_implemented**–`block_dim==1`

,`trans`

!=[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528)or[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_bsrsv_zero_pivot()[#](#rocsparse-bsrsv-zero-pivot)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_bsrsv_zero_pivot([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_int](types.html#_CPPv413rocsparse_int)*position)[#](#_CPPv426rocsparse_bsrsv_zero_pivot16rocsparse_handle18rocsparse_mat_infoP13rocsparse_int) `rocsparse_bsrsv_zero_pivot`

returns[rocsparse_status_zero_pivot](enumerations.html#rocsparse-types_8h_1a578f8c5c1b08f358bf4605b0031006a8a01fe264830c8ce6451ce6888bc8d3e80), if either a structural or numerical zero has been found during[rocsparse_sbsrsv_solve()](#rocsparse__bsrsv_8h_1a29595987030af2b93cc50c15d44f14b9), computation. The first zero pivot \(j\) at \(A_{j,j}\) is stored in`position`

, using same index base as the BSR matrix.`position`

can be in host or device memory. If no zero pivot has been found,`position`

is set to -1 and[rocsparse_status_success](enumerations.html#rocsparse-types_8h_1a578f8c5c1b08f358bf4605b0031006a8a96462a9361cfceb6cf9354e10fdc671b)is returned instead.Note

`rocsparse_bsrsv_zero_pivot`

is a blocking function. It might influence performance negatively.Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**info**–**[in]**structure that holds the information collected during the analysis step.**position**–**[inout]**pointer to zero pivot \(j\), can be in host or device memory.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`info`

or`position`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_zero_pivot**– zero pivot has been found.



## rocsparse_bsrsv_buffer_size()[#](#rocsparse-bsrsv-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sbsrsv_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, size_t *buffer_size)[#](#_CPPv428rocsparse_sbsrsv_buffer_size16rocsparse_handle19rocsparse_direction19rocsparse_operation13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_infoP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dbsrsv_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, size_t *buffer_size)[#](#_CPPv428rocsparse_dbsrsv_buffer_size16rocsparse_handle19rocsparse_direction19rocsparse_operation13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_infoP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cbsrsv_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, size_t *buffer_size)[#](#_CPPv428rocsparse_cbsrsv_buffer_size16rocsparse_handle19rocsparse_direction19rocsparse_operation13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_infoP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zbsrsv_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, size_t *buffer_size)[#](#_CPPv428rocsparse_zbsrsv_buffer_size16rocsparse_handle19rocsparse_direction19rocsparse_operation13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_infoP6size_t) `rocsparse_bsrsv_buffer_size`

returns the size of the temporary storage buffer that is required by[rocsparse_Xbsrsv_analysis()](#rocsparse__bsrsv_8h_1aade89276269f88cd50e357c0a3504c87)and[rocsparse_Xbsrsv_solve()](#rocsparse__bsrsv_8h_1a29595987030af2b93cc50c15d44f14b9). The temporary storage buffer must be allocated by the user.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dir**–**[in]**matrix storage of BSR blocks.**trans**–**[in]**matrix operation type.**mb**–**[in]**number of block rows of the sparse BSR matrix.**nnzb**–**[in]**number of non-zero blocks of the sparse BSR matrix.**descr**–**[in]**descriptor of the sparse BSR matrix.**bsr_val**–**[in]**array of`nnzb`

blocks of the sparse BSR matrix.**bsr_row_ptr**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix.**bsr_col_ind**–**[in]**array of`nnz`

containing the block column indices of the sparse BSR matrix.**block_dim**–**[in]**block dimension of the sparse BSR matrix.**info**–**[out]**structure that holds the information collected during the analysis step.**buffer_size**–**[out]**number of bytes of the temporary storage buffer required by[rocsparse_sbsrsv_analysis()](#rocsparse__bsrsv_8h_1aade89276269f88cd50e357c0a3504c87),[rocsparse_dbsrsv_analysis()](#rocsparse__bsrsv_8h_1aa2841e4f2366e20c07f3d3f04bc2ee85),[rocsparse_cbsrsv_analysis()](#rocsparse__bsrsv_8h_1a5f36d74d3b9a9396a38943142cd7877f),[rocsparse_zbsrsv_analysis()](#rocsparse__bsrsv_8h_1a83ec60a2b9e4d5a992ffde2c3a4c5d7c),[rocsparse_sbsrsv_solve()](#rocsparse__bsrsv_8h_1a29595987030af2b93cc50c15d44f14b9),[rocsparse_dbsrsv_solve()](#rocsparse__bsrsv_8h_1aeff4ceb63fb39b2d41ef05c1e8b94059),[rocsparse_cbsrsv_solve()](#rocsparse__bsrsv_8h_1a52de328a9b91e1c1825739eebe1c816e)and[rocsparse_zbsrsv_solve()](#rocsparse__bsrsv_8h_1ad72e93eb029c2b43403bf6e092a548ab).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`mb`

,`nnzb`

or`block_dim`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`bsr_val`

,`bsr_row_ptr`

,`bsr_col_ind`

,`info`

or`buffer_size`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_not_implemented**–`trans`

==[rocsparse_operation_conjugate_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a6920c1aa5f80005eee4b66ea6f25330f)or[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_bsrsv_analysis()[#](#rocsparse-bsrsv-analysis)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sbsrsv_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_analysis_policy](enumerations.html#_CPPv425rocsparse_analysis_policy)analysis,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)solve, void *temp_buffer)[#](#_CPPv425rocsparse_sbsrsv_analysis16rocsparse_handle19rocsparse_direction19rocsparse_operation13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dbsrsv_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_analysis_policy](enumerations.html#_CPPv425rocsparse_analysis_policy)analysis,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)solve, void *temp_buffer)[#](#_CPPv425rocsparse_dbsrsv_analysis16rocsparse_handle19rocsparse_direction19rocsparse_operation13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cbsrsv_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_analysis_policy](enumerations.html#_CPPv425rocsparse_analysis_policy)analysis,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)solve, void *temp_buffer)[#](#_CPPv425rocsparse_cbsrsv_analysis16rocsparse_handle19rocsparse_direction19rocsparse_operation13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zbsrsv_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_analysis_policy](enumerations.html#_CPPv425rocsparse_analysis_policy)analysis,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)solve, void *temp_buffer)[#](#_CPPv425rocsparse_zbsrsv_analysis16rocsparse_handle19rocsparse_direction19rocsparse_operation13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv) `rocsparse_bsrsv_analysis`

performs the analysis step for[rocsparse_sbsrsv_solve()](#rocsparse__bsrsv_8h_1a29595987030af2b93cc50c15d44f14b9). It is expected that this function will be executed only once for a given matrix and particular operation type. The analysis meta data can be cleared by[rocsparse_bsrsv_clear()](#rocsparse__bsrsv_8h_1a1e95de000b8cd9a1388a4d55fdc9384b).`rocsparse_bsrsv_analysis`

can share its meta data with[rocsparse_Xbsrsm_analysis()](level3.html#rocsparse__bsrsm_8h_1aa7c3da4c56f9dcf7aaae3e65dd35110f),[rocsparse_Xbsrilu0_analysis()](precond.html#rocsparse__bsrilu0_8h_1ac20c3e0a79507660dea8895f4111f170), and[rocsparse_Xbsric0_analysis()](precond.html#rocsparse__bsric0_8h_1a9cfb58036bb689f2becba8c0baa9d716). Selecting[rocsparse_analysis_policy_reuse](enumerations.html#rocsparse-types_8h_1a43b20aa4bb19623a91b5952422fbe35ca658466413f4005c0c103d20d5e352078)policy can greatly improve computation performance of meta data. However, the user needs to make sure that the sparsity pattern remains unchanged. If this cannot be assured,[rocsparse_analysis_policy_force](enumerations.html#rocsparse-types_8h_1a43b20aa4bb19623a91b5952422fbe35cac66b70c4f519ddd03dcbe0f3a973401a)has to be used.Note

If the matrix sparsity pattern changes, the gathered information will become invalid.

Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dir**–**[in]**matrix storage of BSR blocks.**trans**–**[in]**matrix operation type.**mb**–**[in]**number of block rows of the sparse BSR matrix.**nnzb**–**[in]**number of non-zero blocks of the sparse BSR matrix.**descr**–**[in]**descriptor of the sparse BSR matrix.**bsr_val**–**[in]**array of`nnzb`

blocks of the sparse BSR matrix.**bsr_row_ptr**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix.**bsr_col_ind**–**[in]**array of`nnz`

containing the block column indices of the sparse BSR matrix.**block_dim**–**[in]**block dimension of the sparse BSR matrix.**info**–**[out]**structure that holds the information collected during the analysis step.**analysis**–**[in]**[rocsparse_analysis_policy_reuse](enumerations.html#rocsparse-types_8h_1a43b20aa4bb19623a91b5952422fbe35ca658466413f4005c0c103d20d5e352078)or[rocsparse_analysis_policy_force](enumerations.html#rocsparse-types_8h_1a43b20aa4bb19623a91b5952422fbe35cac66b70c4f519ddd03dcbe0f3a973401a).**solve**–**[in]**[rocsparse_solve_policy_auto](enumerations.html#rocsparse-types_8h_1a5a3e261123e81a9e8b267c6109e26957a9c6bdf97e192d429ca536d5ab98ea866).**temp_buffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`mb`

,`nnzb`

or`block_dim`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`bsr_row_ptr`

,`bsr_col_ind`

,`info`

or`temp_buffer`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_not_implemented**–`trans`

==[rocsparse_operation_conjugate_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a6920c1aa5f80005eee4b66ea6f25330f)or[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_bsrsv_solve()[#](#rocsparse-bsrsv-solve)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sbsrsv_solve([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const float *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, const float *x, float *y,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv422rocsparse_sbsrsv_solve16rocsparse_handle19rocsparse_direction19rocsparse_operation13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_infoPKfPf22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dbsrsv_solve([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const double *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, const double *x, double *y,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv422rocsparse_dbsrsv_solve16rocsparse_handle19rocsparse_direction19rocsparse_operation13rocsparse_int13rocsparse_intPKdK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_infoPKdPd22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cbsrsv_solve([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*x,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*y,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv422rocsparse_cbsrsv_solve16rocsparse_handle19rocsparse_direction19rocsparse_operation13rocsparse_int13rocsparse_intPK23rocsparse_float_complexK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_infoPK23rocsparse_float_complexP23rocsparse_float_complex22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zbsrsv_solve([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*x,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*y,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv422rocsparse_zbsrsv_solve16rocsparse_handle19rocsparse_direction19rocsparse_operation13rocsparse_int13rocsparse_intPK24rocsparse_double_complexK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_infoPK24rocsparse_double_complexP24rocsparse_double_complex22rocsparse_solve_policyPv) Sparse triangular solve using BSR storage format.

`rocsparse_bsrsv_solve`

solves a sparse triangular linear system of a sparse \(m \times m\) matrix, defined in BSR storage format, a dense solution vector \(y\) and the right-hand side \(x\) that is multiplied by \(\alpha\), such that\[ op(A) \cdot y = \alpha \cdot x, \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if trans == rocsparse_operation_none} \\ A^T, & \text{if trans == rocsparse_operation_transpose} \end{array} \right. \end{split}\]Performing the above operation requires three steps. First, the user calls

[rocsparse_Xbsrsv_buffer_size()](#rocsparse__bsrsv_8h_1aa0d8d2b089478eaa357c7ca0f2d1332e)which will determine the size of the required temporary storage buffer. The user then allocates this buffer and calls[rocsparse_Xbsrsv_analysis()](#rocsparse__bsrsv_8h_1aade89276269f88cd50e357c0a3504c87)which will perform analysis on the sparse matrix \(op(A)\). Finally, the user completes the computation by calling`rocsparse_bsrsv_solve`

. The buffer size, buffer allocation, and analysis only need to be called once for a given sparse matrix \(op(A)\) while the computation stage can be repeatedly used with different \(x\) and \(y\) vectors. Once all calls to`rocsparse_bsrsv_solve`

are complete, the temporary buffer can be deallocated.Solving a triangular system involves inverting the diagonal blocks. This means that if the sparse matrix is missing the diagonal block (referred to as a structural zero) or the diagonal block is not invertible (referred to as a numerical zero) then a solution is not possible.

`rocsparse_bsrsv_solve`

tracks the location of the first zero pivot (either numerical or structural zero). The zero pivot status can be checked calling[rocsparse_bsrsv_zero_pivot()](#rocsparse__bsrsv_8h_1a622882132eadc19e11566beb6c988d65). If[rocsparse_bsrsv_zero_pivot()](#rocsparse__bsrsv_8h_1a622882132eadc19e11566beb6c988d65)returns[rocsparse_status_success](enumerations.html#rocsparse-types_8h_1a578f8c5c1b08f358bf4605b0031006a8a96462a9361cfceb6cf9354e10fdc671b), then no zero pivot was found and therefore the matrix does not have a structural or numerical zero.The user can specify that the sparse matrix should be interpreted as having identity blocks on the diagonal by setting the diagonal type on the descriptor

`descr`

to[rocsparse_diag_type_unit](enumerations.html#rocsparse-types_8h_1a6e8e038adcd3fa03168a1cb4a7da1bc5ac14545fb3bf8773d5f6b8e258c9576f4)using[rocsparse_set_mat_diag_type](auxiliary.html#rocsparse-auxiliary_8h_1a61f894d80e4da74c7e8cd43f61f9215c). If[rocsparse_diag_type](enumerations.html#rocsparse-types_8h_1a6e8e038adcd3fa03168a1cb4a7da1bc5)==[rocsparse_diag_type_unit](enumerations.html#rocsparse-types_8h_1a6e8e038adcd3fa03168a1cb4a7da1bc5ac14545fb3bf8773d5f6b8e258c9576f4), no zero pivot will be reported, even if the diagonal block \(A_{j,j}\) for some \(j\) is not invertible.The sparse CSR matrix passed to

`rocsparse_bsrsv_solve`

does not actually have to be a triangular matrix. Instead the triangular upper or lower part of the sparse matrix is solved based on[rocsparse_fill_mode](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1)set on the descriptor`descr`

. If the fill mode is set to[rocsparse_fill_mode_lower](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a1eb644f6f2701329635e07d91919d37e), then the lower triangular matrix is solved. If the fill mode is set to[rocsparse_fill_mode_upper](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a905f490c7fc5a59e8a635938cec0d004)then the upper triangular matrix is solved.**Example**Consider the lower triangular \(m \times m\) matrix \(L\), stored in BSR storage format with unit diagonal. The following example solves \(L \cdot y = x\).

int main() { // 2 1 0 0 // A = 1 2 0 0 // 0 0 2 1 // 0 0 1 2 int mb = 2; int nb = 2; int nnzb = 2; int block_dim = 2; double alpha = 1.0; std::vector<int> hbsr_row_ptr = {0, 1, 2}; std::vector<int> hbsr_col_ind = {0, 1}; std::vector<double> hbsr_val = {2.0, 1.0, 1.0, 2.0, 2.0, 1.0, 1.0, 2.0}; std::vector<double> hx(mb * block_dim, 1.0); std::vector<double> hy(mb * block_dim); int* dbsr_row_ptr; int* dbsr_col_ind; double* dbsr_val; double* dx; double* dy; HIP_CHECK(hipMalloc(&dbsr_row_ptr, sizeof(int) * (mb + 1))); HIP_CHECK(hipMalloc(&dbsr_col_ind, sizeof(int) * nnzb)); HIP_CHECK(hipMalloc(&dbsr_val, sizeof(double) * nnzb * block_dim * block_dim)); HIP_CHECK(hipMalloc(&dx, sizeof(double) * mb * block_dim)); HIP_CHECK(hipMalloc(&dy, sizeof(double) * mb * block_dim)); HIP_CHECK(hipMemcpy( dbsr_row_ptr, hbsr_row_ptr.data(), sizeof(int) * (mb + 1), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dbsr_col_ind, hbsr_col_ind.data(), sizeof(int) * nnzb, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dbsr_val, hbsr_val.data(), sizeof(double) * nnzb * block_dim * block_dim, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dx, hx.data(), sizeof(double) * mb * block_dim, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dy, hy.data(), sizeof(double) * mb * block_dim, hipMemcpyHostToDevice)); // Create rocSPARSE handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Create matrix descriptor rocsparse_mat_descr descr; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr)); ROCSPARSE_CHECK(rocsparse_set_mat_fill_mode(descr, rocsparse_fill_mode_lower)); ROCSPARSE_CHECK(rocsparse_set_mat_diag_type(descr, rocsparse_diag_type_non_unit)); // Create matrix info structure rocsparse_mat_info info; ROCSPARSE_CHECK(rocsparse_create_mat_info(&info)); // Obtain required buffer size size_t buffer_size; ROCSPARSE_CHECK(rocsparse_dbsrsv_buffer_size(handle, rocsparse_direction_column, rocsparse_operation_none, mb, nnzb, descr, dbsr_val, dbsr_row_ptr, dbsr_col_ind, block_dim, info, &buffer_size)); // Allocate temporary buffer void* temp_buffer; HIP_CHECK(hipMalloc(&temp_buffer, buffer_size)); // Perform analysis step ROCSPARSE_CHECK(rocsparse_dbsrsv_analysis(handle, rocsparse_direction_column, rocsparse_operation_none, mb, nnzb, descr, dbsr_val, dbsr_row_ptr, dbsr_col_ind, block_dim, info, rocsparse_analysis_policy_reuse, rocsparse_solve_policy_auto, temp_buffer)); // Solve Ly = x ROCSPARSE_CHECK(rocsparse_dbsrsv_solve(handle, rocsparse_direction_column, rocsparse_operation_none, mb, nnzb, &alpha, descr, dbsr_val, dbsr_row_ptr, dbsr_col_ind, block_dim, info, dx, dy, rocsparse_solve_policy_auto, temp_buffer)); HIP_CHECK(hipMemcpy(hy.data(), dy, sizeof(double) * mb * block_dim, hipMemcpyDeviceToHost)); std::cout << "hy" << std::endl; for(size_t i = 0; i < hy.size(); i++) { std::cout << hy[i] << " "; } std::cout << "" << std::endl; // Clean up ROCSPARSE_CHECK(rocsparse_destroy_mat_info(info)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); HIP_CHECK(hipFree(dbsr_row_ptr)); HIP_CHECK(hipFree(dbsr_col_ind)); HIP_CHECK(hipFree(dbsr_val)); HIP_CHECK(hipFree(temp_buffer)); return 0; }


Note

The sparse BSR matrix has to be sorted.

Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

Currently, only

`trans`

==[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528)and`trans`

==[rocsparse_operation_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a1ea3194d0c7bdb9e500d6faeead8ebf5)is supported.Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dir**–**[in]**matrix storage of BSR blocks.**trans**–**[in]**matrix operation type.**mb**–**[in]**number of block rows of the sparse BSR matrix.**nnzb**–**[in]**number of non-zero blocks of the sparse BSR matrix.**alpha**–**[in]**scalar \(\alpha\).**descr**–**[in]**descriptor of the sparse BSR matrix.**bsr_val**–**[in]**array of`nnzb`

blocks of the sparse BSR matrix.**bsr_row_ptr**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix.**bsr_col_ind**–**[in]**array of`nnz`

containing the block column indices of the sparse BSR matrix.**block_dim**–**[in]**block dimension of the sparse BSR matrix.**info**–**[in]**structure that holds the information collected during the analysis step.**x**–**[in]**array of`m`

elements, holding the right-hand side.**y**–**[out]**array of`m`

elements, holding the solution.**policy**–**[in]**[rocsparse_solve_policy_auto](enumerations.html#rocsparse-types_8h_1a5a3e261123e81a9e8b267c6109e26957a9c6bdf97e192d429ca536d5ab98ea866).**temp_buffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`mb`

,`nnzb`

or`block_dim`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`alpha`

,`bsr_val`

,`bsr_row_ptr`

,`bsr_col_ind`

,`x`

or`y`

pointer is invalid.**rocsparse_status_arch_mismatch**– the device is not supported.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_not_implemented**–`trans`

==[rocsparse_operation_conjugate_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a6920c1aa5f80005eee4b66ea6f25330f)or[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_bsrsv_clear()[#](#rocsparse-bsrsv-clear)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_bsrsv_clear([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info)[#](#_CPPv421rocsparse_bsrsv_clear16rocsparse_handle18rocsparse_mat_info) `rocsparse_bsrsv_clear`

deallocates all memory that was allocated by[rocsparse_sbsrsv_analysis()](#rocsparse__bsrsv_8h_1aade89276269f88cd50e357c0a3504c87). This is especially useful, if memory is an issue and the analysis data is not required for further computation, e.g. when switching to another sparse matrix format. Calling`rocsparse_bsrsv_clear`

is optional. All allocated resources will be cleared when the opaque[rocsparse_mat_info](types.html#rocsparse-types_8h_1a3347be72f6e4f3c55318c32b46dcaa92)struct is destroyed using[rocsparse_destroy_mat_info()](auxiliary.html#rocsparse-auxiliary_8h_1a9c143f65076a10ebafcffc633ad5d87b).Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**info**–**[inout]**structure that holds the information collected during the analysis step.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`info`

pointer is invalid.**rocsparse_status_memory_error**– the buffer holding the meta data could not be deallocated.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_coomv()[#](#rocsparse-coomv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scoomv([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const float *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *coo_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_row_ind, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_col_ind, const float *x, const float *beta, float *y)[#](#_CPPv416rocsparse_scoomv16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intPKfPKfPf)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcoomv([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const double *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *coo_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_row_ind, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_col_ind, const double *x, const double *beta, double *y)[#](#_CPPv416rocsparse_dcoomv16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKdK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_intPKdPKdPd)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccoomv([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*coo_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_row_ind, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_col_ind, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*x, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*beta,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*y)[#](#_CPPv416rocsparse_ccoomv16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPK23rocsparse_float_complexK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_intPK23rocsparse_float_complexPK23rocsparse_float_complexP23rocsparse_float_complex)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcoomv([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*coo_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_row_ind, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*coo_col_ind, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*x, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*beta,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*y)[#](#_CPPv416rocsparse_zcoomv16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPK24rocsparse_double_complexK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_intPK24rocsparse_double_complexPK24rocsparse_double_complexP24rocsparse_double_complex) Sparse matrix vector multiplication using COO storage format.

`rocsparse_coomv`

multiplies the scalar \(\alpha\) with a sparse \(m \times n\) matrix, defined in COO storage format, and the dense vector \(x\) and adds the result to the dense vector \(y\) that is multiplied by the scalar \(\beta\), such that\[ y := \alpha \cdot op(A) \cdot x + \beta \cdot y, \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if trans == rocsparse_operation_none} \\ A^T, & \text{if trans == rocsparse_operation_transpose} \\ A^H, & \text{if trans == rocsparse_operation_conjugate_transpose} \end{array} \right. \end{split}\]The COO matrix has to be sorted by row indices. This can be achieved by using

[rocsparse_coosort_by_row()](conversion.html#rocsparse__coosort_8h_1a3df99893a1ceb0aae76f89068369a731).for(i = 0; i < m; ++i) { y[i] = beta * y[i]; } for(i = 0; i < nnz; ++i) { y[coo_row_ind[i]] += alpha * coo_val[i] * x[coo_col_ind[i]]; }

**Example**This example performs a sparse matrix vector multiplication in COO format.

int main() { // rocSPARSE handle rocsparse_handle handle; rocsparse_create_handle(&handle); // A sparse matrix // 1 0 3 4 // 0 0 5 1 // 0 2 0 0 // 4 0 0 8 rocsparse_int hArow[8] = {0, 0, 0, 1, 1, 2, 3, 3}; rocsparse_int hAcol[8] = {0, 2, 3, 2, 3, 1, 0, 3}; double hAval[8] = {1.0, 3.0, 4.0, 5.0, 1.0, 2.0, 4.0, 8.0}; rocsparse_int m = 4; rocsparse_int n = 4; rocsparse_int nnz = 8; double halpha = 1.0; double hbeta = 0.0; double hx[4] = {1.0, 2.0, 3.0, 4.0}; // Matrix descriptor rocsparse_mat_descr descrA; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descrA)); // Offload data to device rocsparse_int* dArow; rocsparse_int* dAcol; double* dAval; double* dx; double* dy; HIP_CHECK(hipMalloc(&dArow, sizeof(rocsparse_int) * nnz)); HIP_CHECK(hipMalloc(&dAcol, sizeof(rocsparse_int) * nnz)); HIP_CHECK(hipMalloc(&dAval, sizeof(double) * nnz)); HIP_CHECK(hipMalloc(&dx, sizeof(double) * n)); HIP_CHECK(hipMalloc(&dy, sizeof(double) * m)); HIP_CHECK(hipMemcpy(dArow, hArow, sizeof(rocsparse_int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dAcol, hAcol, sizeof(rocsparse_int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dAval, hAval, sizeof(double) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dx, hx, sizeof(double) * n, hipMemcpyHostToDevice)); // Call rocsparse coomv ROCSPARSE_CHECK(rocsparse_dcoomv(handle, rocsparse_operation_none, m, n, nnz, &halpha, descrA, dAval, dArow, dAcol, dx, &hbeta, dy)); // Copy back to host double hy[4]; HIP_CHECK(hipMemcpy(hy, dy, sizeof(double) * m, hipMemcpyDeviceToHost)); std::cout << "hy" << std::endl; for(size_t i = 0; i < 4; i++) { std::cout << hy[i] << " "; } std::cout << "" << std::endl; // Clear up on device HIP_CHECK(hipFree(dArow)); HIP_CHECK(hipFree(dAcol)); HIP_CHECK(hipFree(dAval)); HIP_CHECK(hipFree(dx)); HIP_CHECK(hipFree(dy)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descrA)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); return 0; }


Note

This function does not produce deterministic results when A is transposed.

Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**trans**–**[in]**matrix operation type.**m**–**[in]**number of rows of the sparse COO matrix.**n**–**[in]**number of columns of the sparse COO matrix.**nnz**–**[in]**number of non-zero entries of the sparse COO matrix.**alpha**–**[in]**scalar \(\alpha\).**descr**–**[in]**descriptor of the sparse COO matrix. Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**coo_val**–**[in]**array of`nnz`

elements of the sparse COO matrix.**coo_row_ind**–**[in]**array of`nnz`

elements containing the row indices of the sparse COO matrix.**coo_col_ind**–**[in]**array of`nnz`

elements containing the column indices of the sparse COO matrix.**x**–**[in]**array of`n`

elements ( \(op(A) = A\)) or`m`

elements ( \(op(A) = A^T\) or \(op(A) = A^H\)).**beta**–**[in]**scalar \(\beta\).**y**–**[inout]**array of`m`

elements ( \(op(A) = A\)) or`n`

elements ( \(op(A) = A^T\) or \(op(A) = A^H\)).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`n`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`alpha`

,`coo_val`

,`coo_row_ind`

,`coo_col_ind`

,`x`

,`beta`

or`y`

pointer is invalid.**rocsparse_status_arch_mismatch**– the device is not supported.**rocsparse_status_not_implemented**–[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_csrmv_analysis()[#](#rocsparse-csrmv-analysis)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scsrmv_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info)[#](#_CPPv425rocsparse_scsrmv_analysis16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_info)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcsrmv_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info)[#](#_CPPv425rocsparse_dcsrmv_analysis16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_info)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccsrmv_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info)[#](#_CPPv425rocsparse_ccsrmv_analysis16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_info)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcsrmv_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info)[#](#_CPPv425rocsparse_zcsrmv_analysis16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_info) `rocsparse_csrmv_analysis`

performs the analysis step for[rocsparse_Xcsrmv()](#rocsparse__csrmv_8h_1ac44c0132336667a508d00c66370360ce). It is expected that this function will be executed only once for a given sparsity pattern and particular operation type. The gathered analysis meta data is stored in the[rocsparse_mat_info](types.html#rocsparse-types_8h_1a3347be72f6e4f3c55318c32b46dcaa92)object and can be cleared by[rocsparse_csrmv_clear()](#rocsparse__csrmv_8h_1adecf52ee38f94e04379a5c0c90b066fd).If the matrix sparsity pattern changes, the gathered information will become invalid. In order to perform another sparse matrix multiplication with a matrix having a different sparsity pattern, the user would need to either destroy the old

`info`

object and create a new one or the user would need to clear the existing info object using[rocsparse_csrmv_clear()](#rocsparse__csrmv_8h_1adecf52ee38f94e04379a5c0c90b066fd). In both cases, the analysis will need to be called again.Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**trans**–**[in]**matrix operation type.**m**–**[in]**number of rows of the sparse CSR matrix.**n**–**[in]**number of columns of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**descr**–**[in]**descriptor of the sparse CSR matrix.**csr_val**–**[in]**array of`nnz`

elements of the sparse CSR matrix.**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csr_col_ind**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**info**–**[out]**structure that holds the information collected during the analysis step.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`n`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`csr_val`

,`csr_row_ptr`

,`csr_col_ind`

or`info`

pointer is invalid.**rocsparse_status_memory_error**– the buffer for the gathered information could not be allocated.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_not_implemented**– if[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)is not one of[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03),[rocsparse_matrix_type_symmetric](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8340a3909d43b5b6bedd8ecc928605a5), or[rocsparse_matrix_type_triangular](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a73d9ef5e5e18209f9f10a5885d3e15ba).



## rocsparse_csrmv()[#](#rocsparse-csrmv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scsrmv([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const float *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, const float *x, const float *beta, float *y)[#](#_CPPv416rocsparse_scsrmv16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoPKfPKfPf)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcsrmv([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const double *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, const double *x, const double *beta, double *y)[#](#_CPPv416rocsparse_dcsrmv16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKdK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoPKdPKdPd)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccsrmv([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*x, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*beta,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*y)[#](#_CPPv416rocsparse_ccsrmv16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPK23rocsparse_float_complexK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoPK23rocsparse_float_complexPK23rocsparse_float_complexP23rocsparse_float_complex)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcsrmv([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*x, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*beta,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*y)[#](#_CPPv416rocsparse_zcsrmv16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPK24rocsparse_double_complexK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoPK24rocsparse_double_complexPK24rocsparse_double_complexP24rocsparse_double_complex) Sparse matrix vector multiplication using CSR storage format.

`rocsparse_csrmv`

multiplies the scalar \(\alpha\) with a sparse \(m \times n\) matrix, defined in CSR storage format, and the dense vector \(x\) and adds the result to the dense vector \(y\) that is multiplied by the scalar \(\beta\), such that\[ y := \alpha \cdot op(A) \cdot x + \beta \cdot y, \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if trans == rocsparse_operation_none} \\ A^T, & \text{if trans == rocsparse_operation_transpose} \\ A^H, & \text{if trans == rocsparse_operation_conjugate_transpose} \end{array} \right. \end{split}\]The

`info`

parameter is optional and contains information collected by[rocsparse_Xcsrmv_analysis()](#rocsparse__csrmv_8h_1a997deb1ff1d2fb7969f63bb1ab471cf8). If present, the information will be used to speed up the`csrmv`

computation. If`info`

==`NULL`

, a general`csrmv`

routine will be used instead. Running with analysis may result in better performance when computing the matrix vector product but will also incur a performance cost attributed to the additional analysis step. For this reason, running with analysis makes sense when a user plans on computing the matrix vector product many times and therefore can amortize the analysis cost.for(i = 0; i < m; ++i) { y[i] = beta * y[i]; for(j = csr_row_ptr[i]; j < csr_row_ptr[i + 1]; ++j) { y[i] = y[i] + alpha * csr_val[j] * x[csr_col_ind[j]]; } }

To run without analysis, performing the above operation involves simply calling the

`rocsparse_csrmv`

routine while passing`NULL`

for the`info`

parameter.To run with analysis, completing the sparse matrix vector multiplication involves two steps. First, the user creates a

[rocsparse_mat_info](types.html#rocsparse-types_8h_1a3347be72f6e4f3c55318c32b46dcaa92)object by calling[rocsparse_create_mat_info](auxiliary.html#rocsparse-auxiliary_8h_1a23eb2202356ebb8506136b4898abdeaf)and then passes this to[rocsparse_Xcsrmv_analysis()](#rocsparse__csrmv_8h_1a997deb1ff1d2fb7969f63bb1ab471cf8)which will perform analysis on the sparsity pattern of the matrix \(op(A)\). The user then completes the operation by calling`rocsparse_csrmv`

. The creation of the`info`

object and the call to the analysis routine only need to be performed once for a given sparsity pattern while the computation can be performed repeatedly as long as the sparsity pattern has not changed. Once all calls to`rocsparse_csrmv`

have been made, the`info`

object can be destroyed with a call to[rocsparse_destroy_mat_info](auxiliary.html#rocsparse-auxiliary_8h_1a9c143f65076a10ebafcffc633ad5d87b).When running with analysis, a user may find themselves in the situation where they wish to perform multiple sparse matrix multiplications with each sparse matrix having a different sparsity pattern. Instead of creating and destroying multiple

[rocsparse_mat_info](types.html#rocsparse-types_8h_1a3347be72f6e4f3c55318c32b46dcaa92)objects for each unique sparsity pattern, the user can instead create the`info`

object once and then call[rocsparse_csrmv_clear](#rocsparse__csrmv_8h_1adecf52ee38f94e04379a5c0c90b066fd)followed by re-running the analysis in between each sparse matrix multiplication.**Example**This example performs a sparse matrix vector multiplication in CSR format using additional meta data to improve performance.

int main() { // 1 2 3 0 0 // 0 0 0 0 3 // 2 1 0 0 1 // 0 0 3 4 0 int m = 4; int n = 5; float alpha = 1.0f; float beta = -1.0f; std::vector<int> hcsr_row_ptr = {0, 3, 4, 7, 9}; std::vector<int> hcsr_col_ind = {0, 1, 2, 4, 0, 1, 4, 2, 3}; std::vector<float> hcsr_val = {1.0f, 2.0f, 3.0f, 3.0f, 2.0f, 1.0f, 1.0f, 3.0f, 4.0f}; std::vector<float> hx(n, 1.0f); std::vector<float> hy(m, 1.0f); int nnz = hcsr_row_ptr[m] - hcsr_row_ptr[0]; int* dcsr_row_ptr; int* dcsr_col_ind; float* dcsr_val; float* dx; float* dy; HIP_CHECK(hipMalloc(&dcsr_row_ptr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc(&dcsr_col_ind, sizeof(int) * nnz)); HIP_CHECK(hipMalloc(&dcsr_val, sizeof(float) * nnz)); HIP_CHECK(hipMalloc(&dx, sizeof(float) * n)); HIP_CHECK(hipMalloc(&dy, sizeof(float) * m)); HIP_CHECK( hipMemcpy(dcsr_row_ptr, hcsr_row_ptr.data(), sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsr_col_ind, hcsr_col_ind.data(), sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsr_val, hcsr_val.data(), sizeof(float) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dx, hx.data(), sizeof(float) * n, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dy, hy.data(), sizeof(float) * m, hipMemcpyHostToDevice)); // Create rocSPARSE handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Create matrix descriptor rocsparse_mat_descr descr; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr)); // Create matrix info structure rocsparse_mat_info info; ROCSPARSE_CHECK(rocsparse_create_mat_info(&info)); // Perform analysis step to obtain meta data ROCSPARSE_CHECK(rocsparse_scsrmv_analysis(handle, rocsparse_operation_none, m, n, nnz, descr, dcsr_val, dcsr_row_ptr, dcsr_col_ind, info)); // Compute y = Ax ROCSPARSE_CHECK(rocsparse_scsrmv(handle, rocsparse_operation_none, m, n, nnz, &alpha, descr, dcsr_val, dcsr_row_ptr, dcsr_col_ind, info, dx, &beta, dy)); HIP_CHECK(hipMemcpy(hy.data(), dy, sizeof(float) * m, hipMemcpyDeviceToHost)); std::cout << "hy" << std::endl; for(size_t i = 0; i < hy.size(); i++) { std::cout << hy[i] << " "; } std::cout << "" << std::endl; // Clean up ROCSPARSE_CHECK(rocsparse_destroy_mat_info(info)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); // Clear up on device HIP_CHECK(hipFree(dcsr_row_ptr)); HIP_CHECK(hipFree(dcsr_col_ind)); HIP_CHECK(hipFree(dcsr_val)); HIP_CHECK(hipFree(dx)); HIP_CHECK(hipFree(dy)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**trans**–**[in]**matrix operation type.**m**–**[in]**number of rows of the sparse CSR matrix.**n**–**[in]**number of columns of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**alpha**–**[in]**scalar \(\alpha\).**descr**–**[in]**descriptor of the sparse CSR matrix. Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**csr_val**–**[in]**array of`nnz`

elements of the sparse CSR matrix.**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csr_col_ind**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**info**–**[in]**information collected by[rocsparse_Xcsrmv_analysis()](#rocsparse__csrmv_8h_1a997deb1ff1d2fb7969f63bb1ab471cf8), can be`NULL`

if no information is available.**x**–**[in]**array of`n`

elements ( \(op(A) == A\)) or`m`

elements ( \(op(A) == A^T\) or \(op(A) == A^H\)).**beta**–**[in]**scalar \(\beta\).**y**–**[inout]**array of`m`

elements ( \(op(A) == A\)) or`n`

elements ( \(op(A) == A^T\) or \(op(A) == A^H\)).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`n`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`alpha`

,`csr_val`

,`csr_row_ptr`

,`csr_col_ind`

,`x`

,`beta`

or`y`

pointer is invalid.**rocsparse_status_arch_mismatch**– the device is not supported.**rocsparse_status_not_implemented**–[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_csrmv_analysis_clear()[#](#rocsparse-csrmv-analysis-clear)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_csrmv_clear([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info)[#](#_CPPv421rocsparse_csrmv_clear16rocsparse_handle18rocsparse_mat_info) `rocsparse_csrmv_clear`

deallocates all memory that was allocated by[rocsparse_Xcsrmv_analysis()](#rocsparse__csrmv_8h_1a997deb1ff1d2fb7969f63bb1ab471cf8). This is especially useful, if memory is an issue and the analysis data is not required anymore for further computation, e.g. when switching to another sparse matrix format.Note

Calling

`rocsparse_csrmv_clear`

is optional. All allocated resources will be cleared, when the opaque[rocsparse_mat_info](types.html#rocsparse-types_8h_1a3347be72f6e4f3c55318c32b46dcaa92)object is destroyed using[rocsparse_destroy_mat_info()](auxiliary.html#rocsparse-auxiliary_8h_1a9c143f65076a10ebafcffc633ad5d87b).Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**info**–**[inout]**structure that holds the information collected during analysis step.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`info`

pointer is invalid.**rocsparse_status_memory_error**– the buffer for the gathered information could not be deallocated.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_csrsv_zero_pivot()[#](#rocsparse-csrsv-zero-pivot)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_csrsv_zero_pivot([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_int](types.html#_CPPv413rocsparse_int)*position)[#](#_CPPv426rocsparse_csrsv_zero_pivot16rocsparse_handleK19rocsparse_mat_descr18rocsparse_mat_infoP13rocsparse_int) `rocsparse_csrsv_zero_pivot`

returns[rocsparse_status_zero_pivot](enumerations.html#rocsparse-types_8h_1a578f8c5c1b08f358bf4605b0031006a8a01fe264830c8ce6451ce6888bc8d3e80), if either a structural or numerical zero has been found during[rocsparse_Xcsrsv_solve()](#rocsparse__csrsv_8h_1a897426990ac53e10da95bf0953e0c0aa)computation. The first zero pivot \(j\) at \(A_{j,j}\) is stored in`position`

, using same index base as the CSR matrix.`position`

can be in host or device memory. If no zero pivot has been found,`position`

is set to -1 and[rocsparse_status_success](enumerations.html#rocsparse-types_8h_1a578f8c5c1b08f358bf4605b0031006a8a96462a9361cfceb6cf9354e10fdc671b)is returned instead.Note

`rocsparse_csrsv_zero_pivot`

is a blocking function. It might influence performance negatively.Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**descr**–**[in]**descriptor of the sparse CSR matrix.**info**–**[in]**structure that holds the information collected during the analysis step.**position**–**[inout]**pointer to zero pivot \(j\), can be in host or device memory.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`info`

or`position`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_zero_pivot**– zero pivot has been found.



## rocsparse_csrsv_buffer_size()[#](#rocsparse-csrsv-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scsrsv_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, size_t *buffer_size)[#](#_CPPv428rocsparse_scsrsv_buffer_size16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcsrsv_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, size_t *buffer_size)[#](#_CPPv428rocsparse_dcsrsv_buffer_size16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccsrsv_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, size_t *buffer_size)[#](#_CPPv428rocsparse_ccsrsv_buffer_size16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcsrsv_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, size_t *buffer_size)[#](#_CPPv428rocsparse_zcsrsv_buffer_size16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoP6size_t) `rocsparse_csrsv_buffer_size`

returns the size of the temporary storage buffer that is required by[rocsparse_Xcsrsv_analysis()](#rocsparse__csrsv_8h_1af710dcbc752ca8203389907bcbe74273)and[rocsparse_Xcsrsv_solve()](#rocsparse__csrsv_8h_1a897426990ac53e10da95bf0953e0c0aa). The temporary storage buffer must be allocated by the user. The size of the temporary storage buffer is identical to the size returned by[rocsparse_Xcsrilu0_buffer_size()](precond.html#rocsparse__csrilu0_8h_1a75eebaa5a02b9f1f9a05ff440ceef387)if the matrix sparsity pattern is identical. The user allocated buffer can thus be shared between subsequent calls to those functions.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**trans**–**[in]**matrix operation type.**m**–**[in]**number of rows of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**descr**–**[in]**descriptor of the sparse CSR matrix.**csr_val**–**[in]**array of`nnz`

elements of the sparse CSR matrix.**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csr_col_ind**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**info**–**[out]**structure that holds the information collected during the analysis step.**buffer_size**–**[out]**number of bytes of the temporary storage buffer required by[rocsparse_Xcsrsv_analysis()](#rocsparse__csrsv_8h_1af710dcbc752ca8203389907bcbe74273)and[rocsparse_Xcsrsv_solve()](#rocsparse__csrsv_8h_1a897426990ac53e10da95bf0953e0c0aa).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`csr_val`

,`csr_row_ptr`

,`csr_col_ind`

,`info`

or`buffer_size`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_not_implemented**–`trans`

==[rocsparse_operation_conjugate_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a6920c1aa5f80005eee4b66ea6f25330f)or[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_csrsv_analysis()[#](#rocsparse-csrsv-analysis)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scsrsv_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_analysis_policy](enumerations.html#_CPPv425rocsparse_analysis_policy)analysis,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)solve, void *temp_buffer)[#](#_CPPv425rocsparse_scsrsv_analysis16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcsrsv_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_analysis_policy](enumerations.html#_CPPv425rocsparse_analysis_policy)analysis,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)solve, void *temp_buffer)[#](#_CPPv425rocsparse_dcsrsv_analysis16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccsrsv_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_analysis_policy](enumerations.html#_CPPv425rocsparse_analysis_policy)analysis,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)solve, void *temp_buffer)[#](#_CPPv425rocsparse_ccsrsv_analysis16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcsrsv_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_analysis_policy](enumerations.html#_CPPv425rocsparse_analysis_policy)analysis,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)solve, void *temp_buffer)[#](#_CPPv425rocsparse_zcsrsv_analysis16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv) `rocsparse_csrsv_analysis`

performs the analysis step for[rocsparse_Xcsrsv_solve()](#rocsparse__csrsv_8h_1a897426990ac53e10da95bf0953e0c0aa). It is expected that this function will be executed only once for a given matrix and particular operation type. The analysis meta data can be cleared by[rocsparse_csrsv_clear()](#rocsparse__csrsv_8h_1adda3029d2877011cd72b9a2d127b3f7f).If the matrix sparsity pattern changes, the gathered information will become invalid. In order to perform another sparse triangular solve with a matrix having a different sparsity pattern, the user would need to either destroy the old

`info`

object and create a new one or the user would need to clear the existing`info`

object using[rocsparse_csrsv_clear()](#rocsparse__csrsv_8h_1adda3029d2877011cd72b9a2d127b3f7f). In both cases, the analysis will need to be called again.`rocsparse_csrsv_analysis`

can share its meta data with[rocsparse_Xcsrsm_analysis()](level3.html#rocsparse__csrsm_8h_1ac8e943e992641859efdfea49a267133b),[rocsparse_Xcsrilu0_analysis()](precond.html#rocsparse__csrilu0_8h_1a8b0496cb644c23fe65176e70315e431c)and[rocsparse_Xcsric0_analysis()](precond.html#rocsparse__csric0_8h_1a00bf19a537e0d46b1c55826a9c23e23c). Selecting[rocsparse_analysis_policy_reuse](enumerations.html#rocsparse-types_8h_1a43b20aa4bb19623a91b5952422fbe35ca658466413f4005c0c103d20d5e352078)policy can greatly improve computation performance of meta data. However, the user needs to make sure that the sparsity pattern remains unchanged. If this cannot be assured,[rocsparse_analysis_policy_force](enumerations.html#rocsparse-types_8h_1a43b20aa4bb19623a91b5952422fbe35cac66b70c4f519ddd03dcbe0f3a973401a)has to be used.Note

If the matrix sparsity pattern changes, the gathered information will become invalid.

Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**trans**–**[in]**matrix operation type.**m**–**[in]**number of rows of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**descr**–**[in]**descriptor of the sparse CSR matrix.**csr_val**–**[in]**array of`nnz`

elements of the sparse CSR matrix.**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csr_col_ind**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**info**–**[out]**structure that holds the information collected during the analysis step.**analysis**–**[in]**[rocsparse_analysis_policy_reuse](enumerations.html#rocsparse-types_8h_1a43b20aa4bb19623a91b5952422fbe35ca658466413f4005c0c103d20d5e352078)or[rocsparse_analysis_policy_force](enumerations.html#rocsparse-types_8h_1a43b20aa4bb19623a91b5952422fbe35cac66b70c4f519ddd03dcbe0f3a973401a).**solve**–**[in]**[rocsparse_solve_policy_auto](enumerations.html#rocsparse-types_8h_1a5a3e261123e81a9e8b267c6109e26957a9c6bdf97e192d429ca536d5ab98ea866).**temp_buffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`csr_row_ptr`

,`csr_col_ind`

,`info`

or`temp_buffer`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_not_implemented**–`trans`

==[rocsparse_operation_conjugate_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a6920c1aa5f80005eee4b66ea6f25330f)or[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_csrsv_solve()[#](#rocsparse-csrsv-solve)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scsrsv_solve([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const float *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, const float *x, float *y,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv422rocsparse_scsrsv_solve16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoPKfPf22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcsrsv_solve([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const double *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, const double *x, double *y,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv422rocsparse_dcsrsv_solve16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_intPKdK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoPKdPd22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccsrsv_solve([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*x,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*y,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv422rocsparse_ccsrsv_solve16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_intPK23rocsparse_float_complexK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoPK23rocsparse_float_complexP23rocsparse_float_complex22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcsrsv_solve([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*x,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*y,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv422rocsparse_zcsrsv_solve16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_intPK24rocsparse_double_complexK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoPK24rocsparse_double_complexP24rocsparse_double_complex22rocsparse_solve_policyPv) Sparse triangular solve using CSR storage format.

`rocsparse_csrsv_solve`

solves a sparse triangular linear system of a sparse \(m \times m\) matrix, defined in CSR storage format, a dense solution vector \(y\) and the right-hand side \(x\) that is multiplied by \(\alpha\), such that\[ op(A) \cdot y = \alpha \cdot x, \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if trans == rocsparse_operation_none} \\ A^T, & \text{if trans == rocsparse_operation_transpose} \\ A^H, & \text{if trans == rocsparse_operation_conjugate_transpose} \end{array} \right. \end{split}\]Performing the above operation requires three steps. First, the user calls

[rocsparse_Xcsrsv_buffer_size()](#rocsparse__csrsv_8h_1ac74b51be59a42a0387648ac79d633b5e)which will determine the size of the required temporary storage buffer. The user then allocates this buffer and calls[rocsparse_Xcsrsv_analysis()](#rocsparse__csrsv_8h_1af710dcbc752ca8203389907bcbe74273)which will perform analysis on the sparse matrix \(op(A)\). Finally, the user completes the computation by calling`rocsparse_csrsv_solve`

. The buffer size, buffer allocation, and analysis only need to be called once for a given sparse matrix \(op(A)\) while the computation stage can be repeatedly used with different \(x\) and \(y\) vectors. Once all calls to`rocsparse_csrsv_solve`

are complete, the temporary buffer can be deallocated.Solving a triangular system involves division by the diagonal elements. This means that if the sparse matrix is missing the diagonal entry (referred to as a structural zero) or the diagonal entry is zero (referred to as a numerical zero) then a division by zero would occur.

`rocsparse_csrsv_solve`

tracks the location of the first zero pivot (either numerical or structural zero). The zero pivot status can be checked calling[rocsparse_csrsv_zero_pivot()](#rocsparse__csrsv_8h_1ab7299bb98431dfa85798fa5c082e34b4). If[rocsparse_csrsv_zero_pivot()](#rocsparse__csrsv_8h_1ab7299bb98431dfa85798fa5c082e34b4)returns[rocsparse_status_success](enumerations.html#rocsparse-types_8h_1a578f8c5c1b08f358bf4605b0031006a8a96462a9361cfceb6cf9354e10fdc671b), then no zero pivot was found and therefore the matrix does not have a structural or numerical zero.The user can specify that the sparse matrix should be interpreted as having ones on the diagonal by setting the diagonal type on the descriptor

`descr`

to[rocsparse_diag_type_unit](enumerations.html#rocsparse-types_8h_1a6e8e038adcd3fa03168a1cb4a7da1bc5ac14545fb3bf8773d5f6b8e258c9576f4)using[rocsparse_set_mat_diag_type](auxiliary.html#rocsparse-auxiliary_8h_1a61f894d80e4da74c7e8cd43f61f9215c). If[rocsparse_diag_type](enumerations.html#rocsparse-types_8h_1a6e8e038adcd3fa03168a1cb4a7da1bc5)==[rocsparse_diag_type_unit](enumerations.html#rocsparse-types_8h_1a6e8e038adcd3fa03168a1cb4a7da1bc5ac14545fb3bf8773d5f6b8e258c9576f4), no zero pivot will be reported, even if \(A_{j,j} = 0\) for some \(j\).The sparse CSR matrix passed to

`rocsparse_csrsv_solve`

does not actually have to be a triangular matrix. Instead the triangular upper or lower part of the sparse matrix is solved based on[rocsparse_fill_mode](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1)set on the descriptor`descr`

. If the fill mode is set to[rocsparse_fill_mode_lower](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a1eb644f6f2701329635e07d91919d37e), then the lower triangular matrix is solved. If the fill mode is set to[rocsparse_fill_mode_upper](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a905f490c7fc5a59e8a635938cec0d004)then the upper triangular matrix is solved.**Example**Consider the lower triangular \(m \times m\) matrix \(L\), stored in CSR storage format with unit diagonal. The following example solves \(L \cdot y = x\).

int main() { // 2 1 0 0 // A = 1 2 1 0 // 0 1 2 1 // 0 0 1 2 int m = 4; int n = 4; int nnz = 10; double alpha = 1.0; std::vector<int> hcsr_row_ptr = {0, 2, 5, 8, 10}; std::vector<int> hcsr_col_ind = {0, 1, 0, 1, 2, 1, 2, 3, 2, 3}; std::vector<double> hcsr_val = {2.0, 1.0, 1.0, 2.0, 1.0, 1.0, 2.0, 1.0, 1.0, 2.0}; std::vector<double> hx(m, 1.0); std::vector<double> hy(m); int* dcsr_row_ptr; int* dcsr_col_ind; double* dcsr_val; double* dx; double* dy; HIP_CHECK(hipMalloc(&dcsr_row_ptr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc(&dcsr_col_ind, sizeof(int) * nnz)); HIP_CHECK(hipMalloc(&dcsr_val, sizeof(double) * nnz)); HIP_CHECK(hipMalloc(&dx, sizeof(double) * m)); HIP_CHECK(hipMalloc(&dy, sizeof(double) * m)); HIP_CHECK( hipMemcpy(dcsr_row_ptr, hcsr_row_ptr.data(), sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsr_col_ind, hcsr_col_ind.data(), sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsr_val, hcsr_val.data(), sizeof(double) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dx, hx.data(), sizeof(double) * m, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dy, hy.data(), sizeof(double) * m, hipMemcpyHostToDevice)); // Create rocSPARSE handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Create matrix descriptor rocsparse_mat_descr descr; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr)); ROCSPARSE_CHECK(rocsparse_set_mat_fill_mode(descr, rocsparse_fill_mode_lower)); ROCSPARSE_CHECK(rocsparse_set_mat_diag_type(descr, rocsparse_diag_type_non_unit)); // Create matrix info structure rocsparse_mat_info info; ROCSPARSE_CHECK(rocsparse_create_mat_info(&info)); // Obtain required buffer size size_t buffer_size; ROCSPARSE_CHECK(rocsparse_dcsrsv_buffer_size(handle, rocsparse_operation_none, m, nnz, descr, dcsr_val, dcsr_row_ptr, dcsr_col_ind, info, &buffer_size)); // Allocate temporary buffer void* temp_buffer; HIP_CHECK(hipMalloc(&temp_buffer, buffer_size)); // Perform analysis step ROCSPARSE_CHECK(rocsparse_dcsrsv_analysis(handle, rocsparse_operation_none, m, nnz, descr, dcsr_val, dcsr_row_ptr, dcsr_col_ind, info, rocsparse_analysis_policy_reuse, rocsparse_solve_policy_auto, temp_buffer)); // Solve Ly = x ROCSPARSE_CHECK(rocsparse_dcsrsv_solve(handle, rocsparse_operation_none, m, nnz, &alpha, descr, dcsr_val, dcsr_row_ptr, dcsr_col_ind, info, dx, dy, rocsparse_solve_policy_auto, temp_buffer)); HIP_CHECK(hipMemcpy(hy.data(), dy, sizeof(double) * m, hipMemcpyDeviceToHost)); std::cout << "hy" << std::endl; for(size_t i = 0; i < hy.size(); i++) { std::cout << hy[i] << " "; } std::cout << "" << std::endl; // Clean up ROCSPARSE_CHECK(rocsparse_destroy_mat_info(info)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); HIP_CHECK(hipFree(dcsr_row_ptr)); HIP_CHECK(hipFree(dcsr_col_ind)); HIP_CHECK(hipFree(dcsr_val)); HIP_CHECK(hipFree(temp_buffer)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

Currently, only

`trans`

==[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528)and`trans`

==[rocsparse_operation_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a1ea3194d0c7bdb9e500d6faeead8ebf5)is supported.Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**trans**–**[in]**matrix operation type.**m**–**[in]**number of rows of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**alpha**–**[in]**scalar \(\alpha\).**descr**–**[in]**descriptor of the sparse CSR matrix.**csr_val**–**[in]**array of`nnz`

elements of the sparse CSR matrix.**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csr_col_ind**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**info**–**[in]**structure that holds the information collected during the analysis step.**x**–**[in]**array of`m`

elements, holding the right-hand side.**y**–**[out]**array of`m`

elements, holding the solution.**policy**–**[in]**[rocsparse_solve_policy_auto](enumerations.html#rocsparse-types_8h_1a5a3e261123e81a9e8b267c6109e26957a9c6bdf97e192d429ca536d5ab98ea866).**temp_buffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`alpha`

,`csr_val`

,`csr_row_ptr`

,`csr_col_ind`

,`x`

or`y`

pointer is invalid.**rocsparse_status_arch_mismatch**– the device is not supported.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_not_implemented**–`trans`

==[rocsparse_operation_conjugate_transpose](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0a6920c1aa5f80005eee4b66ea6f25330f)or[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_csrsv_clear()[#](#rocsparse-csrsv-clear)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_csrsv_clear([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info)[#](#_CPPv421rocsparse_csrsv_clear16rocsparse_handleK19rocsparse_mat_descr18rocsparse_mat_info) `rocsparse_csrsv_clear`

deallocates all memory that was allocated by[rocsparse_Xcsrsv_analysis()](#rocsparse__csrsv_8h_1af710dcbc752ca8203389907bcbe74273). This is especially useful, if memory is an issue and the analysis data is not required for further computation, e.g. when switching to another sparse matrix format.Calling

`rocsparse_csrsv_clear`

is optional. All allocated resources will be cleared when the opaque[rocsparse_mat_info](types.html#rocsparse-types_8h_1a3347be72f6e4f3c55318c32b46dcaa92)struct is destroyed using[rocsparse_destroy_mat_info()](auxiliary.html#rocsparse-auxiliary_8h_1a9c143f65076a10ebafcffc633ad5d87b).Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**descr**–**[in]**descriptor of the sparse CSR matrix.**info**–**[inout]**structure that holds the information collected during the analysis step.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`info`

pointer is invalid.**rocsparse_status_memory_error**– the buffer holding the meta data could not be deallocated.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_csritsv_zero_pivot()[#](#rocsparse-csritsv-zero-pivot)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_csritsv_zero_pivot([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_int](types.html#_CPPv413rocsparse_int)*position)[#](#_CPPv428rocsparse_csritsv_zero_pivot16rocsparse_handleK19rocsparse_mat_descr18rocsparse_mat_infoP13rocsparse_int) `rocsparse_csritsv_zero_pivot`

returns[rocsparse_status_zero_pivot](enumerations.html#rocsparse-types_8h_1a578f8c5c1b08f358bf4605b0031006a8a01fe264830c8ce6451ce6888bc8d3e80), if either a structural or numerical zero has been found during[rocsparse_Xcsritsv_solve()](#rocsparse__csritsv_8h_1a9832644a9f76260c65be9a6f5f3e2f19)and/or[rocsparse_Xcsritsv_analysis()](#rocsparse__csritsv_8h_1af5d00a0a8877c2ef2ae06219d3d5eec2), execution. The first zero pivot \(j\) at \(A_{j,j}\) is stored in`position`

, using same index base as the CSR matrix.`position`

can be in host or device memory. If no zero pivot has been found,`position`

is set to -1 and[rocsparse_status_success](enumerations.html#rocsparse-types_8h_1a578f8c5c1b08f358bf4605b0031006a8a96462a9361cfceb6cf9354e10fdc671b)is returned instead.Note

`rocsparse_csritsv_zero_pivot`

is a blocking function. It might influence performance negatively.Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**descr**–**[in]**descriptor of the sparse CSR matrix.**info**–**[in]**structure that holds the information collected during the analysis step.**position**–**[inout]**pointer to zero pivot \(j\), can be in host or device memory.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`info`

or`position`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_zero_pivot**– zero pivot has been found.



## rocsparse_csritsv_buffer_size()[#](#rocsparse-csritsv-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scsritsv_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, size_t *buffer_size)[#](#_CPPv430rocsparse_scsritsv_buffer_size16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcsritsv_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, size_t *buffer_size)[#](#_CPPv430rocsparse_dcsritsv_buffer_size16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccsritsv_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, size_t *buffer_size)[#](#_CPPv430rocsparse_ccsritsv_buffer_size16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcsritsv_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, size_t *buffer_size)[#](#_CPPv430rocsparse_zcsritsv_buffer_size16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoP6size_t) `rocsparse_csritsv_buffer_size`

returns the size of the temporary storage buffer that is required by[rocsparse_Xcsritsv_analysis()](#rocsparse__csritsv_8h_1af5d00a0a8877c2ef2ae06219d3d5eec2)and[rocsparse_Xcsritsv_solve()](#rocsparse__csritsv_8h_1a9832644a9f76260c65be9a6f5f3e2f19). The temporary storage buffer must be allocated by the user.Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**trans**–**[in]**matrix operation type.**m**–**[in]**number of rows of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**descr**–**[in]**descriptor of the sparse CSR matrix.**csr_val**–**[in]**array of`nnz`

elements of the sparse CSR matrix.**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csr_col_ind**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**info**–**[out]**structure that holds the information collected during the analysis step.**buffer_size**–**[out]**number of bytes of the temporary storage buffer required by[rocsparse_Xcsritsv_analysis()](#rocsparse__csritsv_8h_1af5d00a0a8877c2ef2ae06219d3d5eec2)and[rocsparse_Xcsritsv_solve()](#rocsparse__csritsv_8h_1a9832644a9f76260c65be9a6f5f3e2f19).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`csr_val`

,`csr_row_ptr`

,`csr_col_ind`

,`info`

or`buffer_size`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_not_implemented**–[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)and[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_triangular](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a73d9ef5e5e18209f9f10a5885d3e15ba).



## rocsparse_csritsv_analysis()[#](#rocsparse-csritsv-analysis)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scsritsv_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_analysis_policy](enumerations.html#_CPPv425rocsparse_analysis_policy)analysis,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)solve, void *temp_buffer)[#](#_CPPv427rocsparse_scsritsv_analysis16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcsritsv_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_analysis_policy](enumerations.html#_CPPv425rocsparse_analysis_policy)analysis,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)solve, void *temp_buffer)[#](#_CPPv427rocsparse_dcsritsv_analysis16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccsritsv_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_analysis_policy](enumerations.html#_CPPv425rocsparse_analysis_policy)analysis,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)solve, void *temp_buffer)[#](#_CPPv427rocsparse_ccsritsv_analysis16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcsritsv_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_analysis_policy](enumerations.html#_CPPv425rocsparse_analysis_policy)analysis,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)solve, void *temp_buffer)[#](#_CPPv427rocsparse_zcsritsv_analysis16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv) `rocsparse_csritsv_analysis`

performs the analysis step for[rocsparse_Xcsritsv_solve()](#rocsparse__csritsv_8h_1a9832644a9f76260c65be9a6f5f3e2f19). It is expected that this function will be executed only once for a given matrix and particular operation type. The analysis meta data can be cleared by[rocsparse_csritsv_clear()](#rocsparse__csritsv_8h_1ac264a33bb653e7712cba4eb1e29cc144).Selecting

[rocsparse_analysis_policy_reuse](enumerations.html#rocsparse-types_8h_1a43b20aa4bb19623a91b5952422fbe35ca658466413f4005c0c103d20d5e352078)policy can greatly improve computation performance of meta data. However, the user needs to make sure that the sparsity pattern remains unchanged. If this cannot be assured,[rocsparse_analysis_policy_force](enumerations.html#rocsparse-types_8h_1a43b20aa4bb19623a91b5952422fbe35cac66b70c4f519ddd03dcbe0f3a973401a)has to be used.Note

If the matrix sparsity pattern changes, the gathered information will become invalid.

Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**trans**–**[in]**matrix operation type.**m**–**[in]**number of rows of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**descr**–**[in]**descriptor of the sparse CSR matrix.**csr_val**–**[in]**array of`nnz`

elements of the sparse CSR matrix.**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csr_col_ind**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**info**–**[out]**structure that holds the information collected during the analysis step.**analysis**–**[in]**[rocsparse_analysis_policy_reuse](enumerations.html#rocsparse-types_8h_1a43b20aa4bb19623a91b5952422fbe35ca658466413f4005c0c103d20d5e352078)or[rocsparse_analysis_policy_force](enumerations.html#rocsparse-types_8h_1a43b20aa4bb19623a91b5952422fbe35cac66b70c4f519ddd03dcbe0f3a973401a).**solve**–**[in]**[rocsparse_solve_policy_auto](enumerations.html#rocsparse-types_8h_1a5a3e261123e81a9e8b267c6109e26957a9c6bdf97e192d429ca536d5ab98ea866).**temp_buffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`csr_row_ptr`

,`csr_col_ind`

,`info`

or`temp_buffer`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_not_implemented**–[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)and[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_triangular](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a73d9ef5e5e18209f9f10a5885d3e15ba).



## rocsparse_csritsv_solve()[#](#rocsparse-csritsv-solve)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scsritsv_solve([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)*host_nmaxiter, const float *host_tol, float *host_history,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const float *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, const float *x, float *y,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv424rocsparse_scsritsv_solve16rocsparse_handleP13rocsparse_intPKfPf19rocsparse_operation13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoPKfPf22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcsritsv_solve([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)*host_nmaxiter, const double *host_tol, double *host_history,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const double *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, const double *x, double *y,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv424rocsparse_dcsritsv_solve16rocsparse_handleP13rocsparse_intPKdPd19rocsparse_operation13rocsparse_int13rocsparse_intPKdK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoPKdPd22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccsritsv_solve([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)*host_nmaxiter, const float *host_tol, float *host_history,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*x,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*y,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv424rocsparse_ccsritsv_solve16rocsparse_handleP13rocsparse_intPKfPf19rocsparse_operation13rocsparse_int13rocsparse_intPK23rocsparse_float_complexK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoPK23rocsparse_float_complexP23rocsparse_float_complex22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcsritsv_solve([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)*host_nmaxiter, const double *host_tol, double *host_history,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*x,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*y,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv424rocsparse_zcsritsv_solve16rocsparse_handleP13rocsparse_intPKdPd19rocsparse_operation13rocsparse_int13rocsparse_intPK24rocsparse_double_complexK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoPK24rocsparse_double_complexP24rocsparse_double_complex22rocsparse_solve_policyPv) Sparse iterative triangular solve using CSR storage format.

`rocsparse_csritsv_solve`

solves iteratively with the use of the Jacobi method a sparse triangular linear system of a sparse \(m \times m\) matrix, defined in CSR storage format, a dense solution vector \(y\) and the right-hand side \(x\) that is multiplied by \(\alpha\), such that\[ op(A) y = \alpha x, \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if trans == rocsparse_operation_none} \\ A^T, & \text{if trans == rocsparse_operation_transpose} \\ A^H, & \text{if trans == rocsparse_operation_conjugate_transpose} \end{array} \right. \end{split}\]The Jacobi method applied to the sparse triangular linear system above gives

\[ y_{k+1} = y_{k} + D^{-1} ( \alpha x - (D + T) y_{k} ) \]with \(A = D + T\), \(D\) the diagonal of \(A\) and \(T\) the strict triangular part of \(A\).The above equation can be also written as

\[ y_{k+1} = y_{k} + D^{-1} r_k \]where\[ r_k = \alpha x - (D + T) y_k. \]Starting with \(y_0 = \)`y`

, the method iterates if \( 0 \le k \lt \)`host_nmaxiter`

and if\[ \Vert r_k \Vert_{\infty} \gt \epsilon, \]with \(\epsilon\) =`host_tol`

.`rocsparse_csritsv_solve`

requires a user allocated temporary buffer. Its size is returned by rocsparse_scsritsv_buffer_size “rocsparse_Xcsritsv_buffer_size()”. Furthermore, analysis meta data is required. It can be obtained by[rocsparse_Xcsritsv_analysis()](#rocsparse__csritsv_8h_1af5d00a0a8877c2ef2ae06219d3d5eec2).`rocsparse_csritsv_solve`

reports the first zero pivot (either numerical or structural zero). The zero pivot status can be checked calling[rocsparse_csritsv_zero_pivot()](#rocsparse__csritsv_8h_1a4a3bfad767b754d5fa3aa19127360149). If[rocsparse_diag_type](enumerations.html#rocsparse-types_8h_1a6e8e038adcd3fa03168a1cb4a7da1bc5)==[rocsparse_diag_type_unit](enumerations.html#rocsparse-types_8h_1a6e8e038adcd3fa03168a1cb4a7da1bc5ac14545fb3bf8773d5f6b8e258c9576f4), no zero pivot will be reported, even if \(A_{j,j} = 0\) for some \(j\).**Example**Consider the lower triangular \(m \times m\) matrix \(L\), stored in CSR storage format with unit diagonal. The following example solves \(L \cdot y = x\).

// Create rocSPARSE handle rocsparse_handle handle; rocsparse_create_handle(&handle); // Create matrix descriptor rocsparse_mat_descr descr; rocsparse_create_mat_descr(&descr); rocsparse_set_mat_fill_mode(descr, rocsparse_fill_mode_lower); rocsparse_set_mat_diag_type(descr, rocsparse_diag_type_unit); // Create matrix info structure rocsparse_mat_info info; rocsparse_create_mat_info(&info); // Obtain required buffer size size_t buffer_size; rocsparse_dcsritsv_buffer_size(handle, rocsparse_operation_none, m, nnz, descr, csr_val, csr_row_ptr, csr_col_ind, info, &buffer_size); // Allocate temporary buffer void* temp_buffer; hipMalloc(&temp_buffer, buffer_size); // Perform analysis step rocsparse_dcsritsv_analysis(handle, rocsparse_operation_none, m, nnz, descr, csr_val, csr_row_ptr, csr_col_ind, info, rocsparse_analysis_policy_reuse, rocsparse_solve_policy_auto, temp_buffer); // Solve Ly = x rocsparse_int nmaxiter = 200; rocsparse_int host_maxiter = nmaxiter; double host_tol = 1.0e-4; double host_history[200]; // Initialization of y hipMemset(y, 0, sizeof(double) * m); rocsparse_dcsritsv_solve(handle, &host_maxiter, &host_tol, host_history, rocsparse_operation_none, m, nnz, &alpha, descr, csr_val, csr_row_ptr, csr_col_ind, info, x, y, rocsparse_solve_policy_auto, temp_buffer); if (host_maxiter < nmaxiter) { printf("convergence\n"); } else { printf("no convergence\n"); } for (int i=0;i<=host_maxiter;++i) { printf("iter = %d, nrm inf residual=%e\n", i, host_history[i]); } // No zero pivot should be found, with L having unit diagonal // Clean up hipFree(temp_buffer); rocsparse_destroy_mat_info(info); rocsparse_destroy_mat_descr(descr); rocsparse_destroy_handle(handle);


Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**host_nmaxiter**–**[inout]**maximum number of iterations on input and number of iterations on output. If the output number of iterations is strictly less than the input maximum number of iterations, then the algorithm converged.**host_tol**–**[in]**if the pointer is null then loop will execute`nmaxiter`

[0] iterations.**host_history**–**[out]**optional array to record the norm of the residual before each iteration.**trans**–**[in]**matrix operation type.**m**–**[in]**number of rows of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**alpha**–**[in]**scalar \(\alpha\).**descr**–**[in]**descriptor of the sparse CSR matrix.**csr_val**–**[in]**array of`nnz`

elements of the sparse CSR matrix.**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csr_col_ind**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**info**–**[in]**structure that holds the information collected during the analysis step.**x**–**[in]**array of`m`

elements, holding the right-hand side.**y**–**[inout]**array of`m`

elements, holding the solution.**policy**–**[in]**[rocsparse_solve_policy_auto](enumerations.html#rocsparse-types_8h_1a5a3e261123e81a9e8b267c6109e26957a9c6bdf97e192d429ca536d5ab98ea866).**temp_buffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`alpha`

,`csr_val`

,`csr_row_ptr`

,`csr_col_ind`

,`x`

or`y`

pointer is invalid.**rocsparse_status_arch_mismatch**– the device is not supported.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_not_implemented**–[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)and[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_triangular](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a73d9ef5e5e18209f9f10a5885d3e15ba).



## rocsparse_csritsv_solve_ex()[#](#rocsparse-csritsv-solve-ex)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scsritsv_solve_ex([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)*host_nmaxiter,[rocsparse_int](types.html#_CPPv413rocsparse_int)host_nfreeiter, const float *host_tol, float *host_history,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const float *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, const float *x, float *y,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv427rocsparse_scsritsv_solve_ex16rocsparse_handleP13rocsparse_int13rocsparse_intPKfPf19rocsparse_operation13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoPKfPf22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcsritsv_solve_ex([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)*host_nmaxiter,[rocsparse_int](types.html#_CPPv413rocsparse_int)host_nfreeiter, const double *host_tol, double *host_history,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const double *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, const double *x, double *y,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv427rocsparse_dcsritsv_solve_ex16rocsparse_handleP13rocsparse_int13rocsparse_intPKdPd19rocsparse_operation13rocsparse_int13rocsparse_intPKdK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoPKdPd22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccsritsv_solve_ex([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)*host_nmaxiter,[rocsparse_int](types.html#_CPPv413rocsparse_int)host_nfreeiter, const float *host_tol, float *host_history,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*x,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*y,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv427rocsparse_ccsritsv_solve_ex16rocsparse_handleP13rocsparse_int13rocsparse_intPKfPf19rocsparse_operation13rocsparse_int13rocsparse_intPK23rocsparse_float_complexK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoPK23rocsparse_float_complexP23rocsparse_float_complex22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcsritsv_solve_ex([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)*host_nmaxiter,[rocsparse_int](types.html#_CPPv413rocsparse_int)host_nfreeiter, const double *host_tol, double *host_history,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*x,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*y,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv427rocsparse_zcsritsv_solve_ex16rocsparse_handleP13rocsparse_int13rocsparse_intPKdPd19rocsparse_operation13rocsparse_int13rocsparse_intPK24rocsparse_double_complexK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoPK24rocsparse_double_complexP24rocsparse_double_complex22rocsparse_solve_policyPv) Sparse iterative triangular solve using CSR storage format.

`rocsparse_csritsv_solve_ex`

solves iteratively with the use of the Jacobi method a sparse triangular linear system of a sparse \(m \times m\) matrix, defined in CSR storage format, a dense solution vector \(y\) and the right-hand side \(x\) that is multiplied by \(\alpha\), such that\[ op(A) y = \alpha x, \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if trans == rocsparse_operation_none} \\ A^T, & \text{if trans == rocsparse_operation_transpose} \\ A^H, & \text{if trans == rocsparse_operation_conjugate_transpose} \end{array} \right. \end{split}\]The Jacobi method applied to the sparse triangular linear system above gives

\[ y_{k+1} = y_{k} + D^{-1} ( \alpha x - (D + T) y_{k} ) \]with \(A = D + T\), \(D\) the diagonal of \(A\) and \(T\) the strict triangular part of \(A\).The above equation can be also written as

\[ y_{k+1} = y_{k} + D^{-1} r_k \]where\[ r_k = \alpha x - (D + T) y_k. \]Starting with \(y_0 = \)`y`

, the method iterates if \( 0 \le k \lt \)`host_nmaxiter`

and if\[ \Vert r_k \Vert_{\infty} \gt \epsilon, \]with \(\epsilon\) =`host_tol`

.The parameter

`host_nfreeiter`

is used to control the frequence of the stopping criteria evaluation, thus potentially improving the performance of the algorithm with less norm calculation. Between each iteration of index \( k \),`host_nfreeiter`

are performed without stopping criteria evaluation. Thus, if the convergence is obtained at index \( k \), that means \( (k + 1) \)`host_nfreeiter`

\( + k \) iterations have been performed.`rocsparse_csritsv_solve_ex`

requires a user allocated temporary buffer. Its size is returned by[rocsparse_Xcsritsv_buffer_size()](#rocsparse__csritsv_8h_1a7ccffa5d1a07641e214aa38a47883591). Furthermore, analysis meta data is required. It can be obtained by[rocsparse_Xcsritsv_analysis()](#rocsparse__csritsv_8h_1af5d00a0a8877c2ef2ae06219d3d5eec2).`rocsparse_csritsv_solve_ex`

reports the first zero pivot (either numerical or structural zero). The zero pivot status can be checked calling[rocsparse_csritsv_zero_pivot()](#rocsparse__csritsv_8h_1a4a3bfad767b754d5fa3aa19127360149). If[rocsparse_diag_type](enumerations.html#rocsparse-types_8h_1a6e8e038adcd3fa03168a1cb4a7da1bc5)==[rocsparse_diag_type_unit](enumerations.html#rocsparse-types_8h_1a6e8e038adcd3fa03168a1cb4a7da1bc5ac14545fb3bf8773d5f6b8e258c9576f4), no zero pivot will be reported, even if \(A_{j,j} = 0\) for some \(j\).**Example**Consider the lower triangular \(m \times m\) matrix \(L\), stored in CSR storage format with unit diagonal. The following example solves \(L \cdot y = x\).

// Create rocSPARSE handle rocsparse_handle handle; rocsparse_create_handle(&handle); // Create matrix descriptor rocsparse_mat_descr descr; rocsparse_create_mat_descr(&descr); rocsparse_set_mat_fill_mode(descr, rocsparse_fill_mode_lower); rocsparse_set_mat_diag_type(descr, rocsparse_diag_type_unit); // Create matrix info structure rocsparse_mat_info info; rocsparse_create_mat_info(&info); // Obtain required buffer size size_t buffer_size; rocsparse_dcsritsv_buffer_size(handle, rocsparse_operation_none, m, nnz, descr, csr_val, csr_row_ptr, csr_col_ind, info, &buffer_size); // Allocate temporary buffer void* temp_buffer; hipMalloc(&temp_buffer, buffer_size); // Perform analysis step rocsparse_dcsritsv_analysis(handle, rocsparse_operation_none, m, nnz, descr, csr_val, csr_row_ptr, csr_col_ind, info, rocsparse_analysis_policy_reuse, rocsparse_solve_policy_auto, temp_buffer); // Solve Ly = x rocsparse_int nmaxiter = 200; rocsparse_int host_maxiter = nmaxiter; rocsparse_int host_nfreeiter = 20; double host_tol = 1.0e-4; double host_history[200]; // Initialization of y hipMemset(y, 0, sizeof(double) * m); rocsparse_dcsritsv_solve_ex(handle, &host_maxiter, host_nfreeiter, &host_tol, host_history, rocsparse_operation_none, m, nnz, &alpha, descr, csr_val, csr_row_ptr, csr_col_ind, info, x, y, rocsparse_solve_policy_auto, temp_buffer); if (host_maxiter < nmaxiter) { printf("convergence\n"); } else { printf("no convergence\n"); } for (int i=0;i<=host_maxiter;++i) { printf("iter = %d, nrm inf residual=%e\n", i, host_history[i]); } // No zero pivot should be found, with L having unit diagonal // Clean up hipFree(temp_buffer); rocsparse_destroy_mat_info(info); rocsparse_destroy_mat_descr(descr); rocsparse_destroy_handle(handle);


Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**host_nmaxiter**–**[inout]**maximum number of iterations on input and number of iterations on output. If the output number of iterations is strictly less than the input maximum number of iterations, then the algorithm converged.**host_nfreeiter**–**[in]**number of free iterations, i.e. the number of iterations performed without stopping criteria evaluation between two iterations with stopping criteria evaluation.**host_tol**–**[in]**if the pointer is null then loop will execute`nmaxiter`

[0] iterations.**host_history**–**[out]**optional array to record the norm of the residual before each iteration.**trans**–**[in]**matrix operation type.**m**–**[in]**number of rows of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**alpha**–**[in]**scalar \(\alpha\).**descr**–**[in]**descriptor of the sparse CSR matrix.**csr_val**–**[in]**array of`nnz`

elements of the sparse CSR matrix.**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csr_col_ind**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**info**–**[in]**structure that holds the information collected during the analysis step.**x**–**[in]**array of`m`

elements, holding the right-hand side.**y**–**[inout]**array of`m`

elements, holding the solution.**policy**–**[in]**[rocsparse_solve_policy_auto](enumerations.html#rocsparse-types_8h_1a5a3e261123e81a9e8b267c6109e26957a9c6bdf97e192d429ca536d5ab98ea866).**temp_buffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`alpha`

,`csr_val`

,`csr_row_ptr`

,`csr_col_ind`

,`x`

or`y`

pointer is invalid.**rocsparse_status_arch_mismatch**– the device is not supported.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_not_implemented**–[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)and[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_triangular](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a73d9ef5e5e18209f9f10a5885d3e15ba).



## rocsparse_csritsv_clear()[#](#rocsparse-csritsv-clear)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_csritsv_clear([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info)[#](#_CPPv423rocsparse_csritsv_clear16rocsparse_handleK19rocsparse_mat_descr18rocsparse_mat_info) `rocsparse_csritsv_clear`

deallocates all memory that was allocated by[rocsparse_Xcsritsv_analysis()](#rocsparse__csritsv_8h_1af5d00a0a8877c2ef2ae06219d3d5eec2). This is especially useful, if memory is an issue and the analysis data is not required for further computation, e.g. when switching to another sparse matrix format. Calling`rocsparse_csritsv_clear`

is optional. All allocated resources will be cleared when the opaque[rocsparse_mat_info](types.html#rocsparse-types_8h_1a3347be72f6e4f3c55318c32b46dcaa92)struct is destroyed using[rocsparse_destroy_mat_info()](auxiliary.html#rocsparse-auxiliary_8h_1a9c143f65076a10ebafcffc633ad5d87b).Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**descr**–**[in]**descriptor of the sparse CSR matrix.**info**–**[inout]**structure that holds the information collected during the analysis step.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`info`

pointer is invalid.**rocsparse_status_memory_error**– the buffer holding the meta data could not be deallocated.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_ellmv()[#](#rocsparse-ellmv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sellmv([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const float *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *ell_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*ell_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)ell_width, const float *x, const float *beta, float *y)[#](#_CPPv416rocsparse_sellmv16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_int13rocsparse_intPKfPKfPf)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dellmv([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const double *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *ell_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*ell_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)ell_width, const double *x, const double *beta, double *y)[#](#_CPPv416rocsparse_dellmv16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_intPKdK19rocsparse_mat_descrPKdPK13rocsparse_int13rocsparse_intPKdPKdPd)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cellmv([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*ell_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*ell_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)ell_width, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*x, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*beta,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*y)[#](#_CPPv416rocsparse_cellmv16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_intPK23rocsparse_float_complexK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_int13rocsparse_intPK23rocsparse_float_complexPK23rocsparse_float_complexP23rocsparse_float_complex)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zellmv([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*ell_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*ell_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)ell_width, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*x, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*beta,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*y)[#](#_CPPv416rocsparse_zellmv16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_intPK24rocsparse_double_complexK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_int13rocsparse_intPK24rocsparse_double_complexPK24rocsparse_double_complexP24rocsparse_double_complex) Sparse matrix vector multiplication using ELL storage format.

`rocsparse_ellmv`

multiplies the scalar \(\alpha\) with a sparse \(m \times n\) matrix, defined in ELL storage format, and the dense vector \(x\) and adds the result to the dense vector \(y\) that is multiplied by the scalar \(\beta\), such that\[ y := \alpha \cdot op(A) \cdot x + \beta \cdot y, \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if trans == rocsparse_operation_none} \\ A^T, & \text{if trans == rocsparse_operation_transpose} \\ A^H, & \text{if trans == rocsparse_operation_conjugate_transpose} \end{array} \right. \end{split}\]for(i = 0; i < m; ++i) { y[i] = beta * y[i]; for(p = 0; p < ell_width; ++p) { idx = p * m + i; if((ell_col_ind[idx] >= 0) && (ell_col_ind[idx] < n)) { y[i] = y[i] + alpha * ell_val[idx] * x[ell_col_ind[idx]]; } } }

**Example**This example performs a sparse matrix vector multiplication in ELL format. It also shows how to convert from CSR to ELL format.

int main() { // A sparse matrix // 1 0 3 4 // 0 0 5 1 // 0 2 0 0 // 4 0 0 8 rocsparse_int hAptr[5] = {0, 3, 5, 6, 8}; rocsparse_int hAcol[8] = {0, 2, 3, 2, 3, 1, 0, 3}; double hAval[8] = {1.0, 3.0, 4.0, 5.0, 1.0, 2.0, 4.0, 8.0}; rocsparse_int m = 4; rocsparse_int n = 4; rocsparse_int nnz = 8; double halpha = 1.0; double hbeta = 0.0; double hx[4] = {1.0, 2.0, 3.0, 4.0}; double hy[4] = {4.0, 5.0, 6.0, 7.0}; // rocSPARSE handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Matrix descriptors rocsparse_mat_descr descrA; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descrA)); rocsparse_mat_descr descrB; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descrB)); // Offload data to device rocsparse_int* dAptr; rocsparse_int* dAcol; double* dAval; double* dx; double* dy; HIP_CHECK(hipMalloc(&dAptr, sizeof(rocsparse_int) * (m + 1))); HIP_CHECK(hipMalloc(&dAcol, sizeof(rocsparse_int) * nnz)); HIP_CHECK(hipMalloc(&dAval, sizeof(double) * nnz)); HIP_CHECK(hipMalloc(&dx, sizeof(double) * n)); HIP_CHECK(hipMalloc(&dy, sizeof(double) * m)); HIP_CHECK(hipMemcpy(dAptr, hAptr, sizeof(rocsparse_int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dAcol, hAcol, sizeof(rocsparse_int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dAval, hAval, sizeof(double) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dx, hx, sizeof(double) * n, hipMemcpyHostToDevice)); // Convert CSR matrix to ELL format rocsparse_int* dBcol; double* dBval; // Determine ELL width rocsparse_int ell_width; ROCSPARSE_CHECK(rocsparse_csr2ell_width(handle, m, descrA, dAptr, descrB, &ell_width)); // Allocate memory for ELL storage format HIP_CHECK(hipMalloc(&dBcol, sizeof(rocsparse_int) * ell_width * m)); HIP_CHECK(hipMalloc(&dBval, sizeof(double) * ell_width * m)); // Convert matrix from CSR to ELL ROCSPARSE_CHECK(rocsparse_dcsr2ell( handle, m, descrA, dAval, dAptr, dAcol, descrB, ell_width, dBval, dBcol)); // Clean up CSR structures HIP_CHECK(hipFree(dAptr)); HIP_CHECK(hipFree(dAcol)); HIP_CHECK(hipFree(dAval)); // Call rocsparse ellmv ROCSPARSE_CHECK(rocsparse_dellmv(handle, rocsparse_operation_none, m, n, &halpha, descrB, dBval, dBcol, ell_width, dx, &hbeta, dy)); // Copy result back to host HIP_CHECK(hipMemcpy(hy, dy, sizeof(double) * m, hipMemcpyDeviceToHost)); std::cout << "hy" << std::endl; for(size_t i = 0; i < m; i++) { std::cout << hy[i] << " "; } std::cout << "" << std::endl; // Clear up on device ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descrA)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descrB)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); HIP_CHECK(hipFree(dBcol)); HIP_CHECK(hipFree(dBval)); HIP_CHECK(hipFree(dx)); HIP_CHECK(hipFree(dy)); return 0; }


Note

This function does not produce deterministic results when A is transposed.

Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**trans**–**[in]**matrix operation type.**m**–**[in]**number of rows of the sparse ELL matrix.**n**–**[in]**number of columns of the sparse ELL matrix.**alpha**–**[in]**scalar \(\alpha\).**descr**–**[in]**descriptor of the sparse ELL matrix. Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**ell_val**–**[in]**array that contains the elements of the sparse ELL matrix. Padded elements should be zero.**ell_col_ind**–**[in]**array that contains the column indices of the sparse ELL matrix. Padded column indices should be -1.**ell_width**–**[in]**number of non-zero elements per row of the sparse ELL matrix.**x**–**[in]**array of`n`

elements ( \(op(A) == A\)) or`m`

elements ( \(op(A) == A^T\) or \(op(A) == A^H\)).**beta**–**[in]**scalar \(\beta\).**y**–**[inout]**array of`m`

elements ( \(op(A) == A\)) or`n`

elements ( \(op(A) == A^T\) or \(op(A) == A^H\)).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`n`

or`ell_width`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`alpha`

,`ell_val`

,`ell_col_ind`

,`x`

,`beta`

or`y`

pointer is invalid.**rocsparse_status_not_implemented**–[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_hybmv()[#](#rocsparse-hybmv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_shybmv([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans, const float *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_hyb_mat](types.html#_CPPv417rocsparse_hyb_mat)hyb, const float *x, const float *beta, float *y)[#](#_CPPv416rocsparse_shybmv16rocsparse_handle19rocsparse_operationPKfK19rocsparse_mat_descrK17rocsparse_hyb_matPKfPKfPf)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dhybmv([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans, const double *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_hyb_mat](types.html#_CPPv417rocsparse_hyb_mat)hyb, const double *x, const double *beta, double *y)[#](#_CPPv416rocsparse_dhybmv16rocsparse_handle19rocsparse_operationPKdK19rocsparse_mat_descrK17rocsparse_hyb_matPKdPKdPd)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_chybmv([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_hyb_mat](types.html#_CPPv417rocsparse_hyb_mat)hyb, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*x, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*beta,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*y)[#](#_CPPv416rocsparse_chybmv16rocsparse_handle19rocsparse_operationPK23rocsparse_float_complexK19rocsparse_mat_descrK17rocsparse_hyb_matPK23rocsparse_float_complexPK23rocsparse_float_complexP23rocsparse_float_complex)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zhybmv([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_hyb_mat](types.html#_CPPv417rocsparse_hyb_mat)hyb, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*x, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*beta,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*y)[#](#_CPPv416rocsparse_zhybmv16rocsparse_handle19rocsparse_operationPK24rocsparse_double_complexK19rocsparse_mat_descrK17rocsparse_hyb_matPK24rocsparse_double_complexPK24rocsparse_double_complexP24rocsparse_double_complex) Sparse matrix vector multiplication using HYB storage format.

`rocsparse_hybmv`

multiplies the scalar \(\alpha\) with a sparse \(m \times n\) matrix, defined in HYB storage format, and the dense vector \(x\) and adds the result to the dense vector \(y\) that is multiplied by the scalar \(\beta\), such that\[ y := \alpha \cdot op(A) \cdot x + \beta \cdot y, \]with\[ op(A) = \left\{ \begin{array}{ll} A, & \text{if trans == rocsparse_operation_none} \end{array} \right. \]**Example**This example performs a sparse matrix vector multiplication in HYB format. Also demonstrate conversion from CSR to HYB.

int main() { // rocSPARSE handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // A sparse matrix // 1 0 3 4 // 0 0 5 1 // 0 2 0 0 // 4 0 0 8 rocsparse_int hAptr[5] = {0, 3, 5, 6, 8}; rocsparse_int hAcol[8] = {0, 2, 3, 2, 3, 1, 0, 3}; double hAval[8] = {1.0, 3.0, 4.0, 5.0, 1.0, 2.0, 4.0, 8.0}; rocsparse_int m = 4; rocsparse_int n = 4; rocsparse_int nnz = 8; double halpha = 1.0; double hbeta = 0.0; double hx[4] = {1.0, 2.0, 3.0, 4.0}; double hy[4] = {4.0, 5.0, 6.0, 7.0}; // Matrix descriptor rocsparse_mat_descr descrA; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descrA)); // Offload data to device rocsparse_int* dAptr; rocsparse_int* dAcol; double* dAval; double* dx; double* dy; HIP_CHECK(hipMalloc(&dAptr, sizeof(rocsparse_int) * (m + 1))); HIP_CHECK(hipMalloc(&dAcol, sizeof(rocsparse_int) * nnz)); HIP_CHECK(hipMalloc(&dAval, sizeof(double) * nnz)); HIP_CHECK(hipMalloc(&dx, sizeof(double) * n)); HIP_CHECK(hipMalloc(&dy, sizeof(double) * m)); HIP_CHECK(hipMemcpy(dAptr, hAptr, sizeof(rocsparse_int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dAcol, hAcol, sizeof(rocsparse_int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dAval, hAval, sizeof(double) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dx, hx, sizeof(double) * n, hipMemcpyHostToDevice)); // Convert CSR matrix to HYB format rocsparse_hyb_mat hybA; ROCSPARSE_CHECK(rocsparse_create_hyb_mat(&hybA)); ROCSPARSE_CHECK(rocsparse_dcsr2hyb( handle, m, n, descrA, dAval, dAptr, dAcol, hybA, 0, rocsparse_hyb_partition_auto)); // Clean up CSR structures HIP_CHECK(hipFree(dAptr)); HIP_CHECK(hipFree(dAcol)); HIP_CHECK(hipFree(dAval)); // Call rocsparse hybmv ROCSPARSE_CHECK( rocsparse_dhybmv(handle, rocsparse_operation_none, &halpha, descrA, hybA, dx, &hbeta, dy)); // Copy result back to host HIP_CHECK(hipMemcpy(hy, dy, sizeof(double) * m, hipMemcpyDeviceToHost)); std::cout << "hy" << std::endl; for(size_t i = 0; i < m; i++) { std::cout << hy[i] << " "; } std::cout << "" << std::endl; // Clear up on device ROCSPARSE_CHECK(rocsparse_destroy_hyb_mat(hybA)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descrA)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); HIP_CHECK(hipFree(dx)); HIP_CHECK(hipFree(dy)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**trans**–**[in]**matrix operation type.**alpha**–**[in]**scalar \(\alpha\).**descr**–**[in]**descriptor of the sparse HYB matrix. Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**hyb**–**[in]**matrix in HYB storage format.**x**–**[in]**array of`n`

elements ( \(op(A) == A\)) or`m`

elements ( \(op(A) == A^T\) or \(op(A) == A^H\)).**beta**–**[in]**scalar \(\beta\).**y**–**[inout]**array of`m`

elements ( \(op(A) == A\)) or`n`

elements ( \(op(A) == A^T\) or \(op(A) == A^H\)).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`hyb`

structure was not initialized with valid matrix sizes.**rocsparse_status_invalid_pointer**–`descr`

,`alpha`

,`hyb`

,`x`

,`beta`

or`y`

pointer is invalid.**rocsparse_status_invalid_value**–`hyb`

structure was not initialized with a valid partitioning type.**rocsparse_status_arch_mismatch**– the device is not supported.**rocsparse_status_memory_error**– the buffer could not be allocated.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_not_implemented**–`trans`

!=[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528)or[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_gebsrmv()[#](#rocsparse-gebsrmv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sgebsrmv([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const float *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, const float *x, const float *beta, float *y)[#](#_CPPv418rocsparse_sgebsrmv16rocsparse_handle19rocsparse_direction19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intPKfPKfPf)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dgebsrmv([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const double *alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, const double *x, const double *beta, double *y)[#](#_CPPv418rocsparse_dgebsrmv16rocsparse_handle19rocsparse_direction19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKdK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intPKdPKdPd)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cgebsrmv([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*x, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*beta,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*y)[#](#_CPPv418rocsparse_cgebsrmv16rocsparse_handle19rocsparse_direction19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPK23rocsparse_float_complexK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intPK23rocsparse_float_complexPK23rocsparse_float_complexP23rocsparse_float_complex)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zgebsrmv([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*alpha, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)row_block_dim,[rocsparse_int](types.html#_CPPv413rocsparse_int)col_block_dim, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*x, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*beta,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*y)[#](#_CPPv418rocsparse_zgebsrmv16rocsparse_handle19rocsparse_direction19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPK24rocsparse_double_complexK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intPK24rocsparse_double_complexPK24rocsparse_double_complexP24rocsparse_double_complex) Sparse matrix vector multiplication using GEBSR storage format.

`rocsparse_gebsrmv`

multiplies the scalar \(\alpha\) with a sparse \(m \times n\) matrix, defined in GEBSR storage format, and the dense vector \(x\) and adds the result to the dense vector \(y\) that is multiplied by the scalar \(\beta\), such that\[ y := \alpha \cdot op(A) \cdot x + \beta \cdot y, \]with\[ op(A) = \left\{ \begin{array}{ll} A, & \text{if trans == rocsparse_operation_none} \end{array} \right. \]and where \(m = mb \times row\_block\_dim\) and \(n = nb \times col\_block\_dim\).**Example**This example performs a sparse matrix vector multiplication in GEBSR format.

int main() { // alpha * ( 1.0 0.0 2.0 ) * ( 1.0 ) + beta * ( 4.0 ) = ( 31.1 ) // ( 3.0 0.0 4.0 ) * ( 2.0 ) ( 5.0 ) = ( 62.0 ) // ( 5.0 6.0 0.0 ) * ( 3.0 ) ( 6.0 ) = ( 70.7 ) // ( 7.0 0.0 8.0 ) * ( 7.0 ) = ( 123.8 ) // GEBSR block dimensions rocsparse_int row_block_dim = 2; rocsparse_int col_block_dim = 3; // Number of block rows and columns rocsparse_int mb = 2; rocsparse_int nb = 1; // Number of non-zero blocks rocsparse_int nnzb = 2; // BSR row pointers rocsparse_int hbsr_row_ptr[3] = {0, 1, 2}; // BSR column indices rocsparse_int hbsr_col_ind[2] = {0, 0}; // BSR values double hbsr_val[16] = {1.0, 3.0, 0.0, 0.0, 2.0, 4.0, 5.0, 7.0, 6.0, 0.0, 0.0, 8.0}; // Block storage in column major rocsparse_direction dir = rocsparse_direction_column; // Transposition of the matrix rocsparse_operation trans = rocsparse_operation_none; // Scalar alpha and beta double alpha = 3.7; double beta = 1.3; // x and y double hx[4] = {1.0, 2.0, 3.0, 0.0}; double hy[4] = {4.0, 5.0, 6.0, 7.0}; // rocSPARSE handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Matrix descriptor rocsparse_mat_descr descr; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr)); // Offload data to device rocsparse_int* dbsr_row_ptr; rocsparse_int* dbsr_col_ind; double* dbsr_val; double* dx; double* dy; HIP_CHECK(hipMalloc(&dbsr_row_ptr, sizeof(rocsparse_int) * (mb + 1))); HIP_CHECK(hipMalloc(&dbsr_col_ind, sizeof(rocsparse_int) * nnzb)); HIP_CHECK(hipMalloc(&dbsr_val, sizeof(double) * nnzb * row_block_dim * col_block_dim)); HIP_CHECK(hipMalloc(&dx, sizeof(double) * nb * col_block_dim)); HIP_CHECK(hipMalloc(&dy, sizeof(double) * mb * row_block_dim)); HIP_CHECK(hipMemcpy( dbsr_row_ptr, hbsr_row_ptr, sizeof(rocsparse_int) * (mb + 1), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dbsr_col_ind, hbsr_col_ind, sizeof(rocsparse_int) * nnzb, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dbsr_val, hbsr_val, sizeof(double) * nnzb * row_block_dim * col_block_dim, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dx, hx, sizeof(double) * nb * col_block_dim, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dy, hy, sizeof(double) * mb * row_block_dim, hipMemcpyHostToDevice)); // Call dbsrmv to perform y = alpha * A x + beta * y ROCSPARSE_CHECK(rocsparse_dgebsrmv(handle, dir, trans, mb, nb, nnzb, &alpha, descr, dbsr_val, dbsr_row_ptr, dbsr_col_ind, row_block_dim, col_block_dim, dx, &beta, dy)); // Copy result back to host HIP_CHECK(hipMemcpy(hy, dy, sizeof(double) * mb * row_block_dim, hipMemcpyDeviceToHost)); std::cout << "hy" << std::endl; for(size_t i = 0; i < mb * row_block_dim; i++) { std::cout << hy[i] << " "; } std::cout << "" << std::endl; // Clear rocSPARSE ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); // Clear device memory HIP_CHECK(hipFree(dbsr_row_ptr)); HIP_CHECK(hipFree(dbsr_col_ind)); HIP_CHECK(hipFree(dbsr_val)); HIP_CHECK(hipFree(dx)); HIP_CHECK(hipFree(dy)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dir**–**[in]**matrix storage of GEBSR blocks.**trans**–**[in]**matrix operation type.**mb**–**[in]**number of block rows of the sparse GEBSR matrix.**nb**–**[in]**number of block columns of the sparse GEBSR matrix.**nnzb**–**[in]**number of non-zero blocks of the sparse GEBSR matrix.**alpha**–**[in]**scalar \(\alpha\).**descr**–**[in]**descriptor of the sparse GEBSR matrix. Currently, only[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)is supported.**bsr_val**–**[in]**array of`nnzb`

blocks of the sparse GEBSR matrix.**bsr_row_ptr**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse GEBSR matrix.**bsr_col_ind**–**[in]**array of`nnz`

containing the block column indices of the sparse GEBSR matrix.**row_block_dim**–**[in]**row block dimension of the sparse GEBSR matrix.**col_block_dim**–**[in]**column block dimension of the sparse GEBSR matrix.**x**–**[in]**array of`nb*col_block_dim`

elements ( \(op(A) = A\)) or`mb*row_block_dim`

elements ( \(op(A) = A^T\) or \(op(A) = A^H\)).**beta**–**[in]**scalar \(\beta\).**y**–**[inout]**array of`mb*row_block_dim`

elements ( \(op(A) = A\)) or`nb*col_block_dim`

elements ( \(op(A) = A^T\) or \(op(A) = A^H\)).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`mb`

,`nb`

,`nnzb`

,`row_block_dim`

or`col_block_dim`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`alpha`

,`bsr_val`

,`bsr_row_ind`

,`bsr_col_ind`

,`x`

,`beta`

or`y`

pointer is invalid.**rocsparse_status_arch_mismatch**– the device is not supported.**rocsparse_status_not_implemented**–`trans`

!=[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528)or[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_gemvi_buffer_size()[#](#rocsparse-gemvi-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sgemvi_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, size_t *buffer_size)[#](#_CPPv428rocsparse_sgemvi_buffer_size16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dgemvi_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, size_t *buffer_size)[#](#_CPPv428rocsparse_dgemvi_buffer_size16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cgemvi_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, size_t *buffer_size)[#](#_CPPv428rocsparse_cgemvi_buffer_size16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zgemvi_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, size_t *buffer_size)[#](#_CPPv428rocsparse_zgemvi_buffer_size16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intP6size_t) `rocsparse_gemvi_buffer_size`

returns the size of the temporary storage buffer required by[rocsparse_Xgemvi()](#rocsparse__gemvi_8h_1adeda2ce940f636044e3a15d624edd50f). The temporary storage buffer must be allocated by the user.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**trans**–**[in]**matrix operation type.**m**–**[in]**number of rows of the dense matrix.**n**–**[in]**number of columns of the dense matrix.**nnz**–**[in]**number of non-zero entries in the sparse vector.**buffer_size**–**[out]**temporary storage buffer size.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`n`

, or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`buffer_size`

pointer is invalid.**rocsparse_status_not_implemented**–`trans`

!=[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528)or[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_gemvi()[#](#rocsparse-gemvi)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sgemvi([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const float *alpha, const float *A,[rocsparse_int](types.html#_CPPv413rocsparse_int)lda,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const float *x_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*x_ind, const float *beta, float *y,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base, void *temp_buffer)[#](#_CPPv416rocsparse_sgemvi16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_intPKfPKf13rocsparse_int13rocsparse_intPKfPK13rocsparse_intPKfPf20rocsparse_index_basePv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dgemvi([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const double *alpha, const double *A,[rocsparse_int](types.html#_CPPv413rocsparse_int)lda,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const double *x_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*x_ind, const double *beta, double *y,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base, void *temp_buffer)[#](#_CPPv416rocsparse_dgemvi16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_intPKdPKd13rocsparse_int13rocsparse_intPKdPK13rocsparse_intPKdPd20rocsparse_index_basePv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cgemvi([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*alpha, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*A,[rocsparse_int](types.html#_CPPv413rocsparse_int)lda,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*x_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*x_ind, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*beta,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*y,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base, void *temp_buffer)[#](#_CPPv416rocsparse_cgemvi16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_intPK23rocsparse_float_complexPK23rocsparse_float_complex13rocsparse_int13rocsparse_intPK23rocsparse_float_complexPK13rocsparse_intPK23rocsparse_float_complexP23rocsparse_float_complex20rocsparse_index_basePv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zgemvi([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_operation](enumerations.html#_CPPv419rocsparse_operation)trans,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*alpha, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*A,[rocsparse_int](types.html#_CPPv413rocsparse_int)lda,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*x_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*x_ind, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*beta,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*y,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base, void *temp_buffer)[#](#_CPPv416rocsparse_zgemvi16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_intPK24rocsparse_double_complexPK24rocsparse_double_complex13rocsparse_int13rocsparse_intPK24rocsparse_double_complexPK13rocsparse_intPK24rocsparse_double_complexP24rocsparse_double_complex20rocsparse_index_basePv) Dense matrix sparse vector multiplication.

`rocsparse_gemvi`

multiplies the scalar \(\alpha\) with a dense \(m \times n\) matrix \(A\) and the sparse vector \(x\) and adds the result to the dense vector \(y\) that is multiplied by the scalar \(\beta\), such that\[ y := \alpha \cdot op(A) \cdot x + \beta \cdot y, \]with\[ op(A) = \left\{ \begin{array}{ll} A, & \text{if trans == rocsparse_operation_none} \end{array} \right. \]Performing the above operation involves two steps. First, the user calls

[rocsparse_Xgemvi_buffer_size()](#rocsparse__gemvi_8h_1a9e914962214cf42b07faaf2cab14390b)in order to determine the size of the temporary storage buffer. Next, the user allocates this temporary buffer and passes it to`rocsparse_gemvi`

to complete the computation. Once all calls to`rocsparse_gemvi`

are complete the temporary storage buffer can be freed.**Example**int main() { // rocSPARSE handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); rocsparse_mat_descr descr; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr)); // Number of rows and columns rocsparse_int m = 3; rocsparse_int n = 5; // Dense matrix A in column-major rocsparse_int lda = m; double hA[15] = {9, 14, 19, 10, 15, 20, 11, 16, 21, 12, 17, 22, 13, 18, 23}; // Number of non-zero entries rocsparse_int nnz = 3; // Vector x indices rocsparse_int hx_ind[3] = {0, 1, 3}; // Vector x values double hx_val[3] = {1, 2, 3}; // Vector y values double hy[3] = {4, 5, 6}; // Scalar alpha and beta double alpha = 3.7; double beta = 1.3; // Matrix operation rocsparse_operation trans = rocsparse_operation_none; // Index base rocsparse_index_base base = rocsparse_index_base_zero; // Offload data to device double* dA; rocsparse_int* dx_ind; double* dx_val; double* dy; HIP_CHECK(hipMalloc(&dA, sizeof(double) * m * n)); HIP_CHECK(hipMalloc(&dx_ind, sizeof(rocsparse_int) * nnz)); HIP_CHECK(hipMalloc(&dx_val, sizeof(double) * nnz)); HIP_CHECK(hipMalloc(&dy, sizeof(double) * m)); HIP_CHECK(hipMemcpy(dA, hA, sizeof(double) * m * n, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dx_ind, hx_ind, sizeof(rocsparse_int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dx_val, hx_val, sizeof(double) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dy, hy, sizeof(double) * m, hipMemcpyHostToDevice)); // Obtain buffer size size_t buffer_size; ROCSPARSE_CHECK(rocsparse_dgemvi_buffer_size(handle, trans, m, n, nnz, &buffer_size)); void* buffer; HIP_CHECK(hipMalloc(&buffer, buffer_size)); // Call dgemvi ROCSPARSE_CHECK(rocsparse_dgemvi( handle, trans, m, n, &alpha, dA, lda, nnz, dx_val, dx_ind, &beta, dy, base, buffer)); // Copy result back to host HIP_CHECK(hipMemcpy(hy, dy, sizeof(double) * m, hipMemcpyDeviceToHost)); std::cout << "hy" << std::endl; for(size_t i = 0; i < m; i++) { std::cout << hy[i] << " "; } std::cout << "" << std::endl; // Clear rocSPARSE ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); // Clear device memory HIP_CHECK(hipFree(dA)); HIP_CHECK(hipFree(dx_ind)); HIP_CHECK(hipFree(dx_val)); HIP_CHECK(hipFree(dy)); HIP_CHECK(hipFree(buffer)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**trans**–**[in]**matrix operation type.**m**–**[in]**number of rows of the dense matrix.**n**–**[in]**number of columns of the dense matrix.**alpha**–**[in]**scalar \(\alpha\).**A**–**[in]**pointer to the dense matrix.**lda**–**[in]**leading dimension of the dense matrix**nnz**–**[in]**number of non-zero entries in the sparse vector**x_val**–**[in]**array of`nnz`

elements containing the values of the sparse vector**x_ind**–**[in]**array of`nnz`

elements containing the indices of the sparse vector**beta**–**[in]**scalar \(\beta\).**y**–**[inout]**array of`m`

elements ( \(op(A) == A\)) or`n`

elements ( \(op(A) == A^T\) or \(op(A) == A^H\)).**idx_base**–**[in]**rocsparse_index_base_zero or rocsparse_index_base_one.**temp_buffer**–**[in]**temporary storage buffer

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`n`

,`lda`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`alpha`

,`A`

,`x_val`

,`x_ind`

,`beta`

,`y`

or`temp_buffer`

pointer is invalid.**rocsparse_status_not_implemented**–`trans`

!=[rocsparse_operation_none](enumerations.html#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0ad992ce988c65ce01fe87f0da2018f528)or[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).
