---
title: "Use ROCm for training"
source_url: "https://rocm.docs.amd.com/en/docs-6.4.0/how-to/rocm-for-ai/training/index.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T16:06:58.344631+00:00
content_hash: "d15ebf0dd5ec09b6"
---

# Use ROCm for training[#](#use-rocm-for-training)

2025-05-13

3 min read time

Training models is the process of teaching a computer program to recognize patterns in data. This involves providing the computer with large amounts of labeled data and allowing it to learn from that data, adjusting the model’s parameters.

The process of training models is computationally intensive, requiring specialized hardware like GPUs to accelerate computations and reduce training time. Training models on AMD GPUs involves leveraging the parallel processing capabilities of these GPUs to significantly speed up the model training process in machine learning and deep learning tasks.

Training models on AMD GPUs with the ROCm™ software platform allows you to use the powerful parallel processing capabilities and efficient compute resource management, significantly improving training time and overall performance in machine learning applications.

The ROCm software platform makes it easier to train models on AMD GPUs while maintaining compatibility with existing code and tools. The platform also provides features like multi-GPU support, allowing for scaling and parallelization of model training across multiple GPUs to enhance performance.

The AI Developer Hub contains [AMD ROCm tutorials](https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/) for
training, fine-tuning, and inference. It leverages popular machine learning frameworks on AMD GPUs.

In this guide, you’ll learn about:

Training a model
