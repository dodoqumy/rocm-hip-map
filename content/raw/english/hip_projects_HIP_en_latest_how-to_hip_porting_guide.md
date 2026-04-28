---
title: "Porting CUDA code to HIP"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_porting_guide.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-04-28
---

::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}

::: header-article-item
- [](../index.html){.nav-link aria-label="Home"}
- Porting\...

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons
[]{.fa-solid .fa-list}

# Porting CUDA code to HIP

## Contents

- [Porting a CUDA project](#porting-a-cuda-project){.reference .internal .nav-link}
  - [General tips](#general-tips){.reference .internal .nav-link}
- [Using HIPIFY](#using-hipify){.reference .internal .nav-link}
  - [Memory copy functions](#memory-copy-functions){.reference .internal .nav-link}
  - [Address spaces](#address-spaces){.reference .internal .nav-link}
  - [Context stack behavior differences](#context-stack-behavior-differences){.reference .internal .nav-link}
  - [Scanning CUDA source to scope the translation](#scanning-cuda-source-to-scope-the-translation){.reference .internal .nav-link}
  - [Automatically converting a CUDA project](#automatically-converting-a-cuda-project){.reference .internal .nav-link}
- [Library and driver equivalents](#library-and-driver-equivalents){.reference .internal .nav-link}
  - [cuModule and hipModule](#cumodule-and-hipmodule){.reference .internal .nav-link}
    - [Using hipModuleLaunchKernel](#using-hipmodulelaunchkernel){.reference .internal .nav-link}
  - [cuCtx and hipCtx](#cuctx-and-hipctx){.reference .internal .nav-link}
- [Compilation](#compilation){.reference .internal .nav-link}
  - [HIP Headers](#hip-headers){.reference .internal .nav-link}
  - [Using a Standard C++ Compiler](#using-a-standard-c-compiler){.reference .internal .nav-link}
  - [Compiler defines for HIP](#compiler-defines-for-hip){.reference .internal .nav-link}
  - [Identifying host or device compilation pass](#identifying-compiler-target){.reference .internal .nav-link}
- [HIP-Clang implementation notes](#hip-clang-implementation-notes){.reference .internal .nav-link}
  - [Initialization and termination functions](#initialization-and-termination-functions){.reference .internal .nav-link}
  - [Kernel launching](#kernel-launching){.reference .internal .nav-link}
  - [Compilation options for hipModuleLoadDataEx](#compilation-options-for-hipmoduleloaddataex){.reference .internal .nav-link}
- [Identifying device architecture and features](#identifying-device-architecture-features){.reference .internal .nav-link}
  - [Device code feature identification](#device-code-feature-identification){.reference .internal .nav-link}
  - [Host code feature identification](#host-code-feature-identification){.reference .internal .nav-link}
  - [Feature macros and properties](#feature-macros-and-properties){.reference .internal .nav-link}
- [warpSize](#warpsize){.reference .internal .nav-link}
- [Lane masks bit-shift](#lane-masks-bit-shift){.reference .internal .nav-link}
- [Porting from CUDA \_\_launch_bounds\_\_](#porting-from-cuda-launch-bounds){.reference .internal .nav-link}
  - [maxregcount](#maxregcount){.reference .internal .nav-link}
- [Driver entry point access](#driver-entry-point-access){.reference .internal .nav-link}
  - [Address retrieval](#address-retrieval){.reference .internal .nav-link}
  - [Per-thread default stream version request](#per-thread-default-stream-version-request){.reference .internal .nav-link}
  - [Accessing HIP features with a newer driver](#accessing-hip-features-with-a-newer-driver){.reference .internal .nav-link}
- [Memory type identification](#memory-type-identification){.reference .internal .nav-link}



# Porting CUDA code to HIP[\#](#porting-cuda-code-to-hip "Link to this heading"){.headerlink}

HIP is a C++ runtime API and kernel language for AMD GPUs. It allows developers to convert existing NVIDIA CUDA code to run on AMD GPUs. This topic describes the available tools and provides practical suggestions for porting your CUDA code and working through common issues.

CUDA provides separate driver and runtime APIs, while HIP mostly uses a single API. The two CUDA APIs generally provide similar functionality and are mostly interchangeable. However, the CUDA driver API provides fine-grained control over kernel-level initialization, contexts, and module management, while the runtime API automatically manages contexts and modules. The driver API is suitable for applications that require tight integration with other systems or advanced control over GPU resources.

- Driver API calls begin with the prefix [`cu`{.docutils .literal .notranslate}]{.pre}, while runtime API calls begin with the prefix [`cuda`{.docutils .literal .notranslate}]{.pre}. For example, the driver API contains [`cuEventCreate`{.docutils .literal .notranslate}]{.pre}, while the runtime API contains [`cudaEventCreate`{.docutils .literal .notranslate}]{.pre}, which has similar functionality.

- The driver API offers two additional low-level functionalities not exposed by the runtime API: module management [`cuModule*`{.docutils .literal .notranslate}]{.pre} and context management [`cuCtx*`{.docutils .literal .notranslate}]{.pre} APIs.

The HIP runtime API includes corresponding functions for both the CUDA driver and the CUDA runtime API. The module and context functionality are available with the [`hipModule`{.docutils .literal .notranslate}]{.pre} and [`hipCtx`{.docutils .literal .notranslate}]{.pre} prefixes, and driver API functions are usually prefixed with [`hipDrv`{.docutils .literal .notranslate}]{.pre}.

## Porting a CUDA project[\#](#porting-a-cuda-project "Link to this heading"){.headerlink}

HIP provides a runtime API for AMD GPUs that closely mirrors CUDA, making it straightforward to port existing CUDA applications. To compile HIP code for AMD platforms, you can use [`amdclang++`{.docutils .literal .notranslate}]{.pre}, also called HIP-Clang, or you can use [`hipcc`{.docutils .literal .notranslate}]{.pre} which offers a higher-level compiler interface.

### General tips[\#](#general-tips "Link to this heading"){.headerlink}

- Use the [HIPIFY](https://github.com/ROCm/HIPIFY){.reference .external} tools to automatically convert CUDA code to HIP, as described in the following section.

- Start with a working CUDA codebase before beginning the porting process.

- Port the application incrementally and test each section as you convert it.

- HIP code runs on AMD GPUs and takes advantage of the ROCm software stack for both performance and tooling support.

## Using HIPIFY[\#](#using-hipify "Link to this heading"){.headerlink}

[[HIPIFY]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/HIPIFY/en/latest/index.html "(in HIPIFY Documentation)"){.reference .external} is a collection of tools that automatically translate CUDA code to HIP code. For example, [`cuEventCreate`{.docutils .literal .notranslate}]{.pre} is translated to [[`hipEventCreate()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../reference/hip_runtime_api/modules/event_management.html#_CPPv414hipEventCreateP10hipEvent_t "hipEventCreate"){.reference .internal}. HIPIFY tools also convert error codes from the driver namespace and coding conventions to the equivalent HIP error code. HIP unifies the APIs for these common functions.

There are two types of HIPIFY available:

- [[hipify-clang]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/HIPIFY/en/latest/how-to/hipify-clang.html "(in HIPIFY Documentation)"){.reference .external} is a Clang-based tool that parses code, translates it into an Abstract Syntax Tree, and generates the HIP source. For this, [`hipify-clang`{.docutils .literal .notranslate}]{.pre} needs to be able to actually compile the code, so the CUDA code needs to be correct, and a CUDA install with all necessary headers must be provided.

- [[hipify-perl]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/HIPIFY/en/latest/how-to/hipify-perl.html "(in HIPIFY Documentation)"){.reference .external} uses pattern matching, to translate the CUDA code to HIP. It does not require a working CUDA installation, and can also convert CUDA code, that is not syntactically correct. It is therefore easier to set up and use, but is not as powerful as [`hipify-clang`{.docutils .literal .notranslate}]{.pre}.

### Memory copy functions[\#](#memory-copy-functions "Link to this heading"){.headerlink}

When copying memory, the CUDA driver includes the memory direction in the name of the API ([`cuMemcpyHtoD`{.docutils .literal .notranslate}]{.pre}), while the CUDA runtime API provides a single memory copy API with a parameter that specifies the direction. It also supports a default direction where the runtime determines the direction automatically.

HIP provides both versions, for example, [[`hipMemcpyHtoD()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../reference/hip_runtime_api/modules/memory_management.html#_CPPv413hipMemcpyHtoD14hipDeviceptr_tPKv6size_t "hipMemcpyHtoD"){.reference .internal} as well as [[`hipMemcpy()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../reference/hip_runtime_api/modules/memory_management.html#_CPPv49hipMemcpyPvPKv6size_t13hipMemcpyKind "hipMemcpy"){.reference .internal}. The first version might be faster in some cases because it avoids any host overhead to detect the direction of the memory copy.

### Address spaces[\#](#address-spaces "Link to this heading"){.headerlink}

HIP-Clang defines a process-wide address space where the CPU and all devices allocate addresses from a single unified pool. This means addresses can be shared between contexts. A new context does not create a new address space for the device.

### Context stack behavior differences[\#](#context-stack-behavior-differences "Link to this heading"){.headerlink}

HIP-Clang creates a primary context when the HIP API is first invoked. It then pushes this primary context onto the context stack if the stack is empty. This behavior differs from the CUDA driver API, where contexts often need to be managed explicitly.

### Scanning CUDA source to scope the translation[\#](#scanning-cuda-source-to-scope-the-translation "Link to this heading"){.headerlink}

The [`--examine`{.docutils .literal .notranslate}]{.pre} option, tells the hipify tools to do a test-run without changing the source files, but instead scanning the files to determine which files contain CUDA code and how much of that code can automatically be hipified.

There also are [`hipexamine-perl.sh`{.docutils .literal .notranslate}]{.pre} or [`hipexamine.sh`{.docutils .literal .notranslate}]{.pre} (for [`hipify-clang`{.docutils .literal .notranslate}]{.pre}) scripts to automatically scan directories.

For example, the following is a scan of one of the [`convolutionSeparable`{.docutils .literal .notranslate}]{.pre} sample from [cuda-samples](https://github.com/NVIDIA/cuda-samples){.reference .external}:

::: highlight
    > cd Samples/2_Concepts_and_Techniques/convolutionSeparable/
    > hipexamine-perl.sh
    [HIPIFY] info: file './convolutionSeparable.cu' statistics:
      CONVERTED refs count: 2
      TOTAL lines of code: 214
      WARNINGS: 0
    [HIPIFY] info: CONVERTED refs by names:
      cooperative_groups.h => hip/hip_cooperative_groups.h: 1
      cudaMemcpyToSymbol => hipMemcpyToSymbol: 1

    [HIPIFY] info: file './main.cpp' statistics:
      CONVERTED refs count: 13
      TOTAL lines of code: 174
      WARNINGS: 0
    [HIPIFY] info: CONVERTED refs by names:
      cudaDeviceSynchronize => hipDeviceSynchronize: 2
      cudaFree => hipFree: 3
      cudaMalloc => hipMalloc: 3
      cudaMemcpy => hipMemcpy: 2
      cudaMemcpyDeviceToHost => hipMemcpyDeviceToHost: 1
      cudaMemcpyHostToDevice => hipMemcpyHostToDevice: 1
      cuda_runtime.h => hip/hip_runtime.h: 1

    [HIPIFY] info: file 'GLOBAL' statistics:
      CONVERTED refs count: 15
      TOTAL lines of code: 512
      WARNINGS: 0
    [HIPIFY] info: CONVERTED refs by names:
      cooperative_groups.h => hip/hip_cooperative_groups.h: 1
      cudaDeviceSynchronize => hipDeviceSynchronize: 2
      cudaFree => hipFree: 3
      cudaMalloc => hipMalloc: 3
      cudaMemcpy => hipMemcpy: 2
      cudaMemcpyDeviceToHost => hipMemcpyDeviceToHost: 1
      cudaMemcpyHostToDevice => hipMemcpyHostToDevice: 1
      cudaMemcpyToSymbol => hipMemcpyToSymbol: 1
      cuda_runtime.h => hip/hip_runtime.h: 1

[`hipexamine-perl.sh`{.docutils .literal .notranslate}]{.pre} reports how many CUDA calls are going to be converted to HIP (e.g. [`CONVERTED`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`refs`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`count:`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`2`{.docutils .literal .notranslate}]{.pre}), and lists them by name together with their corresponding HIP-version (see the lines following [`[HIPIFY]`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`info:`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`CONVERTED`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`refs`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`by`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`names:`{.docutils .literal .notranslate}]{.pre}). It also lists the total lines of code for the file and potential warnings. In the end it prints a summary for all files.

### Automatically converting a CUDA project[\#](#automatically-converting-a-cuda-project "Link to this heading"){.headerlink}

To directly replace the files, the [`--inplace`{.docutils .literal .notranslate}]{.pre} option of [`hipify-perl`{.docutils .literal .notranslate}]{.pre} or [`hipify-clang`{.docutils .literal .notranslate}]{.pre} can be used. This creates a backup of the original files in a [`<filename>.prehip`{.docutils .literal .notranslate}]{.pre} file and overwrites the existing files, keeping their file endings. If the [`--inplace`{.docutils .literal .notranslate}]{.pre} option is not given, the scripts print the hipified code to [`stdout`{.docutils .literal .notranslate}]{.pre}.

[`hipconvertinplace.sh`{.docutils .literal .notranslate}]{.pre} or [`hipconvertinplace-perl.sh`{.docutils .literal .notranslate}]{.pre} operate on whole directories.

## Library and driver equivalents[\#](#library-and-driver-equivalents "Link to this heading"){.headerlink}

ROCm provides libraries to ease porting of code relying on CUDA libraries or the CUDA driver API. Most CUDA libraries have a corresponding HIP library. For more information, see either [[ROCm libraries]{.xref .std .std-doc}](https://rocm.docs.amd.com/en/latest/reference/api-libraries.html "(in ROCm Documentation v7.2.2)"){.reference .external} or [[HIPIFY CUDA compatible libraries]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/HIPIFY/en/latest/reference/supported_apis.html "(in HIPIFY Documentation)"){.reference .external}.

ROCm provides two categories of libraries: those prefixed with [`hip`{.docutils .literal .notranslate}]{.pre} and those prefixed with [`roc`{.docutils .literal .notranslate}]{.pre}. While both are implemented using HIP, the [`roc`{.docutils .literal .notranslate}]{.pre} libraries are optimized specifically for AMD GPUs and may use AMD-specific features to deliver the best performance.

In the case where a library provides both [`roc`{.docutils .literal .notranslate}]{.pre} and [`hip`{.docutils .literal .notranslate}]{.pre} versions, such as [`hipSparse`{.docutils .literal .notranslate}]{.pre} and [`rocSparse`{.docutils .literal .notranslate}]{.pre}, it is recommended to use the [`roc`{.docutils .literal .notranslate}]{.pre} version for applications running on AMD GPUs, as they are optimized for AMD architectures.

Note

For applications running on AMD GPUs, it is recommended to use the [`roc`{.docutils .literal .notranslate}]{.pre}-libraries. In hipify tools, this can be accomplished using the [`--roc`{.docutils .literal .notranslate}]{.pre} option.

### cuModule and hipModule[\#](#cumodule-and-hipmodule "Link to this heading"){.headerlink}

The [`cuModule`{.docutils .literal .notranslate}]{.pre} feature of the driver API provides additional control over how and when accelerator code objects are loaded. For example, the driver API enables code objects to be loaded from files or memory pointers. Symbols for kernels or global data are extracted from the loaded code objects. In contrast, the runtime API loads automatically and, if necessary, compiles all the kernels from an executable binary when it runs.

The Module features are useful in an environment that generates the code objects directly, such as a new accelerator language front end. Other environments have many kernels and don't want all of them to be loaded automatically. The Module functions load the generated code objects and launch kernels.

Like the [`cuModule`{.docutils .literal .notranslate}]{.pre} API, the [`hipModule`{.docutils .literal .notranslate}]{.pre} API provides additional control over code object management, including options to load code from files or from in-memory pointers.

HIP-Clang uses the [`hsaco`{.docutils .literal .notranslate}]{.pre} format for code objects. The following table summarizes the formats used:

::: pst-scrollable-table-container
  Format        APIs                                                                                                                     HIP-CLANG
  ------------- ------------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------
  Code object   [`hipModuleLoad`{.docutils .literal .notranslate}]{.pre}, [`hipModuleLoadData`{.docutils .literal .notranslate}]{.pre}   [`.hsaco`{.docutils .literal .notranslate}]{.pre}
  Fat binary    [`hipModuleLoadFatBin`{.docutils .literal .notranslate}]{.pre}                                                           [`.hip_fatbin`{.docutils .literal .notranslate}]{.pre}


[`hipcc`{.docutils .literal .notranslate}]{.pre} uses HIP-Clang to compile host code. The compiler can embed code objects into the final executable. These code objects are automatically loaded when the application starts. The [`hipModule`{.docutils .literal .notranslate}]{.pre} API can be used to load additional code objects. When used this way, it extends the capability of the automatically loaded code objects. HIP-Clang enables both of these capabilities to be used together. Of course, it is possible to create a program with no kernels and no automatic loading.

For [`hipModule`{.docutils .literal .notranslate}]{.pre} API reference content, see [[Module management]{.std .std-ref}](../reference/hip_runtime_api/modules/module_management.html#module-management-reference){.reference .internal}.

#### Using hipModuleLaunchKernel[\#](#using-hipmodulelaunchkernel "Link to this heading"){.headerlink}

Both CUDA driver and runtime APIs define a function for launching kernels, called [`cuLaunchKernel`{.docutils .literal .notranslate}]{.pre} or [`cudaLaunchKernel`{.docutils .literal .notranslate}]{.pre}. The equivalent API in HIP is [[`hipModuleLaunchKernel()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../reference/hip_runtime_api/modules/execution_control.html#_CPPv421hipModuleLaunchKernel13hipFunction_tjjjjjjj11hipStream_tPPvPPv "hipModuleLaunchKernel"){.reference .internal}. The kernel arguments and the execution configuration (grid dimensions, group dimensions, dynamic shared memory, and stream) are passed as arguments to the launch function.

The HIP runtime API additionally supports the triple chevron ([`<<<`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`>>>`{.docutils .literal .notranslate}]{.pre}) syntax for launching kernels, which resembles a special function call and is easier to use than the explicit launch API, especially when handling kernel arguments.


### cuCtx and hipCtx[\#](#cuctx-and-hipctx "Link to this heading"){.headerlink}

The CUDA driver API defines "Context" and "Devices" as separate entities. Contexts contain a single device, and a device can theoretically have multiple contexts. Each context contains a set of streams and events specific to the context. The [`cuCtx`{.docutils .literal .notranslate}]{.pre} API also provide a mechanism to switch between devices, which enables a single CPU thread to send commands to different GPUs. HIP and recent versions of the CUDA Runtime provide other mechanisms to accomplish this, such as using streams or [`cudaSetDevice`{.docutils .literal .notranslate}]{.pre}.

On the other hand, the CUDA runtime API unifies the Context API with the Device API. This simplifies the APIs and has little loss of functionality because each context can contain a single device, and the benefits of multiple contexts have been replaced with other interfaces.

HIP provides a Context API as a thin layer over the existing device functions to facilitate easy porting from existing driver API code. The [`hipCtx`{.docutils .literal .notranslate}]{.pre} functions largely provide an alternate syntax for changing the active device. The [`hipCtx`{.docutils .literal .notranslate}]{.pre} API can be used to set the current context or to query properties of the device associated with the context. The current context is implicitly used by other APIs, such as [`hipStreamCreate`{.docutils .literal .notranslate}]{.pre}.

Note

The [`hipCtx`{.docutils .literal .notranslate}]{.pre} API is **deprecated** and its use is discouraged. Most new applications use [`hipSetDevice`{.docutils .literal .notranslate}]{.pre} or the [`hipStream`{.docutils .literal .notranslate}]{.pre} APIs. For more details on deprecated APIs, see [[HIP deprecated runtime API functions]{.doc}](../reference/deprecated_api_list.html){.reference .internal}.


## Compilation[\#](#compilation "Link to this heading"){.headerlink}

HIP code must be compiled for a specific AMD GPU architecture, and the resulting binaries contain code tailored to that target architecture.

[`hipcc`{.docutils .literal .notranslate}]{.pre} is a compiler driver that invokes [`amdclang++`{.docutils .literal .notranslate}]{.pre} (HIP-Clang) and passes the required options to it. Tools that rely on [`hipcc`{.docutils .literal .notranslate}]{.pre} must ensure that the compiler flags they provide are appropriate for the underlying compiler.

[`hipconfig`{.docutils .literal .notranslate}]{.pre} is a helpful tool for identifying the current system's platform, compiler and runtime. It can also help set options appropriately. As an example, [`hipconfig`{.docutils .literal .notranslate}]{.pre} can provide a path to HIP, in Makefiles:

::: highlight
    HIP_PATH ?= $(shell hipconfig --path)

### HIP Headers[\#](#hip-headers "Link to this heading"){.headerlink}

The [`hip_runtime.h`{.docutils .literal .notranslate}]{.pre} headers define all the necessary types, functions, macros, etc., needed to compile a HIP program, this includes host as well as device code. [`hip_runtime_api.h`{.docutils .literal .notranslate}]{.pre} is a subset of [`hip_runtime.h`{.docutils .literal .notranslate}]{.pre}.

CUDA has slightly different contents for these two files. In some cases you might need to convert hipified code to include the richer [`hip_runtime.h`{.docutils .literal .notranslate}]{.pre} instead of [`hip_runtime_api.h`{.docutils .literal .notranslate}]{.pre}.

### Using a Standard C++ Compiler[\#](#using-a-standard-c-compiler "Link to this heading"){.headerlink}

A source file that is only calling HIP APIs but neither defines nor launches any kernels can be compiled with a standard C or C++ compiler (GCC or MSVC for example) even when [`hip_runtime_api.h`{.docutils .literal .notranslate}]{.pre} or [`hip_runtime.h`{.docutils .literal .notranslate}]{.pre} are included. The HIP include paths and platform macros ([`__HIP_PLATFORM_AMD__`{.docutils .literal .notranslate}]{.pre}) must be passed to the compiler.

[`hipconfig`{.docutils .literal .notranslate}]{.pre} can help define the necessary options, for example on an AMD platform:

::: highlight
    hipconfig --cpp_config
     -D__HIP_PLATFORM_AMD__= -I/opt/rocm/include

HIP-Clang does not include default headers, and instead you must explicitly include all required files.

Note

The [`hipify`{.docutils .literal .notranslate}]{.pre} tool automatically converts [`cuda_runtime.h`{.docutils .literal .notranslate}]{.pre} to [`hip_runtime.h`{.docutils .literal .notranslate}]{.pre}, and it converts [`cuda_runtime_api.h`{.docutils .literal .notranslate}]{.pre} to [`hip_runtime_api.h`{.docutils .literal .notranslate}]{.pre}, but it may miss nested headers or macros.

### Compiler defines for HIP[\#](#compiler-defines-for-hip "Link to this heading"){.headerlink}

C++ macros are defined by the HIP compilers and APIs. This section lists macros that are available when compiling HIP code and the compiler combinations that define them.

The following table lists the macros that can be used when compiling HIP. Most of these macros are not directly defined by the compilers, but in [`hip_common.h`{.docutils .literal .notranslate}]{.pre}, which is included by [`hip_runtime.h`{.docutils .literal .notranslate}]{.pre}.

::: pst-scrollable-table-container
  Macro                                                               [`amdclang++`{.docutils .literal .notranslate}]{.pre}                                                                                                                                                                        Other (GCC, MSVC, Clang, etc.)
  ------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------
  [`__HIP_PLATFORM_AMD__`{.docutils .literal .notranslate}]{.pre}     Defined                                                                                                                                                                                                                      Undefined, needs to be set explicitly
  [`__HIPCC__`{.docutils .literal .notranslate}]{.pre}                Defined when compiling [`.hip`{.docutils .literal .notranslate}]{.pre} files or specifying [`-x`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`hip`{.docutils .literal .notranslate}]{.pre}   Undefined
  [`__HIP_DEVICE_COMPILE__`{.docutils .literal .notranslate}]{.pre}   1 if compiling for device, undefined if compiling for host                                                                                                                                                                   Undefined
  [`__HIP_ARCH_<FEATURE>__`{.docutils .literal .notranslate}]{.pre}   0 or 1 depending on feature support of targeted hardware (see [[Identifying device architecture and features]{.std .std-ref}](#identifying-device-architecture-features){.reference .internal})                              0
  [`__HIP__`{.docutils .literal .notranslate}]{.pre}                  Defined when compiling [`.hip`{.docutils .literal .notranslate}]{.pre} files or specifying [`-x`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`hip`{.docutils .literal .notranslate}]{.pre}   Undefined



### Identifying host or device compilation pass[\#](#identifying-compiler-target "Link to this heading"){.headerlink}

[`amdclang++`{.docutils .literal .notranslate}]{.pre} makes multiple passes over the code: one pass for the host code, and for the device code one pass for each GPU architecture to be compiled for.

The [`__HIP_DEVICE_COMPILE__`{.docutils .literal .notranslate}]{.pre} macro is defined when the compiler is compiling for the device. This macro can be used to replace the [`__CUDA_ARCH__`{.docutils .literal .notranslate}]{.pre} macro when porting from CUDA.

::: highlight
    #include "hip/hip_runtime.h"
    #include <iostream>

    __host__ __device__ void call_func(){
      #ifdef __HIP_DEVICE_COMPILE__
        printf("device\n");
      #else
        std::cout << "host" << std::endl;
      #endif
    }

    __global__ void test_kernel(){
      call_func();
    }

    int main(int argc, char** argv) {
      test_kernel<<<1, 1, 0, 0>>>();

      call_func();
    }

## HIP-Clang implementation notes[\#](#hip-clang-implementation-notes "Link to this heading"){.headerlink}

HIP-Clang links device code from different translation units together. For each device target, it generates a code object. [`clang-offload-bundler`{.docutils .literal .notranslate}]{.pre} bundles code objects for different device targets into one fat binary, which is embedded as the global symbol [`__hip_fatbin`{.docutils .literal .notranslate}]{.pre} in the [`.hip_fatbin`{.docutils .literal .notranslate}]{.pre} section of the ELF file of the executable or shared object.

### Initialization and termination functions[\#](#initialization-and-termination-functions "Link to this heading"){.headerlink}

HIP-Clang generates initialization and termination functions for each translation unit for host code compilation. The initialization functions call [`__hipRegisterFatBinary`{.docutils .literal .notranslate}]{.pre} to register the fat binary embedded in the ELF file. They also call [`__hipRegisterFunction`{.docutils .literal .notranslate}]{.pre} and [`__hipRegisterVar`{.docutils .literal .notranslate}]{.pre} to register kernel functions and device-side global variables. The termination functions call [`__hipUnregisterFatBinary`{.docutils .literal .notranslate}]{.pre}.

HIP-Clang emits a global variable [`__hip_gpubin_handle`{.docutils .literal .notranslate}]{.pre} of type [`void**`{.docutils .literal .notranslate}]{.pre} with [`linkonce`{.docutils .literal .notranslate}]{.pre} linkage and an initial value of 0 for each host translation unit. Each initialization function checks [`__hip_gpubin_handle`{.docutils .literal .notranslate}]{.pre} and registers the fat binary only if [`__hip_gpubin_handle`{.docutils .literal .notranslate}]{.pre} is 0. It saves the return value of [`__hip_gpubin_handle`{.docutils .literal .notranslate}]{.pre} to [`__hip_gpubin_handle`{.docutils .literal .notranslate}]{.pre}. This ensures that the fat binary is registered once. A similar check is performed in the termination functions.

### Kernel launching[\#](#kernel-launching "Link to this heading"){.headerlink}

HIP-Clang supports kernel launching using either the triple chevron ([`<<<>>>`{.docutils .literal .notranslate}]{.pre}) syntax, [[`hipLaunchKernel()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../reference/hip_runtime_api/modules/launch_api.html#_CPPv415hipLaunchKernelPKv4dim34dim3PPv6size_t11hipStream_t "hipLaunchKernel"){.reference .internal}, or [`hipLaunchKernelGGL()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}. The last option is a macro that expands to the [`<<<>>>`{.docutils .literal .notranslate}]{.pre} syntax by default. It can also be turned into a template by defining [`HIP_TEMPLATE_KERNEL_LAUNCH`{.docutils .literal .notranslate}]{.pre}.

When the executable or shared library is loaded by the dynamic linker, the initialization functions are called. In the initialization functions, the code objects containing all kernels are loaded when [`__hipRegisterFatBinary`{.docutils .literal .notranslate}]{.pre} is called. When [`__hipRegisterFunction`{.docutils .literal .notranslate}]{.pre} is called, the stub functions are associated with the corresponding kernels in the code objects.

HIP-Clang implements two sets of APIs for launching kernels. By default, when HIP-Clang encounters the [`<<<>>>`{.docutils .literal .notranslate}]{.pre} statement in the host code, it first calls [[`hipConfigureCall()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../reference/hip_runtime_api/modules/launch_api.html#_CPPv416hipConfigureCall4dim34dim36size_t11hipStream_t "hipConfigureCall"){.reference .internal} to set up the threads and grids. It then calls the stub function with the given arguments. The stub function calls [[`hipSetupArgument()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../reference/hip_runtime_api/modules/launch_api.html#_CPPv416hipSetupArgumentPKv6size_t6size_t "hipSetupArgument"){.reference .internal} for each kernel argument, then calls [[`hipLaunchByPtr()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../reference/hip_runtime_api/modules/launch_api.html#_CPPv414hipLaunchByPtrPKv "hipLaunchByPtr"){.reference .internal} with a function pointer to the stub function. In [`hipLaunchByPtr`{.docutils .literal .notranslate}]{.pre}, the actual kernel associated with the stub function is launched.

### Compilation options for hipModuleLoadDataEx[\#](#compilation-options-for-hipmoduleloaddataex "Link to this heading"){.headerlink}

The [`hipModule_t`{.xref .cpp .cpp-type .docutils .literal .notranslate}]{.pre} interface provides [[`hipModuleLoadDataEx()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../reference/hip_runtime_api/modules/module_management.html#_CPPv419hipModuleLoadDataExP11hipModule_tPKvjP12hipJitOptionPPv "hipModuleLoadDataEx"){.reference .internal} for loading code modules. HIP-Clang code objects contain fully compiled code for a device-specific instruction set and don't require additional compilation as a part of the load step. Therefore, [[`hipModuleLoadDataEx()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../reference/hip_runtime_api/modules/module_management.html#_CPPv419hipModuleLoadDataExP11hipModule_tPKvjP12hipJitOptionPPv "hipModuleLoadDataEx"){.reference .internal} behaves like [[`hipModuleLoadData()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../reference/hip_runtime_api/modules/module_management.html#_CPPv417hipModuleLoadDataP11hipModule_tPKv "hipModuleLoadData"){.reference .internal} on HIP-Clang (where compilation options are not used).

For example:

::: highlight
    hipModule_t module;
    void *imagePtr = ...; // Somehow populate data pointer with code object

    const int numOptions = 1;
    hipJitOption options[numOptions];
    void *optionValues[numOptions];

    options[0] = hipJitOptionMaxRegisters;
    unsigned maxRegs = 15;
    optionValues[0] = (void *)(&maxRegs);

    // hipModuleLoadData(module, imagePtr) will be called, JIT options will not be used
    hipModuleLoadDataEx(module, imagePtr, numOptions, options, optionValues);

    hipFunction_t k;
    hipModuleGetFunction(&k, module, "myKernel");

The sample below shows how to use :cpp:func:[`hipModuleGetFunction`{.docutils .literal .notranslate}]{.pre}.

::: highlight
    #include <hip/hip_runtime.h>
    #include <hip/hip_runtime_api.h>

    #include <vector>

    int main() {

        size_t elements = 64*1024;
        size_t size_bytes = elements * sizeof(float);

        std::vector<float> A(elements), B(elements);

        // Allocate device memory
        hipDeviceptr_t d_A, d_B;
        HIPCHECK(hipMalloc(&d_A, size_bytes));
        HIPCHECK(hipMalloc(&d_B, size_bytes));

        // Copy data to device
        HIPCHECK(hipMemcpyHtoD(d_A, A.data(), size_bytes));
        HIPCHECK(hipMemcpyHtoD(d_B, B.data(), size_bytes));

        // Load module
        hipModule_t Module;
        // The module file must contain architecture specific object code (.hsaco)
        HIPCHECK(hipModuleLoad(&Module, "vcpy_isa.co"));
        // Get kernel function from the module via its name
        hipFunction_t Function;
        HIPCHECK(hipModuleGetFunction(&Function, Module, "hello_world"));

        // Create buffer for kernel arguments
        std::vector<void*> argBuffer{&d_A, &d_B};
        size_t arg_size_bytes = argBuffer.size() * sizeof(void*);

        // Create configuration passed to the kernel as arguments
        void* config[] = {HIP_LAUNCH_PARAM_BUFFER_POINTER, argBuffer.data(),
                          HIP_LAUNCH_PARAM_BUFFER_SIZE, &arg_size_bytes, HIP_LAUNCH_PARAM_END};

        int threads_per_block = 128;
        int blocks = (elements + threads_per_block - 1) / threads_per_block;

        // Actually launch kernel
        HIPCHECK(hipModuleLaunchKernel(Function, blocks, 1, 1, threads_per_block, 1, 1, 0, 0, NULL, config));

        HIPCHECK(hipMemcpyDtoH(A.data(), d_A, elements));
        HIPCHECK(hipMemcpyDtoH(B.data(), d_B, elements));

        HIPCHECK(hipFree(d_A));
        HIPCHECK(hipFree(d_B));

        return 0;
    }


## Identifying device architecture and features[\#](#identifying-device-architecture-features "Link to this heading"){.headerlink}

GPUs of different generations and architectures do not provide the same level of [[hardware feature support]{.doc}](../reference/hardware_features.html){.reference .internal}. To guard device code that uses architecture-dependent features, the [`__HIP_ARCH_<FEATURE>__`{.docutils .literal .notranslate}]{.pre} C++-macros can be used, as described below.

### Device code feature identification[\#](#device-code-feature-identification "Link to this heading"){.headerlink}

Some CUDA code tests [`__CUDA_ARCH__`{.docutils .literal .notranslate}]{.pre} for a specific value to determine whether the GPU supports a certain architectural feature, depending on its compute capability. This requires knowledge about what [`__CUDA_ARCH__`{.docutils .literal .notranslate}]{.pre} supports what feature set.

HIP simplifies this, by replacing these macros with feature-specific macros, not architecture specific.

For instance,

::: highlight
    //#if __CUDA_ARCH__ >= 130 // does not properly specify what feature is required
    #if __HIP_ARCH_HAS_DOUBLES__ == 1 // explicitly specifies what feature is required
      // device code
    #endif

For host code, the [`__HIP_ARCH_<FEATURE>__`{.docutils .literal .notranslate}]{.pre} defines are set to 0, if [`hip_runtime.h`{.docutils .literal .notranslate}]{.pre} is included, and undefined otherwise. It should not be relied upon in host code.

### Host code feature identification[\#](#host-code-feature-identification "Link to this heading"){.headerlink}

The host code must not rely on the [`__HIP_ARCH_<FEATURE>__`{.docutils .literal .notranslate}]{.pre} macros, because the GPUs available to a system are not known during compile time, and their architectural features differ. Alternatively, the host code can query architecture feature flags during runtime by using [[`hipGetDeviceProperties()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../reference/hip_runtime_api/modules/device_management.html#_CPPv422hipGetDevicePropertiesP15hipDeviceProp_ti "hipGetDeviceProperties"){.reference .internal} or [[`hipDeviceGetAttribute()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../reference/hip_runtime_api/modules/device_management.html#_CPPv421hipDeviceGetAttributePi20hipDeviceAttribute_ti "hipDeviceGetAttribute"){.reference .internal}.

::: highlight
    #include <hip/hip_runtime.h>
    #include <cstdlib>
    #include <iostream>

    #define HIP_CHECK(expression) {                           \
      const hipError_t err = expression;                      \
      if (err != hipSuccess){                                 \
        std::cout << "HIP Error: " << hipGetErrorString(err)) \
                  << " at line " << __LINE__ << std::endl;    \
        std::exit(EXIT_FAILURE);                              \
      }                                                       \
    }

    int main(){
      int deviceCount;
      HIP_CHECK(hipGetDeviceCount(&deviceCount));

      int device = 0; // Query first available GPU. Can be replaced with any
                      // integer up to, not including, deviceCount
      hipDeviceProp_t deviceProp;
      HIP_CHECK(hipGetDeviceProperties(&deviceProp, device));

      std::cout << "The queried device ";
      if (deviceProp.arch.hasSharedInt32Atomics) // HIP feature query
        std::cout << "supports";
      else
        std::cout << "does not support";
      std::cout << " shared int32 atomic operations" << std::endl;
    }

### Feature macros and properties[\#](#feature-macros-and-properties "Link to this heading"){.headerlink}

The following table lists the feature macros that HIP supports, alongside corresponding device properties that can be queried from the host code.

::: pst-scrollable-table-container
  Macro (for device code)                                                                Device property (for host runtime query)                              Comment
  -------------------------------------------------------------------------------------- --------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`__HIP_ARCH_HAS_GLOBAL_INT32_ATOMICS__`{.docutils .literal .notranslate}]{.pre}       [`hasGlobalInt32Atomics`{.docutils .literal .notranslate}]{.pre}      32-bit integer atomics for global memory
  [`__HIP_ARCH_HAS_GLOBAL_FLOAT_ATOMIC_EXCH__`{.docutils .literal .notranslate}]{.pre}   [`hasGlobalFloatAtomicExch`{.docutils .literal .notranslate}]{.pre}   32-bit float atomic exchange for global memory
  [`__HIP_ARCH_HAS_SHARED_INT32_ATOMICS__`{.docutils .literal .notranslate}]{.pre}       [`hasSharedInt32Atomics`{.docutils .literal .notranslate}]{.pre}      32-bit integer atomics for shared memory
  [`__HIP_ARCH_HAS_SHARED_FLOAT_ATOMIC_EXCH__`{.docutils .literal .notranslate}]{.pre}   [`hasSharedFloatAtomicExch`{.docutils .literal .notranslate}]{.pre}   32-bit float atomic exchange for shared memory
  [`__HIP_ARCH_HAS_FLOAT_ATOMIC_ADD__`{.docutils .literal .notranslate}]{.pre}           [`hasFloatAtomicAdd`{.docutils .literal .notranslate}]{.pre}          32-bit float atomic add in global and shared memory
  [`__HIP_ARCH_HAS_GLOBAL_INT64_ATOMICS__`{.docutils .literal .notranslate}]{.pre}       [`hasGlobalInt64Atomics`{.docutils .literal .notranslate}]{.pre}      64-bit integer atomics for global memory
  [`__HIP_ARCH_HAS_SHARED_INT64_ATOMICS__`{.docutils .literal .notranslate}]{.pre}       [`hasSharedInt64Atomics`{.docutils .literal .notranslate}]{.pre}      64-bit integer atomics for shared memory
  [`__HIP_ARCH_HAS_DOUBLES__`{.docutils .literal .notranslate}]{.pre}                    [`hasDoubles`{.docutils .literal .notranslate}]{.pre}                 Double-precision floating-point operations
  [`__HIP_ARCH_HAS_WARP_VOTE__`{.docutils .literal .notranslate}]{.pre}                  [`hasWarpVote`{.docutils .literal .notranslate}]{.pre}                Warp vote instructions ([`any`{.docutils .literal .notranslate}]{.pre}, [`all`{.docutils .literal .notranslate}]{.pre})
  [`__HIP_ARCH_HAS_WARP_BALLOT__`{.docutils .literal .notranslate}]{.pre}                [`hasWarpBallot`{.docutils .literal .notranslate}]{.pre}              Warp ballot instructions
  [`__HIP_ARCH_HAS_WARP_SHUFFLE__`{.docutils .literal .notranslate}]{.pre}               [`hasWarpShuffle`{.docutils .literal .notranslate}]{.pre}             Warp shuffle operations ([`shfl_*`{.docutils .literal .notranslate}]{.pre})
  [`__HIP_ARCH_HAS_WARP_FUNNEL_SHIFT__`{.docutils .literal .notranslate}]{.pre}          [`hasFunnelShift`{.docutils .literal .notranslate}]{.pre}             Funnel shift two input words into one
  [`__HIP_ARCH_HAS_THREAD_FENCE_SYSTEM__`{.docutils .literal .notranslate}]{.pre}        [`hasThreadFenceSystem`{.docutils .literal .notranslate}]{.pre}       [`threadfence_system()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}
  [`__HIP_ARCH_HAS_SYNC_THREAD_EXT__`{.docutils .literal .notranslate}]{.pre}            [`hasSyncThreadsExt`{.docutils .literal .notranslate}]{.pre}          [`syncthreads_count()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}, [`syncthreads_and()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}, [`syncthreads_or()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}
  [`__HIP_ARCH_HAS_SURFACE_FUNCS__`{.docutils .literal .notranslate}]{.pre}              [`hasSurfaceFuncs`{.docutils .literal .notranslate}]{.pre}            Supports [[surface functions]{.std .std-ref}](../reference/hip_runtime_api/modules/memory_management/surface_object.html#surface-object-reference){.reference .internal}.
  [`__HIP_ARCH_HAS_3DGRID__`{.docutils .literal .notranslate}]{.pre}                     [`has3dGrid`{.docutils .literal .notranslate}]{.pre}                  Grids and groups are 3D
  [`__HIP_ARCH_HAS_DYNAMIC_PARALLEL__`{.docutils .literal .notranslate}]{.pre}           [`hasDynamicParallelism`{.docutils .literal .notranslate}]{.pre}      Ability to launch a kernel from within a kernel

## warpSize[\#](#warpsize "Link to this heading"){.headerlink}

Code should not assume a warp size of 32 or 64, as AMD GPU architectures have different warp sizes. The [`warpSize`{.docutils .literal .notranslate}]{.pre} built-in should be used in device code, while the host can query it during runtime via the device properties. See the [[HIP language extension for warpSize]{.std .std-ref}](hip_cpp_language_extensions.html#warp-size){.reference .internal} for information on how to write warpSize-aware code.

## Lane masks bit-shift[\#](#lane-masks-bit-shift "Link to this heading"){.headerlink}

A thread in a warp is also called a lane, and a lane mask is a bitmask where each bit corresponds to a thread in a warp. A bit is 1 if the thread is active, 0 if it's inactive. Bit-shift operations are typically used to create lane masks and on AMD GPUs the [`warpSize`{.docutils .literal .notranslate}]{.pre} can differ between different architectures, that's why it's essential to use correct bitmask type, when porting code.

Example:

::: highlight
    // Get the thread's position in the warp
    unsigned int laneId = threadIdx.x % warpSize;

    // Use lane ID for bit-shift
    val & ((1 << (threadIdx.x % warpSize) )-1 );

    // Shift 32 bit integer with val variable
    WarpReduce::sum( (val < warpSize) ? (1 << val) : 0);

Lane masks are 32-bit integer types as this is the integer precision that C assigns to such constants by default. GCN/CDNA architectures have a warp size of 64, [`threadIdx.x`{.code .docutils .literal .notranslate}]{.pre}` `{.code .docutils .literal .notranslate}[`%`{.code .docutils .literal .notranslate}]{.pre}` `{.code .docutils .literal .notranslate}[`warpSize`{.code .docutils .literal .notranslate}]{.pre} and [`val`{.code .docutils .literal .notranslate}]{.pre} in the example may obtain values greater than 31. Consequently, shifting by such values would clear the 32-bit register to which the shift operation is applied. For AMD architectures, a straightforward fix could look as follows:

::: highlight
    // Get the thread's position in the warp
    unsigned int laneId = threadIdx.x % warpSize;

    // Use lane ID for bit-shift
    val & ((1ull << (threadIdx.x % warpSize) )-1 );

    // Shift 64 bit integer with val variable
    WarpReduce::sum( (val < warpSize) ? (1ull << val) : 0);

To handle different AMD GPU architectures, it is better to introduce appropriately typed placeholders as shown below:

::: highlight
    #if defined(__GFX8__) || defined(__GFX9__)
    typedef uint64_t lane_mask_t;
    #else
    typedef uint32_t lane_mask_t;
    #endif

The use of [`lane_mask_t`{.code .docutils .literal .notranslate}]{.pre} with the previous example:

::: highlight
    // Get the thread's position in the warp
    unsigned int laneId = threadIdx.x % warpSize;

    // Use lane ID for bit-shift
    val & ((lane_mask_t{1} << (threadIdx.x % warpSize) )-1 );

    // Shift 32 or 64 bit integer with val variable
    WarpReduce::sum( (val < warpSize) ? (lane_mask_t{1} << val) : 0);

## Porting from CUDA \_\_launch_bounds\_\_[\#](#porting-from-cuda-launch-bounds "Link to this heading"){.headerlink}

CUDA defines a [`__launch_bounds__`{.docutils .literal .notranslate}]{.pre} qualifier which works similarly to the HIP implementation, however, it uses different parameters:

::: highlight
    __launch_bounds__(MAX_THREADS_PER_BLOCK, MIN_BLOCKS_PER_MULTIPROCESSOR)

[`MAX_THREADS_PER_BLOCK`{.docutils .literal .notranslate}]{.pre} is the same in CUDA and in HIP. However, [`MIN_BLOCKS_PER_MULTIPROCESSOR`{.docutils .literal .notranslate}]{.pre} in CUDA must be converted to [`MIN_WARPS_PER_EXECUTION_UNIT`{.docutils .literal .notranslate}]{.pre} in HIP, which uses warps and execution units rather than blocks and multiprocessors. This conversion can be done manually with the equation considering the GPU's configuration mode.

- In Compute Unit (CU) mode, typical of CDNA:

::: highlight
    MIN_WARPS_PER_EXECUTION_UNIT = (MIN_BLOCKS_PER_MULTIPROCESSOR * MAX_THREADS_PER_BLOCK) / (warpSize * 2)

- In Workgroup Processor (WGP) mode, a feature of RDNA:

::: highlight
    MIN_WARPS_PER_EXECUTION_UNIT = (MIN_BLOCKS_PER_MULTIPROCESSOR * MAX_THREADS_PER_BLOCK) / (warpSize * 4)

Directly controlling the warps per execution unit makes it easier to reason about the occupancy, unlike with blocks, where the occupancy depends on the block size.

The use of execution units rather than multiprocessors also provides support for architectures with multiple execution units per multiprocessor. For example, the AMD GCN architecture has 4 execution units per multiprocessor.

### maxregcount[\#](#maxregcount "Link to this heading"){.headerlink}

The [`nvcc`{.docutils .literal .notranslate}]{.pre} compiler will predict the number of registers per thread based on the launch bounds calculation. [`--maxregcount`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`X`{.docutils .literal .notranslate}]{.pre} can be used to override the compiler's decision by enforcing a hard number of registers ([`X`{.docutils .literal .notranslate}]{.pre}) that the compiler must not exceed. If the compiler is unable to meet this requirement, it will place additional "registers" into memory instead of using hardware registers.

Unlike [`nvcc`{.docutils .literal .notranslate}]{.pre}, [`amdclang++`{.docutils .literal .notranslate}]{.pre} does not support the [`--maxregcount`{.docutils .literal .notranslate}]{.pre} option. You are encouraged to use the [`__launch_bounds__`{.docutils .literal .notranslate}]{.pre} directive since the parameters are more intuitive than micro-architecture details like registers. The directive allows per-kernel control.

## Driver entry point access[\#](#driver-entry-point-access "Link to this heading"){.headerlink}

The HIP runtime provides driver entry point access functionality. This feature lets developers interact directly with the HIP driver API, providing more control over GPU operations.

Driver entry point access provides several features:

- Retrieving the address of a runtime function

- Requesting the default stream version on a per-thread basis

- Accessing HIP features on older toolkits with a newer driver

For more information on driver entry point access, see [[`hipGetProcAddress()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../reference/hip_runtime_api/modules/memory_management.html#_CPPv417hipGetProcAddressPKcPPvi8uint64_tP31hipDriverProcAddressQueryResult "hipGetProcAddress"){.reference .internal}.

### Address retrieval[\#](#address-retrieval "Link to this heading"){.headerlink}

The [[`hipGetProcAddress()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../reference/hip_runtime_api/modules/memory_management.html#_CPPv417hipGetProcAddressPKcPPvi8uint64_tP31hipDriverProcAddressQueryResult "hipGetProcAddress"){.reference .internal} function can be used to obtain the address of a runtime function. This is demonstrated in the following example:

::: highlight
    #include <hip/hip_runtime.h>
    #include <hip/hip_runtime_api.h>

    #include <iostream>

    typedef hipError_t (*hipInit_t)(unsigned int);

    int main() {
        // Initialize the HIP runtime
        hipError_t res = hipInit(0);
        if (res != hipSuccess) {
            std::cerr << "Failed to initialize HIP runtime." << std::endl;
            return 1;
        }

        // Get the address of the hipInit function
        hipInit_t hipInitFunc;
        int hipVersion = HIP_VERSION; // Use the HIP version defined in hip_runtime_api.h
        uint64_t flags = 0; // No special flags
        hipDriverProcAddressQueryResult symbolStatus;

        res = hipGetProcAddress("hipInit", (void**)&hipInitFunc, hipVersion, flags, &symbolStatus);
        if (res != hipSuccess) {
            std::cerr << "Failed to get address of hipInit()." << std::endl;
            return 1;
        }

        // Call the hipInit function using the obtained address
        res = hipInitFunc(0);
        if (res == hipSuccess) {
            std::cout << "HIP runtime initialized successfully using hipGetProcAddress()." << std::endl;
        } else {
            std::cerr << "Failed to initialize HIP runtime using hipGetProcAddress()." << std::endl;
        }

        return 0;
    }

### Per-thread default stream version request[\#](#per-thread-default-stream-version-request "Link to this heading"){.headerlink}

HIP offers functionality for managing streams on a per-thread basis. By using [`hipStreamPerThread`{.docutils .literal .notranslate}]{.pre}, each thread can independently manage its default stream, simplifying operations. The following example demonstrates how this feature enhances performance by reducing contention and improving efficiency.

::: highlight
    #include <hip/hip_runtime.h>

    #include <iostream>

    int main() {
        // Initialize the HIP runtime
        hipError_t res = hipInit(0);
        if (res != hipSuccess) {
            std::cerr << "Failed to initialize HIP runtime." << std::endl;
            return 1;
        }

        // Get the per-thread default stream
        hipStream_t stream = hipStreamPerThread;

        // Use the stream for some operation
        // For example, allocate memory on the device
        void* d_ptr;
        size_t size = 1024;
        res = hipMalloc(&d_ptr, size);
        if (res != hipSuccess) {
            std::cerr << "Failed to allocate memory." << std::endl;
            return 1;
        }

        // Perform some operation using the stream
        // For example, set memory on the device
        res = hipMemsetAsync(d_ptr, 0, size, stream);
        if (res != hipSuccess) {
            std::cerr << "Failed to set memory." << std::endl;
            return 1;
        }

        // Synchronize the stream
        res = hipStreamSynchronize(stream);
        if (res != hipSuccess) {
            std::cerr << "Failed to synchronize stream." << std::endl;
            return 1;
        }

        std::cout << "Operation completed successfully using per-thread default stream." << std::endl;

        // Free the allocated memory
        hipFree(d_ptr);

        return 0;
    }

### Accessing HIP features with a newer driver[\#](#accessing-hip-features-with-a-newer-driver "Link to this heading"){.headerlink}

HIP is forward compatible, allowing newer features to be utilized with older toolkits, provided a compatible driver is present. Feature support can be verified through runtime API functions and version checks. This approach ensures that applications can benefit from new features and improvements in the HIP runtime without requiring recompilation with a newer toolkit. The function [[`hipGetProcAddress()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../reference/hip_runtime_api/modules/memory_management.html#_CPPv417hipGetProcAddressPKcPPvi8uint64_tP31hipDriverProcAddressQueryResult "hipGetProcAddress"){.reference .internal} enables dynamic querying and the use of newer functions offered by the HIP runtime, even if the application was built with an older toolkit.

Note

:cpp:func:[`hipGetProcAddress`{.docutils .literal .notranslate}]{.pre} is limited to HIP driver API function calls. For HIP runtime API calls, the corresponding function is :cpp:func:[`hipGetDriverEntryPoint`{.docutils .literal .notranslate}]{.pre}.

An example is provided for a hypothetical [`foo()`{.docutils .literal .notranslate}]{.pre} function.

::: highlight
    // Get the address of the foo function
    foo_t fooFunc;
    int hipVersion = 60300000; // HIP version number (e.g. 6.3.0)
    uint64_t flags = 0; // No special flags
    hipDriverProcAddressQueryResult symbolStatus;

    res = hipGetProcAddress("foo", (void**)&fooFunc, hipVersion, flags, &symbolStatus);

The HIP version number is defined as an integer:

::: highlight
    HIP_VERSION=HIP_VERSION_MAJOR * 10000000 + HIP_VERSION_MINOR * 100000 + HIP_VERSION_PATCH

## Memory type identification[\#](#memory-type-identification "Link to this heading"){.headerlink}

To return the pointer's memory type in HIP, developers should use [[`hipPointerGetAttributes()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../reference/hip_runtime_api/modules/memory_management.html#_CPPv423hipPointerGetAttributesP21hipPointerAttribute_tPKv "hipPointerGetAttributes"){.reference .internal}. The first parameter of the function is hipPointerAttribute_t. Its [`type`{.docutils .literal .notranslate}]{.pre} member variable indicates whether the memory pointed to is allocated on the device or the host. For example:

::: highlight
    double * ptr;
    hipMalloc(&ptr, sizeof(double));
    hipPointerAttribute_t attr;
    hipPointerGetAttributes(&attr, ptr); /*attr.type is hipMemoryTypeDevice*/
    if(attr.type == hipMemoryTypeDevice)
      std::cout << "ptr is of type hipMemoryTypeDevice" << std::endl;

    double* ptrHost;
    hipHostMalloc(&ptrHost, sizeof(double));
    hipPointerAttribute_t attr;
    hipPointerGetAttributes(&attr, ptrHost); /*attr.type is hipMemoryTypeHost*/
    if(attr.type == hipMemoryTypeHost)
      std::cout << "ptrHost is of type hipMemoryTypeHost" << std::endl;

Note that [`hipMemoryType`{.docutils .literal .notranslate}]{.pre} enum values are different from the [`cudaMemoryType`{.docutils .literal .notranslate}]{.pre} enum values.

[`hipMemoryType`{.docutils .literal .notranslate}]{.pre} is defined in [`hip_runtime_api.h`{.docutils .literal .notranslate}]{.pre}:

::: highlight
    typedef enum hipMemoryType {
        hipMemoryTypeHost = 0,    ///< Memory is physically located on host
        hipMemoryTypeDevice = 1,  ///< Memory is physically located on device. (see deviceId for specific device)
        hipMemoryTypeArray = 2,   ///< Array memory, physically located on device. (see deviceId for specific device)
        hipMemoryTypeUnified = 3, ///< Not used currently
        hipMemoryTypeManaged = 4  ///< Managed memory, automaticallly managed by the unified memory system
    } hipMemoryType;

In the CUDA toolkit, the [`cudaMemoryType`{.docutils .literal .notranslate}]{.pre} is defined as following:

::: highlight
    enum cudaMemoryType
    {
      cudaMemoryTypeUnregistered = 0, // Unregistered memory.
      cudaMemoryTypeHost = 1, // Host memory.
      cudaMemoryTypeDevice = 2, // Device memory.
      cudaMemoryTypeManaged = 3, // Managed memory
    }

Note

[`cudaMemoryTypeUnregistered`{.docutils .literal .notranslate}]{.pre} is currently not supported as [`hipMemoryType`{.docutils .literal .notranslate}]{.pre} enum, due to HIP functionality backward compatibility.

When porting applications that use memory type APIs, ensure that you map the CUDA memory types to the corresponding HIP memory types appropriately.

::::: prev-next-area
[](kernel_language_cpp_support.html "previous page"){.left-prev}

::: prev-next-info
previous

Kernel language C++ support

[](hip_rtc.html "next page"){.right-next}

::: prev-next-info
next

Programming for HIP runtime compiler (RTC)

:::: sidebar-secondary-item
Contents

- [Porting a CUDA project](#porting-a-cuda-project){.reference .internal .nav-link}
  - [General tips](#general-tips){.reference .internal .nav-link}
- [Using HIPIFY](#using-hipify){.reference .internal .nav-link}
  - [Memory copy functions](#memory-copy-functions){.reference .internal .nav-link}
  - [Address spaces](#address-spaces){.reference .internal .nav-link}
  - [Context stack behavior differences](#context-stack-behavior-differences){.reference .internal .nav-link}
  - [Scanning CUDA source to scope the translation](#scanning-cuda-source-to-scope-the-translation){.reference .internal .nav-link}
  - [Automatically converting a CUDA project](#automatically-converting-a-cuda-project){.reference .internal .nav-link}
- [Library and driver equivalents](#library-and-driver-equivalents){.reference .internal .nav-link}
  - [cuModule and hipModule](#cumodule-and-hipmodule){.reference .internal .nav-link}
    - [Using hipModuleLaunchKernel](#using-hipmodulelaunchkernel){.reference .internal .nav-link}
  - [cuCtx and hipCtx](#cuctx-and-hipctx){.reference .internal .nav-link}
- [Compilation](#compilation){.reference .internal .nav-link}
  - [HIP Headers](#hip-headers){.reference .internal .nav-link}
  - [Using a Standard C++ Compiler](#using-a-standard-c-compiler){.reference .internal .nav-link}
  - [Compiler defines for HIP](#compiler-defines-for-hip){.reference .internal .nav-link}
  - [Identifying host or device compilation pass](#identifying-compiler-target){.reference .internal .nav-link}
- [HIP-Clang implementation notes](#hip-clang-implementation-notes){.reference .internal .nav-link}
  - [Initialization and termination functions](#initialization-and-termination-functions){.reference .internal .nav-link}
  - [Kernel launching](#kernel-launching){.reference .internal .nav-link}
  - [Compilation options for hipModuleLoadDataEx](#compilation-options-for-hipmoduleloaddataex){.reference .internal .nav-link}
- [Identifying device architecture and features](#identifying-device-architecture-features){.reference .internal .nav-link}
  - [Device code feature identification](#device-code-feature-identification){.reference .internal .nav-link}
  - [Host code feature identification](#host-code-feature-identification){.reference .internal .nav-link}
  - [Feature macros and properties](#feature-macros-and-properties){.reference .internal .nav-link}
- [warpSize](#warpsize){.reference .internal .nav-link}
- [Lane masks bit-shift](#lane-masks-bit-shift){.reference .internal .nav-link}
- [Porting from CUDA \_\_launch_bounds\_\_](#porting-from-cuda-launch-bounds){.reference .internal .nav-link}
  - [maxregcount](#maxregcount){.reference .internal .nav-link}
- [Driver entry point access](#driver-entry-point-access){.reference .internal .nav-link}
  - [Address retrieval](#address-retrieval){.reference .internal .nav-link}
  - [Per-thread default stream version request](#per-thread-default-stream-version-request){.reference .internal .nav-link}
  - [Accessing HIP features with a newer driver](#accessing-hip-features-with-a-newer-driver){.reference .internal .nav-link}
- [Memory type identification](#memory-type-identification){.reference .internal .nav-link}
