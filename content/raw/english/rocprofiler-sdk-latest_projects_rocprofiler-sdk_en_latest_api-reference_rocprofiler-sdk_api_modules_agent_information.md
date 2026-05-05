---
title: "Agent Information &#8212; ROCprofiler-SDK 1.1.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/api-reference/rocprofiler-sdk_api/modules/agent_information.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:15:24.923229+00:00
content_hash: "a2992702f8713e95"
---

# Agent Information[#](#agent-information)

-
enum rocprofiler_agent_version_t
[#](#_CPPv427rocprofiler_agent_version_t) Enumeration ID for version of the rocprofiler_agent_v*_t struct in rocprofiler_i.

*Values:*-
enumerator ROCPROFILER_AGENT_INFO_VERSION_NONE
[#](#_CPPv4N27rocprofiler_agent_version_t35ROCPROFILER_AGENT_INFO_VERSION_NONEE)

-
enumerator ROCPROFILER_AGENT_INFO_VERSION_0
[#](#_CPPv4N27rocprofiler_agent_version_t32ROCPROFILER_AGENT_INFO_VERSION_0E)

-
enumerator ROCPROFILER_AGENT_INFO_VERSION_LAST
[#](#_CPPv4N27rocprofiler_agent_version_t35ROCPROFILER_AGENT_INFO_VERSION_LASTE)

-
enumerator ROCPROFILER_AGENT_INFO_VERSION_NONE

-
typedef rocprofiler_agent_v0_t rocprofiler_agent_t
[#](#_CPPv419rocprofiler_agent_t) Typedef for the current

[rocprofiler_agent_version_t](#group___a_g_e_n_t_s_1ga3825b04602752083b17a8bd29a1acaf0).

-
typedef
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)(*rocprofiler_query_available_agents_cb_t)([rocprofiler_agent_version_t](#_CPPv427rocprofiler_agent_version_t)version, const void **agents, unsigned long num_agents, void *user_data)[#](#_CPPv439rocprofiler_query_available_agents_cb_t) Callback function type for querying the available agents.

If callback is invoked, returns the

[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#group___b_a_s_i_c___d_a_t_a___t_y_p_e_s_1ga952efee747482031f1478b1fcc4eeddc)value returned from callback- Param version:
**[in]**Enum specifying the version of agent info- Param agents:
**[in]**Array of pointers to agents- Param num_agents:
**[in]**Number of agents in array- Param user_data:
**[in]**Data pointer passback- Retval ROCPROFILER_STATUS_ERROR_INCOMPATIBLE_ABI:
size of the agent struct in application is larger than the agent struct for rocprofiler-sdk

- Retval ROCPROFILER_STATUS_ERROR_INVALID_ARGUMENT:
Invalid

[rocprofiler_agent_version_t](#group___a_g_e_n_t_s_1ga3825b04602752083b17a8bd29a1acaf0)value- Return:


- rocprofiler_agent_v0_t

-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_query_available_agents([rocprofiler_agent_version_t](#_CPPv427rocprofiler_agent_version_t)version,[rocprofiler_query_available_agents_cb_t](#_CPPv439rocprofiler_query_available_agents_cb_t)callback, unsigned long agent_size, void *user_data)[#](#_CPPv434rocprofiler_query_available_agents27rocprofiler_agent_version_t39rocprofiler_query_available_agents_cb_tmPv) Receive synchronous callback with an array of available agents at moment of invocation.

- Parameters:
**version**–**[in]**Enum value specifying the struct type of the agent info**callback**–**[in]**Callback function accepting list of agents**agent_size**–**[in]**Should be set to sizeof(rocprofiler_agent_t)**user_data**–**[in]**Data pointer provided to callback

- Returns:


-
struct rocprofiler_agent_cache_t
[#](#_CPPv425rocprofiler_agent_cache_t) *#include <rocprofiler-sdk/agent.h>*Cache information for an agent.


-
struct rocprofiler_agent_io_link_t
[#](#_CPPv427rocprofiler_agent_io_link_t) *#include <rocprofiler-sdk/agent.h>*IO link information for an agent.


-
struct rocprofiler_agent_mem_bank_t
[#](#_CPPv428rocprofiler_agent_mem_bank_t) *#include <rocprofiler-sdk/agent.h>*Memory bank information for an agent.


-
struct rocprofiler_agent_runtime_visiblity_t
[#](#_CPPv437rocprofiler_agent_runtime_visiblity_t) *#include <rocprofiler-sdk/agent.h>*Provides an

*estimate*about the runtime visibility of an agent based on the environment variables (ROCR_VISIBLE_DEVICES, HIP_VISIBLE_DEVICES, GPU_DEVICE_ORDINAL, CUDA_VISIBLE_DEVICES). Reference:[https://rocm.docs.amd.com/en/latest/conceptual/gpu-isolation.html](https://rocm.docs.amd.com/en/latest/conceptual/gpu-isolation.html).
