---
title: "Naming Information &#8212; ROCprofiler-SDK 1.1.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/api-reference/rocprofiler-sdk-roctx_api/roctx_modules/naming-utilities.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-03T06:26:39.674471+00:00
content_hash: "007c84fe56aea882"
---

# Naming Information[#](#naming-information)

-
int roctxNameOsThread(const char *name)
[#](#_CPPv417roctxNameOsThreadPKc) Indicate to a profiling tool that, where possible, you would like the current CPU OS thread to be labeled by the provided name in the output of the profiling tool.

Rocprofiler does not provide explicit support for how profiling tools handle this request: support for this capability is tool specific. ROCTx does NOT rename the thread via

`pthread_setname_np`

.- Parameters:
**name**–**[in]**Name for the current OS thread- Returns:
int A profiling tool may choose to set this value to a non-zero value to indicate a failure while executing the request or lack of support



-
int roctxNameHsaAgent(const char *name, const struct hsa_agent_s *agent)
[#](#_CPPv417roctxNameHsaAgentPKcPK11hsa_agent_s) Indicate to a profiling tool that, where possible, you would like the given HSA agent to be labeled by the provided name in the output of the profiling tool.

Rocprofiler does not provide any explicit support for how profiling tools handle this request: support for this capability is tool specific.

- Parameters:
**name**–**[in]**Name for the specified agent**agent**–**[in]**Pointer to a HSA agent identifier

- Returns:
int A profiling tool may choose to set this value to a non-zero value to indicate a failure while executing the request or lack of support



-
int roctxNameHipDevice(const char *name, int device_id)
[#](#_CPPv418roctxNameHipDevicePKci) Indicate to a profiling tool that, where possible, you would like the given HIP device id to be labeled by the provided name in the output of the profiling tool.

Rocprofiler does not provide any explicit support for how profiling tools handle this request: support for this capability is tool specific.

- Parameters:
**name**–**[in]**Name for the specified device**device_id**–**[in]**HIP device ordinal

- Returns:
int A profiling tool may choose to set this value to a non-zero value to indicate a failure while executing the request or lack of support



-
int roctxNameHipStream(const char *name, const struct ihipStream_t *stream)
[#](#_CPPv418roctxNameHipStreamPKcPK12ihipStream_t) Indicate to a profiling tool that, where possible, you would like the given HIP stream to be labeled by the provided name in the output of the profiling tool.

Rocprofiler does not provide any explicit support for how profiling tools handle this request: support for this capability is tool specific.

- Parameters:
**name**–**[in]**Name for the specified stream**stream**–**[in]**A`hipStream_t`

value (hipStream_t == ihipStream_t*)

- Returns:
int A profiling tool may choose to set this value to a non-zero value to indicate a failure while executing the request or lack of support



-
int roctxGetThreadId(
[roctx_thread_id_t](../global_roctx_data_structures_topics_files/global_roctx_basic_data_types.html#_CPPv417roctx_thread_id_t)*tid)[#](#_CPPv416roctxGetThreadIdP17roctx_thread_id_t) Retrieve a id value for the current thread which will be identical to the id value a profiling tool gets via

`rocprofiler_get_thread_id(rocprofiler_thread_id_t*)`

- Parameters:
**tid**– [out] Pointer to where the value should be placed- Returns:
int A profiling tool may choose to set this value to a non-zero value to indicate a failure while executing the request or lack of support
