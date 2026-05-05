---
title: "ROCprofiler-SDK samples &#8212; ROCprofiler-SDK 1.1.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/how-to/samples.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:15:01.850300+00:00
content_hash: "3c64f8bfce6586ef"
---

# ROCprofiler-SDK samples[#](#rocprofiler-sdk-samples)

The samples are provided to help you see the profiler in action.

## Finding samples[#](#finding-samples)

The ROCm installation provides sample programs and `rocprofv3`

tool.

Sample programs are installed here:



`rocprofv3`

tool is installed here:


## Building Samples[#](#building-samples)

To build samples from any directory, run:

```
-B build-rocprofiler-sdk-samples /opt/rocm/share/rocprofiler-sdk/samples -DCMAKE_PREFIX_PATH=/opt/rocm
cmake --build build-rocprofiler-sdk-samples --target all --parallel 8
```

## Running samples[#](#running-samples)

To run the built samples, `cd`

into the `build-rocprofiler-sdk-samples`

directory and run:

```
-V
```

The -V option enables verbose output, providing detailed information about the test execution.
