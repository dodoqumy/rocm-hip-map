---
title: "Building and installing rocFFT &#8212; rocFFT 1.0.36 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocFFT/en/latest/install/building-installing-rocfft.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:16:46.129198+00:00
content_hash: "f2bf1544a0af97e3"
---

# Building and installing rocFFT[#](#building-and-installing-rocfft)

This topic explains how to install rocFFT from the prebuilt packages or build it from the source code.

## Installing prebuilt packages[#](#installing-prebuilt-packages)

For information on downloading and installing ROCm, see the
[ROCm installation guide](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html).

To install rocFFT, use the package manager for your Linux distribution.

For example, on the Ubuntu distribution, run the following command:

```
apt update && sudo apt install rocfft
```

## Building rocFFT from source[#](#building-rocfft-from-source)

You can use the GitHub releases tab to download the source code. This might provide you with a more recent version than the prebuilt packages.

rocFFT uses the AMD clang++ compiler and CMake. You can specify several options to customize your build.
Use the following commands to build a shared library for the supported AMD GPUs.
Run these commands from the `rocm-libraries/projects/rocfft`

directory:

```
build && cd build
cmake -DCMAKE_CXX_COMPILER=amdclang++ -DCMAKE_C_COMPILER=amdclang ..
make -j
```

Note

To compile a static library, use the `-DBUILD_SHARED_LIBS=off`

option.

In ROCm version 4.3 or higher, indirect function calls are enabled for rocFFT by default.
Use `-DROCFFT_CALLBACKS_ENABLED=off`

with CMake to prevent these calls on older ROCm versions.

Note

If rocFFT is built with this configuration, callbacks won’t work correctly.

## rocFFT clients[#](#rocfft-clients)

rocFFT includes the following clients and utilities:

**rocfft-bench**: Runs general transforms and performance analysis**rocfft-test**: Runs a series of regression testsVarious samples


The following table includes the CMake option to build each client and the client dependencies.

Client |
CMake option |
Dependencies |
|---|---|---|
rocfft-bench |
|
hipRAND |
rocfft-test |
|
hipRAND, FFTW, GoogleTest |
samples |
|
none |

The clients are not built by default. To build them, use `-DBUILD_CLIENTS=on`

.
The build process downloads and builds GoogleTest and FFTW if they are not already installed.
rocFFT uses version 1.11 of GoogleTest.

You can build the clients separately from the main library.
For example, to build all the clients with an existing rocFFT library, invoke CMake from
within the `rocm-libraries/projects/rocfft/rocFFT-src/clients`

folder using these commands:

```
build && cd build
cmake -DCMAKE_CXX_COMPILER=amdclang++ -DCMAKE_PREFIX_PATH=/path/to/rocFFT-libb ..
make -j
```

To install the client dependencies on Ubuntu, run the following command:

```
apt install libgtest-dev libfftw3-dev libboost-dev
```

Note

`libboost-dev`

is the Boost development package. On Red Hat-related distributions,
these packages are named `gtest-devel`

, `fftw-devel`

and `boost-devel`

.
