---
title: "HIP API 7.0 changes &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/hip-7-changes.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:06:41.584253+00:00
content_hash: "6a49f5da850bfc55"
---

# HIP API 7.0 changes[#](#hip-api-7-0-changes)

To improve code portability between AMD and NVIDIA GPU programming models, changes were made to the HIP API in ROCm 7.0 to simplify cross-platform programming. These changes align HIP C++ even more closely with NVIDIA CUDA. These changes are incompatible with prior releases, and might require recompiling existing HIP applications for use with ROCm 7.0, or editing and recompiling code in some cases. In the best case, the change requires no modification of existing applications. These changes were made available in a preview release based on ROCm 6.4.1 to help you prepare.

## Behavior changes in HIP Runtime API[#](#behavior-changes-in-hip-runtime-api)

### Update `hipGetLastError`

[#](#update-hipgetlasterror)

Prior to the 7.0 release of the HIP API, [ hipGetLastError()](reference/hip_runtime_api/modules/error_handling.html#_CPPv415hipGetLastErrorv) was not fully compliant with CUDA’s behavior. The purpose of this change is to have

`hipGetLastError`

return the last actual error caught in the current thread during the application execution. Neither `hipSuccess`

nor `hipErrorNotReady`

is considered an error. Take the following code as an example:```
1: hipError_t err = hipMalloc(...); // returns hipOutOfMemory
2: err = hipSetDevice(0); // returns hipSuccess
3: err = hipGetLastError();
```

The prior behavior was for `hipGetLastError`

at line 3 to return `hipSuccess`

from line 2. In the 7.0 release, the value of `err`

at line 3 is `hipOutOfMemory`

which is the error returned in Line 1, rather than simply the result returned in line 2. This matches CUDA behavior.

You can still use the prior functionality by using the `hipExtGetLastError`

function. Notice that the function begins with `hipExt`

which denotes a function call that is unique to HIP, without correlation to CUDA. This function was introduced with the 6.0 release.

### Cooperative groups changes[#](#cooperative-groups-changes)

For [ hipLaunchCooperativeKernelMultiDevice()](reference/hip_runtime_api/modules/cooperative_groups_reference.html#_CPPv437hipLaunchCooperativeKernelMultiDeviceP15hipLaunchParamsij) function, HIP now includes additional input parameter validation checks.

If the input launch stream is a NULLPTR or it is

`hipStreamLegacy`

, the function now returns`hipErrorInvalidResourceHandle`

.If the stream capturing is active, the function returns the error code

`hipErrorStreamCaptureUnsupported`

.If the stream capture status is invalidated, the function returns the error

`hipErrorStreamCaptureInvalidated`

.

The [ hipLaunchCooperativeKernel()](reference/hip_runtime_api/modules/cooperative_groups_reference.html#_CPPv426hipLaunchCooperativeKernelPKv4dim34dim3PPvj11hipStream_t) function now checks the input stream handle. If it’s invalid, the returned error is changed to

`hipErrorInvalidHandle`

from `hipErrorContextIsDestroyed`

.### Update `hipPointerGetAttributes`

[#](#update-hippointergetattributes)

[ hipPointerGetAttributes()](reference/hip_runtime_api/modules/memory_management.html#_CPPv423hipPointerGetAttributesP21hipPointerAttribute_tPKv) now matches the functionality of

`cudaPointerGetAttributes`

which changed in CUDA 11. If a NULL host or attribute pointer is passed as input parameter, `hipPointerGetAttributes`

now returns `hipSuccess`

instead of the error code `hipErrorInvalidValue`

.Any application which is expecting the API to return an error instead of success could be impacted and a code change may need to handle the error properly.

### Update `hipFree`

[#](#update-hipfree)

[ hipFree()](reference/hip_runtime_api/modules/memory_management.html#_CPPv47hipFreePv) previously had an implicit wait for synchronization purpose which is applicable for all memory allocations. This wait has been disabled in the HIP 7.0 runtime for allocations made with

`hipMallocAsync`

and `hipMallocFromPoolAsync`

to match the behavior of CUDA API `cudaFree`

### Update `hipFreeAsync`

[#](#update-hipfreeasync)

The API returns `hipSuccess`

when the input pointer is NULL, instead of `hipErrorInvalidValue`

, to be consistent with [ hipFree()](reference/hip_runtime_api/modules/memory_management.html#_CPPv47hipFreePv).

### Exceptions effect during kernel execution changes[#](#exceptions-effect-during-kernel-execution-changes)

Exceptions that occur during kernel execution will no longer abort the process, but will instead return an error, unless core dumping is enabled.

## HIP runtime compiler (hipRTC) changes[#](#hip-runtime-compiler-hiprtc-changes)

Runtime compilation for HIP is available through the `hipRTC`

library as described in [Programming for HIP runtime compiler (RTC)](how-to/hip_rtc.html#hip-runtime-compiler-how-to). The library grew organically within the main HIP runtime code. However, segregation of the `hipRTC`

code is now needed to ensure better compatibility and easier code portability.

### Removal of `hipRTC`

symbols from HIP Runtime Library[#](#removal-of-hiprtc-symbols-from-hip-runtime-library)

`hipRTC`

has been an independent library since the 6.0 release, but the `hipRTC`

symbols were still available in the HIP runtime library. Starting with the 7.0 release `hipRTC`

is no longer included in the HIP runtime, and any application using `hipRTC`

APIs should link explicitly with the `hipRTC`

library.

This change makes the usage of `hipRTC`

library on Linux the same as on Windows and matches the behavior of CUDA `nvRTC`

.

`hipRTC`

compilation[#](#hiprtc-compilation)

The device code compilation via `hipRTC`

now uses namespace `__hip_internal`

, instead of the standard headers `std`

, to avoid namespace collision. These changes are made in the HIP header files.

No code change is required in any application, but rebuilding is necessary.

### Removal of datatypes from `hipRTC`

[#](#removal-of-datatypes-from-hiprtc)

In `hipRTC`

, datatype definitions such as `int64_t`

, `uint64_t`

, `int32_t`

, and `uint32_t`

could result in conflicts in some applications, as they use their own definitions for these types. `nvRTC`

doesn’t define these datatypes either.
These datatypes are removed and replaced by HIP internal datatypes prefixed with `__hip`

, for example, `__hip_int64_t`

.

Any application relying on HIP internal datatypes during `hipRTC`

compilation might be affected.
These changes have no impact on any application if it compiles as expected using `nvRTC`

.

## HIP header clean up[#](#hip-header-clean-up)

HIP header files previously included unnecessary Standard Template Libraries (STL) headers. With the 7.0 release, unnecessary STL headers are no longer included, and only the required STL headers are included.

Applications relying on HIP runtime header files might need to be updated to include STL header files that have been removed in 7.0.

## API signature and struct changes[#](#api-signature-and-struct-changes)

### API signature changes[#](#api-signature-changes)

Signatures in some APIs have been modified to match corresponding CUDA APIs, as described below.

The RTC method definition is changed in the following `hipRTC`

APIs:

In these APIs, the input parameter type changes from `const char**`

to `const char* const*`

.

In addition, the following APIs have signature changes:

, the type of the second argument pointer changes from`hipMemcpyHtoD()`

`const void*`

to`void*`

., the type of second argument is changed from`hipCtxGetApiVersion()`

`int*`

to`unsigned int*`

.

These signature changes do not require code modifications but do require rebuilding the application.

### Deprecated struct `HIP_MEMSET_NODE_PARAMS`

[#](#deprecated-struct-hip-memset-node-params)

The deprecated structure `HIP_MEMSET_NODE_PARAMS`

is removed.
You can use the definition `hipMemsetParams`

instead, as input parameter, while using these two APIs:

`hipMemsetParams`

struct change[#](#hipmemsetparams-struct-change)

The struct `hipMemsetParams`

is updated to be compatible with CUDA.
The change is from the old struct definition shown below:

```
typedef struct hipMemsetParams {
void* dst;
unsigned int elementSize;
size_t height;
size_t pitch;
unsigned int value;
size_t width;
} hipMemsetParams;
```

To the new struct definition as follows:

```
typedef struct hipMemsetParams {
void* dst;
size_t pitch;
unsigned int value;
unsigned int elementSize;
size_t width;
size_t height;
} hipMemsetParams;
```

No code change is required in any application using this structure, but rebuilding is necessary.

### HIP vector constructor change[#](#hip-vector-constructor-change)

Changes have been made to HIP vector constructors for `hipComplex`

initialization to generate values in alignment with CUDA. The affected constructors are small vector types such as `float2`

and `int4`

for example. If your code previously relied on a single value to initialize all components within a vector or complex type, you might need to update your code. Otherwise, rebuilding the application is necessary but no code change is required in any application using these constructors.

## Stream capture updates[#](#stream-capture-updates)

### Restrict stream capture modes[#](#restrict-stream-capture-modes)

Stream capture mode has been restricted in the following APIs to relaxed (`hipStreamCaptureModeRelaxed`

) mode:

These APIs are allowed only in relaxed stream capture mode. If the functions are used with stream capture, the HIP runtime the will return `hipErrorStreamCaptureUnsupported`

on unsupported stream capture modes.

### Check stream capture mode[#](#check-stream-capture-mode)

The following APIs will check the stream capture mode and return error codes to match the behavior of CUDA. No impact if stream capture is working correctly on CUDA. Otherwise, the application would need to modify the graph being captured.

- Returns error code while stream capture status is active. The usage is restricted during stream capture`hipLaunchCooperativeKernelMultiDevice()`

- Returns an error`hipEventQuery()`

`hipErrorStreamCaptureUnsupported`

in global capture mode- The stream capture behavior is updated. The function now checks if any of the blocking streams are capturing. If so, it returns an error and invalidates all capturing streams. The usage of this API is restricted during stream capture to match CUDA.`hipStreamAddCallback()`


### Stream capture error return[#](#stream-capture-error-return)

During stream capture, the following HIP APIs return the `hipErrorStreamCaptureUnsupported`

error on the HIP runtime, but not always `hipSuccess`

, to match behavior with CUDA.

The usage of these APIs is restricted during stream capture. No impact if stream capture is working fine on CUDA.

## Error code changes[#](#error-code-changes)

The following HIP APIs have been updated to return new or additional error codes to match the corresponding
CUDA APIs. Most existing applications just check if `hipSuccess`

is returned and no change is needed.
However, if an application checks for a specific error code, the application code may need to be updated
to match/handle the new error code accordingly.

## Invalid stream input parameter handling matches CUDA[#](#invalid-stream-input-parameter-handling-matches-cuda)

In order to match the CUDA runtime behavior more closely, HIP APIs with streams passed as input parameters no longer check the stream validity. Prior to the 7.0 release, the HIP runtime returns an error code `hipErrorContextIsDestroyed`

if the stream is invalid. In CUDA 12 and later, the equivalent behavior is to raise a segmentation fault. With HIP 7.0, the HIP runtime matches CUDA by causing a segmentation fault. The list of APIs impacted by this change are as follows:

Stream management related APIs

Graph management related APIs

Memory management related APIs

Event management related APIs


Developers porting CUDA code to HIP no longer need to modify their error handling code. However,
if you have come to expect the HIP runtime to return the error code `hipErrorContextIsDestroyed`

,
you might need to adjust your code.

## warpSize Change[#](#warpsize-change)

To match the CUDA specification, `warpSize`

is no longer a `constexpr`

.
In general, this should be a transparent change. However, if an application was using `warpSize`

as a compile-time constant, it will have to be updated to handle the new definition.
For more information, see [warpSize](./how-to/hip_cpp_language_extensions.html#warpsize)
in [HIP C++ language extensions](how-to/hip_cpp_language_extensions.html).
