---
title: "Execution control &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/reference/hip_runtime_api/modules/execution_control.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T06:59:30.054443+00:00
content_hash: "3c2190026646ce82"
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
# Execution control

::
{#print-main-content}
:
{#jb-print-toc}

{}
## Contents

:
::

{#searchbox}

{#execution-control .section}
[]{#execution-control-reference}

# Execution control[\#](#execution-control "Link to this heading"){.headerlink}

[]{#_CPPv3IDpDpE17hipLaunchKernelExPK17hipLaunchConfig_tPFvDp10KernelArgsEDpRR6Params}[]{#_CPPv2IDpDpE17hipLaunchKernelExPK17hipLaunchConfig_tPFvDp10KernelArgsEDpRR6Params}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[typename]{.pre}]{.k}[ ]{.w}[[\...]{.pre}]{.p}[[[KernelArgs]{.pre}]{.n}]{.sig-name .descname}[[,]{.pre}]{.p}[ ]{.w}[[typename]{.pre}]{.k}[ ]{.w}[[\...]{.pre}]{.p}[[[Params]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
[]{#group___stream_o_1gab99b8d6fca7d769c7063de1d4acbb37e .target}[[static]{.pre}]{.k}[ ]{.w}[[inline]{.pre}]{.k}[ ]{.w}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipLaunchKernelEx]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[hipLaunchConfig_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[config]{.pre}]{.n .sig-param}, [[void]{.pre}]{.kt}[ ]{.w}[[(]{.pre}]{.p}[[\*]{.pre}]{.p}[[kernel]{.pre}]{.n .sig-param}[[)]{.pre}]{.p}[[(]{.pre}]{.p}[[[KernelArgs]{.pre}]{.n}](#_CPPv4IDpDpE17hipLaunchKernelEx10hipError_tPK17hipLaunchConfig_tPFvDp10KernelArgsEDpRR6Params "hipLaunchKernelEx::KernelArgs"){.reference .internal}[[\...]{.pre}]{.p}[[)]{.pre}]{.p}, [[[Params]{.pre}]{.n}](#_CPPv4IDpDpE17hipLaunchKernelEx10hipError_tPK17hipLaunchConfig_tPFvDp10KernelArgsEDpRR6Params "hipLaunchKernelEx::Params"){.reference .internal}[[&]{.pre}]{.p}[[&]{.pre}]{.p}[[\...]{.pre}]{.p}[ ]{.w}[[args]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv4IDpDpE17hipLaunchKernelEx10hipError_tPK17hipLaunchConfig_tPFvDp10KernelArgsEDpRR6Params "Link to this definition"){.headerlink}\

:   Launches a HIP kernel using the specified configuration.

    This function dispatches the provided kernel with the given launch configuration and forwards the kernel arguments.

    Parameters[:]{.colon}

    :   - **config** -- **\[in\]** Pointer to the kernel launch configuration structure.

        - **kernel** -- **\[in\]** Pointer to the device kernel function to be launched.

        - **args** -- **\[in\]** Variadic list of arguments to be passed to the kernel.

    Returns[:]{.colon}

    :   hipSuccess if the kernel is launched successfully, otherwise an appropriate error code.

<!-- -->

[]{#_CPPv324hipExtModuleLaunchKernel13hipFunction_t8uint32_t8uint32_t8uint32_t8uint32_t8uint32_t8uint32_t6size_t11hipStream_tPPvPPv10hipEvent_t10hipEvent_t8uint32_t}[]{#_CPPv224hipExtModuleLaunchKernel13hipFunction_t8uint32_t8uint32_t8uint32_t8uint32_t8uint32_t8uint32_t6size_t11hipStream_tPPvPPv10hipEvent_t10hipEvent_t8uint32_t}[]{#hipExtModuleLaunchKernel__hipFunction_t.uint32_t.uint32_t.uint32_t.uint32_t.uint32_t.uint32_t.s.hipStream_t.voidPP.voidPP.hipEvent_t.hipEvent_t.uint32_t}[]{#group___execution_1ga14d4fba7af1cdc9da9949031ebd187d2 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipExtModuleLaunchKernel]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipFunction_t]{.pre}]{.n}[ ]{.w}[[f]{.pre}]{.n .sig-param}, [[uint32_t]{.pre}]{.n}[ ]{.w}[[globalWorkSizeX]{.pre}]{.n .sig-param}, [[uint32_t]{.pre}]{.n}[ ]{.w}[[globalWorkSizeY]{.pre}]{.n .sig-param}, [[uint32_t]{.pre}]{.n}[ ]{.w}[[globalWorkSizeZ]{.pre}]{.n .sig-param}, [[uint32_t]{.pre}]{.n}[ ]{.w}[[localWorkSizeX]{.pre}]{.n .sig-param}, [[uint32_t]{.pre}]{.n}[ ]{.w}[[localWorkSizeY]{.pre}]{.n .sig-param}, [[uint32_t]{.pre}]{.n}[ ]{.w}[[localWorkSizeZ]{.pre}]{.n .sig-param}, [[size_t]{.pre}]{.n}[ ]{.w}[[sharedMemBytes]{.pre}]{.n .sig-param}, [[hipStream_t]{.pre}]{.n}[ ]{.w}[[hStream]{.pre}]{.n .sig-param}, [[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[kernelParams]{.pre}]{.n .sig-param}, [[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[extra]{.pre}]{.n .sig-param}, [[hipEvent_t]{.pre}]{.n}[ ]{.w}[[startEvent]{.pre}]{.n .sig-param}, [[hipEvent_t]{.pre}]{.n}[ ]{.w}[[stopEvent]{.pre}]{.n .sig-param}, [[uint32_t]{.pre}]{.n}[ ]{.w}[[flags]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv424hipExtModuleLaunchKernel13hipFunction_t8uint32_t8uint32_t8uint32_t8uint32_t8uint32_t8uint32_t6size_t11hipStream_tPPvPPv10hipEvent_t10hipEvent_t8uint32_t "Link to this definition"){.headerlink}\

:   Launches kernel with parameters and shared memory on stream with arguments passed to kernel params or extra arguments.

    HIP/ROCm actually updates the start event when the associated kernel completes. Currently, timing between startEvent and stopEvent does not include the time it takes to perform a system scope release/cache flush - only the time it takes to issues writes to cache.

    
{.admonition .note}
    Note

    For this HIP API, the flag 'hipExtAnyOrderLaunch' is not supported on AMD GFX9xx boards.
    

    Parameters[:]{.colon}

    :   - **f** -- **\[in\]** Kernel to launch.

        - **globalWorkSizeX** -- **\[in\]** X grid dimension specified in work-items.

        - **globalWorkSizeY** -- **\[in\]** Y grid dimension specified in work-items.

        - **globalWorkSizeZ** -- **\[in\]** Z grid dimension specified in work-items.

        - **localWorkSizeX** -- **\[in\]** X block dimension specified in work-items.

        - **localWorkSizeY** -- **\[in\]** Y block dimension specified in work-items.

        - **localWorkSizeZ** -- **\[in\]** Z block dimension specified in work-items.

        - **sharedMemBytes** -- **\[in\]** Amount of dynamic shared memory to allocate for this kernel. HIP-Clang compiler provides support for extern shared declarations.

        - **hStream** -- **\[in\]** Stream where the kernel should be dispatched. May be 0, in which case the default stream is used with associated synchronization rules.

        - **kernelParams** -- **\[in\]** pointer to kernel parameters.

        - **extra** -- **\[in\]** Pointer to kernel arguments. These are passed directly to the kernel and must be in the memory layout and alignment expected by the kernel. All passed arguments must be naturally aligned according to their type. The memory address of each argument should be a multiple of its size in bytes. Please refer to hip_porting_driver_api.md for sample usage.

        - **startEvent** -- **\[in\]** If non-null, specified event will be updated to track the start time of the kernel launch. The event must be created before calling this API.

        - **stopEvent** -- **\[in\]** If non-null, specified event will be updated to track the stop time of the kernel launch. The event must be created before calling this API.

        - **flags** -- **\[in\]** The value of hipExtAnyOrderLaunch, signifies if kernel can be launched in any order.

    Returns[:]{.colon}

    :   hipSuccess, hipInvalidDeviceId, hipErrorNotInitialized, hipErrorInvalidValue.

<!-- -->

[]{#_CPPv324hipHccModuleLaunchKernel13hipFunction_t8uint32_t8uint32_t8uint32_t8uint32_t8uint32_t8uint32_t6size_t11hipStream_tPPvPPv10hipEvent_t10hipEvent_t}[]{#_CPPv224hipHccModuleLaunchKernel13hipFunction_t8uint32_t8uint32_t8uint32_t8uint32_t8uint32_t8uint32_t6size_t11hipStream_tPPvPPv10hipEvent_t10hipEvent_t}[]{#hipHccModuleLaunchKernel__hipFunction_t.uint32_t.uint32_t.uint32_t.uint32_t.uint32_t.uint32_t.s.hipStream_t.voidPP.voidPP.hipEvent_t.hipEvent_t}[]{#group___execution_1ga0977a04384013028d822eb0c6b5cf901 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipHccModuleLaunchKernel]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipFunction_t]{.pre}]{.n}[ ]{.w}[[f]{.pre}]{.n .sig-param}, [[uint32_t]{.pre}]{.n}[ ]{.w}[[globalWorkSizeX]{.pre}]{.n .sig-param}, [[uint32_t]{.pre}]{.n}[ ]{.w}[[globalWorkSizeY]{.pre}]{.n .sig-param}, [[uint32_t]{.pre}]{.n}[ ]{.w}[[globalWorkSizeZ]{.pre}]{.n .sig-param}, [[uint32_t]{.pre}]{.n}[ ]{.w}[[localWorkSizeX]{.pre}]{.n .sig-param}, [[uint32_t]{.pre}]{.n}[ ]{.w}[[localWorkSizeY]{.pre}]{.n .sig-param}, [[uint32_t]{.pre}]{.n}[ ]{.w}[[localWorkSizeZ]{.pre}]{.n .sig-param}, [[size_t]{.pre}]{.n}[ ]{.w}[[sharedMemBytes]{.pre}]{.n .sig-param}, [[hipStream_t]{.pre}]{.n}[ ]{.w}[[hStream]{.pre}]{.n .sig-param}, [[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[kernelParams]{.pre}]{.n .sig-param}, [[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[extra]{.pre}]{.n .sig-param}, [[hipEvent_t]{.pre}]{.n}[ ]{.w}[[startEvent]{.pre}]{.n .sig-param}, [[hipEvent_t]{.pre}]{.n}[ ]{.w}[[stopEvent]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv424hipHccModuleLaunchKernel13hipFunction_t8uint32_t8uint32_t8uint32_t8uint32_t8uint32_t8uint32_t6size_t11hipStream_tPPvPPv10hipEvent_t10hipEvent_t "Link to this definition"){.headerlink}\

:   This HIP API is deprecated, please use [[hipExtModuleLaunchKernel()]{.std .std-ref}](#group___execution_1ga14d4fba7af1cdc9da9949031ebd187d2){.reference .internal} instead.

<!-- -->

[]{#_CPPv318hipExtLaunchKernelPKv4dim34dim3PPv6size_t11hipStream_t10hipEvent_t10hipEvent_ti}[]{#_CPPv218hipExtLaunchKernelPKv4dim34dim3PPv6size_t11hipStream_t10hipEvent_t10hipEvent_ti}[]{#hipExtLaunchKernel__voidCP.dim3.dim3.voidPP.s.hipStream_t.hipEvent_t.hipEvent_t.i}[]{#group___execution_1ga601d372753e668aba188e2466c414bbd .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipExtLaunchKernel]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[function_address]{.pre}]{.n .sig-param}, [[dim3]{.pre}]{.n}[ ]{.w}[[numBlocks]{.pre}]{.n .sig-param}, [[dim3]{.pre}]{.n}[ ]{.w}[[dimBlocks]{.pre}]{.n .sig-param}, [[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[args]{.pre}]{.n .sig-param}, [[size_t]{.pre}]{.n}[ ]{.w}[[sharedMemBytes]{.pre}]{.n .sig-param}, [[hipStream_t]{.pre}]{.n}[ ]{.w}[[stream]{.pre}]{.n .sig-param}, [[hipEvent_t]{.pre}]{.n}[ ]{.w}[[startEvent]{.pre}]{.n .sig-param}, [[hipEvent_t]{.pre}]{.n}[ ]{.w}[[stopEvent]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[flags]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv418hipExtLaunchKernelPKv4dim34dim3PPv6size_t11hipStream_t10hipEvent_t10hipEvent_ti "Link to this definition"){.headerlink}\

:   Launches kernel from the pointer address, with arguments and shared memory on stream.

    Parameters[:]{.colon}

    :   - **function_address** -- **\[in\]** pointer to the Kernel to launch.

        - **numBlocks** -- **\[in\]** number of blocks.

        - **dimBlocks** -- **\[in\]** dimension of a block.

        - **args** -- **\[in\]** pointer to kernel arguments.

        - **sharedMemBytes** -- **\[in\]** Amount of dynamic shared memory to allocate for this kernel. HIP-Clang compiler provides support for extern shared declarations.

        - **stream** -- **\[in\]** Stream where the kernel should be dispatched. May be 0, in which case the default stream is used with associated synchronization rules.

        - **startEvent** -- **\[in\]** If non-null, specified event will be updated to track the start time of the kernel launch. The event must be created before calling this API.

        - **stopEvent** -- **\[in\]** If non-null, specified event will be updated to track the stop time of the kernel launch. The event must be created before calling this API.

        - **flags** -- **\[in\]** The value of hipExtAnyOrderLaunch, signifies if kernel can be launched in any order.

    Returns[:]{.colon}

    :   hipSuccess, hipInvalidDeviceId, hipErrorNotInitialized, hipErrorInvalidValue.

<!-- -->

[]{#_CPPv3IDp0E21hipExtLaunchKernelGGL1FRK4dim3RK4dim3NSt8uint32_tE11hipStream_t10hipEvent_t10hipEvent_tNSt8uint32_tEDp4Args}[]{#_CPPv2IDp0E21hipExtLaunchKernelGGL1FRK4dim3RK4dim3NSt8uint32_tE11hipStream_t10hipEvent_t10hipEvent_tNSt8uint32_tEDp4Args}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[typename]{.pre}]{.k}[ ]{.w}[[\...]{.pre}]{.p}[[[Args]{.pre}]{.n}]{.sig-name .descname}[[,]{.pre}]{.p}[ ]{.w}[[typename]{.pre}]{.k}[ ]{.w}[[[F]{.pre}]{.n}]{.sig-name .descname}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[void]{.pre}]{.kt}[ ]{.w}[[(]{.pre}]{.p}[[\*]{.pre}]{.p}[[)]{.pre}]{.p}[[(]{.pre}]{.p}[[[Args]{.pre}]{.n}](#_CPPv4IDp0E21hipExtLaunchKernelGGLv1FRK4dim3RK4dim3NSt8uint32_tE11hipStream_t10hipEvent_t10hipEvent_tNSt8uint32_tEDp4Args "hipExtLaunchKernelGGL::Args"){.reference .internal}[[\...]{.pre}]{.p}[[)]{.pre}]{.p}[[\>]{.pre}]{.p}\
[]{#group___execution_1ga82a15dac5d1205c69c20d84245078bf6 .target}[[inline]{.pre}]{.k}[ ]{.w}[[void]{.pre}]{.kt}[ ]{.w}[[[hipExtLaunchKernelGGL]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[[F]{.pre}]{.n}](#_CPPv4IDp0E21hipExtLaunchKernelGGLv1FRK4dim3RK4dim3NSt8uint32_tE11hipStream_t10hipEvent_t10hipEvent_tNSt8uint32_tEDp4Args "hipExtLaunchKernelGGL::F"){.reference .internal}[ ]{.w}[[kernel]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[dim3]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[numBlocks]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[dim3]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[dimBlocks]{.pre}]{.n .sig-param}, [[std]{.pre}]{.n}[[::]{.pre}]{.p}[[uint32_t]{.pre}]{.n}[ ]{.w}[[sharedMemBytes]{.pre}]{.n .sig-param}, [[hipStream_t]{.pre}]{.n}[ ]{.w}[[stream]{.pre}]{.n .sig-param}, [[hipEvent_t]{.pre}]{.n}[ ]{.w}[[startEvent]{.pre}]{.n .sig-param}, [[hipEvent_t]{.pre}]{.n}[ ]{.w}[[stopEvent]{.pre}]{.n .sig-param}, [[std]{.pre}]{.n}[[::]{.pre}]{.p}[[uint32_t]{.pre}]{.n}[ ]{.w}[[flags]{.pre}]{.n .sig-param}, [[[Args]{.pre}]{.n}](#_CPPv4IDp0E21hipExtLaunchKernelGGLv1FRK4dim3RK4dim3NSt8uint32_tE11hipStream_t10hipEvent_t10hipEvent_tNSt8uint32_tEDp4Args "hipExtLaunchKernelGGL::Args"){.reference .internal}[[\...]{.pre}]{.p}[ ]{.w}[[args]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv4IDp0E21hipExtLaunchKernelGGLv1FRK4dim3RK4dim3NSt8uint32_tE11hipStream_t10hipEvent_t10hipEvent_tNSt8uint32_tEDp4Args "Link to this definition"){.headerlink}\

:   Launches kernel with dimention parameters and shared memory on stream with templated kernel and arguments.

    Parameters[:]{.colon}

    :   - **kernel** -- **\[in\]** Kernel to launch.

        - **numBlocks** -- **\[in\]** const number of blocks.

        - **dimBlocks** -- **\[in\]** const dimension of a block.

        - **sharedMemBytes** -- **\[in\]** Amount of dynamic shared memory to allocate for this kernel. HIP-Clang compiler provides support for extern shared declarations.

        - **stream** -- **\[in\]** Stream where the kernel should be dispatched. May be 0, in which case the default stream is used with associated synchronization rules.

        - **startEvent** -- **\[in\]** If non-null, specified event will be updated to track the start time of the kernel launch. The event must be created before calling this API.

        - **stopEvent** -- **\[in\]** If non-null, specified event will be updated to track the stop time of the kernel launch. The event must be created before calling this API.

        - **flags** -- **\[in\]** The value of hipExtAnyOrderLaunch, signifies if kernel can be launched in any order.

        - **args** -- **\[in\]** templated kernel arguments.

<!-- -->

[]{#_CPPv319hipFuncSetAttributePKv16hipFuncAttributei}[]{#_CPPv219hipFuncSetAttributePKv16hipFuncAttributei}[]{#hipFuncSetAttribute__voidCP.hipFuncAttribute.i}[]{#group___execution_1ga8417deea9092f35e497bc7e19bd5e12d .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipFuncSetAttribute]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[func]{.pre}]{.n .sig-param}, [[hipFuncAttribute]{.pre}]{.n}[ ]{.w}[[attr]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[value]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv419hipFuncSetAttributePKv16hipFuncAttributei "Link to this definition"){.headerlink}\

:   Set attribute for a specific function.

    Note: AMD devices and some Nvidia GPUS do not support shared cache banking, and the hint is ignored on those architectures.

    Parameters[:]{.colon}

    :   - **func** -- **\[in\]** Pointer of the function

        - **attr** -- **\[in\]** Attribute to set

        - **value** -- **\[in\]** Value to set

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidDeviceFunction, hipErrorInvalidValue

<!-- -->

[]{#_CPPv321hipFuncSetCacheConfigPKv14hipFuncCache_t}[]{#_CPPv221hipFuncSetCacheConfigPKv14hipFuncCache_t}[]{#hipFuncSetCacheConfig__voidCP.hipFuncCache_t}[]{#group___execution_1gafdb33ef569eb89808fc5178d04b508ba .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipFuncSetCacheConfig]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[func]{.pre}]{.n .sig-param}, [[hipFuncCache_t]{.pre}]{.n}[ ]{.w}[[config]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv421hipFuncSetCacheConfigPKv14hipFuncCache_t "Link to this definition"){.headerlink}\

:   Set Cache configuration for a specific function.

    Parameters[:]{.colon}

    :   - **func** -- **\[in\]** Pointer of the function.

        - **config** -- **\[in\]** Configuration to set.

    Returns[:]{.colon}

    :   hipSuccess, hipErrorNotInitialized Note: AMD devices and some Nvidia GPUS do not support reconfigurable cache. This hint is ignored on those architectures.

<!-- -->

[]{#_CPPv325hipFuncSetSharedMemConfigPKv18hipSharedMemConfig}[]{#_CPPv225hipFuncSetSharedMemConfigPKv18hipSharedMemConfig}[]{#hipFuncSetSharedMemConfig__voidCP.hipSharedMemConfig}[]{#group___execution_1ga36b1d09bfb54678df0c7dc1066ec029c .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipFuncSetSharedMemConfig]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[func]{.pre}]{.n .sig-param}, [[hipSharedMemConfig]{.pre}]{.n}[ ]{.w}[[config]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv425hipFuncSetSharedMemConfigPKv18hipSharedMemConfig "Link to this definition"){.headerlink}\

:   Set shared memory configuation for a specific function.

    Note: AMD devices and some Nvidia GPUS do not support shared cache banking, and the hint is ignored on those architectures.

    Parameters[:]{.colon}

    :   - **func** -- **\[in\]** Pointer of the function

        - **config** -- **\[in\]** Configuration

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidDeviceFunction, hipErrorInvalidValue

<!-- -->

[]{#_CPPv320hipFuncGetAttributesP17hipFuncAttributesPKv}[]{#_CPPv220hipFuncGetAttributesP17hipFuncAttributesPKv}[]{#hipFuncGetAttributes__hipFuncAttributesP.voidCP}[]{#group___execution_1ga18a72890686975fdd46c7c8a7bb5a607 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipFuncGetAttributes]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[struct]{.pre}]{.k}[ ]{.w}[[hipFuncAttributes]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[attr]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[func]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv420hipFuncGetAttributesP17hipFuncAttributesPKv "Link to this definition"){.headerlink}\

:   Find out attributes for a given function.

    Parameters[:]{.colon}

    :   - **attr** -- **\[out\]** Attributes of funtion

        - **func** -- **\[in\]** Pointer to the function handle

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue, hipErrorInvalidDeviceFunction

<!-- -->

[]{#_CPPv319hipFuncGetAttributePi21hipFunction_attribute13hipFunction_t}[]{#_CPPv219hipFuncGetAttributePi21hipFunction_attribute13hipFunction_t}[]{#hipFuncGetAttribute__iP.hipFunction_attribute.hipFunction_t}[]{#group___execution_1ga488a7f867a3e46015659b5665071d2eb .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipFuncGetAttribute]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[value]{.pre}]{.n .sig-param}, [[hipFunction_attribute]{.pre}]{.n}[ ]{.w}[[attrib]{.pre}]{.n .sig-param}, [[hipFunction_t]{.pre}]{.n}[ ]{.w}[[hfunc]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv419hipFuncGetAttributePi21hipFunction_attribute13hipFunction_t "Link to this definition"){.headerlink}\

:   Find out a specific attribute for a given function.

    Parameters[:]{.colon}

    :   - **value** -- **\[out\]** Pointer to the value

        - **attrib** -- **\[in\]** Attributes of the given funtion

        - **hfunc** -- **\[in\]** Function to get attributes from

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue, hipErrorInvalidDeviceFunction

<!-- -->

[]{#_CPPv321hipModuleLaunchKernel13hipFunction_tjjjjjjj11hipStream_tPPvPPv}[]{#_CPPv221hipModuleLaunchKernel13hipFunction_tjjjjjjj11hipStream_tPPvPPv}[]{#hipModuleLaunchKernel__hipFunction_t.unsigned-i.unsigned-i.unsigned-i.unsigned-i.unsigned-i.unsigned-i.unsigned-i.hipStream_t.voidPP.voidPP}[]{#group___execution_1ga2e4de5937aa8171e9eda16c881ed0674 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipModuleLaunchKernel]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipFunction_t]{.pre}]{.n}[ ]{.w}[[f]{.pre}]{.n .sig-param}, [[unsigned]{.pre}]{.kt}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[gridDimX]{.pre}]{.n .sig-param}, [[unsigned]{.pre}]{.kt}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[gridDimY]{.pre}]{.n .sig-param}, [[unsigned]{.pre}]{.kt}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[gridDimZ]{.pre}]{.n .sig-param}, [[unsigned]{.pre}]{.kt}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[blockDimX]{.pre}]{.n .sig-param}, [[unsigned]{.pre}]{.kt}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[blockDimY]{.pre}]{.n .sig-param}, [[unsigned]{.pre}]{.kt}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[blockDimZ]{.pre}]{.n .sig-param}, [[unsigned]{.pre}]{.kt}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[sharedMemBytes]{.pre}]{.n .sig-param}, [[hipStream_t]{.pre}]{.n}[ ]{.w}[[stream]{.pre}]{.n .sig-param}, [[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[kernelParams]{.pre}]{.n .sig-param}, [[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[extra]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv421hipModuleLaunchKernel13hipFunction_tjjjjjjj11hipStream_tPPvPPv "Link to this definition"){.headerlink}\

:   launches kernel f with launch parameters and shared memory on stream with arguments passed to kernelparams or extra

    Please note, HIP does not support kernel launch with total work items defined in dimension with size gridDim x blockDim \>= 2\^32. So gridDim.x \* blockDim.x, gridDim.y \* blockDim.y and gridDim.z \* blockDim.z are always less than 2\^32.

    Parameters[:]{.colon}

    :   - **f** -- **\[in\]** Kernel to launch.

        - **gridDimX** -- **\[in\]** X grid dimension specified as multiple of blockDimX.

        - **gridDimY** -- **\[in\]** Y grid dimension specified as multiple of blockDimY.

        - **gridDimZ** -- **\[in\]** Z grid dimension specified as multiple of blockDimZ.

        - **blockDimX** -- **\[in\]** X block dimensions specified in work-items

        - **blockDimY** -- **\[in\]** Y grid dimension specified in work-items

        - **blockDimZ** -- **\[in\]** Z grid dimension specified in work-items

        - **sharedMemBytes** -- **\[in\]** Amount of dynamic shared memory to allocate for this kernel. The HIP-Clang compiler provides support for extern shared declarations.

        - **stream** -- **\[in\]** Stream where the kernel should be dispatched. May be 0, in which case th default stream is used with associated synchronization rules.

        - **kernelParams** -- **\[in\]** Kernel parameters to launch

        - **extra** -- **\[in\]** Pointer to kernel arguments. These are passed directly to the kernel and must be in the memory layout and alignment expected by the kernel. All passed arguments must be naturally aligned according to their type. The memory address of each argument should be a multiple of its size in bytes. Please refer to hip_porting_driver_api.md for sample usage.

    Returns[:]{.colon}

    :   hipSuccess, hipErrorNotInitialized, hipErrorInvalidValue

<!-- -->

[]{#_CPPv334hipExtLaunchMultiKernelMultiDeviceP15hipLaunchParamsij}[]{#_CPPv234hipExtLaunchMultiKernelMultiDeviceP15hipLaunchParamsij}[]{#hipExtLaunchMultiKernelMultiDevice__hipLaunchParamsP.i.unsigned-i}[]{#group___execution_1ga24070776eacdf32ba3c4f339315df6ff .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipExtLaunchMultiKernelMultiDevice]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipLaunchParams]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[launchParamsList]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[numDevices]{.pre}]{.n .sig-param}, [[unsigned]{.pre}]{.kt}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[flags]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv434hipExtLaunchMultiKernelMultiDeviceP15hipLaunchParamsij "Link to this definition"){.headerlink}\

:   Launches kernels on multiple devices and guarantees all specified kernels are dispatched on respective streams before enqueuing any other work on the specified streams from any other threads.

    Parameters[:]{.colon}

    :   - **launchParamsList** -- **\[in\]** List of launch parameters, one per device.

        - **numDevices** -- **\[in\]** Size of the launchParamsList array.

        - **flags** -- **\[in\]** Flags to control launch behavior.

    Returns[:]{.colon}

    :   hipSuccess, hipErrorNotInitialized, hipErrorInvalidValue

<!-- -->

[]{#_CPPv318hipLaunchKernelExCPK17hipLaunchConfig_tPKvPPv}[]{#_CPPv218hipLaunchKernelExCPK17hipLaunchConfig_tPKvPPv}[]{#hipLaunchKernelExC__hipLaunchConfig_tCP.voidCP.voidPP}[]{#group___execution_1ga20d5257a68cc6c80c06745f001b0c218 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipLaunchKernelExC]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[hipLaunchConfig_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[config]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[fPtr]{.pre}]{.n .sig-param}, [[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[args]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv418hipLaunchKernelExCPK17hipLaunchConfig_tPKvPPv "Link to this definition"){.headerlink}\

:   Launches a HIP kernel using a generic function pointer and the specified configuration.

    This function is equivalent to hipLaunchKernelEx but accepts the kernel as a generic function pointer.

    Parameters[:]{.colon}

    :   - **config** -- **\[in\]** Pointer to the kernel launch configuration structure.

        - **fPtr** -- **\[in\]** Pointer to the device kernel function.

        - **args** -- **\[in\]** Array of pointers to the kernel arguments.

    Returns[:]{.colon}

    :   hipSuccess if the kernel is launched successfully, otherwise an appropriate error code.

<!-- -->

[]{#_CPPv320hipDrvLaunchKernelExPK17HIP_LAUNCH_CONFIG13hipFunction_tPPvPPv}[]{#_CPPv220hipDrvLaunchKernelExPK17HIP_LAUNCH_CONFIG13hipFunction_tPPvPPv}[]{#hipDrvLaunchKernelEx__HIP_LAUNCH_CONFIGCP.hipFunction_t.voidPP.voidPP}[]{#group___execution_1ga8f44c3147df2b58c8c5b8d5802674df5 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipDrvLaunchKernelEx]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[HIP_LAUNCH_CONFIG]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[config]{.pre}]{.n .sig-param}, [[hipFunction_t]{.pre}]{.n}[ ]{.w}[[f]{.pre}]{.n .sig-param}, [[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[params]{.pre}]{.n .sig-param}, [[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[extra]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv420hipDrvLaunchKernelExPK17HIP_LAUNCH_CONFIG13hipFunction_tPPvPPv "Link to this definition"){.headerlink}\

:   Launches a HIP kernel using the driver API with the specified configuration.

    This function dispatches the device kernel represented by a HIP function object. It passes both the kernel parameters and any extra configuration arguments to the kernel launch.

    Parameters[:]{.colon}

    :   - **config** -- **\[in\]** Pointer to the kernel launch configuration structure.

        - **f** -- **\[in\]** HIP function object representing the device kernel to be launched.

        - **params** -- **\[in\]** Array of pointers to the kernel parameters.

        - **extra** -- **\[in\]** Array of pointers for additional launch parameters or extra configuration data.

    Returns[:]{.colon}

    :   hipSuccess if the kernel is launched successfully, otherwise an appropriate error code.

<!-- -->

[]{#_CPPv3I0E34hipExtLaunchMultiKernelMultiDeviceP15hipLaunchParamsjj}[]{#_CPPv2I0E34hipExtLaunchMultiKernelMultiDeviceP15hipLaunchParamsjj}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
[]{#group___execution_1ga8c7a8d2a8157f472f6554f312bba9bed .target}[[inline]{.pre}]{.k}[ ]{.w}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipExtLaunchMultiKernelMultiDevice]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipLaunchParams]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[launchParamsList]{.pre}]{.n .sig-param}, [[unsigned]{.pre}]{.kt}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[numDevices]{.pre}]{.n .sig-param}, [[unsigned]{.pre}]{.kt}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[flags]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[0]{.pre}]{.m}[)]{.sig-paren}[\#](#_CPPv4I0E34hipExtLaunchMultiKernelMultiDevice10hipError_tP15hipLaunchParamsjj "Link to this definition"){.headerlink}\

:   Launches kernels on multiple devices and guarantees all specified kernels are dispatched on respective streams before enqueuing any other work on the specified streams from any other threads.

    Parameters[:]{.colon}

    :   - **launchParamsList** -- **\[in\]** List of launch parameters, one per device.

        - **numDevices** -- **\[in\]** Size of the launchParamsList array.

        - **flags** -- **\[in\]** Flags to control launch behavior.

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue

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
