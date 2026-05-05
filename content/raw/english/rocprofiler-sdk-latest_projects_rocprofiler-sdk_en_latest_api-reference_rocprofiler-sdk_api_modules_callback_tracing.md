---
title: "Callback tracing &#8212; ROCprofiler-SDK 1.1.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/api-reference/rocprofiler-sdk_api/modules/callback_tracing.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-03T06:26:51.855934+00:00
content_hash: "ebcce146d9f9030b"
---

# Callback tracing[#](#callback-tracing)

-
enum rocprofiler_code_object_storage_type_t
[#](#_CPPv438rocprofiler_code_object_storage_type_t) ROCProfiler Enumeration for code object storage types (identical values to

`hsa_ven_amd_loader_code_object_storage_type_t`

enumeration)*Values:*-
enumerator ROCPROFILER_CODE_OBJECT_STORAGE_TYPE_NONE
[#](#_CPPv4N38rocprofiler_code_object_storage_type_t41ROCPROFILER_CODE_OBJECT_STORAGE_TYPE_NONEE)

-
enumerator ROCPROFILER_CODE_OBJECT_STORAGE_TYPE_FILE
[#](#_CPPv4N38rocprofiler_code_object_storage_type_t41ROCPROFILER_CODE_OBJECT_STORAGE_TYPE_FILEE)

-
enumerator ROCPROFILER_CODE_OBJECT_STORAGE_TYPE_MEMORY
[#](#_CPPv4N38rocprofiler_code_object_storage_type_t43ROCPROFILER_CODE_OBJECT_STORAGE_TYPE_MEMORYE)

-
enumerator ROCPROFILER_CODE_OBJECT_STORAGE_TYPE_LAST
[#](#_CPPv4N38rocprofiler_code_object_storage_type_t41ROCPROFILER_CODE_OBJECT_STORAGE_TYPE_LASTE)

-
enumerator ROCPROFILER_CODE_OBJECT_STORAGE_TYPE_NONE

-
typedef void (*rocprofiler_callback_tracing_cb_t)(
[rocprofiler_callback_tracing_record_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv437rocprofiler_callback_tracing_record_t)record,[rocprofiler_user_data_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv423rocprofiler_user_data_t)*user_data, void *callback_data)[#](#_CPPv433rocprofiler_callback_tracing_cb_t) API Tracing callback function. This function is invoked twice per API function: once before the function is invoked and once after the function is invoked. The external correlation id value within the record is assigned the value at the top of the external correlation id stack. It is permissible to invoke

[rocprofiler_push_external_correlation_id](external_correalation.html#group___e_x_t_e_r_n_a_l___c_o_r_r_e_l_a_t_i_o_n_1ga76c85d6440888d1e429d5dd6ae111a16)within the enter phase; when a new external correlation id is pushed during the enter phase, rocprofiler will use that external correlation id for any async events and provide the new external correlation id during the exit callback… In other words, pushing a new external correlation id within the enter callback will result in that external correlation id value in the exit callback (which may or may not be different from the external correlation id value in the enter callback). If a tool pushes new external correlation ids in the enter phase, it is recommended to pop the external correlation id in the exit callback.- Param record:
**[in]**Callback record data- Param user_data:
**[inout]**This paramter can be used to retain information in between the enter and exit phases.- Param callback_data:
**[in]**User data provided when configuring the callback tracing service


-
typedef int (*rocprofiler_callback_tracing_kind_cb_t)(
[rocprofiler_callback_tracing_kind_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv435rocprofiler_callback_tracing_kind_t)kind, void *data)[#](#_CPPv438rocprofiler_callback_tracing_kind_cb_t) Callback function for mapping

[rocprofiler_callback_tracing_kind_t](../global_data_structures_topics_files/global_basic_data_types.html#group___b_a_s_i_c___d_a_t_a___t_y_p_e_s_1gae2325388cbfe6e72f7b7eaa0738c52a9)ids to string names.See also

rocprofiler_iterate_callback_tracing_kind_names.


-
typedef int (*rocprofiler_callback_tracing_kind_operation_cb_t)(
[rocprofiler_callback_tracing_kind_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv435rocprofiler_callback_tracing_kind_t)kind,[rocprofiler_tracing_operation_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv431rocprofiler_tracing_operation_t)operation, void *data)[#](#_CPPv448rocprofiler_callback_tracing_kind_operation_cb_t) Callback function for mapping the operations of a given

[rocprofiler_callback_tracing_kind_t](../global_data_structures_topics_files/global_basic_data_types.html#group___b_a_s_i_c___d_a_t_a___t_y_p_e_s_1gae2325388cbfe6e72f7b7eaa0738c52a9)to string names.See also

rocprofiler_iterate_callback_tracing_kind_operation_names.


-
typedef int (*rocprofiler_callback_tracing_operation_args_cb_t)(
[rocprofiler_callback_tracing_kind_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv435rocprofiler_callback_tracing_kind_t)kind,[rocprofiler_tracing_operation_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv431rocprofiler_tracing_operation_t)operation, uint32_t arg_number, const void *const arg_value_addr, int32_t arg_indirection_count, const char *arg_type, const char *arg_name, const char *arg_value_str, int32_t arg_dereference_count, void *data)[#](#_CPPv448rocprofiler_callback_tracing_operation_args_cb_t) Callback function for iterating over the function arguments to a traced function. This function will be invoked for each argument.

See also

rocprofiler_iterate_callback_tracing_operation_args

- Param kind:
**[in]**domain- Param operation:
**[in]**associated domain operation- Param arg_number:
**[in]**the argument number, starting at zero- Param arg_value_addr:
**[in]**the address of the argument stored by rocprofiler.- Param arg_indirection_count:
**[in]**the total number of indirection levels for the argument, e.g. int == 0, int* == 1, int** == 2- Param arg_type:
**[in]**the typeid name of the argument- Param arg_name:
**[in]**the name of the argument in the prototype (or rocprofiler union)- Param arg_value_str:
**[in]**conversion of the argument to a string, e.g. operator<< overload- Param arg_dereference_count:
**[in]**the number of times the argument was dereferenced when it was converted to a string- Param data:
**[in]**user data


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_configure_callback_tracing_service([rocprofiler_context_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv424rocprofiler_context_id_t)context_id,[rocprofiler_callback_tracing_kind_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv435rocprofiler_callback_tracing_kind_t)kind, const[rocprofiler_tracing_operation_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv431rocprofiler_tracing_operation_t)*operations, unsigned long operations_count,[rocprofiler_callback_tracing_cb_t](#_CPPv433rocprofiler_callback_tracing_cb_t)callback, void *callback_args)[#](#_CPPv446rocprofiler_configure_callback_tracing_service24rocprofiler_context_id_t35rocprofiler_callback_tracing_kind_tPK31rocprofiler_tracing_operation_tm33rocprofiler_callback_tracing_cb_tPv) Configure Callback Tracing Service. The callback tracing service provides two synchronous callbacks around an API function on the same thread as the application which is invoking the API function. This function can only be invoked once per

[rocprofiler_callback_tracing_kind_t](../global_data_structures_topics_files/global_basic_data_types.html#group___b_a_s_i_c___d_a_t_a___t_y_p_e_s_1gae2325388cbfe6e72f7b7eaa0738c52a9)value, i.e. it can be invoked once for the HSA API, once for the HIP API, and so on but it will fail if it is invoked for the HSA API twice. Please note, the callback API does have the potentially non-trivial overhead of copying the function arguments into the record. If you are willing to let rocprofiler record the timestamps, do not require synchronous notifications of the API calls, and want to lowest possible overhead, use the.See also

Asynchronous Tracing Service.

- Parameters:
**context_id**–**[in]**Context to associate the service with**kind**–**[in]**The domain of the callback tracing service**operations**–**[in]**Array of operations in the domain (i.e. enum values which identify specific API functions). If this is null, all API functions in the domain will be traced**operations_count**–**[in]**If the operations array is non-null, set this to the size of the array.**callback**–**[in]**The function to invoke before and after an API function**callback_args**–**[in]**Data provided to every invocation of the callback function

- Return values:
**ROCPROFILER_STATUS_ERROR_CONFIGURATION_LOCKED**– Invoked outside of the initialization function in[rocprofiler_tool_configure_result_t](tool_registration.html#structrocprofiler__tool__configure__result__t)provided to rocprofiler via[rocprofiler_configure](tool_registration.html#group___r_e_g_i_s_t_r_a_t_i_o_n___g_r_o_u_p_1gaacc20d4f9bda3e14f11d3c4038178743)function**ROCPROFILER_STATUS_ERROR_CONTEXT_NOT_FOUND**– The provided context is not valid/registered**ROCPROFILER_STATUS_ERROR_SERVICE_ALREADY_CONFIGURED**– if the same[rocprofiler_callback_tracing_kind_t](../global_data_structures_topics_files/global_basic_data_types.html#group___b_a_s_i_c___d_a_t_a___t_y_p_e_s_1gae2325388cbfe6e72f7b7eaa0738c52a9)value is provided more than once (per context) — in other words, we do not support overriding or combining the operations in separate function calls.

- Returns:


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_query_callback_tracing_kind_name([rocprofiler_callback_tracing_kind_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv435rocprofiler_callback_tracing_kind_t)kind, const char **name, uint64_t *name_len)[#](#_CPPv444rocprofiler_query_callback_tracing_kind_name35rocprofiler_callback_tracing_kind_tPPKcP8uint64_t) Query the name of the callback tracing kind. The name retrieved from this function is a string literal that is encoded in the read-only section of the binary (i.e. it is always “allocated” and never “deallocated”).

- Parameters:
**kind**–**[in]**Callback tracing domain**name**–**[out]**If non-null and the name is a constant string that does not require dynamic allocation, this paramter will be set to the address of the string literal, otherwise it will be set to nullptr**name_len**–**[out]**If non-null, this will be assigned the length of the name (regardless of the name is a constant string or requires dynamic allocation)

- Returns:


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_query_callback_tracing_kind_operation_name([rocprofiler_callback_tracing_kind_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv435rocprofiler_callback_tracing_kind_t)kind,[rocprofiler_tracing_operation_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv431rocprofiler_tracing_operation_t)operation, const char **name, uint64_t *name_len)[#](#_CPPv454rocprofiler_query_callback_tracing_kind_operation_name35rocprofiler_callback_tracing_kind_t31rocprofiler_tracing_operation_tPPKcP8uint64_t) Query the name of the callback tracing kind. The name retrieved from this function is a string literal that is encoded in the read-only section of the binary (i.e. it is always “allocated” and never “deallocated”).

- Parameters:
**kind**–**[in]**Callback tracing domain**operation**–**[in]**Enumeration id value which maps to a specific API function or event type**name**–**[out]**If non-null and the name is a constant string that does not require dynamic allocation, this paramter will be set to the address of the string literal, otherwise it will be set to nullptr**name_len**–**[out]**If non-null, this will be assigned the length of the name (regardless of the name is a constant string or requires dynamic allocation)

- Return values:
**ROCPROFILER_STATUS_ERROR_KIND_NOT_FOUND**– Domain id is not valid**ROCPROFILER_STATUS_SUCCESS**– Valid domain provided, regardless if there is a constant string or not.

- Returns:


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_iterate_callback_tracing_kinds([rocprofiler_callback_tracing_kind_cb_t](#_CPPv438rocprofiler_callback_tracing_kind_cb_t)callback, void *data)[#](#_CPPv442rocprofiler_iterate_callback_tracing_kinds38rocprofiler_callback_tracing_kind_cb_tPv) Iterate over all the mappings of the callback tracing kinds and get a callback for each kind.

- Parameters:
**callback**–**[in]**Callback function invoked for each enumeration value in[rocprofiler_callback_tracing_kind_t](../global_data_structures_topics_files/global_basic_data_types.html#group___b_a_s_i_c___d_a_t_a___t_y_p_e_s_1gae2325388cbfe6e72f7b7eaa0738c52a9)with the exception of the`NONE`

and`LAST`

values.**data**–**[in]**User data passed back into the callback

- Returns:


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_iterate_callback_tracing_kind_operations([rocprofiler_callback_tracing_kind_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv435rocprofiler_callback_tracing_kind_t)kind,[rocprofiler_callback_tracing_kind_operation_cb_t](#_CPPv448rocprofiler_callback_tracing_kind_operation_cb_t)callback, void *data)[#](#_CPPv452rocprofiler_iterate_callback_tracing_kind_operations35rocprofiler_callback_tracing_kind_t48rocprofiler_callback_tracing_kind_operation_cb_tPv) Iterates over all the mappings of the operations for a given

[rocprofiler_callback_tracing_kind_t](../global_data_structures_topics_files/global_basic_data_types.html#group___b_a_s_i_c___d_a_t_a___t_y_p_e_s_1gae2325388cbfe6e72f7b7eaa0738c52a9)and invokes the callback with the kind id, operation id, and user-provided data.- Parameters:
**kind**–**[in]**which tracing callback kind operations to iterate over**callback**–**[in]**Callback function invoked for each operation associated with[rocprofiler_callback_tracing_kind_t](../global_data_structures_topics_files/global_basic_data_types.html#group___b_a_s_i_c___d_a_t_a___t_y_p_e_s_1gae2325388cbfe6e72f7b7eaa0738c52a9)with the exception of the`NONE`

and`LAST`

values.**data**–**[in]**User data passed back into the callback

- Return values:
**ROCPROFILER_STATUS_ERROR_KIND_NOT_FOUND**– Invalid domain id**ROCPROFILER_STATUS_SUCCESS**– Valid domain

- Returns:


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_iterate_callback_tracing_kind_operation_args([rocprofiler_callback_tracing_record_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv437rocprofiler_callback_tracing_record_t)record,[rocprofiler_callback_tracing_operation_args_cb_t](#_CPPv448rocprofiler_callback_tracing_operation_args_cb_t)callback, int32_t max_dereference_count, void *user_data)[#](#_CPPv456rocprofiler_iterate_callback_tracing_kind_operation_args37rocprofiler_callback_tracing_record_t48rocprofiler_callback_tracing_operation_args_cb_t7int32_tPv)

-
ROCPROFILER_CODE_OBJECT_ID_NONE
[#](#c.ROCPROFILER_CODE_OBJECT_ID_NONE) The NULL value of a code object id. Used when code object is unknown.


-
struct rocprofiler_callback_tracing_hsa_api_data_t
[#](#_CPPv443rocprofiler_callback_tracing_hsa_api_data_t) *#include <rocprofiler-sdk/callback_tracing.h>*ROCProfiler HSA API Callback Data.


-
struct rocprofiler_callback_tracing_hip_api_data_t
[#](#_CPPv443rocprofiler_callback_tracing_hip_api_data_t) *#include <rocprofiler-sdk/callback_tracing.h>*ROCProfiler HIP runtime and compiler API Tracer Callback Data.


-
struct rocprofiler_callback_tracing_ompt_data_t
[#](#_CPPv440rocprofiler_callback_tracing_ompt_data_t) *#include <rocprofiler-sdk/callback_tracing.h>*ROCProfiler OMPT Callback Data.


-
struct rocprofiler_callback_tracing_marker_api_data_t
[#](#_CPPv446rocprofiler_callback_tracing_marker_api_data_t) *#include <rocprofiler-sdk/callback_tracing.h>*ROCProfiler Marker Tracer Callback Data.


-
struct rocprofiler_callback_tracing_rccl_api_data_t
[#](#_CPPv444rocprofiler_callback_tracing_rccl_api_data_t) *#include <rocprofiler-sdk/callback_tracing.h>*ROCProfiler RCCL API Callback Data.


-
struct rocprofiler_callback_tracing_rocdecode_api_data_t
[#](#_CPPv449rocprofiler_callback_tracing_rocdecode_api_data_t) *#include <rocprofiler-sdk/callback_tracing.h>*ROCProfiler rocDecode API Callback Data.


-
struct rocprofiler_callback_tracing_rocjpeg_api_data_t
[#](#_CPPv447rocprofiler_callback_tracing_rocjpeg_api_data_t) *#include <rocprofiler-sdk/callback_tracing.h>*ROCProfiler rocJPEG API Callback Data.


-
struct rocprofiler_callback_tracing_code_object_load_data_t
[#](#_CPPv452rocprofiler_callback_tracing_code_object_load_data_t) *#include <rocprofiler-sdk/callback_tracing.h>*ROCProfiler Code Object Load Tracer Callback Record.


-
struct rocprofiler_callback_tracing_code_object_kernel_symbol_register_data_t
[#](#_CPPv470rocprofiler_callback_tracing_code_object_kernel_symbol_register_data_t) *#include <rocprofiler-sdk/callback_tracing.h>*ROCProfiler Code Object Kernel Symbol Tracer Callback Record.


-
struct rocprofiler_callback_tracing_code_object_host_kernel_symbol_register_data_t
[#](#_CPPv475rocprofiler_callback_tracing_code_object_host_kernel_symbol_register_data_t)

-
struct rocprofiler_callback_tracing_kernel_dispatch_data_t
[#](#_CPPv451rocprofiler_callback_tracing_kernel_dispatch_data_t) *#include <rocprofiler-sdk/callback_tracing.h>*ROCProfiler Kernel Dispatch Callback Tracer Record.


-
struct rocprofiler_callback_tracing_memory_copy_data_t
[#](#_CPPv447rocprofiler_callback_tracing_memory_copy_data_t) *#include <rocprofiler-sdk/callback_tracing.h>*ROCProfiler Memory Copy Callback Tracer Record.

The timestamps in this record will only be non-zero in the

[ROCPROFILER_CALLBACK_PHASE_EXIT](../global_data_structures_topics_files/global_basic_data_types.html#group___b_a_s_i_c___d_a_t_a___t_y_p_e_s_1ggaaa6a432135a8014cfdb1b1abdfa9e6eda685abcbca1810c5e3a60d76aa921fbba)callback

-
struct rocprofiler_callback_tracing_memory_allocation_data_t
[#](#_CPPv453rocprofiler_callback_tracing_memory_allocation_data_t) *#include <rocprofiler-sdk/callback_tracing.h>*ROCProfiler Memory Allocation Tracer Record.


-
struct rocprofiler_callback_tracing_scratch_memory_data_t
[#](#_CPPv450rocprofiler_callback_tracing_scratch_memory_data_t) *#include <rocprofiler-sdk/callback_tracing.h>*ROCProfiler Scratch Memory Callback Data.


-
struct rocprofiler_callback_tracing_runtime_initialization_data_t
[#](#_CPPv458rocprofiler_callback_tracing_runtime_initialization_data_t) *#include <rocprofiler-sdk/callback_tracing.h>*ROCProfiler Runtime Initialization Data.


-
struct rocprofiler_callback_tracing_hip_stream_data_t
[#](#_CPPv446rocprofiler_callback_tracing_hip_stream_data_t) *#include <rocprofiler-sdk/callback_tracing.h>*ROCProfiler Stream Handle Callback Data.


- rocprofiler_callback_tracing_code_object_load_data_t.__unnamed4__

- rocprofiler_callback_tracing_code_object_load_data_t.__unnamed6__
Public Members

- struct rocprofiler_callback_tracing_code_object_load_data_t

- struct rocprofiler_callback_tracing_code_object_load_data_t


- rocprofiler_callback_tracing_code_object_load_data_t.__unnamed6__.__unnamed8__

- rocprofiler_callback_tracing_code_object_load_data_t.__unnamed6__.__unnamed10__
