---
title: "Refactorization data types &#8212; hipSOLVER 3.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/refactor-api/types.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:20:38.140429+00:00
content_hash: "464043ed7013a646"
---

Refactorization data types
hipSOLVER defines types and enumerations that are internally converted to the corresponding backend
types at runtime. Here is a list of the types used in this compatibility API.

hipSOLVER compatibility API types
List of types in the compatibility API

typedef void * hipsolverRfHandle_t
enum hipsolverRfFactorization_t
Values:

enumerator HIPSOLVERRF_FACTORIZATION_ALG0
enumerator HIPSOLVERRF_FACTORIZATION_ALG1
enumerator HIPSOLVERRF_FACTORIZATION_ALG2
enum hipsolverRfNumericBoostReport_t
Values:

enumerator HIPSOLVERRF_NUMERIC_BOOST_NOT_USED
enumerator HIPSOLVERRF_NUMERIC_BOOST_USED
enum hipsolverRfResetValuesFastMode_t
Values:

enumerator HIPSOLVERRF_RESET_VALUES_FAST_MODE_OFF
enumerator HIPSOLVERRF_RESET_VALUES_FAST_MODE_ON
enum hipsolverRfTriangularSolve_t
Values:

enumerator HIPSOLVERRF_TRIANGULAR_SOLVE_ALG1
enumerator HIPSOLVERRF_TRIANGULAR_SOLVE_ALG2
enumerator HIPSOLVERRF_TRIANGULAR_SOLVE_ALG3
enum hipsolverRfUnitDiagonal_t
Values:

enumerator HIPSOLVERRF_UNIT_DIAGONAL_STORED_L
enumerator HIPSOLVERRF_UNIT_DIAGONAL_STORED_U
enumerator HIPSOLVERRF_UNIT_DIAGONAL_ASSUMED_L
enumerator HIPSOLVERRF_UNIT_DIAGONAL_ASSUMED_U
