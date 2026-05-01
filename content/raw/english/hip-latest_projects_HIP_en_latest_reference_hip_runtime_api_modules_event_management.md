---
title: "Event management &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/reference/hip_runtime_api/modules/event_management.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T06:59:11.673590+00:00
content_hash: "f8d22bcc1d52c0e2"
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
# Event management

::
{#print-main-content}
:
{#jb-print-toc}

{}
## Contents

:
::

{#searchbox}

{#event-management .section}
[]{#event-management-reference}

# Event management[\#](#event-management "Link to this heading"){.headerlink}

[]{#_CPPv323hipEventCreateWithFlagsP10hipEvent_tj}[]{#_CPPv223hipEventCreateWithFlagsP10hipEvent_tj}[]{#hipEventCreateWithFlags__hipEvent_tP.unsigned}[]{#group___event_1gae86a5acb1b22b61bc9ecb9c28fc71b75 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipEventCreateWithFlags]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipEvent_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[event]{.pre}]{.n .sig-param}, [[unsigned]{.pre}]{.kt}[ ]{.w}[[flags]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv423hipEventCreateWithFlagsP10hipEvent_tj "Link to this definition"){.headerlink}\

:   Create an event with the specified flags.

    
{.admonition .seealso}
    See also

    [[hipEventCreate]{.std .std-ref}](#group___event_1ga5df2309c9f29ca4c8e669db658d411b4){.reference .internal}, [[hipEventSynchronize]{.std .std-ref}](#group___event_1ga1f72d98ba5d6f7dc3da54e0c41fe38b1){.reference .internal}, [[hipEventDestroy]{.std .std-ref}](#group___event_1ga83260357dce0c39e8c6a3c74ec97484c){.reference .internal}, [[hipEventElapsedTime]{.std .std-ref}](#group___event_1gad4128b815cb475c8e13c7e66ff6250b7){.reference .internal}
    

    Parameters[:]{.colon}

    :   - **event** -- **\[inout\]** Returns the newly created event.

        - **flags** -- **\[in\]** Flags to control event behavior. Valid values are hipEventDefault, hipEventBlockingSync, hipEventDisableTiming, hipEventInterprocess hipEventDefault : Default flag. The event will use active synchronization and will support timing. Blocking synchronization provides lowest possible latency at the expense of dedicating a CPU to poll on the event. hipEventBlockingSync : The event will use blocking synchronization : if hipEventSynchronize is called on this event, the thread will block until the event completes. This can increase latency for the synchroniation but can result in lower power and more resources for other CPU threads. hipEventDisableTiming : Disable recording of timing information. Events created with this flag would not record profiling data and provide best performance if used for synchronization. hipEventInterprocess : The event can be used as an interprocess event. hipEventDisableTiming flag also must be set when hipEventInterprocess flag is set. hipEventDisableSystemFence : Disable acquire and release system scope fence. This may improve performance but device memory may not be visible to the host and other devices if this flag is set.

    Returns[:]{.colon}

    :   hipSuccess, hipErrorNotInitialized, hipErrorInvalidValue, hipErrorLaunchFailure, hipErrorOutOfMemory

<!-- -->

[]{#_CPPv314hipEventCreateP10hipEvent_t}[]{#_CPPv214hipEventCreateP10hipEvent_t}[]{#hipEventCreate__hipEvent_tP}[]{#group___event_1ga5df2309c9f29ca4c8e669db658d411b4 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipEventCreate]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipEvent_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[event]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv414hipEventCreateP10hipEvent_t "Link to this definition"){.headerlink}\

:   Create an event

    
{.admonition .seealso}
    See also

    [[hipEventCreateWithFlags]{.std .std-ref}](#group___event_1gae86a5acb1b22b61bc9ecb9c28fc71b75){.reference .internal}, [[hipEventRecord]{.std .std-ref}](#group___event_1gace88ebd8c7ec42a6c2cebda2e8b0cb38){.reference .internal}, [[hipEventQuery]{.std .std-ref}](#group___event_1ga5d12d7b798b5ceb5932d1ac21f5ac776){.reference .internal}, [[hipEventSynchronize]{.std .std-ref}](#group___event_1ga1f72d98ba5d6f7dc3da54e0c41fe38b1){.reference .internal}, [[hipEventDestroy]{.std .std-ref}](#group___event_1ga83260357dce0c39e8c6a3c74ec97484c){.reference .internal}, [[hipEventElapsedTime]{.std .std-ref}](#group___event_1gad4128b815cb475c8e13c7e66ff6250b7){.reference .internal}
    

    Parameters[:]{.colon}

    :   **event** -- **\[inout\]** Returns the newly created event.

    Returns[:]{.colon}

    :   hipSuccess, hipErrorNotInitialized, hipErrorInvalidValue, hipErrorLaunchFailure, hipErrorOutOfMemory

<!-- -->

[]{#_CPPv323hipEventRecordWithFlags10hipEvent_t11hipStream_tj}[]{#_CPPv223hipEventRecordWithFlags10hipEvent_t11hipStream_tj}[]{#hipEventRecordWithFlags__hipEvent_t.hipStream_t.unsigned-i}[]{#group___event_1gac7b7a416a110f5e1c1a972498c6db698 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipEventRecordWithFlags]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipEvent_t]{.pre}]{.n}[ ]{.w}[[event]{.pre}]{.n .sig-param}, [[hipStream_t]{.pre}]{.n}[ ]{.w}[[stream]{.pre}]{.n .sig-param}, [[unsigned]{.pre}]{.kt}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[flags]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv423hipEventRecordWithFlags10hipEvent_t11hipStream_tj "Link to this definition"){.headerlink}\

:   Record an event in the specified stream.

    [[hipEventQuery()]{.std .std-ref}](#group___event_1ga5d12d7b798b5ceb5932d1ac21f5ac776){.reference .internal} or [[hipEventSynchronize()]{.std .std-ref}](#group___event_1ga1f72d98ba5d6f7dc3da54e0c41fe38b1){.reference .internal} must be used to determine when the event transitions from "recording" (after [[hipEventRecord()]{.std .std-ref}](#group___event_1gace88ebd8c7ec42a6c2cebda2e8b0cb38){.reference .internal} is called) to "recorded" (when timestamps are set, if requested).

    Events which are recorded in a non-NULL stream will transition to from recording to "recorded" state when they reach the head of the specified stream, after all previous commands in that stream have completed executing.

    Flags include: hipEventRecordDefault: Default event creation flag. hipEventRecordExternal: Event is captured in the graph as an external event node when performing stream capture

    If [[hipEventRecord()]{.std .std-ref}](#group___event_1gace88ebd8c7ec42a6c2cebda2e8b0cb38){.reference .internal} has been previously called on this event, then this call will overwrite any existing state in event.

    If this function is called on an event that is currently being recorded, results are undefined

    - either outstanding recording may save state into the event, and the order is not guaranteed.

    
{.admonition .seealso}
    See also

    [[hipEventCreate]{.std .std-ref}](#group___event_1ga5df2309c9f29ca4c8e669db658d411b4){.reference .internal}, [[hipEventCreateWithFlags]{.std .std-ref}](#group___event_1gae86a5acb1b22b61bc9ecb9c28fc71b75){.reference .internal}, [[hipEventQuery]{.std .std-ref}](#group___event_1ga5d12d7b798b5ceb5932d1ac21f5ac776){.reference .internal}, [[hipEventSynchronize]{.std .std-ref}](#group___event_1ga1f72d98ba5d6f7dc3da54e0c41fe38b1){.reference .internal}, [[hipEventDestroy]{.std .std-ref}](#group___event_1ga83260357dce0c39e8c6a3c74ec97484c){.reference .internal}, [[hipEventElapsedTime]{.std .std-ref}](#group___event_1gad4128b815cb475c8e13c7e66ff6250b7){.reference .internal}
    

    
{.admonition .note}
    Note

    : If this function is not called before use [[hipEventQuery()]{.std .std-ref}](#group___event_1ga5d12d7b798b5ceb5932d1ac21f5ac776){.reference .internal} or [[hipEventSynchronize()]{.std .std-ref}](#group___event_1ga1f72d98ba5d6f7dc3da54e0c41fe38b1){.reference .internal}, hipSuccess is returned, meaning no pending event in the stream.
    

    Parameters[:]{.colon}

    :   - **event** -- **\[in\]** event to record.

        - **stream** -- **\[in\]** stream in which to record event.

        - **flags** -- **\[in\]** parameter for operations

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue, hipErrorNotInitialized, hipErrorInvalidHandle, hipErrorLaunchFailure

<!-- -->

[]{#_CPPv314hipEventRecord10hipEvent_t11hipStream_t}[]{#_CPPv214hipEventRecord10hipEvent_t11hipStream_t}[]{#hipEventRecord__hipEvent_t.hipStream_t}[]{#group___event_1gace88ebd8c7ec42a6c2cebda2e8b0cb38 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipEventRecord]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipEvent_t]{.pre}]{.n}[ ]{.w}[[event]{.pre}]{.n .sig-param}, [[hipStream_t]{.pre}]{.n}[ ]{.w}[[stream]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[NULL]{.pre}]{.n}[)]{.sig-paren}[\#](#_CPPv414hipEventRecord10hipEvent_t11hipStream_t "Link to this definition"){.headerlink}\

:   Record an event in the specified stream.

    [[hipEventQuery()]{.std .std-ref}](#group___event_1ga5d12d7b798b5ceb5932d1ac21f5ac776){.reference .internal} or [[hipEventSynchronize()]{.std .std-ref}](#group___event_1ga1f72d98ba5d6f7dc3da54e0c41fe38b1){.reference .internal} must be used to determine when the event transitions from "recording" (after [[hipEventRecord()]{.std .std-ref}](#group___event_1gace88ebd8c7ec42a6c2cebda2e8b0cb38){.reference .internal} is called) to "recorded" (when timestamps are set, if requested).

    Events which are recorded in a non-NULL stream will transition to from recording to "recorded" state when they reach the head of the specified stream, after all previous commands in that stream have completed executing.

    If [[hipEventRecord()]{.std .std-ref}](#group___event_1gace88ebd8c7ec42a6c2cebda2e8b0cb38){.reference .internal} has been previously called on this event, then this call will overwrite any existing state in event.

    If this function is called on an event that is currently being recorded, results are undefined

    - either outstanding recording may save state into the event, and the order is not guaranteed.

    
{.admonition .seealso}
    See also

    [[hipEventCreate]{.std .std-ref}](#group___event_1ga5df2309c9f29ca4c8e669db658d411b4){.reference .internal}, [[hipEventCreateWithFlags]{.std .std-ref}](#group___event_1gae86a5acb1b22b61bc9ecb9c28fc71b75){.reference .internal}, [[hipEventQuery]{.std .std-ref}](#group___event_1ga5d12d7b798b5ceb5932d1ac21f5ac776){.reference .internal}, [[hipEventSynchronize]{.std .std-ref}](#group___event_1ga1f72d98ba5d6f7dc3da54e0c41fe38b1){.reference .internal}, [[hipEventDestroy]{.std .std-ref}](#group___event_1ga83260357dce0c39e8c6a3c74ec97484c){.reference .internal}, [[hipEventElapsedTime]{.std .std-ref}](#group___event_1gad4128b815cb475c8e13c7e66ff6250b7){.reference .internal}
    

    
{.admonition .note}
    Note

    If this function is not called before use [[hipEventQuery()]{.std .std-ref}](#group___event_1ga5d12d7b798b5ceb5932d1ac21f5ac776){.reference .internal} or [[hipEventSynchronize()]{.std .std-ref}](#group___event_1ga1f72d98ba5d6f7dc3da54e0c41fe38b1){.reference .internal}, hipSuccess is returned, meaning no pending event in the stream.
    

    Parameters[:]{.colon}

    :   - **event** -- **\[in\]** event to record.

        - **stream** -- **\[in\]** stream in which to record event.

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue, hipErrorNotInitialized, hipErrorInvalidHandle, hipErrorLaunchFailure

<!-- -->

[]{#_CPPv315hipEventDestroy10hipEvent_t}[]{#_CPPv215hipEventDestroy10hipEvent_t}[]{#hipEventDestroy__hipEvent_t}[]{#group___event_1ga83260357dce0c39e8c6a3c74ec97484c .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipEventDestroy]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipEvent_t]{.pre}]{.n}[ ]{.w}[[event]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv415hipEventDestroy10hipEvent_t "Link to this definition"){.headerlink}\

:   Destroy the specified event.

    Releases memory associated with the event. If the event is recording but has not completed recording when [[hipEventDestroy()]{.std .std-ref}](#group___event_1ga83260357dce0c39e8c6a3c74ec97484c){.reference .internal} is called, the function will return immediately and the completion_future resources will be released later, when the hipDevice is synchronized.

    
{.admonition .seealso}
    See also

    [[hipEventCreate]{.std .std-ref}](#group___event_1ga5df2309c9f29ca4c8e669db658d411b4){.reference .internal}, [[hipEventCreateWithFlags]{.std .std-ref}](#group___event_1gae86a5acb1b22b61bc9ecb9c28fc71b75){.reference .internal}, [[hipEventQuery]{.std .std-ref}](#group___event_1ga5d12d7b798b5ceb5932d1ac21f5ac776){.reference .internal}, [[hipEventSynchronize]{.std .std-ref}](#group___event_1ga1f72d98ba5d6f7dc3da54e0c41fe38b1){.reference .internal}, [[hipEventRecord]{.std .std-ref}](#group___event_1gace88ebd8c7ec42a6c2cebda2e8b0cb38){.reference .internal}, [[hipEventElapsedTime]{.std .std-ref}](#group___event_1gad4128b815cb475c8e13c7e66ff6250b7){.reference .internal}
    

    Parameters[:]{.colon}

    :   **event** -- **\[in\]** Event to destroy.

    Returns[:]{.colon}

    :   hipSuccess, hipErrorNotInitialized, hipErrorInvalidValue, hipErrorLaunchFailure

    Returns[:]{.colon}

    :   hipSuccess

<!-- -->

[]{#_CPPv319hipEventSynchronize10hipEvent_t}[]{#_CPPv219hipEventSynchronize10hipEvent_t}[]{#hipEventSynchronize__hipEvent_t}[]{#group___event_1ga1f72d98ba5d6f7dc3da54e0c41fe38b1 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipEventSynchronize]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipEvent_t]{.pre}]{.n}[ ]{.w}[[event]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv419hipEventSynchronize10hipEvent_t "Link to this definition"){.headerlink}\

:   Wait for an event to complete.

    This function will block until the event is ready, waiting for all previous work in the stream specified when event was recorded with [[hipEventRecord()]{.std .std-ref}](#group___event_1gace88ebd8c7ec42a6c2cebda2e8b0cb38){.reference .internal}.

    If [[hipEventRecord()]{.std .std-ref}](#group___event_1gace88ebd8c7ec42a6c2cebda2e8b0cb38){.reference .internal} has not been called on [`event`{.docutils .literal .notranslate}]{.pre}, this function returns hipSuccess when no event is captured.

    
{.admonition .seealso}
    See also

    [[hipEventCreate]{.std .std-ref}](#group___event_1ga5df2309c9f29ca4c8e669db658d411b4){.reference .internal}, [[hipEventCreateWithFlags]{.std .std-ref}](#group___event_1gae86a5acb1b22b61bc9ecb9c28fc71b75){.reference .internal}, [[hipEventQuery]{.std .std-ref}](#group___event_1ga5d12d7b798b5ceb5932d1ac21f5ac776){.reference .internal}, [[hipEventDestroy]{.std .std-ref}](#group___event_1ga83260357dce0c39e8c6a3c74ec97484c){.reference .internal}, [[hipEventRecord]{.std .std-ref}](#group___event_1gace88ebd8c7ec42a6c2cebda2e8b0cb38){.reference .internal}, [[hipEventElapsedTime]{.std .std-ref}](#group___event_1gad4128b815cb475c8e13c7e66ff6250b7){.reference .internal}
    

    Parameters[:]{.colon}

    :   **event** -- **\[in\]** Event on which to wait.

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue, hipErrorNotInitialized, hipErrorInvalidHandle, hipErrorLaunchFailure

<!-- -->

[]{#_CPPv319hipEventElapsedTimePf10hipEvent_t10hipEvent_t}[]{#_CPPv219hipEventElapsedTimePf10hipEvent_t10hipEvent_t}[]{#hipEventElapsedTime__floatP.hipEvent_t.hipEvent_t}[]{#group___event_1gad4128b815cb475c8e13c7e66ff6250b7 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipEventElapsedTime]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[float]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[ms]{.pre}]{.n .sig-param}, [[hipEvent_t]{.pre}]{.n}[ ]{.w}[[start]{.pre}]{.n .sig-param}, [[hipEvent_t]{.pre}]{.n}[ ]{.w}[[stop]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv419hipEventElapsedTimePf10hipEvent_t10hipEvent_t "Link to this definition"){.headerlink}\

:   Return the elapsed time between two events.

    Computes the elapsed time between two events. Time is computed in ms, with a resolution of approximately 1 us.

    Events which are recorded in a NULL stream will block until all commands on all other streams complete execution, and then record the timestamp.

    Events which are recorded in a non-NULL stream will record their timestamp when they reach the head of the specified stream, after all previous commands in that stream have completed executing. Thus the time that the event recorded may be significantly after the host calls [[hipEventRecord()]{.std .std-ref}](#group___event_1gace88ebd8c7ec42a6c2cebda2e8b0cb38){.reference .internal}.

    If [[hipEventRecord()]{.std .std-ref}](#group___event_1gace88ebd8c7ec42a6c2cebda2e8b0cb38){.reference .internal} has not been called on either event, then hipErrorInvalidHandle is returned. If [[hipEventRecord()]{.std .std-ref}](#group___event_1gace88ebd8c7ec42a6c2cebda2e8b0cb38){.reference .internal} has been called on both events, but the timestamp has not yet been recorded on one or both events (that is, [[hipEventQuery()]{.std .std-ref}](#group___event_1ga5d12d7b798b5ceb5932d1ac21f5ac776){.reference .internal} would return hipErrorNotReady on at least one of the events), then hipErrorNotReady is returned.

    
{.admonition .seealso}
    See also

    [[hipEventCreate]{.std .std-ref}](#group___event_1ga5df2309c9f29ca4c8e669db658d411b4){.reference .internal}, [[hipEventCreateWithFlags]{.std .std-ref}](#group___event_1gae86a5acb1b22b61bc9ecb9c28fc71b75){.reference .internal}, [[hipEventQuery]{.std .std-ref}](#group___event_1ga5d12d7b798b5ceb5932d1ac21f5ac776){.reference .internal}, [[hipEventDestroy]{.std .std-ref}](#group___event_1ga83260357dce0c39e8c6a3c74ec97484c){.reference .internal}, [[hipEventRecord]{.std .std-ref}](#group___event_1gace88ebd8c7ec42a6c2cebda2e8b0cb38){.reference .internal}, [[hipEventSynchronize]{.std .std-ref}](#group___event_1ga1f72d98ba5d6f7dc3da54e0c41fe38b1){.reference .internal}
    

    Parameters[:]{.colon}

    :   - **ms** -- **\[out\]** : Return time between start and stop in ms.

        - **start** -- **\[in\]** : Start event.

        - **stop** -- **\[in\]** : Stop event.

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue, hipErrorNotReady, hipErrorInvalidHandle, hipErrorNotInitialized, hipErrorLaunchFailure

<!-- -->

[]{#_CPPv313hipEventQuery10hipEvent_t}[]{#_CPPv213hipEventQuery10hipEvent_t}[]{#hipEventQuery__hipEvent_t}[]{#group___event_1ga5d12d7b798b5ceb5932d1ac21f5ac776 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipEventQuery]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipEvent_t]{.pre}]{.n}[ ]{.w}[[event]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv413hipEventQuery10hipEvent_t "Link to this definition"){.headerlink}\

:   Query event status.

    Query the status of the specified event. This function will return hipSuccess if all commands in the appropriate stream (specified to [[hipEventRecord()]{.std .std-ref}](#group___event_1gace88ebd8c7ec42a6c2cebda2e8b0cb38){.reference .internal}) have completed. If any execution has not completed, then hipErrorNotReady is returned.

    
{.admonition .seealso}
    See also

    [[hipEventCreate]{.std .std-ref}](#group___event_1ga5df2309c9f29ca4c8e669db658d411b4){.reference .internal}, [[hipEventCreateWithFlags]{.std .std-ref}](#group___event_1gae86a5acb1b22b61bc9ecb9c28fc71b75){.reference .internal}, [[hipEventRecord]{.std .std-ref}](#group___event_1gace88ebd8c7ec42a6c2cebda2e8b0cb38){.reference .internal}, [[hipEventDestroy]{.std .std-ref}](#group___event_1ga83260357dce0c39e8c6a3c74ec97484c){.reference .internal}, [[hipEventSynchronize]{.std .std-ref}](#group___event_1ga1f72d98ba5d6f7dc3da54e0c41fe38b1){.reference .internal}, [[hipEventElapsedTime]{.std .std-ref}](#group___event_1gad4128b815cb475c8e13c7e66ff6250b7){.reference .internal}
    

    
{.admonition .note}
    Note

    This API returns hipSuccess, if [[hipEventRecord()]{.std .std-ref}](#group___event_1gace88ebd8c7ec42a6c2cebda2e8b0cb38){.reference .internal} is not called before this API.
    

    Parameters[:]{.colon}

    :   **event** -- **\[in\]** Event to query.

    Returns[:]{.colon}

    :   hipSuccess, hipErrorNotReady, hipErrorInvalidHandle, hipErrorInvalidValue, hipErrorNotInitialized, hipErrorLaunchFailure

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
