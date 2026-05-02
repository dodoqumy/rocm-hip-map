---
title: "Graph-safe support for ROCm libraries"
source_url: "https://rocm.docs.amd.com/en/docs-7.0.0/reference/graph-safe-support.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T12:05:16.465883+00:00
content_hash: "3db47c73b42794d5"
---

# Graph-safe support for ROCm libraries[#](#graph-safe-support-for-rocm-libraries)

2025-12-19

3 min read time

HIP graph-safe libraries operate safely in HIP execution graphs.
[HIP graphs](https://rocm.docs.amd.com/projects/HIP/en/docs-7.0.0/how-to/hip_runtime_api/hipgraph.html#how-to-hip-graph) are an alternative way of executing tasks on a GPU
that can provide performance benefits over launching kernels using the standard
method via streams.

Functions and routines from graph-safe libraries shouldn’t result in issues like race conditions, deadlocks, or unintended dependencies.

The following table shows whether a ROCm library is graph-safe.

ROCm library |
Graph safe support |
|---|---|
❌ |
|
✅ |
|
⚠️ |
|
✅ |
|
✅ (see |
|
✅ |
|
⚠️ (experimental) |
|
✅ |
|
⚠️ (experimental) |
|
❌ |
|
❌ |
|
✅ |
|
❌ |
|
❌ |
|
✅ (see |
|
❌ |
|
✅ (see |
|
❌ |
|
❌ |
|
✅ |
|
✅ |
|
⚠️ (experimental) |
|
⚠️ (experimental) |
|
❌ (see details) |
|
❌ |
|
⚠️ |
|
✅ |

✅: full support

⚠️: partial support

❌: not supported
