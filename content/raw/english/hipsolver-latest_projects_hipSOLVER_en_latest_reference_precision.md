---
title: "hipSOLVER precision support &#8212; hipSOLVER 3.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/precision.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:20:52.762512+00:00
content_hash: "d06436437190b164"
---

# hipSOLVER precision support[#](#hipsolver-precision-support)

This section provides an overview of the numerical precision types supported by the hipSOLVER library. hipSOLVER provides a consistent interface to linear algebra solvers that can run on AMD hardware.

## Supported precision types[#](#supported-precision-types)

hipSOLVER supports four primary precision types across its functions:

Type prefix |
C++ type |
Description |
|---|---|---|
|
|
Single-precision real (32-bit) |
|
|
Double-precision real (64-bit) |
|
|
Single-precision complex (32-bit real, 32-bit imaginary) |
|
|
Double-precision complex (64-bit real, 64-bit imaginary) |

### Function naming convention[#](#function-naming-convention)

hipSOLVER follows the LAPACK naming convention where the first letter of the function name indicates the precision type:

Functions beginning with

`hipsolverS`

operate on single-precision real data.Functions beginning with

`hipsolverD`

operate on double-precision real data.Functions beginning with

`hipsolverC`

operate on single-precision complex data.Functions beginning with

`hipsolverZ`

operate on double-precision complex data.

For example, the Cholesky factorization function `potrf`

is implemented as:

`hipsolverSpotrf`

- For single-precision real matrices`hipsolverDpotrf`

- For double-precision real matrices`hipsolverCpotrf`

- For single-precision complex matrices`hipsolverZpotrf`

- For double-precision complex matrices

In the documentation, these are sometimes represented generically as `hipsolver<T>potrf()`

, where `<T>`

is a placeholder for the precision type prefix.

### Understanding precision in function signatures[#](#understanding-precision-in-function-signatures)

In the function signatures throughout the documentation, precision information is indicated directly in the parameter types. For example:

```
hipsolver_status hipsolverSpotrf(hipsolverHandle_t handle,
hipsolverFillMode_t uplo,
int n,
float *A,
int lda,
float *work,
int lwork,
int *devInfo)
```

The parameter types (`float`

, `double`

, `hipFloatComplex`

, or `hipDoubleComplex`

) correspond to the
function prefix and indicate the precision used by that specific function variant.

### Real versus complex precision[#](#real-versus-complex-precision)

Some LAPACK-based functions in hipSOLVER have different behaviors or names when operating on real versus complex data:

Functions for symmetric matrices (prefix

`sy`

) use the same name for both real precision types.Functions for Hermitian matrices (prefix

`he`

) are used for complex precision types.Some auxiliary routines might be specific to real or complex precision types.


For example, `hipsolverSsyevj`

and `hipsolverDsyevj`

handle real symmetric matrices, while `hipsolverCheevj`

and `hipsolverZheevj`

handle complex Hermitian matrices.
