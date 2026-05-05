---
title: "Building and installing hipBLASLt &#8212; hipBLASLt 1.2.2 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipBLASLt/en/latest/install/building-installing-hipblaslt.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:06:37.722923+00:00
content_hash: "7f85b611bebdee49"
---

# Building and installing hipBLASLt[#](#building-and-installing-hipblaslt)

This topic describes how to build and install hipBLASLt on Linux systems.

## Prerequisites[#](#prerequisites)

To install hipBLASLt, your system must include these components:

A ROCm-enabled platform. For more information, see the

[ROCm documentation](https://rocm.docs.amd.com/en/latest/index.html).A compatible version of

[hipBLAS](https://rocm.docs.amd.com/projects/hipBLAS/en/latest/index.html).

## Installing prebuilt packages[#](#installing-prebuilt-packages)

Download the prebuilt packages from the native package manager for your distribution.
For more information, see the [ROCm quick start installation guide](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html).

```
apt update && sudo apt install hipblaslt
```

## Building hipBLASLt using the install script[#](#building-hipblaslt-using-the-install-script)

You can use `install.sh`

script to build and install hipBLASLt and its dependencies.
The following sections explain how to use the `install.sh`

script, including the various script options.

### Building the library dependencies and library[#](#building-the-library-dependencies-and-library)

The root of the [hipblaslt folder](https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipblaslt)
in the [rocm-libraries](https://github.com/ROCm/rocm-libraries) GitHub repository contains the `install.sh`

Bash script for building and installing hipBLASLt with a single command.
It includes several options and hard-coded configuration items that can be specified through invoking CMake directly,
but it’s a great way to get started quickly and can serve as an example showing how to build and install hipBLASLt.
A few commands in the script require `sudo`

access, which might prompt you for a password.

Note

To build ROCm 6.4 and older, use the hipBLASLt repository at [ROCm/hipBLASLt](https://github.com/ROCm/hipBLASLt).
Select the documentation associated with the release you want to build.

Some typical examples showing how to use `install.sh`

to build the library dependencies and library are
listed in the table below:

Command |
Description |
|---|---|
|
Help information. |
|
Build the library and dependencies in your local directory. The |
|
Build the library in your local directory. This assumes the dependencies are already built. |
|
Build the library, then build and install the hipBLASLt package in |

### Building the library, client, and all dependencies[#](#building-the-library-client-and-all-dependencies)

This section explains how to build the library, client, library dependencies, and client dependencies. The client contains the executables listed in the table below.

Executable Name |
Description |
|---|---|
|
Runs GoogleTest tests to test the library |
|
Executable to benchmark or test individual functions |

Common ways to use `install.sh`

to build the dependencies, library, and client are
listed in the table below:

Command |
Description |
|---|---|
|
Help information. |
|
Build the library dependencies, client dependencies, library, and client in your local directory. The |
|
Build the library and client in your local directory. This assumes the dependencies are already built. |
|
Build the library dependencies, client dependencies, library, and client, then build and install the hipBLASLt package. This prompts you for |
|
Build and install the hipBLASLt package and build the client. This prompts you for |

### Static library[#](#static-library)

To build static libraries with `install.sh`

, use the `--static`

option.
This produces a non-standard static library build. This means it has an additional runtime dependency
consisting of the entire `hipblaslt/`

subdirectory, which is located in the `/opt/rocm/lib`

folder.
You can move this folder, but you must set the environment variable `HIPBLASLT_TENSILE_LIBPATH`

to the new location.

### Dependencies[#](#dependencies)

Dependencies are listed in the `install.sh`

script. Use `install.sh`

with the `-d`

option to install the dependencies.
CMake has a minimum version requirement which is listed in `install.sh`

.
See the `--cmake_install`

flag in `install.sh`

to upgrade automatically.

## Manual build for all supported platforms[#](#manual-build-for-all-supported-platforms)

This section provides information on how to configure CMake and build manually using individual commands.

### Building the library manually[#](#building-the-library-manually)

Before building hipBLASLt manually, ensure the following dependencies are installed on your system:

The

[hipBLAS-common](https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipblas-common)header files.The

[ROC-tracer (ROC-TX)](https://github.com/ROCm/rocm-systems/tree/develop/projects/roctracer)library (this is typically pre-installed).

#### Building hipBLASLt[#](#building-hipblaslt)

To build hipBLASLt, run these commands:

```
-p [HIPBLASLT_BUILD_DIR]/release
cd [HIPBLASLT_BUILD_DIR]/release
# Default install location is in /opt/rocm, define -DCMAKE_INSTALL_PREFIX=<path> to specify other
# Default build config is 'Release', define -DCMAKE_BUILD_TYPE=<config> to specify other
CXX=/opt/rocm/bin/amdclang++ ccmake [HIPBLASLT_SOURCE]
make -j$(nproc)
sudo make install # sudo required if installing into system directory such as /opt/rocm
```

### Building the library, tests, benchmarks, and samples manually[#](#building-the-library-tests-benchmarks-and-samples-manually)

The repository contains source code for clients that serve as samples, tests, and benchmarks.
You can find this code in the `clients`

subdirectory.

#### Dependencies for the hipBLASLt clients[#](#dependencies-for-the-hipblaslt-clients)

The hipBLASLt samples have no external dependencies, but the unit test and benchmarking applications do. These clients introduce the following dependencies:

[LAPACK](https://github.com/Reference-LAPACK/lapack-release), which adds a dependency on a Fortran compiler

#### Building the hipBLASLt clients[#](#building-the-hipblaslt-clients)

GoogleTest and LAPACK are not easy to install. Many Linux distributions don’t provide a GoogleTest package
with precompiled libraries and the LAPACK packages don’t have the necessary CMake configuration files
to allow the `cmake`

command to configure links with the `cblas`

library. hipBLASLt provides an optional CMake script that builds
the above dependencies from source. You can provide your own builds for
these dependencies and help `cmake`

find them by setting the `CMAKE_PREFIX_PATH`

definition.
Follow this sequence of steps to build the dependencies and install them to the default CMake directory `/usr/local`

.

Build the dependencies from source (optional).

-p [HIPBLASLT_BUILD_DIR]/release/deps cd [HIPBLASLT_BUILD_DIR]/release/deps ccmake -DBUILD_BOOST=OFF [HIPBLASLT_SOURCE]/deps # assuming boost is installed through package manager as above make -j$(nproc) install

After the dependencies are available on the system, configure the clients to build. This requires adding a few extra flags to the library CMake configuration script. If the dependencies are not installed in the system default directories, like

`/usr/local`

, pass the`CMAKE_PREFIX_PATH`

to`cmake`

to help CMake find them.="<semicolon separated paths>" # Default install location is in /opt/rocm, use -DCMAKE_INSTALL_PREFIX=<path> to specify other CXX=/opt/rocm/bin/amdclang++ ccmake -DBUILD_CLIENTS_TESTS=ON -DBUILD_CLIENTS_BENCHMARKS=ON [HIPBLASLT_SOURCE] make -j$(nproc) sudo make install # sudo required if installing into system directory such as /opt/rocm
