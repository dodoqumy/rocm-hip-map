---
title: "Coherence control &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_runtime_api/memory_management/coherence_control.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T06:59:16.056867+00:00
content_hash: "d95b8a938f8e9fde"
---

::::::::::::::::::::::::::::::
{#main-content .bd-main role="main"}

sbt-scroll-pixel-helper

::::::::::::::::::::::::::::
bd-content
:::::::::::::::::::::::
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
# Coherence control

::
{#print-main-content}
:
{#jb-print-toc}

{}
## Contents

:
::

{#searchbox}

:::::::::
{#coherence-control .section}
[]{#id1}

# Coherence control[\#](#coherence-control "Link to this heading"){.headerlink}

Memory coherence describes how memory of a specific part of the system is visible to the other parts of the system. For example, how GPU memory is visible to the CPU and vice versa. In HIP, host and device memory can be allocated with two different types of coherence:

- **Coarse-grained coherence:** The memory is considered up-to-date only after synchronization performed using [[`hipDeviceSynchronize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../../../reference/hip_runtime_api/modules/device_management.html#_CPPv420hipDeviceSynchronizev "hipDeviceSynchronize"){.reference .internal}, [[`hipStreamSynchronize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../../../reference/hip_runtime_api/modules/stream_management.html#_CPPv420hipStreamSynchronize11hipStream_t "hipStreamSynchronize"){.reference .internal}, or any blocking operation that acts on the null stream such as [[`hipMemcpy()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../../../reference/hip_runtime_api/modules/memory_management.html#_CPPv49hipMemcpyPvPKv6size_t13hipMemcpyKind "hipMemcpy"){.reference .internal}. To avoid the cache from being accessed by a part of the system while simultaneously being written by another, the memory is made visible only after the caches have been flushed.

- **Fine-grained coherence:** The memory is coherent even while being modified by a part of the system. Fine-grained coherence ensures that up-to-date data is visible to others regardless of kernel boundaries. This can be useful if both host and device operate on the same data.

{.admonition .note}
Note

To achieve fine-grained coherence, many AMD GPUs use a limited cache policy, such as leaving these allocations uncached by the GPU or making them read-only.

Mi200 accelerator's hardware based floating point instructions work on coarse-grained memory regions. Coarse-grained coherence is typically useful in reducing host-device interconnect communication.

To check the availability of fine- and coarse-grained memory pools, use [`rocminfo`{.docutils .literal .notranslate}]{.pre}:

:
{.highlight-sh .notranslate}

highlight
    $ rocminfo
    ...
    *******
    Agent 1
    *******
    Name:                    AMD EPYC 7742 64-Core Processor
    ...
    Pool Info:
    Pool 1
    Segment:                 GLOBAL; FLAGS: FINE GRAINED
    ...
    Pool 3
    Segment:                 GLOBAL; FLAGS: COARSE GRAINED
    ...
    *******
    Agent 9
    *******
    Name:                    gfx90a
    ...
    Pool Info:
    Pool 1
    Segment:                 GLOBAL; FLAGS: COARSE GRAINED
    ...

:

The APIs, flags and respective memory coherence control are listed in the following table:

pst-scrollable-table-container
+------------------------------------------------------------------+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------+
| API                                                              | Flag                                                                  | [[`hipMemAdvise()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../../../reference/hip_runtime_api/modules/memory_management/unified_memory_reference.html#_CPPv412hipMemAdvisePKv6size_t15hipMemoryAdvisei "hipMemAdvise"){.reference .internal} call with argument | Coherence      |
+==================================================================+=======================================================================+=======================================================================================================================================================================================================================================================================================+================+
| [`hipHostMalloc`{.docutils .literal .notranslate}]{.pre} ^1^     | [`hipHostMallocDefault`{.docutils .literal .notranslate}]{.pre}       |                                                                                                                                                                                                                                                                                       | Fine-grained   |
+------------------------------------------------------------------+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------+
| [`hipHostMalloc`{.docutils .literal .notranslate}]{.pre} ^1^     | [`hipHostMallocNonCoherent`{.docutils .literal .notranslate}]{.pre}   |                                                                                                                                                                                                                                                                                       | Coarse-grained |
+------------------------------------------------------------------+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------+
| [`hipExtMallocWithFlags`{.docutils .literal .notranslate}]{.pre} | [`hipDeviceMallocDefault`{.docutils .literal .notranslate}]{.pre}     |                                                                                                                                                                                                                                                                                       | Coarse-grained |
+------------------------------------------------------------------+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------+
| [`hipExtMallocWithFlags`{.docutils .literal .notranslate}]{.pre} | [`hipDeviceMallocFinegrained`{.docutils .literal .notranslate}]{.pre} |                                                                                                                                                                                                                                                                                       | Fine-grained   |
+------------------------------------------------------------------+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------+
| [`hipMallocManaged`{.docutils .literal .notranslate}]{.pre}      |                                                                       |                                                                                                                                                                                                                                                                                       | Fine-grained   |
+------------------------------------------------------------------+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------+
| [`hipMallocManaged`{.docutils .literal .notranslate}]{.pre}      |                                                                       | [`hipMemAdviseSetCoarseGrain`{.docutils .literal .notranslate}]{.pre}                                                                                                                                                                                                                 | Coarse-grained |
+------------------------------------------------------------------+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------+
| [`malloc`{.docutils .literal .notranslate}]{.pre}                |                                                                       |                                                                                                                                                                                                                                                                                       | Fine-grained   |
+------------------------------------------------------------------+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------+
| [`malloc`{.docutils .literal .notranslate}]{.pre}                |                                                                       | [`hipMemAdviseSetCoarseGrain`{.docutils .literal .notranslate}]{.pre}                                                                                                                                                                                                                 | Coarse-grained |
+------------------------------------------------------------------+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------+

: [Memory coherence control]{.caption-text}[\#](#id2 "Link to this table"){.headerlink} {#id2 .table .table-center}

^1^ The [[`hipHostMalloc()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../../../reference/hip_runtime_api/modules/memory_management.html#_CPPv413hipHostMallocPPv6size_tj "hipHostMalloc"){.reference .internal} memory allocation coherence mode can be affected by the [`HIP_HOST_COHERENT`{.docutils .literal .notranslate}]{.pre} environment variable, if the [`hipHostMallocCoherent`{.docutils .literal .notranslate}]{.pre}, [`hipHostMallocNonCoherent`{.docutils .literal .notranslate}]{.pre}, and [`hipHostMallocMapped`{.docutils .literal .notranslate}]{.pre} are unset. If neither these flags nor the [`HIP_HOST_COHERENT`{.docutils .literal .notranslate}]{.pre} environment variable is set, or set as 0, the host memory allocation is coarse-grained.

{.admonition .note}
Note

- When [`hipHostMallocMapped`{.docutils .literal .notranslate}]{.pre} flag is set, the allocated host memory is fine-grained and the [`hipHostMallocNonCoherent`{.docutils .literal .notranslate}]{.pre} flag is ignored.

- Setting both the [`hipHostMallocCoherent`{.docutils .literal .notranslate}]{.pre} and [`hipHostMallocNonCoherent`{.docutils .literal .notranslate}]{.pre} flags leads to an illegal state.

:
{#performance-implications .section}
## Performance implications[\#](#performance-implications "Link to this heading"){.headerlink}

Understanding the performance characteristics of coherence control is essential for optimizing memory access patterns. Coherence control effectively serves as a **cache control** mechanism, with significant impact on bandwidth and latency.

pst-scrollable-table-container
+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Coherence Type     | Performance Characteristics                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+====================+=========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| **Coarse-grained** | Recommended for bulk data transfers and large memory regions. Utilizes the full L2 cache, providing high bandwidth for sequential access patterns. Synchronization points (e.g., [[`hipDeviceSynchronize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../../../reference/hip_runtime_api/modules/device_management.html#_CPPv420hipDeviceSynchronizev "hipDeviceSynchronize"){.reference .internal}) flush caches to ensure visibility, minimizing host-device interconnect communication overhead. |
+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Fine-grained**   | Recommended for atomic flags, signals, and small synchronization variables. Typically bypasses the L2 cache or employs heavy coherency protocols to ensure immediate visibility, resulting in lower bandwidth. Best suited for scenarios where both host and device require concurrent access to the same data.                                                                                                                                                                                                         |
+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: [Coherence control performance characteristics]{.caption-text}[\#](#id3 "Link to this table"){.headerlink} {#id3 .table .table-center}

In practice, coarse-grained coherence provides better performance for most compute-intensive workloads, while fine-grained coherence should be used selectively for specific synchronization requirements.
:

:
{#visibility-of-synchronization-functions .section}
## Visibility of synchronization functions[\#](#visibility-of-synchronization-functions "Link to this heading"){.headerlink}

The fine-grained coherence memory is visible at the synchronization points, however the visibility of coarse-grained memory depends on the synchronization function used. The effect and visibility of various synchronization functions on fine- and coarse-grained memory types are listed here:

pst-scrollable-table-container
  --------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  HIP API                                 [[`hipStreamSynchronize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../../../reference/hip_runtime_api/modules/stream_management.html#_CPPv420hipStreamSynchronize11hipStream_t "hipStreamSynchronize"){.reference .internal}   [[`hipDeviceSynchronize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../../../reference/hip_runtime_api/modules/device_management.html#_CPPv420hipDeviceSynchronizev "hipDeviceSynchronize"){.reference .internal}   [[`hipEventSynchronize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../../../reference/hip_runtime_api/modules/event_management.html#_CPPv419hipEventSynchronize10hipEvent_t "hipEventSynchronize"){.reference .internal}   [[`hipStreamWaitEvent()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../../../reference/hip_runtime_api/modules/stream_management.html#_CPPv418hipStreamWaitEvent11hipStream_t10hipEvent_tj "hipStreamWaitEvent"){.reference .internal}
  Synchronization effect                  Host waits for all commands in the specified stream to complete                                                                                                                                                                                      Host waits for all commands in all streams on the specified device to complete                                                                                                                                                           Host waits for the specified event to complete                                                                                                                                                                                                  Stream waits for the specified event to complete
  Fence                                   System-scope release                                                                                                                                                                                                                                 System-scope release                                                                                                                                                                                                                     System-scope release                                                                                                                                                                                                                            None
  Fine-grained host memory visibility     Yes                                                                                                                                                                                                                                                  Yes                                                                                                                                                                                                                                      Yes                                                                                                                                                                                                                                             Yes
  Coarse-grained host memory visibility   Yes                                                                                                                                                                                                                                                  Yes                                                                                                                                                                                                                                      Depends on the used event.                                                                                                                                                                                                                      No
  --------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  : [HIP synchronize functions effect and visibility]{.caption-text}[\#](#id4 "Link to this table"){.headerlink} {#id4 .table}

You can control the release scope for [`hipEvents`{.docutils .literal .notranslate}]{.pre}. By default, the GPU performs a device-scope acquire and release operation with each recorded event. This makes the host and device memory visible to other commands executing on the same device.

[[`hipEventCreateWithFlags()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../../../reference/hip_runtime_api/modules/event_management.html#_CPPv423hipEventCreateWithFlagsP10hipEvent_tj "hipEventCreateWithFlags"){.reference .internal}: You can specify a stronger system-level fence by creating the event with [`hipEventCreateWithFlags`{.docutils .literal .notranslate}]{.pre}:

- [`hipEventReleaseToSystem`{.docutils .literal .notranslate}]{.pre}: Performs a system-scope release operation when the event is recorded. This makes both fine-grained and coarse-grained host memory visible to other agents in the system, which might also involve heavyweight operations such as cache flushing. Fine-grained memory typically uses lighter-weight in-kernel synchronization mechanisms such as an atomic operation and thus doesn't need to use [`hipEventReleaseToSystem`{.docutils .literal .notranslate}]{.pre}.

- [`hipEventDisableTiming`{.docutils .literal .notranslate}]{.pre}: Events created with this flag don't record profiling data, which significantly improves synchronization performance.
:
:::::::::
:::::::::::::::::::::::

{.bd-sidebar-secondary .bd-toc}
::
{.sidebar-secondary-items .sidebar-secondary__inner}
:
sidebar-secondary-item

{.page-toc .tocsection .onthispage}
Contents

:
::

::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::
