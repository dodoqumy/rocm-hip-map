---
title: "Cooperative groups &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_runtime_api/cooperative_groups.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T06:58:39.660237+00:00
content_hash: "2a62c2350c6a592a"
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
# Cooperative groups

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
{#cooperative-groups .section}
[]{#cooperative-groups-how-to}

# Cooperative groups[\#](#cooperative-groups "Link to this heading"){.headerlink}

The cooperative groups API is an extension to the HIP programming model, which provides developers with a flexible, dynamic grouping mechanism for the communicating threads. Cooperative groups let you define your own set of thread groups which may fit your use-cases better than those defined by the hardware. This lets you specify the level of granularity for thread communication which can lead to more efficient parallel decompositions.

The API is accessible in the [`cooperative_groups`{.docutils .literal .notranslate}]{.pre} namespace after the [`hip_cooperative_groups.h`{.docutils .literal .notranslate}]{.pre} header is included. The header contains the following elements:

- Static functions to create groups and subgroups.

- Hardware-accelerated operations over the whole group, like shuffles.

- Data types of cooperative groups.

- Synchronize member function of the groups.

- Get group properties member functions.

::
{#cooperative-groups-thread-model .section}
## Cooperative groups thread model[\#](#cooperative-groups-thread-model "Link to this heading"){.headerlink}

The thread hierarchy abstractions of cooperative groups are depicted in the following figures: [[grid hierarchy]{.std .std-ref}](#coop-thread-top-hierarchy){.reference .internal} and [[block hierarchy]{.std .std-ref}](#coop-thread-bottom-hierarchy){.reference .internal}.

<figure id="id1" class="align-default">
<span id="coop-thread-top-hierarchy"></span><img src="../../_images/thread_hierarchy_coop_top.svg" alt="Diagram depicting nested rectangles of varying color. The outermost one titled &quot;Grid&quot;, inside sets of different sized rectangles layered on one another titled &quot;Block&quot;. Each &quot;Block&quot; containing sets of uniform rectangles layered on one another titled &quot;Warp&quot;. Each of the &quot;Warp&quot; titled rectangles filled with downward pointing arrows inside." />
<figcaption><p><span class="caption-text">Cooperative group thread hierarchy in grids.</span><a href="#id1" class="headerlink" title="Link to this image">#</a></p></figcaption>
</figure>

The **multi grid** is an abstraction of potentially multiple simultaneous launches of the same kernel over multiple devices. The **grid** in cooperative groups is a single dispatch of kernels for execution like the original grid.

{.admonition .note}
Note

- The ability to synchronize over a grid or multi grid requires the kernel to be launched using the specific cooperative groups API.

- Multi grid deprecated since ROCm 5.0.

The **block** is the same as the [[Hierarchical thread model]{.std .std-ref}](../../understand/programming_model.html#inherent-thread-model){.reference .internal} block entity.

{.admonition .note}
Note

Explicit warp-level thread handling is absent from the Cooperative groups API. In order to exploit the known hardware SIMD width on which built-in functionality translates to simpler logic, you can use the group partitioning part of the API, such as [`tiled_partition`{.docutils .literal .notranslate}]{.pre}.

<figure id="id2" class="align-default">
<span id="coop-thread-bottom-hierarchy"></span><img src="../../_images/thread_hierarchy_coop_bottom.svg" alt="The new level between block thread and threads." />
<figcaption><p><span class="caption-text">Cooperative group thread hierarchy in blocks.</span><a href="#id2" class="headerlink" title="Link to this image">#</a></p></figcaption>
</figure>

The cooperative groups API introduce a new level between block thread and threads. The [[thread-block tile]{.std .std-ref}](#coop-thread-block-tile){.reference .internal} give the opportunity to have tiles in the thread block, while the [[coalesced group]{.std .std-ref}](#coop-coalesced-groups){.reference .internal} holds the active threads of the parent group. These groups further discussed in the [[groups types]{.std .std-ref}](#coop-group-types){.reference .internal} section.

For details on memory model, check the [[memory model description]{.std .std-ref}](../../understand/programming_model.html#memory-hierarchy){.reference .internal}.
::

:::::::::::::::::::::::::::::
{#group-types .section}
[]{#coop-group-types}

## Group types[\#](#group-types "Link to this heading"){.headerlink}

Group types are based on the levels of synchronization and data sharing among threads.

::::
{#thread-block-group .section}
### Thread-block group[\#](#thread-block-group "Link to this heading"){.headerlink}

Represents an intra-block cooperative groups type where the participating threads within the group are the same threads that participated in the currently executing [`block`{.docutils .literal .notranslate}]{.pre}.

:
{.highlight-cpp .notranslate}

highlight
    class thread_block;

:

Constructed via:

:
{.highlight-cpp .notranslate}

highlight
    thread_block g = this_thread_block();

:

The [`group_index()`{.docutils .literal .notranslate}]{.pre} , [`thread_index()`{.docutils .literal .notranslate}]{.pre} , [`thread_rank()`{.docutils .literal .notranslate}]{.pre} , [`size()`{.docutils .literal .notranslate}]{.pre}, [`cg_type()`{.docutils .literal .notranslate}]{.pre}, [`is_valid()`{.docutils .literal .notranslate}]{.pre} , [`sync()`{.docutils .literal .notranslate}]{.pre} and [`group_dim()`{.docutils .literal .notranslate}]{.pre} member functions are public of the thread_block class. For further details, check the [[thread_block references]{.std .std-ref}](../../reference/hip_runtime_api/modules/cooperative_groups_reference.html#thread-block-ref){.reference .internal} .
::::

::::
{#grid-group .section}
### Grid group[\#](#grid-group "Link to this heading"){.headerlink}

Represents an inter-block cooperative groups type where the group's participating threads span multiple blocks running the same kernel on the same device. Use the cooperative launch API to enable synchronization across the grid group.

:
{.highlight-cpp .notranslate}

highlight
    class grid_group;

:

Constructed via:

:
{.highlight-cpp .notranslate}

highlight
    grid_group g = this_grid();

:

The [`thread_rank()`{.docutils .literal .notranslate}]{.pre} , [`size()`{.docutils .literal .notranslate}]{.pre}, [`cg_type()`{.docutils .literal .notranslate}]{.pre}, [`is_valid()`{.docutils .literal .notranslate}]{.pre} and [`sync()`{.docutils .literal .notranslate}]{.pre} member functions are public of the [`grid_group`{.docutils .literal .notranslate}]{.pre} class. For further details, check the [[grid_group references]{.std .std-ref}](../../reference/hip_runtime_api/modules/cooperative_groups_reference.html#grid-group-ref){.reference .internal}.
::::

::::
{#multi-grid-group .section}
### Multi-grid group[\#](#multi-grid-group "Link to this heading"){.headerlink}

Represents an inter-device cooperative groups type where the participating threads within the group span multiple devices that run the same kernel on the devices. Use the cooperative launch API to enable synchronization across the multi-grid group.

:
{.highlight-cpp .notranslate}

highlight
    class multi_grid_group;

:

Constructed via:

:
{.highlight-cpp .notranslate}

highlight
    // Kernel must be launched with the cooperative multi-device API
    multi_grid_group g = this_multi_grid();

:

The [`num_grids()`{.docutils .literal .notranslate}]{.pre} , [`grid_rank()`{.docutils .literal .notranslate}]{.pre} , [`thread_rank()`{.docutils .literal .notranslate}]{.pre}, [`size()`{.docutils .literal .notranslate}]{.pre}, [`cg_type()`{.docutils .literal .notranslate}]{.pre}, [`is_valid()`{.docutils .literal .notranslate}]{.pre} , and [`sync()`{.docutils .literal .notranslate}]{.pre} member functions are public of the [`multi_grid_group`{.docutils .literal .notranslate}]{.pre} class. For further details check the [[multi_grid_group references]{.std .std-ref}](../../reference/hip_runtime_api/modules/cooperative_groups_reference.html#multi-grid-group-ref){.reference .internal} .
::::

:::::
{#thread-block-tile .section}
[]{#coop-thread-block-tile}

### Thread-block tile[\#](#thread-block-tile "Link to this heading"){.headerlink}

This constructs a templated class derived from [`thread_group`{.docutils .literal .notranslate}]{.pre}. The template defines the tile size of the new thread group at compile time. This group type also supports sub-wave level intrinsics.

:
{.highlight-cpp .notranslate}

highlight
    template <unsigned int Size, typename ParentT = void>
    class thread_block_tile;

:

Constructed via:

:
{.highlight-cpp .notranslate}

highlight
    template <unsigned int Size, typename ParentT>
    _CG_QUALIFIER thread_block_tile<Size, ParentT> tiled_partition(const ParentT& g)

:

{.admonition .note}
Note

- Size must be a power of 2 and not larger than warp (wavefront) size.

- [`shfl()`{.docutils .literal .notranslate}]{.pre} functions support integer or float type.

The [`thread_rank()`{.docutils .literal .notranslate}]{.pre} , [`size()`{.docutils .literal .notranslate}]{.pre}, [`cg_type()`{.docutils .literal .notranslate}]{.pre}, [`is_valid()`{.docutils .literal .notranslate}]{.pre}, [`sync()`{.docutils .literal .notranslate}]{.pre}, [`meta_group_rank()`{.docutils .literal .notranslate}]{.pre}, [`meta_group_size()`{.docutils .literal .notranslate}]{.pre}, [`shfl()`{.docutils .literal .notranslate}]{.pre}, [`shfl_down()`{.docutils .literal .notranslate}]{.pre}, [`shfl_up()`{.docutils .literal .notranslate}]{.pre}, [`shfl_xor()`{.docutils .literal .notranslate}]{.pre}, [`ballot()`{.docutils .literal .notranslate}]{.pre}, [`any()`{.docutils .literal .notranslate}]{.pre}, [`all()`{.docutils .literal .notranslate}]{.pre}, [`match_any()`{.docutils .literal .notranslate}]{.pre} and [`match_all()`{.docutils .literal .notranslate}]{.pre} member functions are public of the [`thread_block_tile`{.docutils .literal .notranslate}]{.pre} class. For further details, check the [[thread_block_tile references]{.std .std-ref}](../../reference/hip_runtime_api/modules/cooperative_groups_reference.html#thread-block-tile-ref){.reference .internal} .
:::::

:::::::
{#coalesced-groups .section}
[]{#coop-coalesced-groups}

### Coalesced groups[\#](#coalesced-groups "Link to this heading"){.headerlink}

Threads (64 threads on CDNA and 32 threads on RDNA) in a warp cannot execute different instructions simultaneously, so conditional branches are executed serially within the warp. When threads encounter a conditional branch, they can diverge, resulting in some threads being disabled if they do not meet the condition to execute that branch. The active threads are referred to as coalesced, and coalesced group represents an active thread group within a warp.

{.admonition .note}
Note

The NVIDIA GPU's independent thread scheduling presents the appearance that threads on different branches execute concurrently.

{.admonition .warning}
Warning

AMD GPUs do not support independent thread scheduling. Some CUDA application can rely on this feature and the ported HIP version on AMD GPUs can deadlock, when they try to make use of independent thread scheduling.

This group type also supports sub-wave level intrinsics.

:
{.highlight-cpp .notranslate}

highlight
    class coalesced_group;

:

Constructed via:

:
{.highlight-cpp .notranslate}

highlight
    coalesced_group active = coalesced_threads();

:

{.admonition .note}
Note

[`shfl()`{.docutils .literal .notranslate}]{.pre} functions support integer or float type.

The [`thread_rank()`{.docutils .literal .notranslate}]{.pre} , [`size()`{.docutils .literal .notranslate}]{.pre}, [`cg_type()`{.docutils .literal .notranslate}]{.pre}, [`is_valid()`{.docutils .literal .notranslate}]{.pre}, [`sync()`{.docutils .literal .notranslate}]{.pre}, [`meta_group_rank()`{.docutils .literal .notranslate}]{.pre}, [`meta_group_size()`{.docutils .literal .notranslate}]{.pre}, [`shfl()`{.docutils .literal .notranslate}]{.pre}, [`shfl_down()`{.docutils .literal .notranslate}]{.pre}, [`shfl_up()`{.docutils .literal .notranslate}]{.pre}, [`ballot()`{.docutils .literal .notranslate}]{.pre}, [`any()`{.docutils .literal .notranslate}]{.pre}, [`all()`{.docutils .literal .notranslate}]{.pre}, [`match_any()`{.docutils .literal .notranslate}]{.pre} and [`match_all()`{.docutils .literal .notranslate}]{.pre} member functions are public of the [`coalesced_group`{.docutils .literal .notranslate}]{.pre} class. For more information, see [[coalesced_group references]{.std .std-ref}](../../reference/hip_runtime_api/modules/cooperative_groups_reference.html#coalesced-group-ref){.reference .internal} .
:::::::
:::::::::::::::::::::::::::::

::::::::::::::
{#cooperative-groups-simple-example .section}
## Cooperative groups simple example[\#](#cooperative-groups-simple-example "Link to this heading"){.headerlink}

The difference to the original block model in the [`reduce_sum`{.docutils .literal .notranslate}]{.pre} device function is the following.

::::::
{.sd-tab-set .docutils}
Original Block

::
{.sd-tab-content .docutils}
:
{.highlight-cuda .notranslate}

highlight
    __device__ int reduce_sum(int *shared, int val) {

        // Thread ID
        const unsigned int thread_id = threadIdx.x;

        // Every iteration the number of active threads
        // halves, until we processed all values
        for(unsigned int i = blockDim.x / 2; i > 0; i /= 2) {
            // Store value in shared memory with thread ID
            shared[thread_id] = val;

            // Synchronize all threads
            __syncthreads();

            // Active thread sum up
            if(thread_id < i)
                val += shared[thread_id + i];

            // Synchronize all threads in the group
            __syncthreads();
        }

        // ...
    }

:
::

Cooperative groups

::
{.sd-tab-content .docutils}
:
{.highlight-cuda .notranslate}

highlight
    __device__ int reduce_sum(thread_group g,
                              int *shared,
                              int val) {

        // Thread ID
        const unsigned int group_thread_id = g.thread_rank();

        // Every iteration the number of active threads
        // halves, until we processed all values
        for(unsigned int i = g.size() / 2; i > 0; i /= 2) {
            // Store value in shared memroy with thread ID
            shared[group_thread_id] = val;

            // Synchronize all threads in the group
            g.sync();

            // Active thread sum up
            if(group_thread_id < i)
                val += shared[group_thread_id + i];

            // Synchronize all threads in the group
            g.sync();
        }

        // ...
    }

:
::
::::::

The [`reduce_sum()`{.docutils .literal .notranslate}]{.pre} function call and input data initialization difference to the original block model is the following.

::::::
{.sd-tab-set .docutils}
Original Block

::
{.sd-tab-content .docutils}
:
{.highlight-cuda .notranslate}

highlight
    __global__ void sum_kernel(...) {

        // ...

        // Workspace array in shared memory
        __shared__ unsigned int workspace[2048];

        // ...

        // Perform reduction
        output = reduce_sum(workspace, input);

        // ...
    }

:
::

Cooperative groups

::
{.sd-tab-content .docutils}
:
{.highlight-cuda .notranslate}

highlight
    __global__ void sum_kernel(...) {

        // ...

        // Workspace array in shared memory
        __shared__ unsigned int workspace[2048];

        // ...

        // Initialize the thread_block
        thread_block thread_block_group = this_thread_block();
        // Perform reduction
        output = reduce_sum(thread_block_group, workspace, input);

        // ...
    }

:
::
::::::

At the device function, the input group type is the [`thread_group`{.docutils .literal .notranslate}]{.pre}, which is the parent class of all the cooperative groups type. With this, you can write generic functions, which can work with any type of cooperative groups.
::::::::::::::

::::::::::::::::::::::::::::
{#synchronization .section}
[]{#coop-synchronization}

## Synchronization[\#](#synchronization "Link to this heading"){.headerlink}

With each group type, the synchronization requires using the correct cooperative groups launch API.

**Check the kernel launch capability**

:::::::
{.sd-tab-set .docutils}
Thread-block

{.sd-tab-content .docutils}
Do not need kernel launch validation.

Grid

::
{.sd-tab-content .docutils}
Confirm the cooperative launch capability on the single AMD GPU:

:
{.highlight-cpp .notranslate}

highlight
    int device               = 0;
    int supports_coop_launch = 0;
    // Check support
    // Use hipDeviceAttributeCooperativeMultiDeviceLaunch when launching across multiple devices
    HIP_CHECK(hipGetDevice(&device));
    HIP_CHECK(
        hipDeviceGetAttribute(&supports_coop_launch, hipDeviceAttributeCooperativeLaunch, device));
    if(!supports_coop_launch)
    {
        std::cout << "Skipping, device " << device << " does not support cooperative groups"
                  << std::endl;
        return 0;
    }

:
::

Multi-grid

::
{.sd-tab-content .docutils}
Confirm the cooperative launch capability over multiple GPUs:

:
{.highlight-cpp .notranslate}

highlight
    // Check support of cooperative groups
    std::vector<int> deviceIDs;
    for(int deviceID = 0; deviceID < device_count; deviceID++) {
    #ifdef __HIP_PLATFORM_AMD__
        int supports_coop_launch = 0;
        HIP_CHECK(
            hipDeviceGetAttribute(
                &supports_coop_launch,
                hipDeviceAttributeCooperativeMultiDeviceLaunch,
                deviceID));
        if(!supports_coop_launch) {
            std::cout << "Skipping, device " << deviceID << " does not support cooperative groups"
                      << std::endl;
        }
        else
    #endif
        {
            std::cout << deviceID << std::endl;
            // Collect valid deviceIDs.
            deviceIDs.push_back(deviceID);
        }
    }

:
::
:::::::

**Kernel launch**

:::::::::
{.sd-tab-set .docutils}
Thread-block

::
{.sd-tab-content .docutils}
You can access the new block representation using the original kernel launch methods.

:
{.highlight-cpp .notranslate}

highlight
    void* params[] = {&d_vector, &d_block_reduced, &d_partition_reduced};
    // Launching kernel from host.
    HIP_CHECK(hipLaunchKernelGGL(vector_reduce_kernel<partition_size>,
                                 dim3(num_blocks),
                                 dim3(threads_per_block),
                                 0,
                                 hipStreamDefault,
                                 &d_vector,
                                 &d_block_reduced,
                                 &d_partition_reduced));

:
::

Grid

::
{.sd-tab-content .docutils}
Launch the cooperative kernel on a single GPU:

:
{.highlight-cpp .notranslate}

highlight
    void* params[] = {};
    // Launching kernel from host.
    HIP_CHECK(hipLaunchCooperativeKernel(vector_reduce_kernel<partition_size>,
                                         dim3(num_blocks),
                                         dim3(threads_per_block),
                                         0,
                                         0,
                                         hipStreamDefault));

:
::

Multi-grid

::
{.sd-tab-content .docutils}
Launch the cooperative kernel over multiple GPUs:

:
{.highlight-cpp .notranslate}

highlight
    hipLaunchParams *launchParamsList = (hipLaunchParams*)malloc(sizeof(hipLaunchParams) * deviceIDs.size());
    for(int deviceID : deviceIDs) {

        // Set device
        HIP_CHECK(hipSetDevice(deviceID));

        // Create stream
        hipStream_t stream;
        HIP_CHECK(hipStreamCreate(&stream));

        // Parameters
        void* params[] = {&(d_vector[deviceID]), &(d_block_reduced[deviceID]), &(d_partition_reduced[deviceID])};

        // Set launchParams
        launchParamsList[deviceID].func = (void*)vector_reduce_kernel<partition_size>;
        launchParamsList[deviceID].gridDim = dim3(1);
        launchParamsList[deviceID].blockDim = dim3(threads_per_block);
        launchParamsList[deviceID].sharedMem = 0;
        launchParamsList[deviceID].stream = stream;
        launchParamsList[deviceID].args = params;
    }

    HIP_CHECK(hipLaunchCooperativeKernelMultiDevice(launchParamsList,
                                                    (int)deviceIDs.size(),
                                                    hipCooperativeLaunchMultiDeviceNoPreSync));

:
::
:::::::::

**Device side synchronization**

:::::::::
{.sd-tab-set .docutils}
Thread-block

::
{.sd-tab-content .docutils}
The device side code of the thread_block synchronization over single GPUs:

:
{.highlight-cpp .notranslate}

highlight
    thread_block g = this_thread_block();
    g.sync();

:
::

Grid

::
{.sd-tab-content .docutils}
The device side code of the grid synchronization over single GPUs:

:
{.highlight-cpp .notranslate}

highlight
    grid_group grid = this_grid();
    grid.sync();

:
::

Multi-grid

::
{.sd-tab-content .docutils}
The device side code of the multi-grid synchronization over multiple GPUs:

:
{.highlight-cpp .notranslate}

highlight
    multi_grid_group multi_grid = this_multi_grid();
    multi_grid.sync();

:
::
:::::::::
::::::::::::::::::::::::::::

{#unsupported-nvidia-cuda-features .section}
## Unsupported NVIDIA CUDA features[\#](#unsupported-nvidia-cuda-features "Link to this heading"){.headerlink}

HIP doesn't support the following NVIDIA CUDA optional headers:

- [`cooperative_groups/memcpy_async.h`{.docutils .literal .notranslate}]{.pre}

- [`cooperative_groups/reduce.h`{.docutils .literal .notranslate}]{.pre}

- [`cooperative_groups/scan.h`{.docutils .literal .notranslate}]{.pre}

HIP doesn't support the following CUDA class in [`cooperative_groups`{.docutils .literal .notranslate}]{.pre} namespace:

- [`cluster_group`{.docutils .literal .notranslate}]{.pre}

HIP doesn't support the following CUDA functions/operators in [`cooperative_groups`{.docutils .literal .notranslate}]{.pre} namespace:

- [`synchronize`{.docutils .literal .notranslate}]{.pre}

- [`memcpy_async`{.docutils .literal .notranslate}]{.pre}

- [`wait`{.docutils .literal .notranslate}]{.pre} and [`wait_prior`{.docutils .literal .notranslate}]{.pre}

- [`invoke_one`{.docutils .literal .notranslate}]{.pre} and [`invoke_one_broadcast`{.docutils .literal .notranslate}]{.pre}

- [`reduce`{.docutils .literal .notranslate}]{.pre}

- [`reduce_update_async`{.docutils .literal .notranslate}]{.pre} and [`reduce_store_async`{.docutils .literal .notranslate}]{.pre}

- Reduce operators [`plus`{.docutils .literal .notranslate}]{.pre} , [`less`{.docutils .literal .notranslate}]{.pre} , [`greater`{.docutils .literal .notranslate}]{.pre} , [`bit_and`{.docutils .literal .notranslate}]{.pre} , [`bit_xor`{.docutils .literal .notranslate}]{.pre} and [`bit_or`{.docutils .literal .notranslate}]{.pre}

- [`inclusive_scan`{.docutils .literal .notranslate}]{.pre} and [`exclusive_scan`{.docutils .literal .notranslate}]{.pre}

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
