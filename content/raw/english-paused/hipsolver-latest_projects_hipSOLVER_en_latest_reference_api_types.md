---
title: "hipSOLVER data types &#8212; hipSOLVER 3.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:05:40.640949+00:00
content_hash: "3656403dcb97cb5f"
---

# hipSOLVER data types[#](#hipsolver-data-types)

hipSOLVER defines data types and enumerations that are internally converted to the corresponding backend types at runtime. Here are the types used in the regular API.

## hipSOLVER regular API types[#](#hipsolver-regular-api-types)

### hipsolverHandle_t[#](#hipsolverhandle-t)

-
typedef void *hipsolverHandle_t
[#](#_CPPv417hipsolverHandle_t)

### hipsolverGesvdjInfo_t[#](#hipsolvergesvdjinfo-t)

-
typedef void *hipsolverGesvdjInfo_t
[#](#_CPPv421hipsolverGesvdjInfo_t)

### hipsolverSyevjInfo_t[#](#hipsolversyevjinfo-t)

-
typedef void *hipsolverSyevjInfo_t
[#](#_CPPv420hipsolverSyevjInfo_t)

### hipsolverStatus_t[#](#hipsolverstatus-t)

-
enum hipsolverStatus_t
[#](#_CPPv417hipsolverStatus_t) *Values:*-
enumerator HIPSOLVER_STATUS_SUCCESS
[#](#_CPPv4N17hipsolverStatus_t24HIPSOLVER_STATUS_SUCCESSE)

-
enumerator HIPSOLVER_STATUS_NOT_INITIALIZED
[#](#_CPPv4N17hipsolverStatus_t32HIPSOLVER_STATUS_NOT_INITIALIZEDE)

-
enumerator HIPSOLVER_STATUS_ALLOC_FAILED
[#](#_CPPv4N17hipsolverStatus_t29HIPSOLVER_STATUS_ALLOC_FAILEDE)

-
enumerator HIPSOLVER_STATUS_INVALID_VALUE
[#](#_CPPv4N17hipsolverStatus_t30HIPSOLVER_STATUS_INVALID_VALUEE)

-
enumerator HIPSOLVER_STATUS_MAPPING_ERROR
[#](#_CPPv4N17hipsolverStatus_t30HIPSOLVER_STATUS_MAPPING_ERRORE)

-
enumerator HIPSOLVER_STATUS_EXECUTION_FAILED
[#](#_CPPv4N17hipsolverStatus_t33HIPSOLVER_STATUS_EXECUTION_FAILEDE)

-
enumerator HIPSOLVER_STATUS_INTERNAL_ERROR
[#](#_CPPv4N17hipsolverStatus_t31HIPSOLVER_STATUS_INTERNAL_ERRORE)

-
enumerator HIPSOLVER_STATUS_NOT_SUPPORTED
[#](#_CPPv4N17hipsolverStatus_t30HIPSOLVER_STATUS_NOT_SUPPORTEDE)

-
enumerator HIPSOLVER_STATUS_ARCH_MISMATCH
[#](#_CPPv4N17hipsolverStatus_t30HIPSOLVER_STATUS_ARCH_MISMATCHE)

-
enumerator HIPSOLVER_STATUS_HANDLE_IS_NULLPTR
[#](#_CPPv4N17hipsolverStatus_t34HIPSOLVER_STATUS_HANDLE_IS_NULLPTRE)

-
enumerator HIPSOLVER_STATUS_INVALID_ENUM
[#](#_CPPv4N17hipsolverStatus_t29HIPSOLVER_STATUS_INVALID_ENUME)

-
enumerator HIPSOLVER_STATUS_UNKNOWN
[#](#_CPPv4N17hipsolverStatus_t24HIPSOLVER_STATUS_UNKNOWNE)

-
enumerator HIPSOLVER_STATUS_ZERO_PIVOT
[#](#_CPPv4N17hipsolverStatus_t27HIPSOLVER_STATUS_ZERO_PIVOTE)

-
enumerator HIPSOLVER_STATUS_MATRIX_TYPE_NOT_SUPPORTED
[#](#_CPPv4N17hipsolverStatus_t42HIPSOLVER_STATUS_MATRIX_TYPE_NOT_SUPPORTEDE)

-
enumerator HIPSOLVER_STATUS_SUCCESS

### hipblasOperation_t[#](#hipblasoperation-t)

### hipsolverOperation_t[#](#hipsolveroperation-t)

-
typedef
[hipblasOperation_t](#_CPPv418hipblasOperation_t)hipsolverOperation_t[#](#_CPPv420hipsolverOperation_t) Alias of hipblasOperation_t. HIPSOLVER_OP_N, HIPSOLVER_OP_T, and HIPSOLVER_OP_C are provided as equivalents to HIPBLAS_OP_N, HIPBLAS_OP_T, and HIPBLAS_OP_C.


### hipblasFillMode_t[#](#hipblasfillmode-t)

-
enum hipblasFillMode_t
[#](#_CPPv417hipblasFillMode_t) Used by the Hermitian, symmetric and triangular matrix routines to specify whether the upper or lower triangle is being referenced.

*Values:*-
enumerator HIPBLAS_FILL_MODE_UPPER
[#](#_CPPv4N17hipblasFillMode_t23HIPBLAS_FILL_MODE_UPPERE) Upper triangle


-
enumerator HIPBLAS_FILL_MODE_LOWER
[#](#_CPPv4N17hipblasFillMode_t23HIPBLAS_FILL_MODE_LOWERE) Lower triangle


-
enumerator HIPBLAS_FILL_MODE_FULL
[#](#_CPPv4N17hipblasFillMode_t22HIPBLAS_FILL_MODE_FULLE)

-
enumerator HIPBLAS_FILL_MODE_UPPER

### hipsolverFillMode_t[#](#hipsolverfillmode-t)

-
typedef
[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)hipsolverFillMode_t[#](#_CPPv419hipsolverFillMode_t) Alias of hipblasFillMode_t. HIPSOLVER_FILL_MODE_UPPER and HIPSOLVER_FILL_MODE_LOWER are provided as equivalents to HIPBLAS_FILL_MODE_UPPER and HIPBLAS_FILL_MODE_LOWER.


### hipblasSideMode_t[#](#hipblassidemode-t)

-
enum hipblasSideMode_t
[#](#_CPPv417hipblasSideMode_t) Indicates the side matrix A is located relative to matrix B during multiplication.

*Values:*-
enumerator HIPBLAS_SIDE_LEFT
[#](#_CPPv4N17hipblasSideMode_t17HIPBLAS_SIDE_LEFTE) Multiply general matrix by symmetric, Hermitian or triangular matrix on the left.


-
enumerator HIPBLAS_SIDE_RIGHT
[#](#_CPPv4N17hipblasSideMode_t18HIPBLAS_SIDE_RIGHTE) Multiply general matrix by symmetric, Hermitian or triangular matrix on the right.


-
enumerator HIPBLAS_SIDE_BOTH
[#](#_CPPv4N17hipblasSideMode_t17HIPBLAS_SIDE_BOTHE)

-
enumerator HIPBLAS_SIDE_LEFT

### hipsolverSideMode_t[#](#hipsolversidemode-t)

-
typedef
[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)hipsolverSideMode_t[#](#_CPPv419hipsolverSideMode_t) Alias of hipblasSideMode_t. HIPSOLVER_SIDE_LEFT and HIPSOLVER_SIDE_RIGHT are provided as equivalents to HIPBLAS_SIDE_LEFT and HIPBLAS_SIDE_RIGHT.
