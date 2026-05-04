---
title: "Installing RCCL using the install script &#8212; RCCL 2.27.7 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rccl/en/latest/install/installation.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:22:56.852832+00:00
content_hash: "097df88bd9e19ad1"
---

# Installing RCCL using the install script[#](#installing-rccl-using-the-install-script)

To quickly install RCCL using the install script, follow these steps.
For instructions on building RCCL from the source code, see [Building and installing RCCL from source code](building-installing.html).
For additional tips, see [RCCL usage tips](../how-to/rccl-usage-tips.html).

## Requirements[#](#requirements)

The following prerequisites are required to use RCCL:

ROCm-supported GPUs

The ROCm stack must be installed on the system, including the

[HIP runtime](https://rocm.docs.amd.com/projects/HIP/en/latest/index.html)and the HIP-Clang compiler.

## Quick start RCCL build[#](#quick-start-rccl-build)

RCCL directly depends on the HIP runtime plus the HIP-Clang compiler, which are part of the ROCm software stack.
For ROCm installation instructions, see the [package manager installation guide](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/install-methods/package-manager-index.html).

Use the [install.sh helper script](https://github.com/ROCm/rccl/blob/develop/install.sh),
located in the root directory of the RCCL repository,
to build and install RCCL with a single command. It uses hard-coded configurations that can be specified directly
when using cmake. However, it’s a great way to get started quickly and provides an
example of how to build and install RCCL.

### Building the library using the install script:[#](#building-the-library-using-the-install-script)

To build the library using the install script, use this command:


For more information on the build options and flags for the install script, run the following command:

```
--help
```

The RCCL build and installation helper script options are as follows:

```
--address-sanitizer Build with address sanitizer enabled
-d|--dependencies Install RCCL dependencies
--debug Build debug library
--enable_backtrace Build with custom backtrace support
--disable-colltrace Build without collective trace
--disable-msccl-kernel Build without MSCCL kernels
--enable-mscclpp Build with MSCCL++ support
-f|--fast Quick-build RCCL (local gpu arch only, no backtrace, and collective trace support)
-h|--help Prints this help message
-i|--install Install RCCL library (see --prefix argument below)
-j|--jobs Specify how many parallel compilation jobs to run ($nproc by default)
-l|--local_gpu_only Only compile for local GPU architecture
--amdgpu_targets Only compile for specified GPU architecture(s). For multiple targets, separate by ';' (builds for all supported GPU architectures by default)
--no_clean Don't delete files if they already exist
--npkit-enable Compile with npkit enabled
--openmp-test-enable Enable OpenMP in rccl unit tests
--roctx-enable Compile with roctx enabled (example usage: rocprof --roctx-trace ./rccl-program)
-p|--package_build Build RCCL package
--prefix Specify custom directory to install RCCL to (default: `/opt/rocm`)
--rm-legacy-include-dir Remove legacy include dir Packaging added for file/folder reorg backward compatibility
--run_tests_all Run all rccl unit tests (must be built already)
-r|--run_tests_quick Run small subset of rccl unit tests (must be built already)
--static Build RCCL as a static library instead of shared library
-t|--tests_build Build rccl unit tests, but do not run
--time-trace Plot the build time of RCCL (requires `ninja-build` package installed on the system)
--verbose Show compile commands
```

Tip

By default, the RCCL install script builds all the GPU targets that are defined in `DEFAULT_GPUS`

in [CMakeLists.txt](https://github.com/ROCm/rccl/blob/develop/CMakeLists.txt).
To target specific GPUs and potentially reduce the build time, use `--amdgpu_targets`

along with
a semicolon (`;`

) separated string list of the GPU targets.
