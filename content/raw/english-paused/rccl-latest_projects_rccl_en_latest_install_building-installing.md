---
title: "Building and installing RCCL from source code &#8212; RCCL 2.27.7 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rccl/en/latest/install/building-installing.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:23:11.661369+00:00
content_hash: "0fa2d53499701140"
---

# Building and installing RCCL from source code[#](#building-and-installing-rccl-from-source-code)

To build RCCL directly from the source code, follow these steps. This guide also includes
instructions explaining how to test the build.
For information on using the quick start install script to build RCCL, see [Installing RCCL using the install script](installation.html).

## Requirements[#](#requirements)

The following prerequisites are required to build RCCL:

ROCm-supported GPUs

Having the ROCm stack installed on the system, including the

[HIP runtime](https://rocm.docs.amd.com/projects/HIP/en/latest/index.html)and the HIP-Clang compiler.

### Building the library using CMake:[#](#building-the-library-using-cmake)

To build the library from source, follow these steps:

```
clone --recursive https://github.com/ROCm/rccl.git
cd rccl
mkdir build
cd build
cmake ..
make -j 16 # Or some other suitable number of parallel jobs
```

If you have already cloned the repository, you can checkout the external submodules manually.

```
submodule update --init --recursive --depth=1
```

You can substitute a different installation path by providing the path as a parameter
to `CMAKE_INSTALL_PREFIX`

, for example:

```
-DCMAKE_INSTALL_PREFIX=$PWD/rccl-install -DCMAKE_BUILD_TYPE=Release ..
```

Note

Ensure ROCm CMake is installed using the command `apt install rocm-cmake`

. By default,
CMake builds the component in debug mode unless `DCMAKE_BUILD_TYPE`

is specified.

### Building the RCCL package and install package:[#](#building-the-rccl-package-and-install-package)

After you have cloned the repository and built the library as described in the previous section, use this command to build the package:

```
cd rccl/build
make package
sudo dpkg -i *.deb
```

Note

The RCCL package install process requires `sudo`

or root access because it creates a directory
named `rccl`

in `/opt/rocm/`

. This is an optional step. RCCL can be used directly by including the path containing `librccl.so`

.

## Testing RCCL[#](#testing-rccl)

The RCCL unit tests are implemented using the Googletest framework in RCCL. These unit tests require Googletest 1.10
or higher to build and run (this dependency can be installed using the `-d`

option for `install.sh`

).
To run the RCCL unit tests, go to the `build`

folder and the `test`

subfolder,
then run the appropriate RCCL unit test executables.

The RCCL unit test names follow this format:

```
[Type of test]
```

Filtering of the RCCL unit tests can be done using environment variables
and by passing the `--gtest_filter`

command line flag:

```
UT_DATATYPES=ncclBfloat16 UT_REDOPS=prod ./rccl-UnitTests --gtest_filter="AllReduce.C*"
```

This command runs only the `AllReduce`

correctness tests with the `float16`

datatype.
A list of the available environment variables for filtering appears at the top of every run.
See the [Googletest documentation](https://google.github.io/googletest/advanced.html#running-a-subset-of-the-tests)
for more information on how to form advanced filters.

There are also other performance and error-checking tests for RCCL. They are maintained separately at [ROCm/rccl-tests](https://github.com/ROCm/rccl-tests).
