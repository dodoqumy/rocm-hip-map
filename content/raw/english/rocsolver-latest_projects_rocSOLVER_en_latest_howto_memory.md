---
title: "rocSOLVER memory model &#8212; rocSOLVER 3.32.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocSOLVER/en/latest/howto/memory.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:11:13.316173+00:00
content_hash: "5e6a0517e9edf0d4"
---

# rocSOLVER memory model[#](#rocsolver-memory-model)

Almost all LAPACK and rocSOLVER routines require workspace memory to compute their results. In contrast to LAPACK, however, pointers to the workspace are not explicitly passed to the rocSOLVER functions as arguments. They are instead managed behind-the-scenes using a configurable device memory model.

rocSOLVER makes use of, and is integrated with, [the rocBLAS memory model](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/memory-alloc.html). Workspace memory
and the scheme used to manage it are tracked for each `rocblas_handle`

. The same functionality that is used to
manipulate the rocBLAS workspace memory also affects the rocSOLVER workspace memory.
For more information, see the rocBLAS [Device memory allocation](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/how-to/Programmers_Guide.html#device-memory-allocation-in-detail) documentation.

There are two schemes for device memory management:

Automatic (managed by rocSOLVER/rocBLAS): This is the default scheme. Device memory persists between function calls and is automatically reallocated if more memory is required by a function.

User-owned: The user manually allocates device memory and calls a rocBLAS helper function to use this memory as the workspace.


## Automatic workspace[#](#automatic-workspace)

By default, rocSOLVER automatically allocates device memory for the internal workspace
using the rocBLAS memory model and increases the amount of allocated memory to meet the needs of the rocSOLVER functions.
If this scheme is in use, the function `rocblas_is_managing_device_memory`

returns
`true`

. To re-enable this scheme if it’s not in use, pass a `nullptr`

or a size of `0`

to the
helper function `rocblas_set_workspace`

. For more details on these rocBLAS APIs,
see [Device Memory Allocation Functions in rocBLAS](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/memory-alloc.html).

This scheme has the disadvantage that automatic reallocation is synchronizing, but the user cannot control when this synchronization happens.

## User-owned workspace[#](#user-owned-workspace)

Alternatively, you have the option to manage the workspace memory manually using HIP.
This involves querying rocSOLVER to determine the minimum amount of memory required,
allocating the memory with `hipMalloc`

, and passing the resulting pointer to rocBLAS.

### Minimum required size[#](#minimum-required-size)

To choose an appropriate amount of memory to allocate, query rocSOLVER to determine
the minimum amount of memory required for the functions to complete.
Start the query by calling `rocblas_start_device_memory_size_query`

, then call the desired functions with appropriate problem sizes (a null pointer
can be passed to the device pointer arguments). A final call to `rocblas_stop_device_memory_size_query`

returns the minimum required size.

For example, the following code snippet returns the memory size required to solve a 1024*1024 linear system with one right-hand side (involving calls to `getrf`

and `getrs`

):

```
size_t memory_size;
rocblas_start_device_memory_size_query(handle);
rocsolver_dgetrf(handle, 1024, 1024, nullptr, lda, nullptr, nullptr);
rocsolver_dgetrs(handle, rocblas_operation_none, 1024, 1, nullptr, lda, nullptr, nullptr, ldb);
rocblas_stop_device_memory_size_query(handle, &memory_size);
```

For more details on the rocBLAS APIs, see [Device Memory Allocation Functions in rocBLAS](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/memory-alloc.html).

### Setting the workspace[#](#setting-the-workspace)

Call the function `rocblas_set_workspace`

and pass a pointer to device memory to rocBLAS for it to use as the rocSOLVER workspace. For example:

```
void* device_memory;
hipMalloc(&device_memory, memory_size);
rocblas_set_workspace(handle, device_memory, memory_size);
// perform computations here
rocblas_set_workspace(handle, nullptr, 0);
hipFree(device_memory);
```

For more details on the rocBLAS APIs, see [Device Memory Allocation Functions in rocBLAS](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/memory-alloc.html).
