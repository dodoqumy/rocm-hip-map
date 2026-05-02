---
title: "Programming guide"
source_url: "https://rocm.docs.amd.com/en/docs-7.0.0/how-to/programming_guide.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:02:39.963213+00:00
content_hash: "23d9f69ea4b47784"
---

# Programming guide[#](#programming-guide)

2025-08-14

3 min read time

ROCm provides a robust environment for heterogeneous programs running on CPUs and AMD GPUs. ROCm supports various programming languages and frameworks to help developers access the power of AMD GPUs. The natively supported programming languages are HIP (Heterogeneous-Compute Interface for Portability) and OpenCL, but HIP bindings are available for Python and Fortran.

HIP is an API based on C++ that provides a runtime and kernel language for GPU programming and is the essential ROCm programming language. HIP is also designed to be a marshalling language, allowing code written for NVIDIA CUDA to be easily ported to run on AMD GPUs. Developers can use HIP to write kernels that execute on AMD GPUs while maintaining compatibility with CUDA-based systems.

OpenCL (Open Computing Language) is an open standard for cross-platform,
parallel programming of diverse processors. ROCm supports OpenCL for developers
who want to use standard frameworks across different hardware platforms,
including CPUs, GPUs, and other accelerators. For more information, see
[OpenCL](https://www.khronos.org/opencl/).

Python bindings can be found at [ROCm/hip-python](https://github.com/ROCm/hip-python).
Python is popular in AI and machine learning applications due to available
frameworks like TensorFlow and PyTorch.

Fortran bindings can be found at [ROCm/hipfort](https://github.com/ROCm/hipfort).
It enables scientific, academic, and legacy applications, particularly those in
high-performance computing, to run on AMD GPUs via HIP.

For a complete description of the HIP programming language, see the [HIP programming guide](https://rocm.docs.amd.com/projects/HIP/en/docs-7.0.0/index.html).
