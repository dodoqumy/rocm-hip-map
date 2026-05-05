---
title: "ROCm components supported in HIP SDK"
source_url: "https://rocm.docs.amd.com/projects/install-on-windows/en/latest/conceptual/component-support.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:14:52.244763+00:00
content_hash: "37b267114f093d65"
---

# ROCm components supported in HIP SDK[#](#rocm-components-supported-in-hip-sdk)

2026-02-19

1 min read time

The HIP SDK brings a subset of ROCm to developers on Windows. The collection of features enabled on Windows is referred to as the HIP SDK. These features allow developers to use the HIP runtime, HIP math libraries and HIP Primitive libraries. The following table shows the differences between Windows and Linux releases.

Note

HIPBlasLT is now available for Windows users in HIP SDK version 6.4.2 and later, supported on gfx1101.

Component |
Linux |
Windows |
|---|---|---|
Driver |
AMD GPU driver |
|
Compiler |
hipcc/amdclang++ |
hipcc/clang++ |
Debugger |
||
Profiler |
||
Porting Tools |
||
Runtime |
|
|
Math Libraries |
Supported |
Supported |
Primitives Libraries |
Supported |
Supported |
Communication Libraries |
Supported |
Not available |
AI Libraries |
Not available |
|
System Management |
hipInfo |
|
AI Frameworks |
Not available |
|
CMake HIP Language |
Enabled |
Unsupported |
Visual Studio |
Not applicable |
Plugin available |
Supported |
Supported |
