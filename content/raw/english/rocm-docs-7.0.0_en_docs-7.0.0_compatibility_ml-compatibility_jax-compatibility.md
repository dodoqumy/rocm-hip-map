---
title: "JAX compatibility"
source_url: "https://rocm.docs.amd.com/en/docs-7.0.0/compatibility/ml-compatibility/jax-compatibility.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T12:05:12.576697+00:00
content_hash: "00c1fd84be52e5c0"
---

# JAX compatibility[#](#jax-compatibility)

2025-11-20

9 min read time

JAX provides a NumPy-like API, which combines automatic differentiation and the Accelerated Linear Algebra (XLA) compiler to achieve high-performance machine learning at scale.

JAX uses composable transformations of Python and NumPy through just-in-time
(JIT) compilation, automatic vectorization, and parallelization. To learn about
JAX, including profiling and optimizations, see the official [JAX documentation](https://jax.readthedocs.io/en/latest/notebooks/quickstart.html).

ROCm support for JAX is upstreamed, and users can build the official source code with ROCm support:

ROCm JAX release:

Offers AMD-validated and community

[Docker images](#jax-docker-compat)with ROCm and JAX preinstalled.ROCm JAX repository:

[ROCm/rocm-jax](https://github.com/ROCm/rocm-jax)See the

[ROCm JAX installation guide](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.0.0/install/3rd-party/jax-install.html)to get started.

Official JAX release:

Official JAX repository:

[jax-ml/jax](https://github.com/jax-ml/jax)See the

[AMD GPU (Linux) installation section](https://jax.readthedocs.io/en/latest/installation.html#amd-gpu-linux)in the JAX documentation.


Note

AMD releases official [ROCm JAX Docker images](https://hub.docker.com/r/rocm/jax)
quarterly alongside new ROCm releases. These images undergo full AMD testing.
[Community ROCm JAX Docker images](https://hub.docker.com/r/rocm/jax-community)
follow upstream JAX releases and use the latest available ROCm version.

## JAX Plugin-PJRT with JAX/JAXLIB compatibility[#](#jax-plugin-pjrt-with-jax-jaxlib-compatibility)

Portable JIT Runtime (PJRT) is an open, stable interface for device runtime and compiler. The following table details the ROCm version compatibility matrix between JAX Plugin–PJRT and JAX/JAXLIB.

JAX Plugin-PJRT |
JAX/JAXLIB |
ROCm |
|---|---|---|
0.6.0 |
0.6.2, 0.6.0 |
7.0.0 |

## Use cases and recommendations[#](#use-cases-and-recommendations)

The

[nanoGPT in JAX](https://rocm.blogs.amd.com/artificial-intelligence/nanoGPT-JAX/README.html)blog explores the implementation and training of a Generative Pre-trained Transformer (GPT) model in JAX, inspired by Andrej Karpathy’s JAX-based nanoGPT. Comparing how essential GPT components—such as self-attention mechanisms and optimizers—are realized in JAX and JAX, also highlights JAX’s unique features.The

[Optimize GPT Training: Enabling Mixed Precision Training in JAX using ROCm on AMD GPUs](https://rocm.blogs.amd.com/artificial-intelligence/jax-mixed-precision/README.html)blog post provides a comprehensive guide on enhancing the training efficiency of GPT models by implementing mixed precision techniques in JAX, specifically tailored for AMD GPUs utilizing the ROCm platform.The

[Supercharging JAX with Triton Kernels on AMD GPUs](https://rocm.blogs.amd.com/artificial-intelligence/jax-triton/README.html)blog demonstrates how to develop a custom fused dropout-activation kernel for matrices using Triton, integrate it with JAX, and benchmark its performance using ROCm.The

[Distributed fine-tuning with JAX on AMD GPUs](https://rocm.blogs.amd.com/artificial-intelligence/distributed-sft-jax/README.html)outlines the process of fine-tuning a Bidirectional Encoder Representations from Transformers (BERT)-based large language model (LLM) using JAX for a text classification task. The blog post discuss techniques for parallelizing the fine-tuning across multiple AMD GPUs and assess the model’s performance on a holdout dataset. During the fine-tuning, a BERT-base-cased transformer model and the General Language Understanding Evaluation (GLUE) benchmark dataset was used on a multi-GPU setup.The

[MI300X workload optimization guide](https://rocm.docs.amd.com/en/latest/how-to/tuning-guides/mi300x/workload.html)provides detailed guidance on optimizing workloads for the AMD Instinct MI300X accelerator using ROCm. The page is aimed at helping users achieve optimal performance for deep learning and other high-performance computing tasks on the MI300X GPU.

For more use cases and recommendations, see [ROCm JAX blog posts](https://rocm.blogs.amd.com/blog/tag/jax.html).

## Docker image compatibility[#](#docker-image-compatibility)

AMD provides preconfigured Docker images with JAX and the ROCm backend.
These images are published on [Docker Hub](https://hub.docker.com/r/rocm/jax) and are the
recommended way to get started with deep learning with JAX on ROCm.
For `jax-community`

images, see [rocm/jax-community](https://hub.docker.com/r/rocm/jax-community/tags) on Docker Hub.

To find the right image tag, see the JAX on ROCm installation
documentation for a list of
available `rocm/jax`

images.

## Key ROCm libraries for JAX[#](#key-rocm-libraries-for-jax)

The following ROCm libraries represent potential targets that could be utilized by JAX on ROCm for various computational tasks. The actual libraries used will depend on the specific implementation and operations performed.

ROCm library |
Version |
Purpose |
|---|---|---|
3.0.0 |
Provides GPU-accelerated Basic Linear Algebra Subprograms (BLAS) for matrix and vector operations. |
|
1.0.0 |
hipBLASLt is an extension of hipBLAS, providing additional features like epilogues fused into the matrix multiplication kernel or use of integer tensor cores. |
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
3.5.0 |
Optimized for deep learning primitives such as convolutions, pooling, normalization, and activation functions. |
|
2.26.6 |
Optimized for multi-GPU communication for operations like all-reduce, broadcast, and scatter. |
|
4.0.0 |
Provides a C++ template library for parallel algorithms like sorting, reduction, and scanning. |

Note

This table shows ROCm libraries that could potentially be utilized by JAX. Not all libraries may be used in every configuration, and the actual library usage will depend on the specific operations and implementation details.

## Supported data types and modules[#](#supported-data-types-and-modules)

The following tables lists the supported public JAX API data types and modules.

### Supported data types[#](#supported-data-types)

ROCm supports all the JAX data types of [jax.dtypes](https://docs.jax.dev/en/latest/jax.dtypes.html)
module, [jax.numpy.dtype](https://docs.jax.dev/en/latest/_autosummary/jax.numpy.dtype.html)
and [default_dtype](https://docs.jax.dev/en/latest/default_dtypes.html) .
The ROCm supported data types in JAX are collected in the following table.

Data type |
Description |
|---|---|
|
16-bit bfloat (brain floating point). |
|
Boolean. |
|
128-bit complex. |
|
64-bit complex. |
|
16-bit (half precision) floating-point. |
|
32-bit (single precision) floating-point. |
|
64-bit (double precision) floating-point. |
|
16-bit (half precision) floating-point. |
|
Signed 16-bit integer. |
|
Signed 32-bit integer. |
|
Signed 64-bit integer. |
|
Signed 8-bit integer. |
|
Unsigned 16-bit (word) integer. |
|
Unsigned 32-bit (dword) integer. |
|
Unsigned 64-bit (qword) integer. |
|
Unsigned 8-bit (byte) integer. |

### Supported modules[#](#supported-modules)

For a complete and up-to-date list of JAX public modules (for example, `jax.numpy`

,
`jax.scipy`

, `jax.lax`

), their descriptions, and usage, please refer directly to the
[official JAX API documentation](https://jax.readthedocs.io/en/latest/jax.html).

Note

Since version 0.1.56, JAX has full support for ROCm, and the
[Known issues and important notes](#jax-comp-known-issues) section
contains details about limitations specific to the ROCm backend. The list of
JAX API modules are maintained by the JAX project and is subject to change.
Refer to the official Jax documentation for the most up-to-date information.

## Key features and enhancements for ROCm 7.0[#](#key-features-and-enhancements-for-rocm-7-0)

Upgraded XLA backend: Integrates a newer XLA version, enabling better optimizations, broader operator support, and potential performance gains.

RNN support: Native RNN support (including LSTMs via

`jax.experimental.rnn`

) now available on ROCm, aiding sequence model development.Comprehensive linear algebra capabilities: Offers robust

`jax.linalg`

operations, essential for scientific and machine learning tasks.Expanded AMD GPU architecture support: Provides ongoing support for gfx1101 GPUs and introduces support for gfx950 and gfx12xx GPUs.

Mixed FP8 precision support: Enables

`lax.dot_general`

operations with mixed FP8 types, offering pathways for memory and compute efficiency.Streamlined PyPi packaging: Provides reliable PyPi wheels for JAX on ROCm, simplifying the installation process.

Pallas experimental kernel development: Continued Pallas framework enhancements for custom GPU kernels, including new intrinsics (specific kernel behaviors under review).

Improved build system and CI: Enhanced ROCm build system and CI for greater reliability and maintainability.

Enhanced distributed computing setup: Improved JAX setup in multi-GPU distributed environments.


## Known issues and notes for ROCm 7.0[#](#known-issues-and-notes-for-rocm-7-0)

`nn.dot_product_attention`

: Certain configurations of`jax.nn.dot_product_attention`

may cause segmentation faults, though the majority of use cases work correctly.SVD with dynamic shapes: SVD on inputs with dynamic/symbolic shapes might result in an error. SVD with static shapes is unaffected.

QR decomposition with symbolic shapes: QR decomposition operations may fail when using symbolic/dynamic shapes in shape polymorphic contexts.

Pallas kernels: Specific advanced Pallas kernels may exhibit variations in numerical output or resource usage. These are actively reviewed as part of Pallas’s experimental development.
