---
title: "Composable Kernel structure &#8212; Composable Kernel 1.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/composable_kernel/en/latest/conceptual/Composable-Kernel-structure.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:17:00.001713+00:00
content_hash: "9da8e9383e6a293e"
---

# Composable Kernel structure[#](#composable-kernel-structure)

The Composable Kernel library uses a tile-based programming model and tensor coordinate transformation to achieve performance portability and code maintainability. Tensor coordinate transformation is a complexity reduction technique for complex machine learning operators.

The Composable Kernel library consists of four layers:

a templated tile operator layer

a templated kernel and invoker layer

an instantiated kernel and invoker layer

a client API layer.


A wrapper component is included to simplify tensor transform operations.
