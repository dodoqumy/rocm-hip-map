---
title: "Peer to peer device memory access &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/reference/hip_runtime_api/modules/peer_to_peer_device_memory_access.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T06:58:53.430237+00:00
content_hash: "c69c8ab5e1e258d9"
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
# Peer to peer device memory access

::
{#print-main-content}
:
{#jb-print-toc}

{}
## Contents

:
::

{#searchbox}

{#peer-to-peer-device-memory-access .section}
[]{#peer-to-peer-device-memory-access-reference}

# Peer to peer device memory access[\#](#peer-to-peer-device-memory-access "Link to this heading"){.headerlink}

[]{#_CPPv322hipDeviceCanAccessPeerPiii}[]{#_CPPv222hipDeviceCanAccessPeerPiii}[]{#hipDeviceCanAccessPeer__iP.i.i}[]{#group___peer_to_peer_1ga0a1c9ccd775758d9d7d5b5a1f525b719 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipDeviceCanAccessPeer]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[canAccessPeer]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[deviceId]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[peerDeviceId]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv422hipDeviceCanAccessPeerPiii "Link to this definition"){.headerlink}\

:   Determines if a device can access a peer device's memory.

    The value of [`canAccessPeer`{.docutils .literal .notranslate}]{.pre},

    Returns "1" if the specified [`deviceId`{.docutils .literal .notranslate}]{.pre} is capable of directly accessing memory physically located on [`peerDeviceId`{.docutils .literal .notranslate}]{.pre},

    Returns "0" if the specified [`deviceId`{.docutils .literal .notranslate}]{.pre} is not capable of directly accessing memory physically located on [`peerDeviceId`{.docutils .literal .notranslate}]{.pre}.

    Returns "0" if [`deviceId`{.docutils .literal .notranslate}]{.pre} == [`peerDeviceId`{.docutils .literal .notranslate}]{.pre}, both are valid devices, however, a device is not a peer of itself.

    Returns hipErrorInvalidDevice if deviceId or peerDeviceId are not valid devices

    Parameters[:]{.colon}

    :   - **canAccessPeer** -- **\[out\]** - Returns the peer access capability (0 or 1)

        - **deviceId** -- **\[in\]** - The device accessing the peer device memory.

        - **peerDeviceId** -- **\[in\]** - Peer device where memory is physically located

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidDevice

<!-- -->

[]{#_CPPv325hipDeviceEnablePeerAccessij}[]{#_CPPv225hipDeviceEnablePeerAccessij}[]{#hipDeviceEnablePeerAccess__i.unsigned-i}[]{#group___peer_to_peer_1ga0caca59034134d7a7bb893cc1caa653e .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipDeviceEnablePeerAccess]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[peerDeviceId]{.pre}]{.n .sig-param}, [[unsigned]{.pre}]{.kt}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[flags]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv425hipDeviceEnablePeerAccessij "Link to this definition"){.headerlink}\

:   Enables direct access to memory allocations on a peer device.

    When this API is successful, all memory allocations on peer device will be mapped into the address space of the current device. In addition, any future memory allocation on the peer device will remain accessible from the current device, until the access is disabled using hipDeviceDisablePeerAccess or device is reset using hipDeviceReset.

    Parameters[:]{.colon}

    :   - **peerDeviceId** -- **\[in\]** - Peer device to enable direct access to from the current device

        - **flags** -- **\[in\]** - Reserved for future use, must be zero

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidDevice, hipErrorInvalidValue,

    Returns[:]{.colon}

    :   hipErrorPeerAccessAlreadyEnabled if peer access is already enabled for this device.

<!-- -->

[]{#_CPPv326hipDeviceDisablePeerAccessi}[]{#_CPPv226hipDeviceDisablePeerAccessi}[]{#hipDeviceDisablePeerAccess__i}[]{#group___peer_to_peer_1ga85030c72824fb60aaddc7374ab60481b .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipDeviceDisablePeerAccess]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[peerDeviceId]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv426hipDeviceDisablePeerAccessi "Link to this definition"){.headerlink}\

:   Disables direct access to memory allocations on a peer device.

    If direct access to memory allocations on peer device has not been enabled yet from the current device, it returns hipErrorPeerAccessNotEnabled.

    Parameters[:]{.colon}

    :   **peerDeviceId** -- **\[in\]** Peer device to disable direct access to

    Returns[:]{.colon}

    :   hipSuccess, hipErrorPeerAccessNotEnabled

<!-- -->

[]{#_CPPv313hipMemcpyPeerPviPKvi6size_t}[]{#_CPPv213hipMemcpyPeerPviPKvi6size_t}[]{#hipMemcpyPeer__voidP.i.voidCP.i.s}[]{#group___peer_to_peer_1ga5512f45e25c08052667c8ffe7162333b .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipMemcpyPeer]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[dst]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[dstDeviceId]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[src]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[srcDeviceId]{.pre}]{.n .sig-param}, [[size_t]{.pre}]{.n}[ ]{.w}[[sizeBytes]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv413hipMemcpyPeerPviPKvi6size_t "Link to this definition"){.headerlink}\

:   Copies memory between two peer accessible devices.

    Parameters[:]{.colon}

    :   - **dst** -- **\[out\]** - Destination device pointer

        - **dstDeviceId** -- **\[in\]** - Destination device

        - **src** -- **\[in\]** - Source device pointer

        - **srcDeviceId** -- **\[in\]** - Source device

        - **sizeBytes** -- **\[in\]** - Size of memory copy in bytes

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue, hipErrorInvalidDevice

<!-- -->

[]{#_CPPv318hipMemcpyPeerAsyncPviPKvi6size_t11hipStream_t}[]{#_CPPv218hipMemcpyPeerAsyncPviPKvi6size_t11hipStream_t}[]{#hipMemcpyPeerAsync__voidP.i.voidCP.i.s.hipStream_t}[]{#group___peer_to_peer_1ga60091a115da3cb616adef5741fab4c4e .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipMemcpyPeerAsync]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[dst]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[dstDeviceId]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[src]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[srcDevice]{.pre}]{.n .sig-param}, [[size_t]{.pre}]{.n}[ ]{.w}[[sizeBytes]{.pre}]{.n .sig-param}, [[hipStream_t]{.pre}]{.n}[ ]{.w}[[stream]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv418hipMemcpyPeerAsyncPviPKvi6size_t11hipStream_t "Link to this definition"){.headerlink}\

:   Copies memory between two peer accessible devices asynchronously.

    Parameters[:]{.colon}

    :   - **dst** -- **\[out\]** - Destination device pointer

        - **dstDeviceId** -- **\[in\]** - Destination device

        - **src** -- **\[in\]** - Source device pointer

        - **srcDevice** -- **\[in\]** - Source device

        - **sizeBytes** -- **\[in\]** - Size of memory copy in bytes

        - **stream** -- **\[in\]** - Stream identifier

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue, hipErrorInvalidDevice

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
