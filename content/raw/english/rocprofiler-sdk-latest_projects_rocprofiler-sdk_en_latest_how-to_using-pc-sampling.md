---
title: "Using PC sampling &#8212; ROCprofiler-SDK 1.1.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/how-to/using-pc-sampling.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:15:12.319028+00:00
content_hash: "170df441d4679c26"
---

# Using PC sampling[#](#using-pc-sampling)

PC (Program Counter) sampling service for GPU profiling is a profiling technique to periodically sample the program counter during GPU kernel execution. PC sampling helps in understanding code execution patterns and identifying hotspot(s).

Here are the benefits of using PC sampling:

Identify performance bottlenecks

Understand kernel execution behavior

Analyze code coverage

Find heavily executed code paths


To try out the PC sampling feature, you can use the command-line tool `rocprofv3`

or the ROCprofiler-SDK library on ROCm 6.4 or later.

Note

PC sampling is ONLY supported on AMD GPUs with architectures gfx90a and later.

## PC sampling availability and configuration[#](#pc-sampling-availability-and-configuration)

To check if the GPU supports PC sampling, use:

```
-L
```

Or

```
--list-avail
```

The output lists if `rocprofv3`

supports PC sampling on the GPU and the supported configuration.

```
Method :host_trap
Unit :time
Min_Interval :1
Max_Interval :18446744073709551615
Flags :none
```

The preceding output shows that the GPU supports PC sampling with the `ROCPROFILER_PC_SAMPLING_METHOD_HOST_TRAP`

method and the `ROCPROFILER_PC_SAMPLING_UNIT_TIME`

unit. The minimum and maximum intervals are also displayed.

Note

Important firmware fixes to host-trap and stochastic PC-sampling for AMD Instinct MI300X have been made in ROCm 7.0. To ensure that you have the latest fixes, check if you have the correct firmware versions installed:

For host-trap PC-sampling on MI300X: PSP TOS Firmware >= version 00.36.02.59 or 0x00360259 For stochastic PC-sampling on MI300X as described in the following section: MEC Firmware feature version: 50, firmware version >= 0x0000001a

To check the firmware versions, use:

```
# To check PSP TOS Firmware:
sudo cat /sys/kernel/debug/dri/0/amdgpu_firmware_info | grep SOS
# To check MEC Firmware:
sudo cat /sys/kernel/debug/dri/1/amdgpu_firmware_info | grep MEC
```

Based on the available PC-sampling configurations, use the following command to profile the application using PC-sampling:

```
--pc-sampling-beta-enabled --pc-sampling-method host_trap --pc-sampling-unit time --pc-sampling-interval 1 --output-format csv -- <application_path>
```

The preceding command enables PC sampling with the `host_trap`

method, `time`

unit, and an interval of `1`

μs (microsecond). Replace `<application_path>`

with the path to the application you want to profile.

This generates two files, `agent_info.csv`

and `pc_sampling_host_trap.csv`

. Both files are prefixed with the process ID.

Here are the contents of `pc_sampling_host_trap.csv`

file generated for MatrixTranspose sample application:

