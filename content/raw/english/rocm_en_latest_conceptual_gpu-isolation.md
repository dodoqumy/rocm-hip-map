---
title: "GPU isolation techniques"
source_url: "https://rocm.docs.amd.com/en/latest/conceptual/gpu-isolation.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-03
---

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-content
::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-article-container
:::::::::: {.bd-header-article .d-print-none}
::::::::: {.header-article-items .header-article__inner}
::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}
:::

::: header-article-item
- [](../index.html){.nav-link aria-label="Home"}
- GPU\...
:::
:::::

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons
[]{.fa-solid .fa-list}
:::
::::
:::::
:::::::::
::::::::::

:::::: {#jb-print-docs-body .onlyprint}
# GPU isolation techniques

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [Environment variables](#environment-variables){.reference .internal .nav-link}
  - [[`ROCR_VISIBLE_DEVICES`{.docutils .literal .notranslate}]{.pre}](#rocr-visible-devices){.reference .internal .nav-link}
  - [[`GPU_DEVICE_ORDINAL`{.docutils .literal .notranslate}]{.pre}](#gpu-device-ordinal){.reference .internal .nav-link}
  - [[`HIP_VISIBLE_DEVICES`{.docutils .literal .notranslate}]{.pre}](#hip-visible-devices){.reference .internal .nav-link}
  - [[`CUDA_VISIBLE_DEVICES`{.docutils .literal .notranslate}]{.pre}](#cuda-visible-devices){.reference .internal .nav-link}
  - [[`OMP_DEFAULT_DEVICE`{.docutils .literal .notranslate}]{.pre}](#omp-default-device){.reference .internal .nav-link}
- [Docker](#docker){.reference .internal .nav-link}
- [GPU passthrough to virtual machines](#gpu-passthrough-to-virtual-machines){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

:::::::::::::::::::::::::::::::::::: {#gpu-isolation-techniques .section .tex2jax_ignore .mathjax_ignore}
# GPU isolation techniques[\#](#gpu-isolation-techniques "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 5 min read time
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils style="color:gray;"}
Applies to Linux and Windows
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
:::
:::::::
::::::::
:::::::::
::::::::::
:::::::::::

Restricting the access of applications to a subset of GPUs, aka isolating GPUs allows users to hide GPU resources from programs. The programs by default will only use the "exposed" GPUs ignoring other (hidden) GPUs in the system.

There are multiple ways to achieve isolation of GPUs in the ROCm software stack, differing in which applications they apply to and the security they provide. This page serves as an overview of the techniques.

:::::::::::::::::::::::: {#environment-variables .section}
## Environment variables[\#](#environment-variables "Link to this heading"){.headerlink}

The runtimes in the ROCm software stack read these environment variables to select the exposed or default device to present to applications using them.

Environment variables shouldn't be used for isolating untrusted applications, as an application can reset them before initializing the runtime.

::::::: {#rocr-visible-devices .section}
### [`ROCR_VISIBLE_DEVICES`{.docutils .literal .notranslate}]{.pre}[\#](#rocr-visible-devices "Link to this heading"){.headerlink}

A list of device indices or [UUID]{.abbr title="universally unique identifier"}s that will be exposed to applications.

Runtime : ROCm Software Runtime. Applies to all applications using the user mode ROCm software stack.

:::::: {#id2 .literal-block-wrapper .docutils .container}
::: code-block-caption
[Example to expose the 1. device and a device based on UUID.]{.caption-text}[\#](#id2 "Link to this code"){.headerlink}
:::

:::: {.highlight-shell .notranslate}
::: highlight
    export ROCR_VISIBLE_DEVICES="0,GPU-4b2c1a9f-8d3e-6f7a-b5c9-2e4d8a1f6c3b"
:::
::::
::::::
:::::::

::::::: {#gpu-device-ordinal .section}
### [`GPU_DEVICE_ORDINAL`{.docutils .literal .notranslate}]{.pre}[\#](#gpu-device-ordinal "Link to this heading"){.headerlink}

Devices indices exposed to OpenCL and HIP applications.

Runtime : ROCm Compute Language Runtime ([`ROCclr`{.docutils .literal .notranslate}]{.pre}). Applies to applications and runtimes using the [`ROCclr`{.docutils .literal .notranslate}]{.pre} abstraction layer including HIP and OpenCL applications.

:::::: {#id3 .literal-block-wrapper .docutils .container}
::: code-block-caption
[Example to expose the 1. and 3. device in the system.]{.caption-text}[\#](#id3 "Link to this code"){.headerlink}
:::

:::: {.highlight-shell .notranslate}
::: highlight
    export GPU_DEVICE_ORDINAL="0,2"
:::
::::
::::::
:::::::

::::::: {#hip-visible-devices .section}
[]{#id1}

### [`HIP_VISIBLE_DEVICES`{.docutils .literal .notranslate}]{.pre}[\#](#hip-visible-devices "Link to this heading"){.headerlink}

Device indices exposed to HIP applications.

Runtime: HIP runtime. Applies only to applications using HIP on the AMD platform.

:::::: {#id4 .literal-block-wrapper .docutils .container}
::: code-block-caption
[Example to expose the 1. and 3. devices in the system.]{.caption-text}[\#](#id4 "Link to this code"){.headerlink}
:::

:::: {.highlight-shell .notranslate}
::: highlight
    export HIP_VISIBLE_DEVICES="0,2"
:::
::::
::::::
:::::::

::: {#cuda-visible-devices .section}
### [`CUDA_VISIBLE_DEVICES`{.docutils .literal .notranslate}]{.pre}[\#](#cuda-visible-devices "Link to this heading"){.headerlink}

Provided for CUDA compatibility, has the same effect as [`HIP_VISIBLE_DEVICES`{.docutils .literal .notranslate}]{.pre} on the AMD platform.

Runtime : HIP or CUDA Runtime. Applies to HIP applications on the AMD or NVIDIA platform and CUDA applications.
:::

::::::: {#omp-default-device .section}
### [`OMP_DEFAULT_DEVICE`{.docutils .literal .notranslate}]{.pre}[\#](#omp-default-device "Link to this heading"){.headerlink}

Default device used for OpenMP target offloading.

Runtime : OpenMP Runtime. Applies only to applications using OpenMP offloading.

:::::: {#id5 .literal-block-wrapper .docutils .container}
::: code-block-caption
[Example on setting the default device to the third device.]{.caption-text}[\#](#id5 "Link to this code"){.headerlink}
:::

:::: {.highlight-shell .notranslate}
::: highlight
    export OMP_DEFAULT_DEVICE="2"
:::
::::
::::::
:::::::
::::::::::::::::::::::::

::: {#docker .section}
## Docker[\#](#docker "Link to this heading"){.headerlink}

Docker uses Linux kernel namespaces to provide isolated environments for applications. This isolation applies to most devices by default, including GPUs. To access them in containers explicit access must be granted, please see [Accessing GPUs in containers](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/how-to/docker.html#docker-access-gpus-in-container "(in ROCm installation on Linux v7.2.2)"){.reference .external} for details. Specifically refer to [Restricting GPU access](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/how-to/docker.html#docker-restrict-gpus "(in ROCm installation on Linux v7.2.2)"){.reference .external} on exposing just a subset of all GPUs.

Docker isolation is more secure than environment variables, and applies to all programs that use the [`amdgpu`{.docutils .literal .notranslate}]{.pre} kernel module interfaces. Even programs that don't use the ROCm runtime, like graphics applications using OpenGL or Vulkan, can only access the GPUs exposed to the container.
:::

::: {#gpu-passthrough-to-virtual-machines .section}
## GPU passthrough to virtual machines[\#](#gpu-passthrough-to-virtual-machines "Link to this heading"){.headerlink}

Virtual machines achieve the highest level of isolation, because even the kernel of the virtual machine is isolated from the host. Devices physically installed in the host system can be passed to the virtual machine using PCIe passthrough. This allows for using the GPU with a different operating systems like a Windows guest from a Linux host.

Setting up PCIe passthrough is specific to the hypervisor used. ROCm officially supports [VMware ESXi](https://www.vmware.com/products/esxi-and-esx.html){.reference .external} for select GPUs.
:::
::::::::::::::::::::::::::::::::::::

::::: prev-next-area
[](file-reorg.html "previous page"){.left-prev}

::: prev-next-info
previous

ROCm Linux Filesystem Hierarchy Standard reorganization
:::

[](cmake-packages.html "next page"){.right-next}

::: prev-next-info
next

Using CMake
:::
:::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::: {.bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {.page-toc .tocsection .onthispage}
Contents
:::

- [Environment variables](#environment-variables){.reference .internal .nav-link}
  - [[`ROCR_VISIBLE_DEVICES`{.docutils .literal .notranslate}]{.pre}](#rocr-visible-devices){.reference .internal .nav-link}
  - [[`GPU_DEVICE_ORDINAL`{.docutils .literal .notranslate}]{.pre}](#gpu-device-ordinal){.reference .internal .nav-link}
  - [[`HIP_VISIBLE_DEVICES`{.docutils .literal .notranslate}]{.pre}](#hip-visible-devices){.reference .internal .nav-link}
  - [[`CUDA_VISIBLE_DEVICES`{.docutils .literal .notranslate}]{.pre}](#cuda-visible-devices){.reference .internal .nav-link}
  - [[`OMP_DEFAULT_DEVICE`{.docutils .literal .notranslate}]{.pre}](#omp-default-device){.reference .internal .nav-link}
- [Docker](#docker){.reference .internal .nav-link}
- [GPU passthrough to virtual machines](#gpu-passthrough-to-virtual-machines){.reference .internal .nav-link}
::::
:::::
::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
