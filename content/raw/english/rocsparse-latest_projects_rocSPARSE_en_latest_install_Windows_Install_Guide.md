---
title: "Installing and building rocSPARSE for Microsoft Windows &#8212; rocSPARSE 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocSPARSE/en/latest/install/Windows_Install_Guide.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:16:44.325358+00:00
content_hash: "251dfd0cae11c14c"
---

# Installing and building rocSPARSE for Microsoft Windows[#](#installing-and-building-rocsparse-for-microsoft-windows)

This topic describes how to install or build rocSPARSE on Microsoft Windows by using prebuilt packages or building from source.
For information on installing and building rocSPARSE on Linux, see [rocSPARSE for Linux](Linux_Install_Guide.html).

## Prerequisites[#](#prerequisites)

rocSPARSE on Windows requires an AMD HIP SDK-enabled platform. It’s supported on the
same Windows versions and toolchains that the HIP SDK supports. For more information, see
[HIP SDK installation for Windows](https://rocm.docs.amd.com/projects/install-on-windows/en/latest/index.html).

## Installing prebuilt packages[#](#installing-prebuilt-packages)

rocSPARSE can be installed on Windows using the AMD HIP SDK installer.
For version support information, see the [System requirements for Windows](https://rocm.docs.amd.com/projects/install-on-windows/en/latest/reference/system-requirements.html).

The simplest way to add rocSPARSE to your code is to use CMake.
Add the SDK installation location to your `CMAKE_PREFIX_PATH`

.

Note

You must use quotes because the path contains a space.

```
="C:\Program Files\AMD\ROCm\7.0"
```

In your `CMakeLists.txt`

file, use these lines:

```
(rocsparse)
target_link_libraries( your_exe PRIVATE roc::rocsparse )
```

After rocSPARSE is installed, it can be used just like any other library with a C API.
To call rocSPARSE, the `rocsparse.h`

header file must be included in the user code.
This means the rocSPARSE import library and dynamic link library respectively become link-time and run-time dependencies
for the user application.

After the installation, you can find `rocsparse.h`

in the HIP SDK `\\include\\rocsparse`

directory. When you need to include rocSPARSE in your application code, you must only use these two files.
You can find the other rocSPARSE files included in the HIP SDK `\\include\\rocsparse\\internal`

directory, but
do not include these files directly in your source code.

## Building rocSPARSE from source[#](#building-rocsparse-from-source)

It isn’t necessary to build rocSPARSE from source because it’s ready to use after installing the prebuilt packages, as described above. To build rocSPARSE from source, follow the instructions in this section.

### Requirements[#](#requirements)

To compile and run rocSPARSE, the [AMD ROCm Platform](https://github.com/ROCm/ROCm) is required.
Building rocSPARSE from source also requires the following components and dependencies:

[CMake](https://cmake.org/)(Version 3.5 or later)[rocBLAS](https://github.com/ROCm/rocm-libraries/tree/develop/projects/rocblas)(Optional: for the library)[GoogleTest](https://github.com/google/googletest)(Optional: only required to build the clients)

When building rocSPARSE from source, select supported versions of the math library
dependencies ([rocPRIM](https://rocm.docs.amd.com/projects/rocPRIM/en/latest/index.html) and optionally [rocBLAS](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/index.html)). Given a version of rocSPARSE,
you must use a version of rocPRIM (and optionally rocBLAS) that is the same or later. For example, it’s
possible to build rocSPARSE 3.2.0 with any future rocPRIM 3.Y.Z version (with the same major version
and where 3.Y.Z is 3.2.0 or later), but compiling rocSPARSE with an older version of
rocPRIM, such as 3.1.0, is not supported.

### Downloading rocSPARSE[#](#downloading-rocsparse)

The rocSPARSE source code for Windows, which is the same as for Linux, is available
from the [rocSPARSE folder](https://github.com/ROCm/rocm-libraries/tree/develop/projects/rocsparse)
of the [rocm-libraries GitHub](https://github.com/ROCm/rocm-libraries).
The ROCm HIP SDK version might be shown in the default installation path, but
you can run the HIP SDK compiler from the `bin/`

folder to display the version using this command:

```
--version
```

The HIP version number consists of major, minor, and patch fields, and is sometimes followed by a build-specific identifier.
For example, the HIP version might be `5.4.22880-135e1ab4`

.
This corresponds to major release `5`

, minor release `4`

, patch `22880`

, and build identifier `135e1ab4`

.
The rocSPARSE GitHub includes branches with names like `release/rocm-rel-major.minor`

,
where major and minor have the same meaning as the HIP version.

To limit your local checkout to only the rocSPARSE project, configure `sparse-checkout`

before cloning.
This uses the Git partial clone feature (`--filter=blob:none`

) to reduce the data download.
Use the following commands for a sparse checkout:

Note

To include the rocPRIM and rocBLAS dependencies, set the projects for the sparse checkout using
`git sparse-checkout set projects/rocsparse projects/rocprim projects/rocblas`

.

```
clone --no-checkout --filter=blob:none https://github.com/ROCm/rocm-libraries.git
cd rocm-libraries
git sparse-checkout init --cone
git sparse-checkout set projects/rocsparse
git checkout release/rocm-rel-x.y # or use the branch you want to work with
```

Replace `x.y`

in the above command with the version of HIP SDK installed on your machine.
For example, if you have HIP 7.0 installed, use `-b release/rocm-rel-7.0`

.

To download all projects in rocm-libraries, use these commands. This process takes longer but is recommended for those working with a large number of libraries.

```
clone -b release/rocm-rel-x.y https://github.com/ROCm/rocm-libraries.git
cd rocm-libraries/projects/rocsparse
```

Note

To build ROCm 6.4.3 and earlier, use the rocSPARSE repository at [ROCm/rocSPARSE](https://github.com/ROCm/rocSPARSE).
For more information, see the documentation associated with the release you want to build.

Add the SDK tools to your path with an entry like the following:

```
\bin
```

### Building using the Python script[#](#building-using-the-python-script)

This section describes the steps required to build rocSPARSE using the `rmake.py`

script. You can build:

The library

The library and client


To call rocSPARSE from your code, you only need the library. The client contains testing and benchmark tools.
`rmake.py`

prints the full `cmake`

command being used to configure rocSPARSE based on the `rmake`

command line options.
This full `cmake`

command can be used in your own build scripts to bypass the Python helper script for a fixed set of build options.

#### Building the library from source[#](#building-the-library-from-source)

The following table lists the common ways to use `rmake.py`

to build the rocSPARSE library only.

Note

You can run `rmake.py`

from the `projects\rocsparse`

directory.

By default, rocBLAS is a dependency and the build will fail if it isn’t found.
To opt out of using rocBLAS when building from source with
the `rmake.py`

script, use the `no-rocblas`

option.

Command |
Description |
|---|---|
|
Print the help information. |
|
Build the library. |
|
Build the library, then build and install the rocSPARSE package. To keep rocSPARSE in your local tree, do not use the |
|
Build the library without rocBLAS, then build and install the rocSPARSE package. To keep rocSPARSE in your local tree, do not use the |
|
Build the library using only the gfx900 architecture, then build and install the rocSPARSE package. To keep rocSPARSE in your local tree, do not use the |

#### Building the library and client from source[#](#building-the-library-and-client-from-source)

The client executables (`.exe`

files) are listed in the table below:

Executable name |
Description |
|---|---|
rocsparse-test |
Runs Google Tests to test the library |
rocsparse-bench |
An executable to benchmark and test functions |
rocsparse_axpyi |
Example C code that calls the |

The following table lists the common ways to use `rmake.py`

to build the rocSPARSE library and client.

Command |
Description |
|---|---|
|
Print the help information. |
|
Build the library and client in your local directory. |
|
Build and install the rocSPARSE package and build the client. To keep rocSPARSE in your local directory, do not use the |
|
Build and install the rocSPARSE package without rocBLAS and build the client. To keep rocSPARSE in your local tree, do not use the |
|
Build and install the rocSPARSE package using only the gfx900 architecture and build the client. To keep rocSPARSE in your local tree, do not use the |
