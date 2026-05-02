---
title: "Global Basic Data Types &#8212; ROCprofiler-SDK 1.1.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/api-reference/rocprofiler-sdk_api/global_data_structures_topics_files/global_basic_data_types.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:15:08.148909+00:00
content_hash: "2a21ec340c3cb147"
---

# Global Basic Data Types[#](#global-basic-data-types)

-
enum rocprofiler_status_t
[#](#_CPPv420rocprofiler_status_t) Status codes.

*Values:*-
enumerator ROCPROFILER_STATUS_SUCCESS
[#](#_CPPv4N20rocprofiler_status_t26ROCPROFILER_STATUS_SUCCESSE) No error occurred.


-
enumerator ROCPROFILER_STATUS_ERROR
[#](#_CPPv4N20rocprofiler_status_t24ROCPROFILER_STATUS_ERRORE) Generalized error.


-
enumerator ROCPROFILER_STATUS_ERROR_CONTEXT_NOT_FOUND
[#](#_CPPv4N20rocprofiler_status_t42ROCPROFILER_STATUS_ERROR_CONTEXT_NOT_FOUNDE) No valid context for given context id.


-
enumerator ROCPROFILER_STATUS_ERROR_BUFFER_NOT_FOUND
[#](#_CPPv4N20rocprofiler_status_t41ROCPROFILER_STATUS_ERROR_BUFFER_NOT_FOUNDE) No valid buffer for given buffer id.


-
enumerator ROCPROFILER_STATUS_ERROR_KIND_NOT_FOUND
[#](#_CPPv4N20rocprofiler_status_t39ROCPROFILER_STATUS_ERROR_KIND_NOT_FOUNDE) Kind identifier is invalid.


-
enumerator ROCPROFILER_STATUS_ERROR_OPERATION_NOT_FOUND
[#](#_CPPv4N20rocprofiler_status_t44ROCPROFILER_STATUS_ERROR_OPERATION_NOT_FOUNDE) Operation identifier is invalid for domain.


-
enumerator ROCPROFILER_STATUS_ERROR_THREAD_NOT_FOUND
[#](#_CPPv4N20rocprofiler_status_t41ROCPROFILER_STATUS_ERROR_THREAD_NOT_FOUNDE) No valid thread for given thread id.


-
enumerator ROCPROFILER_STATUS_ERROR_AGENT_NOT_FOUND
[#](#_CPPv4N20rocprofiler_status_t40ROCPROFILER_STATUS_ERROR_AGENT_NOT_FOUNDE) Agent identifier not found.


-
enumerator ROCPROFILER_STATUS_ERROR_COUNTER_NOT_FOUND
[#](#_CPPv4N20rocprofiler_status_t42ROCPROFILER_STATUS_ERROR_COUNTER_NOT_FOUNDE) Counter identifier does not exist.


-
enumerator ROCPROFILER_STATUS_ERROR_CONTEXT_ERROR
[#](#_CPPv4N20rocprofiler_status_t38ROCPROFILER_STATUS_ERROR_CONTEXT_ERRORE) Generalized context error.


-
enumerator ROCPROFILER_STATUS_ERROR_CONTEXT_INVALID
[#](#_CPPv4N20rocprofiler_status_t40ROCPROFILER_STATUS_ERROR_CONTEXT_INVALIDE) Context configuration is not valid.


-
enumerator ROCPROFILER_STATUS_ERROR_CONTEXT_NOT_STARTED
[#](#_CPPv4N20rocprofiler_status_t44ROCPROFILER_STATUS_ERROR_CONTEXT_NOT_STARTEDE) Context was not started (e.g., atomic swap into active array failed)


-
enumerator ROCPROFILER_STATUS_ERROR_CONTEXT_CONFLICT
[#](#_CPPv4N20rocprofiler_status_t41ROCPROFILER_STATUS_ERROR_CONTEXT_CONFLICTE) Context operation failed due to a conflict with another context.


-
enumerator ROCPROFILER_STATUS_ERROR_CONTEXT_ID_NOT_ZERO
[#](#_CPPv4N20rocprofiler_status_t44ROCPROFILER_STATUS_ERROR_CONTEXT_ID_NOT_ZEROE) Context ID is not initialized to zero.


-
enumerator ROCPROFILER_STATUS_ERROR_BUFFER_BUSY
[#](#_CPPv4N20rocprofiler_status_t36ROCPROFILER_STATUS_ERROR_BUFFER_BUSYE) buffer operation failed because it currently busy handling another request (e.g. flushing)


-
enumerator ROCPROFILER_STATUS_ERROR_SERVICE_ALREADY_CONFIGURED
[#](#_CPPv4N20rocprofiler_status_t51ROCPROFILER_STATUS_ERROR_SERVICE_ALREADY_CONFIGUREDE) service has already been configured in context


-
enumerator ROCPROFILER_STATUS_ERROR_CONFIGURATION_LOCKED
[#](#_CPPv4N20rocprofiler_status_t45ROCPROFILER_STATUS_ERROR_CONFIGURATION_LOCKEDE) Function call is not valid outside of rocprofiler configuration (i.e. function called post-initialization)


-
enumerator ROCPROFILER_STATUS_ERROR_NOT_IMPLEMENTED
[#](#_CPPv4N20rocprofiler_status_t40ROCPROFILER_STATUS_ERROR_NOT_IMPLEMENTEDE) Function is not implemented.


-
enumerator ROCPROFILER_STATUS_ERROR_INCOMPATIBLE_ABI
[#](#_CPPv4N20rocprofiler_status_t41ROCPROFILER_STATUS_ERROR_INCOMPATIBLE_ABIE) Data structure provided by user is incompatible with current version of rocprofiler.


-
enumerator ROCPROFILER_STATUS_ERROR_INVALID_ARGUMENT
[#](#_CPPv4N20rocprofiler_status_t41ROCPROFILER_STATUS_ERROR_INVALID_ARGUMENTE) Function invoked with one or more invalid arguments.


-
enumerator ROCPROFILER_STATUS_ERROR_METRIC_NOT_VALID_FOR_AGENT
[#](#_CPPv4N20rocprofiler_status_t51ROCPROFILER_STATUS_ERROR_METRIC_NOT_VALID_FOR_AGENTE) Invalid metric supplied to agent.


-
enumerator ROCPROFILER_STATUS_ERROR_FINALIZED
[#](#_CPPv4N20rocprofiler_status_t34ROCPROFILER_STATUS_ERROR_FINALIZEDE) invalid because rocprofiler has been finalized


-
enumerator ROCPROFILER_STATUS_ERROR_HSA_NOT_LOADED
[#](#_CPPv4N20rocprofiler_status_t39ROCPROFILER_STATUS_ERROR_HSA_NOT_LOADEDE) Call requires HSA to be loaded before performed.


-
enumerator ROCPROFILER_STATUS_ERROR_DIM_NOT_FOUND
[#](#_CPPv4N20rocprofiler_status_t38ROCPROFILER_STATUS_ERROR_DIM_NOT_FOUNDE) Dimension is not found for counter.


-
enumerator ROCPROFILER_STATUS_ERROR_PROFILE_COUNTER_NOT_FOUND
[#](#_CPPv4N20rocprofiler_status_t50ROCPROFILER_STATUS_ERROR_PROFILE_COUNTER_NOT_FOUNDE) Profile could not find counter for GPU agent.


-
enumerator ROCPROFILER_STATUS_ERROR_AST_GENERATION_FAILED
[#](#_CPPv4N20rocprofiler_status_t46ROCPROFILER_STATUS_ERROR_AST_GENERATION_FAILEDE) AST could not be generated correctly.


-
enumerator ROCPROFILER_STATUS_ERROR_AST_NOT_FOUND
[#](#_CPPv4N20rocprofiler_status_t38ROCPROFILER_STATUS_ERROR_AST_NOT_FOUNDE) AST was not found.


-
enumerator ROCPROFILER_STATUS_ERROR_AQL_NO_EVENT_COORD
[#](#_CPPv4N20rocprofiler_status_t43ROCPROFILER_STATUS_ERROR_AQL_NO_EVENT_COORDE) Event coordinate was not found by AQL profile.


-
enumerator ROCPROFILER_STATUS_ERROR_INCOMPATIBLE_KERNEL
[#](#_CPPv4N20rocprofiler_status_t44ROCPROFILER_STATUS_ERROR_INCOMPATIBLE_KERNELE) A service depends on a newer version of KFD (amdgpu kernel driver). Check logs for service that report incompatibility.


-
enumerator ROCPROFILER_STATUS_ERROR_OUT_OF_RESOURCES
[#](#_CPPv4N20rocprofiler_status_t41ROCPROFILER_STATUS_ERROR_OUT_OF_RESOURCESE) The given resources are insufficient to complete operation.


-
enumerator ROCPROFILER_STATUS_ERROR_PROFILE_NOT_FOUND
[#](#_CPPv4N20rocprofiler_status_t42ROCPROFILER_STATUS_ERROR_PROFILE_NOT_FOUNDE) Could not find the counter profile.


-
enumerator ROCPROFILER_STATUS_ERROR_AGENT_DISPATCH_CONFLICT
[#](#_CPPv4N20rocprofiler_status_t48ROCPROFILER_STATUS_ERROR_AGENT_DISPATCH_CONFLICTE) Cannot enable both agent and dispatch counting in the same context.


-
enumerator ROCPROFILER_STATUS_INTERNAL_NO_AGENT_CONTEXT
[#](#_CPPv4N20rocprofiler_status_t44ROCPROFILER_STATUS_INTERNAL_NO_AGENT_CONTEXTE) No agent context found, may not be an error.


-
enumerator ROCPROFILER_STATUS_ERROR_SAMPLE_RATE_EXCEEDED
[#](#_CPPv4N20rocprofiler_status_t45ROCPROFILER_STATUS_ERROR_SAMPLE_RATE_EXCEEDEDE) Sample rate exceeded.


-
enumerator ROCPROFILER_STATUS_ERROR_NO_PROFILE_QUEUE
[#](#_CPPv4N20rocprofiler_status_t41ROCPROFILER_STATUS_ERROR_NO_PROFILE_QUEUEE) Profile queue creation failed.


-
enumerator ROCPROFILER_STATUS_ERROR_NO_HARDWARE_COUNTERS
[#](#_CPPv4N20rocprofiler_status_t45ROCPROFILER_STATUS_ERROR_NO_HARDWARE_COUNTERSE) No hardware counters were specified.


-
enumerator ROCPROFILER_STATUS_ERROR_AGENT_MISMATCH
[#](#_CPPv4N20rocprofiler_status_t39ROCPROFILER_STATUS_ERROR_AGENT_MISMATCHE) Agent mismatch between profile and context.


-
enumerator ROCPROFILER_STATUS_ERROR_NOT_AVAILABLE
[#](#_CPPv4N20rocprofiler_status_t38ROCPROFILER_STATUS_ERROR_NOT_AVAILABLEE) The service is not available. Please refer to API functions that return this status code for more information.


-
enumerator ROCPROFILER_STATUS_ERROR_EXCEEDS_HW_LIMIT
[#](#_CPPv4N20rocprofiler_status_t41ROCPROFILER_STATUS_ERROR_EXCEEDS_HW_LIMITE) Exceeds hardware limits for collection.


-
enumerator ROCPROFILER_STATUS_ERROR_AGENT_ARCH_NOT_SUPPORTED
[#](#_CPPv4N20rocprofiler_status_t49ROCPROFILER_STATUS_ERROR_AGENT_ARCH_NOT_SUPPORTEDE) Agent HW architecture not supported.


-
enumerator ROCPROFILER_STATUS_ERROR_PERMISSION_DENIED
[#](#_CPPv4N20rocprofiler_status_t42ROCPROFILER_STATUS_ERROR_PERMISSION_DENIEDE) Permission denied.


-
enumerator ROCPROFILER_STATUS_LAST
[#](#_CPPv4N20rocprofiler_status_t23ROCPROFILER_STATUS_LASTE)

-
enumerator ROCPROFILER_STATUS_SUCCESS

-
enum rocprofiler_buffer_category_t
[#](#_CPPv429rocprofiler_buffer_category_t) Buffer record categories. This enumeration type is encoded in

[rocprofiler_record_header_t](#structrocprofiler__record__header__t)category field.*Values:*-
enumerator ROCPROFILER_BUFFER_CATEGORY_NONE
[#](#_CPPv4N29rocprofiler_buffer_category_t32ROCPROFILER_BUFFER_CATEGORY_NONEE)

-
enumerator ROCPROFILER_BUFFER_CATEGORY_TRACING
[#](#_CPPv4N29rocprofiler_buffer_category_t35ROCPROFILER_BUFFER_CATEGORY_TRACINGE)

-
enumerator ROCPROFILER_BUFFER_CATEGORY_PC_SAMPLING
[#](#_CPPv4N29rocprofiler_buffer_category_t39ROCPROFILER_BUFFER_CATEGORY_PC_SAMPLINGE)

-
enumerator ROCPROFILER_BUFFER_CATEGORY_COUNTERS
[#](#_CPPv4N29rocprofiler_buffer_category_t36ROCPROFILER_BUFFER_CATEGORY_COUNTERSE)

-
enumerator ROCPROFILER_BUFFER_CATEGORY_LAST
[#](#_CPPv4N29rocprofiler_buffer_category_t32ROCPROFILER_BUFFER_CATEGORY_LASTE)

-
enumerator ROCPROFILER_BUFFER_CATEGORY_NONE

-
enum rocprofiler_agent_type_t
[#](#_CPPv424rocprofiler_agent_type_t) Agent type.

*Values:*-
enumerator ROCPROFILER_AGENT_TYPE_NONE
[#](#_CPPv4N24rocprofiler_agent_type_t27ROCPROFILER_AGENT_TYPE_NONEE) Agent type is unknown.


-
enumerator ROCPROFILER_AGENT_TYPE_CPU
[#](#_CPPv4N24rocprofiler_agent_type_t26ROCPROFILER_AGENT_TYPE_CPUE) Agent type is a CPU.


-
enumerator ROCPROFILER_AGENT_TYPE_GPU
[#](#_CPPv4N24rocprofiler_agent_type_t26ROCPROFILER_AGENT_TYPE_GPUE) Agent type is a GPU.


-
enumerator ROCPROFILER_AGENT_TYPE_LAST
[#](#_CPPv4N24rocprofiler_agent_type_t27ROCPROFILER_AGENT_TYPE_LASTE)

-
enumerator ROCPROFILER_AGENT_TYPE_NONE

-
enum rocprofiler_callback_phase_t
[#](#_CPPv428rocprofiler_callback_phase_t) Service Callback Phase.

*Values:*-
enumerator ROCPROFILER_CALLBACK_PHASE_NONE
[#](#_CPPv4N28rocprofiler_callback_phase_t31ROCPROFILER_CALLBACK_PHASE_NONEE) Callback has no phase.


-
enumerator ROCPROFILER_CALLBACK_PHASE_ENTER
[#](#_CPPv4N28rocprofiler_callback_phase_t32ROCPROFILER_CALLBACK_PHASE_ENTERE) Callback invoked prior to function execution.


-
enumerator ROCPROFILER_CALLBACK_PHASE_LOAD
[#](#_CPPv4N28rocprofiler_callback_phase_t31ROCPROFILER_CALLBACK_PHASE_LOADE) Callback invoked prior to code object loading.


-
enumerator ROCPROFILER_CALLBACK_PHASE_EXIT
[#](#_CPPv4N28rocprofiler_callback_phase_t31ROCPROFILER_CALLBACK_PHASE_EXITE) Callback invoked after to function execution.


-
enumerator ROCPROFILER_CALLBACK_PHASE_UNLOAD
[#](#_CPPv4N28rocprofiler_callback_phase_t33ROCPROFILER_CALLBACK_PHASE_UNLOADE) Callback invoked prior to code object unloading.


-
enumerator ROCPROFILER_CALLBACK_PHASE_LAST
[#](#_CPPv4N28rocprofiler_callback_phase_t31ROCPROFILER_CALLBACK_PHASE_LASTE)

-
enumerator ROCPROFILER_CALLBACK_PHASE_NONE

-
enum rocprofiler_callback_tracing_kind_t
[#](#_CPPv435rocprofiler_callback_tracing_kind_t) Service Callback Tracing Kind.

*Values:*-
enumerator ROCPROFILER_CALLBACK_TRACING_NONE
[#](#_CPPv4N35rocprofiler_callback_tracing_kind_t33ROCPROFILER_CALLBACK_TRACING_NONEE)

-
enumerator ROCPROFILER_CALLBACK_TRACING_HSA_CORE_API
[#](#_CPPv4N35rocprofiler_callback_tracing_kind_t41ROCPROFILER_CALLBACK_TRACING_HSA_CORE_APIE) See also

rocprofiler_hsa_core_api_id_t


-
enumerator ROCPROFILER_CALLBACK_TRACING_HSA_AMD_EXT_API
[#](#_CPPv4N35rocprofiler_callback_tracing_kind_t44ROCPROFILER_CALLBACK_TRACING_HSA_AMD_EXT_APIE) See also

rocprofiler_hsa_amd_ext_api_id_t


-
enumerator ROCPROFILER_CALLBACK_TRACING_HSA_IMAGE_EXT_API
[#](#_CPPv4N35rocprofiler_callback_tracing_kind_t46ROCPROFILER_CALLBACK_TRACING_HSA_IMAGE_EXT_APIE) See also

rocprofiler_hsa_image_ext_api_id_t


-
enumerator ROCPROFILER_CALLBACK_TRACING_HSA_FINALIZE_EXT_API
[#](#_CPPv4N35rocprofiler_callback_tracing_kind_t49ROCPROFILER_CALLBACK_TRACING_HSA_FINALIZE_EXT_APIE) See also

rocprofiler_hsa_finalize_ext_api_id_t


-
enumerator ROCPROFILER_CALLBACK_TRACING_HIP_RUNTIME_API
[#](#_CPPv4N35rocprofiler_callback_tracing_kind_t44ROCPROFILER_CALLBACK_TRACING_HIP_RUNTIME_APIE) See also

rocprofiler_hip_runtime_api_id_t


-
enumerator ROCPROFILER_CALLBACK_TRACING_HIP_COMPILER_API
[#](#_CPPv4N35rocprofiler_callback_tracing_kind_t45ROCPROFILER_CALLBACK_TRACING_HIP_COMPILER_APIE) See also

rocprofiler_hip_compiler_api_id_t


-
enumerator ROCPROFILER_CALLBACK_TRACING_MARKER_CORE_API
[#](#_CPPv4N35rocprofiler_callback_tracing_kind_t44ROCPROFILER_CALLBACK_TRACING_MARKER_CORE_APIE) See also

rocprofiler_marker_core_api_id_t


-
enumerator ROCPROFILER_CALLBACK_TRACING_MARKER_CONTROL_API
[#](#_CPPv4N35rocprofiler_callback_tracing_kind_t47ROCPROFILER_CALLBACK_TRACING_MARKER_CONTROL_APIE) See also

rocprofiler_marker_control_api_id_t


-
enumerator ROCPROFILER_CALLBACK_TRACING_MARKER_NAME_API
[#](#_CPPv4N35rocprofiler_callback_tracing_kind_t44ROCPROFILER_CALLBACK_TRACING_MARKER_NAME_APIE) See also

rocprofiler_marker_name_api_id_t


-
enumerator ROCPROFILER_CALLBACK_TRACING_CODE_OBJECT
[#](#_CPPv4N35rocprofiler_callback_tracing_kind_t40ROCPROFILER_CALLBACK_TRACING_CODE_OBJECTE)

-
enumerator ROCPROFILER_CALLBACK_TRACING_SCRATCH_MEMORY
[#](#_CPPv4N35rocprofiler_callback_tracing_kind_t43ROCPROFILER_CALLBACK_TRACING_SCRATCH_MEMORYE)

-
enumerator ROCPROFILER_CALLBACK_TRACING_KERNEL_DISPATCH
[#](#_CPPv4N35rocprofiler_callback_tracing_kind_t44ROCPROFILER_CALLBACK_TRACING_KERNEL_DISPATCHE) Callbacks for kernel dispatches.


-
enumerator ROCPROFILER_CALLBACK_TRACING_MEMORY_COPY
[#](#_CPPv4N35rocprofiler_callback_tracing_kind_t40ROCPROFILER_CALLBACK_TRACING_MEMORY_COPYE)

-
enumerator ROCPROFILER_CALLBACK_TRACING_RCCL_API
[#](#_CPPv4N35rocprofiler_callback_tracing_kind_t37ROCPROFILER_CALLBACK_TRACING_RCCL_APIE) RCCL tracing.


-
enumerator ROCPROFILER_CALLBACK_TRACING_OMPT
[#](#_CPPv4N35rocprofiler_callback_tracing_kind_t33ROCPROFILER_CALLBACK_TRACING_OMPTE) See also

rocprofiler_ompt_operation_t


-
enumerator ROCPROFILER_CALLBACK_TRACING_MEMORY_ALLOCATION
[#](#_CPPv4N35rocprofiler_callback_tracing_kind_t46ROCPROFILER_CALLBACK_TRACING_MEMORY_ALLOCATIONE)

-
enumerator ROCPROFILER_CALLBACK_TRACING_RUNTIME_INITIALIZATION
[#](#_CPPv4N35rocprofiler_callback_tracing_kind_t51ROCPROFILER_CALLBACK_TRACING_RUNTIME_INITIALIZATIONE) Callback notifying that a runtime library has been initialized.


-
enumerator ROCPROFILER_CALLBACK_TRACING_ROCDECODE_API
[#](#_CPPv4N35rocprofiler_callback_tracing_kind_t42ROCPROFILER_CALLBACK_TRACING_ROCDECODE_APIE) rocDecode API Tracing


-
enumerator ROCPROFILER_CALLBACK_TRACING_ROCJPEG_API
[#](#_CPPv4N35rocprofiler_callback_tracing_kind_t40ROCPROFILER_CALLBACK_TRACING_ROCJPEG_APIE) rocJPEG API Tracing


-
enumerator ROCPROFILER_CALLBACK_TRACING_HIP_STREAM
[#](#_CPPv4N35rocprofiler_callback_tracing_kind_t39ROCPROFILER_CALLBACK_TRACING_HIP_STREAME)

-
enumerator ROCPROFILER_CALLBACK_TRACING_MARKER_CORE_RANGE_API
[#](#_CPPv4N35rocprofiler_callback_tracing_kind_t50ROCPROFILER_CALLBACK_TRACING_MARKER_CORE_RANGE_APIE) See also

rocprofiler_marker_core_range_api_id_t


-
enumerator ROCPROFILER_CALLBACK_TRACING_LAST
[#](#_CPPv4N35rocprofiler_callback_tracing_kind_t33ROCPROFILER_CALLBACK_TRACING_LASTE)

-
enumerator ROCPROFILER_CALLBACK_TRACING_NONE

-
enum rocprofiler_buffer_tracing_kind_t
[#](#_CPPv433rocprofiler_buffer_tracing_kind_t) Service Buffer Tracing Kind.

*Values:*-
enumerator ROCPROFILER_BUFFER_TRACING_NONE
[#](#_CPPv4N33rocprofiler_buffer_tracing_kind_t31ROCPROFILER_BUFFER_TRACING_NONEE)

-
enumerator ROCPROFILER_BUFFER_TRACING_HSA_CORE_API
[#](#_CPPv4N33rocprofiler_buffer_tracing_kind_t39ROCPROFILER_BUFFER_TRACING_HSA_CORE_APIE) See also

rocprofiler_hsa_core_api_id_t


-
enumerator ROCPROFILER_BUFFER_TRACING_HSA_AMD_EXT_API
[#](#_CPPv4N33rocprofiler_buffer_tracing_kind_t42ROCPROFILER_BUFFER_TRACING_HSA_AMD_EXT_APIE) See also

rocprofiler_hsa_amd_ext_api_id_t


-
enumerator ROCPROFILER_BUFFER_TRACING_HSA_IMAGE_EXT_API
[#](#_CPPv4N33rocprofiler_buffer_tracing_kind_t44ROCPROFILER_BUFFER_TRACING_HSA_IMAGE_EXT_APIE) See also

rocprofiler_hsa_image_ext_api_id_t


-
enumerator ROCPROFILER_BUFFER_TRACING_HSA_FINALIZE_EXT_API
[#](#_CPPv4N33rocprofiler_buffer_tracing_kind_t47ROCPROFILER_BUFFER_TRACING_HSA_FINALIZE_EXT_APIE) See also

rocprofiler_hsa_finalize_ext_api_id_t


-
enumerator ROCPROFILER_BUFFER_TRACING_HIP_RUNTIME_API
[#](#_CPPv4N33rocprofiler_buffer_tracing_kind_t42ROCPROFILER_BUFFER_TRACING_HIP_RUNTIME_APIE) See also

rocprofiler_hip_runtime_api_id_t


-
enumerator ROCPROFILER_BUFFER_TRACING_HIP_COMPILER_API
[#](#_CPPv4N33rocprofiler_buffer_tracing_kind_t43ROCPROFILER_BUFFER_TRACING_HIP_COMPILER_APIE) See also

rocprofiler_hip_compiler_api_id_t


-
enumerator ROCPROFILER_BUFFER_TRACING_MARKER_CORE_API
[#](#_CPPv4N33rocprofiler_buffer_tracing_kind_t42ROCPROFILER_BUFFER_TRACING_MARKER_CORE_APIE) See also

rocprofiler_marker_core_api_id_t


-
enumerator ROCPROFILER_BUFFER_TRACING_MARKER_CONTROL_API
[#](#_CPPv4N33rocprofiler_buffer_tracing_kind_t45ROCPROFILER_BUFFER_TRACING_MARKER_CONTROL_APIE) See also

rocprofiler_marker_control_api_id_t


-
enumerator ROCPROFILER_BUFFER_TRACING_MARKER_NAME_API
[#](#_CPPv4N33rocprofiler_buffer_tracing_kind_t42ROCPROFILER_BUFFER_TRACING_MARKER_NAME_APIE) See also

rocprofiler_marker_name_api_id_t


-
enumerator ROCPROFILER_BUFFER_TRACING_MEMORY_COPY
[#](#_CPPv4N33rocprofiler_buffer_tracing_kind_t38ROCPROFILER_BUFFER_TRACING_MEMORY_COPYE)

-
enumerator ROCPROFILER_BUFFER_TRACING_KERNEL_DISPATCH
[#](#_CPPv4N33rocprofiler_buffer_tracing_kind_t42ROCPROFILER_BUFFER_TRACING_KERNEL_DISPATCHE) Buffer kernel dispatch info.


-
enumerator ROCPROFILER_BUFFER_TRACING_SCRATCH_MEMORY
[#](#_CPPv4N33rocprofiler_buffer_tracing_kind_t41ROCPROFILER_BUFFER_TRACING_SCRATCH_MEMORYE) Buffer scratch memory reclaimation info.


-
enumerator ROCPROFILER_BUFFER_TRACING_CORRELATION_ID_RETIREMENT
[#](#_CPPv4N33rocprofiler_buffer_tracing_kind_t52ROCPROFILER_BUFFER_TRACING_CORRELATION_ID_RETIREMENTE) Correlation ID in no longer in use.


-
enumerator ROCPROFILER_BUFFER_TRACING_RCCL_API
[#](#_CPPv4N33rocprofiler_buffer_tracing_kind_t35ROCPROFILER_BUFFER_TRACING_RCCL_APIE) RCCL tracing.


-
enumerator ROCPROFILER_BUFFER_TRACING_OMPT
[#](#_CPPv4N33rocprofiler_buffer_tracing_kind_t31ROCPROFILER_BUFFER_TRACING_OMPTE) See also

rocprofiler_ompt_operation_t


-
enumerator ROCPROFILER_BUFFER_TRACING_MEMORY_ALLOCATION
[#](#_CPPv4N33rocprofiler_buffer_tracing_kind_t44ROCPROFILER_BUFFER_TRACING_MEMORY_ALLOCATIONE)

-
enumerator ROCPROFILER_BUFFER_TRACING_RUNTIME_INITIALIZATION
[#](#_CPPv4N33rocprofiler_buffer_tracing_kind_t49ROCPROFILER_BUFFER_TRACING_RUNTIME_INITIALIZATIONE) Record indicating a runtime library has been initialized.


-
enumerator ROCPROFILER_BUFFER_TRACING_ROCDECODE_API
[#](#_CPPv4N33rocprofiler_buffer_tracing_kind_t40ROCPROFILER_BUFFER_TRACING_ROCDECODE_APIE) rocDecode tracing


-
enumerator ROCPROFILER_BUFFER_TRACING_ROCJPEG_API
[#](#_CPPv4N33rocprofiler_buffer_tracing_kind_t38ROCPROFILER_BUFFER_TRACING_ROCJPEG_APIE) rocJPEG tracing


-
enumerator ROCPROFILER_BUFFER_TRACING_HIP_STREAM
[#](#_CPPv4N33rocprofiler_buffer_tracing_kind_t37ROCPROFILER_BUFFER_TRACING_HIP_STREAME)

-
enumerator ROCPROFILER_BUFFER_TRACING_HIP_RUNTIME_API_EXT
[#](#_CPPv4N33rocprofiler_buffer_tracing_kind_t46ROCPROFILER_BUFFER_TRACING_HIP_RUNTIME_API_EXTE)

-
enumerator ROCPROFILER_BUFFER_TRACING_HIP_COMPILER_API_EXT
[#](#_CPPv4N33rocprofiler_buffer_tracing_kind_t47ROCPROFILER_BUFFER_TRACING_HIP_COMPILER_API_EXTE)

-
enumerator ROCPROFILER_BUFFER_TRACING_ROCDECODE_API_EXT
[#](#_CPPv4N33rocprofiler_buffer_tracing_kind_t44ROCPROFILER_BUFFER_TRACING_ROCDECODE_API_EXTE)

-
enumerator ROCPROFILER_BUFFER_TRACING_KFD_EVENT_PAGE_MIGRATE
[#](#_CPPv4N33rocprofiler_buffer_tracing_kind_t49ROCPROFILER_BUFFER_TRACING_KFD_EVENT_PAGE_MIGRATEE) See also

rocprofiler_kfd_event_page_migrate_operation_t


-
enumerator ROCPROFILER_BUFFER_TRACING_KFD_EVENT_PAGE_FAULT
[#](#_CPPv4N33rocprofiler_buffer_tracing_kind_t47ROCPROFILER_BUFFER_TRACING_KFD_EVENT_PAGE_FAULTE) See also

rocprofiler_kfd_event_page_fault_operation_t


-
enumerator ROCPROFILER_BUFFER_TRACING_KFD_EVENT_QUEUE
[#](#_CPPv4N33rocprofiler_buffer_tracing_kind_t42ROCPROFILER_BUFFER_TRACING_KFD_EVENT_QUEUEE) See also

rocprofiler_kfd_event_queue_operation_t


-
enumerator ROCPROFILER_BUFFER_TRACING_KFD_EVENT_UNMAP_FROM_GPU
[#](#_CPPv4N33rocprofiler_buffer_tracing_kind_t51ROCPROFILER_BUFFER_TRACING_KFD_EVENT_UNMAP_FROM_GPUE) See also

rocprofiler_kfd_event_unmap_from_gpu_operation_t


-
enumerator ROCPROFILER_BUFFER_TRACING_KFD_EVENT_DROPPED_EVENTS
[#](#_CPPv4N33rocprofiler_buffer_tracing_kind_t51ROCPROFILER_BUFFER_TRACING_KFD_EVENT_DROPPED_EVENTSE) See also

rocprofiler_kfd_event_dropped_events_operation_t


-
enumerator ROCPROFILER_BUFFER_TRACING_KFD_PAGE_MIGRATE
[#](#_CPPv4N33rocprofiler_buffer_tracing_kind_t43ROCPROFILER_BUFFER_TRACING_KFD_PAGE_MIGRATEE) See also

rocprofiler_kfd_page_migrate_operation_t


-
enumerator ROCPROFILER_BUFFER_TRACING_KFD_PAGE_FAULT
[#](#_CPPv4N33rocprofiler_buffer_tracing_kind_t41ROCPROFILER_BUFFER_TRACING_KFD_PAGE_FAULTE) See also

rocprofiler_kfd_page_fault_operation_t


-
enumerator ROCPROFILER_BUFFER_TRACING_KFD_QUEUE
[#](#_CPPv4N33rocprofiler_buffer_tracing_kind_t36ROCPROFILER_BUFFER_TRACING_KFD_QUEUEE) See also

rocprofiler_kfd_queue_operation_t


-
enumerator ROCPROFILER_BUFFER_TRACING_MARKER_CORE_RANGE_API
[#](#_CPPv4N33rocprofiler_buffer_tracing_kind_t48ROCPROFILER_BUFFER_TRACING_MARKER_CORE_RANGE_APIE) See also

rocprofiler_marker_core_range_api_id_t


-
enumerator ROCPROFILER_BUFFER_TRACING_LAST
[#](#_CPPv4N33rocprofiler_buffer_tracing_kind_t31ROCPROFILER_BUFFER_TRACING_LASTE)

-
enumerator ROCPROFILER_BUFFER_TRACING_HIP_RUNTIME_API_EXT

-
enumerator ROCPROFILER_BUFFER_TRACING_HIP_COMPILER_API_EXT

-
enumerator ROCPROFILER_BUFFER_TRACING_ROCDECODE_API_EXT

-
enumerator ROCPROFILER_BUFFER_TRACING_NONE

-
enum rocprofiler_code_object_operation_t
[#](#_CPPv435rocprofiler_code_object_operation_t) ROCProfiler Code Object Tracer Operations.

*Values:*-
enumerator ROCPROFILER_CODE_OBJECT_NONE
[#](#_CPPv4N35rocprofiler_code_object_operation_t28ROCPROFILER_CODE_OBJECT_NONEE) Unknown code object operation.


-
enumerator ROCPROFILER_CODE_OBJECT_LOAD
[#](#_CPPv4N35rocprofiler_code_object_operation_t28ROCPROFILER_CODE_OBJECT_LOADE) Code object containing kernel symbols.


-
enumerator ROCPROFILER_CODE_OBJECT_DEVICE_KERNEL_SYMBOL_REGISTER
[#](#_CPPv4N35rocprofiler_code_object_operation_t53ROCPROFILER_CODE_OBJECT_DEVICE_KERNEL_SYMBOL_REGISTERE) Kernel symbols - Device.


-
enumerator ROCPROFILER_CODE_OBJECT_HOST_KERNEL_SYMBOL_REGISTER
[#](#_CPPv4N35rocprofiler_code_object_operation_t51ROCPROFILER_CODE_OBJECT_HOST_KERNEL_SYMBOL_REGISTERE) Kernel symbols - Host.


-
enumerator ROCPROFILER_CODE_OBJECT_LAST
[#](#_CPPv4N35rocprofiler_code_object_operation_t28ROCPROFILER_CODE_OBJECT_LASTE)

-
enumerator ROCPROFILER_CODE_OBJECT_NONE

-
enum rocprofiler_hip_stream_operation_t
[#](#_CPPv434rocprofiler_hip_stream_operation_t) ROCProfiler HIP Stream Operations. These operations can be used to associate subsequent information with a HIP stream.

*Values:*-
enumerator ROCPROFILER_HIP_STREAM_NONE
[#](#_CPPv4N34rocprofiler_hip_stream_operation_t27ROCPROFILER_HIP_STREAM_NONEE) Unknown stream handle operation.


-
enumerator ROCPROFILER_HIP_STREAM_CREATE
[#](#_CPPv4N34rocprofiler_hip_stream_operation_t29ROCPROFILER_HIP_STREAM_CREATEE) A stream handle is created.


-
enumerator ROCPROFILER_HIP_STREAM_DESTROY
[#](#_CPPv4N34rocprofiler_hip_stream_operation_t30ROCPROFILER_HIP_STREAM_DESTROYE) A stream handle is destroyed.


-
enumerator ROCPROFILER_HIP_STREAM_SET
[#](#_CPPv4N34rocprofiler_hip_stream_operation_t26ROCPROFILER_HIP_STREAM_SETE)

-
enumerator ROCPROFILER_HIP_STREAM_LAST
[#](#_CPPv4N34rocprofiler_hip_stream_operation_t27ROCPROFILER_HIP_STREAM_LASTE)

-
enumerator ROCPROFILER_HIP_STREAM_SET

-
enumerator ROCPROFILER_HIP_STREAM_NONE

-
enum rocprofiler_memory_copy_operation_t
[#](#_CPPv435rocprofiler_memory_copy_operation_t) Memory Copy Operations.

*Values:*-
enumerator ROCPROFILER_MEMORY_COPY_NONE
[#](#_CPPv4N35rocprofiler_memory_copy_operation_t28ROCPROFILER_MEMORY_COPY_NONEE) Unknown memory copy direction.


-
enumerator ROCPROFILER_MEMORY_COPY_HOST_TO_HOST
[#](#_CPPv4N35rocprofiler_memory_copy_operation_t36ROCPROFILER_MEMORY_COPY_HOST_TO_HOSTE) Memory copy from host to host.


-
enumerator ROCPROFILER_MEMORY_COPY_HOST_TO_DEVICE
[#](#_CPPv4N35rocprofiler_memory_copy_operation_t38ROCPROFILER_MEMORY_COPY_HOST_TO_DEVICEE) Memory copy from host to device.


-
enumerator ROCPROFILER_MEMORY_COPY_DEVICE_TO_HOST
[#](#_CPPv4N35rocprofiler_memory_copy_operation_t38ROCPROFILER_MEMORY_COPY_DEVICE_TO_HOSTE) Memory copy from device to host.


-
enumerator ROCPROFILER_MEMORY_COPY_DEVICE_TO_DEVICE
[#](#_CPPv4N35rocprofiler_memory_copy_operation_t40ROCPROFILER_MEMORY_COPY_DEVICE_TO_DEVICEE) Memory copy from device to device.


-
enumerator ROCPROFILER_MEMORY_COPY_LAST
[#](#_CPPv4N35rocprofiler_memory_copy_operation_t28ROCPROFILER_MEMORY_COPY_LASTE)

-
enumerator ROCPROFILER_MEMORY_COPY_NONE

-
enum rocprofiler_memory_allocation_operation_t
[#](#_CPPv441rocprofiler_memory_allocation_operation_t) Memory Allocation Operation.

*Values:*-
enumerator ROCPROFILER_MEMORY_ALLOCATION_NONE
[#](#_CPPv4N41rocprofiler_memory_allocation_operation_t34ROCPROFILER_MEMORY_ALLOCATION_NONEE) Unknown memory allocation function.


-
enumerator ROCPROFILER_MEMORY_ALLOCATION_ALLOCATE
[#](#_CPPv4N41rocprofiler_memory_allocation_operation_t38ROCPROFILER_MEMORY_ALLOCATION_ALLOCATEE) Allocate memory function.


-
enumerator ROCPROFILER_MEMORY_ALLOCATION_VMEM_ALLOCATE
[#](#_CPPv4N41rocprofiler_memory_allocation_operation_t43ROCPROFILER_MEMORY_ALLOCATION_VMEM_ALLOCATEE) Allocate vmem memory handle.


-
enumerator ROCPROFILER_MEMORY_ALLOCATION_FREE
[#](#_CPPv4N41rocprofiler_memory_allocation_operation_t34ROCPROFILER_MEMORY_ALLOCATION_FREEE) Free memory function.


-
enumerator ROCPROFILER_MEMORY_ALLOCATION_VMEM_FREE
[#](#_CPPv4N41rocprofiler_memory_allocation_operation_t39ROCPROFILER_MEMORY_ALLOCATION_VMEM_FREEE) Release vmem memory handle.


-
enumerator ROCPROFILER_MEMORY_ALLOCATION_LAST
[#](#_CPPv4N41rocprofiler_memory_allocation_operation_t34ROCPROFILER_MEMORY_ALLOCATION_LASTE)

-
enumerator ROCPROFILER_MEMORY_ALLOCATION_NONE

-
enum rocprofiler_kernel_dispatch_operation_t
[#](#_CPPv439rocprofiler_kernel_dispatch_operation_t) ROCProfiler Kernel Dispatch Tracing Operation Types.

*Values:*-
enumerator ROCPROFILER_KERNEL_DISPATCH_NONE
[#](#_CPPv4N39rocprofiler_kernel_dispatch_operation_t32ROCPROFILER_KERNEL_DISPATCH_NONEE) Unknown kernel dispatch operation.


-
enumerator ROCPROFILER_KERNEL_DISPATCH_ENQUEUE
[#](#_CPPv4N39rocprofiler_kernel_dispatch_operation_t35ROCPROFILER_KERNEL_DISPATCH_ENQUEUEE)

-
enumerator ROCPROFILER_KERNEL_DISPATCH_COMPLETE
[#](#_CPPv4N39rocprofiler_kernel_dispatch_operation_t36ROCPROFILER_KERNEL_DISPATCH_COMPLETEE)

-
enumerator ROCPROFILER_KERNEL_DISPATCH_LAST
[#](#_CPPv4N39rocprofiler_kernel_dispatch_operation_t32ROCPROFILER_KERNEL_DISPATCH_LASTE)

-
enumerator ROCPROFILER_KERNEL_DISPATCH_ENQUEUE

-
enumerator ROCPROFILER_KERNEL_DISPATCH_COMPLETE

-
enumerator ROCPROFILER_KERNEL_DISPATCH_NONE

-
enum rocprofiler_pc_sampling_method_t
[#](#_CPPv432rocprofiler_pc_sampling_method_t) PC Sampling Method.

*Values:*-
enumerator ROCPROFILER_PC_SAMPLING_METHOD_NONE
[#](#_CPPv4N32rocprofiler_pc_sampling_method_t35ROCPROFILER_PC_SAMPLING_METHOD_NONEE) Unknown sampling type.


-
enumerator ROCPROFILER_PC_SAMPLING_METHOD_STOCHASTIC
[#](#_CPPv4N32rocprofiler_pc_sampling_method_t41ROCPROFILER_PC_SAMPLING_METHOD_STOCHASTICE) Stochastic sampling (MI300+)


-
enumerator ROCPROFILER_PC_SAMPLING_METHOD_HOST_TRAP
[#](#_CPPv4N32rocprofiler_pc_sampling_method_t40ROCPROFILER_PC_SAMPLING_METHOD_HOST_TRAPE) Interval sampling (MI200+)


-
enumerator ROCPROFILER_PC_SAMPLING_METHOD_LAST
[#](#_CPPv4N32rocprofiler_pc_sampling_method_t35ROCPROFILER_PC_SAMPLING_METHOD_LASTE)

-
enumerator ROCPROFILER_PC_SAMPLING_METHOD_NONE

-
enum rocprofiler_pc_sampling_unit_t
[#](#_CPPv430rocprofiler_pc_sampling_unit_t) PC Sampling Unit.

*Values:*-
enumerator ROCPROFILER_PC_SAMPLING_UNIT_NONE
[#](#_CPPv4N30rocprofiler_pc_sampling_unit_t33ROCPROFILER_PC_SAMPLING_UNIT_NONEE) Sample interval has unspecified units.


-
enumerator ROCPROFILER_PC_SAMPLING_UNIT_INSTRUCTIONS
[#](#_CPPv4N30rocprofiler_pc_sampling_unit_t41ROCPROFILER_PC_SAMPLING_UNIT_INSTRUCTIONSE) Sample interval is in instructions.


-
enumerator ROCPROFILER_PC_SAMPLING_UNIT_CYCLES
[#](#_CPPv4N30rocprofiler_pc_sampling_unit_t35ROCPROFILER_PC_SAMPLING_UNIT_CYCLESE) Sample interval is in cycles.


-
enumerator ROCPROFILER_PC_SAMPLING_UNIT_TIME
[#](#_CPPv4N30rocprofiler_pc_sampling_unit_t33ROCPROFILER_PC_SAMPLING_UNIT_TIMEE) Sample internval is in nanoseconds.


-
enumerator ROCPROFILER_PC_SAMPLING_UNIT_LAST
[#](#_CPPv4N30rocprofiler_pc_sampling_unit_t33ROCPROFILER_PC_SAMPLING_UNIT_LASTE)

-
enumerator ROCPROFILER_PC_SAMPLING_UNIT_NONE

-
enum rocprofiler_buffer_policy_t
[#](#_CPPv427rocprofiler_buffer_policy_t) Actions when Buffer is full.

*Values:*-
enumerator ROCPROFILER_BUFFER_POLICY_NONE
[#](#_CPPv4N27rocprofiler_buffer_policy_t30ROCPROFILER_BUFFER_POLICY_NONEE) No policy has been set.


-
enumerator ROCPROFILER_BUFFER_POLICY_DISCARD
[#](#_CPPv4N27rocprofiler_buffer_policy_t33ROCPROFILER_BUFFER_POLICY_DISCARDE) Drop records when buffer is full.


-
enumerator ROCPROFILER_BUFFER_POLICY_LOSSLESS
[#](#_CPPv4N27rocprofiler_buffer_policy_t34ROCPROFILER_BUFFER_POLICY_LOSSLESSE) Block when buffer is full.


-
enumerator ROCPROFILER_BUFFER_POLICY_LAST
[#](#_CPPv4N27rocprofiler_buffer_policy_t30ROCPROFILER_BUFFER_POLICY_LASTE)

-
enumerator ROCPROFILER_BUFFER_POLICY_NONE

-
enum rocprofiler_scratch_memory_operation_t
[#](#_CPPv438rocprofiler_scratch_memory_operation_t) Scratch event kind.

*Values:*-
enumerator ROCPROFILER_SCRATCH_MEMORY_NONE
[#](#_CPPv4N38rocprofiler_scratch_memory_operation_t31ROCPROFILER_SCRATCH_MEMORY_NONEE) Unknown scratch operation.


-
enumerator ROCPROFILER_SCRATCH_MEMORY_ALLOC
[#](#_CPPv4N38rocprofiler_scratch_memory_operation_t32ROCPROFILER_SCRATCH_MEMORY_ALLOCE) Scratch memory allocation event.


-
enumerator ROCPROFILER_SCRATCH_MEMORY_FREE
[#](#_CPPv4N38rocprofiler_scratch_memory_operation_t31ROCPROFILER_SCRATCH_MEMORY_FREEE) Scratch memory free event.


-
enumerator ROCPROFILER_SCRATCH_MEMORY_ASYNC_RECLAIM
[#](#_CPPv4N38rocprofiler_scratch_memory_operation_t40ROCPROFILER_SCRATCH_MEMORY_ASYNC_RECLAIME) Scratch memory asynchronously reclaimed.


-
enumerator ROCPROFILER_SCRATCH_MEMORY_LAST
[#](#_CPPv4N38rocprofiler_scratch_memory_operation_t31ROCPROFILER_SCRATCH_MEMORY_LASTE)

-
enumerator ROCPROFILER_SCRATCH_MEMORY_NONE

-
enum rocprofiler_runtime_library_t
[#](#_CPPv429rocprofiler_runtime_library_t) Enumeration for specifying runtime libraries supported by rocprofiler. This enumeration is used for thread creation callbacks.

See also

Internal Thread Handling.

*Values:*-
enumerator ROCPROFILER_LIBRARY
[#](#_CPPv4N29rocprofiler_runtime_library_t19ROCPROFILER_LIBRARYE)

-
enumerator ROCPROFILER_HSA_LIBRARY
[#](#_CPPv4N29rocprofiler_runtime_library_t23ROCPROFILER_HSA_LIBRARYE)

-
enumerator ROCPROFILER_HIP_LIBRARY
[#](#_CPPv4N29rocprofiler_runtime_library_t23ROCPROFILER_HIP_LIBRARYE)

-
enumerator ROCPROFILER_MARKER_LIBRARY
[#](#_CPPv4N29rocprofiler_runtime_library_t26ROCPROFILER_MARKER_LIBRARYE)

-
enumerator ROCPROFILER_RCCL_LIBRARY
[#](#_CPPv4N29rocprofiler_runtime_library_t24ROCPROFILER_RCCL_LIBRARYE)

-
enumerator ROCPROFILER_ROCDECODE_LIBRARY
[#](#_CPPv4N29rocprofiler_runtime_library_t29ROCPROFILER_ROCDECODE_LIBRARYE)

-
enumerator ROCPROFILER_ROCJPEG_LIBRARY
[#](#_CPPv4N29rocprofiler_runtime_library_t27ROCPROFILER_ROCJPEG_LIBRARYE)

-
enumerator ROCPROFILER_LIBRARY_LAST
[#](#_CPPv4N29rocprofiler_runtime_library_t24ROCPROFILER_LIBRARY_LASTE)

-
enumerator ROCPROFILER_LIBRARY

-
enum rocprofiler_intercept_table_t
[#](#_CPPv429rocprofiler_intercept_table_t) Enumeration for specifying intercept tables supported by rocprofiler. This enumeration is used for intercept tables.

See also

Intercept table for runtime libraries.

*Values:*-
enumerator ROCPROFILER_HSA_TABLE
[#](#_CPPv4N29rocprofiler_intercept_table_t21ROCPROFILER_HSA_TABLEE)

-
enumerator ROCPROFILER_HIP_RUNTIME_TABLE
[#](#_CPPv4N29rocprofiler_intercept_table_t29ROCPROFILER_HIP_RUNTIME_TABLEE)

-
enumerator ROCPROFILER_HIP_COMPILER_TABLE
[#](#_CPPv4N29rocprofiler_intercept_table_t30ROCPROFILER_HIP_COMPILER_TABLEE)

-
enumerator ROCPROFILER_MARKER_CORE_TABLE
[#](#_CPPv4N29rocprofiler_intercept_table_t29ROCPROFILER_MARKER_CORE_TABLEE)

-
enumerator ROCPROFILER_MARKER_CONTROL_TABLE
[#](#_CPPv4N29rocprofiler_intercept_table_t32ROCPROFILER_MARKER_CONTROL_TABLEE)

-
enumerator ROCPROFILER_MARKER_NAME_TABLE
[#](#_CPPv4N29rocprofiler_intercept_table_t29ROCPROFILER_MARKER_NAME_TABLEE)

-
enumerator ROCPROFILER_RCCL_TABLE
[#](#_CPPv4N29rocprofiler_intercept_table_t22ROCPROFILER_RCCL_TABLEE)

-
enumerator ROCPROFILER_ROCDECODE_TABLE
[#](#_CPPv4N29rocprofiler_intercept_table_t27ROCPROFILER_ROCDECODE_TABLEE)

-
enumerator ROCPROFILER_ROCJPEG_TABLE
[#](#_CPPv4N29rocprofiler_intercept_table_t25ROCPROFILER_ROCJPEG_TABLEE)

-
enumerator ROCPROFILER_TABLE_LAST
[#](#_CPPv4N29rocprofiler_intercept_table_t22ROCPROFILER_TABLE_LASTE)

-
enumerator ROCPROFILER_HSA_TABLE

-
enum rocprofiler_runtime_initialization_operation_t
[#](#_CPPv446rocprofiler_runtime_initialization_operation_t) ROCProfiler Runtime Initialization Tracer Operations.

*Values:*-
enumerator ROCPROFILER_RUNTIME_INITIALIZATION_NONE
[#](#_CPPv4N46rocprofiler_runtime_initialization_operation_t39ROCPROFILER_RUNTIME_INITIALIZATION_NONEE) Unknown runtime initialization.


-
enumerator ROCPROFILER_RUNTIME_INITIALIZATION_HSA
[#](#_CPPv4N46rocprofiler_runtime_initialization_operation_t38ROCPROFILER_RUNTIME_INITIALIZATION_HSAE) Application loaded HSA runtime.


-
enumerator ROCPROFILER_RUNTIME_INITIALIZATION_HIP
[#](#_CPPv4N46rocprofiler_runtime_initialization_operation_t38ROCPROFILER_RUNTIME_INITIALIZATION_HIPE) Application loaded HIP runtime.


-
enumerator ROCPROFILER_RUNTIME_INITIALIZATION_MARKER
[#](#_CPPv4N46rocprofiler_runtime_initialization_operation_t41ROCPROFILER_RUNTIME_INITIALIZATION_MARKERE) Application loaded Marker (ROCTx) runtime.


-
enumerator ROCPROFILER_RUNTIME_INITIALIZATION_RCCL
[#](#_CPPv4N46rocprofiler_runtime_initialization_operation_t39ROCPROFILER_RUNTIME_INITIALIZATION_RCCLE) Application loaded RCCL runtime.


-
enumerator ROCPROFILER_RUNTIME_INITIALIZATION_ROCDECODE
[#](#_CPPv4N46rocprofiler_runtime_initialization_operation_t44ROCPROFILER_RUNTIME_INITIALIZATION_ROCDECODEE) Application loaded rocDecoder runtime.


-
enumerator ROCPROFILER_RUNTIME_INITIALIZATION_ROCJPEG
[#](#_CPPv4N46rocprofiler_runtime_initialization_operation_t42ROCPROFILER_RUNTIME_INITIALIZATION_ROCJPEGE) Application loaded rocJPEG runtime.


-
enumerator ROCPROFILER_RUNTIME_INITIALIZATION_LAST
[#](#_CPPv4N46rocprofiler_runtime_initialization_operation_t39ROCPROFILER_RUNTIME_INITIALIZATION_LASTE)

-
enumerator ROCPROFILER_RUNTIME_INITIALIZATION_NONE

-
enum rocprofiler_counter_info_version_id_t
[#](#_CPPv437rocprofiler_counter_info_version_id_t) Enumeration for specifying the counter info struct version you want.

*Values:*-
enumerator ROCPROFILER_COUNTER_INFO_VERSION_NONE
[#](#_CPPv4N37rocprofiler_counter_info_version_id_t37ROCPROFILER_COUNTER_INFO_VERSION_NONEE)

-
enumerator ROCPROFILER_COUNTER_INFO_VERSION_0
[#](#_CPPv4N37rocprofiler_counter_info_version_id_t34ROCPROFILER_COUNTER_INFO_VERSION_0E)

-
enumerator ROCPROFILER_COUNTER_INFO_VERSION_1
[#](#_CPPv4N37rocprofiler_counter_info_version_id_t34ROCPROFILER_COUNTER_INFO_VERSION_1E)

-
enumerator ROCPROFILER_COUNTER_INFO_VERSION_LAST
[#](#_CPPv4N37rocprofiler_counter_info_version_id_t37ROCPROFILER_COUNTER_INFO_VERSION_LASTE)

-
enumerator ROCPROFILER_COUNTER_INFO_VERSION_NONE

-
enum rocprofiler_counter_record_kind_t
[#](#_CPPv433rocprofiler_counter_record_kind_t) Enumeration for distinguishing different buffer record kinds within the ROCPROFILER_BUFFER_CATEGORY_COUNTERS category.

*Values:*-
enumerator ROCPROFILER_COUNTER_RECORD_NONE
[#](#_CPPv4N33rocprofiler_counter_record_kind_t31ROCPROFILER_COUNTER_RECORD_NONEE)

-
enumerator ROCPROFILER_COUNTER_RECORD_PROFILE_COUNTING_DISPATCH_HEADER
[#](#_CPPv4N33rocprofiler_counter_record_kind_t59ROCPROFILER_COUNTER_RECORD_PROFILE_COUNTING_DISPATCH_HEADERE)

-
enumerator ROCPROFILER_COUNTER_RECORD_VALUE
[#](#_CPPv4N33rocprofiler_counter_record_kind_t32ROCPROFILER_COUNTER_RECORD_VALUEE)

-
enumerator ROCPROFILER_COUNTER_RECORD_LAST
[#](#_CPPv4N33rocprofiler_counter_record_kind_t31ROCPROFILER_COUNTER_RECORD_LASTE)

-
enumerator ROCPROFILER_COUNTER_RECORD_NONE

-
enum rocprofiler_counter_flag_t
[#](#_CPPv426rocprofiler_counter_flag_t) Enumeration of flags that can be used with some counter api calls.

*Values:*-
enumerator ROCPROFILER_COUNTER_FLAG_NONE
[#](#_CPPv4N26rocprofiler_counter_flag_t29ROCPROFILER_COUNTER_FLAG_NONEE)

-
enumerator ROCPROFILER_COUNTER_FLAG_ASYNC
[#](#_CPPv4N26rocprofiler_counter_flag_t30ROCPROFILER_COUNTER_FLAG_ASYNCE) Do not wait for completion before returning.


-
enumerator ROCPROFILER_COUNTER_FLAG_APPEND_DEFINITION
[#](#_CPPv4N26rocprofiler_counter_flag_t42ROCPROFILER_COUNTER_FLAG_APPEND_DEFINITIONE) Append the counter definition to the system provided counter definition file.


-
enumerator ROCPROFILER_COUNTER_FLAG_LAST
[#](#_CPPv4N26rocprofiler_counter_flag_t29ROCPROFILER_COUNTER_FLAG_LASTE)

-
enumerator ROCPROFILER_COUNTER_FLAG_NONE

-
enum rocprofiler_pc_sampling_record_kind_t
[#](#_CPPv437rocprofiler_pc_sampling_record_kind_t) Enumeration for distinguishing different buffer record kinds within the ROCPROFILER_BUFFER_CATEGORY_PC_SAMPLING category.

*Values:*-
enumerator ROCPROFILER_PC_SAMPLING_RECORD_NONE
[#](#_CPPv4N37rocprofiler_pc_sampling_record_kind_t35ROCPROFILER_PC_SAMPLING_RECORD_NONEE)

-
enumerator ROCPROFILER_PC_SAMPLING_RECORD_INVALID_SAMPLE
[#](#_CPPv4N37rocprofiler_pc_sampling_record_kind_t45ROCPROFILER_PC_SAMPLING_RECORD_INVALID_SAMPLEE)

-
enumerator ROCPROFILER_PC_SAMPLING_RECORD_HOST_TRAP_V0_SAMPLE
[#](#_CPPv4N37rocprofiler_pc_sampling_record_kind_t50ROCPROFILER_PC_SAMPLING_RECORD_HOST_TRAP_V0_SAMPLEE)

-
enumerator ROCPROFILER_PC_SAMPLING_RECORD_STOCHASTIC_V0_SAMPLE
[#](#_CPPv4N37rocprofiler_pc_sampling_record_kind_t51ROCPROFILER_PC_SAMPLING_RECORD_STOCHASTIC_V0_SAMPLEE)

-
enumerator ROCPROFILER_PC_SAMPLING_RECORD_LAST
[#](#_CPPv4N37rocprofiler_pc_sampling_record_kind_t35ROCPROFILER_PC_SAMPLING_RECORD_LASTE)

-
enumerator ROCPROFILER_PC_SAMPLING_RECORD_NONE

-
typedef uint64_t rocprofiler_timestamp_t
[#](#_CPPv423rocprofiler_timestamp_t) ROCProfiler Timestamp.


-
typedef uint64_t rocprofiler_thread_id_t
[#](#_CPPv423rocprofiler_thread_id_t) Thread ID. Value will be equivalent to

`syscall(__NR_gettid)`


-
typedef int32_t rocprofiler_tracing_operation_t
[#](#_CPPv431rocprofiler_tracing_operation_t) Tracing Operation ID. Depending on the kind, operations can be determined. If the value is equal to zero that means all operations will be considered for tracing. Detailed API tracing operations can be found at associated header file for that partiular operation. i.e: For ROCProfiler enumeration of HSA AMD Extended API tracing operations, look at source/include/rocprofiler-sdk/hsa/amd_ext_api_id.h.


-
typedef uint64_t rocprofiler_kernel_id_t
[#](#_CPPv423rocprofiler_kernel_id_t) Kernel identifier type.


-
typedef uint64_t rocprofiler_dispatch_id_t
[#](#_CPPv425rocprofiler_dispatch_id_t)

-
typedef uint64_t rocprofiler_counter_instance_id_t
[#](#_CPPv433rocprofiler_counter_instance_id_t) Unique record id encoding both the counter and dimensional values (positions) for the record.


-
typedef uint64_t rocprofiler_counter_dimension_id_t
[#](#_CPPv434rocprofiler_counter_dimension_id_t) A dimension for counter instances. Some example dimensions include XCC, SM (Shader), etc. This value represents the dimension beind described or queried about.


-
typedef
[rocprofiler_counter_record_dimension_info_t](#_CPPv443rocprofiler_counter_record_dimension_info_t)rocprofiler_record_dimension_info_t[#](#_CPPv435rocprofiler_record_dimension_info_t)

-
typedef
[rocprofiler_counter_record_t](#_CPPv428rocprofiler_counter_record_t)rocprofiler_record_counter_t[#](#_CPPv428rocprofiler_record_counter_t)

-
static inline uint64_t rocprofiler_record_header_compute_hash(uint32_t category, uint32_t kind)
[#](#_CPPv438rocprofiler_record_header_compute_hash8uint32_t8uint32_t) Function for computing the unsigned 64-bit hash value in

[rocprofiler_record_header_t](#structrocprofiler__record__header__t)from a category and kind (two unsigned 32-bit values)- Parameters:
**category**–**[in]**a value from[rocprofiler_buffer_category_t](#group___b_a_s_i_c___d_a_t_a___t_y_p_e_s_1gadeb6435740d95a66dfc2485349b77a69)**kind**–**[in]**depending on the category, this is the domain value, e.g.,[rocprofiler_buffer_tracing_kind_t](#group___b_a_s_i_c___d_a_t_a___t_y_p_e_s_1gac2eecbf4d5542df3b35fc26837fac59b)value

- Returns:
uint64_t hash value of category and kind



-
ROCPROFILER_CORRELATION_ID_INTERNAL_NONE
[#](#c.ROCPROFILER_CORRELATION_ID_INTERNAL_NONE) The NULL value of an internal correlation ID.


-
ROCPROFILER_CORRELATION_ID_ANCESTOR_NONE
[#](#c.ROCPROFILER_CORRELATION_ID_ANCESTOR_NONE) The NULL value of an ancestor correlation ID.


-
union rocprofiler_user_data_t
[#](#_CPPv423rocprofiler_user_data_t) *#include <rocprofiler-sdk/fwd.h>*User-assignable data type.


-
union rocprofiler_address_t
[#](#_CPPv421rocprofiler_address_t) *#include <rocprofiler-sdk/fwd.h>*Stores memory address for profiling.


-
struct rocprofiler_uuid_t
[#](#_CPPv418rocprofiler_uuid_t) *#include <rocprofiler-sdk/fwd.h>*Stores UUID for devices.


-
struct rocprofiler_version_triplet_t
[#](#_CPPv429rocprofiler_version_triplet_t) *#include <rocprofiler-sdk/fwd.h>*Versioning info.


-
struct rocprofiler_context_id_t
[#](#_CPPv424rocprofiler_context_id_t) *#include <rocprofiler-sdk/fwd.h>*Context ID.


-
struct rocprofiler_queue_id_t
[#](#_CPPv422rocprofiler_queue_id_t) *#include <rocprofiler-sdk/fwd.h>*Queue ID.


-
struct rocprofiler_stream_id_t
[#](#_CPPv423rocprofiler_stream_id_t) *#include <rocprofiler-sdk/fwd.h>*Stream ID.


-
struct rocprofiler_correlation_id_t
[#](#_CPPv428rocprofiler_correlation_id_t) *#include <rocprofiler-sdk/fwd.h>*ROCProfiler Record Correlation ID.


-
struct rocprofiler_async_correlation_id_t
[#](#_CPPv434rocprofiler_async_correlation_id_t) *#include <rocprofiler-sdk/fwd.h>*ROCProfiler Correlation ID record for async activity.


-
struct rocprofiler_buffer_id_t
[#](#_CPPv423rocprofiler_buffer_id_t) *#include <rocprofiler-sdk/fwd.h>*Buffer ID.


-
struct rocprofiler_agent_id_t
[#](#_CPPv422rocprofiler_agent_id_t) *#include <rocprofiler-sdk/fwd.h>*Agent Identifier.


-
struct rocprofiler_counter_id_t
[#](#_CPPv424rocprofiler_counter_id_t) *#include <rocprofiler-sdk/fwd.h>*Counter ID.


-
struct rocprofiler_counter_config_id_t
[#](#_CPPv431rocprofiler_counter_config_id_t) *#include <rocprofiler-sdk/fwd.h>*Profile Configurations.


-
struct rocprofiler_dim3_t
[#](#_CPPv418rocprofiler_dim3_t) *#include <rocprofiler-sdk/fwd.h>*Multi-dimensional struct of data used to describe GPU workgroup and grid sizes.


-
struct rocprofiler_callback_tracing_record_t
[#](#_CPPv437rocprofiler_callback_tracing_record_t) *#include <rocprofiler-sdk/fwd.h>*Tracing record.


-
struct rocprofiler_record_header_t
[#](#_CPPv427rocprofiler_record_header_t) *#include <rocprofiler-sdk/fwd.h>*Generic record with type identifier(s) and a pointer to data. This data type is used with buffered data.

void tool_tracing_callback(rocprofiler_record_header_t** headers, size_t num_headers) { for(size_t i = 0; i < num_headers; ++i) { rocprofiler_record_header_t* header = headers[i]; if(header->category == ROCPROFILER_BUFFER_CATEGORY_TRACING && header->kind == ROCPROFILER_BUFFER_TRACING_HSA_API) { // cast to rocprofiler_buffer_tracing_hsa_api_record_t which // is type associated with this category + kind auto* record = static_cast<rocprofiler_buffer_tracing_hsa_api_record_t*>(header->payload); // trivial test assert(record->start_timestamp <= record->end_timestamp); } } }


-
struct rocprofiler_kernel_dispatch_info_t
[#](#_CPPv434rocprofiler_kernel_dispatch_info_t) *#include <rocprofiler-sdk/fwd.h>*ROCProfiler kernel dispatch information.


-
struct rocprofiler_counter_record_dimension_info_t
[#](#_CPPv443rocprofiler_counter_record_dimension_info_t) *#include <rocprofiler-sdk/fwd.h>*(experimental) Details for the dimension, including its size, for a counter record.


-
struct rocprofiler_counter_record_t
[#](#_CPPv428rocprofiler_counter_record_t) *#include <rocprofiler-sdk/fwd.h>*(experimental) ROCProfiler Profile Counting Counter Record per instance.


- rocprofiler_record_header_t.__unnamed58__

- rocprofiler_record_header_t.__unnamed58__.__unnamed63__
