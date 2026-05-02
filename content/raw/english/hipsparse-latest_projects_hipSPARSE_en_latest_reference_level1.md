---
title: "Sparse level 1 functions &#8212; hipSPARSE 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipSPARSE/en/latest/reference/level1.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:09:27.559304+00:00
content_hash: "000a5f904fe9b05a"
---

# Sparse level 1 functions[#](#sparse-level-1-functions)

The sparse level 1 routines describe operations between a vector in sparse format and a vector in dense format. This section describes all hipSPARSE level 1 sparse linear algebra functions.

## hipsparseXaxpyi()[#](#hipsparsexaxpyi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSaxpyi([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int nnz, const float *alpha, const float *xVal, const int *xInd, float *y,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase)[#](#_CPPv415hipsparseSaxpyi17hipsparseHandle_tiPKfPKfPKiPf20hipsparseIndexBase_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDaxpyi([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int nnz, const double *alpha, const double *xVal, const int *xInd, double *y,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase)[#](#_CPPv415hipsparseDaxpyi17hipsparseHandle_tiPKdPKdPKiPd20hipsparseIndexBase_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCaxpyi([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int nnz, const hipComplex *alpha, const hipComplex *xVal, const int *xInd, hipComplex *y,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase)[#](#_CPPv415hipsparseCaxpyi17hipsparseHandle_tiPK10hipComplexPK10hipComplexPKiP10hipComplex20hipsparseIndexBase_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZaxpyi([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int nnz, const hipDoubleComplex *alpha, const hipDoubleComplex *xVal, const int *xInd, hipDoubleComplex *y,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase)[#](#_CPPv415hipsparseZaxpyi17hipsparseHandle_tiPK16hipDoubleComplexPK16hipDoubleComplexPKiP16hipDoubleComplex20hipsparseIndexBase_t) Scale a sparse vector and add it to a dense vector.

`hipsparseXaxpyi`

multiplies the sparse vector \(x\) with scalar \(\alpha\) and adds the result to the dense vector \(y\), such that\[ y := y + \alpha \cdot x \]for(i = 0; i < nnz; ++i) { y[xInd[i]] = y[xInd[i]] + alpha * xVal[i]; }

