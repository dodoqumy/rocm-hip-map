---
title: "SAXPY - Hello, HIP &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/tutorial/saxpy.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T06:59:26.078281+00:00
content_hash: "454fb1103879f1ff"
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
# SAXPY - Hello, HIP

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
{#saxpy-hello-hip .section}
# SAXPY - Hello, HIP[\#](#saxpy-hello-hip "Link to this heading"){.headerlink}

This tutorial explains the basic concepts of the single-source Heterogeneous-computing Interface for Portability (HIP) programming model and the essential tooling around it. It also reviews some commonalities of heterogenous APIs in general. This topic assumes basic familiarity with the C/C++ compilation model and language.

{#prerequisites .section}
## Prerequisites[\#](#prerequisites "Link to this heading"){.headerlink}

To follow this tutorial, you'll need installed drivers and a HIP compiler toolchain to compile your code. Because HIP supports compiling and running on Linux and Windows with AMD GPUs, the install instructions are more than worth covering as part of this tutorial. For more information about installing HIP development packages, see [[Install HIP]{.doc}](../install/install.html){.reference .internal}.

{#heterogeneous-programming .section}
[]{#hip-tutorial-saxpy-heterogeneous-programming}

## Heterogeneous programming[\#](#heterogeneous-programming "Link to this heading"){.headerlink}

*Heterogeneous programming* and *offloading APIs* are often mentioned together. Heterogeneous programming deals with devices of varying capabilities simultaneously. Offloading focuses on the "remote" and asynchronous aspects of computation. HIP encompasses both. It exposes GPGPU (general-purpose GPU) programming much like ordinary host-side CPU programming and lets you move data across various devices.

When programming in HIP (and other heterogenous APIs for that matter), remember that target devices are built for a specific purpose. They are designed with different tradeoffs than traditional CPUs and therefore have very different performance characteristics. Even subtle changes in code might adversely affect execution time.

::::::::::::
{#your-first-lines-of-hip-code .section}
## Your first lines of HIP code[\#](#your-first-lines-of-hip-code "Link to this heading"){.headerlink}

First, let's do the "Hello, World!" of GPGPU: SAXPY. Single-precision A times X Plus Y (*SAXPY*) is a mathematical acronym; a vector equation [\\(a\\cdot x+y=z\\)]{.math .notranslate .nohighlight} where [\\(a\\in\\mathbb{R}\\)]{.math .notranslate .nohighlight} is a scalar and [\\(x,y,z\\in\\mathbb{V}\\)]{.math .notranslate .nohighlight} are vector quantities of some large dimensionality. This vector space is defined over the set of reals. Practically speaking, you can compute this using a single [`for`{.docutils .literal .notranslate}]{.pre} loop over three arrays.

:
{.highlight-C++ .notranslate}

highlight
    for (int i = 0 ; i < N ; ++i)
        z[i] = a * x[i] + y[i];

:

In linear algebra libraries, such as BLAS (Basic Linear Algebra Subsystem) this operation is defined as AXPY "A times X Plus Y". The "S" comes from *single-precision*, meaning that array element is [`float`{.docutils .literal .notranslate}]{.pre} -s (IEEE 754 binary32 representation).

To quickly get started, use the set of [HIP samples from GitHub](https://github.com/amd/rocm-examples/){.reference .external}. With Git configured on your machine, open a command-line and navigate to your desired working directory, then run:

:
{.highlight-shell .notranslate}

highlight
    git clone https://github.com/amd/rocm-examples.git

:

A simple implementation of SAXPY resides in the [`HIP-Basic/saxpy/main.hip`{.docutils .literal .notranslate}]{.pre} file in this repository. The HIP code here mostly deals with where data has to be and when, and how devices transform this data. The first HIP calls deal with allocating device-side memory and copying data from host-side memory to device side in a C runtime-like fashion.

:
{.highlight-C++ .notranslate}

highlight
    // Allocate and copy vectors to device memory.
    float* d_x{};
    float* d_y{};
    HIP_CHECK(hipMalloc(&d_x, size_bytes));
    HIP_CHECK(hipMalloc(&d_y, size_bytes));
    HIP_CHECK(hipMemcpy(d_x, x.data(), size_bytes, hipMemcpyHostToDevice));
    HIP_CHECK(hipMemcpy(d_y, y.data(), size_bytes, hipMemcpyHostToDevice));

:

[`HIP_CHECK`{.docutils .literal .notranslate}]{.pre} is a custom macro borrowed from the examples utilities which checks the error code returned by API functions for errors and reports them to the console. It is not essential to the API, but it is a good practice to check the error codes of the HIP APIs in case you pass on incorrect values to the API, or the API might be out of resources.

The code selects the device to allocate to and to copy to. Commands are issued to the HIP runtime per thread, and every thread has a device set as the target of commands. The default device is [`0`{.docutils .literal .notranslate}]{.pre}, which is equivalent to calling [`hipSetDevice(0)`{.docutils .literal .notranslate}]{.pre}.

Launch the calculation on the device after the input data has been prepared.

:
{.highlight-C++ .notranslate}

highlight
    __global__ void saxpy_kernel(const float a, const float* d_x, float* d_y, const unsigned int size)
    {
        // ...
    }

    int main()
    {
        // ...

        // Launch the kernel on the default stream.
        saxpy_kernel<<<dim3(grid_size), dim3(block_size), 0, hipStreamDefault>>>(a, d_x, d_y, size);
    }

:

Analyze at the signature of the offloaded function:

- [`__global__`{.docutils .literal .notranslate}]{.pre} instructs the compiler to generate code for this function as an entrypoint to a device program, such that it can be launched from the host.

- The function does not return anything, because there is no trivial way to construct a return channel of a parallel invocation. Device-side entrypoints may not return a value, their results should be communicated using output parameters.

- Device-side functions are typically called compute kernels, or just kernels for short. This is to distinguish them from non-graphics-related graphics shaders, or just shaders for short.

- Arguments are taken by value and all arguments shall be [TriviallyCopyable](https://en.cppreference.com/w/cpp/named_req/TriviallyCopyable){.reference .external}, meaning they should be memcpy-friendly. (Imagine if they had custom copy constructors. Where would that logic execute? On the host? On the device?) Pointer arguments are pointers to device memory, one typically backed by VRAM.

- We said that we'll be computing [\\(a\\cdot x+y=z\\)]{.math .notranslate .nohighlight}, however we only pass two pointers to the function. We'll be canonically reusing one of the inputs as outputs.

This function is launched from the host using a language extension often called the triple chevron syntax. Inside the angle brackets, provide the following.

- The number of [[blocks]{.std .std-ref}](../understand/programming_model.html#inherent-thread-hierarchy-block){.reference .internal} to launch (our [[grid]{.std .std-ref}](../understand/programming_model.html#inherent-thread-hierarchy-grid){.reference .internal} size)

- The number of threads in a [[block]{.std .std-ref}](../understand/programming_model.html#inherent-thread-hierarchy-block){.reference .internal} (our [[block]{.std .std-ref}](../understand/programming_model.html#inherent-thread-hierarchy-block){.reference .internal} size)

- The amount of shared memory to allocate by the host

- The device stream to enqueue the operation on

The [[block]{.std .std-ref}](../understand/programming_model.html#inherent-thread-hierarchy-block){.reference .internal} size and shared memory become important later in [[Reduction]{.doc}](reduction.html){.reference .internal}. For now, a hardcoded [`256`{.docutils .literal .notranslate}]{.pre} is a safe default for simple kernels such as this. Following the triple chevron is ordinary function argument passing.

Look at how the kernel is implemented.

:
{.highlight-C++ .notranslate}

highlight
    __global__ void saxpy_kernel(const float a, const float* d_x, float* d_y, const unsigned int size)
    {
        // Compute the current thread's index in the grid.
        const unsigned int global_idx = blockIdx.x * blockDim.x + threadIdx.x;

        // The grid can be larger than the number of items in the vectors. Avoid out-of-bounds addressing.
        if(global_idx < size)
        {
            d_y[global_idx] = a * d_x[global_idx] + d_y[global_idx];
        }
    }

:

- The unique linear index identifying the thread is computed from the [[block]{.std .std-ref}](../understand/programming_model.html#inherent-thread-hierarchy-block){.reference .internal} ID the thread is a member of, the [[block]{.std .std-ref}](../understand/programming_model.html#inherent-thread-hierarchy-block){.reference .internal}'s size and the ID of the thread within the [[block]{.std .std-ref}](../understand/programming_model.html#inherent-thread-hierarchy-block){.reference .internal}.

- A check is made to avoid overindexing the input.

- The useful part of the computation is carried out.

Retrieval of the result from the device is done much like input data copy. In this current step the results copied from device to host. The opposite direction of the input data copy:

:
{.highlight-C++ .notranslate}

highlight
    HIP_CHECK(hipMemcpy(y.data(), d_y, size_bytes, hipMemcpyDeviceToHost));

:
::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
{#compiling-on-the-command-line .section}
[]{#id1}

## Compiling on the command line[\#](#compiling-on-the-command-line "Link to this heading"){.headerlink}

:::::::::::::
{#setting-up-the-command-line .section}
[]{#id2}

### Setting up the command line[\#](#setting-up-the-command-line "Link to this heading"){.headerlink}

Strictly speaking there's no such thing as "setting up the command-line for compilation" on Linux. To make invocations more terse, Linux and Windows example follow.

::::::::::::
{.sd-tab-set .docutils}
Linux

:::::
{.sd-tab-content .docutils}
While distro maintainers might package ROCm so that it installs to system-default locations, AMD's packages aren't installed that way. They need to be added to the PATH by the user.

:
{.highlight-bash .notranslate}

highlight
    export PATH=/opt/rocm/bin:${PATH}

:

You should be able to call the compiler on the command line now:

:
{.highlight-bash .notranslate}

highlight
    amdclang++ --version

:

{.admonition .note}
Note

Docker images distributed by AMD, such as [rocm-terminal](https://hub.docker.com/r/rocm/rocm-terminal/){.reference .external} already have /opt/rocm/bin on the Path for convenience. This subtly affects CMake package detection logic of ROCm libraries.

:::::

Windows

:::::
{.sd-tab-content .docutils}
Windows compilers and command line tooling have traditionally relied on extra environmental variables and PATH entries to function correctly. Visual Studio refers to command lines with this setup as "Developer Command Prompt" or "Developer PowerShell" for [`cmd.exe`{.docutils .literal .notranslate}]{.pre} and PowerShell respectively.

The HIP SDK on Windows doesn't include a complete toolchain. You will also need:

- The Microsoft Windows SDK. It provides the import libs to crucial system libraries that all executables must link to and some auxiliary compiler tooling.

- A Standard Template Library (STL). Installed as part of the Microsoft Visual C++ compiler (MSVC) or with Visual Studio.

If you don't have a version of Visual Studio 2022 installed, for a minimal command line experience, install the [Build Tools for Visual Studio 2022](https://aka.ms/vs/17/release/vs_BuildTools.exe){.reference .external} with the Desktop Developemnt Workload. Under Individual Components select:

- A version of the Windows SDK

- "MSVC v143 - VS 2022 C++ x64/x86 build tools (Latest)"

- "C++ CMake tools for Windows" (optional)

{.admonition .note}
Note

The "C++ CMake tools for Windows" individual component is a convenience which puts both [`cmake.exe`{.docutils .literal .notranslate}]{.pre} and [`ninja.exe`{.docutils .literal .notranslate}]{.pre} onto the PATH inside developer command prompts. You can install these manually, but then you must manage them manually.

Visual Studio 2017 and later are detectable as COM object instances via WMI. To setup a command line from any shell for the latest Visual Studio's default Visual C++ toolset issue:

:
{.highlight-powershell .notranslate}

highlight
    $InstallationPath = Get-CimInstance MSFT_VSInstance | Sort-Object -Property Version -Descending | Select-Object -First 1 -ExpandProperty InstallLocation
    Import-Module $InstallationPath\Common7\Tools\Microsoft.VisualStudio.DevShell.dll
    Enter-VsDevShell -InstallPath $InstallationPath -SkipAutomaticLocation -Arch amd64 -HostArch amd64 -DevCmdArguments '-no_logo'
    $env:PATH = "${env:HIP_PATH}bin;${env:PATH}"

:

You should be able to call the compiler on the command line now:

:
{.highlight-powershell .notranslate}

highlight
    clang++ --version

:
:::::
::::::::::::
:::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::
{#invoking-the-compiler-manually .section}
### Invoking the compiler manually[\#](#invoking-the-compiler-manually "Link to this heading"){.headerlink}

To compile and link a single-file application, use the following commands:

::::::
{.sd-tab-set .docutils}
Linux

::
{.sd-tab-content .docutils}
:
{.highlight-bash .notranslate}

highlight
    amdclang++ ./HIP-Basic/saxpy/main.hip -o saxpy -I ./Common -lamdhip64 -L /opt/rocm/lib -O2

:
::

Windows

::
{.sd-tab-content .docutils}
:
{.highlight-powershell .notranslate}

highlight
    clang++ .\HIP-Basic\saxpy\main.hip -o saxpy.exe -I .\Common -lamdhip64 -L ${env:HIP_PATH}lib -O2

:
::
::::::

Depending on your computer, the resulting binary might or might not run. If not, it typically complains about "Invalid device function". That error (corresponding to the [`hipErrorInvalidDeviceFunction`{.docutils .literal .notranslate}]{.pre} entry of [`hipError_t`{.docutils .literal .notranslate}]{.pre}) means that the runtime could not find a device program binary of the appropriate flavor embedded into the executable.

So far, the discussion has covered how data makes it from the host to the device and back. It has also discussed the device code as source, with the HIP runtime arguing that the correct binary to dispatch for execution. How can you find out what device binary flavors are embedded into the executable?

::::::::::::::::::::::::
{.sd-tab-set .docutils}
Linux

::::::::::::
{.sd-tab-content .docutils}
The utilities included with ROCm help significantly to inspect binary artifacts on disk. Add the ROCmCC installation folder to your PATH if you want to use these utilities (the utilities expect them to be on the PATH).

You can list embedded program binaries using [`llvm-objdump`{.docutils .literal .notranslate}]{.pre} with [`--offloading`{.docutils .literal .notranslate}]{.pre} option.

:
{.highlight-bash .notranslate}

highlight
    llvm-objdump --offloading ./saxpy

:

It should return something like:

:
{.highlight-shell .notranslate}

highlight
    ./saxpy:        file format elf64-x86-64
    Extracting offload bundle: ./saxpy.0.host-x86_64-unknown-linux-gnu-
    Extracting offload bundle: ./saxpy.0.hipv4-amdgcn-amd-amdhsa--gfx942

:

The compiler embeds a version 4 code object (more on [code object versions](https://www.llvm.org/docs/AMDGPUUsage.html#code-object-metadata){.reference .external}) and used the LLVM target triple [`amdgcn-amd-amdhsa--gfx942`{.docutils .literal .notranslate}]{.pre} (more on [target triples](https://www.llvm.org/docs/AMDGPUUsage.html#target-triples){.reference .external}). You can extract that program object in a disassembled fashion for human consumption via [`llvm-objdump`{.docutils .literal .notranslate}]{.pre}.

:
{.highlight-bash .notranslate}

highlight
    llvm-objdump --disassemble saxpy.0.hipv4-amdgcn-amd-amdhsa--gfx942 > saxpy.s

:

This creates a file on the disk called [`saxpy.s`{.docutils .literal .notranslate}]{.pre} Opening this file or dumping it to the console using [`cat`{.docutils .literal .notranslate}]{.pre} lets find the disassembled binary of the SAXPY compute kernel, something similar to:

:
{.highlight-default .notranslate}

highlight
    saxpy.0.hipv4-amdgcn-amd-amdhsa--gfx942:        file format elf64-amdgpu

    Disassembly of section .text:

    0000000000001900 <_Z12saxpy_kernelfPKfPfj>:
      s_load_dword s3, s[0:1], 0x2c                              // 000000001900: C00200C0 0000002C
      s_load_dword s4, s[0:1], 0x18                              // 000000001908: C0020100 00000018
      s_waitcnt lgkmcnt(0)                                       // 000000001910: BF8CC07F
      s_and_b32 s3, s3, 0xffff                                   // 000000001914: 8603FF03 0000FFFF
      s_mul_i32 s2, s2, s3                                       // 00000000191C: 92020302
      v_add_u32_e32 v0, s2, v0                                   // 000000001920: 68000002
      v_cmp_gt_u32_e32 vcc, s4, v0                               // 000000001924: 7D980004
      s_and_saveexec_b64 s[2:3], vcc                             // 000000001928: BE82206A
      s_cbranch_execz 20                                         // 00000000192C: BF880014 <_Z12saxpy_kernelfPKfPfj+0x80>
      s_load_dwordx4 s[4:7], s[0:1], 0x8                         // 000000001930: C00A0100 00000008
      v_mov_b32_e32 v1, 0                                        // 000000001938: 7E020280
      v_lshlrev_b64 v[0:1], 2, v[0:1]                            // 00000000193C: D28F0000 00020082
      s_load_dword s0, s[0:1], 0x0                               // 000000001944: C0020000 00000000
      s_waitcnt lgkmcnt(0)                                       // 00000000194C: BF8CC07F
      v_lshl_add_u64 v[2:3], s[4:5], 0, v[0:1]                   // 000000001950: D2080002 04010004
      v_lshl_add_u64 v[0:1], s[6:7], 0, v[0:1]                   // 000000001958: D2080000 04010006
      global_load_dword v4, v[2:3], off                          // 000000001960: DC508000 047F0002
      global_load_dword v5, v[0:1], off                          // 000000001968: DC508000 057F0000
      s_waitcnt vmcnt(0)                                         // 000000001970: BF8C0F70
      v_fmac_f32_e32 v5, s0, v4                                  // 000000001974: 760A0800
      global_store_dword v[0:1], v5, off                         // 000000001978: DC708000 007F0500
      s_endpgm                                                   // 000000001980: BF810000
      s_nop 0                                                    // 000000001984: BF800000

:

Alternatively, call the compiler with [`--save-temps`{.docutils .literal .notranslate}]{.pre} to dump all device binary to disk in separate files.

:
{.highlight-bash .notranslate}

highlight
    amdclang++ ./HIP-Basic/saxpy/main.hip -o saxpy -I ./Common -lamdhip64 -L /opt/rocm/lib -O2 --save-temps --offload-arch=gfx942

:

List all the temporaries created while compiling [`main.hip`{.docutils .literal .notranslate}]{.pre} with:

:
{.highlight-bash .notranslate}

highlight
    ls main-hip-amdgcn-amd-amdhsa-*
    main-hip-amdgcn-amd-amdhsa-gfx942.bc
    main-hip-amdgcn-amd-amdhsa-gfx942.o
    main-hip-amdgcn-amd-amdhsa-gfx942.out.resolution.txt
    main-hip-amdgcn-amd-amdhsa-gfx942.hipi
    main-hip-amdgcn-amd-amdhsa-gfx942.out
    main-hip-amdgcn-amd-amdhsa-gfx942.s

:

Files with the [`.s`{.docutils .literal .notranslate}]{.pre} extension hold the disassembled contents of the binary. The filename notes the graphics IPs used by the compiler. The contents of this file are similar to the \*.s file created with [`llvm-objdump`{.docutils .literal .notranslate}]{.pre} earlier.
::::::::::::

Windows

::::::::::
{.sd-tab-content .docutils}
The HIP SDK for Windows don't yet sport the [`roc-*`{.docutils .literal .notranslate}]{.pre} set of utilities to work with binary artifacts. To find out what binary formats are embedded into an executable, one may use [`dumpbin`{.docutils .literal .notranslate}]{.pre} tool from the Windows SDK to obtain the raw data of the [`.hip_fat`{.docutils .literal .notranslate}]{.pre} section of an executable. (This binary payload is what gets parsed by the [`roc-*`{.docutils .literal .notranslate}]{.pre} set of utilities on Linux.) Skipping over the reported header, the rendered raw data as ASCII has \~3 lines per entries. Depending on how many binaries are embedded, you may need to alter the number of rendered lines. An invocation such as:

:
{.highlight-powershell .notranslate}

highlight
    dumpbin.exe /nologo /section:.hip_fat /rawdata:8 .\saxpy.exe | select -Skip 20 -First 12

:

The output may look like:

:
{.highlight-default .notranslate}

highlight
    000000014004C000: 5F474E414C435F5F 5F44414F4C46464F   __CLANG_OFFLOAD_
    000000014004C010: 5F5F454C444E5542 0000000000000002   BUNDLE__........
    000000014004C020: 0000000000001000 0000000000000000   ................
    000000014004C030: 0000000000000019 3638782D74736F68   ........host-x86
    000000014004C040: 6E6B6E752D34365F 756E696C2D6E776F   _64-unknown-linu
    000000014004C050: 0000000000100078 00000000000D9800   x...............
    000000014004C060: 0000000000001F00 612D347670696800   .........hipv4-a
    000000014004C070: 6D612D6E6367646D 617368646D612D64   mdgcn-amd-amdhsa
    000000014004C080: 3630397866672D2D 0000000000000000   --gfx906........
    000000014004C090: 0000000000000000 0000000000000000   ................
    000000014004C0A0: 0000000000000000 0000000000000000   ................
    000000014004C0B0: 0000000000000000 0000000000000000   ................

:

We can see that the compiler embedded a version 4 code object (more on code [object versions](https://www.llvm.org/docs/AMDGPUUsage.html#code-object-metadata){.reference .external}) and used the LLVM target triple [`amdgcn-amd-amdhsa--gfx906`{.docutils .literal .notranslate}]{.pre} (more on [target triples](https://www.llvm.org/docs/AMDGPUUsage.html#target-triples){.reference .external}). Don't be alarmed about linux showing up as a binary format, AMDGPU binaries uploaded to the GPU for execution are proper linux ELF binaries in their format.

Alternatively we can call the compiler with [`--save-temps`{.docutils .literal .notranslate}]{.pre} to dump all device binary to disk in separate files.

:
{.highlight-powershell .notranslate}

highlight
    clang++ .\HIP-Basic\saxpy\main.hip -o saxpy.exe -I .\Common -lamdhip64 -L ${env:HIP_PATH}lib -O2 --save-temps

:

Now we can list all the temporaries created while compiling [`main.hip`{.docutils .literal .notranslate}]{.pre} via

:
{.highlight-powershell .notranslate}

highlight
    Get-ChildItem -Filter main-hip-* | select -Property Name

    Name
    ----
    main-hip-amdgcn-amd-amdhsa-gfx906.bc
    main-hip-amdgcn-amd-amdhsa-gfx906.hipi
    main-hip-amdgcn-amd-amdhsa-gfx906.o
    main-hip-amdgcn-amd-amdhsa-gfx906.out
    main-hip-amdgcn-amd-amdhsa-gfx906.out.resolution.txt
    main-hip-amdgcn-amd-amdhsa-gfx906.s

:

Files with the [`.s`{.docutils .literal .notranslate}]{.pre} extension hold the disassembled contents of the binary and the filename directly informs us of the graphics IPs used by the compiler.

:
{.highlight-powershell .notranslate}

highlight
    Get-ChildItem main-hip-*.s | Get-Content
            .text
            .amdgcn_target "amdgcn-amd-amdhsa--gfx906"
            .protected      _Z12saxpy_kernelfPKfPfj ; -- Begin function _Z12saxpy_kernelfPKfPfj
            .globl  _Z12saxpy_kernelfPKfPfj
            .p2align        8
            .type   _Z12saxpy_kernelfPKfPfj,@function
    _Z12saxpy_kernelfPKfPfj:                ; @_Z12saxpy_kernelfPKfPfj
    ; %bb.0:
            s_load_dword s0, s[4:5], 0x4
            s_load_dword s1, s[6:7], 0x18
            s_waitcnt lgkmcnt(0)
            s_and_b32 s0, s0, 0xffff
            s_mul_i32 s8, s8, s0
            v_add_u32_e32 v0, s8, v0
            v_cmp_gt_u32_e32 vcc, s1, v0
            s_and_saveexec_b64 s[0:1], vcc
            s_cbranch_execz .LBB0_2
    ; %bb.1:
            s_load_dwordx4 s[0:3], s[6:7], 0x8
            v_mov_b32_e32 v1, 0
            v_lshlrev_b64 v[0:1], 2, v[0:1]
            s_waitcnt lgkmcnt(0)
            v_mov_b32_e32 v3, s1
            v_add_co_u32_e32 v2, vcc, s0, v0
            v_addc_co_u32_e32 v3, vcc, v3, v1, vcc
            global_load_dword v2, v[2:3], off
            v_mov_b32_e32 v3, s3
            v_add_co_u32_e32 v0, vcc, s2, v0
            v_addc_co_u32_e32 v1, vcc, v3, v1, vcc
            global_load_dword v3, v[0:1], off
            s_load_dword s0, s[6:7], 0x0
            s_waitcnt vmcnt(0) lgkmcnt(0)
            v_fmac_f32_e32 v3, s0, v2
            global_store_dword v[0:1], v3, off
    .LBB0_2:
            s_endpgm
            ...

:
::::::::::
::::::::::::::::::::::::

Now that you've found what binary got embedded into the executable, find which format our available devices use.

::::::::::::::
{.sd-tab-set .docutils}
Linux

::::::
{.sd-tab-content .docutils}
On Linux a utility called [`rocminfo`{.docutils .literal .notranslate}]{.pre} helps us list all the properties of the devices available on the system, including which version of graphics IP ([`gfxXYZ`{.docutils .literal .notranslate}]{.pre}) they employ. You can filter the output to have only these lines:

:
{.highlight-bash .notranslate}

highlight
    /opt/rocm/bin/rocminfo | grep gfx
      Name:                    gfx906
          Name:                    amdgcn-amd-amdhsa--gfx906:sramecc+:xnack-

:

Now that you know which graphics IPs our devices use, recompile your program with the appropriate parameters.

:
{.highlight-bash .notranslate}

highlight
    amdclang++ ./HIP-Basic/saxpy/main.hip -o saxpy -I ./Common -lamdhip64 -L /opt/rocm/lib -O2 --offload-arch=gfx906:sramecc+:xnack-

:

Now the sample will run.

:
{.highlight-default .notranslate}

highlight
    ./saxpy
    Calculating y[i] = a * x[i] + y[i] over 1000000 elements.
    First 10 elements of the results: [ 3, 5, 7, 9, 11, 13, 15, 17, 19, 21 ]

:
::::::

Windows

::::::
{.sd-tab-content .docutils}
On Windows, a utility called [`hipInfo.exe`{.docutils .literal .notranslate}]{.pre} helps us list all the properties of the devices available on the system, including which version of graphics IP ([`gfxXYZ`{.docutils .literal .notranslate}]{.pre}) they employ. Filter the output to have only these lines:

:
{.highlight-powershell .notranslate}

highlight
    & ${env:HIP_PATH}bin\hipInfo.exe | Select-String gfx

    gcnArchName:                      gfx1032
    gcnArchName:                      gfx1035

:

Now that you know which graphics IPs our devices use, recompile your program with the appropriate parameters.

:
{.highlight-powershell .notranslate}

highlight
    clang++ .\HIP-Basic\saxpy\main.hip -o saxpy.exe -I .\Common -lamdhip64 -L ${env:HIP_PATH}lib -O2 --offload-arch=gfx1032 --offload-arch=gfx1035

:

Now the sample will run.

:
{.highlight-default .notranslate}

highlight
    .\saxpy.exe
    Calculating y[i] = a * x[i] + y[i] over 1000000 elements.
    First 10 elements of the results: [ 3, 5, 7, 9, 11, 13, 15, 17, 19, 21 ]

:
::::::
::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
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
