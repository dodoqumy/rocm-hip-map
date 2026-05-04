---
title: "Device counting service &#8212; ROCprofiler-SDK 1.1.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/api-reference/rocprofiler-sdk_api/modules/device_counting_service.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T18:58:42.640057+00:00
content_hash: "08adc3df21ab4ece"
---

# Device counting service[#](#device-counting-service)

-
typedef
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)(*rocprofiler_device_counting_agent_cb_t)([rocprofiler_context_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv424rocprofiler_context_id_t)context_id,[rocprofiler_counter_config_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv431rocprofiler_counter_config_id_t)config_id)[#](#_CPPv438rocprofiler_device_counting_agent_cb_t) (experimental) Callback to set the profile config for the agent.

- Param context_id:
**[in]**context id- Param config_id:
**[in]**Profile config detailing the counters to collect for this kernel- Retval ROCPROFILER_STATUS_ERROR_PROFILE_NOT_FOUND:
Returned if the config_id is not found

- Retval ROCPROFILER_STATUS_ERROR_CONTEXT_INVALID:
Returned if the ctx is not valid

- Retval ROCPROFILER_STATUS_ERROR_CONFIGURATION_LOCKED:
Returned if attempting to make this call outside of context startup.

- Retval ROCPROFILER_STATUS_ERROR_AGENT_MISMATCH:
Agent of profile does not match agent of the context.

- Retval ROCPROFILER_STATUS_SUCCESS:
Returned if succesfully configured

- Return:


-
typedef void (*rocprofiler_device_counting_service_cb_t)(
[rocprofiler_context_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv424rocprofiler_context_id_t)context_id,[rocprofiler_agent_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv422rocprofiler_agent_id_t)agent_id,[rocprofiler_device_counting_agent_cb_t](#_CPPv438rocprofiler_device_counting_agent_cb_t)set_config, void *user_data)[#](#_CPPv440rocprofiler_device_counting_service_cb_t) (experimental) Configure Profile Counting Service for agent. Called when the context is started. Selects the counters to be used for agent profiling.

- Param context_id:
**[in]**context id- Param agent_id:
**[in]**agent id- Param set_config:
**[in]**Function to call to set the profile config (see rocprofiler_device_counting_agent_cb_t)- Param user_data:
**[in]**Data supplied to rocprofiler_configure_device_counting_service


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_configure_device_counting_service([rocprofiler_context_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv424rocprofiler_context_id_t)context_id,[rocprofiler_buffer_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv423rocprofiler_buffer_id_t)buffer_id,[rocprofiler_agent_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv422rocprofiler_agent_id_t)agent_id,[rocprofiler_device_counting_service_cb_t](#_CPPv440rocprofiler_device_counting_service_cb_t)cb, void *user_data)[#](#_CPPv445rocprofiler_configure_device_counting_service24rocprofiler_context_id_t23rocprofiler_buffer_id_t22rocprofiler_agent_id_t40rocprofiler_device_counting_service_cb_tPv) (experimental) Configure Device Counting Service for agent. There may only be one counting service configured per agent in a context and can be only one active context that is profiling a single agent at a time. Multiple agent contexts can be started at the same time if they are profiling different agents.

- Parameters:
**context_id**–**[in]**context id**buffer_id**–**[in]**id of the buffer to use for the counting service. When rocprofiler_sample_device_counting_service is called, counter data will be written to this buffer. If the input buffer id is null (i.e.

), the counter data will not be written to a buffer and will only be returned in the output_records of rocprofiler_sample_device_counting_service[rocprofiler_buffer_id_t](../global_data_structures_topics_files/global_basic_data_types.html#structrocprofiler__buffer__id__t){.handle = 0}**agent_id**–**[in]**agent to configure profiling on.**cb**–**[in]**Callback called when the context is started for the tool to specify what counters to collect ([rocprofiler_counter_config_id_t](../global_data_structures_topics_files/global_basic_data_types.html#structrocprofiler__counter__config__id__t)).**user_data**–**[in]**User supplied data to be passed to the callback cb when triggered

- Return values:
**ROCPROFILER_STATUS_ERROR_CONTEXT_INVALID**– Returned if the context does not exist.**ROCPROFILER_STATUS_ERROR_BUFFER_NOT_FOUND**– Returned if the buffer is not found.**ROCPROFILER_STATUS_ERROR_INVALID_ARGUMENT**– Returned if context already has agent profiling configured for agent_id.**ROCPROFILER_STATUS_SUCCESS**– Returned if succesfully configured

- Returns:


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_sample_device_counting_service([rocprofiler_context_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv424rocprofiler_context_id_t)context_id,[rocprofiler_user_data_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv423rocprofiler_user_data_t)user_data,[rocprofiler_counter_flag_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv426rocprofiler_counter_flag_t)flags,[rocprofiler_counter_record_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv428rocprofiler_counter_record_t)*output_records, unsigned long *rec_count)[#](#_CPPv442rocprofiler_sample_device_counting_service24rocprofiler_context_id_t23rocprofiler_user_data_t26rocprofiler_counter_flag_tP28rocprofiler_counter_record_tPm) (experimental) Trigger a read of the counter data for the agent profile. The counter data will be written to the buffer specified in rocprofiler_configure_device_counting_service. The data in

[rocprofiler_user_data_t](../global_data_structures_topics_files/global_basic_data_types.html#unionrocprofiler__user__data__t)will be written to the buffer along with the counter data. flags can be used to specify if this call should be performed asynchronously (default is synchronous).- Parameters:
**context_id**–**[in]**context id**user_data**–**[in]**User supplied data, included in records outputted to buffer.**flags**–**[in]**Flags to specify how the counter data should be collected (defaults to sync).**output_records**–**[in]**(Optional) Provides the values immediately instead of outputting to buffer. Must be allocated by caller.**rec_count**–**[in]**(Optional) On entry, this is the maximum number of records rocprof can store in output_records. On exit, contains the number of actual records.

- Return values:
**ROCPROFILER_STATUS_ERROR_CONTEXT_INVALID**– Returned if the context does not exist or the context is not configured for agent profiling.**ROCPROFILER_STATUS_ERROR_CONTEXT_ERROR**– Returned if another operation is in progress ( start/stop ctx or another read).**ROCPROFILER_STATUS_ERROR**– Returned if HSA has not been initialized yet.**ROCPROFILER_STATUS_ERROR_OUT_OF_RESOURCES**– Returned output_records is set but size is too small to store results**ROCPROFILER_STATUS_SUCCESS**– Returned if read request was successful.**ROCPROFILER_STATUS_ERROR_INVALID_ARGUMENT**– Returned If ASYNC is being used while output_records is not null.

- Returns:
