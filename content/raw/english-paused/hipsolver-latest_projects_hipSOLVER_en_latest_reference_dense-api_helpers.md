---
title: "Dense matrix helper functions &#8212; hipSOLVER 3.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/dense-api/helpers.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:21:11.399149+00:00
content_hash: "14017d9a494a9e82"
---

# Dense matrix helper functions[#](#dense-matrix-helper-functions)

These are helper functions that control aspects of the hipSOLVER library. They are divided into the following categories:

[Handle setup and teardown](#dense-initialize): Functions to initialize and clean up the library handle.[Stream manipulation](#dense-stream): Functions to manipulate streams.[Determinism manipulation](#dense-determinism): Functions to manipulate function determinism.[Gesvdj parameter manipulation](#dense-gesvdj-info): Functions to manipulate gesvdj parameters.[Syevj parameter manipulation](#dense-syevj-info): Functions to manipulate syevj parameters.[Other parameter manipulation](#dense-params): Functions to manipulate other parameters.

## Handle setup and teardown[#](#handle-setup-and-teardown)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnCreate([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)*handle)[#](#_CPPv417hipsolverDnCreateP17hipsolverHandle_t) An alias for

[hipsolverCreate](../api/helpers.html#hipsolver-functions_8h_1a35be175b9fa35868e1f637d786b20a08).

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDestroy([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle)[#](#_CPPv418hipsolverDnDestroy17hipsolverHandle_t) An alias for

[hipsolverDestroy](../api/helpers.html#hipsolver-functions_8h_1aab4f3b31271f1938fbf9eb422e650ca9).

## Stream manipulation[#](#stream-manipulation)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSetStream([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, hipStream_t streamId)[#](#_CPPv420hipsolverDnSetStream17hipsolverHandle_t11hipStream_t) An alias for

[hipsolverSetStream](../api/helpers.html#hipsolver-functions_8h_1a467d2991671b6fad494930c3f1ad3a0e).

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnGetStream([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle, hipStream_t *streamId)[#](#_CPPv420hipsolverDnGetStream17hipsolverHandle_tP11hipStream_t) An alias for

[hipsolverGetStream](../api/helpers.html#hipsolver-functions_8h_1a9cb1153c2069ac626e8cd9b33870a7e6).

## Determinism manipulation[#](#determinism-manipulation)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSetDeterministicMode([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverDeterministicMode_t](../api/types.html#_CPPv428hipsolverDeterministicMode_t)mode)[#](#_CPPv431hipsolverDnSetDeterministicMode17hipsolverHandle_t28hipsolverDeterministicMode_t) An alias for

[hipsolverSetDeterministicMode](../api/helpers.html#hipsolver-functions_8h_1a6f4b627b36bcbc1a71497ad8510726d0).

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnGetDeterministicMode([hipsolverHandle_t](../api/types.html#_CPPv417hipsolverHandle_t)handle,[hipsolverDeterministicMode_t](../api/types.html#_CPPv428hipsolverDeterministicMode_t)*mode)[#](#_CPPv431hipsolverDnGetDeterministicMode17hipsolverHandle_tP28hipsolverDeterministicMode_t) An alias for

[hipsolverGetDeterministicMode](../api/helpers.html#hipsolver-functions_8h_1ae8bd6ef6ac3562d351eeabfba6c89dad).

## Gesvdj parameter manipulation[#](#gesvdj-parameter-manipulation)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnCreateGesvdjInfo([hipsolverGesvdjInfo_t](../api/types.html#_CPPv421hipsolverGesvdjInfo_t)*info)[#](#_CPPv427hipsolverDnCreateGesvdjInfoP21hipsolverGesvdjInfo_t)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDestroyGesvdjInfo([hipsolverGesvdjInfo_t](../api/types.html#_CPPv421hipsolverGesvdjInfo_t)info)[#](#_CPPv428hipsolverDnDestroyGesvdjInfo21hipsolverGesvdjInfo_t)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnXgesvdjSetMaxSweeps([hipsolverGesvdjInfo_t](../api/types.html#_CPPv421hipsolverGesvdjInfo_t)info, int max_sweeps)[#](#_CPPv430hipsolverDnXgesvdjSetMaxSweeps21hipsolverGesvdjInfo_ti)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnXgesvdjSetSortEig([hipsolverGesvdjInfo_t](../api/types.html#_CPPv421hipsolverGesvdjInfo_t)info, int sort_eig)[#](#_CPPv428hipsolverDnXgesvdjSetSortEig21hipsolverGesvdjInfo_ti)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnXgesvdjSetTolerance([hipsolverGesvdjInfo_t](../api/types.html#_CPPv421hipsolverGesvdjInfo_t)info, double tolerance)[#](#_CPPv430hipsolverDnXgesvdjSetTolerance21hipsolverGesvdjInfo_td)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnXgesvdjGetResidual([hipsolverDnHandle_t](types.html#_CPPv419hipsolverDnHandle_t)handle,[hipsolverGesvdjInfo_t](../api/types.html#_CPPv421hipsolverGesvdjInfo_t)info, double *residual)[#](#_CPPv429hipsolverDnXgesvdjGetResidual19hipsolverDnHandle_t21hipsolverGesvdjInfo_tPd)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnXgesvdjGetSweeps([hipsolverDnHandle_t](types.html#_CPPv419hipsolverDnHandle_t)handle,[hipsolverGesvdjInfo_t](../api/types.html#_CPPv421hipsolverGesvdjInfo_t)info, int *executed_sweeps)[#](#_CPPv427hipsolverDnXgesvdjGetSweeps19hipsolverDnHandle_t21hipsolverGesvdjInfo_tPi)

## Syevj parameter manipulation[#](#syevj-parameter-manipulation)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnCreateSyevjInfo([hipsolverSyevjInfo_t](../api/types.html#_CPPv420hipsolverSyevjInfo_t)*info)[#](#_CPPv426hipsolverDnCreateSyevjInfoP20hipsolverSyevjInfo_t)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDestroySyevjInfo([hipsolverSyevjInfo_t](../api/types.html#_CPPv420hipsolverSyevjInfo_t)info)[#](#_CPPv427hipsolverDnDestroySyevjInfo20hipsolverSyevjInfo_t)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnXsyevjSetMaxSweeps([hipsolverSyevjInfo_t](../api/types.html#_CPPv420hipsolverSyevjInfo_t)info, int max_sweeps)[#](#_CPPv429hipsolverDnXsyevjSetMaxSweeps20hipsolverSyevjInfo_ti)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnXsyevjSetSortEig([hipsolverSyevjInfo_t](../api/types.html#_CPPv420hipsolverSyevjInfo_t)info, int sort_eig)[#](#_CPPv427hipsolverDnXsyevjSetSortEig20hipsolverSyevjInfo_ti)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnXsyevjSetTolerance([hipsolverSyevjInfo_t](../api/types.html#_CPPv420hipsolverSyevjInfo_t)info, double tolerance)[#](#_CPPv429hipsolverDnXsyevjSetTolerance20hipsolverSyevjInfo_td)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnXsyevjGetResidual([hipsolverDnHandle_t](types.html#_CPPv419hipsolverDnHandle_t)handle,[hipsolverSyevjInfo_t](../api/types.html#_CPPv420hipsolverSyevjInfo_t)info, double *residual)[#](#_CPPv428hipsolverDnXsyevjGetResidual19hipsolverDnHandle_t20hipsolverSyevjInfo_tPd)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnXsyevjGetSweeps([hipsolverDnHandle_t](types.html#_CPPv419hipsolverDnHandle_t)handle,[hipsolverSyevjInfo_t](../api/types.html#_CPPv420hipsolverSyevjInfo_t)info, int *executed_sweeps)[#](#_CPPv426hipsolverDnXsyevjGetSweeps19hipsolverDnHandle_t20hipsolverSyevjInfo_tPi)

## Other parameter manipulation[#](#other-parameter-manipulation)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnCreateParams(hipsolverDnParams_t *params)[#](#_CPPv423hipsolverDnCreateParamsP19hipsolverDnParams_t)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnDestroyParams(hipsolverDnParams_t params)[#](#_CPPv424hipsolverDnDestroyParams19hipsolverDnParams_t)

-
[hipsolverStatus_t](../api/types.html#_CPPv417hipsolverStatus_t)hipsolverDnSetAdvOptions(hipsolverDnParams_t params,[hipsolverDnFunction_t](types.html#_CPPv421hipsolverDnFunction_t)func,[hipsolverAlgMode_t](types.html#_CPPv418hipsolverAlgMode_t)alg)[#](#_CPPv424hipsolverDnSetAdvOptions19hipsolverDnParams_t21hipsolverDnFunction_t18hipsolverAlgMode_t)
