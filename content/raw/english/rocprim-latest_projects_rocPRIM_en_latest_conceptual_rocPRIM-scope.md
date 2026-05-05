---
title: "rocPRIM operation scope &#8212; rocPRIM 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocPRIM/en/latest/conceptual/rocPRIM-scope.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:17:44.770265+00:00
content_hash: "31efa25e1b53d33a"
---

# rocPRIM operation scope[#](#rocprim-operation-scope)

The scope of a rocPRIM operation determines the parts of the GPU that will cooperate to compute the result.

The scope has a direct influence on how the data will be subdivided and processed by the computing units (CUs) and vector arithmetic logic units (VALUs).

A device operation runs at the grid level. Both the operation and the data are broken down into function calls that are dispatched to the CUs. Synchronization at the grid level is done through wait lists and queue barriers.

Each block is made up of warps which are groups of threads. The function calls in the blocks are distributed over warps. Each warp computes an operation. All the warps on the same VALU run the same operation.

Operations then run sequentially in the threads within the warps.

Synchronization at the block, warp, and thread level is done through memory barriers.
