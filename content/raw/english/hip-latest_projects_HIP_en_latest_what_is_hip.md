---
title: "What is HIP? &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/what_is_hip.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T06:58:41.401852+00:00
content_hash: "0c538f80f7fb6a3b"
---

::::::::::::::::::::::::
{#main-content .bd-main role="main"}

sbt-scroll-pixel-helper

::::::::::::::::::::::
bd-content
:::::::::::::::::
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
# What is HIP?

::
{#print-main-content}
:
{#jb-print-toc}

{}
## Contents

:
::

{#searchbox}

{#what-is-hip .section}
[]{#intro-to-hip}

# What is HIP?[\#](#what-is-hip "Link to this heading"){.headerlink}

HIP is a C++ runtime API and kernel language for AMD GPUs. It is part of AMD's ROCm platform and lets developers create applications that run on heterogeneous systems, using CPUs and AMD GPUs from a single source code base.

<figure class="align-center">
<img src="_images/hip.svg" alt="HIP in an application." />
</figure>

- HIP is a thin API with little or no performance impact over coding directly in AMD [[ROCm]{.xref .std .std-doc}](https://rocm.docs.amd.com/en/latest/what-is-rocm.html "(in ROCm Documentation v7.2.2)"){.reference .external}.

- HIP enables coding in a single-source C++ programming language, including features such as templates, C++11 lambdas, classes, namespaces, and more.

- Developers can tune for performance or handle tricky cases via HIP.

ROCm offers compilers ([`clang`{.docutils .literal .notranslate}]{.pre}, [`hipcc`{.docutils .literal .notranslate}]{.pre}), code profilers ([`rocprofv3`{.docutils .literal .notranslate}]{.pre}), debugging tools ([`rocgdb`{.docutils .literal .notranslate}]{.pre}), libraries and HIP with the runtime API and kernel language, to create heterogeneous applications running on both CPUs and GPUs. ROCm provides libraries like [[hipFFT]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/hipFFT/en/latest/index.html "(in hipFFT Documentation v1.0.22)"){.reference .external} and [[hipBLAS]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/hipBLAS/en/latest/index.html "(in hipBLAS Documentation v3.2.0)"){.reference .external} that provide API compatibility with equivalent NVIDIA CUDA libraries, making it easier to port existing NVIDIA CUDA applications. These libraries provide pointer-based memory interfaces and can be easily integrated into your applications.

GPU programmers with NVIDIA CUDA experience will find the HIP API straightforward. You can quickly port NVIDIA CUDA applications to run on AMD GPUs. The [[HIPify]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/HIPIFY/en/latest/index.html "(in HIPIFY Documentation)"){.reference .external} tools, based on the clang front-end and Perl language, can convert NVIDIA CUDA API calls into the corresponding HIP API calls. However, HIP is not intended to be a drop-in replacement for NVIDIA CUDA, and developers should expect to do some manual coding and performance tuning work to port existing projects to AMD GPUs as described in the [[HIP porting guide]{.doc}](how-to/hip_porting_guide.html){.reference .internal}.

HIP provides two components: those that run on the CPU, also known as host system, and those that run on GPUs, also referred to as device. The host-based code is used to create device buffers, move data between the host application and a device, launch the device code (also known as kernel), manage streams and events, and perform synchronization. The kernel language provides a way to develop massively parallel programs that run on GPUs, and provides access to GPU specific hardware capabilities.

In summary, HIP simplifies porting NVIDIA CUDA applications to AMD GPUs, maintains performance, and provides a familiar C++ experience for GPU programming.

::
{#hip-components .section}
## HIP components[\#](#hip-components "Link to this heading"){.headerlink}

HIP consists of the following components. For information on the license associated with each component, see [[HIP licensing]{.doc}](license.html){.reference .internal}.

{#c-runtime-api .section}
### C++ runtime API[\#](#c-runtime-api "Link to this heading"){.headerlink}

HIP provides headers and a runtime library built on top of HIP-Clang compiler in the repository [[Compute Language Runtime (CLR)]{.doc}](understand/amd_clr.html){.reference .internal}. The HIP runtime implements HIP streams, events, and memory APIs, and is an object library that is linked with the application. The source code for all headers and the library implementation is available on GitHub.

For further details, check [[HIP Runtime API Reference]{.std .std-ref}](reference/hip_runtime_api_reference.html#runtime-api-reference){.reference .internal}.

{#kernel-language .section}
### Kernel language[\#](#kernel-language "Link to this heading"){.headerlink}

HIP provides a C++ syntax that is suitable for compiling most code that commonly appears in compute kernels (classes, namespaces, operator overloading, and templates). HIP also defines other language features that are designed to target accelerators, such as:

- Short-vector headers that can serve on a host or device

- Math functions that resemble those in [`math.h`{.docutils .literal .notranslate}]{.pre}, which is included with standard C++ compilers

- Built-in functions for accessing specific GPU hardware capabilities

For further details, check [[HIP C++ language extensions]{.doc}](how-to/hip_cpp_language_extensions.html){.reference .internal} and [[Kernel language C++ support]{.doc}](how-to/kernel_language_cpp_support.html){.reference .internal}.

::

:::::::::::::::::

{.bd-sidebar-secondary .bd-toc}
::
{.sidebar-secondary-items .sidebar-secondary__inner}
:
sidebar-secondary-item

{.page-toc .tocsection .onthispage}
Contents

:
::

::::::::::::::::::::::
::::::::::::::::::::::::
