---
title: "External resource interoperability &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_runtime_api/external_interop.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T06:59:14.243832+00:00
content_hash: "f3c21dd8180d865c"
---

::::::::::::::::::::::::::::::::::::
{#main-content .bd-main role="main"}

sbt-scroll-pixel-helper

::::::::::::::::::::::::::::::::::
bd-content
:::::::::::::::::::::::::::::
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
# External resource interoperability

::
{#print-main-content}
:
{#jb-print-toc}

{}
## Contents

:
::

{#searchbox}

:::::::::::::::
{#external-resource-interoperability .section}
# External resource interoperability[\#](#external-resource-interoperability "Link to this heading"){.headerlink}

This feature allows HIP to work with resources -- like memory and semaphores -- created by other APIs. This means resources can be used from APIs like CUDA, OpenCL and Vulkan within HIP, making it easier to integrate HIP into existing projects.

To use external resources in HIP, you typically follow these steps:

- Import resources from other APIs using HIP provided functions

- Use external resources as if they were created in HIP

- Destroy the HIP resource object to clean up

{#semaphore-functions .section}
## Semaphore Functions[\#](#semaphore-functions "Link to this heading"){.headerlink}

Semaphore functions are essential for synchronization in parallel computing. These functions facilitate communication and coordination between different parts of a program or between different programs. By managing semaphores, tasks are executed in the correct order, and resources are utilized effectively. Semaphore functions ensure smooth operation, preventing conflicts and maintaining the integrity of processes; upholding the integrity and performance of concurrent processes.

External semaphore functions can be used in HIP as described in [[External resource interoperability]{.std .std-ref}](../../reference/hip_runtime_api/modules/memory_management/external_resource_interoperability.html#external-resource-interoperability-reference){.reference .internal}.

{#memory-functions .section}
## Memory Functions[\#](#memory-functions "Link to this heading"){.headerlink}

HIP external memory functions focus on the efficient sharing and management of memory resources. These functions enable importing memory created by external systems, enabling the HIP program to use this memory seamlessly. Memory functions include mapping memory for effective use and ensuring proper cleanup to prevent resource leaks. This is critical for performance, particularly in applications handling large datasets or complex structures such as textures in graphics. Proper memory management ensures stability and efficient resource utilization.

::::::::::::
{#example .section}
## Example[\#](#example "Link to this heading"){.headerlink}

ROCm examples include a [HIP--Vulkan interoperation example](https://github.com/ROCm/rocm-examples/tree/develop/HIP-Basic/vulkan_interop){.reference .external} demonstrates how to perform interoperation between HIP and Vulkan.

In this example, a simple HIP kernel is used to compute a sine wave, which is then rendered to a window as a graphical output using Vulkan. The process requires several initialization steps, such as setting up a HIP context, creating a Vulkan instance, and configuring the GPU device and queue. After these initial steps, the kernel executes the sine wave computation, and Vulkan continuously updates the window framebuffer to display the computed data until the window is closed.

The following code converts a Vulkan memory handle to its equivalent HIP handle. The input [`VkDeviceMemory`{.docutils .literal .notranslate}]{.pre} and the created HIP memory represents the same physical area of GPU memory, through the handles of each respective API. Writing to the buffer in one API will allow us to read the results through the other. Note that access to the buffer should be synchronized between the APIs, for example using queue syncs or semaphores.

:
{.highlight-cpp .notranslate}

highlight
        // Prepare the HIP external semaphore descriptor with the platform-specific
        // handle type that we wish to import. This value should correspond to the
        // handleTypes field set in VkExportMemoryAllocateInfoKHR while creating the
        // Vulkan buffer.
        hipExternalMemoryHandleDesc desc = {};
        desc.size                        = size;

        // Export the Vulkan buffer handle to a platform-specific native handle, depending
        // on the current platform: On Windows the buffer is converted to a HANDLE, and on Linux
        // to a file descriptor representing the driver's GPU handle to the memory.
        // This native handle is then passed to the HIP external memory descriptor so that it
        // may be imported.
    #ifdef _WIN64
        desc.type = hipExternalMemoryHandleTypeOpaqueWin32Kmt;

        VkMemoryGetWin32HandleInfoKHR get_handle_info = {};
        get_handle_info.sType      = VK_STRUCTURE_TYPE_MEMORY_GET_WIN32_HANDLE_INFO_KHR;
        get_handle_info.memory     = memory;
        get_handle_info.handleType = VK_EXTERNAL_MEMORY_HANDLE_TYPE_OPAQUE_WIN32_KMT_BIT_KHR;

        VK_CHECK(
            ctx.vkd->get_memory_win32_handle(ctx.dev, &get_handle_info, &desc.handle.win32.handle));
    #else
        desc.type = hipExternalMemoryHandleTypeOpaqueFd;

        VkMemoryGetFdInfoKHR get_fd_info = {};
        get_fd_info.sType                = VK_STRUCTURE_TYPE_MEMORY_GET_FD_INFO_KHR;
        get_fd_info.memory               = memory;
        get_fd_info.handleType           = VK_EXTERNAL_MEMORY_HANDLE_TYPE_OPAQUE_FD_BIT_KHR;

        VK_CHECK(ctx.vkd->get_memory_fd(ctx.dev, &get_fd_info, &desc.handle.fd));
    #endif

        // Import the native memory handle to HIP to create an external memory.
        hipExternalMemory_t hip_memory;
        HIP_CHECK(hipImportExternalMemory(&hip_memory, &desc));
        return hip_memory;

:

The Vulkan semaphore is converted to HIP semaphore shown in the following example. Signaling on the semaphore in one API will allow the other API to wait on it, which is how we can guarantee synchronized access to resources in a cross-API manner.

:
{.highlight-cpp .notranslate}

highlight
        // Prepare the HIP external semaphore descriptor with the platform-specific handle type
        // that we wish to import. This value should correspond to the handleTypes field set in
        // the VkExportSemaphoreCreateInfoKHR structure that was passed to Vulkan when creating
        // the semaphore.
        hipExternalSemaphoreHandleDesc desc = {};

        // Export the Vulkan semaphore to a platform-specific handle depending on the current
        // platform: On Windows, we convert the semaphore into a HANDLE, and on Linux it is
        // converted to a file descriptor.
        // This native handle is then passed to the HIP external semaphore descriptor.
    #ifdef _WIN64
        desc.type = hipExternalSemaphoreHandleTypeOpaqueWin32;

        VkSemaphoreGetWin32HandleInfoKHR get_handle_info = {};
        get_handle_info.sType      = VK_STRUCTURE_TYPE_SEMAPHORE_GET_WIN32_HANDLE_INFO_KHR;
        get_handle_info.semaphore  = sema;
        get_handle_info.handleType = VK_EXTERNAL_SEMAPHORE_HANDLE_TYPE_OPAQUE_WIN32_BIT_KHR;

        VK_CHECK(
            ctx.vkd->get_semaphore_win32_handle(ctx.dev, &get_handle_info, &desc.handle.win32.handle));

    #else
        desc.type = hipExternalSemaphoreHandleTypeOpaqueFd;

        VkSemaphoreGetFdInfoKHR get_fd_info = {};
        get_fd_info.sType                   = VK_STRUCTURE_TYPE_SEMAPHORE_GET_FD_INFO_KHR;
        get_fd_info.semaphore               = sema;
        get_fd_info.handleType              = VK_EXTERNAL_SEMAPHORE_HANDLE_TYPE_OPAQUE_FD_BIT_KHR;

        VK_CHECK(ctx.vkd->get_semaphore_fd(ctx.dev, &get_fd_info, &desc.handle.fd));
    #endif

        // Import the native semaphore to HIP to create a HIP external semaphore.
        hipExternalSemaphore_t hip_sema;
        HIP_CHECK(hipImportExternalSemaphore(&hip_sema, &desc));

:

When the HIP external memory is exported from Vulkan and imported to HIP, it is not yet ready for use. The Vulkan handle is shared, allowing for memory sharing rather than copying during the export process. To actually use the memory, we need to map it to a pointer so that we may pass it to the kernel so that it can be read from and written to. The external memory map to HIP in the following example:

:
{.highlight-cpp .notranslate}

highlight
        hipExternalMemoryBufferDesc desc = {};
        desc.offset                      = 0;
        desc.size                        = size;
        desc.flags                       = 0;

        void* ptr;
        HIP_CHECK(hipExternalMemoryGetMappedBuffer(&ptr, mem, &desc));

:

Wait for buffer is ready and not under modification at Vulkan side:

:
{.highlight-cpp .notranslate}

highlight
                hipExternalSemaphoreWaitParams wait_params = {};
                HIP_CHECK(hipWaitExternalSemaphoresAsync(&this->hip_buffer_ready,
                                                         &wait_params,
                                                         1,
                                                         this->hip_stream));

:

The sinewave kernel implementation:

:
{.highlight-cpp .notranslate}

highlight
    /// \brief The main HIP kernel for this example - computes a simple sine wave over a
    /// 2-dimensional grid of points.
    /// \param height_map - the grid of points to compute a sine wave for. It is expected to be
    ///   a \p grid_width by \p grid_height array packed into memory.(y on the inner axis).
    /// \param time - The current time relative to the start of the program.
    __global__ void sinewave_kernel(float* height_map, const float time)
    {
        const float        freq = 10.f;
        const unsigned int x    = blockIdx.x * blockDim.x + threadIdx.x;
        const unsigned int y    = blockIdx.y * blockDim.y + threadIdx.y;
        const float        u    = (2.f * x) / grid_width - 1.f;
        const float        v    = (2.f * y) / grid_height - 1.f;

        if(x < grid_width && y < grid_height)
        {
            height_map[x * grid_width + y] = sinf(u * freq + time) * cosf(v * freq + time);
        }
    }

:

Signal to Vulkan that we are done with the buffer and that it can proceed with rendering:

:
{.highlight-cpp .notranslate}

highlight
            hipExternalSemaphoreSignalParams signal_params = {};
            HIP_CHECK(hipSignalExternalSemaphoresAsync(&this->hip_simulation_finished,
                                                       &signal_params,
                                                       1,
                                                       this->hip_stream));

:
::::::::::::
:::::::::::::::
:::::::::::::::::::::::::::::

{.bd-sidebar-secondary .bd-toc}
::
{.sidebar-secondary-items .sidebar-secondary__inner}
:
sidebar-secondary-item

{.page-toc .tocsection .onthispage}
Contents

:
::

::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::
