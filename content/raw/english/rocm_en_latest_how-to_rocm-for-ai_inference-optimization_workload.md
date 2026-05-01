---
title: "AMD Instinct MI300X workload optimization"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference-optimization/workload.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-01
---

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-content
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-article-container
:::::::::: {.bd-header-article .d-print-none}
::::::::: {.header-article-items .header-article__inner}
::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}
:::

::: header-article-item
- [](../../../index.html){.nav-link aria-label="Home"}
- [Use ROCm for AI](../index.html){.nav-link}
- [Use ROCm for AI inference optimization](index.html){.nav-link}
- AMD\...
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
# AMD Instinct MI300X workload optimization

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [Workload tuning strategy](#workload-tuning-strategy){.reference .internal .nav-link}
  - [Measure the current workload](#measure-the-current-workload){.reference .internal .nav-link}
  - [Identify tuning requirements](#mi300x-profiling-start){.reference .internal .nav-link}
    - [High-level profiling tools](#high-level-profiling-tools){.reference .internal .nav-link}
    - [Kernel-level profiling tools](#kernel-level-profiling-tools){.reference .internal .nav-link}
  - [Analyze and tune](#analyze-and-tune){.reference .internal .nav-link}
    - [Optimize model inference with vLLM](#optimize-model-inference-with-vllm){.reference .internal .nav-link}
    - [Auto-tunable configurations](#auto-tunable-configurations){.reference .internal .nav-link}
    - [Manual tuning](#manual-tuning){.reference .internal .nav-link}
  - [Iterate and validate](#iterate-and-validate){.reference .internal .nav-link}
- [Profiling tools](#profiling-tools){.reference .internal .nav-link}
  - [PyTorch Profiler](#pytorch-profiler){.reference .internal .nav-link}
  - [ROCm profiling tools](#rocm-profiling-tools){.reference .internal .nav-link}
    - [ROCProfiler](#rocprofiler){.reference .internal .nav-link}
    - [ROCm Compute Profiler](#rocm-compute-profiler){.reference .internal .nav-link}
    - [ROCm Systems Profiler](#rocm-systems-profiler){.reference .internal .nav-link}
- [vLLM performance optimization](#vllm-performance-optimization){.reference .internal .nav-link}
- [PyTorch TunableOp](#pytorch-tunableop){.reference .internal .nav-link}
  - [Workflow](#workflow){.reference .internal .nav-link}
  - [Offline tuning](#offline-tuning){.reference .internal .nav-link}
- [PyTorch inductor max-autotune tuning knobs](#pytorch-inductor-max-autotune-tuning-knobs){.reference .internal .nav-link}
  - [Triton backend](#triton-backend){.reference .internal .nav-link}
  - [Composable Kernel backend](#composable-kernel-backend){.reference .internal .nav-link}
- [ROCm library tuning](#rocm-library-tuning){.reference .internal .nav-link}
  - [GEMM (general matrix multiplication)](#gemm-general-matrix-multiplication){.reference .internal .nav-link}
    - [hipBLASLt benchmarking](#hipblaslt-benchmarking){.reference .internal .nav-link}
    - [hipBLASLt auto-tuning using hipblaslt-bench](#hipblaslt-auto-tuning-using-hipblaslt-bench){.reference .internal .nav-link}
      - [Prerequisite](#prerequisite){.reference .internal .nav-link}
      - [Quick start](#quick-start){.reference .internal .nav-link}
      - [Output](#output){.reference .internal .nav-link}
      - [A quick view of the config YAML](#a-quick-view-of-the-config-yaml){.reference .internal .nav-link}
    - [hipBLASLt backend assembly generator tuning](#hipblaslt-backend-assembly-generator-tuning){.reference .internal .nav-link}
      - [config.yaml](#config-yaml){.reference .internal .nav-link}
  - [TensileLite tuning flow](#tensilelite-tuning-flow){.reference .internal .nav-link}
    - [Step 1: Initial solution parameters](#step-1-initial-solution-parameters){.reference .internal .nav-link}
    - [Step 2: Benchmark common parameters](#step-2-benchmark-common-parameters){.reference .internal .nav-link}
    - [Step 3: Fork parameters](#step-3-fork-parameters){.reference .internal .nav-link}
    - [Step 4: Benchmark fork parameters](#step-4-benchmark-fork-parameters){.reference .internal .nav-link}
    - [Step 5: Join parameters](#step-5-join-parameters){.reference .internal .nav-link}
    - [Step 6: Benchmark join parameters](#step-6-benchmark-join-parameters){.reference .internal .nav-link}
    - [Step 7: Benchmark final parameters](#step-7-benchmark-final-parameters){.reference .internal .nav-link}
  - [Update logic YAML files](#update-logic-yaml-files){.reference .internal .nav-link}
    - [Tensile optimization and performance tuning tips](#tensile-optimization-and-performance-tuning-tips){.reference .internal .nav-link}
    - [Optimizing Composable Kernel GEMM kernels](#optimizing-composable-kernel-gemm-kernels){.reference .internal .nav-link}
  - [MIOpen](#miopen){.reference .internal .nav-link}
    - [Convolution](#convolution){.reference .internal .nav-link}
    - [Tuning in MIOpen](#tuning-in-miopen){.reference .internal .nav-link}
    - [Finding the fastest kernel](#finding-the-fastest-kernel){.reference .internal .nav-link}
  - [RCCL](#rccl){.reference .internal .nav-link}
    - [Use all eight GPUs](#use-all-eight-gpus){.reference .internal .nav-link}
    - [Disable NUMA auto-balancing](#disable-numa-auto-balancing){.reference .internal .nav-link}
    - [Disable ACS for multi-node RCCL](#disable-acs-for-multi-node-rccl){.reference .internal .nav-link}
    - [Run RCCL-Unittests](#run-rccl-unittests){.reference .internal .nav-link}
    - [NPKit profiler](#npkit-profiler){.reference .internal .nav-link}
    - [RCCL-tests](#rccl-tests){.reference .internal .nav-link}
    - [Use one-process-per-GPU mode](#use-one-process-per-gpu-mode){.reference .internal .nav-link}
    - [RCCL in E2E workloads](#rccl-in-e2e-workloads){.reference .internal .nav-link}
- [Triton kernel performance optimization](#triton-kernel-performance-optimization){.reference .internal .nav-link}
  - [Auto-tunable kernel configurations](#auto-tunable-kernel-configurations){.reference .internal .nav-link}
  - [Overall GPU resource utilization](#overall-gpu-resource-utilization){.reference .internal .nav-link}
  - [MLIR analysis](#mlir-analysis){.reference .internal .nav-link}
  - [ISA assembly analysis](#isa-assembly-analysis){.reference .internal .nav-link}
- [HIP performance optimization](#hip-performance-optimization){.reference .internal .nav-link}
  - [Parallel execution and GPU hardware utilization](#parallel-execution-and-gpu-hardware-utilization){.reference .internal .nav-link}
  - [Memory usage optimization](#memory-usage-optimization){.reference .internal .nav-link}
- [Diagnostic and performance analysis](#diagnostic-and-performance-analysis){.reference .internal .nav-link}
  - [Debug memory access faults](#debug-memory-access-faults){.reference .internal .nav-link}
  - [Compute the occupancy of a kernel](#compute-the-occupancy-of-a-kernel){.reference .internal .nav-link}
- [Special considerations](#special-considerations){.reference .internal .nav-link}
  - [Multi-GPU communications](#multi-gpu-communications){.reference .internal .nav-link}
  - [Multi-node FSDP and RCCL settings](#multi-node-fsdp-and-rccl-settings){.reference .internal .nav-link}
- [Further reading](#further-reading){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#amd-instinct-mi300x-workload-optimization .section}
# AMD Instinct MI300X workload optimization[\#](#amd-instinct-mi300x-workload-optimization "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 48 min read time
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils style="color:gray;"}
Applies to Linux
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
:::
:::::::
::::::::
:::::::::
::::::::::
:::::::::::

This document provides guidelines for optimizing the performance of AMD Instinct™ MI300X GPUs, with a particular focus on GPU kernel programming, high-performance computing (HPC), and deep learning operations using PyTorch. It delves into specific workloads such as [[model inference]{.std .std-ref}](vllm-optimization.html#mi300x-vllm-optimization){.reference .internal}, offering strategies to enhance efficiency.

The following topics highlight [[auto-tunable configurations]{.std .std-ref}](#mi300x-auto-tune){.reference .internal} as well as [[Triton kernel optimization]{.std .std-ref}](#mi300x-triton-kernel-performance-optimization){.reference .internal} for meticulous tuning.

::::::::::::: {#workload-tuning-strategy .section}
## Workload tuning strategy[\#](#workload-tuning-strategy "Link to this heading"){.headerlink}

By following a structured approach, you can systematically address performance issues and enhance the efficiency of your workloads on AMD Instinct MI300X GPUs.

::: {#measure-the-current-workload .section}
### Measure the current workload[\#](#measure-the-current-workload "Link to this heading"){.headerlink}

Begin by evaluating the performance of your workload in its current state. This involves running benchmarks and collecting performance data to establish a baseline. Understanding how your workload behaves under different conditions provides critical insights into where improvements are needed.
:::

::::: {#mi300x-profiling-start .section}
[]{#identify-tuning-requirements}

### Identify tuning requirements[\#](#mi300x-profiling-start "Link to this heading"){.headerlink}

Analyze the collected performance data to identify areas where tuning is required. This could involve detecting bottlenecks in CPU, GPU, memory, or data transfer. Understanding these requirements will help direct your optimization efforts more effectively.

Profiling is a fundamental step in workload tuning. It allows you to gather detailed information about how your workload utilizes system resources, and where potential inefficiencies lie. Profiling tools can provide insights into both high-level and granular performance metrics. See [[Profiling tools]{.std .std-ref}](#mi300x-profiling-tools){.reference .internal}.

::: {#high-level-profiling-tools .section}
#### High-level profiling tools[\#](#high-level-profiling-tools "Link to this heading"){.headerlink}

For a broad overview, use tools like the [[PyTorch Profiler]{.std .std-ref}](#mi300x-pytorch-profiler){.reference .internal}, which helps in understanding how PyTorch operations are executed and where time is spent. This is particularly useful for developers new to workload tuning, as it provides a comprehensive view without requiring in-depth knowledge of lower-level operations.
:::

::: {#kernel-level-profiling-tools .section}
#### Kernel-level profiling tools[\#](#kernel-level-profiling-tools "Link to this heading"){.headerlink}

When profiling indicates that GPUs are a performance bottleneck, delve deeper into kernel-level profiling. Tools such as the [[ROCr Debug Agent]{.std .std-ref}](#mi300x-rocr-debug-agent){.reference .internal}, [[ROCProfiler]{.std .std-ref}](#mi300x-rocprof){.reference .internal}, and [[ROCm Compute Profiler]{.std .std-ref}](#mi300x-rocprof-compute){.reference .internal} offer detailed insights into GPU kernel execution. These tools can help isolate problematic GPU operations and provide data needed for targeted optimizations.
:::
:::::

::::::: {#analyze-and-tune .section}
### Analyze and tune[\#](#analyze-and-tune "Link to this heading"){.headerlink}

Based on the insights gained from profiling, focus your tuning efforts on the identified bottlenecks. This might involve optimizing specific kernel operations, adjusting memory access patterns, or modifying computational algorithms.

The following subsections discuss optimization ranging from high-level and more automated strategies to more involved, hands-on optimization.

:::: {#optimize-model-inference-with-vllm .section}
#### Optimize model inference with vLLM[\#](#optimize-model-inference-with-vllm "Link to this heading"){.headerlink}

vLLM provides tools and techniques specifically designed for efficient model inference on AMD Instinct GPUs. See the official [vLLM installation docs](https://docs.vllm.ai/en/latest/getting_started/installation/gpu.html){.reference .external} for installation guidance. Optimizing performance with vLLM involves configuring tensor parallelism, leveraging advanced features, and ensuring efficient execution.

- Configuration for vLLM: Set engine arguments according to workload requirements.

- Benchmarking and performance metrics: Measure latency and throughput to evaluate performance.

::: {.admonition .seealso}
See also

See [[vLLM V1 performance optimization]{.doc}](vllm-optimization.html){.reference .internal} to learn more about vLLM performance optimization techniques.
:::
::::

::: {#auto-tunable-configurations .section}
[]{#mi300x-auto-tune}

#### Auto-tunable configurations[\#](#auto-tunable-configurations "Link to this heading"){.headerlink}

Auto-tunable configurations can significantly streamline performance optimization by automatically adjusting parameters based on workload characteristics. For example:

- PyTorch: Utilize [[PyTorch's built-in auto-tuning features]{.std .std-ref}](#mi300x-torchinductor-tuning){.reference .internal}, such as the [[TunableOp]{.std .std-ref}](#mi300x-tunableop){.reference .internal} module, which helps in optimizing operation performance by exploring different configurations.

- MIOpen: Leverage [[MIOpen's auto-tuning capabilities]{.std .std-ref}](#mi300x-miopen-tuning){.reference .internal} for convolutional operations and other primitives to find optimal settings for your specific hardware.

- Triton: Use [[Triton's auto-tuning features]{.std .std-ref}](#mi300x-autotunable-kernel-config){.reference .internal} to explore various kernel configurations and select the best-performing ones.
:::

::: {#manual-tuning .section}
#### Manual tuning[\#](#manual-tuning "Link to this heading"){.headerlink}

Advanced developers can manually adjust parameters and configurations to optimize performance. Both Triton and HIP involve manual tuning aspects.

- ROCm libraries: Optimize GPU performance by adjusting various parameters and configurations within [[ROCm libraries]{.std .std-ref}](#mi300x-rocm-library-tuning){.reference .internal}. This approach involves hands-on optimization to maximize efficiency for specific workloads.

- Triton: Tune Triton kernels by adjusting parameters tailored to your workload to [[optimize GPU resource utilization]{.std .std-ref}](#mi300x-triton-gpu-utilization){.reference .internal} and better [[leverage specific hardware features]{.std .std-ref}](#mi300x-assembly-analysis){.reference .internal}.

- HIP: Profile and [[optimize HIP kernels]{.std .std-ref}](#mi300x-hip-optimization){.reference .internal} by optimizing parallel execution, memory access patterns, and other aspects.
:::
:::::::

::: {#iterate-and-validate .section}
### Iterate and validate[\#](#iterate-and-validate "Link to this heading"){.headerlink}

Optimization is an iterative process. After applying tuning changes, re-profile the workload to validate improvements and ensure that the changes have had the desired effect. Continuous iteration helps refine the performance gains and address any new bottlenecks that may emerge.

ROCm provides a prebuilt optimized Docker image that has everything required to implement the LLM inference tips in this section. It includes ROCm, PyTorch, and vLLM. For more information, see [[vLLM inference]{.doc}](../inference/benchmark-docker/vllm.html){.reference .internal}.
:::
:::::::::::::

::::::::::: {#profiling-tools .section}
[]{#mi300x-profiling-tools}

## Profiling tools[\#](#profiling-tools "Link to this heading"){.headerlink}

AMD profiling tools provide valuable insights into how efficiently your application utilizes hardware and help diagnose potential bottlenecks that contribute to poor performance. Developers targeting AMD GPUs have multiple tools available depending on their specific profiling needs.

- ROCProfiler tool collects kernel execution performance metrics. For more information, see the [[ROCProfiler]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocprofiler/en/latest/index.html "(in rocprofiler Documentation v2.0.0)"){.reference .external} documentation.

- ROCm Compute Profiler builds upon ROCProfiler but provides more guided analysis. For more information, see [[ROCm Compute Profiler documentation]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocprofiler-compute/en/latest/index.html "(in ROCm Compute Profiler v3.4.0)"){.reference .external}.

Refer to [[Profiling and debugging]{.doc}](profiling-and-debugging.html){.reference .internal} to explore commonly used profiling tools and their usage patterns.

Once performance bottlenecks are identified, you can implement an informed workload tuning strategy. If kernels are the bottleneck, consider:

- [[Auto-tuning in PyTorch with TunableOp]{.std .std-ref}](#mi300x-tunableop){.reference .internal}

- [[Auto-tuning in MIOpen]{.std .std-ref}](#mi300x-miopen-tuning){.reference .internal}

- [[Triton auto-tunable kernel configurations]{.std .std-ref}](#mi300x-autotunable-kernel-config){.reference .internal}

If auto-tuning does not meet your requirements, consider [[Triton kernel performance optimization]{.std .std-ref}](#mi300x-triton-kernel-performance-optimization){.reference .internal}.

If the issue is multi-GPU scale-out, try [[RCCL tuning and configuration]{.std .std-ref}](#mi300x-rccl){.reference .internal}.

This section discusses profiling and debugging tools and some of their common usage patterns with ROCm applications.

::: {#pytorch-profiler .section}
[]{#mi300x-pytorch-profiler}

### PyTorch Profiler[\#](#pytorch-profiler "Link to this heading"){.headerlink}

[PyTorch Profiler](https://pytorch.org/docs/stable/profiler.html){.reference .external} can be invoked inside Python scripts, letting you collect CPU and GPU performance metrics while the script is running. See the [PyTorch Profiler tutorial](https://pytorch.org/tutorials/recipes/recipes/profiler_recipe.html){.reference .external} for more information.

You can then visualize and view these metrics using an open-source profile visualization tool like [Perfetto UI](https://ui.perfetto.dev){.reference .external}.

1.  Use the following snippet to invoke PyTorch Profiler in your code.

    :::: {.highlight-python .notranslate}
    ::: highlight
        import torch
        import torchvision.models as models
        from torch.profiler import profile, record_function, ProfilerActivity
        model = models.resnet18().cuda()
        inputs = torch.randn(2000, 3, 224, 224).cuda()

        with profile(activities=[ProfilerActivity.CPU, ProfilerActivity.CUDA]) as prof:
            with record_function("model_inference"):
                model(inputs)
        prof.export_chrome_trace("resnet18_profile.json")
    :::
    ::::

2.  Profile results in [`resnet18_profile.json`{.docutils .literal .notranslate}]{.pre} can be viewed by the Perfetto visualization tool. Go to [https://ui.perfetto.dev](https://ui.perfetto.dev){.reference .external} and import the file. In your Perfetto visualization, you'll see that the upper section shows transactions denoting the CPU activities that launch GPU kernels while the lower section shows the actual GPU activities where it processes the [`resnet18`{.docutils .literal .notranslate}]{.pre} inferences layer by layer.

    <figure id="id2" class="align-default">
    <a href="../../../_images/perfetto-trace.svg" class="reference internal image-reference"><img src="../../../_images/perfetto-trace.svg" style="width: 800px;" alt="../../../_images/perfetto-trace.svg" /></a>
    <figcaption><p><span class="caption-text">Perfetto trace visualization example.</span><a href="#id2" class="headerlink" title="Link to this image">#</a></p></figcaption>
    </figure>
:::

::::::::: {#rocm-profiling-tools .section}
### ROCm profiling tools[\#](#rocm-profiling-tools "Link to this heading"){.headerlink}

Heterogenous systems, where programs run on both CPUs and GPUs, introduce additional complexities. Understanding the critical path and kernel execution is all the more important. So, performance tuning is a necessary component in the benchmarking process.

With AMD's profiling tools, developers are able to gain important insight into how efficiently their application is using hardware resources and effectively diagnose potential bottlenecks contributing to poor performance. Developers working with AMD Instinct GPUs have multiple tools depending on their specific profiling needs; these include:

- [[ROCProfiler]{.std .std-ref}](#mi300x-rocprof){.reference .internal}

- [[ROCm Compute Profiler]{.std .std-ref}](#mi300x-rocprof-compute){.reference .internal}

- [[ROCm Systems Profiler]{.std .std-ref}](#mi300x-rocprof-systems){.reference .internal}

:::: {#rocprofiler .section}
[]{#mi300x-rocprof}

#### ROCProfiler[\#](#rocprofiler "Link to this heading"){.headerlink}

[[ROCProfiler]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocprofiler/en/latest/index.html "(in rocprofiler Documentation v2.0.0)"){.reference .external} is primarily a low-level API for accessing and extracting GPU hardware performance metrics, commonly called *performance counters*. These counters quantify the performance of the underlying architecture showcasing which pieces of the computational pipeline and memory hierarchy are being utilized.

Your ROCm installation contains a script or executable command called [`rocprof`{.docutils .literal .notranslate}]{.pre} which provides the ability to list all available hardware counters for your specific GPU, and run applications while collecting counters during their execution.

This [`rocprof`{.docutils .literal .notranslate}]{.pre} utility also depends on the [[ROCTracer and ROC-TX libraries]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/roctracer/en/latest/index.html "(in ROCTracer Documentation v4.1.0)"){.reference .external}, giving it the ability to collect timeline traces of the GPU software stack as well as user-annotated code regions.

::: {.admonition .note}
Note

[`rocprof`{.docutils .literal .notranslate}]{.pre} is a CLI-only utility where inputs and outputs take the form of text and CSV files. These formats provide a raw view of the data and puts the onus on the user to parse and analyze. [`rocprof`{.docutils .literal .notranslate}]{.pre} gives the user full access and control of raw performance profiling data, but requires extra effort to analyze the collected data.
:::
::::

:::: {#rocm-compute-profiler .section}
[]{#mi300x-rocprof-compute}

#### ROCm Compute Profiler[\#](#rocm-compute-profiler "Link to this heading"){.headerlink}

[[ROCm Compute Profiler]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocprofiler-compute/en/latest/index.html "(in ROCm Compute Profiler v3.4.0)"){.reference .external} is a system performance profiler for high-performance computing (HPC) and machine learning (ML) workloads using Instinct GPUs. Under the hood, ROCm Compute Profiler uses [[ROCProfiler]{.std .std-ref}](#mi300x-rocprof){.reference .internal} to collect hardware performance counters. The ROCm Compute Profiler tool performs system profiling based on all approved hardware counters for Instinct GPU architectures. It provides high level performance analysis features including System Speed-of-Light, IP block Speed-of-Light, Memory Chart Analysis, Roofline Analysis, Baseline Comparisons, and more.

ROCm Compute Profiler takes the guesswork out of profiling by removing the need to provide text input files with lists of counters to collect and analyze raw CSV output files as is the case with ROCProfiler. Instead, ROCm Compute Profiler automates the collection of all available hardware counters in one command and provides graphical interfaces to help users understand and analyze bottlenecks and stressors for their computational workloads on AMD Instinct GPUs.

::: {.admonition .note}
Note

ROCm Compute Profiler collects hardware counters in multiple passes, and will therefore re-run the application during each pass to collect different sets of metrics.
:::

<figure id="id3" class="align-default">
<a href="../../../_images/rocprof-compute-analysis.png" class="reference internal image-reference"><img src="../../../_images/rocprof-compute-analysis.png" style="width: 800px;" alt="../../../_images/rocprof-compute-analysis.png" /></a>
<figcaption><p><span class="caption-text">ROCm Compute Profiler memory chart analysis panel.</span><a href="#id3" class="headerlink" title="Link to this image">#</a></p></figcaption>
</figure>

In brief, ROCm Compute Profiler provides details about hardware activity for a particular GPU kernel. It also supports both a web-based GUI or command-line analyzer, depending on your preference.
::::

:::: {#rocm-systems-profiler .section}
[]{#mi300x-rocprof-systems}

#### ROCm Systems Profiler[\#](#rocm-systems-profiler "Link to this heading"){.headerlink}

[[ROCm Systems Profiler]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocprofiler-systems/en/latest/index.html "(in rocprofiler-systems v1.3.0)"){.reference .external} is a comprehensive profiling and tracing tool for parallel applications, including HPC and ML packages, written in C, C++, Fortran, HIP, OpenCL, and Python which execute on the CPU or CPU and GPU. It is capable of gathering the performance information of functions through any combination of binary instrumentation, call-stack sampling, user-defined regions, and Python interpreter hooks.

ROCm Systems Profiler supports interactive visualization of comprehensive traces in the web browser in addition to high-level summary profiles with [`mean/min/max/stddev`{.docutils .literal .notranslate}]{.pre} statistics. Beyond runtime information, ROCm Systems Profiler supports the collection of system-level metrics such as CPU frequency, GPU temperature, and GPU utilization. Process and thread level metrics such as memory usage, page faults, context switches, and numerous other hardware counters are also included.

::: {.admonition .tip}
Tip

When analyzing the performance of an application, it is best not to assume you know where the performance bottlenecks are and why they are happening. ROCm Systems Profiler is the ideal tool for characterizing where optimization would have the greatest impact on the end-to-end execution of the application and to discover what else is happening on the system during a performance bottleneck.
:::

<figure id="id4" class="align-default">
<a href="../../../_images/rocprof-systems-timeline.png" class="reference internal image-reference"><img src="../../../_images/rocprof-systems-timeline.png" style="width: 800px;" alt="../../../_images/rocprof-systems-timeline.png" /></a>
<figcaption><p><span class="caption-text">ROCm Systems Profiler timeline trace example.</span><a href="#id4" class="headerlink" title="Link to this image">#</a></p></figcaption>
</figure>
::::
:::::::::
:::::::::::

::: {#vllm-performance-optimization .section}
## vLLM performance optimization[\#](#vllm-performance-optimization "Link to this heading"){.headerlink}

vLLM is a high-throughput and memory efficient inference and serving engine for large language models that has gained traction in the AI community for its performance and ease of use. See [[vLLM V1 performance optimization]{.doc}](vllm-optimization.html){.reference .internal}, where you'll learn how to:

- Enable AITER (AI Tensor Engine for ROCm) to speed up on LLM models.

- Configure environment variables for optimal HIP, RCCL, and Quick Reduce performance.

- Select the right attention backend for your workload (AITER MHA/MLA vs. Triton).

- Choose parallelism strategies (tensor, pipeline, data, expert) for multi-GPU deployments.

- Apply quantization ([`FP8`{.docutils .literal .notranslate}]{.pre}/[`FP4`{.docutils .literal .notranslate}]{.pre}) to reduce memory usage by 2-4× with minimal accuracy loss.

- Tune engine arguments (batch size, memory utilization, graph modes) for your use case.

- Benchmark and scale across single-node and multi-node configurations.
:::

::::: {#pytorch-tunableop .section}
[]{#mi300x-tunableop}

## PyTorch TunableOp[\#](#pytorch-tunableop "Link to this heading"){.headerlink}

[TunableOp](https://github.com/pytorch/pytorch/blob/main/aten/src/ATen/cuda/tunable/README.md){.reference .external} is a feature used to obtain the optimal GPU kernel for a key PyTorch operations. At the moment, TunableOp supports the tuning of dense matrix multiplies (GEMM, batched GEMM, GEMM and bias, and scaled GEMM). This feature is useful for squeezing out the last bit of performance. In short, it will try up to thousands of matrix multiply algorithms that are available in rocBLAS and hipBLASLt. A caveat is that as the math libraries improve over time, there is a less benefit to using TunableOp, and there is also no guarantee that the workload being tuned will be able to outperform the default GEMM algorithm in hipBLASLt.

Some additional references for PyTorch TunableOp include [ROCm blog](https://rocm.blogs.amd.com/artificial-intelligence/pytorch-tunableop/README.html){.reference .external}, TunableOp [README](https://github.com/pytorch/pytorch/blob/main/aten/src/ATen/cuda/tunable/README.md){.reference .external}, and [llm tuning](https://rocm.docs.amd.com/en/latest/how-to/llm-fine-tuning-optimization/model-acceleration-libraries.html#fine-tuning-llms-pytorch-tunableop){.reference .external}.

The three most important environment variables for controlling TunableOp are:

[`PYTORCH_TUNABLEOP_ENABLED`{.docutils .literal .notranslate}]{.pre}

:   The main on/off switch for all TunableOp implementations. Default is [`0`{.docutils .literal .notranslate}]{.pre} (disabled). Set to [`1`{.docutils .literal .notranslate}]{.pre} to enable.

[`PYTORCH_TUNABLEOP_TUNING`{.docutils .literal .notranslate}]{.pre}

:   When enabled, if a tuned entry isn't found, runs the tuning step and records the entry. Default is [`1`{.docutils .literal .notranslate}]{.pre} (enabled). Set to [`0`{.docutils .literal .notranslate}]{.pre} to disable.

[`PYTORCH_TUNABLEOP_VERBOSE`{.docutils .literal .notranslate}]{.pre}

:   Enables verbose output for debugging purposes -- it can be useful to see if TunableOp is being used at all. Default is [`0`{.docutils .literal .notranslate}]{.pre} (disabled). Set to [`1`{.docutils .literal .notranslate}]{.pre} to enable.

For the complete list of environment variables, see the TunableOp [README](https://github.com/pytorch/pytorch/blob/main/aten/src/ATen/cuda/tunable/README.md){.reference .external}. There are also Python APIs to set some of these environment variables, but the preferred way to set the TunableOp tuning parameters is to use the environment variables.

::: {#workflow .section}
### Workflow[\#](#workflow "Link to this heading"){.headerlink}

Use these environment variables to enable TunableOp for any applications or libraries that use PyTorch (2.3 or later).

The first step is the tuning pass:

1.  Enable TunableOp and tuning. Optionally enable verbose mode:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        PYTORCH_TUNABLEOP_ENABLED=1 PYTORCH_TUNABLEOP_VERBOSE=1 your_script.sh
    :::
    ::::

    This pass can be very slow. The output will be the [`tunableop_results.csv`{.docutils .literal .notranslate}]{.pre} file containing a list of GEMMs encountered and the optimal GPU kernel that was identified.

    Multi-GPU tuning is supported, producing a separate tunableop_results.csv file for each GPU. The tuning algorithm executes independently on each GPU, with each tuning process sandboxed to its respective GPU. There is no inter-GPU communication during tuning.

    For data-parallel algorithms, where GEMM configurations across GPUs are typically identical, this approach can result in redundant work. In such cases, running the workload on a single GPU might suffice. However, for algorithms involving multiple levels of parallelism (as in data parallelism combined with ML model parallelism), different GPUs might require distinct GEMM parameters. In these scenarios, a multi-GPU configuration is recommended.

In the second step, we re-run the workload with optimal configuration using the [`tunableop_results.csv`{.docutils .literal .notranslate}]{.pre} file obtained in step 1.

2.  Enable TunableOp, disable tuning, and measure:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        PYTORCH_TUNABLEOP_ENABLED=1 PYTORCH_TUNABLEOP_TUNING=0 your_script.sh
    :::
    ::::

Compare the wall-clock time from this second step to your reference wall-clock time with TunableOp completely disabled ([`PYTORCH_TUNABLEOP_ENABLED=0`{.docutils .literal .notranslate}]{.pre}).
:::

::: {#offline-tuning .section}
### Offline tuning[\#](#offline-tuning "Link to this heading"){.headerlink}

A new feature of TunableOp, offline tuning, is available in upstream PyTorch and supported in PyTorch 2.6 or later.

Traditionally, tuning is performed in-place during workload execution. While convenient for one-off tuning, this approach can become cumbersome if frequent re-tuning is required -- such as when a new version of a math library is released. In these cases, re-running the workload and performing tuning repeatedly can be inefficient.

Offline tuning addresses this challenge by decoupling the tuning process from workload execution. It enables the collection of GEMMs from a workload during a collection pass, followed by tuning these GEMMs in a separate tuning pass, without re-running the original workload. This approach significantly reduces compute resource requirements, particularly for time-intensive workloads.

For workflow instructions, refer to the [Offline Tuning documentation](https://github.com/pytorch/pytorch/blob/main/aten/src/ATen/cuda/tunable/README.md#offline-tuning){.reference .external}.
:::
:::::

::::::::: {#pytorch-inductor-max-autotune-tuning-knobs .section}
[]{#mi300x-torchinductor-tuning}

## PyTorch inductor max-autotune tuning knobs[\#](#pytorch-inductor-max-autotune-tuning-knobs "Link to this heading"){.headerlink}

The following are suggestions for optimizing matrix multiplication (GEMM) and convolution ([`conv`{.docutils .literal .notranslate}]{.pre}) operations in PyTorch using [`inductor`{.docutils .literal .notranslate}]{.pre}, a part of the PyTorch compilation framework.

Learn more about TorchInductor environment variables and usage in the [PyTorch documentation](https://pytorch.org/docs/2.3/torch.compiler_inductor_profiling.html){.reference .external}.

::: {.admonition .note}
Note

Triton is not used if regular [[MIOpen]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/MIOpen/en/latest/index.html "(in MIOpen Documentation v3.5.1)"){.reference .external} or [[rocBLAS]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/index.html "(in rocBLAS Documentation v5.2.0)"){.reference .external} performs faster for a specific operation.
:::

::: {.admonition .note}
Note

Experimental: TunableOp (see the [[PyTorch TunableOp]{.std .std-ref}](#mi300x-tunableop){.reference .internal} section) can also be used in combination with [`TorchInductor`{.docutils .literal .notranslate}]{.pre} [`max-autotune`{.docutils .literal .notranslate}]{.pre} mode to boost ATen GEMM performance but will further increase tuning time. The environment variable [`TORCHINDUCTOR_AUTOTUNE_MULTI_DEVICE=1`{.docutils .literal .notranslate}]{.pre} can be useful in single GPU workloads to distribute Triton GEMM tuning.
:::

::: {#triton-backend .section}
### Triton backend[\#](#triton-backend "Link to this heading"){.headerlink}

The goal is to leverage Triton to achieve better performance. To tune Triton kernels with [`gemm`{.docutils .literal .notranslate}]{.pre} and convolution ops ([`conv`{.docutils .literal .notranslate}]{.pre}), use the [`torch.compile`{.docutils .literal .notranslate}]{.pre} function with the [`max-autotune`{.docutils .literal .notranslate}]{.pre} mode. This benchmarks a predefined list of Triton configurations and selects the fastest one for each shape. See the configurations in PyTorch source code:

- [conv configurations for "max-autotune"](https://github.com/pytorch/pytorch/blob/a1d02b423c6b4ccacd25ebe86de43f650463bbc6/torch/_inductor/kernel/conv.py#L51){.reference .external}

- [matmul configurations for "max-autotune"](https://github.com/pytorch/pytorch/blob/a1d02b423c6b4ccacd25ebe86de43f650463bbc6/torch/_inductor/kernel/mm_common.py#L118){.reference .external}

This tuning will select the best Triton [`gemm`{.docutils .literal .notranslate}]{.pre} configurations according to tile-size [`(BLOCK_M,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`BLOCK_N,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`BLOCK_K),`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`num_stages,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`num_warps`{.docutils .literal .notranslate}]{.pre} and [`mfma`{.docutils .literal .notranslate}]{.pre} instruction size ( [`matrix_instr_nonkdim`{.docutils .literal .notranslate}]{.pre} ) (see "Triton kernel optimization" section for more details).

- Set [`torch._inductor.config.max_autotune`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`=`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`True`{.docutils .literal .notranslate}]{.pre} or [`TORCHINDUCTOR_MAX_AUTOTUNE=1`{.docutils .literal .notranslate}]{.pre}.

- Or, for more fine-grained control:

  [`torch._inductor.config.max_autotune_gemm`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`=`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`True`{.docutils .literal .notranslate}]{.pre}

  :   To enable tuning or lowering of [`mm`{.docutils .literal .notranslate}]{.pre}/[`conv`{.docutils .literal .notranslate}]{.pre}s.

  [`torch._inductor.config.max_autotune.pointwise`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`=`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`True`{.docutils .literal .notranslate}]{.pre}

  :   To enable tuning for [`pointwise`{.docutils .literal .notranslate}]{.pre}/[`reduction`{.docutils .literal .notranslate}]{.pre} ops.

  [`torch._inductor.max_autotune_gemm_backends`{.docutils .literal .notranslate}]{.pre} or [`TORCHINDUCTOR_MAX_AUTOTUNE_GEMM_BACKENDS`{.docutils .literal .notranslate}]{.pre}

  :   Selects the candidate backends for [`mm`{.docutils .literal .notranslate}]{.pre} auto-tuning. Defaults to [`TRITON,ATEN`{.docutils .literal .notranslate}]{.pre}. Limiting this to [`TRITON`{.docutils .literal .notranslate}]{.pre} might improve performance by enabling more fused [`mm`{.docutils .literal .notranslate}]{.pre} kernels instead of going to rocBLAS.

- Inference can see large improvements on AMD GPUs by utilizing [`torch._inductor.config.freezing=True`{.docutils .literal .notranslate}]{.pre} or the [`TORCHINDUCTOR_FREEZING=1`{.docutils .literal .notranslate}]{.pre} variable, which in-lines weights as constants and enables constant folding optimizations.

- Enabling [`inductor`{.docutils .literal .notranslate}]{.pre}'s cpp_wrapper might improve overhead. This generates C++ code which launches Triton binaries directly with [`hipModuleLaunchKernel`{.docutils .literal .notranslate}]{.pre} and relies on hipification.

  [`torch._inductor.config.cpp_wrapper=True`{.docutils .literal .notranslate}]{.pre} or [`TORCHINDUCTOR_CPP_WRAPPER=1`{.docutils .literal .notranslate}]{.pre}

- Convolution workloads might see a performance benefit by specifying [`torch._inductor.config.layout_optimization=True`{.docutils .literal .notranslate}]{.pre} or [`TORCHINDUCTOR_LAYOUT_OPTIMIZATION=1`{.docutils .literal .notranslate}]{.pre}. This can help performance by enforcing [`channel_last`{.docutils .literal .notranslate}]{.pre} memory format on the convolution in TorchInductor, avoiding any unnecessary transpose operations. Note that [`PYTORCH_MIOPEN_SUGGEST_NHWC=1`{.docutils .literal .notranslate}]{.pre} is recommended if using this.

- To extract the Triton kernels generated by [`inductor`{.docutils .literal .notranslate}]{.pre}, set the environment variable [`TORCH_COMPILE_DEBUG=1`{.docutils .literal .notranslate}]{.pre}, which will create a [`torch_compile_debug/`{.docutils .literal .notranslate}]{.pre} directory in the current path. The wrapper codes generated by [`inductor`{.docutils .literal .notranslate}]{.pre} are in one or more [`output_code.py`{.docutils .literal .notranslate}]{.pre} files corresponding to the FX graphs associated with the model. The Triton kernels are defined in these generated codes.
:::

::::: {#composable-kernel-backend .section}
### Composable Kernel backend[\#](#composable-kernel-backend "Link to this heading"){.headerlink}

You can enable the Composable Kernel ([`CK`{.docutils .literal .notranslate}]{.pre}) backend by appending [`CK`{.docutils .literal .notranslate}]{.pre} to the comma-separated list of backends. This allows the auto-tuning process to use kernels from the Composable Kernel library.

[`torch._inductor.max_autotune_gemm_backends`{.docutils .literal .notranslate}]{.pre} or [`TORCHINDUCTOR_MAX_AUTOTUNE_GEMM_BACKENDS`{.docutils .literal .notranslate}]{.pre}.

Install the Composable Kernel library's Python wrapper via pip using the following command:

:::: {.highlight-shell .notranslate}
::: highlight
    pip install git+https://github.com/rocm/composable_kernel@develop
:::
::::

This wrapper library is responsible for constructing a list of kernel instances available in the Composable Kernel library, as well as storing the kernel instance C++ includes in a known location (so clang can look into these paths when compiling the [`gemm`{.docutils .literal .notranslate}]{.pre} auto-tune candidates).

> ::: {}
> - [`matmul`{.docutils .literal .notranslate}]{.pre} (with [`float16`{.docutils .literal .notranslate}]{.pre} and [`bfloat16`{.docutils .literal .notranslate}]{.pre} inputs, row-major X, row-major or column-major W)
>
> - [`addmm`{.docutils .literal .notranslate}]{.pre} (with [`float16`{.docutils .literal .notranslate}]{.pre} or [`bfloat16`{.docutils .literal .notranslate}]{.pre} X, W and Bias; row-major X, row-major or column-major W; Bias can be broadcast either along row-major or column-major dimension)
>
> - [`scaled_mm`{.docutils .literal .notranslate}]{.pre} ([`float8_e4m3fnuz`{.docutils .literal .notranslate}]{.pre} inputs, [`bfloat16`{.docutils .literal .notranslate}]{.pre} output)
>
> - [`conv2d`{.docutils .literal .notranslate}]{.pre} (with [`float32`{.docutils .literal .notranslate}]{.pre}, [`float16`{.docutils .literal .notranslate}]{.pre} or [`bfloat16`{.docutils .literal .notranslate}]{.pre} inputs, channels-last weight layout)
> :::

- For working examples, see [test/inductor/test_ck_backend.py](https://github.com/pytorch/pytorch/blob/main/test/inductor/test_ck_backend.py){.reference .external}.

- Compiling or build time can be configured by modifying [`torch._inductor.config`{.docutils .literal .notranslate}]{.pre} to reduce the build time to avoid time-out.

  - [`compile_threads`{.docutils .literal .notranslate}]{.pre}: Number of threads used for compilation. Set it to the number of available CPU cores.

  - [`rocm.n_max_profiling_configs`{.docutils .literal .notranslate}]{.pre}: Limiting the number of kernels to speed up compilation.

- Setting environment variable [`PYTORCH_MIOPEN_SUGGEST_NHWC=1`{.docutils .literal .notranslate}]{.pre} to optimize convolution operations.

Debugging and troubleshooting performance:

- Generate a standalone executable runner to debug or assess kernels' performance by setting environment variable [`INDUCTOR_CK_BACKEND_GENERATE_TEST_RUNNER_CODE=1`{.docutils .literal .notranslate}]{.pre} to facilitate debugging and profiling. By default, the CK backend will not build a standalone executable runner.

- Enable debug by passing compilation flags (e.g., [`is_debug`{.docutils .literal .notranslate}]{.pre}) to clang when compiling the kernels in [`torch._inductor.config.rocm`{.docutils .literal .notranslate}]{.pre} class.

- The generated source files and other products of clang compilation are located in the torch inductor root directory (default: [`/tmp/torchinductor_root`{.docutils .literal .notranslate}]{.pre})
:::::
:::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::: {#rocm-library-tuning .section}
[]{#mi300x-rocm-library-tuning}

## ROCm library tuning[\#](#rocm-library-tuning "Link to this heading"){.headerlink}

ROCm library tuning involves optimizing the performance of routine computational operations (such as [`GEMM`{.docutils .literal .notranslate}]{.pre}) provided by ROCm libraries like [[hipBLASLt]{.std .std-ref}](#mi300x-hipblaslt){.reference .internal}, [[Composable Kernel]{.std .std-ref}](#mi300x-ck){.reference .internal}, [[MIOpen]{.std .std-ref}](#mi300x-miopen){.reference .internal}, and [[RCCL]{.std .std-ref}](#mi300x-rccl){.reference .internal}. This tuning aims to maximize efficiency and throughput on Instinct MI300X GPUs to gain improved application performance.

::::::::::::: {#gemm-general-matrix-multiplication .section}
[]{#mi300x-library-gemm}

### GEMM (general matrix multiplication)[\#](#gemm-general-matrix-multiplication "Link to this heading"){.headerlink}

GEMMs (General Matrix Multiplications) are a fundamental building block for many operations in neural networks. GEMM is defined as [`C`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`=`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`αAB`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`+`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`βC`{.docutils .literal .notranslate}]{.pre} where A is an [`MxK`{.docutils .literal .notranslate}]{.pre} matrix input and B is [`KxN`{.docutils .literal .notranslate}]{.pre} matrix input, and C is [`MxN`{.docutils .literal .notranslate}]{.pre} matrix input and is overwritten by the output. α and β are scalar inputs. hipBLASLt is a library that provides general matrix-matrix operations with a flexible API and extends functionalities beyond a traditional BLAS library.

::: {#hipblaslt-benchmarking .section}
[]{#mi300x-hipblaslt}

#### hipBLASLt benchmarking[\#](#hipblaslt-benchmarking "Link to this heading"){.headerlink}

The GEMM library [hipBLASLt](https://rocm.docs.amd.com/projects/hipBLASLt/en/latest/index.html){.reference .external} provides a benchmark tool for its supported operations. Refer to the [documentation](https://github.com/ROCm/hipBLASLt/blob/develop/clients/bench/README.md){.reference .external} for details.

- Example 1: Benchmark mix fp8 GEMM

  :::: {.highlight-shell .notranslate}
  ::: highlight
      HIP_FORCE_DEV_KERNARG=1  hipblaslt-bench --alpha 1 --beta 0 -r f16_r \
      --a_type f16_r --b_type f8_r --compute_type f32_f16_r \
      --initialization trig_float  --cold_iters 100 --iters 1000 --rotating 256
  :::
  ::::

- Example 2: Benchmark forward epilogues and backward epilogues

  - [`HIPBLASLT_EPILOGUE_RELU:`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`"--activation_type`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`relu";`{.docutils .literal .notranslate}]{.pre}

  - [`HIPBLASLT_EPILOGUE_BIAS:`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`"--bias_vector";`{.docutils .literal .notranslate}]{.pre}

  - [`HIPBLASLT_EPILOGUE_RELU_BIAS:`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`"--activation_type`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`relu`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--bias_vector";`{.docutils .literal .notranslate}]{.pre}

  - [`HIPBLASLT_EPILOGUE_GELU:`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`"--activation_type`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`gelu";`{.docutils .literal .notranslate}]{.pre}

  - [`HIPBLASLT_EPILOGUE_DGELU":`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--activation_type`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`gelu`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--gradient";`{.docutils .literal .notranslate}]{.pre}

  - [`HIPBLASLT_EPILOGUE_GELU_BIAS:`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`"--activation_type`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`gelu`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--bias_vector";`{.docutils .literal .notranslate}]{.pre}

  - [`HIPBLASLT_EPILOGUE_GELU_AUX:`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`"--activation_type`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`gelu`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--use_e";`{.docutils .literal .notranslate}]{.pre}

  - [`HIPBLASLT_EPILOGUE_GELU_AUX_BIAS:`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`"--activation_type`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`gelu`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--bias_vector`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--use_e";`{.docutils .literal .notranslate}]{.pre}

  - [`HIPBLASLT_EPILOGUE_DGELU_BGRAD:`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`"--activation_type`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`gelu`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--bias_vector`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--gradient";`{.docutils .literal .notranslate}]{.pre}

  - [`HIPBLASLT_EPILOGUE_BGRADA:`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`"--bias_vector`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--gradient`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--bias_source`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`a";`{.docutils .literal .notranslate}]{.pre}

  - [`HIPBLASLT_EPILOGUE_BGRADB:`{.docutils .literal .notranslate}]{.pre}`  `{.docutils .literal .notranslate}[`"--bias_vector`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--gradient`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--bias_source`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`b";`{.docutils .literal .notranslate}]{.pre}
:::

::::::: {#hipblaslt-auto-tuning-using-hipblaslt-bench .section}
#### hipBLASLt auto-tuning using hipblaslt-bench[\#](#hipblaslt-auto-tuning-using-hipblaslt-bench "Link to this heading"){.headerlink}

Use the auto-tuning tool in hipBLASLt to get the best solution for a given problem size.

::: {#prerequisite .section}
##### Prerequisite[\#](#prerequisite "Link to this heading"){.headerlink}

Build hipBLASLt. See the [hipBLASLt repository](https://github.com/ROCm/hipBLASLt){.reference .external} to see detailed build instructions.
:::

::: {#quick-start .section}
##### Quick start[\#](#quick-start "Link to this heading"){.headerlink}

Create a working folder for the auto-tuning tool, for example, [`tuning/`{.docutils .literal .notranslate}]{.pre}.

1.  Set the [`ProblemType`{.docutils .literal .notranslate}]{.pre}, [`TestConfig`{.docutils .literal .notranslate}]{.pre}, and [`TuningParameters`{.docutils .literal .notranslate}]{.pre} in the YAML file. You can modify the template YAML file in [`hipblaslt/utilities`{.docutils .literal .notranslate}]{.pre}.

<figure class="align-center">
<img src="../../../_images/hipblaslt_yaml_template.png" alt="HipBLASLt auto-tuning yaml file template" />
</figure>

2.  Run the following command to start tuning.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # python3 hipblaslt/utilities/find_exact.py <path-to-config-yaml> <path-to-the-root-of-built-hipblaslt> <working-directory>
        # Assume we're in folder tuning, the default root of the build folder of hipblaslt is hipblaslt/build/release
        python3 ../hipblaslt/utilities/find_exact.py tuning.yaml hipblaslt/build/release ./
    :::
    ::::
:::

::: {#output .section}
##### Output[\#](#output "Link to this heading"){.headerlink}

The tool will create two output folders. The first one is the benchmark results, the second one is the generated equality kernels. If [`SplitK`{.docutils .literal .notranslate}]{.pre} is used, the solution's [`GlobalSplitU`{.docutils .literal .notranslate}]{.pre} will also change if the winner is using a different [`SplitK`{.docutils .literal .notranslate}]{.pre} from the solution. The YAML files generated inside the folder [`1_LogicYaml`{.docutils .literal .notranslate}]{.pre} are logic ones. These YAML files are just like those generated from TensileLite.

<figure class="align-center">
<img src="../../../_images/hipblaslt_auto_tuning_output_files.png" alt="HipBLASLt auto-tuning output folder" />
</figure>
:::

::: {#a-quick-view-of-the-config-yaml .section}
##### A quick view of the config YAML[\#](#a-quick-view-of-the-config-yaml "Link to this heading"){.headerlink}

The tuning tool is a two-step tool. It first runs the benchmark, then it creates the equality YAML for the user. Note that this config YAML file is different from the config YAML used in TensileLite.

- **Benchmarking**

  The first step is to run the benchmark, [`find_exact.py`{.docutils .literal .notranslate}]{.pre} will run the benchmark with [`hipblaslt-bench`{.docutils .literal .notranslate}]{.pre}. For the default configurations, see the Python file.

  :::: {.highlight-python .notranslate}
  ::: highlight
      defaultBenchOptions = {"ProblemType": {
          "TransposeA": 0,
          "TransposeB": 0,
          "ComputeInputDataType": "s",
          "ComputeDataType": "s",
          "DataTypeC": "s",
          "DataTypeD": "s",
          "UseBias": False
      }, "TestConfig": {
          "ColdIter": 20,
          "Iter": 100,
          "AlgoMethod": "all",
          "RequestedSolutions": 2, # Only works in AlgoMethod heuristic
          "SolutionIndex": None, # Only works in AlgoMethod index
          "ApiMethod": "cpp",
          "RotatingBuffer": 0,
      }, "TuningParameters": {
          "SplitK": [0]
      }, "ProblemSizes": []}
      defaultCreateLogicOptions = {}  # Currently unused
  :::
  ::::

- 

  [`TestConfig`{.docutils .literal .notranslate}]{.pre}

  :   1.  [`ColdIter`{.docutils .literal .notranslate}]{.pre}: This is number the warm-up iterations before starting the kernel benchmark.

      2.  [`Iter`{.docutils .literal .notranslate}]{.pre}: This is the number of iterations in kernel benchmarking

      3.  [`AlgoMethod`{.docutils .literal .notranslate}]{.pre}: We recommended to keep this unchanged because method "all" returns all the available solutions for the problem type.

      4.  [`ApiMethod`{.docutils .literal .notranslate}]{.pre}: We have c, mix, and cpp. Doesn't affect the result much.

      5.  [`RotatingBuffer`{.docutils .literal .notranslate}]{.pre}: This is a size in the unit of MB. Recommended to set the value equal to the size of the cache of the card to avoid the kernel fetching data from the cache.

- 

  [`TuningParameters`{.docutils .literal .notranslate}]{.pre}

  :   [`SplitK`{.docutils .literal .notranslate}]{.pre}: Divide [`K`{.docutils .literal .notranslate}]{.pre} into [`N`{.docutils .literal .notranslate}]{.pre} portions. Not every solution supports [`SplitK`{.docutils .literal .notranslate}]{.pre}. The solution will be skipped if not supported.

- 

  [`CreateLogic`{.docutils .literal .notranslate}]{.pre}

  :   Currently no control parameters.
:::
:::::::

:::::: {#hipblaslt-backend-assembly-generator-tuning .section}
#### hipBLASLt backend assembly generator tuning[\#](#hipblaslt-backend-assembly-generator-tuning "Link to this heading"){.headerlink}

[[hipBLASLt]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/hipBLASLt/en/latest/index.html "(in hipBLASLt Documentation v1.2.2)"){.reference .external} has a backend assembly generator in [hipBLASLt's GitHub repository](https://github.com/ROCm/hipBLASLt/tree/develop/tensilelite){.reference .external}, named TensileLite. TensileLite enables performance optimization by tuning the backend assembly generator. The following section explains how to use TensileLite to tune hipBLASLt for better performance.

:::: {.highlight-shell .notranslate}
::: highlight
    cd /hipBLASLt/tensilelite
    ./Tensile/bin/Tensile config.yaml output_path
:::
::::

::: {#config-yaml .section}
##### config.yaml[\#](#config-yaml "Link to this heading"){.headerlink}

This file contains the parameters and settings for the tuning process. Here's a breakdown of the important sections:

[`GlobalParameters`{.docutils .literal .notranslate}]{.pre}

:   The set of parameters which provides context for the entire tuning exercise.

    Using [`0`{.docutils .literal .notranslate}]{.pre} for [`NumElementsToValidate`{.docutils .literal .notranslate}]{.pre} is suggested for performance tuning to avoid validation overhead.

    :::: {.highlight-python .notranslate}
    ::: highlight
        globalParameters["NumElementsToValidate"] = 0
    :::
    ::::

[`BenchmarkProblems`{.docutils .literal .notranslate}]{.pre}

:   Defines the set of kernel specifications as well as the size definitions for the tuning exercise.

    - [`ProblemType`{.docutils .literal .notranslate}]{.pre} ([`OperationType`{.docutils .literal .notranslate}]{.pre}, [`DataType`{.docutils .literal .notranslate}]{.pre}, [`TransposeA`{.docutils .literal .notranslate}]{.pre}, [`TransposeB`{.docutils .literal .notranslate}]{.pre})

    - [`BenchmarkCommonParameters`{.docutils .literal .notranslate}]{.pre} (the same parameters for all solutions)

    - [`ForkParameters`{.docutils .literal .notranslate}]{.pre}

    - [`BenchmarkFinalParameters`{.docutils .literal .notranslate}]{.pre} ([`ProblemSizes`{.docutils .literal .notranslate}]{.pre})

[`LibraryLogic`{.docutils .literal .notranslate}]{.pre}

:   Specifies the target environment and platform.

    - [`ScheduleName`{.docutils .literal .notranslate}]{.pre}

      - [`aldebaran`{.docutils .literal .notranslate}]{.pre} is MI200

      - [`aquavanjaram`{.docutils .literal .notranslate}]{.pre} is MI300

    :::: {.highlight-shell .notranslate}
    ::: highlight
        $ ls
        aldebaran  aquavanjaram  navi31  navi32
    :::
    ::::

    :::: {.highlight-yaml .notranslate}
    ::: highlight
        LibraryLogic:
          ScheduleName: "aldebaran"
          DeviceNames: [Device 0050, Device 0052, Device 0054, Device 0062, Device 7400]
          ArchitectureName: "gfx90a"
    :::
    ::::

[`LibraryClient`{.docutils .literal .notranslate}]{.pre}

:   If defined, this will enable step 4 of the tuning process, which means the final library will be created.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        $ ls
        aldebaran_Cijk_Ailk_Bjlk_S.yaml
    :::
    ::::
:::
::::::
:::::::::::::

:::::::::: {#tensilelite-tuning-flow .section}
### TensileLite tuning flow[\#](#tensilelite-tuning-flow "Link to this heading"){.headerlink}

The TensileLite tuning flow consists of seven steps. In the first six steps, the programmable benchmarking protocol generates fast kernel candidates. In the final step ([[step 7]{.std .std-ref}](#tensilelite-tuning-step-7){.reference .internal}), these candidates are benchmarked against a predefined set of problem sizes.

<figure id="tensilelite-tuning-flow-fig" class="align-center">
<img src="../../../_images/tensilelite-tuning-flow.png" alt="TensileLite tuning flow" />
</figure>

::: {#step-1-initial-solution-parameters .section}
[]{#tensilelite-tuning-step-1}

#### Step 1: Initial solution parameters[\#](#step-1-initial-solution-parameters "Link to this heading"){.headerlink}

Before Tensile is able to benchmark a kernel parameter in Step 2 of the [[preceding figure]{.std .std-ref}](#tensilelite-tuning-flow-fig){.reference .internal}, such as [`PrefetchGlobalRead={False,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`True}`{.docutils .literal .notranslate}]{.pre}, all other kernel parameters not being measured must be specified. Therefore, the first step is to initialize a list of default kernel parameters, then subsequent steps of benchmarking will override a parameter from this default list, with the parameter determined from benchmarking. Tensile is pre-loaded with default parameters for any unspecified during tuning.
:::

::: {#step-2-benchmark-common-parameters .section}
#### Step 2: Benchmark common parameters[\#](#step-2-benchmark-common-parameters "Link to this heading"){.headerlink}

Benchmarking common parameters determines parameters which are universally preferable to their alternatives regardless of other parameters. To benchmark common parameters:

- User specifies parameters and values to benchmark.

- Tensile benchmarks all parameter combinations for a user-specified problem size.

- Tensile selects the fastest parameter combination which is now labeled determined and will subsequently be used.

In practice, these parameters are not used, since globally preferred parameters are set as defaults in Tensile and do not need to be re-measured.
:::

::: {#step-3-fork-parameters .section}
#### Step 3: Fork parameters[\#](#step-3-fork-parameters "Link to this heading"){.headerlink}

Rather than continuing to determine globally fastest parameters, which eventually leads to a single fastest kernel, forking creates many different kernels, all of which will be considered for use. All forked parameters are considered determined, i.e., they aren't measured to determine which is fastest. The [[preceding figure]{.std .std-ref}](#tensilelite-tuning-flow-fig){.reference .internal} shows 7 kernels being forked in Step 3.
:::

::: {#step-4-benchmark-fork-parameters .section}
#### Step 4: Benchmark fork parameters[\#](#step-4-benchmark-fork-parameters "Link to this heading"){.headerlink}

Next, tuning continues its refinement by determining fastest parameters for each forked permutation, same as in Step 2.
:::

::: {#step-5-join-parameters .section}
#### Step 5: Join parameters[\#](#step-5-join-parameters "Link to this heading"){.headerlink}

After tuning the forked kernels, joining reduces the list of kernels so that fewer kernels will be considered for final use. Each kernel in the resulting list must have different values for the listed [`JoinParameters`{.docutils .literal .notranslate}]{.pre}, for example, employing [`JoinParameters`{.docutils .literal .notranslate}]{.pre} = [`MacroTile`{.docutils .literal .notranslate}]{.pre} will result in only a few final kernels, each with a different [`MacroTile`{.docutils .literal .notranslate}]{.pre}. If there are multiple kernels with the same [`MacroTile`{.docutils .literal .notranslate}]{.pre}, only the fastest is kept. In the above figure the 7 forked kernel have been reduced to 3 joined kernels.
:::

::: {#step-6-benchmark-join-parameters .section}
#### Step 6: Benchmark join parameters[\#](#step-6-benchmark-join-parameters "Link to this heading"){.headerlink}

Users can further tune parameters of the joined kernels. This steps is same as Steps 4 except that it tunes after joining so that there are fewer kernels to be tuned. In practice, this step is not used; using Step 4 is preferred so that all parameters are measured before joining.
:::

::: {#step-7-benchmark-final-parameters .section}
[]{#tensilelite-tuning-step-7}

#### Step 7: Benchmark final parameters[\#](#step-7-benchmark-final-parameters "Link to this heading"){.headerlink}

At the conclusion of Step 6, all parameters of all kernels have been determined and the final set of kernels for consideration has been established. Now all final kernels will be measured against all problem sizes specified by the user. Problem sizes can be specified as Range sizes and Exact sizes. Range sizes cause benchmarking of a broad range of sizes, and Tensile will be able to interpolate which kernel is best even between the specifically measured sizes. Exact sizes cause a single problem size to be measured, and the final library is guaranteed to choose the fastest kernel for that size. This final benchmarking generates the data that is subsequently analyzed for creating the mapping of problem size to optimal kernel.
:::
::::::::::

:::::::: {#update-logic-yaml-files .section}
### Update logic YAML files[\#](#update-logic-yaml-files "Link to this heading"){.headerlink}

The logic YAML files in hipBLASLt are located in [`library/src/amd_detail/rocblaslt/src/Tensile/Logic/asm_full/`{.docutils .literal .notranslate}]{.pre}.

To merge the YAML files from the tuned results in TensileLite, use the [`merge.py`{.docutils .literal .notranslate}]{.pre} located in [`tensilelite/Tensile/Utilities`{.docutils .literal .notranslate}]{.pre} with the following command:

:::: {.highlight-shell .notranslate}
::: highlight
    merge.py original_dir new_tuned_yaml_dir output_dir
:::
::::

The following table describes the logic YAML files.

::: pst-scrollable-table-container
  Logic YAML                                             Description
  ------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------
  [`Equality`{.docutils .literal .notranslate}]{.pre}    Update the equality file when your tuned YAML is an exact tuning.
  [`GridBased`{.docutils .literal .notranslate}]{.pre}   Update the gridbased file when your tuned YAML is a grid-based tuning.
  [`FreeSize`{.docutils .literal .notranslate}]{.pre}    Update the freesize file when your tuned YAML contains confidential sizes, or others. Note that freesize YAML files do not require any problem size.
:::

::: {#tensile-optimization-and-performance-tuning-tips .section}
#### Tensile optimization and performance tuning tips[\#](#tensile-optimization-and-performance-tuning-tips "Link to this heading"){.headerlink}

MI16x16 versus MI32x32

:   MI16x16 outperforms MI32x32 due to its superior power efficiency. The MI16x16 format refers to the [`v_mfma`{.docutils .literal .notranslate}]{.pre} instruction (such as [`v_mfma_f32_16x16x16f16`{.docutils .literal .notranslate}]{.pre}). See [https://llvm.org/docs/AMDGPU/AMDGPUAsmGFX940.html#vop3p](https://llvm.org/docs/AMDGPU/AMDGPUAsmGFX940.html#vop3p){.reference .external}.

Clock differences among XCDs

:   There can be a clock speed variation of 3% to 10% among different XCDs. Typically, XCD0 has the highest clock speed, while XCD7 has the lowest on MI300X. For optimal efficiency calculations on MI300X, use the XCD with the lowest average clock speed. If the average clock speed of XCD0 is used, target efficiencies (such as, 95% for DGEMM HPL cases with K=512) may not be achievable.

WorkGroupMapping

:   To maximize L2 cache efficiency, use multiples of the XCD number. For MI300X, this means using multiples of 8 (such as, 24, 32, 40).

GEMM stride issues

:   On MI300, if the matrix stride in GEMM is a multiple of 512 bytes, it can lead to Tagram channel hotspotting issues, causing a significant performance drop, especially for TN transpose cases. This can increase the latency of VMEM instructions and cause a notable performance drop. To avoid this, use stride padding to ensure the stride is not a multiple of 512 bytes (for instance, for TN F16 GEMM, set [`lda`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`=`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`ldb`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`=`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`K`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`+`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`128`{.docutils .literal .notranslate}]{.pre} when [`K`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`%`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`256`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`==`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`0`{.docutils .literal .notranslate}]{.pre}).
:::

::: {#optimizing-composable-kernel-gemm-kernels .section}
[]{#mi300x-ck}

#### Optimizing Composable Kernel GEMM kernels[\#](#optimizing-composable-kernel-gemm-kernels "Link to this heading"){.headerlink}

The performance of a GEMM kernel is significantly influenced by the input values. The performance hierarchy based on input value types, from highest to lowest, is as follows:

- Case 1: \[all 0\]

- Case 2: \[all identical integers\]

- Case 3: \[random integers\]

- Case 4: \[random floats\]

There can be more than a 20 percent performance drop between Case 1 and Case 4, and a 10 percent drop between random integers and random floats.

Additionally, [`bf16`{.docutils .literal .notranslate}]{.pre} matrix core execution is noticeably faster than [`f16`{.docutils .literal .notranslate}]{.pre}.

Distributing workgroups with data sharing on the same XCD can enhance performance (reduce latency) and improve benchmarking stability.

CK provides a rich set of template parameters for generating flexible accelerated computing kernels for difference application scenarios.

See [[Optimizing with Composable Kernel]{.doc}](optimizing-with-composable-kernel.html){.reference .internal} for an overview of Composable Kernel GEMM kernels, information on tunable parameters, and examples.
:::
::::::::

:::::::::::: {#miopen .section}
[]{#mi300x-miopen}

### MIOpen[\#](#miopen "Link to this heading"){.headerlink}

MIOpen is AMD's open-source, deep learning primitives library for GPUs. It implements fusion to optimize for memory bandwidth and GPU launch overheads, providing an auto-tuning infrastructure to overcome the large design space of problem configurations.

::: {#convolution .section}
#### Convolution[\#](#convolution "Link to this heading"){.headerlink}

Many of MIOpen kernels have parameters which affect their performance. Setting these kernel parameters to optimal values for a given convolution problem, allows reaching the best possible throughput. The optimal values of these kernel parameters are saved in PerfDb (Performance database). PerfDb is populated through tuning. To manipulate the tuning level, use the environment variable [`MIOPEN_FIND_ENFORCE`{.docutils .literal .notranslate}]{.pre} (1-6). Optimal values of kernel parameters are used to benchmark all applicable convolution kernels for the given convolution problem. These values reside in the FindDb. To manipulate how to find the best performing kernel for a given convolution problem, use the environment variable [`MIOPEN_FIND_MODE`{.docutils .literal .notranslate}]{.pre} (1-5).
:::

::::: {#tuning-in-miopen .section}
[]{#mi300x-miopen-tuning}

#### Tuning in MIOpen[\#](#tuning-in-miopen "Link to this heading"){.headerlink}

[`MIOPEN_FIND_ENFORCE=DB_UPDATE`{.docutils .literal .notranslate}]{.pre}, [`2`{.docutils .literal .notranslate}]{.pre}

:   Performs auto-tuning and update to the PerfDb.

[`MIOPEN_FIND_ENFORCE=SEARCH`{.docutils .literal .notranslate}]{.pre}, [`3`{.docutils .literal .notranslate}]{.pre}

:   Only perform auto-tuning if PerfDb does not contain optimized value for a given convolution problem

What does [[PerfDb]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/MIOpen/en/latest/conceptual/perfdb.html "(in MIOpen Documentation v3.5.1)"){.reference .external} look like?

:::: {.highlight-default .notranslate}
::: highlight
    [
     2x128x56xNHWCxF, [
                      ConvAsm1x1U          :  1,8,2,64,2,4,1,8 ;       // optimum kernel params for convolution problem 2x128x56xNHWCxF
                      ConvOclDirectFwd1x1  : 1,128,1,1,0,2,32,4,0;     // optimum kernel params for convolution problem 2x128x56xNHWCxF
                      ],
    2x992x516xNHWCxF, [
                      ConvAsm1x1U          :  64,18,2,64,2,4,41,6 ;    // optimum kernel params for convolution problem 2x992x516xNHWCxF
                      ConvOclDirectFwd1x1  : 54,128,21,21,1,23,32,4,0  // optimum kernel params for convolution problem 2x992x516xNHWCxF
                      ]
     ...
    ]
:::
::::

See [Using the performance database](https://rocm.docs.amd.com/projects/MIOpen/en/latest/conceptual/perfdb.html "(in MIOpen Documentation v3.5.1)"){.reference .external} for more information.
:::::

::::::: {#finding-the-fastest-kernel .section}
#### Finding the fastest kernel[\#](#finding-the-fastest-kernel "Link to this heading"){.headerlink}

[`MIOPEN_FIND_MODE=NORMAL`{.docutils .literal .notranslate}]{.pre}, [`1`{.docutils .literal .notranslate}]{.pre}

:   Benchmark all the solvers and return a list (front element is the fastest kernel).

[`MIOPEN_FIND_MODE=FAST`{.docutils .literal .notranslate}]{.pre}, [`2`{.docutils .literal .notranslate}]{.pre}

:   Check FindDb (Find database) if convolution problem is found return - else immediate fallback mode (predict the performing kernel parameters based on mathematical and AI models).

[`MIOPEN_FIND_MODE=HYBRID`{.docutils .literal .notranslate}]{.pre}, [`3`{.docutils .literal .notranslate}]{.pre}

:   Check FindDb if convolution problem is found return - else benchmark that problem.

What does [[FindDb]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/MIOpen/en/latest/conceptual/finddb.html "(in MIOpen Documentation v3.5.1)"){.reference .external} look like?

:::: {.highlight-default .notranslate}
::: highlight
    [

     2x128x56xNHWCxF, [
                      ConvAsm1x1U          :  0.045 (time), 12312 (workspace), algo_type;
                      ConvOclDirectFwd1x1  : 1.145 (time), 0 (workspace), algo_type;
                      ],

    2x992x516xNHWCxF, [
                      ConvAsm1x1U          :  2.045 (time), 12312 (workspace), algo_type;
                      ConvOclDirectFwd1x1  : 1.145 (time), 0 (workspace), algo_type;
                      ]
     ...
    ]
:::
::::

See [Using the find APIs and immediate mode](https://rocm.docs.amd.com/projects/MIOpen/en/latest/how-to/find-and-immediate.html "(in MIOpen Documentation v3.5.1)"){.reference .external} for more information.

For example:

:::: {.highlight-shell .notranslate}
::: highlight
    MIOPEN_FIND_ENFORCE=3 MIOPEN_FIND_MODE=1 ./bin/MIOpenDriver convbfp16 -n 1 -c 1024 -H 14 -W 14 -k 256 -y 1 -x 1 -p 0 -q 0 -u 1 -v 1 -l 1 -j 1 -m conv -g 1 -F 1
:::
::::
:::::::
::::::::::::

::::::::::::::: {#rccl .section}
[]{#mi300x-rccl}

### RCCL[\#](#rccl "Link to this heading"){.headerlink}

[[RCCL]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rccl/en/latest/index.html "(in RCCL Documentation v2.27.7)"){.reference .external} is a stand-alone library of standard collective communication routines for GPUs, implementing all-reduce, all-gather, reduce, broadcast, reduce-scatter, gather, scatter, and all-to-all. RCCL supports an arbitrary number of GPUs installed in a single node or multiple nodes and can be used in either single- or multi-process (such as MPI) applications.

The following subtopics include information on RCCL features and optimization strategies:

- [[Use all eight GPUs]{.std .std-ref}](#mi300x-rccl-8-gpu){.reference .internal}

- [[Disable NUMA auto-balancing]{.std .std-ref}](#mi300x-rccl-disable-numa){.reference .internal}

- [[Disable ACS for multi-node RCCL]{.std .std-ref}](#mi300x-rccl-disable-acs){.reference .internal}

- [[Run RCCL-Unittests]{.std .std-ref}](#mi300x-rccl-unittests){.reference .internal}

- [[NPKit profiler]{.std .std-ref}](#mi300x-rccl-npkit){.reference .internal}

- [[RCCL-tests]{.std .std-ref}](#mi300x-rccl-tests){.reference .internal}

- [[Use one-process-per-GPU mode]{.std .std-ref}](#mi300x-rccl-one-process-per-gpu){.reference .internal}

- [[RCCL in E2E workloads]{.std .std-ref}](#mi300x-rccl-e2e){.reference .internal}

::: {#use-all-eight-gpus .section}
[]{#mi300x-rccl-8-gpu}

#### Use all eight GPUs[\#](#use-all-eight-gpus "Link to this heading"){.headerlink}

In an [[MI300X architecture]{.std .std-ref}](#mi300x-node-level-arch-fig){.reference .internal}, there are dedicated links between each pair of GPUs in a fully connected topology. Therefore, for collective operations, the best performance is achieved when all 8 GPUs and, hence, all the links between them are used. In the case of 2- or 4-GPU collective operations (generally less than 8 GPUs), you can only use a fraction of the potential bandwidth on the node.

The following figure shows an [[MI300X node-level architecture]{.doc}](../../../conceptual/gpu-arch/mi300.html){.reference .internal} of a system with AMD EPYC processors in a dual-socket configuration and eight AMD Instinct MI300X GPUs. The MI300X OAMs attach to the host system via PCIe Gen 5 x16 links (yellow lines). The GPUs use seven high-bandwidth, low-latency AMD Infinity Fabric™ links (red lines) to form a fully connected 8-GPU system.

<figure id="id5" class="align-default">
<span id="mi300x-node-level-arch-fig"></span><img src="../../../_images/mi300-node-level-arch.png" alt="../../../_images/mi300-node-level-arch.png" />
<figcaption><p><span class="caption-text">MI300 Series node-level architecture showing 8 fully interconnected MI300X OAM modules connected to (optional) PCIe switches via re-timers and HGX connectors.</span><a href="#id5" class="headerlink" title="Link to this image">#</a></p></figcaption>
</figure>
:::

::: {#disable-numa-auto-balancing .section}
[]{#mi300x-rccl-disable-numa}

#### Disable NUMA auto-balancing[\#](#disable-numa-auto-balancing "Link to this heading"){.headerlink}

In order to reduce performance variability and also achieve better performance, you need to make sure that NUMA auto-balancing is disabled on the node.

Check whether NUMA auto-balancing is disabled, by running the following command: [`cat`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`/proc/sys/kernel/numa_balancing`{.docutils .literal .notranslate}]{.pre} and checking whether the output is [`0`{.docutils .literal .notranslate}]{.pre}.

If the output is [`1`{.docutils .literal .notranslate}]{.pre}, you can disable NUMA auto-balancing by running the following command: [`sudo`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`sysctl`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`kernel.numa_balancing=0`{.docutils .literal .notranslate}]{.pre}. For more details, see [AMD Instinct MI300X system optimization](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi300x.html#disable-numa-auto-balancing){.reference .external}.
:::

::::: {#disable-acs-for-multi-node-rccl .section}
[]{#mi300x-rccl-disable-acs}

#### Disable ACS for multi-node RCCL[\#](#disable-acs-for-multi-node-rccl "Link to this heading"){.headerlink}

Check if ACS is disabled with [`sudo`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`lspci`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-vvv`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`\|`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`grep`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-i`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`"acsctl"`{.docutils .literal .notranslate}]{.pre}. This will print many lines. Check if there are any that show [`SrcValid+`{.docutils .literal .notranslate}]{.pre}

If there are any [`SrcValid+`{.docutils .literal .notranslate}]{.pre}, then use the following [`disable_acs.sh`{.docutils .literal .notranslate}]{.pre} script to disable ACS (requires [`sudo`{.docutils .literal .notranslate}]{.pre}).

:::: {.highlight-shell .notranslate}
::: highlight
    #!/bin/bash

    #

    # Disable ACS on every device that supports it

    #

    PLATFORM=$(dmidecode --string system-product-name)

    logger "PLATFORM=${PLATFORM}"

    # Enforce platform check here.

    #case "${PLATFORM}" in

    #"OAM"*)

    #logger "INFO: Disabling ACS is no longer necessary for ${PLATFORM}"

    #exit 0

    #;;

    #*)

    #;;

    #esac

    # must be root to access extended PCI config space

    if [ "$EUID" -ne 0 ]; then

    echo "ERROR: $0 must be run as root"

    exit 1

    fi

    for BDF in \`lspci -d "*:*:*" \| awk '{print $1}'`; do

    # skip if it doesn't support ACS

    setpci -v -s ${BDF} ECAP_ACS+0x6.w > /dev/null 2>&1

    if [ $? -ne 0 ]; then

    #echo "${BDF} does not support ACS, skipping"

    continue

    fi

    logger "Disabling ACS on \`lspci -s ${BDF}`"

    setpci -v -s ${BDF} ECAP_ACS+0x6.w=0000

    if [ $? -ne 0 ]; then

    logger "Error enabling directTrans ACS on ${BDF}"

    continue

    fi

    NEW_VAL=`setpci -v -s ${BDF} ECAP_ACS+0x6.w \| awk '{print $NF}'\`

    if [ "${NEW_VAL}" != "0000" ]; then

    logger "Failed to enabling directTrans ACS on ${BDF}"

    continue

    fi

    done

    exit 0
:::
::::
:::::

::: {#run-rccl-unittests .section}
[]{#mi300x-rccl-unittests}

#### Run RCCL-Unittests[\#](#run-rccl-unittests "Link to this heading"){.headerlink}

In order to verify RCCL installation and test whether all parts and units of RCCL work as expected you can run the RCCL-Unittests which is explained in [ROCm/rccl](https://github.com/ROCm/rccl?tab=readme-ov-file#tests){.github .reference .external}.
:::

::: {#npkit-profiler .section}
[]{#mi300x-rccl-npkit}

#### NPKit profiler[\#](#npkit-profiler "Link to this heading"){.headerlink}

To collect fine-grained trace events in RCCL components, especially in giant collective GPU kernels you can use the NPKit profiler explained in [ROCm/rccl](https://github.com/ROCm/rccl?tab=readme-ov-file#npkit){.github .reference .external}.
:::

::: {#rccl-tests .section}
[]{#mi300x-rccl-tests}

#### RCCL-tests[\#](#rccl-tests "Link to this heading"){.headerlink}

RCCL-tests are performance and error-checking tests for RCCL maintained in [ROCm/rccl-tests](https://github.com/ROCm/rccl-tests){.github .reference .external}.

These tests are one of the best ways to check the performance of different collectives provided by RCCL. You can select collectives, message sizes, datatypes, operations, number of iterations, etc., for your test, and then rccl-tests deliver performance metrics such as latency, algorithm bandwidth, and bus bandwidth for each case.
:::

::: {#use-one-process-per-gpu-mode .section}
[]{#mi300x-rccl-one-process-per-gpu}

#### Use one-process-per-GPU mode[\#](#use-one-process-per-gpu-mode "Link to this heading"){.headerlink}

RCCL delivers the best performance for collectives when it is configured in a one-process-per-GPU mode. This is due to the fact that for a one-process-per-multiple-GPUs configuration, you can run into kernel launch latency issues. This is because ROCm serializes kernel launches on multiple GPUs from one process which hurts performance.
:::

::::: {#rccl-in-e2e-workloads .section}
[]{#mi300x-rccl-e2e}

#### RCCL in E2E workloads[\#](#rccl-in-e2e-workloads "Link to this heading"){.headerlink}

Use the following environment variable to increase the number of channels used by RCCL when using RCCL in end-to-end workloads to potentially improve the performance:

:::: {.highlight-text .notranslate}
::: highlight
    export NCCL_MIN_NCHANNELS=112
:::
::::
:::::
:::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::: {#triton-kernel-performance-optimization .section}
[]{#mi300x-triton-kernel-performance-optimization}

## Triton kernel performance optimization[\#](#triton-kernel-performance-optimization "Link to this heading"){.headerlink}

Triton kernel optimization encompasses a variety of strategies aimed at maximizing the efficiency and performance of GPU computations. These strategies include [[optimizing overall GPU resource utilization]{.std .std-ref}](#mi300x-triton-gpu-utilization){.reference .internal}, [[tuning kernel configurations]{.std .std-ref}](#mi300x-autotunable-kernel-config){.reference .internal}, and [[leveraging specific hardware features]{.std .std-ref}](#mi300x-assembly-analysis){.reference .internal} to achieve higher throughput and lower latency.

::: {#auto-tunable-kernel-configurations .section}
[]{#mi300x-autotunable-kernel-config}

### Auto-tunable kernel configurations[\#](#auto-tunable-kernel-configurations "Link to this heading"){.headerlink}

Auto-tunable kernel configuration involves adjusting memory access and computational resources assigned to each compute unit. It encompasses the usage of [[LDS]{.std .std-ref}](#mi300x-cu-fig){.reference .internal}, register, and task scheduling on a compute unit.

The GPU contains global memory, local data share (LDS), and registers. Global memory has high access latency, but is large. LDS access has much lower latency, but is smaller. It is a fast on-CU software-managed memory that can be used to efficiently share data between all work items in a block. Register access is the fastest yet smallest among the three.

<figure id="id6" class="align-default">
<span id="mi300x-cu-fig"></span><img src="../../../_images/compute-unit.png" alt="../../../_images/compute-unit.png" />
<figcaption><p><span class="caption-text">Schematic representation of a CU in the CDNA2 or CDNA3 architecture.</span><a href="#id6" class="headerlink" title="Link to this image">#</a></p></figcaption>
</figure>

The following is a list of kernel arguments used for tuning performance and resource allocation on AMD GPUs, which helps in optimizing the efficiency and throughput of various computational kernels.

[`num_stages=n`{.docutils .literal .notranslate}]{.pre}

:   Adjusts the number of pipeline stages for different types of kernels. On AMD GPUs, set [`num_stages`{.docutils .literal .notranslate}]{.pre} according to the following rules:

    - For kernels with a single GEMM, set to [`2`{.docutils .literal .notranslate}]{.pre}.

    - For kernels with two GEMMs fused (Flash Attention, or any other kernel that fuses 2 GEMMs), set to [`1`{.docutils .literal .notranslate}]{.pre}.

    - For kernels that fuse a single GEMM with another non-GEMM operator (for example ReLU activation), set to [`2`{.docutils .literal .notranslate}]{.pre}.

    - For kernels that have no GEMMs, set to [`1`{.docutils .literal .notranslate}]{.pre}.

[`waves_per_eu=n`{.docutils .literal .notranslate}]{.pre}

:   Helps to manage Vector General Purpose Registers (VGPR) usage to achieve desired occupancy levels. This argument hints to the compiler to reduce VGPR to achieve [`n`{.docutils .literal .notranslate}]{.pre} occupancy where [`n`{.docutils .literal .notranslate}]{.pre} is a number. The goal is to achieve a certain occupancy level for each Execution Unit (EU, also called [[SIMD Unit]{.std .std-ref}](#mi300x-cu-fig){.reference .internal}) to achieve better latency or throughput. For more information on how to compute occupancy, see [[Compute the occupancy of a kernel]{.std .std-ref}](#mi300x-compute-kernel-occ){.reference .internal}.

    This argument is useful if:

    - The occupancy of the kernel is limited by VGPR usage, and

    - The current VGPR usage is only a few above a boundary in [[Occupancy related to VGPR usage in an Instinct MI300X GPU]{.std .std-ref}](#mi300x-occupancy-vgpr-table){.reference .internal}.

<figure id="id7" class="align-center">
<span id="mi300x-occupancy-vgpr-table"></span><img src="../../../_images/occupancy-vgpr.png" alt="Occupancy related to VGPR usage in an Instinct MI300X GPU." />
<figcaption><p><span class="caption-text">Occupancy related to VGPRs usage on an Instinct MI300X GPU</span><a href="#id7" class="headerlink" title="Link to this image">#</a></p></figcaption>
</figure>

For example, according to the table, each Execution Unit (EU) has 512 available VGPRs, which are allocated in blocks of 16. If the current VGPR usage is 170, it will be rounded up to 176 due to the allocation granularity. In this case, the occupancy is limited to 2 waves per EU because [\\(176 \\times 3 \> 512\\)]{.math .notranslate .nohighlight}. So, if you set [`waves_per_eu`{.docutils .literal .notranslate}]{.pre} to 3, the LLVM backend will attempt to reduce VGPR usage so that it might fit 3 waves per EU.

[`BLOCK_M`{.docutils .literal .notranslate}]{.pre}, [`BLOCK_N`{.docutils .literal .notranslate}]{.pre}, [`BLOCK_K`{.docutils .literal .notranslate}]{.pre}

:   Tile sizes to be tuned to balance the memory-to-computation ratio. The goal is to minimize the memory transfer from global to shared and reuse memory across different threads. This needs to be tuned. The tile sizes should be large enough to maximize the efficiency of the memory-to-computation ratio but small enough to parallelize the greatest number of workgroups at the grid level.

[`matrix_instr_nonkdim`{.docutils .literal .notranslate}]{.pre}

:   Experimental feature for Flash Attention-like kernels that determines the size of the Matrix Fused Multiply-Add (MFMA) instruction used.

    - [`matrix_instr_nonkdim`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`=`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`16`{.docutils .literal .notranslate}]{.pre}: [`mfma_16x16`{.docutils .literal .notranslate}]{.pre} is used.

    - [`matrix_instr_nonkdim`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`=`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`32`{.docutils .literal .notranslate}]{.pre}: [`mfma_32x32`{.docutils .literal .notranslate}]{.pre} is used.

    For GEMM kernels on an MI300X GPU, [`mfma_16x16`{.docutils .literal .notranslate}]{.pre} typically outperforms [`mfma_32x32`{.docutils .literal .notranslate}]{.pre}, even for large tile/GEMM sizes.
:::

::::: {#overall-gpu-resource-utilization .section}
[]{#mi300x-triton-gpu-utilization}

### Overall GPU resource utilization[\#](#overall-gpu-resource-utilization "Link to this heading"){.headerlink}

As depicted in the following figure, each XCD in [[MI300X]{.doc}](../../../conceptual/gpu-arch/mi300.html){.reference .internal} contains 40 compute units (CUs), with 38 active. Each MI300X contains eight vertical XCDs, and a total of 304 active compute units capable of parallel computation. The first consideration is the number of CUs a kernel can distribute its task across.

<figure id="id8" class="align-default">
<img src="../../../_images/xcd-sys-arch.png" alt="../../../_images/xcd-sys-arch.png" />
<figcaption><p><span class="caption-text">XCD-level system architecture showing 40 compute units, each with 32 KB L1 cache, a unified compute system with 4 ACE compute GPUs, shared 4MB of L2 cache, and a hardware scheduler (HWS).</span><a href="#id8" class="headerlink" title="Link to this image">#</a></p></figcaption>
</figure>

You can query hardware resources with the command [`rocminfo`{.docutils .literal .notranslate}]{.pre} in the [`/opt/rocm/bin`{.docutils .literal .notranslate}]{.pre} directory. For instance, query the number of CUs, number of SIMD, and wavefront size using the following commands.

:::: {.highlight-shell .notranslate}
::: highlight
    rocminfo | grep "Compute Unit"

    rocminfo | grep "SIMD"

    rocminfo | grep "Wavefront Size"
:::
::::

For the MI300X, the goal is to have a minimum of 1024 thread blocks or workgroups in the grid (kernel), with a preference for more.

Identifying additional parallelism within the algorithm is necessary to enhance GPU utilization. For more information and examples, see [Accelerating A Triton Fused Kernel For W4a16 Quantized Inference With SplitK Work Decomposition](https://arxiv.org/pdf/2402.00025v1){.reference .external}.
:::::

::::::: {#mlir-analysis .section}
[]{#mi300x-mlir-analysis}

### MLIR analysis[\#](#mlir-analysis "Link to this heading"){.headerlink}

Triton includes the following layouts: **blocked**, **shared**, **sliced**, and **MFMA**.

Use the Triton GPU Intermediate Representation (IR) to identify the memory in which each computation takes place.

Use the environment variable [`MLIR_ENABLE_DUMP`{.docutils .literal .notranslate}]{.pre} to dump MLIR:

:::: {.highlight-shell .notranslate}
::: highlight
    export MLIR_ENABLE_DUMP=1
:::
::::

The following is a snippet of IR from the Flash Attention decode [`int4`{.docutils .literal .notranslate}]{.pre} KV program. It is to de-quantize the [`int4`{.docutils .literal .notranslate}]{.pre} key-value from the [`int4`{.docutils .literal .notranslate}]{.pre} data type to [`fp16`{.docutils .literal .notranslate}]{.pre}.

:::: {.highlight-text .notranslate}
::: highlight
    %190 = tt.load %189 {cache = 1 : i32, evict = 1 : i32, isVolatile =
    false} : tensor<1x64xi32, #blocked6> loc(#loc159)

    %266 = arith.andi %190, %cst_28 : tensor<1x64xi32, #blocked6>
    loc(#loc250)

    %267 = arith.trunci %266 : tensor<1x64xi32, #blocked6> to
    tensor<1x64xi16, #blocked6> loc(#loc251)

    %268 = tt.bitcast %267 : tensor<1x64xi16, #blocked6> -> tensor<1x64xf16,
    #blocked6> loc(#loc252)

    %269 = triton_gpu.convert_layout %268 : (tensor<1x64xf16, #blocked6>) ->
    tensor<1x64xf16, #shared1> loc(#loc252)

    %270 = tt.trans %269 : (tensor<1x64xf16, #shared1>) -> tensor<64x1xf16,
    #shared2> loc(#loc194)

    %276 = triton_gpu.convert_layout %270 : (tensor<64x1xf16, #shared2>) ->
    tensor<64x1xf16, #blocked5> loc(#loc254)

    %293 = arith.mulf %276, %cst_30 : tensor<64x1xf16, #blocked5>
    loc(#loc254)

    %295 = arith.mulf %292, %294 : tensor<64x32xf16, #blocked5> loc(#loc264)

    %297 = arith.addf %295, %296 : tensor<64x32xf16, #blocked5> loc(#loc255)

    %298 = triton_gpu.convert_layout %297 : (tensor<64x32xf16, #blocked5>)
    -> tensor<64x32xf16, #shared1> loc(#loc255)

    %299 = tt.trans %298 : (tensor<64x32xf16, #shared1>) ->
    tensor<32x64xf16, #shared2> loc(#loc196)

    %300 = triton_gpu.convert_layout %299 : (tensor<32x64xf16, #shared2>) ->
    tensor<32x64xf16, #triton_gpu.dot_op<{opIdx = 1, parent = #mfma, kWidth
    = 4}>> loc(#loc197)
:::
::::

From the IR snippet, you can see [`i32`{.docutils .literal .notranslate}]{.pre} data is loaded from global memory to registers ([`%190`{.docutils .literal .notranslate}]{.pre}). With a few element-wise operations in registers, it is stored in shared memory ([`%269`{.docutils .literal .notranslate}]{.pre}) for the transpose operation ([`%270`{.docutils .literal .notranslate}]{.pre}), which needs data movement across different threads. With the transpose done, it is loaded from LDS to register again ([`%276`{.docutils .literal .notranslate}]{.pre}), and with a few more element-wise operations, it is stored to LDS again ([`%298`{.docutils .literal .notranslate}]{.pre}). The last step loads from LDS to registers and converts to the dot-operand layout ([`%300`{.docutils .literal .notranslate}]{.pre}).

The IR snippet uses the LDS twice. The first is for the transpose, and the second is to convert a blocked layout to a dot operand layout. There's an opportunity to optimize performance by using LDS once.
:::::::

::: {#isa-assembly-analysis .section}
[]{#mi300x-assembly-analysis}

### ISA assembly analysis[\#](#isa-assembly-analysis "Link to this heading"){.headerlink}

To generate ISA, [`export`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`AMDGCN_ENABLE_DUMP=1`{.docutils .literal .notranslate}]{.pre} when running the Triton program. The generated ISA will be printed as standard output. You can dump it to a file for analysis.

- Ensure [`global_load_dwordx4`{.docutils .literal .notranslate}]{.pre} is used in the ISA, especially when the global memory load happens in the loop.

- In most cases, the LDS load and store should use [`_b128`{.docutils .literal .notranslate}]{.pre} to minimize the number of LDS access instructions.

- The AMD ISA has [`s_waitcnt`{.docutils .literal .notranslate}]{.pre} instruction to synchronize the dependency of memory access and computations. The [`s_waitcnt`{.docutils .literal .notranslate}]{.pre} instructions can typically have two signals in the Triton context:

  - [`lgkmcnt(n)`{.docutils .literal .notranslate}]{.pre}: [`lgkm`{.docutils .literal .notranslate}]{.pre} stands for LDS, GDS (Global Data Share), Constant, and Message. It is often related to LDS access. The [`n`{.docutils .literal .notranslate}]{.pre} indicates the number of data accesses can still be ongoing before moving on to the next step. For example, if [`n`{.docutils .literal .notranslate}]{.pre} is [`0`{.docutils .literal .notranslate}]{.pre}, wait for all [`lgkm`{.docutils .literal .notranslate}]{.pre} access to finish before continuing. If [`n`{.docutils .literal .notranslate}]{.pre} is [`1`{.docutils .literal .notranslate}]{.pre}, move on even if [`1`{.docutils .literal .notranslate}]{.pre} [`lgkm`{.docutils .literal .notranslate}]{.pre} access is still running asynchronously.

  - [`vmcnt(n)`{.docutils .literal .notranslate}]{.pre}: [`vm`{.docutils .literal .notranslate}]{.pre} represents vector memory. This happens when vector memory is accessed, for example, when global load moves from global memory to vector memory. The variable [`n`{.docutils .literal .notranslate}]{.pre} is the same as the previous setting.

Generally recommended guidelines are as follows.

- Vectorize memory access as much as possible.

- Ensure synchronization is done efficiently.

- Overlap of instructions to hide latency, but it requires thoughtful analysis of the algorithms.

- If you find inefficiencies, you can trace it back to LLVM IR, TTGIR and even TTIR to see where the problem comes from. If you find it during compiler optimization, activate the MLIR dump ([`export`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`MLIR_ENABLE_DUMP=1`{.docutils .literal .notranslate}]{.pre}) and check which optimization pass caused the problem.
:::
:::::::::::::

::::: {#hip-performance-optimization .section}
[]{#mi300x-hip-optimization}

## HIP performance optimization[\#](#hip-performance-optimization "Link to this heading"){.headerlink}

This section summarizes the best practices described in the [[Performance guidelines]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/performance_guidelines.html "(in HIP Documentation v7.2.53211)"){.reference .external} section of the HIP documentation.

Optimization areas of concern include:

- Parallel execution

- Memory usage optimization

- Optimization for maximum throughput

- Minimizing memory thrashing

::: {#parallel-execution-and-gpu-hardware-utilization .section}
### Parallel execution and GPU hardware utilization[\#](#parallel-execution-and-gpu-hardware-utilization "Link to this heading"){.headerlink}

The application should reveal and efficiently imply as much parallelism as possible for optimal use to keep all system components active.
:::

::: {#memory-usage-optimization .section}
### Memory usage optimization[\#](#memory-usage-optimization "Link to this heading"){.headerlink}

To optimize memory throughput, minimize low-bandwidth data transfers, particularly between the host and device. Maximize on-chip memory, including shared memory and caches, to reduce data transfers between global memory and the device.

In a GPU, global memory has high latency but a large size, while local data share (LDS) has lower latency but a smaller size, and registers have the fastest but smallest access. Aim to limit load/store operations in global memory. If multiple threads in a block need the same data, transfer it from global memory to LDS for efficient access.

See [[HIP's performance guidelines]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/performance_guidelines.html "(in HIP Documentation v7.2.53211)"){.reference .external} for greater detail.
:::
:::::

::::::::::::: {#diagnostic-and-performance-analysis .section}
## Diagnostic and performance analysis[\#](#diagnostic-and-performance-analysis "Link to this heading"){.headerlink}

::::::::::: {#debug-memory-access-faults .section}
[]{#mi300x-rocr-debug-agent}

### Debug memory access faults[\#](#debug-memory-access-faults "Link to this heading"){.headerlink}

Identifying a faulting kernel is often enough to triage a memory access fault. The ROCr Debug Agent can trap a memory access fault and provide a dump of all active wavefronts that caused the error, as well as the name of the kernel. For more information, see [[ROCr Debug Agent documentation]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocr_debug_agent/en/latest/index.html "(in rocr_debug_agent v2.1.0)"){.reference .external}.

To summarize, the key points include:

1.  Compiling with [`-ggdb`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-O0`{.docutils .literal .notranslate}]{.pre} is recommended but not required.

2.  [`HSA_TOOLS_LIB=/opt/rocm/lib/librocm-debug-agent.so.2`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`HSA_ENABLE_DEBUG=1`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`./my_program`{.docutils .literal .notranslate}]{.pre}

When the debug agent traps the fault, it produces verbose output of all wavefront registers and memory content. Importantly, it also prints something similar to the following:

:::: {.highlight-text .notranslate}
::: highlight
    Disassembly for function vector_add_assert_trap(int*, int*, int*):

    code object:
    file:////rocm-debug-agent/build/test/rocm-debug-agent-test#offset=14309&size=31336

    loaded at: [0x7fd4f100c000-0x7fd4f100e070]
:::
::::

The kernel name and the code object file should be listed. In the example above, the kernel name is vector_add_assert_trap, but this might also look like:

:::: {.highlight-text .notranslate}
::: highlight
    Disassembly for function memory:///path/to/codeobject#offset=1234&size=567:
:::
::::

In this case, it's an in-memory kernel that was generated at runtime. Using the environment variable [`ROCM_DEBUG_AGENT_OPTIONS="--all`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--save-code-objects"`{.docutils .literal .notranslate}]{.pre} will have the debug agent save all code objects to the current directory. Use [`--save-code-objects=[DIR]`{.docutils .literal .notranslate}]{.pre} to save them in another location.

The code objects will be renamed from the URI format with special characters replaced by '\_'. Use [`llvm-objdump`{.docutils .literal .notranslate}]{.pre} to disassemble the indicated in-memory code object that has been saved to disk. The name of the kernel is often found in the disassembled code object.

:::: {.highlight-shell .notranslate}
::: highlight
    llvm-objdump --disassemble-all path/to/code-object.co
:::
::::

Disabling memory caching strategies within the ROCm stack and PyTorch is recommended, where possible. This gives the debug agent the best chance of finding the memory fault where it originates. Otherwise, it could be masked by writing past the end of a cached block within a larger allocation.

:::: {.highlight-text .notranslate}
::: highlight
    PYTORCH_NO_HIP_MEMORY_CACHING=1

    HSA_DISABLE_FRAGMENT_ALLOCATOR=1
:::
::::
:::::::::::

::: {#compute-the-occupancy-of-a-kernel .section}
[]{#mi300x-compute-kernel-occ}

### Compute the occupancy of a kernel[\#](#compute-the-occupancy-of-a-kernel "Link to this heading"){.headerlink}

1.  Get the VGPR count, search for [`.vgpr_count`{.docutils .literal .notranslate}]{.pre} in the ISA (for example, [`N`{.docutils .literal .notranslate}]{.pre}).

2.  Get the allocated LDS following the steps (for example, L for the kernel).

    1.  [`export`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`MLIR_ENABLE_DUMP=1`{.docutils .literal .notranslate}]{.pre}

    2.  [`rm`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-rf`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`~/.triton/cache`{.docutils .literal .notranslate}]{.pre}

    3.  [`python`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`kernel.py`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`|`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`|`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`grep`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`"triton_gpu.shared`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`=`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`"`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`|`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`tail`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-n`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`1`{.docutils .literal .notranslate}]{.pre}

    4.  You should see something like [`triton_gpu.shared`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`=`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`65536`{.docutils .literal .notranslate}]{.pre}, indicating 65536 bytes of LDS are allocated for the kernel.

3.  Get number of waves per workgroup using the following steps (for example, [`nW`{.docutils .literal .notranslate}]{.pre}).

    1.  [`export`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`MLIR_ENABLE_DUMP=1`{.docutils .literal .notranslate}]{.pre}

    2.  [`rm`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-rf`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`~/.triton/cache`{.docutils .literal .notranslate}]{.pre}

    3.  [`python`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`kernel.py`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`|`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`|`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`grep`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`"triton_gpu.num-warps`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`"`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`|`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`tail`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-n`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`1`{.docutils .literal .notranslate}]{.pre}

    4.  You should see something like [`“triton_gpu.num-warps"`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`=`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`8`{.docutils .literal .notranslate}]{.pre}, indicating 8 waves per workgroup.

4.  Compute occupancy limited by VGPR based on N according to the [[preceding table]{.std .std-ref}](#mi300x-occupancy-vgpr-table){.reference .internal}. For example, waves per EU as [`occ_vgpr`{.docutils .literal .notranslate}]{.pre}.

5.  Compute occupancy limited by LDS based on L by: [`occ_lds`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`=`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`floor(65536`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`/`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`L)`{.docutils .literal .notranslate}]{.pre}.

6.  Then the occupancy is [`occ`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`=`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`min(floor(occ_vgpr`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`4`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`/`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`nW),`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`occ_lds)`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`nW`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`/`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`4`{.docutils .literal .notranslate}]{.pre}

    1.  [`occ_vgpr`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`\*`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`4`{.docutils .literal .notranslate}]{.pre} gives the total number of waves on all 4 execution units (SIMDs) per CU.

    2.  [`floor(occ_vgpr`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`4`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`/`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`nW)`{.docutils .literal .notranslate}]{.pre} gives the occupancy of workgroups per CU regrading VGPR usage.

    3.  The true [`occ`{.docutils .literal .notranslate}]{.pre} is the minimum of the two.

Find the full [`occ.sh`{.docutils .literal .notranslate}]{.pre} at [ROCm/triton](https://github.com/ROCm/triton/blob/triton-mlir/scripts/amd/occ.sh){.github .reference .external}.
:::
:::::::::::::

::::: {#special-considerations .section}
## Special considerations[\#](#special-considerations "Link to this heading"){.headerlink}

::: {#multi-gpu-communications .section}
### Multi-GPU communications[\#](#multi-gpu-communications "Link to this heading"){.headerlink}

Because of the characteristics of MI300X inter-GPU communication and limitation of bandwidth between and among 2 GPUs and 4 GPUs, avoid running workloads that use 2 or 4 GPU collectives. It's optimal to either use a single GPU (where no collective is required) or employ 8 GPU collectives.
:::

::: {#multi-node-fsdp-and-rccl-settings .section}
### Multi-node FSDP and RCCL settings[\#](#multi-node-fsdp-and-rccl-settings "Link to this heading"){.headerlink}

When using PyTorch's FSDP (Full Sharded Data Parallel) feature, the HIP streams used by RCCL and HIP streams used for compute kernels do not always overlap well. As a workaround, it's recommended to use high-priority HIP streams with RCCL.

To configure high-priority streams:

- Set environment variable [`TORCH_NCCL_HIGH_PRIORITY=1`{.docutils .literal .notranslate}]{.pre} to force all RCCL streams to be high-priority.

- Set environment variable [`GPU_MAX_HW_QUEUES=2`{.docutils .literal .notranslate}]{.pre} via the HIP runtime library.

Hardware efficiency is maximized with 4 or fewer HIP streams. These environment variables limit the configuration to two compute streams and two RCCL streams, aligning with this best practice. Additionally, RCCL is often pre-optimized for MI300 systems in production by querying the node topology during startup, reducing the need for extensive manual tuning.
:::
:::::

::: {#further-reading .section}
## Further reading[\#](#further-reading "Link to this heading"){.headerlink}

- [[vLLM V1 performance optimization]{.doc}](vllm-optimization.html){.reference .internal}
:::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::: prev-next-area
[](profiling-and-debugging.html "previous page"){.left-prev}

::: prev-next-info
previous

Profiling and debugging
:::

[](vllm-optimization.html "next page"){.right-next}

::: prev-next-info
next

vLLM V1 performance optimization
:::
:::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::: {.bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {.page-toc .tocsection .onthispage}
Contents
:::

- [Workload tuning strategy](#workload-tuning-strategy){.reference .internal .nav-link}
  - [Measure the current workload](#measure-the-current-workload){.reference .internal .nav-link}
  - [Identify tuning requirements](#mi300x-profiling-start){.reference .internal .nav-link}
    - [High-level profiling tools](#high-level-profiling-tools){.reference .internal .nav-link}
    - [Kernel-level profiling tools](#kernel-level-profiling-tools){.reference .internal .nav-link}
  - [Analyze and tune](#analyze-and-tune){.reference .internal .nav-link}
    - [Optimize model inference with vLLM](#optimize-model-inference-with-vllm){.reference .internal .nav-link}
    - [Auto-tunable configurations](#auto-tunable-configurations){.reference .internal .nav-link}
    - [Manual tuning](#manual-tuning){.reference .internal .nav-link}
  - [Iterate and validate](#iterate-and-validate){.reference .internal .nav-link}
- [Profiling tools](#profiling-tools){.reference .internal .nav-link}
  - [PyTorch Profiler](#pytorch-profiler){.reference .internal .nav-link}
  - [ROCm profiling tools](#rocm-profiling-tools){.reference .internal .nav-link}
    - [ROCProfiler](#rocprofiler){.reference .internal .nav-link}
    - [ROCm Compute Profiler](#rocm-compute-profiler){.reference .internal .nav-link}
    - [ROCm Systems Profiler](#rocm-systems-profiler){.reference .internal .nav-link}
- [vLLM performance optimization](#vllm-performance-optimization){.reference .internal .nav-link}
- [PyTorch TunableOp](#pytorch-tunableop){.reference .internal .nav-link}
  - [Workflow](#workflow){.reference .internal .nav-link}
  - [Offline tuning](#offline-tuning){.reference .internal .nav-link}
- [PyTorch inductor max-autotune tuning knobs](#pytorch-inductor-max-autotune-tuning-knobs){.reference .internal .nav-link}
  - [Triton backend](#triton-backend){.reference .internal .nav-link}
  - [Composable Kernel backend](#composable-kernel-backend){.reference .internal .nav-link}
- [ROCm library tuning](#rocm-library-tuning){.reference .internal .nav-link}
  - [GEMM (general matrix multiplication)](#gemm-general-matrix-multiplication){.reference .internal .nav-link}
    - [hipBLASLt benchmarking](#hipblaslt-benchmarking){.reference .internal .nav-link}
    - [hipBLASLt auto-tuning using hipblaslt-bench](#hipblaslt-auto-tuning-using-hipblaslt-bench){.reference .internal .nav-link}
      - [Prerequisite](#prerequisite){.reference .internal .nav-link}
      - [Quick start](#quick-start){.reference .internal .nav-link}
      - [Output](#output){.reference .internal .nav-link}
      - [A quick view of the config YAML](#a-quick-view-of-the-config-yaml){.reference .internal .nav-link}
    - [hipBLASLt backend assembly generator tuning](#hipblaslt-backend-assembly-generator-tuning){.reference .internal .nav-link}
      - [config.yaml](#config-yaml){.reference .internal .nav-link}
  - [TensileLite tuning flow](#tensilelite-tuning-flow){.reference .internal .nav-link}
    - [Step 1: Initial solution parameters](#step-1-initial-solution-parameters){.reference .internal .nav-link}
    - [Step 2: Benchmark common parameters](#step-2-benchmark-common-parameters){.reference .internal .nav-link}
    - [Step 3: Fork parameters](#step-3-fork-parameters){.reference .internal .nav-link}
    - [Step 4: Benchmark fork parameters](#step-4-benchmark-fork-parameters){.reference .internal .nav-link}
    - [Step 5: Join parameters](#step-5-join-parameters){.reference .internal .nav-link}
    - [Step 6: Benchmark join parameters](#step-6-benchmark-join-parameters){.reference .internal .nav-link}
    - [Step 7: Benchmark final parameters](#step-7-benchmark-final-parameters){.reference .internal .nav-link}
  - [Update logic YAML files](#update-logic-yaml-files){.reference .internal .nav-link}
    - [Tensile optimization and performance tuning tips](#tensile-optimization-and-performance-tuning-tips){.reference .internal .nav-link}
    - [Optimizing Composable Kernel GEMM kernels](#optimizing-composable-kernel-gemm-kernels){.reference .internal .nav-link}
  - [MIOpen](#miopen){.reference .internal .nav-link}
    - [Convolution](#convolution){.reference .internal .nav-link}
    - [Tuning in MIOpen](#tuning-in-miopen){.reference .internal .nav-link}
    - [Finding the fastest kernel](#finding-the-fastest-kernel){.reference .internal .nav-link}
  - [RCCL](#rccl){.reference .internal .nav-link}
    - [Use all eight GPUs](#use-all-eight-gpus){.reference .internal .nav-link}
    - [Disable NUMA auto-balancing](#disable-numa-auto-balancing){.reference .internal .nav-link}
    - [Disable ACS for multi-node RCCL](#disable-acs-for-multi-node-rccl){.reference .internal .nav-link}
    - [Run RCCL-Unittests](#run-rccl-unittests){.reference .internal .nav-link}
    - [NPKit profiler](#npkit-profiler){.reference .internal .nav-link}
    - [RCCL-tests](#rccl-tests){.reference .internal .nav-link}
    - [Use one-process-per-GPU mode](#use-one-process-per-gpu-mode){.reference .internal .nav-link}
    - [RCCL in E2E workloads](#rccl-in-e2e-workloads){.reference .internal .nav-link}
- [Triton kernel performance optimization](#triton-kernel-performance-optimization){.reference .internal .nav-link}
  - [Auto-tunable kernel configurations](#auto-tunable-kernel-configurations){.reference .internal .nav-link}
  - [Overall GPU resource utilization](#overall-gpu-resource-utilization){.reference .internal .nav-link}
  - [MLIR analysis](#mlir-analysis){.reference .internal .nav-link}
  - [ISA assembly analysis](#isa-assembly-analysis){.reference .internal .nav-link}
- [HIP performance optimization](#hip-performance-optimization){.reference .internal .nav-link}
  - [Parallel execution and GPU hardware utilization](#parallel-execution-and-gpu-hardware-utilization){.reference .internal .nav-link}
  - [Memory usage optimization](#memory-usage-optimization){.reference .internal .nav-link}
- [Diagnostic and performance analysis](#diagnostic-and-performance-analysis){.reference .internal .nav-link}
  - [Debug memory access faults](#debug-memory-access-faults){.reference .internal .nav-link}
  - [Compute the occupancy of a kernel](#compute-the-occupancy-of-a-kernel){.reference .internal .nav-link}
- [Special considerations](#special-considerations){.reference .internal .nav-link}
  - [Multi-GPU communications](#multi-gpu-communications){.reference .internal .nav-link}
  - [Multi-node FSDP and RCCL settings](#multi-node-fsdp-and-rccl-settings){.reference .internal .nav-link}
- [Further reading](#further-reading){.reference .internal .nav-link}
::::
:::::
::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
