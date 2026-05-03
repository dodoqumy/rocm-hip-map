---
title: "Composable Kernel glossary &#8212; Composable Kernel 1.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/composable_kernel/en/latest/reference/Composable-Kernel-Glossary.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-03T00:10:04.963601+00:00
content_hash: "15fe824c0300cd4f"
---

# Composable Kernel glossary[#](#composable-kernel-glossary)

- Add+Multiply
[#](#term-Add-Multiply) See

[fused add multiply](#term-fused-add-multiply).- alignment
[#](#term-alignment) Alignment is a memory management strategy where data structures are stored at addresses that are multiples of a specific value.

- arithmetic logic unit
[#](#term-arithmetic-logic-unit) The arithmetic logic unit (ALU) is the GPU component responsible for arithmetic and logic operations.

- bank conflict
[#](#term-bank-conflict) A bank conflict occurs when multiple

[work-items](#term-work-item)in a[wavefront](#term-wavefront)access different addresses that map to the same shared memory bank.- batched GEMM
[#](#term-batched-GEMM) A

[kernel](#term-kernel)that calls[VGEMMs](#term-naive-GEMM)with different batches of data. All the data batches have the same[problem shape](#term-problem-shape).- block Size
[#](#term-block-Size) The block size is the number of

[work-items](#term-work-item)in a[compute unit](#term-compute-unit).- block tile
[#](#term-block-tile) A block tile is a memory

[tile](#term-tile)processed by a[work group](#term-work-group).- Col2Im
[#](#term-Col2Im) Col2Im is a data transformation technique that converts column data to image format.

- compute unit
[#](#term-compute-unit) The compute unit (CU) is the parallel vector processor in an AMD GPU with multiple

[ALUs](#term-arithmetic-logic-unit). Each compute unit will run all the[wavefronts](#term-wavefront)in a[work group](#term-work-group). A compute unit is equivalent to NVIDIA’s streaming multiprocessor.- coordinate transformation primitives
[#](#term-coordinate-transformation-primitives) Coordinate transformation primitives are Composable Kernel utilities for converting between different coordinate systems.

- dense tensor
[#](#term-dense-tensor) A dense tensor is a tensor where most of its elements are non-zero. Dense tensors are typically stored in a contiguous block of memory.

- descriptor
[#](#term-descriptor) Metadata structure that defines

[tile](#term-tile)properties, memory layouts, and coordinate transformations for Composable Kernel[operations](#term-operation).- device
[#](#term-device) Device refers to the GPU hardware that runs parallel kernels. The device contains the

[compute units](#term-compute-unit), memory hierarchy, and specialized accelerators.- dilation
[#](#term-dilation) Dilation is the spacing between

[kernel](#term-kernel)elements in convolution[operations](#term-operation), allowing the receptive field to grow without increasing kernel size.- elementwise
[#](#term-elementwise) An elementwise

[operation](#term-operation)is an operation applied to each tensor element independently.- epilogue
[#](#term-epilogue) The epilogue is the final stage of a kernel. Activation functions, bias, and other post-processing steps are applied in the epilogue.

- fast changing dimension
[#](#term-fast-changing-dimension) The fast changing dimension is the innermost dimension in memory layout.

- fused add multiply
[#](#term-fused-add-multiply) A common fused

[operation](#term-operation)in machine language and linear algebra, where an[elementwise](#term-elementwise)addition is immediately followed by a multiplication. Fused add multiply is often used for bias and scaling in neural network layers.- GEMM
[#](#term-GEMM) - GEMV
[#](#term-GEMV) - general matrix multiply
[#](#term-general-matrix-multiply) A general matrix multiply (GEMM) is a Core matrix

[operation](#term-operation)in linear algebra and deep learning. A GEMM is defined as \(C = {\alpha}AB + {\beta}C\), where \(A\), \(B\), and \(C\) are matrices, and \(\alpha\) and \(\beta\) are scalars.- general matrix vector multiplication
[#](#term-general-matrix-vector-multiplication) General matrix vector multiplication (GEMV) is an

[operation](#term-operation)where a matrix is multiplied by a vector, producing another vector.- GGEMM
[#](#term-GGEMM) See

[grouped GEMM](#term-grouped-GEMM).- global memory
[#](#term-global-memory) The main device memory accessible by all threads, offering high capacity but higher latency than shared memory.

- grid
[#](#term-grid) A grid is a collection of

[work groups](#term-work-group)that run a kernel. Each work group within the grid operates independently and can be scheduled on a different[compute unit](#term-compute-unit). A grid can be organized into one, two, or three dimensions. A grid is equivalent to an NVIDIA thread block.- grouped GEMM
[#](#term-grouped-GEMM) A

[kernel](#term-kernel)that calls multiple[VGEMMs](#term-naive-GEMM). Each call can have a different[problem shape](#term-problem-shape).- host
[#](#term-host) Host refers to the CPU and the main memory system that manages GPU execution. The host is responsible for launching kernels, transferring data, and coordinating overall computation.

- host-device transfer
[#](#term-host-device-transfer) A host-device transfer is the process of moving data between

[host](#term-host)and[device](#term-device)memory.- Im2Col
[#](#term-Im2Col) Im2Col is a data transformation technique that converts image data to column format.

- inner dimension
[#](#term-inner-dimension) The inner dimension is the faster-changing dimension in memory layout.

- input
[#](#term-input) See

[problem shape](#term-problem-shape).- kernel
[#](#term-kernel) A kernel is a function that runs an

[operation](#term-operation)or a collection of operations. A kernel will run in parallel on several[work-items](#term-work-item)across the GPU. In Composable Kernel, kernels require[pipelines](#term-pipeline).- launch parameters
[#](#term-launch-parameters) Launch parameters are the configuration values, such as

[grid](#term-grid)and[block size](#term-block-Size), that determine how a[kernel](#term-kernel)is mapped to hardware resources.- LDS
[#](#term-LDS) See

[local data share](#term-local-data-share).- LDS banks
[#](#term-LDS-banks) LDS banks are a type of memory organization where consecutive addresses are distributed across multiple memory banks for parallel access. LDS banks are used to prevent memory access conflicts and improve bandwidth when LDS is used.

- load tile
[#](#term-load-tile) Load tile is an operation that transfers data from

[global memory](#term-global-memory)or the[local data share](#term-local-data-share)to[vector general purpose registers](#term-vector-general-purpose-register).Local data share (LDS) is high-bandwidth, low-latency on-chip memory accessible to all the

[work-items](#term-work-item)in a[work group](#term-work-group). LDS is equivalent to NVIDIA’s shared memory.- matrix core
[#](#term-matrix-core) A matrix core is a specialized GPU unit that accelerate matrix operations for AI and deep learning tasks. A GPU contains multiple matrix cores.

- matrix fused multiply-add
[#](#term-matrix-fused-multiply-add) Matrix fused multiply-add (MFMA) is a

[matrix core](#term-matrix-core)instruction for GEMM[operations](#term-operation).- memory coalescing
[#](#term-memory-coalescing) Memory coalescing is an optimization strategy where consecutive

[work-items](#term-work-item)access consecutive memory addresses in such a way that a single memory transaction serves multiple work-items.- MFMA
[#](#term-MFMA) - naive GEMM
[#](#term-naive-GEMM) The naive GEMM, sometimes referred to as a vanilla GEMM or VGEMM, is the simplest form of

[GEMM](#term-GEMM)in Composable Kernel. The naive GEMM is defined as \(C = AB\), where \(A\), \(B\), and \(C\) are matrices. The naive GEMM is the baseline GEMM that all other GEMM[operations](#term-operation)build on.- occupancy
[#](#term-occupancy) The ratio of active

[wavefronts](#term-wavefront)to the maximum possible number of wavefronts.- operation
[#](#term-operation) An operation is a computation on input data.

- outer dimension
[#](#term-outer-dimension) The outer dimension is the slower-changing dimension in memory layout.

- padding
[#](#term-padding) Padding is the addition of extra elements, often zeros, to tensor edges in order to control output size in convolution and pooling, or to align data for memory access.

- permute
[#](#term-permute) Permute is an

[operation](#term-operation)that rearranges the order of tensor axes, often for the purposes of matching[kernel](#term-kernel)input formats or optimize memory access patterns.- pinned memory
[#](#term-pinned-memory) Pinned memory is

[host](#term-host)memory that is page-locked to accelerate transfers between the CPU and GPU.- pipeline
[#](#term-pipeline) A Composable Kernel pipeline schedules the sequence of operations for a

[kernel](#term-kernel), such as the data loading, computation, and storage phases. A pipeline consists of a[problem](#term-problem)and a[policy](#term-policy).- policy
[#](#term-policy) The policy is the part of the

[pipeline](#term-pipeline)that defines memory access patterns and hardware-specific optimizations.- problem
[#](#term-problem) The problem is the part of the

[pipeline](#term-pipeline)that defines input and output shapes, data types, and mathematical[operations](#term-operation).- problem shape
[#](#term-problem-shape) The problem shape defines the dimensions and data types of input tensors that define the

[problem](#term-problem).- reference kernel
[#](#term-reference-kernel) A reference

[kernel](#term-kernel)is a baseline kernel implementation used to verify correctness and performance. Composable Kernel makes two reference kernels, one for CPU and one for GPU, available.- register
[#](#term-register) Registers are the fastest tier of memory. They’re used for storing temporary values during computations and are private to the

[work-items](#term-work-item)that use them.- scalar general purpose register
[#](#term-scalar-general-purpose-register) A scalar general purpose register (SGPR) is a

[register](#term-register)shared by all the[work-items](#term-work-item)in a[wave](#term-wavefront). SGPRs are used for constants, addresses, and control flow common across the entire wave.- SGPR
[#](#term-SGPR) - SIMD
[#](#term-SIMD) - SIMT
[#](#term-SIMT) - single-instruction, multi-data
[#](#term-single-instruction-multi-data) Single-instruction, multi-data (SIMD) is a parallel computing model where the same instruction is run with different data simultaneously.

- single-instruction, multi-thread
[#](#term-single-instruction-multi-thread) Single-instruction, multi-thread (SIMT) is a parallel computing model where all the

[work-items](#term-work-item)within a[wavefront](#term-wavefront)run the same instruction on different data.- sparse tensor
[#](#term-sparse-tensor) A sparse tensor is a tensor where most of its elements are zero. Typically only the non-zero elements of a sparse tensor and their indices are stored.

- Split-K GEMM
[#](#term-Split-K-GEMM) Split-K GEMM is a parallelization strategy that partitions the reduction dimension (K) of a

[GEMM](#term-GEMM)across multiple[compute units](#term-compute-unit), increasing parallelism for large matrix multiplications.- store tile
[#](#term-store-tile) Store tile is an operation that transfers data from

[vector general purpose registers](#term-vector-general-purpose-register)to[global memory](#term-global-memory)or the[local data share](#term-local-data-share).- stride
[#](#term-stride) A stride is the step size to move from one element to the next in a specific dimension of a tensor or matrix. In convolution and pooling, the stride determines how far the

[kernel](#term-kernel)moves at each step.- tile
[#](#term-tile) A tile is a sub-region of a tensor or matrix that is processed by a

[work group](#term-work-group)or[work-item](#term-work-item). Rectangular data blocks are the unit of computation and memory transfer in Composable Kernel, and are the basis for tiled algorithms.- tile distribution
[#](#term-tile-distribution) The tile distribution is the hierarchical data mapping from

[work-items](#term-work-item)to data in memory.- tile partitioner
[#](#term-tile-partitioner) The tile partitioner defines the mapping between the

[problem](#term-problem)dimensions and GPU hierarchy. It specifies[work group](#term-work-group)-level[tile](#term-tile)sizes and determines[grid](#term-grid)dimensions by dividing the problem size by the tile sizes.- tile programming API
[#](#term-tile-programming-API) The

[tile](#term-tile)programming API is Composable Kernel’s high-level interface for defining tile-based computations with predefined hardware mappings for data loading and storing.- tile window
[#](#term-tile-window) Viewport into a larger tensor that defines the current tile’s position and boundaries for computation.

- transpose
[#](#term-transpose) Transpose is an

[operation](#term-operation)that rearranges the order of tensor axes, often for the purposes of matching[kernel](#term-kernel)input formats or optimize memory access patterns.- user customized tile pipeline
[#](#term-user-customized-tile-pipeline) A customized

[tile](#term-tile)[pipeline](#term-pipeline)that combines custom[problem](#term-problem)and[policy](#term-policy)components for specialized computations.- user customized tile pipeline optimization
[#](#term-user-customized-tile-pipeline-optimization) The process of tuning the

[tile](#term-tile)size, memory access pattern, and hardware utilization for specific workloads.- vanilla GEMM
[#](#term-vanilla-GEMM) See

[naive GEMM](#term-naive-GEMM).- vector
[#](#term-vector) The vector is the smallest data unit processed by an individual

[work-item](#term-work-item). A vectors is typically four to sixteen elements, depending on data type and hardware.- vector general purpose register
[#](#term-vector-general-purpose-register) A vector general purpose register (VGPR) is a

[register](#term-register)that stores individual thread data. Each thread in a[wave](#term-wavefront)has its own set of VGPRs for private variables and calculations.- VGEMM
[#](#term-VGEMM) See

[naive GEMM](#term-naive-GEMM).- VGPR
[#](#term-VGPR) - wave tile
[#](#term-wave-tile) A wave

[tile](#term-tile)is a sub-tile processed by a single[wavefront](#term-wavefront)within a[work group](#term-work-group). The wave tile is the base level granularity of a[single-instruction, multi-thread (SIMD)](#term-single-instruction-multi-thread)model.- wavefront
[#](#term-wavefront) Also referred to as a wave, a wavefront is a group of

[work-items](#term-work-item)that run the same instruction. A wavefront is equivalent to an NVIDIA warp.- work group
[#](#term-work-group) A work group is a collection of

[work-items](#term-work-item)that can synchronize and share memory. A work group is equivalent to NVIDIA’s thread block.- work-item
[#](#term-work-item) A work-item is the smallest unit of parallel execution. A work-item runs a single independent instruction stream on a single data element. A work-item is equivalent to an NVIDIA thread.
