---
title: "System setup for AI workloads on ROCm"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/system-setup/index.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-03T06:16:28.672910+00:00
content_hash: "418aa7fa231c7bb8"
---

# System setup for AI workloads on ROCm[#](#system-setup-for-ai-workloads-on-rocm)

2026-01-23

3 min read time

Before you begin training or inference on AMD Instinct™ GPUs, complete the following system setup and validation steps to ensure optimal performance.

## Prerequisite system validation[#](#prerequisite-system-validation)

First, confirm that your system meets all software and hardware prerequisites.
See [Prerequisite system validation before running AI workloads](prerequisite-system-validation.html).

## Docker images for AMD Instinct GPUs[#](#docker-images-for-amd-instinct-gpus)

AMD provides prebuilt Docker images for AMD Instinct™ MI300X and MI325X GPUs. These images include ROCm-enabled deep learning frameworks and essential software components. They support single-node and multi-node configurations and are ready for training and inference workloads out of the box.

### Multi-node training[#](#multi-node-training)

For instructions on enabling multi-node training, see [Multi-node setup for AI workloads](multi-node-setup.html).

## System optimization and validation[#](#system-optimization-and-validation)

Before running workloads, verify that the system is configured correctly and operating at peak efficiency. Recommended steps include:

Disabling NUMA auto-balancing

Running system benchmarks to validate hardware performance


For details on running system health checks, see [System health benchmarks for AI workloads](system-health-check.html).
