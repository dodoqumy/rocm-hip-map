---
title: "Precision support"
source_url: "https://rocm.docs.amd.com/en/docs-6.2.0/compatibility/precision-support.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T16:17:44.755220+00:00
content_hash: "27dc53ed2b0cb943"
---

# Precision support[#](#precision-support)



Use the following sections to identify data types and HIP types ROCm™ supports.

## Integral types[#](#integral-types)

The signed and unsigned integral types that are supported by ROCm are listed in the following table, together with their corresponding HIP type and a short description.

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

The floating-point types that are supported by ROCm are listed in the following table, together with their corresponding HIP type and a short description.

Type name |
HIP type |
Description |
|---|---|---|
float8 (E4M3) |
|
An 8-bit floating-point number that mostly follows IEEE-754 conventions and |
float8 (E5M2) |
|
An 8-bit floating-point number mostly following IEEE-754 conventions and |
float16 |
|
A 16-bit floating-point number that conforms to the IEEE 754-2008 half-precision storage format. |
bfloat16 |
|
A shortened 16-bit version of the IEEE 754 single-precision storage format. |
tensorfloat32 |
|
A floating-point number that occupies 32 bits or less of storage, providing improved range compared to half (16-bit) format, at (potentially) greater throughput than single-precision (32-bit) formats. |
float32 |
|
A 32-bit floating-point number that conforms to the IEEE 754 single-precision storage format. |
float64 |
|
A 64-bit floating-point number that conforms to the IEEE 754 double-precision storage format. |

Note

The float8 and tensorfloat32 types are internal types used in calculations in Matrix Cores and can be stored in any type of the same size.

The encodings for FP8 (E5M2) and FP8 (E4M3) that are natively supported by MI300 differ from the FP8 (E5M2) and FP8 (E4M3) encodings used in H100 (

[FP8 Formats for Deep Learning](https://arxiv.org/abs/2209.05433)).In some AMD documents and articles, float8 (E5M2) is referred to as bfloat8.


## ROCm support icons[#](#rocm-support-icons)

In the following sections, we use icons to represent the level of support. These icons, described in the following table, are also used on the library data type support pages.

Icon |
Definition |
|---|---|
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


## Hardware type support[#](#hardware-type-support)

AMD GPU hardware support for data types is listed in the following tables.

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

The following table lists data type support for atomic operations.

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
❌ |
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
❌ |
❌ |
✅ |
❌ |
MI200 series |
❌ |
❌ |
✅ |
❌ |
❌ |
✅ |
✅ |
MI300 series |
❌ |
❌ |
✅ |
❌ |
❌ |
✅ |
✅ |

Note

For cases that are not natively supported, you can emulate atomic operations using software. Software-emulated atomic operations have high negative performance impact when they frequently access the same memory address.

## Data Type support in ROCm Libraries[#](#data-type-support-in-rocm-libraries)

ROCm library support for int8, float8 (E4M3), float8 (E5M2), int16, float16, bfloat16, int32, tensorfloat32, float32, int64, and float64 is listed in the following tables.

### Libraries input/output type support[#](#libraries-input-output-type-support)

The following tables list ROCm library support for specific input and output data types. For a detailed description, refer to the corresponding library data type support page.

Library input/output data type name |
float8 (E4M3) |
float8 (E5M2) |
float16 |
bfloat16 |
tensorfloat32 |
float32 |
float64 |
|---|---|---|---|---|---|---|---|
hipSPARSELt ( |
❌/❌ |
❌/❌ |
✅/✅ |
✅/✅ |
❌/❌ |
❌/❌ |
❌/❌ |
rocRAND (details) |
-/❌ |
-/❌ |
-/✅ |
-/❌ |
-/❌ |
-/✅ |
-/✅ |
hipRAND ( |
-/❌ |
-/❌ |
-/✅ |
-/❌ |
-/❌ |
-/✅ |
-/✅ |
rocPRIM ( |
❌/❌ |
❌/❌ |
✅/✅ |
✅/✅ |
❌/❌ |
✅/✅ |
✅/✅ |
hipCUB ( |
❌/❌ |
❌/❌ |
✅/✅ |
✅/✅ |
❌/❌ |
✅/✅ |
✅/✅ |
rocThrust ( |
❌/❌ |
❌/❌ |
⚠️/⚠️ |
⚠️/⚠️ |
❌/❌ |
✅/✅ |
✅/✅ |

### Libraries internal calculations type support[#](#libraries-internal-calculations-type-support)

The following tables list ROCm library support for specific internal data types. For a detailed description, refer to the corresponding library data type support page.
