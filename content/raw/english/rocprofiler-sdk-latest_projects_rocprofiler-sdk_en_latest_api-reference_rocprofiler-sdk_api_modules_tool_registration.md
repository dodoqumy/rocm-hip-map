---
title: "Tool registration &#8212; ROCprofiler-SDK 1.1.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/api-reference/rocprofiler-sdk_api/modules/tool_registration.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:24:46.519628+00:00
content_hash: "3027bc5510f06d74"
---

# Tool registration[#](#tool-registration)

-
typedef void (*rocprofiler_client_finalize_t)(
[rocprofiler_client_id_t](#_CPPv423rocprofiler_client_id_t))[#](#_CPPv429rocprofiler_client_finalize_t) Prototype for the function pointer provided to tool in

[rocprofiler_tool_initialize_t](#group___r_e_g_i_s_t_r_a_t_i_o_n___g_r_o_u_p_1ga509840554a71daf97aa3ec23642672fb). This function can be used to explicitly invoke the client tools[rocprofiler_tool_finalize_t](#group___r_e_g_i_s_t_r_a_t_i_o_n___g_r_o_u_p_1ga0532a1f02b5728f58d916c78145e90e3)finalization function prior to the`atexit`

handler which calls it.If this function pointer is invoked explicitly, rocprofiler will disable calling the

[rocprofiler_tool_finalize_t](#group___r_e_g_i_s_t_r_a_t_i_o_n___g_r_o_u_p_1ga0532a1f02b5728f58d916c78145e90e3)functioin pointer during it’s`atexit`

handler.

-
typedef int (*rocprofiler_tool_initialize_t)(
[rocprofiler_client_finalize_t](#_CPPv429rocprofiler_client_finalize_t)finalize_func, void *tool_data)[#](#_CPPv429rocprofiler_tool_initialize_t) Prototype for the initialize function where a tool creates contexts for the set of rocprofiler services used by the tool.

- Param finalize_func:
**[in]**Function pointer to explicitly invoke the finalize function for the client- Param tool_data:
**[in]**`tool_data`

field returned from[rocprofiler_configure](#group___r_e_g_i_s_t_r_a_t_i_o_n___g_r_o_u_p_1gaacc20d4f9bda3e14f11d3c4038178743)in[rocprofiler_tool_configure_result_t](#structrocprofiler__tool__configure__result__t).


-
typedef void (*rocprofiler_tool_finalize_t)(void *tool_data)
[#](#_CPPv427rocprofiler_tool_finalize_t) Prototype for the finalize function where a tool does any cleanup or output operations once it has finished using rocprofiler services.

- Param tool_data:
**[in]**`tool_data`

field returned from[rocprofiler_configure](#group___r_e_g_i_s_t_r_a_t_i_o_n___g_r_o_u_p_1gaacc20d4f9bda3e14f11d3c4038178743)in[rocprofiler_tool_configure_result_t](#structrocprofiler__tool__configure__result__t).


-
typedef
[rocprofiler_tool_configure_result_t](#_CPPv435rocprofiler_tool_configure_result_t)*(*rocprofiler_configure_func_t)(uint32_t version, const char *runtime_version, uint32_t priority,[rocprofiler_client_id_t](#_CPPv423rocprofiler_client_id_t)*client_id)[#](#_CPPv428rocprofiler_configure_func_t) Function pointer typedef for

[rocprofiler_configure](#group___r_e_g_i_s_t_r_a_t_i_o_n___g_r_o_u_p_1gaacc20d4f9bda3e14f11d3c4038178743)function.- Param version:
**[in]**The version of rocprofiler:`(10000 * major) + (100 * minor) + patch`

- Param runtime_version:
**[in]**String descriptor of the rocprofiler version and other relevant info.- Param priority:
**[in]**How many client tools were initialized before this client tool- Param client_id:
**[inout]**tool identifier value.


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_is_initialized(int *status)[#](#_CPPv426rocprofiler_is_initializedPi) Query whether rocprofiler has already scanned the binary for all the instances of

[rocprofiler_configure](#group___r_e_g_i_s_t_r_a_t_i_o_n___g_r_o_u_p_1gaacc20d4f9bda3e14f11d3c4038178743)(or is currently scanning). If rocprofiler has completed it’s scan, clients can directly register themselves with rocprofiler.- Parameters:
**status**–**[out]**0 indicates rocprofiler has not been initialized (i.e. configured), 1 indicates rocprofiler has been initialized, -1 indicates rocprofiler is currently initializing.- Return values:
**ROCPROFILER_STATUS_SUCCESS**– Returned unconditionally- Returns:


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_is_finalized(int *status)[#](#_CPPv424rocprofiler_is_finalizedPi) Query rocprofiler finalization status.

- Parameters:
**status**–**[out]**0 indicates rocprofiler has not been finalized, 1 indicates rocprofiler has been finalized, -1 indicates rocprofiler is currently finalizing.- Return values:
**ROCPROFILER_STATUS_SUCCESS**– Returned unconditionally- Returns:


-
[rocprofiler_tool_configure_result_t](#_CPPv435rocprofiler_tool_configure_result_t)*rocprofiler_configure(uint32_t version, const char *runtime_version, uint32_t priority,[rocprofiler_client_id_t](#_CPPv423rocprofiler_client_id_t)*client_id)[#](#_CPPv421rocprofiler_configure8uint32_tPKc8uint32_tP23rocprofiler_client_id_t) This is the special function that tools define to enable rocprofiler support. The tool should return a pointer to

[rocprofiler_tool_configure_result_t](#structrocprofiler__tool__configure__result__t)which will contain a function pointer to (1) an initialization function where all the contexts are created, (2) a finalization function (if necessary) which will be invoked when rocprofiler shutdown and, (3) a pointer to any data that the tool wants communicated between the rocprofiler_tool_configure_result_t::initialize and rocprofiler_tool_configure_result_t::finalize functions. If the user.#include <rocprofiler-sdk/registration.h> static rocprofiler_client_id_t my_client_id; static rocprofiler_client_finalize_t my_fini_func; static int my_tool_data = 1234; static int my_init_func(rocprofiler_client_finalize_t fini_func, void* tool_data) { my_fini_func = fini_func; assert(*static_cast<int*>(tool_data) == 1234 && "tool_data is wrong"); rocprofiler_context_id_t ctx{0}; rocprofiler_create_context(&ctx); if(int valid_ctx = 0; rocprofiler_context_is_valid(ctx, &valid_ctx) != ROCPROFILER_STATUS_SUCCESS || valid_ctx != 0) { // notify rocprofiler that initialization failed // and all the contexts, buffers, etc. created // should be ignored return -1; } if(rocprofiler_start_context(ctx) != ROCPROFILER_STATUS_SUCCESS) { // notify rocprofiler that initialization failed // and all the contexts, buffers, etc. created // should be ignored return -1; } // no errors return 0; } static int my_fini_func(void* tool_data) { assert(*static_cast<int*>(tool_data) == 1234 && "tool_data is wrong"); } rocprofiler_tool_configure_result_t* rocprofiler_configure(uint32_t version, const char* runtime_version, uint32_t priority, rocprofiler_client_id_t* client_id) { // only activate if main tool if(priority > 0) return nullptr; // set the client name client_id->name = "ExampleTool"; // make a copy of client info my_client_id = *client_id; // compute major/minor/patch version info uint32_t major = version / 10000; uint32_t minor = (version % 10000) / 100; uint32_t patch = version % 100; // print info printf("Configuring %s with rocprofiler-sdk (v%u.%u.%u) [%s]\n", client_id->name, major, minor, patch, runtime_version); // create configure data static auto cfg = rocprofiler_tool_configure_result_t{ &my_init_func, &my_fini_func, &my_tool_data }; // return pointer to configure data return &cfg; }

- Parameters:
**version**–**[in]**The version of rocprofiler:`(10000 * major) + (100 * minor) + patch`

**runtime_version**–**[in]**String descriptor of the rocprofiler version and other relevant info.**priority**–**[in]**How many client tools were initialized before this client tool**client_id**–**[inout]**tool identifier value.

- Returns:
rocprofiler_tool_configure_result_t*



-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_force_configure([rocprofiler_configure_func_t](#_CPPv428rocprofiler_configure_func_t)configure_func)[#](#_CPPv427rocprofiler_force_configure28rocprofiler_configure_func_t) Function for explicitly registering a configuration with rocprofiler. This can be invoked before any ROCm runtimes (lazily) initialize and context(s) can be started before the runtimes initialize.

- Parameters:
**configure_func**–**[in]**Address of[rocprofiler_configure](#group___r_e_g_i_s_t_r_a_t_i_o_n___g_r_o_u_p_1gaacc20d4f9bda3e14f11d3c4038178743)function. A null pointer is acceptable if the address is not known- Return values:
**ROCPROFILER_STATUS_SUCCESS**– Registration was successfully triggered.**ROCPROFILER_STATUS_ERROR_CONFIGURATION_LOCKED**– Returned if rocprofiler has already been configured, or is currently being configured

- Returns:


-
struct rocprofiler_client_id_t
[#](#_CPPv423rocprofiler_client_id_t) *#include <rocprofiler-sdk/registration.h>*(experimental) A client refers to an individual or entity engaged in the configuration of ROCprofiler services. e.g: any third party tool like PAPI or any internal tool (Omnitrace). A pointer to this data structure is provided to the client tool initialization function. The name member can be set by the client to assist with debugging (e.g. rocprofiler cannot start your context because there is a conflicting context started by

`<name>`

— at least that is the plan). The handle member is a unique identifer assigned by rocprofiler for the client and the client can store it and pass it to the[rocprofiler_client_finalize_t](#group___r_e_g_i_s_t_r_a_t_i_o_n___g_r_o_u_p_1ga0d68596216da9ab144cc6577833637e5)function to force finalization (i.e. deactivate all of it’s contexts) for the client.

-
struct rocprofiler_tool_configure_result_t
[#](#_CPPv435rocprofiler_tool_configure_result_t) *#include <rocprofiler-sdk/registration.h>*Data structure containing a initialization, finalization, and data.

After rocprofiler has retrieved all instances of

[rocprofiler_tool_configure_result_t](#structrocprofiler__tool__configure__result__t)from the tools — via either[rocprofiler_configure](#group___r_e_g_i_s_t_r_a_t_i_o_n___g_r_o_u_p_1gaacc20d4f9bda3e14f11d3c4038178743)and/or[rocprofiler_force_configure](#group___r_e_g_i_s_t_r_a_t_i_o_n___g_r_o_u_p_1gac2f68cfb3be623e1015d5c3214615af2), rocprofiler will invoke all non-null`initialize`

functions and provide the user a function pointer which will explicitly invoke the`finalize`

function pointer. Both the`initialize`

and`finalize`

functions will be passed the value of the`tool_data`

field. The`size`

field is used for ABI reasons, in the event that rocprofiler changes the[rocprofiler_tool_configure_result_t](#structrocprofiler__tool__configure__result__t)struct and it should be set to`sizeof(rocprofiler_tool_configure_result_t)`
