---
title: "What is RCCL? &#8212; RCCL 2.27.7 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rccl/en/latest/what-is-rccl.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:22:53.061343+00:00
content_hash: "19d18a59edf47a2a"
---

# What is RCCL?[#](#what-is-rccl)

The ROCm Communication Collectives Library (RCCL) includes multi-GPU and
multi-node collective communication primitives optimized for AMD GPUs.
It implements routines such as `all-reduce`

, `all-gather`

, `reduce`

,
`broadcast`

, `reduce-scatter`

, `gather`

, `scatter`

, `all-to-allv`

,
and `all-to-all`

, as well as direct point-to-point (GPU-to-GPU) send
and receive operations. It is optimized to achieve high bandwidth
on platforms using PCIe and xGMI and networking using InfiniBand Verbs or TCP/IP
sockets. RCCL supports an arbitrary number of GPUs installed in a single node
or multiple nodes and can be used in either
single- or multi-process (for example, MPI) applications.

The collective operations are implemented using ring and tree algorithms and have been optimized for throughput and latency by leveraging topology awareness, high-speed interconnects, and RDMA-based collectives. For best performance, small operations can be either batched into larger operations or aggregated through the API.

RCCL uses PCIe and xGMI high-speed interconnects for intra-node communication as well as InfiniBand, RoCE, and TCP/IP for inter-node communication. It supports an arbitrary number of GPUs installed in a single-node or multi-node platform and can easily integrate into single- or multi-process (for example, MPI) applications.
