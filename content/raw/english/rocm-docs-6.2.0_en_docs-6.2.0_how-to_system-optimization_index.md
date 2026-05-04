---
title: "System optimization"
source_url: "https://rocm.docs.amd.com/en/docs-6.2.0/how-to/system-optimization/index.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T16:17:40.820211+00:00
content_hash: "ef1e68f6686f17ea"
---

# System optimization[#](#system-optimization)



This guide outlines system setup and tuning suggestions for AMD hardware to optimize performance for specific types of workloads or use-cases.

## High-performance computing workloads[#](#high-performance-computing-workloads)

High-performance computing (HPC) workloads have unique requirements. The default hardware and BIOS configurations for OEM platforms may not provide optimal performance for HPC workloads. To enable optimal HPC settings on a per-platform and per-workload level, this chapter describes:

BIOS settings that can impact performance

Hardware configuration best practices

Supported versions of operating systems

Workload-specific recommendations for optimal BIOS and operating system settings


There is also a discussion on the AMD Instinct™ software development environment, including information on how to install and run the DGEMM, STREAM, HPCG, and HPL benchmarks. This guide provides a good starting point but is not tested exhaustively across all compilers.

Knowledge prerequisites to better understand this document and to perform tuning for HPC applications include:

Experience in configuring servers

Administrative access to the server’s Management Interface (BMC)

Administrative access to the operating system

Familiarity with the OEM server’s BMC (strongly recommended)

Familiarity with the OS specific tools for configuration, monitoring, and troubleshooting (strongly recommended)


This document provides guidance on tuning systems with various AMD Instinct accelerators for HPC workloads. The following sections don’t comprise an all-inclusive guide, and some items referred to may have similar, but different, names in various OEM systems (for example, OEM-specific BIOS settings). This following sections also provide suggestions on items that should be the initial focus of additional, application-specific tuning.

While this guide is a good starting point, developers are encouraged to perform their own performance testing for additional tuning.

System optimization guide |
Architecture reference |
White papers |
|---|---|---|

## Workstation workloads[#](#workstation-workloads)

Workstation workloads, much like those for HPC, have a unique set of requirements: a blend of both graphics and compute, certification, stability and others.

The document covers specific software requirements and processes needed to use these GPUs for Single Root I/O Virtualization (SR-IOV) and machine learning tasks.

The main purpose of this document is to help users utilize the RDNA™ 2 GPUs to their full potential.
