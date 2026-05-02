---
title: "CK Tile Hardware Documentation &#8212; Composable Kernel 1.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/composable_kernel/en/latest/conceptual/ck_tile/hardware/index.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:10:25.804426+00:00
content_hash: "1182ce6940b0ad45"
---

# CK Tile Hardware Documentation[#](#ck-tile-hardware-documentation)

This section provides in-depth coverage of hardware-specific concepts and optimizations for CK Tile on AMD GPUs.

## Overview[#](#overview)

Understanding the underlying hardware architecture is crucial for achieving optimal performance with CK Tile. This documentation covers:

AMD CDNA architecture fundamentals

Memory hierarchy and optimization techniques

Practical examples of high-performance kernels


## Documentation Structure[#](#documentation-structure)

### GPU Architecture Basics[#](#gpu-architecture-basics)

[Intro to AMD CDNA Architecture](gpu_basics.html#ck-tile-gpu-basics) provides an introduction to AMD CDNA architecture.

### LDS and Bank Conflicts[#](#lds-and-bank-conflicts)

[Understanding AMD GPU LDS and Bank Conflicts](lds_bank_conflicts.html#ck-tile-lds-bank-conflicts) explains Local Data Share (LDS) optimization.

### GEMM Optimization Case Study[#](#gemm-optimization-case-study)

[A Block GEMM on MI300](gemm_optimization.html#ck-tile-gemm-optimization) demonstrates a complete optimization journey.

## Key Hardware Considerations[#](#key-hardware-considerations)

### Memory Hierarchy[#](#memory-hierarchy)

**Global Memory**: High latency, high bandwidthOptimize with coalesced access patterns

Use tile windows for automatic optimization


**L2/Infinity Cache**: Intermediate storageBenefits from spatial and temporal locality

CK Tile’s tiling naturally improves cache hit rates


**LDS**: Low latency, shared within CU64KB per CU, organized in 32 banks

CK Tile handles bank conflict avoidance


**Registers**: Lowest latency, per-thread storage512 VGPRs available per wavefront

CK Tile’s compile-time optimization minimizes usage



### Compute Resources[#](#compute-resources)

**Wavefront Execution**: 64 threads in lockstepCK Tile ensures coalesced memory access

Automatic warp-level synchronization


**Matrix Units**: Specialized MFMA instructions16x16x16 operations in 16 cycles

CK Tile can leverage these automatically


**Occupancy**: Balancing threads vs resourcesRegister pressure affects occupancy

CK Tile helps through efficient register use



## Performance Guidelines[#](#performance-guidelines)

To achieve optimal performance with CK Tile:

**Choose appropriate tile sizes**:Match hardware capabilities (e.g., 256x256 for GEMM)

Consider LDS capacity and register pressure


**Align problem dimensions**:Match CU count when possible (304 for MI300)

Use padding for non-aligned sizes


**Enable pipelining**:Use double buffering for latency hiding

CK Tile supports async operations


**Profile and verify**:Use rocprof to check for bottlenecks

Verify bank conflict avoidance

Monitor occupancy and register usage



## Next Steps[#](#next-steps)

Review

[Intro to AMD CDNA Architecture](gpu_basics.html#ck-tile-gpu-basics)for architecture fundamentalsStudy

[Understanding AMD GPU LDS and Bank Conflicts](lds_bank_conflicts.html#ck-tile-lds-bank-conflicts)for shared memory optimizationExplore

[A Block GEMM on MI300](gemm_optimization.html#ck-tile-gemm-optimization)for a complete optimization example

For practical implementation, refer back to the main [CK Tile Conceptual Documentation](../index.html#ck-tile-conceptual) documentation to see how these hardware concepts integrate with CK Tile’s abstractions.
