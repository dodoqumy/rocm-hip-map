---
title: "Intro to AMD CDNA Architecture &#8212; Composable Kernel 1.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/composable_kernel/en/latest/conceptual/ck_tile/hardware/gpu_basics.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-03T03:09:31.801967+00:00
content_hash: "0692a4d75b411420"
---

# Intro to AMD CDNA Architecture[#](#intro-to-amd-cdna-architecture)

The AMD CDNA architecture is a specialized GPU design for high-performance computing (HPC) and AI workloads. Unlike the RDNA architecture used in gaming GPUs, CDNA is optimized for data center tasks, prioritizing compute density, memory bandwidth, and scalability. This is achieved through several key architectural features.

For more information about the AMD GPU architecture, see the [GPU architecture documentation](https://rocm.docs.amd.com/en/latest/conceptual/gpu-arch.html).

## Implications for CK Tile[#](#implications-for-ck-tile)

Understanding the CDNA architecture is crucial for effective use of CK Tile:

**Thread Organization**: CK Tile’s hierarchical[Thread Mapping - Connecting to Hardware](../thread_mapping.html#ck-tile-thread-mapping)(blocks → warps → threads) directly maps to CDNA’s hardware organization.**Memory Hierarchy**: CK Tile’s[Buffer Views - Raw Memory Access](../buffer_views.html#ck-tile-buffer-views)and[Tile Window - Data Access Gateway](../tile_window.html#ck-tile-tile-window)are designed to efficiently utilize the L2, Infinity Cache, and LDS hierarchy.**Register Pressure**: CK Tile’s compile-time optimizations help minimize VGPR usage, preventing spills to slower memory.**Warp Execution**: CK Tile’s[Tile Distribution - The Core API](../tile_distribution.html#ck-tile-tile-distribution)ensures that threads within a warp access contiguous memory for optimal SIMD execution.**LDS Utilization**: CK Tile’s[Static Distributed Tensor](../static_distributed_tensor.html#ck-tile-static-distributed-tensor)and[Tile Window - Data Access Gateway](../tile_window.html#ck-tile-tile-window)make effective use of the 64KB LDS per CU.

By understanding these architectural features, developers can better appreciate how CK Tile’s abstractions map to hardware capabilities and why certain design decisions were made in the framework.

Related Topics

[Thread Mapping - Connecting to Hardware](../thread_mapping.html#ck-tile-thread-mapping)- How threads are organized and mapped to hardware[Coordinate Systems - The Mathematical Foundation](../coordinate_systems.html#ck-tile-coordinate-systems)- Mathematical foundation for data distribution[Understanding AMD GPU LDS and Bank Conflicts](lds_bank_conflicts.html#ck-tile-lds-bank-conflicts)- Optimizing shared memory access patterns[LoadStoreTraits - Memory Access Optimization Engine](../load_store_traits.html#ck-tile-load-store-traits)- Memory access optimization strategies[A Block GEMM on MI300](gemm_optimization.html#ck-tile-gemm-optimization)- Practical application of architecture knowledge
