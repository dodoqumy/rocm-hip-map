---
title: "PyTorch compatibility"
source_url: "https://rocm.docs.amd.com/en/docs-7.0.0/compatibility/ml-compatibility/pytorch-compatibility.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T12:05:53.034120+00:00
content_hash: "350a2a40af532594"
---

# PyTorch compatibility[#](#pytorch-compatibility)

2025-10-28

14 min read time

[PyTorch](https://pytorch.org/) is an open-source tensor library designed for
deep learning. PyTorch on ROCm provides mixed-precision and large-scale training
using [MIOpen](https://github.com/ROCm/MIOpen) and
[RCCL](https://github.com/ROCm/rccl) libraries.

ROCm support for PyTorch is upstreamed into the official PyTorch repository. Due to independent compatibility considerations, this results in two distinct release cycles for PyTorch on ROCm:

ROCm PyTorch release:

Provides the latest version of ROCm but might not necessarily support the latest stable PyTorch version.

Offers

[Docker images](#pytorch-docker-compat)with ROCm and PyTorch preinstalled.ROCm PyTorch repository:

[ROCm/pytorch](https://github.com/ROCm/pytorch)See the

[ROCm PyTorch installation guide](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.0.0/install/3rd-party/pytorch-install.html)to get started.

Official PyTorch release:

Provides the latest stable version of PyTorch but might not necessarily support the latest ROCm version.

Official PyTorch repository:

[pytorch/pytorch](https://github.com/pytorch/pytorch)See the

[Nightly and latest stable version installation guide](https://pytorch.org/get-started/locally/)or[Previous versions](https://pytorch.org/get-started/previous-versions/)to get started.


PyTorch includes tooling that generates HIP source code from the CUDA backend.
This approach allows PyTorch to support ROCm without requiring manual code
modifications. For more information, see [HIPIFY](https://rocm.docs.amd.com/projects/HIPIFY/en/docs-7.0.0/index.html).

ROCm development is aligned with the stable release of PyTorch, while upstream PyTorch testing uses the stable release of ROCm to maintain consistency.

## Use cases and recommendations[#](#use-cases-and-recommendations)

[Using ROCm for AI: training a model](../../how-to/rocm-for-ai/training/benchmark-docker/pytorch-training.html)guides how to leverage the ROCm platform for training AI models. It covers the steps, tools, and best practices for optimizing training workflows on AMD GPUs using PyTorch features.[Single-GPU fine-tuning and inference](../../how-to/rocm-for-ai/fine-tuning/single-gpu-fine-tuning-and-inference.html)describes and demonstrates how to use the ROCm platform for the fine-tuning and inference of machine learning models, particularly large language models (LLMs), on systems with a single GPU. This topic provides a detailed guide for setting up, optimizing, and executing fine-tuning and inference workflows in such environments.[Multi-GPU fine-tuning and inference optimization](../../how-to/rocm-for-ai/fine-tuning/multi-gpu-fine-tuning-and-inference.html)describes and demonstrates the fine-tuning and inference of machine learning models on systems with multiple GPUs.The

[Instinct MI300X workload optimization guide](../../how-to/rocm-for-ai/inference-optimization/workload.html)provides detailed guidance on optimizing workloads for the AMD Instinct MI300X accelerator using ROCm. This guide helps users achieve optimal performance for deep learning and other high-performance computing tasks on the MI300X accelerator.The

[Inception with PyTorch documentation](../../conceptual/ai-pytorch-inception.html)describes how PyTorch integrates with ROCm for AI workloads It outlines the use of PyTorch on the ROCm platform and focuses on efficiently leveraging AMD GPU hardware for training and inference tasks in AI applications.

For more use cases and recommendations, see [ROCm PyTorch blog posts](https://rocm.blogs.amd.com/blog/tag/pytorch.html).

## Docker image compatibility[#](#docker-image-compatibility)

AMD provides preconfigured Docker images with PyTorch and the ROCm backend.
These images are published on [Docker Hub](https://hub.docker.com/r/rocm/pytorch) and are the
recommended way to get started with deep learning with PyTorch on ROCm.

To find the right image tag, see the [PyTorch on ROCm installation
documentation](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.0.0/install/3rd-party/pytorch-install.html#pytorch-docker-support) for a list of
available `rocm/pytorch`

images.

## Key ROCm libraries for PyTorch[#](#key-rocm-libraries-for-pytorch)

PyTorch functionality on ROCm is determined by its underlying library dependencies. These ROCm components affect the capabilities, performance, and feature set available to developers.

ROCm library |
Version |
Purpose |
Used in |
|---|---|---|---|
1.1.0 |
Enables faster execution of core operations like matrix multiplication (GEMM), convolutions and transformations. |
Speeds up |
|
3.0.0 |
Provides GPU-accelerated Basic Linear Algebra Subprograms (BLAS) for matrix and vector operations. |
Supports operations such as matrix multiplication, matrix-vector products, and tensor contractions. Utilized in both dense and batched linear algebra operations. |
|
1.0.0 |
hipBLASLt is an extension of the hipBLAS library, providing additional features like epilogues fused into the matrix multiplication kernel or use of integer tensor cores. |
Accelerates operations such as |
|
4.0.0 |
Provides a C++ template library for parallel algorithms for reduction, scan, sort and select. |
Supports operations such as |
|
1.0.20 |
Provides GPU-accelerated Fast Fourier Transform (FFT) operations. |
Used in functions like the |
|
3.0.0 |
Provides fast random number generation for GPUs. |
The |
|
3.0.0 |
Provides GPU-accelerated solvers for linear systems, eigenvalues, and singular value decompositions (SVD). |
Supports functions like |
|
4.0.1 |
Accelerates operations on sparse matrices, such as sparse matrix-vector or matrix-matrix products. |
Sparse tensor operations |
|
0.2.4 |
Accelerates operations on sparse matrices, such as sparse matrix-vector or matrix-matrix products. |
Sparse tensor operations |
|
2.0.0 |
Optimizes for high-performance tensor operations, such as contractions. |
Accelerates tensor algebra, especially in deep learning and scientific computing. |
|
3.5.0 |
Optimizes deep learning primitives such as convolutions, pooling, normalization, and activation functions. |
Speeds up convolutional neural networks (CNNs), recurrent neural
networks (RNNs), and other layers. Used in operations like
|
|
2.13.0 |
Adds graph-level optimizations, ONNX models and mixed precision support and enable Ahead-of-Time (AOT) Compilation. |
Speeds up inference models and executes ONNX models for
compatibility with other frameworks.
|
|
3.3.0 |
Optimizes acceleration for computer vision and AI workloads like preprocessing, augmentation, and inferencing. |
Faster data preprocessing and augmentation pipelines for datasets like
ImageNet or COCO and easy to integrate into PyTorch’s |
|
2.3.0 |
Accelerates the data pipeline by offloading intensive preprocessing and augmentation tasks. rocAL is part of MIVisionX. |
Easy to integrate into PyTorch’s |
|
2.26.6 |
Optimizes for multi-GPU communication for operations like AllReduce and Broadcast. |
Distributed data parallel training ( |
|
1.0.0 |
Provides hardware-accelerated data decoding capabilities, particularly for image, video, and other dataset formats. |
Can be integrated in |
|
1.1.0 |
Provides hardware-accelerated JPEG image decoding and encoding. |
GPU accelerated |
|
2.0.0 |
Speeds up data augmentation, transformation, and other preprocessing steps. |
Easy to integrate into PyTorch’s |
|
4.0.0 |
Provides a C++ template library for parallel algorithms like sorting, reduction, and scanning. |
Utilized in backend operations for tensor computations requiring parallel processing. |
|
2.0.0 |
Accelerates warp-level matrix-multiply and matrix-accumulate to speed up matrix multiplication (GEMM) and accumulation operations with mixed precision support. |
Linear layers ( |

## Supported modules and data types[#](#supported-modules-and-data-types)

The following section outlines the supported data types, modules, and domain libraries available in PyTorch on ROCm.

### Supported data types[#](#supported-data-types)

The tensor data type is specified using the `dtype`

attribute or argument.
PyTorch supports many data types for different use cases.

The following table lists [torch.Tensor](https://pytorch.org/docs/stable/tensors.html)
single data types:

Data type |
Description |
|---|---|
|
8-bit floating point, e4m3 |
|
8-bit floating point, e5m2 |
|
16-bit floating point |
|
16-bit floating point |
|
32-bit floating point |
|
64-bit floating point |
|
32-bit complex numbers |
|
64-bit complex numbers |
|
128-bit complex numbers |
|
8-bit integer (unsigned) |
|
16-bit integer (unsigned); Not natively supported in ROCm |
|
32-bit integer (unsigned); Not natively supported in ROCm |
|
64-bit integer (unsigned); Not natively supported in ROCm |
|
8-bit integer (signed) |
|
16-bit integer (signed) |
|
32-bit integer (signed) |
|
64-bit integer (signed) |
|
Boolean |
|
Quantized 8-bit integer (unsigned) |
|
Quantized 8-bit integer (signed) |
|
Quantized 32-bit integer (signed) |
|
Quantized 4-bit integer (unsigned) |

Note

Unsigned types, except `uint8`

, have limited support in eager mode. They
primarily exist to assist usage with `torch.compile`

.

See [ROCm precision support](https://rocm.docs.amd.com/en/docs-7.0.0/reference/precision-support.html) for the
native hardware support of data types.

### Supported modules[#](#supported-modules)

For a complete and up-to-date list of PyTorch core modules (for example., `torch`

,
`torch.nn`

, `torch.cuda`

, `torch.backends.cuda`

and
`torch.backends.cudnn`

), their descriptions, and usage, please refer directly
to the [official PyTorch documentation](https://pytorch.org/docs/stable/index.html).

Core PyTorch functionality on ROCm includes tensor operations, neural network layers, automatic differentiation, distributed training, mixed-precision training, compilation features, and domain-specific libraries for audio, vision, text processing, and more.

### Supported domain libraries[#](#supported-domain-libraries)

PyTorch offers specialized [domain libraries](https://pytorch.org/domains/) with
GPU acceleration that build on its core features to support specific application
areas. The table below lists the PyTorch domain libraries that are compatible
with ROCm.

Library |
Description |
|---|---|
Audio and signal processing library for PyTorch. Provides utilities for audio I/O, signal and data processing functions, datasets, model implementations, and application components for audio and speech processing tasks.
|
|
PyTorch-native library designed for fine-tuning large language models (LLMs). Provides supports the full fine-tuning workflow and offers compatibility with popular production inference systems.
|
|
Computer vision library that is part of the PyTorch project. Provides popular datasets, model architectures, and common image transformations for computer vision applications. |
|
Text processing library for PyTorch. Provides data processing utilities and popular datasets for natural language processing, including tokenization, vocabulary management, and text embeddings.
|
|
Beta library of common modular data loading primitives for easily constructing flexible and performant data pipelines, with features still in prototype stage. |
|
PyTorch domain library for common sparsity and parallelism primitives needed for large-scale recommender systems, enabling authors to train models with large embedding tables shared across many GPUs.
|
|
Performant, flexible and easy-to-use tool for serving PyTorch models in production, providing features for model management, batch processing, and scalable deployment.
|
|
Open-source, Python-first Reinforcement Learning library for PyTorch with a focus on high modularity and good runtime performance, providing low and high-level RL abstractions and reusable functionals for cost functions, returns, and data processing.
|
|
Dictionary-like class that simplifies operations on batches of tensors, enhancing code readability, compactness, and modularity by abstracting tailored operations and reducing errors through automatic operation dispatching.
|

## Key features and enhancements for PyTorch 2.7 with ROCm 7.0[#](#key-features-and-enhancements-for-pytorch-2-7-with-rocm-7-0)

Enhanced TunableOp framework: Introduces

`tensorfloat32`

support for TunableOp operations, improved offline tuning for ScaledGEMM operations, submatrix offline tuning capabilities, and better logging for BLAS operations without bias vectors.Expanded GPU architecture support: Provides optimized support for newer GPU architectures, including gfx1200 and gfx1201 with preferred hipBLASLt backend selection, along with improvements for gfx950 and gfx1100 series GPUs.

Advanced Triton Integration: AOTriton 0.10b introduces official support for gfx950 and gfx1201, along with experimental support for gfx1101, gfx1151, gfx1150, and gfx1200.

Improved element-wise kernel performance: Delivers enhanced vectorized element-wise kernels with better support for heterogeneous tensor types and optimized input vectorization for tensors with mixed data types.

MIOpen deep learning optimizations: Enables NHWC BatchNorm by default on ROCm 7.0+, provides

`maxpool`

forward and backward performance improvements targeting ResNet scenarios, and includes updated launch configurations for better performance.Enhanced memory and tensor operations: Features fixes for in-place

`aten`

sum operations with specialized templated kernels, improved 3D tensor performance with NHWC format, and better handling of memory-bound matrix multiplication operations.Robust testing and quality improvements: Includes comprehensive test suite updates with improved tolerance handling for Navi3x architectures, generalized ROCm-specific test conditions, and enhanced unit test coverage for Flash Attention and Memory Efficient operations.

Composable Kernel (CK) updates: Features updated CK submodule integration with the latest optimizations and performance improvements for core mathematical operations.

Development and debugging enhancements: Includes improved source handling for dynamic compilation, better error handling for atomic operations, and enhanced state checking for trace operations.

Integrate APEX fused layer normalization, which can have positive impact on text-to-video models.

Integrate APEX distributed fused LAMB and distributed fused ADAM, which can have positive impact on BERT-L and Llama2-SFT.

FlashAttention v3 has been integrated for AMD GPUs.

[Pytorch C++ extensions](https://pytorch.org/tutorials/advanced/cpp_extension.html)provide a mechanism for compiling custom operations that can be used during network training or inference. For AMD platforms,`amdclang++`

has been validated as the supported compiler for building these extensions.

## Known issues and notes for PyTorch 2.7 with ROCm 7.0[#](#known-issues-and-notes-for-pytorch-2-7-with-rocm-7-0)

The

`matmul.allow_fp16_reduced_precision_reduction`

and`matmul.allow_bf16_reduced_precision_reduction`

options under`torch.backends.cuda`

are not supported. As a result, reduced-precision reductions using FP16 or BF16 accumulation types are not available.
