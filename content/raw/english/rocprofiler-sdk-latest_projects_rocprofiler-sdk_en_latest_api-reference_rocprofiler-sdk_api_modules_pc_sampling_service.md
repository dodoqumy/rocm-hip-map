---
title: "PC Sampling service &#8212; ROCprofiler-SDK 1.1.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/api-reference/rocprofiler-sdk_api/modules/pc_sampling_service.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:15:19.203186+00:00
content_hash: "1a8c5f92ba1e9ebf"
---

# PC Sampling service[#](#pc-sampling-service)

-
enum rocprofiler_pc_sampling_configuration_flags_t
[#](#_CPPv445rocprofiler_pc_sampling_configuration_flags_t) (experimental) Enumeration describing values of flags of

[rocprofiler_pc_sampling_configuration_t](#structrocprofiler__pc__sampling__configuration__t).*Values:*-
enumerator ROCPROFILER_PC_SAMPLING_CONFIGURATION_FLAGS_NONE
[#](#_CPPv4N45rocprofiler_pc_sampling_configuration_flags_t48ROCPROFILER_PC_SAMPLING_CONFIGURATION_FLAGS_NONEE)

-
enumerator ROCPROFILER_PC_SAMPLING_CONFIGURATION_FLAGS_INTERVAL_POW2
[#](#_CPPv4N45rocprofiler_pc_sampling_configuration_flags_t57ROCPROFILER_PC_SAMPLING_CONFIGURATION_FLAGS_INTERVAL_POW2E)

-
enumerator ROCPROFILER_PC_SAMPLING_CONFIGURATION_FLAGS_NONE

-
enum rocprofiler_pc_sampling_instruction_type_t
[#](#_CPPv442rocprofiler_pc_sampling_instruction_type_t) (experimental) Enumeration describing type of sampled issued instruction.

*Values:*-
enumerator ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NONE
[#](#_CPPv4N42rocprofiler_pc_sampling_instruction_type_t45ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NONEE)

-
enumerator ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_VALU
[#](#_CPPv4N42rocprofiler_pc_sampling_instruction_type_t45ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_VALUE) vector ALU instruction


-
enumerator ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_MATRIX
[#](#_CPPv4N42rocprofiler_pc_sampling_instruction_type_t47ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_MATRIXE) matrix instruction


-
enumerator ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_SCALAR
[#](#_CPPv4N42rocprofiler_pc_sampling_instruction_type_t47ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_SCALARE) scalar (memory) instruction


-
enumerator ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_TEX
[#](#_CPPv4N42rocprofiler_pc_sampling_instruction_type_t44ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_TEXE) texture memory instruction


-
enumerator ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_LDS
[#](#_CPPv4N42rocprofiler_pc_sampling_instruction_type_t44ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_LDSE) LDS memory instruction.


-
enumerator ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_LDS_DIRECT
[#](#_CPPv4N42rocprofiler_pc_sampling_instruction_type_t51ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_LDS_DIRECTE) LDS direct memory instruction.


-
enumerator ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_FLAT
[#](#_CPPv4N42rocprofiler_pc_sampling_instruction_type_t45ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_FLATE) flat memory instruction


-
enumerator ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_EXPORT
[#](#_CPPv4N42rocprofiler_pc_sampling_instruction_type_t47ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_EXPORTE) export instruction


-
enumerator ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_MESSAGE
[#](#_CPPv4N42rocprofiler_pc_sampling_instruction_type_t48ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_MESSAGEE) message instruction


-
enumerator ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_BARRIER
[#](#_CPPv4N42rocprofiler_pc_sampling_instruction_type_t48ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_BARRIERE) barrier instruction


-
enumerator ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_BRANCH_NOT_TAKEN
[#](#_CPPv4N42rocprofiler_pc_sampling_instruction_type_t57ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_BRANCH_NOT_TAKENE)

-
enumerator ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_BRANCH_TAKEN
[#](#_CPPv4N42rocprofiler_pc_sampling_instruction_type_t53ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_BRANCH_TAKENE)

-
enumerator ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_JUMP
[#](#_CPPv4N42rocprofiler_pc_sampling_instruction_type_t45ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_JUMPE) jump instruction


-
enumerator ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_OTHER
[#](#_CPPv4N42rocprofiler_pc_sampling_instruction_type_t46ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_OTHERE) other types of instruction


-
enumerator ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST
[#](#_CPPv4N42rocprofiler_pc_sampling_instruction_type_t48ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INSTE) no instruction issued


-
enumerator ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_DUAL_VALU
[#](#_CPPv4N42rocprofiler_pc_sampling_instruction_type_t50ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_DUAL_VALUE)

-
enumerator ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_BRANCH_TAKEN

-
enumerator ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NONE

-
enum rocprofiler_pc_sampling_instruction_not_issued_reason_t
[#](#_CPPv455rocprofiler_pc_sampling_instruction_not_issued_reason_t) (experimental) Enumeration describing reason for not issuing an instruction.

*Values:*-
enumerator ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_NONE
[#](#_CPPv4N55rocprofiler_pc_sampling_instruction_not_issued_reason_t58ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_NONEE)

-
enumerator ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_NO_INSTRUCTION_AVAILABLE
[#](#_CPPv4N55rocprofiler_pc_sampling_instruction_not_issued_reason_t78ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_NO_INSTRUCTION_AVAILABLEE)

-
enumerator ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_ALU_DEPENDENCY
[#](#_CPPv4N55rocprofiler_pc_sampling_instruction_not_issued_reason_t68ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_ALU_DEPENDENCYE)

-
enumerator ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT
[#](#_CPPv4N55rocprofiler_pc_sampling_instruction_not_issued_reason_t61ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNTE) waitcnt dependency


-
enumerator ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_INTERNAL_INSTRUCTION
[#](#_CPPv4N55rocprofiler_pc_sampling_instruction_not_issued_reason_t74ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_INTERNAL_INSTRUCTIONE)

-
enumerator ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_BARRIER_WAIT
[#](#_CPPv4N55rocprofiler_pc_sampling_instruction_not_issued_reason_t66ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_BARRIER_WAITE) waiting on a barrier


-
enumerator ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_ARBITER_NOT_WIN
[#](#_CPPv4N55rocprofiler_pc_sampling_instruction_not_issued_reason_t69ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_ARBITER_NOT_WINE)

-
enumerator ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_ARBITER_WIN_EX_STALL
[#](#_CPPv4N55rocprofiler_pc_sampling_instruction_not_issued_reason_t74ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_ARBITER_WIN_EX_STALLE)

-
enumerator ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_OTHER_WAIT
[#](#_CPPv4N55rocprofiler_pc_sampling_instruction_not_issued_reason_t64ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_OTHER_WAITE)

-
enumerator ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_SLEEP_WAIT
[#](#_CPPv4N55rocprofiler_pc_sampling_instruction_not_issued_reason_t64ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_SLEEP_WAITE) wave was sleeping


-
enumerator ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_ALU_DEPENDENCY

-
enumerator ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_INTERNAL_INSTRUCTION

-
enumerator ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_ARBITER_NOT_WIN

-
enumerator ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_ARBITER_WIN_EX_STALL

-
enumerator ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_OTHER_WAIT

-
enumerator ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_NONE

-
typedef
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)(*rocprofiler_available_pc_sampling_configurations_cb_t)(const[rocprofiler_pc_sampling_configuration_t](#_CPPv439rocprofiler_pc_sampling_configuration_t)*configs, unsigned long num_config, void *user_data)[#](#_CPPv453rocprofiler_available_pc_sampling_configurations_cb_t) (experimental) Rocprofiler SDK’s callback function to deliver the list of available PC sampling configurations upon the call to the

[rocprofiler_query_pc_sampling_agent_configurations](#group___p_c___s_a_m_p_l_i_n_g___s_e_r_v_i_c_e_1ga89e0a3d3c4d69a49c16aad4dc95a7c99).- Param configs:
**[out]**- The array of PC sampling configurations supported by the agent at the moment of invoking[rocprofiler_query_pc_sampling_agent_configurations](#group___p_c___s_a_m_p_l_i_n_g___s_e_r_v_i_c_e_1ga89e0a3d3c4d69a49c16aad4dc95a7c99).- Param num_config:
**[out]**- The number of configurations contained in the underlying array`configs`

. In case the GPU agent does not support PC sampling, the value is 0.- Param user_data:
**[in]**- client’s private data passed via[rocprofiler_query_pc_sampling_agent_configurations](#group___p_c___s_a_m_p_l_i_n_g___s_e_r_v_i_c_e_1ga89e0a3d3c4d69a49c16aad4dc95a7c99)- Return:


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_configure_pc_sampling_service([rocprofiler_context_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv424rocprofiler_context_id_t)context_id,[rocprofiler_agent_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv422rocprofiler_agent_id_t)agent_id,[rocprofiler_pc_sampling_method_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv432rocprofiler_pc_sampling_method_t)method,[rocprofiler_pc_sampling_unit_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv430rocprofiler_pc_sampling_unit_t)unit, uint64_t interval,[rocprofiler_buffer_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv423rocprofiler_buffer_id_t)buffer_id, int flags)[#](#_CPPv441rocprofiler_configure_pc_sampling_service24rocprofiler_context_id_t22rocprofiler_agent_id_t32rocprofiler_pc_sampling_method_t30rocprofiler_pc_sampling_unit_t8uint64_t23rocprofiler_buffer_id_ti) (experimental) Function used to configure the PC sampling service on the GPU agent with

`agent_id`

.Prerequisites are the following:

The client must create a context and supply its

`context_id`

. By using this context, the client can start/stop PC sampling on the agent. For more information, pleaseSee also

rocprofiler_start_context/rocprofiler_stop_context.

The user must create a buffer and supply its

`buffer_id`

. Rocprofiler-SDK uses the buffer to deliver the PC samples to the client. For more information about the data delivery, please

Before calling this function, we recommend querying PC sampling configurations supported by the GPU agent via the

Rocprofiler-SDK checks whether the requsted configuration is actually supported at the moment of calling this function. If the answer is yes, it returns the

There are a few constraints a client’s code needs to be aware of.

See also

[rocprofiler_query_pc_sampling_agent_configurations](#group___p_c___s_a_m_p_l_i_n_g___s_e_r_v_i_c_e_1ga89e0a3d3c4d69a49c16aad4dc95a7c99). The client chooses the`method`

,`unit`

, and`interval`

to match one of the available configurations. Note that the`interval`

must belong to the range of values [available_config.min_interval, available_config.max_interval], where available_config is the instance of theSee also

rocprofiler_pc_sampling_configuration_s supported/available at the moment.


Constraint1: A GPU agent can be configured to support at most one running PC sampling configuration at any time, which implies some of the consequences described below. After the tool configures the PC sampling with one of the available configurations, rocprofiler-SDK guarantees that this configuration will be valid for the tool’s lifetime. The tool can start and stop the configured PC sampling service whenever convenient.

Constraint2: Since the same GPU agent can be used by multiple processes concurrently, Rocprofiler-SDK cannot guarantee the exclusive access to the PC sampling capability. The consequence is the following scenario. The tool TA that belongs to the process PA, calls the

Constraint3: Rocprofiler-SDK allows only one context to contain the configured PC sampling service within the process, that implies that at most one of the loaded tools can use PC sampling. One context can contains multiple PC sampling services configured for different GPU agents.

See also

[rocprofiler_query_pc_sampling_agent_configurations](#group___p_c___s_a_m_p_l_i_n_g___s_e_r_v_i_c_e_1ga89e0a3d3c4d69a49c16aad4dc95a7c99)that returns the two supported configurations CA and CB by the agent. Then the tool TB of the process PB, configures the PC sampling on the same agent by using the configuration CB. Subsequently, the TA tries configuring the CA on the agent, and it fails. To point out that this case happened, we introduce a special status codeSee also

[ROCPROFILER_STATUS_ERROR_NOT_AVAILABLE](../global_data_structures_topics_files/global_basic_data_types.html#group___b_a_s_i_c___d_a_t_a___t_y_p_e_s_1gga952efee747482031f1478b1fcc4eeddca789fbd4fe42b6b0466cc987e1e4a6222). When this status code is observed by the tool TA, it queries all available configurations again by callingSee also

[rocprofiler_query_pc_sampling_agent_configurations](#group___p_c___s_a_m_p_l_i_n_g___s_e_r_v_i_c_e_1ga89e0a3d3c4d69a49c16aad4dc95a7c99), that returns only CB this time. The tool TA can choose CB, so that both TA and TB use the PC sampling capability in the separate processes. Both TA and TB receives samples generated by the kernels launched by the corresponding processes PA and PB, respectively.Constraint4: PC sampling feature is not available within the ROCgdb.

Constraint5: PC sampling service cannot be used simultaneously with counter collection service.

- Parameters:
**context_id**–**[in]**- id of the context used for starting/stopping PC sampling service**agent_id**–**[in]**- id of the agent on which caller tries using PC sampling capability**method**–**[in]**- the type of PC sampling the caller tries to use on the agent.**unit**–**[in]**- The unit appropriate to the PC sampling type/method.**interval**–**[in]**- frequency at which PC samples are generated**buffer_id**–**[in]**- id of the buffer used for delivering PC samples**flags**–**[in]**- for future use

- Return values:
**ROCPROFILER_STATUS_SUCCESS**– PC sampling service configured successfully**ROCPROFILER_STATUS_ERROR_NOT_AVAILABLE**– One of the scenarios is present:PC sampling is already configured with configuration different than requested,

PC sampling is requested from a process that runs within the ROCgdb.

HSA runtime does not support PC sampling.

GPU device does not support requested PC sampling method.


**ROCPROFILER_STATUS_ERROR_INCOMPATIBLE_KERNEL**– the amdgpu driver installed on the system does not support the PC sampling feature**ROCPROFILER_STATUS_ERROR**– a general error caused by the amdgpu driver**ROCPROFILER_STATUS_ERROR_CONTEXT_CONFLICT**– counter collection service already setup in the context**ROCPROFILER_STATUS_ERROR_INVALID_ARGUMENT**– function invoked with an invalid argument

- Returns:


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_query_pc_sampling_agent_configurations([rocprofiler_agent_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv422rocprofiler_agent_id_t)agent_id,[rocprofiler_available_pc_sampling_configurations_cb_t](#_CPPv453rocprofiler_available_pc_sampling_configurations_cb_t)cb, void *user_data)[#](#_CPPv450rocprofiler_query_pc_sampling_agent_configurations22rocprofiler_agent_id_t53rocprofiler_available_pc_sampling_configurations_cb_tPv) (experimental) Query PC Sampling Configuration.

Lists PC sampling configurations a GPU agent with

`agent_id`

supports at the moment of invoking the function. Delivers configurations via`cb`

. In case the PC sampling is configured on the GPU agent, the`cb`

delivers information about the active PC sampling configuration. In case the GPU agent does not support PC sampling capability, the`cb`

delivers none PC sampling configurations.- Parameters:
**agent_id**–**[in]**- id of the agent for which available configurations will be listed**cb**–**[in]**- User callback that delivers the available PC sampling configurations**user_data**–**[in]**- passed to the`cb`


- Return values:
**ROCPROFILER_STATUS_ERROR_NOT_AVAILABLE**– One of the scenarios is present:PC sampling is requested from a process that runs within the ROCgdb.

HSA runtime does not support PC sampling.


**ROCPROFILER_STATUS_ERROR_INCOMPATIBLE_KERNEL**– the amdgpu driver installed on the system does not support the PC sampling feature.**ROCPROFILER_STATUS_ERROR**– a general error caused by the amdgpu driver**ROCPROFILER_STATUS_SUCCESS**–`cb`

successfully finished

- Returns:


-
const char *rocprofiler_get_pc_sampling_instruction_type_name(
[rocprofiler_pc_sampling_instruction_type_t](#_CPPv442rocprofiler_pc_sampling_instruction_type_t)instruction_type)[#](#_CPPv449rocprofiler_get_pc_sampling_instruction_type_name42rocprofiler_pc_sampling_instruction_type_t) (experimental) Return the string encoding of

[rocprofiler_pc_sampling_instruction_type_t](#group___p_c___s_a_m_p_l_i_n_g___s_e_r_v_i_c_e_1gab85fcce5f2d02d6ed992c9aa4331659d)value- Parameters:
**instruction_type**–**[in]**instruction type enum value- Returns:
Will return a nullptr if invalid/unsupported

[rocprofiler_pc_sampling_instruction_type_t](#group___p_c___s_a_m_p_l_i_n_g___s_e_r_v_i_c_e_1gab85fcce5f2d02d6ed992c9aa4331659d)value is provided.


-
const char *rocprofiler_get_pc_sampling_instruction_not_issued_reason_name(
[rocprofiler_pc_sampling_instruction_not_issued_reason_t](#_CPPv455rocprofiler_pc_sampling_instruction_not_issued_reason_t)not_issued_reason)[#](#_CPPv462rocprofiler_get_pc_sampling_instruction_not_issued_reason_name55rocprofiler_pc_sampling_instruction_not_issued_reason_t) (experimental) Return the string encoding of

[rocprofiler_pc_sampling_instruction_not_issued_reason_t](#group___p_c___s_a_m_p_l_i_n_g___s_e_r_v_i_c_e_1ga5007dbd38bfd7f5fc6c97312bd85d6e9)value- Parameters:
**not_issued_reason**–**[in]**no issue reason enum value- Returns:
Will return a nullptr if invalid/unsupported

[rocprofiler_pc_sampling_instruction_not_issued_reason_t](#group___p_c___s_a_m_p_l_i_n_g___s_e_r_v_i_c_e_1ga5007dbd38bfd7f5fc6c97312bd85d6e9)value is provided.


-
struct rocprofiler_pc_sampling_configuration_t
[#](#_CPPv439rocprofiler_pc_sampling_configuration_t) *#include <rocprofiler-sdk/pc_sampling.h>*(experimental) PC sampling configuration supported by a GPU agent.


-
struct rocprofiler_pc_sampling_hw_id_v0_t
[#](#_CPPv434rocprofiler_pc_sampling_hw_id_v0_t) *#include <rocprofiler-sdk/pc_sampling.h>*(experimental) Information about the GPU part where wave was executing at the moment of sampling.


-
struct rocprofiler_pc_t
[#](#_CPPv416rocprofiler_pc_t) *#include <rocprofiler-sdk/pc_sampling.h>*(experimental) Sampled program counter.


-
struct rocprofiler_pc_sampling_record_host_trap_v0_t
[#](#_CPPv445rocprofiler_pc_sampling_record_host_trap_v0_t) *#include <rocprofiler-sdk/pc_sampling.h>*(experimental) ROCProfiler Host-Trap PC Sampling Record.


-
struct rocprofiler_pc_sampling_record_stochastic_header_t
[#](#_CPPv450rocprofiler_pc_sampling_record_stochastic_header_t) *#include <rocprofiler-sdk/pc_sampling.h>*(experimental) The header of the

[rocprofiler_pc_sampling_record_stochastic_v0_t](#structrocprofiler__pc__sampling__record__stochastic__v0__t), indicating what fields of the[rocprofiler_pc_sampling_record_stochastic_v0_t](#structrocprofiler__pc__sampling__record__stochastic__v0__t)instance are meaningful for the sample.

-
struct rocprofiler_pc_sampling_snapshot_v0_t
[#](#_CPPv437rocprofiler_pc_sampling_snapshot_v0_t) *#include <rocprofiler-sdk/pc_sampling.h>*(experimental) Data provided by stochastic sampling hardware.


-
struct rocprofiler_pc_sampling_memory_counters_t
[#](#_CPPv441rocprofiler_pc_sampling_memory_counters_t) *#include <rocprofiler-sdk/pc_sampling.h>*(experimental) Counters of issued but not yet completed instructions.


-
struct rocprofiler_pc_sampling_record_stochastic_v0_t
[#](#_CPPv446rocprofiler_pc_sampling_record_stochastic_v0_t) *#include <rocprofiler-sdk/pc_sampling.h>*(experimental) ROCProfiler Stochastic PC Sampling Record.


-
struct rocprofiler_pc_sampling_record_invalid_t
[#](#_CPPv440rocprofiler_pc_sampling_record_invalid_t) *#include <rocprofiler-sdk/pc_sampling.h>*(experimental) Record representing an invalid PC Sampling Record.
