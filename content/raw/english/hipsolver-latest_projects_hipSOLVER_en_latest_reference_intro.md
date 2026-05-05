---
title: "Introduction to the hipSOLVER API &#8212; hipSOLVER 3.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/intro.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:21:13.466536+00:00
content_hash: "e853a16583621e3a"
---

# Introduction to the hipSOLVER API[#](#introduction-to-the-hipsolver-api)

The following tables summarize the wrapper functions that are implemented in the regular API for the different supported precisions in the hipSOLVER release. Most of these functions have a corresponding version in the compatibility APIs, where applicable.

Note

The hipSOLVER library is in active development, with new features are being continuously added.

## LAPACK auxiliary functions[#](#lapack-auxiliary-functions)

## LAPACK main functions[#](#lapack-main-functions)

Function |
single |
double |
single complex |
double complex |
|---|---|---|---|---|
x |
x |
x |
x |
|
x |
x |
x |
x |
|
x |
x |
x |
x |
|
x |
x |
x |
x |
|
x |
x |
x |
x |
|
x |
x |
x |
x |
|
x |
x |
x |
x |
|
x |
x |
x |
x |

Function |
single |
double |
single complex |
double complex |
|---|---|---|---|---|
x |
x |
x |
x |
|
x |
x |
x |
x |
|
x |
x |
x |
x |
|
x |
x |
x |
x |
|
x |
x |
x |
x |
|
x |
x |
x |
x |
|
x |
x |
x |
x |
|
x |
x |
x |
x |
|
x |
x |
x |
x |
|
x |
x |
x |
x |

## LAPACK-like functions[#](#lapack-like-functions)

Function |
single |
double |
single complex |
double complex |
|---|---|---|---|---|
x |
x |
|||
x |
x |
|||
x |
x |
|||
x |
x |
|||
x |
x |
|||
x |
x |
|||
x |
x |
|||
x |
x |
|||
x |
x |
|||
x |
x |
|||
x |
x |
|||
x |
x |
|||
x |
x |
|||
x |
x |
|||
x |
x |
|||
x |
x |
|||
x |
x |
|||
x |
x |
|||
x |
x |
|||
x |
x |

### Compatibility-only functions[#](#compatibility-only-functions)

The following tables summarize the wrapper functions that are provided only in the compatibility APIs. These wrappers are supported in rocSOLVER, but are provided by equivalent functions that use different algorithmic approaches or by functionality that is not fully exposed in the public API. For these reasons, the corresponding wrappers are not provided in the regular hipSOLVER API.

## Partial SVD functions[#](#partial-svd-functions)

Partial SVD has been implemented in rocSOLVER, but it does not use an approximate algorithm and does not compute the residual norm.

## Sparse matrix routines[#](#sparse-matrix-routines)

Sparse matrix routines and direct solvers for sparse matrices are in the very early stages of development.
Due to unsupported backend functionality, there are several intricacies and possible performance implications
to be aware of when using these routines.
See the [hipsolverSp compatibility API](sparse-api/index.html#library-sparse) for more details and a full listing of supported functions.

## Refactorization routines[#](#refactorization-routines)

Refactorization routines and direct solvers for sparse matrices are in the very early stages of development.
Due to unsupported backend functionality, there are several intricacies and possible performance implications
to be aware of when using these routines.
See the [hipsolverRf compatibility API](refactor-api/index.html#library-refactor) for more details and a full listing of supported functions.
