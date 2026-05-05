---
title: "Texture management &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/reference/hip_runtime_api/modules/memory_management/texture_management.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T06:58:55.463063+00:00
content_hash: "e42360dd17340c87"
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
# Texture management

::
{#print-main-content}
:
{#jb-print-toc}

{}
## Contents

:
::

{#searchbox}

{#texture-management .section}
[]{#texture-management-reference}

# Texture management[\#](#texture-management "Link to this heading"){.headerlink}

[]{#_CPPv322hipCreateTextureObjectP18hipTextureObject_tPK15hipResourceDescPK14hipTextureDescPK19hipResourceViewDesc}[]{#_CPPv222hipCreateTextureObjectP18hipTextureObject_tPK15hipResourceDescPK14hipTextureDescPK19hipResourceViewDesc}[]{#hipCreateTextureObject__hipTextureObject_tP.hipResourceDescCP.hipTextureDescCP.hipResourceViewDescCP}[]{#group___texture_1ga8118c199ca3f347b5b5fd919bb624801 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipCreateTextureObject]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipTextureObject_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[pTexObject]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[hipResourceDesc]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[pResDesc]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[hipTextureDesc]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[pTexDesc]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[struct]{.pre}]{.k}[ ]{.w}[[hipResourceViewDesc]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[pResViewDesc]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv422hipCreateTextureObjectP18hipTextureObject_tPK15hipResourceDescPK14hipTextureDescPK19hipResourceViewDesc "Link to this definition"){.headerlink}\

:   Creates a texture object.

    
{.admonition .note}
    Note

    3D linear filter isn't supported on GFX90A boards, on which the API [`hipCreateTextureObject`{.docutils .literal .notranslate}]{.pre} will return hipErrorNotSupported.
    

    Parameters[:]{.colon}

    :   - **pTexObject** -- **\[out\]** pointer to the texture object to create

        - **pResDesc** -- **\[in\]** pointer to resource descriptor

        - **pTexDesc** -- **\[in\]** pointer to texture descriptor

        - **pResViewDesc** -- **\[in\]** pointer to resource view descriptor

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue, hipErrorNotSupported, hipErrorOutOfMemory

<!-- -->

[]{#_CPPv323hipDestroyTextureObject18hipTextureObject_t}[]{#_CPPv223hipDestroyTextureObject18hipTextureObject_t}[]{#hipDestroyTextureObject__hipTextureObject_t}[]{#group___texture_1gad62c874fe1ae049c9e93a83623b3a82f .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipDestroyTextureObject]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipTextureObject_t]{.pre}]{.n}[ ]{.w}[[textureObject]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv423hipDestroyTextureObject18hipTextureObject_t "Link to this definition"){.headerlink}\

:   Destroys a texture object.

    Parameters[:]{.colon}

    :   **textureObject** -- **\[in\]** texture object to destroy

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue

<!-- -->

[]{#_CPPv317hipGetChannelDescP20hipChannelFormatDesc16hipArray_const_t}[]{#_CPPv217hipGetChannelDescP20hipChannelFormatDesc16hipArray_const_t}[]{#hipGetChannelDesc__hipChannelFormatDescP.hipArray_const_t}[]{#group___texture_1gab87485da6ded39aed13c062a4570f316 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipGetChannelDesc]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipChannelFormatDesc]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[desc]{.pre}]{.n .sig-param}, [[hipArray_const_t]{.pre}]{.n}[ ]{.w}[[array]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv417hipGetChannelDescP20hipChannelFormatDesc16hipArray_const_t "Link to this definition"){.headerlink}\

:   Gets the channel descriptor in an array.

    Parameters[:]{.colon}

    :   - **desc** -- **\[in\]** pointer to channel format descriptor

        - **array** -- **\[out\]** memory array on the device

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue

<!-- -->

[]{#_CPPv331hipGetTextureObjectResourceDescP15hipResourceDesc18hipTextureObject_t}[]{#_CPPv231hipGetTextureObjectResourceDescP15hipResourceDesc18hipTextureObject_t}[]{#hipGetTextureObjectResourceDesc__hipResourceDescP.hipTextureObject_t}[]{#group___texture_1ga5eb7e8f8a486500243cb43b0a3d11d06 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipGetTextureObjectResourceDesc]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipResourceDesc]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[pResDesc]{.pre}]{.n .sig-param}, [[hipTextureObject_t]{.pre}]{.n}[ ]{.w}[[textureObject]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv431hipGetTextureObjectResourceDescP15hipResourceDesc18hipTextureObject_t "Link to this definition"){.headerlink}\

:   Gets resource descriptor for the texture object.

    Parameters[:]{.colon}

    :   - **pResDesc** -- **\[out\]** pointer to resource descriptor

        - **textureObject** -- **\[in\]** texture object

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue

<!-- -->

[]{#_CPPv335hipGetTextureObjectResourceViewDescP19hipResourceViewDesc18hipTextureObject_t}[]{#_CPPv235hipGetTextureObjectResourceViewDescP19hipResourceViewDesc18hipTextureObject_t}[]{#hipGetTextureObjectResourceViewDesc__hipResourceViewDescP.hipTextureObject_t}[]{#group___texture_1ga748e53ac1b10eb11d41efab0de154966 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipGetTextureObjectResourceViewDesc]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[struct]{.pre}]{.k}[ ]{.w}[[hipResourceViewDesc]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[pResViewDesc]{.pre}]{.n .sig-param}, [[hipTextureObject_t]{.pre}]{.n}[ ]{.w}[[textureObject]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv435hipGetTextureObjectResourceViewDescP19hipResourceViewDesc18hipTextureObject_t "Link to this definition"){.headerlink}\

:   Gets resource view descriptor for the texture object.

    Parameters[:]{.colon}

    :   - **pResViewDesc** -- **\[out\]** pointer to resource view descriptor

        - **textureObject** -- **\[in\]** texture object

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue

<!-- -->

[]{#_CPPv330hipGetTextureObjectTextureDescP14hipTextureDesc18hipTextureObject_t}[]{#_CPPv230hipGetTextureObjectTextureDescP14hipTextureDesc18hipTextureObject_t}[]{#hipGetTextureObjectTextureDesc__hipTextureDescP.hipTextureObject_t}[]{#group___texture_1gaf14cf44212e7191a2553d4d09e4fd665 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipGetTextureObjectTextureDesc]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipTextureDesc]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[pTexDesc]{.pre}]{.n .sig-param}, [[hipTextureObject_t]{.pre}]{.n}[ ]{.w}[[textureObject]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv430hipGetTextureObjectTextureDescP14hipTextureDesc18hipTextureObject_t "Link to this definition"){.headerlink}\

:   Gets texture descriptor for the texture object.

    Parameters[:]{.colon}

    :   - **pTexDesc** -- **\[out\]** pointer to texture descriptor

        - **textureObject** -- **\[in\]** texture object

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue

<!-- -->

[]{#_CPPv318hipTexObjectCreateP18hipTextureObject_tPK17HIP_RESOURCE_DESCPK16HIP_TEXTURE_DESCPK22HIP_RESOURCE_VIEW_DESC}[]{#_CPPv218hipTexObjectCreateP18hipTextureObject_tPK17HIP_RESOURCE_DESCPK16HIP_TEXTURE_DESCPK22HIP_RESOURCE_VIEW_DESC}[]{#hipTexObjectCreate__hipTextureObject_tP.HIP_RESOURCE_DESCCP.HIP_TEXTURE_DESCCP.HIP_RESOURCE_VIEW_DESCCP}[]{#group___texture_1ga59d6d76f9ea1e4f58eb3b86958ae1ee4 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipTexObjectCreate]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipTextureObject_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[pTexObject]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[HIP_RESOURCE_DESC]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[pResDesc]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[HIP_TEXTURE_DESC]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[pTexDesc]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[HIP_RESOURCE_VIEW_DESC]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[pResViewDesc]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv418hipTexObjectCreateP18hipTextureObject_tPK17HIP_RESOURCE_DESCPK16HIP_TEXTURE_DESCPK22HIP_RESOURCE_VIEW_DESC "Link to this definition"){.headerlink}\

:   Creates a texture object.

    Parameters[:]{.colon}

    :   - **pTexObject** -- **\[out\]** pointer to texture object to create

        - **pResDesc** -- **\[in\]** pointer to resource descriptor

        - **pTexDesc** -- **\[in\]** pointer to texture descriptor

        - **pResViewDesc** -- **\[in\]** pointer to resource view descriptor

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue

<!-- -->

[]{#_CPPv319hipTexObjectDestroy18hipTextureObject_t}[]{#_CPPv219hipTexObjectDestroy18hipTextureObject_t}[]{#hipTexObjectDestroy__hipTextureObject_t}[]{#group___texture_1ga9df0487a59efcdb063feecb770fa56c2 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipTexObjectDestroy]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipTextureObject_t]{.pre}]{.n}[ ]{.w}[[texObject]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv419hipTexObjectDestroy18hipTextureObject_t "Link to this definition"){.headerlink}\

:   Destroys a texture object.

    Parameters[:]{.colon}

    :   **texObject** -- **\[in\]** texture object to destroy

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue

<!-- -->

[]{#_CPPv327hipTexObjectGetResourceDescP17HIP_RESOURCE_DESC18hipTextureObject_t}[]{#_CPPv227hipTexObjectGetResourceDescP17HIP_RESOURCE_DESC18hipTextureObject_t}[]{#hipTexObjectGetResourceDesc__HIP_RESOURCE_DESCP.hipTextureObject_t}[]{#group___texture_1gac136126d65935da5ca274ac628aa67a4 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipTexObjectGetResourceDesc]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[HIP_RESOURCE_DESC]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[pResDesc]{.pre}]{.n .sig-param}, [[hipTextureObject_t]{.pre}]{.n}[ ]{.w}[[texObject]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv427hipTexObjectGetResourceDescP17HIP_RESOURCE_DESC18hipTextureObject_t "Link to this definition"){.headerlink}\

:   Gets resource descriptor of a texture object.

    Parameters[:]{.colon}

    :   - **pResDesc** -- **\[out\]** pointer to resource descriptor

        - **texObject** -- **\[in\]** texture object

    Returns[:]{.colon}

    :   hipSuccess, hipErrorNotSupported, hipErrorInvalidValue

<!-- -->

[]{#_CPPv331hipTexObjectGetResourceViewDescP22HIP_RESOURCE_VIEW_DESC18hipTextureObject_t}[]{#_CPPv231hipTexObjectGetResourceViewDescP22HIP_RESOURCE_VIEW_DESC18hipTextureObject_t}[]{#hipTexObjectGetResourceViewDesc__HIP_RESOURCE_VIEW_DESCP.hipTextureObject_t}[]{#group___texture_1gac7b4b7bc09c32e2f2e25dbba07876a32 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipTexObjectGetResourceViewDesc]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[HIP_RESOURCE_VIEW_DESC]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[pResViewDesc]{.pre}]{.n .sig-param}, [[hipTextureObject_t]{.pre}]{.n}[ ]{.w}[[texObject]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv431hipTexObjectGetResourceViewDescP22HIP_RESOURCE_VIEW_DESC18hipTextureObject_t "Link to this definition"){.headerlink}\

:   Gets resource view descriptor of a texture object.

    Parameters[:]{.colon}

    :   - **pResViewDesc** -- **\[out\]** pointer to resource view descriptor

        - **texObject** -- **\[in\]** texture object

    Returns[:]{.colon}

    :   hipSuccess, hipErrorNotSupported, hipErrorInvalidValue

<!-- -->

[]{#_CPPv326hipTexObjectGetTextureDescP16HIP_TEXTURE_DESC18hipTextureObject_t}[]{#_CPPv226hipTexObjectGetTextureDescP16HIP_TEXTURE_DESC18hipTextureObject_t}[]{#hipTexObjectGetTextureDesc__HIP_TEXTURE_DESCP.hipTextureObject_t}[]{#group___texture_1ga7d65d4114af2b8ccc803a3bd7f40badd .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipTexObjectGetTextureDesc]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[HIP_TEXTURE_DESC]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[pTexDesc]{.pre}]{.n .sig-param}, [[hipTextureObject_t]{.pre}]{.n}[ ]{.w}[[texObject]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv426hipTexObjectGetTextureDescP16HIP_TEXTURE_DESC18hipTextureObject_t "Link to this definition"){.headerlink}\

:   Gets texture descriptor of a texture object.

    Parameters[:]{.colon}

    :   - **pTexDesc** -- **\[out\]** pointer to texture descriptor

        - **texObject** -- **\[in\]** texture object

    Returns[:]{.colon}

    :   hipSuccess, hipErrorNotSupported, hipErrorInvalidValue

<!-- -->

[]{#_CPPv323hipMallocMipmappedArrayP19hipMipmappedArray_tPK20hipChannelFormatDesc9hipExtentjj}[]{#_CPPv223hipMallocMipmappedArrayP19hipMipmappedArray_tPK20hipChannelFormatDesc9hipExtentjj}[]{#hipMallocMipmappedArray__hipMipmappedArray_tP.hipChannelFormatDescCP.hipExtent.unsigned-i.unsigned-i}[]{#group___texture_1gace6d42a4c294a5fe5cb9a383aca7eb36 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipMallocMipmappedArray]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipMipmappedArray_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[mipmappedArray]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[struct]{.pre}]{.k}[ ]{.w}[[hipChannelFormatDesc]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[desc]{.pre}]{.n .sig-param}, [[struct]{.pre}]{.k}[ ]{.w}[[hipExtent]{.pre}]{.n}[ ]{.w}[[extent]{.pre}]{.n .sig-param}, [[unsigned]{.pre}]{.kt}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[numLevels]{.pre}]{.n .sig-param}, [[unsigned]{.pre}]{.kt}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[flags]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv423hipMallocMipmappedArrayP19hipMipmappedArray_tPK20hipChannelFormatDesc9hipExtentjj "Link to this definition"){.headerlink}\

:   Allocate a mipmapped array on the device.

    
{.admonition .note}
    Note

    This API is implemented on Linux and is under development on Microsoft Windows.
    

    Parameters[:]{.colon}

    :   - **mipmappedArray** -- **\[out\]** - Pointer to allocated mipmapped array in device memory

        - **desc** -- **\[in\]** - Requested channel format

        - **extent** -- **\[in\]** - Requested allocation size (width field in elements)

        - **numLevels** -- **\[in\]** - Number of mipmap levels to allocate

        - **flags** -- **\[in\]** - Flags for extensions

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue, hipErrorMemoryAllocation

<!-- -->

[]{#_CPPv321hipFreeMipmappedArray19hipMipmappedArray_t}[]{#_CPPv221hipFreeMipmappedArray19hipMipmappedArray_t}[]{#hipFreeMipmappedArray__hipMipmappedArray_t}[]{#group___texture_1ga0255fc720bfe4164717b99dbd7c954c4 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipFreeMipmappedArray]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipMipmappedArray_t]{.pre}]{.n}[ ]{.w}[[mipmappedArray]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv421hipFreeMipmappedArray19hipMipmappedArray_t "Link to this definition"){.headerlink}\

:   Frees a mipmapped array on the device.

    
{.admonition .note}
    Note

    This API is implemented on Linux and is under development on Microsoft Windows.
    

    Parameters[:]{.colon}

    :   **mipmappedArray** -- **\[in\]** - Pointer to mipmapped array to free

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue

<!-- -->

[]{#_CPPv325hipGetMipmappedArrayLevelP10hipArray_t25hipMipmappedArray_const_tj}[]{#_CPPv225hipGetMipmappedArrayLevelP10hipArray_t25hipMipmappedArray_const_tj}[]{#hipGetMipmappedArrayLevel__hipArray_tP.hipMipmappedArray_const_t.unsigned-i}[]{#group___texture_1ga1ecc39df7764a7dcd5dad7149ffb2bc5 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipGetMipmappedArrayLevel]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipArray_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[levelArray]{.pre}]{.n .sig-param}, [[hipMipmappedArray_const_t]{.pre}]{.n}[ ]{.w}[[mipmappedArray]{.pre}]{.n .sig-param}, [[unsigned]{.pre}]{.kt}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[level]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv425hipGetMipmappedArrayLevelP10hipArray_t25hipMipmappedArray_const_tj "Link to this definition"){.headerlink}\

:   Gets a mipmap level of a HIP mipmapped array.

    
{.admonition .note}
    Note

    This API is implemented on Linux and is under development on Microsoft Windows.
    

    Parameters[:]{.colon}

    :   - **levelArray** -- **\[out\]** - Returned mipmap level HIP array

        - **mipmappedArray** -- **\[in\]** - HIP mipmapped array

        - **level** -- **\[in\]** - Mipmap level

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue

<!-- -->

[]{#_CPPv323hipMipmappedArrayCreateP19hipMipmappedArray_tP22HIP_ARRAY3D_DESCRIPTORj}[]{#_CPPv223hipMipmappedArrayCreateP19hipMipmappedArray_tP22HIP_ARRAY3D_DESCRIPTORj}[]{#hipMipmappedArrayCreate__hipMipmappedArray_tP.HIP_ARRAY3D_DESCRIPTORP.unsigned-i}[]{#group___texture_1gaadd49ed1c8e2c4d90adb8211779d971f .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipMipmappedArrayCreate]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipMipmappedArray_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[pHandle]{.pre}]{.n .sig-param}, [[HIP_ARRAY3D_DESCRIPTOR]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[pMipmappedArrayDesc]{.pre}]{.n .sig-param}, [[unsigned]{.pre}]{.kt}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[numMipmapLevels]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv423hipMipmappedArrayCreateP19hipMipmappedArray_tP22HIP_ARRAY3D_DESCRIPTORj "Link to this definition"){.headerlink}\

:   Create a mipmapped array.

    
{.admonition .note}
    Note

    This API is implemented on Linux and is under development on Microsoft Windows.
    

    Parameters[:]{.colon}

    :   - **pHandle** -- **\[out\]** pointer to mipmapped array

        - **pMipmappedArrayDesc** -- **\[in\]** mipmapped array descriptor

        - **numMipmapLevels** -- **\[in\]** mipmap level

    Returns[:]{.colon}

    :   hipSuccess, hipErrorNotSupported, hipErrorInvalidValue

<!-- -->

[]{#_CPPv324hipMipmappedArrayDestroy19hipMipmappedArray_t}[]{#_CPPv224hipMipmappedArrayDestroy19hipMipmappedArray_t}[]{#hipMipmappedArrayDestroy__hipMipmappedArray_t}[]{#group___texture_1ga4e5dd69cb90ff4d93aab4d6bff2cbcda .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipMipmappedArrayDestroy]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipMipmappedArray_t]{.pre}]{.n}[ ]{.w}[[hMipmappedArray]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv424hipMipmappedArrayDestroy19hipMipmappedArray_t "Link to this definition"){.headerlink}\

:   Destroy a mipmapped array.

    
{.admonition .note}
    Note

    This API is implemented on Linux and is under development on Microsoft Windows.
    

    Parameters[:]{.colon}

    :   **hMipmappedArray** -- **\[out\]** pointer to mipmapped array to destroy

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue

<!-- -->

[]{#_CPPv325hipMipmappedArrayGetLevelP10hipArray_t19hipMipmappedArray_tj}[]{#_CPPv225hipMipmappedArrayGetLevelP10hipArray_t19hipMipmappedArray_tj}[]{#hipMipmappedArrayGetLevel__hipArray_tP.hipMipmappedArray_t.unsigned-i}[]{#group___texture_1ga4c2ebc58183765e20a8216ee5660ff75 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipMipmappedArrayGetLevel]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipArray_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[pLevelArray]{.pre}]{.n .sig-param}, [[hipMipmappedArray_t]{.pre}]{.n}[ ]{.w}[[hMipMappedArray]{.pre}]{.n .sig-param}, [[unsigned]{.pre}]{.kt}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[level]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv425hipMipmappedArrayGetLevelP10hipArray_t19hipMipmappedArray_tj "Link to this definition"){.headerlink}\

:   Get a mipmapped array on a mipmapped level.

    
{.admonition .note}
    Note

    This API is implemented on Linux and is under development on Microsoft Windows.
    

    Parameters[:]{.colon}

    :   - **pLevelArray** -- **\[in\]** Pointer of array

        - **hMipMappedArray** -- **\[out\]** Pointer of mipmapped array on the requested mipmap level

        - **level** -- **\[out\]** Mipmap level

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
