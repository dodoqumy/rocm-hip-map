---
title: "Sparse reordering functions &#8212; hipSPARSE 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipSPARSE/en/latest/reference/reorder.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:09:20.231102+00:00
content_hash: "f22053488815ec8a"
---

# Sparse reordering functions[#](#sparse-reordering-functions)

This module contains all sparse reordering routines.

## hipsparseXcsrcolor()[#](#hipsparsexcsrcolor)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseScsrcolor([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const float *csrValA, const int *csrRowPtrA, const int *csrColIndA, const float *fractionToColor, int *ncolors, int *coloring, int *reordering,[hipsparseColorInfo_t](types.html#_CPPv420hipsparseColorInfo_t)info)[#](#_CPPv418hipsparseScsrcolor17hipsparseHandle_tiiK19hipsparseMatDescr_tPKfPKiPKiPKfPiPiPi20hipsparseColorInfo_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDcsrcolor([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const double *csrValA, const int *csrRowPtrA, const int *csrColIndA, const double *fractionToColor, int *ncolors, int *coloring, int *reordering,[hipsparseColorInfo_t](types.html#_CPPv420hipsparseColorInfo_t)info)[#](#_CPPv418hipsparseDcsrcolor17hipsparseHandle_tiiK19hipsparseMatDescr_tPKdPKiPKiPKdPiPiPi20hipsparseColorInfo_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCcsrcolor([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipComplex *csrValA, const int *csrRowPtrA, const int *csrColIndA, const float *fractionToColor, int *ncolors, int *coloring, int *reordering,[hipsparseColorInfo_t](types.html#_CPPv420hipsparseColorInfo_t)info)[#](#_CPPv418hipsparseCcsrcolor17hipsparseHandle_tiiK19hipsparseMatDescr_tPK10hipComplexPKiPKiPKfPiPiPi20hipsparseColorInfo_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZcsrcolor([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipDoubleComplex *csrValA, const int *csrRowPtrA, const int *csrColIndA, const double *fractionToColor, int *ncolors, int *coloring, int *reordering,[hipsparseColorInfo_t](types.html#_CPPv420hipsparseColorInfo_t)info)[#](#_CPPv418hipsparseZcsrcolor17hipsparseHandle_tiiK19hipsparseMatDescr_tPK16hipDoubleComplexPKiPKiPKdPiPiPi20hipsparseColorInfo_t) Coloring of the adjacency graph of the matrix \(A\) stored in the CSR format.

`hipsparseXcsrcolor`

performs the coloring of the undirected graph represented by the (symmetric) sparsity pattern of the matrix \(A\) stored in CSR format. Graph coloring is a way of coloring the nodes of a graph such that no two adjacent nodes are of the same color. The`fractionToColor`

is a parameter to only color a given percentage of the graph nodes, the remaining uncolored nodes receive distinct new colors. The optional`reordering`

array is a permutation array such that unknowns of the same color are grouped. The matrix \(A\) must be stored as a general matrix with a symmetric sparsity pattern, and if the matrix \(A\) is non-symmetric then the user is responsible to provide the symmetric part \(\frac{A+A^T}{2}\).- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of sparse matrix \(A\).**nnz**–**[in]**number of non-zero entries of sparse matrix \(A\).**descrA**–**[in]**sparse matrix descriptor.**csrValA**–**[in]**array of`nnz`

elements of the sparse CSR matrix.**csrRowPtrA**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csrColIndA**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**fractionToColor**–**[in]**fraction of nodes to be colored, which should be in the interval \([0.0,1.0]\), for example \(0.8\) implies that \(80\) percent of nodes will be colored.**ncolors**–**[out]**resulting number of distinct colors.**coloring**–**[out]**resulting mapping of colors.**reordering**–**[out]**optional resulting reordering permutation if`reordering`

is a non-null pointer.**info**–**[inout]**structure that holds the information collected during the coloring algorithm.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`nnz`

,`descrA`

,`csrValA`

,`csrRowPtrA`

,`csrColIndA`

,`fractionToColor`

,`ncolors`

,`coloring`

or`info`

pointer is invalid.
