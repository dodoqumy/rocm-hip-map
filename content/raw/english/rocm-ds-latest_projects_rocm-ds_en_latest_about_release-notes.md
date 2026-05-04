---
title: "ROCm-DS 25.10 Release notes"
source_url: "https://rocm.docs.amd.com/projects/rocm-ds/en/latest/about/release-notes.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:26:03.352736+00:00
content_hash: "65a52c1998847b93"
---

# ROCm-DS 25.10 Release notes[#](#rocm-ds-25-10-release-notes)


4 min read time

AMD is pleased to announce the general availability (GA) release of the ROCm Data Science Toolkit (ROCm-DS), a comprehensive open-source software collection designed to accelerate data science and machine learning workloads on AMD GPUs. This GA release marks a significant milestone for ROCm-DS as hipDF and hipMM transition to production status. Additionally, it introduces two new production components: hipRAFT and hipVS. The GA release provides an end-to-end GPU-accelerated data science and AI ecosystem.

Note

hipGRAPH remains early access (EA) in ROCm-DS 25.10.

## ROCm-DS release highlights[#](#rocm-ds-release-highlights)

ROCm-DS 25.10 is a general availability release providing a production-ready foundation for GPU-accelerated data science on AMD hardware, with continued development focused on expanded capabilities and performance optimization in future versions. This release includes the following major updates and highlights:

Transition of hipDF and hipMM from early access to production-ready status.

Introduction of hipRAFT and hipVS for advanced data science, machine learning, and vector similarity workloads.

Alignment of all ROCm-DS components with RAPIDS 25.02, ensuring compatibility and feature parity.

Enhanced performance, memory efficiency, and API stability across all components.

Continued support for both Python and C++ APIs, enabling integration with popular frameworks such as Pandas and other RAPIDS-compatible tools.


## ROCm-DS components[#](#rocm-ds-components)

The following table lists ROCm-DS components versions for the 25.10 release, including any version changes for the components. Click

## Detailed component Changelogs[#](#detailed-component-changelogs)

The following sections describe key changes to ROCm-DS components.

### hipDF (2.0.0)[#](#hipdf-2-0-0)

#### Added[#](#added)

Major upgrade aligning hipDF APIs with RAPIDS cuDF 25.02 APIs

ROCm 7.0.2 support


#### Known limitations and notes[#](#known-limitations-and-notes)

DEBUG builds with -O0 optimization are not currently supported. Use -Og or higher for DEBUG builds (default setting). Support for -O0 is planned in a future toolchain update.

When using the cudf.pandas acceleration layer with XNACK enabled and workloads that significantly exceed physical GPU VRAM (oversubscription), some systems might exhibit instability or reduced performance under heavy memory pressure.

Using the cudf.pandas acceleration layer with XNACK disabled (

`HSA_XNACK=0`

) can trigger instabilities.

### hipMM (3.0.0)[#](#hipmm-3-0-0)

#### Added[#](#id1)

Major upgrade aligning hipDF APIs with RAPIDS cuDF 25.02 APIs

ROCm 7.0.2 support


### hipRAFT (0.1.0)[#](#hipraft-0-1-0)

#### Added[#](#id2)

Major upgrade aligning hipDF APIs with RAPIDS cuDF 25.02 APIs

ROCm 7.0.2 support


#### Changes[#](#changes)

Fixed uninitialized shared memory and bounds checking issues

Optimized kernel launch parameters and LDS memory access for AMD GPUs

Additional thread safety


#### Known limitations and notes[#](#id3)

Multi-Node/ Multi GPU is experimental

Raft-dask is unsupported


### hipVS (0.1.0)[#](#hipvs-0-1-0)

#### Added[#](#id4)

Major upgrade aligning hipDF APIs with RAPIDS cuDF 25.02 APIs

ROCm 7.0.2 support


#### Changes[#](#id5)

Fixed uninitialized shared memory and bounds checking issues

Optimized kernel launch parameters and LDS memory access for AMD GPUs

Relaxed recall thresholds to account for hardware differences


#### Known limitations and notes[#](#id6)

Multi-GPU neighbors API with

[ROCm RCCL](https://rocm.docs.amd.com/projects/rccl/en/docs-7.0.2/)integration is experimental
