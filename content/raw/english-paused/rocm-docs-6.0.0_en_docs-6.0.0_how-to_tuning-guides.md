---
title: "Tuning guides"
source_url: "https://rocm.docs.amd.com/en/docs-6.0.0/how-to/tuning-guides.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T16:18:19.379572+00:00
content_hash: "d28e515e13815891"
---

# Tuning guides[#](#tuning-guides)



Use case-specific system setup and tuning guides.

## High-performance computing[#](#high-performance-computing)

High-performance computing (HPC) workloads have unique requirements. The default hardware and BIOS configurations for OEM platforms may not provide optimal performance for HPC workloads. To enable optimal HPC settings on a per-platform and per-workload level, this guide calls out:

BIOS settings that can impact performance

Hardware configuration best practices

Supported versions of operating systems

Workload-specific recommendations for optimal BIOS and operating system settings


There is also a discussion on the AMD Instinct™ software development environment, including information on how to install and run the DGEMM, STREAM, HPCG, and HPL benchmarks. This guidance provides a good starting point but is not exhaustively tested across all compilers.

Prerequisites to understanding this document and to performing tuning of HPC applications include:

Experience in configuring servers

Administrative access to the server’s Management Interface (BMC)

Administrative access to the operating system

Familiarity with the OEM server’s BMC (strongly recommended)

Familiarity with the OS specific tools for configuration, monitoring, and troubleshooting (strongly recommended)


This document provides guidance on tuning systems with various AMD Instinct™ accelerators for HPC workloads. This document is not an all-inclusive guide, and some items referred to may have similar, but different, names in various OEM systems (for example, OEM-specific BIOS settings). This document also provides suggestions on items that should be the initial focus of additional, application-specific tuning.

This document is based on the AMD EPYC™ 7003-series processor family (former codename “Milan”).

While this guide is a good starting point, developers are encouraged to perform their own performance testing for additional tuning.

This chapter goes through how to configure your AMD Instinct™ MI200 accelerated compute nodes to get the best performance out of them.

## Workstation[#](#workstation)

Workstation workloads, much like high-performance computing, have a unique set of requirements, a blend of both graphics and compute, certification, stability and the list continues.

The document covers specific software requirements and processes needed to use these GPUs for Single Root I/O Virtualization (SR-IOV) and machine learning (ML).

The main purpose of this document is to help users utilize the RDNA 2 GPUs to their full potential.
