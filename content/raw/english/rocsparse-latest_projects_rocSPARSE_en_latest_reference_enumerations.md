---
title: "rocSPARSE enumerations &#8212; rocSPARSE 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocSPARSE/en/latest/reference/enumerations.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:17:02.967937+00:00
content_hash: "1435e36a2e30b010"
---

# rocSPARSE enumerations[#](#rocsparse-enumerations)

## rocsparse_action[#](#rocsparse-action)

-
enum rocsparse_action
[#](#_CPPv416rocsparse_action) Specify where the operation is performed on.

The

[rocsparse_action](#rocsparse-types_8h_1a1ec75a33f6cf43e19b2b4e254213c465)indicates whether the operation is performed on the full matrix, or only on the sparsity pattern of the matrix.*Values:*-
enumerator rocsparse_action_symbolic
[#](#_CPPv4N16rocsparse_action25rocsparse_action_symbolicE) Operate only on indices.


-
enumerator rocsparse_action_numeric
[#](#_CPPv4N16rocsparse_action24rocsparse_action_numericE) Operate on data and indices.


-
enumerator rocsparse_action_symbolic

## rocsparse_direction[#](#rocsparse-direction)

-
enum rocsparse_direction
[#](#_CPPv419rocsparse_direction) Specify the matrix direction.

The

[rocsparse_direction](#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56c)indicates whether a dense matrix should be parsed by rows or by columns, assuming column-major storage.*Values:*-
enumerator rocsparse_direction_row
[#](#_CPPv4N19rocsparse_direction23rocsparse_direction_rowE) Parse the matrix by rows.


-
enumerator rocsparse_direction_column
[#](#_CPPv4N19rocsparse_direction26rocsparse_direction_columnE) Parse the matrix by columns.


-
enumerator rocsparse_direction_row

## rocsparse_hyb_partition[#](#rocsparse-hyb-partition)

-
enum rocsparse_hyb_partition
[#](#_CPPv423rocsparse_hyb_partition) HYB matrix partitioning type.

The

[rocsparse_hyb_partition](#rocsparse-types_8h_1a756fd5aab6f202ce45cbf151fc1a46a6)type indicates how the hybrid format partitioning between COO and ELL storage formats is performed.*Values:*-
enumerator rocsparse_hyb_partition_auto
[#](#_CPPv4N23rocsparse_hyb_partition28rocsparse_hyb_partition_autoE) automatically decide on ELL nnz per row.


-
enumerator rocsparse_hyb_partition_user
[#](#_CPPv4N23rocsparse_hyb_partition28rocsparse_hyb_partition_userE) user given ELL nnz per row.


-
enumerator rocsparse_hyb_partition_max
[#](#_CPPv4N23rocsparse_hyb_partition27rocsparse_hyb_partition_maxE) max ELL nnz per row, no COO part.


-
enumerator rocsparse_hyb_partition_auto

## rocsparse_index_base[#](#rocsparse-index-base)

-
enum rocsparse_index_base
[#](#_CPPv420rocsparse_index_base) Specify the matrix index base.

The

[rocsparse_index_base](#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060d)indicates the index base of the indices. For a given[rocsparse_mat_descr](types.html#rocsparse-types_8h_1a358745704b4da27fd600eb7cb2299b57), the[rocsparse_index_base](#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060d)can be set using[rocsparse_set_mat_index_base()](auxiliary.html#rocsparse-auxiliary_8h_1a590fbadaeab2d0edebbf14e2a82a3a8c). The current[rocsparse_index_base](#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060d)of a matrix can be obtained by[rocsparse_get_mat_index_base()](auxiliary.html#rocsparse-auxiliary_8h_1aa09fd820ec94d9ff94cbd136ea94a798).*Values:*-
enumerator rocsparse_index_base_zero
[#](#_CPPv4N20rocsparse_index_base25rocsparse_index_base_zeroE) zero based indexing.


-
enumerator rocsparse_index_base_one
[#](#_CPPv4N20rocsparse_index_base24rocsparse_index_base_oneE) one based indexing.


-
enumerator rocsparse_index_base_zero

## rocsparse_matrix_type[#](#rocsparse-matrix-type)

-
enum rocsparse_matrix_type
[#](#_CPPv421rocsparse_matrix_type) Specify the matrix type.

The

[rocsparse_matrix_type](#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)indicates the type of a matrix. For a given[rocsparse_mat_descr](types.html#rocsparse-types_8h_1a358745704b4da27fd600eb7cb2299b57), the[rocsparse_matrix_type](#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)can be set using[rocsparse_set_mat_type()](auxiliary.html#rocsparse-auxiliary_8h_1aee1ac5812c3291dce837a3d4e0847973). The current[rocsparse_matrix_type](#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)of a matrix can be obtained by[rocsparse_get_mat_type()](auxiliary.html#rocsparse-auxiliary_8h_1a209a3bd2100d5e02eed6f46a7d74cb88).For the matrix types

[rocsparse_matrix_type_symmetric](#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8340a3909d43b5b6bedd8ecc928605a5),[rocsparse_matrix_type_hermitian](#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75aa30592e2cccfda6e1d66dc3a484fc7a8), and[rocsparse_matrix_type_triangular](#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a73d9ef5e5e18209f9f10a5885d3e15ba), only the upper or lower part of the matrix (specified by setting the[rocsparse_fill_mode](#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1)) is assumed to be stored. The purpose of this is to minimize the amount of memory required to store the matrix.Routines that accept

[rocsparse_matrix_type_symmetric](#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8340a3909d43b5b6bedd8ecc928605a5)or[rocsparse_matrix_type_hermitian](#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75aa30592e2cccfda6e1d66dc3a484fc7a8)will only read from the stored upper or lower part of the matrix but will perform the computation as if the full symmetric/hermitian matrix existed. For example, when computing \(y=A*x\) where A is symmetric and only the lower part is stored, internally the multiplication will be performed in two steps. First the computation \(y=(L+D)*x\) will be performed. Secondly the multiplication will be completed by performing \(y=L^T*x + y\). This second step involves a transposed multiplication which is slower. For this reason, where space allows, it is faster to store the entire symmetric matrix and use[rocsparse_matrix_type_general](#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03)instead of[rocsparse_matrix_type_symmetric](#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8340a3909d43b5b6bedd8ecc928605a5).*Values:*-
enumerator rocsparse_matrix_type_general
[#](#_CPPv4N21rocsparse_matrix_type29rocsparse_matrix_type_generalE) general matrix type.


-
enumerator rocsparse_matrix_type_symmetric
[#](#_CPPv4N21rocsparse_matrix_type31rocsparse_matrix_type_symmetricE) symmetric matrix type.


-
enumerator rocsparse_matrix_type_hermitian
[#](#_CPPv4N21rocsparse_matrix_type31rocsparse_matrix_type_hermitianE) hermitian matrix type.


-
enumerator rocsparse_matrix_type_triangular
[#](#_CPPv4N21rocsparse_matrix_type32rocsparse_matrix_type_triangularE) triangular matrix type.


-
enumerator rocsparse_matrix_type_general

## rocsparse_fill_mode[#](#rocsparse-fill-mode)

-
enum rocsparse_fill_mode
[#](#_CPPv419rocsparse_fill_mode) Specify the matrix fill mode.

The

[rocsparse_fill_mode](#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1)indicates whether the lower or the upper part is stored in a sparse triangular matrix. For a given[rocsparse_mat_descr](types.html#rocsparse-types_8h_1a358745704b4da27fd600eb7cb2299b57), the[rocsparse_fill_mode](#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1)can be set using[rocsparse_set_mat_fill_mode()](auxiliary.html#rocsparse-auxiliary_8h_1aa1a9f7ba86427f6b56ea878fbee04db9). The current[rocsparse_fill_mode](#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1)of a matrix can be obtained by[rocsparse_get_mat_fill_mode()](auxiliary.html#rocsparse-auxiliary_8h_1a0439b9b04fd189fd0fc48640debfb2a6).*Values:*-
enumerator rocsparse_fill_mode_lower
[#](#_CPPv4N19rocsparse_fill_mode25rocsparse_fill_mode_lowerE) lower triangular part is stored.


-
enumerator rocsparse_fill_mode_upper
[#](#_CPPv4N19rocsparse_fill_mode25rocsparse_fill_mode_upperE) upper triangular part is stored.


-
enumerator rocsparse_fill_mode_lower

## rocsparse_storage_mode[#](#rocsparse-storage-mode)

-
enum rocsparse_storage_mode
[#](#_CPPv422rocsparse_storage_mode) Specify whether the matrix is stored sorted or not.

The

[rocsparse_storage_mode](#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13e)indicates whether the matrix is stored sorted or not. For a given[rocsparse_mat_descr](types.html#rocsparse-types_8h_1a358745704b4da27fd600eb7cb2299b57), the[rocsparse_storage_mode](#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13e)can be set using[rocsparse_set_mat_storage_mode()](auxiliary.html#rocsparse-auxiliary_8h_1a56de830362b6785ff367658ebe31fea7). The current[rocsparse_storage_mode](#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13e)of a matrix can be obtained by[rocsparse_get_mat_storage_mode()](auxiliary.html#rocsparse-auxiliary_8h_1aa5400bfd3394ff672a67ec83832b215c).*Values:*-
enumerator rocsparse_storage_mode_sorted
[#](#_CPPv4N22rocsparse_storage_mode29rocsparse_storage_mode_sortedE) matrix is sorted.


-
enumerator rocsparse_storage_mode_unsorted
[#](#_CPPv4N22rocsparse_storage_mode31rocsparse_storage_mode_unsortedE) matrix is unsorted.


-
enumerator rocsparse_storage_mode_sorted

## rocsparse_diag_type[#](#rocsparse-diag-type)

-
enum rocsparse_diag_type
[#](#_CPPv419rocsparse_diag_type) Indicates if the diagonal entries are unity.

The

[rocsparse_diag_type](#rocsparse-types_8h_1a6e8e038adcd3fa03168a1cb4a7da1bc5)indicates whether the diagonal entries of a matrix are unity or not. If[rocsparse_diag_type_unit](#rocsparse-types_8h_1a6e8e038adcd3fa03168a1cb4a7da1bc5ac14545fb3bf8773d5f6b8e258c9576f4)is specified, all present diagonal values will be ignored. For a given[rocsparse_mat_descr](types.html#rocsparse-types_8h_1a358745704b4da27fd600eb7cb2299b57), the[rocsparse_diag_type](#rocsparse-types_8h_1a6e8e038adcd3fa03168a1cb4a7da1bc5)can be set using[rocsparse_set_mat_diag_type()](auxiliary.html#rocsparse-auxiliary_8h_1a61f894d80e4da74c7e8cd43f61f9215c). The current[rocsparse_diag_type](#rocsparse-types_8h_1a6e8e038adcd3fa03168a1cb4a7da1bc5)of a matrix can be obtained by[rocsparse_get_mat_diag_type()](auxiliary.html#rocsparse-auxiliary_8h_1a430a6bd09bce5833909afa5410cc9891).*Values:*-
enumerator rocsparse_diag_type_non_unit
[#](#_CPPv4N19rocsparse_diag_type28rocsparse_diag_type_non_unitE) diagonal entries are non-unity.


-
enumerator rocsparse_diag_type_unit
[#](#_CPPv4N19rocsparse_diag_type24rocsparse_diag_type_unitE) diagonal entries are unity


-
enumerator rocsparse_diag_type_non_unit

## rocsparse_operation[#](#rocsparse-operation)

-
enum rocsparse_operation
[#](#_CPPv419rocsparse_operation) Specify whether the matrix is to be transposed or not.

The

[rocsparse_operation](#rocsparse-types_8h_1a820761e4768bb4f50a1ae78e722c8ca0)indicates the operation performed with the given matrix.*Values:*-
enumerator rocsparse_operation_none
[#](#_CPPv4N19rocsparse_operation24rocsparse_operation_noneE) Operate with matrix.


-
enumerator rocsparse_operation_transpose
[#](#_CPPv4N19rocsparse_operation29rocsparse_operation_transposeE) Operate with transpose.


-
enumerator rocsparse_operation_conjugate_transpose
[#](#_CPPv4N19rocsparse_operation39rocsparse_operation_conjugate_transposeE) Operate with conj. transpose.


-
enumerator rocsparse_operation_none

## rocsparse_pointer_mode[#](#rocsparse-pointer-mode)

-
enum rocsparse_pointer_mode
[#](#_CPPv422rocsparse_pointer_mode) Indicates if the pointer is device pointer or host pointer.

The

[rocsparse_pointer_mode](#rocsparse-types_8h_1a154fe9812f99d1f2c3db94c1ce561a15)indicates whether scalar values are passed by reference on the host or device. The[rocsparse_pointer_mode](#rocsparse-types_8h_1a154fe9812f99d1f2c3db94c1ce561a15)can be changed by[rocsparse_set_pointer_mode()](auxiliary.html#rocsparse-auxiliary_8h_1ae46f13354bf790cc26756c227bff7e64). The currently used pointer mode can be obtained by[rocsparse_get_pointer_mode()](auxiliary.html#rocsparse-auxiliary_8h_1a5d930dbb4f399250fa0ec283754d2a24).*Values:*-
enumerator rocsparse_pointer_mode_host
[#](#_CPPv4N22rocsparse_pointer_mode27rocsparse_pointer_mode_hostE) scalar pointers are in host memory.


-
enumerator rocsparse_pointer_mode_device
[#](#_CPPv4N22rocsparse_pointer_mode29rocsparse_pointer_mode_deviceE) scalar pointers are in device memory.


-
enumerator rocsparse_pointer_mode_host

## rocsparse_analysis_policy[#](#rocsparse-analysis-policy)

-
enum rocsparse_analysis_policy
[#](#_CPPv425rocsparse_analysis_policy) Specify policy in analysis functions.

The

[rocsparse_analysis_policy](#rocsparse-types_8h_1a43b20aa4bb19623a91b5952422fbe35c)specifies whether gathered analysis data should be re-used or not. If meta data from a previous e.g.[rocsparse_Xcsrilu0_analysis()](precond.html#rocsparse__csrilu0_8h_1a8b0496cb644c23fe65176e70315e431c)call is available, it can be re-used for subsequent calls to e.g.[rocsparse_Xcsrsv_analysis()](level2.html#rocsparse__csrsv_8h_1af710dcbc752ca8203389907bcbe74273)and greatly improve performance of the analysis function.*Values:*-
enumerator rocsparse_analysis_policy_reuse
[#](#_CPPv4N25rocsparse_analysis_policy31rocsparse_analysis_policy_reuseE) try to re-use meta data.


-
enumerator rocsparse_analysis_policy_force
[#](#_CPPv4N25rocsparse_analysis_policy31rocsparse_analysis_policy_forceE) force to re-build meta data.


-
enumerator rocsparse_analysis_policy_reuse

## rocsparse_solve_policy[#](#rocsparse-solve-policy)

## rocsparse_layer_mode[#](#rocsparse-layer-mode)

-
enum rocsparse_layer_mode
[#](#_CPPv420rocsparse_layer_mode) Indicates if layer is active with bitmask.

The

[rocsparse_layer_mode](#rocsparse-types_8h_1a062e1e182fefcda578bb4bd8925afb44)bit mask indicates the logging characteristics.*Values:*-
enumerator rocsparse_layer_mode_none
[#](#_CPPv4N20rocsparse_layer_mode25rocsparse_layer_mode_noneE) layer is not active.


-
enumerator rocsparse_layer_mode_log_trace
[#](#_CPPv4N20rocsparse_layer_mode30rocsparse_layer_mode_log_traceE) layer is in logging mode.


-
enumerator rocsparse_layer_mode_log_bench
[#](#_CPPv4N20rocsparse_layer_mode30rocsparse_layer_mode_log_benchE) layer is in benchmarking mode (deprecated)


-
enumerator rocsparse_layer_mode_log_debug
[#](#_CPPv4N20rocsparse_layer_mode30rocsparse_layer_mode_log_debugE) layer is in debug mode.


-
enumerator rocsparse_layer_mode_none

For more details on logging, see [Activity logging [Deprecated]](../how-to/using-rocsparse.html#rocsparse-logging).

## rocsparse_status[#](#rocsparse-status)

-
enum rocsparse_status
[#](#_CPPv416rocsparse_status) List of rocsparse status codes definition.

This is a list of the

[rocsparse_status](#rocsparse-types_8h_1a578f8c5c1b08f358bf4605b0031006a8)types that are used by the rocSPARSE library.*Values:*-
enumerator rocsparse_status_success
[#](#_CPPv4N16rocsparse_status24rocsparse_status_successE) success.


-
enumerator rocsparse_status_invalid_handle
[#](#_CPPv4N16rocsparse_status31rocsparse_status_invalid_handleE) handle not initialized, invalid or null.


-
enumerator rocsparse_status_not_implemented
[#](#_CPPv4N16rocsparse_status32rocsparse_status_not_implementedE) function is not implemented.


-
enumerator rocsparse_status_invalid_pointer
[#](#_CPPv4N16rocsparse_status32rocsparse_status_invalid_pointerE) invalid pointer parameter.


-
enumerator rocsparse_status_invalid_size
[#](#_CPPv4N16rocsparse_status29rocsparse_status_invalid_sizeE) invalid size parameter.


-
enumerator rocsparse_status_memory_error
[#](#_CPPv4N16rocsparse_status29rocsparse_status_memory_errorE) failed memory allocation, copy, dealloc.


-
enumerator rocsparse_status_internal_error
[#](#_CPPv4N16rocsparse_status31rocsparse_status_internal_errorE) other internal library failure.


-
enumerator rocsparse_status_invalid_value
[#](#_CPPv4N16rocsparse_status30rocsparse_status_invalid_valueE) invalid value parameter.


-
enumerator rocsparse_status_arch_mismatch
[#](#_CPPv4N16rocsparse_status30rocsparse_status_arch_mismatchE) device arch is not supported.


-
enumerator rocsparse_status_zero_pivot
[#](#_CPPv4N16rocsparse_status27rocsparse_status_zero_pivotE) encountered zero pivot.


-
enumerator rocsparse_status_not_initialized
[#](#_CPPv4N16rocsparse_status32rocsparse_status_not_initializedE) descriptor has not been initialized.


-
enumerator rocsparse_status_type_mismatch
[#](#_CPPv4N16rocsparse_status30rocsparse_status_type_mismatchE) index types do not match.


-
enumerator rocsparse_status_requires_sorted_storage
[#](#_CPPv4N16rocsparse_status40rocsparse_status_requires_sorted_storageE) sorted storage required.


-
enumerator rocsparse_status_thrown_exception
[#](#_CPPv4N16rocsparse_status33rocsparse_status_thrown_exceptionE) exception being thrown.


-
enumerator rocsparse_status_continue
[#](#_CPPv4N16rocsparse_status25rocsparse_status_continueE) Nothing preventing function to proceed


-
enumerator rocsparse_status_success

## rocsparse_data_status[#](#rocsparse-data-status)

-
enum rocsparse_data_status
[#](#_CPPv421rocsparse_data_status) List of rocsparse data status codes definition.

This is a list of the

[rocsparse_data_status](#rocsparse-types_8h_1aea14f8dcf7c5fa51edc841043e33a048)types that are used by the rocSPARSE library in the matrix check routines.*Values:*-
enumerator rocsparse_data_status_success
[#](#_CPPv4N21rocsparse_data_status29rocsparse_data_status_successE) success.


-
enumerator rocsparse_data_status_inf
[#](#_CPPv4N21rocsparse_data_status25rocsparse_data_status_infE) An inf value detected.


-
enumerator rocsparse_data_status_nan
[#](#_CPPv4N21rocsparse_data_status25rocsparse_data_status_nanE) An nan value detected.


-
enumerator rocsparse_data_status_invalid_offset_ptr
[#](#_CPPv4N21rocsparse_data_status40rocsparse_data_status_invalid_offset_ptrE) An invalid row pointer offset detected.


-
enumerator rocsparse_data_status_invalid_index
[#](#_CPPv4N21rocsparse_data_status35rocsparse_data_status_invalid_indexE) An invalid row indice detected.


-
enumerator rocsparse_data_status_duplicate_entry
[#](#_CPPv4N21rocsparse_data_status37rocsparse_data_status_duplicate_entryE) Duplicate indice detected.


-
enumerator rocsparse_data_status_invalid_sorting
[#](#_CPPv4N21rocsparse_data_status37rocsparse_data_status_invalid_sortingE) Incorrect sorting detected.


-
enumerator rocsparse_data_status_invalid_fill
[#](#_CPPv4N21rocsparse_data_status34rocsparse_data_status_invalid_fillE) Incorrect fill mode detected.


-
enumerator rocsparse_data_status_success

## rocsparse_indextype[#](#rocsparse-indextype)

## rocsparse_datatype[#](#rocsparse-datatype)

-
enum rocsparse_datatype
[#](#_CPPv418rocsparse_datatype) List of rocsparse data types.

Indicates the precision width of data stored in a rocsparse type.

*Values:*-
enumerator rocsparse_datatype_f16_r
[#](#_CPPv4N18rocsparse_datatype24rocsparse_datatype_f16_rE) 16 bit floating point, real.


-
enumerator rocsparse_datatype_f32_r
[#](#_CPPv4N18rocsparse_datatype24rocsparse_datatype_f32_rE) 32 bit floating point, real.


-
enumerator rocsparse_datatype_f64_r
[#](#_CPPv4N18rocsparse_datatype24rocsparse_datatype_f64_rE) 64 bit floating point, real.


-
enumerator rocsparse_datatype_f32_c
[#](#_CPPv4N18rocsparse_datatype24rocsparse_datatype_f32_cE) 32 bit floating point, complex.


-
enumerator rocsparse_datatype_f64_c
[#](#_CPPv4N18rocsparse_datatype24rocsparse_datatype_f64_cE) 64 bit floating point, complex.


-
enumerator rocsparse_datatype_i8_r
[#](#_CPPv4N18rocsparse_datatype23rocsparse_datatype_i8_rE) 8-bit signed integer, real


-
enumerator rocsparse_datatype_u8_r
[#](#_CPPv4N18rocsparse_datatype23rocsparse_datatype_u8_rE) 8-bit unsigned integer, real


-
enumerator rocsparse_datatype_i32_r
[#](#_CPPv4N18rocsparse_datatype24rocsparse_datatype_i32_rE) 32-bit signed integer, real


-
enumerator rocsparse_datatype_u32_r
[#](#_CPPv4N18rocsparse_datatype24rocsparse_datatype_u32_rE) 32-bit unsigned integer, real


-
enumerator rocsparse_datatype_bf16_r
[#](#_CPPv4N18rocsparse_datatype25rocsparse_datatype_bf16_rE) 16-bit brain floating point, real


-
enumerator rocsparse_datatype_f16_r

## rocsparse_format[#](#rocsparse-format)

-
enum rocsparse_format
[#](#_CPPv416rocsparse_format) List of sparse matrix formats.

This is a list of supported

[rocsparse_format](#rocsparse-types_8h_1ae1c0b9de06f3772ed14403400320b378)types that are used to describe a sparse matrix.*Values:*-
enumerator rocsparse_format_coo
[#](#_CPPv4N16rocsparse_format20rocsparse_format_cooE) COO sparse matrix format.


-
enumerator rocsparse_format_coo_aos
[#](#_CPPv4N16rocsparse_format24rocsparse_format_coo_aosE) COO AoS sparse matrix format.


-
enumerator rocsparse_format_csr
[#](#_CPPv4N16rocsparse_format20rocsparse_format_csrE) CSR sparse matrix format.


-
enumerator rocsparse_format_csc
[#](#_CPPv4N16rocsparse_format20rocsparse_format_cscE) CSC sparse matrix format.


-
enumerator rocsparse_format_ell
[#](#_CPPv4N16rocsparse_format20rocsparse_format_ellE) ELL sparse matrix format.


-
enumerator rocsparse_format_bell
[#](#_CPPv4N16rocsparse_format21rocsparse_format_bellE) BLOCKED ELL sparse matrix format.


-
enumerator rocsparse_format_bsr
[#](#_CPPv4N16rocsparse_format20rocsparse_format_bsrE) BSR sparse matrix format.


-
enumerator rocsparse_format_sell
[#](#_CPPv4N16rocsparse_format21rocsparse_format_sellE) SLICED ELL sparse matrix format.


-
enumerator rocsparse_format_coo

## rocsparse_order[#](#rocsparse-order)

-
enum rocsparse_order
[#](#_CPPv415rocsparse_order) List of dense matrix ordering.

This is a list of supported

[rocsparse_order](#rocsparse-types_8h_1a2c805a5d353c83120ba8b84cbff620fd)types that are used to describe the memory layout of a dense matrix*Values:*-
enumerator rocsparse_order_row
[#](#_CPPv4N15rocsparse_order19rocsparse_order_rowE) Row major.


-
enumerator rocsparse_order_column
[#](#_CPPv4N15rocsparse_order22rocsparse_order_columnE) Column major.


-
enumerator rocsparse_order_row

## rocsparse_spmat_attribute[#](#rocsparse-spmat-attribute)

-
enum rocsparse_spmat_attribute
[#](#_CPPv425rocsparse_spmat_attribute) List of sparse matrix attributes.

*Values:*-
enumerator rocsparse_spmat_fill_mode
[#](#_CPPv4N25rocsparse_spmat_attribute25rocsparse_spmat_fill_modeE) Fill mode attribute.


-
enumerator rocsparse_spmat_diag_type
[#](#_CPPv4N25rocsparse_spmat_attribute25rocsparse_spmat_diag_typeE) Diag type attribute.


-
enumerator rocsparse_spmat_matrix_type
[#](#_CPPv4N25rocsparse_spmat_attribute27rocsparse_spmat_matrix_typeE) Matrix type attribute.


-
enumerator rocsparse_spmat_storage_mode
[#](#_CPPv4N25rocsparse_spmat_attribute28rocsparse_spmat_storage_modeE) Matrix storage attribute.


-
enumerator rocsparse_spmat_fill_mode

## rocsparse_spmv_alg[#](#rocsparse-spmv-alg)

-
enum rocsparse_spmv_alg
[#](#_CPPv418rocsparse_spmv_alg) List of SpMV algorithms.

This is a list of supported

[rocsparse_spmv_alg](#rocsparse-types_8h_1aa25b92b978c68d431c22e04aec9b9491)types that are used to perform matrix vector product.*Values:*-
enumerator rocsparse_spmv_alg_default
[#](#_CPPv4N18rocsparse_spmv_alg26rocsparse_spmv_alg_defaultE) Default SpMV algorithm for the given format.


-
enumerator rocsparse_spmv_alg_coo
[#](#_CPPv4N18rocsparse_spmv_alg22rocsparse_spmv_alg_cooE) COO SpMV algorithm 1 (segmented) for COO matrices.


-
enumerator rocsparse_spmv_alg_csr_adaptive
[#](#_CPPv4N18rocsparse_spmv_alg31rocsparse_spmv_alg_csr_adaptiveE) CSR SpMV algorithm 1 (adaptive) for CSR matrices.


-
enumerator rocsparse_spmv_alg_csr_rowsplit
[#](#_CPPv4N18rocsparse_spmv_alg31rocsparse_spmv_alg_csr_rowsplitE) CSR SpMV algorithm 2 (rowsplit) for CSR matrices.


-
enumerator rocsparse_spmv_alg_ell
[#](#_CPPv4N18rocsparse_spmv_alg22rocsparse_spmv_alg_ellE) ELL SpMV algorithm for ELL matrices.


-
enumerator rocsparse_spmv_alg_coo_atomic
[#](#_CPPv4N18rocsparse_spmv_alg29rocsparse_spmv_alg_coo_atomicE) COO SpMV algorithm 2 (atomic) for COO matrices.


-
enumerator rocsparse_spmv_alg_bsr
[#](#_CPPv4N18rocsparse_spmv_alg22rocsparse_spmv_alg_bsrE) BSR SpMV algorithm 1 for BSR matrices.


-
enumerator rocsparse_spmv_alg_csr_lrb
[#](#_CPPv4N18rocsparse_spmv_alg26rocsparse_spmv_alg_csr_lrbE) CSR SpMV algorithm 3 (LRB) for CSR matrices.


-
enumerator rocsparse_spmv_alg_csr_nnzsplit
[#](#_CPPv4N18rocsparse_spmv_alg31rocsparse_spmv_alg_csr_nnzsplitE) CSR SpMV algorithm 4 (nnzsplit) for CSR matrices.


-
enumerator rocsparse_spmv_alg_sell
[#](#_CPPv4N18rocsparse_spmv_alg23rocsparse_spmv_alg_sellE) SLICED ELL SpMV algorithm for SLICED ELL matrices.


-
enumerator rocsparse_spmv_alg_csr_stream
[#](#_CPPv4N18rocsparse_spmv_alg29rocsparse_spmv_alg_csr_streamE) CSR SpMV algorithm 2 (stream) for CSR matrices.


-
enumerator rocsparse_spmv_alg_default

## rocsparse_spmv_stage[#](#rocsparse-spmv-stage)

-
enum rocsparse_spmv_stage
[#](#_CPPv420rocsparse_spmv_stage) List of SpMV stages.

This is a list of possible stages during SpMV computation. Typical order is

[rocsparse_spmv_stage_buffer_size](#rocsparse-types_8h_1ab2e40217ed05ec81a46674ecc91ce7bfafe51d3958904161b4b88990374760359),[rocsparse_spmv_stage_preprocess](#rocsparse-types_8h_1ab2e40217ed05ec81a46674ecc91ce7bfaf2b1eae60f0e1ebfb31f6af522a7b4ab),[rocsparse_spmv_stage_compute](#rocsparse-types_8h_1ab2e40217ed05ec81a46674ecc91ce7bfad920d865c566abca9171faade375ba67).*Values:*-
enumerator rocsparse_spmv_stage_buffer_size
[#](#_CPPv4N20rocsparse_spmv_stage32rocsparse_spmv_stage_buffer_sizeE) Returns the required buffer size.


-
enumerator rocsparse_spmv_stage_preprocess
[#](#_CPPv4N20rocsparse_spmv_stage31rocsparse_spmv_stage_preprocessE) Preprocess data.


-
enumerator rocsparse_spmv_stage_compute
[#](#_CPPv4N20rocsparse_spmv_stage28rocsparse_spmv_stage_computeE) Performs the actual SpMV computation.


-
enumerator rocsparse_spmv_stage_buffer_size

## rocsparse_spmv_input[#](#rocsparse-spmv-input)

-
enum rocsparse_spmv_input
[#](#_CPPv420rocsparse_spmv_input) List of inputs to SpMV descriptor.

This is a list of possible inputs to the SpMV descriptor.

*Values:*-
enumerator rocsparse_spmv_input_alg
[#](#_CPPv4N20rocsparse_spmv_input24rocsparse_spmv_input_algE) Select algorithm for input on SpMV descriptor.


-
enumerator rocsparse_spmv_input_operation
[#](#_CPPv4N20rocsparse_spmv_input30rocsparse_spmv_input_operationE) Select matrix transpose operation for input on SpMV descriptor.


-
enumerator rocsparse_spmv_input_scalar_datatype
[#](#_CPPv4N20rocsparse_spmv_input36rocsparse_spmv_input_scalar_datatypeE) Select scalar datatype for input on SpMV descriptor.


-
enumerator rocsparse_spmv_input_compute_datatype
[#](#_CPPv4N20rocsparse_spmv_input37rocsparse_spmv_input_compute_datatypeE) Select compute datatype for input on SpMV descriptor.


-
enumerator rocsparse_spmv_input_nnz_use_starting_block_ids
[#](#_CPPv4N20rocsparse_spmv_input47rocsparse_spmv_input_nnz_use_starting_block_idsE)

-
enumerator rocsparse_spmv_input_alg

## rocsparse_v2_spmv_stage[#](#rocsparse-v2-spmv-stage)

## rocsparse_spsv_alg[#](#rocsparse-spsv-alg)

-
enum rocsparse_spsv_alg
[#](#_CPPv418rocsparse_spsv_alg) List of SpSV algorithms.

This is a list of supported

[rocsparse_spsv_alg](#rocsparse-types_8h_1a6b5fcd2a14ff10d50e6a90d7993356e3)types that are used to perform triangular solve.*Values:*-
enumerator rocsparse_spsv_alg_default
[#](#_CPPv4N18rocsparse_spsv_alg26rocsparse_spsv_alg_defaultE) Default SpSV algorithm for the given format.


-
enumerator rocsparse_spsv_alg_default

## rocsparse_spsv_stage[#](#rocsparse-spsv-stage)

-
enum rocsparse_spsv_stage
[#](#_CPPv420rocsparse_spsv_stage) List of SpSV stages.

This is a list of possible stages during SpSV computation. Typical order is

[rocsparse_spsv_stage_buffer_size](#rocsparse-types_8h_1ada24ab514fc13a1d817d15d529e55dd2a7bb19094a3a9afafb2e95809f9e1b9ef),[rocsparse_spsv_stage_preprocess](#rocsparse-types_8h_1ada24ab514fc13a1d817d15d529e55dd2ad074073d1146296a5e1f9d7fde7f2bf1),[rocsparse_spsv_stage_compute](#rocsparse-types_8h_1ada24ab514fc13a1d817d15d529e55dd2a80386cc729d7f6610023e3853b65c5a1).*Values:*-
enumerator rocsparse_spsv_stage_buffer_size
[#](#_CPPv4N20rocsparse_spsv_stage32rocsparse_spsv_stage_buffer_sizeE) Returns the required buffer size.


-
enumerator rocsparse_spsv_stage_preprocess
[#](#_CPPv4N20rocsparse_spsv_stage31rocsparse_spsv_stage_preprocessE) Preprocess data.


-
enumerator rocsparse_spsv_stage_compute
[#](#_CPPv4N20rocsparse_spsv_stage28rocsparse_spsv_stage_computeE) Performs the actual SpSV computation.


-
enumerator rocsparse_spsv_stage_buffer_size

## rocsparse_sptrsv_alg[#](#rocsparse-sptrsv-alg)

-
enum rocsparse_sptrsv_alg
[#](#_CPPv420rocsparse_sptrsv_alg) List of SpTRSV algorithms.

This is a list of supported

[rocsparse_sptrsv_alg](#rocsparse-types_8h_1a74650ff283515a073f5302a3d323bf8e)types that are used to perform triangular solve.*Values:*-
enumerator rocsparse_sptrsv_alg_default
[#](#_CPPv4N20rocsparse_sptrsv_alg28rocsparse_sptrsv_alg_defaultE) Default SpTRSV algorithm for the given format.


-
enumerator rocsparse_sptrsv_alg_default

## rocsparse_sptrsv_stage[#](#rocsparse-sptrsv-stage)

## rocsparse_spsm_alg[#](#rocsparse-spsm-alg)

-
enum rocsparse_spsm_alg
[#](#_CPPv418rocsparse_spsm_alg) List of SpSM algorithms.

This is a list of supported

[rocsparse_spsm_alg](#rocsparse-types_8h_1adcf2a884f4f2774acfabd3eac70a154a)types that are used to perform triangular solve.*Values:*-
enumerator rocsparse_spsm_alg_default
[#](#_CPPv4N18rocsparse_spsm_alg26rocsparse_spsm_alg_defaultE) Default SpSM algorithm for the given format.


-
enumerator rocsparse_spsm_alg_default

## rocsparse_spsm_stage[#](#rocsparse-spsm-stage)

-
enum rocsparse_spsm_stage
[#](#_CPPv420rocsparse_spsm_stage) List of SpSM stages.

This is a list of possible stages during SpSM computation. Typical order is

[rocsparse_spsm_stage_buffer_size](#rocsparse-types_8h_1a69fa113206a9a3f650499469165d14acab21141ce4717eda3904c15f49090d728),[rocsparse_spsm_stage_preprocess](#rocsparse-types_8h_1a69fa113206a9a3f650499469165d14aca5251f8721c5114001d2ce9d4f7d826c1),[rocsparse_spsm_stage_compute](#rocsparse-types_8h_1a69fa113206a9a3f650499469165d14acad526329c59dca9ab138a4286c795b8a9).*Values:*-
enumerator rocsparse_spsm_stage_buffer_size
[#](#_CPPv4N20rocsparse_spsm_stage32rocsparse_spsm_stage_buffer_sizeE) Returns the required buffer size.


-
enumerator rocsparse_spsm_stage_preprocess
[#](#_CPPv4N20rocsparse_spsm_stage31rocsparse_spsm_stage_preprocessE) Preprocess data.


-
enumerator rocsparse_spsm_stage_compute
[#](#_CPPv4N20rocsparse_spsm_stage28rocsparse_spsm_stage_computeE) Performs the actual SpSM computation.


-
enumerator rocsparse_spsm_stage_buffer_size

## rocsparse_sptrsm_alg[#](#rocsparse-sptrsm-alg)

-
enum rocsparse_sptrsm_alg
[#](#_CPPv420rocsparse_sptrsm_alg) List of SpTRSM algorithms.

This is a list of supported

[rocsparse_sptrsm_alg](#rocsparse-types_8h_1a0452052df625c3ab5750e178d35e3263)types that are used to perform triangular solve.*Values:*-
enumerator rocsparse_sptrsm_alg_default
[#](#_CPPv4N20rocsparse_sptrsm_alg28rocsparse_sptrsm_alg_defaultE) Default SpTRSM algorithm for the given format.


-
enumerator rocsparse_sptrsm_alg_default

## rocsparse_sptrsm_stage[#](#rocsparse-sptrsm-stage)

## rocsparse_spmm_alg[#](#rocsparse-spmm-alg)

-
enum rocsparse_spmm_alg
[#](#_CPPv418rocsparse_spmm_alg) List of SpMM algorithms.

This is a list of supported

[rocsparse_spmm_alg](#rocsparse-types_8h_1afe9381434c79b9de70070cf8693ac441)types that are used to perform matrix vector product.*Values:*-
enumerator rocsparse_spmm_alg_default
[#](#_CPPv4N18rocsparse_spmm_alg26rocsparse_spmm_alg_defaultE) Default SpMM algorithm for the given format.


-
enumerator rocsparse_spmm_alg_csr
[#](#_CPPv4N18rocsparse_spmm_alg22rocsparse_spmm_alg_csrE) SpMM algorithm for CSR format using row split and shared memory.


-
enumerator rocsparse_spmm_alg_coo_segmented
[#](#_CPPv4N18rocsparse_spmm_alg32rocsparse_spmm_alg_coo_segmentedE) SpMM algorithm for COO format using segmented scan.


-
enumerator rocsparse_spmm_alg_coo_atomic
[#](#_CPPv4N18rocsparse_spmm_alg29rocsparse_spmm_alg_coo_atomicE) SpMM algorithm for COO format using atomics.


-
enumerator rocsparse_spmm_alg_csr_row_split
[#](#_CPPv4N18rocsparse_spmm_alg32rocsparse_spmm_alg_csr_row_splitE) SpMM algorithm for CSR format using row split and shfl.


-
enumerator rocsparse_spmm_alg_csr_merge
[#](#_CPPv4N18rocsparse_spmm_alg28rocsparse_spmm_alg_csr_mergeE) SpMM algorithm for CSR format using nnz split algorithm. Is the same as rocsparse_spmm_alg_csr_nnz_split.


-
enumerator rocsparse_spmm_alg_coo_segmented_atomic
[#](#_CPPv4N18rocsparse_spmm_alg39rocsparse_spmm_alg_coo_segmented_atomicE) SpMM algorithm for COO format using segmented scan and atomics.


-
enumerator rocsparse_spmm_alg_bell
[#](#_CPPv4N18rocsparse_spmm_alg23rocsparse_spmm_alg_bellE) SpMM algorithm for Blocked ELL format.


-
enumerator rocsparse_spmm_alg_bsr
[#](#_CPPv4N18rocsparse_spmm_alg22rocsparse_spmm_alg_bsrE) SpMM algorithm for BSR format.


-
enumerator rocsparse_spmm_alg_csr_merge_path
[#](#_CPPv4N18rocsparse_spmm_alg33rocsparse_spmm_alg_csr_merge_pathE) SpMM algorithm for CSR format using merge path algorithm.


-
enumerator rocsparse_spmm_alg_csr_nnz_split
[#](#_CPPv4N18rocsparse_spmm_alg32rocsparse_spmm_alg_csr_nnz_splitE) SpMM algorithm for CSR format using nnz split algorithm.


-
enumerator rocsparse_spmm_alg_default

## rocsparse_spmm_stage[#](#rocsparse-spmm-stage)

-
enum rocsparse_spmm_stage
[#](#_CPPv420rocsparse_spmm_stage) List of SpMM stages.

This is a list of possible stages during SpMM computation. Typical order is

[rocsparse_spmm_stage_buffer_size](#rocsparse-types_8h_1a28daf89fa49ded50158dcda6e5045aafaef94fe80b7c181dd56d06df7eca379a1),[rocsparse_spmm_stage_preprocess](#rocsparse-types_8h_1a28daf89fa49ded50158dcda6e5045aaface910c4e7024c7fff1c8749849126f2e),[rocsparse_spmm_stage_compute](#rocsparse-types_8h_1a28daf89fa49ded50158dcda6e5045aafaeb9be614ccccf840f3f529786e037259).*Values:*-
enumerator rocsparse_spmm_stage_buffer_size
[#](#_CPPv4N20rocsparse_spmm_stage32rocsparse_spmm_stage_buffer_sizeE) Returns the required buffer size.


-
enumerator rocsparse_spmm_stage_preprocess
[#](#_CPPv4N20rocsparse_spmm_stage31rocsparse_spmm_stage_preprocessE) Preprocess data.


-
enumerator rocsparse_spmm_stage_compute
[#](#_CPPv4N20rocsparse_spmm_stage28rocsparse_spmm_stage_computeE) Performs the actual SpMM computation.


-
enumerator rocsparse_spmm_stage_buffer_size

## rocsparse_sddmm_alg[#](#rocsparse-sddmm-alg)

-
enum rocsparse_sddmm_alg
[#](#_CPPv419rocsparse_sddmm_alg) List of sddmm algorithms.

This is a list of supported

[rocsparse_sddmm_alg](#rocsparse-types_8h_1ac8fbc731ff97c543c29c8c9a08f8ba63)types that are used to perform matrix vector product.*Values:*-
enumerator rocsparse_sddmm_alg_default
[#](#_CPPv4N19rocsparse_sddmm_alg27rocsparse_sddmm_alg_defaultE) Default sddmm algorithm for the given format.


-
enumerator rocsparse_sddmm_alg_dense
[#](#_CPPv4N19rocsparse_sddmm_alg25rocsparse_sddmm_alg_denseE) Sddmm algorithm using dense blas operations.


-
enumerator rocsparse_sddmm_alg_default

## rocsparse_spgemm_stage[#](#rocsparse-spgemm-stage)

-
enum rocsparse_spgemm_stage
[#](#_CPPv422rocsparse_spgemm_stage) List of SpGEMM stages.

This is a list of possible stages during SpGEMM computation. Typical order is

[rocsparse_spgemm_stage_buffer_size](#rocsparse-types_8h_1a66732fbd958d714d7cf5f57250d550b0ad8ea174ec74b7e7596847c5e3864fa28),[rocsparse_spgemm_stage_nnz](#rocsparse-types_8h_1a66732fbd958d714d7cf5f57250d550b0afd089e430f158fd2fb18c900345a1f32),[rocsparse_spgemm_stage_compute](#rocsparse-types_8h_1a66732fbd958d714d7cf5f57250d550b0afac1ee9c06823f6cb6e92ee682e83369).*Values:*-
enumerator rocsparse_spgemm_stage_buffer_size
[#](#_CPPv4N22rocsparse_spgemm_stage34rocsparse_spgemm_stage_buffer_sizeE) Returns the required buffer size.


-
enumerator rocsparse_spgemm_stage_nnz
[#](#_CPPv4N22rocsparse_spgemm_stage26rocsparse_spgemm_stage_nnzE) Computes number of non-zero entries.


-
enumerator rocsparse_spgemm_stage_compute
[#](#_CPPv4N22rocsparse_spgemm_stage30rocsparse_spgemm_stage_computeE) Performs the actual SpGEMM computation.


-
enumerator rocsparse_spgemm_stage_symbolic
[#](#_CPPv4N22rocsparse_spgemm_stage31rocsparse_spgemm_stage_symbolicE) Performs the actual SpGEMM symbolic computation.


-
enumerator rocsparse_spgemm_stage_numeric
[#](#_CPPv4N22rocsparse_spgemm_stage30rocsparse_spgemm_stage_numericE) Performs the actual SpGEMM numeric computation.


-
enumerator rocsparse_spgemm_stage_buffer_size

## rocsparse_spgemm_alg[#](#rocsparse-spgemm-alg)

-
enum rocsparse_spgemm_alg
[#](#_CPPv420rocsparse_spgemm_alg) List of SpGEMM algorithms.

This is a list of supported

[rocsparse_spgemm_alg](#rocsparse-types_8h_1a3eebec64a1ebec0e48327028e894687a)types that are used to perform sparse matrix sparse matrix product.*Values:*-
enumerator rocsparse_spgemm_alg_default
[#](#_CPPv4N20rocsparse_spgemm_alg28rocsparse_spgemm_alg_defaultE) Default SpGEMM algorithm for the given format.


-
enumerator rocsparse_spgemm_alg_default

## rocsparse_spgeam_stage[#](#rocsparse-spgeam-stage)

-
enum rocsparse_spgeam_stage
[#](#_CPPv422rocsparse_spgeam_stage) List of SpGEAM stages.

This is a list of possible stages during SpGEAM computation. Typical order is rocsparse_spgeam_stage_buffer_size, rocsparse_spgeam_stage_analysis, rocsparse_spgeam_stage_compute.

*Values:*-
enumerator rocsparse_spgeam_stage_analysis
[#](#_CPPv4N22rocsparse_spgeam_stage31rocsparse_spgeam_stage_analysisE) Computes number of non-zero entries.


-
enumerator rocsparse_spgeam_stage_compute
[#](#_CPPv4N22rocsparse_spgeam_stage30rocsparse_spgeam_stage_computeE) Performs the actual SpGEAM computation.


-
enumerator rocsparse_spgeam_stage_symbolic_analysis
[#](#_CPPv4N22rocsparse_spgeam_stage40rocsparse_spgeam_stage_symbolic_analysisE) Performs only the symbolic analysis SpGEAM computation to fill the column indices array.


-
enumerator rocsparse_spgeam_stage_symbolic_compute
[#](#_CPPv4N22rocsparse_spgeam_stage39rocsparse_spgeam_stage_symbolic_computeE) Performs only the symbolic SpGEAM computation to fill the column indices array.


-
enumerator rocsparse_spgeam_stage_numeric_analysis
[#](#_CPPv4N22rocsparse_spgeam_stage39rocsparse_spgeam_stage_numeric_analysisE) Performs only the numeric analysis SpGEAM computation to fill the values array.


-
enumerator rocsparse_spgeam_stage_numeric_compute
[#](#_CPPv4N22rocsparse_spgeam_stage38rocsparse_spgeam_stage_numeric_computeE) Performs only the numeric SpGEAM computation to fill the values array.


-
enumerator rocsparse_spgeam_stage_analysis

## rocsparse_spgeam_alg[#](#rocsparse-spgeam-alg)

-
enum rocsparse_spgeam_alg
[#](#_CPPv420rocsparse_spgeam_alg) List of SpGEAM algorithms.

This is a list of supported

[rocsparse_spgeam_alg](#rocsparse-types_8h_1a8adf9059fb87b3047c50bd347c8c4e13)types that are used to perform sparse matrix sparse matrix product.*Values:*-
enumerator rocsparse_spgeam_alg_default
[#](#_CPPv4N20rocsparse_spgeam_alg28rocsparse_spgeam_alg_defaultE) Default SpGEAM algorithm for the given format.


-
enumerator rocsparse_spgeam_alg_default

## rocsparse_spgeam_input[#](#rocsparse-spgeam-input)

-
enum rocsparse_spgeam_input
[#](#_CPPv422rocsparse_spgeam_input) List of inputs to SpGEAM descriptor.

This is a list of possible inputs to the SpGEAM descriptor.

*Values:*-
enumerator rocsparse_spgeam_input_alg
[#](#_CPPv4N22rocsparse_spgeam_input26rocsparse_spgeam_input_algE) Select algorithm for input on SpGEAM descriptor.


-
enumerator rocsparse_spgeam_input_scalar_datatype
[#](#_CPPv4N22rocsparse_spgeam_input38rocsparse_spgeam_input_scalar_datatypeE) Select scalar data type for input on SpGEAM descriptor.


-
enumerator rocsparse_spgeam_input_compute_datatype
[#](#_CPPv4N22rocsparse_spgeam_input39rocsparse_spgeam_input_compute_datatypeE) Select compute data type for input on SpGEAM descriptor.


-
enumerator rocsparse_spgeam_input_operation_A
[#](#_CPPv4N22rocsparse_spgeam_input34rocsparse_spgeam_input_operation_AE) Select A matrix transpose operation for input on SpGEAM descriptor.


-
enumerator rocsparse_spgeam_input_operation_B
[#](#_CPPv4N22rocsparse_spgeam_input34rocsparse_spgeam_input_operation_BE) Select B matrix transpose operation for input on SpGEAM descriptor.


-
enumerator rocsparse_spgeam_input_scalar_alpha
[#](#_CPPv4N22rocsparse_spgeam_input35rocsparse_spgeam_input_scalar_alphaE) Select scalar multiplier alpha for input on SpGEAM descriptor.


-
enumerator rocsparse_spgeam_input_scalar_beta
[#](#_CPPv4N22rocsparse_spgeam_input34rocsparse_spgeam_input_scalar_betaE) Select scalar multiplier beta for input on SpGEAM descriptor.


-
enumerator rocsparse_spgeam_input_alg

## rocsparse_spgeam_output[#](#rocsparse-spgeam-output)

## rocsparse_sparse_to_dense_alg[#](#rocsparse-sparse-to-dense-alg)

-
enum rocsparse_sparse_to_dense_alg
[#](#_CPPv429rocsparse_sparse_to_dense_alg) List of sparse to dense algorithms.

This is a list of supported

[rocsparse_sparse_to_dense_alg](#rocsparse-types_8h_1a20425e827ea9be6bde28db1538e007ea)types that are used to perform sparse to dense conversion.*Values:*-
enumerator rocsparse_sparse_to_dense_alg_default
[#](#_CPPv4N29rocsparse_sparse_to_dense_alg37rocsparse_sparse_to_dense_alg_defaultE) Default sparse to dense algorithm for the given format.


-
enumerator rocsparse_sparse_to_dense_alg_default

## rocsparse_sparse_to_sparse_alg[#](#rocsparse-sparse-to-sparse-alg)

-
enum rocsparse_sparse_to_sparse_alg
[#](#_CPPv430rocsparse_sparse_to_sparse_alg) List of sparse to sparse algorithms.

This is a list of supported

[rocsparse_sparse_to_sparse_alg](#rocsparse-types_8h_1a6220f7b0defca36a071dc37ba7adcc7b)types that are used to perform sparse to sparse conversion.*Values:*-
enumerator rocsparse_sparse_to_sparse_alg_default
[#](#_CPPv4N30rocsparse_sparse_to_sparse_alg38rocsparse_sparse_to_sparse_alg_defaultE) Default sparse to sparse algorithm for the given format.


-
enumerator rocsparse_sparse_to_sparse_alg_default

## rocsparse_sparse_to_sparse_stage[#](#rocsparse-sparse-to-sparse-stage)

-
enum rocsparse_sparse_to_sparse_stage
[#](#_CPPv432rocsparse_sparse_to_sparse_stage) List of sparse_to_sparse stages.

This is a list of possible stages during sparse_to_sparse conversion. Typical order is

[rocsparse_sparse_to_sparse_stage_analysis](#rocsparse-types_8h_1abfa35c63f3dc85a5b6ce031dadf2d124af813df4a9f700fc49472b0ccf96944c1),[rocsparse_sparse_to_sparse_stage_compute](#rocsparse-types_8h_1abfa35c63f3dc85a5b6ce031dadf2d124a952622a17f83c241e2d7cfabbe9b6e81).*Values:*-
enumerator rocsparse_sparse_to_sparse_stage_analysis
[#](#_CPPv4N32rocsparse_sparse_to_sparse_stage41rocsparse_sparse_to_sparse_stage_analysisE) Data analysis.


-
enumerator rocsparse_sparse_to_sparse_stage_compute
[#](#_CPPv4N32rocsparse_sparse_to_sparse_stage40rocsparse_sparse_to_sparse_stage_computeE) Performs the actual conversion.


-
enumerator rocsparse_sparse_to_sparse_stage_analysis

## rocsparse_extract_alg[#](#rocsparse-extract-alg)

-
enum rocsparse_extract_alg
[#](#_CPPv421rocsparse_extract_alg) List of extract algorithms.

This is a list of supported

[rocsparse_extract_alg](#rocsparse-types_8h_1acaa8c058a3a9fbfeb2c4f2cce3e85b08)types that are used to perform the submatrix extraction.*Values:*-
enumerator rocsparse_extract_alg_default
[#](#_CPPv4N21rocsparse_extract_alg29rocsparse_extract_alg_defaultE) Default extract algorithm for the given format.


-
enumerator rocsparse_extract_alg_default

## rocsparse_extract_stage[#](#rocsparse-extract-stage)

-
enum rocsparse_extract_stage
[#](#_CPPv423rocsparse_extract_stage) List of extract stages.

The analysis

[rocsparse_extract_stage_analysis](#rocsparse-types_8h_1a884a4bd3e6b822da9a23b56f89a2e594ae083d0e64809b25bca57ce146d3d080f)must be done before the first call of the calculation[rocsparse_extract_stage_compute](#rocsparse-types_8h_1a884a4bd3e6b822da9a23b56f89a2e594a80bf2aa6b71ba18c1ee7b1c591c05b3c).*Values:*-
enumerator rocsparse_extract_stage_analysis
[#](#_CPPv4N23rocsparse_extract_stage32rocsparse_extract_stage_analysisE) Data analysis.


-
enumerator rocsparse_extract_stage_compute
[#](#_CPPv4N23rocsparse_extract_stage31rocsparse_extract_stage_computeE) Performs the actual extraction.


-
enumerator rocsparse_extract_stage_analysis

## rocsparse_dense_to_sparse_alg[#](#rocsparse-dense-to-sparse-alg)

-
enum rocsparse_dense_to_sparse_alg
[#](#_CPPv429rocsparse_dense_to_sparse_alg) List of dense to sparse algorithms.

This is a list of supported

[rocsparse_dense_to_sparse_alg](#rocsparse-types_8h_1aa5befb67d77c1c17652d3cf5d23a1127)types that are used to perform dense to sparse conversion.*Values:*-
enumerator rocsparse_dense_to_sparse_alg_default
[#](#_CPPv4N29rocsparse_dense_to_sparse_alg37rocsparse_dense_to_sparse_alg_defaultE) Default dense to sparse algorithm for the given format.


-
enumerator rocsparse_dense_to_sparse_alg_default

## rocsparse_gtsv_interleaved_alg[#](#rocsparse-gtsv-interleaved-alg)

-
enum rocsparse_gtsv_interleaved_alg
[#](#_CPPv430rocsparse_gtsv_interleaved_alg) List of interleaved gtsv algorithms.

This is a list of supported

[rocsparse_gtsv_interleaved_alg](#rocsparse-types_8h_1a0c121a0bb0b658587fb1e107096e129a)types that are used to perform interleaved tridiagonal solve.*Values:*-
enumerator rocsparse_gtsv_interleaved_alg_default
[#](#_CPPv4N30rocsparse_gtsv_interleaved_alg38rocsparse_gtsv_interleaved_alg_defaultE) Solve interleaved gtsv using QR algorithm (stable).


-
enumerator rocsparse_gtsv_interleaved_alg_thomas
[#](#_CPPv4N30rocsparse_gtsv_interleaved_alg37rocsparse_gtsv_interleaved_alg_thomasE) Solve interleaved gtsv using thomas algorithm (unstable).


-
enumerator rocsparse_gtsv_interleaved_alg_lu
[#](#_CPPv4N30rocsparse_gtsv_interleaved_alg33rocsparse_gtsv_interleaved_alg_luE) Solve interleaved gtsv using LU algorithm (stable).


-
enumerator rocsparse_gtsv_interleaved_alg_qr
[#](#_CPPv4N30rocsparse_gtsv_interleaved_alg33rocsparse_gtsv_interleaved_alg_qrE) Solve interleaved gtsv using QR algorithm (stable).


-
enumerator rocsparse_gtsv_interleaved_alg_default

## rocsparse_gpsv_interleaved_alg[#](#rocsparse-gpsv-interleaved-alg)

-
enum rocsparse_gpsv_interleaved_alg
[#](#_CPPv430rocsparse_gpsv_interleaved_alg) List of gpsv algorithms.

This is a list of supported

[rocsparse_gpsv_interleaved_alg](#rocsparse-types_8h_1ab3e4407bb8b94cb9315aa521420a4ae0)types that are used to solve pentadiagonal linear systems.*Values:*-
enumerator rocsparse_gpsv_interleaved_alg_default
[#](#_CPPv4N30rocsparse_gpsv_interleaved_alg38rocsparse_gpsv_interleaved_alg_defaultE) Default gpsv algorithm.


-
enumerator rocsparse_gpsv_interleaved_alg_qr
[#](#_CPPv4N30rocsparse_gpsv_interleaved_alg33rocsparse_gpsv_interleaved_alg_qrE) QR algorithm


-
enumerator rocsparse_gpsv_interleaved_alg_default

## rocsparse_check_spmat_stage[#](#rocsparse-check-spmat-stage)

-
enum rocsparse_check_spmat_stage
[#](#_CPPv427rocsparse_check_spmat_stage) List of check matrix stages.

This is a list of possible stages during check matrix computation. Typical order is

[rocsparse_check_spmat_stage_buffer_size](#rocsparse-types_8h_1a0b7629347a648269b10b4dd9dce70a53abc8ebc05a32fffffcc61b0673b3f82d9),[rocsparse_check_spmat_stage_compute](#rocsparse-types_8h_1a0b7629347a648269b10b4dd9dce70a53a638b6aab287a6b9177ed7740db0b2b95).*Values:*-
enumerator rocsparse_check_spmat_stage_buffer_size
[#](#_CPPv4N27rocsparse_check_spmat_stage39rocsparse_check_spmat_stage_buffer_sizeE) Returns the required buffer size.


-
enumerator rocsparse_check_spmat_stage_compute
[#](#_CPPv4N27rocsparse_check_spmat_stage35rocsparse_check_spmat_stage_computeE) Performs check.


-
enumerator rocsparse_check_spmat_stage_buffer_size

## rocsparse_spitsv_alg[#](#rocsparse-spitsv-alg)

-
enum rocsparse_spitsv_alg
[#](#_CPPv420rocsparse_spitsv_alg) List of SpITSV algorithms.

This is a list of supported

[rocsparse_spitsv_alg](#rocsparse-types_8h_1a66325da9fa02d6810a8a7aeea3115dba)types that are used to perform triangular solve.*Values:*-
enumerator rocsparse_spitsv_alg_default
[#](#_CPPv4N20rocsparse_spitsv_alg28rocsparse_spitsv_alg_defaultE) Default SpITSV algorithm for the given format.


-
enumerator rocsparse_spitsv_alg_default

## rocsparse_spitsv_stage[#](#rocsparse-spitsv-stage)

-
enum rocsparse_spitsv_stage
[#](#_CPPv422rocsparse_spitsv_stage) List of SpITSV stages.

This is a list of possible stages during SpITSV computation. Typical order is

[rocsparse_spitsv_stage_buffer_size](#rocsparse-types_8h_1ae307fdb92148195e71d428b7a62dea0cad5b8b6e106eb2c922a5c6f62851e4115),[rocsparse_spitsv_stage_preprocess](#rocsparse-types_8h_1ae307fdb92148195e71d428b7a62dea0cabf1b8852b5312a0762b3ff0a66cf578d),[rocsparse_spitsv_stage_compute](#rocsparse-types_8h_1ae307fdb92148195e71d428b7a62dea0ca955c9f450615646ed6b9f378c9693405).*Values:*-
enumerator rocsparse_spitsv_stage_buffer_size
[#](#_CPPv4N22rocsparse_spitsv_stage34rocsparse_spitsv_stage_buffer_sizeE) Returns the required buffer size.


-
enumerator rocsparse_spitsv_stage_preprocess
[#](#_CPPv4N22rocsparse_spitsv_stage33rocsparse_spitsv_stage_preprocessE) Preprocess data.


-
enumerator rocsparse_spitsv_stage_compute
[#](#_CPPv4N22rocsparse_spitsv_stage30rocsparse_spitsv_stage_computeE) Performs the actual SpITSV computation.


-
enumerator rocsparse_spitsv_stage_buffer_size
