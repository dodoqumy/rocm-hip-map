---
title: "OMPT Registration &#8212; ROCprofiler-SDK 1.1.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/api-reference/rocprofiler-sdk_api/modules/ompt_registration.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:15:43.807773+00:00
content_hash: "d4780385d417f896"
---

# OMPT Registration[#](#ompt-registration)

-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_ompt_is_initialized(int *status)[#](#_CPPv431rocprofiler_ompt_is_initializedPi) (experimental) Query whether rocprofiler-sdk OMPT implementation has been initialized by OpenMP runtime.

- Parameters:
**status**–**[out]**Set to 0 if rocprofiler OMPT has not been initialized. Otherwise, set to 1.- Return values:
**ROCPROFILER_STATUS_SUCCESS**– Always returns this value- Returns:


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_ompt_is_finalized(int *status)[#](#_CPPv429rocprofiler_ompt_is_finalizedPi) (experimental) Query whether rocprofiler-sdk OMPT implementation has invoked ompt_finalize function.

- Parameters:
**status**–**[out]**Set to 0 if rocprofiler OMPT has not been finalized. Otherwise, set to 1.- Return values:
**ROCPROFILER_STATUS_SUCCESS**– Always returns this value- Returns:


-
ompt_start_tool_result_t *rocprofiler_ompt_start_tool(unsigned int omp_version, const char *runtime_version)
[#](#_CPPv427rocprofiler_ompt_start_tooljPKc) (experimental) If a tool which contains a “ompt_start_tool” function which is invoked by the OpenMP runtime but the tool wishes to defer to rocprofiler-sdk to be the OMPT tool, it should invoke this function from it’s

`ompt_start_tool`

implementation.- Parameters:
**omp_version**–**[in]**Refer to OpenMP OMPT docs for more information**runtime_version**–**[in]**Refer to OpenMP OMPT docs for more information

- Returns:
ompt_start_tool_result_t*
