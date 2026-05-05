---
title: "hipSOLVER LAPACK-like functions &#8212; hipSOLVER 3.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/lapacklike.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:21:01.744617+00:00
content_hash: "8c7be6d5da26a8e1"
---

# hipSOLVER LAPACK-like functions[#](#hipsolver-lapack-like-functions)

LAPACK routines solve complex numerical linear algebra problems. These functions are organized into the following categories:

[Symmetric eigensolvers](#likeeigens): Eigenproblems for symmetric matrices.[Singular value decomposition](#likesvds): Singular values and related problems for general matrices.

## Symmetric eigensolvers[#](#symmetric-eigensolvers)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDsyevdx_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverEigRange_t](types.html#_CPPv419hipsolverEigRange_t)range,[hipblasFillMode_t](types.html#_CPPv417hipblasFillMode_t)uplo, int n, const double *A, int lda, double vl, double vu, int il, int iu, int *nev, const double *W, int *lwork)[#](#_CPPv427hipsolverDsyevdx_bufferSize17hipsolverHandle_t18hipsolverEigMode_t19hipsolverEigRange_t17hipblasFillMode_tiPKdiddiiPiPKdPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSsyevdx_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverEigRange_t](types.html#_CPPv419hipsolverEigRange_t)range,[hipblasFillMode_t](types.html#_CPPv417hipblasFillMode_t)uplo, int n, const float *A, int lda, float vl, float vu, int il, int iu, int *nev, const float *W, int *lwork)[#](#_CPPv427hipsolverSsyevdx_bufferSize17hipsolverHandle_t18hipsolverEigMode_t19hipsolverEigRange_t17hipblasFillMode_tiPKfiffiiPiPKfPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZheevdx_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverEigRange_t](types.html#_CPPv419hipsolverEigRange_t)range,[hipblasFillMode_t](types.html#_CPPv417hipblasFillMode_t)uplo, int n, const hipDoubleComplex *A, int lda, double vl, double vu, int il, int iu, int *nev, const double *W, int *lwork)[#](#_CPPv427hipsolverZheevdx_bufferSize17hipsolverHandle_t18hipsolverEigMode_t19hipsolverEigRange_t17hipblasFillMode_tiPK16hipDoubleComplexiddiiPiPKdPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCheevdx_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverEigRange_t](types.html#_CPPv419hipsolverEigRange_t)range,[hipblasFillMode_t](types.html#_CPPv417hipblasFillMode_t)uplo, int n, const hipFloatComplex *A, int lda, float vl, float vu, int il, int iu, int *nev, const float *W, int *lwork)[#](#_CPPv427hipsolverCheevdx_bufferSize17hipsolverHandle_t18hipsolverEigMode_t19hipsolverEigRange_t17hipblasFillMode_tiPK15hipFloatComplexiffiiPiPKfPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDsyevdx([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverEigRange_t](types.html#_CPPv419hipsolverEigRange_t)range,[hipblasFillMode_t](types.html#_CPPv417hipblasFillMode_t)uplo, int n, double *A, int lda, double vl, double vu, int il, int iu, int *nev, double *W, double *work, int lwork, int *devInfo)[#](#_CPPv416hipsolverDsyevdx17hipsolverHandle_t18hipsolverEigMode_t19hipsolverEigRange_t17hipblasFillMode_tiPdiddiiPiPdPdiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSsyevdx([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverEigRange_t](types.html#_CPPv419hipsolverEigRange_t)range,[hipblasFillMode_t](types.html#_CPPv417hipblasFillMode_t)uplo, int n, float *A, int lda, float vl, float vu, int il, int iu, int *nev, float *W, float *work, int lwork, int *devInfo)[#](#_CPPv416hipsolverSsyevdx17hipsolverHandle_t18hipsolverEigMode_t19hipsolverEigRange_t17hipblasFillMode_tiPfiffiiPiPfPfiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZheevdx([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverEigRange_t](types.html#_CPPv419hipsolverEigRange_t)range,[hipblasFillMode_t](types.html#_CPPv417hipblasFillMode_t)uplo, int n, hipDoubleComplex *A, int lda, double vl, double vu, int il, int iu, int *nev, double *W, hipDoubleComplex *work, int lwork, int *devInfo)[#](#_CPPv416hipsolverZheevdx17hipsolverHandle_t18hipsolverEigMode_t19hipsolverEigRange_t17hipblasFillMode_tiP16hipDoubleComplexiddiiPiPdP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCheevdx([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverEigRange_t](types.html#_CPPv419hipsolverEigRange_t)range,[hipblasFillMode_t](types.html#_CPPv417hipblasFillMode_t)uplo, int n, hipFloatComplex *A, int lda, float vl, float vu, int il, int iu, int *nev, float *W, hipFloatComplex *work, int lwork, int *devInfo)[#](#_CPPv416hipsolverCheevdx17hipsolverHandle_t18hipsolverEigMode_t19hipsolverEigRange_t17hipblasFillMode_tiP15hipFloatComplexiffiiPiPfP15hipFloatComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDsyevj_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, double *A, int lda, double *W, int *lwork,[hipsolverSyevjInfo_t](types.html#_CPPv420hipsolverSyevjInfo_t)params)[#](#_CPPv426hipsolverDsyevj_bufferSize17hipsolverHandle_t18hipsolverEigMode_t19hipsolverFillMode_tiPdiPdPi20hipsolverSyevjInfo_t)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSsyevj_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, float *A, int lda, float *W, int *lwork,[hipsolverSyevjInfo_t](types.html#_CPPv420hipsolverSyevjInfo_t)params)[#](#_CPPv426hipsolverSsyevj_bufferSize17hipsolverHandle_t18hipsolverEigMode_t19hipsolverFillMode_tiPfiPfPi20hipsolverSyevjInfo_t)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZheevj_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipDoubleComplex *A, int lda, double *W, int *lwork,[hipsolverSyevjInfo_t](types.html#_CPPv420hipsolverSyevjInfo_t)params)[#](#_CPPv426hipsolverZheevj_bufferSize17hipsolverHandle_t18hipsolverEigMode_t19hipsolverFillMode_tiP16hipDoubleComplexiPdPi20hipsolverSyevjInfo_t)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCheevj_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipFloatComplex *A, int lda, float *W, int *lwork,[hipsolverSyevjInfo_t](types.html#_CPPv420hipsolverSyevjInfo_t)params)[#](#_CPPv426hipsolverCheevj_bufferSize17hipsolverHandle_t18hipsolverEigMode_t19hipsolverFillMode_tiP15hipFloatComplexiPfPi20hipsolverSyevjInfo_t)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDsyevjBatched_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, double *A, int lda, double *W, int *lwork,[hipsolverSyevjInfo_t](types.html#_CPPv420hipsolverSyevjInfo_t)params, int batch_count)[#](#_CPPv433hipsolverDsyevjBatched_bufferSize17hipsolverHandle_t18hipsolverEigMode_t19hipsolverFillMode_tiPdiPdPi20hipsolverSyevjInfo_ti)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSsyevjBatched_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, float *A, int lda, float *W, int *lwork,[hipsolverSyevjInfo_t](types.html#_CPPv420hipsolverSyevjInfo_t)params, int batch_count)[#](#_CPPv433hipsolverSsyevjBatched_bufferSize17hipsolverHandle_t18hipsolverEigMode_t19hipsolverFillMode_tiPfiPfPi20hipsolverSyevjInfo_ti)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZheevjBatched_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipDoubleComplex *A, int lda, double *W, int *lwork,[hipsolverSyevjInfo_t](types.html#_CPPv420hipsolverSyevjInfo_t)params, int batch_count)[#](#_CPPv433hipsolverZheevjBatched_bufferSize17hipsolverHandle_t18hipsolverEigMode_t19hipsolverFillMode_tiP16hipDoubleComplexiPdPi20hipsolverSyevjInfo_ti)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCheevjBatched_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipFloatComplex *A, int lda, float *W, int *lwork,[hipsolverSyevjInfo_t](types.html#_CPPv420hipsolverSyevjInfo_t)params, int batch_count)[#](#_CPPv433hipsolverCheevjBatched_bufferSize17hipsolverHandle_t18hipsolverEigMode_t19hipsolverFillMode_tiP15hipFloatComplexiPfPi20hipsolverSyevjInfo_ti)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDsyevj([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, double *A, int lda, double *W, double *work, int lwork, int *devInfo,[hipsolverSyevjInfo_t](types.html#_CPPv420hipsolverSyevjInfo_t)params)[#](#_CPPv415hipsolverDsyevj17hipsolverHandle_t18hipsolverEigMode_t19hipsolverFillMode_tiPdiPdPdiPi20hipsolverSyevjInfo_t)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSsyevj([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, float *A, int lda, float *W, float *work, int lwork, int *devInfo,[hipsolverSyevjInfo_t](types.html#_CPPv420hipsolverSyevjInfo_t)params)[#](#_CPPv415hipsolverSsyevj17hipsolverHandle_t18hipsolverEigMode_t19hipsolverFillMode_tiPfiPfPfiPi20hipsolverSyevjInfo_t)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZheevj([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipDoubleComplex *A, int lda, double *W, hipDoubleComplex *work, int lwork, int *devInfo,[hipsolverSyevjInfo_t](types.html#_CPPv420hipsolverSyevjInfo_t)params)[#](#_CPPv415hipsolverZheevj17hipsolverHandle_t18hipsolverEigMode_t19hipsolverFillMode_tiP16hipDoubleComplexiPdP16hipDoubleComplexiPi20hipsolverSyevjInfo_t)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCheevj([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipFloatComplex *A, int lda, float *W, hipFloatComplex *work, int lwork, int *devInfo,[hipsolverSyevjInfo_t](types.html#_CPPv420hipsolverSyevjInfo_t)params)[#](#_CPPv415hipsolverCheevj17hipsolverHandle_t18hipsolverEigMode_t19hipsolverFillMode_tiP15hipFloatComplexiPfP15hipFloatComplexiPi20hipsolverSyevjInfo_t)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDsyevjBatched([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, double *A, int lda, double *W, double *work, int lwork, int *devInfo,[hipsolverSyevjInfo_t](types.html#_CPPv420hipsolverSyevjInfo_t)params, int batch_count)[#](#_CPPv422hipsolverDsyevjBatched17hipsolverHandle_t18hipsolverEigMode_t19hipsolverFillMode_tiPdiPdPdiPi20hipsolverSyevjInfo_ti)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSsyevjBatched([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, float *A, int lda, float *W, float *work, int lwork, int *devInfo,[hipsolverSyevjInfo_t](types.html#_CPPv420hipsolverSyevjInfo_t)params, int batch_count)[#](#_CPPv422hipsolverSsyevjBatched17hipsolverHandle_t18hipsolverEigMode_t19hipsolverFillMode_tiPfiPfPfiPi20hipsolverSyevjInfo_ti)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZheevjBatched([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipDoubleComplex *A, int lda, double *W, hipDoubleComplex *work, int lwork, int *devInfo,[hipsolverSyevjInfo_t](types.html#_CPPv420hipsolverSyevjInfo_t)params, int batch_count)[#](#_CPPv422hipsolverZheevjBatched17hipsolverHandle_t18hipsolverEigMode_t19hipsolverFillMode_tiP16hipDoubleComplexiPdP16hipDoubleComplexiPi20hipsolverSyevjInfo_ti)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCheevjBatched([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipFloatComplex *A, int lda, float *W, hipFloatComplex *work, int lwork, int *devInfo,[hipsolverSyevjInfo_t](types.html#_CPPv420hipsolverSyevjInfo_t)params, int batch_count)[#](#_CPPv422hipsolverCheevjBatched17hipsolverHandle_t18hipsolverEigMode_t19hipsolverFillMode_tiP15hipFloatComplexiPfP15hipFloatComplexiPi20hipsolverSyevjInfo_ti)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDsygvdx_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigType_t](types.html#_CPPv418hipsolverEigType_t)itype,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverEigRange_t](types.html#_CPPv419hipsolverEigRange_t)range,[hipblasFillMode_t](types.html#_CPPv417hipblasFillMode_t)uplo, int n, const double *A, int lda, const double *B, int ldb, double vl, double vu, int il, int iu, int *nev, const double *W, int *lwork)[#](#_CPPv427hipsolverDsygvdx_bufferSize17hipsolverHandle_t18hipsolverEigType_t18hipsolverEigMode_t19hipsolverEigRange_t17hipblasFillMode_tiPKdiPKdiddiiPiPKdPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSsygvdx_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigType_t](types.html#_CPPv418hipsolverEigType_t)itype,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverEigRange_t](types.html#_CPPv419hipsolverEigRange_t)range,[hipblasFillMode_t](types.html#_CPPv417hipblasFillMode_t)uplo, int n, const float *A, int lda, const float *B, int ldb, float vl, float vu, int il, int iu, int *nev, const float *W, int *lwork)[#](#_CPPv427hipsolverSsygvdx_bufferSize17hipsolverHandle_t18hipsolverEigType_t18hipsolverEigMode_t19hipsolverEigRange_t17hipblasFillMode_tiPKfiPKfiffiiPiPKfPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZhegvdx_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigType_t](types.html#_CPPv418hipsolverEigType_t)itype,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverEigRange_t](types.html#_CPPv419hipsolverEigRange_t)range,[hipblasFillMode_t](types.html#_CPPv417hipblasFillMode_t)uplo, int n, const hipDoubleComplex *A, int lda, const hipDoubleComplex *B, int ldb, double vl, double vu, int il, int iu, int *nev, const double *W, int *lwork)[#](#_CPPv427hipsolverZhegvdx_bufferSize17hipsolverHandle_t18hipsolverEigType_t18hipsolverEigMode_t19hipsolverEigRange_t17hipblasFillMode_tiPK16hipDoubleComplexiPK16hipDoubleComplexiddiiPiPKdPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverChegvdx_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigType_t](types.html#_CPPv418hipsolverEigType_t)itype,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverEigRange_t](types.html#_CPPv419hipsolverEigRange_t)range,[hipblasFillMode_t](types.html#_CPPv417hipblasFillMode_t)uplo, int n, const hipFloatComplex *A, int lda, const hipFloatComplex *B, int ldb, float vl, float vu, int il, int iu, int *nev, const float *W, int *lwork)[#](#_CPPv427hipsolverChegvdx_bufferSize17hipsolverHandle_t18hipsolverEigType_t18hipsolverEigMode_t19hipsolverEigRange_t17hipblasFillMode_tiPK15hipFloatComplexiPK15hipFloatComplexiffiiPiPKfPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDsygvdx([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigType_t](types.html#_CPPv418hipsolverEigType_t)itype,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverEigRange_t](types.html#_CPPv419hipsolverEigRange_t)range,[hipblasFillMode_t](types.html#_CPPv417hipblasFillMode_t)uplo, int n, double *A, int lda, double *B, int ldb, double vl, double vu, int il, int iu, int *nev, double *W, double *work, int lwork, int *devInfo)[#](#_CPPv416hipsolverDsygvdx17hipsolverHandle_t18hipsolverEigType_t18hipsolverEigMode_t19hipsolverEigRange_t17hipblasFillMode_tiPdiPdiddiiPiPdPdiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSsygvdx([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigType_t](types.html#_CPPv418hipsolverEigType_t)itype,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverEigRange_t](types.html#_CPPv419hipsolverEigRange_t)range,[hipblasFillMode_t](types.html#_CPPv417hipblasFillMode_t)uplo, int n, float *A, int lda, float *B, int ldb, float vl, float vu, int il, int iu, int *nev, float *W, float *work, int lwork, int *devInfo)[#](#_CPPv416hipsolverSsygvdx17hipsolverHandle_t18hipsolverEigType_t18hipsolverEigMode_t19hipsolverEigRange_t17hipblasFillMode_tiPfiPfiffiiPiPfPfiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZhegvdx([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigType_t](types.html#_CPPv418hipsolverEigType_t)itype,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverEigRange_t](types.html#_CPPv419hipsolverEigRange_t)range,[hipblasFillMode_t](types.html#_CPPv417hipblasFillMode_t)uplo, int n, hipDoubleComplex *A, int lda, hipDoubleComplex *B, int ldb, double vl, double vu, int il, int iu, int *nev, double *W, hipDoubleComplex *work, int lwork, int *devInfo)[#](#_CPPv416hipsolverZhegvdx17hipsolverHandle_t18hipsolverEigType_t18hipsolverEigMode_t19hipsolverEigRange_t17hipblasFillMode_tiP16hipDoubleComplexiP16hipDoubleComplexiddiiPiPdP16hipDoubleComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverChegvdx([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigType_t](types.html#_CPPv418hipsolverEigType_t)itype,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverEigRange_t](types.html#_CPPv419hipsolverEigRange_t)range,[hipblasFillMode_t](types.html#_CPPv417hipblasFillMode_t)uplo, int n, hipFloatComplex *A, int lda, hipFloatComplex *B, int ldb, float vl, float vu, int il, int iu, int *nev, float *W, hipFloatComplex *work, int lwork, int *devInfo)[#](#_CPPv416hipsolverChegvdx17hipsolverHandle_t18hipsolverEigType_t18hipsolverEigMode_t19hipsolverEigRange_t17hipblasFillMode_tiP15hipFloatComplexiP15hipFloatComplexiffiiPiPfP15hipFloatComplexiPi)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDsygvj_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigType_t](types.html#_CPPv418hipsolverEigType_t)itype,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, double *A, int lda, double *B, int ldb, double *W, int *lwork,[hipsolverSyevjInfo_t](types.html#_CPPv420hipsolverSyevjInfo_t)params)[#](#_CPPv426hipsolverDsygvj_bufferSize17hipsolverHandle_t18hipsolverEigType_t18hipsolverEigMode_t19hipsolverFillMode_tiPdiPdiPdPi20hipsolverSyevjInfo_t)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSsygvj_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigType_t](types.html#_CPPv418hipsolverEigType_t)itype,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, float *A, int lda, float *B, int ldb, float *W, int *lwork,[hipsolverSyevjInfo_t](types.html#_CPPv420hipsolverSyevjInfo_t)params)[#](#_CPPv426hipsolverSsygvj_bufferSize17hipsolverHandle_t18hipsolverEigType_t18hipsolverEigMode_t19hipsolverFillMode_tiPfiPfiPfPi20hipsolverSyevjInfo_t)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZhegvj_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigType_t](types.html#_CPPv418hipsolverEigType_t)itype,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipDoubleComplex *A, int lda, hipDoubleComplex *B, int ldb, double *W, int *lwork,[hipsolverSyevjInfo_t](types.html#_CPPv420hipsolverSyevjInfo_t)params)[#](#_CPPv426hipsolverZhegvj_bufferSize17hipsolverHandle_t18hipsolverEigType_t18hipsolverEigMode_t19hipsolverFillMode_tiP16hipDoubleComplexiP16hipDoubleComplexiPdPi20hipsolverSyevjInfo_t)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverChegvj_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigType_t](types.html#_CPPv418hipsolverEigType_t)itype,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipFloatComplex *A, int lda, hipFloatComplex *B, int ldb, float *W, int *lwork,[hipsolverSyevjInfo_t](types.html#_CPPv420hipsolverSyevjInfo_t)params)[#](#_CPPv426hipsolverChegvj_bufferSize17hipsolverHandle_t18hipsolverEigType_t18hipsolverEigMode_t19hipsolverFillMode_tiP15hipFloatComplexiP15hipFloatComplexiPfPi20hipsolverSyevjInfo_t)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDsygvj([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigType_t](types.html#_CPPv418hipsolverEigType_t)itype,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, double *A, int lda, double *B, int ldb, double *W, double *work, int lwork, int *devInfo,[hipsolverSyevjInfo_t](types.html#_CPPv420hipsolverSyevjInfo_t)params)[#](#_CPPv415hipsolverDsygvj17hipsolverHandle_t18hipsolverEigType_t18hipsolverEigMode_t19hipsolverFillMode_tiPdiPdiPdPdiPi20hipsolverSyevjInfo_t)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSsygvj([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigType_t](types.html#_CPPv418hipsolverEigType_t)itype,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, float *A, int lda, float *B, int ldb, float *W, float *work, int lwork, int *devInfo,[hipsolverSyevjInfo_t](types.html#_CPPv420hipsolverSyevjInfo_t)params)[#](#_CPPv415hipsolverSsygvj17hipsolverHandle_t18hipsolverEigType_t18hipsolverEigMode_t19hipsolverFillMode_tiPfiPfiPfPfiPi20hipsolverSyevjInfo_t)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZhegvj([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigType_t](types.html#_CPPv418hipsolverEigType_t)itype,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipDoubleComplex *A, int lda, hipDoubleComplex *B, int ldb, double *W, hipDoubleComplex *work, int lwork, int *devInfo,[hipsolverSyevjInfo_t](types.html#_CPPv420hipsolverSyevjInfo_t)params)[#](#_CPPv415hipsolverZhegvj17hipsolverHandle_t18hipsolverEigType_t18hipsolverEigMode_t19hipsolverFillMode_tiP16hipDoubleComplexiP16hipDoubleComplexiPdP16hipDoubleComplexiPi20hipsolverSyevjInfo_t)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverChegvj([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigType_t](types.html#_CPPv418hipsolverEigType_t)itype,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz,[hipsolverFillMode_t](types.html#_CPPv419hipsolverFillMode_t)uplo, int n, hipFloatComplex *A, int lda, hipFloatComplex *B, int ldb, float *W, hipFloatComplex *work, int lwork, int *devInfo,[hipsolverSyevjInfo_t](types.html#_CPPv420hipsolverSyevjInfo_t)params)[#](#_CPPv415hipsolverChegvj17hipsolverHandle_t18hipsolverEigType_t18hipsolverEigMode_t19hipsolverFillMode_tiP15hipFloatComplexiP15hipFloatComplexiPfP15hipFloatComplexiPi20hipsolverSyevjInfo_t)

## Singular value decomposition[#](#singular-value-decomposition)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZgesvdj_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz, int econ, int m, int n, const hipDoubleComplex *A, int lda, const double *S, const hipDoubleComplex *U, int ldu, const hipDoubleComplex *V, int ldv, int *lwork,[hipsolverGesvdjInfo_t](types.html#_CPPv421hipsolverGesvdjInfo_t)params)[#](#_CPPv427hipsolverZgesvdj_bufferSize17hipsolverHandle_t18hipsolverEigMode_tiiiPK16hipDoubleComplexiPKdPK16hipDoubleComplexiPK16hipDoubleComplexiPi21hipsolverGesvdjInfo_t)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCgesvdj_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz, int econ, int m, int n, const hipFloatComplex *A, int lda, const float *S, const hipFloatComplex *U, int ldu, const hipFloatComplex *V, int ldv, int *lwork,[hipsolverGesvdjInfo_t](types.html#_CPPv421hipsolverGesvdjInfo_t)params)[#](#_CPPv427hipsolverCgesvdj_bufferSize17hipsolverHandle_t18hipsolverEigMode_tiiiPK15hipFloatComplexiPKfPK15hipFloatComplexiPK15hipFloatComplexiPi21hipsolverGesvdjInfo_t)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDgesvdj_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz, int econ, int m, int n, const double *A, int lda, const double *S, const double *U, int ldu, const double *V, int ldv, int *lwork,[hipsolverGesvdjInfo_t](types.html#_CPPv421hipsolverGesvdjInfo_t)params)[#](#_CPPv427hipsolverDgesvdj_bufferSize17hipsolverHandle_t18hipsolverEigMode_tiiiPKdiPKdPKdiPKdiPi21hipsolverGesvdjInfo_t)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSgesvdj_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz, int econ, int m, int n, const float *A, int lda, const float *S, const float *U, int ldu, const float *V, int ldv, int *lwork,[hipsolverGesvdjInfo_t](types.html#_CPPv421hipsolverGesvdjInfo_t)params)[#](#_CPPv427hipsolverSgesvdj_bufferSize17hipsolverHandle_t18hipsolverEigMode_tiiiPKfiPKfPKfiPKfiPi21hipsolverGesvdjInfo_t)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZgesvdjBatched_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz, int m, int n, const hipDoubleComplex *A, int lda, const double *S, const hipDoubleComplex *U, int ldu, const hipDoubleComplex *V, int ldv, int *lwork,[hipsolverGesvdjInfo_t](types.html#_CPPv421hipsolverGesvdjInfo_t)params, int batch_count)[#](#_CPPv434hipsolverZgesvdjBatched_bufferSize17hipsolverHandle_t18hipsolverEigMode_tiiPK16hipDoubleComplexiPKdPK16hipDoubleComplexiPK16hipDoubleComplexiPi21hipsolverGesvdjInfo_ti)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCgesvdjBatched_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz, int m, int n, const hipFloatComplex *A, int lda, const float *S, const hipFloatComplex *U, int ldu, const hipFloatComplex *V, int ldv, int *lwork,[hipsolverGesvdjInfo_t](types.html#_CPPv421hipsolverGesvdjInfo_t)params, int batch_count)[#](#_CPPv434hipsolverCgesvdjBatched_bufferSize17hipsolverHandle_t18hipsolverEigMode_tiiPK15hipFloatComplexiPKfPK15hipFloatComplexiPK15hipFloatComplexiPi21hipsolverGesvdjInfo_ti)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDgesvdjBatched_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz, int m, int n, const double *A, int lda, const double *S, const double *U, int ldu, const double *V, int ldv, int *lwork,[hipsolverGesvdjInfo_t](types.html#_CPPv421hipsolverGesvdjInfo_t)params, int batch_count)[#](#_CPPv434hipsolverDgesvdjBatched_bufferSize17hipsolverHandle_t18hipsolverEigMode_tiiPKdiPKdPKdiPKdiPi21hipsolverGesvdjInfo_ti)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSgesvdjBatched_bufferSize([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz, int m, int n, const float *A, int lda, const float *S, const float *U, int ldu, const float *V, int ldv, int *lwork,[hipsolverGesvdjInfo_t](types.html#_CPPv421hipsolverGesvdjInfo_t)params, int batch_count)[#](#_CPPv434hipsolverSgesvdjBatched_bufferSize17hipsolverHandle_t18hipsolverEigMode_tiiPKfiPKfPKfiPKfiPi21hipsolverGesvdjInfo_ti)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZgesvdj([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz, int econ, int m, int n, hipDoubleComplex *A, int lda, double *S, hipDoubleComplex *U, int ldu, hipDoubleComplex *V, int ldv, hipDoubleComplex *work, int lwork, int *devInfo,[hipsolverGesvdjInfo_t](types.html#_CPPv421hipsolverGesvdjInfo_t)params)[#](#_CPPv416hipsolverZgesvdj17hipsolverHandle_t18hipsolverEigMode_tiiiP16hipDoubleComplexiPdP16hipDoubleComplexiP16hipDoubleComplexiP16hipDoubleComplexiPi21hipsolverGesvdjInfo_t)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCgesvdj([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz, int econ, int m, int n, hipFloatComplex *A, int lda, float *S, hipFloatComplex *U, int ldu, hipFloatComplex *V, int ldv, hipFloatComplex *work, int lwork, int *devInfo,[hipsolverGesvdjInfo_t](types.html#_CPPv421hipsolverGesvdjInfo_t)params)[#](#_CPPv416hipsolverCgesvdj17hipsolverHandle_t18hipsolverEigMode_tiiiP15hipFloatComplexiPfP15hipFloatComplexiP15hipFloatComplexiP15hipFloatComplexiPi21hipsolverGesvdjInfo_t)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDgesvdj([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz, int econ, int m, int n, double *A, int lda, double *S, double *U, int ldu, double *V, int ldv, double *work, int lwork, int *devInfo,[hipsolverGesvdjInfo_t](types.html#_CPPv421hipsolverGesvdjInfo_t)params)[#](#_CPPv416hipsolverDgesvdj17hipsolverHandle_t18hipsolverEigMode_tiiiPdiPdPdiPdiPdiPi21hipsolverGesvdjInfo_t)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSgesvdj([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz, int econ, int m, int n, float *A, int lda, float *S, float *U, int ldu, float *V, int ldv, float *work, int lwork, int *devInfo,[hipsolverGesvdjInfo_t](types.html#_CPPv421hipsolverGesvdjInfo_t)params)[#](#_CPPv416hipsolverSgesvdj17hipsolverHandle_t18hipsolverEigMode_tiiiPfiPfPfiPfiPfiPi21hipsolverGesvdjInfo_t)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverZgesvdjBatched([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz, int m, int n, hipDoubleComplex *A, int lda, double *S, hipDoubleComplex *U, int ldu, hipDoubleComplex *V, int ldv, hipDoubleComplex *work, int lwork, int *devInfo,[hipsolverGesvdjInfo_t](types.html#_CPPv421hipsolverGesvdjInfo_t)params, int batch_count)[#](#_CPPv423hipsolverZgesvdjBatched17hipsolverHandle_t18hipsolverEigMode_tiiP16hipDoubleComplexiPdP16hipDoubleComplexiP16hipDoubleComplexiP16hipDoubleComplexiPi21hipsolverGesvdjInfo_ti)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCgesvdjBatched([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz, int m, int n, hipFloatComplex *A, int lda, float *S, hipFloatComplex *U, int ldu, hipFloatComplex *V, int ldv, hipFloatComplex *work, int lwork, int *devInfo,[hipsolverGesvdjInfo_t](types.html#_CPPv421hipsolverGesvdjInfo_t)params, int batch_count)[#](#_CPPv423hipsolverCgesvdjBatched17hipsolverHandle_t18hipsolverEigMode_tiiP15hipFloatComplexiPfP15hipFloatComplexiP15hipFloatComplexiP15hipFloatComplexiPi21hipsolverGesvdjInfo_ti)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDgesvdjBatched([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz, int m, int n, double *A, int lda, double *S, double *U, int ldu, double *V, int ldv, double *work, int lwork, int *devInfo,[hipsolverGesvdjInfo_t](types.html#_CPPv421hipsolverGesvdjInfo_t)params, int batch_count)[#](#_CPPv423hipsolverDgesvdjBatched17hipsolverHandle_t18hipsolverEigMode_tiiPdiPdPdiPdiPdiPi21hipsolverGesvdjInfo_ti)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSgesvdjBatched([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverEigMode_t](types.html#_CPPv418hipsolverEigMode_t)jobz, int m, int n, float *A, int lda, float *S, float *U, int ldu, float *V, int ldv, float *work, int lwork, int *devInfo,[hipsolverGesvdjInfo_t](types.html#_CPPv421hipsolverGesvdjInfo_t)params, int batch_count)[#](#_CPPv423hipsolverSgesvdjBatched17hipsolverHandle_t18hipsolverEigMode_tiiPfiPfPfiPfiPfiPi21hipsolverGesvdjInfo_ti)
