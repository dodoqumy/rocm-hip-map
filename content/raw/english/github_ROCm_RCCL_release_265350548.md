---
title: "RCCL 2.27.7 for ROCm 7.1.1"
source_url: https://github.com/ROCm/rccl/releases/tag/rocm-7.1.1
source_type: github-release
source_org: ROCm
published_date: 2025-11-26
credibility: 4
lifecycle: latest
tags: [github-release, rocm-7.1.1]
---

# RCCL 2.27.7 for ROCm 7.1.1

> 📦 **Release:** [rocm-7.1.1](https://github.com/ROCm/rccl/releases/tag/rocm-7.1.1)
> **发布:** 2025-11-26


### Resolved Issues

* Fixed a single node data corruption issue in MSCCL on the Instinct MI350X and MI355X for the LL protocol. This previously affected about 2% of the runs for single node AllReduce with inputs smaller than 512 KiB.

