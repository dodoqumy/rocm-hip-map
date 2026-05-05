---
title: "Device management &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/reference/hip_runtime_api/modules/device_management.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T06:59:24.292548+00:00
content_hash: "6f0b8a4792a56d15"
---

:::::::::::::::::::::
{#main-content .bd-main role="main"}

sbt-scroll-pixel-helper

:::::::::::::::::::
bd-content
::::::::::::::
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
# Device management

::
{#print-main-content}
:
{#jb-print-toc}

{}
## Contents

:
::

{#searchbox}

{#device-management .section}
[]{#device-management-reference}

# Device management[\#](#device-management "Link to this heading"){.headerlink}

[]{#_CPPv320hipDeviceSynchronizev}[]{#_CPPv220hipDeviceSynchronizev}[]{#hipDeviceSynchronize__void}[]{#group___device_1gaefdc2847fb1d6c3fb1354e827a191ebd .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipDeviceSynchronize]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[)]{.sig-paren}[\#](#_CPPv420hipDeviceSynchronizev "Link to this definition"){.headerlink}\

:   Waits on all active streams on current device.

    When this command is invoked, the host thread gets blocked until all the commands associated with streams associated with the device. HIP does not support multiple blocking modes (yet!).

    
{.admonition .seealso}
    See also

    [[hipSetDevice]{.std .std-ref}](#group___device_1ga43c1e7f15925eeb762195ccb5e063eae){.reference .internal}, [[hipDeviceReset]{.std .std-ref}](#group___device_1ga8d57161ae56a8edc46eeda447417bf6c){.reference .internal}
    

    Returns[:]{.colon}

    :   hipSuccess

<!-- -->

[]{#_CPPv314hipDeviceResetv}[]{#_CPPv214hipDeviceResetv}[]{#hipDeviceReset__void}[]{#group___device_1ga8d57161ae56a8edc46eeda447417bf6c .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipDeviceReset]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[)]{.sig-paren}[\#](#_CPPv414hipDeviceResetv "Link to this definition"){.headerlink}\

:   The state of current device is discarded and updated to a fresh state.

    Calling this function deletes all streams created, memory allocated, kernels running, events created. Make sure that no other thread is using the device or streams, memory, kernels, events associated with the current device.

    
{.admonition .seealso}
    See also

    [[hipDeviceSynchronize]{.std .std-ref}](#group___device_1gaefdc2847fb1d6c3fb1354e827a191ebd){.reference .internal}
    

    Returns[:]{.colon}

    :   hipSuccess

<!-- -->

[]{#_CPPv312hipSetDevicei}[]{#_CPPv212hipSetDevicei}[]{#hipSetDevice__i}[]{#group___device_1ga43c1e7f15925eeb762195ccb5e063eae .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipSetDevice]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[deviceId]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv412hipSetDevicei "Link to this definition"){.headerlink}\

:   Set default device to be used for subsequent hip API calls from this thread.

    Sets [`device`{.docutils .literal .notranslate}]{.pre} as the default device for the calling host thread. Valid device id's are 0... ([[hipGetDeviceCount()]{.std .std-ref}](#group___device_1ga8555d5c76d88c50ddbf54ae70b568394){.reference .internal}-1).

    Many HIP APIs implicitly use the "default device" :

    - Any device memory subsequently allocated from this host thread (using hipMalloc) will be allocated on device.

    - Any streams or events created from this host thread will be associated with device.

    - Any kernels launched from this host thread (using hipLaunchKernel) will be executed on device (unless a specific stream is specified, in which case the device associated with that stream will be used).

    This function may be called from any host thread. Multiple host threads may use the same device. This function does no synchronization with the previous or new device, and has very little runtime overhead. Applications can use hipSetDevice to quickly switch the default device before making a HIP runtime call which uses the default device.

    The default device is stored in thread-local-storage for each thread. Thread-pool implementations may inherit the default device of the previous thread. A good practice is to always call hipSetDevice at the start of HIP coding sequency to establish a known standard device.

    
{.admonition .seealso}
    See also

    [[hipGetDevice]{.std .std-ref}](#group___device_1ga7e0e2e8c5f78e3c7449764657c254e0a){.reference .internal}, [[hipGetDeviceCount]{.std .std-ref}](#group___device_1ga8555d5c76d88c50ddbf54ae70b568394){.reference .internal}
    

    Parameters[:]{.colon}

    :   **deviceId** -- **\[in\]** Valid device in range 0...[[hipGetDeviceCount()]{.std .std-ref}](#group___device_1ga8555d5c76d88c50ddbf54ae70b568394){.reference .internal}.

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidDevice, hipErrorNoDevice

<!-- -->

[]{#_CPPv318hipSetValidDevicesPii}[]{#_CPPv218hipSetValidDevicesPii}[]{#hipSetValidDevices__iP.i}[]{#group___device_1gac5d0061420180b43b74ea39d69351502 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipSetValidDevices]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[device_arr]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[len]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv418hipSetValidDevicesPii "Link to this definition"){.headerlink}\

:   Set a list of devices that can be used.

    
{.admonition .seealso}
    See also

    [[hipGetDevice]{.std .std-ref}](#group___device_1ga7e0e2e8c5f78e3c7449764657c254e0a){.reference .internal}, [[hipGetDeviceCount]{.std .std-ref}](#group___device_1ga8555d5c76d88c50ddbf54ae70b568394){.reference .internal}. [[hipSetDevice]{.std .std-ref}](#group___device_1ga43c1e7f15925eeb762195ccb5e063eae){.reference .internal}. hipGetDeviceProperties. [[hipSetDeviceFlags]{.std .std-ref}](#group___device_1ga6e54db382768827e84725632018307aa){.reference .internal}. hipChooseDevice
    

    Parameters[:]{.colon}

    :   - **device_arr** -- **\[in\]** List of devices to try

        - **len** -- **\[in\]** Number of devices in specified list

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidDevice, hipErrorInvalidValue

<!-- -->

[]{#_CPPv312hipGetDevicePi}[]{#_CPPv212hipGetDevicePi}[]{#hipGetDevice__iP}[]{#group___device_1ga7e0e2e8c5f78e3c7449764657c254e0a .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipGetDevice]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[deviceId]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv412hipGetDevicePi "Link to this definition"){.headerlink}\

:   Return the default device id for the calling host thread.

    HIP maintains an default device for each thread using thread-local-storage. This device is used implicitly for HIP runtime APIs called by this thread. hipGetDevice returns in \* [`device`{.docutils .literal .notranslate}]{.pre} the default device for the calling host thread.

    
{.admonition .seealso}
    See also

    [[hipSetDevice]{.std .std-ref}](#group___device_1ga43c1e7f15925eeb762195ccb5e063eae){.reference .internal}, hipGetDevicesizeBytes
    

    Parameters[:]{.colon}

    :   **deviceId** -- **\[out\]** \*device is written with the default device

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidDevice, hipErrorInvalidValue

<!-- -->

[]{#_CPPv317hipGetDeviceCountPi}[]{#_CPPv217hipGetDeviceCountPi}[]{#hipGetDeviceCount__iP}[]{#group___device_1ga8555d5c76d88c50ddbf54ae70b568394 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipGetDeviceCount]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[count]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv417hipGetDeviceCountPi "Link to this definition"){.headerlink}\

:   Return number of compute-capable devices.

    Returns in [`*count`{.docutils .literal .notranslate}]{.pre} the number of devices that have ability to run compute commands. If there are no such devices, then [[hipGetDeviceCount]{.std .std-ref}](#group___device_1ga8555d5c76d88c50ddbf54ae70b568394){.reference .internal} will return hipErrorNoDevice. If 1 or more devices can be found, then hipGetDeviceCount returns hipSuccess.

    Parameters[:]{.colon}

    :   **count** -- **\[out\]** Returns number of compute-capable devices.

    Returns[:]{.colon}

    :   hipSuccess, hipErrorNoDevice

<!-- -->

[]{#_CPPv321hipDeviceGetAttributePi20hipDeviceAttribute_ti}[]{#_CPPv221hipDeviceGetAttributePi20hipDeviceAttribute_ti}[]{#hipDeviceGetAttribute__iP.hipDeviceAttribute_t.i}[]{#group___device_1ga7080a145a4239a7276e0dc22062026c1 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipDeviceGetAttribute]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[pi]{.pre}]{.n .sig-param}, [[hipDeviceAttribute_t]{.pre}]{.n}[ ]{.w}[[attr]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[deviceId]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv421hipDeviceGetAttributePi20hipDeviceAttribute_ti "Link to this definition"){.headerlink}\

:   Query for a specific device attribute.

    Parameters[:]{.colon}

    :   - **pi** -- **\[out\]** pointer to value to return

        - **attr** -- **\[in\]** attribute to query

        - **deviceId** -- **\[in\]** which device to query for information

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidDevice, hipErrorInvalidValue

<!-- -->

[]{#_CPPv326hipDeviceGetDefaultMemPoolP12hipMemPool_ti}[]{#_CPPv226hipDeviceGetDefaultMemPoolP12hipMemPool_ti}[]{#hipDeviceGetDefaultMemPool__hipMemPool_tP.i}[]{#group___device_1ga16d31ff3398a0c76ea5148563406412a .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipDeviceGetDefaultMemPool]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipMemPool_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[mem_pool]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[device]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv426hipDeviceGetDefaultMemPoolP12hipMemPool_ti "Link to this definition"){.headerlink}\

:   Returns the default memory pool of the specified device.

    
{.admonition .seealso}
    See also

    [[hipDeviceGetDefaultMemPool]{.std .std-ref}](#group___device_1ga16d31ff3398a0c76ea5148563406412a){.reference .internal}, [[hipMallocAsync]{.std .std-ref}](memory_management/stream_ordered_memory_allocator.html#group___stream_o_1gab9b9031bb65f8f9e54487ff8b726591f){.reference .internal}, [[hipMemPoolTrimTo]{.std .std-ref}](memory_management/stream_ordered_memory_allocator.html#group___stream_o_1ga4cd76526312084a115c6007d41ba9b96){.reference .internal}, [[hipMemPoolGetAttribute]{.std .std-ref}](memory_management/stream_ordered_memory_allocator.html#group___stream_o_1ga8ac80ed79a85f4e7a9ce33abfbd8f136){.reference .internal}, [[hipDeviceSetMemPool]{.std .std-ref}](#group___device_1ga29fd231db3cb31fde8f776d5b073e407){.reference .internal}, [[hipMemPoolSetAttribute]{.std .std-ref}](memory_management/stream_ordered_memory_allocator.html#group___stream_o_1ga89006d354ee6e0428a432d6f2e76c8bf){.reference .internal}, [[hipMemPoolSetAccess]{.std .std-ref}](memory_management/stream_ordered_memory_allocator.html#group___stream_o_1ga6198235d5ae856c21f8507fc218e5c0c){.reference .internal}, [[hipMemPoolGetAccess]{.std .std-ref}](memory_management/stream_ordered_memory_allocator.html#group___stream_o_1gabefabb7f014dac6b6f646a517c8dd0a6){.reference .internal}
    

    
{.admonition .warning}
    Warning

    This API is marked as Beta. While this feature is complete, it can change and might have outstanding issues.
    

    Parameters[:]{.colon}

    :   - **mem_pool** -- **\[out\]** Default memory pool to return

        - **device** -- **\[in\]** Device index for query the default memory pool

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidDevice, hipErrorInvalidValue, hipErrorNotSupported

<!-- -->

[]{#_CPPv319hipDeviceSetMemPooli12hipMemPool_t}[]{#_CPPv219hipDeviceSetMemPooli12hipMemPool_t}[]{#hipDeviceSetMemPool__i.hipMemPool_t}[]{#group___device_1ga29fd231db3cb31fde8f776d5b073e407 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipDeviceSetMemPool]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[device]{.pre}]{.n .sig-param}, [[hipMemPool_t]{.pre}]{.n}[ ]{.w}[[mem_pool]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv419hipDeviceSetMemPooli12hipMemPool_t "Link to this definition"){.headerlink}\

:   Sets the current memory pool of a device.

    The memory pool must be local to the specified device. [`hipMallocAsync`{.docutils .literal .notranslate}]{.pre} allocates from the current mempool of the provided stream's device. By default, a device's current memory pool is its default memory pool.

    
{.admonition .seealso}
    See also

    [[hipDeviceGetDefaultMemPool]{.std .std-ref}](#group___device_1ga16d31ff3398a0c76ea5148563406412a){.reference .internal}, [[hipMallocAsync]{.std .std-ref}](memory_management/stream_ordered_memory_allocator.html#group___stream_o_1gab9b9031bb65f8f9e54487ff8b726591f){.reference .internal}, [[hipMemPoolTrimTo]{.std .std-ref}](memory_management/stream_ordered_memory_allocator.html#group___stream_o_1ga4cd76526312084a115c6007d41ba9b96){.reference .internal}, [[hipMemPoolGetAttribute]{.std .std-ref}](memory_management/stream_ordered_memory_allocator.html#group___stream_o_1ga8ac80ed79a85f4e7a9ce33abfbd8f136){.reference .internal}, [[hipDeviceSetMemPool]{.std .std-ref}](#group___device_1ga29fd231db3cb31fde8f776d5b073e407){.reference .internal}, [[hipMemPoolSetAttribute]{.std .std-ref}](memory_management/stream_ordered_memory_allocator.html#group___stream_o_1ga89006d354ee6e0428a432d6f2e76c8bf){.reference .internal}, [[hipMemPoolSetAccess]{.std .std-ref}](memory_management/stream_ordered_memory_allocator.html#group___stream_o_1ga6198235d5ae856c21f8507fc218e5c0c){.reference .internal}, [[hipMemPoolGetAccess]{.std .std-ref}](memory_management/stream_ordered_memory_allocator.html#group___stream_o_1gabefabb7f014dac6b6f646a517c8dd0a6){.reference .internal}
    

    
{.admonition .note}
    Note

    Use [`hipMallocFromPoolAsync`{.docutils .literal .notranslate}]{.pre} for asynchronous memory allocations from a device different than the one the stream runs on.
    

    
{.admonition .warning}
    Warning

    This API is marked as Beta. While this feature is complete, it can change and might have outstanding issues.
    

    Parameters[:]{.colon}

    :   - **device** -- **\[in\]** Device index for the update

        - **mem_pool** -- **\[in\]** Memory pool for update as the current on the specified device

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue, hipErrorInvalidDevice, hipErrorNotSupported

<!-- -->

[]{#_CPPv319hipDeviceGetMemPoolP12hipMemPool_ti}[]{#_CPPv219hipDeviceGetMemPoolP12hipMemPool_ti}[]{#hipDeviceGetMemPool__hipMemPool_tP.i}[]{#group___device_1ga881dfd032ba869936bca97edb1a12ca9 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipDeviceGetMemPool]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipMemPool_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[mem_pool]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[device]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv419hipDeviceGetMemPoolP12hipMemPool_ti "Link to this definition"){.headerlink}\

:   Gets the current memory pool for the specified device.

    Returns the last pool provided to [`hipDeviceSetMemPool`{.docutils .literal .notranslate}]{.pre} for this device or the device's default memory pool if [`hipDeviceSetMemPool`{.docutils .literal .notranslate}]{.pre} has never been called. By default the current mempool is the default mempool for a device, otherwise the returned pool must have been set with [`hipDeviceSetMemPool`{.docutils .literal .notranslate}]{.pre}.

    
{.admonition .seealso}
    See also

    [[hipDeviceGetDefaultMemPool]{.std .std-ref}](#group___device_1ga16d31ff3398a0c76ea5148563406412a){.reference .internal}, [[hipMallocAsync]{.std .std-ref}](memory_management/stream_ordered_memory_allocator.html#group___stream_o_1gab9b9031bb65f8f9e54487ff8b726591f){.reference .internal}, [[hipMemPoolTrimTo]{.std .std-ref}](memory_management/stream_ordered_memory_allocator.html#group___stream_o_1ga4cd76526312084a115c6007d41ba9b96){.reference .internal}, [[hipMemPoolGetAttribute]{.std .std-ref}](memory_management/stream_ordered_memory_allocator.html#group___stream_o_1ga8ac80ed79a85f4e7a9ce33abfbd8f136){.reference .internal}, [[hipDeviceSetMemPool]{.std .std-ref}](#group___device_1ga29fd231db3cb31fde8f776d5b073e407){.reference .internal}, [[hipMemPoolSetAttribute]{.std .std-ref}](memory_management/stream_ordered_memory_allocator.html#group___stream_o_1ga89006d354ee6e0428a432d6f2e76c8bf){.reference .internal}, [[hipMemPoolSetAccess]{.std .std-ref}](memory_management/stream_ordered_memory_allocator.html#group___stream_o_1ga6198235d5ae856c21f8507fc218e5c0c){.reference .internal}, [[hipMemPoolGetAccess]{.std .std-ref}](memory_management/stream_ordered_memory_allocator.html#group___stream_o_1gabefabb7f014dac6b6f646a517c8dd0a6){.reference .internal}
    

    
{.admonition .warning}
    Warning

    This API is marked as Beta. While this feature is complete, it can change and might have outstanding issues.
    

    Parameters[:]{.colon}

    :   - **mem_pool** -- **\[out\]** Current memory pool on the specified device

        - **device** -- **\[in\]** Device index to query the current memory pool

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue, hipErrorNotSupported

<!-- -->

[]{#_CPPv322hipGetDevicePropertiesP15hipDeviceProp_ti}[]{#_CPPv222hipGetDevicePropertiesP15hipDeviceProp_ti}[]{#hipGetDeviceProperties__hipDeviceProp_tP.i}[]{#group___device_1ga32208513b7cd491f0cb5fc884053f790 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipGetDeviceProperties]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipDeviceProp_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[prop]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[deviceId]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv422hipGetDevicePropertiesP15hipDeviceProp_ti "Link to this definition"){.headerlink}\

:   Returns device properties.

    *[Bug:]{.pre}*

    :   HIP-Clang always returns 0 for maxThreadsPerMultiProcessor

        HIP-Clang always returns 0 for regsPerBlock

        HIP-Clang always returns 0 for l2CacheSize

    Populates hipGetDeviceProperties with information for the specified device.

    Parameters[:]{.colon}

    :   - **prop** -- **\[out\]** written with device properties

        - **deviceId** -- **\[in\]** which device to query for information

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidDevice

<!-- -->

[]{#_CPPv335hipDeviceGetTexture1DLinearMaxWidthP6size_tPK20hipChannelFormatDesci}[]{#_CPPv235hipDeviceGetTexture1DLinearMaxWidthP6size_tPK20hipChannelFormatDesci}[]{#hipDeviceGetTexture1DLinearMaxWidth__sP.hipChannelFormatDescCP.i}[]{#group___device_1ga691821555662759693dfeb9acc7826c7 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipDeviceGetTexture1DLinearMaxWidth]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[max_width]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[hipChannelFormatDesc]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[desc]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[device]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv435hipDeviceGetTexture1DLinearMaxWidthP6size_tPK20hipChannelFormatDesci "Link to this definition"){.headerlink}\

:   Gets the maximum width for 1D linear textures on the specified device.

    This function queries the maximum width, in elements, of 1D linear textures that can be allocated on the specified device. The maximum width depends on the texture element size and the hardware limitations of the device.

    
{.admonition .seealso}
    See also

    [[hipDeviceGetAttribute]{.std .std-ref}](#group___device_1ga7080a145a4239a7276e0dc22062026c1){.reference .internal}, [[hipMalloc]{.std .std-ref}](memory_management.html#group___memory_1ga4c6fcfe80010069d2792780d00dcead2){.reference .internal}, [[hipTexRefSetAddressMode]{.std .std-ref}](memory_management/texture_management_deprecated.html#group___texture_d_1ga9c70e94c59c441a3903411256213a963){.reference .internal}
    

    Parameters[:]{.colon}

    :   - **max_width** -- **\[out\]** Maximum width, in elements, of 1D linear textures that the device can support

        - **desc** -- **\[in\]** Requested channel format

        - **device** -- **\[in\]** Device index to query for maximum 1D texture width

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue, hipErrorInvalidDevice

<!-- -->

[]{#_CPPv323hipDeviceSetCacheConfig14hipFuncCache_t}[]{#_CPPv223hipDeviceSetCacheConfig14hipFuncCache_t}[]{#hipDeviceSetCacheConfig__hipFuncCache_t}[]{#group___device_1gaada3d30a46ae06f68cf1574f496b86ee .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipDeviceSetCacheConfig]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipFuncCache_t]{.pre}]{.n}[ ]{.w}[[cacheConfig]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv423hipDeviceSetCacheConfig14hipFuncCache_t "Link to this definition"){.headerlink}\

:   Set L1/Shared cache partition.

    Note: AMD devices do not support reconfigurable cache. This API is not implemented on AMD platform. If the function is called, it will return hipErrorNotSupported.

    Parameters[:]{.colon}

    :   **cacheConfig** -- **\[in\]** Cache configuration

    Returns[:]{.colon}

    :   hipSuccess, hipErrorNotInitialized, hipErrorNotSupported

<!-- -->

[]{#_CPPv323hipDeviceGetCacheConfigP14hipFuncCache_t}[]{#_CPPv223hipDeviceGetCacheConfigP14hipFuncCache_t}[]{#hipDeviceGetCacheConfig__hipFuncCache_tP}[]{#group___device_1ga37057f9830ad6fab7ce5f05f6d3c89ab .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipDeviceGetCacheConfig]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipFuncCache_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[cacheConfig]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv423hipDeviceGetCacheConfigP14hipFuncCache_t "Link to this definition"){.headerlink}\

:   Get Cache configuration for a specific Device.

    Parameters[:]{.colon}

    :   **cacheConfig** -- **\[out\]** Pointer of cache configuration

    Returns[:]{.colon}

    :   hipSuccess, hipErrorNotInitialized Note: AMD devices do not support reconfigurable cache. This hint is ignored on these architectures.

<!-- -->

[]{#_CPPv317hipDeviceGetLimitP6size_t10hipLimit_t}[]{#_CPPv217hipDeviceGetLimitP6size_t10hipLimit_t}[]{#hipDeviceGetLimit__sP.hipLimit_t}[]{#group___device_1ga8edc85bb9637d6b1eda0d064d141a255 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipDeviceGetLimit]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[pValue]{.pre}]{.n .sig-param}, [[enum]{.pre}]{.k}[ ]{.w}[[hipLimit_t]{.pre}]{.n}[ ]{.w}[[limit]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv417hipDeviceGetLimitP6size_t10hipLimit_t "Link to this definition"){.headerlink}\

:   Gets resource limits of current device.

    The function queries the size of limit value, as required by the input enum value hipLimit_t, which can be either hipLimitStackSize, or hipLimitMallocHeapSize. Any other input as default, the function will return hipErrorUnsupportedLimit.

    Parameters[:]{.colon}

    :   - **pValue** -- **\[out\]** Returns the size of the limit in bytes

        - **limit** -- **\[in\]** The limit to query

    Returns[:]{.colon}

    :   hipSuccess, hipErrorUnsupportedLimit, hipErrorInvalidValue

<!-- -->

[]{#_CPPv317hipDeviceSetLimit10hipLimit_t6size_t}[]{#_CPPv217hipDeviceSetLimit10hipLimit_t6size_t}[]{#hipDeviceSetLimit__hipLimit_t.s}[]{#group___device_1gaaa264755a3c1750a12c60aa7807b7fe8 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipDeviceSetLimit]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[enum]{.pre}]{.k}[ ]{.w}[[hipLimit_t]{.pre}]{.n}[ ]{.w}[[limit]{.pre}]{.n .sig-param}, [[size_t]{.pre}]{.n}[ ]{.w}[[value]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv417hipDeviceSetLimit10hipLimit_t6size_t "Link to this definition"){.headerlink}\

:   Sets resource limits of current device.

    As the input enum limit, hipLimitStackSize sets the limit value of the stack size on the current GPU device, per thread. The limit size can get via hipDeviceGetLimit. The size is in units of 256 dwords, up to the limit (128K - 16).

    hipLimitMallocHeapSize sets the limit value of the heap used by the malloc()/free() calls. For limit size, use the [[hipDeviceGetLimit]{.std .std-ref}](#group___device_1ga8edc85bb9637d6b1eda0d064d141a255){.reference .internal} API.

    Any other input as default, the funtion will return hipErrorUnsupportedLimit.

    Parameters[:]{.colon}

    :   - **limit** -- **\[in\]** Enum of hipLimit_t to set

        - **value** -- **\[in\]** The size of limit value in bytes

    Returns[:]{.colon}

    :   hipSuccess, hipErrorUnsupportedLimit, hipErrorInvalidValue

<!-- -->

[]{#_CPPv327hipDeviceGetSharedMemConfigP18hipSharedMemConfig}[]{#_CPPv227hipDeviceGetSharedMemConfigP18hipSharedMemConfig}[]{#hipDeviceGetSharedMemConfig__hipSharedMemConfigP}[]{#group___device_1ga1bb08f774a34a468d969a8a04791c9bb .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipDeviceGetSharedMemConfig]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipSharedMemConfig]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[pConfig]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv427hipDeviceGetSharedMemConfigP18hipSharedMemConfig "Link to this definition"){.headerlink}\

:   Returns bank width of shared memory for current device.

    Note: AMD devices and some Nvidia GPUS do not support shared cache banking, and the hint is ignored on those architectures.

    Parameters[:]{.colon}

    :   **pConfig** -- **\[out\]** The pointer of the bank width for shared memory

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue, hipErrorNotInitialized

<!-- -->

[]{#_CPPv317hipGetDeviceFlagsPj}[]{#_CPPv217hipGetDeviceFlagsPj}[]{#hipGetDeviceFlags__unsigned-iP}[]{#group___device_1ga1270f7281bb46cf3e077944e6f233d53 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipGetDeviceFlags]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[unsigned]{.pre}]{.kt}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[flags]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv417hipGetDeviceFlagsPj "Link to this definition"){.headerlink}\

:   Gets the flags set for current device.

    Parameters[:]{.colon}

    :   **flags** -- **\[out\]** Pointer of the flags

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidDevice, hipErrorInvalidValue

<!-- -->

[]{#_CPPv327hipDeviceSetSharedMemConfig18hipSharedMemConfig}[]{#_CPPv227hipDeviceSetSharedMemConfig18hipSharedMemConfig}[]{#hipDeviceSetSharedMemConfig__hipSharedMemConfig}[]{#group___device_1ga9b1f279084e76691cedfbfadf9c717ee .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipDeviceSetSharedMemConfig]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipSharedMemConfig]{.pre}]{.n}[ ]{.w}[[config]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv427hipDeviceSetSharedMemConfig18hipSharedMemConfig "Link to this definition"){.headerlink}\

:   The bank width of shared memory on current device is set.

    Note: AMD devices and some Nvidia GPUS do not support shared cache banking, and the hint is ignored on those architectures.

    Parameters[:]{.colon}

    :   **config** -- **\[in\]** Configuration for the bank width of shared memory

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue, hipErrorNotInitialized

<!-- -->

[]{#_CPPv317hipSetDeviceFlagsj}[]{#_CPPv217hipSetDeviceFlagsj}[]{#hipSetDeviceFlags__unsigned}[]{#group___device_1ga6e54db382768827e84725632018307aa .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipSetDeviceFlags]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[unsigned]{.pre}]{.kt}[ ]{.w}[[flags]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv417hipSetDeviceFlagsj "Link to this definition"){.headerlink}\

:   The current device behavior is changed according to the flags passed.

    The schedule flags impact how HIP waits for the completion of a command running on a device.

    hipDeviceScheduleSpin : HIP runtime will actively spin in the thread which submitted the work until the command completes. This offers the lowest latency, but will consume a CPU core and may increase power.

    hipDeviceScheduleYield : The HIP runtime will yield the CPU to system so that other tasks can use it. This may increase latency to detect the completion but will consume less power and is friendlier to other tasks in the system.

    hipDeviceScheduleBlockingSync : On ROCm platform, this is a synonym for hipDeviceScheduleYield.

    hipDeviceScheduleAuto : This is the default value if the input 'flags' is zero. Uses a heuristic to select between Spin and Yield modes. If the number of HIP contexts is greater than the number of logical processors in the system, uses Spin scheduling, otherwise uses Yield scheduling.

    hipDeviceMapHost : Allows mapping host memory. On ROCm, this is always allowed and the flag is ignored.

    hipDeviceLmemResizeToMax : This flag is silently ignored on ROCm.

    Parameters[:]{.colon}

    :   **flags** -- **\[in\]** Flag to set on the current device

    Returns[:]{.colon}

    :   hipSuccess, hipErrorNoDevice, hipErrorInvalidDevice, hipErrorSetOnActiveProcess

<!-- -->

[]{#_CPPv315hipChooseDevicePiPK15hipDeviceProp_t}[]{#_CPPv215hipChooseDevicePiPK15hipDeviceProp_t}[]{#hipChooseDevice__iP.hipDeviceProp_tCP}[]{#group___device_1gaf1e365e1d17cf40644d1470de4817c8e .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipChooseDevice]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[device]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[hipDeviceProp_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[prop]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv415hipChooseDevicePiPK15hipDeviceProp_t "Link to this definition"){.headerlink}\

:   Device which matches hipDeviceProp_t is returned.

    Parameters[:]{.colon}

    :   - **device** -- **\[out\]** Pointer of the device

        - **prop** -- **\[in\]** Pointer of the properties

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue

<!-- -->

[]{#_CPPv328hipExtGetLinkTypeAndHopCountiiP8uint32_tP8uint32_t}[]{#_CPPv228hipExtGetLinkTypeAndHopCountiiP8uint32_tP8uint32_t}[]{#hipExtGetLinkTypeAndHopCount__i.i.uint32_tP.uint32_tP}[]{#group___device_1ga633f8eed24c1d27ed55f950aab99fc88 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipExtGetLinkTypeAndHopCount]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[device1]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[device2]{.pre}]{.n .sig-param}, [[uint32_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[linktype]{.pre}]{.n .sig-param}, [[uint32_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[hopcount]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv428hipExtGetLinkTypeAndHopCountiiP8uint32_tP8uint32_t "Link to this definition"){.headerlink}\

:   Returns the link type and hop count between two devices.

    Queries and returns the HSA link type and the hop count between the two specified devices.

    Parameters[:]{.colon}

    :   - **device1** -- **\[in\]** Ordinal for device1

        - **device2** -- **\[in\]** Ordinal for device2

        - **linktype** -- **\[out\]** Returns the link type (See hsa_amd_link_info_type_t) between the two devices

        - **hopcount** -- **\[out\]** Returns the hop count between the two devices

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue

<!-- -->

[]{#_CPPv318hipIpcGetMemHandleP17hipIpcMemHandle_tPv}[]{#_CPPv218hipIpcGetMemHandleP17hipIpcMemHandle_tPv}[]{#hipIpcGetMemHandle__hipIpcMemHandle_tP.voidP}[]{#group___device_1gafd8c80f7e3b6426a630fff768409be70 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipIpcGetMemHandle]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipIpcMemHandle_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[devPtr]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv418hipIpcGetMemHandleP17hipIpcMemHandle_tPv "Link to this definition"){.headerlink}\

:   Gets an interprocess memory handle for an existing device memory allocation.

    Takes a pointer to the base of an existing device memory allocation created with hipMalloc and exports it for use in another process. This is a lightweight operation and may be called multiple times on an allocation without adverse effects.

    If a region of memory is freed with hipFree and a subsequent call to hipMalloc returns memory with the same device address, hipIpcGetMemHandle will return a unique handle for the new memory.

    
{.admonition .note}
    Note

    This IPC memory related feature API on Windows may behave differently from Linux.
    

    Parameters[:]{.colon}

    :   - **handle** -- - Pointer to user allocated hipIpcMemHandle to return the handle in.

        - **devPtr** -- - Base pointer to previously allocated device memory

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidHandle, hipErrorOutOfMemory, hipErrorMapFailed

<!-- -->

[]{#_CPPv319hipIpcOpenMemHandlePPv17hipIpcMemHandle_tj}[]{#_CPPv219hipIpcOpenMemHandlePPv17hipIpcMemHandle_tj}[]{#hipIpcOpenMemHandle__voidPP.hipIpcMemHandle_t.unsigned-i}[]{#group___device_1ga2ada334c986e10805d58167e260cb0df .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipIpcOpenMemHandle]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[devPtr]{.pre}]{.n .sig-param}, [[hipIpcMemHandle_t]{.pre}]{.n}[ ]{.w}[[handle]{.pre}]{.n .sig-param}, [[unsigned]{.pre}]{.kt}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[flags]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv419hipIpcOpenMemHandlePPv17hipIpcMemHandle_tj "Link to this definition"){.headerlink}\

:   Opens an interprocess memory handle exported from another process and returns a device pointer usable in the local process.

    Maps memory exported from another process with hipIpcGetMemHandle into the current device address space. For contexts on different devices hipIpcOpenMemHandle can attempt to enable peer access between the devices as if the user called hipDeviceEnablePeerAccess. This behavior is controlled by the hipIpcMemLazyEnablePeerAccess flag. hipDeviceCanAccessPeer can determine if a mapping is possible.

    Contexts that may open hipIpcMemHandles are restricted in the following way. hipIpcMemHandles from each device in a given process may only be opened by one context per device per other process.

    Memory returned from hipIpcOpenMemHandle must be freed with hipIpcCloseMemHandle.

    Calling hipFree on an exported memory region before calling hipIpcCloseMemHandle in the importing context will result in undefined behavior.

    
{.admonition .note}
    Note

    During multiple processes, using the same memory handle opened by the current context, there is no guarantee that the same device poiter will be returned in [`*devPtr`{.docutils .literal .notranslate}]{.pre}. This is diffrent from CUDA.
    

    
{.admonition .note}
    Note

    This IPC memory related feature API on Windows may behave differently from Linux.
    

    Parameters[:]{.colon}

    :   - **devPtr** -- - Returned device pointer

        - **handle** -- - hipIpcMemHandle to open

        - **flags** -- - Flags for this operation. Must be specified as hipIpcMemLazyEnablePeerAccess

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue, hipErrorInvalidContext, hipErrorInvalidDevicePointer

<!-- -->

[]{#_CPPv320hipIpcCloseMemHandlePv}[]{#_CPPv220hipIpcCloseMemHandlePv}[]{#hipIpcCloseMemHandle__voidP}[]{#group___device_1gac2db0688a6a471e17ca631977e199da7 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipIpcCloseMemHandle]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[devPtr]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv420hipIpcCloseMemHandlePv "Link to this definition"){.headerlink}\

:   Close memory mapped with hipIpcOpenMemHandle.

    Unmaps memory returnd by hipIpcOpenMemHandle. The original allocation in the exporting process as well as imported mappings in other processes will be unaffected.

    Any resources used to enable peer access will be freed if this is the last mapping using them.

    
{.admonition .note}
    Note

    This IPC memory related feature API on Windows may behave differently from Linux.
    

    Parameters[:]{.colon}

    :   **devPtr** -- - Device pointer returned by hipIpcOpenMemHandle

    Returns[:]{.colon}

    :   hipSuccess, hipErrorMapFailed, hipErrorInvalidHandle

<!-- -->

[]{#_CPPv320hipIpcGetEventHandleP19hipIpcEventHandle_t10hipEvent_t}[]{#_CPPv220hipIpcGetEventHandleP19hipIpcEventHandle_t10hipEvent_t}[]{#hipIpcGetEventHandle__hipIpcEventHandle_tP.hipEvent_t}[]{#group___device_1ga16b63a461a72d22dbcbbdbdff548adba .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipIpcGetEventHandle]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipIpcEventHandle_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[hipEvent_t]{.pre}]{.n}[ ]{.w}[[event]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv420hipIpcGetEventHandleP19hipIpcEventHandle_t10hipEvent_t "Link to this definition"){.headerlink}\

:   Gets an opaque interprocess handle for an event.

    This opaque handle may be copied into other processes and opened with hipIpcOpenEventHandle. Then hipEventRecord, hipEventSynchronize, hipStreamWaitEvent and hipEventQuery may be used in either process. Operations on the imported event after the exported event has been freed with hipEventDestroy will result in undefined behavior.

    
{.admonition .note}
    Note

    This IPC event related feature API is currently applicable on Linux.
    

    Parameters[:]{.colon}

    :   - **handle** -- **\[out\]** Pointer to hipIpcEventHandle to return the opaque event handle

        - **event** -- **\[in\]** Event allocated with hipEventInterprocess and hipEventDisableTiming flags

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidConfiguration, hipErrorInvalidValue

<!-- -->

[]{#_CPPv321hipIpcOpenEventHandleP10hipEvent_t19hipIpcEventHandle_t}[]{#_CPPv221hipIpcOpenEventHandleP10hipEvent_t19hipIpcEventHandle_t}[]{#hipIpcOpenEventHandle__hipEvent_tP.hipIpcEventHandle_t}[]{#group___device_1gae73ef28488c43e5343fdf02178c25a5d .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipIpcOpenEventHandle]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipEvent_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[event]{.pre}]{.n .sig-param}, [[hipIpcEventHandle_t]{.pre}]{.n}[ ]{.w}[[handle]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv421hipIpcOpenEventHandleP10hipEvent_t19hipIpcEventHandle_t "Link to this definition"){.headerlink}\

:   Opens an interprocess event handles.

    Opens an interprocess event handle exported from another process with hipIpcGetEventHandle. The returned hipEvent_t behaves like a locally created event with the hipEventDisableTiming flag specified. This event need be freed with hipEventDestroy. Operations on the imported event after the exported event has been freed with hipEventDestroy will result in undefined behavior. If the function is called within the same process where handle is returned by hipIpcGetEventHandle, it will return hipErrorInvalidContext.

    
{.admonition .note}
    Note

    This IPC event related feature API is currently applicable on Linux.
    

    Parameters[:]{.colon}

    :   - **event** -- **\[out\]** Pointer to hipEvent_t to return the event

        - **handle** -- **\[in\]** The opaque interprocess handle to open

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue, hipErrorInvalidContext

::::::::::::::

{.bd-sidebar-secondary .bd-toc}
::
{.sidebar-secondary-items .sidebar-secondary__inner}
:
sidebar-secondary-item

{.page-toc .tocsection .onthispage}
Contents

:
::

:::::::::::::::::::
:::::::::::::::::::::
