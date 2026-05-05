---
title: "Building and installing hipFFT and hipFFTW &#8212; hipFFT 1.0.22 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipFFT/en/latest/install/building-installing-hipfft-and-hipfftw.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:07:23.518508+00:00
content_hash: "99d85e0b26c770d3"
---

# Building and installing hipFFT and hipFFTW[#](#building-and-installing-hipfft-and-hipfftw)

This topic explains how to install hipFFT and hipFFTW from the prebuilt packages or build it from the source code.
hipFTT and hipFFTW require a ROCm-enabled platform. For more information,
see the [Linux system requirements](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html).

## Installing prebuilt packages[#](#installing-prebuilt-packages)

For information on downloading and installing ROCm, see the
[ROCm installation guide](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html).

To install hipFFT and hipFFTW, use the package manager for the Linux distribution, which handles all dependencies. This lets you run programs that use hipFFT or hipFFTW, but not compile them.

On the Ubuntu distribution, run the following command:

```
apt update && sudo apt install hipfft
```

Note

To compile programs, you must install the development package, which
contains the header files and CMake infrastructure.
This package is named `hipfft-dev`

on Ubuntu/Debian systems and
`hipfft-devel`

on RHEL and related variants.

## Building hipFFT and hipFFTW from source[#](#building-hipfft-and-hipfftw-from-source)

To build hipFFT and hipFFTW from source, follow these steps:

Install the library build dependencies:

On AMD platforms, install

[rocFFT](https://rocm.docs.amd.com/projects/rocFFT/en/latest/index.html). To build from source, rocFFT must be installed with the development headers. These headers can be added by installing the`rocfft-dev`

or`rocfft-devel`

package. If rocFFT was built from source, then these headers are already included.Install the client build dependencies for the clients:

The clients that are included with the source code, including samples and tests, depend on

[hipRAND](https://rocm.docs.amd.com/projects/hipRAND/en/latest/index.html),[FFTW](https://fftw.org/),[boost](https://www.boost.org/), and GoogleTest.Build hipFFT and hipFFTW:

To show all build options, run these commands from the

`rocm-libraries/projects/hipfft`

directory:build && cd build cmake -LH ..

Here are some CMake build examples for AMD GPUs:

Building a project using

[HIP language](https://rocm.docs.amd.com/projects/HIP/en/latest/index.html)APIs and hipFFT (or hipFFTW) with the standard host compiler:-DCMAKE_CXX_COMPILER=g++ -DCMAKE_BUILD_TYPE=Release -L ..

Building a project using HIP language APIs, hipFFT (or hipFFTW), and device kernels with HIP-Clang:

-DCMAKE_CXX_COMPILER=amdclang++ -DCMAKE_BUILD_TYPE=Release -DBUILD_CLIENTS=ON -L ..


Note

The

`-DBUILD_CLIENTS=ON`

option is only allowed with the amdclang++ or HIPCC compilers.
