---
title: "RCCL 2.22.3 for ROCm 6.4.0"
source_url: https://github.com/ROCm/rccl/releases/tag/rocm-6.4.0
source_type: github-release
source_org: ROCm
published_date: 2025-04-11
credibility: 4
lifecycle: latest
tags: [github-release, rocm-6.4.0]
---

# RCCL 2.22.3 for ROCm 6.4.0

> 📦 **Release:** [rocm-6.4.0](https://github.com/ROCm/rccl/releases/tag/rocm-6.4.0)
> **发布:** 2025-04-11


### Added

* `RCCL_SOCKET_REUSEADDR` and `RCCL_SOCKET_LINGER` environment parameters
* Setting `NCCL_DEBUG=TRACE NCCL_DEBUG_SUBSYS=VERBS` will generate traces for fifo and data ibv_post_sends
* Added `--log-trace` flag to enable traces through the install.sh script (e.g. `./install.sh --log-trace`)

### Changed

* Compatibility with NCCL 2.22.3
* Added support for the rail-optimized tree algorithm for the MI300 series. This feature requires the use of all eight GPUs within
  each node. It limits NIC traffic to use only GPUs of the same index across nodes and should not impact performance
  on non-rail-optimized network topologies. The original method of building trees can be enabled by setting the
  environment variable `RCCL_DISABLE_RAIL_TREES=1`.
* Additional debug information about how the trees are built can be logged to the GRAPH logging subsys by setting
  `RCCL_OUTPUT_TREES=1`.