Sample_Timestamp |
Exec_Mask |
Dispatch_Id |
Instruction |
Instruction_Comment |
Correlation_Id |
|---|---|---|---|---|---|
3464444413017201 |
65535 |
1 |
s_endpgm |
1 |
|
3464444413017201 |
65535 |
1 |
s_waitcnt vmcnt(0) |
1 |
|
3464444413018481 |
65535 |
1 |
s_waitcnt vmcnt(0) |
1 |
|
3464444413018481 |
65535 |
1 |
s_endpgm |
1 |
|
3464444413018481 |
65535 |
1 |
s_waitcnt vmcnt(0) |
1 |
|
3464444413018481 |
65535 |
1 |
s_waitcnt vmcnt(0) |
1 |
|
3464444413018481 |
65535 |
1 |
s_endpgm |
1 |
|
3464444413018481 |
65535 |
1 |
s_endpgm |
1 |
|
3464444413019601 |
65535 |
1 |
s_waitcnt vmcnt(0) |
1 |
|
3464444413019761 |
65535 |
1 |
s_load_dword s8, s[4:5], 0x24 |
1 |
|
3464444413019761 |
65535 |
1 |
s_waitcnt vmcnt(0) |
1 |
|
3464444413019761 |
65535 |
1 |
s_endpgm |
1 |
|
3464444413019761 |
65535 |
1 |
s_load_dword s8, s[4:5], 0x24 |
1 |
|
3464444413019761 |
65535 |
1 |
s_endpgm |
1 |
|
3464444413019761 |
65535 |
1 |
s_endpgm |
1 |
|
3464444413020881 |
65535 |
1 |
s_endpgm |
1 |
|
3464444413020881 |
65535 |
1 |
s_endpgm |
1 |
|
3464444413020881 |
65535 |
1 |
s_endpgm |
1 |
|
3464444413020881 |
65535 |
1 |
s_waitcnt lgkmcnt(0) |
1 |
|
3464444413020881 |
65535 |
1 |
v_addc_co_u32_e32 v5, vcc, v1, v5, vcc |
1 |
|
3464444413020881 |
65535 |
1 |
s_endpgm |
1 |
|
3464444413020881 |
65535 |
1 |
s_waitcnt vmcnt(0) |
1 |
|
3464444413020881 |
65535 |
1 |
s_endpgm |
1 |
|
3464444413020881 |
65535 |
1 |
s_waitcnt vmcnt(0) |
1 |
|
3464444413021041 |
65535 |
1 |
s_endpgm |
1 |
|
3464444413020881 |
65535 |
1 |
v_bfe_u32 v0, v0, 10, 10 |
1 |
|
3464444413021041 |
65535 |
1 |
s_endpgm |
1 |
|
3464444413021041 |
65535 |
1 |
s_endpgm |
1 |
|
3464444413021041 |
65535 |
1 |
s_waitcnt vmcnt(0) |
1 |
|
3464444413021041 |
65535 |
1 |
s_endpgm |
1 |
|
3464444413021041 |
65535 |
1 |
s_waitcnt vmcnt(0) |
1 |
|
3464444413021041 |
65535 |
1 |
s_endpgm |
1 |
|
3464444413022001 |
65535 |
1 |
s_waitcnt vmcnt(0) |
1 |
|
3464444413022001 |
65535 |
1 |
s_endpgm |
1 |
|
3464444413022001 |
65535 |
1 |
s_endpgm |
1 |
|
3464444413022001 |
65535 |
1 |
s_endpgm |
1 |
|
3464444413022001 |
65535 |
1 |
s_endpgm |
1 |
|
3464444413022001 |
65535 |
1 |
s_waitcnt vmcnt(0) |
1 |
|
3464444413022001 |
65535 |
1 |
s_endpgm |
1 |
|
3464444413022001 |
65535 |
1 |
s_waitcnt vmcnt(0) |
1 |
|
3464444413022001 |
65535 |
1 |
s_waitcnt lgkmcnt(0) |
1 |
|
3464444413022161 |
65535 |
1 |
s_endpgm |
1 |
|
3464444413022161 |
65535 |
1 |
s_waitcnt vmcnt(0) |
1 |
|
3464444413022161 |
65535 |
1 |
s_endpgm |
1 |
|
3464444413022161 |
65535 |
1 |
s_load_dword s8, s[4:5], 0x24 |
1 |
|
3464444413022161 |
65535 |
1 |
global_store_dword v[0:1], v3, off |
1 |
|
3464444413022161 |
65535 |
1 |
s_endpgm |
1 |
|
3464444413022161 |
65535 |
1 |
s_endpgm |
1 |
|
3464444413022161 |
65535 |
1 |
s_waitcnt vmcnt(0) |
1 |
|
3464444413022161 |
65535 |
1 |
s_endpgm |
1 |
|
3464444413022161 |
65535 |
1 |
s_endpgm |
1 |
|
3464444413022161 |
65535 |
1 |
s_waitcnt vmcnt(0) |
1 |
|
3464444413022161 |
65535 |
1 |
s_endpgm |
1 |
|
3464444413022321 |
65535 |
1 |
s_load_dwordx4 s[0:3], s[4:5], 0x0 |
1 |
|
3464444413022161 |
65535 |
1 |
s_waitcnt vmcnt(0) |
1 |
|
3464444413022321 |
65535 |
1 |
s_endpgm |
1 |
|
3464444413022161 |
65535 |
1 |
s_waitcnt vmcnt(0) |
1 |
|
3464444413023281 |
65535 |
1 |
s_endpgm |
1 |
|
3464444413023281 |
65535 |
1 |
s_endpgm |
1 |
|
3464444413023281 |
65535 |
1 |
v_ashrrev_i32_e32 v1, 31, v0 |
1 |
|
3464444413024561 |
65535 |
1 |
s_waitcnt vmcnt(0) |
1 |
|
3464444413023281 |
65535 |
1 |
s_endpgm |
1 |
|
3464444413024561 |
65535 |
1 |
s_endpgm |
1 |
|
3464444413023761 |
65535 |
1 |
s_waitcnt vmcnt(0) |
1 |
|
3464444413026321 |
65535 |
1 |
s_waitcnt vmcnt(0) |
1 |
|
3464444413024401 |
65535 |
1 |
global_store_dword v[0:1], v3, off |
1 |
|
3464444413027121 |
65535 |
1 |
s_waitcnt vmcnt(0) |
1 |
|
3464444413025041 |
65535 |
1 |
v_add_co_u32_e32 v0, vcc, s0, v0 |
1 |
|
3464444413027761 |
65535 |
1 |
s_waitcnt vmcnt(0) |
1 |
|
3464444413025361 |
65535 |
1 |
s_endpgm |
1 |
|
3464444413027601 |
65535 |
1 |
s_waitcnt vmcnt(0) |
1 |
|
3464444413026321 |
65535 |
1 |
s_waitcnt vmcnt(0) |
1 |
|
3464444413028401 |
65535 |
1 |
s_waitcnt vmcnt(0) |
1 |
|
3464444413026481 |
65535 |
1 |
s_waitcnt vmcnt(0) |
1 |
|
3464444413028881 |
65535 |
1 |
s_waitcnt vmcnt(0) |
1 |
|
3464444413026641 |
65535 |
1 |
s_waitcnt vmcnt(0) |
1 |
|
3464444413028401 |
65535 |
1 |
s_load_dword s8, s[4:5], 0x24 |
1 |
|
3464444413027281 |
65535 |
1 |
s_waitcnt vmcnt(0) |
1 |
|
3464444413029681 |
65535 |
1 |
s_endpgm |
1 |

