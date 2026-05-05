---
title: "Prerequisites for hipBLAS installation &#8212; hipBLAS 3.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipBLAS/en/latest/install/prerequisites.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:19:09.967456+00:00
content_hash: "cea578c7ebe57d5b"
---

# Prerequisites for hipBLAS installation[#](#prerequisites-for-hipblas-installation)

The following prerequisites are required to install hipBLAS, whether by using a package manager or building the application from the source code.

## Prerequisites for Linux[#](#prerequisites-for-linux)

The hipBLAS prerequisites are different than the [rocBLAS](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/index.html) and NVIDIA CUDA [cuBLAS](https://developer.nvidia.com/cublas) backend prerequisites.

The prerequisites required to use the rocBLAS backend with AMD components are as follows:

A ROCm-enabled platform. For more information, see the

[Linux system requirements](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html).A compatible version of

[hipblas-common](https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipblas-common).A compatible version of rocBLAS.

For full functionality, optionally install a compatible version of

[rocSOLVER](https://rocm.docs.amd.com/projects/rocSOLVER/en/latest/index.html)and its[rocSPARSE](https://rocm.docs.amd.com/projects/rocSPARSE/en/latest/index.html)and[rocPRIM](https://rocm.docs.amd.com/projects/rocPRIM/en/latest/index.html)dependencies.

The prerequisites required to use the cuBLAS backend with NVIDIA components are as follows:

A HIP-enabled platform. For more information, see

[HIP installation](https://rocm.docs.amd.com/projects/HIP/en/latest/install/install.html).A working CUDA toolkit, including cuBLAS. For more information, see

[CUDA toolkit](https://developer.nvidia.com/accelerated-computing-toolkit/).


## Prerequisites for Microsoft Windows[#](#prerequisites-for-microsoft-windows)

Here are the prerequisites required to use the rocBLAS backend with AMD components:

An AMD HIP SDK-enabled platform. For more information, see

[Windows system requirements](https://rocm.docs.amd.com/projects/install-on-windows/en/latest/reference/system-requirements.html).A compatible version of

[hipblas-common](https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipblas-common).A compatible version of rocBLAS.

For full functionality, a compatible version of

[rocSOLVER](https://rocm.docs.amd.com/projects/rocSOLVER/en/latest/index.html)and its[rocSPARSE](https://rocm.docs.amd.com/projects/rocSPARSE/en/latest/index.html)and[rocPRIM](https://rocm.docs.amd.com/projects/rocPRIM/en/latest/index.html)dependencies.hipBLAS is supported on the same Windows versions and toolchains that HIP SDK supports.


hipBLAS does not support the cuBLAS backend on Windows.
