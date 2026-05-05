---
title: "Performance analysis glossary"
source_url: "https://rocm.docs.amd.com/en/latest/reference/glossary/performance.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-03T15:01:00.123579+00:00
content_hash: "7e1c76b1534efe67"
---

# Performance analysis glossary[#](#performance-analysis-glossary)

2026-02-20

5 min read time

This section provides brief definitions of performance analysis concepts and optimization techniques.

- Active cycle
[#](#term-Active-cycle) An active cycle is a clock cycle in which a

[compute unit](device-hardware.html#term-Compute-units)has at least one active[wavefront](https://rocm.docs.amd.com/projects/rocPRIM/en/latest/reference/rocPRIM-glossary.html#term-Wavefront)resident. See[Warp (Wavefront) execution states](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#wavefront-execution)for details.- Arithmetic bandwidth
[#](#term-Arithmetic-bandwidth) Arithmetic bandwidth is the peak rate at which arithmetic work can be performed, defining the compute roof in

[roofline models](#term-Roofline-model). See[Compute-bound performance](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#compute-bound)for details.- Arithmetic intensity
[#](#term-Arithmetic-intensity) Arithmetic intensity is the ratio of arithmetic operations to memory operations in a kernel, and determines performance characteristics. See

[Arithmetic intensity](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#arithmetic-intensity)for intensity analysis.- Bank conflict
[#](#term-Bank-conflict) A bank conflict occurs when multiple threads simultaneously access different addresses in the same

[LDS bank](device-hardware.html#term-Local-data-share), serializing accesses. See[Bank conflict theory](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#bank-conflicts-theory)for details.- Branch efficiency
[#](#term-Branch-efficiency) Branch efficiency measures how often all threads within a

[wavefront](https://rocm.docs.amd.com/projects/rocPRIM/en/latest/reference/rocPRIM-glossary.html#term-Wavefront)take the same execution path, quantifying control-flow uniformity. See[Branch efficiency](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#branch-efficiency)for branch analysis.- Compute-bound
[#](#term-Compute-bound) Compute-bound kernels are limited by the

[arithmetic bandwidth](#term-Arithmetic-bandwidth)of the GPU’s[compute units](device-hardware.html#term-Compute-units)rather than[memory bandwidth](#term-Memory-bandwidth). See[Compute-bound performance](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#compute-bound)for compute-bound analysis.- CU utilization
[#](#term-CU-utilization) CU utilization measures the percentage of time that

[compute units](device-hardware.html#term-Compute-units)are actively executing instructions. See[CU utilization](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#cu-utilization)for utilization analysis.- Issue efficiency
[#](#term-Issue-efficiency) Issue efficiency measures how effectively the

[wavefront scheduler](device-hardware.html#term-Wavefront-scheduler)keeps execution pipelines busy by issuing instructions. See[Issue efficiency](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#issue-efficiency)for efficiency metrics.- Latency hiding
[#](#term-Latency-hiding) Latency hiding masks long-latency operations by running many concurrent threads, keeping execution pipelines busy. See

[Latency hiding mechanisms](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#latency-hiding)for details.- Little’s Law
[#](#term-Little-s-Law) Little’s Law relates concurrency, latency, and throughput, determining how much independent work must be in flight to hide latency. See

[Little’s Law](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#littles-law)for latency hiding details.- Memory bandwidth
[#](#term-Memory-bandwidth) Memory bandwidth is the maximum rate at which data can be transferred between memory hierarchy levels, typically measured in bytes per second. See

[Memory-bound performance](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#memory-bound)for details.- Memory coalescing
[#](#term-Memory-coalescing) Memory coalescing improves

[memory bandwidth](#term-Memory-bandwidth)by servicing many logical loads or stores with fewer physical memory transactions. See[Memory coalescing theory](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#memory-coalescing-theory)for coalescing patterns.- Memory-bound
[#](#term-Memory-bound) Memory-bound kernels are limited by

[memory bandwidth](#term-Memory-bandwidth)rather than[arithmetic bandwidth](#term-Arithmetic-bandwidth), typically due to low[arithmetic intensity](#term-Arithmetic-intensity). See[Memory-bound performance](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#memory-bound)for memory-bound analysis.- Occupancy
[#](#term-Occupancy) Occupancy is the ratio of active

[wavefronts](https://rocm.docs.amd.com/projects/rocPRIM/en/latest/reference/rocPRIM-glossary.html#term-Wavefront)to the maximum number of wavefronts that can be active on a[compute unit](device-hardware.html#term-Compute-units). See[Occupancy theory](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#occupancy)for occupancy analysis.- Overhead
[#](#term-Overhead) Overhead latency is the time spent with no useful work being done, often due to CPU-side bottlenecks or kernel launch delays. See

[Performance bottlenecks](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#performance-bottlenecks)for details.- Peak rate
[#](#term-Peak-rate) Peak rate is the theoretical maximum throughput at which a hardware system can complete work under ideal conditions. See

[Theoretical performance limits](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#theoretical-performance-limits)for details.- Pipe utilization
[#](#term-Pipe-utilization) Pipe utilization measures how effectively a kernel uses the execution pipelines within each

[compute unit](device-hardware.html#term-Compute-units). See[Pipe utilization](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#pipe-utilization)for utilization details.- Register pressure
[#](#term-Register-pressure) Register pressure occurs when excessive register demand limits the number of active

[wavefronts](https://rocm.docs.amd.com/projects/rocPRIM/en/latest/reference/rocPRIM-glossary.html#term-Wavefront)per[compute unit](device-hardware.html#term-Compute-units), reducing[occupancy](#term-Occupancy). See[Register pressure theory](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#register-pressure-theory)for details.- Roofline model
[#](#term-Roofline-model) The roofline model is a visual performance model that determines whether a program is

[compute-bound](#term-Compute-bound)or[memory-bound](#term-Memory-bound). See[Roofline model](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#roofline-model)for roofline analysis.- Wavefront divergence
[#](#term-Wavefront-divergence) Wavefront divergence occurs when threads within a

[wavefront](https://rocm.docs.amd.com/projects/rocPRIM/en/latest/reference/rocPRIM-glossary.html#term-Wavefront)take different execution paths due to conditional statements. See[Branch efficiency](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#branch-efficiency)for divergence handling details.- Wavefront execution state
[#](#term-Wavefront-execution-state) Wavefront execution states (

*active*,*stalled*,*eligible*,*selected*) describe the scheduling status of[wavefronts](https://rocm.docs.amd.com/projects/rocPRIM/en/latest/reference/rocPRIM-glossary.html#term-Wavefront)on AMD GPUs. See[Warp (Wavefront) execution states](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html#wavefront-execution)for state definitions.
