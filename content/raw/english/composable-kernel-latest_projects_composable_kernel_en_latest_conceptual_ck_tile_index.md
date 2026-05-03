---
title: "CK Tile Conceptual Documentation &#8212; Composable Kernel 1.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/composable_kernel/en/latest/conceptual/ck_tile/index.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-03T03:09:26.690765+00:00
content_hash: "3c556ac9e3c07237"
---

# CK Tile Conceptual Documentation[#](#ck-tile-conceptual-documentation)

Welcome to the conceptual documentation for CK Tile, the core abstraction layer of Composable Kernel that enables efficient GPU programming through compile-time coordinate transformations and tile-based data distribution.

See the [CK Tile conceptual documentation table of contents](CK-tile-index.html#ck-tile-index) for the complete CK Tile documentation structure.

## Overview[#](#overview)

CK Tile provides a mathematical framework for expressing complex GPU computations through:

**Automatic Memory Coalescing**: Ensures optimal memory access patterns without manual optimization**Thread Cooperation**: Coordinates work distribution across the GPU’s hierarchical execution model**Zero-Overhead Abstractions**: Compile-time optimizations ensure no runtime performance penalty**Portable Performance**: Same code achieves high performance across different GPU architectures

## Why CK Tile?[#](#why-ck-tile)

Traditional GPU programming requires manual management of:

Thread-to-data mapping calculations

Memory coalescing patterns

Bank conflict avoidance

Boundary condition handling


CK Tile automates all of these concerns through a unified abstraction that maps logical problem coordinates to physical GPU resources.

## Learning Path[#](#learning-path)

**Start Here**:[Introduction and Motivation - Why Tile Distribution Matters](introduction_motivation.html#ck-tile-introduction)The fundamental problems CK Tile solves and why it’s essential for efficient GPU programming.

**Foundation**:[Buffer Views - Raw Memory Access](buffer_views.html#ck-tile-buffer-views)How CK Tile provides structured access to raw GPU memory across different address spaces.

**Multi-Dimensional Views**:[Tensor Views - Multi-Dimensional Structure](tensor_views.html#ck-tile-tensor-views)How to work with multi-dimensional data structures and memory layouts.

**Core API**:[Tile Distribution - The Core API](tile_distribution.html#ck-tile-tile-distribution)The tile distribution system that maps work to GPU threads.

**Mathematical Framework**:[Coordinate Systems - The Mathematical Foundation](coordinate_systems.html#ck-tile-coordinate-systems)The coordinate transformation system that powers CK Tile’s abstractions.

**Reference**:[Terminology Reference - Key Concepts and Definitions](terminology.html#ck-tile-terminology)Glossary of all terms and concepts used in CK Tile.


## Key Concepts at a Glance[#](#key-concepts-at-a-glance)

**Coordinate Spaces**

**P-space**: Processing element coordinates (thread, warp, block)**Y-space**: Local tile access patterns**X-space**: Physical tensor coordinates**D-space**: Linearized memory addresses

**Core Components**

**BufferView**: Type-safe access to GPU memory**TileDistribution**: Automatic work distribution**TileWindow**: Efficient data loading/storing**Encoding**: Compile-time distribution specification

## Quick Example[#](#quick-example)

```
// Define how to distribute a 256x256 tile across threads
using Encoding = tile_distribution_encoding<
sequence<>, // No replication
tuple<sequence<4,2,8,4>, // M dimension hierarchy
sequence<4,2,8,4>>, // N dimension hierarchy
tuple<sequence<1,2>, sequence<1,2>>, // Thread mapping
tuple<sequence<1,1>, sequence<2,2>>, // Minor indices
sequence<1,1,2,2>, // Y-space mapping
sequence<0,3,0,3> // Y-space minor
>;
// Create distribution and load data
auto distribution = make_static_tile_distribution(Encoding{});
auto window = make_tile_window(tensor_view, tile_size, origin, distribution);
auto tile = window.load();
// Process tile efficiently
sweep_tile(tile, [](auto idx) { /* computation */ });
```

## Next Steps[#](#next-steps)

To dive deeper, start with [Introduction and Motivation - Why Tile Distribution Matters](introduction_motivation.html#ck-tile-introduction) to understand the motivation and core concepts behind CK Tile.

For practical examples, see the [example/ck_tile](https://github.com/ROCm/rocm-libraries/tree/develop/projects/composablekernel/example/ck_tile) directory in the Composable Kernel repository.
