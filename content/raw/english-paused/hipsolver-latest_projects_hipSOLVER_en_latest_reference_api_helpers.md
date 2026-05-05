---
title: "hipSOLVER helper functions &#8212; hipSOLVER 3.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/helpers.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:08:40.328177+00:00
content_hash: "953da9d4f157a862"
---

# hipSOLVER helper functions[#](#hipsolver-helper-functions)

These are helper functions that control aspects of the hipSOLVER library. They are divided into the following categories:

[Handle setup and teardown](#initialize): Functions to initialize and cleanup the library handle.[Stream manipulation](#stream): Functions to manipulate streams.[Determinism manipulation](#determinism): Functions to manipulate function determinism.[Gesvdj parameter manipulation](#gesvdj-info): Functions to manipulate gesvdj parameters.[Syevj parameter manipulation](#syevj-info): Functions to manipulate syevj parameters.

## Handle setup and teardown[#](#handle-setup-and-teardown)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCreate([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)*handle)[#](#_CPPv415hipsolverCreateP17hipsolverHandle_t)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDestroy([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle)[#](#_CPPv416hipsolverDestroy17hipsolverHandle_t)

## Stream manipulation[#](#stream-manipulation)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSetStream([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, hipStream_t streamId)[#](#_CPPv418hipsolverSetStream17hipsolverHandle_t11hipStream_t)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverGetStream([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle, hipStream_t *streamId)[#](#_CPPv418hipsolverGetStream17hipsolverHandle_tP11hipStream_t)

## Determinism manipulation[#](#determinism-manipulation)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverSetDeterministicMode([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverDeterministicMode_t](types.html#_CPPv428hipsolverDeterministicMode_t)mode)[#](#_CPPv429hipsolverSetDeterministicMode17hipsolverHandle_t28hipsolverDeterministicMode_t)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverGetDeterministicMode([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverDeterministicMode_t](types.html#_CPPv428hipsolverDeterministicMode_t)*mode)[#](#_CPPv429hipsolverGetDeterministicMode17hipsolverHandle_tP28hipsolverDeterministicMode_t)

## Gesvdj parameter manipulation[#](#gesvdj-parameter-manipulation)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCreateGesvdjInfo([hipsolverGesvdjInfo_t](types.html#_CPPv421hipsolverGesvdjInfo_t)*info)[#](#_CPPv425hipsolverCreateGesvdjInfoP21hipsolverGesvdjInfo_t)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDestroyGesvdjInfo([hipsolverGesvdjInfo_t](types.html#_CPPv421hipsolverGesvdjInfo_t)info)[#](#_CPPv426hipsolverDestroyGesvdjInfo21hipsolverGesvdjInfo_t)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverXgesvdjSetMaxSweeps([hipsolverGesvdjInfo_t](types.html#_CPPv421hipsolverGesvdjInfo_t)info, int max_sweeps)[#](#_CPPv428hipsolverXgesvdjSetMaxSweeps21hipsolverGesvdjInfo_ti)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverXgesvdjSetSortEig([hipsolverGesvdjInfo_t](types.html#_CPPv421hipsolverGesvdjInfo_t)info, int sort_eig)[#](#_CPPv426hipsolverXgesvdjSetSortEig21hipsolverGesvdjInfo_ti)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverXgesvdjSetTolerance([hipsolverGesvdjInfo_t](types.html#_CPPv421hipsolverGesvdjInfo_t)info, double tolerance)[#](#_CPPv428hipsolverXgesvdjSetTolerance21hipsolverGesvdjInfo_td)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverXgesvdjGetResidual([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverGesvdjInfo_t](types.html#_CPPv421hipsolverGesvdjInfo_t)info, double *residual)[#](#_CPPv427hipsolverXgesvdjGetResidual17hipsolverHandle_t21hipsolverGesvdjInfo_tPd)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverXgesvdjGetSweeps([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverGesvdjInfo_t](types.html#_CPPv421hipsolverGesvdjInfo_t)info, int *executed_sweeps)[#](#_CPPv425hipsolverXgesvdjGetSweeps17hipsolverHandle_t21hipsolverGesvdjInfo_tPi)

## Syevj parameter manipulation[#](#syevj-parameter-manipulation)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverCreateSyevjInfo([hipsolverSyevjInfo_t](types.html#_CPPv420hipsolverSyevjInfo_t)*info)[#](#_CPPv424hipsolverCreateSyevjInfoP20hipsolverSyevjInfo_t)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverDestroySyevjInfo([hipsolverSyevjInfo_t](types.html#_CPPv420hipsolverSyevjInfo_t)info)[#](#_CPPv425hipsolverDestroySyevjInfo20hipsolverSyevjInfo_t)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverXsyevjSetMaxSweeps([hipsolverSyevjInfo_t](types.html#_CPPv420hipsolverSyevjInfo_t)info, int max_sweeps)[#](#_CPPv427hipsolverXsyevjSetMaxSweeps20hipsolverSyevjInfo_ti)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverXsyevjSetSortEig([hipsolverSyevjInfo_t](types.html#_CPPv420hipsolverSyevjInfo_t)info, int sort_eig)[#](#_CPPv425hipsolverXsyevjSetSortEig20hipsolverSyevjInfo_ti)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverXsyevjSetTolerance([hipsolverSyevjInfo_t](types.html#_CPPv420hipsolverSyevjInfo_t)info, double tolerance)[#](#_CPPv427hipsolverXsyevjSetTolerance20hipsolverSyevjInfo_td)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverXsyevjGetResidual([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverSyevjInfo_t](types.html#_CPPv420hipsolverSyevjInfo_t)info, double *residual)[#](#_CPPv426hipsolverXsyevjGetResidual17hipsolverHandle_t20hipsolverSyevjInfo_tPd)

-
[hipsolverStatus_t](types.html#_CPPv417hipsolverStatus_t)hipsolverXsyevjGetSweeps([hipsolverHandle_t](types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverSyevjInfo_t](types.html#_CPPv420hipsolverSyevjInfo_t)info, int *executed_sweeps)[#](#_CPPv424hipsolverXsyevjGetSweeps17hipsolverHandle_t20hipsolverSyevjInfo_tPi)
