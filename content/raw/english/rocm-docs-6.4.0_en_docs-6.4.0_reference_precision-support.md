---
title: "Data types and precision support"
source_url: "https://rocm.docs.amd.com/en/docs-6.4.0/reference/precision-support.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T16:05:50.190171+00:00
content_hash: "f062a2933429e2a3"
---

# Data types and precision support[#](#data-types-and-precision-support)

2025-04-09

7 min read time

This topic lists the data types support on AMD GPUs, ROCm libraries along
with corresponding [HIP](https://rocm.docs.amd.com/projects/HIP/en/docs-6.4.0/index.html) data types.

## Integral types[#](#integral-types)

The signed and unsigned integral types supported by ROCm are listed in the following table.

Type name |
HIP type |
Description |
|---|---|---|
int8 |
|
A signed or unsigned 8-bit integer |
int16 |
|
A signed or unsigned 16-bit integer |
int32 |
|
A signed or unsigned 32-bit integer |
int64 |
|
A signed or unsigned 64-bit integer |

## Floating-point types[#](#floating-point-types)

The floating-point types supported by ROCm are listed in the following table.

Type name |
HIP type |
Description |
|---|---|---|
float8 (E4M3) |
|
An 8-bit floating-point number that mostly follows IEEE-754 conventions
and |
float8 (E5M2) |
|
An 8-bit floating-point number mostly following IEEE-754 conventions and
|
float16 |
|
A 16-bit floating-point number that conforms to the IEEE 754-2008 half-precision storage format. |
bfloat16 |
|
A shortened 16-bit version of the IEEE 754 single-precision storage format. |
tensorfloat32 |
Not available |
A floating-point number that occupies 32 bits or less of storage, providing improved range compared to half (16-bit) format, at (potentially) greater throughput than single-precision (32-bit) formats. |
float32 |
|
A 32-bit floating-point number that conforms to the IEEE 754 single-precision storage format. |
float64 |
|
A 64-bit floating-point number that conforms to the IEEE 754 double-precision storage format. |

Note

The float8 and tensorfloat32 types are internal types used in calculations in Matrix Cores and can be stored in any type of the same size.

The encodings for FP8 (E5M2) and FP8 (E4M3) that the MI300 series natively supports differ from the FP8 (E5M2) and FP8 (E4M3) encodings used in NVIDIA H100 (

[FP8 Formats for Deep Learning](https://arxiv.org/abs/2209.05433)).In some AMD documents and articles, float8 (E5M2) is referred to as bfloat8.

The

[low precision floating point types page](https://rocm.docs.amd.com/projects/HIP/en/docs-6.4.0/reference/low_fp_types.html)describes how to use these types in HIP with examples.

## Level of support definitions[#](#level-of-support-definitions)

In the following sections, icons represent the level of support. These icons, described in the following table, are also used in the library data type support pages.

Icon |
Definition |
|---|---|
NA |
Not applicable |
❌ |
Not supported |
⚠️ |
Partial support |
✅ |
Full support |

Note

Full support means that the type is supported natively or with hardware emulation.

Native support means that the operations for that type are implemented in hardware. Types that are not natively supported are emulated with the available hardware. The performance of non-natively supported types can differ from the full instruction throughput rate. For example, 16-bit integer operations can be performed on the 32-bit integer ALUs at full rate; however, 64-bit integer operations might need several instructions on the 32-bit integer ALUs.

Any type can be emulated by software, but this page does not cover such cases.


## Data type support by Hardware Architecture[#](#data-type-support-by-hardware-architecture)

The MI200 series GPUs, which include MI210, MI250, and MI250X, are based on the CDNA2 architecture. The MI300 series GPUs, consisting of MI300A, MI300X, and MI325X, are based on the CDNA3 architecture.

### Compute units support[#](#compute-units-support)

The following table lists data type support for compute units.

Type name |
int8 |
int16 |
int32 |
int64 |
|---|---|---|---|---|
MI100 |
✅ |
✅ |
✅ |
✅ |
MI200 series |
✅ |
✅ |
✅ |
✅ |
MI300 series |
✅ |
✅ |
✅ |
✅ |

Type name |
float8 (E4M3) |
float8 (E5M2) |
float16 |
bfloat16 |
tensorfloat32 |
float32 |
float64 |
|---|---|---|---|---|---|---|---|
MI100 |
❌ |
❌ |
✅ |
✅ |
❌ |
✅ |
✅ |
MI200 series |
❌ |
❌ |
✅ |
✅ |
❌ |
✅ |
✅ |
MI300 series |
❌ |
❌ |
✅ |
✅ |
❌ |
✅ |
✅ |

### Matrix core support[#](#matrix-core-support)

The following table lists data type support for AMD GPU matrix cores.

Type name |
int8 |
int16 |
int32 |
int64 |
|---|---|---|---|---|
MI100 |
✅ |
❌ |
❌ |
❌ |
MI200 series |
✅ |
❌ |
❌ |
❌ |
MI300 series |
✅ |
❌ |
❌ |
❌ |

Type name |
float8 (E4M3) |
float8 (E5M2) |
float16 |
bfloat16 |
tensorfloat32 |
float32 |
float64 |
|---|---|---|---|---|---|---|---|
MI100 |
❌ |
❌ |
✅ |
✅ |
❌ |
✅ |
❌ |
MI200 series |
❌ |
❌ |
✅ |
✅ |
❌ |
✅ |
✅ |
MI300 series |
✅ |
✅ |
✅ |
✅ |
✅ |
✅ |
✅ |

### Atomic operations support[#](#atomic-operations-support)

The following table lists which data types are supported for atomic
operations on AMD GPUs. The atomics operation type behavior is affected by the
memory locations, memory granularity, or scope of operations. For detailed
various support of atomic read-modify-write (atomicRMW) operations collected on
the [Hardware atomics operation support](gpu-atomics-operation.html#hw-atomics-operation-support)
page.

Type name |
int8 |
int16 |
int32 |
int64 |
|---|---|---|---|---|
MI100 |
❌ |
❌ |
✅ |
✅ |
MI200 series |
❌ |
❌ |
✅ |
✅ |
MI300 series |
❌ |
❌ |
✅ |
✅ |

Type name |
float8 (E4M3) |
float8 (E5M2) |
2 x float16 |
2 x bfloat16 |
tensorfloat32 |
float32 |
float64 |
|---|---|---|---|---|---|---|---|
MI100 |
❌ |
❌ |
✅ |
✅ |
❌ |
✅ |
❌ |
MI200 series |
❌ |
❌ |
✅ |
✅ |
❌ |
✅ |
✅ |
MI300 series |
❌ |
❌ |
✅ |
✅ |
❌ |
✅ |
✅ |

Note

You can emulate atomic operations using software for cases that are not natively supported. Software-emulated atomic operations have a high negative performance impact when they frequently access the same memory address.

## Data type support in ROCm libraries[#](#data-type-support-in-rocm-libraries)

ROCm library support for int8, float8 (E4M3), float8 (E5M2), int16, float16, bfloat16, int32, tensorfloat32, float32, int64, and float64 is listed in the following tables.

### Libraries input/output type support[#](#libraries-input-output-type-support)

The following tables list ROCm library support for specific input and output data types. Refer to the corresponding library data type support page for a detailed description.

Library input/output data type name |
float8 (E4M3) |
float8 (E5M2) |
float16 |
bfloat16 |
tensorfloat32 |
float32 |
float64 |
|---|---|---|---|---|---|---|---|
❌/❌ |
❌/❌ |
✅/✅ |
✅/✅ |
❌/❌ |
❌/❌ |
❌/❌ |
|
NA/❌ |
NA/❌ |
NA/✅ |
NA/❌ |
NA/❌ |
NA/✅ |
NA/✅ |
|
NA/❌ |
NA/❌ |
NA/✅ |
NA/❌ |
NA/❌ |
NA/✅ |
NA/✅ |
|
❌/❌ |
❌/❌ |
✅/✅ |
✅/✅ |
❌/❌ |
✅/✅ |
✅/✅ |
|
❌/❌ |
❌/❌ |
✅/✅ |
✅/✅ |
❌/❌ |
✅/✅ |
✅/✅ |
|
❌/❌ |
❌/❌ |
⚠️/⚠️ |
⚠️/⚠️ |
❌/❌ |
✅/✅ |
✅/✅ |

Note

As random number generation libraries, rocRAND and hipRAND only specify output data types for the random values they generate, with no need for input data types.

### Libraries internal calculations type support[#](#libraries-internal-calculations-type-support)

The following tables list ROCm library support for specific internal data types. Refer to the corresponding library data type support page for a detailed description.
