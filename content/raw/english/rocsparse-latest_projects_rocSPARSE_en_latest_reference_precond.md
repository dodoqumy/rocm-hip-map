---
title: "Sparse preconditioner functions &#8212; rocSPARSE 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocSPARSE/en/latest/reference/precond.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:08:50.940994+00:00
content_hash: "1117d78fd47cfe22"
---

# Sparse preconditioner functions[#](#sparse-preconditioner-functions)

This module contains all sparse preconditioners.

The sparse preconditioners describe manipulations on a matrix in sparse format to obtain a sparse preconditioner matrix.

## rocsparse_bsric0_zero_pivot()[#](#rocsparse-bsric0-zero-pivot)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_bsric0_zero_pivot([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_int](types.html#_CPPv413rocsparse_int)*position)[#](#_CPPv427rocsparse_bsric0_zero_pivot16rocsparse_handle18rocsparse_mat_infoP13rocsparse_int) `rocsparse_bsric0_zero_pivot`

returns[rocsparse_status_zero_pivot](enumerations.html#rocsparse-types_8h_1a578f8c5c1b08f358bf4605b0031006a8a01fe264830c8ce6451ce6888bc8d3e80), if either a structural or numerical zero has been found during[rocsparse_Xbsric0()](#rocsparse__bsric0_8h_1a8ba21d327368ebe0a096331a480baf3e), computation. The first zero pivot \(j\) at \(A_{j,j}\) is stored in`position`

, using same index base as the BSR matrix.`position`

can be in host or device memory. If no zero pivot has been found,`position`

is set to -1 and[rocsparse_status_success](enumerations.html#rocsparse-types_8h_1a578f8c5c1b08f358bf4605b0031006a8a96462a9361cfceb6cf9354e10fdc671b)is returned instead.Note

If a zero pivot is found,

`position=j`

means that either the diagonal block`A(j,j)`

is missing (structural zero) or the diagonal block`A(j,j)`

is not positive definite (numerical zero).Note

`rocsparse_bsric0_zero_pivot`

is a blocking function. It might influence performance negatively.Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**info**–**[in]**structure that holds the information collected during the analysis step.**position**–**[inout]**pointer to zero pivot \(j\), can be in host or device memory.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`info`

or`position`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_zero_pivot**– zero pivot has been found.



## rocsparse_bsric0_buffer_size()[#](#rocsparse-bsric0-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sbsric0_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, size_t *buffer_size)[#](#_CPPv429rocsparse_sbsric0_buffer_size16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_infoP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dbsric0_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, size_t *buffer_size)[#](#_CPPv429rocsparse_dbsric0_buffer_size16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_infoP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cbsric0_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, size_t *buffer_size)[#](#_CPPv429rocsparse_cbsric0_buffer_size16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_infoP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zbsric0_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, size_t *buffer_size)[#](#_CPPv429rocsparse_zbsric0_buffer_size16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_infoP6size_t) `rocsparse_bsric0_buffer_size`

returns the size of the temporary storage buffer that is required by[rocsparse_Xbsric0_analysis()](#rocsparse__bsric0_8h_1a9cfb58036bb689f2becba8c0baa9d716)and[rocsparse_Xbsric0()](#rocsparse__bsric0_8h_1a8ba21d327368ebe0a096331a480baf3e). The temporary storage buffer must be allocated by the user. The size of the temporary storage buffer is identical to the size returned by[rocsparse_Xbsrsv_buffer_size()](level2.html#rocsparse__bsrsv_8h_1aa0d8d2b089478eaa357c7ca0f2d1332e)and[rocsparse_Xbsrilu0_buffer_size()](#rocsparse__bsrilu0_8h_1a71976ed155de1fc6a71c79144a546cdb)if the matrix sparsity pattern is identical. The user allocated buffer can thus be shared between subsequent calls to those functions.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dir**–**[in]**direction that specifies whether to count nonzero elements by[rocsparse_direction_row](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca40d95f05d0cd4ad3c89465959c58943e)or by[rocsparse_direction_column](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca23355bb7b606c550ba61c781bcecfc5b).**mb**–**[in]**number of block rows in the sparse BSR matrix.**nnzb**–**[in]**number of non-zero block entries of the sparse BSR matrix.**descr**–**[in]**descriptor of the sparse BSR matrix.**bsr_val**–**[in]**array of length`nnzb*block_dim*block_dim`

containing the values of the sparse BSR matrix.**bsr_row_ptr**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix.**bsr_col_ind**–**[in]**array of`nnzb`

elements containing the block column indices of the sparse BSR matrix.**block_dim**–**[in]**the block dimension of the BSR matrix. Between 1 and m where`m=mb*block_dim`

.**info**–**[out]**structure that holds the information collected during the analysis step.**buffer_size**–**[out]**number of bytes of the temporary storage buffer required by[rocsparse_Xbsric0_analysis()](#rocsparse__bsric0_8h_1a9cfb58036bb689f2becba8c0baa9d716)and[rocsparse_Xbsric0()](#rocsparse__bsric0_8h_1a8ba21d327368ebe0a096331a480baf3e).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`mb`

,`nnzb`

, or`block_dim`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`bsr_val`

,`bsr_row_ptr`

,`bsr_col_ind`

,`info`

or`buffer_size`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_not_implemented**–[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_bsric0_analysis()[#](#rocsparse-bsric0-analysis)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sbsric0_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_analysis_policy](enumerations.html#_CPPv425rocsparse_analysis_policy)analysis,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)solve, void *temp_buffer)[#](#_CPPv426rocsparse_sbsric0_analysis16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dbsric0_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_analysis_policy](enumerations.html#_CPPv425rocsparse_analysis_policy)analysis,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)solve, void *temp_buffer)[#](#_CPPv426rocsparse_dbsric0_analysis16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cbsric0_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_analysis_policy](enumerations.html#_CPPv425rocsparse_analysis_policy)analysis,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)solve, void *temp_buffer)[#](#_CPPv426rocsparse_cbsric0_analysis16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zbsric0_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_analysis_policy](enumerations.html#_CPPv425rocsparse_analysis_policy)analysis,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)solve, void *temp_buffer)[#](#_CPPv426rocsparse_zbsric0_analysis16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv) `rocsparse_bsric0_analysis`

performs the analysis step for[rocsparse_Xbsric0()](#rocsparse__bsric0_8h_1a8ba21d327368ebe0a096331a480baf3e). It is expected that this function will be executed only once for a given matrix and particular operation type. The analysis meta data can be cleared by[rocsparse_bsric0_clear()](#rocsparse__bsric0_8h_1a20955e3a4d112ef74970a8f6f7ec5ef6).`rocsparse_bsric0_analysis`

can share its meta data with[rocsparse_Xbsrilu0_analysis()](#rocsparse__bsrilu0_8h_1ac20c3e0a79507660dea8895f4111f170),[rocsparse_Xbsrsv_analysis()](level2.html#rocsparse__bsrsv_8h_1aade89276269f88cd50e357c0a3504c87), and[rocsparse_Xbsrsm_analysis()](level3.html#rocsparse__bsrsm_8h_1aa7c3da4c56f9dcf7aaae3e65dd35110f). Selecting[rocsparse_analysis_policy_reuse](enumerations.html#rocsparse-types_8h_1a43b20aa4bb19623a91b5952422fbe35ca658466413f4005c0c103d20d5e352078)policy can greatly improve computation performance of meta data. However, the user needs to make sure that the sparsity pattern remains unchanged. If this cannot be assured,[rocsparse_analysis_policy_force](enumerations.html#rocsparse-types_8h_1a43b20aa4bb19623a91b5952422fbe35cac66b70c4f519ddd03dcbe0f3a973401a)has to be used.Note

If the matrix sparsity pattern changes, the gathered information will become invalid.

Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dir**–**[in]**direction that specified whether to count nonzero elements by[rocsparse_direction_row](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca40d95f05d0cd4ad3c89465959c58943e)or by[rocsparse_direction_column](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca23355bb7b606c550ba61c781bcecfc5b).**mb**–**[in]**number of block rows in the sparse BSR matrix.**nnzb**–**[in]**number of non-zero block entries of the sparse BSR matrix.**descr**–**[in]**descriptor of the sparse BSR matrix.**bsr_val**–**[in]**array of length`nnzb*block_dim*block_dim`

containing the values of the sparse BSR matrix.**bsr_row_ptr**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix.**bsr_col_ind**–**[in]**array of`nnzb`

elements containing the block column indices of the sparse BSR matrix.**block_dim**–**[in]**the block dimension of the BSR matrix. Between 1 and m where`m=mb*block_dim`

.**info**–**[out]**structure that holds the information collected during the analysis step.**analysis**–**[in]**[rocsparse_analysis_policy_reuse](enumerations.html#rocsparse-types_8h_1a43b20aa4bb19623a91b5952422fbe35ca658466413f4005c0c103d20d5e352078)or[rocsparse_analysis_policy_force](enumerations.html#rocsparse-types_8h_1a43b20aa4bb19623a91b5952422fbe35cac66b70c4f519ddd03dcbe0f3a973401a).**solve**–**[in]**[rocsparse_solve_policy_auto](enumerations.html#rocsparse-types_8h_1a5a3e261123e81a9e8b267c6109e26957a9c6bdf97e192d429ca536d5ab98ea866).**temp_buffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`mb`

,`nnzb`

, or`block_dim`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`bsr_val`

,`bsr_row_ptr`

,`bsr_col_ind`

,`info`

or`temp_buffer`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_not_implemented**–[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_bsric0()[#](#rocsparse-bsric0)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sbsric0([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, float *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv417rocsparse_sbsric016rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPfPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_info22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dbsric0([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, double *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv417rocsparse_dbsric016rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPdPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_info22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cbsric0([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv417rocsparse_cbsric016rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrP23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_info22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zbsric0([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv417rocsparse_zbsric016rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrP24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_info22rocsparse_solve_policyPv) Incomplete Cholesky factorization with 0 fill-ins and no pivoting using BSR storage format.

`rocsparse_bsric0`

computes the incomplete Cholesky factorization with 0 fill-ins and no pivoting of a sparse \(mb \times mb\) BSR matrix \(A\), such that\[ A \approx LL^T \]Computing the above incomplete Cholesky factorization requires three steps to complete. First, the user determines the size of the required temporary storage buffer by calling

[rocsparse_sbsric0_buffer_size](#rocsparse__bsric0_8h_1a795bc27abdfcb87d4b66dbd8cdb2c92f),[rocsparse_dbsric0_buffer_size](#rocsparse__bsric0_8h_1a397d4f4bd30f921c251f713dd11f2605),[rocsparse_cbsric0_buffer_size](#rocsparse__bsric0_8h_1a6d07943bd91f31821ba05d6016164900), or[rocsparse_zbsric0_buffer_size](#rocsparse__bsric0_8h_1a308a5760d7fd2ef933e177cebb58170b). Once this buffer size has been determined, the user allocates the buffer and passes it to[rocsparse_sbsric0_analysis](#rocsparse__bsric0_8h_1a9cfb58036bb689f2becba8c0baa9d716),[rocsparse_dbsric0_analysis](#rocsparse__bsric0_8h_1a73f35e25bc0ec4d02e1358c34cae7fd1),[rocsparse_cbsric0_analysis](#rocsparse__bsric0_8h_1aa17dc296403aa88fa8ed86e661fe374a), or[rocsparse_zbsric0_analysis](#rocsparse__bsric0_8h_1aa8308572f8f45a92247e99b3c32b8b47). This will perform analysis on the sparsity pattern of the matrix. Finally, the user calls`rocsparse_sbsric0`

,`rocsparse_dbsric0`

,`rocsparse_cbsric0`

, or`rocsparse_zbsric0`

to perform the actual factorization. The calculation of the buffer size and the analysis of the sparse matrix only need to be performed once for a given sparsity pattern while the factorization can be repeatedly applied to multiple matrices having the same sparsity pattern. Once all calls to[rocsparse_Xbsric0()](#rocsparse__bsric0_8h_1a8ba21d327368ebe0a096331a480baf3e)are complete, the temporary buffer can be deallocated.`rocsparse_bsric0`

reports the first zero pivot (either numerical or structural zero). The zero pivot status can be obtained by calling[rocsparse_bsric0_zero_pivot()](#rocsparse__bsric0_8h_1a5fb0028e1a1a77fea56a139b06f2c231).**Example**Consider the sparse \(m \times m\) matrix \(A\), stored in BSR storage format. The following example computes the incomplete Cholesky factorization \(M \approx LL^T\) and solves the preconditioned system \(My = x\).

int main() { // 2 1 0 0 // A = 1 2 0 0 // 0 0 2 1 // 0 0 1 2 int mb = 2; int nb = 2; int nnzb = 2; int block_dim = 2; double alpha = 1.0; std::vector<int> hbsr_row_ptr = {0, 1, 2}; std::vector<int> hbsr_col_ind = {0, 1}; std::vector<double> hbsr_val = {2.0, 1.0, 1.0, 2.0, 2.0, 1.0, 1.0, 2.0}; std::vector<double> hx(mb * block_dim, 1.0); int* dbsr_row_ptr; int* dbsr_col_ind; double* dbsr_val; double* dx; double* dy; double* dz; HIP_CHECK(hipMalloc(&dbsr_row_ptr, sizeof(int) * (mb + 1))); HIP_CHECK(hipMalloc(&dbsr_col_ind, sizeof(int) * nnzb)); HIP_CHECK(hipMalloc(&dbsr_val, sizeof(double) * nnzb * block_dim * block_dim)); HIP_CHECK(hipMalloc(&dx, sizeof(double) * mb * block_dim)); HIP_CHECK(hipMalloc(&dy, sizeof(double) * mb * block_dim)); HIP_CHECK(hipMalloc(&dz, sizeof(double) * mb * block_dim)); HIP_CHECK(hipMemcpy( dbsr_row_ptr, hbsr_row_ptr.data(), sizeof(int) * (mb + 1), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dbsr_col_ind, hbsr_col_ind.data(), sizeof(int) * nnzb, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dbsr_val, hbsr_val.data(), sizeof(double) * nnzb * block_dim * block_dim, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dx, hx.data(), sizeof(double) * mb * block_dim, hipMemcpyHostToDevice)); // Create rocSPARSE handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Create matrix descriptor for M rocsparse_mat_descr descr_M; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr_M)); // Create matrix descriptor for L rocsparse_mat_descr descr_L; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr_L)); ROCSPARSE_CHECK(rocsparse_set_mat_fill_mode(descr_L, rocsparse_fill_mode_lower)); ROCSPARSE_CHECK(rocsparse_set_mat_diag_type(descr_L, rocsparse_diag_type_unit)); // Create matrix descriptor for L' rocsparse_mat_descr descr_Lt; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr_Lt)); ROCSPARSE_CHECK(rocsparse_set_mat_fill_mode(descr_Lt, rocsparse_fill_mode_upper)); ROCSPARSE_CHECK(rocsparse_set_mat_diag_type(descr_Lt, rocsparse_diag_type_non_unit)); // Create matrix info structure rocsparse_mat_info info; ROCSPARSE_CHECK(rocsparse_create_mat_info(&info)); // Obtain required buffer size size_t buffer_size_M; size_t buffer_size_L; size_t buffer_size_Lt; ROCSPARSE_CHECK(rocsparse_dbsric0_buffer_size(handle, rocsparse_direction_row, mb, nnzb, descr_M, dbsr_val, dbsr_row_ptr, dbsr_col_ind, block_dim, info, &buffer_size_M)); ROCSPARSE_CHECK(rocsparse_dbsrsv_buffer_size(handle, rocsparse_direction_row, rocsparse_operation_none, mb, nnzb, descr_L, dbsr_val, dbsr_row_ptr, dbsr_col_ind, block_dim, info, &buffer_size_L)); ROCSPARSE_CHECK(rocsparse_dbsrsv_buffer_size(handle, rocsparse_direction_row, rocsparse_operation_transpose, mb, nnzb, descr_Lt, dbsr_val, dbsr_row_ptr, dbsr_col_ind, block_dim, info, &buffer_size_Lt)); size_t buffer_size = max(buffer_size_M, max(buffer_size_L, buffer_size_Lt)); // Allocate temporary buffer void* temp_buffer; HIP_CHECK(hipMalloc(&temp_buffer, buffer_size)); // Perform analysis steps, using rocsparse_analysis_policy_reuse to improve // computation performance ROCSPARSE_CHECK(rocsparse_dbsric0_analysis(handle, rocsparse_direction_row, mb, nnzb, descr_M, dbsr_val, dbsr_row_ptr, dbsr_col_ind, block_dim, info, rocsparse_analysis_policy_reuse, rocsparse_solve_policy_auto, temp_buffer)); ROCSPARSE_CHECK(rocsparse_dbsrsv_analysis(handle, rocsparse_direction_row, rocsparse_operation_none, mb, nnzb, descr_L, dbsr_val, dbsr_row_ptr, dbsr_col_ind, block_dim, info, rocsparse_analysis_policy_reuse, rocsparse_solve_policy_auto, temp_buffer)); ROCSPARSE_CHECK(rocsparse_dbsrsv_analysis(handle, rocsparse_direction_row, rocsparse_operation_transpose, mb, nnzb, descr_Lt, dbsr_val, dbsr_row_ptr, dbsr_col_ind, block_dim, info, rocsparse_analysis_policy_reuse, rocsparse_solve_policy_auto, temp_buffer)); // Check for zero pivot rocsparse_int position; if(rocsparse_status_zero_pivot == rocsparse_bsric0_zero_pivot(handle, info, &position)) { printf("A has structural zero at A(%d,%d)\n", position, position); } // Compute incomplete Cholesky factorization M = LL' ROCSPARSE_CHECK(rocsparse_dbsric0(handle, rocsparse_direction_row, mb, nnzb, descr_M, dbsr_val, dbsr_row_ptr, dbsr_col_ind, block_dim, info, rocsparse_solve_policy_auto, temp_buffer)); // Check for zero pivot if(rocsparse_status_zero_pivot == rocsparse_bsric0_zero_pivot(handle, info, &position)) { printf("L has structural and/or numerical zero at L(%d,%d)\n", position, position); } // Solve Lz = x ROCSPARSE_CHECK(rocsparse_dbsrsv_solve(handle, rocsparse_direction_row, rocsparse_operation_none, mb, nnzb, &alpha, descr_L, dbsr_val, dbsr_row_ptr, dbsr_col_ind, block_dim, info, dx, dz, rocsparse_solve_policy_auto, temp_buffer)); // Solve L'y = z ROCSPARSE_CHECK(rocsparse_dbsrsv_solve(handle, rocsparse_direction_row, rocsparse_operation_transpose, mb, nnzb, &alpha, descr_Lt, dbsr_val, dbsr_row_ptr, dbsr_col_ind, block_dim, info, dz, dy, rocsparse_solve_policy_auto, temp_buffer)); std::vector<double> hy(mb * block_dim); HIP_CHECK(hipMemcpy(hy.data(), dy, sizeof(double) * mb * block_dim, hipMemcpyDeviceToHost)); std::cout << "hy" << std::endl; for(size_t i = 0; i < hy.size(); i++) { std::cout << hy[i] << " "; } std::cout << "" << std::endl; // Clean up ROCSPARSE_CHECK(rocsparse_destroy_mat_info(info)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr_M)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr_L)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr_Lt)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); HIP_CHECK(hipFree(dbsr_row_ptr)); HIP_CHECK(hipFree(dbsr_col_ind)); HIP_CHECK(hipFree(dbsr_val)); HIP_CHECK(hipFree(dx)); HIP_CHECK(hipFree(dy)); HIP_CHECK(hipFree(dz)); HIP_CHECK(hipFree(temp_buffer)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dir**–**[in]**direction that specified whether to count nonzero elements by[rocsparse_direction_row](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca40d95f05d0cd4ad3c89465959c58943e)or by[rocsparse_direction_column](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca23355bb7b606c550ba61c781bcecfc5b).**mb**–**[in]**number of block rows in the sparse BSR matrix.**nnzb**–**[in]**number of non-zero block entries of the sparse BSR matrix.**descr**–**[in]**descriptor of the sparse BSR matrix.**bsr_val**–**[inout]**array of length`nnzb*block_dim*block_dim`

containing the values of the sparse BSR matrix.**bsr_row_ptr**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix.**bsr_col_ind**–**[in]**array of`nnzb`

elements containing the block column indices of the sparse BSR matrix.**block_dim**–**[in]**the block dimension of the BSR matrix. Between 1 and m where`m=mb*block_dim`

.**info**–**[in]**structure that holds the information collected during the analysis step.**policy**–**[in]**[rocsparse_solve_policy_auto](enumerations.html#rocsparse-types_8h_1a5a3e261123e81a9e8b267c6109e26957a9c6bdf97e192d429ca536d5ab98ea866).**temp_buffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`mb`

,`nnzb`

, or`block_dim`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`bsr_val`

,`bsr_row_ptr`

or`bsr_col_ind`

pointer is invalid.**rocsparse_status_arch_mismatch**– the device is not supported.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_not_implemented**–[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_bsric0_clear()[#](#rocsparse-bsric0-clear)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_bsric0_clear([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info)[#](#_CPPv422rocsparse_bsric0_clear16rocsparse_handle18rocsparse_mat_info) `rocsparse_bsric0_clear`

deallocates all memory that was allocated by[rocsparse_Xbsric0_analysis()](#rocsparse__bsric0_8h_1a9cfb58036bb689f2becba8c0baa9d716). This is especially useful, if memory is an issue and the analysis data is not required for further computation.Note

Calling

`rocsparse_bsric0_clear`

is optional. All allocated resources will be cleared, when the opaque[rocsparse_mat_info](types.html#rocsparse-types_8h_1a3347be72f6e4f3c55318c32b46dcaa92)struct is destroyed using[rocsparse_destroy_mat_info()](auxiliary.html#rocsparse-auxiliary_8h_1a9c143f65076a10ebafcffc633ad5d87b).Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**info**–**[inout]**structure that holds the information collected during the analysis step.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`info`

pointer is invalid.**rocsparse_status_memory_error**– the buffer holding the meta data could not be deallocated.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_bsrilu0_zero_pivot()[#](#rocsparse-bsrilu0-zero-pivot)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_bsrilu0_zero_pivot([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_int](types.html#_CPPv413rocsparse_int)*position)[#](#_CPPv428rocsparse_bsrilu0_zero_pivot16rocsparse_handle18rocsparse_mat_infoP13rocsparse_int) `rocsparse_bsrilu0_zero_pivot`

returns[rocsparse_status_zero_pivot](enumerations.html#rocsparse-types_8h_1a578f8c5c1b08f358bf4605b0031006a8a01fe264830c8ce6451ce6888bc8d3e80), if either a structural or numerical zero has been found during[rocsparse_Xbsrilu0()](#rocsparse__bsrilu0_8h_1a26ae3e54761e7f15b9dac27d0f51d337)computation. The first zero pivot \(j\) at \(A_{j,j}\) is stored in`position`

, using same index base as the BSR matrix.`position`

can be in host or device memory. If no zero pivot has been found,`position`

is set to -1 and[rocsparse_status_success](enumerations.html#rocsparse-types_8h_1a578f8c5c1b08f358bf4605b0031006a8a96462a9361cfceb6cf9354e10fdc671b)is returned instead.Note

If a zero pivot is found,

`position`

\(=j\) means that either the diagonal block \(A_{j,j}\) is missing (structural zero) or the diagonal block \(A_{j,j}\) is not invertible (numerical zero).Note

`rocsparse_bsrilu0_zero_pivot`

is a blocking function. It might influence performance negatively.Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**info**–**[in]**structure that holds the information collected during the analysis step.**position**–**[inout]**pointer to zero pivot \(j\), can be in host or device memory.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`info`

or`position`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_zero_pivot**– zero pivot has been found.



## rocsparse_bsrilu0_numeric_boost()[#](#rocsparse-bsrilu0-numeric-boost)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sbsrilu0_numeric_boost([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, int enable_boost, const float *boost_tol, const float *boost_val)[#](#_CPPv432rocsparse_sbsrilu0_numeric_boost16rocsparse_handle18rocsparse_mat_infoiPKfPKf)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dbsrilu0_numeric_boost([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, int enable_boost, const double *boost_tol, const double *boost_val)[#](#_CPPv432rocsparse_dbsrilu0_numeric_boost16rocsparse_handle18rocsparse_mat_infoiPKdPKd)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cbsrilu0_numeric_boost([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, int enable_boost, const float *boost_tol, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*boost_val)[#](#_CPPv432rocsparse_cbsrilu0_numeric_boost16rocsparse_handle18rocsparse_mat_infoiPKfPK23rocsparse_float_complex)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zbsrilu0_numeric_boost([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, int enable_boost, const double *boost_tol, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*boost_val)[#](#_CPPv432rocsparse_zbsrilu0_numeric_boost16rocsparse_handle18rocsparse_mat_infoiPKdPK24rocsparse_double_complex) `rocsparse_bsrilu0_numeric_boost`

enables the user to replace a numerical value in an incomplete LU factorization.`tol`

is used to determine whether a numerical value is replaced by`boost_val`

, such that \(A_{j,j} = \text{boost_val}\) if \(\text{tol} \ge \left|A_{j,j}\right|\).Note

The boost value is enabled by setting

`enable_boost`

to 1 or disabled by setting`enable_boost`

to 0.Note

`tol`

and`boost_val`

can be in host or device memory.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**info**–**[in]**structure that holds the information collected during the analysis step.**enable_boost**–**[in]**enable/disable numeric boost.**boost_tol**–**[in]**tolerance to determine whether a numerical value is replaced or not.**boost_val**–**[in]**boost value to replace a numerical value.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`info`

,`tol`

or`boost_val`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_bsrilu0_buffer_size()[#](#rocsparse-bsrilu0-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sbsrilu0_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, size_t *buffer_size)[#](#_CPPv430rocsparse_sbsrilu0_buffer_size16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_infoP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dbsrilu0_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, size_t *buffer_size)[#](#_CPPv430rocsparse_dbsrilu0_buffer_size16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_infoP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cbsrilu0_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, size_t *buffer_size)[#](#_CPPv430rocsparse_cbsrilu0_buffer_size16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_infoP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zbsrilu0_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, size_t *buffer_size)[#](#_CPPv430rocsparse_zbsrilu0_buffer_size16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_infoP6size_t) `rocsparse_bsrilu0_buffer_size`

returns the size of the temporary storage buffer that is required by[rocsparse_Xbsrilu0_analysis()](#rocsparse__bsrilu0_8h_1ac20c3e0a79507660dea8895f4111f170)and[rocsparse_Xbsrilu0()](#rocsparse__bsrilu0_8h_1a26ae3e54761e7f15b9dac27d0f51d337). The temporary storage buffer must be allocated by the user. The size of the temporary storage buffer is identical to the size returned by[rocsparse_Xbsrsv_buffer_size()](level2.html#rocsparse__bsrsv_8h_1aa0d8d2b089478eaa357c7ca0f2d1332e)and[rocsparse_Xbsric0_buffer_size()](#rocsparse__bsric0_8h_1a795bc27abdfcb87d4b66dbd8cdb2c92f)if the matrix sparsity pattern is identical. The user allocated buffer can thus be shared between subsequent calls to those functions.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dir**–**[in]**direction that specifies whether to count nonzero elements by[rocsparse_direction_row](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca40d95f05d0cd4ad3c89465959c58943e)or by[rocsparse_direction_column](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca23355bb7b606c550ba61c781bcecfc5b).**mb**–**[in]**number of block rows in the sparse BSR matrix.**nnzb**–**[in]**number of non-zero block entries of the sparse BSR matrix.**descr**–**[in]**descriptor of the sparse BSR matrix.**bsr_val**–**[in]**array of length`nnzb*block_dim*block_dim`

containing the values of the sparse BSR matrix.**bsr_row_ptr**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix.**bsr_col_ind**–**[in]**array of`nnzb`

elements containing the block column indices of the sparse BSR matrix.**block_dim**–**[in]**the block dimension of the BSR matrix. Between 1 and m where`m=mb*block_dim`

.**info**–**[out]**structure that holds the information collected during the analysis step.**buffer_size**–**[out]**number of bytes of the temporary storage buffer required by[rocsparse_Xbsrilu0_analysis()](#rocsparse__bsrilu0_8h_1ac20c3e0a79507660dea8895f4111f170)and[rocsparse_Xbsrilu0()](#rocsparse__bsrilu0_8h_1a26ae3e54761e7f15b9dac27d0f51d337).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`mb`

,`nnzb`

, or`block_dim`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`bsr_val`

,`bsr_row_ptr`

,`bsr_col_ind`

,`info`

or`buffer_size`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_not_implemented**–[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_bsrilu0_analysis()[#](#rocsparse-bsrilu0-analysis)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sbsrilu0_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_analysis_policy](enumerations.html#_CPPv425rocsparse_analysis_policy)analysis,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)solve, void *temp_buffer)[#](#_CPPv427rocsparse_sbsrilu0_analysis16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dbsrilu0_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_analysis_policy](enumerations.html#_CPPv425rocsparse_analysis_policy)analysis,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)solve, void *temp_buffer)[#](#_CPPv427rocsparse_dbsrilu0_analysis16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cbsrilu0_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_analysis_policy](enumerations.html#_CPPv425rocsparse_analysis_policy)analysis,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)solve, void *temp_buffer)[#](#_CPPv427rocsparse_cbsrilu0_analysis16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zbsrilu0_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_analysis_policy](enumerations.html#_CPPv425rocsparse_analysis_policy)analysis,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)solve, void *temp_buffer)[#](#_CPPv427rocsparse_zbsrilu0_analysis16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv) `rocsparse_bsrilu0_analysis`

performs the analysis step for[rocsparse_Xbsrilu0()](#rocsparse__bsrilu0_8h_1a26ae3e54761e7f15b9dac27d0f51d337). It is expected that this function will be executed only once for a given matrix. The analysis meta data can be cleared by[rocsparse_bsrilu0_clear()](#rocsparse__bsrilu0_8h_1a2b91f9c0baf4c1f951223a2c62bc738b).`rocsparse_bsrilu0_analysis`

can share its meta data with[rocsparse_Xbsric0_analysis()](#rocsparse__bsric0_8h_1a9cfb58036bb689f2becba8c0baa9d716),[rocsparse_Xbsrsv_analysis()](level2.html#rocsparse__bsrsv_8h_1aade89276269f88cd50e357c0a3504c87), and[rocsparse_Xbsrsm_analysis()](level3.html#rocsparse__bsrsm_8h_1aa7c3da4c56f9dcf7aaae3e65dd35110f). Selecting[rocsparse_analysis_policy_reuse](enumerations.html#rocsparse-types_8h_1a43b20aa4bb19623a91b5952422fbe35ca658466413f4005c0c103d20d5e352078)policy can greatly improve computation performance of meta data. However, the user needs to make sure that the sparsity pattern remains unchanged. If this cannot be assured,[rocsparse_analysis_policy_force](enumerations.html#rocsparse-types_8h_1a43b20aa4bb19623a91b5952422fbe35cac66b70c4f519ddd03dcbe0f3a973401a)has to be used.Note

If the matrix sparsity pattern changes, the gathered information will become invalid.

Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dir**–**[in]**direction that specified whether to count nonzero elements by[rocsparse_direction_row](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca40d95f05d0cd4ad3c89465959c58943e)or by[rocsparse_direction_column](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca23355bb7b606c550ba61c781bcecfc5b).**mb**–**[in]**number of block rows in the sparse BSR matrix.**nnzb**–**[in]**number of non-zero block entries of the sparse BSR matrix.**descr**–**[in]**descriptor of the sparse BSR matrix.**bsr_val**–**[in]**array of length`nnzb*block_dim*block_dim`

containing the values of the sparse BSR matrix.**bsr_row_ptr**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix.**bsr_col_ind**–**[in]**array of`nnzb`

elements containing the block column indices of the sparse BSR matrix.**block_dim**–**[in]**the block dimension of the BSR matrix. Between 1 and m where`m=mb*block_dim`

.**info**–**[out]**structure that holds the information collected during the analysis step.**analysis**–**[in]**[rocsparse_analysis_policy_reuse](enumerations.html#rocsparse-types_8h_1a43b20aa4bb19623a91b5952422fbe35ca658466413f4005c0c103d20d5e352078)or[rocsparse_analysis_policy_force](enumerations.html#rocsparse-types_8h_1a43b20aa4bb19623a91b5952422fbe35cac66b70c4f519ddd03dcbe0f3a973401a).**solve**–**[in]**[rocsparse_solve_policy_auto](enumerations.html#rocsparse-types_8h_1a5a3e261123e81a9e8b267c6109e26957a9c6bdf97e192d429ca536d5ab98ea866).**temp_buffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`mb`

,`nnzb`

, or`block_dim`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`bsr_val`

,`bsr_row_ptr`

,`bsr_col_ind`

,`info`

or`temp_buffer`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_not_implemented**–[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_bsrilu0()[#](#rocsparse-bsrilu0)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sbsrilu0([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, float *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv418rocsparse_sbsrilu016rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPfPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_info22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dbsrilu0([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, double *bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv418rocsparse_dbsrilu016rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPdPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_info22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cbsrilu0([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv418rocsparse_cbsrilu016rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrP23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_info22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zbsrilu0([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)dir,[rocsparse_int](types.html#_CPPv413rocsparse_int)mb,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnzb, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*bsr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*bsr_col_ind,[rocsparse_int](types.html#_CPPv413rocsparse_int)block_dim,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv418rocsparse_zbsrilu016rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrP24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_info22rocsparse_solve_policyPv) Incomplete LU factorization with 0 fill-ins and no pivoting using BSR storage format.

`rocsparse_bsrilu0`

computes the incomplete LU factorization with 0 fill-ins and no pivoting of a sparse \(mb \times mb\) BSR matrix \(A\), such that\[ A \approx LU \]Computing the above incomplete LU factorization requires three steps to complete. First, the user determines the size of the required temporary storage buffer by calling

[rocsparse_Xbsrilu0_buffer_size()](#rocsparse__bsrilu0_8h_1a71976ed155de1fc6a71c79144a546cdb). Once this buffer size has been determined, the user allocates the buffer and passes it to[rocsparse_Xbsrilu0_analysis()](#rocsparse__bsrilu0_8h_1ac20c3e0a79507660dea8895f4111f170). This will perform analysis on the sparsity pattern of the matrix. Finally, the user calls`rocsparse_sbsrilu0`

,`rocsparse_dbsrilu0`

,`rocsparse_cbsrilu0`

, or`rocsparse_zbsrilu0`

to perform the actual factorization. The calculation of the buffer size and the analysis of the sparse matrix only need to be performed once for a given sparsity pattern while the factorization can be repeatedly applied to multiple matrices having the same sparsity pattern. Once all calls to[rocsparse_Xbsrilu0()](#rocsparse__bsrilu0_8h_1a26ae3e54761e7f15b9dac27d0f51d337)are complete, the temporary buffer can be deallocated.`rocsparse_bsrilu0`

reports the first zero pivot (either numerical or structural zero). The zero pivot status can be obtained by calling[rocsparse_bsrilu0_zero_pivot()](#rocsparse__bsrilu0_8h_1a1108eb9557a87028c21cbaa258fe9cb9).**Example**Consider the sparse \(m \times m\) matrix \(A\), stored in BSR storage format. The following example computes the incomplete LU factorization \(M \approx LU\) and solves the preconditioned system \(My = x\).

int main() { // 2 1 0 0 // A = 1 2 0 0 // 0 0 2 1 // 0 0 1 2 int mb = 2; int nb = 2; int nnzb = 2; int block_dim = 2; double alpha = 1.0; std::vector<int> hbsr_row_ptr = {0, 1, 2}; std::vector<int> hbsr_col_ind = {0, 1}; std::vector<double> hbsr_val = {2.0, 1.0, 1.0, 2.0, 2.0, 1.0, 1.0, 2.0}; std::vector<double> hx(mb * block_dim, 1.0); int* dbsr_row_ptr; int* dbsr_col_ind; double* dbsr_val; double* dx; double* dy; double* dz; HIP_CHECK(hipMalloc(&dbsr_row_ptr, sizeof(int) * (mb + 1))); HIP_CHECK(hipMalloc(&dbsr_col_ind, sizeof(int) * nnzb)); HIP_CHECK(hipMalloc(&dbsr_val, sizeof(double) * nnzb * block_dim * block_dim)); HIP_CHECK(hipMalloc(&dx, sizeof(double) * mb * block_dim)); HIP_CHECK(hipMalloc(&dy, sizeof(double) * mb * block_dim)); HIP_CHECK(hipMalloc(&dz, sizeof(double) * mb * block_dim)); HIP_CHECK(hipMemcpy( dbsr_row_ptr, hbsr_row_ptr.data(), sizeof(int) * (mb + 1), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dbsr_col_ind, hbsr_col_ind.data(), sizeof(int) * nnzb, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dbsr_val, hbsr_val.data(), sizeof(double) * nnzb * block_dim * block_dim, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dx, hx.data(), sizeof(double) * mb * block_dim, hipMemcpyHostToDevice)); // Create rocSPARSE handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Create matrix descriptor for M rocsparse_mat_descr descr_M; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr_M)); // Create matrix descriptor for L rocsparse_mat_descr descr_L; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr_L)); ROCSPARSE_CHECK(rocsparse_set_mat_fill_mode(descr_L, rocsparse_fill_mode_lower)); ROCSPARSE_CHECK(rocsparse_set_mat_diag_type(descr_L, rocsparse_diag_type_unit)); // Create matrix descriptor for U rocsparse_mat_descr descr_U; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr_U)); ROCSPARSE_CHECK(rocsparse_set_mat_fill_mode(descr_U, rocsparse_fill_mode_upper)); ROCSPARSE_CHECK(rocsparse_set_mat_diag_type(descr_U, rocsparse_diag_type_non_unit)); // Create matrix info structure rocsparse_mat_info info; ROCSPARSE_CHECK(rocsparse_create_mat_info(&info)); // Obtain required buffer size size_t buffer_size_M; size_t buffer_size_L; size_t buffer_size_U; ROCSPARSE_CHECK(rocsparse_dbsrilu0_buffer_size(handle, rocsparse_direction_row, mb, nnzb, descr_M, dbsr_val, dbsr_row_ptr, dbsr_col_ind, block_dim, info, &buffer_size_M)); ROCSPARSE_CHECK(rocsparse_dbsrsv_buffer_size(handle, rocsparse_direction_row, rocsparse_operation_none, mb, nnzb, descr_L, dbsr_val, dbsr_row_ptr, dbsr_col_ind, block_dim, info, &buffer_size_L)); ROCSPARSE_CHECK(rocsparse_dbsrsv_buffer_size(handle, rocsparse_direction_row, rocsparse_operation_none, mb, nnzb, descr_U, dbsr_val, dbsr_row_ptr, dbsr_col_ind, block_dim, info, &buffer_size_U)); size_t buffer_size = max(buffer_size_M, max(buffer_size_L, buffer_size_U)); // Allocate temporary buffer void* temp_buffer; HIP_CHECK(hipMalloc(&temp_buffer, buffer_size)); // Perform analysis steps, using rocsparse_analysis_policy_reuse to improve // computation performance ROCSPARSE_CHECK(rocsparse_dbsrilu0_analysis(handle, rocsparse_direction_row, mb, nnzb, descr_M, dbsr_val, dbsr_row_ptr, dbsr_col_ind, block_dim, info, rocsparse_analysis_policy_reuse, rocsparse_solve_policy_auto, temp_buffer)); ROCSPARSE_CHECK(rocsparse_dbsrsv_analysis(handle, rocsparse_direction_row, rocsparse_operation_none, mb, nnzb, descr_L, dbsr_val, dbsr_row_ptr, dbsr_col_ind, block_dim, info, rocsparse_analysis_policy_reuse, rocsparse_solve_policy_auto, temp_buffer)); ROCSPARSE_CHECK(rocsparse_dbsrsv_analysis(handle, rocsparse_direction_row, rocsparse_operation_none, mb, nnzb, descr_U, dbsr_val, dbsr_row_ptr, dbsr_col_ind, block_dim, info, rocsparse_analysis_policy_reuse, rocsparse_solve_policy_auto, temp_buffer)); // Check for zero pivot rocsparse_int position; if(rocsparse_status_zero_pivot == rocsparse_bsrilu0_zero_pivot(handle, info, &position)) { printf("A has structural zero at A(%d,%d)\n", position, position); } // Compute incomplete LU factorization M = LU ROCSPARSE_CHECK(rocsparse_dbsrilu0(handle, rocsparse_direction_row, mb, nnzb, descr_M, dbsr_val, dbsr_row_ptr, dbsr_col_ind, block_dim, info, rocsparse_solve_policy_auto, temp_buffer)); // Check for zero pivot if(rocsparse_status_zero_pivot == rocsparse_bsrilu0_zero_pivot(handle, info, &position)) { printf("L has structural and/or numerical zero at L(%d,%d)\n", position, position); } // Solve Lz = x ROCSPARSE_CHECK(rocsparse_dbsrsv_solve(handle, rocsparse_direction_row, rocsparse_operation_none, mb, nnzb, &alpha, descr_L, dbsr_val, dbsr_row_ptr, dbsr_col_ind, block_dim, info, dx, dz, rocsparse_solve_policy_auto, temp_buffer)); // Solve Uy = z ROCSPARSE_CHECK(rocsparse_dbsrsv_solve(handle, rocsparse_direction_row, rocsparse_operation_none, mb, nnzb, &alpha, descr_U, dbsr_val, dbsr_row_ptr, dbsr_col_ind, block_dim, info, dz, dy, rocsparse_solve_policy_auto, temp_buffer)); std::vector<double> hy(mb * block_dim); HIP_CHECK(hipMemcpy(hy.data(), dy, sizeof(double) * mb * block_dim, hipMemcpyDeviceToHost)); std::cout << "hy" << std::endl; for(size_t i = 0; i < hy.size(); i++) { std::cout << hy[i] << " "; } std::cout << "" << std::endl; // Clean up ROCSPARSE_CHECK(rocsparse_destroy_mat_info(info)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr_M)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr_L)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr_U)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); HIP_CHECK(hipFree(dbsr_row_ptr)); HIP_CHECK(hipFree(dbsr_col_ind)); HIP_CHECK(hipFree(dbsr_val)); HIP_CHECK(hipFree(dx)); HIP_CHECK(hipFree(dy)); HIP_CHECK(hipFree(dz)); HIP_CHECK(hipFree(temp_buffer)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dir**–**[in]**direction that specified whether to count nonzero elements by[rocsparse_direction_row](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca40d95f05d0cd4ad3c89465959c58943e)or by[rocsparse_direction_column](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca23355bb7b606c550ba61c781bcecfc5b).**mb**–**[in]**number of block rows in the sparse BSR matrix.**nnzb**–**[in]**number of non-zero block entries of the sparse BSR matrix.**descr**–**[in]**descriptor of the sparse BSR matrix.**bsr_val**–**[inout]**array of length`nnzb*block_dim*block_dim`

containing the values of the sparse BSR matrix.**bsr_row_ptr**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix.**bsr_col_ind**–**[in]**array of`nnzb`

elements containing the block column indices of the sparse BSR matrix.**block_dim**–**[in]**the block dimension of the BSR matrix. Between 1 and m where`m=mb*block_dim`

.**info**–**[in]**structure that holds the information collected during the analysis step.**policy**–**[in]**[rocsparse_solve_policy_auto](enumerations.html#rocsparse-types_8h_1a5a3e261123e81a9e8b267c6109e26957a9c6bdf97e192d429ca536d5ab98ea866).**temp_buffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`mb`

,`nnzb`

, or`block_dim`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`bsr_val`

,`bsr_row_ptr`

or`bsr_col_ind`

pointer is invalid.**rocsparse_status_arch_mismatch**– the device is not supported.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_not_implemented**–[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_bsrilu0_clear()[#](#rocsparse-bsrilu0-clear)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_bsrilu0_clear([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info)[#](#_CPPv423rocsparse_bsrilu0_clear16rocsparse_handle18rocsparse_mat_info) `rocsparse_bsrilu0_clear`

deallocates all memory that was allocated by[rocsparse_Xbsrilu0_analysis()](#rocsparse__bsrilu0_8h_1ac20c3e0a79507660dea8895f4111f170). This is especially useful, if memory is an issue and the analysis data is not required for further computation.Note

Calling

`rocsparse_bsrilu0_clear`

is optional. All allocated resources will be cleared, when the opaque[rocsparse_mat_info](types.html#rocsparse-types_8h_1a3347be72f6e4f3c55318c32b46dcaa92)struct is destroyed using[rocsparse_destroy_mat_info()](auxiliary.html#rocsparse-auxiliary_8h_1a9c143f65076a10ebafcffc633ad5d87b).Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**info**–**[inout]**structure that holds the information collected during the analysis step.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`info`

pointer is invalid.**rocsparse_status_memory_error**– the buffer holding the meta data could not be deallocated.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_csric0_zero_pivot()[#](#rocsparse-csric0-zero-pivot)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_csric0_zero_pivot([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_int](types.html#_CPPv413rocsparse_int)*position)[#](#_CPPv427rocsparse_csric0_zero_pivot16rocsparse_handle18rocsparse_mat_infoP13rocsparse_int) `rocsparse_csric_zero_pivot`

returns[rocsparse_status_zero_pivot](enumerations.html#rocsparse-types_8h_1a578f8c5c1b08f358bf4605b0031006a8a01fe264830c8ce6451ce6888bc8d3e80), if either a structural or numerical zero has been found during[rocsparse_Xcsric0()](#rocsparse__csric0_8h_1a6d61446c1a2eb58d242e0a1b0640ebda)computation. The first zero pivot \(j\) at \(A_{j,j}\) is stored in`position`

, using same index base as the CSR matrix.`position`

can be in host or device memory. If no zero pivot has been found,`position`

is set to -1 and[rocsparse_status_success](enumerations.html#rocsparse-types_8h_1a578f8c5c1b08f358bf4605b0031006a8a96462a9361cfceb6cf9354e10fdc671b)is returned instead.Note

`rocsparse_csric0_zero_pivot`

is a blocking function. It might influence performance negatively.Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**info**–**[in]**structure that holds the information collected during the analysis step.**position**–**[inout]**pointer to zero pivot \(j\), can be in host or device memory.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`info`

or`position`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_zero_pivot**– zero pivot has been found.



## rocsparse_csric0_singular_pivot()[#](#rocsparse-csric0-singular-pivot)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_csric0_singular_pivot([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_int](types.html#_CPPv413rocsparse_int)*position)[#](#_CPPv431rocsparse_csric0_singular_pivot16rocsparse_handle18rocsparse_mat_infoP13rocsparse_int)

returns the position of a numerical singular pivot (where \(|L_{j,j}| \leq \text{tolerance}\)) that has been found during[rocsparse_csric0_singular_pivot()](#rocsparse__csric0_8h_1a5c1b5fe5ab2189cbb5e0aa28873d677b)[rocsparse_Xcsric0()](#rocsparse__csric0_8h_1a6d61446c1a2eb58d242e0a1b0640ebda)computation. The first singular pivot \(j\) at \(L_{j,j}\) is stored in`position`

, using same index base as the CSR matrix.`position`

can be in host or device memory. If no singular pivot has been found,`position`

is set to -1.Note


is a blocking function. It might influence performance negatively.[rocsparse_csric0_singular_pivot()](#rocsparse__csric0_8h_1a5c1b5fe5ab2189cbb5e0aa28873d677b)Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**info**–**[in]**structure that holds the information collected during the analysis step.**position**–**[inout]**pointer to singular pivot \(k\), can be in host or device memory.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`info`

or`position`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_csric0_set_tolerance()[#](#rocsparse-csric0-set-tolerance)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_csric0_set_tolerance([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, double tolerance)[#](#_CPPv430rocsparse_csric0_set_tolerance16rocsparse_handle18rocsparse_mat_infod)

sets the numerical tolerance for detecting a numerical singular pivot (where \(|L_{j,j}| \leq \text{tolerance}\)) that might be found during[rocsparse_csric0_set_tolerance()](#rocsparse__csric0_8h_1a517964d418167436823664e306578cc9)[rocsparse_Xcsric0()](#rocsparse__csric0_8h_1a6d61446c1a2eb58d242e0a1b0640ebda)computation.Note


is a blocking function. It might influence performance negatively.[rocsparse_csric0_set_tolerance()](#rocsparse__csric0_8h_1a517964d418167436823664e306578cc9)Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**info**–**[in]**structure that holds the information collected during the analysis step.**tolerance**–**[in]**tolerance for detecting singular pivot ( \(|L_{j,j}| \leq \text{tolerance}\))

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**– if`info`

tolerance pointer is invalid



## rocsparse_csric0_get_tolerance()[#](#rocsparse-csric0-get-tolerance)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_csric0_get_tolerance([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, double *tolerance)[#](#_CPPv430rocsparse_csric0_get_tolerance16rocsparse_handle18rocsparse_mat_infoPd)

returns the numerical tolerance for detecting a numerical singular pivot (where \(|L_{j,j}| \leq \text{tolerance}\)) that might be found during[rocsparse_csric0_get_tolerance()](#rocsparse__csric0_8h_1afc19ab4abff2d71eb154d7ddca044463)[rocsparse_Xcsric0()](#rocsparse__csric0_8h_1a6d61446c1a2eb58d242e0a1b0640ebda)computation.Note


is a blocking function. It might influence performance negatively.[rocsparse_csric0_get_tolerance()](#rocsparse__csric0_8h_1afc19ab4abff2d71eb154d7ddca044463)Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**info**–**[in]**structure that holds the information collected during the analysis step.**tolerance**–**[out]**obtain tolerance for detecting singular pivot ( \(|L_{j,j}| \leq \text{tolerance}\))

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**– if`info`

or`tolerance`

pointer is invalid



## rocsparse_csric0_buffer_size()[#](#rocsparse-csric0-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scsric0_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, size_t *buffer_size)[#](#_CPPv429rocsparse_scsric0_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcsric0_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, size_t *buffer_size)[#](#_CPPv429rocsparse_dcsric0_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccsric0_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, size_t *buffer_size)[#](#_CPPv429rocsparse_ccsric0_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcsric0_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, size_t *buffer_size)[#](#_CPPv429rocsparse_zcsric0_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoP6size_t) `rocsparse_csric0_buffer_size`

returns the size of the temporary storage buffer that is required by[rocsparse_Xcsric0_analysis()](#rocsparse__csric0_8h_1a00bf19a537e0d46b1c55826a9c23e23c). The temporary storage buffer must be allocated by the user. The size of the temporary storage buffer is identical to the size returned by[rocsparse_Xcsrsv_buffer_size()](level2.html#rocsparse__csrsv_8h_1ac74b51be59a42a0387648ac79d633b5e)and[rocsparse_Xcsrilu0_buffer_size()](#rocsparse__csrilu0_8h_1a75eebaa5a02b9f1f9a05ff440ceef387)if the matrix sparsity pattern is identical. The user allocated buffer can thus be shared between subsequent calls to those functions.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**descr**–**[in]**descriptor of the sparse CSR matrix.**csr_val**–**[in]**array of`nnz`

elements of the sparse CSR matrix.**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csr_col_ind**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**info**–**[out]**structure that holds the information collected during the analysis step.**buffer_size**–**[out]**number of bytes of the temporary storage buffer required by[rocsparse_Xcsric0_analysis()](#rocsparse__csric0_8h_1a00bf19a537e0d46b1c55826a9c23e23c)and[rocsparse_Xcsric0()](#rocsparse__csric0_8h_1a6d61446c1a2eb58d242e0a1b0640ebda).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`csr_val`

,`csr_row_ptr`

,`csr_col_ind`

,`info`

or`buffer_size`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_not_implemented**–[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_csric0_analysis()[#](#rocsparse-csric0-analysis)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scsric0_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_analysis_policy](enumerations.html#_CPPv425rocsparse_analysis_policy)analysis,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)solve, void *temp_buffer)[#](#_CPPv426rocsparse_scsric0_analysis16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcsric0_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_analysis_policy](enumerations.html#_CPPv425rocsparse_analysis_policy)analysis,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)solve, void *temp_buffer)[#](#_CPPv426rocsparse_dcsric0_analysis16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccsric0_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_analysis_policy](enumerations.html#_CPPv425rocsparse_analysis_policy)analysis,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)solve, void *temp_buffer)[#](#_CPPv426rocsparse_ccsric0_analysis16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcsric0_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_analysis_policy](enumerations.html#_CPPv425rocsparse_analysis_policy)analysis,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)solve, void *temp_buffer)[#](#_CPPv426rocsparse_zcsric0_analysis16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv) `rocsparse_csric0_analysis`

performs the analysis step for[rocsparse_Xcsric0()](#rocsparse__csric0_8h_1a6d61446c1a2eb58d242e0a1b0640ebda). It is expected that this function will be executed only once for a given matrix and particular operation type. The analysis meta data can be cleared by[rocsparse_csric0_clear()](#rocsparse__csric0_8h_1a36406e44f237904f507a934ee0d94ea1).`rocsparse_csric0_analysis`

can share its meta data with[rocsparse_Xcsrilu0_analysis()](#rocsparse__csrilu0_8h_1a8b0496cb644c23fe65176e70315e431c),[rocsparse_Xcsrsv_analysis()](level2.html#rocsparse__csrsv_8h_1af710dcbc752ca8203389907bcbe74273), and[rocsparse_Xcsrsm_analysis()](level3.html#rocsparse__csrsm_8h_1ac8e943e992641859efdfea49a267133b). Selecting[rocsparse_analysis_policy_reuse](enumerations.html#rocsparse-types_8h_1a43b20aa4bb19623a91b5952422fbe35ca658466413f4005c0c103d20d5e352078)policy can greatly improve computation performance of meta data. However, the user needs to make sure that the sparsity pattern remains unchanged. If this cannot be assured,[rocsparse_analysis_policy_force](enumerations.html#rocsparse-types_8h_1a43b20aa4bb19623a91b5952422fbe35cac66b70c4f519ddd03dcbe0f3a973401a)has to be used.Note

If the matrix sparsity pattern changes, the gathered information will become invalid.

Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**descr**–**[in]**descriptor of the sparse CSR matrix.**csr_val**–**[in]**array of`nnz`

elements of the sparse CSR matrix.**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csr_col_ind**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**info**–**[out]**structure that holds the information collected during the analysis step.**analysis**–**[in]**[rocsparse_analysis_policy_reuse](enumerations.html#rocsparse-types_8h_1a43b20aa4bb19623a91b5952422fbe35ca658466413f4005c0c103d20d5e352078)or[rocsparse_analysis_policy_force](enumerations.html#rocsparse-types_8h_1a43b20aa4bb19623a91b5952422fbe35cac66b70c4f519ddd03dcbe0f3a973401a).**solve**–**[in]**[rocsparse_solve_policy_auto](enumerations.html#rocsparse-types_8h_1a5a3e261123e81a9e8b267c6109e26957a9c6bdf97e192d429ca536d5ab98ea866).**temp_buffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`csr_val`

,`csr_row_ptr`

,`csr_col_ind`

,`info`

or`temp_buffer`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_not_implemented**–[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_csric0()[#](#rocsparse-csric0)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scsric0([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, float *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv417rocsparse_scsric016rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPfPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_info22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcsric0([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, double *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv417rocsparse_dcsric016rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPdPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_info22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccsric0([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv417rocsparse_ccsric016rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrP23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_info22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcsric0([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv417rocsparse_zcsric016rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrP24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_info22rocsparse_solve_policyPv) Incomplete Cholesky factorization with 0 fill-ins and no pivoting using CSR storage format.

`rocsparse_csric0`

computes the incomplete Cholesky factorization with 0 fill-ins and no pivoting of a sparse \(m \times m\) CSR matrix \(A\), such that\[ A \approx LL^T \]where the lower triangular matrix \(L\) is computed using:\[\begin{split} L_{ij} = \left\{ \begin{array}{ll} \sqrt{A_{jj} - \sum_{k=0}^{j-1}(L_{jk})^{2}}, & \text{if i == j} \\ \frac{1}{L_{jj}}(A_{jj} - \sum_{k=0}^{j-1}L_{ik} \times L_{jk}), & \text{if i > j} \end{array} \right. \end{split}\]for each entry found in the CSR matrix \(A\).Computing the above incomplete Cholesky factorization requires three steps to complete. First, the user determines the size of the required temporary storage buffer by calling

[rocsparse_Xcsric0_buffer_size()](#rocsparse__csric0_8h_1a2e7bbf0d8c1c1542facd95b37b461078). Once this buffer size has been determined, the user allocates the buffer and passes it to[rocsparse_Xcsric0_analysis()](#rocsparse__csric0_8h_1a00bf19a537e0d46b1c55826a9c23e23c). This will perform analysis on the sparsity pattern of the matrix. Finally, the user calls`rocsparse_scsric0`

,`rocsparse_dcsric0`

,`rocsparse_ccsric0`

, or`rocsparse_zcsric0`

to perform the actual factorization. The calculation of the buffer size and the analysis of the sparse matrix only need to be performed once for a given sparsity pattern while the factorization can be repeatedly applied to multiple matrices having the same sparsity pattern. Once all calls to[rocsparse_Xcsric0()](#rocsparse__csric0_8h_1a6d61446c1a2eb58d242e0a1b0640ebda)are complete, the temporary buffer can be deallocated.When computing the Cholesky factorization, it is possible that \(L_{jj} == 0\) which would result in a division by zero. This could occur from either \(A_{jj}\) not existing in the sparse CSR matrix (referred to as a structural zero) or because \(A_{jj} - \sum_{k=0}^{j-1}(L_{jk})^{2} == 0\) (referred to as a numerical zero). For example, running the Cholesky factorization on the following matrix:

\[\begin{split} \begin{bmatrix} 2 & 1 & 0 \\ 1 & 2 & 1 \\ 0 & 1 & 2 \end{bmatrix} \end{split}\]results in a successful Cholesky factorization, however running with the matrix:\[\begin{split} \begin{bmatrix} 2 & 1 & 0 \\ 1 & 1/2 & 1 \\ 0 & 1 & 2 \end{bmatrix} \end{split}\]results in a numerical zero because:\[\begin{split} \begin{array}{ll} L_{00} &= \sqrt{2} \\ L_{10} &= \frac{1}{\sqrt{2}} \\ L_{11} &= \sqrt{\frac{1}{2} - (\frac{1}{\sqrt{2}})^2} &= 0 \end{array} \end{split}\]The user can detect the presence of a structural zero by calling[rocsparse_csric0_zero_pivot()](#rocsparse__csric0_8h_1a2d5dd20d3f9915040de2067cba681de9)after[rocsparse_Xcsric0_analysis()](#rocsparse__csric0_8h_1a00bf19a537e0d46b1c55826a9c23e23c)and/or the presence of a structural or numerical zero by calling[rocsparse_csric0_zero_pivot()](#rocsparse__csric0_8h_1a2d5dd20d3f9915040de2067cba681de9)after[rocsparse_Xcsric0()](#rocsparse__csric0_8h_1a6d61446c1a2eb58d242e0a1b0640ebda):In both cases,rocsparse_dcsric0(handle, m, nnz, descr_M, csr_val, csr_row_ptr, csr_col_ind, info, rocsparse_solve_policy_auto, temp_buffer); // Check for zero pivot if(rocsparse_status_zero_pivot == rocsparse_csric0_zero_pivot(handle, info, &position)) { printf("L has structural and/or numerical zero at L(%d,%d)\n", position, position); }

[rocsparse_csric0_zero_pivot()](#rocsparse__csric0_8h_1a2d5dd20d3f9915040de2067cba681de9)will report the first zero pivot (either numerical or structural) found. See full example below. The user can also set the diagonal type to be \(1\) using[rocsparse_set_mat_diag_type()](auxiliary.html#rocsparse-auxiliary_8h_1a61f894d80e4da74c7e8cd43f61f9215c)which will interpret the matrix \(A\) as having ones on its diagonal (even if no nonzero exists in the sparsity pattern).`rocsparse_csric0`

computes the Cholesky factorization inplace meaning that the values array`csr_val`

of the \(A\) matrix is overwritten with the \(L\) matrix stored in the lower triangular part of \(A\):\[\begin{split} \begin{align} \begin{bmatrix} a_{00} & a_{01} & a_{02} \\ a_{10} & a_{11} & a_{12} \\ a_{20} & a_{21} & a_{22} \end{bmatrix} \rightarrow \begin{bmatrix} l_{00} & a_{01} & a_{02} \\ l_{10} & l_{11} & a_{12} \\ l_{20} & l_{21} & l_{22} \end{bmatrix} \end{align} \end{split}\]The row pointer array`csr_row_ptr`

and the column indices array`csr_col_ind`

remain the same for \(A\) and the output as the incomplete factorization does not generate new nonzeros in the output which do not already exist in \(A\).The performance of computing Cholesky factorization with rocSPARSE greatly depends on the sparisty pattern the the matrix \(A\) as this is what determines the amount of parallelism available.

**Example**Consider the sparse \(m \times m\) matrix \(A\), stored in CSR storage format. The following example computes the incomplete Cholesky factorization \(M \approx LL^T\) and solves the preconditioned system \(My = x\).

int main() { // 2 1 0 0 // A = 1 2 1 0 // 0 1 2 1 // 0 0 1 2 int m = 4; int n = 4; double alpha = 1.0; std::vector<int> hcsr_row_ptr = {0, 2, 5, 8, 10}; std::vector<int> hcsr_col_ind = {0, 1, 0, 1, 2, 1, 2, 3, 2, 3}; std::vector<double> hcsr_val = {2.0, 1.0, 1.0, 2.0, 1.0, 1.0, 2.0, 1.0, 1.0, 2.0}; int nnz = hcsr_row_ptr[m] - hcsr_row_ptr[0]; std::vector<double> hx(m, 1.0); int* dcsr_row_ptr; int* dcsr_col_ind; double* dcsr_val; double* dx; double* dy; double* dz; HIP_CHECK(hipMalloc(&dcsr_row_ptr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc(&dcsr_col_ind, sizeof(int) * nnz)); HIP_CHECK(hipMalloc(&dcsr_val, sizeof(double) * nnz)); HIP_CHECK(hipMalloc(&dx, sizeof(double) * m)); HIP_CHECK(hipMalloc(&dy, sizeof(double) * m)); HIP_CHECK(hipMalloc(&dz, sizeof(double) * m)); HIP_CHECK( hipMemcpy(dcsr_row_ptr, hcsr_row_ptr.data(), sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsr_col_ind, hcsr_col_ind.data(), sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsr_val, hcsr_val.data(), sizeof(double) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dx, hx.data(), sizeof(double) * m, hipMemcpyHostToDevice)); // Create rocSPARSE handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Create matrix descriptor for M rocsparse_mat_descr descr_M; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr_M)); // Create matrix descriptor for L rocsparse_mat_descr descr_L; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr_L)); ROCSPARSE_CHECK(rocsparse_set_mat_fill_mode(descr_L, rocsparse_fill_mode_lower)); ROCSPARSE_CHECK(rocsparse_set_mat_diag_type(descr_L, rocsparse_diag_type_non_unit)); // Create matrix descriptor for L' rocsparse_mat_descr descr_Lt; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr_Lt)); ROCSPARSE_CHECK(rocsparse_set_mat_fill_mode(descr_Lt, rocsparse_fill_mode_lower)); ROCSPARSE_CHECK(rocsparse_set_mat_diag_type(descr_Lt, rocsparse_diag_type_non_unit)); // Create matrix info structure rocsparse_mat_info info; ROCSPARSE_CHECK(rocsparse_create_mat_info(&info)); // Obtain required buffer size size_t buffer_size_M; size_t buffer_size_L; size_t buffer_size_Lt; ROCSPARSE_CHECK(rocsparse_dcsric0_buffer_size( handle, m, nnz, descr_M, dcsr_val, dcsr_row_ptr, dcsr_col_ind, info, &buffer_size_M)); ROCSPARSE_CHECK(rocsparse_dcsrsv_buffer_size(handle, rocsparse_operation_none, m, nnz, descr_L, dcsr_val, dcsr_row_ptr, dcsr_col_ind, info, &buffer_size_L)); ROCSPARSE_CHECK(rocsparse_dcsrsv_buffer_size(handle, rocsparse_operation_transpose, m, nnz, descr_Lt, dcsr_val, dcsr_row_ptr, dcsr_col_ind, info, &buffer_size_Lt)); size_t buffer_size = max(buffer_size_M, max(buffer_size_L, buffer_size_Lt)); // Allocate temporary buffer void* temp_buffer; HIP_CHECK(hipMalloc(&temp_buffer, buffer_size)); // Perform analysis steps, using rocsparse_analysis_policy_reuse to improve // computation performance ROCSPARSE_CHECK(rocsparse_dcsric0_analysis(handle, m, nnz, descr_M, dcsr_val, dcsr_row_ptr, dcsr_col_ind, info, rocsparse_analysis_policy_reuse, rocsparse_solve_policy_auto, temp_buffer)); ROCSPARSE_CHECK(rocsparse_dcsrsv_analysis(handle, rocsparse_operation_none, m, nnz, descr_L, dcsr_val, dcsr_row_ptr, dcsr_col_ind, info, rocsparse_analysis_policy_reuse, rocsparse_solve_policy_auto, temp_buffer)); ROCSPARSE_CHECK(rocsparse_dcsrsv_analysis(handle, rocsparse_operation_transpose, m, nnz, descr_Lt, dcsr_val, dcsr_row_ptr, dcsr_col_ind, info, rocsparse_analysis_policy_reuse, rocsparse_solve_policy_auto, temp_buffer)); // Check for zero pivot rocsparse_int position; if(rocsparse_status_zero_pivot == rocsparse_csric0_zero_pivot(handle, info, &position)) { printf("A has structural zero at A(%d,%d)\n", position, position); } // Compute incomplete Cholesky factorization M = LL' ROCSPARSE_CHECK(rocsparse_dcsric0(handle, m, nnz, descr_M, dcsr_val, dcsr_row_ptr, dcsr_col_ind, info, rocsparse_solve_policy_auto, temp_buffer)); // Check for zero pivot if(rocsparse_status_zero_pivot == rocsparse_csric0_zero_pivot(handle, info, &position)) { printf("L has structural and/or numerical zero at L(%d,%d)\n", position, position); } // Copy incomplete LL^T factorization to host (note only lower L is stored and is written inplace into the original matrix) HIP_CHECK( hipMemcpy(hcsr_row_ptr.data(), dcsr_row_ptr, sizeof(int) * (m + 1), hipMemcpyDeviceToHost)); HIP_CHECK( hipMemcpy(hcsr_col_ind.data(), dcsr_col_ind, sizeof(int) * nnz, hipMemcpyDeviceToHost)); HIP_CHECK(hipMemcpy(hcsr_val.data(), dcsr_val, sizeof(double) * nnz, hipMemcpyDeviceToHost)); std::cout << "LL^T" << std::endl; for(int i = 0; i < m; i++) { int start = hcsr_row_ptr[i]; int end = hcsr_row_ptr[i + 1]; std::vector<double> temp(n, 0.0); for(int j = start; j < end; j++) { temp[hcsr_col_ind[j]] = hcsr_val[j]; } for(int j = 0; j < n; j++) { std::cout << temp[j] << " "; } std::cout << std::endl; } std::cout << std::endl; // Solve Lz = x ROCSPARSE_CHECK(rocsparse_dcsrsv_solve(handle, rocsparse_operation_none, m, nnz, &alpha, descr_L, dcsr_val, dcsr_row_ptr, dcsr_col_ind, info, dx, dz, rocsparse_solve_policy_auto, temp_buffer)); // Solve L'y = z ROCSPARSE_CHECK(rocsparse_dcsrsv_solve(handle, rocsparse_operation_transpose, m, nnz, &alpha, descr_Lt, dcsr_val, dcsr_row_ptr, dcsr_col_ind, info, dz, dy, rocsparse_solve_policy_auto, temp_buffer)); std::vector<double> hy(m); HIP_CHECK(hipMemcpy(hy.data(), dy, sizeof(double) * m, hipMemcpyDeviceToHost)); std::cout << "hy" << std::endl; for(size_t i = 0; i < hy.size(); i++) { std::cout << hy[i] << " "; } std::cout << "" << std::endl; // Clean up ROCSPARSE_CHECK(rocsparse_destroy_mat_info(info)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr_M)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr_L)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr_Lt)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); HIP_CHECK(hipFree(dcsr_row_ptr)); HIP_CHECK(hipFree(dcsr_col_ind)); HIP_CHECK(hipFree(dcsr_val)); HIP_CHECK(hipFree(dx)); HIP_CHECK(hipFree(dy)); HIP_CHECK(hipFree(dz)); HIP_CHECK(hipFree(temp_buffer)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**descr**–**[in]**descriptor of the sparse CSR matrix.**csr_val**–**[inout]**array of`nnz`

elements of the sparse CSR matrix.**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csr_col_ind**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**info**–**[in]**structure that holds the information collected during the analysis step.**policy**–**[in]**[rocsparse_solve_policy_auto](enumerations.html#rocsparse-types_8h_1a5a3e261123e81a9e8b267c6109e26957a9c6bdf97e192d429ca536d5ab98ea866).**temp_buffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`csr_val`

,`csr_row_ptr`

or`csr_col_ind`

pointer is invalid.**rocsparse_status_arch_mismatch**– the device is not supported.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_not_implemented**–[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_csric0_clear()[#](#rocsparse-csric0-clear)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_csric0_clear([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info)[#](#_CPPv422rocsparse_csric0_clear16rocsparse_handle18rocsparse_mat_info) `rocsparse_csric0_clear`

deallocates all memory that was allocated by[rocsparse_Xcsric0_analysis()](#rocsparse__csric0_8h_1a00bf19a537e0d46b1c55826a9c23e23c). This is especially useful, if memory is an issue and the analysis data is not required for further computation.Note

Calling

`rocsparse_csric0_clear`

is optional. All allocated resources will be cleared, when the opaque[rocsparse_mat_info](types.html#rocsparse-types_8h_1a3347be72f6e4f3c55318c32b46dcaa92)struct is destroyed using[rocsparse_destroy_mat_info()](auxiliary.html#rocsparse-auxiliary_8h_1a9c143f65076a10ebafcffc633ad5d87b).Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**info**–**[inout]**structure that holds the information collected during the analysis step.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`info`

pointer is invalid.**rocsparse_status_memory_error**– the buffer holding the meta data could not be deallocated.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_csritilu0_buffer_size()[#](#rocsparse-csritilu0-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_csritilu0_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, rocsparse_itilu0_alg alg,[rocsparse_int](types.html#_CPPv413rocsparse_int)option,[rocsparse_int](types.html#_CPPv413rocsparse_int)nmaxiter,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)datatype, size_t *buffer_size)[#](#_CPPv431rocsparse_csritilu0_buffer_size16rocsparse_handle20rocsparse_itilu0_alg13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base18rocsparse_datatypeP6size_t) `rocsparse_csritilu0_buffer_size`

computes the size in bytes of the buffer that has to be allocated by the user. This buffer is then used in[rocsparse_csritilu0_preprocess](#rocsparse__csritilu0_8h_1a9accbedf9d964c6d89d6f02bcf8bbc15),[rocsparse_Xcsritilu0_compute()](#rocsparse__csritilu0_8h_1ad12fb46604e835832dd43c158ab12393),[rocsparse_Xcsritilu0_compute_ex()](#rocsparse__csritilu0_8h_1af45f2191d3a15f646f35816f752d38b3), and[rocsparse_Xcsritilu0_history()](#rocsparse__csritilu0_8h_1a09aa07279c81bfd9a257f15aca0a9cd0).Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**alg**–**[in]**algorithm to use, rocsparse_itilu0_alg**option**–**[in]**combination of enumeration values from rocsparse_itilu0_option.**nmaxiter**–**[in]**maximum number of iterations.**m**–**[in]**number of rows of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csr_col_ind**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**datatype**–**[in]**Type of numerical values,[rocsparse_datatype](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108ed).**buffer_size**–**[out]**size of the temporary storage buffer allocated by the user.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`nnz`

is invalid.**rocsparse_status_invalid_value**–`alg`

,`base`

or datatype is invalid.**rocsparse_status_invalid_pointer**–`csr_row_ptr`

or`csr_col_ind`

pointer is invalid.**rocsparse_status_zero_pivot**– if nnz is zero.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_csritilu0_preprocess()[#](#rocsparse-csritilu0-preprocess)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_csritilu0_preprocess([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, rocsparse_itilu0_alg alg,[rocsparse_int](types.html#_CPPv413rocsparse_int)option,[rocsparse_int](types.html#_CPPv413rocsparse_int)nmaxiter,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)datatype, size_t buffer_size, void *buffer)[#](#_CPPv430rocsparse_csritilu0_preprocess16rocsparse_handle20rocsparse_itilu0_alg13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base18rocsparse_datatype6size_tPv) `rocsparse_csritilu0_preprocess`

computes the information required to run[rocsparse_Xcsritilu0_compute()](#rocsparse__csritilu0_8h_1ad12fb46604e835832dd43c158ab12393), and[rocsparse_Xcsritilu0_compute_ex()](#rocsparse__csritilu0_8h_1af45f2191d3a15f646f35816f752d38b3)and stores it in the buffer.Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**alg**–**[in]**algorithm to use, rocsparse_itilu0_alg**option**–**[in]**combination of enumeration values from rocsparse_itilu0_option.**nmaxiter**–**[in]**maximum number of iterations.**m**–**[in]**number of rows of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csr_col_ind**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**datatype**–**[in]**Type of numerical values,[rocsparse_datatype](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108ed).**buffer_size**–**[in]**size of the storage buffer allocated by the user.**buffer**–**[in]**storage buffer allocated by the user.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_value**–`alg`

,`base`

or datatype is invalid.**rocsparse_status_invalid_size**–`m`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`csr_row_ptr`

or`csr_col_ind`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_zero_pivot**– if missing diagonal element is detected.



## rocsparse_csritilu0_history()[#](#rocsparse-csritilu0-history)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scsritilu0_history([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, rocsparse_itilu0_alg alg,[rocsparse_int](types.html#_CPPv413rocsparse_int)*niter, float *data, size_t buffer_size, void *buffer)[#](#_CPPv428rocsparse_scsritilu0_history16rocsparse_handle20rocsparse_itilu0_algP13rocsparse_intPf6size_tPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcsritilu0_history([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, rocsparse_itilu0_alg alg,[rocsparse_int](types.html#_CPPv413rocsparse_int)*niter, double *data, size_t buffer_size, void *buffer)[#](#_CPPv428rocsparse_dcsritilu0_history16rocsparse_handle20rocsparse_itilu0_algP13rocsparse_intPd6size_tPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccsritilu0_history([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, rocsparse_itilu0_alg alg,[rocsparse_int](types.html#_CPPv413rocsparse_int)*niter, float *data, size_t buffer_size, void *buffer)[#](#_CPPv428rocsparse_ccsritilu0_history16rocsparse_handle20rocsparse_itilu0_algP13rocsparse_intPf6size_tPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcsritilu0_history([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, rocsparse_itilu0_alg alg,[rocsparse_int](types.html#_CPPv413rocsparse_int)*niter, double *data, size_t buffer_size, void *buffer)[#](#_CPPv428rocsparse_zcsritilu0_history16rocsparse_handle20rocsparse_itilu0_algP13rocsparse_intPd6size_tPv) `rocsparse_csritilu0_history`

fetches convergence history data if rocsparse_itilu0_option_convergence_history has been set when calling[rocsparse_Xcsritilu0_compute](#rocsparse__csritilu0_8h_1ad12fb46604e835832dd43c158ab12393)or[rocsparse_Xcsritilu0_compute_ex](#rocsparse__csritilu0_8h_1af45f2191d3a15f646f35816f752d38b3):int options = 0; options |= rocsparse_itilu0_option_stopping_criteria; options |= rocsparse_itilu0_option_compute_nrm_residual; options |= rocsparse_itilu0_option_convergence_history; rocsparse_scsritilu0_compute(handle, alg, options, &nmaxiter, tol, m, nnz, dcsr_row_ptr, dcsr_col_ind, dcsr_val, dilu0, idx_base, buffer_size, dbuffer); if((options & rocsparse_itilu0_option_convergence_history) > 0) { std::vector<float> history(nmaxiter * 2); rocsparse_int history_niter = 0; rocsparse_scsritilu0_history(handle, alg, &history_niter, history.data(), buffer_size, dbuffer); const bool nrm_residual = (options & rocsparse_itilu0_option_compute_nrm_residual) > 0; for(rocsparse_int i = 0; i < history_niter; ++i) { std::cout << std::setw(12) << i; if(nrm_residual) { std::cout << std::setw(12) << history[history_niter + i]; } std::cout << std::endl; } }

Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**alg**–**[in]**algorithm to use, rocsparse_itilu0_alg**niter**–**[out]**number of performed iterations.**data**–**[out]**norms.**buffer_size**–**[in]**size of the buffer allocated by the user.**buffer**–**[in]**buffer allocated by the user.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`niter`

or`data`

is invalid.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_csritilu0_compute()[#](#rocsparse-csritilu0-compute)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scsritilu0_compute([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, rocsparse_itilu0_alg alg,[rocsparse_int](types.html#_CPPv413rocsparse_int)option,[rocsparse_int](types.html#_CPPv413rocsparse_int)*nmaxiter, float tol,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, const float *csr_val, float *ilu0,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base, size_t buffer_size, void *buffer)[#](#_CPPv428rocsparse_scsritilu0_compute16rocsparse_handle20rocsparse_itilu0_alg13rocsparse_intP13rocsparse_intf13rocsparse_int13rocsparse_intPK13rocsparse_intPK13rocsparse_intPKfPf20rocsparse_index_base6size_tPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcsritilu0_compute([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, rocsparse_itilu0_alg alg,[rocsparse_int](types.html#_CPPv413rocsparse_int)option,[rocsparse_int](types.html#_CPPv413rocsparse_int)*nmaxiter, double tol,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, const double *csr_val, double *ilu0,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base, size_t buffer_size, void *buffer)[#](#_CPPv428rocsparse_dcsritilu0_compute16rocsparse_handle20rocsparse_itilu0_alg13rocsparse_intP13rocsparse_intd13rocsparse_int13rocsparse_intPK13rocsparse_intPK13rocsparse_intPKdPd20rocsparse_index_base6size_tPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccsritilu0_compute([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, rocsparse_itilu0_alg alg,[rocsparse_int](types.html#_CPPv413rocsparse_int)option,[rocsparse_int](types.html#_CPPv413rocsparse_int)*nmaxiter, float tol,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*ilu0,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base, size_t buffer_size, void *buffer)[#](#_CPPv428rocsparse_ccsritilu0_compute16rocsparse_handle20rocsparse_itilu0_alg13rocsparse_intP13rocsparse_intf13rocsparse_int13rocsparse_intPK13rocsparse_intPK13rocsparse_intPK23rocsparse_float_complexP23rocsparse_float_complex20rocsparse_index_base6size_tPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcsritilu0_compute([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, rocsparse_itilu0_alg alg,[rocsparse_int](types.html#_CPPv413rocsparse_int)option,[rocsparse_int](types.html#_CPPv413rocsparse_int)*nmaxiter, double tol,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*ilu0,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base, size_t buffer_size, void *buffer)[#](#_CPPv428rocsparse_zcsritilu0_compute16rocsparse_handle20rocsparse_itilu0_alg13rocsparse_intP13rocsparse_intd13rocsparse_int13rocsparse_intPK13rocsparse_intPK13rocsparse_intPK24rocsparse_double_complexP24rocsparse_double_complex20rocsparse_index_base6size_tPv) Iterative Incomplete LU factorization with 0 fill-ins and no pivoting using CSR storage format.

`rocsparse_csritilu0_compute`

computes iteratively the incomplete LU factorization with 0 fill-ins and no pivoting of a sparse \(m \times m\) CSR matrix \(A\), such that\[ A \approx (L + Id)(D + U) \]We use the following notation for the equations below: diag is the diagonal part, lower is the strict lower triangular part and upper is the strict upper triangular part of a given matrix. Starting with \(L_{0} = lower(\)

`ilu0`

\()\), \(U_{0} = upper(\)`ilu0`

\()\), the method iterates with\[\begin{split} \begin{eqnarray} R_k &=& A - L_{k} U_{k},\\ D_{k+1} &=& diag(R_k),\\ L_{k+1} &=& lower(R_k) D_{k+1}^{-1},\\ U_{k+1} &=& upper(R_k), \end{eqnarray} \end{split}\]if \( 0 \le k \lt \)`nmaxiter`

and if\[ \Vert R_k \Vert_{\infty} \gt \epsilon \Vert A \Vert_{\infty}, \]with \(\epsilon\) =`tol`

. Note that the calculation of \(R_k\) is performed with no fill-in.Computing the above iterative incomplete LU factorization requires three steps to complete. First, the user determines the size of the required temporary storage buffer by calling

[rocsparse_csritilu0_buffer_size](#rocsparse__csritilu0_8h_1aa78b4cd8e523e9ed78e451c18fea12f2). Once this buffer size has been determined, the user allocates the buffer and passes it to[rocsparse_csritilu0_preprocess](#rocsparse__csritilu0_8h_1a9accbedf9d964c6d89d6f02bcf8bbc15). This will perform analysis on the sparsity pattern of the matrix. Finally, the user calls`rocsparse_scsritilu0_compute`

,`rocsparse_dcsritilu0_compute`

,`rocsparse_ccsritilu0_compute`

, or`rocsparse_zcsritilu0_compute`

to perform the actual factorization. The calculation of the buffer size and the analysis of the sparse matrix only need to be performed once for a given sparsity pattern while the factorization can be repeatedly applied to multiple matrices having the same sparsity pattern. Once all calls to[rocsparse_Xcsritilu0_compute()](#rocsparse__csritilu0_8h_1ad12fb46604e835832dd43c158ab12393)are complete, the temporary buffer can be deallocated.`rocsparse_csritilu0`

has a number of options that can be useful for examining the convergence history, easily printing debug information, and for using COO internal format.Option

Notes

rocsparse_itilu0_option_verbose

Print to stdout convergence data as the routine runs. Useful for debugging.

rocsparse_itilu0_option_stopping_criteria

Enable stopping criteria.

rocsparse_itilu0_option_compute_nrm_correction

Compute and store normalized correction. The stored data can then be queried later with

[rocsparse_Xcsritilu0_history](#rocsparse__csritilu0_8h_1a09aa07279c81bfd9a257f15aca0a9cd0).rocsparse_itilu0_option_compute_nrm_residual

Compute and store the normalized residual of the between the approximate solution and the exact solution per iteration. The stored data can then be queried later with

[rocsparse_Xcsritilu0_history](#rocsparse__csritilu0_8h_1a09aa07279c81bfd9a257f15aca0a9cd0).rocsparse_itilu0_option_convergence_history

Enable collecting convergence history data with

[rocsparse_Xcsritilu0_history](#rocsparse__csritilu0_8h_1a09aa07279c81bfd9a257f15aca0a9cd0).rocsparse_itilu0_option_coo_format

Use COO format internally.

**Example**/* ************************************************************************ * Copyright (C) 2025 Advanced Micro Devices, Inc. All rights Reserved. * * Permission is hereby granted, free of charge, to any person obtaining a copy * of this software and associated documentation files (the "Software"), to deal * in the Software without restriction, including without limitation the rights * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell * copies of the Software, and to permit persons to whom the Software is * furnished to do so, subject to the following conditions: * * The above copyright notice and this permission notice shall be included in * all copies or substantial portions of the Software. * * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN * THE SOFTWARE. * * ************************************************************************ */ #include <iostream> #include <vector> #include <rocsparse/rocsparse.h> #define HIP_CHECK(stat) \ { \ if(stat != hipSuccess) \ { \ std::cerr << "Error: hip error " << stat << " in line " << __LINE__ << std::endl; \ return -1; \ } \ } #define ROCSPARSE_CHECK(stat) \ { \ if(stat != rocsparse_status_success) \ { \ std::cerr << "Error: rocsparse error " << stat << " in line " << __LINE__ \ << std::endl; \ return -1; \ } \ } int main() { int m = 3; int n = 3; int nnz = 7; rocsparse_index_base idx_base = rocsparse_index_base_zero; rocsparse_datatype datatype = rocsparse_datatype_f32_r; // 2 1 0 // 1 2 1 // 0 1 2 std::vector<int> hcsr_row_ptr = {0, 2, 5, 7}; std::vector<int> hcsr_col_ind = {0, 1, 0, 1, 2, 1, 2}; std::vector<float> hcsr_val = {2.0f, 1.0f, 1.0f, 2.0f, 1.0f, 1.0f, 2.0f}; int* dcsr_row_ptr; int* dcsr_col_ind; float* dcsr_val; float* dilu0; HIP_CHECK(hipMalloc(&dcsr_row_ptr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc(&dcsr_col_ind, sizeof(int) * nnz)); HIP_CHECK(hipMalloc(&dcsr_val, sizeof(float) * nnz)); HIP_CHECK(hipMalloc(&dilu0, sizeof(float) * nnz)); HIP_CHECK( hipMemcpy(dcsr_row_ptr, hcsr_row_ptr.data(), sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsr_col_ind, hcsr_col_ind.data(), sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsr_val, hcsr_val.data(), sizeof(float) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemset(dilu0, 0, sizeof(float) * nnz)); rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); rocsparse_itilu0_alg alg = rocsparse_itilu0_alg_async_inplace; int nmaxiter = 1000; int option = 0; float tol = 1e-7; size_t buffer_size; ROCSPARSE_CHECK(rocsparse_csritilu0_buffer_size(handle, alg, option, nmaxiter, m, nnz, dcsr_row_ptr, dcsr_col_ind, idx_base, datatype, &buffer_size)); void* dbuffer; HIP_CHECK(hipMalloc(&dbuffer, buffer_size)); ROCSPARSE_CHECK(rocsparse_csritilu0_preprocess(handle, alg, option, nmaxiter, m, nnz, dcsr_row_ptr, dcsr_col_ind, idx_base, datatype, buffer_size, dbuffer)); ROCSPARSE_CHECK(rocsparse_scsritilu0_compute(handle, alg, option, &nmaxiter, tol, m, nnz, dcsr_row_ptr, dcsr_col_ind, dcsr_val, dilu0, idx_base, buffer_size, dbuffer)); std::vector<float> hilu0(nnz); HIP_CHECK(hipMemcpy(hilu0.data(), dilu0, sizeof(float) * nnz, hipMemcpyDeviceToHost)); std::cout << "hilu0" << std::endl; for(size_t i = 0; i < hilu0.size(); i++) { std::cout << hilu0[i] << " "; } std::cout << "" << std::endl; ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); HIP_CHECK(hipFree(dbuffer)); HIP_CHECK(hipFree(dcsr_row_ptr)); HIP_CHECK(hipFree(dcsr_col_ind)); HIP_CHECK(hipFree(dcsr_val)); HIP_CHECK(hipFree(dilu0)); return 0; }


Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**alg**–**[in]**algorithm to use, rocsparse_itilu0_alg**option**–**[in]**combination of enumeration values from rocsparse_itilu0_option.**nmaxiter**–**[inout]**maximum number of iterations on input and number of iterations on output. If the output number of iterations is strictly less than the input maximum number of iterations, then the algorithm converged.**tol**–**[in]**tolerance to use for stopping criteria.**m**–**[in]**number of rows of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csr_col_ind**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**csr_val**–**[inout]**array of`nnz`

elements of the sparse CSR matrix.**ilu0**–**[out]**incomplete factorization.**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**buffer_size**–**[in]**size of the storage buffer allocated by the user.**buffer**–**[in]**storage buffer allocated by the user.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_value**–`alg`

or`base`

is invalid.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`csr_row_ptr`

or`csr_col_ind`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_csritilu0_compute_ex()[#](#rocsparse-csritilu0-compute-ex)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scsritilu0_compute_ex([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, rocsparse_itilu0_alg alg,[rocsparse_int](types.html#_CPPv413rocsparse_int)option,[rocsparse_int](types.html#_CPPv413rocsparse_int)*nmaxiter,[rocsparse_int](types.html#_CPPv413rocsparse_int)nfreeiter, float tol,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, const float *csr_val, float *ilu0,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base, size_t buffer_size, void *buffer)[#](#_CPPv431rocsparse_scsritilu0_compute_ex16rocsparse_handle20rocsparse_itilu0_alg13rocsparse_intP13rocsparse_int13rocsparse_intf13rocsparse_int13rocsparse_intPK13rocsparse_intPK13rocsparse_intPKfPf20rocsparse_index_base6size_tPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcsritilu0_compute_ex([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, rocsparse_itilu0_alg alg,[rocsparse_int](types.html#_CPPv413rocsparse_int)option,[rocsparse_int](types.html#_CPPv413rocsparse_int)*nmaxiter,[rocsparse_int](types.html#_CPPv413rocsparse_int)nfreeiter, double tol,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, const double *csr_val, double *ilu0,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base, size_t buffer_size, void *buffer)[#](#_CPPv431rocsparse_dcsritilu0_compute_ex16rocsparse_handle20rocsparse_itilu0_alg13rocsparse_intP13rocsparse_int13rocsparse_intd13rocsparse_int13rocsparse_intPK13rocsparse_intPK13rocsparse_intPKdPd20rocsparse_index_base6size_tPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccsritilu0_compute_ex([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, rocsparse_itilu0_alg alg,[rocsparse_int](types.html#_CPPv413rocsparse_int)option,[rocsparse_int](types.html#_CPPv413rocsparse_int)*nmaxiter,[rocsparse_int](types.html#_CPPv413rocsparse_int)nfreeiter, float tol,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*ilu0,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base, size_t buffer_size, void *buffer)[#](#_CPPv431rocsparse_ccsritilu0_compute_ex16rocsparse_handle20rocsparse_itilu0_alg13rocsparse_intP13rocsparse_int13rocsparse_intf13rocsparse_int13rocsparse_intPK13rocsparse_intPK13rocsparse_intPK23rocsparse_float_complexP23rocsparse_float_complex20rocsparse_index_base6size_tPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcsritilu0_compute_ex([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, rocsparse_itilu0_alg alg,[rocsparse_int](types.html#_CPPv413rocsparse_int)option,[rocsparse_int](types.html#_CPPv413rocsparse_int)*nmaxiter,[rocsparse_int](types.html#_CPPv413rocsparse_int)nfreeiter, double tol,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*ilu0,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base, size_t buffer_size, void *buffer)[#](#_CPPv431rocsparse_zcsritilu0_compute_ex16rocsparse_handle20rocsparse_itilu0_alg13rocsparse_intP13rocsparse_int13rocsparse_intd13rocsparse_int13rocsparse_intPK13rocsparse_intPK13rocsparse_intPK24rocsparse_double_complexP24rocsparse_double_complex20rocsparse_index_base6size_tPv) Iterative Incomplete LU factorization with 0 fill-ins and no pivoting using CSR storage format.

`rocsparse_csritilu0_compute`

computes iteratively the incomplete LU factorization with 0 fill-ins and no pivoting of a sparse \(m \times m\) CSR matrix \(A\), such that\[ A \approx (L + Id)(D + U) \]We use the following notation for the equations below: diag is the diagonal part, lower is the strict lower triangular part and upper is the strict upper triangular part of a given matrix. Starting with \(L_{0} = lower(\)

`ilu0`

\()\), \(U_{0} = upper(\)`ilu0`

\()\), the method iterates with\[\begin{split} \begin{eqnarray} R_k &=& A - L_{k} U_{k},\\ D_{k+1} &=& diag(R_k),\\ L_{k+1} &=& lower(R_k) D_{k+1}^{-1},\\ U_{k+1} &=& upper(R_k), \end{eqnarray} \end{split}\]if \( 0 \le k \lt \)`nmaxiter`

and if\[ \Vert R_k \Vert_{\infty} \gt \epsilon \Vert A \Vert_{\infty}, \]with \(\epsilon\) =`tol`

. Note that the calculation of \(R_k\) is performed with no fill-in.The parameter

`nfreeiter`

is used to control the frequence of the stopping criteria evaluation, thus potentially improving the performance of the algorithm with less norm calculation. Between each iteration of index \( k \),`nfreeiter`

are performed without stopping criteria evaluation. Thus, if the convergence is obtained with \( k \) This means \( (k + 1)( \)`nfreeiter`

\( ) + k \) iterations.`rocsparse_csritilu0`

requires a user allocated temporary buffer. Its size is returned by[rocsparse_csritilu0_buffer_size()](#rocsparse__csritilu0_8h_1aa78b4cd8e523e9ed78e451c18fea12f2). Furthermore, analysis meta data is required. It can be obtained by rocsparse_csritlu0_preprocess().Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**alg**–**[in]**algorithm to use, rocsparse_itilu0_alg**option**–**[in]**combination of enumeration values from rocsparse_itilu0_option.**nmaxiter**–**[inout]**maximum number of iterations on input and number of iterations on output. If the output number of iterations is strictly less than the input maximum number of iterations, then the algorithm converged.**nfreeiter**–**[inout]**number of free iterations, i.e. the number of iterations the algorithm will perform without stopping criteria evaluations.**tol**–**[in]**tolerance to use for stopping criteria.**m**–**[in]**number of rows of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csr_col_ind**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**csr_val**–**[inout]**array of`nnz`

elements of the sparse CSR matrix.**ilu0**–**[out]**incomplete factorization.**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**buffer_size**–**[in]**size of the storage buffer allocated by the user.**buffer**–**[in]**storage buffer allocated by the user.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_value**–`alg`

or`base`

is invalid.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`csr_row_ptr`

or`csr_col_ind`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_csrilu0_zero_pivot()[#](#rocsparse-csrilu0-zero-pivot)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_csrilu0_zero_pivot([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_int](types.html#_CPPv413rocsparse_int)*position)[#](#_CPPv428rocsparse_csrilu0_zero_pivot16rocsparse_handle18rocsparse_mat_infoP13rocsparse_int) `rocsparse_csrilu0_zero_pivot`

returns[rocsparse_status_zero_pivot](enumerations.html#rocsparse-types_8h_1a578f8c5c1b08f358bf4605b0031006a8a01fe264830c8ce6451ce6888bc8d3e80), if either a structural or numerical zero has been found during[rocsparse_Xcsrilu0()](#rocsparse__csrilu0_8h_1a0534b64d0f29503b7cabf7c8cf3332b4)computation. The first zero pivot \(j\) at \(A_{j,j}\) is stored in`position`

, using same index base as the CSR matrix.`position`

can be in host or device memory. If no zero pivot has been found,`position`

is set to -1 and[rocsparse_status_success](enumerations.html#rocsparse-types_8h_1a578f8c5c1b08f358bf4605b0031006a8a96462a9361cfceb6cf9354e10fdc671b)is returned instead.Note

`rocsparse_csrilu0_zero_pivot`

is a blocking function. It might influence performance negatively.Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**info**–**[in]**structure that holds the information collected during the analysis step.**position**–**[inout]**pointer to zero pivot \(j\), can be in host or device memory.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`info`

or`position`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_zero_pivot**– zero pivot has been found.



## rocsparse_csrilu0_singular_pivot()[#](#rocsparse-csrilu0-singular-pivot)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_csrilu0_singular_pivot([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_int](types.html#_CPPv413rocsparse_int)*position)[#](#_CPPv432rocsparse_csrilu0_singular_pivot16rocsparse_handle18rocsparse_mat_infoP13rocsparse_int)

returns the position of a near numerical zero entry that has been found during[rocsparse_csrilu0_singular_pivot()](#rocsparse__csrilu0_8h_1a7c40b3309bb74ca714c3cc8c66a180b6)[rocsparse_Xcsrilu0()](#rocsparse__csrilu0_8h_1a0534b64d0f29503b7cabf7c8cf3332b4)computation. The first singular pivot \(j\) at \(|A_{j,j}| \leq \text{tolerance}\) is stored in`position`

, using same index base as the CSR matrix.`position`

can be in host or device memory. If no singular pivot has been found,`position`

is set to -1.Note


is a blocking function. It might influence performance negatively.[rocsparse_csrilu0_singular_pivot()](#rocsparse__csrilu0_8h_1a7c40b3309bb74ca714c3cc8c66a180b6)Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**info**–**[in]**structure that holds the information collected during the analysis step.**position**–**[inout]**pointer to singular pivot \(j\), can be in host or device memory.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`info`

or`position`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_csrilu0_set_tolerance()[#](#rocsparse-csrilu0-set-tolerance)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_csrilu0_set_tolerance([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, double tolerance)[#](#_CPPv431rocsparse_csrilu0_set_tolerance16rocsparse_handle18rocsparse_mat_infod)

sets the numerical tolerance for detecting a near numerical zero entry during[rocsparse_csrilu0_set_tolerance()](#rocsparse__csrilu0_8h_1a01eca023be5fd7dceeabe77a6625cfc3)[rocsparse_Xcsrilu0()](#rocsparse__csrilu0_8h_1a0534b64d0f29503b7cabf7c8cf3332b4)computation. The first singular pivot \(j\) at \(|A_{j,j}| \leq \text{tolerance}\).Note


is a blocking function. It might influence performance negatively.[rocsparse_csrilu0_set_tolerance()](#rocsparse__csrilu0_8h_1a01eca023be5fd7dceeabe77a6625cfc3)Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**info**–**[in]**structure that holds the information collected during the analysis step.**tolerance**–**[in]**tolerance value to determine singular pivot \(|A_{j,j}| \leq \text{tolerance}\), where variable tolerance is in host memory.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`info`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_csrilu0_get_tolerance()[#](#rocsparse-csrilu0-get-tolerance)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_csrilu0_get_tolerance([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, double *tolerance)[#](#_CPPv431rocsparse_csrilu0_get_tolerance16rocsparse_handle18rocsparse_mat_infoPd)

returns the numerical tolerance for detecing a near numerical zero entry during[rocsparse_csrilu0_get_tolerance()](#rocsparse__csrilu0_8h_1a39449f9bf0e2896954348e3dd417a70d)[rocsparse_Xcsrilu0()](#rocsparse__csrilu0_8h_1a0534b64d0f29503b7cabf7c8cf3332b4)computation. The first singular pivot \(j\) at \(|A_{j,j}| \leq \text{tolerance}\).Note


is a blocking function. It might influence performance negatively.[rocsparse_csrilu0_get_tolerance()](#rocsparse__csrilu0_8h_1a39449f9bf0e2896954348e3dd417a70d)Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**info**–**[in]**structure that holds the information collected during the analysis step.**tolerance**–**[out]**obtain tolerance value to determine singular pivot \(|A_{j,j}| \leq \text{tolerance}\), where variable tolerance is in host memory.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`info`

or tolerance pointer is invalid..**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_csrilu0_numeric_boost()[#](#rocsparse-csrilu0-numeric-boost)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scsrilu0_numeric_boost([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, int enable_boost, const float *boost_tol, const float *boost_val)[#](#_CPPv432rocsparse_scsrilu0_numeric_boost16rocsparse_handle18rocsparse_mat_infoiPKfPKf)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcsrilu0_numeric_boost([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, int enable_boost, const double *boost_tol, const double *boost_val)[#](#_CPPv432rocsparse_dcsrilu0_numeric_boost16rocsparse_handle18rocsparse_mat_infoiPKdPKd)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccsrilu0_numeric_boost([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, int enable_boost, const float *boost_tol, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*boost_val)[#](#_CPPv432rocsparse_ccsrilu0_numeric_boost16rocsparse_handle18rocsparse_mat_infoiPKfPK23rocsparse_float_complex)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcsrilu0_numeric_boost([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, int enable_boost, const double *boost_tol, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*boost_val)[#](#_CPPv432rocsparse_zcsrilu0_numeric_boost16rocsparse_handle18rocsparse_mat_infoiPKdPK24rocsparse_double_complex) `rocsparse_csrilu0_numeric_boost`

enables the user to replace a numerical value in an incomplete LU factorization.`tol`

is used to determine whether a numerical value is replaced by`boost_val`

, such that \(A_{j,j} = \text{boost_val}\) if \(\text{tol} \ge \left|A_{j,j}\right|\).Note

The boost value is enabled by setting

`enable_boost`

to 1 or disabled by setting`enable_boost`

to 0.Note

`tol`

and`boost_val`

can be in host or device memory.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**info**–**[in]**structure that holds the information collected during the analysis step.**enable_boost**–**[in]**enable/disable numeric boost.**boost_tol**–**[in]**tolerance to determine whether a numerical value is replaced or not.**boost_val**–**[in]**boost value to replace a numerical value.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`info`

,`tol`

or`boost_val`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_csrilu0_buffer_size()[#](#rocsparse-csrilu0-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scsrilu0_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, size_t *buffer_size)[#](#_CPPv430rocsparse_scsrilu0_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcsrilu0_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, size_t *buffer_size)[#](#_CPPv430rocsparse_dcsrilu0_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccsrilu0_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, size_t *buffer_size)[#](#_CPPv430rocsparse_ccsrilu0_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcsrilu0_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info, size_t *buffer_size)[#](#_CPPv430rocsparse_zcsrilu0_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoP6size_t) `rocsparse_csrilu0_buffer_size`

returns the size of the temporary storage buffer that is required by[rocsparse_Xcsrilu0_analysis()](#rocsparse__csrilu0_8h_1a8b0496cb644c23fe65176e70315e431c)and[rocsparse_Xcsrilu0()](#rocsparse__csrilu0_8h_1a0534b64d0f29503b7cabf7c8cf3332b4). The temporary storage buffer must be allocated by the user. The size of the temporary storage buffer is identical to the size returned by[rocsparse_Xcsrsv_buffer_size()](level2.html#rocsparse__csrsv_8h_1ac74b51be59a42a0387648ac79d633b5e)if the matrix sparsity pattern is identical. The user allocated buffer can thus be shared between subsequent calls to those functions.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**descr**–**[in]**descriptor of the sparse CSR matrix.**csr_val**–**[in]**array of`nnz`

elements of the sparse CSR matrix.**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csr_col_ind**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**info**–**[out]**structure that holds the information collected during the analysis step.**buffer_size**–**[out]**number of bytes of the temporary storage buffer required by[rocsparse_Xcsrilu0_analysis()](#rocsparse__csrilu0_8h_1a8b0496cb644c23fe65176e70315e431c)and[rocsparse_Xcsrilu0()](#rocsparse__csrilu0_8h_1a0534b64d0f29503b7cabf7c8cf3332b4).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`csr_val`

,`csr_row_ptr`

,`csr_col_ind`

,`info`

or`buffer_size`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_not_implemented**–[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_csrilu0_analysis()[#](#rocsparse-csrilu0-analysis)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scsrilu0_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_analysis_policy](enumerations.html#_CPPv425rocsparse_analysis_policy)analysis,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)solve, void *temp_buffer)[#](#_CPPv427rocsparse_scsrilu0_analysis16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcsrilu0_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_analysis_policy](enumerations.html#_CPPv425rocsparse_analysis_policy)analysis,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)solve, void *temp_buffer)[#](#_CPPv427rocsparse_dcsrilu0_analysis16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccsrilu0_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_analysis_policy](enumerations.html#_CPPv425rocsparse_analysis_policy)analysis,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)solve, void *temp_buffer)[#](#_CPPv427rocsparse_ccsrilu0_analysis16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcsrilu0_analysis([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_analysis_policy](enumerations.html#_CPPv425rocsparse_analysis_policy)analysis,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)solve, void *temp_buffer)[#](#_CPPv427rocsparse_zcsrilu0_analysis16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv) `rocsparse_csrilu0_analysis`

performs the analysis step for[rocsparse_Xcsrilu0()](#rocsparse__csrilu0_8h_1a0534b64d0f29503b7cabf7c8cf3332b4). It is expected that this function will be executed only once for a given matrix and particular operation type. The analysis meta data can be cleared by[rocsparse_csrilu0_clear()](#rocsparse__csrilu0_8h_1a4bf854d470cb749fa4e696aa49c51044).`rocsparse_csrilu0_analysis`

can share its meta data with[rocsparse_Xcsric0_analysis()](#rocsparse__csric0_8h_1a00bf19a537e0d46b1c55826a9c23e23c),[rocsparse_Xcsrsv_analysis()](level2.html#rocsparse__csrsv_8h_1af710dcbc752ca8203389907bcbe74273), and[rocsparse_Xcsrsm_analysis()](level3.html#rocsparse__csrsm_8h_1ac8e943e992641859efdfea49a267133b). Selecting[rocsparse_analysis_policy_reuse](enumerations.html#rocsparse-types_8h_1a43b20aa4bb19623a91b5952422fbe35ca658466413f4005c0c103d20d5e352078)policy can greatly improve computation performance of meta data. However, the user needs to make sure that the sparsity pattern remains unchanged. If this cannot be assured,[rocsparse_analysis_policy_force](enumerations.html#rocsparse-types_8h_1a43b20aa4bb19623a91b5952422fbe35cac66b70c4f519ddd03dcbe0f3a973401a)has to be used.Note

If the matrix sparsity pattern changes, the gathered information will become invalid.

Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**descr**–**[in]**descriptor of the sparse CSR matrix.**csr_val**–**[in]**array of`nnz`

elements of the sparse CSR matrix.**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csr_col_ind**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**info**–**[out]**structure that holds the information collected during the analysis step.**analysis**–**[in]**[rocsparse_analysis_policy_reuse](enumerations.html#rocsparse-types_8h_1a43b20aa4bb19623a91b5952422fbe35ca658466413f4005c0c103d20d5e352078)or[rocsparse_analysis_policy_force](enumerations.html#rocsparse-types_8h_1a43b20aa4bb19623a91b5952422fbe35cac66b70c4f519ddd03dcbe0f3a973401a).**solve**–**[in]**[rocsparse_solve_policy_auto](enumerations.html#rocsparse-types_8h_1a5a3e261123e81a9e8b267c6109e26957a9c6bdf97e192d429ca536d5ab98ea866).**temp_buffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`csr_val`

,`csr_row_ptr`

,`csr_col_ind`

,`info`

or`temp_buffer`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_not_implemented**–[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_csrilu0()[#](#rocsparse-csrilu0)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scsrilu0([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, float *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv418rocsparse_scsrilu016rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPfPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_info22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcsrilu0([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, double *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv418rocsparse_dcsrilu016rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPdPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_info22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccsrilu0([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv418rocsparse_ccsrilu016rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrP23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_info22rocsparse_solve_policyPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcsrilu0([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info,[rocsparse_solve_policy](enumerations.html#_CPPv422rocsparse_solve_policy)policy, void *temp_buffer)[#](#_CPPv418rocsparse_zcsrilu016rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrP24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_info22rocsparse_solve_policyPv) Incomplete LU factorization with 0 fill-ins and no pivoting using CSR storage format.

`rocsparse_csrilu0`

computes the incomplete LU factorization with 0 fill-ins and no pivoting of a sparse \(m \times m\) CSR matrix \(A\), such that\[ A \approx LU \]where the lower triangular matrix \(L\) and the upper triangular matrix \(U\) are computed using:\[\begin{split} \begin{array}{ll} L_{ij} = \frac{1}{U_{jj}}(A_{ij} - \sum_{k=0}^{j-1}L_{ik} \times U_{kj}), & \text{if i > j} \\ U_{ij} = (A_{ij} - \sum_{k=0}^{j-1}L_{ik} \times U_{kj}), & \text{if i <= j} \end{array} \end{split}\]for each entry found in the CSR matrix \(A\).Computing the above incomplete \(LU\) factorization requires three steps to complete. First, the user determines the size of the required temporary storage buffer by calling

[rocsparse_Xcsrilu0_buffer_size()](#rocsparse__csrilu0_8h_1a75eebaa5a02b9f1f9a05ff440ceef387). Once this buffer size has been determined, the user allocates the buffer and passes it to[rocsparse_Xcsrilu0_analysis()](#rocsparse__csrilu0_8h_1a8b0496cb644c23fe65176e70315e431c). This will perform analysis on the sparsity pattern of the matrix. Finally, the user calls`rocsparse_scsrilu0`

,`rocsparse_dcsrilu0`

,`rocsparse_ccsrilu0`

, or`rocsparse_zcsrilu0`

to perform the actual factorization. The calculation of the buffer size and the analysis of the sparse matrix only need to be performed once for a given sparsity pattern while the factorization can be repeatedly applied to multiple matrices having the same sparsity pattern. Once all calls to[rocsparse_Xcsrilu0()](#rocsparse__csrilu0_8h_1a0534b64d0f29503b7cabf7c8cf3332b4)are complete, the temporary buffer can be deallocated.When computing the \(LU\) factorization, it is possible that \(U_{jj} == 0\) which would result in a division by zero. This could occur from either \(A_{jj}\) not existing in the sparse CSR matrix (referred to as a structural zero) or because \(A_{ij} - \sum_{k=0}^{j-1}L_{ik} \times U_{kj} == 0\) (referred to as a numerical zero). For example, running the \(LU\) factorization on the following matrix:

\[\begin{split} \begin{bmatrix} 2 & 1 & 0 \\ 1 & 2 & 1 \\ 0 & 1 & 2 \end{bmatrix} \end{split}\]results in a successful \(LU\) factorization, however running with the matrix:\[\begin{split} \begin{bmatrix} 2 & 1 & 0 \\ 1 & 1/2 & 1 \\ 0 & 1 & 2 \end{bmatrix} \end{split}\]results in a numerical zero because:\[\begin{split} \begin{array}{ll} U_{00} &= 2 \\ U_{01} &= 1 \\ L_{10} &= \frac{1}{2} \\ U_{11} &= \frac{1}{2} - \frac{1}{2} &= 0 \end{array} \end{split}\]The user can detect the presence of a structural zero by calling[rocsparse_csrilu0_zero_pivot()](#rocsparse__csrilu0_8h_1ae4ed19a637de57c82ba06d084208fe74)after[rocsparse_Xcsrilu0_analysis()](#rocsparse__csrilu0_8h_1a8b0496cb644c23fe65176e70315e431c)and/or the presence of a structural or numerical zero by calling[rocsparse_csrilu0_zero_pivot()](#rocsparse__csrilu0_8h_1ae4ed19a637de57c82ba06d084208fe74)after[rocsparse_Xcsric0()](#rocsparse__csrilu0_8h_1a0534b64d0f29503b7cabf7c8cf3332b4). In both cases,[rocsparse_csrilu0_zero_pivot()](#rocsparse__csrilu0_8h_1ae4ed19a637de57c82ba06d084208fe74)will report the first zero pivot (either numerical or structural) found. See example below. The user can also set the diagonal type to be \(1\) using[rocsparse_set_mat_diag_type()](auxiliary.html#rocsparse-auxiliary_8h_1a61f894d80e4da74c7e8cd43f61f9215c)which will interpret the matrix \(A\) as having ones on its diagonal (even if no nonzero exists in the sparsity pattern).`rocsparse_csrilu0`

computes the \(LU\) factorization inplace meaning that the values array`csr_val`

of the \(A\) matrix is overwritten with the \(L\) matrix stored in the strictly lower triangular part of \(A\) and the \(U\) matrix stored in the upper part of \(A\):\[\begin{split} \begin{align} \begin{bmatrix} a_{00} & a_{01} & a_{02} \\ a_{10} & a_{11} & a_{12} \\ a_{20} & a_{21} & a_{22} \end{bmatrix} \rightarrow \begin{bmatrix} u_{00} & u_{01} & u_{02} \\ l_{10} & u_{11} & u_{12} \\ l_{20} & l_{21} & u_{22} \end{bmatrix} \end{align} \end{split}\]The row pointer array`csr_row_ptr`

and the column indices array`csr_col_ind`

remain the same for \(A\) and \(LU\) as the incomplete factorization does not generate new nonzeros in \(LU\) which do not already exist in \(A\).The performance of computing \(LU\) factorization with rocSPARSE greatly depends on the sparisty pattern the the matrix \(A\) as this is what determines the amount of parallelism available.

**Example**Consider the sparse \(m \times m\) matrix \(A\), stored in CSR storage format. The following example computes the incomplete LU factorization \(M \approx LU\) and solves the preconditioned system \(My = x\).

int main() { // 2 1 0 0 // A = 1 2 1 0 // 0 1 2 1 // 0 0 1 2 int m = 4; int n = 4; double alpha = 1.0; std::vector<int> hcsr_row_ptr = {0, 2, 5, 8, 10}; std::vector<int> hcsr_col_ind = {0, 1, 0, 1, 2, 1, 2, 3, 2, 3}; std::vector<double> hcsr_val = {2.0, 1.0, 1.0, 2.0, 1.0, 1.0, 2.0, 1.0, 1.0, 2.0}; int nnz = hcsr_row_ptr[m] - hcsr_row_ptr[0]; std::vector<double> hx(m, 1.0); int* dcsr_row_ptr; int* dcsr_col_ind; double* dcsr_val; double* dx; double* dy; double* dz; HIP_CHECK(hipMalloc(&dcsr_row_ptr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc(&dcsr_col_ind, sizeof(int) * nnz)); HIP_CHECK(hipMalloc(&dcsr_val, sizeof(double) * nnz)); HIP_CHECK(hipMalloc(&dx, sizeof(double) * m)); HIP_CHECK(hipMalloc(&dy, sizeof(double) * m)); HIP_CHECK(hipMalloc(&dz, sizeof(double) * m)); HIP_CHECK( hipMemcpy(dcsr_row_ptr, hcsr_row_ptr.data(), sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsr_col_ind, hcsr_col_ind.data(), sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsr_val, hcsr_val.data(), sizeof(double) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dx, hx.data(), sizeof(double) * m, hipMemcpyHostToDevice)); // Create rocSPARSE handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Create matrix descriptor for M rocsparse_mat_descr descr_M; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr_M)); // Create matrix descriptor for L rocsparse_mat_descr descr_L; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr_L)); ROCSPARSE_CHECK(rocsparse_set_mat_fill_mode(descr_L, rocsparse_fill_mode_lower)); ROCSPARSE_CHECK(rocsparse_set_mat_diag_type(descr_L, rocsparse_diag_type_unit)); // Create matrix descriptor for U rocsparse_mat_descr descr_U; ROCSPARSE_CHECK(rocsparse_create_mat_descr(&descr_U)); ROCSPARSE_CHECK(rocsparse_set_mat_fill_mode(descr_U, rocsparse_fill_mode_upper)); ROCSPARSE_CHECK(rocsparse_set_mat_diag_type(descr_U, rocsparse_diag_type_non_unit)); // Create matrix info structure rocsparse_mat_info info; ROCSPARSE_CHECK(rocsparse_create_mat_info(&info)); // Obtain required buffer size size_t buffer_size_M; size_t buffer_size_L; size_t buffer_size_U; ROCSPARSE_CHECK(rocsparse_dcsrilu0_buffer_size( handle, m, nnz, descr_M, dcsr_val, dcsr_row_ptr, dcsr_col_ind, info, &buffer_size_M)); ROCSPARSE_CHECK(rocsparse_dcsrsv_buffer_size(handle, rocsparse_operation_none, m, nnz, descr_L, dcsr_val, dcsr_row_ptr, dcsr_col_ind, info, &buffer_size_L)); ROCSPARSE_CHECK(rocsparse_dcsrsv_buffer_size(handle, rocsparse_operation_none, m, nnz, descr_U, dcsr_val, dcsr_row_ptr, dcsr_col_ind, info, &buffer_size_U)); size_t buffer_size = max(buffer_size_M, max(buffer_size_L, buffer_size_U)); // Allocate temporary buffer void* temp_buffer; HIP_CHECK(hipMalloc(&temp_buffer, buffer_size)); // Perform analysis steps, using rocsparse_analysis_policy_reuse to improve // computation performance ROCSPARSE_CHECK(rocsparse_dcsrilu0_analysis(handle, m, nnz, descr_M, dcsr_val, dcsr_row_ptr, dcsr_col_ind, info, rocsparse_analysis_policy_reuse, rocsparse_solve_policy_auto, temp_buffer)); ROCSPARSE_CHECK(rocsparse_dcsrsv_analysis(handle, rocsparse_operation_none, m, nnz, descr_L, dcsr_val, dcsr_row_ptr, dcsr_col_ind, info, rocsparse_analysis_policy_reuse, rocsparse_solve_policy_auto, temp_buffer)); ROCSPARSE_CHECK(rocsparse_dcsrsv_analysis(handle, rocsparse_operation_none, m, nnz, descr_U, dcsr_val, dcsr_row_ptr, dcsr_col_ind, info, rocsparse_analysis_policy_reuse, rocsparse_solve_policy_auto, temp_buffer)); // Check for zero pivot rocsparse_int position; if(rocsparse_status_zero_pivot == rocsparse_csrilu0_zero_pivot(handle, info, &position)) { printf("A has structural zero at A(%d,%d)\n", position, position); } // Compute incomplete LU factorization ROCSPARSE_CHECK(rocsparse_dcsrilu0(handle, m, nnz, descr_M, dcsr_val, dcsr_row_ptr, dcsr_col_ind, info, rocsparse_solve_policy_auto, temp_buffer)); // Check for zero pivot if(rocsparse_status_zero_pivot == rocsparse_csrilu0_zero_pivot(handle, info, &position)) { printf("U has structural and/or numerical zero at U(%d,%d)\n", position, position); } // Copy incomplete LU factorization to host HIP_CHECK( hipMemcpy(hcsr_row_ptr.data(), dcsr_row_ptr, sizeof(int) * (m + 1), hipMemcpyDeviceToHost)); HIP_CHECK( hipMemcpy(hcsr_col_ind.data(), dcsr_col_ind, sizeof(int) * nnz, hipMemcpyDeviceToHost)); HIP_CHECK(hipMemcpy(hcsr_val.data(), dcsr_val, sizeof(double) * nnz, hipMemcpyDeviceToHost)); std::cout << "LU" << std::endl; for(int i = 0; i < m; i++) { int start = hcsr_row_ptr[i]; int end = hcsr_row_ptr[i + 1]; std::vector<double> temp(n, 0.0); for(int j = start; j < end; j++) { temp[hcsr_col_ind[j]] = hcsr_val[j]; } for(int j = 0; j < n; j++) { std::cout << temp[j] << " "; } std::cout << "" << std::endl; } std::cout << "" << std::endl; // Solve Lz = x ROCSPARSE_CHECK(rocsparse_dcsrsv_solve(handle, rocsparse_operation_none, m, nnz, &alpha, descr_L, dcsr_val, dcsr_row_ptr, dcsr_col_ind, info, dx, dz, rocsparse_solve_policy_auto, temp_buffer)); // Solve Uy = z ROCSPARSE_CHECK(rocsparse_dcsrsv_solve(handle, rocsparse_operation_none, m, nnz, &alpha, descr_U, dcsr_val, dcsr_row_ptr, dcsr_col_ind, info, dz, dy, rocsparse_solve_policy_auto, temp_buffer)); std::vector<double> hy(m); HIP_CHECK(hipMemcpy(hy.data(), dy, sizeof(double) * m, hipMemcpyDeviceToHost)); std::cout << "hy" << std::endl; for(size_t i = 0; i < hy.size(); i++) { std::cout << hy[i] << " "; } std::cout << "" << std::endl; // Clean up ROCSPARSE_CHECK(rocsparse_destroy_mat_info(info)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr_M)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr_L)); ROCSPARSE_CHECK(rocsparse_destroy_mat_descr(descr_U)); ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); HIP_CHECK(hipFree(dcsr_row_ptr)); HIP_CHECK(hipFree(dcsr_col_ind)); HIP_CHECK(hipFree(dcsr_val)); HIP_CHECK(hipFree(dx)); HIP_CHECK(hipFree(dy)); HIP_CHECK(hipFree(dz)); HIP_CHECK(hipFree(temp_buffer)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**descr**–**[in]**descriptor of the sparse CSR matrix.**csr_val**–**[inout]**array of`nnz`

elements of the sparse CSR matrix.**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csr_col_ind**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**info**–**[in]**structure that holds the information collected during the analysis step.**policy**–**[in]**[rocsparse_solve_policy_auto](enumerations.html#rocsparse-types_8h_1a5a3e261123e81a9e8b267c6109e26957a9c6bdf97e192d429ca536d5ab98ea866).**temp_buffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`csr_val`

,`csr_row_ptr`

or`csr_col_ind`

pointer is invalid.**rocsparse_status_arch_mismatch**– the device is not supported.**rocsparse_status_internal_error**– an internal error occurred.**rocsparse_status_not_implemented**–[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)!=[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03).



## rocsparse_csrilu0_clear()[#](#rocsparse-csrilu0-clear)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_csrilu0_clear([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info)[#](#_CPPv423rocsparse_csrilu0_clear16rocsparse_handle18rocsparse_mat_info) `rocsparse_csrilu0_clear`

deallocates all memory that was allocated by[rocsparse_Xcsrilu0_analysis()](#rocsparse__csrilu0_8h_1a8b0496cb644c23fe65176e70315e431c). This is especially useful, if memory is an issue and the analysis data is not required for further computation.Note

Calling

`rocsparse_csrilu0_clear`

is optional. All allocated resources will be cleared, when the opaque[rocsparse_mat_info](types.html#rocsparse-types_8h_1a3347be72f6e4f3c55318c32b46dcaa92)struct is destroyed using[rocsparse_destroy_mat_info()](auxiliary.html#rocsparse-auxiliary_8h_1a9c143f65076a10ebafcffc633ad5d87b).Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**info**–**[inout]**structure that holds the information collected during the analysis step.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_pointer**–`info`

pointer is invalid.**rocsparse_status_memory_error**– the buffer holding the meta data could not be deallocated.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_gtsv_buffer_size()[#](#rocsparse-gtsv-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sgtsv_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const float *dl, const float *d, const float *du, const float *B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb, size_t *buffer_size)[#](#_CPPv427rocsparse_sgtsv_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_intPKfPKfPKfPKf13rocsparse_intP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dgtsv_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const double *dl, const double *d, const double *du, const double *B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb, size_t *buffer_size)[#](#_CPPv427rocsparse_dgtsv_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_intPKdPKdPKdPKd13rocsparse_intP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cgtsv_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*dl, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*d, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*du, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb, size_t *buffer_size)[#](#_CPPv427rocsparse_cgtsv_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_intPK23rocsparse_float_complexPK23rocsparse_float_complexPK23rocsparse_float_complexPK23rocsparse_float_complex13rocsparse_intP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zgtsv_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*dl, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*d, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*du, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb, size_t *buffer_size)[#](#_CPPv427rocsparse_zgtsv_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_intPK24rocsparse_double_complexPK24rocsparse_double_complexPK24rocsparse_double_complexPK24rocsparse_double_complex13rocsparse_intP6size_t) `rocsparse_gtsv_buffer_size`

returns the size of the temporary storage buffer that is required by[rocsparse_Xgtsv()](#rocsparse__gtsv_8h_1a7343a69337de814ebf667280d8f8403c). The temporary storage buffer must be allocated by the user.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**size of the tri-diagonal linear system (must be >= 2).**n**–**[in]**number of columns in the dense matrix B.**dl**–**[in]**lower diagonal of tri-diagonal system. First entry must be zero.**d**–**[in]**main diagonal of tri-diagonal system.**du**–**[in]**upper diagonal of tri-diagonal system. Last entry must be zero.**B**–**[in]**Dense matrix of size (`ldb`

,`n`

).**ldb**–**[in]**Leading dimension of B. Must satisfy`ldb`

>= max(1, m).**buffer_size**–**[out]**number of bytes of the temporary storage buffer required by[rocsparse_sgtsv()](#rocsparse__gtsv_8h_1a7343a69337de814ebf667280d8f8403c),[rocsparse_dgtsv()](#rocsparse__gtsv_8h_1ad17eb7e96971b5ab6f162ab120be18f0),[rocsparse_cgtsv()](#rocsparse__gtsv_8h_1abdd7a15c54f05458af623c765332c526)and[rocsparse_zgtsv()](#rocsparse__gtsv_8h_1a1f805db7a1e49c7d5d419c16c1625428).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`n`

or`ldb`

is invalid.**rocsparse_status_invalid_pointer**–`dl`

,`d`

,`du`

,`B`

or`buffer_size`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_gtsv()[#](#rocsparse-gtsv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sgtsv([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const float *dl, const float *d, const float *du, float *B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb, void *temp_buffer)[#](#_CPPv415rocsparse_sgtsv16rocsparse_handle13rocsparse_int13rocsparse_intPKfPKfPKfPf13rocsparse_intPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dgtsv([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const double *dl, const double *d, const double *du, double *B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb, void *temp_buffer)[#](#_CPPv415rocsparse_dgtsv16rocsparse_handle13rocsparse_int13rocsparse_intPKdPKdPKdPd13rocsparse_intPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cgtsv([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*dl, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*d, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*du,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb, void *temp_buffer)[#](#_CPPv415rocsparse_cgtsv16rocsparse_handle13rocsparse_int13rocsparse_intPK23rocsparse_float_complexPK23rocsparse_float_complexPK23rocsparse_float_complexP23rocsparse_float_complex13rocsparse_intPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zgtsv([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*dl, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*d, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*du,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb, void *temp_buffer)[#](#_CPPv415rocsparse_zgtsv16rocsparse_handle13rocsparse_int13rocsparse_intPK24rocsparse_double_complexPK24rocsparse_double_complexPK24rocsparse_double_complexP24rocsparse_double_complex13rocsparse_intPv) Tridiagonal solver with pivoting.

`rocsparse_gtsv`

solves a tridiagonal system for multiple right hand sides using pivoting\[ T*B = B \]where \(T\) is a sparse tridiagonal matrix and \(B\) is a dense \(ldb \times n\) matrix storing the right-hand side vectors in column order. The tridiagonal matrix \(T\) is defined by three vectors:`dl`

for the lower diagonal,`d`

for the main diagonal and`du`

for the upper diagonal.Solving the tridiagonal system involves two steps. First, the user calls

[rocsparse_Xgtsv_buffer_size()](#rocsparse__gtsv_8h_1a081ff445184be145495b8003abe9a1b3)in order to determine the size of the required temporary storage buffer. Once determined, the user allocates this buffer and passes it to[rocsparse_Xgtsv()](#rocsparse__gtsv_8h_1a7343a69337de814ebf667280d8f8403c)to perform the actual solve. The \(B\) dense matrix, which initially stores the`n`

right-hand side vectors, is overwritten with the`n`

solution vectors after the call to[rocsparse_Xgtsv()](#rocsparse__gtsv_8h_1a7343a69337de814ebf667280d8f8403c).**Example**int main() { // Size of square tridiagonal matrix rocsparse_int m = 5; // Number of columns in right-hand side (column ordered) matrix rocsparse_int n = 3; // Leading dimension of right-hand side (column ordered) matrix rocsparse_int ldb = m; // Host tri-diagonal matrix // 2 3 0 0 0 // 2 4 2 0 0 // 0 1 1 1 0 // 0 0 1 3 1 // 0 0 0 1 4 std::vector<float> hdl = {0.0f, 2.0f, 1.0f, 1.0f, 1.0f}; std::vector<float> hd = {2.0f, 4.0f, 1.0f, 3.0f, 4.0f}; std::vector<float> hdu = {3.0f, 2.0f, 1.0f, 1.0f, 0.0f}; // Host right-hand side column vectors std::vector<float> hB(ldb * n, 2.0f); float* ddl; float* dd; float* ddu; float* dB; HIP_CHECK(hipMalloc(&ddl, sizeof(float) * m)); HIP_CHECK(hipMalloc(&dd, sizeof(float) * m)); HIP_CHECK(hipMalloc(&ddu, sizeof(float) * m)); HIP_CHECK(hipMalloc(&dB, sizeof(float) * ldb * n)); HIP_CHECK(hipMemcpy(ddl, hdl.data(), sizeof(float) * m, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dd, hd.data(), sizeof(float) * m, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(ddu, hdu.data(), sizeof(float) * m, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dB, hB.data(), sizeof(float) * ldb * n, hipMemcpyHostToDevice)); // rocSPARSE handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Obtain required buffer size size_t buffer_size; ROCSPARSE_CHECK(rocsparse_sgtsv_buffer_size(handle, m, n, ddl, dd, ddu, dB, ldb, &buffer_size)); void* dbuffer; HIP_CHECK(hipMalloc(&dbuffer, buffer_size)); ROCSPARSE_CHECK(rocsparse_sgtsv(handle, m, n, ddl, dd, ddu, dB, ldb, dbuffer)); // Copy right-hand side to host HIP_CHECK(hipMemcpy(hB.data(), dB, sizeof(float) * ldb * n, hipMemcpyDeviceToHost)); std::cout << "hB" << std::endl; for(size_t i = 0; i < hB.size(); i++) { std::cout << hB[i] << " "; } std::cout << "" << std::endl; // Clear rocSPARSE ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); // Clear device memory HIP_CHECK(hipFree(ddl)); HIP_CHECK(hipFree(dd)); HIP_CHECK(hipFree(ddu)); HIP_CHECK(hipFree(dB)); HIP_CHECK(hipFree(dbuffer)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**size of the tri-diagonal linear system (must be >= 2).**n**–**[in]**number of columns in the dense matrix B.**dl**–**[in]**lower diagonal of tri-diagonal system. First entry must be zero.**d**–**[in]**main diagonal of tri-diagonal system.**du**–**[in]**upper diagonal of tri-diagonal system. Last entry must be zero.**B**–**[inout]**Dense matrix of size (`ldb`

,`n`

).**ldb**–**[in]**Leading dimension of B. Must satisfy`ldb`

>= max(1, m).**temp_buffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`n`

or`ldb`

is invalid.**rocsparse_status_invalid_pointer**–`dl`

,`d`

,`du`

,`B`

or`temp_buffer`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_gtsv_no_pivot_buffer_size()[#](#rocsparse-gtsv-no-pivot-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sgtsv_no_pivot_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const float *dl, const float *d, const float *du, const float *B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb, size_t *buffer_size)[#](#_CPPv436rocsparse_sgtsv_no_pivot_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_intPKfPKfPKfPKf13rocsparse_intP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dgtsv_no_pivot_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const double *dl, const double *d, const double *du, const double *B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb, size_t *buffer_size)[#](#_CPPv436rocsparse_dgtsv_no_pivot_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_intPKdPKdPKdPKd13rocsparse_intP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cgtsv_no_pivot_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*dl, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*d, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*du, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb, size_t *buffer_size)[#](#_CPPv436rocsparse_cgtsv_no_pivot_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_intPK23rocsparse_float_complexPK23rocsparse_float_complexPK23rocsparse_float_complexPK23rocsparse_float_complex13rocsparse_intP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zgtsv_no_pivot_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*dl, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*d, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*du, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb, size_t *buffer_size)[#](#_CPPv436rocsparse_zgtsv_no_pivot_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_intPK24rocsparse_double_complexPK24rocsparse_double_complexPK24rocsparse_double_complexPK24rocsparse_double_complex13rocsparse_intP6size_t) `rocsparse_gtsv_no_pivot_buffer_size`

returns the size of the temporary storage buffer that is required by[rocsparse_Xgtsv_no_pivot()](#rocsparse__gtsv_8h_1a00fb11eee2eec8c754c326e0dbc38c3c). The temporary storage buffer must be allocated by the user.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**size of the tri-diagonal linear system (must be >= 2).**n**–**[in]**number of columns in the dense matrix B.**dl**–**[in]**lower diagonal of tri-diagonal system. First entry must be zero.**d**–**[in]**main diagonal of tri-diagonal system.**du**–**[in]**upper diagonal of tri-diagonal system. Last entry must be zero.**B**–**[in]**Dense matrix of size (`ldb`

,`n`

).**ldb**–**[in]**Leading dimension of B. Must satisfy`ldb`

>= max(1, m).**buffer_size**–**[out]**number of bytes of the temporary storage buffer required by[rocsparse_sgtsv_no_pivot()](#rocsparse__gtsv_8h_1a00fb11eee2eec8c754c326e0dbc38c3c),[rocsparse_dgtsv_no_pivot()](#rocsparse__gtsv_8h_1a7d59f579b71db5da23ede0976d16ad26),[rocsparse_cgtsv_no_pivot()](#rocsparse__gtsv_8h_1a241a88cb4387eb16d51cfcc4e3d58f85)and[rocsparse_zgtsv_no_pivot()](#rocsparse__gtsv_8h_1a036583c6a9ccc2d16b87daa691b799ff).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`n`

or`ldb`

is invalid.**rocsparse_status_invalid_pointer**–`dl`

,`d`

,`du`

,`B`

or`buffer_size`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_gtsv_no_pivot()[#](#rocsparse-gtsv-no-pivot)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sgtsv_no_pivot([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const float *dl, const float *d, const float *du, float *B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb, void *temp_buffer)[#](#_CPPv424rocsparse_sgtsv_no_pivot16rocsparse_handle13rocsparse_int13rocsparse_intPKfPKfPKfPf13rocsparse_intPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dgtsv_no_pivot([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const double *dl, const double *d, const double *du, double *B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb, void *temp_buffer)[#](#_CPPv424rocsparse_dgtsv_no_pivot16rocsparse_handle13rocsparse_int13rocsparse_intPKdPKdPKdPd13rocsparse_intPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cgtsv_no_pivot([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*dl, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*d, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*du,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb, void *temp_buffer)[#](#_CPPv424rocsparse_cgtsv_no_pivot16rocsparse_handle13rocsparse_int13rocsparse_intPK23rocsparse_float_complexPK23rocsparse_float_complexPK23rocsparse_float_complexP23rocsparse_float_complex13rocsparse_intPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zgtsv_no_pivot([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)n, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*dl, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*d, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*du,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*B,[rocsparse_int](types.html#_CPPv413rocsparse_int)ldb, void *temp_buffer)[#](#_CPPv424rocsparse_zgtsv_no_pivot16rocsparse_handle13rocsparse_int13rocsparse_intPK24rocsparse_double_complexPK24rocsparse_double_complexPK24rocsparse_double_complexP24rocsparse_double_complex13rocsparse_intPv) Tridiagonal solver (no pivoting)

`rocsparse_gtsv_no_pivot`

solves a tridiagonal linear system for multiple right-hand sides without pivoting\[ T*B = B \]where \(T\) is a sparse tridiagonal matrix and \(B\) is a dense \(ldb \times n\) matrix storing the right-hand side vectors in column order. The tridiagonal matrix \(T\) is defined by three vectors:`dl`

for the lower diagonal,`d`

for the main diagonal and`du`

for the upper diagonal.Solving the tridiagonal system with multiple right-hand sides without pivoting involves two steps. First, the user calls

[rocsparse_Xgtsv_no_pivot_buffer_size()](#rocsparse__gtsv_8h_1a68c97476e843737c5e41494647d779ab)in order to determine the size of the required temporary storage buffer. Once determined, the user allocates this buffer and passes it to[rocsparse_Xgtsv_no_pivot()](#rocsparse__gtsv_8h_1a00fb11eee2eec8c754c326e0dbc38c3c)to perform the actual solve. The \(B\) dense matrix, which initially stores the`n`

right-hand side vectors, is overwritten with the`n`

solution vectors after the call to[rocsparse_Xgtsv_no_pivot()](#rocsparse__gtsv_8h_1a00fb11eee2eec8c754c326e0dbc38c3c).**Example**int main() { // Size of square tridiagonal matrix rocsparse_int m = 5; // Number of columns in right-hand side (column ordered) matrix rocsparse_int n = 3; // Leading dimension of right-hand side (column ordered) matrix rocsparse_int ldb = m; // Host tri-diagonal matrix // 2 -1 0 0 0 // -1 2 -1 0 0 // 0 -1 2 -1 0 // 0 0 -1 2 -1 // 0 0 0 -1 2 std::vector<float> hdl = {0.0f, -1.0f, -1.0f, -1.0f, -1.0f}; std::vector<float> hd = {2.0f, 2.0f, 2.0f, 2.0f, 2.0f}; std::vector<float> hdu = {-1.0f, -1.0f, -1.0f, -1.0f, 0.0f}; // Host right-hand side column vectors std::vector<float> hB(ldb * n, 1.0f); float* ddl; float* dd; float* ddu; float* dB; HIP_CHECK(hipMalloc(&ddl, sizeof(float) * m)); HIP_CHECK(hipMalloc(&dd, sizeof(float) * m)); HIP_CHECK(hipMalloc(&ddu, sizeof(float) * m)); HIP_CHECK(hipMalloc(&dB, sizeof(float) * ldb * n)); HIP_CHECK(hipMemcpy(ddl, hdl.data(), sizeof(float) * m, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dd, hd.data(), sizeof(float) * m, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(ddu, hdu.data(), sizeof(float) * m, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dB, hB.data(), sizeof(float) * ldb * n, hipMemcpyHostToDevice)); // rocSPARSE handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Obtain required buffer size size_t buffer_size; ROCSPARSE_CHECK( rocsparse_sgtsv_no_pivot_buffer_size(handle, m, n, ddl, dd, ddu, dB, ldb, &buffer_size)); void* dbuffer; HIP_CHECK(hipMalloc(&dbuffer, buffer_size)); ROCSPARSE_CHECK(rocsparse_sgtsv_no_pivot(handle, m, n, ddl, dd, ddu, dB, ldb, dbuffer)); // Copy right-hand side to host HIP_CHECK(hipMemcpy(hB.data(), dB, sizeof(float) * ldb * n, hipMemcpyDeviceToHost)); std::cout << "hB" << std::endl; for(size_t i = 0; i < hB.size(); i++) { std::cout << hB[i] << " "; } std::cout << "" << std::endl; // Clear rocSPARSE ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); // Clear device memory HIP_CHECK(hipFree(ddl)); HIP_CHECK(hipFree(dd)); HIP_CHECK(hipFree(ddu)); HIP_CHECK(hipFree(dB)); HIP_CHECK(hipFree(dbuffer)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**size of the tri-diagonal linear system (must be >= 2).**n**–**[in]**number of columns in the dense matrix B.**dl**–**[in]**lower diagonal of tri-diagonal system. First entry must be zero.**d**–**[in]**main diagonal of tri-diagonal system.**du**–**[in]**upper diagonal of tri-diagonal system. Last entry must be zero.**B**–**[inout]**Dense matrix of size (`ldb`

,`n`

).**ldb**–**[in]**Leading dimension of B. Must satisfy`ldb`

>= max(1, m).**temp_buffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`n`

or`ldb`

is invalid.**rocsparse_status_invalid_pointer**–`dl`

,`d`

,`du`

,`B`

or`temp_buffer`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_gtsv_no_pivot_strided_batch_buffer_size()[#](#rocsparse-gtsv-no-pivot-strided-batch-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sgtsv_no_pivot_strided_batch_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m, const float *dl, const float *d, const float *du, const float *x,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_count,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_stride, size_t *buffer_size)[#](#_CPPv450rocsparse_sgtsv_no_pivot_strided_batch_buffer_size16rocsparse_handle13rocsparse_intPKfPKfPKfPKf13rocsparse_int13rocsparse_intP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dgtsv_no_pivot_strided_batch_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m, const double *dl, const double *d, const double *du, const double *x,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_count,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_stride, size_t *buffer_size)[#](#_CPPv450rocsparse_dgtsv_no_pivot_strided_batch_buffer_size16rocsparse_handle13rocsparse_intPKdPKdPKdPKd13rocsparse_int13rocsparse_intP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cgtsv_no_pivot_strided_batch_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*dl, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*d, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*du, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*x,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_count,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_stride, size_t *buffer_size)[#](#_CPPv450rocsparse_cgtsv_no_pivot_strided_batch_buffer_size16rocsparse_handle13rocsparse_intPK23rocsparse_float_complexPK23rocsparse_float_complexPK23rocsparse_float_complexPK23rocsparse_float_complex13rocsparse_int13rocsparse_intP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zgtsv_no_pivot_strided_batch_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*dl, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*d, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*du, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*x,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_count,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_stride, size_t *buffer_size)[#](#_CPPv450rocsparse_zgtsv_no_pivot_strided_batch_buffer_size16rocsparse_handle13rocsparse_intPK24rocsparse_double_complexPK24rocsparse_double_complexPK24rocsparse_double_complexPK24rocsparse_double_complex13rocsparse_int13rocsparse_intP6size_t) `rocsparse_gtsv_no_pivot_strided_batch_buffer_size`

returns the size of the temporary storage buffer that is required by[rocsparse_Xgtsv_no_pivot_strided_batch()](#rocsparse__gtsv_8h_1a1d319185d35c86c564c0e84780142ab3). The temporary storage buffer must be allocated by the user.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**size of the tri-diagonal linear system.**dl**–**[in]**lower diagonal of tri-diagonal system where the ith system lower diagonal starts at`dl+batch_stride*i`

.**d**–**[in]**main diagonal of tri-diagonal system where the ith system diagonal starts at`d+batch_stride*i`

.**du**–**[in]**upper diagonal of tri-diagonal system where the ith system upper diagonal starts at`du+batch_stride*i`

.**x**–**[inout]**Dense array of righthand-sides where the ith righthand-side starts at`x+batch_stride*i`

.**batch_count**–**[in]**The number of systems to solve.**batch_stride**–**[in]**The number of elements that separate each system. Must satisfy`batch_stride`

>=`m`

.**buffer_size**–**[out]**number of bytes of the temporary storage buffer required by[rocsparse_Xgtsv_no_pivot_strided_batch()](#rocsparse__gtsv_8h_1a1d319185d35c86c564c0e84780142ab3).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`batch_count`

or`batch_stride`

is invalid.**rocsparse_status_invalid_pointer**–`dl`

,`d`

,`du`

,`x`

or`buffer_size`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_gtsv_no_pivot_strided_batch()[#](#rocsparse-gtsv-no-pivot-strided-batch)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sgtsv_no_pivot_strided_batch([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m, const float *dl, const float *d, const float *du, float *x,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_count,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_stride, void *temp_buffer)[#](#_CPPv438rocsparse_sgtsv_no_pivot_strided_batch16rocsparse_handle13rocsparse_intPKfPKfPKfPf13rocsparse_int13rocsparse_intPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dgtsv_no_pivot_strided_batch([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m, const double *dl, const double *d, const double *du, double *x,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_count,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_stride, void *temp_buffer)[#](#_CPPv438rocsparse_dgtsv_no_pivot_strided_batch16rocsparse_handle13rocsparse_intPKdPKdPKdPd13rocsparse_int13rocsparse_intPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cgtsv_no_pivot_strided_batch([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*dl, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*d, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*du,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*x,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_count,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_stride, void *temp_buffer)[#](#_CPPv438rocsparse_cgtsv_no_pivot_strided_batch16rocsparse_handle13rocsparse_intPK23rocsparse_float_complexPK23rocsparse_float_complexPK23rocsparse_float_complexP23rocsparse_float_complex13rocsparse_int13rocsparse_intPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zgtsv_no_pivot_strided_batch([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*dl, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*d, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*du,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*x,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_count,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_stride, void *temp_buffer)[#](#_CPPv438rocsparse_zgtsv_no_pivot_strided_batch16rocsparse_handle13rocsparse_intPK24rocsparse_double_complexPK24rocsparse_double_complexPK24rocsparse_double_complexP24rocsparse_double_complex13rocsparse_int13rocsparse_intPv) Strided Batch tridiagonal solver (no pivoting)

`rocsparse_gtsv_no_pivot_strided_batch`

solves a batched tridiagonal linear system\[ T^{i}*x^{i} = x^{i} \]where for each batch \(i=0\ldots\)`batch_count`

, \(T^{i}\) is a sparse tridiagonal matrix and \(x^{i}\) is a dense right-hand side vector. All of the tridiagonal matrices, \(T^{i}\), are packed one after the other into three vectors:`dl`

for the lower diagonals,`d`

for the main diagonals and`du`

for the upper diagonals. See below for a description of what this strided memory pattern looks like.Solving the batched tridiagonal system involves two steps. First, the user calls

[rocsparse_Xgtsv_no_pivot_strided_batch_buffer_size()](#rocsparse__gtsv_8h_1ab33c387ee7b44711b611cb225862276e)in order to determine the size of the required temporary storage buffer. Once determined, the user allocates this buffer and passes it to[rocsparse_Xgtsv_no_pivot_strided_batch()](#rocsparse__gtsv_8h_1a1d319185d35c86c564c0e84780142ab3)to perform the actual solve. The \(x^{i}\) vectors, which initially stores the right-hand side values, are overwritten with the solution after the call to[rocsparse_Xgtsv_no_pivot_strided_batch()](#rocsparse__gtsv_8h_1a1d319185d35c86c564c0e84780142ab3).The strided batch routines write each batch matrix one after the other in memory. For example, consider the following batch matrices:

\[\begin{split} \begin{bmatrix} t^{0}_{00} & t^{0}_{01} & 0 \\ t^{0}_{10} & t^{0}_{11} & t^{0}_{12} \\ 0 & t^{0}_{21} & t^{0}_{22} \end{bmatrix} \begin{bmatrix} t^{1}_{00} & t^{1}_{01} & 0 \\ t^{1}_{10} & t^{1}_{11} & t^{1}_{12} \\ 0 & t^{1}_{21} & t^{1}_{22} \end{bmatrix} \begin{bmatrix} t^{2}_{00} & t^{2}_{01} & 0 \\ t^{2}_{10} & t^{2}_{11} & t^{2}_{12} \\ 0 & t^{2}_{21} & t^{2}_{22} \end{bmatrix} \end{split}\]In strided format, the upper, lower, and diagonal arrays would look like:

\[\begin{split} \begin{align} \text{lower} &= \begin{bmatrix} 0 & t^{0}_{10} & t^{0}_{21} & 0 & t^{1}_{10} & t^{1}_{21} & 0 & t^{2}_{10} & t^{2}_{21} \end{bmatrix} \\ \text{diagonal} &= \begin{bmatrix} t^{0}_{00} & t^{0}_{11} & t^{0}_{22} & t^{1}_{00} & t^{1}_{11} & t^{1}_{22} & t^{2}_{00} & t^{2}_{11} & t^{2}_{22} \end{bmatrix} \\ \text{upper} &= \begin{bmatrix} t^{0}_{01} & t^{0}_{12} & 0 & t^{1}_{01} & t^{1}_{12} & 0 & t^{2}_{01} & t^{2}_{12} & 0 \end{bmatrix} \\ \end{align} \end{split}\]For the lower array, for each batch`i`

, the`i*batch_stride`

entries are zero and for the upper array the`i*batch_stride+batch_stride-1`

entries are zero.**Example**int main() { // Size of each square tridiagonal matrix int m = 6; // Number of batches int batch_count = 4; // Batch stride int batch_stride = m; // Host tridiagonal matrix std::vector<float> hdl(batch_stride * batch_count); std::vector<float> hd(batch_stride * batch_count); std::vector<float> hdu(batch_stride * batch_count); // Solve multiple tridiagonal matrix systems: // // 4 2 0 0 0 0 5 3 0 0 0 0 6 4 0 0 0 0 7 5 0 0 0 0 // 2 4 2 0 0 0 3 5 3 0 0 0 4 6 4 0 0 0 5 7 5 0 0 0 // A1 = 0 2 4 2 0 0 A2 = 0 3 5 3 0 0 A3 = 0 4 6 4 0 0 A4 = 0 5 7 5 0 0 // 0 0 2 4 2 0 0 0 3 5 3 0 0 0 4 6 4 0 0 0 5 7 5 0 // 0 0 0 2 4 2 0 0 0 3 5 3 0 0 0 4 6 4 0 0 0 5 7 5 // 0 0 0 0 2 4 0 0 0 0 3 5 0 0 0 0 4 6 0 0 0 0 5 7 // // hdl = 0 2 2 2 2 2 0 3 3 3 3 3 0 4 4 4 4 4 0 5 5 5 5 5 // hd = 4 4 4 4 4 4 5 5 5 5 5 5 6 6 6 6 6 6 7 7 7 7 7 7 // hdu = 2 2 2 2 2 0 3 3 3 3 3 0 4 4 4 4 4 0 5 5 5 5 5 0 for(int b = 0; b < batch_count; ++b) { for(rocsparse_int i = 0; i < m; ++i) { hdl[batch_stride * b + i] = 2 + b; hd[batch_stride * b + i] = 4 + b; hdu[batch_stride * b + i] = 2 + b; } hdl[batch_stride * b + 0] = 0.0f; hdu[batch_stride * b + (m - 1)] = 0.0f; } // Host dense rhs std::vector<float> hx(batch_stride * batch_count); for(int b = 0; b < batch_count; ++b) { for(int i = 0; i < m; ++i) { hx[batch_stride * b + i] = static_cast<float>(b + 1); } } float* ddl; float* dd; float* ddu; float* dx; HIP_CHECK(hipMalloc(&ddl, sizeof(float) * batch_stride * batch_count)); HIP_CHECK(hipMalloc(&dd, sizeof(float) * batch_stride * batch_count)); HIP_CHECK(hipMalloc(&ddu, sizeof(float) * batch_stride * batch_count)); HIP_CHECK(hipMalloc(&dx, sizeof(float) * batch_stride * batch_count)); HIP_CHECK(hipMemcpy( ddl, hdl.data(), sizeof(float) * batch_stride * batch_count, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( dd, hd.data(), sizeof(float) * batch_stride * batch_count, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( ddu, hdu.data(), sizeof(float) * batch_stride * batch_count, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( dx, hx.data(), sizeof(float) * batch_stride * batch_count, hipMemcpyHostToDevice)); // rocSPARSE handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Obtain required buffer size size_t buffer_size; ROCSPARSE_CHECK(rocsparse_sgtsv_no_pivot_strided_batch_buffer_size( handle, m, ddl, dd, ddu, dx, batch_count, batch_stride, &buffer_size)); void* dbuffer; HIP_CHECK(hipMalloc(&dbuffer, buffer_size)); ROCSPARSE_CHECK(rocsparse_sgtsv_no_pivot_strided_batch( handle, m, ddl, dd, ddu, dx, batch_count, batch_stride, dbuffer)); // Copy right-hand side to host HIP_CHECK(hipMemcpy( hx.data(), dx, sizeof(float) * batch_stride * batch_count, hipMemcpyDeviceToHost)); std::cout << "hx" << std::endl; for(size_t i = 0; i < hx.size(); i++) { std::cout << hx[i] << " "; } std::cout << "" << std::endl; // Clear rocSPARSE ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); // Clear device memory HIP_CHECK(hipFree(ddl)); HIP_CHECK(hipFree(dd)); HIP_CHECK(hipFree(ddu)); HIP_CHECK(hipFree(dx)); HIP_CHECK(hipFree(dbuffer)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**size of the tri-diagonal linear system (must be >= 2).**dl**–**[in]**lower diagonal of tri-diagonal system. First entry must be zero.**d**–**[in]**main diagonal of tri-diagonal system.**du**–**[in]**upper diagonal of tri-diagonal system. Last entry must be zero.**x**–**[inout]**Dense array of righthand-sides where the ith righthand-side starts at`x+batch_stride*i`

.**batch_count**–**[in]**The number of systems to solve.**batch_stride**–**[in]**The number of elements that separate each system. Must satisfy`batch_stride`

>=`m`

.**temp_buffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`batch_count`

or`batch_stride`

is invalid.**rocsparse_status_invalid_pointer**–`dl`

,`d`

,`du`

,`x`

or`temp_buffer`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_gtsv_interleaved_batch_buffer_size()[#](#rocsparse-gtsv-interleaved-batch-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sgtsv_interleaved_batch_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_gtsv_interleaved_alg](enumerations.html#_CPPv430rocsparse_gtsv_interleaved_alg)alg,[rocsparse_int](types.html#_CPPv413rocsparse_int)m, const float *dl, const float *d, const float *du, const float *x,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_count,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_stride, size_t *buffer_size)[#](#_CPPv445rocsparse_sgtsv_interleaved_batch_buffer_size16rocsparse_handle30rocsparse_gtsv_interleaved_alg13rocsparse_intPKfPKfPKfPKf13rocsparse_int13rocsparse_intP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dgtsv_interleaved_batch_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_gtsv_interleaved_alg](enumerations.html#_CPPv430rocsparse_gtsv_interleaved_alg)alg,[rocsparse_int](types.html#_CPPv413rocsparse_int)m, const double *dl, const double *d, const double *du, const double *x,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_count,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_stride, size_t *buffer_size)[#](#_CPPv445rocsparse_dgtsv_interleaved_batch_buffer_size16rocsparse_handle30rocsparse_gtsv_interleaved_alg13rocsparse_intPKdPKdPKdPKd13rocsparse_int13rocsparse_intP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cgtsv_interleaved_batch_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_gtsv_interleaved_alg](enumerations.html#_CPPv430rocsparse_gtsv_interleaved_alg)alg,[rocsparse_int](types.html#_CPPv413rocsparse_int)m, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*dl, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*d, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*du, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*x,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_count,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_stride, size_t *buffer_size)[#](#_CPPv445rocsparse_cgtsv_interleaved_batch_buffer_size16rocsparse_handle30rocsparse_gtsv_interleaved_alg13rocsparse_intPK23rocsparse_float_complexPK23rocsparse_float_complexPK23rocsparse_float_complexPK23rocsparse_float_complex13rocsparse_int13rocsparse_intP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zgtsv_interleaved_batch_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_gtsv_interleaved_alg](enumerations.html#_CPPv430rocsparse_gtsv_interleaved_alg)alg,[rocsparse_int](types.html#_CPPv413rocsparse_int)m, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*dl, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*d, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*du, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*x,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_count,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_stride, size_t *buffer_size)[#](#_CPPv445rocsparse_zgtsv_interleaved_batch_buffer_size16rocsparse_handle30rocsparse_gtsv_interleaved_alg13rocsparse_intPK24rocsparse_double_complexPK24rocsparse_double_complexPK24rocsparse_double_complexPK24rocsparse_double_complex13rocsparse_int13rocsparse_intP6size_t) `rocsparse_gtsv_interleaved_batch_buffer_size`

returns the size of the temporary storage buffer that is required by[rocsparse_Xgtsv_interleaved_batch()](#rocsparse__gtsv_8h_1a0941310c268b475bcd3339f4b251afb3). The temporary storage buffer must be allocated by the user.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**alg**–**[in]**Algorithm to use when solving tridiagonal systems. Options are thomas ([rocsparse_gtsv_interleaved_alg_thomas](enumerations.html#rocsparse-types_8h_1a0c121a0bb0b658587fb1e107096e129aa5b728e6e0b694c4f55235205712970ec)), LU ([rocsparse_gtsv_interleaved_alg_lu](enumerations.html#rocsparse-types_8h_1a0c121a0bb0b658587fb1e107096e129aa56fe081c0cd0724cd167d44f1aceb344)), or QR ([rocsparse_gtsv_interleaved_alg_qr](enumerations.html#rocsparse-types_8h_1a0c121a0bb0b658587fb1e107096e129aae5ad0ad9c5db640bd7a023db75102d8b)). Passing[rocsparse_gtsv_interleaved_alg_default](enumerations.html#rocsparse-types_8h_1a0c121a0bb0b658587fb1e107096e129aa591336d91b33c45167f163ed032fb3e8)defaults the algorithm to use QR. Thomas algorithm is the fastest but is not stable while LU and QR are slower but are stable.**m**–**[in]**size of the tri-diagonal linear system.**dl**–**[in]**lower diagonal of tri-diagonal system. The first element of the lower diagonal must be zero.**d**–**[in]**main diagonal of tri-diagonal system.**du**–**[in]**upper diagonal of tri-diagonal system. The last element of the upper diagonal must be zero.**x**–**[inout]**Dense array of righthand-sides with dimension`batch_stride`

by`m`

.**batch_count**–**[in]**The number of systems to solve.**batch_stride**–**[in]**The number of elements that separate consecutive elements in a system. Must satisfy`batch_stride`

>=`batch_count`

.**buffer_size**–**[out]**number of bytes of the temporary storage buffer required by[rocsparse_Xgtsv_interleaved_batch()](#rocsparse__gtsv_8h_1a0941310c268b475bcd3339f4b251afb3).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`batch_count`

,`batch_stride`

is invalid.**rocsparse_status_invalid_pointer**–`dl`

,`d`

,`du`

,`x`

or`buffer_size`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_gtsv_interleaved_batch()[#](#rocsparse-gtsv-interleaved-batch)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sgtsv_interleaved_batch([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_gtsv_interleaved_alg](enumerations.html#_CPPv430rocsparse_gtsv_interleaved_alg)alg,[rocsparse_int](types.html#_CPPv413rocsparse_int)m, float *dl, float *d, float *du, float *x,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_count,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_stride, void *temp_buffer)[#](#_CPPv433rocsparse_sgtsv_interleaved_batch16rocsparse_handle30rocsparse_gtsv_interleaved_alg13rocsparse_intPfPfPfPf13rocsparse_int13rocsparse_intPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dgtsv_interleaved_batch([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_gtsv_interleaved_alg](enumerations.html#_CPPv430rocsparse_gtsv_interleaved_alg)alg,[rocsparse_int](types.html#_CPPv413rocsparse_int)m, double *dl, double *d, double *du, double *x,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_count,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_stride, void *temp_buffer)[#](#_CPPv433rocsparse_dgtsv_interleaved_batch16rocsparse_handle30rocsparse_gtsv_interleaved_alg13rocsparse_intPdPdPdPd13rocsparse_int13rocsparse_intPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cgtsv_interleaved_batch([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_gtsv_interleaved_alg](enumerations.html#_CPPv430rocsparse_gtsv_interleaved_alg)alg,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*dl,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*d,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*du,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*x,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_count,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_stride, void *temp_buffer)[#](#_CPPv433rocsparse_cgtsv_interleaved_batch16rocsparse_handle30rocsparse_gtsv_interleaved_alg13rocsparse_intP23rocsparse_float_complexP23rocsparse_float_complexP23rocsparse_float_complexP23rocsparse_float_complex13rocsparse_int13rocsparse_intPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zgtsv_interleaved_batch([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_gtsv_interleaved_alg](enumerations.html#_CPPv430rocsparse_gtsv_interleaved_alg)alg,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*dl,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*d,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*du,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*x,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_count,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_stride, void *temp_buffer)[#](#_CPPv433rocsparse_zgtsv_interleaved_batch16rocsparse_handle30rocsparse_gtsv_interleaved_alg13rocsparse_intP24rocsparse_double_complexP24rocsparse_double_complexP24rocsparse_double_complexP24rocsparse_double_complex13rocsparse_int13rocsparse_intPv) Interleaved Batch tridiagonal solver.

`rocsparse_gtsv_interleaved_batch`

solves a batched tridiagonal linear system\[ T^{i}*x^{i} = x^{i} \]where for each batch \(i=0\ldots\)`batch_count`

, \(T^{i}\) is a sparse tridiagonal matrix and \(x^{i}\) is a dense right-hand side vector. All of the tridiagonal matrices, \(T^{i}\), are packed in an interleaved fashion into three vectors:`dl`

for the lower diagonals,`d`

for the main diagonals and`du`

for the upper diagonals. See below for a description of what this interleaved memory pattern looks like.Solving the batched tridiagonal system involves two steps. First, the user calls

[rocsparse_Xgtsv_interleaved_batch_buffer_size()](#rocsparse__gtsv_8h_1a897fb7b0e8e637296521cd5edfecc9ce)in order to determine the size of the required temporary storage buffer. Once determined, the user allocates this buffer and passes it to[rocsparse_Xgtsv_interleaved_batch()](#rocsparse__gtsv_8h_1a0941310c268b475bcd3339f4b251afb3)to perform the actual solve. The \(x^{i}\) vectors, which initially stores the right-hand side values, are overwritten with the solution after the call to[rocsparse_Xgtsv_interleaved_batch()](#rocsparse__gtsv_8h_1a0941310c268b475bcd3339f4b251afb3).The user can specify different algorithms for

`rocsparse_gtsv_interleaved_batch`

to use. Options are thomas ([rocsparse_gtsv_interleaved_alg_thomas](enumerations.html#rocsparse-types_8h_1a0c121a0bb0b658587fb1e107096e129aa5b728e6e0b694c4f55235205712970ec)), LU ([rocsparse_gtsv_interleaved_alg_lu](enumerations.html#rocsparse-types_8h_1a0c121a0bb0b658587fb1e107096e129aa56fe081c0cd0724cd167d44f1aceb344)), or QR ([rocsparse_gtsv_interleaved_alg_qr](enumerations.html#rocsparse-types_8h_1a0c121a0bb0b658587fb1e107096e129aae5ad0ad9c5db640bd7a023db75102d8b)). Passing[rocsparse_gtsv_interleaved_alg_default](enumerations.html#rocsparse-types_8h_1a0c121a0bb0b658587fb1e107096e129aa591336d91b33c45167f163ed032fb3e8)defaults the algorithm to use QR.Unlike the strided batch routines which write each batch matrix one after the other in memory, the interleaved routines write the batch matrices such that each element from each matrix is written consecutively one after the other. For example, consider the following batch matrices:

\[\begin{split} \begin{bmatrix} t^{0}_{00} & t^{0}_{01} & 0 \\ t^{0}_{10} & t^{0}_{11} & t^{0}_{12} \\ 0 & t^{0}_{21} & t^{0}_{22} \end{bmatrix} \begin{bmatrix} t^{1}_{00} & t^{1}_{01} & 0 \\ t^{1}_{10} & t^{1}_{11} & t^{1}_{12} \\ 0 & t^{1}_{21} & t^{1}_{22} \end{bmatrix} \begin{bmatrix} t^{2}_{00} & t^{2}_{01} & 0 \\ t^{2}_{10} & t^{2}_{11} & t^{2}_{12} \\ 0 & t^{2}_{21} & t^{2}_{22} \end{bmatrix} \end{split}\]In interleaved format, the upper, lower, and diagonal arrays would look like:

\[\begin{split} \begin{align} \text{lower} &= \begin{bmatrix} 0 & 0 & 0 & t^{0}_{10} & t^{1}_{10} & t^{1}_{10} & t^{0}_{21} & t^{1}_{21} & t^{2}_{21} \end{bmatrix} \\ \text{diagonal} &= \begin{bmatrix} t^{0}_{00} & t^{1}_{00} & t^{2}_{00} & t^{0}_{11} & t^{1}_{11} & t^{2}_{11} & t^{0}_{22} & t^{1}_{22} & t^{2}_{22} \end{bmatrix} \\ \text{upper} &= \begin{bmatrix} t^{0}_{01} & t^{1}_{01} & t^{2}_{01} & t^{0}_{12} & t^{1}_{12} & t^{2}_{12} & 0 & 0 & 0 \end{bmatrix} \\ \end{align} \end{split}\]For the lower array, the first`batch_count`

entries are zero and for the upper array the last`batch_count`

entries are zero.**Example**int main() { // Size of each square tridiagonal matrix rocsparse_int m = 6; // Number of batches rocsparse_int batch_count = 4; // Batch stride rocsparse_int batch_stride = batch_count; // Host tridiagonal matrix std::vector<float> hdl(m * batch_stride); std::vector<float> hd(m * batch_stride); std::vector<float> hdu(m * batch_stride); // Solve multiple tridiagonal matrix systems by interleaving matrices for better memory access: // // 4 2 0 0 0 0 5 3 0 0 0 0 6 4 0 0 0 0 7 5 0 0 0 0 // 2 4 2 0 0 0 3 5 3 0 0 0 4 6 4 0 0 0 5 7 5 0 0 0 // A1 = 0 2 4 2 0 0 A2 = 0 3 5 3 0 0 A3 = 0 4 6 4 0 0 A4 = 0 5 7 5 0 0 // 0 0 2 4 2 0 0 0 3 5 3 0 0 0 4 6 4 0 0 0 5 7 5 0 // 0 0 0 2 4 2 0 0 0 3 5 3 0 0 0 4 6 4 0 0 0 5 7 5 // 0 0 0 0 2 4 0 0 0 0 3 5 0 0 0 0 4 6 0 0 0 0 5 7 // // hdl = 0 0 0 0 2 3 4 5 2 3 4 5 2 3 4 5 2 3 4 5 2 3 4 5 // hd = 4 5 6 7 4 5 6 7 4 5 6 7 4 5 6 7 4 5 6 7 4 5 6 7 // hdu = 2 3 4 5 2 3 4 5 2 3 4 5 2 3 4 5 2 3 4 5 0 0 0 0 for(int b = 0; b < batch_count; ++b) { for(rocsparse_int i = 0; i < m; ++i) { hdl[batch_stride * i + b] = 2 + b; hd[batch_stride * i + b] = 4 + b; hdu[batch_stride * i + b] = 2 + b; } hdl[batch_stride * 0 + b] = 0.0f; hdu[batch_stride * (m - 1) + b] = 0.0f; } // Host dense rhs std::vector<float> hx(m * batch_stride); for(int b = 0; b < batch_count; ++b) { for(int i = 0; i < m; ++i) { hx[batch_stride * i + b] = static_cast<float>(b + 1); } } float* ddl; float* dd; float* ddu; float* dx; HIP_CHECK(hipMalloc(&ddl, sizeof(float) * m * batch_stride)); HIP_CHECK(hipMalloc(&dd, sizeof(float) * m * batch_stride)); HIP_CHECK(hipMalloc(&ddu, sizeof(float) * m * batch_stride)); HIP_CHECK(hipMalloc(&dx, sizeof(float) * m * batch_stride)); HIP_CHECK(hipMemcpy(ddl, hdl.data(), sizeof(float) * m * batch_stride, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dd, hd.data(), sizeof(float) * m * batch_stride, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(ddu, hdu.data(), sizeof(float) * m * batch_stride, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dx, hx.data(), sizeof(float) * m * batch_stride, hipMemcpyHostToDevice)); // rocSPARSE handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Obtain required buffer size size_t buffer_size; ROCSPARSE_CHECK( rocsparse_sgtsv_interleaved_batch_buffer_size(handle, rocsparse_gtsv_interleaved_alg_default, m, ddl, dd, ddu, dx, batch_count, batch_stride, &buffer_size)); void* dbuffer; HIP_CHECK(hipMalloc(&dbuffer, buffer_size)); ROCSPARSE_CHECK(rocsparse_sgtsv_interleaved_batch(handle, rocsparse_gtsv_interleaved_alg_default, m, ddl, dd, ddu, dx, batch_count, batch_stride, dbuffer)); // Copy right-hand side to host HIP_CHECK(hipMemcpy(hx.data(), dx, sizeof(float) * m * batch_stride, hipMemcpyDeviceToHost)); std::cout << "hx" << std::endl; for(size_t i = 0; i < hx.size(); i++) { std::cout << hx[i] << " "; } std::cout << "" << std::endl; // Clear rocSPARSE ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); // Clear device memory HIP_CHECK(hipFree(ddl)); HIP_CHECK(hipFree(dd)); HIP_CHECK(hipFree(ddu)); HIP_CHECK(hipFree(dx)); HIP_CHECK(hipFree(dbuffer)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**alg**–**[in]**Algorithm to use when solving tridiagonal systems. Options are thomas ([rocsparse_gtsv_interleaved_alg_thomas](enumerations.html#rocsparse-types_8h_1a0c121a0bb0b658587fb1e107096e129aa5b728e6e0b694c4f55235205712970ec)), LU ([rocsparse_gtsv_interleaved_alg_lu](enumerations.html#rocsparse-types_8h_1a0c121a0bb0b658587fb1e107096e129aa56fe081c0cd0724cd167d44f1aceb344)), or QR ([rocsparse_gtsv_interleaved_alg_qr](enumerations.html#rocsparse-types_8h_1a0c121a0bb0b658587fb1e107096e129aae5ad0ad9c5db640bd7a023db75102d8b)). Passing[rocsparse_gtsv_interleaved_alg_default](enumerations.html#rocsparse-types_8h_1a0c121a0bb0b658587fb1e107096e129aa591336d91b33c45167f163ed032fb3e8)defaults the algorithm to use QR. Thomas algorithm is the fastest but is not stable while LU and QR are slower but are stable.**m**–**[in]**size of the tri-diagonal linear system.**dl**–**[inout]**lower diagonal of tri-diagonal system. The first element of the lower diagonal must be zero.**d**–**[inout]**main diagonal of tri-diagonal system.**du**–**[inout]**upper diagonal of tri-diagonal system. The last element of the upper diagonal must be zero.**x**–**[inout]**Dense array of righthand-sides with dimension`batch_stride`

by`m`

.**batch_count**–**[in]**The number of systems to solve.**batch_stride**–**[in]**The number of elements that separate consecutive elements in a system. Must satisfy`batch_stride`

>=`batch_count`

.**temp_buffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`batch_count`

or`batch_stride`

is invalid.**rocsparse_status_invalid_pointer**–`dl`

,`d`

,`du`

,`x`

or`temp_buffer`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_gpsv_interleaved_batch_buffer_size()[#](#rocsparse-gpsv-interleaved-batch-buffer-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sgpsv_interleaved_batch_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_gpsv_interleaved_alg](enumerations.html#_CPPv430rocsparse_gpsv_interleaved_alg)alg,[rocsparse_int](types.html#_CPPv413rocsparse_int)m, const float *ds, const float *dl, const float *d, const float *du, const float *dw, const float *x,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_count,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_stride, size_t *buffer_size)[#](#_CPPv445rocsparse_sgpsv_interleaved_batch_buffer_size16rocsparse_handle30rocsparse_gpsv_interleaved_alg13rocsparse_intPKfPKfPKfPKfPKfPKf13rocsparse_int13rocsparse_intP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dgpsv_interleaved_batch_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_gpsv_interleaved_alg](enumerations.html#_CPPv430rocsparse_gpsv_interleaved_alg)alg,[rocsparse_int](types.html#_CPPv413rocsparse_int)m, const double *ds, const double *dl, const double *d, const double *du, const double *dw, const double *x,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_count,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_stride, size_t *buffer_size)[#](#_CPPv445rocsparse_dgpsv_interleaved_batch_buffer_size16rocsparse_handle30rocsparse_gpsv_interleaved_alg13rocsparse_intPKdPKdPKdPKdPKdPKd13rocsparse_int13rocsparse_intP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cgpsv_interleaved_batch_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_gpsv_interleaved_alg](enumerations.html#_CPPv430rocsparse_gpsv_interleaved_alg)alg,[rocsparse_int](types.html#_CPPv413rocsparse_int)m, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*ds, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*dl, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*d, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*du, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*dw, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*x,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_count,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_stride, size_t *buffer_size)[#](#_CPPv445rocsparse_cgpsv_interleaved_batch_buffer_size16rocsparse_handle30rocsparse_gpsv_interleaved_alg13rocsparse_intPK23rocsparse_float_complexPK23rocsparse_float_complexPK23rocsparse_float_complexPK23rocsparse_float_complexPK23rocsparse_float_complexPK23rocsparse_float_complex13rocsparse_int13rocsparse_intP6size_t)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zgpsv_interleaved_batch_buffer_size([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_gpsv_interleaved_alg](enumerations.html#_CPPv430rocsparse_gpsv_interleaved_alg)alg,[rocsparse_int](types.html#_CPPv413rocsparse_int)m, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*ds, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*dl, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*d, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*du, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*dw, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*x,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_count,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_stride, size_t *buffer_size)[#](#_CPPv445rocsparse_zgpsv_interleaved_batch_buffer_size16rocsparse_handle30rocsparse_gpsv_interleaved_alg13rocsparse_intPK24rocsparse_double_complexPK24rocsparse_double_complexPK24rocsparse_double_complexPK24rocsparse_double_complexPK24rocsparse_double_complexPK24rocsparse_double_complex13rocsparse_int13rocsparse_intP6size_t) `rocsparse_gpsv_interleaved_batch_buffer_size`

calculates the required buffer size for[rocsparse_Xgpsv_interleaved_batch()](#rocsparse__gpsv_8h_1a020a0c83c118f30ecb87b0c826acec77). It is the user’s responsibility to allocate this buffer.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**alg**–**[in]**algorithm to solve the linear system.**m**–**[in]**size of the pentadiagonal linear system.**ds**–**[in]**lower diagonal (distance 2) of pentadiagonal system. First two entries must be zero.**dl**–**[in]**lower diagonal of pentadiagonal system. First entry must be zero.**d**–**[in]**main diagonal of pentadiagonal system.**du**–**[in]**upper diagonal of pentadiagonal system. Last entry must be zero.**dw**–**[in]**upper diagonal (distance 2) of pentadiagonal system. Last two entries must be zero.**x**–**[in]**Dense array of right-hand-sides with dimension`batch_stride`

by`m`

.**batch_count**–**[in]**The number of systems to solve.**batch_stride**–**[in]**The number of elements that separate consecutive elements in a system. Must satisfy`batch_stride`

>=`batch_count`

.**buffer_size**–**[out]**Number of bytes of the temporary storage buffer required.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`alg`

,`batch_count`

or`batch_stride`

is invalid.**rocsparse_status_invalid_pointer**–`ds`

,`dl`

,`d`

,`du`

,`dw`

,`x`

or`temp_buffer`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_gpsv_interleaved_batch()[#](#rocsparse-gpsv-interleaved-batch)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sgpsv_interleaved_batch([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_gpsv_interleaved_alg](enumerations.html#_CPPv430rocsparse_gpsv_interleaved_alg)alg,[rocsparse_int](types.html#_CPPv413rocsparse_int)m, float *ds, float *dl, float *d, float *du, float *dw, float *x,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_count,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_stride, void *temp_buffer)[#](#_CPPv433rocsparse_sgpsv_interleaved_batch16rocsparse_handle30rocsparse_gpsv_interleaved_alg13rocsparse_intPfPfPfPfPfPf13rocsparse_int13rocsparse_intPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dgpsv_interleaved_batch([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_gpsv_interleaved_alg](enumerations.html#_CPPv430rocsparse_gpsv_interleaved_alg)alg,[rocsparse_int](types.html#_CPPv413rocsparse_int)m, double *ds, double *dl, double *d, double *du, double *dw, double *x,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_count,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_stride, void *temp_buffer)[#](#_CPPv433rocsparse_dgpsv_interleaved_batch16rocsparse_handle30rocsparse_gpsv_interleaved_alg13rocsparse_intPdPdPdPdPdPd13rocsparse_int13rocsparse_intPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_cgpsv_interleaved_batch([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_gpsv_interleaved_alg](enumerations.html#_CPPv430rocsparse_gpsv_interleaved_alg)alg,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*ds,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*dl,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*d,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*du,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*dw,[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*x,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_count,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_stride, void *temp_buffer)[#](#_CPPv433rocsparse_cgpsv_interleaved_batch16rocsparse_handle30rocsparse_gpsv_interleaved_alg13rocsparse_intP23rocsparse_float_complexP23rocsparse_float_complexP23rocsparse_float_complexP23rocsparse_float_complexP23rocsparse_float_complexP23rocsparse_float_complex13rocsparse_int13rocsparse_intPv)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zgpsv_interleaved_batch([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_gpsv_interleaved_alg](enumerations.html#_CPPv430rocsparse_gpsv_interleaved_alg)alg,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*ds,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*dl,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*d,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*du,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*dw,[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*x,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_count,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_stride, void *temp_buffer)[#](#_CPPv433rocsparse_zgpsv_interleaved_batch16rocsparse_handle30rocsparse_gpsv_interleaved_alg13rocsparse_intP24rocsparse_double_complexP24rocsparse_double_complexP24rocsparse_double_complexP24rocsparse_double_complexP24rocsparse_double_complexP24rocsparse_double_complex13rocsparse_int13rocsparse_intPv) Batched Pentadiagonal solver.

`rocsparse_gpsv_interleaved_batch`

solves a batch of pentadiagonal linear systems\[ P^{i}*x^{i} = x^{i} \]where for each batch \(i=0\ldots\)`batch_count`

, \(P^{i}\) is a sparse pentadiagonal matrix and \(x^{i}\) is a dense right-hand side vector. All of the pentadiagonal matrices, \(P^{i}\), are packed in an interleaved fashion into five vectors:`ds`

for the lowest diagonals,`dl`

for the lower diagonals,`d`

for the main diagonals,`du`

for the upper diagonals, and`dw`

for the highest digaonals. See below for a description of what this interleaved memory pattern looks like.Solving the batched pentadiagonal system involves two steps. First, the user calls

[rocsparse_Xgpsv_interleaved_batch_buffer_size()](#rocsparse__gpsv_8h_1ad94b154b62167a007f22572678170538)in order to determine the size of the required temporary storage buffer. Once determined, the user allocates this buffer and passes it to[rocsparse_Xgpsv_interleaved_batch()](#rocsparse__gpsv_8h_1a020a0c83c118f30ecb87b0c826acec77)to perform the actual solve. The \(x^{i}\) vectors, which initially stores the right-hand side values, are overwritten with the solution after the call to[rocsparse_Xgpsv_interleaved_batch()](#rocsparse__gpsv_8h_1a020a0c83c118f30ecb87b0c826acec77).Unlike the strided batch routines which write each batch matrix one after the other in memory, the interleaved routines write the batch matrices such that each element from each matrix is written consecutively one after the other. For example, consider the following batch matrices:

\[\begin{split} \begin{bmatrix} t^{0}_{00} & t^{0}_{01} & t^{0}_{02} \\ t^{0}_{10} & t^{0}_{11} & t^{0}_{12} \\ t^{0}_{20} & t^{0}_{21} & t^{0}_{22} \end{bmatrix} \begin{bmatrix} t^{1}_{00} & t^{1}_{01} & t^{1}_{02} \\ t^{1}_{10} & t^{1}_{11} & t^{1}_{12} \\ t^{1}_{20} & t^{1}_{21} & t^{1}_{22} \end{bmatrix} \begin{bmatrix} t^{2}_{00} & t^{2}_{01} & t^{2}_{02} \\ t^{2}_{10} & t^{2}_{11} & t^{2}_{12} \\ t^{2}_{20} & t^{2}_{21} & t^{2}_{22} \end{bmatrix} \end{split}\]In interleaved format, the highest, higher, lowest, lower, and diagonal arrays would look like:

\[\begin{split} \begin{align} \text{lowest} &= \begin{bmatrix} 0 & 0 & 0 & 0 & 0 & 0 & t^{0}_{20} & t^{1}_{20} & t^{2}_{20} \end{bmatrix} \\ \text{lower} &= \begin{bmatrix} 0 & 0 & 0 & t^{0}_{10} & t^{1}_{10} & t^{1}_{10} & t^{0}_{21} & t^{1}_{21} & t^{2}_{21} \end{bmatrix} \\ \text{diagonal} &= \begin{bmatrix} t^{0}_{00} & t^{1}_{00} & t^{2}_{00} & t^{0}_{11} & t^{1}_{11} & t^{2}_{11} & t^{0}_{22} & t^{1}_{22} & t^{2}_{22} \end{bmatrix} \\ \text{higher} &= \begin{bmatrix} t^{0}_{01} & t^{1}_{01} & t^{2}_{01} & t^{0}_{12} & t^{1}_{12} & t^{2}_{12} & 0 & 0 & 0 \end{bmatrix} \\ \text{highest} &= \begin{bmatrix} t^{0}_{02} & t^{1}_{02} & t^{2}_{02} & 0 & 0 & 0 & 0 & 0 & 0 \end{bmatrix} \\ \end{align} \end{split}\]For the lowest array, the first`2*batch_count`

entries are zero, for the lower array, the first`batch_count`

entries are zero, for the upper array the last`batch_count`

entries are zero, and for the highest array, the last`2*batch_count`

entries are zero.**Example**int main() { // Size of each square pentadiagonal matrix rocsparse_int m = 6; // Number of batches rocsparse_int batch_count = 4; // Batch stride rocsparse_int batch_stride = batch_count; // Host pentadiagonal matrix std::vector<float> hds(m * batch_stride); std::vector<float> hdl(m * batch_stride); std::vector<float> hd(m * batch_stride); std::vector<float> hdu(m * batch_stride); std::vector<float> hdw(m * batch_stride); // Solve multiple pentadiagonal matrix systems by interleaving matrices for better memory access: // // 4 2 1 0 0 0 5 3 2 0 0 0 6 4 3 0 0 0 7 5 4 0 0 0 // 2 4 2 1 0 0 3 5 3 2 0 0 4 6 4 3 0 0 5 7 5 4 0 0 // A1 = 1 2 4 2 1 0 A2 = 2 3 5 3 2 0 A3 = 3 4 6 4 3 0 A4 = 4 5 7 5 4 0 // 0 1 2 4 2 1 0 2 3 5 3 2 0 3 4 6 4 3 0 4 5 7 5 4 // 0 0 1 2 4 2 0 0 2 3 5 3 0 0 3 4 6 4 0 0 4 5 7 5 // 0 0 0 1 2 4 0 0 0 2 3 5 0 0 0 3 4 6 0 0 0 4 5 7 // // hds = 0 0 0 0 0 0 0 0 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 // hdl = 0 0 0 0 2 3 4 5 2 3 4 5 2 3 4 5 2 3 4 5 2 3 4 5 // hd = 4 5 6 7 4 5 6 7 4 5 6 7 4 5 6 7 4 5 6 7 4 5 6 7 // hdu = 2 3 4 5 2 3 4 5 2 3 4 5 2 3 4 5 2 3 4 5 0 0 0 0 // hdw = 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 0 0 0 0 0 0 0 0 for(int b = 0; b < batch_count; ++b) { for(rocsparse_int i = 0; i < m; ++i) { hds[batch_stride * i + b] = 1 + b; hdl[batch_stride * i + b] = 2 + b; hd[batch_stride * i + b] = 4 + b; hdu[batch_stride * i + b] = 2 + b; hdw[batch_stride * i + b] = 1 + b; } hds[batch_stride * 0 + b] = 0.0f; hds[batch_stride * 1 + b] = 0.0f; hdl[batch_stride * 0 + b] = 0.0f; hdu[batch_stride * (m - 1) + b] = 0.0f; hdw[batch_stride * (m - 1) + b] = 0.0f; hdw[batch_stride * (m - 2) + b] = 0.0f; } // Host dense rhs std::vector<float> hx(m * batch_stride); for(int b = 0; b < batch_count; ++b) { for(int i = 0; i < m; ++i) { hx[batch_stride * i + b] = static_cast<float>(b + 1); } } float* dds; float* ddl; float* dd; float* ddu; float* ddw; float* dx; HIP_CHECK(hipMalloc(&dds, sizeof(float) * m * batch_stride)); HIP_CHECK(hipMalloc(&ddl, sizeof(float) * m * batch_stride)); HIP_CHECK(hipMalloc(&dd, sizeof(float) * m * batch_stride)); HIP_CHECK(hipMalloc(&ddu, sizeof(float) * m * batch_stride)); HIP_CHECK(hipMalloc(&ddw, sizeof(float) * m * batch_stride)); HIP_CHECK(hipMalloc(&dx, sizeof(float) * m * batch_stride)); HIP_CHECK(hipMemcpy(dds, hds.data(), sizeof(float) * m * batch_stride, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(ddl, hdl.data(), sizeof(float) * m * batch_stride, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dd, hd.data(), sizeof(float) * m * batch_stride, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(ddu, hdu.data(), sizeof(float) * m * batch_stride, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(ddw, hdw.data(), sizeof(float) * m * batch_stride, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dx, hx.data(), sizeof(float) * m * batch_stride, hipMemcpyHostToDevice)); // rocSPARSE handle rocsparse_handle handle; ROCSPARSE_CHECK(rocsparse_create_handle(&handle)); // Obtain required buffer size size_t buffer_size; ROCSPARSE_CHECK( rocsparse_sgpsv_interleaved_batch_buffer_size(handle, rocsparse_gpsv_interleaved_alg_default, m, dds, ddl, dd, ddu, ddw, dx, batch_count, batch_stride, &buffer_size)); void* dbuffer; HIP_CHECK(hipMalloc(&dbuffer, buffer_size)); ROCSPARSE_CHECK(rocsparse_sgpsv_interleaved_batch(handle, rocsparse_gpsv_interleaved_alg_default, m, dds, ddl, dd, ddu, ddw, dx, batch_count, batch_stride, dbuffer)); // Copy right-hand side to host HIP_CHECK(hipMemcpy(hx.data(), dx, sizeof(float) * m * batch_stride, hipMemcpyDeviceToHost)); std::cout << "hx" << std::endl; for(size_t i = 0; i < hx.size(); i++) { std::cout << hx[i] << " "; } std::cout << "" << std::endl; // Clear rocSPARSE ROCSPARSE_CHECK(rocsparse_destroy_handle(handle)); // Clear device memory HIP_CHECK(hipFree(dds)); HIP_CHECK(hipFree(ddl)); HIP_CHECK(hipFree(dd)); HIP_CHECK(hipFree(ddu)); HIP_CHECK(hipFree(ddw)); HIP_CHECK(hipFree(dx)); HIP_CHECK(hipFree(dbuffer)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

The routine is numerically stable because it uses QR to solve the linear systems.

Note

m need to be at least 3, to be a valid pentadiagonal matrix.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**alg**–**[in]**algorithm to solve the linear system.**m**–**[in]**size of the pentadiagonal linear system.**ds**–**[inout]**lower diagonal (distance 2) of pentadiagonal system. First two entries must be zero.**dl**–**[inout]**lower diagonal of pentadiagonal system. First entry must be zero.**d**–**[inout]**main diagonal of pentadiagonal system.**du**–**[inout]**upper diagonal of pentadiagonal system. Last entry must be zero.**dw**–**[inout]**upper diagonal (distance 2) of pentadiagonal system. Last two entries must be zero.**x**–**[inout]**Dense array of right-hand-sides with dimension`batch_stride`

by`m`

.**batch_count**–**[in]**The number of systems to solve.**batch_stride**–**[in]**The number of elements that separate consecutive elements in a system. Must satisfy`batch_stride`

>=`batch_count`

.**temp_buffer**–**[in]**Temporary storage buffer allocated by the user.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

,`alg`

,`batch_count`

or`batch_stride`

is invalid.**rocsparse_status_invalid_pointer**–`ds`

,`dl`

,`d`

,`du`

,`dw`

,`x`

or`temp_buffer`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.
