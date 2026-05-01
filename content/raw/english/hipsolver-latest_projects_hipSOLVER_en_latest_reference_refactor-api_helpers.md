---
title: "Refactorization helper functions &#8212; hipSOLVER 3.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/refactor-api/helpers.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:20:59.180946+00:00
content_hash: "7c3a24386a9c688f"
---

# Refactorization helper functions[#](#refactorization-helper-functions)

These helper functions control aspects of the hipSOLVER library. They are divided into the following categories:

[Handle setup and teardown](#refactor-initialize): Functions to initialize and cleanup the library handle.[Input manipulation](#refactor-input): Functions to manipulate function input.[Output manipulation](#refactor-output): Functions to access function output.[Parameter manipulation](#refactor-parameters): Functions to manipulate parameters.

## Handle setup and teardown[#](#handle-setup-and-teardown)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverRfCreate([hipsolverRfHandle_t](types.html#_CPPv419hipsolverRfHandle_t)*handle)[#](#_CPPv417hipsolverRfCreateP19hipsolverRfHandle_t)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverRfDestroy([hipsolverRfHandle_t](types.html#_CPPv419hipsolverRfHandle_t)handle)[#](#_CPPv418hipsolverRfDestroy19hipsolverRfHandle_t)

## Input manipulation[#](#input-manipulation)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverRfSetupDevice(int n, int nnzA, int *csrRowPtrA, int *csrColIndA, double *csrValA, int nnzL, int *csrRowPtrL, int *csrColIndL, double *csrValL, int nnzU, int *csrRowPtrU, int *csrColIndU, double *csrValU, int *P, int *Q,[hipsolverRfHandle_t](types.html#_CPPv419hipsolverRfHandle_t)handle)[#](#_CPPv422hipsolverRfSetupDeviceiiPiPiPdiPiPiPdiPiPiPdPiPi19hipsolverRfHandle_t)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverRfSetupHost(int n, int nnzA, int *h_csrRowPtrA, int *h_csrColIndA, double *h_csrValA, int nnzL, int *h_csrRowPtrL, int *h_csrColIndL, double *h_csrValL, int nnzU, int *h_csrRowPtrU, int *h_csrColIndU, double *h_csrValU, int *h_P, int *h_Q,[hipsolverRfHandle_t](types.html#_CPPv419hipsolverRfHandle_t)handle)[#](#_CPPv420hipsolverRfSetupHostiiPiPiPdiPiPiPdiPiPiPdPiPi19hipsolverRfHandle_t)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverRfBatchSetupHost(int batchSize, int n, int nnzA, int *h_csrRowPtrA, int *h_csrColIndA, double *h_csrValA_array[], int nnzL, int *h_csrRowPtrL, int *h_csrColIndL, double *h_csrValL, int nnzU, int *h_csrRowPtrU, int *h_csrColIndU, double *h_csrValU, int *h_P, int *h_Q,[hipsolverRfHandle_t](types.html#_CPPv419hipsolverRfHandle_t)handle)[#](#_CPPv425hipsolverRfBatchSetupHostiiiPiPiA_PdiPiPiPdiPiPiPdPiPi19hipsolverRfHandle_t)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverRfAnalyze([hipsolverRfHandle_t](types.html#_CPPv419hipsolverRfHandle_t)handle)[#](#_CPPv418hipsolverRfAnalyze19hipsolverRfHandle_t)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverRfBatchAnalyze([hipsolverRfHandle_t](types.html#_CPPv419hipsolverRfHandle_t)handle)[#](#_CPPv423hipsolverRfBatchAnalyze19hipsolverRfHandle_t)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverRfResetValues(int n, int nnzA, int *csrRowPtrA, int *csrColIndA, double *csrValA, int *P, int *Q,[hipsolverRfHandle_t](types.html#_CPPv419hipsolverRfHandle_t)handle)[#](#_CPPv422hipsolverRfResetValuesiiPiPiPdPiPi19hipsolverRfHandle_t)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverRfBatchResetValues(int batchSize, int n, int nnzA, int *csrRowPtrA, int *csrColIndA, double *csrValA_array[], int *P, int *Q,[hipsolverRfHandle_t](types.html#_CPPv419hipsolverRfHandle_t)handle)[#](#_CPPv427hipsolverRfBatchResetValuesiiiPiPiA_PdPiPi19hipsolverRfHandle_t)

## Output manipulation[#](#output-manipulation)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverRfAccessBundledFactorsDevice([hipsolverRfHandle_t](types.html#_CPPv419hipsolverRfHandle_t)handle, int *nnzM, int **Mp, int **Mi, double **Mx)[#](#_CPPv437hipsolverRfAccessBundledFactorsDevice19hipsolverRfHandle_tPiPPiPPiPPd)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverRfExtractBundledFactorsHost([hipsolverRfHandle_t](types.html#_CPPv419hipsolverRfHandle_t)handle, int *h_nnzM, int **h_Mp, int **h_Mi, double **h_Mx)[#](#_CPPv436hipsolverRfExtractBundledFactorsHost19hipsolverRfHandle_tPiPPiPPiPPd)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverRfExtractSplitFactorsHost([hipsolverRfHandle_t](types.html#_CPPv419hipsolverRfHandle_t)handle, int *h_nnzL, int **h_Lp, int **h_Li, double **h_Lx, int *h_nnzU, int **h_Up, int **h_Ui, double **h_Ux)[#](#_CPPv434hipsolverRfExtractSplitFactorsHost19hipsolverRfHandle_tPiPPiPPiPPdPiPPiPPiPPd)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverRfBatchZeroPivot([hipsolverRfHandle_t](types.html#_CPPv419hipsolverRfHandle_t)handle, int *position)[#](#_CPPv425hipsolverRfBatchZeroPivot19hipsolverRfHandle_tPi)

## Parameter manipulation[#](#parameter-manipulation)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverRfGet_Algs([hipsolverRfHandle_t](types.html#_CPPv419hipsolverRfHandle_t)handle,[hipsolverRfFactorization_t](types.html#_CPPv426hipsolverRfFactorization_t)*fact_alg,[hipsolverRfTriangularSolve_t](types.html#_CPPv428hipsolverRfTriangularSolve_t)*solve_alg)[#](#_CPPv419hipsolverRfGet_Algs19hipsolverRfHandle_tP26hipsolverRfFactorization_tP28hipsolverRfTriangularSolve_t)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverRfGetMatrixFormat([hipsolverRfHandle_t](types.html#_CPPv419hipsolverRfHandle_t)handle,[hipsolverRfMatrixFormat_t](types.html#_CPPv425hipsolverRfMatrixFormat_t)*format,[hipsolverRfUnitDiagonal_t](types.html#_CPPv425hipsolverRfUnitDiagonal_t)*diag)[#](#_CPPv426hipsolverRfGetMatrixFormat19hipsolverRfHandle_tP25hipsolverRfMatrixFormat_tP25hipsolverRfUnitDiagonal_t)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverRfGetNumericBoostReport([hipsolverRfHandle_t](types.html#_CPPv419hipsolverRfHandle_t)handle,[hipsolverRfNumericBoostReport_t](types.html#_CPPv431hipsolverRfNumericBoostReport_t)*report)[#](#_CPPv432hipsolverRfGetNumericBoostReport19hipsolverRfHandle_tP31hipsolverRfNumericBoostReport_t)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverRfGetNumericProperties([hipsolverRfHandle_t](types.html#_CPPv419hipsolverRfHandle_t)handle, double *zero, double *boost)[#](#_CPPv431hipsolverRfGetNumericProperties19hipsolverRfHandle_tPdPd)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverRfGetResetValuesFastMode([hipsolverRfHandle_t](types.html#_CPPv419hipsolverRfHandle_t)handle,[hipsolverRfResetValuesFastMode_t](types.html#_CPPv432hipsolverRfResetValuesFastMode_t)*fastMode)[#](#_CPPv433hipsolverRfGetResetValuesFastMode19hipsolverRfHandle_tP32hipsolverRfResetValuesFastMode_t)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverRfSetAlgs([hipsolverRfHandle_t](types.html#_CPPv419hipsolverRfHandle_t)handle,[hipsolverRfFactorization_t](types.html#_CPPv426hipsolverRfFactorization_t)fact_alg,[hipsolverRfTriangularSolve_t](types.html#_CPPv428hipsolverRfTriangularSolve_t)solve_alg)[#](#_CPPv418hipsolverRfSetAlgs19hipsolverRfHandle_t26hipsolverRfFactorization_t28hipsolverRfTriangularSolve_t)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverRfSetMatrixFormat([hipsolverRfHandle_t](types.html#_CPPv419hipsolverRfHandle_t)handle,[hipsolverRfMatrixFormat_t](types.html#_CPPv425hipsolverRfMatrixFormat_t)format,[hipsolverRfUnitDiagonal_t](types.html#_CPPv425hipsolverRfUnitDiagonal_t)diag)[#](#_CPPv426hipsolverRfSetMatrixFormat19hipsolverRfHandle_t25hipsolverRfMatrixFormat_t25hipsolverRfUnitDiagonal_t)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverRfSetNumericProperties([hipsolverRfHandle_t](types.html#_CPPv419hipsolverRfHandle_t)handle, double effective_zero, double boost_val)[#](#_CPPv431hipsolverRfSetNumericProperties19hipsolverRfHandle_tdd)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverRfSetResetValuesFastMode([hipsolverRfHandle_t](types.html#_CPPv419hipsolverRfHandle_t)handle,[hipsolverRfResetValuesFastMode_t](types.html#_CPPv432hipsolverRfResetValuesFastMode_t)fastMode)[#](#_CPPv433hipsolverRfSetResetValuesFastMode19hipsolverRfHandle_t32hipsolverRfResetValuesFastMode_t)
