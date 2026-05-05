---
title: "Intercept table &#8212; ROCprofiler-SDK 1.1.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/api-reference/rocprofiler-sdk_api/modules/intercept_table.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T18:21:30.492689+00:00
content_hash: "81e19e500209b07f"
---

# Intercept table[#](#intercept-table)

-
typedef void (*rocprofiler_intercept_library_cb_t)(
[rocprofiler_intercept_table_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv429rocprofiler_intercept_table_t)type, uint64_t lib_version, uint64_t lib_instance, void **tables, uint64_t num_tables, void *user_data)[#](#_CPPv434rocprofiler_intercept_library_cb_t) (experimental) Callback type when a new runtime library is loaded.

See also

rocprofiler_at_intercept_table_registration

- Param type:
**[in]**Type of API table- Param lib_version:
**[in]**Major, minor, and patch version of library encoded into single number similar to ROCPROFILER_VERSION- Param lib_instance:
**[in]**The number of times this runtime library has been registered previously- Param tables:
**[in]**An array of pointers to the API tables- Param num_tables:
**[in]**The size of the array of pointers to the API tables- Param user_data:
**[in]**The pointer to the data provided to rocprofiler_at_intercept_table_registration


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_query_intercept_table_name([rocprofiler_intercept_table_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv429rocprofiler_intercept_table_t)kind, const char **name, uint64_t *name_len)[#](#_CPPv438rocprofiler_query_intercept_table_name29rocprofiler_intercept_table_tPPKcP8uint64_t) (experimental) Query the name of the intercept table. The name retrieved from this function is a string literal that is encoded in the read-only section of the binary (i.e. it is always “allocated” and never “deallocated”).

- Parameters:
**kind**–**[in]**Intercept table kind**name**–**[out]**If non-null and the name is a constant string that does not require dynamic allocation, this paramter will be set to the address of the string literal, otherwise it will be set to nullptr**name_len**–**[out]**If non-null, this will be assigned the length of the name (regardless of the name is a constant string or requires dynamic allocation)

- Return values:
**ROCPROFILER_STATUS_ERROR_KIND_NOT_FOUND**– Returned if the domain id is not valid**ROCPROFILER_STATUS_SUCCESS**– Returned if a valid domain, regardless if there is a constant string or not.

- Returns:


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_at_intercept_table_registration([rocprofiler_intercept_library_cb_t](#_CPPv434rocprofiler_intercept_library_cb_t)callback, int libs, void *data)[#](#_CPPv443rocprofiler_at_intercept_table_registration34rocprofiler_intercept_library_cb_tiPv)
