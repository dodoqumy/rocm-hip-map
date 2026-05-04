---
title: "Fine-tuning and inference"
source_url: "https://rocm.docs.amd.com/en/docs-6.2.0/how-to/llm-fine-tuning-optimization/fine-tuning-and-inference.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T16:22:48.945418+00:00
content_hash: "eed72b1b71093015"
---

# Fine-tuning and inference[#](#fine-tuning-and-inference)



Fine-tuning using ROCm involves leveraging AMD’s GPU-accelerated [libraries](https://rocm.docs.amd.com/en/docs-6.2.0/reference/api-libraries.html) and
[tools](https://rocm.docs.amd.com/en/docs-6.2.0/reference/rocm-tools.html) to optimize and train deep learning models. ROCm provides a comprehensive
ecosystem for deep learning development, including open-source libraries for optimized deep learning operations and
ROCm-aware versions of [deep learning frameworks](../deep-learning-rocm.html) such as PyTorch, TensorFlow, and JAX.

Single-accelerator systems, such as a machine equipped with a single accelerator or GPU, are commonly used for
smaller-scale deep learning tasks, including fine-tuning pre-trained models and running inference on moderately
sized datasets. See [Fine-tuning and inference using a single accelerator](single-gpu-fine-tuning-and-inference.html).

Multi-accelerator systems, on the other hand, consist of multiple accelerators working in parallel. These systems are
typically used in LLMs and other large-scale deep learning tasks where performance, scalability, and the handling of
massive datasets are crucial. See [Fine-tuning and inference using multiple accelerators](multi-gpu-fine-tuning-and-inference.html).
