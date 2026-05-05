---
title: "Use ROCm for fine-tuning LLMs"
source_url: "https://rocm.docs.amd.com/en/docs-7.0.0/how-to/rocm-for-ai/fine-tuning/index.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T18:03:27.360254+00:00
content_hash: "d382405bac8b14a5"
---

# Use ROCm for fine-tuning LLMs[#](#use-rocm-for-fine-tuning-llms)

2025-08-14

3 min read time

Fine-tuning is an essential technique in machine learning, where a pre-trained model, typically trained on a large-scale dataset, is further refined to achieve better performance and adapt to a particular task or dataset of interest.

With AMD GPUs, the fine-tuning process benefits from the parallel processing capabilities and efficient resource management, ultimately leading to improved performance and faster model adaptation to the target domain.

The ROCm™ software platform helps you optimize this fine-tuning process by supporting various optimization techniques tailored for AMD GPUs. It empowers the fine-tuning of large language models, making them accessible and efficient for specialized tasks. ROCm supports the broader AI ecosystem to ensure seamless integration with open frameworks, models, and tools.

Throughout the following topics, this guide discusses the goals and [challenges of fine-tuning a large language
model](overview.html#fine-tuning-llms-concept-challenge) like Llama 2. In the
sections that follow, you’ll find practical guides on libraries and tools to accelerate your fine-tuning.

The AI Developer Hub contains [AMD ROCm tutorials](https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/) for
training, fine-tuning, and inference. It leverages popular machine learning frameworks on AMD GPUs.

[Fine-tuning and inference](fine-tuning-and-inference.html)using a[single-accelerator](single-gpu-fine-tuning-and-inference.html)or[multi-accelerator](multi-gpu-fine-tuning-and-inference.html)system.
