---
title: "Counters &#8212; ROCprofiler-SDK 1.1.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/api-reference/rocprofiler-sdk_api/modules/counters.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:15:30.077200+00:00
content_hash: "e2357e23a4de0350"
---

# Counters[#](#counters)

-
typedef
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)(*rocprofiler_available_counters_cb_t)([rocprofiler_agent_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv422rocprofiler_agent_id_t)agent_id,[rocprofiler_counter_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv424rocprofiler_counter_id_t)*counters, unsigned long num_counters, void *user_data)[#](#_CPPv435rocprofiler_available_counters_cb_t) (experimental) Callback that gives a list of counters available on an agent. The counters variable is owned by rocprofiler and should not be free’d.

- Param agent_id:
**[in]**Agent ID of the current callback- Param counters:
**[in]**An array of counters that are avialable on the agent[rocprofiler_iterate_agent_supported_counters](#group___c_o_u_n_t_e_r_s_1ga55713ffe2b4d17a497eaa00774710534)was called on.- Param num_counters:
**[in]**Number of counters contained in counters- Param user_data:
**[in]**User data supplied by[rocprofiler_iterate_agent_supported_counters](#group___c_o_u_n_t_e_r_s_1ga55713ffe2b4d17a497eaa00774710534)


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_query_record_counter_id([rocprofiler_counter_instance_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv433rocprofiler_counter_instance_id_t)id,[rocprofiler_counter_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv424rocprofiler_counter_id_t)*counter_id)[#](#_CPPv435rocprofiler_query_record_counter_id33rocprofiler_counter_instance_id_tP24rocprofiler_counter_id_t) (experimental) Query counter id information from record_id.

- Parameters:
**id**–**[in]**record id from[rocprofiler_counter_record_t](../global_data_structures_topics_files/global_basic_data_types.html#structrocprofiler__counter__record__t)**counter_id**–**[out]**counter id associated with the record

- Return values:
**ROCPROFILER_STATUS_SUCCESS**– if id decoded- Returns:


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_query_record_dimension_position([rocprofiler_counter_instance_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv433rocprofiler_counter_instance_id_t)id,[rocprofiler_counter_dimension_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv434rocprofiler_counter_dimension_id_t)dim, unsigned long *pos)[#](#_CPPv443rocprofiler_query_record_dimension_position33rocprofiler_counter_instance_id_t34rocprofiler_counter_dimension_id_tPm) (experimental) Query dimension position from record_id. If the dimension does not exist in the counter, the return will be 0.

- Parameters:
**id**–**[in]**record id from[rocprofiler_counter_record_t](../global_data_structures_topics_files/global_basic_data_types.html#structrocprofiler__counter__record__t)**dim**–**[in]**dimension for which positional info is requested (currently only 0 is allowed, i.e. flat array without dimension).**pos**–**[out]**value of the dimension in id

- Return values:
**ROCPROFILER_STATUS_SUCCESS**– if dimension decoded- Returns:


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_query_counter_info([rocprofiler_counter_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv424rocprofiler_counter_id_t)counter_id,[rocprofiler_counter_info_version_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv437rocprofiler_counter_info_version_id_t)version, void *info)[#](#_CPPv430rocprofiler_query_counter_info24rocprofiler_counter_id_t37rocprofiler_counter_info_version_id_tPv) (experimental) Query Counter info such as name or description.

- Parameters:
**counter_id**–**[in]**counter to get info for**version**–**[in]**Version of struct in info, see[rocprofiler_counter_info_version_id_t](../global_data_structures_topics_files/global_basic_data_types.html#group___b_a_s_i_c___d_a_t_a___t_y_p_e_s_1gafaa2562d8c2611d781e4356e43d0f884)for available types**info**–**[out]**rocprofiler_counter_info_{version}_t struct to write info to.

- Return values:
**ROCPROFILER_STATUS_SUCCESS**– if counter found**ROCPROFILER_STATUS_ERROR_COUNTER_NOT_FOUND**– if counter not found**ROCPROFILER_STATUS_ERROR_INCOMPATIBLE_ABI**– Version is not supported

- Returns:


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_iterate_agent_supported_counters([rocprofiler_agent_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv422rocprofiler_agent_id_t)agent_id,[rocprofiler_available_counters_cb_t](#_CPPv435rocprofiler_available_counters_cb_t)cb, void *user_data)[#](#_CPPv444rocprofiler_iterate_agent_supported_counters22rocprofiler_agent_id_t35rocprofiler_available_counters_cb_tPv) (experimental) Query Agent Counters Availability.

- Parameters:
**agent_id**–**[in]**GPU agent identifier**cb**–**[in]**callback to caller to get counters**user_data**–**[in]**data to pass into the callback

- Return values:
**ROCPROFILER_STATUS_SUCCESS**– if counters found for agent**ROCPROFILER_STATUS_ERROR**– if no counters found for agent

- Returns:


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_create_counter(const char *name, unsigned long name_len, const char *expr, unsigned long expr_len, const char *description, unsigned long description_len,[rocprofiler_agent_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv422rocprofiler_agent_id_t)agent,[rocprofiler_counter_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv424rocprofiler_counter_id_t)*counter_id)[#](#_CPPv426rocprofiler_create_counterPKcmPKcmPKcm22rocprofiler_agent_id_tP24rocprofiler_counter_id_t) (experimental) Creates a new counter based on a derived metric provided. The counter will only be available for counter collection profiles created after the addition of this counter. Due to the regeneration of internal ASTs and dimension cache, this call may be slow and should generally be avoided in performance sensitive code blocks (i.e. dispatch callbacks).

- Parameters:
**name**–**[in]**The name of the new counter.**name_len**–**[in]**The length of the counter name.**expr**–**[in]**The counter expression, formatted identically to YAML counter definitions.**expr_len**–**[in]**The length of the expression.**agent**–**[in]**The[rocprofiler_agent_id_t](../global_data_structures_topics_files/global_basic_data_types.html#structrocprofiler__agent__id__t)specifying the agent for which to create the counter.**description**–**[in]**The description of the new counter (optional).**description_len**–**[in]**The length of the description.**counter_id**–**[out]**The[rocprofiler_counter_id_t](../global_data_structures_topics_files/global_basic_data_types.html#structrocprofiler__counter__id__t)of the created counter.

- Return values:
**ROCPROFILER_STATUS_SUCCESS**– if the counter was successfully created.**ROCPROFILER_STATUS_ERROR_AST_GENERATION_FAILED**– if the counter could not be created.**ROCPROFILER_STATUS_ERROR_INVALID_ARGUMENT**– if a counter argument is incorrect**ROCPROFILER_STATUS_ERROR_AGENT_NOT_FOUND**– if the agent is not found

- Returns:


-
struct rocprofiler_counter_info_v0_t
[#](#_CPPv429rocprofiler_counter_info_v0_t) *#include <rocprofiler-sdk/counters.h>*(experimental) Counter info struct version 0


-
struct rocprofiler_counter_dimension_info_t
[#](#_CPPv436rocprofiler_counter_dimension_info_t) *#include <rocprofiler-sdk/counters.h>*(experimental) Represents metadata about a single dimension of a counter instance.

This structure provides the name of the dimension (e.g., “XCC”, “SE”, etc.) and the index indicating the position of a specific counter instance within that dimension.


-
struct rocprofiler_counter_record_dimension_instance_info_t
[#](#_CPPv452rocprofiler_counter_record_dimension_instance_info_t) *#include <rocprofiler-sdk/counters.h>*(experimental) Describes a specific counter instance and its position across multiple dimensions.

This structure provides the unique instance ID, associated counter ID, number of dimensions for the instance, and a pointer to an array of metadata describing each dimension’s name and index.


-
struct rocprofiler_counter_info_v1_t
[#](#_CPPv429rocprofiler_counter_info_v1_t) *#include <rocprofiler-sdk/counters.h>*(experimental) Counter info struct version 1. Combines information from

[rocprofiler_counter_info_v0_t](#structrocprofiler__counter__info__v0__t)with the dimension information.
