---
title: "Refactorization functions &#8212; hipSOLVER 3.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/refactor-api/refactor.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:20:54.685231+00:00
content_hash: "a92b52ef95c9132b"
---

# Refactorization functions[#](#refactorization-functions)

Refactoring routines are used to solve complex numerical linear algebra problems for sparse matrices. These functions are organized into the following categories:

## Triangular factorizations[#](#triangular-factorizations)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverRfRefactor([hipsolverRfHandle_t](types.html#_CPPv419hipsolverRfHandle_t)handle)[#](#_CPPv419hipsolverRfRefactor19hipsolverRfHandle_t)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverRfBatchRefactor([hipsolverRfHandle_t](types.html#_CPPv419hipsolverRfHandle_t)handle)[#](#_CPPv424hipsolverRfBatchRefactor19hipsolverRfHandle_t)

## Linear-systems solvers[#](#linear-systems-solvers)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverRfSolve([hipsolverRfHandle_t](types.html#_CPPv419hipsolverRfHandle_t)handle, int *P, int *Q, int nrhs, double *Temp, int ldt, double *XF, int ldxf)[#](#_CPPv416hipsolverRfSolve19hipsolverRfHandle_tPiPiiPdiPdi)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverRfBatchSolve([hipsolverRfHandle_t](types.html#_CPPv419hipsolverRfHandle_t)handle, int *P, int *Q, int nrhs, double *Temp, int ldt, double *XF_array[], int ldxf)[#](#_CPPv421hipsolverRfBatchSolve19hipsolverRfHandle_tPiPiiPdiA_Pdi)
