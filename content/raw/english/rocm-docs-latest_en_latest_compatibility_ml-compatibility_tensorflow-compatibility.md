---
title: "TensorFlow compatibility"
source_url: "https://rocm.docs.amd.com/en/latest/compatibility/ml-compatibility/tensorflow-compatibility.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T06:58:08.581675+00:00
content_hash: "0ee6a5c1220f7d5b"
---

:::::::::::::::::::::::::::::::::::::::::::::
{#main-content .bd-main role="main"}

sbt-scroll-pixel-helper

:::::::::::::::::::::::::::::::::::::::::::
bd-content
::::::::::::::::::::::::::::::::::::::
bd-article-container
:::::::
{.bd-header-article .d-print-none}
::::::
{.header-article-items .header-article__inner}
::
header-article-items__start

header-article-item
[]{.fa-solid .fa-angle-right}

header-article-item

::

::
header-article-items__end
:
header-article-item

article-header-buttons
[]{.fa-solid .fa-list}

:
::
::::::
:::::::

{#jb-print-docs-body .onlyprint}
# TensorFlow compatibility

::
{#print-main-content}
:
{#jb-print-toc}

{}
## Contents

:
::

{#searchbox}

::::::::::::::::::::::::
{#tensorflow-compatibility .section}
# TensorFlow compatibility[\#](#tensorflow-compatibility "Link to this heading"){.headerlink}

::::::::
{#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::
{.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::
{.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::
{.sd-container-fluid .sd-sphinx-override .docutils}
::::
{.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}

{.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23

{.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 11 min read time

{.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils style="color:gray;"}
Applies to Linux

{.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}

::::
:::::
::::::
:::::::
::::::::

[TensorFlow](https://www.tensorflow.org/){.reference .external} is an open-source library for solving machine learning, deep learning, and AI problems. It can solve many problems across different sectors and industries, but primarily focuses on neural network training and inference. It is one of the most popular deep learning frameworks and is very active in open-source development.

:
{#support-overview .section}
## Support overview[\#](#support-overview "Link to this heading"){.headerlink}

- The ROCm-supported version of TensorFlow is maintained in the official [ROCm/tensorflow-upstream](https://github.com/ROCm/tensorflow-upstream){.github .reference .external} repository, which differs from the [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow){.github .reference .external} upstream repository.

- To get started and install TensorFlow on ROCm, use the prebuilt [[Docker images]{.std .std-ref}](#tensorflow-docker-compat){.reference .internal}, which include ROCm, TensorFlow, and all required dependencies.

  - See the [[ROCm TensorFlow installation guide]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/tensorflow-install.html "(in ROCm installation on Linux v7.2.2)"){.reference .external} for installation and setup instructions.

  - You can also consult the [TensorFlow API versions](https://www.tensorflow.org/versions){.reference .external} list for additional context.

{#version-support .section}
### Version support[\#](#version-support "Link to this heading"){.headerlink}

The [official TensorFlow repository](http://github.com/tensorflow/tensorflow){.reference .external} includes full ROCm support. AMD maintains a TensorFlow [ROCm repository](http://github.com/rocm/tensorflow-upstream){.reference .external} in order to quickly add bug fixes, updates, and support for the latest ROCm versions.

:

{#docker-image-compatibility .section}
[]{#tensorflow-docker-compat}

## Docker image compatibility[\#](#docker-image-compatibility "Link to this heading"){.headerlink}

AMD provides preconfigured Docker images with TensorFlow and the ROCm backend. These images are published on [Docker Hub](https://hub.docker.com/r/rocm/tensorflow){.reference .external} and are the recommended way to get started with deep learning with TensorFlow on ROCm.

To find the right image tag, see the [[TensorFlow on ROCm installation documentation]{.xref .std .std-ref}](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/tensorflow-install.html#tensorflow-docker-support "(in ROCm installation on Linux v7.2.2)"){.reference .external} for a list of available [`rocm/tensorflow`{.docutils .literal .notranslate}]{.pre} images.

:
{#critical-rocm-libraries-for-tensorflow .section}
## Critical ROCm libraries for TensorFlow[\#](#critical-rocm-libraries-for-tensorflow "Link to this heading"){.headerlink}

TensorFlow depends on multiple components and the supported features of those components can affect the TensorFlow ROCm supported feature set. The versions in the following table refer to the first TensorFlow version where the ROCm library was introduced as a dependency. The versions described are available in ROCm 7.2.2/7.2.1.

pst-scrollable-table-container
+----------------------------------------------------------------------+------------------------------+---------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ROCm library                                                         | Version                      | Purpose                                                                                                             | Used in                                                                                                                                                                                                                                                                                                                  |
+======================================================================+==============================+=====================================================================================================================+==========================================================================================================================================================================================================================================================================================================================+
| [hipBLAS](https://github.com/ROCm/hipBLAS){.reference .external}     | [3.2.0]{.version-reference}  | Provides GPU-accelerated Basic Linear Algebra Subprograms (BLAS) for matrix and vector operations.                  | Accelerates operations like [`tf.matmul`{.docutils .literal .notranslate}]{.pre}, [`tf.linalg.matmul`{.docutils .literal .notranslate}]{.pre}, and other matrix multiplications commonly used in neural network layers.                                                                                                  |
+----------------------------------------------------------------------+------------------------------+---------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [hipBLASLt](https://github.com/ROCm/hipBLASLt){.reference .external} | [1.2.2]{.version-reference}  | Extends hipBLAS with additional optimizations like fused kernels and integer tensor cores.                          | Optimizes matrix multiplications and linear algebra operations used in layers like dense, convolutional, and RNNs in TensorFlow.                                                                                                                                                                                         |
+----------------------------------------------------------------------+------------------------------+---------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [hipCUB](https://github.com/ROCm/hipCUB){.reference .external}       | [4.2.0]{.version-reference}  | Provides a C++ template library for parallel algorithms for reduction, scan, sort and select.                       | Supports operations like [`tf.reduce_sum`{.docutils .literal .notranslate}]{.pre}, [`tf.cumsum`{.docutils .literal .notranslate}]{.pre}, [`tf.sort`{.docutils .literal .notranslate}]{.pre} and other tensor operations in TensorFlow, especially those involving scanning, sorting, and filtering.                      |
+----------------------------------------------------------------------+------------------------------+---------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [hipFFT](https://github.com/ROCm/hipFFT){.reference .external}       | [1.0.22]{.version-reference} | Accelerates Fast Fourier Transforms (FFT) for signal processing tasks.                                              | Used for operations like signal processing, image filtering, and certain types of neural networks requiring FFT-based transformations.                                                                                                                                                                                   |
+----------------------------------------------------------------------+------------------------------+---------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [hipSOLVER](https://github.com/ROCm/hipSOLVER){.reference .external} | [3.2.0]{.version-reference}  | Provides GPU-accelerated direct linear solvers for dense and sparse systems.                                        | Optimizes linear algebra functions such as solving systems of linear equations, often used in optimization and training tasks.                                                                                                                                                                                           |
+----------------------------------------------------------------------+------------------------------+---------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [hipSPARSE](https://github.com/ROCm/hipSPARSE){.reference .external} | [4.2.0]{.version-reference}  | Optimizes sparse matrix operations for efficient computations on sparse data.                                       | Accelerates sparse matrix operations in models with sparse weight matrices or activations, commonly used in neural networks.                                                                                                                                                                                             |
+----------------------------------------------------------------------+------------------------------+---------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [MIOpen](https://github.com/ROCm/MIOpen){.reference .external}       | [3.5.1]{.version-reference}  | Provides optimized deep learning primitives such as convolutions, pooling, normalization, and activation functions. | Speeds up convolutional neural networks (CNNs) and other layers. Used in TensorFlow for layers like [`tf.nn.conv2d`{.docutils .literal .notranslate}]{.pre}, [`tf.nn.relu`{.docutils .literal .notranslate}]{.pre}, and [`tf.nn.lstm_cell`{.docutils .literal .notranslate}]{.pre}.                                      |
+----------------------------------------------------------------------+------------------------------+---------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [RCCL](https://github.com/ROCm/rccl){.reference .external}           | [2.27.7]{.version-reference} | Optimizes for multi-GPU communication for operations like AllReduce and Broadcast.                                  | Distributed data parallel training ([`tf.distribute.MirroredStrategy`{.docutils .literal .notranslate}]{.pre}). Handles communication in multi-GPU setups.                                                                                                                                                               |
+----------------------------------------------------------------------+------------------------------+---------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [rocThrust](https://github.com/ROCm/rocThrust){.reference .external} | [4.2.0]{.version-reference}  | Provides a C++ template library for parallel algorithms like sorting, reduction, and scanning.                      | Reduction operations like [`tf.reduce_sum`{.docutils .literal .notranslate}]{.pre}, [`tf.cumsum`{.docutils .literal .notranslate}]{.pre} for computing the cumulative sum of elements along a given axis or [`tf.unique`{.docutils .literal .notranslate}]{.pre} to finds unique elements in a tensor can use rocThrust. |
+----------------------------------------------------------------------+------------------------------+---------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

:

::::::
{#supported-and-unsupported-features .section}
## Supported and unsupported features[\#](#supported-and-unsupported-features "Link to this heading"){.headerlink}

The following section maps supported data types and GPU-accelerated TensorFlow features to their minimum supported ROCm and TensorFlow versions.

:
{#data-types .section}
### Data types[\#](#data-types "Link to this heading"){.headerlink}

The data type of a tensor is specified using the [`dtype`{.docutils .literal .notranslate}]{.pre} attribute or argument, and TensorFlow supports a wide range of data types for different use cases.

The basic, single data types of [tf.dtypes](https://www.tensorflow.org/api_docs/python/tf/dtypes){.reference .external} are as follows:

pst-scrollable-table-container
  Data type                                               Description                                            Since TensorFlow   Since ROCm
  ------------------------------------------------------- ------------------------------------------------------ ------------------ ------------
  [`bfloat16`{.docutils .literal .notranslate}]{.pre}     16-bit bfloat (brain floating point).                  1.0.0              1.7
  [`bool`{.docutils .literal .notranslate}]{.pre}         Boolean.                                               1.0.0              1.7
  [`complex128`{.docutils .literal .notranslate}]{.pre}   128-bit complex.                                       1.0.0              1.7
  [`complex64`{.docutils .literal .notranslate}]{.pre}    64-bit complex.                                        1.0.0              1.7
  [`double`{.docutils .literal .notranslate}]{.pre}       64-bit (double precision) floating-point.              1.0.0              1.7
  [`float16`{.docutils .literal .notranslate}]{.pre}      16-bit (half precision) floating-point.                1.0.0              1.7
  [`float32`{.docutils .literal .notranslate}]{.pre}      32-bit (single precision) floating-point.              1.0.0              1.7
  [`float64`{.docutils .literal .notranslate}]{.pre}      64-bit (double precision) floating-point.              1.0.0              1.7
  [`half`{.docutils .literal .notranslate}]{.pre}         16-bit (half precision) floating-point.                2.0.0              2.0
  [`int16`{.docutils .literal .notranslate}]{.pre}        Signed 16-bit integer.                                 1.0.0              1.7
  [`int32`{.docutils .literal .notranslate}]{.pre}        Signed 32-bit integer.                                 1.0.0              1.7
  [`int64`{.docutils .literal .notranslate}]{.pre}        Signed 64-bit integer.                                 1.0.0              1.7
  [`int8`{.docutils .literal .notranslate}]{.pre}         Signed 8-bit integer.                                  1.0.0              1.7
  [`qint16`{.docutils .literal .notranslate}]{.pre}       Signed quantized 16-bit integer.                       1.0.0              1.7
  [`qint32`{.docutils .literal .notranslate}]{.pre}       Signed quantized 32-bit integer.                       1.0.0              1.7
  [`qint8`{.docutils .literal .notranslate}]{.pre}        Signed quantized 8-bit integer.                        1.0.0              1.7
  [`quint16`{.docutils .literal .notranslate}]{.pre}      Unsigned quantized 16-bit integer.                     1.0.0              1.7
  [`quint8`{.docutils .literal .notranslate}]{.pre}       Unsigned quantized 8-bit integer.                      1.0.0              1.7
  [`resource`{.docutils .literal .notranslate}]{.pre}     Handle to a mutable, dynamically allocated resource.   1.0.0              1.7
  [`string`{.docutils .literal .notranslate}]{.pre}       Variable-length string, represented as byte array.     1.0.0              1.7
  [`uint16`{.docutils .literal .notranslate}]{.pre}       Unsigned 16-bit (word) integer.                        1.0.0              1.7
  [`uint32`{.docutils .literal .notranslate}]{.pre}       Unsigned 32-bit (dword) integer.                       1.5.0              1.7
  [`uint64`{.docutils .literal .notranslate}]{.pre}       Unsigned 64-bit (qword) integer.                       1.5.0              1.7
  [`uint8`{.docutils .literal .notranslate}]{.pre}        Unsigned 8-bit (byte) integer.                         1.0.0              1.7
  [`variant`{.docutils .literal .notranslate}]{.pre}      Data of arbitrary type (known at runtime).             1.4.0              1.7

:

:
{#features .section}
### Features[\#](#features "Link to this heading"){.headerlink}

This table provides an overview of key features in TensorFlow and their availability in ROCm.

pst-scrollable-table-container
  Module                                                                                         Description                                                                                                                                                                                                                                                                                                                                                                                                          Since TensorFlow   Since ROCm
  ---------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------ ------------
  [`tf.linalg`{.docutils .literal .notranslate}]{.pre} (Linear Algebra)                          Operations for matrix and tensor computations, such as [`tf.linalg.matmul`{.docutils .literal .notranslate}]{.pre} (matrix multiplication), [`tf.linalg.inv`{.docutils .literal .notranslate}]{.pre} (matrix inversion) and [`tf.linalg.cholesky`{.docutils .literal .notranslate}]{.pre} (Cholesky decomposition). These leverage GPUs for high-performance linear algebra operations.                              1.4                1.8.2
  [`tf.nn`{.docutils .literal .notranslate}]{.pre} (Neural Network Operations)                   GPU-accelerated building blocks for deep learning models, such as 2D convolutions with [`tf.nn.conv2d`{.docutils .literal .notranslate}]{.pre}, max pooling operations with [`tf.nn.max_pool`{.docutils .literal .notranslate}]{.pre}, activation functions like [`tf.nn.relu`{.docutils .literal .notranslate}]{.pre} or softmax for output layers with [`tf.nn.softmax`{.docutils .literal .notranslate}]{.pre}.   1.0                1.8.2
  [`tf.image`{.docutils .literal .notranslate}]{.pre} (Image Processing)                         GPU-accelerated functions for image preprocessing and augmentations, such as resize images with [`tf.image.resize`{.docutils .literal .notranslate}]{.pre}, flip images horizontally with [`tf.image.flip_left_right`{.docutils .literal .notranslate}]{.pre} and adjust image brightness randomly with [`tf.image.random_brightness`{.docutils .literal .notranslate}]{.pre}.                                       1.1                1.8.2
  [`tf.keras`{.docutils .literal .notranslate}]{.pre} (High-Level API)                           GPU acceleration for Keras layers and models, including dense layers ([`tf.keras.layers.Dense`{.docutils .literal .notranslate}]{.pre}), convolutional layers ([`tf.keras.layers.Conv2D`{.docutils .literal .notranslate}]{.pre}) and recurrent layers ([`tf.keras.layers.LSTM`{.docutils .literal .notranslate}]{.pre}).                                                                                            1.4                1.8.2
  [`tf.math`{.docutils .literal .notranslate}]{.pre} (Mathematical Operations)                   GPU-accelerated mathematical operations, such as sum across dimensions with [`tf.math.reduce_sum`{.docutils .literal .notranslate}]{.pre}, elementwise exponentiation with [`tf.math.exp`{.docutils .literal .notranslate}]{.pre} and sigmoid activation ([`tf.math.sigmoid`{.docutils .literal .notranslate}]{.pre}).                                                                                               1.5                1.8.2
  [`tf.signal`{.docutils .literal .notranslate}]{.pre} (Signal Processing)                       Functions for spectral analysis and signal transformations.                                                                                                                                                                                                                                                                                                                                                          1.13               2.1
  [`tf.data`{.docutils .literal .notranslate}]{.pre} (Data Input Pipeline)                       GPU-accelerated data preprocessing for efficient input pipelines, Prefetching with [`tf.data.experimental.AUTOTUNE`{.docutils .literal .notranslate}]{.pre}. GPU-enabled transformations like map and batch.                                                                                                                                                                                                         1.4                1.8.2
  [`tf.distribute`{.docutils .literal .notranslate}]{.pre} (Distributed Training)                Enabling to scale computations across multiple devices on a single machine or across multiple machines.                                                                                                                                                                                                                                                                                                              1.13               2.1
  [`tf.random`{.docutils .literal .notranslate}]{.pre} (Random Number Generation)                GPU-accelerated random number generation                                                                                                                                                                                                                                                                                                                                                                             1.12               1.9.2
  [`tf.TensorArray`{.docutils .literal .notranslate}]{.pre} (Dynamic Array Operations)           Enables dynamic tensor manipulation on GPUs.                                                                                                                                                                                                                                                                                                                                                                         1.0                1.8.2
  [`tf.sparse`{.docutils .literal .notranslate}]{.pre} (Sparse Tensor Operations)                GPU-accelerated sparse matrix manipulations.                                                                                                                                                                                                                                                                                                                                                                         1.9                1.9.0
  [`tf.experimental.numpy`{.docutils .literal .notranslate}]{.pre}                               GPU-accelerated NumPy-like API for numerical computations.                                                                                                                                                                                                                                                                                                                                                           2.4                4.1.1
  [`tf.RaggedTensor`{.docutils .literal .notranslate}]{.pre}                                     Handling of variable-length sequences and ragged tensors with GPU support.                                                                                                                                                                                                                                                                                                                                           1.13               2.1
  [`tf.function`{.docutils .literal .notranslate}]{.pre} with XLA (Accelerated Linear Algebra)   Enable GPU-accelerated functions in optimization.                                                                                                                                                                                                                                                                                                                                                                    1.14               2.4
  [`tf.quantization`{.docutils .literal .notranslate}]{.pre}                                     Quantized operations for inference, accelerated on GPUs.                                                                                                                                                                                                                                                                                                                                                             1.12               1.9.2

:

:
{#distributed-library-features .section}
### Distributed library features[\#](#distributed-library-features "Link to this heading"){.headerlink}

Enables developers to scale computations across multiple devices on a single machine or across multiple machines.

pst-scrollable-table-container
  Feature                                                                  Description                                                                        Since TensorFlow   Since ROCm
  ------------------------------------------------------------------------ ---------------------------------------------------------------------------------- ------------------ ------------
  [`MultiWorkerMirroredStrategy`{.docutils .literal .notranslate}]{.pre}   Synchronous training across multiple workers using mirrored variables.             2.0                3.0
  [`MirroredStrategy`{.docutils .literal .notranslate}]{.pre}              Synchronous training across multiple GPUs on one machine.                          1.5                2.5
  [`TPUStrategy`{.docutils .literal .notranslate}]{.pre}                   Efficiently trains models on Google TPUs.                                          1.9                ❌
  [`ParameterServerStrategy`{.docutils .literal .notranslate}]{.pre}       Asynchronous training using parameter servers for variable management.             2.1                4.0
  [`CentralStorageStrategy`{.docutils .literal .notranslate}]{.pre}        Keeps variables on a single device and performs computation on multiple devices.   2.3                4.1
  [`CollectiveAllReduceStrategy`{.docutils .literal .notranslate}]{.pre}   Synchronous training across multiple devices and hosts.                            1.14               3.5
  Distribution Strategies API                                              High-level API to simplify distributed training configuration and execution.       1.10               3.0

:
::::::

:
{#unsupported-tensorflow-features .section}
## Unsupported TensorFlow features[\#](#unsupported-tensorflow-features "Link to this heading"){.headerlink}

The following are GPU-accelerated TensorFlow features not currently supported by ROCm.

pst-scrollable-table-container
  Feature                                                                Description                                                                                                                                                                            Since TensorFlow
  ---------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------
  Mixed Precision with TF32                                              Mixed precision with TF32 is used for matrix multiplications, convolutions, and other linear algebra operations, particularly in deep learning workloads like CNNs and transformers.   2.4
  [`tf.distribute.TPUStrategy`{.docutils .literal .notranslate}]{.pre}   Efficiently trains models on Google TPUs.                                                                                                                                              1.9

:

{#use-cases-and-recommendations .section}
## Use cases and recommendations[\#](#use-cases-and-recommendations "Link to this heading"){.headerlink}

- The [Training a Neural Collaborative Filtering (NCF) Recommender on an AMD GPU](https://rocm.blogs.amd.com/artificial-intelligence/ncf/README.html){.reference .external} blog post discusses training an NCF recommender system using TensorFlow. It explains how NCF improves traditional collaborative filtering methods by leveraging neural networks to model non-linear user-item interactions. The post outlines the implementation using the recommenders library, focusing on the use of implicit data (for example, user interactions like viewing or purchasing) and how it addresses challenges like the lack of negative values.

- The [Creating a PyTorch/TensorFlow code environment on AMD GPUs](https://rocm.blogs.amd.com/software-tools-optimization/pytorch-tensorflow-env/README.html){.reference .external} blog post provides instructions for creating a machine learning environment for PyTorch and TensorFlow on AMD GPUs using ROCm. It covers steps like installing the libraries, cloning code repositories, installing dependencies, and troubleshooting potential issues with CUDA-based code. Additionally, it explains how to HIPify code (port CUDA code to HIP) and manage Docker images for a better experience on AMD GPUs. This guide aims to help data scientists and ML practitioners adapt their code for AMD GPUs.

For more use cases and recommendations, see the [ROCm Tensorflow blog posts](https://rocm.blogs.amd.com/blog/tag/tensorflow.html){.reference .external}.

::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::

{.bd-sidebar-secondary .bd-toc}
::
{.sidebar-secondary-items .sidebar-secondary__inner}
:
sidebar-secondary-item

{.page-toc .tocsection .onthispage}
Contents

:
::

:::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::
