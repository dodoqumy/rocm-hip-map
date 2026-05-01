---
title: "Bitwise reproducibility &#8212; rocSPARSE 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocSPARSE/en/latest/reference/reproducibility.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:16:40.553278+00:00
content_hash: "d07ee45b618a8c7b"
---

# Bitwise reproducibility[#](#bitwise-reproducibility)

Some routines do not produce deterministic results from run to run. This is typically the case when HIP atomics are used. This page catalogues the run-to-run reproducibility of each routine.

## Sparse level 1 functions[#](#sparse-level-1-functions)

## Sparse level 2 functions[#](#sparse-level-2-functions)

Function name |
yes |
no |
|---|---|---|
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |

The reproducibility of [ rocsparse_Xbsrmv()](level2.html#_CPPv416rocsparse_sbsrmv16rocsparse_handle19rocsparse_direction19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_infoPKfPKfPf),

[,](level2.html#_CPPv417rocsparse_sbsrxmv16rocsparse_handle19rocsparse_direction19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intPK13rocsparse_intPK13rocsparse_int13rocsparse_intPKfPKfPf)

`rocsparse_Xbsrxmv()`

[,](level2.html#_CPPv416rocsparse_scoomv16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intPKfPKfPf)

`rocsparse_Xcoomv()`

[,](level2.html#_CPPv416rocsparse_scsrmv16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoPKfPKfPf)

`rocsparse_Xcsrmv()`

[,](level2.html#_CPPv416rocsparse_sellmv16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_int13rocsparse_intPKfPKfPf)

`rocsparse_Xellmv()`

[, and](level2.html#_CPPv416rocsparse_shybmv16rocsparse_handle19rocsparse_operationPKfK19rocsparse_mat_descrK17rocsparse_hyb_matPKfPKfPf)

`rocsparse_Xhybmv()`

[is more complicated, depending on whether A is transposed or not. See the chart below to determine whether these routines are deterministic.](level2.html#_CPPv418rocsparse_sgebsrmv16rocsparse_handle19rocsparse_direction19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intPKfPKfPf)

`rocsparse_Xgebsrmv()`

Routine |
A non-transpose |
A transpose |
||
|---|---|---|---|---|
Yes |
No |
Yes |
No |
|
rocsparse_Xbsrmv |
x |
N/A |
N/A |
|
rocsparse_Xbsrxmv |
x |
N/A |
N/A |
|
rocsparse_Xcoomv |
x |
x |
||
rocsparse_Xcsrmv |
x |
x |
||
rocsparse_Xcsrmv (info != NULL) |
x |
x |
||
rocsparse_Xellmv |
x |
x |
||
rocsparse_Xhybmv |
x |
x |
||
rocsparse_Xgebsrmv |
x |
N/A |
N/A |

## Sparse level 3 functions[#](#sparse-level-3-functions)

Function name |
yes |
no |
|---|---|---|
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |

The reproducibility of [ rocsparse_Xbsrmm()](level3.html#_CPPv416rocsparse_sbsrmm16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_intPKf13rocsparse_intPKfPf13rocsparse_int),

[, and](level3.html#_CPPv418rocsparse_sgebsrmm16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intPKf13rocsparse_intPKfPf13rocsparse_int)

`rocsparse_Xgebsrmm()`

[is more complicated, depending on whether A is transposed or not. See the chart below to determine whether these routines are deterministic.](level3.html#_CPPv416rocsparse_scsrmm16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intPKf13rocsparse_intPKfPf13rocsparse_int)

`rocsparse_Xcsrmm()`

Routine |
A non-transpose |
A transpose |
||
|---|---|---|---|---|
Yes |
No |
Yes |
No |
|
rocsparse_Xbsrmm |
x |
N/A |
N/A |
|
rocsparse_Xgebsrmm |
x |
N/A |
N/A |
|
rocsparse_Xcsrmm |
x |
x |

## Sparse extra functions[#](#sparse-extra-functions)

Function name |
yes |
no |
|---|---|---|
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |

## Preconditioner functions[#](#preconditioner-functions)

Function name |
yes |
no |
|---|---|---|
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |

## Conversion functions[#](#conversion-functions)

Function name |
yes |
no |
|---|---|---|
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |

## Reordering functions[#](#reordering-functions)

## Utility functions[#](#utility-functions)

Function name |
yes |
no |
|---|---|---|
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |

## Sparse generic functions[#](#sparse-generic-functions)

Function name |
yes |
no |
|---|---|---|
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |
||
x |

The reproducibility of [ rocsparse_spmv()](generic.html#_CPPv414rocsparse_spmv16rocsparse_handle19rocsparse_operationPKv27rocsparse_const_spmat_descr27rocsparse_const_dnvec_descrPKvK21rocsparse_dnvec_descr18rocsparse_datatype18rocsparse_spmv_alg20rocsparse_spmv_stageP6size_tPv) and

[is more complicated because these generic routines support multiple sparse matrix formats and algorithms. See the chart below to determine whether a given algorithm is deterministic.](generic.html#_CPPv417rocsparse_v2_spmv16rocsparse_handle20rocsparse_spmv_descrPKv27rocsparse_const_spmat_descr27rocsparse_const_dnvec_descrPKv21rocsparse_dnvec_descr23rocsparse_v2_spmv_stage6size_tPvP15rocsparse_error)

`rocsparse_v2_spmv()`

Bit-wise reproducibility of SpMV/v2_SpMV |
||||
|---|---|---|---|---|
Algorithm |
A non-transpose |
A transpose |
||
Yes |
No |
Yes |
No |
|
rocsparse_spmv_alg_csr_stream |
x |
x |
||
rocsparse_spmv_alg_csr_rowsplit |
x |
x |
||
rocsparse_spmv_alg_csr_adaptive |
x |
x |
||
rocsparse_spmv_alg_csr_lrb |
x |
x |
||
rocsparse_spmv_alg_csr_stream (CSC FORMAT) |
x |
x |
||
rocsparse_spmv_alg_csr_rowsplit (CSC FORMAT) |
x |
x |
||
rocsparse_spmv_alg_csr_adaptive (CSC FORMAT) |
x |
x |
||
rocsparse_spmv_alg_csr_lrb (CSC FORMAT) |
x |
x |
||
rocsparse_spmv_alg_coo |
x |
x |
||
rocsparse_spmv_alg_coo_atomic |
x |
x |
||
rocsparse_spmv_alg_ell |
x |
N/A |
N/A |
|
rocsparse_spmv_alg_bsr |
x |
N/A |
N/A |
|
rocsparse_spmv_alg_sell |
x |
N/A |
N/A |

The reproducibility of [ rocsparse_spmm()](generic.html#_CPPv414rocsparse_spmm16rocsparse_handle19rocsparse_operation19rocsparse_operationPKv27rocsparse_const_spmat_descr27rocsparse_const_dnmat_descrPKvK21rocsparse_dnmat_descr18rocsparse_datatype18rocsparse_spmm_alg20rocsparse_spmm_stageP6size_tPv) is more complicated because this generic routine
supports multiple sparse matrix formats and algorithms. See the chart below to determine whether
a given algorithm is deterministic.

Bit-wise reproducibility of SpMM |
||||
|---|---|---|---|---|
Algorithm |
A non-transpose |
A transpose |
||
Yes |
No |
Yes |
No |
|
rocsparse_spmm_alg_csr |
x |
x |
||
rocsparse_spmm_alg_csr_row_split |
x |
x |
||
rocsparse_spmm_alg_csr_nnz_split |
x |
x |
||
rocsparse_spmm_alg_csr_merge_path |
x |
x |
||
rocsparse_spmm_alg_csr (CSC FORMAT) |
x |
x |
||
rocsparse_spmm_alg_csr_row_split (CSC FORMAT) |
x |
x |
||
rocsparse_spmm_alg_csr_nnz_split (CSC FORMAT) |
x |
x |
||
rocsparse_spmm_alg_csr_merge_path (CSC FORMAT) |
x |
x |
||
rocsparse_spmm_alg_coo_segmented |
x |
x |
||
rocsparse_spmm_alg_coo_atomic |
x |
x |
||
rocsparse_spmm_alg_coo_segmented_atomic |
x |
x |
||
rocsparse_spmm_alg_bell |
x |
N/A |
N/A |
|
rocsparse_spmm_alg_bsr |
x |
N/A |
N/A |
