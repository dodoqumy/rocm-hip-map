---
title: "Memory management (deprecated) &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/reference/hip_runtime_api/modules/memory_management/memory_management_deprecated.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T06:59:28.145160+00:00
content_hash: "bfe7b62512fcaf9d"
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
# Memory management (deprecated)

::
{#print-main-content}
:
{#jb-print-toc}

{}
## Contents

:
::

{#searchbox}

{#memory-management-deprecated .section}
[]{#memory-management-deprecated-reference}

# Memory management (deprecated)[\#](#memory-management-deprecated "Link to this heading"){.headerlink}

[]{#_CPPv313hipMallocHostPPv6size_t}[]{#_CPPv213hipMallocHostPPv6size_t}[]{#hipMallocHost__voidPP.s}[]{#group___memory_d_1ga66399e729223ff5b66ffc16297c0710e .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipMallocHost]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[ptr]{.pre}]{.n .sig-param}, [[size_t]{.pre}]{.n}[ ]{.w}[[size]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv413hipMallocHostPPv6size_t "Link to this definition"){.headerlink}\

:   Allocate pinned host memory \[Deprecated\].

    If size is 0, no memory is allocated, \*ptr returns nullptr, and hipSuccess is returned.

    
{.admonition .warning}
    Warning

    This API is deprecated, use [[hipHostMalloc()]{.std .std-ref}](../memory_management.html#group___memory_1gaad40bc7d97ccc799403ef5a9a8c246e1){.reference .internal} instead
    

    Parameters[:]{.colon}

    :   - **ptr** -- **\[out\]** Pointer to the allocated host pinned memory

        - **size** -- **\[in\]** Requested memory size

    Returns[:]{.colon}

    :   hipSuccess, hipErrorOutOfMemory

<!-- -->

[]{#_CPPv315hipMemAllocHostPPv6size_t}[]{#_CPPv215hipMemAllocHostPPv6size_t}[]{#hipMemAllocHost__voidPP.s}[]{#group___memory_d_1gaefab023bb8ec9b13a95b5362ab7c62d2 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipMemAllocHost]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[ptr]{.pre}]{.n .sig-param}, [[size_t]{.pre}]{.n}[ ]{.w}[[size]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv415hipMemAllocHostPPv6size_t "Link to this definition"){.headerlink}\

:   Allocate pinned host memory \[Deprecated\].

    If size is 0, no memory is allocated, \*ptr returns nullptr, and hipSuccess is returned.

    
{.admonition .warning}
    Warning

    This API is deprecated, use [[hipHostMalloc()]{.std .std-ref}](../memory_management.html#group___memory_1gaad40bc7d97ccc799403ef5a9a8c246e1){.reference .internal} instead
    

    Parameters[:]{.colon}

    :   - **ptr** -- **\[out\]** Pointer to the allocated host pinned memory

        - **size** -- **\[in\]** Requested memory size

    Returns[:]{.colon}

    :   hipSuccess, hipErrorOutOfMemory

<!-- -->

[]{#_CPPv311hipHostFreePv}[]{#_CPPv211hipHostFreePv}[]{#hipHostFree__voidP}[]{#group___memory_d_1ga2e543f58ee4544e317cd695d6d82e0a3 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipHostFree]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[ptr]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv411hipHostFreePv "Link to this definition"){.headerlink}\

:   Free memory allocated by the HIP-Clang hip host memory allocation API This API performs an implicit [[hipDeviceSynchronize()]{.std .std-ref}](../device_management.html#group___device_1gaefdc2847fb1d6c3fb1354e827a191ebd){.reference .internal} call. If pointer is NULL, the hip runtime is initialized and hipSuccess is returned.

    
{.admonition .seealso}
    See also

    [[hipMalloc]{.std .std-ref}](../memory_management.html#group___memory_1ga4c6fcfe80010069d2792780d00dcead2){.reference .internal}, [[hipMallocPitch]{.std .std-ref}](../memory_management.html#group___memory_1ga805c7320498926e444616fe090c727ee){.reference .internal}, [[hipFree]{.std .std-ref}](../memory_management.html#group___memory_1ga740d08da65cae1441ba32f8fedb863d1){.reference .internal}, [[hipMallocArray]{.std .std-ref}](../memory_management.html#group___memory_1ga8376a0644463118cd96432365bb470e3){.reference .internal}, [[hipFreeArray]{.std .std-ref}](../memory_management.html#group___memory_1gad6c25b3106fb47a2a75285ff2bd8cb29){.reference .internal}, [[hipMalloc3D]{.std .std-ref}](../memory_management.html#group___memory_1gad12f684263bbc92690553af2aa918fd9){.reference .internal}, [[hipMalloc3DArray]{.std .std-ref}](../memory_management.html#group___memory_1ga3be2acb8c75857958ddd1ab949ed4476){.reference .internal}, [[hipHostMalloc]{.std .std-ref}](../memory_management.html#group___memory_1gaad40bc7d97ccc799403ef5a9a8c246e1){.reference .internal}
    

    Parameters[:]{.colon}

    :   **ptr** -- **\[in\]** Pointer to memory to be freed

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue (if pointer is invalid, including device pointers allocated with hipMalloc)

<!-- -->

[]{#_CPPv316hipMemcpyToArray10hipArray_t6size_t6size_tPKv6size_t13hipMemcpyKind}[]{#_CPPv216hipMemcpyToArray10hipArray_t6size_t6size_tPKv6size_t13hipMemcpyKind}[]{#hipMemcpyToArray__hipArray_t.s.s.voidCP.s.hipMemcpyKind}[]{#group___memory_d_1ga835954048fd6cf0b4de065ada300d8ef .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipMemcpyToArray]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipArray_t]{.pre}]{.n}[ ]{.w}[[dst]{.pre}]{.n .sig-param}, [[size_t]{.pre}]{.n}[ ]{.w}[[wOffset]{.pre}]{.n .sig-param}, [[size_t]{.pre}]{.n}[ ]{.w}[[hOffset]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[src]{.pre}]{.n .sig-param}, [[size_t]{.pre}]{.n}[ ]{.w}[[count]{.pre}]{.n .sig-param}, [[hipMemcpyKind]{.pre}]{.n}[ ]{.w}[[kind]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv416hipMemcpyToArray10hipArray_t6size_t6size_tPKv6size_t13hipMemcpyKind "Link to this definition"){.headerlink}\

:   Copies data between host and device \[Deprecated\].

    
{.admonition .seealso}
    See also

    [[hipMemcpy]{.std .std-ref}](../memory_management.html#group___memory_1gac1a055d288302edd641c6d7416858e1e){.reference .internal}, [[hipMemcpy2DToArray]{.std .std-ref}](../memory_management.html#group___memory_1gaccf359cb35ce1887e6250c09e115e9a2){.reference .internal}, [[hipMemcpy2D]{.std .std-ref}](../memory_management.html#group___memory_1ga8af4597ff0cd17247d8a857c4d8bfa8a){.reference .internal}, [[hipMemcpyFromArray]{.std .std-ref}](#group___memory_d_1ga8c39c67c4ba098c6e6e116a9a4839a24){.reference .internal}, [[hipMemcpyToSymbol]{.std .std-ref}](../memory_management.html#group___memory_1gac0d988981c8535af1712f1f57436869b){.reference .internal}, [[hipMemcpyAsync]{.std .std-ref}](../memory_management.html#group___memory_1gad55fa9f5980b711bc93c52820149ba18){.reference .internal}
    

    
{.admonition .warning}
    Warning

    This API is deprecated.
    

    Parameters[:]{.colon}

    :   - **dst** -- **\[in\]** Destination memory address

        - **wOffset** -- **\[in\]** Destination starting X offset

        - **hOffset** -- **\[in\]** Destination starting Y offset

        - **src** -- **\[in\]** Source memory address

        - **count** -- **\[in\]** size in bytes to copy

        - **kind** -- **\[in\]** Type of transfer

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue, hipErrorInvalidPitchValue, hipErrorInvalidDevicePointer, hipErrorInvalidMemcpyDirection

<!-- -->

[]{#_CPPv318hipMemcpyFromArrayPv16hipArray_const_t6size_t6size_t6size_t13hipMemcpyKind}[]{#_CPPv218hipMemcpyFromArrayPv16hipArray_const_t6size_t6size_t6size_t13hipMemcpyKind}[]{#hipMemcpyFromArray__voidP.hipArray_const_t.s.s.s.hipMemcpyKind}[]{#group___memory_d_1ga8c39c67c4ba098c6e6e116a9a4839a24 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipMemcpyFromArray]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[dst]{.pre}]{.n .sig-param}, [[hipArray_const_t]{.pre}]{.n}[ ]{.w}[[srcArray]{.pre}]{.n .sig-param}, [[size_t]{.pre}]{.n}[ ]{.w}[[wOffset]{.pre}]{.n .sig-param}, [[size_t]{.pre}]{.n}[ ]{.w}[[hOffset]{.pre}]{.n .sig-param}, [[size_t]{.pre}]{.n}[ ]{.w}[[count]{.pre}]{.n .sig-param}, [[hipMemcpyKind]{.pre}]{.n}[ ]{.w}[[kind]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv418hipMemcpyFromArrayPv16hipArray_const_t6size_t6size_t6size_t13hipMemcpyKind "Link to this definition"){.headerlink}\

:   Copies data between host and device \[Deprecated\].

    
{.admonition .seealso}
    See also

    [[hipMemcpy]{.std .std-ref}](../memory_management.html#group___memory_1gac1a055d288302edd641c6d7416858e1e){.reference .internal}, [[hipMemcpy2DToArray]{.std .std-ref}](../memory_management.html#group___memory_1gaccf359cb35ce1887e6250c09e115e9a2){.reference .internal}, [[hipMemcpy2D]{.std .std-ref}](../memory_management.html#group___memory_1ga8af4597ff0cd17247d8a857c4d8bfa8a){.reference .internal}, [[hipMemcpyFromArray]{.std .std-ref}](#group___memory_d_1ga8c39c67c4ba098c6e6e116a9a4839a24){.reference .internal}, [[hipMemcpyToSymbol]{.std .std-ref}](../memory_management.html#group___memory_1gac0d988981c8535af1712f1f57436869b){.reference .internal}, [[hipMemcpyAsync]{.std .std-ref}](../memory_management.html#group___memory_1gad55fa9f5980b711bc93c52820149ba18){.reference .internal}
    

    
{.admonition .warning}
    Warning

    This API is deprecated.
    

    Parameters[:]{.colon}

    :   - **dst** -- **\[in\]** Destination memory address

        - **srcArray** -- **\[in\]** Source memory address

        - **wOffset** -- **\[in\]** Source starting X offset

        - **hOffset** -- **\[in\]** Source starting Y offset

        - **count** -- **\[in\]** Size in bytes to copy

        - **kind** -- **\[in\]** Type of transfer

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue, hipErrorInvalidPitchValue, hipErrorInvalidDevicePointer, hipErrorInvalidMemcpyDirection

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
