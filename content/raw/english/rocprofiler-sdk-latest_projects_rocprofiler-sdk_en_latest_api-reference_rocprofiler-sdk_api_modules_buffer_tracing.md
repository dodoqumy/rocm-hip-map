---
title: "Buffer tracing &#8212; ROCprofiler-SDK 1.1.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/api-reference/rocprofiler-sdk_api/modules/buffer_tracing.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:24:34.515160+00:00
content_hash: "364d3b4af05bc1be"
---

# Buffer tracing[#](#buffer-tracing)

-
typedef int (*rocprofiler_buffer_tracing_kind_cb_t)(
[rocprofiler_buffer_tracing_kind_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv433rocprofiler_buffer_tracing_kind_t)kind, void *data)[#](#_CPPv436rocprofiler_buffer_tracing_kind_cb_t) Callback function for mapping

[rocprofiler_buffer_tracing_kind_t](../global_data_structures_topics_files/global_basic_data_types.html#group___b_a_s_i_c___d_a_t_a___t_y_p_e_s_1gac2eecbf4d5542df3b35fc26837fac59b)ids to string names.See also

rocprofiler_iterate_buffer_trace_kind_names.


-
typedef int (*rocprofiler_buffer_tracing_kind_operation_cb_t)(
[rocprofiler_buffer_tracing_kind_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv433rocprofiler_buffer_tracing_kind_t)kind,[rocprofiler_tracing_operation_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv431rocprofiler_tracing_operation_t)operation, void *data)[#](#_CPPv446rocprofiler_buffer_tracing_kind_operation_cb_t) Callback function for mapping the operations of a given

[rocprofiler_buffer_tracing_kind_t](../global_data_structures_topics_files/global_basic_data_types.html#group___b_a_s_i_c___d_a_t_a___t_y_p_e_s_1gac2eecbf4d5542df3b35fc26837fac59b)to string names.See also

rocprofiler_iterate_buffer_trace_kind_operation_names.


-
typedef int (*rocprofiler_buffer_tracing_operation_args_cb_t)(
[rocprofiler_buffer_tracing_kind_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv433rocprofiler_buffer_tracing_kind_t)kind,[rocprofiler_tracing_operation_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv431rocprofiler_tracing_operation_t)operation, uint32_t arg_number, const void *const arg_value_addr, int32_t arg_indirection_count, const char *arg_type, const char *arg_name, const char *arg_value_str, void *data)[#](#_CPPv446rocprofiler_buffer_tracing_operation_args_cb_t) Callback function for iterating over the function arguments to a traced function. This function will be invoked for each argument.

See also

rocprofiler_iterate_buffer_tracing_record_args

- Param kind:
**[in]**domain- Param operation:
**[in]**associated domain operation- Param arg_number:
**[in]**the argument number, starting at zero- Param arg_value_addr:
**[in]**the address of the argument stored by rocprofiler.- Param arg_indirection_count:
**[in]**the total number of indirection levels for the argument, e.g. int == 0, int* == 1, int** == 2- Param arg_type:
**[in]**the typeid name of the argument (not demangled)- Param arg_name:
**[in]**the name of the argument in the prototype (or rocprofiler union)- Param arg_value_str:
**[in]**conversion of the argument to a string, e.g. operator<< overload- Param data:
**[in]**user data


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_configure_buffer_tracing_service([rocprofiler_context_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv424rocprofiler_context_id_t)context_id,[rocprofiler_buffer_tracing_kind_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv433rocprofiler_buffer_tracing_kind_t)kind, const[rocprofiler_tracing_operation_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv431rocprofiler_tracing_operation_t)*operations, unsigned long operations_count,[rocprofiler_buffer_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv423rocprofiler_buffer_id_t)buffer_id)[#](#_CPPv444rocprofiler_configure_buffer_tracing_service24rocprofiler_context_id_t33rocprofiler_buffer_tracing_kind_tPK31rocprofiler_tracing_operation_tm23rocprofiler_buffer_id_t) Configure Buffer Tracing Service.

- Parameters:
**context_id**–**[in]**Associated context to control activation of service**kind**–**[in]**Buffer tracing category**operations**–**[in]**Array of specific operations (if desired)**operations_count**–**[in]**Number of specific operations (if non-null set of operations)**buffer_id**–**[in]**Buffer to store the records in

- Return values:
**ROCPROFILER_STATUS_ERROR_CONFIGURATION_LOCKED**–[rocprofiler_configure](tool_registration.html#group___r_e_g_i_s_t_r_a_t_i_o_n___g_r_o_u_p_1gaacc20d4f9bda3e14f11d3c4038178743)initialization phase has passed**ROCPROFILER_STATUS_ERROR_CONTEXT_NOT_FOUND**– context is not valid**ROCPROFILER_STATUS_ERROR_SERVICE_ALREADY_CONFIGURED**– Context has already been configured for the[rocprofiler_buffer_tracing_kind_t](../global_data_structures_topics_files/global_basic_data_types.html#group___b_a_s_i_c___d_a_t_a___t_y_p_e_s_1gac2eecbf4d5542df3b35fc26837fac59b)kind**ROCPROFILER_STATUS_ERROR_KIND_NOT_FOUND**– Invalid[rocprofiler_buffer_tracing_kind_t](../global_data_structures_topics_files/global_basic_data_types.html#group___b_a_s_i_c___d_a_t_a___t_y_p_e_s_1gac2eecbf4d5542df3b35fc26837fac59b)**ROCPROFILER_STATUS_ERROR_OPERATION_NOT_FOUND**– Invalid operation id for[rocprofiler_buffer_tracing_kind_t](../global_data_structures_topics_files/global_basic_data_types.html#group___b_a_s_i_c___d_a_t_a___t_y_p_e_s_1gac2eecbf4d5542df3b35fc26837fac59b)kind was found

- Returns:


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_query_buffer_tracing_kind_name([rocprofiler_buffer_tracing_kind_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv433rocprofiler_buffer_tracing_kind_t)kind, const char **name, uint64_t *name_len)[#](#_CPPv442rocprofiler_query_buffer_tracing_kind_name33rocprofiler_buffer_tracing_kind_tPPKcP8uint64_t) Query the name of the buffer tracing kind. The name retrieved from this function is a string literal that is encoded in the read-only section of the binary (i.e. it is always “allocated” and never “deallocated”).

- Parameters:
**kind**–**[in]**Buffer tracing domain**name**–**[out]**If non-null and the name is a constant string that does not require dynamic allocation, this paramter will be set to the address of the string literal, otherwise it will be set to nullptr**name_len**–**[out]**If non-null, this will be assigned the length of the name (regardless of the name is a constant string or requires dynamic allocation)

- Return values:
**ROCPROFILER_STATUS_ERROR_KIND_NOT_FOUND**– Returned if the domain id is not valid**ROCPROFILER_STATUS_SUCCESS**– Returned if a valid domain, regardless if there is a constant string or not.

- Returns:


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_query_buffer_tracing_kind_operation_name([rocprofiler_buffer_tracing_kind_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv433rocprofiler_buffer_tracing_kind_t)kind,[rocprofiler_tracing_operation_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv431rocprofiler_tracing_operation_t)operation, const char **name, uint64_t *name_len)[#](#_CPPv452rocprofiler_query_buffer_tracing_kind_operation_name33rocprofiler_buffer_tracing_kind_t31rocprofiler_tracing_operation_tPPKcP8uint64_t) Query the name of the buffer tracing kind. The name retrieved from this function is a string literal that is encoded in the read-only section of the binary (i.e. it is always “allocated” and never “deallocated”).

- Parameters:
**kind**–**[in]**Buffer tracing domain**operation**–**[in]**Enumeration id value which maps to a specific API function or event type**name**–**[out]**If non-null and the name is a constant string that does not require dynamic allocation, this paramter will be set to the address of the string literal, otherwise it will be set to nullptr**name_len**–**[out]**If non-null, this will be assigned the length of the name (regardless of the name is a constant string or requires dynamic allocation)

- Return values:
**ROCPROFILER_STATUS_ERROR_KIND_NOT_FOUND**– An invalid domain id**ROCPROFILER_STATUS_ERROR_OPERATION_NOT_FOUND**– The operation number is not recognized for the given domain**ROCPROFILER_STATUS_ERROR_NOT_IMPLEMENTED**– Rocprofiler does not support providing the operation name within this domain**ROCPROFILER_STATUS_SUCCESS**– Valid domain and operation, regardless of whether there is a constant string or not.

- Returns:


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_iterate_buffer_tracing_kinds([rocprofiler_buffer_tracing_kind_cb_t](#_CPPv436rocprofiler_buffer_tracing_kind_cb_t)callback, void *data)[#](#_CPPv440rocprofiler_iterate_buffer_tracing_kinds36rocprofiler_buffer_tracing_kind_cb_tPv) Iterate over all the buffer tracing kinds and invokes the callback for each buffer tracing kind.

This is typically used to invoke

[rocprofiler_iterate_buffer_tracing_kind_operations](#group___b_u_f_f_e_r___t_r_a_c_i_n_g___s_e_r_v_i_c_e_1gafc84277a0837e4218167ad4122f12191)for each buffer tracing kind.- Parameters:
**callback**–**[in]**Callback function invoked for each enumeration value in[rocprofiler_buffer_tracing_kind_t](../global_data_structures_topics_files/global_basic_data_types.html#group___b_a_s_i_c___d_a_t_a___t_y_p_e_s_1gac2eecbf4d5542df3b35fc26837fac59b)with the exception of the`NONE`

and`LAST`

values.**data**–**[in]**User data passed back into the callback

- Returns:


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_iterate_buffer_tracing_kind_operations([rocprofiler_buffer_tracing_kind_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv433rocprofiler_buffer_tracing_kind_t)kind,[rocprofiler_buffer_tracing_kind_operation_cb_t](#_CPPv446rocprofiler_buffer_tracing_kind_operation_cb_t)callback, void *data)[#](#_CPPv450rocprofiler_iterate_buffer_tracing_kind_operations33rocprofiler_buffer_tracing_kind_t46rocprofiler_buffer_tracing_kind_operation_cb_tPv) Iterates over all the operations for a given

[rocprofiler_buffer_tracing_kind_t](../global_data_structures_topics_files/global_basic_data_types.html#group___b_a_s_i_c___d_a_t_a___t_y_p_e_s_1gac2eecbf4d5542df3b35fc26837fac59b)and invokes the callback with the kind and operation id. This is useful to build a map of the operation names during tool initialization instead of querying rocprofiler everytime in the callback hotpath.- Parameters:
**kind**–**[in]**which buffer tracing kind operations to iterate over**callback**–**[in]**Callback function invoked for each operation associated with[rocprofiler_buffer_tracing_kind_t](../global_data_structures_topics_files/global_basic_data_types.html#group___b_a_s_i_c___d_a_t_a___t_y_p_e_s_1gac2eecbf4d5542df3b35fc26837fac59b)with the exception of the`NONE`

and`LAST`

values.**data**–**[in]**User data passed back into the callback

- Returns:


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_iterate_buffer_tracing_record_args([rocprofiler_record_header_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv427rocprofiler_record_header_t)record,[rocprofiler_buffer_tracing_operation_args_cb_t](#_CPPv446rocprofiler_buffer_tracing_operation_args_cb_t)callback, void *user_data)[#](#_CPPv446rocprofiler_iterate_buffer_tracing_record_args27rocprofiler_record_header_t46rocprofiler_buffer_tracing_operation_args_cb_tPv)

-
struct rocprofiler_buffer_tracing_hsa_api_record_t
[#](#_CPPv443rocprofiler_buffer_tracing_hsa_api_record_t) *#include <rocprofiler-sdk/buffer_tracing.h>*ROCProfiler Buffer HSA API Tracer Record.


-
struct rocprofiler_buffer_tracing_hip_api_record_t
[#](#_CPPv443rocprofiler_buffer_tracing_hip_api_record_t) *#include <rocprofiler-sdk/buffer_tracing.h>*ROCProfiler Buffer HIP API Tracer Record.


-
struct rocprofiler_buffer_tracing_hip_api_ext_record_t
[#](#_CPPv447rocprofiler_buffer_tracing_hip_api_ext_record_t) *#include <rocprofiler-sdk/buffer_tracing.h>*ROCProfiler Buffer HIP API Tracer Record.


-
struct rocprofiler_buffer_tracing_ompt_target_t
[#](#_CPPv440rocprofiler_buffer_tracing_ompt_target_t) *#include <rocprofiler-sdk/buffer_tracing.h>*Additional trace data for OpenMP target routines.


-
struct rocprofiler_buffer_tracing_ompt_target_data_op_t
[#](#_CPPv448rocprofiler_buffer_tracing_ompt_target_data_op_t)

-
struct rocprofiler_buffer_tracing_ompt_target_kernel_t
[#](#_CPPv447rocprofiler_buffer_tracing_ompt_target_kernel_t)

-
struct rocprofiler_buffer_tracing_ompt_record_t
[#](#_CPPv440rocprofiler_buffer_tracing_ompt_record_t) *#include <rocprofiler-sdk/buffer_tracing.h>*ROCProfiler Buffer OMPT Tracer Record.


-
struct rocprofiler_buffer_tracing_marker_api_record_t
[#](#_CPPv446rocprofiler_buffer_tracing_marker_api_record_t) *#include <rocprofiler-sdk/buffer_tracing.h>*ROCProfiler Buffer Marker Tracer Record.


-
struct rocprofiler_buffer_tracing_rccl_api_record_t
[#](#_CPPv444rocprofiler_buffer_tracing_rccl_api_record_t) *#include <rocprofiler-sdk/buffer_tracing.h>*ROCProfiler Buffer RCCL API Record.


-
struct rocprofiler_buffer_tracing_rocdecode_api_record_t
[#](#_CPPv449rocprofiler_buffer_tracing_rocdecode_api_record_t) *#include <rocprofiler-sdk/buffer_tracing.h>*ROCProfiler Buffer rocDecode API Record.


-
struct rocprofiler_buffer_tracing_rocdecode_api_ext_record_t
[#](#_CPPv453rocprofiler_buffer_tracing_rocdecode_api_ext_record_t) *#include <rocprofiler-sdk/buffer_tracing.h>*An extended ROCProfiler rocDecode API Tracer Record which includes function arguments. Pointers are not dereferenced.


-
struct rocprofiler_buffer_tracing_rocjpeg_api_record_t
[#](#_CPPv447rocprofiler_buffer_tracing_rocjpeg_api_record_t) *#include <rocprofiler-sdk/buffer_tracing.h>*ROCProfiler Buffer rocJPEG API Record.


-
struct rocprofiler_buffer_tracing_memory_copy_record_t
[#](#_CPPv447rocprofiler_buffer_tracing_memory_copy_record_t) *#include <rocprofiler-sdk/buffer_tracing.h>*ROCProfiler Buffer Memory Copy Tracer Record.


-
struct rocprofiler_buffer_tracing_memory_allocation_record_t
[#](#_CPPv453rocprofiler_buffer_tracing_memory_allocation_record_t) *#include <rocprofiler-sdk/buffer_tracing.h>*ROCProfiler Buffer Memory Allocation Tracer Record.


-
struct rocprofiler_buffer_tracing_kernel_dispatch_record_t
[#](#_CPPv451rocprofiler_buffer_tracing_kernel_dispatch_record_t) *#include <rocprofiler-sdk/buffer_tracing.h>*ROCProfiler Buffer Kernel Dispatch Tracer Record.


-
struct rocprofiler_buffer_tracing_kfd_event_page_migrate_record_t
[#](#_CPPv458rocprofiler_buffer_tracing_kfd_event_page_migrate_record_t) *#include <rocprofiler-sdk/buffer_tracing.h>*ROCProfiler Buffer Page Migration event record from KFD.


-
struct rocprofiler_buffer_tracing_kfd_event_page_fault_record_t
[#](#_CPPv456rocprofiler_buffer_tracing_kfd_event_page_fault_record_t) *#include <rocprofiler-sdk/buffer_tracing.h>*ROCProfiler Buffer Page Fault event record from KFD.


-
struct rocprofiler_buffer_tracing_kfd_event_queue_record_t
[#](#_CPPv451rocprofiler_buffer_tracing_kfd_event_queue_record_t) *#include <rocprofiler-sdk/buffer_tracing.h>*ROCProfiler Buffer Queue event record from KFD.


-
struct rocprofiler_buffer_tracing_kfd_event_unmap_from_gpu_record_t
[#](#_CPPv460rocprofiler_buffer_tracing_kfd_event_unmap_from_gpu_record_t) *#include <rocprofiler-sdk/buffer_tracing.h>*ROCProfiler Buffer Unmap of memory from GPU event record from KFD.


-
struct rocprofiler_buffer_tracing_kfd_event_dropped_events_record_t
[#](#_CPPv460rocprofiler_buffer_tracing_kfd_event_dropped_events_record_t) *#include <rocprofiler-sdk/buffer_tracing.h>*ROCProfiler Buffer Dropped events event record, for when KFD reports that it has dropped some events.


-
struct rocprofiler_buffer_tracing_kfd_page_migrate_record_t
[#](#_CPPv452rocprofiler_buffer_tracing_kfd_page_migrate_record_t) *#include <rocprofiler-sdk/buffer_tracing.h>*ROCProfiler Buffer Page Migration (paired) record from KFD.


-
struct rocprofiler_buffer_tracing_kfd_page_fault_record_t
[#](#_CPPv450rocprofiler_buffer_tracing_kfd_page_fault_record_t) *#include <rocprofiler-sdk/buffer_tracing.h>*ROCProfiler Buffer Page Fault (paired) record from KFD.


-
struct rocprofiler_buffer_tracing_kfd_queue_record_t
[#](#_CPPv445rocprofiler_buffer_tracing_kfd_queue_record_t) *#include <rocprofiler-sdk/buffer_tracing.h>*ROCProfiler Buffer Queue suspend (paired) record from KFD.


-
struct rocprofiler_buffer_tracing_scratch_memory_record_t
[#](#_CPPv450rocprofiler_buffer_tracing_scratch_memory_record_t) *#include <rocprofiler-sdk/buffer_tracing.h>*ROCProfiler Buffer Scratch Memory Tracer Record.


-
struct rocprofiler_buffer_tracing_correlation_id_retirement_record_t
[#](#_CPPv461rocprofiler_buffer_tracing_correlation_id_retirement_record_t) *#include <rocprofiler-sdk/buffer_tracing.h>*ROCProfiler Buffer Correlation ID Retirement Tracer Record.


-
struct rocprofiler_buffer_tracing_runtime_initialization_record_t
[#](#_CPPv458rocprofiler_buffer_tracing_runtime_initialization_record_t) *#include <rocprofiler-sdk/buffer_tracing.h>*ROCProfiler Buffer Runtime Initialization Tracer Record.


- rocprofiler_buffer_tracing_ompt_record_t.__unnamed2__
