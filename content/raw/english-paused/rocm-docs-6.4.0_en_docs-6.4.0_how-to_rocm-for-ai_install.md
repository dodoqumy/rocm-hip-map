---
title: "Installing ROCm and machine learning frameworks"
source_url: "https://rocm.docs.amd.com/en/docs-6.4.0/how-to/rocm-for-ai/install.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:22:05.865623+00:00
content_hash: "ffeb5bba84cbe151"
---

# Installing ROCm and machine learning frameworks[#](#installing-rocm-and-machine-learning-frameworks)

2025-07-02

3 min read time

Before getting started, install ROCm and supported machine learning frameworks.

If you’re new to ROCm, refer to the [ROCm quick start install guide for Linux](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-6.4.0/install/quick-start.html).

If you’re using a Radeon GPU for graphics-accelerated applications, refer to the
[Radeon installation instructions](https://rocm.docs.amd.com/projects/radeon/en/docs-6.1.3/docs/install/native_linux/install-radeon.html).

ROCm supports multiple [installation methods](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-6.4.0/install/install-overview.html):

Follow the [post-installation instructions](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-6.4.0/install/post-install.html) to
configure your system linker, PATH, and verify the installation.

If you encounter any issues during installation, refer to the
[Installation troubleshooting](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-6.4.0/reference/install-faq.html) guide.

## Machine learning frameworks[#](#machine-learning-frameworks)

ROCm supports popular machine learning frameworks and libraries including [PyTorch](https://pytorch.org/blog/pytorch-for-amd-rocm-platform-now-available-as-python-package), [TensorFlow](https://tensorflow.org), [JAX](https://jax.readthedocs.io/en/latest), and [DeepSpeed](https://cloudblogs.microsoft.com/opensource/2022/03/21/supporting-efficient-large-model-training-on-amd-instinct-gpus-with-deepspeed/).

Review the framework installation documentation. For ease-of-use, it’s recommended to use official ROCm prebuilt Docker images with the framework pre-installed.

## Next steps[#](#next-steps)

After installing ROCm and your desired ML libraries – and before running AI workloads – conduct system health benchmarks
to test the optimal performance of your AMD hardware. See [System health benchmarks](system-health-check.html) to get started.
