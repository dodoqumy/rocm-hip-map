---
title: "RCCL 2.27.7 for ROCm 7.2.0"
source_url: https://github.com/ROCm/rccl/releases/tag/rocm-7.2.0
source_type: github-release
source_org: ROCm
published_date: 2026-01-21
credibility: 4
lifecycle: latest
tags: [github-release, rocm-7.2.0]
---

# RCCL 2.27.7 for ROCm 7.2.0

> 📦 **Release:** [rocm-7.2.0](https://github.com/ROCm/rccl/releases/tag/rocm-7.2.0)
> **发布:** 2026-01-21


### Changed

* RCCL error messages have been made more verbose in several cases. RCCL now prints out fatal error messages by default. Fatal error messages can be suppressed by setting `NCCL_DEBUG=NONE`.
* Disabled `reduceCopyPacks` pipelining for `gfx950`.

