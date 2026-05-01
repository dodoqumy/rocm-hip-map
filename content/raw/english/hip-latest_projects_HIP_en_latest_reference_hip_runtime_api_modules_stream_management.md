---
title: "Stream management &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/reference/hip_runtime_api/modules/stream_management.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T06:59:01.770588+00:00
content_hash: "23f53bd704190631"
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
# Stream management

::
{#print-main-content}
:
{#jb-print-toc}

{}
## Contents

:
::

{#searchbox}

{#stream-management .section}
[]{#stream-management-reference}

# Stream management[\#](#stream-management "Link to this heading"){.headerlink}

[]{#_CPPv319hipStreamCallback_t}[]{#_CPPv219hipStreamCallback_t}[]{#hipStreamCallback_t}[]{#group___stream_1ga6d4e90ec5736f9728102be22d0559dfd .target}[[typedef]{.pre}]{.k}[ ]{.w}[[void]{.pre}]{.kt}[ ]{.w}[[(]{.pre}]{.p}[[\*]{.pre}]{.p}[[[hipStreamCallback_t]{.pre}]{.n}]{.sig-name .descname}[[)]{.pre}]{.p}[[(]{.pre}]{.p}[[hipStream_t]{.pre}]{.n}[ ]{.w}[[stream]{.pre}]{.n}[[,]{.pre}]{.p}[ ]{.w}[[hipError_t]{.pre}]{.n}[ ]{.w}[[status]{.pre}]{.n}[[,]{.pre}]{.p}[ ]{.w}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[userData]{.pre}]{.n}[[)]{.pre}]{.p}[\#](#_CPPv419hipStreamCallback_t "Link to this definition"){.headerlink}\

:   Stream CallBack struct

<!-- -->

[]{#_CPPv315hipStreamCreateP11hipStream_t}[]{#_CPPv215hipStreamCreateP11hipStream_t}[]{#hipStreamCreate__hipStream_tP}[]{#group___stream_1gaff5b62d6e9502d80879f7176f4d03102 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipStreamCreate]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipStream_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[stream]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv415hipStreamCreateP11hipStream_t "Link to this definition"){.headerlink}\

:   Creates an asynchronous stream.

    Creates a new asynchronous stream with its associated current device. The [`stream`{.docutils .literal .notranslate}]{.pre} returns an opaque handle that can be used to reference the newly created stream in subsequent hipStream\* commands. The stream is allocated on the heap and will remain allocated even if the handle goes out-of-scope. To release the memory used by the stream, the application must call hipStreamDestroy.

    
{.admonition .seealso}
    See also

    [[hipStreamCreateWithFlags]{.std .std-ref}](#group___stream_1gaf2382e3cc6632332a8983a0f58e43494){.reference .internal}, [[hipStreamCreateWithPriority]{.std .std-ref}](#group___stream_1gace005d8ea734fb66c995bd43dac3fd44){.reference .internal}, [[hipStreamSynchronize]{.std .std-ref}](#group___stream_1gabbfb9f573a6ebe8c478605ecb5504a74){.reference .internal}, [[hipStreamWaitEvent]{.std .std-ref}](#group___stream_1gacdd84c8f8ef1539c96c57c1d5bcae633){.reference .internal}, [[hipStreamDestroy]{.std .std-ref}](#group___stream_1ga3076a3499ed2c7821311006100bb95ec){.reference .internal}
    

    Parameters[:]{.colon}

    :   **stream** -- **\[inout\]** Valid pointer to hipStream_t. This function writes the memory with the newly created stream.

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue

<!-- -->

[]{#_CPPv324hipStreamCreateWithFlagsP11hipStream_tj}[]{#_CPPv224hipStreamCreateWithFlagsP11hipStream_tj}[]{#hipStreamCreateWithFlags__hipStream_tP.unsigned-i}[]{#group___stream_1gaf2382e3cc6632332a8983a0f58e43494 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipStreamCreateWithFlags]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipStream_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[stream]{.pre}]{.n .sig-param}, [[unsigned]{.pre}]{.kt}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[flags]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv424hipStreamCreateWithFlagsP11hipStream_tj "Link to this definition"){.headerlink}\

:   Creates an asynchronous stream with flag.

    Creates a new asynchronous stream with its associated current device. [`stream`{.docutils .literal .notranslate}]{.pre} returns an opaque handle that can be used to reference the newly created stream in subsequent hipStream\* commands. The stream is allocated on the heap and will remain allocated even if the handle goes out-of-scope. To release the memory used by the stream, application must call hipStreamDestroy.

    The [`flags`{.docutils .literal .notranslate}]{.pre} parameter controls behavior of the stream. The valid values are hipStreamDefault and hipStreamNonBlocking.

    
{.admonition .seealso}
    See also

    [[hipStreamCreate]{.std .std-ref}](#group___stream_1gaff5b62d6e9502d80879f7176f4d03102){.reference .internal}, [[hipStreamCreateWithPriority]{.std .std-ref}](#group___stream_1gace005d8ea734fb66c995bd43dac3fd44){.reference .internal}, [[hipStreamSynchronize]{.std .std-ref}](#group___stream_1gabbfb9f573a6ebe8c478605ecb5504a74){.reference .internal}, [[hipStreamWaitEvent]{.std .std-ref}](#group___stream_1gacdd84c8f8ef1539c96c57c1d5bcae633){.reference .internal}, [[hipStreamDestroy]{.std .std-ref}](#group___stream_1ga3076a3499ed2c7821311006100bb95ec){.reference .internal}.
    

    Parameters[:]{.colon}

    :   - **stream** -- **\[inout\]** Pointer to new stream

        - **flags** -- **\[in\]** Parameters to control stream creation

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue

<!-- -->

[]{#_CPPv327hipStreamCreateWithPriorityP11hipStream_tji}[]{#_CPPv227hipStreamCreateWithPriorityP11hipStream_tji}[]{#hipStreamCreateWithPriority__hipStream_tP.unsigned-i.i}[]{#group___stream_1gace005d8ea734fb66c995bd43dac3fd44 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipStreamCreateWithPriority]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipStream_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[stream]{.pre}]{.n .sig-param}, [[unsigned]{.pre}]{.kt}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[flags]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[priority]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv427hipStreamCreateWithPriorityP11hipStream_tji "Link to this definition"){.headerlink}\

:   Creates an asynchronous stream with the specified priority.

    Creates a new asynchronous stream with the specified priority, with its associated current device. [`stream`{.docutils .literal .notranslate}]{.pre} returns an opaque handle that can be used to reference the newly created stream in subsequent hipStream\* commands. The stream is allocated on the heap and will remain allocated even if the handle goes out-of-scope. To release the memory used by the stream, application must call hipStreamDestroy.

    The [`flags`{.docutils .literal .notranslate}]{.pre} parameter controls behavior of the stream. The valid values are hipStreamDefault and hipStreamNonBlocking.

    
{.admonition .seealso}
    See also

    [[hipStreamCreate]{.std .std-ref}](#group___stream_1gaff5b62d6e9502d80879f7176f4d03102){.reference .internal}, [[hipStreamSynchronize]{.std .std-ref}](#group___stream_1gabbfb9f573a6ebe8c478605ecb5504a74){.reference .internal}, [[hipStreamWaitEvent]{.std .std-ref}](#group___stream_1gacdd84c8f8ef1539c96c57c1d5bcae633){.reference .internal}, [[hipStreamDestroy]{.std .std-ref}](#group___stream_1ga3076a3499ed2c7821311006100bb95ec){.reference .internal}
    

    Parameters[:]{.colon}

    :   - **stream** -- **\[inout\]** Pointer to new stream

        - **flags** -- **\[in\]** Parameters to control stream creation

        - **priority** -- **\[in\]** Priority of the stream. Lower numbers represent higher priorities.

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue

<!-- -->

[]{#_CPPv331hipDeviceGetStreamPriorityRangePiPi}[]{#_CPPv231hipDeviceGetStreamPriorityRangePiPi}[]{#hipDeviceGetStreamPriorityRange__iP.iP}[]{#group___stream_1ga2b0709fb23b273abec8ea223ebb362bc .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipDeviceGetStreamPriorityRange]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[leastPriority]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[greatestPriority]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv431hipDeviceGetStreamPriorityRangePiPi "Link to this definition"){.headerlink}\

:   Returns numerical values that correspond to the least and greatest stream priority.

    Returns in \*leastPriority and \*greatestPriority the numerical values that correspond to the least and greatest stream priority respectively. Stream priorities follow a convention where lower numbers imply greater priorities. The range of meaningful stream priorities is given by \[\*leastPriority,\*greatestPriority\]. If the user attempts to create a stream with a priority value that is outside the meaningful range as specified by this API, the priority is automatically clamped to within the valid range.

    
{.admonition .warning}
    Warning

    This API is under development on AMD GPUs and simply returns hipSuccess.
    

    Parameters[:]{.colon}

    :   - **leastPriority** -- **\[inout\]** Pointer in which a value corresponding to least priority is returned.

        - **greatestPriority** -- **\[inout\]** Pointer in which a value corresponding to greatest priority is returned.

    Returns[:]{.colon}

    :   hipSuccess

<!-- -->

[]{#_CPPv316hipStreamDestroy11hipStream_t}[]{#_CPPv216hipStreamDestroy11hipStream_t}[]{#hipStreamDestroy__hipStream_t}[]{#group___stream_1ga3076a3499ed2c7821311006100bb95ec .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipStreamDestroy]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipStream_t]{.pre}]{.n}[ ]{.w}[[stream]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv416hipStreamDestroy11hipStream_t "Link to this definition"){.headerlink}\

:   Destroys the specified stream.

    Destroys the specified stream.

    If commands are still executing on the specified stream, some may complete execution before the queue is deleted.

    The queue may be destroyed while some commands are still inflight, or may wait for all commands queued to the stream before destroying it.

    
{.admonition .seealso}
    See also

    [[hipStreamCreate]{.std .std-ref}](#group___stream_1gaff5b62d6e9502d80879f7176f4d03102){.reference .internal}, [[hipStreamCreateWithFlags]{.std .std-ref}](#group___stream_1gaf2382e3cc6632332a8983a0f58e43494){.reference .internal}, [[hipStreamCreateWithPriority]{.std .std-ref}](#group___stream_1gace005d8ea734fb66c995bd43dac3fd44){.reference .internal}, [[hipStreamQuery]{.std .std-ref}](#group___stream_1ga925b39ff78d3b5fd458bd9e2cade9f4e){.reference .internal}, [[hipStreamWaitEvent]{.std .std-ref}](#group___stream_1gacdd84c8f8ef1539c96c57c1d5bcae633){.reference .internal}, [[hipStreamSynchronize]{.std .std-ref}](#group___stream_1gabbfb9f573a6ebe8c478605ecb5504a74){.reference .internal}
    

    Parameters[:]{.colon}

    :   **stream** -- **\[in\]** Stream identifier

    Returns[:]{.colon}

    :   hipSuccess hipErrorInvalidHandle

<!-- -->

[]{#_CPPv314hipStreamQuery11hipStream_t}[]{#_CPPv214hipStreamQuery11hipStream_t}[]{#hipStreamQuery__hipStream_t}[]{#group___stream_1ga925b39ff78d3b5fd458bd9e2cade9f4e .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipStreamQuery]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipStream_t]{.pre}]{.n}[ ]{.w}[[stream]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv414hipStreamQuery11hipStream_t "Link to this definition"){.headerlink}\

:   Returns hipSuccess if all of the operations in the specified [`stream`{.docutils .literal .notranslate}]{.pre} have completed, or hipErrorNotReady if not.

    This is thread-safe and returns a snapshot of the current state of the queue. However, if other host threads are sending work to the stream, the status may change immediately after the function is called. It is typically used for debug.

    
{.admonition .seealso}
    See also

    [[hipStreamCreate]{.std .std-ref}](#group___stream_1gaff5b62d6e9502d80879f7176f4d03102){.reference .internal}, [[hipStreamCreateWithFlags]{.std .std-ref}](#group___stream_1gaf2382e3cc6632332a8983a0f58e43494){.reference .internal}, [[hipStreamCreateWithPriority]{.std .std-ref}](#group___stream_1gace005d8ea734fb66c995bd43dac3fd44){.reference .internal}, [[hipStreamWaitEvent]{.std .std-ref}](#group___stream_1gacdd84c8f8ef1539c96c57c1d5bcae633){.reference .internal}, [[hipStreamSynchronize]{.std .std-ref}](#group___stream_1gabbfb9f573a6ebe8c478605ecb5504a74){.reference .internal}, [[hipStreamDestroy]{.std .std-ref}](#group___stream_1ga3076a3499ed2c7821311006100bb95ec){.reference .internal}
    

    Parameters[:]{.colon}

    :   **stream** -- **\[in\]** Stream to query

    Returns[:]{.colon}

    :   hipSuccess, hipErrorNotReady, hipErrorInvalidHandle

<!-- -->

[]{#_CPPv320hipStreamSynchronize11hipStream_t}[]{#_CPPv220hipStreamSynchronize11hipStream_t}[]{#hipStreamSynchronize__hipStream_t}[]{#group___stream_1gabbfb9f573a6ebe8c478605ecb5504a74 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipStreamSynchronize]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipStream_t]{.pre}]{.n}[ ]{.w}[[stream]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv420hipStreamSynchronize11hipStream_t "Link to this definition"){.headerlink}\

:   Waits for all commands in the stream to complete.

    This command is host-synchronous : the host will block until all operations on the specified stream with its associated device are completed. On multiple device systems, the [`stream`{.docutils .literal .notranslate}]{.pre} is associated with its device, no need to call hipSetDevice before this API.

    This command follows standard null-stream semantics. Specifying the null stream will cause the command to wait for other streams on the same device to complete all pending operations.

    This command honors the hipDeviceScheduleBlockingSync flag, which controls whether the wait is active or blocking.

    
{.admonition .seealso}
    See also

    [[hipStreamCreate]{.std .std-ref}](#group___stream_1gaff5b62d6e9502d80879f7176f4d03102){.reference .internal}, [[hipStreamCreateWithFlags]{.std .std-ref}](#group___stream_1gaf2382e3cc6632332a8983a0f58e43494){.reference .internal}, [[hipStreamCreateWithPriority]{.std .std-ref}](#group___stream_1gace005d8ea734fb66c995bd43dac3fd44){.reference .internal}, [[hipStreamWaitEvent]{.std .std-ref}](#group___stream_1gacdd84c8f8ef1539c96c57c1d5bcae633){.reference .internal}, [[hipStreamDestroy]{.std .std-ref}](#group___stream_1ga3076a3499ed2c7821311006100bb95ec){.reference .internal}
    

    Parameters[:]{.colon}

    :   **stream** -- **\[in\]** Stream identifier.

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidHandle

<!-- -->

[]{#_CPPv318hipStreamWaitEvent11hipStream_t10hipEvent_tj}[]{#_CPPv218hipStreamWaitEvent11hipStream_t10hipEvent_tj}[]{#hipStreamWaitEvent__hipStream_t.hipEvent_t.unsigned-i}[]{#group___stream_1gacdd84c8f8ef1539c96c57c1d5bcae633 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipStreamWaitEvent]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipStream_t]{.pre}]{.n}[ ]{.w}[[stream]{.pre}]{.n .sig-param}, [[hipEvent_t]{.pre}]{.n}[ ]{.w}[[event]{.pre}]{.n .sig-param}, [[unsigned]{.pre}]{.kt}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[flags]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv418hipStreamWaitEvent11hipStream_t10hipEvent_tj "Link to this definition"){.headerlink}\

:   Makes the specified compute stream wait for the specified event.

    This function inserts a wait operation into the specified stream. All future work submitted to [`stream`{.docutils .literal .notranslate}]{.pre} will wait until [`event`{.docutils .literal .notranslate}]{.pre} reports completion before beginning execution.

    Flags include: hipEventWaitDefault: Default event creation flag. hipEventWaitExternal: Wait is captured in the graph as an external event node when performing stream capture

    This function only waits for commands in the current stream to complete. Notably, this function does not implicitly wait for commands in the default stream to complete, even if the specified stream is created with hipStreamNonBlocking = 0.

    
{.admonition .seealso}
    See also

    [[hipStreamCreate]{.std .std-ref}](#group___stream_1gaff5b62d6e9502d80879f7176f4d03102){.reference .internal}, [[hipStreamCreateWithFlags]{.std .std-ref}](#group___stream_1gaf2382e3cc6632332a8983a0f58e43494){.reference .internal}, [[hipStreamCreateWithPriority]{.std .std-ref}](#group___stream_1gace005d8ea734fb66c995bd43dac3fd44){.reference .internal}, [[hipStreamSynchronize]{.std .std-ref}](#group___stream_1gabbfb9f573a6ebe8c478605ecb5504a74){.reference .internal}, [[hipStreamDestroy]{.std .std-ref}](#group___stream_1ga3076a3499ed2c7821311006100bb95ec){.reference .internal}
    

    Parameters[:]{.colon}

    :   - **stream** -- **\[in\]** Stream to make wait

        - **event** -- **\[in\]** Event to wait on

        - **flags** -- **\[in\]** Parameters to control the operation

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidHandle, hipErrorInvalidValue, hipErrorStreamCaptureIsolation

<!-- -->

[]{#_CPPv317hipStreamGetFlags11hipStream_tPj}[]{#_CPPv217hipStreamGetFlags11hipStream_tPj}[]{#hipStreamGetFlags__hipStream_t.unsigned-iP}[]{#group___stream_1ga3249555a26439591b8873f70b39bb116 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipStreamGetFlags]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipStream_t]{.pre}]{.n}[ ]{.w}[[stream]{.pre}]{.n .sig-param}, [[unsigned]{.pre}]{.kt}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[flags]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv417hipStreamGetFlags11hipStream_tPj "Link to this definition"){.headerlink}\

:   Returns flags associated with this stream.

    
{.admonition .seealso}
    See also

    [[hipStreamCreateWithFlags]{.std .std-ref}](#group___stream_1gaf2382e3cc6632332a8983a0f58e43494){.reference .internal}
    

    Parameters[:]{.colon}

    :   - **stream** -- **\[in\]** Stream to be queried

        - **flags** -- **\[inout\]** Pointer to an unsigned integer in which the stream's flags are returned

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue, hipErrorInvalidHandle.

<!-- -->

[]{#_CPPv314hipStreamGetId11hipStream_tPy}[]{#_CPPv214hipStreamGetId11hipStream_tPy}[]{#hipStreamGetId__hipStream_t.unsigned-l-lP}[]{#group___stream_1ga296cfc9c2ffa8b2a3856ba7a7058d7de .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipStreamGetId]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipStream_t]{.pre}]{.n}[ ]{.w}[[stream]{.pre}]{.n .sig-param}, [[unsigned]{.pre}]{.kt}[ ]{.w}[[long]{.pre}]{.kt}[ ]{.w}[[long]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[streamId]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv414hipStreamGetId11hipStream_tPy "Link to this definition"){.headerlink}\

:   Queries the Id of a stream.

    
{.admonition .seealso}
    See also

    [[hipStreamCreateWithFlags]{.std .std-ref}](#group___stream_1gaf2382e3cc6632332a8983a0f58e43494){.reference .internal}, [[hipStreamGetFlags]{.std .std-ref}](#group___stream_1ga3249555a26439591b8873f70b39bb116){.reference .internal}, [[hipStreamCreateWithPriority]{.std .std-ref}](#group___stream_1gace005d8ea734fb66c995bd43dac3fd44){.reference .internal}, [[hipStreamGetPriority]{.std .std-ref}](#group___stream_1gae5a0d1e66035b157149ec10f5c7952be){.reference .internal}
    

    Parameters[:]{.colon}

    :   - **stream** -- **\[in\]** Stream to be queried

        - **flags** -- **\[inout\]** Pointer to an unsigned long long in which the stream's id is returned

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue, hipErrorInvalidHandle.

<!-- -->

[]{#_CPPv320hipStreamGetPriority11hipStream_tPi}[]{#_CPPv220hipStreamGetPriority11hipStream_tPi}[]{#hipStreamGetPriority__hipStream_t.iP}[]{#group___stream_1gae5a0d1e66035b157149ec10f5c7952be .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipStreamGetPriority]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipStream_t]{.pre}]{.n}[ ]{.w}[[stream]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[priority]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv420hipStreamGetPriority11hipStream_tPi "Link to this definition"){.headerlink}\

:   Queries the priority of a stream.

    
{.admonition .seealso}
    See also

    [[hipStreamCreateWithPriority]{.std .std-ref}](#group___stream_1gace005d8ea734fb66c995bd43dac3fd44){.reference .internal}
    

    Parameters[:]{.colon}

    :   - **stream** -- **\[in\]** Stream to be queried

        - **priority** -- **\[inout\]** Pointer to an unsigned integer in which the stream's priority is returned

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue, hipErrorInvalidHandle.

<!-- -->

[]{#_CPPv318hipStreamGetDevice11hipStream_tP11hipDevice_t}[]{#_CPPv218hipStreamGetDevice11hipStream_tP11hipDevice_t}[]{#hipStreamGetDevice__hipStream_t.hipDevice_tP}[]{#group___stream_1ga91b2d98f5530f0bd73a257fdca1abe4d .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipStreamGetDevice]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipStream_t]{.pre}]{.n}[ ]{.w}[[stream]{.pre}]{.n .sig-param}, [[hipDevice_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[device]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv418hipStreamGetDevice11hipStream_tP11hipDevice_t "Link to this definition"){.headerlink}\

:   Gets the device associated with the stream.

    
{.admonition .seealso}
    See also

    [[hipStreamCreate]{.std .std-ref}](#group___stream_1gaff5b62d6e9502d80879f7176f4d03102){.reference .internal}, [[hipStreamDestroy]{.std .std-ref}](#group___stream_1ga3076a3499ed2c7821311006100bb95ec){.reference .internal}, [[hipDeviceGetStreamPriorityRange]{.std .std-ref}](#group___stream_1ga2b0709fb23b273abec8ea223ebb362bc){.reference .internal}
    

    Parameters[:]{.colon}

    :   - **stream** -- **\[in\]** Stream to be queried

        - **device** -- **\[out\]** Device associated with the stream

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue, hipErrorContextIsDestroyed, hipErrorInvalidHandle, hipErrorNotInitialized, hipErrorDeinitialized, hipErrorInvalidContext

<!-- -->

[]{#_CPPv328hipExtStreamCreateWithCUMaskP11hipStream_t8uint32_tPK8uint32_t}[]{#_CPPv228hipExtStreamCreateWithCUMaskP11hipStream_t8uint32_tPK8uint32_t}[]{#hipExtStreamCreateWithCUMask__hipStream_tP.uint32_t.uint32_tCP}[]{#group___stream_1gad61df06555ebdfa30784b3233ca5e13f .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipExtStreamCreateWithCUMask]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipStream_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[stream]{.pre}]{.n .sig-param}, [[uint32_t]{.pre}]{.n}[ ]{.w}[[cuMaskSize]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[uint32_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[cuMask]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv428hipExtStreamCreateWithCUMaskP11hipStream_t8uint32_tPK8uint32_t "Link to this definition"){.headerlink}\

:   Creates an asynchronous stream with the specified CU mask.

    Creates a new asynchronous stream with the specified CU mask. [`stream`{.docutils .literal .notranslate}]{.pre} returns an opaque handle that can be used to reference the newly created stream in subsequent hipStream\* commands. The stream is allocated on the heap and will remain allocated even if the handle goes out-of-scope. To release the memory used by the stream, application must call hipStreamDestroy.

    
{.admonition .seealso}
    See also

    [[hipStreamCreate]{.std .std-ref}](#group___stream_1gaff5b62d6e9502d80879f7176f4d03102){.reference .internal}, [[hipStreamSynchronize]{.std .std-ref}](#group___stream_1gabbfb9f573a6ebe8c478605ecb5504a74){.reference .internal}, [[hipStreamWaitEvent]{.std .std-ref}](#group___stream_1gacdd84c8f8ef1539c96c57c1d5bcae633){.reference .internal}, [[hipStreamDestroy]{.std .std-ref}](#group___stream_1ga3076a3499ed2c7821311006100bb95ec){.reference .internal}
    

    Parameters[:]{.colon}

    :   - **stream** -- **\[inout\]** Pointer to new stream

        - **cuMaskSize** -- **\[in\]** Size of CU mask bit array passed in.

        - **cuMask** -- **\[in\]** Bit-vector representing the CU mask. Each active bit represents using one CU. The first 32 bits represent the first 32 CUs, and so on. If its size is greater than physical CU number (i.e., multiProcessorCount member of hipDeviceProp_t), the extra elements are ignored. It is user's responsibility to make sure the input is meaningful.

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidHandle, hipErrorInvalidValue

<!-- -->

[]{#_CPPv321hipExtStreamGetCUMask11hipStream_t8uint32_tP8uint32_t}[]{#_CPPv221hipExtStreamGetCUMask11hipStream_t8uint32_tP8uint32_t}[]{#hipExtStreamGetCUMask__hipStream_t.uint32_t.uint32_tP}[]{#group___stream_1gaf08dde4ae0b8acdff59bc4f5c77a261b .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipExtStreamGetCUMask]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipStream_t]{.pre}]{.n}[ ]{.w}[[stream]{.pre}]{.n .sig-param}, [[uint32_t]{.pre}]{.n}[ ]{.w}[[cuMaskSize]{.pre}]{.n .sig-param}, [[uint32_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[cuMask]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv421hipExtStreamGetCUMask11hipStream_t8uint32_tP8uint32_t "Link to this definition"){.headerlink}\

:   Gets CU mask associated with an asynchronous stream.

    
{.admonition .seealso}
    See also

    [[hipStreamCreate]{.std .std-ref}](#group___stream_1gaff5b62d6e9502d80879f7176f4d03102){.reference .internal}, [[hipStreamSynchronize]{.std .std-ref}](#group___stream_1gabbfb9f573a6ebe8c478605ecb5504a74){.reference .internal}, [[hipStreamWaitEvent]{.std .std-ref}](#group___stream_1gacdd84c8f8ef1539c96c57c1d5bcae633){.reference .internal}, [[hipStreamDestroy]{.std .std-ref}](#group___stream_1ga3076a3499ed2c7821311006100bb95ec){.reference .internal}
    

    Parameters[:]{.colon}

    :   - **stream** -- **\[in\]** Stream to be queried

        - **cuMaskSize** -- **\[in\]** Number of the block of memories (uint32_t \*) allocated by user

        - **cuMask** -- **\[out\]** Pointer to a pre-allocated block of memories (uint32_t \*) in which the stream's CU mask is returned. The CU mask is returned in a chunck of 32 bits where each active bit represents one active CU.

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidHandle, hipErrorInvalidValue

<!-- -->

[]{#_CPPv320hipStreamAddCallback11hipStream_t19hipStreamCallback_tPvj}[]{#_CPPv220hipStreamAddCallback11hipStream_t19hipStreamCallback_tPvj}[]{#hipStreamAddCallback__hipStream_t.hipStreamCallback_t.voidP.unsigned-i}[]{#group___stream_1ga3e098cd7478828b2104abb41a7bb00d3 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipStreamAddCallback]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipStream_t]{.pre}]{.n}[ ]{.w}[[stream]{.pre}]{.n .sig-param}, [[[hipStreamCallback_t]{.pre}]{.n}](#_CPPv419hipStreamCallback_t "hipStreamCallback_t"){.reference .internal}[ ]{.w}[[callback]{.pre}]{.n .sig-param}, [[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[userData]{.pre}]{.n .sig-param}, [[unsigned]{.pre}]{.kt}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[flags]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv420hipStreamAddCallback11hipStream_t19hipStreamCallback_tPvj "Link to this definition"){.headerlink}\

:   Adds a callback to be called on the host after all currently enqueued items in the stream have completed. For each hipStreamAddCallback call, a callback will be executed exactly once. The callback will block later work in the stream until it is finished.

    
{.admonition .seealso}
    See also

    [[hipStreamCreate]{.std .std-ref}](#group___stream_1gaff5b62d6e9502d80879f7176f4d03102){.reference .internal}, [[hipStreamCreateWithFlags]{.std .std-ref}](#group___stream_1gaf2382e3cc6632332a8983a0f58e43494){.reference .internal}, [[hipStreamQuery]{.std .std-ref}](#group___stream_1ga925b39ff78d3b5fd458bd9e2cade9f4e){.reference .internal}, [[hipStreamSynchronize]{.std .std-ref}](#group___stream_1gabbfb9f573a6ebe8c478605ecb5504a74){.reference .internal}, [[hipStreamWaitEvent]{.std .std-ref}](#group___stream_1gacdd84c8f8ef1539c96c57c1d5bcae633){.reference .internal}, [[hipStreamDestroy]{.std .std-ref}](#group___stream_1ga3076a3499ed2c7821311006100bb95ec){.reference .internal}, [[hipStreamCreateWithPriority]{.std .std-ref}](#group___stream_1gace005d8ea734fb66c995bd43dac3fd44){.reference .internal}
    

    Parameters[:]{.colon}

    :   - **stream** -- **\[in\]** - Stream to add callback to

        - **callback** -- **\[in\]** - The function to call once preceding stream operations are complete

        - **userData** -- **\[in\]** - User specified data to be passed to the callback function

        - **flags** -- **\[in\]** - Reserved for future use, must be 0

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidHandle, hipErrorNotSupported

<!-- -->

[]{#_CPPv321hipStreamSetAttribute11hipStream_t15hipStreamAttrIDPK18hipStreamAttrValue}[]{#_CPPv221hipStreamSetAttribute11hipStream_t15hipStreamAttrIDPK18hipStreamAttrValue}[]{#hipStreamSetAttribute__hipStream_t.hipStreamAttrID.hipStreamAttrValueCP}[]{#group___stream_1gac1aa936620145bf822f0318a9ac758c2 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipStreamSetAttribute]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipStream_t]{.pre}]{.n}[ ]{.w}[[stream]{.pre}]{.n .sig-param}, [[hipStreamAttrID]{.pre}]{.n}[ ]{.w}[[attr]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[hipStreamAttrValue]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[value]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv421hipStreamSetAttribute11hipStream_t15hipStreamAttrIDPK18hipStreamAttrValue "Link to this definition"){.headerlink}\

:   Sets stream attribute. Updated attribute is applied to work submitted to the stream.

    Parameters[:]{.colon}

    :   - **stream** -- **\[in\]** - Stream to set attributes to

        - **attr** -- **\[in\]** - Attribute ID for the attribute to set

        - **value** -- **\[in\]** - Attribute value for the attribute to set

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue, hipErrorInvalidResourceHandle

<!-- -->

[]{#_CPPv321hipStreamGetAttribute11hipStream_t15hipStreamAttrIDP18hipStreamAttrValue}[]{#_CPPv221hipStreamGetAttribute11hipStream_t15hipStreamAttrIDP18hipStreamAttrValue}[]{#hipStreamGetAttribute__hipStream_t.hipStreamAttrID.hipStreamAttrValueP}[]{#group___stream_1gaf111d0d141be35560d37e8a755f2ef4a .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipStreamGetAttribute]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipStream_t]{.pre}]{.n}[ ]{.w}[[stream]{.pre}]{.n .sig-param}, [[hipStreamAttrID]{.pre}]{.n}[ ]{.w}[[attr]{.pre}]{.n .sig-param}, [[hipStreamAttrValue]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[value_out]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv421hipStreamGetAttribute11hipStream_t15hipStreamAttrIDP18hipStreamAttrValue "Link to this definition"){.headerlink}\

:   queries stream attribute.

    Parameters[:]{.colon}

    :   - **stream** -- **\[in\]** - Stream to geet attributes from

        - **attr** -- **\[in\]** - Attribute ID for the attribute to query

        - **value** -- **\[out\]** - Attribute value output

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue, hipErrorInvalidResourceHandle

<!-- -->

[]{#_CPPv323hipStreamCopyAttributes11hipStream_t11hipStream_t}[]{#_CPPv223hipStreamCopyAttributes11hipStream_t11hipStream_t}[]{#hipStreamCopyAttributes__hipStream_t.hipStream_t}[]{#group___stream_1ga49a95255ce713ae1bbc341bf81678c1b .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipStreamCopyAttributes]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipStream_t]{.pre}]{.n}[ ]{.w}[[dst]{.pre}]{.n .sig-param}, [[hipStream_t]{.pre}]{.n}[ ]{.w}[[src]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv423hipStreamCopyAttributes11hipStream_t11hipStream_t "Link to this definition"){.headerlink}\

:   Copies attributes from source stream to destination stream.

    Parameters[:]{.colon}

    :   - **dst** -- **\[in\]** - Destination stream

        - **src** -- **\[in\]** - Source stream

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
