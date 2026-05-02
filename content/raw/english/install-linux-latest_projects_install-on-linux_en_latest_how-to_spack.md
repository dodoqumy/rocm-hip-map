---
title: "Using Spack to install ROCm packages"
source_url: "https://rocm.docs.amd.com/projects/install-on-linux/en/latest/how-to/spack.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:13:43.882086+00:00
content_hash: "755cdc3ba0efa0a9"
---

# Using Spack to install ROCm packages[#](#using-spack-to-install-rocm-packages)

2026-04-28

14 min read time

Spack is a package management tool designed to support multiple software versions and configurations on a wide variety of platforms and environments. It was designed for large supercomputing centers, where many users share common software installations on clusters with exotic architectures using libraries that do not have a standard ABI. Spack is non-destructive: installing a new version does not break existing installations, so many configurations can coexist on the same system.

Most importantly, Spack is simple. It offers a simple `spec`

syntax, so users
can concisely specify versions and configuration options. Spack is also simple
for package authors: package files are written in pure Python, and specs allow
package authors to maintain a single file for many different builds of the same
package.

See the [official Spack documentation](https://spack-tutorial.readthedocs.io/en/latest/) for more information.

## Installing prerequisites for Spack[#](#installing-prerequisites-for-spack)

Note

You must install all prerequisites before installing Spack.

```
# Install some essential utilities:
apt-get -y update
apt-get -y install make patch bash tar gzip unzip bzip2 file gnupg2 git gawk
apt-get -y update
apt-get -y install xz-utils
apt-get -y install build-essential
apt-get -y install vim
apt-get -y install libpci-dev
# Install Python:
apt-get -y install python3
apt-get -y upgrade python3-pip
# Install Compilers:
apt-get -y install gcc
apt-get -y install gfortran
apt-get -y install liblzma-dev
apt-get -y install libbz2-dev
```

```
# Install some essential utilities:
zypper update
zypper install make patch bash tar gzip unzip bzip xz file gnupg2 git awk
zypper in -t pattern
zypper install vim
# Install Python:
zypper install python3
zypper install python3-pip
# Install Compilers:
zypper install gcc
zypper install gcc-fortran
zypper install gcc-c++
```

## Building ROCm components using Spack[#](#building-rocm-components-using-spack)

To use the Spack package manager, clone the Spack project from

[spack/spack](https://github.com/spack/spack).clone https://github.com/spack/spack.git

Initialize Spack.

The

`setup-env.sh`

script initializes the Spack environment.cd spack . share/spack/setup-env.sh

Spack commands are available once the above steps are completed. To list the available commands, use

`help`

.help


After running `setup-env.sh`

, the develop branch of the [Spack packages repository](https://github.com/spack/spack-packages) will be cloned and used.

Note

To use your own local version of spack packages execute the following command:

```
repo set --destination /path/to/local/spack-packages builtin
```

## ROCm packages in Spack[#](#rocm-packages-in-spack)

Note

The supported ROCm components and their versions listed below were accurate as of the time of initial ROCm release. For the most up-to-date information, see the latest version of this information at [ROCm packages in Spack](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/how-to/spack.html#rocm-packages-in-spack).

Component |
Spack package name |
Minimum supported version |
Latest supported version |
|---|---|---|---|
AMD SMI |
|
5.6.0 |
7.2.1 |
aqlprofile |
|
7.0.0 |
7.2.1 |
comgr |
|
5.6.0 |
7.2.1 |
Composable Kernel |
|
5.6.0 |
7.2.1 |
devicelibs |
|
5.6.0 |
7.2.1 |
HIP (hip_in_vdi) |
|
5.6.0 |
7.2.1 |
hipBLAS |
|
5.6.0 |
7.2.1 |
hipBLAS-common |
|
6.3.0 |
7.2.1 |
hipBLASLt |
|
6.0.0 |
7.2.1 |
HIPCC |
|
5.7.0 |
7.2.1 |
hipCUB |
|
5.6.0 |
7.2.1 |
hipFFT |
|
5.6.0 |
7.2.1 |
hipfort |
|
5.6.0 |
7.2.1 |
HIPIFY |
|
5.6.0 |
7.2.1 |
hipRAND |
|
5.6.0 |
7.2.1 |
hipSOLVER |
|
5.6.0 |
7.2.1 |
hipSPARSE |
|
5.6.0 |
7.2.1 |
hipSPARSELt |
|
6.0.0 |
7.2.1 |
hipTensor |
|
5.7.0 |
7.2.1 |
HIP Tests |
|
6.1.0 |
7.2.1 |
llvm |
|
5.6.0 |
7.2.1 |
MIGraphX |
|
5.6.0 |
7.2.1 |
MIOpen (HIP) |
|
5.6.0 |
7.2.1 |
MIVisionX |
|
5.6.0 |
7.2.1 |
OpenCL |
|
5.6.0 |
7.2.1 |
openmp-extras |
|
5.6.0 |
7.2.1 |
RCCL |
|
5.6.0 |
7.2.1 |
rocAL |
|
6.2.0 |
7.2.1 |
rocALUTION |
|
5.6.0 |
7.2.1 |
rocBLAS |
|
5.6.0 |
7.2.1 |
ROCdbgapi |
|
5.6.0 |
7.2.1 |
rocDecode |
|
6.1.0 |
7.2.1 |
rocFFT |
|
5.6.0 |
7.2.1 |
rocJPEG |
|
6.3.0 |
7.2.1 |
rocm-core |
|
5.6.0 |
7.2.1 |
rocminfo |
|
5.6.0 |
7.2.1 |
rocMLIR |
|
5.4.0 |
7.2.1 |
ROCm Bandwidth Test |
|
5.6.0 |
7.2.1 |
ROCm CMake |
|
5.6.0 |
7.2.1 |
ROCm Compute Profiler |
|
6.3.2 |
7.2.1 |
ROCm Data Center Tool (RDC) |
|
5.6.0 |
7.2.1 |
ROCm Debug Agent |
|
5.6.0 |
7.2.1 |
ROCm Debugger (ROCgdb) |
|
5.6.0 |
7.2.1 |
ROCm Examples |
|
6.2.0 |
7.2.1 |
ROCm SMI Library |
|
5.6.0 |
7.2.1 |
ROCm Systems Profiler |
|
6.3.0 |
7.2.1 |
ROCm Validation Suite |
|
5.6.0 |
7.2.1 |
rocPRIM |
|
5.6.0 |
7.2.1 |
ROCProfiler |
|
5.6.0 |
7.2.1 |
rocprofiler-register |
|
6.1.0 |
7.2.1 |
ROCprofiler-SDK |
|
6.2.4 |
7.2.1 |
rocPyDecode |
|
6.2.0 |
7.2.1 |
rocRAND |
|
5.6.0 |
7.2.1 |
ROCr Runtime |
|
5.6.0 |
7.2.1 |
rocSHMEM |
|
6.4.0 |
7.2.1 |
rocSOLVER |
|
5.6.0 |
7.2.1 |
rocSPARSE |
|
5.6.0 |
7.2.1 |
rocThrust |
|
5.6.0 |
7.2.1 |
ROCTracer |
|
5.6.0 |
7.2.1 |
roctracer-dev-api |
|
5.6.0 |
7.2.1 |
rocWMMA |
|
5.6.0 |
7.2.1 |
ROCm Performance Primitives (RPP) |
|
5.7.0 |
7.2.1 |
TransferBench |
|
6.3.0 |
7.2.1 |
aqlprofile (old) |
|
5.6.0 |
6.4.3 (final) |
clang-ocl |
|
5.6.0 |
6.1.2 (final) |
Omniperf |
|
6.2.0 |
6.3.1 (final) |
Omnitrace |
|
rocm-6.2.0 |
rocm-6.3.0 (final) |
ROCT Thunk Interface |
|
5.6.0 |
6.2.4 (final) |
Tensile |
|
5.6.0 |
7.2.1 |

## Installing ROCm components using Spack[#](#installing-rocm-components-using-spack)

`rocm-cmake`

Install the default variants and the latest version of

`rocm-cmake`

.install rocm-cmake

To install a specific version of

`rocm-cmake`

, use:install rocm-cmake@<version number>

For example,

`spack install rocm-cmake@7.2.1`

`info`

The

`info`

command displays basic package information. It shows the preferred, safe, and deprecated versions, in addition to the available variants. It also shows the dependencies with other packages.info mivisionx

For example:

$ spack info mivisionx CMakePackage: mivisionx Description: MIVisionX toolkit is a set of comprehensive computer vision and machine intelligence libraries, utilities, and applications bundled into a single toolkit. Homepage: https://github.com/ROCm/MIVisionX Preferred version: 7.2.1 https://github.com/ROCm/MIVisionX/archive/rocm-7.2.1.tar.gz Safe versions: 7.2.1 https://github.com/ROCm/MIVisionX/archive/rocm-7.2.1.tar.gz 7.2.0 https://github.com/ROCm/MIVisionX/archive/rocm-7.2.0.tar.gz 7.1.1 https://github.com/ROCm/MIVisionX/archive/rocm-7.1.1.tar.gz 7.1.0 https://github.com/ROCm/MIVisionX/archive/rocm-7.1.0.tar.gz 7.0.2 https://github.com/ROCm/MIVisionX/archive/rocm-7.0.2.tar.gz 7.0.0 https://github.com/ROCm/MIVisionX/archive/rocm-7.0.0.tar.gz 6.4.3 https://github.com/ROCm/MIVisionX/archive/rocm-6.4.3.tar.gz 6.4.3 https://github.com/ROCm/MIVisionX/archive/rocm-6.4.3.tar.gz 6.4.2 https://github.com/ROCm/MIVisionX/archive/rocm-6.4.2.tar.gz 6.4.1 https://github.com/ROCm/MIVisionX/archive/rocm-6.4.1.tar.gz 6.4.0 https://github.com/ROCm/MIVisionX/archive/rocm-6.4.0.tar.gz 6.3.3 https://github.com/ROCm/MIVisionX/archive/rocm-6.3.3.tar.gz 6.3.2 https://github.com/ROCm/MIVisionX/archive/rocm-6.3.2.tar.gz 6.3.1 https://github.com/ROCm/MIVisionX/archive/rocm-6.3.1.tar.gz 6.3.0 https://github.com/ROCm/MIVisionX/archive/rocm-6.3.0.tar.gz 6.2.4 https://github.com/ROCm/MIVisionX/archive/rocm-6.2.4.tar.gz 6.2.1 https://github.com/ROCm/MIVisionX/archive/rocm-6.2.1.tar.gz 6.2.0 https://github.com/ROCm/MIVisionX/archive/rocm-6.2.0.tar.gz 6.1.2 https://github.com/ROCm/MIVisionX/archive/rocm-6.1.2.tar.gz 6.1.1 https://github.com/ROCm/MIVisionX/archive/rocm-6.1.1.tar.gz 6.1.0 https://github.com/ROCm/MIVisionX/archive/rocm-6.1.0.tar.gz 6.0.2 https://github.com/ROCm/MIVisionX/archive/rocm-6.0.2.tar.gz 6.0.0 https://github.com/ROCm/MIVisionX/archive/rocm-6.0.0.tar.gz 5.7.1 https://github.com/ROCm/MIVisionX/archive/rocm-5.7.1.tar.gz 5.7.0 https://github.com/ROCm/MIVisionX/archive/rocm-5.7.0.tar.gz Deprecated versions: None Variants: add_tests [false] false, true add tests and samples folder asan [false] false, true Build with address-sanitizer enabled or disabled build_system [cmake] cmake Build systems supported by the package hip [true] false, true Use HIP as backend when build_system=cmake build_type [Release] Debug, MinSizeRel, RelWithDebInfo, Release CMake build type generator [make] none the build system generator to use when build_system=cmake ^cmake@3.9: ipo [false] false, true CMake interprocedural optimization Build Dependencies: cmake ffmpeg hip libjpeg-turbo lmdb miopen-hip opencv protobuf py-google-api-python-client py-protobuf py-pytz py-wheel rapidjson rpp cxx gmake hsa-rocr-dev llvm-amdgpu migraphx ninja openssl py-future py-numpy py-pybind11 py-setuptools python rocm-core Link Dependencies: hip hsa-rocr-dev llvm-amdgpu lmdb migraphx miopen-hip openssl py-future py-google-api-python-client py-numpy py-pybind11 py-pytz py-setuptools py-wheel rapidjson rocm-core rpp Run Dependencies: py-protobuf Licenses: MIT


## Installing variants for ROCm components[#](#installing-variants-for-rocm-components)

The variants listed above indicate that the `mivisionx`

package is built by
default with `build_type=Release`

and the `hip`

backend, and without the
`opencl`

backend. `build_type=Debug`

and `RelWithDebInfo`

, with `opencl`

and without `hip`

, are also supported.

For example:

```
install mivisionx build_type=Debug #Backend will be hip since it is the default one
spack install mivisionx+opencl build_type=Debug #Backend will be opencl and hip will be disabled as per the conflict defined in recipe
```

`spack spec`

commandTo display the dependency tree, the

`spack spec`

command can be used with the same format.For example:

$ spack spec mivisionx - mivisionx@7.2.1%gcc@13.2.0~add_tests~asan+hip~ipo~opencl build_system=cmake build_type=Release generator=make arch=linux-ubuntu24.04-skylake_avx512 - ^cmake@3.28.3%gcc@13.2.0~doc+ncurses+ownlibs~qtgui build_system=generic build_type=Release patches=dbc3892 arch=linux-ubuntu24.04-skylake_avx512 - ^ffmpeg@4.4.4%gcc@13.2.0~X~avresample+bzlib~doc~drawtext+gpl~libaom~libmp3lame~libopenjpeg~libopus~libsnappy~libspeex~libssh~libvorbis~libvpx~libwebp~libx264~libxml2~libzmq~lzma~nonfree~openssl~sdl2+shared+version3 build_system=autotools patches=f070ac1 arch=linux-ubuntu24.04-skylake_avx512 - ^alsa-lib@1.2.3.2%gcc@13.2.0~python build_system=autotools arch=linux-ubuntu24.04-skylake_avx512 - ^bzip2@1.0.8%gcc@13.2.0~debug~pic+shared build_system=generic arch=linux-ubuntu24.04-skylake_avx512 - ^libiconv@1.17%gcc@13.2.0 build_system=autotools libs=shared,static arch=linux-ubuntu24.04-skylake_avx512 ...


## Creating an environment[#](#creating-an-environment)

You can create an environment with all the required components of your version, install them collectively, and work in the environment.

Create a Spack environment.

env create myenv

Activate the created environment.

env activate myenv

Add the ROCm packages.

add rocm-cmake@7.2.1 rocm-dbgapi@7.2.1 rocm-debug-agent@7.2.1 rocm-gdb@7.2.1 rocminfo@7.2.1 \ rocm-opencl@7.2.1 rocm-smi-lib@7.2.1 rocprim@7.2.1 rocprofiler-dev@7.2.1 rocrand@7.2.1 \ rocthrust@7.2.1 roctracer-dev@7.2.1

Generate the build plan.

`concretize`

Install the packages.

`install`


## Creating and applying a patch before installation[#](#creating-and-applying-a-patch-before-installation)

Spack installs ROCm packages after pulling the source code from GitHub and building it locally. In order to build a component with any modification to the source code, you must generate a patch and apply it before the build phase.

To generate a patch and build with the changes:

Stage the source code. For example:

stage hip@7.2.1 # (This will pull the 7.2.1 release version source code of hip and display the path to spack-src directory where entire source code is available)

You should see something like this:

==> Using cached archive: /data/root/temp/rocm-7.2.1/spack/var/spack/cache/_source-cache/archive/d8/d8dba8cdf05463afb7879de2833983cafa6a006ba719815a35b96d9b92fc7fc4.tar.gz ==> Using cached archive: /data/root/temp/rocm-7.2.1/spack/var/spack/cache/_source-cache/archive/82/829e61a5c54d0c8325d02b0191c0c8254b5740e63b8bfdb05eec9e03d48f7d2c.tar.gz ==> Using cached archive: /data/root/temp/rocm-7.2.1/spack/var/spack/cache/_source-cache/archive/80/8081d4ab1a43ffa1cebd646668d83008b799ab98c14daf7b455922355a439c8a.tar.gz ==> Moving resource stage source: /tmp/root/spack-stage/resource-clr-zo53ondw3tevsr3gmoofbhre7asvis46/spack-src/ destination: /tmp/root/spack-stage/spack-stage-hip-7.2.1-zo53ondw3tevsr3gmoofbhre7asvis46/spack-src/clr ==> Moving resource stage source: /tmp/root/spack-stage/resource-hip-tests-zo53ondw3tevsr3gmoofbhre7asvis46/spack-src/ destination: /tmp/root/spack-stage/spack-stage-hip-7.2.1-zo53ondw3tevsr3gmoofbhre7asvis46/spack-src/hip-tests ==> Staged hip in /tmp/root/spack-stage/spack-stage-hip-7.2.1-zo53ondw3tevsr3gmoofbhre7asvis46

Change directory to

`spack-src`

inside the staged directory./spack$ cd /tmp/root/spack-stage/spack-stage-hip-7.2.1-zo53ondw3tevsr3gmoofbhre7asvis46 /tmp/root/spack-stage/spack-stage-hip-7.2.1-zo53ondw3tevsr3gmoofbhre7asvis46$ cd spack-src/

Create a new Git repository.

git init

Add the entire directory to the repository.

git add .

Make the required changes to the source code.

vi hipamd/CMakeLists.txt # Make required changes in the source code

Generate the patch using the

`git diff`

command.> /spack/var/spack/repos/builtin/packages/hip/0001-modifications.patch /tmp/root/spack-stage/spack-stage-hip-7.2.1-zo53ondw3tevsr3gmoofbhre7asvis46/spack-src$ git diff > /spack/var/spack/repos/builtin/packages/hip/0001-modifications.patch

Update the recipe with the patch file name and any conditions you want to apply.

spack edit hip

Provide the patch file name and the conditions for the patch to be applied in the

`hip`

recipe as follows.("0001-modifications.patch", when="@7.2.1")

Spack will apply

`0001-modifications.patch`

on the 7.2.1 release code before starting the`hip`

build.After each modification, you must update the recipe. If there is no change to the recipe, run

`/spack/var/spack/repos/builtin/packages/hip/package.py`
