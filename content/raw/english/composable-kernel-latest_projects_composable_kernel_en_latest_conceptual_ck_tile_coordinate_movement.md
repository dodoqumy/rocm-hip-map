---
title: "Advanced Coordinate Movement &#8212; Composable Kernel 1.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/composable_kernel/en/latest/conceptual/ck_tile/coordinate_movement.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-03T00:10:31.385060+00:00
content_hash: "295f34cad55a1886"
---

# Advanced Coordinate Movement[#](#advanced-coordinate-movement)

## Overview[#](#overview)

Advanced coordinate operations form the bridge between mathematical transformations and practical tensor manipulation in CK Tile. These operations enable efficient navigation through complex tensor layouts without recalculating entire transformation chains. Understanding coordinate movement is essential for implementing high-performance GPU kernels that traverse multi-dimensional data structures.

The coordinate movement system provides two key abstractions: TensorCoordinate for descriptor-aware navigation and TensorAdaptorCoordinate for tracking positions through transformation chains. Together with movement functions, they enable advanced access patterns while maintaining optimal performance through incremental updates rather than full recalculation.

For the mathematical foundations of coordinate systems, see [Coordinate Systems - The Mathematical Foundation](coordinate_systems.html#ck-tile-coordinate-systems). For simpler coordinate concepts, see [Tensor Coordinates](tensor_coordinates.html#ck-tile-tensor-coordinates).

## TensorAdaptorCoordinate: Transform-Aware Tracking[#](#tensoradaptorcoordinate-transform-aware-tracking)

TensorAdaptorCoordinate extends the concept to track coordinates through transformation chains, maintaining both input (top) and output (bottom) positions. This leverages [Tensor Adaptors - Chaining Transformations](adaptors.html#ck-tile-adaptors) and [Individual Transform Operations](transforms.html#ck-tile-transforms) for complex coordinate mappings.

### Structure and Implementation[#](#structure-and-implementation)

```
template<typename TensorAdaptor>
class TensorAdaptorCoordinate {
private:
MultiIndex top_index_; // Input position
MultiIndex bottom_index_; // Output after transformations
MultiIndex hidden_index_; // Intermediate results
public:
// Create from adaptor and position
__host__ __device__ TensorAdaptorCoordinate(
const TensorAdaptor& adaptor,
const MultiIndex& top_index)
{
top_index_ = top_index;
// Apply adaptor transforms
bottom_index_ = adaptor.calculate_bottom_index(top_index);
// Cache intermediate results
hidden_index_ = adaptor.get_hidden_index(top_index);
}
// Access transformed coordinates
__host__ __device__ const MultiIndex& get_top_index() const {
return top_index_;
}
__host__ __device__ const MultiIndex& get_bottom_index() const {
return bottom_index_;
}
};
```

### Tracking Through Transformations[#](#tracking-through-transformations)

```
// Example: Track coordinates through transpose
template<typename DataType>
__device__ void demonstrate_adaptor_coordinate() {
// Create transpose adaptor (swap dimensions)
auto adaptor = make_transpose_adaptor<2>(Sequence<1, 0>{});
// Create coordinate at [2, 3]
auto coord = make_tensor_adaptor_coordinate(
adaptor,
make_multi_index(2, 3)
);
// Track transformation
auto input_pos = coord.get_top_index(); // [2, 3]
auto output_pos = coord.get_bottom_index(); // [3, 2] (swapped)
// Use for complex access patterns
DataType* src_data = ...;
DataType* dst_data = ...;
// Read from transposed position
index_t src_offset = calculate_offset(output_pos);
DataType value = src_data[src_offset];
}
```

## Efficient Coordinate Movement[#](#efficient-coordinate-movement)

The `move_tensor_coordinate`

function provides efficient navigation by updating coordinates incrementally rather than recreating them.

### Basic Movement Operations[#](#basic-movement-operations)

```
// Move tensor coordinate through descriptor
template<typename TensorDescriptor>
__host__ __device__ void move_tensor_coordinate(
const TensorDescriptor& desc,
TensorCoordinate<TensorDescriptor>& coord,
const MultiIndex& step)
{
// Update top index
coord.top_index_ += step;
// Incrementally update cached values
// Only recalculate affected transformations
if (transformation_affects_movement(desc, step)) {
coord.hidden_index_ = desc.calculate_bottom_index(coord.top_index_);
coord.offset_ = desc.calculate_offset(coord.top_index_);
} else {
// Fast path: simple offset update
coord.offset_ += calculate_step_offset(desc, step);
}
}
```

### Practical Movement Patterns[#](#practical-movement-patterns)

```
// Example: Efficient matrix traversal
template<typename DataType>
__global__ void matrix_traversal_kernel(
const DataType* input,
DataType* output,
index_t rows, index_t cols)
{
// Create descriptor for matrix
using Desc = TensorDescriptor<DynamicSequence, DynamicSequence>;
Desc desc(make_tuple(rows, cols), make_tuple(cols, 1));
// Start at thread's assigned position
index_t start_row = blockIdx.y * blockDim.y + threadIdx.y;
index_t start_col = blockIdx.x * blockDim.x + threadIdx.x;
auto coord = make_tensor_coordinate(
desc,
make_multi_index(start_row, start_col)
);
// Row-wise traversal pattern
for (index_t i = 0; i < 4; ++i) {
if (coord.get_index()[0] < rows) {
// Process current position
output[coord.get_offset()] =
process_value(input[coord.get_offset()]);
// Move to next column
move_tensor_coordinate(desc, coord, make_multi_index(0, 1));
// Wrap to next row if needed
if (coord.get_index()[1] >= cols) {
move_tensor_coordinate(
desc, coord,
make_multi_index(1, -cols)
);
}
}
}
}
```

### Movement Through Adaptors[#](#movement-through-adaptors)

```
// Move through adaptor transformations
template<typename TensorAdaptor>
__host__ __device__ MultiIndex move_tensor_adaptor_coordinate(
const TensorAdaptor& adaptor,
TensorAdaptorCoordinate<TensorAdaptor>& coord,
const MultiIndex& step)
{
// Update top index
MultiIndex old_top = coord.top_index_;
coord.top_index_ += step;
// Calculate new bottom index
MultiIndex old_bottom = coord.bottom_index_;
coord.bottom_index_ = adaptor.calculate_bottom_index(coord.top_index_);
// Return the change in bottom coordinates
return coord.bottom_index_ - old_bottom;
}
```

## Advanced Movement Patterns[#](#advanced-movement-patterns)

Real-world applications use advanced movement patterns for optimal memory access. These patterns often relate to [Tile Window - Data Access Gateway](tile_window.html#ck-tile-tile-window) operations and [Tile Distribution - The Core API](tile_distribution.html#ck-tile-tile-distribution) concepts:

### Tiled Access Pattern[#](#tiled-access-pattern)

```
template<index_t TileM, index_t TileN>
__device__ void tiled_movement_pattern(
const float* input,
float* output,
index_t M, index_t N)
{
// Descriptor for full matrix
using MatrixDesc = TensorDescriptor<
DynamicSequence,
DynamicSequence
>;
MatrixDesc desc(make_tuple(M, N), make_tuple(N, 1));
// Start at tile corner
index_t tile_row = blockIdx.y * TileM;
index_t tile_col = blockIdx.x * TileN;
auto coord = make_tensor_coordinate(
desc,
make_multi_index(tile_row, tile_col)
);
// Process tile with efficient movement
#pragma unroll
for (index_t i = 0; i < TileM; ++i) {
#pragma unroll
for (index_t j = 0; j < TileN; ++j) {
if (i == 0 && j == 0) {
// First element - already positioned
} else if (j == 0) {
// New row - move down and back to start column
move_tensor_coordinate(
desc, coord,
make_multi_index(1, -(TileN-1))
);
} else {
// Same row - move right
move_tensor_coordinate(
desc, coord,
make_multi_index(0, 1)
);
}
// Process element
output[coord.get_offset()] =
compute_value(input[coord.get_offset()]);
}
}
}
```

### Space-Filling Curve Movement[#](#space-filling-curve-movement)

For more details on space-filling curves and their benefits, see [Space-Filling Curves - Optimal Memory Traversal](space_filling_curve.html#ck-tile-space-filling-curve).

```
// Snake pattern for optimal cache usage
template<index_t BlockSize>
__device__ void snake_pattern_movement(
const float* input,
float* output,
index_t M, index_t N)
{
using Desc = TensorDescriptor<DynamicSequence, DynamicSequence>;
Desc desc(make_tuple(M, N), make_tuple(N, 1));
auto coord = make_tensor_coordinate(
desc,
make_multi_index(threadIdx.y, threadIdx.x)
);
// Snake through block
for (index_t row = 0; row < BlockSize; ++row) {
for (index_t col = 0; col < BlockSize; ++col) {
// Process current position
process_element(input, output, coord.get_offset());
// Snake movement pattern
if (row % 2 == 0) {
// Even rows: move right
if (col < BlockSize - 1) {
move_tensor_coordinate(
desc, coord, make_multi_index(0, 1)
);
}
} else {
// Odd rows: move left
if (col < BlockSize - 1) {
move_tensor_coordinate(
desc, coord, make_multi_index(0, -1)
);
}
}
}
// Move to next row
if (row < BlockSize - 1) {
move_tensor_coordinate(
desc, coord, make_multi_index(1, 0)
);
}
}
}
```

## Performance Considerations[#](#performance-considerations)

Efficient coordinate movement is critical for GPU performance. See [Intro to AMD CDNA Architecture](hardware/gpu_basics.html#ck-tile-gpu-basics) for hardware details.

**1. Incremental Updates**

```
// Inefficient: recreate coordinate
for (index_t i = 0; i < N; ++i) {
auto coord = make_tensor_coordinate(desc, make_multi_index(i, j));
process(data[coord.get_offset()]);
}
// Efficient: incremental movement
auto coord = make_tensor_coordinate(desc, make_multi_index(0, j));
for (index_t i = 0; i < N; ++i) {
process(data[coord.get_offset()]);
move_tensor_coordinate(desc, coord, make_multi_index(1, 0));
}
```

**2. Movement Caching**

```
// Cache frequently used movements
template<typename Desc>
struct MovementCache {
MultiIndex row_step = make_multi_index(1, 0);
MultiIndex col_step = make_multi_index(0, 1);
MultiIndex diag_step = make_multi_index(1, 1);
__device__ void move_row(auto& coord) {
move_tensor_coordinate(Desc{}, coord, row_step);
}
};
```

**3. Vectorized Movement**

```
// Move multiple coordinates simultaneously
template<index_t NumCoords>
__device__ void vectorized_movement(
TensorCoordinate<Desc> coords[NumCoords],
const MultiIndex& step)
{
#pragma unroll
for (index_t i = 0; i < NumCoords; ++i) {
move_tensor_coordinate(Desc{}, coords[i], step);
}
}
```

## Integration with CK Tile Components[#](#integration-with-ck-tile-components)

Coordinate movement integrates seamlessly with other CK Tile components:

```
// Example: Tile window with coordinate movement
template<typename TileWindow>
__device__ void process_tile_with_movement(
TileWindow& window,
index_t tile_size)
{
// Create coordinate for tile traversal
auto coord = window.get_tile_coordinate();
// Process tile elements with movement
for (index_t i = 0; i < tile_size; ++i) {
for (index_t j = 0; j < tile_size; ++j) {
// Load using coordinate
auto value = window.load_at(coord);
// Process value
auto result = compute(value);
// Store result
window.store_at(coord, result);
// Move to next element
window.move_coordinate(coord, {0, 1});
}
// Move to next row
window.move_coordinate(coord, {1, -tile_size});
}
}
```

Advanced coordinate operations provide the foundation for efficient tensor navigation in CK Tile:

**TensorCoordinate**: Combines position with descriptor context for validated navigation**TensorAdaptorCoordinate**: Tracks coordinates through transformation chains**move_tensor_coordinate**: Enables efficient incremental updates without recalculation**Movement Patterns**: Support advanced access patterns like tiling and space-filling curves**Performance**: Incremental updates are orders of magnitude faster than coordinate recreation**Integration**: Seamlessly works with tile windows, distributions, and other CK Tile components

These operations are essential for implementing high-performance GPU kernels that can navigate complex tensor layouts efficiently. By understanding and utilizing coordinate movement, kernels can be created that achieve optimal memory access patterns while maintaining code clarity and correctness.
