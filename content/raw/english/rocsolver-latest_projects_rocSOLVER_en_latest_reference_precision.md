---
title: "rocSOLVER precision support &#8212; rocSOLVER 3.32.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocSOLVER/en/latest/reference/precision.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:10:37.633359+00:00
content_hash: "7dccd417ba9d989b"
---

# rocSOLVER precision support[#](#rocsolver-precision-support)

This section provides an overview of the numerical precision types supported by the rocSOLVER library.

## Supported precision types[#](#supported-precision-types)

rocSOLVER supports four primary precision types across its functions:

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

rocSOLVER follows the standard LAPACK naming convention where the first letter of the function name indicates the precision type:

Functions beginning with

`rocsolver_s`

operate on single-precision real data.Functions beginning with

`rocsolver_d`

operate on double-precision real data.Functions beginning with

`rocsolver_c`

operate on single-precision complex data.Functions beginning with

`rocsolver_z`

operate on double-precision complex data.

For example, the LU factorization function `getrf`

is implemented as:

`rocsolver_sgetrf`

- For single-precision real matrices`rocsolver_dgetrf`

- For double-precision real matrices`rocsolver_cgetrf`

- For single-precision complex matrices`rocsolver_zgetrf`

- For double-precision complex matrices

In the documentation, these are often represented generically as `rocsolver_<type>getrf()`

, where `<type>`

is a placeholder for the precision type prefix.

### Understanding precision in function signatures[#](#understanding-precision-in-function-signatures)

In the function signatures throughout the documentation, precision information is indicated directly in the parameter types. For example:

```
rocblas_status rocsolver_slarfb(rocblas_handle handle, /* ... */
float *v, /* ... */
float *t, /* ... */
float *a, /* ... */)
```

The parameter types (`float`

, `double`

, `rocblas_float_complex`

, or `rocblas_double_complex`

) correspond
to the function prefix and indicate the precision used by that specific function variant.

### Real versus complex precision[#](#real-versus-complex-precision)

Some LAPACK functions have different behaviors or names when operating on real versus complex data:

Functions for symmetric matrices (prefix

`sy`

) use the same name for both real precision types.Functions for Hermitian matrices (prefix

`he`

) are used for complex precision types.Some auxiliary routines might be specific to real or complex precision types.


For example, `rocsolver_ssytrd`

and `rocsolver_dsytrd`

handle real symmetric matrices, while `rocsolver_chetrd`

and `rocsolver_zhetrd`

handle complex Hermitian matrices.
