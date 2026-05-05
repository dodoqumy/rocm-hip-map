---
title: "Glossary of rocPRIM terms &#8212; rocPRIM 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocPRIM/en/latest/reference/rocPRIM-glossary.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:17:58.835155+00:00
content_hash: "7d852fc72207964d"
---

# Glossary of rocPRIM terms[#](#glossary-of-rocprim-terms)

This glossary is to help users understand the basic concepts or terminologies used in the rocPRIM library.

- Block
[#](#term-Block) See

[tile](#term-Tile). rocPRIM uses “block” and “tile” interchangeably.- Flat ID
[#](#term-Flat-ID) The flattened block or thread idex. The flat ID is a one-dimensional index created from two-dimensional or three-dimensional indices. For example the flat ID of a two-dimensional thread ID {X, Y} in a two-dimensional

`128x4`

block is`Y*128*X`

.- Grid
[#](#term-Grid) A group of blocks that all run the same kernel call.

- Hardware warp size
[#](#term-Hardware-warp-size) The number of threads in a warp as defined by the hardware. On AMD GPUs, the warp size can be either thirty-two (32) or sixty-four (64) threads.

- Lane ID
[#](#term-Lane-ID) The identifier of the thread within the warp.

- Logical warp size
[#](#term-Logical-warp-size) The number of threads in a warp as defined by the user. This can be equal to or less than the size of the hardware warp size.

- SIMT
[#](#term-SIMT) - Single-Instruction, Multi-Thread
[#](#term-Single-Instruction-Multi-Thread) Single-instruction, multi-thread (SIMT) is a parallel computing model where all the

[work-items](#term-Work-item)within a[wavefront](#term-Wavefront)run the same instruction on different data.- Stride
[#](#term-Stride) The number of threads per block.

- Thread
[#](#term-Thread) See

[work-item](#term-Work-item). rocPrim uses “thread” and “work-item” interchangeably.- Thread ID
[#](#term-Thread-ID) The identifier of the thread within a block.

- Tile
[#](#term-Tile) A group of warps that run on the same streaming multiprocessor (SM). Threads in the block can be indexed using one dimension, {X}, two dimensions, {X, Y}, or three dimensions, {X, Y, Z}. In rocPRIM the tile size is always the same as the block size.

- Warp
[#](#term-Warp) Alternate term for a

[wavefront](#term-Wavefront). rocPRIM uses “warp”, “wave”, and “wavefront” interchangeably.- Warp ID
[#](#term-Warp-ID) The identifier of the warp within a block. A warp’s warp ID is guaranteed to be unique.

- Wave
[#](#term-Wave) See

[wavefront](#term-Wavefront). rocPRIM uses “warp”, “wave”, and “wavefront” interchangeably.- Wavefront
[#](#term-Wavefront) A group of threads that runs using the single instruction, multiple thread (SIMT) model.

- Work-item
[#](#term-Work-item) A work-item is the smallest unit of parallel execution. A work-item runs a single independent instruction stream on a single data element.
