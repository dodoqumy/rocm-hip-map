---
title: "Profiler Control Information &#8212; ROCprofiler-SDK 1.1.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/api-reference/rocprofiler-sdk-roctx_api/roctx_modules/profiler-control.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:15:33.954991+00:00
content_hash: "f9f8a76b6c5a933b"
---

# Profiler Control Information[#](#profiler-control-information)

-
int roctxProfilerPause(
[roctx_thread_id_t](../global_roctx_data_structures_topics_files/global_roctx_basic_data_types.html#_CPPv417roctx_thread_id_t)tid)[#](#_CPPv418roctxProfilerPause17roctx_thread_id_t) Request any currently running profiling tool that is should stop collecting data.

Within a profiling tool, it is recommended that the tool cache all active contexts at the time of the request and then stop them. By convention, the application should pass zero to indicate a global pause of the profiler in the current process. If the application wishes to pause only the current thread, the application should obtain the thread ID via

[roctxGetThreadId](naming-utilities.html#group___u_t_i_l_i_t_i_e_s_1ga02c2d26205c9c0c9a6b896b9d425b081).- Parameters:
**tid**–**[in]**Zero for all threads in current process or non-zero for a specific thread- Returns:
int A profiling tool may choose to set this value to a non-zero value to indicate a failure while executing the request or lack of support. If the profiling tool supports pausing but is already paused, the tool should ignore the request and return zero.



-
int roctxProfilerResume(
[roctx_thread_id_t](../global_roctx_data_structures_topics_files/global_roctx_basic_data_types.html#_CPPv417roctx_thread_id_t)tid)[#](#_CPPv419roctxProfilerResume17roctx_thread_id_t) Request any currently running profiling tool that is should resume collecting data.

Within a profiling tool, it is recommended that the tool re-activated the active contexts which were cached when the pause request was issued. By convention, the application should pass zero to indicate a global pause of the profiler in the current process. If the application wishes to pause only the current thread, the application should obtain the thread ID via

[roctxGetThreadId](naming-utilities.html#group___u_t_i_l_i_t_i_e_s_1ga02c2d26205c9c0c9a6b896b9d425b081).- Parameters:
**tid**–**[in]**Zero for all threads in current process or non-zero for a specific thread- Returns:
int A profiling tool may choose to set this value to a non-zero value to indicate a failure while executing the request or lack of support. If the profiling tool is supports resuming but is already active, the tool should ignore the request and return zero.
