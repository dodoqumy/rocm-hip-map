---
title: "HIP deprecated runtime API functions &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/reference/deprecated_api_list.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T06:58:47.560652+00:00
content_hash: "75f106a66e5bf711"
---

:::::::::::::::::::::::::::::::::::::
{#main-content .bd-main role="main"}

sbt-scroll-pixel-helper

:::::::::::::::::::::::::::::::::::
bd-content
::::::::::::::::::::::::::::::
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
# HIP deprecated runtime API functions

::
{#print-main-content}
:
{#jb-print-toc}

{}
## Contents

:
::

{#searchbox}

::::::::::::::::
{#hip-deprecated-runtime-api-functions .section}
# HIP deprecated runtime API functions[\#](#hip-deprecated-runtime-api-functions "Link to this heading"){.headerlink}

Several of our API functions have been flagged for deprecation. Using the following functions results in errors and unexpected results, so we encourage you to update your code accordingly.

:
{#deprecated-since-rocm-6-1-0 .section}
## Deprecated since ROCm 6.1.0[\#](#deprecated-since-rocm-6-1-0 "Link to this heading"){.headerlink}

Deprecated texture management functions.

pst-scrollable-table-container
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| function                                                                                                                                                                                                                                                                        |
+=================================================================================================================================================================================================================================================================================+
| [[`hipTexRefGetBorderColor()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management/texture_management_deprecated.html#_CPPv423hipTexRefGetBorderColorPfPK16textureReference "hipTexRefGetBorderColor"){.reference .internal} |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipTexRefGetArray()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management/texture_management_deprecated.html#_CPPv417hipTexRefGetArrayP10hipArray_tPK16textureReference "hipTexRefGetArray"){.reference .internal}        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

:

:
{#deprecated-since-rocm-5-7-0 .section}
## Deprecated since ROCm 5.7.0[\#](#deprecated-since-rocm-5-7-0 "Link to this heading"){.headerlink}

Deprecated texture management functions.

pst-scrollable-table-container
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| function                                                                                                                                                                                                                                                                                                                                              |
+=======================================================================================================================================================================================================================================================================================================================================================+
| [[`hipBindTextureToMipmappedArray()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management/texture_management_deprecated.html#_CPPv430hipBindTextureToMipmappedArrayPK16textureReference25hipMipmappedArray_const_tPK20hipChannelFormatDesc "hipBindTextureToMipmappedArray"){.reference .internal} |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

:

:
{#deprecated-since-rocm-5-3-0 .section}
## Deprecated since ROCm 5.3.0[\#](#deprecated-since-rocm-5-3-0 "Link to this heading"){.headerlink}

Deprecated texture management functions.

pst-scrollable-table-container
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| function                                                                                                                                                                                                                                                                                                          |
+===================================================================================================================================================================================================================================================================================================================+
| [[`hipGetTextureReference()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management/texture_management_deprecated.html#_CPPv422hipGetTextureReferencePPK16textureReferencePKv "hipGetTextureReference"){.reference .internal}                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipTexRefSetAddressMode()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management/texture_management_deprecated.html#_CPPv423hipTexRefSetAddressModeP16textureReferencei21hipTextureAddressMode "hipTexRefSetAddressMode"){.reference .internal}              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipTexRefSetArray()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management/texture_management_deprecated.html#_CPPv417hipTexRefSetArrayP16textureReference16hipArray_const_tj "hipTexRefSetArray"){.reference .internal}                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipTexRefSetFlags()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management/texture_management_deprecated.html#_CPPv417hipTexRefSetFlagsP16textureReferencej "hipTexRefSetFlags"){.reference .internal}                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipTexRefSetFilterMode()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management/texture_management_deprecated.html#_CPPv422hipTexRefSetFilterModeP16textureReference20hipTextureFilterMode "hipTexRefSetFilterMode"){.reference .internal}                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipTexRefSetFormat()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management/texture_management_deprecated.html#_CPPv418hipTexRefSetFormatP16textureReference15hipArray_Formati "hipTexRefSetFormat"){.reference .internal}                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipTexRefSetMipmapFilterMode()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management/texture_management_deprecated.html#_CPPv428hipTexRefSetMipmapFilterModeP16textureReference20hipTextureFilterMode "hipTexRefSetMipmapFilterMode"){.reference .internal} |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipTexRefSetMipmapLevelBias()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management/texture_management_deprecated.html#_CPPv427hipTexRefSetMipmapLevelBiasP16textureReferencef "hipTexRefSetMipmapLevelBias"){.reference .internal}                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipTexRefSetMipmapLevelClamp()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management/texture_management_deprecated.html#_CPPv428hipTexRefSetMipmapLevelClampP16textureReferenceff "hipTexRefSetMipmapLevelClamp"){.reference .internal}                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipTexRefSetMipmappedArray()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management/texture_management_deprecated.html#_CPPv426hipTexRefSetMipmappedArrayP16textureReferenceP17hipMipmappedArrayj "hipTexRefSetMipmappedArray"){.reference .internal}        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

:

:
{#deprecated-since-rocm-4-3-0 .section}
## Deprecated since ROCm 4.3.0[\#](#deprecated-since-rocm-4-3-0 "Link to this heading"){.headerlink}

Deprecated texture management functions.

pst-scrollable-table-container
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| function                                                                                                                                                                                                                                                                                                              |
+=======================================================================================================================================================================================================================================================================================================================+
| [[`hipTexRefGetAddress()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management/texture_management_deprecated.html#_CPPv419hipTexRefGetAddressP14hipDeviceptr_tPK16textureReference "hipTexRefGetAddress"){.reference .internal}                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipTexRefGetAddressMode()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management/texture_management_deprecated.html#_CPPv423hipTexRefGetAddressModeP21hipTextureAddressModePK16textureReferencei "hipTexRefGetAddressMode"){.reference .internal}                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipTexRefGetFilterMode()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management/texture_management_deprecated.html#_CPPv422hipTexRefGetFilterModeP20hipTextureFilterModePK16textureReference "hipTexRefGetFilterMode"){.reference .internal}                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipTexRefGetFlags()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management/texture_management_deprecated.html#_CPPv417hipTexRefGetFlagsPjPK16textureReference "hipTexRefGetFlags"){.reference .internal}                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipTexRefGetFormat()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management/texture_management_deprecated.html#_CPPv418hipTexRefGetFormatP15hipArray_FormatPiPK16textureReference "hipTexRefGetFormat"){.reference .internal}                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipTexRefGetMaxAnisotropy()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management/texture_management_deprecated.html#_CPPv425hipTexRefGetMaxAnisotropyPiPK16textureReference "hipTexRefGetMaxAnisotropy"){.reference .internal}                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipTexRefGetMipmapFilterMode()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management/texture_management_deprecated.html#_CPPv428hipTexRefGetMipmapFilterModeP20hipTextureFilterModePK16textureReference "hipTexRefGetMipmapFilterMode"){.reference .internal}   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipTexRefGetMipmapLevelBias()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management/texture_management_deprecated.html#_CPPv427hipTexRefGetMipmapLevelBiasPfPK16textureReference "hipTexRefGetMipmapLevelBias"){.reference .internal}                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipTexRefGetMipmapLevelClamp()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management/texture_management_deprecated.html#_CPPv428hipTexRefGetMipmapLevelClampPfPfPK16textureReference "hipTexRefGetMipmapLevelClamp"){.reference .internal}                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipTexRefGetMipMappedArray()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management/texture_management_deprecated.html#_CPPv426hipTexRefGetMipMappedArrayP19hipMipmappedArray_tPK16textureReference "hipTexRefGetMipMappedArray"){.reference .internal}          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipTexRefSetAddress()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management/texture_management_deprecated.html#_CPPv419hipTexRefSetAddressP6size_tP16textureReference14hipDeviceptr_t6size_t "hipTexRefSetAddress"){.reference .internal}                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipTexRefSetAddress2D()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management/texture_management_deprecated.html#_CPPv421hipTexRefSetAddress2DP16textureReferencePK20HIP_ARRAY_DESCRIPTOR14hipDeviceptr_t6size_t "hipTexRefSetAddress2D"){.reference .internal} |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipTexRefSetBorderColor()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management/texture_management_deprecated.html#_CPPv423hipTexRefSetBorderColorP16textureReferencePf "hipTexRefSetBorderColor"){.reference .internal}                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipTexRefSetMaxAnisotropy()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management/texture_management_deprecated.html#_CPPv425hipTexRefSetMaxAnisotropyP16textureReferencej "hipTexRefSetMaxAnisotropy"){.reference .internal}                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

:

:
{#deprecated-since-rocm-3-8-0 .section}
## Deprecated since ROCm 3.8.0[\#](#deprecated-since-rocm-3-8-0 "Link to this heading"){.headerlink}

Deprecated memory management and texture management functions.

pst-scrollable-table-container
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| function                                                                                                                                                                                                                                                                                                          |
+===================================================================================================================================================================================================================================================================================================================+
| [[`hipBindTexture()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management/texture_management_deprecated.html#_CPPv414hipBindTextureP6size_tPK16textureReferencePKvPK20hipChannelFormatDesc6size_t "hipBindTexture"){.reference .internal}                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipBindTexture2D()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management/texture_management_deprecated.html#_CPPv416hipBindTexture2DP6size_tPK16textureReferencePKvPK20hipChannelFormatDesc6size_t6size_t6size_t "hipBindTexture2D"){.reference .internal}  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipBindTextureToArray()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management/texture_management_deprecated.html#_CPPv421hipBindTextureToArrayPK16textureReference16hipArray_const_tPK20hipChannelFormatDesc "hipBindTextureToArray"){.reference .internal} |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipGetTextureAlignmentOffset()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management/texture_management_deprecated.html#_CPPv428hipGetTextureAlignmentOffsetP6size_tPK16textureReference "hipGetTextureAlignmentOffset"){.reference .internal}              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipUnbindTexture()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management/texture_management_deprecated.html#_CPPv416hipUnbindTexturePK16textureReference "hipUnbindTexture"){.reference .internal}                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipMemcpyToArray()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management/memory_management_deprecated.html#_CPPv416hipMemcpyToArray10hipArray_t6size_t6size_tPKv6size_t13hipMemcpyKind "hipMemcpyToArray"){.reference .internal}                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipMemcpyFromArray()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management/memory_management_deprecated.html#_CPPv418hipMemcpyFromArrayPv16hipArray_const_t6size_t6size_t6size_t13hipMemcpyKind "hipMemcpyFromArray"){.reference .internal}                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

:

:
{#deprecated-since-rocm-3-1-0 .section}
## Deprecated since ROCm 3.1.0[\#](#deprecated-since-rocm-3-1-0 "Link to this heading"){.headerlink}

Deprecated memory management functions.

pst-scrollable-table-container
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| function                                                                                                                                                                                                                                   |                                                                                                                                                                                                                     |
+============================================================================================================================================================================================================================================+=====================================================================================================================================================================================================================+
| [[`hipMallocHost()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management/memory_management_deprecated.html#_CPPv413hipMallocHostPPv6size_t "hipMallocHost"){.reference .internal}       | replaced with [[`hipHostAlloc()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management.html#_CPPv412hipHostAllocPPv6size_tj "hipHostAlloc"){.reference .internal} |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipMemAllocHost()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management/memory_management_deprecated.html#_CPPv415hipMemAllocHostPPv6size_t "hipMemAllocHost"){.reference .internal} | replaced with [[`hipHostAlloc()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/memory_management.html#_CPPv412hipHostAllocPPv6size_tj "hipHostAlloc"){.reference .internal} |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

:

:
{#deprecated-since-rocm-3-0-0 .section}
## Deprecated since ROCm 3.0.0[\#](#deprecated-since-rocm-3-0-0 "Link to this heading"){.headerlink}

The [`hipProfilerStart`{.docutils .literal .notranslate}]{.pre} and [`hipProfilerStop`{.docutils .literal .notranslate}]{.pre} functions are deprecated. Instead, you can use [`roctracer`{.docutils .literal .notranslate}]{.pre} or [`rocTX`{.docutils .literal .notranslate}]{.pre} for profiling which provide more flexibility and detailed profiling capabilities.

pst-scrollable-table-container
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| function                                                                                                                                                                                               |
+========================================================================================================================================================================================================+
| [[`hipProfilerStart()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/profiler_control.html#_CPPv416hipProfilerStartv "hipProfilerStart"){.reference .internal} |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipProfilerStop()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/profiler_control.html#_CPPv415hipProfilerStopv "hipProfilerStop"){.reference .internal}    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

:

:
{#deprecated-since-rocm-1-9-0 .section}
## Deprecated since ROCm 1.9.0[\#](#deprecated-since-rocm-1-9-0 "Link to this heading"){.headerlink}

CUDA supports cuCtx API, which is the driver API that defines "Context" and "Devices" as separate entities. Context contains a single device, and a device can theoretically have multiple contexts. HIP initially added limited support for context APIs in order to facilitate porting from existing driver codes. These APIs are now marked as deprecated because there are better alternate interfaces (such as [`hipSetDevice`{.docutils .literal .notranslate}]{.pre} or the stream API) to achieve these functions.

pst-scrollable-table-container
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| function                                                                                                                                                                                                                                                  |
+===========================================================================================================================================================================================================================================================+
| [[`hipCtxCreate()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/context_management.html#_CPPv412hipCtxCreateP8hipCtx_tj11hipDevice_t "hipCtxCreate"){.reference .internal}                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipCtxDestroy()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/context_management.html#_CPPv413hipCtxDestroy8hipCtx_t "hipCtxDestroy"){.reference .internal}                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipCtxPopCurrent()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/context_management.html#_CPPv416hipCtxPopCurrentP8hipCtx_t "hipCtxPopCurrent"){.reference .internal}                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipCtxPushCurrent()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/context_management.html#_CPPv417hipCtxPushCurrent8hipCtx_t "hipCtxPushCurrent"){.reference .internal}                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipCtxSetCurrent()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/context_management.html#_CPPv416hipCtxSetCurrent8hipCtx_t "hipCtxSetCurrent"){.reference .internal}                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipCtxGetCurrent()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/context_management.html#_CPPv416hipCtxGetCurrentP8hipCtx_t "hipCtxGetCurrent"){.reference .internal}                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipCtxGetDevice()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/context_management.html#_CPPv415hipCtxGetDeviceP11hipDevice_t "hipCtxGetDevice"){.reference .internal}                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipCtxGetApiVersion()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/context_management.html#_CPPv419hipCtxGetApiVersion8hipCtx_tPj "hipCtxGetApiVersion"){.reference .internal}                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipCtxGetCacheConfig()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/context_management.html#_CPPv420hipCtxGetCacheConfigP14hipFuncCache_t "hipCtxGetCacheConfig"){.reference .internal}                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipCtxSetCacheConfig()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/context_management.html#_CPPv420hipCtxSetCacheConfig14hipFuncCache_t "hipCtxSetCacheConfig"){.reference .internal}                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipCtxSetSharedMemConfig()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/context_management.html#_CPPv424hipCtxSetSharedMemConfig18hipSharedMemConfig "hipCtxSetSharedMemConfig"){.reference .internal}       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipCtxGetSharedMemConfig()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/context_management.html#_CPPv424hipCtxGetSharedMemConfigP18hipSharedMemConfig "hipCtxGetSharedMemConfig"){.reference .internal}      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipCtxSynchronize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/context_management.html#_CPPv417hipCtxSynchronizev "hipCtxSynchronize"){.reference .internal}                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipCtxGetFlags()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/context_management.html#_CPPv414hipCtxGetFlagsPj "hipCtxGetFlags"){.reference .internal}                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipCtxEnablePeerAccess()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/context_management.html#_CPPv422hipCtxEnablePeerAccess8hipCtx_tj "hipCtxEnablePeerAccess"){.reference .internal}                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipCtxDisablePeerAccess()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/context_management.html#_CPPv423hipCtxDisablePeerAccess8hipCtx_t "hipCtxDisablePeerAccess"){.reference .internal}                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipDevicePrimaryCtxGetState()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/context_management.html#_CPPv427hipDevicePrimaryCtxGetState11hipDevice_tPjPi "hipDevicePrimaryCtxGetState"){.reference .internal} |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipDevicePrimaryCtxRelease()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/context_management.html#_CPPv426hipDevicePrimaryCtxRelease11hipDevice_t "hipDevicePrimaryCtxRelease"){.reference .internal}        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipDevicePrimaryCtxRetain()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/context_management.html#_CPPv425hipDevicePrimaryCtxRetainP8hipCtx_t11hipDevice_t "hipDevicePrimaryCtxRetain"){.reference .internal} |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipDevicePrimaryCtxReset()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/context_management.html#_CPPv424hipDevicePrimaryCtxReset11hipDevice_t "hipDevicePrimaryCtxReset"){.reference .internal}              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`hipDevicePrimaryCtxSetFlags()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](hip_runtime_api/modules/context_management.html#_CPPv427hipDevicePrimaryCtxSetFlags11hipDevice_tj "hipDevicePrimaryCtxSetFlags"){.reference .internal}    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

:
::::::::::::::::
::::::::::::::::::::::::::::::

{.bd-sidebar-secondary .bd-toc}
::
{.sidebar-secondary-items .sidebar-secondary__inner}
:
sidebar-secondary-item

{.page-toc .tocsection .onthispage}
Contents

:
::

:::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::
