---
title: "Dispatch counting service &#8212; ROCprofiler-SDK 1.1.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/api-reference/rocprofiler-sdk_api/modules/dispatch_counting_service.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-03T06:26:36.000393+00:00
content_hash: "0da53c3029638b90"
---

# Dispatch counting service[#](#dispatch-counting-service)

-
typedef void (*rocprofiler_dispatch_counting_service_cb_t)(
[rocprofiler_dispatch_counting_service_data_t](#_CPPv444rocprofiler_dispatch_counting_service_data_t)dispatch_data,[rocprofiler_counter_config_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv431rocprofiler_counter_config_id_t)*config,[rocprofiler_user_data_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv423rocprofiler_user_data_t)*user_data, void *callback_data_args)[#](#_CPPv442rocprofiler_dispatch_counting_service_cb_t) (experimental) Kernel Dispatch Callback. This is a callback that is invoked before the kernel is enqueued into the HSA queue. What counters to collect for a kernel are set via passing back a profile config (config) in this callback. These counters will be collected and emplaced in the buffer with

[rocprofiler_buffer_id_t](../global_data_structures_topics_files/global_basic_data_types.html#structrocprofiler__buffer__id__t)used when setting up this callback.- Param dispatch_data:
**[in]**- Param config:
**[out]**Profile config detailing the counters to collect for this kernel- Param user_data:
**[out]**User data unique to this dispatch. Returned in record callback- Param callback_data_args:
**[in]**Callback supplied via buffered_dispatch_counting_service


-
typedef void (*rocprofiler_dispatch_counting_record_cb_t)(
[rocprofiler_dispatch_counting_service_data_t](#_CPPv444rocprofiler_dispatch_counting_service_data_t)dispatch_data,[rocprofiler_counter_record_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv428rocprofiler_counter_record_t)*record_data, unsigned long record_count,[rocprofiler_user_data_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv423rocprofiler_user_data_t)user_data, void *callback_data_args)[#](#_CPPv441rocprofiler_dispatch_counting_record_cb_t) (experimental) Counting record callback. This is a callback is invoked when the kernel execution is complete and contains the counter profile data requested in

[rocprofiler_dispatch_counting_service_cb_t](#group__dispatch__counting__service_1ga7a3ad5fd51cdf8cfecd138fda01ec223). Only used with[rocprofiler_configure_callback_dispatch_counting_service](#group__dispatch__counting__service_1ga20ddd899611f773a6f82aa102ede07ae).- Param dispatch_data:
**[in]**- Param record_data:
**[in]**Counter record data.- Param record_count:
**[in]**Number of counter records.- Param user_data:
**[in]**User data instance from dispatch callback- Param callback_data_args:
**[in]**Callback supplied via buffered_dispatch_counting_service


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_configure_buffer_dispatch_counting_service([rocprofiler_context_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv424rocprofiler_context_id_t)context_id,[rocprofiler_buffer_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv423rocprofiler_buffer_id_t)buffer_id,[rocprofiler_dispatch_counting_service_cb_t](#_CPPv442rocprofiler_dispatch_counting_service_cb_t)callback, void *callback_data_args)[#](#_CPPv454rocprofiler_configure_buffer_dispatch_counting_service24rocprofiler_context_id_t23rocprofiler_buffer_id_t42rocprofiler_dispatch_counting_service_cb_tPv) (experimental) Configure buffered dispatch profile Counting Service. Collects the counters in dispatch packets and stores them in a buffer with

`buffer_id`

. The buffer may contain packets from more than one dispatch (denoted by correlation id). Will trigger the callback based on the parameters setup in buffer_id_t.NOTE: Interface is up for comment as to whether restrictions on agent should be made here (limiting the CB based on agent) or if the restriction should be performed by the tool in

[rocprofiler_dispatch_counting_service_cb_t](#group__dispatch__counting__service_1ga7a3ad5fd51cdf8cfecd138fda01ec223)(i.e. tool code checking the agent param to see if they want to profile it).Interface is up for comment as to whether restrictions on agent should be made here (limiting the CB based on agent) or if the restriction should be performed by the tool in

[rocprofiler_dispatch_counting_service_cb_t](#group__dispatch__counting__service_1ga7a3ad5fd51cdf8cfecd138fda01ec223)(i.e. tool code checking the agent param to see if they want to profile it).- Parameters:
**context_id**–**[in]**context id**buffer_id**–**[in]**id of the buffer to use for the counting service**callback**–**[in]**callback to perform when dispatch is enqueued**callback_data_args**–**[in]**callback data

- Returns:


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_configure_callback_dispatch_counting_service([rocprofiler_context_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv424rocprofiler_context_id_t)context_id,[rocprofiler_dispatch_counting_service_cb_t](#_CPPv442rocprofiler_dispatch_counting_service_cb_t)dispatch_callback, void *dispatch_callback_args,[rocprofiler_dispatch_counting_record_cb_t](#_CPPv441rocprofiler_dispatch_counting_record_cb_t)record_callback, void *record_callback_args)[#](#_CPPv456rocprofiler_configure_callback_dispatch_counting_service24rocprofiler_context_id_t42rocprofiler_dispatch_counting_service_cb_tPv41rocprofiler_dispatch_counting_record_cb_tPv) (experimental) Configure buffered dispatch profile Counting Service. Collects the counters in dispatch packets and calls a callback with the counters collected during that dispatch.

- Parameters:
**context_id**–**[in]**context id**dispatch_callback**–**[in]**callback to perform when dispatch is enqueued**dispatch_callback_args**–**[in]**callback data for dispatch callback**record_callback**–**[in]**Record callback for completed profile data**record_callback_args**–**[in]**Callback args for record callback

- Returns:


-
struct rocprofiler_dispatch_counting_service_data_t
[#](#_CPPv444rocprofiler_dispatch_counting_service_data_t) *#include <rocprofiler-sdk/dispatch_counting_service.h>*(experimental) Kernel dispatch data for profile counting callbacks.


-
struct rocprofiler_dispatch_counting_service_record_t
[#](#_CPPv446rocprofiler_dispatch_counting_service_record_t) *#include <rocprofiler-sdk/dispatch_counting_service.h>*(experimental) ROCProfiler Profile Counting Counter Record Header Information

This is buffer equivalent of

[rocprofiler_dispatch_counting_service_data_t](#structrocprofiler__dispatch__counting__service__data__t)
