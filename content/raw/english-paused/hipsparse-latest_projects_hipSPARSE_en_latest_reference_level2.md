---
title: "Sparse level 2 functions &#8212; hipSPARSE 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipSPARSE/en/latest/reference/level2.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:09:42.125147+00:00
content_hash: "9d7c8e0eb938c090"
---

# Sparse level 2 functions[#](#sparse-level-2-functions)

This module contains all sparse level 2 routines.

The sparse level 2 routines describe operations between a matrix in sparse format and a vector in dense format.

## hipsparseXcsrmv()[#](#hipsparsexcsrmv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseScsrmv([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int m, int n, int nnz, const float *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const float *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA, const float *x, const float *beta, float *y)[#](#_CPPv415hipsparseScsrmv17hipsparseHandle_t20hipsparseOperation_tiiiPKfK19hipsparseMatDescr_tPKfPKiPKiPKfPKfPf)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDcsrmv([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int m, int n, int nnz, const double *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const double *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA, const double *x, const double *beta, double *y)[#](#_CPPv415hipsparseDcsrmv17hipsparseHandle_t20hipsparseOperation_tiiiPKdK19hipsparseMatDescr_tPKdPKiPKiPKdPKdPd)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCcsrmv([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int m, int n, int nnz, const hipComplex *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipComplex *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA, const hipComplex *x, const hipComplex *beta, hipComplex *y)[#](#_CPPv415hipsparseCcsrmv17hipsparseHandle_t20hipsparseOperation_tiiiPK10hipComplexK19hipsparseMatDescr_tPK10hipComplexPKiPKiPK10hipComplexPK10hipComplexP10hipComplex)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZcsrmv([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int m, int n, int nnz, const hipDoubleComplex *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipDoubleComplex *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA, const hipDoubleComplex *x, const hipDoubleComplex *beta, hipDoubleComplex *y)[#](#_CPPv415hipsparseZcsrmv17hipsparseHandle_t20hipsparseOperation_tiiiPK16hipDoubleComplexK19hipsparseMatDescr_tPK16hipDoubleComplexPKiPKiPK16hipDoubleComplexPK16hipDoubleComplexP16hipDoubleComplex) Sparse matrix vector multiplication using CSR storage format.

`hipsparseXcsrmv`

multiplies the scalar \(\alpha\) with a sparse \(m \times n\) matrix, defined in CSR storage format, and the dense vector \(x\) and adds the result to the dense vector \(y\) that is multiplied by the scalar \(\beta\), such that\[ y := \alpha \cdot op(A) \cdot x + \beta \cdot y, \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if transA == HIPSPARSE_OPERATION_NON_TRANSPOSE} \\ A^T, & \text{if transA == HIPSPARSE_OPERATION_TRANSPOSE} \\ A^H, & \text{if transA == HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE} \end{array} \right. \end{split}\]for(i = 0; i < m; ++i) { y[i] = beta * y[i]; for(j = csrRowPtr[i]; j < csrRowPtr[i + 1]; ++j) { y[i] = y[i] + alpha * csrVal[j] * x[csrColInd[j]]; } }

