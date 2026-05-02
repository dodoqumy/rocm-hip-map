---
title: "Sparse level 3 functions &#8212; hipSPARSE 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipSPARSE/en/latest/reference/level3.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:09:51.082284+00:00
content_hash: "a0be5114c0b3f9d5"
---

# Sparse level 3 functions[#](#sparse-level-3-functions)

This module contains all sparse level 3 routines.

The sparse level 3 routines describe operations between a matrix in sparse format and multiple vectors in dense format that can also be seen as a dense matrix.

## hipsparseXbsrmm()[#](#hipsparsexbsrmm)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSbsrmm([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transB, int mb, int n, int kb, int nnzb, const float *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const float *bsrValA, const int *bsrRowPtrA, const int *bsrColIndA, int blockDim, const float *B, int ldb, const float *beta, float *C, int ldc)[#](#_CPPv415hipsparseSbsrmm17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_t20hipsparseOperation_tiiiiPKfK19hipsparseMatDescr_tPKfPKiPKiiPKfiPKfPfi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDbsrmm([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transB, int mb, int n, int kb, int nnzb, const double *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const double *bsrValA, const int *bsrRowPtrA, const int *bsrColIndA, int blockDim, const double *B, int ldb, const double *beta, double *C, int ldc)[#](#_CPPv415hipsparseDbsrmm17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_t20hipsparseOperation_tiiiiPKdK19hipsparseMatDescr_tPKdPKiPKiiPKdiPKdPdi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCbsrmm([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transB, int mb, int n, int kb, int nnzb, const hipComplex *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipComplex *bsrValA, const int *bsrRowPtrA, const int *bsrColIndA, int blockDim, const hipComplex *B, int ldb, const hipComplex *beta, hipComplex *C, int ldc)[#](#_CPPv415hipsparseCbsrmm17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_t20hipsparseOperation_tiiiiPK10hipComplexK19hipsparseMatDescr_tPK10hipComplexPKiPKiiPK10hipComplexiPK10hipComplexP10hipComplexi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZbsrmm([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transB, int mb, int n, int kb, int nnzb, const hipDoubleComplex *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipDoubleComplex *bsrValA, const int *bsrRowPtrA, const int *bsrColIndA, int blockDim, const hipDoubleComplex *B, int ldb, const hipDoubleComplex *beta, hipDoubleComplex *C, int ldc)[#](#_CPPv415hipsparseZbsrmm17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_t20hipsparseOperation_tiiiiPK16hipDoubleComplexK19hipsparseMatDescr_tPK16hipDoubleComplexPKiPKiiPK16hipDoubleComplexiPK16hipDoubleComplexP16hipDoubleComplexi) Sparse matrix dense matrix multiplication using BSR storage format.

`hipsparseXbsrmm`

