---
title: "Understanding GPU performance &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T06:58:49.636488+00:00
content_hash: "f2ad3e77ca43913e"
---

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
{#main-content .bd-main role="main"}

sbt-scroll-pixel-helper

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
bd-content
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
bd-article-container
:::::::
{.bd-header-article .d-print-none}
::::::
{.header-article-items .header-article__inner}
::
header-article-items__start

header-article-item
[]{.fa-solid .fa-angle-right}

header-article-item

::

::
header-article-items__end
:
header-article-item

article-header-buttons
[]{.fa-solid .fa-list}

:
::
::::::
:::::::

{#jb-print-docs-body .onlyprint}
# Understanding GPU performance

::
{#print-main-content}
:
{#jb-print-toc}

{}
## Contents

:
::

{#searchbox}

:::::::::::::::::::::::::::::::::::::::::::::
{#understanding-gpu-performance .section}
[]{#performance-optimization}

# Understanding GPU performance[\#](#understanding-gpu-performance "Link to this heading"){.headerlink}

This topic explains the theoretical foundations of GPU performance on AMD hardware. Understanding these concepts helps you analyze performance characteristics, identify bottlenecks, and make informed optimization decisions.

For practical optimization techniques and step-by-step guidance, see [[Performance guidelines]{.doc}](../how-to/performance_guidelines.html){.reference .internal}.

{#performance-bottlenecks .section}
[]{#id1}

## Performance bottlenecks[\#](#performance-bottlenecks "Link to this heading"){.headerlink}

The neck of a bottle limits the rate at which liquid can be poured. A performance bottleneck in a computing system similarly limits the rate at which work can be completed.

A performance bottleneck is the limiting factor that prevents a GPU kernel from achieving higher performance. Understanding which bottleneck applies helps identify the appropriate optimization approach.

Performance bottlenecks for GPU kernels fall into three main categories:

- **Compute-bound**: The kernel is limited by arithmetic throughput (the arithmetic bandwidth of compute units)

- **Memory-bound**: The kernel is limited by memory bandwidth (how quickly data can move between High Bandwidth Memory (HBM) and on-chip caches or Local Data Share (LDS))

- **Overhead-bound**: The kernel is limited by latency (host-side scheduling, kernel launch overhead, or small array operations)

This categorization aligns with the textbook approach to optimization: determine the bottleneck, elevate the bottleneck until it is no longer limiting, and repeat on the new bottleneck.

[[Roofline model analysis]{.std .std-ref}](#roofline-model){.reference .internal} helps quickly identify whether a kernel's performance is bottlenecked by compute throughput or memory bandwidth.

{#roofline-model .section}
[]{#id2}

## Roofline model[\#](#roofline-model "Link to this heading"){.headerlink}

The roofline model is a simplified, visual model of performance used to quickly determine whether a program is limited by memory bandwidth or arithmetic bandwidth.

In the roofline model, two hardware-derived "roofs" place upper bounds---or ceilings---on achievable performance:

- **Compute roof**: The peak arithmetic rate of the target hardware (vector Arithmetic Logic Units (ALUs) or [[Matrix Fused Multiply-Add (MFMA) units]{.std .std-ref}](hardware_implementation.html#mfma-units){.reference .internal}), sometimes referred to as its arithmetic bandwidth

- **Memory roof**: The peak data transfer rate of the memory subsystem, or memory bandwidth

These are plotted on a plane with arithmetic intensity (operations per byte) on the x-axis and performance (operations per second) on the y-axis.

The compute roof is a horizontal line at a height equal to the hardware's maximum arithmetic throughput. The memory roof is a slanted line whose slope equals the memory bandwidth (in bytes per second). Because slope is "rise over run," its units correspond to throughput per intensity.

<figure id="id11" class="align-center">
<a href="../_images/roofline.svg" class="reference internal image-reference"><img src="../_images/roofline.svg" style="width: 100%;" alt="Roofline model diagram showing memory bandwidth ceiling and compute ceiling" /></a>
<figcaption><p><span class="caption-text">Roofline model showing the relationship between arithmetic intensity and achievable performance. The memory bandwidth ceiling represents the GPU’s memory bandwidth limit, while the compute ceiling shows the maximum achievable TFLOPs. Kernels falling into the area to the left of the ridge point are memory-bound, while they are compute-bound if they fall into the right area.</span><a href="#id11" class="headerlink" title="Link to this image">#</a></p></figcaption>
</figure>

A kernel's position on the x-axis indicates whether it is fundamentally compute-bound (beneath the flat roof) or memory-bound (beneath the slanted roof). In practice, few kernels ever fully reach either roof due to overhead, latency, and control-divergence effects.

The point where the diagonal and horizontal roofs intersect is called the ridge point. Its x-coordinate gives the minimum arithmetic intensity required to escape the memory bottleneck. Systems with ridge points farther to the left are easier to saturate, but over time, improvements in compute throughput have far outpaced memory growth---pushing ridge points steadily to the right.

On AMD platforms, roofline analysis is built into ROCm's profiling and performance visualization ecosystem. [[rocprofv3]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/how-to/using-rocprofv3.html "(in Rocprofiler SDK v1.1.0)"){.reference .external} can be used to gather achieved FLOPs, memory transactions, and operational intensity.

The roofline model's elegance lies in its simplicity---but also in its deliberate omissions. It ignores latency entirely, focusing only on sustained throughput limits. Understanding those assumptions---and when they hold---is essential to applying the model correctly.

{#compute-bound-performance .section}
[]{#compute-bound}

## Compute-bound performance[\#](#compute-bound-performance "Link to this heading"){.headerlink}

A kernel is compute-bound when its performance is limited by the GPU's arithmetic throughput rather than memory bandwidth. These kernels have high [[arithmetic intensity]{.std .std-ref}](#arithmetic-intensity){.reference .internal}, spending most cycles executing arithmetic operations.

Kernels that are compute-bound are limited by the arithmetic bandwidth of the GPU's [[Compute Units (CUs)]{.std .std-ref}](hardware_implementation.html#compute-unit){.reference .internal}---on AMD architectures, this means the [[vector ALUs]{.std .std-ref}](hardware_implementation.html#valu){.reference .internal} and [[MFMA units]{.std .std-ref}](hardware_implementation.html#mfma-units){.reference .internal} within each [[CU]{.std .std-ref}](hardware_implementation.html#compute-unit){.reference .internal} or Single Instruction Multiple Data (SIMD) unit.

Characteristics of compute-bound kernels:

- High ratio of arithmetic operations to memory accesses (high arithmetic intensity)

- Performance scales with GPU compute capacity

- Limited benefit from memory bandwidth optimization

- Can often achieve a high percentage of peak theoretical FLOPS

- The limiting factor is utilization of arithmetic pipelines: the number of concurrent floating-point or integer operations the GPU can sustain per clock

The theoretical maximum is determined by:

- Number of compute units and SIMD lanes

- Clock frequency

- Instruction throughput per cycle

- Specialized unit capabilities ([[matrix cores]{.std .std-ref}](hardware_implementation.html#mfma-units){.reference .internal}, Special Function Units (SFUs))

{#memory-bound-performance .section}
[]{#memory-bound}

## Memory-bound performance[\#](#memory-bound-performance "Link to this heading"){.headerlink}

A kernel is memory-bound when its performance is limited by memory bandwidth rather than compute capacity. These kernels have low [[arithmetic intensity]{.std .std-ref}](#arithmetic-intensity){.reference .internal} and spend significant time waiting for memory operations.

Kernels that are memory-bound are limited by the memory bandwidth of the GPU---that is, by how quickly data can move between [[HBM]{.std .std-ref}](hardware_implementation.html#hbm){.reference .internal} and the on-chip caches or [[LDS]{.std .std-ref}](hardware_implementation.html#lds){.reference .internal} of the GPU's [[compute units]{.std .std-ref}](hardware_implementation.html#compute-unit){.reference .internal}.

Memory-bound kernels are limited by the bandwidth between GPU RAM and local caches because the working sets of most real-world GPU workloads are far larger than any higher level of the memory hierarchy. When data reuse is low and arithmetic operations per byte are few, the speed of computation is dominated by how quickly memory can feed operands to the arithmetic units.

Characteristics of memory-bound kernels:

- Low ratio of arithmetic operations to memory accesses (low arithmetic intensity)

- Performance scales with memory bandwidth

- Sensitive to memory access patterns

- Typically achieve lower percentage of peak FLOPS

- Fall to the left of the ridge point on the roofline diagram

The theoretical maximum is determined by:

- HBM bandwidth capacity

- Memory controller efficiency

- Cache hierarchy effectiveness

- Memory access pattern efficiency

::
{#arithmetic-intensity .section}
[]{#id3}

## Arithmetic intensity[\#](#arithmetic-intensity "Link to this heading"){.headerlink}

Arithmetic intensity is the ratio of arithmetic operations to memory operations in a kernel. It is the ratio of floating-point operations (FLOPs) to memory traffic (bytes) for a given kernel or algorithm.

{.math .notranslate .nohighlight}
\\\[\\text{Arithmetic Intensity} = \\frac{\\text{FLOPs}}{\\text{Bytes Transferred}}\\\]

This metric determines whether a kernel is compute-bound or memory-bound.

Key points:

- Higher arithmetic intensity indicates more computation per byte transferred

- A high arithmetic intensity indicates that a kernel performs many arithmetic operations per byte loaded

- The balance point (ridge point) depends on the GPU's compute-to-bandwidth ratio

- It can be calculated theoretically or measured empirically

- Different precision types affect both FLOPs and bytes

For modern AMD GPUs:

- The compute-to-bandwidth ratio varies by GPU generation

- Higher-end models have higher ratios

- Kernels above the GPU's specific ratio (ridge point) are compute-bound

- Because modern GPUs deliver far more arithmetic throughput than memory bandwidth, the most efficient kernels are those with high arithmetic intensity

{#algorithmic-complexity-and-intensity-scaling .section}
### Algorithmic complexity and intensity scaling[\#](#algorithmic-complexity-and-intensity-scaling "Link to this heading"){.headerlink}

Because algorithms have different operational and memory complexities, they scale differently in arithmetic intensity:

- An algorithm with [\\(\\mathcal{O}(1)\\)]{.math .notranslate .nohighlight} operations and [\\(\\mathcal{O}(N)\\)]{.math .notranslate .nohighlight} memory has [\\(\\mathcal{O}(\\frac{1}{N})\\)]{.math .notranslate .nohighlight} intensity (decreasing with size)

- One with [\\(\\mathcal{O}(N)\\)]{.math .notranslate .nohighlight} operations and [\\(\\mathcal{O}(1)\\)]{.math .notranslate .nohighlight} memory has [\\(\\mathcal{O}(N)\\)]{.math .notranslate .nohighlight} intensity (increasing with size)

Examples of kernel complexity scaling:

- **SAXPY** ([\\(y = ax + y\\)]{.math .notranslate .nohighlight}): [\\(2N \\text{ FLOPs}\\)]{.math .notranslate .nohighlight}, [\\(8N \\text{ bytes}\\)]{.math .notranslate .nohighlight} → intensity [\\(\\frac{1}{4}\\)]{.math .notranslate .nohighlight} → [\\(\\mathcal{O}(1)\\)]{.math .notranslate .nohighlight} scaling

- **Single-Precision Real Fast Fourier Transform (FFT)**: [\\(\\frac{5}{2} N \\log N \\text{ FLOPs}\\)]{.math .notranslate .nohighlight}, [\\(16N \\text{ bytes}\\)]{.math .notranslate .nohighlight} → intensity [\\(\\frac{5}{32} \\log N\\)]{.math .notranslate .nohighlight} → [\\(\\mathcal{O}(\\log N)\\)]{.math .notranslate .nohighlight} scaling

- **SGEMM** (matrix multiplication): [\\(2N\^3 \\text{ FLOPs}\\)]{.math .notranslate .nohighlight}, [\\(6N\^2 \\text{ bytes}\\)]{.math .notranslate .nohighlight} → [\\(\\mathcal{O}(N)\\)]{.math .notranslate .nohighlight} scaling

Matrix multiplication scales linearly in arithmetic intensity--- [\\(\\mathcal{O}(N\^3)\\)]{.math .notranslate .nohighlight} operations versus [\\(\\mathcal{O}(N\^2)\\)]{.math .notranslate .nohighlight} memory---making it an ideal match for high-throughput architectures. This favorable scaling is a key reason why many machine-learning algorithms built around dense linear algebra achieve high GPU utilization.

Techniques that shift memory transfers to additional compute operations reduce memory traffic but increase arithmetic load, thereby raising the arithmetic intensity. For example:

- Compressing data in [[global memory]{.std .std-ref}](hardware_implementation.html#hbm){.reference .internal} reduces bytes transferred but adds decompression arithmetic---raising arithmetic intensity

- In training and inference of neural networks, techniques like gradient checkpointing reduce memory storage of activations (fewer bytes stored and loaded) but add recompute work---again increasing arithmetic intensity

::

::::
{#latency-hiding-mechanisms .section}
[]{#latency-hiding}

## Latency hiding mechanisms[\#](#latency-hiding-mechanisms "Link to this heading"){.headerlink}

GPUs hide memory and instruction latency through massive hardware multithreading rather than complex CPU techniques like out-of-order execution.

Latency hiding is the strategy of masking long-latency operations by running them concurrently. On AMD GPUs, performant kernels interleave the execution of many threads across [[warps]{.std .std-ref}](programming_model.html#wavefront){.reference .internal} keeping overall throughput high even when individual instructions take many cycles. When one warp stalls on a slow [[global-memory]{.std .std-ref}](hardware_implementation.html#hbm){.reference .internal} access, the [[scheduler]{.std .std-ref}](hardware_implementation.html#wave-scheduling){.reference .internal} immediately issues instructions from another eligible warp.

How latency hiding works:

- **warp switching**: Context switches occur every cycle with zero overhead

- **Multiple warps per CU**: Many concurrent warps supported

- **Instruction-level parallelism**: Multiple independent instructions in flight

This keeps the [[compute units]{.std .std-ref}](hardware_implementation.html#compute-unit){.reference .internal} busy: while one warp drives [[MFMA matrix ops]{.std .std-ref}](hardware_implementation.html#mfma-units){.reference .internal}, another runs scalar and vector ALU work (e.g., quantize and dequantize), and a third issues loads and stores through the memory pipeline ([[LDS]{.std .std-ref}](hardware_implementation.html#lds){.reference .internal}, L1, and L2 ↔ [[HBM]{.std .std-ref}](hardware_implementation.html#hbm){.reference .internal}).

The hardware can completely hide memory latency if there are enough active warps with independent work. The number of instructions required from other warps to hide latency depends on the GPU's specific memory latency and instruction throughput characteristics.

{#little-s-law .section}
[]{#littles-law}

### Little's Law[\#](#little-s-law "Link to this heading"){.headerlink}

Little's Law relates concurrency (how much work is in flight) to latency and throughput:

{.math .notranslate .nohighlight}
\\\[\\text{concurrency (ops)} = \\text{latency (s)} \\times \\text{throughput (ops/s)}\\\]

In GPU terms, it tells you how much independent work you must have in flight to hide latency via fine-grained scheduling. On AMD GPUs, [[warp]{.std .std-ref}](programming_model.html#wavefront){.reference .internal} switching by the warp schedulers is the primary latency-hiding mechanism.

Little's Law determines how many independent memory transactions or instructions must be outstanding across active warps to keep the compute units busy.

Concretely, consider a simple sequence in AMD CDNA terms:

:
{.highlight-amdgpu .notranslate}

highlight
    global_load_dword    v1, v[2:3], off   ; long-latency global load (hundreds of cycles)
    v_mul_lo_u32         v2, v1, 0xBEEF    ; integer multiply
    v_add_u32            v4, v2, 0xAFFE    ; integer add
    v_mul_lo_u32         v6, v4, 0x1337    ; integer multiply

:

Executed strictly serially, the total time is dominated by the global load. Using Little's Law, if your effective issue rate is \~1 inst/cycle and the load takes hundreds of cycles, you need hundreds of independent in-flight operations to finish, on average, one such sequence per cycle---hiding the memory latency from consumers.

Issuance occurs at the warp granularity (64 threads per warp on CDNA). When latency hiding is successful, the CU maintains enough active warps and rapidly context-switches among them whenever one blocks, so execution units don't sit idle waiting on memory or other long-latency events.

Requirements for effective latency hiding:

- Sufficient occupancy (active warps)

- Independent instructions to overlap

- Balanced resource usage

- Minimal divergence

::::

{#warp-wavefront-execution-states .section}
[]{#wavefront-execution}

## Warp (Wavefront) execution states[\#](#warp-wavefront-execution-states "Link to this heading"){.headerlink}

The state of the [[warps]{.std .std-ref}](programming_model.html#wavefront){.reference .internal} executing a kernel on an AMD GPU can be described using several non-exclusive terms---active, stalled, eligible, and selected.

A warp is considered **active** from the time its threads begin executing until all threads in that warp have completed the kernel. The [[warp schedulers]{.std .std-ref}](hardware_implementation.html#wave-scheduling){.reference .internal} select warps from the active pool each cycle; the selected warps then issue their instructions.

An **eligible** warp is an active warp ready to issue its next instruction. For a warp to be eligible:

- Its next instruction has been fetched

- The required pipeline (vector ALU, [[MFMA]{.std .std-ref}](hardware_implementation.html#mfma-units){.reference .internal}, or memory) is available

- All data dependencies have been resolved

- No synchronization barriers (for example, [`s_barrier`{.docutils .literal .notranslate}]{.pre}) are pending

Eligible warps are the immediate candidates for issue. A lack of eligible warps often indicates dependency or memory stalls---a key target in performance tuning.

A **stalled** warp is active but unable to issue its next instruction due to resource or data hazards. Common causes include:

- Execution dependencies: waiting for results from previous ALU or [[MFMA]{.std .std-ref}](hardware_implementation.html#mfma-units){.reference .internal} operations

- Memory dependencies: waiting for global or [[LDS]{.std .std-ref}](hardware_implementation.html#lds){.reference .internal} memory fetches

- Pipeline conflicts: required execution units are occupied

AMD hardware uses a scoreboard mechanism to track outstanding dependencies per warp. When waiting on [[LDS]{.std .std-ref}](hardware_implementation.html#lds){.reference .internal} or ALU results, a warp is said to be on the short scoreboard; when waiting on off-chip [[HBM]{.std .std-ref}](hardware_implementation.html#hbm){.reference .internal} accesses, it is on the long scoreboard. This scoreboarding approach---originally from the CDC 6600 supercomputer---allows dynamic scheduling across warps (thread-level parallelism) rather than within them (instruction-level parallelism).

A **selected** warp is an eligible one chosen by the warp scheduler to issue an instruction in the current cycle. Each [[CU]{.std .std-ref}](hardware_implementation.html#compute-unit){.reference .internal} typically has multiple schedulers that can each issue one instruction per cycle from their eligible pool.

Understanding these states helps explain GPU utilization metrics:

- **Active cycles**: Percentage of cycles with at least one instruction executing

- **Stall cycles**: Percentage of cycles waiting for resources

- **Idle cycles**: No warps available to execute

Maximizing active cycles while minimizing stall and idle cycles improves performance. Effective latency hiding on AMD hardware relies on keeping enough active and eligible warps resident so that the schedulers always have work to select, ensuring the CU pipelines remain fully utilized.

:
{#occupancy-theory .section}
[]{#occupancy}

## Occupancy theory[\#](#occupancy-theory "Link to this heading"){.headerlink}

Occupancy measures the ratio of active [[warp]{.std .std-ref}](programming_model.html#wavefront){.reference .internal} to the maximum possible warps on a [[compute unit]{.std .std-ref}](hardware_implementation.html#compute-unit){.reference .internal}.

{.math .notranslate .nohighlight}
\\\[\\text{Occupancy} = \\frac{\\text{Active warps}}{\\text{Max warps per CU}}\\\]

There are two common ways to measure it:

- **Theoretical occupancy**: The upper limit determined by the kernel's launch configuration (threads per block, register use, LDS use) and the hardware limits of the CU

- **Achieved occupancy**: The actual number of warps active during kernel execution, i.e., on active cycles

As part of the AMD execution model, all threads in a [[block]{.std .std-ref}](programming_model.html#inherent-thread-hierarchy-block){.reference .internal} are scheduled to the same CU. Each CU has finite resources---Vector General-Purpose Registers (VGPRs), Scalar General-Purpose Registers (SGPRs), [[LDS]{.std .std-ref}](hardware_implementation.html#lds){.reference .internal} (shared memory), and wave slots---that must be shared among all resident blocks. These constraints jointly determine the maximum number of active warps.

Why occupancy matters:

- Higher occupancy improves [[latency hiding]{.std .std-ref}](#latency-hiding){.reference .internal}

- More concurrent warps mask memory and instruction latency

- Enables better utilization of execution units

Limiting factors:

- **Register usage**: VGPRs and SGPRs per thread

- **Shared memory (LDS)**: Allocation per block

- **Warp slots**: Hardware limit on concurrent warps

- **Block size**: Small blocks may waste resources

Trade-offs:

- Higher occupancy improves latency hiding but reduces resources per thread

- Lower occupancy allows more resources per thread but may expose latency

- Optimal occupancy depends on kernel characteristics

- Memory-bound kernels benefit more from high occupancy

Low occupancy often reduces performance when there aren't enough eligible warps to hide memory or arithmetic latency, causing low issue efficiency and underutilized pipelines. However, once occupancy is sufficient for latency hiding, increasing it further can hurt performance by reducing the number of available registers or LDS per warp---both of which can limit [[arithmetic intensity]{.std .std-ref}](#arithmetic-intensity){.reference .internal}.

In short, occupancy measures how fully a [[CU]{.std .std-ref}](hardware_implementation.html#compute-unit){.reference .internal} is loaded, not how efficiently it is utilized. High-performance kernels (for example, [[MFMA]{.std .std-ref}](hardware_implementation.html#mfma-units){.reference .internal}-based GEMMs on [[CDNA]{.std .std-ref}](hardware_implementation.html#cdna-architecture){.reference .internal}) often operate at low occupancy because only a few warps are needed to fully saturate the MFMA and memory pipelines.
:

::::::::::::::
{#memory-hierarchy-impact-on-performance .section}
[]{#memory-hierarchy-theory}

## Memory hierarchy impact on performance[\#](#memory-hierarchy-impact-on-performance "Link to this heading"){.headerlink}

The GPU memory hierarchy has different bandwidths and latencies:

Memory types by speed:

1.  **Registers**: Fastest, lowest latency (per-thread storage)

2.  **LDS (shared memory)**: Very fast, on-chip (per-block storage)

3.  **L1 cache**: Fast, on-chip (per-CU cache)

4.  **L2 cache**: Moderate, on-chip (shared across CUs)

5.  **HBM (global memory)**: Slower, off-chip but high bandwidth

{#memory-coalescing-theory .section}
[]{#id4}

### Memory coalescing theory[\#](#memory-coalescing-theory "Link to this heading"){.headerlink}

Memory coalescing is a hardware technique that improves effective memory bandwidth by servicing many logical loads or stores with a small number of physical memory transactions.

Memory coalescing combines memory accesses from multiple threads into fewer transactions. When consecutive threads access consecutive memory addresses, the hardware can merge requests into efficient cache line accesses.

Memory coalescing is relevant when accessing [[global memory]{.std .std-ref}](hardware_implementation.html#hbm){.reference .internal} ([[HBM]{.std .std-ref}](hardware_implementation.html#hbm){.reference .internal} and GDDR attached to the GPU). For efficient access to LDS and shared memory, see the discussion of bank conflicts below.

On AMD GPUs, global memory is backed by HBM (in data-center parts) or GDDR (on many client parts). These Dynamic Random-Access Memory (DRAM) technologies provide very high bandwidth but have relatively long access latency. If each thread's load or store were always turned into its own physical DRAM transaction, the GPU would leave a large fraction of that raw bandwidth unused.

Coalescing takes advantage of how DRAM is organized internally. When a DRAM address is accessed, the hardware actually fetches or writes a burst: a run of consecutive addresses fetched together in a single transaction. If multiple threads in a [[warp]{.std .std-ref}](programming_model.html#wavefront){.reference .internal} access addresses that fall into the same burst, those logical accesses can be coalesced into that single transaction.

This fits naturally with the warp execution model: in normal execution, all threads in a warp execute the same instruction at the same time. If each lane in the warp loads or stores a value from a contiguous region (e.g., lane *i* accesses [`base`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`+`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`i`{.docutils .literal .notranslate}]{.pre}), the memory system can typically serve the entire warp's request with a small number of large, aligned bursts. When addresses are scattered (e.g., large strides or irregular indexing), more bursts are needed, and effective bandwidth drops.

Why coalescing matters:

- Reduces number of memory transactions

- Improves memory bandwidth utilization

- Decreases memory access latency

**Coalesced pattern**: Consecutive threads accessing consecutive addresses achieve high bandwidth utilization.

**Non-coalesced pattern**: Random or strided addresses result in many separate transactions and low bandwidth utilization.

::
{#example-strided-access-pattern .section}
#### Example: strided access pattern[\#](#example-strided-access-pattern "Link to this heading"){.headerlink}

Consider this kernel that reads from an input array with a configurable stride (distance between consecutive elements accessed by each thread):

:
{.highlight-cuda .notranslate}

highlight
    __global__ void strided_read_kernel(const float* __restrict__ in,
                                        float* __restrict__ out,
                                        std::size_t N, std::size_t stride)
    {
        const std::size_t t  = blockIdx.x * blockDim.x + threadIdx.x;
        const std::size_t T  = gridDim.x * blockDim.x;

        float acc = 0.f;

        for (std::size_t j = t * stride; j < N; j += T * stride)
        {
            // across a warp, addresses differ by (stride * sizeof(float))
            float v = in[j]; // perfectly coalesced for stride == 1
            acc = acc * 1.000000119f + v;  // force compiler to keep the load
        }

        // one write per thread (negligible vs reads)
        if (t < N) out[t] = acc;
    }

:

When [`stride`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`==`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`1`{.docutils .literal .notranslate}]{.pre}, threads in the same warp access consecutive 4-byte elements ([`in[j]`{.docutils .literal .notranslate}]{.pre}, [`in[j+1]`{.docutils .literal .notranslate}]{.pre}, [`in[j+2]`{.docutils .literal .notranslate}]{.pre}, ...). These accesses fall into a small number of aligned DRAM bursts, so the memory system can coalesce them efficiently and deliver high bandwidth.

As stride increases:

- The addresses accessed by neighboring threads move farther apart

- Each warp's loads spread across more bursts

- The number of physical transactions per logical access increases

- Effective bandwidth drops
::

:::::::::
{#bank-conflict-theory .section}
[]{#bank-conflicts-theory}

### Bank conflict theory[\#](#bank-conflict-theory "Link to this heading"){.headerlink}

Shared memory (LDS) is organized into banks that can be accessed independently. Bank conflicts occur when multiple threads access different addresses in the same bank.

A bank conflict occurs when multiple threads in a [[warp]{.std .std-ref}](programming_model.html#wavefront){.reference .internal} simultaneously access different addresses that reside in the same [[LDS]{.std .std-ref}](hardware_implementation.html#lds){.reference .internal} bank. When that happens, the accesses to that bank must be serialized, reducing effective LDS throughput by an integer factor and preventing full utilization of the on-chip memory bandwidth.

On AMD GPUs, the on-chip LDS (HIP's "shared memory") inside each compute unit is physically organized into banks. These banks can be accessed in parallel, which is how LDS achieves very high bandwidth. On CDNA and RDNA architectures, LDS is divided into 32 (CDNA, CDNA2 and CDNA3) or 64 (CDNA4+ and RDNA2+) banks, each 4 bytes wide. Conceptually, addresses map to banks like this (low bits only, in bytes):

:
{.highlight-text .notranslate}

highlight
    Address: 0x00 0x04 0x08 0x0C 0x10 0x14 0x18 0x1C ... 0x7C
    Bank:       0    1    2    3    4    5    6    7 ...   31

    Address: 0x80 0x84 0x88 0x8C 0x90 0x94 0x98 0x9C ... 0xFC
    Bank:       0    1    2    3    4    5    6    7 ...   31

:

Any two addresses that differ by [\\(32 \\times 4 = 128 \\text{bytes}\\)]{.math .notranslate .nohighlight} map to the same bank.

Why bank conflicts matter:

- Conflicts serialize accesses, reducing throughput

- LDS bandwidth drops proportionally to conflict degree

- Can turn parallel operations into sequential ones

Common patterns:

- **No conflict**: Each thread accesses a different bank (full bandwidth)

- **Broadcast**: Multiple threads read the same address (no conflict)

- **N-way conflict**: N threads access the same bank (1/N bandwidth)

::
{#example-conflict-free-access .section}
#### Example: conflict-free access[\#](#example-conflict-free-access "Link to this heading"){.headerlink}

If you access sequential elements of a float array in LDS, different lanes in a warp naturally land in different banks:

:
{.highlight-cuda .notranslate}

highlight
    __shared__ float data[1024];  // in HIP, __shared__ maps to LDS

    int tid = threadIdx.x;
    float value = data[tid];  // addresses: 0x00, 0x04, 0x08, ...

:

For 32 consecutive float elements, this maps cleanly: each 4-byte word goes to a different bank (0--31). All these accesses can be serviced in one LDS transaction, so there are no bank conflicts. This is the "good" pattern.
::

::
{#example-pathological-strided-access-conflict-heavy .section}
#### Example: pathological strided access (conflict-heavy)[\#](#example-pathological-strided-access-conflict-heavy "Link to this heading"){.headerlink}

Now consider a pattern that walks down a column of a row-major LDS array where each row has 32 floats:

:
{.highlight-cuda .notranslate}

highlight
    __shared__ float data[32 * 32];  // 32 columns per row

    int tid = threadIdx.x;
    float value = data[tid * 32];    // addresses: 0x00, 0x80, 0x100, ...
    // recall: sizeof(float) == 4 bytes

:

Here, each successive access is offset by [\\(32 \\times 4 = 128 \\text{bytes}\\)]{.math .notranslate .nohighlight} ---exactly one full bank span. So:

- [`data[0]`{.docutils .literal .notranslate}]{.pre} → bank 0

- [`data[32]`{.docutils .literal .notranslate}]{.pre} → bank 0

- [`data[64]`{.docutils .literal .notranslate}]{.pre} → bank 0

Every lane in the warp is hitting bank 0, but at different addresses, all in the same cycle. These accesses must be serialized by the LDS hardware, which can turn a fast LDS access into a slow operation.
::

{#when-conflicts-don-t-happen .section}
#### When conflicts don't happen[\#](#when-conflicts-don-t-happen "Link to this heading"){.headerlink}

If all threads in a warp access the exact same address in a bank (e.g., all lanes reading the same control value from LDS), hardware can often broadcast that value. In that case, the request is not treated as a conflict---it's one read, fanned out to many lanes.

:::::::::
::::::::::::::

:
{#register-pressure-theory .section}
[]{#id5}

## Register pressure theory[\#](#register-pressure-theory "Link to this heading"){.headerlink}

Register pressure refers to a situation where the register file becomes a performance bottleneck due to excessive demand for registers by active threads.

Register pressure occurs when a kernel requires more registers than optimal for the target occupancy.

In GPU programming, registers are the fastest level of the memory hierarchy, holding per-thread variables for arithmetic and address computation. However, while the compiler (amdclang++ for ROCm) works with an unbounded set of virtual registers, the hardware has only a finite number of physical registers per compute unit.

{#how-register-pressure-arises .section}
### How register pressure arises[\#](#how-register-pressure-arises "Link to this heading"){.headerlink}

Each thread in a [[warp]{.std .std-ref}](programming_model.html#wavefront){.reference .internal} consumes a number of registers as determined by the compiled Instruction Set Architecture (ISA) code (AMD CDNA or RDNA assembly). All threads in a work-group share the same CU, so the total register file usage per work-group depends on both:

- The number of threads per work-group (launch configuration), and

- The number of registers required per thread (kernel complexity)

As the register footprint per work-group increases, fewer work-groups can be resident on a CU at once. This directly reduces occupancy, which in turn limits the ability of the GPU to hide latency through thread-level parallelism. In extreme cases, the compiler may even "spill" register values into [[global memory]{.std .std-ref}](hardware_implementation.html#hbm){.reference .internal}---orders of magnitude slower than register access.

Why register pressure matters:

- Reduces maximum occupancy

- May cause register spilling to memory

- Decreases ability to hide latency

- Lowers overall throughput

The relationship between registers and occupancy:

- More registers per thread → fewer concurrent warps

- Fewer registers per thread → higher occupancy but may need memory spills

- Optimal balance depends on kernel memory access patterns

:

::::::::
{#performance-metrics-explained .section}
[]{#performance-metrics-theory}

## Performance metrics explained[\#](#performance-metrics-explained "Link to this heading"){.headerlink}

Understanding performance metrics is essential for analyzing GPU behavior:

{#peak-rate .section}
### Peak rate[\#](#peak-rate "Link to this heading"){.headerlink}

Peak rate is the theoretical maximum throughput a hardware system can achieve. It represents the absolute upper bound of GPU performance---the architecture's effective 'speed of light.'

Peak rate assumes ideal conditions: every compute unit is fully active, all execution pipelines are perfectly fed, and no constraints (e.g., register pressure, memory stalls, synchronization, or bandwidth limits) impede progress.

The theoretical maximum performance of a GPU:

- **Peak FLOPS**: Maximum floating-point operations per second

- **Peak bandwidth**: Maximum memory throughput

- **Peak instruction rate**: Maximum instructions per cycle

In performance analysis, peak rate serves several roles:

- It defines the compute-bound "roof" in a roofline model

- It forms the denominator for utilization metrics such as pipe utilization or CU utilization

- It provides the theoretical yardstick against which achieved performance (measured FLOPs per second) is compared

Actual performance is always below peak due to various inefficiencies.

::::::
{#utilization-metrics .section}
### Utilization metrics[\#](#utilization-metrics "Link to this heading"){.headerlink}

{#pipe-utilization .section}
[]{#id6}

#### Pipe utilization[\#](#pipe-utilization "Link to this heading"){.headerlink}

Pipe utilization measures how effectively a kernel uses the execution pipelines within each compute unit.

Each CU contains multiple independent execution pipes, each specialized for a different class of operations---for example:

- VALU pipes handle general vector arithmetic (add, multiply, Fused Multiply-Add (FMA))

- MFMA pipes handle matrix operations on [[matrix-fused multiply--accumulate units]{.std .std-ref}](hardware_implementation.html#mfma-units){.reference .internal}

- SALU pipes handle scalar operations

- Load and Store (LDS and VMEM) units handle memory access instructions

- Branch and Control units handle program flow

Pipe utilization quantifies the percentage of each pipeline's peak theoretical throughput that is being achieved, averaged over all active CUs and cycles in which the pipeline is active.

**Pipe utilization**: The percentage of execution cycles where the pipeline is actively processing instructions. Low utilization indicates stalls or insufficient work.

Before analyzing performance at the level of pipe utilization, you should first examine kernel utilization (how often CUs are busy) and CU utilization (how evenly work is distributed across CUs). Once those are sufficient, per-pipe metrics reveal whether the performance limit is arithmetic, memory, or control-bound.

On AMD GPUs, these measurements are exposed through ROCm profiling tools such as [`rocprofv3`{.docutils .literal .notranslate}]{.pre}.

Relevant counters include:

- [`SQ_ACCUM_PREV_HI_BUSY`{.docutils .literal .notranslate}]{.pre} (VALU pipeline busy percentage)

- [`SQ_ACCUM_MFMA_BUSY`{.docutils .literal .notranslate}]{.pre} (MFMA utilization)

- [`SQ_ACCUM_LDS_BUSY`{.docutils .literal .notranslate}]{.pre} and [`SQ_ACCUM_VMEM_BUSY`{.docutils .literal .notranslate}]{.pre} (memory pipelines)

- [`SQ_ACCUM_SALU_BUSY`{.docutils .literal .notranslate}]{.pre} (scalar ALU activity)

Together, these form the pipe utilization profile---showing how well each instruction pipeline is being fed with eligible [[warps]{.std .std-ref}](programming_model.html#wavefront){.reference .internal} and how close the kernel is to saturating the hardware's arithmetic or memory throughput.

{#issue-efficiency .section}
[]{#id7}

#### Issue efficiency[\#](#issue-efficiency "Link to this heading"){.headerlink}

Issue efficiency measures how effectively the warp scheduler on each compute unit keeps the execution pipelines busy by issuing instructions from eligible warps. In a perfectly efficient kernel, the scheduler issues one instruction every cycle for every active CU.

An issue efficiency of 100% means that on every active cycle, at least one warp was eligible and an instruction was successfully issued. Lower values indicate that during some cycles, all active warps were stalled---waiting on memory, dependencies, or resources---and the scheduler was idle, reducing total instruction throughput.

**Issue efficiency**: The ratio of issued instructions to the maximum possible. Low efficiency can indicate instruction cache misses, scheduling inefficiencies, or resource conflicts.

On AMD GPUs, issue efficiency can be measured using hardware performance counters exposed through ROCProfiler or Omnitrace, such as:

- [`SQ_WAVES_BUSY`{.docutils .literal .notranslate}]{.pre} --- percentage of cycles where any warp was actively executing

- [`SQ_WAVES_ISSUED`{.docutils .literal .notranslate}]{.pre} --- number of issued waves per cycle

- [`SQ_ACCUM_INSTS_ISSUED`{.docutils .literal .notranslate}]{.pre} --- total instructions issued per CU

- [`SQ_ACCUM_CYCLES_BUSY`{.docutils .literal .notranslate}]{.pre} --- number of cycles the CU was active

By combining these metrics, you can estimate how efficiently the scheduler keeps the CU's pipelines fed. Low issue efficiency typically signals insufficient concurrency (low occupancy) or high memory latency, both of which prevent the hardware from issuing instructions continuously.

{#cu-utilization .section}
[]{#id8}

#### CU utilization[\#](#cu-utilization "Link to this heading"){.headerlink}

CU utilization measures the percentage of time that compute units on an AMD GPU are actively executing instructions.

Instead of reporting the fraction of time a kernel is executing somewhere on the GPU, CU utilization reports the fraction of time all CUs spend executing warps.

**CU utilization**: The percentage of compute units actively executing work. Low utilization suggests insufficient parallelism, load imbalance, or synchronization overhead.

As with GPU utilization, high CU utilization is generally desirable. It indicates that most CUs are busy executing instructions across the device. However, high CU utilization alone does not guarantee full performance.

If CU utilization is high but throughput remains low, the kernel may not be effectively using the functional pipelines within each CU---such as [[vector ALUs]{.std .std-ref}](hardware_implementation.html#valu){.reference .internal}, [[MFMA tensor cores]{.std .std-ref}](hardware_implementation.html#mfma-units){.reference .internal}, or [[load and store units]{.std .std-ref}](hardware_implementation.html#lsu){.reference .internal}. In that case, you should examine pipe utilization, which measures how fully those individual execution paths are being used.

CU utilization can be observed with AMD's profiling and monitoring tools:

- [`amd-smi`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`metric`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--usage`{.docutils .literal .notranslate}]{.pre} --- reports overall GPU activity percentage

- [`rocprofv3`{.docutils .literal .notranslate}]{.pre} --- provides performance counters like [`SQ_WAVE_CYCLES`{.docutils .literal .notranslate}]{.pre}, [`SQ_BUSY_CYCLES`{.docutils .literal .notranslate}]{.pre}, and per-pipe instruction metrics

- [`rocminfo`{.docutils .literal .notranslate}]{.pre} --- shows the number of CUs available per GPU

In summary, CU utilization captures how actively the GPU's compute units are engaged in running warps. High CU utilization indicates good parallel workload distribution, while low CU utilization may point to poor occupancy, launch configuration limits, or insufficient concurrency.

::
{#branch-efficiency .section}
[]{#id9}

#### Branch efficiency[\#](#branch-efficiency "Link to this heading"){.headerlink}

Branch efficiency measures how often all threads within a [[warp]{.std .std-ref}](programming_model.html#wavefront){.reference .internal} take the same execution path when encountering conditional statements.

It quantifies control-flow uniformity---that is, how often all lanes in a [[warp]{.std .std-ref}](programming_model.html#wavefront){.reference .internal} evaluate a conditional identically. It is calculated as the ratio of uniform branch decisions to total branch instructions executed. High branch efficiency indicates little to no warp divergence, while low branch efficiency means many lanes are masked off due to diverging control flow.

**Branch efficiency**: The ratio of non-divergent to total branches. Low efficiency indicates significant divergence overhead.

Not all conditionals reduce branch efficiency. The common "bounds check" pattern found in most GPU kernels, for instance:

:
{.highlight-cuda .notranslate}

highlight
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx < n)

:

usually has very high branch efficiency, since nearly all warps consist entirely of threads that either satisfy [`idx`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`<`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`n`{.docutils .literal .notranslate}]{.pre} or not---except perhaps for the last partial warp, which straddles the boundary of [`n`{.docutils .literal .notranslate}]{.pre}.

While CPUs also optimize branch behavior, they focus on temporal uniformity---predicting whether the same branch will be taken or not over repeated iterations. GPUs, on the other hand, care about spatial uniformity: whether all lanes in the warp take the same branch at the same time.

On AMD architectures, this spatial uniformity is tracked via the EXEC mask. Divergence forces EXEC to toggle individual bits to deactivate lanes following a different control path. High branch efficiency implies minimal EXEC manipulation, meaning nearly all lanes execute the same instruction stream simultaneously---maximizing SIMD efficiency and overall throughput.
::
::::::
::::::::

::
{#theoretical-performance-limits .section}
[]{#id10}

## Theoretical performance limits[\#](#theoretical-performance-limits "Link to this heading"){.headerlink}

Understanding theoretical limits helps set realistic performance expectations.

{#peak-performance-bounds .section}
### Peak performance bounds[\#](#peak-performance-bounds "Link to this heading"){.headerlink}

Every GPU has theoretical maximum performance determined by:

- Clock frequency and number of compute units

- Instruction throughput per clock cycle

- Memory bandwidth capacity

- Specialized unit capabilities ([[matrix cores]{.std .std-ref}](hardware_implementation.html#mfma-units){.reference .internal}, SFUs)

{#achievable-performance .section}
### Achievable performance[\#](#achievable-performance "Link to this heading"){.headerlink}

Real applications typically achieve a fraction of theoretical peak due to:

- Imperfect resource utilization

- Memory access inefficiencies

- Control flow divergence

- Synchronization overhead

- Launch and scheduling costs

The gap between theoretical and achieved performance reveals optimization opportunities. The roofline model provides a framework for understanding these limits and identifying which factor (compute or memory) constrains performance.

::

{#summary .section}
## Summary[\#](#summary "Link to this heading"){.headerlink}

Understanding GPU performance requires knowledge of several interconnected concepts:

- **Performance bottlenecks**: Whether compute, memory, or overhead limits performance

- **Roofline model**: Visual framework for analyzing performance limits based on arithmetic intensity

- **Arithmetic intensity**: The compute-to-memory ratio of algorithms

- **Latency hiding**: How concurrent execution masks delays through warp switching

- **Occupancy**: How warp concurrency affects resource utilization

- **Memory hierarchy**: How different memory types affect bandwidth and the importance of coalescing

- **Performance metrics**: Quantitative measures for analysis including pipe utilization, issue efficiency, CU utilization, and branch efficiency

These theoretical foundations inform practical optimization decisions. For step-by-step optimization techniques and practical guidance, see [[Performance guidelines]{.doc}](../how-to/performance_guidelines.html){.reference .internal}.

:::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

{.bd-sidebar-secondary .bd-toc}
::
{.sidebar-secondary-items .sidebar-secondary__inner}
:
sidebar-secondary-item

{.page-toc .tocsection .onthispage}
Contents

:
::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
