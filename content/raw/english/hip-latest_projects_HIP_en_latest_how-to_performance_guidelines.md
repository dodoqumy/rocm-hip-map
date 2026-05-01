---
title: "Performance guidelines &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/performance_guidelines.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T06:58:59.509516+00:00
content_hash: "22c807d9f9a4af52"
---

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
{#main-content .bd-main role="main"}

sbt-scroll-pixel-helper

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
bd-content
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
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
# Performance guidelines

::
{#print-main-content}
:
{#jb-print-toc}

{}
## Contents

:
::

{#searchbox}

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
{#performance-guidelines .section}
[]{#how-to-performance-guidelines}

# Performance guidelines[\#](#performance-guidelines "Link to this heading"){.headerlink}

The AMD HIP performance guidelines provide practical, actionable techniques for optimizing application performance on AMD GPUs. This guide focuses on step-by-step instructions and best practices for improving performance.

For theoretical foundations and performance concepts, see [[Understanding GPU performance]{.doc}](../understand/performance_optimization.html){.reference .internal}.

{#optimization-workflow .section}
## Optimization workflow[\#](#optimization-workflow "Link to this heading"){.headerlink}

Follow this systematic approach to optimize GPU performance:

1.  **Profile and measure baseline**

    Use [`rocprofv3`{.docutils .literal .notranslate}]{.pre} to identify bottlenecks:

    :
{.highlight-bash .notranslate}
    
highlight
        rocprofv3 --stats --<tracing_option> -- <application_path>
    
    :

    Collect metrics on kernel execution time, memory bandwidth, occupancy, and CU utilization. For more details on using [`rocprofv3`{.docutils .literal .notranslate}]{.pre} for application tracing and profiling, see [[rocprofv3 documentation]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/how-to/using-rocprofv3.html "(in Rocprofiler SDK v1.1.0)"){.reference .external}.

2.  **Analyze metrics to identify bottlenecks**

    Determine if kernels are compute-bound or memory-bound. Check arithmetic intensity, memory bandwidth achieved vs peak, and compute throughput.

    For understanding the roofline model, see [[Roofline model]{.std .std-ref}](../understand/performance_optimization.html#roofline-model){.reference .internal}.

3.  **Apply targeted optimizations**

    Based on identified bottlenecks, apply techniques from this guide.

4.  **Verify improvements**

    Re-profile to confirm performance gains.

5.  **Iterate**

    Repeat until performance goals are met.

:::::::
{#profiling-and-analysis-tools .section}
## Profiling and analysis tools[\#](#profiling-and-analysis-tools "Link to this heading"){.headerlink}

ROCm provides a comprehensive suite of profiling and analysis tools that help developers understand and optimize GPU performance. These tools are essential for identifying bottlenecks and evaluating the effectiveness of performance optimizations.

:
{#rocprofv3 .section}
### rocprofv3[\#](#rocprofv3 "Link to this heading"){.headerlink}

The tool [[rocprofv3]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/how-to/using-rocprofv3.html "(in Rocprofiler SDK v1.1.0)"){.reference .external} provides command-line-driven profiling for detailed performance analysis. It collects metrics on kernel execution time, memory bandwidth, warp occupancy, VALU utilization, and instruction-level counters.

[`rocprofv3`{.docutils .literal .notranslate}]{.pre} integrates with the [[rocProfiler-SDK framework]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/index.html "(in Rocprofiler SDK v1.1.0)"){.reference .external} to collect hardware traces and API-level timing data. The collected data can be exported in JSON and CSV formats for further analysis or visualization.

Key capabilities:

- Kernel execution profiling

- Memory bandwidth analysis

- Warp occupancy metrics

- Compute unit utilization

- Instruction-level performance counters

- API call tracing

- Hardware event collection

{#trace-visualization-with-perfetto .section}
#### Trace visualization with Perfetto[\#](#trace-visualization-with-perfetto "Link to this heading"){.headerlink}

For application-level tracing, [`rocprofv3`{.docutils .literal .notranslate}]{.pre} can generate traces compatible with [Perfetto](https://ui.perfetto.dev){.reference .external}, a third-party, open-source trace viewer. This enables visualization of the complete timeline of application execution, including the temporal relationships among host operations, kernel launches, memory transfers, and synchronization events.

Using Perfetto with traces generated by [`rocprofv3`{.docutils .literal .notranslate}]{.pre} can help identify performance issues caused by API overhead, inefficient synchronization, or insufficient overlap between computation and data movement.

The following trace data is available for visualization:

- Application execution timelines

- HIP API call tracking and timing

- ROCm library call analysis

- Host-device synchronization events

- Memory transfer operations

:

{#rocprof-compute-viewer .section}
### ROCprof Compute Viewer[\#](#rocprof-compute-viewer "Link to this heading"){.headerlink}

[ROCprof Compute Viewer](https://rocm.docs.amd.com/projects/rocprof-compute-viewer/en/latest/){.reference .external} provides a GUI-based environment for analyzing GPU kernel performance data. It delivers detailed kernel-level insights, including counter correlation and hierarchical performance breakdowns, helping developers interpret execution patterns and identify optimization opportunities.

Key features:

- Kernel performance counter analysis

- Counter correlation and visualization

- Hierarchical kernel performance breakdown

- Interactive performance data exploration

- Kernel-level optimization insights

::
{#amd-system-management-interface .section}
### AMD System Management Interface[\#](#amd-system-management-interface "Link to this heading"){.headerlink}

The [[AMD System Management Interface]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/amdsmi/en/latest/index.html "(in AMD SMI v26.2.2)"){.reference .external} (AMD SMI) is a command-line utility for querying, monitoring, and managing AMD GPUs. It provides system administrators and developers with detailed, real-time information about GPU hardware, utilization, and power metrics.

[`amd-smi`{.docutils .literal .notranslate}]{.pre} reports the following categories of information:

- GPU identity information, such as the card name, device ID, and PCI bus location

- Live utilization metrics, including GPU activity, memory usage, clock speeds, and active processes

- Power and thermal readings, such as temperature, fan speed, voltage, and power draw

- Performance states and limits, such as available frequency levels, clock throttling, and voltage controls

These metrics are retrieved through the AMD SMI C API, which exposes a stable, scriptable interface for system and performance monitoring tools.

[`amd-smi`{.docutils .literal .notranslate}]{.pre} also supports management operations, including:

- Setting power caps and performance profiles

- Adjusting clock frequencies

- Performing GPU resets and controlling persistence mode

- Reporting or controlling ECC status on supported data center GPUs

Output can be formatted as human-readable text or JSON ([`--json`{.docutils .literal .notranslate}]{.pre}), commonly used for integration into automated monitoring pipelines.

Basic usage examples:

:
{.highlight-shell .notranslate}

highlight
    # Display GPU information
    amd-smi static

    # Monitor GPU utilization and metrics
    amd-smi metric --usage

    # Show detailed information in JSON format
    amd-smi static --json

:
::

{#typical-workflow .section}
### Typical workflow[\#](#typical-workflow "Link to this heading"){.headerlink}

For comprehensive ROCm performance analysis:

1.  Use [`rocprofv3`{.docutils .literal .notranslate}]{.pre} to collect profiling data and generate traces

2.  Use ROCprof Compute Viewer for detailed kernel performance analysis and counter correlation

3.  Use third-party tools like Perfetto to visualize application traces, API calls, and timeline behavior

4.  Use [`amd-smi`{.docutils .literal .notranslate}]{.pre} to monitor GPU utilization and system health

5.  Iterate between profiling and optimization, verifying improvements with each change

This multi-tool approach provides kernel-level metrics, application-level tracing, system monitoring, and visual context to understand overall performance behavior.

:::::::

{#parallel-execution .section}
[]{#id1}

## Parallel execution[\#](#parallel-execution "Link to this heading"){.headerlink}

For optimal use and to keep all system components busy, the application must reveal and efficiently provide as much parallelism as possible.

{#application-level .section}
### Application level[\#](#application-level "Link to this heading"){.headerlink}

To enable parallel execution across the host and devices:

- Use [[asynchronous calls and streams]{.std .std-ref}](hip_runtime_api/asynchronous.html#asynchronous-how-to){.reference .internal}

- Assign serial workloads to the host

- Assign parallel workloads to the devices

For parallel workloads:

- Use [`__syncthreads()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre} (see [[Synchronization functions]{.std .std-ref}](hip_cpp_language_extensions.html#synchronization-functions){.reference .internal}) for intra-block synchronization

- Use global memory with separate kernel invocations for inter-block synchronization (has overhead, minimize when possible)

{#device-level .section}
### Device level[\#](#device-level "Link to this heading"){.headerlink}

Maximize parallel execution across multiprocessors:

- Execute multiple kernels concurrently on a device

- Use streams to overlap computation and data transfers

- Keep all multiprocessors busy with enough concurrent kernels

- Avoid launching too many kernels (causes resource contention)

{#multiprocessor-level .section}
### Multiprocessor level[\#](#multiprocessor-level "Link to this heading"){.headerlink}

Maximize parallel execution within each [[compute unit]{.std .std-ref}](../understand/hardware_implementation.html#compute-unit){.reference .internal}:

- Ensure sufficient resident [[warps]{.std .std-ref}](../understand/programming_model.html#wavefront){.reference .internal} for every clock cycle

- Exploit instruction-level parallelism within warps

- Exploit thread-level parallelism across warps

- Balance resource usage for optimal [[occupancy]{.std .std-ref}](../understand/performance_optimization.html#occupancy){.reference .internal}

::::::::::::::::::::
{#memory-throughput-optimization .section}
[]{#memory-optimization}

## Memory throughput optimization[\#](#memory-throughput-optimization "Link to this heading"){.headerlink}

The first step in maximizing memory throughput is to minimize low-bandwidth data transfers between the host and the device.

Additionally, maximize the use of on-chip memory (shared memory and caches) and minimize transfers with global memory.

::::::
{#data-transfer-optimization .section}
[]{#data-transfer}

### Data transfer optimization[\#](#data-transfer-optimization "Link to this heading"){.headerlink}

**Minimize host-device transfers**

- Move computations from host to device when possible

- Create, use, and discard intermediate data structures on device

- Avoid unnecessary copies to host memory

**Batch small transfers**

Each memory transfer incurs a fixed overhead from driver calls and PCIe transaction setup. Consolidating many small transfers into a single large transfer amortizes this overhead across more data, resulting in much higher effective bandwidth.

:
{.highlight-cuda .notranslate}

highlight
    // Instead of many small transfers
    for (int i = 0; i < n; i++) {
        hipMemcpy(&d_data[i], &h_data[i], sizeof(float), ...);
    }

    // Use a single large transfer
    hipMemcpy(d_data, h_data, n * sizeof(float), ...);

:

**Use page-locked memory for transfers**

Page-locked (pinned) memory cannot be swapped to disk by the operating system, allowing the GPU to access it directly via DMA without CPU involvement. This eliminates an extra copy through a staging buffer and achieves higher bandwidth.

:
{.highlight-cuda .notranslate}

highlight
    float* h_pinned;
    hipHostMalloc(&h_pinned, size);
    // Faster transfers than pageable memory
    hipMemcpy(d_data, h_pinned, size, hipMemcpyHostToDevice);

:

**Use mapped memory on integrated systems**

On integrated GPUs (APUs), the CPU and GPU share the same physical memory. Mapped page-locked memory allows zero-copy access, where the GPU reads directly from host memory without requiring an explicit transfer, eliminating redundant copies.

:
{.highlight-cuda .notranslate}

highlight
    int integrated;
    hipDeviceGetAttribute(&integrated, hipDeviceAttributeIntegrated, device);
    if (integrated) {
        // Use mapped page-locked memory - no explicit copy needed
        hipHostMalloc(&ptr, size, hipHostMallocMapped);
    }

:
::::::

::::::::::::
{#device-memory-access .section}
[]{#id2}

### Device memory access[\#](#device-memory-access "Link to this heading"){.headerlink}

**Ensure proper alignment**

Memory hardware loads data in aligned chunks (typically 128 bytes). Using naturally aligned data types ensures each access maps to a single memory transaction, maximizing bandwidth and avoiding split transactions.

:
{.highlight-cuda .notranslate}

highlight
    // Use naturally aligned types
    float4 data;  // 16-byte aligned
    float2 data;  // 8-byte aligned

    // Ensure structure alignment
    struct __align__(16) MyStruct {
        float4 data;
    };

:

**Optimize 2D array access**

Padding 2D arrays to multiples of the warp size ensures each row starts at an aligned memory boundary. This allows consecutive threads accessing the same row to generate coalesced memory transactions, thereby maximizing bandwidth.

:
{.highlight-cuda .notranslate}

highlight
    // Ensure array width is multiple of warp size
    int width = ((actual_width + warpSize - 1) / warpSize) * warpSize;
    hipMalloc(&array, width * height * sizeof(float));

    // Access pattern
    int idx = x + width * y;  // width should be warp-aligned

:

**Coalesce memory accesses**

When consecutive threads in a warp access consecutive memory addresses, the hardware combines these into a single wide transaction. Non-coalesced patterns require multiple transactions, reducing effective bandwidth.

:
{.highlight-cuda .notranslate}

highlight
    // Good: consecutive threads access consecutive addresses
    int idx = threadIdx.x + blockIdx.x * blockDim.x;
    data[idx] = value;

    // Bad: strided access
    int idx = threadIdx.x * stride;  // Non-coalesced if stride > 1
    data[idx] = value;

:

For understanding memory coalescing theory, see [[Memory hierarchy impact on performance]{.std .std-ref}](../understand/performance_optimization.html#memory-hierarchy-theory){.reference .internal}.

**Use shared memory for data reuse**

Shared memory ([[LDS]{.std .std-ref}](../understand/hardware_implementation.html#lds){.reference .internal}) provides fast on-CU scratchpad memory for communication between threads in a block. Loading data into shared memory once and reusing it many times reduces global memory traffic, particularly effective for tiled algorithms such as matrix multiplication.

:
{.highlight-cuda .notranslate}

highlight
    __global__ void optimized_kernel(float* input, float* output) {
        __shared__ float tile[TILE_SIZE][TILE_SIZE];

        // Load data into shared memory
        tile[threadIdx.y][threadIdx.x] = input[...];
        __syncthreads();

        // Reuse data from fast shared memory
        float result = 0;
        for (int i = 0; i < TILE_SIZE; i++) {
            result += tile[threadIdx.y][i] * tile[i][threadIdx.x];
        }
        __syncthreads();

        output[...] = result;
    }

:

**Avoid bank conflicts in shared memory**

Shared memory is organized into banks, each capable of servicing one request per cycle. When multiple threads in a [[warp]{.std .std-ref}](../understand/programming_model.html#wavefront){.reference .internal} access the same bank simultaneously, the requests are serialized, reducing throughput. Padding arrays by one element shifts addresses to avoid systematic conflicts.

:
{.highlight-cuda .notranslate}

highlight
    // Bad: power-of-2 stride causes conflicts
    __shared__ float data[32][32];
    float value = data[threadIdx.x][threadIdx.y];

    // Good: padding avoids conflicts
    __shared__ float data[32][33];  // Extra column
    float value = data[threadIdx.x][threadIdx.y];

:

For bank conflict theory, see [[Bank conflict theory]{.std .std-ref}](../understand/performance_optimization.html#bank-conflicts-theory){.reference .internal}.

**Use texture memory for 2D spatial access**

Texture memory provides hardware-accelerated 2D filtering and caching optimized for spatial locality. It automatically handles boundary conditions and can interpolate values, making it ideal for image processing and nearby-neighbor access patterns.

:
{.highlight-cuda .notranslate}

highlight
    // Create texture object
    hipTextureObject_t texObj;
    hipCreateTextureObject(&texObj, &resDesc, &texDesc, NULL);

    // Access in kernel
    float value = tex2D<float>(texObj, x, y);

:
::::::::::::
::::::::::::::::::::

:::::::::::::::::::
{#instruction-throughput-optimization .section}
[]{#instruction-optimization}

## Instruction throughput optimization[\#](#instruction-throughput-optimization "Link to this heading"){.headerlink}

::::::
{#arithmetic-instructions .section}
### Arithmetic instructions[\#](#arithmetic-instructions "Link to this heading"){.headerlink}

**Use efficient operations**

Division requires many more hardware cycles than multiplication. Similarly, bitwise operations (shifts, AND, OR) are single-cycle instructions on integer units, making them far more efficient than equivalent arithmetic for power-of-two calculations.

:
{.highlight-cuda .notranslate}

highlight
    // Prefer multiplication over division
    float result = value * 0.5f;     // Fast
    float result = value / 2.0f;     // Slower

    // Use bitwise operations for powers of 2
    int index = threadIdx.x << 2;    // Multiply by 4
    int mask = (1 << n) - 1;         // Create bit mask

:

**Use single-precision when possible**

AMD GPUs have significantly higher throughput for single-precision (FP32) operations compared to double-precision (FP64). Using single-precision math functions can deliver substantial performance gains when FP64 accuracy is not required.

:
{.highlight-cuda .notranslate}

highlight
    // Single-precision (faster)
    float result = sinf(x);
    float result = expf(x);

    // Double-precision (slower, use only when necessary)
    double result = sin(x);
    double result = exp(x);

:

**Leverage fast math intrinsics**

Hardware-specific intrinsics bypass certain accuracy checks and use lookup tables or polynomial approximations, trading slight precision loss for significantly higher throughput. These should be used when the application can tolerate reduced precision.

:
{.highlight-cuda .notranslate}

highlight
    // Fast intrinsic versions
    float ex = __expf(x);            // Fast exponential
    float lg = __logf(x);            // Fast logarithm
    float sq = __fsqrt_rn(x);        // Fast square root
    float rc = __frcp_rn(x);         // Fast reciprocal

:
::::::

::::::
{#control-flow-optimization .section}
[]{#control-flow-instructions}

### Control flow optimization[\#](#control-flow-optimization "Link to this heading"){.headerlink}

**Minimize divergence**

When threads in a warp take different execution paths, the hardware serializes both branches, executing each path with only the relevant threads active. This reduces effective parallelism and wastes cycles on inactive threads.

:
{.highlight-cuda .notranslate}

highlight
    // Good: no divergence (condition depends on threadIdx)
    if (threadIdx.x < 32) {
        // All threads in first half-warp execute
    }

    // Bad: divergence within warp
    if (data[threadIdx.x] > threshold) {
        // Some threads execute, others don't
    }

:

**Use branch hints for predictable conditions**

Providing hints about branch likelihood helps the compiler generate better instruction ordering and can improve the branch predictor's accuracy, reducing pipeline stalls when the prediction proves correct.

:
{.highlight-cuda .notranslate}

highlight
    if (__builtin_expect(rare_condition, 0)) {
        // Unlikely branch
    }

    // C++20 attribute
    if (common_condition) [[likely]] {
        // Likely branch
    }

:

**Avoid divergent warps**

When divergence is unavoidable, restructure the code to separate divergent paths into different kernel launches or use predication (branchless programming) to keep all threads active, though computing unnecessary values may be acceptable if it avoids the serialization penalty.

:
{.highlight-cuda .notranslate}

highlight
    // Instead of:
    if (threadIdx.x % 2 == 0) {
        result = compute_even();
    } else {
        result = compute_odd();
    }

    // Consider separating into different kernels or using predication

:
::::::

::::
{#synchronization .section}
### Synchronization[\#](#synchronization "Link to this heading"){.headerlink}

**Use minimal synchronization**

Each synchronization point stalls all threads in a block until the slowest one reaches the barrier. Minimize synchronizations by carefully analyzing data dependencies---only synchronize when threads genuinely need to exchange data through shared memory.

:
{.highlight-cuda .notranslate}

highlight
    __global__ void kernel() {
        __shared__ float data[256];

        // Load phase
        data[threadIdx.x] = input[...];
        __syncthreads();  // Necessary sync

        // Compute phase - no sync needed if threads are independent
        float result = compute(data[...]);

        // Store phase - sync only if needed
        output[...] = result;
    }

:

**Use streams for async execution**

Streams enable concurrent execution of independent operations. Commands in different streams can overlap in time, allowing kernel execution and memory transfers to run simultaneously. This maximizes GPU utilization by keeping multiple execution engines busy concurrently.

:
{.highlight-cuda .notranslate}

highlight
    hipStream_t stream1, stream2;
    hipStreamCreate(&stream1);
    hipStreamCreate(&stream2);

    // Overlap independent operations
    kernel1<<<grid, block, 0, stream1>>>(...);
    kernel2<<<grid, block, 0, stream2>>>(...);

    hipStreamSynchronize(stream1);
    hipStreamSynchronize(stream2);

:
::::
:::::::::::::::::::

::::::::
{#managing-register-pressure .section}
## Managing register pressure[\#](#managing-register-pressure "Link to this heading"){.headerlink}

High register usage can limit [[occupancy]{.std .std-ref}](../understand/performance_optimization.html#occupancy){.reference .internal}. Follow these steps:

**Minimize live variables**

The compiler allocates registers for every variable that must remain accessible. Reducing the number of simultaneously live variables frees registers, allowing more warps to fit on each CU. Chaining function calls trades some redundant computation for lower register usage.

:
{.highlight-cuda .notranslate}

highlight
    // Instead of storing all intermediate results
    float a = compute_a();
    float b = compute_b();
    float c = compute_c();
    float result = combine(a, b, c);

    // Recompute or chain operations
    float result = combine(compute_a(), compute_b(), compute_c());

:

**Use shared memory for temporary storage**

Per-thread arrays stored in registers consume valuable register space, limiting [[occupancy]{.std .std-ref}](../understand/performance_optimization.html#occupancy){.reference .internal}. Moving temporary storage to [[shared memory]{.std .std-ref}](../understand/hardware_implementation.html#lds){.reference .internal} trades register usage for shared memory usage, often allowing higher occupancy since shared memory limits are typically less restrictive.

:
{.highlight-cuda .notranslate}

highlight
    // Instead of per-thread arrays (uses registers)
    float temp[100];

    // Use shared memory
    __shared__ float temp[blockDim.x][100];
    float* my_temp = temp[threadIdx.x];

:

**Adjust launch bounds**

The [`__launch_bounds__`{.docutils .literal .notranslate}]{.pre} attribute provides hints to the compiler about expected thread block size and minimum blocks per CU. This guides register allocation decisions, potentially trading per-thread register count for higher occupancy.

:
{.highlight-cuda .notranslate}

highlight
    __global__ void
    __launch_bounds__(256, 4)  // 256 threads, 4 blocks per CU
    my_kernel() {
        // Kernel code
    }

:

**Check register usage during compilation**

The compiler can report per-kernel register usage statistics. Monitoring this output helps identify kernels consuming excessive registers, guiding optimization efforts toward reducing register pressure in the most impactful areas.

:
{.highlight-shell .notranslate}

highlight
    hipcc --resource-usage kernel.hip

:

For register pressure theory, see [[Register pressure theory]{.std .std-ref}](../understand/performance_optimization.html#register-pressure-theory){.reference .internal}.
::::::::

::::::
{#improving-occupancy .section}
## Improving occupancy[\#](#improving-occupancy "Link to this heading"){.headerlink}

Higher [[occupancy]{.std .std-ref}](../understand/performance_optimization.html#occupancy){.reference .internal} helps hide latency. Follow these steps:

**Reduce register usage per thread**

Use techniques from "Managing register pressure" above.

**Reduce shared memory usage per block**

Each [[CU]{.std .std-ref}](../understand/hardware_implementation.html#compute-unit){.reference .internal} has limited [[shared memory]{.std .std-ref}](../understand/hardware_implementation.html#lds){.reference .internal} that must be divided among resident blocks. Reducing per-block shared memory usage allows more blocks to reside simultaneously, increasing [[occupancy]{.std .std-ref}](../understand/performance_optimization.html#occupancy){.reference .internal} and improving latency hiding through greater thread-level parallelism.

:
{.highlight-cuda .notranslate}

highlight
    // Allocate only what's needed
    __shared__ float tile[TILE_SIZE][TILE_SIZE];

    // Or use dynamic allocation
    extern __shared__ float dynamic_shared[];

:

**Optimize block size**

AMD Instinct GPUs execute threads in [[warps]{.std .std-ref}](../understand/programming_model.html#wavefront){.reference .internal} of 64, while AMD Radeon GPUs execute threads in warps of 32. Choosing block sizes as multiples of 64 or 32 prevents partial warps that waste execution slots. Larger blocks (128-256 threads) typically achieve better [[occupancy]{.std .std-ref}](../understand/performance_optimization.html#occupancy){.reference .internal} and resource utilization.

:
{.highlight-cuda .notranslate}

highlight
    // Use multiples of warp size
    dim3 block(64);    // Good for AMD Instinct GPUs (warp=64)
    dim3 block(128);   // Common choice
    dim3 block(256);   // Good for high-occupancy kernels

    // Avoid very small blocks
    dim3 block(32);    // May waste resources on Instinct GPUs

:

**Profile occupancy**

Profiling tools report the ratio of active [[warps]{.std .std-ref}](../understand/programming_model.html#wavefront){.reference .internal} to maximum possible warps per [[CU]{.std .std-ref}](../understand/hardware_implementation.html#compute-unit){.reference .internal}. Low [[occupancy]{.std .std-ref}](../understand/performance_optimization.html#occupancy){.reference .internal} suggests resource constraints (registers or shared memory) are limiting parallelism and may indicate opportunities for optimization.

:
{.highlight-shell .notranslate}

highlight
    rocprofv3 --occupancy ./your_application

:

For occupancy theory, see [[Occupancy theory]{.std .std-ref}](../understand/performance_optimization.html#occupancy){.reference .internal}.
::::::

::::::
{#minimizing-memory-thrashing .section}
## Minimizing memory thrashing[\#](#minimizing-memory-thrashing "Link to this heading"){.headerlink}

Applications frequently allocating and freeing memory might experience slower allocation calls over time. To optimize:

**Allocate early, deallocate late**

Frequent allocation and deallocation causes memory fragmentation and increases allocator overhead. Reusing allocations across iterations amortizes the cost of memory management and maintains better memory locality.

:
{.highlight-cuda .notranslate}

highlight
    // Bad: frequent allocation in loop
    for (int i = 0; i < iterations; i++) {
        float* temp;
        hipMalloc(&temp, size);
        // Use temp
        hipFree(temp);
    }

    // Good: allocate once
    float* temp;
    hipMalloc(&temp, size);
    for (int i = 0; i < iterations; i++) {
        // Reuse temp
    }
    hipFree(temp);

:

**Avoid allocating all available memory**

Reserving some memory headroom prevents allocation failures and system instability. The driver and runtime need workspace for internal operations, and leaving a safety margin ensures stable operation without unexpected out-of-memory errors.

:
{.highlight-cuda .notranslate}

highlight
    std::size_t free, total;
    hipMemGetInfo(&free, &total);

    // Don't allocate all free memory
    std::size_t safe_size = free * 0.9;  // Leave some margin

:

**Use managed memory for oversubscription**

Managed memory automatically migrates data between host and device on demand, allowing allocations larger than physical GPU memory. Prefetching hints help the runtime optimize page placement, reducing migration overhead during kernel execution.

:
{.highlight-cuda .notranslate}

highlight
    // Allows exceeding physical memory
    float* data;
    hipMallocManaged(&data, large_size);

    // Optionally prefetch to device
    hipMemPrefetchAsync(data, size, device, stream);

:
::::::

{#summary .section}
## Summary[\#](#summary "Link to this heading"){.headerlink}

Key optimization techniques:

- **Profile first**: Use [`rocprofv3`{.docutils .literal .notranslate}]{.pre} to identify actual bottlenecks

- **Parallelize effectively**: Maximize work at all levels (application, device, CU)

- **Optimize memory**: Minimize transfers, maximize coalescing, use LDS

- **Manage resources**: Balance registers, shared memory, and occupancy

- **Minimize divergence**: Structure control flow to keep [[warps]{.std .std-ref}](../understand/programming_model.html#wavefront){.reference .internal} coherent

For understanding the theory behind these techniques, refer to [[Understanding GPU performance]{.doc}](../understand/performance_optimization.html){.reference .internal} and [[Hardware implementation]{.doc}](../understand/hardware_implementation.html){.reference .internal}.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

{.bd-sidebar-secondary .bd-toc}
::
{.sidebar-secondary-items .sidebar-secondary__inner}
:
sidebar-secondary-item

{.page-toc .tocsection .onthispage}
Contents

:
::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
