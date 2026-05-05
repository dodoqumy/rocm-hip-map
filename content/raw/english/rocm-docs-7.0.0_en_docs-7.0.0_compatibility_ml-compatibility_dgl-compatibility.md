---
title: "DGL compatibility"
source_url: "https://rocm.docs.amd.com/en/docs-7.0.0/compatibility/ml-compatibility/dgl-compatibility.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:04:06.367151+00:00
content_hash: "977a3c19320865bf"
---

# DGL compatibility[#](#dgl-compatibility)

2025-08-14

6 min read time

Deep Graph Library [(DGL)](https://www.dgl.ai/) is an easy-to-use, high-performance and scalable
Python package for deep learning on graphs. DGL is framework agnostic, meaning
if a deep graph model is a component in an end-to-end application, the rest of
the logic is implemented using PyTorch.

ROCm support for DGL is hosted in the

[ROCm/dgl](https://github.com/ROCm/dgl)repository.Due to independent compatibility considerations, this location differs from the

[dmlc/dgl](https://github.com/dmlc/dgl)upstream repository.Use the prebuilt

[Docker images](#dgl-docker-compat)with DGL, PyTorch, and ROCm preinstalled.See the

[ROCm DGL installation guide](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.0.0/install/3rd-party/dgl-install.html)to install and get started.

## Supported devices[#](#supported-devices)

**Officially Supported**: TF32 with AMD Instinct MI300X (through hipblaslt)**Partially Supported**: TF32 with AMD Instinct MI250X

## Use cases and recommendations[#](#use-cases-and-recommendations)

DGL can be used for Graph Learning, and building popular graph models like GAT, GCN and GraphSage. Using these we can support a variety of use-cases such as:

Recommender systems

Network Optimization and Analysis

1D (Temporal) and 2D (Image) Classification

Drug Discovery


Multiple use cases of DGL have been tested and verified.
However, a recommended example follows a drug discovery pipeline using the `SE3Transformer`

.
Refer to the [AMD ROCm blog](https://rocm.blogs.amd.com/),
where you can search for DGL examples and best practices to optimize your training workflows on AMD GPUs.

Coverage includes:

Single-GPU training/inference

Multi-GPU training


## Docker image compatibility[#](#docker-image-compatibility)

AMD validates and publishes [DGL images](https://hub.docker.com/r/rocm/dgl)
with ROCm and Pytorch backends on Docker Hub. The following Docker image tags and associated
inventories were tested on [ROCm 6.4.0](https://repo.radeon.com/rocm/apt/6.4/).
Click the

## Key ROCm libraries for DGL[#](#key-rocm-libraries-for-dgl)

DGL on ROCm depends on specific libraries that affect its features and performance. Using the DGL Docker container or building it with the provided docker file or a ROCm base image is recommended. If you prefer to build it yourself, ensure the following dependencies are installed:

ROCm library |
Version |
Purpose |
|---|---|---|
1.1.0 |
Enables faster execution of core operations like matrix multiplication (GEMM), convolutions and transformations. |
|
3.0.0 |
Provides GPU-accelerated Basic Linear Algebra Subprograms (BLAS) for matrix and vector operations. |
|
1.0.0 |
hipBLASLt is an extension of the hipBLAS library, providing additional features like epilogues fused into the matrix multiplication kernel or use of integer tensor cores. |
|
4.0.0 |
Provides a C++ template library for parallel algorithms for reduction, scan, sort and select. |
|
1.0.20 |
Provides GPU-accelerated Fast Fourier Transform (FFT) operations. |
|
3.0.0 |
Provides fast random number generation for GPUs. |
|
3.0.0 |
Provides GPU-accelerated solvers for linear systems, eigenvalues, and singular value decompositions (SVD). |
|
4.0.1 |
Accelerates operations on sparse matrices, such as sparse matrix-vector or matrix-matrix products. |
|
0.2.4 |
Accelerates operations on sparse matrices, such as sparse matrix-vector or matrix-matrix products. |
|
2.0.0 |
Optimizes for high-performance tensor operations, such as contractions. |
|
3.5.0 |
Optimizes deep learning primitives such as convolutions, pooling, normalization, and activation functions. |
|
2.13.0 |
Adds graph-level optimizations, ONNX models and mixed precision support and enable Ahead-of-Time (AOT) Compilation. |
|
3.3.0 |
Optimizes acceleration for computer vision and AI workloads like preprocessing, augmentation, and inferencing. |
|
2.3.0 |
Accelerates the data pipeline by offloading intensive preprocessing and augmentation tasks. rocAL is part of MIVisionX. |
|
2.26.6 |
Optimizes for multi-GPU communication for operations like AllReduce and Broadcast. |
|
1.0.0 |
Provides hardware-accelerated data decoding capabilities, particularly for image, video, and other dataset formats. |
|
1.1.0 |
Provides hardware-accelerated JPEG image decoding and encoding. |
|
2.0.0 |
Speeds up data augmentation, transformation, and other preprocessing steps. |
|
4.0.0 |
Provides a C++ template library for parallel algorithms like sorting, reduction, and scanning. |
|
2.0.0 |
Accelerates warp-level matrix-multiply and matrix-accumulate to speed up matrix multiplication (GEMM) and accumulation operations with mixed precision support. |

## Supported features[#](#supported-features)

Many functions and methods available in DGL Upstream are also supported in DGL ROCm. Instead of listing them all, support is grouped into the following categories to provide a general overview.

DGL Base

DGL Backend

DGL Data

DGL Dataloading

DGL DGLGraph

DGL Function

DGL Ops

DGL Sampling

DGL Transforms

DGL Utils

DGL Distributed

DGL Geometry

DGL Mpops

DGL NN

DGL Optim

DGL Sparse


## Unsupported features[#](#unsupported-features)

Graphbolt

Partial TF32 Support (MI250x only)

Kineto/ ROCTracer integration


## Unsupported functions[#](#unsupported-functions)

`more_nnz`

`format`

`multiprocess_sparse_adam_state_dict`

`record_stream_ndarray`

`half_spmm`

`segment_mm`

`gather_mm_idx_b`

`pgexplainer`

`sample_labors_prob`

`sample_labors_noprob`
