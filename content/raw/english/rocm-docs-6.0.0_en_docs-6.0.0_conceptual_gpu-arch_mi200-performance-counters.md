---
title: "MI200 performance counters and metrics"
source_url: "https://rocm.docs.amd.com/en/docs-6.0.0/conceptual/gpu-arch/mi200-performance-counters.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T16:10:02.282049+00:00
content_hash: "960a5fac82548169"
---

# MI200 performance counters and metrics[#](#mi200-performance-counters-and-metrics)



This document lists and describes the hardware performance counters and derived metrics available on the AMD Instinct™ MI200 GPU. All the hardware basic counters and derived metrics are accessible via [ROCProfiler tool](https://rocm.docs.amd.com/projects/rocprofiler/en/docs-6.0.0/rocprofv1.html).

## MI200 performance counters list[#](#mi200-performance-counters-list)

See the category-wise listing of MI200 performance counters in the following tables.

Note

Preliminary validation of all MI200 performance counters is in progress. Those with “*” appended to the names require further evaluation.

### Graphics Register Bus Management (GRBM) counters[#](#graphics-register-bus-management-grbm-counters)

Hardware Counter |
Unit |
Definition |
|---|---|---|
|
Cycles |
Number of free-running GPU cycles |
|
Cycles |
Number of GPU active cycles |
|
Cycles |
Number of cycles any of the Command Processor (CP) blocks are busy |
|
Cycles |
Number of cycles any of the Shader Processor Input (SPI) are busy in the shader engine(s) |
|
Cycles |
Number of cycles any of the Texture Addressing Unit (TA) are busy in the shader engine(s) |
|
Cycles |
Number of cycles any of the Texture Cache Blocks (TCP/TCI/TCA/TCC) are busy |
|
Cycles |
Number of cycles the Command Processor - Compute (CPC) is busy |
|
Cycles |
Number of cycles the Command Processor - Fetcher (CPF) is busy |
|
Cycles |
Number of cycles the Unified Translation Cache - Level 2 (UTCL2) block is busy |
|
Cycles |
Number of cycles the Efficiency Arbiter (EA) block is busy |

### Command Processor (CP) counters[#](#command-processor-cp-counters)

The CP counters are further classified into CP-Fetcher (CPF) and CP-Compute (CPC).

#### CPF counters[#](#cpf-counters)

Hardware Counter |
Unit |
Definition |
|---|---|---|
|
Cycles |
Number of cycles one of the Compute UTCL1s is stalled waiting on translation |
|
Cycles |
Number of cycles CPF is busy |
|
Cycles |
Number of cycles CPF is idle |
|
Cycles |
Number of cycles CPF is stalled |
|
Cycles |
Number of cycles CPF Texture Cache Interface Unit (TCIU) interface is busy |
|
Cycles |
Number of cycles CPF TCIU interface is idle |
|
Cycles |
Number of cycles CPF TCIU interface is stalled waiting on free tags |

#### CPC counters[#](#cpc-counters)

Hardware Counter |
Unit |
Definition |
|---|---|---|
|
Cycles |
Number of cycles CPC Micro Engine (ME1) is busy decoding packets |
|
Cycles |
Number of cycles one of the UTCL1s is stalled waiting on translation |
|
Cycles |
Number of cycles CPC is busy |
|
Cycles |
Number of cycles CPC is idle |
|
Cycles |
Number of cycles CPC is stalled |
|
Cycles |
Number of cycles CPC TCIU interface is busy |
|
Cycles |
Number of cycles CPC TCIU interface is idle |
|
Cycles |
Number of cycles CPC UTCL2 interface is busy |
|
Cycles |
Number of cycles CPC UTCL2 interface is idle |
|
Cycles |
Number of cycles CPC UTCL2 interface is stalled |
|
Cycles |
Number of cycles CPC ME1 Processor is busy |

### Shader Processor Input (SPI) counters[#](#shader-processor-input-spi-counters)

Hardware Counter |
Unit |
Definition |
|---|---|---|
|
Cycles |
Number of cycles with outstanding waves |
|
Cycles |
Number of cycles enabled by |
|
Workgroups |
Number of dispatched workgroups |
|
Wavefronts |
Number of dispatched wavefronts |
|
Cycles |
Number of Arb cycles with requests but no allocation |
|
Cycles |
Number of Arb cycles with Compute Shader, n-th pipe (CSn) requests but no CSn allocation |
|
Cycles |
Number of Arb stall cycles due to shortage of CSn pipeline slots |
|
Cycles |
Number of stall cycles due to shortage of temp space |
|
SIMD-cycles |
Accumulated number of Single Instruction Multiple Data (SIMDs) per cycle affected by shortage of wave slots for CSn wave dispatch |
|
SIMD-cycles |
Accumulated number of SIMDs per cycle affected by shortage of VGPR slots for CSn wave dispatch |
|
SIMD-cycles |
Accumulated number of SIMDs per cycle affected by shortage of SGPR slots for CSn wave dispatch |
|
CUs |
Number of Compute Units (CUs) affected by shortage of LDS space for CSn wave dispatch |
|
CUs |
Number of CUs with CSn waves waiting at a BARRIER |
|
CUs |
Number of CUs with CSn waves waiting for BULKY resource |
|
Cycles |
Number of CSn wave stall cycles due to restriction of |
|
Cycles |
Number of cycles CSn is stalled due to WAVE_LIMIT |
|
Qcycles |
Number of quad-cycles taken to initialize Vector General Purpose Register (VGPRs) when launching waves |
|
Qcycles |
Number of quad-cycles taken to initialize Vector General Purpose Register (SGPRs) when launching waves |

### Compute Unit (CU) counters[#](#compute-unit-cu-counters)

The CU counters are further classified into instruction mix, Matrix Fused Multiply Add (MFMA) operation counters, level counters, wavefront counters, wavefront cycle counters and Local Data Share (LDS) counters.

#### Instruction mix[#](#instruction-mix)

Hardware Counter |
Unit |
Definition |
|---|---|---|
|
Instr |
Number of instructions issued. |
|
Instr |
Number of Vector Arithmetic Logic Unit (VALU) instructions including MFMA issued. |
|
Instr |
Number of VALU Half Precision Floating Point (F16) ADD/SUB instructions issued. |
|
Instr |
Number of VALU F16 Multiply instructions issued. |
|
Instr |
Number of VALU F16 Fused Multiply Add (FMA)/ Multiply Add (MAD) instructions issued. |
|
Instr |
Number of VALU F16 Transcendental instructions issued. |
|
Instr |
Number of VALU Full Precision Floating Point (F32) ADD/SUB instructions issued. |
|
Instr |
Number of VALU F32 Multiply instructions issued. |
|
Instr |
Number of VALU F32 FMA/MAD instructions issued. |
|
Instr |
Number of VALU F32 Transcendental instructions issued. |
|
Instr |
Number of VALU F64 ADD/SUB instructions issued. |
|
Instr |
Number of VALU F64 Multiply instructions issued. |
|
Instr |
Number of VALU F64 FMA/MAD instructions issued. |
|
Instr |
Number of VALU F64 Transcendental instructions issued. |
|
Instr |
Number of VALU 32-bit integer instructions (signed or unsigned) issued. |
|
Instr |
Number of VALU 64-bit integer instructions (signed or unsigned) issued. |
|
Instr |
Number of VALU Conversion instructions issued. |
|
Instr |
Number of 8-bit Integer MFMA instructions issued. |
|
Instr |
Number of F16 MFMA instructions issued. |
|
Instr |
Number of Brain Floating Point - 16 (BF16) MFMA instructions issued. |
|
Instr |
Number of F32 MFMA instructions issued. |
|
Instr |
Number of F64 MFMA instructions issued. |
|
Instr |
Number of MFMA instructions issued. |
|
Instr |
Number of Vector Memory (VMEM) Write instructions (including FLAT) issued. |
|
Instr |
Number of VMEM Read instructions (including FLAT) issued. |
|
Instr |
Number of VMEM instructions issued, including both FLAT and Buffer instructions. |
|
Instr |
Number of SALU instructions issued. |
|
Instr |
Number of Scalar Memory (SMEM) instructions issued. |
|
Instr |
Number of SMEM instructions normalized to match |
|
Instr |
Number of FLAT instructions issued. |
|
Instr |
Number of FLAT instructions that read/write only from/to LDS issued. Works only if |
|
Instr |
Number of Local Data Share (LDS) instructions issued (including FLAT). |
|
Instr |
Number of Global Data Share (GDS) instructions issued. |
|
Instr |
Number of EXP and GDS instructions excluding skipped export instructions issued. |
|
Instr |
Number of Branch instructions issued. |
|
Instr |
Number of |
|
Instr |
Number of vector instructions skipped. |

#### MFMA operation counters[#](#mfma-operation-counters)

Hardware Counter |
Unit |
Definition |
|---|---|---|
|
IOP |
Number of 8-bit integer MFMA ops in the unit of 512 |
|
FLOP |
Number of F16 floating MFMA ops in the unit of 512 |
|
FLOP |
Number of BF16 floating MFMA ops in the unit of 512 |
|
FLOP |
Number of F32 floating MFMA ops in the unit of 512 |
|
FLOP |
Number of F64 floating MFMA ops in the unit of 512 |

#### Level counters[#](#level-counters)

Note

All level counters must be followed by `SQ_ACCUM_PREV_HIRES`

counter to measure average latency.

Hardware Counter |
Unit |
Definition |
|---|---|---|
|
Count |
Accumulated counter sample value where accumulation takes place once every four cycles. |
|
Count |
Accumulated counter sample value where accumulation takes place once every cycle. |
|
Waves |
Number of inflight waves. To calculate the wave latency, divide |
|
Instr |
Number of inflight VMEM (including FLAT) instructions. To calculate the VMEM latency, divide |
|
Instr |
Number of inflight SMEM instructions. To calculate the SMEM latency, divide |
|
Instr |
Number of inflight LDS (including FLAT) instructions. To calculate the LDS latency, divide |
|
Instr |
Number of inflight instruction fetch requests from the cache. To calculate the instruction fetch latency, divide |

#### Wavefront counters[#](#wavefront-counters)

Hardware Counter |
Unit |
Definition |
|---|---|---|
|
Waves |
Number of wavefronts dispatched to Sequencers (SQs), including both new and restored wavefronts |
|
Waves |
Number of context-saved waves |
|
Waves |
Number of context-restored waves sent to SQs |
|
Waves |
Number of wavefronts with exactly 64 active threads sent to SQs |
|
Waves |
Number of wavefronts with less than 64 active threads sent to SQs |
|
Waves |
Number of wavefronts with less than 48 active threads sent to SQs |
|
Waves |
Number of wavefronts with less than 32 active threads sent to SQs |
|
Waves |
Number of wavefronts with less than 16 active threads sent to SQs |

#### Wavefront cycle counters[#](#wavefront-cycle-counters)

Hardware Counter |
Unit |
Definition |
|---|---|---|
|
Cycles |
Clock cycles. |
|
Cycles |
Number of cycles while SQ reports it to be busy. |
|
Qcycles |
Number of quad-cycles each CU is busy. |
|
Cycles |
Number of cycles the MFMA ALU is busy. |
|
Qcycles |
Number of quad-cycles spent by waves in the CUs. |
|
Qcycles |
Number of quad-cycles spent waiting for anything. |
|
Qcycles |
Number of quad-cycles spent waiting for any instruction to be issued. |
|
Qcycles |
Number of quad-cycles spent by each wave to work on an instruction. |
|
Qcycles |
Number of quad-cycles spent by the SQ instruction arbiter to work on a VMEM instruction. |
|
Qcycles |
Number of quad-cycles spent by the SQ instruction arbiter to work on an LDS instruction. |
|
Qcycles |
Number of quad-cycles spent by the SQ instruction arbiter to work on a VALU instruction. |
|
Qcycles |
Number of quad-cycles spent by the SQ instruction arbiter to work on a SALU or SMEM instruction. |
|
Qcycles |
Number of quad-cycles spent by the SQ instruction arbiter to work on an EXPORT or GDS instruction. |
|
Qcycles |
Number of quad-cycles spent by the SQ instruction aribter to work on a BRANCH or |
|
Qcycles |
Number of quad-cycles spent by the SQ instruction arbiter to work on a FLAT instruction. |
|
Qcycles |
Number of quad-cycles spent to send addr and cmd data for VMEM Write instructions. |
|
Qcycles |
Number of quad-cycles spent to send addr and cmd data for VMEM Read instructions. |
|
Qcycles |
Number of quad-cycles spent to execute scalar memory reads. |
|
Qcycles |
Number of quad-cycles spent to execute non-memory read scalar operations. |
|
Cycles |
Number of thread-cycles spent to execute VALU operations. This is similar to |
|
Qcycles |
Number of quad-cycles spent waiting for LDS instruction to be issued. |

#### LDS counters[#](#lds-counters)

Hardware Counter |
Unit |
Definition |
|---|---|---|
|
Cycles |
Number of atomic return cycles in LDS |
|
Cycles |
Number of cycles LDS is stalled by bank conflicts |
|
Cycles |
Number of cycles LDS is stalled by address conflicts |
|
Cycles |
Number of cycles LDS is stalled processing flat unaligned load/store ops |
|
Count |
Number of threads that have a memory violation in the LDS |
|
Cycles |
Number of cycles LDS is used for indexed operations |

#### Miscellaneous counters[#](#miscellaneous-counters)

Hardware Counter |
Unit |
Definition |
|---|---|---|
|
Count |
Number of instruction fetch requests from |
|
Threads |
Number of valid items per wave |

### L1I and sL1D cache counters[#](#l1i-and-sl1d-cache-counters)

Hardware Counter |
Unit |
Definition |
|---|---|---|
|
Req |
Number of |
|
Count |
Number of |
|
Count |
Number of non-duplicate |
|
Count |
Number of duplicate |
|
Req |
Number of |
|
Cycles |
Number of cycles while SQ input is valid but sL1D cache is not ready |
|
Count |
Number of |
|
Count |
Number of non-duplicate |
|
Count |
Number of duplicate |
|
Req |
Number of constant cache read requests in a single DW |
|
Req |
Number of constant cache read requests in two DW |
|
Req |
Number of constant cache read requests in four DW |
|
Req |
Number of constant cache read requests in eight DW |
|
Req |
Number of constant cache read requests in 16 DW |
|
Req |
Number of atomic requests |
|
Req |
Number of TC requests that were issued by instruction and constant caches |
|
Req |
Number of instruction requests to the L2 cache |
|
Req |
Number of data Read requests to the L2 cache |
|
Req |
Number of data write requests to the L2 cache |
|
Req |
Number of data atomic requests to the L2 cache |
|
Cycles |
Number of cycles while the valid requests to the L2 cache are stalled |

### Vector L1 cache subsystem[#](#vector-l1-cache-subsystem)

The vector L1 cache subsystem counters are further classified into Texture Addressing Unit (TA), Texture Data Unit (TD), vector L1D cache or Texture Cache per Pipe (TCP), and Texture Cache Arbiter (TCA) counters.

#### TA counters[#](#ta-counters)

Hardware Counter |
Unit |
Definition |
|---|---|---|
|
Cycles |
TA busy cycles. Value range for n: [0-15]. |
|
Instr |
Number of wavefronts processed by TA. Value range for n: [0-15]. |
|
Instr |
Number of buffer wavefronts processed by TA. Value range for n: [0-15]. |
|
Instr |
Number of buffer read wavefronts processed by TA. Value range for n: [0-15]. |
|
Instr |
Number of buffer write wavefronts processed by TA. Value range for n: [0-15]. |
|
Instr |
Number of buffer atomic wavefronts processed by TA. Value range for n: [0-15]. |
|
Cycles |
Number of buffer cycles (including read and write) issued to TC. Value range for n: [0-15]. |
|
Cycles |
Number of coalesced buffer read cycles issued to TC. Value range for n: [0-15]. |
|
Cycles |
Number of coalesced buffer write cycles issued to TC. Value range for n: [0-15]. |
|
Cycles |
Number of cycles TA address path is stalled by TC. Value range for n: [0-15]. |
|
Cycles |
Number of cycles TA data path is stalled by TC. Value range for n: [0-15]. |
|
Cycles |
Number of cycles TA address path is stalled by TD. Value range for n: [0-15]. |
|
Instr |
Number of flat opcode wavefronts processed by TA. Value range for n: [0-15]. |
|
Instr |
Number of flat opcode read wavefronts processed by TA. Value range for n: [0-15]. |
|
Instr |
Number of flat opcode write wavefronts processed by TA. Value range for n: [0-15]. |
|
Instr |
Number of flat opcode atomic wavefronts processed by TA. Value range for n: [0-15]. |

#### TD counters[#](#td-counters)

Hardware Counter |
Unit |
Definition |
|---|---|---|
|
Cycle |
TD busy cycles while it is processing or waiting for data. Value range for n: [0-15]. |
|
Cycle |
Number of cycles TD is stalled waiting for TC data. Value range for n: [0-15]. |
|
Cycle |
Number of cycles TD is stalled by SPI. Value range for n: [0-15]. |
|
Instr |
Number of wavefront instructions (read/write/atomic). Value range for n: [0-15]. |
|
Instr |
Number of write wavefront instructions. Value range for n: [0-15]. |
|
Instr |
Number of atomic wavefront instructions. Value range for n: [0-15]. |
|
Instr |
Number of coalescable wavefronts according to TA. Value range for n: [0-15]. |

#### TCP counters[#](#tcp-counters)

Hardware Counter |
Unit |
Definition |
|---|---|---|
|
Cycles |
Number of cycles vL1D interface clocks are turned on. Value range for n: [0-15]. |
|
Cycles |
Number of cycles vL1D core clocks are turned on. Value range for n: [0-15]. |
|
Cycles |
Number of cycles TD stalls vL1D. Value range for n: [0-15]. |
|
Cycles |
Number of cycles TCR stalls vL1D. Value range for n: [0-15]. |
|
Cycles |
Number of cycles tagram conflict stalls on a read. Value range for n: [0-15]. |
|
Cycles |
Number of cycles tagram conflict stalls on a write. Value range for n: [0-15]. |
|
Cycles |
Number of cycles tagram conflict stalls on an atomic. Value range for n: [0-15]. |
|
Cycles |
Number of cycles vL1D cache is stalled due to data pending from L2 Cache. Value range for n: [0-15]. |
|
Cycles |
Number of cycles TCP stalls TA data interface. |
|
Req |
Number of state reads. Value range for n: [0-15]. |
|
Req |
Number of L1 volatile pixels/buffers from TA. Value range for n: [0-15]. |
|
Req |
Number of vL1D accesses. Equals |
|
Req |
Number of vL1D read accesses. Equals |
|
Req |
Number of vL1D write accesses. |
|
Req |
Number of vL1D atomic requests with return. Value range for n: [0-15]. |
|
Req |
Number of vL1D atomic without return. Value range for n: [0-15]. |
|
Count |
Total number of vL1D writebacks and invalidates. Equals |
|
Req |
Number of address translation requests to UTCL1. Value range for n: [0-15]. |
|
Req |
Number of UTCL1 translation hits. Value range for n: [0-15]. |
|
Req |
Number of UTCL1 translation misses. Value range for n: [0-15]. |
|
Req |
Number of UTCL1 permission misses. Value range for n: [0-15]. |
|
Req |
Number of vL1D cache accesses including hits and misses. Value range for n: [0-15]. |
|
Cycles |
Accumulated wave access latency to vL1D over all wavefronts. Value range for n: [0-15]. |
|
Cycles |
Total vL1D to L2 request latency over all wavefronts for reads and atomics with return. Value range for n: [0-15]. |
|
Cycles |
Total vL1D to L2 request latency over all wavefronts for writes and atomics without return. Value range for n: [0-15]. |
|
Req |
Number of read requests to L2 cache. Value range for n: [0-15]. |
|
Req |
Number of write requests to L2 cache. Value range for n: [0-15]. |
|
Req |
Number of atomic requests to L2 cache with return. Value range for n: [0-15]. |
|
Req |
Number of atomic requests to L2 cache without return. Value range for n: [0-15]. |
|
Req |
Number of NC read requests to L2 cache. Value range for n: [0-15]. |
|
Req |
Number of UC read requests to L2 cache. Value range for n: [0-15]. |
|
Req |
Number of CC read requests to L2 cache. Value range for n: [0-15]. |
|
Req |
Number of RW read requests to L2 cache. Value range for n: [0-15]. |
|
Req |
Number of NC write requests to L2 cache. Value range for n: [0-15]. |
|
Req |
Number of UC write requests to L2 cache. Value range for n: [0-15]. |
|
Req |
Number of CC write requests to L2 cache. Value range for n: [0-15]. |
|
Req |
Number of RW write requests to L2 cache. Value range for n: [0-15]. |
|
Req |
Number of NC atomic requests to L2 cache. Value range for n: [0-15]. |
|
Req |
Number of UC atomic requests to L2 cache. Value range for n: [0-15]. |
|
Req |
Number of CC atomic requests to L2 cache. Value range for n: [0-15]. |
|
Req |
Number of RW atomic requests to L2 cache. Value range for n: [0-15]. |

#### TCA counters[#](#tca-counters)

Hardware Counter |
Unit |
Definition |
|---|---|---|
|
Cycles |
Number of TCA cycles. Value range for n: [0-31]. |
|
Cycles |
Number of cycles TCA has a pending request. Value range for n: [0-31]. |

### L2 cache access counters[#](#l2-cache-access-counters)

L2 Cache is also known as Texture Cache per Channel (TCC).

Hardware Counter |
Unit |
Definition |
|---|---|---|
|
Cycle |
Number of L2 cache free-running clocks. Value range for n: [0-31]. |
|
Cycle |
Number of L2 cache busy cycles. Value range for n: [0-31]. |
|
Req |
Number of L2 cache requests of all types. This is measured at the tag block. This may be more than the number of requests arriving at the TCC, but it is a good indication of the total amount of work that needs to be performed. Value range for n: [0-31]. |
|
Req |
Number of L2 cache streaming requests. This is measured at the tag block. Value range for n: [0-31]. |
|
Req |
Number of NC requests. This is measured at the tag block. Value range for n: [0-31]. |
|
Req |
Number of UC requests. This is measured at the tag block. Value range for n: [0-31]. |
|
Req |
Number of CC requests. This is measured at the tag block. Value range for n: [0-31]. |
|
Req |
Number of RW requests. This is measured at the tag block. Value range for n: [0-31]. |
|
Req |
Number of probe requests. Value range for n: [0-31]. |
|
Req |
Number of external probe requests with |
|
Req |
Number of L2 cache read requests. This includes compressed reads but not metadata reads. Value range for n: [0-31]. |
|
Req |
Number of L2 cache write requests. Value range for n: [0-31]. |
|
Req |
Number of L2 cache atomic requests of all types. Value range for n: [0-31]. |
|
Req |
Number of L2 cache hits. Value range for n: [0-31]. |
|
Req |
Number of L2 cache misses. Value range for n: [0-31]. |
|
Req |
Number of lines written back to the main memory, including writebacks of dirty lines and uncached write/atomic requests. Value range for n: [0-31]. |
|
Req |
Number of 32-byte and 64-byte transactions going over the |
|
Req |
Total number of 64-byte transactions (write or |
|
Req |
Number of 32-byte write/atomic going over the |
|
Cycles |
Number of cycles a write request is stalled. Value range for n: [0-31]. |
|
Cycles |
Number of cycles an EA write request is stalled due to the interface running out of IO credits. Value range for n: [0-31]. |
|
Cycles |
Number of cycles an EA write request is stalled due to the interface running out of GMI credits. Value range for n: [0-31]. |
|
Cycles |
Number of cycles an EA write request is stalled due to the interface running out of DRAM credits. Value range for n: [0-31]. |
|
Cycles |
Number of cycles the L2 cache is unable to send an EA write request due to it reaching its maximum capacity of pending EA write requests. Value range for n: [0-31]. |
|
Req |
The accumulated number of EA write requests in flight. This is primarily intended to measure average EA write latency. Average write latency = |
|
Req |
Number of 32-byte or 64-byte atomic requests going over the |
|
Req |
The accumulated number of EA atomic requests in flight. This is primarily intended to measure average EA atomic latency. Average atomic latency = |
|
Req |
Number of 32-byte or 64-byte read requests to EA. Value range for n: [0-31]. |
|
Req |
Number of 32-byte read requests to EA. Value range for n: [0-31]. |
|
Req |
Number of 32-byte EA reads due to uncached traffic. A 64-byte request is counted as 2. Value range for n: [0-31]. |
|
Cycles |
Number of cycles there is a stall due to the read request interface running out of IO credits. Stalls occur irrespective of the need for a read to be performed. Value range for n: [0-31]. |
|
Cycles |
Number of cycles there is a stall due to the read request interface running out of GMI credits. Stalls occur irrespective of the need for a read to be performed. Value range for n: [0-31]. |
|
Cycles |
Number of cycles there is a stall due to the read request interface running out of DRAM credits. Stalls occur irrespective of the need for a read to be performed. Value range for n: [0-31]. |
|
Req |
The accumulated number of EA read requests in flight. This is primarily intended to measure average EA read latency. Average read latency = |
|
Req |
Number of 32-byte or 64-byte EA read requests to High Bandwidth Memory (HBM). Value range for n: [0-31]. |
|
Req |
Number of 32-byte or 64-byte EA write requests to HBM. Value range for n: [0-31]. |
|
Cycles |
Number of cycles the normal request pipeline in the tag is stalled for any reason. Normally, stalls of this nature are measured exactly at one point in the pipeline however in case of this counter, probes can stall the pipeline at a variety of places and there is no single point that can reasonably measure the total stalls accurately. Value range for n: [0-31]. |
|
Req |
Number of writebacks due to requests that are not writeback requests. Value range for n: [0-31]. |
|
Req |
Number of writebacks due to all |
|
Req |
Number of evictions due to requests that are not invalidate or probe requests. Value range for n: [0-31]. |
|
Req |
Number of evictions due to all |

## MI200 derived metrics list[#](#mi200-derived-metrics-list)

Derived Metric |
Description |
|---|---|
|
Percentage of GPU time ALU units are stalled due to the LDS input queue being full or the output queue not being ready. Reduce this by reducing the LDS bank conflicts or the number of LDS accesses if possible. Value range: 0% (optimal) to 100% (bad). |
|
Total kilobytes fetched from the video memory. This is measured with all extra fetches and any cache or memory effects taken into account. |
|
Average number of FLAT instructions that read from or write to LDS, executed per work item (affected by flow control). |
|
Average number of FLAT instructions that read from or write to the video memory, executed per work item (affected by flow control). Includes FLAT instructions that read from or write to scratch. |
|
Average number of GDS read/write instructions executed per work item (affected by flow control). |
|
Percentage of time GPU is busy. |
|
Percentage of fetch, write, atomic, and other instructions that hit the data in L2 cache. Value range: 0% (no hit) to 100% (optimal). |
|
Percentage of GPU time LDS is stalled by bank conflicts. Value range: 0% (optimal) to 100% (bad). |
|
Average number of LDS read/write instructions executed per work item (affected by flow control). Excludes FLAT instructions that read from or write to LDS. |
|
Percentage of GPU time the memory unit is active. The result includes the stall time ( |
|
Percentage of GPU time the memory unit is stalled. Try reducing the number or size of fetches and writes if possible. Value range: 0% (optimal) to 100% (bad). |
|
Total number of effective 32B write transactions to the memory. |
|
Percentage of GPU time scalar ALU instructions are processed. Value range: 0% (bad) to 100% (optimal). |
|
Average number of scalar ALU instructions executed per work item (affected by flow control). |
|
Average number of scalar fetch instructions from the video memory executed per work item (affected by flow control). |
|
Total number of cycles TA address path is stalled by TC, over all TA instances. |
|
Total number of cycles TA address path is stalled by TD, over all TA instances. |
|
Total number of buffer wavefronts processed by all TA instances. |
|
Total number of buffer read wavefronts processed by all TA instances. |
|
Total number of buffer write wavefronts processed by all TA instances. |
|
Total number of buffer atomic wavefronts processed by all TA instances. |
|
Total number of buffer cycles (including read and write) issued to TC by all TA instances. |
|
Total number of coalesced buffer read cycles issued to TC by all TA instances. |
|
Total number of coalesced buffer write cycles issued to TC by all TA instances. |
|
Average number of busy cycles over all TA instances. |
|
Maximum number of TA busy cycles over all TA instances. |
|
Minimum number of TA busy cycles over all TA instances. |
|
Total number of cycles TA data path is stalled by TC, over all TA instances. |
|
Sum of flat opcode reads processed by all TA instances. |
|
Sum of flat opcode writes processed by all TA instances. |
|
Total number of flat opcode wavefronts processed by all TA instances. |
|
Total number of flat opcode read wavefronts processed by all TA instances. |
|
Total number of flat opcode atomic wavefronts processed by all TA instances. |
|
Total number of TA busy cycles over all TA instances. |
|
Total number of wavefronts processed by all TA instances. |
|
Total number of cycles TCA has a pending request, over all TCA instances. |
|
Total number of cycles over all TCA instances. |
|
Total number of writebacks due to all TC_OP writeback requests, over all TCC instances. |
|
Total number of evictions due to all TC_OP invalidate requests, over all TCC instances. |
|
Total number of L2 cache atomic requests of all types, over all TCC instances. |
|
Average number of L2 cache busy cycles, over all TCC instances. |
|
Total number of L2 cache busy cycles, over all TCC instances. |
|
Total number of CC requests over all TCC instances. |
|
Total number of L2 cache free running clocks, over all TCC instances. |
|
Total number of 32-byte and 64-byte transactions going over the TC_EA_wrreq interface, over all TCC instances. Atomics may travel over the same interface and are generally classified as write requests. This does not include probe commands. |
|
Total number of 64-byte transactions (write or |
|
Total Number of 32-byte write/atomic going over the TC_EA_wrreq interface due to uncached traffic, over all TCC instances. Note that CC mtypes can produce uncached requests, and those are included in this. A 64-byte request is counted as 2. |
|
Total Number of cycles a write request is stalled, over all instances. |
|
Total number of cycles an EA write request is stalled due to the interface running out of IO credits, over all instances. |
|
Total number of cycles an EA write request is stalled due to the interface running out of GMI credits, over all instances. |
|
Total number of cycles an EA write request is stalled due to the interface running out of DRAM credits, over all instances. |
|
Total number of EA write requests in flight over all TCC instances. |
|
Total number of EA read requests in flight over all TCC instances. |
|
Total Number of 32-byte or 64-byte atomic requests going over the TC_EA_wrreq interface, over all TCC instances. |
|
Total number of EA atomic requests in flight, over all TCC instances. |
|
Total number of 32-byte or 64-byte read requests to EA, over all TCC instances. |
|
Total number of 32-byte read requests to EA, over all TCC instances. |
|
Total number of 32-byte EA reads due to uncached traffic, over all TCC instances. |
|
Total number of cycles there is a stall due to the read request interface running out of IO credits, over all TCC instances. |
|
Total number of cycles there is a stall due to the read request interface running out of GMI credits, over all TCC instances. |
|
Total number of cycles there is a stall due to the read request interface running out of DRAM credits, over all TCC instances. |
|
Total number of 32-byte or 64-byte EA read requests to HBM, over all TCC instances. |
|
Total number of 32-byte or 64-byte EA write requests to HBM, over all TCC instances. |
|
Total number of L2 cache hits over all TCC instances. |
|
Total number of L2 cache misses over all TCC instances. |
|
Total number of NC requests over all TCC instances. |
|
Total number of writebacks due to requests that are not writeback requests, over all TCC instances. |
|
Total number of evictions due to requests that are not invalidate or probe requests, over all TCC instances. |
|
Total number of probe requests over all TCC instances. |
|
Total number of external probe requests with EA_TCC_preq_all== 1, over all TCC instances. |
|
Total number of L2 cache read requests (including compressed reads but not metadata reads) over all TCC instances. |
|
Total number of all types of L2 cache requests over all TCC instances. |
|
Total number of RW requests over all TCC instances. |
|
Total number of L2 cache streaming requests over all TCC instances. |
|
Total number of cycles the normal request pipeline in the tag is stalled for any reason, over all TCC instances. |
|
Total number of cycles L2 cache is unable to send an EA write request due to it reaching its maximum capacity of pending EA write requests, over all TCC instances. |
|
Total number of UC requests over all TCC instances. |
|
Total number of L2 cache write requests over all TCC instances. |
|
Total number of lines written back to the main memory including writebacks of dirty lines and uncached write/atomic requests, over all TCC instances. |
|
Maximum number of cycles a write request is stalled, over all TCC instances. |
|
Total number of cycles tagram conflict stalls on an atomic, over all TCP instances. |
|
Total number of cycles vL1D interface clocks are turned on, over all TCP instances. |
|
Total number of cycles vL1D core clocks are turned on, over all TCP instances. |
|
Total number of cycles vL1D cache is stalled due to data pending from L2 Cache, over all TCP instances. |
|
Total number of cycles tagram conflict stalls on a read, over all TCP instances. |
|
Total number of state reads by all TCP instances. |
|
Total number of atomic requests to L2 cache with return, over all TCP instances. |
|
Total number of atomic requests to L2 cache without return, over all TCP instances. |
|
Total number of CC read requests to L2 cache, over all TCP instances. |
|
Total number of CC write requests to L2 cache, over all TCP instances. |
|
Total number of CC atomic requests to L2 cache, over all TCP instances. |
|
Total number of NC read requests to L2 cache, over all TCP instances. |
|
Total number of NC write requests to L2 cache, over all TCP instances. |
|
Total number of NC atomic requests to L2 cache, over all TCP instances. |
|
Total vL1D to L2 request latency over all wavefronts for reads and atomics with return for all TCP instances. |
|
Total number of read requests to L2 cache, over all TCP instances. |
|
Total number of RW read requests to L2 cache, over all TCP instances. |
|
Total number of RW write requests to L2 cache, over all TCP instances. |
|
Total number of RW atomic requests to L2 cache, over all TCP instances. |
|
Total number of UC read requests to L2 cache, over all TCP instances. |
|
Total number of UC write requests to L2 cache, over all TCP instances. |
|
Total number of UC atomic requests to L2 cache, over all TCP instances. |
|
Total vL1D to L2 request latency over all wavefronts for writes and atomics without return for all TCP instances. |
|
Total number of write requests to L2 cache, over all TCP instances. |
|
Total wave access latency to vL1D over all wavefronts for all TCP instances. |
|
Total number of cycles TCR stalls vL1D, over all TCP instances. |
|
Total number of cycles TD stalls vL1D, over all TCP instances. |
|
Total number of vL1D accesses, over all TCP instances. |
|
Total number of vL1D read accesses, over all TCP instances. |
|
Total number of vL1D write accesses, over all TCP instances. |
|
Total number of vL1D atomic requests with return, over all TCP instances. |
|
Total number of vL1D atomic requests without return, over all TCP instances. |
|
Total number of vL1D cache accesses (including hits and misses) by all TCP instances. |
|
Total number of vL1D writebacks and invalidates, over all TCP instances. |
|
Total number of UTCL1 permission misses by all TCP instances. |
|
Total number of address translation requests to UTCL1 by all TCP instances. |
|
Total number of UTCL1 translation misses by all TCP instances. |
|
Total number of UTCL1 translation hits by all TCP instances. |
|
Total number of L1 volatile pixels/buffers from TA, over all TCP instances. |
|
Total number of cycles tagram conflict stalls on a write, over all TCP instances. |
|
Total number of atomic wavefront instructions, over all TD instances. |
|
Total number of coalescable wavefronts according to TA, over all TD instances. |
|
Total number of wavefront instructions (read/write/atomic), over all TD instances. |
|
Total number of cycles TD is stalled by SPI, over all TD instances. |
|
Total number of write wavefront instructions, over all TD instances. |
|
Total number of cycles TD is stalled waiting for TC data, over all TD instances. |
|
Total number of TD busy cycles while it is processing or waiting for data, over all TD instances. |
|
Percentage of GPU time vector ALU instructions are processed. Value range: 0% (bad) to 100% (optimal). |
|
Average number of vector ALU instructions executed per work item (affected by flow control). |
|
Percentage of active vector ALU threads in a wave. A lower number can mean either more thread divergence in a wave or that the work-group size is not a multiple of 64. Value range: 0% (bad), 100% (ideal - no thread divergence). |
|
Average number of vector fetch instructions from the video memory executed per work-item (affected by flow control). Excludes FLAT instructions that fetch from video memory. |
|
Average number of vector write instructions to the video memory executed per work-item (affected by flow control). Excludes FLAT instructions that write to video memory. |
|
Total wavefronts. |
|
Total number of 32-byte effective memory writes. |
|
Total kilobytes written to the video memory. This is measured with all extra fetches and any cache or memory effects taken into account. |
|
Percentage of GPU time the write unit is stalled. Value range: 0% to 100% (bad). |

## Abbreviations[#](#abbreviations)

Abbreviation |
Meaning |
|---|---|
|
Arithmetic Logic Unit |
|
Arbiter |
|
Brain Floating Point - 16 bits |
|
Coherently Cached |
|
Command Processor |
|
Command Processor - Compute |
|
Command Processor - Fetcher |
|
Compute Shader |
|
Compute Shader Controller |
|
Compute Shader, the n-th pipe |
|
Compute Unit |
|
32-bit Data Word, DWORD |
|
Efficiency Arbiter |
|
Half Precision Floating Point |
|
Full Precision Floating Point |
|
FLAT instructions allow read/write/atomic access to a generic memory address pointer, which can resolve to any of the following physical memories: |
|
Fused Multiply Add |
|
Global Data Share |
|
Graphics Register Bus Manager |
|
High Bandwidth Memory |
|
Instructions |
|
Integer Operation |
|
Level-2 Cache |
|
Local Data Share |
|
Micro Engine, running packet processing firmware on CPC |
|
Matrix Fused Multiply Add |
|
Noncoherently Cached |
|
Coherently Cached with Write |
|
Scalar ALU |
|
Scalar General Purpose Register |
|
Single Instruction Multiple Data |
|
Scalar Level-1 Data Cache |
|
Scalar Memory |
|
Shader Processor Input |
|
Sequencer |
|
Texture Addressing Unit |
|
Texture Cache |
|
Texture Cache Arbiter |
|
Texture Cache per Channel, known as L2 Cache |
|
Texture Cache Interface Unit (interface between CP and the memory system) |
|
Texture Cache per Pipe, known as vector L1 Cache |
|
Texture Cache Router |
|
Texture Data Unit |
|
Uncached |
|
Unified Translation Cache - Level 1 |
|
Unified Translation Cache - Level 2 |
|
Vector ALU |
|
Vector General Purpose Register |
|
Vector Level -1 Data Cache |
|
Vector Memory |
