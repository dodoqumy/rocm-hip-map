---
title: "Dense matrix LAPACK auxiliary functions &#8212; hipSOLVER 3.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/dense-api/auxiliary.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T18:06:22.230163+00:00
content_hash: "6f809babfee81d98"
---

# Dense matrix LAPACK auxiliary functions[#](#dense-matrix-lapack-auxiliary-functions)

These functions support more [advanced LAPACK routines](lapack.html#dense-lapackfunc).
The auxiliary functions are divided into the following categories:

[Orthonormal matrices](#dense-orthonormal): Generation and application of orthonormal matrices.[Unitary matrices](#dense-unitary): Generation and application of unitary matrices.

## Orthonormal matrices[#](#orthonormal-matrices)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDorgbr_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasSideMode_t](../api/types.html#_CPPv417hipblasSideMode_t)side, int m, int n, int k, const double *A, int lda, const double *tau, int *lwork)[#](#_CPPv428hipsolverDnDorgbr_bufferSize17hipsolverHandle_t17hipblasSideMode_tiiiPKdiPKdPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSorgbr_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasSideMode_t](../api/types.html#_CPPv417hipblasSideMode_t)side, int m, int n, int k, const float *A, int lda, const float *tau, int *lwork)[#](#_CPPv428hipsolverDnSorgbr_bufferSize17hipsolverHandle_t17hipblasSideMode_tiiiPKfiPKfPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDorgbr([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasSideMode_t](../api/types.html#_CPPv417hipblasSideMode_t)side, int m, int n, int k, double *A, int lda, const double *tau, double *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnDorgbr17hipsolverHandle_t17hipblasSideMode_tiiiPdiPKdPdiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSorgbr([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasSideMode_t](../api/types.html#_CPPv417hipblasSideMode_t)side, int m, int n, int k, float *A, int lda, const float *tau, float *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnSorgbr17hipsolverHandle_t17hipblasSideMode_tiiiPfiPKfPfiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDorgqr_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int k, const double *A, int lda, const double *tau, int *lwork)[#](#_CPPv428hipsolverDnDorgqr_bufferSize17hipsolverHandle_tiiiPKdiPKdPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSorgqr_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int k, const float *A, int lda, const float *tau, int *lwork)[#](#_CPPv428hipsolverDnSorgqr_bufferSize17hipsolverHandle_tiiiPKfiPKfPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDorgqr([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int k, double *A, int lda, const double *tau, double *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnDorgqr17hipsolverHandle_tiiiPdiPKdPdiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSorgqr([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int k, float *A, int lda, const float *tau, float *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnSorgqr17hipsolverHandle_tiiiPfiPKfPfiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDorgtr_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, const double *A, int lda, const double *tau, int *lwork)[#](#_CPPv428hipsolverDnDorgtr_bufferSize17hipsolverHandle_t17hipblasFillMode_tiPKdiPKdPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSorgtr_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, const float *A, int lda, const float *tau, int *lwork)[#](#_CPPv428hipsolverDnSorgtr_bufferSize17hipsolverHandle_t17hipblasFillMode_tiPKfiPKfPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDorgtr([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, double *A, int lda, const double *tau, double *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnDorgtr17hipsolverHandle_t17hipblasFillMode_tiPdiPKdPdiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSorgtr([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, float *A, int lda, const float *tau, float *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnSorgtr17hipsolverHandle_t17hipblasFillMode_tiPfiPKfPfiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDormqr_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasSideMode_t](../api/types.html#_CPPv417hipblasSideMode_t)side,[hipblasOperation_t](../api/types.html#_CPPv418hipblasOperation_t)trans, int m, int n, int k, const double *A, int lda, const double *tau, const double *C, int ldc, int *lwork)[#](#_CPPv428hipsolverDnDormqr_bufferSize17hipsolverHandle_t17hipblasSideMode_t18hipblasOperation_tiiiPKdiPKdPKdiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSormqr_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasSideMode_t](../api/types.html#_CPPv417hipblasSideMode_t)side,[hipblasOperation_t](../api/types.html#_CPPv418hipblasOperation_t)trans, int m, int n, int k, const float *A, int lda, const float *tau, const float *C, int ldc, int *lwork)[#](#_CPPv428hipsolverDnSormqr_bufferSize17hipsolverHandle_t17hipblasSideMode_t18hipblasOperation_tiiiPKfiPKfPKfiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDormqr([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasSideMode_t](../api/types.html#_CPPv417hipblasSideMode_t)side,[hipblasOperation_t](../api/types.html#_CPPv418hipblasOperation_t)trans, int m, int n, int k, const double *A, int lda, const double *tau, double *C, int ldc, double *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnDormqr17hipsolverHandle_t17hipblasSideMode_t18hipblasOperation_tiiiPKdiPKdPdiPdiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSormqr([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasSideMode_t](../api/types.html#_CPPv417hipblasSideMode_t)side,[hipblasOperation_t](../api/types.html#_CPPv418hipblasOperation_t)trans, int m, int n, int k, const float *A, int lda, const float *tau, float *C, int ldc, float *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnSormqr17hipsolverHandle_t17hipblasSideMode_t18hipblasOperation_tiiiPKfiPKfPfiPfiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDormtr_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasSideMode_t](../api/types.html#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](../api/types.html#_CPPv418hipblasOperation_t)trans, int m, int n, const double *A, int lda, const double *tau, const double *C, int ldc, int *lwork)[#](#_CPPv428hipsolverDnDormtr_bufferSize17hipsolverHandle_t17hipblasSideMode_t17hipblasFillMode_t18hipblasOperation_tiiPKdiPKdPKdiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSormtr_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasSideMode_t](../api/types.html#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](../api/types.html#_CPPv418hipblasOperation_t)trans, int m, int n, const float *A, int lda, const float *tau, const float *C, int ldc, int *lwork)[#](#_CPPv428hipsolverDnSormtr_bufferSize17hipsolverHandle_t17hipblasSideMode_t17hipblasFillMode_t18hipblasOperation_tiiPKfiPKfPKfiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDormtr([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasSideMode_t](../api/types.html#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](../api/types.html#_CPPv418hipblasOperation_t)trans, int m, int n, double *A, int lda, double *tau, double *C, int ldc, double *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnDormtr17hipsolverHandle_t17hipblasSideMode_t17hipblasFillMode_t18hipblasOperation_tiiPdiPdPdiPdiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSormtr([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasSideMode_t](../api/types.html#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](../api/types.html#_CPPv418hipblasOperation_t)trans, int m, int n, float *A, int lda, float *tau, float *C, int ldc, float *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnSormtr17hipsolverHandle_t17hipblasSideMode_t17hipblasFillMode_t18hipblasOperation_tiiPfiPfPfiPfiPi)

## Unitary matrices[#](#unitary-matrices)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnZungbr_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasSideMode_t](../api/types.html#_CPPv417hipblasSideMode_t)side, int m, int n, int k, const hipDoubleComplex *A, int lda, const hipDoubleComplex *tau, int *lwork)[#](#_CPPv428hipsolverDnZungbr_bufferSize17hipsolverHandle_t17hipblasSideMode_tiiiPK16hipDoubleComplexiPK16hipDoubleComplexPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnCungbr_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasSideMode_t](../api/types.html#_CPPv417hipblasSideMode_t)side, int m, int n, int k, const hipFloatComplex *A, int lda, const hipFloatComplex *tau, int *lwork)[#](#_CPPv428hipsolverDnCungbr_bufferSize17hipsolverHandle_t17hipblasSideMode_tiiiPK15hipFloatComplexiPK15hipFloatComplexPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnZungbr([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasSideMode_t](../api/types.html#_CPPv417hipblasSideMode_t)side, int m, int n, int k, hipDoubleComplex *A, int lda, const hipDoubleComplex *tau, hipDoubleComplex *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnZungbr17hipsolverHandle_t17hipblasSideMode_tiiiP16hipDoubleComplexiPK16hipDoubleComplexP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnCungbr([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasSideMode_t](../api/types.html#_CPPv417hipblasSideMode_t)side, int m, int n, int k, hipFloatComplex *A, int lda, const hipFloatComplex *tau, hipFloatComplex *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnCungbr17hipsolverHandle_t17hipblasSideMode_tiiiP15hipFloatComplexiPK15hipFloatComplexP15hipFloatComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnZungqr_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int k, const hipDoubleComplex *A, int lda, const hipDoubleComplex *tau, int *lwork)[#](#_CPPv428hipsolverDnZungqr_bufferSize17hipsolverHandle_tiiiPK16hipDoubleComplexiPK16hipDoubleComplexPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnCungqr_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int k, const hipFloatComplex *A, int lda, const hipFloatComplex *tau, int *lwork)[#](#_CPPv428hipsolverDnCungqr_bufferSize17hipsolverHandle_tiiiPK15hipFloatComplexiPK15hipFloatComplexPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnZungqr([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int k, hipDoubleComplex *A, int lda, const hipDoubleComplex *tau, hipDoubleComplex *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnZungqr17hipsolverHandle_tiiiP16hipDoubleComplexiPK16hipDoubleComplexP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnCungqr([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int k, hipFloatComplex *A, int lda, const hipFloatComplex *tau, hipFloatComplex *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnCungqr17hipsolverHandle_tiiiP15hipFloatComplexiPK15hipFloatComplexP15hipFloatComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnZungtr_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, const hipDoubleComplex *A, int lda, const hipDoubleComplex *tau, int *lwork)[#](#_CPPv428hipsolverDnZungtr_bufferSize17hipsolverHandle_t17hipblasFillMode_tiPK16hipDoubleComplexiPK16hipDoubleComplexPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnCungtr_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, const hipFloatComplex *A, int lda, const hipFloatComplex *tau, int *lwork)[#](#_CPPv428hipsolverDnCungtr_bufferSize17hipsolverHandle_t17hipblasFillMode_tiPK15hipFloatComplexiPK15hipFloatComplexPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnZungtr([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, hipDoubleComplex *A, int lda, const hipDoubleComplex *tau, hipDoubleComplex *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnZungtr17hipsolverHandle_t17hipblasFillMode_tiP16hipDoubleComplexiPK16hipDoubleComplexP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnCungtr([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo, int n, hipFloatComplex *A, int lda, const hipFloatComplex *tau, hipFloatComplex *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnCungtr17hipsolverHandle_t17hipblasFillMode_tiP15hipFloatComplexiPK15hipFloatComplexP15hipFloatComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnZunmqr_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasSideMode_t](../api/types.html#_CPPv417hipblasSideMode_t)side,[hipblasOperation_t](../api/types.html#_CPPv418hipblasOperation_t)trans, int m, int n, int k, const hipDoubleComplex *A, int lda, const hipDoubleComplex *tau, const hipDoubleComplex *C, int ldc, int *lwork)[#](#_CPPv428hipsolverDnZunmqr_bufferSize17hipsolverHandle_t17hipblasSideMode_t18hipblasOperation_tiiiPK16hipDoubleComplexiPK16hipDoubleComplexPK16hipDoubleComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnCunmqr_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasSideMode_t](../api/types.html#_CPPv417hipblasSideMode_t)side,[hipblasOperation_t](../api/types.html#_CPPv418hipblasOperation_t)trans, int m, int n, int k, const hipFloatComplex *A, int lda, const hipFloatComplex *tau, const hipFloatComplex *C, int ldc, int *lwork)[#](#_CPPv428hipsolverDnCunmqr_bufferSize17hipsolverHandle_t17hipblasSideMode_t18hipblasOperation_tiiiPK15hipFloatComplexiPK15hipFloatComplexPK15hipFloatComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnZunmqr([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasSideMode_t](../api/types.html#_CPPv417hipblasSideMode_t)side,[hipblasOperation_t](../api/types.html#_CPPv418hipblasOperation_t)trans, int m, int n, int k, const hipDoubleComplex *A, int lda, const hipDoubleComplex *tau, hipDoubleComplex *C, int ldc, hipDoubleComplex *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnZunmqr17hipsolverHandle_t17hipblasSideMode_t18hipblasOperation_tiiiPK16hipDoubleComplexiPK16hipDoubleComplexP16hipDoubleComplexiP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnCunmqr([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasSideMode_t](../api/types.html#_CPPv417hipblasSideMode_t)side,[hipblasOperation_t](../api/types.html#_CPPv418hipblasOperation_t)trans, int m, int n, int k, const hipFloatComplex *A, int lda, const hipFloatComplex *tau, hipFloatComplex *C, int ldc, hipFloatComplex *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnCunmqr17hipsolverHandle_t17hipblasSideMode_t18hipblasOperation_tiiiPK15hipFloatComplexiPK15hipFloatComplexP15hipFloatComplexiP15hipFloatComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnZunmtr_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasSideMode_t](../api/types.html#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](../api/types.html#_CPPv418hipblasOperation_t)trans, int m, int n, const hipDoubleComplex *A, int lda, const hipDoubleComplex *tau, const hipDoubleComplex *C, int ldc, int *lwork)[#](#_CPPv428hipsolverDnZunmtr_bufferSize17hipsolverHandle_t17hipblasSideMode_t17hipblasFillMode_t18hipblasOperation_tiiPK16hipDoubleComplexiPK16hipDoubleComplexPK16hipDoubleComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnCunmtr_bufferSize([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasSideMode_t](../api/types.html#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](../api/types.html#_CPPv418hipblasOperation_t)trans, int m, int n, const hipFloatComplex *A, int lda, const hipFloatComplex *tau, const hipFloatComplex *C, int ldc, int *lwork)[#](#_CPPv428hipsolverDnCunmtr_bufferSize17hipsolverHandle_t17hipblasSideMode_t17hipblasFillMode_t18hipblasOperation_tiiPK15hipFloatComplexiPK15hipFloatComplexPK15hipFloatComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnZunmtr([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasSideMode_t](../api/types.html#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](../api/types.html#_CPPv418hipblasOperation_t)trans, int m, int n, hipDoubleComplex *A, int lda, hipDoubleComplex *tau, hipDoubleComplex *C, int ldc, hipDoubleComplex *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnZunmtr17hipsolverHandle_t17hipblasSideMode_t17hipblasFillMode_t18hipblasOperation_tiiP16hipDoubleComplexiP16hipDoubleComplexP16hipDoubleComplexiP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnCunmtr([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipblasSideMode_t](../api/types.html#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](../api/types.html#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](../api/types.html#_CPPv418hipblasOperation_t)trans, int m, int n, hipFloatComplex *A, int lda, hipFloatComplex *tau, hipFloatComplex *C, int ldc, hipFloatComplex *work, int lwork, int *devInfo)[#](#_CPPv417hipsolverDnCunmtr17hipsolverHandle_t17hipblasSideMode_t17hipblasFillMode_t18hipblasOperation_tiiP15hipFloatComplexiP15hipFloatComplexP15hipFloatComplexiP15hipFloatComplexiPi)
