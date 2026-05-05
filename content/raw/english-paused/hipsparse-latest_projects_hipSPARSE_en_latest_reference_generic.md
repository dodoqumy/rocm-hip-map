---
title: "Sparse generic functions &#8212; hipSPARSE 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipSPARSE/en/latest/reference/generic.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:09:55.780746+00:00
content_hash: "9b47e7cbb3d5686e"
---

# Sparse generic functions[#](#sparse-generic-functions)

This module contains all sparse generic routines.

The sparse generic routines describe operations that manipulate sparse matrices.

## hipsparseAxpby()[#](#hipsparseaxpby)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseAxpby([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, const void *alpha, hipsparseConstSpVecDescr_t vecX, const void *beta,[hipsparseDnVecDescr_t](types.html#_CPPv421hipsparseDnVecDescr_t)vecY)[#](#_CPPv414hipsparseAxpby17hipsparseHandle_tPKv26hipsparseConstSpVecDescr_tPKv21hipsparseDnVecDescr_t) Scale a sparse vector and add it to a scaled dense vector.

`hipsparseAxpby`

multiplies the sparse vector \(x\) with scalar \(\alpha\) and adds the result to the dense vector \(y\) that is multiplied with scalar \(\beta\), such that\[ y := \alpha \cdot x + \beta \cdot y \]for(i = 0; i < size; ++i) { y[i] = beta * y[i] } for(i = 0; i < nnz; ++i) { y[xInd[i]] += alpha * xVal[i] }

`hipsparseAxpby`

supports the following precision data types for the sparse and dense vectors \(x\) and \(y\) and compute types for the scalars \(\alpha\) and \(\beta\).**Uniform Precisions:**X / Y / compute_type

HIP_R_32F

HIP_R_64F

HIP_C_32F

HIP_C_64F

**Mixed precisions:**X / Y

compute_type

HIP_R_16F

HIP_R_32F

HIP_R_16BF

HIP_R_32F

