---
title: "HIP documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/index.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-04-28
---

:::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons

# HIP documentation

# HIP documentation[\#](#hip-documentation "Link to this heading"){.headerlink}

HIP is a C++ runtime API and kernel programming language designed for AMD GPUs. By providing an interface closely aligned with NVIDIA CUDA, HIP allows developers to write portable applications and efficiently migrate existing CUDA code to AMD platforms. Additional information is available in [[What is HIP?]{.doc .std .std-doc}](what_is_hip.html){.reference .internal}

Developers who require a unified, book‑style reference for ROCm and HIP can consult the AMD ROCm Programming Guide. It aggregates documentation from the ROCm portal and organizes it into a structured format optimized for in‑depth study and offline access in both PDF and HTML. Additional details are available in the [AMD ROCm Programming Guide](https://rocm-handbook.amd.com/projects/amd-rocm-programming-guide/en/latest/){.reference .external}.

Note

HIP API 7.0 introduces changes to make it align more closely with NVIDIA CUDA. These changes are incompatible with prior releases, and might require recompiling existing HIP applications for use with the ROCm 7.0 release. For more information, see [[HIP API 7.0 changes]{.doc .std .std-doc}](hip-7-changes.html){.reference .internal}.

Installation instructions are available from:

- [[Installing HIP]{.doc .std .std-doc}](install/install.html){.reference .internal}

- [[Building HIP from source]{.doc .std .std-doc}](install/build.html){.reference .internal}

The HIP documentation is organized into the following categories:

Programming guide

- [[Introduction to the HIP programming model]{.doc}](understand/programming_model.html){.reference .internal}

- [[Understanding GPU performance]{.doc}](understand/performance_optimization.html){.reference .internal}

- [[Hardware implementation]{.doc}](understand/hardware_implementation.html){.reference .internal}

- [[HIP compilers]{.doc}](understand/compilers.html){.reference .internal}

- [[Performance guidelines]{.doc}](how-to/performance_guidelines.html){.reference .internal}

- [[Debugging with HIP]{.doc .std .std-doc}](how-to/debugging.html){.reference .internal}

- [[Logging HIP activity]{.doc}](how-to/logging.html){.reference .internal}

- [[Using HIP runtime API]{.doc}](how-to/hip_runtime_api.html){.reference .internal}

- [[HIP C++ language extensions]{.doc}](how-to/hip_cpp_language_extensions.html){.reference .internal}

- [[Kernel language C++ support]{.doc}](how-to/kernel_language_cpp_support.html){.reference .internal}

- [[Porting CUDA code to HIP]{.doc}](how-to/hip_porting_guide.html){.reference .internal}

- [[Programming for HIP runtime compiler (RTC)]{.doc}](how-to/hip_rtc.html){.reference .internal}

- [[AMD compute language runtimes (CLR)]{.doc}](understand/amd_clr.html){.reference .internal}

Reference

- [[HIP runtime API]{.doc .std .std-doc}](reference/hip_runtime_api_reference.html){.reference .internal}

- [[HIP math API]{.doc .std .std-doc}](reference/math_api.html){.reference .internal}

- [[HIP complex math API]{.doc .std .std-doc}](reference/complex_math_api.html){.reference .internal}

- [[HIP environment variables]{.doc .std .std-doc}](reference/env_variables.html){.reference .internal}

- [[HIP error codes]{.doc .std .std-doc}](reference/error_codes.html){.reference .internal}

- [[NVIDIA CUDA to HIP API Function Comparison]{.doc .std .std-doc}](reference/api_syntax.html){.reference .internal}

- [[List of deprecated APIs]{.doc .std .std-doc}](reference/deprecated_api_list.html){.reference .internal}

- [[Low Precision Floating Point Types]{.doc .std .std-doc}](reference/low_fp_types.html){.reference .internal}

- [[Hardware features]{.doc}](reference/hardware_features.html){.reference .internal}

Tutorial

- [HIP basic examples](https://github.com/ROCm/rocm-examples/tree/develop/HIP-Basic){.reference .external}

- [HIP examples](https://github.com/ROCm/rocm-examples){.reference .external}

- [[SAXPY tutorial]{.doc .std .std-doc}](tutorial/saxpy.html){.reference .internal}

- [[GPU programming patterns]{.doc .std .std-doc}](tutorial/programming-patterns.html){.reference .internal}

- [[Reduction tutorial]{.doc .std .std-doc}](tutorial/reduction.html){.reference .internal}

- [[Cooperative groups tutorial]{.doc .std .std-doc}](tutorial/cooperative_groups_tutorial.html){.reference .internal}

- [[HIP Graph API tutorial]{.doc .std .std-doc}](tutorial/graph_api.html){.reference .internal}

Known issues are listed on the [HIP GitHub repository](https://github.com/ROCm/HIP/issues){.reference .external}.

To contribute features or functions to the HIP project, refer to [Contributing to HIP](https://github.com/ROCm/HIP/blob/develop/CONTRIBUTING.md){.reference .external}. To contribute to the documentation, refer to [[Contributing to ROCm docs]{.xref .std .std-doc}](https://rocm.docs.amd.com/en/latest/contribute/contributing.html "(in ROCm Documentation v7.2.2)"){.reference .external} page.

You can find licensing information on the [Licensing](https://rocm.docs.amd.com/en/latest/about/license.html){.reference .external} page.

:::: prev-next-area
[](what_is_hip.html "next page"){.right-next}

::: prev-next-info
next

What is HIP?