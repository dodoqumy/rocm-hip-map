---
title: "Deep learning compilation with MIGraphX"
source_url: "https://rocm.docs.amd.com/projects/AMDMIGraphX/en/latest/conceptual/deep-learning-compilation.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:25:12.076453+00:00
content_hash: "b75bea39bf6782cb"
---

# Deep learning compilation with MIGraphX[#](#deep-learning-compilation-with-migraphx)

2025-10-28

2 min read time

The MIGraphX deep learning (DL) compiler improves inference by analyzing a model’s compute graph and applying program transformations. After optimization, the compiler lowers graph operations to device kernels (from libraries or via code generation) for efficient execution.

A common transformation is kernel fusion; where compatible operations are merged into a single kernel launch. Fusion reduces launch overhead and avoids extra reads or writes between host and device, which typically improves latency and throughput. By applying graph-level optimizations and choosing or generating efficient device kernels, MIGraphX delivers high-performance over uncompiled models and less optimized compiled solutions.

An overview of the compilation process for MIGraphX is shown below in
`compilation-label`

. One type of optimization that MIGraphX
performs are kernel fusions such as the Attention fusion seen in
`attention-label`

.



## What MIGraphX provides[#](#what-migraphx-provides)

**End-to-end:**compilation and execution of DL models on AMD GPUs**C++ implementation:**with Python and C++ APIs**Model inputs:**ONNX and TensorFlow

PyTorch through

[ROCm/torch_migraphx](https://github.com/ROCm/torch_migraphx)ONNX Runtime execution provider



**Hardware targets:**AMD Navi (consumer) and MI (server) GPUs**Supported data types:**FP16, BF16, OCP FP8, INT8, INT4