**Example**int main(int argc, char* argv[]) { // Number of non-zeros of the sparse vector int nnz = 3; // Size of sparse and dense vector int size = 9; // Sparse index vector std::vector<int> hxInd = {0, 3, 5}; // Sparse value vector std::vector<float> hxVal = {1.0f, 2.0f, 3.0f}; // Dense vector std::vector<float> hy = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f, 9.0f}; // Scalar alpha float alpha = 3.7f; // Scalar beta float beta = 1.2f; // Offload data to device int* dxInd; float* dxVal; float* dy; HIP_CHECK(hipMalloc((void**)&dxInd, sizeof(int) * nnz)); HIP_CHECK(hipMalloc((void**)&dxVal, sizeof(float) * nnz)); HIP_CHECK(hipMalloc((void**)&dy, sizeof(float) * size)); HIP_CHECK(hipMemcpy(dxInd, hxInd.data(), sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dxVal, hxVal.data(), sizeof(float) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dy, hy.data(), sizeof(float) * size, hipMemcpyHostToDevice)); hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // Create sparse vector X hipsparseSpVecDescr_t vecX; HIPSPARSE_CHECK(hipsparseCreateSpVec( &vecX, size, nnz, dxInd, dxVal, HIPSPARSE_INDEX_32I, HIPSPARSE_INDEX_BASE_ZERO, HIP_R_32F)); // Create dense vector Y hipsparseDnVecDescr_t vecY; HIPSPARSE_CHECK(hipsparseCreateDnVec(&vecY, size, dy, HIP_R_32F)); // Call axpby to perform y = beta * y + alpha * x HIPSPARSE_CHECK(hipsparseAxpby(handle, &alpha, vecX, &beta, vecY)); HIPSPARSE_CHECK(hipsparseDnVecGetValues(vecY, (void**)&dy)); // Copy result back to host HIP_CHECK(hipMemcpy(hy.data(), dy, sizeof(float) * size, hipMemcpyDeviceToHost)); std::cout << "hy" << std::endl; for(size_t i = 0; i < hy.size(); i++) { std::cout << hy[i] << " "; } std::cout << "" << std::endl; // Clear hipSPARSE HIPSPARSE_CHECK(hipsparseDestroySpVec(vecX)); HIPSPARSE_CHECK(hipsparseDestroyDnVec(vecY)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); // Clear device memory HIP_CHECK(hipFree(dxInd)); HIP_CHECK(hipFree(dxVal)); HIP_CHECK(hipFree(dy)); return 0; }


- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**alpha**–**[in]**scalar \(\alpha\).**vecX**–**[in]**sparse matrix descriptor.**beta**–**[in]**scalar \(\beta\).**vecY**–**[inout]**dense matrix descriptor.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`alpha`

,`vecX`

,`beta`

or`vecY`

pointer is invalid.



## hipsparseGather()[#](#hipsparsegather)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseGather([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, hipsparseConstDnVecDescr_t vecY,[hipsparseSpVecDescr_t](types.html#_CPPv421hipsparseSpVecDescr_t)vecX)[#](#_CPPv415hipsparseGather17hipsparseHandle_t26hipsparseConstDnVecDescr_t21hipsparseSpVecDescr_t) Gather elements from a dense vector and store them into a sparse vector.

`hipsparseGather`

gathers the elements from the dense vector \(y\) and stores them in the sparse vector \(x\).for(i = 0; i < nnz; ++i) { x_val[i] = y[x_ind[i]]; }

`hipsparseGather`

supports the following uniform precision data types for the sparse and dense vectors \(x\) and \(y\).**Uniform Precisions:**X / Y

HIP_R_8I

HIP_R_16F

HIP_R_16BF

HIP_R_32F

HIP_R_64F

HIP_C_32F

HIP_C_64F

**Example**int main(int argc, char* argv[]) { // Number of non-zeros of the sparse vector int nnz = 3; // Size of sparse and dense vector int size = 9; // Sparse index vector std::vector<int> hxInd = {0, 3, 5}; // Dense vector std::vector<float> hy = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f, 9.0f}; // Offload data to device int* dxInd; float* dxVal; float* dy; HIP_CHECK(hipMalloc((void**)&dxInd, sizeof(int) * nnz)); HIP_CHECK(hipMalloc((void**)&dxVal, sizeof(float) * nnz)); HIP_CHECK(hipMalloc((void**)&dy, sizeof(float) * size)); HIP_CHECK(hipMemcpy(dxInd, hxInd.data(), sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dy, hy.data(), sizeof(float) * size, hipMemcpyHostToDevice)); hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // Create sparse vector X hipsparseSpVecDescr_t vecX; HIPSPARSE_CHECK(hipsparseCreateSpVec( &vecX, size, nnz, dxInd, dxVal, HIPSPARSE_INDEX_32I, HIPSPARSE_INDEX_BASE_ZERO, HIP_R_32F)); // Create dense vector Y hipsparseDnVecDescr_t vecY; HIPSPARSE_CHECK(hipsparseCreateDnVec(&vecY, size, dy, HIP_R_32F)); // Perform gather HIPSPARSE_CHECK(hipsparseGather(handle, vecY, vecX)); HIPSPARSE_CHECK(hipsparseSpVecGetValues(vecX, (void**)&dxVal)); // Copy result back to host std::vector<float> hxVal(nnz, 0.0f); HIP_CHECK(hipMemcpy(hxVal.data(), dxVal, sizeof(float) * nnz, hipMemcpyDeviceToHost)); // Clear hipSPARSE HIPSPARSE_CHECK(hipsparseDestroySpVec(vecX)); HIPSPARSE_CHECK(hipsparseDestroyDnVec(vecY)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); // Clear device memory HIP_CHECK(hipFree(dxInd)); HIP_CHECK(hipFree(dxVal)); HIP_CHECK(hipFree(dy)); return 0; }


- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**vecY**–**[in]**dense vector descriptor \(y\).**vecX**–**[out]**sparse vector descriptor \(x\).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`vecX`

or`vecY`

pointer is invalid.



## hipsparseScatter()[#](#hipsparsescatter)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseScatter([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, hipsparseConstSpVecDescr_t vecX,[hipsparseDnVecDescr_t](types.html#_CPPv421hipsparseDnVecDescr_t)vecY)[#](#_CPPv416hipsparseScatter17hipsparseHandle_t26hipsparseConstSpVecDescr_t21hipsparseDnVecDescr_t) Scatter elements from a sparse vector into a dense vector.

`hipsparseScatter`

scatters the elements from the sparse vector \(x\) in the dense vector \(y\).for(i = 0; i < nnz; ++i) { y[x_ind[i]] = x_val[i]; }

`hipsparseScatter`

supports the following uniform precision data types for the sparse and dense vectors \(x\) and \(y\).**Uniform Precisions:**X / Y

HIP_R_8I

HIP_R_16F

HIP_R_16BF

HIP_R_32F

HIP_R_64F

HIP_C_32F

HIP_C_64F

**Example**int main(int argc, char* argv[]) { // Number of non-zeros of the sparse vector int nnz = 3; // Size of sparse and dense vector int size = 9; // Sparse index vector std::vector<int> hxInd = {0, 3, 5}; // Sparse value vector std::vector<float> hxVal = {1.0f, 2.0f, 3.0f}; // Dense vector std::vector<float> hy = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f, 9.0f}; // Offload data to device int* dxInd; float* dxVal; float* dy; HIP_CHECK(hipMalloc((void**)&dxInd, sizeof(int) * nnz)); HIP_CHECK(hipMalloc((void**)&dxVal, sizeof(float) * nnz)); HIP_CHECK(hipMalloc((void**)&dy, sizeof(float) * size)); HIP_CHECK(hipMemcpy(dxInd, hxInd.data(), sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dxVal, hxVal.data(), sizeof(float) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dy, hy.data(), sizeof(float) * size, hipMemcpyHostToDevice)); hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // Create sparse vector X hipsparseSpVecDescr_t vecX; HIPSPARSE_CHECK(hipsparseCreateSpVec( &vecX, size, nnz, dxInd, dxVal, HIPSPARSE_INDEX_32I, HIPSPARSE_INDEX_BASE_ZERO, HIP_R_32F)); // Create dense vector Y hipsparseDnVecDescr_t vecY; HIPSPARSE_CHECK(hipsparseCreateDnVec(&vecY, size, dy, HIP_R_32F)); // Perform scatter HIPSPARSE_CHECK(hipsparseScatter(handle, vecX, vecY)); HIPSPARSE_CHECK(hipsparseDnVecGetValues(vecY, (void**)&dy)); // Copy result back to host HIP_CHECK(hipMemcpy(hy.data(), dy, sizeof(float) * size, hipMemcpyDeviceToHost)); // Clear hipSPARSE HIPSPARSE_CHECK(hipsparseDestroySpVec(vecX)); HIPSPARSE_CHECK(hipsparseDestroyDnVec(vecY)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); // Clear device memory HIP_CHECK(hipFree(dxInd)); HIP_CHECK(hipFree(dxVal)); HIP_CHECK(hipFree(dy)); return 0; }


- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**vecX**–**[in]**sparse vector descriptor \(x\).**vecY**–**[out]**dense vector descriptor \(y\).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`vecX`

or`vecY`

pointer is invalid.



## hipsparseRot()[#](#hipsparserot)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseRot([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, const void *c_coeff, const void *s_coeff,[hipsparseSpVecDescr_t](types.html#_CPPv421hipsparseSpVecDescr_t)vecX,[hipsparseDnVecDescr_t](types.html#_CPPv421hipsparseDnVecDescr_t)vecY)[#](#_CPPv412hipsparseRot17hipsparseHandle_tPKvPKv21hipsparseSpVecDescr_t21hipsparseDnVecDescr_t) Apply Givens rotation to a dense and a sparse vector.

`hipsparseRot`

applies the Givens rotation matrix \(G\) to the sparse vector \(x\) and the dense vector \(y\), where\[\begin{split} G = \begin{pmatrix} c & s \\ -s & c \end{pmatrix} \end{split}\]for(i = 0; i < nnz; ++i) { x_tmp = x_val[i]; y_tmp = y[x_ind[i]]; x_val[i] = c * x_tmp + s * y_tmp; y[x_ind[i]] = c * y_tmp - s * x_tmp; }

`hipsparseRot`

supports the following uniform precision data types for the sparse and dense vectors \(x\) and \(y\) and compute types for the scalars \(c\) and \(s\).**Uniform Precisions:**X / Y / compute_type

HIP_R_32F

HIP_R_64F

HIP_C_32F

HIP_C_64F

**Example**int main(int argc, char* argv[]) { // Number of non-zeros of the sparse vector int nnz = 3; // Size of sparse and dense vector int size = 9; // Sparse index vector std::vector<int> hxInd = {0, 3, 5}; // Sparse value vector std::vector<float> hxVal = {1.0f, 2.0f, 3.0f}; // Dense vector std::vector<float> hy = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f, 9.0f}; // Scalar c float c = 3.7f; // Scalar s float s = 1.2f; // Offload data to device int* dxInd; float* dxVal; float* dy; HIP_CHECK(hipMalloc((void**)&dxInd, sizeof(int) * nnz)); HIP_CHECK(hipMalloc((void**)&dxVal, sizeof(float) * nnz)); HIP_CHECK(hipMalloc((void**)&dy, sizeof(float) * size)); HIP_CHECK(hipMemcpy(dxInd, hxInd.data(), sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dxVal, hxVal.data(), sizeof(float) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dy, hy.data(), sizeof(float) * size, hipMemcpyHostToDevice)); hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // Create sparse vector X hipsparseSpVecDescr_t vecX; HIPSPARSE_CHECK(hipsparseCreateSpVec( &vecX, size, nnz, dxInd, dxVal, HIPSPARSE_INDEX_32I, HIPSPARSE_INDEX_BASE_ZERO, HIP_R_32F)); // Create dense vector Y hipsparseDnVecDescr_t vecY; HIPSPARSE_CHECK(hipsparseCreateDnVec(&vecY, size, dy, HIP_R_32F)); // Call rot HIPSPARSE_CHECK(hipsparseRot(handle, (void*)&c, (void*)&s, vecX, vecY)); HIPSPARSE_CHECK(hipsparseSpVecGetValues(vecX, (void**)&dxVal)); HIPSPARSE_CHECK(hipsparseDnVecGetValues(vecY, (void**)&dy)); // Copy result back to host HIP_CHECK(hipMemcpy(hxVal.data(), dxVal, sizeof(float) * nnz, hipMemcpyDeviceToHost)); HIP_CHECK(hipMemcpy(hy.data(), dy, sizeof(float) * size, hipMemcpyDeviceToHost)); // Clear hipSPARSE HIPSPARSE_CHECK(hipsparseDestroySpVec(vecX)); HIPSPARSE_CHECK(hipsparseDestroyDnVec(vecY)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); // Clear device memory HIP_CHECK(hipFree(dxInd)); HIP_CHECK(hipFree(dxVal)); HIP_CHECK(hipFree(dy)); return 0; }


- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**c_coeff**–**[in]**pointer to the cosine element of \(G\), can be on host or device.**s_coeff**–**[in]**pointer to the sine element of \(G\), can be on host or device.**vecX**–**[inout]**sparse vector descriptor \(x\).**vecY**–**[inout]**dense vector descriptor \(y\).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`c_coeff`

,`s_coeff`

,`vecX`

or`vecY`

pointer is invalid.



## hipsparseSparseToDense_bufferSize()[#](#hipsparsesparsetodense-buffersize)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSparseToDense_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, hipsparseConstSpMatDescr_t matA,[hipsparseDnMatDescr_t](types.html#_CPPv421hipsparseDnMatDescr_t)matB,[hipsparseSparseToDenseAlg_t](types.html#_CPPv427hipsparseSparseToDenseAlg_t)alg, size_t *pBufferSizeInBytes)[#](#_CPPv433hipsparseSparseToDense_bufferSize17hipsparseHandle_t26hipsparseConstSpMatDescr_t21hipsparseDnMatDescr_t27hipsparseSparseToDenseAlg_tP6size_t) `hipsparseSparseToDense_bufferSize`

computes the required user allocated buffer size needed when converting a sparse matrix to a dense matrix. This routine currently accepts the sparse matrix descriptor`matA`

in CSR, CSC, or COO format. This routine is used to determine the size of the buffer needed in[hipsparseSparseToDense](#hipsparse__sparse2dense_8h_1a88f88d207ae284bb1748af4c86158c53).`hipsparseSparseToDense_bufferSize`

supports different data types for the sparse and dense matrices. See[hipsparseSparseToDense](#hipsparse__sparse2dense_8h_1a88f88d207ae284bb1748af4c86158c53)for a complete listing of all the data types available.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**matA**–**[in]**sparse matrix descriptor.**matB**–**[in]**dense matrix descriptor.**alg**–**[in]**algorithm for the sparse to dense computation.**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`matA`

,`matB`

, or`pBufferSizeInBytes`

pointer is invalid.



## hipsparseSparseToDense()[#](#hipsparsesparsetodense)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSparseToDense([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, hipsparseConstSpMatDescr_t matA,[hipsparseDnMatDescr_t](types.html#_CPPv421hipsparseDnMatDescr_t)matB,[hipsparseSparseToDenseAlg_t](types.html#_CPPv427hipsparseSparseToDenseAlg_t)alg, void *externalBuffer)[#](#_CPPv422hipsparseSparseToDense17hipsparseHandle_t26hipsparseConstSpMatDescr_t21hipsparseDnMatDescr_t27hipsparseSparseToDenseAlg_tPv) Sparse matrix to dense matrix conversion.

`hipsparseSparseToDense`

converts a sparse matrix to a dense matrix. This routine currently accepts the sparse matrix descriptor`matA`

in CSR, CSC, or COO format. This routine takes a user allocated buffer whose size must first be computed by calling[hipsparseSparseToDense_bufferSize](#hipsparse__sparse2dense_8h_1ad9c85487c1d32159e61c56134dd84ba9)The conversion of a sparse matrix into a dense one involves two steps. First, the user creates the sparse and dense matrix descriptors and calls

[hipsparseSparseToDense_bufferSize](#hipsparse__sparse2dense_8h_1ad9c85487c1d32159e61c56134dd84ba9)to determine the size of the required temporary storage buffer. The user then allocates this buffer and passes it to[hipsparseSparseToDense](#hipsparse__sparse2dense_8h_1a88f88d207ae284bb1748af4c86158c53)in order to complete the conversion. Once the conversion is complete, the user is free to deallocate the storage buffer. See full example below for details.`hipsparseSparseToDense`

supports the following uniform precision data types for the sparse and dense matrices \(A\) and \(B\):**Uniform Precisions:**A / B

HIP_R_16F

HIP_R_16BF

HIP_R_32F

HIP_R_64F

HIP_C_32F

HIP_C_64F

**Example**int main(int argc, char* argv[]) { // 1 0 0 0 // A = 4 2 0 4 // 0 3 7 0 // 9 0 0 1 int m = 4; int n = 4; int nnz = 8; std::vector<int> hcsrRowPtrA = {0, 1, 4, 6, 8}; std::vector<int> hcsrColIndA = {0, 0, 1, 3, 1, 2, 0, 3}; std::vector<float> hcsrValA = {1.0f, 4.0f, 2.0f, 4.0f, 3.0f, 7.0f, 9.0f, 1.0f}; int* dcsrRowPtrA; int* dcsrColIndA; float* dcsrValA; HIP_CHECK(hipMalloc((void**)&dcsrRowPtrA, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&dcsrColIndA, sizeof(int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcsrValA, sizeof(float) * nnz)); HIP_CHECK( hipMemcpy(dcsrRowPtrA, hcsrRowPtrA.data(), sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrColIndA, hcsrColIndA.data(), sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrValA, hcsrValA.data(), sizeof(float) * nnz, hipMemcpyHostToDevice)); float* ddenseB; HIP_CHECK(hipMalloc((void**)&ddenseB, sizeof(float) * m * n)); hipsparseHandle_t handle; hipsparseSpMatDescr_t matA; hipsparseDnMatDescr_t matB; HIPSPARSE_CHECK(hipsparseCreate(&handle)); hipsparseIndexType_t rowIdxTypeA = HIPSPARSE_INDEX_32I; hipsparseIndexType_t colIdxTypeA = HIPSPARSE_INDEX_32I; hipDataType dataTypeA = HIP_R_32F; hipsparseIndexBase_t idxBaseA = HIPSPARSE_INDEX_BASE_ZERO; // Create sparse matrix A HIPSPARSE_CHECK(hipsparseCreateCsr(&matA, m, n, nnz, dcsrRowPtrA, dcsrColIndA, dcsrValA, rowIdxTypeA, colIdxTypeA, idxBaseA, dataTypeA)); // Create dense matrix B HIPSPARSE_CHECK(hipsparseCreateDnMat(&matB, m, n, m, ddenseB, HIP_R_32F, HIPSPARSE_ORDER_COL)); hipsparseSparseToDenseAlg_t alg = HIPSPARSE_SPARSETODENSE_ALG_DEFAULT; size_t bufferSize; HIPSPARSE_CHECK(hipsparseSparseToDense_bufferSize(handle, matA, matB, alg, &bufferSize)); void* tempBuffer; HIP_CHECK(hipMalloc((void**)&tempBuffer, bufferSize)); // Complete the conversion HIPSPARSE_CHECK(hipsparseSparseToDense(handle, matA, matB, alg, tempBuffer)); // Copy result back to host std::vector<float> hdenseB(m * n); HIP_CHECK(hipMemcpy(hdenseB.data(), ddenseB, sizeof(float) * m * n, hipMemcpyDeviceToHost)); // Clear hipSPARSE HIPSPARSE_CHECK(hipsparseDestroyMatDescr(matA)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(matB)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); // Clear device memory HIP_CHECK(hipFree(dcsrRowPtrA)); HIP_CHECK(hipFree(dcsrColIndA)); HIP_CHECK(hipFree(dcsrValA)); HIP_CHECK(hipFree(ddenseB)); HIP_CHECK(hipFree(tempBuffer)); return 0; }


Note

Currently only the sparse matrix formats CSR, CSC, and COO are supported when converting a sparse matrix to a dense matrix.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**matA**–**[in]**sparse matrix descriptor.**matB**–**[in]**dense matrix descriptor.**alg**–**[in]**algorithm for the sparse to dense computation.**externalBuffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`matA`

,`matB`

, or`externalBuffer`

pointer is invalid.



## hipsparseDenseToSparse_bufferSize()[#](#hipsparsedensetosparse-buffersize)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDenseToSparse_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, hipsparseConstDnMatDescr_t matA,[hipsparseSpMatDescr_t](types.html#_CPPv421hipsparseSpMatDescr_t)matB,[hipsparseDenseToSparseAlg_t](types.html#_CPPv427hipsparseDenseToSparseAlg_t)alg, size_t *pBufferSizeInBytes)[#](#_CPPv433hipsparseDenseToSparse_bufferSize17hipsparseHandle_t26hipsparseConstDnMatDescr_t21hipsparseSpMatDescr_t27hipsparseDenseToSparseAlg_tP6size_t) `hipsparseDenseToSparse_bufferSize`

computes the required user allocated buffer size needed when converting a dense matrix to a sparse matrix. This routine currently accepts the sparse matrix descriptor`matB`

in CSR, CSC, or COO format. This routine is used to determine the size of the buffer needed in[hipsparseDenseToSparse_analysis](#hipsparse__dense2sparse_8h_1a732ce6d8dfc602c8b1ff56b78c1872d4)and[hipsparseDenseToSparse_convert](#hipsparse__dense2sparse_8h_1a0015b2663de639d3f47620b48b0fd11c).`hipsparseDenseToSparse_bufferSize`

supports different data types for the dense and sparse matrices. See[hipsparseDenseToSparse_convert](#hipsparse__dense2sparse_8h_1a0015b2663de639d3f47620b48b0fd11c)for a complete listing of all the data types available.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**matA**–**[in]**dense matrix descriptor.**matB**–**[in]**sparse matrix descriptor.**alg**–**[in]**algorithm for the dense to sparse computation.**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`matA`

,`matB`

, or`pBufferSizeInBytes`

pointer is invalid.



## hipsparseDenseToSparse_analysis()[#](#hipsparsedensetosparse-analysis)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDenseToSparse_analysis([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, hipsparseConstDnMatDescr_t matA,[hipsparseSpMatDescr_t](types.html#_CPPv421hipsparseSpMatDescr_t)matB,[hipsparseDenseToSparseAlg_t](types.html#_CPPv427hipsparseDenseToSparseAlg_t)alg, void *externalBuffer)[#](#_CPPv431hipsparseDenseToSparse_analysis17hipsparseHandle_t26hipsparseConstDnMatDescr_t21hipsparseSpMatDescr_t27hipsparseDenseToSparseAlg_tPv) `hipsparseDenseToSparse_analysis`

performs analysis that is later used in[hipsparseDenseToSparse_convert](#hipsparse__dense2sparse_8h_1a0015b2663de639d3f47620b48b0fd11c)when converting a dense matrix to sparse matrix. This routine currently accepts the sparse matrix descriptor`matB`

in CSR, CSC, or COO format. This routine takes a user allocated buffer whose size must first be computed using[hipsparseDenseToSparse_bufferSize](#hipsparse__dense2sparse_8h_1abe0d0ca5ff6be464f7f42adb9466c51f).`hipsparseDenseToSparse_analysis`

supports different data types for the dense and sparse matrices. See[hipsparseDenseToSparse_convert](#hipsparse__dense2sparse_8h_1a0015b2663de639d3f47620b48b0fd11c)for a complete listing of all the data types available.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**matA**–**[in]**dense matrix descriptor.**matB**–**[in]**sparse matrix descriptor.**alg**–**[in]**algorithm for the dense to sparse computation.**externalBuffer**–**[out]**temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`matA`

,`matB`

, or`externalBuffer`

pointer is invalid.



## hipsparseDenseToSparse_convert()[#](#hipsparsedensetosparse-convert)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDenseToSparse_convert([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, hipsparseConstDnMatDescr_t matA,[hipsparseSpMatDescr_t](types.html#_CPPv421hipsparseSpMatDescr_t)matB,[hipsparseDenseToSparseAlg_t](types.html#_CPPv427hipsparseDenseToSparseAlg_t)alg, void *externalBuffer)[#](#_CPPv430hipsparseDenseToSparse_convert17hipsparseHandle_t26hipsparseConstDnMatDescr_t21hipsparseSpMatDescr_t27hipsparseDenseToSparseAlg_tPv) Dense matrix to sparse matrix conversion.

`hipsparseDenseToSparse_convert`

converts a dense matrix to a sparse matrix. This routine currently accepts the sparse matrix descriptor`matB`

in CSR, CSC, or COO format. This routine requires a user allocated buffer whose size must be determined by first calling[hipsparseDenseToSparse_bufferSize](#hipsparse__dense2sparse_8h_1abe0d0ca5ff6be464f7f42adb9466c51f).The conversion of a dense matrix into a sparse one involves three steps. First, the user creates the dense and sparse matrix descriptors. Because the number of non-zeros that will exist in the sparse matrix is not known apriori, when creating the sparse matrix descriptor, the user simply sets the arrays to

`NULL`

and the non-zero count to zero. For example, in the case of a CSR sparse matrix, this would look like:In the case of a COO sparse matrix, this would look like:hipsparseCreateCsr(&matB, m, n, 0, dcsrRowPtrB, // This array can be allocated as its size (i.e. m + 1) is known NULL, // Column indices array size is not yet known, pass NULL for now NULL, // Values array size is not yet known, pass NULL for now rowIdxTypeB, colIdxTypeB, idxBaseB, dataTypeB);

Once the descriptors have been created, the user callshipsparseCreateCoo(&matB, m, n, 0, NULL, // Row indices array size is not yet known, pass NULL for now NULL, // Column indices array size is not yet known, pass NULL for now NULL, // Values array size is not yet known, pass NULL for now rowIdxTypeB, colIdxTypeB, idxBaseB, dataTypeB);

[hipsparseDenseToSparse_bufferSize](#hipsparse__dense2sparse_8h_1abe0d0ca5ff6be464f7f42adb9466c51f). This routine will determine the size of the required temporary storage buffer. The user then allocates this buffer and passes it to[hipsparseDenseToSparse_analysis](#hipsparse__dense2sparse_8h_1a732ce6d8dfc602c8b1ff56b78c1872d4)which will perform analysis on the dense matrix in order to determine the number of non-zeros that will exist in the sparse matrix. Once this[hipsparseDenseToSparse_analysis](#hipsparse__dense2sparse_8h_1a732ce6d8dfc602c8b1ff56b78c1872d4)routine has been called, the non-zero count is stored in the sparse matrix descriptor`matB`

. In order to allocate our remaining sparse matrix arrays, we query the sparse matrix descriptor`matB`

for this non-zero count:The remaining arrays are then allocated and set on the sparse matrix descriptor// Grab the non-zero count from the B matrix decriptor int64_t rows; int64_t cols; int64_t nnz; hipsparseSpMatGetSize(matB, &rows, &cols, &nnz);

`matB`

. Finally, we complete the conversion by calling[hipsparseDenseToSparse_convert](#hipsparse__dense2sparse_8h_1a0015b2663de639d3f47620b48b0fd11c). Once the conversion is complete, the user is free to deallocate the storage buffer. See full example below for details.`hipsparseDenseToSparse_convert`

supports the following uniform precision data types for the dense and sparse matrices \(A\) and \(B\):**Uniform Precisions:**A / B

HIP_R_16F

HIP_R_16BF

HIP_R_32F

HIP_R_64F

HIP_C_32F

HIP_C_64F

**Example**int main(int argc, char* argv[]) { // 1 0 0 0 // A = 4 2 0 4 // 0 3 7 0 // 9 0 0 1 int m = 4; int n = 4; std::vector<float> hdenseA = {1.0f, 4.0f, 0.0f, 9.0f, 0.0f, 2.0f, 3.0f, 0.0f, 0.0f, 0.0f, 7.0f, 0.0f, 0.0f, 4.0f, 0.0f, 1.0f}; float* ddenseA; HIP_CHECK(hipMalloc((void**)&ddenseA, sizeof(float) * m * n)); HIP_CHECK(hipMemcpy(ddenseA, hdenseA.data(), sizeof(float) * m * n, hipMemcpyHostToDevice)); int* dcsrRowPtrB; HIP_CHECK(hipMalloc((void**)&dcsrRowPtrB, sizeof(int) * (m + 1))); hipsparseHandle_t handle; hipsparseDnMatDescr_t matA; hipsparseSpMatDescr_t matB; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // Create dense matrix A HIPSPARSE_CHECK(hipsparseCreateDnMat(&matA, m, n, m, ddenseA, HIP_R_32F, HIPSPARSE_ORDER_COL)); hipsparseIndexType_t rowIdxTypeB = HIPSPARSE_INDEX_32I; hipsparseIndexType_t colIdxTypeB = HIPSPARSE_INDEX_32I; hipDataType dataTypeB = HIP_R_32F; hipsparseIndexBase_t idxBaseB = HIPSPARSE_INDEX_BASE_ZERO; // Create sparse matrix B HIPSPARSE_CHECK(hipsparseCreateCsr( &matB, m, n, 0, dcsrRowPtrB, NULL, NULL, rowIdxTypeB, colIdxTypeB, idxBaseB, dataTypeB)); hipsparseDenseToSparseAlg_t alg = HIPSPARSE_DENSETOSPARSE_ALG_DEFAULT; size_t bufferSize; HIPSPARSE_CHECK(hipsparseDenseToSparse_bufferSize(handle, matA, matB, alg, &bufferSize)); void* tempBuffer; HIP_CHECK(hipMalloc((void**)&tempBuffer, bufferSize)); // Perform analysis which will determine the number of non-zeros in the CSR matrix HIPSPARSE_CHECK(hipsparseDenseToSparse_analysis(handle, matA, matB, alg, tempBuffer)); // Grab the non-zero count from the B matrix decriptor int64_t rows; int64_t cols; int64_t nnz; HIPSPARSE_CHECK(hipsparseSpMatGetSize(matB, &rows, &cols, &nnz)); // Allocate the column indices and values arrays int* dcsrColIndB; float* dcsrValB; HIP_CHECK(hipMalloc((void**)&dcsrColIndB, sizeof(int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcsrValB, sizeof(float) * nnz)); // Set the newly allocated arrays on the sparse matrix descriptor HIPSPARSE_CHECK(hipsparseCsrSetPointers(matB, dcsrRowPtrB, dcsrColIndB, dcsrValB)); // Complete the conversion HIPSPARSE_CHECK(hipsparseDenseToSparse_convert(handle, matA, matB, alg, tempBuffer)); // Copy result back to host std::vector<int> hcsrRowPtrB(m + 1); std::vector<int> hcsrColIndB(nnz); std::vector<float> hcsrValB(nnz); HIP_CHECK( hipMemcpy(hcsrRowPtrB.data(), dcsrRowPtrB, sizeof(int) * (m + 1), hipMemcpyDeviceToHost)); HIP_CHECK(hipMemcpy(hcsrColIndB.data(), dcsrColIndB, sizeof(int) * nnz, hipMemcpyDeviceToHost)); HIP_CHECK(hipMemcpy(hcsrValB.data(), dcsrValB, sizeof(float) * nnz, hipMemcpyDeviceToHost)); // Clear hipSPARSE HIPSPARSE_CHECK(hipsparseDestroyMatDescr(matA)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(matB)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); // Clear device memory HIP_CHECK(hipFree(ddenseA)); HIP_CHECK(hipFree(dcsrRowPtrB)); HIP_CHECK(hipFree(dcsrColIndB)); HIP_CHECK(hipFree(dcsrValB)); HIP_CHECK(hipFree(tempBuffer)); return 0; }


Note

Currently only the sparse matrix formats CSR, CSC, and COO are supported when converting a dense matrix to a sparse matrix.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**matA**–**[in]**dense matrix descriptor.**matB**–**[in]**sparse matrix descriptor.**alg**–**[in]**algorithm for the dense to sparse computation.**externalBuffer**–**[out]**temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`matA`

,`matB`

, or`externalBuffer`

pointer is invalid.



## hipsparseSpVV_bufferSize()[#](#hipsparsespvv-buffersize)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpVV_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opX, hipsparseConstSpVecDescr_t vecX, hipsparseConstDnVecDescr_t vecY, void *result, hipDataType computeType, size_t *pBufferSizeInBytes)[#](#_CPPv424hipsparseSpVV_bufferSize17hipsparseHandle_t20hipsparseOperation_t26hipsparseConstSpVecDescr_t26hipsparseConstDnVecDescr_tPv11hipDataTypeP6size_t) `hipsparseSpVV_bufferSize`

computes the required user allocated buffer size needed when computing the inner dot product of a sparse vector with a dense vector:\[ \text{result} := op(x) \cdot y, \]`hipsparseSpVV_bufferSize`

supports multiple combinations of data types and compute types. See[hipsparseSpVV](#hipsparse__spvv_8h_1a9be5659aed0ce6e92addeb2a30a21fc8)for a complete listing of all the data type and compute type combinations available.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**opX**–**[in]**sparse vector operation type.**vecX**–**[in]**sparse vector descriptor.**vecY**–**[in]**dense vector descriptor.**result**–**[out]**pointer to the result, can be host or device memory**computeType**–**[in]**floating point precision for the SpVV computation.**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`vecX`

,`vecY`

,`result`

or`pBufferSizeInBytes`

pointer is invalid.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`computeType`

is currently not supported.



## hipsparseSpVV()[#](#hipsparsespvv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpVV([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opX, hipsparseConstSpVecDescr_t vecX, hipsparseConstDnVecDescr_t vecY, void *result, hipDataType computeType, void *externalBuffer)[#](#_CPPv413hipsparseSpVV17hipsparseHandle_t20hipsparseOperation_t26hipsparseConstSpVecDescr_t26hipsparseConstDnVecDescr_tPv11hipDataTypePv) Compute the inner dot product of a sparse vector with a dense vector.

`hipsparseSpVV`

computes the inner dot product of the sparse vector \(x\) with the dense vector \(y\), such that\[ \text{result} := op(x) \cdot y, \]with\[\begin{split} op(x) = \left\{ \begin{array}{ll} x, & \text{if trans == HIPSPARSE_OPERATION_NON_TRANSPOSE} \\ \bar{x}, & \text{if trans == HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE} \\ \end{array} \right. \end{split}\]result = 0; for(i = 0; i < nnz; ++i) { result += x_val[i] * y[x_ind[i]]; }

Performing the above operation involves two steps. First, the user calls

`hipsparseSpVV_bufferSize`

which will return the required temporary buffer size. The user then allocates this buffer. Finally, the user then completes the computation by calling`hipsparseSpVV`

with the newly allocated buffer. Once the computation is complete, the user is free to deallocate the buffer.`hipsparseSpVV`

supports the following uniform and mixed precision data types for the sparse and dense vectors \(x\) and \(y\) and compute types for the scalar \(result\).**Uniform Precisions:**X / Y / compute_type

HIP_R_32F

HIP_R_64F

HIP_C_32F

HIP_C_64F

**Mixed precisions:**X / Y

compute_type

HIP_R_8I

HIP_R_32I

HIP_R_8I

HIP_R_32F

HIP_R_16F

HIP_R_32F

HIP_R_16BF

HIP_R_32F

**Example**int main(int argc, char* argv[]) { // Number of non-zeros of the sparse vector int nnz = 3; // Size of sparse and dense vector int size = 9; // Sparse index vector std::vector<int> hxInd = {0, 3, 5}; // Sparse value vector std::vector<float> hxVal = {1.0f, 2.0f, 3.0f}; // Dense vector std::vector<float> hy = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f, 9.0f}; // Offload data to device int* dxInd; float* dxVal; float* dy; HIP_CHECK(hipMalloc((void**)&dxInd, sizeof(int) * nnz)); HIP_CHECK(hipMalloc((void**)&dxVal, sizeof(float) * nnz)); HIP_CHECK(hipMalloc((void**)&dy, sizeof(float) * size)); HIP_CHECK(hipMemcpy(dxInd, hxInd.data(), sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dxVal, hxVal.data(), sizeof(float) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dy, hy.data(), sizeof(float) * size, hipMemcpyHostToDevice)); hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // Create sparse vector X hipsparseSpVecDescr_t vecX; HIPSPARSE_CHECK(hipsparseCreateSpVec( &vecX, size, nnz, dxInd, dxVal, HIPSPARSE_INDEX_32I, HIPSPARSE_INDEX_BASE_ZERO, HIP_R_32F)); // Create dense vector Y hipsparseDnVecDescr_t vecY; HIPSPARSE_CHECK(hipsparseCreateDnVec(&vecY, size, dy, HIP_R_32F)); // Obtain buffer size float hresult = 0.0f; size_t buffer_size; HIPSPARSE_CHECK(hipsparseSpVV_bufferSize( handle, HIPSPARSE_OPERATION_NON_TRANSPOSE, vecX, vecY, &hresult, HIP_R_32F, &buffer_size)); void* temp_buffer; HIP_CHECK(hipMalloc(&temp_buffer, buffer_size)); // SpVV HIPSPARSE_CHECK(hipsparseSpVV( handle, HIPSPARSE_OPERATION_NON_TRANSPOSE, vecX, vecY, &hresult, HIP_R_32F, temp_buffer)); HIP_CHECK(hipDeviceSynchronize()); std::cout << "hresult: " << hresult << std::endl; // Clear hipSPARSE HIPSPARSE_CHECK(hipsparseDestroySpVec(vecX)); HIPSPARSE_CHECK(hipsparseDestroyDnVec(vecY)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); // Clear device memory HIP_CHECK(hipFree(dxInd)); HIP_CHECK(hipFree(dxVal)); HIP_CHECK(hipFree(dy)); HIP_CHECK(hipFree(temp_buffer)); return 0; }


- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**opX**–**[in]**sparse vector operation type.**vecX**–**[in]**sparse vector descriptor.**vecY**–**[in]**dense vector descriptor.**result**–**[out]**pointer to the result, can be host or device memory**computeType**–**[in]**floating point precision for the SpVV computation.**externalBuffer**–**[out]**temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`vecX`

,`vecY`

,`result`

or`externalBuffer`

pointer is invalid.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`computeType`

is currently not supported.



## hipsparseSpMV_bufferSize()[#](#hipsparsespmv-buffersize)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpMV_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opA, const void *alpha, hipsparseConstSpMatDescr_t matA, hipsparseConstDnVecDescr_t vecX, const void *beta, const[hipsparseDnVecDescr_t](types.html#_CPPv421hipsparseDnVecDescr_t)vecY, hipDataType computeType,[hipsparseSpMVAlg_t](types.html#_CPPv418hipsparseSpMVAlg_t)alg, size_t *pBufferSizeInBytes)[#](#_CPPv424hipsparseSpMV_bufferSize17hipsparseHandle_t20hipsparseOperation_tPKv26hipsparseConstSpMatDescr_t26hipsparseConstDnVecDescr_tPKvK21hipsparseDnVecDescr_t11hipDataType18hipsparseSpMVAlg_tP6size_t) `hipsparseSpMV_bufferSize`

computes the required user allocated buffer size needed when computing the sparse matrix multiplication with a dense vector:\[ y := \alpha \cdot op(A) \cdot x + \beta \cdot y, \]where \(op(A)\) is a sparse \(m \times n\) matrix in CSR, CSC, COO, or COO (AoS) format, \(x\) is a dense vector of length \(n\) and \(y\) is a dense vector of length \(m\).`hipsparseSpMV_bufferSize`

supports multiple combinations of data types and compute types. See[hipsparseSpMV](#hipsparse__spmv_8h_1aef27d7c11068e573577d681b7e6480ab)for a complete listing of all the data type and compute type combinations available.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**opA**–**[in]**matrix operation type.**alpha**–**[in]**scalar \(\alpha\).**matA**–**[in]**matrix descriptor.**vecX**–**[in]**vector descriptor.**beta**–**[in]**scalar \(\beta\).**vecY**–**[inout]**vector descriptor.**computeType**–**[in]**floating point precision for the SpMV computation.**alg**–**[in]**SpMV algorithm for the SpMV computation.**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`alpha`

,`matA`

,`x`

,`beta`

,`y`

or`pBufferSizeInBytes`

pointer is invalid or if`opA`

,`computeType`

,`alg`

is incorrect.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`computeType`

or`alg`

is currently not supported.



## hipsparseSpMV_preprocess()[#](#hipsparsespmv-preprocess)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpMV_preprocess([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opA, const void *alpha, hipsparseConstSpMatDescr_t matA, hipsparseConstDnVecDescr_t vecX, const void *beta, const[hipsparseDnVecDescr_t](types.html#_CPPv421hipsparseDnVecDescr_t)vecY, hipDataType computeType,[hipsparseSpMVAlg_t](types.html#_CPPv418hipsparseSpMVAlg_t)alg, void *externalBuffer)[#](#_CPPv424hipsparseSpMV_preprocess17hipsparseHandle_t20hipsparseOperation_tPKv26hipsparseConstSpMatDescr_t26hipsparseConstDnVecDescr_tPKvK21hipsparseDnVecDescr_t11hipDataType18hipsparseSpMVAlg_tPv) `hipsparseSpMV_preprocess`

performs analysis on the sparse matrix \(op(A)\) when computing the sparse matrix multiplication with a dense vector:\[ y := \alpha \cdot op(A) \cdot x + \beta \cdot y, \]where \(op(A)\) is a sparse \(m \times n\) matrix in CSR, CSC, COO, or COO (AoS) format, \(x\) is a dense vector of length \(n\) and \(y\) is a dense vector of length \(m\). This step is optional but if used may results in better performance.`hipsparseSpMV_preprocess`

supports multiple combinations of data types and compute types. See[hipsparseSpMV](#hipsparse__spmv_8h_1aef27d7c11068e573577d681b7e6480ab)for a complete listing of all the data type and compute type combinations available.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**opA**–**[in]**matrix operation type.**alpha**–**[in]**scalar \(\alpha\).**matA**–**[in]**matrix descriptor.**vecX**–**[in]**vector descriptor.**beta**–**[in]**scalar \(\beta\).**vecY**–**[inout]**vector descriptor.**computeType**–**[in]**floating point precision for the SpMV computation.**alg**–**[in]**SpMV algorithm for the SpMV computation.**externalBuffer**–**[out]**temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`alpha`

,`matA`

,`x`

,`beta`

,`y`

or`externalBuffer`

pointer is invalid or if`opA`

,`computeType`

,`alg`

is incorrect.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`computeType`

or`alg`

is currently not supported.



## hipsparseSpMV()[#](#hipsparsespmv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpMV([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opA, const void *alpha, hipsparseConstSpMatDescr_t matA, hipsparseConstDnVecDescr_t vecX, const void *beta, const[hipsparseDnVecDescr_t](types.html#_CPPv421hipsparseDnVecDescr_t)vecY, hipDataType computeType,[hipsparseSpMVAlg_t](types.html#_CPPv418hipsparseSpMVAlg_t)alg, void *externalBuffer)[#](#_CPPv413hipsparseSpMV17hipsparseHandle_t20hipsparseOperation_tPKv26hipsparseConstSpMatDescr_t26hipsparseConstDnVecDescr_tPKvK21hipsparseDnVecDescr_t11hipDataType18hipsparseSpMVAlg_tPv) Compute the sparse matrix multiplication with a dense vector.

`hipsparseSpMV`

multiplies the scalar \(\alpha\) with a sparse \(m \times n\) matrix \(op(A)\), defined in CSR, CSC, COO, or COO (AoS) format, with the dense vector \(x\) and adds the result to the dense vector \(y\) that is multiplied by the scalar \(\beta\), such that\[ y := \alpha \cdot op(A) \cdot x + \beta \cdot y, \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if trans == HIPSPARSE_OPERATION_NON_TRANSPOSE} \\ A^T, & \text{if trans == HIPSPARSE_OPERATION_TRANSPOSE} \\ A^H, & \text{if trans == HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE} \end{array} \right. \end{split}\]Performing the above operation involves multiple steps. First the user calls

[hipsparseSpMV_bufferSize](#hipsparse__spmv_8h_1a769d0d9e98c800e5bac4469d87714301)to determine the size of the required temporary storage buffer. The user then allocates this buffer and calls[hipsparseSpMV_preprocess](#hipsparse__spmv_8h_1a10ee6e1173d0c756cc81c21a551c8d5d). Depending on the algorithm and sparse matrix format, this will perform analysis on the sparsity pattern of \(op(A)\). Finally the user completes the operation by calling`hipsparseSpMV`

. The buffer size and preprecess routines only need to be called once for a given sparse matrix \(op(A)\) while the computation can be repeatedly used with different \(x\) and \(y\) vectors. Once all calls to`hipsparseSpMV`

are complete, the temporary buffer can be deallocated.`hipsparseSpMV`

supports multiple different algorithms. These algorithms have different trade offs depending on the sparsity pattern of the matrix, whether or not the results need to be deterministic, and how many times the sparse-vector product will be performed.CSR Algorithms

HIPSPARSE_SPMV_CSR_ALG1

HIPSPARSE_SPMV_CSR_ALG2

COO Algorithms

HIPSPARSE_SPMV_COO_ALG1

HIPSPARSE_SPMV_COO_ALG2

`hipsparseSpMV`

supports multiple combinations of data types and compute types. The tables below indicate the currently supported data types that can be used for the sparse matrix \(op(A)\) and the dense vectors \(x\) and \(y\) and the compute type for \(\alpha\) and \(\beta\). The advantage of using different data types is to save on memory bandwidth and storage when a user application allows while performing the actual computation in a higher precision.`hipsparseSpMV`

supports[HIPSPARSE_INDEX_32I](types.html#hipsparse-generic-types_8h_1aaeacc98278238b4555b312b38a8ca3a1a39d66b98a770ce4f130cf175614bf1ee)and[HIPSPARSE_INDEX_64I](types.html#hipsparse-generic-types_8h_1aaeacc98278238b4555b312b38a8ca3a1aaf693262ac42a636addc9be11c1f534b)index precisions for storing the row pointer and row/column indices arrays of the sparse matrices.**Uniform Precisions:**A / X / Y / compute_type

HIP_R_32F

HIP_R_64F

HIP_C_32F

HIP_C_64F

**Mixed precisions:**A / X

Y

compute_type

HIP_R_8I

HIP_R_32I

HIP_R_32I

HIP_R_8I

HIP_R_32F

HIP_R_32F

HIP_R_16F

HIP_R_32F

HIP_R_32F

HIP_R_16BF

HIP_R_32F

HIP_R_32F

**Mixed-regular real precisions**A

X / Y / compute_type

HIP_R_32F

HIP_R_64F

HIP_C_32F

HIP_C_64F

**Mixed-regular Complex precisions**A

X / Y / compute_type

HIP_R_32F

HIP_C_32F

HIP_R_64F

HIP_C_64F


**Example**int main(int argc, char* argv[]) { // A, x, and y are m×k, k×1, and m×1 int m = 3, k = 4; int nnz_A = 8; hipsparseOperation_t transA = HIPSPARSE_OPERATION_NON_TRANSPOSE; // alpha and beta float alpha = 0.5f; float beta = 0.25f; std::vector<int> hcsrRowPtr = {0, 3, 5, 8}; std::vector<int> hcsrColInd = {0, 1, 3, 1, 2, 0, 2, 3}; std::vector<float> hcsrVal = {1, 2, 3, 4, 5, 6, 7, 8}; std::vector<float> hx(k, 1.0f); std::vector<float> hy(m, 1.0f); int* dcsrRowPtr; int* dcsrColInd; float* dcsrVal; HIP_CHECK(hipMalloc((void**)&dcsrRowPtr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&dcsrColInd, sizeof(int) * nnz_A)); HIP_CHECK(hipMalloc((void**)&dcsrVal, sizeof(float) * nnz_A)); HIP_CHECK( hipMemcpy(dcsrRowPtr, hcsrRowPtr.data(), sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrColInd, hcsrColInd.data(), sizeof(int) * nnz_A, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrVal, hcsrVal.data(), sizeof(float) * nnz_A, hipMemcpyHostToDevice)); hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); hipsparseSpMatDescr_t matA; HIPSPARSE_CHECK(hipsparseCreateCsr(&matA, m, k, nnz_A, dcsrRowPtr, dcsrColInd, dcsrVal, HIPSPARSE_INDEX_32I, HIPSPARSE_INDEX_32I, HIPSPARSE_INDEX_BASE_ZERO, HIP_R_32F)); // Allocate memory for the vector x float* dx; HIP_CHECK(hipMalloc((void**)&dx, sizeof(float) * k)); HIP_CHECK(hipMemcpy(dx, hx.data(), sizeof(float) * k, hipMemcpyHostToDevice)); hipsparseDnVecDescr_t vecX; HIPSPARSE_CHECK(hipsparseCreateDnVec(&vecX, k, dx, HIP_R_32F)); // Allocate memory for the resulting vector y float* dy; HIP_CHECK(hipMalloc((void**)&dy, sizeof(float) * m)); HIP_CHECK(hipMemcpy(dy, hy.data(), sizeof(float) * m, hipMemcpyHostToDevice)); hipsparseDnMatDescr_t vecY; HIPSPARSE_CHECK(hipsparseCreateDnVec(&vecY, m, dy, HIP_R_32F)); // Compute buffersize size_t bufferSize; HIPSPARSE_CHECK(hipsparseSpMV_bufferSize(handle, transA, &alpha, matA, vecX, &beta, vecY, HIP_R_32F, HIPSPARSE_MV_ALG_DEFAULT, &bufferSize)); void* buffer; HIP_CHECK(hipMalloc(&buffer, bufferSize)); // Preprocess operation (Optional) HIPSPARSE_CHECK(hipsparseSpMV_preprocess(handle, transA, &alpha, matA, vecX, &beta, vecY, HIP_R_32F, HIPSPARSE_MV_ALG_DEFAULT, buffer)); // Perform operation HIPSPARSE_CHECK(hipsparseSpMV(handle, transA, &alpha, matA, vecX, &beta, vecY, HIP_R_32F, HIPSPARSE_MV_ALG_DEFAULT, buffer)); // Copy device to host HIP_CHECK(hipMemcpy(hy.data(), dy, sizeof(float) * m, hipMemcpyDeviceToHost)); // Destroy matrix descriptors and handles HIPSPARSE_CHECK(hipsparseDestroySpMat(matA)); HIPSPARSE_CHECK(hipsparseDestroyDnVec(vecX)); HIPSPARSE_CHECK(hipsparseDestroyDnVec(vecY)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); HIP_CHECK(hipFree(buffer)); HIP_CHECK(hipFree(dcsrRowPtr)); HIP_CHECK(hipFree(dcsrColInd)); HIP_CHECK(hipFree(dcsrVal)); HIP_CHECK(hipFree(dx)); HIP_CHECK(hipFree(dy)); return 0; }


Note

None of the algorithms above are deterministic when \(A\) is transposed.

Note

The sparse matrix formats currently supported are:

[HIPSPARSE_FORMAT_COO](types.html#hipsparse-generic-types_8h_1a775c0e17b2f7c40076f21942e05ecb97a665d68b44910002c7ccd486e41fbf807),[HIPSPARSE_FORMAT_COO_AOS](types.html#hipsparse-generic-types_8h_1a775c0e17b2f7c40076f21942e05ecb97a1d183f5ce59240fe4d4aa366ae4292f2),[HIPSPARSE_FORMAT_CSR](types.html#hipsparse-generic-types_8h_1a775c0e17b2f7c40076f21942e05ecb97af80eddaa1c17533044b75fb76871be91), and[HIPSPARSE_FORMAT_CSC](types.html#hipsparse-generic-types_8h_1a775c0e17b2f7c40076f21942e05ecb97a5045b64ea700d831b7103a0d39a92e65).Note

Only the

[hipsparseSpMV_bufferSize](#hipsparse__spmv_8h_1a769d0d9e98c800e5bac4469d87714301)and[hipsparseSpMV](#hipsparse__spmv_8h_1aef27d7c11068e573577d681b7e6480ab)routines are non blocking and executed asynchronously with respect to the host. They may return before the actual computation has finished. The[hipsparseSpMV_preprocess](#hipsparse__spmv_8h_1a10ee6e1173d0c756cc81c21a551c8d5d)routine is blocking with respect to the host.Note

Only the

[hipsparseSpMV_bufferSize](#hipsparse__spmv_8h_1a769d0d9e98c800e5bac4469d87714301)and the[hipsparseSpMV](#hipsparse__spmv_8h_1aef27d7c11068e573577d681b7e6480ab)routines support execution in a hipGraph context. The[hipsparseSpMV_preprocess](#hipsparse__spmv_8h_1a10ee6e1173d0c756cc81c21a551c8d5d)stage does not support hipGraph.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**opA**–**[in]**matrix operation type.**alpha**–**[in]**scalar \(\alpha\).**matA**–**[in]**matrix descriptor.**vecX**–**[in]**vector descriptor.**beta**–**[in]**scalar \(\beta\).**vecY**–**[inout]**vector descriptor.**computeType**–**[in]**floating point precision for the SpMV computation.**alg**–**[in]**SpMV algorithm for the SpMV computation.**externalBuffer**–**[out]**temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`alpha`

,`matA`

,`x`

,`beta`

,`y`

or`externalBuffer`

pointer is invalid or if`opA`

,`computeType`

,`alg`

is incorrect.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`computeType`

or`alg`

is currently not supported.



## hipsparseSpMM_bufferSize()[#](#hipsparsespmm-buffersize)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpMM_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opB, const void *alpha, hipsparseConstSpMatDescr_t matA, hipsparseConstDnMatDescr_t matB, const void *beta, const[hipsparseDnMatDescr_t](types.html#_CPPv421hipsparseDnMatDescr_t)matC, hipDataType computeType,[hipsparseSpMMAlg_t](types.html#_CPPv418hipsparseSpMMAlg_t)alg, size_t *pBufferSizeInBytes)[#](#_CPPv424hipsparseSpMM_bufferSize17hipsparseHandle_t20hipsparseOperation_t20hipsparseOperation_tPKv26hipsparseConstSpMatDescr_t26hipsparseConstDnMatDescr_tPKvK21hipsparseDnMatDescr_t11hipDataType18hipsparseSpMMAlg_tP6size_t) `hipsparseSpMM_bufferSize`

computes the required user allocated buffer size needed when computing the sparse matrix multiplication with a dense matrix:\[ C := \alpha \cdot op(A) \cdot op(B) + \beta \cdot C, \]where \(op(A)\) is a sparse \(m \times k\) matrix in CSR, COO, BSR or Blocked ELL storage format, \(B\) is a dense matrix of size \(k \times n\) and \(C\) is a dense matrix of size \(m \times n\).`hipsparseSpMM_bufferSize`

supports multiple combinations of data types and compute types. See[hipsparseSpMM](#hipsparse__spmm_8h_1ae349579ee7546d7b76a5ba865fe036f0)for a complete listing of all the data type and compute type combinations available.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**opA**–**[in]**matrix operation type.**opB**–**[in]**matrix operation type.**alpha**–**[in]**scalar \(\alpha\).**matA**–**[in]**matrix descriptor.**matB**–**[in]**matrix descriptor.**beta**–**[in]**scalar \(\beta\).**matC**–**[in]**matrix descriptor.**computeType**–**[in]**floating point precision for the SpMM computation.**alg**–**[in]**SpMM algorithm for the SpMM computation.**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`alpha`

,`matA`

,`matB`

,`matC`

,`beta`

, or`pBufferSizeInBytes`

pointer is invalid.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`opA`

,`opB`

,`computeType`

or`alg`

is currently not supported.



## hipsparseSpMM_preprocess()[#](#hipsparsespmm-preprocess)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpMM_preprocess([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opB, const void *alpha, hipsparseConstSpMatDescr_t matA, hipsparseConstDnMatDescr_t matB, const void *beta, const[hipsparseDnMatDescr_t](types.html#_CPPv421hipsparseDnMatDescr_t)matC, hipDataType computeType,[hipsparseSpMMAlg_t](types.html#_CPPv418hipsparseSpMMAlg_t)alg, void *externalBuffer)[#](#_CPPv424hipsparseSpMM_preprocess17hipsparseHandle_t20hipsparseOperation_t20hipsparseOperation_tPKv26hipsparseConstSpMatDescr_t26hipsparseConstDnMatDescr_tPKvK21hipsparseDnMatDescr_t11hipDataType18hipsparseSpMMAlg_tPv) `hipsparseSpMM_preprocess`

performs the required preprocessing used when computing the sparse matrix multiplication with a dense matrix:\[ C := \alpha \cdot op(A) \cdot op(B) + \beta \cdot C, \]where \(op(A)\) is a sparse \(m \times k\) matrix in CSR, COO, BSR or Blocked ELL storage format, \(B\) is a dense matrix of size \(k \times n\) and \(C\) is a dense matrix of size \(m \times n\).`hipsparseSpMM_preprocess`

supports multiple combinations of data types and compute types. See[hipsparseSpMM](#hipsparse__spmm_8h_1ae349579ee7546d7b76a5ba865fe036f0)for a complete listing of all the data type and compute type combinations available.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**opA**–**[in]**matrix operation type.**opB**–**[in]**matrix operation type.**alpha**–**[in]**scalar \(\alpha\).**matA**–**[in]**matrix descriptor.**matB**–**[in]**matrix descriptor.**beta**–**[in]**scalar \(\beta\).**matC**–**[in]**matrix descriptor.**computeType**–**[in]**floating point precision for the SpMM computation.**alg**–**[in]**SpMM algorithm for the SpMM computation.**externalBuffer**–**[out]**temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`alpha`

,`matA`

,`matB`

,`matC`

,`beta`

, or`externalBuffer`

pointer is invalid.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`opA`

,`opB`

,`computeType`

or`alg`

is currently not supported.



## hipsparseSpMM()[#](#hipsparsespmm)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpMM([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opB, const void *alpha, hipsparseConstSpMatDescr_t matA, hipsparseConstDnMatDescr_t matB, const void *beta, const[hipsparseDnMatDescr_t](types.html#_CPPv421hipsparseDnMatDescr_t)matC, hipDataType computeType,[hipsparseSpMMAlg_t](types.html#_CPPv418hipsparseSpMMAlg_t)alg, void *externalBuffer)[#](#_CPPv413hipsparseSpMM17hipsparseHandle_t20hipsparseOperation_t20hipsparseOperation_tPKv26hipsparseConstSpMatDescr_t26hipsparseConstDnMatDescr_tPKvK21hipsparseDnMatDescr_t11hipDataType18hipsparseSpMMAlg_tPv) Compute the sparse matrix multiplication with a dense matrix.

`hipsparseSpMM`

multiplies the scalar \(\alpha\) with a sparse \(m \times k\) matrix \(op(A)\), defined in CSR, COO, BSR or Blocked ELL storage format, and the dense \(k \times n\) matrix \(op(B)\) and adds the result to the dense \(m \times n\) matrix \(C\) that is multiplied by the scalar \(\beta\), such that\[ C := \alpha \cdot op(A) \cdot op(B) + \beta \cdot C, \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if trans_A == HIPSPARSE_OPERATION_NON_TRANSPOSE} \\ A^T, & \text{if trans_A == HIPSPARSE_OPERATION_TRANSPOSE} \\ A^H, & \text{if trans_A == HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE} \end{array} \right. \end{split}\]and\[\begin{split} op(B) = \left\{ \begin{array}{ll} B, & \text{if trans_B == HIPSPARSE_OPERATION_NON_TRANSPOSE} \\ B^T, & \text{if trans_B == HIPSPARSE_OPERATION_TRANSPOSE} \\ B^H, & \text{if trans_B == HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE} \end{array} \right. \end{split}\]Both \(B\) and \(C\) can be in row or column order.`hipsparseSpMM`

requires three stages to complete. First, the user calls[hipsparseSpMM_bufferSize](#hipsparse__spmm_8h_1aba83d67b10db2ea2c8b34f505125b269)to determine the size of the required temporary storage buffer. Next, the user allocates this buffer and calls[hipsparseSpMM_preprocess](#hipsparse__spmm_8h_1acbd7a6593a68561ce00894353dc3e44e)which will perform analysis on the sparse matrix \(op(A)\). Finally, the user calls`hipsparseSpMM`

to perform the actual computation. The buffer size and preprecess routines only need to be called once for a given sparse matrix \(op(A)\) while the computation routine can be repeatedly used with different \(B\) and \(C\) matrices. Once all calls to`hipsparseSpMM`

are complete, the temporary buffer can be deallocated.As noted above, both \(B\) and \(C\) can be in row or column order (this includes mixing the order so that \(B\) is row order and \(C\) is column order and vice versa). For best performance, use row order for both \(B\) and \(C\) as this provides the best memory access.

`hipsparseSpMM`

supports multiple different algorithms. These algorithms have different trade offs depending on the sparsity pattern of the matrix, whether or not the results need to be deterministic, and how many times the sparse-matrix product will be performed.CSR Algorithms

HIPSPARSE_SPMM_CSR_ALG1

HIPSPARSE_SPMM_CSR_ALG2

HIPSPARSE_SPMM_CSR_ALG3

COO Algorithms

HIPSPARSE_SPMM_COO_ALG1

HIPSPARSE_SPMM_COO_ALG2

HIPSPARSE_SPMM_COO_ALG3

HIPSPARSE_SPMM_COO_ALG4

ELL Algorithms

HIPSPARSE_SPMM_BLOCKED_ELL_ALG1

BSR Algorithms

CUSPARSE_SPMM_BSR_ALG1

One can also pass

[HIPSPARSE_SPMM_ALG_DEFAULT](types.html#hipsparse-generic-types_8h_1ad5583e919ccd433146385003d863ee40af215e0280f3e0aa60ee2e19cca463dab)which will automatically select from the algorithms listed above based on the sparse matrix format.When A is transposed,

`hipsparseSpMM`

will revert to using[HIPSPARSE_SPMM_CSR_ALG2](types.html#hipsparse-generic-types_8h_1ad5583e919ccd433146385003d863ee40ae3bbb875651dde582e2409d36391c972)for CSR format and[HIPSPARSE_SPMM_COO_ALG1](types.html#hipsparse-generic-types_8h_1ad5583e919ccd433146385003d863ee40abd4f67f70278ccf10c2ca114d0f10d9d)for COO format regardless of algorithm selected.`hipsparseSpMM`

supports multiple combinations of data types and compute types. The tables below indicate the currently supported different data types that can be used for for the sparse matrix \(op(A)\) and the dense matrices \(op(B)\) and \(C\) and the compute type for \(\alpha\) and \(\beta\). The advantage of using different data types is to save on memory bandwidth and storage when a user application allows while performing the actual computation in a higher precision.`hipsparseSpMM`

supports[HIPSPARSE_INDEX_32I](types.html#hipsparse-generic-types_8h_1aaeacc98278238b4555b312b38a8ca3a1a39d66b98a770ce4f130cf175614bf1ee)and[HIPSPARSE_INDEX_64I](types.html#hipsparse-generic-types_8h_1aaeacc98278238b4555b312b38a8ca3a1aaf693262ac42a636addc9be11c1f534b)index precisions for storing the row pointer and column indices arrays of the sparse matrices.**Uniform Precisions:**A / B / C / compute_type

HIP_R_32F

HIP_R_64F

HIP_C_32F

HIP_C_64F

**Mixed precisions:**A / B

C

compute_type

HIP_R_8I

HIP_R_32I

HIP_R_32I

HIP_R_8I

HIP_R_32F

HIP_R_32F

HIP_R_16F

HIP_R_32F

HIP_R_32F

HIP_R_16BF

HIP_R_32F

HIP_R_32F


`hipsparseSpMM`

also supports batched computation for CSR and COO matrices. There are three supported batch modes:\[\begin{split} C_i = A \times B_i \\ C_i = A_i \times B \\ C_i = A_i \times B_i \end{split}\]The batch mode is determined by the batch count and stride passed for each matrix. For example to use the first batch mode ( \(C_i = A \times B_i\)) with 100 batches for non-transposed \(A\), \(B\), and \(C\), one passes:

\[\begin{split} batchCountA=1 \\ batchCountB=100 \\ batchCountC=100 \\ offsetsBatchStrideA=0 \\ columnsValuesBatchStrideA=0 \\ batchStrideB=k*n \\ batchStrideC=m*n \end{split}\]To use the second batch mode ( \(C_i = A_i \times B\)) one could use:\[\begin{split} batchCountA=100 \\ batchCountB=1 \\ batchCountC=100 \\ offsetsBatchStrideA=m+1 \\ columnsValuesBatchStrideA=nnz \\ batchStrideB=0 \\ batchStrideC=m*n \end{split}\]And to use the third batch mode ( \(C_i = A_i \times B_i\)) one could use:\[\begin{split} batchCountA=100 \\ batchCountB=100 \\ batchCountC=100 \\ offsetsBatchStrideA=m+1 \\ columnsValuesBatchStrideA=nnz \\ batchStrideB=k*n \\ batchStrideC=m*n \end{split}\]See examples below.**Example**int main(int argc, char* argv[]) { // A, B, and C are m×k, k×n, and m×n int m = 3, n = 5, k = 4; int ldb = n, ldc = n; int nnz_A = 8, nnz_B = 20, nnz_C = 15; hipsparseOperation_t transA = HIPSPARSE_OPERATION_NON_TRANSPOSE; hipsparseOperation_t transB = HIPSPARSE_OPERATION_NON_TRANSPOSE; hipsparseOperation_t transC = HIPSPARSE_OPERATION_NON_TRANSPOSE; hipsparseOrder_t order = HIPSPARSE_ORDER_ROW; // alpha and beta float alpha = 0.5f; float beta = 0.25f; std::vector<int> hcsrRowPtr = {0, 3, 5, 8}; std::vector<int> hcsrColInd = {0, 1, 3, 1, 2, 0, 2, 3}; std::vector<float> hcsrVal = {1, 2, 3, 4, 5, 6, 7, 8}; std::vector<float> hB(nnz_B, 1.0f); std::vector<float> hC(nnz_C, 1.0f); int* dcsrRowPtr; int* dcsrColInd; float* dcsrVal; HIP_CHECK(hipMalloc((void**)&dcsrRowPtr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&dcsrColInd, sizeof(int) * nnz_A)); HIP_CHECK(hipMalloc((void**)&dcsrVal, sizeof(float) * nnz_A)); HIP_CHECK( hipMemcpy(dcsrRowPtr, hcsrRowPtr.data(), sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrColInd, hcsrColInd.data(), sizeof(int) * nnz_A, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrVal, hcsrVal.data(), sizeof(float) * nnz_A, hipMemcpyHostToDevice)); hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); hipsparseSpMatDescr_t matA; HIPSPARSE_CHECK(hipsparseCreateCsr(&matA, m, k, nnz_A, dcsrRowPtr, dcsrColInd, dcsrVal, HIPSPARSE_INDEX_32I, HIPSPARSE_INDEX_32I, HIPSPARSE_INDEX_BASE_ZERO, HIP_R_32F)); // Allocate memory for the matrix B float* dB; HIP_CHECK(hipMalloc((void**)&dB, sizeof(float) * nnz_B)); HIP_CHECK(hipMemcpy(dB, hB.data(), sizeof(float) * nnz_B, hipMemcpyHostToDevice)); hipsparseDnMatDescr_t matB; HIPSPARSE_CHECK(hipsparseCreateDnMat(&matB, k, n, ldb, dB, HIP_R_32F, order)); // Allocate memory for the resulting matrix C float* dC; HIP_CHECK(hipMalloc((void**)&dC, sizeof(float) * nnz_C)); HIP_CHECK(hipMemcpy(dC, hC.data(), sizeof(float) * nnz_C, hipMemcpyHostToDevice)); hipsparseDnMatDescr_t matC; HIPSPARSE_CHECK(hipsparseCreateDnMat(&matC, m, n, ldc, dC, HIP_R_32F, HIPSPARSE_ORDER_ROW)); // Compute buffersize size_t bufferSize; HIPSPARSE_CHECK(hipsparseSpMM_bufferSize(handle, transA, transB, &alpha, matA, matB, &beta, matC, HIP_R_32F, HIPSPARSE_MM_ALG_DEFAULT, &bufferSize)); void* buffer; HIP_CHECK(hipMalloc(&buffer, bufferSize)); // Preprocess operation (Optional) HIPSPARSE_CHECK(hipsparseSpMM_preprocess(handle, transA, transB, &alpha, matA, matB, &beta, matC, HIP_R_32F, HIPSPARSE_MM_ALG_DEFAULT, buffer)); // Perform operation HIPSPARSE_CHECK(hipsparseSpMM(handle, transA, transB, &alpha, matA, matB, &beta, matC, HIP_R_32F, HIPSPARSE_MM_ALG_DEFAULT, buffer)); // Copy device to host HIP_CHECK(hipMemcpy(hC.data(), dC, sizeof(float) * nnz_C, hipMemcpyDeviceToHost)); // Destroy matrix descriptors and handles HIPSPARSE_CHECK(hipsparseDestroySpMat(matA)); HIPSPARSE_CHECK(hipsparseDestroyDnMat(matB)); HIPSPARSE_CHECK(hipsparseDestroyDnMat(matC)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); HIP_CHECK(hipFree(buffer)); HIP_CHECK(hipFree(dcsrRowPtr)); HIP_CHECK(hipFree(dcsrColInd)); HIP_CHECK(hipFree(dcsrVal)); HIP_CHECK(hipFree(dB)); HIP_CHECK(hipFree(dC)); return 0; }


- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**opA**–**[in]**matrix operation type.**opB**–**[in]**matrix operation type.**alpha**–**[in]**scalar \(\alpha\).**matA**–**[in]**matrix descriptor.**matB**–**[in]**matrix descriptor.**beta**–**[in]**scalar \(\beta\).**matC**–**[in]**matrix descriptor.**computeType**–**[in]**floating point precision for the SpMM computation.**alg**–**[in]**SpMM algorithm for the SpMM computation.**externalBuffer**–**[out]**temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`alpha`

,`matA`

,`matB`

,`matC`

,`beta`

, or`externalBuffer`

pointer is invalid.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`opA`

,`opB`

,`computeType`

or`alg`

is currently not supported.



## hipsparseSpGEMM_createDescr()[#](#hipsparsespgemm-createdescr)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpGEMM_createDescr([hipsparseSpGEMMDescr_t](types.html#_CPPv422hipsparseSpGEMMDescr_t)*descr)[#](#_CPPv427hipsparseSpGEMM_createDescrP22hipsparseSpGEMMDescr_t) `hipsparseSpGEMM_createDescr`

creates a sparse matrix sparse matrix product descriptor. It should be destroyed at the end using[hipsparseSpGEMM_destroyDescr()](#hipsparse__spgemm_8h_1a539207acdf900526b27a20a9ca923773).

## hipsparseSpGEMM_destroyDescr()[#](#hipsparsespgemm-destroydescr)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpGEMM_destroyDescr([hipsparseSpGEMMDescr_t](types.html#_CPPv422hipsparseSpGEMMDescr_t)descr)[#](#_CPPv428hipsparseSpGEMM_destroyDescr22hipsparseSpGEMMDescr_t) `hipsparseSpGEMM_destroyDescr`

destroys a sparse matrix sparse matrix product descriptor and releases all resources used by the descriptor.

## hipsparseSpGEMM_workEstimation()[#](#hipsparsespgemm-workestimation)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpGEMM_workEstimation([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opB, const void *alpha, hipsparseConstSpMatDescr_t matA, hipsparseConstSpMatDescr_t matB, const void *beta,[hipsparseSpMatDescr_t](types.html#_CPPv421hipsparseSpMatDescr_t)matC, hipDataType computeType,[hipsparseSpGEMMAlg_t](types.html#_CPPv420hipsparseSpGEMMAlg_t)alg,[hipsparseSpGEMMDescr_t](types.html#_CPPv422hipsparseSpGEMMDescr_t)spgemmDescr, size_t *bufferSize1, void *externalBuffer1)[#](#_CPPv430hipsparseSpGEMM_workEstimation17hipsparseHandle_t20hipsparseOperation_t20hipsparseOperation_tPKv26hipsparseConstSpMatDescr_t26hipsparseConstSpMatDescr_tPKv21hipsparseSpMatDescr_t11hipDataType20hipsparseSpGEMMAlg_t22hipsparseSpGEMMDescr_tP6size_tPv) Work estimation step of the sparse matrix sparse matrix product:

\[ C' := \alpha \cdot op(A) \cdot op(B) + \beta \cdot C, \]where \(C'\), \(A\), \(B\), \(C\) are sparse matrices and \(C'\) and \(C\) have the same sparsity pattern.`hipsparseSpGEMM_workEstimation`

is called twice. We call it to compute the size of the first required user allocated buffer. After this buffer size is determined, the user allocates it and calls`hipsparseSpGEMM_workEstimation`

a second time with the newly allocated buffer passed in. This second call inspects the matrices \(A\) and \(B\) to determine the number of intermediate products that will result from multipltying \(A\) and \(B\) together.`hipsparseSpGEMM_workEstimation`

supports multiple combinations of data types and compute types. See[hipsparseSpGEMM_copy](#hipsparse__spgemm_8h_1a299610cce161dd7ebb36dcc83a6d068d)for a complete listing of all the data type and compute type combinations available.**Example (See full example below)**void* dBuffer1 = NULL; size_t bufferSize1 = 0; hipsparseSpGEMMDescr_t spgemmDesc; hipsparseSpGEMM_createDescr(&spgemmDesc); size_t bufferSize1 = 0; hipsparseSpGEMM_workEstimation(handle, opA, opB, &alpha, matA, matB, &beta, matC, computeType, HIPSPARSE_SPGEMM_DEFAULT, spgemmDesc, &bufferSize1, NULL); hipMalloc((void**) &dBuffer1, bufferSize1); // Determine number of intermediate product when computing A * B hipsparseSpGEMM_workEstimation(handle, opA, opB, &alpha, matA, matB, &beta, matC, computeType, HIPSPARSE_SPGEMM_DEFAULT, spgemmDesc, &bufferSize1, dBuffer1);


- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**opA**–**[in]**sparse matrix \(A\) operation type.**opB**–**[in]**sparse matrix \(B\) operation type.**alpha**–**[in]**scalar \(\alpha\).**matA**–**[in]**sparse matrix \(A\) descriptor.**matB**–**[in]**sparse matrix \(B\) descriptor.**beta**–**[in]**scalar \(\beta\).**matC**–**[out]**sparse matrix \(C\) descriptor.**computeType**–**[in]**floating point precision for the SpGEMM computation.**alg**–**[in]**SpGEMM algorithm for the SpGEMM computation.**spgemmDescr**–**[in]**SpGEMM descriptor.**bufferSize1**–**[out]**number of bytes of the temporary storage buffer.**externalBuffer1**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`alpha`

,`beta`

,`matA`

,`matB`

,`matC`

or`bufferSize1`

pointer is invalid.**HIPSPARSE_STATUS_ALLOC_FAILED**– additional buffer for long rows could not be allocated.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`opA`

!=[HIPSPARSE_OPERATION_NON_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141a270f0124eb0d0ac15c3e7afb18064547)or`opB`

!=[HIPSPARSE_OPERATION_NON_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141a270f0124eb0d0ac15c3e7afb18064547).



## hipsparseSpGEMM_compute()[#](#hipsparsespgemm-compute)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpGEMM_compute([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opB, const void *alpha, hipsparseConstSpMatDescr_t matA, hipsparseConstSpMatDescr_t matB, const void *beta,[hipsparseSpMatDescr_t](types.html#_CPPv421hipsparseSpMatDescr_t)matC, hipDataType computeType,[hipsparseSpGEMMAlg_t](types.html#_CPPv420hipsparseSpGEMMAlg_t)alg,[hipsparseSpGEMMDescr_t](types.html#_CPPv422hipsparseSpGEMMDescr_t)spgemmDescr, size_t *bufferSize2, void *externalBuffer2)[#](#_CPPv423hipsparseSpGEMM_compute17hipsparseHandle_t20hipsparseOperation_t20hipsparseOperation_tPKv26hipsparseConstSpMatDescr_t26hipsparseConstSpMatDescr_tPKv21hipsparseSpMatDescr_t11hipDataType20hipsparseSpGEMMAlg_t22hipsparseSpGEMMDescr_tP6size_tPv) Compute step of the sparse matrix sparse matrix product:

\[ C' := \alpha \cdot op(A) \cdot op(B) + \beta \cdot C, \]where \(C'\), \(A\), \(B\), \(C\) are sparse matrices and \(C'\) and \(C\) have the same sparsity pattern.`hipsparseSpGEMM_compute`

is called twice. First to compute the size of the second required user allocated buffer. After this buffer size is determined, the user allocates it and calls`hipsparseSpGEMM_compute`

a second time with the newly allocated buffer passed in. This second call performs the actual computation of \(C' = \alpha \cdot A \cdot B\) (the result is stored in the temporary buffers).`hipsparseSpGEMM_compute`

supports multiple combinations of data types and compute types. See[hipsparseSpGEMM_copy](#hipsparse__spgemm_8h_1a299610cce161dd7ebb36dcc83a6d068d)for a complete listing of all the data type and compute type combinations available.**Example (See full example below)**void* dBuffer2 = NULL; size_t bufferSize2 = 0; size_t bufferSize2 = 0; hipsparseSpGEMM_compute(handle, opA, opB, &alpha, matA, matB, &beta, matC, computeType, HIPSPARSE_SPGEMM_DEFAULT, spgemmDesc, &bufferSize2, NULL); hipMalloc((void**) &dBuffer2, bufferSize2); // compute the intermediate product of A * B hipsparseSpGEMM_compute(handle, opA, opB, &alpha, matA, matB, &beta, matC, computeType, HIPSPARSE_SPGEMM_DEFAULT, spgemmDesc, &bufferSize2, dBuffer2);


- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**opA**–**[in]**sparse matrix \(A\) operation type.**opB**–**[in]**sparse matrix \(B\) operation type.**alpha**–**[in]**scalar \(\alpha\).**matA**–**[in]**sparse matrix \(A\) descriptor.**matB**–**[in]**sparse matrix \(B\) descriptor.**beta**–**[in]**scalar \(\beta\).**matC**–**[out]**sparse matrix \(C\) descriptor.**computeType**–**[in]**floating point precision for the SpGEMM computation.**alg**–**[in]**SpGEMM algorithm for the SpGEMM computation.**spgemmDescr**–**[in]**SpGEMM descriptor.**bufferSize2**–**[out]**number of bytes of the temporary storage buffer.**externalBuffer2**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`alpha`

,`beta`

,`matA`

,`matB`

,`matC`

or`bufferSize2`

pointer is invalid.**HIPSPARSE_STATUS_ALLOC_FAILED**– additional buffer for long rows could not be allocated.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`opA`

!=[HIPSPARSE_OPERATION_NON_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141a270f0124eb0d0ac15c3e7afb18064547)or`opB`

!=[HIPSPARSE_OPERATION_NON_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141a270f0124eb0d0ac15c3e7afb18064547).



## hipsparseSpGEMM_copy()[#](#hipsparsespgemm-copy)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpGEMM_copy([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opB, const void *alpha, hipsparseConstSpMatDescr_t matA, hipsparseConstSpMatDescr_t matB, const void *beta,[hipsparseSpMatDescr_t](types.html#_CPPv421hipsparseSpMatDescr_t)matC, hipDataType computeType,[hipsparseSpGEMMAlg_t](types.html#_CPPv420hipsparseSpGEMMAlg_t)alg,[hipsparseSpGEMMDescr_t](types.html#_CPPv422hipsparseSpGEMMDescr_t)spgemmDescr)[#](#_CPPv420hipsparseSpGEMM_copy17hipsparseHandle_t20hipsparseOperation_t20hipsparseOperation_tPKv26hipsparseConstSpMatDescr_t26hipsparseConstSpMatDescr_tPKv21hipsparseSpMatDescr_t11hipDataType20hipsparseSpGEMMAlg_t22hipsparseSpGEMMDescr_t) Copy step of the sparse matrix sparse matrix product:

\[ C' := \alpha \cdot op(A) \cdot op(B) + \beta \cdot C, \]where \(C'\), \(A\), \(B\), \(C\) are sparse matrices and \(C'\) and \(C\) have the same sparsity pattern.`hipsparseSpGEMM_copy`

is called once to copy the results (that are currently stored in the temporary arrays) to the output sparse matrix. If \(\beta != 0\), then the \(beta \cdot C\) portion of the computation: \(C' = \alpha \cdot A \cdot B + \beta * C\) is handled. This is possible because \(C'\) and \(C\) must have the same sparsity pattern.`hipsparseSpGEMM_copy`

supports multiple combinations of data types and compute types. The tables below indicate the currently supported different data types that can be used for for the sparse matrices \(op(A)\), \(op(B)\), \(C\), and \(C'\) and the compute type for \(\alpha\) and \(\beta\). The advantage of using different data types is to save on memory bandwidth and storage when a user application allows while performing the actual computation in a higher precision.`hipsparseSpGEMM_copy`

supports[HIPSPARSE_INDEX_32I](types.html#hipsparse-generic-types_8h_1aaeacc98278238b4555b312b38a8ca3a1a39d66b98a770ce4f130cf175614bf1ee)and[HIPSPARSE_INDEX_64I](types.html#hipsparse-generic-types_8h_1aaeacc98278238b4555b312b38a8ca3a1aaf693262ac42a636addc9be11c1f534b)index precisions for storing the row pointer and row/column indices arrays of the sparse matrices.**Uniform Precisions:**A / B / C / C’ / compute_type

HIP_R_32F

HIP_R_64F

HIP_C_32F

HIP_C_64F


**Example (Full example)**int main(int argc, char* argv[]) { int m = 2; int k = 2; int n = 3; int nnzA = 4; int nnzB = 4; float alpha{1.0f}; float beta{0.0f}; hipsparseOperation_t opA = HIPSPARSE_OPERATION_NON_TRANSPOSE; hipsparseOperation_t opB = HIPSPARSE_OPERATION_NON_TRANSPOSE; hipDataType computeType = HIP_R_32F; // A, B, and C are m×k, k×n, and m×n // A std::vector<int> hcsrRowPtrA = {0, 2, 4}; std::vector<int> hcsrColIndA = {0, 1, 0, 1}; std::vector<float> hcsrValA = {1.0f, 2.0f, 3.0f, 4.0f}; // B std::vector<int> hcsrRowPtrB = {0, 2, 4}; std::vector<int> hcsrColIndB = {1, 2, 0, 2}; std::vector<float> hcsrValB = {5.0f, 6.0f, 7.0f, 8.0f}; // Device memory management: Allocate and copy A, B int* dcsrRowPtrA; int* dcsrColIndA; float* dcsrValA; int* dcsrRowPtrB; int* dcsrColIndB; float* dcsrValB; int* dcsrRowPtrC; int* dcsrColIndC; float* dcsrValC; HIP_CHECK(hipMalloc((void**)&dcsrRowPtrA, (m + 1) * sizeof(int))); HIP_CHECK(hipMalloc((void**)&dcsrColIndA, nnzA * sizeof(int))); HIP_CHECK(hipMalloc((void**)&dcsrValA, nnzA * sizeof(float))); HIP_CHECK(hipMalloc((void**)&dcsrRowPtrB, (k + 1) * sizeof(int))); HIP_CHECK(hipMalloc((void**)&dcsrColIndB, nnzB * sizeof(int))); HIP_CHECK(hipMalloc((void**)&dcsrValB, nnzB * sizeof(float))); HIP_CHECK(hipMalloc((void**)&dcsrRowPtrC, (m + 1) * sizeof(int))); HIP_CHECK( hipMemcpy(dcsrRowPtrA, hcsrRowPtrA.data(), (m + 1) * sizeof(int), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsrColIndA, hcsrColIndA.data(), nnzA * sizeof(int), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrValA, hcsrValA.data(), nnzA * sizeof(float), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsrRowPtrB, hcsrRowPtrB.data(), (k + 1) * sizeof(int), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsrColIndB, hcsrColIndB.data(), nnzB * sizeof(int), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrValB, hcsrValB.data(), nnzB * sizeof(float), hipMemcpyHostToDevice)); hipsparseSpMatDescr_t matA, matB, matC; hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // Create sparse matrix A in CSR format HIPSPARSE_CHECK(hipsparseCreateCsr(&matA, m, k, nnzA, dcsrRowPtrA, dcsrColIndA, dcsrValA, HIPSPARSE_INDEX_32I, HIPSPARSE_INDEX_32I, HIPSPARSE_INDEX_BASE_ZERO, HIP_R_32F)); HIPSPARSE_CHECK(hipsparseCreateCsr(&matB, k, n, nnzB, dcsrRowPtrB, dcsrColIndB, dcsrValB, HIPSPARSE_INDEX_32I, HIPSPARSE_INDEX_32I, HIPSPARSE_INDEX_BASE_ZERO, HIP_R_32F)); HIPSPARSE_CHECK(hipsparseCreateCsr(&matC, m, n, 0, dcsrRowPtrC, NULL, NULL, HIPSPARSE_INDEX_32I, HIPSPARSE_INDEX_32I, HIPSPARSE_INDEX_BASE_ZERO, HIP_R_32F)); hipsparseSpGEMMDescr_t spgemmDesc; HIPSPARSE_CHECK(hipsparseSpGEMM_createDescr(&spgemmDesc)); void* dBuffer1 = NULL; void* dBuffer2 = NULL; size_t bufferSize1 = 0; size_t bufferSize2 = 0; // Determine size of first user allocated buffer HIPSPARSE_CHECK(hipsparseSpGEMM_workEstimation(handle, opA, opB, &alpha, matA, matB, &beta, matC, computeType, HIPSPARSE_SPGEMM_DEFAULT, spgemmDesc, &bufferSize1, NULL)); HIP_CHECK(hipMalloc((void**)&dBuffer1, bufferSize1)); // Inspect the matrices A and B to determine the number of intermediate product in // C = alpha * A * B HIPSPARSE_CHECK(hipsparseSpGEMM_workEstimation(handle, opA, opB, &alpha, matA, matB, &beta, matC, computeType, HIPSPARSE_SPGEMM_DEFAULT, spgemmDesc, &bufferSize1, dBuffer1)); // Determine size of second user allocated buffer HIPSPARSE_CHECK(hipsparseSpGEMM_compute(handle, opA, opB, &alpha, matA, matB, &beta, matC, computeType, HIPSPARSE_SPGEMM_DEFAULT, spgemmDesc, &bufferSize2, NULL)); HIP_CHECK(hipMalloc((void**)&dBuffer2, bufferSize2)); // Compute C = alpha * A * B and store result in temporary buffers HIPSPARSE_CHECK(hipsparseSpGEMM_compute(handle, opA, opB, &alpha, matA, matB, &beta, matC, computeType, HIPSPARSE_SPGEMM_DEFAULT, spgemmDesc, &bufferSize2, dBuffer2)); // Get matrix C non-zero entries C_nnz1 int64_t C_num_rows1, C_num_cols1, C_nnz1; HIPSPARSE_CHECK(hipsparseSpMatGetSize(matC, &C_num_rows1, &C_num_cols1, &C_nnz1)); // Allocate the CSR structures for the matrix C HIP_CHECK(hipMalloc((void**)&dcsrColIndC, C_nnz1 * sizeof(int))); HIP_CHECK(hipMalloc((void**)&dcsrValC, C_nnz1 * sizeof(float))); // Update matC with the new pointers HIPSPARSE_CHECK(hipsparseCsrSetPointers(matC, dcsrRowPtrC, dcsrColIndC, dcsrValC)); // Copy the final products to the matrix C HIPSPARSE_CHECK(hipsparseSpGEMM_copy(handle, opA, opB, &alpha, matA, matB, &beta, matC, computeType, HIPSPARSE_SPGEMM_DEFAULT, spgemmDesc)); std::vector<int> hcsrRowPtrC(m + 1); std::vector<int> hcsrColIndC(C_nnz1); std::vector<float> hcsrValC(C_nnz1); // Copy back to the host HIP_CHECK( hipMemcpy(hcsrRowPtrC.data(), dcsrRowPtrC, sizeof(int) * (m + 1), hipMemcpyDeviceToHost)); HIP_CHECK( hipMemcpy(hcsrColIndC.data(), dcsrColIndC, sizeof(int) * C_nnz1, hipMemcpyDeviceToHost)); HIP_CHECK(hipMemcpy(hcsrValC.data(), dcsrValC, sizeof(float) * C_nnz1, hipMemcpyDeviceToHost)); std::cout << "C" << std::endl; for(int i = 0; i < m; i++) { int start = hcsrRowPtrC[i]; int end = hcsrRowPtrC[i + 1]; std::vector<float> temp(n, 0.0f); for(int j = start; j < end; j++) { temp[hcsrColIndC[j]] = hcsrValC[j]; } for(int j = 0; j < n; j++) { std::cout << temp[j] << " "; } std::cout << "" << std::endl; } std::cout << "" << std::endl; // Destroy matrix descriptors and handles HIPSPARSE_CHECK(hipsparseSpGEMM_destroyDescr(spgemmDesc)); HIPSPARSE_CHECK(hipsparseDestroySpMat(matA)); HIPSPARSE_CHECK(hipsparseDestroySpMat(matB)); HIPSPARSE_CHECK(hipsparseDestroySpMat(matC)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); // Free device memory HIP_CHECK(hipFree(dBuffer1)); HIP_CHECK(hipFree(dBuffer2)); return 0; }


Note

The two user allocated temporary buffers can only be freed after the call to

`hipsparseSpGEMM_copy`

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**opA**–**[in]**sparse matrix \(A\) operation type.**opB**–**[in]**sparse matrix \(B\) operation type.**alpha**–**[in]**scalar \(\alpha\).**matA**–**[in]**sparse matrix \(A\) descriptor.**matB**–**[in]**sparse matrix \(B\) descriptor.**beta**–**[in]**scalar \(\beta\).**matC**–**[out]**sparse matrix \(C\) descriptor.**computeType**–**[in]**floating point precision for the SpGEMM computation.**alg**–**[in]**SpGEMM algorithm for the SpGEMM computation.**spgemmDescr**–**[in]**SpGEMM descriptor.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`alpha`

,`beta`

,`matA`

,`matB`

,`matC`

pointer is invalid.**HIPSPARSE_STATUS_ALLOC_FAILED**– additional buffer for long rows could not be allocated.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`opA`

!=[HIPSPARSE_OPERATION_NON_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141a270f0124eb0d0ac15c3e7afb18064547)or`opB`

!=[HIPSPARSE_OPERATION_NON_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141a270f0124eb0d0ac15c3e7afb18064547).



## hipsparseSpGEMMreuse_workEstimation()[#](#hipsparsespgemmreuse-workestimation)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpGEMMreuse_workEstimation([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opB, hipsparseConstSpMatDescr_t matA, hipsparseConstSpMatDescr_t matB,[hipsparseSpMatDescr_t](types.html#_CPPv421hipsparseSpMatDescr_t)matC,[hipsparseSpGEMMAlg_t](types.html#_CPPv420hipsparseSpGEMMAlg_t)alg,[hipsparseSpGEMMDescr_t](types.html#_CPPv422hipsparseSpGEMMDescr_t)spgemmDescr, size_t *bufferSize1, void *externalBuffer1)[#](#_CPPv435hipsparseSpGEMMreuse_workEstimation17hipsparseHandle_t20hipsparseOperation_t20hipsparseOperation_t26hipsparseConstSpMatDescr_t26hipsparseConstSpMatDescr_t21hipsparseSpMatDescr_t20hipsparseSpGEMMAlg_t22hipsparseSpGEMMDescr_tP6size_tPv) Work estimation step of the sparse matrix sparse matrix product:

\[ C' := \alpha \cdot op(A) \cdot op(B) + \beta \cdot C, \]where \(C'\), \(A\), \(B\), \(C\) are sparse matrices and \(C'\) and \(C\) have the same sparsity pattern.`hipsparseSpGEMMreuse_workEstimation`

is called twice. We call it to compute the size of the first required user allocated buffer. After this buffer size is determined, the user allocates it and calls`hipsparseSpGEMMreuse_workEstimation`

a second time with the newly allocated buffer passed in. This second call inspects the matrices \(A\) and \(B\) to determine the number of intermediate products that will result from multipltying \(A\) and \(B\) together.**Example (See full example below)**void* dBuffer1 = NULL; size_t bufferSize1 = 0; hipsparseSpGEMMDescr_t spgemmDesc; hipsparseSpGEMM_createDescr(&spgemmDesc); size_t bufferSize1 = 0; hipsparseSpGEMMreuse_workEstimation(handle, opA, opB, matA, matB, matC, HIPSPARSE_SPGEMM_DEFAULT, spgemmDesc, &bufferSize1, NULL); hipMalloc((void**) &dBuffer1, bufferSize1); // Determine number of intermediate product when computing A * B hipsparseSpGEMMreuse_workEstimation(handle, opA, opB, matA, matB, matC, HIPSPARSE_SPGEMM_DEFAULT, spgemmDesc, &bufferSize1, dBuffer1);


- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**opA**–**[in]**sparse matrix \(A\) operation type.**opB**–**[in]**sparse matrix \(B\) operation type.**matA**–**[in]**sparse matrix \(A\) descriptor.**matB**–**[in]**sparse matrix \(B\) descriptor.**matC**–**[out]**sparse matrix \(C\) descriptor.**alg**–**[in]**SpGEMM algorithm for the SpGEMM computation.**spgemmDescr**–**[in]**SpGEMM descriptor.**bufferSize1**–**[out]**number of bytes of the temporary storage buffer.**externalBuffer1**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`matA`

,`matB`

,`matC`

or`bufferSize1`

pointer is invalid.**HIPSPARSE_STATUS_ALLOC_FAILED**– additional buffer for long rows could not be allocated.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`opA`

!=[HIPSPARSE_OPERATION_NON_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141a270f0124eb0d0ac15c3e7afb18064547)or`opB`

!=[HIPSPARSE_OPERATION_NON_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141a270f0124eb0d0ac15c3e7afb18064547).



## hipsparseSpGEMMreuse_nnz()[#](#hipsparsespgemmreuse-nnz)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpGEMMreuse_nnz([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opB, hipsparseConstSpMatDescr_t matA, hipsparseConstSpMatDescr_t matB,[hipsparseSpMatDescr_t](types.html#_CPPv421hipsparseSpMatDescr_t)matC,[hipsparseSpGEMMAlg_t](types.html#_CPPv420hipsparseSpGEMMAlg_t)alg,[hipsparseSpGEMMDescr_t](types.html#_CPPv422hipsparseSpGEMMDescr_t)spgemmDescr, size_t *bufferSize2, void *externalBuffer2, size_t *bufferSize3, void *externalBuffer3, size_t *bufferSize4, void *externalBuffer4)[#](#_CPPv424hipsparseSpGEMMreuse_nnz17hipsparseHandle_t20hipsparseOperation_t20hipsparseOperation_t26hipsparseConstSpMatDescr_t26hipsparseConstSpMatDescr_t21hipsparseSpMatDescr_t20hipsparseSpGEMMAlg_t22hipsparseSpGEMMDescr_tP6size_tPvP6size_tPvP6size_tPv) Nnz calculation step of the sparse matrix sparse matrix product:

\[ C' := \alpha \cdot op(A) \cdot op(B) + \beta \cdot C, \]where \(C'\), \(A\), \(B\), \(C\) are sparse matrices and \(C'\) and \(C\) have the same sparsity pattern.**Example (See full example below)**// Determine size of second, third, and fourth user allocated buffer hipsparseSpGEMMreuse_nnz(handle, opA, opB, matA, matB, matC, HIPSPARSE_SPGEMM_DEFAULT, spgemmDesc, &bufferSize2, NULL, &bufferSize3, NULL, &bufferSize4, NULL); hipMalloc((void**) &dBuffer2, bufferSize2); hipMalloc((void**) &dBuffer3, bufferSize3); hipMalloc((void**) &dBuffer4, bufferSize4); // COmpute sparsity pattern of C matrix and store in temporary buffers hipsparseSpGEMMreuse_nnz(handle, opA, opB, matA, matB, matC, HIPSPARSE_SPGEMM_DEFAULT, spgemmDesc, &bufferSize2, dBuffer2, &bufferSize3, dBuffer3, &bufferSize4, dBuffer4); // We can now free buffer 1 and 2 hipFree(dBuffer1); hipFree(dBuffer2);


- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**opA**–**[in]**sparse matrix \(A\) operation type.**opB**–**[in]**sparse matrix \(B\) operation type.**matA**–**[in]**sparse matrix \(A\) descriptor.**matB**–**[in]**sparse matrix \(B\) descriptor.**matC**–**[out]**sparse matrix \(C\) descriptor.**alg**–**[in]**SpGEMM algorithm for the SpGEMM computation.**spgemmDescr**–**[in]**SpGEMM descriptor.**bufferSize2**–**[out]**number of bytes of the temporary storage`externalBuffer2`

.**externalBuffer2**–**[in]**temporary storage buffer allocated by the user.**bufferSize3**–**[out]**number of bytes of the temporary storage`externalBuffer3`

.**externalBuffer3**–**[in]**temporary storage buffer allocated by the user.**bufferSize4**–**[out]**number of bytes of the temporary storage`externalBuffer4`

.**externalBuffer4**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`matA`

,`matB`

,`matC`

,`bufferSize2`

,`bufferSize3`

or`bufferSize4`

pointer is invalid.**HIPSPARSE_STATUS_ALLOC_FAILED**– additional buffer for long rows could not be allocated.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`opA`

!=[HIPSPARSE_OPERATION_NON_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141a270f0124eb0d0ac15c3e7afb18064547)or`opB`

!=[HIPSPARSE_OPERATION_NON_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141a270f0124eb0d0ac15c3e7afb18064547).



## hipsparseSpGEMMreuse_copy()[#](#hipsparsespgemmreuse-copy)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpGEMMreuse_copy([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opB, hipsparseConstSpMatDescr_t matA, hipsparseConstSpMatDescr_t matB,[hipsparseSpMatDescr_t](types.html#_CPPv421hipsparseSpMatDescr_t)matC,[hipsparseSpGEMMAlg_t](types.html#_CPPv420hipsparseSpGEMMAlg_t)alg,[hipsparseSpGEMMDescr_t](types.html#_CPPv422hipsparseSpGEMMDescr_t)spgemmDescr, size_t *bufferSize5, void *externalBuffer5)[#](#_CPPv425hipsparseSpGEMMreuse_copy17hipsparseHandle_t20hipsparseOperation_t20hipsparseOperation_t26hipsparseConstSpMatDescr_t26hipsparseConstSpMatDescr_t21hipsparseSpMatDescr_t20hipsparseSpGEMMAlg_t22hipsparseSpGEMMDescr_tP6size_tPv) Copy step of the sparse matrix sparse matrix product:

\[ C' := \alpha \cdot op(A) \cdot op(B) + \beta \cdot C, \]where \(C'\), \(A\), \(B\), \(C\) are sparse matrices and \(C'\) and \(C\) have the same sparsity pattern.**Example (See full example below)**// Get matrix C non-zero entries nnzC int64_t rowsC, colsC, nnzC; hipsparseSpMatGetSize(matC, &rowsC, &colsC, &nnzC); // Allocate matrix C hipMalloc((void**) &dcsrColIndC, sizeof(int) * nnzC); hipMalloc((void**) &dcsrValC, sizeof(float) * nnzC); // Update matC with the new pointers. The C values array can be filled with data here // which is used if beta != 0. hipsparseCsrSetPointers(matC, dcsrRowPtrC, dcsrColIndC, dcsrValC); // Determine size of fifth user allocated buffer hipsparseSpGEMMreuse_copy(handle, opA, opB, matA, matB, matC, HIPSPARSE_SPGEMM_DEFAULT, spgemmDesc, &bufferSize5, NULL); hipMalloc((void**) &dBuffer5, bufferSize5); // Copy data from temporary buffers to the newly allocated C matrix hipsparseSpGEMMreuse_copy(handle, opA, opB, matA, matB, matC, HIPSPARSE_SPGEMM_DEFAULT, spgemmDesc, &bufferSize5, dBuffer5); // We can now free buffer 3 hipFree(dBuffer3);


- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**opA**–**[in]**sparse matrix \(A\) operation type.**opB**–**[in]**sparse matrix \(B\) operation type.**matA**–**[in]**sparse matrix \(A\) descriptor.**matB**–**[in]**sparse matrix \(B\) descriptor.**matC**–**[out]**sparse matrix \(C\) descriptor.**alg**–**[in]**SpGEMM algorithm for the SpGEMM computation.**spgemmDescr**–**[in]**SpGEMM descriptor.**bufferSize5**–**[out]**number of bytes of the temporary storage`externalBuffer5`

.**externalBuffer5**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`matA`

,`matB`

,`matC`

, or`bufferSize5`

pointer is invalid.**HIPSPARSE_STATUS_ALLOC_FAILED**– additional buffer for long rows could not be allocated.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`opA`

!=[HIPSPARSE_OPERATION_NON_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141a270f0124eb0d0ac15c3e7afb18064547)or`opB`

!=[HIPSPARSE_OPERATION_NON_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141a270f0124eb0d0ac15c3e7afb18064547).



## hipsparseSpGEMMreuse_compute()[#](#hipsparsespgemmreuse-compute)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpGEMMreuse_compute([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opB, const void *alpha, hipsparseConstSpMatDescr_t matA, hipsparseConstSpMatDescr_t matB, const void *beta,[hipsparseSpMatDescr_t](types.html#_CPPv421hipsparseSpMatDescr_t)matC, hipDataType computeType,[hipsparseSpGEMMAlg_t](types.html#_CPPv420hipsparseSpGEMMAlg_t)alg,[hipsparseSpGEMMDescr_t](types.html#_CPPv422hipsparseSpGEMMDescr_t)spgemmDescr)[#](#_CPPv428hipsparseSpGEMMreuse_compute17hipsparseHandle_t20hipsparseOperation_t20hipsparseOperation_tPKv26hipsparseConstSpMatDescr_t26hipsparseConstSpMatDescr_tPKv21hipsparseSpMatDescr_t11hipDataType20hipsparseSpGEMMAlg_t22hipsparseSpGEMMDescr_t) Copy step of the sparse matrix sparse matrix product:

\[ C' := \alpha \cdot op(A) \cdot op(B) + \beta \cdot C, \]where \(C'\), \(A\), \(B\), \(C\) are sparse matrices and \(C'\) and \(C\) have the same sparsity pattern.**Example**int main(int argc, char* argv[]) { int m = 2; int k = 2; int n = 3; int nnzA = 4; int nnzB = 4; float alpha{1.0f}; float beta{0.0f}; hipsparseOperation_t opA = HIPSPARSE_OPERATION_NON_TRANSPOSE; hipsparseOperation_t opB = HIPSPARSE_OPERATION_NON_TRANSPOSE; hipDataType computeType = HIP_R_32F; // A, B, and C are m×k, k×n, and m×n // A std::vector<int> hcsrRowPtrA = {0, 2, 4}; std::vector<int> hcsrColIndA = {0, 1, 0, 1}; std::vector<float> hcsrValA = {1.0f, 2.0f, 3.0f, 4.0f}; // B std::vector<int> hcsrRowPtrB = {0, 2, 4}; std::vector<int> hcsrColIndB = {1, 2, 0, 2}; std::vector<float> hcsrValB = {5.0f, 6.0f, 7.0f, 8.0f}; // Device memory management: Allocate and copy A, B int* dcsrRowPtrA; int* dcsrColIndA; float* dcsrValA; int* dcsrRowPtrB; int* dcsrColIndB; float* dcsrValB; int* dcsrRowPtrC; int* dcsrColIndC; float* dcsrValC; HIP_CHECK(hipMalloc((void**)&dcsrRowPtrA, (m + 1) * sizeof(int))); HIP_CHECK(hipMalloc((void**)&dcsrColIndA, nnzA * sizeof(int))); HIP_CHECK(hipMalloc((void**)&dcsrValA, nnzA * sizeof(float))); HIP_CHECK(hipMalloc((void**)&dcsrRowPtrB, (k + 1) * sizeof(int))); HIP_CHECK(hipMalloc((void**)&dcsrColIndB, nnzB * sizeof(int))); HIP_CHECK(hipMalloc((void**)&dcsrValB, nnzB * sizeof(float))); HIP_CHECK(hipMalloc((void**)&dcsrRowPtrC, (m + 1) * sizeof(int))); HIP_CHECK( hipMemcpy(dcsrRowPtrA, hcsrRowPtrA.data(), (m + 1) * sizeof(int), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsrColIndA, hcsrColIndA.data(), nnzA * sizeof(int), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrValA, hcsrValA.data(), nnzA * sizeof(float), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsrRowPtrB, hcsrRowPtrB.data(), (k + 1) * sizeof(int), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsrColIndB, hcsrColIndB.data(), nnzB * sizeof(int), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrValB, hcsrValB.data(), nnzB * sizeof(float), hipMemcpyHostToDevice)); hipsparseHandle_t handle = NULL; hipsparseSpMatDescr_t matA, matB, matC; void* dBuffer1 = NULL; void* dBuffer2 = NULL; void* dBuffer3 = NULL; void* dBuffer4 = NULL; void* dBuffer5 = NULL; size_t bufferSize1 = 0; size_t bufferSize2 = 0; size_t bufferSize3 = 0; size_t bufferSize4 = 0; size_t bufferSize5 = 0; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // Create sparse matrix A in CSR format HIPSPARSE_CHECK(hipsparseCreateCsr(&matA, m, k, nnzA, dcsrRowPtrA, dcsrColIndA, dcsrValA, HIPSPARSE_INDEX_32I, HIPSPARSE_INDEX_32I, HIPSPARSE_INDEX_BASE_ZERO, HIP_R_32F)); HIPSPARSE_CHECK(hipsparseCreateCsr(&matB, k, n, nnzB, dcsrRowPtrB, dcsrColIndB, dcsrValB, HIPSPARSE_INDEX_32I, HIPSPARSE_INDEX_32I, HIPSPARSE_INDEX_BASE_ZERO, HIP_R_32F)); HIPSPARSE_CHECK(hipsparseCreateCsr(&matC, m, n, 0, dcsrRowPtrC, NULL, NULL, HIPSPARSE_INDEX_32I, HIPSPARSE_INDEX_32I, HIPSPARSE_INDEX_BASE_ZERO, HIP_R_32F)); hipsparseSpGEMMDescr_t spgemmDesc; HIPSPARSE_CHECK(hipsparseSpGEMM_createDescr(&spgemmDesc)); // Determine size of first user allocated buffer HIPSPARSE_CHECK(hipsparseSpGEMMreuse_workEstimation(handle, opA, opB, matA, matB, matC, HIPSPARSE_SPGEMM_DEFAULT, spgemmDesc, &bufferSize1, NULL)); HIP_CHECK(hipMalloc((void**)&dBuffer1, bufferSize1)); // Inspect the matrices A and B to determine the number of intermediate product in // C = alpha * A * B HIPSPARSE_CHECK(hipsparseSpGEMMreuse_workEstimation(handle, opA, opB, matA, matB, matC, HIPSPARSE_SPGEMM_DEFAULT, spgemmDesc, &bufferSize1, dBuffer1)); // Determine size of second, third, and fourth user allocated buffer HIPSPARSE_CHECK(hipsparseSpGEMMreuse_nnz(handle, opA, opB, matA, matB, matC, HIPSPARSE_SPGEMM_DEFAULT, spgemmDesc, &bufferSize2, NULL, &bufferSize3, NULL, &bufferSize4, NULL)); HIP_CHECK(hipMalloc((void**)&dBuffer2, bufferSize2)); HIP_CHECK(hipMalloc((void**)&dBuffer3, bufferSize3)); HIP_CHECK(hipMalloc((void**)&dBuffer4, bufferSize4)); // Compute sparsity pattern of C matrix and store in temporary buffers HIPSPARSE_CHECK(hipsparseSpGEMMreuse_nnz(handle, opA, opB, matA, matB, matC, HIPSPARSE_SPGEMM_DEFAULT, spgemmDesc, &bufferSize2, dBuffer2, &bufferSize3, dBuffer3, &bufferSize4, dBuffer4)); // We can now free buffer 1 and 2 HIP_CHECK(hipFree(dBuffer1)); HIP_CHECK(hipFree(dBuffer2)); // Get matrix C non-zero entries nnzC int64_t rowsC, colsC, nnzC; HIPSPARSE_CHECK(hipsparseSpMatGetSize(matC, &rowsC, &colsC, &nnzC)); // Allocate matrix C HIP_CHECK(hipMalloc((void**)&dcsrColIndC, sizeof(int) * nnzC)); HIP_CHECK(hipMalloc((void**)&dcsrValC, sizeof(float) * nnzC)); // Update matC with the new pointers. The C values array can be filled with data here // which is used if beta != 0. HIPSPARSE_CHECK(hipsparseCsrSetPointers(matC, dcsrRowPtrC, dcsrColIndC, dcsrValC)); // Determine size of fifth user allocated buffer HIPSPARSE_CHECK(hipsparseSpGEMMreuse_copy(handle, opA, opB, matA, matB, matC, HIPSPARSE_SPGEMM_DEFAULT, spgemmDesc, &bufferSize5, NULL)); HIP_CHECK(hipMalloc((void**)&dBuffer5, bufferSize5)); // Copy data from temporary buffers to the newly allocated C matrix HIPSPARSE_CHECK(hipsparseSpGEMMreuse_copy(handle, opA, opB, matA, matB, matC, HIPSPARSE_SPGEMM_DEFAULT, spgemmDesc, &bufferSize5, dBuffer5)); // We can now free buffer 3 HIP_CHECK(hipFree(dBuffer3)); // Compute C' = alpha * A * B + beta * C HIPSPARSE_CHECK(hipsparseSpGEMMreuse_compute(handle, opA, opB, &alpha, matA, matB, &beta, matC, computeType, HIPSPARSE_SPGEMM_DEFAULT, spgemmDesc)); // Copy results back to host if required std::vector<int> hcsrRowPtrC(m + 1); std::vector<int> hcsrColIndC(nnzC); std::vector<float> hcsrValC(nnzC); HIP_CHECK( hipMemcpy(hcsrRowPtrC.data(), dcsrRowPtrC, sizeof(int) * (m + 1), hipMemcpyDeviceToHost)); HIP_CHECK( hipMemcpy(hcsrColIndC.data(), dcsrColIndC, sizeof(int) * nnzC, hipMemcpyDeviceToHost)); HIP_CHECK(hipMemcpy(hcsrValC.data(), dcsrValC, sizeof(float) * nnzC, hipMemcpyDeviceToHost)); // Update dcsrValA, dcsrValB with new values for(size_t i = 0; i < hcsrValA.size(); i++) { hcsrValA[i] = 1.0f; } for(size_t i = 0; i < hcsrValB.size(); i++) { hcsrValB[i] = 2.0f; } HIP_CHECK(hipMemcpy(dcsrValA, hcsrValA.data(), sizeof(float) * nnzA, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrValB, hcsrValB.data(), sizeof(float) * nnzB, hipMemcpyHostToDevice)); // Compute C' = alpha * A * B + beta * C again with the new A and B values HIPSPARSE_CHECK(hipsparseSpGEMMreuse_compute(handle, opA, opB, &alpha, matA, matB, &beta, matC, computeType, HIPSPARSE_SPGEMM_DEFAULT, spgemmDesc)); // Copy results back to host if required HIP_CHECK( hipMemcpy(hcsrRowPtrC.data(), dcsrRowPtrC, sizeof(int) * (m + 1), hipMemcpyDeviceToHost)); HIP_CHECK( hipMemcpy(hcsrColIndC.data(), dcsrColIndC, sizeof(int) * nnzC, hipMemcpyDeviceToHost)); HIP_CHECK(hipMemcpy(hcsrValC.data(), dcsrValC, sizeof(float) * nnzC, hipMemcpyDeviceToHost)); // Destroy matrix descriptors and handles HIPSPARSE_CHECK(hipsparseSpGEMM_destroyDescr(spgemmDesc)); HIPSPARSE_CHECK(hipsparseDestroySpMat(matA)); HIPSPARSE_CHECK(hipsparseDestroySpMat(matB)); HIPSPARSE_CHECK(hipsparseDestroySpMat(matC)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); // Free device memory HIP_CHECK(hipFree(dBuffer4)); HIP_CHECK(hipFree(dBuffer5)); HIP_CHECK(hipFree(dcsrRowPtrA)); HIP_CHECK(hipFree(dcsrColIndA)); HIP_CHECK(hipFree(dcsrValA)); HIP_CHECK(hipFree(dcsrRowPtrB)); HIP_CHECK(hipFree(dcsrColIndB)); HIP_CHECK(hipFree(dcsrValB)); HIP_CHECK(hipFree(dcsrRowPtrC)); HIP_CHECK(hipFree(dcsrColIndC)); HIP_CHECK(hipFree(dcsrValC)); return 0; }


- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**opA**–**[in]**sparse matrix \(A\) operation type.**opB**–**[in]**sparse matrix \(B\) operation type.**alpha**–**[in]**scalar \(\alpha\).**matA**–**[in]**sparse matrix \(A\) descriptor.**matB**–**[in]**sparse matrix \(B\) descriptor.**beta**–**[in]**scalar \(\beta\).**matC**–**[out]**sparse matrix \(C\) descriptor.**computeType**–**[in]**floating point precision for the SpGEMM computation.**alg**–**[in]**SpGEMM algorithm for the SpGEMM computation.**spgemmDescr**–**[in]**SpGEMM descriptor.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`alpha`

,`beta`

,`matA`

,`matB`

, or`matC`

pointer is invalid.**HIPSPARSE_STATUS_ALLOC_FAILED**– additional buffer for long rows could not be allocated.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`opA`

!=[HIPSPARSE_OPERATION_NON_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141a270f0124eb0d0ac15c3e7afb18064547)or`opB`

!=[HIPSPARSE_OPERATION_NON_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141a270f0124eb0d0ac15c3e7afb18064547).



## hipsparseSDDMM_bufferSize()[#](#hipsparsesddmm-buffersize)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSDDMM_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opB, const void *alpha, hipsparseConstDnMatDescr_t A, hipsparseConstDnMatDescr_t B, const void *beta,[hipsparseSpMatDescr_t](types.html#_CPPv421hipsparseSpMatDescr_t)C, hipDataType computeType,[hipsparseSDDMMAlg_t](types.html#_CPPv419hipsparseSDDMMAlg_t)alg, size_t *pBufferSizeInBytes)[#](#_CPPv425hipsparseSDDMM_bufferSize17hipsparseHandle_t20hipsparseOperation_t20hipsparseOperation_tPKv26hipsparseConstDnMatDescr_t26hipsparseConstDnMatDescr_tPKv21hipsparseSpMatDescr_t11hipDataType19hipsparseSDDMMAlg_tP6size_t) `hipsparseSDDMM_bufferSize`

returns the size of the required buffer needed when computing the sampled dense-dense matrix multiplication:\[ C := \alpha (op(A) \cdot op(B)) \circ spy(C) + \beta \cdot C, \]where \(C\) is a sparse matrix and \(A\) and \(B\) are dense matrices. This routine is used in conjunction with[hipsparseSDDMM_preprocess()](#hipsparse__sddmm_8h_1ab3d6dc15bb7cef9ec1acd8c1102b592a)and[hipsparseSDDMM()](#hipsparse__sddmm_8h_1a71bc507b97a44981c31ca97f5cf559bc).`hipsparseSDDMM_bufferSize`

supports multiple combinations of data types and compute types. See[hipsparseSDDMM](#hipsparse__sddmm_8h_1a71bc507b97a44981c31ca97f5cf559bc)for a complete listing of all the data type and compute type combinations available.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**opA**–**[in]**dense matrix \(A\) operation type.**opB**–**[in]**dense matrix \(B\) operation type.**alpha**–**[in]**scalar \(\alpha\).**A**–**[in]**dense matrix \(A\) descriptor.**B**–**[in]**dense matrix \(B\) descriptor.**beta**–**[in]**scalar \(\beta\).**C**–**[inout]**sparse matrix \(C\) descriptor.**computeType**–**[in]**floating point precision for the SDDMM computation.**alg**–**[in]**specification of the algorithm to use.**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`alpha`

,`beta`

,`A`

,`B`

,`D`

,`C`

or`pBufferSizeInBytes`

pointer is invalid or the value of`opA`

or`opB`

is incorrect**HIPSPARSE_STATUS_NOT_SUPPORTED**–`opA`

==[HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141ac55e75ba3027186f1dc6164fdcb06f0e)or`opB`

==[HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141ac55e75ba3027186f1dc6164fdcb06f0e).



## hipsparseSDDMM_preprocess()[#](#hipsparsesddmm-preprocess)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSDDMM_preprocess([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opB, const void *alpha, hipsparseConstDnMatDescr_t A, hipsparseConstDnMatDescr_t B, const void *beta,[hipsparseSpMatDescr_t](types.html#_CPPv421hipsparseSpMatDescr_t)C, hipDataType computeType,[hipsparseSDDMMAlg_t](types.html#_CPPv419hipsparseSDDMMAlg_t)alg, void *tempBuffer)[#](#_CPPv425hipsparseSDDMM_preprocess17hipsparseHandle_t20hipsparseOperation_t20hipsparseOperation_tPKv26hipsparseConstDnMatDescr_t26hipsparseConstDnMatDescr_tPKv21hipsparseSpMatDescr_t11hipDataType19hipsparseSDDMMAlg_tPv) `hipsparseSDDMM_preprocess`

performs the required preprocessing used when computing the sampled dense dense matrix multiplication:\[ C := \alpha (op(A) \cdot op(B)) \circ spy(C) + \beta \cdot C, \]where \(C\) is a sparse matrix and \(A\) and \(B\) are dense matrices. This routine is used in conjunction with[hipsparseSDDMM()](#hipsparse__sddmm_8h_1a71bc507b97a44981c31ca97f5cf559bc).`hipsparseSDDMM_preprocess`

supports multiple combinations of data types and compute types. See[hipsparseSDDMM](#hipsparse__sddmm_8h_1a71bc507b97a44981c31ca97f5cf559bc)for a complete listing of all the data type and compute type combinations available.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**opA**–**[in]**dense matrix \(A\) operation type.**opB**–**[in]**dense matrix \(B\) operation type.**alpha**–**[in]**scalar \(\alpha\).**A**–**[in]**dense matrix \(A\) descriptor.**B**–**[in]**dense matrix \(B\) descriptor.**beta**–**[in]**scalar \(\beta\).**C**–**[inout]**sparse matrix \(C\) descriptor.**computeType**–**[in]**floating point precision for the SDDMM computation.**alg**–**[in]**specification of the algorithm to use.**tempBuffer**–**[in]**temporary storage buffer allocated by the user. The size must be greater or equal to the size obtained with[hipsparseSDDMM_bufferSize](#hipsparse__sddmm_8h_1a8bbef07065620267a7e64cccc8398cd4).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`alpha`

,`beta`

,`A`

,`B`

,`C`

or`tempBuffer`

pointer is invalid or the value of`opA`

or`opB`

is incorrect.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`opA`

==[HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141ac55e75ba3027186f1dc6164fdcb06f0e)or`opB`

==[HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141ac55e75ba3027186f1dc6164fdcb06f0e).



## hipsparseSDDMM()[#](#hipsparsesddmm)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSDDMM([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opB, const void *alpha, hipsparseConstDnMatDescr_t A, hipsparseConstDnMatDescr_t B, const void *beta,[hipsparseSpMatDescr_t](types.html#_CPPv421hipsparseSpMatDescr_t)C, hipDataType computeType,[hipsparseSDDMMAlg_t](types.html#_CPPv419hipsparseSDDMMAlg_t)alg, void *tempBuffer)[#](#_CPPv414hipsparseSDDMM17hipsparseHandle_t20hipsparseOperation_t20hipsparseOperation_tPKv26hipsparseConstDnMatDescr_t26hipsparseConstDnMatDescr_tPKv21hipsparseSpMatDescr_t11hipDataType19hipsparseSDDMMAlg_tPv) Sampled Dense-Dense Matrix Multiplication.

`hipsparseSDDMM`

multiplies the scalar \(\alpha\) with the dense \(m \times k\) matrix \(op(A)\), the dense \(k \times n\) matrix \(op(B)\), filtered by the sparsity pattern of the \(m \times n\) sparse matrix \(C\) and adds the result to \(C\) scaled by \(\beta\). The final result is stored in the sparse \(m \times n\) matrix \(C\), such that\[ C := \alpha ( op(A) \cdot op(B) ) \circ spy(C) + \beta C, \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if op(A) == HIPSPARSE_OPERATION_NON_TRANSPOSE} \\ A^T, & \text{if op(A) == HIPSPARSE_OPERATION_TRANSPOSE} \\ \end{array} \right. \end{split}\],\[\begin{split} op(B) = \left\{ \begin{array}{ll} B, & \text{if op(B) == HIPSPARSE_OPERATION_NON_TRANSPOSE} \\ B^T, & \text{if op(B) == HIPSPARSE_OPERATION_TRANSPOSE} \\ \end{array} \right. \end{split}\]and\[\begin{split} spy(C)_{ij} = \left\{ \begin{array}{ll} 1, & \text{ if C_{ij} != 0} \\ 0, & \text{ otherwise} \\ \end{array} \right. \end{split}\]Computing the above sampled dense-dense multiplication requires three steps to complete. First, the user calls

[hipsparseSDDMM_bufferSize](#hipsparse__sddmm_8h_1a8bbef07065620267a7e64cccc8398cd4)to determine the size of the required temporary storage buffer. Next, the user allocates this buffer and calls[hipsparseSDDMM_preprocess](#hipsparse__sddmm_8h_1ab3d6dc15bb7cef9ec1acd8c1102b592a)which performs any analysis of the input matrices that may be required. Finally, the user calls`hipsparseSDDMM`

to complete the computation. Once all calls to`hipsparseSDDMM`

are complete, the temporary buffer can be deallocated.`hipsparseSDDMM`

supports different algorithms which can provide better performance for different matrices.CSR/CSC Algorithms

HIPSPARSE_SDDMM_ALG_DEFAULT

Currently,

`hipsparseSDDMM`

only supports the uniform precisions indicated in the table below. For the sparse matrix \(C\),`hipsparseSDDMM`

supports the index types[HIPSPARSE_INDEX_32I](types.html#hipsparse-generic-types_8h_1aaeacc98278238b4555b312b38a8ca3a1a39d66b98a770ce4f130cf175614bf1ee)and[HIPSPARSE_INDEX_64I](types.html#hipsparse-generic-types_8h_1aaeacc98278238b4555b312b38a8ca3a1aaf693262ac42a636addc9be11c1f534b).**Uniform Precisions:**A / B / C / compute_type

HIP_R_16F

HIP_R_32F

HIP_R_64F

HIP_C_32F

HIP_C_64F

**Mixed precisions:**A / B

C

compute_type

HIP_R_16F

HIP_R_32F

HIP_R_32F

HIP_R_16F

HIP_R_16F

HIP_R_32F

**Example**This example performs sampled dense-dense matrix product, \(C := \alpha ( A \cdot B ) \circ spy(C) + \beta C\) where \(\circ\) is the hadamard product

int main(int argc, char* argv[]) { // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); __half halpha = 1.0; __half hbeta = 0.0; // A, B, and C are mxk, kxn, and mxn int m = 4; int k = 3; int n = 2; int nnzC = 5; // 2 3 -1 // A = 0 2 1 // 0 0 5 // 0 -2 0.5 // 0 4 // B = 1 0 // -2 0.5 // 1 0 1 0 // C = 2 3 spy(C) = 1 1 // 0 0 0 0 // 4 5 1 1 std::vector<__half> hA = {2.0, 3.0, -1.0, 0.0, 2.0, 1.0, 0.0, 0.0, 5.0, 0.0, -2.0, 0.5}; std::vector<__half> hB = {0.0, 4.0, 1.0, 0.0, -2.0, 0.5}; std::vector<int> hcsr_row_ptrC = {0, 1, 3, 3, 5}; std::vector<int> hcsr_col_indC = {0, 0, 1, 0, 1}; std::vector<__half> hcsr_valC = {1.0, 2.0, 3.0, 4.0, 5.0}; __half* dA = nullptr; __half* dB = nullptr; HIP_CHECK(hipMalloc((void**)&dA, sizeof(__half) * m * k)); HIP_CHECK(hipMalloc((void**)&dB, sizeof(__half) * k * n)); int* dcsr_row_ptrC = nullptr; int* dcsr_col_indC = nullptr; __half* dcsr_valC = nullptr; HIP_CHECK(hipMalloc((void**)&dcsr_row_ptrC, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&dcsr_col_indC, sizeof(int) * nnzC)); HIP_CHECK(hipMalloc((void**)&dcsr_valC, sizeof(__half) * nnzC)); HIP_CHECK(hipMemcpy(dA, hA.data(), sizeof(__half) * m * k, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dB, hB.data(), sizeof(__half) * k * n, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy( dcsr_row_ptrC, hcsr_row_ptrC.data(), sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsr_col_indC, hcsr_col_indC.data(), sizeof(int) * nnzC, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsr_valC, hcsr_valC.data(), sizeof(__half) * nnzC, hipMemcpyHostToDevice)); hipsparseDnMatDescr_t matA; HIPSPARSE_CHECK(hipsparseCreateDnMat(&matA, m, k, k, dA, HIP_R_16F, HIPSPARSE_ORDER_ROW)); hipsparseDnMatDescr_t matB; HIPSPARSE_CHECK(hipsparseCreateDnMat(&matB, k, n, n, dB, HIP_R_16F, HIPSPARSE_ORDER_ROW)); hipsparseSpMatDescr_t matC; HIPSPARSE_CHECK(hipsparseCreateCsr(&matC, m, n, nnzC, dcsr_row_ptrC, dcsr_col_indC, dcsr_valC, HIPSPARSE_INDEX_32I, HIPSPARSE_INDEX_32I, HIPSPARSE_INDEX_BASE_ZERO, HIP_R_16F)); size_t buffer_size = 0; HIPSPARSE_CHECK(hipsparseSDDMM_bufferSize(handle, HIPSPARSE_OPERATION_NON_TRANSPOSE, HIPSPARSE_OPERATION_NON_TRANSPOSE, &halpha, matA, matB, &hbeta, matC, HIP_R_16F, HIPSPARSE_SDDMM_ALG_DEFAULT, &buffer_size)); void* dbuffer = nullptr; HIP_CHECK(hipMalloc((void**)&dbuffer, buffer_size)); HIPSPARSE_CHECK(hipsparseSDDMM_preprocess(handle, HIPSPARSE_OPERATION_NON_TRANSPOSE, HIPSPARSE_OPERATION_NON_TRANSPOSE, &halpha, matA, matB, &hbeta, matC, HIP_R_16F, HIPSPARSE_SDDMM_ALG_DEFAULT, dbuffer)); HIPSPARSE_CHECK(hipsparseSDDMM(handle, HIPSPARSE_OPERATION_NON_TRANSPOSE, HIPSPARSE_OPERATION_NON_TRANSPOSE, &halpha, matA, matB, &hbeta, matC, HIP_R_16F, HIPSPARSE_SDDMM_ALG_DEFAULT, dbuffer)); HIP_CHECK(hipMemcpy( hcsr_row_ptrC.data(), dcsr_row_ptrC, sizeof(int) * (m + 1), hipMemcpyDeviceToHost)); HIP_CHECK( hipMemcpy(hcsr_col_indC.data(), dcsr_col_indC, sizeof(int) * nnzC, hipMemcpyDeviceToHost)); HIP_CHECK(hipMemcpy(hcsr_valC.data(), dcsr_valC, sizeof(__half) * nnzC, hipMemcpyDeviceToHost)); std::cout << "C" << std::endl; for(int i = 0; i < m; i++) { int start = hcsr_row_ptrC[i]; int end = hcsr_row_ptrC[i + 1]; std::vector<__half> temp(n, 0.0); for(int j = start; j < end; j++) { temp[hcsr_col_indC[j]] = hcsr_valC[j]; } for(int j = 0; j < n; j++) { std::cout << temp[j] << " "; } std::cout << "" << std::endl; } std::cout << "" << std::endl; HIPSPARSE_CHECK(hipsparseDestroyMatDescr(matA)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(matB)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(matC)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); HIP_CHECK(hipFree(dA)); HIP_CHECK(hipFree(dB)); HIP_CHECK(hipFree(dcsr_row_ptrC)); HIP_CHECK(hipFree(dcsr_col_indC)); HIP_CHECK(hipFree(dcsr_valC)); HIP_CHECK(hipFree(dbuffer)); return 0; }


- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**opA**–**[in]**dense matrix \(A\) operation type.**opB**–**[in]**dense matrix \(B\) operation type.**alpha**–**[in]**scalar \(\alpha\).**A**–**[in]**dense matrix \(A\) descriptor.**B**–**[in]**dense matrix \(B\) descriptor.**beta**–**[in]**scalar \(\beta\).**C**–**[inout]**sparse matrix \(C\) descriptor.**computeType**–**[in]**floating point precision for the SDDMM computation.**alg**–**[in]**specification of the algorithm to use.**tempBuffer**–**[in]**temporary storage buffer allocated by the user. The size must be greater or equal to the size obtained with[hipsparseSDDMM_bufferSize](#hipsparse__sddmm_8h_1a8bbef07065620267a7e64cccc8398cd4).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`alpha`

,`beta`

,`A`

,`B`

,`C`

or`tempBuffer`

pointer is invalid or the value of`opA`

or`opB`

is incorrect.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`opA`

==[HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141ac55e75ba3027186f1dc6164fdcb06f0e)or`opB`

==[HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE](types.html#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141ac55e75ba3027186f1dc6164fdcb06f0e).



## hipsparseSpSV_createDescr()[#](#hipsparsespsv-createdescr)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpSV_createDescr([hipsparseSpSVDescr_t](types.html#_CPPv420hipsparseSpSVDescr_t)*descr)[#](#_CPPv425hipsparseSpSV_createDescrP20hipsparseSpSVDescr_t) `hipsparseSpSV_createDescr`

creates a sparse matrix triangular solve descriptor. It should be destroyed at the end using[hipsparseSpSV_destroyDescr()](#hipsparse__spsv_8h_1a1cec939dbc1a55370694da3f718f7dde).

## hipsparseSpSV_destroyDescr()[#](#hipsparsespsv-destroydescr)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpSV_destroyDescr([hipsparseSpSVDescr_t](types.html#_CPPv420hipsparseSpSVDescr_t)descr)[#](#_CPPv426hipsparseSpSV_destroyDescr20hipsparseSpSVDescr_t) `hipsparseSpSV_destroyDescr`

destroys a sparse matrix triangular solve descriptor and releases all resources used by the descriptor.

## hipsparseSpSV_bufferSize()[#](#hipsparsespsv-buffersize)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpSV_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opA, const void *alpha, hipsparseConstSpMatDescr_t matA, hipsparseConstDnVecDescr_t x, const[hipsparseDnVecDescr_t](types.html#_CPPv421hipsparseDnVecDescr_t)y, hipDataType computeType,[hipsparseSpSVAlg_t](types.html#_CPPv418hipsparseSpSVAlg_t)alg,[hipsparseSpSVDescr_t](types.html#_CPPv420hipsparseSpSVDescr_t)spsvDescr, size_t *pBufferSizeInBytes)[#](#_CPPv424hipsparseSpSV_bufferSize17hipsparseHandle_t20hipsparseOperation_tPKv26hipsparseConstSpMatDescr_t26hipsparseConstDnVecDescr_tK21hipsparseDnVecDescr_t11hipDataType18hipsparseSpSVAlg_t20hipsparseSpSVDescr_tP6size_t) `hipsparseSpSV_bufferSize`

computes the size of the required user allocated buffer needed when solving the triangular linear system:\[ op(A) \cdot y := \alpha \cdot x, \]where \(op(A)\) is a sparse matrix in CSR or COO storage format, \(x\) and \(y\) are dense vectors.`hipsparseSpSV_bufferSize`

supports multiple combinations of data types and compute types. See[hipsparseSpSV_solve](#hipsparse__spsv_8h_1a120f5f65677a69730ae7630b7027ee6c)for a complete listing of all the data type and compute type combinations available.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**opA**–**[in]**matrix operation type.**alpha**–**[in]**scalar \(\alpha\).**matA**–**[in]**matrix descriptor.**x**–**[in]**vector descriptor.**y**–**[inout]**vector descriptor.**computeType**–**[in]**floating point precision for the SpSV computation.**alg**–**[in]**SpSV algorithm for the SpSV computation.**spsvDescr**–**[in]**SpSV descriptor.**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`alpha`

,`matA`

,`x`

,`y`

,`spsvDescr`

or`pBufferSizeInBytes`

pointer is invalid.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`opA`

,`computeType`

or`alg`

is currently not supported.



## hipsparseSpSV_analysis()[#](#hipsparsespsv-analysis)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpSV_analysis([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opA, const void *alpha, hipsparseConstSpMatDescr_t matA, hipsparseConstDnVecDescr_t x, const[hipsparseDnVecDescr_t](types.html#_CPPv421hipsparseDnVecDescr_t)y, hipDataType computeType,[hipsparseSpSVAlg_t](types.html#_CPPv418hipsparseSpSVAlg_t)alg,[hipsparseSpSVDescr_t](types.html#_CPPv420hipsparseSpSVDescr_t)spsvDescr, void *externalBuffer)[#](#_CPPv422hipsparseSpSV_analysis17hipsparseHandle_t20hipsparseOperation_tPKv26hipsparseConstSpMatDescr_t26hipsparseConstDnVecDescr_tK21hipsparseDnVecDescr_t11hipDataType18hipsparseSpSVAlg_t20hipsparseSpSVDescr_tPv) `hipsparseSpSV_analysis`

performs the required analysis needed when solving the triangular linear system:\[ op(A) \cdot y := \alpha \cdot x, \]where \(op(A)\) is a sparse matrix in CSR or COO storage format, \(x\) and \(y\) are dense vectors.`hipsparseSpSV_analysis`

supports multiple combinations of data types and compute types. See[hipsparseSpSV_solve](#hipsparse__spsv_8h_1a120f5f65677a69730ae7630b7027ee6c)for a complete listing of all the data type and compute type combinations available.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**opA**–**[in]**matrix operation type.**alpha**–**[in]**scalar \(\alpha\).**matA**–**[in]**matrix descriptor.**x**–**[in]**vector descriptor.**y**–**[inout]**vector descriptor.**computeType**–**[in]**floating point precision for the SpSV computation.**alg**–**[in]**SpSV algorithm for the SpSV computation.**spsvDescr**–**[in]**SpSV descriptor.**externalBuffer**–**[out]**temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`alpha`

,`matA`

,`x`

,`y`

,`spsvDescr`

or`externalBuffer`

pointer is invalid.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`opA`

,`computeType`

or`alg`

is currently not supported.



## hipsparseSpSV_solve()[#](#hipsparsespsv-solve)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpSV_solve([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opA, const void *alpha, hipsparseConstSpMatDescr_t matA, hipsparseConstDnVecDescr_t x, const[hipsparseDnVecDescr_t](types.html#_CPPv421hipsparseDnVecDescr_t)y, hipDataType computeType,[hipsparseSpSVAlg_t](types.html#_CPPv418hipsparseSpSVAlg_t)alg,[hipsparseSpSVDescr_t](types.html#_CPPv420hipsparseSpSVDescr_t)spsvDescr)[#](#_CPPv419hipsparseSpSV_solve17hipsparseHandle_t20hipsparseOperation_tPKv26hipsparseConstSpMatDescr_t26hipsparseConstDnVecDescr_tK21hipsparseDnVecDescr_t11hipDataType18hipsparseSpSVAlg_t20hipsparseSpSVDescr_t) Sparse triangular solve.

`hipsparseSpSV_solve`

solves a triangular linear system of equations defined by a sparse \(m \times m\) square matrix \(op(A)\), given in CSR or COO storage format, such that\[ op(A) \cdot y = \alpha \cdot x, \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if trans == HIPSPARSE_OPERATION_NON_TRANSPOSE} \\ A^T, & \text{if trans == HIPSPARSE_OPERATION_TRANSPOSE} \end{array} \right. \end{split}\]and where \(y\) is the dense solution vector and \(x\) is the dense right-hand side vector.Performing the above operation requires three steps. First,

[hipsparseSpSV_bufferSize](#hipsparse__spsv_8h_1a6a47526261741c624acb9511cb70e669)must be called which will determine the size of the required temporary storage buffer. The user then allocates this buffer and calls[hipsparseSpSV_analysis](#hipsparse__spsv_8h_1a22c011e445b2a217ab47ff1f7e84f25d)which will perform analysis on the sparse matrix \(op(A)\). Finally, the user completes the computation by calling`hipsparseSpSV_solve`

. The buffer size and preprecess routines only need to be called once for a given sparse matrix \(op(A)\) while the computation can be repeatedly used with different \(x\) and \(y\) vectors. Once all calls to`hipsparseSpSV_solve`

are complete, the temporary buffer can be deallocated.`hipsparseSpSV_solve`

supports[HIPSPARSE_INDEX_32I](types.html#hipsparse-generic-types_8h_1aaeacc98278238b4555b312b38a8ca3a1a39d66b98a770ce4f130cf175614bf1ee)and[HIPSPARSE_INDEX_64I](types.html#hipsparse-generic-types_8h_1aaeacc98278238b4555b312b38a8ca3a1aaf693262ac42a636addc9be11c1f534b)index types for storing the row pointer and column indices arrays of the sparse matrices.`hipsparseSpSV_solve`

supports the following data types for \(op(A)\), \(x\), \(y\) and compute types for \(\alpha\):**Uniform Precisions:**A / X / Y / compute_type

HIP_R_32F

HIP_R_64F

HIP_C_32F

HIP_C_64F

**Example**int main(int argc, char* argv[]) { // 1 0 0 0 // A = 4 2 0 0 // 0 3 7 0 // 0 0 0 1 int m = 4; std::vector<int> hcsr_row_ptr = {0, 1, 3, 5, 6}; std::vector<int> hcsr_col_ind = {0, 0, 1, 1, 2, 3}; std::vector<float> hcsr_val = {1, 4, 2, 3, 7, 1}; std::vector<float> hx(m, 1.0f); std::vector<float> hy(m, 0.0f); // Scalar alpha float alpha = 1.0f; int nnz = hcsr_row_ptr[m] - hcsr_row_ptr[0]; // Offload data to device int* dcsr_row_ptr; int* dcsr_col_ind; float* dcsr_val; float* dx; float* dy; HIP_CHECK(hipMalloc((void**)&dcsr_row_ptr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&dcsr_col_ind, sizeof(int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcsr_val, sizeof(float) * nnz)); HIP_CHECK(hipMalloc((void**)&dx, sizeof(float) * m)); HIP_CHECK(hipMalloc((void**)&dy, sizeof(float) * m)); HIP_CHECK( hipMemcpy(dcsr_row_ptr, hcsr_row_ptr.data(), sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsr_col_ind, hcsr_col_ind.data(), sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsr_val, hcsr_val.data(), sizeof(float) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dx, hx.data(), sizeof(float) * m, hipMemcpyHostToDevice)); hipsparseHandle_t handle; hipsparseSpMatDescr_t matA; hipsparseDnVecDescr_t vecX; hipsparseDnVecDescr_t vecY; hipsparseIndexType_t row_idx_type = HIPSPARSE_INDEX_32I; hipsparseIndexType_t col_idx_type = HIPSPARSE_INDEX_32I; hipDataType data_type = HIP_R_32F; hipDataType computeType = HIP_R_32F; hipsparseIndexBase_t idx_base = HIPSPARSE_INDEX_BASE_ZERO; hipsparseOperation_t trans = HIPSPARSE_OPERATION_NON_TRANSPOSE; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // Create sparse matrix A HIPSPARSE_CHECK(hipsparseCreateCsr(&matA, m, m, nnz, dcsr_row_ptr, dcsr_col_ind, dcsr_val, row_idx_type, col_idx_type, idx_base, data_type)); // Create dense vector X HIPSPARSE_CHECK(hipsparseCreateDnVec(&vecX, m, dx, data_type)); // Create dense vector Y HIPSPARSE_CHECK(hipsparseCreateDnVec(&vecY, m, dy, data_type)); hipsparseSpSVDescr_t descr; HIPSPARSE_CHECK(hipsparseSpSV_createDescr(&descr)); // Call spsv to get buffer size size_t buffer_size; HIPSPARSE_CHECK(hipsparseSpSV_bufferSize(handle, trans, &alpha, matA, vecX, vecY, computeType, HIPSPARSE_SPSV_ALG_DEFAULT, descr, &buffer_size)); void* temp_buffer; HIP_CHECK(hipMalloc((void**)&temp_buffer, buffer_size)); // Call spsv to perform analysis HIPSPARSE_CHECK(hipsparseSpSV_analysis(handle, trans, &alpha, matA, vecX, vecY, computeType, HIPSPARSE_SPSV_ALG_DEFAULT, descr, temp_buffer)); // Call spsv to perform computation HIPSPARSE_CHECK(hipsparseSpSV_solve( handle, trans, &alpha, matA, vecX, vecY, computeType, HIPSPARSE_SPSV_ALG_DEFAULT, descr)); // Copy result back to host HIP_CHECK(hipMemcpy(hy.data(), dy, sizeof(float) * m, hipMemcpyDeviceToHost)); // Clear hipSPARSE HIPSPARSE_CHECK(hipsparseSpSV_destroyDescr(descr)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(matA)); HIPSPARSE_CHECK(hipsparseDestroyDnVec(vecX)); HIPSPARSE_CHECK(hipsparseDestroyDnVec(vecY)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); // Clear device memory HIP_CHECK(hipFree(dcsr_row_ptr)); HIP_CHECK(hipFree(dcsr_col_ind)); HIP_CHECK(hipFree(dcsr_val)); HIP_CHECK(hipFree(dx)); HIP_CHECK(hipFree(dy)); HIP_CHECK(hipFree(temp_buffer)); return 0; }


- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**opA**–**[in]**matrix operation type.**alpha**–**[in]**scalar \(\alpha\).**matA**–**[in]**matrix descriptor.**x**–**[in]**vector descriptor.**y**–**[inout]**vector descriptor.**computeType**–**[in]**floating point precision for the SpSV computation.**alg**–**[in]**SpSV algorithm for the SpSV computation.**spsvDescr**–**[in]**SpSV descriptor.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`alpha`

,`matA`

,`x`

,`y`

, or`spsvDescr`

pointer is invalid.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`opA`

,`computeType`

or`alg`

is currently not supported.



## hipsparseSpSM_createDescr()[#](#hipsparsespsm-createdescr)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpSM_createDescr([hipsparseSpSMDescr_t](types.html#_CPPv420hipsparseSpSMDescr_t)*descr)[#](#_CPPv425hipsparseSpSM_createDescrP20hipsparseSpSMDescr_t) `hipsparseSpSM_createDescr`

creates a sparse matrix triangular solve with multiple rhs descriptor. It should be destroyed at the end using[hipsparseSpSM_destroyDescr()](#hipsparse__spsm_8h_1aa52c5c27bf7a6451282da2c26a32aae4).

## hipsparseSpSM_destroyDescr()[#](#hipsparsespsm-destroydescr)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpSM_destroyDescr([hipsparseSpSMDescr_t](types.html#_CPPv420hipsparseSpSMDescr_t)descr)[#](#_CPPv426hipsparseSpSM_destroyDescr20hipsparseSpSMDescr_t) `hipsparseSpSM_destroyDescr`

destroys a sparse matrix triangular solve with multiple rhs descriptor and releases all resources used by the descriptor.

## hipsparseSpSM_bufferSize()[#](#hipsparsespsm-buffersize)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpSM_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opB, const void *alpha, hipsparseConstSpMatDescr_t matA, hipsparseConstDnMatDescr_t matB, const[hipsparseDnMatDescr_t](types.html#_CPPv421hipsparseDnMatDescr_t)matC, hipDataType computeType,[hipsparseSpSMAlg_t](types.html#_CPPv418hipsparseSpSMAlg_t)alg,[hipsparseSpSMDescr_t](types.html#_CPPv420hipsparseSpSMDescr_t)spsmDescr, size_t *pBufferSizeInBytes)[#](#_CPPv424hipsparseSpSM_bufferSize17hipsparseHandle_t20hipsparseOperation_t20hipsparseOperation_tPKv26hipsparseConstSpMatDescr_t26hipsparseConstDnMatDescr_tK21hipsparseDnMatDescr_t11hipDataType18hipsparseSpSMAlg_t20hipsparseSpSMDescr_tP6size_t) `hipsparseSpSM_bufferSize`

computes the size of the required user allocated buffer needed when solving the triangular linear system:\[ op(A) \cdot C := \alpha \cdot op(B), \]where \(op(A)\) is a square sparse matrix in CSR or COO storage format, \(B\) and \(C\) are dense matrices.`hipsparseSpSM_bufferSize`

supports multiple combinations of data types and compute types. See[hipsparseSpSM_solve](#hipsparse__spsm_8h_1a1396f9876800f44cf5fca0c2efc524c0)for a complete listing of all the data type and compute type combinations available.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**opA**–**[in]**matrix operation type for the sparse matrix \(A\).**opB**–**[in]**matrix operation type for the dense matrix \(B\).**alpha**–**[in]**scalar \(\alpha\).**matA**–**[in]**sparse matrix descriptor.**matB**–**[in]**dense matrix descriptor.**matC**–**[inout]**dense matrix descriptor.**computeType**–**[in]**floating point precision for the SpSM computation.**alg**–**[in]**SpSM algorithm for the SpSM computation.**spsmDescr**–**[in]**SpSM descriptor.**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`alpha`

,`matA`

,`matB`

,`matC`

,`spsmDescr`

or`pBufferSizeInBytes`

pointer is invalid.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`opA`

,`opB`

,`computeType`

or`alg`

is currently not supported.



## hipsparseSpSM_analysis()[#](#hipsparsespsm-analysis)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpSM_analysis([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opB, const void *alpha, hipsparseConstSpMatDescr_t matA, hipsparseConstDnMatDescr_t matB, const[hipsparseDnMatDescr_t](types.html#_CPPv421hipsparseDnMatDescr_t)matC, hipDataType computeType,[hipsparseSpSMAlg_t](types.html#_CPPv418hipsparseSpSMAlg_t)alg,[hipsparseSpSMDescr_t](types.html#_CPPv420hipsparseSpSMDescr_t)spsmDescr, void *externalBuffer)[#](#_CPPv422hipsparseSpSM_analysis17hipsparseHandle_t20hipsparseOperation_t20hipsparseOperation_tPKv26hipsparseConstSpMatDescr_t26hipsparseConstDnMatDescr_tK21hipsparseDnMatDescr_t11hipDataType18hipsparseSpSMAlg_t20hipsparseSpSMDescr_tPv) `hipsparseSpSM_analysis`

performs the required analysis needed when solving the triangular linear system:\[ op(A) \cdot C := \alpha \cdot op(B), \]where \(A\) is a sparse matrix in CSR or COO storage format, \(B\) and \(C\) are dense vectors.`hipsparseSpSM_bufferSize`

supports multiple combinations of data types and compute types. See[hipsparseSpSM_solve](#hipsparse__spsm_8h_1a1396f9876800f44cf5fca0c2efc524c0)for a complete listing of all the data type and compute type combinations available.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**opA**–**[in]**matrix operation type for the sparse matrix \(A\).**opB**–**[in]**matrix operation type for the dense matrix \(B\).**alpha**–**[in]**scalar \(\alpha\).**matA**–**[in]**sparse matrix descriptor.**matB**–**[in]**dense matrix descriptor.**matC**–**[inout]**dense matrix descriptor.**computeType**–**[in]**floating point precision for the SpSM computation.**alg**–**[in]**SpSM algorithm for the SpSM computation.**spsmDescr**–**[in]**SpSM descriptor.**externalBuffer**–**[out]**temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`alpha`

,`matA`

,`matB`

,`matC`

,`spsmDescr`

or`externalBuffer`

pointer is invalid.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`opA`

,`opB`

,`computeType`

or`alg`

is currently not supported.



## hipsparseSpSM_solve()[#](#hipsparsespsm-solve)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpSM_solve([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opA,[hipsparseOperation_t](types.html#_CPPv420hipsparseOperation_t)opB, const void *alpha, hipsparseConstSpMatDescr_t matA, hipsparseConstDnMatDescr_t matB, const[hipsparseDnMatDescr_t](types.html#_CPPv421hipsparseDnMatDescr_t)matC, hipDataType computeType,[hipsparseSpSMAlg_t](types.html#_CPPv418hipsparseSpSMAlg_t)alg,[hipsparseSpSMDescr_t](types.html#_CPPv420hipsparseSpSMDescr_t)spsmDescr, void *externalBuffer)[#](#_CPPv419hipsparseSpSM_solve17hipsparseHandle_t20hipsparseOperation_t20hipsparseOperation_tPKv26hipsparseConstSpMatDescr_t26hipsparseConstDnMatDescr_tK21hipsparseDnMatDescr_t11hipDataType18hipsparseSpSMAlg_t20hipsparseSpSMDescr_tPv) Sparse triangular system solve.

`hipsparseSpSM_solve`

solves a triangular linear system of equations defined by a sparse \(m \times m\) square matrix \(op(A)\), given in CSR or COO storage format, such that\[ op(A) \cdot C = \alpha \cdot op(B), \]with\[\begin{split} op(A) = \left\{ \begin{array}{ll} A, & \text{if opA == HIPSPARSE_OPERATION_NON_TRANSPOSE} \\ A^T, & \text{if opB == HIPSPARSE_OPERATION_TRANSPOSE} \end{array} \right. \end{split}\]and\[\begin{split} op(B) = \left\{ \begin{array}{ll} B, & \text{if opA == HIPSPARSE_OPERATION_NON_TRANSPOSE} \\ B^T, & \text{if opB == HIPSPARSE_OPERATION_TRANSPOSE} \end{array} \right. \end{split}\]and where \(C\) is the dense solution matrix and \(B\) is the dense right-hand side matrix. Both \(B\) and \(C\) can be in row or column order.Performing the above operation requires three steps. First, the user calls

[hipsparseSpSM_bufferSize](#hipsparse__spsm_8h_1a162f0d8273e0fa5ff86b6a157c0e2a2d)in order to determine the size of the required temporary storage buffer. The user then allocates this buffer and calls[hipsparseSpSM_analysis](#hipsparse__spsm_8h_1a64862dcaca88252ee31888b611a75380)which will perform analysis on the sparse matrix \(op(A)\). Finally, the user completes the computation by calling`hipsparseSpSM_solve`

. The buffer size and analysis routines only need to be called once for a given sparse matrix \(op(A)\) while the computation can be called repeatedly with different \(B\) and \(C\) matrices. Once all calls to`hipsparseSpSM_solve`

are complete, the temporary buffer can be deallocated.As noted above, both \(B\) and \(C\) can be in row or column order (this includes mixing the order so that \(B\) is row order and \(C\) is column order and vice versa). When running on an AMD system with the rocSPARSE backend, the kernels solve the system assuming the matrices \(B\) and \(C\) are in row order as this provides the best memory access. This means that if the matrix \(C\) is not in row order and/or the matrix \(B\) is not row order (or \(B^{T}\) is not column order as this is equivalent to being in row order), then internally memory copies and/or transposing of data may be performed to get them into the correct order (possbily using extra buffer size). Once computation is completed, additional memory copies and/or transposing of data may be performed to get them back into the user arrays. For best performance and smallest required temporary storage buffers on an AMD system, use row order for the matrix \(C\) and row order for the matrix \(B\) (or column order if \(B\) is being transposed).

`hipsparseSpSM_solve`

supports[HIPSPARSE_INDEX_32I](types.html#hipsparse-generic-types_8h_1aaeacc98278238b4555b312b38a8ca3a1a39d66b98a770ce4f130cf175614bf1ee)and[HIPSPARSE_INDEX_64I](types.html#hipsparse-generic-types_8h_1aaeacc98278238b4555b312b38a8ca3a1aaf693262ac42a636addc9be11c1f534b)index precisions for storing the row pointer and column indices arrays of the sparse matrices.`hipsparseSpSM_solve`

supports the following data types for \(op(A)\), \(op(B)\), \(C\) and compute types for \(\alpha\):**Uniform Precisions:**A / B / C / compute_type

HIP_R_32F

HIP_R_64F

HIP_C_32F

HIP_C_64F

**Example**int main(int argc, char* argv[]) { // 1 0 0 0 // A = 4 2 0 0 // 0 3 7 0 // 0 0 0 1 int m = 4; int n = 2; std::vector<int> hcsr_row_ptr = {0, 1, 3, 5, 6}; std::vector<int> hcsr_col_ind = {0, 0, 1, 1, 2, 3}; std::vector<float> hcsr_val = {1, 4, 2, 3, 7, 1}; std::vector<float> hB(m * n); std::vector<float> hC(m * n); for(int i = 0; i < n; i++) { for(int j = 0; j < m; j++) { hB[m * i + j] = static_cast<float>(i + 1); } } // Scalar alpha float alpha = 1.0f; int nnz = hcsr_row_ptr[m] - hcsr_row_ptr[0]; // Offload data to device int* dcsr_row_ptr; int* dcsr_col_ind; float* dcsr_val; float* dB; float* dC; HIP_CHECK(hipMalloc((void**)&dcsr_row_ptr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&dcsr_col_ind, sizeof(int) * nnz)); HIP_CHECK(hipMalloc((void**)&dcsr_val, sizeof(float) * nnz)); HIP_CHECK(hipMalloc((void**)&dB, sizeof(float) * m * n)); HIP_CHECK(hipMalloc((void**)&dC, sizeof(float) * m * n)); HIP_CHECK( hipMemcpy(dcsr_row_ptr, hcsr_row_ptr.data(), sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK( hipMemcpy(dcsr_col_ind, hcsr_col_ind.data(), sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsr_val, hcsr_val.data(), sizeof(float) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dB, hB.data(), sizeof(float) * m * n, hipMemcpyHostToDevice)); hipsparseHandle_t handle; hipsparseSpMatDescr_t matA; hipsparseDnMatDescr_t matB; hipsparseDnMatDescr_t matC; hipsparseIndexType_t row_idx_type = HIPSPARSE_INDEX_32I; hipsparseIndexType_t col_idx_type = HIPSPARSE_INDEX_32I; hipDataType dataType = HIP_R_32F; hipDataType computeType = HIP_R_32F; hipsparseIndexBase_t idxBase = HIPSPARSE_INDEX_BASE_ZERO; hipsparseOperation_t transA = HIPSPARSE_OPERATION_NON_TRANSPOSE; hipsparseOperation_t transB = HIPSPARSE_OPERATION_NON_TRANSPOSE; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // Create sparse matrix A HIPSPARSE_CHECK(hipsparseCreateCsr(&matA, m, m, nnz, dcsr_row_ptr, dcsr_col_ind, dcsr_val, row_idx_type, col_idx_type, idxBase, dataType)); // Create dense matrix B HIPSPARSE_CHECK(hipsparseCreateDnMat(&matB, m, n, m, dB, dataType, HIPSPARSE_ORDER_COL)); // Create dense matrix C HIPSPARSE_CHECK(hipsparseCreateDnMat(&matC, m, n, m, dC, dataType, HIPSPARSE_ORDER_COL)); hipsparseSpSMDescr_t descr; HIPSPARSE_CHECK(hipsparseSpSM_createDescr(&descr)); // Call SpSM to get buffer size size_t buffer_size; HIPSPARSE_CHECK(hipsparseSpSM_bufferSize(handle, transA, transB, &alpha, matA, matB, matC, computeType, HIPSPARSE_SPSM_ALG_DEFAULT, descr, &buffer_size)); void* temp_buffer; HIP_CHECK(hipMalloc((void**)&temp_buffer, buffer_size)); // Call SpSM to perform analysis HIPSPARSE_CHECK(hipsparseSpSM_analysis(handle, transA, transB, &alpha, matA, matB, matC, computeType, HIPSPARSE_SPSM_ALG_DEFAULT, descr, temp_buffer)); // Call SpSM to perform computation HIPSPARSE_CHECK(hipsparseSpSM_solve(handle, transA, transB, &alpha, matA, matB, matC, computeType, HIPSPARSE_SPSM_ALG_DEFAULT, descr, temp_buffer)); // Copy result back to host HIP_CHECK(hipMemcpy(hC.data(), dC, sizeof(float) * m * n, hipMemcpyDeviceToHost)); // Clear hipSPARSE HIPSPARSE_CHECK(hipsparseSpSM_destroyDescr(descr)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(matA)); HIPSPARSE_CHECK(hipsparseDestroyDnMat(matB)); HIPSPARSE_CHECK(hipsparseDestroyDnMat(matC)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); // Clear device memory HIP_CHECK(hipFree(dcsr_row_ptr)); HIP_CHECK(hipFree(dcsr_col_ind)); HIP_CHECK(hipFree(dcsr_val)); HIP_CHECK(hipFree(dB)); HIP_CHECK(hipFree(dC)); HIP_CHECK(hipFree(temp_buffer)); return 0; }


- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**opA**–**[in]**matrix operation type for the sparse matrix \(A\).**opB**–**[in]**matrix operation type for the dense matrix \(B\).**alpha**–**[in]**scalar \(\alpha\).**matA**–**[in]**sparse matrix descriptor.**matB**–**[in]**dense matrix descriptor.**matC**–**[inout]**dense matrix descriptor.**computeType**–**[in]**floating point precision for the SpSM computation.**alg**–**[in]**SpSM algorithm for the SpSM computation.**spsmDescr**–**[in]**SpSM descriptor.**externalBuffer**–**[out]**temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`alpha`

,`matA`

,`matB`

,`matC`

,`spsmDescr`

or`externalBuffer`

pointer is invalid.**HIPSPARSE_STATUS_NOT_SUPPORTED**–`opA`

,`opB`

,`computeType`

or`alg`

is currently not supported.
