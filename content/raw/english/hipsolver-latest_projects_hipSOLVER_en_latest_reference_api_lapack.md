---
title: "hipSOLVER LAPACK functions &#8212; hipSOLVER 3.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/lapack.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:20:45.177016+00:00
content_hash: "9f3bf653a93d6519"
---

# hipSOLVER LAPACK functions[#](#hipsolver-lapack-functions)

LAPACK routines solve complex numerical linear algebra problems. These functions are organized into the following categories:

[Triangular factorizations](#triangular): Based on Gaussian elimination.[Orthogonal factorizations](#orthogonal): Based on Householder reflections.[Problem and matrix reductions](#reductions): Transformation of matrices and problems into equivalent forms.[Linear-systems solvers](#linears): Based on triangular factorizations.[Least-squares solvers](#leastsqr): Based on orthogonal factorizations.[Symmetric eigensolvers](#eigens): Eigenproblems for symmetric matrices.[Singular value decomposition](#svds): Singular values and related problems for general matrices.

## Triangular factorizations[#](#triangular-factorizations)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZpotrf_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipDoubleComplex *A, int lda, int *lwork)[#](#_CPPv426hipsolverZpotrf_bufferSize17hipsolverHandle_t19hipsolverFillMode_tiP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCpotrf_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipFloatComplex *A, int lda, int *lwork)[#](#_CPPv426hipsolverCpotrf_bufferSize17hipsolverHandle_t19hipsolverFillMode_tiP15hipFloatComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDpotrf_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, double *A, int lda, int *lwork)[#](#_CPPv426hipsolverDpotrf_bufferSize17hipsolverHandle_t19hipsolverFillMode_tiPdiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSpotrf_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, float *A, int lda, int *lwork)[#](#_CPPv426hipsolverSpotrf_bufferSize17hipsolverHandle_t19hipsolverFillMode_tiPfiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZpotrfBatched_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipDoubleComplex *A[], int lda, int *lwork, int batch_count)[#](#_CPPv433hipsolverZpotrfBatched_bufferSize17hipsolverHandle_t19hipsolverFillMode_tiA_P16hipDoubleComplexiPii)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCpotrfBatched_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipFloatComplex *A[], int lda, int *lwork, int batch_count)[#](#_CPPv433hipsolverCpotrfBatched_bufferSize17hipsolverHandle_t19hipsolverFillMode_tiA_P15hipFloatComplexiPii)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDpotrfBatched_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, double *A[], int lda, int *lwork, int batch_count)[#](#_CPPv433hipsolverDpotrfBatched_bufferSize17hipsolverHandle_t19hipsolverFillMode_tiA_PdiPii)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSpotrfBatched_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, float *A[], int lda, int *lwork, int batch_count)[#](#_CPPv433hipsolverSpotrfBatched_bufferSize17hipsolverHandle_t19hipsolverFillMode_tiA_PfiPii)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZpotrf([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipDoubleComplex *A, int lda, hipDoubleComplex *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverZpotrf17hipsolverHandle_t19hipsolverFillMode_tiP16hipDoubleComplexiP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCpotrf([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipFloatComplex *A, int lda, hipFloatComplex *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverCpotrf17hipsolverHandle_t19hipsolverFillMode_tiP15hipFloatComplexiP15hipFloatComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDpotrf([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, double *A, int lda, double *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverDpotrf17hipsolverHandle_t19hipsolverFillMode_tiPdiPdiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSpotrf([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, float *A, int lda, float *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverSpotrf17hipsolverHandle_t19hipsolverFillMode_tiPfiPfiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZpotrfBatched([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipDoubleComplex *A[], int lda, hipDoubleComplex *work, int lwork, int *devInfo, int batch_count)[#](#_CPPv422hipsolverZpotrfBatched17hipsolverHandle_t19hipsolverFillMode_tiA_P16hipDoubleComplexiP16hipDoubleComplexiPii)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCpotrfBatched([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipFloatComplex *A[], int lda, hipFloatComplex *work, int lwork, int *devInfo, int batch_count)[#](#_CPPv422hipsolverCpotrfBatched17hipsolverHandle_t19hipsolverFillMode_tiA_P15hipFloatComplexiP15hipFloatComplexiPii)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDpotrfBatched([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, double *A[], int lda, double *work, int lwork, int *devInfo, int batch_count)[#](#_CPPv422hipsolverDpotrfBatched17hipsolverHandle_t19hipsolverFillMode_tiA_PdiPdiPii)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSpotrfBatched([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, float *A[], int lda, float *work, int lwork, int *devInfo, int batch_count)[#](#_CPPv422hipsolverSpotrfBatched17hipsolverHandle_t19hipsolverFillMode_tiA_PfiPfiPii)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZgetrf_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, hipDoubleComplex *A, int lda, int *lwork)[#](#_CPPv426hipsolverZgetrf_bufferSize17hipsolverHandle_tiiP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCgetrf_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, hipFloatComplex *A, int lda, int *lwork)[#](#_CPPv426hipsolverCgetrf_bufferSize17hipsolverHandle_tiiP15hipFloatComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDgetrf_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, double *A, int lda, int *lwork)[#](#_CPPv426hipsolverDgetrf_bufferSize17hipsolverHandle_tiiPdiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSgetrf_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, float *A, int lda, int *lwork)[#](#_CPPv426hipsolverSgetrf_bufferSize17hipsolverHandle_tiiPfiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZgetrf([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, hipDoubleComplex *A, int lda, hipDoubleComplex *work, int lwork, int *devIpiv, int *devInfo)[#](#_CPPv415hipsolverZgetrf17hipsolverHandle_tiiP16hipDoubleComplexiP16hipDoubleComplexiPiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCgetrf([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, hipFloatComplex *A, int lda, hipFloatComplex *work, int lwork, int *devIpiv, int *devInfo)[#](#_CPPv415hipsolverCgetrf17hipsolverHandle_tiiP15hipFloatComplexiP15hipFloatComplexiPiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDgetrf([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, double *A, int lda, double *work, int lwork, int *devIpiv, int *devInfo)[#](#_CPPv415hipsolverDgetrf17hipsolverHandle_tiiPdiPdiPiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSgetrf([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, float *A, int lda, float *work, int lwork, int *devIpiv, int *devInfo)[#](#_CPPv415hipsolverSgetrf17hipsolverHandle_tiiPfiPfiPiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZsytrf_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int n, hipDoubleComplex *A, int lda, int *lwork)[#](#_CPPv426hipsolverZsytrf_bufferSize17hipsolverHandle_tiP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCsytrf_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int n, hipFloatComplex *A, int lda, int *lwork)[#](#_CPPv426hipsolverCsytrf_bufferSize17hipsolverHandle_tiP15hipFloatComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDsytrf_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int n, double *A, int lda, int *lwork)[#](#_CPPv426hipsolverDsytrf_bufferSize17hipsolverHandle_tiPdiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSsytrf_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int n, float *A, int lda, int *lwork)[#](#_CPPv426hipsolverSsytrf_bufferSize17hipsolverHandle_tiPfiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZsytrf([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipDoubleComplex *A, int lda, int *ipiv, hipDoubleComplex *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverZsytrf17hipsolverHandle_t19hipsolverFillMode_tiP16hipDoubleComplexiPiP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCsytrf([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipFloatComplex *A, int lda, int *ipiv, hipFloatComplex *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverCsytrf17hipsolverHandle_t19hipsolverFillMode_tiP15hipFloatComplexiPiP15hipFloatComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDsytrf([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, double *A, int lda, int *ipiv, double *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverDsytrf17hipsolverHandle_t19hipsolverFillMode_tiPdiPiPdiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSsytrf([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, float *A, int lda, int *ipiv, float *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverSsytrf17hipsolverHandle_t19hipsolverFillMode_tiPfiPiPfiPi)

## Orthogonal factorizations[#](#orthogonal-factorizations)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZgeqrf_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, hipDoubleComplex *A, int lda, int *lwork)[#](#_CPPv426hipsolverZgeqrf_bufferSize17hipsolverHandle_tiiP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCgeqrf_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, hipFloatComplex *A, int lda, int *lwork)[#](#_CPPv426hipsolverCgeqrf_bufferSize17hipsolverHandle_tiiP15hipFloatComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDgeqrf_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, double *A, int lda, int *lwork)[#](#_CPPv426hipsolverDgeqrf_bufferSize17hipsolverHandle_tiiPdiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSgeqrf_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, float *A, int lda, int *lwork)[#](#_CPPv426hipsolverSgeqrf_bufferSize17hipsolverHandle_tiiPfiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZgeqrf([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, hipDoubleComplex *A, int lda, hipDoubleComplex *tau, hipDoubleComplex *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverZgeqrf17hipsolverHandle_tiiP16hipDoubleComplexiP16hipDoubleComplexP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCgeqrf([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, hipFloatComplex *A, int lda, hipFloatComplex *tau, hipFloatComplex *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverCgeqrf17hipsolverHandle_tiiP15hipFloatComplexiP15hipFloatComplexP15hipFloatComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDgeqrf([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, double *A, int lda, double *tau, double *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverDgeqrf17hipsolverHandle_tiiPdiPdPdiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSgeqrf([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, float *A, int lda, float *tau, float *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverSgeqrf17hipsolverHandle_tiiPfiPfPfiPi)

## Problem and matrix reductions[#](#problem-and-matrix-reductions)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZgebrd_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int *lwork)[#](#_CPPv426hipsolverZgebrd_bufferSize17hipsolverHandle_tiiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCgebrd_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int *lwork)[#](#_CPPv426hipsolverCgebrd_bufferSize17hipsolverHandle_tiiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDgebrd_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int *lwork)[#](#_CPPv426hipsolverDgebrd_bufferSize17hipsolverHandle_tiiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSgebrd_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int *lwork)[#](#_CPPv426hipsolverSgebrd_bufferSize17hipsolverHandle_tiiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZgebrd([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, hipDoubleComplex *A, int lda, double *D, double *E, hipDoubleComplex *tauq, hipDoubleComplex *taup, hipDoubleComplex *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverZgebrd17hipsolverHandle_tiiP16hipDoubleComplexiPdPdP16hipDoubleComplexP16hipDoubleComplexP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCgebrd([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, hipFloatComplex *A, int lda, float *D, float *E, hipFloatComplex *tauq, hipFloatComplex *taup, hipFloatComplex *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverCgebrd17hipsolverHandle_tiiP15hipFloatComplexiPfPfP15hipFloatComplexP15hipFloatComplexP15hipFloatComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDgebrd([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, double *A, int lda, double *D, double *E, double *tauq, double *taup, double *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverDgebrd17hipsolverHandle_tiiPdiPdPdPdPdPdiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSgebrd([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, float *A, int lda, float *D, float *E, float *tauq, float *taup, float *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverSgebrd17hipsolverHandle_tiiPfiPfPfPfPfPfiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDsytrd_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, double *A, int lda, double *D, double *E, double *tau, int *lwork)[#](#_CPPv426hipsolverDsytrd_bufferSize17hipsolverHandle_t19hipsolverFillMode_tiPdiPdPdPdPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSsytrd_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, float *A, int lda, float *D, float *E, float *tau, int *lwork)[#](#_CPPv426hipsolverSsytrd_bufferSize17hipsolverHandle_t19hipsolverFillMode_tiPfiPfPfPfPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZhetrd_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipDoubleComplex *A, int lda, double *D, double *E, hipDoubleComplex *tau, int *lwork)[#](#_CPPv426hipsolverZhetrd_bufferSize17hipsolverHandle_t19hipsolverFillMode_tiP16hipDoubleComplexiPdPdP16hipDoubleComplexPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverChetrd_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipFloatComplex *A, int lda, float *D, float *E, hipFloatComplex *tau, int *lwork)[#](#_CPPv426hipsolverChetrd_bufferSize17hipsolverHandle_t19hipsolverFillMode_tiP15hipFloatComplexiPfPfP15hipFloatComplexPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDsytrd([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, double *A, int lda, double *D, double *E, double *tau, double *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverDsytrd17hipsolverHandle_t19hipsolverFillMode_tiPdiPdPdPdPdiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSsytrd([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, float *A, int lda, float *D, float *E, float *tau, float *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverSsytrd17hipsolverHandle_t19hipsolverFillMode_tiPfiPfPfPfPfiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZhetrd([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipDoubleComplex *A, int lda, double *D, double *E, hipDoubleComplex *tau, hipDoubleComplex *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverZhetrd17hipsolverHandle_t19hipsolverFillMode_tiP16hipDoubleComplexiPdPdP16hipDoubleComplexP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverChetrd([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipFloatComplex *A, int lda, float *D, float *E, hipFloatComplex *tau, hipFloatComplex *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverChetrd17hipsolverHandle_t19hipsolverFillMode_tiP15hipFloatComplexiPfPfP15hipFloatComplexP15hipFloatComplexiPi)

## Linear-systems solvers[#](#linear-systems-solvers)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZpotri_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipDoubleComplex *A, int lda, int *lwork)[#](#_CPPv426hipsolverZpotri_bufferSize17hipsolverHandle_t19hipsolverFillMode_tiP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCpotri_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipFloatComplex *A, int lda, int *lwork)[#](#_CPPv426hipsolverCpotri_bufferSize17hipsolverHandle_t19hipsolverFillMode_tiP15hipFloatComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDpotri_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, double *A, int lda, int *lwork)[#](#_CPPv426hipsolverDpotri_bufferSize17hipsolverHandle_t19hipsolverFillMode_tiPdiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSpotri_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, float *A, int lda, int *lwork)[#](#_CPPv426hipsolverSpotri_bufferSize17hipsolverHandle_t19hipsolverFillMode_tiPfiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZpotri([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipDoubleComplex *A, int lda, hipDoubleComplex *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverZpotri17hipsolverHandle_t19hipsolverFillMode_tiP16hipDoubleComplexiP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCpotri([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipFloatComplex *A, int lda, hipFloatComplex *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverCpotri17hipsolverHandle_t19hipsolverFillMode_tiP15hipFloatComplexiP15hipFloatComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDpotri([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, double *A, int lda, double *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverDpotri17hipsolverHandle_t19hipsolverFillMode_tiPdiPdiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSpotri([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, float *A, int lda, float *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverSpotri17hipsolverHandle_t19hipsolverFillMode_tiPfiPfiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZpotrs_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, int nrhs, hipDoubleComplex *A, int lda, hipDoubleComplex *B, int ldb, int *lwork)[#](#_CPPv426hipsolverZpotrs_bufferSize17hipsolverHandle_t19hipsolverFillMode_tiiP16hipDoubleComplexiP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCpotrs_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, int nrhs, hipFloatComplex *A, int lda, hipFloatComplex *B, int ldb, int *lwork)[#](#_CPPv426hipsolverCpotrs_bufferSize17hipsolverHandle_t19hipsolverFillMode_tiiP15hipFloatComplexiP15hipFloatComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDpotrs_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, int nrhs, double *A, int lda, double *B, int ldb, int *lwork)[#](#_CPPv426hipsolverDpotrs_bufferSize17hipsolverHandle_t19hipsolverFillMode_tiiPdiPdiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSpotrs_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, int nrhs, float *A, int lda, float *B, int ldb, int *lwork)[#](#_CPPv426hipsolverSpotrs_bufferSize17hipsolverHandle_t19hipsolverFillMode_tiiPfiPfiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZpotrsBatched_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, int nrhs, hipDoubleComplex *A[], int lda, hipDoubleComplex *B[], int ldb, int *lwork, int batch_count)[#](#_CPPv433hipsolverZpotrsBatched_bufferSize17hipsolverHandle_t19hipsolverFillMode_tiiA_P16hipDoubleComplexiA_P16hipDoubleComplexiPii)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCpotrsBatched_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, int nrhs, hipFloatComplex *A[], int lda, hipFloatComplex *B[], int ldb, int *lwork, int batch_count)[#](#_CPPv433hipsolverCpotrsBatched_bufferSize17hipsolverHandle_t19hipsolverFillMode_tiiA_P15hipFloatComplexiA_P15hipFloatComplexiPii)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDpotrsBatched_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, int nrhs, double *A[], int lda, double *B[], int ldb, int *lwork, int batch_count)[#](#_CPPv433hipsolverDpotrsBatched_bufferSize17hipsolverHandle_t19hipsolverFillMode_tiiA_PdiA_PdiPii)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSpotrsBatched_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, int nrhs, float *A[], int lda, float *B[], int ldb, int *lwork, int batch_count)[#](#_CPPv433hipsolverSpotrsBatched_bufferSize17hipsolverHandle_t19hipsolverFillMode_tiiA_PfiA_PfiPii)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZpotrs([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, int nrhs, hipDoubleComplex *A, int lda, hipDoubleComplex *B, int ldb, hipDoubleComplex *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverZpotrs17hipsolverHandle_t19hipsolverFillMode_tiiP16hipDoubleComplexiP16hipDoubleComplexiP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCpotrs([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, int nrhs, hipFloatComplex *A, int lda, hipFloatComplex *B, int ldb, hipFloatComplex *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverCpotrs17hipsolverHandle_t19hipsolverFillMode_tiiP15hipFloatComplexiP15hipFloatComplexiP15hipFloatComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDpotrs([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, int nrhs, double *A, int lda, double *B, int ldb, double *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverDpotrs17hipsolverHandle_t19hipsolverFillMode_tiiPdiPdiPdiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSpotrs([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, int nrhs, float *A, int lda, float *B, int ldb, float *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverSpotrs17hipsolverHandle_t19hipsolverFillMode_tiiPfiPfiPfiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZpotrsBatched([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, int nrhs, hipDoubleComplex *A[], int lda, hipDoubleComplex *B[], int ldb, hipDoubleComplex *work, int lwork, int *devInfo, int batch_count)[#](#_CPPv422hipsolverZpotrsBatched17hipsolverHandle_t19hipsolverFillMode_tiiA_P16hipDoubleComplexiA_P16hipDoubleComplexiP16hipDoubleComplexiPii)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCpotrsBatched([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, int nrhs, hipFloatComplex *A[], int lda, hipFloatComplex *B[], int ldb, hipFloatComplex *work, int lwork, int *devInfo, int batch_count)[#](#_CPPv422hipsolverCpotrsBatched17hipsolverHandle_t19hipsolverFillMode_tiiA_P15hipFloatComplexiA_P15hipFloatComplexiP15hipFloatComplexiPii)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDpotrsBatched([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, int nrhs, double *A[], int lda, double *B[], int ldb, double *work, int lwork, int *devInfo, int batch_count)[#](#_CPPv422hipsolverDpotrsBatched17hipsolverHandle_t19hipsolverFillMode_tiiA_PdiA_PdiPdiPii)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSpotrsBatched([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, int nrhs, float *A[], int lda, float *B[], int ldb, float *work, int lwork, int *devInfo, int batch_count)[#](#_CPPv422hipsolverSpotrsBatched17hipsolverHandle_t19hipsolverFillMode_tiiA_PfiA_PfiPfiPii)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZgetrs_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverOperation_t](types.html#_CPPv420hipsolverOperation_t)trans, int n, int nrhs, hipDoubleComplex *A, int lda, int *devIpiv, hipDoubleComplex *B, int ldb, int *lwork)[#](#_CPPv426hipsolverZgetrs_bufferSize17hipsolverHandle_t20hipsolverOperation_tiiP16hipDoubleComplexiPiP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCgetrs_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverOperation_t](types.html#_CPPv420hipsolverOperation_t)trans, int n, int nrhs, hipFloatComplex *A, int lda, int *devIpiv, hipFloatComplex *B, int ldb, int *lwork)[#](#_CPPv426hipsolverCgetrs_bufferSize17hipsolverHandle_t20hipsolverOperation_tiiP15hipFloatComplexiPiP15hipFloatComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDgetrs_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverOperation_t](types.html#_CPPv420hipsolverOperation_t)trans, int n, int nrhs, double *A, int lda, int *devIpiv, double *B, int ldb, int *lwork)[#](#_CPPv426hipsolverDgetrs_bufferSize17hipsolverHandle_t20hipsolverOperation_tiiPdiPiPdiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSgetrs_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverOperation_t](types.html#_CPPv420hipsolverOperation_t)trans, int n, int nrhs, float *A, int lda, int *devIpiv, float *B, int ldb, int *lwork)[#](#_CPPv426hipsolverSgetrs_bufferSize17hipsolverHandle_t20hipsolverOperation_tiiPfiPiPfiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZgetrs([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverOperation_t](types.html#_CPPv420hipsolverOperation_t)trans, int n, int nrhs, hipDoubleComplex *A, int lda, int *devIpiv, hipDoubleComplex *B, int ldb, hipDoubleComplex *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverZgetrs17hipsolverHandle_t20hipsolverOperation_tiiP16hipDoubleComplexiPiP16hipDoubleComplexiP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCgetrs([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverOperation_t](types.html#_CPPv420hipsolverOperation_t)trans, int n, int nrhs, hipFloatComplex *A, int lda, int *devIpiv, hipFloatComplex *B, int ldb, hipFloatComplex *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverCgetrs17hipsolverHandle_t20hipsolverOperation_tiiP15hipFloatComplexiPiP15hipFloatComplexiP15hipFloatComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDgetrs([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverOperation_t](types.html#_CPPv420hipsolverOperation_t)trans, int n, int nrhs, double *A, int lda, int *devIpiv, double *B, int ldb, double *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverDgetrs17hipsolverHandle_t20hipsolverOperation_tiiPdiPiPdiPdiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSgetrs([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverOperation_t](types.html#_CPPv420hipsolverOperation_t)trans, int n, int nrhs, float *A, int lda, int *devIpiv, float *B, int ldb, float *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverSgetrs17hipsolverHandle_t20hipsolverOperation_tiiPfiPiPfiPfiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZZgesv_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int n, int nrhs, hipDoubleComplex *A, int lda, int *devIpiv, hipDoubleComplex *B, int ldb, hipDoubleComplex *X, int ldx, size_t *lwork)[#](#_CPPv426hipsolverZZgesv_bufferSize17hipsolverHandle_tiiP16hipDoubleComplexiPiP16hipDoubleComplexiP16hipDoubleComplexiP6size_t)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCCgesv_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int n, int nrhs, hipFloatComplex *A, int lda, int *devIpiv, hipFloatComplex *B, int ldb, hipFloatComplex *X, int ldx, size_t *lwork)[#](#_CPPv426hipsolverCCgesv_bufferSize17hipsolverHandle_tiiP15hipFloatComplexiPiP15hipFloatComplexiP15hipFloatComplexiP6size_t)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDDgesv_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int n, int nrhs, double *A, int lda, int *devIpiv, double *B, int ldb, double *X, int ldx, size_t *lwork)[#](#_CPPv426hipsolverDDgesv_bufferSize17hipsolverHandle_tiiPdiPiPdiPdiP6size_t)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSSgesv_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int n, int nrhs, float *A, int lda, int *devIpiv, float *B, int ldb, float *X, int ldx, size_t *lwork)[#](#_CPPv426hipsolverSSgesv_bufferSize17hipsolverHandle_tiiPfiPiPfiPfiP6size_t)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZZgesv([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int n, int nrhs, hipDoubleComplex *A, int lda, int *devIpiv, hipDoubleComplex *B, int ldb, hipDoubleComplex *X, int ldx, void *work, size_t lwork, int *niters, int *devInfo)[#](#_CPPv415hipsolverZZgesv17hipsolverHandle_tiiP16hipDoubleComplexiPiP16hipDoubleComplexiP16hipDoubleComplexiPv6size_tPiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCCgesv([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int n, int nrhs, hipFloatComplex *A, int lda, int *devIpiv, hipFloatComplex *B, int ldb, hipFloatComplex *X, int ldx, void *work, size_t lwork, int *niters, int *devInfo)[#](#_CPPv415hipsolverCCgesv17hipsolverHandle_tiiP15hipFloatComplexiPiP15hipFloatComplexiP15hipFloatComplexiPv6size_tPiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDDgesv([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int n, int nrhs, double *A, int lda, int *devIpiv, double *B, int ldb, double *X, int ldx, void *work, size_t lwork, int *niters, int *devInfo)[#](#_CPPv415hipsolverDDgesv17hipsolverHandle_tiiPdiPiPdiPdiPv6size_tPiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSSgesv([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int n, int nrhs, float *A, int lda, int *devIpiv, float *B, int ldb, float *X, int ldx, void *work, size_t lwork, int *niters, int *devInfo)[#](#_CPPv415hipsolverSSgesv17hipsolverHandle_tiiPfiPiPfiPfiPv6size_tPiPi)

## Least-squares solvers[#](#least-squares-solvers)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZZgels_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int nrhs, hipDoubleComplex *A, int lda, hipDoubleComplex *B, int ldb, hipDoubleComplex *X, int ldx, size_t *lwork)[#](#_CPPv426hipsolverZZgels_bufferSize17hipsolverHandle_tiiiP16hipDoubleComplexiP16hipDoubleComplexiP16hipDoubleComplexiP6size_t)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCCgels_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int nrhs, hipFloatComplex *A, int lda, hipFloatComplex *B, int ldb, hipFloatComplex *X, int ldx, size_t *lwork)[#](#_CPPv426hipsolverCCgels_bufferSize17hipsolverHandle_tiiiP15hipFloatComplexiP15hipFloatComplexiP15hipFloatComplexiP6size_t)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDDgels_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int nrhs, double *A, int lda, double *B, int ldb, double *X, int ldx, size_t *lwork)[#](#_CPPv426hipsolverDDgels_bufferSize17hipsolverHandle_tiiiPdiPdiPdiP6size_t)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSSgels_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int nrhs, float *A, int lda, float *B, int ldb, float *X, int ldx, size_t *lwork)[#](#_CPPv426hipsolverSSgels_bufferSize17hipsolverHandle_tiiiPfiPfiPfiP6size_t)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZZgels([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int nrhs, hipDoubleComplex *A, int lda, hipDoubleComplex *B, int ldb, hipDoubleComplex *X, int ldx, void *work, size_t lwork, int *niters, int *devInfo)[#](#_CPPv415hipsolverZZgels17hipsolverHandle_tiiiP16hipDoubleComplexiP16hipDoubleComplexiP16hipDoubleComplexiPv6size_tPiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCCgels([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int nrhs, hipFloatComplex *A, int lda, hipFloatComplex *B, int ldb, hipFloatComplex *X, int ldx, void *work, size_t lwork, int *niters, int *devInfo)[#](#_CPPv415hipsolverCCgels17hipsolverHandle_tiiiP15hipFloatComplexiP15hipFloatComplexiP15hipFloatComplexiPv6size_tPiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDDgels([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int nrhs, double *A, int lda, double *B, int ldb, double *X, int ldx, void *work, size_t lwork, int *niters, int *devInfo)[#](#_CPPv415hipsolverDDgels17hipsolverHandle_tiiiPdiPdiPdiPv6size_tPiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSSgels([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, int m, int n, int nrhs, float *A, int lda, float *B, int ldb, float *X, int ldx, void *work, size_t lwork, int *niters, int *devInfo)[#](#_CPPv415hipsolverSSgels17hipsolverHandle_tiiiPfiPfiPfiPv6size_tPiPi)

## Symmetric eigensolvers[#](#symmetric-eigensolvers)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDsyevd_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, double *A, int lda, double *D, int *lwork)[#](#_CPPv426hipsolverDsyevd_bufferSize17hipsolverHandle_t18hipsolverEigMode_t19hipsolverFillMode_tiPdiPdPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSsyevd_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, float *A, int lda, float *D, int *lwork)[#](#_CPPv426hipsolverSsyevd_bufferSize17hipsolverHandle_t18hipsolverEigMode_t19hipsolverFillMode_tiPfiPfPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZheevd_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipDoubleComplex *A, int lda, double *D, int *lwork)[#](#_CPPv426hipsolverZheevd_bufferSize17hipsolverHandle_t18hipsolverEigMode_t19hipsolverFillMode_tiP16hipDoubleComplexiPdPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCheevd_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipFloatComplex *A, int lda, float *D, int *lwork)[#](#_CPPv426hipsolverCheevd_bufferSize17hipsolverHandle_t18hipsolverEigMode_t19hipsolverFillMode_tiP15hipFloatComplexiPfPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDsyevd([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, double *A, int lda, double *D, double *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverDsyevd17hipsolverHandle_t18hipsolverEigMode_t19hipsolverFillMode_tiPdiPdPdiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSsyevd([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, float *A, int lda, float *D, float *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverSsyevd17hipsolverHandle_t18hipsolverEigMode_t19hipsolverFillMode_tiPfiPfPfiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZheevd([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipDoubleComplex *A, int lda, double *D, hipDoubleComplex *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverZheevd17hipsolverHandle_t18hipsolverEigMode_t19hipsolverFillMode_tiP16hipDoubleComplexiPdP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCheevd([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipFloatComplex *A, int lda, float *D, hipFloatComplex *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverCheevd17hipsolverHandle_t18hipsolverEigMode_t19hipsolverFillMode_tiP15hipFloatComplexiPfP15hipFloatComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDsygvd_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigType_t](types.html#_CPPv418hipsolverEigType_t)itype,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, double *A, int lda, double *B, int ldb, double *W, int *lwork)[#](#_CPPv426hipsolverDsygvd_bufferSize17hipsolverHandle_t18hipsolverEigType_t18hipsolverEigMode_t19hipsolverFillMode_tiPdiPdiPdPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSsygvd_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigType_t](types.html#_CPPv418hipsolverEigType_t)itype,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, float *A, int lda, float *B, int ldb, float *W, int *lwork)[#](#_CPPv426hipsolverSsygvd_bufferSize17hipsolverHandle_t18hipsolverEigType_t18hipsolverEigMode_t19hipsolverFillMode_tiPfiPfiPfPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZhegvd_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigType_t](types.html#_CPPv418hipsolverEigType_t)itype,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipDoubleComplex *A, int lda, hipDoubleComplex *B, int ldb, double *W, int *lwork)[#](#_CPPv426hipsolverZhegvd_bufferSize17hipsolverHandle_t18hipsolverEigType_t18hipsolverEigMode_t19hipsolverFillMode_tiP16hipDoubleComplexiP16hipDoubleComplexiPdPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverChegvd_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigType_t](types.html#_CPPv418hipsolverEigType_t)itype,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipFloatComplex *A, int lda, hipFloatComplex *B, int ldb, float *W, int *lwork)[#](#_CPPv426hipsolverChegvd_bufferSize17hipsolverHandle_t18hipsolverEigType_t18hipsolverEigMode_t19hipsolverFillMode_tiP15hipFloatComplexiP15hipFloatComplexiPfPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDsygvd([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigType_t](types.html#_CPPv418hipsolverEigType_t)itype,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, double *A, int lda, double *B, int ldb, double *W, double *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverDsygvd17hipsolverHandle_t18hipsolverEigType_t18hipsolverEigMode_t19hipsolverFillMode_tiPdiPdiPdPdiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSsygvd([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigType_t](types.html#_CPPv418hipsolverEigType_t)itype,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, float *A, int lda, float *B, int ldb, float *W, float *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverSsygvd17hipsolverHandle_t18hipsolverEigType_t18hipsolverEigMode_t19hipsolverFillMode_tiPfiPfiPfPfiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZhegvd([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigType_t](types.html#_CPPv418hipsolverEigType_t)itype,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipDoubleComplex *A, int lda, hipDoubleComplex *B, int ldb, double *W, hipDoubleComplex *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverZhegvd17hipsolverHandle_t18hipsolverEigType_t18hipsolverEigMode_t19hipsolverFillMode_tiP16hipDoubleComplexiP16hipDoubleComplexiPdP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverChegvd([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigType_t](types.html#_CPPv418hipsolverEigType_t)itype,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipFloatComplex *A, int lda, hipFloatComplex *B, int ldb, float *W, hipFloatComplex *work, int lwork, int *devInfo)[#](#_CPPv415hipsolverChegvd17hipsolverHandle_t18hipsolverEigType_t18hipsolverEigMode_t19hipsolverFillMode_tiP15hipFloatComplexiP15hipFloatComplexiPfP15hipFloatComplexiPi)

## Singular value decomposition[#](#singular-value-decomposition)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZgesvd_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, signed char jobu, signed char jobv, int m, int n, int *lwork)[#](#_CPPv426hipsolverZgesvd_bufferSize17hipsolverHandle_taaiiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCgesvd_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, signed char jobu, signed char jobv, int m, int n, int *lwork)[#](#_CPPv426hipsolverCgesvd_bufferSize17hipsolverHandle_taaiiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDgesvd_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, signed char jobu, signed char jobv, int m, int n, int *lwork)[#](#_CPPv426hipsolverDgesvd_bufferSize17hipsolverHandle_taaiiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSgesvd_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, signed char jobu, signed char jobv, int m, int n, int *lwork)[#](#_CPPv426hipsolverSgesvd_bufferSize17hipsolverHandle_taaiiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZgesvd([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, signed char jobu, signed char jobv, int m, int n, hipDoubleComplex *A, int lda, double *S, hipDoubleComplex *U, int ldu, hipDoubleComplex *V, int ldv, hipDoubleComplex *work, int lwork, double *rwork, int *devInfo)[#](#_CPPv415hipsolverZgesvd17hipsolverHandle_taaiiP16hipDoubleComplexiPdP16hipDoubleComplexiP16hipDoubleComplexiP16hipDoubleComplexiPdPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCgesvd([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, signed char jobu, signed char jobv, int m, int n, hipFloatComplex *A, int lda, float *S, hipFloatComplex *U, int ldu, hipFloatComplex *V, int ldv, hipFloatComplex *work, int lwork, float *rwork, int *devInfo)[#](#_CPPv415hipsolverCgesvd17hipsolverHandle_taaiiP15hipFloatComplexiPfP15hipFloatComplexiP15hipFloatComplexiP15hipFloatComplexiPfPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDgesvd([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, signed char jobu, signed char jobv, int m, int n, double *A, int lda, double *S, double *U, int ldu, double *V, int ldv, double *work, int lwork, double *rwork, int *devInfo)[#](#_CPPv415hipsolverDgesvd17hipsolverHandle_taaiiPdiPdPdiPdiPdiPdPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSgesvd([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, signed char jobu, signed char jobv, int m, int n, float *A, int lda, float *S, float *U, int ldu, float *V, int ldv, float *work, int lwork, float *rwork, int *devInfo)[#](#_CPPv415hipsolverSgesvd17hipsolverHandle_taaiiPfiPfPfiPfiPfiPfPi)
