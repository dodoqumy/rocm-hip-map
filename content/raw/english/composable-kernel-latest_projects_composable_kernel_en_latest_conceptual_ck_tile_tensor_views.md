---
title: "Tensor Views - Multi-Dimensional Structure &#8212; Composable Kernel 1.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/composable_kernel/en/latest/conceptual/ck_tile/tensor_views.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:10:13.921446+00:00
content_hash: "8303f94fe1638a16"
---

# Tensor Views - Multi-Dimensional Structure[#](#tensor-views-multi-dimensional-structure)

## Overview[#](#overview)

While [BufferView](buffer_views.html#ck-tile-buffer-views) provides the foundation for raw memory access, TensorView adds multi-dimensional structure to flat memory regions. This abstraction bridges the gap between how developers conceptualize data and how that data is physically stored in linear memory. TensorView enables coordinate-based access patterns that match the natural structure of algorithms while maintaining the performance characteristics necessary for efficient GPU computation.

TensorView presents different logical views of the same underlying memory without copying data. A single memory region can be viewed as a row-major matrix, a column-major matrix, or a transposed matrix, using different TensorView configurations. This zero-copy abstraction enables flexible transformations and access patterns while maintaining optimal memory bandwidth utilization.

## TensorView Architecture[#](#tensorview-architecture)

## The Foundation: BufferView and TensorDescriptor[#](#the-foundation-bufferview-and-tensordescriptor)

TensorView builds upon two fundamental components that work in concert to provide structured access to memory. The [BufferView](buffer_views.html#ck-tile-buffer-views) component handles the low-level memory access, providing type-safe operations with address space awareness. The [TensorDescriptor](descriptors.html#ck-tile-descriptors) component encodes the multi-dimensional structure, including shape information and stride patterns that determine how coordinates map to memory offsets.

This separation of concerns enables optimizations. The BufferView can optimize for the specific memory space while the TensorDescriptor can encode complex access patterns without concern for the underlying memory type. Together, they provide a complete abstraction for multi-dimensional data access.

## C++ Implementation[#](#c-implementation)

**File**: `include/ck_tile/core/tensor/tensor_view.hpp`


### Creating TensorViews[#](#creating-tensorviews)

The creation of a TensorView involves combining a BufferView with a TensorDescriptor. This process can be done explicitly for maximum control or through convenience functions for common patterns:

```
#include <ck_tile/core/tensor/tensor_view.hpp>
#include <ck_tile/core/tensor/tensor_descriptor.hpp>
#include <ck_tile/core/numeric/tuple.hpp>
// The actual C++ template signature from tensor_view.hpp:
// template <typename BufferView_,
// typename TensorDesc_,
// memory_operation_enum DstInMemOp_ = memory_operation_enum::set>
// struct tensor_view
__device__ void example_tensor_creation()
{
// Create a 3x4 matrix in global memory
float data[12] = {0,1,2,3,4,5,6,7,8,9,10,11};
// Method 1: Create buffer and descriptor separately
auto buffer = make_buffer_view<address_space_enum::global>(data, 12);
auto desc = make_tensor_descriptor(
make_tuple(3, 4), // shape: 3 rows, 4 columns
make_tuple(4, 1) // strides: row stride=4, col stride=1
);
// Create tensor view
auto tensor = make_tensor_view<address_space_enum::global>(buffer, desc);
// Method 2: Use convenience function for packed layout
auto tensor2 = make_naive_tensor_view_packed<address_space_enum::global>(
data, // pointer
make_tuple(3, 4) // shape (strides calculated automatically)
);
// Access element at (1, 2)
float value = tensor(make_tuple(1, 2)); // Returns 6
// Update element
tensor(make_tuple(2, 1)) = 99.0f;
}
```

### Coordinate-Based Access[#](#coordinate-based-access)

The fundamental operation of TensorView is translating multi-dimensional coordinates into memory accesses. This translation happens through an advanced pipeline that maintains efficiency while providing flexibility:

## Memory Layouts and Strides[#](#memory-layouts-and-strides)

A key feature of TensorView is its ability to represent different memory layouts through stride manipulation. This capability enables zero-copy transformations that would otherwise require expensive memory operations:

### Row-Major vs Column-Major Layouts[#](#row-major-vs-column-major-layouts)

The choice of memory layout has profound implications for performance. Row-major layout, where consecutive elements in a row are stored contiguously, optimizes for row-wise traversal. Column-major layout optimizes for column-wise traversal. CK’s TensorView abstraction allows algorithms to work with their natural access patterns regardless of the underlying storage:

```
__device__ void example_memory_layouts()
{
float data[12] = {0,1,2,3,4,5,6,7,8,9,10,11};
// Row-major layout (default)
auto row_major = make_naive_tensor_view_packed<address_space_enum::global>(
data, make_tuple(3, 4)
);
// Strides: (4, 1) - moving one row advances by 4 elements
// Column-major layout through custom strides
auto col_major = make_tensor_view<address_space_enum::global>(
make_buffer_view<address_space_enum::global>(data, 12),
make_tensor_descriptor(
make_tuple(3, 4), // shape
make_tuple(1, 3) // strides: row stride=1, col stride=3
)
);
// Transposed view (no data copy!)
auto transposed = make_tensor_view<address_space_enum::global>(
make_buffer_view<address_space_enum::global>(data, 12),
make_tensor_descriptor(
make_tuple(4, 3), // transposed shape
make_tuple(1, 4) // transposed strides
)
);
// All three views access the same memory, just differently
// row_major(1,2) == col_major(2,1) == transposed(2,1)
}
```

## Advanced Operations[#](#advanced-operations)

### Slicing and Subviews[#](#slicing-and-subviews)

TensorView supports advanced slicing operations that create new views of subsets of the data. These operations are essential for algorithms that process data in blocks or tiles. See [Tile Window - Data Access Gateway](tile_window.html#ck-tile-tile-window) for production use.

```
__device__ void example_slicing_operations()
{
// Create a larger tensor
float data[100];
auto tensor = make_naive_tensor_view_packed<address_space_enum::global>(
data, make_tuple(10, 10)
);
// Create a subview using transforms
// This would typically be done with tile_window in production code
auto subview = make_tensor_view<address_space_enum::global>(
tensor.get_buffer_view(),
transform_tensor_descriptor(
tensor.get_tensor_descriptor(),
make_tuple(
make_pass_through_transform(number<5>{}), // 5 rows
make_pass_through_transform(number<5>{}) // 5 columns
),
make_tuple(number<2>{}, number<3>{}) // offset (2,3)
)
);
// subview now represents a 5x5 region starting at (2,3)
}
```

### Vectorized Access[#](#vectorized-access)

GPUs achieve maximum memory bandwidth through vectorized operations. TensorView provides native support for vector loads and stores. See [LoadStoreTraits - Memory Access Optimization Engine](load_store_traits.html#ck-tile-load-store-traits) for more details.

```
__device__ void example_vectorized_access()
{
float data[256];
auto tensor = make_naive_tensor_view_packed<address_space_enum::global>(
data, make_tuple(16, 16)
);
// Create coordinate for vectorized access
auto coord = make_tensor_coordinate(
tensor.get_tensor_descriptor(),
make_tuple(4, 0) // row 4, starting at column 0
);
// Load 4 consecutive elements as float4
using float4 = vector_type<float, 4>::type;
auto vec4 = tensor.get_vectorized_elements<float4>(coord, 0);
// Process vector data
vec4.x *= 2.0f;
vec4.y *= 2.0f;
vec4.z *= 2.0f;
vec4.w *= 2.0f;
// Store back
tensor.set_vectorized_elements<float4>(coord, 0, vec4);
}
```

## Performance Considerations[#](#performance-considerations)

### Memory Access Patterns[#](#memory-access-patterns)

The efficiency of TensorView operations depends on memory access patterns. Understanding these patterns is important for achieving optimal performance. See [Intro to AMD CDNA Architecture](hardware/gpu_basics.html#ck-tile-gpu-basics) for hardware considerations.

### Compile-Time Optimization[#](#compile-time-optimization)

CK’s TensorView leverages compile-time optimization to achieve zero-overhead abstraction. When tensor dimensions and strides are known at compile time, the entire coordinate-to-offset calculation can be resolved during compilation:

```
// Compile-time known dimensions enable optimization
constexpr auto shape = make_tuple(number<256>{}, number<256>{});
constexpr auto strides = make_tuple(number<256>{}, number<1>{});
auto tensor = make_tensor_view<address_space_enum::global>(
buffer,
make_tensor_descriptor(shape, strides)
);
// This access compiles to a single memory instruction
constexpr auto coord = make_tuple(number<5>{}, number<10>{});
auto value = tensor(coord); // Offset calculated at compile time
```

## TensorView vs BufferView[#](#tensorview-vs-bufferview)

Understanding when to use TensorView versus BufferView is crucial for writing efficient code:

BufferView excels at raw memory operations where linear access is natural or where the overhead of coordinate calculation would be prohibitive. TensorView is best suited for algorithms that operate in terms of multi-dimensional coordinates, such as matrix operations, image processing, or tensor contractions.

## Integration with Tile Distribution[#](#integration-with-tile-distribution)

TensorView serves as the foundation for [tile distribution’s](tile_distribution.html#ck-tile-tile-distribution) higher-level abstractions. When combined with [tile windows](tile_window.html#ck-tile-tile-window) and distribution patterns, TensorView enables the automatic generation of efficient access patterns:

```
// TensorView provides the base abstraction
auto tensor_view = make_naive_tensor_view_packed<address_space_enum::global>(
global_memory, make_tuple(M, N)
);
// Tile window builds on TensorView for distributed access
auto tile_window = make_tile_window(
tensor_view,
tile_shape,
origin,
distribution
);
// The distribution automatically generates optimal access patterns
auto distributed_tensor = tile_window.load();
```

## Summary[#](#summary)

TensorView bridges the gap between logical multi-dimensional data structures and physical memory layout. Through its advanced design, TensorView provides:

**Multi-dimensional Indexing**: Natural coordinate-based access to data, matching how algorithms conceptualize their operations. This abstraction eliminates error-prone manual index calculations while maintaining performance.

**Flexible Memory Layouts**: Support for row-major, column-major, and custom stride patterns enables algorithms to work with data in its most natural form. Zero-copy transformations like transposition become stride manipulations.

**Zero-Copy Views**: The ability to create different logical views of the same physical memory enables flexible transformations without the overhead of data movement. This capability is essential for efficient GPU programming where memory bandwidth is often the limiting factor.

**Type Safety**: Dimensions and memory spaces are encoded in the type system, catching errors at compile time rather than runtime. This safety comes without performance overhead thanks to template metaprogramming.

**Seamless Integration**: TensorView works harmoniously with [BufferView](buffer_views.html#ck-tile-buffer-views) for low-level access and serves as the foundation for higher-level abstractions like [tile windows](tile_window.html#ck-tile-tile-window) and [distributed tensors](static_distributed_tensor.html#ck-tile-static-distributed-tensor).

The abstraction enables writing dimension-agnostic algorithms while maintaining high performance through compile-time optimizations.

## Next Steps[#](#next-steps)

Continue to [Coordinate Systems - The Mathematical Foundation](coordinate_systems.html#ck-tile-coordinate-systems) to understand the mathematical foundation of coordinate transformations in CK Tile.
