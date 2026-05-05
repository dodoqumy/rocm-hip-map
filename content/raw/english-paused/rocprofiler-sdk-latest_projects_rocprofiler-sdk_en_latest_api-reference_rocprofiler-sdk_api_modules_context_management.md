---
title: "Context management &#8212; ROCprofiler-SDK 1.1.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/api-reference/rocprofiler-sdk_api/modules/context_management.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:15:16.822709+00:00
content_hash: "4ab0f29c6491f6c6"
---

# Context management[#](#context-management)

-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_create_context([rocprofiler_context_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv424rocprofiler_context_id_t)*context_id)[#](#_CPPv426rocprofiler_create_contextP24rocprofiler_context_id_t) Create context.

- Parameters:
**context_id**–**[out]**Context identifier- Returns:


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_start_context([rocprofiler_context_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv424rocprofiler_context_id_t)context_id)[#](#_CPPv425rocprofiler_start_context24rocprofiler_context_id_t) Start context.

- Parameters:
**context_id**–**[in]**Identifier for context to be activated- Returns:


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_stop_context([rocprofiler_context_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv424rocprofiler_context_id_t)context_id)[#](#_CPPv424rocprofiler_stop_context24rocprofiler_context_id_t) Stop context.

- Parameters:
**context_id**–**[in]**Identifier for context to be deactivated- Returns:


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_context_is_active([rocprofiler_context_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv424rocprofiler_context_id_t)context_id, int *status)[#](#_CPPv429rocprofiler_context_is_active24rocprofiler_context_id_tPi) Query whether context is currently active.

- Parameters:
**context_id**–**[in]**Context identifier for the query**status**–**[out]**If context is active, this will be a nonzero value

- Return values:
**ROCPROFILER_STATUS_SUCCESS**– The input context id identified a registered context**ROCPROFILER_STATUS_ERROR_CONTEXT_NOT_FOUND**– The input context id did not identify a registered context

- Returns:


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_context_is_valid([rocprofiler_context_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv424rocprofiler_context_id_t)context_id, int *status)[#](#_CPPv428rocprofiler_context_is_valid24rocprofiler_context_id_tPi) Query whether the context is valid.

- Parameters:
**context_id**–**[in]**Context identifier for the query**status**–**[out]**If context is invalid, this will be a nonzero value

- Returns:


-
ROCPROFILER_CONTEXT_NONE
[#](#c.ROCPROFILER_CONTEXT_NONE) The NULL Context handle.
