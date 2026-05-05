---
title: "Initialization &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_runtime_api/initialization.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T06:59:03.656223+00:00
content_hash: "e0af2550a0eadb11"
---

::::::::::::::::::::::::::::
{#main-content .bd-main role="main"}

sbt-scroll-pixel-helper

::::::::::::::::::::::::::
bd-content
:::::::::::::::::::::
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
# Initialization

::
{#print-main-content}
:
{#jb-print-toc}

{}
## Contents

:
::

{#searchbox}

:::::::
{#initialization .section}
[]{#id1}

# Initialization[\#](#initialization "Link to this heading"){.headerlink}

The initialization involves setting up the environment and resources needed for using GPUs. The following steps are covered with the initialization:

- Setting up the HIP runtime

  This includes reading the environment variables set during init, setting up the active or visible devices, loading necessary libraries, setting up internal buffers for memory copies or cooperative launches, initialize the compiler as well as HSA runtime and checks any errors due to lack of resources or no active devices.

- Querying and setting GPUs

  Identifying and querying the available GPU devices on the system.

- Setting up contexts

  Creating contexts for each GPU device, which are essential for managing resources and executing kernels. For further details, check the [[context section]{.std .std-ref}](../hip_porting_guide.html#context-driver-api){.reference .internal}.

:
{#initialize-the-hip-runtime .section}
## Initialize the HIP runtime[\#](#initialize-the-hip-runtime "Link to this heading"){.headerlink}

The HIP runtime is initialized automatically when the first HIP API call is made. However, you can explicitly initialize it using [[`hipInit()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../../reference/hip_runtime_api/modules/initialization_and_version.html#_CPPv47hipInitj "hipInit"){.reference .internal}, to be able to control the timing of the initialization. The manual initialization can be useful to ensure that the GPU is initialized and ready, or to isolate GPU initialization time from other parts of your program.

{.admonition .note}
Note

You can use [[`hipDeviceReset()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../../reference/hip_runtime_api/modules/device_management.html#_CPPv414hipDeviceResetv "hipDeviceReset"){.reference .internal} to delete all streams created, memory allocated, kernels running and events created by the current process. Any new HIP API call initializes the HIP runtime again.

:

::::
{#querying-and-setting-gpus .section}
## Querying and setting GPUs[\#](#querying-and-setting-gpus "Link to this heading"){.headerlink}

If multiple GPUs are available in the system, you can query and select the desired GPU(s) to use based on device properties, such as size of global memory, size shared memory per block, support of cooperative launch and support of managed memory.

::
{#querying-gpus .section}
### Querying GPUs[\#](#querying-gpus "Link to this heading"){.headerlink}

The properties of a GPU can be queried using [[`hipGetDeviceProperties()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../../reference/hip_runtime_api/modules/device_management.html#_CPPv422hipGetDevicePropertiesP15hipDeviceProp_ti "hipGetDeviceProperties"){.reference .internal}, which returns a struct of [`hipDeviceProp_t`{.xref .cpp .cpp-struct .docutils .literal .notranslate}]{.pre}. The properties in the struct can be used to identify a device or give an overview of hardware characteristics, that might make one GPU better suited for the task than others.

The [[`hipGetDeviceCount()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../../reference/hip_runtime_api/modules/device_management.html#_CPPv417hipGetDeviceCountPi "hipGetDeviceCount"){.reference .internal} function returns the number of available GPUs, which can be used to loop over the available GPUs.

Example code of querying GPUs:

:
{.highlight-cpp .notranslate}

highlight
    #include <hip/hip_runtime.h>
    #include <iostream>

    int main()
    {
        int deviceCount;
        if (hipGetDeviceCount(&deviceCount) == hipSuccess)
        {
            for (int i = 0; i < deviceCount; ++i)
            {
                hipDeviceProp_t prop;
                if (hipGetDeviceProperties(&prop, i) == hipSuccess)
                    std::cout << "Device" << i << prop.name << std::endl;
            }
        }

        return 0;
    }

:
::

{#setting-the-gpu .section}
### Setting the GPU[\#](#setting-the-gpu "Link to this heading"){.headerlink}

[[`hipSetDevice()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../../reference/hip_runtime_api/modules/device_management.html#_CPPv412hipSetDevicei "hipSetDevice"){.reference .internal} function select the GPU to be used for subsequent HIP operations. This function performs several key tasks:

- Context Binding

  Binds the current thread to the context of the specified GPU device. This ensures that all subsequent operations are executed on the selected device.

- Resource Allocation

  Prepares the device for resource allocation, such as memory allocation and stream creation.

- Check device availability

  Checks for errors in device selection and returns error if the specified device is not available or not capable of executing HIP operations.

::::
:::::::
:::::::::::::::::::::

{.bd-sidebar-secondary .bd-toc}
::
{.sidebar-secondary-items .sidebar-secondary__inner}
:
sidebar-secondary-item

{.page-toc .tocsection .onthispage}
Contents

:
::

::::::::::::::::::::::::::
::::::::::::::::::::::::::::
