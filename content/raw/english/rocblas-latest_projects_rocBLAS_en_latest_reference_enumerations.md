---
title: "rocBLAS enumeration &#8212; rocBLAS 5.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/enumerations.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:05:29.649617+00:00
content_hash: "c501c6505322c660"
---

# rocBLAS enumeration[#](#rocblas-enumeration)

Enumeration constants have numbering that is consistent with CBLAS, ACML, and most standard C BLAS libraries

## rocblas_operation[#](#rocblas-operation)

-
enum rocblas_operation
[#](#_CPPv417rocblas_operation) Used to specify whether the matrix is to be transposed or not.

Parameter constants. numbering is consistent with CBLAS, ACML and most standard C BLAS libraries

*Values:*-
enumerator rocblas_operation_none
[#](#_CPPv4N17rocblas_operation22rocblas_operation_noneE) Operate with the matrix.


-
enumerator rocblas_operation_transpose
[#](#_CPPv4N17rocblas_operation27rocblas_operation_transposeE) Operate with the transpose of the matrix.


-
enumerator rocblas_operation_conjugate_transpose
[#](#_CPPv4N17rocblas_operation37rocblas_operation_conjugate_transposeE) Operate with the conjugate transpose of the matrix.


-
enumerator rocblas_operation_none

## rocblas_fill[#](#rocblas-fill)

## rocblas_diagonal[#](#rocblas-diagonal)

## rocblas_side[#](#rocblas-side)

-
enum rocblas_side
[#](#_CPPv412rocblas_side) Indicates the side matrix A is located relative to matrix B during multiplication.

*Values:*-
enumerator rocblas_side_left
[#](#_CPPv4N12rocblas_side17rocblas_side_leftE) Multiply general matrix by symmetric, Hermitian, or triangular matrix on the left.


-
enumerator rocblas_side_right
[#](#_CPPv4N12rocblas_side18rocblas_side_rightE) Multiply general matrix by symmetric, Hermitian, or triangular matrix on the right.


-
enumerator rocblas_side_both
[#](#_CPPv4N12rocblas_side17rocblas_side_bothE)

-
enumerator rocblas_side_left

## rocblas_status[#](#rocblas-status)

-
enum rocblas_status
[#](#_CPPv414rocblas_status) rocblas status codes definition

*Values:*-
enumerator rocblas_status_success
[#](#_CPPv4N14rocblas_status22rocblas_status_successE) Success


-
enumerator rocblas_status_invalid_handle
[#](#_CPPv4N14rocblas_status29rocblas_status_invalid_handleE) Handle not initialized, invalid or null


-
enumerator rocblas_status_not_implemented
[#](#_CPPv4N14rocblas_status30rocblas_status_not_implementedE) Function is not implemented


-
enumerator rocblas_status_invalid_pointer
[#](#_CPPv4N14rocblas_status30rocblas_status_invalid_pointerE) Invalid pointer argument


-
enumerator rocblas_status_invalid_size
[#](#_CPPv4N14rocblas_status27rocblas_status_invalid_sizeE) Invalid size argument


-
enumerator rocblas_status_memory_error
[#](#_CPPv4N14rocblas_status27rocblas_status_memory_errorE) Failed internal memory allocation, copy or dealloc


-
enumerator rocblas_status_internal_error
[#](#_CPPv4N14rocblas_status29rocblas_status_internal_errorE) Other internal library failure


-
enumerator rocblas_status_perf_degraded
[#](#_CPPv4N14rocblas_status28rocblas_status_perf_degradedE) Performance degraded due to low device memory


-
enumerator rocblas_status_size_query_mismatch
[#](#_CPPv4N14rocblas_status34rocblas_status_size_query_mismatchE) Unmatched start/stop size query


-
enumerator rocblas_status_size_increased
[#](#_CPPv4N14rocblas_status29rocblas_status_size_increasedE) Queried device memory size increased


-
enumerator rocblas_status_size_unchanged
[#](#_CPPv4N14rocblas_status29rocblas_status_size_unchangedE) Queried device memory size unchanged


-
enumerator rocblas_status_invalid_value
[#](#_CPPv4N14rocblas_status28rocblas_status_invalid_valueE) Passed argument not valid


-
enumerator rocblas_status_continue
[#](#_CPPv4N14rocblas_status23rocblas_status_continueE) Nothing preventing function to proceed


-
enumerator rocblas_status_check_numerics_fail
[#](#_CPPv4N14rocblas_status34rocblas_status_check_numerics_failE) Will be set if the vector/matrix has a NaN/Infinity/denormal value


-
enumerator rocblas_status_excluded_from_build
[#](#_CPPv4N14rocblas_status34rocblas_status_excluded_from_buildE) Function is not available in build, likely a function requiring Tensile built without Tensile


-
enumerator rocblas_status_arch_mismatch
[#](#_CPPv4N14rocblas_status28rocblas_status_arch_mismatchE) The function requires a feature absent from the device architecture


-
enumerator rocblas_status_success

## rocblas_datatype[#](#rocblas-datatype)

-
enum rocblas_datatype
[#](#_CPPv416rocblas_datatype) Indicates the precision width of data stored in a blas type.

Parameter constants. Numbering continues into next free decimal range but not shared with other BLAS libraries

*Values:*-
enumerator rocblas_datatype_f16_r
[#](#_CPPv4N16rocblas_datatype22rocblas_datatype_f16_rE) 16-bit floating point, real


-
enumerator rocblas_datatype_f32_r
[#](#_CPPv4N16rocblas_datatype22rocblas_datatype_f32_rE) 32-bit floating point, real


-
enumerator rocblas_datatype_f64_r
[#](#_CPPv4N16rocblas_datatype22rocblas_datatype_f64_rE) 64-bit floating point, real


-
enumerator rocblas_datatype_f16_c
[#](#_CPPv4N16rocblas_datatype22rocblas_datatype_f16_cE) 16-bit floating point, complex


-
enumerator rocblas_datatype_f32_c
[#](#_CPPv4N16rocblas_datatype22rocblas_datatype_f32_cE) 32-bit floating point, complex


-
enumerator rocblas_datatype_f64_c
[#](#_CPPv4N16rocblas_datatype22rocblas_datatype_f64_cE) 64-bit floating point, complex


-
enumerator rocblas_datatype_i8_r
[#](#_CPPv4N16rocblas_datatype21rocblas_datatype_i8_rE) 8-bit signed integer, real


-
enumerator rocblas_datatype_u8_r
[#](#_CPPv4N16rocblas_datatype21rocblas_datatype_u8_rE) 8-bit unsigned integer, real


-
enumerator rocblas_datatype_i32_r
[#](#_CPPv4N16rocblas_datatype22rocblas_datatype_i32_rE) 32-bit signed integer, real


-
enumerator rocblas_datatype_u32_r
[#](#_CPPv4N16rocblas_datatype22rocblas_datatype_u32_rE) 32-bit unsigned integer, real


-
enumerator rocblas_datatype_i8_c
[#](#_CPPv4N16rocblas_datatype21rocblas_datatype_i8_cE) 8-bit signed integer, complex


-
enumerator rocblas_datatype_u8_c
[#](#_CPPv4N16rocblas_datatype21rocblas_datatype_u8_cE) 8-bit unsigned integer, complex


-
enumerator rocblas_datatype_i32_c
[#](#_CPPv4N16rocblas_datatype22rocblas_datatype_i32_cE) 32-bit signed integer, complex


-
enumerator rocblas_datatype_u32_c
[#](#_CPPv4N16rocblas_datatype22rocblas_datatype_u32_cE) 32-bit unsigned integer, complex


-
enumerator rocblas_datatype_bf16_r
[#](#_CPPv4N16rocblas_datatype23rocblas_datatype_bf16_rE) 16-bit bfloat, real


-
enumerator rocblas_datatype_bf16_c
[#](#_CPPv4N16rocblas_datatype23rocblas_datatype_bf16_cE) 16-bit bfloat, complex


-
enumerator rocblas_datatype_invalid
[#](#_CPPv4N16rocblas_datatype24rocblas_datatype_invalidE) Invalid datatype value, do not use


-
enumerator rocblas_datatype_f16_r

## rocblas_pointer_mode[#](#rocblas-pointer-mode)

-
enum rocblas_pointer_mode
[#](#_CPPv420rocblas_pointer_mode) Indicates if scalar pointers are on host or device. This is used for scalars alpha and beta and for scalar function return values.

*Values:*-
enumerator rocblas_pointer_mode_host
[#](#_CPPv4N20rocblas_pointer_mode25rocblas_pointer_mode_hostE) Scalar values affected by this variable are located on the host.


-
enumerator rocblas_pointer_mode_device
[#](#_CPPv4N20rocblas_pointer_mode27rocblas_pointer_mode_deviceE) Scalar values affected by this variable are located on the device.


-
enumerator rocblas_pointer_mode_host

## rocblas_atomics_mode[#](#rocblas-atomics-mode)

-
enum rocblas_atomics_mode
[#](#_CPPv420rocblas_atomics_mode) Indicates if atomics operations are allowed. Not allowing atomic operations may generally improve determinism and repeatability of results at a cost of performance. Defaults to rocblas_atomics_allowed.

*Values:*-
enumerator rocblas_atomics_not_allowed
[#](#_CPPv4N20rocblas_atomics_mode27rocblas_atomics_not_allowedE) Algorithms will refrain from atomics where applicable.


-
enumerator rocblas_atomics_allowed
[#](#_CPPv4N20rocblas_atomics_mode23rocblas_atomics_allowedE) Algorithms will take advantage of atomics where applicable.


-
enumerator rocblas_atomics_not_allowed

## rocblas_layer_mode[#](#rocblas-layer-mode)

-
enum rocblas_layer_mode
[#](#_CPPv418rocblas_layer_mode) Indicates if layer is active with bitmask.

*Values:*-
enumerator rocblas_layer_mode_none
[#](#_CPPv4N18rocblas_layer_mode23rocblas_layer_mode_noneE) No logging will take place.


-
enumerator rocblas_layer_mode_log_trace
[#](#_CPPv4N18rocblas_layer_mode28rocblas_layer_mode_log_traceE) A line containing the function name and value of arguments passed will be printed with each rocBLAS function call.


-
enumerator rocblas_layer_mode_log_bench
[#](#_CPPv4N18rocblas_layer_mode28rocblas_layer_mode_log_benchE) Outputs a line each time a rocBLAS function is called, this line can be used with rocblas-bench to make the same call again.


-
enumerator rocblas_layer_mode_log_profile
[#](#_CPPv4N18rocblas_layer_mode30rocblas_layer_mode_log_profileE) Outputs a YAML description of each rocBLAS function called, along with its arguments and number of times it was called.


-
enumerator rocblas_layer_mode_log_internal
[#](#_CPPv4N18rocblas_layer_mode31rocblas_layer_mode_log_internalE) Outputs to the same stream as trace logging with limited internal API details like GEMM backend used.


-
enumerator rocblas_layer_mode_none

## rocblas_gemm_algo[#](#rocblas-gemm-algo)

## rocblas_gemm_flags[#](#rocblas-gemm-flags)

-
enum rocblas_gemm_flags
[#](#_CPPv418rocblas_gemm_flags) Control flags passed into gemm algorithms invoked by Tensile Host.

*Values:*-
enumerator rocblas_gemm_flags_none
[#](#_CPPv4N18rocblas_gemm_flags23rocblas_gemm_flags_noneE) Default empty flags.


-
enumerator rocblas_gemm_flags_use_cu_efficiency
[#](#_CPPv4N18rocblas_gemm_flags36rocblas_gemm_flags_use_cu_efficiencyE) Before ROCm 6.0 rocblas_gemm_flags_pack_int8x4 = 0x1, as has now been removed so is available for future use.

Select the gemm problem with the highest efficiency per compute unit used. Useful for running multiple smaller problems simultaneously. This takes precedence over the performance metric set in rocblas_handle and currently only works for gemm_*_ex problems.


-
enumerator rocblas_gemm_flags_fp16_alt_impl
[#](#_CPPv4N18rocblas_gemm_flags32rocblas_gemm_flags_fp16_alt_implE) Select an alternate implementation for the MI200 FP16 HPA (High Precision Accumulate) GEMM kernel utilizing the BF16 matrix instructions with reduced accuracy in cases where computation cannot tolerate the FP16 matrix instructions flushing subnormal FP16 input/output data to zero. See the “MI200 (gfx90a) Considerations” section for more details.


-
enumerator rocblas_gemm_flags_check_solution_index
[#](#_CPPv4N18rocblas_gemm_flags39rocblas_gemm_flags_check_solution_indexE)

-
enumerator rocblas_gemm_flags_fp16_alt_impl_rnz
[#](#_CPPv4N18rocblas_gemm_flags36rocblas_gemm_flags_fp16_alt_impl_rnzE)

-
enumerator rocblas_gemm_flags_stochastic_rounding
[#](#_CPPv4N18rocblas_gemm_flags38rocblas_gemm_flags_stochastic_roundingE)

-
enumerator rocblas_gemm_flags_none
