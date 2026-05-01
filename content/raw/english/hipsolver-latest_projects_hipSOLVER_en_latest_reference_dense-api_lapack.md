---
title: "Dense matrix LAPACK functions &#8212; hipSOLVER 3.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/dense-api/lapack.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:20:57.418912+00:00
content_hash: "9a2454bc5c6f767b"
---

# Dense matrix LAPACK functions[#](#dense-matrix-lapack-functions)

LAPACK routines solve complex numerical linear algebra problems. These functions are organized into the following categories:

[Triangular factorizations](#dense-triangular): Based on Gaussian elimination.[Orthogonal factorizations](#dense-orthogonal): Based on Householder reflections.[Problem and matrix reductions](#dense-reductions): Transformation of matrices and problems into equivalent forms.[Linear-systems solvers](#dense-linears): Based on triangular factorizations.[Least-squares solvers](#dense-leastsqr): Based on orthogonal factorizations.[Symmetric eigensolvers](#dense-eigens): Eigenproblems for symmetric matrices.[Singular value decomposition](#dense-svds): Singular values and related problems for general matrices.

## Triangular factorizations[#](#triangular-factorizations)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnXpotrf_bufferSize([hipsolverDnHandle_t](types.html#_CPPv419hipsolverDnHandle_t)handle, hipsolverDnParams_t params,[hipsolverFillMode_t](../api/types.html#_CPPv419hipsolverFillMode_t)uplo, int64_t n, hipDataType dataTypeA, const void *A, int64_t lda, hipDataType computeType, size_t *lworkOnDevice, size_t *lworkOnHost)[#](#_CPPv428hipsolverDnXpotrf_bufferSize19hipsolverDnHandle_t19hipsolverDnParams_t19hipsolverFillMode_t7int64_t11hipDataTypePKv7int64_t11hipDataTypeP6size_tP6size_t)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnZpotrf_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, hipDoubleComplex *A, int lda, int *lwork)[#](#_CPPv428hipsolverDnZpotrf_bufferSize17hipsolverHandle_t17hipblasFillMode_tiP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnCpotrf_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, hipFloatComplex *A, int lda, int *lwork)[#](#_CPPv428hipsolverDnCpotrf_bufferSize17hipsolverHandle_t17hipblasFillMode_tiP15hipFloatComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDpotrf_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, double *A, int lda, int *lwork)[#](#_CPPv428hipsolverDnDpotrf_bufferSize17hipsolverHandle_t17hipblasFillMode_tiPdiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSpotrf_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, float *A, int lda, int *lwork)[#](#_CPPv428hipsolverDnSpotrf_bufferSize17hipsolverHandle_t17hipblasFillMode_tiPfiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnXpotrf([hipsolverDnHandle_t](types.html#_CPPv419hipsolverDnHandle_t)handle, hipsolverDnParams_t params,[hipsolverFillMode_t](../api/types.html#_CPPv419hipsolverFillMode_t)uplo, int64_t n, hipDataType dataTypeA, void *A, int64_t lda, hipDataType computeType, void *workOnDevice, size_t lworkOnDevice, void *workOnHost, size_t lworkOnHost, int *info)[#](#_CPPv417hipsolverDnXpotrf19hipsolverDnHandle_t19hipsolverDnParams_t19hipsolverFillMode_t7int64_t11hipDataTypePv7int64_t11hipDataTypePv6size_tPv6size_tPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnZpotrf([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, hipDoubleComplex *A, int lda, hipDoubleComplex *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnZpotrf17hipsolverHandle_t17hipblasFillMode_tiP16hipDoubleComplexiP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnCpotrf([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, hipFloatComplex *A, int lda, hipFloatComplex *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnCpotrf17hipsolverHandle_t17hipblasFillMode_tiP15hipFloatComplexiP15hipFloatComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDpotrf([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, double *A, int lda, double *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnDpotrf17hipsolverHandle_t17hipblasFillMode_tiPdiPdiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSpotrf([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, float *A, int lda, float *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnSpotrf17hipsolverHandle_t17hipblasFillMode_tiPfiPfiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnZpotrfBatched([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, hipDoubleComplex *A[], int lda, int *devInfo, int batch_count)[#](#_CPPv424hipsolverDnZpotrfBatched17hipsolverHandle_t17hipblasFillMode_tiA_P16hipDoubleComplexiPii)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnCpotrfBatched([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, hipFloatComplex *A[], int lda, int *devInfo, int batch_count)[#](#_CPPv424hipsolverDnCpotrfBatched17hipsolverHandle_t17hipblasFillMode_tiA_P15hipFloatComplexiPii)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDpotrfBatched([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, double *A[], int lda, int *devInfo, int batch_count)[#](#_CPPv424hipsolverDnDpotrfBatched17hipsolverHandle_t17hipblasFillMode_tiA_PdiPii)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSpotrfBatched([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, float *A[], int lda, int *devInfo, int batch_count)[#](#_CPPv424hipsolverDnSpotrfBatched17hipsolverHandle_t17hipblasFillMode_tiA_PfiPii)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnXgetrf_bufferSize([hipsolverDnHandle_t](types.html#_CPPv419hipsolverDnHandle_t)handle, hipsolverDnParams_t params, int64_t m, int64_t n, hipDataType dataTypeA, const void *A, int64_t lda, hipDataType computeType, size_t *lworkOnDevice, size_t *lworkOnHost)[#](#_CPPv428hipsolverDnXgetrf_bufferSize19hipsolverDnHandle_t19hipsolverDnParams_t7int64_t7int64_t11hipDataTypePKv7int64_t11hipDataTypeP6size_tP6size_t)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnZgetrf_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, hipDoubleComplex *A, int lda, int *lwork)[#](#_CPPv428hipsolverDnZgetrf_bufferSize17hipsolverHandle_tiiP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnCgetrf_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, hipFloatComplex *A, int lda, int *lwork)[#](#_CPPv428hipsolverDnCgetrf_bufferSize17hipsolverHandle_tiiP15hipFloatComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDgetrf_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, double *A, int lda, int *lwork)[#](#_CPPv428hipsolverDnDgetrf_bufferSize17hipsolverHandle_tiiPdiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSgetrf_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, float *A, int lda, int *lwork)[#](#_CPPv428hipsolverDnSgetrf_bufferSize17hipsolverHandle_tiiPfiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnXgetrf([hipsolverDnHandle_t](types.html#_CPPv419hipsolverDnHandle_t)handle, hipsolverDnParams_t params, int64_t m, int64_t n, hipDataType dataTypeA, void *A, int64_t lda, int64_t *devIpiv, hipDataType computeType, void *workOnDevice, size_t lworkOnDevice, void *workOnHost, size_t lworkOnHost, int *devInfo)[#](#_CPPv417hipsolverDnXgetrf19hipsolverDnHandle_t19hipsolverDnParams_t7int64_t7int64_t11hipDataTypePv7int64_tP7int64_t11hipDataTypePv6size_tPv6size_tPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnZgetrf([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, hipDoubleComplex *A, int lda, hipDoubleComplex *work, int *devIpiv, int *devInfo)[#](#_CPPv417hipsolverDnZgetrf17hipsolverHandle_tiiP16hipDoubleComplexiP16hipDoubleComplexPiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnCgetrf([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, hipFloatComplex *A, int lda, hipFloatComplex *work, int *devIpiv, int *devInfo)[#](#_CPPv417hipsolverDnCgetrf17hipsolverHandle_tiiP15hipFloatComplexiP15hipFloatComplexPiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDgetrf([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, double *A, int lda, double *work, int *devIpiv, int *devInfo)[#](#_CPPv417hipsolverDnDgetrf17hipsolverHandle_tiiPdiPdPiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSgetrf([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, float *A, int lda, float *work, int *devIpiv, int *devInfo)[#](#_CPPv417hipsolverDnSgetrf17hipsolverHandle_tiiPfiPfPiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnZsytrf_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int n, hipDoubleComplex *A, int lda, int *lwork)[#](#_CPPv428hipsolverDnZsytrf_bufferSize17hipsolverHandle_tiP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnCsytrf_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int n, hipFloatComplex *A, int lda, int *lwork)[#](#_CPPv428hipsolverDnCsytrf_bufferSize17hipsolverHandle_tiP15hipFloatComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDsytrf_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int n, double *A, int lda, int *lwork)[#](#_CPPv428hipsolverDnDsytrf_bufferSize17hipsolverHandle_tiPdiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSsytrf_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int n, float *A, int lda, int *lwork)[#](#_CPPv428hipsolverDnSsytrf_bufferSize17hipsolverHandle_tiPfiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnZsytrf([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, hipDoubleComplex *A, int lda, int *ipiv, hipDoubleComplex *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnZsytrf17hipsolverHandle_t17hipblasFillMode_tiP16hipDoubleComplexiPiP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnCsytrf([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, hipFloatComplex *A, int lda, int *ipiv, hipFloatComplex *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnCsytrf17hipsolverHandle_t17hipblasFillMode_tiP15hipFloatComplexiPiP15hipFloatComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDsytrf([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, double *A, int lda, int *ipiv, double *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnDsytrf17hipsolverHandle_t17hipblasFillMode_tiPdiPiPdiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSsytrf([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, float *A, int lda, int *ipiv, float *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnSsytrf17hipsolverHandle_t17hipblasFillMode_tiPfiPiPfiPi)

## Orthogonal factorizations[#](#orthogonal-factorizations)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnXgeqrf_bufferSize([hipsolverDnHandle_t](types.html#_CPPv419hipsolverDnHandle_t)handle, hipsolverDnParams_t params, int64_t m, int64_t n, hipDataType dataTypeA, const void *A, int64_t lda, hipDataType dataTypeTau, const void *tau, hipDataType computeType, size_t *lworkOnDevice, size_t *lworkOnHost)[#](#_CPPv428hipsolverDnXgeqrf_bufferSize19hipsolverDnHandle_t19hipsolverDnParams_t7int64_t7int64_t11hipDataTypePKv7int64_t11hipDataTypePKv11hipDataTypeP6size_tP6size_t)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnZgeqrf_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, hipDoubleComplex *A, int lda, int *lwork)[#](#_CPPv428hipsolverDnZgeqrf_bufferSize17hipsolverHandle_tiiP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnCgeqrf_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, hipFloatComplex *A, int lda, int *lwork)[#](#_CPPv428hipsolverDnCgeqrf_bufferSize17hipsolverHandle_tiiP15hipFloatComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDgeqrf_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, double *A, int lda, int *lwork)[#](#_CPPv428hipsolverDnDgeqrf_bufferSize17hipsolverHandle_tiiPdiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSgeqrf_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, float *A, int lda, int *lwork)[#](#_CPPv428hipsolverDnSgeqrf_bufferSize17hipsolverHandle_tiiPfiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnXgeqrf([hipsolverDnHandle_t](types.html#_CPPv419hipsolverDnHandle_t)handle, hipsolverDnParams_t params, int64_t m, int64_t n, hipDataType dataTypeA, void *A, int64_t lda, hipDataType dataTypeTau, void *tau, hipDataType computeType, void *workOnDevice, size_t lworkOnDevice, void *workOnHost, size_t lworkOnHost, int *devInfo)[#](#_CPPv417hipsolverDnXgeqrf19hipsolverDnHandle_t19hipsolverDnParams_t7int64_t7int64_t11hipDataTypePv7int64_t11hipDataTypePv11hipDataTypePv6size_tPv6size_tPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnZgeqrf([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, hipDoubleComplex *A, int lda, hipDoubleComplex *tau, hipDoubleComplex *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnZgeqrf17hipsolverHandle_tiiP16hipDoubleComplexiP16hipDoubleComplexP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnCgeqrf([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, hipFloatComplex *A, int lda, hipFloatComplex *tau, hipFloatComplex *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnCgeqrf17hipsolverHandle_tiiP15hipFloatComplexiP15hipFloatComplexP15hipFloatComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDgeqrf([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, double *A, int lda, double *tau, double *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnDgeqrf17hipsolverHandle_tiiPdiPdPdiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSgeqrf([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, float *A, int lda, float *tau, float *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnSgeqrf17hipsolverHandle_tiiPfiPfPfiPi)

## Problem and matrix reductions[#](#problem-and-matrix-reductions)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnZgebrd_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int *lwork)[#](#_CPPv428hipsolverDnZgebrd_bufferSize17hipsolverHandle_tiiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnCgebrd_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int *lwork)[#](#_CPPv428hipsolverDnCgebrd_bufferSize17hipsolverHandle_tiiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDgebrd_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int *lwork)[#](#_CPPv428hipsolverDnDgebrd_bufferSize17hipsolverHandle_tiiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSgebrd_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int *lwork)[#](#_CPPv428hipsolverDnSgebrd_bufferSize17hipsolverHandle_tiiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnZgebrd([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, hipDoubleComplex *A, int lda, double *D, double *E, hipDoubleComplex *tauq, hipDoubleComplex *taup, hipDoubleComplex *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnZgebrd17hipsolverHandle_tiiP16hipDoubleComplexiPdPdP16hipDoubleComplexP16hipDoubleComplexP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnCgebrd([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, hipFloatComplex *A, int lda, float *D, float *E, hipFloatComplex *tauq, hipFloatComplex *taup, hipFloatComplex *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnCgebrd17hipsolverHandle_tiiP15hipFloatComplexiPfPfP15hipFloatComplexP15hipFloatComplexP15hipFloatComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDgebrd([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, double *A, int lda, double *D, double *E, double *tauq, double *taup, double *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnDgebrd17hipsolverHandle_tiiPdiPdPdPdPdPdiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSgebrd([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, float *A, int lda, float *D, float *E, float *tauq, float *taup, float *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnSgebrd17hipsolverHandle_tiiPfiPfPfPfPfPfiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDsytrd_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, const double *A, int lda, const double *D, const double *E, const double *tau, int *lwork)[#](#_CPPv428hipsolverDnDsytrd_bufferSize17hipsolverHandle_t17hipblasFillMode_tiPKdiPKdPKdPKdPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSsytrd_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, const float *A, int lda, const float *D, const float *E, const float *tau, int *lwork)[#](#_CPPv428hipsolverDnSsytrd_bufferSize17hipsolverHandle_t17hipblasFillMode_tiPKfiPKfPKfPKfPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnZhetrd_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, const hipDoubleComplex *A, int lda, const double *D, const double *E, const hipDoubleComplex *tau, int *lwork)[#](#_CPPv428hipsolverDnZhetrd_bufferSize17hipsolverHandle_t17hipblasFillMode_tiPK16hipDoubleComplexiPKdPKdPK16hipDoubleComplexPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnChetrd_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, const hipFloatComplex *A, int lda, const float *D, const float *E, const hipFloatComplex *tau, int *lwork)[#](#_CPPv428hipsolverDnChetrd_bufferSize17hipsolverHandle_t17hipblasFillMode_tiPK15hipFloatComplexiPKfPKfPK15hipFloatComplexPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDsytrd([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, double *A, int lda, double *D, double *E, double *tau, double *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnDsytrd17hipsolverHandle_t17hipblasFillMode_tiPdiPdPdPdPdiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSsytrd([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, float *A, int lda, float *D, float *E, float *tau, float *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnSsytrd17hipsolverHandle_t17hipblasFillMode_tiPfiPfPfPfPfiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnZhetrd([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, hipDoubleComplex *A, int lda, double *D, double *E, hipDoubleComplex *tau, hipDoubleComplex *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnZhetrd17hipsolverHandle_t17hipblasFillMode_tiP16hipDoubleComplexiPdPdP16hipDoubleComplexP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnChetrd([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, hipFloatComplex *A, int lda, float *D, float *E, hipFloatComplex *tau, hipFloatComplex *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnChetrd17hipsolverHandle_t17hipblasFillMode_tiP15hipFloatComplexiPfPfP15hipFloatComplexP15hipFloatComplexiPi)

## Linear-systems solvers[#](#linear-systems-solvers)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnZpotri_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, hipDoubleComplex *A, int lda, int *lwork)[#](#_CPPv428hipsolverDnZpotri_bufferSize17hipsolverHandle_t17hipblasFillMode_tiP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnCpotri_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, hipFloatComplex *A, int lda, int *lwork)[#](#_CPPv428hipsolverDnCpotri_bufferSize17hipsolverHandle_t17hipblasFillMode_tiP15hipFloatComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDpotri_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, double *A, int lda, int *lwork)[#](#_CPPv428hipsolverDnDpotri_bufferSize17hipsolverHandle_t17hipblasFillMode_tiPdiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSpotri_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, float *A, int lda, int *lwork)[#](#_CPPv428hipsolverDnSpotri_bufferSize17hipsolverHandle_t17hipblasFillMode_tiPfiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnZpotri([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, hipDoubleComplex *A, int lda, hipDoubleComplex *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnZpotri17hipsolverHandle_t17hipblasFillMode_tiP16hipDoubleComplexiP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnCpotri([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, hipFloatComplex *A, int lda, hipFloatComplex *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnCpotri17hipsolverHandle_t17hipblasFillMode_tiP15hipFloatComplexiP15hipFloatComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDpotri([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, double *A, int lda, double *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnDpotri17hipsolverHandle_t17hipblasFillMode_tiPdiPdiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSpotri([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, float *A, int lda, float *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnSpotri17hipsolverHandle_t17hipblasFillMode_tiPfiPfiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnXpotrs([hipsolverDnHandle_t](types.html#_CPPv419hipsolverDnHandle_t)handle, hipsolverDnParams_t params,[hipsolverFillMode_t](../api/types.html#_CPPv419hipsolverFillMode_t)uplo, int64_t n, int64_t nrhs, hipDataType dataTypeA, const void *A, int64_t lda, hipDataType dataTypeB, void *B, int64_t ldb, int *info)[#](#_CPPv417hipsolverDnXpotrs19hipsolverDnHandle_t19hipsolverDnParams_t19hipsolverFillMode_t7int64_t7int64_t11hipDataTypePKv7int64_t11hipDataTypePv7int64_tPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnZpotrs([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, int nrhs, const hipDoubleComplex *A, int lda, hipDoubleComplex *B, int ldb, int *devInfo)[#](#_CPPv417hipsolverDnZpotrs17hipsolverHandle_t17hipblasFillMode_tiiPK16hipDoubleComplexiP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnCpotrs([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, int nrhs, const hipFloatComplex *A, int lda, hipFloatComplex *B, int ldb, int *devInfo)[#](#_CPPv417hipsolverDnCpotrs17hipsolverHandle_t17hipblasFillMode_tiiPK15hipFloatComplexiP15hipFloatComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDpotrs([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, int nrhs, const double *A, int lda, double *B, int ldb, int *devInfo)[#](#_CPPv417hipsolverDnDpotrs17hipsolverHandle_t17hipblasFillMode_tiiPKdiPdiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSpotrs([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, int nrhs, const float *A, int lda, float *B, int ldb, int *devInfo)[#](#_CPPv417hipsolverDnSpotrs17hipsolverHandle_t17hipblasFillMode_tiiPKfiPfiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnZpotrsBatched([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, int nrhs, hipDoubleComplex *A[], int lda, hipDoubleComplex *B[], int ldb, int *devInfo, int batch_count)[#](#_CPPv424hipsolverDnZpotrsBatched17hipsolverHandle_t17hipblasFillMode_tiiA_P16hipDoubleComplexiA_P16hipDoubleComplexiPii)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnCpotrsBatched([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, int nrhs, hipFloatComplex *A[], int lda, hipFloatComplex *B[], int ldb, int *devInfo, int batch_count)[#](#_CPPv424hipsolverDnCpotrsBatched17hipsolverHandle_t17hipblasFillMode_tiiA_P15hipFloatComplexiA_P15hipFloatComplexiPii)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDpotrsBatched([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, int nrhs, double *A[], int lda, double *B[], int ldb, int *devInfo, int batch_count)[#](#_CPPv424hipsolverDnDpotrsBatched17hipsolverHandle_t17hipblasFillMode_tiiA_PdiA_PdiPii)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSpotrsBatched([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, int nrhs, float *A[], int lda, float *B[], int ldb, int *devInfo, int batch_count)[#](#_CPPv424hipsolverDnSpotrsBatched17hipsolverHandle_t17hipblasFillMode_tiiA_PfiA_PfiPii)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnXgetrs([hipsolverDnHandle_t](types.html#_CPPv419hipsolverDnHandle_t)handle, hipsolverDnParams_t params,[hipsolverOperation_t](../api/types.html#_CPPv420hipsolverOperation_t)trans, int64_t n, int64_t nrhs, hipDataType dataTypeA, const void *A, int64_t lda, const int64_t *devIpiv, hipDataType dataTypeB, void *B, int64_t ldb, int *devInfo)[#](#_CPPv417hipsolverDnXgetrs19hipsolverDnHandle_t19hipsolverDnParams_t20hipsolverOperation_t7int64_t7int64_t11hipDataTypePKv7int64_tPK7int64_t11hipDataTypePv7int64_tPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnZgetrs([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasOperation_t](../api/types.html#_CPPv418hipblasOperation_t)trans, int n, int nrhs, const hipDoubleComplex *A, int lda, const int *devIpiv, hipDoubleComplex *B, int ldb, int *devInfo)[#](#_CPPv417hipsolverDnZgetrs17hipsolverHandle_t18hipblasOperation_tiiPK16hipDoubleComplexiPKiP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnCgetrs([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasOperation_t](../api/types.html#_CPPv418hipblasOperation_t)trans, int n, int nrhs, const hipFloatComplex *A, int lda, const int *devIpiv, hipFloatComplex *B, int ldb, int *devInfo)[#](#_CPPv417hipsolverDnCgetrs17hipsolverHandle_t18hipblasOperation_tiiPK15hipFloatComplexiPKiP15hipFloatComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDgetrs([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasOperation_t](../api/types.html#_CPPv418hipblasOperation_t)trans, int n, int nrhs, const double *A, int lda, const int *devIpiv, double *B, int ldb, int *devInfo)[#](#_CPPv417hipsolverDnDgetrs17hipsolverHandle_t18hipblasOperation_tiiPKdiPKiPdiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSgetrs([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasOperation_t](../api/types.html#_CPPv418hipblasOperation_t)trans, int n, int nrhs, const float *A, int lda, const int *devIpiv, float *B, int ldb, int *devInfo)[#](#_CPPv417hipsolverDnSgetrs17hipsolverHandle_t18hipblasOperation_tiiPKfiPKiPfiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnZZgesv_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int n, int nrhs, hipDoubleComplex *A, int lda, int *devIpiv, hipDoubleComplex *B, int ldb, hipDoubleComplex *X, int ldx, void *work, size_t *lwork)[#](#_CPPv428hipsolverDnZZgesv_bufferSize17hipsolverHandle_tiiP16hipDoubleComplexiPiP16hipDoubleComplexiP16hipDoubleComplexiPvP6size_t)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnCCgesv_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int n, int nrhs, hipFloatComplex *A, int lda, int *devIpiv, hipFloatComplex *B, int ldb, hipFloatComplex *X, int ldx, void *work, size_t *lwork)[#](#_CPPv428hipsolverDnCCgesv_bufferSize17hipsolverHandle_tiiP15hipFloatComplexiPiP15hipFloatComplexiP15hipFloatComplexiPvP6size_t)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDDgesv_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int n, int nrhs, double *A, int lda, int *devIpiv, double *B, int ldb, double *X, int ldx, void *work, size_t *lwork)[#](#_CPPv428hipsolverDnDDgesv_bufferSize17hipsolverHandle_tiiPdiPiPdiPdiPvP6size_t)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSSgesv_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int n, int nrhs, float *A, int lda, int *devIpiv, float *B, int ldb, float *X, int ldx, void *work, size_t *lwork)[#](#_CPPv428hipsolverDnSSgesv_bufferSize17hipsolverHandle_tiiPfiPiPfiPfiPvP6size_t)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnZZgesv([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int n, int nrhs, hipDoubleComplex *A, int lda, int *devIpiv, hipDoubleComplex *B, int ldb, hipDoubleComplex *X, int ldx, void *work, size_t lwork, int *niters, int *devInfo)[#](#_CPPv417hipsolverDnZZgesv17hipsolverHandle_tiiP16hipDoubleComplexiPiP16hipDoubleComplexiP16hipDoubleComplexiPv6size_tPiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnCCgesv([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int n, int nrhs, hipFloatComplex *A, int lda, int *devIpiv, hipFloatComplex *B, int ldb, hipFloatComplex *X, int ldx, void *work, size_t lwork, int *niters, int *devInfo)[#](#_CPPv417hipsolverDnCCgesv17hipsolverHandle_tiiP15hipFloatComplexiPiP15hipFloatComplexiP15hipFloatComplexiPv6size_tPiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDDgesv([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int n, int nrhs, double *A, int lda, int *devIpiv, double *B, int ldb, double *X, int ldx, void *work, size_t lwork, int *niters, int *devInfo)[#](#_CPPv417hipsolverDnDDgesv17hipsolverHandle_tiiPdiPiPdiPdiPv6size_tPiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSSgesv([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int n, int nrhs, float *A, int lda, int *devIpiv, float *B, int ldb, float *X, int ldx, void *work, size_t lwork, int *niters, int *devInfo)[#](#_CPPv417hipsolverDnSSgesv17hipsolverHandle_tiiPfiPiPfiPfiPv6size_tPiPi)

## Least-squares solvers[#](#least-squares-solvers)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnZZgels_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int nrhs, hipDoubleComplex *A, int lda, hipDoubleComplex *B, int ldb, hipDoubleComplex *X, int ldx, void *work, size_t *lwork)[#](#_CPPv428hipsolverDnZZgels_bufferSize17hipsolverHandle_tiiiP16hipDoubleComplexiP16hipDoubleComplexiP16hipDoubleComplexiPvP6size_t)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnCCgels_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int nrhs, hipFloatComplex *A, int lda, hipFloatComplex *B, int ldb, hipFloatComplex *X, int ldx, void *work, size_t *lwork)[#](#_CPPv428hipsolverDnCCgels_bufferSize17hipsolverHandle_tiiiP15hipFloatComplexiP15hipFloatComplexiP15hipFloatComplexiPvP6size_t)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDDgels_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int nrhs, double *A, int lda, double *B, int ldb, double *X, int ldx, void *work, size_t *lwork)[#](#_CPPv428hipsolverDnDDgels_bufferSize17hipsolverHandle_tiiiPdiPdiPdiPvP6size_t)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSSgels_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int nrhs, float *A, int lda, float *B, int ldb, float *X, int ldx, void *work, size_t *lwork)[#](#_CPPv428hipsolverDnSSgels_bufferSize17hipsolverHandle_tiiiPfiPfiPfiPvP6size_t)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnZZgels([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int nrhs, hipDoubleComplex *A, int lda, hipDoubleComplex *B, int ldb, hipDoubleComplex *X, int ldx, void *work, size_t lwork, int *niters, int *devInfo)[#](#_CPPv417hipsolverDnZZgels17hipsolverHandle_tiiiP16hipDoubleComplexiP16hipDoubleComplexiP16hipDoubleComplexiPv6size_tPiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnCCgels([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int nrhs, hipFloatComplex *A, int lda, hipFloatComplex *B, int ldb, hipFloatComplex *X, int ldx, void *work, size_t lwork, int *niters, int *devInfo)[#](#_CPPv417hipsolverDnCCgels17hipsolverHandle_tiiiP15hipFloatComplexiP15hipFloatComplexiP15hipFloatComplexiPv6size_tPiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDDgels([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int nrhs, double *A, int lda, double *B, int ldb, double *X, int ldx, void *work, size_t lwork, int *niters, int *devInfo)[#](#_CPPv417hipsolverDnDDgels17hipsolverHandle_tiiiPdiPdiPdiPv6size_tPiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSSgels([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int nrhs, float *A, int lda, float *B, int ldb, float *X, int ldx, void *work, size_t lwork, int *niters, int *devInfo)[#](#_CPPv417hipsolverDnSSgels17hipsolverHandle_tiiiPfiPfiPfiPv6size_tPiPi)

## Symmetric eigensolvers[#](#symmetric-eigensolvers)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDsyevd_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](../api/types.html#_CPPv418hipsolverEigMode_t)jobz,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, const double *A, int lda, const double *W, int *lwork)[#](#_CPPv428hipsolverDnDsyevd_bufferSize17hipsolverHandle_t18hipsolverEigMode_t17hipblasFillMode_tiPKdiPKdPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSsyevd_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](../api/types.html#_CPPv418hipsolverEigMode_t)jobz,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, const float *A, int lda, const float *W, int *lwork)[#](#_CPPv428hipsolverDnSsyevd_bufferSize17hipsolverHandle_t18hipsolverEigMode_t17hipblasFillMode_tiPKfiPKfPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnZheevd_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](../api/types.html#_CPPv418hipsolverEigMode_t)jobz,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, const hipDoubleComplex *A, int lda, const double *W, int *lwork)[#](#_CPPv428hipsolverDnZheevd_bufferSize17hipsolverHandle_t18hipsolverEigMode_t17hipblasFillMode_tiPK16hipDoubleComplexiPKdPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnCheevd_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](../api/types.html#_CPPv418hipsolverEigMode_t)jobz,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, const hipFloatComplex *A, int lda, const float *W, int *lwork)[#](#_CPPv428hipsolverDnCheevd_bufferSize17hipsolverHandle_t18hipsolverEigMode_t17hipblasFillMode_tiPK15hipFloatComplexiPKfPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDsyevd([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](../api/types.html#_CPPv418hipsolverEigMode_t)jobz,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, double *A, int lda, double *W, double *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnDsyevd17hipsolverHandle_t18hipsolverEigMode_t17hipblasFillMode_tiPdiPdPdiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSsyevd([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](../api/types.html#_CPPv418hipsolverEigMode_t)jobz,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, float *A, int lda, float *W, float *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnSsyevd17hipsolverHandle_t18hipsolverEigMode_t17hipblasFillMode_tiPfiPfPfiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnZheevd([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](../api/types.html#_CPPv418hipsolverEigMode_t)jobz,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, hipDoubleComplex *A, int lda, double *W, hipDoubleComplex *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnZheevd17hipsolverHandle_t18hipsolverEigMode_t17hipblasFillMode_tiP16hipDoubleComplexiPdP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnCheevd([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](../api/types.html#_CPPv418hipsolverEigMode_t)jobz,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, hipFloatComplex *A, int lda, float *W, hipFloatComplex *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnCheevd17hipsolverHandle_t18hipsolverEigMode_t17hipblasFillMode_tiP15hipFloatComplexiPfP15hipFloatComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDsygvd_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigType_t](../api/types.html#_CPPv418hipsolverEigType_t)itype,[hipsolverEigMode_t](../api/types.html#_CPPv418hipsolverEigMode_t)jobz,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, const double *A, int lda, const double *B, int ldb, const double *W, int *lwork)[#](#_CPPv428hipsolverDnDsygvd_bufferSize17hipsolverHandle_t18hipsolverEigType_t18hipsolverEigMode_t17hipblasFillMode_tiPKdiPKdiPKdPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSsygvd_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigType_t](../api/types.html#_CPPv418hipsolverEigType_t)itype,[hipsolverEigMode_t](../api/types.html#_CPPv418hipsolverEigMode_t)jobz,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, const float *A, int lda, const float *B, int ldb, const float *W, int *lwork)[#](#_CPPv428hipsolverDnSsygvd_bufferSize17hipsolverHandle_t18hipsolverEigType_t18hipsolverEigMode_t17hipblasFillMode_tiPKfiPKfiPKfPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnZhegvd_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigType_t](../api/types.html#_CPPv418hipsolverEigType_t)itype,[hipsolverEigMode_t](../api/types.html#_CPPv418hipsolverEigMode_t)jobz,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, const hipDoubleComplex *A, int lda, const hipDoubleComplex *B, int ldb, const double *W, int *lwork)[#](#_CPPv428hipsolverDnZhegvd_bufferSize17hipsolverHandle_t18hipsolverEigType_t18hipsolverEigMode_t17hipblasFillMode_tiPK16hipDoubleComplexiPK16hipDoubleComplexiPKdPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnChegvd_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigType_t](../api/types.html#_CPPv418hipsolverEigType_t)itype,[hipsolverEigMode_t](../api/types.html#_CPPv418hipsolverEigMode_t)jobz,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, const hipFloatComplex *A, int lda, const hipFloatComplex *B, int ldb, const float *W, int *lwork)[#](#_CPPv428hipsolverDnChegvd_bufferSize17hipsolverHandle_t18hipsolverEigType_t18hipsolverEigMode_t17hipblasFillMode_tiPK15hipFloatComplexiPK15hipFloatComplexiPKfPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDsygvd([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigType_t](../api/types.html#_CPPv418hipsolverEigType_t)itype,[hipsolverEigMode_t](../api/types.html#_CPPv418hipsolverEigMode_t)jobz,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, double *A, int lda, double *B, int ldb, double *W, double *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnDsygvd17hipsolverHandle_t18hipsolverEigType_t18hipsolverEigMode_t17hipblasFillMode_tiPdiPdiPdPdiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSsygvd([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigType_t](../api/types.html#_CPPv418hipsolverEigType_t)itype,[hipsolverEigMode_t](../api/types.html#_CPPv418hipsolverEigMode_t)jobz,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, float *A, int lda, float *B, int ldb, float *W, float *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnSsygvd17hipsolverHandle_t18hipsolverEigType_t18hipsolverEigMode_t17hipblasFillMode_tiPfiPfiPfPfiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnZhegvd([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigType_t](../api/types.html#_CPPv418hipsolverEigType_t)itype,[hipsolverEigMode_t](../api/types.html#_CPPv418hipsolverEigMode_t)jobz,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, hipDoubleComplex *A, int lda, hipDoubleComplex *B, int ldb, double *W, hipDoubleComplex *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnZhegvd17hipsolverHandle_t18hipsolverEigType_t18hipsolverEigMode_t17hipblasFillMode_tiP16hipDoubleComplexiP16hipDoubleComplexiPdP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnChegvd([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigType_t](../api/types.html#_CPPv418hipsolverEigType_t)itype,[hipsolverEigMode_t](../api/types.html#_CPPv418hipsolverEigMode_t)jobz,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, hipFloatComplex *A, int lda, hipFloatComplex *B, int ldb, float *W, hipFloatComplex *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnChegvd17hipsolverHandle_t18hipsolverEigType_t18hipsolverEigMode_t17hipblasFillMode_tiP15hipFloatComplexiP15hipFloatComplexiPfP15hipFloatComplexiPi)

## Singular value decomposition[#](#singular-value-decomposition)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnZgesvd_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int *lwork)[#](#_CPPv428hipsolverDnZgesvd_bufferSize17hipsolverHandle_tiiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnCgesvd_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int *lwork)[#](#_CPPv428hipsolverDnCgesvd_bufferSize17hipsolverHandle_tiiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDgesvd_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int *lwork)[#](#_CPPv428hipsolverDnDgesvd_bufferSize17hipsolverHandle_tiiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSgesvd_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int *lwork)[#](#_CPPv428hipsolverDnSgesvd_bufferSize17hipsolverHandle_tiiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnZgesvd([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, signed char jobu, signed char jobv, int m, int n, hipDoubleComplex *A, int lda, double *S, hipDoubleComplex *U, int ldu, hipDoubleComplex *V, int ldv, hipDoubleComplex *work, int lwork, double *rwork, int *devInfo)[#](#_CPPv417hipsolverDnZgesvd17hipsolverHandle_taaiiP16hipDoubleComplexiPdP16hipDoubleComplexiP16hipDoubleComplexiP16hipDoubleComplexiPdPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnCgesvd([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, signed char jobu, signed char jobv, int m, int n, hipFloatComplex *A, int lda, float *S, hipFloatComplex *U, int ldu, hipFloatComplex *V, int ldv, hipFloatComplex *work, int lwork, float *rwork, int *devInfo)[#](#_CPPv417hipsolverDnCgesvd17hipsolverHandle_taaiiP15hipFloatComplexiPfP15hipFloatComplexiP15hipFloatComplexiP15hipFloatComplexiPfPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDgesvd([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, signed char jobu, signed char jobv, int m, int n, double *A, int lda, double *S, double *U, int ldu, double *V, int ldv, double *work, int lwork, double *rwork, int *devInfo)[#](#_CPPv417hipsolverDnDgesvd17hipsolverHandle_taaiiPdiPdPdiPdiPdiPdPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSgesvd([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, signed char jobu, signed char jobv, int m, int n, float *A, int lda, float *S, float *U, int ldu, float *V, int ldv, float *work, int lwork, float *rwork, int *devInfo)[#](#_CPPv417hipsolverDnSgesvd17hipsolverHandle_taaiiPfiPfPfiPfiPfiPfPi)