**Example**int main(int argc, char* argv[]) { // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // alpha * ( 1.0 0.0 2.0 ) * ( 1.0 ) + beta * ( 4.0 ) = ( 31.1 ) // ( 3.0 0.0 4.0 ) * ( 2.0 ) ( 5.0 ) = ( 62.0 ) // ( 5.0 6.0 0.0 ) * ( 3.0 ) ( 6.0 ) = ( 70.7 ) // ( 7.0 0.0 8.0 ) * ( 7.0 ) = ( 123.8 ) const int m = 4; const int n = 3; const int nnz = 8; // CSR row pointers int hcsrRowPtr[m + 1] = {0, 2, 4, 6, 8}; // CSR column indices int hcsrColInd[nnz] = {0, 2, 0, 2, 0, 1, 0, 2}; // CSR values double hcsrVal[nnz] = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0}; // Transposition of the matrix hipsparseOperation_t trans = HIPSPARSE_OPERATION_NON_TRANSPOSE; // Scalar alpha and beta double alpha = 3.7; double beta = 1.3; // x and y double hx[n] = {1.0, 2.0, 3.0}; double hy[m] = {4.0, 5.0, 6.0, 7.0}; // Matrix descriptor hipsparseMatDescr_t descr; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&descr)); // Offload data to device int* dcsrRowPtr; int* dcsrColInd; double* dcsrVal; double* dx; double* dy; HIP_CHECK(hipMalloc((void**)&dcsrRowPtr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&dcsrColInd, sizeof(int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcsrVal, sizeof(double) * nnz)); HIP_CHECK(hipMalloc((void**)&dx, sizeof(double) * n)); HIP_CHECK(hipMalloc((void**)&dy, sizeof(double) * m)); HIP_CHECK(hipMemcpy(dcsrRowPtr, hcsrRowPtr, sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrColInd, hcsrColInd, sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrVal, hcsrVal, sizeof(double) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dx, hx, sizeof(double) * n, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dy, hy, sizeof(double) * m, hipMemcpyHostToDevice)); // Call dcsrmv to perform y = alpha * A x + beta * y HIPSPARSE_CHECK(hipsparseDcsrmv( handle, trans, m, n, nnz, &alpha, descr, dcsrVal, dcsrRowPtr, dcsrColInd, dx, &beta, dy)); // Copy result back to host HIP_CHECK(hipMemcpy(hy, dy, sizeof(double) * m, hipMemcpyDeviceToHost)); std::cout << "hy" << std::endl; for(int i = 0; i < m; i++) { std::cout << hy[i] << " "; } std::cout << "" << std::endl; // Clear hipSPARSE HIPSPARSE_CHECK(hipsparseDestroyMatDescr(descr)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); // Clear device memory HIP_CHECK(hipFree(dcsrRowPtr)); HIP_CHECK(hipFree(dcsrColInd)); HIP_CHECK(hipFree(dcsrVal)); HIP_CHECK(hipFree(dx)); HIP_CHECK(hipFree(dy)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**transA**–**[in]**matrix operation type.**m**–**[in]**number of rows of the sparse CSR matrix.**n**–**[in]**number of columns of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**alpha**–**[in]**scalar \(\alpha\).**descrA**–**[in]**descriptor of the sparse CSR matrix. Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**csrSortedValA**–**[in]**array of`nnz`

elements of the sparse CSR matrix.**csrSortedRowPtrA**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csrSortedColIndA**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**x**–**[in]**array of`n`

elements ( \(op(A) == A\)) or`m`

elements ( \(op(A) == A^T\) or \(op(A) == A^H\)).**beta**–**[in]**scalar \(\beta\).**y**–**[inout]**array of`m`

elements ( \(op(A) == A\)) or`n`

elements ( \(op(A) == A^T\) or \(op(A) == A^H\)).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

or`nnz`

,`descr`

,`alpha`

,`csrSortedValA`

,`csrSortedRowPtrA`

,`csrSortedColIndA`

,`x`

,`beta`

or`y`

is invalid.**HIPSPARSE_STATUS_ARCH_MISMATCH**– the device is not supported.**HIPSPARSE_STATUS_NOT_SUPPORTED**–[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXcsrsv2_zeroPivot()[#](#hipsparsexcsrsv2-zeropivot)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseXcsrsv2_zeroPivot([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[csrsv2Info_t](types.html#_CPPv412csrsv2Info_t)info, int *position)[#](#_CPPv426hipsparseXcsrsv2_zeroPivot17hipsparseHandle_t12csrsv2Info_tPi) `hipsparseXcsrsv2_zeroPivot`

returns[HIPSPARSE_STATUS_ZERO_PIVOT](types.html#hipsparse-types_8h_1aa069bec7a4f24d00dab1dc4612d4de79a88ff0f0537dfe037fcf9f99ff0cf79da), if either a structural or numerical zero has been found during[hipsparseScsrsv2_solve()](#hipsparse__csrsv_8h_1ae696c633b40b43ea9c3b9bc1387db731),[hipsparseDcsrsv2_solve()](#hipsparse__csrsv_8h_1a0ce534eecebb7d79ea9bb33e36db1628),[hipsparseCcsrsv2_solve()](#hipsparse__csrsv_8h_1a65d504f2ae713ff1bb5a2ae45d55b95d)or[hipsparseZcsrsv2_solve()](#hipsparse__csrsv_8h_1a270f439dc9580f53f55db6a1bac6adb6)computation. The first zero pivot \(j\) at \(A_{j,j}\) is stored in`position`

, using same index base as the CSR matrix.`position`

can be in host or device memory. If no zero pivot has been found,`position`

is set to -1 and[HIPSPARSE_STATUS_SUCCESS](types.html#hipsparse-types_8h_1aa069bec7a4f24d00dab1dc4612d4de79a146a8a2fd27ee49132f8dcea617fc481)is returned instead.Note

`hipsparseXcsrsv2_zeroPivot`

is a blocking function. It might influence performance negatively.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**info**–**[in]**structure that holds the information collected during the analysis step.**position**–**[inout]**pointer to zero pivot \(j\), can be in host or device memory.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

`info`

or`position`

is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.**HIPSPARSE_STATUS_ZERO_PIVOT**– zero pivot has been found.



## hipsparseXcsrsv2_bufferSize()[#](#hipsparsexcsrsv2-buffersize)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseScsrsv2_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, float *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csrsv2Info_t](types.html#_CPPv412csrsv2Info_t)info, int *pBufferSizeInBytes)[#](#_CPPv427hipsparseScsrsv2_bufferSize17hipsparseHandle_t20hipsparseOperation_tiiK19hipsparseMatDescr_tPfPKiPKi12csrsv2Info_tPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDcsrsv2_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, double *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csrsv2Info_t](types.html#_CPPv412csrsv2Info_t)info, int *pBufferSizeInBytes)[#](#_CPPv427hipsparseDcsrsv2_bufferSize17hipsparseHandle_t20hipsparseOperation_tiiK19hipsparseMatDescr_tPdPKiPKi12csrsv2Info_tPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCcsrsv2_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, hipComplex *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csrsv2Info_t](types.html#_CPPv412csrsv2Info_t)info, int *pBufferSizeInBytes)[#](#_CPPv427hipsparseCcsrsv2_bufferSize17hipsparseHandle_t20hipsparseOperation_tiiK19hipsparseMatDescr_tP10hipComplexPKiPKi12csrsv2Info_tPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZcsrsv2_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, hipDoubleComplex *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csrsv2Info_t](types.html#_CPPv412csrsv2Info_t)info, int *pBufferSizeInBytes)[#](#_CPPv427hipsparseZcsrsv2_bufferSize17hipsparseHandle_t20hipsparseOperation_tiiK19hipsparseMatDescr_tP16hipDoubleComplexPKiPKi12csrsv2Info_tPi) `hipsparseXcsrsv2_bufferSize`

returns the size of the temporary storage buffer in bytes that is required by[hipsparseScsrsv2_analysis()](#hipsparse__csrsv_8h_1a201995e83a6140db524e3b15cbed4dcb)and[hipsparseXcsrsv2_solve()](#hipsparse__csrsv_8h_1ae696c633b40b43ea9c3b9bc1387db731). The temporary storage buffer must be allocated by the user.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**transA**–**[in]**matrix operation type.**m**–**[in]**number of rows of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**descrA**–**[in]**descriptor of the sparse CSR matrix.**csrSortedValA**–**[in]**array of`nnz`

elements of the sparse CSR matrix.**csrSortedRowPtrA**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csrSortedColIndA**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**info**–**[out]**structure that holds the information collected during the analysis step.**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer required by[hipsparseXcsrsv2_analysis()](#hipsparse__csrsv_8h_1a201995e83a6140db524e3b15cbed4dcb)and[hipsparseXcsrsv2_solve()](#hipsparse__csrsv_8h_1ae696c633b40b43ea9c3b9bc1387db731).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`nnz`

,`descrA`

,`csrSortedValA`

,`csrSortedRowPtrA`

,`csrSortedColIndA`

,`info`

or`pBufferSizeInBytes`

is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`transA`

==[HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141ac55e75ba3027186f1dc6164fdcb06f0e)or[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXcsrsv2_bufferSizeExt()[#](#hipsparsexcsrsv2-buffersizeext)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseScsrsv2_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, float *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csrsv2Info_t](types.html#_CPPv412csrsv2Info_t)info, size_t *pBufferSizeInBytes)[#](#_CPPv430hipsparseScsrsv2_bufferSizeExt17hipsparseHandle_t20hipsparseOperation_tiiK19hipsparseMatDescr_tPfPKiPKi12csrsv2Info_tP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDcsrsv2_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, double *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csrsv2Info_t](types.html#_CPPv412csrsv2Info_t)info, size_t *pBufferSizeInBytes)[#](#_CPPv430hipsparseDcsrsv2_bufferSizeExt17hipsparseHandle_t20hipsparseOperation_tiiK19hipsparseMatDescr_tPdPKiPKi12csrsv2Info_tP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCcsrsv2_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, hipComplex *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csrsv2Info_t](types.html#_CPPv412csrsv2Info_t)info, size_t *pBufferSizeInBytes)[#](#_CPPv430hipsparseCcsrsv2_bufferSizeExt17hipsparseHandle_t20hipsparseOperation_tiiK19hipsparseMatDescr_tP10hipComplexPKiPKi12csrsv2Info_tP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZcsrsv2_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, hipDoubleComplex *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csrsv2Info_t](types.html#_CPPv412csrsv2Info_t)info, size_t *pBufferSizeInBytes)[#](#_CPPv430hipsparseZcsrsv2_bufferSizeExt17hipsparseHandle_t20hipsparseOperation_tiiK19hipsparseMatDescr_tP16hipDoubleComplexPKiPKi12csrsv2Info_tP6size_t) `hipsparseXcsrsv2_bufferSizeExt`

returns the size of the temporary storage buffer in bytes that is required by[hipsparseXcsrsv2_analysis()](#hipsparse__csrsv_8h_1a201995e83a6140db524e3b15cbed4dcb)and[hipsparseScsrsv2_solve()](#hipsparse__csrsv_8h_1ae696c633b40b43ea9c3b9bc1387db731). The temporary storage buffer must be allocated by the user.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**transA**–**[in]**matrix operation type.**m**–**[in]**number of rows of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**descrA**–**[in]**descriptor of the sparse CSR matrix.**csrSortedValA**–**[in]**array of`nnz`

elements of the sparse CSR matrix.**csrSortedRowPtrA**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csrSortedColIndA**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**info**–**[out]**structure that holds the information collected during the analysis step.**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer required by[hipsparseXcsrsv2_analysis()](#hipsparse__csrsv_8h_1a201995e83a6140db524e3b15cbed4dcb)and[hipsparseXcsrsv2_solve()](#hipsparse__csrsv_8h_1ae696c633b40b43ea9c3b9bc1387db731).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`nnz`

,`descrA`

,`csrSortedValA`

,`csrSortedRowPtrA`

,`csrSortedColIndA`

,`info`

or`pBufferSizeInBytes`

is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`transA`

==[HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141ac55e75ba3027186f1dc6164fdcb06f0e)or[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXcsrsv2_analysis()[#](#hipsparsexcsrsv2-analysis)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseScsrsv2_analysis([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const float *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csrsv2Info_t](types.html#_CPPv412csrsv2Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv425hipsparseScsrsv2_analysis17hipsparseHandle_t20hipsparseOperation_tiiK19hipsparseMatDescr_tPKfPKiPKi12csrsv2Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDcsrsv2_analysis([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const double *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csrsv2Info_t](types.html#_CPPv412csrsv2Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv425hipsparseDcsrsv2_analysis17hipsparseHandle_t20hipsparseOperation_tiiK19hipsparseMatDescr_tPKdPKiPKi12csrsv2Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCcsrsv2_analysis([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipComplex *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csrsv2Info_t](types.html#_CPPv412csrsv2Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv425hipsparseCcsrsv2_analysis17hipsparseHandle_t20hipsparseOperation_tiiK19hipsparseMatDescr_tPK10hipComplexPKiPKi12csrsv2Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZcsrsv2_analysis([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipDoubleComplex *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csrsv2Info_t](types.html#_CPPv412csrsv2Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv425hipsparseZcsrsv2_analysis17hipsparseHandle_t20hipsparseOperation_tiiK19hipsparseMatDescr_tPK16hipDoubleComplexPKiPKi12csrsv2Info_t22hipsparseSolvePolicy_tPv) `hipsparseXcsrsv2_analysis`

performs the analysis step for[hipsparseXcsrsv2_solve()](#hipsparse__csrsv_8h_1ae696c633b40b43ea9c3b9bc1387db731). It is expected that this function will be executed only once for a given matrix and particular operation type.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**transA**–**[in]**matrix operation type.**m**–**[in]**number of rows of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**descrA**–**[in]**descriptor of the sparse CSR matrix.**csrSortedValA**–**[in]**array of`nnz`

elements of the sparse CSR matrix.**csrSortedRowPtrA**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csrSortedColIndA**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**info**–**[out]**structure that holds the information collected during the analysis step.**policy**–**[in]**[HIPSPARSE_SOLVE_POLICY_NO_LEVEL](types.html#hipsparse-types_8h_1a0d98e490c94d4facc231db60baf1c3b3ac5830aa96848e832b3b375ad08abdb09)or[HIPSPARSE_SOLVE_POLICY_USE_LEVEL](types.html#hipsparse-types_8h_1a0d98e490c94d4facc231db60baf1c3b3a934309d6656638e375f0759b89fd81b5).**pBuffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`nnz`

,`descr`

,`csrSortedRowPtrA`

,`csrSortedColIndA`

,`info`

or`pBuffer`

is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`transA`

==[HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141ac55e75ba3027186f1dc6164fdcb06f0e)or[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXcsrsv2_solve()[#](#hipsparsexcsrsv2-solve)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseScsrsv2_solve([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int m, int nnz, const float *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const float *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csrsv2Info_t](types.html#_CPPv412csrsv2Info_t)info, const float *f, float *x,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv422hipsparseScsrsv2_solve17hipsparseHandle_t20hipsparseOperation_tiiPKfK19hipsparseMatDescr_tPKfPKiPKi12csrsv2Info_tPKfPf22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDcsrsv2_solve([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int m, int nnz, const double *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const double *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csrsv2Info_t](types.html#_CPPv412csrsv2Info_t)info, const double *f, double *x,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv422hipsparseDcsrsv2_solve17hipsparseHandle_t20hipsparseOperation_tiiPKdK19hipsparseMatDescr_tPKdPKiPKi12csrsv2Info_tPKdPd22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCcsrsv2_solve([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int m, int nnz, const hipComplex *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipComplex *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csrsv2Info_t](types.html#_CPPv412csrsv2Info_t)info, const hipComplex *f, hipComplex *x,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv422hipsparseCcsrsv2_solve17hipsparseHandle_t20hipsparseOperation_tiiPK10hipComplexK19hipsparseMatDescr_tPK10hipComplexPKiPKi12csrsv2Info_tPK10hipComplexP10hipComplex22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZcsrsv2_solve([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int m, int nnz, const hipDoubleComplex *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipDoubleComplex *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csrsv2Info_t](types.html#_CPPv412csrsv2Info_t)info, const hipDoubleComplex *f, hipDoubleComplex *x,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv422hipsparseZcsrsv2_solve17hipsparseHandle_t20hipsparseOperation_tiiPK16hipDoubleComplexK19hipsparseMatDescr_tPK16hipDoubleComplexPKiPKi12csrsv2Info_tPK16hipDoubleComplexP16hipDoubleComplex22hipsparseSolvePolicy_tPv) Sparse triangular solve using CSR storage format.

`hipsparseXcsrsv2_solve`

solves a sparse triangular linear system of a sparse \(m \times m\) matrix, defined in CSR storage format, a dense solution vector \(y\) and the right-hand side \(x\) that is multiplied by \(\alpha\), such that\[ op(A) \cdot y = \alpha \cdot x, \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if trans == HIPSPARSE_OPERATION_NON_TRANSPOSE} \\ A^T, & \text{if trans == HIPSPARSE_OPERATION_TRANSPOSE} \\ A^H, & \text{if trans == HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE} \end{array} \right. \end{split}\]Performing the above operation requires three steps. First, the user calls

[hipsparseXcsrsv2_bufferSize()](#hipsparse__csrsv_8h_1ac2b333394fd5c3ed2c1cf717bf2d1661)(or[hipsparseXcsrsv2_bufferSizeExt()](#hipsparse__csrsv_8h_1a59d71b90836b38586e737223805dbedc)) which will determine the size of the required temporary storage buffer. The user then allocates this buffer and calls[hipsparseXcsrsv2_analysis()](#hipsparse__csrsv_8h_1a201995e83a6140db524e3b15cbed4dcb)which will perform analysis on the sparse matrix \(op(A)\). Finally, the user completes the computation by calling`hipsparseXcsrsv2_solve`

. The buffer size, buffer allocation, and analysis only need to be called once for a given sparse matrix \(op(A)\) while the computation stage can be repeatedly used with different \(x\) and \(y\) vectors. Once all calls to`hipsparseXcsrsv2_solve`

are complete, the temporary buffer can be deallocated.Solving a triangular system involves division by the diagonal elements. This means that if the sparse matrix is missing the diagonal entry (referred to as a structural zero) or the diagonal entry is zero (referred to as a numerical zero) then a division by zero would occur.

`hipsparseXcsrsv2_solve`

tracks the location of the first zero pivot (either numerical or structural zero). The zero pivot status can be checked calling[hipsparseXcsrsv2_zeroPivot()](#hipsparse__csrsv_8h_1a12b4fe69770b7a69609a1f54ab3869b5). If[hipsparseXcsrsv2_zeroPivot()](#hipsparse__csrsv_8h_1a12b4fe69770b7a69609a1f54ab3869b5)returns[HIPSPARSE_STATUS_SUCCESS](types.html#hipsparse-types_8h_1aa069bec7a4f24d00dab1dc4612d4de79a146a8a2fd27ee49132f8dcea617fc481), then no zero pivot was found and therefore the matrix does not have a structural or numerical zero.The user can specify that the sparse matrix should be interpreted as having ones on the diagonal by setting the diagonal type on the descriptor

`descrA`

to[HIPSPARSE_DIAG_TYPE_UNIT](types.html#hipsparse-types_8h_1a79e036b6c0680cb37e2aa53d3542a054a532a9a4a4eaf63a967bfaac7f9936b39)using[hipsparseSetMatDiagType](auxiliary.html#hipsparse-auxiliary_8h_1aec6fa039793196011f15cfb0b21c2b59). If[hipsparseDiagType_t](types.html#hipsparse-types_8h_1a79e036b6c0680cb37e2aa53d3542a054)==[HIPSPARSE_DIAG_TYPE_UNIT](types.html#hipsparse-types_8h_1a79e036b6c0680cb37e2aa53d3542a054a532a9a4a4eaf63a967bfaac7f9936b39), no zero pivot will be reported, even if \(A_{j,j} = 0\) for some \(j\).The sparse CSR matrix passed to

`hipsparseXcsrsv2_solve`

does not actually have to be a triangular matrix. Instead the triangular upper or lower part of the sparse matrix is solved based on[hipsparseFillMode_t](types.html#hipsparse-types_8h_1ace47655e52ed1bb17309eda331c44332)set on the descriptor`descrA`

. If the fill mode is set to[HIPSPARSE_FILL_MODE_LOWER](types.html#hipsparse-types_8h_1ace47655e52ed1bb17309eda331c44332a470abb0661ab8951449efa6988ed49ef), then the lower triangular matrix is solved. If the fill mode is set to[HIPSPARSE_FILL_MODE_UPPER](types.html#hipsparse-types_8h_1ace47655e52ed1bb17309eda331c44332ac5c8ccc62dfff77c56c8480c24ed6b3b)then the upper triangular matrix is solved.**Example**int main(int argc, char* argv[]) { // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // alpha * ( 1.0 0.0 2.0 0.0 ) * ( x_0 ) = ( 32.0 ) // ( 3.0 2.0 4.0 1.0 ) * ( x_1 ) = ( 14.7 ) // ( 5.0 6.0 1.0 3.0 ) * ( x_2 ) = ( 33.6 ) // ( 7.0 0.0 8.0 0.6 ) * ( x_3 ) = ( 10.0 ) const int m = 4; const int nnz = 13; // CSR row pointers int hcsrRowPtr[m + 1] = {0, 2, 6, 10, 13}; // CSR column indices int hcsrColInd[nnz] = {0, 2, 0, 1, 2, 3, 0, 1, 2, 3, 0, 2, 3}; // CSR values double hcsrVal[nnz] = {1.0, 2.0, 3.0, 2.0, 4.0, 1.0, 5.0, 6.0, 1.0, 3.0, 7.0, 8.0, 0.6}; // Transposition of the matrix hipsparseOperation_t trans = HIPSPARSE_OPERATION_NON_TRANSPOSE; hipsparseSolvePolicy_t policy = HIPSPARSE_SOLVE_POLICY_USE_LEVEL; // Scalar alpha double alpha = 1.0; // f and x double hf[m] = {32.0, 14.7, 33.6, 10.0}; double hx[m]; // Matrix descriptor hipsparseMatDescr_t descr; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&descr)); // Set index base on descriptor HIPSPARSE_CHECK(hipsparseSetMatIndexBase(descr, HIPSPARSE_INDEX_BASE_ZERO)); // Set fill mode on descriptor HIPSPARSE_CHECK(hipsparseSetMatFillMode(descr, HIPSPARSE_FILL_MODE_LOWER)); // Set diag type on descriptor HIPSPARSE_CHECK(hipsparseSetMatDiagType(descr, HIPSPARSE_DIAG_TYPE_UNIT)); // Csrsv info csrsv2Info_t info; HIPSPARSE_CHECK(hipsparseCreateCsrsv2Info(&info)); // Offload data to device int* dcsrRowPtr; int* dcsrColInd; double* dcsrVal; double* df; double* dx; HIP_CHECK(hipMalloc((void**)&dcsrRowPtr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&dcsrColInd, sizeof(int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcsrVal, sizeof(double) * nnz)); HIP_CHECK(hipMalloc((void**)&df, sizeof(double) * m)); HIP_CHECK(hipMalloc((void**)&dx, sizeof(double) * m)); HIP_CHECK(hipMemcpy(dcsrRowPtr, hcsrRowPtr, sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrColInd, hcsrColInd, sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrVal, hcsrVal, sizeof(double) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(df, hf, sizeof(double) * m, hipMemcpyHostToDevice)); int bufferSize = 0; HIPSPARSE_CHECK(hipsparseDcsrsv2_bufferSize( handle, trans, m, nnz, descr, dcsrVal, dcsrRowPtr, dcsrColInd, info, &bufferSize)); void* dbuffer = nullptr; HIP_CHECK(hipMalloc((void**)&dbuffer, bufferSize)); HIPSPARSE_CHECK(hipsparseDcsrsv2_analysis( handle, trans, m, nnz, descr, dcsrVal, dcsrRowPtr, dcsrColInd, info, policy, dbuffer)); // Call dcsrsv to perform alpha * A * x = f HIPSPARSE_CHECK(hipsparseDcsrsv2_solve(handle, trans, m, nnz, &alpha, descr, dcsrVal, dcsrRowPtr, dcsrColInd, info, df, dx, policy, dbuffer)); // Copy result back to host HIP_CHECK(hipMemcpy(hx, dx, sizeof(double) * m, hipMemcpyDeviceToHost)); std::cout << "hx" << std::endl; for(int i = 0; i < m; i++) { std::cout << hx[i] << " "; } std::cout << "" << std::endl; // Clear hipSPARSE HIPSPARSE_CHECK(hipsparseDestroyMatDescr(descr)); HIPSPARSE_CHECK(hipsparseDestroyCsrsv2Info(info)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); // Clear device memory HIP_CHECK(hipFree(dcsrRowPtr)); HIP_CHECK(hipFree(dcsrColInd)); HIP_CHECK(hipFree(dcsrVal)); HIP_CHECK(hipFree(df)); HIP_CHECK(hipFree(dx)); HIP_CHECK(hipFree(dbuffer)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

Currently, only

`transA`

==[HIPSPARSE_OPERATION_NON_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141a270f0124eb0d0ac15c3e7afb18064547)and`transA`

==[HIPSPARSE_OPERATION_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141a20e9c4bdd71ea4b509b6c0b7a495c0bf)is supported.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**transA**–**[in]**matrix operation type.**m**–**[in]**number of rows of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**alpha**–**[in]**scalar \(\alpha\).**descrA**–**[in]**descriptor of the sparse CSR matrix.**csrSortedValA**–**[in]**array of`nnz`

elements of the sparse CSR matrix.**csrSortedRowPtrA**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csrSortedColIndA**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**info**–**[in]**structure that holds the information collected during the analysis step.**f**–**[in]**array of`m`

elements, holding the right-hand side.**x**–**[out]**array of`m`

elements, holding the solution.**policy**–**[in]**[HIPSPARSE_SOLVE_POLICY_NO_LEVEL](types.html#hipsparse-types_8h_1a0d98e490c94d4facc231db60baf1c3b3ac5830aa96848e832b3b375ad08abdb09)or[HIPSPARSE_SOLVE_POLICY_USE_LEVEL](types.html#hipsparse-types_8h_1a0d98e490c94d4facc231db60baf1c3b3a934309d6656638e375f0759b89fd81b5).**pBuffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`nnz`

,`descrA`

,`alpha`

,`csrSortedValA`

,`csrSortedRowPtrA`

,`csrSortedColIndA`

,`f`

or`x`

is invalid.**HIPSPARSE_STATUS_ARCH_MISMATCH**– the device is not supported.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`transA`

==[HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141ac55e75ba3027186f1dc6164fdcb06f0e)or[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXhybmv()[#](#hipsparsexhybmv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseShybmv([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, const float *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const[hipsparseHybMat_t](types.html#_CPPv417hipsparseHybMat_t)hybA, const float *x, const float *beta, float *y)[#](#_CPPv415hipsparseShybmv17hipsparseHandle_t20hipsparseOperation_tPKfK19hipsparseMatDescr_tK17hipsparseHybMat_tPKfPKfPf)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDhybmv([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, const double *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const[hipsparseHybMat_t](types.html#_CPPv417hipsparseHybMat_t)hybA, const double *x, const double *beta, double *y)[#](#_CPPv415hipsparseDhybmv17hipsparseHandle_t20hipsparseOperation_tPKdK19hipsparseMatDescr_tK17hipsparseHybMat_tPKdPKdPd)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseChybmv([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, const hipComplex *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const[hipsparseHybMat_t](types.html#_CPPv417hipsparseHybMat_t)hybA, const hipComplex *x, const hipComplex *beta, hipComplex *y)[#](#_CPPv415hipsparseChybmv17hipsparseHandle_t20hipsparseOperation_tPK10hipComplexK19hipsparseMatDescr_tK17hipsparseHybMat_tPK10hipComplexPK10hipComplexP10hipComplex)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZhybmv([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, const hipDoubleComplex *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const[hipsparseHybMat_t](types.html#_CPPv417hipsparseHybMat_t)hybA, const hipDoubleComplex *x, const hipDoubleComplex *beta, hipDoubleComplex *y)[#](#_CPPv415hipsparseZhybmv17hipsparseHandle_t20hipsparseOperation_tPK16hipDoubleComplexK19hipsparseMatDescr_tK17hipsparseHybMat_tPK16hipDoubleComplexPK16hipDoubleComplexP16hipDoubleComplex) Sparse matrix vector multiplication using HYB storage format.

`hipsparseXhybmv`

multiplies the scalar \(\alpha\) with a sparse \(m \times n\) matrix, defined in HYB storage format, and the dense vector \(x\) and adds the result to the dense vector \(y\) that is multiplied by the scalar \(\beta\), such that\[ y := \alpha \cdot op(A) \cdot x + \beta \cdot y, \]with\[ op(A) = \left\{ \begin{array}{ll} A, & \text{if transA == HIPSPARSE_OPERATION_NON_TRANSPOSE} \end{array} \right. \]**Example**int main(int argc, char* argv[]) { // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // A sparse matrix // 1 0 3 4 // 0 0 5 1 // 0 2 0 0 // 4 0 0 8 int hAptr[5] = {0, 3, 5, 6, 8}; int hAcol[8] = {0, 2, 3, 2, 3, 1, 0, 3}; double hAval[8] = {1.0, 3.0, 4.0, 5.0, 1.0, 2.0, 4.0, 8.0}; int m = 4; int n = 4; int nnz = 8; double halpha = 1.0; double hbeta = 0.0; double hx[4] = {1.0, 2.0, 3.0, 4.0}; double hy[4] = {4.0, 5.0, 6.0, 7.0}; // Matrix descriptor hipsparseMatDescr_t descrA; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&descrA)); // Offload data to device int* dAptr = NULL; int* dAcol = NULL; double* dAval = NULL; double* dx = NULL; double* dy = NULL; HIP_CHECK(hipMalloc((void**)&dAptr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&dAcol, sizeof(int) * nnz)); HIP_CHECK(hipMalloc((void**)&dAval, sizeof(double) * nnz)); HIP_CHECK(hipMalloc((void**)&dx, sizeof(double) * n)); HIP_CHECK(hipMalloc((void**)&dy, sizeof(double) * m)); HIP_CHECK(hipMemcpy(dAptr, hAptr, sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dAcol, hAcol, sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dAval, hAval, sizeof(double) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dx, hx, sizeof(double) * n, hipMemcpyHostToDevice)); // Convert CSR matrix to HYB format hipsparseHybMat_t hybA; HIPSPARSE_CHECK(hipsparseCreateHybMat(&hybA)); HIPSPARSE_CHECK(hipsparseDcsr2hyb( handle, m, n, descrA, dAval, dAptr, dAcol, hybA, 0, HIPSPARSE_HYB_PARTITION_AUTO)); // Clean up CSR structures HIP_CHECK(hipFree(dAptr)); HIP_CHECK(hipFree(dAcol)); HIP_CHECK(hipFree(dAval)); // Call hipsparse hybmv HIPSPARSE_CHECK(hipsparseDhybmv( handle, HIPSPARSE_OPERATION_NON_TRANSPOSE, &halpha, descrA, hybA, dx, &hbeta, dy)); // Copy result back to host HIP_CHECK(hipMemcpy(hy, dy, sizeof(double) * m, hipMemcpyDeviceToHost)); std::cout << "hy" << std::endl; for(int i = 0; i < m; i++) { std::cout << hy[i] << " "; } std::cout << "" << std::endl; // Clear up on device HIPSPARSE_CHECK(hipsparseDestroyHybMat(hybA)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(descrA)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); HIP_CHECK(hipFree(dx)); HIP_CHECK(hipFree(dy)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**transA**–**[in]**matrix operation type.**alpha**–**[in]**scalar \(\alpha\).**descrA**–**[in]**descriptor of the sparse HYB matrix. Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**hybA**–**[in]**matrix in HYB storage format.**x**–**[in]**array of`n`

elements ( \(op(A) == A\)) or`m`

elements ( \(op(A) == A^T\) or \(op(A) == A^H\)).**beta**–**[in]**scalar \(\beta\).**y**–**[inout]**array of`m`

elements ( \(op(A) == A\)) or`n`

elements ( \(op(A) == A^T\) or \(op(A) == A^H\)).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`descrA`

,`alpha`

,`hybA`

,`x`

,`beta`

or`y`

is invalid.**HIPSPARSE_STATUS_ARCH_MISMATCH**– the device is not supported.**HIPSPARSE_STATUS_ALLOC_FAILED**– the buffer could not be allocated.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`transA`

!=[HIPSPARSE_OPERATION_NON_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141a270f0124eb0d0ac15c3e7afb18064547)or[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXbsrmv()[#](#hipsparsexbsrmv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSbsrmv([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int mb, int nb, int nnzb, const float *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const float *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim, const float *x, const float *beta, float *y)[#](#_CPPv415hipsparseSbsrmv17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_tiiiPKfK19hipsparseMatDescr_tPKfPKiPKiiPKfPKfPf)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDbsrmv([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int mb, int nb, int nnzb, const double *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const double *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim, const double *x, const double *beta, double *y)[#](#_CPPv415hipsparseDbsrmv17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_tiiiPKdK19hipsparseMatDescr_tPKdPKiPKiiPKdPKdPd)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCbsrmv([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int mb, int nb, int nnzb, const hipComplex *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipComplex *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim, const hipComplex *x, const hipComplex *beta, hipComplex *y)[#](#_CPPv415hipsparseCbsrmv17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_tiiiPK10hipComplexK19hipsparseMatDescr_tPK10hipComplexPKiPKiiPK10hipComplexPK10hipComplexP10hipComplex)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZbsrmv([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int mb, int nb, int nnzb, const hipDoubleComplex *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipDoubleComplex *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim, const hipDoubleComplex *x, const hipDoubleComplex *beta, hipDoubleComplex *y)[#](#_CPPv415hipsparseZbsrmv17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_tiiiPK16hipDoubleComplexK19hipsparseMatDescr_tPK16hipDoubleComplexPKiPKiiPK16hipDoubleComplexPK16hipDoubleComplexP16hipDoubleComplex) Sparse matrix vector multiplication using BSR storage format.

`hipsparseXbsrmv`

multiplies the scalar \(\alpha\) with a sparse \(m \times n\) matrix, defined in BSR storage format, and the dense vector \(x\) and adds the result to the dense vector \(y\) that is multiplied by the scalar \(\beta\), such that\[ y := \alpha \cdot op(A) \cdot x + \beta \cdot y, \]with\[ op(A) = \left\{ \begin{array}{ll} A, & \text{if trans == HIPSPARSE_OPERATION_NON_TRANSPOSE} \end{array} \right. \]and where \(m = mb \times blockDim\) and \(n= nb \times blockDim\).**Example**int main(int argc, char* argv[]) { // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // alpha * ( 1.0 0.0 2.0 ) * ( 1.0 ) + beta * ( 4.0 ) = ( 31.1 ) // ( 3.0 0.0 4.0 ) * ( 2.0 ) ( 5.0 ) = ( 62.0 ) // ( 5.0 6.0 0.0 ) * ( 3.0 ) ( 6.0 ) = ( 70.7 ) // ( 7.0 0.0 8.0 ) * ( 7.0 ) = ( 123.8 ) // BSR block dimension const int bsr_dim = 2; // Number of block rows and columns const int mb = 2; const int nb = 2; // Number of non-zero blocks const int nnzb = 4; // Number of rows and columns const int m = mb * bsr_dim; const int n = nb * bsr_dim; // BSR row pointers int hbsrRowPtr[mb + 1] = {0, 2, 4}; // BSR column indices int hbsrColInd[nnzb] = {0, 1, 0, 1}; // BSR values double hbsrVal[nnzb * bsr_dim * bsr_dim] = {1.0, 3.0, 0.0, 0.0, 2.0, 4.0, 0.0, 0.0, 5.0, 7.0, 6.0, 0.0, 0.0, 8.0, 0.0, 0.0}; // Block storage in column major hipsparseDirection_t dir = HIPSPARSE_DIRECTION_COLUMN; // Transposition of the matrix hipsparseOperation_t trans = HIPSPARSE_OPERATION_NON_TRANSPOSE; // Scalar alpha and beta double alpha = 3.7; double beta = 1.3; // x and y double hx[n] = {1.0, 2.0, 3.0, 0.0}; double hy[m] = {4.0, 5.0, 6.0, 7.0}; // Matrix descriptor hipsparseMatDescr_t descr; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&descr)); // Offload data to device int* dbsrRowPtr; int* dbsrColInd; double* dbsrVal; double* dx; double* dy; HIP_CHECK(hipMalloc((void**)&dbsrRowPtr, sizeof(int) * (mb + 1))); HIP_CHECK(hipMalloc((void**)&dbsrColInd, sizeof(int) * nnzb)); HIP_CHECK(hipMalloc((void**)&dbsrVal, sizeof(double) * nnzb * bsr_dim * bsr_dim)); HIP_CHECK(hipMalloc((void**)&dx, sizeof(double) * n)); HIP_CHECK(hipMalloc((void**)&dy, sizeof(double) * m)); HIP_CHECK(hipMemcpy(dbsrRowPtr, hbsrRowPtr, sizeof(int) * (mb + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dbsrColInd, hbsrColInd, sizeof(int) * nnzb, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( dbsrVal, hbsrVal, sizeof(double) * nnzb * bsr_dim * bsr_dim, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dx, hx, sizeof(double) * n, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dy, hy, sizeof(double) * m, hipMemcpyHostToDevice)); // Call dbsrmv to perform y = alpha * A x + beta * y HIPSPARSE_CHECK(hipsparseDbsrmv(handle, dir, trans, mb, nb, nnzb, &alpha, descr, dbsrVal, dbsrRowPtr, dbsrColInd, bsr_dim, dx, &beta, dy)); // Copy result back to host HIP_CHECK(hipMemcpy(hy, dy, sizeof(double) * m, hipMemcpyDeviceToHost)); std::cout << "hy" << std::endl; for(int i = 0; i < m; i++) { std::cout << hy[i] << " "; } std::cout << "" << std::endl; // Clear hipSPARSE HIPSPARSE_CHECK(hipsparseDestroyMatDescr(descr)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); // Clear device memory HIP_CHECK(hipFree(dbsrRowPtr)); HIP_CHECK(hipFree(dbsrColInd)); HIP_CHECK(hipFree(dbsrVal)); HIP_CHECK(hipFree(dx)); HIP_CHECK(hipFree(dy)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**dirA**–**[in]**matrix storage of BSR blocks.**transA**–**[in]**matrix operation type.**mb**–**[in]**number of block rows of the sparse BSR matrix.**nb**–**[in]**number of block columns of the sparse BSR matrix.**nnzb**–**[in]**number of non-zero blocks of the sparse BSR matrix.**alpha**–**[in]**scalar \(\alpha\).**descrA**–**[in]**descriptor of the sparse BSR matrix. Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**bsrSortedValA**–**[in]**array of`nnzb`

blocks of the sparse BSR matrix.**bsrSortedRowPtrA**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix.**bsrSortedColIndA**–**[in]**array of`nnzb`

elements containing the block column indices of the sparse BSR matrix.**blockDim**–**[in]**block dimension of the sparse BSR matrix.**x**–**[in]**array of`nb*blockDim`

elements ( \(op(A) = A\)) or`mb*blockDim`

elements ( \(op(A) = A^T\) or \(op(A) = A^H\)).**beta**–**[in]**scalar \(\beta\).**y**–**[inout]**array of`mb*blockDim`

elements ( \(op(A) = A\)) or`nb*blockDim`

elements ( \(op(A) = A^T\) or \(op(A) = A^H\)).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`mb`

,`nb`

,`nnzb`

,`blockDim`

,`descr`

,`alpha`

,`bsrSortedValA`

,`bsrSortedRowPtrA`

,`bsrSortedColIndA`

,`x`

,`beta`

or`y`

is invalid.**HIPSPARSE_STATUS_ARCH_MISMATCH**– the device is not supported.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`trans`

!=[HIPSPARSE_OPERATION_NON_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141a270f0124eb0d0ac15c3e7afb18064547)or[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXbsrxmv()[#](#hipsparsexbsrxmv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSbsrxmv([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dir,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)trans, int sizeOfMask, int mb, int nb, int nnzb, const float *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descr, const float *bsrVal, const int *bsrMaskPtr, const int *bsrRowPtr, const int *bsrEndPtr, const int *bsrColInd, int blockDim, const float *x, const float *beta, float *y)[#](#_CPPv416hipsparseSbsrxmv17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_tiiiiPKfK19hipsparseMatDescr_tPKfPKiPKiPKiPKiiPKfPKfPf)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDbsrxmv([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dir,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)trans, int sizeOfMask, int mb, int nb, int nnzb, const double *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descr, const double *bsrVal, const int *bsrMaskPtr, const int *bsrRowPtr, const int *bsrEndPtr, const int *bsrColInd, int blockDim, const double *x, const double *beta, double *y)[#](#_CPPv416hipsparseDbsrxmv17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_tiiiiPKdK19hipsparseMatDescr_tPKdPKiPKiPKiPKiiPKdPKdPd)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCbsrxmv([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dir,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)trans, int sizeOfMask, int mb, int nb, int nnzb, const hipComplex *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descr, const hipComplex *bsrVal, const int *bsrMaskPtr, const int *bsrRowPtr, const int *bsrEndPtr, const int *bsrColInd, int blockDim, const hipComplex *x, const hipComplex *beta, hipComplex *y)[#](#_CPPv416hipsparseCbsrxmv17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_tiiiiPK10hipComplexK19hipsparseMatDescr_tPK10hipComplexPKiPKiPKiPKiiPK10hipComplexPK10hipComplexP10hipComplex)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZbsrxmv([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dir,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)trans, int sizeOfMask, int mb, int nb, int nnzb, const hipDoubleComplex *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descr, const hipDoubleComplex *bsrVal, const int *bsrMaskPtr, const int *bsrRowPtr, const int *bsrEndPtr, const int *bsrColInd, int blockDim, const hipDoubleComplex *x, const hipDoubleComplex *beta, hipDoubleComplex *y)[#](#_CPPv416hipsparseZbsrxmv17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_tiiiiPK16hipDoubleComplexK19hipsparseMatDescr_tPK16hipDoubleComplexPKiPKiPKiPKiiPK16hipDoubleComplexPK16hipDoubleComplexP16hipDoubleComplex) Sparse matrix vector multiplication with mask operation using BSR storage format.

`hipsparseXbsrxmv`

multiplies the scalar \(\alpha\) with a sparse \((mb \times \text{blockDim}) \times (nb \times \text{blockDim})\) modified matrix, defined in BSR storage format, and the dense vector \(x\) and adds the result to the dense vector \(y\) that is multiplied by the scalar \(\beta\), such that\[ y := \left( \alpha \cdot op(A) \cdot x + \beta \cdot y \right)\left( \text{mask} \right), \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if trans == HIPSPARSE_OPERATION_NON_TRANSPOSE} \\ A^T, & \text{if trans == HIPSPARSE_OPERATION_TRANSPOSE} \\ A^H, & \text{if trans == HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE} \end{array} \right. \end{split}\]The \(\text{mask}\) is defined as an array of block row indices. The input sparse matrix is defined with a modified BSR storage format where the beginning and the end of each row is defined with two arrays,

`bsrRowPtr`

and`bsr_end_ptr`

(both of size`mb`

), rather the usual`bsrRowPtr`

of size`mb+1`

.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

Currently, only

`trans`

==[HIPSPARSE_OPERATION_NON_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141a270f0124eb0d0ac15c3e7afb18064547)is supported. Currently,`blockDim`

== 1 is not supported.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**dir**–**[in]**matrix storage of BSR blocks.**trans**–**[in]**matrix operation type.**sizeOfMask**–**[in]**number of updated block rows of the array`y`

.**mb**–**[in]**number of block rows of the sparse BSR matrix.**nb**–**[in]**number of block columns of the sparse BSR matrix.**nnzb**–**[in]**number of non-zero blocks of the sparse BSR matrix.**alpha**–**[in]**scalar \(\alpha\).**descr**–**[in]**descriptor of the sparse BSR matrix. Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**bsrVal**–**[in]**array of`nnzb`

blocks of the sparse BSR matrix.**bsrMaskPtr**–**[in]**array of`sizeOfMask`

elements that give the indices of the updated block rows.**bsrRowPtr**–**[in]**array of`mb`

elements that point to the start of every block row of the sparse BSR matrix.**bsrEndPtr**–**[in]**array of`mb`

elements that point to the end of every block row of the sparse BSR matrix.**bsrColInd**–**[in]**array of`nnzb`

elements containing the block column indices of the sparse BSR matrix.**blockDim**–**[in]**block dimension of the sparse BSR matrix.**x**–**[in]**array of`nb*blockDim`

elements ( \(op(A) = A\)) or`mb*blockDim`

elements ( \(op(A) = A^T\) or \(op(A) = A^H\)).**beta**–**[in]**scalar \(\beta\).**y**–**[inout]**array of`mb*blockDim`

elements ( \(op(A) = A\)) or`nb*blockDim`

elements ( \(op(A) = A^T\) or \(op(A) = A^H\)).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`mb`

,`nb`

,`nnzb`

,`blockDim`

,`sizeOfMask`

,`descr`

,`alpha`

,`bsrVal`

,`bsrRowPtr`

,`bsrEndPtr`

,`bsrColInd`

,`x`

,`beta`

or`y`

is invalid or if`sizeOfMask`

is greater than`mb`

.**HIPSPARSE_STATUS_ARCH_MISMATCH**– the device is not supported.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`blockDim==1`

,`trans`

!=[HIPSPARSE_OPERATION_NON_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141a270f0124eb0d0ac15c3e7afb18064547)or[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXbsrsv2_zeroPivot()[#](#hipsparsexbsrsv2-zeropivot)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseXbsrsv2_zeroPivot([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[bsrsv2Info_t](types.html#_CPPv412bsrsv2Info_t)info, int *position)[#](#_CPPv426hipsparseXbsrsv2_zeroPivot17hipsparseHandle_t12bsrsv2Info_tPi) `hipsparseXbsrsv2_zeroPivot`

returns[HIPSPARSE_STATUS_ZERO_PIVOT](types.html#hipsparse-types_8h_1aa069bec7a4f24d00dab1dc4612d4de79a88ff0f0537dfe037fcf9f99ff0cf79da), if either a structural or numerical zero has been found during[hipsparseXbsrsv2_analysis()](#hipsparse__bsrsv_8h_1ac81adbb927bbccfc1627e3c0f36ea8bd)or[hipsparseXbsrsv2_solve()](#hipsparse__bsrsv_8h_1a7a6e7dac8f1cb43d92ea2df1f1e65c18)computation. The first zero pivot \(j\) at \(A_{j,j}\) is stored in`position`

, using same index base as the BSR matrix.`position`

can be in host or device memory. If no zero pivot has been found,`position`

is set to -1 and[HIPSPARSE_STATUS_SUCCESS](types.html#hipsparse-types_8h_1aa069bec7a4f24d00dab1dc4612d4de79a146a8a2fd27ee49132f8dcea617fc481)is returned instead.Note

`hipsparseXbsrsv2_zeroPivot`

is a blocking function. It might influence performance negatively.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**info**–**[in]**structure that holds the information collected during the analysis step.**position**–**[inout]**pointer to zero pivot \(j\), can be in host or device memory.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`info`

or`position`

is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.**HIPSPARSE_STATUS_ZERO_PIVOT**– zero pivot has been found.



## hipsparseXbsrsv2_bufferSize()[#](#hipsparsexbsrsv2-buffersize)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSbsrsv2_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int mb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, float *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrsv2Info_t](types.html#_CPPv412bsrsv2Info_t)info, int *pBufferSizeInBytes)[#](#_CPPv427hipsparseSbsrsv2_bufferSize17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_tiiK19hipsparseMatDescr_tPfPKiPKii12bsrsv2Info_tPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDbsrsv2_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int mb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, double *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrsv2Info_t](types.html#_CPPv412bsrsv2Info_t)info, int *pBufferSizeInBytes)[#](#_CPPv427hipsparseDbsrsv2_bufferSize17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_tiiK19hipsparseMatDescr_tPdPKiPKii12bsrsv2Info_tPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCbsrsv2_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int mb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, hipComplex *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrsv2Info_t](types.html#_CPPv412bsrsv2Info_t)info, int *pBufferSizeInBytes)[#](#_CPPv427hipsparseCbsrsv2_bufferSize17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_tiiK19hipsparseMatDescr_tP10hipComplexPKiPKii12bsrsv2Info_tPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZbsrsv2_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int mb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, hipDoubleComplex *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrsv2Info_t](types.html#_CPPv412bsrsv2Info_t)info, int *pBufferSizeInBytes)[#](#_CPPv427hipsparseZbsrsv2_bufferSize17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_tiiK19hipsparseMatDescr_tP16hipDoubleComplexPKiPKii12bsrsv2Info_tPi) `hipsparseXbsrsv2_bufferSize`

returns the size of the temporary storage buffer in bytes that is required by[hipsparseXbsrsv2_analysis()](#hipsparse__bsrsv_8h_1ac81adbb927bbccfc1627e3c0f36ea8bd)and[hipsparseXbsrsv2_solve()](#hipsparse__bsrsv_8h_1a7a6e7dac8f1cb43d92ea2df1f1e65c18). The temporary storage buffer must be allocated by the user.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**dirA**–**[in]**matrix storage of BSR blocks.**transA**–**[in]**matrix operation type.**mb**–**[in]**number of block rows of the sparse BSR matrix.**nnzb**–**[in]**number of non-zero blocks of the sparse BSR matrix.**descrA**–**[in]**descriptor of the sparse BSR matrix.**bsrSortedValA**–**[in]**array of`nnzb`

blocks of the sparse BSR matrix.**bsrSortedRowPtrA**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix.**bsrSortedColIndA**–**[in]**array of`nnz`

containing the block column indices of the sparse BSR matrix.**blockDim**–**[in]**block dimension of the sparse BSR matrix.**info**–**[out]**structure that holds the information collected during the analysis step.**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer required by[hipsparseXbsrsv2_analysis()](#hipsparse__bsrsv_8h_1ac81adbb927bbccfc1627e3c0f36ea8bd)and[hipsparseXbsrsv2_solve()](#hipsparse__bsrsv_8h_1a7a6e7dac8f1cb43d92ea2df1f1e65c18).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`mb`

,`nnzb`

or`blockDim`

,`descr`

,`bsrSortedValA`

,`bsrSortedRowPtrA`

,`bsrSortedColIndA`

,`info`

or`pBufferSizeInBytes`

is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`transA`

==[HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141ac55e75ba3027186f1dc6164fdcb06f0e)or[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXbsrsv2_bufferSizeExt()[#](#hipsparsexbsrsv2-buffersizeext)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSbsrsv2_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int mb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, float *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrsv2Info_t](types.html#_CPPv412bsrsv2Info_t)info, size_t *pBufferSizeInBytes)[#](#_CPPv430hipsparseSbsrsv2_bufferSizeExt17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_tiiK19hipsparseMatDescr_tPfPKiPKii12bsrsv2Info_tP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDbsrsv2_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int mb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, double *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrsv2Info_t](types.html#_CPPv412bsrsv2Info_t)info, size_t *pBufferSizeInBytes)[#](#_CPPv430hipsparseDbsrsv2_bufferSizeExt17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_tiiK19hipsparseMatDescr_tPdPKiPKii12bsrsv2Info_tP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCbsrsv2_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int mb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, hipComplex *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrsv2Info_t](types.html#_CPPv412bsrsv2Info_t)info, size_t *pBufferSizeInBytes)[#](#_CPPv430hipsparseCbsrsv2_bufferSizeExt17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_tiiK19hipsparseMatDescr_tP10hipComplexPKiPKii12bsrsv2Info_tP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZbsrsv2_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int mb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, hipDoubleComplex *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrsv2Info_t](types.html#_CPPv412bsrsv2Info_t)info, size_t *pBufferSizeInBytes)[#](#_CPPv430hipsparseZbsrsv2_bufferSizeExt17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_tiiK19hipsparseMatDescr_tP16hipDoubleComplexPKiPKii12bsrsv2Info_tP6size_t) `hipsparseXbsrsv2_bufferSizeExt`

returns the size of the temporary storage buffer in bytes that is required by[hipsparseXbsrsv2_analysis()](#hipsparse__bsrsv_8h_1ac81adbb927bbccfc1627e3c0f36ea8bd)and[hipsparseXbsrsv2_solve()](#hipsparse__bsrsv_8h_1a7a6e7dac8f1cb43d92ea2df1f1e65c18). The temporary storage buffer must be allocated by the user.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**dirA**–**[in]**matrix storage of BSR blocks.**transA**–**[in]**matrix operation type.**mb**–**[in]**number of block rows of the sparse BSR matrix.**nnzb**–**[in]**number of non-zero blocks of the sparse BSR matrix.**descrA**–**[in]**descriptor of the sparse BSR matrix.**bsrSortedValA**–**[in]**array of`nnzb`

blocks of the sparse BSR matrix.**bsrSortedRowPtrA**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix.**bsrSortedColIndA**–**[in]**array of`nnz`

containing the block column indices of the sparse BSR matrix.**blockDim**–**[in]**block dimension of the sparse BSR matrix.**info**–**[out]**structure that holds the information collected during the analysis step.**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer required by[hipsparseXbsrsv2_analysis()](#hipsparse__bsrsv_8h_1ac81adbb927bbccfc1627e3c0f36ea8bd)and[hipsparseXbsrsv2_solve()](#hipsparse__bsrsv_8h_1a7a6e7dac8f1cb43d92ea2df1f1e65c18).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`mb`

,`nnzb`

or`blockDim`

,`descr`

,`bsrSortedValA`

,`bsrSortedRowPtrA`

,`bsrSortedColIndA`

,`info`

or`pBufferSizeInBytes`

is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`transA`

==[HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141ac55e75ba3027186f1dc6164fdcb06f0e)or[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXbsrsv2_analysis()[#](#hipsparsexbsrsv2-analysis)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSbsrsv2_analysis([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int mb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const float *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrsv2Info_t](types.html#_CPPv412bsrsv2Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv425hipsparseSbsrsv2_analysis17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_tiiK19hipsparseMatDescr_tPKfPKiPKii12bsrsv2Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDbsrsv2_analysis([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int mb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const double *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrsv2Info_t](types.html#_CPPv412bsrsv2Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv425hipsparseDbsrsv2_analysis17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_tiiK19hipsparseMatDescr_tPKdPKiPKii12bsrsv2Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCbsrsv2_analysis([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int mb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipComplex *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrsv2Info_t](types.html#_CPPv412bsrsv2Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv425hipsparseCbsrsv2_analysis17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_tiiK19hipsparseMatDescr_tPK10hipComplexPKiPKii12bsrsv2Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZbsrsv2_analysis([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int mb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipDoubleComplex *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrsv2Info_t](types.html#_CPPv412bsrsv2Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv425hipsparseZbsrsv2_analysis17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_tiiK19hipsparseMatDescr_tPK16hipDoubleComplexPKiPKii12bsrsv2Info_t22hipsparseSolvePolicy_tPv) `hipsparseXbsrsv2_analysis`

performs the analysis step for[hipsparseXbsrsv2_solve()](#hipsparse__bsrsv_8h_1a7a6e7dac8f1cb43d92ea2df1f1e65c18). It is expected that this function will be executed only once for a given matrix and particular operation type.Note

If the matrix sparsity pattern changes, the gathered information will become invalid.

Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**dirA**–**[in]**matrix storage of BSR blocks.**transA**–**[in]**matrix operation type.**mb**–**[in]**number of block rows of the sparse BSR matrix.**nnzb**–**[in]**number of non-zero blocks of the sparse BSR matrix.**descrA**–**[in]**descriptor of the sparse BSR matrix.**bsrSortedValA**–**[in]**array of`nnzb`

blocks of the sparse BSR matrix.**bsrSortedRowPtrA**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix.**bsrSortedColIndA**–**[in]**array of`nnz`

containing the block column indices of the sparse BSR matrix.**blockDim**–**[in]**block dimension of the sparse BSR matrix.**info**–**[out]**structure that holds the information collected during the analysis step.**policy**–**[in]**[HIPSPARSE_SOLVE_POLICY_NO_LEVEL](types.html#hipsparse-types_8h_1a0d98e490c94d4facc231db60baf1c3b3ac5830aa96848e832b3b375ad08abdb09)or[HIPSPARSE_SOLVE_POLICY_USE_LEVEL](types.html#hipsparse-types_8h_1a0d98e490c94d4facc231db60baf1c3b3a934309d6656638e375f0759b89fd81b5).**pBuffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`mb`

,`nnzb`

,`blockDim`

,`descrA`

,`bsrSortedRowPtrA`

,`bsrSortedColIndA`

,`info`

or`pBuffer`

is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`transA`

==[HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141ac55e75ba3027186f1dc6164fdcb06f0e)or[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXbsrsv2_solve()[#](#hipsparsexbsrsv2-solve)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSbsrsv2_solve([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int mb, int nnzb, const float *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const float *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrsv2Info_t](types.html#_CPPv412bsrsv2Info_t)info, const float *f, float *x,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv422hipsparseSbsrsv2_solve17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_tiiPKfK19hipsparseMatDescr_tPKfPKiPKii12bsrsv2Info_tPKfPf22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDbsrsv2_solve([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int mb, int nnzb, const double *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const double *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrsv2Info_t](types.html#_CPPv412bsrsv2Info_t)info, const double *f, double *x,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv422hipsparseDbsrsv2_solve17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_tiiPKdK19hipsparseMatDescr_tPKdPKiPKii12bsrsv2Info_tPKdPd22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCbsrsv2_solve([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int mb, int nnzb, const hipComplex *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipComplex *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrsv2Info_t](types.html#_CPPv412bsrsv2Info_t)info, const hipComplex *f, hipComplex *x,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv422hipsparseCbsrsv2_solve17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_tiiPK10hipComplexK19hipsparseMatDescr_tPK10hipComplexPKiPKii12bsrsv2Info_tPK10hipComplexP10hipComplex22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZbsrsv2_solve([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int mb, int nnzb, const hipDoubleComplex *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipDoubleComplex *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrsv2Info_t](types.html#_CPPv412bsrsv2Info_t)info, const hipDoubleComplex *f, hipDoubleComplex *x,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv422hipsparseZbsrsv2_solve17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_tiiPK16hipDoubleComplexK19hipsparseMatDescr_tPK16hipDoubleComplexPKiPKii12bsrsv2Info_tPK16hipDoubleComplexP16hipDoubleComplex22hipsparseSolvePolicy_tPv) Sparse triangular solve using BSR storage format.

`hipsparseXbsrsv2_solve`

solves a sparse triangular linear system of a sparse \(m \times m\) matrix, defined in BSR storage format, a dense solution vector \(y\) and the right-hand side \(x\) that is multiplied by \(\alpha\), such that\[ op(A) \cdot y = \alpha \cdot x, \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if trans == HIPSPARSE_OPERATION_NON_TRANSPOSE} \\ A^T, & \text{if trans == HIPSPARSE_OPERATION_TRANSPOSE} \end{array} \right. \end{split}\]Performing the above operation requires three steps. First, the user calls

[hipsparseXbsrsv2_bufferSize()](#hipsparse__bsrsv_8h_1a83d97ea0c338ecf860e6292b5d7637dd)which will determine the size of the required temporary storage buffer. The user then allocates this buffer and calls[hipsparseXbsrsv2_analysis()](#hipsparse__bsrsv_8h_1ac81adbb927bbccfc1627e3c0f36ea8bd)which will perform analysis on the sparse matrix \(op(A)\). Finally, the user completes the computation by calling`hipsparseXbsrsv2_solve`

. The buffer size, buffer allocation, and analysis only need to be called once for a given sparse matrix \(op(A)\) while the computation stage can be repeatedly used with different \(x\) and \(y\) vectors. Once all calls to`hipsparseXbsrsv2_solve`

are complete, the temporary buffer can be deallocated.Solving a triangular system involves inverting the diagonal blocks. This means that if the sparse matrix is missing the diagonal block (referred to as a structural zero) or the diagonal block is not invertible (referred to as a numerical zero) then a solution is not possible.

`hipsparseXbsrsv2_solve`

tracks the location of the first zero pivot (either numerical or structural zero). The zero pivot status can be checked calling[hipsparseXbsrsv2_zeroPivot()](#hipsparse__bsrsv_8h_1a8772270c10f8bdfb033e0dbb7d74cd82). If[hipsparseXbsrsv2_zeroPivot()](#hipsparse__bsrsv_8h_1a8772270c10f8bdfb033e0dbb7d74cd82)returns[HIPSPARSE_STATUS_SUCCESS](types.html#hipsparse-types_8h_1aa069bec7a4f24d00dab1dc4612d4de79a146a8a2fd27ee49132f8dcea617fc481), then no zero pivot was found and therefore the matrix does not have a structural or numerical zero.The user can specify that the sparse matrix should be interpreted as having identity blocks on the diagonal by setting the diagonal type on the descriptor

`descrA`

to[HIPSPARSE_DIAG_TYPE_UNIT](types.html#hipsparse-types_8h_1a79e036b6c0680cb37e2aa53d3542a054a532a9a4a4eaf63a967bfaac7f9936b39)using[hipsparseSetMatDiagType](auxiliary.html#hipsparse-auxiliary_8h_1aec6fa039793196011f15cfb0b21c2b59). If[hipsparseDiagType_t](types.html#hipsparse-types_8h_1a79e036b6c0680cb37e2aa53d3542a054)==[HIPSPARSE_DIAG_TYPE_UNIT](types.html#hipsparse-types_8h_1a79e036b6c0680cb37e2aa53d3542a054a532a9a4a4eaf63a967bfaac7f9936b39), no zero pivot will be reported, even if the diagonal block \(A_{j,j}\) for some \(j\) is not invertible.The sparse CSR matrix passed to

`hipsparseXbsrsv2_solve`

does not actually have to be a triangular matrix. Instead the triangular upper or lower part of the sparse matrix is solved based on[hipsparseFillMode_t](types.html#hipsparse-types_8h_1ace47655e52ed1bb17309eda331c44332)set on the descriptor`descrA`

. If the fill mode is set to[HIPSPARSE_FILL_MODE_LOWER](types.html#hipsparse-types_8h_1ace47655e52ed1bb17309eda331c44332a470abb0661ab8951449efa6988ed49ef), then the lower triangular matrix is solved. If the fill mode is set to[HIPSPARSE_FILL_MODE_UPPER](types.html#hipsparse-types_8h_1ace47655e52ed1bb17309eda331c44332ac5c8ccc62dfff77c56c8480c24ed6b3b)then the upper triangular matrix is solved.**Example**int main(int argc, char* argv[]) { // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // A = ( 1.0 0.0 0.0 0.0 ) // ( 2.0 3.0 0.0 0.0 ) // ( 4.0 5.0 6.0 0.0 ) // ( 7.0 0.0 8.0 9.0 ) // // with bsr_dim = 2 // // ------------------- // = | 1.0 0.0 | 0.0 0.0 | // | 2.0 3.0 | 0.0 0.0 | // ------------------- // | 4.0 5.0 | 6.0 0.0 | // | 7.0 0.0 | 8.0 9.0 | // ------------------- // Number of rows (matrix must be square) const int m = 4; // Number of block rows and block columns const int mb = 2; const int nb = 2; // BSR block dimension const int bsr_dim = 2; // Number of non-zero blocks const int nnzb = 3; // BSR row pointers int hbsrRowPtr[mb + 1] = {0, 1, 3}; // BSR column indices int hbsrColInd[nnzb] = {0, 0, 1}; // BSR values double hbsrVal[nnzb * bsr_dim * bsr_dim] = {1.0, 2.0, 0.0, 3.0, 4.0, 7.0, 5.0, 0.0, 6.0, 8.0, 0.0, 9.0}; // Storage scheme of the BSR blocks hipsparseDirection_t dir = HIPSPARSE_DIRECTION_COLUMN; // Transposition of the matrix and rhs matrix hipsparseOperation_t trans = HIPSPARSE_OPERATION_NON_TRANSPOSE; // Solve policy hipsparseSolvePolicy_t solve_policy = HIPSPARSE_SOLVE_POLICY_USE_LEVEL; // Scalar alpha and beta double alpha = 3.7; double hx[m] = {1, 2, 3, 4}; double hy[m]; // Offload data to device int* dbsrRowPtr; int* dbsrColInd; double* dbsrVal; double* dx; double* dy; HIP_CHECK(hipMalloc((void**)&dbsrRowPtr, sizeof(int) * (mb + 1))); HIP_CHECK(hipMalloc((void**)&dbsrColInd, sizeof(int) * nnzb)); HIP_CHECK(hipMalloc((void**)&dbsrVal, sizeof(double) * nnzb * bsr_dim * bsr_dim)); HIP_CHECK(hipMalloc((void**)&dx, sizeof(double) * m)); HIP_CHECK(hipMalloc((void**)&dy, sizeof(double) * m)); HIP_CHECK(hipMemcpy(dbsrRowPtr, hbsrRowPtr, sizeof(int) * (mb + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dbsrColInd, hbsrColInd, sizeof(int) * nnzb, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( dbsrVal, hbsrVal, sizeof(double) * nnzb * bsr_dim * bsr_dim, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dx, hx, sizeof(double) * m, hipMemcpyHostToDevice)); // Matrix descriptor hipsparseMatDescr_t descr; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&descr)); // Matrix fill mode HIPSPARSE_CHECK(hipsparseSetMatFillMode(descr, HIPSPARSE_FILL_MODE_LOWER)); // Matrix diagonal type HIPSPARSE_CHECK(hipsparseSetMatDiagType(descr, HIPSPARSE_DIAG_TYPE_UNIT)); // Matrix info structure bsrsv2Info_t info; HIPSPARSE_CHECK(hipsparseCreateBsrsv2Info(&info)); // Obtain required buffer size int buffer_size; HIPSPARSE_CHECK(hipsparseDbsrsv2_bufferSize(handle, dir, trans, mb, nnzb, descr, dbsrVal, dbsrRowPtr, dbsrColInd, bsr_dim, info, &buffer_size)); // Allocate temporary buffer void* dbuffer; HIP_CHECK(hipMalloc(&dbuffer, buffer_size)); // Perform analysis step HIPSPARSE_CHECK(hipsparseDbsrsv2_analysis(handle, dir, trans, mb, nnzb, descr, dbsrVal, dbsrRowPtr, dbsrColInd, bsr_dim, info, solve_policy, dbuffer)); // Call dbsrsm to perform lower triangular solve LX = B HIPSPARSE_CHECK(hipsparseDbsrsv2_solve(handle, dir, trans, mb, nnzb, &alpha, descr, dbsrVal, dbsrRowPtr, dbsrColInd, bsr_dim, info, dx, dy, solve_policy, dbuffer)); // Check for zero pivots int pivot; hipsparseStatus_t status = hipsparseXbsrsv2_zeroPivot(handle, info, &pivot); if(status == HIPSPARSE_STATUS_ZERO_PIVOT) { std::cout << "Found zero pivot in matrix row " << pivot << std::endl; } // Copy results back to the host HIP_CHECK(hipMemcpy(hy, dy, sizeof(double) * m, hipMemcpyDeviceToHost)); std::cout << "hy" << std::endl; for(int i = 0; i < m; i++) { std::cout << hy[i] << " "; } std::cout << "" << std::endl; // Clear hipSPARSE HIPSPARSE_CHECK(hipsparseDestroyBsrsv2Info(info)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(descr)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); // Clear device memory HIP_CHECK(hipFree(dbsrRowPtr)); HIP_CHECK(hipFree(dbsrColInd)); HIP_CHECK(hipFree(dbsrVal)); HIP_CHECK(hipFree(dx)); HIP_CHECK(hipFree(dy)); HIP_CHECK(hipFree(dbuffer)); return 0; }


Note

The sparse BSR matrix has to be sorted.

Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

Currently, only

`transA`

==[HIPSPARSE_OPERATION_NON_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141a270f0124eb0d0ac15c3e7afb18064547)and`transA`

==[HIPSPARSE_OPERATION_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141a20e9c4bdd71ea4b509b6c0b7a495c0bf)is supported.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**dirA**–**[in]**matrix storage of BSR blocks.**transA**–**[in]**matrix operation type.**mb**–**[in]**number of block rows of the sparse BSR matrix.**nnzb**–**[in]**number of non-zero blocks of the sparse BSR matrix.**alpha**–**[in]**scalar \(\alpha\).**descrA**–**[in]**descriptor of the sparse BSR matrix.**bsrSortedValA**–**[in]**array of`nnzb`

blocks of the sparse BSR matrix.**bsrSortedRowPtrA**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix.**bsrSortedColIndA**–**[in]**array of`nnz`

containing the block column indices of the sparse BSR matrix.**blockDim**–**[in]**block dimension of the sparse BSR matrix.**info**–**[in]**structure that holds the information collected during the analysis step.**f**–**[in]**array of`m`

elements, holding the right-hand side.**x**–**[out]**array of`m`

elements, holding the solution.**policy**–**[in]**[HIPSPARSE_SOLVE_POLICY_NO_LEVEL](types.html#hipsparse-types_8h_1a0d98e490c94d4facc231db60baf1c3b3ac5830aa96848e832b3b375ad08abdb09)or[HIPSPARSE_SOLVE_POLICY_USE_LEVEL](types.html#hipsparse-types_8h_1a0d98e490c94d4facc231db60baf1c3b3a934309d6656638e375f0759b89fd81b5).**pBuffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`mb`

,`nnzb`

,`blockDim`

,`descrA`

,`alpha`

,`bsrSortedValA`

,`bsrSortedRowPtrA`

,`bsrSortedColIndA`

,`f`

or`x`

is invalid.**HIPSPARSE_STATUS_ARCH_MISMATCH**– the device is not supported.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`transA`

==[HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141ac55e75ba3027186f1dc6164fdcb06f0e)or[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXgemvi_bufferSize()[#](#hipsparsexgemvi-buffersize)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSgemvi_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int m, int n, int nnz, int *pBufferSizeInBytes)[#](#_CPPv426hipsparseSgemvi_bufferSize17hipsparseHandle_t20hipsparseOperation_tiiiPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDgemvi_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int m, int n, int nnz, int *pBufferSizeInBytes)[#](#_CPPv426hipsparseDgemvi_bufferSize17hipsparseHandle_t20hipsparseOperation_tiiiPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCgemvi_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int m, int n, int nnz, int *pBufferSizeInBytes)[#](#_CPPv426hipsparseCgemvi_bufferSize17hipsparseHandle_t20hipsparseOperation_tiiiPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZgemvi_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int m, int n, int nnz, int *pBufferSizeInBytes)[#](#_CPPv426hipsparseZgemvi_bufferSize17hipsparseHandle_t20hipsparseOperation_tiiiPi) `hipsparseXgemvi_bufferSize`

returns the size of the temporary storage buffer in bytes required by[hipsparseXgemvi()](#hipsparse__gemvi_8h_1ace439b9bcd0663a60caae27f6581abc5). The temporary storage buffer must be allocated by the user.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**transA**–**[in]**matrix operation type.**m**–**[in]**number of rows of the dense matrix.**n**–**[in]**number of columns of the dense matrix.**nnz**–**[in]**number of non-zero entries in the sparse vector.**pBufferSizeInBytes**–**[out]**temporary storage buffer size.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`nnz`

or`pBufferSizeInBytes`

is invalid.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`transA`

!=[HIPSPARSE_OPERATION_NON_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141a270f0124eb0d0ac15c3e7afb18064547)or[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXgemvi()[#](#hipsparsexgemvi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSgemvi([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int m, int n, const float *alpha, const float *A, int lda, int nnz, const float *x, const int *xInd, const float *beta, float *y,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase, void *pBuffer)[#](#_CPPv415hipsparseSgemvi17hipsparseHandle_t20hipsparseOperation_tiiPKfPKfiiPKfPKiPKfPf20hipsparseIndexBase_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDgemvi([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int m, int n, const double *alpha, const double *A, int lda, int nnz, const double *x, const int *xInd, const double *beta, double *y,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase, void *pBuffer)[#](#_CPPv415hipsparseDgemvi17hipsparseHandle_t20hipsparseOperation_tiiPKdPKdiiPKdPKiPKdPd20hipsparseIndexBase_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCgemvi([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int m, int n, const hipComplex *alpha, const hipComplex *A, int lda, int nnz, const hipComplex *x, const int *xInd, const hipComplex *beta, hipComplex *y,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase, void *pBuffer)[#](#_CPPv415hipsparseCgemvi17hipsparseHandle_t20hipsparseOperation_tiiPK10hipComplexPK10hipComplexiiPK10hipComplexPKiPK10hipComplexP10hipComplex20hipsparseIndexBase_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZgemvi([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int m, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *A, int lda, int nnz, const hipDoubleComplex *x, const int *xInd, const hipDoubleComplex *beta, hipDoubleComplex *y,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase, void *pBuffer)[#](#_CPPv415hipsparseZgemvi17hipsparseHandle_t20hipsparseOperation_tiiPK16hipDoubleComplexPK16hipDoubleComplexiiPK16hipDoubleComplexPKiPK16hipDoubleComplexP16hipDoubleComplex20hipsparseIndexBase_tPv) Dense matrix sparse vector multiplication.

`hipsparseXgemvi`

multiplies the scalar \(\alpha\) with a dense \(m \times n\) matrix \(A\) and the sparse vector \(x\) and adds the result to the dense vector \(y\) that is multiplied by the scalar \(\beta\), such that\[ y := \alpha \cdot op(A) \cdot x + \beta \cdot y, \]with\[ op(A) = \left\{ \begin{array}{ll} A, & \text{if transA == HIPSPARSE_OPERATION_NON_TRANSPOSE} \end{array} \right. \]Performing the above operation involves two steps. First, the user calls

[hipsparseXgemvi_bufferSize()](#hipsparse__gemvi_8h_1aa99ce9ca1a224152219179805ee8ae9e)in order to determine the size of the temporary storage buffer. Next, the user allocates this temporary buffer and passes it to`hipsparseXgemvi`

to complete the computation. Once all calls to`hipsparseXgemvi`

are complete the temporary storage buffer can be freed.**Example**int main(int argc, char* argv[]) { hipsparseOperation_t opA = HIPSPARSE_OPERATION_NON_TRANSPOSE; hipsparseIndexBase_t idxBase = HIPSPARSE_INDEX_BASE_ZERO; // Scalar alpha and beta float alpha = 1.0f; float beta = 1.0f; const int m = 4; // Number of rows of A const int n = 4; // Number of columns of A const int lda = m; // leading dimension of A // A = 1 2 3 4 // 5 6 7 8 // 2 4 6 8 // 4 3 2 1 std::vector<float> hA = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f, 2.0f, 4.0f, 6.0f, 8.0f, 4.0f, 3.0f, 2.0f, 1.0f}; // Sparse vector x int nnz = 2; std::vector<int> hxInd = {0, 2}; std::vector<float> hx = {10.0f, 11.0f}; // Dense vector y std::vector<float> hy = {1.0f, 2.0f, 3.0f, 4.0f}; // Device data float* dA = nullptr; HIP_CHECK(hipMalloc((void**)&dA, sizeof(float) * m * n)); int* dxInd = nullptr; float* dx = nullptr; HIP_CHECK(hipMalloc((void**)&dxInd, sizeof(int) * nnz)); HIP_CHECK(hipMalloc((void**)&dx, sizeof(float) * nnz)); float* dy = nullptr; HIP_CHECK(hipMalloc((void**)&dy, sizeof(float) * m)); // Copy data from host to device HIP_CHECK(hipMemcpy(dA, hA.data(), sizeof(float) * m * n, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dxInd, hxInd.data(), sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dx, hx.data(), sizeof(float) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dy, hy.data(), sizeof(float) * m, hipMemcpyHostToDevice)); // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // Call hipsparseSgemvi to perform y = alpha * A * x + beta * y int bufferSize = 0; HIPSPARSE_CHECK(hipsparseSgemvi_bufferSize(handle, opA, m, n, nnz, &bufferSize)); void* dbuffer = nullptr; HIP_CHECK(hipMalloc((void**)&dbuffer, bufferSize)); HIPSPARSE_CHECK(hipsparseSgemvi( handle, opA, m, n, &alpha, dA, lda, nnz, dx, dxInd, &beta, dy, idxBase, dbuffer)); // Copy result back to host HIP_CHECK(hipMemcpy(hy.data(), dy, sizeof(float) * m, hipMemcpyDeviceToHost)); // Print the result (optional) std::cout << "hy" << std::endl; for(int i = 0; i < m; i++) { std::cout << hy[i] << " "; } std::cout << "" << std::endl; // Clear hipSPARSE HIPSPARSE_CHECK(hipsparseDestroy(handle)); // Clear device memory HIP_CHECK(hipFree(dA)); HIP_CHECK(hipFree(dxInd)); HIP_CHECK(hipFree(dx)); HIP_CHECK(hipFree(dy)); HIP_CHECK(hipFree(dbuffer)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**transA**–**[in]**matrix operation type.**m**–**[in]**number of rows of the dense matrix.**n**–**[in]**number of columns of the dense matrix.**alpha**–**[in]**scalar \(\alpha\).**A**–**[in]**pointer to the dense matrix.**lda**–**[in]**leading dimension of the dense matrix**nnz**–**[in]**number of non-zero entries in the sparse vector**x**–**[in]**array of`nnz`

elements containing the values of the sparse vector**xInd**–**[in]**array of`nnz`

elements containing the indices of the sparse vector**beta**–**[in]**scalar \(\beta\).**y**–**[inout]**array of`m`

elements ( \(op(A) == A\)) or`n`

elements ( \(op(A) == A^T\) or \(op(A) == A^H\)).**idxBase**–**[in]**[HIPSPARSE_INDEX_BASE_ZERO](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4a14913ab324aaea1154abd00ee7c50b63)or[HIPSPARSE_INDEX_BASE_ONE](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4ae48a9ab138ca9588d485c078bddc0792).**pBuffer**–**[in]**temporary storage buffer

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`lda`

,`nnz`

,`alpha`

,`A`

,`x`

,`xInd`

,`beta`

,`y`

or`pBuffer`

is invalid.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`transA`

!=[HIPSPARSE_OPERATION_NON_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141a270f0124eb0d0ac15c3e7afb18064547)or[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).
