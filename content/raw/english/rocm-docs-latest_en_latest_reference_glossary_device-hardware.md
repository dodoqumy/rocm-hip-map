---
title: "Device hardware glossary"
source_url: "https://rocm.docs.amd.com/en/latest/reference/glossary/device-hardware.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-03T09:01:18.071393+00:00
content_hash: "49f954fcdd47c33c"
---

# Device hardware glossary[#](#device-hardware-glossary)

2026-02-20

9 min read time

This section provides concise definitions of hardware components and architectural features of AMD GPUs.

- AccVGPR
[#](#term-AccVGPR) Accumulation General Purpose Vector Registers (AccVGPRs) are a special type of

[VGPRs](#term-VGPR)used exclusively for matrix operations.- ALU
[#](#term-ALU) Arithmetic logic units (ALUs) are the primary arithmetic engines that execute mathematical and logical operations within

[compute units](#term-Compute-units). See[Vector arithmetic logic unit (VALU)](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/hardware_implementation.html#valu)for details.- AMD device architecture
[#](#term-AMD-device-architecture) AMD device architecture is based on unified, programmable compute engines known as

[compute units (CUs)](#term-Compute-units). See[Hardware implementation](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/hardware_implementation.html#hardware-implementation)for details.- Compute unit versioning
[#](#term-Compute-unit-versioning) [Compute units](#term-Compute-units)are versioned with[GFX IP](#term-GFX-IP)identifiers that define their microarchitectural features and instruction set compatibility. See[Target GPU architectures (GFX IP)](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/compilers.html#gfx-ip)for details.- Compute units
[#](#term-Compute-units) Compute units (CUs) are the fundamental programmable execution engines in AMD GPUs capable of running complex programs. See

[Compute unit architecture](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/hardware_implementation.html#compute-unit)for details.- Data movement engine
[#](#term-Data-movement-engine) Data movement engines (DMEs) are specialized hardware units in AMD Instinct MI300 and MI350 series GPUs that accelerate multi-dimensional tensor data copies between global memory and on-chip memory. See

[Data movement engine (CDNA 3 / CDNA 4)](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/hardware_implementation.html#dme)for details.- GCD
[#](#term-GCD) On AMD Instinct MI100 and MI250 series GPUs and AMD Radeon GPUs, the Graphics Compute Die (GCD) contains the GPU’s computational elements and lower levels of the cache hierarchy. See

[AMD Instinct™ MI250 microarchitecture](../../conceptual/gpu-arch/mi250.html)for details.- GFX IP
[#](#term-GFX-IP) GFX IP (Graphics IP) versions are identifiers that specify which instruction formats, memory models, and compute features are supported by each AMD GPU generation. See

[Target GPU architectures (GFX IP)](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/compilers.html#gfx-ip)for versioning information.- GFX IP major version
[#](#term-GFX-IP-major-version) The

[GFX IP](#term-GFX-IP)major version represents the GPU’s core instruction set and architecture. For example, a GFX IP 11 major version corresponds to the RDNA3 architecture, influencing driver support and available compute features. See[Target GPU architectures (GFX IP)](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/compilers.html#gfx-ip)for versioning information.- GFX IP minor version
[#](#term-GFX-IP-minor-version) The

[GFX IP](#term-GFX-IP)minor version represents specific variations within a[GFX IP](#term-GFX-IP)major version and affects feature sets, optimizations, and driver behavior. Different GPU models within the same major version can have unique capabilities, impacting performance and supported instructions. See[Target GPU architectures (GFX IP)](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/compilers.html#gfx-ip)for versioning information.- GPU RAM (VRAM)
[#](#term-GPU-RAM-VRAM) GPU RAM, also known as

[global memory](device-software.html#term-Global-memory)in the HIP programming model, is the large, high-capacity off-chip memory subsystem accessible by all[compute units](#term-Compute-units), forming the foundation of the device’s[memory hierarchy](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/hardware_implementation.html#hbm).- Graphics L1 cache
[#](#term-Graphics-L1-cache) On AMD Radeon GPUs, the read-only graphics level 1 (L1) cache is local to groups of

[WGPs](#term-WGP)called shader arrays, providing fast access to recently used data. AMD Instinct GPUs do not feature the graphics L1 cache.- Infinity Cache (L3 cache)
[#](#term-Infinity-Cache-L3-cache) On AMD Instinct MI300 and MI350 series GPUs and AMD Radeon GPUs, the Infinity Cache is the last level cache of the cache hierarchy. It is shared by all

[compute units](#term-Compute-units)and[WGPs](#term-WGP)on the GPU.- L0 instruction cache
[#](#term-L0-instruction-cache) On AMD Radeon GPUs, the level 0 (L0) instruction cache is local to each

[WGP](#term-WGP)and thus shared between the WGP’s[compute units](#term-Compute-units).- L0 scalar cache
[#](#term-L0-scalar-cache) On AMD Radeon GPUs, the level 0 (L0) scalar data cache is local to each

[WGP](#term-WGP)and thus shared between the WGP’s[compute units](#term-Compute-units). It provides the[scalar ALU](#term-SALU)with fast access to recently used data.- L0 vector cache
[#](#term-L0-vector-cache) On AMD Radeon GPUs, the level 0 (L0) vector data cache is local to each

[WGP](#term-WGP)and thus shared between the WGP’s[compute units](#term-Compute-units). It provides the[vector ALU](#term-VALU)with fast access to recently used data.- L1 instruction cache
[#](#term-L1-instruction-cache) On AMD Instinct GPUs, the level 1 (L1) instruction cache is local to each

[compute unit](#term-Compute-units). On AMD Radeon GPUs, the L1 instruction cache does not exist as a separate cache level, and instructions are stored in the[L0 instruction cache](#term-L0-instruction-cache).- L1 scalar cache
[#](#term-L1-scalar-cache) On AMD Instinct GPUs, the level 1 (L1) scalar data cache is local to each

[compute unit](#term-Compute-units), providing the[scalar ALU](#term-SALU)with fast access to recently used data. On AMD Radeon GPUs, the L1 scalar cache does not exist as a separate cache level, and recently used scalar data is stored in the[L0 scalar cache](#term-L0-scalar-cache).- L1 vector cache
[#](#term-L1-vector-cache) On AMD Instinct GPUs, the level 1 (L1) vector data cache is local to each

[compute unit](#term-Compute-units), providing the[vector ALU](#term-VALU)with fast access to recently used data. On AMD Radeon GPUs, the L1 vector cache does not exist as a separate cache level, and recently used vector data is stored in the[L0 vector cache](#term-L0-vector-cache).- L2 cache
[#](#term-L2-cache) On AMD Instinct MI100 series GPUs, the L2 cache is shared across the entire chip, while for all other AMD GPUs the L2 caches are shared by the

[compute units](#term-Compute-units)on the same[GCD](#term-GCD)or[XCD](#term-XCD).- Load/store unit
[#](#term-Load-store-unit) Load/store units (LSUs) handle data transfer between

[compute units](#term-Compute-units)and the GPU’s memory subsystems, managing thousands of concurrent memory operations. See[Load/store unit (LSU)](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/hardware_implementation.html#lsu)for details.Local data share (LDS) is fast on-chip memory local to each

[compute unit](#term-Compute-units)and shared among[work-items](#term-Work-item-Thread)in a[work-group](#term-Work-group-Block), enabling efficient coordination and data reuse. In the HIP programming model, the LDS is known as shared memory. See[Local data share (LDS)](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/hardware_implementation.html#lds)for LDS programming details.- Matrix cores (MFMA units)
[#](#term-Matrix-cores-MFMA-units) Matrix cores (MFMA units) are specialized execution units that perform large-scale matrix operations in a single instruction, delivering high throughput for AI and HPC workloads. See

[Matrix fused multiply-add (MFMA)](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/hardware_implementation.html#mfma-units)for details.- Register file
[#](#term-Register-file) The register file is the primary on-chip memory store in each

[compute unit](#term-Compute-units), holding data between arithmetic and memory operations. See[Memory model](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/programming_model.html#memory-hierarchy)for details.- Registers
[#](#term-Registers) Registers are the lowest level of the memory hierarchy, storing per-thread temporary variables and intermediate results. See

[Memory model](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/programming_model.html#memory-hierarchy)for register usage details.- SALU
[#](#term-SALU) Scalar

[ALUs](#term-ALU)(SALUs) operate on a single value per[wavefront](https://rocm.docs.amd.com/projects/rocPRIM/en/latest/reference/rocPRIM-glossary.html#term-Wavefront)and manage all control flow.- SGPR
[#](#term-SGPR) Scalar general-purpose

[registers](#term-Registers)(SGPRs) hold data produced and consumed by a[compute unit](#term-Compute-units)’s[scalar ALU](#term-SALU).- SGPR file
[#](#term-SGPR-file) The

[SGPR](#term-SGPR)file is the[register file](#term-Register-file)that holds data used by the[scalar ALU](#term-SALU).- SIMD core
[#](#term-SIMD-core) SIMD cores are execution lanes that perform scalar and vector arithmetic operations inside each

[compute unit](https://rocm.docs.amd.com/projects/composable_kernel/en/latest/reference/Composable-Kernel-Glossary.html#term-compute-unit). See[CDNA architecture](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/hardware_implementation.html#cdna-architecture)and[RDNA architecture](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/hardware_implementation.html#rdna-architecture)for details.- Special function unit
[#](#term-Special-function-unit) Special function units (SFUs) accelerate transcendental and reciprocal mathematical functions such as

`exp`

,`log`

,`sin`

, and`cos`

. See[Special function unit (SFU)](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/hardware_implementation.html#sfu)for details.- VALU
[#](#term-VALU) Vector

[ALUs](#term-ALU)(VALUs) perform an arithmetic or logical operation on data for each[work-item](#term-Work-item-Thread)in a[wavefront](https://rocm.docs.amd.com/projects/rocPRIM/en/latest/reference/rocPRIM-glossary.html#term-Wavefront), enabling data-parallel execution.- VGPR
[#](#term-VGPR) Vector general-purpose

[registers](#term-Registers)(VGPRs) hold data produced and consumed by a[compute unit](#term-Compute-units)’s[vector ALU](#term-VALU).- VGPR file
[#](#term-VGPR-file) The

[VGPR](#term-VGPR)file is the[register file](#term-Register-file)that holds data used by the[vector ALU](#term-VALU). GPUs with[matrix cores](#term-Matrix-cores-MFMA-units)also have[AccVGPR](#term-AccVGPR)files, used specifically for matrix instructions.- Wavefront (Warp)
[#](#term-Wavefront-Warp) A wavefront (also called a warp) is a group of

[work-items](#term-Work-item-Thread)that execute in parallel on a single[compute unit](#term-Compute-units), sharing one instruction stream. See[Warp (or Wavefront)](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/programming_model.html#wavefront)for execution details.- Wavefront scheduler
[#](#term-Wavefront-scheduler) The wavefront scheduler in each

[compute unit](#term-Compute-units)decides which[wavefront](https://rocm.docs.amd.com/projects/composable_kernel/en/latest/reference/Composable-Kernel-Glossary.html#term-wavefront)to execute each clock cycle, enabling rapid context switching for latency hiding. See[Sequencer and scheduling](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/hardware_implementation.html#wave-scheduling)for details.- Wavefront size
[#](#term-Wavefront-size) The wavefront size is the number of

[work-items](#term-Work-item-Thread)that execute together in a single[wavefront](#term-Wavefront-Warp). For AMD Instinct GPUs, the wavefront size is 64 threads, while AMD Radeon GPUs have a wavefront size of 32 threads. See[Warp (or Wavefront)](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/programming_model.html#wavefront)for details.- WGP
[#](#term-WGP) A Workgroup Processor (WGP) is a hardware unit on AMD Radeon GPUs that contains two

[compute units](#term-Compute-units)and their associated resources, enabling efficient scheduling and execution of[wavefronts](https://rocm.docs.amd.com/projects/composable_kernel/en/latest/reference/Composable-Kernel-Glossary.html#term-wavefront). See[RDNA architecture](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/hardware_implementation.html#rdna-architecture)for details.- Work-group (Block)
[#](#term-Work-group-Block) A work-group (also called a block) is a collection of

[wavefronts](#term-Wavefront-Warp)scheduled together on a single[compute unit](#term-Compute-units)that can coordinate through[Local data share](#term-Local-data-share)memory. See[Block (Work-group)](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/programming_model.html#inherent-thread-hierarchy-block)for work-group details.- Work-item (Thread)
[#](#term-Work-item-Thread) A work-item (also called a thread) is the smallest unit of execution on an AMD GPU and represents a single element of work. See

[Thread (Work-item)](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/programming_model.html#work-item)for thread hierarchy details.- XCD
[#](#term-XCD) On AMD Instinct MI300 and MI350 series GPUs, the Accelerator Complex Die (XCD) contains the GPU’s computational elements and lower levels of the cache hierarchy. See

[AMD Instinct™ MI300 Series microarchitecture](../../conceptual/gpu-arch/mi300.html)for details.
