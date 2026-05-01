---
title: "hipBLAS API &#8212; hipBLAS 3.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipBLAS/en/latest/reference/hipblas-api-functions.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:19:01.915247+00:00
content_hash: "effc7244304c0ce8"
---

# hipBLAS API[#](#hipblas-api)

The topic discusses technical aspects of the hipBLAS API and provides reference information about the API functions.

## The hipBLAS interface[#](#the-hipblas-interface)

The hipBLAS interface is compatible with the rocBLAS and cuBLAS-v2 APIs. Porting a CUDA application which originally called the cuBLAS API to an application calling the hipBLAS API should be relatively straightforward.

### GEMV API[#](#gemv-api)

For example, the hipBLAS SGEMV interface is:

```
hipblasStatus_t
hipblasSgemv(hipblasHandle_t handle,
hipblasOperation_t trans,
int m, int n, const float *alpha,
const float *A, int lda,
const float *x, int incx, const float *beta,
float *y, int incy );
```

### Batched and strided GEMM API[#](#batched-and-strided-gemm-api)

hipBLAS GEMM can process matrices in batches with regular strides by using the strided-batched version of the API:

```
hipblasStatus_t
hipblasSgemmStridedBatched(hipblasHandle_t handle,
hipblasOperation_t transa, hipblasOperation_t transb,
int m, int n, int k, const float *alpha,
const float *A, int lda, long long bsa,
const float *B, int ldb, long long bsb, const float *beta,
float *C, int ldc, long long bsc,
int batchCount);
```

hipBLAS assumes matrix `A`

and vectors `x`

and `y`

are allocated in the GPU memory space for data.
You are responsible for copying data to and from the host and device memory.

## Naming conventions[#](#naming-conventions)

hipBLAS follows the following naming conventions:

Upper case for a matrix, for example, matrix A, B, C GEMM (C = A*B)

Lower case for a vector, for example, vector x, y GEMV (y = A*x)


## Notations[#](#notations)

hipBLAS function uses the following notations to denote precisions:

h = half

bf = 16-bit brain floating point

s = single

d = double

c = single complex

z = double complex


## hipBLAS backends[#](#hipblas-backends)

hipBLAS has multiple backends for different platforms: cuBLAS for the NVIDIA
platform and rocBLAS for the AMD platform. The cuBLAS backend does not support
all the functions and only returns the `HIPBLAS_STATUS_NOT_SUPPORTED`

status
code.

The following level 1-3 and solver functions are not supported with the cuBLAS backend:

[AXPY](#hipblas-axpy)functions with half.[DOT](#hipblas-dot)functions with half and bfloat16.[SPR](#hipblas-spr)functions with`std:complex<float>`

and`std:complex<double>`

.All the batched functions except for

[TRSM](#hipblas-trsm),[GEMV](#hipblas-gemv), and[GEMM](#hipblas-gemm)and[solver functions](#solver-api)([GETRF](#hipblas-getrf),[GETRS](#hipblas-getrs),[GEQRF](#hipblas-geqrf),[GELS](#hipblas-gels)).[GETRF](#hipblas-getrf),[GETRS](#hipblas-getrs),[GEQRF](#hipblas-geqrf), and[GELS](#hipblas-gels)non-batched and strided_batched functions.

## ILP64 interfaces[#](#ilp64-interfaces)

The hipBLAS library Level-1 functions are also provided with ILP64 interfaces.
With these interfaces, all `int`

arguments are replaced with the typename
`int64_t`

. These ILP64 function names all end with the `_64`

suffix.
The only output arguments that change are for
xMAX and xMIN, for which the index is now `int64_t`

. Function level documentation is not
repeated for these APIs because they are identical in behavior to the LP64 versions.
However functions that support this alternate API include the line:
`This function supports the 64-bit integer interface`

.

The functionality of the ILP64 interfaces depends on the backend being used,
see the [rocBLAS](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/index.html) or NVIDIA CUDA cuBLAS documentation for more
information about support for ILP64 interfaces.

## Atomic operations[#](#atomic-operations)

Some hipBLAS functions might use atomic operations to increase performance.
This can cause these functions to give results that are not bit-wise reproducible.
By default, the rocBLAS backend allows the use of atomics while the CUDA cuBLAS backend disallows their use.
To set the desired behavior, users can call
[ hipblasSetAtomicsMode()](#_CPPv421hipblasSetAtomicsMode15hipblasHandle_t20hipblasAtomicsMode_t). See the

[rocBLAS](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/index.html)or CUDA cuBLAS documentation for more specific information about atomic operations in the backend library.

## Graph support for hipBLAS[#](#graph-support-for-hipblas)

Graph support (also referred to as stream capture support) for hipBLAS depends on the backend being used.
If rocBLAS is the backend, see the [rocBLAS](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/index.html) documentation.
Similarly, if CUDA cuBLAS is the backend, see the cuBLAS documentation.

## Custom data types[#](#custom-data-types)

hipBlas defines the `hipblasBfloat16`

. For more details, see
[Custom types](data-type-support.html#custom-types).

# hipBLAS types[#](#hipblas-types)

For information about the `hipblasStatus_t`

, `hipblasComputeType_t`

, and `hipblasOperation_t`

enumerations,
see `hipblas-common.h`

in the [hipBLAS-common GitHub](https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipblas-common) repository.

## Definitions[#](#definitions)

### hipblasHandle_t[#](#hipblashandle-t)

-
typedef void *hipblasHandle_t
[#](#_CPPv415hipblasHandle_t) hipblasHanlde_t is a void pointer, to store the library context (either rocBLAS or cuBLAS)


### hipblasHalf[#](#hipblashalf)

-
typedef uint16_t hipblasHalf
[#](#_CPPv411hipblasHalf) To specify the datatype to be unsigned short.


### hipblasInt8[#](#hipblasint8)

-
typedef int8_t hipblasInt8
[#](#_CPPv411hipblasInt8) To specify the datatype to be signed char.


### hipblasStride[#](#hipblasstride)

-
typedef int64_t hipblasStride
[#](#_CPPv413hipblasStride) Stride between matrices or vectors in strided_batched functions.


### hipblasBfloat16[#](#hipblasbfloat16)

-
struct hipblasBfloat16
[#](#_CPPv415hipblasBfloat16) Struct to represent a 16 bit Brain floating-point number.


## Enums[#](#enums)

Enumeration constants have numbering that is consistent with CBLAS, ACML, and most standard C BLAS libraries.

### hipblasStatus_t[#](#hipblasstatus-t)

For information about `hipblasStatus_t`

,
see `hipblas-common.h`

in the [hipBLAS-common GitHub](https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipblas-common) repository.

### hipblasOperation_t[#](#hipblasoperation-t)

For information about `hipblasOperation_t`

,
see `hipblas-common.h`

in the [hipBLAS-common GitHub](https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipblas-common) repository.

### hipblasPointerMode_t[#](#hipblaspointermode-t)

-
enum hipblasPointerMode_t
[#](#_CPPv420hipblasPointerMode_t) Indicates if scalar pointers are on host or device. This is used for scalars alpha and beta and for scalar function return values.

*Values:*-
enumerator HIPBLAS_POINTER_MODE_HOST
[#](#_CPPv4N20hipblasPointerMode_t25HIPBLAS_POINTER_MODE_HOSTE) Scalar values affected by this variable will be located on the host.


-
enumerator HIPBLAS_POINTER_MODE_DEVICE
[#](#_CPPv4N20hipblasPointerMode_t27HIPBLAS_POINTER_MODE_DEVICEE) Scalar values affected by this variable will be located on the device.


-
enumerator HIPBLAS_POINTER_MODE_HOST

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

### hipblasDiagType_t[#](#hipblasdiagtype-t)

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

### hipblasComputeType_t[#](#hipblascomputetype-t)

For information about `hipblasComputeType_t`

,
see `hipblas-common.h`

in the [hipBLAS-common GitHub](https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipblas-common) repository.

### hipblasGemmAlgo_t[#](#hipblasgemmalgo-t)

### hipblasAtomicsMode_t[#](#hipblasatomicsmode-t)

-
enum hipblasAtomicsMode_t
[#](#_CPPv420hipblasAtomicsMode_t) Indicates if atomics operations are allowed. Not allowing atomic operations may generally improve determinism and repeatability of results at a cost of performance. By default, the rocBLAS backend will allow atomic operations while the cuBLAS backend will disallow atomic operations. See backend documentation for more detail.

*Values:*-
enumerator HIPBLAS_ATOMICS_NOT_ALLOWED
[#](#_CPPv4N20hipblasAtomicsMode_t27HIPBLAS_ATOMICS_NOT_ALLOWEDE) Algorithms will refrain from atomics where applicable.


-
enumerator HIPBLAS_ATOMICS_ALLOWED
[#](#_CPPv4N20hipblasAtomicsMode_t23HIPBLAS_ATOMICS_ALLOWEDE) Algorithms will take advantage of atomics where applicable.


-
enumerator HIPBLAS_ATOMICS_NOT_ALLOWED

# hipBLAS functions[#](#hipblas-functions)

## Level 1 BLAS[#](#level-1-blas)

-
hipblasStatus_t hipblasIsamax(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const float *x, int incx, int *result)[#](#_CPPv413hipblasIsamax15hipblasHandle_tiPKfiPi)

-
hipblasStatus_t hipblasIdamax(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const double *x, int incx, int *result)[#](#_CPPv413hipblasIdamax15hipblasHandle_tiPKdiPi)

-
hipblasStatus_t hipblasIcamax(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipComplex *x, int incx, int *result)[#](#_CPPv413hipblasIcamax15hipblasHandle_tiPK10hipComplexiPi)

-
hipblasStatus_t hipblasIzamax(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipDoubleComplex *x, int incx, int *result)[#](#_CPPv413hipblasIzamax15hipblasHandle_tiPK16hipDoubleComplexiPi) BLAS Level 1 API.

amax finds the first index of the element of maximum magnitude of a vector x.

Supported precisions in rocBLAS : s,d,c,z.

Supported precisions in cuBLAS : s,d,c,z.


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] the number of elements in x.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[int] specifies the increment for the elements of y.**result**–**[inout]**device pointer or host pointer to store the amax index. return is 0.0 if n, incx<=0.



The `amax`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasIsamaxBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const float *const x[], int incx, int batchCount, int *result)[#](#_CPPv420hipblasIsamaxBatched15hipblasHandle_tiA_PCKfiiPi)

-
hipblasStatus_t hipblasIdamaxBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const double *const x[], int incx, int batchCount, int *result)[#](#_CPPv420hipblasIdamaxBatched15hipblasHandle_tiA_PCKdiiPi)

-
hipblasStatus_t hipblasIcamaxBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipComplex *const x[], int incx, int batchCount, int *result)[#](#_CPPv420hipblasIcamaxBatched15hipblasHandle_tiA_PCK10hipComplexiiPi)

-
hipblasStatus_t hipblasIzamaxBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipDoubleComplex *const x[], int incx, int batchCount, int *result)[#](#_CPPv420hipblasIzamaxBatched15hipblasHandle_tiA_PCK16hipDoubleComplexiiPi) BLAS Level 1 API.

amaxBatched finds the first index of the element of maximum magnitude of each vector x_i in a batch, for i = 1, …, batchCount.

Supported precisions in rocBLAS : s,d,c,z.

Supported precisions in cuBLAS : No support.


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] number of elements in each vector x_i**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[int] specifies the increment for the elements of each x_i. incx must be > 0.**batchCount**–**[in]**[int] number of instances in the batch, must be > 0.**result**–**[out]**device or host array of pointers of batchCount size for results. return is 0 if n, incx<=0.



The `amaxBatched`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasIsamaxStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const float *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount, int *result)[#](#_CPPv427hipblasIsamaxStridedBatched15hipblasHandle_tiPKfi13hipblasStrideiPi)

-
hipblasStatus_t hipblasIdamaxStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const double *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount, int *result)[#](#_CPPv427hipblasIdamaxStridedBatched15hipblasHandle_tiPKdi13hipblasStrideiPi)

-
hipblasStatus_t hipblasIcamaxStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount, int *result)[#](#_CPPv427hipblasIcamaxStridedBatched15hipblasHandle_tiPK10hipComplexi13hipblasStrideiPi)

-
hipblasStatus_t hipblasIzamaxStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipDoubleComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount, int *result)[#](#_CPPv427hipblasIzamaxStridedBatched15hipblasHandle_tiPK16hipDoubleComplexi13hipblasStrideiPi) BLAS Level 1 API.

amaxStridedBatched finds the first index of the element of maximum magnitude of each vector x_i in a batch, for i = 1, …, batchCount.

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] number of elements in each vector x_i**x**–**[in]**device pointer to the first vector x_1.**incx**–**[in]**[int] specifies the increment for the elements of each x_i. incx must be > 0.**stridex**–**[in]**[hipblasStride] specifies the pointer increment between one x_i and the next x_(i + 1).**batchCount**–**[in]**[int] number of instances in the batch**result**–**[out]**device or host pointer for storing contiguous batchCount results. return is 0 if n <= 0, incx<=0.



The `amaxStridedBatched`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasIsamin(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const float *x, int incx, int *result)[#](#_CPPv413hipblasIsamin15hipblasHandle_tiPKfiPi)

-
hipblasStatus_t hipblasIdamin(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const double *x, int incx, int *result)[#](#_CPPv413hipblasIdamin15hipblasHandle_tiPKdiPi)

-
hipblasStatus_t hipblasIcamin(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipComplex *x, int incx, int *result)[#](#_CPPv413hipblasIcamin15hipblasHandle_tiPK10hipComplexiPi)

-
hipblasStatus_t hipblasIzamin(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipDoubleComplex *x, int incx, int *result)[#](#_CPPv413hipblasIzamin15hipblasHandle_tiPK16hipDoubleComplexiPi) BLAS Level 1 API.

amin finds the first index of the element of minimum magnitude of a vector x.

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : s,d,c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] the number of elements in x.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[int] specifies the increment for the elements of y.**result**–**[inout]**device pointer or host pointer to store the amin index. return is 0.0 if n, incx<=0.



The `amin`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasIsaminBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const float *const x[], int incx, int batchCount, int *result)[#](#_CPPv420hipblasIsaminBatched15hipblasHandle_tiA_PCKfiiPi)

-
hipblasStatus_t hipblasIdaminBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const double *const x[], int incx, int batchCount, int *result)[#](#_CPPv420hipblasIdaminBatched15hipblasHandle_tiA_PCKdiiPi)

-
hipblasStatus_t hipblasIcaminBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipComplex *const x[], int incx, int batchCount, int *result)[#](#_CPPv420hipblasIcaminBatched15hipblasHandle_tiA_PCK10hipComplexiiPi)

-
hipblasStatus_t hipblasIzaminBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipDoubleComplex *const x[], int incx, int batchCount, int *result)[#](#_CPPv420hipblasIzaminBatched15hipblasHandle_tiA_PCK16hipDoubleComplexiiPi) BLAS Level 1 API.

aminBatched finds the first index of the element of minimum magnitude of each vector x_i in a batch, for i = 1, …, batchCount.

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] number of elements in each vector x_i**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[int] specifies the increment for the elements of each x_i. incx must be > 0.**batchCount**–**[in]**[int] number of instances in the batch, must be > 0.**result**–**[out]**device or host pointers to array of batchCount size for results. return is 0 if n, incx<=0.



The `aminBatched`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasIsaminStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const float *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount, int *result)[#](#_CPPv427hipblasIsaminStridedBatched15hipblasHandle_tiPKfi13hipblasStrideiPi)

-
hipblasStatus_t hipblasIdaminStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const double *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount, int *result)[#](#_CPPv427hipblasIdaminStridedBatched15hipblasHandle_tiPKdi13hipblasStrideiPi)

-
hipblasStatus_t hipblasIcaminStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount, int *result)[#](#_CPPv427hipblasIcaminStridedBatched15hipblasHandle_tiPK10hipComplexi13hipblasStrideiPi)

-
hipblasStatus_t hipblasIzaminStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipDoubleComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount, int *result)[#](#_CPPv427hipblasIzaminStridedBatched15hipblasHandle_tiPK16hipDoubleComplexi13hipblasStrideiPi) BLAS Level 1 API.

aminStridedBatched finds the first index of the element of minimum magnitude of each vector x_i in a batch, for i = 1, …, batchCount.

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] number of elements in each vector x_i**x**–**[in]**device pointer to the first vector x_1.**incx**–**[in]**[int] specifies the increment for the elements of each x_i. incx must be > 0.**stridex**–**[in]**[hipblasStride] specifies the pointer increment between one x_i and the next x_(i + 1)**batchCount**–**[in]**[int] number of instances in the batch**result**–**[out]**device or host pointer to array for storing contiguous batchCount results. return is 0 if n <= 0, incx<=0.



The `aminStridedBatched`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSasum(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const float *x, int incx, float *result)[#](#_CPPv412hipblasSasum15hipblasHandle_tiPKfiPf)

-
hipblasStatus_t hipblasDasum(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const double *x, int incx, double *result)[#](#_CPPv412hipblasDasum15hipblasHandle_tiPKdiPd)

-
hipblasStatus_t hipblasScasum(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipComplex *x, int incx, float *result)[#](#_CPPv413hipblasScasum15hipblasHandle_tiPK10hipComplexiPf)

-
hipblasStatus_t hipblasDzasum(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipDoubleComplex *x, int incx, double *result)[#](#_CPPv413hipblasDzasum15hipblasHandle_tiPK16hipDoubleComplexiPd) BLAS Level 1 API.

asum computes the sum of the magnitudes of elements of a real vector x, or the sum of magnitudes of the real and imaginary parts of elements if x is a complex vector.

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : s,d,c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] the number of elements in x and y.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[int] specifies the increment for the elements of x. incx must be > 0.**result**–**[inout]**device pointer or host pointer to store the asum product. return is 0.0 if n <= 0.



The `asum`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSasumBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const float *const x[], int incx, int batchCount, float *result)[#](#_CPPv419hipblasSasumBatched15hipblasHandle_tiA_PCKfiiPf)

-
hipblasStatus_t hipblasDasumBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const double *const x[], int incx, int batchCount, double *result)[#](#_CPPv419hipblasDasumBatched15hipblasHandle_tiA_PCKdiiPd)

-
hipblasStatus_t hipblasScasumBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipComplex *const x[], int incx, int batchCount, float *result)[#](#_CPPv420hipblasScasumBatched15hipblasHandle_tiA_PCK10hipComplexiiPf)

-
hipblasStatus_t hipblasDzasumBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipDoubleComplex *const x[], int incx, int batchCount, double *result)[#](#_CPPv420hipblasDzasumBatched15hipblasHandle_tiA_PCK16hipDoubleComplexiiPd) BLAS Level 1 API.

asumBatched computes the sum of the magnitudes of the elements in a batch of real vectors x_i, or the sum of magnitudes of the real and imaginary parts of elements if x_i is a complex vector, for i = 1, …, batchCount.

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] number of elements in each vector x_i**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[int] specifies the increment for the elements of each x_i. incx must be > 0.**batchCount**–**[in]**[int] number of instances in the batch.**result**–**[out]**device array or host array of batchCount size for results. return is 0.0 if n, incx<=0.



The `asumBatched`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSasumStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const float *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount, float *result)[#](#_CPPv426hipblasSasumStridedBatched15hipblasHandle_tiPKfi13hipblasStrideiPf)

-
hipblasStatus_t hipblasDasumStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const double *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount, double *result)[#](#_CPPv426hipblasDasumStridedBatched15hipblasHandle_tiPKdi13hipblasStrideiPd)

-
hipblasStatus_t hipblasScasumStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount, float *result)[#](#_CPPv427hipblasScasumStridedBatched15hipblasHandle_tiPK10hipComplexi13hipblasStrideiPf)

-
hipblasStatus_t hipblasDzasumStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipDoubleComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount, double *result)[#](#_CPPv427hipblasDzasumStridedBatched15hipblasHandle_tiPK16hipDoubleComplexi13hipblasStrideiPd) BLAS Level 1 API.

asumStridedBatched computes the sum of the magnitudes of elements of a real vectors x_i, or the sum of magnitudes of the real and imaginary parts of elements if x_i is a complex vector, for i = 1, …, batchCount.

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] number of elements in each vector x_i**x**–**[in]**device pointer to the first vector x_1.**incx**–**[in]**[int] specifies the increment for the elements of each x_i. incx must be > 0.**stridex**–**[in]**[hipblasStride] stride from the start of one vector (x_i) and the next one (x_i+1). There are no restrictions placed on stride_x, however the user should take care to ensure that stride_x is of appropriate size, for a typical case this means stride_x >= n * incx.**batchCount**–**[in]**[int] number of instances in the batch**result**–**[out]**device pointer or host pointer to array for storing contiguous batchCount results. return is 0.0 if n, incx<=0.



The `asumStridedBatched`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasHaxpy(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const[hipblasHalf](#_CPPv411hipblasHalf)*alpha, const[hipblasHalf](#_CPPv411hipblasHalf)*x, int incx,[hipblasHalf](#_CPPv411hipblasHalf)*y, int incy)[#](#_CPPv412hipblasHaxpy15hipblasHandle_tiPK11hipblasHalfPK11hipblasHalfiP11hipblasHalfi)

-
hipblasStatus_t hipblasSaxpy(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const float *alpha, const float *x, int incx, float *y, int incy)[#](#_CPPv412hipblasSaxpy15hipblasHandle_tiPKfPKfiPfi)

-
hipblasStatus_t hipblasDaxpy(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const double *alpha, const double *x, int incx, double *y, int incy)[#](#_CPPv412hipblasDaxpy15hipblasHandle_tiPKdPKdiPdi)

-
hipblasStatus_t hipblasCaxpy(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipComplex *alpha, const hipComplex *x, int incx, hipComplex *y, int incy)[#](#_CPPv412hipblasCaxpy15hipblasHandle_tiPK10hipComplexPK10hipComplexiP10hipComplexi)

-
hipblasStatus_t hipblasZaxpy(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *x, int incx, hipDoubleComplex *y, int incy)[#](#_CPPv412hipblasZaxpy15hipblasHandle_tiPK16hipDoubleComplexPK16hipDoubleComplexiP16hipDoubleComplexi) BLAS Level 1 API.

axpy computes constant alpha multiplied by vector x, plus vector y

y := alpha * x + y

Supported precisions in rocBLAS : h,s,d,c,z

Supported precisions in cuBLAS : s,d,c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] the number of elements in x and y.**alpha**–**[in]**device pointer or host pointer to specify the scalar alpha.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[int] specifies the increment for the elements of x.**y**–**[out]**device pointer storing vector y.**incy**–**[inout]**[int] specifies the increment for the elements of y.



The `axpy`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasHaxpyBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const[hipblasHalf](#_CPPv411hipblasHalf)*alpha, const[hipblasHalf](#_CPPv411hipblasHalf)*const x[], int incx,[hipblasHalf](#_CPPv411hipblasHalf)*const y[], int incy, int batchCount)[#](#_CPPv419hipblasHaxpyBatched15hipblasHandle_tiPK11hipblasHalfA_PCK11hipblasHalfiA_PC11hipblasHalfii)

-
hipblasStatus_t hipblasSaxpyBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const float *alpha, const float *const x[], int incx, float *const y[], int incy, int batchCount)[#](#_CPPv419hipblasSaxpyBatched15hipblasHandle_tiPKfA_PCKfiA_PCfii)

-
hipblasStatus_t hipblasDaxpyBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const double *alpha, const double *const x[], int incx, double *const y[], int incy, int batchCount)[#](#_CPPv419hipblasDaxpyBatched15hipblasHandle_tiPKdA_PCKdiA_PCdii)

-
hipblasStatus_t hipblasCaxpyBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipComplex *alpha, const hipComplex *const x[], int incx, hipComplex *const y[], int incy, int batchCount)[#](#_CPPv419hipblasCaxpyBatched15hipblasHandle_tiPK10hipComplexA_PCK10hipComplexiA_PC10hipComplexii)

-
hipblasStatus_t hipblasZaxpyBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *const x[], int incx, hipDoubleComplex *const y[], int incy, int batchCount)[#](#_CPPv419hipblasZaxpyBatched15hipblasHandle_tiPK16hipDoubleComplexA_PCK16hipDoubleComplexiA_PC16hipDoubleComplexii) BLAS Level 1 API.

axpyBatched compute y := alpha * x + y over a set of batched vectors.

Supported precisions in rocBLAS : h,s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] the number of elements in x and y.**alpha**–**[in]**specifies the scalar alpha.**x**–**[in]**pointer storing vector x on the GPU.**incx**–**[in]**[int] specifies the increment for the elements of x.**y**–**[out]**pointer storing vector y on the GPU.**incy**–**[inout]**[int] specifies the increment for the elements of y.**batchCount**–**[in]**[int] number of instances in the batch



The `axpyBatched`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasHaxpyStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const[hipblasHalf](#_CPPv411hipblasHalf)*alpha, const[hipblasHalf](#_CPPv411hipblasHalf)*x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex,[hipblasHalf](#_CPPv411hipblasHalf)*y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount)[#](#_CPPv426hipblasHaxpyStridedBatched15hipblasHandle_tiPK11hipblasHalfPK11hipblasHalfi13hipblasStrideP11hipblasHalfi13hipblasStridei)

-
hipblasStatus_t hipblasSaxpyStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const float *alpha, const float *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, float *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount)[#](#_CPPv426hipblasSaxpyStridedBatched15hipblasHandle_tiPKfPKfi13hipblasStridePfi13hipblasStridei)

-
hipblasStatus_t hipblasDaxpyStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const double *alpha, const double *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, double *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount)[#](#_CPPv426hipblasDaxpyStridedBatched15hipblasHandle_tiPKdPKdi13hipblasStridePdi13hipblasStridei)

-
hipblasStatus_t hipblasCaxpyStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipComplex *alpha, const hipComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, hipComplex *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount)[#](#_CPPv426hipblasCaxpyStridedBatched15hipblasHandle_tiPK10hipComplexPK10hipComplexi13hipblasStrideP10hipComplexi13hipblasStridei)

-
hipblasStatus_t hipblasZaxpyStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, hipDoubleComplex *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount)[#](#_CPPv426hipblasZaxpyStridedBatched15hipblasHandle_tiPK16hipDoubleComplexPK16hipDoubleComplexi13hipblasStrideP16hipDoubleComplexi13hipblasStridei) BLAS Level 1 API.

axpyStridedBatched compute y := alpha * x + y over a set of strided batched vectors.

Supported precisions in rocBLAS : h,s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int]**alpha**–**[in]**specifies the scalar alpha.**x**–**[in]**pointer storing vector x on the GPU.**incx**–**[in]**[int] specifies the increment for the elements of x.**stridex**–**[in]**[hipblasStride] specifies the increment between vectors of x.**y**–**[out]**pointer storing vector y on the GPU.**incy**–**[inout]**[int] specifies the increment for the elements of y.**stridey**–**[in]**[hipblasStride] specifies the increment between vectors of y.**batchCount**–**[in]**[int] number of instances in the batch



The `axpyStridedBatched`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasScopy(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const float *x, int incx, float *y, int incy)[#](#_CPPv412hipblasScopy15hipblasHandle_tiPKfiPfi)

-
hipblasStatus_t hipblasDcopy(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const double *x, int incx, double *y, int incy)[#](#_CPPv412hipblasDcopy15hipblasHandle_tiPKdiPdi)

-
hipblasStatus_t hipblasCcopy(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipComplex *x, int incx, hipComplex *y, int incy)[#](#_CPPv412hipblasCcopy15hipblasHandle_tiPK10hipComplexiP10hipComplexi)

-
hipblasStatus_t hipblasZcopy(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipDoubleComplex *x, int incx, hipDoubleComplex *y, int incy)[#](#_CPPv412hipblasZcopy15hipblasHandle_tiPK16hipDoubleComplexiP16hipDoubleComplexi) BLAS Level 1 API.

copy copies each element x[i] into y[i], for i = 1 , … , n

y := x,

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : s,d,c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] the number of elements in x to be copied to y.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[int] specifies the increment for the elements of x.**y**–**[out]**device pointer storing vector y.**incy**–**[in]**[int] specifies the increment for the elements of y.



The `copy`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasScopyBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const float *const x[], int incx, float *const y[], int incy, int batchCount)[#](#_CPPv419hipblasScopyBatched15hipblasHandle_tiA_PCKfiA_PCfii)

-
hipblasStatus_t hipblasDcopyBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const double *const x[], int incx, double *const y[], int incy, int batchCount)[#](#_CPPv419hipblasDcopyBatched15hipblasHandle_tiA_PCKdiA_PCdii)

-
hipblasStatus_t hipblasCcopyBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipComplex *const x[], int incx, hipComplex *const y[], int incy, int batchCount)[#](#_CPPv419hipblasCcopyBatched15hipblasHandle_tiA_PCK10hipComplexiA_PC10hipComplexii)

-
hipblasStatus_t hipblasZcopyBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipDoubleComplex *const x[], int incx, hipDoubleComplex *const y[], int incy, int batchCount)[#](#_CPPv419hipblasZcopyBatched15hipblasHandle_tiA_PCK16hipDoubleComplexiA_PC16hipDoubleComplexii) BLAS Level 1 API.

copyBatched copies each element x_i[j] into y_i[j], for j = 1 , … , n; i = 1 , … , batchCount

where (x_i, y_i) is the i-th instance of the batch. x_i and y_i are vectors.y_i := x_i,

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] the number of elements in each x_i to be copied to y_i.**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[int] specifies the increment for the elements of each vector x_i.**y**–**[out]**device array of device pointers storing each vector y_i.**incy**–**[in]**[int] specifies the increment for the elements of each vector y_i.**batchCount**–**[in]**[int] number of instances in the batch



The `copyBatched`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasScopyStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const float *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, float *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount)[#](#_CPPv426hipblasScopyStridedBatched15hipblasHandle_tiPKfi13hipblasStridePfi13hipblasStridei)

-
hipblasStatus_t hipblasDcopyStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const double *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, double *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount)[#](#_CPPv426hipblasDcopyStridedBatched15hipblasHandle_tiPKdi13hipblasStridePdi13hipblasStridei)

-
hipblasStatus_t hipblasCcopyStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, hipComplex *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount)[#](#_CPPv426hipblasCcopyStridedBatched15hipblasHandle_tiPK10hipComplexi13hipblasStrideP10hipComplexi13hipblasStridei)

-
hipblasStatus_t hipblasZcopyStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipDoubleComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, hipDoubleComplex *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount)[#](#_CPPv426hipblasZcopyStridedBatched15hipblasHandle_tiPK16hipDoubleComplexi13hipblasStrideP16hipDoubleComplexi13hipblasStridei) BLAS Level 1 API.

copyStridedBatched copies each element x_i[j] into y_i[j], for j = 1 , … , n; i = 1 , … , batchCount

where (x_i, y_i) is the i-th instance of the batch. x_i and y_i are vectors.y_i := x_i,

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] the number of elements in each x_i to be copied to y_i.**x**–**[in]**device pointer to the first vector (x_1) in the batch.**incx**–**[in]**[int] specifies the increments for the elements of vectors x_i.**stridex**–**[in]**[hipblasStride] stride from the start of one vector (x_i) and the next one (x_i+1). There are no restrictions placed on stride_x, however the user should take care to ensure that stride_x is of appropriate size, for a typical case this means stride_x >= n * incx.**y**–**[out]**device pointer to the first vector (y_1) in the batch.**incy**–**[in]**[int] specifies the increment for the elements of vectors y_i.**stridey**–**[in]**[hipblasStride] stride from the start of one vector (y_i) and the next one (y_i+1). There are no restrictions placed on stride_y, however the user should take care to ensure that stride_y is of appropriate size, for a typical case this means stride_y >= n * incy. stridey should be non zero.**batchCount**–**[in]**[int] number of instances in the batch



The `copyStridedBatched`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasHdot(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const[hipblasHalf](#_CPPv411hipblasHalf)*x, int incx, const[hipblasHalf](#_CPPv411hipblasHalf)*y, int incy,[hipblasHalf](#_CPPv411hipblasHalf)*result)[#](#_CPPv411hipblasHdot15hipblasHandle_tiPK11hipblasHalfiPK11hipblasHalfiP11hipblasHalf)

-
hipblasStatus_t hipblasBfdot(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const[hipblasBfloat16](#_CPPv415hipblasBfloat16)*x, int incx, const[hipblasBfloat16](#_CPPv415hipblasBfloat16)*y, int incy,[hipblasBfloat16](#_CPPv415hipblasBfloat16)*result)[#](#_CPPv412hipblasBfdot15hipblasHandle_tiPK15hipblasBfloat16iPK15hipblasBfloat16iP15hipblasBfloat16)

-
hipblasStatus_t hipblasSdot(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const float *x, int incx, const float *y, int incy, float *result)[#](#_CPPv411hipblasSdot15hipblasHandle_tiPKfiPKfiPf)

-
hipblasStatus_t hipblasDdot(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const double *x, int incx, const double *y, int incy, double *result)[#](#_CPPv411hipblasDdot15hipblasHandle_tiPKdiPKdiPd)

-
hipblasStatus_t hipblasCdotc(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipComplex *x, int incx, const hipComplex *y, int incy, hipComplex *result)[#](#_CPPv412hipblasCdotc15hipblasHandle_tiPK10hipComplexiPK10hipComplexiP10hipComplex)

-
hipblasStatus_t hipblasCdotu(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipComplex *x, int incx, const hipComplex *y, int incy, hipComplex *result)[#](#_CPPv412hipblasCdotu15hipblasHandle_tiPK10hipComplexiPK10hipComplexiP10hipComplex)

-
hipblasStatus_t hipblasZdotc(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipDoubleComplex *x, int incx, const hipDoubleComplex *y, int incy, hipDoubleComplex *result)[#](#_CPPv412hipblasZdotc15hipblasHandle_tiPK16hipDoubleComplexiPK16hipDoubleComplexiP16hipDoubleComplex)

-
hipblasStatus_t hipblasZdotu(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipDoubleComplex *x, int incx, const hipDoubleComplex *y, int incy, hipDoubleComplex *result)[#](#_CPPv412hipblasZdotu15hipblasHandle_tiPK16hipDoubleComplexiPK16hipDoubleComplexiP16hipDoubleComplex) BLAS Level 1 API.

dot(u) performs the dot product of vectors x and y

dotc performs the dot product of the conjugate of complex vector x and complex vector yresult = x * y;

result = conjugate (x) * y;

Supported precisions in rocBLAS : h,bf,s,d,c,z

Supported precisions in cuBLAS : s,d,c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] the number of elements in x and y.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[int] specifies the increment for the elements of y.**y**–**[in]**device pointer storing vector y.**incy**–**[in]**[int] specifies the increment for the elements of y.**result**–**[inout]**device pointer or host pointer to store the dot product. return is 0.0 if n <= 0.



The `dot`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasHdotBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const[hipblasHalf](#_CPPv411hipblasHalf)*const x[], int incx, const[hipblasHalf](#_CPPv411hipblasHalf)*const y[], int incy, int batchCount,[hipblasHalf](#_CPPv411hipblasHalf)*result)[#](#_CPPv418hipblasHdotBatched15hipblasHandle_tiA_PCK11hipblasHalfiA_PCK11hipblasHalfiiP11hipblasHalf)

-
hipblasStatus_t hipblasBfdotBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const[hipblasBfloat16](#_CPPv415hipblasBfloat16)*const x[], int incx, const[hipblasBfloat16](#_CPPv415hipblasBfloat16)*const y[], int incy, int batchCount,[hipblasBfloat16](#_CPPv415hipblasBfloat16)*result)[#](#_CPPv419hipblasBfdotBatched15hipblasHandle_tiA_PCK15hipblasBfloat16iA_PCK15hipblasBfloat16iiP15hipblasBfloat16)

-
hipblasStatus_t hipblasSdotBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const float *const x[], int incx, const float *const y[], int incy, int batchCount, float *result)[#](#_CPPv418hipblasSdotBatched15hipblasHandle_tiA_PCKfiA_PCKfiiPf)

-
hipblasStatus_t hipblasDdotBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const double *const x[], int incx, const double *const y[], int incy, int batchCount, double *result)[#](#_CPPv418hipblasDdotBatched15hipblasHandle_tiA_PCKdiA_PCKdiiPd)

-
hipblasStatus_t hipblasCdotcBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipComplex *const x[], int incx, const hipComplex *const y[], int incy, int batchCount, hipComplex *result)[#](#_CPPv419hipblasCdotcBatched15hipblasHandle_tiA_PCK10hipComplexiA_PCK10hipComplexiiP10hipComplex)

-
hipblasStatus_t hipblasCdotuBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipComplex *const x[], int incx, const hipComplex *const y[], int incy, int batchCount, hipComplex *result)[#](#_CPPv419hipblasCdotuBatched15hipblasHandle_tiA_PCK10hipComplexiA_PCK10hipComplexiiP10hipComplex)

-
hipblasStatus_t hipblasZdotcBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipDoubleComplex *const x[], int incx, const hipDoubleComplex *const y[], int incy, int batchCount, hipDoubleComplex *result)[#](#_CPPv419hipblasZdotcBatched15hipblasHandle_tiA_PCK16hipDoubleComplexiA_PCK16hipDoubleComplexiiP16hipDoubleComplex)

-
hipblasStatus_t hipblasZdotuBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipDoubleComplex *const x[], int incx, const hipDoubleComplex *const y[], int incy, int batchCount, hipDoubleComplex *result)[#](#_CPPv419hipblasZdotuBatched15hipblasHandle_tiA_PCK16hipDoubleComplexiA_PCK16hipDoubleComplexiiP16hipDoubleComplex) BLAS Level 1 API.

dotBatched(u) performs a batch of dot products of vectors x and y

dotcBatched performs a batch of dot products of the conjugate of complex vector x and complex vector yresult_i = x_i * y_i;

where (x_i, y_i) is the i-th instance of the batch. x_i and y_i are vectors, for i = 1, …, batchCountresult_i = conjugate (x_i) * y_i;

Supported precisions in rocBLAS : h,bf,s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] the number of elements in each x_i and y_i.**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**y**–**[in]**device array of device pointers storing each vector y_i.**incy**–**[in]**[int] specifies the increment for the elements of each y_i.**batchCount**–**[in]**[int] number of instances in the batch**result**–**[inout]**device array or host array of batchCount size to store the dot products of each batch. return 0.0 for each element if n <= 0.



The `dotBatched`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasHdotStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const[hipblasHalf](#_CPPv411hipblasHalf)*x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const[hipblasHalf](#_CPPv411hipblasHalf)*y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount,[hipblasHalf](#_CPPv411hipblasHalf)*result)[#](#_CPPv425hipblasHdotStridedBatched15hipblasHandle_tiPK11hipblasHalfi13hipblasStridePK11hipblasHalfi13hipblasStrideiP11hipblasHalf)

-
hipblasStatus_t hipblasBfdotStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const[hipblasBfloat16](#_CPPv415hipblasBfloat16)*x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const[hipblasBfloat16](#_CPPv415hipblasBfloat16)*y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount,[hipblasBfloat16](#_CPPv415hipblasBfloat16)*result)[#](#_CPPv426hipblasBfdotStridedBatched15hipblasHandle_tiPK15hipblasBfloat16i13hipblasStridePK15hipblasBfloat16i13hipblasStrideiP15hipblasBfloat16)

-
hipblasStatus_t hipblasSdotStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const float *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const float *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount, float *result)[#](#_CPPv425hipblasSdotStridedBatched15hipblasHandle_tiPKfi13hipblasStridePKfi13hipblasStrideiPf)

-
hipblasStatus_t hipblasDdotStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const double *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const double *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount, double *result)[#](#_CPPv425hipblasDdotStridedBatched15hipblasHandle_tiPKdi13hipblasStridePKdi13hipblasStrideiPd)

-
hipblasStatus_t hipblasCdotcStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const hipComplex *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount, hipComplex *result)[#](#_CPPv426hipblasCdotcStridedBatched15hipblasHandle_tiPK10hipComplexi13hipblasStridePK10hipComplexi13hipblasStrideiP10hipComplex)

-
hipblasStatus_t hipblasCdotuStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const hipComplex *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount, hipComplex *result)[#](#_CPPv426hipblasCdotuStridedBatched15hipblasHandle_tiPK10hipComplexi13hipblasStridePK10hipComplexi13hipblasStrideiP10hipComplex)

-
hipblasStatus_t hipblasZdotcStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipDoubleComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const hipDoubleComplex *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount, hipDoubleComplex *result)[#](#_CPPv426hipblasZdotcStridedBatched15hipblasHandle_tiPK16hipDoubleComplexi13hipblasStridePK16hipDoubleComplexi13hipblasStrideiP16hipDoubleComplex)

-
hipblasStatus_t hipblasZdotuStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipDoubleComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const hipDoubleComplex *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount, hipDoubleComplex *result)[#](#_CPPv426hipblasZdotuStridedBatched15hipblasHandle_tiPK16hipDoubleComplexi13hipblasStridePK16hipDoubleComplexi13hipblasStrideiP16hipDoubleComplex) BLAS Level 1 API.

dotStridedBatched(u) performs a batch of dot products of vectors x and y

dotcStridedBatched performs a batch of dot products of the conjugate of complex vector x and complex vector yresult_i = x_i * y_i;

where (x_i, y_i) is the i-th instance of the batch. x_i and y_i are vectors, for i = 1, …, batchCountresult_i = conjugate (x_i) * y_i;

Supported precisions in rocBLAS : h,bf,s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] the number of elements in each x_i and y_i.**x**–**[in]**device pointer to the first vector (x_1) in the batch.**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**stridex**–**[in]**[hipblasStride] stride from the start of one vector (x_i) and the next one (x_i+1)**y**–**[in]**device pointer to the first vector (y_1) in the batch.**incy**–**[in]**[int] specifies the increment for the elements of each y_i.**stridey**–**[in]**[hipblasStride] stride from the start of one vector (y_i) and the next one (y_i+1)**batchCount**–**[in]**[int] number of instances in the batch**result**–**[inout]**device array or host array of batchCount size to store the dot products of each batch. return 0.0 for each element if n <= 0.



The `dotStridedBatched`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSnrm2(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const float *x, int incx, float *result)[#](#_CPPv412hipblasSnrm215hipblasHandle_tiPKfiPf)

-
hipblasStatus_t hipblasDnrm2(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const double *x, int incx, double *result)[#](#_CPPv412hipblasDnrm215hipblasHandle_tiPKdiPd)

-
hipblasStatus_t hipblasScnrm2(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipComplex *x, int incx, float *result)[#](#_CPPv413hipblasScnrm215hipblasHandle_tiPK10hipComplexiPf)

-
hipblasStatus_t hipblasDznrm2(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipDoubleComplex *x, int incx, double *result)[#](#_CPPv413hipblasDznrm215hipblasHandle_tiPK16hipDoubleComplexiPd) BLAS Level 1 API.

nrm2 computes the euclidean norm of a real or complex vector

result := sqrt( x'*x ) for real vectors result := sqrt( x**H*x ) for complex vectors

Supported precisions in rocBLAS : s,d,c,z,sc,dz

Supported precisions in cuBLAS : s,d,sc,dz


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] the number of elements in x.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[int] specifies the increment for the elements of y.**result**–**[inout]**device pointer or host pointer to store the nrm2 product. return is 0.0 if n, incx<=0.



The `nrm2`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSnrm2Batched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const float *const x[], int incx, int batchCount, float *result)[#](#_CPPv419hipblasSnrm2Batched15hipblasHandle_tiA_PCKfiiPf)

-
hipblasStatus_t hipblasDnrm2Batched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const double *const x[], int incx, int batchCount, double *result)[#](#_CPPv419hipblasDnrm2Batched15hipblasHandle_tiA_PCKdiiPd)

-
hipblasStatus_t hipblasScnrm2Batched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipComplex *const x[], int incx, int batchCount, float *result)[#](#_CPPv420hipblasScnrm2Batched15hipblasHandle_tiA_PCK10hipComplexiiPf)

-
hipblasStatus_t hipblasDznrm2Batched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipDoubleComplex *const x[], int incx, int batchCount, double *result)[#](#_CPPv420hipblasDznrm2Batched15hipblasHandle_tiA_PCK16hipDoubleComplexiiPd) BLAS Level 1 API.

nrm2Batched computes the euclidean norm over a batch of real or complex vectors

result := sqrt( x_i'*x_i ) for real vectors x, for i = 1, ..., batchCount result := sqrt( x_i**H*x_i ) for complex vectors x, for i = 1, ..., batchCount

Supported precisions in rocBLAS : s,d,c,z,sc,dz

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] number of elements in each x_i.**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[int] specifies the increment for the elements of each x_i. incx must be > 0.**batchCount**–**[in]**[int] number of instances in the batch**result**–**[out]**device pointer or host pointer to array of batchCount size for nrm2 results. return is 0.0 for each element if n <= 0, incx<=0.



The `nrm2Batched`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSnrm2StridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const float *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount, float *result)[#](#_CPPv426hipblasSnrm2StridedBatched15hipblasHandle_tiPKfi13hipblasStrideiPf)

-
hipblasStatus_t hipblasDnrm2StridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const double *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount, double *result)[#](#_CPPv426hipblasDnrm2StridedBatched15hipblasHandle_tiPKdi13hipblasStrideiPd)

-
hipblasStatus_t hipblasScnrm2StridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount, float *result)[#](#_CPPv427hipblasScnrm2StridedBatched15hipblasHandle_tiPK10hipComplexi13hipblasStrideiPf)

-
hipblasStatus_t hipblasDznrm2StridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipDoubleComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount, double *result)[#](#_CPPv427hipblasDznrm2StridedBatched15hipblasHandle_tiPK16hipDoubleComplexi13hipblasStrideiPd) BLAS Level 1 API.

nrm2StridedBatched computes the euclidean norm over a batch of real or complex vectors

:= sqrt( x_i'*x_i ) for real vectors x, for i = 1, ..., batchCount := sqrt( x_i**H*x_i ) for complex vectors, for i = 1, ..., batchCount

Supported precisions in rocBLAS : s,d,c,z,sc,dz

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] number of elements in each x_i.**x**–**[in]**device pointer to the first vector x_1.**incx**–**[in]**[int] specifies the increment for the elements of each x_i. incx must be > 0.**stridex**–**[in]**[hipblasStride] stride from the start of one vector (x_i) and the next one (x_i+1). There are no restrictions placed on stride_x, however the user should take care to ensure that stride_x is of appropriate size, for a typical case this means stride_x >= n * incx.**batchCount**–**[in]**[int] number of instances in the batch**result**–**[out]**device pointer or host pointer to array for storing contiguous batchCount results. return is 0.0 for each element if n <= 0, incx<=0.



The `nrm2StridedBatched`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSrot(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, float *x, int incx, float *y, int incy, const float *c, const float *s)[#](#_CPPv411hipblasSrot15hipblasHandle_tiPfiPfiPKfPKf)

-
hipblasStatus_t hipblasDrot(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, double *x, int incx, double *y, int incy, const double *c, const double *s)[#](#_CPPv411hipblasDrot15hipblasHandle_tiPdiPdiPKdPKd)

-
hipblasStatus_t hipblasCrot(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, hipComplex *x, int incx, hipComplex *y, int incy, const float *c, const hipComplex *s)[#](#_CPPv411hipblasCrot15hipblasHandle_tiP10hipComplexiP10hipComplexiPKfPK10hipComplex)

-
hipblasStatus_t hipblasCsrot(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, hipComplex *x, int incx, hipComplex *y, int incy, const float *c, const float *s)[#](#_CPPv412hipblasCsrot15hipblasHandle_tiP10hipComplexiP10hipComplexiPKfPKf)

-
hipblasStatus_t hipblasZrot(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, hipDoubleComplex *x, int incx, hipDoubleComplex *y, int incy, const double *c, const hipDoubleComplex *s)[#](#_CPPv411hipblasZrot15hipblasHandle_tiP16hipDoubleComplexiP16hipDoubleComplexiPKdPK16hipDoubleComplex)

-
hipblasStatus_t hipblasZdrot(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, hipDoubleComplex *x, int incx, hipDoubleComplex *y, int incy, const double *c, const double *s)[#](#_CPPv412hipblasZdrot15hipblasHandle_tiP16hipDoubleComplexiP16hipDoubleComplexiPKdPKd) BLAS Level 1 API.

rot applies the Givens rotation matrix defined by c=cos(alpha) and s=sin(alpha) to vectors x and y. Scalars c and s may be stored in either host or device memory, location is specified by calling hipblasSetPointerMode.

Supported precisions in rocBLAS : s,d,c,z,sc,dz

Supported precisions in cuBLAS : s,d,c,z,cs,zd


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] number of elements in the x and y vectors.**x**–**[inout]**device pointer storing vector x.**incx**–**[in]**[int] specifies the increment between elements of x.**y**–**[inout]**device pointer storing vector y.**incy**–**[in]**[int] specifies the increment between elements of y.**c**–**[in]**device pointer or host pointer storing scalar cosine component of the rotation matrix.**s**–**[in]**device pointer or host pointer storing scalar sine component of the rotation matrix.



The `rot`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSrotBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, float *const x[], int incx, float *const y[], int incy, const float *c, const float *s, int batchCount)[#](#_CPPv418hipblasSrotBatched15hipblasHandle_tiA_PCfiA_PCfiPKfPKfi)

-
hipblasStatus_t hipblasDrotBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, double *const x[], int incx, double *const y[], int incy, const double *c, const double *s, int batchCount)[#](#_CPPv418hipblasDrotBatched15hipblasHandle_tiA_PCdiA_PCdiPKdPKdi)

-
hipblasStatus_t hipblasCrotBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, hipComplex *const x[], int incx, hipComplex *const y[], int incy, const float *c, const hipComplex *s, int batchCount)[#](#_CPPv418hipblasCrotBatched15hipblasHandle_tiA_PC10hipComplexiA_PC10hipComplexiPKfPK10hipComplexi)

-
hipblasStatus_t hipblasCsrotBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, hipComplex *const x[], int incx, hipComplex *const y[], int incy, const float *c, const float *s, int batchCount)[#](#_CPPv419hipblasCsrotBatched15hipblasHandle_tiA_PC10hipComplexiA_PC10hipComplexiPKfPKfi)

-
hipblasStatus_t hipblasZrotBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, hipDoubleComplex *const x[], int incx, hipDoubleComplex *const y[], int incy, const double *c, const hipDoubleComplex *s, int batchCount)[#](#_CPPv418hipblasZrotBatched15hipblasHandle_tiA_PC16hipDoubleComplexiA_PC16hipDoubleComplexiPKdPK16hipDoubleComplexi)

-
hipblasStatus_t hipblasZdrotBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, hipDoubleComplex *const x[], int incx, hipDoubleComplex *const y[], int incy, const double *c, const double *s, int batchCount)[#](#_CPPv419hipblasZdrotBatched15hipblasHandle_tiA_PC16hipDoubleComplexiA_PC16hipDoubleComplexiPKdPKdi) BLAS Level 1 API.

rotBatched applies the Givens rotation matrix defined by c=cos(alpha) and s=sin(alpha) to batched vectors x_i and y_i, for i = 1, …, batchCount. Scalars c and s may be stored in either host or device memory, location is specified by calling hipblasSetPointerMode.

Supported precisions in rocBLAS : s,d,sc,dz

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] number of elements in each x_i and y_i vectors.**x**–**[inout]**device array of device pointers storing each vector x_i.**incx**–**[in]**[int] specifies the increment between elements of each x_i.**y**–**[inout]**device array of device pointers storing each vector y_i.**incy**–**[in]**[int] specifies the increment between elements of each y_i.**c**–**[in]**device pointer or host pointer to scalar cosine component of the rotation matrix.**s**–**[in]**device pointer or host pointer to scalar sine component of the rotation matrix.**batchCount**–**[in]**[int] the number of x and y arrays, i.e. the number of batches.



The `rotBatched`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSrotStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, float *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, float *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, const float *c, const float *s, int batchCount)[#](#_CPPv425hipblasSrotStridedBatched15hipblasHandle_tiPfi13hipblasStridePfi13hipblasStridePKfPKfi)

-
hipblasStatus_t hipblasDrotStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, double *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, double *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, const double *c, const double *s, int batchCount)[#](#_CPPv425hipblasDrotStridedBatched15hipblasHandle_tiPdi13hipblasStridePdi13hipblasStridePKdPKdi)

-
hipblasStatus_t hipblasCrotStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, hipComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, hipComplex *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, const float *c, const hipComplex *s, int batchCount)[#](#_CPPv425hipblasCrotStridedBatched15hipblasHandle_tiP10hipComplexi13hipblasStrideP10hipComplexi13hipblasStridePKfPK10hipComplexi)

-
hipblasStatus_t hipblasCsrotStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, hipComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, hipComplex *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, const float *c, const float *s, int batchCount)[#](#_CPPv426hipblasCsrotStridedBatched15hipblasHandle_tiP10hipComplexi13hipblasStrideP10hipComplexi13hipblasStridePKfPKfi)

-
hipblasStatus_t hipblasZrotStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, hipDoubleComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, hipDoubleComplex *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, const double *c, const hipDoubleComplex *s, int batchCount)[#](#_CPPv425hipblasZrotStridedBatched15hipblasHandle_tiP16hipDoubleComplexi13hipblasStrideP16hipDoubleComplexi13hipblasStridePKdPK16hipDoubleComplexi)

-
hipblasStatus_t hipblasZdrotStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, hipDoubleComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, hipDoubleComplex *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, const double *c, const double *s, int batchCount)[#](#_CPPv426hipblasZdrotStridedBatched15hipblasHandle_tiP16hipDoubleComplexi13hipblasStrideP16hipDoubleComplexi13hipblasStridePKdPKdi) BLAS Level 1 API.

rotStridedBatched applies the Givens rotation matrix defined by c=cos(alpha) and s=sin(alpha) to strided batched vectors x_i and y_i, for i = 1, …, batchCount. Scalars c and s may be stored in either host or device memory, location is specified by calling hipblasSetPointerMode.

Supported precisions in rocBLAS : s,d,sc,dz

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] number of elements in each x_i and y_i vectors.**x**–**[inout]**device pointer to the first vector x_1.**incx**–**[in]**[int] specifies the increment between elements of each x_i.**stridex**–**[in]**[hipblasStride] specifies the increment from the beginning of x_i to the beginning of x_(i+1)**y**–**[inout]**device pointer to the first vector y_1.**incy**–**[in]**[int] specifies the increment between elements of each y_i.**stridey**–**[in]**[hipblasStride] specifies the increment from the beginning of y_i to the beginning of y_(i+1)**c**–**[in]**device pointer or host pointer to scalar cosine component of the rotation matrix.**s**–**[in]**device pointer or host pointer to scalar sine component of the rotation matrix.**batchCount**–**[in]**[int] the number of x and y arrays, i.e. the number of batches.



The `rotStridedBatched`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSrotg(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, float *a, float *b, float *c, float *s)[#](#_CPPv412hipblasSrotg15hipblasHandle_tPfPfPfPf)

-
hipblasStatus_t hipblasDrotg(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, double *a, double *b, double *c, double *s)[#](#_CPPv412hipblasDrotg15hipblasHandle_tPdPdPdPd)

-
hipblasStatus_t hipblasCrotg(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, hipComplex *a, hipComplex *b, float *c, hipComplex *s)[#](#_CPPv412hipblasCrotg15hipblasHandle_tP10hipComplexP10hipComplexPfP10hipComplex)

-
hipblasStatus_t hipblasZrotg(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, hipDoubleComplex *a, hipDoubleComplex *b, double *c, hipDoubleComplex *s)[#](#_CPPv412hipblasZrotg15hipblasHandle_tP16hipDoubleComplexP16hipDoubleComplexPdP16hipDoubleComplex) BLAS Level 1 API.

rotg creates the Givens rotation matrix for the vector (a b). Scalars c and s and arrays a and b may be stored in either host or device memory, location is specified by calling hipblasSetPointerMode. If the pointer mode is set to HIPBLAS_POINTER_MODE_HOST, this function blocks the CPU until the GPU has finished and the results are available in host memory. If the pointer mode is set to HIPBLAS_POINTER_MODE_DEVICE, this function returns immediately and synchronization is required to read the results.

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : s,d,c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**a**–**[inout]**device pointer or host pointer to input vector element, overwritten with r.**b**–**[inout]**device pointer or host pointer to input vector element, overwritten with z.**c**–**[inout]**device pointer or host pointer to cosine element of Givens rotation.**s**–**[inout]**device pointer or host pointer sine element of Givens rotation.



The `rotg`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSrotgBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, float *const a[], float *const b[], float *const c[], float *const s[], int batchCount)[#](#_CPPv419hipblasSrotgBatched15hipblasHandle_tA_PCfA_PCfA_PCfA_PCfi)

-
hipblasStatus_t hipblasDrotgBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, double *const a[], double *const b[], double *const c[], double *const s[], int batchCount)[#](#_CPPv419hipblasDrotgBatched15hipblasHandle_tA_PCdA_PCdA_PCdA_PCdi)

-
hipblasStatus_t hipblasCrotgBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, hipComplex *const a[], hipComplex *const b[], float *const c[], hipComplex *const s[], int batchCount)[#](#_CPPv419hipblasCrotgBatched15hipblasHandle_tA_PC10hipComplexA_PC10hipComplexA_PCfA_PC10hipComplexi)

-
hipblasStatus_t hipblasZrotgBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, hipDoubleComplex *const a[], hipDoubleComplex *const b[], double *const c[], hipDoubleComplex *const s[], int batchCount)[#](#_CPPv419hipblasZrotgBatched15hipblasHandle_tA_PC16hipDoubleComplexA_PC16hipDoubleComplexA_PCdA_PC16hipDoubleComplexi) BLAS Level 1 API.

rotgBatched creates the Givens rotation matrix for the batched vectors (a_i b_i), for i = 1, …, batchCount. a, b, c, and s may be stored in either host or device memory, location is specified by calling hipblasSetPointerMode. If the pointer mode is set to HIPBLAS_POINTER_MODE_HOST, this function blocks the CPU until the GPU has finished and the results are available in host memory. If the pointer mode is set to HIPBLAS_POINTER_MODE_DEVICE, this function returns immediately and synchronization is required to read the results.

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**a**–**[inout]**device array of device pointers storing each single input vector element a_i, overwritten with r_i.**b**–**[inout]**device array of device pointers storing each single input vector element b_i, overwritten with z_i.**c**–**[inout]**device array of device pointers storing each cosine element of Givens rotation for the batch.**s**–**[inout]**device array of device pointers storing each sine element of Givens rotation for the batch.**batchCount**–**[in]**[int] number of batches (length of arrays a, b, c, and s).



The `rotgBatched`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSrotgStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, float *a,[hipblasStride](#_CPPv413hipblasStride)stridea, float *b,[hipblasStride](#_CPPv413hipblasStride)strideb, float *c,[hipblasStride](#_CPPv413hipblasStride)stridec, float *s,[hipblasStride](#_CPPv413hipblasStride)strides, int batchCount)[#](#_CPPv426hipblasSrotgStridedBatched15hipblasHandle_tPf13hipblasStridePf13hipblasStridePf13hipblasStridePf13hipblasStridei)

-
hipblasStatus_t hipblasDrotgStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, double *a,[hipblasStride](#_CPPv413hipblasStride)stridea, double *b,[hipblasStride](#_CPPv413hipblasStride)strideb, double *c,[hipblasStride](#_CPPv413hipblasStride)stridec, double *s,[hipblasStride](#_CPPv413hipblasStride)strides, int batchCount)[#](#_CPPv426hipblasDrotgStridedBatched15hipblasHandle_tPd13hipblasStridePd13hipblasStridePd13hipblasStridePd13hipblasStridei)

-
hipblasStatus_t hipblasCrotgStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, hipComplex *a,[hipblasStride](#_CPPv413hipblasStride)stridea, hipComplex *b,[hipblasStride](#_CPPv413hipblasStride)strideb, float *c,[hipblasStride](#_CPPv413hipblasStride)stridec, hipComplex *s,[hipblasStride](#_CPPv413hipblasStride)strides, int batchCount)[#](#_CPPv426hipblasCrotgStridedBatched15hipblasHandle_tP10hipComplex13hipblasStrideP10hipComplex13hipblasStridePf13hipblasStrideP10hipComplex13hipblasStridei)

-
hipblasStatus_t hipblasZrotgStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, hipDoubleComplex *a,[hipblasStride](#_CPPv413hipblasStride)stridea, hipDoubleComplex *b,[hipblasStride](#_CPPv413hipblasStride)strideb, double *c,[hipblasStride](#_CPPv413hipblasStride)stridec, hipDoubleComplex *s,[hipblasStride](#_CPPv413hipblasStride)strides, int batchCount)[#](#_CPPv426hipblasZrotgStridedBatched15hipblasHandle_tP16hipDoubleComplex13hipblasStrideP16hipDoubleComplex13hipblasStridePd13hipblasStrideP16hipDoubleComplex13hipblasStridei) BLAS Level 1 API.

rotgStridedBatched creates the Givens rotation matrix for the strided batched vectors (a_i b_i), for i = 1, …, batchCount. a, b, c, and s may be stored in either host or device memory, location is specified by calling hipblasSetPointerMode. If the pointer mode is set to HIPBLAS_POINTER_MODE_HOST, this function blocks the CPU until the GPU has finished and the results are available in host memory. If the pointer mode is set to HIPBLAS_POINTER_MODE_HOST, this function returns immediately and synchronization is required to read the results.

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**a**–**[inout]**device strided_batched pointer or host strided_batched pointer to first single input vector element a_1, overwritten with r.**stridea**–**[in]**[hipblasStride] distance between elements of a in batch (distance between a_i and a_(i + 1))**b**–**[inout]**device strided_batched pointer or host strided_batched pointer to first single input vector element b_1, overwritten with z.**strideb**–**[in]**[hipblasStride] distance between elements of b in batch (distance between b_i and b_(i + 1))**c**–**[inout]**device strided_batched pointer or host strided_batched pointer to first cosine element of Givens rotations c_1.**stridec**–**[in]**[hipblasStride] distance between elements of c in batch (distance between c_i and c_(i + 1))**s**–**[inout]**device strided_batched pointer or host strided_batched pointer to sine element of Givens rotations s_1.**strides**–**[in]**[hipblasStride] distance between elements of s in batch (distance between s_i and s_(i + 1))**batchCount**–**[in]**[int] number of batches (length of arrays a, b, c, and s).



The `rotgStridedBatched`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSrotm(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, float *x, int incx, float *y, int incy, const float *param)[#](#_CPPv412hipblasSrotm15hipblasHandle_tiPfiPfiPKf)

-
hipblasStatus_t hipblasDrotm(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, double *x, int incx, double *y, int incy, const double *param)[#](#_CPPv412hipblasDrotm15hipblasHandle_tiPdiPdiPKd) BLAS Level 1 API.

rotm applies the modified Givens rotation matrix defined by param to vectors x and y.

Supported precisions in rocBLAS : s,d

Supported precisions in cuBLAS : s,d


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] number of elements in the x and y vectors.**x**–**[inout]**device pointer storing vector x.**incx**–**[in]**[int] specifies the increment between elements of x.**y**–**[inout]**device pointer storing vector y.**incy**–**[in]**[int] specifies the increment between elements of y.**param**–**[in]**device vector or host vector of 5 elements defining the rotation. param[0] = flag param[1] = H11 param[2] = H21 param[3] = H12 param[4] = H22 The flag parameter defines the form of H: flag = -1 => H = ( H11 H12 H21 H22 ) flag = 0 => H = ( 1.0 H12 H21 1.0 ) flag = 1 => H = ( H11 1.0 -1.0 H22 ) flag = -2 => H = ( 1.0 0.0 0.0 1.0 ) param may be stored in either host or device memory, location is specified by calling hipblasSetPointerMode.



The `rotm`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSrotmBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, float *const x[], int incx, float *const y[], int incy, const float *const param[], int batchCount)[#](#_CPPv419hipblasSrotmBatched15hipblasHandle_tiA_PCfiA_PCfiA_PCKfi)

-
hipblasStatus_t hipblasDrotmBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, double *const x[], int incx, double *const y[], int incy, const double *const param[], int batchCount)[#](#_CPPv419hipblasDrotmBatched15hipblasHandle_tiA_PCdiA_PCdiA_PCKdi) BLAS Level 1 API.

rotmBatched applies the modified Givens rotation matrix defined by param_i to batched vectors x_i and y_i, for i = 1, …, batchCount.

Supported precisions in rocBLAS : s,d

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] number of elements in the x and y vectors.**x**–**[inout]**device array of device pointers storing each vector x_i.**incx**–**[in]**[int] specifies the increment between elements of each x_i.**y**–**[inout]**device array of device pointers storing each vector y_1.**incy**–**[in]**[int] specifies the increment between elements of each y_i.**param**–**[in]**device array of device vectors of 5 elements defining the rotation. param[0] = flag param[1] = H11 param[2] = H21 param[3] = H12 param[4] = H22 The flag parameter defines the form of H: flag = -1 => H = ( H11 H12 H21 H22 ) flag = 0 => H = ( 1.0 H12 H21 1.0 ) flag = 1 => H = ( H11 1.0 -1.0 H22 ) flag = -2 => H = ( 1.0 0.0 0.0 1.0 ) param may ONLY be stored on the device for the batched version of this function.**batchCount**–**[in]**[int] the number of x and y arrays, i.e. the number of batches.



The `rotmBatched`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSrotmStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, float *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, float *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, const float *param,[hipblasStride](#_CPPv413hipblasStride)strideParam, int batchCount)[#](#_CPPv426hipblasSrotmStridedBatched15hipblasHandle_tiPfi13hipblasStridePfi13hipblasStridePKf13hipblasStridei)

-
hipblasStatus_t hipblasDrotmStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, double *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, double *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, const double *param,[hipblasStride](#_CPPv413hipblasStride)strideParam, int batchCount)[#](#_CPPv426hipblasDrotmStridedBatched15hipblasHandle_tiPdi13hipblasStridePdi13hipblasStridePKd13hipblasStridei) BLAS Level 1 API.

rotmStridedBatched applies the modified Givens rotation matrix defined by param_i to strided batched vectors x_i and y_i, for i = 1, …, batchCount

Supported precisions in rocBLAS : s,d

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] number of elements in the x and y vectors.**x**–**[inout]**device pointer pointing to first strided batched vector x_1.**incx**–**[in]**[int] specifies the increment between elements of each x_i.**stridex**–**[in]**[hipblasStride] specifies the increment between the beginning of x_i and x_(i + 1)**y**–**[inout]**device pointer pointing to first strided batched vector y_1.**incy**–**[in]**[int] specifies the increment between elements of each y_i.**stridey**–**[in]**[hipblasStride] specifies the increment between the beginning of y_i and y_(i + 1)**param**–**[in]**device pointer pointing to first array of 5 elements defining the rotation (param_1). param[0] = flag param[1] = H11 param[2] = H21 param[3] = H12 param[4] = H22 The flag parameter defines the form of H: flag = -1 => H = ( H11 H12 H21 H22 ) flag = 0 => H = ( 1.0 H12 H21 1.0 ) flag = 1 => H = ( H11 1.0 -1.0 H22 ) flag = -2 => H = ( 1.0 0.0 0.0 1.0 ) param may ONLY be stored on the device for the strided_batched version of this function.**strideParam**–**[in]**[hipblasStride] specifies the increment between the beginning of param_i and param_(i + 1)**batchCount**–**[in]**[int] the number of x and y arrays, i.e. the number of batches.



The `rotmStridedBatched`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSrotmg(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, float *d1, float *d2, float *x1, const float *y1, float *param)[#](#_CPPv413hipblasSrotmg15hipblasHandle_tPfPfPfPKfPf)

-
hipblasStatus_t hipblasDrotmg(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, double *d1, double *d2, double *x1, const double *y1, double *param)[#](#_CPPv413hipblasDrotmg15hipblasHandle_tPdPdPdPKdPd) BLAS Level 1 API.

rotmg creates the modified Givens rotation matrix for the vector (d1 * x1, d2 * y1). Parameters may be stored in either host or device memory, location is specified by calling hipblasSetPointerMode. If the pointer mode is set to HIPBLAS_POINTER_MODE_HOST, this function blocks the CPU until the GPU has finished and the results are available in host memory. If the pointer mode is set to HIPBLAS_POINTER_MODE_DEVICE, this function returns immediately and synchronization is required to read the results.

Supported precisions in rocBLAS : s,d

Supported precisions in cuBLAS : s,d


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**d1**–**[inout]**device pointer or host pointer to input scalar that is overwritten.**d2**–**[inout]**device pointer or host pointer to input scalar that is overwritten.**x1**–**[inout]**device pointer or host pointer to input scalar that is overwritten.**y1**–**[in]**device pointer or host pointer to input scalar.**param**–**[out]**device vector or host vector of 5 elements defining the rotation. param[0] = flag param[1] = H11 param[2] = H21 param[3] = H12 param[4] = H22 The flag parameter defines the form of H: flag = -1 => H = ( H11 H12 H21 H22 ) flag = 0 => H = ( 1.0 H12 H21 1.0 ) flag = 1 => H = ( H11 1.0 -1.0 H22 ) flag = -2 => H = ( 1.0 0.0 0.0 1.0 ) param may be stored in either host or device memory, location is specified by calling hipblasSetPointerMode.



The `rotmg`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSrotmgBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, float *const d1[], float *const d2[], float *const x1[], const float *const y1[], float *const param[], int batchCount)[#](#_CPPv420hipblasSrotmgBatched15hipblasHandle_tA_PCfA_PCfA_PCfA_PCKfA_PCfi)

-
hipblasStatus_t hipblasDrotmgBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, double *const d1[], double *const d2[], double *const x1[], const double *const y1[], double *const param[], int batchCount)[#](#_CPPv420hipblasDrotmgBatched15hipblasHandle_tA_PCdA_PCdA_PCdA_PCKdA_PCdi) BLAS Level 1 API.

rotmgBatched creates the modified Givens rotation matrix for the batched vectors (d1_i * x1_i, d2_i * y1_i), for i = 1, …, batchCount. Parameters may be stored in either host or device memory, location is specified by calling hipblasSetPointerMode. If the pointer mode is set to HIPBLAS_POINTER_MODE_HOST, this function blocks the CPU until the GPU has finished and the results are available in host memory. If the pointer mode is set to HIPBLAS_POINTER_MODE_DEVICE, this function returns immediately and synchronization is required to read the results.

Supported precisions in rocBLAS : s,d

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**d1**–**[inout]**device batched array or host batched array of input scalars that is overwritten.**d2**–**[inout]**device batched array or host batched array of input scalars that is overwritten.**x1**–**[inout]**device batched array or host batched array of input scalars that is overwritten.**y1**–**[in]**device batched array or host batched array of input scalars.**param**–**[out]**device batched array or host batched array of vectors of 5 elements defining the rotation. param[0] = flag param[1] = H11 param[2] = H21 param[3] = H12 param[4] = H22 The flag parameter defines the form of H: flag = -1 => H = ( H11 H12 H21 H22 ) flag = 0 => H = ( 1.0 H12 H21 1.0 ) flag = 1 => H = ( H11 1.0 -1.0 H22 ) flag = -2 => H = ( 1.0 0.0 0.0 1.0 ) param may be stored in either host or device memory, location is specified by calling hipblasSetPointerMode.**batchCount**–**[in]**[int] the number of instances in the batch.



The `rotmgBatched`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSrotmgStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, float *d1,[hipblasStride](#_CPPv413hipblasStride)strided1, float *d2,[hipblasStride](#_CPPv413hipblasStride)strided2, float *x1,[hipblasStride](#_CPPv413hipblasStride)stridex1, const float *y1,[hipblasStride](#_CPPv413hipblasStride)stridey1, float *param,[hipblasStride](#_CPPv413hipblasStride)strideParam, int batchCount)[#](#_CPPv427hipblasSrotmgStridedBatched15hipblasHandle_tPf13hipblasStridePf13hipblasStridePf13hipblasStridePKf13hipblasStridePf13hipblasStridei)

-
hipblasStatus_t hipblasDrotmgStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, double *d1,[hipblasStride](#_CPPv413hipblasStride)strided1, double *d2,[hipblasStride](#_CPPv413hipblasStride)strided2, double *x1,[hipblasStride](#_CPPv413hipblasStride)stridex1, const double *y1,[hipblasStride](#_CPPv413hipblasStride)stridey1, double *param,[hipblasStride](#_CPPv413hipblasStride)strideParam, int batchCount)[#](#_CPPv427hipblasDrotmgStridedBatched15hipblasHandle_tPd13hipblasStridePd13hipblasStridePd13hipblasStridePKd13hipblasStridePd13hipblasStridei) BLAS Level 1 API.

rotmgStridedBatched creates the modified Givens rotation matrix for the strided batched vectors (d1_i * x1_i, d2_i * y1_i), for i = 1, …, batchCount. Parameters may be stored in either host or device memory, location is specified by calling hipblasSetPointerMode. If the pointer mode is set to HIPBLAS_POINTER_MODE_HOST, this function blocks the CPU until the GPU has finished and the results are available in host memory. If the pointer mode is set to HIPBLAS_POINTER_MODE_DEVICE, this function returns immediately and synchronization is required to read the results.

Supported precisions in rocBLAS : s,d

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**d1**–**[inout]**device strided_batched array or host strided_batched array of input scalars that is overwritten.**strided1**–**[in]**[hipblasStride] specifies the increment between the beginning of d1_i and d1_(i+1)**d2**–**[inout]**device strided_batched array or host strided_batched array of input scalars that is overwritten.**strided2**–**[in]**[hipblasStride] specifies the increment between the beginning of d2_i and d2_(i+1)**x1**–**[inout]**device strided_batched array or host strided_batched array of input scalars that is overwritten.**stridex1**–**[in]**[hipblasStride] specifies the increment between the beginning of x1_i and x1_(i+1)**y1**–**[in]**device strided_batched array or host strided_batched array of input scalars.**stridey1**–**[in]**[hipblasStride] specifies the increment between the beginning of y1_i and y1_(i+1)**param**–**[out]**device stridedBatched array or host stridedBatched array of vectors of 5 elements defining the rotation. param[0] = flag param[1] = H11 param[2] = H21 param[3] = H12 param[4] = H22 The flag parameter defines the form of H: flag = -1 => H = ( H11 H12 H21 H22 ) flag = 0 => H = ( 1.0 H12 H21 1.0 ) flag = 1 => H = ( H11 1.0 -1.0 H22 ) flag = -2 => H = ( 1.0 0.0 0.0 1.0 ) param may be stored in either host or device memory, location is specified by calling hipblasSetPointerMode.**strideParam**–**[in]**[hipblasStride] specifies the increment between the beginning of param_i and param_(i + 1)**batchCount**–**[in]**[int] the number of instances in the batch.



The `rotmgStridedBatched`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSscal(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const float *alpha, float *x, int incx)[#](#_CPPv412hipblasSscal15hipblasHandle_tiPKfPfi)

-
hipblasStatus_t hipblasDscal(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const double *alpha, double *x, int incx)[#](#_CPPv412hipblasDscal15hipblasHandle_tiPKdPdi)

-
hipblasStatus_t hipblasCscal(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipComplex *alpha, hipComplex *x, int incx)[#](#_CPPv412hipblasCscal15hipblasHandle_tiPK10hipComplexP10hipComplexi)

-
hipblasStatus_t hipblasCsscal(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const float *alpha, hipComplex *x, int incx)[#](#_CPPv413hipblasCsscal15hipblasHandle_tiPKfP10hipComplexi)

-
hipblasStatus_t hipblasZscal(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipDoubleComplex *alpha, hipDoubleComplex *x, int incx)[#](#_CPPv412hipblasZscal15hipblasHandle_tiPK16hipDoubleComplexP16hipDoubleComplexi)

-
hipblasStatus_t hipblasZdscal(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const double *alpha, hipDoubleComplex *x, int incx)[#](#_CPPv413hipblasZdscal15hipblasHandle_tiPKdP16hipDoubleComplexi) BLAS Level 1 API.

scal scales each element of vector x with scalar alpha.

x := alpha * x

Supported precisions in rocBLAS : s,d,c,z,cs,zd

Supported precisions in cuBLAS : s,d,c,z,cs,zd


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] the number of elements in x.**alpha**–**[in]**device pointer or host pointer for the scalar alpha.**x**–**[inout]**device pointer storing vector x.**incx**–**[in]**[int] specifies the increment for the elements of x.



The `scal`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSscalBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const float *alpha, float *const x[], int incx, int batchCount)[#](#_CPPv419hipblasSscalBatched15hipblasHandle_tiPKfA_PCfii)

-
hipblasStatus_t hipblasDscalBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const double *alpha, double *const x[], int incx, int batchCount)[#](#_CPPv419hipblasDscalBatched15hipblasHandle_tiPKdA_PCdii)

-
hipblasStatus_t hipblasCscalBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipComplex *alpha, hipComplex *const x[], int incx, int batchCount)[#](#_CPPv419hipblasCscalBatched15hipblasHandle_tiPK10hipComplexA_PC10hipComplexii)

-
hipblasStatus_t hipblasZscalBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipDoubleComplex *alpha, hipDoubleComplex *const x[], int incx, int batchCount)[#](#_CPPv419hipblasZscalBatched15hipblasHandle_tiPK16hipDoubleComplexA_PC16hipDoubleComplexii)

-
hipblasStatus_t hipblasCsscalBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const float *alpha, hipComplex *const x[], int incx, int batchCount)[#](#_CPPv420hipblasCsscalBatched15hipblasHandle_tiPKfA_PC10hipComplexii)

-
hipblasStatus_t hipblasZdscalBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const double *alpha, hipDoubleComplex *const x[], int incx, int batchCount)[#](#_CPPv420hipblasZdscalBatched15hipblasHandle_tiPKdA_PC16hipDoubleComplexii) BLAS Level 1 API.

scalBatched scales each element of vector x_i with scalar alpha, for i = 1, … , batchCount.

where (x_i) is the i-th instance of the batch.x_i := alpha * x_i

Supported precisions in rocBLAS : s,d,c,z,cs,zd

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] the number of elements in each x_i.**alpha**–**[in]**host pointer or device pointer for the scalar alpha.**x**–**[inout]**device array of device pointers storing each vector x_i.**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**batchCount**–**[in]**[int] specifies the number of batches in x.



The `scalBatched`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSscalStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const float *alpha, float *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount)[#](#_CPPv426hipblasSscalStridedBatched15hipblasHandle_tiPKfPfi13hipblasStridei)

-
hipblasStatus_t hipblasDscalStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const double *alpha, double *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount)[#](#_CPPv426hipblasDscalStridedBatched15hipblasHandle_tiPKdPdi13hipblasStridei)

-
hipblasStatus_t hipblasCscalStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipComplex *alpha, hipComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount)[#](#_CPPv426hipblasCscalStridedBatched15hipblasHandle_tiPK10hipComplexP10hipComplexi13hipblasStridei)

-
hipblasStatus_t hipblasZscalStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const hipDoubleComplex *alpha, hipDoubleComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount)[#](#_CPPv426hipblasZscalStridedBatched15hipblasHandle_tiPK16hipDoubleComplexP16hipDoubleComplexi13hipblasStridei)

-
hipblasStatus_t hipblasCsscalStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const float *alpha, hipComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount)[#](#_CPPv427hipblasCsscalStridedBatched15hipblasHandle_tiPKfP10hipComplexi13hipblasStridei)

-
hipblasStatus_t hipblasZdscalStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const double *alpha, hipDoubleComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount)[#](#_CPPv427hipblasZdscalStridedBatched15hipblasHandle_tiPKdP16hipDoubleComplexi13hipblasStridei) BLAS Level 1 API.

scalStridedBatched scales each element of vector x_i with scalar alpha, for i = 1, … , batchCount.

where (x_i) is the i-th instance of the batch.x_i := alpha * x_i ,

Supported precisions in rocBLAS : s,d,c,z,cs,zd

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] the number of elements in each x_i.**alpha**–**[in]**host pointer or device pointer for the scalar alpha.**x**–**[inout]**device pointer to the first vector (x_1) in the batch.**incx**–**[in]**[int] specifies the increment for the elements of x.**stridex**–**[in]**[hipblasStride] stride from the start of one vector (x_i) and the next one (x_i+1). There are no restrictions placed on stride_x, however the user should take care to ensure that stride_x is of appropriate size, for a typical case this means stride_x >= n * incx.**batchCount**–**[in]**[int] specifies the number of batches in x.



The `scalStridedBatched`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSswap(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, float *x, int incx, float *y, int incy)[#](#_CPPv412hipblasSswap15hipblasHandle_tiPfiPfi)

-
hipblasStatus_t hipblasDswap(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, double *x, int incx, double *y, int incy)[#](#_CPPv412hipblasDswap15hipblasHandle_tiPdiPdi)

-
hipblasStatus_t hipblasCswap(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, hipComplex *x, int incx, hipComplex *y, int incy)[#](#_CPPv412hipblasCswap15hipblasHandle_tiP10hipComplexiP10hipComplexi)

-
hipblasStatus_t hipblasZswap(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, hipDoubleComplex *x, int incx, hipDoubleComplex *y, int incy)[#](#_CPPv412hipblasZswap15hipblasHandle_tiP16hipDoubleComplexiP16hipDoubleComplexi) BLAS Level 1 API.

swap interchanges vectors x and y.

y := x; x := y

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : s,d,c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] the number of elements in x and y.**x**–**[inout]**device pointer storing vector x.**incx**–**[in]**[int] specifies the increment for the elements of x.**y**–**[inout]**device pointer storing vector y.**incy**–**[in]**[int] specifies the increment for the elements of y.



The `swap`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSswapBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, float *const x[], int incx, float *const y[], int incy, int batchCount)[#](#_CPPv419hipblasSswapBatched15hipblasHandle_tiA_PCfiA_PCfii)

-
hipblasStatus_t hipblasDswapBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, double *const x[], int incx, double *const y[], int incy, int batchCount)[#](#_CPPv419hipblasDswapBatched15hipblasHandle_tiA_PCdiA_PCdii)

-
hipblasStatus_t hipblasCswapBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, hipComplex *const x[], int incx, hipComplex *const y[], int incy, int batchCount)[#](#_CPPv419hipblasCswapBatched15hipblasHandle_tiA_PC10hipComplexiA_PC10hipComplexii)

-
hipblasStatus_t hipblasZswapBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, hipDoubleComplex *const x[], int incx, hipDoubleComplex *const y[], int incy, int batchCount)[#](#_CPPv419hipblasZswapBatched15hipblasHandle_tiA_PC16hipDoubleComplexiA_PC16hipDoubleComplexii) BLAS Level 1 API.

swapBatched interchanges vectors x_i and y_i, for i = 1 , … , batchCount

y_i := x_i; x_i := y_i

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] the number of elements in each x_i and y_i.**x**–**[inout]**device array of device pointers storing each vector x_i.**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**y**–**[inout]**device array of device pointers storing each vector y_i.**incy**–**[in]**[int] specifies the increment for the elements of each y_i.**batchCount**–**[in]**[int] number of instances in the batch.



The `swapBatched`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSswapStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, float *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, float *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount)[#](#_CPPv426hipblasSswapStridedBatched15hipblasHandle_tiPfi13hipblasStridePfi13hipblasStridei)

-
hipblasStatus_t hipblasDswapStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, double *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, double *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount)[#](#_CPPv426hipblasDswapStridedBatched15hipblasHandle_tiPdi13hipblasStridePdi13hipblasStridei)

-
hipblasStatus_t hipblasCswapStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, hipComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, hipComplex *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount)[#](#_CPPv426hipblasCswapStridedBatched15hipblasHandle_tiP10hipComplexi13hipblasStrideP10hipComplexi13hipblasStridei)

-
hipblasStatus_t hipblasZswapStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, hipDoubleComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, hipDoubleComplex *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount)[#](#_CPPv426hipblasZswapStridedBatched15hipblasHandle_tiP16hipDoubleComplexi13hipblasStrideP16hipDoubleComplexi13hipblasStridei) BLAS Level 1 API.

swapStridedBatched interchanges vectors x_i and y_i, for i = 1 , … , batchCount

y_i := x_i; x_i := y_i

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] the number of elements in each x_i and y_i.**x**–**[inout]**device pointer to the first vector x_1.**incx**–**[in]**[int] specifies the increment for the elements of x.**stridex**–**[in]**[hipblasStride] stride from the start of one vector (x_i) and the next one (x_i+1). There are no restrictions placed on stride_x, however the user should take care to ensure that stride_x is of appropriate size, for a typical case this means stride_x >= n * incx.**y**–**[inout]**device pointer to the first vector y_1.**incy**–**[in]**[int] specifies the increment for the elements of y.**stridey**–**[in]**[hipblasStride] stride from the start of one vector (y_i) and the next one (y_i+1). There are no restrictions placed on stride_x, however the user should take care to ensure that stride_y is of appropriate size, for a typical case this means stride_y >= n * incy. stridey should be non zero.**batchCount**–**[in]**[int] number of instances in the batch.



The `swapStridedBatched`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

## Level 2 BLAS[#](#level-2-blas)

-
hipblasStatus_t hipblasSgbmv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, int m, int n, int kl, int ku, const float *alpha, const float *AP, int lda, const float *x, int incx, const float *beta, float *y, int incy)[#](#_CPPv412hipblasSgbmv15hipblasHandle_t18hipblasOperation_tiiiiPKfPKfiPKfiPKfPfi)

-
hipblasStatus_t hipblasDgbmv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, int m, int n, int kl, int ku, const double *alpha, const double *AP, int lda, const double *x, int incx, const double *beta, double *y, int incy)[#](#_CPPv412hipblasDgbmv15hipblasHandle_t18hipblasOperation_tiiiiPKdPKdiPKdiPKdPdi)

-
hipblasStatus_t hipblasCgbmv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, int m, int n, int kl, int ku, const hipComplex *alpha, const hipComplex *AP, int lda, const hipComplex *x, int incx, const hipComplex *beta, hipComplex *y, int incy)[#](#_CPPv412hipblasCgbmv15hipblasHandle_t18hipblasOperation_tiiiiPK10hipComplexPK10hipComplexiPK10hipComplexiPK10hipComplexP10hipComplexi)

-
hipblasStatus_t hipblasZgbmv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, int m, int n, int kl, int ku, const hipDoubleComplex *alpha, const hipDoubleComplex *AP, int lda, const hipDoubleComplex *x, int incx, const hipDoubleComplex *beta, hipDoubleComplex *y, int incy)[#](#_CPPv412hipblasZgbmv15hipblasHandle_t18hipblasOperation_tiiiiPK16hipDoubleComplexPK16hipDoubleComplexiPK16hipDoubleComplexiPK16hipDoubleComplexP16hipDoubleComplexi) BLAS Level 2 API.

gbmv performs one of the matrix-vector operations

where alpha and beta are scalars, x and y are vectors and A is an m by n banded matrix with kl sub-diagonals and ku super-diagonals.y := alpha*A*x + beta*y, or y := alpha*A**T*x + beta*y, or y := alpha*A**H*x + beta*y,

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : s,d,c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**trans**–**[in]**[hipblasOperation_t] indicates whether matrix A is tranposed (conjugated) or not**m**–**[in]**[int] number of rows of matrix A**n**–**[in]**[int] number of columns of matrix A**kl**–**[in]**[int] number of sub-diagonals of A**ku**–**[in]**[int] number of super-diagonals of A**alpha**–**[in]**device pointer or host pointer to scalar alpha.**AP**–**[in]**device pointer storing banded matrix A. Leading (kl + ku + 1) by n part of the matrix contains the coefficients of the banded matrix. The leading diagonal resides in row (ku + 1) with the first super-diagonal above on the RHS of row ku. The first sub-diagonal resides below on the LHS of row ku + 2. This propagates up and down across sub/super-diagonals. Ex: (m = n = 7; ku = 2, kl = 2) 1 2 3 0 0 0 0 0 0 3 3 3 3 3 4 1 2 3 0 0 0 0 2 2 2 2 2 2 5 4 1 2 3 0 0 -—> 1 1 1 1 1 1 1 0 5 4 1 2 3 0 4 4 4 4 4 4 0 0 0 5 4 1 2 0 5 5 5 5 5 0 0 0 0 0 5 4 1 2 0 0 0 0 0 0 0 0 0 0 0 5 4 1 0 0 0 0 0 0 0 Note that the empty elements which don’t correspond to data will not be referenced.**lda**–**[in]**[int] specifies the leading dimension of A. Must be >= (kl + ku + 1)**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[int] specifies the increment for the elements of x.**beta**–**[in]**device pointer or host pointer to scalar beta.**y**–**[inout]**device pointer storing vector y.**incy**–**[in]**[int] specifies the increment for the elements of y.



The `gbmv`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSgbmvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, int m, int n, int kl, int ku, const float *alpha, const float *const AP[], int lda, const float *const x[], int incx, const float *beta, float *const y[], int incy, int batchCount)[#](#_CPPv419hipblasSgbmvBatched15hipblasHandle_t18hipblasOperation_tiiiiPKfA_PCKfiA_PCKfiPKfA_PCfii)

-
hipblasStatus_t hipblasDgbmvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, int m, int n, int kl, int ku, const double *alpha, const double *const AP[], int lda, const double *const x[], int incx, const double *beta, double *const y[], int incy, int batchCount)[#](#_CPPv419hipblasDgbmvBatched15hipblasHandle_t18hipblasOperation_tiiiiPKdA_PCKdiA_PCKdiPKdA_PCdii)

-
hipblasStatus_t hipblasCgbmvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, int m, int n, int kl, int ku, const hipComplex *alpha, const hipComplex *const AP[], int lda, const hipComplex *const x[], int incx, const hipComplex *beta, hipComplex *const y[], int incy, int batchCount)[#](#_CPPv419hipblasCgbmvBatched15hipblasHandle_t18hipblasOperation_tiiiiPK10hipComplexA_PCK10hipComplexiA_PCK10hipComplexiPK10hipComplexA_PC10hipComplexii)

-
hipblasStatus_t hipblasZgbmvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, int m, int n, int kl, int ku, const hipDoubleComplex *alpha, const hipDoubleComplex *const AP[], int lda, const hipDoubleComplex *const x[], int incx, const hipDoubleComplex *beta, hipDoubleComplex *const y[], int incy, int batchCount)[#](#_CPPv419hipblasZgbmvBatched15hipblasHandle_t18hipblasOperation_tiiiiPK16hipDoubleComplexA_PCK16hipDoubleComplexiA_PCK16hipDoubleComplexiPK16hipDoubleComplexA_PC16hipDoubleComplexii) BLAS Level 2 API.

gbmvBatched performs one of the matrix-vector operations

where (A_i, x_i, y_i) is the i-th instance of the batch. alpha and beta are scalars, x_i and y_i are vectors and A_i is an m by n banded matrix with kl sub-diagonals and ku super-diagonals, for i = 1, …, batchCount.y_i := alpha*A_i*x_i + beta*y_i, or y_i := alpha*A_i**T*x_i + beta*y_i, or y_i := alpha*A_i**H*x_i + beta*y_i,

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**trans**–**[in]**[hipblasOperation_t] indicates whether matrix A is tranposed (conjugated) or not**m**–**[in]**[int] number of rows of each matrix A_i**n**–**[in]**[int] number of columns of each matrix A_i**kl**–**[in]**[int] number of sub-diagonals of each A_i**ku**–**[in]**[int] number of super-diagonals of each A_i**alpha**–**[in]**device pointer or host pointer to scalar alpha.**AP**–**[in]**device array of device pointers storing each banded matrix A_i. Leading (kl + ku + 1) by n part of the matrix contains the coefficients of the banded matrix. The leading diagonal resides in row (ku + 1) with the first super-diagonal above on the RHS of row ku. The first sub-diagonal resides below on the LHS of row ku + 2. This propagates up and down across sub/super-diagonals. Ex: (m = n = 7; ku = 2, kl = 2) 1 2 3 0 0 0 0 0 0 3 3 3 3 3 4 1 2 3 0 0 0 0 2 2 2 2 2 2 5 4 1 2 3 0 0 -—> 1 1 1 1 1 1 1 0 5 4 1 2 3 0 4 4 4 4 4 4 0 0 0 5 4 1 2 0 5 5 5 5 5 0 0 0 0 0 5 4 1 2 0 0 0 0 0 0 0 0 0 0 0 5 4 1 0 0 0 0 0 0 0 Note that the empty elements which don’t correspond to data will not be referenced.**lda**–**[in]**[int] specifies the leading dimension of each A_i. Must be >= (kl + ku + 1)**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**beta**–**[in]**device pointer or host pointer to scalar beta.**y**–**[inout]**device array of device pointers storing each vector y_i.**incy**–**[in]**[int] specifies the increment for the elements of each y_i.**batchCount**–**[in]**[int] specifies the number of instances in the batch.



The `gbmvBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSgbmvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, int m, int n, int kl, int ku, const float *alpha, const float *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const float *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const float *beta, float *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount)[#](#_CPPv426hipblasSgbmvStridedBatched15hipblasHandle_t18hipblasOperation_tiiiiPKfPKfi13hipblasStridePKfi13hipblasStridePKfPfi13hipblasStridei)

-
hipblasStatus_t hipblasDgbmvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, int m, int n, int kl, int ku, const double *alpha, const double *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const double *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const double *beta, double *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount)[#](#_CPPv426hipblasDgbmvStridedBatched15hipblasHandle_t18hipblasOperation_tiiiiPKdPKdi13hipblasStridePKdi13hipblasStridePKdPdi13hipblasStridei)

-
hipblasStatus_t hipblasCgbmvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, int m, int n, int kl, int ku, const hipComplex *alpha, const hipComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const hipComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const hipComplex *beta, hipComplex *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount)[#](#_CPPv426hipblasCgbmvStridedBatched15hipblasHandle_t18hipblasOperation_tiiiiPK10hipComplexPK10hipComplexi13hipblasStridePK10hipComplexi13hipblasStridePK10hipComplexP10hipComplexi13hipblasStridei)

-
hipblasStatus_t hipblasZgbmvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, int m, int n, int kl, int ku, const hipDoubleComplex *alpha, const hipDoubleComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const hipDoubleComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const hipDoubleComplex *beta, hipDoubleComplex *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount)[#](#_CPPv426hipblasZgbmvStridedBatched15hipblasHandle_t18hipblasOperation_tiiiiPK16hipDoubleComplexPK16hipDoubleComplexi13hipblasStridePK16hipDoubleComplexi13hipblasStridePK16hipDoubleComplexP16hipDoubleComplexi13hipblasStridei) BLAS Level 2 API.

gbmvStridedBatched performs one of the matrix-vector operations

where (A_i, x_i, y_i) is the i-th instance of the batch. alpha and beta are scalars, x_i and y_i are vectors and A_i is an m by n banded matrix with kl sub-diagonals and ku super-diagonals, for i = 1, …, batchCount.y_i := alpha*A_i*x_i + beta*y_i, or y_i := alpha*A_i**T*x_i + beta*y_i, or y_i := alpha*A_i**H*x_i + beta*y_i,

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**trans**–**[in]**[hipblasOperation_t] indicates whether matrix A is tranposed (conjugated) or not**m**–**[in]**[int] number of rows of matrix A**n**–**[in]**[int] number of columns of matrix A**kl**–**[in]**[int] number of sub-diagonals of A**ku**–**[in]**[int] number of super-diagonals of A**alpha**–**[in]**device pointer or host pointer to scalar alpha.**AP**–**[in]**device pointer to first banded matrix (A_1). Leading (kl + ku + 1) by n part of the matrix contains the coefficients of the banded matrix. The leading diagonal resides in row (ku + 1) with the first super-diagonal above on the RHS of row ku. The first sub-diagonal resides below on the LHS of row ku + 2. This propagates up and down across sub/super-diagonals. Ex: (m = n = 7; ku = 2, kl = 2) 1 2 3 0 0 0 0 0 0 3 3 3 3 3 4 1 2 3 0 0 0 0 2 2 2 2 2 2 5 4 1 2 3 0 0 -—> 1 1 1 1 1 1 1 0 5 4 1 2 3 0 4 4 4 4 4 4 0 0 0 5 4 1 2 0 5 5 5 5 5 0 0 0 0 0 5 4 1 2 0 0 0 0 0 0 0 0 0 0 0 5 4 1 0 0 0 0 0 0 0 Note that the empty elements which don’t correspond to data will not be referenced.**lda**–**[in]**[int] specifies the leading dimension of A. Must be >= (kl + ku + 1)**strideA**–**[in]**[hipblasStride] stride from the start of one matrix (A_i) and the next one (A_i+1)**x**–**[in]**device pointer to first vector (x_1).**incx**–**[in]**[int] specifies the increment for the elements of x.**stridex**–**[in]**[hipblasStride] stride from the start of one vector (x_i) and the next one (x_i+1)**beta**–**[in]**device pointer or host pointer to scalar beta.**y**–**[inout]**device pointer to first vector (y_1).**incy**–**[in]**[int] specifies the increment for the elements of y.**stridey**–**[in]**[hipblasStride] stride from the start of one vector (y_i) and the next one (x_i+1)**batchCount**–**[in]**[int] specifies the number of instances in the batch.



The `gbmvStridedBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSgemv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, int m, int n, const float *alpha, const float *AP, int lda, const float *x, int incx, const float *beta, float *y, int incy)[#](#_CPPv412hipblasSgemv15hipblasHandle_t18hipblasOperation_tiiPKfPKfiPKfiPKfPfi)

-
hipblasStatus_t hipblasDgemv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, int m, int n, const double *alpha, const double *AP, int lda, const double *x, int incx, const double *beta, double *y, int incy)[#](#_CPPv412hipblasDgemv15hipblasHandle_t18hipblasOperation_tiiPKdPKdiPKdiPKdPdi)

-
hipblasStatus_t hipblasCgemv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, int m, int n, const hipComplex *alpha, const hipComplex *AP, int lda, const hipComplex *x, int incx, const hipComplex *beta, hipComplex *y, int incy)[#](#_CPPv412hipblasCgemv15hipblasHandle_t18hipblasOperation_tiiPK10hipComplexPK10hipComplexiPK10hipComplexiPK10hipComplexP10hipComplexi)

-
hipblasStatus_t hipblasZgemv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, int m, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *AP, int lda, const hipDoubleComplex *x, int incx, const hipDoubleComplex *beta, hipDoubleComplex *y, int incy)[#](#_CPPv412hipblasZgemv15hipblasHandle_t18hipblasOperation_tiiPK16hipDoubleComplexPK16hipDoubleComplexiPK16hipDoubleComplexiPK16hipDoubleComplexP16hipDoubleComplexi) BLAS Level 2 API.

gemv performs one of the matrix-vector operations

where alpha and beta are scalars, x and y are vectors and A is an m by n matrix.y := alpha*A*x + beta*y, or y := alpha*A**T*x + beta*y, or y := alpha*A**H*x + beta*y,

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : s,d,c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**trans**–**[in]**[hipblasOperation_t] indicates whether matrix A is tranposed (conjugated) or not**m**–**[in]**[int] number of rows of matrix A**n**–**[in]**[int] number of columns of matrix A**alpha**–**[in]**device pointer or host pointer to scalar alpha.**AP**–**[in]**device pointer storing matrix A.**lda**–**[in]**[int] specifies the leading dimension of A.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[int] specifies the increment for the elements of x.**beta**–**[in]**device pointer or host pointer to scalar beta.**y**–**[inout]**device pointer storing vector y.**incy**–**[in]**[int] specifies the increment for the elements of y.



The `gemv``

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSgemvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, int m, int n, const float *alpha, const float *const AP[], int lda, const float *const x[], int incx, const float *beta, float *const y[], int incy, int batchCount)[#](#_CPPv419hipblasSgemvBatched15hipblasHandle_t18hipblasOperation_tiiPKfA_PCKfiA_PCKfiPKfA_PCfii)

-
hipblasStatus_t hipblasDgemvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, int m, int n, const double *alpha, const double *const AP[], int lda, const double *const x[], int incx, const double *beta, double *const y[], int incy, int batchCount)[#](#_CPPv419hipblasDgemvBatched15hipblasHandle_t18hipblasOperation_tiiPKdA_PCKdiA_PCKdiPKdA_PCdii)

-
hipblasStatus_t hipblasCgemvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, int m, int n, const hipComplex *alpha, const hipComplex *const AP[], int lda, const hipComplex *const x[], int incx, const hipComplex *beta, hipComplex *const y[], int incy, int batchCount)[#](#_CPPv419hipblasCgemvBatched15hipblasHandle_t18hipblasOperation_tiiPK10hipComplexA_PCK10hipComplexiA_PCK10hipComplexiPK10hipComplexA_PC10hipComplexii)

-
hipblasStatus_t hipblasZgemvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, int m, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *const AP[], int lda, const hipDoubleComplex *const x[], int incx, const hipDoubleComplex *beta, hipDoubleComplex *const y[], int incy, int batchCount)[#](#_CPPv419hipblasZgemvBatched15hipblasHandle_t18hipblasOperation_tiiPK16hipDoubleComplexA_PCK16hipDoubleComplexiA_PCK16hipDoubleComplexiPK16hipDoubleComplexA_PC16hipDoubleComplexii) BLAS Level 2 API.

gemvBatched performs a batch of matrix-vector operations

where (A_i, x_i, y_i) is the i-th instance of the batch. alpha and beta are scalars, x_i and y_i are vectors and A_i is an m by n matrix, for i = 1, …, batchCount.y_i := alpha*A_i*x_i + beta*y_i, or y_i := alpha*A_i**T*x_i + beta*y_i, or y_i := alpha*A_i**H*x_i + beta*y_i,

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**trans**–**[in]**[hipblasOperation_t] indicates whether matrices A_i are tranposed (conjugated) or not**m**–**[in]**[int] number of rows of each matrix A_i**n**–**[in]**[int] number of columns of each matrix A_i**alpha**–**[in]**device pointer or host pointer to scalar alpha.**AP**–**[in]**device array of device pointers storing each matrix A_i.**lda**–**[in]**[int] specifies the leading dimension of each matrix A_i.**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[int] specifies the increment for the elements of each vector x_i.**beta**–**[in]**device pointer or host pointer to scalar beta.**y**–**[inout]**device array of device pointers storing each vector y_i.**incy**–**[in]**[int] specifies the increment for the elements of each vector y_i.**batchCount**–**[in]**[int] number of instances in the batch



The `gemvBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSgemvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int m, int n, const float *alpha, const float *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const float *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const float *beta, float *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount)[#](#_CPPv426hipblasSgemvStridedBatched15hipblasHandle_t18hipblasOperation_tiiPKfPKfi13hipblasStridePKfi13hipblasStridePKfPfi13hipblasStridei)

-
hipblasStatus_t hipblasDgemvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int m, int n, const double *alpha, const double *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const double *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const double *beta, double *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount)[#](#_CPPv426hipblasDgemvStridedBatched15hipblasHandle_t18hipblasOperation_tiiPKdPKdi13hipblasStridePKdi13hipblasStridePKdPdi13hipblasStridei)

-
hipblasStatus_t hipblasCgemvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int m, int n, const hipComplex *alpha, const hipComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const hipComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const hipComplex *beta, hipComplex *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount)[#](#_CPPv426hipblasCgemvStridedBatched15hipblasHandle_t18hipblasOperation_tiiPK10hipComplexPK10hipComplexi13hipblasStridePK10hipComplexi13hipblasStridePK10hipComplexP10hipComplexi13hipblasStridei)

-
hipblasStatus_t hipblasZgemvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int m, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const hipDoubleComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const hipDoubleComplex *beta, hipDoubleComplex *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount)[#](#_CPPv426hipblasZgemvStridedBatched15hipblasHandle_t18hipblasOperation_tiiPK16hipDoubleComplexPK16hipDoubleComplexi13hipblasStridePK16hipDoubleComplexi13hipblasStridePK16hipDoubleComplexP16hipDoubleComplexi13hipblasStridei) BLAS Level 2 API.

gemvStridedBatched performs a batch of matrix-vector operations

where (A_i, x_i, y_i) is the i-th instance of the batch. alpha and beta are scalars, x_i and y_i are vectors and A_i is an m by n matrix, for i = 1, …, batchCount.y_i := alpha*A_i*x_i + beta*y_i, or y_i := alpha*A_i**T*x_i + beta*y_i, or y_i := alpha*A_i**H*x_i + beta*y_i,

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**transA**–**[in]**[hipblasOperation_t] indicates whether matrices A_i are tranposed (conjugated) or not**m**–**[in]**[int] number of rows of matrices A_i**n**–**[in]**[int] number of columns of matrices A_i**alpha**–**[in]**device pointer or host pointer to scalar alpha.**AP**–**[in]**device pointer to the first matrix (A_1) in the batch.**lda**–**[in]**[int] specifies the leading dimension of matrices A_i.**strideA**–**[in]**[hipblasStride] stride from the start of one matrix (A_i) and the next one (A_i+1)**x**–**[in]**device pointer to the first vector (x_1) in the batch.**incx**–**[in]**[int] specifies the increment for the elements of vectors x_i.**stridex**–**[in]**[hipblasStride] stride from the start of one vector (x_i) and the next one (x_i+1). There are no restrictions placed on stridex, however the user should take care to ensure that stridex is of appropriate size. When trans equals HIPBLAS_OP_N this typically means stridex >= n * incx, otherwise stridex >= m * incx.**beta**–**[in]**device pointer or host pointer to scalar beta.**y**–**[inout]**device pointer to the first vector (y_1) in the batch.**incy**–**[in]**[int] specifies the increment for the elements of vectors y_i.**stridey**–**[in]**[hipblasStride] stride from the start of one vector (y_i) and the next one (y_i+1). There are no restrictions placed on stridey, however the user should take care to ensure that stridey is of appropriate size. When trans equals HIPBLAS_OP_N this typically means stridey >= m * incy, otherwise stridey >= n * incy. stridey should be non zero.**batchCount**–**[in]**[int] number of instances in the batch



The `gemvStridedBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSger(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int m, int n, const float *alpha, const float *x, int incx, const float *y, int incy, float *AP, int lda)[#](#_CPPv411hipblasSger15hipblasHandle_tiiPKfPKfiPKfiPfi)

-
hipblasStatus_t hipblasDger(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int m, int n, const double *alpha, const double *x, int incx, const double *y, int incy, double *AP, int lda)[#](#_CPPv411hipblasDger15hipblasHandle_tiiPKdPKdiPKdiPdi)

-
hipblasStatus_t hipblasCgeru(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int m, int n, const hipComplex *alpha, const hipComplex *x, int incx, const hipComplex *y, int incy, hipComplex *AP, int lda)[#](#_CPPv412hipblasCgeru15hipblasHandle_tiiPK10hipComplexPK10hipComplexiPK10hipComplexiP10hipComplexi)

-
hipblasStatus_t hipblasCgerc(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int m, int n, const hipComplex *alpha, const hipComplex *x, int incx, const hipComplex *y, int incy, hipComplex *AP, int lda)[#](#_CPPv412hipblasCgerc15hipblasHandle_tiiPK10hipComplexPK10hipComplexiPK10hipComplexiP10hipComplexi)

-
hipblasStatus_t hipblasZgeru(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int m, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *x, int incx, const hipDoubleComplex *y, int incy, hipDoubleComplex *AP, int lda)[#](#_CPPv412hipblasZgeru15hipblasHandle_tiiPK16hipDoubleComplexPK16hipDoubleComplexiPK16hipDoubleComplexiP16hipDoubleComplexi)

-
hipblasStatus_t hipblasZgerc(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int m, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *x, int incx, const hipDoubleComplex *y, int incy, hipDoubleComplex *AP, int lda)[#](#_CPPv412hipblasZgerc15hipblasHandle_tiiPK16hipDoubleComplexPK16hipDoubleComplexiPK16hipDoubleComplexiP16hipDoubleComplexi) BLAS Level 2 API.

ger,geru,gerc performs the matrix-vector operations

where alpha is a scalar, x and y are vectors, and A is an m by n matrix.A := A + alpha*x*y**T , OR A := A + alpha*x*y**H for gerc

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : s,d,c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**m**–**[in]**[int] the number of rows of the matrix A.**n**–**[in]**[int] the number of columns of the matrix A.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[int] specifies the increment for the elements of x.**y**–**[in]**device pointer storing vector y.**incy**–**[in]**[int] specifies the increment for the elements of y.**AP**–**[inout]**device pointer storing matrix A.**lda**–**[in]**[int] specifies the leading dimension of A.



The `ger`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSgerBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int m, int n, const float *alpha, const float *const x[], int incx, const float *const y[], int incy, float *const AP[], int lda, int batchCount)[#](#_CPPv418hipblasSgerBatched15hipblasHandle_tiiPKfA_PCKfiA_PCKfiA_PCfii)

-
hipblasStatus_t hipblasDgerBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int m, int n, const double *alpha, const double *const x[], int incx, const double *const y[], int incy, double *const AP[], int lda, int batchCount)[#](#_CPPv418hipblasDgerBatched15hipblasHandle_tiiPKdA_PCKdiA_PCKdiA_PCdii)

-
hipblasStatus_t hipblasCgeruBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int m, int n, const hipComplex *alpha, const hipComplex *const x[], int incx, const hipComplex *const y[], int incy, hipComplex *const AP[], int lda, int batchCount)[#](#_CPPv419hipblasCgeruBatched15hipblasHandle_tiiPK10hipComplexA_PCK10hipComplexiA_PCK10hipComplexiA_PC10hipComplexii)

-
hipblasStatus_t hipblasCgercBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int m, int n, const hipComplex *alpha, const hipComplex *const x[], int incx, const hipComplex *const y[], int incy, hipComplex *const AP[], int lda, int batchCount)[#](#_CPPv419hipblasCgercBatched15hipblasHandle_tiiPK10hipComplexA_PCK10hipComplexiA_PCK10hipComplexiA_PC10hipComplexii)

-
hipblasStatus_t hipblasZgeruBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int m, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *const x[], int incx, const hipDoubleComplex *const y[], int incy, hipDoubleComplex *const AP[], int lda, int batchCount)[#](#_CPPv419hipblasZgeruBatched15hipblasHandle_tiiPK16hipDoubleComplexA_PCK16hipDoubleComplexiA_PCK16hipDoubleComplexiA_PC16hipDoubleComplexii)

-
hipblasStatus_t hipblasZgercBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int m, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *const x[], int incx, const hipDoubleComplex *const y[], int incy, hipDoubleComplex *const AP[], int lda, int batchCount)[#](#_CPPv419hipblasZgercBatched15hipblasHandle_tiiPK16hipDoubleComplexA_PCK16hipDoubleComplexiA_PCK16hipDoubleComplexiA_PC16hipDoubleComplexii) BLAS Level 2 API.

gerBatched,geruBatched,gercBatched performs a batch of the matrix-vector operations

where (A_i, x_i, y_i) is the i-th instance of the batch. alpha is a scalar, x_i and y_i are vectors and A_i is an m by n matrix, for i = 1, …, batchCount.A := A + alpha*x*y**T , OR A := A + alpha*x*y**H for gerc

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**m**–**[in]**[int] the number of rows of each matrix A_i.**n**–**[in]**[int] the number of columns of eaceh matrix A_i.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[int] specifies the increment for the elements of each vector x_i.**y**–**[in]**device array of device pointers storing each vector y_i.**incy**–**[in]**[int] specifies the increment for the elements of each vector y_i.**AP**–**[inout]**device array of device pointers storing each matrix A_i.**lda**–**[in]**[int] specifies the leading dimension of each A_i.**batchCount**–**[in]**[int] number of instances in the batch



The `gerBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSgerStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int m, int n, const float *alpha, const float *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const float *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, float *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, int batchCount)[#](#_CPPv425hipblasSgerStridedBatched15hipblasHandle_tiiPKfPKfi13hipblasStridePKfi13hipblasStridePfi13hipblasStridei)

-
hipblasStatus_t hipblasDgerStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int m, int n, const double *alpha, const double *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const double *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, double *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, int batchCount)[#](#_CPPv425hipblasDgerStridedBatched15hipblasHandle_tiiPKdPKdi13hipblasStridePKdi13hipblasStridePdi13hipblasStridei)

-
hipblasStatus_t hipblasCgeruStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int m, int n, const hipComplex *alpha, const hipComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const hipComplex *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, hipComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, int batchCount)[#](#_CPPv426hipblasCgeruStridedBatched15hipblasHandle_tiiPK10hipComplexPK10hipComplexi13hipblasStridePK10hipComplexi13hipblasStrideP10hipComplexi13hipblasStridei)

-
hipblasStatus_t hipblasCgercStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int m, int n, const hipComplex *alpha, const hipComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const hipComplex *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, hipComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, int batchCount)[#](#_CPPv426hipblasCgercStridedBatched15hipblasHandle_tiiPK10hipComplexPK10hipComplexi13hipblasStridePK10hipComplexi13hipblasStrideP10hipComplexi13hipblasStridei)

-
hipblasStatus_t hipblasZgeruStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int m, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const hipDoubleComplex *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, hipDoubleComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, int batchCount)[#](#_CPPv426hipblasZgeruStridedBatched15hipblasHandle_tiiPK16hipDoubleComplexPK16hipDoubleComplexi13hipblasStridePK16hipDoubleComplexi13hipblasStrideP16hipDoubleComplexi13hipblasStridei)

-
hipblasStatus_t hipblasZgercStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int m, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const hipDoubleComplex *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, hipDoubleComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, int batchCount)[#](#_CPPv426hipblasZgercStridedBatched15hipblasHandle_tiiPK16hipDoubleComplexPK16hipDoubleComplexi13hipblasStridePK16hipDoubleComplexi13hipblasStrideP16hipDoubleComplexi13hipblasStridei) BLAS Level 2 API.

gerStridedBatched,geruStridedBatched,gercStridedBatched performs the matrix-vector operations

where (A_i, x_i, y_i) is the i-th instance of the batch. alpha is a scalar, x_i and y_i are vectors and A_i is an m by n matrix, for i = 1, …, batchCount.A_i := A_i + alpha*x_i*y_i**T, OR A_i := A_i + alpha*x_i*y_i**H for gerc

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**m**–**[in]**[int] the number of rows of each matrix A_i.**n**–**[in]**[int] the number of columns of each matrix A_i.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device pointer to the first vector (x_1) in the batch.**incx**–**[in]**[int] specifies the increments for the elements of each vector x_i.**stridex**–**[in]**[hipblasStride] stride from the start of one vector (x_i) and the next one (x_i+1). There are no restrictions placed on stridex, however the user should take care to ensure that stridex is of appropriate size, for a typical case this means stridex >= m * incx.**y**–**[inout]**device pointer to the first vector (y_1) in the batch.**incy**–**[in]**[int] specifies the increment for the elements of each vector y_i.**stridey**–**[in]**[hipblasStride] stride from the start of one vector (y_i) and the next one (y_i+1). There are no restrictions placed on stridey, however the user should take care to ensure that stridey is of appropriate size, for a typical case this means stridey >= n * incy.**AP**–**[inout]**device pointer to the first matrix (A_1) in the batch.**lda**–**[in]**[int] specifies the leading dimension of each A_i.**strideA**–**[in]**[hipblasStride] stride from the start of one matrix (A_i) and the next one (A_i+1)**batchCount**–**[in]**[int] number of instances in the batch



The `gerStridedBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasChbmv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, int k, const hipComplex *alpha, const hipComplex *AP, int lda, const hipComplex *x, int incx, const hipComplex *beta, hipComplex *y, int incy)[#](#_CPPv412hipblasChbmv15hipblasHandle_t17hipblasFillMode_tiiPK10hipComplexPK10hipComplexiPK10hipComplexiPK10hipComplexP10hipComplexi)

-
hipblasStatus_t hipblasZhbmv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, int k, const hipDoubleComplex *alpha, const hipDoubleComplex *AP, int lda, const hipDoubleComplex *x, int incx, const hipDoubleComplex *beta, hipDoubleComplex *y, int incy)[#](#_CPPv412hipblasZhbmv15hipblasHandle_t17hipblasFillMode_tiiPK16hipDoubleComplexPK16hipDoubleComplexiPK16hipDoubleComplexiPK16hipDoubleComplexP16hipDoubleComplexi) BLAS Level 2 API.

hbmv performs the matrix-vector operations

where alpha and beta are scalars, x and y are n element vectors and A is an n by n Hermitian band matrix, with k super-diagonals.y := alpha*A*x + beta*y

Supported precisions in rocBLAS : c,z

Supported precisions in cuBLAS : c,z


if uplo == HIPBLAS_FILL_MODE_LOWER: The leading (k + 1) by n part of A must contain the lower triangular band part of the Hermitian matrix, with the leading diagonal in row (1), the first sub-diagonal on the LHS of row 2, etc. The bottom right k by k triangle of A will not be referenced. Ex (lower, lda = 2, n = 4, k = 1): A Represented matrix (1,0) (2,0) (3,0) (4,0) (1, 0) (5,-9) (0, 0) (0, 0) (5,9) (6,8) (7,7) (0,0) (5, 9) (2, 0) (6,-8) (0, 0) (0, 0) (6, 8) (3, 0) (7,-7) (0, 0) (0, 0) (7, 7) (4, 0)

As a Hermitian matrix, the imaginary part of the main diagonal of A will not be referenced and is assumed to be == 0.

- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: The upper triangular part of A is being supplied. HIPBLAS_FILL_MODE_LOWER: The lower triangular part of A is being supplied.**n**–**[in]**[int] the order of the matrix A.**k**–**[in]**[int] the number of super-diagonals of the matrix A. Must be >= 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**AP**–**[in]**device pointer storing matrix A. Of dimension (lda, n). if uplo == HIPBLAS_FILL_MODE_UPPER: The leading (k + 1) by n part of A must contain the upper triangular band part of the Hermitian matrix, with the leading diagonal in row (k + 1), the first super-diagonal on the RHS of row k, etc. The top left k by x triangle of A will not be referenced. Ex (upper, lda = n = 4, k = 1): A Represented matrix (0,0) (5,9) (6,8) (7,7) (1, 0) (5, 9) (0, 0) (0, 0) (1,0) (2,0) (3,0) (4,0) (5,-9) (2, 0) (6, 8) (0, 0) (0,0) (0,0) (0,0) (0,0) (0, 0) (6,-8) (3, 0) (7, 7) (0,0) (0,0) (0,0) (0,0) (0, 0) (0, 0) (7,-7) (4, 0)**lda**–**[in]**[int] specifies the leading dimension of A. must be >= k + 1**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[int] specifies the increment for the elements of x.**beta**–**[in]**device pointer or host pointer to scalar beta.**y**–**[inout]**device pointer storing vector y.**incy**–**[in]**[int] specifies the increment for the elements of y.



The `hbmv`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasChbmvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, int k, const hipComplex *alpha, const hipComplex *const AP[], int lda, const hipComplex *const x[], int incx, const hipComplex *beta, hipComplex *const y[], int incy, int batchCount)[#](#_CPPv419hipblasChbmvBatched15hipblasHandle_t17hipblasFillMode_tiiPK10hipComplexA_PCK10hipComplexiA_PCK10hipComplexiPK10hipComplexA_PC10hipComplexii)

-
hipblasStatus_t hipblasZhbmvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, int k, const hipDoubleComplex *alpha, const hipDoubleComplex *const AP[], int lda, const hipDoubleComplex *const x[], int incx, const hipDoubleComplex *beta, hipDoubleComplex *const y[], int incy, int batchCount)[#](#_CPPv419hipblasZhbmvBatched15hipblasHandle_t17hipblasFillMode_tiiPK16hipDoubleComplexA_PCK16hipDoubleComplexiA_PCK16hipDoubleComplexiPK16hipDoubleComplexA_PC16hipDoubleComplexii) BLAS Level 2 API.

hbmvBatched performs one of the matrix-vector operations

where alpha and beta are scalars, x_i and y_i are n element vectors and A_i is an n by n Hermitian band matrix with k super-diagonals, for each batch in i = [1, batchCount].y_i := alpha*A_i*x_i + beta*y_i

Supported precisions in rocBLAS : c,z

Supported precisions in cuBLAS : No support


if uplo == HIPBLAS_FILL_MODE_LOWER: The leading (k + 1) by n part of each A_i must contain the lower triangular band part of the Hermitian matrix, with the leading diagonal in row (1), the first sub-diagonal on the LHS of row 2, etc. The bottom right k by k triangle of each A_i will not be referenced. Ex (lower, lda = 2, n = 4, k = 1): A Represented matrix (1,0) (2,0) (3,0) (4,0) (1, 0) (5,-9) (0, 0) (0, 0) (5,9) (6,8) (7,7) (0,0) (5, 9) (2, 0) (6,-8) (0, 0) (0, 0) (6, 8) (3, 0) (7,-7) (0, 0) (0, 0) (7, 7) (4, 0)

As a Hermitian matrix, the imaginary part of the main diagonal of each A_i will not be referenced and is assumed to be == 0.

- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: The upper triangular part of each A_i is being supplied. HIPBLAS_FILL_MODE_LOWER: The lower triangular part of each A_i is being supplied.**n**–**[in]**[int] the order of each matrix A_i.**k**–**[in]**[int] the number of super-diagonals of each matrix A_i. Must be >= 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**AP**–**[in]**device array of device pointers storing each matrix_i A of dimension (lda, n). if uplo == HIPBLAS_FILL_MODE_UPPER: The leading (k + 1) by n part of each A_i must contain the upper triangular band part of the Hermitian matrix, with the leading diagonal in row (k + 1), the first super-diagonal on the RHS of row k, etc. The top left k by x triangle of each A_i will not be referenced. Ex (upper, lda = n = 4, k = 1): A Represented matrix (0,0) (5,9) (6,8) (7,7) (1, 0) (5, 9) (0, 0) (0, 0) (1,0) (2,0) (3,0) (4,0) (5,-9) (2, 0) (6, 8) (0, 0) (0,0) (0,0) (0,0) (0,0) (0, 0) (6,-8) (3, 0) (7, 7) (0,0) (0,0) (0,0) (0,0) (0, 0) (0, 0) (7,-7) (4, 0)**lda**–**[in]**[int] specifies the leading dimension of each A_i. must be >= max(1, n)**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**beta**–**[in]**device pointer or host pointer to scalar beta.**y**–**[inout]**device array of device pointers storing each vector y_i.**incy**–**[in]**[int] specifies the increment for the elements of y.**batchCount**–**[in]**[int] number of instances in the batch.



The `hbmvBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasChbmvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, int k, const hipComplex *alpha, const hipComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const hipComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const hipComplex *beta, hipComplex *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount)[#](#_CPPv426hipblasChbmvStridedBatched15hipblasHandle_t17hipblasFillMode_tiiPK10hipComplexPK10hipComplexi13hipblasStridePK10hipComplexi13hipblasStridePK10hipComplexP10hipComplexi13hipblasStridei)

-
hipblasStatus_t hipblasZhbmvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, int k, const hipDoubleComplex *alpha, const hipDoubleComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const hipDoubleComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const hipDoubleComplex *beta, hipDoubleComplex *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount)[#](#_CPPv426hipblasZhbmvStridedBatched15hipblasHandle_t17hipblasFillMode_tiiPK16hipDoubleComplexPK16hipDoubleComplexi13hipblasStridePK16hipDoubleComplexi13hipblasStridePK16hipDoubleComplexP16hipDoubleComplexi13hipblasStridei) BLAS Level 2 API.

hbmvStridedBatched performs one of the matrix-vector operations

where alpha and beta are scalars, x_i and y_i are n element vectors and A_i is an n by n Hermitian band matrix with k super-diagonals, for each batch in i = [1, batchCount].y_i := alpha*A_i*x_i + beta*y_i

Supported precisions in rocBLAS : c,z

Supported precisions in cuBLAS : No support


if uplo == HIPBLAS_FILL_MODE_LOWER: The leading (k + 1) by n part of each A_i must contain the lower triangular band part of the Hermitian matrix, with the leading diagonal in row (1), the first sub-diagonal on the LHS of row 2, etc. The bottom right k by k triangle of each A_i will not be referenced. Ex (lower, lda = 2, n = 4, k = 1): A Represented matrix (1,0) (2,0) (3,0) (4,0) (1, 0) (5,-9) (0, 0) (0, 0) (5,9) (6,8) (7,7) (0,0) (5, 9) (2, 0) (6,-8) (0, 0) (0, 0) (6, 8) (3, 0) (7,-7) (0, 0) (0, 0) (7, 7) (4, 0)

As a Hermitian matrix, the imaginary part of the main diagonal of each A_i will not be referenced and is assumed to be == 0.

- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: The upper triangular part of each A_i is being supplied. HIPBLAS_FILL_MODE_LOWER: The lower triangular part of each A_i is being supplied.**n**–**[in]**[int] the order of each matrix A_i.**k**–**[in]**[int] the number of super-diagonals of each matrix A_i. Must be >= 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**AP**–**[in]**device array pointing to the first matrix A_1. Each A_i is of dimension (lda, n). if uplo == HIPBLAS_FILL_MODE_UPPER: The leading (k + 1) by n part of each A_i must contain the upper triangular band part of the Hermitian matrix, with the leading diagonal in row (k + 1), the first super-diagonal on the RHS of row k, etc. The top left k by x triangle of each A_i will not be referenced. Ex (upper, lda = n = 4, k = 1): A Represented matrix (0,0) (5,9) (6,8) (7,7) (1, 0) (5, 9) (0, 0) (0, 0) (1,0) (2,0) (3,0) (4,0) (5,-9) (2, 0) (6, 8) (0, 0) (0,0) (0,0) (0,0) (0,0) (0, 0) (6,-8) (3, 0) (7, 7) (0,0) (0,0) (0,0) (0,0) (0, 0) (0, 0) (7,-7) (4, 0)**lda**–**[in]**[int] specifies the leading dimension of each A_i. must be >= max(1, n)**strideA**–**[in]**[hipblasStride] stride from the start of one matrix (A_i) and the next one (A_i+1)**x**–**[in]**device array pointing to the first vector y_1.**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**stridex**–**[in]**[hipblasStride] stride from the start of one vector (x_i) and the next one (x_i+1)**beta**–**[in]**device pointer or host pointer to scalar beta.**y**–**[inout]**device array pointing to the first vector y_1.**incy**–**[in]**[int] specifies the increment for the elements of y.**stridey**–**[in]**[hipblasStride] stride from the start of one vector (y_i) and the next one (y_i+1)**batchCount**–**[in]**[int] number of instances in the batch.



The `hbmvStridedBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasChemv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipComplex *alpha, const hipComplex *AP, int lda, const hipComplex *x, int incx, const hipComplex *beta, hipComplex *y, int incy)[#](#_CPPv412hipblasChemv15hipblasHandle_t17hipblasFillMode_tiPK10hipComplexPK10hipComplexiPK10hipComplexiPK10hipComplexP10hipComplexi)

-
hipblasStatus_t hipblasZhemv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *AP, int lda, const hipDoubleComplex *x, int incx, const hipDoubleComplex *beta, hipDoubleComplex *y, int incy)[#](#_CPPv412hipblasZhemv15hipblasHandle_t17hipblasFillMode_tiPK16hipDoubleComplexPK16hipDoubleComplexiPK16hipDoubleComplexiPK16hipDoubleComplexP16hipDoubleComplexi) BLAS Level 2 API.

hemv performs one of the matrix-vector operations

where alpha and beta are scalars, x and y are n element vectors and A is an n by n Hermitian matrix.y := alpha*A*x + beta*y

Supported precisions in rocBLAS : c,z

Supported precisions in cuBLAS : c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: the upper triangular part of the Hermitian matrix A is supplied. HIPBLAS_FILL_MODE_LOWER: the lower triangular part of the Hermitian matrix A is supplied.**n**–**[in]**[int] the order of the matrix A.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**AP**–**[in]**device pointer storing matrix A. Of dimension (lda, n). if uplo == HIPBLAS_FILL_MODE_UPPER: The upper triangular part of A must contain the upper triangular part of a Hermitian matrix. The lower triangular part of A will not be referenced. if uplo == HIPBLAS_FILL_MODE_LOWER: The lower triangular part of A must contain the lower triangular part of a Hermitian matrix. The upper triangular part of A will not be referenced. As a Hermitian matrix, the imaginary part of the main diagonal of A will not be referenced and is assumed to be == 0.**lda**–**[in]**[int] specifies the leading dimension of A. must be >= max(1, n)**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[int] specifies the increment for the elements of x.**beta**–**[in]**device pointer or host pointer to scalar beta.**y**–**[inout]**device pointer storing vector y.**incy**–**[in]**[int] specifies the increment for the elements of y.



The `hemv`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasChemvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipComplex *alpha, const hipComplex *const AP[], int lda, const hipComplex *const x[], int incx, const hipComplex *beta, hipComplex *const y[], int incy, int batchCount)[#](#_CPPv419hipblasChemvBatched15hipblasHandle_t17hipblasFillMode_tiPK10hipComplexA_PCK10hipComplexiA_PCK10hipComplexiPK10hipComplexA_PC10hipComplexii)

-
hipblasStatus_t hipblasZhemvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *const AP[], int lda, const hipDoubleComplex *const x[], int incx, const hipDoubleComplex *beta, hipDoubleComplex *const y[], int incy, int batchCount)[#](#_CPPv419hipblasZhemvBatched15hipblasHandle_t17hipblasFillMode_tiPK16hipDoubleComplexA_PCK16hipDoubleComplexiA_PCK16hipDoubleComplexiPK16hipDoubleComplexA_PC16hipDoubleComplexii) BLAS Level 2 API.

hemvBatched performs one of the matrix-vector operations

where alpha and beta are scalars, x_i and y_i are n element vectors and A_i is an n by n Hermitian matrix, for each batch in i = [1, batchCount].y_i := alpha*A_i*x_i + beta*y_i

Supported precisions in rocBLAS : c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: the upper triangular part of the Hermitian matrix A is supplied. HIPBLAS_FILL_MODE_LOWER: the lower triangular part of the Hermitian matrix A is supplied.**n**–**[in]**[int] the order of each matrix A_i.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**AP**–**[in]**device array of device pointers storing each matrix A_i of dimension (lda, n). if uplo == HIPBLAS_FILL_MODE_UPPER: The upper triangular part of each A_i must contain the upper triangular part of a Hermitian matrix. The lower triangular part of each A_i will not be referenced. if uplo == HIPBLAS_FILL_MODE_LOWER: The lower triangular part of each A_i must contain the lower triangular part of a Hermitian matrix. The upper triangular part of each A_i will not be referenced. As a Hermitian matrix, the imaginary part of the main diagonal of each A_i will not be referenced and is assumed to be == 0.**lda**–**[in]**[int] specifies the leading dimension of each A_i. must be >= max(1, n)**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**beta**–**[in]**device pointer or host pointer to scalar beta.**y**–**[inout]**device array of device pointers storing each vector y_i.**incy**–**[in]**[int] specifies the increment for the elements of y.**batchCount**–**[in]**[int] number of instances in the batch.



The `hemvBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasChemvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipComplex *alpha, const hipComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const hipComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const hipComplex *beta, hipComplex *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount)[#](#_CPPv426hipblasChemvStridedBatched15hipblasHandle_t17hipblasFillMode_tiPK10hipComplexPK10hipComplexi13hipblasStridePK10hipComplexi13hipblasStridePK10hipComplexP10hipComplexi13hipblasStridei)

-
hipblasStatus_t hipblasZhemvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const hipDoubleComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const hipDoubleComplex *beta, hipDoubleComplex *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount)[#](#_CPPv426hipblasZhemvStridedBatched15hipblasHandle_t17hipblasFillMode_tiPK16hipDoubleComplexPK16hipDoubleComplexi13hipblasStridePK16hipDoubleComplexi13hipblasStridePK16hipDoubleComplexP16hipDoubleComplexi13hipblasStridei) BLAS Level 2 API.

hemvStridedBatched performs one of the matrix-vector operations

where alpha and beta are scalars, x_i and y_i are n element vectors and A_i is an n by n Hermitian matrix, for each batch in i = [1, batchCount].y_i := alpha*A_i*x_i + beta*y_i

Supported precisions in rocBLAS : c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: the upper triangular part of the Hermitian matrix A is supplied. HIPBLAS_FILL_MODE_LOWER: the lower triangular part of the Hermitian matrix A is supplied.**n**–**[in]**[int] the order of each matrix A_i.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**AP**–**[in]**device array of device pointers storing each matrix A_i of dimension (lda, n). if uplo == HIPBLAS_FILL_MODE_UPPER: The upper triangular part of each A_i must contain the upper triangular part of a Hermitian matrix. The lower triangular part of each A_i will not be referenced. if uplo == HIPBLAS_FILL_MODE_LOWER: The lower triangular part of each A_i must contain the lower triangular part of a Hermitian matrix. The upper triangular part of each A_i will not be referenced. As a Hermitian matrix, the imaginary part of the main diagonal of each A_i will not be referenced and is assumed to be == 0.**lda**–**[in]**[int] specifies the leading dimension of each A_i. must be >= max(1, n)**strideA**–**[in]**[hipblasStride] stride from the start of one (A_i) to the next (A_i+1)**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**stridex**–**[in]**[hipblasStride] stride from the start of one vector (x_i) and the next one (x_i+1).**beta**–**[in]**device pointer or host pointer to scalar beta.**y**–**[inout]**device array of device pointers storing each vector y_i.**incy**–**[in]**[int] specifies the increment for the elements of y.**stridey**–**[in]**[hipblasStride] stride from the start of one vector (y_i) and the next one (y_i+1).**batchCount**–**[in]**[int] number of instances in the batch.



The `hemvStridedBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasCher(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const float *alpha, const hipComplex *x, int incx, hipComplex *AP, int lda)[#](#_CPPv411hipblasCher15hipblasHandle_t17hipblasFillMode_tiPKfPK10hipComplexiP10hipComplexi)

-
hipblasStatus_t hipblasZher(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const double *alpha, const hipDoubleComplex *x, int incx, hipDoubleComplex *AP, int lda)[#](#_CPPv411hipblasZher15hipblasHandle_t17hipblasFillMode_tiPKdPK16hipDoubleComplexiP16hipDoubleComplexi) BLAS Level 2 API.

her performs the matrix-vector operations

where alpha is a real scalar, x is a vector, and A is an n by n Hermitian matrix.A := A + alpha*x*x**H

Supported precisions in rocBLAS : c,z

Supported precisions in cuBLAS : c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] specifies whether the upper ‘HIPBLAS_FILL_MODE_UPPER’ or lower ‘HIPBLAS_FILL_MODE_LOWER’ HIPBLAS_FILL_MODE_UPPER: The upper triangular part of A is supplied in A. HIPBLAS_FILL_MODE_LOWER: The lower triangular part of A is supplied in A.**n**–**[in]**[int] the number of rows and columns of matrix A, must be at least 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[int] specifies the increment for the elements of x.**AP**–**[inout]**device pointer storing the specified triangular portion of the Hermitian matrix A. Of size (lda * n). if uplo == HIPBLAS_FILL_MODE_UPPER: The upper triangular portion of the Hermitian matrix A is supplied. The lower triangluar portion will not be touched. if uplo == HIPBLAS_FILL_MODE_LOWER: The lower triangular portion of the Hermitian matrix A is supplied. The upper triangular portion will not be touched. Note that the imaginary part of the diagonal elements are not accessed and are assumed to be 0.**lda**–**[in]**[int] specifies the leading dimension of A. Must be at least max(1, n).



The `her`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasCherBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const float *alpha, const hipComplex *const x[], int incx, hipComplex *const AP[], int lda, int batchCount)[#](#_CPPv418hipblasCherBatched15hipblasHandle_t17hipblasFillMode_tiPKfA_PCK10hipComplexiA_PC10hipComplexii)

-
hipblasStatus_t hipblasZherBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const double *alpha, const hipDoubleComplex *const x[], int incx, hipDoubleComplex *const AP[], int lda, int batchCount)[#](#_CPPv418hipblasZherBatched15hipblasHandle_t17hipblasFillMode_tiPKdA_PCK16hipDoubleComplexiA_PC16hipDoubleComplexii) BLAS Level 2 API.

herBatched performs the matrix-vector operations

where alpha is a real scalar, x_i is a vector, and A_i is an n by n symmetric matrix, for i = 1, …, batchCount.A_i := A_i + alpha*x_i*x_i**H

Supported precisions in rocBLAS : c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] specifies whether the upper ‘HIPBLAS_FILL_MODE_UPPER’ or lower ‘HIPBLAS_FILL_MODE_LOWER’ HIPBLAS_FILL_MODE_UPPER: The upper triangular part of each A_i is supplied in A. HIPBLAS_FILL_MODE_LOWER: The lower triangular part of each A_i is supplied in A.**n**–**[in]**[int] the number of rows and columns of each matrix A_i, must be at least 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**AP**–**[inout]**device array of device pointers storing the specified triangular portion of each Hermitian matrix A_i of at least size ((n * (n + 1)) / 2). Array is of at least size batchCount. if uplo == HIPBLAS_FILL_MODE_UPPER: The upper triangular portion of each Hermitian matrix A_i is supplied. The lower triangular portion of each A_i will not be touched. if uplo == HIPBLAS_FILL_MODE_LOWER: The lower triangular portion of each Hermitian matrix A_i is supplied. The upper triangular portion of each A_i will not be touched. Note that the imaginary part of the diagonal elements are not accessed and are assumed to be 0.**lda**–**[in]**[int] specifies the leading dimension of each A_i. Must be at least max(1, n).**batchCount**–**[in]**[int] number of instances in the batch.



The `herBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasCherStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const float *alpha, const hipComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, hipComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, int batchCount)[#](#_CPPv425hipblasCherStridedBatched15hipblasHandle_t17hipblasFillMode_tiPKfPK10hipComplexi13hipblasStrideP10hipComplexi13hipblasStridei)

-
hipblasStatus_t hipblasZherStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const double *alpha, const hipDoubleComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, hipDoubleComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, int batchCount)[#](#_CPPv425hipblasZherStridedBatched15hipblasHandle_t17hipblasFillMode_tiPKdPK16hipDoubleComplexi13hipblasStrideP16hipDoubleComplexi13hipblasStridei) BLAS Level 2 API.

herStridedBatched performs the matrix-vector operations

where alpha is a real scalar, x_i is a vector, and A_i is an n by n Hermitian matrix, for i = 1, …, batchCount.A_i := A_i + alpha*x_i*x_i**H

Supported precisions in rocBLAS : c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] specifies whether the upper ‘HIPBLAS_FILL_MODE_UPPER’ or lower ‘HIPBLAS_FILL_MODE_LOWER’ HIPBLAS_FILL_MODE_UPPER: The upper triangular part of each A_i is supplied in A. HIPBLAS_FILL_MODE_LOWER: The lower triangular part of each A_i is supplied in A.**n**–**[in]**[int] the number of rows and columns of each matrix A_i, must be at least 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device pointer pointing to the first vector (x_1).**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**stridex**–**[in]**[hipblasStride] stride from the start of one vector (x_i) and the next one (x_i+1).**AP**–**[inout]**device array of device pointers storing the specified triangular portion of each Hermitian matrix A_i. Points to the first matrix (A_1). if uplo == HIPBLAS_FILL_MODE_UPPER: The upper triangular portion of each Hermitian matrix A_i is supplied. The lower triangular portion of each A_i will not be touched. if uplo == HIPBLAS_FILL_MODE_LOWER: The lower triangular portion of each Hermitian matrix A_i is supplied. The upper triangular portion of each A_i will not be touched. Note that the imaginary part of the diagonal elements are not accessed and are assumed to be 0.**lda**–**[in]**[int] specifies the leading dimension of each A_i.**strideA**–**[in]**[hipblasStride] stride from the start of one (A_i) and the next (A_i+1)**batchCount**–**[in]**[int] number of instances in the batch.



The `herStridedBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasCher2(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipComplex *alpha, const hipComplex *x, int incx, const hipComplex *y, int incy, hipComplex *AP, int lda)[#](#_CPPv412hipblasCher215hipblasHandle_t17hipblasFillMode_tiPK10hipComplexPK10hipComplexiPK10hipComplexiP10hipComplexi)

-
hipblasStatus_t hipblasZher2(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *x, int incx, const hipDoubleComplex *y, int incy, hipDoubleComplex *AP, int lda)[#](#_CPPv412hipblasZher215hipblasHandle_t17hipblasFillMode_tiPK16hipDoubleComplexPK16hipDoubleComplexiPK16hipDoubleComplexiP16hipDoubleComplexi) BLAS Level 2 API.

her2 performs the matrix-vector operations

where alpha is a complex scalar, x and y are vectors, and A is an n by n Hermitian matrix.A := A + alpha*x*y**H + conj(alpha)*y*x**H

Supported precisions in rocBLAS : c,z

Supported precisions in cuBLAS : c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] specifies whether the upper ‘HIPBLAS_FILL_MODE_UPPER’ or lower ‘HIPBLAS_FILL_MODE_LOWER’ HIPBLAS_FILL_MODE_UPPER: The upper triangular part of A is supplied. HIPBLAS_FILL_MODE_LOWER: The lower triangular part of A is supplied.**n**–**[in]**[int] the number of rows and columns of matrix A, must be at least 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[int] specifies the increment for the elements of x.**y**–**[in]**device pointer storing vector y.**incy**–**[in]**[int] specifies the increment for the elements of y.**AP**–**[inout]**device pointer storing the specified triangular portion of the Hermitian matrix A. Of size (lda, n). if uplo == HIPBLAS_FILL_MODE_UPPER: The upper triangular portion of the Hermitian matrix A is supplied. The lower triangular portion of A will not be touched. if uplo == HIPBLAS_FILL_MODE_LOWER: The lower triangular portion of the Hermitian matrix A is supplied. The upper triangular portion of A will not be touched. Note that the imaginary part of the diagonal elements are not accessed and are assumed to be 0.**lda**–**[in]**[int] specifies the leading dimension of A. Must be at least max(lda, 1).



The `her2`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasCher2Batched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipComplex *alpha, const hipComplex *const x[], int incx, const hipComplex *const y[], int incy, hipComplex *const AP[], int lda, int batchCount)[#](#_CPPv419hipblasCher2Batched15hipblasHandle_t17hipblasFillMode_tiPK10hipComplexA_PCK10hipComplexiA_PCK10hipComplexiA_PC10hipComplexii)

-
hipblasStatus_t hipblasZher2Batched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *const x[], int incx, const hipDoubleComplex *const y[], int incy, hipDoubleComplex *const AP[], int lda, int batchCount)[#](#_CPPv419hipblasZher2Batched15hipblasHandle_t17hipblasFillMode_tiPK16hipDoubleComplexA_PCK16hipDoubleComplexiA_PCK16hipDoubleComplexiA_PC16hipDoubleComplexii) BLAS Level 2 API.

her2Batched performs the matrix-vector operations

where alpha is a complex scalar, x_i and y_i are vectors, and A_i is an n by n Hermitian matrix for each batch in i = [1, batchCount].A_i := A_i + alpha*x_i*y_i**H + conj(alpha)*y_i*x_i**H

Supported precisions in rocBLAS : c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] specifies whether the upper ‘HIPBLAS_FILL_MODE_UPPER’ or lower ‘HIPBLAS_FILL_MODE_LOWER’ HIPBLAS_FILL_MODE_UPPER: The upper triangular part of each A_i is supplied. HIPBLAS_FILL_MODE_LOWER: The lower triangular part of each A_i is supplied.**n**–**[in]**[int] the number of rows and columns of each matrix A_i, must be at least 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[int] specifies the increment for the elements of x.**y**–**[in]**device array of device pointers storing each vector y_i.**incy**–**[in]**[int] specifies the increment for the elements of each y_i.**AP**–**[inout]**device array of device pointers storing the specified triangular portion of each Hermitian matrix A_i of size (lda, n). if uplo == HIPBLAS_FILL_MODE_UPPER: The upper triangular portion of each Hermitian matrix A_i is supplied. The lower triangular portion of each A_i will not be touched. if uplo == HIPBLAS_FILL_MODE_LOWER: The lower triangular portion of each Hermitian matrix A_i is supplied. The upper triangular portion of each A_i will not be touched. Note that the imaginary part of the diagonal elements are not accessed and are assumed to be 0.**lda**–**[in]**[int] specifies the leading dimension of each A_i. Must be at least max(lda, 1).**batchCount**–**[in]**[int] number of instances in the batch.



The `her2Batched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasCher2StridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipComplex *alpha, const hipComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const hipComplex *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, hipComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, int batchCount)[#](#_CPPv426hipblasCher2StridedBatched15hipblasHandle_t17hipblasFillMode_tiPK10hipComplexPK10hipComplexi13hipblasStridePK10hipComplexi13hipblasStrideP10hipComplexi13hipblasStridei)

-
hipblasStatus_t hipblasZher2StridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const hipDoubleComplex *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, hipDoubleComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, int batchCount)[#](#_CPPv426hipblasZher2StridedBatched15hipblasHandle_t17hipblasFillMode_tiPK16hipDoubleComplexPK16hipDoubleComplexi13hipblasStridePK16hipDoubleComplexi13hipblasStrideP16hipDoubleComplexi13hipblasStridei) BLAS Level 2 API.

her2StridedBatched performs the matrix-vector operations

where alpha is a complex scalar, x_i and y_i are vectors, and A_i is an n by n Hermitian matrix for each batch in i = [1, batchCount].A_i := A_i + alpha*x_i*y_i**H + conj(alpha)*y_i*x_i**H

Supported precisions in rocBLAS : c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] specifies whether the upper ‘HIPBLAS_FILL_MODE_UPPER’ or lower ‘HIPBLAS_FILL_MODE_LOWER’ HIPBLAS_FILL_MODE_UPPER: The upper triangular part of each A_i is supplied. HIPBLAS_FILL_MODE_LOWER: The lower triangular part of each A_i is supplied.**n**–**[in]**[int] the number of rows and columns of each matrix A_i, must be at least 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device pointer pointing to the first vector x_1.**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**stridex**–**[in]**[hipblasStride] specifies the stride between the beginning of one vector (x_i) and the next (x_i+1).**y**–**[in]**device pointer pointing to the first vector y_i.**incy**–**[in]**[int] specifies the increment for the elements of each y_i.**stridey**–**[in]**[hipblasStride] specifies the stride between the beginning of one vector (y_i) and the next (y_i+1).**AP**–**[inout]**device pointer pointing to the first matrix (A_1). Stores the specified triangular portion of each Hermitian matrix A_i. if uplo == HIPBLAS_FILL_MODE_UPPER: The upper triangular portion of each Hermitian matrix A_i is supplied. The lower triangular portion of each A_i will not be touched. if uplo == HIPBLAS_FILL_MODE_LOWER: The lower triangular portion of each Hermitian matrix A_i is supplied. The upper triangular portion of each A_i will not be touched. Note that the imaginary part of the diagonal elements are not accessed and are assumed to be 0.**lda**–**[in]**[int] specifies the leading dimension of each A_i. Must be at least max(lda, 1).**strideA**–**[in]**[hipblasStride] specifies the stride between the beginning of one matrix (A_i) and the next (A_i+1).**batchCount**–**[in]**[int] number of instances in the batch.



The `her2StridedBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasChpmv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipComplex *alpha, const hipComplex *AP, const hipComplex *x, int incx, const hipComplex *beta, hipComplex *y, int incy)[#](#_CPPv412hipblasChpmv15hipblasHandle_t17hipblasFillMode_tiPK10hipComplexPK10hipComplexPK10hipComplexiPK10hipComplexP10hipComplexi)

-
hipblasStatus_t hipblasZhpmv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *AP, const hipDoubleComplex *x, int incx, const hipDoubleComplex *beta, hipDoubleComplex *y, int incy)[#](#_CPPv412hipblasZhpmv15hipblasHandle_t17hipblasFillMode_tiPK16hipDoubleComplexPK16hipDoubleComplexPK16hipDoubleComplexiPK16hipDoubleComplexP16hipDoubleComplexi) BLAS Level 2 API.

hpmv performs the matrix-vector operation

where alpha and beta are scalars, x and y are n element vectors and A is an n by n Hermitian matrix, supplied in packed form (see description below).y := alpha*A*x + beta*y

Supported precisions in rocBLAS : c,z

Supported precisions in cuBLAS : c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: the upper triangular part of the Hermitian matrix A is supplied in AP. HIPBLAS_FILL_MODE_LOWER: the lower triangular part of the Hermitian matrix A is supplied in AP.**n**–**[in]**[int] the order of the matrix A, must be >= 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**AP**–**[in]**device pointer storing the packed version of the specified triangular portion of the Hermitian matrix A. Of at least size ((n * (n + 1)) / 2). if uplo == HIPBLAS_FILL_MODE_UPPER: The upper triangular portion of the Hermitian matrix A is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(0,1) AP(2) = A(1,1), etc. Ex: (HIPBLAS_FILL_MODE_UPPER; n = 3) (1, 0) (2, 1) (3, 2) (2,-1) (4, 0) (5,-1) –—> [(1,0), (2,1), (4,0), (3,2), (5,-1), (6,0)] (3,-2) (5, 1) (6, 0) if uplo == HIPBLAS_FILL_MODE_LOWER: The lower triangular portion of the Hermitian matrix A is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(1,0) AP(2) = A(2,1), etc. Ex: (HIPBLAS_FILL_MODE_LOWER; n = 3) (1, 0) (2, 1) (3, 2) (2,-1) (4, 0) (5,-1) –—> [(1,0), (2,-1), (3,-2), (4,0), (5,1), (6,0)] (3,-2) (5, 1) (6, 0) Note that the imaginary part of the diagonal elements are not accessed and are assumed to be 0.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[int] specifies the increment for the elements of x.**beta**–**[in]**device pointer or host pointer to scalar beta.**y**–**[inout]**device pointer storing vector y.**incy**–**[in]**[int] specifies the increment for the elements of y.



The `hpmv`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasChpmvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipComplex *alpha, const hipComplex *const AP[], const hipComplex *const x[], int incx, const hipComplex *beta, hipComplex *const y[], int incy, int batchCount)[#](#_CPPv419hipblasChpmvBatched15hipblasHandle_t17hipblasFillMode_tiPK10hipComplexA_PCK10hipComplexA_PCK10hipComplexiPK10hipComplexA_PC10hipComplexii)

-
hipblasStatus_t hipblasZhpmvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *const AP[], const hipDoubleComplex *const x[], int incx, const hipDoubleComplex *beta, hipDoubleComplex *const y[], int incy, int batchCount)[#](#_CPPv419hipblasZhpmvBatched15hipblasHandle_t17hipblasFillMode_tiPK16hipDoubleComplexA_PCK16hipDoubleComplexA_PCK16hipDoubleComplexiPK16hipDoubleComplexA_PC16hipDoubleComplexii) BLAS Level 2 API.

hpmvBatched performs the matrix-vector operation

where alpha and beta are scalars, x_i and y_i are n element vectors and A_i is an n by n Hermitian matrix, supplied in packed form (see description below), for each batch in i = [1, batchCount].y_i := alpha*A_i*x_i + beta*y_i

Supported precisions in rocBLAS : c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: the upper triangular part of each Hermitian matrix A_i is supplied in AP. HIPBLAS_FILL_MODE_LOWER: the lower triangular part of each Hermitian matrix A_i is supplied in AP.**n**–**[in]**[int] the order of each matrix A_i.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**AP**–**[in]**device pointer of device pointers storing the packed version of the specified triangular portion of each Hermitian matrix A_i. Each A_i is of at least size ((n * (n + 1)) / 2). if uplo == HIPBLAS_FILL_MODE_UPPER: The upper triangular portion of each Hermitian matrix A_i is supplied. The matrix is compacted so that each AP_i contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(0,1) AP(2) = A(1,1), etc. Ex: (HIPBLAS_FILL_MODE_UPPER; n = 3) (1, 0) (2, 1) (3, 2) (2,-1) (4, 0) (5,-1) –—> [(1,0), (2,1), (4,0), (3,2), (5,-1), (6,0)] (3,-2) (5, 1) (6, 0) if uplo == HIPBLAS_FILL_MODE_LOWER: The lower triangular portion of each Hermitian matrix A_i is supplied. The matrix is compacted so that each AP_i contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(1,0) AP(2) = A(2,1), etc. Ex: (HIPBLAS_FILL_MODE_LOWER; n = 3) (1, 0) (2, 1) (3, 2) (2,-1) (4, 0) (5,-1) –—> [(1,0), (2,-1), (3,-2), (4,0), (5,1), (6,0)] (3,-2) (5, 1) (6, 0) Note that the imaginary part of the diagonal elements are not accessed and are assumed to be 0.**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**beta**–**[in]**device pointer or host pointer to scalar beta.**y**–**[inout]**device array of device pointers storing each vector y_i.**incy**–**[in]**[int] specifies the increment for the elements of y.**batchCount**–**[in]**[int] number of instances in the batch.



The `hpmvBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasChpmvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipComplex *alpha, const hipComplex *AP,[hipblasStride](#_CPPv413hipblasStride)strideA, const hipComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const hipComplex *beta, hipComplex *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount)[#](#_CPPv426hipblasChpmvStridedBatched15hipblasHandle_t17hipblasFillMode_tiPK10hipComplexPK10hipComplex13hipblasStridePK10hipComplexi13hipblasStridePK10hipComplexP10hipComplexi13hipblasStridei)

-
hipblasStatus_t hipblasZhpmvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *AP,[hipblasStride](#_CPPv413hipblasStride)strideA, const hipDoubleComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const hipDoubleComplex *beta, hipDoubleComplex *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount)[#](#_CPPv426hipblasZhpmvStridedBatched15hipblasHandle_t17hipblasFillMode_tiPK16hipDoubleComplexPK16hipDoubleComplex13hipblasStridePK16hipDoubleComplexi13hipblasStridePK16hipDoubleComplexP16hipDoubleComplexi13hipblasStridei) BLAS Level 2 API.

hpmvStridedBatched performs the matrix-vector operation

where alpha and beta are scalars, x_i and y_i are n element vectors and A_i is an n by n Hermitian matrix, supplied in packed form (see description below), for each batch in i = [1, batchCount].y_i := alpha*A_i*x_i + beta*y_i

Supported precisions in rocBLAS : c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: the upper triangular part of each Hermitian matrix A_i is supplied in AP. HIPBLAS_FILL_MODE_LOWER: the lower triangular part of each Hermitian matrix A_i is supplied in AP.**n**–**[in]**[int] the order of each matrix A_i.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**AP**–**[in]**device pointer pointing to the beginning of the first matrix (AP_1). Stores the packed version of the specified triangular portion of each Hermitian matrix AP_i of size ((n * (n + 1)) / 2). if uplo == HIPBLAS_FILL_MODE_UPPER: The upper triangular portion of each Hermitian matrix A_i is supplied. The matrix is compacted so that each AP_i contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(0,1) AP(2) = A(1,1), etc. Ex: (HIPBLAS_FILL_MODE_UPPER; n = 3) (1, 0) (2, 1) (3, 2) (2,-1) (4, 0) (5,-1) –—> [(1,0), (2,1), (4,0), (3,2), (5,-1), (6,0)] (3,-2) (5, 1) (6, 0) if uplo == HIPBLAS_FILL_MODE_LOWER: The lower triangular portion of each Hermitian matrix A_i is supplied. The matrix is compacted so that each AP_i contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(1,0) AP(2) = A(2,1), etc. Ex: (HIPBLAS_FILL_MODE_LOWER; n = 3) (1, 0) (2, 1) (3, 2) (2,-1) (4, 0) (5,-1) –—> [(1,0), (2,-1), (3,-2), (4,0), (5,1), (6,0)] (3,-2) (5, 1) (6, 0) Note that the imaginary part of the diagonal elements are not accessed and are assumed to be 0.**strideA**–**[in]**[hipblasStride] stride from the start of one matrix (AP_i) and the next one (AP_i+1).**x**–**[in]**device array pointing to the beginning of the first vector (x_1).**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**stridex**–**[in]**[hipblasStride] stride from the start of one vector (x_i) and the next one (x_i+1).**beta**–**[in]**device pointer or host pointer to scalar beta.**y**–**[inout]**device array pointing to the beginning of the first vector (y_1).**incy**–**[in]**[int] specifies the increment for the elements of y.**stridey**–**[in]**[hipblasStride] stride from the start of one vector (y_i) and the next one (y_i+1).**batchCount**–**[in]**[int] number of instances in the batch.



The `hpmvStridedBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasChpr(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const float *alpha, const hipComplex *x, int incx, hipComplex *AP)[#](#_CPPv411hipblasChpr15hipblasHandle_t17hipblasFillMode_tiPKfPK10hipComplexiP10hipComplex)

-
hipblasStatus_t hipblasZhpr(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const double *alpha, const hipDoubleComplex *x, int incx, hipDoubleComplex *AP)[#](#_CPPv411hipblasZhpr15hipblasHandle_t17hipblasFillMode_tiPKdPK16hipDoubleComplexiP16hipDoubleComplex) BLAS Level 2 API.

hpr performs the matrix-vector operations

where alpha is a real scalar, x is a vector, and A is an n by n Hermitian matrix, supplied in packed form.A := A + alpha*x*x**H

Supported precisions in rocBLAS : c,z

Supported precisions in cuBLAS : c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] specifies whether the upper ‘HIPBLAS_FILL_MODE_UPPER’ or lower ‘HIPBLAS_FILL_MODE_LOWER’ HIPBLAS_FILL_MODE_UPPER: The upper triangular part of A is supplied in AP. HIPBLAS_FILL_MODE_LOWER: The lower triangular part of A is supplied in AP.**n**–**[in]**[int] the number of rows and columns of matrix A, must be at least 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[int] specifies the increment for the elements of x.**AP**–**[inout]**device pointer storing the packed version of the specified triangular portion of the Hermitian matrix A. Of at least size ((n * (n + 1)) / 2). if uplo == HIPBLAS_FILL_MODE_UPPER: The upper triangular portion of the Hermitian matrix A is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(0,1) AP(2) = A(1,1), etc. Ex: (HIPBLAS_FILL_MODE_UPPER; n = 3) (1, 0) (2, 1) (4,9) (2,-1) (3, 0) (5,3) –—> [(1,0), (2,1), (3,0), (4,9), (5,3), (6,0)] (4,-9) (5,-3) (6,0) if uplo == HIPBLAS_FILL_MODE_LOWER: The lower triangular portion of the Hermitian matrix A is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(1,0) AP(2) = A(2,1), etc. Ex: (HIPBLAS_FILL_MODE_LOWER; n = 3) (1, 0) (2, 1) (4,9) (2,-1) (3, 0) (5,3) –—> [(1,0), (2,-1), (4,-9), (3,0), (5,-3), (6,0)] (4,-9) (5,-3) (6,0) Note that the imaginary part of the diagonal elements are not accessed and are assumed to be 0.



The `hpr`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasChprBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const float *alpha, const hipComplex *const x[], int incx, hipComplex *const AP[], int batchCount)[#](#_CPPv418hipblasChprBatched15hipblasHandle_t17hipblasFillMode_tiPKfA_PCK10hipComplexiA_PC10hipComplexi)

-
hipblasStatus_t hipblasZhprBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const double *alpha, const hipDoubleComplex *const x[], int incx, hipDoubleComplex *const AP[], int batchCount)[#](#_CPPv418hipblasZhprBatched15hipblasHandle_t17hipblasFillMode_tiPKdA_PCK16hipDoubleComplexiA_PC16hipDoubleComplexi) BLAS Level 2 API.

hprBatched performs the matrix-vector operations

where alpha is a real scalar, x_i is a vector, and A_i is an n by n symmetric matrix, supplied in packed form, for i = 1, …, batchCount.A_i := A_i + alpha*x_i*x_i**H

Supported precisions in rocBLAS : c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] specifies whether the upper ‘HIPBLAS_FILL_MODE_UPPER’ or lower ‘HIPBLAS_FILL_MODE_LOWER’ HIPBLAS_FILL_MODE_UPPER: The upper triangular part of each A_i is supplied in AP. HIPBLAS_FILL_MODE_LOWER: The lower triangular part of each A_i is supplied in AP.**n**–**[in]**[int] the number of rows and columns of each matrix A_i, must be at least 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**AP**–**[inout]**device array of device pointers storing the packed version of the specified triangular portion of each Hermitian matrix A_i of at least size ((n * (n + 1)) / 2). Array is of at least size batchCount. if uplo == HIPBLAS_FILL_MODE_UPPER: The upper triangular portion of each Hermitian matrix A_i is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(0,1) AP(2) = A(1,1), etc. Ex: (HIPBLAS_FILL_MODE_UPPER; n = 3) (1, 0) (2, 1) (4,9) (2,-1) (3, 0) (5,3) –—> [(1,0), (2,1), (3,0), (4,9), (5,3), (6,0)] (4,-9) (5,-3) (6,0) if uplo == HIPBLAS_FILL_MODE_LOWER: The lower triangular portion of each Hermitian matrix A_i is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(1,0) AP(2) = A(2,1), etc. Ex: (HIPBLAS_FILL_MODE_LOWER; n = 3) (1, 0) (2, 1) (4,9) (2,-1) (3, 0) (5,3) –—> [(1,0), (2,-1), (4,-9), (3,0), (5,-3), (6,0)] (4,-9) (5,-3) (6,0) Note that the imaginary part of the diagonal elements are not accessed and are assumed to be 0.**batchCount**–**[in]**[int] number of instances in the batch.



The `hprBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasChprStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const float *alpha, const hipComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, hipComplex *AP,[hipblasStride](#_CPPv413hipblasStride)strideA, int batchCount)[#](#_CPPv425hipblasChprStridedBatched15hipblasHandle_t17hipblasFillMode_tiPKfPK10hipComplexi13hipblasStrideP10hipComplex13hipblasStridei)

-
hipblasStatus_t hipblasZhprStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const double *alpha, const hipDoubleComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, hipDoubleComplex *AP,[hipblasStride](#_CPPv413hipblasStride)strideA, int batchCount)[#](#_CPPv425hipblasZhprStridedBatched15hipblasHandle_t17hipblasFillMode_tiPKdPK16hipDoubleComplexi13hipblasStrideP16hipDoubleComplex13hipblasStridei) BLAS Level 2 API.

hprStridedBatched performs the matrix-vector operations

where alpha is a real scalar, x_i is a vector, and A_i is an n by n symmetric matrix, supplied in packed form, for i = 1, …, batchCount.A_i := A_i + alpha*x_i*x_i**H

Supported precisions in rocBLAS : c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] specifies whether the upper ‘HIPBLAS_FILL_MODE_UPPER’ or lower ‘HIPBLAS_FILL_MODE_LOWER’ HIPBLAS_FILL_MODE_UPPER: The upper triangular part of each A_i is supplied in AP. HIPBLAS_FILL_MODE_LOWER: The lower triangular part of each A_i is supplied in AP.**n**–**[in]**[int] the number of rows and columns of each matrix A_i, must be at least 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device pointer pointing to the first vector (x_1).**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**stridex**–**[in]**[hipblasStride] stride from the start of one vector (x_i) and the next one (x_i+1).**AP**–**[inout]**device array of device pointers storing the packed version of the specified triangular portion of each Hermitian matrix A_i. Points to the first matrix (A_1). if uplo == HIPBLAS_FILL_MODE_UPPER: The upper triangular portion of each Hermitian matrix A_i is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(0,1) AP(2) = A(1,1), etc. Ex: (HIPBLAS_FILL_MODE_UPPER; n = 3) (1, 0) (2, 1) (4,9) (2,-1) (3, 0) (5,3) –—> [(1,0), (2,1), (3,0), (4,9), (5,3), (6,0)] (4,-9) (5,-3) (6,0) if uplo == HIPBLAS_FILL_MODE_LOWER: The lower triangular portion of each Hermitian matrix A_i is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(1,0) AP(2) = A(2,1), etc. Ex: (HIPBLAS_FILL_MODE_LOWER; n = 3) (1, 0) (2, 1) (4,9) (2,-1) (3, 0) (5,3) –—> [(1,0), (2,-1), (4,-9), (3,0), (5,-3), (6,0)] (4,-9) (5,-3) (6,0) Note that the imaginary part of the diagonal elements are not accessed and are assumed to be 0.**strideA**–**[in]**[hipblasStride] stride from the start of one (A_i) and the next (A_i+1)**batchCount**–**[in]**[int] number of instances in the batch.



The `hprStridedBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasChpr2(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipComplex *alpha, const hipComplex *x, int incx, const hipComplex *y, int incy, hipComplex *AP)[#](#_CPPv412hipblasChpr215hipblasHandle_t17hipblasFillMode_tiPK10hipComplexPK10hipComplexiPK10hipComplexiP10hipComplex)

-
hipblasStatus_t hipblasZhpr2(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *x, int incx, const hipDoubleComplex *y, int incy, hipDoubleComplex *AP)[#](#_CPPv412hipblasZhpr215hipblasHandle_t17hipblasFillMode_tiPK16hipDoubleComplexPK16hipDoubleComplexiPK16hipDoubleComplexiP16hipDoubleComplex) BLAS Level 2 API.

hpr2 performs the matrix-vector operations

where alpha is a complex scalar, x and y are vectors, and A is an n by n Hermitian matrix, supplied in packed form.A := A + alpha*x*y**H + conj(alpha)*y*x**H

Supported precisions in rocBLAS : c,z

Supported precisions in cuBLAS : c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] specifies whether the upper ‘HIPBLAS_FILL_MODE_UPPER’ or lower ‘HIPBLAS_FILL_MODE_LOWER’ HIPBLAS_FILL_MODE_UPPER: The upper triangular part of A is supplied in AP. HIPBLAS_FILL_MODE_LOWER: The lower triangular part of A is supplied in AP.**n**–**[in]**[int] the number of rows and columns of matrix A, must be at least 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[int] specifies the increment for the elements of x.**y**–**[in]**device pointer storing vector y.**incy**–**[in]**[int] specifies the increment for the elements of y.**AP**–**[inout]**device pointer storing the packed version of the specified triangular portion of the Hermitian matrix A. Of at least size ((n * (n + 1)) / 2). if uplo == HIPBLAS_FILL_MODE_UPPER: The upper triangular portion of the Hermitian matrix A is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(0,1) AP(2) = A(1,1), etc. Ex: (HIPBLAS_FILL_MODE_UPPER; n = 3) (1, 0) (2, 1) (4,9) (2,-1) (3, 0) (5,3) –—> [(1,0), (2,1), (3,0), (4,9), (5,3), (6,0)] (4,-9) (5,-3) (6,0) if uplo == HIPBLAS_FILL_MODE_LOWER: The lower triangular portion of the Hermitian matrix A is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(1,0) AP(2) = A(2,1), etc. Ex: (HIPBLAS_FILL_MODE_LOWER; n = 3) (1, 0) (2, 1) (4,9) (2,-1) (3, 0) (5,3) –—> [(1,0), (2,-1), (4,-9), (3,0), (5,-3), (6,0)] (4,-9) (5,-3) (6,0) Note that the imaginary part of the diagonal elements are not accessed and are assumed to be 0.



The `hpr2`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasChpr2Batched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipComplex *alpha, const hipComplex *const x[], int incx, const hipComplex *const y[], int incy, hipComplex *const AP[], int batchCount)[#](#_CPPv419hipblasChpr2Batched15hipblasHandle_t17hipblasFillMode_tiPK10hipComplexA_PCK10hipComplexiA_PCK10hipComplexiA_PC10hipComplexi)

-
hipblasStatus_t hipblasZhpr2Batched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *const x[], int incx, const hipDoubleComplex *const y[], int incy, hipDoubleComplex *const AP[], int batchCount)[#](#_CPPv419hipblasZhpr2Batched15hipblasHandle_t17hipblasFillMode_tiPK16hipDoubleComplexA_PCK16hipDoubleComplexiA_PCK16hipDoubleComplexiA_PC16hipDoubleComplexi) BLAS Level 2 API.

hpr2Batched performs the matrix-vector operations

where alpha is a complex scalar, x_i and y_i are vectors, and A_i is an n by n symmetric matrix, supplied in packed form, for i = 1, …, batchCount.A_i := A_i + alpha*x_i*y_i**H + conj(alpha)*y_i*x_i**H

Supported precisions in rocBLAS : c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] specifies whether the upper ‘HIPBLAS_FILL_MODE_UPPER’ or lower ‘HIPBLAS_FILL_MODE_LOWER’ HIPBLAS_FILL_MODE_UPPER: The upper triangular part of each A_i is supplied in AP. HIPBLAS_FILL_MODE_LOWER: The lower triangular part of each A_i is supplied in AP.**n**–**[in]**[int] the number of rows and columns of each matrix A_i, must be at least 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**y**–**[in]**device array of device pointers storing each vector y_i.**incy**–**[in]**[int] specifies the increment for the elements of each y_i.**AP**–**[inout]**device array of device pointers storing the packed version of the specified triangular portion of each Hermitian matrix A_i of at least size ((n * (n + 1)) / 2). Array is of at least size batchCount. if uplo == HIPBLAS_FILL_MODE_UPPER: The upper triangular portion of each Hermitian matrix A_i is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(0,1) AP(2) = A(1,1), etc. Ex: (HIPBLAS_FILL_MODE_UPPER; n = 3) (1, 0) (2, 1) (4,9) (2,-1) (3, 0) (5,3) –—> [(1,0), (2,1), (3,0), (4,9), (5,3), (6,0)] (4,-9) (5,-3) (6,0) if uplo == HIPBLAS_FILL_MODE_LOWER: The lower triangular portion of each Hermitian matrix A_i is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(1,0) AP(2) = A(2,1), etc. Ex: (HIPBLAS_FILL_MODE_LOWER; n = 3) (1, 0) (2, 1) (4,9) (2,-1) (3, 0) (5,3) –—> [(1,0), (2,-1), (4,-9), (3,0), (5,-3), (6,0)] (4,-9) (5,-3) (6,0) Note that the imaginary part of the diagonal elements are not accessed and are assumed to be 0.**batchCount**–**[in]**[int] number of instances in the batch.



The `hpr2Batched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasChpr2StridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipComplex *alpha, const hipComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const hipComplex *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, hipComplex *AP,[hipblasStride](#_CPPv413hipblasStride)strideA, int batchCount)[#](#_CPPv426hipblasChpr2StridedBatched15hipblasHandle_t17hipblasFillMode_tiPK10hipComplexPK10hipComplexi13hipblasStridePK10hipComplexi13hipblasStrideP10hipComplex13hipblasStridei)

-
hipblasStatus_t hipblasZhpr2StridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const hipDoubleComplex *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, hipDoubleComplex *AP,[hipblasStride](#_CPPv413hipblasStride)strideA, int batchCount)[#](#_CPPv426hipblasZhpr2StridedBatched15hipblasHandle_t17hipblasFillMode_tiPK16hipDoubleComplexPK16hipDoubleComplexi13hipblasStridePK16hipDoubleComplexi13hipblasStrideP16hipDoubleComplex13hipblasStridei) BLAS Level 2 API.

hpr2StridedBatched performs the matrix-vector operations

where alpha is a complex scalar, x_i and y_i are vectors, and A_i is an n by n symmetric matrix, supplied in packed form, for i = 1, …, batchCount.A_i := A_i + alpha*x_i*y_i**H + conj(alpha)*y_i*x_i**H

Supported precisions in rocBLAS : c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] specifies whether the upper ‘HIPBLAS_FILL_MODE_UPPER’ or lower ‘HIPBLAS_FILL_MODE_LOWER’ HIPBLAS_FILL_MODE_UPPER: The upper triangular part of each A_i is supplied in AP. HIPBLAS_FILL_MODE_LOWER: The lower triangular part of each A_i is supplied in AP.**n**–**[in]**[int] the number of rows and columns of each matrix A_i, must be at least 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device pointer pointing to the first vector (x_1).**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**stridex**–**[in]**[hipblasStride] stride from the start of one vector (x_i) and the next one (x_i+1).**y**–**[in]**device pointer pointing to the first vector (y_1).**incy**–**[in]**[int] specifies the increment for the elements of each y_i.**stridey**–**[in]**[hipblasStride] stride from the start of one vector (y_i) and the next one (y_i+1).**AP**–**[inout]**device array of device pointers storing the packed version of the specified triangular portion of each Hermitian matrix A_i. Points to the first matrix (A_1). if uplo == HIPBLAS_FILL_MODE_UPPER: The upper triangular portion of each Hermitian matrix A_i is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(0,1) AP(2) = A(1,1), etc. Ex: (HIPBLAS_FILL_MODE_UPPER; n = 3) (1, 0) (2, 1) (4,9) (2,-1) (3, 0) (5,3) –—> [(1,0), (2,1), (3,0), (4,9), (5,3), (6,0)] (4,-9) (5,-3) (6,0) if uplo == HIPBLAS_FILL_MODE_LOWER: The lower triangular portion of each Hermitian matrix A_i is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(1,0) AP(2) = A(2,1), etc. Ex: (HIPBLAS_FILL_MODE_LOWER; n = 3) (1, 0) (2, 1) (4,9) (2,-1) (3, 0) (5,3) –—> [(1,0), (2,-1), (4,-9), (3,0), (5,-3), (6,0)] (4,-9) (5,-3) (6,0) Note that the imaginary part of the diagonal elements are not accessed and are assumed to be 0.**strideA**–**[in]**[hipblasStride] stride from the start of one (A_i) and the next (A_i+1)**batchCount**–**[in]**[int] number of instances in the batch.



The `hpr2StridedBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSsbmv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, int k, const float *alpha, const float *AP, int lda, const float *x, int incx, const float *beta, float *y, int incy)[#](#_CPPv412hipblasSsbmv15hipblasHandle_t17hipblasFillMode_tiiPKfPKfiPKfiPKfPfi)

-
hipblasStatus_t hipblasDsbmv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, int k, const double *alpha, const double *AP, int lda, const double *x, int incx, const double *beta, double *y, int incy)[#](#_CPPv412hipblasDsbmv15hipblasHandle_t17hipblasFillMode_tiiPKdPKdiPKdiPKdPdi) BLAS Level 2 API.

sbmv performs the matrix-vector operation:

where alpha and beta are scalars, x and y are n element vectors and A should contain an upper or lower triangular n by n symmetric banded matrix.y := alpha*A*x + beta*y,

Supported precisions in rocBLAS : s,d

Supported precisions in cuBLAS : s,d


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] specifies whether the upper ‘HIPBLAS_FILL_MODE_UPPER’ or lower ‘HIPBLAS_FILL_MODE_LOWER’ if HIPBLAS_FILL_MODE_UPPER, the lower part of A is not referenced if HIPBLAS_FILL_MODE_LOWER, the upper part of A is not referenced**n**–**[in]**[int]**k**–**[in]**[int] specifies the number of sub- and super-diagonals**alpha**–**[in]**specifies the scalar alpha**AP**–**[in]**pointer storing matrix A on the GPU**lda**–**[in]**[int] specifies the leading dimension of matrix A**x**–**[in]**pointer storing vector x on the GPU**incx**–**[in]**[int] specifies the increment for the elements of x**beta**–**[in]**specifies the scalar beta**y**–**[out]**pointer storing vector y on the GPU**incy**–**[in]**[int] specifies the increment for the elements of y



The `sbmv`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSsbmvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, int k, const float *alpha, const float *const AP[], int lda, const float *const x[], int incx, const float *beta, float *const y[], int incy, int batchCount)[#](#_CPPv419hipblasSsbmvBatched15hipblasHandle_t17hipblasFillMode_tiiPKfA_PCKfiA_PCKfiPKfA_PCfii)

-
hipblasStatus_t hipblasDsbmvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, int k, const double *alpha, const double *const AP[], int lda, const double *const x[], int incx, const double *beta, double *const y[], int incy, int batchCount)[#](#_CPPv419hipblasDsbmvBatched15hipblasHandle_t17hipblasFillMode_tiiPKdA_PCKdiA_PCKdiPKdA_PCdii) BLAS Level 2 API.

sbmvBatched performs the matrix-vector operation:

where (A_i, x_i, y_i) is the i-th instance of the batch. alpha and beta are scalars, x_i and y_i are vectors and A_i is an n by n symmetric banded matrix, for i = 1, …, batchCount. A should contain an upper or lower triangular n by n symmetric banded matrix.y_i := alpha*A_i*x_i + beta*y_i,

Supported precisions in rocBLAS : s,d

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue**uplo**–**[in]**[hipblasFillMode_t] specifies whether the upper ‘HIPBLAS_FILL_MODE_UPPER’ or lower ‘HIPBLAS_FILL_MODE_LOWER’ if HIPBLAS_FILL_MODE_UPPER, the lower part of A is not referenced if HIPBLAS_FILL_MODE_LOWER, the upper part of A is not referenced**n**–**[in]**[int] number of rows and columns of each matrix A_i**k**–**[in]**[int] specifies the number of sub- and super-diagonals**alpha**–**[in]**device pointer or host pointer to scalar alpha**AP**–**[in]**device array of device pointers storing each matrix A_i**lda**–**[in]**[int] specifies the leading dimension of each matrix A_i**x**–**[in]**device array of device pointers storing each vector x_i**incx**–**[in]**[int] specifies the increment for the elements of each vector x_i**beta**–**[in]**device pointer or host pointer to scalar beta**y**–**[out]**device array of device pointers storing each vector y_i**incy**–**[in]**[int] specifies the increment for the elements of each vector y_i**batchCount**–**[in]**[int] number of instances in the batch



The `sbmvBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSsbmvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, int k, const float *alpha, const float *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const float *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const float *beta, float *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount)[#](#_CPPv426hipblasSsbmvStridedBatched15hipblasHandle_t17hipblasFillMode_tiiPKfPKfi13hipblasStridePKfi13hipblasStridePKfPfi13hipblasStridei)

-
hipblasStatus_t hipblasDsbmvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, int k, const double *alpha, const double *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const double *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const double *beta, double *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount)[#](#_CPPv426hipblasDsbmvStridedBatched15hipblasHandle_t17hipblasFillMode_tiiPKdPKdi13hipblasStridePKdi13hipblasStridePKdPdi13hipblasStridei) BLAS Level 2 API.

sbmvStridedBatched performs the matrix-vector operation:

where (A_i, x_i, y_i) is the i-th instance of the batch. alpha and beta are scalars, x_i and y_i are vectors and A_i is an n by n symmetric banded matrix, for i = 1, …, batchCount. A should contain an upper or lower triangular n by n symmetric banded matrix.y_i := alpha*A_i*x_i + beta*y_i,

Supported precisions in rocBLAS : s,d

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue**uplo**–**[in]**[hipblasFillMode_t] specifies whether the upper ‘HIPBLAS_FILL_MODE_UPPER’ or lower ‘HIPBLAS_FILL_MODE_LOWER’ if HIPBLAS_FILL_MODE_UPPER, the lower part of A is not referenced if HIPBLAS_FILL_MODE_LOWER, the upper part of A is not referenced**n**–**[in]**[int] number of rows and columns of each matrix A_i**k**–**[in]**[int] specifies the number of sub- and super-diagonals**alpha**–**[in]**device pointer or host pointer to scalar alpha**AP**–**[in]**Device pointer to the first matrix A_1 on the GPU**lda**–**[in]**[int] specifies the leading dimension of each matrix A_i**strideA**–**[in]**[hipblasStride] stride from the start of one matrix (A_i) and the next one (A_i+1)**x**–**[in]**Device pointer to the first vector x_1 on the GPU**incx**–**[in]**[int] specifies the increment for the elements of each vector x_i**stridex**–**[in]**[hipblasStride] stride from the start of one vector (x_i) and the next one (x_i+1). There are no restrictions placed on stridex, however the user should take care to ensure that stridex is of appropriate size. This typically means stridex >= n * incx. stridex should be non zero.**beta**–**[in]**device pointer or host pointer to scalar beta**y**–**[out]**Device pointer to the first vector y_1 on the GPU**incy**–**[in]**[int] specifies the increment for the elements of each vector y_i**stridey**–**[in]**[hipblasStride] stride from the start of one vector (y_i) and the next one (y_i+1). There are no restrictions placed on stridey, however the user should take care to ensure that stridey is of appropriate size. This typically means stridey >= n * incy. stridey should be non zero.**batchCount**–**[in]**[int] number of instances in the batch



The `sbmvStridedBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSspmv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const float *alpha, const float *AP, const float *x, int incx, const float *beta, float *y, int incy)[#](#_CPPv412hipblasSspmv15hipblasHandle_t17hipblasFillMode_tiPKfPKfPKfiPKfPfi)

-
hipblasStatus_t hipblasDspmv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const double *alpha, const double *AP, const double *x, int incx, const double *beta, double *y, int incy)[#](#_CPPv412hipblasDspmv15hipblasHandle_t17hipblasFillMode_tiPKdPKdPKdiPKdPdi) BLAS Level 2 API.

spmv performs the matrix-vector operation:

where alpha and beta are scalars, x and y are n element vectors and A should contain an upper or lower triangular n by n packed symmetric matrix.y := alpha*A*x + beta*y,

Supported precisions in rocBLAS : s,d

Supported precisions in cuBLAS : s,d


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] specifies whether the upper ‘HIPBLAS_FILL_MODE_UPPER’ or lower ‘HIPBLAS_FILL_MODE_LOWER’ if HIPBLAS_FILL_MODE_UPPER, the lower part of A is not referenced if HIPBLAS_FILL_MODE_LOWER, the upper part of A is not referenced**n**–**[in]**[int]**alpha**–**[in]**specifies the scalar alpha**AP**–**[in]**pointer storing matrix A on the GPU**x**–**[in]**pointer storing vector x on the GPU**incx**–**[in]**[int] specifies the increment for the elements of x**beta**–**[in]**specifies the scalar beta**y**–**[out]**pointer storing vector y on the GPU**incy**–**[in]**[int] specifies the increment for the elements of y



The `spmv`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSspmvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const float *alpha, const float *const AP[], const float *const x[], int incx, const float *beta, float *const y[], int incy, int batchCount)[#](#_CPPv419hipblasSspmvBatched15hipblasHandle_t17hipblasFillMode_tiPKfA_PCKfA_PCKfiPKfA_PCfii)

-
hipblasStatus_t hipblasDspmvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const double *alpha, const double *const AP[], const double *const x[], int incx, const double *beta, double *const y[], int incy, int batchCount)[#](#_CPPv419hipblasDspmvBatched15hipblasHandle_t17hipblasFillMode_tiPKdA_PCKdA_PCKdiPKdA_PCdii) BLAS Level 2 API.

spmvBatched performs the matrix-vector operation:

where (A_i, x_i, y_i) is the i-th instance of the batch. alpha and beta are scalars, x_i and y_i are vectors and A_i is an n by n symmetric matrix, for i = 1, …, batchCount. A should contain an upper or lower triangular n by n packed symmetric matrix.y_i := alpha*AP_i*x_i + beta*y_i,

Supported precisions in rocBLAS : s,d

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue**uplo**–**[in]**[hipblasFillMode_t] specifies whether the upper ‘HIPBLAS_FILL_MODE_UPPER’ or lower ‘HIPBLAS_FILL_MODE_LOWER’ if HIPBLAS_FILL_MODE_UPPER, the lower part of A is not referenced if HIPBLAS_FILL_MODE_LOWER, the upper part of A is not referenced**n**–**[in]**[int] number of rows and columns of each matrix A_i**alpha**–**[in]**device pointer or host pointer to scalar alpha**AP**–**[in]**device array of device pointers storing each matrix A_i**x**–**[in]**device array of device pointers storing each vector x_i**incx**–**[in]**[int] specifies the increment for the elements of each vector x_i**beta**–**[in]**device pointer or host pointer to scalar beta**y**–**[out]**device array of device pointers storing each vector y_i**incy**–**[in]**[int] specifies the increment for the elements of each vector y_i**batchCount**–**[in]**[int] number of instances in the batch



The `spmvBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSspmvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const float *alpha, const float *AP,[hipblasStride](#_CPPv413hipblasStride)strideA, const float *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const float *beta, float *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount)[#](#_CPPv426hipblasSspmvStridedBatched15hipblasHandle_t17hipblasFillMode_tiPKfPKf13hipblasStridePKfi13hipblasStridePKfPfi13hipblasStridei)

-
hipblasStatus_t hipblasDspmvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const double *alpha, const double *AP,[hipblasStride](#_CPPv413hipblasStride)strideA, const double *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const double *beta, double *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount)[#](#_CPPv426hipblasDspmvStridedBatched15hipblasHandle_t17hipblasFillMode_tiPKdPKd13hipblasStridePKdi13hipblasStridePKdPdi13hipblasStridei) BLAS Level 2 API.

spmvStridedBatched performs the matrix-vector operation:

where (A_i, x_i, y_i) is the i-th instance of the batch. alpha and beta are scalars, x_i and y_i are vectors and A_i is an n by n symmetric matrix, for i = 1, …, batchCount. A should contain an upper or lower triangular n by n packed symmetric matrix.y_i := alpha*A_i*x_i + beta*y_i,

Supported precisions in rocBLAS : s,d

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue**uplo**–**[in]**[hipblasFillMode_t] specifies whether the upper ‘HIPBLAS_FILL_MODE_UPPER’ or lower ‘HIPBLAS_FILL_MODE_LOWER’ if HIPBLAS_FILL_MODE_UPPER, the lower part of A is not referenced if HIPBLAS_FILL_MODE_LOWER, the upper part of A is not referenced**n**–**[in]**[int] number of rows and columns of each matrix A_i**alpha**–**[in]**device pointer or host pointer to scalar alpha**AP**–**[in]**Device pointer to the first matrix A_1 on the GPU**strideA**–**[in]**[hipblasStride] stride from the start of one matrix (A_i) and the next one (A_i+1)**x**–**[in]**Device pointer to the first vector x_1 on the GPU**incx**–**[in]**[int] specifies the increment for the elements of each vector x_i**stridex**–**[in]**[hipblasStride] stride from the start of one vector (x_i) and the next one (x_i+1). There are no restrictions placed on stridex, however the user should take care to ensure that stridex is of appropriate size. This typically means stridex >= n * incx. stridex should be non zero.**beta**–**[in]**device pointer or host pointer to scalar beta**y**–**[out]**Device pointer to the first vector y_1 on the GPU**incy**–**[in]**[int] specifies the increment for the elements of each vector y_i**stridey**–**[in]**[hipblasStride] stride from the start of one vector (y_i) and the next one (y_i+1). There are no restrictions placed on stridey, however the user should take care to ensure that stridey is of appropriate size. This typically means stridey >= n * incy. stridey should be non zero.**batchCount**–**[in]**[int] number of instances in the batch



The `spmvStridedBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSspr(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const float *alpha, const float *x, int incx, float *AP)[#](#_CPPv411hipblasSspr15hipblasHandle_t17hipblasFillMode_tiPKfPKfiPf)

-
hipblasStatus_t hipblasDspr(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const double *alpha, const double *x, int incx, double *AP)[#](#_CPPv411hipblasDspr15hipblasHandle_t17hipblasFillMode_tiPKdPKdiPd)

-
hipblasStatus_t hipblasCspr(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipComplex *alpha, const hipComplex *x, int incx, hipComplex *AP)[#](#_CPPv411hipblasCspr15hipblasHandle_t17hipblasFillMode_tiPK10hipComplexPK10hipComplexiP10hipComplex)

-
hipblasStatus_t hipblasZspr(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *x, int incx, hipDoubleComplex *AP)[#](#_CPPv411hipblasZspr15hipblasHandle_t17hipblasFillMode_tiPK16hipDoubleComplexPK16hipDoubleComplexiP16hipDoubleComplex) BLAS Level 2 API.

spr performs the matrix-vector operations

where alpha is a scalar, x is a vector, and A is an n by n symmetric matrix, supplied in packed form.A := A + alpha*x*x**T

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : s,d,c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] specifies whether the upper ‘HIPBLAS_FILL_MODE_UPPER’ or lower ‘HIPBLAS_FILL_MODE_LOWER’ HIPBLAS_FILL_MODE_UPPER: The upper triangular part of A is supplied in AP. HIPBLAS_FILL_MODE_LOWER: The lower triangular part of A is supplied in AP.**n**–**[in]**[int] the number of rows and columns of matrix A, must be at least 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[int] specifies the increment for the elements of x.**AP**–**[inout]**device pointer storing the packed version of the specified triangular portion of the symmetric matrix A. Of at least size ((n * (n + 1)) / 2). if uplo == HIPBLAS_FILL_MODE_UPPER: The upper triangular portion of the symmetric matrix A is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(0,1) AP(2) = A(1,1), etc. Ex: (HIPBLAS_FILL_MODE_UPPER; n = 4) 1 2 4 7 2 3 5 8 –—> [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] 4 5 6 9 7 8 9 0 if uplo == HIPBLAS_FILL_MODE_LOWER: The lower triangular portion of the symmetric matrix A is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(1,0) AP(2) = A(2,1), etc. Ex: (HIPBLAS_FILL_MODE_LOWER; n = 4) 1 2 3 4 2 5 6 7 –—> [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] 3 6 8 9 4 7 9 0



The `spr`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSsprBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const float *alpha, const float *const x[], int incx, float *const AP[], int batchCount)[#](#_CPPv418hipblasSsprBatched15hipblasHandle_t17hipblasFillMode_tiPKfA_PCKfiA_PCfi)

-
hipblasStatus_t hipblasDsprBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const double *alpha, const double *const x[], int incx, double *const AP[], int batchCount)[#](#_CPPv418hipblasDsprBatched15hipblasHandle_t17hipblasFillMode_tiPKdA_PCKdiA_PCdi)

-
hipblasStatus_t hipblasCsprBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipComplex *alpha, const hipComplex *const x[], int incx, hipComplex *const AP[], int batchCount)[#](#_CPPv418hipblasCsprBatched15hipblasHandle_t17hipblasFillMode_tiPK10hipComplexA_PCK10hipComplexiA_PC10hipComplexi)

-
hipblasStatus_t hipblasZsprBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *const x[], int incx, hipDoubleComplex *const AP[], int batchCount)[#](#_CPPv418hipblasZsprBatched15hipblasHandle_t17hipblasFillMode_tiPK16hipDoubleComplexA_PCK16hipDoubleComplexiA_PC16hipDoubleComplexi) BLAS Level 2 API.

sprBatched performs the matrix-vector operations

where alpha is a scalar, x_i is a vector, and A_i is an n by n symmetric matrix, supplied in packed form, for i = 1, …, batchCount.A_i := A_i + alpha*x_i*x_i**T

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] specifies whether the upper ‘HIPBLAS_FILL_MODE_UPPER’ or lower ‘HIPBLAS_FILL_MODE_LOWER’ HIPBLAS_FILL_MODE_UPPER: The upper triangular part of each A_i is supplied in AP. HIPBLAS_FILL_MODE_LOWER: The lower triangular part of each A_i is supplied in AP.**n**–**[in]**[int] the number of rows and columns of each matrix A_i, must be at least 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**AP**–**[inout]**device array of device pointers storing the packed version of the specified triangular portion of each symmetric matrix A_i of at least size ((n * (n + 1)) / 2). Array is of at least size batchCount. if uplo == HIPBLAS_FILL_MODE_UPPER: The upper triangular portion of each symmetric matrix A_i is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(0,1) AP(2) = A(1,1), etc. Ex: (HIPBLAS_FILL_MODE_UPPER; n = 4) 1 2 4 7 2 3 5 8 –—> [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] 4 5 6 9 7 8 9 0 if uplo == HIPBLAS_FILL_MODE_LOWER: The lower triangular portion of each symmetric matrix A_i is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(1,0) AP(2) = A(2,1), etc. Ex: (HIPBLAS_FILL_MODE_LOWER; n = 4) 1 2 3 4 2 5 6 7 –—> [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] 3 6 8 9 4 7 9 0**batchCount**–**[in]**[int] number of instances in the batch.



The `sprBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSsprStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const float *alpha, const float *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, float *AP,[hipblasStride](#_CPPv413hipblasStride)strideA, int batchCount)[#](#_CPPv425hipblasSsprStridedBatched15hipblasHandle_t17hipblasFillMode_tiPKfPKfi13hipblasStridePf13hipblasStridei)

-
hipblasStatus_t hipblasDsprStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const double *alpha, const double *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, double *AP,[hipblasStride](#_CPPv413hipblasStride)strideA, int batchCount)[#](#_CPPv425hipblasDsprStridedBatched15hipblasHandle_t17hipblasFillMode_tiPKdPKdi13hipblasStridePd13hipblasStridei)

-
hipblasStatus_t hipblasCsprStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipComplex *alpha, const hipComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, hipComplex *AP,[hipblasStride](#_CPPv413hipblasStride)strideA, int batchCount)[#](#_CPPv425hipblasCsprStridedBatched15hipblasHandle_t17hipblasFillMode_tiPK10hipComplexPK10hipComplexi13hipblasStrideP10hipComplex13hipblasStridei)

-
hipblasStatus_t hipblasZsprStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, hipDoubleComplex *AP,[hipblasStride](#_CPPv413hipblasStride)strideA, int batchCount)[#](#_CPPv425hipblasZsprStridedBatched15hipblasHandle_t17hipblasFillMode_tiPK16hipDoubleComplexPK16hipDoubleComplexi13hipblasStrideP16hipDoubleComplex13hipblasStridei) BLAS Level 2 API.

sprStridedBatched performs the matrix-vector operations

where alpha is a scalar, x_i is a vector, and A_i is an n by n symmetric matrix, supplied in packed form, for i = 1, …, batchCount.A_i := A_i + alpha*x_i*x_i**T

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] specifies whether the upper ‘HIPBLAS_FILL_MODE_UPPER’ or lower ‘HIPBLAS_FILL_MODE_LOWER’ HIPBLAS_FILL_MODE_UPPER: The upper triangular part of each A_i is supplied in AP. HIPBLAS_FILL_MODE_LOWER: The lower triangular part of each A_i is supplied in AP.**n**–**[in]**[int] the number of rows and columns of each matrix A_i, must be at least 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device pointer pointing to the first vector (x_1).**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**stridex**–**[in]**[hipblasStride] stride from the start of one vector (x_i) and the next one (x_i+1).**AP**–**[inout]**device pointer storing the packed version of the specified triangular portion of each symmetric matrix A_i. Points to the first A_1. if uplo == HIPBLAS_FILL_MODE_UPPER: The upper triangular portion of each symmetric matrix A_i is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(0,1) AP(2) = A(1,1), etc. Ex: (HIPBLAS_FILL_MODE_UPPER; n = 4) 1 2 4 7 2 3 5 8 –—> [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] 4 5 6 9 7 8 9 0 if uplo == HIPBLAS_FILL_MODE_LOWER: The lower triangular portion of each symmetric matrix A_i is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(1,0) AP(2) = A(2,1), etc. Ex: (HIPBLAS_FILL_MODE_LOWER; n = 4) 1 2 3 4 2 5 6 7 –—> [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] 3 6 8 9 4 7 9 0**strideA**–**[in]**[hipblasStride] stride from the start of one (A_i) and the next (A_i+1)**batchCount**–**[in]**[int] number of instances in the batch.



The `sprStridedBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSspr2(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const float *alpha, const float *x, int incx, const float *y, int incy, float *AP)[#](#_CPPv412hipblasSspr215hipblasHandle_t17hipblasFillMode_tiPKfPKfiPKfiPf)

-
hipblasStatus_t hipblasDspr2(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const double *alpha, const double *x, int incx, const double *y, int incy, double *AP)[#](#_CPPv412hipblasDspr215hipblasHandle_t17hipblasFillMode_tiPKdPKdiPKdiPd) BLAS Level 2 API.

spr2 performs the matrix-vector operation

where alpha is a scalar, x and y are vectors, and A is an n by n symmetric matrix, supplied in packed form.A := A + alpha*x*y**T + alpha*y*x**T

Supported precisions in rocBLAS : s,d

Supported precisions in cuBLAS : s,d


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] specifies whether the upper ‘HIPBLAS_FILL_MODE_UPPER’ or lower ‘HIPBLAS_FILL_MODE_LOWER’ HIPBLAS_FILL_MODE_UPPER: The upper triangular part of A is supplied in AP. HIPBLAS_FILL_MODE_LOWER: The lower triangular part of A is supplied in AP.**n**–**[in]**[int] the number of rows and columns of matrix A, must be at least 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[int] specifies the increment for the elements of x.**y**–**[in]**device pointer storing vector y.**incy**–**[in]**[int] specifies the increment for the elements of y.**AP**–**[inout]**device pointer storing the packed version of the specified triangular portion of the symmetric matrix A. Of at least size ((n * (n + 1)) / 2). if uplo == HIPBLAS_FILL_MODE_UPPER: The upper triangular portion of the symmetric matrix A is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(0,1) AP(2) = A(1,1), etc. Ex: (HIPBLAS_FILL_MODE_UPPER; n = 4) 1 2 4 7 2 3 5 8 –—> [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] 4 5 6 9 7 8 9 0 if uplo == HIPBLAS_FILL_MODE_LOWER: The lower triangular portion of the symmetric matrix A is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(1,0) AP(n) = A(2,1), etc. Ex: (HIPBLAS_FILL_MODE_LOWER; n = 4) 1 2 3 4 2 5 6 7 –—> [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] 3 6 8 9 4 7 9 0



The `spr2`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSspr2Batched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const float *alpha, const float *const x[], int incx, const float *const y[], int incy, float *const AP[], int batchCount)[#](#_CPPv419hipblasSspr2Batched15hipblasHandle_t17hipblasFillMode_tiPKfA_PCKfiA_PCKfiA_PCfi)

-
hipblasStatus_t hipblasDspr2Batched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const double *alpha, const double *const x[], int incx, const double *const y[], int incy, double *const AP[], int batchCount)[#](#_CPPv419hipblasDspr2Batched15hipblasHandle_t17hipblasFillMode_tiPKdA_PCKdiA_PCKdiA_PCdi) BLAS Level 2 API.

spr2Batched performs the matrix-vector operation

where alpha is a scalar, x_i and y_i are vectors, and A_i is an n by n symmetric matrix, supplied in packed form, for i = 1, …, batchCount.A_i := A_i + alpha*x_i*y_i**T + alpha*y_i*x_i**T

Supported precisions in rocBLAS : s,d

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] specifies whether the upper ‘HIPBLAS_FILL_MODE_UPPER’ or lower ‘HIPBLAS_FILL_MODE_LOWER’ HIPBLAS_FILL_MODE_UPPER: The upper triangular part of each A_i is supplied in AP. HIPBLAS_FILL_MODE_LOWER: The lower triangular part of each A_i is supplied in AP.**n**–**[in]**[int] the number of rows and columns of each matrix A_i, must be at least 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**y**–**[in]**device array of device pointers storing each vector y_i.**incy**–**[in]**[int] specifies the increment for the elements of each y_i.**AP**–**[inout]**device array of device pointers storing the packed version of the specified triangular portion of each symmetric matrix A_i of at least size ((n * (n + 1)) / 2). Array is of at least size batchCount. if uplo == HIPBLAS_FILL_MODE_UPPER: The upper triangular portion of each symmetric matrix A_i is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(0,1) AP(2) = A(1,1), etc. Ex: (HIPBLAS_FILL_MODE_UPPER; n = 4) 1 2 4 7 2 3 5 8 –—> [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] 4 5 6 9 7 8 9 0 if uplo == HIPBLAS_FILL_MODE_LOWER: The lower triangular portion of each symmetric matrix A_i is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(1,0) AP(n) = A(2,1), etc. Ex: (HIPBLAS_FILL_MODE_LOWER; n = 4) 1 2 3 4 2 5 6 7 –—> [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] 3 6 8 9 4 7 9 0**batchCount**–**[in]**[int] number of instances in the batch.



The `spr2Batched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSspr2StridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const float *alpha, const float *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const float *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, float *AP,[hipblasStride](#_CPPv413hipblasStride)strideA, int batchCount)[#](#_CPPv426hipblasSspr2StridedBatched15hipblasHandle_t17hipblasFillMode_tiPKfPKfi13hipblasStridePKfi13hipblasStridePf13hipblasStridei)

-
hipblasStatus_t hipblasDspr2StridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const double *alpha, const double *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const double *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, double *AP,[hipblasStride](#_CPPv413hipblasStride)strideA, int batchCount)[#](#_CPPv426hipblasDspr2StridedBatched15hipblasHandle_t17hipblasFillMode_tiPKdPKdi13hipblasStridePKdi13hipblasStridePd13hipblasStridei) BLAS Level 2 API.

spr2StridedBatched performs the matrix-vector operation

where alpha is a scalar, x_i amd y_i are vectors, and A_i is an n by n symmetric matrix, supplied in packed form, for i = 1, …, batchCount.A_i := A_i + alpha*x_i*y_i**T + alpha*y_i*x_i**T

Supported precisions in rocBLAS : s,d

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] specifies whether the upper ‘HIPBLAS_FILL_MODE_UPPER’ or lower ‘HIPBLAS_FILL_MODE_LOWER’ HIPBLAS_FILL_MODE_UPPER: The upper triangular part of each A_i is supplied in AP. HIPBLAS_FILL_MODE_LOWER: The lower triangular part of each A_i is supplied in AP.**n**–**[in]**[int] the number of rows and columns of each matrix A_i, must be at least 0.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device pointer pointing to the first vector (x_1).**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**stridex**–**[in]**[hipblasStride] stride from the start of one vector (x_i) and the next one (x_i+1).**y**–**[in]**device pointer pointing to the first vector (y_1).**incy**–**[in]**[int] specifies the increment for the elements of each y_i.**stridey**–**[in]**[hipblasStride] stride from the start of one vector (y_i) and the next one (y_i+1).**AP**–**[inout]**device pointer storing the packed version of the specified triangular portion of each symmetric matrix A_i. Points to the first A_1. if uplo == HIPBLAS_FILL_MODE_UPPER: The upper triangular portion of each symmetric matrix A_i is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(0,1) AP(2) = A(1,1), etc. Ex: (HIPBLAS_FILL_MODE_UPPER; n = 4) 1 2 4 7 2 3 5 8 –—> [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] 4 5 6 9 7 8 9 0 if uplo == HIPBLAS_FILL_MODE_LOWER: The lower triangular portion of each symmetric matrix A_i is supplied. The matrix is compacted so that AP contains the triangular portion column-by-column so that: AP(0) = A(0,0) AP(1) = A(1,0) AP(n) = A(2,1), etc. Ex: (HIPBLAS_FILL_MODE_LOWER; n = 4) 1 2 3 4 2 5 6 7 –—> [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] 3 6 8 9 4 7 9 0**strideA**–**[in]**[hipblasStride] stride from the start of one (A_i) and the next (A_i+1)**batchCount**–**[in]**[int] number of instances in the batch.



The `spr2StridedBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSsymv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const float *alpha, const float *AP, int lda, const float *x, int incx, const float *beta, float *y, int incy)[#](#_CPPv412hipblasSsymv15hipblasHandle_t17hipblasFillMode_tiPKfPKfiPKfiPKfPfi)

-
hipblasStatus_t hipblasDsymv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const double *alpha, const double *AP, int lda, const double *x, int incx, const double *beta, double *y, int incy)[#](#_CPPv412hipblasDsymv15hipblasHandle_t17hipblasFillMode_tiPKdPKdiPKdiPKdPdi)

-
hipblasStatus_t hipblasCsymv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipComplex *alpha, const hipComplex *AP, int lda, const hipComplex *x, int incx, const hipComplex *beta, hipComplex *y, int incy)[#](#_CPPv412hipblasCsymv15hipblasHandle_t17hipblasFillMode_tiPK10hipComplexPK10hipComplexiPK10hipComplexiPK10hipComplexP10hipComplexi)

-
hipblasStatus_t hipblasZsymv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *AP, int lda, const hipDoubleComplex *x, int incx, const hipDoubleComplex *beta, hipDoubleComplex *y, int incy)[#](#_CPPv412hipblasZsymv15hipblasHandle_t17hipblasFillMode_tiPK16hipDoubleComplexPK16hipDoubleComplexiPK16hipDoubleComplexiPK16hipDoubleComplexP16hipDoubleComplexi) BLAS Level 2 API.

symv performs the matrix-vector operation:

where alpha and beta are scalars, x and y are n element vectors and A should contain an upper or lower triangular n by n symmetric matrix.y := alpha*A*x + beta*y,

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : s,d,c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] specifies whether the upper ‘HIPBLAS_FILL_MODE_UPPER’ or lower ‘HIPBLAS_FILL_MODE_LOWER’ if HIPBLAS_FILL_MODE_UPPER, the lower part of A is not referenced if HIPBLAS_FILL_MODE_LOWER, the upper part of A is not referenced**n**–**[in]**[int]**alpha**–**[in]**specifies the scalar alpha**AP**–**[in]**pointer storing matrix A on the GPU**lda**–**[in]**[int] specifies the leading dimension of A**x**–**[in]**pointer storing vector x on the GPU**incx**–**[in]**[int] specifies the increment for the elements of x**beta**–**[in]**specifies the scalar beta**y**–**[out]**pointer storing vector y on the GPU**incy**–**[in]**[int] specifies the increment for the elements of y



The `symv`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSsymvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const float *alpha, const float *const AP[], int lda, const float *const x[], int incx, const float *beta, float *const y[], int incy, int batchCount)[#](#_CPPv419hipblasSsymvBatched15hipblasHandle_t17hipblasFillMode_tiPKfA_PCKfiA_PCKfiPKfA_PCfii)

-
hipblasStatus_t hipblasDsymvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const double *alpha, const double *const AP[], int lda, const double *const x[], int incx, const double *beta, double *const y[], int incy, int batchCount)[#](#_CPPv419hipblasDsymvBatched15hipblasHandle_t17hipblasFillMode_tiPKdA_PCKdiA_PCKdiPKdA_PCdii)

-
hipblasStatus_t hipblasCsymvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipComplex *alpha, const hipComplex *const AP[], int lda, const hipComplex *const x[], int incx, const hipComplex *beta, hipComplex *const y[], int incy, int batchCount)[#](#_CPPv419hipblasCsymvBatched15hipblasHandle_t17hipblasFillMode_tiPK10hipComplexA_PCK10hipComplexiA_PCK10hipComplexiPK10hipComplexA_PC10hipComplexii)

-
hipblasStatus_t hipblasZsymvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *const AP[], int lda, const hipDoubleComplex *const x[], int incx, const hipDoubleComplex *beta, hipDoubleComplex *const y[], int incy, int batchCount)[#](#_CPPv419hipblasZsymvBatched15hipblasHandle_t17hipblasFillMode_tiPK16hipDoubleComplexA_PCK16hipDoubleComplexiA_PCK16hipDoubleComplexiPK16hipDoubleComplexA_PC16hipDoubleComplexii) BLAS Level 2 API.

symvBatched performs the matrix-vector operation:

where (A_i, x_i, y_i) is the i-th instance of the batch. alpha and beta are scalars, x_i and y_i are vectors and A_i is an n by n symmetric matrix, for i = 1, …, batchCount. A a should contain an upper or lower triangular symmetric matrix and the opposing triangular part of A is not referencedy_i := alpha*A_i*x_i + beta*y_i,

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue**uplo**–**[in]**[hipblasFillMode_t] specifies whether the upper ‘HIPBLAS_FILL_MODE_UPPER’ or lower ‘HIPBLAS_FILL_MODE_LOWER’ if HIPBLAS_FILL_MODE_UPPER, the lower part of A is not referenced if HIPBLAS_FILL_MODE_LOWER, the upper part of A is not referenced**n**–**[in]**[int] number of rows and columns of each matrix A_i**alpha**–**[in]**device pointer or host pointer to scalar alpha**AP**–**[in]**device array of device pointers storing each matrix A_i**lda**–**[in]**[int] specifies the leading dimension of each matrix A_i**x**–**[in]**device array of device pointers storing each vector x_i**incx**–**[in]**[int] specifies the increment for the elements of each vector x_i**beta**–**[in]**device pointer or host pointer to scalar beta**y**–**[out]**device array of device pointers storing each vector y_i**incy**–**[in]**[int] specifies the increment for the elements of each vector y_i**batchCount**–**[in]**[int] number of instances in the batch



The `symvBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSsymvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const float *alpha, const float *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const float *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const float *beta, float *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount)[#](#_CPPv426hipblasSsymvStridedBatched15hipblasHandle_t17hipblasFillMode_tiPKfPKfi13hipblasStridePKfi13hipblasStridePKfPfi13hipblasStridei)

-
hipblasStatus_t hipblasDsymvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const double *alpha, const double *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const double *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const double *beta, double *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount)[#](#_CPPv426hipblasDsymvStridedBatched15hipblasHandle_t17hipblasFillMode_tiPKdPKdi13hipblasStridePKdi13hipblasStridePKdPdi13hipblasStridei)

-
hipblasStatus_t hipblasCsymvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipComplex *alpha, const hipComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const hipComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const hipComplex *beta, hipComplex *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount)[#](#_CPPv426hipblasCsymvStridedBatched15hipblasHandle_t17hipblasFillMode_tiPK10hipComplexPK10hipComplexi13hipblasStridePK10hipComplexi13hipblasStridePK10hipComplexP10hipComplexi13hipblasStridei)

-
hipblasStatus_t hipblasZsymvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const hipDoubleComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const hipDoubleComplex *beta, hipDoubleComplex *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount)[#](#_CPPv426hipblasZsymvStridedBatched15hipblasHandle_t17hipblasFillMode_tiPK16hipDoubleComplexPK16hipDoubleComplexi13hipblasStridePK16hipDoubleComplexi13hipblasStridePK16hipDoubleComplexP16hipDoubleComplexi13hipblasStridei) BLAS Level 2 API.

symvStridedBatched performs the matrix-vector operation:

where (A_i, x_i, y_i) is the i-th instance of the batch. alpha and beta are scalars, x_i and y_i are vectors and A_i is an n by n symmetric matrix, for i = 1, …, batchCount. A a should contain an upper or lower triangular symmetric matrix and the opposing triangular part of A is not referencedy_i := alpha*A_i*x_i + beta*y_i,

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue**uplo**–**[in]**[hipblasFillMode_t] specifies whether the upper ‘HIPBLAS_FILL_MODE_UPPER’ or lower ‘HIPBLAS_FILL_MODE_LOWER’ if HIPBLAS_FILL_MODE_UPPER, the lower part of A is not referenced if HIPBLAS_FILL_MODE_LOWER, the upper part of A is not referenced**n**–**[in]**[int] number of rows and columns of each matrix A_i**alpha**–**[in]**device pointer or host pointer to scalar alpha**AP**–**[in]**Device pointer to the first matrix A_1 on the GPU**lda**–**[in]**[int] specifies the leading dimension of each matrix A_i**strideA**–**[in]**[hipblasStride] stride from the start of one matrix (A_i) and the next one (A_i+1)**x**–**[in]**Device pointer to the first vector x_1 on the GPU**incx**–**[in]**[int] specifies the increment for the elements of each vector x_i**stridex**–**[in]**[hipblasStride] stride from the start of one vector (x_i) and the next one (x_i+1). There are no restrictions placed on stridex, however the user should take care to ensure that stridex is of appropriate size. This typically means stridex >= n * incx. stridex should be non zero.**beta**–**[in]**device pointer or host pointer to scalar beta**y**–**[out]**Device pointer to the first vector y_1 on the GPU**incy**–**[in]**[int] specifies the increment for the elements of each vector y_i**stridey**–**[in]**[hipblasStride] stride from the start of one vector (y_i) and the next one (y_i+1). There are no restrictions placed on stridey, however the user should take care to ensure that stridey is of appropriate size. This typically means stridey >= n * incy. stridey should be non zero.**batchCount**–**[in]**[int] number of instances in the batch



The `symvStridedBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSsyr(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const float *alpha, const float *x, int incx, float *AP, int lda)[#](#_CPPv411hipblasSsyr15hipblasHandle_t17hipblasFillMode_tiPKfPKfiPfi)

-
hipblasStatus_t hipblasDsyr(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const double *alpha, const double *x, int incx, double *AP, int lda)[#](#_CPPv411hipblasDsyr15hipblasHandle_t17hipblasFillMode_tiPKdPKdiPdi)

-
hipblasStatus_t hipblasCsyr(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipComplex *alpha, const hipComplex *x, int incx, hipComplex *AP, int lda)[#](#_CPPv411hipblasCsyr15hipblasHandle_t17hipblasFillMode_tiPK10hipComplexPK10hipComplexiP10hipComplexi)

-
hipblasStatus_t hipblasZsyr(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *x, int incx, hipDoubleComplex *AP, int lda)[#](#_CPPv411hipblasZsyr15hipblasHandle_t17hipblasFillMode_tiPK16hipDoubleComplexPK16hipDoubleComplexiP16hipDoubleComplexi) BLAS Level 2 API.

syr performs the matrix-vector operations

where alpha is a scalar, x is a vector, and A is an n by n symmetric matrix.A := A + alpha*x*x**T

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : s,d,c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] specifies whether the upper ‘HIPBLAS_FILL_MODE_UPPER’ or lower ‘HIPBLAS_FILL_MODE_LOWER’ if HIPBLAS_FILL_MODE_UPPER, the lower part of A is not referenced if HIPBLAS_FILL_MODE_LOWER, the upper part of A is not referenced**n**–**[in]**[int] the number of rows and columns of matrix A.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[int] specifies the increment for the elements of x.**AP**–**[inout]**device pointer storing matrix A.**lda**–**[in]**[int] specifies the leading dimension of A.



The `syr`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSsyrBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const float *alpha, const float *const x[], int incx, float *const AP[], int lda, int batchCount)[#](#_CPPv418hipblasSsyrBatched15hipblasHandle_t17hipblasFillMode_tiPKfA_PCKfiA_PCfii)

-
hipblasStatus_t hipblasDsyrBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const double *alpha, const double *const x[], int incx, double *const AP[], int lda, int batchCount)[#](#_CPPv418hipblasDsyrBatched15hipblasHandle_t17hipblasFillMode_tiPKdA_PCKdiA_PCdii)

-
hipblasStatus_t hipblasCsyrBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipComplex *alpha, const hipComplex *const x[], int incx, hipComplex *const AP[], int lda, int batchCount)[#](#_CPPv418hipblasCsyrBatched15hipblasHandle_t17hipblasFillMode_tiPK10hipComplexA_PCK10hipComplexiA_PC10hipComplexii)

-
hipblasStatus_t hipblasZsyrBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *const x[], int incx, hipDoubleComplex *const AP[], int lda, int batchCount)[#](#_CPPv418hipblasZsyrBatched15hipblasHandle_t17hipblasFillMode_tiPK16hipDoubleComplexA_PCK16hipDoubleComplexiA_PC16hipDoubleComplexii) BLAS Level 2 API.

syrBatched performs a batch of matrix-vector operations

where alpha is a scalar, x is an array of vectors, and A is an array of n by n symmetric matrices, for i = 1 , … , batchCount.A[i] := A[i] + alpha*x[i]*x[i]**T

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] specifies whether the upper ‘HIPBLAS_FILL_MODE_UPPER’ or lower ‘HIPBLAS_FILL_MODE_LOWER’ if HIPBLAS_FILL_MODE_UPPER, the lower part of A is not referenced if HIPBLAS_FILL_MODE_LOWER, the upper part of A is not referenced**n**–**[in]**[int] the number of rows and columns of matrix A.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**AP**–**[inout]**device array of device pointers storing each matrix A_i.**lda**–**[in]**[int] specifies the leading dimension of each A_i.**batchCount**–**[in]**[int] number of instances in the batch



The `syrBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSsyrStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const float *alpha, const float *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, float *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, int batchCount)[#](#_CPPv425hipblasSsyrStridedBatched15hipblasHandle_t17hipblasFillMode_tiPKfPKfi13hipblasStridePfi13hipblasStridei)

-
hipblasStatus_t hipblasDsyrStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const double *alpha, const double *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, double *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, int batchCount)[#](#_CPPv425hipblasDsyrStridedBatched15hipblasHandle_t17hipblasFillMode_tiPKdPKdi13hipblasStridePdi13hipblasStridei)

-
hipblasStatus_t hipblasCsyrStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipComplex *alpha, const hipComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, hipComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, int batchCount)[#](#_CPPv425hipblasCsyrStridedBatched15hipblasHandle_t17hipblasFillMode_tiPK10hipComplexPK10hipComplexi13hipblasStrideP10hipComplexi13hipblasStridei)

-
hipblasStatus_t hipblasZsyrStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, hipDoubleComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, int batchCount)[#](#_CPPv425hipblasZsyrStridedBatched15hipblasHandle_t17hipblasFillMode_tiPK16hipDoubleComplexPK16hipDoubleComplexi13hipblasStrideP16hipDoubleComplexi13hipblasStridei) BLAS Level 2 API.

syrStridedBatched performs the matrix-vector operations

where alpha is a scalar, vectors, and A is an array of n by n symmetric matrices, for i = 1 , … , batchCount.A[i] := A[i] + alpha*x[i]*x[i]**T

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] specifies whether the upper ‘HIPBLAS_FILL_MODE_UPPER’ or lower ‘HIPBLAS_FILL_MODE_LOWER’ if HIPBLAS_FILL_MODE_UPPER, the lower part of A is not referenced if HIPBLAS_FILL_MODE_LOWER, the upper part of A is not referenced**n**–**[in]**[int] the number of rows and columns of each matrix A.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device pointer to the first vector x_1.**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**stridex**–**[in]**[hipblasStride] specifies the pointer increment between vectors (x_i) and (x_i+1).**AP**–**[inout]**device pointer to the first matrix A_1.**lda**–**[in]**[int] specifies the leading dimension of each A_i.**strideA**–**[in]**[hipblasStride] stride from the start of one matrix (A_i) and the next one (A_i+1)**batchCount**–**[in]**[int] number of instances in the batch



The `syrStridedBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSsyr2(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const float *alpha, const float *x, int incx, const float *y, int incy, float *AP, int lda)[#](#_CPPv412hipblasSsyr215hipblasHandle_t17hipblasFillMode_tiPKfPKfiPKfiPfi)

-
hipblasStatus_t hipblasDsyr2(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const double *alpha, const double *x, int incx, const double *y, int incy, double *AP, int lda)[#](#_CPPv412hipblasDsyr215hipblasHandle_t17hipblasFillMode_tiPKdPKdiPKdiPdi)

-
hipblasStatus_t hipblasCsyr2(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipComplex *alpha, const hipComplex *x, int incx, const hipComplex *y, int incy, hipComplex *AP, int lda)[#](#_CPPv412hipblasCsyr215hipblasHandle_t17hipblasFillMode_tiPK10hipComplexPK10hipComplexiPK10hipComplexiP10hipComplexi)

-
hipblasStatus_t hipblasZsyr2(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *x, int incx, const hipDoubleComplex *y, int incy, hipDoubleComplex *AP, int lda)[#](#_CPPv412hipblasZsyr215hipblasHandle_t17hipblasFillMode_tiPK16hipDoubleComplexPK16hipDoubleComplexiPK16hipDoubleComplexiP16hipDoubleComplexi) BLAS Level 2 API.

syr2 performs the matrix-vector operations

where alpha is a scalar, x and y are vectors, and A is an n by n symmetric matrix.A := A + alpha*x*y**T + alpha*y*x**T

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] specifies whether the upper ‘HIPBLAS_FILL_MODE_UPPER’ or lower ‘HIPBLAS_FILL_MODE_LOWER’ if HIPBLAS_FILL_MODE_UPPER, the lower part of A is not referenced if HIPBLAS_FILL_MODE_LOWER, the upper part of A is not referenced**n**–**[in]**[int] the number of rows and columns of matrix A.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[int] specifies the increment for the elements of x.**y**–**[in]**device pointer storing vector y.**incy**–**[in]**[int] specifies the increment for the elements of y.**AP**–**[inout]**device pointer storing matrix A.**lda**–**[in]**[int] specifies the leading dimension of A.



The `syr2`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSsyr2Batched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const float *alpha, const float *const x[], int incx, const float *const y[], int incy, float *const AP[], int lda, int batchCount)[#](#_CPPv419hipblasSsyr2Batched15hipblasHandle_t17hipblasFillMode_tiPKfA_PCKfiA_PCKfiA_PCfii)

-
hipblasStatus_t hipblasDsyr2Batched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const double *alpha, const double *const x[], int incx, const double *const y[], int incy, double *const AP[], int lda, int batchCount)[#](#_CPPv419hipblasDsyr2Batched15hipblasHandle_t17hipblasFillMode_tiPKdA_PCKdiA_PCKdiA_PCdii)

-
hipblasStatus_t hipblasCsyr2Batched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipComplex *alpha, const hipComplex *const x[], int incx, const hipComplex *const y[], int incy, hipComplex *const AP[], int lda, int batchCount)[#](#_CPPv419hipblasCsyr2Batched15hipblasHandle_t17hipblasFillMode_tiPK10hipComplexA_PCK10hipComplexiA_PCK10hipComplexiA_PC10hipComplexii)

-
hipblasStatus_t hipblasZsyr2Batched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *const x[], int incx, const hipDoubleComplex *const y[], int incy, hipDoubleComplex *const AP[], int lda, int batchCount)[#](#_CPPv419hipblasZsyr2Batched15hipblasHandle_t17hipblasFillMode_tiPK16hipDoubleComplexA_PCK16hipDoubleComplexiA_PCK16hipDoubleComplexiA_PC16hipDoubleComplexii) BLAS Level 2 API.

syr2Batched performs a batch of matrix-vector operations

where alpha is a scalar, x[i] and y[i] are vectors, and A[i] is a n by n symmetric matrix, for i = 1 , … , batchCount.A[i] := A[i] + alpha*x[i]*y[i]**T + alpha*y[i]*x[i]**T

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] specifies whether the upper ‘HIPBLAS_FILL_MODE_UPPER’ or lower ‘HIPBLAS_FILL_MODE_LOWER’ if HIPBLAS_FILL_MODE_UPPER, the lower part of A is not referenced if HIPBLAS_FILL_MODE_LOWER, the upper part of A is not referenced**n**–**[in]**[int] the number of rows and columns of matrix A.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**y**–**[in]**device array of device pointers storing each vector y_i.**incy**–**[in]**[int] specifies the increment for the elements of each y_i.**AP**–**[inout]**device array of device pointers storing each matrix A_i.**lda**–**[in]**[int] specifies the leading dimension of each A_i.**batchCount**–**[in]**[int] number of instances in the batch



The `syr2Batched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSsyr2StridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const float *alpha, const float *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const float *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, float *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, int batchCount)[#](#_CPPv426hipblasSsyr2StridedBatched15hipblasHandle_t17hipblasFillMode_tiPKfPKfi13hipblasStridePKfi13hipblasStridePfi13hipblasStridei)

-
hipblasStatus_t hipblasDsyr2StridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const double *alpha, const double *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const double *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, double *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, int batchCount)[#](#_CPPv426hipblasDsyr2StridedBatched15hipblasHandle_t17hipblasFillMode_tiPKdPKdi13hipblasStridePKdi13hipblasStridePdi13hipblasStridei)

-
hipblasStatus_t hipblasCsyr2StridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipComplex *alpha, const hipComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const hipComplex *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, hipComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, int batchCount)[#](#_CPPv426hipblasCsyr2StridedBatched15hipblasHandle_t17hipblasFillMode_tiPK10hipComplexPK10hipComplexi13hipblasStridePK10hipComplexi13hipblasStrideP10hipComplexi13hipblasStridei)

-
hipblasStatus_t hipblasZsyr2StridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const hipDoubleComplex *y, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, hipDoubleComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, int batchCount)[#](#_CPPv426hipblasZsyr2StridedBatched15hipblasHandle_t17hipblasFillMode_tiPK16hipDoubleComplexPK16hipDoubleComplexi13hipblasStridePK16hipDoubleComplexi13hipblasStrideP16hipDoubleComplexi13hipblasStridei) BLAS Level 2 API.

syr2StridedBatched the matrix-vector operations

where alpha is a scalar, x[i] and y[i] are vectors, and A[i] is a n by n symmetric matrices, for i = 1 , … , batchCount.A[i] := A[i] + alpha*x[i]*y[i]**T + alpha*y[i]*x[i]**T

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] specifies whether the upper ‘HIPBLAS_FILL_MODE_UPPER’ or lower ‘HIPBLAS_FILL_MODE_LOWER’ if HIPBLAS_FILL_MODE_UPPER, the lower part of A is not referenced if HIPBLAS_FILL_MODE_LOWER, the upper part of A is not referenced**n**–**[in]**[int] the number of rows and columns of each matrix A.**alpha**–**[in]**device pointer or host pointer to scalar alpha.**x**–**[in]**device pointer to the first vector x_1.**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**stridex**–**[in]**[hipblasStride] specifies the pointer increment between vectors (x_i) and (x_i+1).**y**–**[in]**device pointer to the first vector y_1.**incy**–**[in]**[int] specifies the increment for the elements of each y_i.**stridey**–**[in]**[hipblasStride] specifies the pointer increment between vectors (y_i) and (y_i+1).**AP**–**[inout]**device pointer to the first matrix A_1.**lda**–**[in]**[int] specifies the leading dimension of each A_i.**strideA**–**[in]**[hipblasStride] stride from the start of one matrix (A_i) and the next one (A_i+1)**batchCount**–**[in]**[int] number of instances in the batch



The `syr2StridedBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasStbmv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, int k, const float *AP, int lda, float *x, int incx)[#](#_CPPv412hipblasStbmv15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPKfiPfi)

-
hipblasStatus_t hipblasDtbmv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, int k, const double *AP, int lda, double *x, int incx)[#](#_CPPv412hipblasDtbmv15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPKdiPdi)

-
hipblasStatus_t hipblasCtbmv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, int k, const hipComplex *AP, int lda, hipComplex *x, int incx)[#](#_CPPv412hipblasCtbmv15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPK10hipComplexiP10hipComplexi)

-
hipblasStatus_t hipblasZtbmv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, int k, const hipDoubleComplex *AP, int lda, hipDoubleComplex *x, int incx)[#](#_CPPv412hipblasZtbmv15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPK16hipDoubleComplexiP16hipDoubleComplexi) BLAS Level 2 API.

tbmv performs one of the matrix-vector operations

x is a vectors and A is a banded n by n matrix (see description below).x := A*x or x := A**T*x or x := A**H*x,

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : s,d,c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: A is an upper banded triangular matrix. HIPBLAS_FILL_MODE_LOWER: A is a lower banded triangular matrix.**transA**–**[in]**[hipblasOperation_t] indicates whether matrix A is tranposed (conjugated) or not.**diag**–**[in]**[hipblasDiagType_t] HIPBLAS_DIAG_UNIT: The main diagonal of A is assumed to consist of only 1’s and is not referenced. HIPBLAS_DIAG_NON_UNIT: No assumptions are made of A’s main diagonal.**n**–**[in]**[int] the number of rows and columns of the matrix represented by A.**k**–**[in]**[int] if uplo == HIPBLAS_FILL_MODE_UPPER, k specifies the number of super-diagonals of the matrix A. if uplo == HIPBLAS_FILL_MODE_LOWER, k specifies the number of sub-diagonals of the matrix A. k must satisfy k > 0 && k < lda.**AP**–**[in]**device pointer storing banded triangular matrix A. if uplo == HIPBLAS_FILL_MODE_UPPER: The matrix represented is an upper banded triangular matrix with the main diagonal and k super-diagonals, everything else can be assumed to be 0. The matrix is compacted so that the main diagonal resides on the k’th row, the first super diagonal resides on the RHS of the k-1’th row, etc, with the k’th diagonal on the RHS of the 0’th row. Ex: (HIPBLAS_FILL_MODE_UPPER; n = 5; k = 2) 1 6 9 0 0 0 0 9 8 7 0 2 7 8 0 0 6 7 8 9 0 0 3 8 7 -—> 1 2 3 4 5 0 0 0 4 9 0 0 0 0 0 0 0 0 0 5 0 0 0 0 0 if uplo == HIPBLAS_FILL_MODE_LOWER: The matrix represnted is a lower banded triangular matrix with the main diagonal and k sub-diagonals, everything else can be assumed to be 0. The matrix is compacted so that the main diagonal resides on the 0’th row, working up to the k’th diagonal residing on the LHS of the k’th row. Ex: (HIPBLAS_FILL_MODE_LOWER; n = 5; k = 2) 1 0 0 0 0 1 2 3 4 5 6 2 0 0 0 6 7 8 9 0 9 7 3 0 0 -—> 9 8 7 0 0 0 8 8 4 0 0 0 0 0 0 0 0 7 9 5 0 0 0 0 0**lda**–**[in]**[int] specifies the leading dimension of A. lda must satisfy lda > k.**x**–**[inout]**device pointer storing vector x.**incx**–**[in]**[int] specifies the increment for the elements of x.



The `tbmv`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasStbmvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, int k, const float *const AP[], int lda, float *const x[], int incx, int batchCount)[#](#_CPPv419hipblasStbmvBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiA_PCKfiA_PCfii)

-
hipblasStatus_t hipblasDtbmvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, int k, const double *const AP[], int lda, double *const x[], int incx, int batchCount)[#](#_CPPv419hipblasDtbmvBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiA_PCKdiA_PCdii)

-
hipblasStatus_t hipblasCtbmvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, int k, const hipComplex *const AP[], int lda, hipComplex *const x[], int incx, int batchCount)[#](#_CPPv419hipblasCtbmvBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiA_PCK10hipComplexiA_PC10hipComplexii)

-
hipblasStatus_t hipblasZtbmvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, int k, const hipDoubleComplex *const AP[], int lda, hipDoubleComplex *const x[], int incx, int batchCount)[#](#_CPPv419hipblasZtbmvBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiA_PCK16hipDoubleComplexiA_PC16hipDoubleComplexii) BLAS Level 2 API.

tbmvBatched performs one of the matrix-vector operations

where (A_i, x_i) is the i-th instance of the batch. x_i is a vector and A_i is an n by n matrix, for i = 1, …, batchCount.x_i := A_i*x_i or x_i := A_i**T*x_i or x_i := A_i**H*x_i,

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: each A_i is an upper banded triangular matrix. HIPBLAS_FILL_MODE_LOWER: each A_i is a lower banded triangular matrix.**transA**–**[in]**[hipblasOperation_t] indicates whether each matrix A_i is tranposed (conjugated) or not.**diag**–**[in]**[hipblasDiagType_t] HIPBLAS_DIAG_UNIT: The main diagonal of each A_i is assumed to consist of only 1’s and is not referenced. HIPBLAS_DIAG_NON_UNIT: No assumptions are made of each A_i’s main diagonal.**n**–**[in]**[int] the number of rows and columns of the matrix represented by each A_i.**k**–**[in]**[int] if uplo == HIPBLAS_FILL_MODE_UPPER, k specifies the number of super-diagonals of each matrix A_i. if uplo == HIPBLAS_FILL_MODE_LOWER, k specifies the number of sub-diagonals of each matrix A_i. k must satisfy k > 0 && k < lda.**AP**–**[in]**device array of device pointers storing each banded triangular matrix A_i. if uplo == HIPBLAS_FILL_MODE_UPPER: The matrix represented is an upper banded triangular matrix with the main diagonal and k super-diagonals, everything else can be assumed to be 0. The matrix is compacted so that the main diagonal resides on the k’th row, the first super diagonal resides on the RHS of the k-1’th row, etc, with the k’th diagonal on the RHS of the 0’th row. Ex: (HIPBLAS_FILL_MODE_UPPER; n = 5; k = 2) 1 6 9 0 0 0 0 9 8 7 0 2 7 8 0 0 6 7 8 9 0 0 3 8 7 -—> 1 2 3 4 5 0 0 0 4 9 0 0 0 0 0 0 0 0 0 5 0 0 0 0 0 if uplo == HIPBLAS_FILL_MODE_LOWER: The matrix represnted is a lower banded triangular matrix with the main diagonal and k sub-diagonals, everything else can be assumed to be 0. The matrix is compacted so that the main diagonal resides on the 0’th row, working up to the k’th diagonal residing on the LHS of the k’th row. Ex: (HIPBLAS_FILL_MODE_LOWER; n = 5; k = 2) 1 0 0 0 0 1 2 3 4 5 6 2 0 0 0 6 7 8 9 0 9 7 3 0 0 -—> 9 8 7 0 0 0 8 8 4 0 0 0 0 0 0 0 0 7 9 5 0 0 0 0 0**lda**–**[in]**[int] specifies the leading dimension of each A_i. lda must satisfy lda > k.**x**–**[inout]**device array of device pointer storing each vector x_i.**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**batchCount**–**[in]**[int] number of instances in the batch.



The `tbmvBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasStbmvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, int k, const float *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, float *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount)[#](#_CPPv426hipblasStbmvStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPKfi13hipblasStridePfi13hipblasStridei)

-
hipblasStatus_t hipblasDtbmvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, int k, const double *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, double *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount)[#](#_CPPv426hipblasDtbmvStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPKdi13hipblasStridePdi13hipblasStridei)

-
hipblasStatus_t hipblasCtbmvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, int k, const hipComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, hipComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount)[#](#_CPPv426hipblasCtbmvStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPK10hipComplexi13hipblasStrideP10hipComplexi13hipblasStridei)

-
hipblasStatus_t hipblasZtbmvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, int k, const hipDoubleComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, hipDoubleComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount)[#](#_CPPv426hipblasZtbmvStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPK16hipDoubleComplexi13hipblasStrideP16hipDoubleComplexi13hipblasStridei) BLAS Level 2 API.

tbmvStridedBatched performs one of the matrix-vector operations

where (A_i, x_i) is the i-th instance of the batch. x_i is a vector and A_i is an n by n matrix, for i = 1, …, batchCount.x_i := A_i*x_i or x_i := A_i**T*x_i or x_i := A_i**H*x_i,

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: each A_i is an upper banded triangular matrix. HIPBLAS_FILL_MODE_LOWER: each A_i is a lower banded triangular matrix.**transA**–**[in]**[hipblasOperation_t] indicates whether each matrix A_i is tranposed (conjugated) or not.**diag**–**[in]**[hipblasDiagType_t] HIPBLAS_DIAG_UNIT: The main diagonal of each A_i is assumed to consist of only 1’s and is not referenced. HIPBLAS_DIAG_NON_UNIT: No assumptions are made of each A_i’s main diagonal.**n**–**[in]**[int] the number of rows and columns of the matrix represented by each A_i.**k**–**[in]**[int] if uplo == HIPBLAS_FILL_MODE_UPPER, k specifies the number of super-diagonals of each matrix A_i. if uplo == HIPBLAS_FILL_MODE_LOWER, k specifies the number of sub-diagonals of each matrix A_i. k must satisfy k > 0 && k < lda.**AP**–**[in]**device array to the first matrix A_i of the batch. Stores each banded triangular matrix A_i. if uplo == HIPBLAS_FILL_MODE_UPPER: The matrix represented is an upper banded triangular matrix with the main diagonal and k super-diagonals, everything else can be assumed to be 0. The matrix is compacted so that the main diagonal resides on the k’th row, the first super diagonal resides on the RHS of the k-1’th row, etc, with the k’th diagonal on the RHS of the 0’th row. Ex: (HIPBLAS_FILL_MODE_UPPER; n = 5; k = 2) 1 6 9 0 0 0 0 9 8 7 0 2 7 8 0 0 6 7 8 9 0 0 3 8 7 -—> 1 2 3 4 5 0 0 0 4 9 0 0 0 0 0 0 0 0 0 5 0 0 0 0 0 if uplo == HIPBLAS_FILL_MODE_LOWER: The matrix represnted is a lower banded triangular matrix with the main diagonal and k sub-diagonals, everything else can be assumed to be 0. The matrix is compacted so that the main diagonal resides on the 0’th row, working up to the k’th diagonal residing on the LHS of the k’th row. Ex: (HIPBLAS_FILL_MODE_LOWER; n = 5; k = 2) 1 0 0 0 0 1 2 3 4 5 6 2 0 0 0 6 7 8 9 0 9 7 3 0 0 -—> 9 8 7 0 0 0 8 8 4 0 0 0 0 0 0 0 0 7 9 5 0 0 0 0 0**lda**–**[in]**[int] specifies the leading dimension of each A_i. lda must satisfy lda > k.**strideA**–**[in]**[hipblasStride] stride from the start of one A_i matrix to the next A_(i + 1).**x**–**[inout]**device array to the first vector x_i of the batch.**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**stridex**–**[in]**[hipblasStride] stride from the start of one x_i matrix to the next x_(i + 1).**batchCount**–**[in]**[int] number of instances in the batch.



The `tbmvStridedBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasStbsv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, int k, const float *AP, int lda, float *x, int incx)[#](#_CPPv412hipblasStbsv15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPKfiPfi)

-
hipblasStatus_t hipblasDtbsv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, int k, const double *AP, int lda, double *x, int incx)[#](#_CPPv412hipblasDtbsv15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPKdiPdi)

-
hipblasStatus_t hipblasCtbsv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, int k, const hipComplex *AP, int lda, hipComplex *x, int incx)[#](#_CPPv412hipblasCtbsv15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPK10hipComplexiP10hipComplexi)

-
hipblasStatus_t hipblasZtbsv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, int k, const hipDoubleComplex *AP, int lda, hipDoubleComplex *x, int incx)[#](#_CPPv412hipblasZtbsv15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPK16hipDoubleComplexiP16hipDoubleComplexi) BLAS Level 2 API.

tbsv solves

where x and b are vectors and A is a banded triangular matrix.A*x = b or A**T*x = b or A**H*x = b,

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : s,d,c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: A is an upper triangular matrix. HIPBLAS_FILL_MODE_LOWER: A is a lower triangular matrix.**transA**–**[in]**[hipblasOperation_t] HIPBLAS_OP_N: Solves A*x = b HIPBLAS_OP_T: Solves A**T*x = b HIPBLAS_OP_C: Solves A**H*x = b**diag**–**[in]**[hipblasDiagType_t] HIPBLAS_DIAG_UNIT: A is assumed to be unit triangular (i.e. the diagonal elements of A are not used in computations). HIPBLAS_DIAG_NON_UNIT: A is not assumed to be unit triangular.**n**–**[in]**[int] n specifies the number of rows of b. n >= 0.**k**–**[in]**[int] if(uplo == HIPBLAS_FILL_MODE_UPPER) k specifies the number of super-diagonals of A. if(uplo == HIPBLAS_FILL_MODE_LOWER) k specifies the number of sub-diagonals of A. k >= 0.**AP**–**[in]**device pointer storing the matrix A in banded format.**lda**–**[in]**[int] specifies the leading dimension of A. lda >= (k + 1).**x**–**[inout]**device pointer storing input vector b. Overwritten by the output vector x.**incx**–**[in]**[int] specifies the increment for the elements of x.



The `tbsv`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasStbsvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, int k, const float *const AP[], int lda, float *const x[], int incx, int batchCount)[#](#_CPPv419hipblasStbsvBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiA_PCKfiA_PCfii)

-
hipblasStatus_t hipblasDtbsvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, int k, const double *const AP[], int lda, double *const x[], int incx, int batchCount)[#](#_CPPv419hipblasDtbsvBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiA_PCKdiA_PCdii)

-
hipblasStatus_t hipblasCtbsvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, int k, const hipComplex *const AP[], int lda, hipComplex *const x[], int incx, int batchCount)[#](#_CPPv419hipblasCtbsvBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiA_PCK10hipComplexiA_PC10hipComplexii)

-
hipblasStatus_t hipblasZtbsvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, int k, const hipDoubleComplex *const AP[], int lda, hipDoubleComplex *const x[], int incx, int batchCount)[#](#_CPPv419hipblasZtbsvBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiA_PCK16hipDoubleComplexiA_PC16hipDoubleComplexii) BLAS Level 2 API.

tbsvBatched solves

where x_i and b_i are vectors and A_i is a banded triangular matrix, for i = [1, batchCount].A_i*x_i = b_i or A_i**T*x_i = b_i or A_i**H*x_i = b_i,

The input vectors b_i are overwritten by the output vectors x_i.

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: A_i is an upper triangular matrix. HIPBLAS_FILL_MODE_LOWER: A_i is a lower triangular matrix.**transA**–**[in]**[hipblasOperation_t] HIPBLAS_OP_N: Solves A_i*x_i = b_i HIPBLAS_OP_T: Solves A_i**T*x_i = b_i HIPBLAS_OP_C: Solves A_i**H*x_i = b_i**diag**–**[in]**[hipblasDiagType_t] HIPBLAS_DIAG_UNIT: each A_i is assumed to be unit triangular (i.e. the diagonal elements of each A_i are not used in computations). HIPBLAS_DIAG_NON_UNIT: each A_i is not assumed to be unit triangular.**n**–**[in]**[int] n specifies the number of rows of each b_i. n >= 0.**k**–**[in]**[int] if(uplo == HIPBLAS_FILL_MODE_UPPER) k specifies the number of super-diagonals of each A_i. if(uplo == HIPBLAS_FILL_MODE_LOWER) k specifies the number of sub-diagonals of each A_i. k >= 0.**AP**–**[in]**device vector of device pointers storing each matrix A_i in banded format.**lda**–**[in]**[int] specifies the leading dimension of each A_i. lda >= (k + 1).**x**–**[inout]**device vector of device pointers storing each input vector b_i. Overwritten by each output vector x_i.**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**batchCount**–**[in]**[int] number of instances in the batch.



The `tbsvBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasStbsvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, int k, const float *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, float *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount)[#](#_CPPv426hipblasStbsvStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPKfi13hipblasStridePfi13hipblasStridei)

-
hipblasStatus_t hipblasDtbsvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, int k, const double *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, double *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount)[#](#_CPPv426hipblasDtbsvStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPKdi13hipblasStridePdi13hipblasStridei)

-
hipblasStatus_t hipblasCtbsvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, int k, const hipComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, hipComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount)[#](#_CPPv426hipblasCtbsvStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPK10hipComplexi13hipblasStrideP10hipComplexi13hipblasStridei)

-
hipblasStatus_t hipblasZtbsvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, int k, const hipDoubleComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, hipDoubleComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount)[#](#_CPPv426hipblasZtbsvStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPK16hipDoubleComplexi13hipblasStrideP16hipDoubleComplexi13hipblasStridei) BLAS Level 2 API.

tbsvStridedBatched solves

where x_i and b_i are vectors and A_i is a banded triangular matrix, for i = [1, batchCount].A_i*x_i = b_i or A_i**T*x_i = b_i or A_i**H*x_i = b_i,

The input vectors b_i are overwritten by the output vectors x_i.

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: A_i is an upper triangular matrix. HIPBLAS_FILL_MODE_LOWER: A_i is a lower triangular matrix.**transA**–**[in]**[hipblasOperation_t] HIPBLAS_OP_N: Solves A_i*x_i = b_i HIPBLAS_OP_T: Solves A_i**T*x_i = b_i HIPBLAS_OP_C: Solves A_i**H*x_i = b_i**diag**–**[in]**[hipblasDiagType_t] HIPBLAS_DIAG_UNIT: each A_i is assumed to be unit triangular (i.e. the diagonal elements of each A_i are not used in computations). HIPBLAS_DIAG_NON_UNIT: each A_i is not assumed to be unit triangular.**n**–**[in]**[int] n specifies the number of rows of each b_i. n >= 0.**k**–**[in]**[int] if(uplo == HIPBLAS_FILL_MODE_UPPER) k specifies the number of super-diagonals of each A_i. if(uplo == HIPBLAS_FILL_MODE_LOWER) k specifies the number of sub-diagonals of each A_i. k >= 0.**AP**–**[in]**device pointer pointing to the first banded matrix A_1.**lda**–**[in]**[int] specifies the leading dimension of each A_i. lda >= (k + 1).**strideA**–**[in]**[hipblasStride] specifies the distance between the start of one matrix (A_i) and the next (A_i+1).**x**–**[inout]**device pointer pointing to the first input vector b_1. Overwritten by output vectors x.**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**stridex**–**[in]**[hipblasStride] specifies the distance between the start of one vector (x_i) and the next (x_i+1).**batchCount**–**[in]**[int] number of instances in the batch.



The `tbsvStridedBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasStpmv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const float *AP, float *x, int incx)[#](#_CPPv412hipblasStpmv15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiPKfPfi)

-
hipblasStatus_t hipblasDtpmv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const double *AP, double *x, int incx)[#](#_CPPv412hipblasDtpmv15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiPKdPdi)

-
hipblasStatus_t hipblasCtpmv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const hipComplex *AP, hipComplex *x, int incx)[#](#_CPPv412hipblasCtpmv15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiPK10hipComplexP10hipComplexi)

-
hipblasStatus_t hipblasZtpmv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const hipDoubleComplex *AP, hipDoubleComplex *x, int incx)[#](#_CPPv412hipblasZtpmv15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiPK16hipDoubleComplexP16hipDoubleComplexi) BLAS Level 2 API.

tpmv performs one of the matrix-vector operations

where x is an n element vector and A is an n by n unit, or non-unit, upper or lower triangular matrix, supplied in the pack form.x = A*x or x = A**T*x,

The vector x is overwritten.

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : s,d,c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: A is an upper triangular matrix. HIPBLAS_FILL_MODE_LOWER: A is a lower triangular matrix.**transA**–**[in]**[hipblasOperation_t]**diag**–**[in]**[hipblasDiagType_t] HIPBLAS_DIAG_UNIT: A is assumed to be unit triangular. HIPBLAS_DIAG_NON_UNIT: A is not assumed to be unit triangular.**n**–**[in]**[int] n specifies the number of rows of A. n >= 0.**AP**–**[in]**device pointer storing matrix A, of dimension at least ( n * ( n + 1 ) / 2 ). Before entry with uplo = HIPBLAS_FILL_MODE_UPPER, the array A must contain the upper triangular matrix packed sequentially, column by column, so that A[0] contains a_{0,0}, A[1] and A[2] contain a_{0,1} and a_{1, 1} respectively, and so on. Before entry with uplo = HIPBLAS_FILL_MODE_LOWER, the array A must contain the lower triangular matrix packed sequentially, column by column, so that A[0] contains a_{0,0}, A[1] and A[2] contain a_{1,0} and a_{2,0} respectively, and so on. Note that when DIAG = HIPBLAS_DIAG_UNIT, the diagonal elements of A are not referenced, but are assumed to be unity.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[int] specifies the increment for the elements of x. incx must not be zero.



The `tpmv`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasStpmvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const float *const AP[], float *const x[], int incx, int batchCount)[#](#_CPPv419hipblasStpmvBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiA_PCKfA_PCfii)

-
hipblasStatus_t hipblasDtpmvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const double *const AP[], double *const x[], int incx, int batchCount)[#](#_CPPv419hipblasDtpmvBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiA_PCKdA_PCdii)

-
hipblasStatus_t hipblasCtpmvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const hipComplex *const AP[], hipComplex *const x[], int incx, int batchCount)[#](#_CPPv419hipblasCtpmvBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiA_PCK10hipComplexA_PC10hipComplexii)

-
hipblasStatus_t hipblasZtpmvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const hipDoubleComplex *const AP[], hipDoubleComplex *const x[], int incx, int batchCount)[#](#_CPPv419hipblasZtpmvBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiA_PCK16hipDoubleComplexA_PC16hipDoubleComplexii) BLAS Level 2 API.

tpmvBatched performs one of the matrix-vector operations

where x_i is an n element vector and A_i is an n by n (unit, or non-unit, upper or lower triangular matrix)x_i = A_i*x_i or x_i = A**T*x_i, 0 \le i < batchCount

The vectors x_i are overwritten.

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: A_i is an upper triangular matrix. HIPBLAS_FILL_MODE_LOWER: A_i is a lower triangular matrix.**transA**–**[in]**[hipblasOperation_t]**diag**–**[in]**[hipblasDiagType_t] HIPBLAS_DIAG_UNIT: A_i is assumed to be unit triangular. HIPBLAS_DIAG_NON_UNIT: A_i is not assumed to be unit triangular.**n**–**[in]**[int] n specifies the number of rows of matrices A_i. n >= 0.**AP**–**[in]**device pointer storing pointer of matrices A_i, of dimension ( lda, n )**x**–**[in]**device pointer storing vectors x_i.**incx**–**[in]**[int] specifies the increment for the elements of vectors x_i.**batchCount**–**[in]**[int] The number of batched matrices/vectors.



The `tpmvBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasStpmvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const float *AP,[hipblasStride](#_CPPv413hipblasStride)strideA, float *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount)[#](#_CPPv426hipblasStpmvStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiPKf13hipblasStridePfi13hipblasStridei)

-
hipblasStatus_t hipblasDtpmvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const double *AP,[hipblasStride](#_CPPv413hipblasStride)strideA, double *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount)[#](#_CPPv426hipblasDtpmvStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiPKd13hipblasStridePdi13hipblasStridei)

-
hipblasStatus_t hipblasCtpmvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const hipComplex *AP,[hipblasStride](#_CPPv413hipblasStride)strideA, hipComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount)[#](#_CPPv426hipblasCtpmvStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiPK10hipComplex13hipblasStrideP10hipComplexi13hipblasStridei)

-
hipblasStatus_t hipblasZtpmvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const hipDoubleComplex *AP,[hipblasStride](#_CPPv413hipblasStride)strideA, hipDoubleComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount)[#](#_CPPv426hipblasZtpmvStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiPK16hipDoubleComplex13hipblasStrideP16hipDoubleComplexi13hipblasStridei) BLAS Level 2 API.

tpmvStridedBatched performs one of the matrix-vector operations

where x_i is an n element vector and A_i is an n by n (unit, or non-unit, upper or lower triangular matrix) with strides specifying how to retrieve $x_i$ (resp. $A_i$) from $x_{i-1}$ (resp. $A_i$).x_i = A_i*x_i or x_i = A**T*x_i, 0 \le i < batchCount

The vectors x_i are overwritten.

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: A_i is an upper triangular matrix. HIPBLAS_FILL_MODE_LOWER: A_i is a lower triangular matrix.**transA**–**[in]**[hipblasOperation_t]**diag**–**[in]**[hipblasDiagType_t] HIPBLAS_DIAG_UNIT: A_i is assumed to be unit triangular. HIPBLAS_DIAG_NON_UNIT: A_i is not assumed to be unit triangular.**n**–**[in]**[int] n specifies the number of rows of matrices A_i. n >= 0.**AP**–**[in]**device pointer of the matrix A_0, of dimension ( lda, n )**strideA**–**[in]**[hipblasStride] stride from the start of one A_i matrix to the next A_{i + 1}**x**–**[in]**device pointer storing the vector x_0.**incx**–**[in]**[int] specifies the increment for the elements of one vector x.**stridex**–**[in]**[hipblasStride] stride from the start of one x_i vector to the next x_{i + 1}**batchCount**–**[in]**[int] The number of batched matrices/vectors.



The `tpmvStridedBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasStpsv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const float *AP, float *x, int incx)[#](#_CPPv412hipblasStpsv15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiPKfPfi)

-
hipblasStatus_t hipblasDtpsv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const double *AP, double *x, int incx)[#](#_CPPv412hipblasDtpsv15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiPKdPdi)

-
hipblasStatus_t hipblasCtpsv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const hipComplex *AP, hipComplex *x, int incx)[#](#_CPPv412hipblasCtpsv15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiPK10hipComplexP10hipComplexi)

-
hipblasStatus_t hipblasZtpsv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const hipDoubleComplex *AP, hipDoubleComplex *x, int incx)[#](#_CPPv412hipblasZtpsv15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiPK16hipDoubleComplexP16hipDoubleComplexi) BLAS Level 2 API.

tpsv solves

where x and b are vectors and A is a triangular matrix stored in the packed format.A*x = b or A**T*x = b, or A**H*x = b,

The input vector b is overwritten by the output vector x.

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : s,d,c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: A is an upper triangular matrix. HIPBLAS_FILL_MODE_LOWER: A is a lower triangular matrix.**transA**–**[in]**[hipblasOperation_t] HIPBLAS_OP_N: Solves A*x = b HIPBLAS_OP_T: Solves A**T*x = b HIPBLAS_OP_C: Solves A**H*x = b**diag**–**[in]**[hipblasDiagType_t] HIPBLAS_DIAG_UNIT: A is assumed to be unit triangular (i.e. the diagonal elements of A are not used in computations). HIPBLAS_DIAG_NON_UNIT: A is not assumed to be unit triangular.**n**–**[in]**[int] n specifies the number of rows of b. n >= 0.**AP**–**[in]**device pointer storing the packed version of matrix A, of dimension >= (n * (n + 1) / 2)**x**–**[inout]**device pointer storing vector b on input, overwritten by x on output.**incx**–**[in]**[int] specifies the increment for the elements of x.



The `tpsv`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasStpsvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const float *const AP[], float *const x[], int incx, int batchCount)[#](#_CPPv419hipblasStpsvBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiA_PCKfA_PCfii)

-
hipblasStatus_t hipblasDtpsvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const double *const AP[], double *const x[], int incx, int batchCount)[#](#_CPPv419hipblasDtpsvBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiA_PCKdA_PCdii)

-
hipblasStatus_t hipblasCtpsvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const hipComplex *const AP[], hipComplex *const x[], int incx, int batchCount)[#](#_CPPv419hipblasCtpsvBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiA_PCK10hipComplexA_PC10hipComplexii)

-
hipblasStatus_t hipblasZtpsvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const hipDoubleComplex *const AP[], hipDoubleComplex *const x[], int incx, int batchCount)[#](#_CPPv419hipblasZtpsvBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiA_PCK16hipDoubleComplexA_PC16hipDoubleComplexii) BLAS Level 2 API.

tpsvBatched solves

where x_i and b_i are vectors and A_i is a triangular matrix stored in the packed format, for i in [1, batchCount].A_i*x_i = b_i or A_i**T*x_i = b_i, or A_i**H*x_i = b_i,

The input vectors b_i are overwritten by the output vectors x_i.

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: each A_i is an upper triangular matrix. HIPBLAS_FILL_MODE_LOWER: each A_i is a lower triangular matrix.**transA**–**[in]**[hipblasOperation_t] HIPBLAS_OP_N: Solves A*x = b HIPBLAS_OP_T: Solves A**T*x = b HIPBLAS_OP_C: Solves A**H*x = b**diag**–**[in]**[hipblasDiagType_t] HIPBLAS_DIAG_UNIT: each A_i is assumed to be unit triangular (i.e. the diagonal elements of each A_i are not used in computations). HIPBLAS_DIAG_NON_UNIT: each A_i is not assumed to be unit triangular.**n**–**[in]**[int] n specifies the number of rows of each b_i. n >= 0.**AP**–**[in]**device array of device pointers storing the packed versions of each matrix A_i, of dimension >= (n * (n + 1) / 2)**x**–**[inout]**device array of device pointers storing each input vector b_i, overwritten by x_i on output.**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**batchCount**–**[in]**[int] specifies the number of instances in the batch.



The `tpsvBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasStpsvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const float *AP,[hipblasStride](#_CPPv413hipblasStride)strideA, float *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount)[#](#_CPPv426hipblasStpsvStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiPKf13hipblasStridePfi13hipblasStridei)

-
hipblasStatus_t hipblasDtpsvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const double *AP,[hipblasStride](#_CPPv413hipblasStride)strideA, double *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount)[#](#_CPPv426hipblasDtpsvStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiPKd13hipblasStridePdi13hipblasStridei)

-
hipblasStatus_t hipblasCtpsvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const hipComplex *AP,[hipblasStride](#_CPPv413hipblasStride)strideA, hipComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount)[#](#_CPPv426hipblasCtpsvStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiPK10hipComplex13hipblasStrideP10hipComplexi13hipblasStridei)

-
hipblasStatus_t hipblasZtpsvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const hipDoubleComplex *AP,[hipblasStride](#_CPPv413hipblasStride)strideA, hipDoubleComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount)[#](#_CPPv426hipblasZtpsvStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiPK16hipDoubleComplex13hipblasStrideP16hipDoubleComplexi13hipblasStridei) BLAS Level 2 API.

tpsvStridedBatched solves

where x_i and b_i are vectors and A_i is a triangular matrix stored in the packed format, for i in [1, batchCount].A_i*x_i = b_i or A_i**T*x_i = b_i, or A_i**H*x_i = b_i,

The input vectors b_i are overwritten by the output vectors x_i.

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: each A_i is an upper triangular matrix. HIPBLAS_FILL_MODE_LOWER: each A_i is a lower triangular matrix.**transA**–**[in]**[hipblasOperation_t] HIPBLAS_OP_N: Solves A*x = b HIPBLAS_OP_T: Solves A**T*x = b HIPBLAS_OP_C: Solves A**H*x = b**diag**–**[in]**[hipblasDiagType_t] HIPBLAS_DIAG_UNIT: each A_i is assumed to be unit triangular (i.e. the diagonal elements of each A_i are not used in computations). HIPBLAS_DIAG_NON_UNIT: each A_i is not assumed to be unit triangular.**n**–**[in]**[int] n specifies the number of rows of each b_i. n >= 0.**AP**–**[in]**device pointer pointing to the first packed matrix A_1, of dimension >= (n * (n + 1) / 2)**strideA**–**[in]**[hipblasStride] stride from the beginning of one packed matrix (AP_i) and the next (AP_i+1).**x**–**[inout]**device pointer pointing to the first input vector b_1. Overwritten by each x_i on output.**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**stridex**–**[in]**[hipblasStride] stride from the beginning of one vector (x_i) and the next (x_i+1).**batchCount**–**[in]**[int] specifies the number of instances in the batch.



The `tpsvStridedBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasStrmv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const float *AP, int lda, float *x, int incx)[#](#_CPPv412hipblasStrmv15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiPKfiPfi)

-
hipblasStatus_t hipblasDtrmv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const double *AP, int lda, double *x, int incx)[#](#_CPPv412hipblasDtrmv15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiPKdiPdi)

-
hipblasStatus_t hipblasCtrmv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const hipComplex *AP, int lda, hipComplex *x, int incx)[#](#_CPPv412hipblasCtrmv15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiPK10hipComplexiP10hipComplexi)

-
hipblasStatus_t hipblasZtrmv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const hipDoubleComplex *AP, int lda, hipDoubleComplex *x, int incx)[#](#_CPPv412hipblasZtrmv15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiPK16hipDoubleComplexiP16hipDoubleComplexi) BLAS Level 2 API.

trmv performs one of the matrix-vector operations

where x is an n element vector and A is an n by n unit, or non-unit, upper or lower triangular matrix.x = A*x or x = A**T*x,

The vector x is overwritten.

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : s,d,c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: A is an upper triangular matrix. HIPBLAS_FILL_MODE_LOWER: A is a lower triangular matrix.**transA**–**[in]**[hipblasOperation_t]**diag**–**[in]**[hipblasDiagType_t] HIPBLAS_DIAG_UNIT: A is assumed to be unit triangular. HIPBLAS_DIAG_NON_UNIT: A is not assumed to be unit triangular.**n**–**[in]**[int] n specifies the number of rows of A. n >= 0.**AP**–**[in]**device pointer storing matrix A, of dimension ( lda, n )**lda**–**[in]**[int] specifies the leading dimension of A. lda = max( 1, n ).**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[int] specifies the increment for the elements of x.



The `trmv`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasStrmvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const float *const AP[], int lda, float *const x[], int incx, int batchCount)[#](#_CPPv419hipblasStrmvBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiA_PCKfiA_PCfii)

-
hipblasStatus_t hipblasDtrmvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const double *const AP[], int lda, double *const x[], int incx, int batchCount)[#](#_CPPv419hipblasDtrmvBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiA_PCKdiA_PCdii)

-
hipblasStatus_t hipblasCtrmvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const hipComplex *const AP[], int lda, hipComplex *const x[], int incx, int batchCount)[#](#_CPPv419hipblasCtrmvBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiA_PCK10hipComplexiA_PC10hipComplexii)

-
hipblasStatus_t hipblasZtrmvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const hipDoubleComplex *const AP[], int lda, hipDoubleComplex *const x[], int incx, int batchCount)[#](#_CPPv419hipblasZtrmvBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiA_PCK16hipDoubleComplexiA_PC16hipDoubleComplexii) BLAS Level 2 API.

trmvBatched performs one of the matrix-vector operations

where x_i is an n element vector and A_i is an n by n (unit, or non-unit, upper or lower triangular matrix)x_i = A_i*x_i or x_i = A**T*x_i, 0 \le i < batchCount

The vectors x_i are overwritten.

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: A_i is an upper triangular matrix. HIPBLAS_FILL_MODE_LOWER: A_i is a lower triangular matrix.**transA**–**[in]**[hipblasOperation_t]**diag**–**[in]**[hipblasDiagType_t] HIPBLAS_DIAG_UNIT: A_i is assumed to be unit triangular. HIPBLAS_DIAG_NON_UNIT: A_i is not assumed to be unit triangular.**n**–**[in]**[int] n specifies the number of rows of matrices A_i. n >= 0.**AP**–**[in]**device pointer storing pointer of matrices A_i, of dimension ( lda, n )**lda**–**[in]**[int] specifies the leading dimension of A_i. lda >= max( 1, n ).**x**–**[in]**device pointer storing vectors x_i.**incx**–**[in]**[int] specifies the increment for the elements of vectors x_i.**batchCount**–**[in]**[int] The number of batched matrices/vectors.



The `trmvBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasStrmvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const float *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, float *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount)[#](#_CPPv426hipblasStrmvStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiPKfi13hipblasStridePfi13hipblasStridei)

-
hipblasStatus_t hipblasDtrmvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const double *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, double *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount)[#](#_CPPv426hipblasDtrmvStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiPKdi13hipblasStridePdi13hipblasStridei)

-
hipblasStatus_t hipblasCtrmvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const hipComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, hipComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount)[#](#_CPPv426hipblasCtrmvStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiPK10hipComplexi13hipblasStrideP10hipComplexi13hipblasStridei)

-
hipblasStatus_t hipblasZtrmvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const hipDoubleComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, hipDoubleComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount)[#](#_CPPv426hipblasZtrmvStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiPK16hipDoubleComplexi13hipblasStrideP16hipDoubleComplexi13hipblasStridei) BLAS Level 2 API.

trmvStridedBatched performs one of the matrix-vector operations

where x_i is an n element vector and A_i is an n by n (unit, or non-unit, upper or lower triangular matrix) with strides specifying how to retrieve $x_i$ (resp. $A_i$) from $x_{i-1}$ (resp. $A_i$).x_i = A_i*x_i or x_i = A**T*x_i, 0 \le i < batchCount

The vectors x_i are overwritten.

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: A_i is an upper triangular matrix. HIPBLAS_FILL_MODE_LOWER: A_i is a lower triangular matrix.**transA**–**[in]**[hipblasOperation_t]**diag**–**[in]**[hipblasDiagType_t] HIPBLAS_DIAG_UNIT: A_i is assumed to be unit triangular. HIPBLAS_DIAG_NON_UNIT: A_i is not assumed to be unit triangular.**n**–**[in]**[int] n specifies the number of rows of matrices A_i. n >= 0.**AP**–**[in]**device pointer of the matrix A_0, of dimension ( lda, n )**lda**–**[in]**[int] specifies the leading dimension of A_i. lda >= max( 1, n ).**strideA**–**[in]**[hipblasStride] stride from the start of one A_i matrix to the next A_{i + 1}**x**–**[in]**device pointer storing the vector x_0.**incx**–**[in]**[int] specifies the increment for the elements of one vector x.**stridex**–**[in]**[hipblasStride] stride from the start of one x_i vector to the next x_{i + 1}**batchCount**–**[in]**[int] The number of batched matrices/vectors.



The `trmvStridedBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasStrsv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const float *AP, int lda, float *x, int incx)[#](#_CPPv412hipblasStrsv15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiPKfiPfi)

-
hipblasStatus_t hipblasDtrsv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const double *AP, int lda, double *x, int incx)[#](#_CPPv412hipblasDtrsv15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiPKdiPdi)

-
hipblasStatus_t hipblasCtrsv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const hipComplex *AP, int lda, hipComplex *x, int incx)[#](#_CPPv412hipblasCtrsv15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiPK10hipComplexiP10hipComplexi)

-
hipblasStatus_t hipblasZtrsv(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const hipDoubleComplex *AP, int lda, hipDoubleComplex *x, int incx)[#](#_CPPv412hipblasZtrsv15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiPK16hipDoubleComplexiP16hipDoubleComplexi) BLAS Level 2 API.

trsv solves

where x and b are vectors and A is a triangular matrix.A*x = b or A**T*x = b,

The vector x is overwritten on b.

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : s,d,c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: A is an upper triangular matrix. HIPBLAS_FILL_MODE_LOWER: A is a lower triangular matrix.**transA**–**[in]**[hipblasOperation_t]**diag**–**[in]**[hipblasDiagType_t] HIPBLAS_DIAG_UNIT: A is assumed to be unit triangular. HIPBLAS_DIAG_NON_UNIT: A is not assumed to be unit triangular.**n**–**[in]**[int] n specifies the number of rows of b. n >= 0.**AP**–**[in]**device pointer storing matrix A, of dimension ( lda, n )**lda**–**[in]**[int] specifies the leading dimension of A. lda = max( 1, n ).**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[int] specifies the increment for the elements of x.



The `trsv`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasStrsvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const float *const AP[], int lda, float *const x[], int incx, int batchCount)[#](#_CPPv419hipblasStrsvBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiA_PCKfiA_PCfii)

-
hipblasStatus_t hipblasDtrsvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const double *const AP[], int lda, double *const x[], int incx, int batchCount)[#](#_CPPv419hipblasDtrsvBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiA_PCKdiA_PCdii)

-
hipblasStatus_t hipblasCtrsvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const hipComplex *const AP[], int lda, hipComplex *const x[], int incx, int batchCount)[#](#_CPPv419hipblasCtrsvBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiA_PCK10hipComplexiA_PC10hipComplexii)

-
hipblasStatus_t hipblasZtrsvBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const hipDoubleComplex *const AP[], int lda, hipDoubleComplex *const x[], int incx, int batchCount)[#](#_CPPv419hipblasZtrsvBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiA_PCK16hipDoubleComplexiA_PC16hipDoubleComplexii) BLAS Level 2 API.

trsvBatched solves

where (A_i, x_i, b_i) is the i-th instance of the batch. x_i and b_i are vectors and A_i is an n by n triangular matrix.A_i*x_i = b_i or A_i**T*x_i = b_i,

The vector x is overwritten on b.

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: A is an upper triangular matrix. HIPBLAS_FILL_MODE_LOWER: A is a lower triangular matrix.**transA**–**[in]**[hipblasOperation_t]**diag**–**[in]**[hipblasDiagType_t] HIPBLAS_DIAG_UNIT: A is assumed to be unit triangular. HIPBLAS_DIAG_NON_UNIT: A is not assumed to be unit triangular.**n**–**[in]**[int] n specifies the number of rows of b. n >= 0.**AP**–**[in]**device array of device pointers storing each matrix A_i.**lda**–**[in]**[int] specifies the leading dimension of each A_i. lda = max(1, n)**x**–**[in]**device array of device pointers storing each vector x_i.**incx**–**[in]**[int] specifies the increment for the elements of x.**batchCount**–**[in]**[int] number of instances in the batch



The `trsvBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasStrsvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const float *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, float *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount)[#](#_CPPv426hipblasStrsvStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiPKfi13hipblasStridePfi13hipblasStridei)

-
hipblasStatus_t hipblasDtrsvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const double *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, double *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount)[#](#_CPPv426hipblasDtrsvStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiPKdi13hipblasStridePdi13hipblasStridei)

-
hipblasStatus_t hipblasCtrsvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const hipComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, hipComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount)[#](#_CPPv426hipblasCtrsvStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiPK10hipComplexi13hipblasStrideP10hipComplexi13hipblasStridei)

-
hipblasStatus_t hipblasZtrsvStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const hipDoubleComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, hipDoubleComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount)[#](#_CPPv426hipblasZtrsvStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiPK16hipDoubleComplexi13hipblasStrideP16hipDoubleComplexi13hipblasStridei) BLAS Level 2 API.

trsvStridedBatched solves

where (A_i, x_i, b_i) is the i-th instance of the batch. x_i and b_i are vectors and A_i is an n by n triangular matrix, for i = 1, …, batchCount.A_i*x_i = b_i or A_i**T*x_i = b_i,

The vector x is overwritten on b.

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: A is an upper triangular matrix. HIPBLAS_FILL_MODE_LOWER: A is a lower triangular matrix.**transA**–**[in]**[hipblasOperation_t]**diag**–**[in]**[hipblasDiagType_t] HIPBLAS_DIAG_UNIT: A is assumed to be unit triangular. HIPBLAS_DIAG_NON_UNIT: A is not assumed to be unit triangular.**n**–**[in]**[int] n specifies the number of rows of each b_i. n >= 0.**AP**–**[in]**device pointer to the first matrix (A_1) in the batch, of dimension ( lda, n )**strideA**–**[in]**[hipblasStride] stride from the start of one A_i matrix to the next A_(i + 1)**lda**–**[in]**[int] specifies the leading dimension of each A_i. lda = max( 1, n ).**x**–**[inout]**device pointer to the first vector (x_1) in the batch.**stridex**–**[in]**[hipblasStride] stride from the start of one x_i vector to the next x_(i + 1)**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**batchCount**–**[in]**[int] number of instances in the batch



The `trsvStridedBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

## Level 3 BLAS[#](#level-3-blas)

-
hipblasStatus_t hipblasHgemm(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transB, int m, int n, int k, const[hipblasHalf](#_CPPv411hipblasHalf)*alpha, const[hipblasHalf](#_CPPv411hipblasHalf)*AP, int lda, const[hipblasHalf](#_CPPv411hipblasHalf)*BP, int ldb, const[hipblasHalf](#_CPPv411hipblasHalf)*beta,[hipblasHalf](#_CPPv411hipblasHalf)*CP, int ldc)[#](#_CPPv412hipblasHgemm15hipblasHandle_t18hipblasOperation_t18hipblasOperation_tiiiPK11hipblasHalfPK11hipblasHalfiPK11hipblasHalfiPK11hipblasHalfP11hipblasHalfi)

-
hipblasStatus_t hipblasSgemm(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transB, int m, int n, int k, const float *alpha, const float *AP, int lda, const float *BP, int ldb, const float *beta, float *CP, int ldc)[#](#_CPPv412hipblasSgemm15hipblasHandle_t18hipblasOperation_t18hipblasOperation_tiiiPKfPKfiPKfiPKfPfi)

-
hipblasStatus_t hipblasDgemm(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transB, int m, int n, int k, const double *alpha, const double *AP, int lda, const double *BP, int ldb, const double *beta, double *CP, int ldc)[#](#_CPPv412hipblasDgemm15hipblasHandle_t18hipblasOperation_t18hipblasOperation_tiiiPKdPKdiPKdiPKdPdi)

-
hipblasStatus_t hipblasCgemm(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transB, int m, int n, int k, const hipComplex *alpha, const hipComplex *AP, int lda, const hipComplex *BP, int ldb, const hipComplex *beta, hipComplex *CP, int ldc)[#](#_CPPv412hipblasCgemm15hipblasHandle_t18hipblasOperation_t18hipblasOperation_tiiiPK10hipComplexPK10hipComplexiPK10hipComplexiPK10hipComplexP10hipComplexi)

-
hipblasStatus_t hipblasZgemm(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transB, int m, int n, int k, const hipDoubleComplex *alpha, const hipDoubleComplex *AP, int lda, const hipDoubleComplex *BP, int ldb, const hipDoubleComplex *beta, hipDoubleComplex *CP, int ldc)[#](#_CPPv412hipblasZgemm15hipblasHandle_t18hipblasOperation_t18hipblasOperation_tiiiPK16hipDoubleComplexPK16hipDoubleComplexiPK16hipDoubleComplexiPK16hipDoubleComplexP16hipDoubleComplexi) BLAS Level 3 API.

gemm performs one of the matrix-matrix operations

where op( X ) is one ofC = alpha*op( A )*op( B ) + beta*C,

alpha and beta are scalars, and A, B and C are matrices, with op( A ) an m by k matrix, op( B ) a k by n matrix and C an m by n matrix.op( X ) = X or op( X ) = X**T or op( X ) = X**H,

Supported precisions in rocBLAS : h,s,d,c,z

Supported precisions in cuBLAS : h,s,d,c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t]`.`

**transA**–**[in]**[hipblasOperation_t] specifies the form of op( A )**transB**–**[in]**[hipblasOperation_t] specifies the form of op( B )**m**–**[in]**[int] number or rows of matrices op( A ) and C**n**–**[in]**[int] number of columns of matrices op( B ) and C**k**–**[in]**[int] number of columns of matrix op( A ) and number of rows of matrix op( B )**alpha**–**[in]**device pointer or host pointer specifying the scalar alpha.**AP**–**[in]**device pointer storing matrix A.**lda**–**[in]**[int] specifies the leading dimension of A.**BP**–**[in]**device pointer storing matrix B.**ldb**–**[in]**[int] specifies the leading dimension of B.**beta**–**[in]**device pointer or host pointer specifying the scalar beta.**CP**–**[inout]**device pointer storing matrix C on the GPU.**ldc**–**[in]**[int] specifies the leading dimension of C.



The `gemm`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasHgemmBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transB, int m, int n, int k, const[hipblasHalf](#_CPPv411hipblasHalf)*alpha, const[hipblasHalf](#_CPPv411hipblasHalf)*const AP[], int lda, const[hipblasHalf](#_CPPv411hipblasHalf)*const BP[], int ldb, const[hipblasHalf](#_CPPv411hipblasHalf)*beta,[hipblasHalf](#_CPPv411hipblasHalf)*const CP[], int ldc, int batchCount)[#](#_CPPv419hipblasHgemmBatched15hipblasHandle_t18hipblasOperation_t18hipblasOperation_tiiiPK11hipblasHalfA_PCK11hipblasHalfiA_PCK11hipblasHalfiPK11hipblasHalfA_PC11hipblasHalfii)

-
hipblasStatus_t hipblasSgemmBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transB, int m, int n, int k, const float *alpha, const float *const AP[], int lda, const float *const BP[], int ldb, const float *beta, float *const CP[], int ldc, int batchCount)[#](#_CPPv419hipblasSgemmBatched15hipblasHandle_t18hipblasOperation_t18hipblasOperation_tiiiPKfA_PCKfiA_PCKfiPKfA_PCfii)

-
hipblasStatus_t hipblasDgemmBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transB, int m, int n, int k, const double *alpha, const double *const AP[], int lda, const double *const BP[], int ldb, const double *beta, double *const CP[], int ldc, int batchCount)[#](#_CPPv419hipblasDgemmBatched15hipblasHandle_t18hipblasOperation_t18hipblasOperation_tiiiPKdA_PCKdiA_PCKdiPKdA_PCdii)

-
hipblasStatus_t hipblasCgemmBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transB, int m, int n, int k, const hipComplex *alpha, const hipComplex *const AP[], int lda, const hipComplex *const BP[], int ldb, const hipComplex *beta, hipComplex *const CP[], int ldc, int batchCount)[#](#_CPPv419hipblasCgemmBatched15hipblasHandle_t18hipblasOperation_t18hipblasOperation_tiiiPK10hipComplexA_PCK10hipComplexiA_PCK10hipComplexiPK10hipComplexA_PC10hipComplexii)

-
hipblasStatus_t hipblasZgemmBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transB, int m, int n, int k, const hipDoubleComplex *alpha, const hipDoubleComplex *const AP[], int lda, const hipDoubleComplex *const BP[], int ldb, const hipDoubleComplex *beta, hipDoubleComplex *const CP[], int ldc, int batchCount)[#](#_CPPv419hipblasZgemmBatched15hipblasHandle_t18hipblasOperation_t18hipblasOperation_tiiiPK16hipDoubleComplexA_PCK16hipDoubleComplexiA_PCK16hipDoubleComplexiPK16hipDoubleComplexA_PC16hipDoubleComplexii) BLAS Level 3 API.

gemmBatched performs one of the batched matrix-matrix operations C_i = alpha*op( A_i )*op( B_i ) + beta*C_i, for i = 1, …, batchCount. where op( X ) is one of op( X ) = X or op( X ) = X**T or op( X ) = X**H, alpha and beta are scalars, and A, B and C are strided batched matrices, with op( A ) an m by k by batchCount strided_batched matrix, op( B ) an k by n by batchCount strided_batched matrix and C an m by n by batchCount strided_batched matrix.

Supported precisions in rocBLAS : h,s,d,c,z

Supported precisions in cuBLAS : h,s,d,c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**transA**–**[in]**[hipblasOperation_t] specifies the form of op( A )**transB**–**[in]**[hipblasOperation_t] specifies the form of op( B )**m**–**[in]**[int] matrix dimension m.**n**–**[in]**[int] matrix dimension n.**k**–**[in]**[int] matrix dimension k.**alpha**–**[in]**device pointer or host pointer specifying the scalar alpha.**AP**–**[in]**device array of device pointers storing each matrix A_i.**lda**–**[in]**[int] specifies the leading dimension of each A_i.**BP**–**[in]**device array of device pointers storing each matrix B_i.**ldb**–**[in]**[int] specifies the leading dimension of each B_i.**beta**–**[in]**device pointer or host pointer specifying the scalar beta.**CP**–**[inout]**device array of device pointers storing each matrix C_i.**ldc**–**[in]**[int] specifies the leading dimension of each C_i.**batchCount**–**[in]**[int] number of gemm operations in the batch



The `gemmBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasHgemmStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transB, int m, int n, int k, const[hipblasHalf](#_CPPv411hipblasHalf)*alpha, const[hipblasHalf](#_CPPv411hipblasHalf)*AP, int lda, long long strideA, const[hipblasHalf](#_CPPv411hipblasHalf)*BP, int ldb, long long strideB, const[hipblasHalf](#_CPPv411hipblasHalf)*beta,[hipblasHalf](#_CPPv411hipblasHalf)*CP, int ldc, long long strideC, int batchCount)[#](#_CPPv426hipblasHgemmStridedBatched15hipblasHandle_t18hipblasOperation_t18hipblasOperation_tiiiPK11hipblasHalfPK11hipblasHalfixPK11hipblasHalfixPK11hipblasHalfP11hipblasHalfixi)

-
hipblasStatus_t hipblasSgemmStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transB, int m, int n, int k, const float *alpha, const float *AP, int lda, long long strideA, const float *BP, int ldb, long long strideB, const float *beta, float *CP, int ldc, long long strideC, int batchCount)[#](#_CPPv426hipblasSgemmStridedBatched15hipblasHandle_t18hipblasOperation_t18hipblasOperation_tiiiPKfPKfixPKfixPKfPfixi)

-
hipblasStatus_t hipblasDgemmStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transB, int m, int n, int k, const double *alpha, const double *AP, int lda, long long strideA, const double *BP, int ldb, long long strideB, const double *beta, double *CP, int ldc, long long strideC, int batchCount)[#](#_CPPv426hipblasDgemmStridedBatched15hipblasHandle_t18hipblasOperation_t18hipblasOperation_tiiiPKdPKdixPKdixPKdPdixi)

-
hipblasStatus_t hipblasCgemmStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transB, int m, int n, int k, const hipComplex *alpha, const hipComplex *AP, int lda, long long strideA, const hipComplex *BP, int ldb, long long strideB, const hipComplex *beta, hipComplex *CP, int ldc, long long strideC, int batchCount)[#](#_CPPv426hipblasCgemmStridedBatched15hipblasHandle_t18hipblasOperation_t18hipblasOperation_tiiiPK10hipComplexPK10hipComplexixPK10hipComplexixPK10hipComplexP10hipComplexixi)

-
hipblasStatus_t hipblasZgemmStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transB, int m, int n, int k, const hipDoubleComplex *alpha, const hipDoubleComplex *AP, int lda, long long strideA, const hipDoubleComplex *BP, int ldb, long long strideB, const hipDoubleComplex *beta, hipDoubleComplex *CP, int ldc, long long strideC, int batchCount)[#](#_CPPv426hipblasZgemmStridedBatched15hipblasHandle_t18hipblasOperation_t18hipblasOperation_tiiiPK16hipDoubleComplexPK16hipDoubleComplexixPK16hipDoubleComplexixPK16hipDoubleComplexP16hipDoubleComplexixi) BLAS Level 3 API.

gemmStridedBatched performs one of the strided batched matrix-matrix operations

where op( X ) is one ofC_i = alpha*op( A_i )*op( B_i ) + beta*C_i, for i = 1, ..., batchCount.

alpha and beta are scalars, and A, B and C are strided batched matrices, with op( A ) an m by k by batchCount strided_batched matrix, op( B ) an k by n by batchCount strided_batched matrix and C an m by n by batchCount strided_batched matrix.op( X ) = X or op( X ) = X**T or op( X ) = X**H,

Supported precisions in rocBLAS : h,s,d,c,z

Supported precisions in cuBLAS : h,s,d,c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**transA**–**[in]**[hipblasOperation_t] specifies the form of op( A )**transB**–**[in]**[hipblasOperation_t] specifies the form of op( B )**m**–**[in]**[int] matrix dimension m.**n**–**[in]**[int] matrix dimension n.**k**–**[in]**[int] matrix dimension k.**alpha**–**[in]**device pointer or host pointer specifying the scalar alpha.**AP**–**[in]**device pointer pointing to the first matrix A_1.**lda**–**[in]**[int] specifies the leading dimension of each A_i.**strideA**–**[in]**[hipblasStride] stride from the start of one A_i matrix to the next A_(i + 1).**BP**–**[in]**device pointer pointing to the first matrix B_1.**ldb**–**[in]**[int] specifies the leading dimension of each B_i.**strideB**–**[in]**[hipblasStride] stride from the start of one B_i matrix to the next B_(i + 1).**beta**–**[in]**device pointer or host pointer specifying the scalar beta.**CP**–**[inout]**device pointer pointing to the first matrix C_1.**ldc**–**[in]**[int] specifies the leading dimension of each C_i.**strideC**–**[in]**[hipblasStride] stride from the start of one C_i matrix to the next C_(i + 1).**batchCount**–**[in]**[int] number of gemm operatons in the batch



The `gemmStridedBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasCherk(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const float *alpha, const hipComplex *AP, int lda, const float *beta, hipComplex *CP, int ldc)[#](#_CPPv412hipblasCherk15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPKfPK10hipComplexiPKfP10hipComplexi)

-
hipblasStatus_t hipblasZherk(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const double *alpha, const hipDoubleComplex *AP, int lda, const double *beta, hipDoubleComplex *CP, int ldc)[#](#_CPPv412hipblasZherk15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPKdPK16hipDoubleComplexiPKdP16hipDoubleComplexi) BLAS Level 3 API.

herk performs one of the matrix-matrix operations for a Hermitian rank-k update

C := alpha*op( A )*op( A )^H + beta*C

where alpha and beta are scalars, op(A) is an n by k matrix, and C is a n x n Hermitian matrix stored as either upper or lower.

op( A ) = A, and A is n by k if transA == HIPBLAS_OP_N op( A ) = A^H and A is k by n if transA == HIPBLAS_OP_C

Supported precisions in rocBLAS : c,z

Supported precisions in cuBLAS : c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: C is an upper triangular matrix HIPBLAS_FILL_MODE_LOWER: C is a lower triangular matrix**transA**–**[in]**[hipblasOperation_t] HIPBLAS_OP_C: op(A) = A^H HIPBLAS_ON_N: op(A) = A**n**–**[in]**[int] n specifies the number of rows and columns of C. n >= 0.**k**–**[in]**[int] k specifies the number of columns of op(A). k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A is not referenced and A need not be set before entry.**AP**–**[in]**pointer storing matrix A on the GPU. Martrix dimension is ( lda, k ) when if transA = HIPBLAS_OP_N, otherwise (lda, n) only the upper/lower triangular part is accessed.**lda**–**[in]**[int] lda specifies the first dimension of A. if transA = HIPBLAS_OP_N, lda >= max( 1, n ), otherwise lda >= max( 1, k ).**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**CP**–**[in]**pointer storing matrix C on the GPU. The imaginary component of the diagonal elements are not used but are set to zero unless quick return.**ldc**–**[in]**[int] ldc specifies the first dimension of C. ldc >= max( 1, n ).



The `herk`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasCherkBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const float *alpha, const hipComplex *const AP[], int lda, const float *beta, hipComplex *const CP[], int ldc, int batchCount)[#](#_CPPv419hipblasCherkBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPKfA_PCK10hipComplexiPKfA_PC10hipComplexii)

-
hipblasStatus_t hipblasZherkBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const double *alpha, const hipDoubleComplex *const AP[], int lda, const double *beta, hipDoubleComplex *const CP[], int ldc, int batchCount)[#](#_CPPv419hipblasZherkBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPKdA_PCK16hipDoubleComplexiPKdA_PC16hipDoubleComplexii) BLAS Level 3 API.

herkBatched performs a batch of the matrix-matrix operations for a Hermitian rank-k update

C_i := alpha*op( A_i )*op( A_i )^H + beta*C_i

where alpha and beta are scalars, op(A) is an n by k matrix, and C_i is a n x n Hermitian matrix stored as either upper or lower.

op( A_i ) = A_i, and A_i is n by k if transA == HIPBLAS_OP_N op( A_i ) = A_i^H and A_i is k by n if transA == HIPBLAS_OP_C

Supported precisions in rocBLAS : c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: C_i is an upper triangular matrix HIPBLAS_FILL_MODE_LOWER: C_i is a lower triangular matrix**transA**–**[in]**[hipblasOperation_t] HIPBLAS_OP_C: op(A) = A^H HIPBLAS_OP_N: op(A) = A**n**–**[in]**[int] n specifies the number of rows and columns of C_i. n >= 0.**k**–**[in]**[int] k specifies the number of columns of op(A). k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A is not referenced and A need not be set before entry.**AP**–**[in]**device array of device pointers storing each matrix_i A of dimension (lda, k) when transA is HIPBLAS_OP_N, otherwise of dimension (lda, n)**lda**–**[in]**[int] lda specifies the first dimension of A_i. if transA = HIPBLAS_OP_N, lda >= max( 1, n ), otherwise lda >= max( 1, k ).**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**CP**–**[in]**device array of device pointers storing each matrix C_i on the GPU. The imaginary component of the diagonal elements are not used but are set to zero unless quick return.**ldc**–**[in]**[int] ldc specifies the first dimension of C. ldc >= max( 1, n ).**batchCount**–**[in]**[int] number of instances in the batch.



The `herkBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasCherkStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const float *alpha, const hipComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const float *beta, hipComplex *CP, int ldc,[hipblasStride](#_CPPv413hipblasStride)strideC, int batchCount)[#](#_CPPv426hipblasCherkStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPKfPK10hipComplexi13hipblasStridePKfP10hipComplexi13hipblasStridei)

-
hipblasStatus_t hipblasZherkStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const double *alpha, const hipDoubleComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const double *beta, hipDoubleComplex *CP, int ldc,[hipblasStride](#_CPPv413hipblasStride)strideC, int batchCount)[#](#_CPPv426hipblasZherkStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPKdPK16hipDoubleComplexi13hipblasStridePKdP16hipDoubleComplexi13hipblasStridei) BLAS Level 3 API.

herkStridedBatched performs a batch of the matrix-matrix operations for a Hermitian rank-k update

C_i := alpha*op( A_i )*op( A_i )^H + beta*C_i

where alpha and beta are scalars, op(A) is an n by k matrix, and C_i is a n x n Hermitian matrix stored as either upper or lower.

op( A_i ) = A_i, and A_i is n by k if transA == HIPBLAS_OP_N op( A_i ) = A_i^H and A_i is k by n if transA == HIPBLAS_OP_C

Supported precisions in rocBLAS : c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: C_i is an upper triangular matrix HIPBLAS_FILL_MODE_LOWER: C_i is a lower triangular matrix**transA**–**[in]**[hipblasOperation_t] HIPBLAS_OP_C: op(A) = A^H HIPBLAS_OP_N: op(A) = A**n**–**[in]**[int] n specifies the number of rows and columns of C_i. n >= 0.**k**–**[in]**[int] k specifies the number of columns of op(A). k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A is not referenced and A need not be set before entry.**AP**–**[in]**Device pointer to the first matrix A_1 on the GPU of dimension (lda, k) when transA is HIPBLAS_OP_N, otherwise of dimension (lda, n)**lda**–**[in]**[int] lda specifies the first dimension of A_i. if transA = HIPBLAS_OP_N, lda >= max( 1, n ), otherwise lda >= max( 1, k ).**strideA**–**[in]**[hipblasStride] stride from the start of one matrix (A_i) and the next one (A_i+1)**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**CP**–**[in]**Device pointer to the first matrix C_1 on the GPU. The imaginary component of the diagonal elements are not used but are set to zero unless quick return.**ldc**–**[in]**[int] ldc specifies the first dimension of C. ldc >= max( 1, n ).**strideC**–**[inout]**[hipblasStride] stride from the start of one matrix (C_i) and the next one (C_i+1)**batchCount**–**[in]**[int] number of instances in the batch.



The `herkStridedBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasCherkx(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const hipComplex *alpha, const hipComplex *AP, int lda, const hipComplex *BP, int ldb, const float *beta, hipComplex *CP, int ldc)[#](#_CPPv413hipblasCherkx15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPK10hipComplexPK10hipComplexiPK10hipComplexiPKfP10hipComplexi)

-
hipblasStatus_t hipblasZherkx(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const hipDoubleComplex *alpha, const hipDoubleComplex *AP, int lda, const hipDoubleComplex *BP, int ldb, const double *beta, hipDoubleComplex *CP, int ldc)[#](#_CPPv413hipblasZherkx15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPK16hipDoubleComplexPK16hipDoubleComplexiPK16hipDoubleComplexiPKdP16hipDoubleComplexi) BLAS Level 3 API.

herkx performs one of the matrix-matrix operations for a Hermitian rank-k update

C := alpha*op( A )*op( B )^H + beta*C

where alpha and beta are scalars, op(A) and op(B) are n by k matrices, and C is a n x n Hermitian matrix stored as either upper or lower. This routine should only be used when the caller can guarantee that the result of op( A )*op( B )^T will be Hermitian.

op( A ) = A, op( B ) = B, and A and B are n by k if trans == HIPBLAS_OP_N op( A ) = A^H, op( B ) = B^H, and A and B are k by n if trans == HIPBLAS_OP_C

Supported precisions in rocBLAS : c,z

Supported precisions in cuBLAS : c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: C is an upper triangular matrix HIPBLAS_FILL_MODE_LOWER: C is a lower triangular matrix**transA**–**[in]**[hipblasOperation_t] HIPBLAS_OP_C: op( A ) = A^H, op( B ) = B^H HIPBLAS_OP_N: op( A ) = A, op( B ) = B**n**–**[in]**[int] n specifies the number of rows and columns of C. n >= 0.**k**–**[in]**[int] k specifies the number of columns of op(A). k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A is not referenced and A need not be set before entry.**AP**–**[in]**pointer storing matrix A on the GPU. Martrix dimension is ( lda, k ) when if trans = HIPBLAS_OP_N, otherwise (lda, n) only the upper/lower triangular part is accessed.**lda**–**[in]**[int] lda specifies the first dimension of A. if trans = HIPBLAS_OP_N, lda >= max( 1, n ), otherwise lda >= max( 1, k ).**BP**–**[in]**pointer storing matrix B on the GPU. Martrix dimension is ( ldb, k ) when if trans = HIPBLAS_OP_N, otherwise (ldb, n) only the upper/lower triangular part is accessed.**ldb**–**[in]**[int] ldb specifies the first dimension of B. if trans = HIPBLAS_OP_N, ldb >= max( 1, n ), otherwise ldb >= max( 1, k ).**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**CP**–**[in]**pointer storing matrix C on the GPU. The imaginary component of the diagonal elements are not used but are set to zero unless quick return.**ldc**–**[in]**[int] ldc specifies the first dimension of C. ldc >= max( 1, n ).



The `herkx`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasCherkxBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const hipComplex *alpha, const hipComplex *const AP[], int lda, const hipComplex *const BP[], int ldb, const float *beta, hipComplex *const CP[], int ldc, int batchCount)[#](#_CPPv420hipblasCherkxBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPK10hipComplexA_PCK10hipComplexiA_PCK10hipComplexiPKfA_PC10hipComplexii)

-
hipblasStatus_t hipblasZherkxBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const hipDoubleComplex *alpha, const hipDoubleComplex *const AP[], int lda, const hipDoubleComplex *const BP[], int ldb, const double *beta, hipDoubleComplex *const CP[], int ldc, int batchCount)[#](#_CPPv420hipblasZherkxBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPK16hipDoubleComplexA_PCK16hipDoubleComplexiA_PCK16hipDoubleComplexiPKdA_PC16hipDoubleComplexii) BLAS Level 3 API.

herkxBatched performs a batch of the matrix-matrix operations for a Hermitian rank-k update

C_i := alpha*op( A_i )*op( B_i )^H + beta*C_i

where alpha and beta are scalars, op(A_i) and op(B_i) are n by k matrices, and C_i is a n x n Hermitian matrix stored as either upper or lower. This routine should only be used when the caller can guarantee that the result of op( A )*op( B )^T will be Hermitian.

op( A_i ) = A_i, op( B_i ) = B_i, and A_i and B_i are n by k if trans == HIPBLAS_OP_N op( A_i ) = A_i^H, op( B_i ) = B_i^H, and A_i and B_i are k by n if trans == HIPBLAS_OP_C

Supported precisions in rocBLAS : c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: C_i is an upper triangular matrix HIPBLAS_FILL_MODE_LOWER: C_i is a lower triangular matrix**transA**–**[in]**[hipblasOperation_t] HIPBLAS_OP_C: op(A) = A^H HIPBLAS_OP_N: op(A) = A**n**–**[in]**[int] n specifies the number of rows and columns of C_i. n >= 0.**k**–**[in]**[int] k specifies the number of columns of op(A). k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A is not referenced and A need not be set before entry.**AP**–**[in]**device array of device pointers storing each matrix_i A of dimension (lda, k) when trans is HIPBLAS_OP_N, otherwise of dimension (lda, n)**lda**–**[in]**[int] lda specifies the first dimension of A_i. if trans = HIPBLAS_OP_N, lda >= max( 1, n ), otherwise lda >= max( 1, k ).**BP**–**[in]**device array of device pointers storing each matrix_i B of dimension (ldb, k) when trans is HIPBLAS_OP_N, otherwise of dimension (ldb, n)**ldb**–**[in]**[int] ldb specifies the first dimension of B_i. if trans = HIPBLAS_OP_N, ldb >= max( 1, n ), otherwise ldb >= max( 1, k ).**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**CP**–**[in]**device array of device pointers storing each matrix C_i on the GPU. The imaginary component of the diagonal elements are not used but are set to zero unless quick return.**ldc**–**[in]**[int] ldc specifies the first dimension of C. ldc >= max( 1, n ).**batchCount**–**[in]**[int] number of instances in the batch.



The `herkxBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasCherkxStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const hipComplex *alpha, const hipComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const hipComplex *BP, int ldb,[hipblasStride](#_CPPv413hipblasStride)strideB, const float *beta, hipComplex *CP, int ldc,[hipblasStride](#_CPPv413hipblasStride)strideC, int batchCount)[#](#_CPPv427hipblasCherkxStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPK10hipComplexPK10hipComplexi13hipblasStridePK10hipComplexi13hipblasStridePKfP10hipComplexi13hipblasStridei)

-
hipblasStatus_t hipblasZherkxStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const hipDoubleComplex *alpha, const hipDoubleComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const hipDoubleComplex *BP, int ldb,[hipblasStride](#_CPPv413hipblasStride)strideB, const double *beta, hipDoubleComplex *CP, int ldc,[hipblasStride](#_CPPv413hipblasStride)strideC, int batchCount)[#](#_CPPv427hipblasZherkxStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPK16hipDoubleComplexPK16hipDoubleComplexi13hipblasStridePK16hipDoubleComplexi13hipblasStridePKdP16hipDoubleComplexi13hipblasStridei) BLAS Level 3 API.

herkxStridedBatched performs a batch of the matrix-matrix operations for a Hermitian rank-k update

C_i := alpha*op( A_i )*op( B_i )^H + beta*C_i

where alpha and beta are scalars, op(A_i) and op(B_i) are n by k matrices, and C_i is a n x n Hermitian matrix stored as either upper or lower. This routine should only be used when the caller can guarantee that the result of op( A )*op( B )^T will be Hermitian.

op( A_i ) = A_i, op( B_i ) = B_i, and A_i and B_i are n by k if trans == HIPBLAS_OP_N op( A_i ) = A_i^H, op( B_i ) = B_i^H, and A_i and B_i are k by n if trans == HIPBLAS_OP_C

Supported precisions in rocBLAS : c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: C_i is an upper triangular matrix HIPBLAS_FILL_MODE_LOWER: C_i is a lower triangular matrix**transA**–**[in]**[hipblasOperation_t] HIPBLAS_OP_C: op( A_i ) = A_i^H, op( B_i ) = B_i^H HIPBLAS_OP_N: op( A_i ) = A_i, op( B_i ) = B_i**n**–**[in]**[int] n specifies the number of rows and columns of C_i. n >= 0.**k**–**[in]**[int] k specifies the number of columns of op(A). k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A is not referenced and A need not be set before entry.**AP**–**[in]**Device pointer to the first matrix A_1 on the GPU of dimension (lda, k) when trans is HIPBLAS_OP_N, otherwise of dimension (lda, n)**lda**–**[in]**[int] lda specifies the first dimension of A_i. if trans = HIPBLAS_OP_N, lda >= max( 1, n ), otherwise lda >= max( 1, k ).**strideA**–**[in]**[hipblasStride] stride from the start of one matrix (A_i) and the next one (A_i+1)**BP**–**[in]**Device pointer to the first matrix B_1 on the GPU of dimension (ldb, k) when trans is HIPBLAS_OP_N, otherwise of dimension (ldb, n)**ldb**–**[in]**[int] ldb specifies the first dimension of B_i. if trans = HIPBLAS_OP_N, ldb >= max( 1, n ), otherwise ldb >= max( 1, k ).**strideB**–**[in]**[hipblasStride] stride from the start of one matrix (B_i) and the next one (B_i+1)**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**CP**–**[in]**Device pointer to the first matrix C_1 on the GPU. The imaginary component of the diagonal elements are not used but are set to zero unless quick return.**ldc**–**[in]**[int] ldc specifies the first dimension of C. ldc >= max( 1, n ).**strideC**–**[inout]**[hipblasStride] stride from the start of one matrix (C_i) and the next one (C_i+1)**batchCount**–**[in]**[int] number of instances in the batch.



The `herkxStridedBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasCher2k(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const hipComplex *alpha, const hipComplex *AP, int lda, const hipComplex *BP, int ldb, const float *beta, hipComplex *CP, int ldc)[#](#_CPPv413hipblasCher2k15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPK10hipComplexPK10hipComplexiPK10hipComplexiPKfP10hipComplexi)

-
hipblasStatus_t hipblasZher2k(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const hipDoubleComplex *alpha, const hipDoubleComplex *AP, int lda, const hipDoubleComplex *BP, int ldb, const double *beta, hipDoubleComplex *CP, int ldc)[#](#_CPPv413hipblasZher2k15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPK16hipDoubleComplexPK16hipDoubleComplexiPK16hipDoubleComplexiPKdP16hipDoubleComplexi) BLAS Level 3 API.

her2k performs one of the matrix-matrix operations for a Hermitian rank-2k update

C := alpha*op( A )*op( B )^H + conj(alpha)*op( B )*op( A )^H + beta*C

where alpha and beta are scalars, op(A) and op(B) are n by k matrices, and C is a n x n Hermitian matrix stored as either upper or lower.

op( A ) = A, op( B ) = B, and A and B are n by k if trans == HIPBLAS_OP_N op( A ) = A^H, op( B ) = B^H, and A and B are k by n if trans == HIPBLAS_OP_C

Supported precisions in rocBLAS : c,z

Supported precisions in cuBLAS : c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: C is an upper triangular matrix HIPBLAS_FILL_MODE_LOWER: C is a lower triangular matrix**transA**–**[in]**[hipblasOperation_t] HIPBLAS_OP_C: op( A ) = A^H, op( B ) = B^H HIPBLAS_OP_N: op( A ) = A, op( B ) = B**n**–**[in]**[int] n specifies the number of rows and columns of C. n >= 0.**k**–**[in]**[int] k specifies the number of columns of op(A). k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A is not referenced and A need not be set before entry.**AP**–**[in]**pointer storing matrix A on the GPU. Martrix dimension is ( lda, k ) when if trans = HIPBLAS_OP_N, otherwise (lda, n) only the upper/lower triangular part is accessed.**lda**–**[in]**[int] lda specifies the first dimension of A. if trans = HIPBLAS_OP_N, lda >= max( 1, n ), otherwise lda >= max( 1, k ).**BP**–**[in]**pointer storing matrix B on the GPU. Martrix dimension is ( ldb, k ) when if trans = HIPBLAS_OP_N, otherwise (ldb, n) only the upper/lower triangular part is accessed.**ldb**–**[in]**[int] ldb specifies the first dimension of B. if trans = HIPBLAS_OP_N, ldb >= max( 1, n ), otherwise ldb >= max( 1, k ).**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**CP**–**[in]**pointer storing matrix C on the GPU. The imaginary component of the diagonal elements are not used but are set to zero unless quick return.**ldc**–**[in]**[int] ldc specifies the first dimension of C. ldc >= max( 1, n ).



The `her2k`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasCher2kBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const hipComplex *alpha, const hipComplex *const AP[], int lda, const hipComplex *const BP[], int ldb, const float *beta, hipComplex *const CP[], int ldc, int batchCount)[#](#_CPPv420hipblasCher2kBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPK10hipComplexA_PCK10hipComplexiA_PCK10hipComplexiPKfA_PC10hipComplexii)

-
hipblasStatus_t hipblasZher2kBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const hipDoubleComplex *alpha, const hipDoubleComplex *const AP[], int lda, const hipDoubleComplex *const BP[], int ldb, const double *beta, hipDoubleComplex *const CP[], int ldc, int batchCount)[#](#_CPPv420hipblasZher2kBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPK16hipDoubleComplexA_PCK16hipDoubleComplexiA_PCK16hipDoubleComplexiPKdA_PC16hipDoubleComplexii) BLAS Level 3 API.

her2kBatched performs a batch of the matrix-matrix operations for a Hermitian rank-2k update

C_i := alpha*op( A_i )*op( B_i )^H + conj(alpha)*op( B_i )*op( A_i )^H + beta*C_i

where alpha and beta are scalars, op(A_i) and op(B_i) are n by k matrices, and C_i is a n x n Hermitian matrix stored as either upper or lower.

op( A_i ) = A_i, op( B_i ) = B_i, and A_i and B_i are n by k if trans == HIPBLAS_OP_N op( A_i ) = A_i^H, op( B_i ) = B_i^H, and A_i and B_i are k by n if trans == HIPBLAS_OP_C

Supported precisions in rocBLAS : c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: C_i is an upper triangular matrix HIPBLAS_FILL_MODE_LOWER: C_i is a lower triangular matrix**transA**–**[in]**[hipblasOperation_t] HIPBLAS_OP_C: op(A) = A^H HIPBLAS_OP_N: op(A) = A**n**–**[in]**[int] n specifies the number of rows and columns of C_i. n >= 0.**k**–**[in]**[int] k specifies the number of columns of op(A). k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A is not referenced and A need not be set before entry.**AP**–**[in]**device array of device pointers storing each matrix_i A of dimension (lda, k) when trans is HIPBLAS_OP_N, otherwise of dimension (lda, n)**lda**–**[in]**[int] lda specifies the first dimension of A_i. if trans = HIPBLAS_OP_N, lda >= max( 1, n ), otherwise lda >= max( 1, k ).**BP**–**[in]**device array of device pointers storing each matrix_i B of dimension (ldb, k) when trans is HIPBLAS_OP_N, otherwise of dimension (ldb, n)**ldb**–**[in]**[int] ldb specifies the first dimension of B_i. if trans = HIPBLAS_OP_N, ldb >= max( 1, n ), otherwise ldb >= max( 1, k ).**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**CP**–**[in]**device array of device pointers storing each matrix C_i on the GPU. The imaginary component of the diagonal elements are not used but are set to zero unless quick return.**ldc**–**[in]**[int] ldc specifies the first dimension of C. ldc >= max( 1, n ).**batchCount**–**[in]**[int] number of instances in the batch.



The `her2kBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasCher2kStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const hipComplex *alpha, const hipComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const hipComplex *BP, int ldb,[hipblasStride](#_CPPv413hipblasStride)strideB, const float *beta, hipComplex *CP, int ldc,[hipblasStride](#_CPPv413hipblasStride)strideC, int batchCount)[#](#_CPPv427hipblasCher2kStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPK10hipComplexPK10hipComplexi13hipblasStridePK10hipComplexi13hipblasStridePKfP10hipComplexi13hipblasStridei)

-
hipblasStatus_t hipblasZher2kStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const hipDoubleComplex *alpha, const hipDoubleComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const hipDoubleComplex *BP, int ldb,[hipblasStride](#_CPPv413hipblasStride)strideB, const double *beta, hipDoubleComplex *CP, int ldc,[hipblasStride](#_CPPv413hipblasStride)strideC, int batchCount)[#](#_CPPv427hipblasZher2kStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPK16hipDoubleComplexPK16hipDoubleComplexi13hipblasStridePK16hipDoubleComplexi13hipblasStridePKdP16hipDoubleComplexi13hipblasStridei) BLAS Level 3 API.

her2kStridedBatched performs a batch of the matrix-matrix operations for a Hermitian rank-2k update

C_i := alpha*op( A_i )*op( B_i )^H + conj(alpha)*op( B_i )*op( A_i )^H + beta*C_i

where alpha and beta are scalars, op(A_i) and op(B_i) are n by k matrices, and C_i is a n x n Hermitian matrix stored as either upper or lower.

op( A_i ) = A_i, op( B_i ) = B_i, and A_i and B_i are n by k if trans == HIPBLAS_OP_N op( A_i ) = A_i^H, op( B_i ) = B_i^H, and A_i and B_i are k by n if trans == HIPBLAS_OP_C

Supported precisions in rocBLAS : c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: C_i is an upper triangular matrix HIPBLAS_FILL_MODE_LOWER: C_i is a lower triangular matrix**transA**–**[in]**[hipblasOperation_t] HIPBLAS_OP_C: op( A_i ) = A_i^H, op( B_i ) = B_i^H HIPBLAS_OP_N: op( A_i ) = A_i, op( B_i ) = B_i**n**–**[in]**[int] n specifies the number of rows and columns of C_i. n >= 0.**k**–**[in]**[int] k specifies the number of columns of op(A). k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A is not referenced and A need not be set before entry.**AP**–**[in]**Device pointer to the first matrix A_1 on the GPU of dimension (lda, k) when trans is HIPBLAS_OP_N, otherwise of dimension (lda, n)**lda**–**[in]**[int] lda specifies the first dimension of A_i. if trans = HIPBLAS_OP_N, lda >= max( 1, n ), otherwise lda >= max( 1, k ).**strideA**–**[in]**[hipblasStride] stride from the start of one matrix (A_i) and the next one (A_i+1)**BP**–**[in]**Device pointer to the first matrix B_1 on the GPU of dimension (ldb, k) when trans is HIPBLAS_OP_N, otherwise of dimension (ldb, n)**ldb**–**[in]**[int] ldb specifies the first dimension of B_i. if trans = HIPBLAS_OP_N, ldb >= max( 1, n ), otherwise ldb >= max( 1, k ).**strideB**–**[in]**[hipblasStride] stride from the start of one matrix (B_i) and the next one (B_i+1)**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**CP**–**[in]**Device pointer to the first matrix C_1 on the GPU. The imaginary component of the diagonal elements are not used but are set to zero unless quick return.**ldc**–**[in]**[int] ldc specifies the first dimension of C. ldc >= max( 1, n ).**strideC**–**[inout]**[hipblasStride] stride from the start of one matrix (C_i) and the next one (C_i+1)**batchCount**–**[in]**[int] number of instances in the batch.



The `her2kStridedBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSsymm(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int m, int n, const float *alpha, const float *AP, int lda, const float *BP, int ldb, const float *beta, float *CP, int ldc)[#](#_CPPv412hipblasSsymm15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_tiiPKfPKfiPKfiPKfPfi)

-
hipblasStatus_t hipblasDsymm(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int m, int n, const double *alpha, const double *AP, int lda, const double *BP, int ldb, const double *beta, double *CP, int ldc)[#](#_CPPv412hipblasDsymm15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_tiiPKdPKdiPKdiPKdPdi)

-
hipblasStatus_t hipblasCsymm(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int m, int n, const hipComplex *alpha, const hipComplex *AP, int lda, const hipComplex *BP, int ldb, const hipComplex *beta, hipComplex *CP, int ldc)[#](#_CPPv412hipblasCsymm15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_tiiPK10hipComplexPK10hipComplexiPK10hipComplexiPK10hipComplexP10hipComplexi)

-
hipblasStatus_t hipblasZsymm(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int m, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *AP, int lda, const hipDoubleComplex *BP, int ldb, const hipDoubleComplex *beta, hipDoubleComplex *CP, int ldc)[#](#_CPPv412hipblasZsymm15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_tiiPK16hipDoubleComplexPK16hipDoubleComplexiPK16hipDoubleComplexiPK16hipDoubleComplexP16hipDoubleComplexi) BLAS Level 3 API.

symm performs one of the matrix-matrix operations:

C := alpha*A*B + beta*C if side == HIPBLAS_SIDE_LEFT, C := alpha*B*A + beta*C if side == HIPBLAS_SIDE_RIGHT,

where alpha and beta are scalars, B and C are m by n matrices, and A is a symmetric matrix stored as either upper or lower.

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : s,d,c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**side**–**[in]**[hipblasSideMode_t] HIPBLAS_SIDE_LEFT: C := alpha*A*B + beta*C HIPBLAS_SIDE_RIGHT: C := alpha*B*A + beta*C**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: A is an upper triangular matrix HIPBLAS_FILL_MODE_LOWER: A is a lower triangular matrix**m**–**[in]**[int] m specifies the number of rows of B and C. m >= 0.**n**–**[in]**[int] n specifies the number of columns of B and C. n >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A and B are not referenced.**AP**–**[in]**pointer storing matrix A on the GPU. A is m by m if side == HIPBLAS_SIDE_LEFT A is n by n if side == HIPBLAS_SIDE_RIGHT only the upper/lower triangular part is accessed.**lda**–**[in]**[int] lda specifies the first dimension of A. if side = HIPBLAS_SIDE_LEFT, lda >= max( 1, m ), otherwise lda >= max( 1, n ).**BP**–**[in]**pointer storing matrix B on the GPU. Matrix dimension is m by n**ldb**–**[in]**[int] ldb specifies the first dimension of B. ldb >= max( 1, m )**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**CP**–**[in]**pointer storing matrix C on the GPU. Matrix dimension is m by n**ldc**–**[in]**[int] ldc specifies the first dimension of C. ldc >= max( 1, m )



The `symm`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSsymmBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int m, int n, const float *alpha, const float *const AP[], int lda, const float *const BP[], int ldb, const float *beta, float *const CP[], int ldc, int batchCount)[#](#_CPPv419hipblasSsymmBatched15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_tiiPKfA_PCKfiA_PCKfiPKfA_PCfii)

-
hipblasStatus_t hipblasDsymmBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int m, int n, const double *alpha, const double *const AP[], int lda, const double *const BP[], int ldb, const double *beta, double *const CP[], int ldc, int batchCount)[#](#_CPPv419hipblasDsymmBatched15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_tiiPKdA_PCKdiA_PCKdiPKdA_PCdii)

-
hipblasStatus_t hipblasCsymmBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int m, int n, const hipComplex *alpha, const hipComplex *const AP[], int lda, const hipComplex *const BP[], int ldb, const hipComplex *beta, hipComplex *const CP[], int ldc, int batchCount)[#](#_CPPv419hipblasCsymmBatched15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_tiiPK10hipComplexA_PCK10hipComplexiA_PCK10hipComplexiPK10hipComplexA_PC10hipComplexii)

-
hipblasStatus_t hipblasZsymmBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int m, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *const AP[], int lda, const hipDoubleComplex *const BP[], int ldb, const hipDoubleComplex *beta, hipDoubleComplex *const CP[], int ldc, int batchCount)[#](#_CPPv419hipblasZsymmBatched15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_tiiPK16hipDoubleComplexA_PCK16hipDoubleComplexiA_PCK16hipDoubleComplexiPK16hipDoubleComplexA_PC16hipDoubleComplexii) BLAS Level 3 API.

symmBatched performs a batch of the matrix-matrix operations:

C_i := alpha*A_i*B_i + beta*C_i if side == HIPBLAS_SIDE_LEFT, C_i := alpha*B_i*A_i + beta*C_i if side == HIPBLAS_SIDE_RIGHT,

where alpha and beta are scalars, B_i and C_i are m by n matrices, and A_i is a symmetric matrix stored as either upper or lower.

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**side**–**[in]**[hipblasSideMode_t] HIPBLAS_SIDE_LEFT: C_i := alpha*A_i*B_i + beta*C_i HIPBLAS_SIDE_RIGHT: C_i := alpha*B_i*A_i + beta*C_i**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: A_i is an upper triangular matrix HIPBLAS_FILL_MODE_LOWER: A_i is a lower triangular matrix**m**–**[in]**[int] m specifies the number of rows of B_i and C_i. m >= 0.**n**–**[in]**[int] n specifies the number of columns of B_i and C_i. n >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A_i and B_i are not referenced.**AP**–**[in]**device array of device pointers storing each matrix A_i on the GPU. A_i is m by m if side == HIPBLAS_SIDE_LEFT A_i is n by n if side == HIPBLAS_SIDE_RIGHT only the upper/lower triangular part is accessed.**lda**–**[in]**[int] lda specifies the first dimension of A_i. if side = HIPBLAS_SIDE_LEFT, lda >= max( 1, m ), otherwise lda >= max( 1, n ).**BP**–**[in]**device array of device pointers storing each matrix B_i on the GPU. Matrix dimension is m by n**ldb**–**[in]**[int] ldb specifies the first dimension of B_i. ldb >= max( 1, m )**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C_i need not be set before entry.**CP**–**[in]**device array of device pointers storing each matrix C_i on the GPU. Matrix dimension is m by n**ldc**–**[in]**[int] ldc specifies the first dimension of C_i. ldc >= max( 1, m )**batchCount**–**[in]**[int] number of instances in the batch.



The `symmBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSsymmStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int m, int n, const float *alpha, const float *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const float *BP, int ldb,[hipblasStride](#_CPPv413hipblasStride)strideB, const float *beta, float *CP, int ldc,[hipblasStride](#_CPPv413hipblasStride)strideC, int batchCount)[#](#_CPPv426hipblasSsymmStridedBatched15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_tiiPKfPKfi13hipblasStridePKfi13hipblasStridePKfPfi13hipblasStridei)

-
hipblasStatus_t hipblasDsymmStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int m, int n, const double *alpha, const double *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const double *BP, int ldb,[hipblasStride](#_CPPv413hipblasStride)strideB, const double *beta, double *CP, int ldc,[hipblasStride](#_CPPv413hipblasStride)strideC, int batchCount)[#](#_CPPv426hipblasDsymmStridedBatched15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_tiiPKdPKdi13hipblasStridePKdi13hipblasStridePKdPdi13hipblasStridei)

-
hipblasStatus_t hipblasCsymmStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int m, int n, const hipComplex *alpha, const hipComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const hipComplex *BP, int ldb,[hipblasStride](#_CPPv413hipblasStride)strideB, const hipComplex *beta, hipComplex *CP, int ldc,[hipblasStride](#_CPPv413hipblasStride)strideC, int batchCount)[#](#_CPPv426hipblasCsymmStridedBatched15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_tiiPK10hipComplexPK10hipComplexi13hipblasStridePK10hipComplexi13hipblasStridePK10hipComplexP10hipComplexi13hipblasStridei)

-
hipblasStatus_t hipblasZsymmStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int m, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const hipDoubleComplex *BP, int ldb,[hipblasStride](#_CPPv413hipblasStride)strideB, const hipDoubleComplex *beta, hipDoubleComplex *CP, int ldc,[hipblasStride](#_CPPv413hipblasStride)strideC, int batchCount)[#](#_CPPv426hipblasZsymmStridedBatched15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_tiiPK16hipDoubleComplexPK16hipDoubleComplexi13hipblasStridePK16hipDoubleComplexi13hipblasStridePK16hipDoubleComplexP16hipDoubleComplexi13hipblasStridei) BLAS Level 3 API.

symmStridedBatched performs a batch of the matrix-matrix operations:

C_i := alpha*A_i*B_i + beta*C_i if side == HIPBLAS_SIDE_LEFT, C_i := alpha*B_i*A_i + beta*C_i if side == HIPBLAS_SIDE_RIGHT,

where alpha and beta are scalars, B_i and C_i are m by n matrices, and A_i is a symmetric matrix stored as either upper or lower.

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**side**–**[in]**[hipblasSideMode_t] HIPBLAS_SIDE_LEFT: C_i := alpha*A_i*B_i + beta*C_i HIPBLAS_SIDE_RIGHT: C_i := alpha*B_i*A_i + beta*C_i**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: A_i is an upper triangular matrix HIPBLAS_FILL_MODE_LOWER: A_i is a lower triangular matrix**m**–**[in]**[int] m specifies the number of rows of B_i and C_i. m >= 0.**n**–**[in]**[int] n specifies the number of columns of B_i and C_i. n >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A_i and B_i are not referenced.**AP**–**[in]**device pointer to first matrix A_1 A_i is m by m if side == HIPBLAS_SIDE_LEFT A_i is n by n if side == HIPBLAS_SIDE_RIGHT only the upper/lower triangular part is accessed.**lda**–**[in]**[int] lda specifies the first dimension of A_i. if side = HIPBLAS_SIDE_LEFT, lda >= max( 1, m ), otherwise lda >= max( 1, n ).**strideA**–**[in]**[hipblasStride] stride from the start of one matrix (A_i) and the next one (A_i+1)**BP**–**[in]**device pointer to first matrix B_1 of dimension (ldb, n) on the GPU.**ldb**–**[in]**[int] ldb specifies the first dimension of B_i. ldb >= max( 1, m )**strideB**–**[in]**[hipblasStride] stride from the start of one matrix (B_i) and the next one (B_i+1)**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**CP**–**[in]**device pointer to first matrix C_1 of dimension (ldc, n) on the GPU.**ldc**–**[in]**[int] ldc specifies the first dimension of C. ldc >= max( 1, m ).**strideC**–**[inout]**[hipblasStride] stride from the start of one matrix (C_i) and the next one (C_i+1)**batchCount**–**[in]**[int] number of instances in the batch.



The `symmStridedBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSsyrk(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const float *alpha, const float *AP, int lda, const float *beta, float *CP, int ldc)[#](#_CPPv412hipblasSsyrk15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPKfPKfiPKfPfi)

-
hipblasStatus_t hipblasDsyrk(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const double *alpha, const double *AP, int lda, const double *beta, double *CP, int ldc)[#](#_CPPv412hipblasDsyrk15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPKdPKdiPKdPdi)

-
hipblasStatus_t hipblasCsyrk(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const hipComplex *alpha, const hipComplex *AP, int lda, const hipComplex *beta, hipComplex *CP, int ldc)[#](#_CPPv412hipblasCsyrk15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPK10hipComplexPK10hipComplexiPK10hipComplexP10hipComplexi)

-
hipblasStatus_t hipblasZsyrk(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const hipDoubleComplex *alpha, const hipDoubleComplex *AP, int lda, const hipDoubleComplex *beta, hipDoubleComplex *CP, int ldc)[#](#_CPPv412hipblasZsyrk15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPK16hipDoubleComplexPK16hipDoubleComplexiPK16hipDoubleComplexP16hipDoubleComplexi) BLAS Level 3 API.

syrk performs one of the matrix-matrix operations for a symmetric rank-k update

C := alpha*op( A )*op( A )^T + beta*C

where alpha and beta are scalars, op(A) is an n by k matrix, and C is a symmetric n x n matrix stored as either upper or lower.

op( A ) = A, and A is n by k if transA == HIPBLAS_OP_N op( A ) = A^T and A is k by n if transA == HIPBLAS_OP_T

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : s,d,c,z


HIPBLAS_OP_C is not supported for complex types, see cherk and zherk.

- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: C is an upper triangular matrix HIPBLAS_FILL_MODE_LOWER: C is a lower triangular matrix**transA**–**[in]**[hipblasOperation_t] HIPBLAS_OP_T: op(A) = A^T HIPBLAS_OP_N: op(A) = A HIPBLAS_OP_C: op(A) = A^T**n**–**[in]**[int] n specifies the number of rows and columns of C. n >= 0.**k**–**[in]**[int] k specifies the number of columns of op(A). k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A is not referenced and A need not be set before entry.**AP**–**[in]**pointer storing matrix A on the GPU. Martrix dimension is ( lda, k ) when if transA = HIPBLAS_OP_N, otherwise (lda, n) only the upper/lower triangular part is accessed.**lda**–**[in]**[int] lda specifies the first dimension of A. if transA = HIPBLAS_OP_N, lda >= max( 1, n ), otherwise lda >= max( 1, k ).**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**CP**–**[in]**pointer storing matrix C on the GPU.**ldc**–**[in]**[int] ldc specifies the first dimension of C. ldc >= max( 1, n ).



The `syrk`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSsyrkBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const float *alpha, const float *const AP[], int lda, const float *beta, float *const CP[], int ldc, int batchCount)[#](#_CPPv419hipblasSsyrkBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPKfA_PCKfiPKfA_PCfii)

-
hipblasStatus_t hipblasDsyrkBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const double *alpha, const double *const AP[], int lda, const double *beta, double *const CP[], int ldc, int batchCount)[#](#_CPPv419hipblasDsyrkBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPKdA_PCKdiPKdA_PCdii)

-
hipblasStatus_t hipblasCsyrkBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const hipComplex *alpha, const hipComplex *const AP[], int lda, const hipComplex *beta, hipComplex *const CP[], int ldc, int batchCount)[#](#_CPPv419hipblasCsyrkBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPK10hipComplexA_PCK10hipComplexiPK10hipComplexA_PC10hipComplexii)

-
hipblasStatus_t hipblasZsyrkBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const hipDoubleComplex *alpha, const hipDoubleComplex *const AP[], int lda, const hipDoubleComplex *beta, hipDoubleComplex *const CP[], int ldc, int batchCount)[#](#_CPPv419hipblasZsyrkBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPK16hipDoubleComplexA_PCK16hipDoubleComplexiPK16hipDoubleComplexA_PC16hipDoubleComplexii) BLAS Level 3 API.

syrkBatched performs a batch of the matrix-matrix operations for a symmetric rank-k update

C_i := alpha*op( A_i )*op( A_i )^T + beta*C_i

where alpha and beta are scalars, op(A_i) is an n by k matrix, and C_i is a symmetric n x n matrix stored as either upper or lower.

op( A_i ) = A_i, and A_i is n by k if transA == HIPBLAS_OP_N op( A_i ) = A_i^T and A_i is k by n if transA == HIPBLAS_OP_T

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


HIPBLAS_OP_C is not supported for complex types, see cherk and zherk.

- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: C_i is an upper triangular matrix HIPBLAS_FILL_MODE_LOWER: C_i is a lower triangular matrix**transA**–**[in]**[hipblasOperation_t] HIPBLAS_OP_T: op(A) = A^T HIPBLAS_OP_N: op(A) = A HIPBLAS_OP_C: op(A) = A^T**n**–**[in]**[int] n specifies the number of rows and columns of C_i. n >= 0.**k**–**[in]**[int] k specifies the number of columns of op(A). k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A is not referenced and A need not be set before entry.**AP**–**[in]**device array of device pointers storing each matrix_i A of dimension (lda, k) when transA is HIPBLAS_OP_N, otherwise of dimension (lda, n)**lda**–**[in]**[int] lda specifies the first dimension of A_i. if transA = HIPBLAS_OP_N, lda >= max( 1, n ), otherwise lda >= max( 1, k ).**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**CP**–**[in]**device array of device pointers storing each matrix C_i on the GPU.**ldc**–**[in]**[int] ldc specifies the first dimension of C. ldc >= max( 1, n ).**batchCount**–**[in]**[int] number of instances in the batch.



The `syrkBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSsyrkStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const float *alpha, const float *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const float *beta, float *CP, int ldc,[hipblasStride](#_CPPv413hipblasStride)strideC, int batchCount)[#](#_CPPv426hipblasSsyrkStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPKfPKfi13hipblasStridePKfPfi13hipblasStridei)

-
hipblasStatus_t hipblasDsyrkStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const double *alpha, const double *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const double *beta, double *CP, int ldc,[hipblasStride](#_CPPv413hipblasStride)strideC, int batchCount)[#](#_CPPv426hipblasDsyrkStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPKdPKdi13hipblasStridePKdPdi13hipblasStridei)

-
hipblasStatus_t hipblasCsyrkStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const hipComplex *alpha, const hipComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const hipComplex *beta, hipComplex *CP, int ldc,[hipblasStride](#_CPPv413hipblasStride)strideC, int batchCount)[#](#_CPPv426hipblasCsyrkStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPK10hipComplexPK10hipComplexi13hipblasStridePK10hipComplexP10hipComplexi13hipblasStridei)

-
hipblasStatus_t hipblasZsyrkStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const hipDoubleComplex *alpha, const hipDoubleComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const hipDoubleComplex *beta, hipDoubleComplex *CP, int ldc,[hipblasStride](#_CPPv413hipblasStride)strideC, int batchCount)[#](#_CPPv426hipblasZsyrkStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPK16hipDoubleComplexPK16hipDoubleComplexi13hipblasStridePK16hipDoubleComplexP16hipDoubleComplexi13hipblasStridei) BLAS Level 3 API.

syrkStridedBatched performs a batch of the matrix-matrix operations for a symmetric rank-k update

C_i := alpha*op( A_i )*op( A_i )^T + beta*C_i

where alpha and beta are scalars, op(A_i) is an n by k matrix, and C_i is a symmetric n x n matrix stored as either upper or lower.

op( A_i ) = A_i, and A_i is n by k if transA == HIPBLAS_OP_N op( A_i ) = A_i^T and A_i is k by n if transA == HIPBLAS_OP_T

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


HIPBLAS_OP_C is not supported for complex types, see cherk and zherk.

- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: C_i is an upper triangular matrix HIPBLAS_FILL_MODE_LOWER: C_i is a lower triangular matrix**transA**–**[in]**[hipblasOperation_t] HIPBLAS_OP_T: op(A) = A^T HIPBLAS_OP_N: op(A) = A HIPBLAS_OP_C: op(A) = A^T**n**–**[in]**[int] n specifies the number of rows and columns of C_i. n >= 0.**k**–**[in]**[int] k specifies the number of columns of op(A). k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A is not referenced and A need not be set before entry.**AP**–**[in]**Device pointer to the first matrix A_1 on the GPU of dimension (lda, k) when transA is HIPBLAS_OP_N, otherwise of dimension (lda, n)**lda**–**[in]**[int] lda specifies the first dimension of A_i. if transA = HIPBLAS_OP_N, lda >= max( 1, n ), otherwise lda >= max( 1, k ).**strideA**–**[in]**[hipblasStride] stride from the start of one matrix (A_i) and the next one (A_i+1)**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**CP**–**[in]**Device pointer to the first matrix C_1 on the GPU. on the GPU.**ldc**–**[in]**[int] ldc specifies the first dimension of C. ldc >= max( 1, n ).**strideC**–**[inout]**[hipblasStride] stride from the start of one matrix (C_i) and the next one (C_i+1)**batchCount**–**[in]**[int] number of instances in the batch.



The `syrkStridedBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSsyr2k(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const float *alpha, const float *AP, int lda, const float *BP, int ldb, const float *beta, float *CP, int ldc)[#](#_CPPv413hipblasSsyr2k15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPKfPKfiPKfiPKfPfi)

-
hipblasStatus_t hipblasDsyr2k(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const double *alpha, const double *AP, int lda, const double *BP, int ldb, const double *beta, double *CP, int ldc)[#](#_CPPv413hipblasDsyr2k15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPKdPKdiPKdiPKdPdi)

-
hipblasStatus_t hipblasCsyr2k(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const hipComplex *alpha, const hipComplex *AP, int lda, const hipComplex *BP, int ldb, const hipComplex *beta, hipComplex *CP, int ldc)[#](#_CPPv413hipblasCsyr2k15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPK10hipComplexPK10hipComplexiPK10hipComplexiPK10hipComplexP10hipComplexi)

-
hipblasStatus_t hipblasZsyr2k(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const hipDoubleComplex *alpha, const hipDoubleComplex *AP, int lda, const hipDoubleComplex *BP, int ldb, const hipDoubleComplex *beta, hipDoubleComplex *CP, int ldc)[#](#_CPPv413hipblasZsyr2k15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPK16hipDoubleComplexPK16hipDoubleComplexiPK16hipDoubleComplexiPK16hipDoubleComplexP16hipDoubleComplexi) BLAS Level 3 API.

syr2k performs one of the matrix-matrix operations for a symmetric rank-2k update

C := alpha*(op( A )*op( B )^T + op( B )*op( A )^T) + beta*C

where alpha and beta are scalars, op(A) and op(B) are n by k matrix, and C is a symmetric n x n matrix stored as either upper or lower.

op( A ) = A, op( B ) = B, and A and B are n by k if trans == HIPBLAS_OP_N op( A ) = A^T, op( B ) = B^T, and A and B are k by n if trans == HIPBLAS_OP_T

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : s,d,c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: C is an upper triangular matrix HIPBLAS_FILL_MODE_LOWER: C is a lower triangular matrix**transA**–**[in]**[hipblasOperation_t] HIPBLAS_OP_T: op( A ) = A^T, op( B ) = B^T HIPBLAS_OP_N: op( A ) = A, op( B ) = B**n**–**[in]**[int] n specifies the number of rows and columns of C. n >= 0.**k**–**[in]**[int] k specifies the number of columns of op(A) and op(B). k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A is not referenced and A need not be set before entry.**AP**–**[in]**pointer storing matrix A on the GPU. Martrix dimension is ( lda, k ) when if trans = HIPBLAS_OP_N, otherwise (lda, n) only the upper/lower triangular part is accessed.**lda**–**[in]**[int] lda specifies the first dimension of A. if trans = HIPBLAS_OP_N, lda >= max( 1, n ), otherwise lda >= max( 1, k ).**BP**–**[in]**pointer storing matrix B on the GPU. Martrix dimension is ( ldb, k ) when if trans = HIPBLAS_OP_N, otherwise (ldb, n) only the upper/lower triangular part is accessed.**ldb**–**[in]**[int] ldb specifies the first dimension of B. if trans = HIPBLAS_OP_N, ldb >= max( 1, n ), otherwise ldb >= max( 1, k ).**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**CP**–**[in]**pointer storing matrix C on the GPU.**ldc**–**[in]**[int] ldc specifies the first dimension of C. ldc >= max( 1, n ).



The `syr2k`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSsyr2kBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const float *alpha, const float *const AP[], int lda, const float *const BP[], int ldb, const float *beta, float *const CP[], int ldc, int batchCount)[#](#_CPPv420hipblasSsyr2kBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPKfA_PCKfiA_PCKfiPKfA_PCfii)

-
hipblasStatus_t hipblasDsyr2kBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const double *alpha, const double *const AP[], int lda, const double *const BP[], int ldb, const double *beta, double *const CP[], int ldc, int batchCount)[#](#_CPPv420hipblasDsyr2kBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPKdA_PCKdiA_PCKdiPKdA_PCdii)

-
hipblasStatus_t hipblasCsyr2kBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const hipComplex *alpha, const hipComplex *const AP[], int lda, const hipComplex *const BP[], int ldb, const hipComplex *beta, hipComplex *const CP[], int ldc, int batchCount)[#](#_CPPv420hipblasCsyr2kBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPK10hipComplexA_PCK10hipComplexiA_PCK10hipComplexiPK10hipComplexA_PC10hipComplexii)

-
hipblasStatus_t hipblasZsyr2kBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const hipDoubleComplex *alpha, const hipDoubleComplex *const AP[], int lda, const hipDoubleComplex *const BP[], int ldb, const hipDoubleComplex *beta, hipDoubleComplex *const CP[], int ldc, int batchCount)[#](#_CPPv420hipblasZsyr2kBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPK16hipDoubleComplexA_PCK16hipDoubleComplexiA_PCK16hipDoubleComplexiPK16hipDoubleComplexA_PC16hipDoubleComplexii) BLAS Level 3 API.

syr2kBatched performs a batch of the matrix-matrix operations for a symmetric rank-2k update

C_i := alpha*(op( A_i )*op( B_i )^T + op( B_i )*op( A_i )^T) + beta*C_i

where alpha and beta are scalars, op(A_i) and op(B_i) are n by k matrix, and C_i is a symmetric n x n matrix stored as either upper or lower.

op( A_i ) = A_i, op( B_i ) = B_i, and A_i and B_i are n by k if trans == HIPBLAS_OP_N op( A_i ) = A_i^T, op( B_i ) = B_i^T, and A_i and B_i are k by n if trans == HIPBLAS_OP_T

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: C_i is an upper triangular matrix HIPBLAS_FILL_MODE_LOWER: C_i is a lower triangular matrix**transA**–**[in]**[hipblasOperation_t] HIPBLAS_OP_T: op( A_i ) = A_i^T, op( B_i ) = B_i^T HIPBLAS_OP_N: op( A_i ) = A_i, op( B_i ) = B_i**n**–**[in]**[int] n specifies the number of rows and columns of C_i. n >= 0.**k**–**[in]**[int] k specifies the number of columns of op(A). k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A is not referenced and A need not be set before entry.**AP**–**[in]**device array of device pointers storing each matrix_i A of dimension (lda, k) when trans is HIPBLAS_OP_N, otherwise of dimension (lda, n)**lda**–**[in]**[int] lda specifies the first dimension of A_i. if trans = HIPBLAS_OP_N, lda >= max( 1, n ), otherwise lda >= max( 1, k ).**BP**–**[in]**device array of device pointers storing each matrix_i B of dimension (ldb, k) when trans is HIPBLAS_OP_N, otherwise of dimension (ldb, n)**ldb**–**[in]**[int] ldb specifies the first dimension of B. if trans = HIPBLAS_OP_N, ldb >= max( 1, n ), otherwise ldb >= max( 1, k ).**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**CP**–**[in]**device array of device pointers storing each matrix C_i on the GPU.**ldc**–**[in]**[int] ldc specifies the first dimension of C. ldc >= max( 1, n ).**batchCount**–**[in]**[int] number of instances in the batch.



The `syr2kBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSsyr2kStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const float *alpha, const float *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const float *BP, int ldb,[hipblasStride](#_CPPv413hipblasStride)strideB, const float *beta, float *CP, int ldc,[hipblasStride](#_CPPv413hipblasStride)strideC, int batchCount)[#](#_CPPv427hipblasSsyr2kStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPKfPKfi13hipblasStridePKfi13hipblasStridePKfPfi13hipblasStridei)

-
hipblasStatus_t hipblasDsyr2kStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const double *alpha, const double *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const double *BP, int ldb,[hipblasStride](#_CPPv413hipblasStride)strideB, const double *beta, double *CP, int ldc,[hipblasStride](#_CPPv413hipblasStride)strideC, int batchCount)[#](#_CPPv427hipblasDsyr2kStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPKdPKdi13hipblasStridePKdi13hipblasStridePKdPdi13hipblasStridei)

-
hipblasStatus_t hipblasCsyr2kStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const hipComplex *alpha, const hipComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const hipComplex *BP, int ldb,[hipblasStride](#_CPPv413hipblasStride)strideB, const hipComplex *beta, hipComplex *CP, int ldc,[hipblasStride](#_CPPv413hipblasStride)strideC, int batchCount)[#](#_CPPv427hipblasCsyr2kStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPK10hipComplexPK10hipComplexi13hipblasStridePK10hipComplexi13hipblasStridePK10hipComplexP10hipComplexi13hipblasStridei)

-
hipblasStatus_t hipblasZsyr2kStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const hipDoubleComplex *alpha, const hipDoubleComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const hipDoubleComplex *BP, int ldb,[hipblasStride](#_CPPv413hipblasStride)strideB, const hipDoubleComplex *beta, hipDoubleComplex *CP, int ldc,[hipblasStride](#_CPPv413hipblasStride)strideC, int batchCount)[#](#_CPPv427hipblasZsyr2kStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPK16hipDoubleComplexPK16hipDoubleComplexi13hipblasStridePK16hipDoubleComplexi13hipblasStridePK16hipDoubleComplexP16hipDoubleComplexi13hipblasStridei) BLAS Level 3 API.

syr2kStridedBatched performs a batch of the matrix-matrix operations for a symmetric rank-2k update

C_i := alpha*(op( A_i )*op( B_i )^T + op( B_i )*op( A_i )^T) + beta*C_i

where alpha and beta are scalars, op(A_i) and op(B_i) are n by k matrix, and C_i is a symmetric n x n matrix stored as either upper or lower.

op( A_i ) = A_i, op( B_i ) = B_i, and A_i and B_i are n by k if trans == HIPBLAS_OP_N op( A_i ) = A_i^T, op( B_i ) = B_i^T, and A_i and B_i are k by n if trans == HIPBLAS_OP_T

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: C_i is an upper triangular matrix HIPBLAS_FILL_MODE_LOWER: C_i is a lower triangular matrix**transA**–**[in]**[hipblasOperation_t] HIPBLAS_OP_T: op( A_i ) = A_i^T, op( B_i ) = B_i^T HIPBLAS_OP_N: op( A_i ) = A_i, op( B_i ) = B_i**n**–**[in]**[int] n specifies the number of rows and columns of C_i. n >= 0.**k**–**[in]**[int] k specifies the number of columns of op(A). k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A is not referenced and A need not be set before entry.**AP**–**[in]**Device pointer to the first matrix A_1 on the GPU of dimension (lda, k) when trans is HIPBLAS_OP_N, otherwise of dimension (lda, n)**lda**–**[in]**[int] lda specifies the first dimension of A_i. if trans = HIPBLAS_OP_N, lda >= max( 1, n ), otherwise lda >= max( 1, k ).**strideA**–**[in]**[hipblasStride] stride from the start of one matrix (A_i) and the next one (A_i+1)**BP**–**[in]**Device pointer to the first matrix B_1 on the GPU of dimension (ldb, k) when trans is HIPBLAS_OP_N, otherwise of dimension (ldb, n)**ldb**–**[in]**[int] ldb specifies the first dimension of B_i. if trans = HIPBLAS_OP_N, ldb >= max( 1, n ), otherwise ldb >= max( 1, k ).**strideB**–**[in]**[hipblasStride] stride from the start of one matrix (B_i) and the next one (B_i+1)**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**CP**–**[in]**Device pointer to the first matrix C_1 on the GPU.**ldc**–**[in]**[int] ldc specifies the first dimension of C. ldc >= max( 1, n ).**strideC**–**[inout]**[hipblasStride] stride from the start of one matrix (C_i) and the next one (C_i+1)**batchCount**–**[in]**[int] number of instances in the batch.



The `syr2kStridedBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSsyrkx(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const float *alpha, const float *AP, int lda, const float *BP, int ldb, const float *beta, float *CP, int ldc)[#](#_CPPv413hipblasSsyrkx15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPKfPKfiPKfiPKfPfi)

-
hipblasStatus_t hipblasDsyrkx(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const double *alpha, const double *AP, int lda, const double *BP, int ldb, const double *beta, double *CP, int ldc)[#](#_CPPv413hipblasDsyrkx15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPKdPKdiPKdiPKdPdi)

-
hipblasStatus_t hipblasCsyrkx(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const hipComplex *alpha, const hipComplex *AP, int lda, const hipComplex *BP, int ldb, const hipComplex *beta, hipComplex *CP, int ldc)[#](#_CPPv413hipblasCsyrkx15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPK10hipComplexPK10hipComplexiPK10hipComplexiPK10hipComplexP10hipComplexi)

-
hipblasStatus_t hipblasZsyrkx(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const hipDoubleComplex *alpha, const hipDoubleComplex *AP, int lda, const hipDoubleComplex *BP, int ldb, const hipDoubleComplex *beta, hipDoubleComplex *CP, int ldc)[#](#_CPPv413hipblasZsyrkx15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPK16hipDoubleComplexPK16hipDoubleComplexiPK16hipDoubleComplexiPK16hipDoubleComplexP16hipDoubleComplexi) BLAS Level 3 API.

syrkx performs one of the matrix-matrix operations for a symmetric rank-k update

C := alpha*op( A )*op( B )^T + beta*C

where alpha and beta are scalars, op(A) and op(B) are n by k matrix, and C is a symmetric n x n matrix stored as either upper or lower. This routine should only be used when the caller can guarantee that the result of op( A )*op( B )^T will be symmetric.

op( A ) = A, op( B ) = B, and A and B are n by k if trans == HIPBLAS_OP_N op( A ) = A^T, op( B ) = B^T, and A and B are k by n if trans == HIPBLAS_OP_T

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : s,d,c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: C is an upper triangular matrix HIPBLAS_FILL_MODE_LOWER: C is a lower triangular matrix**transA**–**[in]**[hipblasOperation_t] HIPBLAS_OP_T: op( A ) = A^T, op( B ) = B^T HIPBLAS_OP_N: op( A ) = A, op( B ) = B**n**–**[in]**[int] n specifies the number of rows and columns of C. n >= 0.**k**–**[in]**[int] k specifies the number of columns of op(A) and op(B). k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A is not referenced and A need not be set before entry.**AP**–**[in]**pointer storing matrix A on the GPU. Martrix dimension is ( lda, k ) when if trans = HIPBLAS_OP_N, otherwise (lda, n) only the upper/lower triangular part is accessed.**lda**–**[in]**[int] lda specifies the first dimension of A. if trans = HIPBLAS_OP_N, lda >= max( 1, n ), otherwise lda >= max( 1, k ).**BP**–**[in]**pointer storing matrix B on the GPU. Martrix dimension is ( ldb, k ) when if trans = HIPBLAS_OP_N, otherwise (ldb, n) only the upper/lower triangular part is accessed.**ldb**–**[in]**[int] ldb specifies the first dimension of B. if trans = HIPBLAS_OP_N, ldb >= max( 1, n ), otherwise ldb >= max( 1, k ).**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**CP**–**[in]**pointer storing matrix C on the GPU.**ldc**–**[in]**[int] ldc specifies the first dimension of C. ldc >= max( 1, n ).



The `syrkx`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSsyrkxBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const float *alpha, const float *const AP[], int lda, const float *const BP[], int ldb, const float *beta, float *const CP[], int ldc, int batchCount)[#](#_CPPv420hipblasSsyrkxBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPKfA_PCKfiA_PCKfiPKfA_PCfii)

-
hipblasStatus_t hipblasDsyrkxBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const double *alpha, const double *const AP[], int lda, const double *const BP[], int ldb, const double *beta, double *const CP[], int ldc, int batchCount)[#](#_CPPv420hipblasDsyrkxBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPKdA_PCKdiA_PCKdiPKdA_PCdii)

-
hipblasStatus_t hipblasCsyrkxBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const hipComplex *alpha, const hipComplex *const AP[], int lda, const hipComplex *const BP[], int ldb, const hipComplex *beta, hipComplex *const CP[], int ldc, int batchCount)[#](#_CPPv420hipblasCsyrkxBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPK10hipComplexA_PCK10hipComplexiA_PCK10hipComplexiPK10hipComplexA_PC10hipComplexii)

-
hipblasStatus_t hipblasZsyrkxBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const hipDoubleComplex *alpha, const hipDoubleComplex *const AP[], int lda, const hipDoubleComplex *const BP[], int ldb, const hipDoubleComplex *beta, hipDoubleComplex *const CP[], int ldc, int batchCount)[#](#_CPPv420hipblasZsyrkxBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPK16hipDoubleComplexA_PCK16hipDoubleComplexiA_PCK16hipDoubleComplexiPK16hipDoubleComplexA_PC16hipDoubleComplexii) BLAS Level 3 API.

syrkxBatched performs a batch of the matrix-matrix operations for a symmetric rank-k update

C_i := alpha*op( A_i )*op( B_i )^T + beta*C_i

where alpha and beta are scalars, op(A_i) and op(B_i) are n by k matrix, and C_i is a symmetric n x n matrix stored as either upper or lower. This routine should only be used when the caller can guarantee that the result of op( A_i )*op( B_i )^T will be symmetric.

op( A_i ) = A_i, op( B_i ) = B_i, and A_i and B_i are n by k if trans == HIPBLAS_OP_N op( A_i ) = A_i^T, op( B_i ) = B_i^T, and A_i and B_i are k by n if trans == HIPBLAS_OP_T

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: C_i is an upper triangular matrix HIPBLAS_FILL_MODE_LOWER: C_i is a lower triangular matrix**transA**–**[in]**[hipblasOperation_t] HIPBLAS_OP_T: op( A_i ) = A_i^T, op( B_i ) = B_i^T HIPBLAS_OP_N: op( A_i ) = A_i, op( B_i ) = B_i**n**–**[in]**[int] n specifies the number of rows and columns of C_i. n >= 0.**k**–**[in]**[int] k specifies the number of columns of op(A). k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A is not referenced and A need not be set before entry.**AP**–**[in]**device array of device pointers storing each matrix_i A of dimension (lda, k) when trans is HIPBLAS_OP_N, otherwise of dimension (lda, n)**lda**–**[in]**[int] lda specifies the first dimension of A_i. if trans = HIPBLAS_OP_N, lda >= max( 1, n ), otherwise lda >= max( 1, k ).**BP**–**[in]**device array of device pointers storing each matrix_i B of dimension (ldb, k) when trans is HIPBLAS_OP_N, otherwise of dimension (ldb, n)**ldb**–**[in]**[int] ldb specifies the first dimension of B. if trans = HIPBLAS_OP_N, ldb >= max( 1, n ), otherwise ldb >= max( 1, k ).**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**CP**–**[in]**device array of device pointers storing each matrix C_i on the GPU.**ldc**–**[in]**[int] ldc specifies the first dimension of C. ldc >= max( 1, n ).**batchCount**–**[in]**[int] number of instances in the batch.



The `syrkxBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSsyrkxStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const float *alpha, const float *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const float *BP, int ldb,[hipblasStride](#_CPPv413hipblasStride)strideB, const float *beta, float *CP, int ldc,[hipblasStride](#_CPPv413hipblasStride)strideC, int batchCount)[#](#_CPPv427hipblasSsyrkxStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPKfPKfi13hipblasStridePKfi13hipblasStridePKfPfi13hipblasStridei)

-
hipblasStatus_t hipblasDsyrkxStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const double *alpha, const double *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const double *BP, int ldb,[hipblasStride](#_CPPv413hipblasStride)strideB, const double *beta, double *CP, int ldc,[hipblasStride](#_CPPv413hipblasStride)strideC, int batchCount)[#](#_CPPv427hipblasDsyrkxStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPKdPKdi13hipblasStridePKdi13hipblasStridePKdPdi13hipblasStridei)

-
hipblasStatus_t hipblasCsyrkxStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const hipComplex *alpha, const hipComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const hipComplex *BP, int ldb,[hipblasStride](#_CPPv413hipblasStride)strideB, const hipComplex *beta, hipComplex *CP, int ldc,[hipblasStride](#_CPPv413hipblasStride)strideC, int batchCount)[#](#_CPPv427hipblasCsyrkxStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPK10hipComplexPK10hipComplexi13hipblasStridePK10hipComplexi13hipblasStridePK10hipComplexP10hipComplexi13hipblasStridei)

-
hipblasStatus_t hipblasZsyrkxStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA, int n, int k, const hipDoubleComplex *alpha, const hipDoubleComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const hipDoubleComplex *BP, int ldb,[hipblasStride](#_CPPv413hipblasStride)strideB, const hipDoubleComplex *beta, hipDoubleComplex *CP, int ldc,[hipblasStride](#_CPPv413hipblasStride)strideC, int batchCount)[#](#_CPPv427hipblasZsyrkxStridedBatched15hipblasHandle_t17hipblasFillMode_t18hipblasOperation_tiiPK16hipDoubleComplexPK16hipDoubleComplexi13hipblasStridePK16hipDoubleComplexi13hipblasStridePK16hipDoubleComplexP16hipDoubleComplexi13hipblasStridei) BLAS Level 3 API.

syrkxStridedBatched performs a batch of the matrix-matrix operations for a symmetric rank-k update

C_i := alpha*op( A_i )*op( B_i )^T + beta*C_i

where alpha and beta are scalars, op(A_i) and op(B_i) are n by k matrix, and C_i is a symmetric n x n matrix stored as either upper or lower. This routine should only be used when the caller can guarantee that the result of op( A_i )*op( B_i )^T will be symmetric.

op( A_i ) = A_i, op( B_i ) = B_i, and A_i and B_i are n by k if trans == HIPBLAS_OP_N op( A_i ) = A_i^T, op( B_i ) = B_i^T, and A_i and B_i are k by n if trans == HIPBLAS_OP_T

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: C_i is an upper triangular matrix HIPBLAS_FILL_MODE_LOWER: C_i is a lower triangular matrix**transA**–**[in]**[hipblasOperation_t] HIPBLAS_OP_T: op( A_i ) = A_i^T, op( B_i ) = B_i^T HIPBLAS_OP_N: op( A_i ) = A_i, op( B_i ) = B_i**n**–**[in]**[int] n specifies the number of rows and columns of C_i. n >= 0.**k**–**[in]**[int] k specifies the number of columns of op(A). k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A is not referenced and A need not be set before entry.**AP**–**[in]**Device pointer to the first matrix A_1 on the GPU of dimension (lda, k) when trans is HIPBLAS_OP_N, otherwise of dimension (lda, n)**lda**–**[in]**[int] lda specifies the first dimension of A_i. if trans = HIPBLAS_OP_N, lda >= max( 1, n ), otherwise lda >= max( 1, k ).**strideA**–**[in]**[hipblasStride] stride from the start of one matrix (A_i) and the next one (A_i+1)**BP**–**[in]**Device pointer to the first matrix B_1 on the GPU of dimension (ldb, k) when trans is HIPBLAS_OP_N, otherwise of dimension (ldb, n)**ldb**–**[in]**[int] ldb specifies the first dimension of B_i. if trans = HIPBLAS_OP_N, ldb >= max( 1, n ), otherwise ldb >= max( 1, k ).**strideB**–**[in]**[hipblasStride] stride from the start of one matrix (B_i) and the next one (B_i+1)**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**CP**–**[in]**Device pointer to the first matrix C_1 on the GPU.**ldc**–**[in]**[int] ldc specifies the first dimension of C. ldc >= max( 1, n ).**strideC**–**[inout]**[hipblasStride] stride from the start of one matrix (C_i) and the next one (C_i+1)**batchCount**–**[in]**[int] number of instances in the batch.



The `syrkxStridedBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSgeam(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transB, int m, int n, const float *alpha, const float *AP, int lda, const float *beta, const float *BP, int ldb, float *CP, int ldc)[#](#_CPPv412hipblasSgeam15hipblasHandle_t18hipblasOperation_t18hipblasOperation_tiiPKfPKfiPKfPKfiPfi)

-
hipblasStatus_t hipblasDgeam(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transB, int m, int n, const double *alpha, const double *AP, int lda, const double *beta, const double *BP, int ldb, double *CP, int ldc)[#](#_CPPv412hipblasDgeam15hipblasHandle_t18hipblasOperation_t18hipblasOperation_tiiPKdPKdiPKdPKdiPdi)

-
hipblasStatus_t hipblasCgeam(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transB, int m, int n, const hipComplex *alpha, const hipComplex *AP, int lda, const hipComplex *beta, const hipComplex *BP, int ldb, hipComplex *CP, int ldc)[#](#_CPPv412hipblasCgeam15hipblasHandle_t18hipblasOperation_t18hipblasOperation_tiiPK10hipComplexPK10hipComplexiPK10hipComplexPK10hipComplexiP10hipComplexi)

-
hipblasStatus_t hipblasZgeam(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transB, int m, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *AP, int lda, const hipDoubleComplex *beta, const hipDoubleComplex *BP, int ldb, hipDoubleComplex *CP, int ldc)[#](#_CPPv412hipblasZgeam15hipblasHandle_t18hipblasOperation_t18hipblasOperation_tiiPK16hipDoubleComplexPK16hipDoubleComplexiPK16hipDoubleComplexPK16hipDoubleComplexiP16hipDoubleComplexi) BLAS Level 3 API.

geam performs one of the matrix-matrix operations

where op( X ) is one ofC = alpha*op( A ) + beta*op( B ),

alpha and beta are scalars, and A, B and C are matrices, with op( A ) an m by n matrix, op( B ) an m by n matrix, and C an m by n matrix.op( X ) = X or op( X ) = X**T or op( X ) = X**H,

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : s,d,c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**transA**–**[in]**[hipblasOperation_t] specifies the form of op( A )**transB**–**[in]**[hipblasOperation_t] specifies the form of op( B )**m**–**[in]**[int] matrix dimension m.**n**–**[in]**[int] matrix dimension n.**alpha**–**[in]**device pointer or host pointer specifying the scalar alpha.**AP**–**[in]**device pointer storing matrix A.**lda**–**[in]**[int] specifies the leading dimension of A.**beta**–**[in]**device pointer or host pointer specifying the scalar beta.**BP**–**[in]**device pointer storing matrix B.**ldb**–**[in]**[int] specifies the leading dimension of B.**CP**–**[inout]**device pointer storing matrix C.**ldc**–**[in]**[int] specifies the leading dimension of C.



The `geam`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSgeamBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transB, int m, int n, const float *alpha, const float *const AP[], int lda, const float *beta, const float *const BP[], int ldb, float *const CP[], int ldc, int batchCount)[#](#_CPPv419hipblasSgeamBatched15hipblasHandle_t18hipblasOperation_t18hipblasOperation_tiiPKfA_PCKfiPKfA_PCKfiA_PCfii)

-
hipblasStatus_t hipblasDgeamBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transB, int m, int n, const double *alpha, const double *const AP[], int lda, const double *beta, const double *const BP[], int ldb, double *const CP[], int ldc, int batchCount)[#](#_CPPv419hipblasDgeamBatched15hipblasHandle_t18hipblasOperation_t18hipblasOperation_tiiPKdA_PCKdiPKdA_PCKdiA_PCdii)

-
hipblasStatus_t hipblasCgeamBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transB, int m, int n, const hipComplex *alpha, const hipComplex *const AP[], int lda, const hipComplex *beta, const hipComplex *const BP[], int ldb, hipComplex *const CP[], int ldc, int batchCount)[#](#_CPPv419hipblasCgeamBatched15hipblasHandle_t18hipblasOperation_t18hipblasOperation_tiiPK10hipComplexA_PCK10hipComplexiPK10hipComplexA_PCK10hipComplexiA_PC10hipComplexii)

-
hipblasStatus_t hipblasZgeamBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transB, int m, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *const AP[], int lda, const hipDoubleComplex *beta, const hipDoubleComplex *const BP[], int ldb, hipDoubleComplex *const CP[], int ldc, int batchCount)[#](#_CPPv419hipblasZgeamBatched15hipblasHandle_t18hipblasOperation_t18hipblasOperation_tiiPK16hipDoubleComplexA_PCK16hipDoubleComplexiPK16hipDoubleComplexA_PCK16hipDoubleComplexiA_PC16hipDoubleComplexii) BLAS Level 3 API.

geamBatched performs one of the batched matrix-matrix operations

where alpha and beta are scalars, and op(A_i), op(B_i) and C_i are m by n matrices and op( X ) is one ofC_i = alpha*op( A_i ) + beta*op( B_i ) for i = 0, 1, ... batchCount - 1

op( X ) = X or op( X ) = X**T

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**transA**–**[in]**[hipblasOperation_t] specifies the form of op( A )**transB**–**[in]**[hipblasOperation_t] specifies the form of op( B )**m**–**[in]**[int] matrix dimension m.**n**–**[in]**[int] matrix dimension n.**alpha**–**[in]**device pointer or host pointer specifying the scalar alpha.**AP**–**[in]**device array of device pointers storing each matrix A_i on the GPU. Each A_i is of dimension ( lda, k ), where k is m when transA == HIPBLAS_OP_N and is n when transA == HIPBLAS_OP_T.**lda**–**[in]**[int] specifies the leading dimension of A.**beta**–**[in]**device pointer or host pointer specifying the scalar beta.**BP**–**[in]**device array of device pointers storing each matrix B_i on the GPU. Each B_i is of dimension ( ldb, k ), where k is m when transB == HIPBLAS_OP_N and is n when transB == HIPBLAS_OP_T.**ldb**–**[in]**[int] specifies the leading dimension of B.**CP**–**[inout]**device array of device pointers storing each matrix C_i on the GPU. Each C_i is of dimension ( ldc, n ).**ldc**–**[in]**[int] specifies the leading dimension of C.**batchCount**–**[in]**[int] number of instances i in the batch.



The `geamBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSgeamStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transB, int m, int n, const float *alpha, const float *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const float *beta, const float *BP, int ldb,[hipblasStride](#_CPPv413hipblasStride)strideB, float *CP, int ldc,[hipblasStride](#_CPPv413hipblasStride)strideC, int batchCount)[#](#_CPPv426hipblasSgeamStridedBatched15hipblasHandle_t18hipblasOperation_t18hipblasOperation_tiiPKfPKfi13hipblasStridePKfPKfi13hipblasStridePfi13hipblasStridei)

-
hipblasStatus_t hipblasDgeamStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transB, int m, int n, const double *alpha, const double *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const double *beta, const double *BP, int ldb,[hipblasStride](#_CPPv413hipblasStride)strideB, double *CP, int ldc,[hipblasStride](#_CPPv413hipblasStride)strideC, int batchCount)[#](#_CPPv426hipblasDgeamStridedBatched15hipblasHandle_t18hipblasOperation_t18hipblasOperation_tiiPKdPKdi13hipblasStridePKdPKdi13hipblasStridePdi13hipblasStridei)

-
hipblasStatus_t hipblasCgeamStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transB, int m, int n, const hipComplex *alpha, const hipComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const hipComplex *beta, const hipComplex *BP, int ldb,[hipblasStride](#_CPPv413hipblasStride)strideB, hipComplex *CP, int ldc,[hipblasStride](#_CPPv413hipblasStride)strideC, int batchCount)[#](#_CPPv426hipblasCgeamStridedBatched15hipblasHandle_t18hipblasOperation_t18hipblasOperation_tiiPK10hipComplexPK10hipComplexi13hipblasStridePK10hipComplexPK10hipComplexi13hipblasStrideP10hipComplexi13hipblasStridei)

-
hipblasStatus_t hipblasZgeamStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transB, int m, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const hipDoubleComplex *beta, const hipDoubleComplex *BP, int ldb,[hipblasStride](#_CPPv413hipblasStride)strideB, hipDoubleComplex *CP, int ldc,[hipblasStride](#_CPPv413hipblasStride)strideC, int batchCount)[#](#_CPPv426hipblasZgeamStridedBatched15hipblasHandle_t18hipblasOperation_t18hipblasOperation_tiiPK16hipDoubleComplexPK16hipDoubleComplexi13hipblasStridePK16hipDoubleComplexPK16hipDoubleComplexi13hipblasStrideP16hipDoubleComplexi13hipblasStridei) BLAS Level 3 API.

geamStridedBatched performs one of the batched matrix-matrix operations

where alpha and beta are scalars, and op(A_i), op(B_i) and C_i are m by n matrices and op( X ) is one ofC_i = alpha*op( A_i ) + beta*op( B_i ) for i = 0, 1, ... batchCount - 1

op( X ) = X or op( X ) = X**T

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**transA**–**[in]**[hipblasOperation_t] specifies the form of op( A )**transB**–**[in]**[hipblasOperation_t] specifies the form of op( B )**m**–**[in]**[int] matrix dimension m.**n**–**[in]**[int] matrix dimension n.**alpha**–**[in]**device pointer or host pointer specifying the scalar alpha.**AP**–**[in]**device pointer to the first matrix A_0 on the GPU. Each A_i is of dimension ( lda, k ), where k is m when transA == HIPBLAS_OP_N and is n when transA == HIPBLAS_OP_T.**lda**–**[in]**[int] specifies the leading dimension of A.**strideA**–**[in]**[hipblasStride] stride from the start of one matrix (A_i) and the next one (A_i+1)**beta**–**[in]**device pointer or host pointer specifying the scalar beta.**BP**–**[in]**pointer to the first matrix B_0 on the GPU. Each B_i is of dimension ( ldb, k ), where k is m when transB == HIPBLAS_OP_N and is n when transB == HIPBLAS_OP_T.**ldb**–**[in]**[int] specifies the leading dimension of B.**strideB**–**[in]**[hipblasStride] stride from the start of one matrix (B_i) and the next one (B_i+1)**CP**–**[inout]**pointer to the first matrix C_0 on the GPU. Each C_i is of dimension ( ldc, n ).**ldc**–**[in]**[int] specifies the leading dimension of C.**strideC**–**[in]**[hipblasStride] stride from the start of one matrix (C_i) and the next one (C_i+1)**batchCount**–**[in]**[int] number of instances i in the batch.



The `geamStridedBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasChemm(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, int k, const hipComplex *alpha, const hipComplex *AP, int lda, const hipComplex *BP, int ldb, const hipComplex *beta, hipComplex *CP, int ldc)[#](#_CPPv412hipblasChemm15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_tiiPK10hipComplexPK10hipComplexiPK10hipComplexiPK10hipComplexP10hipComplexi)

-
hipblasStatus_t hipblasZhemm(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, int k, const hipDoubleComplex *alpha, const hipDoubleComplex *AP, int lda, const hipDoubleComplex *BP, int ldb, const hipDoubleComplex *beta, hipDoubleComplex *CP, int ldc)[#](#_CPPv412hipblasZhemm15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_tiiPK16hipDoubleComplexPK16hipDoubleComplexiPK16hipDoubleComplexiPK16hipDoubleComplexP16hipDoubleComplexi) BLAS Level 3 API.

hemm performs one of the matrix-matrix operations:

C := alpha*A*B + beta*C if side == HIPBLAS_SIDE_LEFT, C := alpha*B*A + beta*C if side == HIPBLAS_SIDE_RIGHT,

where alpha and beta are scalars, B and C are m by n matrices, and A is a Hermitian matrix stored as either upper or lower.

Supported precisions in rocBLAS : c,z

Supported precisions in cuBLAS : c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**side**–**[in]**[hipblasSideMode_t] HIPBLAS_SIDE_LEFT: C := alpha*A*B + beta*C HIPBLAS_SIDE_RIGHT: C := alpha*B*A + beta*C**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: A is an upper triangular matrix HIPBLAS_FILL_MODE_LOWER: A is a lower triangular matrix**n**–**[in]**[int] n specifies the number of rows of B and C. n >= 0.**k**–**[in]**[int] n specifies the number of columns of B and C. k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A and B are not referenced.**AP**–**[in]**pointer storing matrix A on the GPU. A is m by m if side == HIPBLAS_SIDE_LEFT A is n by n if side == HIPBLAS_SIDE_RIGHT Only the upper/lower triangular part is accessed. The imaginary component of the diagonal elements is not used.**lda**–**[in]**[int] lda specifies the first dimension of A. if side = HIPBLAS_SIDE_LEFT, lda >= max( 1, m ), otherwise lda >= max( 1, n ).**BP**–**[in]**pointer storing matrix B on the GPU. Matrix dimension is m by n**ldb**–**[in]**[int] ldb specifies the first dimension of B. ldb >= max( 1, m )**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**CP**–**[in]**pointer storing matrix C on the GPU. Matrix dimension is m by n**ldc**–**[in]**[int] ldc specifies the first dimension of C. ldc >= max( 1, m )



The `hemm`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasChemmBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, int k, const hipComplex *alpha, const hipComplex *const AP[], int lda, const hipComplex *const BP[], int ldb, const hipComplex *beta, hipComplex *const CP[], int ldc, int batchCount)[#](#_CPPv419hipblasChemmBatched15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_tiiPK10hipComplexA_PCK10hipComplexiA_PCK10hipComplexiPK10hipComplexA_PC10hipComplexii)

-
hipblasStatus_t hipblasZhemmBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, int k, const hipDoubleComplex *alpha, const hipDoubleComplex *const AP[], int lda, const hipDoubleComplex *const BP[], int ldb, const hipDoubleComplex *beta, hipDoubleComplex *const CP[], int ldc, int batchCount)[#](#_CPPv419hipblasZhemmBatched15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_tiiPK16hipDoubleComplexA_PCK16hipDoubleComplexiA_PCK16hipDoubleComplexiPK16hipDoubleComplexA_PC16hipDoubleComplexii) BLAS Level 3 API.

hemmBatched performs a batch of the matrix-matrix operations:

C_i := alpha*A_i*B_i + beta*C_i if side == HIPBLAS_SIDE_LEFT, C_i := alpha*B_i*A_i + beta*C_i if side == HIPBLAS_SIDE_RIGHT,

where alpha and beta are scalars, B_i and C_i are m by n matrices, and A_i is a Hermitian matrix stored as either upper or lower.

Supported precisions in rocBLAS : c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**side**–**[in]**[hipblasSideMode_t] HIPBLAS_SIDE_LEFT: C_i := alpha*A_i*B_i + beta*C_i HIPBLAS_SIDE_RIGHT: C_i := alpha*B_i*A_i + beta*C_i**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: A_i is an upper triangular matrix HIPBLAS_FILL_MODE_LOWER: A_i is a lower triangular matrix**n**–**[in]**[int] n specifies the number of rows of B_i and C_i. n >= 0.**k**–**[in]**[int] k specifies the number of columns of B_i and C_i. k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A_i and B_i are not referenced.**AP**–**[in]**device array of device pointers storing each matrix A_i on the GPU. A_i is m by m if side == HIPBLAS_SIDE_LEFT A_i is n by n if side == HIPBLAS_SIDE_RIGHT Only the upper/lower triangular part is accessed. The imaginary component of the diagonal elements is not used.**lda**–**[in]**[int] lda specifies the first dimension of A_i. if side = HIPBLAS_SIDE_LEFT, lda >= max( 1, m ), otherwise lda >= max( 1, n ).**BP**–**[in]**device array of device pointers storing each matrix B_i on the GPU. Matrix dimension is m by n**ldb**–**[in]**[int] ldb specifies the first dimension of B_i. ldb >= max( 1, m )**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C_i need not be set before entry.**CP**–**[in]**device array of device pointers storing each matrix C_i on the GPU. Matrix dimension is m by n**ldc**–**[in]**[int] ldc specifies the first dimension of C_i. ldc >= max( 1, m )**batchCount**–**[in]**[int] number of instances in the batch.



The `hemmBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasChemmStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, int k, const hipComplex *alpha, const hipComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const hipComplex *BP, int ldb,[hipblasStride](#_CPPv413hipblasStride)strideB, const hipComplex *beta, hipComplex *CP, int ldc,[hipblasStride](#_CPPv413hipblasStride)strideC, int batchCount)[#](#_CPPv426hipblasChemmStridedBatched15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_tiiPK10hipComplexPK10hipComplexi13hipblasStridePK10hipComplexi13hipblasStridePK10hipComplexP10hipComplexi13hipblasStridei)

-
hipblasStatus_t hipblasZhemmStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo, int n, int k, const hipDoubleComplex *alpha, const hipDoubleComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const hipDoubleComplex *BP, int ldb,[hipblasStride](#_CPPv413hipblasStride)strideB, const hipDoubleComplex *beta, hipDoubleComplex *CP, int ldc,[hipblasStride](#_CPPv413hipblasStride)strideC, int batchCount)[#](#_CPPv426hipblasZhemmStridedBatched15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_tiiPK16hipDoubleComplexPK16hipDoubleComplexi13hipblasStridePK16hipDoubleComplexi13hipblasStridePK16hipDoubleComplexP16hipDoubleComplexi13hipblasStridei) BLAS Level 3 API.

hemmStridedBatched performs a batch of the matrix-matrix operations:

C_i := alpha*A_i*B_i + beta*C_i if side == HIPBLAS_SIDE_LEFT, C_i := alpha*B_i*A_i + beta*C_i if side == HIPBLAS_SIDE_RIGHT,

where alpha and beta are scalars, B_i and C_i are m by n matrices, and A_i is a Hermitian matrix stored as either upper or lower.

Supported precisions in rocBLAS : c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**side**–**[in]**[hipblasSideMode_t] HIPBLAS_SIDE_LEFT: C_i := alpha*A_i*B_i + beta*C_i HIPBLAS_SIDE_RIGHT: C_i := alpha*B_i*A_i + beta*C_i**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: A_i is an upper triangular matrix HIPBLAS_FILL_MODE_LOWER: A_i is a lower triangular matrix**n**–**[in]**[int] n specifies the number of rows of B_i and C_i. n >= 0.**k**–**[in]**[int] k specifies the number of columns of B_i and C_i. k >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A_i and B_i are not referenced.**AP**–**[in]**device pointer to first matrix A_1 A_i is m by m if side == HIPBLAS_SIDE_LEFT A_i is n by n if side == HIPBLAS_SIDE_RIGHT Only the upper/lower triangular part is accessed. The imaginary component of the diagonal elements is not used.**lda**–**[in]**[int] lda specifies the first dimension of A_i. if side = HIPBLAS_SIDE_LEFT, lda >= max( 1, m ), otherwise lda >= max( 1, n ).**strideA**–**[in]**[hipblasStride] stride from the start of one matrix (A_i) and the next one (A_i+1)**BP**–**[in]**device pointer to first matrix B_1 of dimension (ldb, n) on the GPU**ldb**–**[in]**[int] ldb specifies the first dimension of B_i. if side = HIPBLAS_OP_N, ldb >= max( 1, m ), otherwise ldb >= max( 1, n ).**strideB**–**[in]**[hipblasStride] stride from the start of one matrix (B_i) and the next one (B_i+1)**beta**–**[in]**beta specifies the scalar beta. When beta is zero then C need not be set before entry.**CP**–**[in]**device pointer to first matrix C_1 of dimension (ldc, n) on the GPU.**ldc**–**[in]**[int] ldc specifies the first dimension of C. ldc >= max( 1, m )**strideC**–**[inout]**[hipblasStride] stride from the start of one matrix (C_i) and the next one (C_i+1)**batchCount**–**[in]**[int] number of instances in the batch



The `hemmStridedBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasStrmm(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int m, int n, const float *alpha, const float *A, int lda, const float *B, int ldb, float *C, int ldc)[#](#_CPPv412hipblasStrmm15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPKfPKfiPKfiPfi)

-
hipblasStatus_t hipblasDtrmm(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int m, int n, const double *alpha, const double *A, int lda, const double *B, int ldb, double *C, int ldc)[#](#_CPPv412hipblasDtrmm15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPKdPKdiPKdiPdi)

-
hipblasStatus_t hipblasCtrmm(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int m, int n, const hipComplex *alpha, const hipComplex *A, int lda, const hipComplex *B, int ldb, hipComplex *C, int ldc)[#](#_CPPv412hipblasCtrmm15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPK10hipComplexPK10hipComplexiPK10hipComplexiP10hipComplexi)

-
hipblasStatus_t hipblasZtrmm(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int m, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *A, int lda, const hipDoubleComplex *B, int ldb, hipDoubleComplex *C, int ldc)[#](#_CPPv412hipblasZtrmm15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPK16hipDoubleComplexPK16hipDoubleComplexiPK16hipDoubleComplexiP16hipDoubleComplexi) BLAS Level 3 API.

trmm performs one of the matrix-matrix operations

C := alpha*op( A )*B, or C := alpha*B*op( A )

where alpha is a scalar, B and C are an m by n matrices, A is a unit, or non-unit, upper or lower triangular matrix and op( A ) is one of

Note that trmm can provide in-place functionality by passing in the same address for both matrices B and C and by setting ldb equal to ldc.op( A ) = A or op( A ) = A^T or op( A ) = A^H.

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : s,d,c,z


When uplo == HIPBLAS_FILL_MODE_UPPER the leading k by k upper triangular part of the array A must contain the upper triangular matrix and the strictly lower triangular part of A is not referenced.

When uplo == HIPBLAS_FILL_MODE_LOWER the leading k by k lower triangular part of the array A must contain the lower triangular matrix and the strictly upper triangular part of A is not referenced.

Note that when diag == HIPBLAS_DIAG_UNIT the diagonal elements of A are not referenced either, but are assumed to be unity.

- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**side**–**[in]**[hipblasSideMode_t] Specifies whether op(A) multiplies B from the left or right as follows: HIPBLAS_SIDE_LEFT: C := alpha*op( A )*B. HIPBLAS_SIDE_RIGHT: C := alpha*B*op( A ).**uplo**–**[in]**[hipblasFillMode_t] Specifies whether the matrix A is an upper or lower triangular matrix as follows: HIPBLAS_FILL_MODE_UPPER: A is an upper triangular matrix. HIPBLAS_FILL_MODE_LOWER: A is a lower triangular matrix.**transA**–**[in]**[hipblasOperation_t] Specifies the form of op(A) to be used in the matrix multiplication as follows: HIPBLAS_OP_N: op(A) = A. HIPBLAS_OP_T: op(A) = A^T. HIPBLAS_OP_C: op(A) = A^H.**diag**–**[in]**[hipblasDiagType_t] Specifies whether or not A is unit triangular as follows: HIPBLAS_DIAG_UNIT: A is assumed to be unit triangular. HIPBLAS_DIAG_NON_UNIT: A is not assumed to be unit triangular.**m**–**[in]**[int] m specifies the number of rows of B and C. m >= 0.**n**–**[in]**[int] n specifies the number of columns of B and C. n >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A is not referenced and B need not be set before entry.**A**–**[in]**Device pointer to matrix A on the GPU. A has dimension ( lda, k ), where k is m when side == HIPBLAS_SIDE_LEFT and is n when side == HIPBLAS_SIDE_RIGHT.**lda**–**[in]**[int] lda specifies the first dimension of A. if side == HIPBLAS_SIDE_LEFT, lda >= max( 1, m ), if side == HIPBLAS_SIDE_RIGHT, lda >= max( 1, n ).**B**–**[inout]**Device pointer to the matrix B of dimension (ldb, n) on the GPU.**ldb**–**[in]**[int] ldb specifies the first dimension of B. ldb >= max( 1, m ).**C**–**[in]**Device pointer to the matrix C of dimension (ldc, n) on the GPU. Users can pass in the same matrix B to parameter C to achieve in-place functionality of trmm.**ldc**–**[in]**[int] ldc specifies the first dimension of C. ldc >= max( 1, m ).



The `trmm`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasStrmmBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int m, int n, const float *alpha, const float *const A[], int lda, const float *const B[], int ldb, float *const C[], int ldc, int batchCount)[#](#_CPPv419hipblasStrmmBatched15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPKfA_PCKfiA_PCKfiA_PCfii)

-
hipblasStatus_t hipblasDtrmmBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int m, int n, const double *alpha, const double *const A[], int lda, const double *const B[], int ldb, double *const C[], int ldc, int batchCount)[#](#_CPPv419hipblasDtrmmBatched15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPKdA_PCKdiA_PCKdiA_PCdii)

-
hipblasStatus_t hipblasCtrmmBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int m, int n, const hipComplex *alpha, const hipComplex *const A[], int lda, const hipComplex *const B[], int ldb, hipComplex *const C[], int ldc, int batchCount)[#](#_CPPv419hipblasCtrmmBatched15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPK10hipComplexA_PCK10hipComplexiA_PCK10hipComplexiA_PC10hipComplexii)

-
hipblasStatus_t hipblasZtrmmBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int m, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *const A[], int lda, const hipDoubleComplex *const B[], int ldb, hipDoubleComplex *const C[], int ldc, int batchCount)[#](#_CPPv419hipblasZtrmmBatched15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPK16hipDoubleComplexA_PCK16hipDoubleComplexiA_PCK16hipDoubleComplexiA_PC16hipDoubleComplexii) BLAS Level 3 API.

trmmBatched performs one of the batched matrix-matrix operations

C_i := alpha*op( A_i )*B_i, or C_i := alpha*B_i*op( A_i ) for i = 0, 1, … batchCount -1

where alpha is a scalar, B_i and C_i are m by n matrices, A_i is a unit, or non-unit, upper or lower triangular matrix and op( A_i ) is one of

Note that trmmBatched can provide in-place functionality by passing in the same address for both matrices B and C and by setting ldb equal to ldc.op( A_i ) = A_i or op( A_i ) = A_i^T or op( A_i ) = A_i^H.

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


When uplo == HIPBLAS_FILL_MODE_UPPER the leading k by k upper triangular part of the array A must contain the upper triangular matrix and the strictly lower triangular part of A is not referenced.

When uplo == HIPBLAS_FILL_MODE_LOWER the leading k by k lower triangular part of the array A must contain the lower triangular matrix and the strictly upper triangular part of A is not referenced.

Note that when diag == HIPBLAS_DIAG_UNIT the diagonal elements of A_i are not referenced either, but are assumed to be unity.

- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**side**–**[in]**[hipblasSideMode_t] Specifies whether op(A_i) multiplies B_i from the left or right as follows: HIPBLAS_SIDE_LEFT: B_i := alpha*op( A_i )*B_i. HIPBLAS_SIDE_RIGHT: B_i := alpha*B_i*op( A_i ).**uplo**–**[in]**[hipblasFillMode_t] Specifies whether the matrix A is an upper or lower triangular matrix as follows: HIPBLAS_FILL_MODE_UPPER: A is an upper triangular matrix. HIPBLAS_FILL_MODE_LOWER: A is a lower triangular matrix.**transA**–**[in]**[hipblasOperation_t] Specifies the form of op(A_i) to be used in the matrix multiplication as follows: HIPBLAS_OP_N: op(A_i) = A_i. HIPBLAS_OP_T: op(A_i) = A_i^T. HIPBLAS_OP_C: op(A_i) = A_i^H.**diag**–**[in]**[hipblasDiagType_t] Specifies whether or not A_i is unit triangular as follows: HIPBLAS_DIAG_UNIT: A_i is assumed to be unit triangular. HIPBLAS_DIAG_NON_UNIT: A_i is not assumed to be unit triangular.**m**–**[in]**[int] m specifies the number of rows of B_i and C_i. m >= 0.**n**–**[in]**[int] n specifies the number of columns of B_i and C_i. n >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A_i is not referenced and B_i need not be set before entry.**A**–**[in]**Device array of device pointers storing each matrix A_i on the GPU. Each A_i is of dimension ( lda, k ), where k is m when side == HIPBLAS_SIDE_LEFT and is n when side == HIPBLAS_SIDE_RIGHT.**lda**–**[in]**[int] lda specifies the first dimension of A. if side == HIPBLAS_SIDE_LEFT, lda >= max( 1, m ), if side == HIPBLAS_SIDE_RIGHT, lda >= max( 1, n ).**B**–**[inout]**device array of device pointers storing each matrix B_i of dimension (ldb, n) on the GPU.**ldb**–**[in]**[int] ldb specifies the first dimension of B_i. ldb >= max( 1, m ).**C**–**[in]**device array of device pointers storing each matrix C_i of dimension (ldc, n) on the GPU. Users can pass in the same matrices B to parameter C to achieve in-place functionality of trmmBatched.**ldc**–**[in]**lec specifies the first dimension of C_i. ldc >= max( 1, m ).**batchCount**–**[in]**[int] number of instances i in the batch.



The `trmmBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasStrmmStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int m, int n, const float *alpha, const float *A, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const float *B, int ldb,[hipblasStride](#_CPPv413hipblasStride)strideB, float *C, int ldc,[hipblasStride](#_CPPv413hipblasStride)strideC, int batchCount)[#](#_CPPv426hipblasStrmmStridedBatched15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPKfPKfi13hipblasStridePKfi13hipblasStridePfi13hipblasStridei)

-
hipblasStatus_t hipblasDtrmmStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int m, int n, const double *alpha, const double *A, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const double *B, int ldb,[hipblasStride](#_CPPv413hipblasStride)strideB, double *C, int ldc,[hipblasStride](#_CPPv413hipblasStride)strideC, int batchCount)[#](#_CPPv426hipblasDtrmmStridedBatched15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPKdPKdi13hipblasStridePKdi13hipblasStridePdi13hipblasStridei)

-
hipblasStatus_t hipblasCtrmmStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int m, int n, const hipComplex *alpha, const hipComplex *A, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const hipComplex *B, int ldb,[hipblasStride](#_CPPv413hipblasStride)strideB, hipComplex *C, int ldc,[hipblasStride](#_CPPv413hipblasStride)strideC, int batchCount)[#](#_CPPv426hipblasCtrmmStridedBatched15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPK10hipComplexPK10hipComplexi13hipblasStridePK10hipComplexi13hipblasStrideP10hipComplexi13hipblasStridei)

-
hipblasStatus_t hipblasZtrmmStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int m, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *A, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const hipDoubleComplex *B, int ldb,[hipblasStride](#_CPPv413hipblasStride)strideB, hipDoubleComplex *C, int ldc,[hipblasStride](#_CPPv413hipblasStride)strideC, int batchCount)[#](#_CPPv426hipblasZtrmmStridedBatched15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPK16hipDoubleComplexPK16hipDoubleComplexi13hipblasStridePK16hipDoubleComplexi13hipblasStrideP16hipDoubleComplexi13hipblasStridei) BLAS Level 3 API.

trmmStridedBatched performs one of the strided_batched matrix-matrix operations

C_i := alpha*op( A_i )*B_i, or C_i := alpha*B_i*op( A_i ) for i = 0, 1, … batchCount -1

where alpha is a scalar, B_i and C_i are m by n matrices, A_i is a unit, or non-unit, upper or lower triangular matrix and op( A_i ) is one of

Note that trmmStridedBatched can provide in-place functionality by passing in the same address for both matrices B and C and by setting ldb equal to ldc.op( A_i ) = A_i or op( A_i ) = A_i^T or op( A_i ) = A_i^H.

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


When uplo == HIPBLAS_FILL_MODE_UPPER the leading k by k upper triangular part of the array A must contain the upper triangular matrix and the strictly lower triangular part of A is not referenced.

When uplo == HIPBLAS_FILL_MODE_LOWER the leading k by k lower triangular part of the array A must contain the lower triangular matrix and the strictly upper triangular part of A is not referenced.

Note that when diag == HIPBLAS_DIAG_UNIT the diagonal elements of A_i are not referenced either, but are assumed to be unity.

- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**side**–**[in]**[hipblasSideMode_t] Specifies whether op(A_i) multiplies B_i from the left or right as follows: HIPBLAS_SIDE_LEFT: C_i := alpha*op( A_i )*B_i. HIPBLAS_SIDE_RIGHT: C_i := alpha*B_i*op( A_i ).**uplo**–**[in]**[hipblasFillMode_t] Specifies whether the matrix A is an upper or lower triangular matrix as follows: HIPBLAS_FILL_MODE_UPPER: A is an upper triangular matrix. HIPBLAS_FILL_MODE_LOWER: A is a lower triangular matrix.**transA**–**[in]**[hipblasOperation_t] Specifies the form of op(A_i) to be used in the matrix multiplication as follows: HIPBLAS_OP_N: op(A_i) = A_i. HIPBLAS_OP_T: op(A_i) = A_i^T. HIPBLAS_OP_C: op(A_i) = A_i^H.**diag**–**[in]**[hipblasDiagType_t] Specifies whether or not A_i is unit triangular as follows: HIPBLAS_DIAG_UNIT: A_i is assumed to be unit triangular. HIPBLAS_DIAG_NON_UNIT: A_i is not assumed to be unit triangular.**m**–**[in]**[int] m specifies the number of rows of B_i and C_i. m >= 0.**n**–**[in]**[int] n specifies the number of columns of B_i and C_i. n >= 0.**alpha**–**[in]**alpha specifies the scalar alpha. When alpha is zero then A_i is not referenced and B_i need not be set before entry.**A**–**[in]**Device pointer to the first matrix A_0 on the GPU. Each A_i is of dimension ( lda, k ), where k is m when side == HIPBLAS_SIDE_LEFT and is n when side == HIPBLAS_SIDE_RIGHT.**lda**–**[in]**[int] lda specifies the first dimension of A. if side == HIPBLAS_SIDE_LEFT, lda >= max( 1, m ), if side == HIPBLAS_SIDE_RIGHT, lda >= max( 1, n ).**strideA**–**[in]**[hipblasStride] stride from the start of one matrix (A_i) and the next one (A_i+1)**B**–**[inout]**Device pointer to the first matrix B_0 on the GPU. Each B_i is of dimension ( ldb, n )**ldb**–**[in]**[int] ldb specifies the first dimension of B_i. ldb >= max( 1, m ).**strideB**–**[in]**[hipblasStride] stride from the start of one matrix (B_i) and the next one (B_i+1)**C**–**[in]**Device pointer to the first matrix C_0 on the GPU. Each C_i is of dimension ( ldc, n ).**ldc**–**[in]**[int] ldc specifies the first dimension of C_i. ldc >= max( 1, m ).**strideC**–**[in]**[hipblasStride] stride from the start of one matrix (C_i) and the next one (C_i+1)**batchCount**–**[in]**[int] number of instances i in the batch.



The `trmmStridedBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasStrsm(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int m, int n, const float *alpha, const float *AP, int lda, float *BP, int ldb)[#](#_CPPv412hipblasStrsm15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPKfPKfiPfi)

-
hipblasStatus_t hipblasDtrsm(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int m, int n, const double *alpha, const double *AP, int lda, double *BP, int ldb)[#](#_CPPv412hipblasDtrsm15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPKdPKdiPdi)

-
hipblasStatus_t hipblasCtrsm(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int m, int n, const hipComplex *alpha, const hipComplex *AP, int lda, hipComplex *BP, int ldb)[#](#_CPPv412hipblasCtrsm15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPK10hipComplexPK10hipComplexiP10hipComplexi)

-
hipblasStatus_t hipblasZtrsm(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int m, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *AP, int lda, hipDoubleComplex *BP, int ldb)[#](#_CPPv412hipblasZtrsm15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPK16hipDoubleComplexPK16hipDoubleComplexiP16hipDoubleComplexi) BLAS Level 3 API.

trsm solves

where alpha is a scalar, X and B are m by n matrices, A is triangular matrix and op(A) is one ofop(A)*X = alpha*B or X*op(A) = alpha*B,

The matrix X is overwritten on B.op( A ) = A or op( A ) = A^T or op( A ) = A^H.

Note about memory allocation: When trsm is launched with a k evenly divisible by the internal block size of 128, and is no larger than 10 of these blocks, the API takes advantage of utilizing pre-allocated memory found in the handle to increase overall performance (where k is m when HIPBLAS_SIDE_LEFT and is n when HIPBLAS_SIDE_RIGHT). For more information on pre-allocated memory in the handle, see the Device Memory Allocation in rocBLAS section of the rocBLAS API Reference.

(where k is m when HIPBLAS_SIDE_LEFT and is n when HIPBLAS_SIDE_RIGHT)

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : s,d,c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**side**–**[in]**[hipblasSideMode_t] HIPBLAS_SIDE_LEFT: op(A)*X = alpha*B. HIPBLAS_SIDE_RIGHT: X*op(A) = alpha*B.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: A is an upper triangular matrix. HIPBLAS_FILL_MODE_LOWER: A is a lower triangular matrix.**transA**–**[in]**[hipblasOperation_t] HIPBLAS_OP_N: op(A) = A. HIPBLAS_OP_T: op(A) = A^T. HIPBLAS_OP_C: op(A) = A^H.**diag**–**[in]**[hipblasDiagType_t] HIPBLAS_DIAG_UNIT: A is assumed to be unit triangular. HIPBLAS_DIAG_NON_UNIT: A is not assumed to be unit triangular.**m**–**[in]**[int] m specifies the number of rows of B. m >= 0.**n**–**[in]**[int] n specifies the number of columns of B. n >= 0.**alpha**–**[in]**device pointer or host pointer specifying the scalar alpha. When alpha is &zero then A is not referenced and B need not be set before entry.**AP**–**[in]**device pointer storing matrix A. of dimension ( lda, k ), where k is m when HIPBLAS_SIDE_LEFT and is n when HIPBLAS_SIDE_RIGHT only the upper/lower triangular part is accessed.**lda**–**[in]**[int] lda specifies the first dimension of A. if side = HIPBLAS_SIDE_LEFT, lda >= max( 1, m ), if side = HIPBLAS_SIDE_RIGHT, lda >= max( 1, n ).**BP**–**[inout]**device pointer storing matrix B.**ldb**–**[in]**[int] ldb specifies the first dimension of B. ldb >= max( 1, m ).



The `trsm`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasStrsmBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int m, int n, const float *alpha, const float *const AP[], int lda, float *const BP[], int ldb, int batchCount)[#](#_CPPv419hipblasStrsmBatched15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPKfA_PCKfiA_PCfii)

-
hipblasStatus_t hipblasDtrsmBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int m, int n, const double *alpha, const double *const AP[], int lda, double *const BP[], int ldb, int batchCount)[#](#_CPPv419hipblasDtrsmBatched15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPKdA_PCKdiA_PCdii)

-
hipblasStatus_t hipblasCtrsmBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int m, int n, const hipComplex *alpha, const hipComplex *const AP[], int lda, hipComplex *const BP[], int ldb, int batchCount)[#](#_CPPv419hipblasCtrsmBatched15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPK10hipComplexA_PCK10hipComplexiA_PC10hipComplexii)

-
hipblasStatus_t hipblasZtrsmBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int m, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *const AP[], int lda, hipDoubleComplex *const BP[], int ldb, int batchCount)[#](#_CPPv419hipblasZtrsmBatched15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPK16hipDoubleComplexA_PCK16hipDoubleComplexiA_PC16hipDoubleComplexii) BLAS Level 3 API.

trsmBatched performs the following batched operation:

where alpha is a scalar, X and B are batched m by n matrices, A is triangular batched matrix and op(A) is one ofop(A_i)*X_i = alpha*B_i or X_i*op(A_i) = alpha*B_i, for i = 1, ..., batchCount.

Each matrix X_i is overwritten on B_i for i = 1, …, batchCount.op( A ) = A or op( A ) = A^T or op( A ) = A^H.

Note about memory allocation: When trsm is launched with a k evenly divisible by the internal block size of 128, and is no larger than 10 of these blocks, the API takes advantage of utilizing pre-allocated memory found in the handle to increase overall performance (where k is m when HIPBLAS_SIDE_LEFT and is n when HIPBLAS_SIDE_RIGHT). For more information on pre-allocated memory in the handle, see the Device Memory Allocation in rocBLAS section of the rocBLAS API Reference.

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : s,d,c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**side**–**[in]**[hipblasSideMode_t] HIPBLAS_SIDE_LEFT: op(A)*X = alpha*B. HIPBLAS_SIDE_RIGHT: X*op(A) = alpha*B.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: each A_i is an upper triangular matrix. HIPBLAS_FILL_MODE_LOWER: each A_i is a lower triangular matrix.**transA**–**[in]**[hipblasOperation_t] HIPBLAS_OP_N: op(A) = A. HIPBLAS_OP_T: op(A) = A^T. HIPBLAS_OP_C: op(A) = A^H.**diag**–**[in]**[hipblasDiagType_t] HIPBLAS_DIAG_UNIT: each A_i is assumed to be unit triangular. HIPBLAS_DIAG_NON_UNIT: each A_i is not assumed to be unit triangular.**m**–**[in]**[int] m specifies the number of rows of each B_i. m >= 0.**n**–**[in]**[int] n specifies the number of columns of each B_i. n >= 0.**alpha**–**[in]**device pointer or host pointer specifying the scalar alpha. When alpha is &zero then A is not referenced and B need not be set before entry.**AP**–**[in]**device array of device pointers storing each matrix A_i on the GPU. Matricies are of dimension ( lda, k ), where k is m when HIPBLAS_SIDE_LEFT and is n when HIPBLAS_SIDE_RIGHT only the upper/lower triangular part is accessed.**lda**–**[in]**[int] lda specifies the first dimension of each A_i. if side = HIPBLAS_SIDE_LEFT, lda >= max( 1, m ), if side = HIPBLAS_SIDE_RIGHT, lda >= max( 1, n ).**BP**–**[inout]**device array of device pointers storing each matrix B_i on the GPU.**ldb**–**[in]**[int] ldb specifies the first dimension of each B_i. ldb >= max( 1, m ).**batchCount**–**[in]**[int] number of trsm operatons in the batch.



The `trsmBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasStrsmStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int m, int n, const float *alpha, const float *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, float *BP, int ldb,[hipblasStride](#_CPPv413hipblasStride)strideB, int batchCount)[#](#_CPPv426hipblasStrsmStridedBatched15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPKfPKfi13hipblasStridePfi13hipblasStridei)

-
hipblasStatus_t hipblasDtrsmStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int m, int n, const double *alpha, const double *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, double *BP, int ldb,[hipblasStride](#_CPPv413hipblasStride)strideB, int batchCount)[#](#_CPPv426hipblasDtrsmStridedBatched15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPKdPKdi13hipblasStridePdi13hipblasStridei)

-
hipblasStatus_t hipblasCtrsmStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int m, int n, const hipComplex *alpha, const hipComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, hipComplex *BP, int ldb,[hipblasStride](#_CPPv413hipblasStride)strideB, int batchCount)[#](#_CPPv426hipblasCtrsmStridedBatched15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPK10hipComplexPK10hipComplexi13hipblasStrideP10hipComplexi13hipblasStridei)

-
hipblasStatus_t hipblasZtrsmStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int m, int n, const hipDoubleComplex *alpha, const hipDoubleComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, hipDoubleComplex *BP, int ldb,[hipblasStride](#_CPPv413hipblasStride)strideB, int batchCount)[#](#_CPPv426hipblasZtrsmStridedBatched15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPK16hipDoubleComplexPK16hipDoubleComplexi13hipblasStrideP16hipDoubleComplexi13hipblasStridei) BLAS Level 3 API.

trsmSridedBatched performs the following strided batched operation:

where alpha is a scalar, X and B are strided batched m by n matrices, A is triangular strided batched matrix and op(A) is one ofop(A_i)*X_i = alpha*B_i or X_i*op(A_i) = alpha*B_i, for i = 1, ..., batchCount.

Each matrix X_i is overwritten on B_i for i = 1, …, batchCount.op( A ) = A or op( A ) = A^T or op( A ) = A^H.

Note about memory allocation: When trsm is launched with a k evenly divisible by the internal block size of 128, and is no larger than 10 of these blocks, the API takes advantage of utilizing pre-allocated memory found in the handle to increase overall performance (where k is m when HIPBLAS_SIDE_LEFT and is n when HIPBLAS_SIDE_RIGHT). For more information on pre-allocated memory in the handle, see the Device Memory Allocation in rocBLAS section of the rocBLAS API Reference.

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**side**–**[in]**[hipblasSideMode_t] HIPBLAS_SIDE_LEFT: op(A)*X = alpha*B. HIPBLAS_SIDE_RIGHT: X*op(A) = alpha*B.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: each A_i is an upper triangular matrix. HIPBLAS_FILL_MODE_LOWER: each A_i is a lower triangular matrix.**transA**–**[in]**[hipblasOperation_t] HIPBLAS_OP_N: op(A) = A. HIPBLAS_OP_T: op(A) = A^T. HIPBLAS_OP_C: op(A) = A^H.**diag**–**[in]**[hipblasDiagType_t] HIPBLAS_DIAG_UNIT: each A_i is assumed to be unit triangular. HIPBLAS_DIAG_NON_UNIT: each A_i is not assumed to be unit triangular.**m**–**[in]**[int] m specifies the number of rows of each B_i. m >= 0.**n**–**[in]**[int] n specifies the number of columns of each B_i. n >= 0.**alpha**–**[in]**device pointer or host pointer specifying the scalar alpha. When alpha is &zero then A is not referenced and B need not be set before entry.**AP**–**[in]**device pointer pointing to the first matrix A_1. of dimension ( lda, k ), where k is m when HIPBLAS_SIDE_LEFT and is n when HIPBLAS_SIDE_RIGHT only the upper/lower triangular part is accessed.**lda**–**[in]**[int] lda specifies the first dimension of each A_i. if side = HIPBLAS_SIDE_LEFT, lda >= max( 1, m ), if side = HIPBLAS_SIDE_RIGHT, lda >= max( 1, n ).**strideA**–**[in]**[hipblasStride] stride from the start of one A_i matrix to the next A_(i + 1).**BP**–**[inout]**device pointer pointing to the first matrix B_1.**ldb**–**[in]**[int] ldb specifies the first dimension of each B_i. ldb >= max( 1, m ).**strideB**–**[in]**[hipblasStride] stride from the start of one B_i matrix to the next B_(i + 1).**batchCount**–**[in]**[int] number of trsm operatons in the batch.



The `trsmStridedBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasStrtri(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const float *AP, int lda, float *invA, int ldinvA)[#](#_CPPv413hipblasStrtri15hipblasHandle_t17hipblasFillMode_t17hipblasDiagType_tiPKfiPfi)

-
hipblasStatus_t hipblasDtrtri(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const double *AP, int lda, double *invA, int ldinvA)[#](#_CPPv413hipblasDtrtri15hipblasHandle_t17hipblasFillMode_t17hipblasDiagType_tiPKdiPdi)

-
hipblasStatus_t hipblasCtrtri(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const hipComplex *AP, int lda, hipComplex *invA, int ldinvA)[#](#_CPPv413hipblasCtrtri15hipblasHandle_t17hipblasFillMode_t17hipblasDiagType_tiPK10hipComplexiP10hipComplexi)

-
hipblasStatus_t hipblasZtrtri(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const hipDoubleComplex *AP, int lda, hipDoubleComplex *invA, int ldinvA)[#](#_CPPv413hipblasZtrtri15hipblasHandle_t17hipblasFillMode_t17hipblasDiagType_tiPK16hipDoubleComplexiP16hipDoubleComplexi) BLAS Level 3 API.

trtri compute the inverse of a matrix A, namely, invA

and write the result into invA;

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] specifies whether the upper ‘HIPBLAS_FILL_MODE_UPPER’ or lower ‘HIPBLAS_FILL_MODE_LOWER’ if HIPBLAS_FILL_MODE_UPPER, the lower part of A is not referenced if HIPBLAS_FILL_MODE_LOWER, the upper part of A is not referenced**diag**–**[in]**[hipblasDiagType_t] = ‘HIPBLAS_DIAG_NON_UNIT’, A is non-unit triangular; = ‘HIPBLAS_DIAG_UNIT’, A is unit triangular;**n**–**[in]**[int] size of matrix A and invA**AP**–**[in]**device pointer storing matrix A.**lda**–**[in]**[int] specifies the leading dimension of A.**invA**–**[out]**device pointer storing matrix invA.**ldinvA**–**[in]**[int] specifies the leading dimension of invA.



-
hipblasStatus_t hipblasStrtriBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const float *const AP[], int lda, float *invA[], int ldinvA, int batchCount)[#](#_CPPv420hipblasStrtriBatched15hipblasHandle_t17hipblasFillMode_t17hipblasDiagType_tiA_PCKfiA_Pfii)

-
hipblasStatus_t hipblasDtrtriBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const double *const AP[], int lda, double *invA[], int ldinvA, int batchCount)[#](#_CPPv420hipblasDtrtriBatched15hipblasHandle_t17hipblasFillMode_t17hipblasDiagType_tiA_PCKdiA_Pdii)

-
hipblasStatus_t hipblasCtrtriBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const hipComplex *const AP[], int lda, hipComplex *invA[], int ldinvA, int batchCount)[#](#_CPPv420hipblasCtrtriBatched15hipblasHandle_t17hipblasFillMode_t17hipblasDiagType_tiA_PCK10hipComplexiA_P10hipComplexii)

-
hipblasStatus_t hipblasZtrtriBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const hipDoubleComplex *const AP[], int lda, hipDoubleComplex *invA[], int ldinvA, int batchCount)[#](#_CPPv420hipblasZtrtriBatched15hipblasHandle_t17hipblasFillMode_t17hipblasDiagType_tiA_PCK16hipDoubleComplexiA_P16hipDoubleComplexii) BLAS Level 3 API.

trtriBatched compute the inverse of A_i and write into invA_i where A_i and invA_i are the i-th matrices in the batch, for i = 1, …, batchCount.

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] specifies whether the upper ‘HIPBLAS_FILL_MODE_UPPER’ or lower ‘HIPBLAS_FILL_MODE_LOWER’**diag**–**[in]**[hipblasDiagType_t] = ‘HIPBLAS_DIAG_NON_UNIT’, A is non-unit triangular; = ‘HIPBLAS_DIAG_UNIT’, A is unit triangular;**n**–**[in]**[int]**AP**–**[in]**device array of device pointers storing each matrix A_i.**lda**–**[in]**[int] specifies the leading dimension of each A_i.**invA**–**[out]**device array of device pointers storing the inverse of each matrix A_i. Partial inplace operation is supported, see below. If UPLO = ‘U’, the leading N-by-N upper triangular part of the invA will store the inverse of the upper triangular matrix, and the strictly lower triangular part of invA is cleared. If UPLO = ‘L’, the leading N-by-N lower triangular part of the invA will store the inverse of the lower triangular matrix, and the strictly upper triangular part of invA is cleared.**ldinvA**–**[in]**[int] specifies the leading dimension of each invA_i.**batchCount**–**[in]**[int] numbers of matrices in the batch



-
hipblasStatus_t hipblasStrtriStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const float *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, float *invA, int ldinvA,[hipblasStride](#_CPPv413hipblasStride)stride_invA, int batchCount)[#](#_CPPv427hipblasStrtriStridedBatched15hipblasHandle_t17hipblasFillMode_t17hipblasDiagType_tiPKfi13hipblasStridePfi13hipblasStridei)

-
hipblasStatus_t hipblasDtrtriStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const double *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, double *invA, int ldinvA,[hipblasStride](#_CPPv413hipblasStride)stride_invA, int batchCount)[#](#_CPPv427hipblasDtrtriStridedBatched15hipblasHandle_t17hipblasFillMode_t17hipblasDiagType_tiPKdi13hipblasStridePdi13hipblasStridei)

-
hipblasStatus_t hipblasCtrtriStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const hipComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, hipComplex *invA, int ldinvA,[hipblasStride](#_CPPv413hipblasStride)stride_invA, int batchCount)[#](#_CPPv427hipblasCtrtriStridedBatched15hipblasHandle_t17hipblasFillMode_t17hipblasDiagType_tiPK10hipComplexi13hipblasStrideP10hipComplexi13hipblasStridei)

-
hipblasStatus_t hipblasZtrtriStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int n, const hipDoubleComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, hipDoubleComplex *invA, int ldinvA,[hipblasStride](#_CPPv413hipblasStride)stride_invA, int batchCount)[#](#_CPPv427hipblasZtrtriStridedBatched15hipblasHandle_t17hipblasFillMode_t17hipblasDiagType_tiPK16hipDoubleComplexi13hipblasStrideP16hipDoubleComplexi13hipblasStridei) BLAS Level 3 API.

trtriStridedBatched compute the inverse of A_i and write into invA_i where A_i and invA_i are the i-th matrices in the batch, for i = 1, …, batchCount

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**uplo**–**[in]**[hipblasFillMode_t] specifies whether the upper ‘HIPBLAS_FILL_MODE_UPPER’ or lower ‘HIPBLAS_FILL_MODE_LOWER’**diag**–**[in]**[hipblasDiagType_t] = ‘HIPBLAS_DIAG_NON_UNIT’, A is non-unit triangular; = ‘HIPBLAS_DIAG_UNIT’, A is unit triangular;**n**–**[in]**[int]**AP**–**[in]**device pointer pointing to address of first matrix A_1.**lda**–**[in]**[int] specifies the leading dimension of each A.**strideA**–**[in]**[hipblasStride] “batch stride a”: stride from the start of one A_i matrix to the next A_(i + 1).**invA**–**[out]**device pointer storing the inverses of each matrix A_i. Partial inplace operation is supported, see below. If UPLO = ‘U’, the leading N-by-N upper triangular part of the invA will store the inverse of the upper triangular matrix, and the strictly lower triangular part of invA is cleared. If UPLO = ‘L’, the leading N-by-N lower triangular part of the invA will store the inverse of the lower triangular matrix, and the strictly upper triangular part of invA is cleared.**ldinvA**–**[in]**[int] specifies the leading dimension of each invA_i.**stride_invA**–**[in]**[hipblasStride] “batch stride invA”: stride from the start of one invA_i matrix to the next invA_(i + 1).**batchCount**–**[in]**[int] numbers of matrices in the batch



-
hipblasStatus_t hipblasSdgmm(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side, int m, int n, const float *AP, int lda, const float *x, int incx, float *CP, int ldc)[#](#_CPPv412hipblasSdgmm15hipblasHandle_t17hipblasSideMode_tiiPKfiPKfiPfi)

-
hipblasStatus_t hipblasDdgmm(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side, int m, int n, const double *AP, int lda, const double *x, int incx, double *CP, int ldc)[#](#_CPPv412hipblasDdgmm15hipblasHandle_t17hipblasSideMode_tiiPKdiPKdiPdi)

-
hipblasStatus_t hipblasCdgmm(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side, int m, int n, const hipComplex *AP, int lda, const hipComplex *x, int incx, hipComplex *CP, int ldc)[#](#_CPPv412hipblasCdgmm15hipblasHandle_t17hipblasSideMode_tiiPK10hipComplexiPK10hipComplexiP10hipComplexi)

-
hipblasStatus_t hipblasZdgmm(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side, int m, int n, const hipDoubleComplex *AP, int lda, const hipDoubleComplex *x, int incx, hipDoubleComplex *CP, int ldc)[#](#_CPPv412hipblasZdgmm15hipblasHandle_t17hipblasSideMode_tiiPK16hipDoubleComplexiPK16hipDoubleComplexiP16hipDoubleComplexi) BLAS Level 3 API.

dgmm performs one of the matrix-matrix operations

where C and A are m by n dimensional matrices. diag( x ) is a diagonal matrix and x is vector of dimension n if side == HIPBLAS_SIDE_RIGHT and dimension m if side == HIPBLAS_SIDE_LEFT.C = A * diag(x) if side == HIPBLAS_SIDE_RIGHT C = diag(x) * A if side == HIPBLAS_SIDE_LEFT

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : s,d,c,z


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**side**–**[in]**[hipblasSideMode_t] specifies the side of diag(x)**m**–**[in]**[int] matrix dimension m.**n**–**[in]**[int] matrix dimension n.**AP**–**[in]**device pointer storing matrix A.**lda**–**[in]**[int] specifies the leading dimension of A.**x**–**[in]**device pointer storing vector x.**incx**–**[in]**[int] specifies the increment between values of x**CP**–**[inout]**device pointer storing matrix C.**ldc**–**[in]**[int] specifies the leading dimension of C.



The `dgmm`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSdgmmBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side, int m, int n, const float *const AP[], int lda, const float *const x[], int incx, float *const CP[], int ldc, int batchCount)[#](#_CPPv419hipblasSdgmmBatched15hipblasHandle_t17hipblasSideMode_tiiA_PCKfiA_PCKfiA_PCfii)

-
hipblasStatus_t hipblasDdgmmBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side, int m, int n, const double *const AP[], int lda, const double *const x[], int incx, double *const CP[], int ldc, int batchCount)[#](#_CPPv419hipblasDdgmmBatched15hipblasHandle_t17hipblasSideMode_tiiA_PCKdiA_PCKdiA_PCdii)

-
hipblasStatus_t hipblasCdgmmBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side, int m, int n, const hipComplex *const AP[], int lda, const hipComplex *const x[], int incx, hipComplex *const CP[], int ldc, int batchCount)[#](#_CPPv419hipblasCdgmmBatched15hipblasHandle_t17hipblasSideMode_tiiA_PCK10hipComplexiA_PCK10hipComplexiA_PC10hipComplexii)

-
hipblasStatus_t hipblasZdgmmBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side, int m, int n, const hipDoubleComplex *const AP[], int lda, const hipDoubleComplex *const x[], int incx, hipDoubleComplex *const CP[], int ldc, int batchCount)[#](#_CPPv419hipblasZdgmmBatched15hipblasHandle_t17hipblasSideMode_tiiA_PCK16hipDoubleComplexiA_PCK16hipDoubleComplexiA_PC16hipDoubleComplexii) BLAS Level 3 API.

dgmmBatched performs one of the batched matrix-matrix operations

where C_i and A_i are m by n dimensional matrices. diag(x_i) is a diagonal matrix and x_i is vector of dimension n if side == HIPBLAS_SIDE_RIGHT and dimension m if side == HIPBLAS_SIDE_LEFT.C_i = A_i * diag(x_i) for i = 0, 1, ... batchCount-1 if side == HIPBLAS_SIDE_RIGHT C_i = diag(x_i) * A_i for i = 0, 1, ... batchCount-1 if side == HIPBLAS_SIDE_LEFT

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**side**–**[in]**[hipblasSideMode_t] specifies the side of diag(x)**m**–**[in]**[int] matrix dimension m.**n**–**[in]**[int] matrix dimension n.**AP**–**[in]**device array of device pointers storing each matrix A_i on the GPU. Each A_i is of dimension ( lda, n )**lda**–**[in]**[int] specifies the leading dimension of A_i.**x**–**[in]**device array of device pointers storing each vector x_i on the GPU. Each x_i is of dimension n if side == HIPBLAS_SIDE_RIGHT and dimension m if side == HIPBLAS_SIDE_LEFT**incx**–**[in]**[int] specifies the increment between values of x_i**CP**–**[inout]**device array of device pointers storing each matrix C_i on the GPU. Each C_i is of dimension ( ldc, n ).**ldc**–**[in]**[int] specifies the leading dimension of C_i.**batchCount**–**[in]**[int] number of instances in the batch.



The `dgmmBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasSdgmmStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side, int m, int n, const float *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const float *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, float *CP, int ldc,[hipblasStride](#_CPPv413hipblasStride)strideC, int batchCount)[#](#_CPPv426hipblasSdgmmStridedBatched15hipblasHandle_t17hipblasSideMode_tiiPKfi13hipblasStridePKfi13hipblasStridePfi13hipblasStridei)

-
hipblasStatus_t hipblasDdgmmStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side, int m, int n, const double *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const double *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, double *CP, int ldc,[hipblasStride](#_CPPv413hipblasStride)strideC, int batchCount)[#](#_CPPv426hipblasDdgmmStridedBatched15hipblasHandle_t17hipblasSideMode_tiiPKdi13hipblasStridePKdi13hipblasStridePdi13hipblasStridei)

-
hipblasStatus_t hipblasCdgmmStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side, int m, int n, const hipComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const hipComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, hipComplex *CP, int ldc,[hipblasStride](#_CPPv413hipblasStride)strideC, int batchCount)[#](#_CPPv426hipblasCdgmmStridedBatched15hipblasHandle_t17hipblasSideMode_tiiPK10hipComplexi13hipblasStridePK10hipComplexi13hipblasStrideP10hipComplexi13hipblasStridei)

-
hipblasStatus_t hipblasZdgmmStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side, int m, int n, const hipDoubleComplex *AP, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const hipDoubleComplex *x, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, hipDoubleComplex *CP, int ldc,[hipblasStride](#_CPPv413hipblasStride)strideC, int batchCount)[#](#_CPPv426hipblasZdgmmStridedBatched15hipblasHandle_t17hipblasSideMode_tiiPK16hipDoubleComplexi13hipblasStridePK16hipDoubleComplexi13hipblasStrideP16hipDoubleComplexi13hipblasStridei) BLAS Level 3 API.

dgmmStridedBatched performs one of the batched matrix-matrix operations

where C_i and A_i are m by n dimensional matrices. diag(x_i) is a diagonal matrix and x_i is vector of dimension n if side == HIPBLAS_SIDE_RIGHT and dimension m if side == HIPBLAS_SIDE_LEFT.C_i = A_i * diag(x_i) if side == HIPBLAS_SIDE_RIGHT for i = 0, 1, ... batchCount-1 C_i = diag(x_i) * A_i if side == HIPBLAS_SIDE_LEFT for i = 0, 1, ... batchCount-1

Supported precisions in rocBLAS : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**side**–**[in]**[hipblasSideMode_t] specifies the side of diag(x)**m**–**[in]**[int] matrix dimension m.**n**–**[in]**[int] matrix dimension n.**AP**–**[in]**device pointer to the first matrix A_0 on the GPU. Each A_i is of dimension ( lda, n )**lda**–**[in]**[int] specifies the leading dimension of A.**strideA**–**[in]**[hipblasStride] stride from the start of one matrix (A_i) and the next one (A_i+1)**x**–**[in]**pointer to the first vector x_0 on the GPU. Each x_i is of dimension n if side == HIPBLAS_SIDE_RIGHT and dimension m if side == HIPBLAS_SIDE_LEFT**incx**–**[in]**[int] specifies the increment between values of x**stridex**–**[in]**[hipblasStride] stride from the start of one vector(x_i) and the next one (x_i+1)**CP**–**[inout]**device pointer to the first matrix C_0 on the GPU. Each C_i is of dimension ( ldc, n ).**ldc**–**[in]**[int] specifies the leading dimension of C.**strideC**–**[in]**[hipblasStride] stride from the start of one matrix (C_i) and the next one (C_i+1)**batchCount**–**[in]**[int] number of instances i in the batch.



The `dgmmStridedBatched`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

## BLAS extensions[#](#blas-extensions)

-
hipblasStatus_t hipblasGemmEx(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transB, int m, int n, int k, const void *alpha, const void *A, hipDataType aType, int lda, const void *B, hipDataType bType, int ldb, const void *beta, void *C, hipDataType cType, int ldc, hipblasComputeType_t computeType,[hipblasGemmAlgo_t](#_CPPv417hipblasGemmAlgo_t)algo)[#](#_CPPv413hipblasGemmEx15hipblasHandle_t18hipblasOperation_t18hipblasOperation_tiiiPKvPKv11hipDataTypeiPKv11hipDataTypeiPKvPv11hipDataTypei20hipblasComputeType_t17hipblasGemmAlgo_t) BLAS EX API.

gemmEx performs one of the matrix-matrix operations

where op( X ) is one ofC = alpha*op( A )*op( B ) + beta*C,

alpha and beta are scalars, and A, B, and C are matrices, with op( A ) an m by k matrix, op( B ) a k by n matrix and C is a m by n matrix.op( X ) = X or op( X ) = X**T or op( X ) = X**H,

Supported types are determined by the backend. See cuBLAS documentation for cuBLAS backend. For rocBLAS backend, conversion from hipblasComputeType_t to rocblas_datatype_t happens within hipBLAS. Supported types are as follows:


aType

bType

cType

computeType

HIP_R_16F

HIP_R_16F

HIP_R_16F

HIPBLAS_COMPUTE_16F

HIP_R_16F

HIP_R_16F

HIP_R_16F

HIPBLAS_COMPUTE_32F

HIP_R_16F

HIP_R_16F

HIP_R_32F

HIPBLAS_COMPUTE_32F

HIP_R_16BF

HIP_R_16BF

HIP_R_16BF

HIPBLAS_COMPUTE_32F

HIP_R_16BF

HIP_R_16BF

HIP_R_32F

HIPBLAS_COMPUTE_32F

HIP_R_32F

HIP_R_32F

HIP_R_32F

HIPBLAS_COMPUTE_32F

HIP_R_64F

HIP_R_64F

HIP_R_64F

HIPBLAS_COMPUTE_64F

HIP_R_8I

HIP_R_8I

HIP_R_32I

HIPBLAS_COMPUTE_32I

HIP_C_32F

HIP_C_32F

HIP_C_32F

HIPBLAS_COMPUTE_32F

HIP_C_64F

HIP_C_64F

HIP_C_64F

HIPBLAS_COMPUTE_64F

hipblasGemmExWithFlags is also available which is identical to hipblasGemmEx with the addition of a “flags” parameter which controls flags used in Tensile to control gemm algorithms with the rocBLAS backend. When using a cuBLAS backend this parameter is ignored.

- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**transA**–**[in]**[hipblasOperation_t] specifies the form of op( A ).**transB**–**[in]**[hipblasOperation_t] specifies the form of op( B ).**m**–**[in]**[int] matrix dimension m.**n**–**[in]**[int] matrix dimension n.**k**–**[in]**[int] matrix dimension k.**alpha**–**[in]**[const void *] device pointer or host pointer specifying the scalar alpha. Same datatype as computeType.**A**–**[in]**[void *] device pointer storing matrix A.**aType**–**[in]**[hipDataType] specifies the datatype of matrix A.**lda**–**[in]**[int] specifies the leading dimension of A.**B**–**[in]**[void *] device pointer storing matrix B.**bType**–**[in]**[hipDataType] specifies the datatype of matrix B.**ldb**–**[in]**[int] specifies the leading dimension of B.**beta**–**[in]**[const void *] device pointer or host pointer specifying the scalar beta. Same datatype as computeType.**C**–**[in]**[void *] device pointer storing matrix C.**cType**–**[in]**[hipDataType] specifies the datatype of matrix C.**ldc**–**[in]**[int] specifies the leading dimension of C.**computeType**–**[in]**[hipblasComputeType_t] specifies the datatype of computation.**algo**–**[in]**[hipblasGemmAlgo_t] enumerant specifying the algorithm type.



-
hipblasStatus_t hipblasGemmBatchedEx(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transB, int m, int n, int k, const void *alpha, const void *A[], hipDataType aType, int lda, const void *B[], hipDataType bType, int ldb, const void *beta, void *C[], hipDataType cType, int ldc, int batchCount, hipblasComputeType_t computeType,[hipblasGemmAlgo_t](#_CPPv417hipblasGemmAlgo_t)algo)[#](#_CPPv420hipblasGemmBatchedEx15hipblasHandle_t18hipblasOperation_t18hipblasOperation_tiiiPKvA_PKv11hipDataTypeiA_PKv11hipDataTypeiPKvA_Pv11hipDataTypeii20hipblasComputeType_t17hipblasGemmAlgo_t) BLAS EX API.

gemmBatchedEx performs one of the batched matrix-matrix operations C_i = alpha*op(A_i)*op(B_i) + beta*C_i, for i = 1, …, batchCount. where op( X ) is one of op( X ) = X or op( X ) = X**T or op( X ) = X**H, alpha and beta are scalars, and A, B, and C are batched pointers to matrices, with op( A ) an m by k by batchCount batched matrix, op( B ) a k by n by batchCount batched matrix and C a m by n by batchCount batched matrix. The batched matrices are an array of pointers to matrices. The number of pointers to matrices is batchCount.

Supported types are determined by the backend. See rocBLAS/cuBLAS documentation.


hipblasGemmBatchedExWithFlags is also available which is identical to hipblasGemmBatchedEx with the addition of a “flags” parameter which controls flags used in Tensile to control gemm algorithms with the rocBLAS backend. When using a cuBLAS backend this parameter is ignored.

- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**transA**–**[in]**[hipblasOperation_t] specifies the form of op( A ).**transB**–**[in]**[hipblasOperation_t] specifies the form of op( B ).**m**–**[in]**[int] matrix dimension m.**n**–**[in]**[int] matrix dimension n.**k**–**[in]**[int] matrix dimension k.**alpha**–**[in]**[const void *] device pointer or host pointer specifying the scalar alpha. Same datatype as computeType.**A**–**[in]**[void *] device pointer storing array of pointers to each matrix A_i.**aType**–**[in]**[hipDataType] specifies the datatype of each matrix A_i.**lda**–**[in]**[int] specifies the leading dimension of each A_i.**B**–**[in]**[void *] device pointer storing array of pointers to each matrix B_i.**bType**–**[in]**[hipDataType] specifies the datatype of each matrix B_i.**ldb**–**[in]**[int] specifies the leading dimension of each B_i.**beta**–**[in]**[const void *] device pointer or host pointer specifying the scalar beta. Same datatype as computeType.**C**–**[in]**[void *] device array of device pointers to each matrix C_i.**cType**–**[in]**[hipDataType] specifies the datatype of each matrix C_i.**ldc**–**[in]**[int] specifies the leading dimension of each C_i.**batchCount**–**[in]**[int] number of gemm operations in the batch.**computeType**–**[in]**[hipblasComputeType_t] specifies the datatype of computation.**algo**–**[in]**[hipblasGemmAlgo_t] enumerant specifying the algorithm type.



-
hipblasStatus_t hipblasGemmStridedBatchedEx(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transB, int m, int n, int k, const void *alpha, const void *A, hipDataType aType, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, const void *B, hipDataType bType, int ldb,[hipblasStride](#_CPPv413hipblasStride)strideB, const void *beta, void *C, hipDataType cType, int ldc,[hipblasStride](#_CPPv413hipblasStride)strideC, int batchCount, hipblasComputeType_t computeType,[hipblasGemmAlgo_t](#_CPPv417hipblasGemmAlgo_t)algo)[#](#_CPPv427hipblasGemmStridedBatchedEx15hipblasHandle_t18hipblasOperation_t18hipblasOperation_tiiiPKvPKv11hipDataTypei13hipblasStridePKv11hipDataTypei13hipblasStridePKvPv11hipDataTypei13hipblasStridei20hipblasComputeType_t17hipblasGemmAlgo_t) BLAS EX API.

gemmStridedBatchedEx performs one of the strided_batched matrix-matrix operations

where op( X ) is one ofC_i = alpha*op(A_i)*op(B_i) + beta*C_i, for i = 1, ..., batchCount

alpha and beta are scalars, and A, B, and C are strided_batched matrices, with op( A ) an m by k by batchCount strided_batched matrix, op( B ) a k by n by batchCount strided_batched matrix and C a m by n by batchCount strided_batched matrix.op( X ) = X or op( X ) = X**T or op( X ) = X**H,

The strided_batched matrices are multiple matrices separated by a constant stride. The number of matrices is batchCount.

Supported types are determined by the backend. See rocBLAS/cuBLAS documentation.


hipblasGemmStridedBatchedExWithFlags is also available which is identical to hipblasStridedBatchedGemmEx with the addition of a “flags” parameter which controls flags used in Tensile to control gemm algorithms with the rocBLAS backend. When using a cuBLAS backend this parameter is ignored.

- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**transA**–**[in]**[hipblasOperation_t] specifies the form of op( A ).**transB**–**[in]**[hipblasOperation_t] specifies the form of op( B ).**m**–**[in]**[int] matrix dimension m.**n**–**[in]**[int] matrix dimension n.**k**–**[in]**[int] matrix dimension k.**alpha**–**[in]**[const void *] device pointer or host pointer specifying the scalar alpha. Same datatype as computeType.**A**–**[in]**[void *] device pointer pointing to first matrix A_1.**aType**–**[in]**[hipDataType] specifies the datatype of each matrix A_i.**lda**–**[in]**[int] specifies the leading dimension of each A_i.**strideA**–**[in]**[hipblasStride] specifies stride from start of one A_i matrix to the next A_(i + 1).**B**–**[in]**[void *] device pointer pointing to first matrix B_1.**bType**–**[in]**[hipDataType] specifies the datatype of each matrix B_i.**ldb**–**[in]**[int] specifies the leading dimension of each B_i.**strideB**–**[in]**[hipblasStride] specifies stride from start of one B_i matrix to the next B_(i + 1).**beta**–**[in]**[const void *] device pointer or host pointer specifying the scalar beta. Same datatype as computeType.**C**–**[in]**[void *] device pointer pointing to first matrix C_1.**cType**–**[in]**[hipDataType] specifies the datatype of each matrix C_i.**ldc**–**[in]**[int] specifies the leading dimension of each C_i.**strideC**–**[in]**[hipblasStride] specifies stride from start of one C_i matrix to the next C_(i + 1).**batchCount**–**[in]**[int] number of gemm operations in the batch.**computeType**–**[in]**[hipblasComputeType_t] specifies the datatype of computation.**algo**–**[in]**[hipblasGemmAlgo_t] enumerant specifying the algorithm type.



The `gemmEx`

, `gemmBatchedEx`

, and `gemmStridedBatchedEx`

functions support the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasTrsmEx(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int m, int n, const void *alpha, void *A, int lda, void *B, int ldb, const void *invA, int invAsize, hipDataType computeType)[#](#_CPPv413hipblasTrsmEx15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPKvPviPviPKvi11hipDataType) BLAS EX API

trsmEx solves

where alpha is a scalar, X and B are m by n matrices, A is triangular matrix and op(A) is one ofop(A)*X = alpha*B or X*op(A) = alpha*B,

The matrix X is overwritten on B.op( A ) = A or op( A ) = A^T or op( A ) = A^H.

This function gives the user the ability to reuse the invA matrix between runs. If invA == NULL, hipblasTrsmEx will automatically calculate invA on every run.

Setting up invA: The accepted invA matrix consists of the packed 128x128 inverses of the diagonal blocks of matrix A, followed by any smaller diagonal block that remains. To set up invA it is recommended that hipblasTrtriBatched be used with matrix A as the input.

Device memory of size 128 x k should be allocated for invA ahead of time, where k is m when HIPBLAS_SIDE_LEFT and is n when HIPBLAS_SIDE_RIGHT. The actual number of elements in invA should be passed as invAsize.

To begin, hipblasTrtriBatched must be called on the full 128x128 sized diagonal blocks of matrix A. Below are the restricted parameters:

n = 128

ldinvA = 128

stride_invA = 128x128

batchCount = k / 128,


Then any remaining block may be added:

n = k % 128

invA = invA + stride_invA * previousBatchCount

ldinvA = 128

batchCount = 1


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**side**–**[in]**[hipblasSideMode_t] HIPBLAS_SIDE_LEFT: op(A)*X = alpha*B. HIPBLAS_SIDE_RIGHT: X*op(A) = alpha*B.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: A is an upper triangular matrix. HIPBLAS_FILL_MODE_LOWER: A is a lower triangular matrix.**transA**–**[in]**[hipblasOperation_t] HIPBLAS_OP_N: op(A) = A. HIPBLAS_OP_T: op(A) = A^T. HIPBLAS_ON_C: op(A) = A^H.**diag**–**[in]**[hipblasDiagType_t] HIPBLAS_DIAG_UNIT: A is assumed to be unit triangular. HIPBLAS_DIAG_NON_UNIT: A is not assumed to be unit triangular.**m**–**[in]**[int] m specifies the number of rows of B. m >= 0.**n**–**[in]**[int] n specifies the number of columns of B. n >= 0.**alpha**–**[in]**[void *] device pointer or host pointer specifying the scalar alpha. When alpha is &zero then A is not referenced, and B need not be set before entry.**A**–**[in]**[void *] device pointer storing matrix A. of dimension ( lda, k ), where k is m when HIPBLAS_SIDE_LEFT and is n when HIPBLAS_SIDE_RIGHT only the upper/lower triangular part is accessed.**lda**–**[in]**[int] lda specifies the first dimension of A. if side = HIPBLAS_SIDE_LEFT, lda >= max( 1, m ), if side = HIPBLAS_SIDE_RIGHT, lda >= max( 1, n ).**B**–**[inout]**[void *] device pointer storing matrix B. B is of dimension ( ldb, n ). Before entry, the leading m by n part of the array B must contain the right-hand side matrix B, and on exit is overwritten by the solution matrix X.**ldb**–**[in]**[int] ldb specifies the first dimension of B. ldb >= max( 1, m ).**invA**–**[in]**[void *] device pointer storing the inverse diagonal blocks of A. invA is of dimension ( ld_invA, k ), where k is m when HIPBLAS_SIDE_LEFT and is n when HIPBLAS_SIDE_RIGHT. ld_invA must be equal to 128.**invAsize**–**[in]**[int] invAsize specifies the number of elements of device memory in invA.**computeType**–**[in]**[hipDataType] specifies the datatype of computation.



-
hipblasStatus_t hipblasTrsmBatchedEx(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int m, int n, const void *alpha, void *A, int lda, void *B, int ldb, int batchCount, const void *invA, int invAsize, hipDataType computeType)[#](#_CPPv420hipblasTrsmBatchedEx15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPKvPviPviiPKvi11hipDataType) BLAS EX API

trsmBatchedEx solves

for i = 1, …, batchCount; and where alpha is a scalar, X and B are arrays of m by n matrices, A is an array of triangular matrix and each op(A_i) is one ofop(A_i)*X_i = alpha*B_i or X_i*op(A_i) = alpha*B_i,

Each matrix X_i is overwritten on B_i.op( A_i ) = A_i or op( A_i ) = A_i^T or op( A_i ) = A_i^H.

This function gives the user the ability to reuse the invA matrix between runs. If invA == NULL, hipblasTrsmBatchedEx will automatically calculate each invA_i on every run.

Setting up invA: Each accepted invA_i matrix consists of the packed 128x128 inverses of the diagonal blocks of matrix A_i, followed by any smaller diagonal block that remains. To set up each invA_i it is recommended that hipblasTrtriBatched be used with matrix A_i as the input. invA is an array of pointers of batchCount length holding each invA_i.

Device memory of size 128 x k should be allocated for each invA_i ahead of time, where k is m when HIPBLAS_SIDE_LEFT and is n when HIPBLAS_SIDE_RIGHT. The actual number of elements in each invA_i should be passed as invAsize.

To begin, hipblasTrtriBatched must be called on the full 128x128 sized diagonal blocks of each matrix A_i. Below are the restricted parameters:

n = 128

ldinvA = 128

stride_invA = 128x128

batchCount = k / 128,


Then any remaining block may be added:

n = k % 128

invA = invA + stride_invA * previousBatchCount

ldinvA = 128

batchCount = 1


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**side**–**[in]**[hipblasSideMode_t] HIPBLAS_SIDE_LEFT: op(A)*X = alpha*B. HIPBLAS_SIDE_RIGHT: X*op(A) = alpha*B.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: each A_i is an upper triangular matrix. HIPBLAS_FILL_MODE_LOWER: each A_i is a lower triangular matrix.**transA**–**[in]**[hipblasOperation_t] HIPBLAS_OP_N: op(A) = A. HIPBLAS_OP_T: op(A) = A^T. HIPBLAS_OP_C: op(A) = A^H.**diag**–**[in]**[hipblasDiagType_t] HIPBLAS_DIAG_UNIT: each A_i is assumed to be unit triangular. HIPBLAS_DIAG_NON_UNIT: each A_i is not assumed to be unit triangular.**m**–**[in]**[int] m specifies the number of rows of each B_i. m >= 0.**n**–**[in]**[int] n specifies the number of columns of each B_i. n >= 0.**alpha**–**[in]**[void *] device pointer or host pointer alpha specifying the scalar alpha. When alpha is &zero then A is not referenced, and B need not be set before entry.**A**–**[in]**[void *] device array of device pointers storing each matrix A_i. each A_i is of dimension ( lda, k ), where k is m when HIPBLAS_SIDE_LEFT and is n when HIPBLAS_SIDE_RIGHT only the upper/lower triangular part is accessed.**lda**–**[in]**[int] lda specifies the first dimension of each A_i. if side = HIPBLAS_SIDE_LEFT, lda >= max( 1, m ), if side = HIPBLAS_SIDE_RIGHT, lda >= max( 1, n ).**B**–**[inout]**[void *] device array of device pointers storing each matrix B_i. each B_i is of dimension ( ldb, n ). Before entry, the leading m by n part of the array B_i must contain the right-hand side matrix B_i, and on exit is overwritten by the solution matrix X_i**ldb**–**[in]**[int] ldb specifies the first dimension of each B_i. ldb >= max( 1, m ).**batchCount**–**[in]**[int] specifies how many batches.**invA**–**[in]**[void *] device array of device pointers storing the inverse diagonal blocks of each A_i. each invA_i is of dimension ( ld_invA, k ), where k is m when HIPBLAS_SIDE_LEFT and is n when HIPBLAS_SIDE_RIGHT. ld_invA must be equal to 128.**invAsize**–**[in]**[int] invAsize specifies the number of elements of device memory in each invA_i.**computeType**–**[in]**[hipDataType] specifies the datatype of computation.



-
hipblasStatus_t hipblasTrsmStridedBatchedEx(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasSideMode_t](#_CPPv417hipblasSideMode_t)side,[hipblasFillMode_t](#_CPPv417hipblasFillMode_t)uplo,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)transA,[hipblasDiagType_t](#_CPPv417hipblasDiagType_t)diag, int m, int n, const void *alpha, void *A, int lda,[hipblasStride](#_CPPv413hipblasStride)strideA, void *B, int ldb,[hipblasStride](#_CPPv413hipblasStride)strideB, int batchCount, const void *invA, int invAsize,[hipblasStride](#_CPPv413hipblasStride)strideInvA, hipDataType computeType)[#](#_CPPv427hipblasTrsmStridedBatchedEx15hipblasHandle_t17hipblasSideMode_t17hipblasFillMode_t18hipblasOperation_t17hipblasDiagType_tiiPKvPvi13hipblasStridePvi13hipblasStrideiPKvi13hipblasStride11hipDataType) BLAS EX API

trsmStridedBatchedEx solves

for i = 1, …, batchCount; and where alpha is a scalar, X and B are strided batched m by n matrices, A is a strided batched triangular matrix and op(A_i) is one ofop(A_i)*X_i = alpha*B_i or X_i*op(A_i) = alpha*B_i,

Each matrix X_i is overwritten on B_i.op( A_i ) = A_i or op( A_i ) = A_i^T or op( A_i ) = A_i^H.

This function gives the user the ability to reuse each invA_i matrix between runs. If invA == NULL, hipblasTrsmStridedBatchedEx will automatically calculate each invA_i on every run.

Setting up invA: Each accepted invA_i matrix consists of the packed 128x128 inverses of the diagonal blocks of matrix A_i, followed by any smaller diagonal block that remains. To set up invA_i it is recommended that hipblasTrtriBatched be used with matrix A_i as the input. invA is a contiguous piece of memory holding each invA_i.

Device memory of size 128 x k should be allocated for each invA_i ahead of time, where k is m when HIPBLAS_SIDE_LEFT and is n when HIPBLAS_SIDE_RIGHT. The actual number of elements in each invA_i should be passed as invAsize.

To begin, hipblasTrtriBatched must be called on the full 128x128 sized diagonal blocks of each matrix A_i. Below are the restricted parameters:

n = 128

ldinvA = 128

stride_invA = 128x128

batchCount = k / 128,


Then any remaining block may be added:

n = k % 128

invA = invA + stride_invA * previousBatchCount

ldinvA = 128

batchCount = 1


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**side**–**[in]**[hipblasSideMode_t] HIPBLAS_SIDE_LEFT: op(A)*X = alpha*B. HIPBLAS_SIDE_RIGHT: X*op(A) = alpha*B.**uplo**–**[in]**[hipblasFillMode_t] HIPBLAS_FILL_MODE_UPPER: each A_i is an upper triangular matrix. HIPBLAS_FILL_MODE_LOWER: each A_i is a lower triangular matrix.**transA**–**[in]**[hipblasOperation_t] HIPBLAS_OP_N: op(A) = A. HIPBLAS_OP_T: op(A) = A^T. HIPBLAS_OP_C: op(A) = A^H.**diag**–**[in]**[hipblasDiagType_t] HIPBLAS_DIAG_UNIT: each A_i is assumed to be unit triangular. HIPBLAS_DIAG_NON_UNIT: each A_i is not assumed to be unit triangular.**m**–**[in]**[int] m specifies the number of rows of each B_i. m >= 0.**n**–**[in]**[int] n specifies the number of columns of each B_i. n >= 0.**alpha**–**[in]**[void *] device pointer or host pointer specifying the scalar alpha. When alpha is &zero then A is not referenced, and B need not be set before entry.**A**–**[in]**[void *] device pointer storing matrix A. of dimension ( lda, k ), where k is m when HIPBLAS_SIDE_LEFT and is n when HIPBLAS_SIDE_RIGHT only the upper/lower triangular part is accessed.**lda**–**[in]**[int] lda specifies the first dimension of A. if side = HIPBLAS_SIDE_LEFT, lda >= max( 1, m ), if side = HIPBLAS_SIDE_RIGHT, lda >= max( 1, n ).**strideA**–**[in]**[hipblasStride] The stride between each A matrix.**B**–**[inout]**[void *] device pointer pointing to first matrix B_i. each B_i is of dimension ( ldb, n ). Before entry, the leading m by n part of each array B_i must contain the right-hand side of matrix B_i, and on exit is overwritten by the solution matrix X_i.**ldb**–**[in]**[int] ldb specifies the first dimension of each B_i. ldb >= max( 1, m ).**strideB**–**[in]**[hipblasStride] The stride between each B_i matrix.**batchCount**–**[in]**[int] specifies how many batches.**invA**–**[in]**[void *] device pointer storing the inverse diagonal blocks of each A_i. invA points to the first invA_1. each invA_i is of dimension ( ld_invA, k ), where k is m when HIPBLAS_SIDE_LEFT and is n when HIPBLAS_SIDE_RIGHT. ld_invA must be equal to 128.**invAsize**–**[in]**[int] invAsize specifies the number of elements of device memory in each invA_i.**strideInvA**–**[in]**[hipblasStride] The stride between each invA matrix.**computeType**–**[in]**[hipDataType] specifies the datatype of computation.



-
hipblasStatus_t hipblasAxpyEx(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const void *alpha, hipDataType alphaType, const void *x, hipDataType xType, int incx, void *y, hipDataType yType, int incy, hipDataType executionType)[#](#_CPPv413hipblasAxpyEx15hipblasHandle_tiPKv11hipDataTypePKv11hipDataTypeiPv11hipDataTypei11hipDataType) BLAS EX API.

axpyEx computes constant alpha multiplied by vector x, plus vector y

y := alpha * x + y - Supported types are determined by the backend. See rocBLAS/cuBLAS documentation.

- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] the number of elements in x and y.**alpha**–**[in]**device pointer or host pointer to specify the scalar alpha.**alphaType**–**[in]**[hipDataType] specifies the datatype of alpha.**x**–**[in]**device pointer storing vector x.**xType**–**[in]**[hipDataType] specifies the datatype of vector x.**incx**–**[in]**[int] specifies the increment for the elements of x.**y**–**[inout]**device pointer storing vector y.**yType**–**[in]**[hipDataType] specifies the datatype of vector y.**incy**–**[in]**[int] specifies the increment for the elements of y.**executionType**–**[in]**[hipDataType] specifies the datatype of computation.



The `axpyEx`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasAxpyBatchedEx(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const void *alpha, hipDataType alphaType, const void *x, hipDataType xType, int incx, void *y, hipDataType yType, int incy, int batchCount, hipDataType executionType)[#](#_CPPv420hipblasAxpyBatchedEx15hipblasHandle_tiPKv11hipDataTypePKv11hipDataTypeiPv11hipDataTypeii11hipDataType) BLAS EX API.

axpyBatchedEx computes constant alpha multiplied by vector x, plus vector y over a set of batched vectors.

y := alpha * x + y

Supported types are determined by the backend. See rocBLAS/cuBLAS documentation.


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] the number of elements in each x_i and y_i.**alpha**–**[in]**device pointer or host pointer to specify the scalar alpha.**alphaType**–**[in]**[hipDataType] specifies the datatype of alpha.**x**–**[in]**device array of device pointers storing each vector x_i.**xType**–**[in]**[hipDataType] specifies the datatype of each vector x_i.**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**y**–**[inout]**device array of device pointers storing each vector y_i.**yType**–**[in]**[hipDataType] specifies the datatype of each vector y_i.**incy**–**[in]**[int] specifies the increment for the elements of each y_i.**batchCount**–**[in]**[int] number of instances in the batch.**executionType**–**[in]**[hipDataType] specifies the datatype of computation.



The `axpyBatchedEx`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasAxpyStridedBatchedEx(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const void *alpha, hipDataType alphaType, const void *x, hipDataType xType, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, void *y, hipDataType yType, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount, hipDataType executionType)[#](#_CPPv427hipblasAxpyStridedBatchedEx15hipblasHandle_tiPKv11hipDataTypePKv11hipDataTypei13hipblasStridePv11hipDataTypei13hipblasStridei11hipDataType) BLAS EX API.

axpyStridedBatchedEx computes constant alpha multiplied by vector x, plus vector y over a set of strided batched vectors.

y := alpha * x + y

Supported types are determined by the backend. See rocBLAS/cuBLAS documentation.


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] the number of elements in each x_i and y_i.**alpha**–**[in]**device pointer or host pointer to specify the scalar alpha.**alphaType**–**[in]**[hipDataType] specifies the datatype of alpha.**x**–**[in]**device pointer to the first vector x_1.**xType**–**[in]**[hipDataType] specifies the datatype of each vector x_i.**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**stridex**–**[in]**[hipblasStride] stride from the start of one vector (x_i) to the next one (x_i+1). There are no restrictions placed on stridex, however the user should take care to ensure that stridex is of appropriate size, for a typical case this means stridex >= n * incx.**y**–**[inout]**device pointer to the first vector y_1.**yType**–**[in]**[hipDataType] specifies the datatype of each vector y_i.**incy**–**[in]**[int] specifies the increment for the elements of each y_i.**stridey**–**[in]**[hipblasStride] stride from the start of one vector (y_i) to the next one (y_i+1). There are no restrictions placed on stridey, however the user should take care to ensure that stridey is of appropriate size, for a typical case this means stridey >= n * incy.**batchCount**–**[in]**[int] number of instances in the batch.**executionType**–**[in]**[hipDataType] specifies the datatype of computation.



The `axpyStridedBatchedEx`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasDotEx(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const void *x, hipDataType xType, int incx, const void *y, hipDataType yType, int incy, void *result, hipDataType resultType, hipDataType executionType)[#](#_CPPv412hipblasDotEx15hipblasHandle_tiPKv11hipDataTypeiPKv11hipDataTypeiPv11hipDataType11hipDataType) BLAS EX API.

dotEx performs the dot product of vectors x and y

dotcEx performs the dot product of the conjugate of complex vector x and complex vector yresult = x * y;

result = conjugate (x) * y; - Supported types are determined by the backend. See rocBLAS/cuBLAS documentation.

- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] the number of elements in x and y.**x**–**[in]**device pointer storing vector x.**xType**–**[in]**[hipDataType] specifies the datatype of vector x.**incx**–**[in]**[int] specifies the increment for the elements of y.**y**–**[in]**device pointer storing vector y.**yType**–**[in]**[hipDataType] specifies the datatype of vector y.**incy**–**[in]**[int] specifies the increment for the elements of y.**result**–**[inout]**device pointer or host pointer to store the dot product. return is 0.0 if n <= 0.**resultType**–**[in]**[hipDataType] specifies the datatype of the result.**executionType**–**[in]**[hipDataType] specifies the datatype of computation.



The `dotEx`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasDotBatchedEx(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const void *x, hipDataType xType, int incx, const void *y, hipDataType yType, int incy, int batchCount, void *result, hipDataType resultType, hipDataType executionType)[#](#_CPPv419hipblasDotBatchedEx15hipblasHandle_tiPKv11hipDataTypeiPKv11hipDataTypeiiPv11hipDataType11hipDataType) BLAS EX API.

dotBatchedEx performs a batch of dot products of vectors x and y

dotcBatchedEx performs a batch of dot products of the conjugate of complex vector x and complex vector yresult_i = x_i * y_i;

where (x_i, y_i) is the i-th instance of the batch. x_i and y_i are vectors, for i = 1, …, batchCountresult_i = conjugate (x_i) * y_i;

- Supported types are determined by the backend. See rocBLAS/cuBLAS documentation.

- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] the number of elements in each x_i and y_i.**x**–**[in]**device array of device pointers storing each vector x_i.**xType**–**[in]**[hipDataType] specifies the datatype of each vector x_i.**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**y**–**[in]**device array of device pointers storing each vector y_i.**yType**–**[in]**[hipDataType] specifies the datatype of each vector y_i.**incy**–**[in]**[int] specifies the increment for the elements of each y_i.**batchCount**–**[in]**[int] number of instances in the batch**result**–**[inout]**device array or host array of batchCount size to store the dot products of each batch. return 0.0 for each element if n <= 0.**resultType**–**[in]**[hipDataType] specifies the datatype of the result.**executionType**–**[in]**[hipDataType] specifies the datatype of computation.



The `dotBatchedEx`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasDotStridedBatchedEx(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const void *x, hipDataType xType, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const void *y, hipDataType yType, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount, void *result, hipDataType resultType, hipDataType executionType)[#](#_CPPv426hipblasDotStridedBatchedEx15hipblasHandle_tiPKv11hipDataTypei13hipblasStridePKv11hipDataTypei13hipblasStrideiPv11hipDataType11hipDataType) BLAS EX API.

dotStridedBatchedEx performs a batch of dot products of vectors x and y

dotc_strided_batched_ex performs a batch of dot products of the conjugate of complex vector x and complex vector yresult_i = x_i * y_i;

where (x_i, y_i) is the i-th instance of the batch. x_i and y_i are vectors, for i = 1, …, batchCountresult_i = conjugate (x_i) * y_i;

- Supported types are determined by the backend. See rocBLAS/cuBLAS documentation.

- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] the number of elements in each x_i and y_i.**x**–**[in]**device pointer to the first vector (x_1) in the batch.**xType**–**[in]**[hipDataType] specifies the datatype of each vector x_i.**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**stridex**–**[in]**[hipblasStride] stride from the start of one vector (x_i) and the next one (x_i+1)**y**–**[in]**device pointer to the first vector (y_1) in the batch.**yType**–**[in]**[hipDataType] specifies the datatype of each vector y_i.**incy**–**[in]**[int] specifies the increment for the elements of each y_i.**stridey**–**[in]**[hipblasStride] stride from the start of one vector (y_i) and the next one (y_i+1)**batchCount**–**[in]**[int] number of instances in the batch**result**–**[inout]**device array or host array of batchCount size to store the dot products of each batch. return 0.0 for each element if n <= 0.**resultType**–**[in]**[hipDataType] specifies the datatype of the result.**executionType**–**[in]**[hipDataType] specifies the datatype of computation.



The `dotStridedBatchedEx`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasDotcEx(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const void *x, hipDataType xType, int incx, const void *y, hipDataType yType, int incy, void *result, hipDataType resultType, hipDataType executionType)[#](#_CPPv413hipblasDotcEx15hipblasHandle_tiPKv11hipDataTypeiPKv11hipDataTypeiPv11hipDataType11hipDataType) BLAS EX API.

dotEx performs the dot product of vectors x and y

dotcEx performs the dot product of the conjugate of complex vector x and complex vector yresult = x * y;

result = conjugate (x) * y; - Supported types are determined by the backend. See rocBLAS/cuBLAS documentation.

- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] the number of elements in x and y.**x**–**[in]**device pointer storing vector x.**xType**–**[in]**[hipDataType] specifies the datatype of vector x.**incx**–**[in]**[int] specifies the increment for the elements of y.**y**–**[in]**device pointer storing vector y.**yType**–**[in]**[hipDataType] specifies the datatype of vector y.**incy**–**[in]**[int] specifies the increment for the elements of y.**result**–**[inout]**device pointer or host pointer to store the dot product. return is 0.0 if n <= 0.**resultType**–**[in]**[hipDataType] specifies the datatype of the result.**executionType**–**[in]**[hipDataType] specifies the datatype of computation.



The `dotcEx`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasDotcBatchedEx(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const void *x, hipDataType xType, int incx, const void *y, hipDataType yType, int incy, int batchCount, void *result, hipDataType resultType, hipDataType executionType)[#](#_CPPv420hipblasDotcBatchedEx15hipblasHandle_tiPKv11hipDataTypeiPKv11hipDataTypeiiPv11hipDataType11hipDataType) BLAS EX API.

dotBatchedEx performs a batch of dot products of vectors x and y

dotcBatchedEx performs a batch of dot products of the conjugate of complex vector x and complex vector yresult_i = x_i * y_i;

where (x_i, y_i) is the i-th instance of the batch. x_i and y_i are vectors, for i = 1, …, batchCountresult_i = conjugate (x_i) * y_i;

- Supported types are determined by the backend. See rocBLAS/cuBLAS documentation.

- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] the number of elements in each x_i and y_i.**x**–**[in]**device array of device pointers storing each vector x_i.**xType**–**[in]**[hipDataType] specifies the datatype of each vector x_i.**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**y**–**[in]**device array of device pointers storing each vector y_i.**yType**–**[in]**[hipDataType] specifies the datatype of each vector y_i.**incy**–**[in]**[int] specifies the increment for the elements of each y_i.**batchCount**–**[in]**[int] number of instances in the batch**result**–**[inout]**device array or host array of batchCount size to store the dot products of each batch. return 0.0 for each element if n <= 0.**resultType**–**[in]**[hipDataType] specifies the datatype of the result.**executionType**–**[in]**[hipDataType] specifies the datatype of computation.



The `dotcBatchedEx`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasDotcStridedBatchedEx(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const void *x, hipDataType xType, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, const void *y, hipDataType yType, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, int batchCount, void *result, hipDataType resultType, hipDataType executionType)[#](#_CPPv427hipblasDotcStridedBatchedEx15hipblasHandle_tiPKv11hipDataTypei13hipblasStridePKv11hipDataTypei13hipblasStrideiPv11hipDataType11hipDataType) BLAS EX API.

dotStridedBatchedEx performs a batch of dot products of vectors x and y

dotc_strided_batched_ex performs a batch of dot products of the conjugate of complex vector x and complex vector yresult_i = x_i * y_i;

where (x_i, y_i) is the i-th instance of the batch. x_i and y_i are vectors, for i = 1, …, batchCountresult_i = conjugate (x_i) * y_i;

- Supported types are determined by the backend. See rocBLAS/cuBLAS documentation.

- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] the number of elements in each x_i and y_i.**x**–**[in]**device pointer to the first vector (x_1) in the batch.**xType**–**[in]**[hipDataType] specifies the datatype of each vector x_i.**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**stridex**–**[in]**[hipblasStride] stride from the start of one vector (x_i) and the next one (x_i+1)**y**–**[in]**device pointer to the first vector (y_1) in the batch.**yType**–**[in]**[hipDataType] specifies the datatype of each vector y_i.**incy**–**[in]**[int] specifies the increment for the elements of each y_i.**stridey**–**[in]**[hipblasStride] stride from the start of one vector (y_i) and the next one (y_i+1)**batchCount**–**[in]**[int] number of instances in the batch**result**–**[inout]**device array or host array of batchCount size to store the dot products of each batch. return 0.0 for each element if n <= 0.**resultType**–**[in]**[hipDataType] specifies the datatype of the result.**executionType**–**[in]**[hipDataType] specifies the datatype of computation.



The `dotcStridedBatchedEx`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasNrm2Ex(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const void *x, hipDataType xType, int incx, void *result, hipDataType resultType, hipDataType executionType)[#](#_CPPv413hipblasNrm2Ex15hipblasHandle_tiPKv11hipDataTypeiPv11hipDataType11hipDataType) BLAS_EX API.

nrm2Ex computes the euclidean norm of a real or complex vector

result := sqrt( x'*x ) for real vectors result := sqrt( x**H*x ) for complex vectors

Supported types are determined by the backend. See rocBLAS/cuBLAS documentation.


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] the number of elements in x.**x**–**[in]**device pointer storing vector x.**xType**–**[in]**[hipDataType] specifies the datatype of the vector x.**incx**–**[in]**[int] specifies the increment for the elements of y.**result**–**[inout]**device pointer or host pointer to store the nrm2 product. return is 0.0 if n, incx<=0.**resultType**–**[in]**[hipDataType] specifies the datatype of the result.**executionType**–**[in]**[hipDataType] specifies the datatype of computation.



The `nrm2Ex`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasNrm2BatchedEx(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const void *x, hipDataType xType, int incx, int batchCount, void *result, hipDataType resultType, hipDataType executionType)[#](#_CPPv420hipblasNrm2BatchedEx15hipblasHandle_tiPKv11hipDataTypeiiPv11hipDataType11hipDataType) BLAS_EX API.

nrm2BatchedEx computes the euclidean norm over a batch of real or complex vectors

result := sqrt( x_i'*x_i ) for real vectors x, for i = 1, ..., batchCount result := sqrt( x_i**H*x_i ) for complex vectors x, for i = 1, ..., batchCount

Supported types are determined by the backend. See rocBLAS/cuBLAS documentation.


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] number of elements in each x_i.**x**–**[in]**device array of device pointers storing each vector x_i.**xType**–**[in]**[hipDataType] specifies the datatype of each vector x_i.**incx**–**[in]**[int] specifies the increment for the elements of each x_i. incx must be > 0.**batchCount**–**[in]**[int] number of instances in the batch**result**–**[out]**device pointer or host pointer to array of batchCount size for nrm2 results. return is 0.0 for each element if n <= 0, incx<=0.**resultType**–**[in]**[hipDataType] specifies the datatype of the result.**executionType**–**[in]**[hipDataType] specifies the datatype of computation.



The `nrm2BatchedEx`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasNrm2StridedBatchedEx(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const void *x, hipDataType xType, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount, void *result, hipDataType resultType, hipDataType executionType)[#](#_CPPv427hipblasNrm2StridedBatchedEx15hipblasHandle_tiPKv11hipDataTypei13hipblasStrideiPv11hipDataType11hipDataType) BLAS_EX API.

nrm2StridedBatchedEx computes the euclidean norm over a batch of real or complex vectors

:= sqrt( x_i'*x_i ) for real vectors x, for i = 1, ..., batchCount := sqrt( x_i**H*x_i ) for complex vectors, for i = 1, ..., batchCount

Supported types are determined by the backend. See rocBLAS/cuBLAS documentation.


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] number of elements in each x_i.**x**–**[in]**device pointer to the first vector x_1.**xType**–**[in]**[hipDataType] specifies the datatype of each vector x_i.**incx**–**[in]**[int] specifies the increment for the elements of each x_i. incx must be > 0.**stridex**–**[in]**[hipblasStride] stride from the start of one vector (x_i) and the next one (x_i+1). There are no restrictions placed on stride_x, however the user should take care to ensure that stride_x is of appropriate size, for a typical case this means stride_x >= n * incx.**batchCount**–**[in]**[int] number of instances in the batch**result**–**[out]**device pointer or host pointer to array for storing contiguous batchCount results. return is 0.0 for each element if n <= 0, incx<=0.**resultType**–**[in]**[hipDataType] specifies the datatype of the result.**executionType**–**[in]**[hipDataType] specifies the datatype of computation.



The `nrm2StridedBatchedEx`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasRotEx(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, void *x, hipDataType xType, int incx, void *y, hipDataType yType, int incy, const void *c, const void *s, hipDataType csType, hipDataType executionType)[#](#_CPPv412hipblasRotEx15hipblasHandle_tiPv11hipDataTypeiPv11hipDataTypeiPKvPKv11hipDataType11hipDataType) BLAS EX API.

rotEx applies the Givens rotation matrix defined by c=cos(alpha) and s=sin(alpha) to vectors x and y. Scalars c and s may be stored in either host or device memory, location is specified by calling hipblasSetPointerMode.

In the case where cs_type is real: x := c * x + s * y y := c * y - s * x

In the case where cs_type is complex, the imaginary part of c is ignored: x := real(c) * x + s * y y := real(c) * y - conj(s) * x

Supported types are determined by the backend. See rocBLAS/cuBLAS documentation.


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] number of elements in the x and y vectors.**x**–**[inout]**device pointer storing vector x.**xType**–**[in]**[hipDataType] specifies the datatype of vector x.**incx**–**[in]**[int] specifies the increment between elements of x.**y**–**[inout]**device pointer storing vector y.**yType**–**[in]**[hipDataType] specifies the datatype of vector y.**incy**–**[in]**[int] specifies the increment between elements of y.**c**–**[in]**device pointer or host pointer storing scalar cosine component of the rotation matrix.**s**–**[in]**device pointer or host pointer storing scalar sine component of the rotation matrix.**csType**–**[in]**[hipDataType] specifies the datatype of c and s.**executionType**–**[in]**[hipDataType] specifies the datatype of computation.



The `rotEx`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasRotBatchedEx(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, void *x, hipDataType xType, int incx, void *y, hipDataType yType, int incy, const void *c, const void *s, hipDataType csType, int batchCount, hipDataType executionType)[#](#_CPPv419hipblasRotBatchedEx15hipblasHandle_tiPv11hipDataTypeiPv11hipDataTypeiPKvPKv11hipDataTypei11hipDataType) BLAS EX API.

rotBatchedEx applies the Givens rotation matrix defined by c=cos(alpha) and s=sin(alpha) to batched vectors x_i and y_i, for i = 1, …, batchCount. Scalars c and s may be stored in either host or device memory, location is specified by calling hipblasSetPointerMode.

In the case where cs_type is real: x := c * x + s * y y := c * y - s * x

In the case where cs_type is complex, the imaginary part of c is ignored: x := real(c) * x + s * y y := real(c) * y - conj(s) * x

Supported types are determined by the backend. See rocBLAS/cuBLAS documentation.


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] number of elements in each x_i and y_i vectors.**x**–**[inout]**device array of device pointers storing each vector x_i.**xType**–**[in]**[hipDataType] specifies the datatype of each vector x_i.**incx**–**[in]**[int] specifies the increment between elements of each x_i.**y**–**[inout]**device array of device pointers storing each vector y_i.**yType**–**[in]**[hipDataType] specifies the datatype of each vector y_i.**incy**–**[in]**[int] specifies the increment between elements of each y_i.**c**–**[in]**device pointer or host pointer to scalar cosine component of the rotation matrix.**s**–**[in]**device pointer or host pointer to scalar sine component of the rotation matrix.**csType**–**[in]**[hipDataType] specifies the datatype of c and s.**batchCount**–**[in]**[int] the number of x and y arrays, i.e. the number of batches.**executionType**–**[in]**[hipDataType] specifies the datatype of computation.



The `rotBatchedEx`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasRotStridedBatchedEx(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, void *x, hipDataType xType, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, void *y, hipDataType yType, int incy,[hipblasStride](#_CPPv413hipblasStride)stridey, const void *c, const void *s, hipDataType csType, int batchCount, hipDataType executionType)[#](#_CPPv426hipblasRotStridedBatchedEx15hipblasHandle_tiPv11hipDataTypei13hipblasStridePv11hipDataTypei13hipblasStridePKvPKv11hipDataTypei11hipDataType) BLAS Level 1 API.

rotStridedBatchedEx applies the Givens rotation matrix defined by c=cos(alpha) and s=sin(alpha) to strided batched vectors x_i and y_i, for i = 1, …, batchCount. Scalars c and s may be stored in either host or device memory, location is specified by calling hipblasSetPointerMode.

In the case where cs_type is real: x := c * x + s * y y := c * y - s * x

In the case where cs_type is complex, the imaginary part of c is ignored: x := real(c) * x + s * y y := real(c) * y - conj(s) * x

Supported types are determined by the backend. See rocBLAS/cuBLAS documentation.


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] number of elements in each x_i and y_i vectors.**x**–**[inout]**device pointer to the first vector x_1.**xType**–**[in]**[hipDataType] specifies the datatype of each vector x_i.**incx**–**[in]**[int] specifies the increment between elements of each x_i.**stridex**–**[in]**[hipblasStride] specifies the increment from the beginning of x_i to the beginning of x_(i+1)**y**–**[inout]**device pointer to the first vector y_1.**yType**–**[in]**[hipDataType] specifies the datatype of each vector y_i.**incy**–**[in]**[int] specifies the increment between elements of each y_i.**stridey**–**[in]**[hipblasStride] specifies the increment from the beginning of y_i to the beginning of y_(i+1)**c**–**[in]**device pointer or host pointer to scalar cosine component of the rotation matrix.**s**–**[in]**device pointer or host pointer to scalar sine component of the rotation matrix.**csType**–**[in]**[hipDataType] specifies the datatype of c and s.**batchCount**–**[in]**[int] the number of x and y arrays, i.e. the number of batches.**executionType**–**[in]**[hipDataType] specifies the datatype of computation.



The `rotStridedBatchedEx`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasScalEx(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const void *alpha, hipDataType alphaType, void *x, hipDataType xType, int incx, hipDataType executionType)[#](#_CPPv413hipblasScalEx15hipblasHandle_tiPKv11hipDataTypePv11hipDataTypei11hipDataType) BLAS EX API.

scalEx scales each element of vector x with scalar alpha.

x := alpha * x

Supported types are determined by the backend. See rocBLAS/cuBLAS documentation.


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] the number of elements in x.**alpha**–**[in]**device pointer or host pointer for the scalar alpha.**alphaType**–**[in]**[hipDataType] specifies the datatype of alpha.**x**–**[inout]**device pointer storing vector x.**xType**–**[in]**[hipDataType] specifies the datatype of vector x.**incx**–**[in]**[int] specifies the increment for the elements of x.**executionType**–**[in]**[hipDataType] specifies the datatype of computation.



The `scalEx`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasScalBatchedEx(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const void *alpha, hipDataType alphaType, void *x, hipDataType xType, int incx, int batchCount, hipDataType executionType)[#](#_CPPv420hipblasScalBatchedEx15hipblasHandle_tiPKv11hipDataTypePv11hipDataTypeii11hipDataType) BLAS EX API.

scalBatchedEx scales each element of each vector x_i with scalar alpha.

x_i := alpha * x_i

Supported types are determined by the backend. See rocBLAS/cuBLAS documentation.


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] the number of elements in x.**alpha**–**[in]**device pointer or host pointer for the scalar alpha.**alphaType**–**[in]**[hipDataType] specifies the datatype of alpha.**x**–**[inout]**device array of device pointers storing each vector x_i.**xType**–**[in]**[hipDataType] specifies the datatype of each vector x_i.**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**batchCount**–**[in]**[int] number of instances in the batch.**executionType**–**[in]**[hipDataType] specifies the datatype of computation.



The `scalBatchedEx`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

-
hipblasStatus_t hipblasScalStridedBatchedEx(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, int n, const void *alpha, hipDataType alphaType, void *x, hipDataType xType, int incx,[hipblasStride](#_CPPv413hipblasStride)stridex, int batchCount, hipDataType executionType)[#](#_CPPv427hipblasScalStridedBatchedEx15hipblasHandle_tiPKv11hipDataTypePv11hipDataTypei13hipblasStridei11hipDataType) BLAS EX API.

scalStridedBatchedEx scales each element of vector x with scalar alpha over a set of strided batched vectors.

x := alpha * x

Supported types are determined by the backend. See rocBLAS/cuBLAS documentation.


- Parameters:
**handle**–**[in]**[hipblasHandle_t] handle to the hipblas library context queue.**n**–**[in]**[int] the number of elements in x.**alpha**–**[in]**device pointer or host pointer for the scalar alpha.**alphaType**–**[in]**[hipDataType] specifies the datatype of alpha.**x**–**[inout]**device pointer to the first vector x_1.**xType**–**[in]**[hipDataType] specifies the datatype of each vector x_i.**incx**–**[in]**[int] specifies the increment for the elements of each x_i.**stridex**–**[in]**[hipblasStride] stride from the start of one vector (x_i) to the next one (x_i+1). There are no restrictions placed on stridex, however the user should take care to ensure that stridex is of appropriate size, for a typical case this means stridex >= n * incx.**batchCount**–**[in]**[int] number of instances in the batch.**executionType**–**[in]**[hipDataType] specifies the datatype of computation.



The `scalStridedBatchedEx`

function supports the 64-bit integer interface. See the [ILP64 interfaces](#ilp64-api) section.

## SOLVER API[#](#solver-api)

-
hipblasStatus_t hipblasSgetrf(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const int n, float *A, const int lda, int *ipiv, int *info)[#](#_CPPv413hipblasSgetrf15hipblasHandle_tKiPfKiPiPi)

-
hipblasStatus_t hipblasDgetrf(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const int n, double *A, const int lda, int *ipiv, int *info)[#](#_CPPv413hipblasDgetrf15hipblasHandle_tKiPdKiPiPi)

-
hipblasStatus_t hipblasCgetrf(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const int n, hipComplex *A, const int lda, int *ipiv, int *info)[#](#_CPPv413hipblasCgetrf15hipblasHandle_tKiP10hipComplexKiPiPi)

-
hipblasStatus_t hipblasZgetrf(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const int n, hipDoubleComplex *A, const int lda, int *ipiv, int *info)[#](#_CPPv413hipblasZgetrf15hipblasHandle_tKiP16hipDoubleComplexKiPiPi) SOLVER API.

getrf computes the LU factorization of a general n-by-n matrix A using partial pivoting with row interchanges. The LU factorization can be done without pivoting if ipiv is passed as a nullptr.

In the case that ipiv is not null, the factorization has the form:

\[ A = PLU \]where P is a permutation matrix, L is lower triangular with unit diagonal elements, and U is upper triangular.

In the case that ipiv is null, the factorization is done without pivoting:

\[ A = LU \]Supported precisions in rocSOLVER : s,d,c,z

Supported precisions in cuBLAS : s,d,c,z


- Parameters:
**handle**–**[in]**hipblasHandle_t.**n**–**[in]**int. n >= 0.

The number of columns and rows of the matrix A.

**A**–**[inout]**pointer to type. Array on the GPU of dimension lda*n.

On entry, the n-by-n matrix A to be factored. On exit, the factors L and U from the factorization. The unit diagonal elements of L are not stored.

**lda**–**[in]**int. lda >= n.

Specifies the leading dimension of A.

**ipiv**–**[out]**pointer to int. Array on the GPU of dimension n.

The vector of pivot indices. Elements of ipiv are 1-based indices. For 1 <= i <= n, the row i of the matrix was interchanged with row ipiv[i]. Matrix P of the factorization can be derived from ipiv. The factorization here can be done without pivoting if ipiv is passed in as a nullptr.

**info**–**[out]**pointer to a int on the GPU.

If info = 0, successful exit. If info = j > 0, U is singular. U[j,j] is the first zero pivot.




-
hipblasStatus_t hipblasSgetrfBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const int n, float *const A[], const int lda, int *ipiv, int *info, const int batchCount)[#](#_CPPv420hipblasSgetrfBatched15hipblasHandle_tKiA_PCfKiPiPiKi)

-
hipblasStatus_t hipblasDgetrfBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const int n, double *const A[], const int lda, int *ipiv, int *info, const int batchCount)[#](#_CPPv420hipblasDgetrfBatched15hipblasHandle_tKiA_PCdKiPiPiKi)

-
hipblasStatus_t hipblasCgetrfBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const int n, hipComplex *const A[], const int lda, int *ipiv, int *info, const int batchCount)[#](#_CPPv420hipblasCgetrfBatched15hipblasHandle_tKiA_PC10hipComplexKiPiPiKi)

-
hipblasStatus_t hipblasZgetrfBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const int n, hipDoubleComplex *const A[], const int lda, int *ipiv, int *info, const int batchCount)[#](#_CPPv420hipblasZgetrfBatched15hipblasHandle_tKiA_PC16hipDoubleComplexKiPiPiKi) SOLVER API.

getrfBatched computes the LU factorization of a batch of general n-by-n matrices using partial pivoting with row interchanges. The LU factorization can be done without pivoting if ipiv is passed as a nullptr.

In the case that ipiv is not null, the factorization of matrix \(A_i\) in the batch has the form:

\[ A_i = P_iL_iU_i \]where \(P_i\) is a permutation matrix, \(L_i\) is lower triangular with unit diagonal elements, and \(U_i\) is upper triangular.

In the case that ipiv is null, the factorization is done without pivoting:

\[ A_i = L_iU_i \]Supported precisions in rocSOLVER : s,d,c,z

Supported precisions in cuBLAS : s,d,c,z


- Parameters:
**handle**–**[in]**hipblasHandle_t.**n**–**[in]**int. n >= 0.

The number of columns and rows of all matrices A_i in the batch.

**A**–**[inout]**array of pointers to type. Each pointer points to an array on the GPU of dimension lda*n.

On entry, the n-by-n matrices A_i to be factored. On exit, the factors L_i and U_i from the factorizations. The unit diagonal elements of L_i are not stored.

**lda**–**[in]**int. lda >= n.

Specifies the leading dimension of matrices A_i.

**ipiv**–**[out]**pointer to int. Array on the GPU.

Contains the vectors of pivot indices ipiv_i (corresponding to A_i). Dimension of ipiv_i is n. Elements of ipiv_i are 1-based indices. For each instance A_i in the batch and for 1 <= j <= n, the row j of the matrix A_i was interchanged with row ipiv_i[j]. Matrix P_i of the factorization can be derived from ipiv_i. The factorization here can be done without pivoting if ipiv is passed in as a nullptr.

**info**–**[out]**pointer to int. Array of batchCount integers on the GPU.

If info[i] = 0, successful exit for factorization of A_i. If info[i] = j > 0, U_i is singular. U_i[j,j] is the first zero pivot.

**batchCount**–**[in]**int. batchCount >= 0.

Number of matrices in the batch.




-
hipblasStatus_t hipblasSgetrfStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const int n, float *A, const int lda, const[hipblasStride](#_CPPv413hipblasStride)strideA, int *ipiv, const[hipblasStride](#_CPPv413hipblasStride)strideP, int *info, const int batchCount)[#](#_CPPv427hipblasSgetrfStridedBatched15hipblasHandle_tKiPfKiK13hipblasStridePiK13hipblasStridePiKi)

-
hipblasStatus_t hipblasDgetrfStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const int n, double *A, const int lda, const[hipblasStride](#_CPPv413hipblasStride)strideA, int *ipiv, const[hipblasStride](#_CPPv413hipblasStride)strideP, int *info, const int batchCount)[#](#_CPPv427hipblasDgetrfStridedBatched15hipblasHandle_tKiPdKiK13hipblasStridePiK13hipblasStridePiKi)

-
hipblasStatus_t hipblasCgetrfStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const int n, hipComplex *A, const int lda, const[hipblasStride](#_CPPv413hipblasStride)strideA, int *ipiv, const[hipblasStride](#_CPPv413hipblasStride)strideP, int *info, const int batchCount)[#](#_CPPv427hipblasCgetrfStridedBatched15hipblasHandle_tKiP10hipComplexKiK13hipblasStridePiK13hipblasStridePiKi)

-
hipblasStatus_t hipblasZgetrfStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const int n, hipDoubleComplex *A, const int lda, const[hipblasStride](#_CPPv413hipblasStride)strideA, int *ipiv, const[hipblasStride](#_CPPv413hipblasStride)strideP, int *info, const int batchCount)[#](#_CPPv427hipblasZgetrfStridedBatched15hipblasHandle_tKiP16hipDoubleComplexKiK13hipblasStridePiK13hipblasStridePiKi) SOLVER API.

getrfStridedBatched computes the LU factorization of a batch of general n-by-n matrices using partial pivoting with row interchanges. The LU factorization can be done without pivoting if ipiv is passed as a nullptr.

In the case that ipiv is not null, the factorization of matrix \(A_i\) in the batch has the form:

\[ A_i = P_iL_iU_i \]where \(P_i\) is a permutation matrix, \(L_i\) is lower triangular with unit diagonal elements, and \(U_i\) is upper triangular.

In the case that ipiv is null, the factorization is done without pivoting:

\[ A_i = L_iU_i \]Supported precisions in rocSOLVER : s,d,c,z

Supported precisions in cuBLAS : s,d,c,z


- Parameters:
**handle**–**[in]**hipblasHandle_t.**n**–**[in]**int. n >= 0.

The number of columns and rows of all matrices A_i in the batch.

**A**–**[inout]**pointer to type. Array on the GPU (the size depends on the value of strideA).

On entry, the n-by-n matrices A_i to be factored. On exit, the factors L_i and U_i from the factorization. The unit diagonal elements of L_i are not stored.

**lda**–**[in]**int. lda >= n.

Specifies the leading dimension of matrices A_i.

**strideA**–**[in]**hipblasStride.

Stride from the start of one matrix A_i to the next one A_(i+1). There is no restriction for the value of strideA. Normal use case is strideA >= lda*n

**ipiv**–**[out]**pointer to int. Array on the GPU (the size depends on the value of strideP).

Contains the vectors of pivots indices ipiv_i (corresponding to A_i). Dimension of ipiv_i is n. Elements of ipiv_i are 1-based indices. For each instance A_i in the batch and for 1 <= j <= n, the row j of the matrix A_i was interchanged with row ipiv_i[j]. Matrix P_i of the factorization can be derived from ipiv_i. The factorization here can be done without pivoting if ipiv is passed in as a nullptr.

**strideP**–**[in]**hipblasStride.

Stride from the start of one vector ipiv_i to the next one ipiv_(i+1). There is no restriction for the value of strideP. Normal use case is strideP >= n.

**info**–**[out]**pointer to int. Array of batchCount integers on the GPU.

If info[i] = 0, successful exit for factorization of A_i. If info[i] = j > 0, U_i is singular. U_i[j,j] is the first zero pivot.

**batchCount**–**[in]**int. batchCount >= 0.

Number of matrices in the batch.




-
hipblasStatus_t hipblasSgetrs(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, const int n, const int nrhs, float *A, const int lda, const int *ipiv, float *B, const int ldb, int *info)[#](#_CPPv413hipblasSgetrs15hipblasHandle_tK18hipblasOperation_tKiKiPfKiPKiPfKiPi)

-
hipblasStatus_t hipblasDgetrs(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, const int n, const int nrhs, double *A, const int lda, const int *ipiv, double *B, const int ldb, int *info)[#](#_CPPv413hipblasDgetrs15hipblasHandle_tK18hipblasOperation_tKiKiPdKiPKiPdKiPi)

-
hipblasStatus_t hipblasCgetrs(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, const int n, const int nrhs, hipComplex *A, const int lda, const int *ipiv, hipComplex *B, const int ldb, int *info)[#](#_CPPv413hipblasCgetrs15hipblasHandle_tK18hipblasOperation_tKiKiP10hipComplexKiPKiP10hipComplexKiPi)

-
hipblasStatus_t hipblasZgetrs(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, const int n, const int nrhs, hipDoubleComplex *A, const int lda, const int *ipiv, hipDoubleComplex *B, const int ldb, int *info)[#](#_CPPv413hipblasZgetrs15hipblasHandle_tK18hipblasOperation_tKiKiP16hipDoubleComplexKiPKiP16hipDoubleComplexKiPi) SOLVER API.

getrs solves a system of n linear equations on n variables in its factorized form.

It solves one of the following systems, depending on the value of trans:

\[\begin{split} \begin{array}{cl} A X = B & \: \text{not transposed,}\\ A^T X = B & \: \text{transposed, or}\\ A^H X = B & \: \text{conjugate transposed.} \end{array} \end{split}\]Matrix A is defined by its triangular factors as returned by

[getrf](#hipblas_8h_1a8b9ff19905576bd48391f8eaaa2781da).Supported precisions in rocSOLVER : s,d,c,z

Supported precisions in cuBLAS : s,d,c,z


- Parameters:
**handle**–**[in]**hipblasHandle_t.**trans**–**[in]**hipblasOperation_t.

Specifies the form of the system of equations.

**n**–**[in]**int. n >= 0.

The order of the system, i.e. the number of columns and rows of A.

**nrhs**–**[in]**int. nrhs >= 0.

The number of right hand sides, i.e., the number of columns of the matrix B.

**A**–**[in]**pointer to type. Array on the GPU of dimension lda*n.

The factors L and U of the factorization A = P*L*U returned by

[getrf](#hipblas_8h_1a8b9ff19905576bd48391f8eaaa2781da).**lda**–**[in]**int. lda >= n.

The leading dimension of A.

**ipiv**–**[in]**pointer to int. Array on the GPU of dimension n.

The pivot indices returned by

[getrf](#hipblas_8h_1a8b9ff19905576bd48391f8eaaa2781da).**B**–**[inout]**pointer to type. Array on the GPU of dimension ldb*nrhs.

On entry, the right hand side matrix B. On exit, the solution matrix X.

**ldb**–**[in]**int. ldb >= n.

The leading dimension of B.

**info**–**[out]**pointer to a int on the host.

If info = 0, successful exit. If info = j < 0, the argument at position -j is invalid.




-
hipblasStatus_t hipblasSgetrsBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, const int n, const int nrhs, float *const A[], const int lda, const int *ipiv, float *const B[], const int ldb, int *info, const int batchCount)[#](#_CPPv420hipblasSgetrsBatched15hipblasHandle_tK18hipblasOperation_tKiKiA_PCfKiPKiA_PCfKiPiKi)

-
hipblasStatus_t hipblasDgetrsBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, const int n, const int nrhs, double *const A[], const int lda, const int *ipiv, double *const B[], const int ldb, int *info, const int batchCount)[#](#_CPPv420hipblasDgetrsBatched15hipblasHandle_tK18hipblasOperation_tKiKiA_PCdKiPKiA_PCdKiPiKi)

-
hipblasStatus_t hipblasCgetrsBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, const int n, const int nrhs, hipComplex *const A[], const int lda, const int *ipiv, hipComplex *const B[], const int ldb, int *info, const int batchCount)[#](#_CPPv420hipblasCgetrsBatched15hipblasHandle_tK18hipblasOperation_tKiKiA_PC10hipComplexKiPKiA_PC10hipComplexKiPiKi)

-
hipblasStatus_t hipblasZgetrsBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, const int n, const int nrhs, hipDoubleComplex *const A[], const int lda, const int *ipiv, hipDoubleComplex *const B[], const int ldb, int *info, const int batchCount)[#](#_CPPv420hipblasZgetrsBatched15hipblasHandle_tK18hipblasOperation_tKiKiA_PC16hipDoubleComplexKiPKiA_PC16hipDoubleComplexKiPiKi) SOLVER API.

getrsBatched solves a batch of systems of n linear equations on n variables in its factorized forms.

For each instance i in the batch, it solves one of the following systems, depending on the value of trans:

\[\begin{split} \begin{array}{cl} A_i X_i = B_i & \: \text{not transposed,}\\ A_i^T X_i = B_i & \: \text{transposed, or}\\ A_i^H X_i = B_i & \: \text{conjugate transposed.} \end{array} \end{split}\]Matrix \(A_i\) is defined by its triangular factors as returned by

[getrfBatched](#hipblas_8h_1a721bba1f328f6300b18e96cd1749d8a9).Supported precisions in rocSOLVER : s,d,c,z

Supported precisions in cuBLAS : s,d,c,z


- Parameters:
**handle**–**[in]**hipblasHandle_t.**trans**–**[in]**hipblasOperation_t.

Specifies the form of the system of equations of each instance in the batch.

**n**–**[in]**int. n >= 0.

The order of the system, i.e. the number of columns and rows of all A_i matrices.

**nrhs**–**[in]**int. nrhs >= 0.

The number of right hand sides, i.e., the number of columns of all the matrices B_i.

**A**–**[in]**Array of pointers to type. Each pointer points to an array on the GPU of dimension lda*n.

The factors L_i and U_i of the factorization A_i = P_i*L_i*U_i returned by

[getrfBatched](#hipblas_8h_1a721bba1f328f6300b18e96cd1749d8a9).**lda**–**[in]**int. lda >= n.

The leading dimension of matrices A_i.

**ipiv**–**[in]**pointer to int. Array on the GPU.

Contains the vectors ipiv_i of pivot indices returned by

[getrfBatched](#hipblas_8h_1a721bba1f328f6300b18e96cd1749d8a9).**B**–**[inout]**Array of pointers to type. Each pointer points to an array on the GPU of dimension ldb*nrhs.

On entry, the right hand side matrices B_i. On exit, the solution matrix X_i of each system in the batch.

**ldb**–**[in]**int. ldb >= n.

The leading dimension of matrices B_i.

**info**–**[out]**pointer to a int on the host.

If info = 0, successful exit. If info = j < 0, the argument at position -j is invalid.

**batchCount**–**[in]**int. batchCount >= 0.

Number of instances (systems) in the batch.




-
hipblasStatus_t hipblasSgetrsStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, const int n, const int nrhs, float *A, const int lda, const[hipblasStride](#_CPPv413hipblasStride)strideA, const int *ipiv, const[hipblasStride](#_CPPv413hipblasStride)strideP, float *B, const int ldb, const[hipblasStride](#_CPPv413hipblasStride)strideB, int *info, const int batchCount)[#](#_CPPv427hipblasSgetrsStridedBatched15hipblasHandle_tK18hipblasOperation_tKiKiPfKiK13hipblasStridePKiK13hipblasStridePfKiK13hipblasStridePiKi)

-
hipblasStatus_t hipblasDgetrsStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, const int n, const int nrhs, double *A, const int lda, const[hipblasStride](#_CPPv413hipblasStride)strideA, const int *ipiv, const[hipblasStride](#_CPPv413hipblasStride)strideP, double *B, const int ldb, const[hipblasStride](#_CPPv413hipblasStride)strideB, int *info, const int batchCount)[#](#_CPPv427hipblasDgetrsStridedBatched15hipblasHandle_tK18hipblasOperation_tKiKiPdKiK13hipblasStridePKiK13hipblasStridePdKiK13hipblasStridePiKi)

-
hipblasStatus_t hipblasCgetrsStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, const int n, const int nrhs, hipComplex *A, const int lda, const[hipblasStride](#_CPPv413hipblasStride)strideA, const int *ipiv, const[hipblasStride](#_CPPv413hipblasStride)strideP, hipComplex *B, const int ldb, const[hipblasStride](#_CPPv413hipblasStride)strideB, int *info, const int batchCount)[#](#_CPPv427hipblasCgetrsStridedBatched15hipblasHandle_tK18hipblasOperation_tKiKiP10hipComplexKiK13hipblasStridePKiK13hipblasStrideP10hipComplexKiK13hipblasStridePiKi)

-
hipblasStatus_t hipblasZgetrsStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, const int n, const int nrhs, hipDoubleComplex *A, const int lda, const[hipblasStride](#_CPPv413hipblasStride)strideA, const int *ipiv, const[hipblasStride](#_CPPv413hipblasStride)strideP, hipDoubleComplex *B, const int ldb, const[hipblasStride](#_CPPv413hipblasStride)strideB, int *info, const int batchCount)[#](#_CPPv427hipblasZgetrsStridedBatched15hipblasHandle_tK18hipblasOperation_tKiKiP16hipDoubleComplexKiK13hipblasStridePKiK13hipblasStrideP16hipDoubleComplexKiK13hipblasStridePiKi) SOLVER API.

getrsStridedBatched solves a batch of systems of n linear equations on n variables in its factorized forms.

For each instance i in the batch, it solves one of the following systems, depending on the value of trans:

\[\begin{split} \begin{array}{cl} A_i X_i = B_i & \: \text{not transposed,}\\ A_i^T X_i = B_i & \: \text{transposed, or}\\ A_i^H X_i = B_i & \: \text{conjugate transposed.} \end{array} \end{split}\]Matrix \(A_i\) is defined by its triangular factors as returned by

[getrfStridedBatched](#hipblas_8h_1a177364030077e01b06ba7153ba0407a8).Supported precisions in rocSOLVER : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**hipblasHandle_t.**trans**–**[in]**hipblasOperation_t.

Specifies the form of the system of equations of each instance in the batch.

**n**–**[in]**int. n >= 0.

The order of the system, i.e. the number of columns and rows of all A_i matrices.

**nrhs**–**[in]**int. nrhs >= 0.

The number of right hand sides, i.e., the number of columns of all the matrices B_i.

**A**–**[in]**pointer to type. Array on the GPU (the size depends on the value of strideA).

The factors L_i and U_i of the factorization A_i = P_i*L_i*U_i returned by

[getrfStridedBatched](#hipblas_8h_1a177364030077e01b06ba7153ba0407a8).**lda**–**[in]**int. lda >= n.

The leading dimension of matrices A_i.

**strideA**–**[in]**hipblasStride.

Stride from the start of one matrix A_i to the next one A_(i+1). There is no restriction for the value of strideA. Normal use case is strideA >= lda*n.

**ipiv**–**[in]**pointer to int. Array on the GPU (the size depends on the value of strideP).

Contains the vectors ipiv_i of pivot indices returned by

[getrfStridedBatched](#hipblas_8h_1a177364030077e01b06ba7153ba0407a8).**strideP**–**[in]**hipblasStride.

Stride from the start of one vector ipiv_i to the next one ipiv_(i+1). There is no restriction for the value of strideP. Normal use case is strideP >= n.

**B**–**[inout]**pointer to type. Array on the GPU (size depends on the value of strideB).

On entry, the right hand side matrices B_i. On exit, the solution matrix X_i of each system in the batch.

**ldb**–**[in]**int. ldb >= n.

The leading dimension of matrices B_i.

**strideB**–**[in]**hipblasStride.

Stride from the start of one matrix B_i to the next one B_(i+1). There is no restriction for the value of strideB. Normal use case is strideB >= ldb*nrhs.

**info**–**[out]**pointer to a int on the host.

If info = 0, successful exit. If info = j < 0, the argument at position -j is invalid.

**batchCount**–**[in]**int. batchCount >= 0.

Number of instances (systems) in the batch.




-
hipblasStatus_t hipblasSgetriBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const int n, float *const A[], const int lda, int *ipiv, float *const C[], const int ldc, int *info, const int batchCount)[#](#_CPPv420hipblasSgetriBatched15hipblasHandle_tKiA_PCfKiPiA_PCfKiPiKi)

-
hipblasStatus_t hipblasDgetriBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const int n, double *const A[], const int lda, int *ipiv, double *const C[], const int ldc, int *info, const int batchCount)[#](#_CPPv420hipblasDgetriBatched15hipblasHandle_tKiA_PCdKiPiA_PCdKiPiKi)

-
hipblasStatus_t hipblasCgetriBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const int n, hipComplex *const A[], const int lda, int *ipiv, hipComplex *const C[], const int ldc, int *info, const int batchCount)[#](#_CPPv420hipblasCgetriBatched15hipblasHandle_tKiA_PC10hipComplexKiPiA_PC10hipComplexKiPiKi)

-
hipblasStatus_t hipblasZgetriBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const int n, hipDoubleComplex *const A[], const int lda, int *ipiv, hipDoubleComplex *const C[], const int ldc, int *info, const int batchCount)[#](#_CPPv420hipblasZgetriBatched15hipblasHandle_tKiA_PC16hipDoubleComplexKiPiA_PC16hipDoubleComplexKiPiKi) SOLVER API.

getriBatched computes the inverse \(C_i = A_i^{-1}\) of a batch of general n-by-n matrices \(A_i\).

The inverse is computed by solving the linear system

\[ A_i C_i = I \]where I is the identity matrix, and \(A_i\) is factorized as \(A_i = P_i L_i U_i\) as given by

[getrfBatched](#hipblas_8h_1a721bba1f328f6300b18e96cd1749d8a9).Supported precisions in rocSOLVER : s,d,c,z

Supported precisions in cuBLAS : s,d,c,z


- Parameters:
**handle**–**[in]**hipblasHandle_t.**n**–**[in]**int. n >= 0.

The number of rows and columns of all matrices A_i in the batch.

**A**–**[in]**array of pointers to type. Each pointer points to an array on the GPU of dimension lda*n.

The factors L_i and U_i of the factorization A_i = P_i*L_i*U_i returned by

[getrfBatched](#hipblas_8h_1a721bba1f328f6300b18e96cd1749d8a9).**lda**–**[in]**int. lda >= n.

Specifies the leading dimension of matrices A_i.

**ipiv**–**[in]**pointer to int. Array on the GPU (the size depends on the value of strideP).

The pivot indices returned by

[getrfBatched](#hipblas_8h_1a721bba1f328f6300b18e96cd1749d8a9). ipiv can be passed in as a nullptr, this will assume that getrfBatched was called without partial pivoting.**C**–**[out]**array of pointers to type. Each pointer points to an array on the GPU of dimension ldc*n.

If info[i] = 0, the inverse of matrices A_i. Otherwise, undefined.

**ldc**–**[in]**int. ldc >= n.

Specifies the leading dimension of C_i.

**info**–**[out]**pointer to int. Array of batchCount integers on the GPU.

If info[i] = 0, successful exit for inversion of A_i. If info[i] = j > 0, U_i is singular. U_i[j,j] is the first zero pivot.

**batchCount**–**[in]**int. batchCount >= 0.

Number of matrices in the batch.




-
hipblasStatus_t hipblasSgeqrf(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const int m, const int n, float *A, const int lda, float *ipiv, int *info)[#](#_CPPv413hipblasSgeqrf15hipblasHandle_tKiKiPfKiPfPi)

-
hipblasStatus_t hipblasDgeqrf(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const int m, const int n, double *A, const int lda, double *ipiv, int *info)[#](#_CPPv413hipblasDgeqrf15hipblasHandle_tKiKiPdKiPdPi)

-
hipblasStatus_t hipblasCgeqrf(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const int m, const int n, hipComplex *A, const int lda, hipComplex *ipiv, int *info)[#](#_CPPv413hipblasCgeqrf15hipblasHandle_tKiKiP10hipComplexKiP10hipComplexPi)

-
hipblasStatus_t hipblasZgeqrf(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const int m, const int n, hipDoubleComplex *A, const int lda, hipDoubleComplex *ipiv, int *info)[#](#_CPPv413hipblasZgeqrf15hipblasHandle_tKiKiP16hipDoubleComplexKiP16hipDoubleComplexPi) SOLVER API.

geqrf computes a QR factorization of a general m-by-n matrix A.

The factorization has the form

\[\begin{split} A = Q\left[\begin{array}{c} R\\ 0 \end{array}\right] \end{split}\]where R is upper triangular (upper trapezoidal if m < n), and Q is a m-by-m orthogonal/unitary matrix represented as the product of Householder matrices

\[ Q = H_1H_2\cdots H_k, \quad \text{with} \: k = \text{min}(m,n) \]Each Householder matrix \(H_i\) is given by

\[ H_i = I - \text{ipiv}[i] \cdot v_i v_i' \]where the first i-1 elements of the Householder vector \(v_i\) are zero, and \(v_i[i] = 1\).

Supported precisions in rocSOLVER : s,d,c,z

Supported precisions in cuBLAS : s,d,c,z


- Parameters:
**handle**–**[in]**hipblasHandle_t.**m**–**[in]**int. m >= 0.

The number of rows of the matrix A.

**n**–**[in]**int. n >= 0.

The number of columns of the matrix A.

**A**–**[inout]**pointer to type. Array on the GPU of dimension lda*n.

On entry, the m-by-n matrix to be factored. On exit, the elements on and above the diagonal contain the factor R; the elements below the diagonal are the last m - i elements of Householder vector v_i.

**lda**–**[in]**int. lda >= m.

Specifies the leading dimension of A.

**ipiv**–**[out]**pointer to type. Array on the GPU of dimension min(m,n).

The Householder scalars.

**info**–**[out]**pointer to a int on the host.

If info = 0, successful exit. If info = j < 0, the argument at position -j is invalid.




-
hipblasStatus_t hipblasSgeqrfBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const int m, const int n, float *const A[], const int lda, float *const ipiv[], int *info, const int batchCount)[#](#_CPPv420hipblasSgeqrfBatched15hipblasHandle_tKiKiA_PCfKiA_PCfPiKi)

-
hipblasStatus_t hipblasDgeqrfBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const int m, const int n, double *const A[], const int lda, double *const ipiv[], int *info, const int batchCount)[#](#_CPPv420hipblasDgeqrfBatched15hipblasHandle_tKiKiA_PCdKiA_PCdPiKi)

-
hipblasStatus_t hipblasCgeqrfBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const int m, const int n, hipComplex *const A[], const int lda, hipComplex *const ipiv[], int *info, const int batchCount)[#](#_CPPv420hipblasCgeqrfBatched15hipblasHandle_tKiKiA_PC10hipComplexKiA_PC10hipComplexPiKi)

-
hipblasStatus_t hipblasZgeqrfBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const int m, const int n, hipDoubleComplex *const A[], const int lda, hipDoubleComplex *const ipiv[], int *info, const int batchCount)[#](#_CPPv420hipblasZgeqrfBatched15hipblasHandle_tKiKiA_PC16hipDoubleComplexKiA_PC16hipDoubleComplexPiKi) SOLVER API.

geqrfBatched computes the QR factorization of a batch of general m-by-n matrices.

The factorization of matrix \(A_i\) in the batch has the form

\[\begin{split} A_i = Q_i\left[\begin{array}{c} R_i\\ 0 \end{array}\right] \end{split}\]where \(R_i\) is upper triangular (upper trapezoidal if m < n), and \(Q_i\) is a m-by-m orthogonal/unitary matrix represented as the product of Householder matrices

\[ Q_i = H_{i_1}H_{i_2}\cdots H_{i_k}, \quad \text{with} \: k = \text{min}(m,n) \]Each Householder matrix \(H_{i_j}\) is given by

\[ H_{i_j} = I - \text{ipiv}_i[j] \cdot v_{i_j} v_{i_j}' \]where the first j-1 elements of Householder vector \(v_{i_j}\) are zero, and \(v_{i_j}[j] = 1\).

Supported precisions in rocSOLVER : s,d,c,z

Supported precisions in cuBLAS : s,d,c,z


- Parameters:
**handle**–**[in]**hipblasHandle_t.**m**–**[in]**int. m >= 0.

The number of rows of all the matrices A_i in the batch.

**n**–**[in]**int. n >= 0.

The number of columns of all the matrices A_i in the batch.

**A**–**[inout]**Array of pointers to type. Each pointer points to an array on the GPU of dimension lda*n.

On entry, the m-by-n matrices A_i to be factored. On exit, the elements on and above the diagonal contain the factor R_i. The elements below the diagonal are the last m - j elements of Householder vector v_(i_j).

**lda**–**[in]**int. lda >= m.

Specifies the leading dimension of matrices A_i.

**ipiv**–**[out]**array of pointers to type. Each pointer points to an array on the GPU of dimension min(m, n).

Contains the vectors ipiv_i of corresponding Householder scalars.

**info**–**[out]**pointer to a int on the host.

If info = 0, successful exit. If info = j < 0, the argument at position -j is invalid.

**batchCount**–**[in]**int. batchCount >= 0.

Number of matrices in the batch.




-
hipblasStatus_t hipblasSgeqrfStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const int m, const int n, float *A, const int lda, const[hipblasStride](#_CPPv413hipblasStride)strideA, float *ipiv, const[hipblasStride](#_CPPv413hipblasStride)strideP, int *info, const int batchCount)[#](#_CPPv427hipblasSgeqrfStridedBatched15hipblasHandle_tKiKiPfKiK13hipblasStridePfK13hipblasStridePiKi)

-
hipblasStatus_t hipblasDgeqrfStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const int m, const int n, double *A, const int lda, const[hipblasStride](#_CPPv413hipblasStride)strideA, double *ipiv, const[hipblasStride](#_CPPv413hipblasStride)strideP, int *info, const int batchCount)[#](#_CPPv427hipblasDgeqrfStridedBatched15hipblasHandle_tKiKiPdKiK13hipblasStridePdK13hipblasStridePiKi)

-
hipblasStatus_t hipblasCgeqrfStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const int m, const int n, hipComplex *A, const int lda, const[hipblasStride](#_CPPv413hipblasStride)strideA, hipComplex *ipiv, const[hipblasStride](#_CPPv413hipblasStride)strideP, int *info, const int batchCount)[#](#_CPPv427hipblasCgeqrfStridedBatched15hipblasHandle_tKiKiP10hipComplexKiK13hipblasStrideP10hipComplexK13hipblasStridePiKi)

-
hipblasStatus_t hipblasZgeqrfStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, const int m, const int n, hipDoubleComplex *A, const int lda, const[hipblasStride](#_CPPv413hipblasStride)strideA, hipDoubleComplex *ipiv, const[hipblasStride](#_CPPv413hipblasStride)strideP, int *info, const int batchCount)[#](#_CPPv427hipblasZgeqrfStridedBatched15hipblasHandle_tKiKiP16hipDoubleComplexKiK13hipblasStrideP16hipDoubleComplexK13hipblasStridePiKi) SOLVER API.

geqrfStridedBatched computes the QR factorization of a batch of general m-by-n matrices.

The factorization of matrix \(A_i\) in the batch has the form

\[\begin{split} A_i = Q_i\left[\begin{array}{c} R_i\\ 0 \end{array}\right] \end{split}\]where \(R_i\) is upper triangular (upper trapezoidal if m < n), and \(Q_i\) is a m-by-m orthogonal/unitary matrix represented as the product of Householder matrices

\[ Q_i = H_{i_1}H_{i_2}\cdots H_{i_k}, \quad \text{with} \: k = \text{min}(m,n) \]Each Householder matrix \(H_{i_j}\) is given by

\[ H_{i_j} = I - \text{ipiv}_j[j] \cdot v_{i_j} v_{i_j}' \]where the first j-1 elements of Householder vector \(v_{i_j}\) are zero, and \(v_{i_j}[j] = 1\).

Supported precisions in rocSOLVER : s,d,c,z

Supported precisions in cuBLAS : No support


- Parameters:
**handle**–**[in]**hipblasHandle_t.**m**–**[in]**int. m >= 0.

The number of rows of all the matrices A_i in the batch.

**n**–**[in]**int. n >= 0.

The number of columns of all the matrices A_i in the batch.

**A**–**[inout]**pointer to type. Array on the GPU (the size depends on the value of strideA).

On entry, the m-by-n matrices A_i to be factored. On exit, the elements on and above the diagonal contain the factor R_i. The elements below the diagonal are the last m - j elements of Householder vector v_(i_j).

**lda**–**[in]**int. lda >= m.

Specifies the leading dimension of matrices A_i.

**strideA**–**[in]**hipblasStride.

Stride from the start of one matrix A_i to the next one A_(i+1). There is no restriction for the value of strideA. Normal use case is strideA >= lda*n.

**ipiv**–**[out]**pointer to type. Array on the GPU (the size depends on the value of strideP).

Contains the vectors ipiv_i of corresponding Householder scalars.

**strideP**–**[in]**hipblasStride.

Stride from the start of one vector ipiv_i to the next one ipiv_(i+1). There is no restriction for the value of strideP. Normal use is strideP >= min(m,n).

**info**–**[out]**pointer to a int on the host.

If info = 0, successful exit. If info = j < 0, the argument at position -j is invalid.

**batchCount**–**[in]**int. batchCount >= 0.

Number of matrices in the batch.




-
hipblasStatus_t hipblasSgels(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, const int m, const int n, const int nrhs, float *A, const int lda, float *B, const int ldb, int *info, int *deviceInfo)[#](#_CPPv412hipblasSgels15hipblasHandle_t18hipblasOperation_tKiKiKiPfKiPfKiPiPi)

-
hipblasStatus_t hipblasDgels(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, const int m, const int n, const int nrhs, double *A, const int lda, double *B, const int ldb, int *info, int *deviceInfo)[#](#_CPPv412hipblasDgels15hipblasHandle_t18hipblasOperation_tKiKiKiPdKiPdKiPiPi)

-
hipblasStatus_t hipblasCgels(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, const int m, const int n, const int nrhs, hipComplex *A, const int lda, hipComplex *B, const int ldb, int *info, int *deviceInfo)[#](#_CPPv412hipblasCgels15hipblasHandle_t18hipblasOperation_tKiKiKiP10hipComplexKiP10hipComplexKiPiPi)

-
hipblasStatus_t hipblasZgels(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, const int m, const int n, const int nrhs, hipDoubleComplex *A, const int lda, hipDoubleComplex *B, const int ldb, int *info, int *deviceInfo)[#](#_CPPv412hipblasZgels15hipblasHandle_t18hipblasOperation_tKiKiKiP16hipDoubleComplexKiP16hipDoubleComplexKiPiPi) GELS solves an overdetermined (or underdetermined) linear system defined by an m-by-n matrix A, and a corresponding matrix B, using the QR factorization computed by

[GEQRF](#hipblas_8h_1a33be31a47447c76aa30a2f5022ca821b)(or the LQ factorization computed by “GELQF”).Depending on the value of trans, the problem solved by this function is either of the form

\[\begin{split} \begin{array}{cl} A X = B & \: \text{not transposed, or}\\ A' X = B & \: \text{transposed if real, or conjugate transposed if complex} \end{array} \end{split}\]If m >= n (or m < n in the case of transpose/conjugate transpose), the system is overdetermined and a least-squares solution approximating X is found by minimizing

\[ || B - A X || \quad \text{(or} \: || B - A' X ||\text{)} \]If m < n (or m >= n in the case of transpose/conjugate transpose), the system is underdetermined and a unique solution for X is chosen such that \(|| X ||\) is minimal.

Supported precisions in rocSOLVER : s,d,c,z

Supported precisions in cuBLAS : currently unsupported


- Parameters:
**handle**–**[in]**hipblasHandle_t.**trans**–**[in]**hipblasOperation_t.

Specifies the form of the system of equations.

**m**–**[in]**int. m >= 0.

The number of rows of matrix A.

**n**–**[in]**int. n >= 0.

The number of columns of matrix A.

**nrhs**–**[in]**int. nrhs >= 0.

The number of columns of matrices B and X; i.e., the columns on the right hand side.

**A**–**[inout]**pointer to type. Array on the GPU of dimension lda*n.

On entry, the matrix A. On exit, the QR (or LQ) factorization of A as returned by “GEQRF” (or “GELQF”).

**lda**–**[in]**int. lda >= m.

Specifies the leading dimension of matrix A.

**B**–**[inout]**pointer to type. Array on the GPU of dimension ldb*nrhs.

On entry, the matrix B. On exit, when info = 0, B is overwritten by the solution vectors (and the residuals in the overdetermined cases) stored as columns.

**ldb**–**[in]**int. ldb >= max(m,n).

Specifies the leading dimension of matrix B.

**info**–**[out]**pointer to an int on the host.

If info = 0, successful exit. If info = j < 0, the argument at position -j is invalid.

**deviceInfo**–**[out]**pointer to int on the GPU.

If info = 0, successful exit. If info = i > 0, the solution could not be computed because input matrix A is rank deficient; the i-th diagonal element of its triangular factor is zero.




-
hipblasStatus_t hipblasSgelsBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, const int m, const int n, const int nrhs, float *const A[], const int lda, float *const B[], const int ldb, int *info, int *deviceInfo, const int batchCount)[#](#_CPPv419hipblasSgelsBatched15hipblasHandle_t18hipblasOperation_tKiKiKiA_PCfKiA_PCfKiPiPiKi)

-
hipblasStatus_t hipblasDgelsBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, const int m, const int n, const int nrhs, double *const A[], const int lda, double *const B[], const int ldb, int *info, int *deviceInfo, const int batchCount)[#](#_CPPv419hipblasDgelsBatched15hipblasHandle_t18hipblasOperation_tKiKiKiA_PCdKiA_PCdKiPiPiKi)

-
hipblasStatus_t hipblasCgelsBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, const int m, const int n, const int nrhs, hipComplex *const A[], const int lda, hipComplex *const B[], const int ldb, int *info, int *deviceInfo, const int batchCount)[#](#_CPPv419hipblasCgelsBatched15hipblasHandle_t18hipblasOperation_tKiKiKiA_PC10hipComplexKiA_PC10hipComplexKiPiPiKi)

-
hipblasStatus_t hipblasZgelsBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, const int m, const int n, const int nrhs, hipDoubleComplex *const A[], const int lda, hipDoubleComplex *const B[], const int ldb, int *info, int *deviceInfo, const int batchCount)[#](#_CPPv419hipblasZgelsBatched15hipblasHandle_t18hipblasOperation_tKiKiKiA_PC16hipDoubleComplexKiA_PC16hipDoubleComplexKiPiPiKi) gelsBatched solves a batch of overdetermined (or underdetermined) linear systems defined by a set of m-by-n matrices \(A_j\), and corresponding matrices \(B_j\), using the QR factorizations computed by “GEQRF_BATCHED” (or the LQ factorizations computed by “GELQF_BATCHED”).

For each instance in the batch, depending on the value of trans, the problem solved by this function is either of the form

\[\begin{split} \begin{array}{cl} A_j X_j = B_j & \: \text{not transposed, or}\\ A_j' X_j = B_j & \: \text{transposed if real, or conjugate transposed if complex} \end{array} \end{split}\]If m >= n (or m < n in the case of transpose/conjugate transpose), the system is overdetermined and a least-squares solution approximating X_j is found by minimizing

\[ || B_j - A_j X_j || \quad \text{(or} \: || B_j - A_j' X_j ||\text{)} \]If m < n (or m >= n in the case of transpose/conjugate transpose), the system is underdetermined and a unique solution for X_j is chosen such that \(|| X_j ||\) is minimal.

Supported precisions in rocSOLVER : s,d,c,z

Supported precisions in cuBLAS : s,d,c,z Note that cuBLAS backend supports only the non-transpose operation and only solves over-determined systems (m >= n).


- Parameters:
**handle**–**[in]**hipblasHandle_t.**trans**–**[in]**hipblasOperation_t.

Specifies the form of the system of equations.

**m**–**[in]**int. m >= 0.

The number of rows of all matrices A_j in the batch.

**n**–**[in]**int. n >= 0.

The number of columns of all matrices A_j in the batch.

**nrhs**–**[in]**int. nrhs >= 0.

The number of columns of all matrices B_j and X_j in the batch; i.e., the columns on the right hand side.

**A**–**[inout]**array of pointer to type. Each pointer points to an array on the GPU of dimension lda*n.

On entry, the matrices A_j. On exit, the QR (or LQ) factorizations of A_j as returned by “GEQRF_BATCHED” (or “GELQF_BATCHED”).

**lda**–**[in]**int. lda >= m.

Specifies the leading dimension of matrices A_j.

**B**–**[inout]**array of pointer to type. Each pointer points to an array on the GPU of dimension ldb*nrhs.

On entry, the matrices B_j. On exit, when info[j] = 0, B_j is overwritten by the solution vectors (and the residuals in the overdetermined cases) stored as columns.

**ldb**–**[in]**int. ldb >= max(m,n).

Specifies the leading dimension of matrices B_j.

**info**–**[out]**pointer to an int on the host.

If info = 0, successful exit. If info = j < 0, the argument at position -j is invalid.

**deviceInfo**–**[out]**pointer to int. Array of batchCount integers on the GPU.

If deviceInfo[j] = 0, successful exit for solution of A_j. If deviceInfo[j] = i > 0, the solution of A_j could not be computed because input matrix A_j is rank deficient; the i-th diagonal element of its triangular factor is zero.

**batchCount**–**[in]**int. batchCount >= 0.

Number of matrices in the batch.




-
hipblasStatus_t hipblasSgelsStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, const int m, const int n, const int nrhs, float *A, const int lda, const[hipblasStride](#_CPPv413hipblasStride)strideA, float *B, const int ldb, const[hipblasStride](#_CPPv413hipblasStride)strideB, int *info, int *deviceInfo, const int batchCount)[#](#_CPPv426hipblasSgelsStridedBatched15hipblasHandle_t18hipblasOperation_tKiKiKiPfKiK13hipblasStridePfKiK13hipblasStridePiPiKi)

-
hipblasStatus_t hipblasDgelsStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, const int m, const int n, const int nrhs, double *A, const int lda, const[hipblasStride](#_CPPv413hipblasStride)strideA, double *B, const int ldb, const[hipblasStride](#_CPPv413hipblasStride)strideB, int *info, int *deviceInfo, const int batchCount)[#](#_CPPv426hipblasDgelsStridedBatched15hipblasHandle_t18hipblasOperation_tKiKiKiPdKiK13hipblasStridePdKiK13hipblasStridePiPiKi)

-
hipblasStatus_t hipblasCgelsStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, const int m, const int n, const int nrhs, hipComplex *A, const int lda, const[hipblasStride](#_CPPv413hipblasStride)strideA, hipComplex *B, const int ldb, const[hipblasStride](#_CPPv413hipblasStride)strideB, int *info, int *deviceInfo, const int batchCount)[#](#_CPPv426hipblasCgelsStridedBatched15hipblasHandle_t18hipblasOperation_tKiKiKiP10hipComplexKiK13hipblasStrideP10hipComplexKiK13hipblasStridePiPiKi)

-
hipblasStatus_t hipblasZgelsStridedBatched(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)trans, const int m, const int n, const int nrhs, hipDoubleComplex *A, const int lda, const[hipblasStride](#_CPPv413hipblasStride)strideA, hipDoubleComplex *B, const int ldb, const[hipblasStride](#_CPPv413hipblasStride)strideB, int *info, int *deviceInfo, const int batchCount)[#](#_CPPv426hipblasZgelsStridedBatched15hipblasHandle_t18hipblasOperation_tKiKiKiP16hipDoubleComplexKiK13hipblasStrideP16hipDoubleComplexKiK13hipblasStridePiPiKi) gelsStridedBatched solves a batch of overdetermined (or underdetermined) linear systems defined by a set of m-by-n matrices \(A_j\), and corresponding matrices \(B_j\), using the QR factorizations computed by “GEQRF_STRIDED_BATCHED” (or the LQ factorizations computed by “GELQF_STRIDED_BATCHED”).

For each instance in the batch, depending on the value of trans, the problem solved by this function is either of the form

\[\begin{split} \begin{array}{cl} A_j X_j = B_j & \: \text{not transposed, or}\\ A_j' X_j = B_j & \: \text{transposed if real, or conjugate transposed if complex} \end{array} \end{split}\]If m >= n (or m < n in the case of transpose/conjugate transpose), the system is overdetermined and a least-squares solution approximating X_j is found by minimizing

\[ || B_j - A_j X_j || \quad \text{(or} \: || B_j - A_j' X_j ||\text{)} \]If m < n (or m >= n in the case of transpose/conjugate transpose), the system is underdetermined and a unique solution for X_j is chosen such that \(|| X_j ||\) is minimal.

Supported precisions in rocSOLVER : s,d,c,z

Supported precisions in cuBLAS : currently unsupported


- Parameters:
**handle**–**[in]**hipblasHandle_t.**trans**–**[in]**hipblasOperation_t.

Specifies the form of the system of equations.

**m**–**[in]**int. m >= 0.

The number of rows of all matrices A_j in the batch.

**n**–**[in]**int. n >= 0.

The number of columns of all matrices A_j in the batch.

**nrhs**–**[in]**int. nrhs >= 0.

The number of columns of all matrices B_j and X_j in the batch; i.e., the columns on the right hand side.

**A**–**[inout]**pointer to type. Array on the GPU (the size depends on the value of strideA).

On entry, the matrices A_j. On exit, the QR (or LQ) factorizations of A_j as returned by “GEQRF_STRIDED_BATCHED” (or “GELQF_STRIDED_BATCHED”).

**lda**–**[in]**int. lda >= m.

Specifies the leading dimension of matrices A_j.

**strideA**–**[in]**hipblasStride.

Stride from the start of one matrix A_j to the next one A_(j+1). There is no restriction for the value of strideA. Normal use case is strideA >= lda*n

**B**–**[inout]**pointer to type. Array on the GPU (the size depends on the value of strideB).

On entry, the matrices B_j. On exit, when info[j] = 0, each B_j is overwritten by the solution vectors (and the residuals in the overdetermined cases) stored as columns.

**ldb**–**[in]**int. ldb >= max(m,n).

Specifies the leading dimension of matrices B_j.

**strideB**–**[in]**hipblasStride.

Stride from the start of one matrix B_j to the next one B_(j+1). There is no restriction for the value of strideB. Normal use case is strideB >= ldb*nrhs

**info**–**[out]**pointer to an int on the host.

If info = 0, successful exit. If info = j < 0, the argument at position -j is invalid.

**deviceInfo**–**[out]**pointer to int. Array of batchCount integers on the GPU.

If deviceInfo[j] = 0, successful exit for solution of A_j. If deviceInfo[j] = i > 0, the solution of A_j could not be computed because input matrix A_j is rank deficient; the i-th diagonal element of its triangular factor is zero.

**batchCount**–**[in]**int. batchCount >= 0.

Number of matrices in the batch.




## Auxiliary[#](#auxiliary)

### hipblasCreate[#](#hipblascreate)

-
hipblasStatus_t hipblasCreate(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)*handle)[#](#_CPPv413hipblasCreateP15hipblasHandle_t) Create hipblas handle.


### hipblasDestroy[#](#hipblasdestroy)

-
hipblasStatus_t hipblasDestroy(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle)[#](#_CPPv414hipblasDestroy15hipblasHandle_t) Destroys the library context created using

[hipblasCreate()](#hipblas_8h_1a7d90472ea2e53d6d82d299228480d6da)

### hipblasSetStream[#](#hipblassetstream)

-
hipblasStatus_t hipblasSetStream(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, hipStream_t streamId)[#](#_CPPv416hipblasSetStream15hipblasHandle_t11hipStream_t) Set stream for handle.


### hipblasGetStream[#](#hipblasgetstream)

-
hipblasStatus_t hipblasGetStream(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle, hipStream_t *streamId)[#](#_CPPv416hipblasGetStream15hipblasHandle_tP11hipStream_t) Get stream[0] for handle.


### hipblasSetPointerMode[#](#hipblassetpointermode)

-
hipblasStatus_t hipblasSetPointerMode(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasPointerMode_t](#_CPPv420hipblasPointerMode_t)mode)[#](#_CPPv421hipblasSetPointerMode15hipblasHandle_t20hipblasPointerMode_t) Set hipblas pointer mode.


### hipblasGetPointerMode[#](#hipblasgetpointermode)

-
hipblasStatus_t hipblasGetPointerMode(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasPointerMode_t](#_CPPv420hipblasPointerMode_t)*mode)[#](#_CPPv421hipblasGetPointerMode15hipblasHandle_tP20hipblasPointerMode_t) Get hipblas pointer mode.


### hipblasSetVector[#](#hipblassetvector)

-
hipblasStatus_t hipblasSetVector(int n, int elemSize, const void *x, int incx, void *y, int incy)
[#](#_CPPv416hipblasSetVectoriiPKviPvi) copy vector from host to device

- Parameters:
**n**–**[in]**[int] number of elements in the vector**elemSize**–**[in]**[int] Size of both vectors in bytes**x**–**[in]**pointer to vector on the host**incx**–**[in]**[int] specifies the increment for the elements of the vector**y**–**[out]**pointer to vector on the device**incy**–**[in]**[int] specifies the increment for the elements of the vector



### hipblasGetVector[#](#hipblasgetvector)

-
hipblasStatus_t hipblasGetVector(int n, int elemSize, const void *x, int incx, void *y, int incy)
[#](#_CPPv416hipblasGetVectoriiPKviPvi) copy vector from device to host

- Parameters:
**n**–**[in]**[int] number of elements in the vector**elemSize**–**[in]**[int] Size of both vectors in bytes**x**–**[in]**pointer to vector on the device**incx**–**[in]**[int] specifies the increment for the elements of the vector**y**–**[out]**pointer to vector on the host**incy**–**[in]**[int] specifies the increment for the elements of the vector



### hipblasSetMatrix[#](#hipblassetmatrix)

-
hipblasStatus_t hipblasSetMatrix(int rows, int cols, int elemSize, const void *AP, int lda, void *BP, int ldb)
[#](#_CPPv416hipblasSetMatrixiiiPKviPvi) copy matrix from host to device

- Parameters:
**rows**–**[in]**[int] number of rows in matrices**cols**–**[in]**[int] number of columns in matrices**elemSize**–**[in]**[int] number of bytes per element in the matrix**AP**–**[in]**pointer to matrix on the host**lda**–**[in]**[int] specifies the leading dimension of A, lda >= rows**BP**–**[out]**pointer to matrix on the GPU**ldb**–**[in]**[int] specifies the leading dimension of B, ldb >= rows



### hipblasGetMatrix[#](#hipblasgetmatrix)

-
hipblasStatus_t hipblasGetMatrix(int rows, int cols, int elemSize, const void *AP, int lda, void *BP, int ldb)
[#](#_CPPv416hipblasGetMatrixiiiPKviPvi) copy matrix from device to host

- Parameters:
**rows**–**[in]**[int] number of rows in matrices**cols**–**[in]**[int] number of columns in matrices**elemSize**–**[in]**[int] number of bytes per element in the matrix**AP**–**[in]**pointer to matrix on the GPU**lda**–**[in]**[int] specifies the leading dimension of A, lda >= rows**BP**–**[out]**pointer to matrix on the host**ldb**–**[in]**[int] specifies the leading dimension of B, ldb >= rows



### hipblasSetVectorAsync[#](#hipblassetvectorasync)

-
hipblasStatus_t hipblasSetVectorAsync(int n, int elemSize, const void *x, int incx, void *y, int incy, hipStream_t stream)
[#](#_CPPv421hipblasSetVectorAsynciiPKviPvi11hipStream_t) asynchronously copy vector from host to device

hipblasSetVectorAsync copies a vector from pinned host memory to device memory asynchronously. Memory on the host must be allocated with hipHostMalloc or the transfer will be synchronous.

- Parameters:
**n**–**[in]**[int] number of elements in the vector**elemSize**–**[in]**[int] number of bytes per element in the matrix**x**–**[in]**pointer to vector on the host**incx**–**[in]**[int] specifies the increment for the elements of the vector**y**–**[out]**pointer to vector on the device**incy**–**[in]**[int] specifies the increment for the elements of the vector**stream**–**[in]**specifies the stream into which this transfer request is queued



### hipblasGetVectorAsync[#](#hipblasgetvectorasync)

-
hipblasStatus_t hipblasGetVectorAsync(int n, int elemSize, const void *x, int incx, void *y, int incy, hipStream_t stream)
[#](#_CPPv421hipblasGetVectorAsynciiPKviPvi11hipStream_t) asynchronously copy vector from device to host

hipblasGetVectorAsync copies a vector from pinned host memory to device memory asynchronously. Memory on the host must be allocated with hipHostMalloc or the transfer will be synchronous.

- Parameters:
**n**–**[in]**[int] number of elements in the vector**elemSize**–**[in]**[int] number of bytes per element in the matrix**x**–**[in]**pointer to vector on the device**incx**–**[in]**[int] specifies the increment for the elements of the vector**y**–**[out]**pointer to vector on the host**incy**–**[in]**[int] specifies the increment for the elements of the vector**stream**–**[in]**specifies the stream into which this transfer request is queued



### hipblasSetMatrixAsync[#](#hipblassetmatrixasync)

-
hipblasStatus_t hipblasSetMatrixAsync(int rows, int cols, int elemSize, const void *AP, int lda, void *BP, int ldb, hipStream_t stream)
[#](#_CPPv421hipblasSetMatrixAsynciiiPKviPvi11hipStream_t) asynchronously copy matrix from host to device

hipblasSetMatrixAsync copies a matrix from pinned host memory to device memory asynchronously. Memory on the host must be allocated with hipHostMalloc or the transfer will be synchronous.

- Parameters:
**rows**–**[in]**[int] number of rows in matrices**cols**–**[in]**[int] number of columns in matrices**elemSize**–**[in]**[int] number of bytes per element in the matrix**AP**–**[in]**pointer to matrix on the host**lda**–**[in]**[int] specifies the leading dimension of A, lda >= rows**BP**–**[out]**pointer to matrix on the GPU**ldb**–**[in]**[int] specifies the leading dimension of B, ldb >= rows**stream**–**[in]**specifies the stream into which this transfer request is queued



### hipblasGetMatrixAsync[#](#hipblasgetmatrixasync)

-
hipblasStatus_t hipblasGetMatrixAsync(int rows, int cols, int elemSize, const void *AP, int lda, void *BP, int ldb, hipStream_t stream)
[#](#_CPPv421hipblasGetMatrixAsynciiiPKviPvi11hipStream_t) asynchronously copy matrix from device to host

hipblasGetMatrixAsync copies a matrix from device memory to pinned host memory asynchronously. Memory on the host must be allocated with hipHostMalloc or the transfer will be synchronous.

- Parameters:
**rows**–**[in]**[int] number of rows in matrices**cols**–**[in]**[int] number of columns in matrices**elemSize**–**[in]**[int] number of bytes per element in the matrix**AP**–**[in]**pointer to matrix on the GPU**lda**–**[in]**[int] specifies the leading dimension of A, lda >= rows**BP**–**[out]**pointer to matrix on the host**ldb**–**[in]**[int] specifies the leading dimension of B, ldb >= rows**stream**–**[in]**specifies the stream into which this transfer request is queued



### hipblasSetAtomicsMode[#](#hipblassetatomicsmode)

-
hipblasStatus_t hipblasSetAtomicsMode(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasAtomicsMode_t](#_CPPv420hipblasAtomicsMode_t)atomics_mode)[#](#_CPPv421hipblasSetAtomicsMode15hipblasHandle_t20hipblasAtomicsMode_t) Set hipblasSetAtomicsMode.


### hipblasGetAtomicsMode[#](#hipblasgetatomicsmode)

-
hipblasStatus_t hipblasGetAtomicsMode(
[hipblasHandle_t](#_CPPv415hipblasHandle_t)handle,[hipblasAtomicsMode_t](#_CPPv420hipblasAtomicsMode_t)*atomics_mode)[#](#_CPPv421hipblasGetAtomicsMode15hipblasHandle_tP20hipblasAtomicsMode_t) Get hipblasSetAtomicsMode.


### hipblasStatusToString[#](#hipblasstatustostring)

-
const char *hipblasStatusToString(hipblasStatus_t status)
[#](#_CPPv421hipblasStatusToString15hipblasStatus_t) HIPBLAS Auxiliary API

hipblasStatusToString

Returns string representing hipblasStatus_t value

- Parameters:
**status**–**[in]**[hipblasStatus_t] hipBLAS status to convert to string
