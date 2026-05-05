---
title: "Sparse matrix functions &#8212; hipSOLVER 3.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/sparse-api/sparse.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:21:03.306882+00:00
content_hash: "9bbfb0f12c5f3cef"
---

# Sparse matrix functions[#](#sparse-matrix-functions)

Sparse matrix routines solve complex numerical linear algebra problems for sparse matrices.

## Combined factorization and linear-system solvers[#](#combined-factorization-and-linear-system-solvers)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverSpDcsrlsvchol([hipsolverSpHandle_t](types.html#_CPPv419hipsolverSpHandle_t)handle, int n, int nnzA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const double *csrVal, const int *csrRowPtr, const int *csrColInd, const double *b, double tolerance, int reorder, double *x, int *singularity)[#](#_CPPv422hipsolverSpDcsrlsvchol19hipsolverSpHandle_tiiK19hipsparseMatDescr_tPKdPKiPKiPKddiPdPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverSpScsrlsvchol([hipsolverSpHandle_t](types.html#_CPPv419hipsolverSpHandle_t)handle, int n, int nnzA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const float *csrVal, const int *csrRowPtr, const int *csrColInd, const float *b, float tolerance, int reorder, float *x, int *singularity)[#](#_CPPv422hipsolverSpScsrlsvchol19hipsolverSpHandle_tiiK19hipsparseMatDescr_tPKfPKiPKiPKffiPfPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverSpDcsrlsvcholHost([hipsolverSpHandle_t](types.html#_CPPv419hipsolverSpHandle_t)handle, int n, int nnzA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const double *csrVal, const int *csrRowPtr, const int *csrColInd, const double *b, double tolerance, int reorder, double *x, int *singularity)[#](#_CPPv426hipsolverSpDcsrlsvcholHost19hipsolverSpHandle_tiiK19hipsparseMatDescr_tPKdPKiPKiPKddiPdPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverSpScsrlsvcholHost([hipsolverSpHandle_t](types.html#_CPPv419hipsolverSpHandle_t)handle, int n, int nnzA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const float *csrVal, const int *csrRowPtr, const int *csrColInd, const float *b, float tolerance, int reorder, float *x, int *singularity)[#](#_CPPv426hipsolverSpScsrlsvcholHost19hipsolverSpHandle_tiiK19hipsparseMatDescr_tPKfPKiPKiPKffiPfPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverSpDcsrlsvqr([hipsolverSpHandle_t](types.html#_CPPv419hipsolverSpHandle_t)handle, int n, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const double *csrVal, const int *csrRowPts, const int *csrColInd, const double *b, double tolerance, int reorder, double *x, int *singularity)[#](#_CPPv420hipsolverSpDcsrlsvqr19hipsolverSpHandle_tiiK19hipsparseMatDescr_tPKdPKiPKiPKddiPdPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverSpScsrlsvqr([hipsolverSpHandle_t](types.html#_CPPv419hipsolverSpHandle_t)handle, int n, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const float *csrVal, const int *csrRowPts, const int *csrColInd, const float *b, double tolerance, int reorder, float *x, int *singularity)[#](#_CPPv420hipsolverSpScsrlsvqr19hipsolverSpHandle_tiiK19hipsparseMatDescr_tPKfPKiPKiPKfdiPfPi)
