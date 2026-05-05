---
title: "Device memory allocation in rocBLAS &#8212; rocBLAS 5.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/memory-alloc.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:05:19.515134+00:00
content_hash: "ae88baa5c57af9fc"
---

# Device memory allocation in rocBLAS[#](#device-memory-allocation-in-rocblas)

For temporary device memory, rocBLAS uses a per-handle memory allocation with out-of-band management. For more information, see the device memory allocation section of the :ref:programmers-guide.

The following computational functions use temporary device memory.

Function |
Use of temporary device memory |
|---|---|
L1 reduction functions
|
Reduction array |
L2 functions
|
Result array before overwriting input Column reductions of skinny transposed matrices
applicable for |
L3 GEMM-based functions
|
Block of matrix |

## Environment variable for preallocating memory[#](#environment-variable-for-preallocating-memory)

The environment variable `ROCBLAS_DEVICE_MEMORY_SIZE`

is used to set how much memory to preallocate:

If it is greater than 0, it sets the default handle device memory size to the specified size (in bytes).

If it is equal to 0 or unset, it lets rocBLAS manage the device memory. It uses a default size, like 32MiB or 128MiB, and expands it when necessary.


## Memory allocation functions[#](#memory-allocation-functions)

rocBLAS includes functions for manually setting the memory size and determining the memory requirements.

### Functions for manually setting the memory size[#](#functions-for-manually-setting-the-memory-size)

`rocblas_set_device_memory_size`

`rocblas_get_device_memory_size`

`rocblas_is_user_managing_device_memory`


### Function for setting a user-owned workspace[#](#function-for-setting-a-user-owned-workspace)

`rocblas_set_workspace`


### Functions for determining memory requirements[#](#functions-for-determining-memory-requirements)

`rocblas_start_device_memory_size_query`

`rocblas_stop_device_memory_size_query`

`rocblas_is_managing_device_memory`


See the API section for information about these functions.

## rocBLAS function return values for insufficient device memory[#](#rocblas-function-return-values-for-insufficient-device-memory)

If the user preallocates or manually allocates, that size is used as the limit and no resizing or synchronizing ever occurs. The following two function return values indicate insufficient memory:

`rocblas_status == rocblas_status_memory_error`

: indicates there is insufficient device memory for a rocBLAS function.`rocblas_status == rocblas_status_perf_degraded`

: indicates that a slower algorithm was used because of insufficient device memory for the optimal algorithm.

## Stream-ordered memory allocation[#](#stream-ordered-memory-allocation)

Stream-ordered device memory allocation is added to rocBLAS. The asynchronous allocators
`hipMallocAsync()`

and `hipFreeAsync()`

are used to allow allocation and deallocation to happen in stream order.

This is a non-default beta option that can be enabled by setting the environment variable `ROCBLAS_STREAM_ORDER_ALLOC`

.

To check whether the device supports stream-order allocation, call `hipDeviceGetAttribute()`

with the
device attribute `hipDeviceAttributeMemoryPoolsSupported`

.

### Enabling stream-ordered memory allocation[#](#enabling-stream-ordered-memory-allocation)

On supported platforms, the environment variable `ROCBLAS_STREAM_ORDER_ALLOC`

is used to enable stream-ordered memory allocation.

If it is greater than 0 (

`> 0`

), it sets the allocation to be stream-ordered and uses`hipMallocAsync/hipFreeAsync`

to manage device memory.If it is equal to zero (

`= 0`

) or unset, it uses`hipMalloc`

and`hipFree`

to manage device memory.

### Switching streams without synchronization[#](#switching-streams-without-synchronization)

Stream-order memory allocation lets the application switch streams without having to call `hipStreamSynchronize()`

.
