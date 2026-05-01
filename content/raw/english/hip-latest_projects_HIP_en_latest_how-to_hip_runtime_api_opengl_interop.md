---
title: "OpenGL interoperability &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_runtime_api/opengl_interop.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T06:58:43.545779+00:00
content_hash: "2d1c0a9eb89f9dbe"
---

:::::::::::::::::::::::::::::::::
{#main-content .bd-main role="main"}

sbt-scroll-pixel-helper

:::::::::::::::::::::::::::::::
bd-content
::::::::::::::::::::::::::
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
# OpenGL interoperability

::
{#print-main-content}
:
{#jb-print-toc}

{}
## Contents

:
::

{#searchbox}

::::::::::::
{#opengl-interoperability .section}
# OpenGL interoperability[\#](#opengl-interoperability "Link to this heading"){.headerlink}

The HIP--OpenGL interoperation involves mapping OpenGL resources, such as buffers and textures, for HIP to interact with OpenGL. This mapping process enables HIP to utilize these resources directly, bypassing the need for costly data transfers between the CPU and GPU. This capability is useful in applications that require both intensive GPU computation and real-time visualization.

The graphics resources must be registered using functions like [[`hipGraphicsGLRegisterBuffer()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../../reference/hip_runtime_api/modules/opengl_interoperability.html#_CPPv427hipGraphicsGLRegisterBufferPP19hipGraphicsResource6GLuintj "hipGraphicsGLRegisterBuffer"){.reference .internal} or [[`hipGraphicsGLRegisterImage()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../../reference/hip_runtime_api/modules/opengl_interoperability.html#_CPPv426hipGraphicsGLRegisterImagePP19hipGraphicsResource6GLuint6GLenumj "hipGraphicsGLRegisterImage"){.reference .internal} then they can be mapped to HIP with [[`hipGraphicsMapResources()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../../reference/hip_runtime_api/modules/graphics_interoperability.html#_CPPv423hipGraphicsMapResourcesiP21hipGraphicsResource_t11hipStream_t "hipGraphicsMapResources"){.reference .internal} function.

After mapping, the [[`hipGraphicsResourceGetMappedPointer()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../../reference/hip_runtime_api/modules/graphics_interoperability.html#_CPPv435hipGraphicsResourceGetMappedPointerPPvP6size_t21hipGraphicsResource_t "hipGraphicsResourceGetMappedPointer"){.reference .internal} or [[`hipGraphicsSubResourceGetMappedArray()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../../reference/hip_runtime_api/modules/graphics_interoperability.html#_CPPv436hipGraphicsSubResourceGetMappedArrayP10hipArray_t21hipGraphicsResource_tjj "hipGraphicsSubResourceGetMappedArray"){.reference .internal} functions used to retrieve a device pointer to the mapped resource, which can then be used in HIP kernels.

Unmapping resources with [[`hipGraphicsUnmapResources()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../../reference/hip_runtime_api/modules/graphics_interoperability.html#_CPPv425hipGraphicsUnmapResourcesiP21hipGraphicsResource_t11hipStream_t "hipGraphicsUnmapResources"){.reference .internal} after computations ensure proper resource management.

:::::::::::
{#example .section}
## Example[\#](#example "Link to this heading"){.headerlink}

ROCm examples have a [HIP--OpenGL interoperation example](https://github.com/ROCm/rocm-examples/tree/develop/HIP-Basic/opengl_interop){.reference .external}, where a simple HIP kernel is used to simulate a sine wave and rendered to a window as a grid of triangles using OpenGL. For a working example, there are multiple initialization steps needed like creating and opening a window, initializing OpenGL or selecting the OpenGL-capable device. After the initialization in the example, the kernel simulates the sinewave and updates the window's framebuffer in a cycle until the window is closed.

::
{.admonition .note}
Note

The more recent OpenGL functions are loaded with [OpenGL loader](https://github.com/ROCm/rocm-examples/tree/develop/External/glad){.reference .external}, as these are not loaded by default on all platforms. The use of a custom loader is shown in the following example

:
{.highlight-cpp .notranslate}

highlight
        // Make GLFW use a custom loader - we need this for the more recent OpenGL functions,
        // as these are not loaded by default on all platforms.
        if(!gladLoadGLLoader(reinterpret_cast<GLADloadproc>(glfwGetProcAddress)))
        {
            std::cerr << "Failed to load OpenGL function pointers" << std::endl;
            return error_exit_code;
        }

:
::

The OpenGL buffer is imported to HIP in the following way:

:
{.highlight-cpp .notranslate}

highlight
            // Import the OpenGL height buffer into a HIP graphics resource.
            HIP_CHECK(hipGraphicsGLRegisterBuffer(
                &this->hip_height_buffer,
                renderer.height_buffer,
                // We are going to write to this buffer from HIP,
                // but we do not need to read from it.
                // As an optimization we can pass hipGraphicsRegisterFlagsWriteDiscard,
                // so that the driver knows that we do not need the old values of
                // the buffer.
                hipGraphicsRegisterFlagsWriteDiscard));

            // After importing the OpenGL height buffer into HIP, map it into HIP memory so that we can use it.
            HIP_CHECK(hipGraphicsMapResources(1, &this->hip_height_buffer, this->hip_stream));

            // Fetch the device pointer that points to the OpenGL buffer's memory.
            // This function also fetches the size of the buffer. We already know it, but we still need to pass
            // a valid pointer to hipGraphicsResourceGetMappedPointer.
            size_t size;
            HIP_CHECK(
                hipGraphicsResourceGetMappedPointer(reinterpret_cast<void**>(&this->hip_height_ptr),
                                                    &size,
                                                    this->hip_height_buffer));

:

The imported pointer is manipulated in the sinewave kernel as shown in the following example:

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

:
{.highlight-cpp .notranslate}

highlight
            // The tile size to be used for each block of the computation. A tile is
            // tile_size by tile_size threads in this case, since we are invoking the
            // computation over a 2D-grid.
            constexpr size_t tile_size = 8;

            // Launch the HIP kernel to advance the simulation.
            sinewave_kernel<<<dim3(ceiling_div(grid_width, tile_size),
                                   ceiling_div(grid_height, tile_size)),
                              dim3(tile_size, tile_size),
                              0,
                              this->hip_stream>>>(this->hip_height_ptr, time);

            // Check that no errors occured while launching the kernel.
            HIP_CHECK(hipGetLastError());

:

The HIP graphics resource that is imported from the OpenGL buffer and is not needed anymore should be unmapped and unregistered as shown in the following way:

:
{.highlight-cpp .notranslate}

highlight
            HIP_CHECK(hipStreamSynchronize(this->hip_stream));
            HIP_CHECK(hipGraphicsUnmapResources(1, &this->hip_height_buffer, this->hip_stream));
            HIP_CHECK(hipGraphicsUnregisterResource(this->hip_height_buffer));
            HIP_CHECK(hipStreamDestroy(this->hip_stream));

:
:::::::::::
::::::::::::
::::::::::::::::::::::::::

{.bd-sidebar-secondary .bd-toc}
::
{.sidebar-secondary-items .sidebar-secondary__inner}
:
sidebar-secondary-item

{.page-toc .tocsection .onthispage}
Contents

:
::

:::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::
