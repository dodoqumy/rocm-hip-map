---
title: "Building and installing rocThrust on Windows and Linux with CMake &#8212; rocThrust Documentation 4.2.0 documentation"
source_url: "https://rocm.docs.amd.com/projects/rocThrust/en/latest/install/rocThrust-install-with-cmake.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:19:38.380583+00:00
content_hash: "db8a3f1efa1c9e95"
---

# Building and installing rocThrust on Windows and Linux with CMake[#](#building-and-installing-rocthrust-on-windows-and-linux-with-cmake)

You can build and install rocThrust with CMake on either Windows or Linux.

Set `CXX`

to `hipcc`

and set `CMAKE_CXX_COMPILER`

to hipcc’s absolute path. For example:

```
CXX=hipcc
CMAKE_CXX_COMPILER=/usr/bin/hipcc
```

After [cloning the project](rocThrust-install-overview.html), create the `build`

directory under the `rocthrust`

root directory, then change directory to the `build`

directory:

```
build
cd build
```

Generate the rocThrust makefile using the `cmake`

command:

```
../. [-D<OPTION1=VALUE1> [-D<OPTION2=VALUE2>] ...]
```

The build options are:

`DISABLE_WERROR`

. Set this to`OFF`

to pass`-Werror`

to the compiler. Default is`ON`

.`BUILD_TEST`

. Set this to`ON`

to enable rocThrust tests. Default is`OFF`

.`BUILD_HIPSTDPAR_TEST`

. Set this to`ON`

to enable HIPSTDPAR tests. Default is`OFF`

.`BUILD_BENCHMARK`

. Set this to`ON`

to build rocThrust benchmarks. Default is`OFF`

.`BUILD_EXAMPLE`

. Set this to`ON`

to build the rocThrust examples. Default is`OFF`

.`BUILD_OFFLOAD_COMPRESS`

. Set this to`OFF`

to prevent the`--offload-compress`

switch from being passed to the compiler and compressing the binary. On by default.`USE_SYSTEM_LIB`

. Set this to`ON`

to use the installed`ROCm`

libraries when building the tests. For this option to take effect,`BUILD_TEST`

must be set to`ON`

. Default is`OFF`

.`RNG_SEED_COUNT`

. Set this to the non-repeatable random dataset count. Default is 0.`PRNG_SEEDS`

. Set this to the RNG seeds. The seeds must be passed as a semicolon-delimited array of 32-bit unsigned integers. To avoid command line parsing errors, enclose the entire option in quotation marks. For example,`cmake "-DPRNG_SEEDS=1;2;3;4"`

.`-DPRNG_SEEDS=1`

is used by default.`BUILD_ADDRESS_SANITIZER`

. Set this to`ON`

to build with the Clang address sanitizer enabled. Default is`OFF`

.`EXTERNAL_DEPS_FORCE_DOWNLOAD`

. Set this to`ON`

to download the non-ROCm dependencies such as Google Test even if they’re already installed. Default is`OFF`

.`USE_HIPCXX`

. Set this to`ON`

to build with CMake HIP language support. Setting this to`ON`

eliminates the need to use`CXX=hipcc`

. Default is`OFF`

.`ROCPRIM_FETCH_METHOD`

and`ROCRAND_FETCH_METHOD`

. Set these to the method to use to download the rocPRIM and rocRAND components, respectively. Can be set to`PACKAGE`

,`DOWNLOAD`

, or`MONOREPO`

. Set to`MONOREPO`

if the component isn’t already installed and you’re building rocThrust from within a clone of the[rocm-libraries](https://github.com/ROCm/rocm-libraries/)repository that includes the component. Set to`DOWNLOAD`

if the component isn’t installed and you aren’t in a clone of the`rocm-libraries`

repository that includes the component.`DOWNLOAD`

will clone the repository using sparse checkout so that only the necessary files are downloaded. Set to`PACKAGE`

if the component is already installed. If the component isn’t installed, it’ll be downloaded form the repository in the same way as using the`DOWNLOAD`

option. The default method is`PACKAGE`

.

Note

If you’re using a version of git earlier than 2.25, `-DROCPRIM_FETCH_METHOD=DOWNLOAD`

and `-DROCRAND_FETCH_METHOD=DOWNLOAD`

will download the entire `rocm-libraries`

repository.

Build rocThrust using the generated make file:

```
-j4
```

After you’ve built rocThrust, you can optionally generate tar, zip, and deb packages:

```
package
```

Finally, install rocThrust:

```
install
```