multiplies the scalar \(\alpha\) with a sparse \(m \times k\) matrix \(A\), defined in BSR storage format, and the column-oriented dense \(k \times n\) matrix \(B\) and adds the result to the column-oriented dense \(m \times n\) matrix \(C\) that is multiplied by the scalar \(\beta\), such that\[ C := \alpha \cdot op(A) \cdot op(B) + \beta \cdot C, \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if transA == HIPSPARSE_OPERATION_NON_TRANSPOSE} \\ \end{array} \right. \end{split}\]and\[\begin{split} op(B) = \left\{ \begin{array}{ll} B, & \text{if transB == HIPSPARSE_OPERATION_NON_TRANSPOSE} \\ B^T, & \text{if transB == HIPSPARSE_OPERATION_TRANSPOSE} \\ \end{array} \right. \end{split}\]and where \(k = blockDim \times kb\) and \(m = blockDim \times mb\).**Example**int main(int argc, char* argv[]) { // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // 1 2 0 3 0 0 // A = 0 4 5 0 0 0 // 0 0 0 7 8 0 // 0 0 1 2 4 1 const int blockDim = 2; const int mb = 2; const int kb = 3; const int nnzb = 4; const hipsparseDirection_t dir = HIPSPARSE_DIRECTION_ROW; int hbsrRowPtr[mb + 1] = {0, 2, 4}; int hbsrColInd[nnzb] = {0, 1, 1, 2}; float hbsrVal[nnzb * blockDim * blockDim] = {1, 2, 0, 4, 0, 3, 5, 0, 0, 7, 1, 2, 8, 0, 4, 1}; // Set dimension n of B const int n = 3; const int m = mb * blockDim; const int k = kb * blockDim; // Allocate and generate dense matrix B (k x n) float hB[k * n] = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f, 9.0f, 10.0f, 11.0f, 12.0f, 13.0f, 14.0f, 15.0f, 16.0f, 17.0f, 18.0f}; int* dbsrRowPtr = NULL; int* dbsrColInd = NULL; float* dbsrVal = NULL; HIP_CHECK(hipMalloc((void**)&dbsrRowPtr, sizeof(int) * (mb + 1))); HIP_CHECK(hipMalloc((void**)&dbsrColInd, sizeof(int) * nnzb)); HIP_CHECK(hipMalloc((void**)&dbsrVal, sizeof(float) * nnzb * blockDim * blockDim)); HIP_CHECK(hipMemcpy(dbsrRowPtr, hbsrRowPtr, sizeof(int) * (mb + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dbsrColInd, hbsrColInd, sizeof(int) * nnzb, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( dbsrVal, hbsrVal, sizeof(float) * nnzb * blockDim * blockDim, hipMemcpyHostToDevice)); // Copy B to the device float* dB; HIP_CHECK(hipMalloc((void**)&dB, sizeof(float) * k * n)); HIP_CHECK(hipMemcpy(dB, hB, sizeof(float) * k * n, hipMemcpyHostToDevice)); // alpha and beta float alpha = 1.0f; float beta = 0.0f; // Allocate memory for the resulting matrix C float* dC; HIP_CHECK(hipMalloc((void**)&dC, sizeof(float) * m * n)); // Matrix descriptor hipsparseMatDescr_t descr; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&descr)); // Perform the matrix multiplication HIPSPARSE_CHECK(hipsparseSbsrmm(handle, dir, HIPSPARSE_OPERATION_NON_TRANSPOSE, HIPSPARSE_OPERATION_NON_TRANSPOSE, mb, n, kb, nnzb, &alpha, descr, dbsrVal, dbsrRowPtr, dbsrColInd, blockDim, dB, k, &beta, dC, m)); // Copy results to host float hC[m * n]; HIP_CHECK(hipMemcpy(hC, dC, sizeof(float) * m * n, hipMemcpyDeviceToHost)); std::cout << "hC" << std::endl; for(int i = 0; i < m * n; i++) { std::cout << hC[i] << " "; } std::cout << "" << std::endl; HIP_CHECK(hipFree(dbsrRowPtr)); HIP_CHECK(hipFree(dbsrColInd)); HIP_CHECK(hipFree(dbsrVal)); HIP_CHECK(hipFree(dB)); HIP_CHECK(hipFree(dC)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**dirA**–**[in]**the storage format of the blocks. Can be[HIPSPARSE_DIRECTION_ROW](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59ae8589abecf2fbfb4b6307fd9dacd9e55)or[HIPSPARSE_DIRECTION_COLUMN](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59a32e23f292b2377f6e60bdc90274c796c).**transA**–**[in]**matrix \(A\) operation type. Currently, only[HIPSPARSE_OPERATION_NON_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141a270f0124eb0d0ac15c3e7afb18064547)is supported.**transB**–**[in]**matrix \(B\) operation type. Currently, only[HIPSPARSE_OPERATION_NON_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141a270f0124eb0d0ac15c3e7afb18064547)and[HIPSPARSE_OPERATION_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141a20e9c4bdd71ea4b509b6c0b7a495c0bf)are supported.**mb**–**[in]**number of block rows of the sparse BSR matrix \(A\).**n**–**[in]**number of columns of the dense matrix \(op(B)\) and \(C\).**kb**–**[in]**number of block columns of the sparse BSR matrix \(A\).**nnzb**–**[in]**number of non-zero blocks of the sparse BSR matrix \(A\).**alpha**–**[in]**scalar \(\alpha\).**descrA**–**[in]**descriptor of the sparse BSR matrix \(A\). Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**bsrValA**–**[in]**array of`nnzb*blockDim*blockDim`

elements of the sparse BSR matrix \(A\).**bsrRowPtrA**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix \(A\).**bsrColIndA**–**[in]**array of`nnzb`

elements containing the block column indices of the sparse BSR matrix \(A\).**blockDim**–**[in]**size of the blocks in the sparse BSR matrix.**B**–**[in]**array of dimension`ldb*n`

( \(op(B) == B\)),`ldb*k`

otherwise.**ldb**–**[in]**leading dimension of \(B\), must be at least \(\max{(1, k)}\) ( \( op(B) == B\)) where`k=blockDim*kb`

, \(\max{(1, n)}\) otherwise.**beta**–**[in]**scalar \(\beta\).**C**–**[inout]**array of dimension`ldc*n`

.**ldc**–**[in]**leading dimension of \(C\), must be at least \(\max{(1, m)}\) ( \( op(A) == A\)) where`m=blockDim*mb`

, \(\max{(1, k)}\) where`k=blockDim*kb`

otherwise.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`mb`

,`n`

,`kb`

,`nnzb`

,`ldb`

,`ldc`

,`descr`

,`alpha`

,`bsrValA`

,`bsrRowPtrA`

,`bsrColIndA`

,`B`

,`beta`

or`C`

is invalid.**HIPSPARSE_STATUS_ARCH_MISMATCH**– the device is not supported.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`transA`

!=[HIPSPARSE_OPERATION_NON_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141a270f0124eb0d0ac15c3e7afb18064547)or`transB`

==[HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141ac55e75ba3027186f1dc6164fdcb06f0e)or[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXcsrmm()[#](#hipsparsexcsrmm)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseScsrmm([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int m, int n, int k, int nnz, const float *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const float *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA, const float *B, int ldb, const float *beta, float *C, int ldc)[#](#_CPPv415hipsparseScsrmm17hipsparseHandle_t20hipsparseOperation_tiiiiPKfK19hipsparseMatDescr_tPKfPKiPKiPKfiPKfPfi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDcsrmm([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int m, int n, int k, int nnz, const double *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const double *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA, const double *B, int ldb, const double *beta, double *C, int ldc)[#](#_CPPv415hipsparseDcsrmm17hipsparseHandle_t20hipsparseOperation_tiiiiPKdK19hipsparseMatDescr_tPKdPKiPKiPKdiPKdPdi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCcsrmm([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int m, int n, int k, int nnz, const hipComplex *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipComplex *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA, const hipComplex *B, int ldb, const hipComplex *beta, hipComplex *C, int ldc)[#](#_CPPv415hipsparseCcsrmm17hipsparseHandle_t20hipsparseOperation_tiiiiPK10hipComplexK19hipsparseMatDescr_tPK10hipComplexPKiPKiPK10hipComplexiPK10hipComplexP10hipComplexi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZcsrmm([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA, int m, int n, int k, int nnz, const hipDoubleComplex *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipDoubleComplex *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA, const hipDoubleComplex *B, int ldb, const hipDoubleComplex *beta, hipDoubleComplex *C, int ldc)[#](#_CPPv415hipsparseZcsrmm17hipsparseHandle_t20hipsparseOperation_tiiiiPK16hipDoubleComplexK19hipsparseMatDescr_tPK16hipDoubleComplexPKiPKiPK16hipDoubleComplexiPK16hipDoubleComplexP16hipDoubleComplexi) Sparse matrix dense matrix multiplication using CSR storage format.

`hipsparseXcsrmm`

multiplies the scalar \(\alpha\) with a sparse \(m \times k\) matrix \(A\), defined in CSR storage format, and the column-oriented dense \(k \times n\) matrix \(B\) and adds the result to the column-oriented dense \(m \times n\) matrix \(C\) that is multiplied by the scalar \(\beta\), such that\[ C := \alpha \cdot op(A) \cdot B + \beta \cdot C, \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if transA == HIPSPARSE_OPERATION_NON_TRANSPOSE} \\ A^T, & \text{if transA == HIPSPARSE_OPERATION_TRANSPOSE} \\ A^H, & \text{if transA == HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE} \end{array} \right. \end{split}\]for(i = 0; i < ldc; ++i) { for(j = 0; j < n; ++j) { C[i][j] = beta * C[i][j]; for(k = csrRowPtr[i]; k < csrRowPtr[i + 1]; ++k) { C[i][j] += alpha * csrVal[k] * B[csrColInd[k]][j]; } } }

**Example**int main(int argc, char* argv[]) { // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // 1 2 0 3 0 0 // A = 0 4 5 0 0 0 // 0 0 0 7 8 0 // 0 0 1 2 4 1 const int m = 4; const int k = 6; const int nnz = 11; const hipsparseDirection_t dir = HIPSPARSE_DIRECTION_ROW; int hcsrRowPtr[m + 1] = {0, 3, 5, 7, 11}; int hcsrColInd[nnz] = {0, 1, 3, 1, 2, 3, 4, 2, 3, 4, 5}; float hcsrVal[nnz] = {1, 2, 3, 4, 5, 7, 8, 1, 2, 4, 1}; // Set dimension n of B const int n = 3; // Allocate and generate dense matrix B (k x n) float hB[k * n] = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f, 9.0f, 10.0f, 11.0f, 12.0f, 13.0f, 14.0f, 15.0f, 16.0f, 17.0f, 18.0f}; int* dcsrRowPtr = NULL; int* dcsrColInd = NULL; float* dcsrVal = NULL; HIP_CHECK(hipMalloc((void**)&dcsrRowPtr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&dcsrColInd, sizeof(int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcsrVal, sizeof(float) * nnz)); HIP_CHECK(hipMemcpy(dcsrRowPtr, hcsrRowPtr, sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrColInd, hcsrColInd, sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrVal, hcsrVal, sizeof(float) * nnz, hipMemcpyHostToDevice)); // Copy B to the device float* dB; HIP_CHECK(hipMalloc((void**)&dB, sizeof(float) * k * n)); HIP_CHECK(hipMemcpy(dB, hB, sizeof(float) * k * n, hipMemcpyHostToDevice)); // alpha and beta float alpha = 1.0f; float beta = 0.0f; // Allocate memory for the resulting matrix C float* dC; HIP_CHECK(hipMalloc((void**)&dC, sizeof(float) * m * n)); // Matrix descriptor hipsparseMatDescr_t descr; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&descr)); // Perform the matrix multiplication HIPSPARSE_CHECK(hipsparseScsrmm(handle, HIPSPARSE_OPERATION_NON_TRANSPOSE, m, n, k, nnz, &alpha, descr, dcsrVal, dcsrRowPtr, dcsrColInd, dB, k, &beta, dC, m)); // Copy results to host float hC[6 * 3]; HIP_CHECK(hipMemcpy(hC, dC, sizeof(float) * m * n, hipMemcpyDeviceToHost)); std::cout << "hC" << std::endl; for(int i = 0; i < m * n; i++) { std::cout << hC[i] << " "; } std::cout << "" << std::endl; HIP_CHECK(hipFree(dcsrRowPtr)); HIP_CHECK(hipFree(dcsrColInd)); HIP_CHECK(hipFree(dcsrVal)); HIP_CHECK(hipFree(dB)); HIP_CHECK(hipFree(dC)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**transA**–**[in]**matrix \(A\) operation type.**m**–**[in]**number of rows of the sparse CSR matrix \(A\).**n**–**[in]**number of columns of the dense matrix \(op(B)\) and \(C\).**k**–**[in]**number of columns of the sparse CSR matrix \(A\).**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix \(A\).**alpha**–**[in]**scalar \(\alpha\).**descrA**–**[in]**descriptor of the sparse CSR matrix \(A\). Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**csrSortedValA**–**[in]**array of`nnz`

elements of the sparse CSR matrix \(A\).**csrSortedRowPtrA**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(A\).**csrSortedColIndA**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix \(A\).**B**–**[in]**array of dimension`ldb*n`

( \(op(B) == B\)),`ldb*k`

otherwise.**ldb**–**[in]**leading dimension of \(B\), must be at least \(\max{(1, k)}\) ( \(op(B) == B\)), \(\max{(1, n)}\) otherwise.**beta**–**[in]**scalar \(\beta\).**C**–**[inout]**array of dimension`ldc*n`

.**ldc**–**[in]**leading dimension of \(C\), must be at least \(\max{(1, m)}\) ( \(op(A) == A\)), \(\max{(1, k)}\) otherwise.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`k`

,`nnz`

,`ldb`

,`ldc`

`descrA`

,`alpha`

,`csrSortedValA`

,`csrSortedRowPtrA`

,`csrSortedColIndA`

,`B`

,`beta`

or`C`

is invalid.**HIPSPARSE_STATUS_ARCH_MISMATCH**– the device is not supported.**HIPSPARSE_STATUS_NOT_SUPPORTED**–[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXcsrmm2()[#](#hipsparsexcsrmm2)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseScsrmm2([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transB, int m, int n, int k, int nnz, const float *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const float *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA, const float *B, int ldb, const float *beta, float *C, int ldc)[#](#_CPPv416hipsparseScsrmm217hipsparseHandle_t20hipsparseOperation_t20hipsparseOperation_tiiiiPKfK19hipsparseMatDescr_tPKfPKiPKiPKfiPKfPfi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDcsrmm2([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transB, int m, int n, int k, int nnz, const double *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const double *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA, const double *B, int ldb, const double *beta, double *C, int ldc)[#](#_CPPv416hipsparseDcsrmm217hipsparseHandle_t20hipsparseOperation_t20hipsparseOperation_tiiiiPKdK19hipsparseMatDescr_tPKdPKiPKiPKdiPKdPdi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCcsrmm2([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transB, int m, int n, int k, int nnz, const hipComplex *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipComplex *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA, const hipComplex *B, int ldb, const hipComplex *beta, hipComplex *C, int ldc)[#](#_CPPv416hipsparseCcsrmm217hipsparseHandle_t20hipsparseOperation_t20hipsparseOperation_tiiiiPK10hipComplexK19hipsparseMatDescr_tPK10hipComplexPKiPKiPK10hipComplexiPK10hipComplexP10hipComplexi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZcsrmm2([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transB, int m, int n, int k, int nnz, const hipDoubleComplex *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipDoubleComplex *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA, const hipDoubleComplex *B, int ldb, const hipDoubleComplex *beta, hipDoubleComplex *C, int ldc)[#](#_CPPv416hipsparseZcsrmm217hipsparseHandle_t20hipsparseOperation_t20hipsparseOperation_tiiiiPK16hipDoubleComplexK19hipsparseMatDescr_tPK16hipDoubleComplexPKiPKiPK16hipDoubleComplexiPK16hipDoubleComplexP16hipDoubleComplexi) Sparse matrix dense matrix multiplication using CSR storage format.

`hipsparseXcsrmm2`

multiplies the scalar \(\alpha\) with a sparse \(m \times k\) matrix \(A\), defined in CSR storage format, and the column-oriented dense \(k \times n\) matrix \(B\) and adds the result to the column-oriented dense \(m \times n\) matrix \(C\) that is multiplied by the scalar \(\beta\), such that\[ C := \alpha \cdot op(A) \cdot op(B) + \beta \cdot C, \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if transA == HIPSPARSE_OPERATION_NON_TRANSPOSE} \\ A^T, & \text{if transA == HIPSPARSE_OPERATION_TRANSPOSE} \\ A^H, & \text{if transA == HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE} \end{array} \right. \end{split}\]and\[\begin{split} op(B) = \left\{ \begin{array}{ll} B, & \text{if transB == HIPSPARSE_OPERATION_NON_TRANSPOSE} \\ B^T, & \text{if transB == HIPSPARSE_OPERATION_TRANSPOSE} \\ B^H, & \text{if transB == HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE} \end{array} \right. \end{split}\]for(i = 0; i < ldc; ++i) { for(j = 0; j < n; ++j) { C[i][j] = beta * C[i][j]; for(k = csrRowPtr[i]; k < csrRowPtr[i + 1]; ++k) { C[i][j] += alpha * csrVal[k] * B[csrColInd[k]][j]; } } }

Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**transA**–**[in]**matrix \(A\) operation type.**transB**–**[in]**matrix \(B\) operation type.**m**–**[in]**number of rows of the sparse CSR matrix \(A\).**n**–**[in]**number of columns of the dense matrix \(op(B)\) and \(C\).**k**–**[in]**number of columns of the sparse CSR matrix \(A\).**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix \(A\).**alpha**–**[in]**scalar \(\alpha\).**descrA**–**[in]**descriptor of the sparse CSR matrix \(A\). Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**csrSortedValA**–**[in]**array of`nnz`

elements of the sparse CSR matrix \(A\).**csrSortedRowPtrA**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(A\).**csrSortedColIndA**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix \(A\).**B**–**[in]**array of dimension`ldb*n`

( \(op(B) == B\)),`ldb*k`

otherwise.**ldb**–**[in]**leading dimension of \(B\), must be at least \(\max{(1, k)}\) ( \(op(B) == B\)), \(\max{(1, n)}\) otherwise.**beta**–**[in]**scalar \(\beta\).**C**–**[inout]**array of dimension`ldc*n`

.**ldc**–**[in]**leading dimension of \(C\), must be at least \(\max{(1, m)}\) ( \(op(A) == A\)), \(\max{(1, k)}\) otherwise.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`k`

,`nnz`

,`ldb`

,`ldc`

`descrA`

,`alpha`

,`csrSortedValA`

,`csrSortedRowPtrA`

,`csrSortedColIndA`

,`B`

,`beta`

or`C`

is invalid.**HIPSPARSE_STATUS_ARCH_MISMATCH**– the device is not supported.**HIPSPARSE_STATUS_NOT_SUPPORTED**–[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXbsrsm2_zeroPivot()[#](#hipsparsexbsrsm2-zeropivot)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseXbsrsm2_zeroPivot([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[bsrsm2Info_t](types.html#_CPPv412bsrsm2Info_t)info, int *position)[#](#_CPPv426hipsparseXbsrsm2_zeroPivot17hipsparseHandle_t12bsrsm2Info_tPi) `hipsparseXbsrsm2_zeroPivot`

returns[HIPSPARSE_STATUS_ZERO_PIVOT](types.html#hipsparse-types_8h_1aa069bec7a4f24d00dab1dc4612d4de79a88ff0f0537dfe037fcf9f99ff0cf79da), if either a structural or numerical zero has been found during[hipsparseXbsrsm2_analysis()](#hipsparse__bsrsm_8h_1aacd9b432867bd4ef875955696c57ccd4)or[hipsparseXbsrsm2_solve()](#hipsparse__bsrsm_8h_1a5103145304428e88b9ccb189c6a5a790)computation. The first zero pivot \(j\) at \(A_{j,j}\) is stored in`position`

, using same index base as the BSR matrix.`position`

can be in host or device memory. If no zero pivot has been found,`position`

is set to -1 and[HIPSPARSE_STATUS_SUCCESS](types.html#hipsparse-types_8h_1aa069bec7a4f24d00dab1dc4612d4de79a146a8a2fd27ee49132f8dcea617fc481)is returned instead.Note

`hipsparseXbsrsm2_zeroPivot`

is a blocking function. It might influence performance negatively.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**info**–**[in]**structure that holds the information collected during the analysis step.**position**–**[inout]**pointer to zero pivot \(j\), can be in host or device memory.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`info`

or`position`

is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.**HIPSPARSE_STATUS_ZERO_PIVOT**– zero pivot has been found.



## hipsparseXbsrsm2_bufferSize()[#](#hipsparsexbsrsm2-buffersize)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSbsrsm2_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transX, int mb, int nrhs, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, float *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrsm2Info_t](types.html#_CPPv412bsrsm2Info_t)info, int *pBufferSizeInBytes)[#](#_CPPv427hipsparseSbsrsm2_bufferSize17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_t20hipsparseOperation_tiiiK19hipsparseMatDescr_tPfPKiPKii12bsrsm2Info_tPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDbsrsm2_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transX, int mb, int nrhs, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, double *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrsm2Info_t](types.html#_CPPv412bsrsm2Info_t)info, int *pBufferSizeInBytes)[#](#_CPPv427hipsparseDbsrsm2_bufferSize17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_t20hipsparseOperation_tiiiK19hipsparseMatDescr_tPdPKiPKii12bsrsm2Info_tPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCbsrsm2_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transX, int mb, int nrhs, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, hipComplex *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrsm2Info_t](types.html#_CPPv412bsrsm2Info_t)info, int *pBufferSizeInBytes)[#](#_CPPv427hipsparseCbsrsm2_bufferSize17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_t20hipsparseOperation_tiiiK19hipsparseMatDescr_tP10hipComplexPKiPKii12bsrsm2Info_tPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZbsrsm2_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transX, int mb, int nrhs, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, hipDoubleComplex *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrsm2Info_t](types.html#_CPPv412bsrsm2Info_t)info, int *pBufferSizeInBytes)[#](#_CPPv427hipsparseZbsrsm2_bufferSize17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_t20hipsparseOperation_tiiiK19hipsparseMatDescr_tP16hipDoubleComplexPKiPKii12bsrsm2Info_tPi) `hipsparseXbsrsm2_buffer_size`

returns the size of the temporary storage buffer in bytes that is required by[hipsparseXbsrsm2_analysis()](#hipsparse__bsrsm_8h_1aacd9b432867bd4ef875955696c57ccd4)and[hipsparseXbsrsm2_solve()](#hipsparse__bsrsm_8h_1a5103145304428e88b9ccb189c6a5a790). The temporary storage buffer must be allocated by the user.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**dirA**–**[in]**matrix storage of BSR blocks.**transA**–**[in]**matrix \(A\) operation type.**transX**–**[in]**matrix \(X\) operation type.**mb**–**[in]**number of block rows of the sparse BSR matrix \(A\).**nrhs**–**[in]**number of columns of the dense matrix \(op(X)\).**nnzb**–**[in]**number of non-zero blocks of the sparse BSR matrix \(A\).**descrA**–**[in]**descriptor of the sparse BSR matrix \(A\).**bsrSortedValA**–**[in]**array of`nnzb`

blocks of the sparse BSR matrix.**bsrSortedRowPtrA**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix.**bsrSortedColIndA**–**[in]**array of`nnzb`

containing the block column indices of the sparse BSR matrix.**blockDim**–**[in]**block dimension of the sparse BSR matrix.**info**–**[in]**structure that holds the information collected during the analysis step.**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer required by[hipsparseXbsrsm2_analysis()](#hipsparse__bsrsm_8h_1aacd9b432867bd4ef875955696c57ccd4)and[hipsparseXbsrsm2_solve()](#hipsparse__bsrsm_8h_1a5103145304428e88b9ccb189c6a5a790).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`mb`

,`nrhs`

,`nnzb`

,`blockDim`

,`descrA`

,`bsrSortedValA`

,`bsrSortedRowPtrA`

,`bsrSortedColIndA`

,`info`

or`pBufferSizeInBytes`

is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`transA`

==[HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141ac55e75ba3027186f1dc6164fdcb06f0e),`transX`

==[HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141ac55e75ba3027186f1dc6164fdcb06f0e)or[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXbsrsm2_analysis()[#](#hipsparsexbsrsm2-analysis)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSbsrsm2_analysis([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transX, int mb, int nrhs, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const float *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrsm2Info_t](types.html#_CPPv412bsrsm2Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv425hipsparseSbsrsm2_analysis17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_t20hipsparseOperation_tiiiK19hipsparseMatDescr_tPKfPKiPKii12bsrsm2Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDbsrsm2_analysis([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transX, int mb, int nrhs, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const double *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrsm2Info_t](types.html#_CPPv412bsrsm2Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv425hipsparseDbsrsm2_analysis17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_t20hipsparseOperation_tiiiK19hipsparseMatDescr_tPKdPKiPKii12bsrsm2Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCbsrsm2_analysis([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transX, int mb, int nrhs, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipComplex *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrsm2Info_t](types.html#_CPPv412bsrsm2Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv425hipsparseCbsrsm2_analysis17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_t20hipsparseOperation_tiiiK19hipsparseMatDescr_tPK10hipComplexPKiPKii12bsrsm2Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZbsrsm2_analysis([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transX, int mb, int nrhs, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipDoubleComplex *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrsm2Info_t](types.html#_CPPv412bsrsm2Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv425hipsparseZbsrsm2_analysis17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_t20hipsparseOperation_tiiiK19hipsparseMatDescr_tPK16hipDoubleComplexPKiPKii12bsrsm2Info_t22hipsparseSolvePolicy_tPv) Sparse triangular system solve using BSR storage format.

`hipsparseXbsrsm2_analysis`

performs the analysis step for[hipsparseXbsrsm2_solve()](#hipsparse__bsrsm_8h_1a5103145304428e88b9ccb189c6a5a790). It is expected that this function will be executed only once for a given matrix and particular operation type.Note

If the matrix sparsity pattern changes, the gathered information will become invalid.

Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**dirA**–**[in]**matrix storage of BSR blocks.**transA**–**[in]**matrix \(A\) operation type.**transX**–**[in]**matrix \(X\) operation type.**mb**–**[in]**number of block rows of the sparse BSR matrix \(A\).**nrhs**–**[in]**number of columns of the dense matrix \(op(X)\).**nnzb**–**[in]**number of non-zero blocks of the sparse BSR matrix \(A\).**descrA**–**[in]**descriptor of the sparse BSR matrix \(A\).**bsrSortedValA**–**[in]**array of`nnzb`

blocks of the sparse BSR matrix \(A\).**bsrSortedRowPtrA**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix \(A\).**bsrSortedColIndA**–**[in]**array of`nnzb`

containing the block column indices of the sparse BSR matrix \(A\).**blockDim**–**[in]**block dimension of the sparse BSR matrix \(A\).**info**–**[out]**structure that holds the information collected during the analysis step.**policy**–**[in]**[HIPSPARSE_SOLVE_POLICY_NO_LEVEL](types.html#hipsparse-types_8h_1a0d98e490c94d4facc231db60baf1c3b3ac5830aa96848e832b3b375ad08abdb09)or[HIPSPARSE_SOLVE_POLICY_USE_LEVEL](types.html#hipsparse-types_8h_1a0d98e490c94d4facc231db60baf1c3b3a934309d6656638e375f0759b89fd81b5).**pBuffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`mb`

,`nrhs`

,`nnzb`

or`blockDim`

,`descrA`

,`bsrSortedValA`

,`bsrSortedRowPtrA`

,`bsrSortedColIndA`

,`info`

or`pBuffer`

is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`transA`

==[HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141ac55e75ba3027186f1dc6164fdcb06f0e),`transX`

==[HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141ac55e75ba3027186f1dc6164fdcb06f0e)or[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXbsrsm2_solve()[#](#hipsparsexbsrsm2-solve)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSbsrsm2_solve([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transX, int mb, int nrhs, int nnzb, const float *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const float *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrsm2Info_t](types.html#_CPPv412bsrsm2Info_t)info, const float *B, int ldb, float *X, int ldx,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv422hipsparseSbsrsm2_solve17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_t20hipsparseOperation_tiiiPKfK19hipsparseMatDescr_tPKfPKiPKii12bsrsm2Info_tPKfiPfi22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDbsrsm2_solve([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transX, int mb, int nrhs, int nnzb, const double *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const double *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrsm2Info_t](types.html#_CPPv412bsrsm2Info_t)info, const double *B, int ldb, double *X, int ldx,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv422hipsparseDbsrsm2_solve17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_t20hipsparseOperation_tiiiPKdK19hipsparseMatDescr_tPKdPKiPKii12bsrsm2Info_tPKdiPdi22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCbsrsm2_solve([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transX, int mb, int nrhs, int nnzb, const hipComplex *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipComplex *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrsm2Info_t](types.html#_CPPv412bsrsm2Info_t)info, const hipComplex *B, int ldb, hipComplex *X, int ldx,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv422hipsparseCbsrsm2_solve17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_t20hipsparseOperation_tiiiPK10hipComplexK19hipsparseMatDescr_tPK10hipComplexPKiPKii12bsrsm2Info_tPK10hipComplexiP10hipComplexi22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZbsrsm2_solve([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transX, int mb, int nrhs, int nnzb, const hipDoubleComplex *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipDoubleComplex *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrsm2Info_t](types.html#_CPPv412bsrsm2Info_t)info, const hipDoubleComplex *B, int ldb, hipDoubleComplex *X, int ldx,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv422hipsparseZbsrsm2_solve17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_t20hipsparseOperation_tiiiPK16hipDoubleComplexK19hipsparseMatDescr_tPK16hipDoubleComplexPKiPKii12bsrsm2Info_tPK16hipDoubleComplexiP16hipDoubleComplexi22hipsparseSolvePolicy_tPv) Sparse triangular system solve using BSR storage format.

`hipsparseXbsrsm2_solve`

solves a sparse triangular linear system of a sparse \(m \times m\) matrix, defined in BSR storage format, a column-oriented dense solution matrix \(X\) and the column-oriented dense right-hand side matrix \(B\) that is multiplied by \(\alpha\), such that\[ op(A) \cdot op(X) = \alpha \cdot op(B), \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if transA == HIPSPARSE_OPERATION_NON_TRANSPOSE} \\ A^T, & \text{if transA == HIPSPARSE_OPERATION_TRANSPOSE} \\ A^H, & \text{if transA == HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE} \end{array} \right. \end{split}\],\[\begin{split} op(B) = \left\{ \begin{array}{ll} B, & \text{if transX == HIPSPARSE_OPERATION_NON_TRANSPOSE} \\ B^T, & \text{if transX == HIPSPARSE_OPERATION_TRANSPOSE} \\ B^H, & \text{if transX == HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE} \end{array} \right. \end{split}\]and\[\begin{split} op(X) = \left\{ \begin{array}{ll} X, & \text{if transX == HIPSPARSE_OPERATION_NON_TRANSPOSE} \\ X^T, & \text{if transX == HIPSPARSE_OPERATION_TRANSPOSE} \\ X^H, & \text{if transX == HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE} \end{array} \right. \end{split}\]and where \(m = blockDim \times mb\).Note that as indicated above, the operation type of both \(op(B)\) and \(op(X)\) is specified by the

`transX`

parameter and that the operation type of \(B\) and \(X\) must match. For example, if \(op(B)=B\) then \(op(X)=X\). Likewise, if \(op(B)=B^T\) then \(op(X)=X^T\).Given that the sparse matrix \(A\) is a square matrix, its size is \(m \times m\) regardless of whether \(A\) is transposed or not. The size of the column-oriented dense matrices \(B\) and \(X\) have size that depends on the value of

`transX:`

\[\begin{split} op(B) = \left\{ \begin{array}{ll} ldb \times nrhs, \text{ } ldb \ge m, & \text{if transX == HIPSPARSE_OPERATION_NON_TRANSPOSE} \\ ldb \times m, \text{ } ldb \ge nrhs, & \text{if transX == HIPSPARSE_OPERATION_TRANSPOSE} \\ ldb \times m, \text{ } ldb \ge nrhs, & \text{if transX == HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE} \end{array} \right. \end{split}\]and\[\begin{split} op(X) = \left\{ \begin{array}{ll} ldb \times nrhs, \text{ } ldb \ge m, & \text{if transX == HIPSPARSE_OPERATION_NON_TRANSPOSE} \\ ldb \times m, \text{ } ldb \ge nrhs, & \text{if transX == HIPSPARSE_OPERATION_TRANSPOSE} \\ ldb \times m, \text{ } ldb \ge nrhs, & \text{if transX == HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE} \end{array} \right. \end{split}\]`hipsparseXbsrsm2_solve`

requires a user allocated temporary buffer. Its size is returned by[hipsparseXbsrsm2_bufferSize()](#hipsparse__bsrsm_8h_1afc00f788090e6c16c1e790b9683df3b8). The size of the required buffer is larger when`transA`

equals[HIPSPARSE_OPERATION_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141a20e9c4bdd71ea4b509b6c0b7a495c0bf)or[HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141ac55e75ba3027186f1dc6164fdcb06f0e)and when`transX`

is[HIPSPARSE_OPERATION_NON_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141a270f0124eb0d0ac15c3e7afb18064547). The subsequent solve will also be faster when \(A\) is non-transposed and \(B\) is transposed (or conjugate transposed). For example, instead of solving:\[\begin{split} \left[ \begin{array}{c | c} \begin{array}{c c} a_{00} & a_{01} \\ a_{10} & a_{11} \end{array} & \begin{array}{c c} 0 & 0 \\ 0 & 0 \end{array} \\ \hline \begin{array}{c c} a_{20} & a_{21} \\ a_{30} & a_{31} \end{array} & \begin{array}{c c} a_{22} & a_{23} \\ a_{32} & a_{33} \end{array} \\ \end{array} \right] \cdot \begin{bmatrix} x_{00} & x_{01} \\ x_{10} & x_{11} \\ x_{20} & x_{21} \\ x_{30} & x_{31} \\ \end{bmatrix} = \begin{bmatrix} b_{00} & b_{01} \\ b_{10} & b_{11} \\ b_{20} & b_{21} \\ b_{30} & b_{31} \\ \end{bmatrix} \end{split}\]Consider solving:

\[\begin{split} \left[ \begin{array}{c | c} \begin{array}{c c} a_{00} & a_{01} \\ a_{10} & a_{11} \end{array} & \begin{array}{c c} 0 & 0 \\ 0 & 0 \end{array} \\ \hline \begin{array}{c c} a_{20} & a_{21} \\ a_{30} & a_{31} \end{array} & \begin{array}{c c} a_{22} & a_{23} \\ a_{32} & a_{33} \end{array} \\ \end{array} \right] \cdot \begin{bmatrix} x_{00} & x_{10} & x_{20} & x_{30} \\ x_{01} & x_{11} & x_{21} & x_{31} \end{bmatrix}^{T} = \begin{bmatrix} b_{00} & b_{10} & b_{20} & b_{30} \\ b_{01} & b_{11} & b_{21} & b_{31} \end{bmatrix}^{T} \end{split}\]Once the temporary storage buffer has been allocated, analysis meta data is required. It can be obtained by hipsparseSbsrsm2_analysis “hipsparseXbsrsm2_analysis()”. The triangular solve is completed by calling

`hipsparseXbsrsm2_solve`

and once all solves are performed, the temporary storage buffer allocated by the user can be freed.Solving a triangular system involves inverting the diagonal blocks. This means that if the sparse matrix is missing the diagonal block (referred to as a structural zero) or the diagonal block is not invertible (referred to as a numerical zero) then a solution is not possible.

`hipsparseXbsrsm2_solve`

tracks the location of the first zero pivot (either numerical or structural zero). The zero pivot status can be checked calling[hipsparseXbsrsm2_zeroPivot()](#hipsparse__bsrsm_8h_1a6d4fd566a8037938f5d3929208b848cd). If[hipsparseXbsrsm2_zeroPivot()](#hipsparse__bsrsm_8h_1a6d4fd566a8037938f5d3929208b848cd)returns[HIPSPARSE_STATUS_SUCCESS](types.html#hipsparse-types_8h_1aa069bec7a4f24d00dab1dc4612d4de79a146a8a2fd27ee49132f8dcea617fc481), then no zero pivot was found and therefore the matrix does not have a structural or numerical zero.The user can specify that the sparse matrix should be interpreted as having identity blocks on the diagonal by setting the diagonal type on the descriptor

`descrA`

to[HIPSPARSE_DIAG_TYPE_UNIT](types.html#hipsparse-types_8h_1a79e036b6c0680cb37e2aa53d3542a054a532a9a4a4eaf63a967bfaac7f9936b39)using[hipsparseSetMatDiagType](auxiliary.html#hipsparse-auxiliary_8h_1aec6fa039793196011f15cfb0b21c2b59). If[hipsparseDiagType_t](types.html#hipsparse-types_8h_1a79e036b6c0680cb37e2aa53d3542a054)==[HIPSPARSE_DIAG_TYPE_UNIT](types.html#hipsparse-types_8h_1a79e036b6c0680cb37e2aa53d3542a054a532a9a4a4eaf63a967bfaac7f9936b39), no zero pivot will be reported, even if the diagonal block \(A_{j,j}\) for some \(j\) is not invertible.The sparse CSR matrix passed to

`hipsparseXbsrsm2_solve`

does not actually have to be a triangular matrix. Instead the triangular upper or lower part of the sparse matrix is solved based on[hipsparseFillMode_t](types.html#hipsparse-types_8h_1ace47655e52ed1bb17309eda331c44332)set on the descriptor`descrA`

. If the fill mode is set to[HIPSPARSE_FILL_MODE_LOWER](types.html#hipsparse-types_8h_1ace47655e52ed1bb17309eda331c44332a470abb0661ab8951449efa6988ed49ef), then the lower triangular matrix is solved. If the fill mode is set to[HIPSPARSE_FILL_MODE_UPPER](types.html#hipsparse-types_8h_1ace47655e52ed1bb17309eda331c44332ac5c8ccc62dfff77c56c8480c24ed6b3b)then the upper triangular matrix is solved.**Example**int main(int argc, char* argv[]) { // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // A = ( 1.0 0.0 0.0 0.0 ) // ( 2.0 3.0 0.0 0.0 ) // ( 4.0 5.0 6.0 0.0 ) // ( 7.0 0.0 8.0 9.0 ) // // with bsr_dim = 2 // // ------------------- // = | 1.0 0.0 | 0.0 0.0 | // | 2.0 3.0 | 0.0 0.0 | // ------------------- // | 4.0 5.0 | 6.0 0.0 | // | 7.0 0.0 | 8.0 9.0 | // ------------------- // Number of rows and columns const int m = 4; // Number of block rows and block columns const int mb = 2; const int nb = 2; // BSR block dimension const int bsr_dim = 2; // Number of right-hand-sides const int nrhs = 4; // Number of non-zero blocks const int nnzb = 3; // BSR row pointers int hbsrRowPtr[mb + 1] = {0, 1, 3}; // BSR column indices int hbsrColInd[nnzb] = {0, 0, 1}; // BSR values double hbsrVal[nnzb * bsr_dim * bsr_dim] = {1.0, 2.0, 0.0, 3.0, 4.0, 7.0, 5.0, 0.0, 6.0, 8.0, 0.0, 9.0}; // Storage scheme of the BSR blocks hipsparseDirection_t dir = HIPSPARSE_DIRECTION_COLUMN; // Transposition of the matrix and rhs matrix hipsparseOperation_t transA = HIPSPARSE_OPERATION_NON_TRANSPOSE; hipsparseOperation_t transX = HIPSPARSE_OPERATION_NON_TRANSPOSE; // Solve policy hipsparseSolvePolicy_t solve_policy = HIPSPARSE_SOLVE_POLICY_NO_LEVEL; // Scalar alpha and beta double alpha = 1.0; // rhs and solution matrix const int ldb = nb * bsr_dim; const int ldx = mb * bsr_dim; double hB[ldb * nrhs] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}; double hX[ldx * nrhs]; // Offload data to device int* dbsrRowPtr; int* dbsrColInd; double* dbsrVal; double* dB; double* dX; HIP_CHECK(hipMalloc((void**)&dbsrRowPtr, sizeof(int) * (mb + 1))); HIP_CHECK(hipMalloc((void**)&dbsrColInd, sizeof(int) * nnzb)); HIP_CHECK(hipMalloc((void**)&dbsrVal, sizeof(double) * nnzb * bsr_dim * bsr_dim)); HIP_CHECK(hipMalloc((void**)&dB, sizeof(double) * nb * bsr_dim * nrhs)); HIP_CHECK(hipMalloc((void**)&dX, sizeof(double) * mb * bsr_dim * nrhs)); HIP_CHECK(hipMemcpy(dbsrRowPtr, hbsrRowPtr, sizeof(int) * (mb + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dbsrColInd, hbsrColInd, sizeof(int) * nnzb, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( dbsrVal, hbsrVal, sizeof(double) * nnzb * bsr_dim * bsr_dim, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dB, hB, sizeof(double) * nb * bsr_dim * nrhs, hipMemcpyHostToDevice)); // Matrix descriptor hipsparseMatDescr_t descr; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&descr)); // Matrix fill mode HIPSPARSE_CHECK(hipsparseSetMatFillMode(descr, HIPSPARSE_FILL_MODE_LOWER)); // Matrix diagonal type HIPSPARSE_CHECK(hipsparseSetMatDiagType(descr, HIPSPARSE_DIAG_TYPE_NON_UNIT)); // Matrix info structure bsrsm2Info_t info; HIPSPARSE_CHECK(hipsparseCreateBsrsm2Info(&info)); // Obtain required buffer size int buffer_size; HIPSPARSE_CHECK(hipsparseDbsrsm2_bufferSize(handle, dir, transA, transX, mb, nrhs, nnzb, descr, dbsrVal, dbsrRowPtr, dbsrColInd, bsr_dim, info, &buffer_size)); // Allocate temporary buffer void* dbuffer; HIP_CHECK(hipMalloc(&dbuffer, buffer_size)); // Perform analysis step HIPSPARSE_CHECK(hipsparseDbsrsm2_analysis(handle, dir, transA, transX, mb, nrhs, nnzb, descr, dbsrVal, dbsrRowPtr, dbsrColInd, bsr_dim, info, solve_policy, dbuffer)); // Call dbsrsm to perform lower triangular solve LX = B HIPSPARSE_CHECK(hipsparseDbsrsm2_solve(handle, dir, transA, transX, mb, nrhs, nnzb, &alpha, descr, dbsrVal, dbsrRowPtr, dbsrColInd, bsr_dim, info, dB, ldb, dX, ldx, solve_policy, dbuffer)); // Check for zero pivots int pivot; hipsparseStatus_t status = hipsparseXbsrsm2_zeroPivot(handle, info, &pivot); if(status == HIPSPARSE_STATUS_ZERO_PIVOT) { std::cout << "Found zero pivot in matrix row " << pivot << std::endl; } // Copy result back to host HIP_CHECK(hipMemcpy(hX, dX, sizeof(double) * mb * bsr_dim * nrhs, hipMemcpyDeviceToHost)); std::cout << "hX" << std::endl; for(int i = 0; i < ldx * nrhs; i++) { std::cout << hX[i] << " "; } std::cout << "" << std::endl; // Clear hipSPARSE HIPSPARSE_CHECK(hipsparseDestroyBsrsm2Info(info)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(descr)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); // Clear device memory HIP_CHECK(hipFree(dbsrRowPtr)); HIP_CHECK(hipFree(dbsrColInd)); HIP_CHECK(hipFree(dbsrVal)); HIP_CHECK(hipFree(dB)); HIP_CHECK(hipFree(dX)); HIP_CHECK(hipFree(dbuffer)); return 0; }


Note

The sparse BSR matrix has to be sorted.

Note

Operation type of B and X must match, if \(op(B)=B, op(X)=X\).

Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

Currently, only

`transA`

!=[HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141ac55e75ba3027186f1dc6164fdcb06f0e)and`transX`

!=[HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141ac55e75ba3027186f1dc6164fdcb06f0e)is supported.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**dirA**–**[in]**matrix storage of BSR blocks.**transA**–**[in]**matrix \(A\) operation type.**transX**–**[in]**matrix \(X\) operation type.**mb**–**[in]**number of block rows of the sparse BSR matrix \(A\).**nrhs**–**[in]**number of columns of the dense matrix \(op(X)\).**nnzb**–**[in]**number of non-zero blocks of the sparse BSR matrix \(A\).**alpha**–**[in]**scalar \(\alpha\).**descrA**–**[in]**descriptor of the sparse BSR matrix \(A\).**bsrSortedValA**–**[in]**array of`nnzb`

blocks of the sparse BSR matrix.**bsrSortedRowPtrA**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix.**bsrSortedColIndA**–**[in]**array of`nnzb`

containing the block column indices of the sparse BSR matrix.**blockDim**–**[in]**block dimension of the sparse BSR matrix.**info**–**[in]**structure that holds the information collected during the analysis step.**B**–**[in]**rhs matrix B with leading dimension`ldb`

.**ldb**–**[in]**leading dimension of rhs matrix \(B\).**X**–**[out]**solution matrix X with leading dimension`ldx`

.**ldx**–**[in]**leading dimension of solution matrix \(X\).**policy**–**[in]**[HIPSPARSE_SOLVE_POLICY_NO_LEVEL](types.html#hipsparse-types_8h_1a0d98e490c94d4facc231db60baf1c3b3ac5830aa96848e832b3b375ad08abdb09)or[HIPSPARSE_SOLVE_POLICY_USE_LEVEL](types.html#hipsparse-types_8h_1a0d98e490c94d4facc231db60baf1c3b3a934309d6656638e375f0759b89fd81b5).**pBuffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`mb`

,`nrhs`

,`nnzb`

,`blockDim`

,`alpha`

,`descrA`

,`bsrSortedValA`

,`bsrSortedRowPtrA`

,`bsrSortedColIndA`

,`B`

,`X`

`info`

or`pBuffer`

is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`transA`

==[HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141ac55e75ba3027186f1dc6164fdcb06f0e),`transX`

==[HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141ac55e75ba3027186f1dc6164fdcb06f0e)or[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXcsrsm2_zeroPivot()[#](#hipsparsexcsrsm2-zeropivot)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseXcsrsm2_zeroPivot([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[csrsm2Info_t](types.html#_CPPv412csrsm2Info_t)info, int *position)[#](#_CPPv426hipsparseXcsrsm2_zeroPivot17hipsparseHandle_t12csrsm2Info_tPi) `hipsparseXcsrsm2_zeroPivot`

returns[HIPSPARSE_STATUS_ZERO_PIVOT](types.html#hipsparse-types_8h_1aa069bec7a4f24d00dab1dc4612d4de79a88ff0f0537dfe037fcf9f99ff0cf79da), if either a structural or numerical zero has been found during[hipsparseXcsrsm2_analysis()](#hipsparse__csrsm_8h_1aec706e7d801804490c7609b6796ddf0f)or[hipsparseXcsrsm2_solve()](#hipsparse__csrsm_8h_1a410914eb84ccae282c09b6022351422a)computation. The first zero pivot \(j\) at \(A_{j,j}\) is stored in`position`

, using same index base as the CSR matrix.`position`

can be in host or device memory. If no zero pivot has been found,`position`

is set to -1 and[HIPSPARSE_STATUS_SUCCESS](types.html#hipsparse-types_8h_1aa069bec7a4f24d00dab1dc4612d4de79a146a8a2fd27ee49132f8dcea617fc481)is returned instead.Note

`hipsparseXcsrsm2_zeroPivot`

is a blocking function. It might influence performance negatively.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**info**–**[in]**structure that holds the information collected during the analysis step.**position**–**[inout]**pointer to zero pivot \(j\), can be in host or device memory.

- Return values:
**HIPSPARSE_STATUS_SUCCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`info`

or`position`

is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.**HIPSPARSE_STATUS_ZERO_PIVOT**– zero pivot has been found.



## hipsparseXcsrsm2_bufferSizeExt()[#](#hipsparsexcsrsm2-buffersizeext)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseScsrsm2_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int algo,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transB, int m, int nrhs, int nnz, const float *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const float *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA, const float *B, int ldb,[csrsm2Info_t](types.html#_CPPv412csrsm2Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, size_t *pBufferSizeInBytes)[#](#_CPPv430hipsparseScsrsm2_bufferSizeExt17hipsparseHandle_ti20hipsparseOperation_t20hipsparseOperation_tiiiPKfK19hipsparseMatDescr_tPKfPKiPKiPKfi12csrsm2Info_t22hipsparseSolvePolicy_tP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDcsrsm2_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int algo,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transB, int m, int nrhs, int nnz, const double *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const double *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA, const double *B, int ldb,[csrsm2Info_t](types.html#_CPPv412csrsm2Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, size_t *pBufferSizeInBytes)[#](#_CPPv430hipsparseDcsrsm2_bufferSizeExt17hipsparseHandle_ti20hipsparseOperation_t20hipsparseOperation_tiiiPKdK19hipsparseMatDescr_tPKdPKiPKiPKdi12csrsm2Info_t22hipsparseSolvePolicy_tP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCcsrsm2_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int algo,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transB, int m, int nrhs, int nnz, const hipComplex *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipComplex *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA, const hipComplex *B, int ldb,[csrsm2Info_t](types.html#_CPPv412csrsm2Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, size_t *pBufferSizeInBytes)[#](#_CPPv430hipsparseCcsrsm2_bufferSizeExt17hipsparseHandle_ti20hipsparseOperation_t20hipsparseOperation_tiiiPK10hipComplexK19hipsparseMatDescr_tPK10hipComplexPKiPKiPK10hipComplexi12csrsm2Info_t22hipsparseSolvePolicy_tP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZcsrsm2_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int algo,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transB, int m, int nrhs, int nnz, const hipDoubleComplex *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipDoubleComplex *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA, const hipDoubleComplex *B, int ldb,[csrsm2Info_t](types.html#_CPPv412csrsm2Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, size_t *pBufferSizeInBytes)[#](#_CPPv430hipsparseZcsrsm2_bufferSizeExt17hipsparseHandle_ti20hipsparseOperation_t20hipsparseOperation_tiiiPK16hipDoubleComplexK19hipsparseMatDescr_tPK16hipDoubleComplexPKiPKiPK16hipDoubleComplexi12csrsm2Info_t22hipsparseSolvePolicy_tP6size_t) `hipsparseXcsrsm2_bufferSizeExt`

returns the size of the temporary storage buffer in bytes that is required by[hipsparseXcsrsm2_analysis()](#hipsparse__csrsm_8h_1aec706e7d801804490c7609b6796ddf0f)and[hipsparseXcsrsm2_solve()](#hipsparse__csrsm_8h_1a410914eb84ccae282c09b6022351422a). The temporary storage buffer must be allocated by the user.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**algo**–**[in]**algorithm to use.**transA**–**[in]**matrix \(A\) operation type.**transB**–**[in]**matrix \(B\) operation type.**m**–**[in]**number of rows of the sparse CSR matrix \(A\).**nrhs**–**[in]**number of columns of the dense matrix \(op(B)\).**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix \(A\).**alpha**–**[in]**scalar \(\alpha\).**descrA**–**[in]**descriptor of the sparse CSR matrix \(A\).**csrSortedValA**–**[in]**array of`nnz`

elements of the sparse CSR matrix \(A\).**csrSortedRowPtrA**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(A\).**csrSortedColIndA**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix \(A\).**B**–**[in]**array of`m`

\(\times\)`nrhs`

elements of the rhs matrix \(B\).**ldb**–**[in]**leading dimension of rhs matrix \(B\).**info**–**[in]**structure that holds the information collected during the analysis step.**policy**–**[in]**[HIPSPARSE_SOLVE_POLICY_NO_LEVEL](types.html#hipsparse-types_8h_1a0d98e490c94d4facc231db60baf1c3b3ac5830aa96848e832b3b375ad08abdb09)or[HIPSPARSE_SOLVE_POLICY_USE_LEVEL](types.html#hipsparse-types_8h_1a0d98e490c94d4facc231db60baf1c3b3a934309d6656638e375f0759b89fd81b5).**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer required by[hipsparseXcsrsm2_analysis()](#hipsparse__csrsm_8h_1aec706e7d801804490c7609b6796ddf0f)and[hipsparseXcsrsm2_solve()](#hipsparse__csrsm_8h_1a410914eb84ccae282c09b6022351422a).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`nrhs`

,`nnz`

,`alpha`

,`descrA`

,`csrSortedValA`

,`csrSortedRowPtrA`

,`csrSortedColIndA`

,`B`

,`info`

or`pBufferSizeInBytes`

is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`transA`

==[HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141ac55e75ba3027186f1dc6164fdcb06f0e),`transB`

==[HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141ac55e75ba3027186f1dc6164fdcb06f0e)or[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXcsrsm2_analysis()[#](#hipsparsexcsrsm2-analysis)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseScsrsm2_analysis([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int algo,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transB, int m, int nrhs, int nnz, const float *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const float *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA, const float *B, int ldb,[csrsm2Info_t](types.html#_CPPv412csrsm2Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv425hipsparseScsrsm2_analysis17hipsparseHandle_ti20hipsparseOperation_t20hipsparseOperation_tiiiPKfK19hipsparseMatDescr_tPKfPKiPKiPKfi12csrsm2Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDcsrsm2_analysis([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int algo,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transB, int m, int nrhs, int nnz, const double *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const double *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA, const double *B, int ldb,[csrsm2Info_t](types.html#_CPPv412csrsm2Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv425hipsparseDcsrsm2_analysis17hipsparseHandle_ti20hipsparseOperation_t20hipsparseOperation_tiiiPKdK19hipsparseMatDescr_tPKdPKiPKiPKdi12csrsm2Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCcsrsm2_analysis([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int algo,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transB, int m, int nrhs, int nnz, const hipComplex *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipComplex *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA, const hipComplex *B, int ldb,[csrsm2Info_t](types.html#_CPPv412csrsm2Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv425hipsparseCcsrsm2_analysis17hipsparseHandle_ti20hipsparseOperation_t20hipsparseOperation_tiiiPK10hipComplexK19hipsparseMatDescr_tPK10hipComplexPKiPKiPK10hipComplexi12csrsm2Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZcsrsm2_analysis([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int algo,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transB, int m, int nrhs, int nnz, const hipDoubleComplex *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipDoubleComplex *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA, const hipDoubleComplex *B, int ldb,[csrsm2Info_t](types.html#_CPPv412csrsm2Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv425hipsparseZcsrsm2_analysis17hipsparseHandle_ti20hipsparseOperation_t20hipsparseOperation_tiiiPK16hipDoubleComplexK19hipsparseMatDescr_tPK16hipDoubleComplexPKiPKiPK16hipDoubleComplexi12csrsm2Info_t22hipsparseSolvePolicy_tPv) `hipsparseXcsrsm2_analysis`

performs the analysis step for[hipsparseXcsrsm2_solve()](#hipsparse__csrsm_8h_1a410914eb84ccae282c09b6022351422a). It is expected that this function will be executed only once for a given matrix and particular operation type.Note

If the matrix sparsity pattern changes, the gathered information will become invalid.

Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**algo**–**[in]**algorithm to use.**transA**–**[in]**matrix \(A\) operation type.**transB**–**[in]**matrix \(B\) operation type.**m**–**[in]**number of rows of the sparse CSR matrix \(A\).**nrhs**–**[in]**number of columns of the dense matrix \(op(B)\).**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix \(A\).**alpha**–**[in]**scalar \(\alpha\).**descrA**–**[in]**descriptor of the sparse CSR matrix \(A\).**csrSortedValA**–**[in]**array of`nnz`

elements of the sparse CSR matrix \(A\).**csrSortedRowPtrA**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(A\).**csrSortedColIndA**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix \(A\).**B**–**[in]**array of`m`

\(\times\)`nrhs`

elements of the rhs matrix \(B\).**ldb**–**[in]**leading dimension of rhs matrix \(B\).**info**–**[out]**structure that holds the information collected during the analysis step.**policy**–**[in]**[HIPSPARSE_SOLVE_POLICY_NO_LEVEL](types.html#hipsparse-types_8h_1a0d98e490c94d4facc231db60baf1c3b3ac5830aa96848e832b3b375ad08abdb09)or[HIPSPARSE_SOLVE_POLICY_USE_LEVEL](types.html#hipsparse-types_8h_1a0d98e490c94d4facc231db60baf1c3b3a934309d6656638e375f0759b89fd81b5).**pBuffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`nrhs`

,`nnz`

,`alpha`

,`descrA`

,`csrSortedValA`

,`csrSortedRowPtrA`

,`csrSortedColIndA`

,`B`

,`info`

or`pBuffer`

is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`transA`

==[HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141ac55e75ba3027186f1dc6164fdcb06f0e),`transB`

==[HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141ac55e75ba3027186f1dc6164fdcb06f0e)or[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXcsrsm2_solve()[#](#hipsparsexcsrsm2-solve)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseScsrsm2_solve([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int algo,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transB, int m, int nrhs, int nnz, const float *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const float *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA, float *B, int ldb,[csrsm2Info_t](types.html#_CPPv412csrsm2Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv422hipsparseScsrsm2_solve17hipsparseHandle_ti20hipsparseOperation_t20hipsparseOperation_tiiiPKfK19hipsparseMatDescr_tPKfPKiPKiPfi12csrsm2Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDcsrsm2_solve([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int algo,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transB, int m, int nrhs, int nnz, const double *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const double *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA, double *B, int ldb,[csrsm2Info_t](types.html#_CPPv412csrsm2Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv422hipsparseDcsrsm2_solve17hipsparseHandle_ti20hipsparseOperation_t20hipsparseOperation_tiiiPKdK19hipsparseMatDescr_tPKdPKiPKiPdi12csrsm2Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCcsrsm2_solve([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int algo,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transB, int m, int nrhs, int nnz, const hipComplex *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipComplex *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA, hipComplex *B, int ldb,[csrsm2Info_t](types.html#_CPPv412csrsm2Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv422hipsparseCcsrsm2_solve17hipsparseHandle_ti20hipsparseOperation_t20hipsparseOperation_tiiiPK10hipComplexK19hipsparseMatDescr_tPK10hipComplexPKiPKiP10hipComplexi12csrsm2Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZcsrsm2_solve([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int algo,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transB, int m, int nrhs, int nnz, const hipDoubleComplex *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipDoubleComplex *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA, hipDoubleComplex *B, int ldb,[csrsm2Info_t](types.html#_CPPv412csrsm2Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv422hipsparseZcsrsm2_solve17hipsparseHandle_ti20hipsparseOperation_t20hipsparseOperation_tiiiPK16hipDoubleComplexK19hipsparseMatDescr_tPK16hipDoubleComplexPKiPKiP16hipDoubleComplexi12csrsm2Info_t22hipsparseSolvePolicy_tPv) Sparse triangular system solve using CSR storage format.

`hipsparseXcsrsm2_solve`

solves a sparse triangular linear system of a sparse \(m \times m\) matrix, defined in CSR storage format, a column-oriented dense solution matrix \(X\) and the column-oriented dense right-hand side matrix \(B\) that is multiplied by \(\alpha\), such that\[ op(A) \cdot op(X) = \alpha \cdot op(B), \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if transA == HIPSPARSE_OPERATION_NON_TRANSPOSE} \\ A^T, & \text{if transA == HIPSPARSE_OPERATION_TRANSPOSE} \\ A^H, & \text{if transA == HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE} \end{array} \right. \end{split}\],\[\begin{split} op(B) = \left\{ \begin{array}{ll} B, & \text{if transB == HIPSPARSE_OPERATION_NON_TRANSPOSE} \\ B^T, & \text{if transB == HIPSPARSE_OPERATION_TRANSPOSE} \\ B^H, & \text{if transB == HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE} \end{array} \right. \end{split}\]and\[\begin{split} op(X) = \left\{ \begin{array}{ll} X, & \text{if transB == HIPSPARSE_OPERATION_NON_TRANSPOSE} \\ X^T, & \text{if transB == HIPSPARSE_OPERATION_TRANSPOSE} \\ X^H, & \text{if transB == HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE} \end{array} \right. \end{split}\]The solution is performed inplace meaning that the matrix \(B\) is overwritten with the solution \(X\) after calling

`hipsparseXcsrsm2_solve`

. Given that the sparse matrix \(A\) is a square matrix, its size is \(m \times m\) regardless of whether \(A\) is transposed or not. The size of the column-oriented dense matrices \(B\) and \(X\) have size that depends on the value of`transB:`

\[\begin{split} op(B)/op(X) = \left\{ \begin{array}{ll} ldb \times nrhs, \text{ } ldb \ge m, & \text{if transB == HIPSPARSE_OPERATION_NON_TRANSPOSE} \\ ldb \times m, \text{ } ldb \ge nrhs, & \text{if transB == HIPSPARSE_OPERATION_TRANSPOSE} \\ ldb \times m, \text{ } ldb \ge nrhs, & \text{if transB == HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE} \end{array} \right. \end{split}\]`hipsparseXcsrsm2_solve`

requires a user allocated temporary buffer. Its size is returned by[hipsparseXcsrsm2_bufferSizeExt()](#hipsparse__csrsm_8h_1a36c0b1981e97635cde38cf9fcbbc37ac). The size of the required buffer is larger when`transA`

equals[HIPSPARSE_OPERATION_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141a20e9c4bdd71ea4b509b6c0b7a495c0bf)or[HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141ac55e75ba3027186f1dc6164fdcb06f0e)and when`transB`

is[HIPSPARSE_OPERATION_NON_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141a270f0124eb0d0ac15c3e7afb18064547). The subsequent solve will also be faster when \(A\) is non-transposed and \(B\) is transposed (or conjugate transposed). For example, instead of solving:\[\begin{split} \begin{bmatrix} a_{00} & 0 & 0 \\ a_{10} & a_{11} & 0 \\ a_{20} & a_{21} & a_{22} \\ \end{bmatrix} \cdot \begin{bmatrix} x_{00} & x_{01} \\ x_{10} & x_{11} \\ x_{20} & x_{21} \\ \end{bmatrix} = \begin{bmatrix} b_{00} & b_{01} \\ b_{10} & b_{11} \\ b_{20} & b_{21} \\ \end{bmatrix} \end{split}\]Consider solving:

\[\begin{split} \begin{bmatrix} a_{00} & 0 & 0 \\ a_{10} & a_{11} & 0 \\ a_{20} & a_{21} & a_{22} \end{bmatrix} \cdot \begin{bmatrix} x_{00} & x_{10} & x_{20} \\ x_{01} & x_{11} & x_{21} \end{bmatrix}^{T} = \begin{bmatrix} b_{00} & b_{10} & b_{20} \\ b_{01} & b_{11} & b_{21} \end{bmatrix}^{T} \end{split}\]Once the temporary storage buffer has been allocated, analysis meta data is required. It can be obtained by

[hipsparseXcsrsm2_analysis()](#hipsparse__csrsm_8h_1aec706e7d801804490c7609b6796ddf0f). The triangular solve is completed by calling`hipsparseXcsrsm2_solve`

and once all solves are performed, the temporary storage buffer allocated by the user can be freed.Solving a triangular system involves division by the diagonal elements. This means that if the sparse matrix is missing the diagonal entry (referred to as a structural zero) or the diagonal entry is zero (referred to as a numerical zero) then a division by zero would occur.

`hipsparseXcsrsm2_solve`

tracks the location of the first zero pivot (either numerical or structural zero). The zero pivot status can be checked calling[hipsparseXcsrsm2_zeroPivot()](#hipsparse__csrsm_8h_1a0ea9dd8a24b17270fde9ddbaed87c54d). If[hipsparseXcsrsm2_zeroPivot()](#hipsparse__csrsm_8h_1a0ea9dd8a24b17270fde9ddbaed87c54d)returns[HIPSPARSE_STATUS_SUCCESS](types.html#hipsparse-types_8h_1aa069bec7a4f24d00dab1dc4612d4de79a146a8a2fd27ee49132f8dcea617fc481), then no zero pivot was found and therefore the matrix does not have a structural or numerical zero.The user can specify that the sparse matrix should be interpreted as having ones on the diagonal by setting the diagonal type on the descriptor

`descrA`

to[HIPSPARSE_DIAG_TYPE_UNIT](types.html#hipsparse-types_8h_1a79e036b6c0680cb37e2aa53d3542a054a532a9a4a4eaf63a967bfaac7f9936b39)using[hipsparseSetMatDiagType](auxiliary.html#hipsparse-auxiliary_8h_1aec6fa039793196011f15cfb0b21c2b59). If[hipsparseDiagType_t](types.html#hipsparse-types_8h_1a79e036b6c0680cb37e2aa53d3542a054)==[HIPSPARSE_DIAG_TYPE_UNIT](types.html#hipsparse-types_8h_1a79e036b6c0680cb37e2aa53d3542a054a532a9a4a4eaf63a967bfaac7f9936b39), no zero pivot will be reported, even if \(A_{j,j} = 0\) for some \(j\).The sparse CSR matrix passed to

`hipsparseXcsrsm2_solve`

does not actually have to be a triangular matrix. Instead the triangular upper or lower part of the sparse matrix is solved based on[hipsparseFillMode_t](types.html#hipsparse-types_8h_1ace47655e52ed1bb17309eda331c44332)set on the descriptor`descrA`

. If the fill mode is set to[HIPSPARSE_FILL_MODE_LOWER](types.html#hipsparse-types_8h_1ace47655e52ed1bb17309eda331c44332a470abb0661ab8951449efa6988ed49ef), then the lower triangular matrix is solved. If the fill mode is set to[HIPSPARSE_FILL_MODE_UPPER](types.html#hipsparse-types_8h_1ace47655e52ed1bb17309eda331c44332ac5c8ccc62dfff77c56c8480c24ed6b3b)then the upper triangular matrix is solved.**Example**int main(int argc, char* argv[]) { // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // A = ( 1.0 0.0 0.0 0.0 ) // ( 2.0 3.0 0.0 0.0 ) // ( 4.0 5.0 6.0 0.0 ) // ( 7.0 0.0 8.0 9.0 ) // Number of rows and columns int m = 4; int n = 4; // Number of right-hand-sides int nrhs = 4; // Number of non-zeros int nnz = 9; // CSR row pointers int hcsrRowPtr[5] = {0, 1, 3, 6, 9}; // CSR column indices int hcsrColInd[9] = {0, 0, 1, 0, 1, 2, 0, 2, 3}; // CSR values double hcsrVal[9] = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0}; // Transposition of the matrix and rhs matrix hipsparseOperation_t transA = HIPSPARSE_OPERATION_NON_TRANSPOSE; hipsparseOperation_t transB = HIPSPARSE_OPERATION_NON_TRANSPOSE; // Solve policy hipsparseSolvePolicy_t solve_policy = HIPSPARSE_SOLVE_POLICY_NO_LEVEL; // Scalar alpha and beta double alpha = 1.0; // rhs and solution matrix int ldb = n; double hB[16] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}; // Offload data to device int* dcsrRowPtr; int* dcsrColInd; double* dcsrVal; double* dB; HIP_CHECK(hipMalloc((void**)&dcsrRowPtr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&dcsrColInd, sizeof(int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcsrVal, sizeof(double) * nnz)); HIP_CHECK(hipMalloc((void**)&dB, sizeof(double) * n * nrhs)); HIP_CHECK(hipMemcpy(dcsrRowPtr, hcsrRowPtr, sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrColInd, hcsrColInd, sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrVal, hcsrVal, sizeof(double) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dB, hB, sizeof(double) * n * nrhs, hipMemcpyHostToDevice)); // Matrix descriptor hipsparseMatDescr_t descr; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&descr)); // Matrix fill mode HIPSPARSE_CHECK(hipsparseSetMatFillMode(descr, HIPSPARSE_FILL_MODE_LOWER)); // Matrix diagonal type HIPSPARSE_CHECK(hipsparseSetMatDiagType(descr, HIPSPARSE_DIAG_TYPE_NON_UNIT)); // Matrix info structure csrsm2Info_t info; HIPSPARSE_CHECK(hipsparseCreateCsrsm2Info(&info)); // Obtain required buffer size size_t buffer_size; HIPSPARSE_CHECK(hipsparseDcsrsm2_bufferSizeExt(handle, 0, transA, transB, m, nrhs, nnz, &alpha, descr, dcsrVal, dcsrRowPtr, dcsrColInd, dB, ldb, info, solve_policy, &buffer_size)); // Allocate temporary buffer void* dbuffer; HIP_CHECK(hipMalloc(&dbuffer, buffer_size)); // Perform analysis step HIPSPARSE_CHECK(hipsparseDcsrsm2_analysis(handle, 0, transA, transB, m, nrhs, nnz, &alpha, descr, dcsrVal, dcsrRowPtr, dcsrColInd, dB, ldb, info, solve_policy, dbuffer)); // Call dcsrsm to perform lower triangular solve LB = B HIPSPARSE_CHECK(hipsparseDcsrsm2_solve(handle, 0, transA, transB, m, nrhs, nnz, &alpha, descr, dcsrVal, dcsrRowPtr, dcsrColInd, dB, ldb, info, solve_policy, dbuffer)); // Check for zero pivots int pivot; hipsparseStatus_t status = hipsparseXcsrsm2_zeroPivot(handle, info, &pivot); if(status == HIPSPARSE_STATUS_ZERO_PIVOT) { std::cout << "Found zero pivot in matrix row " << pivot << std::endl; } // Copy result back to host HIP_CHECK(hipMemcpy(hB, dB, sizeof(double) * m * nrhs, hipMemcpyDeviceToHost)); // Clear hipSPARSE HIPSPARSE_CHECK(hipsparseDestroyCsrsm2Info(info)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(descr)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); // Clear device memory HIP_CHECK(hipFree(dcsrRowPtr)); HIP_CHECK(hipFree(dcsrColInd)); HIP_CHECK(hipFree(dcsrVal)); HIP_CHECK(hipFree(dB)); HIP_CHECK(hipFree(dbuffer)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

Currently, only

`transA`

!=[HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141ac55e75ba3027186f1dc6164fdcb06f0e)and`transB`

!=[HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141ac55e75ba3027186f1dc6164fdcb06f0e)is supported.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**algo**–**[in]**algorithm to use.**transA**–**[in]**matrix \(A\) operation type.**transB**–**[in]**matrix \(B\) operation type.**m**–**[in]**number of rows of the sparse CSR matrix \(A\).**nrhs**–**[in]**number of columns of the dense matrix \(op(B)\).**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix \(A\).**alpha**–**[in]**scalar \(\alpha\).**descrA**–**[in]**descriptor of the sparse CSR matrix \(A\).**csrSortedValA**–**[in]**array of`nnz`

elements of the sparse CSR matrix \(A\).**csrSortedRowPtrA**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(A\).**csrSortedColIndA**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix \(A\).**B**–**[inout]**array of`m`

\(\times\)`nrhs`

elements of the rhs matrix \(B\).**ldb**–**[in]**leading dimension of rhs matrix \(B\).**info**–**[in]**structure that holds the information collected during the analysis step.**policy**–**[in]**[HIPSPARSE_SOLVE_POLICY_NO_LEVEL](types.html#hipsparse-types_8h_1a0d98e490c94d4facc231db60baf1c3b3ac5830aa96848e832b3b375ad08abdb09)or[HIPSPARSE_SOLVE_POLICY_USE_LEVEL](types.html#hipsparse-types_8h_1a0d98e490c94d4facc231db60baf1c3b3a934309d6656638e375f0759b89fd81b5).**pBuffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`nrhs`

,`nnz`

,`alpha`

,`descrA`

,`csrSortedValA`

,`csrSortedRowPtrA`

,`csrSortedColIndA`

,`B`

,`info`

or`pBuffer`

is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`transA`

==[HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141ac55e75ba3027186f1dc6164fdcb06f0e),`transB`

==[HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141ac55e75ba3027186f1dc6164fdcb06f0e)or[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXgemmi()[#](#hipsparsexgemmi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSgemmi([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int k, int nnz, const float *alpha, const float *A, int lda, const float *cscValB, const int *cscColPtrB, const int *cscRowIndB, const float *beta, float *C, int ldc)[#](#_CPPv415hipsparseSgemmi17hipsparseHandle_tiiiiPKfPKfiPKfPKiPKiPKfPfi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDgemmi([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int k, int nnz, const double *alpha, const double *A, int lda, const double *cscValB, const int *cscColPtrB, const int *cscRowIndB, const double *beta, double *C, int ldc)[#](#_CPPv415hipsparseDgemmi17hipsparseHandle_tiiiiPKdPKdiPKdPKiPKiPKdPdi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCgemmi([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int k, int nnz, const hipComplex *alpha, const hipComplex *A, int lda, const hipComplex *cscValB, const int *cscColPtrB, const int *cscRowIndB, const hipComplex *beta, hipComplex *C, int ldc)[#](#_CPPv415hipsparseCgemmi17hipsparseHandle_tiiiiPK10hipComplexPK10hipComplexiPK10hipComplexPKiPKiPK10hipComplexP10hipComplexi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZgemmi([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int k, int nnz, const hipDoubleComplex *alpha, const hipDoubleComplex *A, int lda, const hipDoubleComplex *cscValB, const int *cscColPtrB, const int *cscRowIndB, const hipDoubleComplex *beta, hipDoubleComplex *C, int ldc)[#](#_CPPv415hipsparseZgemmi17hipsparseHandle_tiiiiPK16hipDoubleComplexPK16hipDoubleComplexiPK16hipDoubleComplexPKiPKiPK16hipDoubleComplexP16hipDoubleComplexi) Dense matrix sparse matrix multiplication using CSC storage format.

`hipsparseXgemmi`

multiplies the scalar \(\alpha\) with a dense column-oriented \(m \times k\) matrix \(A\) and the sparse \(k \times n\) matrix \(B\), defined in CSC storage format and adds the result to the dense column-oriented \(m \times n\) matrix \(C\) that is multiplied by the scalar \(\beta\), such that\[ C := \alpha \cdot A \cdot B + \beta \cdot C \]**Example**int main(int argc, char* argv[]) { // A, B, and C are m×k, k×n, and m×n const int m = 3, n = 5, k = 4; const int lda = m, ldc = m; const int nnz_A = m * k, nnz_B = 10, nnz_C = m * n; // alpha and beta float alpha = 0.5f; float beta = 0.25f; std::vector<int> hcscColPtr = {0, 2, 5, 7, 8, 10}; std::vector<int> hcscRowInd = {0, 2, 0, 1, 3, 1, 3, 2, 0, 2}; std::vector<float> hcsc_val = {1, 6, 2, 4, 9, 5, 2, 7, 3, 8}; std::vector<float> hA(nnz_A, 1.0f); std::vector<float> hC(nnz_C, 1.0f); int* dcscColPtr; int* dcscRowInd; float* dcsc_val; HIP_CHECK(hipMalloc((void**)&dcscColPtr, sizeof(int) * (n + 1))); HIP_CHECK(hipMalloc((void**)&dcscRowInd, sizeof(int) * nnz_B)); HIP_CHECK(hipMalloc((void**)&dcsc_val, sizeof(float) * nnz_B)); HIP_CHECK( hipMemcpy(dcscColPtr, hcscColPtr.data(), sizeof(int) * (n + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcscRowInd, hcscRowInd.data(), sizeof(int) * nnz_B, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsc_val, hcsc_val.data(), sizeof(float) * nnz_B, hipMemcpyHostToDevice)); hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // Allocate memory for the matrix A float* dA; HIP_CHECK(hipMalloc((void**)&dA, sizeof(float) * nnz_A)); HIP_CHECK(hipMemcpy(dA, hA.data(), sizeof(float) * nnz_A, hipMemcpyHostToDevice)); // Allocate memory for the resulting matrix C float* dC; HIP_CHECK(hipMalloc((void**)&dC, sizeof(float) * nnz_C)); HIP_CHECK(hipMemcpy(dC, hC.data(), sizeof(float) * nnz_C, hipMemcpyHostToDevice)); // Perform operation HIPSPARSE_CHECK(hipsparseSgemmi( handle, m, n, k, nnz_B, &alpha, dA, lda, dcsc_val, dcscColPtr, dcscRowInd, &beta, dC, ldc)); // Copy device to host HIP_CHECK(hipMemcpy(hC.data(), dC, sizeof(float) * nnz_C, hipMemcpyDeviceToHost)); std::cout << "hC" << std::endl; for(int i = 0; i < nnz_C; i++) { std::cout << hC[i] << " "; } std::cout << "" << std::endl; // Destroy matrix descriptors and handles HIPSPARSE_CHECK(hipsparseDestroy(handle)); HIP_CHECK(hipFree(dcscColPtr)); HIP_CHECK(hipFree(dcscRowInd)); HIP_CHECK(hipFree(dcsc_val)); HIP_CHECK(hipFree(dA)); HIP_CHECK(hipFree(dC)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the dense matrix \(A\).**n**–**[in]**number of columns of the sparse CSC matrix \(op(B)\) and \(C\).**k**–**[in]**number of columns of the dense matrix \(A\).**nnz**–**[in]**number of non-zero entries of the sparse CSC matrix \(B\).**alpha**–**[in]**scalar \(\alpha\).**A**–**[in]**array of dimension \(lda \times k\) ( \(op(A) == A\)) or \(lda \times m\) ( \(op(A) == A^T\) or \(op(A) == A^H\)).**lda**–**[in]**leading dimension of \(A\), must be at least \(m\) ( \(op(A) == A\)) or \(k\) ( \(op(A) == A^T\) or \(op(A) == A^H\)).**cscValB**–**[in]**array of`nnz`

elements of the sparse CSC matrix \(B\).**cscColPtrB**–**[in]**array of`n+1`

elements that point to the start of every column of the sparse CSC matrix \(B\).**cscRowIndB**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSC matrix \(B\).**beta**–**[in]**scalar \(\beta\).**C**–**[inout]**array of dimension \(ldc \times n\) that holds the values of \(C\).**ldc**–**[in]**leading dimension of \(C\), must be at least \(m\).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`k`

,`nnz`

,`lda`

,`ldc`

,`alpha`

,`A`

,`cscValB`

,`cscColPtrB`

,`cscRowIndB`

,`beta`

or`C`

is invalid.
