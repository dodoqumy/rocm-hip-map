---
title: "hipSOLVER LAPACK auxiliary functions &#8212; hipSOLVER 3.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/auxiliary.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:21:09.490709+00:00
content_hash: "c94bb8978796aad6"
---

# hipSOLVER LAPACK auxiliary functions[#](#hipsolver-lapack-auxiliary-functions)

These functions support more [advanced LAPACK routines](lapack.html#lapackfunc).
The auxiliary functions are divided into the following categories:

[Orthonormal matrices](#orthonormal): Generation and application of orthonormal matrices.[Unitary matrices](#unitary): Generation and application of unitary matrices.

## Orthonormal matrices[#](#orthonormal-matrices)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDorgbr_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverSideMode_t](types.html#_CPPv419hipsolverSideMode_t)side, int m, int n, int k, double *A, int lda, double *tau, int *lwork)[#](#_CPPv426hipsolverDorgbr_bufferSize17hipsolverHandle_t19hipsolverSideMode_tiiiPdiPdPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSorgbr_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverSideMode_t](types.html#_CPPv419hipsolverSideMode_t)side, int m, int n, int k, float *A, int lda, float *tau, int *lwork)[#](#_CPPv426hipsolverSorgbr_bufferSize17hipsolverHandle_t19hipsolverSideMode_tiiiPfiPfPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDorgbr([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverSideMode_t](types.html#_CPPv419hipsolverSideMode_t)side, int m, int n, int k, double *A, int lda, double *tau, double *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverDorgbr17hipsolverHandle_t19hipsolverSideMode_tiiiPdiPdPdiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSorgbr([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverSideMode_t](types.html#_CPPv419hipsolverSideMode_t)side, int m, int n, int k, float *A, int lda, float *tau, float *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverSorgbr17hipsolverHandle_t19hipsolverSideMode_tiiiPfiPfPfiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDorgqr_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int k, double *A, int lda, double *tau, int *lwork)[#](#_CPPv426hipsolverDorgqr_bufferSize17hipsolverHandle_tiiiPdiPdPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSorgqr_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int k, float *A, int lda, float *tau, int *lwork)[#](#_CPPv426hipsolverSorgqr_bufferSize17hipsolverHandle_tiiiPfiPfPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDorgqr([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int k, double *A, int lda, double *tau, double *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverDorgqr17hipsolverHandle_tiiiPdiPdPdiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSorgqr([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int k, float *A, int lda, float *tau, float *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverSorgqr17hipsolverHandle_tiiiPfiPfPfiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDorgtr_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, double *A, int lda, double *tau, int *lwork)[#](#_CPPv426hipsolverDorgtr_bufferSize17hipsolverHandle_t19hipsolverFillMode_tiPdiPdPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSorgtr_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, float *A, int lda, float *tau, int *lwork)[#](#_CPPv426hipsolverSorgtr_bufferSize17hipsolverHandle_t19hipsolverFillMode_tiPfiPfPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDorgtr([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, double *A, int lda, double *tau, double *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverDorgtr17hipsolverHandle_t19hipsolverFillMode_tiPdiPdPdiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSorgtr([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, float *A, int lda, float *tau, float *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverSorgtr17hipsolverHandle_t19hipsolverFillMode_tiPfiPfPfiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDormqr_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverSideMode_t](types.html#_CPPv419hipsolverSideMode_t)side,[hipsolverOperation_t](types.html#_CPPv420hipsolverOperation_t)trans, int m, int n, int k, double *A, int lda, double *tau, double *C, int ldc, int *lwork)[#](#_CPPv426hipsolverDormqr_bufferSize17hipsolverHandle_t19hipsolverSideMode_t20hipsolverOperation_tiiiPdiPdPdiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSormqr_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverSideMode_t](types.html#_CPPv419hipsolverSideMode_t)side,[hipsolverOperation_t](types.html#_CPPv420hipsolverOperation_t)trans, int m, int n, int k, float *A, int lda, float *tau, float *C, int ldc, int *lwork)[#](#_CPPv426hipsolverSormqr_bufferSize17hipsolverHandle_t19hipsolverSideMode_t20hipsolverOperation_tiiiPfiPfPfiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDormqr([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverSideMode_t](types.html#_CPPv419hipsolverSideMode_t)side,[hipsolverOperation_t](types.html#_CPPv420hipsolverOperation_t)trans, int m, int n, int k, double *A, int lda, double *tau, double *C, int ldc, double *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverDormqr17hipsolverHandle_t19hipsolverSideMode_t20hipsolverOperation_tiiiPdiPdPdiPdiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSormqr([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverSideMode_t](types.html#_CPPv419hipsolverSideMode_t)side,[hipsolverOperation_t](types.html#_CPPv420hipsolverOperation_t)trans, int m, int n, int k, float *A, int lda, float *tau, float *C, int ldc, float *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverSormqr17hipsolverHandle_t19hipsolverSideMode_t20hipsolverOperation_tiiiPfiPfPfiPfiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDormtr_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverSideMode_t](types.html#_CPPv419hipsolverSideMode_t)side,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo,[hipsolverOperation_t](types.html#_CPPv420hipsolverOperation_t)trans, int m, int n, double *A, int lda, double *tau, double *C, int ldc, int *lwork)[#](#_CPPv426hipsolverDormtr_bufferSize17hipsolverHandle_t19hipsolverSideMode_t19hipsolverFillMode_t20hipsolverOperation_tiiPdiPdPdiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSormtr_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverSideMode_t](types.html#_CPPv419hipsolverSideMode_t)side,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo,[hipsolverOperation_t](types.html#_CPPv420hipsolverOperation_t)trans, int m, int n, float *A, int lda, float *tau, float *C, int ldc, int *lwork)[#](#_CPPv426hipsolverSormtr_bufferSize17hipsolverHandle_t19hipsolverSideMode_t19hipsolverFillMode_t20hipsolverOperation_tiiPfiPfPfiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDormtr([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverSideMode_t](types.html#_CPPv419hipsolverSideMode_t)side,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo,[hipsolverOperation_t](types.html#_CPPv420hipsolverOperation_t)trans, int m, int n, double *A, int lda, double *tau, double *C, int ldc, double *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverDormtr17hipsolverHandle_t19hipsolverSideMode_t19hipsolverFillMode_t20hipsolverOperation_tiiPdiPdPdiPdiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSormtr([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverSideMode_t](types.html#_CPPv419hipsolverSideMode_t)side,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo,[hipsolverOperation_t](types.html#_CPPv420hipsolverOperation_t)trans, int m, int n, float *A, int lda, float *tau, float *C, int ldc, float *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverSormtr17hipsolverHandle_t19hipsolverSideMode_t19hipsolverFillMode_t20hipsolverOperation_tiiPfiPfPfiPfiPi)

## Unitary matrices[#](#unitary-matrices)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZungbr_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverSideMode_t](types.html#_CPPv419hipsolverSideMode_t)side, int m, int n, int k, hipDoubleComplex *A, int lda, hipDoubleComplex *tau, int *lwork)[#](#_CPPv426hipsolverZungbr_bufferSize17hipsolverHandle_t19hipsolverSideMode_tiiiP16hipDoubleComplexiP16hipDoubleComplexPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCungbr_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverSideMode_t](types.html#_CPPv419hipsolverSideMode_t)side, int m, int n, int k, hipFloatComplex *A, int lda, hipFloatComplex *tau, int *lwork)[#](#_CPPv426hipsolverCungbr_bufferSize17hipsolverHandle_t19hipsolverSideMode_tiiiP15hipFloatComplexiP15hipFloatComplexPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZungbr([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverSideMode_t](types.html#_CPPv419hipsolverSideMode_t)side, int m, int n, int k, hipDoubleComplex *A, int lda, hipDoubleComplex *tau, hipDoubleComplex *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverZungbr17hipsolverHandle_t19hipsolverSideMode_tiiiP16hipDoubleComplexiP16hipDoubleComplexP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCungbr([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverSideMode_t](types.html#_CPPv419hipsolverSideMode_t)side, int m, int n, int k, hipFloatComplex *A, int lda, hipFloatComplex *tau, hipFloatComplex *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverCungbr17hipsolverHandle_t19hipsolverSideMode_tiiiP15hipFloatComplexiP15hipFloatComplexP15hipFloatComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZungqr_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int k, hipDoubleComplex *A, int lda, hipDoubleComplex *tau, int *lwork)[#](#_CPPv426hipsolverZungqr_bufferSize17hipsolverHandle_tiiiP16hipDoubleComplexiP16hipDoubleComplexPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCungqr_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int k, hipFloatComplex *A, int lda, hipFloatComplex *tau, int *lwork)[#](#_CPPv426hipsolverCungqr_bufferSize17hipsolverHandle_tiiiP15hipFloatComplexiP15hipFloatComplexPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZungqr([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int k, hipDoubleComplex *A, int lda, hipDoubleComplex *tau, hipDoubleComplex *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverZungqr17hipsolverHandle_tiiiP16hipDoubleComplexiP16hipDoubleComplexP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCungqr([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int k, hipFloatComplex *A, int lda, hipFloatComplex *tau, hipFloatComplex *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverCungqr17hipsolverHandle_tiiiP15hipFloatComplexiP15hipFloatComplexP15hipFloatComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZungtr_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipDoubleComplex *A, int lda, hipDoubleComplex *tau, int *lwork)[#](#_CPPv426hipsolverZungtr_bufferSize17hipsolverHandle_t19hipsolverFillMode_tiP16hipDoubleComplexiP16hipDoubleComplexPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCungtr_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipFloatComplex *A, int lda, hipFloatComplex *tau, int *lwork)[#](#_CPPv426hipsolverCungtr_bufferSize17hipsolverHandle_t19hipsolverFillMode_tiP15hipFloatComplexiP15hipFloatComplexPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZungtr([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipDoubleComplex *A, int lda, hipDoubleComplex *tau, hipDoubleComplex *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverZungtr17hipsolverHandle_t19hipsolverFillMode_tiP16hipDoubleComplexiP16hipDoubleComplexP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCungtr([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipFloatComplex *A, int lda, hipFloatComplex *tau, hipFloatComplex *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverCungtr17hipsolverHandle_t19hipsolverFillMode_tiP15hipFloatComplexiP15hipFloatComplexP15hipFloatComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZunmqr_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverSideMode_t](types.html#_CPPv419hipsolverSideMode_t)side,[hipsolverOperation_t](types.html#_CPPv420hipsolverOperation_t)trans, int m, int n, int k, hipDoubleComplex *A, int lda, hipDoubleComplex *tau, hipDoubleComplex *C, int ldc, int *lwork)[#](#_CPPv426hipsolverZunmqr_bufferSize17hipsolverHandle_t19hipsolverSideMode_t20hipsolverOperation_tiiiP16hipDoubleComplexiP16hipDoubleComplexP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCunmqr_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverSideMode_t](types.html#_CPPv419hipsolverSideMode_t)side,[hipsolverOperation_t](types.html#_CPPv420hipsolverOperation_t)trans, int m, int n, int k, hipFloatComplex *A, int lda, hipFloatComplex *tau, hipFloatComplex *C, int ldc, int *lwork)[#](#_CPPv426hipsolverCunmqr_bufferSize17hipsolverHandle_t19hipsolverSideMode_t20hipsolverOperation_tiiiP15hipFloatComplexiP15hipFloatComplexP15hipFloatComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZunmqr([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverSideMode_t](types.html#_CPPv419hipsolverSideMode_t)side,[hipsolverOperation_t](types.html#_CPPv420hipsolverOperation_t)trans, int m, int n, int k, hipDoubleComplex *A, int lda, hipDoubleComplex *tau, hipDoubleComplex *C, int ldc, hipDoubleComplex *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverZunmqr17hipsolverHandle_t19hipsolverSideMode_t20hipsolverOperation_tiiiP16hipDoubleComplexiP16hipDoubleComplexP16hipDoubleComplexiP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCunmqr([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverSideMode_t](types.html#_CPPv419hipsolverSideMode_t)side,[hipsolverOperation_t](types.html#_CPPv420hipsolverOperation_t)trans, int m, int n, int k, hipFloatComplex *A, int lda, hipFloatComplex *tau, hipFloatComplex *C, int ldc, hipFloatComplex *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverCunmqr17hipsolverHandle_t19hipsolverSideMode_t20hipsolverOperation_tiiiP15hipFloatComplexiP15hipFloatComplexP15hipFloatComplexiP15hipFloatComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZunmtr_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverSideMode_t](types.html#_CPPv419hipsolverSideMode_t)side,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo,[hipsolverOperation_t](types.html#_CPPv420hipsolverOperation_t)trans, int m, int n, hipDoubleComplex *A, int lda, hipDoubleComplex *tau, hipDoubleComplex *C, int ldc, int *lwork)[#](#_CPPv426hipsolverZunmtr_bufferSize17hipsolverHandle_t19hipsolverSideMode_t19hipsolverFillMode_t20hipsolverOperation_tiiP16hipDoubleComplexiP16hipDoubleComplexP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCunmtr_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverSideMode_t](types.html#_CPPv419hipsolverSideMode_t)side,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo,[hipsolverOperation_t](types.html#_CPPv420hipsolverOperation_t)trans, int m, int n, hipFloatComplex *A, int lda, hipFloatComplex *tau, hipFloatComplex *C, int ldc, int *lwork)[#](#_CPPv426hipsolverCunmtr_bufferSize17hipsolverHandle_t19hipsolverSideMode_t19hipsolverFillMode_t20hipsolverOperation_tiiP15hipFloatComplexiP15hipFloatComplexP15hipFloatComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZunmtr([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverSideMode_t](types.html#_CPPv419hipsolverSideMode_t)side,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo,[hipsolverOperation_t](types.html#_CPPv420hipsolverOperation_t)trans, int m, int n, hipDoubleComplex *A, int lda, hipDoubleComplex *tau, hipDoubleComplex *C, int ldc, hipDoubleComplex *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverZunmtr17hipsolverHandle_t19hipsolverSideMode_t19hipsolverFillMode_t20hipsolverOperation_tiiP16hipDoubleComplexiP16hipDoubleComplexP16hipDoubleComplexiP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCunmtr([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverSideMode_t](types.html#_CPPv419hipsolverSideMode_t)side,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo,[hipsolverOperation_t](types.html#_CPPv420hipsolverOperation_t)trans, int m, int n, hipFloatComplex *A, int lda, hipFloatComplex *tau, hipFloatComplex *C, int ldc, hipFloatComplex *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverCunmtr17hipsolverHandle_t19hipsolverSideMode_t19hipsolverFillMode_t20hipsolverOperation_tiiP15hipFloatComplexiP15hipFloatComplexP15hipFloatComplexiP15hipFloatComplexiPi)
