---
title: "Thread trace &#8212; ROCprofiler-SDK 1.1.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/api-reference/rocprofiler-sdk_api/modules/thread_trace.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:15:32.172168+00:00
content_hash: "6fb80f724c214b13"
---

# Thread trace[#](#thread-trace)

-
enum rocprofiler_thread_trace_parameter_type_t
[#](#_CPPv441rocprofiler_thread_trace_parameter_type_t) Types of Thread Trace parameters.

*Values:*-
enumerator ROCPROFILER_THREAD_TRACE_PARAMETER_TARGET_CU
[#](#_CPPv4N41rocprofiler_thread_trace_parameter_type_t44ROCPROFILER_THREAD_TRACE_PARAMETER_TARGET_CUE) Select the Target CU or WGP.


-
enumerator ROCPROFILER_THREAD_TRACE_PARAMETER_SHADER_ENGINE_MASK
[#](#_CPPv4N41rocprofiler_thread_trace_parameter_type_t53ROCPROFILER_THREAD_TRACE_PARAMETER_SHADER_ENGINE_MASKE) Bitmask of shader engines.


-
enumerator ROCPROFILER_THREAD_TRACE_PARAMETER_BUFFER_SIZE
[#](#_CPPv4N41rocprofiler_thread_trace_parameter_type_t46ROCPROFILER_THREAD_TRACE_PARAMETER_BUFFER_SIZEE) Size of combined GPU buffer for ATT.


-
enumerator ROCPROFILER_THREAD_TRACE_PARAMETER_SIMD_SELECT
[#](#_CPPv4N41rocprofiler_thread_trace_parameter_type_t46ROCPROFILER_THREAD_TRACE_PARAMETER_SIMD_SELECTE) Bitmask (GFX9) or ID (Navi) of SIMDs.


-
enumerator ROCPROFILER_THREAD_TRACE_PARAMETER_PERFCOUNTERS_CTRL
[#](#_CPPv4N41rocprofiler_thread_trace_parameter_type_t52ROCPROFILER_THREAD_TRACE_PARAMETER_PERFCOUNTERS_CTRLE) Period [1,32] or disable (0) perfmon.


-
enumerator ROCPROFILER_THREAD_TRACE_PARAMETER_PERFCOUNTER
[#](#_CPPv4N41rocprofiler_thread_trace_parameter_type_t46ROCPROFILER_THREAD_TRACE_PARAMETER_PERFCOUNTERE) Perfmon ID and SIMD mask. gfx9 only.


-
enumerator ROCPROFILER_THREAD_TRACE_PARAMETER_SERIALIZE_ALL
[#](#_CPPv4N41rocprofiler_thread_trace_parameter_type_t48ROCPROFILER_THREAD_TRACE_PARAMETER_SERIALIZE_ALLE) Serializes also kernels not under thread trace.


-
enumerator ROCPROFILER_THREAD_TRACE_PARAMETER_PERFCOUNTER_EXCLUDE_MASK
[#](#_CPPv4N41rocprofiler_thread_trace_parameter_type_t59ROCPROFILER_THREAD_TRACE_PARAMETER_PERFCOUNTER_EXCLUDE_MASKE) Bitmask of which compute units to exclude from perfcounters. gfx9 only.


-
enumerator ROCPROFILER_THREAD_TRACE_PARAMETER_NO_DETAIL
[#](#_CPPv4N41rocprofiler_thread_trace_parameter_type_t44ROCPROFILER_THREAD_TRACE_PARAMETER_NO_DETAILE) Dont collect instruction timing, only shader-wide information.


-
enumerator ROCPROFILER_THREAD_TRACE_PARAMETER_LAST
[#](#_CPPv4N41rocprofiler_thread_trace_parameter_type_t39ROCPROFILER_THREAD_TRACE_PARAMETER_LASTE)

-
enumerator ROCPROFILER_THREAD_TRACE_PARAMETER_TARGET_CU

-
enum rocprofiler_thread_trace_control_flags_t
[#](#_CPPv440rocprofiler_thread_trace_control_flags_t) *Values:*-
enumerator ROCPROFILER_THREAD_TRACE_CONTROL_NONE
[#](#_CPPv4N40rocprofiler_thread_trace_control_flags_t37ROCPROFILER_THREAD_TRACE_CONTROL_NONEE)

-
enumerator ROCPROFILER_THREAD_TRACE_CONTROL_START_AND_STOP
[#](#_CPPv4N40rocprofiler_thread_trace_control_flags_t47ROCPROFILER_THREAD_TRACE_CONTROL_START_AND_STOPE)

-
enumerator ROCPROFILER_THREAD_TRACE_CONTROL_NONE

-
enum rocprofiler_thread_trace_decoder_info_t
[#](#_CPPv439rocprofiler_thread_trace_decoder_info_t) Describes the type of info received.

*Values:*-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_INFO_NONE
[#](#_CPPv4N39rocprofiler_thread_trace_decoder_info_t42ROCPROFILER_THREAD_TRACE_DECODER_INFO_NONEE)

-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_INFO_DATA_LOST
[#](#_CPPv4N39rocprofiler_thread_trace_decoder_info_t47ROCPROFILER_THREAD_TRACE_DECODER_INFO_DATA_LOSTE)

-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_INFO_STITCH_INCOMPLETE
[#](#_CPPv4N39rocprofiler_thread_trace_decoder_info_t55ROCPROFILER_THREAD_TRACE_DECODER_INFO_STITCH_INCOMPLETEE)

-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_INFO_WAVE_INCOMPLETE
[#](#_CPPv4N39rocprofiler_thread_trace_decoder_info_t53ROCPROFILER_THREAD_TRACE_DECODER_INFO_WAVE_INCOMPLETEE)

-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_INFO_LAST
[#](#_CPPv4N39rocprofiler_thread_trace_decoder_info_t42ROCPROFILER_THREAD_TRACE_DECODER_INFO_LASTE)

-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_INFO_NONE

-
enum rocprofiler_thread_trace_decoder_wstate_type_t
[#](#_CPPv446rocprofiler_thread_trace_decoder_wstate_type_t) Wave state type.

*Values:*-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_WSTATE_EMPTY
[#](#_CPPv4N46rocprofiler_thread_trace_decoder_wstate_type_t45ROCPROFILER_THREAD_TRACE_DECODER_WSTATE_EMPTYE)

-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_WSTATE_IDLE
[#](#_CPPv4N46rocprofiler_thread_trace_decoder_wstate_type_t44ROCPROFILER_THREAD_TRACE_DECODER_WSTATE_IDLEE)

-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_WSTATE_EXEC
[#](#_CPPv4N46rocprofiler_thread_trace_decoder_wstate_type_t44ROCPROFILER_THREAD_TRACE_DECODER_WSTATE_EXECE)

-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_WSTATE_WAIT
[#](#_CPPv4N46rocprofiler_thread_trace_decoder_wstate_type_t44ROCPROFILER_THREAD_TRACE_DECODER_WSTATE_WAITE)

-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_WSTATE_STALL
[#](#_CPPv4N46rocprofiler_thread_trace_decoder_wstate_type_t45ROCPROFILER_THREAD_TRACE_DECODER_WSTATE_STALLE)

-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_WSTATE_LAST
[#](#_CPPv4N46rocprofiler_thread_trace_decoder_wstate_type_t44ROCPROFILER_THREAD_TRACE_DECODER_WSTATE_LASTE)

-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_WSTATE_EMPTY

-
enum rocprofiler_thread_trace_decoder_inst_category_t
[#](#_CPPv448rocprofiler_thread_trace_decoder_inst_category_t) Instruction type.

*Values:*-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_INST_NONE
[#](#_CPPv4N48rocprofiler_thread_trace_decoder_inst_category_t42ROCPROFILER_THREAD_TRACE_DECODER_INST_NONEE)

-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_INST_SMEM
[#](#_CPPv4N48rocprofiler_thread_trace_decoder_inst_category_t42ROCPROFILER_THREAD_TRACE_DECODER_INST_SMEME) Scalar memory op.


-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_INST_SALU
[#](#_CPPv4N48rocprofiler_thread_trace_decoder_inst_category_t42ROCPROFILER_THREAD_TRACE_DECODER_INST_SALUE) Scalar ALU op.


-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_INST_VMEM
[#](#_CPPv4N48rocprofiler_thread_trace_decoder_inst_category_t42ROCPROFILER_THREAD_TRACE_DECODER_INST_VMEME) Vector memory op.


-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_INST_FLAT
[#](#_CPPv4N48rocprofiler_thread_trace_decoder_inst_category_t42ROCPROFILER_THREAD_TRACE_DECODER_INST_FLATE) Flat addressing vmem or lds.


-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_INST_LDS
[#](#_CPPv4N48rocprofiler_thread_trace_decoder_inst_category_t41ROCPROFILER_THREAD_TRACE_DECODER_INST_LDSE) Local Data Share op.


-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_INST_VALU
[#](#_CPPv4N48rocprofiler_thread_trace_decoder_inst_category_t42ROCPROFILER_THREAD_TRACE_DECODER_INST_VALUE) Vector ALU op.


-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_INST_JUMP
[#](#_CPPv4N48rocprofiler_thread_trace_decoder_inst_category_t42ROCPROFILER_THREAD_TRACE_DECODER_INST_JUMPE) Branch taken.


-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_INST_NEXT
[#](#_CPPv4N48rocprofiler_thread_trace_decoder_inst_category_t42ROCPROFILER_THREAD_TRACE_DECODER_INST_NEXTE) Branch not taken.


-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_INST_IMMED
[#](#_CPPv4N48rocprofiler_thread_trace_decoder_inst_category_t43ROCPROFILER_THREAD_TRACE_DECODER_INST_IMMEDE) Internal operation.


-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_INST_CONTEXT
[#](#_CPPv4N48rocprofiler_thread_trace_decoder_inst_category_t45ROCPROFILER_THREAD_TRACE_DECODER_INST_CONTEXTE) Wave context switch.


-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_INST_MESSAGE
[#](#_CPPv4N48rocprofiler_thread_trace_decoder_inst_category_t45ROCPROFILER_THREAD_TRACE_DECODER_INST_MESSAGEE) MSG types.


-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_INST_BVH
[#](#_CPPv4N48rocprofiler_thread_trace_decoder_inst_category_t41ROCPROFILER_THREAD_TRACE_DECODER_INST_BVHE) Raytrace op.


-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_INST_LAST
[#](#_CPPv4N48rocprofiler_thread_trace_decoder_inst_category_t42ROCPROFILER_THREAD_TRACE_DECODER_INST_LASTE)

-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_INST_NONE

-
enum rocprofiler_thread_trace_decoder_shaderdata_flags_t
[#](#_CPPv451rocprofiler_thread_trace_decoder_shaderdata_flags_t) Bitmask of additional information for shaderdata_t Added in rocprof-trace-decoder 0.1.3.

*Values:*-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_SHADERDATA_FLAGS_IMM
[#](#_CPPv4N51rocprofiler_thread_trace_decoder_shaderdata_flags_t53ROCPROFILER_THREAD_TRACE_DECODER_SHADERDATA_FLAGS_IMME)

-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_SHADERDATA_FLAGS_IMM

-
enum rocprofiler_thread_trace_decoder_record_type_t
[#](#_CPPv446rocprofiler_thread_trace_decoder_record_type_t) Defines the type of payload received by rocprofiler_thread_trace_decoder_callback_t.

*Values:*-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_RECORD_GFXIP
[#](#_CPPv4N46rocprofiler_thread_trace_decoder_record_type_t45ROCPROFILER_THREAD_TRACE_DECODER_RECORD_GFXIPE) Record is gfxip_major, type uint64_t.


-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_RECORD_OCCUPANCY
[#](#_CPPv4N46rocprofiler_thread_trace_decoder_record_type_t49ROCPROFILER_THREAD_TRACE_DECODER_RECORD_OCCUPANCYE) rocprofiler_thread_trace_decoder_occupancy_t*


-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_RECORD_PERFEVENT
[#](#_CPPv4N46rocprofiler_thread_trace_decoder_record_type_t49ROCPROFILER_THREAD_TRACE_DECODER_RECORD_PERFEVENTE) rocprofiler_thread_trace_decoder_perfevent_t*


-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_RECORD_WAVE
[#](#_CPPv4N46rocprofiler_thread_trace_decoder_record_type_t44ROCPROFILER_THREAD_TRACE_DECODER_RECORD_WAVEE) rocprofiler_thread_trace_decoder_wave_t*


-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_RECORD_INFO
[#](#_CPPv4N46rocprofiler_thread_trace_decoder_record_type_t44ROCPROFILER_THREAD_TRACE_DECODER_RECORD_INFOE) rocprofiler_thread_trace_decoder_info_t*


-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_RECORD_DEBUG
[#](#_CPPv4N46rocprofiler_thread_trace_decoder_record_type_t45ROCPROFILER_THREAD_TRACE_DECODER_RECORD_DEBUGE) Debug.


-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_RECORD_SHADERDATA
[#](#_CPPv4N46rocprofiler_thread_trace_decoder_record_type_t50ROCPROFILER_THREAD_TRACE_DECODER_RECORD_SHADERDATAE) rocprofiler_thread_trace_decoder_shaderdata_t*


-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_RECORD_REALTIME
[#](#_CPPv4N46rocprofiler_thread_trace_decoder_record_type_t48ROCPROFILER_THREAD_TRACE_DECODER_RECORD_REALTIMEE) rocprofiler_thread_trace_decoder_realtime_t*


-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_RECORD_RT_FREQUENCY
[#](#_CPPv4N46rocprofiler_thread_trace_decoder_record_type_t52ROCPROFILER_THREAD_TRACE_DECODER_RECORD_RT_FREQUENCYE)

-
enumerator ROCPROFILER_THREAD_TRACE_DECODER_RECORD_GFXIP

-
typedef void (*rocprofiler_thread_trace_shader_data_callback_t)(
[rocprofiler_agent_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv422rocprofiler_agent_id_t)agent, int64_t shader_engine_id, void *data, unsigned long data_size,[rocprofiler_user_data_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv423rocprofiler_user_data_t)userdata)[#](#_CPPv447rocprofiler_thread_trace_shader_data_callback_t) Callback to be triggered every time some ATT data is generated by the device.

- Param agent:
**[in]**Identifier for the target agent (- Param shader_engine_id:
**[in]**ID of shader engine, as enabled by SE_MASK- Param data:
**[in]**Pointer to the buffer containing the ATT data- Param data_size:
**[in]**Number of bytes in “data”- Param userdata:
**[in]**Passed back to user from[rocprofiler_thread_trace_dispatch_callback_t()](#group___t_h_r_e_a_d___t_r_a_c_e_1gaae15af8aec2ff90c99fb54d608ede84e)


-
typedef
[rocprofiler_thread_trace_control_flags_t](#_CPPv440rocprofiler_thread_trace_control_flags_t)(*rocprofiler_thread_trace_dispatch_callback_t)([rocprofiler_agent_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv422rocprofiler_agent_id_t)agent_id,[rocprofiler_queue_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv422rocprofiler_queue_id_t)queue_id,[rocprofiler_async_correlation_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv434rocprofiler_async_correlation_id_t)correlation_id,[rocprofiler_kernel_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv423rocprofiler_kernel_id_t)kernel_id,[rocprofiler_dispatch_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv425rocprofiler_dispatch_id_t)dispatch_id, void *userdata_config,[rocprofiler_user_data_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv423rocprofiler_user_data_t)*userdata_shader)[#](#_CPPv444rocprofiler_thread_trace_dispatch_callback_t) Callback to be triggered every kernel dispatch, indicating to start and/or stop ATT.

- Param agent_id:
**[in]**agent_id.- Param queue_id:
**[in]**queue_id.- Param correlation_id:
**[in]**internal correlation id.- Param kernel_id:
**[in]**kernel_id.- Param dispatch_id:
**[in]**dispatch_id.- Param userdata_config:
**[in]**Userdata passed back from rocprofiler_configure_dispatch_thread_trace_service.- Param userdata_shader:
**[out]**Userdata to be passed in shader_callback


-
typedef void (*rocprofiler_thread_trace_decoder_callback_t)(
[rocprofiler_thread_trace_decoder_record_type_t](#_CPPv446rocprofiler_thread_trace_decoder_record_type_t)record_type_id, void *trace_events, uint64_t trace_size, void *userdata)[#](#_CPPv443rocprofiler_thread_trace_decoder_callback_t) Callback for rocprof-trace-decoder to return decoder traces back to user.

- Param record_type_id:
**[in]**One of[rocprofiler_thread_trace_decoder_record_type_t](#group___t_h_r_e_a_d___t_r_a_c_e_1ga7bb3c3d21d8725c642456872e3d06adb)- Param trace_events:
**[in]**A pointer to sequence of events, of size trace_size.- Param trace_size:
**[in]**The number of events in the trace.- Param userdata:
**[in]**Arbitrary data pointer to be sent back to the user via callback.


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_configure_device_thread_trace_service([rocprofiler_context_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv424rocprofiler_context_id_t)context_id,[rocprofiler_agent_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv422rocprofiler_agent_id_t)agent_id,[rocprofiler_thread_trace_parameter_t](#_CPPv436rocprofiler_thread_trace_parameter_t)*parameters, unsigned long num_parameters,[rocprofiler_thread_trace_shader_data_callback_t](#_CPPv447rocprofiler_thread_trace_shader_data_callback_t)shader_callback,[rocprofiler_user_data_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv423rocprofiler_user_data_t)callback_userdata)[#](#_CPPv449rocprofiler_configure_device_thread_trace_service24rocprofiler_context_id_t22rocprofiler_agent_id_tP36rocprofiler_thread_trace_parameter_tm47rocprofiler_thread_trace_shader_data_callback_t23rocprofiler_user_data_t) Configure Thread Trace Service for agent. There may only be one agent profile configured per context and can be only one active context that is profiling a single agent at a time. Multiple agent contexts can be started at the same time if they are profiling different agents.

- Parameters:
**context_id**–**[in]**context id**parameters**–**[in]**List of ATT-specific parameters.**num_parameters**–**[in]**Number of parameters. Zero is allowed.**agent_id**–**[in]**agent to configure profiling on.**shader_callback**–**[in]**Callback fn where the collected data will be sent to.**callback_userdata**–**[in]**Passed back to user in shader_callback.

- Return values:
**ROCPROFILER_STATUS_SUCCESS**– on success**ROCPROFILER_STATUS_ERROR_CONFIGURATION_LOCKED**– for configuration locked**ROCPROFILER_STATUS_ERROR_CONTEXT_INVALID**– for conflicting configurations in the same ctx**ROCPROFILER_STATUS_ERROR_CONTEXT_NOT_FOUND**– for invalid context id**ROCPROFILER_STATUS_ERROR_INVALID_ARGUMENT**– for invalid[rocprofiler_thread_trace_parameter_t](#structrocprofiler__thread__trace__parameter__t)

- Returns:


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_configure_dispatch_thread_trace_service([rocprofiler_context_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv424rocprofiler_context_id_t)context_id,[rocprofiler_agent_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv422rocprofiler_agent_id_t)agent_id,[rocprofiler_thread_trace_parameter_t](#_CPPv436rocprofiler_thread_trace_parameter_t)*parameters, unsigned long num_parameters,[rocprofiler_thread_trace_dispatch_callback_t](#_CPPv444rocprofiler_thread_trace_dispatch_callback_t)dispatch_callback,[rocprofiler_thread_trace_shader_data_callback_t](#_CPPv447rocprofiler_thread_trace_shader_data_callback_t)shader_callback, void *callback_userdata)[#](#_CPPv451rocprofiler_configure_dispatch_thread_trace_service24rocprofiler_context_id_t22rocprofiler_agent_id_tP36rocprofiler_thread_trace_parameter_tm44rocprofiler_thread_trace_dispatch_callback_t47rocprofiler_thread_trace_shader_data_callback_tPv) Enables the thread trace service for dispatch-based tracing. The tool has an option to enable/disable thread trace on every dispatch callback. This service serializes all traced kernels, and optionally all non-traced kernels.

- Parameters:
**context_id**–**[in]**id of the context used for start/stop thread_trace.**agent_id**–**[in]**[rocprofiler_agent_id_t](../global_data_structures_topics_files/global_basic_data_types.html#structrocprofiler__agent__id__t)to configure thread trace.**parameters**–**[in]**List of ATT-specific parameters.**num_parameters**–**[in]**Number of parameters. Zero is allowed.**dispatch_callback**–**[in]**Control fn which decides when TT starts/stop collecting.**shader_callback**–**[in]**Callback fn where the collected data will be sent to.**callback_userdata**–**[in]**Passed back to user in dispatch_callback.

- Return values:
**ROCPROFILER_STATUS_SUCCESS**– on success**ROCPROFILER_STATUS_ERROR_CONFIGURATION_LOCKED**– for configuration locked**ROCPROFILER_STATUS_ERROR_CONTEXT_INVALID**– for conflicting configurations in the same ctx**ROCPROFILER_STATUS_ERROR_CONTEXT_NOT_FOUND**– for invalid context id**ROCPROFILER_STATUS_ERROR_INVALID_ARGUMENT**– for invalid[rocprofiler_thread_trace_parameter_t](#structrocprofiler__thread__trace__parameter__t)**ROCPROFILER_STATUS_ERROR_SERVICE_ALREADY_CONFIGURED**– if already configured

- Returns:


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_thread_trace_decoder_create([rocprofiler_thread_trace_decoder_id_t](#_CPPv437rocprofiler_thread_trace_decoder_id_t)*handle, const char *path)[#](#_CPPv439rocprofiler_thread_trace_decoder_createP37rocprofiler_thread_trace_decoder_id_tPKc) Initializes Trace Decoder library with a library search path.

- Parameters:
**handle**–**[out]**Handle to created decoder instance.**path**–**[in]**Path to trace decoder library location (e.g. /opt/rocm/lib).

- Return values:
**ROCPROFILER_STATUS_ERROR_NOT_AVAILABLE**– Library not found**ROCPROFILER_STATUS_ERROR_INCOMPATIBLE_ABI**– Library found but version not supported**ROCPROFILER_STATUS_SUCCESS**– Handle created

- Returns:


-
void rocprofiler_thread_trace_decoder_destroy(
[rocprofiler_thread_trace_decoder_id_t](#_CPPv437rocprofiler_thread_trace_decoder_id_t)handle)[#](#_CPPv440rocprofiler_thread_trace_decoder_destroy37rocprofiler_thread_trace_decoder_id_t) Deletes handle created by

[rocprofiler_thread_trace_decoder_create](#group___t_h_r_e_a_d___t_r_a_c_e_1ga7245fb595c03b7ae501f801a92704067).- Parameters:
**handle**–**[in]**Handle to destroy


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_thread_trace_decoder_codeobj_load([rocprofiler_thread_trace_decoder_id_t](#_CPPv437rocprofiler_thread_trace_decoder_id_t)handle, uint64_t load_id, uint64_t load_addr, uint64_t load_size, const void *data, uint64_t size)[#](#_CPPv445rocprofiler_thread_trace_decoder_codeobj_load37rocprofiler_thread_trace_decoder_id_t8uint64_t8uint64_t8uint64_tPKv8uint64_t) Loads a code object binary to match with Thread Trace. The size, data and load_* are reported by rocprofiler-sdk’s code object tracing service. Used for the decoder library to know what code objects to look into when decoding shader data. Not all application code objects are required to be reported here, only the ones containing code executed at the time the shader data was collected by thread_trace services. If a code object not reported here is encountered while decoding shader data, a record of type INFO_STITCH_INCOMPLETE will be generated and instructions will not be reported with a PC address.

- Parameters:
**handle**–**[in]**Handle to decoder instance.**load_id**–**[in]**Code object load ID.**load_addr**–**[in]**Code object load address.**load_size**–**[in]**Code object load size.**data**–**[in]**Code object binary data.**size**–**[in]**Code object binary data size.

- Return values:
**ROCPROFILER_STATUS_ERROR**– Unable to load code object.**ROCPROFILER_STATUS_ERROR_INVALID_ARGUMENT**– Invalid handle**ROCPROFILER_STATUS_SUCCESS**– Code object loaded

- Returns:


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_thread_trace_decoder_codeobj_unload([rocprofiler_thread_trace_decoder_id_t](#_CPPv437rocprofiler_thread_trace_decoder_id_t)handle, uint64_t load_id)[#](#_CPPv447rocprofiler_thread_trace_decoder_codeobj_unload37rocprofiler_thread_trace_decoder_id_t8uint64_t) Unloads a code object binary.

- Parameters:
**handle**–**[in]**Handle to decoder instance.**load_id**–**[in]**Code object load ID to remove.

- Return values:
**ROCPROFILER_STATUS_ERROR**– Code object not loaded.**ROCPROFILER_STATUS_ERROR_INVALID_ARGUMENT**– Invalid handle**ROCPROFILER_STATUS_SUCCESS**– Code object unloaded

- Returns:


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_trace_decode([rocprofiler_thread_trace_decoder_id_t](#_CPPv437rocprofiler_thread_trace_decoder_id_t)handle,[rocprofiler_thread_trace_decoder_callback_t](#_CPPv443rocprofiler_thread_trace_decoder_callback_t)callback, void *data, uint64_t size, void *userdata)[#](#_CPPv424rocprofiler_trace_decode37rocprofiler_thread_trace_decoder_id_t43rocprofiler_thread_trace_decoder_callback_tPv8uint64_tPv) Decodes shader data returned by

[rocprofiler_thread_trace_shader_data_callback_t](#group___t_h_r_e_a_d___t_r_a_c_e_1ga557add8e2308a321994b0d172ead99bb). Use[rocprofiler_thread_trace_decoder_codeobj_load](#group___t_h_r_e_a_d___t_r_a_c_e_1gaddc6920798a08a984946c8f719429314)to add references to loaded code objects during the trace. A[rocprofiler_thread_trace_decoder_callback_t](#group___t_h_r_e_a_d___t_r_a_c_e_1gade7b9d90a8de975b709b09c57b52446d)returns decoded data back to user. The first record is always of type[ROCPROFILER_THREAD_TRACE_DECODER_RECORD_GFXIP](#group___t_h_r_e_a_d___t_r_a_c_e_1gga7bb3c3d21d8725c642456872e3d06adba0ddabd23c25360da61ff53b27a43534c).- Parameters:
**handle**–**[in]**Decoder handle**callback**–**[in]**Decoded trace data returned to user.**data**–**[in]**Thread trace binary data.**size**–**[in]**Thread trace binary size.**userdata**–**[in]**Userdata passed back to caller via callback.

- Return values:
**ROCPROFILER_STATUS_ERROR_INVALID_ARGUMENT**– invalid argument**ROCPROFILER_STATUS_ERROR_AGENT_ARCH_NOT_SUPPORTED**– arch not supported**ROCPROFILER_STATUS_ERROR**– generic error**ROCPROFILER_STATUS_SUCCESS**– on success

- Returns:


-
const char *rocprofiler_thread_trace_decoder_info_string(
[rocprofiler_thread_trace_decoder_id_t](#_CPPv437rocprofiler_thread_trace_decoder_id_t)handle,[rocprofiler_thread_trace_decoder_info_t](#_CPPv439rocprofiler_thread_trace_decoder_info_t)info)[#](#_CPPv444rocprofiler_thread_trace_decoder_info_string37rocprofiler_thread_trace_decoder_id_t39rocprofiler_thread_trace_decoder_info_t) Returns the string description of a

[rocprofiler_thread_trace_decoder_info_t](#group___t_h_r_e_a_d___t_r_a_c_e_1ga90ebf09a5706b6411aafeeaa5dd06ee7)record.- Parameters:
**handle**–**[in]**Decoder handle**info**–**[in]**The decoder info received

- Return values:
**null**– terminated string as description of “info”.


-
struct rocprofiler_thread_trace_parameter_t
[#](#_CPPv436rocprofiler_thread_trace_parameter_t) *#include <rocprofiler-sdk/experimental/thread-trace/core.h>*Thread Trace parameter specification.


-
struct rocprofiler_thread_trace_decoder_id_t
[#](#_CPPv437rocprofiler_thread_trace_decoder_id_t) *#include <rocprofiler-sdk/experimental/thread-trace/trace_decoder.h>*Handle containing a loaded rocprof-trace-decoder and a decoder state.


-
struct rocprofiler_thread_trace_decoder_pc_t
[#](#_CPPv437rocprofiler_thread_trace_decoder_pc_t) *#include <rocprofiler-sdk/experimental/thread-trace/trace_decoder_types.h>*Describes a PC address.


-
struct rocprofiler_thread_trace_decoder_perfevent_t
[#](#_CPPv444rocprofiler_thread_trace_decoder_perfevent_t) *#include <rocprofiler-sdk/experimental/thread-trace/trace_decoder_types.h>*Describes four performance counter values.


-
struct rocprofiler_thread_trace_decoder_occupancy_t
[#](#_CPPv444rocprofiler_thread_trace_decoder_occupancy_t) *#include <rocprofiler-sdk/experimental/thread-trace/trace_decoder_types.h>*Describes an occupancy event (wave started or wave ended).


-
struct rocprofiler_thread_trace_decoder_wave_state_t
[#](#_CPPv445rocprofiler_thread_trace_decoder_wave_state_t) *#include <rocprofiler-sdk/experimental/thread-trace/trace_decoder_types.h>*A wave state change event.


-
struct rocprofiler_thread_trace_decoder_inst_t
[#](#_CPPv439rocprofiler_thread_trace_decoder_inst_t) *#include <rocprofiler-sdk/experimental/thread-trace/trace_decoder_types.h>*Describes an instruction execution event.

The duration is measured as stall+issue time (gfx9) or stall+execution time (gfx10+). Time + duration marks the issue (gfx9) or execution (gfx10+) completion time. Time + stall marks the successful issue time. Duration - stall is the issue time (gfx9) or execution time (gfx10+).


-
struct rocprofiler_thread_trace_decoder_wave_t
[#](#_CPPv439rocprofiler_thread_trace_decoder_wave_t) *#include <rocprofiler-sdk/experimental/thread-trace/trace_decoder_types.h>*Struct describing a wave during it’s lifetime. This record is only generated for waves executing in the target_cu and target_simd, selected by ROCPROFILER_THREAD_TRACE_PARAMETER_TARGET_CU and ROCPROFILER_THREAD_TRACE_PARAMETER_SIMD_SELECT.

instructions_array contains a time-ordered list of all (traced) instructions by the wave.


-
struct rocprofiler_thread_trace_decoder_realtime_t
[#](#_CPPv443rocprofiler_thread_trace_decoder_realtime_t) *#include <rocprofiler-sdk/experimental/thread-trace/trace_decoder_types.h>*Matches the reference (realtime) clock with the shader clock Added in rocprof-trace-decoder 0.1.3. Requires aqlprofile for rocm 7.1+. clock_in_seconds = realtime_clock / ROCPROFILER_THREAD_TRACE_DECODER_RECORD_RT_FREQUENCY gfx_frequency = delta(shader_clock) / delta(clock_in_seconds) For best average, use gfx_frequency[n] = (shader_clock[n]-shader_clock[0]) / (clock_in_seconds[n]-clock_in_seconds[0])


-
struct rocprofiler_thread_trace_decoder_shaderdata_t
[#](#_CPPv445rocprofiler_thread_trace_decoder_shaderdata_t) *#include <rocprofiler-sdk/experimental/thread-trace/trace_decoder_types.h>*Record created by s_ttracedata and s_ttracedata_imm Added in rocprof-trace-decoder 0.1.3.


- rocprofiler_thread_trace_parameter_t.__unnamed12__

- rocprofiler_thread_trace_parameter_t.__unnamed12__.__unnamed14__
