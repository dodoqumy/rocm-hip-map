---
title: "External correlation &#8212; ROCprofiler-SDK 1.1.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/api-reference/rocprofiler-sdk_api/modules/external_correalation.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:24:36.537175+00:00
content_hash: "97f9baf5a68bd12f"
---

# External correlation[#](#external-correlation)

-
enum rocprofiler_external_correlation_id_request_kind_t
[#](#_CPPv450rocprofiler_external_correlation_id_request_kind_t) (experimental) ROCProfiler External Correlation ID Operations.

These kinds correspond to callback and buffered tracing kinds (

See also

[rocprofiler_callback_tracing_kind_t](../global_data_structures_topics_files/global_basic_data_types.html#group___b_a_s_i_c___d_a_t_a___t_y_p_e_s_1gae2325388cbfe6e72f7b7eaa0738c52a9)and[rocprofiler_buffer_tracing_kind_t](../global_data_structures_topics_files/global_basic_data_types.html#group___b_a_s_i_c___d_a_t_a___t_y_p_e_s_1gac2eecbf4d5542df3b35fc26837fac59b)) which generate correlation IDs. Typically, rocprofiler-sdk uses the most recent external correlation ID on the current thread set via[rocprofiler_push_external_correlation_id](#group___e_x_t_e_r_n_a_l___c_o_r_r_e_l_a_t_i_o_n_1ga76c85d6440888d1e429d5dd6ae111a16); however, this approach can be problematic if a new external correlation ID should be set before the[ROCPROFILER_CALLBACK_PHASE_ENTER](../global_data_structures_topics_files/global_basic_data_types.html#group___b_a_s_i_c___d_a_t_a___t_y_p_e_s_1ggaaa6a432135a8014cfdb1b1abdfa9e6eda90754f965f00a1b8e94679ba07de20b9)callback or if relevant external correlation IDs are desired when the buffered tracing is used. Thus, rocprofiler-sdk provides a way for tools to get a callback whenever an external correlation ID is needed. However, this can add significant overhead for those who only need these callbacks for, say, kernel dispatches while the HSA API is being traced (i.e. lots of callbacks for HSA API functions). The enumeration below is provided to ensure that tools can default to using the external correlation IDs set via the push/pop methods where the external correlation ID value is not important while also getting a request for an external correlation ID for other tracing kinds.*Values:*-
enumerator ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_NONE
[#](#_CPPv4N50rocprofiler_external_correlation_id_request_kind_t45ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_NONEE) Unknown kind.


-
enumerator ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_HSA_CORE_API
[#](#_CPPv4N50rocprofiler_external_correlation_id_request_kind_t53ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_HSA_CORE_APIE)

-
enumerator ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_HSA_AMD_EXT_API
[#](#_CPPv4N50rocprofiler_external_correlation_id_request_kind_t56ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_HSA_AMD_EXT_APIE)

-
enumerator ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_HSA_IMAGE_EXT_API
[#](#_CPPv4N50rocprofiler_external_correlation_id_request_kind_t58ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_HSA_IMAGE_EXT_APIE)

-
enumerator ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_HSA_FINALIZE_EXT_API
[#](#_CPPv4N50rocprofiler_external_correlation_id_request_kind_t61ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_HSA_FINALIZE_EXT_APIE)

-
enumerator ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_HIP_RUNTIME_API
[#](#_CPPv4N50rocprofiler_external_correlation_id_request_kind_t56ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_HIP_RUNTIME_APIE)

-
enumerator ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_HIP_COMPILER_API
[#](#_CPPv4N50rocprofiler_external_correlation_id_request_kind_t57ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_HIP_COMPILER_APIE)

-
enumerator ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_MARKER_CORE_API
[#](#_CPPv4N50rocprofiler_external_correlation_id_request_kind_t56ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_MARKER_CORE_APIE)

-
enumerator ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_MARKER_CONTROL_API
[#](#_CPPv4N50rocprofiler_external_correlation_id_request_kind_t59ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_MARKER_CONTROL_APIE)

-
enumerator ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_MARKER_NAME_API
[#](#_CPPv4N50rocprofiler_external_correlation_id_request_kind_t56ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_MARKER_NAME_APIE)

-
enumerator ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_MEMORY_COPY
[#](#_CPPv4N50rocprofiler_external_correlation_id_request_kind_t52ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_MEMORY_COPYE)

-
enumerator ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_KERNEL_DISPATCH
[#](#_CPPv4N50rocprofiler_external_correlation_id_request_kind_t56ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_KERNEL_DISPATCHE)

-
enumerator ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_SCRATCH_MEMORY
[#](#_CPPv4N50rocprofiler_external_correlation_id_request_kind_t55ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_SCRATCH_MEMORYE)

-
enumerator ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_RCCL_API
[#](#_CPPv4N50rocprofiler_external_correlation_id_request_kind_t49ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_RCCL_APIE)

-
enumerator ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_OMPT
[#](#_CPPv4N50rocprofiler_external_correlation_id_request_kind_t45ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_OMPTE)

-
enumerator ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_MEMORY_ALLOCATION
[#](#_CPPv4N50rocprofiler_external_correlation_id_request_kind_t58ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_MEMORY_ALLOCATIONE)

-
enumerator ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_ROCDECODE_API
[#](#_CPPv4N50rocprofiler_external_correlation_id_request_kind_t54ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_ROCDECODE_APIE)

-
enumerator ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_ROCJPEG_API
[#](#_CPPv4N50rocprofiler_external_correlation_id_request_kind_t52ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_ROCJPEG_APIE)

-
enumerator ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_MARKER_CORE_RANGE_API
[#](#_CPPv4N50rocprofiler_external_correlation_id_request_kind_t62ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_MARKER_CORE_RANGE_APIE)

-
enumerator ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_LAST
[#](#_CPPv4N50rocprofiler_external_correlation_id_request_kind_t45ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_LASTE)

-
enumerator ROCPROFILER_EXTERNAL_CORRELATION_REQUEST_NONE

-
typedef int (*rocprofiler_external_correlation_id_request_cb_t)(
[rocprofiler_thread_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv423rocprofiler_thread_id_t)thread_id,[rocprofiler_context_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv424rocprofiler_context_id_t)context_id,[rocprofiler_external_correlation_id_request_kind_t](#_CPPv450rocprofiler_external_correlation_id_request_kind_t)kind,[rocprofiler_tracing_operation_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv431rocprofiler_tracing_operation_t)operation, uint64_t internal_corr_id_value,[rocprofiler_user_data_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv423rocprofiler_user_data_t)*external_corr_id_value, void *data)[#](#_CPPv448rocprofiler_external_correlation_id_request_cb_t) (experimental) Callback requesting a value for the external correlation id.

- Param thread_id:
**[in]**Id of the thread making the request- Param context_id:
**[in]**Id of the context making the request- Param kind:
**[in]**Origin of the external correlation id request- Param operation:
**[in]**Regardless of whether callback or buffer tracing is being used, the operation value will be the same, i.e., regardless of whether callback kind is[ROCPROFILER_CALLBACK_TRACING_HSA_CORE_API](../global_data_structures_topics_files/global_basic_data_types.html#group___b_a_s_i_c___d_a_t_a___t_y_p_e_s_1ggae2325388cbfe6e72f7b7eaa0738c52a9aaabbdd12a72827858e6874df4e4f5956)or the buffer record kind is[ROCPROFILER_BUFFER_TRACING_HSA_CORE_API](../global_data_structures_topics_files/global_basic_data_types.html#group___b_a_s_i_c___d_a_t_a___t_y_p_e_s_1ggac2eecbf4d5542df3b35fc26837fac59ba843a4a781ba70e1c3ea128762185c3a1), the data/record for`hsa_init`

will have an operation value of ROCPROFILER_HSA_CORE_API_ID_hsa_init.- Param internal_corr_id_value:
**[in]**Current internal correlation ID value for the request- Param external_corr_id_value:
**[out]**Set this value to the desired external correlation ID value- Param data:
**[in]**The`callback_args`

value passed to[rocprofiler_configure_external_correlation_id_request_service](#group___e_x_t_e_r_n_a_l___c_o_r_r_e_l_a_t_i_o_n_1ga6975efbb1c587878db616682ef7cda16).- Retval 0:
Used to indicate the tool had zero issues setting the external correlation ID field

- Retval 1:
(or any other non-zero number) Used to indicate the callback did not set an external correlation ID value and the thread-local value for the most recently pushed external correlation ID should be used instead

- Return:
int



-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_configure_external_correlation_id_request_service([rocprofiler_context_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv424rocprofiler_context_id_t)context_id, const[rocprofiler_external_correlation_id_request_kind_t](#_CPPv450rocprofiler_external_correlation_id_request_kind_t)*kinds, unsigned long kinds_count,[rocprofiler_external_correlation_id_request_cb_t](#_CPPv448rocprofiler_external_correlation_id_request_cb_t)callback, void *callback_args)[#](#_CPPv461rocprofiler_configure_external_correlation_id_request_service24rocprofiler_context_id_tPK50rocprofiler_external_correlation_id_request_kind_tm48rocprofiler_external_correlation_id_request_cb_tPv) (experimental) Configure External Correlation ID Request Service.

- Parameters:
**context_id**–**[in]**Context to associate the service with**kinds**–**[in]**Array of[rocprofiler_external_correlation_id_request_kind_t](#group___e_x_t_e_r_n_a_l___c_o_r_r_e_l_a_t_i_o_n_1gace0ad23024db8d8454948ccf1fec5416)values. If this parameter is null, all tracing operations will invoke the callback to request an external correlation ID.**kinds_count**–**[in]**If the kinds array is non-null, set this to the size of the array.**callback**–**[in]**The function to invoke for an external correlation ID request**callback_args**–**[in]**Data provided to every invocation of the callback function

- Return values:
**ROCPROFILER_STATUS_ERROR_CONFIGURATION_LOCKED**– Invoked outside of the initialization function in[rocprofiler_tool_configure_result_t](tool_registration.html#structrocprofiler__tool__configure__result__t)provided to rocprofiler via[rocprofiler_configure](tool_registration.html#group___r_e_g_i_s_t_r_a_t_i_o_n___g_r_o_u_p_1gaacc20d4f9bda3e14f11d3c4038178743)function**ROCPROFILER_STATUS_ERROR_CONTEXT_NOT_FOUND**– The provided context is not valid/registered**ROCPROFILER_STATUS_ERROR_SERVICE_ALREADY_CONFIGURED**– if the same[rocprofiler_callback_tracing_kind_t](../global_data_structures_topics_files/global_basic_data_types.html#group___b_a_s_i_c___d_a_t_a___t_y_p_e_s_1gae2325388cbfe6e72f7b7eaa0738c52a9)value is provided more than once (per context) — in other words, we do not support overriding or combining the kinds in separate function calls.

- Returns:


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_query_external_correlation_id_request_kind_name([rocprofiler_external_correlation_id_request_kind_t](#_CPPv450rocprofiler_external_correlation_id_request_kind_t)kind, const char **name, uint64_t *name_len)[#](#_CPPv459rocprofiler_query_external_correlation_id_request_kind_name50rocprofiler_external_correlation_id_request_kind_tPPKcP8uint64_t) Query the name of the external correlation request kind. The name retrieved from this function is a string literal that is encoded in the read-only section of the binary (i.e. it is always “allocated” and never “deallocated”).

- Parameters:
**kind**–**[in]**External correlation id request domain**name**–**[out]**If non-null and the name is a constant string that does not require dynamic allocation, this paramter will be set to the address of the string literal, otherwise it will be set to nullptr**name_len**–**[out]**If non-null, this will be assigned the length of the name (regardless of the name is a constant string or requires dynamic allocation)

- Return values:
**ROCPROFILER_STATUS_ERROR_KIND_NOT_FOUND**– Returned if the domain id is not valid**ROCPROFILER_STATUS_SUCCESS**– Returned if a valid domain, regardless if there is a constant string or not.

- Returns:


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_push_external_correlation_id([rocprofiler_context_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv424rocprofiler_context_id_t)context,[rocprofiler_thread_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv423rocprofiler_thread_id_t)tid,[rocprofiler_user_data_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv423rocprofiler_user_data_t)external_correlation_id)[#](#_CPPv440rocprofiler_push_external_correlation_id24rocprofiler_context_id_t23rocprofiler_thread_id_t23rocprofiler_user_data_t) Push default value for

`external`

field in[rocprofiler_correlation_id_t](../global_data_structures_topics_files/global_basic_data_types.html#structrocprofiler__correlation__id__t)onto stack.External correlation ids are thread-local values. However, if rocprofiler internally requests an external correlation id on a non-main thread and an external correlation id has not been pushed for this thread, the external correlation ID will default to the latest external correlation id on the main thread — this allows tools to push an external correlation id once on the main thread for, say, the MPI rank or process-wide UUID and this value will be used by all subsequent child threads.

See also

rocprofiler_get_thread_id

- Parameters:
**context**–**[in]**Associated context**tid**–**[in]**thread identifier.**external_correlation_id**–**[in]**User data to place in external field in[rocprofiler_correlation_id_t](../global_data_structures_topics_files/global_basic_data_types.html#structrocprofiler__correlation__id__t)

- Return values:
**ROCPROFILER_STATUS_ERROR_CONTEXT_NOT_FOUND**– Context does not exist**ROCPROFILER_STATUS_ERROR_INVALID_ARGUMENT**– Thread id is not valid

- Returns:


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_pop_external_correlation_id([rocprofiler_context_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv424rocprofiler_context_id_t)context,[rocprofiler_thread_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv423rocprofiler_thread_id_t)tid,[rocprofiler_user_data_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv423rocprofiler_user_data_t)*external_correlation_id)[#](#_CPPv439rocprofiler_pop_external_correlation_id24rocprofiler_context_id_t23rocprofiler_thread_id_tP23rocprofiler_user_data_t) Pop default value for

`external`

field in[rocprofiler_correlation_id_t](../global_data_structures_topics_files/global_basic_data_types.html#structrocprofiler__correlation__id__t)off of stack.See also

rocprofiler_get_thread_id

- Parameters:
**context**–**[in]**Associated context**tid**–**[in]**thread identifier.**external_correlation_id**–**[out]**Correlation id data popped off the stack

- Return values:
**ROCPROFILER_STATUS_ERROR_CONTEXT_NOT_FOUND**– Context does not exist**ROCPROFILER_STATUS_ERROR_INVALID_ARGUMENT**– Thread id is not valid

- Returns:
