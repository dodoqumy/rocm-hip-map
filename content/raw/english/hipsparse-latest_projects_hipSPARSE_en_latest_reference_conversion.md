---
title: "Sparse conversion functions &#8212; hipSPARSE 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipSPARSE/en/latest/reference/conversion.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:09:48.700319+00:00
content_hash: "3b048fad53b2b09b"
---

# Sparse conversion functions[#](#sparse-conversion-functions)

This module contains all sparse conversion routines.

The sparse conversion routines describe operations performed on a matrix in sparse format to obtain a matrix in a different sparse format.

## hipsparseXnnz()[#](#hipsparsexnnz)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSnnz([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const float *A, int lda, int *nnzPerRowColumn, int *nnzTotalDevHostPtr)[#](#_CPPv413hipsparseSnnz17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPKfiPiPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDnnz([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const double *A, int lda, int *nnzPerRowColumn, int *nnzTotalDevHostPtr)[#](#_CPPv413hipsparseDnnz17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPKdiPiPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCnnz([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipComplex *A, int lda, int *nnzPerRowColumn, int *nnzTotalDevHostPtr)[#](#_CPPv413hipsparseCnnz17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPK10hipComplexiPiPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZnnz([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipDoubleComplex *A, int lda, int *nnzPerRowColumn, int *nnzTotalDevHostPtr)[#](#_CPPv413hipsparseZnnz17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPK16hipDoubleComplexiPiPi) `hipsparseXnnz`

computes the number of nonzero elements per row or column and the total number of nonzero elements in a dense matrix.For example, given the dense matrix:

\[\begin{split} \begin{bmatrix} 1 & 0 & 0 & 2 \\ 3 & 4 & 0 & 0 \\ 5 & 0 & 6 & 7 \end{bmatrix} \end{split}\]then using

`dirA`

==[HIPSPARSE_DIRECTION_ROW](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59ae8589abecf2fbfb4b6307fd9dacd9e55)results in:\[\begin{split} \begin{align} \text{nnzPerRowColumn} &= \begin{bmatrix} 2 & 2 & 3 \end{bmatrix} \\ \text{nnzTotalDevHostPtr} &= 7 \end{align} \end{split}\]while using

`dirA`

==[HIPSPARSE_DIRECTION_COLUMN](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59a32e23f292b2377f6e60bdc90274c796c)results in:\[\begin{split} \begin{align} \text{nnzPerRowColumn} &= \begin{bmatrix} 3 & 1 & 1 & 2 \end{bmatrix} \\ \text{nnzTotalDevHostPtr} &= 7 \end{align} \end{split}\]The array

`nnzPerRowColumn`

must be allocated by the user before calling`hipsparseXnnz`

and has length equal to`m`

if`dirA`

==[HIPSPARSE_DIRECTION_ROW](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59ae8589abecf2fbfb4b6307fd9dacd9e55)or`n`

if`dirA`

==[HIPSPARSE_DIRECTION_COLUMN](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59a32e23f292b2377f6e60bdc90274c796c).For a complete code example on its usage, see the example found with

[hipsparseSdense2csr()](#hipsparse__dense2csr_8h_1a50644fe63a8ff54bc39e7393286b050f).Note

As indicated,

`nnzTotalDevHostPtr`

can point either to host or device memory. This is controlled by setting the pointer mode. See[hipsparseSetPointerMode()](auxiliary.html#hipsparse-auxiliary_8h_1a7d876174f77e1f8f816781af1c3c667c).Note

The routine does support asynchronous execution if the pointer mode is set to device.

- Parameters:
**handle**–**[in]**handle to the rocsparse library context queue.**dirA**–**[in]**direction that specified whether to count nonzero elements by[HIPSPARSE_DIRECTION_ROW](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59ae8589abecf2fbfb4b6307fd9dacd9e55)or by[HIPSPARSE_DIRECTION_COLUMN](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59a32e23f292b2377f6e60bdc90274c796c).**m**–**[in]**number of rows of the dense matrix`A`

.**n**–**[in]**number of columns of the dense matrix`A`

.**descrA**–**[in]**the descriptor of the dense matrix`A`

.**A**–**[in]**array of dimensions (`lda`

,`n`

)**lda**–**[in]**leading dimension of dense array`A`

.**nnzPerRowColumn**–**[out]**array of size`m`

or`n`

containing the number of nonzero elements per row or column, respectively.**nnzTotalDevHostPtr**–**[out]**total number of nonzero elements in device or host memory.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`lda`

,`A`

or`nnzPerRowColumn`

or`nnzTotalDevHostPtr`

pointer is invalid.



## hipsparseXdense2csr()[#](#hipsparsexdense2csr)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSdense2csr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descr, const float *A, int ld, const int *nnzPerRow, float *csrVal, int *csrRowPtr, int *csrColInd)[#](#_CPPv419hipsparseSdense2csr17hipsparseHandle_tiiK19hipsparseMatDescr_tPKfiPKiPfPiPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDdense2csr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descr, const double *A, int ld, const int *nnzPerRow, double *csrVal, int *csrRowPtr, int *csrColInd)[#](#_CPPv419hipsparseDdense2csr17hipsparseHandle_tiiK19hipsparseMatDescr_tPKdiPKiPdPiPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCdense2csr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descr, const hipComplex *A, int ld, const int *nnzPerRow, hipComplex *csrVal, int *csrRowPtr, int *csrColInd)[#](#_CPPv419hipsparseCdense2csr17hipsparseHandle_tiiK19hipsparseMatDescr_tPK10hipComplexiPKiP10hipComplexPiPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZdense2csr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descr, const hipDoubleComplex *A, int ld, const int *nnzPerRow, hipDoubleComplex *csrVal, int *csrRowPtr, int *csrColInd)[#](#_CPPv419hipsparseZdense2csr17hipsparseHandle_tiiK19hipsparseMatDescr_tPK16hipDoubleComplexiPKiP16hipDoubleComplexPiPi) `hipsparseXdense2csr`

converts the matrix A in dense format into a sparse matrix in CSR format.Given a dense, column ordered, matrix

`A`

with leading dimension`ld`

where`ld>=m`

,`hipsparseXdense2csr`

converts the matrix to a sparse CSR format matrix. All the parameters are assumed to have been pre-allocated by the user and the arrays are filled in based on number of nonzeros per row, which can be pre-computed with[hipsparseXnnz()](#hipsparse__nnz_8h_1a939d35fea53d730267afe6abda38fcbf). The desired index base in the output CSR matrix is set in the[hipsparseMatDescr_t](types.html#hipsparse-types_8h_1a4c2f3ad3f2057bffb1adf6a8256537b9). See[hipsparseSetMatIndexBase()](auxiliary.html#hipsparse-auxiliary_8h_1a3c81b4bd7b1e9bb04a63a620f51dc2a8).As an example, if using index base zero (i.e. the default) and the dense matrix:

\[\begin{split} \begin{bmatrix} 1 & 0 & 0 & 2 \\ 3 & 4 & 0 & 0 \\ 5 & 0 & 6 & 7 \end{bmatrix} \end{split}\]The conversion results in the CSR arrays:

\[\begin{split} \begin{align} \text{csrRowPtr} &= \begin{bmatrix} 0 & 2 & 4 & 7 \end{bmatrix} \\ \text{csrColInd} &= \begin{bmatrix} 0 & 3 & 0 & 1 & 0 & 2 & 3 \end{bmatrix} \\ \text{csrVal} &= \begin{bmatrix} 1 & 2 & 3 & 4 & 5 & 6 & 7 \end{bmatrix} \\ \end{align} \end{split}\]**Example**int main(int argc, char* argv[]) { // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // Matrix descriptor hipsparseMatDescr_t descr; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&descr)); // Dense matrix in column order // 1 2 0 3 0 // A = 0 4 5 0 0 // 6 0 0 7 8 float hdense_A[15] = { 1.0f, 0.0f, 6.0f, 2.0f, 4.0f, 0.0f, 0.0f, 5.0f, 0.0f, 3.0f, 0.0f, 7.0f, 0.0f, 0.0f, 8.0f}; int m = 3; int n = 5; hipsparseDirection_t dir = HIPSPARSE_DIRECTION_ROW; float* ddense_A = nullptr; HIP_CHECK(hipMalloc((void**)&ddense_A, sizeof(float) * m * n)); HIP_CHECK(hipMemcpy(ddense_A, hdense_A, sizeof(float) * m * n, hipMemcpyHostToDevice)); // Allocate memory for the nnz_per_row_columns array int* dnnz_per_row; HIP_CHECK(hipMalloc((void**)&dnnz_per_row, sizeof(int) * m)); int nnz_A; HIPSPARSE_CHECK(hipsparseSnnz(handle, dir, m, n, descr, ddense_A, m, dnnz_per_row, &nnz_A)); // Allocate sparse CSR matrix int* dcsrRowPtr = nullptr; int* dcsrColInd = nullptr; float* dcsrVal = nullptr; HIP_CHECK(hipMalloc((void**)&dcsrRowPtr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&dcsrColInd, sizeof(int) * nnz_A)); HIP_CHECK(hipMalloc((void**)&dcsrVal, sizeof(float) * nnz_A)); HIPSPARSE_CHECK(hipsparseSdense2csr( handle, m, n, descr, ddense_A, m, dnnz_per_row, dcsrVal, dcsrRowPtr, dcsrColInd)); HIP_CHECK(hipFree(dcsrRowPtr)); HIP_CHECK(hipFree(dcsrColInd)); HIP_CHECK(hipFree(dcsrVal)); HIP_CHECK(hipFree(dnnz_per_row)); HIP_CHECK(hipFree(ddense_A)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(descr)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); return 0; }


Note

It is executed asynchronously with respect to the host and may return control to the application on the host before the entire result is ready.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the dense matrix`A`

.**n**–**[in]**number of columns of the dense matrix`A`

.**descr**–**[in]**the descriptor of the dense matrix`A`

, the supported matrix type is[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)and also any valid value of the[hipsparseIndexBase_t](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4).**A**–**[in]**array of dimensions (`ld`

,`n`

)**ld**–**[in]**leading dimension of dense array`A`

.**nnzPerRow**–**[in]**array of size`n`

containing the number of non-zero elements per row.**csrVal**–**[out]**array of nnz ( =`csrRowPtr`

[m] -`csrRowPtr`

[0] ) nonzero elements of matrix`A`

.**csrRowPtr**–**[out]**integer array of`m+1`

elements that contains the start of every row and the end of the last row plus one.**csrColInd**–**[out]**integer array of nnz ( =`csrRowPtr`

[m] -`csrRowPtr`

[0] ) column indices of the non-zero elements of matrix`A`

.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`ld`

,`A`

,`nnzPerRow`

,`csrVal`

`csrRowPtr`

or`csrColInd`

pointer is invalid.



## hipsparseXpruneDense2csr_bufferSize()[#](#hipsparsexprunedense2csr-buffersize)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpruneDense2csr_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const float *A, int lda, const float *threshold, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descr, const float *csrVal, const int *csrRowPtr, const int *csrColInd, size_t *pBufferSizeInBytes)[#](#_CPPv435hipsparseSpruneDense2csr_bufferSize17hipsparseHandle_tiiPKfiPKfK19hipsparseMatDescr_tPKfPKiPKiP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDpruneDense2csr_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const double *A, int lda, const double *threshold, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descr, const double *csrVal, const int *csrRowPtr, const int *csrColInd, size_t *pBufferSizeInBytes)[#](#_CPPv435hipsparseDpruneDense2csr_bufferSize17hipsparseHandle_tiiPKdiPKdK19hipsparseMatDescr_tPKdPKiPKiP6size_t) `hipsparseXpruneDense2csr_bufferSize`

computes the the size of the user allocated temporary storage buffer used when converting a dense matrix to a pruned CSR matrix.Specifically given an input dense column ordered matrix A, with leading dimension

`lda`

where`lda>=m`

, the resulting pruned sparse CSR matrix C is computed using:\[ |C(i,j)| = A(i, j) \text{ if |A(i, j)| > threshold} \]The first step in this conversion is to determine the required user allocated buffer size using

`hipsparseXpruneDense2csr_bufferSize()`

that will be passed to the subsequent steps of the conversion. Once the buffer size has been determined the user must allocate it. This user allocated buffer is then passed to[hipsparseXpruneDense2csrNnz()](#hipsparse__prune__dense2csr_8h_1a7b6dbd23c7b0154b20f5fa6a9a991bb3)and[hipsparseXpruneDense2csr()](#hipsparse__prune__dense2csr_8h_1ae059ad9fdc8ecd2ce0078c5f246b6222)to complete the conversion. The user is responsible to then free the buffer once the conversion has been completed.See

[hipsparseSpruneDense2csr()](#hipsparse__prune__dense2csr_8h_1ae059ad9fdc8ecd2ce0078c5f246b6222)for a full code example.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the dense matrix`A`

.**n**–**[in]**number of columns of the dense matrix`A`

.**A**–**[in]**array of dimensions (`lda`

,`n`

)**lda**–**[in]**leading dimension of dense array`A`

.**threshold**–**[in]**pointer to the pruning non-negative threshold which can exist in either host or device memory.**descr**–**[in]**the descriptor of the dense matrix`A`

, the supported matrix type is[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)and also any valid value of the[hipsparseIndexBase_t](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4).**csrVal**–**[in]**array of nnz ( =`csrRowPtr`

[m] -`csrRowPtr`

[0] ) nonzero elements of matrix`A`

.**csrRowPtr**–**[in]**integer array of`m+1`

elements that contains the start of every row and the end of the last row plus one.**csrColInd**–**[in]**integer array of nnz ( =`csrRowPtr`

[m] -`csrRowPtr`

[0] ) column indices of the non-zero elements of matrix`A`

.**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer required by[hipsparseSpruneDense2csrNnz()](#hipsparse__prune__dense2csr_8h_1a7b6dbd23c7b0154b20f5fa6a9a991bb3),[hipsparseDpruneDense2csrNnz()](#hipsparse__prune__dense2csr_8h_1a7b367a71c107eff5c3ed5b9c69eff66e),[hipsparseSpruneDense2csr()](#hipsparse__prune__dense2csr_8h_1ae059ad9fdc8ecd2ce0078c5f246b6222)and[hipsparseDpruneDense2csr()](#hipsparse__prune__dense2csr_8h_1a83d440868c4a6321c1a4448dd40f8e67).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

or`pBufferSizeInBytes`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.



## hipsparseXpruneDense2csr_bufferSizeExt()[#](#hipsparsexprunedense2csr-buffersizeext)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpruneDense2csr_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const float *A, int lda, const float *threshold, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descr, const float *csrVal, const int *csrRowPtr, const int *csrColInd, size_t *pBufferSizeInBytes)[#](#_CPPv438hipsparseSpruneDense2csr_bufferSizeExt17hipsparseHandle_tiiPKfiPKfK19hipsparseMatDescr_tPKfPKiPKiP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDpruneDense2csr_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const double *A, int lda, const double *threshold, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descr, const double *csrVal, const int *csrRowPtr, const int *csrColInd, size_t *pBufferSizeInBytes)[#](#_CPPv438hipsparseDpruneDense2csr_bufferSizeExt17hipsparseHandle_tiiPKdiPKdK19hipsparseMatDescr_tPKdPKiPKiP6size_t) `hipsparseXpruneDense2csr_bufferSize`

computes the the size of the user allocated temporary storage buffer used when converting a dense matrix to a pruned CSR matrix.Specifically given an input dense column ordered matrix A, with leading dimension

`lda`

where`lda>=m`

, the resulting pruned sparse CSR matrix C is computed using:\[ |C(i,j)| = A(i, j) \text{ if |A(i, j)| > threshold} \]The first step in this conversion is to determine the required user allocated buffer size using

`hipsparseXpruneDense2csr_bufferSize()`

that will be passed to the subsequent steps of the conversion. Once the buffer size has been determined the user must allocate it. This user allocated buffer is then passed to[hipsparseXpruneDense2csrNnz()](#hipsparse__prune__dense2csr_8h_1a7b6dbd23c7b0154b20f5fa6a9a991bb3)and[hipsparseXpruneDense2csr()](#hipsparse__prune__dense2csr_8h_1ae059ad9fdc8ecd2ce0078c5f246b6222)to complete the conversion. The user is responsible to then free the buffer once the conversion has been completed.See

[hipsparseSpruneDense2csr()](#hipsparse__prune__dense2csr_8h_1ae059ad9fdc8ecd2ce0078c5f246b6222)for a full code example.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the dense matrix`A`

.**n**–**[in]**number of columns of the dense matrix`A`

.**A**–**[in]**array of dimensions (`lda`

,`n`

)**lda**–**[in]**leading dimension of dense array`A`

.**threshold**–**[in]**pointer to the pruning non-negative threshold which can exist in either host or device memory.**descr**–**[in]**the descriptor of the dense matrix`A`

, the supported matrix type is[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)and also any valid value of the[hipsparseIndexBase_t](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4).**csrVal**–**[in]**array of nnz ( =`csrRowPtr`

[m] -`csrRowPtr`

[0] ) nonzero elements of matrix`A`

.**csrRowPtr**–**[in]**integer array of`m+1`

elements that contains the start of every row and the end of the last row plus one.**csrColInd**–**[in]**integer array of nnz ( =`csrRowPtr`

[m] -`csrRowPtr`

[0] ) column indices of the non-zero elements of matrix`A`

.**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer required by[hipsparseSpruneDense2csrNnz()](#hipsparse__prune__dense2csr_8h_1a7b6dbd23c7b0154b20f5fa6a9a991bb3),[hipsparseDpruneDense2csrNnz()](#hipsparse__prune__dense2csr_8h_1a7b367a71c107eff5c3ed5b9c69eff66e),[hipsparseSpruneDense2csr()](#hipsparse__prune__dense2csr_8h_1ae059ad9fdc8ecd2ce0078c5f246b6222)and[hipsparseDpruneDense2csr()](#hipsparse__prune__dense2csr_8h_1a83d440868c4a6321c1a4448dd40f8e67).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

or`pBufferSizeInBytes`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.



## hipsparseXpruneDense2csrNnz()[#](#hipsparsexprunedense2csrnnz)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpruneDense2csrNnz([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const float *A, int lda, const float *threshold, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descr, int *csrRowPtr, int *nnzTotalDevHostPtr, void *buffer)[#](#_CPPv427hipsparseSpruneDense2csrNnz17hipsparseHandle_tiiPKfiPKfK19hipsparseMatDescr_tPiPiPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDpruneDense2csrNnz([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const double *A, int lda, const double *threshold, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descr, int *csrRowPtr, int *nnzTotalDevHostPtr, void *buffer)[#](#_CPPv427hipsparseDpruneDense2csrNnz17hipsparseHandle_tiiPKdiPKdK19hipsparseMatDescr_tPiPiPv) `hipsparseXpruneDense2csrNnz`

function computes the number of nonzero elements per row and the total number of nonzero elements in a dense matrix once the elements less than the (non-negative) threshold are pruned from the matrix.Specifically given an input dense column ordered matrix A, with leading dimension

`lda`

where`lda>=m`

, the resulting pruned sparse CSR matrix C is computed using:\[ |C(i,j)| = A(i, j) \text{ if |A(i, j)| > threshold} \]First the user must determine the size of the required temporary buffer using the routine

[hipsparseXpruneDense2csr_bufferSize()](#hipsparse__prune__dense2csr_8h_1ab4ca9017e6aeebcf2f6cbba0b14c7c5f)and then allocate it. Next the user allocates`csrRowPtr`

with size`m+1`

. Then the passes both the temporary storage buffer as well as`csrRowPtr`

to`hipsparseXpruneDense2csrNnz`

in order to determine the total number of non-zeros that will exist in the sparse CSR matrix C (after pruning has been performed on A) as well as fill the output CSR row pointer array`csrRowPtr`

.For example, given the dense matrix:

\[\begin{split} \begin{bmatrix} 6 & 2 & 3 & 7 \\ 5 & 6 & 7 & 8 \\ 5 & 4 & 8 & 1 \end{bmatrix} \end{split}\]and the

`threshold`

value 5, the resulting matrix after pruning is:\[\begin{split} \begin{bmatrix} 6 & 0 & 0 & 7 \\ 0 & 6 & 7 & 8 \\ 0 & 0 & 8 & 0 \end{bmatrix} \end{split}\]and corresponding row pointer array and non-zero count:

\[\begin{split} \begin{align} \text{csrRowPtr} &= \begin{bmatrix} 0 & 2 & 5 & 6 \end{bmatrix} \\ \text{nnzTotalDevHostPtr} &= 6 \end{align} \end{split}\]The above example assumes a zero index base for the output CSR matrix. We can set the desired index base in the output CSR matrix by setting it in the

[hipsparseMatDescr_t](types.html#hipsparse-types_8h_1a4c2f3ad3f2057bffb1adf6a8256537b9). See[hipsparseSetMatIndexBase()](auxiliary.html#hipsparse-auxiliary_8h_1a3c81b4bd7b1e9bb04a63a620f51dc2a8).For a full code example on how to use this routine, see

[hipsparseSpruneDense2csr()](#hipsparse__prune__dense2csr_8h_1ae059ad9fdc8ecd2ce0078c5f246b6222).Note

The routine does support asynchronous execution if the pointer mode is set to device.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the dense matrix`A`

.**n**–**[in]**number of columns of the dense matrix`A`

.**A**–**[in]**array of dimensions (`lda`

,`n`

)**lda**–**[in]**leading dimension of dense array`A`

.**threshold**–**[in]**pointer to the pruning non-negative threshold which can exist in either host or device memory.**descr**–**[in]**the descriptor of the dense matrix`A`

.**csrRowPtr**–**[out]**integer array of`m+1`

elements that contains the start of every row and the end of the last row plus one.**nnzTotalDevHostPtr**–**[out]**total number of nonzero elements in device or host memory.**buffer**–**[out]**buffer allocated by the user whose size is determined by calling[hipsparseXpruneDense2csr_bufferSize()](#hipsparse__prune__dense2csr_8h_1ab4ca9017e6aeebcf2f6cbba0b14c7c5f)or[hipsparseXpruneDense2csr_bufferSizeExt()](#hipsparse__prune__dense2csr_8h_1adc3f583364ae38063db8d5ccb4298434).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`lda`

,`A`

,`threshold`

,`descr`

,`csrRowPtr`

`nnzTotalDevHostPtr`

or`buffer`

pointer is invalid.



## hipsparseXpruneDense2csr()[#](#hipsparsexprunedense2csr)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpruneDense2csr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const float *A, int lda, const float *threshold, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descr, float *csrVal, const int *csrRowPtr, int *csrColInd, void *buffer)[#](#_CPPv424hipsparseSpruneDense2csr17hipsparseHandle_tiiPKfiPKfK19hipsparseMatDescr_tPfPKiPiPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDpruneDense2csr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const double *A, int lda, const double *threshold, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descr, double *csrVal, const int *csrRowPtr, int *csrColInd, void *buffer)[#](#_CPPv424hipsparseDpruneDense2csr17hipsparseHandle_tiiPKdiPKdK19hipsparseMatDescr_tPdPKiPiPv) `hipsparseXpruneDense2csr`

converts the matrix A in dense format into a sparse matrix in CSR format while pruning values that are less than the (non-negative) threshold. All the parameters are assumed to have been pre-allocated by the user.Specifically given an input dense column ordered matrix A, with leading dimension

`lda`

where`lda>=m`

, the resulting pruned sparse CSR matrix C is computed using:\[ |C(i,j)| = A(i, j) \text{ if |A(i, j)| > threshold} \]The user first calls

[hipsparseXpruneDense2csr_bufferSize()](#hipsparse__prune__dense2csr_8h_1ab4ca9017e6aeebcf2f6cbba0b14c7c5f)to determine the size of the required user allocate temporary storage buffer. The user then allocates this buffer. Next, the user allocates`csrRowPtr`

to have`m+1`

elements and then calls[hipsparseXpruneDense2csrNnz()](#hipsparse__prune__dense2csr_8h_1a7b6dbd23c7b0154b20f5fa6a9a991bb3)which fills in the`csrRowPtr`

array and stores the number of elements that are larger than the pruning`threshold`

in`nnzTotalDevHostPtr`

. The user then allocates`csrColInd`

and`csrVal`

to have size`nnzTotalDevHostPtr`

and completes the conversion by calling`hipsparseXpruneDense2csr()`

.For example, performing these steps with the dense input matrix A:

\[\begin{split} \begin{bmatrix} 6 & 2 & 3 & 7 \\ 5 & 6 & 7 & 8 \\ 5 & 4 & 8 & 1 \end{bmatrix} \end{split}\]and the

`threshold`

value 5, results in the pruned matrix C:\[\begin{split} \begin{bmatrix} 6 & 0 & 0 & 7 \\ 0 & 6 & 7 & 8 \\ 0 & 0 & 8 & 0 \end{bmatrix} \end{split}\]and corresponding CSR row, column, and values arrays:

\[\begin{split} \begin{align} \text{csrRowPtr} &= \begin{bmatrix} 0 & 2 & 5 & 6 \end{bmatrix} \\ \text{csrColInd} &= \begin{bmatrix} 0 & 3 & 1 & 2 & 3 & 2 \end{bmatrix} \\ \text{csrVal} &= \begin{bmatrix} 6 & 7 & 6 & 7 & 8 & 8 \end{bmatrix} \\ \end{align} \end{split}\]**Example**int main(int argc, char* argv[]) { // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // Matrix descriptor hipsparseMatDescr_t descr; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&descr)); // Dense matrix in column order // 1 2 0 3 0 // A = 0 4 5 0 0 // 6 0 0 7 8 float hdense_A[15] = { 1.0f, 0.0f, 6.0f, 2.0f, 4.0f, 0.0f, 0.0f, 5.0f, 0.0f, 3.0f, 0.0f, 7.0f, 0.0f, 0.0f, 8.0f}; int m = 3; int n = 5; int lda = m; float threshold = 4.0f; float* ddense_A = nullptr; HIP_CHECK(hipMalloc((void**)&ddense_A, sizeof(float) * lda * n)); HIP_CHECK(hipMemcpy(ddense_A, hdense_A, sizeof(float) * lda * n, hipMemcpyHostToDevice)); // Allocate sparse CSR matrix int* dcsrRowPtr = nullptr; HIP_CHECK(hipMalloc((void**)&dcsrRowPtr, sizeof(int) * (m + 1))); size_t bufferSize; HIPSPARSE_CHECK(hipsparseSpruneDense2csr_bufferSize( handle, m, n, ddense_A, lda, &threshold, descr, nullptr, dcsrRowPtr, nullptr, &bufferSize)); void* dbuffer = nullptr; HIP_CHECK(hipMalloc((void**)&dbuffer, bufferSize)); int nnz_A; HIPSPARSE_CHECK(hipsparseSpruneDense2csrNnz( handle, m, n, ddense_A, lda, &threshold, descr, dcsrRowPtr, &nnz_A, dbuffer)); int* dcsrColInd = nullptr; float* dcsrVal = nullptr; HIP_CHECK(hipMalloc((void**)&dcsrColInd, sizeof(int) * nnz_A)); HIP_CHECK(hipMalloc((void**)&dcsrVal, sizeof(float) * nnz_A)); HIPSPARSE_CHECK(hipsparseSpruneDense2csr( handle, m, n, ddense_A, lda, &threshold, descr, dcsrVal, dcsrRowPtr, dcsrColInd, dbuffer)); HIP_CHECK(hipFree(dcsrRowPtr)); HIP_CHECK(hipFree(dcsrColInd)); HIP_CHECK(hipFree(dcsrVal)); HIP_CHECK(hipFree(ddense_A)); HIP_CHECK(hipFree(dbuffer)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(descr)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); return 0; }


Note

The routine

`hipsparseXpruneDense2csr()`

is executed asynchronously with respect to the host and may return control to the application on the host before the entire result is ready.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the dense matrix`A`

.**n**–**[in]**number of columns of the dense matrix`A`

.**A**–**[in]**array of dimensions (`lda`

,`n`

)**lda**–**[in]**leading dimension of dense array`A`

.**threshold**–**[in]**pointer to the non-negative pruning threshold which can exist in either host or device memory.**descr**–**[in]**the descriptor of the dense matrix`A`

, the supported matrix type is[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)and also any valid value of the[hipsparseIndexBase_t](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4).**csrVal**–**[out]**array of nnz ( =`csrRowPtr`

[m] -`csrRowPtr`

[0] ) nonzero elements of matrix`A`

.**csrRowPtr**–**[in]**integer array of`m+1`

elements that contains the start of every row and the end of the last row plus one.**csrColInd**–**[out]**integer array of nnz ( =`csrRowPtr`

[m] -`csrRowPtr`

[0] ) column indices of the non-zero elements of matrix`A`

.**buffer**–**[in]**temporary storage buffer allocated by the user, size is returned by[hipsparseXpruneDense2csr_bufferSize()](#hipsparse__prune__dense2csr_8h_1ab4ca9017e6aeebcf2f6cbba0b14c7c5f)or[hipsparseXpruneDense2csr_bufferSizeExt()](#hipsparse__prune__dense2csr_8h_1adc3f583364ae38063db8d5ccb4298434).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`lda`

,`A`

,`descr`

,`threshold`

,`csrVal`

`csrRowPtr`

,`csrColInd`

,`buffer`

pointer is invalid.



## hipsparseXpruneDense2csrByPercentage_bufferSize()[#](#hipsparsexprunedense2csrbypercentage-buffersize)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpruneDense2csrByPercentage_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const float *A, int lda, float percentage, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descr, const float *csrVal, const int *csrRowPtr, const int *csrColInd,[pruneInfo_t](types.html#_CPPv411pruneInfo_t)info, size_t *pBufferSizeInBytes)[#](#_CPPv447hipsparseSpruneDense2csrByPercentage_bufferSize17hipsparseHandle_tiiPKfifK19hipsparseMatDescr_tPKfPKiPKi11pruneInfo_tP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDpruneDense2csrByPercentage_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const double *A, int lda, double percentage, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descr, const double *csrVal, const int *csrRowPtr, const int *csrColInd,[pruneInfo_t](types.html#_CPPv411pruneInfo_t)info, size_t *pBufferSizeInBytes)[#](#_CPPv447hipsparseDpruneDense2csrByPercentage_bufferSize17hipsparseHandle_tiiPKdidK19hipsparseMatDescr_tPKdPKiPKi11pruneInfo_tP6size_t) `hipsparseXpruneDense2csrByPercentage_bufferSize`

computes the size of the user allocated temporary storage buffer used when converting a dense matrix to a pruned CSR matrix where the pruning is done based on a percantage.When converting and pruning a dense matrix A to a CSR matrix by percentage the following steps are performed. First the user calls

`hipsparseXpruneDense2csrByPercentage_bufferSize`

which determines the size of the temporary storage buffer. Once determined, this buffer must be allocated by the user. Next the user allocates the`csrRowPtr`

array to have`m+1`

elements and calls[hipsparseXpruneDense2csrNnzByPercentage()](#hipsparse__prune__dense2csr__by__percentage_8h_1afa03216a28f5bf36e3bce51950b4a140). Finally the user finishes the conversion by allocating the`csrColInd`

and`csrVal`

arrays (whose size is determined by the value at`nnzTotalDevHostPtr`

) and calling[hipsparseXpruneDense2csrByPercentage()](#hipsparse__prune__dense2csr__by__percentage_8h_1ace1c36935b6211e53445f81331cc190b).The pruning by percentage works by first sorting the absolute values of the dense matrix

`A`

. We then determine a position in this sorted array by\[\begin{split} pos = ceil(m \cdot n \cdot (percentage/100)) - 1 \\ pos = \min(pos, m \cdot n-1) \\ pos = \max(pos, 0) \\ threshold = sorted_A[pos] \end{split}\]Once we have this threshold we prune values in the dense matrix

`A`

as in[hipsparseXpruneDense2csr()](#hipsparse__prune__dense2csr_8h_1ae059ad9fdc8ecd2ce0078c5f246b6222).Note

It is executed asynchronously with respect to the host and may return control to the application on the host before the entire result is ready.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the dense matrix`A`

.**n**–**[in]**number of columns of the dense matrix`A`

.**A**–**[in]**array of dimensions (`lda`

,`n`

)**lda**–**[in]**leading dimension of dense array`A`

.**percentage**–**[in]**`percentage>=0`

and`percentage<=100`

.**descr**–**[in]**the descriptor of the dense matrix`A`

, the supported matrix type is[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)and also any valid value of the[hipsparseIndexBase_t](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4).**csrVal**–**[in]**array of nnz ( =`csrRowPtr`

[m] -`csrRowPtr`

[0] ) nonzero elements of matrix`A`

.**csrRowPtr**–**[in]**integer array of`m+1`

elements that contains the start of every row and the end of the last row plus one.**csrColInd**–**[in]**integer array of nnz ( =`csrRowPtr`

[m] -`csrRowPtr`

[0] ) column indices of the non-zero elements of matrix`A`

.**info**–**[in]**prune information structure**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer required by[hipsparseSpruneDense2csrNnzByPercentage()](#hipsparse__prune__dense2csr__by__percentage_8h_1afa03216a28f5bf36e3bce51950b4a140),[hipsparseDpruneDense2csrNnzByPercentage()](#hipsparse__prune__dense2csr__by__percentage_8h_1ae3aff7a76bd2b6bab8d6cf2c5283face).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**– the`handle`

or`pBufferSizeInBytes`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.



## hipsparseXpruneDense2csrByPercentage_bufferSizeExt()[#](#hipsparsexprunedense2csrbypercentage-buffersizeext)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpruneDense2csrByPercentage_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const float *A, int lda, float percentage, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descr, const float *csrVal, const int *csrRowPtr, const int *csrColInd,[pruneInfo_t](types.html#_CPPv411pruneInfo_t)info, size_t *pBufferSizeInBytes)[#](#_CPPv450hipsparseSpruneDense2csrByPercentage_bufferSizeExt17hipsparseHandle_tiiPKfifK19hipsparseMatDescr_tPKfPKiPKi11pruneInfo_tP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDpruneDense2csrByPercentage_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const double *A, int lda, double percentage, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descr, const double *csrVal, const int *csrRowPtr, const int *csrColInd,[pruneInfo_t](types.html#_CPPv411pruneInfo_t)info, size_t *pBufferSizeInBytes)[#](#_CPPv450hipsparseDpruneDense2csrByPercentage_bufferSizeExt17hipsparseHandle_tiiPKdidK19hipsparseMatDescr_tPKdPKiPKi11pruneInfo_tP6size_t) This function computes the size of the user allocated temporary storage buffer used when converting and pruning by percentage a dense matrix to a CSR matrix.

When converting and pruning a dense matrix A to a CSR matrix by percentage the following steps are performed. First the user calls

`hipsparseXpruneDense2csrByPercentage_bufferSizeExt`

which determines the size of the temporary storage buffer. Once determined, this buffer must be allocated by the user. Next the user allocates the`csrRowPtr`

array to have`m+1`

elements and calls[hipsparseXpruneDense2csrNnzByPercentage()](#hipsparse__prune__dense2csr__by__percentage_8h_1afa03216a28f5bf36e3bce51950b4a140). Finally the user finishes the conversion by allocating the`csrColInd`

and`csrVal`

arrays (whos size is determined by the value at`nnzTotalDevHostPtr`

) and calling[hipsparseXpruneDense2csrByPercentage()](#hipsparse__prune__dense2csr__by__percentage_8h_1ace1c36935b6211e53445f81331cc190b).The pruning by percentage works by first sorting the absolute values of the dense matrix

`A`

. We then determine a position in this sorted array by\[\begin{split} pos = ceil(m \cdot n \cdot (percentage/100)) - 1 \\ pos = \min(pos, m \cdot n-1) \\ pos = \max(pos, 0) \\ threshold = sorted_A[pos] \end{split}\]Once we have this threshold we prune values in the dense matrix

`A`

as in[hipsparseXpruneDense2csr()](#hipsparse__prune__dense2csr_8h_1ae059ad9fdc8ecd2ce0078c5f246b6222).Note

It is executed asynchronously with respect to the host and may return control to the application on the host before the entire result is ready.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the dense matrix`A`

.**n**–**[in]**number of columns of the dense matrix`A`

.**A**–**[in]**array of dimensions (`lda`

,`n`

)**lda**–**[in]**leading dimension of dense array`A`

.**percentage**–**[in]**`percentage>=0`

and`percentage<=100`

.**descr**–**[in]**the descriptor of the dense matrix`A`

, the supported matrix type is[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)and also any valid value of the[hipsparseIndexBase_t](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4).**csrVal**–**[in]**array of nnz ( =`csrRowPtr`

[m] -`csrRowPtr`

[0] ) nonzero elements of matrix`A`

.**csrRowPtr**–**[in]**integer array of`m+1`

elements that contains the start of every row and the end of the last row plus one.**csrColInd**–**[in]**integer array of nnz ( =`csrRowPtr`

[m] -`csrRowPtr`

[0] ) column indices of the non-zero elements of matrix`A`

.**info**–**[in]**prune information structure**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer required by[hipsparseSpruneDense2csrNnzByPercentage()](#hipsparse__prune__dense2csr__by__percentage_8h_1afa03216a28f5bf36e3bce51950b4a140),[hipsparseDpruneDense2csrNnzByPercentage()](#hipsparse__prune__dense2csr__by__percentage_8h_1ae3aff7a76bd2b6bab8d6cf2c5283face).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**– the`handle`

or`pBufferSizeInBytes`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.



## hipsparseXpruneDense2csrNnzByPercentage()[#](#hipsparsexprunedense2csrnnzbypercentage)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpruneDense2csrNnzByPercentage([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const float *A, int lda, float percentage, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descr, int *csrRowPtr, int *nnzTotalDevHostPtr,[pruneInfo_t](types.html#_CPPv411pruneInfo_t)info, void *buffer)[#](#_CPPv439hipsparseSpruneDense2csrNnzByPercentage17hipsparseHandle_tiiPKfifK19hipsparseMatDescr_tPiPi11pruneInfo_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDpruneDense2csrNnzByPercentage([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const double *A, int lda, double percentage, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descr, int *csrRowPtr, int *nnzTotalDevHostPtr,[pruneInfo_t](types.html#_CPPv411pruneInfo_t)info, void *buffer)[#](#_CPPv439hipsparseDpruneDense2csrNnzByPercentage17hipsparseHandle_tiiPKdidK19hipsparseMatDescr_tPiPi11pruneInfo_tPv) This function computes the number of nonzero elements per row and the total number of nonzero elements in a dense matrix when converting and pruning by percentage a dense matrix to a CSR matrix.

When converting and pruning a dense matrix A to a CSR matrix by percentage the following steps are performed. First the user calls

[hipsparseXpruneDense2csrByPercentage_bufferSize()](#hipsparse__prune__dense2csr__by__percentage_8h_1afe90279b2f19fceb880883e98156e29e)which determines the size of the temporary storage buffer. Once determined, this buffer must be allocated by the user. Next the user allocates the`csrRowPtr`

array to have`m+1`

elements and calls`hipsparseXpruneDense2csrNnzByPercentage`

. Finally the user finishes the conversion by allocating the`csrColInd`

and`csrVal`

arrays (whos size is determined by the value at`nnzTotalDevHostPtr`

) and calling[hipsparseXpruneDense2csrByPercentage()](#hipsparse__prune__dense2csr__by__percentage_8h_1ace1c36935b6211e53445f81331cc190b).The pruning by percentage works by first sorting the absolute values of the dense matrix

`A`

. We then determine a position in this sorted array by\[\begin{split} pos = ceil(m \cdot n \cdot (percentage/100)) - 1 \\ pos = \min(pos, m \cdot n-1) \\ pos = \max(pos, 0) \\ threshold = sorted_A[pos] \end{split}\]Once we have this threshold we prune values in the dense matrix

`A`

as in[hipsparseXpruneDense2csr()](#hipsparse__prune__dense2csr_8h_1ae059ad9fdc8ecd2ce0078c5f246b6222).Note

The routine does support asynchronous execution if the pointer mode is set to device.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the dense matrix`A`

.**n**–**[in]**number of columns of the dense matrix`A`

.**A**–**[in]**array of dimensions (`lda`

,`n`

)**lda**–**[in]**leading dimension of dense array`A`

.**percentage**–**[in]**`percentage>=0`

and`percentage<=100`

.**descr**–**[in]**the descriptor of the dense matrix`A`

.**csrRowPtr**–**[out]**integer array of`m+1`

elements that contains the start of every row and the end of the last row plus one.**nnzTotalDevHostPtr**–**[out]**total number of nonzero elements in device or host memory.**info**–**[in]**prune information structure**buffer**–**[out]**buffer allocated by the user whose size is determined by calling[hipsparseXpruneDense2csrByPercentage_bufferSize()](#hipsparse__prune__dense2csr__by__percentage_8h_1afe90279b2f19fceb880883e98156e29e)or[hipsparseXpruneDense2csrByPercentage_bufferSizeExt()](#hipsparse__prune__dense2csr__by__percentage_8h_1a5f59e4f1ade1b8b383cc39e7adf7da58).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`lda`

,`percentage`

,`A`

,`descr`

,`info`

,`csrRowPtr`

`nnzTotalDevHostPtr`

or`buffer`

pointer is invalid.



## hipsparseXpruneDense2csrByPercentage()[#](#hipsparsexprunedense2csrbypercentage)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpruneDense2csrByPercentage([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const float *A, int lda, float percentage, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descr, float *csrVal, const int *csrRowPtr, int *csrColInd,[pruneInfo_t](types.html#_CPPv411pruneInfo_t)info, void *buffer)[#](#_CPPv436hipsparseSpruneDense2csrByPercentage17hipsparseHandle_tiiPKfifK19hipsparseMatDescr_tPfPKiPi11pruneInfo_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDpruneDense2csrByPercentage([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const double *A, int lda, double percentage, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descr, double *csrVal, const int *csrRowPtr, int *csrColInd,[pruneInfo_t](types.html#_CPPv411pruneInfo_t)info, void *buffer)[#](#_CPPv436hipsparseDpruneDense2csrByPercentage17hipsparseHandle_tiiPKdidK19hipsparseMatDescr_tPdPKiPi11pruneInfo_tPv) This function computes the number of nonzero elements per row and the total number of nonzero elements in a dense matrix when converting and pruning by percentage a dense matrix to a CSR matrix.

When converting and pruning a dense matrix A to a CSR matrix by percentage the following steps are performed. First the user calls

[hipsparseXpruneDense2csrByPercentage_bufferSize()](#hipsparse__prune__dense2csr__by__percentage_8h_1afe90279b2f19fceb880883e98156e29e)which determines the size of the temporary storage buffer. Once determined, this buffer must be allocated by the user. Next the user allocates the`csrRowPtr`

array to have`m+1`

elements and calls[hipsparseXpruneDense2csrNnzByPercentage()](#hipsparse__prune__dense2csr__by__percentage_8h_1afa03216a28f5bf36e3bce51950b4a140). Finally the user finishes the conversion by allocating the`csrColInd`

and`csrVal`

arrays (whos size is determined by the value at`nnzTotalDevHostPtr`

) and calling`hipsparseXpruneDense2csrByPercentage`

.The pruning by percentage works by first sorting the absolute values of the dense matrix

`A`

. We then determine a position in this sorted array by\[\begin{split} pos = ceil(m \ cdot n \cdot (percentage/100)) - 1 \\ pos = \min(pos, m \cdot n-1) \\ pos = \max(pos, 0) \\ threshold = sorted_A[pos] \end{split}\]Once we have this threshold we prune values in the dense matrix

`A`

as in[hipsparseXpruneDense2csr()](#hipsparse__prune__dense2csr_8h_1ae059ad9fdc8ecd2ce0078c5f246b6222).**Example**int main(int argc, char* argv[]) { // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // Matrix descriptor hipsparseMatDescr_t descr; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&descr)); // Dense matrix in column order // 1 2 0 3 0 // A = 0 4 5 0 0 // 6 0 0 7 8 float hdense_A[15] = { 1.0f, 0.0f, 6.0f, 2.0f, 4.0f, 0.0f, 0.0f, 5.0f, 0.0f, 3.0f, 0.0f, 7.0f, 0.0f, 0.0f, 8.0f}; int m = 3; int n = 5; int lda = m; float percentage = 70.0f; float* ddense_A = nullptr; HIP_CHECK(hipMalloc((void**)&ddense_A, sizeof(float) * lda * n)); HIP_CHECK(hipMemcpy(ddense_A, hdense_A, sizeof(float) * lda * n, hipMemcpyHostToDevice)); // Allocate sparse CSR matrix int* dcsrRowPtr = nullptr; HIP_CHECK(hipMalloc((void**)&dcsrRowPtr, sizeof(int) * (m + 1))); pruneInfo_t info; HIPSPARSE_CHECK(hipsparseCreatePruneInfo(&info)); size_t bufferSize; HIPSPARSE_CHECK(hipsparseSpruneDense2csrByPercentage_bufferSize(handle, m, n, ddense_A, lda, percentage, descr, nullptr, dcsrRowPtr, nullptr, info, &bufferSize)); void* dbuffer = nullptr; HIP_CHECK(hipMalloc((void**)&dbuffer, bufferSize)); int nnz_A; HIPSPARSE_CHECK(hipsparseSpruneDense2csrNnzByPercentage( handle, m, n, ddense_A, lda, percentage, descr, dcsrRowPtr, &nnz_A, info, dbuffer)); int* dcsrColInd = nullptr; float* dcsrVal = nullptr; HIP_CHECK(hipMalloc((void**)&dcsrColInd, sizeof(int) * nnz_A)); HIP_CHECK(hipMalloc((void**)&dcsrVal, sizeof(float) * nnz_A)); HIPSPARSE_CHECK(hipsparseSpruneDense2csrByPercentage(handle, m, n, ddense_A, lda, percentage, descr, dcsrVal, dcsrRowPtr, dcsrColInd, info, dbuffer)); HIP_CHECK(hipFree(dcsrRowPtr)); HIP_CHECK(hipFree(dcsrColInd)); HIP_CHECK(hipFree(dcsrVal)); HIP_CHECK(hipFree(ddense_A)); HIP_CHECK(hipFree(dbuffer)); HIPSPARSE_CHECK(hipsparseDestroyPruneInfo(info)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(descr)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); return 0; }


Note

The routine does support asynchronous execution if the pointer mode is set to device.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the dense matrix`A`

.**n**–**[in]**number of columns of the dense matrix`A`

.**A**–**[in]**array of dimensions (`lda`

,`n`

)**lda**–**[in]**leading dimension of dense array`A`

.**percentage**–**[in]**`percentage>=0`

and`percentage<=100`

.**descr**–**[in]**the descriptor of the dense matrix`A`

, the supported matrix type is[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)and also any valid value of the[hipsparseIndexBase_t](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4).**csrVal**–**[out]**array of nnz ( =`csrRowPtr`

[m] -`csrRowPtr`

[0] ) nonzero elements of matrix`A`

.**csrRowPtr**–**[in]**integer array of`m+1`

elements that contains the start of every row and the end of the last row plus one.**csrColInd**–**[out]**integer array of nnz ( =`csrRowPtr`

[m] -`csrRowPtr`

[0] ) column indices of the non-zero elements of matrix`A`

.**info**–**[in]**prune information structure**buffer**–**[in]**temporary storage buffer allocated by the user, size is returned by[hipsparseXpruneDense2csrByPercentage_bufferSize()](#hipsparse__prune__dense2csr__by__percentage_8h_1afe90279b2f19fceb880883e98156e29e)or[hipsparseXpruneDense2csrByPercentage_bufferSizeExt()](#hipsparse__prune__dense2csr__by__percentage_8h_1a5f59e4f1ade1b8b383cc39e7adf7da58).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`lda`

,`percentage`

,`A`

,`descr`

,`info`

,`csrVal`

`csrRowPtr`

,`csrColInd`

or`buffer`

pointer is invalid.



## hipsparseXdense2csc()[#](#hipsparsexdense2csc)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSdense2csc([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descr, const float *A, int ld, const int *nnzPerColumn, float *cscVal, int *cscRowInd, int *cscColPtr)[#](#_CPPv419hipsparseSdense2csc17hipsparseHandle_tiiK19hipsparseMatDescr_tPKfiPKiPfPiPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDdense2csc([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descr, const double *A, int ld, const int *nnzPerColumn, double *cscVal, int *cscRowInd, int *cscColPtr)[#](#_CPPv419hipsparseDdense2csc17hipsparseHandle_tiiK19hipsparseMatDescr_tPKdiPKiPdPiPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCdense2csc([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descr, const hipComplex *A, int ld, const int *nnzPerColumn, hipComplex *cscVal, int *cscRowInd, int *cscColPtr)[#](#_CPPv419hipsparseCdense2csc17hipsparseHandle_tiiK19hipsparseMatDescr_tPK10hipComplexiPKiP10hipComplexPiPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZdense2csc([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descr, const hipDoubleComplex *A, int ld, const int *nnzPerColumn, hipDoubleComplex *cscVal, int *cscRowInd, int *cscColPtr)[#](#_CPPv419hipsparseZdense2csc17hipsparseHandle_tiiK19hipsparseMatDescr_tPK16hipDoubleComplexiPKiP16hipDoubleComplexPiPi) `hipsparseXdense2csc`

converts the matrix A in dense format into a sparse matrix in CSC format.Given a dense, column ordered, matrix

`A`

with leading dimension`ld`

where`ld>=m`

,`hipsparseXdense2csc`

converts the matrix to a sparse CSC format matrix. All the parameters are assumed to have been pre-allocated by the user and the arrays are filled in based on number of nonzeros per row, which can be pre-computed with[hipsparseXnnz()](#hipsparse__nnz_8h_1a939d35fea53d730267afe6abda38fcbf). We can set the desired index base in the output CSC matrix by setting it in the[hipsparseMatDescr_t](types.html#hipsparse-types_8h_1a4c2f3ad3f2057bffb1adf6a8256537b9). See[hipsparseSetMatIndexBase()](auxiliary.html#hipsparse-auxiliary_8h_1a3c81b4bd7b1e9bb04a63a620f51dc2a8).As an example, if using index base zero (i.e. the default) and the dense matrix:

\[\begin{split} \begin{bmatrix} 1 & 0 & 0 & 2 \\ 3 & 4 & 0 & 0 \\ 5 & 0 & 6 & 7 \end{bmatrix} \end{split}\]where the

`A`

values have column ordering with leading dimension`ld=m:`

\[\begin{split} \text{A} &= \begin{bmatrix} 1 & 3 & 5 & 0 & 4 & 0 & 0 & 0 & 6 & 2 & 0 & 7 \end{bmatrix} \\ \end{split}\]the conversion results in the CSC arrays:

\[\begin{split} \begin{align} \text{cscRowInd} &= \begin{bmatrix} 0 & 1 & 2 & 1 & 2 & 0 & 2 \end{bmatrix} \\ \text{cscColPtr} &= \begin{bmatrix} 0 & 3 & 4 & 5 & 7 \end{bmatrix} \\ \text{cscVal} &= \begin{bmatrix} 1 & 3 & 5 & 4 & 6 & 2 & 7 \end{bmatrix} \\ \end{align} \end{split}\]This function works very similar to

[hipsparseXdense2csr()](#hipsparse__dense2csr_8h_1a50644fe63a8ff54bc39e7393286b050f). & See[hipsparseSdense2csr()](#hipsparse__dense2csr_8h_1a50644fe63a8ff54bc39e7393286b050f)for a code example.Note

It is executed asynchronously with respect to the host and may return control to the application on the host before the entire result is ready.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the dense matrix`A`

.**n**–**[in]**number of columns of the dense matrix`A`

.**descr**–**[in]**the descriptor of the dense matrix`A`

, the supported matrix type is[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)and also any valid value of the[hipsparseIndexBase_t](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4).**A**–**[in]**array of dimensions (`ld`

,`n`

)**ld**–**[in]**leading dimension of dense array`A`

.**nnzPerColumn**–**[in]**array of size`n`

containing the number of non-zero elements per column.**cscVal**–**[out]**array of nnz ( =`cscColPtr`

[n] -`cscColPtr`

[0] ) nonzero elements of matrix`A`

.**cscRowInd**–**[out]**integer array of nnz ( =`cscColPtr`

[n] -`cscColPtr`

[0] ) column indices of the non-zero elements of matrix`A`

.**cscColPtr**–**[out]**integer array of`n+1`

elements that contains the start of every column and the end of the last column plus one.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`ld`

,`A`

,`nnzPerColumn`

or`cscVal`

`cscColPtr`

or`cscRowInd`

pointer is invalid.



## hipsparseXcsr2dense()[#](#hipsparsexcsr2dense)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseScsr2dense([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descr, const float *csrVal, const int *csrRowPtr, const int *csrColInd, float *A, int ld)[#](#_CPPv419hipsparseScsr2dense17hipsparseHandle_tiiK19hipsparseMatDescr_tPKfPKiPKiPfi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDcsr2dense([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descr, const double *csrVal, const int *csrRowPtr, const int *csrColInd, double *A, int ld)[#](#_CPPv419hipsparseDcsr2dense17hipsparseHandle_tiiK19hipsparseMatDescr_tPKdPKiPKiPdi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCcsr2dense([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descr, const hipComplex *csrVal, const int *csrRowPtr, const int *csrColInd, hipComplex *A, int ld)[#](#_CPPv419hipsparseCcsr2dense17hipsparseHandle_tiiK19hipsparseMatDescr_tPK10hipComplexPKiPKiP10hipComplexi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZcsr2dense([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descr, const hipDoubleComplex *csrVal, const int *csrRowPtr, const int *csrColInd, hipDoubleComplex *A, int ld)[#](#_CPPv419hipsparseZcsr2dense17hipsparseHandle_tiiK19hipsparseMatDescr_tPK16hipDoubleComplexPKiPKiP16hipDoubleComplexi) `hipsparseXcsr2dense`

function converts the sparse matrix in CSR format into a dense matrix.Given the input CSR matrix of size

`mxn`

, the routine writes the matrix to the dense array`A`

such that`A`

has leading dimension`ld`

and is column ordered. This means that`A`

has size`ldxn`

where`ld>=m`

. All the parameters are assumed to have been pre-allocated by the user. If the input CSR matrix has index base of one, it must be set in the[hipsparseMatDescr_t](types.html#hipsparse-types_8h_1a4c2f3ad3f2057bffb1adf6a8256537b9). See[hipsparseSetMatIndexBase()](auxiliary.html#hipsparse-auxiliary_8h_1a3c81b4bd7b1e9bb04a63a620f51dc2a8)prior to calling`hipsparseXcsr2dense`

.For example, consider the sparse CSR matrix:

\[\begin{split} \begin{align} \text{csrRowPtr} &= \begin{bmatrix} 0 & 2 & 4 & 7 \end{bmatrix} \\ \text{csrColInd} &= \begin{bmatrix} 0 & 3 & 0 & 1 & 0 & 2 & 3 \end{bmatrix} \\ \text{csrVal} &= \begin{bmatrix} 1 & 2 & 3 & 4 & 5 & 6 & 7 \end{bmatrix} \\ \end{align} \end{split}\]`hipsparseXcsr2dense`

is used to convert to the dense matrix:\[\begin{split} \begin{bmatrix} 1 & 0 & 0 & 2 \\ 3 & 4 & 0 & 0 \\ 5 & 0 & 6 & 7 \end{bmatrix} \end{split}\]where the values in the

`A`

array are column ordered:\[\begin{split} \text{A} &= \begin{bmatrix} 1 & 3 & 5 & 0 & 4 & 0 & 0 & 0 & 6 & 2 & 0 & 7 \end{bmatrix} \\ \end{split}\]**Example**int main(int argc, char* argv[]) { // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // Matrix descriptor hipsparseMatDescr_t descr; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&descr)); // Sparse matrix in CSR format // 1 2 0 3 0 // A = 0 4 5 0 0 // 6 0 0 7 8 int hcsrRowPtr[4] = {0, 3, 5, 8}; int hcsrColInd[8] = {0, 1, 3, 1, 2, 0, 3, 4}; float hcsrVal[8] = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f}; int m = 3; int n = 5; int ld = 3; int nnz = 8; int* dcsrRowPtr = nullptr; int* dcsrColInd = nullptr; float* dcsrVal = nullptr; HIP_CHECK(hipMalloc((void**)&dcsrRowPtr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&dcsrColInd, sizeof(int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcsrVal, sizeof(float) * nnz)); HIP_CHECK(hipMemcpy(dcsrRowPtr, hcsrRowPtr, sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrColInd, hcsrColInd, sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrVal, hcsrVal, sizeof(float) * nnz, hipMemcpyHostToDevice)); float* ddense_A = nullptr; HIP_CHECK(hipMalloc((void**)&ddense_A, sizeof(float) * ld * n)); HIPSPARSE_CHECK( hipsparseScsr2dense(handle, m, n, descr, dcsrVal, dcsrRowPtr, dcsrColInd, ddense_A, ld)); HIP_CHECK(hipFree(dcsrRowPtr)); HIP_CHECK(hipFree(dcsrColInd)); HIP_CHECK(hipFree(dcsrVal)); HIP_CHECK(hipFree(ddense_A)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(descr)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); return 0; }


Note

It is executed asynchronously with respect to the host and may return control to the application on the host before the entire result is ready.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the dense matrix`A`

.**n**–**[in]**number of columns of the dense matrix`A`

.**descr**–**[in]**the descriptor of the dense matrix`A`

, the supported matrix type is[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)and also any valid value of the[hipsparseIndexBase_t](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4).**csrVal**–**[in]**array of nnz ( =`csrRowPtr`

[m] -`csrRowPtr`

[0] ) nonzero elements of matrix`A`

.**csrRowPtr**–**[in]**integer array of`m+1`

elements that contains the start of every row and the end of the last row plus one.**csrColInd**–**[in]**integer array of nnz ( =`csrRowPtr`

[m] -`csrRowPtr`

[0] ) column indices of the non-zero elements of matrix`A`

.**A**–**[out]**array of dimensions (`ld`

,`n`

)**ld**–**[out]**leading dimension of dense array`A`

.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`ld`

,`A`

,`csrVal`

,`csrRowPtr`

or`csrColInd`

pointer is invalid.



## hipsparseXcsc2dense()[#](#hipsparsexcsc2dense)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseScsc2dense([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descr, const float *cscVal, const int *cscRowInd, const int *cscColPtr, float *A, int ld)[#](#_CPPv419hipsparseScsc2dense17hipsparseHandle_tiiK19hipsparseMatDescr_tPKfPKiPKiPfi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDcsc2dense([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descr, const double *cscVal, const int *cscRowInd, const int *cscColPtr, double *A, int ld)[#](#_CPPv419hipsparseDcsc2dense17hipsparseHandle_tiiK19hipsparseMatDescr_tPKdPKiPKiPdi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCcsc2dense([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descr, const hipComplex *cscVal, const int *cscRowInd, const int *cscColPtr, hipComplex *A, int ld)[#](#_CPPv419hipsparseCcsc2dense17hipsparseHandle_tiiK19hipsparseMatDescr_tPK10hipComplexPKiPKiP10hipComplexi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZcsc2dense([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descr, const hipDoubleComplex *cscVal, const int *cscRowInd, const int *cscColPtr, hipDoubleComplex *A, int ld)[#](#_CPPv419hipsparseZcsc2dense17hipsparseHandle_tiiK19hipsparseMatDescr_tPK16hipDoubleComplexPKiPKiP16hipDoubleComplexi) `hipsparseXcsc2dense`

function converts the sparse matrix in CSC format into a dense matrix.Given the input CSC matrix of size

`mxn`

, the routine writes the matrix to the dense array`A`

such that`A`

has leading dimension`ld`

and is column ordered. This means that`A`

has size`ldxn`

where`ld>=m`

. All the parameters are assumed to have been pre-allocated by the user. If the input CSC matrix has index base of one, it must be set in the[hipsparseMatDescr_t](types.html#hipsparse-types_8h_1a4c2f3ad3f2057bffb1adf6a8256537b9). See[hipsparseSetMatIndexBase()](auxiliary.html#hipsparse-auxiliary_8h_1a3c81b4bd7b1e9bb04a63a620f51dc2a8)prior to calling`hipsparseXcsc2dense`

.For example, consider the sparse CSC matrix:

\[\begin{split} \begin{align} \text{cscRowInd} &= \begin{bmatrix} 0 & 1 & 2 & 1 & 2 & 0 & 2 \end{bmatrix} \\ \text{cscColPtr} &= \begin{bmatrix} 0 & 3 & 4 & 5 & 7 \end{bmatrix} \\ \text{cscVal} &= \begin{bmatrix} 1 & 3 & 5 & 4 & 6 & 2 & 7 \end{bmatrix} \\ \end{align} \end{split}\]`hipsparseXcsc2dense`

is used to convert to the dense matrix:\[\begin{split} \begin{bmatrix} 1 & 0 & 0 & 2 \\ 3 & 4 & 0 & 0 \\ 5 & 0 & 6 & 7 \end{bmatrix} \end{split}\]where the values in the

`A`

array are column ordered:\[\begin{split} \text{A} &= \begin{bmatrix} 1 & 3 & 5 & 0 & 4 & 0 & 0 & 0 & 6 & 2 & 0 & 7 \end{bmatrix} \\ \end{split}\]Note

It is executed asynchronously with respect to the host and may return control to the application on the host before the entire result is ready.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the dense matrix`A`

.**n**–**[in]**number of columns of the dense matrix`A`

.**descr**–**[in]**the descriptor of the dense matrix`A`

, the supported matrix type is[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)and also any valid value of the[hipsparseIndexBase_t](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4).**cscVal**–**[in]**array of nnz ( =`cscColPtr`

[n] -`cscColPtr`

[0] ) nonzero elements of matrix`A`

.**cscRowInd**–**[in]**integer array of nnz ( =`cscColPtr`

[n] -`cscColPtr`

[0] ) column indices of the non-zero elements of matrix`A`

.**cscColPtr**–**[in]**integer array of`n+1`

elements that contains the start of every column and the end of the last column plus one.**A**–**[out]**array of dimensions (`ld`

,`n`

)**ld**–**[out]**leading dimension of dense array`A`

.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`ld`

,`A`

,`cscVal`

`cscColPtr`

or`cscRowInd`

pointer is invalid.



## hipsparseXcsr2bsrNnz()[#](#hipsparsexcsr2bsrnnz)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseXcsr2bsrNnz([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const int *csrRowPtrA, const int *csrColIndA, int blockDim, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, int *bsrRowPtrC, int *bsrNnzb)[#](#_CPPv420hipsparseXcsr2bsrNnz17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPKiPKiiK19hipsparseMatDescr_tPiPi) This function computes the number of nonzero block columns per row and the total number of nonzero blocks in a sparse BSR matrix given a sparse CSR matrix as input.

Consider the matrix:

\[\begin{split} \begin{bmatrix} 1 & 0 & 0 & 2 \\ 3 & 4 & 0 & 0 \\ 5 & 0 & 6 & 7 \\ 1 & 2 & 3 & 4 \end{bmatrix} \end{split}\]stored as a sparse CSR matrix. This function computes both the BSR row pointer array as well as the total number of non-zero blocks that results when converting the CSR matrix to the BSR format. Assuming a block dimension of 2, the above matrix once converted to BSR format looks like:

\[\begin{split} \left[ \begin{array}{c | c} \begin{array}{c c} 1 & 0 \\ 3 & 4 \end{array} & \begin{array}{c c} 0 & 2 \\ 0 & 0 \end{array} \\ \hline \begin{array}{c c} 5 & 0 \\ 1 & 2 \end{array} & \begin{array}{c c} 6 & 7 \\ 3 & 4 \end{array} \\ \end{array} \right] \end{split}\]and the resulting BSR row pointer array and total non-zero blocks once

`hipsparseXcsr2bsrNnz`

has been called:\[\begin{split} \begin{align} \text{bsrRowPtrC} &= \begin{bmatrix} 0 & 2 & 4 \end{bmatrix} \\ \text{bsrNnzb} &= 4 \end{align} \end{split}\]In general, when converting a CSR matrix of size

`m`

x`n`

to a BSR matrix, the resulting BSR matrix will have size`mb`

x`nb`

where`mb`

and`nb`

equal:\[\begin{split} \begin{align} \text{mb} &= \text{(m - 1) / blockDim + 1} \\ \text{nb} &= \text{(n - 1) / blockDim + 1} \end{align} \end{split}\]In particular, it may be the case that

`blockDim`

does not divide evenly into`m`

and/or`n`

. In these cases, the CSR matrix is expanded in size in order to fit full BSR blocks. For example, using the original CSR matrix and block dimension 3 instead of 2, the function`hipsparseXcsr2bsrNnz`

computes the BSR row pointer array and total number of non-zero blocks for the BSR matrix:\[\begin{split} \left[ \begin{array}{c | c} \begin{array}{c c c} 1 & 0 & 0 \\ 3 & 4 & 0 \\ 5 & 0 & 6 \end{array} & \begin{array}{c c c} 2 & 0 & 0 \\ 0 & 0 & 0 \\ 7 & 0 & 0 \end{array} \\ \hline \begin{array}{c c c} 1 & 2 & 3 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} & \begin{array}{c c c} 4 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \\ \end{array} \right] \end{split}\]See

[hipsparseScsr2bsr()](#hipsparse__csr2bsr_8h_1ac8c0ae4bfa5e5873d1374b22308e700d)for full code example.Note

The routine does support asynchronous execution if the pointer mode is set to device.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**dirA**–**[in]**direction that specified whether to count nonzero elements by[HIPSPARSE_DIRECTION_ROW](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59ae8589abecf2fbfb4b6307fd9dacd9e55)or by[HIPSPARSE_DIRECTION_COLUMN](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59a32e23f292b2377f6e60bdc90274c796c).**m**–**[in]**number of rows of the sparse CSR matrix.**n**–**[in]**number of columns of the sparse CSR matrix.**descrA**–**[in]**descriptor of the sparse CSR matrix. Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**csrRowPtrA**–**[in]**integer array containing`m+1`

elements that point to the start of each row of the CSR matrix**csrColIndA**–**[in]**integer array of the column indices for each non-zero element in the CSR matrix**blockDim**–**[in]**the block dimension of the BSR matrix. Between \(1\) and \(\min(m, n)\)**descrC**–**[in]**descriptor of the sparse BSR matrix. Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**bsrRowPtrC**–**[out]**integer array containing`mb+1`

elements that point to the start of each block row of the BSR matrix**bsrNnzb**–**[out]**total number of nonzero elements in device or host memory.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`blockDim`

,`csrRowPtrA`

,`csrColIndA`

,`bsrRowPtrC`

or`bsrNnzb`

pointer is invalid.



## hipsparseXcsr2bsr()[#](#hipsparsexcsr2bsr)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseScsr2bsr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const float *csrValA, const int *csrRowPtrA, const int *csrColIndA, int blockDim, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, float *bsrValC, int *bsrRowPtrC, int *bsrColIndC)[#](#_CPPv417hipsparseScsr2bsr17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPKfPKiPKiiK19hipsparseMatDescr_tPfPiPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDcsr2bsr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const double *csrValA, const int *csrRowPtrA, const int *csrColIndA, int blockDim, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, double *bsrValC, int *bsrRowPtrC, int *bsrColIndC)[#](#_CPPv417hipsparseDcsr2bsr17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPKdPKiPKiiK19hipsparseMatDescr_tPdPiPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCcsr2bsr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipComplex *csrValA, const int *csrRowPtrA, const int *csrColIndA, int blockDim, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, hipComplex *bsrValC, int *bsrRowPtrC, int *bsrColIndC)[#](#_CPPv417hipsparseCcsr2bsr17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPK10hipComplexPKiPKiiK19hipsparseMatDescr_tP10hipComplexPiPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZcsr2bsr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipDoubleComplex *csrValA, const int *csrRowPtrA, const int *csrColIndA, int blockDim, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, hipDoubleComplex *bsrValC, int *bsrRowPtrC, int *bsrColIndC)[#](#_CPPv417hipsparseZcsr2bsr17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPK16hipDoubleComplexPKiPKiiK19hipsparseMatDescr_tP16hipDoubleComplexPiPi) Convert a sparse CSR matrix into a sparse BSR matrix.

`hipsparseXcsr2bsr`

completes the conversion of a CSR matrix into a BSR matrix. It is assumed, that`bsrValC`

,`bsrColIndC`

and`bsrRowPtrC`

are allocated. The allocation size for`bsrRowPtr`

is computed as`mb+1`

where`mb`

is the number of block rows in the BSR matrix defined as:\[ \begin{align} \text{mb} &= \text{(m - 1) / blockDim + 1} \end{align} \]The allocation size for

`bsrColIndC`

, i.e.`bsrNnzb`

, is computed using[hipsparseXcsr2bsrNnz()](#hipsparse__csr2bsr_8h_1a85c7a64b0de03ebfd87c7132c567fcfb)which also fills the`bsrRowPtrC`

array. The allocation size for`bsrValC`

is then equal to:\[ \text{bsrNnzb * blockDim * blockDim} \]For example, given the CSR matrix:

\[\begin{split} \begin{bmatrix} 1 & 0 & 0 & 2 \\ 3 & 4 & 0 & 0 \\ 5 & 0 & 6 & 7 \\ 1 & 2 & 3 & 4 \end{bmatrix} \end{split}\]The resulting BSR matrix using block dimension 2 would look like:

\[\begin{split} \left[ \begin{array}{c | c} \begin{array}{c c} 1 & 0 \\ 3 & 4 \end{array} & \begin{array}{c c} 0 & 2 \\ 0 & 0 \end{array} \\ \hline \begin{array}{c c} 5 & 0 \\ 1 & 2 \end{array} & \begin{array}{c c} 6 & 7 \\ 3 & 4 \end{array} \\ \end{array} \right] \end{split}\]The call to

[hipsparseXcsr2bsrNnz](#hipsparse__csr2bsr_8h_1a85c7a64b0de03ebfd87c7132c567fcfb)results in the BSR row pointer array:\[\begin{split} \begin{align} \text{bsrRowPtrC} &= \begin{bmatrix} 0 & 2 & 4 \end{bmatrix} \\ \end{align} \end{split}\]and the call to

`hipsparseXcsr2bsr`

completes the conversion resulting in the BSR column indices and values arrays:\[\begin{split} \begin{align} \text{bsrColIndC} &= \begin{bmatrix} 0 & 1 & 0 & 1 \end{bmatrix} \\ \text{bsrValC} &= \begin{bmatrix} 1 & 0 & 3 & 4 & 0 & 2 & 0 & 0 & 5 & 0 & 1 & 2 & 6 & 7 & 3 & 4 \end{bmatrix} \\ \end{align} \end{split}\]The

`dirA`

parameter determines the order of the BSR block values. The example above uses row order. Using column ordering would result instead in the BSR values array:\[\begin{split} \text{bsrValC} &= \begin{bmatrix} 1 & 3 & 0 & 4 & 0 & 0 & 2 & 0 & 5 & 1 & 0 & 2 & 6 & 3 & 7 & 4 \end{bmatrix} \\ \end{split}\]**Example**int main(int argc, char* argv[]) { // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // Matrix descriptor hipsparseMatDescr_t csr_descr; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&csr_descr)); hipsparseMatDescr_t bsr_descr; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&bsr_descr)); // Sparse matrix in CSR format // 1 2 0 3 0 // A = 0 4 5 0 0 // 6 0 0 7 8 int hcsrRowPtr[4] = {0, 3, 5, 8}; int hcsrColInd[8] = {0, 1, 3, 1, 2, 0, 3, 4}; float hcsrVal[8] = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f}; int m = 3; int n = 5; int nnz = 8; int blockDim = 3; hipsparseDirection_t dir = HIPSPARSE_DIRECTION_ROW; int mb = (m + blockDim - 1) / blockDim; int nb = (n + blockDim - 1) / blockDim; int* dcsrRowPtr = nullptr; int* dcsrColInd = nullptr; float* dcsrVal = nullptr; HIP_CHECK(hipMalloc((void**)&dcsrRowPtr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&dcsrColInd, sizeof(int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcsrVal, sizeof(float) * nnz)); HIP_CHECK(hipMemcpy(dcsrRowPtr, hcsrRowPtr, sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrColInd, hcsrColInd, sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrVal, hcsrVal, sizeof(float) * nnz, hipMemcpyHostToDevice)); int* dbsrRowPtr = nullptr; HIP_CHECK(hipMalloc((void**)&dbsrRowPtr, sizeof(int) * (mb + 1))); int nnzb; HIPSPARSE_CHECK(hipsparseXcsr2bsrNnz(handle, dir, m, n, csr_descr, dcsrRowPtr, dcsrColInd, blockDim, bsr_descr, dbsrRowPtr, &nnzb)); int* dbsrColInd = nullptr; float* dbsrVal = nullptr; HIP_CHECK(hipMalloc((void**)&dbsrColInd, sizeof(int) * nnzb)); HIP_CHECK(hipMalloc((void**)&dbsrVal, sizeof(float) * blockDim * blockDim * nnzb)); HIPSPARSE_CHECK(hipsparseScsr2bsr(handle, dir, m, n, csr_descr, dcsrVal, dcsrRowPtr, dcsrColInd, blockDim, bsr_descr, dbsrVal, dbsrRowPtr, dbsrColInd)); HIP_CHECK(hipFree(dcsrRowPtr)); HIP_CHECK(hipFree(dcsrColInd)); HIP_CHECK(hipFree(dcsrVal)); HIP_CHECK(hipFree(dbsrRowPtr)); HIP_CHECK(hipFree(dbsrColInd)); HIP_CHECK(hipFree(dbsrVal)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(csr_descr)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(bsr_descr)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); return 0; }


Note

`hipsparseXcsr2bsr`

requires extra temporary storage that is allocated internally if`blockDim>16`

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**dirA**–**[in]**the storage format of the blocks,[HIPSPARSE_DIRECTION_ROW](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59ae8589abecf2fbfb4b6307fd9dacd9e55)or[HIPSPARSE_DIRECTION_COLUMN](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59a32e23f292b2377f6e60bdc90274c796c)**m**–**[in]**number of rows in the sparse CSR matrix.**n**–**[in]**number of columns in the sparse CSR matrix.**descrA**–**[in]**descriptor of the sparse CSR matrix. Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**csrValA**–**[in]**array of`nnz`

elements containing the values of the sparse CSR matrix.**csrRowPtrA**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csrColIndA**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**blockDim**–**[in]**size of the blocks in the sparse BSR matrix.**descrC**–**[in]**descriptor of the sparse BSR matrix. Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**bsrValC**–**[out]**array of`nnzb*blockDim*blockDim`

containing the values of the sparse BSR matrix.**bsrRowPtrC**–**[out]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix.**bsrColIndC**–**[out]**array of`nnzb`

elements containing the block column indices of the sparse BSR matrix.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`blockDim`

,`bsrValC`

,`bsrRowPtrC`

,`bsrColIndC`

,`csrValA`

,`csrRowPtrA`

or`csrColIndA`

pointer is invalid.



## hipsparseXnnz_compress()[#](#hipsparsexnnz-compress)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSnnz_compress([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const float *csrValA, const int *csrRowPtrA, int *nnzPerRow, int *nnzC, float tol)[#](#_CPPv422hipsparseSnnz_compress17hipsparseHandle_tiK19hipsparseMatDescr_tPKfPKiPiPif)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDnnz_compress([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const double *csrValA, const int *csrRowPtrA, int *nnzPerRow, int *nnzC, double tol)[#](#_CPPv422hipsparseDnnz_compress17hipsparseHandle_tiK19hipsparseMatDescr_tPKdPKiPiPid)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCnnz_compress([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipComplex *csrValA, const int *csrRowPtrA, int *nnzPerRow, int *nnzC, hipComplex tol)[#](#_CPPv422hipsparseCnnz_compress17hipsparseHandle_tiK19hipsparseMatDescr_tPK10hipComplexPKiPiPi10hipComplex)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZnnz_compress([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipDoubleComplex *csrValA, const int *csrRowPtrA, int *nnzPerRow, int *nnzC, hipDoubleComplex tol)[#](#_CPPv422hipsparseZnnz_compress17hipsparseHandle_tiK19hipsparseMatDescr_tPK16hipDoubleComplexPKiPiPi16hipDoubleComplex) This function is used as the first step in converting a CSR matrix to a compressed CSR matrix.

Given a sparse CSR matrix and a non-negative tolerance, this function computes how many entries would be left in each row of the matrix if elements less than the tolerance were removed. It also computes the total number of remaining elements in the matrix.

Specifically given an input sparse matrix A in CSR format, the resulting compressed sparse CSR matrix C is computed using:

\[ C(i,j) = A(i, j) \text{ if |A(i, j)| > tol} \]The user first allocates

`nnzPerRow`

with size`m`

elements. Then calling`hipsparseXnnz_compress`

, the function fills in the`nnzPerRow`

array and sets the total number of nonzeros found in`nnzC`

.See

[hipsparseScsr2csr_compress()](#hipsparse__csr2csr__compress_8h_1abb44035d98127875bf731e3afcf5f974)for full code example.**Example**int main(int argc, char* argv[]) { // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // Matrix descriptor hipsparseMatDescr_t descr_A; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&descr_A)); // 1 2 0 3 0 // A = 0 4 5 0 0 // 6 0 0 7 8 float tol = 4.2f; int m = 3; int n = 5; int nnz_A = 8; int hcsrRowPtr_A[4] = {0, 3, 5, 8}; float hcsrVal_A[8] = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f}; int* dcsrRowPtr_A = nullptr; float* dcsrVal_A = nullptr; HIP_CHECK(hipMalloc((void**)&dcsrRowPtr_A, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&dcsrVal_A, sizeof(float) * nnz_A)); HIP_CHECK(hipMemcpy(dcsrRowPtr_A, hcsrRowPtr_A, sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrVal_A, hcsrVal_A, sizeof(float) * nnz_A, hipMemcpyHostToDevice)); // Allocate memory for the nnz_per_row array int* dnnz_per_row; HIP_CHECK(hipMalloc((void**)&dnnz_per_row, sizeof(int) * m)); // Call snnz_compress() which fills in nnz_per_row array and finds the number // of entries that will be in the compressed CSR matrix int nnz_C; HIPSPARSE_CHECK(hipsparseSnnz_compress( handle, m, descr_A, dcsrVal_A, dcsrRowPtr_A, dnnz_per_row, &nnz_C, tol)); HIP_CHECK(hipFree(dcsrRowPtr_A)); HIP_CHECK(hipFree(dcsrVal_A)); HIP_CHECK(hipFree(dnnz_per_row)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(descr_A)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); return 0; }


Note

In the case of complex matrices only the magnitude of the real part of

`tol`

is used.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix.**descrA**–**[in]**the descriptor of the sparse CSR matrix.**csrValA**–**[in]**array of`nnzA`

elements of the sparse CSR matrix.**csrRowPtrA**–**[in]**array of`m+1`

elements that point to the start of every row of the uncompressed sparse CSR matrix.**nnzPerRow**–**[out]**array of length`m`

containing the number of entries that will be kept per row in the final compressed CSR matrix.**nnzC**–**[out]**number of elements in the column indices and values arrays of the compressed sparse CSR matrix. Can be either host or device pointer.**tol**–**[in]**the non-negative tolerance used for compression. If`tol`

is complex then only the magnitude of the real part is used. Entries in the input uncompressed CSR array that are below the tolerance are removed in output compressed CSR matrix.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`tol`

,`csrValA`

,`csrRowPtrA`

,`nnzPerRow`

or`nnzC`

pointer is invalid.



## hipsparseXcsr2coo()[#](#hipsparsexcsr2coo)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseXcsr2coo([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, const int *csrRowPtr, int nnz, int m, int *cooRowInd,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase)[#](#_CPPv417hipsparseXcsr2coo17hipsparseHandle_tPKiiiPi20hipsparseIndexBase_t) Convert a sparse CSR matrix into a sparse COO matrix.

`hipsparseXcsr2coo`

converts the CSR array containing the row offsets, that point to the start of every row, into a COO array of row indices. All arrays are assumed to be allocated by the user prior to calling`hipsparseXcsr2coo`

.For example, given the CSR row pointer array (assuming zero index base):

\[ \begin{align} \text{csrRowPtr} &= \begin{bmatrix} 0 & 1 & 3 & 4 \end{bmatrix} \end{align} \]Calling


results in the COO row indices array:[hipsparseXcsr2coo()](#hipsparse__csr2coo_8h_1a445e0da18bc0faf111aaa05cc7706600)\[ \begin{align} \text{cooRowInd} &= \begin{bmatrix} 0 & 1 & 1 & 2 \end{bmatrix} \end{align} \]Note

It can also be used to convert a CSC array containing the column offsets into a COO array of column indices.

Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**csrRowPtr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**m**–**[in]**number of rows of the sparse CSR matrix.**cooRowInd**–**[out]**array of`nnz`

elements containing the row indices of the sparse COO matrix.**idxBase**–**[in]**[HIPSPARSE_INDEX_BASE_ZERO](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4a14913ab324aaea1154abd00ee7c50b63)or[HIPSPARSE_INDEX_BASE_ONE](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4ae48a9ab138ca9588d485c078bddc0792).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`nnz`

,`csrRowPtr`

or`cooRowInd`

pointer is invalid.**HIPSPARSE_STATUS_ARCH_MISMATCH**– the device is not supported.



## hipsparseXcsr2csc()[#](#hipsparsexcsr2csc)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseScsr2csc([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnz, const float *csrSortedVal, const int *csrSortedRowPtr, const int *csrSortedColInd, float *cscSortedVal, int *cscSortedRowInd, int *cscSortedColPtr,[hipsparseAction_t](types.html#_CPPv417hipsparseAction_t)copyValues,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase)[#](#_CPPv417hipsparseScsr2csc17hipsparseHandle_tiiiPKfPKiPKiPfPiPi17hipsparseAction_t20hipsparseIndexBase_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDcsr2csc([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnz, const double *csrSortedVal, const int *csrSortedRowPtr, const int *csrSortedColInd, double *cscSortedVal, int *cscSortedRowInd, int *cscSortedColPtr,[hipsparseAction_t](types.html#_CPPv417hipsparseAction_t)copyValues,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase)[#](#_CPPv417hipsparseDcsr2csc17hipsparseHandle_tiiiPKdPKiPKiPdPiPi17hipsparseAction_t20hipsparseIndexBase_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCcsr2csc([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnz, const hipComplex *csrSortedVal, const int *csrSortedRowPtr, const int *csrSortedColInd, hipComplex *cscSortedVal, int *cscSortedRowInd, int *cscSortedColPtr,[hipsparseAction_t](types.html#_CPPv417hipsparseAction_t)copyValues,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase)[#](#_CPPv417hipsparseCcsr2csc17hipsparseHandle_tiiiPK10hipComplexPKiPKiP10hipComplexPiPi17hipsparseAction_t20hipsparseIndexBase_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZcsr2csc([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnz, const hipDoubleComplex *csrSortedVal, const int *csrSortedRowPtr, const int *csrSortedColInd, hipDoubleComplex *cscSortedVal, int *cscSortedRowInd, int *cscSortedColPtr,[hipsparseAction_t](types.html#_CPPv417hipsparseAction_t)copyValues,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase)[#](#_CPPv417hipsparseZcsr2csc17hipsparseHandle_tiiiPK16hipDoubleComplexPKiPKiP16hipDoubleComplexPiPi17hipsparseAction_t20hipsparseIndexBase_t) Convert a sparse CSR matrix into a sparse CSC matrix.

`hipsparseXcsr2csc`

converts a CSR matrix into a CSC matrix.`hipsparseXcsr2csc`

can also be used to convert a CSC matrix into a CSR matrix.`copyValues`

decides whether`cscSortedVal`

is being filled during conversion ([HIPSPARSE_ACTION_NUMERIC](types.html#hipsparse-types_8h_1a728aa53636cea88149e375bf26bdeb75aab600a301578142c7551f7f10cbedf13)) or not ([HIPSPARSE_ACTION_SYMBOLIC](types.html#hipsparse-types_8h_1a728aa53636cea88149e375bf26bdeb75a9195a9de2db9ae0c39181db3fa297bb1)).For example given the matrix:

\[\begin{split} \begin{bmatrix} 1 & 0 & 0 & 2 \\ 3 & 4 & 0 & 0 \\ 5 & 0 & 6 & 7 \end{bmatrix} \end{split}\]Represented using the sparse CSR format as:

\[\begin{split} \begin{align} \text{csrSortedRowPtr} &= \begin{bmatrix} 0 & 2 & 4 & 7 \end{bmatrix} \\ \text{csrSortedColInd} &= \begin{bmatrix} 0 & 3 & 0 & 1 & 0 & 2 & 3 \end{bmatrix} \\ \text{csrSortedVal} &= \begin{bmatrix} 1 & 2 & 3 & 4 & 5 & 6 & 7 \end{bmatrix} \end{align} \end{split}\]this function converts to sparse CSC format:

\[\begin{split} \begin{align} \text{cscSortedRowInd} &= \begin{bmatrix} 0 & 1 & 2 & 1 & 2 & 0 & 2 \end{bmatrix} \\ \text{cscSortedColPtr} &= \begin{bmatrix} 0 & 3 & 4 & 5 & 7 \end{bmatrix} \\ \text{cscSortedVal} &= \begin{bmatrix} 1 & 3 & 5 & 4 & 6 & 2 & 7 \end{bmatrix} \end{align} \end{split}\]The CSC arrays,

`cscSortedRowInd`

,`cscSortedColPtr`

, and`cscSortedVal`

must be allocated by the user prior to calling`hipsparseXcsr2csc()`

.**Example**int main(int argc, char* argv[]) { // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // Sparse matrix in CSR format // 1 2 0 3 0 // A = 0 4 5 0 0 // 6 0 0 7 8 int hcsrRowPtr[4] = {0, 3, 5, 8}; int hcsrColInd[8] = {0, 1, 3, 1, 2, 0, 3, 4}; float hcsrVal[8] = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f}; int m = 3; int n = 5; int nnz = 8; hipsparseIndexBase_t base = HIPSPARSE_INDEX_BASE_ZERO; hipsparseAction_t action = HIPSPARSE_ACTION_NUMERIC; int* dcsrRowPtr = nullptr; int* dcsrColInd = nullptr; float* dcsrVal = nullptr; HIP_CHECK(hipMalloc((void**)&dcsrRowPtr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&dcsrColInd, sizeof(int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcsrVal, sizeof(float) * nnz)); HIP_CHECK(hipMemcpy(dcsrRowPtr, hcsrRowPtr, sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrColInd, hcsrColInd, sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrVal, hcsrVal, sizeof(float) * nnz, hipMemcpyHostToDevice)); int* dcscRowInd = nullptr; int* dcscColPtr = nullptr; float* dcsc_val = nullptr; HIP_CHECK(hipMalloc((void**)&dcscRowInd, sizeof(int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcscColPtr, sizeof(int) * (n + 1))); HIP_CHECK(hipMalloc((void**)&dcsc_val, sizeof(float) * nnz)); HIPSPARSE_CHECK(hipsparseScsr2csc(handle, m, n, nnz, dcsrVal, dcsrRowPtr, dcsrColInd, dcsc_val, dcscRowInd, dcscColPtr, action, base)); HIP_CHECK(hipFree(dcsrRowPtr)); HIP_CHECK(hipFree(dcsrColInd)); HIP_CHECK(hipFree(dcsrVal)); HIP_CHECK(hipFree(dcscRowInd)); HIP_CHECK(hipFree(dcscColPtr)); HIP_CHECK(hipFree(dcsc_val)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); return 0; }


Note

The resulting matrix can also be seen as the transpose of the input matrix.

Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix.**n**–**[in]**number of columns of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**csrSortedVal**–**[in]**array of`nnz`

elements of the sparse CSR matrix.**csrSortedRowPtr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csrSortedColInd**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**cscSortedVal**–**[out]**array of`nnz`

elements of the sparse CSC matrix.**cscSortedRowInd**–**[out]**array of`nnz`

elements containing the row indices of the sparse CSC matrix.**cscSortedColPtr**–**[out]**array of`n+1`

elements that point to the start of every column of the sparse CSC matrix.**copyValues**–**[in]**[HIPSPARSE_ACTION_SYMBOLIC](types.html#hipsparse-types_8h_1a728aa53636cea88149e375bf26bdeb75a9195a9de2db9ae0c39181db3fa297bb1)or[HIPSPARSE_ACTION_NUMERIC](types.html#hipsparse-types_8h_1a728aa53636cea88149e375bf26bdeb75aab600a301578142c7551f7f10cbedf13).**idxBase**–**[in]**[HIPSPARSE_INDEX_BASE_ZERO](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4a14913ab324aaea1154abd00ee7c50b63)or[HIPSPARSE_INDEX_BASE_ONE](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4ae48a9ab138ca9588d485c078bddc0792).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`nnz`

,`csrSortedVal`

,`csrSortedRowPtr`

,`csrSortedColInd`

,`cscSortedVal`

,`cscSortedRowInd`

or`cscSortedColPtr`

pointer is invalid.**HIPSPARSE_STATUS_ARCH_MISMATCH**– the device is not supported.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.



## hipsparseXcsr2cscEx2_bufferSize()[#](#hipsparsexcsr2cscex2-buffersize)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCsr2cscEx2_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnz, const void *csrVal, const int *csrRowPtr, const int *csrColInd, void *cscVal, int *cscColPtr, int *cscRowInd, hipDataType valType,[hipsparseAction_t](types.html#_CPPv417hipsparseAction_t)copyValues,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase,[hipsparseCsr2CscAlg_t](types.html#_CPPv421hipsparseCsr2CscAlg_t)alg, size_t *pBufferSizeInBytes)[#](#_CPPv430hipsparseCsr2cscEx2_bufferSize17hipsparseHandle_tiiiPKvPKiPKiPvPiPi11hipDataType17hipsparseAction_t20hipsparseIndexBase_t21hipsparseCsr2CscAlg_tP6size_t) This function computes the size of the user allocated temporary storage buffer used when converting a sparse CSR matrix into a sparse CSC matrix.

`hipsparseCsr2cscEx2_bufferSize`

calculates the required user allocated temporary buffer needed by[hipsparseCsr2cscEx2](#hipsparse__csr2csc_8h_1a091d6b107db830512171e38ea51a54e6)to convert a CSR matrix into a CSC matrix.[hipsparseCsr2cscEx2](#hipsparse__csr2csc_8h_1a091d6b107db830512171e38ea51a54e6)can also be used to convert a CSC matrix into a CSR matrix.`copyValues`

decides whether`cscVal`

is being filled during conversion ([HIPSPARSE_ACTION_NUMERIC](types.html#hipsparse-types_8h_1a728aa53636cea88149e375bf26bdeb75aab600a301578142c7551f7f10cbedf13)) or not ([HIPSPARSE_ACTION_SYMBOLIC](types.html#hipsparse-types_8h_1a728aa53636cea88149e375bf26bdeb75a9195a9de2db9ae0c39181db3fa297bb1)).Note

The resulting matrix can also be seen as the transpose of the input matrix.

Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix.**n**–**[in]**number of columns of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**csrVal**–**[in]**array of`nnz`

elements of the sparse CSR matrix.**csrRowPtr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csrColInd**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**cscVal**–**[in]**array of`nnz`

elements of the sparse CSC matrix.**cscColPtr**–**[in]**array of`n+1`

elements that point to the start of every column of the sparse CSC matrix.**cscRowInd**–**[in]**array of`nnz`

elements containing the row indices of the sparse CSC matrix.**valType**–**[in]**The data type of the values arrays`csrVal`

and`cscVal`

. Can be HIP_R_32F, HIP_R_64F, HIP_C_32F or HIP_C_64F**copyValues**–**[in]**[HIPSPARSE_ACTION_SYMBOLIC](types.html#hipsparse-types_8h_1a728aa53636cea88149e375bf26bdeb75a9195a9de2db9ae0c39181db3fa297bb1)or[HIPSPARSE_ACTION_NUMERIC](types.html#hipsparse-types_8h_1a728aa53636cea88149e375bf26bdeb75aab600a301578142c7551f7f10cbedf13).**idxBase**–**[in]**[HIPSPARSE_INDEX_BASE_ZERO](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4a14913ab324aaea1154abd00ee7c50b63)or[HIPSPARSE_INDEX_BASE_ONE](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4ae48a9ab138ca9588d485c078bddc0792).**alg**–**[in]**HIPSPARSE_CSR2CSC_ALG_DEFAULT, HIPSPARSE_CSR2CSC_ALG1 or HIPSPARSE_CSR2CSC_ALG2.**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer required by[hipsparseCsr2cscEx2()](#hipsparse__csr2csc_8h_1a091d6b107db830512171e38ea51a54e6).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`nnz`

,`csrRowPtr`

,`csrColInd`

or`pBufferSizeInBytes`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.



## hipsparseXcsr2cscEx2()[#](#hipsparsexcsr2cscex2)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCsr2cscEx2([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnz, const void *csrVal, const int *csrRowPtr, const int *csrColInd, void *cscVal, int *cscColPtr, int *cscRowInd, hipDataType valType,[hipsparseAction_t](types.html#_CPPv417hipsparseAction_t)copyValues,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase,[hipsparseCsr2CscAlg_t](types.html#_CPPv421hipsparseCsr2CscAlg_t)alg, void *buffer)[#](#_CPPv419hipsparseCsr2cscEx217hipsparseHandle_tiiiPKvPKiPKiPvPiPi11hipDataType17hipsparseAction_t20hipsparseIndexBase_t21hipsparseCsr2CscAlg_tPv) Convert a sparse CSR matrix into a sparse CSC matrix.

`hipsparseCsr2cscEx2`

converts a CSR matrix into a CSC matrix.`hipsparseCsr2cscEx2`

can also be used to convert a CSC matrix into a CSR matrix.`copyValues`

decides whether`cscVal`

is being filled during conversion ([HIPSPARSE_ACTION_NUMERIC](types.html#hipsparse-types_8h_1a728aa53636cea88149e375bf26bdeb75aab600a301578142c7551f7f10cbedf13)) or not ([HIPSPARSE_ACTION_SYMBOLIC](types.html#hipsparse-types_8h_1a728aa53636cea88149e375bf26bdeb75a9195a9de2db9ae0c39181db3fa297bb1)).**Example**int main(int argc, char* argv[]) { // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // Sparse matrix in CSR format // 1 2 0 3 0 // A = 0 4 5 0 0 // 6 0 0 7 8 int hcsrRowPtr[4] = {0, 3, 5, 8}; int hcsrColInd[8] = {0, 1, 3, 1, 2, 0, 3, 4}; float hcsrVal[8] = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f}; int m = 3; int n = 5; int nnz = 8; hipsparseIndexBase_t base = HIPSPARSE_INDEX_BASE_ZERO; hipsparseAction_t action = HIPSPARSE_ACTION_NUMERIC; hipsparseCsr2CscAlg_t alg = HIPSPARSE_CSR2CSC_ALG_DEFAULT; int* dcsrRowPtr = nullptr; int* dcsrColInd = nullptr; float* dcsrVal = nullptr; HIP_CHECK(hipMalloc((void**)&dcsrRowPtr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&dcsrColInd, sizeof(int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcsrVal, sizeof(float) * nnz)); HIP_CHECK(hipMemcpy(dcsrRowPtr, hcsrRowPtr, sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrColInd, hcsrColInd, sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrVal, hcsrVal, sizeof(float) * nnz, hipMemcpyHostToDevice)); int* dcscRowInd = nullptr; int* dcscColPtr = nullptr; float* dcsc_val = nullptr; HIP_CHECK(hipMalloc((void**)&dcscRowInd, sizeof(int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcscColPtr, sizeof(int) * (n + 1))); HIP_CHECK(hipMalloc((void**)&dcsc_val, sizeof(float) * nnz)); size_t bufferSize; HIPSPARSE_CHECK(hipsparseCsr2cscEx2_bufferSize(handle, m, n, nnz, dcsrVal, dcsrRowPtr, dcsrColInd, dcsc_val, dcscColPtr, dcscRowInd, HIP_R_32F, action, base, alg, &bufferSize)); void* dbuffer = nullptr; HIP_CHECK(hipMalloc((void**)&dbuffer, bufferSize)); HIPSPARSE_CHECK(hipsparseCsr2cscEx2(handle, m, n, nnz, dcsrVal, dcsrRowPtr, dcsrColInd, dcsc_val, dcscColPtr, dcscRowInd, HIP_R_32F, action, base, alg, dbuffer)); HIP_CHECK(hipFree(dcsrRowPtr)); HIP_CHECK(hipFree(dcsrColInd)); HIP_CHECK(hipFree(dcsrVal)); HIP_CHECK(hipFree(dcscRowInd)); HIP_CHECK(hipFree(dcscColPtr)); HIP_CHECK(hipFree(dcsc_val)); HIP_CHECK(hipFree(dbuffer)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); return 0; }


Note

The resulting matrix can also be seen as the transpose of the input matrix.

Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix.**n**–**[in]**number of columns of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**csrVal**–**[in]**array of`nnz`

elements of the sparse CSR matrix.**csrRowPtr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csrColInd**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**cscVal**–**[in]**array of`nnz`

elements of the sparse CSC matrix.**cscColPtr**–**[in]**array of`n+1`

elements that point to the start of every column of the sparse CSC matrix.**cscRowInd**–**[in]**array of`nnz`

elements containing the row indices of the sparse CSC matrix.**valType**–**[in]**The data type of the values arrays`csrVal`

and`cscVal`

. Can be HIP_R_32F, HIP_R_64F, HIP_C_32F or HIP_C_64F**copyValues**–**[in]**[HIPSPARSE_ACTION_SYMBOLIC](types.html#hipsparse-types_8h_1a728aa53636cea88149e375bf26bdeb75a9195a9de2db9ae0c39181db3fa297bb1)or[HIPSPARSE_ACTION_NUMERIC](types.html#hipsparse-types_8h_1a728aa53636cea88149e375bf26bdeb75aab600a301578142c7551f7f10cbedf13).**idxBase**–**[in]**[HIPSPARSE_INDEX_BASE_ZERO](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4a14913ab324aaea1154abd00ee7c50b63)or[HIPSPARSE_INDEX_BASE_ONE](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4ae48a9ab138ca9588d485c078bddc0792).**alg**–**[in]**HIPSPARSE_CSR2CSC_ALG_DEFAULT, HIPSPARSE_CSR2CSC_ALG1 or HIPSPARSE_CSR2CSC_ALG2.**buffer**–**[in]**temporary storage buffer allocated by the user, size is returned by[hipsparseCsr2cscEx2_bufferSize()](#hipsparse__csr2csc_8h_1a9508f6d010bacdb65cb0b3b29f9e75cf).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`nnz`

,`csrRowPtr`

,`csrColInd`

or`pBufferSizeInBytes`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.



## hipsparseXcsr2hyb()[#](#hipsparsexcsr2hyb)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseScsr2hyb([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const float *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[hipsparseHybMat_t](types.html#_CPPv417hipsparseHybMat_t)hybA, int userEllWidth,[hipsparseHybPartition_t](types.html#_CPPv423hipsparseHybPartition_t)partitionType)[#](#_CPPv417hipsparseScsr2hyb17hipsparseHandle_tiiK19hipsparseMatDescr_tPKfPKiPKi17hipsparseHybMat_ti23hipsparseHybPartition_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDcsr2hyb([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const double *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[hipsparseHybMat_t](types.html#_CPPv417hipsparseHybMat_t)hybA, int userEllWidth,[hipsparseHybPartition_t](types.html#_CPPv423hipsparseHybPartition_t)partitionType)[#](#_CPPv417hipsparseDcsr2hyb17hipsparseHandle_tiiK19hipsparseMatDescr_tPKdPKiPKi17hipsparseHybMat_ti23hipsparseHybPartition_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCcsr2hyb([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipComplex *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[hipsparseHybMat_t](types.html#_CPPv417hipsparseHybMat_t)hybA, int userEllWidth,[hipsparseHybPartition_t](types.html#_CPPv423hipsparseHybPartition_t)partitionType)[#](#_CPPv417hipsparseCcsr2hyb17hipsparseHandle_tiiK19hipsparseMatDescr_tPK10hipComplexPKiPKi17hipsparseHybMat_ti23hipsparseHybPartition_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZcsr2hyb([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipDoubleComplex *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[hipsparseHybMat_t](types.html#_CPPv417hipsparseHybMat_t)hybA, int userEllWidth,[hipsparseHybPartition_t](types.html#_CPPv423hipsparseHybPartition_t)partitionType)[#](#_CPPv417hipsparseZcsr2hyb17hipsparseHandle_tiiK19hipsparseMatDescr_tPK16hipDoubleComplexPKiPKi17hipsparseHybMat_ti23hipsparseHybPartition_t) Convert a sparse CSR matrix into a sparse HYB matrix.

`hipsparseXcsr2hyb`

converts a CSR matrix into a HYB matrix. It is assumed that`hyb`

has been initialized with[hipsparseCreateHybMat()](auxiliary.html#hipsparse-auxiliary_8h_1ab0a4ae83034f87cff9c9405150261648).**Example**int main(int argc, char* argv[]) { // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); hipsparseMatDescr_t descr; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&descr)); // Sparse matrix in CSR format // 1 2 0 3 0 // A = 0 4 5 0 0 // 6 0 0 7 8 int hcsrRowPtr[4] = {0, 3, 5, 8}; int hcsrColInd[8] = {0, 1, 3, 1, 2, 0, 3, 4}; float hcsrVal[8] = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f}; int m = 3; int n = 5; int nnz = 8; int userEllWidth = 2; hipsparseHybPartition_t partitionType = HIPSPARSE_HYB_PARTITION_AUTO; int* dcsrRowPtr = nullptr; int* dcsrColInd = nullptr; float* dcsrVal = nullptr; HIP_CHECK(hipMalloc((void**)&dcsrRowPtr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&dcsrColInd, sizeof(int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcsrVal, sizeof(float) * nnz)); HIP_CHECK(hipMemcpy(dcsrRowPtr, hcsrRowPtr, sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrColInd, hcsrColInd, sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrVal, hcsrVal, sizeof(float) * nnz, hipMemcpyHostToDevice)); hipsparseHybMat_t hyb; HIPSPARSE_CHECK(hipsparseCreateHybMat(&hyb)); HIPSPARSE_CHECK(hipsparseScsr2hyb( handle, m, n, descr, dcsrVal, dcsrRowPtr, dcsrColInd, hyb, userEllWidth, partitionType)); HIP_CHECK(hipFree(dcsrRowPtr)); HIP_CHECK(hipFree(dcsrColInd)); HIP_CHECK(hipFree(dcsrVal)); HIPSPARSE_CHECK(hipsparseDestroyHybMat(hyb)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(descr)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); return 0; }


Note

This function requires a significant amount of storage for the HYB matrix, depending on the matrix structure.

Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix.**n**–**[in]**number of columns of the sparse CSR matrix.**descrA**–**[in]**descriptor of the sparse CSR matrix. Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**csrSortedValA**–**[in]**array containing the values of the sparse CSR matrix.**csrSortedRowPtrA**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csrSortedColIndA**–**[in]**array containing the column indices of the sparse CSR matrix.**hybA**–**[out]**sparse matrix in HYB format.**userEllWidth**–**[in]**width of the ELL part of the HYB matrix (only required if`partitionType`

==[HIPSPARSE_HYB_PARTITION_USER](types.html#hipsparse-types_8h_1a982aa7c059922aafb1f77bfc868a460fa8dcbb0790495944d5924c3781a048800)).**partitionType**–**[in]**[HIPSPARSE_HYB_PARTITION_AUTO](types.html#hipsparse-types_8h_1a982aa7c059922aafb1f77bfc868a460fa48e6d1a15949afdbed7033da76f2952c)(recommended),[HIPSPARSE_HYB_PARTITION_USER](types.html#hipsparse-types_8h_1a982aa7c059922aafb1f77bfc868a460fa8dcbb0790495944d5924c3781a048800)or[HIPSPARSE_HYB_PARTITION_MAX](types.html#hipsparse-types_8h_1a982aa7c059922aafb1f77bfc868a460fa23ceac98ac46e11a18da5cd912c3eca6).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`userEllWidth`

,`partitionType`

,`descrA`

,`hybA`

,`csrSortedValA`

,`csrSortedRowPtrA`

or`csrSortedColIndA`

pointer is invalid.**HIPSPARSE_STATUS_ALLOC_FAILED**– the buffer for the HYB matrix could not be allocated.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.**HIPSPARSE_STATUS_NOT_SUPPORTED**–[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXgebsr2gebsc_bufferSize()[#](#hipsparsexgebsr2gebsc-buffersize)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSgebsr2gebsc_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int mb, int nb, int nnzb, const float *bsrVal, const int *bsrRowPtr, const int *bsrColInd, int rowBlockDim, int colBlockDim, size_t *pBufferSizeInBytes)[#](#_CPPv432hipsparseSgebsr2gebsc_bufferSize17hipsparseHandle_tiiiPKfPKiPKiiiP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDgebsr2gebsc_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int mb, int nb, int nnzb, const double *bsrVal, const int *bsrRowPtr, const int *bsrColInd, int rowBlockDim, int colBlockDim, size_t *pBufferSizeInBytes)[#](#_CPPv432hipsparseDgebsr2gebsc_bufferSize17hipsparseHandle_tiiiPKdPKiPKiiiP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCgebsr2gebsc_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int mb, int nb, int nnzb, const hipComplex *bsrVal, const int *bsrRowPtr, const int *bsrColInd, int rowBlockDim, int colBlockDim, size_t *pBufferSizeInBytes)[#](#_CPPv432hipsparseCgebsr2gebsc_bufferSize17hipsparseHandle_tiiiPK10hipComplexPKiPKiiiP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZgebsr2gebsc_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int mb, int nb, int nnzb, const hipDoubleComplex *bsrVal, const int *bsrRowPtr, const int *bsrColInd, int rowBlockDim, int colBlockDim, size_t *pBufferSizeInBytes)[#](#_CPPv432hipsparseZgebsr2gebsc_bufferSize17hipsparseHandle_tiiiPK16hipDoubleComplexPKiPKiiiP6size_t) Convert a sparse GEBSR matrix into a sparse GEBSC matrix.

`hipsparseXgebsr2gebsc_bufferSize`

returns the size of the temporary storage buffer required by[hipsparseXgebsr2gebsc()](#hipsparse__gebsr2gebsc_8h_1abf98470b5448d73d75ac92517f6d755e)and is the first step in converting a sparse matrix in GEBSR format to a sparse matrix in GEBSC format. Once the size of the temporary storage buffer has been determined, it must be allocated by the user.See

[hipsparseSgebsr2gebsc()](#hipsparse__gebsr2gebsc_8h_1abf98470b5448d73d75ac92517f6d755e)for a complete code example.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**mb**–**[in]**number of rows of the sparse GEneral BSR matrix.**nb**–**[in]**number of columns of the sparse GEneral BSR matrix.**nnzb**–**[in]**number of non-zero entries of the sparse GEneral BSR matrix.**bsrVal**–**[in]**array of`nnzb*rowBlockDim*colBlockDim`

containing the values of the sparse GEneral BSR matrix.**bsrRowPtr**–**[in]**array of`mb+1`

elements that point to the start of every row of the sparse GEneral BSR matrix.**bsrColInd**–**[in]**array of`nnzb`

elements containing the column indices of the sparse GEneral BSR matrix.**rowBlockDim**–**[in]**row size of the blocks in the sparse general BSR matrix.**colBlockDim**–**[in]**col size of the blocks in the sparse general BSR matrix.**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer required by[hipsparseSgebsr2gebsc()](#hipsparse__gebsr2gebsc_8h_1abf98470b5448d73d75ac92517f6d755e),[hipsparseDgebsr2gebsc()](#hipsparse__gebsr2gebsc_8h_1aebbec9720b09fe27c3713b97c31fab01),[hipsparseCgebsr2gebsc()](#hipsparse__gebsr2gebsc_8h_1a123af996e87efd7d4dcd1da129badbf0)and[hipsparseZgebsr2gebsc()](#hipsparse__gebsr2gebsc_8h_1a43cbb17bb28bd6794416a783598fbdee).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`mb`

,`nb`

,`nnzb`

,`bsrRowPtr`

,`bsrColInd`

or`pBufferSizeInBytes`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.



## hipsparseXgebsr2gebsc()[#](#hipsparsexgebsr2gebsc)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSgebsr2gebsc([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int mb, int nb, int nnzb, const float *bsrVal, const int *bsrRowPtr, const int *bsrColInd, int rowBlockDim, int colBlockDim, float *bscVal, int *bscRowInd, int *bscColPtr,[hipsparseAction_t](types.html#_CPPv417hipsparseAction_t)copyValues,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase, void *temp_buffer)[#](#_CPPv421hipsparseSgebsr2gebsc17hipsparseHandle_tiiiPKfPKiPKiiiPfPiPi17hipsparseAction_t20hipsparseIndexBase_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDgebsr2gebsc([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int mb, int nb, int nnzb, const double *bsrVal, const int *bsrRowPtr, const int *bsrColInd, int rowBlockDim, int colBlockDim, double *bscVal, int *bscRowInd, int *bscColPtr,[hipsparseAction_t](types.html#_CPPv417hipsparseAction_t)copyValues,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase, void *temp_buffer)[#](#_CPPv421hipsparseDgebsr2gebsc17hipsparseHandle_tiiiPKdPKiPKiiiPdPiPi17hipsparseAction_t20hipsparseIndexBase_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCgebsr2gebsc([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int mb, int nb, int nnzb, const hipComplex *bsrVal, const int *bsrRowPtr, const int *bsrColInd, int rowBlockDim, int colBlockDim, hipComplex *bscVal, int *bscRowInd, int *bscColPtr,[hipsparseAction_t](types.html#_CPPv417hipsparseAction_t)copyValues,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase, void *temp_buffer)[#](#_CPPv421hipsparseCgebsr2gebsc17hipsparseHandle_tiiiPK10hipComplexPKiPKiiiP10hipComplexPiPi17hipsparseAction_t20hipsparseIndexBase_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZgebsr2gebsc([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int mb, int nb, int nnzb, const hipDoubleComplex *bsrVal, const int *bsrRowPtr, const int *bsrColInd, int rowBlockDim, int colBlockDim, hipDoubleComplex *bscVal, int *bscRowInd, int *bscColPtr,[hipsparseAction_t](types.html#_CPPv417hipsparseAction_t)copyValues,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase, void *temp_buffer)[#](#_CPPv421hipsparseZgebsr2gebsc17hipsparseHandle_tiiiPK16hipDoubleComplexPKiPKiiiP16hipDoubleComplexPiPi17hipsparseAction_t20hipsparseIndexBase_tPv) Convert a sparse GEBSR matrix into a sparse GEBSC matrix.

`hipsparseXgebsr2gebsc`

converts a GEBSR matrix into a GEBSC matrix.`hipsparseXgebsr2gebsc`

can also be used to convert a GEBSC matrix into a GEBSR matrix.`copyValues`

decides whether`bscVal`

is being filled during conversion ([HIPSPARSE_ACTION_NUMERIC](types.html#hipsparse-types_8h_1a728aa53636cea88149e375bf26bdeb75aab600a301578142c7551f7f10cbedf13)) or not ([HIPSPARSE_ACTION_SYMBOLIC](types.html#hipsparse-types_8h_1a728aa53636cea88149e375bf26bdeb75a9195a9de2db9ae0c39181db3fa297bb1)).`hipsparseXgebsr2gebsc`

requires extra temporary storage buffer that has to be allocated by the user. Storage buffer size can be determined by[hipsparseXgebsr2gebsc_bufferSize()](#hipsparse__gebsr2gebsc_8h_1a4d20dd4e735f7e7f541a87f7bd7b458a).For example, given the GEBSR matrix:

\[\begin{split} \left[ \begin{array}{c | c} \begin{array}{c c} 1 & 2 \\ 3 & 4 \\ 6 & 0 \end{array} & \begin{array}{c c} 0 & 2 \\ 0 & 0 \\ 3 & 4 \end{array} \\ \hline \begin{array}{c c} 5 & 0 \\ 1 & 2 \\ 3 & 4 \end{array} & \begin{array}{c c} 6 & 7 \\ 3 & 4 \\ 3 & 4 \end{array} \\ \end{array} \right] \end{split}\]represented with the arrays:

\[\begin{split} \begin{align} \text{bsrRowPtr} &= \begin{bmatrix} 0 & 2 & 4 \end{bmatrix} \\ \text{bsrColInd} &= \begin{bmatrix} 0 & 1 & 0 & 1 \end{bmatrix} \\ \text{bsrVal} &= \begin{bmatrix} 1 & 2 & 3 & 4 & 6 & 0 & 0 & 2 & 0 & 0 & 3 & 4 & 5 & 0 & 1 & 2 & 3 & 4 & 6 & 7 & 3 & 4 & 3 & 4 \end{bmatrix} \end{align} \end{split}\]this function converts the matrix to GEBSC format:

\[\begin{split} \begin{align} \text{bscRowInd} &= \begin{bmatrix} 0 & 1 & 0 & 1 \end{bmatrix} \\ \text{bscColPtr} &= \begin{bmatrix} 0 & 2 & 4 \end{bmatrix} \\ \text{bscVal} &= \begin{bmatrix} 1 & 2 & 3 & 4 & 6 & 0 & 5 & 0 & 1 & 2 & 3 & 4 & 0 & 2 & 0 & 0 & 3 & 4 & 6 & 7 & 3 & 4 & 3 & 4 \end{bmatrix} \end{align} \end{split}\]The GEBSC arrays,

`bscRowInd`

,`bscColPtr`

, and`bscVal`

must be allocated by the user prior to calling`hipsparseXgebsr2gebsc()`

. The`bscRowInd`

array has size`nnzb`

, the`bscColPtr`

array has size`nb+1`

, and the`bscVal`

array has size`nnzb*rowBlockDim*colBlockDim`

.**Example**int main(int argc, char* argv[]) { // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // Sparse matrix in BSR format // 1 2 | 0 3 | 0 0 // 0 4 | 5 0 | 0 1 // A = 6 0 | 0 7 | 8 0 // --------------- // 0 0 | 3 0 | 2 2 // 1 0 | 0 0 | 4 3 // 7 2 | 0 0 | 1 4 int hbsrRowPtr[3] = {0, 3, 6}; int hbsrColInd[6] = {0, 1, 2, 0, 1, 2}; float hbsrVal[36] = {1.0f, 2.0f, 0.0f, 4.0f, 6.0f, 0.0f, 0.0f, 3.0f, 5.0f, 0.0f, 0.0f, 7.0f, 0.0f, 0.0f, 0.0f, 1.0f, 8.0f, 0.0f, 0.0f, 0.0f, 1.0f, 0.0f, 7.0f, 2.0f, 3.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 2.0f, 2.0f, 4.0f, 3.0f, 1.0f, 4.0f}; int m = 6; int n = 6; int rowBlockDim = 3; int colBlockDim = 2; int nnzb = 6; hipsparseDirection_t dir = HIPSPARSE_DIRECTION_ROW; hipsparseAction_t action = HIPSPARSE_ACTION_NUMERIC; hipsparseIndexBase_t base = HIPSPARSE_INDEX_BASE_ZERO; int mb = (m + rowBlockDim - 1) / rowBlockDim; int nb = (n + colBlockDim - 1) / colBlockDim; int* dbsrRowPtr = nullptr; int* dbsrColInd = nullptr; float* dbsrVal = nullptr; HIP_CHECK(hipMalloc((void**)&dbsrRowPtr, sizeof(int) * (mb + 1))); HIP_CHECK(hipMalloc((void**)&dbsrColInd, sizeof(int) * nnzb)); HIP_CHECK(hipMalloc((void**)&dbsrVal, sizeof(float) * rowBlockDim * colBlockDim * nnzb)); HIP_CHECK(hipMemcpy(dbsrRowPtr, hbsrRowPtr, sizeof(int) * (mb + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dbsrColInd, hbsrColInd, sizeof(int) * nnzb, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( dbsrVal, hbsrVal, sizeof(float) * rowBlockDim * colBlockDim * nnzb, hipMemcpyHostToDevice)); int* dbscRowInd = nullptr; int* dbscColPtr = nullptr; float* dbscVal = nullptr; HIP_CHECK(hipMalloc((void**)&dbscRowInd, sizeof(int) * nnzb)); HIP_CHECK(hipMalloc((void**)&dbscColPtr, sizeof(int) * (nb + 1))); HIP_CHECK(hipMalloc((void**)&dbscVal, sizeof(float) * rowBlockDim * colBlockDim * nnzb)); size_t bufferSize; HIPSPARSE_CHECK(hipsparseSgebsr2gebsc_bufferSize(handle, mb, nb, nnzb, dbsrVal, dbsrRowPtr, dbsrColInd, rowBlockDim, colBlockDim, &bufferSize)); void* dbuffer = nullptr; HIP_CHECK(hipMalloc((void**)&dbuffer, bufferSize)); HIPSPARSE_CHECK(hipsparseSgebsr2gebsc(handle, mb, nb, nnzb, dbsrVal, dbsrRowPtr, dbsrColInd, rowBlockDim, colBlockDim, dbscVal, dbscRowInd, dbscColPtr, action, base, dbuffer)); HIP_CHECK(hipFree(dbsrRowPtr)); HIP_CHECK(hipFree(dbsrColInd)); HIP_CHECK(hipFree(dbsrVal)); HIP_CHECK(hipFree(dbscRowInd)); HIP_CHECK(hipFree(dbscColPtr)); HIP_CHECK(hipFree(dbscVal)); HIP_CHECK(hipFree(dbuffer)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); return 0; }


Note

The resulting matrix can also be seen as the transpose of the input matrix.

Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**mb**–**[in]**number of rows of the sparse GEneral BSR matrix.**nb**–**[in]**number of columns of the sparse GEneral BSR matrix.**nnzb**–**[in]**number of non-zero entries of the sparse GEneral BSR matrix.**bsrVal**–**[in]**array of`nnzb`

*`rowBlockDim`

*`colBlockDim`

elements of the sparse GEneral BSR matrix.**bsrRowPtr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse GEneral BSR matrix.**bsrColInd**–**[in]**array of`nnz`

elements containing the column indices of the sparse GEneral BSR matrix.**rowBlockDim**–**[in]**row size of the blocks in the sparse general BSR matrix.**colBlockDim**–**[in]**col size of the blocks in the sparse general BSR matrix.**bscVal**–**[out]**array of`nnz`

elements of the sparse BSC matrix.**bscRowInd**–**[out]**array of`nnz`

elements containing the row indices of the sparse BSC matrix.**bscColPtr**–**[out]**array of`n+1`

elements that point to the start of every column of the sparse BSC matrix.**copyValues**–**[in]**[HIPSPARSE_ACTION_SYMBOLIC](types.html#hipsparse-types_8h_1a728aa53636cea88149e375bf26bdeb75a9195a9de2db9ae0c39181db3fa297bb1)or[HIPSPARSE_ACTION_NUMERIC](types.html#hipsparse-types_8h_1a728aa53636cea88149e375bf26bdeb75aab600a301578142c7551f7f10cbedf13).**idxBase**–**[in]**[HIPSPARSE_INDEX_BASE_ZERO](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4a14913ab324aaea1154abd00ee7c50b63)or[HIPSPARSE_INDEX_BASE_ONE](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4ae48a9ab138ca9588d485c078bddc0792).**temp_buffer**–**[in]**temporary storage buffer allocated by the user, size is returned by[hipsparseXgebsr2gebsc_bufferSize()](#hipsparse__gebsr2gebsc_8h_1a4d20dd4e735f7e7f541a87f7bd7b458a).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`mb`

,`nb`

,`nnzb`

,`bsrVal`

,`bsrRowPtr`

,`bsrColInd`

,`bscVal`

,`bscRowInd`

,`bscColPtr`

or`temp_buffer`

pointer is invalid.**HIPSPARSE_STATUS_ARCH_MISMATCH**– the device is not supported.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.



## hipsparseXcsr2gebsr_bufferSize()[#](#hipsparsexcsr2gebsr-buffersize)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseScsr2gebsr_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dir, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)csr_descr, const float *csrVal, const int *csrRowPtr, const int *csrColInd, int rowBlockDim, int colBlockDim, size_t *pBufferSizeInBytes)[#](#_CPPv430hipsparseScsr2gebsr_bufferSize17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPKfPKiPKiiiP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDcsr2gebsr_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dir, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)csr_descr, const double *csrVal, const int *csrRowPtr, const int *csrColInd, int rowBlockDim, int colBlockDim, size_t *pBufferSizeInBytes)[#](#_CPPv430hipsparseDcsr2gebsr_bufferSize17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPKdPKiPKiiiP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCcsr2gebsr_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dir, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)csr_descr, const hipComplex *csrVal, const int *csrRowPtr, const int *csrColInd, int rowBlockDim, int colBlockDim, size_t *pBufferSizeInBytes)[#](#_CPPv430hipsparseCcsr2gebsr_bufferSize17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPK10hipComplexPKiPKiiiP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZcsr2gebsr_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dir, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)csr_descr, const hipDoubleComplex *csrVal, const int *csrRowPtr, const int *csrColInd, int rowBlockDim, int colBlockDim, size_t *pBufferSizeInBytes)[#](#_CPPv430hipsparseZcsr2gebsr_bufferSize17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPK16hipDoubleComplexPKiPKiiiP6size_t) Convert a sparse CSR matrix into a sparse GEBSR matrix.

`hipsparseXcsr2gebsr_bufferSize`

returns the size of the temporary buffer that is required by[hipsparseXcsr2gebsrNnz](#hipsparse__csr2gebsr_8h_1a260feed7bdabb3e436c6bcf2d836b6dd)and[hipsparseXcsr2gebsr()](#hipsparse__csr2gebsr_8h_1a62d852d6d7130e993f6f8860e7352b0f). Once the temporary buffer size has been determined, it must be allocated by the user prior to calling[hipsparseXcsr2gebsrNnz](#hipsparse__csr2gebsr_8h_1a260feed7bdabb3e436c6bcf2d836b6dd)and[hipsparseXcsr2gebsr()](#hipsparse__csr2gebsr_8h_1a62d852d6d7130e993f6f8860e7352b0f).See

[hipsparseScsr2gebsr()](#hipsparse__csr2gebsr_8h_1a62d852d6d7130e993f6f8860e7352b0f)for complete code example.Note

The routine does support asynchronous execution if the pointer mode is set to device.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**dir**–**[in]**direction that specified whether to count nonzero elements by[HIPSPARSE_DIRECTION_ROW](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59ae8589abecf2fbfb4b6307fd9dacd9e55)or by[HIPSPARSE_DIRECTION_COLUMN](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59a32e23f292b2377f6e60bdc90274c796c).**m**–**[in]**number of rows of the sparse CSR matrix.**n**–**[in]**number of columns of the sparse CSR matrix.**csr_descr**–**[in]**descriptor of the sparse CSR matrix. Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**csrVal**–**[in]**array of`nnz`

elements containing the values of the sparse CSR matrix.**csrRowPtr**–**[in]**integer array containing`m+1`

elements that point to the start of each row of the CSR matrix**csrColInd**–**[in]**integer array of the column indices for each non-zero element in the CSR matrix**rowBlockDim**–**[in]**the row block dimension of the GEneral BSR matrix. Between 1 and`m`

**colBlockDim**–**[in]**the col block dimension of the GEneral BSR matrix. Between 1 and`n`

**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer required by[hipsparseXcsr2gebsrNnz()](#hipsparse__csr2gebsr_8h_1a260feed7bdabb3e436c6bcf2d836b6dd)and[hipsparseXcsr2gebsr()](#hipsparse__csr2gebsr_8h_1a62d852d6d7130e993f6f8860e7352b0f).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`rowBlockDim`

,`colBlockDim`

,`csrVal`

,`csrRowPtr`

,`csrColInd`

or`pBufferSizeInBytes`

pointer is invalid.



## hipsparseXcsr2gebsrNnz()[#](#hipsparsexcsr2gebsrnnz)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseXcsr2gebsrNnz([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dir, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)csr_descr, const int *csrRowPtr, const int *csrColInd, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)bsr_descr, int *bsrRowPtr, int rowBlockDim, int colBlockDim, int *bsrNnzDevhost, void *pbuffer)[#](#_CPPv422hipsparseXcsr2gebsrNnz17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPKiPKiK19hipsparseMatDescr_tPiiiPiPv) This function computes the number of nonzero block columns per row and the total number of nonzero blocks in a sparse GEBSR matrix given a sparse CSR matrix as input.

This is the second step in conveting a CSR matrix to a GEBSR matrix. The user must first call

[hipsparseXcsr2gebsr_bufferSize()](#hipsparse__csr2gebsr_8h_1a7affde46e05e85ce8417ef756e8ac0df)to determine the size of the required temporary storage buffer. The user then allocates this buffer as well as the`bsrRowPtr`

array ( size`mb+1`

) and passes both to

. This second step then computes the number of nonzero block columns per row and the total number of nonzero blocks.[hipsparseXcsr2gebsrNnz()](#hipsparse__csr2gebsr_8h_1a260feed7bdabb3e436c6bcf2d836b6dd)In general, when converting a CSR matrix of size

`m`

x`n`

to a GEBSR matrix, the resulting GEBSR matrix will have size`mb`

x`nb`

where`mb`

and`nb`

equal:\[\begin{split} \begin{align} \text{mb} &= \text{(m - 1) / rowBlockDim + 1} \\ \text{nb} &= \text{(n - 1) / colBlockDim + 1} \end{align} \end{split}\]For example given a matrix:

\[\begin{split} \begin{bmatrix} 1 & 0 & 0 & 2 & 4 & 0 \\ 3 & 4 & 0 & 0 & 5 & 1 \\ 5 & 0 & 6 & 7 & 6 & 2 \end{bmatrix} \end{split}\]represented in CSR format with the arrays:

\[\begin{split} \begin{align} \text{csrRowPtr} &= \begin{bmatrix} 0 & 3 & 7 & 12 \end{bmatrix} \\ \text{csrColInd} &= \begin{bmatrix} 0 & 3 & 4 & 0 & 1 & 4 & 5 & 0 & 2 & 3 & 4 & 5 \end{bmatrix} \\ \text{csrVal} &= \begin{bmatrix} 1 & 2 & 4 & 3 & 4 & 5 & 1 & 5 & 6 & 7 & 6 & 2 \end{bmatrix} \end{align} \end{split}\]the

`bsrRowPtr`

array and total nonzero block count will be filled with:\[\begin{split} \begin{align} \text{bsrRowPtr} &= \begin{bmatrix} 0 & 3 \end{bmatrix} \\ \text{*bsrNnzDevhost} &= 3 \end{align} \end{split}\]after calling

`hipsparseXcsr2gebsrNnz`

with`rowBlockDim=3`

and`colBlockDim=2`

.It may be the case that

`rowBlockDim`

does not divide evenly into`m`

and/or that`colBlockDim`

does not divide evenly into`n`

. In these cases, the CSR matrix is expanded in size in order to fit full GEBSR blocks. For example, using the original CSR matrix but this time with`rowBlockDim=2`

and`colBlockDim=3`

, the function`hipsparseXcsr2gebsrNnz`

computes the GEBSR row pointer array and total number of non-zero blocks for the GEBSR matrix:\[\begin{split} \left[ \begin{array}{c | c} \begin{array}{c c c} 1 & 0 & 0 \\ 3 & 4 & 0 \end{array} & \begin{array}{c c c} 2 & 4 & 0 \\ 0 & 5 & 1 \end{array} \\ \hline \begin{array}{c c c} 5 & 0 & 6 \\ 0 & 0 & 0 \end{array} & \begin{array}{c c c} 7 & 6 & 2 \\ 0 & 0 & 0 \end{array} \end{array} \right] \end{split}\]See

[hipsparseScsr2gebsr()](#hipsparse__csr2gebsr_8h_1a62d852d6d7130e993f6f8860e7352b0f)for full code example.Note

As indicated,

`bsrNnzDevhost`

can point either to host or device memory. This is controlled by setting the pointer mode. See[hipsparseSetPointerMode()](auxiliary.html#hipsparse-auxiliary_8h_1a7d876174f77e1f8f816781af1c3c667c).- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**dir**–**[in]**direction that specified whether to count nonzero elements by[HIPSPARSE_DIRECTION_ROW](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59ae8589abecf2fbfb4b6307fd9dacd9e55)or by[HIPSPARSE_DIRECTION_COLUMN](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59a32e23f292b2377f6e60bdc90274c796c).**m**–**[in]**number of rows of the sparse CSR matrix.**n**–**[in]**number of columns of the sparse CSR matrix.**csr_descr**–**[in]**descriptor of the sparse CSR matrix. Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**csrRowPtr**–**[in]**integer array containing`m+1`

elements that point to the start of each row of the CSR matrix**csrColInd**–**[in]**integer array of the column indices for each non-zero element in the CSR matrix**bsr_descr**–**[in]**descriptor of the sparse GEneral BSR matrix. Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**bsrRowPtr**–**[out]**integer array containing`mb+1`

elements that point to the start of each block row of the General BSR matrix**rowBlockDim**–**[in]**the row block dimension of the GEneral BSR matrix. Between \(1\) and \(\min(m, n)\)**colBlockDim**–**[in]**the col block dimension of the GEneral BSR matrix. Between \(1\) and \(\min(m, n)\)**bsrNnzDevhost**–**[out]**total number of nonzero elements in device or host memory.**pbuffer**–**[in]**buffer allocated by the user whose size is determined by calling[hipsparseXcsr2gebsr_bufferSize()](#hipsparse__csr2gebsr_8h_1a7affde46e05e85ce8417ef756e8ac0df).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`rowBlockDim`

,`colBlockDim`

,`csrRowPtr`

,`csrColInd`

,`bsrRowPtr`

or`bsrNnzDevhost`

pointer is invalid.



## hipsparseXcsr2gebsr()[#](#hipsparsexcsr2gebsr)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseScsr2gebsr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dir, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)csr_descr, const float *csrVal, const int *csrRowPtr, const int *csrColInd, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)bsr_descr, float *bsrVal, int *bsrRowPtr, int *bsrColInd, int rowBlockDim, int colBlockDim, void *pbuffer)[#](#_CPPv419hipsparseScsr2gebsr17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPKfPKiPKiK19hipsparseMatDescr_tPfPiPiiiPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDcsr2gebsr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dir, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)csr_descr, const double *csrVal, const int *csrRowPtr, const int *csrColInd, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)bsr_descr, double *bsrVal, int *bsrRowPtr, int *bsrColInd, int rowBlockDim, int colBlockDim, void *pbuffer)[#](#_CPPv419hipsparseDcsr2gebsr17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPKdPKiPKiK19hipsparseMatDescr_tPdPiPiiiPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCcsr2gebsr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dir, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)csr_descr, const hipComplex *csrVal, const int *csrRowPtr, const int *csrColInd, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)bsr_descr, hipComplex *bsrVal, int *bsrRowPtr, int *bsrColInd, int rowBlockDim, int colBlockDim, void *pbuffer)[#](#_CPPv419hipsparseCcsr2gebsr17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPK10hipComplexPKiPKiK19hipsparseMatDescr_tP10hipComplexPiPiiiPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZcsr2gebsr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dir, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)csr_descr, const hipDoubleComplex *csrVal, const int *csrRowPtr, const int *csrColInd, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)bsr_descr, hipDoubleComplex *bsrVal, int *bsrRowPtr, int *bsrColInd, int rowBlockDim, int colBlockDim, void *pbuffer)[#](#_CPPv419hipsparseZcsr2gebsr17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPK16hipDoubleComplexPKiPKiK19hipsparseMatDescr_tP16hipDoubleComplexPiPiiiPv) Convert a sparse CSR matrix into a sparse GEBSR matrix.

`hipsparseXcsr2gebsr`

converts a CSR matrix into a GEBSR matrix. It is assumed, that`bsrVal`

,`bsrColInd`

and`bsrRowPtr`

are allocated. Allocation size for`bsrRowPtr`

is computed as`mb+1`

where`mb`

is the number of block rows in the GEBSR matrix. The number of nonzero blocks in the resulting GEBSR matrix is computed using[hipsparseXcsr2gebsrNnz](#hipsparse__csr2gebsr_8h_1a260feed7bdabb3e436c6bcf2d836b6dd)which also fills in`bsrRowPtr`

.In more detail,

`hipsparseXcsr2gebsr`

is the third and final step on the conversion from CSR to GEBSR. The user first determines the size of the required user allocated temporary storage buffer using[hipsparseXcsr2gebsr_bufferSize()](#hipsparse__csr2gebsr_8h_1a7affde46e05e85ce8417ef756e8ac0df). The user then allocates this buffer as well as the row pointer array`bsrRowPtr`

with size`mb+1`

, where`mb`

is the number of block rows in the GEBSR matrix and`nb`

is the number of block columns in GEBSR matrix:\[\begin{split} \begin{align} \text{mb} &= \text{(m - 1) / rowBlockDim + 1} \\ \text{nb} &= \text{(n - 1) / colBlockDim + 1} \end{align} \end{split}\]Both the temporary storage buffer and the GEBSR row pointer array are then passed to

[hipsparseXcsr2gebsrNnz](#hipsparse__csr2gebsr_8h_1a260feed7bdabb3e436c6bcf2d836b6dd)which fills the GEBSR row pointer array`bsrRowPtr`

and also computes the number of nonzero blocks,`bsrNnzDevhost`

, that will exist in the GEBSR matrix. The user then allocates both the GEBSR column indices array`bsrColInd`

with size`bsrNnzDevhost`

as well as the GEBSR values array`bsrVal`

with size`bsrNnzDevhost*rowBlockDim*colBlockDim`

. Finally, with all arrays allocated, the conversion is completed by calling`hipsparseXcsr2gebsr`

.For example, assuming the matrix:

\[\begin{split} \begin{bmatrix} 1 & 0 & 0 & 2 & 4 & 0 \\ 3 & 4 & 0 & 0 & 5 & 1 \\ 5 & 0 & 6 & 7 & 6 & 2 \end{bmatrix} \end{split}\]represented in CSR format with the arrays:

\[\begin{split} \begin{align} \text{csrRowPtr} &= \begin{bmatrix} 0 & 3 & 7 & 12 \end{bmatrix} \\ \text{csrColInd} &= \begin{bmatrix} 0 & 3 & 4 & 0 & 1 & 4 & 5 & 0 & 2 & 3 & 4 & 5 \end{bmatrix} \\ \text{csrVal} &= \begin{bmatrix} 1 & 2 & 4 & 3 & 4 & 5 & 1 & 5 & 6 & 7 & 6 & 2 \end{bmatrix} \end{align} \end{split}\]then using

`rowBlockDim=3`

and`colBlockDim=2`

, the final GEBSR matrix is:\[\begin{split} \left[ \begin{array}{c | c} \begin{array}{c c} 1 & 0 \\ 3 & 4 \\ 3 & 0 \end{array} & \begin{array}{c c} 0 & 2 \\ 0 & 0 \\ 6 & 7 \end{array} & \begin{array}{c c} 4 & 0 \\ 5 & 1 \\ 6 & 2 \end{array} \end{array} \right] \end{split}\]and is represented with the arrays:

\[\begin{split} \begin{align} \text{bsrRowPtr} &= \begin{bmatrix} 0 & 3 \end{bmatrix} \\ \text{bsrColInd} &= \begin{bmatrix} 0 & 1 & 2 \end{bmatrix} \\ \text{bsrVal} &= \begin{bmatrix} 1 & 0 & 3 & 4 & 3 & 0 & 0 & 2 & 0 & 0 & 6 & 7 & 4 & 0 & 5 & 1 & 6 & 2 \end{bmatrix} \end{align} \end{split}\]The above example assumes that the blocks are row ordered. If instead the blocks are column ordered, the

`bsrVal`

arrays becomes:\[ \begin{align} \text{bsrVal} &= \begin{bmatrix} 1 & 3 & 3 & 0 & 4 & 0 & 0 & 0 & 6 & 2 & 0 & 7 & 4 & 5 & 6 & 0 & 1 & 2 \end{bmatrix} \end{align} \]The block order direction is determined by

`dir`

.It may be the case that

`rowBlockDim`

does not divide evenly into`m`

and/or that`colBlockDim`

does not divide evenly into`n`

. In these cases, the CSR matrix is expanded in size in order to fit full GEBSR blocks. For example, using the original CSR matrix but this time with`rowBlockDim=2`

and`colBlockDim=3`

, the resulting GEBSR matrix would looks like:\[\begin{split} \left[ \begin{array}{c | c} \begin{array}{c c c} 1 & 0 & 0 \\ 3 & 4 & 0 \end{array} & \begin{array}{c c c} 2 & 4 & 0 \\ 0 & 5 & 1 \end{array} \\ \hline \begin{array}{c c c} 5 & 0 & 6 \\ 0 & 0 & 0 \end{array} & \begin{array}{c c c} 7 & 6 & 2 \\ 0 & 0 & 0 \end{array} \end{array} \right] \end{split}\]**Example**int main(int argc, char* argv[]) { // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); hipsparseMatDescr_t csr_descr; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&csr_descr)); hipsparseMatDescr_t bsr_descr; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&bsr_descr)); // Sparse matrix in CSR format // 1 2 0 3 0 0 // 0 4 5 0 0 1 // A = 6 0 0 7 8 0 // 0 0 3 0 2 2 // 1 0 0 0 4 3 // 7 2 0 0 1 4 int hcsrRowPtr[7] = {0, 3, 6, 9, 12, 15, 19}; int hcsrColInd[19] = {0, 1, 3, 1, 2, 5, 0, 3, 4, 2, 4, 5, 0, 4, 5, 0, 1, 4, 5}; float hcsrVal[19] = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 1.0f, 6.0f, 7.0f, 8.0f, 3.0f, 2.0f, 2.0f, 1.0f, 4.0f, 3.0f, 7.0f, 2.0f, 1.0f, 4.0f}; int m = 6; int n = 6; int nnz = 19; int rowBlockDim = 3; int colBlockDim = 2; hipsparseDirection_t dir = HIPSPARSE_DIRECTION_ROW; hipsparseIndexBase_t base = HIPSPARSE_INDEX_BASE_ZERO; int mb = (m + rowBlockDim - 1) / rowBlockDim; int nb = (n + colBlockDim - 1) / colBlockDim; int* dcsrRowPtr = nullptr; int* dcsrColInd = nullptr; float* dcsrVal = nullptr; HIP_CHECK(hipMalloc((void**)&dcsrRowPtr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&dcsrColInd, sizeof(int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcsrVal, sizeof(float) * nnz)); HIP_CHECK(hipMemcpy(dcsrRowPtr, hcsrRowPtr, sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrColInd, hcsrColInd, sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrVal, hcsrVal, sizeof(float) * nnz, hipMemcpyHostToDevice)); int* dbsrRowPtr = nullptr; HIP_CHECK(hipMalloc((void**)&dbsrRowPtr, sizeof(int) * (mb + 1))); size_t bufferSize; HIPSPARSE_CHECK(hipsparseScsr2gebsr_bufferSize(handle, dir, m, n, csr_descr, dcsrVal, dcsrRowPtr, dcsrColInd, rowBlockDim, colBlockDim, &bufferSize)); void* dbuffer = nullptr; HIP_CHECK(hipMalloc((void**)&dbuffer, bufferSize)); int nnzb; HIPSPARSE_CHECK(hipsparseXcsr2gebsrNnz(handle, dir, m, n, csr_descr, dcsrRowPtr, dcsrColInd, bsr_descr, dbsrRowPtr, rowBlockDim, colBlockDim, &nnzb, dbuffer)); int* dbsrColInd = nullptr; float* dbsrVal = nullptr; HIP_CHECK(hipMalloc((void**)&dbsrColInd, sizeof(int) * nnzb)); HIP_CHECK(hipMalloc((void**)&dbsrVal, sizeof(float) * rowBlockDim * colBlockDim * nnzb)); HIPSPARSE_CHECK(hipsparseScsr2gebsr(handle, dir, m, n, csr_descr, dcsrVal, dcsrRowPtr, dcsrColInd, bsr_descr, dbsrVal, dbsrRowPtr, dbsrColInd, rowBlockDim, colBlockDim, dbuffer)); HIP_CHECK(hipFree(dcsrRowPtr)); HIP_CHECK(hipFree(dcsrColInd)); HIP_CHECK(hipFree(dcsrVal)); HIP_CHECK(hipFree(dbsrRowPtr)); HIP_CHECK(hipFree(dbsrColInd)); HIP_CHECK(hipFree(dbsrVal)); HIP_CHECK(hipFree(dbuffer)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(csr_descr)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(bsr_descr)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); return 0; }


- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**dir**–**[in]**the storage format of the blocks,[HIPSPARSE_DIRECTION_ROW](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59ae8589abecf2fbfb4b6307fd9dacd9e55)or[HIPSPARSE_DIRECTION_COLUMN](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59a32e23f292b2377f6e60bdc90274c796c)**m**–**[in]**number of rows in the sparse CSR matrix.**n**–**[in]**number of columns in the sparse CSR matrix.**csr_descr**–**[in]**descriptor of the sparse CSR matrix. Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**csrVal**–**[in]**array of`nnz`

elements containing the values of the sparse CSR matrix.**csrRowPtr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csrColInd**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**bsr_descr**–**[in]**descriptor of the sparse BSR matrix. Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**bsrVal**–**[out]**array of`nnzb*`

`rowBlockDim*`

`colBlockDim`

containing the values of the sparse BSR matrix.**bsrRowPtr**–**[out]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix.**bsrColInd**–**[out]**array of`nnzb`

elements containing the block column indices of the sparse BSR matrix.**rowBlockDim**–**[in]**row size of the blocks in the sparse GEneral BSR matrix.**colBlockDim**–**[in]**col size of the blocks in the sparse GEneral BSR matrix.**pbuffer**–**[in]**buffer allocated by the user whose size is determined by calling[hipsparseXcsr2gebsr_bufferSize()](#hipsparse__csr2gebsr_8h_1a7affde46e05e85ce8417ef756e8ac0df).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`rowBlockDim`

,`colBlockDim`

,`bsrVal`

,`bsrRowPtr`

,`bsrColInd`

,`csrVal`

,`csrRowPtr`

or`csrColInd`

pointer is invalid.



## hipsparseXbsr2csr()[#](#hipsparsexbsr2csr)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSbsr2csr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const float *bsrValA, const int *bsrRowPtrA, const int *bsrColIndA, int blockDim, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, float *csrValC, int *csrRowPtrC, int *csrColIndC)[#](#_CPPv417hipsparseSbsr2csr17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPKfPKiPKiiK19hipsparseMatDescr_tPfPiPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDbsr2csr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const double *bsrValA, const int *bsrRowPtrA, const int *bsrColIndA, int blockDim, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, double *csrValC, int *csrRowPtrC, int *csrColIndC)[#](#_CPPv417hipsparseDbsr2csr17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPKdPKiPKiiK19hipsparseMatDescr_tPdPiPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCbsr2csr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipComplex *bsrValA, const int *bsrRowPtrA, const int *bsrColIndA, int blockDim, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, hipComplex *csrValC, int *csrRowPtrC, int *csrColIndC)[#](#_CPPv417hipsparseCbsr2csr17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPK10hipComplexPKiPKiiK19hipsparseMatDescr_tP10hipComplexPiPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZbsr2csr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipDoubleComplex *bsrValA, const int *bsrRowPtrA, const int *bsrColIndA, int blockDim, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, hipDoubleComplex *csrValC, int *csrRowPtrC, int *csrColIndC)[#](#_CPPv417hipsparseZbsr2csr17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPK16hipDoubleComplexPKiPKiiK19hipsparseMatDescr_tP16hipDoubleComplexPiPi) Convert a sparse BSR matrix into a sparse CSR matrix.

`hipsparseXbsr2csr`

converts a BSR matrix into a CSR matrix. It is assumed, that`csrValC`

,`csrColIndC`

and`csrRowPtrC`

are allocated. Allocation size for`csrRowPtrC`

is computed by the number of block rows multiplied by the block dimension plus one. Allocation for`csrValC`

and`csrColInd`

is computed by the the number of blocks in the BSR matrix multiplied by the block dimension squared.For example, given the BSR matrix using block dimension 2:

\[\begin{split} \left[ \begin{array}{c | c} \begin{array}{c c} 1 & 0 \\ 3 & 4 \end{array} & \begin{array}{c c} 0 & 2 \\ 0 & 0 \end{array} \\ \hline \begin{array}{c c} 5 & 0 \\ 1 & 2 \end{array} & \begin{array}{c c} 6 & 7 \\ 3 & 4 \end{array} \\ \end{array} \right] \end{split}\]The resulting CSR matrix row pointer, column indices, and values arrays are:

\[\begin{split} \begin{align} \text{csrRowPtrC} &= \begin{bmatrix} 0 & 4 & 8 & 12 & 16 \end{bmatrix} \\ \text{csrColIndC} &= \begin{bmatrix} 0 & 1 & 2 & 3 & 0 & 1 & 2 & 3 & 0 & 1 & 2 & 3 & 0 & 1 & 2 & 3 \end{bmatrix} \\ \text{csrValC} &= \begin{bmatrix} 1 & 0 & 0 & 2 & 3 & 4 & 0 & 0 & 5 & 0 & 6 & 7 & 1 & 2 & 3 & 4 \end{bmatrix} \\ \end{align} \end{split}\]**Example**int main(int argc, char* argv[]) { // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); hipsparseMatDescr_t csr_descr; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&csr_descr)); hipsparseMatDescr_t bsr_descr; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&bsr_descr)); // Sparse matrix in BSR format // 1 2 | 0 3 | 0 0 // 0 4 | 5 0 | 0 1 // --------------- // A = 6 0 | 0 7 | 8 0 // 0 0 | 3 0 | 2 2 // --------------- // 1 0 | 0 0 | 4 3 // 7 2 | 0 0 | 1 4 int hbsrRowPtr[4] = {0, 3, 6, 8}; int hbsrColInd[8] = {0, 1, 2, 0, 1, 2, 0, 2}; float hbsrVal[32] = {1.0f, 2.0f, 0.0f, 4.0f, 0.0f, 3.0f, 5.0f, 0.0f, 0.0f, 0.0f, 0.0f, 1.0f, 6.0f, 0.0f, 0.0f, 0.0f, 0.0f, 7.0f, 3.0f, 0.0f, 8.0f, 0.0f, 2.0f, 2.0f, 1.0f, 0.0f, 7.0f, 2.0f, 4.0f, 3.0f, 1.0f, 4.0f}; int m = 6; int n = 6; int nnz = 32; int mb = 3; int nb = 3; int nnzb = 8; int blockDim = 2; hipsparseDirection_t dir = HIPSPARSE_DIRECTION_ROW; int* dbsrRowPtr = nullptr; int* dbsrColInd = nullptr; float* dbsrVal = nullptr; HIP_CHECK(hipMalloc((void**)&dbsrRowPtr, sizeof(int) * (mb + 1))); HIP_CHECK(hipMalloc((void**)&dbsrColInd, sizeof(int) * nnzb)); HIP_CHECK(hipMalloc((void**)&dbsrVal, sizeof(float) * blockDim * blockDim * nnzb)); HIP_CHECK(hipMemcpy(dbsrRowPtr, hbsrRowPtr, sizeof(int) * (mb + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dbsrColInd, hbsrColInd, sizeof(int) * nnzb, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( dbsrVal, hbsrVal, sizeof(float) * blockDim * blockDim * nnzb, hipMemcpyHostToDevice)); int* dcsrRowPtr = nullptr; int* dcsrColInd = nullptr; float* dcsrVal = nullptr; HIP_CHECK(hipMalloc((void**)&dcsrRowPtr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&dcsrColInd, sizeof(int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcsrVal, sizeof(float) * nnz)); HIPSPARSE_CHECK(hipsparseSbsr2csr(handle, dir, mb, nb, bsr_descr, dbsrVal, dbsrRowPtr, dbsrColInd, blockDim, csr_descr, dcsrVal, dcsrRowPtr, dcsrColInd)); std::vector<int> hcsrRowPtr(m + 1); std::vector<int> hcsrColInd(nnz); std::vector<float> hcsrVal(nnz); // Copy back to the host HIP_CHECK( hipMemcpy(hcsrRowPtr.data(), dcsrRowPtr, sizeof(int) * (m + 1), hipMemcpyDeviceToHost)); HIP_CHECK(hipMemcpy(hcsrColInd.data(), dcsrColInd, sizeof(int) * nnz, hipMemcpyDeviceToHost)); HIP_CHECK(hipMemcpy(hcsrVal.data(), dcsrVal, sizeof(float) * nnz, hipMemcpyDeviceToHost)); std::cout << "C" << std::endl; for(int i = 0; i < m; i++) { int start = hcsrRowPtr[i]; int end = hcsrRowPtr[i + 1]; std::vector<float> temp(n, 0.0f); for(int j = start; j < end; j++) { temp[hcsrColInd[j]] = hcsrVal[j]; } for(int j = 0; j < n; j++) { std::cout << temp[j] << " "; } std::cout << "" << std::endl; } std::cout << "" << std::endl; HIP_CHECK(hipFree(dbsrRowPtr)); HIP_CHECK(hipFree(dbsrColInd)); HIP_CHECK(hipFree(dbsrVal)); HIP_CHECK(hipFree(dcsrRowPtr)); HIP_CHECK(hipFree(dcsrColInd)); HIP_CHECK(hipFree(dcsrVal)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(csr_descr)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(bsr_descr)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**dirA**–**[in]**the storage format of the blocks,[HIPSPARSE_DIRECTION_ROW](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59ae8589abecf2fbfb4b6307fd9dacd9e55)or[HIPSPARSE_DIRECTION_COLUMN](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59a32e23f292b2377f6e60bdc90274c796c)**mb**–**[in]**number of block rows in the sparse BSR matrix.**nb**–**[in]**number of block columns in the sparse BSR matrix.**descrA**–**[in]**descriptor of the sparse BSR matrix. Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**bsrValA**–**[in]**array of`nnzb*blockDim*blockDim`

containing the values of the sparse BSR matrix.**bsrRowPtrA**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix.**bsrColIndA**–**[in]**array of`nnzb`

elements containing the block column indices of the sparse BSR matrix.**blockDim**–**[in]**size of the blocks in the sparse BSR matrix.**descrC**–**[in]**descriptor of the sparse CSR matrix. Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**csrValC**–**[out]**array of`nnzb*blockDim*blockDim`

elements containing the values of the sparse CSR matrix.**csrRowPtrC**–**[out]**array of`m+1`

where`m=mb*blockDim`

elements that point to the start of every row of the sparse CSR matrix.**csrColIndC**–**[out]**array of`nnzb*blockDim*blockDim`

elements containing the column indices of the sparse CSR matrix.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`mb`

,`nb`

,`blockDim`

,`bsrValA`

,`bsrRowPtrA`

,`bsrColIndA`

,`csrValC`

,`csrRowPtrC`

or`csrColIndC`

pointer is invalid.



## hipsparseXgebsr2csr()[#](#hipsparsexgebsr2csr)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSgebsr2csr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const float *bsrValA, const int *bsrRowPtrA, const int *bsrColIndA, int rowBlockDim, int colBlockDim, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, float *csrValC, int *csrRowPtrC, int *csrColIndC)[#](#_CPPv419hipsparseSgebsr2csr17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPKfPKiPKiiiK19hipsparseMatDescr_tPfPiPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDgebsr2csr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const double *bsrValA, const int *bsrRowPtrA, const int *bsrColIndA, int rowBlockDim, int colBlockDim, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, double *csrValC, int *csrRowPtrC, int *csrColIndC)[#](#_CPPv419hipsparseDgebsr2csr17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPKdPKiPKiiiK19hipsparseMatDescr_tPdPiPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCgebsr2csr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipComplex *bsrValA, const int *bsrRowPtrA, const int *bsrColIndA, int rowBlockDim, int colBlockDim, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, hipComplex *csrValC, int *csrRowPtrC, int *csrColIndC)[#](#_CPPv419hipsparseCgebsr2csr17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPK10hipComplexPKiPKiiiK19hipsparseMatDescr_tP10hipComplexPiPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZgebsr2csr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipDoubleComplex *bsrValA, const int *bsrRowPtrA, const int *bsrColIndA, int rowBlockDim, int colBlockDim, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, hipDoubleComplex *csrValC, int *csrRowPtrC, int *csrColIndC)[#](#_CPPv419hipsparseZgebsr2csr17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPK16hipDoubleComplexPKiPKiiiK19hipsparseMatDescr_tP16hipDoubleComplexPiPi) Convert a sparse GEBSR matrix into a sparse CSR matrix.

`hipsparseXgebsr2csr`

converts a GEBSR matrix into a CSR matrix. It is assumed, that`csrValC`

,`csrColIndC`

and`csrRowPtrC`

are already allocated prior to calling`hipsparseXgebsr2csr`

. Allocation size for`csrRowPtrC`

equals`m+1`

where:\[\begin{split} \begin{align} \text{m} &= \text{mb * rowBlockDim} \\ \text{n} &= \text{nb * colBlockDim} \end{align} \end{split}\]Allocation size for

`csrValC`

and`csrColIndC`

is computed by the the number of blocks in the GEBSR matrix,`nnzb`

, multiplied by the product of the block dimensions, i.e.`nnz=nnzb*rocBlockDim*colBlockDim`

.For example, given the GEBSR matrix:

\[\begin{split} \left[ \begin{array}{c | c | c} \begin{array}{c c} 6 & 2 \\ 1 & 4 \\ 5 & 4 \end{array} & \begin{array}{c c} 0 & 3 \\ 5 & 0 \\ 0 & 7 \end{array} & \begin{array}{c c} 0 & 0 \\ 0 & 0 \\ 0 & 0 \end{array} \\ \hline \begin{array}{c c} 0 & 0 \\ 0 & 0 \\ 0 & 0 \end{array} & \begin{array}{c c} 3 & 0 \\ 0 & 0 \\ 0 & 7 \end{array} & \begin{array}{c c} 2 & 2 \\ 4 & 3 \\ 1 & 4 \end{array} \\ \end{array} \right] \end{split}\]**Example**int main(int argc, char* argv[]) { // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); hipsparseMatDescr_t csr_descr; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&csr_descr)); hipsparseMatDescr_t bsr_descr; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&bsr_descr)); // Sparse matrix in GEBSR format // 1 2 | 0 3 | 0 0 // 0 4 | 5 0 | 0 1 // A = 6 0 | 0 7 | 8 0 // --------------- // 0 0 | 3 0 | 2 2 // 1 0 | 0 0 | 4 3 // 7 2 | 0 0 | 1 4 int hbsrRowPtr[3] = {0, 3, 6}; int hbsrColInd[6] = {0, 1, 2, 0, 1, 2}; float hbsrVal[36] = {1.0f, 2.0f, 0.0f, 4.0f, 6.0f, 0.0f, 0.0f, 3.0f, 5.0f, 0.0f, 0.0f, 7.0f, 0.0f, 0.0f, 0.0f, 1.0f, 8.0f, 0.0f, 0.0f, 0.0f, 1.0f, 0.0f, 7.0f, 2.0f, 3.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 2.0f, 2.0f, 4.0f, 3.0f, 1.0f, 4.0f}; int m = 6; int n = 6; int nnz = 36; int mb = 2; int nb = 3; int nnzb = 6; int rowBlockDim = 3; int colBlockDim = 2; hipsparseDirection_t dir = HIPSPARSE_DIRECTION_ROW; int* dbsrRowPtr = nullptr; int* dbsrColInd = nullptr; float* dbsrVal = nullptr; HIP_CHECK(hipMalloc((void**)&dbsrRowPtr, sizeof(int) * (mb + 1))); HIP_CHECK(hipMalloc((void**)&dbsrColInd, sizeof(int) * nnzb)); HIP_CHECK(hipMalloc((void**)&dbsrVal, sizeof(float) * rowBlockDim * colBlockDim * nnzb)); HIP_CHECK(hipMemcpy(dbsrRowPtr, hbsrRowPtr, sizeof(int) * (mb + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dbsrColInd, hbsrColInd, sizeof(int) * nnzb, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( dbsrVal, hbsrVal, sizeof(float) * rowBlockDim * colBlockDim * nnzb, hipMemcpyHostToDevice)); int* dcsrRowPtr = nullptr; int* dcsrColInd = nullptr; float* dcsrVal = nullptr; HIP_CHECK(hipMalloc((void**)&dcsrRowPtr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&dcsrColInd, sizeof(int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcsrVal, sizeof(float) * nnz)); HIPSPARSE_CHECK(hipsparseSgebsr2csr(handle, dir, mb, nb, bsr_descr, dbsrVal, dbsrRowPtr, dbsrColInd, rowBlockDim, colBlockDim, csr_descr, dcsrVal, dcsrRowPtr, dcsrColInd)); HIP_CHECK(hipFree(dbsrRowPtr)); HIP_CHECK(hipFree(dbsrColInd)); HIP_CHECK(hipFree(dbsrVal)); HIP_CHECK(hipFree(dcsrRowPtr)); HIP_CHECK(hipFree(dcsrColInd)); HIP_CHECK(hipFree(dcsrVal)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(csr_descr)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(bsr_descr)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**dirA**–**[in]**the storage format of the blocks,[HIPSPARSE_DIRECTION_ROW](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59ae8589abecf2fbfb4b6307fd9dacd9e55)or[HIPSPARSE_DIRECTION_COLUMN](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59a32e23f292b2377f6e60bdc90274c796c)**mb**–**[in]**number of block rows in the sparse general BSR matrix.**nb**–**[in]**number of block columns in the sparse general BSR matrix.**descrA**–**[in]**descriptor of the sparse general BSR matrix. Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**bsrValA**–**[in]**array of`nnzb*rowBlockDim*colBlockDim`

containing the values of the sparse BSR matrix.**bsrRowPtrA**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix.**bsrColIndA**–**[in]**array of`nnzb`

elements containing the block column indices of the sparse BSR matrix.**rowBlockDim**–**[in]**row size of the blocks in the sparse general BSR matrix.**colBlockDim**–**[in]**column size of the blocks in the sparse general BSR matrix.**descrC**–**[in]**descriptor of the sparse CSR matrix. Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**csrValC**–**[out]**array of`nnzb*rowBlockDim*colBlockDim`

elements containing the values of the sparse CSR matrix.**csrRowPtrC**–**[out]**array of`m+1`

where`m=mb*rowBlockDim`

elements that point to the start of every row of the sparse CSR matrix.**csrColIndC**–**[out]**array of`nnzb*block_dim*block_dim`

elements containing the column indices of the sparse CSR matrix.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`mb`

,`nb`

,`block_dim`

,`bsrValA`

,`bsrRowPtrA`

,`bsrColIndA`

,`csrValC`

,`csrRowPtrC`

or`csrColIndC`

pointer is invalid.



## hipsparseXcsr2csr_compress()[#](#hipsparsexcsr2csr-compress)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseScsr2csr_compress([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const float *csrValA, const int *csrColIndA, const int *csrRowPtrA, int nnzA, const int *nnzPerRow, float *csrValC, int *csrColIndC, int *csrRowPtrC, float tol)[#](#_CPPv426hipsparseScsr2csr_compress17hipsparseHandle_tiiK19hipsparseMatDescr_tPKfPKiPKiiPKiPfPiPif)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDcsr2csr_compress([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const double *csrValA, const int *csrColIndA, const int *csrRowPtrA, int nnzA, const int *nnzPerRow, double *csrValC, int *csrColIndC, int *csrRowPtrC, double tol)[#](#_CPPv426hipsparseDcsr2csr_compress17hipsparseHandle_tiiK19hipsparseMatDescr_tPKdPKiPKiiPKiPdPiPid)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCcsr2csr_compress([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipComplex *csrValA, const int *csrColIndA, const int *csrRowPtrA, int nnzA, const int *nnzPerRow, hipComplex *csrValC, int *csrColIndC, int *csrRowPtrC, hipComplex tol)[#](#_CPPv426hipsparseCcsr2csr_compress17hipsparseHandle_tiiK19hipsparseMatDescr_tPK10hipComplexPKiPKiiPKiP10hipComplexPiPi10hipComplex)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZcsr2csr_compress([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipDoubleComplex *csrValA, const int *csrColIndA, const int *csrRowPtrA, int nnzA, const int *nnzPerRow, hipDoubleComplex *csrValC, int *csrColIndC, int *csrRowPtrC, hipDoubleComplex tol)[#](#_CPPv426hipsparseZcsr2csr_compress17hipsparseHandle_tiiK19hipsparseMatDescr_tPK16hipDoubleComplexPKiPKiiPKiP16hipDoubleComplexPiPi16hipDoubleComplex) Convert a sparse CSR matrix into a compressed sparse CSR matrix.

`hipsparseXcsr2csr_compress`

converts a CSR matrix into a compressed CSR matrix by removing entries in the input CSR matrix that are below a non-negative threshold`tol:`

\[ C(i,j) = A(i, j) \text{ if |A(i, j)| > tol} \]The user must first call

[hipsparseXnnz_compress()](#hipsparse__nnz__compress_8h_1a6a9237cf1117262afa6e4d71b7896997)to determine the number of nonzeros per row as well as the total number of nonzeros that will exist in resulting compressed CSR matrix. The user then uses this information to allocate the column indices array`csrColIndC`

and the values array`csrValC`

. The user then calls`hipsparseXcsr2csr_compress`

to complete the conversion.**Example**int main(int argc, char* argv[]) { // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // Matrix descriptor hipsparseMatDescr_t descr; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&descr)); // Sparse matrix in CSR format // 1 2 0 3 0 // A = 0 4 5 0 0 // 6 0 0 7 8 int hcsrRowPtrA[4] = {0, 3, 5, 8}; int hcsrColIndA[8] = {0, 1, 3, 1, 2, 0, 3, 4}; float hcsrValA[8] = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f}; int m = 3; int n = 5; int nnzA = 8; float tol = 5.9f; int* dcsrRowPtrA = nullptr; int* dcsrColIndA = nullptr; float* dcsrValA = nullptr; HIP_CHECK(hipMalloc((void**)&dcsrRowPtrA, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&dcsrColIndA, sizeof(int) * nnzA)); HIP_CHECK(hipMalloc((void**)&dcsrValA, sizeof(float) * nnzA)); HIP_CHECK(hipMemcpy(dcsrRowPtrA, hcsrRowPtrA, sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrColIndA, hcsrColIndA, sizeof(int) * nnzA, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrValA, hcsrValA, sizeof(float) * nnzA, hipMemcpyHostToDevice)); // Allocate memory for the nnz_per_row array int* dnnz_per_row; HIP_CHECK(hipMalloc((void**)&dnnz_per_row, sizeof(int) * m)); // Call snnz_compress() which fills in nnz_per_row array and finds the number // of entries that will be in the compressed CSR matrix int nnzC; HIPSPARSE_CHECK( hipsparseSnnz_compress(handle, m, descr, dcsrValA, dcsrRowPtrA, dnnz_per_row, &nnzC, tol)); int* dcsrRowPtrC = nullptr; int* dcsrColIndC = nullptr; float* dcsrValC = nullptr; HIP_CHECK(hipMalloc((void**)&dcsrRowPtrC, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&dcsrColIndC, sizeof(int) * nnzC)); HIP_CHECK(hipMalloc((void**)&dcsrValC, sizeof(float) * nnzC)); HIPSPARSE_CHECK(hipsparseScsr2csr_compress(handle, m, n, descr, dcsrValA, dcsrColIndA, dcsrRowPtrA, nnzA, dnnz_per_row, dcsrValC, dcsrColIndC, dcsrRowPtrC, tol)); HIP_CHECK(hipFree(dcsrRowPtrA)); HIP_CHECK(hipFree(dcsrColIndA)); HIP_CHECK(hipFree(dcsrValA)); HIP_CHECK(hipFree(dcsrRowPtrC)); HIP_CHECK(hipFree(dcsrColIndC)); HIP_CHECK(hipFree(dcsrValC)); HIP_CHECK(hipFree(dnnz_per_row)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(descr)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); return 0; }


Note

In the case of complex matrices only the magnitude of the real part of

`tol`

is used.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix.**n**–**[in]**number of columns of the sparse CSR matrix.**descrA**–**[in]**matrix descriptor for the CSR matrix**csrValA**–**[in]**array of`nnzA`

elements of the sparse CSR matrix.**csrRowPtrA**–**[in]**array of`m+1`

elements that point to the start of every row of the uncompressed sparse CSR matrix.**csrColIndA**–**[in]**array of`nnzA`

elements containing the column indices of the uncompressed sparse CSR matrix.**nnzA**–**[in]**number of elements in the column indices and values arrays of the uncompressed sparse CSR matrix.**nnzPerRow**–**[in]**array of length`m`

containing the number of entries that will be kept per row in the final compressed CSR matrix.**csrValC**–**[out]**array of`nnzC`

elements of the compressed sparse CSC matrix.**csrRowPtrC**–**[out]**array of`m+1`

elements that point to the start of every column of the compressed sparse CSR matrix.**csrColIndC**–**[out]**array of`nnzC`

elements containing the row indices of the compressed sparse CSR matrix.**tol**–**[in]**the non-negative tolerance used for compression. If`tol`

is complex then only the magnitude of the real part is used. Entries in the input uncompressed CSR array that are below the tolerance are removed in output compressed CSR matrix.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`nnzA`

,`tol`

,`csrValA`

,`csrRowPtrA`

,`csrColIndA`

,`csrValC`

,`csrRowPtrC`

,`csrColIndC`

or`nnzPerRow`

pointer is invalid.



## hipsparseXpruneCsr2csr_bufferSize()[#](#hipsparsexprunecsr2csr-buffersize)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpruneCsr2csr_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnzA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const float *csrValA, const int *csrRowPtrA, const int *csrColIndA, const float *threshold, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, const float *csrValC, const int *csrRowPtrC, const int *csrColIndC, size_t *pBufferSizeInBytes)[#](#_CPPv433hipsparseSpruneCsr2csr_bufferSize17hipsparseHandle_tiiiK19hipsparseMatDescr_tPKfPKiPKiPKfK19hipsparseMatDescr_tPKfPKiPKiP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDpruneCsr2csr_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnzA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const double *csrValA, const int *csrRowPtrA, const int *csrColIndA, const double *threshold, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, const double *csrValC, const int *csrRowPtrC, const int *csrColIndC, size_t *pBufferSizeInBytes)[#](#_CPPv433hipsparseDpruneCsr2csr_bufferSize17hipsparseHandle_tiiiK19hipsparseMatDescr_tPKdPKiPKiPKdK19hipsparseMatDescr_tPKdPKiPKiP6size_t) Convert and prune sparse CSR matrix into a sparse CSR matrix.

`hipsparseXpruneCsr2csr_bufferSize`

returns the size of the temporary buffer that is required by`hipsparseXpruneCsr2csrNnz`

and hipsparseXpruneCsr2csr. The temporary storage buffer must be allocated by the user.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows in the sparse CSR matrix.**n**–**[in]**number of columns in the sparse CSR matrix.**nnzA**–**[in]**number of non-zeros in the sparse CSR matrix A.**descrA**–**[in]**descriptor of the sparse CSR matrix A. Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**csrValA**–**[in]**array of`nnzA`

elements containing the values of the sparse CSR matrix A.**csrRowPtrA**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix A.**csrColIndA**–**[in]**array of`nnzA`

elements containing the column indices of the sparse CSR matrix A.**threshold**–**[in]**pointer to the non-negative pruning threshold which can exist in either host or device memory.**descrC**–**[in]**descriptor of the sparse CSR matrix C. Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**csrValC**–**[in]**array of`nnzC`

elements containing the values of the sparse CSR matrix C.**csrRowPtrC**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix C.**csrColIndC**–**[in]**array of`nnzC`

elements containing the column indices of the sparse CSR matrix C.**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer required by[hipsparseSpruneCsr2csrNnz()](#hipsparse__prune__csr2csr_8h_1ac7e23d0e39782b88b53e88effc2ef58b),[hipsparseDpruneCsr2csrNnz()](#hipsparse__prune__csr2csr_8h_1a0fd1cf7717f29656975f8ed438e41754),[hipsparseSpruneCsr2csr()](#hipsparse__prune__csr2csr_8h_1a07dcb61b8620950392747591244549e9), and[hipsparseDpruneCsr2csr()](#hipsparse__prune__csr2csr_8h_1a25ed7f5b62df4fb1b4dd7462e898108c).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

or`pBufferSizeInBytes`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.



## hipsparseXpruneCsr2csr_bufferSizeExt()[#](#hipsparsexprunecsr2csr-buffersizeext)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpruneCsr2csr_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnzA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const float *csrValA, const int *csrRowPtrA, const int *csrColIndA, const float *threshold, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, const float *csrValC, const int *csrRowPtrC, const int *csrColIndC, size_t *pBufferSizeInBytes)[#](#_CPPv436hipsparseSpruneCsr2csr_bufferSizeExt17hipsparseHandle_tiiiK19hipsparseMatDescr_tPKfPKiPKiPKfK19hipsparseMatDescr_tPKfPKiPKiP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDpruneCsr2csr_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnzA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const double *csrValA, const int *csrRowPtrA, const int *csrColIndA, const double *threshold, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, const double *csrValC, const int *csrRowPtrC, const int *csrColIndC, size_t *pBufferSizeInBytes)[#](#_CPPv436hipsparseDpruneCsr2csr_bufferSizeExt17hipsparseHandle_tiiiK19hipsparseMatDescr_tPKdPKiPKiPKdK19hipsparseMatDescr_tPKdPKiPKiP6size_t) Convert and prune sparse CSR matrix into a sparse CSR matrix.

`hipsparseXpruneCsr2csr_bufferSizeExt`

returns the size of the temporary buffer that is required by[hipsparseXpruneCsr2csrNnz()](#hipsparse__prune__csr2csr_8h_1ac7e23d0e39782b88b53e88effc2ef58b)and[hipsparseXpruneCsr2csr()](#hipsparse__prune__csr2csr_8h_1a07dcb61b8620950392747591244549e9). The temporary storage buffer must be allocated by the user.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows in the sparse CSR matrix.**n**–**[in]**number of columns in the sparse CSR matrix.**nnzA**–**[in]**number of non-zeros in the sparse CSR matrix A.**descrA**–**[in]**descriptor of the sparse CSR matrix A. Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**csrValA**–**[in]**array of`nnzA`

elements containing the values of the sparse CSR matrix A.**csrRowPtrA**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix A.**csrColIndA**–**[in]**array of`nnzA`

elements containing the column indices of the sparse CSR matrix A.**threshold**–**[in]**pointer to the non-negative pruning threshold which can exist in either host or device memory.**descrC**–**[in]**descriptor of the sparse CSR matrix C. Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**csrValC**–**[in]**array of`nnzC`

elements containing the values of the sparse CSR matrix C.**csrRowPtrC**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix C.**csrColIndC**–**[in]**array of`nnzC`

elements containing the column indices of the sparse CSR matrix C.**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer required by[hipsparseSpruneCsr2csrNnz()](#hipsparse__prune__csr2csr_8h_1ac7e23d0e39782b88b53e88effc2ef58b),[hipsparseDpruneCsr2csrNnz()](#hipsparse__prune__csr2csr_8h_1a0fd1cf7717f29656975f8ed438e41754),[hipsparseSpruneCsr2csr()](#hipsparse__prune__csr2csr_8h_1a07dcb61b8620950392747591244549e9), and[hipsparseDpruneCsr2csr()](#hipsparse__prune__csr2csr_8h_1a25ed7f5b62df4fb1b4dd7462e898108c).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

or`pBufferSizeInBytes`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.



## hipsparseXpruneCsr2csrNnz()[#](#hipsparsexprunecsr2csrnnz)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpruneCsr2csrNnz([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnzA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const float *csrValA, const int *csrRowPtrA, const int *csrColIndA, const float *threshold, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, int *csrRowPtrC, int *nnzTotalDevHostPtr, void *buffer)[#](#_CPPv425hipsparseSpruneCsr2csrNnz17hipsparseHandle_tiiiK19hipsparseMatDescr_tPKfPKiPKiPKfK19hipsparseMatDescr_tPiPiPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDpruneCsr2csrNnz([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnzA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const double *csrValA, const int *csrRowPtrA, const int *csrColIndA, const double *threshold, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, int *csrRowPtrC, int *nnzTotalDevHostPtr, void *buffer)[#](#_CPPv425hipsparseDpruneCsr2csrNnz17hipsparseHandle_tiiiK19hipsparseMatDescr_tPKdPKiPKiPKdK19hipsparseMatDescr_tPiPiPv) Convert and prune sparse CSR matrix into a sparse CSR matrix.

`hipsparseXpruneCsr2csrNnz`

computes the number of nonzero elements per row and the total number of nonzero elements in a sparse CSR matrix once elements less than the threshold are pruned from the matrix.Note

The routine does support asynchronous execution if the pointer mode is set to device.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows in the sparse CSR matrix.**n**–**[in]**number of columns in the sparse CSR matrix.**nnzA**–**[in]**number of non-zeros in the sparse CSR matrix A.**descrA**–**[in]**descriptor of the sparse CSR matrix A. Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**csrValA**–**[in]**array of`nnzA`

elements containing the values of the sparse CSR matrix A.**csrRowPtrA**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix A.**csrColIndA**–**[in]**array of`nnzA`

elements containing the column indices of the sparse CSR matrix A.**threshold**–**[in]**pointer to the non-negative pruning threshold which can exist in either host or device memory.**descrC**–**[in]**descriptor of the sparse CSR matrix C. Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**csrRowPtrC**–**[out]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix C.**nnzTotalDevHostPtr**–**[out]**total number of nonzero elements in device or host memory.**buffer**–**[out]**buffer allocated by the user whose size is determined by calling[hipsparseXpruneCsr2csr_bufferSize()](#hipsparse__prune__csr2csr_8h_1a16786194717117a4902032dd8afbebe0).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`nnzA`

,`threshold`

,`descrA`

,`descrC`

,`csrValA`

,`csrRowPtrA`

,`csrColIndA`

,`csrRowPtrC`

,`nnzTotalDevHostPtr`

or`buffer`

pointer is invalid.



## hipsparseXpruneCsr2csr()[#](#hipsparsexprunecsr2csr)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpruneCsr2csr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnzA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const float *csrValA, const int *csrRowPtrA, const int *csrColIndA, const float *threshold, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, float *csrValC, const int *csrRowPtrC, int *csrColIndC, void *buffer)[#](#_CPPv422hipsparseSpruneCsr2csr17hipsparseHandle_tiiiK19hipsparseMatDescr_tPKfPKiPKiPKfK19hipsparseMatDescr_tPfPKiPiPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDpruneCsr2csr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnzA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const double *csrValA, const int *csrRowPtrA, const int *csrColIndA, const double *threshold, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, double *csrValC, const int *csrRowPtrC, int *csrColIndC, void *buffer)[#](#_CPPv422hipsparseDpruneCsr2csr17hipsparseHandle_tiiiK19hipsparseMatDescr_tPKdPKiPKiPKdK19hipsparseMatDescr_tPdPKiPiPv) Convert and prune sparse CSR matrix into a sparse CSR matrix.

This function converts the sparse CSR matrix A into a sparse CSR matrix C by pruning values in A that are less than the threshold. All the parameters are assumed to have been pre-allocated by the user. The user first calls

[hipsparseXpruneCsr2csr_bufferSize()](#hipsparse__prune__csr2csr_8h_1a16786194717117a4902032dd8afbebe0)to determine the size of the buffer used by[hipsparseXpruneCsr2csrNnz()](#hipsparse__prune__csr2csr_8h_1ac7e23d0e39782b88b53e88effc2ef58b)and`hipsparseXpruneCsr2csr()`

which the user then allocates. The user then allocates`csrRowPtrC`

to have`m+1`

elements and then calls hipsparseXpruneCsr2csrNnz() which fills in the`csrRowPtrC`

array stores then number of elements that are larger than the pruning`threshold`

in`nnzTotalDevHostPtr`

. The user then calls`hipsparseXpruneCsr2csr()`

to complete the conversion. It is executed asynchronously with respect to the host and may return control to the application on the host before the entire result is ready.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows in the sparse CSR matrix.**n**–**[in]**number of columns in the sparse CSR matrix.**nnzA**–**[in]**number of non-zeros in the sparse CSR matrix A.**descrA**–**[in]**descriptor of the sparse CSR matrix A. Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**csrValA**–**[in]**array of`nnzA`

elements containing the values of the sparse CSR matrix A.**csrRowPtrA**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix A.**csrColIndA**–**[in]**array of`nnzA`

elements containing the column indices of the sparse CSR matrix A.**threshold**–**[in]**pointer to the non-negative pruning threshold which can exist in either host or device memory.**descrC**–**[in]**descriptor of the sparse CSR matrix C. Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**csrValC**–**[out]**array of`nnzC`

elements containing the values of the sparse CSR matrix C.**csrRowPtrC**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix C.**csrColIndC**–**[out]**array of`nnzC`

elements containing the column indices of the sparse CSR matrix C.**buffer**–**[in]**buffer allocated by the user whose size is determined by calling[hipsparseXpruneCsr2csr_bufferSize()](#hipsparse__prune__csr2csr_8h_1a16786194717117a4902032dd8afbebe0).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`nnzA`

,`threshold`

,`descrA`

,`descrC`

,`csrValA`

,`csrRowPtrA`

,`csrcolindA`

,`csrvalC`

,`csrrowptrC`

,`csrcolIndC`

or`buffer`

pointer is invalid.



## hipsparseXpruneCsr2csrByPercentage_bufferSize()[#](#hipsparsexprunecsr2csrbypercentage-buffersize)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpruneCsr2csrByPercentage_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnzA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const float *csrValA, const int *csrRowPtrA, const int *csrColIndA, float percentage, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, const float *csrValC, const int *csrRowPtrC, const int *csrColIndC,[pruneInfo_t](types.html#_CPPv411pruneInfo_t)info, size_t *pBufferSizeInBytes)[#](#_CPPv445hipsparseSpruneCsr2csrByPercentage_bufferSize17hipsparseHandle_tiiiK19hipsparseMatDescr_tPKfPKiPKifK19hipsparseMatDescr_tPKfPKiPKi11pruneInfo_tP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDpruneCsr2csrByPercentage_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnzA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const double *csrValA, const int *csrRowPtrA, const int *csrColIndA, double percentage, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, const double *csrValC, const int *csrRowPtrC, const int *csrColIndC,[pruneInfo_t](types.html#_CPPv411pruneInfo_t)info, size_t *pBufferSizeInBytes)[#](#_CPPv445hipsparseDpruneCsr2csrByPercentage_bufferSize17hipsparseHandle_tiiiK19hipsparseMatDescr_tPKdPKiPKidK19hipsparseMatDescr_tPKdPKiPKi11pruneInfo_tP6size_t) Convert and prune by percentage a sparse CSR matrix into a sparse CSR matrix.

`hipsparseXpruneCsr2csrByPercentage_bufferSize`

returns the size of the temporary buffer that is required by[hipsparseXpruneCsr2csrNnzByPercentage()](#hipsparse__prune__csr2csr__by__percentage_8h_1a49fdcbf9234f1ca31b1260183ffe49d7). The temporary storage buffer must be allocated by the user.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows in the sparse CSR matrix.**n**–**[in]**number of columns in the sparse CSR matrix.**nnzA**–**[in]**number of non-zeros in the sparse CSR matrix A.**descrA**–**[in]**descriptor of the sparse CSR matrix A. Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**csrValA**–**[in]**array of`nnzA`

elements containing the values of the sparse CSR matrix A.**csrRowPtrA**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix A.**csrColIndA**–**[in]**array of`nnzA`

elements containing the column indices of the sparse CSR matrix A.**percentage**–**[in]**`percentage>=0`

and`percentage<=100`

.**descrC**–**[in]**descriptor of the sparse CSR matrix C. Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**csrValC**–**[in]**array of`nnzC`

elements containing the values of the sparse CSR matrix C.**csrRowPtrC**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix C.**csrColIndC**–**[in]**array of`nnzC`

elements containing the column indices of the sparse CSR matrix C.**info**–**[in]**prune info structure.**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer required by[hipsparseSpruneCsr2csrNnzByPercentage()](#hipsparse__prune__csr2csr__by__percentage_8h_1a49fdcbf9234f1ca31b1260183ffe49d7),[hipsparseDpruneCsr2csrNnzByPercentage()](#hipsparse__prune__csr2csr__by__percentage_8h_1a210f79e55e8cc05aa115ca1ecea275f0),[hipsparseSpruneCsr2csrByPercentage()](#hipsparse__prune__csr2csr__by__percentage_8h_1aec7357dd8820e2aaf5aefce1c045a772), and[hipsparseDpruneCsr2csrByPercentage()](#hipsparse__prune__csr2csr__by__percentage_8h_1a3d297bb66bb60223b54403de8eb7e040).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

or`pBufferSizeInBytes`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.



## hipsparseXpruneCsr2csrByPercentage_bufferSizeExt()[#](#hipsparsexprunecsr2csrbypercentage-buffersizeext)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpruneCsr2csrByPercentage_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnzA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const float *csrValA, const int *csrRowPtrA, const int *csrColIndA, float percentage, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, const float *csrValC, const int *csrRowPtrC, const int *csrColIndC,[pruneInfo_t](types.html#_CPPv411pruneInfo_t)info, size_t *pBufferSizeInBytes)[#](#_CPPv448hipsparseSpruneCsr2csrByPercentage_bufferSizeExt17hipsparseHandle_tiiiK19hipsparseMatDescr_tPKfPKiPKifK19hipsparseMatDescr_tPKfPKiPKi11pruneInfo_tP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDpruneCsr2csrByPercentage_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnzA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const double *csrValA, const int *csrRowPtrA, const int *csrColIndA, double percentage, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, const double *csrValC, const int *csrRowPtrC, const int *csrColIndC,[pruneInfo_t](types.html#_CPPv411pruneInfo_t)info, size_t *pBufferSizeInBytes)[#](#_CPPv448hipsparseDpruneCsr2csrByPercentage_bufferSizeExt17hipsparseHandle_tiiiK19hipsparseMatDescr_tPKdPKiPKidK19hipsparseMatDescr_tPKdPKiPKi11pruneInfo_tP6size_t) Convert and prune by percentage a sparse CSR matrix into a sparse CSR matrix.

`hipsparseXpruneCsr2csrByPercentage_bufferSizeExt`

returns the size of the temporary buffer that is required by[hipsparseXpruneCsr2csrNnzByPercentage()](#hipsparse__prune__csr2csr__by__percentage_8h_1a49fdcbf9234f1ca31b1260183ffe49d7). The temporary storage buffer must be allocated by the user.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows in the sparse CSR matrix.**n**–**[in]**number of columns in the sparse CSR matrix.**nnzA**–**[in]**number of non-zeros in the sparse CSR matrix A.**descrA**–**[in]**descriptor of the sparse CSR matrix A. Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**csrValA**–**[in]**array of`nnzA`

elements containing the values of the sparse CSR matrix A.**csrRowPtrA**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix A.**csrColIndA**–**[in]**array of`nnzA`

elements containing the column indices of the sparse CSR matrix A.**percentage**–**[in]**`percentage>=0`

and`percentage<=100`

.**descrC**–**[in]**descriptor of the sparse CSR matrix C. Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**csrValC**–**[in]**array of`nnzC`

elements containing the values of the sparse CSR matrix C.**csrRowPtrC**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix C.**csrColIndC**–**[in]**array of`nnzC`

elements containing the column indices of the sparse CSR matrix C.**info**–**[in]**prune info structure.**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer required by[hipsparseSpruneCsr2csrNnzByPercentage()](#hipsparse__prune__csr2csr__by__percentage_8h_1a49fdcbf9234f1ca31b1260183ffe49d7),[hipsparseDpruneCsr2csrNnzByPercentage()](#hipsparse__prune__csr2csr__by__percentage_8h_1a210f79e55e8cc05aa115ca1ecea275f0),[hipsparseSpruneCsr2csrByPercentage()](#hipsparse__prune__csr2csr__by__percentage_8h_1aec7357dd8820e2aaf5aefce1c045a772), and[hipsparseDpruneCsr2csrByPercentage()](#hipsparse__prune__csr2csr__by__percentage_8h_1a3d297bb66bb60223b54403de8eb7e040).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

or`pBufferSizeInBytes`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.



## hipsparseXpruneCsr2csrNnzByPercentage()[#](#hipsparsexprunecsr2csrnnzbypercentage)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpruneCsr2csrNnzByPercentage([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnzA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const float *csrValA, const int *csrRowPtrA, const int *csrColIndA, float percentage, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, int *csrRowPtrC, int *nnzTotalDevHostPtr,[pruneInfo_t](types.html#_CPPv411pruneInfo_t)info, void *buffer)[#](#_CPPv437hipsparseSpruneCsr2csrNnzByPercentage17hipsparseHandle_tiiiK19hipsparseMatDescr_tPKfPKiPKifK19hipsparseMatDescr_tPiPi11pruneInfo_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDpruneCsr2csrNnzByPercentage([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnzA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const double *csrValA, const int *csrRowPtrA, const int *csrColIndA, double percentage, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, int *csrRowPtrC, int *nnzTotalDevHostPtr,[pruneInfo_t](types.html#_CPPv411pruneInfo_t)info, void *buffer)[#](#_CPPv437hipsparseDpruneCsr2csrNnzByPercentage17hipsparseHandle_tiiiK19hipsparseMatDescr_tPKdPKiPKidK19hipsparseMatDescr_tPiPi11pruneInfo_tPv) Convert and prune by percentage a sparse CSR matrix into a sparse CSR matrix.

`hipsparseXpruneCsr2csrNnzByPercentage`

computes the number of nonzero elements per row and the total number of nonzero elements in a sparse CSR matrix once elements less than the threshold are pruned from the matrix.Note

The routine does support asynchronous execution if the pointer mode is set to device.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows in the sparse CSR matrix.**n**–**[in]**number of columns in the sparse CSR matrix.**nnzA**–**[in]**number of non-zeros in the sparse CSR matrix A.**descrA**–**[in]**descriptor of the sparse CSR matrix A. Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**csrValA**–**[in]**array of`nnzA`

elements containing the values of the sparse CSR matrix A.**csrRowPtrA**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix A.**csrColIndA**–**[in]**array of`nnzA`

elements containing the column indices of the sparse CSR matrix A.**percentage**–**[in]**`percentage>=0`

and`percentage<=100`

.**descrC**–**[in]**descriptor of the sparse CSR matrix C. Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**csrRowPtrC**–**[out]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix C.**nnzTotalDevHostPtr**–**[out]**total number of nonzero elements in device or host memory.**info**–**[in]**prune info structure.**buffer**–**[out]**buffer allocated by the user whose size is determined by calling[hipsparseXpruneCsr2csrByPercentage_bufferSize()](#hipsparse__prune__csr2csr__by__percentage_8h_1a7a3cc1745b789370fb69d3068c9dd925).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`nnzA`

,`percentage`

,`descrA`

,`descrC`

,`info`

,`csrValA`

,`csrRowPtrA`

,`csrColIndA`

,`csrRowPtrC`

,`nnzTotalDevHostPtr`

or`buffer`

pointer is invalid.



## hipsparseXpruneCsr2csrByPercentage()[#](#hipsparsexprunecsr2csrbypercentage)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpruneCsr2csrByPercentage([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnzA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const float *csrValA, const int *csrRowPtrA, const int *csrColIndA, float percentage, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, float *csrValC, const int *csrRowPtrC, int *csrColIndC,[pruneInfo_t](types.html#_CPPv411pruneInfo_t)info, void *buffer)[#](#_CPPv434hipsparseSpruneCsr2csrByPercentage17hipsparseHandle_tiiiK19hipsparseMatDescr_tPKfPKiPKifK19hipsparseMatDescr_tPfPKiPi11pruneInfo_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDpruneCsr2csrByPercentage([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnzA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const double *csrValA, const int *csrRowPtrA, const int *csrColIndA, double percentage, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, double *csrValC, const int *csrRowPtrC, int *csrColIndC,[pruneInfo_t](types.html#_CPPv411pruneInfo_t)info, void *buffer)[#](#_CPPv434hipsparseDpruneCsr2csrByPercentage17hipsparseHandle_tiiiK19hipsparseMatDescr_tPKdPKiPKidK19hipsparseMatDescr_tPdPKiPi11pruneInfo_tPv) Convert and prune by percentage a sparse CSR matrix into a sparse CSR matrix.

This function converts the sparse CSR matrix A into a sparse CSR matrix C by pruning values in A that are less than the threshold. All the parameters are assumed to have been pre-allocated by the user. The user first calls

[hipsparseXpruneCsr2csr_bufferSize()](#hipsparse__prune__csr2csr_8h_1a16786194717117a4902032dd8afbebe0)to determine the size of the buffer used by[hipsparseXpruneCsr2csrNnz()](#hipsparse__prune__csr2csr_8h_1ac7e23d0e39782b88b53e88effc2ef58b)and`hipsparseXpruneCsr2csr()`

which the user then allocates. The user then allocates`csrRowPtrC`

to have`m+1`

elements and then calls[hipsparseXpruneCsr2csrNnz()](#hipsparse__prune__csr2csr_8h_1ac7e23d0e39782b88b53e88effc2ef58b)which fills in the`csrRowPtrC`

array stores then number of elements that are larger than the pruning`threshold`

in`nnzTotalDevHostPtr`

. The user then calls`hipsparseXpruneCsr2csr()`

to complete the conversion. It is executed asynchronously with respect to the host and may return control to the application on the host before the entire result is ready.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows in the sparse CSR matrix.**n**–**[in]**number of columns in the sparse CSR matrix.**nnzA**–**[in]**number of non-zeros in the sparse CSR matrix A.**descrA**–**[in]**descriptor of the sparse CSR matrix A. Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**csrValA**–**[in]**array of`nnzA`

elements containing the values of the sparse CSR matrix A.**csrRowPtrA**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix A.**csrColIndA**–**[in]**array of`nnzA`

elements containing the column indices of the sparse CSR matrix A.**percentage**–**[in]**`percentage>=0`

and`percentage<=100`

.**descrC**–**[in]**descriptor of the sparse CSR matrix C. Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**csrValC**–**[out]**array of`nnz_C`

elements containing the values of the sparse CSR matrix C.**csrRowPtrC**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix C.**csrColIndC**–**[out]**array of`nnz_C`

elements containing the column indices of the sparse CSR matrix C.**info**–**[in]**prune info structure.**buffer**–**[in]**buffer allocated by the user whose size is determined by calling[hipsparseXpruneCsr2csrByPercentage_bufferSize()](#hipsparse__prune__csr2csr__by__percentage_8h_1a7a3cc1745b789370fb69d3068c9dd925).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`nnzA`

,`percentage`

,`descrA`

,`descrC`

,`info`

,`csrValA`

,`csrRowPtrA`

,`csrColIndA`

,`csrValC`

,`csrRowPtrC`

,`csrColIndC`

or`buffer`

pointer is invalid.



## hipsparseXhyb2csr()[#](#hipsparsexhyb2csr)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseShyb2csr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const[hipsparseHybMat_t](types.html#_CPPv417hipsparseHybMat_t)hybA, float *csrSortedValA, int *csrSortedRowPtrA, int *csrSortedColIndA)[#](#_CPPv417hipsparseShyb2csr17hipsparseHandle_tK19hipsparseMatDescr_tK17hipsparseHybMat_tPfPiPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDhyb2csr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const[hipsparseHybMat_t](types.html#_CPPv417hipsparseHybMat_t)hybA, double *csrSortedValA, int *csrSortedRowPtrA, int *csrSortedColIndA)[#](#_CPPv417hipsparseDhyb2csr17hipsparseHandle_tK19hipsparseMatDescr_tK17hipsparseHybMat_tPdPiPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseChyb2csr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const[hipsparseHybMat_t](types.html#_CPPv417hipsparseHybMat_t)hybA, hipComplex *csrSortedValA, int *csrSortedRowPtrA, int *csrSortedColIndA)[#](#_CPPv417hipsparseChyb2csr17hipsparseHandle_tK19hipsparseMatDescr_tK17hipsparseHybMat_tP10hipComplexPiPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZhyb2csr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const[hipsparseHybMat_t](types.html#_CPPv417hipsparseHybMat_t)hybA, hipDoubleComplex *csrSortedValA, int *csrSortedRowPtrA, int *csrSortedColIndA)[#](#_CPPv417hipsparseZhyb2csr17hipsparseHandle_tK19hipsparseMatDescr_tK17hipsparseHybMat_tP16hipDoubleComplexPiPi) Convert a sparse HYB matrix into a sparse CSR matrix.

`hipsparseXhyb2csr`

converts a HYB matrix into a CSR matrix.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**descrA**–**[in]**descriptor of the sparse HYB matrix. Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**hybA**–**[in]**sparse matrix in HYB format.**csrSortedValA**–**[out]**array containing the values of the sparse CSR matrix.**csrSortedRowPtrA**–**[out]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csrSortedColIndA**–**[out]**array containing the column indices of the sparse CSR matrix.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`descrA`

,`hybA`

,`csrSortedValA`

,`csrSortedRowPtrA`

or`csrSortedColIndA`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.**HIPSPARSE_STATUS_NOT_SUPPORTED**–[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXcoo2csr()[#](#hipsparsexcoo2csr)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseXcoo2csr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, const int *cooRowInd, int nnz, int m, int *csrRowPtr,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase)[#](#_CPPv417hipsparseXcoo2csr17hipsparseHandle_tPKiiiPi20hipsparseIndexBase_t) Convert a sparse COO matrix into a sparse CSR matrix.

`hipsparseXcoo2csr`

converts the COO array containing the row indices into a CSR array of row offsets, that point to the start of every row. It is assumed that the COO row index array is sorted and that all arrays have been allocated prior to calling hipsparseXcoo2csr.For example, given the COO row indices array:

\[ \begin{align} \text{cooRowInd} &= \begin{bmatrix} 0 & 0 & 1 & 2 & 2 & 4 & 4 & 4 \end{bmatrix} \end{align} \]the resulting CSR row pointer array after calling

`hipsparseXcoo2csr`

is:\[ \begin{align} \text{csrRowPtr} &= \begin{bmatrix} 0 & 2 & 3 & 5 & 8 \end{bmatrix} \end{align} \]**Example**int main(int argc, char* argv[]) { // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // Sparse matrix in COO format // 1 2 0 3 0 // A = 0 4 5 0 0 // 6 0 0 7 8 int hcooRowInd[8] = {0, 0, 0, 1, 1, 2, 2, 2}; int hcooColInd[8] = {0, 1, 3, 1, 2, 0, 3, 4}; float hcooVal[8] = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f}; int m = 3; int n = 5; int nnz = 8; hipsparseIndexBase_t base = HIPSPARSE_INDEX_BASE_ZERO; int* dcooRowInd = nullptr; int* dcooColInd = nullptr; HIP_CHECK(hipMalloc((void**)&dcooRowInd, sizeof(int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcooColInd, sizeof(int) * nnz)); HIP_CHECK(hipMemcpy(dcooRowInd, hcooRowInd, sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcooColInd, hcooColInd, sizeof(int) * nnz, hipMemcpyHostToDevice)); int* dcsrRowPtr = nullptr; HIP_CHECK(hipMalloc((void**)&dcsrRowPtr, sizeof(int) * (m + 1))); HIPSPARSE_CHECK(hipsparseXcoo2csr(handle, dcooRowInd, nnz, m, dcsrRowPtr, base)); HIP_CHECK(hipFree(dcooRowInd)); HIP_CHECK(hipFree(dcooColInd)); HIP_CHECK(hipFree(dcsrRowPtr)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); return 0; }


Note

It can also be used, to convert a COO array containing the column indices into a CSC array of column offsets, that point to the start of every column. Then, it is assumed that the COO column index array is sorted, instead.

Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**cooRowInd**–**[in]**array of`nnz`

elements containing the row indices of the sparse COO matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**m**–**[in]**number of rows of the sparse CSR matrix.**csrRowPtr**–**[out]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**idxBase**–**[in]**[HIPSPARSE_INDEX_BASE_ZERO](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4a14913ab324aaea1154abd00ee7c50b63)or[HIPSPARSE_INDEX_BASE_ONE](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4ae48a9ab138ca9588d485c078bddc0792).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`nnz`

,`cooRowInd`

or`csrRowPtr`

pointer is invalid.



## hipsparseCreateIdentityPermutation()[#](#hipsparsecreateidentitypermutation)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCreateIdentityPermutation([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int n, int *p)[#](#_CPPv434hipsparseCreateIdentityPermutation17hipsparseHandle_tiPi) Create the identity map.

`hipsparseCreateIdentityPermutation`

stores the identity map in`p`

, such that \(p = 0:1:(n-1)\).for(i = 0; i < n; ++i) { p[i] = i; }

**Example**int main(int argc, char* argv[]) { // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); int n = 10; int* dperm = nullptr; HIP_CHECK(hipMalloc((void**)&dperm, sizeof(int) * n)); HIPSPARSE_CHECK(hipsparseCreateIdentityPermutation(handle, n, dperm)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**n**–**[in]**size of the map`p`

.**p**–**[out]**array of`n`

integers containing the map.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`n`

or`p`

pointer is invalid.



## hipsparseXcsrsort_bufferSizeExt()[#](#hipsparsexcsrsort-buffersizeext)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseXcsrsort_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnz, const int *csrRowPtr, const int *csrColInd, size_t *pBufferSizeInBytes)[#](#_CPPv431hipsparseXcsrsort_bufferSizeExt17hipsparseHandle_tiiiPKiPKiP6size_t) Sort a sparse CSR matrix.

`hipsparseXcsrsort_bufferSizeExt`

returns the size of the temporary storage buffer in bytes required by[hipsparseXcsrsort()](#hipsparse__csrsort_8h_1ae15af50d5195cf1adb4b2dd38d2349ed). The temporary storage buffer must be allocated by the user.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix.**n**–**[in]**number of columns of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**csrRowPtr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csrColInd**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer required by[hipsparseXcsrsort()](#hipsparse__csrsort_8h_1ae15af50d5195cf1adb4b2dd38d2349ed).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`nnz`

,`csrRowPtr`

,`csrColInd`

or`pBufferSizeInBytes`

pointer is invalid.



## hipsparseXcsrsort()[#](#hipsparsexcsrsort)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseXcsrsort([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const int *csrRowPtr, int *csrColInd, int *P, void *pBuffer)[#](#_CPPv417hipsparseXcsrsort17hipsparseHandle_tiiiK19hipsparseMatDescr_tPKiPiPiPv) Sort a sparse CSR matrix.

`hipsparseXcsrsort`

sorts a matrix in CSR format. The sorted permutation vector`P`

can be used to obtain sorted`csrVal`

array. In this case,`P`

must be initialized as the identity permutation, see[hipsparseCreateIdentityPermutation()](#hipsparse__create__identity__permutation_8h_1a0f8af98c53b893f48787dd41fe1f761f). To apply the permutation vector to the CSR values, see hipsparse[hipsparseXgthr()](level1.html#hipsparse__gthr_8h_1aa87741f7b416835d59474b40c91aaee8).`hipsparseXcsrsort`

requires extra temporary storage buffer that has to be allocated by the user. Storage buffer size can be determined by[hipsparseXcsrsort_bufferSizeExt()](#hipsparse__csrsort_8h_1abe22f4642f1c9537f6adf6f0acda5be3).**Example**int main(int argc, char* argv[]) { // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); hipsparseMatDescr_t descr; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&descr)); // Sparse matrix in CSR format (columns unsorted) // 1 2 0 3 0 // A = 0 4 5 0 0 // 6 0 0 7 8 int hcsrRowPtr[4] = {0, 3, 5, 8}; int hcsrColInd[8] = {3, 1, 0, 2, 1, 0, 4, 3}; float hcsrVal[8] = {3.0f, 2.0f, 1.0f, 5.0f, 4.0f, 6.0f, 8.0f, 7.0f}; int m = 3; int n = 5; int nnz = 8; int* dcsrRowPtr = nullptr; int* dcsrColInd = nullptr; float* dcsrVal = nullptr; HIP_CHECK(hipMalloc((void**)&dcsrRowPtr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&dcsrColInd, sizeof(int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcsrVal, sizeof(float) * nnz)); HIP_CHECK(hipMemcpy(dcsrRowPtr, hcsrRowPtr, sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrColInd, hcsrColInd, sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrVal, hcsrVal, sizeof(float) * nnz, hipMemcpyHostToDevice)); size_t bufferSize; HIPSPARSE_CHECK( hipsparseXcsrsort_bufferSizeExt(handle, m, n, nnz, dcsrRowPtr, dcsrColInd, &bufferSize)); void* dbuffer = nullptr; HIP_CHECK(hipMalloc((void**)&dbuffer, bufferSize)); int* dperm = nullptr; HIP_CHECK(hipMalloc((void**)&dperm, sizeof(int) * nnz)); HIPSPARSE_CHECK(hipsparseCreateIdentityPermutation(handle, nnz, dperm)); HIPSPARSE_CHECK( hipsparseXcsrsort(handle, m, n, nnz, descr, dcsrRowPtr, dcsrColInd, dperm, dbuffer)); float* dcsrValSorted = nullptr; HIP_CHECK(hipMalloc((void**)&dcsrValSorted, sizeof(float) * nnz)); HIPSPARSE_CHECK( hipsparseSgthr(handle, nnz, dcsrVal, dcsrValSorted, dperm, HIPSPARSE_INDEX_BASE_ZERO)); HIP_CHECK(hipFree(dcsrRowPtr)); HIP_CHECK(hipFree(dcsrColInd)); HIP_CHECK(hipFree(dcsrVal)); HIP_CHECK(hipFree(dcsrValSorted)); HIP_CHECK(hipFree(dbuffer)); HIP_CHECK(hipFree(dperm)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(descr)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); return 0; }


Note

`P`

can be`NULL`

if a sorted permutation vector is not required.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix.**n**–**[in]**number of columns of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**descrA**–**[in]**descriptor of the sparse CSR matrix. Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**csrRowPtr**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csrColInd**–**[inout]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**P**–**[inout]**array of`nnz`

integers containing the unsorted map indices, can be`NULL`

.**pBuffer**–**[in]**temporary storage buffer allocated by the user, size is returned by[hipsparseXcsrsort_bufferSizeExt()](#hipsparse__csrsort_8h_1abe22f4642f1c9537f6adf6f0acda5be3).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`nnz`

,`descrA`

,`csrRowPtr`

,`csrColInd`

or`pBuffer`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.**HIPSPARSE_STATUS_NOT_SUPPORTED**–[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXcscsort_bufferSizeExt()[#](#hipsparsexcscsort-buffersizeext)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseXcscsort_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnz, const int *cscColPtr, const int *cscRowInd, size_t *pBufferSizeInBytes)[#](#_CPPv431hipsparseXcscsort_bufferSizeExt17hipsparseHandle_tiiiPKiPKiP6size_t) Sort a sparse CSC matrix.

`hipsparseXcscsort_bufferSizeExt`

returns the size of the temporary storage buffer in bytes required by[hipsparseXcscsort()](#hipsparse__cscsort_8h_1a45702012a757ba8e9d26d1669091d5e5). The temporary storage buffer must be allocated by the user.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the sparse CSC matrix.**n**–**[in]**number of columns of the sparse CSC matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSC matrix.**cscColPtr**–**[in]**array of`n+1`

elements that point to the start of every column of the sparse CSC matrix.**cscRowInd**–**[in]**array of`nnz`

elements containing the row indices of the sparse CSC matrix.**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer required by[hipsparseXcscsort()](#hipsparse__cscsort_8h_1a45702012a757ba8e9d26d1669091d5e5).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`nnz`

,`cscColPtr`

,`cscRowInd`

or`pBufferSizeInBytes`

pointer is invalid.



## hipsparseXcscsort()[#](#hipsparsexcscsort)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseXcscsort([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const int *cscColPtr, int *cscRowInd, int *P, void *pBuffer)[#](#_CPPv417hipsparseXcscsort17hipsparseHandle_tiiiK19hipsparseMatDescr_tPKiPiPiPv) Sort a sparse CSC matrix.

`hipsparseXcscsort`

sorts a matrix in CSC format. The sorted permutation vector`P`

can be used to obtain sorted`cscVal`

array. In this case,`P`

must be initialized as the identity permutation, see[hipsparseCreateIdentityPermutation()](#hipsparse__create__identity__permutation_8h_1a0f8af98c53b893f48787dd41fe1f761f). To apply the permutation vector to the CSC values, see hipsparse[hipsparseXgthr()](level1.html#hipsparse__gthr_8h_1aa87741f7b416835d59474b40c91aaee8).`hipsparseXcscsort`

requires extra temporary storage buffer that has to be allocated by the user. Storage buffer size can be determined by[hipsparseXcscsort_bufferSizeExt()](#hipsparse__cscsort_8h_1a6fc010a5ae4873248697c480b0762848).**Example**int main(int argc, char* argv[]) { // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); hipsparseMatDescr_t descr; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&descr)); // Sparse matrix in CSC format (unsorted row indices) // 1 2 0 3 0 // A = 0 4 5 0 0 // 6 0 0 7 8 int hcscRowInd[8] = {2, 0, 1, 0, 1, 2, 0, 2}; int hcscColPtr[6] = {0, 2, 4, 5, 7, 8}; float hcscVal[8] = {6.0f, 1.0f, 4.0f, 2.0f, 5.0f, 7.0f, 3.0f, 8.0f}; int m = 3; int n = 5; int nnz = 8; int* dcscRowInd = nullptr; int* dcscColPtr = nullptr; float* dcscVal = nullptr; HIP_CHECK(hipMalloc((void**)&dcscRowInd, sizeof(int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcscColPtr, sizeof(int) * (n + 1))); HIP_CHECK(hipMalloc((void**)&dcscVal, sizeof(float) * nnz)); HIP_CHECK(hipMemcpy(dcscRowInd, hcscRowInd, sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcscColPtr, hcscColPtr, sizeof(int) * (n + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcscVal, hcscVal, sizeof(float) * nnz, hipMemcpyHostToDevice)); size_t bufferSize; HIPSPARSE_CHECK( hipsparseXcscsort_bufferSizeExt(handle, m, n, nnz, dcscColPtr, dcscRowInd, &bufferSize)); void* dbuffer = nullptr; HIP_CHECK(hipMalloc((void**)&dbuffer, bufferSize)); int* dperm = nullptr; HIP_CHECK(hipMalloc((void**)&dperm, sizeof(int) * nnz)); HIPSPARSE_CHECK(hipsparseCreateIdentityPermutation(handle, nnz, dperm)); HIPSPARSE_CHECK( hipsparseXcscsort(handle, m, n, nnz, descr, dcscColPtr, dcscRowInd, dperm, dbuffer)); float* dcscValSorted = nullptr; HIP_CHECK(hipMalloc((void**)&dcscValSorted, sizeof(float) * nnz)); HIPSPARSE_CHECK( hipsparseSgthr(handle, nnz, dcscVal, dcscValSorted, dperm, HIPSPARSE_INDEX_BASE_ZERO)); HIP_CHECK(hipFree(dcscRowInd)); HIP_CHECK(hipFree(dcscColPtr)); HIP_CHECK(hipFree(dcscVal)); HIP_CHECK(hipFree(dcscValSorted)); HIP_CHECK(hipFree(dbuffer)); HIP_CHECK(hipFree(dperm)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(descr)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); return 0; }


Note

`P`

can be`NULL`

if a sorted permutation vector is not required.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the sparse CSC matrix.**n**–**[in]**number of columns of the sparse CSC matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSC matrix.**descrA**–**[in]**descriptor of the sparse CSC matrix. Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**cscColPtr**–**[in]**array of`n+1`

elements that point to the start of every column of the sparse CSC matrix.**cscRowInd**–**[inout]**array of`nnz`

elements containing the row indices of the sparse CSC matrix.**P**–**[inout]**array of`nnz`

integers containing the unsorted map indices, can be`NULL`

.**pBuffer**–**[in]**temporary storage buffer allocated by the user, size is returned by[hipsparseXcscsort_bufferSizeExt()](#hipsparse__cscsort_8h_1a6fc010a5ae4873248697c480b0762848).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`nnz`

,`descrA`

,`cscColPtr`

,`cscRowInd`

or`pBuffer`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.**HIPSPARSE_STATUS_NOT_SUPPORTED**–[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXcoosort_bufferSizeExt()[#](#hipsparsexcoosort-buffersizeext)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseXcoosort_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnz, const int *cooRows, const int *cooCols, size_t *pBufferSizeInBytes)[#](#_CPPv431hipsparseXcoosort_bufferSizeExt17hipsparseHandle_tiiiPKiPKiP6size_t) Sort a sparse COO matrix.

`hipsparseXcoosort_bufferSizeExt`

returns the size of the temporary storage buffer in bytes required by[hipsparseXcoosortByRow()](#hipsparse__coosort_8h_1add5a60b4936e71fadd4b1c9d7bd90e78)and[hipsparseXcoosortByColumn()](#hipsparse__coosort_8h_1aac0c90ccb5292891a696e886163e6515). The temporary storage buffer must be allocated by the user.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the sparse COO matrix.**n**–**[in]**number of columns of the sparse COO matrix.**nnz**–**[in]**number of non-zero entries of the sparse COO matrix.**cooRows**–**[in]**array of`nnz`

elements containing the row indices of the sparse COO matrix.**cooCols**–**[in]**array of`nnz`

elements containing the column indices of the sparse COO matrix.**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer required by[hipsparseXcoosortByRow()](#hipsparse__coosort_8h_1add5a60b4936e71fadd4b1c9d7bd90e78)and[hipsparseXcoosortByColumn()](#hipsparse__coosort_8h_1aac0c90ccb5292891a696e886163e6515).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`nnz`

,`cooRows`

,`cooCols`

or`pBufferSizeInBytes`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.



## hipsparseXcoosortByRow()[#](#hipsparsexcoosortbyrow)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseXcoosortByRow([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnz, int *cooRows, int *cooCols, int *P, void *pBuffer)[#](#_CPPv422hipsparseXcoosortByRow17hipsparseHandle_tiiiPiPiPiPv) Sort a sparse COO matrix by row.

`hipsparseXcoosortByRow`

sorts a matrix in COO format by row. The sorted permutation vector`P`

can be used to obtain sorted`cooVal`

array. In this case,`P`

must be initialized as the identity permutation, see[hipsparseCreateIdentityPermutation()](#hipsparse__create__identity__permutation_8h_1a0f8af98c53b893f48787dd41fe1f761f). To apply the permutation vector to the COO values, see hipsparse[hipsparseXgthr()](level1.html#hipsparse__gthr_8h_1aa87741f7b416835d59474b40c91aaee8).`hipsparseXcoosortByRow`

requires extra temporary storage buffer that has to be allocated by the user. Storage buffer size can be determined by[hipsparseXcoosort_bufferSizeExt()](#hipsparse__coosort_8h_1a04bfea582ca088785763421f253b2fda).**Example**int main(int argc, char* argv[]) { // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // Sparse matrix in COO format (with unsorted row indices) // 1 2 0 3 0 // A = 0 4 5 0 0 // 6 0 0 7 8 int hcooRowInd[8] = {0, 2, 0, 1, 1, 0, 2, 2}; int hcooColInd[8] = {0, 0, 1, 1, 2, 3, 3, 4}; float hcooVal[8] = {1.0f, 6.0f, 2.0f, 4.0f, 5.0f, 3.0f, 7.0f, 8.0f}; int m = 3; int n = 5; int nnz = 8; hipsparseIndexBase_t base = HIPSPARSE_INDEX_BASE_ZERO; int* dcooRowInd = nullptr; int* dcooColInd = nullptr; float* dcooVal = nullptr; HIP_CHECK(hipMalloc((void**)&dcooRowInd, sizeof(int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcooColInd, sizeof(int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcooVal, sizeof(float) * nnz)); HIP_CHECK(hipMemcpy(dcooRowInd, hcooRowInd, sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcooColInd, hcooColInd, sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcooVal, hcooVal, sizeof(float) * nnz, hipMemcpyHostToDevice)); size_t bufferSize; HIPSPARSE_CHECK( hipsparseXcoosort_bufferSizeExt(handle, m, n, nnz, dcooRowInd, dcooColInd, &bufferSize)); void* dbuffer = nullptr; HIP_CHECK(hipMalloc((void**)&dbuffer, bufferSize)); int* dperm = nullptr; HIP_CHECK(hipMalloc((void**)&dperm, sizeof(int) * nnz)); HIPSPARSE_CHECK(hipsparseCreateIdentityPermutation(handle, nnz, dperm)); HIPSPARSE_CHECK( hipsparseXcoosortByRow(handle, m, n, nnz, dcooRowInd, dcooColInd, dperm, dbuffer)); float* dcooValSorted = nullptr; HIP_CHECK(hipMalloc((void**)&dcooValSorted, sizeof(float) * nnz)); HIPSPARSE_CHECK(hipsparseSgthr(handle, nnz, dcooVal, dcooValSorted, dperm, base)); HIP_CHECK(hipFree(dcooRowInd)); HIP_CHECK(hipFree(dcooColInd)); HIP_CHECK(hipFree(dcooVal)); HIP_CHECK(hipFree(dcooValSorted)); HIP_CHECK(hipFree(dperm)); HIP_CHECK(hipFree(dbuffer)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); return 0; }


Note

`P`

can be`NULL`

if a sorted permutation vector is not required.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the sparse COO matrix.**n**–**[in]**number of columns of the sparse COO matrix.**nnz**–**[in]**number of non-zero entries of the sparse COO matrix.**cooRows**–**[inout]**array of`nnz`

elements containing the row indices of the sparse COO matrix.**cooCols**–**[inout]**array of`nnz`

elements containing the column indices of the sparse COO matrix.**P**–**[inout]**array of`nnz`

integers containing the unsorted map indices, can be`NULL`

.**pBuffer**–**[in]**temporary storage buffer allocated by the user, size is returned by[hipsparseXcoosort_bufferSizeExt()](#hipsparse__coosort_8h_1a04bfea582ca088785763421f253b2fda).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`nnz`

,`cooRows`

,`cooCols`

or`pBuffer`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.



## hipsparseXcoosortByColumn()[#](#hipsparsexcoosortbycolumn)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseXcoosortByColumn([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnz, int *cooRows, int *cooCols, int *P, void *pBuffer)[#](#_CPPv425hipsparseXcoosortByColumn17hipsparseHandle_tiiiPiPiPiPv) Sort a sparse COO matrix by column.

`hipsparseXcoosortByColumn`

sorts a matrix in COO format by column. The sorted permutation vector`P`

can be used to obtain sorted`cooVal`

array. In this case,`P`

must be initialized as the identity permutation, see[hipsparseCreateIdentityPermutation()](#hipsparse__create__identity__permutation_8h_1a0f8af98c53b893f48787dd41fe1f761f). To apply the permutation vector to the COO values, see hipsparse[hipsparseXgthr()](level1.html#hipsparse__gthr_8h_1aa87741f7b416835d59474b40c91aaee8).`hipsparseXcoosortByColumn`

requires extra temporary storage buffer that has to be allocated by the user. Storage buffer size can be determined by[hipsparseXcoosort_bufferSizeExt()](#hipsparse__coosort_8h_1a04bfea582ca088785763421f253b2fda).**Example**int main(int argc, char* argv[]) { // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // Sparse matrix in COO format (with unsorted column indices) // 1 2 0 3 0 // A = 0 4 5 0 0 // 6 0 0 7 8 int hcooRowInd[8] = {0, 0, 0, 1, 1, 2, 2, 2}; int hcooColInd[8] = {0, 1, 3, 1, 2, 0, 3, 4}; float hcooVal[8] = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f}; int m = 3; int n = 5; int nnz = 8; hipsparseIndexBase_t base = HIPSPARSE_INDEX_BASE_ZERO; int* dcooRowInd = nullptr; int* dcooColInd = nullptr; float* dcooVal = nullptr; HIP_CHECK(hipMalloc((void**)&dcooRowInd, sizeof(int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcooColInd, sizeof(int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcooVal, sizeof(float) * nnz)); HIP_CHECK(hipMemcpy(dcooRowInd, hcooRowInd, sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcooColInd, hcooColInd, sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcooVal, hcooVal, sizeof(float) * nnz, hipMemcpyHostToDevice)); size_t bufferSize; HIPSPARSE_CHECK( hipsparseXcoosort_bufferSizeExt(handle, m, n, nnz, dcooRowInd, dcooColInd, &bufferSize)); void* dbuffer = nullptr; HIP_CHECK(hipMalloc((void**)&dbuffer, bufferSize)); int* dperm = nullptr; HIP_CHECK(hipMalloc((void**)&dperm, sizeof(int) * nnz)); HIPSPARSE_CHECK(hipsparseCreateIdentityPermutation(handle, nnz, dperm)); HIPSPARSE_CHECK( hipsparseXcoosortByColumn(handle, m, n, nnz, dcooRowInd, dcooColInd, dperm, dbuffer)); float* dcooValSorted = nullptr; HIP_CHECK(hipMalloc((void**)&dcooValSorted, sizeof(float) * nnz)); HIPSPARSE_CHECK(hipsparseSgthr(handle, nnz, dcooVal, dcooValSorted, dperm, base)); HIP_CHECK(hipFree(dcooRowInd)); HIP_CHECK(hipFree(dcooColInd)); HIP_CHECK(hipFree(dcooVal)); HIP_CHECK(hipFree(dcooValSorted)); HIP_CHECK(hipFree(dperm)); HIP_CHECK(hipFree(dbuffer)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); return 0; }


Note

`P`

can be`NULL`

if a sorted permutation vector is not required.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the sparse COO matrix.**n**–**[in]**number of columns of the sparse COO matrix.**nnz**–**[in]**number of non-zero entries of the sparse COO matrix.**cooRows**–**[inout]**array of`nnz`

elements containing the row indices of the sparse COO matrix.**cooCols**–**[inout]**array of`nnz`

elements containing the column indices of the sparse COO matrix.**P**–**[inout]**array of`nnz`

integers containing the unsorted map indices, can be`NULL`

.**pBuffer**–**[in]**temporary storage buffer allocated by the user, size is returned by[hipsparseXcoosort_bufferSizeExt()](#hipsparse__coosort_8h_1a04bfea582ca088785763421f253b2fda).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`nnz`

,`cooRows`

,`cooCols`

or`pBuffer`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.



## hipsparseXgebsr2gebsr_bufferSize()[#](#hipsparsexgebsr2gebsr-buffersize)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSgebsr2gebsr_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const float *bsrValA, const int *bsrRowPtrA, const int *bsrColIndA, int rowBlockDimA, int colBlockDimA, int rowBlockDimC, int colBlockDimC, int *pBufferSizeInBytes)[#](#_CPPv432hipsparseSgebsr2gebsr_bufferSize17hipsparseHandle_t20hipsparseDirection_tiiiK19hipsparseMatDescr_tPKfPKiPKiiiiiPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDgebsr2gebsr_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const double *bsrValA, const int *bsrRowPtrA, const int *bsrColIndA, int rowBlockDimA, int colBlockDimA, int rowBlockDimC, int colBlockDimC, int *pBufferSizeInBytes)[#](#_CPPv432hipsparseDgebsr2gebsr_bufferSize17hipsparseHandle_t20hipsparseDirection_tiiiK19hipsparseMatDescr_tPKdPKiPKiiiiiPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCgebsr2gebsr_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipComplex *bsrValA, const int *bsrRowPtrA, const int *bsrColIndA, int rowBlockDimA, int colBlockDimA, int rowBlockDimC, int colBlockDimC, int *pBufferSizeInBytes)[#](#_CPPv432hipsparseCgebsr2gebsr_bufferSize17hipsparseHandle_t20hipsparseDirection_tiiiK19hipsparseMatDescr_tPK10hipComplexPKiPKiiiiiPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZgebsr2gebsr_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipDoubleComplex *bsrValA, const int *bsrRowPtrA, const int *bsrColIndA, int rowBlockDimA, int colBlockDimA, int rowBlockDimC, int colBlockDimC, int *pBufferSizeInBytes)[#](#_CPPv432hipsparseZgebsr2gebsr_bufferSize17hipsparseHandle_t20hipsparseDirection_tiiiK19hipsparseMatDescr_tPK16hipDoubleComplexPKiPKiiiiiPi) This function computes the the size of the user allocated temporary storage buffer used when converting a sparse GEBSR matrix to another sparse GEBSR matrix.

`hipsparseXgebsr2gebsr_bufferSize`

returns the size of the temporary storage buffer that is required by[hipsparseXgebsr2gebsrNnz()](#hipsparse__gebsr2gebsr_8h_1a60f114467872e19c249e19dbd83da63e)and[hipsparseXgebsr2gebsr()](#hipsparse__gebsr2gebsr_8h_1a40443d9894bee3914e8a3928d5be8bc2). The temporary storage buffer must be allocated by the user.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**dirA**–**[in]**the storage format of the blocks,[HIPSPARSE_DIRECTION_ROW](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59ae8589abecf2fbfb4b6307fd9dacd9e55)or[HIPSPARSE_DIRECTION_COLUMN](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59a32e23f292b2377f6e60bdc90274c796c)**mb**–**[in]**number of block rows of the general BSR sparse matrix \(A\).**nb**–**[in]**number of block columns of the general BSR sparse matrix \(A\).**nnzb**–**[in]**number of blocks in the general BSR sparse matrix \(A\).**descrA**–**[in]**the descriptor of the general BSR sparse matrix \(A\), the supported matrix type is[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)and also any valid value of the[hipsparseIndexBase_t](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4).**bsrValA**–**[in]**array of`nnzb*rowBlockDimA*colBlockDimA`

containing the values of the sparse general BSR matrix \(A\).**bsrRowPtrA**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse general BSR matrix \(A\).**bsrColIndA**–**[in]**array of`nnzb`

elements containing the block column indices of the sparse general BSR matrix \(A\).**rowBlockDimA**–**[in]**row size of the blocks in the sparse general BSR matrix \(A\).**colBlockDimA**–**[in]**column size of the blocks in the sparse general BSR matrix \(A\).**rowBlockDimC**–**[in]**row size of the blocks in the sparse general BSR matrix \(C\).**colBlockDimC**–**[in]**column size of the blocks in the sparse general BSR matrix \(C\).**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer required by[hipsparseXgebsr2gebsrNnz()](#hipsparse__gebsr2gebsr_8h_1a60f114467872e19c249e19dbd83da63e),[hipsparseSgebsr2gebsr()](#hipsparse__gebsr2gebsr_8h_1a40443d9894bee3914e8a3928d5be8bc2),[hipsparseDgebsr2gebsr()](#hipsparse__gebsr2gebsr_8h_1a2efe5d6fb96085dcb975b50f7ab0501b),[hipsparseCgebsr2gebsr()](#hipsparse__gebsr2gebsr_8h_1af0e34975374064709cbf32311c990422), and[hipsparseZgebsr2gebsr()](#hipsparse__gebsr2gebsr_8h_1a52b6586520dedc00a10971441c47f4a6).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`mb`

,`nb`

,`nnzb`

,`rowBlockDimA`

,`colBlockDimA`

,`rowBlockDimC`

,`colBlockDimC`

,`bsrRowPtrA`

,`bsrColIndA`

,`descrA`

or`pBufferSizeInBytes`

pointer is invalid.



## hipsparseXgebsr2gebsrNnz()[#](#hipsparsexgebsr2gebsrnnz)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseXgebsr2gebsrNnz([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const int *bsrRowPtrA, const int *bsrColIndA, int rowBlockDimA, int colBlockDimA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, int *bsrRowPtrC, int rowBlockDimC, int colBlockDimC, int *nnzTotalDevHostPtr, void *buffer)[#](#_CPPv424hipsparseXgebsr2gebsrNnz17hipsparseHandle_t20hipsparseDirection_tiiiK19hipsparseMatDescr_tPKiPKiiiK19hipsparseMatDescr_tPiiiPiPv) This function is used when converting a GEBSR sparse matrix \(A\) to another GEBSR sparse matrix \(C\). Specifically, this function determines the number of non-zero blocks that will exist in \(C\) (stored using either a host or device pointer), and computes the row pointer array for \(C\).

The routine does support asynchronous execution.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**dirA**–**[in]**the storage format of the blocks,[HIPSPARSE_DIRECTION_ROW](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59ae8589abecf2fbfb4b6307fd9dacd9e55)or[HIPSPARSE_DIRECTION_COLUMN](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59a32e23f292b2377f6e60bdc90274c796c)**mb**–**[in]**number of block rows of the general BSR sparse matrix \(A\).**nb**–**[in]**number of block columns of the general BSR sparse matrix \(A\).**nnzb**–**[in]**number of blocks in the general BSR sparse matrix \(A\).**descrA**–**[in]**the descriptor of the general BSR sparse matrix \(A\), the supported matrix type is[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)and also any valid value of the[hipsparseIndexBase_t](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4).**bsrRowPtrA**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse general BSR matrix \(A\).**bsrColIndA**–**[in]**array of`nnzb`

elements containing the block column indices of the sparse general BSR matrix`A`

.**rowBlockDimA**–**[in]**row size of the blocks in the sparse general BSR matrix \(A\).**colBlockDimA**–**[in]**column size of the blocks in the sparse general BSR matrix \(A\).**descrC**–**[in]**the descriptor of the general BSR sparse matrix \(C\), the supported matrix type is[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)and also any valid value of the[hipsparseIndexBase_t](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4).**bsrRowPtrC**–**[in]**array of`mbC+1`

elements that point to the start of every block row of the sparse general BSR matrix \(C\) where`mbC`

= (`m+rowBlockDimC-1`

) /`rowBlockDimC`

.**rowBlockDimC**–**[in]**row size of the blocks in the sparse general BSR matrix \(C\).**colBlockDimC**–**[in]**column size of the blocks in the sparse general BSR matrix \(C\).**nnzTotalDevHostPtr**–**[out]**total number of nonzero blocks in general BSR sparse matrix \(C\) stored using device or host memory.**buffer**–**[out]**buffer allocated by the user whose size is determined by calling[hipsparseXgebsr2gebsr_bufferSize()](#hipsparse__gebsr2gebsr_8h_1a0315a9ada5ccb960371a2430cb2e652e).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`mb`

,`nb`

,`nnzb`

,`rowBlockDimA`

,`colBlockDimA`

,`rowBlockDimC`

,`colBlockDimC`

,`bsrRowPtrA`

,`bsrColIndA`

,`bsrRowPtrC`

,`descrA`

,`descrC`

,`buffer`

pointer is invalid.



## hipsparseXgebsr2gebsr()[#](#hipsparsexgebsr2gebsr)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSgebsr2gebsr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const float *bsrValA, const int *bsrRowPtrA, const int *bsrColIndA, int rowBlockDimA, int colBlockDimA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, float *bsrValC, int *bsrRowPtrC, int *bsrColIndC, int rowBlockDimC, int colBlockDimC, void *buffer)[#](#_CPPv421hipsparseSgebsr2gebsr17hipsparseHandle_t20hipsparseDirection_tiiiK19hipsparseMatDescr_tPKfPKiPKiiiK19hipsparseMatDescr_tPfPiPiiiPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDgebsr2gebsr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const double *bsrValA, const int *bsrRowPtrA, const int *bsrColIndA, int rowBlockDimA, int colBlockDimA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, double *bsrValC, int *bsrRowPtrC, int *bsrColIndC, int rowBlockDimC, int colBlockDimC, void *buffer)[#](#_CPPv421hipsparseDgebsr2gebsr17hipsparseHandle_t20hipsparseDirection_tiiiK19hipsparseMatDescr_tPKdPKiPKiiiK19hipsparseMatDescr_tPdPiPiiiPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCgebsr2gebsr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipComplex *bsrValA, const int *bsrRowPtrA, const int *bsrColIndA, int rowBlockDimA, int colBlockDimA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, hipComplex *bsrValC, int *bsrRowPtrC, int *bsrColIndC, int rowBlockDimC, int colBlockDimC, void *buffer)[#](#_CPPv421hipsparseCgebsr2gebsr17hipsparseHandle_t20hipsparseDirection_tiiiK19hipsparseMatDescr_tPK10hipComplexPKiPKiiiK19hipsparseMatDescr_tP10hipComplexPiPiiiPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZgebsr2gebsr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipDoubleComplex *bsrValA, const int *bsrRowPtrA, const int *bsrColIndA, int rowBlockDimA, int colBlockDimA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, hipDoubleComplex *bsrValC, int *bsrRowPtrC, int *bsrColIndC, int rowBlockDimC, int colBlockDimC, void *buffer)[#](#_CPPv421hipsparseZgebsr2gebsr17hipsparseHandle_t20hipsparseDirection_tiiiK19hipsparseMatDescr_tPK16hipDoubleComplexPKiPKiiiK19hipsparseMatDescr_tP16hipDoubleComplexPiPiiiPv) This function converts the GEBSR sparse matrix \(A\) to another GEBSR sparse matrix \(C\).

The conversion uses three steps. First, the user calls

[hipsparseXgebsr2gebsr_bufferSize()](#hipsparse__gebsr2gebsr_8h_1a0315a9ada5ccb960371a2430cb2e652e)to determine the size of the required temporary storage buffer. The user then allocates this buffer. Secondly, the user then allocates`mbC+1`

integers for the row pointer array for \(C\) where:\[\begin{split} \begin{align} \text{mbC} &= \text{(m - 1) / rowBlockDimC + 1} \\ \text{nbC} &= \text{(n - 1) / colBlockDimC + 1} \end{align} \end{split}\]The user then calls[hipsparseXgebsr2gebsrNnz()](#hipsparse__gebsr2gebsr_8h_1a60f114467872e19c249e19dbd83da63e)to fill in the row pointer array for \(C\) (`bsrRowPtrC`

) and determine the number of non-zero blocks that will exist in \(C\). Finally, the user allocates space for the column indices array of \(C\) to have`nnzbC`

elements and space for the values array of \(C\) to have`nnzbC*rowBlockDimC*colBlockDimC`

and then calls`hipsparseXgebsr2gebsr`

to complete the conversion.It may be the case that

`rowBlockDimC`

does not divide evenly into`m`

and/or`colBlockDim`

does not divide evenly into`n`

. In these cases, the GEBSR matrix is expanded in size in order to fit full GEBSR blocks. For example, if the original GEBSR matrix A (using`rowBlockDimA=2`

,`colBlockDimA=3`

) looks like:\[\begin{split} \left[ \begin{array}{c | c} \begin{array}{c c c} 1 & 0 & 0 \\ 3 & 4 & 0 \end{array} & \begin{array}{c c c} 2 & 0 & 0 \\ 4 & 5 & 6 \end{array} \\ \hline \begin{array}{c c c} 1 & 2 & 3 \\ 1 & 2 & 0 \end{array} & \begin{array}{c c c} 4 & 0 & 0 \\ 3 & 0 & 1 \end{array} \\ \end{array} \right] \end{split}\]then if we specify

`rowBlockDimC=3`

and`colBlockDimC=2`

, our output GEBSR matrix C would be:\[\begin{split} \left[ \begin{array}{c | c | c} \begin{array}{c c} 1 & 0 \\ 3 & 4 \\ 1 & 2 \end{array} & \begin{array}{c c} 0 & 2 \\ 0 & 4 \\ 3 & 4 \end{array} & \begin{array}{c c} 0 & 0 \\ 5 & 6 \\ 0 & 0 \end{array} \\ \hline \begin{array}{c c} 1 & 2 \\ 0 & 0 \\ 0 & 0 \end{array} & \begin{array}{c c} 0 & 3 \\ 0 & 0 \\ 0 & 0 \end{array} & \begin{array}{c c} 0 & 1 \\ 0 & 0 \\ 0 & 0 \end{array} \\ \end{array} \right] \end{split}\]**Example**int main(int argc, char* argv[]) { // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); hipsparseMatDescr_t descrA; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&descrA)); hipsparseMatDescr_t descrC; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&descrC)); // Sparse matrix in BSR format // 1 2 | 0 3 | 0 0 // 0 4 | 5 0 | 0 1 // A = 6 0 | 0 7 | 8 0 // --------------- // 0 0 | 3 0 | 2 2 // 1 0 | 0 0 | 4 3 // 7 2 | 0 0 | 1 4 int hbsrRowPtrA[3] = {0, 3, 6}; int hbsrColIndA[6] = {0, 1, 2, 0, 1, 2}; float hbsrValA[36] = {1.0f, 2.0f, 0.0f, 4.0f, 6.0f, 0.0f, 0.0f, 3.0f, 5.0f, 0.0f, 0.0f, 7.0f, 0.0f, 0.0f, 0.0f, 1.0f, 8.0f, 0.0f, 0.0f, 0.0f, 1.0f, 0.0f, 7.0f, 2.0f, 3.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 2.0f, 2.0f, 4.0f, 3.0f, 1.0f, 4.0f}; int m = 6; int n = 6; int rowBlockDimA = 3; int colBlockDimA = 2; int rowBlockDimC = 2; int colBlockDimC = 2; hipsparseDirection_t dirA = HIPSPARSE_DIRECTION_ROW; int mbA = (m + rowBlockDimA - 1) / rowBlockDimA; int nbA = (n + colBlockDimA - 1) / colBlockDimA; int nnzbA = 6; int mbC = (m + rowBlockDimC - 1) / rowBlockDimC; int nbC = (n + colBlockDimC - 1) / colBlockDimC; int* dbsrRowPtrA = nullptr; int* dbsrColIndA = nullptr; float* dbsrValA = nullptr; HIP_CHECK(hipMalloc((void**)&dbsrRowPtrA, sizeof(int) * (mbA + 1))); HIP_CHECK(hipMalloc((void**)&dbsrColIndA, sizeof(int) * nnzbA)); HIP_CHECK(hipMalloc((void**)&dbsrValA, sizeof(float) * rowBlockDimA * colBlockDimA * nnzbA)); HIP_CHECK(hipMemcpy(dbsrRowPtrA, hbsrRowPtrA, sizeof(int) * (mbA + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dbsrColIndA, hbsrColIndA, sizeof(int) * nnzbA, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dbsrValA, hbsrValA, sizeof(float) * rowBlockDimA * colBlockDimA * nnzbA, hipMemcpyHostToDevice)); int* dbsrRowPtrC = nullptr; HIP_CHECK(hipMalloc((void**)&dbsrRowPtrC, sizeof(int) * (mbC + 1))); int bufferSize; HIPSPARSE_CHECK(hipsparseSgebsr2gebsr_bufferSize(handle, dirA, mbA, nbA, nnzbA, descrA, dbsrValA, dbsrRowPtrA, dbsrColIndA, rowBlockDimA, colBlockDimA, rowBlockDimC, colBlockDimC, &bufferSize)); void* dbuffer = nullptr; HIP_CHECK(hipMalloc((void**)&dbuffer, bufferSize)); int nnzbC; HIPSPARSE_CHECK(hipsparseXgebsr2gebsrNnz(handle, dirA, mbA, nbA, nnzbA, descrA, dbsrRowPtrA, dbsrColIndA, rowBlockDimA, colBlockDimA, descrC, dbsrRowPtrC, rowBlockDimC, colBlockDimC, &nnzbC, dbuffer)); HIP_CHECK(hipDeviceSynchronize()); int* dbsrColIndC = nullptr; float* dbsrValC = nullptr; HIP_CHECK(hipMalloc((void**)&dbsrColIndC, sizeof(int) * nnzbC)); HIP_CHECK(hipMalloc((void**)&dbsrValC, sizeof(float) * rowBlockDimC * colBlockDimC * nnzbC)); HIPSPARSE_CHECK(hipsparseSgebsr2gebsr(handle, dirA, mbA, nbA, nnzbA, descrA, dbsrValA, dbsrRowPtrA, dbsrColIndA, rowBlockDimA, colBlockDimA, descrC, dbsrValC, dbsrRowPtrC, dbsrColIndC, rowBlockDimC, colBlockDimC, dbuffer)); HIP_CHECK(hipFree(dbsrRowPtrA)); HIP_CHECK(hipFree(dbsrColIndA)); HIP_CHECK(hipFree(dbsrValA)); HIP_CHECK(hipFree(dbsrRowPtrC)); HIP_CHECK(hipFree(dbsrColIndC)); HIP_CHECK(hipFree(dbsrValC)); HIP_CHECK(hipFree(dbuffer)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(descrA)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(descrC)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); return 0; }


- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**dirA**–**[in]**the storage format of the blocks,[HIPSPARSE_DIRECTION_ROW](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59ae8589abecf2fbfb4b6307fd9dacd9e55)or[HIPSPARSE_DIRECTION_COLUMN](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59a32e23f292b2377f6e60bdc90274c796c)**mb**–**[in]**number of block rows of the general BSR sparse matrix \(A\).**nb**–**[in]**number of block columns of the general BSR sparse matrix \(A\).**nnzb**–**[in]**number of blocks in the general BSR sparse matrix \(A\).**descrA**–**[in]**the descriptor of the general BSR sparse matrix \(A\), the supported matrix type is[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)and also any valid value of the[hipsparseIndexBase_t](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4).**bsrValA**–**[in]**array of`nnzb*rowBlockDimA*colBlockDimA`

containing the values of the sparse general BSR matrix \(A\).**bsrRowPtrA**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse general BSR matrix \(A\).**bsrColIndA**–**[in]**array of`nnzb`

elements containing the block column indices of the sparse general BSR matrix \(A\).**rowBlockDimA**–**[in]**row size of the blocks in the sparse general BSR matrix \(A\).**colBlockDimA**–**[in]**column size of the blocks in the sparse general BSR matrix \(A\).**descrC**–**[in]**the descriptor of the general BSR sparse matrix \(C\), the supported matrix type is[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)and also any valid value of the[hipsparseIndexBase_t](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4).**bsrValC**–**[in]**array of`nnzbC*rowBlockDimC*colBlockDimC`

containing the values of the sparse general BSR matrix \(C\).**bsrRowPtrC**–**[in]**array of`mbC+1`

elements that point to the start of every block row of the sparse general BSR matrix \(C\).**bsrColIndC**–**[in]**array of`nnzbC`

elements containing the block column indices of the sparse general BSR matrix \(C\).**rowBlockDimC**–**[in]**row size of the blocks in the sparse general BSR matrix \(C\).**colBlockDimC**–**[in]**column size of the blocks in the sparse general BSR matrix \(C\).**buffer**–**[out]**buffer allocated by the user whose size is determined by calling[hipsparseXgebsr2gebsr_bufferSize()](#hipsparse__gebsr2gebsr_8h_1a0315a9ada5ccb960371a2430cb2e652e).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`mb`

,`nb`

,`nnzb`

,`rowBlockDimA`

,`colBlockDimA`

,`rowBlockDimC`

,`colBlockDimC`

,`bsrRowPtrA`

,`bsrColIndA`

,`bsrValA`

,`bsrRowPtrC`

,`bsrColIndC`

,`bsrValC`

,`descrA`

,`descrC`

or`buffer`

pointer is invalid.



## hipsparseXcsru2csr_bufferSizeExt()[#](#hipsparsexcsru2csr-buffersizeext)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseScsru2csr_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnz, float *csrVal, const int *csrRowPtr, int *csrColInd,[csru2csrInfo_t](types.html#_CPPv414csru2csrInfo_t)info, size_t *pBufferSizeInBytes)[#](#_CPPv432hipsparseScsru2csr_bufferSizeExt17hipsparseHandle_tiiiPfPKiPi14csru2csrInfo_tP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDcsru2csr_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnz, double *csrVal, const int *csrRowPtr, int *csrColInd,[csru2csrInfo_t](types.html#_CPPv414csru2csrInfo_t)info, size_t *pBufferSizeInBytes)[#](#_CPPv432hipsparseDcsru2csr_bufferSizeExt17hipsparseHandle_tiiiPdPKiPi14csru2csrInfo_tP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCcsru2csr_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnz, hipComplex *csrVal, const int *csrRowPtr, int *csrColInd,[csru2csrInfo_t](types.html#_CPPv414csru2csrInfo_t)info, size_t *pBufferSizeInBytes)[#](#_CPPv432hipsparseCcsru2csr_bufferSizeExt17hipsparseHandle_tiiiP10hipComplexPKiPi14csru2csrInfo_tP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZcsru2csr_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnz, hipDoubleComplex *csrVal, const int *csrRowPtr, int *csrColInd,[csru2csrInfo_t](types.html#_CPPv414csru2csrInfo_t)info, size_t *pBufferSizeInBytes)[#](#_CPPv432hipsparseZcsru2csr_bufferSizeExt17hipsparseHandle_tiiiP16hipDoubleComplexPKiPi14csru2csrInfo_tP6size_t) This function calculates the amount of temporary storage in bytes required for hipsparseXcsru2csr() and hipsparseXcsr2csru().


## hipsparseXcsru2csr()[#](#hipsparsexcsru2csr)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseScsru2csr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, float *csrVal, const int *csrRowPtr, int *csrColInd,[csru2csrInfo_t](types.html#_CPPv414csru2csrInfo_t)info, void *pBuffer)[#](#_CPPv418hipsparseScsru2csr17hipsparseHandle_tiiiK19hipsparseMatDescr_tPfPKiPi14csru2csrInfo_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDcsru2csr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, double *csrVal, const int *csrRowPtr, int *csrColInd,[csru2csrInfo_t](types.html#_CPPv414csru2csrInfo_t)info, void *pBuffer)[#](#_CPPv418hipsparseDcsru2csr17hipsparseHandle_tiiiK19hipsparseMatDescr_tPdPKiPi14csru2csrInfo_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCcsru2csr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, hipComplex *csrVal, const int *csrRowPtr, int *csrColInd,[csru2csrInfo_t](types.html#_CPPv414csru2csrInfo_t)info, void *pBuffer)[#](#_CPPv418hipsparseCcsru2csr17hipsparseHandle_tiiiK19hipsparseMatDescr_tP10hipComplexPKiPi14csru2csrInfo_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZcsru2csr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, hipDoubleComplex *csrVal, const int *csrRowPtr, int *csrColInd,[csru2csrInfo_t](types.html#_CPPv414csru2csrInfo_t)info, void *pBuffer)[#](#_CPPv418hipsparseZcsru2csr17hipsparseHandle_tiiiK19hipsparseMatDescr_tP16hipDoubleComplexPKiPi14csru2csrInfo_tPv) This function converts unsorted CSR format to sorted CSR format. The required temporary storage has to be allocated by the user.


## hipsparseXcsr2csru()[#](#hipsparsexcsr2csru)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseScsr2csru([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, float *csrVal, const int *csrRowPtr, int *csrColInd,[csru2csrInfo_t](types.html#_CPPv414csru2csrInfo_t)info, void *pBuffer)[#](#_CPPv418hipsparseScsr2csru17hipsparseHandle_tiiiK19hipsparseMatDescr_tPfPKiPi14csru2csrInfo_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDcsr2csru([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, double *csrVal, const int *csrRowPtr, int *csrColInd,[csru2csrInfo_t](types.html#_CPPv414csru2csrInfo_t)info, void *pBuffer)[#](#_CPPv418hipsparseDcsr2csru17hipsparseHandle_tiiiK19hipsparseMatDescr_tPdPKiPi14csru2csrInfo_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCcsr2csru([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, hipComplex *csrVal, const int *csrRowPtr, int *csrColInd,[csru2csrInfo_t](types.html#_CPPv414csru2csrInfo_t)info, void *pBuffer)[#](#_CPPv418hipsparseCcsr2csru17hipsparseHandle_tiiiK19hipsparseMatDescr_tP10hipComplexPKiPi14csru2csrInfo_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZcsr2csru([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, hipDoubleComplex *csrVal, const int *csrRowPtr, int *csrColInd,[csru2csrInfo_t](types.html#_CPPv414csru2csrInfo_t)info, void *pBuffer)[#](#_CPPv418hipsparseZcsr2csru17hipsparseHandle_tiiiK19hipsparseMatDescr_tP16hipDoubleComplexPKiPi14csru2csrInfo_tPv) This function converts sorted CSR format to unsorted CSR format. The required temporary storage has to be allocated by the user.
