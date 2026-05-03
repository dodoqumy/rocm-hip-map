---
title: "Counter config &#8212; ROCprofiler-SDK 1.1.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/api-reference/rocprofiler-sdk_api/modules/counter_config.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-03T06:26:30.835248+00:00
content_hash: "c67699f1d91a8036"
---

# Counter config[#](#counter-config)

-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_create_counter_config([rocprofiler_agent_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv422rocprofiler_agent_id_t)agent_id,[rocprofiler_counter_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv424rocprofiler_counter_id_t)*counters_list, unsigned long counters_count,[rocprofiler_counter_config_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv431rocprofiler_counter_config_id_t)*config_id)[#](#_CPPv433rocprofiler_create_counter_config22rocprofiler_agent_id_tP24rocprofiler_counter_id_tmP31rocprofiler_counter_config_id_t) (experimental) Create Counter Configuration. A config is bound to an agent but can be used across many contexts. The config has a fixed set of counters that are collected (and specified by counter_list). The available counters for an agent can be queried using

[rocprofiler_iterate_agent_supported_counters](counters.html#group___c_o_u_n_t_e_r_s_1ga55713ffe2b4d17a497eaa00774710534). An existing config may be supplied via config_id to use as a base for the new config. All counters in the existing config will be copied over to the new config. The existing config will remain unmodified and usable with the new config id being returned in config_id.- Parameters:
**agent_id**–**[in]**Agent identifier**counters_list**–**[in]**List of GPU counters**counters_count**–**[in]**Size of counters list**config_id**–**[inout]**Identifier for GPU counters group. If an existing config is supplied, that profiles counters will be copied over to a new config (returned via this id)

- Return values:
**ROCPROFILER_STATUS_SUCCESS**– if config created**ROCPROFILER_STATUS_ERROR**– if config could not be created

- Returns:


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_destroy_counter_config([rocprofiler_counter_config_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv431rocprofiler_counter_config_id_t)config_id)[#](#_CPPv434rocprofiler_destroy_counter_config31rocprofiler_counter_config_id_t) (experimental) Destroy Profile Configuration.

- Parameters:
**config_id**–**[in]**- Return values:
**ROCPROFILER_STATUS_SUCCESS**– if config destroyed**ROCPROFILER_STATUS_ERROR**– if config could not be destroyed

- Returns:
