---
title: "Tensor Descriptors - Complete Tensor Specifications &#8212; Composable Kernel 1.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/composable_kernel/en/latest/conceptual/ck_tile/descriptors.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:16:32.975250+00:00
content_hash: "7e49505eac374911"
---

# Tensor Descriptors - Complete Tensor Specifications[#](#tensor-descriptors-complete-tensor-specifications)

## Overview[#](#overview)

A TensorDescriptor is the complete blueprint for a tensor. It combines a shape, stride information, and a series of [transformations](transforms.html#ck-tile-transforms) into a single object that defines exactly how a tensor’s data is laid out in memory. This specification enables CK Tile to create complex tensor views without any data movement.

In CK Tile, TensorDescriptors serve as the foundation for all tensor operations, providing:

**Memory Layout Specification**: How data is arranged in physical memory**Logical View Definition**: How the tensor appears to the programmer**Transformation Pipeline**: A series of[coordinate transformations](coordinate_systems.html#ck-tile-coordinate-systems)**Zero-Copy Views**: Different logical representations of the same data, building on[BufferViews](buffer_views.html#ck-tile-buffer-views)and[TensorViews](tensor_views.html#ck-tile-tensor-views)

## Creating Basic Tensor Layouts[#](#creating-basic-tensor-layouts)

CK Tile provides several ways to create tensor descriptors for common memory layouts.

### Custom Strides[#](#custom-strides)

The most fundamental way to define a tensor is with custom strides. This provides full control over how many elements to “jump” in memory to move to the next item along each dimension. This is particularly useful for creating padded layouts required by GPU algorithms.

```
using namespace ck_tile;
// Create a 3x4 tensor, but make each row take up 8 elements in memory
// (4 for data, 4 for padding)
constexpr auto M = 3;
constexpr auto N = 4;
constexpr auto RowStride = 8; // Padded stride
auto descriptor = make_naive_tensor_descriptor(
make_tuple(M, N), // Shape: [3, 4]
make_tuple(RowStride, 1) // Strides: [8, 1]
);
// The total memory needed is 3 rows * 8 elements/row = 24
constexpr auto element_space_size = M * RowStride;
// Calculate offset of the element at [row=1, col=2]
multi_index<2> coord{1, 2};
auto offset = descriptor.calculate_offset(coord);
// offset = 1*8 + 2*1 = 10
```

### Packed Row-Major Layout[#](#packed-row-major-layout)

For most cases, a tightly packed, row-major layout is sufficient. The strides are calculated automatically, leaving no unused space between elements.

```
using namespace ck_tile;
// Create a packed 3x4 tensor
auto descriptor_packed = make_naive_tensor_descriptor_packed(
make_tuple(3, 4)
);
// Total memory is 3 * 4 = 12 elements
// Strides are automatically [4, 1] for row-major layout
// Calculate offset of the element at [row=1, col=2]
multi_index<2> coord{1, 2};
auto offset = descriptor_packed.calculate_offset(coord);
// offset = 1*4 + 2*1 = 6
```

### Aligned Layout[#](#aligned-layout)

For GPU performance, memory layouts often need to be aligned. This function creates a row-major layout but ensures that each row’s starting address is a multiple of a given alignment value, adding padding if necessary.

```
using namespace ck_tile;
// Create a 4x5 tensor with 8-element alignment
constexpr auto align = 8; // Align each row to 8-element boundary
auto descriptor_aligned = make_naive_tensor_descriptor_aligned(
make_tuple(4, 5),
align
);
// Without alignment, size would be 4*5=20
// With alignment, the row stride becomes 8 (smallest multiple of 8 >= 5)
// Total size = 4 rows * 8 elements/row = 32
```

## The Pipeline Concept[#](#the-pipeline-concept)

Every TensorDescriptor in CK Tile can be thought of as a **transformation pipeline**. The functions above create the *first stage* of this pipeline, defining the initial [transformation](transforms.html#ck-tile-transforms) that takes a simple, one-dimensional block of memory and presents it as a logical, multi-dimensional tensor view.

### The Initial Pipeline Stage[#](#the-initial-pipeline-stage)

A simple packed descriptor sets up a pipeline with a single transform:

**Input**: The raw, one-dimensional memory buffer (hidden dimension ID 0)**Output**: The logical dimensions that you interact with (hidden dimension IDs 1, 2, …)

This initial stage converts linear memory addresses into multi-dimensional coordinates. See [Tensor Adaptors - Chaining Transformations](adaptors.html#ck-tile-adaptors) for how transforms chain together.

## Advanced Layouts: Step-by-Step Transformation[#](#advanced-layouts-step-by-step-transformation)

The `transform_tensor_descriptor`

function adds new stages to an existing descriptor’s pipeline using [transforms](transforms.html#ck-tile-transforms).

### Transform a [2, 6] Tensor into a [2, 2, 3] View[#](#transform-a-2-6-tensor-into-a-2-2-3-view)

This example reinterprets a 2D tensor with shape [2, 6] as a 3D tensor with shape [2, 2, 3], without changing the underlying 12-element memory buffer.

**Step 1: Define the Base Descriptor**

```
using namespace ck_tile;
// Create the [2, 6] base descriptor
auto base_descriptor = make_naive_tensor_descriptor_packed(
make_tuple(2, 6)
);
// This creates an initial pipeline stage that:
// - Takes the raw buffer (hidden ID 0) as input
// - Produces two outputs (hidden IDs 1 and 2)
// - These outputs become logical dimensions 0 and 1
```

**Step 2: Define the New Transformation Stage**

To get from [2, 6] to [2, 2, 3], we need:

**For logical dimension 0 (length 2)**: Preserve it with PassThroughTransform**For logical dimension 1 (length 6)**: Split it with UnmergeTransform([2, 3])

**Step 3: Apply Transformation**

```
// Create the transformed descriptor
auto transformed_descriptor = transform_tensor_descriptor(
base_descriptor,
make_tuple(
make_pass_through_transform(2), // For dim 0
make_unmerge_transform(make_tuple(2, 3)) // For dim 1
),
make_tuple(sequence<0>{}, sequence<1>{}), // Input mapping
make_tuple(sequence<0>{}, sequence<1, 2>{}) // Output mapping
);
// Result: A [2, 2, 3] view of the same data
```

### Analysis of the Final Pipeline[#](#analysis-of-the-final-pipeline)

The pipeline now has three stages:

**Base UnmergeTransform**: Converts raw buffer to [2, 6] layout**PassThroughTransform**: Preserves the first dimension**UnmergeTransform**: Splits the second dimension into [2, 3]

## 5D to 3D Block Transformation[#](#d-to-3d-block-transformation)

These concepts are critical in [GPU programming](hardware/gpu_basics.html#ck-tile-gpu-basics). This example transforms a 5D tensor representing a GPU thread block’s workload into a simpler 3D view using MergeTransform. See [Thread Mapping - Connecting to Hardware](thread_mapping.html#ck-tile-thread-mapping) for thread distribution details.

```
using namespace ck_tile;
// Define parameters (typical for a GPU block)
constexpr auto Block_M = 256;
constexpr auto NumWarps = 8;
constexpr auto WarpSize = 64;
constexpr auto KVector = 4;
constexpr auto wavesPerK = 2;
constexpr auto wavesPerM = NumWarps / wavesPerK;
constexpr auto NumIssues = Block_M / wavesPerM;
// Create the base 5D descriptor
auto base_descriptor = make_naive_tensor_descriptor_packed(
make_tuple(NumIssues, wavesPerM, wavesPerK, WarpSize, KVector)
);
// Transform to 3D by merging dimensions
auto transformed_descriptor = transform_tensor_descriptor(
base_descriptor,
make_tuple(
make_pass_through_transform(NumIssues),
make_merge_transform(make_tuple(wavesPerM, wavesPerK)),
make_merge_transform(make_tuple(WarpSize, KVector))
),
make_tuple(sequence<0>{}, sequence<1, 2>{}, sequence<3, 4>{}),
make_tuple(sequence<0>{}, sequence<1>{}, sequence<2>{})
);
// Result: [NumIssues, wavesPerM*wavesPerK, WarpSize*KVector]
// This simplifies thread block management while preserving data layout
```

## Common Descriptor Patterns[#](#common-descriptor-patterns)

### Matrix Transposition[#](#matrix-transposition)

```
// Create a transposed view of a matrix
auto transposed = transform_tensor_descriptor(
original_matrix,
make_tuple(
make_pass_through_transform(N),
make_pass_through_transform(M)
),
make_tuple(sequence<1>{}, sequence<0>{}), // Swap dimensions
make_tuple(sequence<0>{}, sequence<1>{})
);
```

### Padding for Convolution[#](#padding-for-convolution)

```
// Add padding to spatial dimensions
auto padded = transform_tensor_descriptor(
input_tensor,
make_tuple(
make_pass_through_transform(N), // Batch
make_pass_through_transform(C), // Channel
make_pad_transform(H, pad_h, pad_h), // Height
make_pad_transform(W, pad_w, pad_w) // Width
),
make_tuple(sequence<0>{}, sequence<1>{}, sequence<2>{}, sequence<3>{}),
make_tuple(sequence<0>{}, sequence<1>{}, sequence<2>{}, sequence<3>{})
);
```

For a complete convolution example, see [Convolution Implementation with CK Tile](convolution_example.html#ck-tile-convolution-example).

### Tensor Slicing[#](#tensor-slicing)

```
// Extract a sub-tensor
auto slice = transform_tensor_descriptor(
full_tensor,
make_tuple(
make_slice_transform(M, start_m, end_m),
make_slice_transform(N, start_n, end_n)
),
make_tuple(sequence<0>{}, sequence<1>{}),
make_tuple(sequence<0>{}, sequence<1>{})
);
```

## Key Concepts Summary[#](#key-concepts-summary)

TensorDescriptors provide a key abstraction for tensor manipulation:

**Pipeline Architecture**: Each descriptor is a transformation pipeline**Zero-Copy Views**: All transformations are logical, no data movement**Composability**: Complex layouts built from simple transforms**GPU Optimization**: Designed for efficient GPU memory access patterns

Important principles:

**Always Handle All Dimensions**: When transforming, provide a transform for each input dimension**Hidden Dimension IDs**: Track the flow of data through the pipeline**Compile-Time Resolution**: All transformations resolved at compile time**Type Safety**: Template metaprogramming ensures correctness

## Performance Considerations[#](#performance-considerations)

When designing tensor descriptors for GPU kernels:

**Memory Coalescing**: Ensure contiguous threads access contiguous memory**Bank Conflicts**: Avoid patterns that cause[shared memory conflicts](hardware/lds_bank_conflicts.html#ck-tile-lds-bank-conflicts)**Alignment**: Use aligned layouts for better memory throughput**Padding**: Strategic padding can improve access patterns. Ssee[Load Data Share Index Swapping](lds_index_swapping.html#ck-tile-lds-index-swapping)for advanced techniques.

## Next Steps[#](#next-steps)

[Tile Window - Data Access Gateway](tile_window.html#ck-tile-tile-window)- Using descriptors for efficient data loading[Tile Distribution - The Core API](tile_distribution.html#ck-tile-tile-distribution)- How descriptors enable automatic work distribution[Convolution Implementation with CK Tile](convolution_example.html#ck-tile-convolution-example)- Real-world application of complex descriptors[Static Distributed Tensor](static_distributed_tensor.html#ck-tile-static-distributed-tensor)- Managing distributed tensors with descriptors[A Block GEMM on MI300](hardware/gemm_optimization.html#ck-tile-gemm-optimization)- GEMM kernels using descriptor transformations
