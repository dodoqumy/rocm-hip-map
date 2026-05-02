---
title: "Installing ROCm and deep learning frameworks"
source_url: "https://rocm.docs.amd.com/en/docs-7.2.0/how-to/rocm-for-ai/install.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T12:04:35.132387+00:00
content_hash: "0f80c3ea34a50a35"
---

# Installing ROCm and deep learning frameworks[#](#installing-rocm-and-deep-learning-frameworks)

2025-12-12

3 min read time

Before getting started, install ROCm and supported deep learning frameworks.

If you’re new to ROCm, refer to the [ROCm quick start install guide for Linux](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.0/install/quick-start.html).

If you’re using a Radeon GPU for graphics-accelerated applications, refer to the
[Radeon installation instructions](https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/native_linux/howto_native_linux.html).

You can install ROCm on [compatible systems](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.0/reference/system-requirements.html) via your Linux
distribution’s package manager. See the following documentation resources to get started:

Follow the [post-installation instructions](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.0/install/post-install.html) to
configure your system linker, PATH, and verify the installation.

If you encounter any issues during installation, refer to the
[Installation troubleshooting](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.0/reference/install-faq.html) guide.

## Deep learning frameworks[#](#deep-learning-frameworks)

ROCm supports deep learning frameworks and libraries including [PyTorch](https://pytorch.org), [TensorFlow](https://tensorflow.org), [JAX](https://jax.readthedocs.io/en/latest), and more.

Review the [framework installation documentation](../deep-learning-rocm.html). For ease-of-use, it’s recommended to use official ROCm prebuilt Docker
images with the framework pre-installed.

## Next steps[#](#next-steps)

After installing ROCm and your desired ML libraries – and before running AI workloads – conduct system health benchmarks
to test the optimal performance of your AMD hardware. See [System setup for AI workloads on ROCm](system-setup/index.html) to get started.
