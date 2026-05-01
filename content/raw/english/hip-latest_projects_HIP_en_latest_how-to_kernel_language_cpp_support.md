---
title: "Kernel language C++ support &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/kernel_language_cpp_support.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T06:59:38.018961+00:00
content_hash: "190e24d410a2ec07"
---

:::::::::::::::::::::::::::::::::::::::::::::::::
{#main-content .bd-main role="main"}

sbt-scroll-pixel-helper

:::::::::::::::::::::::::::::::::::::::::::::::
bd-content
::::::::::::::::::::::::::::::::::::::::::
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
# Kernel language C++ support

::
{#print-main-content}
:
{#jb-print-toc}

{}
## Contents

:
::

{#searchbox}

::::::::::::::::::::::::::::
{#kernel-language-c-support .section}
# Kernel language C++ support[\#](#kernel-language-c-support "Link to this heading"){.headerlink}

The HIP host API can be compiled with any conforming C++ compiler, as long as no kernel launch is present in the code.

To compile device code and include kernel launches, a compiler with full HIP support is needed, such as [`amdclang++`{.docutils .literal .notranslate}]{.pre}. For more information, see [[ROCm compilers]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/llvm-project/en/latest/index.html "(in llvm-project Documentation v22.0.0)"){.reference .external}.

In host code all modern C++ standards that are supported by the compiler can be used. Device code compilation has some restrictions on modern C++ standards, but in general also supports all C++ standards. The biggest restriction is the reduced support of the C++ standard library in device code, as functions are only compiled for the host by default. An exception to this are [`constexpr`{.docutils .literal .notranslate}]{.pre} functions that are resolved at compile time and can be used in device code. There are ongoing efforts to implement C++ standard library functionality with [libhipcxx](https://github.com/ROCm/libhipcxx){.reference .external}.

::::::::::::::
{#supported-kernel-language-c-features .section}
## Supported kernel language C++ features[\#](#supported-kernel-language-c-features "Link to this heading"){.headerlink}

This section describes HIP's kernel language C++ feature support for the different versions of the standard.

:::::::::
{#general-c-features .section}
### General C++ features[\#](#general-c-features "Link to this heading"){.headerlink}

{#exception-handling .section}
#### Exception handling[\#](#exception-handling "Link to this heading"){.headerlink}

An important difference between the host and device code C++ support is exception handling. In device code, exceptions aren't available due to the hardware architecture. The device code must use return codes to handle errors.

::
{#assertions .section}
#### Assertions[\#](#assertions "Link to this heading"){.headerlink}

The [`assert`{.docutils .literal .notranslate}]{.pre} function is supported in device code. Assertions are used for debugging purposes. When the input expression equals zero, the execution will be stopped. HIP provides its own implementation for [`assert`{.docutils .literal .notranslate}]{.pre} for usage in device code in [`hip/hip_runtime.h`{.docutils .literal .notranslate}]{.pre}.

:
{.highlight-cpp .notranslate}

highlight
    void assert(int input)

:

HIP also provides the function [`abort()`{.docutils .literal .notranslate}]{.pre} which can be used to terminate the application when terminal failures are detected. It is implemented using the [`__builtin_trap()`{.docutils .literal .notranslate}]{.pre} function.

This function produces a similar effect as using CUDA's [`asm("trap")`{.docutils .literal .notranslate}]{.pre}. In HIP, [`abort()`{.docutils .literal .notranslate}]{.pre} terminates the entire application, while in CUDA, [`asm("trap")`{.docutils .literal .notranslate}]{.pre} only terminates the current kernel and the application continues to run.
::

::
{#printf .section}
#### printf[\#](#printf "Link to this heading"){.headerlink}

[`printf`{.docutils .literal .notranslate}]{.pre} is supported in device code, and can be used just like in host code.

:
{.highlight-cpp .notranslate}

highlight
    #include <hip/hip_runtime.h>

    __global__ void run_printf() { printf("Hello World\n"); }

    int main() {
      run_printf<<<dim3(1), dim3(1), 0, 0>>>();
    }

:
::

{#device-side-dynamic-global-memory-allocation .section}
#### Device-Side Dynamic Global Memory Allocation[\#](#device-side-dynamic-global-memory-allocation "Link to this heading"){.headerlink}

Device code can use [`new`{.docutils .literal .notranslate}]{.pre} or [`malloc`{.docutils .literal .notranslate}]{.pre} to dynamically allocate global memory on the device, and [`delete`{.docutils .literal .notranslate}]{.pre} or [`free`{.docutils .literal .notranslate}]{.pre} to deallocate global memory.

{#classes .section}
#### Classes[\#](#classes "Link to this heading"){.headerlink}

Classes work on both host and device side, with some constraints on the device side.

Member functions with the appropriate qualifiers can be called in host and device code, and the corresponding overload is executed.

[`virtual`{.docutils .literal .notranslate}]{.pre} member functions are also supported, however calling these functions from the host if the object was created on the device, or the other way around, is undefined behaviour.

The [`__host__`{.docutils .literal .notranslate}]{.pre}, [`__device__`{.docutils .literal .notranslate}]{.pre}, [`__managed__`{.docutils .literal .notranslate}]{.pre}, [`__shared__`{.docutils .literal .notranslate}]{.pre} and [`__constant__`{.docutils .literal .notranslate}]{.pre} memory space qualifiers can not be applied to member variables.

:::::::::

{#c-11-support .section}
### C++11 support[\#](#c-11-support "Link to this heading"){.headerlink}

[`constexpr`{.docutils .literal .notranslate}]{.pre}

:   Full support in device code. [`constexpr`{.docutils .literal .notranslate}]{.pre} implicitly defines [`__host__`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`__device__`{.docutils .literal .notranslate}]{.pre}, so standard library functions that are marked [`constexpr`{.docutils .literal .notranslate}]{.pre} can be used in device code. [`constexpr`{.docutils .literal .notranslate}]{.pre} variables can be used in both host and device code.

Lambdas

:   Lambdas are implicitly marked with [`__host__`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`__device__`{.docutils .literal .notranslate}]{.pre}. To mark them as only executable for the host or the device, they can be explicitly marked like any other function. There are restrictions on variable capture, however. Host and device specific variables can only be accessed on other devices or the host by explicitly copying them. Accessing captured the variables by reference, when the variable is not located on the executing device or host, causes undefined behaviour.

Polymorphic function wrappers

:   HIP does not support the polymorphic function wrapper [`std::function`{.docutils .literal .notranslate}]{.pre}

{#c-14-support .section}
### C++14 support[\#](#c-14-support "Link to this heading"){.headerlink}

All [C++14 language features](https://isocpp.org/wiki/faq/cpp14-language){.reference .external} are supported.

{#c-17-support .section}
### C++17 support[\#](#c-17-support "Link to this heading"){.headerlink}

All [C++17 language features](https://en.cppreference.com/w/cpp/17){.reference .external} are supported.

{#c-20-support .section}
### C++20 support[\#](#c-20-support "Link to this heading"){.headerlink}

Most [C++20 language features](https://en.cppreference.com/w/cpp/20){.reference .external} are supported, but some restrictions apply. Coroutines are not available in device code.

::::::::::::::

::::::::::::
{#compiler-features .section}
## Compiler features[\#](#compiler-features "Link to this heading"){.headerlink}

::::::
{#pragma-unroll .section}
### Pragma Unroll[\#](#pragma-unroll "Link to this heading"){.headerlink}

The unroll pragma for unrolling loops with a compile-time constant is supported:

:
{.highlight-cpp .notranslate}

highlight
    #pragma unroll 16 /* hint to compiler to unroll next loop by 16 */
    for (int i=0; i<16; i++) ...

:

:
{.highlight-cpp .notranslate}

highlight
    #pragma unroll 1 /* tell compiler to never unroll the loop */
    for (int i=0; i<16; i++) ...

:

:
{.highlight-cpp .notranslate}

highlight
    #pragma unroll /* hint to compiler to completely unroll next loop. */
    for (int i=0; i<16; i++) ...

:
::::::

{#in-line-assembly .section}
### In-Line Assembly[\#](#in-line-assembly "Link to this heading"){.headerlink}

GCN ISA In-line assembly can be included in device code.

It has to be mentioned however, that in-line assembly should be used carefully. For more information, please refer to the [[Inline ASM statements section of amdclang]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/llvm-project/en/latest/reference/rocmcc.html "(in llvm-project Documentation v22.0.0)"){.reference .external}.

A short example program including inline assembly can be found in [HIP inline_assembly sample](https://github.com/ROCm/rocm-examples/tree/develop/HIP-Basic/inline_assembly){.reference .external}.

For information on what special AMD GPU hardware features are available through assembly, please refer to the [ISA manuals of the corresponding architecture](https://llvm.org/docs/AMDGPUUsage.html#additional-documentation){.reference .external}.

::
{#kernel-compilation .section}
### Kernel Compilation[\#](#kernel-compilation "Link to this heading"){.headerlink}

[`hipcc`{.docutils .literal .notranslate}]{.pre} now supports compiling C++/HIP kernels to binary code objects. The file format for the binary files is usually [`.co`{.docutils .literal .notranslate}]{.pre} which means Code Object. The following command builds the code object using [`hipcc`{.docutils .literal .notranslate}]{.pre}.

:
{.highlight-bash .notranslate}

highlight
    hipcc --genco --offload-arch=[TARGET GPU] [INPUT FILE] -o [OUTPUT FILE]

    [TARGET GPU] = GPU architecture
    [INPUT FILE] = Name of the file containing source code
    [OUTPUT FILE] = Name of the generated code object file

:

For an example on how to use these object files, refer to the [HIP module_api sample](https://github.com/ROCm/rocm-examples/tree/develop/HIP-Basic/module_api){.reference .external}.
::

{#architecture-specific-code .section}
### Architecture specific code[\#](#architecture-specific-code "Link to this heading"){.headerlink}

[`amdclang++`{.docutils .literal .notranslate}]{.pre} defines [`__gfx*__`{.docutils .literal .notranslate}]{.pre} macros based on the GPU architecture to be compiled for. These macros can be used to include GPU architecture specific code. Refer to the sample in [HIP gpu_arch sample](https://github.com/ROCm/rocm-examples/tree/develop/HIP-Basic/gpu_arch){.reference .external}.

::::::::::::
::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::

{.bd-sidebar-secondary .bd-toc}
::
{.sidebar-secondary-items .sidebar-secondary__inner}
:
sidebar-secondary-item

{.page-toc .tocsection .onthispage}
Contents

:
::

:::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::
