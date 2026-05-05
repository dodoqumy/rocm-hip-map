---
title: "Sparse reordering functions &#8212; rocSPARSE 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocSPARSE/en/latest/reference/reorder.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:16:32.383489+00:00
content_hash: "e5191aa8e34571b8"
---

# Sparse reordering functions[#](#sparse-reordering-functions)

This module contains all sparse reordering routines.

The sparse reordering routines describe algorithms for reordering sparse matrices.
These routines do not support execution in a `hipGraph`

context.

## rocsparse_csrcolor()[#](#rocsparse-csrcolor)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_scsrcolor([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const float *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, const float *fraction_to_color,[rocsparse_int](types.html#_CPPv413rocsparse_int)*ncolors,[rocsparse_int](types.html#_CPPv413rocsparse_int)*coloring,[rocsparse_int](types.html#_CPPv413rocsparse_int)*reordering,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info)[#](#_CPPv419rocsparse_scsrcolor16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intPKfP13rocsparse_intP13rocsparse_intP13rocsparse_int18rocsparse_mat_info)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dcsrcolor([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const double *csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, const double *fraction_to_color,[rocsparse_int](types.html#_CPPv413rocsparse_int)*ncolors,[rocsparse_int](types.html#_CPPv413rocsparse_int)*coloring,[rocsparse_int](types.html#_CPPv413rocsparse_int)*reordering,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info)[#](#_CPPv419rocsparse_dcsrcolor16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKdPK13rocsparse_intPK13rocsparse_intPKdP13rocsparse_intP13rocsparse_intP13rocsparse_int18rocsparse_mat_info)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ccsrcolor([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_float_complex](types.html#_CPPv423rocsparse_float_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, const float *fraction_to_color,[rocsparse_int](types.html#_CPPv413rocsparse_int)*ncolors,[rocsparse_int](types.html#_CPPv413rocsparse_int)*coloring,[rocsparse_int](types.html#_CPPv413rocsparse_int)*reordering,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info)[#](#_CPPv419rocsparse_ccsrcolor16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK23rocsparse_float_complexPK13rocsparse_intPK13rocsparse_intPKfP13rocsparse_intP13rocsparse_intP13rocsparse_int18rocsparse_mat_info)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_zcsrcolor([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_int](types.html#_CPPv413rocsparse_int)m,[rocsparse_int](types.html#_CPPv413rocsparse_int)nnz, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr, const[rocsparse_double_complex](types.html#_CPPv424rocsparse_double_complex)*csr_val, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_row_ptr, const[rocsparse_int](types.html#_CPPv413rocsparse_int)*csr_col_ind, const double *fraction_to_color,[rocsparse_int](types.html#_CPPv413rocsparse_int)*ncolors,[rocsparse_int](types.html#_CPPv413rocsparse_int)*coloring,[rocsparse_int](types.html#_CPPv413rocsparse_int)*reordering,[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info)[#](#_CPPv419rocsparse_zcsrcolor16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK24rocsparse_double_complexPK13rocsparse_intPK13rocsparse_intPKdP13rocsparse_intP13rocsparse_intP13rocsparse_int18rocsparse_mat_info) Coloring of the adjacency graph of the matrix \(A\) stored in the CSR format.

`rocsparse_csrcolor`

performs the coloring of the undirected graph represented by the (symmetric) sparsity pattern of the matrix \(A\) stored in CSR format. Graph coloring is a way of coloring the nodes of a graph such that no two adjacent nodes are of the same color. The`fraction_to_color`

is a parameter to only color a given percentage of the graph nodes, the remaining uncolored nodes receive distinct new colors. The optional`reordering`

array is a permutation array such that unknowns of the same color are grouped. The matrix \(A\) must be stored as a general matrix with a symmetric sparsity pattern, and if the matrix \(A\) is non-symmetric then the user is responsible to provide the symmetric part \(\frac{A+A^T}{2}\).Note

This function is blocking with respect to the host.

Note

This routine does not support execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**m**–**[in]**number of rows of sparse matrix \(A\).**nnz**–**[in]**number of non-zero entries of sparse matrix \(A\).**descr**–**[in]**sparse matrix descriptor.**csr_val**–**[in]**array of`nnz`

elements of the sparse CSR matrix.**csr_row_ptr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csr_col_ind**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**fraction_to_color**–**[in]**fraction of nodes to be colored, which should be in the interval [0.0,1.0], for example 0.8 implies that 80 percent of nodes will be colored.**ncolors**–**[out]**resulting number of distinct colors.**coloring**–**[out]**resulting mapping of colors.**reordering**–**[out]**optional resulting reordering permutation if`reordering`

is a non-null pointer.**info**–**[inout]**structure that holds the information collected during the coloring algorithm.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**– the library context was not initialized.**rocsparse_status_invalid_size**–`m`

or`nnz`

is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`csr_val`

,`csr_row_ptr`

,`csr_col_ind`

,`fraction_to_color`

,`ncolors`

,`coloring`

or`info`

pointer is invalid.
