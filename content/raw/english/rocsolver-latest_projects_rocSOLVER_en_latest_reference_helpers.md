---
title: "rocSOLVER library and logging functions &#8212; rocSOLVER 3.32.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocSOLVER/en/latest/reference/helpers.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:10:53.962813+00:00
content_hash: "a6da30e579896ee6"
---

# rocSOLVER library and logging functions[#](#rocsolver-library-and-logging-functions)

These are helper functions that retrieve information and control some functions of the library. The helper functions are divided into the following categories:

[Library information](#lib-info): Return information about the library version.[Algorithm selection](#algo-select): Select different algorithm modes of certain APIs.[Logging functions](#api-logging): Control the[rocSOLVER multi-level logging](../howto/logging.html#logging-label)capabilities.

## Library information[#](#library-information)

-
[rocblas_status](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/enumerations.html#_CPPv414rocblas_status)rocsolver_get_version_string(char *buf, size_t len)[#](#_CPPv428rocsolver_get_version_stringPc6size_t) GET_VERSION_STRING Queries the library version.

- Parameters:
**buf**–**[out]**A buffer that the version string will be written into.**len**–**[in]**The size of the given buffer in bytes.



-
[rocblas_status](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/enumerations.html#_CPPv414rocblas_status)rocsolver_get_version_string_size(size_t *len)[#](#_CPPv433rocsolver_get_version_string_sizeP6size_t) GET_VERSION_STRING_SIZE Queries the minimum buffer size for a successful call to

[rocsolver_get_version_string](#rocsolver-functions_8h_1a08c71a84eb864521ca71f2d833ccc5b4).- Parameters:
**len**–**[out]**pointer to size_t. The minimum length of buffer to pass to[rocsolver_get_version_string](#rocsolver-functions_8h_1a08c71a84eb864521ca71f2d833ccc5b4).


## Algorithm selection[#](#algorithm-selection)

-
[rocblas_status](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/enumerations.html#_CPPv414rocblas_status)rocsolver_set_alg_mode([rocblas_handle](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv414rocblas_handle)handle, const[rocsolver_function](types.html#_CPPv418rocsolver_function)func, const[rocsolver_alg_mode](types.html#_CPPv418rocsolver_alg_mode)mode)[#](#_CPPv422rocsolver_set_alg_mode14rocblas_handleK18rocsolver_functionK18rocsolver_alg_mode) SET_ALG_MODE sets the algorithm mode to be used by the specified function.

- Parameters:
**handle**–**[in]**rocblas_handle.**func**–**[in]**[rocsolver_function](types.html#rocsolver-extra-types_8h_1a251296f9df0bb35186b64bc5b5cc4fd4). The function that will use the selected algorithm mode.**mode**–**[in]**[rocsolver_alg_mode](types.html#rocsolver-extra-types_8h_1a736dec4bfb5ab967bf6c29c675eeb9f8). The algorithm mode that will be used by the specified function. rocsolver_alg_mode_mixed is not supported.



-
[rocblas_status](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/enumerations.html#_CPPv414rocblas_status)rocsolver_get_alg_mode([rocblas_handle](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv414rocblas_handle)handle, const[rocsolver_function](types.html#_CPPv418rocsolver_function)func,[rocsolver_alg_mode](types.html#_CPPv418rocsolver_alg_mode)*mode)[#](#_CPPv422rocsolver_get_alg_mode14rocblas_handleK18rocsolver_functionP18rocsolver_alg_mode) GET_ALG_MODE gets the algorithm mode being used by the specified function.

- Parameters:
**handle**–**[in]**rocblas_handle.**func**–**[in]**[rocsolver_function](types.html#rocsolver-extra-types_8h_1a251296f9df0bb35186b64bc5b5cc4fd4). The specified function.**mode**–**[out]**pointer to[rocsolver_alg_mode](types.html#rocsolver-extra-types_8h_1a736dec4bfb5ab967bf6c29c675eeb9f8). On exit, the value is overwritten by the algorithm mode used by the specified function.



## Logging functions[#](#logging-functions)

-
[rocblas_status](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/enumerations.html#_CPPv414rocblas_status)rocsolver_log_begin(void)[#](#_CPPv419rocsolver_log_beginv) LOG_BEGIN begins a rocSOLVER multi-level logging session.

Initializes the rocSOLVER logging environment with default values (no logging and one level depth). Default mode can be overridden by using the environment variables ROCSOLVER_LAYER and ROCSOLVER_LEVELS.

This function also sets the streams where the log results will be outputted. The default is STDERR for all the modes. This default can also be overridden using the environment variable ROCSOLVER_LOG_PATH, or specifically ROCSOLVER_LOG_TRACE_PATH, ROCSOLVER_LOG_BENCH_PATH, and/or ROCSOLVER_LOG_PROFILE_PATH.


-
[rocblas_status](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/enumerations.html#_CPPv414rocblas_status)rocsolver_log_end(void)[#](#_CPPv417rocsolver_log_endv) LOG_END ends the multi-level rocSOLVER logging session.

If applicable, this function also prints the profile logging results before cleaning the logging environment.


-
[rocblas_status](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/enumerations.html#_CPPv414rocblas_status)rocsolver_log_set_layer_mode(const[rocblas_layer_mode_flags](types.html#_CPPv424rocblas_layer_mode_flags)layer_mode)[#](#_CPPv428rocsolver_log_set_layer_modeK24rocblas_layer_mode_flags) LOG_SET_LAYER_MODE sets the logging mode for the rocSOLVER multi-level logging environment.

- Parameters:
**layer_mode**–**[in]**rocblas_layer_mode_flags. Specifies the logging mode.


-
[rocblas_status](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/enumerations.html#_CPPv414rocblas_status)rocsolver_log_set_max_levels(const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)max_levels)[#](#_CPPv428rocsolver_log_set_max_levelsK11rocblas_int) LOG_SET_MAX_LEVELS sets the maximum trace log depth for the rocSOLVER multi-level logging environment.

- Parameters:
**max_levels**–**[in]**rocblas_int. max_levels >= 1. Specifies the maximum depth at which nested function calls will appear in the trace and profile logs.


-
[rocblas_status](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/enumerations.html#_CPPv414rocblas_status)rocsolver_log_restore_defaults(void)[#](#_CPPv430rocsolver_log_restore_defaultsv) LOG_RESTORE_DEFAULTS restores the default values of the rocSOLVER multi-level logging environment.

This function sets the logging mode and maximum trace log depth to their default values (no logging and one level depth).


-
[rocblas_status](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/enumerations.html#_CPPv414rocblas_status)rocsolver_log_write_profile(void)[#](#_CPPv427rocsolver_log_write_profilev) LOG_WRITE_PROFILE prints the profile logging results.


-
[rocblas_status](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/enumerations.html#_CPPv414rocblas_status)rocsolver_log_flush_profile(void)[#](#_CPPv427rocsolver_log_flush_profilev) LOG_FLUSH_PROFILE prints the profile logging results and clears the profile record.