For description of the fields in the output file, see [PC sampling fields](#pc-sampling-fields).

If you find the `Instruction_Comment`

field in the output file to be empty, populate this field by compiling your application with debug symbols.
Enabling debug symbols while compiling the application maps back to the source line. This helps in understanding the code execution pattern and hotspots.

Sample_Timestamp |
Exec_Mask |
Dispatch_Id |
Instruction |
Instruction_Comment |
Correlation_Id |
|---|---|---|---|---|---|
54155306462675 |
65535 |
1 |
s_waitcnt lgkmcnt(0) |
/opt/rocm/include/hip/amd_detail/amd_hip_runtime.h:275 |
1 |
54155306462715 |
65535 |
1 |
s_waitcnt vmcnt(0) |
/opt/rocm-6.4.0/share/hip/samples/2_Cookbook/0_MatrixTranspose/MatrixTranspose.cpp:44 |
1 |
54155306462755 |
65535 |
1 |
s_endpgm |
/opt/rocm-6.4.0/share/hip/samples/2_Cookbook/0_MatrixTranspose/MatrixTranspose.cpp:45 |
1 |
54155306462755 |
65535 |
1 |
s_endpgm |
/opt/rocm-6.4.0/share/hip/samples/2_Cookbook/0_MatrixTranspose/MatrixTranspose.cpp:45 |
1 |
54155306462955 |
65535 |
1 |
s_endpgm |
/opt/rocm-6.4.0/share/hip/samples/2_Cookbook/0_MatrixTranspose/MatrixTranspose.cpp:45 |
1 |
54155306463035 |
65535 |
1 |
s_waitcnt vmcnt(0) |
/opt/rocm-6.4.0/share/hip/samples/2_Cookbook/0_MatrixTranspose/MatrixTranspose.cpp:44 |
1 |
54155306463235 |
65535 |
1 |
s_waitcnt vmcnt(0) |
/opt/rocm-6.4.0/share/hip/samples/2_Cookbook/0_MatrixTranspose/MatrixTranspose.cpp:44 |
1 |
54155306463315 |
65535 |
1 |
s_waitcnt vmcnt(0) |
/opt/rocm-6.4.0/share/hip/samples/2_Cookbook/0_MatrixTranspose/MatrixTranspose.cpp:44 |
1 |
54155306463515 |
65535 |
1 |
s_endpgm |
/opt/rocm-6.4.0/share/hip/samples/2_Cookbook/0_MatrixTranspose/MatrixTranspose.cpp:45 |
1 |
54155306463755 |
65535 |
1 |
s_waitcnt vmcnt(0) |
/opt/rocm-6.4.0/share/hip/samples/2_Cookbook/0_MatrixTranspose/MatrixTranspose.cpp:44 |
1 |
54155306463875 |
65535 |
1 |
s_waitcnt vmcnt(0) |
/opt/rocm-6.4.0/share/hip/samples/2_Cookbook/0_MatrixTranspose/MatrixTranspose.cpp:44 |
1 |
54155306464075 |
65535 |
1 |
v_mov_b32_e32 v2, s4 |
/opt/rocm/include/hip/amd_detail/amd_hip_runtime.h:275 |
1 |
54155306464155 |
65535 |
1 |
s_waitcnt vmcnt(0) |
/opt/rocm-6.4.0/share/hip/samples/2_Cookbook/0_MatrixTranspose/MatrixTranspose.cpp:44 |
1 |
54155306464155 |
65535 |
1 |
s_waitcnt vmcnt(0) |
/opt/rocm-6.4.0/share/hip/samples/2_Cookbook/0_MatrixTranspose/MatrixTranspose.cpp:44 |
1 |
54155306464275 |
65535 |
1 |
s_endpgm |
/opt/rocm-6.4.0/share/hip/samples/2_Cookbook/0_MatrixTranspose/MatrixTranspose.cpp:45 |
1 |
54155306464395 |
65535 |
1 |
s_waitcnt vmcnt(0) |
/opt/rocm-6.4.0/share/hip/samples/2_Cookbook/0_MatrixTranspose/MatrixTranspose.cpp:44 |
1 |
54155306464515 |
65535 |
1 |
s_waitcnt lgkmcnt(0) |
/opt/rocm/include/hip/amd_detail/amd_hip_runtime.h:275 |
1 |
54155306464555 |
65535 |
1 |
s_waitcnt vmcnt(0) |
/opt/rocm-6.4.0/share/hip/samples/2_Cookbook/0_MatrixTranspose/MatrixTranspose.cpp:44 |
1 |
54155306464595 |
65535 |
1 |
s_waitcnt vmcnt(0) |
/opt/rocm-6.4.0/share/hip/samples/2_Cookbook/0_MatrixTranspose/MatrixTranspose.cpp:44 |
1 |
54155306464595 |
65535 |
1 |
v_mov_b32_e32 v2, s6 |
/opt/rocm/include/hip/amd_detail/amd_hip_runtime.h:275 |
1 |
54155306464595 |
65535 |
1 |
s_waitcnt lgkmcnt(0) |
/opt/rocm/include/hip/amd_detail/amd_hip_runtime.h:275 |
1 |

The preceding output shows the `Instruction_Comment`

field populated with the source-line information.

## PC sampling fields[#](#pc-sampling-fields)

Here are the fields in the output file generated by PC sampling:

`Sample_Timestamp`

: Timestamp when sample is generated`Exec_Mask`

: Active SIMD lanes when sampled`Dispatch_Id`

: Originating kernel dispatch ID`Instruction`

: Assembly instruction such as`s_load_dword s8, s[1:2], 0x10`

`Instruction_Comment`

: Instruction comment that maps back to the source-line if debug symbols were enabled when application was compiled`Correlation_Id`

: API launch call ID that matches dispatch ID

To dump samples in a more comprehensive format, use JSON through

`--output-format json`

:

```
--pc-sampling-beta-enabled --pc-sampling-method host_trap --pc-sampling-unit time --pc-sampling-interval 1 --output-format json -- <application_path>
```

The preceding command generates a JSON file with the comprehensive output. Here is a trimmed down output with multiple records:


For description of the fields in the JSON output, see [Output file fields](using-rocprofv3.html#output-file-fields).

## Host-trap PC sampling and arbitrary sampling skid[#](#host-trap-pc-sampling-and-arbitrary-sampling-skid)

Host-trap PC sampling is a software-based technique that utilizes a background kernel thread to periodically interrupt running waves to capture the program counter (PC). This method is effective for gathering performance data without requiring specialized hardware to snapshot the waves. However, this method has certain limitations due to the potential delay between receiving and processing the interrupt by the wave to capture the PC. This delay can lead to a sampling skid, where the PC samples might be attributed to the instructions that are up to two instructions away from the actual source of latency. This results in a non-precise intra-kernel sampling method.

When analyzing an application profile generated by host-trap PC sampling, it is important to consider not only the costliest reported instruction but also the instructions immediately preceding or following it. If the costly instruction is near a branch instruction, it is important to consider the instruction targeted by the branch and the one immediately following it as well.

To address the limitations of host-trap sampling, the hardware-based stochastic PC sampling method has been developed. This method provides precise intra-kernel sampling with zero sampling skid, offering more accurate performance insights.

It is important to note that the skid issue inherent in host-trap PC sampling is not likely to be resolved in its current form. Therefore, to achieve more precise performance profiling, it is recommended to adopt stochastic PC sampling starting with the gfx942 architecture.

Note

Host-trap PC sampling is supported on AMD Instinct MI200, MI300, MI325, MI350, and MI355.

## Hardware-based (stochastic) PC sampling method[#](#hardware-based-stochastic-pc-sampling-method)

The `ROCPROFILER_PC_SAMPLING_METHOD_STOCHASTIC`

method has been introduced for the gfx942 architecture.
It employs a specific hardware for probing waves actively running on the GPU.
Besides the information already provided with `ROCPROFILER_PC_SAMPLING_METHOD_HOST_TRAP`

useful for
determining hotspots within the kernel, this method delivers additional information, which helps to determine
whether a sampled wave issued an instruction represented with the specified PC.
If not, this method provides the reason for not issuing the instruction (stall reason).
Such information is particularly useful for understanding stalls during kernel execution.

To use this method on gfx942, it is recommended to list available PC sampling configurations to verify if the latest ROCm stack is installed on the system using:

```
-L
```

An output similar to the following indicates that the `ROCPROFILER_PC_SAMPLING_METHOD_STOCHASTIC`

method is available:

```
Method :stochastic
Unit :cycle
Min_Interval :256
Max_Interval :2147483648
Flags :interval pow2
```

Note

On gfx942, `ROCPROFILER_PC_SAMPLING_METHOD_STOCHASTIC`

requires intervals to be specified in cycles with values as powers of 2.

To profile an application with `ROCPROFILER_PC_SAMPLING_METHOD_STOCHASTIC`

PC sampling enabled on gfx942, use:

```
--pc-sampling-beta-enabled --pc-sampling-method stochastic --pc-sampling-unit cycles --pc-sampling-interval 1048576 --output-format csv, json -- <application_path>
```

The preceding command serializes samples in both CSV and JSON output formats in the `pc_sampling_stochastic.csv`

and `out_results.json`

files, respectively.

On comparing the [pc_sampling_stochastic.csv](#pc-sampling-stochastic) to [pc_sampling_host_trap.csv](#pc-sampling-host-trap), you can notice that the `ROCPROFILER_PC_SAMPLING_METHOD_STOCHASTIC`

method
generates the following additional fields:

`Wave_Issued_Instruction`

: Indicates whether the wave issued an instruction represented with the specified PC. Value = 1 for yes and 0 for no.`Instruction_Type`

: If the value of`Wave_Issued_Instruction`

is 1, this field indicates the type of the issued instruction. Otherwise, this field remains irrelevant.`Stall_Reason`

: If the value of`Wave_Issued_Instruction`

is 0, this field indicates the reason for not issuing the instruction (stall reason). Otherwise, this field remains irrelevant.`Wave_Count`

: Total number of waves actively running on a compute unit when the sample is generated.

Sample_Timestamp |
Exec_Mask |
Dispatch_Id |
Instruction |
Instruction_Comment |
Correlation_Id |
Wave_Issued_Instruction |
Instruction_Type |
Stall_Reason |
Wave_Count |
|---|---|---|---|---|---|---|---|---|---|
390705261841337 |
18446744073709551615 |
24 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:133 |
24 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
4 |
390705261924637 |
18446744073709551615 |
29 |
v_max_i32_e32 v1, v2, v0 |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:77 |
29 |
1 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_VALU |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_OTHER_WAIT |
6 |
390705694732429 |
18446744073709551615 |
53 |
v_mad_u64_u32 v[0:1], s[2:3], v0, s2, v[2:3] |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:80 |
53 |
1 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_VALU |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_OTHER_WAIT |
6 |
390705694744189 |
18446744073709551615 |
54 |
v_lshl_add_u64 v[0:1], s[4:5], 0, v[0:1] |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:99 |
54 |
1 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_VALU |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_OTHER_WAIT |
4 |
390705694769549 |
18446744073709551615 |
56 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:133 |
56 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
6 |
390705694772089 |
18446744073709551615 |
56 |
s_waitcnt lgkmcnt(0) |
/usr/include/hip/amd_detail/amd_hip_runtime.h:275 |
56 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
5 |
390705694810449 |
18446744073709551615 |
58 |
v_cmp_gt_i32_e32 vcc, s2, v1 |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:94 |
58 |
1 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_VALU |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_OTHER_WAIT |
3 |
390705694820489 |
18446744073709551615 |
59 |
s_waitcnt vmcnt(1) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:116 |
59 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
4 |
390705694840850 |
18446744073709551615 |
60 |
s_and_b32 s5, s4, 0xffff |
/usr/include/hip/amd_detail/amd_hip_runtime.h:275 |
60 |
1 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_SCALAR |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_OTHER_WAIT |
5 |
390705694856630 |
18446744073709551615 |
61 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:82 |
61 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
5 |
390706112944694 |
18446744073709551615 |
65 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:82 |
65 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
7 |
390706112965404 |
18446744073709551615 |
66 |
global_store_dword v[0:1], v2, off |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:99 |
66 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_ALU_DEPENDENCY |
3 |
390706112966284 |
18446744073709551615 |
66 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:99 |
66 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
6 |
390706112966644 |
18446744073709551615 |
66 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:99 |
66 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
3 |
390706112967404 |
18446744073709551615 |
66 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:99 |
66 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
4 |
390706112971414 |
18446744073709551615 |
66 |
s_load_dwordx4 s[4:7], s[0:1], 0x0 |
/usr/include/hip/amd_detail/amd_hip_runtime.h:275 |
66 |
1 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_SCALAR |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_OTHER_WAIT |
5 |
390706112984885 |
18446744073709551615 |
67 |
s_waitcnt vmcnt(1) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:116 |
67 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
5 |
390706112988655 |
18446744073709551615 |
67 |
s_waitcnt vmcnt(1) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:116 |
67 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
4 |
390706113000775 |
18446744073709551615 |
68 |
v_add_u32_e32 v0, s3, v0 |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:128 |
68 |
1 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_VALU |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_OTHER_WAIT |
5 |
390706113004375 |
18446744073709551615 |
68 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:133 |
68 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
4 |
390706113053815 |
18446744073709551615 |
69 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:82 |
69 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
7 |
390706113059125 |
18446744073709551615 |
69 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:82 |
69 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
6 |
390706113080805 |
18446744073709551615 |
70 |
s_load_dwordx4 s[4:7], s[0:1], 0x0 |
/usr/include/hip/amd_detail/amd_hip_runtime.h:275 |
70 |
1 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_SCALAR |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_OTHER_WAIT |
3 |
390706113097725 |
18446744073709551615 |
71 |
s_waitcnt vmcnt(1) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:116 |
71 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
3 |
390706113101805 |
18446744073709551615 |
71 |
s_waitcnt vmcnt(1) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:116 |
71 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
4 |
390706113111775 |
18446744073709551615 |
72 |
v_sub_f32_e32 v4, v2, v3 |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:133 |
72 |
1 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_VALU |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_OTHER_WAIT |
5 |
390706113115735 |
18446744073709551615 |
72 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:133 |
72 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
5 |
390706113134725 |
18446744073709551615 |
73 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:82 |
73 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
7 |
390706113147605 |
18446744073709551615 |
74 |
s_waitcnt lgkmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:97 |
74 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
4 |
390706113149485 |
18446744073709551615 |
74 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:99 |
74 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
4 |
390706113153735 |
18446744073709551615 |
74 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:99 |
74 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
5 |
390706113179326 |
18446744073709551615 |
76 |
s_waitcnt lgkmcnt(0) |
/usr/include/hip/amd_detail/amd_hip_runtime.h:275 |
76 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
2 |
390706113184086 |
18446744073709551615 |
76 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:133 |
76 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
5 |
390706113184406 |
18446744073709551615 |
76 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:133 |
76 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
4 |
390706113206736 |
18446744073709551615 |
77 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:82 |
77 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
10 |
390706113209216 |
18446744073709551615 |
77 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:82 |
77 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
11 |
390706113220016 |
18446744073709551615 |
78 |
s_load_dword s4, s[0:1], 0x2c |
/usr/include/hip/amd_detail/amd_hip_runtime.h:275 |
78 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_NO_INSTRUCTION_AVAILABLE |
1 |
390706113221566 |
18446744073709551615 |
78 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:99 |
78 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
4 |
390706113227816 |
18446744073709551615 |
78 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:99 |
78 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
5 |
390706113234976 |
18446744073709551615 |
79 |
s_waitcnt vmcnt(1) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:116 |
79 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
4 |
390706113235016 |
18446744073709551615 |
79 |
s_load_dwordx2 s[0:1], s[0:1], 0x10 |
/usr/include/hip/amd_detail/amd_hip_runtime.h:275 |
79 |
1 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_SCALAR |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_OTHER_WAIT |
3 |
390706113236806 |
18446744073709551615 |
79 |
s_and_saveexec_b64 s[2:3], vcc |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:113 |
79 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_ALU_DEPENDENCY |
3 |
390706113250926 |
18446744073709551615 |
80 |
s_waitcnt lgkmcnt(0) |
/usr/include/hip/amd_detail/amd_hip_runtime.h:275 |
80 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
1 |
390706113253456 |
18446744073709551615 |
80 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:133 |
80 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
5 |
390706113255496 |
18446744073709551615 |
80 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:133 |
80 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
6 |
390706113257566 |
18446744073709551615 |
80 |
v_add_f32_e32 v2, 1.0, v2 |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:133 |
80 |
1 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_VALU |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_OTHER_WAIT |
4 |
390706113270176 |
18446744073709551615 |
81 |
s_waitcnt lgkmcnt(0) |
/usr/include/hip/amd_detail/amd_hip_runtime.h:275 |
81 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
3 |
390706113278256 |
18446744073709551615 |
81 |
s_load_dword s2, s[0:1], 0x18 |
/usr/include/hip/amd_detail/amd_hip_runtime.h:275 |
81 |
1 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_SCALAR |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_OTHER_WAIT |
8 |
390706113292776 |
18446744073709551615 |
82 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:99 |
82 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
3 |
390706113301126 |
18446744073709551615 |
83 |
s_waitcnt lgkmcnt(0) |
/usr/include/hip/amd_detail/amd_hip_runtime.h:275 |
83 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
1 |
390706113301606 |
18446744073709551615 |
83 |
s_and_saveexec_b64 s[2:3], vcc |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:113 |
83 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_ALU_DEPENDENCY |
3 |
390706113303846 |
18446744073709551615 |
83 |
s_and_saveexec_b64 s[2:3], vcc |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:113 |
83 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_ALU_DEPENDENCY |
3 |
390706113305086 |
18446744073709551615 |
83 |
v_lshlrev_b64 v[0:1], 2, v[0:1] |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:116 |
83 |
1 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_VALU |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_OTHER_WAIT |
3 |
390706113317256 |
18446744073709551615 |
84 |
v_div_fmas_f32 v3, v3, v6, v7 |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:133 |
84 |
1 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_VALU |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_OTHER_WAIT |
5 |
390706113318166 |
18446744073709551615 |
84 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:133 |
84 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
6 |
390706113336687 |
18446744073709551615 |
85 |
global_load_dword v2, v[2:3], off |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:82 |
85 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_ALU_DEPENDENCY |
11 |
390706113351087 |
18446744073709551615 |
86 |
s_mul_i32 s2, s2, s5 |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:93 |
86 |
1 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_SCALAR |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_OTHER_WAIT |
3 |
390706113352487 |
18446744073709551615 |
86 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:99 |
86 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
5 |
390706113369607 |
18446744073709551615 |
87 |
s_waitcnt vmcnt(1) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:116 |
87 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
6 |
390706113373647 |
18446744073709551615 |
87 |
s_waitcnt vmcnt(1) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:116 |
87 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
5 |
390706113387017 |
18446744073709551615 |
88 |
s_waitcnt lgkmcnt(0) |
/usr/include/hip/amd_detail/amd_hip_runtime.h:275 |
88 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
1 |
390706113390207 |
18446744073709551615 |
88 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:133 |
88 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
5 |
390706113408977 |
18446744073709551615 |
89 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:82 |
89 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
5 |
390706113409057 |
18446744073709551615 |
89 |
v_add_f32_e32 v2, v2, v3 |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:82 |
89 |
1 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_VALU |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_OTHER_WAIT |
10 |
390706113411607 |
18446744073709551615 |
89 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:82 |
89 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
9 |
390706113411737 |
18446744073709551615 |
89 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:82 |
89 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
7 |
390706113412777 |
18446744073709551615 |
89 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:82 |
89 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
7 |
390706113415847 |
18446744073709551615 |
89 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:82 |
89 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
9 |
390706113424217 |
18446744073709551615 |
90 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:99 |
90 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
4 |
390706113443127 |
18446744073709551615 |
91 |
v_add_f32_e32 v2, -1.0, v2 |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:116 |
91 |
1 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_VALU |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_OTHER_WAIT |
2 |
390706113444857 |
18446744073709551615 |
91 |
v_add_f32_e32 v3, -1.0, v3 |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:116 |
91 |
1 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_VALU |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_OTHER_WAIT |
3 |
390706113459367 |
18446744073709551615 |
92 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:133 |
92 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
6 |
390706113459767 |
18446744073709551615 |
92 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:133 |
92 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
6 |
390706113462927 |
18446744073709551615 |
92 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:133 |
92 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
4 |
390706113480097 |
18446744073709551615 |
93 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:82 |
93 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
15 |
390706113484087 |
18446744073709551615 |
93 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:82 |
93 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
7 |
390706113496167 |
18446744073709551615 |
93 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:82 |
93 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
6 |
390706113500167 |
18446744073709551615 |
93 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:82 |
93 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
9 |
390706113506057 |
18446744073709551615 |
93 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:82 |
93 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
14 |
390706113506327 |
18446744073709551615 |
93 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:82 |
93 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
6 |
390706113508577 |
18446744073709551615 |
93 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:82 |
93 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
17 |
390706113522058 |
18446744073709551615 |
93 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:82 |
93 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
15 |
390706113561378 |
18446744073709551615 |
94 |
s_waitcnt lgkmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:97 |
94 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
3 |
390706113573138 |
18446744073709551615 |
95 |
s_waitcnt vmcnt(1) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:116 |
95 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
5 |
390706526501642 |
18446744073709551615 |
112 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:133 |
112 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
6 |
390706526582893 |
18446744073709551615 |
117 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:82 |
117 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
8 |
390706526594683 |
18446744073709551615 |
118 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:99 |
118 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
4 |
390706526629813 |
18446744073709551615 |
120 |
s_waitcnt lgkmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:131 |
120 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
5 |
390706526629803 |
18446744073709551615 |
120 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:133 |
120 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
5 |
390706526633683 |
18446744073709551615 |
120 |
v_mul_f32_e32 v7, v3, v6 |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:133 |
120 |
1 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_VALU |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_OTHER_WAIT |
4 |
390706526634933 |
18446744073709551615 |
120 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:133 |
120 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
4 |
390706526665053 |
18446744073709551615 |
122 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:99 |
122 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
4 |
390706526677283 |
18446744073709551615 |
123 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:116 |
123 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
6 |
390706526695733 |
18446744073709551615 |
124 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:133 |
124 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
5 |
390706526809694 |
18446744073709551615 |
126 |
v_and_b32_e32 v2, 0x7fffffff, v2 |
/opt/rocm-6.4.0/lib/llvm/lib/clang/19/include/__clang_hip_math.h:427 |
126 |
1 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_VALU |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_OTHER_WAIT |
5 |
390706526810014 |
18446744073709551615 |
126 |
s_waitcnt vmcnt(0) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:99 |
126 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
5 |
390706526821284 |
18446744073709551615 |
127 |
s_waitcnt vmcnt(1) |
/home/vlaindic/git/rocprofiler-sdk-internal/tests/bin/vector-operations/vector-ops.cpp:116 |
127 |
0 |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_TYPE_NO_INST |
ROCPROFILER_PC_SAMPLING_INSTRUCTION_NOT_ISSUED_REASON_WAITCNT |
5 |

Similarly, `ROCPROFILER_PC_SAMPLING_METHOD_STOCHASTIC`

method delivers additional information to every sample in the JSON output.

Here is a `out_results.json`

file sample:


Fields starting with `arb_state_`

are of particular interest as they indicate the state of the arbiter at the time of sampling.
For example, `arb_state_issue_`

fields indicate the type of instructions issued by the arbiter at the time of sampling.
On the other hand, `arb_state_stall_`

fields indicate the type of instructions stalled at the time of sampling.
This information is useful for understanding how many instructions per cycle (IPC) are issued.

Note

The stochastic PC sampling is supported on AMD Instinct MI300, MI325, MI350, and MI355.
