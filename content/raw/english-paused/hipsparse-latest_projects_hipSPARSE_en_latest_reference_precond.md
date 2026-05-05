---
title: "Preconditioner functions &#8212; hipSPARSE 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipSPARSE/en/latest/reference/precond.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:09:59.788358+00:00
content_hash: "81fa18848e9c229e"
---

# Preconditioner functions[#](#preconditioner-functions)

This module contains all sparse preconditioners.

The sparse preconditioners describe manipulations on a matrix in sparse format to obtain a sparse preconditioner matrix.

## hipsparseXbsrilu02_zeroPivot()[#](#hipsparsexbsrilu02-zeropivot)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseXbsrilu02_zeroPivot([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[bsrilu02Info_t](types.html#_CPPv414bsrilu02Info_t)info, int *position)[#](#_CPPv428hipsparseXbsrilu02_zeroPivot17hipsparseHandle_t14bsrilu02Info_tPi) `hipsparseXbsrilu02_zeroPivot`

returns[HIPSPARSE_STATUS_ZERO_PIVOT](types.html#hipsparse-types_8h_1aa069bec7a4f24d00dab1dc4612d4de79a88ff0f0537dfe037fcf9f99ff0cf79da), if either a structural or numerical zero has been found during[hipsparseXbsrilu02_analysis()](#hipsparse__bsrilu0_8h_1a47d4addbbfeb087b1050a3b1a6c11b56)or[hipsparseXbsrilu02()](#hipsparse__bsrilu0_8h_1a79aa95847c1439cba4250be3ac0460e3)computation. The first zero pivot \(j\) at \(A_{j,j}\) is stored in`position`

, using same index base as the BSR matrix.`position`

can be in host or device memory. If no zero pivot has been found,`position`

is set to -1 and[HIPSPARSE_STATUS_SUCCESS](types.html#hipsparse-types_8h_1aa069bec7a4f24d00dab1dc4612d4de79a146a8a2fd27ee49132f8dcea617fc481)is returned instead.Note

If a zero pivot is found,

`position`

\(=j\) means that either the diagonal block \(A_{j,j}\) is missing (structural zero) or the diagonal block \(A_{j,j}\) is not invertible (numerical zero).Note

`hipsparseXbsrilu02_zeroPivot`

is a blocking function. It might influence performance negatively.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**info**–**[in]**structure that holds the information collected during the analysis step.**position**–**[inout]**pointer to zero pivot \(j\), can be in host or device memory.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`info`

or`position`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.**HIPSPARSE_STATUS_ZERO_PIVOT**– zero pivot has been found.



## hipsparseXbsrilu02_numericBoost()[#](#hipsparsexbsrilu02-numericboost)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSbsrilu02_numericBoost([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[bsrilu02Info_t](types.html#_CPPv414bsrilu02Info_t)info, int enable_boost, double *tol, float *boost_val)[#](#_CPPv431hipsparseSbsrilu02_numericBoost17hipsparseHandle_t14bsrilu02Info_tiPdPf)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDbsrilu02_numericBoost([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[bsrilu02Info_t](types.html#_CPPv414bsrilu02Info_t)info, int enable_boost, double *tol, double *boost_val)[#](#_CPPv431hipsparseDbsrilu02_numericBoost17hipsparseHandle_t14bsrilu02Info_tiPdPd)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCbsrilu02_numericBoost([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[bsrilu02Info_t](types.html#_CPPv414bsrilu02Info_t)info, int enable_boost, double *tol, hipComplex *boost_val)[#](#_CPPv431hipsparseCbsrilu02_numericBoost17hipsparseHandle_t14bsrilu02Info_tiPdP10hipComplex)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZbsrilu02_numericBoost([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[bsrilu02Info_t](types.html#_CPPv414bsrilu02Info_t)info, int enable_boost, double *tol, hipDoubleComplex *boost_val)[#](#_CPPv431hipsparseZbsrilu02_numericBoost17hipsparseHandle_t14bsrilu02Info_tiPdP16hipDoubleComplex) `hipsparseXbsrilu02_numericBoost`

enables the user to replace a numerical value in an incomplete LU factorization.`tol`

is used to determine whether a numerical value is replaced by`boost_val`

, such that \(A_{j,j} = \text{boost_val}\) if \(\text{tol} \ge \left|A_{j,j}\right|\).Note

The boost value is enabled by setting

`enable_boost`

to 1 or disabled by setting`enable_boost`

to 0.Note

`tol`

and`boost_val`

can be in host or device memory.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**info**–**[in]**structure that holds the information collected during the analysis step.**enable_boost**–**[in]**enable/disable numeric boost.**tol**–**[in]**tolerance to determine whether a numerical value is replaced or not.**boost_val**–**[in]**boost value to replace a numerical value.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`info`

,`tol`

or`boost_val`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.



## hipsparseXbsrilu02_bufferSize()[#](#hipsparsexbsrilu02-buffersize)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSbsrilu02_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, float *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrilu02Info_t](types.html#_CPPv414bsrilu02Info_t)info, int *pBufferSizeInBytes)[#](#_CPPv429hipsparseSbsrilu02_bufferSize17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPfPKiPKii14bsrilu02Info_tPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDbsrilu02_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, double *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrilu02Info_t](types.html#_CPPv414bsrilu02Info_t)info, int *pBufferSizeInBytes)[#](#_CPPv429hipsparseDbsrilu02_bufferSize17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPdPKiPKii14bsrilu02Info_tPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCbsrilu02_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, hipComplex *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrilu02Info_t](types.html#_CPPv414bsrilu02Info_t)info, int *pBufferSizeInBytes)[#](#_CPPv429hipsparseCbsrilu02_bufferSize17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tP10hipComplexPKiPKii14bsrilu02Info_tPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZbsrilu02_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, hipDoubleComplex *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrilu02Info_t](types.html#_CPPv414bsrilu02Info_t)info, int *pBufferSizeInBytes)[#](#_CPPv429hipsparseZbsrilu02_bufferSize17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tP16hipDoubleComplexPKiPKii14bsrilu02Info_tPi) `hipsparseXbsrilu02_bufferSize`

returns the size of the temporary storage buffer in bytes that is required by[hipsparseXbsrilu02_analysis()](#hipsparse__bsrilu0_8h_1a47d4addbbfeb087b1050a3b1a6c11b56)and[hipsparseXbsrilu02()](#hipsparse__bsrilu0_8h_1a79aa95847c1439cba4250be3ac0460e3). The temporary storage buffer must be allocated by the user.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**dirA**–**[in]**direction that specifies whether to count nonzero elements by[HIPSPARSE_DIRECTION_ROW](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59ae8589abecf2fbfb4b6307fd9dacd9e55)or by[HIPSPARSE_DIRECTION_COLUMN](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59a32e23f292b2377f6e60bdc90274c796c).**mb**–**[in]**number of block rows in the sparse BSR matrix.**nnzb**–**[in]**number of non-zero block entries of the sparse BSR matrix.**descrA**–**[in]**descriptor of the sparse BSR matrix.**bsrSortedValA**–**[in]**array of length`nnzb*blockDim*blockDim`

containing the values of the sparse BSR matrix.**bsrSortedRowPtrA**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix.**bsrSortedColIndA**–**[in]**array of`nnzb`

elements containing the block column indices of the sparse BSR matrix.**blockDim**–**[in]**the block dimension of the BSR matrix. Between 1 and m where`m=mb*blockDim`

.**info**–**[out]**structure that holds the information collected during the analysis step.**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer required by[hipsparseSbsrilu02_analysis()](#hipsparse__bsrilu0_8h_1a47d4addbbfeb087b1050a3b1a6c11b56),[hipsparseDbsrilu02_analysis()](#hipsparse__bsrilu0_8h_1abfcb456cf859fd04f147e1420f3f5a17),[hipsparseCbsrilu02_analysis()](#hipsparse__bsrilu0_8h_1a14348a494fef58e587bf76be3181f916),[hipsparseZbsrilu02_analysis()](#hipsparse__bsrilu0_8h_1a90e3c8425bddad6e4908a252525f5b67),[hipsparseSbsrilu02()](#hipsparse__bsrilu0_8h_1a79aa95847c1439cba4250be3ac0460e3),[hipsparseDbsrilu02()](#hipsparse__bsrilu0_8h_1a23452d0e0e96ef994100ee7e18044f71),[hipsparseCbsrilu02()](#hipsparse__bsrilu0_8h_1a3079756bb5dee0abe8c41856de70c8c5)and[hipsparseZbsrilu02()](#hipsparse__bsrilu0_8h_1a71f3144dffdd83341ecdcb695e04b54f).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`mb`

,`nnzb`

,`blockDim`

,`descrA`

,`bsrSortedValA`

,`bsrSortedRowPtrA`

,`bsrSortedColIndA`

,`info`

or`pBufferSizeInBytes`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.**HIPSPARSE_STATUS_NOT_SUPPORTED**–[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXbsrilu02_analysis()[#](#hipsparsexbsrilu02-analysis)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSbsrilu02_analysis([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, float *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrilu02Info_t](types.html#_CPPv414bsrilu02Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv427hipsparseSbsrilu02_analysis17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPfPKiPKii14bsrilu02Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDbsrilu02_analysis([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, double *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrilu02Info_t](types.html#_CPPv414bsrilu02Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv427hipsparseDbsrilu02_analysis17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPdPKiPKii14bsrilu02Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCbsrilu02_analysis([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, hipComplex *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrilu02Info_t](types.html#_CPPv414bsrilu02Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv427hipsparseCbsrilu02_analysis17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tP10hipComplexPKiPKii14bsrilu02Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZbsrilu02_analysis([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, hipDoubleComplex *bsrSortedValA, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrilu02Info_t](types.html#_CPPv414bsrilu02Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv427hipsparseZbsrilu02_analysis17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tP16hipDoubleComplexPKiPKii14bsrilu02Info_t22hipsparseSolvePolicy_tPv) `hipsparseXbsrilu02_analysis`

performs the analysis step for[hipsparseXbsrilu02()](#hipsparse__bsrilu0_8h_1a79aa95847c1439cba4250be3ac0460e3). It is expected that this function will be executed only once for a given matrix.Note

If the matrix sparsity pattern changes, the gathered information will become invalid.

Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**dirA**–**[in]**direction that specified whether to count nonzero elements by[HIPSPARSE_DIRECTION_ROW](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59ae8589abecf2fbfb4b6307fd9dacd9e55)or by[HIPSPARSE_DIRECTION_COLUMN](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59a32e23f292b2377f6e60bdc90274c796c).**mb**–**[in]**number of block rows in the sparse BSR matrix.**nnzb**–**[in]**number of non-zero block entries of the sparse BSR matrix.**descrA**–**[in]**descriptor of the sparse BSR matrix.**bsrSortedValA**–**[in]**array of length`nnzb*blockDim*blockDim`

containing the values of the sparse BSR matrix.**bsrSortedRowPtrA**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix.**bsrSortedColIndA**–**[in]**array of`nnzb`

elements containing the block column indices of the sparse BSR matrix.**blockDim**–**[in]**the block dimension of the BSR matrix. Between 1 and m where`m=mb*blockDim`

.**info**–**[out]**structure that holds the information collected during the analysis step.**policy**–**[in]**[HIPSPARSE_SOLVE_POLICY_NO_LEVEL](types.html#hipsparse-types_8h_1a0d98e490c94d4facc231db60baf1c3b3ac5830aa96848e832b3b375ad08abdb09)or[HIPSPARSE_SOLVE_POLICY_USE_LEVEL](types.html#hipsparse-types_8h_1a0d98e490c94d4facc231db60baf1c3b3a934309d6656638e375f0759b89fd81b5).**pBuffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`mb`

,`nnzb`

,`blockDim`

,`descrA`

,`bsrSortedValA`

,`bsrSortedRowPtrA`

,`bsrSortedColIndA`

,`info`

or`pBuffer`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.**HIPSPARSE_STATUS_NOT_SUPPORTED**–[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXbsrilu02()[#](#hipsparsexbsrilu02)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSbsrilu02([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, float *bsrSortedValA_valM, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrilu02Info_t](types.html#_CPPv414bsrilu02Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv418hipsparseSbsrilu0217hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPfPKiPKii14bsrilu02Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDbsrilu02([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, double *bsrSortedValA_valM, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrilu02Info_t](types.html#_CPPv414bsrilu02Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv418hipsparseDbsrilu0217hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPdPKiPKii14bsrilu02Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCbsrilu02([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, hipComplex *bsrSortedValA_valM, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrilu02Info_t](types.html#_CPPv414bsrilu02Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv418hipsparseCbsrilu0217hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tP10hipComplexPKiPKii14bsrilu02Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZbsrilu02([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, hipDoubleComplex *bsrSortedValA_valM, const int *bsrSortedRowPtrA, const int *bsrSortedColIndA, int blockDim,[bsrilu02Info_t](types.html#_CPPv414bsrilu02Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv418hipsparseZbsrilu0217hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tP16hipDoubleComplexPKiPKii14bsrilu02Info_t22hipsparseSolvePolicy_tPv) Incomplete LU factorization with 0 fill-ins and no pivoting using BSR storage format.

`hipsparseXbsrilu02`

computes the incomplete LU factorization with 0 fill-ins and no pivoting of a sparse \(mb \times mb\) BSR matrix \(A\), such that\[ A \approx LU \]Computing the above incomplete LU factorization requires three steps to complete. First, the user determines the size of the required temporary storage buffer by calling

[hipsparseXbsrilu02_bufferSize()](#hipsparse__bsrilu0_8h_1a8efe2b2ba788104b397bbe5ab75cce8d). Once this buffer size has been determined, the user allocates the buffer and passes it to[hipsparseXbsrilu02_analysis()](#hipsparse__bsrilu0_8h_1a47d4addbbfeb087b1050a3b1a6c11b56). This will perform analysis on the sparsity pattern of the matrix. Finally, the user calls`hipsparseXbsrilu02`

to perform the actual factorization. The calculation of the buffer size and the analysis of the sparse matrix only need to be performed once for a given sparsity pattern while the factorization can be repeatedly applied to multiple matrices having the same sparsity pattern. Once all calls to[hipsparseXbsrilu02()](#hipsparse__bsrilu0_8h_1a79aa95847c1439cba4250be3ac0460e3)are complete, the temporary buffer can be deallocated.`hipsparseXbsrilu02`

reports the first zero pivot (either numerical or structural zero). The zero pivot status can be obtained by calling[hipsparseXbsrilu02_zeroPivot()](#hipsparse__bsrilu0_8h_1a53831a4fbf7559ddd3efed860ff8e79f).**Example**int main(int argc, char* argv[]) { // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // A sample square matrix A (4x4) in BSR format for ILU(0) factorization. // The 'S' in Sbsrilu02 indicates single precision float. // We'll use a block size of 1 for simplicity, making it behave like CSR ILU. // Matrix A: // ( 1 2 0 0 ) // ( 3 4 5 0 ) // ( 0 6 7 8 ) // ( 0 0 9 10 ) int m = 4; // Number of rows int n = 4; // Number of columns int bs = 1; // Block size int mb = m / bs; // Number of block rows int nb = n / bs; // Number of block columns int nnzb = 10; // Number of non-zero blocks // BSR row pointers int hbsrRowPtr[5] = {0, 2, 5, 8, 10}; // BSR column indices int hbsrColInd[10] = {0, 1, 0, 1, 2, 1, 2, 3, 2, 3}; // BSR values (single precision float) float hbsrVal[10] = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f, 9.0f, 10.0f}; // Matrix descriptor hipsparseMatDescr_t descr; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&descr)); // Set index base on descriptor HIPSPARSE_CHECK(hipsparseSetMatIndexBase(descr, HIPSPARSE_INDEX_BASE_ZERO)); // For ILU(0), the L factor often has a unit diagonal. HIPSPARSE_CHECK(hipsparseSetMatDiagType(descr, HIPSPARSE_DIAG_TYPE_UNIT)); // BSRILU02 info bsrilu02Info_t info; HIPSPARSE_CHECK(hipsparseCreateBsrilu02Info(&info)); // Offload data to device int* dbsrRowPtr; int* dbsrColInd; float* dbsrVal; // This will store the factorized L and U values HIP_CHECK(hipMalloc((void**)&dbsrRowPtr, sizeof(int) * (mb + 1))); HIP_CHECK(hipMalloc((void**)&dbsrColInd, sizeof(int) * nnzb)); HIP_CHECK(hipMalloc((void**)&dbsrVal, sizeof(float) * nnzb * bs * bs)); HIP_CHECK(hipMemcpy(dbsrRowPtr, hbsrRowPtr, sizeof(int) * (mb + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dbsrColInd, hbsrColInd, sizeof(int) * nnzb, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dbsrVal, hbsrVal, sizeof(float) * nnzb * bs * bs, hipMemcpyHostToDevice)); // 1. Get buffer size int bufferSize = 0; HIPSPARSE_CHECK( hipsparseSbsrilu02_bufferSize(handle, HIPSPARSE_DIRECTION_COLUMN, // Block storage direction mb, nnzb, descr, dbsrVal, dbsrRowPtr, dbsrColInd, bs, info, &bufferSize)); void* dbuffer = nullptr; HIP_CHECK(hipMalloc((void**)&dbuffer, bufferSize)); // 2. Perform analysis (symbolic factorization) // This step analyzes the sparsity pattern of A to determine the structure of L and U. HIPSPARSE_CHECK( hipsparseSbsrilu02_analysis(handle, HIPSPARSE_DIRECTION_COLUMN, mb, nnzb, descr, dbsrVal, dbsrRowPtr, dbsrColInd, bs, info, HIPSPARSE_SOLVE_POLICY_USE_LEVEL, // Policy for analysis dbuffer)); // 3. Perform factorization (numerical computation) // This step computes the actual numerical values of L and U, stored in dbsrVal. HIPSPARSE_CHECK(hipsparseSbsrilu02(handle, HIPSPARSE_DIRECTION_COLUMN, mb, nnzb, descr, dbsrVal, dbsrRowPtr, dbsrColInd, bs, info, HIPSPARSE_SOLVE_POLICY_USE_LEVEL, // Policy for factorization dbuffer)); // 4. Check for zero pivots // A zero pivot can occur during factorization, indicating a numerical breakdown. int zeroPivot = 0; // -1 if no zero pivot, otherwise the block row index of the first zero pivot HIPSPARSE_CHECK(hipsparseXbsrilu02_zeroPivot(handle, info, &zeroPivot)); if(zeroPivot != -1) { printf("Error: Zero pivot detected during ILU0 factorization at block row index %d\n", zeroPivot); // Handle the error (e.g., return, use a different preconditioner, etc.) } else { printf("BSRILU0 factorization completed successfully (no zero pivots detected).\n"); } // Copy the factorized values (L and U combined) back to host float* hbsrVal_result = new float[nnzb * bs * bs]; HIP_CHECK( hipMemcpy(hbsrVal_result, dbsrVal, sizeof(float) * nnzb * bs * bs, hipMemcpyDeviceToHost)); // Print the result (the values of the factorized L and U combined) printf("\nFactorized BSR values (L and U combined):\n"); for(int i = 0; i < nnzb * bs * bs; ++i) { printf("val[%d] = %f\n", i, hbsrVal_result[i]); } // Clean up delete[] hbsrVal_result; HIPSPARSE_CHECK(hipsparseDestroyBsrilu02Info(info)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(descr)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); HIP_CHECK(hipFree(dbsrRowPtr)); HIP_CHECK(hipFree(dbsrColInd)); HIP_CHECK(hipFree(dbsrVal)); HIP_CHECK(hipFree(dbuffer)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**dirA**–**[in]**direction that specified whether to count nonzero elements by[HIPSPARSE_DIRECTION_ROW](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59ae8589abecf2fbfb4b6307fd9dacd9e55)or by[HIPSPARSE_DIRECTION_COLUMN](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59a32e23f292b2377f6e60bdc90274c796c).**mb**–**[in]**number of block rows in the sparse BSR matrix.**nnzb**–**[in]**number of non-zero block entries of the sparse BSR matrix.**descrA**–**[in]**descriptor of the sparse BSR matrix.**bsrSortedValA_valM**–**[inout]**array of length`nnzb*blockDim*blockDim`

containing the values of the sparse BSR matrix.**bsrSortedRowPtrA**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix.**bsrSortedColIndA**–**[in]**array of`nnzb`

elements containing the block column indices of the sparse BSR matrix.**blockDim**–**[in]**the block dimension of the BSR matrix. Between 1 and m where`m=mb*blockDim`

.**info**–**[in]**structure that holds the information collected during the analysis step.**policy**–**[in]**[HIPSPARSE_SOLVE_POLICY_NO_LEVEL](types.html#hipsparse-types_8h_1a0d98e490c94d4facc231db60baf1c3b3ac5830aa96848e832b3b375ad08abdb09)or[HIPSPARSE_SOLVE_POLICY_USE_LEVEL](types.html#hipsparse-types_8h_1a0d98e490c94d4facc231db60baf1c3b3a934309d6656638e375f0759b89fd81b5).**pBuffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`mb`

,`nnzb`

,`blockDim`

,`descrA`

,`bsrSortedValA_valM`

,`bsrSortedRowPtrA`

or`bsrSortedColIndA`

pointer is invalid.**HIPSPARSE_STATUS_ARCH_MISMATCH**– the device is not supported.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.**HIPSPARSE_STATUS_NOT_SUPPORTED**–[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXcsrilu02_zeroPivot()[#](#hipsparsexcsrilu02-zeropivot)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseXcsrilu02_zeroPivot([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[csrilu02Info_t](types.html#_CPPv414csrilu02Info_t)info, int *position)[#](#_CPPv428hipsparseXcsrilu02_zeroPivot17hipsparseHandle_t14csrilu02Info_tPi) `hipsparseXcsrilu02_zeroPivot`

returns[HIPSPARSE_STATUS_ZERO_PIVOT](types.html#hipsparse-types_8h_1aa069bec7a4f24d00dab1dc4612d4de79a88ff0f0537dfe037fcf9f99ff0cf79da), if either a structural or numerical zero has been found during[hipsparseXcsrilu02()](#hipsparse__csrilu0_8h_1a7fd68be2e8b248a9ee7304b24d3819a0)computation. The first zero pivot \(j\) at \(A_{j,j}\) is stored in`position`

, using same index base as the CSR matrix.`position`

can be in host or device memory. If no zero pivot has been found,`position`

is set to -1 and[HIPSPARSE_STATUS_SUCCESS](types.html#hipsparse-types_8h_1aa069bec7a4f24d00dab1dc4612d4de79a146a8a2fd27ee49132f8dcea617fc481)is returned instead.Note

`hipsparseXcsrilu02_zeroPivot`

is a blocking function. It might influence performance negatively.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**info**–**[in]**structure that holds the information collected during the analysis step.**position**–**[inout]**pointer to zero pivot \(j\), can be in host or device memory.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`info`

or`position`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.**HIPSPARSE_STATUS_ZERO_PIVOT**– zero pivot has been found.



## hipsparseXcsrilu02_numericBoost()[#](#hipsparsexcsrilu02-numericboost)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseScsrilu02_numericBoost([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[csrilu02Info_t](types.html#_CPPv414csrilu02Info_t)info, int enable_boost, double *tol, float *boost_val)[#](#_CPPv431hipsparseScsrilu02_numericBoost17hipsparseHandle_t14csrilu02Info_tiPdPf)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDcsrilu02_numericBoost([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[csrilu02Info_t](types.html#_CPPv414csrilu02Info_t)info, int enable_boost, double *tol, double *boost_val)[#](#_CPPv431hipsparseDcsrilu02_numericBoost17hipsparseHandle_t14csrilu02Info_tiPdPd)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCcsrilu02_numericBoost([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[csrilu02Info_t](types.html#_CPPv414csrilu02Info_t)info, int enable_boost, double *tol, hipComplex *boost_val)[#](#_CPPv431hipsparseCcsrilu02_numericBoost17hipsparseHandle_t14csrilu02Info_tiPdP10hipComplex)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZcsrilu02_numericBoost([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[csrilu02Info_t](types.html#_CPPv414csrilu02Info_t)info, int enable_boost, double *tol, hipDoubleComplex *boost_val)[#](#_CPPv431hipsparseZcsrilu02_numericBoost17hipsparseHandle_t14csrilu02Info_tiPdP16hipDoubleComplex) `hipsparseXcsrilu02_numericBoost`

enables the user to replace a numerical value in an incomplete LU factorization.`tol`

is used to determine whether a numerical value is replaced by`boost_val`

, such that \(A_{j,j} = \text{boost_val}\) if \(\text{tol} \ge \left|A_{j,j}\right|\).Note

The boost value is enabled by setting

`enable_boost`

to 1 or disabled by setting`enable_boost`

to 0.Note

`tol`

and`boost_val`

can be in host or device memory.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**info**–**[in]**structure that holds the information collected during the analysis step.**enable_boost**–**[in]**enable/disable numeric boost.**tol**–**[in]**tolerance to determine whether a numerical value is replaced or not.**boost_val**–**[in]**boost value to replace a numerical value.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`info`

,`tol`

or`boost_val`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.



## hipsparseXcsrilu02_bufferSize()[#](#hipsparsexcsrilu02-buffersize)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseScsrilu02_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, float *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csrilu02Info_t](types.html#_CPPv414csrilu02Info_t)info, int *pBufferSizeInBytes)[#](#_CPPv429hipsparseScsrilu02_bufferSize17hipsparseHandle_tiiK19hipsparseMatDescr_tPfPKiPKi14csrilu02Info_tPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDcsrilu02_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, double *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csrilu02Info_t](types.html#_CPPv414csrilu02Info_t)info, int *pBufferSizeInBytes)[#](#_CPPv429hipsparseDcsrilu02_bufferSize17hipsparseHandle_tiiK19hipsparseMatDescr_tPdPKiPKi14csrilu02Info_tPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCcsrilu02_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, hipComplex *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csrilu02Info_t](types.html#_CPPv414csrilu02Info_t)info, int *pBufferSizeInBytes)[#](#_CPPv429hipsparseCcsrilu02_bufferSize17hipsparseHandle_tiiK19hipsparseMatDescr_tP10hipComplexPKiPKi14csrilu02Info_tPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZcsrilu02_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, hipDoubleComplex *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csrilu02Info_t](types.html#_CPPv414csrilu02Info_t)info, int *pBufferSizeInBytes)[#](#_CPPv429hipsparseZcsrilu02_bufferSize17hipsparseHandle_tiiK19hipsparseMatDescr_tP16hipDoubleComplexPKiPKi14csrilu02Info_tPi) `hipsparseXcsrilu02_bufferSize`

returns the size of the temporary storage buffer in bytes that is required by[hipsparseXcsrilu02_analysis()](#hipsparse__csrilu0_8h_1af9373f20b711d53705ac27a3a12ff894)and[hipsparseXcsrilu02()](#hipsparse__csrilu0_8h_1a7fd68be2e8b248a9ee7304b24d3819a0). The temporary storage buffer must be allocated by the user.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**descrA**–**[in]**descriptor of the sparse CSR matrix.**csrSortedValA**–**[in]**array of`nnz`

elements of the sparse CSR matrix.**csrSortedRowPtrA**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csrSortedColIndA**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**info**–**[out]**structure that holds the information collected during the analysis step.**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer required by[hipsparseXcsrilu02_analysis()](#hipsparse__csrilu0_8h_1af9373f20b711d53705ac27a3a12ff894)and[hipsparseXcsrilu02()](#hipsparse__csrilu0_8h_1a7fd68be2e8b248a9ee7304b24d3819a0).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`nnz`

,`descrA`

,`csrSortedValA`

,`csrSortedRowPtrA`

,`csrSortedColIndA`

,`info`

or`pBufferSizeInBytes`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.



## hipsparseXcsrilu02_bufferSizeExt()[#](#hipsparsexcsrilu02-buffersizeext)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseScsrilu02_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, float *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csrilu02Info_t](types.html#_CPPv414csrilu02Info_t)info, size_t *pBufferSizeInBytes)[#](#_CPPv432hipsparseScsrilu02_bufferSizeExt17hipsparseHandle_tiiK19hipsparseMatDescr_tPfPKiPKi14csrilu02Info_tP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDcsrilu02_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, double *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csrilu02Info_t](types.html#_CPPv414csrilu02Info_t)info, size_t *pBufferSizeInBytes)[#](#_CPPv432hipsparseDcsrilu02_bufferSizeExt17hipsparseHandle_tiiK19hipsparseMatDescr_tPdPKiPKi14csrilu02Info_tP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCcsrilu02_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, hipComplex *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csrilu02Info_t](types.html#_CPPv414csrilu02Info_t)info, size_t *pBufferSizeInBytes)[#](#_CPPv432hipsparseCcsrilu02_bufferSizeExt17hipsparseHandle_tiiK19hipsparseMatDescr_tP10hipComplexPKiPKi14csrilu02Info_tP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZcsrilu02_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, hipDoubleComplex *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csrilu02Info_t](types.html#_CPPv414csrilu02Info_t)info, size_t *pBufferSizeInBytes)[#](#_CPPv432hipsparseZcsrilu02_bufferSizeExt17hipsparseHandle_tiiK19hipsparseMatDescr_tP16hipDoubleComplexPKiPKi14csrilu02Info_tP6size_t) `hipsparseXcsrilu02_bufferSizeExt`

returns the size of the temporary storage buffer in bytes that is required by[hipsparseXcsrilu02_analysis()](#hipsparse__csrilu0_8h_1af9373f20b711d53705ac27a3a12ff894)and[hipsparseXcsrilu02()](#hipsparse__csrilu0_8h_1a7fd68be2e8b248a9ee7304b24d3819a0). The temporary storage buffer must be allocated by the user.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**descrA**–**[in]**descriptor of the sparse CSR matrix.**csrSortedValA**–**[in]**array of`nnz`

elements of the sparse CSR matrix.**csrSortedRowPtrA**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csrSortedColIndA**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**info**–**[out]**structure that holds the information collected during the analysis step.**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer required by[hipsparseXcsrilu02_analysis()](#hipsparse__csrilu0_8h_1af9373f20b711d53705ac27a3a12ff894)and[hipsparseXcsrilu02()](#hipsparse__csrilu0_8h_1a7fd68be2e8b248a9ee7304b24d3819a0).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`nnz`

,`descrA`

,`csrSortedValA`

,`csrSortedRowPtrA`

,`csrSortedColIndA`

,`info`

or`pBufferSizeInBytes`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.



## hipsparseXcsrilu02_analysis()[#](#hipsparsexcsrilu02-analysis)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseScsrilu02_analysis([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const float *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csrilu02Info_t](types.html#_CPPv414csrilu02Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv427hipsparseScsrilu02_analysis17hipsparseHandle_tiiK19hipsparseMatDescr_tPKfPKiPKi14csrilu02Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDcsrilu02_analysis([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const double *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csrilu02Info_t](types.html#_CPPv414csrilu02Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv427hipsparseDcsrilu02_analysis17hipsparseHandle_tiiK19hipsparseMatDescr_tPKdPKiPKi14csrilu02Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCcsrilu02_analysis([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipComplex *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csrilu02Info_t](types.html#_CPPv414csrilu02Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv427hipsparseCcsrilu02_analysis17hipsparseHandle_tiiK19hipsparseMatDescr_tPK10hipComplexPKiPKi14csrilu02Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZcsrilu02_analysis([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipDoubleComplex *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csrilu02Info_t](types.html#_CPPv414csrilu02Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv427hipsparseZcsrilu02_analysis17hipsparseHandle_tiiK19hipsparseMatDescr_tPK16hipDoubleComplexPKiPKi14csrilu02Info_t22hipsparseSolvePolicy_tPv) `hipsparseXcsrilu02_analysis`

performs the analysis step for[hipsparseXcsrilu02()](#hipsparse__csrilu0_8h_1a7fd68be2e8b248a9ee7304b24d3819a0). It is expected that this function will be executed only once for a given matrix and particular operation type.Note

If the matrix sparsity pattern changes, the gathered information will become invalid.

Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**descrA**–**[in]**descriptor of the sparse CSR matrix.**csrSortedValA**–**[in]**array of`nnz`

elements of the sparse CSR matrix.**csrSortedRowPtrA**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csrSortedColIndA**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**info**–**[out]**structure that holds the information collected during the analysis step.**policy**–**[in]**[HIPSPARSE_SOLVE_POLICY_NO_LEVEL](types.html#hipsparse-types_8h_1a0d98e490c94d4facc231db60baf1c3b3ac5830aa96848e832b3b375ad08abdb09)or[HIPSPARSE_SOLVE_POLICY_USE_LEVEL](types.html#hipsparse-types_8h_1a0d98e490c94d4facc231db60baf1c3b3a934309d6656638e375f0759b89fd81b5).**pBuffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`nnz`

,`descrA`

,`csrSortedValA`

,`csrSortedRowPtrA`

,`csrSortedColIndA`

,`info`

or`pBuffer`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.



## hipsparseXcsrilu02()[#](#hipsparsexcsrilu02)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseScsrilu02([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, float *csrSortedValA_valM, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csrilu02Info_t](types.html#_CPPv414csrilu02Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv418hipsparseScsrilu0217hipsparseHandle_tiiK19hipsparseMatDescr_tPfPKiPKi14csrilu02Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDcsrilu02([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, double *csrSortedValA_valM, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csrilu02Info_t](types.html#_CPPv414csrilu02Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv418hipsparseDcsrilu0217hipsparseHandle_tiiK19hipsparseMatDescr_tPdPKiPKi14csrilu02Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCcsrilu02([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, hipComplex *csrSortedValA_valM, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csrilu02Info_t](types.html#_CPPv414csrilu02Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv418hipsparseCcsrilu0217hipsparseHandle_tiiK19hipsparseMatDescr_tP10hipComplexPKiPKi14csrilu02Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZcsrilu02([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, hipDoubleComplex *csrSortedValA_valM, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csrilu02Info_t](types.html#_CPPv414csrilu02Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv418hipsparseZcsrilu0217hipsparseHandle_tiiK19hipsparseMatDescr_tP16hipDoubleComplexPKiPKi14csrilu02Info_t22hipsparseSolvePolicy_tPv) Incomplete LU factorization with 0 fill-ins and no pivoting using CSR storage format.

`hipsparseXcsrilu02`

computes the incomplete LU factorization with 0 fill-ins and no pivoting of a sparse \(m \times m\) CSR matrix \(A\), such that\[ A \approx LU \]where the lower triangular matrix \(L\) and the upper triangular matrix \(U\) are computed using:\[\begin{split} \begin{array}{ll} L_{ij} = \frac{1}{U_{jj}}(A_{ij} - \sum_{k=0}^{j-1}L_{ik} \times U_{kj}), & \text{if i > j} \\ U_{ij} = (A_{ij} - \sum_{k=0}^{j-1}L_{ik} \times U_{kj}), & \text{if i <= j} \end{array} \end{split}\]for each entry found in the CSR matrix \(A\).Computing the above incomplete \(LU\) factorization requires three steps to complete. First, the user determines the size of the required temporary storage buffer by calling

[hipsparseXcsrilu02_bufferSize()](#hipsparse__csrilu0_8h_1a1cdc19abd5d4d3defb3737c790f8f010). Once this buffer size has been determined, the user allocates the buffer and passes it to[hipsparseXcsrilu02_analysis()](#hipsparse__csrilu0_8h_1af9373f20b711d53705ac27a3a12ff894). This will perform analysis on the sparsity pattern of the matrix. Finally, the user calls`hipsparseScsrilu02`

,`hipsparseDcsrilu02`

,`hipsparseCcsrilu02`

, or`hipsparseZcsrilu02`

to perform the actual factorization. The calculation of the buffer size and the analysis of the sparse matrix only need to be performed once for a given sparsity pattern while the factorization can be repeatedly applied to multiple matrices having the same sparsity pattern. Once all calls to[hipsparseXcsrilu02()](#hipsparse__csrilu0_8h_1a7fd68be2e8b248a9ee7304b24d3819a0)are complete, the temporary buffer can be deallocated.When computing the \(LU\) factorization, it is possible that \(U_{jj} == 0\) which would result in a division by zero. This could occur from either \(A_{jj}\) not existing in the sparse CSR matrix (referred to as a structural zero) or because \(A_{ij} - \sum_{k=0}^{j-1}L_{ik} \times U_{kj} == 0\) (referred to as a numerical zero). For example, running the \(LU\) factorization on the following matrix:

\[\begin{split} \begin{bmatrix} 2 & 1 & 0 \\ 1 & 2 & 1 \\ 0 & 1 & 2 \end{bmatrix} \end{split}\]results in a successful \(LU\) factorization, however running with the matrix:\[\begin{split} \begin{bmatrix} 2 & 1 & 0 \\ 1 & 1/2 & 1 \\ 0 & 1 & 2 \end{bmatrix} \end{split}\]results in a numerical zero because:\[\begin{split} \begin{array}{ll} U_{00} &= 2 \\ U_{01} &= 1 \\ L_{10} &= \frac{1}{2} \\ U_{11} &= \frac{1}{2} - \frac{1}{2} &= 0 \end{array} \end{split}\]The user can detect the presence of a structural zero by calling[hipsparseXcsrilu02_zeroPivot()](#hipsparse__csrilu0_8h_1ab139ea359b40dd01937f8cd6f6890d04)after[hipsparseXcsrilu02_analysis()](#hipsparse__csrilu0_8h_1af9373f20b711d53705ac27a3a12ff894)and/or the presence of a structural or numerical zero by calling[hipsparseXcsrilu02_zeroPivot()](#hipsparse__csrilu0_8h_1ab139ea359b40dd01937f8cd6f6890d04)after[hipsparseXcsrilu02()](#hipsparse__csrilu0_8h_1a7fd68be2e8b248a9ee7304b24d3819a0). In both cases,[hipsparseXcsrilu02_zeroPivot()](#hipsparse__csrilu0_8h_1ab139ea359b40dd01937f8cd6f6890d04)will report the first zero pivot (either numerical or structural) found. See example below. The user can also set the diagonal type to be \(1\) using[hipsparseSetMatDiagType()](auxiliary.html#hipsparse-auxiliary_8h_1aec6fa039793196011f15cfb0b21c2b59)which will interpret the matrix \(A\) as having ones on its diagonal (even if no nonzero exists in the sparsity pattern).`hipsparseXcsrilu02`

computes the \(LU\) factorization inplace meaning that the values array`csrSortedValA_valM`

of the \(A\) matrix is overwritten with the \(L\) matrix stored in the strictly lower triangular part of \(A\) and the \(U\) matrix stored in the upper part of \(A\):\[\begin{split} \begin{align} \begin{bmatrix} a_{00} & a_{01} & a_{02} \\ a_{10} & a_{11} & a_{12} \\ a_{20} & a_{21} & a_{22} \end{bmatrix} \rightarrow \begin{bmatrix} u_{00} & u_{01} & u_{02} \\ l_{10} & u_{11} & u_{12} \\ l_{20} & l_{21} & u_{22} \end{bmatrix} \end{align} \end{split}\]The row pointer array`csrSortedRowPtrA`

and the column indices array`csrSortedColIndA`

remain the same for \(A\) and \(LU\) as the incomplete factorization does not generate new nonzeros in \(LU\) which do not already exist in \(A\).The performance of computing \(LU\) factorization with hipSPARSE greatly depends on the sparisty pattern the the matrix \(A\) as this is what determines the amount of parallelism available.

**Example**int main(int argc, char* argv[]) { // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // A sample square matrix A (4x4) in CSR format for ILU(0) factorization. // The 'S' in Scsrilu02 indicates single precision float. // Matrix A: // ( 1 2 0 0 ) // ( 3 4 5 0 ) // ( 0 6 7 8 ) // ( 0 0 9 10 ) int m = 4; // Number of rows int n = 4; // Number of columns (equal to m for ILU) int nnz = 10; // Number of non-zero elements // CSR row pointers int hcsrRowPtr[5] = {0, 2, 5, 8, 10}; // CSR column indices int hcsrColInd[10] = {0, 1, 0, 1, 2, 1, 2, 3, 2, 3}; // CSR values float hcsrVal[10] = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f, 9.0f, 10.0f}; // Matrix descriptor hipsparseMatDescr_t descr; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&descr)); // Set index base on descriptor HIPSPARSE_CHECK(hipsparseSetMatIndexBase(descr, HIPSPARSE_INDEX_BASE_ZERO)); // For incomplete LU, the L factor often has a unit diagonal. HIPSPARSE_CHECK(hipsparseSetMatDiagType(descr, HIPSPARSE_DIAG_TYPE_UNIT)); // CSRILU02 info (for incomplete LU factorization) csrilu02Info_t info; HIPSPARSE_CHECK(hipsparseCreateCsrilu02Info(&info)); // Offload data to device int* dcsrRowPtr; int* dcsrColInd; float* dcsrVal; // This will store the factorized L and U values HIP_CHECK(hipMalloc((void**)&dcsrRowPtr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&dcsrColInd, sizeof(int) * nnz)); HIP_CHECK( hipMalloc((void**)&dcsrVal, sizeof(float) * nnz)); // Note: Same size as input, values will be overwritten HIP_CHECK(hipMemcpy(dcsrRowPtr, hcsrRowPtr, sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrColInd, hcsrColInd, sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrVal, hcsrVal, sizeof(float) * nnz, hipMemcpyHostToDevice)); // 1. Get buffer size int bufferSize = 0; HIPSPARSE_CHECK(hipsparseScsrilu02_bufferSize( handle, m, nnz, descr, dcsrVal, dcsrRowPtr, dcsrColInd, info, &bufferSize)); void* dbuffer = nullptr; HIP_CHECK(hipMalloc((void**)&dbuffer, bufferSize)); // 2. Perform analysis (symbolic factorization) // This step analyzes the sparsity pattern of A to determine the structure of L and U. HIPSPARSE_CHECK( hipsparseScsrilu02_analysis(handle, m, nnz, descr, dcsrVal, dcsrRowPtr, dcsrColInd, info, HIPSPARSE_SOLVE_POLICY_USE_LEVEL, // Policy for analysis dbuffer)); // 3. Perform factorization (numerical computation) // This step computes the actual numerical values of L and U, stored in dcsrVal. HIPSPARSE_CHECK(hipsparseScsrilu02(handle, m, nnz, descr, dcsrVal, dcsrRowPtr, dcsrColInd, info, HIPSPARSE_SOLVE_POLICY_USE_LEVEL, // Policy for factorization dbuffer)); // 4. Check for zero pivots // A zero pivot can occur during factorization, indicating a numerical breakdown. int zeroPivot = 0; // -1 if no zero pivot, otherwise the row index of the first zero pivot HIPSPARSE_CHECK(hipsparseXcsrilu02_zeroPivot(handle, info, &zeroPivot)); if(zeroPivot != -1) { printf("Error: Zero pivot detected during ILU0 factorization at row index %d\n", zeroPivot); // Depending on your application, you might want to handle this error // or switch to a different preconditioner. } else { printf("CSRILU0 factorization completed successfully (no zero pivots detected).\n"); } // Copy the factorized values (L and U combined) back to host float* hcsrVal_result = new float[nnz]; HIP_CHECK(hipMemcpy(hcsrVal_result, dcsrVal, sizeof(float) * nnz, hipMemcpyDeviceToHost)); // Print the result (the values of the factorized L and U combined) printf("\nFactorized CSR values (L and U combined):\n"); for(int i = 0; i < nnz; ++i) { printf("val[%d] = %f\n", i, hcsrVal_result[i]); } // Clean up delete[] hcsrVal_result; HIPSPARSE_CHECK(hipsparseDestroyCsrilu02Info(info)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(descr)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); HIP_CHECK(hipFree(dcsrRowPtr)); HIP_CHECK(hipFree(dcsrColInd)); HIP_CHECK(hipFree(dcsrVal)); HIP_CHECK(hipFree(dbuffer)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**descrA**–**[in]**descriptor of the sparse CSR matrix.**csrSortedValA_valM**–**[inout]**array of`nnz`

elements of the sparse CSR matrix.**csrSortedRowPtrA**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csrSortedColIndA**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**info**–**[in]**structure that holds the information collected during the analysis step.**policy**–**[in]**[HIPSPARSE_SOLVE_POLICY_NO_LEVEL](types.html#hipsparse-types_8h_1a0d98e490c94d4facc231db60baf1c3b3ac5830aa96848e832b3b375ad08abdb09)or[HIPSPARSE_SOLVE_POLICY_USE_LEVEL](types.html#hipsparse-types_8h_1a0d98e490c94d4facc231db60baf1c3b3a934309d6656638e375f0759b89fd81b5).**pBuffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`nnz`

,`descrA`

,`csrSortedValA_valM`

,`csrSortedRowPtrA`

or`csrSortedColIndA`

pointer is invalid.**HIPSPARSE_STATUS_ARCH_MISMATCH**– the device is not supported.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.



## hipsparseXbsric02_zeroPivot()[#](#hipsparsexbsric02-zeropivot)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseXbsric02_zeroPivot([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[bsric02Info_t](types.html#_CPPv413bsric02Info_t)info, int *position)[#](#_CPPv427hipsparseXbsric02_zeroPivot17hipsparseHandle_t13bsric02Info_tPi) `hipsparseXbsric02_zeroPivot`

returns[HIPSPARSE_STATUS_ZERO_PIVOT](types.html#hipsparse-types_8h_1aa069bec7a4f24d00dab1dc4612d4de79a88ff0f0537dfe037fcf9f99ff0cf79da), if either a structural or numerical zero has been found during[hipsparseXbsric02_analysis()](#hipsparse__bsric0_8h_1a3f330948f32374685ad4cf062ed51af8)or[hipsparseXbsric02()](#hipsparse__bsric0_8h_1a3b4e7c01e4bb25b62c05b90a5d1307e1)computation. The first zero pivot \(j\) at \(A_{j,j}\) is stored in`position`

, using same index base as the BSR matrix.`position`

can be in host or device memory. If no zero pivot has been found,`position`

is set to -1 and[HIPSPARSE_STATUS_SUCCESS](types.html#hipsparse-types_8h_1aa069bec7a4f24d00dab1dc4612d4de79a146a8a2fd27ee49132f8dcea617fc481)is returned instead.Note

If a zero pivot is found,

`position=j`

means that either the diagonal block`A(j,j)`

is missing (structural zero) or the diagonal block`A(j,j)`

is not positive definite (numerical zero).Note

`hipsparseXbsric02_zeroPivot`

is a blocking function. It might influence performance negatively.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**info**–**[in]**structure that holds the information collected during the analysis step.**position**–**[inout]**pointer to zero pivot \(j\), can be in host or device memory.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`info`

or`position`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.**HIPSPARSE_STATUS_ZERO_PIVOT**– zero pivot has been found.



## hipsparseXbsric02_bufferSize()[#](#hipsparsexbsric02-buffersize)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSbsric02_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, float *bsrValA, const int *bsrRowPtrA, const int *bsrColIndA, int blockDim,[bsric02Info_t](types.html#_CPPv413bsric02Info_t)info, int *pBufferSizeInBytes)[#](#_CPPv428hipsparseSbsric02_bufferSize17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPfPKiPKii13bsric02Info_tPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDbsric02_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, double *bsrValA, const int *bsrRowPtrA, const int *bsrColIndA, int blockDim,[bsric02Info_t](types.html#_CPPv413bsric02Info_t)info, int *pBufferSizeInBytes)[#](#_CPPv428hipsparseDbsric02_bufferSize17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPdPKiPKii13bsric02Info_tPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCbsric02_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, hipComplex *bsrValA, const int *bsrRowPtrA, const int *bsrColIndA, int blockDim,[bsric02Info_t](types.html#_CPPv413bsric02Info_t)info, int *pBufferSizeInBytes)[#](#_CPPv428hipsparseCbsric02_bufferSize17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tP10hipComplexPKiPKii13bsric02Info_tPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZbsric02_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, hipDoubleComplex *bsrValA, const int *bsrRowPtrA, const int *bsrColIndA, int blockDim,[bsric02Info_t](types.html#_CPPv413bsric02Info_t)info, int *pBufferSizeInBytes)[#](#_CPPv428hipsparseZbsric02_bufferSize17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tP16hipDoubleComplexPKiPKii13bsric02Info_tPi) `hipsparseXbsric02_bufferSize`

returns the size of the temporary storage buffer in bytes that is required by[hipsparseXbsric02_analysis()](#hipsparse__bsric0_8h_1a3f330948f32374685ad4cf062ed51af8)and[hipsparseXbsric02()](#hipsparse__bsric0_8h_1a3b4e7c01e4bb25b62c05b90a5d1307e1). The temporary storage buffer must be allocated by the user.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**dirA**–**[in]**direction that specifies whether to count nonzero elements by[HIPSPARSE_DIRECTION_ROW](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59ae8589abecf2fbfb4b6307fd9dacd9e55)or by[HIPSPARSE_DIRECTION_COLUMN](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59a32e23f292b2377f6e60bdc90274c796c).**mb**–**[in]**number of block rows in the sparse BSR matrix.**nnzb**–**[in]**number of non-zero block entries of the sparse BSR matrix.**descrA**–**[in]**descriptor of the sparse BSR matrix.**bsrValA**–**[in]**array of length`nnzb*blockDim*blockDim`

containing the values of the sparse BSR matrix.**bsrRowPtrA**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix.**bsrColIndA**–**[in]**array of`nnzb`

elements containing the block column indices of the sparse BSR matrix.**blockDim**–**[in]**the block dimension of the BSR matrix. Between 1 and m where`m=mb*blockDim`

.**info**–**[out]**structure that holds the information collected during the analysis step.**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer required by[hipsparseSbsric02_analysis()](#hipsparse__bsric0_8h_1a3f330948f32374685ad4cf062ed51af8),[hipsparseDbsric02_analysis()](#hipsparse__bsric0_8h_1a6e65d26d95ea1f3f947e20a04b065f9e),[hipsparseCbsric02_analysis()](#hipsparse__bsric0_8h_1a20f5aaaf6b3b8d5ea499035b325cda12),[hipsparseZbsric02_analysis()](#hipsparse__bsric0_8h_1ab2295912ac0ee031aebaa64e8731fa48),[hipsparseSbsric02()](#hipsparse__bsric0_8h_1a3b4e7c01e4bb25b62c05b90a5d1307e1),[hipsparseDbsric02()](#hipsparse__bsric0_8h_1a840ca04fd7e61ee06287361b461883fe),[hipsparseCbsric02()](#hipsparse__bsric0_8h_1a84cc2be2bfec98ca670a9cb07367e4e2)and[hipsparseZbsric02()](#hipsparse__bsric0_8h_1a3e68d4bf13e0a5e11be8827e15f51abe).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`mb`

,`nnzb`

,`blockDim`

,`descrA`

,`bsrValA`

,`bsrRowPtrA`

,`bsrColIndA`

,`info`

or`pBufferSizeInBytes`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.**HIPSPARSE_STATUS_NOT_SUPPORTED**–[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXbsric02_analysis()[#](#hipsparsexbsric02-analysis)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSbsric02_analysis([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const float *bsrValA, const int *bsrRowPtrA, const int *bsrColIndA, int blockDim,[bsric02Info_t](types.html#_CPPv413bsric02Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv426hipsparseSbsric02_analysis17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPKfPKiPKii13bsric02Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDbsric02_analysis([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const double *bsrValA, const int *bsrRowPtrA, const int *bsrColIndA, int blockDim,[bsric02Info_t](types.html#_CPPv413bsric02Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv426hipsparseDbsric02_analysis17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPKdPKiPKii13bsric02Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCbsric02_analysis([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipComplex *bsrValA, const int *bsrRowPtrA, const int *bsrColIndA, int blockDim,[bsric02Info_t](types.html#_CPPv413bsric02Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv426hipsparseCbsric02_analysis17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPK10hipComplexPKiPKii13bsric02Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZbsric02_analysis([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipDoubleComplex *bsrValA, const int *bsrRowPtrA, const int *bsrColIndA, int blockDim,[bsric02Info_t](types.html#_CPPv413bsric02Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv426hipsparseZbsric02_analysis17hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPK16hipDoubleComplexPKiPKii13bsric02Info_t22hipsparseSolvePolicy_tPv) `hipsparseXbsric02_analysis`

performs the analysis step for[hipsparseXbsric02()](#hipsparse__bsric0_8h_1a3b4e7c01e4bb25b62c05b90a5d1307e1). It is expected that this function will be executed only once for a given matrix and particular operation type.Note

If the matrix sparsity pattern changes, the gathered information will become invalid.

Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**dirA**–**[in]**direction that specified whether to count nonzero elements by[HIPSPARSE_DIRECTION_ROW](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59ae8589abecf2fbfb4b6307fd9dacd9e55)or by[HIPSPARSE_DIRECTION_COLUMN](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59a32e23f292b2377f6e60bdc90274c796c).**mb**–**[in]**number of block rows in the sparse BSR matrix.**nnzb**–**[in]**number of non-zero block entries of the sparse BSR matrix.**descrA**–**[in]**descriptor of the sparse BSR matrix.**bsrValA**–**[in]**array of length`nnzb*blockDim*blockDim`

containing the values of the sparse BSR matrix.**bsrRowPtrA**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix.**bsrColIndA**–**[in]**array of`nnzb`

elements containing the block column indices of the sparse BSR matrix.**blockDim**–**[in]**the block dimension of the BSR matrix. Between 1 and m where`m=mb*blockDim`

.**info**–**[out]**structure that holds the information collected during the analysis step.**policy**–**[in]**[HIPSPARSE_SOLVE_POLICY_NO_LEVEL](types.html#hipsparse-types_8h_1a0d98e490c94d4facc231db60baf1c3b3ac5830aa96848e832b3b375ad08abdb09)or[HIPSPARSE_SOLVE_POLICY_USE_LEVEL](types.html#hipsparse-types_8h_1a0d98e490c94d4facc231db60baf1c3b3a934309d6656638e375f0759b89fd81b5).**pBuffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`mb`

,`nnzb`

,`blockDim`

,`descrA`

,`bsrValA`

,`bsrRowPtrA`

,`bsrColIndA`

,`info`

or`pBuffer`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.**HIPSPARSE_STATUS_NOT_SUPPORTED**–[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXbsric02()[#](#hipsparsexbsric02)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSbsric02([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, float *bsrValA, const int *bsrRowPtrA, const int *bsrColIndA, int blockDim,[bsric02Info_t](types.html#_CPPv413bsric02Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv417hipsparseSbsric0217hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPfPKiPKii13bsric02Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDbsric02([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, double *bsrValA, const int *bsrRowPtrA, const int *bsrColIndA, int blockDim,[bsric02Info_t](types.html#_CPPv413bsric02Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv417hipsparseDbsric0217hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tPdPKiPKii13bsric02Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCbsric02([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, hipComplex *bsrValA, const int *bsrRowPtrA, const int *bsrColIndA, int blockDim,[bsric02Info_t](types.html#_CPPv413bsric02Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv417hipsparseCbsric0217hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tP10hipComplexPKiPKii13bsric02Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZbsric02([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[hipsparseDirection_t](types.html#_CPPv420hipsparseDirection_t)dirA, int mb, int nnzb, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, hipDoubleComplex *bsrValA, const int *bsrRowPtrA, const int *bsrColIndA, int blockDim,[bsric02Info_t](types.html#_CPPv413bsric02Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv417hipsparseZbsric0217hipsparseHandle_t20hipsparseDirection_tiiK19hipsparseMatDescr_tP16hipDoubleComplexPKiPKii13bsric02Info_t22hipsparseSolvePolicy_tPv) Incomplete Cholesky factorization with 0 fill-ins and no pivoting using BSR storage format.

`hipsparseXbsric02`

computes the incomplete Cholesky factorization with 0 fill-ins and no pivoting of a sparse \(mb \times mb\) BSR matrix \(A\), such that\[ A \approx LL^T \]Computing the above incomplete Cholesky factorization requires three steps to complete. First, the user determines the size of the required temporary storage buffer by calling

[hipsparseXbsric02_bufferSize()](#hipsparse__bsric0_8h_1a9573e196c9f4eacc5cf2e44a25e817d1). Once this buffer size has been determined, the user allocates the buffer and passes it to[hipsparseXbsric02_analysis()](#hipsparse__bsric0_8h_1a3f330948f32374685ad4cf062ed51af8). This will perform analysis on the sparsity pattern of the matrix. Finally, the user calls`hipsparseXbsric02`

to perform the actual factorization. The calculation of the buffer size and the analysis of the sparse matrix only need to be performed once for a given sparsity pattern while the factorization can be repeatedly applied to multiple matrices having the same sparsity pattern. Once all calls to`hipsparseXbsric02`

are complete, the temporary buffer can be deallocated.`hipsparseXbsric02`

requires a user allocated temporary buffer. Its size is returned by[hipsparseXbsric02_bufferSize()](#hipsparse__bsric0_8h_1a9573e196c9f4eacc5cf2e44a25e817d1). Furthermore, analysis meta data is required. It can be obtained by[hipsparseXbsric02_analysis()](#hipsparse__bsric0_8h_1a3f330948f32374685ad4cf062ed51af8).`hipsparseXbsric02`

reports the first zero pivot (either numerical or structural zero). The zero pivot status can be obtained by calling[hipsparseXbsric02_zeroPivot()](#hipsparse__bsric0_8h_1a4f2a00c9180b635f14c0c7d33cc5a408).`hipsparseXbsric02`

reports the first zero pivot (either numerical or structural zero). The zero pivot status can be obtained by calling[hipsparseXbsric02_zeroPivot()](#hipsparse__bsric0_8h_1a4f2a00c9180b635f14c0c7d33cc5a408).**Example**int main(int argc, char* argv[]) { // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // A sample symmetric positive definite matrix A (4x4) // with a block size of 1. This example effectively uses BSR format // for a CSR-like matrix. // Matrix A: // ( 4 1 0 0 ) // ( 1 5 2 0 ) // ( 0 2 3 1 ) // ( 0 0 1 2 ) const int m = 4; // Number of rows const int n = 4; // Number of columns const int bs = 1; // Block size const int mb = m / bs; // Number of block rows const int nb = n / bs; // Number of block columns const int nnzb = 10; // Number of non-zero blocks // BSR row pointers int hbsrRowPtr[mb + 1] = {0, 2, 5, 8, 10}; // BSR column indices int hbsrColInd[nnzb] = {0, 1, 0, 1, 2, 1, 2, 3, 2, 3}; // BSR values (single precision float for 'S'bsric02) // Values are stored column-major within each block, but with bs=1, this is simple. // The values correspond to the upper triangular part of the matrix. float hbsrVal[nnzb * bs * bs] = {4.0f, 1.0f, 1.0f, 5.0f, 2.0f, 2.0f, 3.0f, 1.0f, 1.0f, 2.0f}; // Matrix descriptor hipsparseMatDescr_t descr; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&descr)); // Set index base on descriptor HIPSPARSE_CHECK(hipsparseSetMatIndexBase(descr, HIPSPARSE_INDEX_BASE_ZERO)); // Set fill mode to lower and diagonal type to unit (required for IC02) HIPSPARSE_CHECK(hipsparseSetMatFillMode(descr, HIPSPARSE_FILL_MODE_LOWER)); HIPSPARSE_CHECK(hipsparseSetMatDiagType(descr, HIPSPARSE_DIAG_TYPE_UNIT)); // BSRIC02 info bsric02Info_t info; HIPSPARSE_CHECK(hipsparseCreateBsric02Info(&info)); // Offload data to device int* dbsrRowPtr; int* dbsrColInd; float* dbsrVal; HIP_CHECK(hipMalloc((void**)&dbsrRowPtr, sizeof(int) * (mb + 1))); HIP_CHECK(hipMalloc((void**)&dbsrColInd, sizeof(int) * nnzb)); HIP_CHECK(hipMalloc((void**)&dbsrVal, sizeof(float) * nnzb * bs * bs)); HIP_CHECK(hipMemcpy(dbsrRowPtr, hbsrRowPtr, sizeof(int) * (mb + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dbsrColInd, hbsrColInd, sizeof(int) * nnzb, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dbsrVal, hbsrVal, sizeof(float) * nnzb * bs * bs, hipMemcpyHostToDevice)); // 1. Get buffer size int bufferSize = 0; HIPSPARSE_CHECK(hipsparseSbsric02_bufferSize(handle, HIPSPARSE_DIRECTION_COLUMN, mb, nnzb, descr, dbsrVal, dbsrRowPtr, dbsrColInd, bs, info, &bufferSize)); void* dbuffer = nullptr; HIP_CHECK(hipMalloc((void**)&dbuffer, bufferSize)); // 2. Perform analysis (symbolic factorization) HIPSPARSE_CHECK(hipsparseSbsric02_analysis(handle, HIPSPARSE_DIRECTION_COLUMN, mb, nnzb, descr, dbsrVal, dbsrRowPtr, dbsrColInd, bs, info, HIPSPARSE_SOLVE_POLICY_USE_LEVEL, dbuffer)); // 3. Perform factorization (numerical computation) HIPSPARSE_CHECK(hipsparseSbsric02(handle, HIPSPARSE_DIRECTION_COLUMN, mb, nnzb, descr, dbsrVal, dbsrRowPtr, dbsrColInd, bs, info, HIPSPARSE_SOLVE_POLICY_USE_LEVEL, dbuffer)); // 4. Check for zero pivots int zeroPivot = 0; HIPSPARSE_CHECK(hipsparseXbsric02_zeroPivot(handle, info, &zeroPivot)); if(zeroPivot != -1) { printf("Error: Zero pivot detected at index %d\n", zeroPivot); // Handle error, e.g., by returning an error code } // Copy the factorized values back to host float* hbsrVal_result = new float[nnzb * bs * bs]; HIP_CHECK( hipMemcpy(hbsrVal_result, dbsrVal, sizeof(float) * nnzb * bs * bs, hipMemcpyDeviceToHost)); // Print the result (the values of the factorized matrix) printf("Successfully computed incomplete Cholesky factorization.\n"); printf("Factorized BSR values:\n"); for(int i = 0; i < nnzb * bs * bs; ++i) { printf("val[%d] = %f\n", i, hbsrVal_result[i]); } // Clean up delete[] hbsrVal_result; HIPSPARSE_CHECK(hipsparseDestroyBsric02Info(info)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(descr)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); HIP_CHECK(hipFree(dbsrRowPtr)); HIP_CHECK(hipFree(dbsrColInd)); HIP_CHECK(hipFree(dbsrVal)); HIP_CHECK(hipFree(dbuffer)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**dirA**–**[in]**direction that specified whether to count nonzero elements by[HIPSPARSE_DIRECTION_ROW](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59ae8589abecf2fbfb4b6307fd9dacd9e55)or by[HIPSPARSE_DIRECTION_COLUMN](types.html#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59a32e23f292b2377f6e60bdc90274c796c).**mb**–**[in]**number of block rows in the sparse BSR matrix.**nnzb**–**[in]**number of non-zero block entries of the sparse BSR matrix.**descrA**–**[in]**descriptor of the sparse BSR matrix.**bsrValA**–**[inout]**array of length`nnzb*blockDim*blockDim`

containing the values of the sparse BSR matrix.**bsrRowPtrA**–**[in]**array of`mb+1`

elements that point to the start of every block row of the sparse BSR matrix.**bsrColIndA**–**[in]**array of`nnzb`

elements containing the block column indices of the sparse BSR matrix.**blockDim**–**[in]**the block dimension of the BSR matrix. Between 1 and m where`m=mb*blockDim`

.**info**–**[in]**structure that holds the information collected during the analysis step.**policy**–**[in]**[HIPSPARSE_SOLVE_POLICY_NO_LEVEL](types.html#hipsparse-types_8h_1a0d98e490c94d4facc231db60baf1c3b3ac5830aa96848e832b3b375ad08abdb09)or[HIPSPARSE_SOLVE_POLICY_USE_LEVEL](types.html#hipsparse-types_8h_1a0d98e490c94d4facc231db60baf1c3b3a934309d6656638e375f0759b89fd81b5).**pBuffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`mb`

,`nnzb`

,`blockDim`

,`descrA`

,`bsrValA`

,`bsrRowPtrA`

, or`bsrColIndA`

pointer is invalid.**HIPSPARSE_STATUS_ARCH_MISMATCH**– the device is not supported.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.**HIPSPARSE_STATUS_NOT_SUPPORTED**–[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXcsric02_zeroPivot()[#](#hipsparsexcsric02-zeropivot)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseXcsric02_zeroPivot([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle,[csric02Info_t](types.html#_CPPv413csric02Info_t)info, int *position)[#](#_CPPv427hipsparseXcsric02_zeroPivot17hipsparseHandle_t13csric02Info_tPi) `hipsparseXcsric02_zeroPivot`

returns[HIPSPARSE_STATUS_ZERO_PIVOT](types.html#hipsparse-types_8h_1aa069bec7a4f24d00dab1dc4612d4de79a88ff0f0537dfe037fcf9f99ff0cf79da), if either a structural or numerical zero has been found during[hipsparseXcsric02_analysis()](#hipsparse__csric0_8h_1a047d0b5927a32cbeef5ea061ef89a4b4)or[hipsparseXcsric02()](#hipsparse__csric0_8h_1a59983f16d2c4bcf1fe265b4ba25b29a3)computation. The first zero pivot \(j\) at \(A_{j,j}\) is stored in`position`

, using same index base as the CSR matrix.`position`

can be in host or device memory. If no zero pivot has been found,`position`

is set to -1 and[HIPSPARSE_STATUS_SUCCESS](types.html#hipsparse-types_8h_1aa069bec7a4f24d00dab1dc4612d4de79a146a8a2fd27ee49132f8dcea617fc481)is returned instead.Note

`hipsparseXcsric02_zeroPivot`

is a blocking function. It might influence performance negatively.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**info**–**[in]**structure that holds the information collected during the analysis step.**position**–**[inout]**pointer to zero pivot \(j\), can be in host or device memory.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`info`

or`position`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.**HIPSPARSE_STATUS_ZERO_PIVOT**– zero pivot has been found.



## hipsparseXcsric02_bufferSize()[#](#hipsparsexcsric02-buffersize)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseScsric02_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, float *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csric02Info_t](types.html#_CPPv413csric02Info_t)info, int *pBufferSizeInBytes)[#](#_CPPv428hipsparseScsric02_bufferSize17hipsparseHandle_tiiK19hipsparseMatDescr_tPfPKiPKi13csric02Info_tPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDcsric02_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, double *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csric02Info_t](types.html#_CPPv413csric02Info_t)info, int *pBufferSizeInBytes)[#](#_CPPv428hipsparseDcsric02_bufferSize17hipsparseHandle_tiiK19hipsparseMatDescr_tPdPKiPKi13csric02Info_tPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCcsric02_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, hipComplex *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csric02Info_t](types.html#_CPPv413csric02Info_t)info, int *pBufferSizeInBytes)[#](#_CPPv428hipsparseCcsric02_bufferSize17hipsparseHandle_tiiK19hipsparseMatDescr_tP10hipComplexPKiPKi13csric02Info_tPi)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZcsric02_bufferSize([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, hipDoubleComplex *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csric02Info_t](types.html#_CPPv413csric02Info_t)info, int *pBufferSizeInBytes)[#](#_CPPv428hipsparseZcsric02_bufferSize17hipsparseHandle_tiiK19hipsparseMatDescr_tP16hipDoubleComplexPKiPKi13csric02Info_tPi) `hipsparseXcsric02_bufferSize`

returns the size of the temporary storage buffer in bytes that is required by[hipsparseXcsric02_analysis()](#hipsparse__csric0_8h_1a047d0b5927a32cbeef5ea061ef89a4b4)and[hipsparseXcsric02()](#hipsparse__csric0_8h_1a59983f16d2c4bcf1fe265b4ba25b29a3). The temporary storage buffer must be allocated by the user.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**descrA**–**[in]**descriptor of the sparse CSR matrix.**csrSortedValA**–**[in]**array of`nnz`

elements of the sparse CSR matrix.**csrSortedRowPtrA**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csrSortedColIndA**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**info**–**[out]**structure that holds the information collected during the analysis step.**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer required by[hipsparseXcsric02_analysis()](#hipsparse__csric0_8h_1a047d0b5927a32cbeef5ea061ef89a4b4)and[hipsparseXcsric02()](#hipsparse__csric0_8h_1a59983f16d2c4bcf1fe265b4ba25b29a3).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`nnz`

,`descrA`

,`csrSortedValA`

,`csrSortedRowPtrA`

,`csrSortedColIndA`

,`info`

or`pBufferSizeInBytes`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.**HIPSPARSE_STATUS_NOT_SUPPORTED**–[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXcsric02_bufferSizeExt()[#](#hipsparsexcsric02-buffersizeext)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseScsric02_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, float *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csric02Info_t](types.html#_CPPv413csric02Info_t)info, size_t *pBufferSizeInBytes)[#](#_CPPv431hipsparseScsric02_bufferSizeExt17hipsparseHandle_tiiK19hipsparseMatDescr_tPfPKiPKi13csric02Info_tP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDcsric02_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, double *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csric02Info_t](types.html#_CPPv413csric02Info_t)info, size_t *pBufferSizeInBytes)[#](#_CPPv431hipsparseDcsric02_bufferSizeExt17hipsparseHandle_tiiK19hipsparseMatDescr_tPdPKiPKi13csric02Info_tP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCcsric02_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, hipComplex *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csric02Info_t](types.html#_CPPv413csric02Info_t)info, size_t *pBufferSizeInBytes)[#](#_CPPv431hipsparseCcsric02_bufferSizeExt17hipsparseHandle_tiiK19hipsparseMatDescr_tP10hipComplexPKiPKi13csric02Info_tP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZcsric02_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, hipDoubleComplex *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csric02Info_t](types.html#_CPPv413csric02Info_t)info, size_t *pBufferSizeInBytes)[#](#_CPPv431hipsparseZcsric02_bufferSizeExt17hipsparseHandle_tiiK19hipsparseMatDescr_tP16hipDoubleComplexPKiPKi13csric02Info_tP6size_t) `hipsparseXcsric02_bufferSizeExt`

returns the size of the temporary storage buffer in bytes that is required by[hipsparseXcsric02_analysis()](#hipsparse__csric0_8h_1a047d0b5927a32cbeef5ea061ef89a4b4)and[hipsparseXcsric02()](#hipsparse__csric0_8h_1a59983f16d2c4bcf1fe265b4ba25b29a3). The temporary storage buffer must be allocated by the user.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**descrA**–**[in]**descriptor of the sparse CSR matrix.**csrSortedValA**–**[in]**array of`nnz`

elements of the sparse CSR matrix.**csrSortedRowPtrA**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csrSortedColIndA**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**info**–**[out]**structure that holds the information collected during the analysis step.**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer required by[hipsparseXcsric02_analysis()](#hipsparse__csric0_8h_1a047d0b5927a32cbeef5ea061ef89a4b4)and[hipsparseXcsric02()](#hipsparse__csric0_8h_1a59983f16d2c4bcf1fe265b4ba25b29a3).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`nnz`

,`descrA`

,`csrSortedValA`

,`csrSortedRowPtrA`

,`csrSortedColIndA`

,`info`

or`pBufferSizeInBytes`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.**HIPSPARSE_STATUS_NOT_SUPPORTED**–[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXcsric02_analysis()[#](#hipsparsexcsric02-analysis)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseScsric02_analysis([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const float *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csric02Info_t](types.html#_CPPv413csric02Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv426hipsparseScsric02_analysis17hipsparseHandle_tiiK19hipsparseMatDescr_tPKfPKiPKi13csric02Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDcsric02_analysis([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const double *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csric02Info_t](types.html#_CPPv413csric02Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv426hipsparseDcsric02_analysis17hipsparseHandle_tiiK19hipsparseMatDescr_tPKdPKiPKi13csric02Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCcsric02_analysis([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipComplex *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csric02Info_t](types.html#_CPPv413csric02Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv426hipsparseCcsric02_analysis17hipsparseHandle_tiiK19hipsparseMatDescr_tPK10hipComplexPKiPKi13csric02Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZcsric02_analysis([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, const hipDoubleComplex *csrSortedValA, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csric02Info_t](types.html#_CPPv413csric02Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv426hipsparseZcsric02_analysis17hipsparseHandle_tiiK19hipsparseMatDescr_tPK16hipDoubleComplexPKiPKi13csric02Info_t22hipsparseSolvePolicy_tPv) `hipsparseXcsric02_analysis`

performs the analysis step for[hipsparseXcsric02()](#hipsparse__csric0_8h_1a59983f16d2c4bcf1fe265b4ba25b29a3).Note

If the matrix sparsity pattern changes, the gathered information will become invalid.

Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**descrA**–**[in]**descriptor of the sparse CSR matrix.**csrSortedValA**–**[in]**array of`nnz`

elements of the sparse CSR matrix.**csrSortedRowPtrA**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csrSortedColIndA**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**info**–**[out]**structure that holds the information collected during the analysis step.**policy**–**[in]**[HIPSPARSE_SOLVE_POLICY_NO_LEVEL](types.html#hipsparse-types_8h_1a0d98e490c94d4facc231db60baf1c3b3ac5830aa96848e832b3b375ad08abdb09)or[HIPSPARSE_SOLVE_POLICY_USE_LEVEL](types.html#hipsparse-types_8h_1a0d98e490c94d4facc231db60baf1c3b3a934309d6656638e375f0759b89fd81b5).**pBuffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`nnz`

,`descrA`

,`csrSortedValA`

,`csrSortedRowPtrA`

,`csrSortedColIndA`

,`info`

or`pBuffer`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.**HIPSPARSE_STATUS_NOT_SUPPORTED**–[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXcsric02()[#](#hipsparsexcsric02)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseScsric02([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, float *csrSortedValA_valM, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csric02Info_t](types.html#_CPPv413csric02Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv417hipsparseScsric0217hipsparseHandle_tiiK19hipsparseMatDescr_tPfPKiPKi13csric02Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDcsric02([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, double *csrSortedValA_valM, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csric02Info_t](types.html#_CPPv413csric02Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv417hipsparseDcsric0217hipsparseHandle_tiiK19hipsparseMatDescr_tPdPKiPKi13csric02Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCcsric02([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, hipComplex *csrSortedValA_valM, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csric02Info_t](types.html#_CPPv413csric02Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv417hipsparseCcsric0217hipsparseHandle_tiiK19hipsparseMatDescr_tP10hipComplexPKiPKi13csric02Info_t22hipsparseSolvePolicy_tPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZcsric02([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int nnz, const[hipsparseMatDescr_t](types.html#_CPPv419hipsparseMatDescr_t)descrA, hipDoubleComplex *csrSortedValA_valM, const int *csrSortedRowPtrA, const int *csrSortedColIndA,[csric02Info_t](types.html#_CPPv413csric02Info_t)info,[hipsparseSolvePolicy_t](types.html#_CPPv422hipsparseSolvePolicy_t)policy, void *pBuffer)[#](#_CPPv417hipsparseZcsric0217hipsparseHandle_tiiK19hipsparseMatDescr_tP16hipDoubleComplexPKiPKi13csric02Info_t22hipsparseSolvePolicy_tPv) Incomplete Cholesky factorization with 0 fill-ins and no pivoting using CSR storage format.

`hipsparseXcsric02`

computes the incomplete Cholesky factorization with 0 fill-ins and no pivoting of a sparse \(m \times m\) CSR matrix \(A\), such that\[ A \approx LL^T \]where the lower triangular matrix \(L\) is computed using:\[\begin{split} L_{ij} = \left\{ \begin{array}{ll} \sqrt{A_{jj} - \sum_{k=0}^{j-1}(L_{jk})^{2}}, & \text{if i == j} \\ \frac{1}{L_{jj}}(A_{jj} - \sum_{k=0}^{j-1}L_{ik} \times L_{jk}), & \text{if i > j} \end{array} \right. \end{split}\]for each entry found in the CSR matrix \(A\).Computing the above incomplete Cholesky factorization requires three steps to complete. First, the user determines the size of the required temporary storage buffer by calling

[hipsparseXcsric02_bufferSize()](#hipsparse__csric0_8h_1ae324850728daf314b0f24bd9376cb91d). Once this buffer size has been determined, the user allocates the buffer and passes it to[hipsparseXcsric02_analysis()](#hipsparse__csric0_8h_1a047d0b5927a32cbeef5ea061ef89a4b4). This will perform analysis on the sparsity pattern of the matrix. Finally, the user calls`hipsparseScsric02`

,`hipsparseDcsric02`

,`hipsparseCcsric02`

, or`hipsparseZcsric02`

to perform the actual factorization. The calculation of the buffer size and the analysis of the sparse matrix only need to be performed once for a given sparsity pattern while the factorization can be repeatedly applied to multiple matrices having the same sparsity pattern. Once all calls to[hipsparseXcsric02()](#hipsparse__csric0_8h_1a59983f16d2c4bcf1fe265b4ba25b29a3)are complete, the temporary buffer can be deallocated.When computing the Cholesky factorization, it is possible that \(L_{jj} == 0\) which would result in a division by zero. This could occur from either \(A_{jj}\) not existing in the sparse CSR matrix (referred to as a structural zero) or because \(A_{jj} - \sum_{k=0}^{j-1}(L_{jk})^{2} == 0\) (referred to as a numerical zero). For example, running the Cholesky factorization on the following matrix:

\[\begin{split} \begin{bmatrix} 2 & 1 & 0 \\ 1 & 2 & 1 \\ 0 & 1 & 2 \end{bmatrix} \end{split}\]results in a successful Cholesky factorization, however running with the matrix:\[\begin{split} \begin{bmatrix} 2 & 1 & 0 \\ 1 & 1/2 & 1 \\ 0 & 1 & 2 \end{bmatrix} \end{split}\]results in a numerical zero because:\[\begin{split} \begin{array}{ll} L_{00} &= \sqrt{2} \\ L_{10} &= \frac{1}{\sqrt{2}} \\ L_{11} &= \sqrt{\frac{1}{2} - (\frac{1}{\sqrt{2}})^2} &= 0 \end{array} \end{split}\]The user can detect the presence of a structural zero by calling[hipsparseXcsric02_zeroPivot()](#hipsparse__csric0_8h_1a8400c63b72d75beae59167a0e790eac2)after[hipsparseXcsric02_analysis()](#hipsparse__csric0_8h_1a047d0b5927a32cbeef5ea061ef89a4b4)and/or the presence of a structural or numerical zero by calling[hipsparseXcsric02_zeroPivot()](#hipsparse__csric0_8h_1a8400c63b72d75beae59167a0e790eac2)after[hipsparseXcsric02()](#hipsparse__csric0_8h_1a59983f16d2c4bcf1fe265b4ba25b29a3):In both cases,hipsparseDcsric02(handle, m, nnz, descrM, csrVal, csrRowPtr, csrColInd, info, HIPSPARSE_SOLVE_POLICY_USE_LEVEL, buffer); // Check for zero pivot if(CUSPARSE_STATUS_ZERO_PIVOT == hipsparseXcsric02_zeroPivot(handle, info, &position)) { printf("L has structural and/or numerical zero at L(%d,%d)\n", position, position); }

[hipsparseXcsric02_zeroPivot()](#hipsparse__csric0_8h_1a8400c63b72d75beae59167a0e790eac2)will report the first zero pivot (either numerical or structural) found. See full example below. The user can also set the diagonal type to be \(1\) using[hipsparseSetMatDiagType()](auxiliary.html#hipsparse-auxiliary_8h_1aec6fa039793196011f15cfb0b21c2b59)which will interpret the matrix \(A\) as having ones on its diagonal (even if no nonzero exists in the sparsity pattern).`hipsparseXcsric02`

computes the Cholesky factorization inplace meaning that the values array`csrSortedValA_valM`

of the \(A\) matrix is overwritten with the \(L\) matrix stored in the lower triangular part of \(A\):\[\begin{split} \begin{align} \begin{bmatrix} a_{00} & a_{01} & a_{02} \\ a_{10} & a_{11} & a_{12} \\ a_{20} & a_{21} & a_{22} \end{bmatrix} \rightarrow \begin{bmatrix} l_{00} & a_{01} & a_{02} \\ l_{10} & l_{11} & a_{12} \\ l_{20} & l_{21} & l_{22} \end{bmatrix} \end{align} \end{split}\]The row pointer array`csrSortedRowPtrA`

and the column indices array`csrSortedColIndA`

remain the same for \(A\) and the output as the incomplete factorization does not generate new nonzeros in the output which do not already exist in \(A\).The performance of computing Cholesky factorization with hipSPARSE greatly depends on the sparisty pattern the the matrix \(A\) as this is what determines the amount of parallelism available.

**Example**int main(int argc, char* argv[]) { // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // A sample symmetric positive definite matrix A (4x4) in CSR format. // The 'S' in Scsric02 indicates single precision float. // Matrix A: // ( 4 1 0 0 ) // ( 1 5 2 0 ) // ( 0 2 3 1 ) // ( 0 0 1 2 ) // This matrix is symmetric. For IC02, we typically provide the full matrix // or just the lower/upper part if using `HIPSPARSE_MATRIX_TYPE_SYMMETRIC` // with the descriptor. Here, we provide elements for both lower and upper parts // for simplicity, but the factorization will operate on the implicitly // symmetric matrix and produce the lower triangular factor L. int m = 4; // Number of rows int n = 4; // Number of columns (equal to m for Cholesky) int nnz = 10; // Number of non-zero elements (counting only one side for symmetric) // CSR row pointers int hcsrRowPtr[5] = {0, 2, 5, 8, 10}; // CSR column indices // These indices correspond to the non-zero values used below. // For a symmetric matrix A, we implicitly work with A_lower. // The output will be L. int hcsrColInd[10] = {0, 1, 0, 1, 2, 1, 2, 3, 2, 3}; // CSR values (single precision float for 'S'csric02) // The factorization computes the lower triangular L factor. // The input values represent the entries of A that correspond to the non-zero pattern. float hcsrVal[10] = {4.0f, 1.0f, 1.0f, 5.0f, 2.0f, 2.0f, 3.0f, 1.0f, 1.0f, 2.0f}; // Matrix descriptor hipsparseMatDescr_t descr; HIPSPARSE_CHECK(hipsparseCreateMatDescr(&descr)); // Set index base on descriptor HIPSPARSE_CHECK(hipsparseSetMatIndexBase(descr, HIPSPARSE_INDEX_BASE_ZERO)); // For incomplete Cholesky, the L factor is computed. // L is lower triangular with a unit diagonal. HIPSPARSE_CHECK(hipsparseSetMatFillMode(descr, HIPSPARSE_FILL_MODE_LOWER)); HIPSPARSE_CHECK(hipsparseSetMatDiagType(descr, HIPSPARSE_DIAG_TYPE_UNIT)); // Optionally set matrix type to symmetric if only storing one triangle of A // HIPSPARSE_CHECK(hipsparseSetMatType(descr, HIPSPARSE_MATRIX_TYPE_SYMMETRIC)); // CSRIC02 info csric02Info_t info; HIPSPARSE_CHECK(hipsparseCreateCsric02Info(&info)); // Offload data to device int* dcsrRowPtr; int* dcsrColInd; float* dcsrVal; // This will store the factorized L values HIP_CHECK(hipMalloc((void**)&dcsrRowPtr, sizeof(int) * (m + 1))); HIP_CHECK(hipMalloc((void**)&dcsrColInd, sizeof(int) * nnz)); HIP_CHECK( hipMalloc((void**)&dcsrVal, sizeof(float) * nnz)); // Note: Same size as input, values will be overwritten HIP_CHECK(hipMemcpy(dcsrRowPtr, hcsrRowPtr, sizeof(int) * (m + 1), hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrColInd, hcsrColInd, sizeof(int) * nnz, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dcsrVal, hcsrVal, sizeof(float) * nnz, hipMemcpyHostToDevice)); // 1. Get buffer size int bufferSize = 0; HIPSPARSE_CHECK(hipsparseScsric02_bufferSize( handle, m, nnz, descr, dcsrVal, dcsrRowPtr, dcsrColInd, info, &bufferSize)); void* dbuffer = nullptr; HIP_CHECK(hipMalloc((void**)&dbuffer, bufferSize)); // 2. Perform analysis (symbolic factorization) // This step analyzes the sparsity pattern of A to determine the structure of L. HIPSPARSE_CHECK( hipsparseScsric02_analysis(handle, m, nnz, descr, dcsrVal, dcsrRowPtr, dcsrColInd, info, HIPSPARSE_SOLVE_POLICY_USE_LEVEL, // Policy for analysis dbuffer)); // 3. Perform factorization (numerical computation) // This step computes the actual numerical values of L, stored in dcsrVal. HIPSPARSE_CHECK(hipsparseScsric02(handle, m, nnz, descr, dcsrVal, dcsrRowPtr, dcsrColInd, info, HIPSPARSE_SOLVE_POLICY_USE_LEVEL, // Policy for factorization dbuffer)); // 4. Check for zero pivots // A zero pivot can occur during factorization, indicating a numerical breakdown. int zeroPivot = 0; // -1 if no zero pivot, otherwise the row index of the first zero pivot HIPSPARSE_CHECK(hipsparseXcsric02_zeroPivot(handle, info, &zeroPivot)); if(zeroPivot != -1) { printf("Error: Zero pivot detected during IC02 factorization at row index %d\n", zeroPivot); // Depending on your application, you might want to handle this error // or switch to a different preconditioner. } else { printf("CSRIC02 factorization completed successfully (no zero pivots detected).\n"); } // Copy the factorized values (L) back to host float* hcsrVal_result = new float[nnz]; HIP_CHECK(hipMemcpy(hcsrVal_result, dcsrVal, sizeof(float) * nnz, hipMemcpyDeviceToHost)); // Print the result (the values of the factorized L) printf("\nFactorized CSR values (L factor):\n"); for(int i = 0; i < nnz; ++i) { printf("val[%d] = %f\n", i, hcsrVal_result[i]); } // Clean up delete[] hcsrVal_result; HIPSPARSE_CHECK(hipsparseDestroyCsric02Info(info)); HIPSPARSE_CHECK(hipsparseDestroyMatDescr(descr)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); HIP_CHECK(hipFree(dcsrRowPtr)); HIP_CHECK(hipFree(dcsrColInd)); HIP_CHECK(hipFree(dcsrVal)); HIP_CHECK(hipFree(dbuffer)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**number of rows of the sparse CSR matrix.**nnz**–**[in]**number of non-zero entries of the sparse CSR matrix.**descrA**–**[in]**descriptor of the sparse CSR matrix.**csrSortedValA_valM**–**[inout]**array of`nnz`

elements of the sparse CSR matrix.**csrSortedRowPtrA**–**[in]**array of`m+1`

elements that point to the start of every row of the sparse CSR matrix.**csrSortedColIndA**–**[in]**array of`nnz`

elements containing the column indices of the sparse CSR matrix.**info**–**[in]**structure that holds the information collected during the analysis step.**policy**–**[in]**[HIPSPARSE_SOLVE_POLICY_NO_LEVEL](types.html#hipsparse-types_8h_1a0d98e490c94d4facc231db60baf1c3b3ac5830aa96848e832b3b375ad08abdb09)or[HIPSPARSE_SOLVE_POLICY_USE_LEVEL](types.html#hipsparse-types_8h_1a0d98e490c94d4facc231db60baf1c3b3a934309d6656638e375f0759b89fd81b5).**pBuffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`nnz`

,`descrA`

,`csrSortedValA_valM`

,`csrSortedRowPtrA`

or`csrSortedColIndA`

pointer is invalid.**HIPSPARSE_STATUS_ARCH_MISMATCH**– the device is not supported.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.**HIPSPARSE_STATUS_NOT_SUPPORTED**–[hipsparseMatrixType_t](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)!=[HIPSPARSE_MATRIX_TYPE_GENERAL](types.html#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8bae8a4b2414c40725f416edde7ec8af5f8).



## hipsparseXgtsv2_bufferSizeExt()[#](#hipsparsexgtsv2-buffersizeext)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSgtsv2_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const float *dl, const float *d, const float *du, const float *B, int ldb, size_t *pBufferSizeInBytes)[#](#_CPPv429hipsparseSgtsv2_bufferSizeExt17hipsparseHandle_tiiPKfPKfPKfPKfiP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDgtsv2_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const double *dl, const double *d, const double *du, const double *B, int ldb, size_t *pBufferSizeInBytes)[#](#_CPPv429hipsparseDgtsv2_bufferSizeExt17hipsparseHandle_tiiPKdPKdPKdPKdiP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCgtsv2_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const hipComplex *dl, const hipComplex *d, const hipComplex *du, const hipComplex *B, int ldb, size_t *pBufferSizeInBytes)[#](#_CPPv429hipsparseCgtsv2_bufferSizeExt17hipsparseHandle_tiiPK10hipComplexPK10hipComplexPK10hipComplexPK10hipComplexiP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZgtsv2_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const hipDoubleComplex *dl, const hipDoubleComplex *d, const hipDoubleComplex *du, const hipDoubleComplex *B, int ldb, size_t *pBufferSizeInBytes)[#](#_CPPv429hipsparseZgtsv2_bufferSizeExt17hipsparseHandle_tiiPK16hipDoubleComplexPK16hipDoubleComplexPK16hipDoubleComplexPK16hipDoubleComplexiP6size_t) `hipsparseSgtsv2_bufferSizeExt`

returns the size of the temporary storage buffer that is required by[hipsparseXgtsv2()](#hipsparse__gtsv_8h_1a81ff4e9b3e475b6189067c5d836c9eee). The temporary storage buffer must be allocated by the user.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the hipSPARSE library context queue.**m**–**[in]**size of the tri-diagonal linear system (must be >= 2).**n**–**[in]**number of columns in the dense matrix B.**dl**–**[in]**lower diagonal of tri-diagonal system. First entry must be zero.**d**–**[in]**main diagonal of tri-diagonal system.**du**–**[in]**upper diagonal of tri-diagonal system. Last entry must be zero.**B**–**[in]**Dense matrix of size (`ldb`

,`n`

).**ldb**–**[in]**Leading dimension of B. Must satisfy`ldb`

>= max(1, m).**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer required by[hipsparseXgtsv2()](#hipsparse__gtsv_8h_1a81ff4e9b3e475b6189067c5d836c9eee).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`ldb`

,`dl`

,`d`

,`du`

,`B`

or`pBufferSizeInBytes`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.



## hipsparseXgtsv2()[#](#hipsparsexgtsv2)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSgtsv2([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const float *dl, const float *d, const float *du, float *B, int ldb, void *pBuffer)[#](#_CPPv415hipsparseSgtsv217hipsparseHandle_tiiPKfPKfPKfPfiPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDgtsv2([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const double *dl, const double *d, const double *du, double *B, int ldb, void *pBuffer)[#](#_CPPv415hipsparseDgtsv217hipsparseHandle_tiiPKdPKdPKdPdiPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCgtsv2([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const hipComplex *dl, const hipComplex *d, const hipComplex *du, hipComplex *B, int ldb, void *pBuffer)[#](#_CPPv415hipsparseCgtsv217hipsparseHandle_tiiPK10hipComplexPK10hipComplexPK10hipComplexP10hipComplexiPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZgtsv2([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const hipDoubleComplex *dl, const hipDoubleComplex *d, const hipDoubleComplex *du, hipDoubleComplex *B, int ldb, void *pBuffer)[#](#_CPPv415hipsparseZgtsv217hipsparseHandle_tiiPK16hipDoubleComplexPK16hipDoubleComplexPK16hipDoubleComplexP16hipDoubleComplexiPv) Tridiagonal solver with pivoting.

`hipsparseXgtsv2`

solves a tridiagonal system for multiple right hand sides using pivoting\[ T*B = B \]where \(T\) is a sparse tridiagonal matrix and \(B\) is a dense \(ldb \times n\) matrix storing the right-hand side vectors in column order. The tridiagonal matrix \(T\) is defined by three vectors:`dl`

for the lower diagonal,`d`

for the main diagonal and`du`

for the upper diagonal.Solving the tridiagonal system involves two steps. First, the user calls

[hipsparseXgtsv2_bufferSizeExt()](#hipsparse__gtsv_8h_1a56f87bb50ca231c2ae79acaf59f99311)in order to determine the size of the required temporary storage buffer. Once determined, the user allocates this buffer and passes it to[hipsparseXgtsv2()](#hipsparse__gtsv_8h_1a81ff4e9b3e475b6189067c5d836c9eee)to perform the actual solve. The \(B\) dense matrix, which initially stores the`n`

right-hand side vectors, is overwritten with the`n`

solution vectors after the call to[hipsparseXgtsv2()](#hipsparse__gtsv_8h_1a81ff4e9b3e475b6189067c5d836c9eee).**Example**int main(int argc, char* argv[]) { // Size of square tridiagonal matrix int m = 5; // Number of columns in right-hand side (column ordered) matrix int n = 3; // Leading dimension of right-hand side (column ordered) matrix int ldb = m; // Host tri-diagonal matrix // 2 3 0 0 0 // 2 4 2 0 0 // 0 1 1 1 0 // 0 0 1 3 1 // 0 0 0 1 4 std::vector<float> hdl = {0.0f, 2.0f, 1.0f, 1.0f, 1.0f}; std::vector<float> hd = {2.0f, 4.0f, 1.0f, 3.0f, 4.0f}; std::vector<float> hdu = {3.0f, 2.0f, 1.0f, 1.0f, 0.0f}; // Host right-hand side column vectors std::vector<float> hB(ldb * n, 2.0f); float* ddl = nullptr; float* dd = nullptr; float* ddu = nullptr; float* dB = nullptr; HIP_CHECK(hipMalloc((void**)&ddl, sizeof(float) * m)); HIP_CHECK(hipMalloc((void**)&dd, sizeof(float) * m)); HIP_CHECK(hipMalloc((void**)&ddu, sizeof(float) * m)); HIP_CHECK(hipMalloc((void**)&dB, sizeof(float) * ldb * n)); HIP_CHECK(hipMemcpy(ddl, hdl.data(), sizeof(float) * m, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dd, hd.data(), sizeof(float) * m, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(ddu, hdu.data(), sizeof(float) * m, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dB, hB.data(), sizeof(float) * ldb * n, hipMemcpyHostToDevice)); // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // 1. Get buffer size size_t bufferSize = 0; HIPSPARSE_CHECK( hipsparseSgtsv2_bufferSizeExt(handle, m, m, ddl, dd, ddu, dB, ldb, &bufferSize)); void* dbuffer = nullptr; HIP_CHECK(hipMalloc((void**)&dbuffer, bufferSize)); // 2. Perform tridiagonal solve with pivoting // The solution is computed and stored in the dB vector. HIPSPARSE_CHECK(hipsparseSgtsv2(handle, m, m, ddl, dd, ddu, dB, ldb, dbuffer)); // Copy solution back to host from dB HIP_CHECK(hipMemcpy(hB.data(), dB, sizeof(float) * m, hipMemcpyDeviceToHost)); // Print the solution printf("Solution for the tridiagonal system:\n"); for(int i = 0; i < m; ++i) { printf(" x[%d] = %f\n", i, hB[i]); } // Clean up HIP_CHECK(hipFree(ddl)); HIP_CHECK(hipFree(dd)); HIP_CHECK(hipFree(ddu)); HIP_CHECK(hipFree(dB)); HIP_CHECK(hipFree(dbuffer)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

Note

This routine supports execution in a hipGraph context.

- Parameters:
**handle**–**[in]**handle to the hipSPARSE library context queue.**m**–**[in]**size of the tri-diagonal linear system (must be >= 2).**n**–**[in]**number of columns in the dense matrix B.**dl**–**[in]**lower diagonal of tri-diagonal system. First entry must be zero.**d**–**[in]**main diagonal of tri-diagonal system.**du**–**[in]**upper diagonal of tri-diagonal system. Last entry must be zero.**B**–**[inout]**Dense matrix of size (`ldb`

,`n`

).**ldb**–**[in]**Leading dimension of B. Must satisfy`ldb`

>= max(1, m).**pBuffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`ldb`

,`dl`

,`d`

,`du`

,`B`

or`pBuffer`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.



## hipsparseXgtsv2_nopivot_bufferSizeExt()[#](#hipsparsexgtsv2-nopivot-buffersizeext)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSgtsv2_nopivot_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const float *dl, const float *d, const float *du, const float *B, int ldb, size_t *pBufferSizeInBytes)[#](#_CPPv437hipsparseSgtsv2_nopivot_bufferSizeExt17hipsparseHandle_tiiPKfPKfPKfPKfiP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDgtsv2_nopivot_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const double *dl, const double *d, const double *du, const double *B, int ldb, size_t *pBufferSizeInBytes)[#](#_CPPv437hipsparseDgtsv2_nopivot_bufferSizeExt17hipsparseHandle_tiiPKdPKdPKdPKdiP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCgtsv2_nopivot_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const hipComplex *dl, const hipComplex *d, const hipComplex *du, const hipComplex *B, int ldb, size_t *pBufferSizeInBytes)[#](#_CPPv437hipsparseCgtsv2_nopivot_bufferSizeExt17hipsparseHandle_tiiPK10hipComplexPK10hipComplexPK10hipComplexPK10hipComplexiP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZgtsv2_nopivot_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const hipDoubleComplex *dl, const hipDoubleComplex *d, const hipDoubleComplex *du, const hipDoubleComplex *B, int ldb, size_t *pBufferSizeInBytes)[#](#_CPPv437hipsparseZgtsv2_nopivot_bufferSizeExt17hipsparseHandle_tiiPK16hipDoubleComplexPK16hipDoubleComplexPK16hipDoubleComplexPK16hipDoubleComplexiP6size_t) `hipsparseXgtsv2_nopivot_bufferSizeExt`

returns the size of the temporary storage buffer in bytes that is required by[hipsparseXgtsv2_nopivot()](#hipsparse__gtsv__nopivot_8h_1aeefdaf91be96a281d75377b56ffe8b5c). The temporary storage buffer must be allocated by the user.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**size of the tri-diagonal linear system (must be >= 2).**n**–**[in]**number of columns in the dense matrix B.**dl**–**[in]**lower diagonal of tri-diagonal system. First entry must be zero.**d**–**[in]**main diagonal of tri-diagonal system.**du**–**[in]**upper diagonal of tri-diagonal system. Last entry must be zero.**B**–**[in]**Dense matrix of size (`ldb`

,`n`

).**ldb**–**[in]**Leading dimension of B. Must satisfy`ldb`

>= max(1, m).**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer required by hipsparseSgtsv2_nopivot “hipsparseXgtsv2_nopivot()”.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`ldb`

,`dl`

,`d`

,`du`

,`B`

or`pBufferSizeInBytes`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.



## hipsparseXgtsv2_nopivot()[#](#hipsparsexgtsv2-nopivot)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSgtsv2_nopivot([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const float *dl, const float *d, const float *du, float *B, int ldb, void *pBuffer)[#](#_CPPv423hipsparseSgtsv2_nopivot17hipsparseHandle_tiiPKfPKfPKfPfiPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDgtsv2_nopivot([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const double *dl, const double *d, const double *du, double *B, int ldb, void *pBuffer)[#](#_CPPv423hipsparseDgtsv2_nopivot17hipsparseHandle_tiiPKdPKdPKdPdiPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCgtsv2_nopivot([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const hipComplex *dl, const hipComplex *d, const hipComplex *du, hipComplex *B, int ldb, void *pBuffer)[#](#_CPPv423hipsparseCgtsv2_nopivot17hipsparseHandle_tiiPK10hipComplexPK10hipComplexPK10hipComplexP10hipComplexiPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZgtsv2_nopivot([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, int n, const hipDoubleComplex *dl, const hipDoubleComplex *d, const hipDoubleComplex *du, hipDoubleComplex *B, int ldb, void *pBuffer)[#](#_CPPv423hipsparseZgtsv2_nopivot17hipsparseHandle_tiiPK16hipDoubleComplexPK16hipDoubleComplexPK16hipDoubleComplexP16hipDoubleComplexiPv) Tridiagonal solver (no pivoting)

`hipsparseXgtsv2_nopivot`

solves a tridiagonal linear system for multiple right-hand sides without pivoting\[ T*B = B \]where \(T\) is a sparse tridiagonal matrix and \(B\) is a dense \(ldb \times n\) matrix storing the right-hand side vectors in column order. The tridiagonal matrix \(T\) is defined by three vectors:`dl`

for the lower diagonal,`d`

for the main diagonal and`du`

for the upper diagonal.Solving the tridiagonal system with multiple right-hand sides without pivoting involves two steps. First, the user calls

[hipsparseXgtsv2_nopivot_bufferSizeExt()](#hipsparse__gtsv__nopivot_8h_1a45a8262adecc55d312e562f57e8276aa)in order to determine the size of the required temporary storage buffer. Once determined, the user allocates this buffer and passes it to[hipsparseXgtsv2_nopivot()](#hipsparse__gtsv__nopivot_8h_1aeefdaf91be96a281d75377b56ffe8b5c)to perform the actual solve. The \(B\) dense matrix, which initially stores the`n`

right-hand side vectors, is overwritten with the`n`

solution vectors after the call to[hipsparseXgtsv2_nopivot()](#hipsparse__gtsv__nopivot_8h_1aeefdaf91be96a281d75377b56ffe8b5c).**Example**int main(int argc, char* argv[]) { // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // Size of square tridiagonal matrix int m = 5; // Number of columns in right-hand side (column ordered) matrix int n = 3; // Leading dimension of right-hand side (column ordered) matrix int ldb = m; // Host tri-diagonal matrix // 2 -1 0 0 0 // -1 2 -1 0 0 // 0 -1 2 -1 0 // 0 0 -1 2 -1 // 0 0 0 -1 2 std::vector<float> hdl = {0.0f, -1.0f, -1.0f, -1.0f, -1.0f}; std::vector<float> hd = {2.0f, 2.0f, 2.0f, 2.0f, 2.0f}; std::vector<float> hdu = {-1.0f, -1.0f, -1.0f, -1.0f, 0.0f}; // Host right-hand side column vectors std::vector<float> hB(ldb * n, 1.0f); float* ddl = nullptr; float* dd = nullptr; float* ddu = nullptr; float* dB = nullptr; HIP_CHECK(hipMalloc((void**)&ddl, sizeof(float) * m)); HIP_CHECK(hipMalloc((void**)&dd, sizeof(float) * m)); HIP_CHECK(hipMalloc((void**)&ddu, sizeof(float) * m)); HIP_CHECK(hipMalloc((void**)&dB, sizeof(float) * ldb * n)); HIP_CHECK(hipMemcpy(ddl, hdl.data(), sizeof(float) * m, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dd, hd.data(), sizeof(float) * m, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(ddu, hdu.data(), sizeof(float) * m, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dB, hB.data(), sizeof(float) * ldb * n, hipMemcpyHostToDevice)); // Obtain required buffer size size_t bufferSize; HIPSPARSE_CHECK( hipsparseSgtsv2_nopivot_bufferSizeExt(handle, m, n, ddl, dd, ddu, dB, ldb, &bufferSize)); void* dbuffer; HIP_CHECK(hipMalloc(&dbuffer, bufferSize)); HIPSPARSE_CHECK(hipsparseSgtsv2_nopivot(handle, m, n, ddl, dd, ddu, dB, ldb, dbuffer)); // Copy right-hand side to host HIP_CHECK(hipMemcpy(hB.data(), dB, sizeof(float) * ldb * n, hipMemcpyDeviceToHost)); // Print the solution printf("Solution for the tridiagonal system:\n"); for(int i = 0; i < m; ++i) { printf(" x[%d] = %f\n", i, hB[i]); } // Clean up HIP_CHECK(hipFree(ddl)); HIP_CHECK(hipFree(dd)); HIP_CHECK(hipFree(ddu)); HIP_CHECK(hipFree(dB)); HIP_CHECK(hipFree(dbuffer)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**size of the tri-diagonal linear system (must be >= 2).**n**–**[in]**number of columns in the dense matrix B.**dl**–**[in]**lower diagonal of tri-diagonal system. First entry must be zero.**d**–**[in]**main diagonal of tri-diagonal system.**du**–**[in]**upper diagonal of tri-diagonal system. Last entry must be zero.**B**–**[inout]**Dense matrix of size (`ldb`

,`n`

).**ldb**–**[in]**Leading dimension of B. Must satisfy`ldb`

>= max(1, m).**pBuffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`n`

,`ldb`

,`dl`

,`d`

,`du`

,`B`

or`pBuffer`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.



## hipsparseXgtsv2StridedBatch_bufferSizeExt()[#](#hipsparsexgtsv2stridedbatch-buffersizeext)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSgtsv2StridedBatch_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, const float *dl, const float *d, const float *du, const float *x, int batchCount, int batchStride, size_t *pBufferSizeInBytes)[#](#_CPPv441hipsparseSgtsv2StridedBatch_bufferSizeExt17hipsparseHandle_tiPKfPKfPKfPKfiiP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDgtsv2StridedBatch_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, const double *dl, const double *d, const double *du, const double *x, int batchCount, int batchStride, size_t *pBufferSizeInBytes)[#](#_CPPv441hipsparseDgtsv2StridedBatch_bufferSizeExt17hipsparseHandle_tiPKdPKdPKdPKdiiP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCgtsv2StridedBatch_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, const hipComplex *dl, const hipComplex *d, const hipComplex *du, const hipComplex *x, int batchCount, int batchStride, size_t *pBufferSizeInBytes)[#](#_CPPv441hipsparseCgtsv2StridedBatch_bufferSizeExt17hipsparseHandle_tiPK10hipComplexPK10hipComplexPK10hipComplexPK10hipComplexiiP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZgtsv2StridedBatch_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, const hipDoubleComplex *dl, const hipDoubleComplex *d, const hipDoubleComplex *du, const hipDoubleComplex *x, int batchCount, int batchStride, size_t *pBufferSizeInBytes)[#](#_CPPv441hipsparseZgtsv2StridedBatch_bufferSizeExt17hipsparseHandle_tiPK16hipDoubleComplexPK16hipDoubleComplexPK16hipDoubleComplexPK16hipDoubleComplexiiP6size_t) `hipsparseXgtsv2StridedBatch_bufferSizeExt`

returns the size of the temporary storage buffer in bytes that is required by[hipsparseXgtsv2StridedBatch()](#hipsparse__gtsv__strided__batch_8h_1ac0c3cb9c297452cf07aa9456803d18c9). The temporary storage buffer must be allocated by the user.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**size of the tri-diagonal linear system.**dl**–**[in]**lower diagonal of tri-diagonal system where the ith system lower diagonal starts at`dl+batchStride*i`

.**d**–**[in]**main diagonal of tri-diagonal system where the ith system diagonal starts at`d+batchStride*i`

.**du**–**[in]**upper diagonal of tri-diagonal system where the ith system upper diagonal starts at`du+batchStride*i`

.**x**–**[inout]**Dense array of righthand-sides where the ith righthand-side starts at`x+batchStride*i`

.**batchCount**–**[in]**The number of systems to solve.**batchStride**–**[in]**The number of elements that separate each system. Must satisfy`batchStride`

>= m.**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer required by hipsparseSgtsv2StridedBatch “hipsparseXgtsv2StridedBatch()”.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`batchCount`

,`batchStride`

,`dl`

,`d`

,`du`

,`x`

or`pBufferSizeInBytes`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.



## hipsparseXgtsv2StridedBatch()[#](#hipsparsexgtsv2stridedbatch)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSgtsv2StridedBatch([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, const float *dl, const float *d, const float *du, float *x, int batchCount, int batchStride, void *pBuffer)[#](#_CPPv427hipsparseSgtsv2StridedBatch17hipsparseHandle_tiPKfPKfPKfPfiiPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDgtsv2StridedBatch([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, const double *dl, const double *d, const double *du, double *x, int batchCount, int batchStride, void *pBuffer)[#](#_CPPv427hipsparseDgtsv2StridedBatch17hipsparseHandle_tiPKdPKdPKdPdiiPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCgtsv2StridedBatch([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, const hipComplex *dl, const hipComplex *d, const hipComplex *du, hipComplex *x, int batchCount, int batchStride, void *pBuffer)[#](#_CPPv427hipsparseCgtsv2StridedBatch17hipsparseHandle_tiPK10hipComplexPK10hipComplexPK10hipComplexP10hipComplexiiPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZgtsv2StridedBatch([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int m, const hipDoubleComplex *dl, const hipDoubleComplex *d, const hipDoubleComplex *du, hipDoubleComplex *x, int batchCount, int batchStride, void *pBuffer)[#](#_CPPv427hipsparseZgtsv2StridedBatch17hipsparseHandle_tiPK16hipDoubleComplexPK16hipDoubleComplexPK16hipDoubleComplexP16hipDoubleComplexiiPv) Strided Batch tridiagonal solver (no pivoting)

`hipsparseXgtsv2StridedBatch`

solves a batched tridiagonal linear system\[ T^{i}*x^{i} = x^{i} \]where for each batch \(i=0\ldots\)`batchCount`

, \(T^{i}\) is a sparse tridiagonal matrix and \(x^{i}\) is a dense right-hand side vector. All of the tridiagonal matrices, \(T^{i}\), are packed one after the other into three vectors:`dl`

for the lower diagonals,`d`

for the main diagonals and`du`

for the upper diagonals. See below for a description of what this strided memory pattern looks like.Solving the batched tridiagonal system involves two steps. First, the user calls

[hipsparseXgtsv2StridedBatch_bufferSizeExt()](#hipsparse__gtsv__strided__batch_8h_1a50afa2b448621212cd71139a08da48be)in order to determine the size of the required temporary storage buffer. Once determined, the user allocates this buffer and passes it to[hipsparseXgtsv2StridedBatch()](#hipsparse__gtsv__strided__batch_8h_1ac0c3cb9c297452cf07aa9456803d18c9)to perform the actual solve. The \(x^{i}\) vectors, which initially stores the right-hand side values, are overwritten with the solution after the call to[hipsparseXgtsv2StridedBatch()](#hipsparse__gtsv__strided__batch_8h_1ac0c3cb9c297452cf07aa9456803d18c9).The strided batch routines write each batch matrix one after the other in memory. For example, consider the following batch matrices:

\[\begin{split} \begin{bmatrix} t^{0}_{00} & t^{0}_{01} & 0 \\ t^{0}_{10} & t^{0}_{11} & t^{0}_{12} \\ 0 & t^{0}_{21} & t^{0}_{22} \end{bmatrix} \begin{bmatrix} t^{1}_{00} & t^{1}_{01} & 0 \\ t^{1}_{10} & t^{1}_{11} & t^{1}_{12} \\ 0 & t^{1}_{21} & t^{1}_{22} \end{bmatrix} \begin{bmatrix} t^{2}_{00} & t^{2}_{01} & 0 \\ t^{2}_{10} & t^{2}_{11} & t^{2}_{12} \\ 0 & t^{2}_{21} & t^{2}_{22} \end{bmatrix} \end{split}\]In strided format, the upper, lower, and diagonal arrays would look like:

\[\begin{split} \begin{align} \text{lower} &= \begin{bmatrix} 0 & t^{0}_{10} & t^{0}_{21} & 0 & t^{1}_{10} & t^{1}_{21} & 0 & t^{2}_{10} & t^{2}_{21} \end{bmatrix} \\ \text{diagonal} &= \begin{bmatrix} t^{0}_{00} & t^{0}_{11} & t^{0}_{22} & t^{1}_{00} & t^{1}_{11} & t^{1}_{22} & t^{2}_{00} & t^{2}_{11} & t^{2}_{22} \end{bmatrix} \\ \text{upper} &= \begin{bmatrix} t^{0}_{01} & t^{0}_{12} & 0 & t^{1}_{01} & t^{1}_{12} & 0 & t^{2}_{01} & t^{2}_{12} & 0 \end{bmatrix} \\ \end{align} \end{split}\]For the lower array, for each batch`i`

, the`i*batchStride`

entries are zero and for the upper array the`i*batchStride+batchStride-1`

entries are zero.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**m**–**[in]**size of the tri-diagonal linear system (must be >= 2).**dl**–**[in]**lower diagonal of tri-diagonal system. First entry must be zero.**d**–**[in]**main diagonal of tri-diagonal system.**du**–**[in]**upper diagonal of tri-diagonal system. Last entry must be zero.**x**–**[inout]**Dense array of righthand-sides where the ith righthand-side starts at`x+batchStride*i`

.**batchCount**–**[in]**The number of systems to solve.**batchStride**–**[in]**The number of elements that separate each system. Must satisfy`batchStride`

>= m.**pBuffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`batchCount`

,`batchStride`

,`dl`

,`d`

,`du`

,`x`

or`pBuffer`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.



## hipsparseXgtsvInterleavedBatch_bufferSizeExt()[#](#hipsparsexgtsvinterleavedbatch-buffersizeext)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSgtsvInterleavedBatch_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int algo, int m, const float *dl, const float *d, const float *du, const float *x, int batchCount, size_t *pBufferSizeInBytes)[#](#_CPPv444hipsparseSgtsvInterleavedBatch_bufferSizeExt17hipsparseHandle_tiiPKfPKfPKfPKfiP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDgtsvInterleavedBatch_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int algo, int m, const double *dl, const double *d, const double *du, const double *x, int batchCount, size_t *pBufferSizeInBytes)[#](#_CPPv444hipsparseDgtsvInterleavedBatch_bufferSizeExt17hipsparseHandle_tiiPKdPKdPKdPKdiP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCgtsvInterleavedBatch_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int algo, int m, const hipComplex *dl, const hipComplex *d, const hipComplex *du, const hipComplex *x, int batchCount, size_t *pBufferSizeInBytes)[#](#_CPPv444hipsparseCgtsvInterleavedBatch_bufferSizeExt17hipsparseHandle_tiiPK10hipComplexPK10hipComplexPK10hipComplexPK10hipComplexiP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZgtsvInterleavedBatch_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int algo, int m, const hipDoubleComplex *dl, const hipDoubleComplex *d, const hipDoubleComplex *du, const hipDoubleComplex *x, int batchCount, size_t *pBufferSizeInBytes)[#](#_CPPv444hipsparseZgtsvInterleavedBatch_bufferSizeExt17hipsparseHandle_tiiPK16hipDoubleComplexPK16hipDoubleComplexPK16hipDoubleComplexPK16hipDoubleComplexiP6size_t) `hipsparseXgtsvInterleavedBatch_bufferSizeExt`

returns the size of the temporary storage buffer in bytes that is required by[hipsparseXgtsvInterleavedBatch()](#hipsparse__gtsv__interleaved__batch_8h_1a762d0cd69377215f128a2a6d07024161). The temporary storage buffer must be allocated by the user.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**algo**–**[in]**Algorithm to use when solving tridiagonal systems. Options are thomas (`algo=0`

), LU (`algo=1`

), or QR (`algo=2`

). Thomas algorithm is the fastest but is not stable while LU and QR are slower but are stable.**m**–**[in]**size of the tri-diagonal linear system.**dl**–**[in]**lower diagonal of tri-diagonal system. The first element of the lower diagonal must be zero.**d**–**[in]**main diagonal of tri-diagonal system.**du**–**[in]**upper diagonal of tri-diagonal system. The last element of the upper diagonal must be zero.**x**–**[inout]**Dense array of righthand-sides with dimension`batchCount`

by`m`

.**batchCount**–**[in]**The number of systems to solve.**pBufferSizeInBytes**–**[out]**number of bytes of the temporary storage buffer required by[hipsparseSgtsvInterleavedBatch()](#hipsparse__gtsv__interleaved__batch_8h_1a762d0cd69377215f128a2a6d07024161).

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`batchCount`

,`dl`

,`d`

,`du`

,`x`

or`pBufferSizeInBytes`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.



## hipsparseXgtsvInterleavedBatch()[#](#hipsparsexgtsvinterleavedbatch)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSgtsvInterleavedBatch([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int algo, int m, float *dl, float *d, float *du, float *x, int batchCount, void *pBuffer)[#](#_CPPv430hipsparseSgtsvInterleavedBatch17hipsparseHandle_tiiPfPfPfPfiPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDgtsvInterleavedBatch([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int algo, int m, double *dl, double *d, double *du, double *x, int batchCount, void *pBuffer)[#](#_CPPv430hipsparseDgtsvInterleavedBatch17hipsparseHandle_tiiPdPdPdPdiPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCgtsvInterleavedBatch([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int algo, int m, hipComplex *dl, hipComplex *d, hipComplex *du, hipComplex *x, int batchCount, void *pBuffer)[#](#_CPPv430hipsparseCgtsvInterleavedBatch17hipsparseHandle_tiiP10hipComplexP10hipComplexP10hipComplexP10hipComplexiPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZgtsvInterleavedBatch([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int algo, int m, hipDoubleComplex *dl, hipDoubleComplex *d, hipDoubleComplex *du, hipDoubleComplex *x, int batchCount, void *pBuffer)[#](#_CPPv430hipsparseZgtsvInterleavedBatch17hipsparseHandle_tiiP16hipDoubleComplexP16hipDoubleComplexP16hipDoubleComplexP16hipDoubleComplexiPv) Interleaved Batch tridiagonal solver.

`hipsparseXgtsvInterleavedBatch`

solves a batched tridiagonal linear system\[ T^{i}*x^{i} = x^{i} \]where for each batch \(i=0\ldots\)`batchCount`

, \(T^{i}\) is a sparse tridiagonal matrix and \(x^{i}\) is a dense right-hand side vector. All of the tridiagonal matrices, \(T^{i}\), are packed in an interleaved fashion into three vectors:`dl`

for the lower diagonals,`d`

for the main diagonals and`du`

for the upper diagonals. See below for a description of what this interleaved memory pattern looks like.Solving the batched tridiagonal system involves two steps. First, the user calls

[hipsparseXgtsvInterleavedBatch_bufferSizeExt()](#hipsparse__gtsv__interleaved__batch_8h_1af7834969052003d50271c971371617cc)in order to determine the size of the required temporary storage buffer. Once determined, the user allocates this buffer and passes it to[hipsparseXgtsvInterleavedBatch()](#hipsparse__gtsv__interleaved__batch_8h_1a762d0cd69377215f128a2a6d07024161)to perform the actual solve. The \(x^{i}\) vectors, which initially stores the right-hand side values, are overwritten with the solution after the call to[hipsparseXgtsvInterleavedBatch()](#hipsparse__gtsv__interleaved__batch_8h_1a762d0cd69377215f128a2a6d07024161).The user can specify different algorithms for

`hipsparseXgtsvInterleavedBatch`

to use. Options are thomas (`algo=0`

), LU (`algo=1`

), or QR (`algo=2`

).Unlike the strided batch routines which write each batch matrix one after the other in memory, the interleaved routines write the batch matrices such that each element from each matrix is written consecutively one after the other. For example, consider the following batch matrices:

\[\begin{split} \begin{bmatrix} t^{0}_{00} & t^{0}_{01} & 0 \\ t^{0}_{10} & t^{0}_{11} & t^{0}_{12} \\ 0 & t^{0}_{21} & t^{0}_{22} \end{bmatrix} \begin{bmatrix} t^{1}_{00} & t^{1}_{01} & 0 \\ t^{1}_{10} & t^{1}_{11} & t^{1}_{12} \\ 0 & t^{1}_{21} & t^{1}_{22} \end{bmatrix} \begin{bmatrix} t^{2}_{00} & t^{2}_{01} & 0 \\ t^{2}_{10} & t^{2}_{11} & t^{2}_{12} \\ 0 & t^{2}_{21} & t^{2}_{22} \end{bmatrix} \end{split}\]In interleaved format, the upper, lower, and diagonal arrays would look like:

\[\begin{split} \begin{align} \text{lower} &= \begin{bmatrix} 0 & 0 & 0 & t^{0}_{10} & t^{1}_{10} & t^{1}_{10} & t^{0}_{21} & t^{1}_{21} & t^{2}_{21} \end{bmatrix} \\ \text{diagonal} &= \begin{bmatrix} t^{0}_{00} & t^{1}_{00} & t^{2}_{00} & t^{0}_{11} & t^{1}_{11} & t^{2}_{11} & t^{0}_{22} & t^{1}_{22} & t^{2}_{22} \end{bmatrix} \\ \text{upper} &= \begin{bmatrix} t^{0}_{01} & t^{1}_{01} & t^{2}_{01} & t^{0}_{12} & t^{1}_{12} & t^{2}_{12} & 0 & 0 & 0 \end{bmatrix} \\ \end{align} \end{split}\]For the lower array, the first`batchCount`

entries are zero and for the upper array the last`batchCount`

entries are zero.**Example**int main(int argc, char* argv[]) { // hipSPARSE handle hipsparseHandle_t handle; HIPSPARSE_CHECK(hipsparseCreate(&handle)); // Size of each square tridiagonal matrix int m = 6; // Number of batches int batchCount = 4; // Can be Thomas algorithm (0), LU (1), or QR (2) int algo = 1; // Host tridiagonal matrix std::vector<float> hdl(m * batchCount); std::vector<float> hd(m * batchCount); std::vector<float> hdu(m * batchCount); // Solve multiple tridiagonal matrix systems by interleaving matrices for better memory access: // // 4 2 0 0 0 0 5 3 0 0 0 0 6 4 0 0 0 0 7 5 0 0 0 0 // 2 4 2 0 0 0 3 5 3 0 0 0 4 6 4 0 0 0 5 7 5 0 0 0 // A1 = 0 2 4 2 0 0 A2 = 0 3 5 3 0 0 A3 = 0 4 6 4 0 0 A4 = 0 5 7 5 0 0 // 0 0 2 4 2 0 0 0 3 5 3 0 0 0 4 6 4 0 0 0 5 7 5 0 // 0 0 0 2 4 2 0 0 0 3 5 3 0 0 0 4 6 4 0 0 0 5 7 5 // 0 0 0 0 2 4 0 0 0 0 3 5 0 0 0 0 4 6 0 0 0 0 5 7 // // hdl = 0 0 0 0 2 3 4 5 2 3 4 5 2 3 4 5 2 3 4 5 2 3 4 5 // hd = 4 5 6 7 4 5 6 7 4 5 6 7 4 5 6 7 4 5 6 7 4 5 6 7 // hdu = 2 3 4 5 2 3 4 5 2 3 4 5 2 3 4 5 2 3 4 5 0 0 0 0 for(int b = 0; b < batchCount; ++b) { for(int i = 0; i < m; ++i) { hdl[batchCount * i + b] = 2 + b; hd[batchCount * i + b] = 4 + b; hdu[batchCount * i + b] = 2 + b; } hdl[batchCount * 0 + b] = 0.0f; hdu[batchCount * (m - 1) + b] = 0.0f; } // Host dense rhs std::vector<float> hx(m * batchCount); for(int b = 0; b < batchCount; ++b) { for(int i = 0; i < m; ++i) { hx[batchCount * i + b] = static_cast<float>(b + 1); } } float* ddl = nullptr; float* dd = nullptr; float* ddu = nullptr; float* dx = nullptr; HIP_CHECK(hipMalloc((void**)&ddl, sizeof(float) * m * batchCount)); HIP_CHECK(hipMalloc((void**)&dd, sizeof(float) * m * batchCount)); HIP_CHECK(hipMalloc((void**)&ddu, sizeof(float) * m * batchCount)); HIP_CHECK(hipMalloc((void**)&dx, sizeof(float) * m * batchCount)); HIP_CHECK(hipMemcpy(ddl, hdl.data(), sizeof(float) * m * batchCount, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dd, hd.data(), sizeof(float) * m * batchCount, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(ddu, hdu.data(), sizeof(float) * m * batchCount, hipMemcpyHostToDevice)); HIP_CHECK(hipMemcpy(dx, hx.data(), sizeof(float) * m * batchCount, hipMemcpyHostToDevice)); // 1. Get buffer size size_t bufferSize = 0; HIPSPARSE_CHECK(hipsparseSgtsvInterleavedBatch_bufferSizeExt( handle, algo, m, ddl, dd, ddu, dx, batchCount, &bufferSize)); void* dbuffer = nullptr; HIP_CHECK(hipMalloc((void**)&dbuffer, bufferSize)); // 2. Perform batched tridiagonal solve HIPSPARSE_CHECK( hipsparseSgtsvInterleavedBatch(handle, algo, m, ddl, dd, ddu, dx, batchCount, dbuffer)); // Copy solution back to host HIP_CHECK(hipMemcpy(hx.data(), dx, sizeof(float) * m * batchCount, hipMemcpyDeviceToHost)); // Print the solutions printf("Solutions for batched tridiagonal systems:\n"); for(int b = 0; b < batchCount; ++b) { printf(" Batch %d:\n", b); for(int i = 0; i < m; ++i) { printf(" x[%d] = %f\n", i, hx[i * batchCount + b]); } } // Clean up HIP_CHECK(hipFree(ddl)); HIP_CHECK(hipFree(dd)); HIP_CHECK(hipFree(ddu)); HIP_CHECK(hipFree(dx)); HIP_CHECK(hipFree(dbuffer)); HIPSPARSE_CHECK(hipsparseDestroy(handle)); return 0; }


Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**algo**–**[in]**Algorithm to use when solving tridiagonal systems. Options are thomas (`algo=0`

), LU (`algo=1`

), or QR (`algo=2`

). Thomas algorithm is the fastest but is not stable while LU and QR are slower but are stable.**m**–**[in]**size of the tri-diagonal linear system.**dl**–**[inout]**lower diagonal of tri-diagonal system. The first element of the lower diagonal must be zero.**d**–**[inout]**main diagonal of tri-diagonal system.**du**–**[inout]**upper diagonal of tri-diagonal system. The last element of the upper diagonal must be zero.**x**–**[inout]**Dense array of righthand-sides with dimension`batchCount`

by`m`

.**batchCount**–**[in]**The number of systems to solve.**pBuffer**–**[in]**temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`batchCount`

,`dl`

,`d`

,`du`

,`x`

or`pBuffer`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.



## hipsparseXgpsvInterleavedBatch_bufferSizeExt()[#](#hipsparsexgpsvinterleavedbatch-buffersizeext)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSgpsvInterleavedBatch_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int algo, int m, const float *ds, const float *dl, const float *d, const float *du, const float *dw, const float *x, int batchCount, size_t *pBufferSizeInBytes)[#](#_CPPv444hipsparseSgpsvInterleavedBatch_bufferSizeExt17hipsparseHandle_tiiPKfPKfPKfPKfPKfPKfiP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDgpsvInterleavedBatch_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int algo, int m, const double *ds, const double *dl, const double *d, const double *du, const double *dw, const double *x, int batchCount, size_t *pBufferSizeInBytes)[#](#_CPPv444hipsparseDgpsvInterleavedBatch_bufferSizeExt17hipsparseHandle_tiiPKdPKdPKdPKdPKdPKdiP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCgpsvInterleavedBatch_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int algo, int m, const hipComplex *ds, const hipComplex *dl, const hipComplex *d, const hipComplex *du, const hipComplex *dw, const hipComplex *x, int batchCount, size_t *pBufferSizeInBytes)[#](#_CPPv444hipsparseCgpsvInterleavedBatch_bufferSizeExt17hipsparseHandle_tiiPK10hipComplexPK10hipComplexPK10hipComplexPK10hipComplexPK10hipComplexPK10hipComplexiP6size_t)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZgpsvInterleavedBatch_bufferSizeExt([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int algo, int m, const hipDoubleComplex *ds, const hipDoubleComplex *dl, const hipDoubleComplex *d, const hipDoubleComplex *du, const hipDoubleComplex *dw, const hipDoubleComplex *x, int batchCount, size_t *pBufferSizeInBytes)[#](#_CPPv444hipsparseZgpsvInterleavedBatch_bufferSizeExt17hipsparseHandle_tiiPK16hipDoubleComplexPK16hipDoubleComplexPK16hipDoubleComplexPK16hipDoubleComplexPK16hipDoubleComplexPK16hipDoubleComplexiP6size_t) `hipsparseXgpsvInterleavedBatch_bufferSizeExt`

returns the size of the temporary storage buffer in bytes that is required by[hipsparseXgpsvInterleavedBatch()](#hipsparse__gpsv__interleaved__batch_8h_1a077fff1c509bbe46f1961c7f0c06c16b). The temporary storage buffer must be allocated by the user.- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**algo**–**[in]**algorithm to solve the linear system.**m**–**[in]**size of the pentadiagonal linear system.**ds**–**[in]**lower diagonal (distance 2) of pentadiagonal system. First two entries must be zero.**dl**–**[in]**lower diagonal of pentadiagonal system. First entry must be zero.**d**–**[in]**main diagonal of pentadiagonal system.**du**–**[in]**upper diagonal of pentadiagonal system. Last entry must be zero.**dw**–**[in]**upper diagonal (distance 2) of pentadiagonal system. Last two entries must be zero.**x**–**[in]**Dense array of right-hand-sides with dimension`batchCount`

by`m`

.**batchCount**–**[in]**The number of systems to solve.**pBufferSizeInBytes**–**[out]**Number of bytes of the temporary storage buffer required.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`alg`

,`batchCount`

,`ds`

,`dl`

,`d`

,`du`

,`dw`

,`x`

or`pBufferSizeInBytes`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.



## hipsparseXgpsvInterleavedBatch()[#](#hipsparsexgpsvinterleavedbatch)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseSgpsvInterleavedBatch([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int algo, int m, float *ds, float *dl, float *d, float *du, float *dw, float *x, int batchCount, void *pBuffer)[#](#_CPPv430hipsparseSgpsvInterleavedBatch17hipsparseHandle_tiiPfPfPfPfPfPfiPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseDgpsvInterleavedBatch([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int algo, int m, double *ds, double *dl, double *d, double *du, double *dw, double *x, int batchCount, void *pBuffer)[#](#_CPPv430hipsparseDgpsvInterleavedBatch17hipsparseHandle_tiiPdPdPdPdPdPdiPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseCgpsvInterleavedBatch([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int algo, int m, hipComplex *ds, hipComplex *dl, hipComplex *d, hipComplex *du, hipComplex *dw, hipComplex *x, int batchCount, void *pBuffer)[#](#_CPPv430hipsparseCgpsvInterleavedBatch17hipsparseHandle_tiiP10hipComplexP10hipComplexP10hipComplexP10hipComplexP10hipComplexP10hipComplexiPv)

-
[hipsparseStatus_t](types.html#_CPPv417hipsparseStatus_t)hipsparseZgpsvInterleavedBatch([hipsparseHandle_t](types.html#_CPPv417hipsparseHandle_t)handle, int algo, int m, hipDoubleComplex *ds, hipDoubleComplex *dl, hipDoubleComplex *d, hipDoubleComplex *du, hipDoubleComplex *dw, hipDoubleComplex *x, int batchCount, void *pBuffer)[#](#_CPPv430hipsparseZgpsvInterleavedBatch17hipsparseHandle_tiiP16hipDoubleComplexP16hipDoubleComplexP16hipDoubleComplexP16hipDoubleComplexP16hipDoubleComplexP16hipDoubleComplexiPv) Interleaved Batch pentadiagonal solver.

`hipsparseXgpsvInterleavedBatch`

solves a batch of pentadiagonal linear systems\[ P^{i}*x^{i} = x^{i} \]where for each batch \(i=0\ldots\)`batchCount`

, \(P^{i}\) is a sparse pentadiagonal matrix and \(x^{i}\) is a dense right-hand side vector. All of the pentadiagonal matrices, \(P^{i}\), are packed in an interleaved fashion into five vectors:`ds`

for the lowest diagonals,`dl`

for the lower diagonals,`d`

for the main diagonals,`du`

for the upper diagonals, and`dw`

for the highest digaonals. See below for a description of what this interleaved memory pattern looks like.Solving the batched pentadiagonal system involves two steps. First, the user calls

[hipsparseSgpsvInterleavedBatch_bufferSizeExt()](#hipsparse__gpsv__interleaved__batch_8h_1a451bdd94f381872f753d98c9e96b210e)in order to determine the size of the required temporary storage buffer. Once determined, the user allocates this buffer and passes it to[hipsparseXgpsvInterleavedBatch()](#hipsparse__gpsv__interleaved__batch_8h_1a077fff1c509bbe46f1961c7f0c06c16b)to perform the actual solve. The \(x^{i}\) vectors, which initially stores the right-hand side values, are overwritten with the solution after the call to[hipsparseXgpsvInterleavedBatch()](#hipsparse__gpsv__interleaved__batch_8h_1a077fff1c509bbe46f1961c7f0c06c16b).Unlike the strided batch routines which write each batch matrix one after the other in memory, the interleaved routines write the batch matrices such that each element from each matrix is written consecutively one after the other. For example, consider the following batch matrices:

\[\begin{split} \begin{bmatrix} t^{0}_{00} & t^{0}_{01} & t^{0}_{02} \\ t^{0}_{10} & t^{0}_{11} & t^{0}_{12} \\ t^{0}_{20} & t^{0}_{21} & t^{0}_{22} \end{bmatrix} \begin{bmatrix} t^{1}_{00} & t^{1}_{01} & t^{1}_{02} \\ t^{1}_{10} & t^{1}_{11} & t^{1}_{12} \\ t^{1}_{20} & t^{1}_{21} & t^{1}_{22} \end{bmatrix} \begin{bmatrix} t^{2}_{00} & t^{2}_{01} & t^{2}_{02} \\ t^{2}_{10} & t^{2}_{11} & t^{2}_{12} \\ t^{2}_{20} & t^{2}_{21} & t^{2}_{22} \end{bmatrix} \end{split}\]In interleaved format, the highest, higher, lowest, lower, and diagonal arrays would look like:

\[\begin{split} \begin{align} \text{lowest} &= \begin{bmatrix} 0 & 0 & 0 & 0 & 0 & 0 & t^{0}_{20} & t^{1}_{20} & t^{2}_{20} \end{bmatrix} \\ \text{lower} &= \begin{bmatrix} 0 & 0 & 0 & t^{0}_{10} & t^{1}_{10} & t^{1}_{10} & t^{0}_{21} & t^{1}_{21} & t^{2}_{21} \end{bmatrix} \\ \text{diagonal} &= \begin{bmatrix} t^{0}_{00} & t^{1}_{00} & t^{2}_{00} & t^{0}_{11} & t^{1}_{11} & t^{2}_{11} & t^{0}_{22} & t^{1}_{22} & t^{2}_{22} \end{bmatrix} \\ \text{higher} &= \begin{bmatrix} t^{0}_{01} & t^{1}_{01} & t^{2}_{01} & t^{0}_{12} & t^{1}_{12} & t^{2}_{12} & 0 & 0 & 0 \end{bmatrix} \\ \text{highest} &= \begin{bmatrix} t^{0}_{02} & t^{1}_{02} & t^{2}_{02} & 0 & 0 & 0 & 0 & 0 & 0 \end{bmatrix} \\ \end{align} \end{split}\]For the lowest array, the first`2*batchCount`

entries are zero, for the lower array, the first`batchCount`

entries are zero, for the upper array the last`batchCount`

entries are zero, and for the highest array, the last`2*batchCount`

entries are zero.Note

This function is non blocking and executed asynchronously with respect to the host. It may return before the actual computation has finished.

- Parameters:
**handle**–**[in]**handle to the hipsparse library context queue.**algo**–**[in]**algorithm to solve the linear system.**m**–**[in]**size of the pentadiagonal linear system.**ds**–**[inout]**lower diagonal (distance 2) of pentadiagonal system. First two entries must be zero.**dl**–**[inout]**lower diagonal of pentadiagonal system. First entry must be zero.**d**–**[inout]**main diagonal of pentadiagonal system.**du**–**[inout]**upper diagonal of pentadiagonal system. Last entry must be zero.**dw**–**[inout]**upper diagonal (distance 2) of pentadiagonal system. Last two entries must be zero.**x**–**[inout]**Dense array of right-hand-sides with dimension`batchCount`

by`m`

.**batchCount**–**[in]**The number of systems to solve.**pBuffer**–**[in]**Temporary storage buffer allocated by the user.

- Return values:
**HIPSPARSE_STATUS_SUCCESS**– the operation completed successfully.**HIPSPARSE_STATUS_INVALID_VALUE**–`handle`

,`m`

,`alg`

,`batchCount`

,`ds`

,`dl`

,`d`

,`du`

,`dw`

,`x`

or`pBuffer`

pointer is invalid.**HIPSPARSE_STATUS_INTERNAL_ERROR**– an internal error occurred.
