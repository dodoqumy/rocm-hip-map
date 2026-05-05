---
title: "Using hipSOLVER &#8212; hipSOLVER 3.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/howto/usage.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:20:50.812707+00:00
content_hash: "850022c335a9dab7"
---

# Using hipSOLVER[#](#using-hipsolver)

hipSOLVER is an open-source marshalling library for [LAPACK routines](https://www.netlib.org/lapack/index.html) on the GPU.
It sits between a backend library and the user application, marshalling inputs to and outputs from the backend library so that the user
application doesn’t have to change when using different backends. hipSOLVER supports two backend libraries: The NVIDIA CUDA [cuSOLVER
library](https://developer.nvidia.com/cusolver) and the open-source AMD ROCm [rocSOLVER library](https://rocm.docs.amd.com/projects/rocSOLVER/en/latest/index.html).
For more background on the LAPACK routines, see the [introduction to rocSOLVER](https://rocm.docs.amd.com/projects/rocSOLVER/en/latest/conceptual/intro-rocsolver.html).

The [regular hipSOLVER API](../reference/api/index.html#library-api) is a thin wrapper layer around the different backends that does not typically introduce
significant overhead. However, its main purpose is portability, so when performance is critical, it’s recommended to
use the library backend directly.

After it is installed, hipSOLVER can be used like any other library with a C API. The header file has to be included in the user code, which means the shared library becomes a link-time and run-time dependency for the user application. The user application code can be ported with no changes to any system with hipSOLVER installed, regardless of the backend library.

For more details on how to use the API methods, see the client code samples in the
[rocm-libraries GitHub](https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipsolver/clients/samples) or
the documentation for the corresponding backend libraries.

## Multi-level logging in hipSOLVER[#](#multi-level-logging-in-hipsolver)

hipSOLVER can leverage the rocSOLVER logging functionality by using the rocSOLVER environment variables.
Upon handle creation, hipSOLVER retrieves these variables using `std::getenv`

.

To enable hipSOLVER logging, specify the default layer mode and max level depth using the following environment variables:

`ROCSOLVER_LAYER`

`ROCSOLVER_LEVELS`


For more details on how to set these variables to configure logging output, see [rocSOLVER logging](https://rocm.docs.amd.com/projects/rocSOLVER/en/latest/howto/logging.html).

## Porting cuSOLVER applications to hipSOLVER[#](#porting-cusolver-applications-to-hipsolver)

The hipSOLVER design facilitates the translation of cuSOLVER applications to the AMD open-source
[ROCm](https://rocm.docs.amd.com/en/latest/index.html) platform and ecosystem.
This makes it easy for you to port your existing cuSOLVER applications to hipSOLVER. hipSOLVER provides two
separate but interchangeable API patterns to facilitate a two-stage transition process. Users are encouraged to start with
the hipSOLVER compatibility APIs, which use the [hipsolverDn](../reference/dense-api/index.html#library-dense), [hipsolverSp](../reference/sparse-api/index.html#library-sparse), and
[hipsolverRf](../reference/refactor-api/index.html#library-refactor) prefixes and have method signatures that are fully consistent with cuSOLVER functions.

However, the compatibility APIs might introduce some performance drawbacks, especially when using the rocSOLVER backend. So, as a second
stage, it’s best to switch to using the hipSOLVER [regular API](../reference/api/index.html#library-api) when possible. The regular API uses the `hipsolver`

prefix.
It makes minor adjustments to the API to get the best performance out of the rocSOLVER backend. In most cases, switching to
the regular API is as simple as removing `Dn`

from the `hipsolverDn`

prefix.

Note

Methods with the `hipsolverSp`

and `hipsolverRf`

prefixes are not currently supported by the regular API.

No matter which API is used, a hipSOLVER application can be executed without modifications to the code on systems with cuSOLVER or rocSOLVER installed. However, using the regular API ensures the best performance out of both backends.

## Using the hipsolverDn API[#](#using-the-hipsolverdn-api)

The hipsolverDn API is intended as a 1:1 translation of the cusolverDn API, but not all functionality is equally supported in rocSOLVER. The following considerations apply when using this compatibility API.

### Arguments not referenced by rocSOLVER[#](#arguments-not-referenced-by-rocsolver)

Unlike cuSOLVER, rocSOLVER functions do not provide information on invalid arguments in the

`info`

parameter, although they do provide info on singularities and algorithm convergence. Therefore, when using the rocSOLVER backend,`info`

always returns a value >= 0. In cases where a rocSOLVER function does not accept`info`

as an argument, hipSOLVER sets it to zero.The

`niters`

argument for[hipsolverDnXXgels](../reference/dense-api/lapack.html#dense-gels)and[hipsolverDnXXgesv](../reference/dense-api/lapack.html#dense-gesv)is not referenced by the rocSOLVER backend. rocSOLVER does not implement an iterative refinement.The

`hRnrmF`

argument for[hipsolverDnXgesvdaStridedBatched](../reference/dense-api/lapacklike.html#dense-gesvda-strided-batched)is not referenced by the rocSOLVER backend.

### Performance implications of the hipsolverDn API[#](#performance-implications-of-the-hipsolverdn-api)

To calculate the workspace required by the

`gesvd`

function in rocSOLVER, the values of`jobu`

and`jobv`

are needed. However, the function[hipsolverDnXgesvd_bufferSize](../reference/dense-api/lapack.html#dense-gesvd-buffersize)does not accept these arguments. When using the rocSOLVER backend,`hipsolverDnXgesvd_bufferSize`

has to internally calculate the workspace for all possible values of`jobu`

and`jobv`

and return the maximum.Note

`hipsolverDnXgesvd_bufferSize`

is slower than`hipsolverXgesvd_bufferSize`

, and the workspace size it returns might be slightly larger than what is actually required.To properly use a user-provided workspace, rocSOLVER requires both the allocated pointer and its size. However, the function

[hipsolverDnXgetrf](../reference/dense-api/lapack.html#dense-getrf)does not accept`lwork`

as an argument. Consequently, when using the rocSOLVER backend,`hipsolverDnXgetrf`

has to internally call`hipsolverDnXgetrf_bufferSize`

to obtain the workspace size.Note

In practice,

`hipsolverDnXgetrf_bufferSize`

is called twice, once by the user before allocating the workspace and once by hipSOLVER internally when executing the`hipsolverDnXgetrf`

function.`hipsolverDnXgetrf`

can be slightly slower than`hipsolverXgetrf`

because of the extra call to the`bufferSize`

helper.The functions

[hipsolverDnXgetrs](../reference/dense-api/lapack.html#dense-getrs),[hipsolverDnXpotrs](../reference/dense-api/lapack.html#dense-potrs),[hipsolverDnXpotrsBatched](../reference/dense-api/lapack.html#dense-potrs-batched), and[hipsolverDnXpotrfBatched](../reference/dense-api/lapack.html#dense-potrf-batched)do not accept`work`

and`lwork`

as arguments. However, this functionality does require a non-zero workspace in rocSOLVER. As a result, these functions switch to the automatic workspace management model when using the rocSOLVER backend. For more information, see the[memory model information](#mem-model).Note

Even though the compatibility API does not provide

`bufferSize`

helpers for these functions, the functions still require a workspace to use rocSOLVER. This workspace is automatically managed, but it might result in device memory reallocations with a corresponding overhead.

## Using the hipsolverSp API[#](#using-the-hipsolversp-api)

The hipsolverSp API is intended as a 1:1 translation of the cusolverSp API, but not all functionality is equally supported in rocSOLVER. The following considerations apply when using this compatibility API.

### Unsupported methods[#](#unsupported-methods)

RCM reordering is not supported by rocSOLVER, rocSPARSE, and SuiteSparse. The following methods use AMD reordering instead when RCM is requested.

[hipsolverSpXcsrlsvcholHost](../reference/sparse-api/sparse.html#sparse-csrlsvcholhost)with`reorder = 1`

[hipsolverSpXcsrlsvchol](../reference/sparse-api/sparse.html#sparse-csrlsvchol)with`reorder = 1`


The function

[hipsolverSpScsrlsvqr](../reference/sparse-api/sparse.html#sparse-csrlsvqr)is implemented by converting the sparse input matrix to a dense matrix. It therefore does not support any reordering method. The host path is also unsupported.

### Arguments not referenced by rocSOLVER[#](#id1)

The

`reorder`

and`tolerance`

arguments of[hipsolverSpScsrlsvqr](../reference/sparse-api/sparse.html#sparse-csrlsvqr)are not referenced by the rocSOLVER backend.

### Performance implications of the hipsolverSp API[#](#performance-implications-of-the-hipsolversp-api)

The third-party SuiteSparse library is used to provide host-side functionality for

[hipsolverSpXcsrlsvchol](../reference/sparse-api/sparse.html#sparse-csrlsvchol)when using the rocSOLVER backend. SuiteSparse does not support single-precision arrays, so hipSOLVER must allocate temporary double-precision arrays and copy the values one-by-one to and from the user-provided arguments.A fully-featured, GPU-accelerated Cholesky factorization for sparse matrices is not implemented in either rocSOLVER or rocSPARSE. These components rely on SuiteSparse to provide this functionality. The

[hipsolverSpXcsrlsvchol](../reference/sparse-api/sparse.html#sparse-csrlsvchol)functions allocate space for sparse matrices on the host, copy the data to the host, use SuiteSparse to perform the symbolic factorization, and then copy the resulting data back to the device.The function

[hipsolverSpScsrlsvqr](../reference/sparse-api/sparse.html#sparse-csrlsvqr)converts the sparse input matrix to a dense matrix, then runs the dense factorization and linear solver on the result. This might result in slower-than-expected performance and significant memory usage for large matrices.

## Using the hipsolverRf API[#](#using-the-hipsolverrf-api)

The hipsolverRf API is intended as a 1:1 translation of the cusolverRf API, but not all functionality is equally supported in rocSOLVER. The following considerations apply when using this compatibility API.

### Unsupported methods[#](#id2)

Batched refactorization methods are currently unsupported with the rocSOLVER backend. They return a

`HIPSOLVER_STATUS_NOT_SUPPORTED`

status code.Parameter-setting methods are currently unsupported with the rocSOLVER backend. They return a

`HIPSOLVER_STATUS_NOT_SUPPORTED`

status code.

## Using the regular hipSOLVER API[#](#using-the-regular-hipsolver-api)

hipSOLVER’s regular API is similar to cuSOLVER. However, due to differences in the implementation and design between cuSOLVER and rocSOLVER, some minor adjustments were introduced to ensure the best performance out of both backends.

### Different signatures and additional API methods[#](#different-signatures-and-additional-api-methods)

The methods to obtain the size of the workspace needed by the

`gels`

and`gesv`

functions in cuSOLVER require`dwork`

as an argument. However, this argument is never used and can be null. On the rocSOLVER side,`dwork`

is not needed to calculate the workspace size. As a consequence,[hipsolverXXgels_bufferSize](../reference/api/lapack.html#gels-buffersize)and[hipsolverXXgesv_bufferSize](../reference/api/lapack.html#gesv-buffersize)do not require`dwork`

as an argument.Note

These wrappers pass

`dwork = nullptr`

when calling cuSOLVER.To calculate the workspace required by the function

`gesvd`

in rocSOLVER, the values of`jobu`

and`jobv`

are needed. As a result,[hipsolverXgesvd_bufferSize](../reference/api/lapack.html#gesvd-buffersize)requires`jobu`

and`jobv`

as arguments.Note

These arguments are ignored when the wrapper calls cuSOLVER because they are not needed.

To properly use a user-provided workspace, rocSOLVER requires both the allocated pointer and its size. Consequently,

[hipsolverXgetrf](../reference/api/lapack.html#getrf)requires`lwork`

as an argument.Note

`lwork`

is ignored when the wrapper calls cuSOLVER because it is not needed.All rocSOLVER functions called by hipSOLVER require a workspace. To allow the user to specify one,

[hipsolverXgetrs](../reference/api/lapack.html#getrs),[hipsolverXpotrfBatched](../reference/api/lapack.html#potrf-batched),[hipsolverXpotrs](../reference/api/lapack.html#potrs), and[hipsolverXpotrsBatched](../reference/api/lapack.html#potrs-batched)require`work`

and`lwork`

as arguments.Note

These arguments are ignored when these wrappers call cuSOLVER because they are not needed.

To support these changes, the regular API adds the following functions:

Note

These methods return

`lwork = 0`

when using the cuSOLVER backend, because the corresponding functions in cuSOLVER do not need a workspace.

### Arguments not referenced by rocSOLVER[#](#id3)

Unlike cuSOLVER, rocSOLVER functions do not provide information on invalid arguments in the

`info`

parameter, although they provide info on singularities and algorithm convergence. Therefore, when using the rocSOLVER backend,`info`

always returns a value >= 0. In cases where a rocSOLVER function does not accept`info`

as an argument, hipSOLVER sets it to zero.The

`niters`

argument for[hipsolverXXgels](../reference/api/lapack.html#gels)and[hipsolverXXgesv](../reference/api/lapack.html#gesv)is not referenced by the rocSOLVER backend. rocSOLVER does not implement any type of iterative refinement.

### Using the rocSOLVER memory model[#](#using-the-rocsolver-memory-model)

Most hipSOLVER functions take a workspace pointer and size as arguments, allowing the user to manage the device memory used
internally by the backends. rocSOLVER, however, can maintain the device workspace automatically by default
(see the [rocSOLVER memory model](https://rocm.docs.amd.com/projects/rocSOLVER/en/latest/howto/memory.html) for more details). To take
advantage of this feature, users can pass a null pointer for the `work`

argument or a zero size for the `lwork`

argument of any function
when using the rocSOLVER backend. The workspace will then be automatically managed behind-the-scenes. However, it’s best to use
a consistent workspace management strategy because performance issues might arise if the internal workspace is forced to frequently switch between
user-provided and automatically allocated workspaces.

Warning

This feature should not be used with the cuSOLVER backend. hipSOLVER does not guarantee a defined behavior when passing a null workspace to cuSOLVER functions that require one.

### Using the rocSOLVER in-place functions[#](#using-the-rocsolver-in-place-functions)

In cuSOLVER, the solvers `gesv`

and `gels`

are out-of-place in the sense that the solution vectors `X`

do not overwrite the input matrix `B`

.
In rocSOLVER, this is not the case. When `hipsolverXXgels`

or `hipsolverXXgesv`

call rocSOLVER, some data
movements must be done internally to restore `B`

and copy the results back to `X`

. These copies might introduce noticeable
overhead, depending on the size of the matrices. To avoid this potential problem, pass `X = B`

to `hipsolverXXgels`

or `hipsolverXXgesv`

when using the rocSOLVER backend. In this case, no data movements are required, and the solution
vectors can be retrieved using either `B`

or `X`

.

Warning

This feature should not be used with the cuSOLVER backend. hipSOLVER does not guarantee a defined behavior when passing
`X = B`

to these functions in cuSOLVER.
