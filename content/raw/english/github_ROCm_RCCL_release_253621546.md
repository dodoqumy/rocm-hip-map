---
title: "RCCL 2.26.6 for ROCm 7.0.2"
source_url: https://github.com/ROCm/rccl/releases/tag/rocm-7.0.2
source_type: github-release
source_org: ROCm
published_date: 2025-10-10
credibility: 4
lifecycle: latest
tags: [github-release, rocm-7.0.2]
---

# RCCL 2.26.6 for ROCm 7.0.2

> 📦 **Release:** [rocm-7.0.2](https://github.com/ROCm/rccl/releases/tag/rocm-7.0.2)
> **发布:** 2025-10-10


### Added

* Enabled double-buffering in `reduceCopyPacks` to trigger pipelining, especially to overlap bf16 arithmetic.
* Added `--force-reduce-pipeline` as an option that can be passed to the `install.sh` script. Passing this option will enable software-triggered pipelining `bfloat16` reductions (i.e. `all_reduce`, `reduce_scatter` and `reduce`).