**Example**int main(int argc, char* argv[]) { // Number of non-zeros of the sparse vector const int nnz = 3; // Number of entries in the dense vector const int size = 9; // Sparse index vector int hxInd[nnz] = {0, 3, 5}; // Sparse value vector double hxVal[nnz] = {1.0, 2.0, 3.0}; // Dense vector double hy[size] = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0}; // Scalar alpha double alpha = 3.7; // Index base hipsparseIndexBase_t idxBase = HIPSPARSE_INDEX_BASE_ZERO; // Offload data to device int* dxInd; double* dxVal; double* dy; HIP_CHECK(hipMalloc((void**)&dxInd, sizeof(int) * nnz)); HIP_CHECK(hipMalloc((void**)&dxVal, sizeof(double) * nnz)); HIP_CHECK(hipMalloc((void**)&dy, sizeof(double) * 9)); HIP_CHECK(hipMemcpy(dxInd, hxInd, sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dxVal, hxVal, sizeof(double) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dy, hy, sizeof(double) * size, hipMemcpyHostToDevice)); // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // Call daxpyi to perform y = y + alpha * x HIPSPARSE_CHECK(hipsparseDaxpyi(handle, nnz, &alpha, dxVal, dxInd, dy, idxBase)); // Copy result back to host HIP_CHECK(hipMemcpy(hy, dy, sizeof(double) * size, hipMemcpyDeviceToHost)); std::cout << "hy" << std::endl; for(int i = 0; i < size; i++) { std::cout << hy[i] << " "; } std::cout << "" << std::endl; // Clear hipSPARSE HIPSPARSE_CHECK(hipsparseDestroy(handle)); // Clear device memory HIP_CHECK(hipFree(dxInd)); HIP_CHECK(hipFree(dxVal)); HIP_CHECK(hipFree(dy)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**nnz**–**[in]**number of non-zero entries of vector \(x\).**alpha**–**[in]**scalar \(\alpha\).**xVal**–**[in]**array of`nnz`

elements containing the values of \(x\).**xInd**–**[in]**array of`nnz`

elements containing the indices of the non-zero values of \(x\).**y**–**[inout]**array of values in dense format.**idxBase**–**[in]**[HIPSPARSE_INDEX_BASE_ZERO](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4a14913ab324aaea1154abd00ee7c50b63)or[HIPSPARSE_INDEX_BASE_ONE](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4ae48a9ab138ca9588d485c078bddc0792).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`idxBase`

,`nnz`

,`alpha`

,`xVal`

,`xInd`

or`y`

is invalid.



## hipsparseXdoti()[#](#hipsparsexdoti)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSdoti([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int nnz, const float *xVal, const int *xInd, const float *y, float *result,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase)[#](#_CPPv414hipsparseSdoti17hipsparseHandle_tiPKfPKiPKfPf20hipsparseIndexBase_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDdoti([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int nnz, const double *xVal, const int *xInd, const double *y, double *result,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase)[#](#_CPPv414hipsparseDdoti17hipsparseHandle_tiPKdPKiPKdPd20hipsparseIndexBase_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCdoti([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int nnz, const hipComplex *xVal, const int *xInd, const hipComplex *y, hipComplex *result,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase)[#](#_CPPv414hipsparseCdoti17hipsparseHandle_tiPK10hipComplexPKiPK10hipComplexP10hipComplex20hipsparseIndexBase_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZdoti([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int nnz, const hipDoubleComplex *xVal, const int *xInd, const hipDoubleComplex *y, hipDoubleComplex *result,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase)[#](#_CPPv414hipsparseZdoti17hipsparseHandle_tiPK16hipDoubleComplexPKiPK16hipDoubleComplexP16hipDoubleComplex20hipsparseIndexBase_t) Compute the dot product of a sparse vector with a dense vector.

`hipsparseXdoti`

computes the dot product of the sparse vector \(x\) with the dense vector \(y\), such that\[ result := y^T x \]result = 0 for(i = 0; i < nnz; ++i) { result += xVal[i] * y[xInd[i]]; }

**Example**int main(int argc, char* argv[]) { // Number of non-zeros of the sparse vector const int nnz = 3; // Number of entries in the dense vector const int size = 9; // Sparse index vector int hxInd[nnz] = {0, 3, 5}; // Sparse value vector float hxVal[nnz] = {1.0f, 2.0f, 3.0f}; // Dense vector float hy[size] = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f, 9.0f}; // Index base hipsparseIndexBase_t idxBase = HIPSPARSE_INDEX_BASE_ZERO; // Offload data to device int* dxInd; float* dxVal; float* dy; HIP_CHECK(hipMalloc((void**)&dxInd, sizeof(int) * nnz)); HIP_CHECK(hipMalloc((void**)&dxVal, sizeof(float) * nnz)); HIP_CHECK(hipMalloc((void**)&dy, sizeof(float) * size)); HIP_CHECK(hipMemcpy(dxInd, hxInd, sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dxVal, hxVal, sizeof(float) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dy, hy, sizeof(float) * size, hipMemcpyHostToDevice)); // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // Call sdoti to compute the dot product float dot; HIPSPARSE_CHECK(hipsparseSdoti(handle, nnz, dxVal, dxInd, dy, &dot, idxBase)); std::cout << "dot: " << dot << std::endl; // Clear hipSPARSE HIPSPARSE_CHECK(hipsparseDestroy(handle)); // Clear device memory HIP_CHECK(hipFree(dxInd)); HIP_CHECK(hipFree(dxVal)); HIP_CHECK(hipFree(dy)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**nnz**–**[in]**number of non-zero entries of vector \(x\).**xVal**–**[in]**array of`nnz`

values.**xInd**–**[in]**array of`nnz`

elements containing the indices of the non-zero values of \(x\).**y**–**[in]**array of values in dense format.**result**–**[out]**pointer to the result, can be host or device memory**idxBase**–**[in]**[HIPSPARSE_INDEX_BASE_ZERO](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4a14913ab324aaea1154abd00ee7c50b63)or[HIPSPARSE_INDEX_BASE_ONE](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4ae48a9ab138ca9588d485c078bddc0792).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`idxBase`

,`nnz`

,`xVal`

,`xInd`

,`y`

or`result`

is invalid.**HIPSPARSE_STATUS_ALLOC_FAILED**– the buffer for the dot product reduction could not be allocated.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.



## hipsparseXdotci()[#](#hipsparsexdotci)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCdotci([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int nnz, const hipComplex *xVal, const int *xInd, const hipComplex *y, hipComplex *result,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase)[#](#_CPPv415hipsparseCdotci17hipsparseHandle_tiPK10hipComplexPKiPK10hipComplexP10hipComplex20hipsparseIndexBase_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZdotci([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int nnz, const hipDoubleComplex *xVal, const int *xInd, const hipDoubleComplex *y, hipDoubleComplex *result,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase)[#](#_CPPv415hipsparseZdotci17hipsparseHandle_tiPK16hipDoubleComplexPKiPK16hipDoubleComplexP16hipDoubleComplex20hipsparseIndexBase_t) Compute the dot product of a complex conjugate sparse vector with a dense vector.

`hipsparseXdotci`

computes the dot product of the complex conjugate sparse vector \(x\) with the dense vector \(y\), such that\[ result := \bar{x}^H y \]result = 0 for(i = 0; i < nnz; ++i) { result += conj(xVal[i]) * y[xInd[i]]; }

Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**nnz**–**[in]**number of non-zero entries of vector \(x\).**xVal**–**[in]**array of`nnz`

values.**xInd**–**[in]**array of`nnz`

elements containing the indices of the non-zero values of \(x\).**y**–**[in]**array of values in dense format.**result**–**[out]**pointer to the result, can be host or device memory**idxBase**–**[in]**[HIPSPARSE_INDEX_BASE_ZERO](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4a14913ab324aaea1154abd00ee7c50b63)or[HIPSPARSE_INDEX_BASE_ONE](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4ae48a9ab138ca9588d485c078bddc0792).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`idxBase`

,`nnz`

,`xVal`

,`xInd`

,`y`

or`result`

is invalid.**HIPSPARSE_STATUS_ALLOC_FAILED**– the buffer for the dot product reduction could not be allocated.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.



## hipsparseXgthr()[#](#hipsparsexgthr)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSgthr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int nnz, const float *y, float *xVal, const int *xInd,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase)[#](#_CPPv414hipsparseSgthr17hipsparseHandle_tiPKfPfPKi20hipsparseIndexBase_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDgthr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int nnz, const double *y, double *xVal, const int *xInd,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase)[#](#_CPPv414hipsparseDgthr17hipsparseHandle_tiPKdPdPKi20hipsparseIndexBase_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCgthr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int nnz, const hipComplex *y, hipComplex *xVal, const int *xInd,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase)[#](#_CPPv414hipsparseCgthr17hipsparseHandle_tiPK10hipComplexP10hipComplexPKi20hipsparseIndexBase_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZgthr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int nnz, const hipDoubleComplex *y, hipDoubleComplex *xVal, const int *xInd,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase)[#](#_CPPv414hipsparseZgthr17hipsparseHandle_tiPK16hipDoubleComplexP16hipDoubleComplexPKi20hipsparseIndexBase_t) Gather elements from a dense vector and store them into a sparse vector.

`hipsparseXgthr`

gathers the elements that are listed in`xInd`

from the dense vector \(y\) and stores them in the sparse vector \(x\).for(i = 0; i < nnz; ++i) { xVal[i] = y[xInd[i]]; }

**Example**int main(int argc, char* argv[]) { // Number of non-zeros of the sparse vector const int nnz = 3; // Number of entries in the dense vector const int size = 9; // Sparse index vector int hxInd[nnz] = {0, 3, 5}; // Sparse value vector float hxVal[nnz]; // Dense vector float hy[size] = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0}; // Index base hipsparseIndexBase_t idxBase = HIPSPARSE_INDEX_BASE_ZERO; // Offload data to device int* dxInd; float* dxVal; float* dy; HIP_CHECK(hipMalloc((void**)&dxInd, sizeof(int) * nnz)); HIP_CHECK(hipMalloc((void**)&dxVal, sizeof(float) * nnz)); HIP_CHECK(hipMalloc((void**)&dy, sizeof(float) * size)); HIP_CHECK(hipMemcpy(dxInd, hxInd, sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dy, hy, sizeof(float) * size, hipMemcpyHostToDevice)); // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // Call sgthr HIPSPARSE_CHECK(hipsparseSgthr(handle, nnz, dy, dxVal, dxInd, idxBase)); // Copy result back to host HIP_CHECK(hipMemcpy(hxVal, dxVal, sizeof(float) * nnz, hipMemcpyDeviceToHost)); std::cout << "hxVal" << std::endl; for(int i = 0; i < nnz; i++) { std::cout << hxVal[i] << " "; } std::cout << "" << std::endl; // Clear hipSPARSE HIPSPARSE_CHECK(hipsparseDestroy(handle)); // Clear device memory HIP_CHECK(hipFree(dxInd)); HIP_CHECK(hipFree(dxVal)); HIP_CHECK(hipFree(dy)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**nnz**–**[in]**number of non-zero entries of \(x\).**y**–**[in]**array of values in dense format.**xVal**–**[out]**array of`nnz`

elements containing the values of \(x\).**xInd**–**[in]**array of`nnz`

elements containing the indices of the non-zero values of \(x\).**idxBase**–**[in]**[HIPSPARSE_INDEX_BASE_ZERO](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4a14913ab324aaea1154abd00ee7c50b63)or[HIPSPARSE_INDEX_BASE_ONE](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4ae48a9ab138ca9588d485c078bddc0792).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`idxBase`

,`nnz`

,`y`

,`xVal`

or`xInd`

is invalid.



## hipsparseXgthrz()[#](#hipsparsexgthrz)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSgthrz([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int nnz, float *y, float *xVal, const int *xInd,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase)[#](#_CPPv415hipsparseSgthrz17hipsparseHandle_tiPfPfPKi20hipsparseIndexBase_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDgthrz([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int nnz, double *y, double *xVal, const int *xInd,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase)[#](#_CPPv415hipsparseDgthrz17hipsparseHandle_tiPdPdPKi20hipsparseIndexBase_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCgthrz([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int nnz, hipComplex *y, hipComplex *xVal, const int *xInd,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase)[#](#_CPPv415hipsparseCgthrz17hipsparseHandle_tiP10hipComplexP10hipComplexPKi20hipsparseIndexBase_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZgthrz([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int nnz, hipDoubleComplex *y, hipDoubleComplex *xVal, const int *xInd,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase)[#](#_CPPv415hipsparseZgthrz17hipsparseHandle_tiP16hipDoubleComplexP16hipDoubleComplexPKi20hipsparseIndexBase_t) Gather and zero out elements from a dense vector and store them into a sparse vector.

`hipsparseXgthrz`

gathers the elements that are listed in`xInd`

from the dense vector \(y\) and stores them in the sparse vector \(x\). The gathered elements in \(y\) are replaced by zero.for(i = 0; i < nnz; ++i) { xVal[i] = y[xInd[i]]; y[xInd[i]] = 0; }

Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**nnz**–**[in]**number of non-zero entries of \(x\).**y**–**[inout]**array of values in dense format.**xVal**–**[out]**array of`nnz`

elements containing the non-zero values of \(x\).**xInd**–**[in]**array of`nnz`

elements containing the indices of the non-zero values of \(x\).**idxBase**–**[in]**[HIPSPARSE_INDEX_BASE_ZERO](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4a14913ab324aaea1154abd00ee7c50b63)or[HIPSPARSE_INDEX_BASE_ONE](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4ae48a9ab138ca9588d485c078bddc0792).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`idxBase`

,`nnz`

,`y`

,`xVal`

or`xInd`

is invalid.



## hipsparseXroti()[#](#hipsparsexroti)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSroti([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int nnz, float *xVal, const int *xInd, float *y, const float *c, const float *s,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase)[#](#_CPPv414hipsparseSroti17hipsparseHandle_tiPfPKiPfPKfPKf20hipsparseIndexBase_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDroti([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int nnz, double *xVal, const int *xInd, double *y, const double *c, const double *s,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase)[#](#_CPPv414hipsparseDroti17hipsparseHandle_tiPdPKiPdPKdPKd20hipsparseIndexBase_t) Apply Givens rotation to a dense and a sparse vector.

`hipsparseXroti`

applies the Givens rotation matrix \(G\) to the sparse vector \(x\) and the dense vector \(y\), where\[\begin{split} G = \begin{pmatrix} c & s \\ -s & c \end{pmatrix} \end{split}\]for(i = 0; i < nnz; ++i) { x_tmp = xVal[i]; y_tmp = y[xInd[i]]; xVal[i] = c * x_tmp + s * y_tmp; y[xInd[i]] = c * y_tmp - s * x_tmp; }

**Example**int main(int argc, char* argv[]) { // Number of non-zeros of the sparse vector const int nnz = 3; // Number of entries in the dense vector const int size = 9; // Sparse index vector int hxInd[nnz] = {0, 3, 5}; // Sparse value vector float hxVal[nnz] = {1.0f, 2.0f, 3.0f}; // Dense vector float hy[size] = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f, 9.0f}; // c and s float c = 3.7; float s = 1.3; // Index base hipsparseIndexBase_t idxBase = HIPSPARSE_INDEX_BASE_ZERO; // Offload data to device int* dxInd; float* dxVal; float* dy; HIP_CHECK(hipMalloc((void**)&dxInd, sizeof(int) * nnz)); HIP_CHECK(hipMalloc((void**)&dxVal, sizeof(float) * nnz)); HIP_CHECK(hipMalloc((void**)&dy, sizeof(float) * size)); HIP_CHECK(hipMemcpy(dxInd, hxInd, sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dxVal, hxVal, sizeof(float) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dy, hy, sizeof(float) * size, hipMemcpyHostToDevice)); // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // Call sroti HIPSPARSE_CHECK(hipsparseSroti(handle, nnz, dxVal, dxInd, dy, &c, &s, idxBase)); // Copy result back to host HIP_CHECK(hipMemcpy(hxVal, dxVal, sizeof(float) * nnz, hipMemcpyDeviceToHost)); HIP_CHECK(hipMemcpy(hy, dy, sizeof(float) * size, hipMemcpyDeviceToHost)); std::cout << "hxVal" << std::endl; for(int i = 0; i < nnz; i++) { std::cout << hxVal[i] << " "; } std::cout << "" << std::endl; std::cout << "hy" << std::endl; for(int i = 0; i < size; i++) { std::cout << hy[i] << " "; } std::cout << "" << std::endl; // Clear hipSPARSE HIPSPARSE_CHECK(hipsparseDestroy(handle)); // Clear device memory HIP_CHECK(hipFree(dxInd)); HIP_CHECK(hipFree(dxVal)); HIP_CHECK(hipFree(dy)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**nnz**–**[in]**number of non-zero entries of \(x\).**xVal**–**[inout]**array of`nnz`

elements containing the non-zero values of \(x\).**xInd**–**[in]**array of`nnz`

elements containing the indices of the non-zero values of \(x\).**y**–**[inout]**array of values in dense format.**c**–**[in]**pointer to the cosine element of \(G\), can be on host or device.**s**–**[in]**pointer to the sine element of \(G\), can be on host or device.**idxBase**–**[in]**[HIPSPARSE_INDEX_BASE_ZERO](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4a14913ab324aaea1154abd00ee7c50b63)or[HIPSPARSE_INDEX_BASE_ONE](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4ae48a9ab138ca9588d485c078bddc0792).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`idxBase`

,`nnz`

,`c`

,`s`

,`xVal`

,`xInd`

or`y`

is invalid.



## hipsparseXsctr()[#](#hipsparsexsctr)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSsctr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int nnz, const float *xVal, const int *xInd, float *y,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase)[#](#_CPPv414hipsparseSsctr17hipsparseHandle_tiPKfPKiPf20hipsparseIndexBase_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDsctr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int nnz, const double *xVal, const int *xInd, double *y,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase)[#](#_CPPv414hipsparseDsctr17hipsparseHandle_tiPKdPKiPd20hipsparseIndexBase_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCsctr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int nnz, const hipComplex *xVal, const int *xInd, hipComplex *y,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase)[#](#_CPPv414hipsparseCsctr17hipsparseHandle_tiPK10hipComplexPKiP10hipComplex20hipsparseIndexBase_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZsctr([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int nnz, const hipDoubleComplex *xVal, const int *xInd, hipDoubleComplex *y,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase)[#](#_CPPv414hipsparseZsctr17hipsparseHandle_tiPK16hipDoubleComplexPKiP16hipDoubleComplex20hipsparseIndexBase_t) Scatter elements from a dense vector across a sparse vector.

`hipsparseXsctr`

scatters the elements that are listed in`xInd`

from the sparse vector \(x\) into the dense vector \(y\). Indices of \(y\) that are not listed in`xInd`

remain unchanged.for(i = 0; i < nnz; ++i) { y[xInd[i]] = xVal[i]; }

**Example**int main(int argc, char* argv[]) { // Number of non-zeros of the sparse vector const int nnz = 3; // Number of entries in the dense vector const int size = 9; // Sparse index vector int hxInd[nnz] = {0, 3, 5}; // Sparse value vector float hxVal[nnz] = {9.0, 2.0, 3.0}; // Dense vector float hy[size] = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0}; // Index base hipsparseIndexBase_t idxBase = HIPSPARSE_INDEX_BASE_ZERO; // Offload data to device int* dxInd; float* dxVal; float* dy; HIP_CHECK(hipMalloc((void**)&dxInd, sizeof(int) * nnz)); HIP_CHECK(hipMalloc((void**)&dxVal, sizeof(float) * nnz)); HIP_CHECK(hipMalloc((void**)&dy, sizeof(float) * size)); HIP_CHECK(hipMemcpy(dxInd, hxInd, sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dxVal, hxVal, sizeof(float) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dy, hy, sizeof(float) * size, hipMemcpyHostToDevice)); // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // Call ssctr HIPSPARSE_CHECK(hipsparseSsctr(handle, nnz, dxVal, dxInd, dy, idxBase)); // Copy result back to host HIP_CHECK(hipMemcpy(hy, dy, sizeof(float) * size, hipMemcpyDeviceToHost)); std::cout << "hy" << std::endl; for(int i = 0; i < size; i++) { std::cout << hy[i] << " "; } std::cout << "" << std::endl; // Clear hipSPARSE HIPSPARSE_CHECK(hipsparseDestroy(handle)); // Clear device memory HIP_CHECK(hipFree(dxInd)); HIP_CHECK(hipFree(dxVal)); HIP_CHECK(hipFree(dy)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**nnz**–**[in]**number of non-zero entries of \(x\).**xVal**–**[in]**array of`nnz`

elements containing the non-zero values of \(x\).**xInd**–**[in]**array of`nnz`

elements containing the indices of the non-zero values of x.**y**–**[inout]**array of values in dense format.**idxBase**–**[in]**[HIPSPARSE_INDEX_BASE_ZERO](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4a14913ab324aaea1154abd00ee7c50b63)or[HIPSPARSE_INDEX_BASE_ONE](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4ae48a9ab138ca9588d485c078bddc0792).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`idxBase`

,`nnz`

,`xVal`

,`xInd`

or`y`

is invalid.
