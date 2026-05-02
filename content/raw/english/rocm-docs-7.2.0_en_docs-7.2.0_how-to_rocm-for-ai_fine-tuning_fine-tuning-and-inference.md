---
title: "Fine-tuning and inference"
source_url: "https://rocm.docs.amd.com/en/docs-7.2.0/how-to/rocm-for-ai/fine-tuning/fine-tuning-and-inference.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T18:02:27.545167+00:00
content_hash: "c568e39fad6c9b6d"
---

# Fine-tuning and inference[#](#fine-tuning-and-inference)

2025-12-12

3 min read time

Fine-tuning using ROCm involves leveraging AMD’s GPU-accelerated [libraries](https://rocm.docs.amd.com/en/docs-7.2.0/reference/api-libraries.html) and
[tools](https://rocm.docs.amd.com/en/docs-7.2.0/reference/rocm-tools.html) to optimize and train deep learning models. ROCm provides a comprehensive
ecosystem for deep learning development, including open-source libraries for optimized deep learning operations and
ROCm-aware versions of [deep learning frameworks](../../deep-learning-rocm.html) such as PyTorch, TensorFlow, and JAX.

Single-accelerator systems, such as a machine equipped with a single GPU, are commonly used for
smaller-scale deep learning tasks, including fine-tuning pre-trained models and running inference on moderately
sized datasets. See [Fine-tuning and inference using a single GPU](single-gpu-fine-tuning-and-inference.html).

Multi-accelerator systems, on the other hand, consist of multiple GPUs working in parallel. These systems are
typically used in LLMs and other large-scale deep learning tasks where performance, scalability, and the handling of
massive datasets are crucial. See [Fine-tuning and inference using multiple GPUs](multi-gpu-fine-tuning-and-inference.html).
