---
title: "Sparse auxiliary functions &#8212; hipSPARSE 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipSPARSE/en/latest/reference/auxiliary.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:09:53.121670+00:00
content_hash: "77010964f6b5ec46"
---

# Sparse auxiliary functions[#](#sparse-auxiliary-functions)

This module contains all sparse auxiliary functions.

The functions that are contained in the auxiliary module describe all available helper functions that are required for subsequent library calls.

## hipsparseCreate()[#](#hipsparsecreate)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCreate([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)*handle)[#](#_CPPv415hipsparseCreateP17hipsparseHandle_t) Create a hipsparse handle.

`hipsparseCreate`

creates the hipSPARSE library context. It must be initialized before any other hipSPARSE API function is invoked and must be passed to all subsequent library function calls. The handle should be destroyed at the end using[hipsparseDestroy()](#hipsparse-auxiliary_8h_1a320899e020b6f66f73730105f0ad98c0).

## hipsparseDestroy()[#](#hipsparsedestroy)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDestroy([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle)[#](#_CPPv416hipsparseDestroy17hipsparseHandle_t) Destroy a hipsparse handle.

`hipsparseDestroy`

destroys the hipSPARSE library context and releases all resources used by the hipSPARSE library.

## hipsparseGetVersion()[#](#hipsparsegetversion)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseGetVersion([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int *version)[#](#_CPPv419hipsparseGetVersion17hipsparseHandle_tPi) Get hipSPARSE version.

`hipsparseGetVersion`

gets the hipSPARSE library version number.patch = version % 100

minor = version / 100 % 1000

major = version / 100000



## hipsparseGetGitRevision()[#](#hipsparsegetgitrevision)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseGetGitRevision([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, char *rev)[#](#_CPPv423hipsparseGetGitRevision17hipsparseHandle_tPc) Get hipSPARSE git revision.

`hipsparseGetGitRevision`

gets the hipSPARSE library git commit revision (SHA-1).

## hipsparseSetStream()[#](#hipsparsesetstream)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSetStream([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, hipStream_t streamId)[#](#_CPPv418hipsparseSetStream17hipsparseHandle_t11hipStream_t) Specify user defined HIP stream.

`hipsparseSetStream`

specifies the stream to be used by the hipSPARSE library context and all subsequent function calls.

## hipsparseGetStream()[#](#hipsparsegetstream)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseGetStream([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, hipStream_t *streamId)[#](#_CPPv418hipsparseGetStream17hipsparseHandle_tP11hipStream_t) Get current stream from library context.

`hipsparseGetStream`

gets the hipSPARSE library context stream which is currently used for all subsequent function calls.

## hipsparseSetPointerMode()[#](#hipsparsesetpointermode)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSetPointerMode([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparsePointerMode_t](types.html#_CPPv422hipsparsePointerMode_t)mode)[#](#_CPPv423hipsparseSetPointerMode17hipsparseHandle_t22hipsparsePointerMode_t) Specify pointer mode.

`hipsparseSetPointerMode`

specifies the pointer mode to be used by the hipSPARSE library context and all subsequent function calls. By default, all values are passed by reference on the host. Valid pointer modes are[HIPSPARSE_POINTER_MODE_HOST](types.html#hipsparse-types_8h_1a4aee6c92be9410c58c46d33cc4d14bc4ad86470ce2b41935086751f20c3e0a099)or[HIPSPARSE_POINTER_MODE_DEVICE](types.html#hipsparse-types_8h_1a4aee6c92be9410c58c46d33cc4d14bc4ad5736185eda0fe21455354aafe8437ea).

## hipsparseGetPointerMode()[#](#hipsparsegetpointermode)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseGetPointerMode([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparsePointerMode_t](types.html#_CPPv422hipsparsePointerMode_t)*mode)[#](#_CPPv423hipsparseGetPointerMode17hipsparseHandle_tP22hipsparsePointerMode_t) Get current pointer mode from library context.

`hipsparseGetPointerMode`

gets the hipSPARSE library context pointer mode which is currently used for all subsequent function calls.

## hipsparseCreateMatDescr()[#](#hipsparsecreatematdescr)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCreateMatDescr([hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)*descrA)[#](#_CPPv423hipsparseCreateMatDescrP19hipsparseMatDescr_t) Create a matrix descriptor.

`hipsparseCreateMatDescr`

creates a matrix descriptor. It initializes[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)to[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8)and[hipsparseIndexBase_t](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4)to[HIPSPARSE_INDEX_BASE_ZERO](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4a14913ab324aaea1154abd00ee7c50b63). It should be destroyed at the end using[hipsparseDestroyMatDescr()](#hipsparse-auxiliary_8h_1a21684bd690594fd8f98718eb3094f30b).

## hipsparseDestroyMatDescr()[#](#hipsparsedestroymatdescr)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDestroyMatDescr([hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA)[#](#_CPPv424hipsparseDestroyMatDescr19hipsparseMatDescr_t) Destroy a matrix descriptor.

`hipsparseDestroyMatDescr`

destroys a matrix descriptor and releases all resources used by the descriptor.

## hipsparseCopyMatDescr()[#](#hipsparsecopymatdescr)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCopyMatDescr([hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)dest, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)src)[#](#_CPPv421hipsparseCopyMatDescr19hipsparseMatDescr_tK19hipsparseMatDescr_t) Copy a matrix descriptor.

`hipsparseCopyMatDescr`

copies a matrix descriptor. Both, source and destination matrix descriptors must be initialized prior to calling`hipsparseCopyMatDescr`

.

## hipsparseSetMatType()[#](#hipsparsesetmattype)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSetMatType([hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA,[hipsparseMatrixType_t](types.html#_CPPv421hipsparseMatrixType_t)type)[#](#_CPPv419hipsparseSetMatType19hipsparseMatDescr_t21hipsparseMatrixType_t) Specify the matrix type of a matrix descriptor.

`hipsparseSetMatType`

sets the matrix type of a matrix descriptor. Valid matrix types are[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8),[HIPSPARSE_MATRIX_TYPE_SYMMETRIC](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8ba9b05c306a7141d32517cfe036f46bc15),[HIPSPARSE_MATRIX_TYPE_HERMITIAN](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8baff5fc1613efe652ddcb6b4f0a49bd8e8)or[HIPSPARSE_MATRIX_TYPE_TRIANGULAR](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8badebbc5ce9315f6e46e4a2534d44cc15f).

## hipsparseGetMatType()[#](#hipsparsegetmattype)

-
[hipsparseMatrixType_t](types.html#_CPPv421hipsparseMatrixType_t)hipsparseGetMatType(const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA)[#](#_CPPv419hipsparseGetMatTypeK19hipsparseMatDescr_t) Get the matrix type of a matrix descriptor.

`hipsparseGetMatType`

returns the matrix type of a matrix descriptor.

## hipsparseSetMatFillMode()[#](#hipsparsesetmatfillmode)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSetMatFillMode([hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA,[hipsparseFillMode_t](types.html#_CPPv419hipsparseFillMode_t)fillMode)[#](#_CPPv423hipsparseSetMatFillMode19hipsparseMatDescr_t19hipsparseFillMode_t) Specify the matrix fill mode of a matrix descriptor.

`hipsparseSetMatFillMode`

sets the matrix fill mode of a matrix descriptor. Valid fill modes are[HIPSPARSE_FILL_MODE_LOWER](types.html#hipsparse-types_8h_1ace47655e52ed1bb17309eda331c44332a470abb0661ab8951449efa6988ed49ef)or[HIPSPARSE_FILL_MODE_UPPER](types.html#hipsparse-types_8h_1ace47655e52ed1bb17309eda331c44332ac5c8ccc62dfff77c56c8480c24ed6b3b).

## hipsparseGetMatFillMode()[#](#hipsparsegetmatfillmode)

-
[hipsparseFillMode_t](types.html#_CPPv419hipsparseFillMode_t)hipsparseGetMatFillMode(const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA)[#](#_CPPv423hipsparseGetMatFillModeK19hipsparseMatDescr_t) Get the matrix fill mode of a matrix descriptor.

`hipsparseGetMatFillMode`

returns the matrix fill mode of a matrix descriptor.

## hipsparseSetMatDiagType()[#](#hipsparsesetmatdiagtype)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSetMatDiagType([hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA,[hipsparseDiagType_t](types.html#_CPPv419hipsparseDiagType_t)diagType)[#](#_CPPv423hipsparseSetMatDiagType19hipsparseMatDescr_t19hipsparseDiagType_t) Specify the matrix diagonal type of a matrix descriptor.

`hipsparseSetMatDiagType`

sets the matrix diagonal type of a matrix descriptor. Valid diagonal types are[HIPSPARSE_DIAG_TYPE_UNIT](types.html#hipsparse-types_8h_1a79e036b6c0680cb37e2aa53d3542a054a532a9a4a4eaf63a967bfaac7f9936b39)or[HIPSPARSE_DIAG_TYPE_NON_UNIT](types.html#hipsparse-types_8h_1a79e036b6c0680cb37e2aa53d3542a054acb2dc5d3da3b6e790f8bff22a17de72e).

## hipsparseGetMatDiagType()[#](#hipsparsegetmatdiagtype)

-
[hipsparseDiagType_t](types.html#_CPPv419hipsparseDiagType_t)hipsparseGetMatDiagType(const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA)[#](#_CPPv423hipsparseGetMatDiagTypeK19hipsparseMatDescr_t) Get the matrix diagonal type of a matrix descriptor.

`hipsparseGetMatDiagType`

returns the matrix diagonal type of a matrix descriptor.

## hipsparseSetMatIndexBase()[#](#hipsparsesetmatindexbase)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSetMatIndexBase([hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)base)[#](#_CPPv424hipsparseSetMatIndexBase19hipsparseMatDescr_t20hipsparseIndexBase_t) Specify the index base of a matrix descriptor.

`hipsparseSetMatIndexBase`

sets the index base of a matrix descriptor. Valid options are[HIPSPARSE_INDEX_BASE_ZERO](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4a14913ab324aaea1154abd00ee7c50b63)or[HIPSPARSE_INDEX_BASE_ONE](types.html#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4ae48a9ab138ca9588d485c078bddc0792).

## hipsparseGetMatIndexBase()[#](#hipsparsegetmatindexbase)

-
[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)hipsparseGetMatIndexBase(const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA)[#](#_CPPv424hipsparseGetMatIndexBaseK19hipsparseMatDescr_t) Get the index base of a matrix descriptor.

`hipsparseGetMatIndexBase`

returns the index base of a matrix descriptor.

## hipsparseCreateHybMat()[#](#hipsparsecreatehybmat)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCreateHybMat([hipsparseHybMat_t](types.html#_CPPv417hipsparseHybMat_t)*hybA)[#](#_CPPv421hipsparseCreateHybMatP17hipsparseHybMat_t) Create a

`HYB`

matrix structure.`hipsparseCreateHybMat`

creates a structure that holds the matrix in`HYB`

storage format. It should be destroyed at the end using[hipsparseDestroyHybMat()](#hipsparse-auxiliary_8h_1a1e97ab0183146de9e21d9dd8333d0a18).

## hipsparseDestroyHybMat()[#](#hipsparsedestroyhybmat)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDestroyHybMat([hipsparseHybMat_t](types.html#_CPPv417hipsparseHybMat_t)hybA)[#](#_CPPv422hipsparseDestroyHybMat17hipsparseHybMat_t) Destroy a

`HYB`

matrix structure.`hipsparseDestroyHybMat`

destroys a`HYB`

structure.

## hipsparseCreateBsrsv2Info()[#](#hipsparsecreatebsrsv2info)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCreateBsrsv2Info([bsrsv2Info_t](types.html#_CPPv412bsrsv2Info_t)*info)[#](#_CPPv425hipsparseCreateBsrsv2InfoP12bsrsv2Info_t) Create a bsrsv2 info structure.

`hipsparseCreateBsrsv2Info`

creates a structure that holds the bsrsv2 info data that is gathered during the analysis routines available. It should be destroyed at the end using[hipsparseDestroyBsrsv2Info()](#hipsparse-auxiliary_8h_1a841ac0ec43568a501db3fb2b656fff1b).

## hipsparseDestroyBsrsv2Info()[#](#hipsparsedestroybsrsv2info)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDestroyBsrsv2Info([bsrsv2Info_t](types.html#_CPPv412bsrsv2Info_t)info)[#](#_CPPv426hipsparseDestroyBsrsv2Info12bsrsv2Info_t) Destroy a bsrsv2 info structure.

`hipsparseDestroyBsrsv2Info`

destroys a bsrsv2 info structure.

## hipsparseCreateBsrsm2Info()[#](#hipsparsecreatebsrsm2info)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCreateBsrsm2Info([bsrsm2Info_t](types.html#_CPPv412bsrsm2Info_t)*info)[#](#_CPPv425hipsparseCreateBsrsm2InfoP12bsrsm2Info_t) Create a bsrsm2 info structure.

`hipsparseCreateBsrsm2Info`

creates a structure that holds the bsrsm2 info data that is gathered during the analysis routines available. It should be destroyed at the end using[hipsparseDestroyBsrsm2Info()](#hipsparse-auxiliary_8h_1a63ffdc1ecd67733ae40fe04d6889502d).

## hipsparseDestroyBsrsm2Info()[#](#hipsparsedestroybsrsm2info)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDestroyBsrsm2Info([bsrsm2Info_t](types.html#_CPPv412bsrsm2Info_t)info)[#](#_CPPv426hipsparseDestroyBsrsm2Info12bsrsm2Info_t) Destroy a bsrsm2 info structure.

`hipsparseDestroyBsrsm2Info`

destroys a bsrsm2 info structure.

## hipsparseCreateBsrilu02Info()[#](#hipsparsecreatebsrilu02info)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCreateBsrilu02Info([bsrilu02Info_t](types.html#_CPPv414bsrilu02Info_t)*info)[#](#_CPPv427hipsparseCreateBsrilu02InfoP14bsrilu02Info_t) Create a bsrilu02 info structure.

`hipsparseCreateBsrilu02Info`

creates a structure that holds the bsrilu02 info data that is gathered during the analysis routines available. It should be destroyed at the end using[hipsparseDestroyBsrilu02Info()](#hipsparse-auxiliary_8h_1ab33fdae0197dd03f61d4c5fd8e278bac).

## hipsparseDestroyBsrilu02Info()[#](#hipsparsedestroybsrilu02info)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDestroyBsrilu02Info([bsrilu02Info_t](types.html#_CPPv414bsrilu02Info_t)info)[#](#_CPPv428hipsparseDestroyBsrilu02Info14bsrilu02Info_t) Destroy a bsrilu02 info structure.

`hipsparseDestroyBsrilu02Info`

destroys a bsrilu02 info structure.

## hipsparseCreateBsric02Info()[#](#hipsparsecreatebsric02info)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCreateBsric02Info([bsric02Info_t](types.html#_CPPv413bsric02Info_t)*info)[#](#_CPPv426hipsparseCreateBsric02InfoP13bsric02Info_t) Create a bsric02 info structure.

`hipsparseCreateBsric02Info`

creates a structure that holds the bsric02 info data that is gathered during the analysis routines available. It should be destroyed at the end using[hipsparseDestroyBsric02Info()](#hipsparse-auxiliary_8h_1a2554df520ef427bd99c38414df1324ee).

## hipsparseDestroyBsric02Info()[#](#hipsparsedestroybsric02info)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDestroyBsric02Info([bsric02Info_t](types.html#_CPPv413bsric02Info_t)info)[#](#_CPPv427hipsparseDestroyBsric02Info13bsric02Info_t) Destroy a bsric02 info structure.

`hipsparseDestroyBsric02Info`

destroys a bsric02 info structure.

## hipsparseCreateCsrsv2Info()[#](#hipsparsecreatecsrsv2info)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCreateCsrsv2Info([csrsv2Info_t](types.html#_CPPv412csrsv2Info_t)*info)[#](#_CPPv425hipsparseCreateCsrsv2InfoP12csrsv2Info_t) Create a csrsv2 info structure.

`hipsparseCreateCsrsv2Info`

creates a structure that holds the csrsv2 info data that is gathered during the analysis routines available. It should be destroyed at the end using[hipsparseDestroyCsrsv2Info()](#hipsparse-auxiliary_8h_1a2aade2ef1590036d61764e52bd4d1b05).

## hipsparseDestroyCsrsv2Info()[#](#hipsparsedestroycsrsv2info)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDestroyCsrsv2Info([csrsv2Info_t](types.html#_CPPv412csrsv2Info_t)info)[#](#_CPPv426hipsparseDestroyCsrsv2Info12csrsv2Info_t) Destroy a csrsv2 info structure.

`hipsparseDestroyCsrsv2Info`

destroys a csrsv2 info structure.

## hipsparseCreateCsrsm2Info()[#](#hipsparsecreatecsrsm2info)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCreateCsrsm2Info([csrsm2Info_t](types.html#_CPPv412csrsm2Info_t)*info)[#](#_CPPv425hipsparseCreateCsrsm2InfoP12csrsm2Info_t) Create a csrsm2 info structure.

`hipsparseCreateCsrsm2Info`

creates a structure that holds the csrsm2 info data that is gathered during the analysis routines available. It should be destroyed at the end using[hipsparseDestroyCsrsm2Info()](#hipsparse-auxiliary_8h_1a54ce02e38d0514887788ac6964a21f1e).

## hipsparseDestroyCsrsm2Info()[#](#hipsparsedestroycsrsm2info)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDestroyCsrsm2Info([csrsm2Info_t](types.html#_CPPv412csrsm2Info_t)info)[#](#_CPPv426hipsparseDestroyCsrsm2Info12csrsm2Info_t) Destroy a csrsm2 info structure.

`hipsparseDestroyCsrsm2Info`

destroys a csrsm2 info structure.

## hipsparseCreateCsrilu02Info()[#](#hipsparsecreatecsrilu02info)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCreateCsrilu02Info([csrilu02Info_t](types.html#_CPPv414csrilu02Info_t)*info)[#](#_CPPv427hipsparseCreateCsrilu02InfoP14csrilu02Info_t) Create a csrilu02 info structure.

`hipsparseCreateCsrilu02Info`

creates a structure that holds the csrilu02 info data that is gathered during the analysis routines available. It should be destroyed at the end using[hipsparseDestroyCsrilu02Info()](#hipsparse-auxiliary_8h_1ada7faf2216e4bf9a4b2b37f8b621b343).

## hipsparseDestroyCsrilu02Info()[#](#hipsparsedestroycsrilu02info)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDestroyCsrilu02Info([csrilu02Info_t](types.html#_CPPv414csrilu02Info_t)info)[#](#_CPPv428hipsparseDestroyCsrilu02Info14csrilu02Info_t) Destroy a csrilu02 info structure.

`hipsparseDestroyCsrilu02Info`

destroys a csrilu02 info structure.

## hipsparseCreateCsric02Info()[#](#hipsparsecreatecsric02info)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCreateCsric02Info([csric02Info_t](types.html#_CPPv413csric02Info_t)*info)[#](#_CPPv426hipsparseCreateCsric02InfoP13csric02Info_t) Create a csric02 info structure.

`hipsparseCreateCsric02Info`

creates a structure that holds the csric02 info data that is gathered during the analysis routines available. It should be destroyed at the end using[hipsparseDestroyCsric02Info()](#hipsparse-auxiliary_8h_1a656fa4a86918b2f33db754aec7c692f9).

## hipsparseDestroyCsric02Info()[#](#hipsparsedestroycsric02info)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDestroyCsric02Info([csric02Info_t](types.html#_CPPv413csric02Info_t)info)[#](#_CPPv427hipsparseDestroyCsric02Info13csric02Info_t) Destroy a csric02 info structure.

`hipsparseDestroyCsric02Info`

destroys a csric02 info structure.

## hipsparseCreateCsru2csrInfo()[#](#hipsparsecreatecsru2csrinfo)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCreateCsru2csrInfo([csru2csrInfo_t](types.html#_CPPv414csru2csrInfo_t)*info)[#](#_CPPv427hipsparseCreateCsru2csrInfoP14csru2csrInfo_t) Create a csru2csr info structure.

`hipsparseCreateCsru2csrInfo`

creates a structure that holds the csru2csr info data that is gathered during the analysis routines available. It should be destroyed at the end using[hipsparseDestroyCsru2csrInfo()](#hipsparse-auxiliary_8h_1a910c7704054c8e51ea819af184a70abf).

## hipsparseDestroyCsru2csrInfo()[#](#hipsparsedestroycsru2csrinfo)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDestroyCsru2csrInfo([csru2csrInfo_t](types.html#_CPPv414csru2csrInfo_t)info)[#](#_CPPv428hipsparseDestroyCsru2csrInfo14csru2csrInfo_t) Destroy a csru2csr info structure.

`hipsparseDestroyCsru2csrInfo`

destroys a csru2csr info structure.

## hipsparseCreateColorInfo()[#](#hipsparsecreatecolorinfo)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCreateColorInfo([hipsparseColorInfo_t](types.html#_CPPv420hipsparseColorInfo_t)*info)[#](#_CPPv424hipsparseCreateColorInfoP20hipsparseColorInfo_t) Create a color info structure.

`hipsparseCreateColorInfo`

creates a structure that holds the color info data that is gathered during the analysis routines available. It should be destroyed at the end using[hipsparseDestroyColorInfo()](#hipsparse-auxiliary_8h_1a31e93a4d1e43a3bbc78ca0d04e9449c7).

## hipsparseDestroyColorInfo()[#](#hipsparsedestroycolorinfo)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDestroyColorInfo([hipsparseColorInfo_t](types.html#_CPPv420hipsparseColorInfo_t)info)[#](#_CPPv425hipsparseDestroyColorInfo20hipsparseColorInfo_t) Destroy a color info structure.

`hipsparseDestroyColorInfo`

destroys a color info structure.

## hipsparseCreateCsrgemm2Info()[#](#hipsparsecreatecsrgemm2info)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCreateCsrgemm2Info([csrgemm2Info_t](types.html#_CPPv414csrgemm2Info_t)*info)[#](#_CPPv427hipsparseCreateCsrgemm2InfoP14csrgemm2Info_t) Create a csrgemm2 info structure.

`hipsparseCreateCsrgemm2Info`

creates a structure that holds the csrgemm2 info data that is gathered during the analysis routines available. It should be destroyed at the end using[hipsparseDestroyCsrgemm2Info()](#hipsparse-auxiliary_8h_1a853e11e6f0282141bdb3957813f752f4).

## hipsparseDestroyCsrgemm2Info()[#](#hipsparsedestroycsrgemm2info)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDestroyCsrgemm2Info([csrgemm2Info_t](types.html#_CPPv414csrgemm2Info_t)info)[#](#_CPPv428hipsparseDestroyCsrgemm2Info14csrgemm2Info_t) Destroy a csrgemm2 info structure.

`hipsparseDestroyCsrgemm2Info`

destroys a csrgemm2 info structure.

## hipsparseCreatePruneInfo()[#](#hipsparsecreatepruneinfo)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCreatePruneInfo([pruneInfo_t](types.html#_CPPv411pruneInfo_t)*info)[#](#_CPPv424hipsparseCreatePruneInfoP11pruneInfo_t) Create a prune info structure.

`hipsparseCreatePruneInfo`

creates a structure that holds the prune info data that is gathered during the analysis routines available. It should be destroyed at the end using[hipsparseDestroyPruneInfo()](#hipsparse-auxiliary_8h_1ab497109423846bc1c4325a4e4a9d7b21).

## hipsparseDestroyPruneInfo()[#](#hipsparsedestroypruneinfo)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDestroyPruneInfo([pruneInfo_t](types.html#_CPPv411pruneInfo_t)info)[#](#_CPPv425hipsparseDestroyPruneInfo11pruneInfo_t) Destroy a prune info structure.

`hipsparseDestroyPruneInfo`

destroys a prune info structure.

## hipsparseCreateSpVec()[#](#hipsparsecreatespvec)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCreateSpVec([hipsparseSpVecDescr_t](types.html#_CPPv421hipsparseSpVecDescr_t)*spVecDescr, int64_t size, int64_t nnz, void *indices, void *values,[hipsparseIndexType_t](types.html#_CPPv420hipsparseIndexType_t)idxType,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase, hipDataType valueType)[#](#_CPPv420hipsparseCreateSpVecP21hipsparseSpVecDescr_t7int64_t7int64_tPvPv20hipsparseIndexType_t20hipsparseIndexBase_t11hipDataType) Create a sparse vector.

`hipsparseCreateSpVec`

creates a sparse vector descriptor. It should be destroyed at the end using[hipsparseDestroySpVec()](#hipsparse-generic-auxiliary_8h_1ac833153c10c06c6e349c5b11c6a9a549).

## hipsparseDestroySpVec()[#](#hipsparsedestroyspvec)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDestroySpVec(hipsparseConstSpVecDescr_t spVecDescr)[#](#_CPPv421hipsparseDestroySpVec26hipsparseConstSpVecDescr_t) Destroy a sparse vector.

`hipsparseDestroySpVec`

destroys a sparse vector descriptor and releases all resources used by the descriptor.

## hipsparseSpVecGet()[#](#hipsparsespvecget)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpVecGet(const[hipsparseSpVecDescr_t](types.html#_CPPv421hipsparseSpVecDescr_t)spVecDescr, int64_t *size, int64_t *nnz, void **indices, void **values,[hipsparseIndexType_t](types.html#_CPPv420hipsparseIndexType_t)*idxType,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)*idxBase, hipDataType *valueType)[#](#_CPPv417hipsparseSpVecGetK21hipsparseSpVecDescr_tP7int64_tP7int64_tPPvPPvP20hipsparseIndexType_tP20hipsparseIndexBase_tP11hipDataType) Get the fields of the sparse vector descriptor.

`hipsparseSpVecGet`

gets the fields of the sparse vector descriptor

## hipsparseSpVecGetIndexBase()[#](#hipsparsespvecgetindexbase)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpVecGetIndexBase(const hipsparseConstSpVecDescr_t spVecDescr,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)*idxBase)[#](#_CPPv426hipsparseSpVecGetIndexBaseK26hipsparseConstSpVecDescr_tP20hipsparseIndexBase_t) Get index base of a sparse vector.


## hipsparseSpVecGetValues()[#](#hipsparsespvecgetvalues)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpVecGetValues(const[hipsparseSpVecDescr_t](types.html#_CPPv421hipsparseSpVecDescr_t)spVecDescr, void **values)[#](#_CPPv423hipsparseSpVecGetValuesK21hipsparseSpVecDescr_tPPv) Get pointer to a sparse vector data array.


## hipsparseSpVecSetValues()[#](#hipsparsespvecsetvalues)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpVecSetValues([hipsparseSpVecDescr_t](types.html#_CPPv421hipsparseSpVecDescr_t)spVecDescr, void *values)[#](#_CPPv423hipsparseSpVecSetValues21hipsparseSpVecDescr_tPv) Set pointer of a sparse vector data array.


## hipsparseCreateCoo()[#](#hipsparsecreatecoo)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCreateCoo([hipsparseSpMatDescr_t](types.html#_CPPv421hipsparseSpMatDescr_t)*spMatDescr, int64_t rows, int64_t cols, int64_t nnz, void *cooRowInd, void *cooColInd, void *cooValues,[hipsparseIndexType_t](types.html#_CPPv420hipsparseIndexType_t)cooIdxType,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase, hipDataType valueType)[#](#_CPPv418hipsparseCreateCooP21hipsparseSpMatDescr_t7int64_t7int64_t7int64_tPvPvPv20hipsparseIndexType_t20hipsparseIndexBase_t11hipDataType) Create a sparse COO matrix descriptor.

`hipsparseCreateCoo`

creates a sparse COO matrix descriptor. It should be destroyed at the end using`hipsparseDestroySpMat`

.

## hipsparseCreateCooAoS()[#](#hipsparsecreatecooaos)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCreateCooAoS([hipsparseSpMatDescr_t](types.html#_CPPv421hipsparseSpMatDescr_t)*spMatDescr, int64_t rows, int64_t cols, int64_t nnz, void *cooInd, void *cooValues,[hipsparseIndexType_t](types.html#_CPPv420hipsparseIndexType_t)cooIdxType,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase, hipDataType valueType)[#](#_CPPv421hipsparseCreateCooAoSP21hipsparseSpMatDescr_t7int64_t7int64_t7int64_tPvPv20hipsparseIndexType_t20hipsparseIndexBase_t11hipDataType) Create a sparse COO (AoS) matrix descriptor.

`hipsparseCreateCooAoS`

creates a sparse COO (AoS) matrix descriptor. It should be destroyed at the end using`hipsparseDestroySpMat`

.

## hipsparseCreateCsr()[#](#hipsparsecreatecsr)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCreateCsr([hipsparseSpMatDescr_t](types.html#_CPPv421hipsparseSpMatDescr_t)*spMatDescr, int64_t rows, int64_t cols, int64_t nnz, void *csrRowOffsets, void *csrColInd, void *csrValues,[hipsparseIndexType_t](types.html#_CPPv420hipsparseIndexType_t)csrRowOffsetsType,[hipsparseIndexType_t](types.html#_CPPv420hipsparseIndexType_t)csrColIndType,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase, hipDataType valueType)[#](#_CPPv418hipsparseCreateCsrP21hipsparseSpMatDescr_t7int64_t7int64_t7int64_tPvPvPv20hipsparseIndexType_t20hipsparseIndexType_t20hipsparseIndexBase_t11hipDataType) Create a sparse CSR matrix descriptor.

`hipsparseCreateCsr`

creates a sparse CSR matrix descriptor. It should be destroyed at the end using`hipsparseDestroySpMat`

.

## hipsparseCreateCsc()[#](#hipsparsecreatecsc)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCreateCsc([hipsparseSpMatDescr_t](types.html#_CPPv421hipsparseSpMatDescr_t)*spMatDescr, int64_t rows, int64_t cols, int64_t nnz, void *cscColOffsets, void *cscRowInd, void *cscValues,[hipsparseIndexType_t](types.html#_CPPv420hipsparseIndexType_t)cscColOffsetsType,[hipsparseIndexType_t](types.html#_CPPv420hipsparseIndexType_t)cscRowIndType,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase, hipDataType valueType)[#](#_CPPv418hipsparseCreateCscP21hipsparseSpMatDescr_t7int64_t7int64_t7int64_tPvPvPv20hipsparseIndexType_t20hipsparseIndexType_t20hipsparseIndexBase_t11hipDataType) Create a sparse CSC matrix descriptor.

`hipsparseCreateCsc`

creates a sparse CSC matrix descriptor. It should be destroyed at the end using`hipsparseDestroySpMat`

.

## hipsparseCreateBlockedEll()[#](#hipsparsecreateblockedell)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCreateBlockedEll([hipsparseSpMatDescr_t](types.html#_CPPv421hipsparseSpMatDescr_t)*spMatDescr, int64_t rows, int64_t cols, int64_t ellBlockSize, int64_t ellCols, void *ellColInd, void *ellValue,[hipsparseIndexType_t](types.html#_CPPv420hipsparseIndexType_t)ellIdxType,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)idxBase, hipDataType valueType)[#](#_CPPv425hipsparseCreateBlockedEllP21hipsparseSpMatDescr_t7int64_t7int64_t7int64_t7int64_tPvPv20hipsparseIndexType_t20hipsparseIndexBase_t11hipDataType) Create a sparse Blocked ELL matrix descriptor.

`hipsparseCreateCsr`

creates a sparse Blocked ELL matrix descriptor. It should be destroyed at the end using`hipsparseDestroySpMat`

.

## hipsparseDestroySpMat()[#](#hipsparsedestroyspmat)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDestroySpMat(hipsparseConstSpMatDescr_t spMatDescr)[#](#_CPPv421hipsparseDestroySpMat26hipsparseConstSpMatDescr_t) Destroy a sparse matrix descriptor.

`hipsparseDestroySpMat`

destroys a sparse matrix descriptor and releases all resources used by the descriptor.

## hipsparseCooGet()[#](#hipsparsecooget)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCooGet(const[hipsparseSpMatDescr_t](types.html#_CPPv421hipsparseSpMatDescr_t)spMatDescr, int64_t *rows, int64_t *cols, int64_t *nnz, void **cooRowInd, void **cooColInd, void **cooValues,[hipsparseIndexType_t](types.html#_CPPv420hipsparseIndexType_t)*idxType,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)*idxBase, hipDataType *valueType)[#](#_CPPv415hipsparseCooGetK21hipsparseSpMatDescr_tP7int64_tP7int64_tP7int64_tPPvPPvPPvP20hipsparseIndexType_tP20hipsparseIndexBase_tP11hipDataType) Get pointers of a sparse COO matrix.

`hipsparseCooGet`

gets the fields of the sparse COO matrix descriptor

## hipsparseCooAoSGet()[#](#hipsparsecooaosget)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCooAoSGet(const[hipsparseSpMatDescr_t](types.html#_CPPv421hipsparseSpMatDescr_t)spMatDescr, int64_t *rows, int64_t *cols, int64_t *nnz, void **cooInd, void **cooValues,[hipsparseIndexType_t](types.html#_CPPv420hipsparseIndexType_t)*idxType,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)*idxBase, hipDataType *valueType)[#](#_CPPv418hipsparseCooAoSGetK21hipsparseSpMatDescr_tP7int64_tP7int64_tP7int64_tPPvPPvP20hipsparseIndexType_tP20hipsparseIndexBase_tP11hipDataType) Get pointers of a sparse COO (AoS) matrix.

`hipsparseCooAoSGet`

gets the fields of the sparse COO (AoS) matrix descriptor

## hipsparseCsrGet()[#](#hipsparsecsrget)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCsrGet(const[hipsparseSpMatDescr_t](types.html#_CPPv421hipsparseSpMatDescr_t)spMatDescr, int64_t *rows, int64_t *cols, int64_t *nnz, void **csrRowOffsets, void **csrColInd, void **csrValues,[hipsparseIndexType_t](types.html#_CPPv420hipsparseIndexType_t)*csrRowOffsetsType,[hipsparseIndexType_t](types.html#_CPPv420hipsparseIndexType_t)*csrColIndType,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)*idxBase, hipDataType *valueType)[#](#_CPPv415hipsparseCsrGetK21hipsparseSpMatDescr_tP7int64_tP7int64_tP7int64_tPPvPPvPPvP20hipsparseIndexType_tP20hipsparseIndexType_tP20hipsparseIndexBase_tP11hipDataType) Get pointers of a sparse CSR matrix.

`hipsparseCsrGet`

gets the fields of the sparse CSR matrix descriptor

## hipsparseBlockedEllGet()[#](#hipsparseblockedellget)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseBlockedEllGet(const[hipsparseSpMatDescr_t](types.html#_CPPv421hipsparseSpMatDescr_t)spMatDescr, int64_t *rows, int64_t *cols, int64_t *ellBlockSize, int64_t *ellCols, void **ellColInd, void **ellValue,[hipsparseIndexType_t](types.html#_CPPv420hipsparseIndexType_t)*ellIdxType,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)*idxBase, hipDataType *valueType)[#](#_CPPv422hipsparseBlockedEllGetK21hipsparseSpMatDescr_tP7int64_tP7int64_tP7int64_tP7int64_tPPvPPvP20hipsparseIndexType_tP20hipsparseIndexBase_tP11hipDataType) Get pointers of a sparse blocked ELL matrix.

`hipsparseBlockedEllGet`

gets the fields of the sparse blocked ELL matrix descriptor

## hipsparseCsrSetPointers()[#](#hipsparsecsrsetpointers)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCsrSetPointers([hipsparseSpMatDescr_t](types.html#_CPPv421hipsparseSpMatDescr_t)spMatDescr, void *csrRowOffsets, void *csrColInd, void *csrValues)[#](#_CPPv423hipsparseCsrSetPointers21hipsparseSpMatDescr_tPvPvPv) Set pointers of a sparse CSR matrix.

`hipsparseCsrSetPointers`

sets the fields of the sparse CSR matrix descriptor

## hipsparseCscSetPointers()[#](#hipsparsecscsetpointers)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCscSetPointers([hipsparseSpMatDescr_t](types.html#_CPPv421hipsparseSpMatDescr_t)spMatDescr, void *cscColOffsets, void *cscRowInd, void *cscValues)[#](#_CPPv423hipsparseCscSetPointers21hipsparseSpMatDescr_tPvPvPv) Set pointers of a sparse CSC matrix.

`hipsparseCscSetPointers`

sets the fields of the sparse CSC matrix descriptor

## hipsparseCooSetPointers()[#](#hipsparsecoosetpointers)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCooSetPointers([hipsparseSpMatDescr_t](types.html#_CPPv421hipsparseSpMatDescr_t)spMatDescr, void *cooRowInd, void *cooColInd, void *cooValues)[#](#_CPPv423hipsparseCooSetPointers21hipsparseSpMatDescr_tPvPvPv) Set pointers of a sparse COO matrix.

`hipsparseCooSetPointers`

sets the fields of the sparse COO matrix descriptor

## hipsparseSpMatGetSize()[#](#hipsparsespmatgetsize)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpMatGetSize(hipsparseConstSpMatDescr_t spMatDescr, int64_t *rows, int64_t *cols, int64_t *nnz)[#](#_CPPv421hipsparseSpMatGetSize26hipsparseConstSpMatDescr_tP7int64_tP7int64_tP7int64_t) Get the sizes of a sparse matrix.


## hipsparseSpMatGetFormat()[#](#hipsparsespmatgetformat)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpMatGetFormat(hipsparseConstSpMatDescr_t spMatDescr,[hipsparseFormat_t](types.html#_CPPv417hipsparseFormat_t)*format)[#](#_CPPv423hipsparseSpMatGetFormat26hipsparseConstSpMatDescr_tP17hipsparseFormat_t) Get the format of a sparse matrix.


## hipsparseSpMatGetIndexBase()[#](#hipsparsespmatgetindexbase)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpMatGetIndexBase(hipsparseConstSpMatDescr_t spMatDescr,[hipsparseIndexBase_t](types.html#_CPPv420hipsparseIndexBase_t)*idxBase)[#](#_CPPv426hipsparseSpMatGetIndexBase26hipsparseConstSpMatDescr_tP20hipsparseIndexBase_t) Get the index base of a sparse matrix.


## hipsparseSpMatGetValues()[#](#hipsparsespmatgetvalues)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpMatGetValues([hipsparseSpMatDescr_t](types.html#_CPPv421hipsparseSpMatDescr_t)spMatDescr, void **values)[#](#_CPPv423hipsparseSpMatGetValues21hipsparseSpMatDescr_tPPv) Get the pointer of the values array of a sparse matrix.


## hipsparseSpMatSetValues()[#](#hipsparsespmatsetvalues)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpMatSetValues([hipsparseSpMatDescr_t](types.html#_CPPv421hipsparseSpMatDescr_t)spMatDescr, void *values)[#](#_CPPv423hipsparseSpMatSetValues21hipsparseSpMatDescr_tPv) Set the pointer of the values array of a sparse matrix.


## hipsparseSpMatGetAttribute()[#](#hipsparsespmatgetattribute)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpMatGetAttribute(hipsparseConstSpMatDescr_t spMatDescr,[hipsparseSpMatAttribute_t](types.html#_CPPv425hipsparseSpMatAttribute_t)attribute, void *data, size_t dataSize)[#](#_CPPv426hipsparseSpMatGetAttribute26hipsparseConstSpMatDescr_t25hipsparseSpMatAttribute_tPv6size_t) Get attribute from sparse matrix descriptor.


## hipsparseSpMatSetAttribute()[#](#hipsparsespmatsetattribute)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSpMatSetAttribute([hipsparseSpMatDescr_t](types.html#_CPPv421hipsparseSpMatDescr_t)spMatDescr,[hipsparseSpMatAttribute_t](types.html#_CPPv425hipsparseSpMatAttribute_t)attribute, const void *data, size_t dataSize)[#](#_CPPv426hipsparseSpMatSetAttribute21hipsparseSpMatDescr_t25hipsparseSpMatAttribute_tPKv6size_t) Set attribute in sparse matrix descriptor.


## hipsparseCreateDnVec()[#](#hipsparsecreatednvec)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCreateDnVec([hipsparseDnVecDescr_t](types.html#_CPPv421hipsparseDnVecDescr_t)*dnVecDescr, int64_t size, void *values, hipDataType valueType)[#](#_CPPv420hipsparseCreateDnVecP21hipsparseDnVecDescr_t7int64_tPv11hipDataType) Create dense vector.

`hipsparseCreateDnVec`

creates a dense vector descriptor. It should be destroyed at the end using[hipsparseDestroyDnVec()](#hipsparse-generic-auxiliary_8h_1abe2ba87d1ba1ba7d4ca2e6af0c870565).

## hipsparseDestroyDnVec()[#](#hipsparsedestroydnvec)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDestroyDnVec(hipsparseConstDnVecDescr_t dnVecDescr)[#](#_CPPv421hipsparseDestroyDnVec26hipsparseConstDnVecDescr_t) Destroy dense vector.

`hipsparseDestroyDnVec`

destroys a dense vector descriptor and releases all resources used by the descriptor.

## hipsparseDnVecGet()[#](#hipsparsednvecget)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDnVecGet(const[hipsparseDnVecDescr_t](types.html#_CPPv421hipsparseDnVecDescr_t)dnVecDescr, int64_t *size, void **values, hipDataType *valueType)[#](#_CPPv417hipsparseDnVecGetK21hipsparseDnVecDescr_tP7int64_tPPvP11hipDataType) Get the fields from a dense vector.

`hipsparseDnVecGet`

gets the fields of the dense vector descriptor

## hipsparseDnVecGetValues()[#](#hipsparsednvecgetvalues)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDnVecGetValues(const[hipsparseDnVecDescr_t](types.html#_CPPv421hipsparseDnVecDescr_t)dnVecDescr, void **values)[#](#_CPPv423hipsparseDnVecGetValuesK21hipsparseDnVecDescr_tPPv) Get value pointer from a dense vector.

`hipsparseDnVecGetValues`

gets the fields of the dense vector descriptor

## hipsparseDnVecSetValues()[#](#hipsparsednvecsetvalues)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDnVecSetValues([hipsparseDnVecDescr_t](types.html#_CPPv421hipsparseDnVecDescr_t)dnVecDescr, void *values)[#](#_CPPv423hipsparseDnVecSetValues21hipsparseDnVecDescr_tPv) Set value pointer of a dense vector.

`hipsparseDnVecSetValues`

sets the fields of the dense vector descriptor

## hipsparseCreateDnMat()[#](#hipsparsecreatednmat)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCreateDnMat([hipsparseDnMatDescr_t](types.html#_CPPv421hipsparseDnMatDescr_t)*dnMatDescr, int64_t rows, int64_t cols, int64_t ld, void *values, hipDataType valueType,[hipsparseOrder_t](types.html#_CPPv416hipsparseOrder_t)order)[#](#_CPPv420hipsparseCreateDnMatP21hipsparseDnMatDescr_t7int64_t7int64_t7int64_tPv11hipDataType16hipsparseOrder_t) Create dense matrix.

`hipsparseCreateDnMat`

creates a dense matrix descriptor. It should be destroyed at the end using[hipsparseDestroyDnMat()](#hipsparse-generic-auxiliary_8h_1ab364f0605fcb79337045a7782cadaaec).

## hipsparseDestroyDnMat()[#](#hipsparsedestroydnmat)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDestroyDnMat(hipsparseConstDnMatDescr_t dnMatDescr)[#](#_CPPv421hipsparseDestroyDnMat26hipsparseConstDnMatDescr_t) Destroy dense matrix.

`hipsparseDestroyDnMat`

destroys a dense matrix descriptor and releases all resources used by the descriptor.

## hipsparseDnMatGet()[#](#hipsparsednmatget)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDnMatGet(const[hipsparseDnMatDescr_t](types.html#_CPPv421hipsparseDnMatDescr_t)dnMatDescr, int64_t *rows, int64_t *cols, int64_t *ld, void **values, hipDataType *valueType,[hipsparseOrder_t](types.html#_CPPv416hipsparseOrder_t)*order)[#](#_CPPv417hipsparseDnMatGetK21hipsparseDnMatDescr_tP7int64_tP7int64_tP7int64_tPPvP11hipDataTypeP16hipsparseOrder_t) Get fields from a dense matrix.


## hipsparseDnMatGetValues()[#](#hipsparsednmatgetvalues)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDnMatGetValues(const[hipsparseDnMatDescr_t](types.html#_CPPv421hipsparseDnMatDescr_t)dnMatDescr, void **values)[#](#_CPPv423hipsparseDnMatGetValuesK21hipsparseDnMatDescr_tPPv) Get value pointer from a dense matrix.


## hipsparseDnMatSetValues()[#](#hipsparsednmatsetvalues)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDnMatSetValues([hipsparseDnMatDescr_t](types.html#_CPPv421hipsparseDnMatDescr_t)dnMatDescr, void *values)[#](#_CPPv423hipsparseDnMatSetValues21hipsparseDnMatDescr_tPv) Set value pointer of a dense matrix.
