---
title: "Sparse extra functions &#8212; hipSPARSE 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipSPARSE/en/latest/reference/extra.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:09:44.974420+00:00
content_hash: "b5e8e12ef36795ee"
---

# Sparse extra functions[#](#sparse-extra-functions)

This module contains all sparse extra routines.

The sparse extra routines describe operations that manipulate sparse matrices.

## hipsparseXcsrgeamNnz()[#](#hipsparsexcsrgeamnnz)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseXcsrgeamNnz([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, int nnzA, const int *csrRowPtrA, const int *csrColIndA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrB, int nnzB, const int *csrRowPtrB, const int *csrColIndB, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, int *csrRowPtrC, int *nnzTotalDevHostPtr)[#](#_CPPv420hipsparseXcsrgeamNnz17hipsparseHandle_tiiK19hipsparseMatDescr_tiPKiPKiK19hipsparseMatDescr_tiPKiPKiK19hipsparseMatDescr_tPiPi) `hipsparseXcsrgeamNnz`

computes the total CSR non-zero elements and the CSR row offsets, that point to the start of every row of the sparse CSR matrix, of the resulting matrix \(C\). It is assumed that`csrRowPtrC`

has been allocated with size`m+1`

. The desired index base in the output CSR matrix is set in the[hipsparseMatDescr_t](types.html#hipsparse-types_8h_1a4c2f3ad3f2057bffb1adf6a8256537b9). See[hipsparseSetMatIndexBase()](auxiliary.html#hipsparse-auxiliary_8h_1a3c81b4bd7b1e9bb04a63a620f51dc2a8).For full code example, see

[hipsparseScsrgeam()](#hipsparse__csrgeam_8h_1a118edeb77e424820f829d2c46e746037).Note

As indicated,

`nnzTotalDevHostPtr`

can point either to host or device memory. This is controlled by setting the pointer mode. See[hipsparseSetPointerMode()](auxiliary.html#hipsparse-auxiliary_8h_1a7d876174f77e1f8f816781af1c3c667c).Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix \(A\), \(B\) and \(C\).**n**–**[in]**number of columns of the sparse CSR matrix \(A\), \(B\) and \(C\).**descrA**–**[in]**descriptor of the sparse CSR matrix \(A\). Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**nnzA**–**[in]**number of non-zero entries of the sparse CSR matrix \(A\).**csrRowPtrA**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(A\).**csrColIndA**–**[in]**array of`nnzA`

elements containing the column indices of the sparse CSR matrix \(A\).**descrB**–**[in]**descriptor of the sparse CSR matrix \(B\). Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**nnzB**–**[in]**number of non-zero entries of the sparse CSR matrix \(B\).**csrRowPtrB**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(B\).**csrColIndB**–**[in]**array of`nnzB`

elements containing the column indices of the sparse CSR matrix \(B\).**descrC**–**[in]**descriptor of the sparse CSR matrix \(C\). Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**csrRowPtrC**–**[out]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(C\).**nnzTotalDevHostPtr**–**[out]**pointer to the number of non-zero entries of the sparse CSR matrix \(C\).`nnzTotalDevHostPtr`

can be a host or device pointer.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`nnzA`

,`nnzB`

,`descrA`

,`csrRowPtrA`

,`csrColIndA`

,`descrB`

,`csrRowPtrB`

,`csrColIndB`

,`descrC`

,`csrRowPtrC`

or`nnzTotalDevHostPtr`

is invalid.**HIPSPARSE_STATUS_NOT_SUPPORTED**–[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXcsrgeam()[#](#hipsparsexcsrgeam)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseScsrgeam([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const float *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, int nnzA, const float *csrValA, const int *csrRowPtrA, const int *csrColIndA, const float *beta, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrB, int nnzB, const float *csrValB, const int *csrRowPtrB, const int *csrColIndB, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, float *csrValC, int *csrRowPtrC, int *csrColIndC)[#](#_CPPv417hipsparseScsrgeam17hipsparseHandle_tiiPKfK19hipsparseMatDescr_tiPKfPKiPKiPKfK19hipsparseMatDescr_tiPKfPKiPKiK19hipsparseMatDescr_tPfPiPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDcsrgeam([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const double *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, int nnzA, const double *csrValA, const int *csrRowPtrA, const int *csrColIndA, const double *beta, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrB, int nnzB, const double *csrValB, const int *csrRowPtrB, const int *csrColIndB, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, double *csrValC, int *csrRowPtrC, int *csrColIndC)[#](#_CPPv417hipsparseDcsrgeam17hipsparseHandle_tiiPKdK19hipsparseMatDescr_tiPKdPKiPKiPKdK19hipsparseMatDescr_tiPKdPKiPKiK19hipsparseMatDescr_tPdPiPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCcsrgeam([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const hipComplex *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, int nnzA, const hipComplex *csrValA, const int *csrRowPtrA, const int *csrColIndA, const hipComplex *beta, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrB, int nnzB, const hipComplex *csrValB, const int *csrRowPtrB, const int *csrColIndB, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, hipComplex *csrValC, int *csrRowPtrC, int *csrColIndC)[#](#_CPPv417hipsparseCcsrgeam17hipsparseHandle_tiiPK10hipComplexK19hipsparseMatDescr_tiPK10hipComplexPKiPKiPK10hipComplexK19hipsparseMatDescr_tiPK10hipComplexPKiPKiK19hipsparseMatDescr_tP10hipComplexPiPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZcsrgeam([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const hipDoubleComplex *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, int nnzA, const hipDoubleComplex *csrValA, const int *csrRowPtrA, const int *csrColIndA, const hipDoubleComplex *beta, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrB, int nnzB, const hipDoubleComplex *csrValB, const int *csrRowPtrB, const int *csrColIndB, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, hipDoubleComplex *csrValC, int *csrRowPtrC, int *csrColIndC)[#](#_CPPv417hipsparseZcsrgeam17hipsparseHandle_tiiPK16hipDoubleComplexK19hipsparseMatDescr_tiPK16hipDoubleComplexPKiPKiPK16hipDoubleComplexK19hipsparseMatDescr_tiPK16hipDoubleComplexPKiPKiK19hipsparseMatDescr_tP16hipDoubleComplexPiPi) Sparse matrix sparse matrix addition using CSR storage format.

`hipsparseXcsrgeam`

multiplies the scalar \(\alpha\) with the sparse \(m \times n\) matrix \(A\), defined in CSR storage format, multiplies the scalar \(\beta\) with the sparse \(m \times n\) matrix \(B\), defined in CSR storage format, and adds both resulting matrices to obtain the sparse \(m \times n\) matrix \(C\), defined in CSR storage format, such that\[ C := \alpha \cdot A + \beta \cdot B. \]This computation involves a multi step process. First the user must allocate

`csrRowPtrC`

to have size`m+1`

. The user then calls[hipsparseXcsrgeamNnz](#hipsparse__csrgeam_8h_1a71b9f65b7ebbb45c20b7f523e4e542e6)which fills in the`csrRowPtrC`

array as well as computes the total number of nonzeros in \(C\),`nnzC`

. The user then allocates both arrays`csrColIndC`

and`csrValC`

to have size`nnzC`

and calls`hipsparseXcsrgeam`

to complete the computation. The desired index base in the output CSR matrix \(C\) is set in the[hipsparseMatDescr_t](types.html#hipsparse-types_8h_1a4c2f3ad3f2057bffb1adf6a8256537b9)`descrC`

. See[hipsparseSetMatIndexBase()](auxiliary.html#hipsparse-auxiliary_8h_1a3c81b4bd7b1e9bb04a63a620f51dc2a8).**Example**int main(int argc, char* argv[]) { const int m = 4; const int n = 4; const int nnzA = 9; const int nnzB = 6; float alpha{1.0f}; float beta{1.0f}; // A, B, and C are m×n // A // 1 0 0 2 // 3 4 0 0 // 5 6 7 8 // 0 0 9 0 std::vector<int> hcsrRowPtrA = {0, 2, 4, 8, 9}; std::vector<int> hcsrColIndA = {0, 3, 0, 1, 0, 1, 2, 3, 2}; std::vector<float> hcsrValA = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f, 9.0f}; // B // 0 1 0 0 // 1 0 1 0 // 0 1 0 1 // 0 0 1 0 std::vector<int> hcsrRowPtrB = {0, 1, 3, 5, 6}; std::vector<int> hcsrColIndB = {1, 0, 2, 1, 3, 2}; std::vector<float> hcsrValB = {1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f}; // Device memory management: Allocate and copy A, B int* dcsrRowPtrA; int* dcsrColIndA; float* dcsrValA; int* dcsrRowPtrB; int* dcsrColIndB; float* dcsrValB; int* dcsrRowPtrC; HIP_CHECK(hipMalloc((void**)&dcsrRowPtrA, (m + 1) * sizeof(int))); HIP_CHECK(hipMalloc((void**)&dcsrColIndA, nnzA * sizeof(int))); HIP_CHECK(hipMalloc((void**)&dcsrValA, nnzA * sizeof(float))); HIP_CHECK(hipMalloc((void**)&dcsrRowPtrB, (m + 1) * sizeof(int))); HIP_CHECK(hipMalloc((void**)&dcsrColIndB, nnzB * sizeof(int))); HIP_CHECK(hipMalloc((void**)&dcsrValB, nnzB * sizeof(float))); HIP_CHECK(hipMalloc((void**)&dcsrRowPtrC, (m + 1) * sizeof(int))); HIP_CHECK( hipMemcpy(dcsrRowPtrA, hcsrRowPtrA.data(), (m + 1) * sizeof(int), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsrColIndA, hcsrColIndA.data(), nnzA * sizeof(int), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrValA, hcsrValA.data(), nnzA * sizeof(float), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsrRowPtrB, hcsrRowPtrB.data(), (m + 1) * sizeof(int), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsrColIndB, hcsrColIndB.data(), nnzB * sizeof(int), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrValB, hcsrValB.data(), nnzB * sizeof(float), hipMemcpyHostToDevice)); hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); hipsparseMatDescr_t descrA; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&descrA)); hipsparseMatDescr_t descrB; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&descrB)); hipsparseMatDescr_t descrC; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&descrC)); int nnzC; HIPSPARSE_CHECK(hipsparseXcsrgeamNnz(handle, m, n, descrA, nnzA, dcsrRowPtrA, dcsrColIndA, descrB, nnzB, dcsrRowPtrB, dcsrColIndB, descrC, dcsrRowPtrC, &nnzC)); int* dcsrColIndC = nullptr; float* dcsrValC = nullptr; HIP_CHECK(hipMalloc((void**)&dcsrColIndC, sizeof(int) * nnzC)); HIP_CHECK(hipMalloc((void**)&dcsrValC, sizeof(float) * nnzC)); HIPSPARSE_CHECK(hipsparseScsrgeam(handle, m, n, &alpha, descrA, nnzA, dcsrValA, dcsrRowPtrA, dcsrColIndA, &beta, descrB, nnzB, dcsrValB, dcsrRowPtrB, dcsrColIndB, descrC, dcsrValC, dcsrRowPtrC, dcsrColIndC)); std::vector<int> hcsrRowPtrC(m + 1); std::vector<int> hcsrColIndC(nnzC); std::vector<float> hcsrValC(nnzC); // Copy back to the host HIP_CHECK( hipMemcpy(hcsrRowPtrC.data(), dcsrRowPtrC, sizeof(int) * (m + 1), hipMemcpyDeviceToHost)); HIP_CHECK( hipMemcpy(hcsrColIndC.data(), dcsrColIndC, sizeof(int) * nnzC, hipMemcpyDeviceToHost)); HIP_CHECK(hipMemcpy(hcsrValC.data(), dcsrValC, sizeof(float) * nnzC, hipMemcpyDeviceToHost)); std::cout << "C" << std::endl; for(int i = 0; i < m; i++) { int start = hcsrRowPtrC[i]; int end = hcsrRowPtrC[i + 1]; std::vector<float> temp(n, 0.0f); for(int j = start; j < end; j++) { temp[hcsrColIndC[j]] = hcsrValC[j]; } for(int j = 0; j < n; j++) { std::cout << temp[j] << " "; } std::cout << "" << std::endl; } std::cout << "" << std::endl; HIP_CHECK(hipFree(dcsrRowPtrA)); HIP_CHECK(hipFree(dcsrColIndA)); HIP_CHECK(hipFree(dcsrValA)); HIP_CHECK(hipFree(dcsrRowPtrB)); HIP_CHECK(hipFree(dcsrColIndB)); HIP_CHECK(hipFree(dcsrValB)); HIP_CHECK(hipFree(dcsrRowPtrC)); HIP_CHECK(hipFree(dcsrColIndC)); HIP_CHECK(hipFree(dcsrValC)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(descrA)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(descrB)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(descrC)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); return 0; }


Note

Both scalars \(\alpha\) and \(beta\) have to be valid.

Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix \(A\), \(B\) and \(C\).**n**–**[in]**number of columns of the sparse CSR matrix \(A\), \(B\) and \(C\).**alpha**–**[in]**scalar \(\alpha\).**descrA**–**[in]**descriptor of the sparse CSR matrix \(A\). Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**nnzA**–**[in]**number of non-zero entries of the sparse CSR matrix \(A\).**csrValA**–**[in]**array of`nnzA`

elements of the sparse CSR matrix \(A\).**csrRowPtrA**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(A\).**csrColIndA**–**[in]**array of`nnzA`

elements containing the column indices of the sparse CSR matrix \(A\).**beta**–**[in]**scalar \(\beta\).**descrB**–**[in]**descriptor of the sparse CSR matrix \(B\). Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**nnzB**–**[in]**number of non-zero entries of the sparse CSR matrix \(B\).**csrValB**–**[in]**array of`nnzB`

elements of the sparse CSR matrix \(B\).**csrRowPtrB**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(B\).**csrColIndB**–**[in]**array of`nnzB`

elements containing the column indices of the sparse CSR matrix \(B\).**descrC**–**[in]**descriptor of the sparse CSR matrix \(C\). Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**csrValC**–**[out]**array of elements of the sparse CSR matrix \(C\).**csrRowPtrC**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(C\).**csrColIndC**–**[out]**array of elements containing the column indices of the sparse CSR matrix \(C\).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`nnzA`

,`nnzB`

,`alpha`

,`descrA`

,`csrValA`

,`csrRowPtrA`

,`csrColIndA`

,`beta`

,`descrB`

,`csrValB`

,`csrRowPtrB`

,`csrColIndB`

,`descrC`

,`csrValC`

,`csrRowPtrC`

or`csrColIndC`

is invalid.**HIPSPARSE_STATUS_NOT_SUPPORTED**–[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXcsrgeam2_bufferSizeExt()[#](#hipsparsexcsrgeam2-buffersizeext)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseScsrgeam2_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const float *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, int nnzA, const float *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA, const float *beta, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrB, int nnzB, const float *csrSortedValB, const int *csrSortedRowPtrB, const int *csrSortedColIndB, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, const float *csrSortedValC, const int *csrSortedRowPtrC, const int *csrSortedColIndC, size_t *pBufferSizeInBytes)[#](#_CPPv432hipsparseScsrgeam2_bufferSizeExt17hipsparseHandle_tiiPKfK19hipsparseMatDescr_tiPKfPKiPKiPKfK19hipsparseMatDescr_tiPKfPKiPKiK19hipsparseMatDescr_tPKfPKiPKiP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDcsrgeam2_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const double *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, int nnzA, const double *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA, const double *beta, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrB, int nnzB, const double *csrSortedValB, const int *csrSortedRowPtrB, const int *csrSortedColIndB, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, const double *csrSortedValC, const int *csrSortedRowPtrC, const int *csrSortedColIndC, size_t *pBufferSizeInBytes)[#](#_CPPv432hipsparseDcsrgeam2_bufferSizeExt17hipsparseHandle_tiiPKdK19hipsparseMatDescr_tiPKdPKiPKiPKdK19hipsparseMatDescr_tiPKdPKiPKiK19hipsparseMatDescr_tPKdPKiPKiP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCcsrgeam2_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const hipComplex *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, int nnzA, const hipComplex *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA, const hipComplex *beta, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrB, int nnzB, const hipComplex *csrSortedValB, const int *csrSortedRowPtrB, const int *csrSortedColIndB, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, const hipComplex *csrSortedValC, const int *csrSortedRowPtrC, const int *csrSortedColIndC, size_t *pBufferSizeInBytes)[#](#_CPPv432hipsparseCcsrgeam2_bufferSizeExt17hipsparseHandle_tiiPK10hipComplexK19hipsparseMatDescr_tiPK10hipComplexPKiPKiPK10hipComplexK19hipsparseMatDescr_tiPK10hipComplexPKiPKiK19hipsparseMatDescr_tPK10hipComplexPKiPKiP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZcsrgeam2_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const hipDoubleComplex *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, int nnzA, const hipDoubleComplex *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA, const hipDoubleComplex *beta, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrB, int nnzB, const hipDoubleComplex *csrSortedValB, const int *csrSortedRowPtrB, const int *csrSortedColIndB, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, const hipDoubleComplex *csrSortedValC, const int *csrSortedRowPtrC, const int *csrSortedColIndC, size_t *pBufferSizeInBytes)[#](#_CPPv432hipsparseZcsrgeam2_bufferSizeExt17hipsparseHandle_tiiPK16hipDoubleComplexK19hipsparseMatDescr_tiPK16hipDoubleComplexPKiPKiPK16hipDoubleComplexK19hipsparseMatDescr_tiPK16hipDoubleComplexPKiPKiK19hipsparseMatDescr_tPK16hipDoubleComplexPKiPKiP6size_t) `hipsparseXcsrgeam2_bufferSizeExt`

returns the size of the temporary storage buffer in bytes that is required by[hipsparseXcsrgeam2Nnz()](#hipsparse__csrgeam_8h_1aa2563842dd05498422f1044f80fd5516)and[hipsparseXcsrgeam2()](#hipsparse__csrgeam_8h_1a843ebe3e65ecc29d92aeacabdaa08db6). The temporary storage buffer must be allocated by the user.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix \(A\), \(B\) and \(C\).**n**–**[in]**number of columns of the sparse CSR matrix \(A\), \(B\) and \(C\).**alpha**–**[in]**scalar \(\alpha\).**descrA**–**[in]**descriptor of the sparse CSR matrix \(A\). Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**nnzA**–**[in]**number of non-zero entries of the sparse CSR matrix \(A\).**csrSortedValA**–**[in]**array of`nnzA`

elements of the sparse CSR matrix \(A\).**csrSortedRowPtrA**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(A\).**csrSortedColIndA**–**[in]**array of`nnzA`

elements containing the column indices of the sparse CSR matrix \(A\).**beta**–**[in]**scalar \(\beta\).**descrB**–**[in]**descriptor of the sparse CSR matrix \(B\). Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**nnzB**–**[in]**number of non-zero entries of the sparse CSR matrix \(B\).**csrSortedValB**–**[in]**array of`nnzB`

elements of the sparse CSR matrix \(B\).**csrSortedRowPtrB**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(B\).**csrSortedColIndB**–**[in]**array of`nnzB`

elements containing the column indices of the sparse CSR matrix \(B\).**descrC**–**[in]**descriptor of the sparse CSR matrix \(C\). Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**csrSortedValC**–**[out]**array of elements of the sparse CSR matrix \(C\).**csrSortedRowPtrC**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(C\).**csrSortedColIndC**–**[out]**array of elements containing the column indices of the sparse CSR matrix \(C\).**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer required by[hipsparseXcsrgeam2Nnz()](#hipsparse__csrgeam_8h_1aa2563842dd05498422f1044f80fd5516)and[hipsparseXcsrgeam2()](#hipsparse__csrgeam_8h_1a843ebe3e65ecc29d92aeacabdaa08db6).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`nnzA`

,`nnzB`

,`alpha`

,`descrA`

,`csrSortedValA`

,`csrSortedRowPtrA`

,`csrSortedColIndA`

,`beta`

,`descrB`

,`csrSortedValB`

,`csrSortedRowPtrB`

,`csrSortedColIndB`

,`descrC`

,`csrSortedValC`

,`csrSortedRowPtrC`

,`csrSortedColIndC`

, or`pBufferSizeInBytes`

is invalid.**HIPSPARSE_STATUS_NOT_SUPPORTED**–[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXcsrgeam2Nnz()[#](#hipsparsexcsrgeam2nnz)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseXcsrgeam2Nnz([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, int nnzA, const int *csrSortedRowPtrA, const int *csrSortedColIndA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrB, int nnzB, const int *csrSortedRowPtrB, const int *csrSortedColIndB, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, int *csrSortedRowPtrC, int *nnzTotalDevHostPtr, void *workspace)[#](#_CPPv421hipsparseXcsrgeam2Nnz17hipsparseHandle_tiiK19hipsparseMatDescr_tiPKiPKiK19hipsparseMatDescr_tiPKiPKiK19hipsparseMatDescr_tPiPiPv) `hipsparseXcsrgeam2Nnz`

computes the total CSR non-zero elements and the CSR row offsets, that point to the start of every row of the sparse CSR matrix, of the resulting matrix \(C\). It is assumed that`csrRowPtrC`

has been allocated with size`m+1`

. The required buffer size can be obtained by[hipsparseXcsrgeam2_bufferSizeExt()](#hipsparse__csrgeam_8h_1a2f08b455db7fc0f233b32e86d36fb240). The desired index base in the output CSR matrix \(C\) is set in the[hipsparseMatDescr_t](types.html#hipsparse-types_8h_1a4c2f3ad3f2057bffb1adf6a8256537b9)`descrC`

. See[hipsparseSetMatIndexBase()](auxiliary.html#hipsparse-auxiliary_8h_1a3c81b4bd7b1e9bb04a63a620f51dc2a8).Note

As indicated,

`nnzTotalDevHostPtr`

can point either to host or device memory. This is controlled by setting the pointer mode. See[hipsparseSetPointerMode()](auxiliary.html#hipsparse-auxiliary_8h_1a7d876174f77e1f8f816781af1c3c667c).Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix \(A\), \(B\) and \(C\).**n**–**[in]**number of columns of the sparse CSR matrix \(A\), \(B\) and \(C\).**descrA**–**[in]**descriptor of the sparse CSR matrix \(A\). Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**nnzA**–**[in]**number of non-zero entries of the sparse CSR matrix \(A\).**csrSortedRowPtrA**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(A\).**csrSortedColIndA**–**[in]**array of`nnzA`

elements containing the column indices of the sparse CSR matrix \(A\).**descrB**–**[in]**descriptor of the sparse CSR matrix \(B\). Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**nnzB**–**[in]**number of non-zero entries of the sparse CSR matrix \(B\).**csrSortedRowPtrB**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(B\).**csrSortedColIndB**–**[in]**array of`nnzB`

elements containing the column indices of the sparse CSR matrix \(B\).**descrC**–**[in]**descriptor of the sparse CSR matrix \(C\). Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**csrSortedRowPtrC**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(C\).**nnzTotalDevHostPtr**–**[out]**pointer to the number of non-zero entries of the sparse CSR matrix \(C\).`nnzTotalDevHostPtr`

can be a host or device pointer.**workspace**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`nnzA`

,`nnzB`

,`descrA`

,`csrSortedRowPtrA`

,`csrSortedColIndA`

,`descrB`

,`csrSortedRowPtrB`

,`csrSortedColIndB`

,`descrC`

,`csrSortedRowPtrC`

or`nnzTotalDevHostPtr`

is invalid.**HIPSPARSE_STATUS_NOT_SUPPORTED**–[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXcsrgeam2()[#](#hipsparsexcsrgeam2)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseScsrgeam2([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const float *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, int nnzA, const float *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA, const float *beta, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrB, int nnzB, const float *csrSortedValB, const int *csrSortedRowPtrB, const int *csrSortedColIndB, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, float *csrSortedValC, int *csrSortedRowPtrC, int *csrSortedColIndC, void *pBuffer)[#](#_CPPv418hipsparseScsrgeam217hipsparseHandle_tiiPKfK19hipsparseMatDescr_tiPKfPKiPKiPKfK19hipsparseMatDescr_tiPKfPKiPKiK19hipsparseMatDescr_tPfPiPiPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDcsrgeam2([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const double *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, int nnzA, const double *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA, const double *beta, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrB, int nnzB, const double *csrSortedValB, const int *csrSortedRowPtrB, const int *csrSortedColIndB, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, double *csrSortedValC, int *csrSortedRowPtrC, int *csrSortedColIndC, void *pBuffer)[#](#_CPPv418hipsparseDcsrgeam217hipsparseHandle_tiiPKdK19hipsparseMatDescr_tiPKdPKiPKiPKdK19hipsparseMatDescr_tiPKdPKiPKiK19hipsparseMatDescr_tPdPiPiPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCcsrgeam2([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const hipComplex *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, int nnzA, const hipComplex *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA, const hipComplex *beta, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrB, int nnzB, const hipComplex *csrSortedValB, const int *csrSortedRowPtrB, const int *csrSortedColIndB, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, hipComplex *csrSortedValC, int *csrSortedRowPtrC, int *csrSortedColIndC, void *pBuffer)[#](#_CPPv418hipsparseCcsrgeam217hipsparseHandle_tiiPK10hipComplexK19hipsparseMatDescr_tiPK10hipComplexPKiPKiPK10hipComplexK19hipsparseMatDescr_tiPK10hipComplexPKiPKiK19hipsparseMatDescr_tP10hipComplexPiPiPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZcsrgeam2([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const hipDoubleComplex *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, int nnzA, const hipDoubleComplex *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA, const hipDoubleComplex *beta, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrB, int nnzB, const hipDoubleComplex *csrSortedValB, const int *csrSortedRowPtrB, const int *csrSortedColIndB, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, hipDoubleComplex *csrSortedValC, int *csrSortedRowPtrC, int *csrSortedColIndC, void *pBuffer)[#](#_CPPv418hipsparseZcsrgeam217hipsparseHandle_tiiPK16hipDoubleComplexK19hipsparseMatDescr_tiPK16hipDoubleComplexPKiPKiPK16hipDoubleComplexK19hipsparseMatDescr_tiPK16hipDoubleComplexPKiPKiK19hipsparseMatDescr_tP16hipDoubleComplexPiPiPv) Sparse matrix sparse matrix addition using CSR storage format.

`hipsparseXcsrgeam2`

multiplies the scalar \(\alpha\) with the sparse \(m \times n\) matrix \(A\), defined in CSR storage format, multiplies the scalar \(\beta\) with the sparse \(m \times n\) matrix \(B\), defined in CSR storage format, and adds both resulting matrices to obtain the sparse \(m \times n\) matrix \(C\), defined in CSR storage format, such that\[ C := \alpha \cdot A + \beta \cdot B. \]This computation involves a multi step process. First the user must call

[hipsparseXcsrgeam2_bufferSizeExt()](#hipsparse__csrgeam_8h_1a2f08b455db7fc0f233b32e86d36fb240)in order to determine the required user allocated temporary buffer size. The user then allocates this buffer and also allocates`csrRowPtrC`

to have size`m+1`

. Both the temporary storage buffer and`csrRowPtrC`

array are then passed to[hipsparseXcsrgeam2Nnz](#hipsparse__csrgeam_8h_1aa2563842dd05498422f1044f80fd5516)which fills in the`csrRowPtrC`

array as well as computes the total number of nonzeros in C,`nnzC`

. The user then allocates both arrays`csrColIndC`

and`csrValC`

to have size`nnzC`

and calls`hipsparseXcsrgeam2`

to complete the computation. The desired index base in the output CSR matrix C is set in the[hipsparseMatDescr_t](types.html#hipsparse-types_8h_1a4c2f3ad3f2057bffb1adf6a8256537b9)`descrC`

. See[hipsparseSetMatIndexBase()](auxiliary.html#hipsparse-auxiliary_8h_1a3c81b4bd7b1e9bb04a63a620f51dc2a8).**Example**int main(int argc, char* argv[]) { const int m = 4; const int n = 4; const int nnzA = 9; const int nnzB = 6; float alpha{1.0f}; float beta{1.0f}; // A, B, and C are m×n // A // 1 0 0 2 // 3 4 0 0 // 5 6 7 8 // 0 0 9 0 std::vector<int> hcsrRowPtrA = {0, 2, 4, 8, 9}; std::vector<int> hcsrColIndA = {0, 3, 0, 1, 0, 1, 2, 3, 2}; std::vector<float> hcsrValA = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f, 9.0f}; // B // 0 1 0 0 // 1 0 1 0 // 0 1 0 1 // 0 0 1 0 std::vector<int> hcsrRowPtrB = {0, 1, 3, 5, 6}; std::vector<int> hcsrColIndB = {1, 0, 2, 1, 3, 2}; std::vector<float> hcsrValB = {1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f}; // Device memory management: Allocate and copy A, B int* dcsrRowPtrA; int* dcsrColIndA; float* dcsrValA; int* dcsrRowPtrB; int* dcsrColIndB; float* dcsrValB; int* dcsrRowPtrC; HIP_CHECK(hipMalloc((void**)&dcsrRowPtrA, (m + 1) * sizeof(int))); HIP_CHECK(hipMalloc((void**)&dcsrColIndA, nnzA * sizeof(int))); HIP_CHECK(hipMalloc((void**)&dcsrValA, nnzA * sizeof(float))); HIP_CHECK(hipMalloc((void**)&dcsrRowPtrB, (m + 1) * sizeof(int))); HIP_CHECK(hipMalloc((void**)&dcsrColIndB, nnzB * sizeof(int))); HIP_CHECK(hipMalloc((void**)&dcsrValB, nnzB * sizeof(float))); HIP_CHECK(hipMalloc((void**)&dcsrRowPtrC, (m + 1) * sizeof(int))); HIP_CHECK( hipMemcpy(dcsrRowPtrA, hcsrRowPtrA.data(), (m + 1) * sizeof(int), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsrColIndA, hcsrColIndA.data(), nnzA * sizeof(int), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrValA, hcsrValA.data(), nnzA * sizeof(float), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsrRowPtrB, hcsrRowPtrB.data(), (m + 1) * sizeof(int), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsrColIndB, hcsrColIndB.data(), nnzB * sizeof(int), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrValB, hcsrValB.data(), nnzB * sizeof(float), hipMemcpyHostToDevice)); hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); hipsparseMatDescr_t descrA; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&descrA)); hipsparseMatDescr_t descrB; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&descrB)); hipsparseMatDescr_t descrC; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&descrC)); size_t bufferSize; HIPSPARSE_CHECK(hipsparseScsrgeam2_bufferSizeExt(handle, m, n, &alpha, descrA, nnzA, dcsrValA, dcsrRowPtrA, dcsrColIndA, &beta, descrB, nnzB, dcsrValB, dcsrRowPtrB, dcsrColIndB, descrC, nullptr, dcsrRowPtrC, nullptr, &bufferSize)); void* dbuffer = nullptr; HIP_CHECK(hipMalloc((void**)&dbuffer, bufferSize)); int nnzC; HIPSPARSE_CHECK(hipsparseXcsrgeam2Nnz(handle, m, n, descrA, nnzA, dcsrRowPtrA, dcsrColIndA, descrB, nnzB, dcsrRowPtrB, dcsrColIndB, descrC, dcsrRowPtrC, &nnzC, dbuffer)); int* dcsrColIndC = nullptr; float* dcsrValC = nullptr; HIP_CHECK(hipMalloc((void**)&dcsrColIndC, sizeof(int) * nnzC)); HIP_CHECK(hipMalloc((void**)&dcsrValC, sizeof(float) * nnzC)); HIPSPARSE_CHECK(hipsparseScsrgeam2(handle, m, n, &alpha, descrA, nnzA, dcsrValA, dcsrRowPtrA, dcsrColIndA, &beta, descrB, nnzB, dcsrValB, dcsrRowPtrB, dcsrColIndB, descrC, dcsrValC, dcsrRowPtrC, dcsrColIndC, dbuffer)); std::vector<int> hcsrRowPtrC(m + 1); std::vector<int> hcsrColIndC(nnzC); std::vector<float> hcsrValC(nnzC); // Copy back to the host HIP_CHECK( hipMemcpy(hcsrRowPtrC.data(), dcsrRowPtrC, sizeof(int) * (m + 1), hipMemcpyDeviceToHost)); HIP_CHECK( hipMemcpy(hcsrColIndC.data(), dcsrColIndC, sizeof(int) * nnzC, hipMemcpyDeviceToHost)); HIP_CHECK(hipMemcpy(hcsrValC.data(), dcsrValC, sizeof(float) * nnzC, hipMemcpyDeviceToHost)); std::cout << "C" << std::endl; for(int i = 0; i < m; i++) { int start = hcsrRowPtrC[i]; int end = hcsrRowPtrC[i + 1]; std::vector<float> temp(n, 0.0f); for(int j = start; j < end; j++) { temp[hcsrColIndC[j]] = hcsrValC[j]; } for(int j = 0; j < n; j++) { std::cout << temp[j] << " "; } std::cout << "" << std::endl; } std::cout << "" << std::endl; HIP_CHECK(hipFree(dcsrRowPtrA)); HIP_CHECK(hipFree(dcsrColIndA)); HIP_CHECK(hipFree(dcsrValA)); HIP_CHECK(hipFree(dcsrRowPtrB)); HIP_CHECK(hipFree(dcsrColIndB)); HIP_CHECK(hipFree(dcsrValB)); HIP_CHECK(hipFree(dcsrRowPtrC)); HIP_CHECK(hipFree(dcsrColIndC)); HIP_CHECK(hipFree(dcsrValC)); HIP_CHECK(hipFree(dbuffer)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(descrA)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(descrB)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(descrC)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); return 0; }


Note

Both scalars \(\alpha\) and \(beta\) have to be valid.

Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix \(A\), \(B\) and \(C\).**n**–**[in]**number of columns of the sparse CSR matrix \(A\), \(B\) and \(C\).**alpha**–**[in]**scalar \(\alpha\).**descrA**–**[in]**descriptor of the sparse CSR matrix \(A\). Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**nnzA**–**[in]**number of non-zero entries of the sparse CSR matrix \(A\).**csrSortedValA**–**[in]**array of`nnzA`

elements of the sparse CSR matrix \(A\).**csrSortedRowPtrA**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(A\).**csrSortedColIndA**–**[in]**array of`nnzA`

elements containing the column indices of the sparse CSR matrix \(A\).**beta**–**[in]**scalar \(\beta\).**descrB**–**[in]**descriptor of the sparse CSR matrix \(B\). Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**nnzB**–**[in]**number of non-zero entries of the sparse CSR matrix \(B\).**csrSortedValB**–**[in]**array of`nnzB`

elements of the sparse CSR matrix \(B\).**csrSortedRowPtrB**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(B\).**csrSortedColIndB**–**[in]**array of`nnzB`

elements containing the column indices of the sparse CSR matrix \(B\).**descrC**–**[in]**descriptor of the sparse CSR matrix \(C\). Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**csrSortedValC**–**[out]**array of elements of the sparse CSR matrix \(C\).**csrSortedRowPtrC**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(C\).**csrSortedColIndC**–**[out]**array of elements containing the column indices of the sparse CSR matrix \(C\).**pBuffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`nnzA`

,`nnzB`

,`alpha`

,`descrA`

,`csrSortedValA`

,`csrSortedRowPtrA`

,`csrSortedColIndA`

,`beta`

,`descrB`

,`csrSortedValB`

,`csrSortedRowPtrB`

,`csrSortedColIndB`

,`descrC`

,`csrSortedValC`

,`csrSortedRowPtrC`

,`csrSortedColIndC`

or`pBuffer`

is invalid.**HIPSPARSE_STATUS_NOT_SUPPORTED**–[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXcsrgemmNnz()[#](#hipsparsexcsrgemmnnz)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseXcsrgemmNnz([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transB, int m, int n, int k, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, int nnzA, const int *csrRowPtrA, const int *csrColIndA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrB, int nnzB, const int *csrRowPtrB, const int *csrColIndB, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, int *csrRowPtrC, int *nnzTotalDevHostPtr)[#](#_CPPv420hipsparseXcsrgemmNnz17hipsparseHandle_t20hipsparseOperation_t20hipsparseOperation_tiiiK19hipsparseMatDescr_tiPKiPKiK19hipsparseMatDescr_tiPKiPKiK19hipsparseMatDescr_tPiPi) `hipsparseXcsrgemmNnz`

computes the total CSR non-zero elements and the CSR row offsets, that point to the start of every row of the sparse CSR matrix, of the resulting multiplied matrix \(C\). It is assumed that`csrRowPtrC`

has been allocated with size`m+1`

. The desired index base in the output CSR matrix \(C\) is set in the[hipsparseMatDescr_t](types.html#hipsparse-types_8h_1a4c2f3ad3f2057bffb1adf6a8256537b9)`descrC`

. See[hipsparseSetMatIndexBase()](auxiliary.html#hipsparse-auxiliary_8h_1a3c81b4bd7b1e9bb04a63a620f51dc2a8).Note

As indicated,

`nnzTotalDevHostPtr`

can point either to host or device memory. This is controlled by setting the pointer mode. See[hipsparseSetPointerMode()](auxiliary.html#hipsparse-auxiliary_8h_1a7d876174f77e1f8f816781af1c3c667c).Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

Please note, that for matrix products with more than 8192 intermediate products per row, additional temporary storage buffer is allocated by the algorithm.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**transA**–**[in]**matrix \(A\) operation type.**transB**–**[in]**matrix \(B\) operation type.**m**–**[in]**number of rows of the sparse CSR matrix \(op(A)\) and \(C\).**n**–**[in]**number of columns of the sparse CSR matrix \(op(B)\) and \(C\).**k**–**[in]**number of columns of the sparse CSR matrix \(op(A)\) and number of rows of the sparse CSR matrix \(op(B)\).**descrA**–**[in]**descriptor of the sparse CSR matrix \(A\). Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**nnzA**–**[in]**number of non-zero entries of the sparse CSR matrix \(A\).**csrRowPtrA**–**[in]**array of`m+1`

elements ( \(op(A) == A\),`k+1`

otherwise) that point to the start of every row of the sparse CSR matrix \(op(A)\).**csrColIndA**–**[in]**array of`nnzA`

elements containing the column indices of the sparse CSR matrix \(A\).**descrB**–**[in]**descriptor of the sparse CSR matrix \(B\). Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**nnzB**–**[in]**number of non-zero entries of the sparse CSR matrix \(B\).**csrRowPtrB**–**[in]**array of`k+1`

elements ( \(op(B) == B\),`m+1`

otherwise) that point to the start of every row of the sparse CSR matrix \(op(B)\).**csrColIndB**–**[in]**array of`nnzB`

elements containing the column indices of the sparse CSR matrix \(B\).**descrC**–**[in]**descriptor of the sparse CSR matrix \(C\). Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**csrRowPtrC**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(C\).**nnzTotalDevHostPtr**–**[inout]**pointer to the number of non-zero entries of the sparse CSR matrix \(C\).`nnzTotalDevHostPtr`

can be a host or device pointer.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`k`

,`nnzA`

,`nnzB`

,`nnzC`

,`descrA`

,`csrRowPtrA`

,`csrColIndA`

,`descrB`

,`csrRowPtrB`

,`csrColIndB`

,`descrC`

,`csrRowPtrC`

or`nnzTotalDevHostPtr`

is invalid.**HIPSPARSE_STATUS_MATRIX_TYPE_NOT_SUPPORTED**–`transA`

!=[HIPSPARSE_OPERATION_NON_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141a270f0124eb0d0ac15c3e7afb18064547),`transB`

!=[HIPSPARSE_OPERATION_NON_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141a270f0124eb0d0ac15c3e7afb18064547), or[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXcsrgemm()[#](#hipsparsexcsrgemm)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseScsrgemm([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transB, int m, int n, int k, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, int nnzA, const float *csrValA, const int *csrRowPtrA, const int *csrColIndA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrB, int nnzB, const float *csrValB, const int *csrRowPtrB, const int *csrColIndB, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, float *csrValC, const int *csrRowPtrC, int *csrColIndC)[#](#_CPPv417hipsparseScsrgemm17hipsparseHandle_t20hipsparseOperation_t20hipsparseOperation_tiiiK19hipsparseMatDescr_tiPKfPKiPKiK19hipsparseMatDescr_tiPKfPKiPKiK19hipsparseMatDescr_tPfPKiPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDcsrgemm([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transB, int m, int n, int k, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, int nnzA, const double *csrValA, const int *csrRowPtrA, const int *csrColIndA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrB, int nnzB, const double *csrValB, const int *csrRowPtrB, const int *csrColIndB, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, double *csrValC, const int *csrRowPtrC, int *csrColIndC)[#](#_CPPv417hipsparseDcsrgemm17hipsparseHandle_t20hipsparseOperation_t20hipsparseOperation_tiiiK19hipsparseMatDescr_tiPKdPKiPKiK19hipsparseMatDescr_tiPKdPKiPKiK19hipsparseMatDescr_tPdPKiPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCcsrgemm([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transB, int m, int n, int k, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, int nnzA, const hipComplex *csrValA, const int *csrRowPtrA, const int *csrColIndA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrB, int nnzB, const hipComplex *csrValB, const int *csrRowPtrB, const int *csrColIndB, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, hipComplex *csrValC, const int *csrRowPtrC, int *csrColIndC)[#](#_CPPv417hipsparseCcsrgemm17hipsparseHandle_t20hipsparseOperation_t20hipsparseOperation_tiiiK19hipsparseMatDescr_tiPK10hipComplexPKiPKiK19hipsparseMatDescr_tiPK10hipComplexPKiPKiK19hipsparseMatDescr_tP10hipComplexPKiPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZcsrgemm([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)transB, int m, int n, int k, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, int nnzA, const hipDoubleComplex *csrValA, const int *csrRowPtrA, const int *csrColIndA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrB, int nnzB, const hipDoubleComplex *csrValB, const int *csrRowPtrB, const int *csrColIndB, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, hipDoubleComplex *csrValC, const int *csrRowPtrC, int *csrColIndC)[#](#_CPPv417hipsparseZcsrgemm17hipsparseHandle_t20hipsparseOperation_t20hipsparseOperation_tiiiK19hipsparseMatDescr_tiPK16hipDoubleComplexPKiPKiK19hipsparseMatDescr_tiPK16hipDoubleComplexPKiPKiK19hipsparseMatDescr_tP16hipDoubleComplexPKiPi) Sparse matrix sparse matrix multiplication using CSR storage format.

`hipsparseXcsrgemm`

multiplies the sparse \(m \times k\) matrix \(op(A)\), defined in CSR storage format with the sparse \(k \times n\) matrix \(op(B)\), defined in CSR storage format, and stores the result in the sparse \(m \times n\) matrix \(C\), defined in CSR storage format, such that\[ C := op(A) \cdot op(B), \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if transA == HIPSPARSE_OPERATION_NON_TRANSPOSE} \\ A^T, & \text{if transA == HIPSPARSE_OPERATION_TRANSPOSE} \\ A^H, & \text{if transA == HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE} \end{array} \right. \end{split}\]and\[\begin{split} op(B) = \left\{ \begin{array}{ll} B, & \text{if transB == HIPSPARSE_OPERATION_NON_TRANSPOSE} \\ B^T, & \text{if transB == HIPSPARSE_OPERATION_TRANSPOSE} \\ B^H, & \text{if transB == HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE} \end{array} \right. \end{split}\]This computation involves a multi step process. First the user must allocate

`csrRowPtrC`

to have size`m+1`

. The user then calls[hipsparseXcsrgemmNnz](#hipsparse__csrgemm_8h_1af84d1c00a2fef2309fc6114626d4de60)which fills in the`csrRowPtrC`

array as well as computes the total number of nonzeros in C,`nnzC`

. The user then allocates both arrays`csrColIndC`

and`csrValC`

to have size`nnzC`

and calls`hipsparseXcsrgemm`

to complete the computation. The desired index base in the output CSR matrix C is set in the[hipsparseMatDescr_t](types.html#hipsparse-types_8h_1a4c2f3ad3f2057bffb1adf6a8256537b9)`descrC`

. See[hipsparseSetMatIndexBase()](auxiliary.html#hipsparse-auxiliary_8h_1a3c81b4bd7b1e9bb04a63a620f51dc2a8).**Example**int main(int argc, char* argv[]) { const int m = 4; const int k = 3; const int n = 2; const int nnzA = 7; const int nnzB = 3; hipsparseOperation_t transA = HIPSPARSE_OPERATION_NON_TRANSPOSE; hipsparseOperation_t transB = HIPSPARSE_OPERATION_NON_TRANSPOSE; // A, B, and C are mxk, kxn, and m×n // A // 1 0 0 // 3 4 0 // 5 6 7 // 0 0 9 std::vector<int> hcsrRowPtrA = {0, 1, 3, 6, 7}; std::vector<int> hcsrColIndA = {0, 0, 1, 0, 1, 2, 2}; std::vector<float> hcsrValA = {1.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 9.0f}; // B // 0 1 // 1 0 // 0 1 std::vector<int> hcsrRowPtrB = {0, 1, 2, 3}; std::vector<int> hcsrColIndB = {1, 0, 1}; std::vector<float> hcsrValB = {1.0f, 1.0f, 1.0f}; // Device memory management: Allocate and copy A, B int* dcsrRowPtrA; int* dcsrColIndA; float* dcsrValA; int* dcsrRowPtrB; int* dcsrColIndB; float* dcsrValB; int* dcsrRowPtrC; HIP_CHECK(hipMalloc((void**)&dcsrRowPtrA, (m + 1) * sizeof(int))); HIP_CHECK(hipMalloc((void**)&dcsrColIndA, nnzA * sizeof(int))); HIP_CHECK(hipMalloc((void**)&dcsrValA, nnzA * sizeof(float))); HIP_CHECK(hipMalloc((void**)&dcsrRowPtrB, (m + 1) * sizeof(int))); HIP_CHECK(hipMalloc((void**)&dcsrColIndB, nnzB * sizeof(int))); HIP_CHECK(hipMalloc((void**)&dcsrValB, nnzB * sizeof(float))); HIP_CHECK(hipMalloc((void**)&dcsrRowPtrC, (m + 1) * sizeof(int))); HIP_CHECK( hipMemcpy(dcsrRowPtrA, hcsrRowPtrA.data(), (m + 1) * sizeof(int), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsrColIndA, hcsrColIndA.data(), nnzA * sizeof(int), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrValA, hcsrValA.data(), nnzA * sizeof(float), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsrRowPtrB, hcsrRowPtrB.data(), (m + 1) * sizeof(int), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsrColIndB, hcsrColIndB.data(), nnzB * sizeof(int), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrValB, hcsrValB.data(), nnzB * sizeof(float), hipMemcpyHostToDevice)); hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); hipsparseMatDescr_t descrA; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&descrA)); hipsparseMatDescr_t descrB; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&descrB)); hipsparseMatDescr_t descrC; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&descrC)); int nnzC; HIPSPARSE_CHECK(hipsparseXcsrgemmNnz(handle, transA, transB, m, n, k, descrA, nnzA, dcsrRowPtrA, dcsrColIndA, descrB, nnzB, dcsrRowPtrB, dcsrColIndB, descrC, dcsrRowPtrC, &nnzC)); int* dcsrColIndC = nullptr; float* dcsrValC = nullptr; HIP_CHECK(hipMalloc((void**)&dcsrColIndC, sizeof(int) * nnzC)); HIP_CHECK(hipMalloc((void**)&dcsrValC, sizeof(float) * nnzC)); HIPSPARSE_CHECK(hipsparseScsrgemm(handle, transA, transB, m, n, k, descrA, nnzA, dcsrValA, dcsrRowPtrA, dcsrColIndA, descrB, nnzB, dcsrValB, dcsrRowPtrB, dcsrColIndB, descrC, dcsrValC, dcsrRowPtrC, dcsrColIndC)); std::vector<int> hcsrRowPtrC(m + 1); std::vector<int> hcsrColIndC(nnzC); std::vector<float> hcsrValC(nnzC); // Copy back to the host HIP_CHECK( hipMemcpy(hcsrRowPtrC.data(), dcsrRowPtrC, sizeof(int) * (m + 1), hipMemcpyDeviceToHost)); HIP_CHECK( hipMemcpy(hcsrColIndC.data(), dcsrColIndC, sizeof(int) * nnzC, hipMemcpyDeviceToHost)); HIP_CHECK(hipMemcpy(hcsrValC.data(), dcsrValC, sizeof(float) * nnzC, hipMemcpyDeviceToHost)); std::cout << "C" << std::endl; for(int i = 0; i < m; i++) { int start = hcsrRowPtrC[i]; int end = hcsrRowPtrC[i + 1]; std::vector<float> temp(n, 0.0f); for(int j = start; j < end; j++) { temp[hcsrColIndC[j]] = hcsrValC[j]; } for(int j = 0; j < n; j++) { std::cout << temp[j] << " "; } std::cout << "" << std::endl; } std::cout << "" << std::endl; HIP_CHECK(hipFree(dcsrRowPtrA)); HIP_CHECK(hipFree(dcsrColIndA)); HIP_CHECK(hipFree(dcsrValA)); HIP_CHECK(hipFree(dcsrRowPtrB)); HIP_CHECK(hipFree(dcsrColIndB)); HIP_CHECK(hipFree(dcsrValB)); HIP_CHECK(hipFree(dcsrRowPtrC)); HIP_CHECK(hipFree(dcsrColIndC)); HIP_CHECK(hipFree(dcsrValC)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(descrA)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(descrB)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(descrC)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

Please note, that for matrix products with more than 4096 non-zero entries per row, additional temporary storage buffer is allocated by the algorithm.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**transA**–**[in]**matrix \(A\) operation type.**transB**–**[in]**matrix \(B\) operation type.**m**–**[in]**number of rows of the sparse CSR matrix \(op(A)\) and \(C\).**n**–**[in]**number of columns of the sparse CSR matrix \(op(B)\) and \(C\).**k**–**[in]**number of columns of the sparse CSR matrix \(op(A)\) and number of rows of the sparse CSR matrix \(op(B)\).**descrA**–**[in]**descriptor of the sparse CSR matrix \(A\). Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**nnzA**–**[in]**number of non-zero entries of the sparse CSR matrix \(A\).**csrValA**–**[in]**array of`nnzA`

elements of the sparse CSR matrix \(A\).**csrRowPtrA**–**[in]**array of`m+1`

elements ( \(op(A) == A\),`k+1`

otherwise) that point to the start of every row of the sparse CSR matrix \(op(A)\).**csrColIndA**–**[in]**array of`nnzA`

elements containing the column indices of the sparse CSR matrix \(A\).**descrB**–**[in]**descriptor of the sparse CSR matrix \(B\). Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**nnzB**–**[in]**number of non-zero entries of the sparse CSR matrix \(B\).**csrValB**–**[in]**array of`nnzB`

elements of the sparse CSR matrix \(B\).**csrRowPtrB**–**[in]**array of`k+1`

elements ( \(op(B) == B\),`m+1`

otherwise) that point to the start of every row of the sparse CSR matrix \(op(B)\).**csrColIndB**–**[in]**array of`nnzB`

elements containing the column indices of the sparse CSR matrix \(B\).**descrC**–**[in]**descriptor of the sparse CSR matrix \(C\). Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**csrValC**–**[out]**array of`nnzC`

elements of the sparse CSR matrix \(C\).**csrRowPtrC**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(C\).**csrColIndC**–**[out]**array of`nnzC`

elements containing the column indices of the sparse CSR matrix \(C\).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`k`

,`nnzA`

,`nnzB`

,`descrA`

,`csrValA`

,`csrRowPtrA`

,`csrColIndA`

,`descrB`

,`csrValB`

,`csrRowPtrB`

,`csrColIndB`

,`descrC`

,`csrValC`

,`csrRowPtrC`

,`csrColIndC`

is invalid.**HIPSPARSE_STATUS_ALLOC_FAILED**– additional buffer for long rows could not be allocated.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`transA`

!=[HIPSPARSE_OPERATION_NON_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141a270f0124eb0d0ac15c3e7afb18064547),`transB`

!=[HIPSPARSE_OPERATION_NON_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141a270f0124eb0d0ac15c3e7afb18064547), or[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXcsrgemm2_bufferSizeExt()[#](#hipsparsexcsrgemm2-buffersizeext)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseScsrgemm2_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int k, const float *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, int nnzA, const int *csrRowPtrA, const int *csrColIndA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrB, int nnzB, const int *csrRowPtrB, const int *csrColIndB, const float *beta, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrD, int nnzD, const int *csrRowPtrD, const int *csrColIndD,[csrgemm2Info_t](types.html#_CPPv414csrgemm2Info_t)info, size_t *pBufferSizeInBytes)[#](#_CPPv432hipsparseScsrgemm2_bufferSizeExt17hipsparseHandle_tiiiPKfK19hipsparseMatDescr_tiPKiPKiK19hipsparseMatDescr_tiPKiPKiPKfK19hipsparseMatDescr_tiPKiPKi14csrgemm2Info_tP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDcsrgemm2_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int k, const double *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, int nnzA, const int *csrRowPtrA, const int *csrColIndA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrB, int nnzB, const int *csrRowPtrB, const int *csrColIndB, const double *beta, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrD, int nnzD, const int *csrRowPtrD, const int *csrColIndD,[csrgemm2Info_t](types.html#_CPPv414csrgemm2Info_t)info, size_t *pBufferSizeInBytes)[#](#_CPPv432hipsparseDcsrgemm2_bufferSizeExt17hipsparseHandle_tiiiPKdK19hipsparseMatDescr_tiPKiPKiK19hipsparseMatDescr_tiPKiPKiPKdK19hipsparseMatDescr_tiPKiPKi14csrgemm2Info_tP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCcsrgemm2_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int k, const hipComplex *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, int nnzA, const int *csrRowPtrA, const int *csrColIndA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrB, int nnzB, const int *csrRowPtrB, const int *csrColIndB, const hipComplex *beta, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrD, int nnzD, const int *csrRowPtrD, const int *csrColIndD,[csrgemm2Info_t](types.html#_CPPv414csrgemm2Info_t)info, size_t *pBufferSizeInBytes)[#](#_CPPv432hipsparseCcsrgemm2_bufferSizeExt17hipsparseHandle_tiiiPK10hipComplexK19hipsparseMatDescr_tiPKiPKiK19hipsparseMatDescr_tiPKiPKiPK10hipComplexK19hipsparseMatDescr_tiPKiPKi14csrgemm2Info_tP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZcsrgemm2_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int k, const hipDoubleComplex *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, int nnzA, const int *csrRowPtrA, const int *csrColIndA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrB, int nnzB, const int *csrRowPtrB, const int *csrColIndB, const hipDoubleComplex *beta, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrD, int nnzD, const int *csrRowPtrD, const int *csrColIndD,[csrgemm2Info_t](types.html#_CPPv414csrgemm2Info_t)info, size_t *pBufferSizeInBytes)[#](#_CPPv432hipsparseZcsrgemm2_bufferSizeExt17hipsparseHandle_tiiiPK16hipDoubleComplexK19hipsparseMatDescr_tiPKiPKiK19hipsparseMatDescr_tiPKiPKiPK16hipDoubleComplexK19hipsparseMatDescr_tiPKiPKi14csrgemm2Info_tP6size_t) `hipsparseXcsrgemm2_bufferSizeExt`

returns the size of the temporary storage buffer in bytes that is required by[hipsparseXcsrgemm2Nnz()](#hipsparse__csrgemm_8h_1a6a9ad055ef2698ae82a819363e2be0fa)and[hipsparseXcsrgemm2()](#hipsparse__csrgemm_8h_1a3cd3c5f29897ec4ad5ba0512cd4b6d47). The temporary storage buffer must be allocated by the user.Note

Please note, that for matrix products with more than 4096 non-zero entries per row, additional temporary storage buffer is allocated by the algorithm.

Note

Please note, that for matrix products with more than 8192 intermediate products per row, additional temporary storage buffer is allocated by the algorithm.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix \(op(A)\) and \(C\).**n**–**[in]**number of columns of the sparse CSR matrix \(op(B)\) and \(C\).**k**–**[in]**number of columns of the sparse CSR matrix \(op(A)\) and number of rows of the sparse CSR matrix \(op(B)\).**alpha**–**[in]**scalar \(\alpha\).**descrA**–**[in]**descriptor of the sparse CSR matrix \(A\). Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**nnzA**–**[in]**number of non-zero entries of the sparse CSR matrix \(A\).**csrRowPtrA**–**[in]**array of`m+1`

elements ( \(op(A) == A\),`k+1`

otherwise) that point to the start of every row of the sparse CSR matrix \(op(A)\).**csrColIndA**–**[in]**array of`nnzA`

elements containing the column indices of the sparse CSR matrix \(A\).**descrB**–**[in]**descriptor of the sparse CSR matrix \(B\). Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**nnzB**–**[in]**number of non-zero entries of the sparse CSR matrix \(B\).**csrRowPtrB**–**[in]**array of`k+1`

elements ( \(op(B) == B\),`m+1`

otherwise) that point to the start of every row of the sparse CSR matrix \(op(B)\).**csrColIndB**–**[in]**array of`nnzB`

elements containing the column indices of the sparse CSR matrix \(B\).**beta**–**[in]**scalar \(\beta\).**descrD**–**[in]**descriptor of the sparse CSR matrix \(D\). Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**nnzD**–**[in]**number of non-zero entries of the sparse CSR matrix \(D\).**csrRowPtrD**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(D\).**csrColIndD**–**[in]**array of`nnzD`

elements containing the column indices of the sparse CSR matrix \(D\).**info**–**[inout]**structure that holds meta data for the sparse CSR matrix \(C\).**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer required by[hipsparseXcsrgemm2Nnz()](#hipsparse__csrgemm_8h_1a6a9ad055ef2698ae82a819363e2be0fa),[hipsparseScsrgemm2()](#hipsparse__csrgemm_8h_1a3cd3c5f29897ec4ad5ba0512cd4b6d47),[hipsparseDcsrgemm2()](#hipsparse__csrgemm_8h_1af278b41ed3a7fee0d7bc959a8d29de2f),[hipsparseCcsrgemm2()](#hipsparse__csrgemm_8h_1a3bf0c8b6c50dce094f814e70c9f5fad0)and[hipsparseZcsrgemm2()](#hipsparse__csrgemm_8h_1a04eb4177dce7fa526c903b87ae2c95bb).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`k`

,`nnzA`

,`nnzB`

,`nnz_D`

,`alpha`

,`beta`

,`descrA`

,`csrRowPtrA`

,`csrColIndA`

,`descrB`

,`csrRowPtrB`

,`csrColIndB`

,`descrD`

,`csrRowPtrD`

,`csrColIndD`

,`info`

or`pBufferSizeInBytes`

is invalid.**HIPSPARSE_STATUS_NOT_SUPPORTED**–[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXcsrgemm2Nnz()[#](#hipsparsexcsrgemm2nnz)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseXcsrgemm2Nnz([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int k, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, int nnzA, const int *csrRowPtrA, const int *csrColIndA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrB, int nnzB, const int *csrRowPtrB, const int *csrColIndB, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrD, int nnzD, const int *csrRowPtrD, const int *csrColIndD, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, int *csrRowPtrC, int *nnzTotalDevHostPtr, const[csrgemm2Info_t](types.html#_CPPv414csrgemm2Info_t)info, void *pBuffer)[#](#_CPPv421hipsparseXcsrgemm2Nnz17hipsparseHandle_tiiiK19hipsparseMatDescr_tiPKiPKiK19hipsparseMatDescr_tiPKiPKiK19hipsparseMatDescr_tiPKiPKiK19hipsparseMatDescr_tPiPiK14csrgemm2Info_tPv) `hipsparseXcsrgemm2Nnz`

computes the total CSR non-zero elements and the CSR row offsets, that point to the start of every row of the sparse CSR matrix, of the resulting multiplied matrix \(C\). It is assumed that`csrRowPtrC`

has been allocated with size`m+1`

. The required buffer size can be obtained by[hipsparseXcsrgemm2_bufferSizeExt()](#hipsparse__csrgemm_8h_1a9f570232697e2acfacd584ea74513db1). The desired index base in the output CSR matrix \(C\) is set in the[hipsparseMatDescr_t](types.html#hipsparse-types_8h_1a4c2f3ad3f2057bffb1adf6a8256537b9)`descrC`

. See[hipsparseSetMatIndexBase()](auxiliary.html#hipsparse-auxiliary_8h_1a3c81b4bd7b1e9bb04a63a620f51dc2a8).Note

As indicated,

`nnzTotalDevHostPtr`

can point either to host or device memory. This is controlled by setting the pointer mode. See[hipsparseSetPointerMode()](auxiliary.html#hipsparse-auxiliary_8h_1a7d876174f77e1f8f816781af1c3c667c).Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

Please note, that for matrix products with more than 8192 intermediate products per row, additional temporary storage buffer is allocated by the algorithm.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix \(op(A)\) and \(C\).**n**–**[in]**number of columns of the sparse CSR matrix \(op(B)\) and \(C\).**k**–**[in]**number of columns of the sparse CSR matrix \(op(A)\) and number of rows of the sparse CSR matrix \(op(B)\).**descrA**–**[in]**descriptor of the sparse CSR matrix \(A\). Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**nnzA**–**[in]**number of non-zero entries of the sparse CSR matrix \(A\).**csrRowPtrA**–**[in]**array of`m+1`

elements ( \(op(A) == A\),`k+1`

otherwise) that point to the start of every row of the sparse CSR matrix \(op(A)\).**csrColIndA**–**[in]**array of`nnzA`

elements containing the column indices of the sparse CSR matrix \(A\).**descrB**–**[in]**descriptor of the sparse CSR matrix \(B\). Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**nnzB**–**[in]**number of non-zero entries of the sparse CSR matrix \(B\).**csrRowPtrB**–**[in]**array of`k+1`

elements ( \(op(B) == B\),`m+1`

otherwise) that point to the start of every row of the sparse CSR matrix \(op(B)\).**csrColIndB**–**[in]**array of`nnzB`

elements containing the column indices of the sparse CSR matrix \(B\).**descrD**–**[in]**descriptor of the sparse CSR matrix \(D\). Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**nnzD**–**[in]**number of non-zero entries of the sparse CSR matrix \(D\).**csrRowPtrD**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(D\).**csrColIndD**–**[in]**array of`nnzD`

elements containing the column indices of the sparse CSR matrix \(D\).**descrC**–**[in]**descriptor of the sparse CSR matrix \(C\). Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**csrRowPtrC**–**[out]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(C\).**nnzTotalDevHostPtr**–**[out]**pointer to the number of non-zero entries of the sparse CSR matrix \(C\).**info**–**[in]**structure that holds meta data for the sparse CSR matrix \(C\).**pBuffer**–**[in]**temporary storage buffer allocated by the user, size is returned by[hipsparseScsrgemm2_bufferSizeExt()](#hipsparse__csrgemm_8h_1a9f570232697e2acfacd584ea74513db1),[hipsparseDcsrgemm2_bufferSizeExt()](#hipsparse__csrgemm_8h_1a3325f5f8b018d8f73418be9e6e57f860),[hipsparseZcsrgemm2_bufferSizeExt()](#hipsparse__csrgemm_8h_1a2fe91e2dbb1c17edc7cbb2e473a5b1e5)or[hipsparseZcsrgemm2_bufferSizeExt()](#hipsparse__csrgemm_8h_1a2fe91e2dbb1c17edc7cbb2e473a5b1e5).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`k`

,`nnzA`

,`nnzB`

,`nnzD`

,`descrA`

,`csrRowPtrA`

,`csrColIndA`

,`descrB`

,`csrRowPtrB`

,`csrColIndB`

,`descrD`

,`csrRowPtrD`

,`csrColIndD`

,`descrC`

,`csrRowPtrC`

,`nnzTotalDevHostPtr`

,`info`

or`pBuffer`

is invalid.**HIPSPARSE_STATUS_ALLOC_FAILED**– additional buffer for long rows could not be allocated.**HIPSPARSE_STATUS_NOT_SUPPORTED**–[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXcsrgemm2()[#](#hipsparsexcsrgemm2)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseScsrgemm2([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int k, const float *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, int nnzA, const float *csrValA, const int *csrRowPtrA, const int *csrColIndA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrB, int nnzB, const float *csrValB, const int *csrRowPtrB, const int *csrColIndB, const float *beta, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrD, int nnzD, const float *csrValD, const int *csrRowPtrD, const int *csrColIndD, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, float *csrValC, const int *csrRowPtrC, int *csrColIndC, const[csrgemm2Info_t](types.html#_CPPv414csrgemm2Info_t)info, void *pBuffer)[#](#_CPPv418hipsparseScsrgemm217hipsparseHandle_tiiiPKfK19hipsparseMatDescr_tiPKfPKiPKiK19hipsparseMatDescr_tiPKfPKiPKiPKfK19hipsparseMatDescr_tiPKfPKiPKiK19hipsparseMatDescr_tPfPKiPiK14csrgemm2Info_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDcsrgemm2([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int k, const double *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, int nnzA, const double *csrValA, const int *csrRowPtrA, const int *csrColIndA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrB, int nnzB, const double *csrValB, const int *csrRowPtrB, const int *csrColIndB, const double *beta, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrD, int nnzD, const double *csrValD, const int *csrRowPtrD, const int *csrColIndD, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, double *csrValC, const int *csrRowPtrC, int *csrColIndC, const[csrgemm2Info_t](types.html#_CPPv414csrgemm2Info_t)info, void *pBuffer)[#](#_CPPv418hipsparseDcsrgemm217hipsparseHandle_tiiiPKdK19hipsparseMatDescr_tiPKdPKiPKiK19hipsparseMatDescr_tiPKdPKiPKiPKdK19hipsparseMatDescr_tiPKdPKiPKiK19hipsparseMatDescr_tPdPKiPiK14csrgemm2Info_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCcsrgemm2([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int k, const hipComplex *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, int nnzA, const hipComplex *csrValA, const int *csrRowPtrA, const int *csrColIndA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrB, int nnzB, const hipComplex *csrValB, const int *csrRowPtrB, const int *csrColIndB, const hipComplex *beta, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrD, int nnzD, const hipComplex *csrValD, const int *csrRowPtrD, const int *csrColIndD, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, hipComplex *csrValC, const int *csrRowPtrC, int *csrColIndC, const[csrgemm2Info_t](types.html#_CPPv414csrgemm2Info_t)info, void *pBuffer)[#](#_CPPv418hipsparseCcsrgemm217hipsparseHandle_tiiiPK10hipComplexK19hipsparseMatDescr_tiPK10hipComplexPKiPKiK19hipsparseMatDescr_tiPK10hipComplexPKiPKiPK10hipComplexK19hipsparseMatDescr_tiPK10hipComplexPKiPKiK19hipsparseMatDescr_tP10hipComplexPKiPiK14csrgemm2Info_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZcsrgemm2([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, int k, const hipDoubleComplex *alpha, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, int nnzA, const hipDoubleComplex *csrValA, const int *csrRowPtrA, const int *csrColIndA, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrB, int nnzB, const hipDoubleComplex *csrValB, const int *csrRowPtrB, const int *csrColIndB, const hipDoubleComplex *beta, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrD, int nnzD, const hipDoubleComplex *csrValD, const int *csrRowPtrD, const int *csrColIndD, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrC, hipDoubleComplex *csrValC, const int *csrRowPtrC, int *csrColIndC, const[csrgemm2Info_t](types.html#_CPPv414csrgemm2Info_t)info, void *pBuffer)[#](#_CPPv418hipsparseZcsrgemm217hipsparseHandle_tiiiPK16hipDoubleComplexK19hipsparseMatDescr_tiPK16hipDoubleComplexPKiPKiK19hipsparseMatDescr_tiPK16hipDoubleComplexPKiPKiPK16hipDoubleComplexK19hipsparseMatDescr_tiPK16hipDoubleComplexPKiPKiK19hipsparseMatDescr_tP16hipDoubleComplexPKiPiK14csrgemm2Info_tPv) Sparse matrix sparse matrix multiplication using CSR storage format.

`hipsparseXcsrgemm2`

multiplies the scalar \(\alpha\) with the sparse \(m \times k\) matrix \(A\), defined in CSR storage format, and the sparse \(k \times n\) matrix \(B\), defined in CSR storage format, and adds the result to the sparse \(m \times n\) matrix \(D\) that is multiplied by \(\beta\). The final result is stored in the sparse \(m \times n\) matrix \(C\), defined in CSR storage format, such that\[ C := \alpha \cdot A \cdot B + \beta \cdot D \]This computation involves a multi step process. First the user must call

[hipsparseXcsrgemm2_bufferSizeExt()](#hipsparse__csrgemm_8h_1a9f570232697e2acfacd584ea74513db1)in order to determine the required user allocated temporary buffer size. The user then allocates this buffer and also allocates`csrRowPtrC`

to have size`m+1`

. Both the temporary storage buffer and`csrRowPtrC`

array are then passed to[hipsparseXcsrgemm2Nnz](#hipsparse__csrgemm_8h_1a6a9ad055ef2698ae82a819363e2be0fa)which fills in the`csrRowPtrC`

array as well as computes the total number of nonzeros in C,`nnzC`

. The user then allocates both arrays`csrColIndC`

and`csrValC`

to have size`nnzC`

and calls`hipsparseXcsrgemm2`

to complete the computation. The desired index base in the output CSR matrix C is set in the[hipsparseMatDescr_t](types.html#hipsparse-types_8h_1a4c2f3ad3f2057bffb1adf6a8256537b9)`descrC`

. See[hipsparseSetMatIndexBase()](auxiliary.html#hipsparse-auxiliary_8h_1a3c81b4bd7b1e9bb04a63a620f51dc2a8).**Example**int main(int argc, char* argv[]) { int m = 4; int k = 3; int n = 2; int nnzA = 7; int nnzB = 3; int nnzD = 6; float alpha{1.0f}; float beta{1.0f}; // A, B, and C are mxk, kxn, and m×n // A // 1 0 0 // 3 4 0 // 5 6 7 // 0 0 9 std::vector<int> hcsrRowPtrA = {0, 1, 3, 6, 7}; std::vector<int> hcsrColIndA = {0, 0, 1, 0, 1, 2, 2}; std::vector<float> hcsrValA = {1.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 9.0f}; // B // 0 1 // 1 0 // 0 1 std::vector<int> hcsrRowPtrB = {0, 1, 2, 3}; std::vector<int> hcsrColIndB = {1, 0, 1}; std::vector<float> hcsrValB = {1.0f, 1.0f, 1.0f}; // D // 0 1 // 2 3 // 4 5 // 0 6 std::vector<int> hcsrRowPtrD = {0, 1, 3, 5, 6}; std::vector<int> hcsrColIndD = {1, 0, 1, 0, 1, 1}; std::vector<float> hcsrValD = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f}; // Device memory management: Allocate and copy A, B int* dcsrRowPtrA; int* dcsrColIndA; float* dcsrValA; int* dcsrRowPtrB; int* dcsrColIndB; float* dcsrValB; int* dcsrRowPtrD; int* dcsrColIndD; float* dcsrValD; int* dcsrRowPtrC; HIP_CHECK(hipMalloc((void**)&dcsrRowPtrA, (m + 1) * sizeof(int))); HIP_CHECK(hipMalloc((void**)&dcsrColIndA, nnzA * sizeof(int))); HIP_CHECK(hipMalloc((void**)&dcsrValA, nnzA * sizeof(float))); HIP_CHECK(hipMalloc((void**)&dcsrRowPtrB, (k + 1) * sizeof(int))); HIP_CHECK(hipMalloc((void**)&dcsrColIndB, nnzB * sizeof(int))); HIP_CHECK(hipMalloc((void**)&dcsrValB, nnzB * sizeof(float))); HIP_CHECK(hipMalloc((void**)&dcsrRowPtrD, (m + 1) * sizeof(int))); HIP_CHECK(hipMalloc((void**)&dcsrColIndD, nnzD * sizeof(int))); HIP_CHECK(hipMalloc((void**)&dcsrValD, nnzD * sizeof(float))); HIP_CHECK(hipMalloc((void**)&dcsrRowPtrC, (m + 1) * sizeof(int))); HIP_CHECK( hipMemcpy(dcsrRowPtrA, hcsrRowPtrA.data(), (m + 1) * sizeof(int), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsrColIndA, hcsrColIndA.data(), nnzA * sizeof(int), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrValA, hcsrValA.data(), nnzA * sizeof(float), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsrRowPtrB, hcsrRowPtrB.data(), (k + 1) * sizeof(int), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsrColIndB, hcsrColIndB.data(), nnzB * sizeof(int), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrValB, hcsrValB.data(), nnzB * sizeof(float), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsrRowPtrD, hcsrRowPtrD.data(), (m + 1) * sizeof(int), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsrColIndD, hcsrColIndD.data(), nnzD * sizeof(int), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrValD, hcsrValD.data(), nnzD * sizeof(float), hipMemcpyHostToDevice)); hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); hipsparseMatDescr_t descrA; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&descrA)); hipsparseMatDescr_t descrB; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&descrB)); hipsparseMatDescr_t descrC; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&descrC)); hipsparseMatDescr_t descrD; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&descrD)); csrgemm2Info_t info; HIPSPARSE_CHECK(hipsparseCreateCsrgemm2Info(&info)); size_t bufferSize; HIPSPARSE_CHECK(hipsparseScsrgemm2_bufferSizeExt(handle, m, n, k, &alpha, descrA, nnzA, dcsrRowPtrA, dcsrColIndA, descrB, nnzB, dcsrRowPtrB, dcsrColIndB, &beta, descrD, nnzD, dcsrRowPtrD, dcsrColIndD, info, &bufferSize)); void* dbuffer = nullptr; HIP_CHECK(hipMalloc((void**)&dbuffer, bufferSize)); int nnzC; HIPSPARSE_CHECK(hipsparseXcsrgemm2Nnz(handle, m, n, k, descrA, nnzA, dcsrRowPtrA, dcsrColIndA, descrB, nnzB, dcsrRowPtrB, dcsrColIndB, descrD, nnzD, dcsrRowPtrD, dcsrColIndD, descrC, dcsrRowPtrC, &nnzC, info, dbuffer)); int* dcsrColIndC = nullptr; float* dcsrValC = nullptr; HIP_CHECK(hipMalloc((void**)&dcsrColIndC, sizeof(int) * nnzC)); HIP_CHECK(hipMalloc((void**)&dcsrValC, sizeof(float) * nnzC)); HIPSPARSE_CHECK(hipsparseScsrgemm2(handle, m, n, k, &alpha, descrA, nnzA, dcsrValA, dcsrRowPtrA, dcsrColIndA, descrB, nnzB, dcsrValB, dcsrRowPtrB, dcsrColIndB, &beta, descrD, nnzD, dcsrValD, dcsrRowPtrD, dcsrColIndD, descrC, dcsrValC, dcsrRowPtrC, dcsrColIndC, info, dbuffer)); std::vector<int> hcsrRowPtrC(m + 1); std::vector<int> hcsrColIndC(nnzC); std::vector<float> hcsrValC(nnzC); // Copy back to the host HIP_CHECK( hipMemcpy(hcsrRowPtrC.data(), dcsrRowPtrC, sizeof(int) * (m + 1), hipMemcpyDeviceToHost)); HIP_CHECK( hipMemcpy(hcsrColIndC.data(), dcsrColIndC, sizeof(int) * nnzC, hipMemcpyDeviceToHost)); HIP_CHECK(hipMemcpy(hcsrValC.data(), dcsrValC, sizeof(float) * nnzC, hipMemcpyDeviceToHost)); std::cout << "C" << std::endl; for(int i = 0; i < m; i++) { int start = hcsrRowPtrC[i]; int end = hcsrRowPtrC[i + 1]; std::vector<float> temp(n, 0.0f); for(int j = start; j < end; j++) { temp[hcsrColIndC[j]] = hcsrValC[j]; } for(int j = 0; j < n; j++) { std::cout << temp[j] << " "; } std::cout << "" << std::endl; } std::cout << "" << std::endl; HIP_CHECK(hipFree(dcsrRowPtrA)); HIP_CHECK(hipFree(dcsrColIndA)); HIP_CHECK(hipFree(dcsrValA)); HIP_CHECK(hipFree(dcsrRowPtrB)); HIP_CHECK(hipFree(dcsrColIndB)); HIP_CHECK(hipFree(dcsrValB)); HIP_CHECK(hipFree(dcsrRowPtrC)); HIP_CHECK(hipFree(dcsrColIndC)); HIP_CHECK(hipFree(dcsrValC)); HIP_CHECK(hipFree(dcsrRowPtrD)); HIP_CHECK(hipFree(dcsrColIndD)); HIP_CHECK(hipFree(dcsrValD)); HIP_CHECK(hipFree(dbuffer)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(descrA)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(descrB)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(descrC)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(descrD)); HIPSPARSE_CHECK(hipsparseDestroyCsrgemm2Info(info)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); return 0; }


Note

If \(\alpha == 0\), then \(C = \beta \cdot D\) will be computed.

Note

If \(\beta == 0\), then \(C = \alpha \cdot A \cdot B\) will be computed.

Note

\(\alpha == beta == 0\) is invalid.

Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

Please note, that for matrix products with more than 4096 non-zero entries per row, additional temporary storage buffer is allocated by the algorithm.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix \(op(A)\) and \(C\).**n**–**[in]**number of columns of the sparse CSR matrix \(op(B)\) and \(C\).**k**–**[in]**number of columns of the sparse CSR matrix \(op(A)\) and number of rows of the sparse CSR matrix \(op(B)\).**alpha**–**[in]**scalar \(\alpha\).**descrA**–**[in]**descriptor of the sparse CSR matrix \(A\). Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**nnzA**–**[in]**number of non-zero entries of the sparse CSR matrix \(A\).**csrValA**–**[in]**array of`nnzA`

elements of the sparse CSR matrix \(A\).**csrRowPtrA**–**[in]**array of`m+1`

elements ( \(op(A) == A\),`k+1`

otherwise) that point to the start of every row of the sparse CSR matrix \(op(A)\).**csrColIndA**–**[in]**array of`nnzA`

elements containing the column indices of the sparse CSR matrix \(A\).**descrB**–**[in]**descriptor of the sparse CSR matrix \(B\). Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**nnzB**–**[in]**number of non-zero entries of the sparse CSR matrix \(B\).**csrValB**–**[in]**array of`nnzB`

elements of the sparse CSR matrix \(B\).**csrRowPtrB**–**[in]**array of`k+1`

elements ( \(op(B) == B\),`m+1`

otherwise) that point to the start of every row of the sparse CSR matrix \(op(B)\).**csrColIndB**–**[in]**array of`nnzB`

elements containing the column indices of the sparse CSR matrix \(B\).**beta**–**[in]**scalar \(\beta\).**descrD**–**[in]**descriptor of the sparse CSR matrix \(D\). Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**nnzD**–**[in]**number of non-zero entries of the sparse CSR matrix \(D\).**csrValD**–**[in]**array of`nnzD`

elements of the sparse CSR matrix \(D\).**csrRowPtrD**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(D\).**csrColIndD**–**[in]**array of`nnzD`

elements containing the column indices of the sparse CSR matrix \(D\).**descrC**–**[in]**descriptor of the sparse CSR matrix \(C\). Currently, only[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)is supported.**csrValC**–**[out]**array of`nnzC`

elements of the sparse CSR matrix \(C\).**csrRowPtrC**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix \(C\).**csrColIndC**–**[out]**array of`nnzC`

elements containing the column indices of the sparse CSR matrix \(C\).**info**–**[in]**structure that holds meta data for the sparse CSR matrix \(C\).**pBuffer**–**[in]**temporary storage buffer allocated by the user, size is returned by[hipsparseScsrgemm2_bufferSizeExt()](#hipsparse__csrgemm_8h_1a9f570232697e2acfacd584ea74513db1),[hipsparseDcsrgemm2_bufferSizeExt()](#hipsparse__csrgemm_8h_1a3325f5f8b018d8f73418be9e6e57f860),[hipsparseCcsrgemm2_bufferSizeExt()](#hipsparse__csrgemm_8h_1aae78f291bb6febff4804100fc17c3c91)or[hipsparseZcsrgemm2_bufferSizeExt()](#hipsparse__csrgemm_8h_1a2fe91e2dbb1c17edc7cbb2e473a5b1e5).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`k`

,`nnzA`

,`nnzB`

,`nnzD`

,`alpha`

,`beta`

,`descrA`

,`csrValA`

,`csrRowPtrA`

,`csrColIndA`

,`descrB`

,`csrValB`

,`csrRowPtrB`

,`csrColIndB`

,`descrD`

,`csrValD`

,`csrRowPtrD`

,`csrColIndD`

,`csrValC`

,`csrRowPtrC`

,`csrColIndC`

,`info`

or`pBuffer`

is invalid.**HIPSPARSE_STATUS_ALLOC_FAILED**– additional buffer for long rows could not be allocated.**HIPSPARSE_STATUS_NOT_SUPPORTED**–[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).
