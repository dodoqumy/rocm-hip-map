---
title: "Ranges Information &#8212; ROCprofiler-SDK 1.1.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/api-reference/rocprofiler-sdk-roctx_api/roctx_modules/ranges.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:24:32.632677+00:00
content_hash: "88378a3c39c136f3"
---

# Ranges Information[#](#ranges-information)

-
int roctxRangePushA(const char *message)
[#](#_CPPv415roctxRangePushAPKc) Start a new nested range.

Nested ranges are stacked and local to the current CPU thread.

- Parameters:
**message**–**[in]**The message associated with this range.- Returns:
Returns the level this nested range is started at. Nested range levels are 0 based.



-
int roctxRangePop()
[#](#_CPPv413roctxRangePopv) Stop the current nested range.

Stop the current nested range, and pop it from the stack. If a nested range was active before the last one was started, it becomes again the current nested range.

- Returns:
Returns the level the stopped nested range was started at, or a negative value if there was no nested range active.



-
[roctx_range_id_t](../global_roctx_data_structures_topics_files/global_roctx_basic_data_types.html#_CPPv416roctx_range_id_t)roctxRangeStartA(const char *message)[#](#_CPPv416roctxRangeStartAPKc) Starts a process range.

Start/stop ranges can be started and stopped in different threads. Each timespan is assigned a unique range ID.

- Parameters:
**message**–**[in]**The message associated with this range.- Returns:
Returns the ID of the new range.



-
void roctxRangeStop(
[roctx_range_id_t](../global_roctx_data_structures_topics_files/global_roctx_basic_data_types.html#_CPPv416roctx_range_id_t)id)[#](#_CPPv414roctxRangeStop16roctx_range_id_t) Stop a process range.

- Parameters:
**id**–**[in]**[roctx_range_id_t](../global_roctx_data_structures_topics_files/global_roctx_basic_data_types.html#group___b_a_s_i_c___d_a_t_a___t_y_p_e_s_1gaed49a7e620fadae3d9ea7050b30847c6)returned from[roctxRangeStartA](#group__range__group_1ga37b17a196b1b8a6b785e94002a87f617)to stop
