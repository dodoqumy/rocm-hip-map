---
title: "HIP error codes &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/reference/error_codes.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T06:59:08.176394+00:00
content_hash: "495e3a7e18dc7f6d"
---

::::::::::::::::::::::::::::::::::::::::::::
{#main-content .bd-main role="main"}

sbt-scroll-pixel-helper

::::::::::::::::::::::::::::::::::::::::::
bd-content
:::::::::::::::::::::::::::::::::::::
bd-article-container
:::::::
{.bd-header-article .d-print-none}
::::::
{.header-article-items .header-article__inner}
::
header-article-items__start

header-article-item
[]{.fa-solid .fa-angle-right}

header-article-item

::

::
header-article-items__end
:
header-article-item

article-header-buttons
[]{.fa-solid .fa-list}

:
::
::::::
:::::::

{#jb-print-docs-body .onlyprint}
# HIP error codes

::
{#print-main-content}
:
{#jb-print-toc}

{}
## Contents

:
::

{#searchbox}

:::::::::::::::::::::::
{#hip-error-codes .section}
[]{#id1}

# HIP error codes[\#](#hip-error-codes "Link to this heading"){.headerlink}

This page lists all HIP runtime error codes and their descriptions. These error codes are returned by HIP API functions to indicate various runtime conditions and errors.

For more details, see [[Error handling functions]{.std .std-ref}](hip_runtime_api/modules/error_handling.html#error-handling-reference){.reference .internal}.

:
{#basic-runtime-errors .section}
[]{#id2}

## Basic Runtime Errors[\#](#basic-runtime-errors "Link to this heading"){.headerlink}

pst-scrollable-table-container
+--------------------------------------------------------------------------------------------------+-------------------------------------------------+--------------------------------------------------------+
| Error Code                                                                                       | Value                                           | Description                                            |
+==================================================================================================+=================================================+========================================================+
| [[hipSuccess]{.xref .std .std-term}](#term-hipSuccess){.reference .internal}                     | [`0`{.docutils .literal .notranslate}]{.pre}    | No error                                               |
+--------------------------------------------------------------------------------------------------+-------------------------------------------------+--------------------------------------------------------+
| [[hipErrorUnknown]{.xref .std .std-term}](#term-hipErrorUnknown){.reference .internal}           | [`999`{.docutils .literal .notranslate}]{.pre}  | Unknown error                                          |
+--------------------------------------------------------------------------------------------------+-------------------------------------------------+--------------------------------------------------------+
| [[hipErrorNotReady]{.xref .std .std-term}](#term-hipErrorNotReady){.reference .internal}         | [`600`{.docutils .literal .notranslate}]{.pre}  | Device not ready                                       |
+--------------------------------------------------------------------------------------------------+-------------------------------------------------+--------------------------------------------------------+
| [[hipErrorIllegalState]{.xref .std .std-term}](#term-hipErrorIllegalState){.reference .internal} | [`401`{.docutils .literal .notranslate}]{.pre}  | The operation cannot be performed in the present state |
+--------------------------------------------------------------------------------------------------+-------------------------------------------------+--------------------------------------------------------+
| [[hipErrorNotSupported]{.xref .std .std-term}](#term-hipErrorNotSupported){.reference .internal} | [`801`{.docutils .literal .notranslate}]{.pre}  | Operation not supported                                |
+--------------------------------------------------------------------------------------------------+-------------------------------------------------+--------------------------------------------------------+
| [[hipErrorTbd]{.xref .std .std-term}](#term-hipErrorTbd){.reference .internal}                   | [`1054`{.docutils .literal .notranslate}]{.pre} | To be determined/implemented                           |
+--------------------------------------------------------------------------------------------------+-------------------------------------------------+--------------------------------------------------------+

hipSuccess[\#](#term-hipSuccess "Link to this term"){.headerlink}

:   No error. Operation completed successfully. This is returned when a HIP function completes without any errors and indicates normal execution.

hipErrorUnknown[\#](#term-hipErrorUnknown "Link to this term"){.headerlink}

:   Unknown error. This is a general error code returned when no other error code is applicable or when the specific error condition cannot be determined. This may indicate an unexpected internal error in the HIP runtime or driver.

hipErrorNotReady[\#](#term-hipErrorNotReady "Link to this term"){.headerlink}

:   Device not ready. This error occurs when asynchronous operations have not completed. Common scenarios include:

    - Attempting to access results of an asynchronous operation that is still in progress

    - Querying the status of a device that is still processing commands

    - Attempting to synchronize with an event that hasn't occurred yet

hipErrorIllegalState[\#](#term-hipErrorIllegalState "Link to this term"){.headerlink}

:   The operation cannot be performed in the present state. This error occurs when a valid operation is attempted at an inappropriate time or when the system is in a state that doesn't allow the requested action. Common scenarios include:

    - Attempting to modify resources that are in use by an active operation

    - Calling functions in an incorrect sequence

    - State machine violations in the HIP runtime

    - Attempting operations on a device that is in an error state

    - Trying to change configurations that can only be set during initialization

    - Calling APIs in the wrong order for multi-step operations

hipErrorNotSupported[\#](#term-hipErrorNotSupported "Link to this term"){.headerlink}

:   Operation not supported. This error indicates that the requested operation is not supported by the current hardware, driver, or HIP implementation.

hipErrorTbd[\#](#term-hipErrorTbd "Link to this term"){.headerlink}

:   To be determined/implemented. This is a placeholder error code for functionality that is planned but not yet fully implemented. It indicates that:

    - The feature or API may be documented but not fully functional

    - The error handling for a particular edge case is not yet defined

    - The functionality is under development and will be available in future releases

    If this error is encountered, it generally means the API or feature is not fully supported in the current version.
:

:
{#memory-management-errors .section}
[]{#id3}

## Memory Management Errors[\#](#memory-management-errors "Link to this heading"){.headerlink}

pst-scrollable-table-container
+--------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Error Code                                                                                                                     | Value                                           | Description                                                                                       |
+================================================================================================================================+=================================================+===================================================================================================+
| [[hipErrorOutOfMemory]{.xref .std .std-term}](#term-hipErrorOutOfMemory){.reference .internal}                                 | [`2`{.docutils .literal .notranslate}]{.pre}    | Out of memory                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+---------------------------------------------------------------------------------------------------+
| [[hipErrorInvalidDevicePointer]{.xref .std .std-term}](#term-hipErrorInvalidDevicePointer){.reference .internal}               | [`17`{.docutils .literal .notranslate}]{.pre}   | Invalid device pointer                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+---------------------------------------------------------------------------------------------------+
| [[hipErrorHostMemoryAlreadyRegistered]{.xref .std .std-term}](#term-hipErrorHostMemoryAlreadyRegistered){.reference .internal} | [`712`{.docutils .literal .notranslate}]{.pre}  | Part or all of the requested memory range is already mapped                                       |
+--------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+---------------------------------------------------------------------------------------------------+
| [[hipErrorHostMemoryNotRegistered]{.xref .std .std-term}](#term-hipErrorHostMemoryNotRegistered){.reference .internal}         | [`713`{.docutils .literal .notranslate}]{.pre}  | Pointer does not correspond to a registered memory region                                         |
+--------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+---------------------------------------------------------------------------------------------------+
| [[hipErrorInvalidMemcpyDirection]{.xref .std .std-term}](#term-hipErrorInvalidMemcpyDirection){.reference .internal}           | [`21`{.docutils .literal .notranslate}]{.pre}   | Invalid copy direction for memcpy                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+---------------------------------------------------------------------------------------------------+
| [[hipErrorIllegalAddress]{.xref .std .std-term}](#term-hipErrorIllegalAddress){.reference .internal}                           | [`700`{.docutils .literal .notranslate}]{.pre}  | An illegal memory access was encountered                                                          |
+--------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+---------------------------------------------------------------------------------------------------+
| [[hipErrorRuntimeMemory]{.xref .std .std-term}](#term-hipErrorRuntimeMemory){.reference .internal}                             | [`1052`{.docutils .literal .notranslate}]{.pre} | Runtime memory call returned error                                                                |
+--------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+---------------------------------------------------------------------------------------------------+
| [[hipErrorInvalidChannelDescriptor]{.xref .std .std-term}](#term-hipErrorInvalidChannelDescriptor){.reference .internal}       | [`911`{.docutils .literal .notranslate}]{.pre}  | Input for texture object, resource descriptor, or texture descriptor is a NULL pointer or invalid |
+--------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+---------------------------------------------------------------------------------------------------+
| [[hipErrorInvalidTexture]{.xref .std .std-term}](#term-hipErrorInvalidTexture){.reference .internal}                           | [`912`{.docutils .literal .notranslate}]{.pre}  | Texture reference pointer is NULL or invalid                                                      |
+--------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+---------------------------------------------------------------------------------------------------+

hipErrorOutOfMemory[\#](#term-hipErrorOutOfMemory "Link to this term"){.headerlink}

:   Out of memory. This error occurs when the HIP runtime cannot allocate enough memory to perform the requested operation. Common scenarios include:

    - Device memory exhaustion during [[`hipMalloc()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management.html#_CPPv49hipMallocPPv6size_t "hipMalloc"){.reference .internal} or similar allocation functions

    - Allocating more memory than is available on the device

    - Fragmentation of device memory preventing allocation of a contiguous block

    - Multiple concurrent allocations exceeding available memory

hipErrorInvalidDevicePointer[\#](#term-hipErrorInvalidDevicePointer "Link to this term"){.headerlink}

:   Invalid device pointer. This error occurs when:

    - Using a host pointer where a device pointer is expected

    - Using an unallocated device pointer

    - Using a device pointer that has been freed

    - Using a device pointer from a different context

hipErrorHostMemoryAlreadyRegistered[\#](#term-hipErrorHostMemoryAlreadyRegistered "Link to this term"){.headerlink}

:   Part or all of the requested memory range is already mapped. This error occurs when attempting to register host memory that has already been registered. Common scenarios include:

    - Calling [[`hipHostRegister()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management.html#_CPPv415hipHostRegisterPv6size_tj "hipHostRegister"){.reference .internal} on a memory region that was previously registered

    - Overlapping memory ranges where part of the new range is already registered

    - Multiple registration attempts of the same pointer in different parts of the application

    - Attempting to register memory that was allocated with [[`hipHostMalloc()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management.html#_CPPv413hipHostMallocPPv6size_tj "hipHostMalloc"){.reference .internal} (which is already registered)

    This error is distinct from general allocation errors as it specifically deals with the page-locking/registration of host memory for faster GPU access.

hipErrorHostMemoryNotRegistered[\#](#term-hipErrorHostMemoryNotRegistered "Link to this term"){.headerlink}

:   Pointer does not correspond to a registered memory region. This error occurs when operations that require registered host memory are performed on unregistered memory. Common scenarios include:

    - Calling [[`hipHostUnregister()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management.html#_CPPv417hipHostUnregisterPv "hipHostUnregister"){.reference .internal} on a pointer that was not previously registered

    - Using [[`hipHostGetDevicePointer()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management.html#_CPPv423hipHostGetDevicePointerPPvPvj "hipHostGetDevicePointer"){.reference .internal} on an unregistered host pointer

    - Attempting to use [[`hipHostGetFlags()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management.html#_CPPv415hipHostGetFlagsPjPv "hipHostGetFlags"){.reference .internal} on an unregistered pointer

    - Expecting zero-copy behavior with memory that hasn't been properly registered

    This error is the complement to [`hipErrorHostMemoryAlreadyRegistered`{.docutils .literal .notranslate}]{.pre} and indicates that an operation expected registered memory but received a standard host allocation.

hipErrorInvalidMemcpyDirection[\#](#term-hipErrorInvalidMemcpyDirection "Link to this term"){.headerlink}

:   Invalid copy direction for memcpy. This error occurs when an invalid direction parameter is specified for memory copy operations. Valid directions include:

    - [`hipMemcpyHostToHost`{.docutils .literal .notranslate}]{.pre}

    - [`hipMemcpyHostToDevice`{.docutils .literal .notranslate}]{.pre}

    - [`hipMemcpyDeviceToHost`{.docutils .literal .notranslate}]{.pre}

    - [`hipMemcpyDeviceToDevice`{.docutils .literal .notranslate}]{.pre}

    - [`hipMemcpyDefault`{.docutils .literal .notranslate}]{.pre}

    The error typically occurs when:

    - Using an undefined direction value

    - Using [`hipMemcpyDeviceToDevice`{.docutils .literal .notranslate}]{.pre} when copying between incompatible devices

    - Using a direction that doesn't match the actual source and destination pointer types

hipErrorIllegalAddress[\#](#term-hipErrorIllegalAddress "Link to this term"){.headerlink}

:   An illegal memory access was encountered. This error indicates that a memory access violation occurred during kernel execution. Common causes include:

    - Dereferencing a null pointer in device code

    - Out-of-bounds access to an array or buffer

    - Using an unallocated memory address

    - Accessing memory after it has been freed

    - Misaligned memory access for types requiring specific alignment

    - Writing to read-only memory

    - Race conditions in multi-threaded kernels

    This error typically terminates the kernel execution and may provide additional debugging information when running with GPU debugging tools enabled.

hipErrorRuntimeMemory[\#](#term-hipErrorRuntimeMemory "Link to this term"){.headerlink}

:   Runtime memory call returned error. This is a general error indicating that a memory management operation within the HIP runtime has failed. Common scenarios include:

    - Internal memory allocation failures within the HIP runtime

    - Memory corruption affecting the runtime's internal data structures

    - System-wide memory pressure affecting runtime operations

    - Resource limitations preventing memory operations

    - Driver-level memory management errors bubbling up to the application

    This error differs from [`hipErrorOutOfMemory`{.docutils .literal .notranslate}]{.pre} in that it relates to memory operations internal to the HIP runtime rather than explicit application requests for memory allocation.

hipErrorInvalidChannelDescriptor[\#](#term-hipErrorInvalidChannelDescriptor "Link to this term"){.headerlink}

:   This error indicates that an invalid channel descriptor is used to define the format and layout of data in memory, particularly when working with textures or arrays. This could happen if the descriptor is incorrectly set up or if it does not match the expected format for the operation being performed.

hipErrorInvalidTexture[\#](#term-hipErrorInvalidTexture "Link to this term"){.headerlink}

:   The error code is returned when an invalid texture object is used in a function call. This typically occurs when a texture object is not properly initialized or configured before being used in operations that require valid texture data. If you encounter this error, it suggests that the texture object might be missing necessary configuration details or has been corrupted.
:

:
{#device-and-context-errors .section}
[]{#device-context-errors}

## Device and Context Errors[\#](#device-and-context-errors "Link to this heading"){.headerlink}

pst-scrollable-table-container
+--------------------------------------------------------------------------------------------------------------------+------------------------------------------------+--------------------------------------------------------------+
| Error Code                                                                                                         | Value                                          | Description                                                  |
+====================================================================================================================+================================================+==============================================================+
| [[hipErrorNoDevice]{.xref .std .std-term}](#term-hipErrorNoDevice){.reference .internal}                           | [`100`{.docutils .literal .notranslate}]{.pre} | No ROCm-capable device is detected                           |
+--------------------------------------------------------------------------------------------------------------------+------------------------------------------------+--------------------------------------------------------------+
| [[hipErrorInvalidDevice]{.xref .std .std-term}](#term-hipErrorInvalidDevice){.reference .internal}                 | [`101`{.docutils .literal .notranslate}]{.pre} | Invalid device ordinal                                       |
+--------------------------------------------------------------------------------------------------------------------+------------------------------------------------+--------------------------------------------------------------+
| [[hipErrorInvalidContext]{.xref .std .std-term}](#term-hipErrorInvalidContext){.reference .internal}               | [`201`{.docutils .literal .notranslate}]{.pre} | Invalid device context                                       |
+--------------------------------------------------------------------------------------------------------------------+------------------------------------------------+--------------------------------------------------------------+
| [[hipErrorContextAlreadyCurrent]{.xref .std .std-term}](#term-hipErrorContextAlreadyCurrent){.reference .internal} | [`202`{.docutils .literal .notranslate}]{.pre} | Context is already current context                           |
+--------------------------------------------------------------------------------------------------------------------+------------------------------------------------+--------------------------------------------------------------+
| [[hipErrorContextAlreadyInUse]{.xref .std .std-term}](#term-hipErrorContextAlreadyInUse){.reference .internal}     | [`216`{.docutils .literal .notranslate}]{.pre} | Exclusive-thread device already in use by a different thread |
+--------------------------------------------------------------------------------------------------------------------+------------------------------------------------+--------------------------------------------------------------+
| [[hipErrorContextIsDestroyed]{.xref .std .std-term}](#term-0){.reference .internal}                                | [`709`{.docutils .literal .notranslate}]{.pre} | Context is destroyed                                         |
+--------------------------------------------------------------------------------------------------------------------+------------------------------------------------+--------------------------------------------------------------+
| [[hipErrorInvalidHandle]{.xref .std .std-term}](#term-hipErrorInvalidHandle){.reference .internal}                 | [`400`{.docutils .literal .notranslate}]{.pre} | Invalid resource handle                                      |
+--------------------------------------------------------------------------------------------------------------------+------------------------------------------------+--------------------------------------------------------------+
| [[hipErrorSetOnActiveProcess]{.xref .std .std-term}](#term-hipErrorSetOnActiveProcess){.reference .internal}       | [`708`{.docutils .literal .notranslate}]{.pre} | Cannot set while device is active in this process            |
+--------------------------------------------------------------------------------------------------------------------+------------------------------------------------+--------------------------------------------------------------+
| [[hipErrorDeinitialized]{.xref .std .std-term}](#term-hipErrorDeinitialized){.reference .internal}                 | [`4`{.docutils .literal .notranslate}]{.pre}   | Driver shutting down                                         |
+--------------------------------------------------------------------------------------------------------------------+------------------------------------------------+--------------------------------------------------------------+
| [[hipErrorNotInitialized]{.xref .std .std-term}](#term-hipErrorNotInitialized){.reference .internal}               | [`3`{.docutils .literal .notranslate}]{.pre}   | Initialization error                                         |
+--------------------------------------------------------------------------------------------------------------------+------------------------------------------------+--------------------------------------------------------------+
| [[hipErrorInsufficientDriver]{.xref .std .std-term}](#term-hipErrorInsufficientDriver){.reference .internal}       | [`35`{.docutils .literal .notranslate}]{.pre}  | Driver version is insufficient for runtime version           |
+--------------------------------------------------------------------------------------------------------------------+------------------------------------------------+--------------------------------------------------------------+

hipErrorNoDevice[\#](#term-hipErrorNoDevice "Link to this term"){.headerlink}

:   No ROCm-capable device is detected. This error occurs when the system does not have any compatible GPU devices that support the HIP runtime. Common scenarios include:

    - No physical GPU is installed in the system

    - Installed GPUs are not supported by the current HIP/ROCm version

    - GPU drivers are missing, outdated, or corrupted

    - GPU hardware failure or disconnection

    - System configuration prevents GPU detection (e.g., BIOS settings, virtualization limitations)

    - On Linux with [`HIP_PLATFORM=amd`{.docutils .literal .notranslate}]{.pre}, insufficient user permissions - the user must belong to both the [`render`{.docutils .literal .notranslate}]{.pre} and [`video`{.docutils .literal .notranslate}]{.pre} groups

hipErrorInvalidDevice[\#](#term-hipErrorInvalidDevice "Link to this term"){.headerlink}

:   Invalid device ordinal. This error occurs when a function is called with a device index that doesn't correspond to a valid device. Common scenarios include:

    - Using a device index greater than or equal to the number of available devices

    - Using a negative device index

    - Using a device that has been removed or disabled

    - Attempting to access a device after system configuration changes

    Unlike [`hipErrorNoDevice`{.docutils .literal .notranslate}]{.pre} which indicates no devices are available at all, this error occurs when trying to access a specific invalid device index while other valid devices might still be present.

hipErrorInvalidContext[\#](#term-hipErrorInvalidContext "Link to this term"){.headerlink}

:   Invalid device context. This error occurs when an operation is attempted with an invalid or destroyed context. Common scenarios include:

    - Using a context after calling [[`hipCtxDestroy()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/context_management.html#_CPPv413hipCtxDestroy8hipCtx_t "hipCtxDestroy"){.reference .internal} on it

    - Context corruption due to previous errors

    - Using a context associated with a device that has been reset

    - Mixing contexts improperly between different HIP API calls

    - Context handle that was never properly created or initialized

    - Using a context from a different process or thread incorrectly

    Context errors often indicate improper resource management in the application or incorrect context handling in multi-GPU or multi-threaded applications.

hipErrorContextAlreadyCurrent[\#](#term-hipErrorContextAlreadyCurrent "Link to this term"){.headerlink}

:   Context is already current context. This error occurs when attempting to make a context current when it is already the current context for the calling thread.

hipErrorContextAlreadyInUse[\#](#term-hipErrorContextAlreadyInUse "Link to this term"){.headerlink}

:   Exclusive-thread device already in use by a different thread. This error occurs when attempting to access a device or context that has been allocated in exclusive thread mode from a thread other than the one that created it.

hipErrorContextIsDestroyed[\#](#term-hipErrorContextIsDestroyed "Link to this term"){.headerlink}

:   Context is destroyed. This error occurs when attempting to use a context that has been previously destroyed.

hipErrorInvalidHandle[\#](#term-hipErrorInvalidHandle "Link to this term"){.headerlink}

:   Invalid resource handle. This error occurs when an invalid handle is provided to a HIP API function. Common scenarios include using handles that have been destroyed or were never properly initialized.

hipErrorSetOnActiveProcess[\#](#term-hipErrorSetOnActiveProcess "Link to this term"){.headerlink}

:   Cannot set while device is active in this process. This error occurs when attempting to change settings that cannot be modified while the device is active.

hipErrorDeinitialized[\#](#term-hipErrorDeinitialized "Link to this term"){.headerlink}

:   Driver shutting down. This error occurs when attempting to use HIP functionality when the driver is in the process of shutting down or has been deinitialized. Common scenarios include:

    - Using HIP functions after calling [[`hipDeviceReset()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/device_management.html#_CPPv414hipDeviceResetv "hipDeviceReset"){.reference .internal}

    - System is in the process of shutdown or reboot

    - Driver crash or unexpected termination

    - Another process has triggered driver reset

hipErrorNotInitialized[\#](#term-hipErrorNotInitialized "Link to this term"){.headerlink}

:   Initialization error. This occurs when attempting to use HIP functionality before the runtime has been properly initialized. Common scenarios include:

    - Calling HIP API functions before calling [[`hipInit()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/initialization_and_version.html#_CPPv47hipInitj "hipInit"){.reference .internal}

    - Driver or runtime initialization failure

    - System configuration issues preventing proper initialization of the HIP runtime

    - Hardware initialization problems

hipErrorInsufficientDriver[\#](#term-hipErrorInsufficientDriver "Link to this term"){.headerlink}

:   Driver version is insufficient for runtime version. This error occurs when the installed GPU driver is too old to support the current HIP runtime version. This version mismatch can cause compatibility issues. Common scenarios include:

    - Using a newer HIP SDK with older driver installations

    - System updates that upgraded the HIP runtime but not the GPU drivers

    - Custom build environments with mismatched components

    - Partial upgrades of the ROCm stack
:

:
{#kernel-and-launch-errors .section}
[]{#kernel-launch-errors}

## Kernel and Launch Errors[\#](#kernel-and-launch-errors "Link to this heading"){.headerlink}

pst-scrollable-table-container
+----------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+---------------------------------------------------------------------------------------+
| Error Code                                                                                                                 | Value                                          | Description                                                                           |
+============================================================================================================================+================================================+=======================================================================================+
| [[hipErrorInvalidValue]{.xref .std .std-term}](#term-hipErrorInvalidValue){.reference .internal}                           | [`1`{.docutils .literal .notranslate}]{.pre}   | Invalid input value                                                                   |
+----------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+---------------------------------------------------------------------------------------+
| [[hipErrorInvalidDeviceFunction]{.xref .std .std-term}](#term-hipErrorInvalidDeviceFunction){.reference .internal}         | [`98`{.docutils .literal .notranslate}]{.pre}  | Invalid device function                                                               |
+----------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+---------------------------------------------------------------------------------------+
| [[hipErrorContextIsDestroyed]{.xref .std .std-term}](#term-0){.reference .internal}                                        | [`709`{.docutils .literal .notranslate}]{.pre} | Invalid stream handle                                                                 |
+----------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+---------------------------------------------------------------------------------------+
| [[hipErrorInvalidConfiguration]{.xref .std .std-term}](#term-hipErrorInvalidConfiguration){.reference .internal}           | [`9`{.docutils .literal .notranslate}]{.pre}   | Invalid configuration argument                                                        |
+----------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+---------------------------------------------------------------------------------------+
| [[hipErrorInvalidSymbol]{.xref .std .std-term}](#term-hipErrorInvalidSymbol){.reference .internal}                         | [`13`{.docutils .literal .notranslate}]{.pre}  | Invalid device symbol                                                                 |
+----------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+---------------------------------------------------------------------------------------+
| [[hipErrorMissingConfiguration]{.xref .std .std-term}](#term-hipErrorMissingConfiguration){.reference .internal}           | [`52`{.docutils .literal .notranslate}]{.pre}  | [`__global__`{.docutils .literal .notranslate}]{.pre} function call is not configured |
+----------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+---------------------------------------------------------------------------------------+
| [[hipErrorNoBinaryForGpu]{.xref .std .std-term}](#term-hipErrorNoBinaryForGpu){.reference .internal}                       | [`209`{.docutils .literal .notranslate}]{.pre} | No kernel image is available for execution on the device                              |
+----------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+---------------------------------------------------------------------------------------+
| [[hipErrorInvalidKernelFile]{.xref .std .std-term}](#term-hipErrorInvalidKernelFile){.reference .internal}                 | [`218`{.docutils .literal .notranslate}]{.pre} | Invalid kernel file                                                                   |
+----------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+---------------------------------------------------------------------------------------+
| [[hipErrorInvalidImage]{.xref .std .std-term}](#term-hipErrorInvalidImage){.reference .internal}                           | [`200`{.docutils .literal .notranslate}]{.pre} | Device kernel image is invalid                                                        |
+----------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+---------------------------------------------------------------------------------------+
| [[hipErrorLaunchFailure]{.xref .std .std-term}](#term-hipErrorLaunchFailure){.reference .internal}                         | [`719`{.docutils .literal .notranslate}]{.pre} | Unspecified launch failure                                                            |
+----------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+---------------------------------------------------------------------------------------+
| [[hipErrorLaunchTimeOut]{.xref .std .std-term}](#term-hipErrorLaunchTimeOut){.reference .internal}                         | [`702`{.docutils .literal .notranslate}]{.pre} | The launch timed out and was terminated                                               |
+----------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+---------------------------------------------------------------------------------------+
| [[hipErrorLaunchOutOfResources]{.xref .std .std-term}](#term-hipErrorLaunchOutOfResources){.reference .internal}           | [`701`{.docutils .literal .notranslate}]{.pre} | Too many resources requested for launch                                               |
+----------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+---------------------------------------------------------------------------------------+
| [[hipErrorCooperativeLaunchTooLarge]{.xref .std .std-term}](#term-hipErrorCooperativeLaunchTooLarge){.reference .internal} | [`720`{.docutils .literal .notranslate}]{.pre} | Too many blocks in cooperative launch                                                 |
+----------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+---------------------------------------------------------------------------------------+
| [[hipErrorPriorLaunchFailure]{.xref .std .std-term}](#term-hipErrorPriorLaunchFailure){.reference .internal}               | [`53`{.docutils .literal .notranslate}]{.pre}  | Unspecified launch failure in prior launch                                            |
+----------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+---------------------------------------------------------------------------------------+

hipErrorInvalidValue[\#](#term-hipErrorInvalidValue "Link to this term"){.headerlink}

:   Error returned when a grid dimension check finds any input global work size dimension is zero, or a shared memory size check finds the size exceeds the size limit.

hipErrorInvalidDeviceFunction[\#](#term-hipErrorInvalidDeviceFunction "Link to this term"){.headerlink}

:   Invalid device function. This error occurs when attempting to use a function that is not a valid device function or is not available for the current device. Common scenarios include:

    - Code compiled for a specific GPU architecture (using [`--offload-arch`{.docutils .literal .notranslate}]{.pre}) but executed on an different/incompatible GPU

hipErrorContextIsDestroyed[\#](#term-0 "Link to this term"){.headerlink}

:   This error is returned when the input stream or input stream handle is invalid.

hipErrorInvalidConfiguration[\#](#term-hipErrorInvalidConfiguration "Link to this term"){.headerlink}

:   Invalid configuration argument. This error occurs when the configuration specified for a kernel launch or other configurable operation contains invalid parameters. Common scenarios include:

    - Block dimensions exceeding hardware limits (too many threads per block)

    - Grid dimensions that are invalid (zero size or exceeding limits)

    - Invalid shared memory configuration

    - Incompatible combination of launch parameters

    - Block dimensions that don't match kernel requirements

    - Attempting to use more resources per block than available on the device

    This error typically requires adjusting kernel launch parameters to stay within the limits of the target device. Device properties and specific hardware constraints can be queried using [[`hipGetDeviceProperties()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/device_management.html#_CPPv422hipGetDevicePropertiesP15hipDeviceProp_ti "hipGetDeviceProperties"){.reference .internal}.

hipErrorInvalidSymbol[\#](#term-hipErrorInvalidSymbol "Link to this term"){.headerlink}

:   Invalid device symbol. This error occurs when a referenced symbol (variable or function) cannot be found or is improperly specified. Common scenarios include:

    - Referencing a symbol that doesn't exist in the compiled kernel

    - Symbol name typos or case mismatches

    - Attempting to access a host symbol as if it were a device symbol

    - Symbol not properly decorated with [`__device__`{.docutils .literal .notranslate}]{.pre} or other required attributes

    - Symbol not visible due to scope/namespace issues

hipErrorMissingConfiguration[\#](#term-hipErrorMissingConfiguration "Link to this term"){.headerlink}

:   [`__global__`{.docutils .literal .notranslate}]{.pre} function call is not configured. This error occurs when a kernel launch is attempted without proper configuration. Common scenarios include:

    - Calling a kernel without specifying execution configuration (grid and block dimensions)

    - Invalid or incomplete kernel configuration

    - Calling a [`__global__`{.docutils .literal .notranslate}]{.pre} function directly as if it were a regular CPU function

    - Using a function pointer to a [`__global__`{.docutils .literal .notranslate}]{.pre} function incorrectly

    This error is specific to improper kernel invocation syntax and is different from general configuration errors ([`hipErrorInvalidConfiguration`{.docutils .literal .notranslate}]{.pre}) which relate to the values provided in a properly formed launch configuration.

hipErrorNoBinaryForGpu[\#](#term-hipErrorNoBinaryForGpu "Link to this term"){.headerlink}

:   No kernel image is available for execution on the device. This error occurs when attempting to run a kernel on a device for which no compatible compiled binary exists. Common scenarios include:

    - Attempting to run code compiled for a different GPU architecture

    - Missing or corrupted kernel binary for the target device

    - Kernel was compiled without support for the target device architecture

    - Using pre-compiled kernels that don't support the installed hardware

    - JIT compilation failure during runtime

hipErrorInvalidKernelFile[\#](#term-hipErrorInvalidKernelFile "Link to this term"){.headerlink}

:   Invalid kernel file. This error occurs when the kernel file or module being loaded is corrupted or in an invalid format, for example the file name exists but the file size is 0.

hipErrorInvalidImage[\#](#term-hipErrorInvalidImage "Link to this term"){.headerlink}

:   Device kernel image is invalid. This error occurs when the device code image is corrupted or in an unsupported format.

hipErrorLaunchFailure[\#](#term-hipErrorLaunchFailure "Link to this term"){.headerlink}

:   Unspecified launch failure. This is a general error that occurs when a kernel launch fails. Common causes include:

    - Mismatch between block size configuration and block size specified in launch bounds parameter

    - Invalid memory access in kernel

    - Kernel execution timeout

    - Hardware-specific failures

hipErrorLaunchTimeOut[\#](#term-hipErrorLaunchTimeOut "Link to this term"){.headerlink}

:   The launch timed out and was terminated. This error occurs when a kernel execution exceeds the system's watchdog timeout limit. Common scenarios include:

    - Infinite loops in kernel code

    - Extremely long-running computations exceeding system limits

    - Deadlocks in kernel execution

    - Complex kernels that legitimately need more time than the watchdog allows

    - Hardware or driver issues preventing normal kernel termination

    The GPU's watchdog timer is a safety mechanism to prevent a hanging kernel from making the system unresponsive.

hipErrorLaunchOutOfResources[\#](#term-hipErrorLaunchOutOfResources "Link to this term"){.headerlink}

:   Too many resources requested for launch. This occurs when kernel resource requirements exceed device limits, such as:

    - Exceeding maximum threads per block

    - Exceeding maximum shared memory per block

    - Exceeding maximum register count per thread

    - Insufficient hardware resources for parallel execution

hipErrorCooperativeLaunchTooLarge[\#](#term-hipErrorCooperativeLaunchTooLarge "Link to this term"){.headerlink}

:   Too many blocks in cooperative launch. This error occurs when a cooperative kernel launch requests more thread blocks than the device can support for cooperative groups functionality. Common scenarios include:

    - Launching a cooperative kernel with grid dimensions that exceed hardware limits

    - Requesting more resources than available for synchronization across thread blocks

    - The shared memory size in bytes exceeds the device local memory size per CU

    - Using cooperative groups on hardware with limited support

    - Not accounting for cooperative launch limitations in kernel configuration

    Cooperative kernels allow thread blocks to synchronize with each other, but this requires special hardware support with specific limitations on the maximum number of blocks that can participate in synchronization operations.

hipErrorPriorLaunchFailure[\#](#term-hipErrorPriorLaunchFailure "Link to this term"){.headerlink}

:   Unspecified launch failure in prior launch. This error indicates that a previous kernel launch failed and affected the current HIP context state. Common scenarios include:

    - Launching a new kernel after a previous kernel crashed without resetting the device

    - Context contamination from previous failed operations

    - Resource leaks from previous launches affecting current operations

    - Attempting to use results from a previous failed kernel execution

    When this error occurs, it may be necessary to reset the device or create a new context to continue normal operation. Additional debugging of the previous failed launch may be required to identify the root cause.
:

:
{#stream-capture-errors .section}
[]{#id4}

## Stream Capture Errors[\#](#stream-capture-errors "Link to this heading"){.headerlink}

pst-scrollable-table-container
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| Error Code                                                                                                               | Value                                          | Description                                                                                                                             |
+==========================================================================================================================+================================================+=========================================================================================================================================+
| [[hipErrorStreamCaptureUnsupported]{.xref .std .std-term}](#term-hipErrorStreamCaptureUnsupported){.reference .internal} | [`900`{.docutils .literal .notranslate}]{.pre} | Operation not permitted when stream is capturing                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| [[hipErrorStreamCaptureInvalidated]{.xref .std .std-term}](#term-hipErrorStreamCaptureInvalidated){.reference .internal} | [`901`{.docutils .literal .notranslate}]{.pre} | Operation failed due to a previous error during capture                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| [[hipErrorStreamCaptureMerge]{.xref .std .std-term}](#term-hipErrorStreamCaptureMerge){.reference .internal}             | [`902`{.docutils .literal .notranslate}]{.pre} | Operation would result in a merge of separate capture sequences                                                                         |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| [[hipErrorStreamCaptureUnmatched]{.xref .std .std-term}](#term-hipErrorStreamCaptureUnmatched){.reference .internal}     | [`903`{.docutils .literal .notranslate}]{.pre} | Capture was not ended in the same stream as it began                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| [[hipErrorStreamCaptureUnjoined]{.xref .std .std-term}](#term-hipErrorStreamCaptureUnjoined){.reference .internal}       | [`904`{.docutils .literal .notranslate}]{.pre} | Capturing stream has unjoined work                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| [[hipErrorStreamCaptureIsolation]{.xref .std .std-term}](#term-hipErrorStreamCaptureIsolation){.reference .internal}     | [`905`{.docutils .literal .notranslate}]{.pre} | Dependency created on uncaptured work in another stream                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| [[hipErrorStreamCaptureImplicit]{.xref .std .std-term}](#term-hipErrorStreamCaptureImplicit){.reference .internal}       | [`906`{.docutils .literal .notranslate}]{.pre} | Operation would make the legacy stream depend on a capturing blocking stream                                                            |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| [[hipErrorStreamCaptureWrongThread]{.xref .std .std-term}](#term-hipErrorStreamCaptureWrongThread){.reference .internal} | [`908`{.docutils .literal .notranslate}]{.pre} | Attempt to terminate a thread-local capture sequence from another thread                                                                |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| [[hipErrorCapturedEvent]{.xref .std .std-term}](#term-hipErrorCapturedEvent){.reference .internal}                       | [`907`{.docutils .literal .notranslate}]{.pre} | Operation not permitted on an event last recorded in a capturing stream                                                                 |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| [[hipErrorInvalidResourceHandle]{.xref .std .std-term}](#term-hipErrorInvalidResourceHandle){.reference .internal}       | [`400`{.docutils .literal .notranslate}]{.pre} | Input launch stream is [`NULL`{.docutils .literal .notranslate}]{.pre} or is [`hipStreamLegacy`{.docutils .literal .notranslate}]{.pre} |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+

hipErrorStreamCaptureUnsupported[\#](#term-hipErrorStreamCaptureUnsupported "Link to this term"){.headerlink}

:   Operation not permitted when stream is capturing. This error occurs when attempting to perform an operation that is incompatible with stream capture mode. Common scenarios include:

    - Calling synchronization functions like [[`hipDeviceSynchronize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/device_management.html#_CPPv420hipDeviceSynchronizev "hipDeviceSynchronize"){.reference .internal} during capture

    - Using operations that implicitly synchronize during stream capture

    - Attempting to use features that cannot be captured as part of a graph

    - Trying to perform operations on different devices during capture

    - Using driver APIs that are incompatible with the stream capture mechanism

    Stream capture is used to record operations for later replay as a graph. Certain operations that affect global state or rely on host-device synchronization cannot be properly captured in this execution model.

hipErrorStreamCaptureInvalidated[\#](#term-hipErrorStreamCaptureInvalidated "Link to this term"){.headerlink}

:   Operation failed due to a previous error during capture. This error occurs when a stream capture has been invalidated by a prior error but capture operations are still being attempted. Common scenarios include:

    - Continuing to add operations to a stream after a capture-invalidating error

    - Not checking return codes from previous capture operations

    - Attempting to end a capture after invalidation

    - System or resource conditions changing during capture

    Once a stream capture has been invalidated, the entire capture sequence should be aborted and restarted from the beginning after resolving the cause of the initial failure.

hipErrorStreamCaptureMerge[\#](#term-hipErrorStreamCaptureMerge "Link to this term"){.headerlink}

:   Operation would result in a merge of separate capture sequences. This error occurs when an operation would cause independent capture sequences to merge, which is not supported. Common scenarios include:

    - A stream that is being captured interacting with another capturing stream

    - Operations creating implicit dependencies between separate capture sequences

    - Using events or other synchronization primitives that would link separate captures

    - Resource sharing between different capture sequences

    Stream captures must remain independent of each other to be converted into separate executable graphs. Operations that would create dependencies between separate captures are not allowed.

hipErrorStreamCaptureUnmatched[\#](#term-hipErrorStreamCaptureUnmatched "Link to this term"){.headerlink}

:   Capture was not ended in the same stream as it began. This error occurs when trying to end a stream capture in a different stream than the one where it was started. Common scenarios include:

    - Calling [[`hipStreamEndCapture()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/graph_management.html#_CPPv419hipStreamEndCapture11hipStream_tP10hipGraph_t "hipStreamEndCapture"){.reference .internal} on a different stream than [[`hipStreamBeginCapture()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/graph_management.html#_CPPv421hipStreamBeginCapture11hipStream_t20hipStreamCaptureMode "hipStreamBeginCapture"){.reference .internal}

    - Confusing stream handles in multi-stream applications

    - Not properly tracking which streams have active captures

    - Programming errors in capture sequence management

    Stream captures must begin and end in the same stream to maintain the integrity of the captured operation sequence. The same stream handle must be used for beginning and ending a capture sequence.

hipErrorStreamCaptureUnjoined[\#](#term-hipErrorStreamCaptureUnjoined "Link to this term"){.headerlink}

:   Capturing stream has unjoined work. This error occurs when attempting to end a stream capture when there are still pending operations from other streams that have not been joined back to the capturing stream. Common scenarios include:

    - Forgetting to properly join forked work before ending capture

    - Missing [[`hipEventRecord()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/event_management.html#_CPPv414hipEventRecord10hipEvent_t11hipStream_t "hipEventRecord"){.reference .internal} / [[`hipStreamWaitEvent()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/stream_management.html#_CPPv418hipStreamWaitEvent11hipStream_t10hipEvent_tj "hipStreamWaitEvent"){.reference .internal} pairs for joined streams

    - Complex stream dependencies that are not fully resolved at capture end

    - Attempting to end a capture before all child operations complete

    When a stream capture forks work to other streams, those operations must be explicitly joined back to the capturing stream before the capture can be ended. This ensures that all dependencies are properly represented in the resulting graph.

hipErrorStreamCaptureIsolation[\#](#term-hipErrorStreamCaptureIsolation "Link to this term"){.headerlink}

:   Dependency created on uncaptured work in another stream. This error occurs when a capturing stream becomes dependent on operations in a non-capturing stream. Common scenarios include:

    - A capturing stream waiting on an event recorded in a non-capturing stream

    - Creating dependencies on the default stream or other streams outside the capture

    - Using synchronization primitives that create implicit dependencies

    - Operations that depend on host-side or uncaptured GPU work

    Stream capture requires that all dependencies be explicitly captured as part of the graph. Operations that would make the captured sequence dependent on work outside the capture cannot be represented in the resulting graph and are therefore not allowed.

hipErrorStreamCaptureImplicit[\#](#term-hipErrorStreamCaptureImplicit "Link to this term"){.headerlink}

:   Operation would make the legacy stream depend on a capturing blocking stream. This error occurs when an operation would create a dependency from the default (legacy/null) stream to a stream that is being captured in blocking mode. Common scenarios include:

    - Using the default stream during capture in ways that would create dependencies

    - Operations that would cause implicit synchronization with the null stream

    - Mixing legacy stream synchronization behavior with stream capture

    - Not properly managing stream relationships in applications using both explicit streams and the default stream

    This error is related to the implicit synchronization behavior of the default stream in HIP, which can conflict with the explicit dependency tracking needed for stream capture.

hipErrorStreamCaptureWrongThread[\#](#term-hipErrorStreamCaptureWrongThread "Link to this term"){.headerlink}

:   Attempt to terminate a thread-local capture sequence from another thread. This error occurs when a thread tries to end a stream capture that was begun by a different thread when using thread-local capture mode. Common scenarios include:

    - Multi-threaded applications incorrectly managing stream capture

    - Attempting to end a capture from a different thread than the one that started it

    - Thread pool or worker thread designs that don't properly track capture ownership

    - Misunderstanding the thread locality requirements of certain capture modes

    When using [`hipStreamCaptureModeThreadLocal`{.docutils .literal .notranslate}]{.pre}, stream captures are associated with the specific thread that started them and can only be ended by that same thread.

hipErrorCapturedEvent[\#](#term-hipErrorCapturedEvent "Link to this term"){.headerlink}

:   Operation not permitted on an event last recorded in a capturing stream. This error occurs when attempting to perform operations on an event that was last recorded in a stream that is being captured. Common scenarios include:

    - Calling [[`hipEventQuery()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/event_management.html#_CPPv413hipEventQuery10hipEvent_t "hipEventQuery"){.reference .internal} or [[`hipEventSynchronize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/event_management.html#_CPPv419hipEventSynchronize10hipEvent_t "hipEventSynchronize"){.reference .internal} on an event recorded during capture

    - Using events for host synchronization that are part of a stream capture

    - Attempting to reuse events across capturing and non-capturing contexts

    - Mixing event usage between graph capture and immediate execution modes

    Events that are part of a stream capture sequence are handled differently than regular events and cannot be used for host-side synchronization until the capture is complete and the graph is executed.

hipErrorInvalidResourceHandle[\#](#term-hipErrorInvalidResourceHandle "Link to this term"){.headerlink}

:   This error is returned when the input launch stream is a NULL pointer, is invalid, or is [`hipStreamLegacy`{.docutils .literal .notranslate}]{.pre}. If you encounter this error, you should check the validity of the resource handle being used in your HIP API calls. Ensure that the handle was correctly obtained and has not been freed or invalidated before use.
:

::
{#profiler-errors .section}
[]{#id5}

## Profiler Errors[\#](#profiler-errors "Link to this heading"){.headerlink}

{.admonition .warning}
Warning

The HIP Profiler Control APIs ([[`hipProfilerStart()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/profiler_control.html#_CPPv416hipProfilerStartv "hipProfilerStart"){.reference .internal}, [[`hipProfilerStop()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/profiler_control.html#_CPPv415hipProfilerStopv "hipProfilerStop"){.reference .internal}) are deprecated. It is recommended to use the ROCm profiling tools such as rocprof, roctracer, or AMD Radeon GPU Profiler for performance analysis instead.

pst-scrollable-table-container
+----------------------------------------------------------------------------------------------------------------------+----------------------------------------------+-------------------------------------------------------+
| Error Code                                                                                                           | Value                                        | Description                                           |
+======================================================================================================================+==============================================+=======================================================+
| [[hipErrorProfilerDisabled]{.xref .std .std-term}](#term-hipErrorProfilerDisabled){.reference .internal}             | [`5`{.docutils .literal .notranslate}]{.pre} | Profiler disabled while using external profiling tool |
+----------------------------------------------------------------------------------------------------------------------+----------------------------------------------+-------------------------------------------------------+
| [[hipErrorProfilerNotInitialized]{.xref .std .std-term}](#term-hipErrorProfilerNotInitialized){.reference .internal} | [`6`{.docutils .literal .notranslate}]{.pre} | Profiler is not initialized                           |
+----------------------------------------------------------------------------------------------------------------------+----------------------------------------------+-------------------------------------------------------+
| [[hipErrorProfilerAlreadyStarted]{.xref .std .std-term}](#term-hipErrorProfilerAlreadyStarted){.reference .internal} | [`7`{.docutils .literal .notranslate}]{.pre} | Profiler already started                              |
+----------------------------------------------------------------------------------------------------------------------+----------------------------------------------+-------------------------------------------------------+
| [[hipErrorProfilerAlreadyStopped]{.xref .std .std-term}](#term-hipErrorProfilerAlreadyStopped){.reference .internal} | [`8`{.docutils .literal .notranslate}]{.pre} | Profiler already stopped                              |
+----------------------------------------------------------------------------------------------------------------------+----------------------------------------------+-------------------------------------------------------+

hipErrorProfilerDisabled[\#](#term-hipErrorProfilerDisabled "Link to this term"){.headerlink}

:   Profiler disabled while using external profiling tool. This error occurs when attempting to use the built-in HIP profiling functionality while an external profiling tool has taken control of the profiling interface. Common scenarios include:

    - Using [[`hipProfilerStart()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/profiler_control.html#_CPPv416hipProfilerStartv "hipProfilerStart"){.reference .internal} / [[`hipProfilerStop()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/profiler_control.html#_CPPv415hipProfilerStopv "hipProfilerStop"){.reference .internal} while running under tools like rocprof or AMD Radeon GPU Profiler

    - Conflicting profiling requests from different parts of an application

    - Attempting to use the HIP profiling API when profiling has been disabled at the driver level

    - Environment configurations that disable internal profiling in favor of external tools

    When external performance analysis tools are in use, they typically take exclusive control of the profiling interface, preventing the application from using the built-in profiling functions.

hipErrorProfilerNotInitialized[\#](#term-hipErrorProfilerNotInitialized "Link to this term"){.headerlink}

:   Profiler is not initialized. This error occurs when attempting to use profiling functions before the profiler has been properly initialized. Common scenarios include:

    - Calling [[`hipProfilerStop()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/profiler_control.html#_CPPv415hipProfilerStopv "hipProfilerStop"){.reference .internal} without first calling [[`hipProfilerStart()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/profiler_control.html#_CPPv416hipProfilerStartv "hipProfilerStart"){.reference .internal}

    - Using profiling functions before the HIP runtime has fully initialized

    - Configuration issues preventing proper profiler initialization

    - Missing required profiler components or drivers

    The HIP profiler requires proper initialization before it can collect performance data. The [[`hipProfilerStart()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/profiler_control.html#_CPPv416hipProfilerStartv "hipProfilerStart"){.reference .internal} function must be called successfully before using other profiling functions or attempting to collect profile data.

hipErrorProfilerAlreadyStarted[\#](#term-hipErrorProfilerAlreadyStarted "Link to this term"){.headerlink}

:   Profiler already started. This error occurs when attempting to start the HIP profiler when it has already been started. Common scenarios include:

    - Multiple calls to [[`hipProfilerStart()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/profiler_control.html#_CPPv416hipProfilerStartv "hipProfilerStart"){.reference .internal} without intervening [[`hipProfilerStop()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/profiler_control.html#_CPPv415hipProfilerStopv "hipProfilerStop"){.reference .internal}

    - Attempting to restart profiling in different parts of code without coordination

    - Nested profiling sections that don't properly track profiler state

    - Mismanagement of profiler state in complex applications

    The HIP profiler can only be started once and must be stopped before it can be started again. This error is informational and indicates that the profiler is already in the desired active state.

hipErrorProfilerAlreadyStopped[\#](#term-hipErrorProfilerAlreadyStopped "Link to this term"){.headerlink}

:   Profiler already stopped. This error occurs when attempting to stop the HIP profiler when it is not currently running. Common scenarios include:

    - Calling [[`hipProfilerStop()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/profiler_control.html#_CPPv415hipProfilerStopv "hipProfilerStop"){.reference .internal} multiple times without intervening [[`hipProfilerStart()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/profiler_control.html#_CPPv416hipProfilerStartv "hipProfilerStart"){.reference .internal}

    - Mismanagement of profiler state in code with multiple profiling sections

    - Attempting to stop profiling in error handling paths when it wasn't started

    - Improper profiler state tracking in complex applications

    The HIP profiler must be in an active state before it can be stopped. This error is informational and indicates that the profiler is already in the desired inactive state.
::

:
{#resource-mapping-errors .section}
[]{#id6}

## Resource Mapping Errors[\#](#resource-mapping-errors "Link to this heading"){.headerlink}

pst-scrollable-table-container
+--------------------------------------------------------------------------------------------------------------+------------------------------------------------+------------------------------------------+
| Error Code                                                                                                   | Value                                          | Description                              |
+==============================================================================================================+================================================+==========================================+
| [[hipErrorMapFailed]{.xref .std .std-term}](#term-hipErrorMapFailed){.reference .internal}                   | [`205`{.docutils .literal .notranslate}]{.pre} | Mapping of buffer object failed          |
+--------------------------------------------------------------------------------------------------------------+------------------------------------------------+------------------------------------------+
| [[hipErrorUnmapFailed]{.xref .std .std-term}](#term-hipErrorUnmapFailed){.reference .internal}               | [`206`{.docutils .literal .notranslate}]{.pre} | Unmapping of buffer object failed        |
+--------------------------------------------------------------------------------------------------------------+------------------------------------------------+------------------------------------------+
| [[hipErrorArrayIsMapped]{.xref .std .std-term}](#term-hipErrorArrayIsMapped){.reference .internal}           | [`207`{.docutils .literal .notranslate}]{.pre} | Array is mapped                          |
+--------------------------------------------------------------------------------------------------------------+------------------------------------------------+------------------------------------------+
| [[hipErrorAlreadyMapped]{.xref .std .std-term}](#term-hipErrorAlreadyMapped){.reference .internal}           | [`208`{.docutils .literal .notranslate}]{.pre} | Resource already mapped                  |
+--------------------------------------------------------------------------------------------------------------+------------------------------------------------+------------------------------------------+
| [[hipErrorNotMapped]{.xref .std .std-term}](#term-hipErrorNotMapped){.reference .internal}                   | [`211`{.docutils .literal .notranslate}]{.pre} | Resource not mapped                      |
+--------------------------------------------------------------------------------------------------------------+------------------------------------------------+------------------------------------------+
| [[hipErrorNotMappedAsArray]{.xref .std .std-term}](#term-hipErrorNotMappedAsArray){.reference .internal}     | [`212`{.docutils .literal .notranslate}]{.pre} | Resource not mapped as array             |
+--------------------------------------------------------------------------------------------------------------+------------------------------------------------+------------------------------------------+
| [[hipErrorNotMappedAsPointer]{.xref .std .std-term}](#term-hipErrorNotMappedAsPointer){.reference .internal} | [`213`{.docutils .literal .notranslate}]{.pre} | Resource not mapped as pointer           |
+--------------------------------------------------------------------------------------------------------------+------------------------------------------------+------------------------------------------+

hipErrorMapFailed[\#](#term-hipErrorMapFailed "Link to this term"){.headerlink}

:   Mapping of buffer object failed. This error occurs when the system fails to map device memory to host-accessible memory space. Common scenarios include:

    - Insufficient system resources for mapping

    - Attempting to map too much memory simultaneously

    - Mapping memory that is in an invalid state (e.g., already mapped or in use)

    - Trying to map memory with incompatible access flags or properties

    - System-level memory mapping constraints or limitations

    - Attempting to map special memory types that don't support mapping

    - Memory pressure affecting the operating system's ability to establish mappings

    This error typically occurs with functions like [[`hipHostRegister()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management.html#_CPPv415hipHostRegisterPv6size_tj "hipHostRegister"){.reference .internal}, [`hipGLMapBufferObject()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}, or similar functions that attempt to make device memory accessible to the host through memory mapping mechanisms.

hipErrorUnmapFailed[\#](#term-hipErrorUnmapFailed "Link to this term"){.headerlink}

:   Unmapping of buffer object failed. This error occurs when the system fails to unmap previously mapped memory. Common scenarios include:

    - Attempting to unmap memory that is not currently mapped

    - Resources being in use by an active operation

    - System or driver issues affecting memory management

    - Invalid handle or pointer provided to unmap function

    - Corrupted mapping state due to application errors

    - Operating system resource constraints or failures

    This error is the counterpart to [`hipErrorMapFailed`{.docutils .literal .notranslate}]{.pre} and occurs during cleanup operations when releasing mappings between host and device memory spaces. It may indicate resource leaks or state inconsistencies if not properly handled.

hipErrorArrayIsMapped[\#](#term-hipErrorArrayIsMapped "Link to this term"){.headerlink}

:   Array is mapped. This error occurs when attempting an operation that is not permitted on a mapped array or buffer. Common scenarios include:

    - Trying to free or modify a mapped array

    - Performing certain operations that require exclusive access to mapped resources

    - Attempting to re-map an already mapped array

    - Using mapped arrays in ways that conflict with their current mapped state

    - API calls that are incompatible with the current mapping state

    Arrays or buffers that are currently mapped to host memory have certain restrictions on the operations that can be performed on them. They must be unmapped before certain operations are allowed.

hipErrorAlreadyMapped[\#](#term-hipErrorAlreadyMapped "Link to this term"){.headerlink}

:   Resource already mapped. This error occurs when attempting to map a resource that is already in a mapped state. Common scenarios include:

    - Calling mapping functions multiple times on the same resource

    - Improper tracking of resource mapping state in complex applications

    - Race conditions in multi-threaded applications accessing the same resources

    - Attempting to map a resource with different flags when it's already mapped

    This error is similar to [`hipErrorArrayIsMapped`{.docutils .literal .notranslate}]{.pre} but is more general and can apply to various mappable resources, not just arrays. Resources must be unmapped before they can be mapped again, possibly with different properties.

hipErrorNotMapped[\#](#term-hipErrorNotMapped "Link to this term"){.headerlink}

:   Resource not mapped. This error occurs when attempting to perform an operation that requires a resource to be in a mapped state, but the resource is not currently mapped. Common scenarios include:

    - Trying to unmap a resource that is not mapped

    - Attempting to access host pointers for unmapped resources

    - Using mapping-dependent functions on unmapped resources

    - Mismanaging mapping state in complex applications

    - Attempting to use mapping-specific features with resources that don't support mapping

    This error indicates that a resource must be explicitly mapped before certain operations can be performed on it.

hipErrorNotMappedAsArray[\#](#term-hipErrorNotMappedAsArray "Link to this term"){.headerlink}

:   Resource not mapped as array. This error occurs when attempting to use a mapped resource as an array when it was not mapped with the appropriate array mapping type. Common scenarios include:

    - Attempting to use a resource as an array when it was mapped with a different mapping type

    - Using [[`hipArrayGetInfo()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management.html#_CPPv415hipArrayGetInfoP20hipChannelFormatDescP9hipExtentPj10hipArray_t "hipArrayGetInfo"){.reference .internal} or similar functions on resources not mapped as arrays

    - Type confusion in complex applications using multiple mapping types

    - Mismatched mapping and usage patterns for shared resources

    Different mapping types provide access to resources in different ways, and operations specific to one mapping type cannot be used with resources mapped using a different type. This error specifically indicates that an array-specific operation was attempted on a resource that was not mapped as an array.

hipErrorNotMappedAsPointer[\#](#term-hipErrorNotMappedAsPointer "Link to this term"){.headerlink}

:   Resource not mapped as pointer. This error occurs when attempting to use a mapped resource as a pointer when it was not mapped with the appropriate pointer mapping type. Common scenarios include:

    - Attempting to use a resource as a pointer when it was mapped with a different mapping type

    - Trying to perform pointer arithmetic or pointer-based access on inappropriately mapped resources

    - Type confusion in complex applications using multiple mapping types

    - Mismatched mapping and usage patterns for shared resources

    This error is complementary to [`hipErrorNotMappedAsArray`{.docutils .literal .notranslate}]{.pre} and indicates that a pointer-specific operation was attempted on a resource that was not mapped as a pointer. Resources must be mapped with the appropriate mapping type for the operations that will be performed on them.
:

:
{#peer-access-errors .section}
[]{#id7}

## Peer Access Errors[\#](#peer-access-errors "Link to this heading"){.headerlink}

pst-scrollable-table-container
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+--------------------------------------------------------+
| Error Code                                                                                                               | Value                                          | Description                                            |
+==========================================================================================================================+================================================+========================================================+
| [[hipErrorPeerAccessUnsupported]{.xref .std .std-term}](#term-hipErrorPeerAccessUnsupported){.reference .internal}       | [`217`{.docutils .literal .notranslate}]{.pre} | Peer access is not supported between these two devices |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+--------------------------------------------------------+
| [[hipErrorPeerAccessAlreadyEnabled]{.xref .std .std-term}](#term-hipErrorPeerAccessAlreadyEnabled){.reference .internal} | [`704`{.docutils .literal .notranslate}]{.pre} | Peer access is already enabled                         |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+--------------------------------------------------------+
| [[hipErrorPeerAccessNotEnabled]{.xref .std .std-term}](#term-hipErrorPeerAccessNotEnabled){.reference .internal}         | [`705`{.docutils .literal .notranslate}]{.pre} | Peer access has not been enabled                       |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+--------------------------------------------------------+

hipErrorPeerAccessUnsupported[\#](#term-hipErrorPeerAccessUnsupported "Link to this term"){.headerlink}

:   Peer access is not supported between these two devices. This error occurs when attempting to enable peer access between devices that cannot physically support direct access to each other's memory. Common scenarios include:

    - Devices connected to different PCIe root complexes without required hardware support

    - Different types or generations of GPUs that are incompatible for peer access

    - System configurations (BIOS, chipset) that don't allow peer-to-peer transfers

    - Virtualized environments that restrict direct hardware access

    - Attempting peer access on systems where the hardware interconnect doesn't support it

    This error indicates a hardware or system limitation, not an application error. To work around it, use regular host-mediated memory transfers instead of direct peer access. Device compatibility should be verified with [[`hipDeviceCanAccessPeer()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/peer_to_peer_device_memory_access.html#_CPPv422hipDeviceCanAccessPeerPiii "hipDeviceCanAccessPeer"){.reference .internal} before enabling peer access.

hipErrorPeerAccessAlreadyEnabled[\#](#term-hipErrorPeerAccessAlreadyEnabled "Link to this term"){.headerlink}

:   Peer access is already enabled. This error occurs when attempting to enable peer access between two devices when that access has already been enabled. Common scenarios include:

    - Multiple calls to [[`hipDeviceEnablePeerAccess()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/peer_to_peer_device_memory_access.html#_CPPv425hipDeviceEnablePeerAccessij "hipDeviceEnablePeerAccess"){.reference .internal} for the same device pair

    - Enabling peer access in different parts of code without tracking the current state

    - Attempting to re-enable peer access after a context change without checking status

    This error is informational and typically doesn't indicate a problem that needs to be fixed, but rather that the requested state is already in effect.

hipErrorPeerAccessNotEnabled[\#](#term-hipErrorPeerAccessNotEnabled "Link to this term"){.headerlink}

:   Peer access has not been enabled. This error occurs when operations requiring peer access between devices are attempted without first enabling that access. Common scenarios include:

    - Attempting peer-to-peer memory copies without calling [[`hipDeviceEnablePeerAccess()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/peer_to_peer_device_memory_access.html#_CPPv425hipDeviceEnablePeerAccessij "hipDeviceEnablePeerAccess"){.reference .internal}

    - Kernel launches that access memory on peer devices without proper access rights

    - Accessing peer memory after peer access has been disabled

    To fix this error, call [[`hipDeviceEnablePeerAccess()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/peer_to_peer_device_memory_access.html#_CPPv425hipDeviceEnablePeerAccessij "hipDeviceEnablePeerAccess"){.reference .internal} before attempting operations that require direct access between peer devices. Not all device combinations support peer access. Compatibility can be determined with [[`hipDeviceCanAccessPeer()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/peer_to_peer_device_memory_access.html#_CPPv422hipDeviceCanAccessPeerPiii "hipDeviceCanAccessPeer"){.reference .internal}.
:

:
{#system-and-file-errors .section}
[]{#system-file-errors}

## System and File Errors[\#](#system-and-file-errors "Link to this heading"){.headerlink}

pst-scrollable-table-container
+------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+------------------------------------------------------+
| Error Code                                                                                                                   | Value                                           | Description                                          |
+==============================================================================================================================+=================================================+======================================================+
| [[hipErrorFileNotFound]{.xref .std .std-term}](#term-hipErrorFileNotFound){.reference .internal}                             | [`301`{.docutils .literal .notranslate}]{.pre}  | File not found                                       |
+------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+------------------------------------------------------+
| [[hipErrorSharedObjectSymbolNotFound]{.xref .std .std-term}](#term-hipErrorSharedObjectSymbolNotFound){.reference .internal} | [`302`{.docutils .literal .notranslate}]{.pre}  | Shared object symbol not found                       |
+------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+------------------------------------------------------+
| [[hipErrorSharedObjectInitFailed]{.xref .std .std-term}](#term-hipErrorSharedObjectInitFailed){.reference .internal}         | [`303`{.docutils .literal .notranslate}]{.pre}  | Shared object initialization failed                  |
+------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+------------------------------------------------------+
| [[hipErrorOperatingSystem]{.xref .std .std-term}](#term-hipErrorOperatingSystem){.reference .internal}                       | [`304`{.docutils .literal .notranslate}]{.pre}  | OS call failed or operation not supported on this OS |
+------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+------------------------------------------------------+
| [[hipErrorNotFound]{.xref .std .std-term}](#term-hipErrorNotFound){.reference .internal}                                     | [`500`{.docutils .literal .notranslate}]{.pre}  | Named symbol not found                               |
+------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+------------------------------------------------------+
| [[hipErrorRuntimeOther]{.xref .std .std-term}](#term-hipErrorRuntimeOther){.reference .internal}                             | [`1053`{.docutils .literal .notranslate}]{.pre} | Runtime call other than memory returned error        |
+------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+------------------------------------------------------+

hipErrorFileNotFound[\#](#term-hipErrorFileNotFound "Link to this term"){.headerlink}

:   File not found. This error occurs when HIP attempts to load a file that doesn't exist in the specified location. Common scenarios include:

    - Missing kernel source or binary files

    - Incorrect file paths provided to API functions

    - Missing shared libraries or dependencies

    - Files deleted or moved after initial configuration

    - Permission issues preventing file access

    This error typically occurs with operations like loading external kernels, modules, or shared libraries required by HIP applications.

hipErrorSharedObjectSymbolNotFound[\#](#term-hipErrorSharedObjectSymbolNotFound "Link to this term"){.headerlink}

:   Shared object symbol not found. This error occurs when attempting to access a symbol in a shared library or module that doesn't exist or isn't exported. Common scenarios include:

    - Misspelled symbol names

    - Using symbols that exist in the source code but weren't exported in the compiled library

    - Versioning mismatches between headers and implementation

    - Mangled C++ symbol names not properly accounted for

    - Library compiled with different visibility settings than expected

    - Using a function or variable name that exists but is in a different namespace

    This error is commonly encountered when using [[`hipModuleGetFunction()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/module_management.html#_CPPv420hipModuleGetFunctionP13hipFunction_t11hipModule_tPKc "hipModuleGetFunction"){.reference .internal} or similar functions to obtain handles to functions in dynamically loaded modules.

hipErrorSharedObjectInitFailed[\#](#term-hipErrorSharedObjectInitFailed "Link to this term"){.headerlink}

:   Shared object initialization failed. This error occurs when a shared library or module fails during its initialization routine. Common scenarios include:

    - Dependencies of the shared object are missing

    - Incompatible library versions

    - Library initialization code encountering errors

    - Resource allocation failures during initialization

    - Incompatible compilation settings between application and shared object

    - Issues with static constructors in C++ libraries

    This error indicates that while the shared object was found and could be loaded, something prevented its proper initialization, making its functions and resources unavailable for use.

hipErrorOperatingSystem[\#](#term-hipErrorOperatingSystem "Link to this term"){.headerlink}

:   OS call failed or operation not supported on this OS. This error indicates a system-level failure outside of the HIP runtime's direct control. Common scenarios include:

    - Insufficient permissions for requested operations

    - OS resource limits reached (file descriptors, memory limits, etc.)

    - System calls returning failure codes

    - Attempting operations not supported by the current OS or OS version

    - Driver or hardware interactions failing at the OS level

    - File system errors or permission issues

    This is a general error that can occur when HIP interacts with the operating system and encounters problems that prevent successful completion of the requested operation.

hipErrorNotFound[\#](#term-hipErrorNotFound "Link to this term"){.headerlink}

:   Named symbol not found. This error is returned when a requested named entity (such as a symbol, texture, surface, etc.) cannot be found. Common scenarios include:

    - Referencing a kernel function that doesn't exist in the module

    - Looking up a texture that hasn't been bound or created

    - Searching for a device with specific properties that no installed device has

    - Referencing a stream or event that has been destroyed

    - Using a name for a resource that was never created

    - Typos in symbol names

    This error is similar to [`hipErrorSharedObjectSymbolNotFound`{.docutils .literal .notranslate}]{.pre} but is more general and applies to various named entities beyond just symbols in shared objects.

hipErrorRuntimeOther[\#](#term-hipErrorRuntimeOther "Link to this term"){.headerlink}

:   Runtime call other than memory returned error. This is a general error code for failures in the HIP runtime that don't fit into other more specific categories. Common scenarios include:

    - Internal runtime function failures

    - Unexpected conditions encountered during HIP API execution

    - Driver-level errors not covered by more specific error codes

    - Hardware interaction issues

    - State inconsistencies within the runtime

    This is a catch-all error that may require looking at system logs or using additional debugging tools to identify the root cause.
:

:
{#graphics-context-errors .section}
[]{#graphics-content-errors}

## Graphics Context Errors[\#](#graphics-context-errors "Link to this heading"){.headerlink}

pst-scrollable-table-container
+----------------------------------------------------------------------------------------------------------------------+------------------------------------------------+-------------------------------------------------------------------------------+
| Error Code                                                                                                           | Value                                          | Description                                                                   |
+======================================================================================================================+================================================+===============================================================================+
| [[hipErrorInvalidGraphicsContext]{.xref .std .std-term}](#term-hipErrorInvalidGraphicsContext){.reference .internal} | [`219`{.docutils .literal .notranslate}]{.pre} | Invalid OpenGL or DirectX context                                             |
+----------------------------------------------------------------------------------------------------------------------+------------------------------------------------+-------------------------------------------------------------------------------+
| [[hipErrorGraphExecUpdateFailure]{.xref .std .std-term}](#term-hipErrorGraphExecUpdateFailure){.reference .internal} | [`910`{.docutils .literal .notranslate}]{.pre} | 
line                                                                      |
|                                                                                                                      |                                                | The graph update was not performed because it included changes which violated |
|                                                                                                                      |                                                | 
                                                                          |
|                                                                                                                      |                                                |                                                                               |
|                                                                                                                      |                                                | 
line                                                                      |
|                                                                                                                      |                                                | constraints specific to instantiated graph update                             |
|                                                                                                                      |                                                | 
                                                                          |
+----------------------------------------------------------------------------------------------------------------------+------------------------------------------------+-------------------------------------------------------------------------------+

hipErrorInvalidGraphicsContext[\#](#term-hipErrorInvalidGraphicsContext "Link to this term"){.headerlink}

:   Invalid OpenGL or DirectX context. This error occurs when attempting to perform interoperability operations with an invalid or incompatible graphics context.

hipErrorGraphExecUpdateFailure[\#](#term-hipErrorGraphExecUpdateFailure "Link to this term"){.headerlink}

:   The graph update was not performed because it included changes which violated constraints specific to instantiated graph update. This error occurs when attempting to update an already instantiated graph with changes that are not allowed.
:

:
{#hardware-errors .section}
[]{#id8}

## Hardware Errors[\#](#hardware-errors "Link to this heading"){.headerlink}

pst-scrollable-table-container
+------------------------------------------------------------------------------------------------------------+------------------------------------------------+---------------------------------------------+
| Error Code                                                                                                 | Value                                          | Description                                 |
+============================================================================================================+================================================+=============================================+
| [[hipErrorECCNotCorrectable]{.xref .std .std-term}](#term-hipErrorECCNotCorrectable){.reference .internal} | [`214`{.docutils .literal .notranslate}]{.pre} | Uncorrectable ECC error encountered         |
+------------------------------------------------------------------------------------------------------------+------------------------------------------------+---------------------------------------------+
| [[hipErrorUnsupportedLimit]{.xref .std .std-term}](#term-hipErrorUnsupportedLimit){.reference .internal}   | [`215`{.docutils .literal .notranslate}]{.pre} | Limit is not supported on this architecture |
+------------------------------------------------------------------------------------------------------------+------------------------------------------------+---------------------------------------------+
| [[hipErrorAssert]{.xref .std .std-term}](#term-hipErrorAssert){.reference .internal}                       | [`710`{.docutils .literal .notranslate}]{.pre} | Device-side assert triggered                |
+------------------------------------------------------------------------------------------------------------+------------------------------------------------+---------------------------------------------+

hipErrorECCNotCorrectable[\#](#term-hipErrorECCNotCorrectable "Link to this term"){.headerlink}

:   Uncorrectable ECC error encountered. This hardware-level error occurs when the GPU's Error-Correcting Code (ECC) mechanism detects memory corruption that cannot be automatically corrected. Common scenarios include:

    - Physical hardware failure or degradation in GPU memory

    - Overheating causing memory bit flips

    - Running at extreme overclocked settings

    - Aging hardware with declining reliability

    - Power supply issues affecting memory integrity

    When this error occurs, the affected memory contents are unreliable and the operation cannot continue safely. This error generally requires system intervention, and in persistent cases, may indicate hardware that needs replacement.

hipErrorUnsupportedLimit[\#](#term-hipErrorUnsupportedLimit "Link to this term"){.headerlink}

:   Limit is not supported on this architecture. This error occurs when attempting to query or set a device limit that is not supported by the current hardware. Common scenarios include:

    - Using [[`hipDeviceSetLimit()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/device_management.html#_CPPv417hipDeviceSetLimit10hipLimit_t6size_t "hipDeviceSetLimit"){.reference .internal} with a limit type not supported by the hardware

    - Requesting advanced features on entry-level or older GPU hardware

    - Setting limits specific to one GPU architecture on a different architecture

    - Using limit types introduced in newer HIP versions with older hardware

    This error indicates a hardware capability limitation rather than an application error.

hipErrorAssert[\#](#term-hipErrorAssert "Link to this term"){.headerlink}

:   Device-side assert triggered. This error occurs when an assertion inside GPU kernel code fails. Common scenarios include:

    - Explicit [`assert()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre} statement in device code evaluates to false

    - Debug checks added by developers that detect invalid conditions

    - Parameter validation in kernel code that failed

    - Detected algorithmic errors or unexpected conditions

    This error is particularly useful for debugging as it explicitly indicates where a programmer-defined condition was violated in device code.
:
:::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::

{.bd-sidebar-secondary .bd-toc}
::
{.sidebar-secondary-items .sidebar-secondary__inner}
:
sidebar-secondary-item

{.page-toc .tocsection .onthispage}
Contents

:
::

::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::
