---
title: "ROCTx API &#8212; ROCprofiler-SDK 1.1.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/api-reference/rocprofiler-sdk-roctx_api_reference.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:15:05.661508+00:00
content_hash: "d36c3d405a63ecac"
---

# ROCTx API[#](#roctx-api)

## Introduction[#](#introduction)

ROCTx is a comprehensive library that implements the AMD code annotation API. It provides essential functionality for:

Event annotation and marking

Code range tracking and management

Profiler control and customization

Thread and device naming capabilities


Key features:

Nested range tracking with push/pop functionality

Process-wide range management

Thread-specific and global profiler control

Device and stream naming support

HSA agent and HIP device management


The API is divided into several main components:

**Markers**- For single event annotations**Ranges**- For tracking code execution spans**Profiler Control**- For managing profiling tool behavior**Naming Utilities**- For labeling threads, devices, and streams

Thread Safety:

Range operations are thread-local and thread-safe

Marking operations are thread-safe

Profiler control operations are process-wide


Integration:

Compatible with HIP runtime

Supports HSA (Heterogeneous System Architecture)

Provides both C and C++ interfaces


Performance Considerations:

Minimal overhead for marking and range operations

Thread-local storage for efficient range stacking

Lightweight profiler control mechanisms


Note

All string parameters must be null-terminated.

Warning

Proper nesting of range push/pop operations is the user’s responsibility.

This ROCTx API topic broadly covers:
