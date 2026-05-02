---
title: "Using Origami and Stream-K with hipBLASLt &#8212; hipBLASLt 1.2.2 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipBLASLt/en/latest/how-to/how-to-use-streamk.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:06:33.987231+00:00
content_hash: "bb81c2301012d5cf"
---

# Using Origami and Stream-K with hipBLASLt[#](#using-origami-and-stream-k-with-hipblaslt)

hipBLASLt supports the Origami with Stream-K library, which reduces library sizes for a wide range of General Matrix-Matrix Multiplication (GEMM) shapes and sizes.
It also provides more consistent performance, which might be better in some cases.
Stream-K partitions an equal share of the aggregate inner-loop iterations among physical processing elements,
which provides a near-perfect utilization of computing resources.
For more information about Stream-K, see
[Stream-K: Work-centric Parallel Decomposition for Dense Matrix-Matrix Multiplication on the GPU](https://arxiv.org/abs/2301.03598)
on the arXiv website.

## Configuring the kernel selection strategy[#](#configuring-the-kernel-selection-strategy)

The `TENSILE_SOLUTION_SELECTION_METHOD`

environment variable controls the hipBLASLt kernel selection strategy for GEMM operations.
These variables apply to all GEMMs in an application.
Set this variable to `2`

to enable the Origami with Stream-K library or leave it set to `0`

to continue to use the default settings.

Note

On the AMD Instinct™ MI350 series, Origami with Stream-K is the only kernel selection strategy available.
There is no alternative library and the `TENSILE_SOLUTION_SELECTION_METHOD`

variable has no effect.

`TENSILE_SOLUTION_SELECTION_METHOD=0`

(Standard tuned libraries)Kernels are selected from the standard tuned libraries.

The heuristic best kernel is selected from the standard tuning grid.

User-driven tuning (tunable ops) only accesses kernels from the standard grid and free-size libraries.

This option does NOT use any Stream-K kernels.


`TENSILE_SOLUTION_SELECTION_METHOD=2`

(Stream-K)This enables the optional Origami with Stream-K solution selection to use a GEMM scheduling algorithm that results in consistently good peak GEMM performance with far fewer tuned kernels.

The heuristic best kernel is selected from the Origami with Stream-K library.

User-driven tuning (tunable ops) considers all kernels from the standard grid, the free-size library, and the Origami with Stream-K library.



Note

Stream-K supports a different range of data types on different AMD GPUs. For example, the MI300A APU supports
a wider variety of data types, including `FP32`

, `FP16`

, `BF16`

, `FP8`

, and `BF8`

.
`TENSILE_SOLUTION_SELECTION_METHOD=2`

is used to enable Stream-K on all MI300 platforms.

## Configuring the kernel launch behavior[#](#configuring-the-kernel-launch-behavior)

You can control The Stream-K kernel launch behavior using the environment variables listed in the following table. These variables apply to all GEMMs in an application. By default, Stream-K uses a model to predict the optimal grid size to use when launching a GEMM kernel at runtime. However, you can choose how many workgroups to launch a GEMM kernel with using the Stream-K settings below:

Environment Variable |
Description |
|---|---|
|
Set this variable to |
|
This variable overrides the default grid size and launches Stream-K GEMM kernels using the specified number of workgroups. |
|
This variable sets the maximum number of compute units to use for Stream-K kernels. By default, Stream-K kernels are allowed to use all compute units on the device, but this setting lets you limit the number of units that can be used. |

## Recommendations for using Stream-K[#](#recommendations-for-using-stream-k)

Stream-K is especially advantageous in certain situations. Follow these guidelines when choosing a kernel selection strategy, based on your application and the desired performance.

**Wide range of GEMM sizes**: Stream-K is a better choice for applications that handle a variety of GEMM shapes and sizes.**Non-uniform dimensions**: Stream-K is particularly beneficial for GEMMs where one dimension is significantly larger than the others.**Consistent performance**: Stream-K provides more consistent peak performance than the default selection method by evenly distributing work across the available compute units.

### Managing Stream-K resource use[#](#managing-stream-k-resource-use)

Follow these guidelines to optimize how Stream-K uses resources:

**Promoting concurrency**: Use`TENSILE_STREAMK_FIXED_GRID`

to limit the number of workgroups. This prevents GEMM from monopolizing the GPU resources and allows other kernels to run concurrently.The following example limits the GEMM kernels to 64 workgroups:

export TENSILE_STREAMK_FIXED_GRID=64

**Limiting compute units**: Use`TENSILE_STREAMK_MAX_CUS`

to restrict the number of compute units the Stream-K kernels can use.This example limits the GEMM kernels to 32 compute units:

export TENSILE_STREAMK_MAX_CUS=32
