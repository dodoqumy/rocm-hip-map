---
title: "Library source code organization &#8212; hipBLAS 3.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipBLAS/en/latest/conceptual/library-source-code-organization.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:19:20.016088+00:00
content_hash: "4d5ad6347306d3da"
---

# Library source code organization[#](#library-source-code-organization)

The hipBLAS code is split into the following sections:

The

`library`

directory, which contains all source code for the libraryThe

`clients`

directory, which contains all test code and the code to build clientsInfrastructure


## The library directory[#](#the-library-directory)

The `library`

directory includes the following subdirectories.

### library/include[#](#library-include)

Contains C98 include files for the external API. These files include Doxygen comments that document the API.

### library/src/amd_detail[#](#library-src-amd-detail)

Implementation of the hipBLAS interface, which is compatible with the rocBLAS APIs.

### library/src/nvidia_detail[#](#library-src-nvidia-detail)

Implementation of the hipBLAS interface, which is compatible with the cuBLAS-v2 APIs.

### library/src/include[#](#library-src-include)

Internal include files for converting C++ exceptions to hipBLAS statuses.

## The clients directory[#](#the-clients-directory)

The `clients`

directory includes the following subdirectories.

### clients/gtest[#](#clients-gtest)

Code for the hipblas-test client. This client is used to test hipBLAS. For
more information, see [Using hipBLAS clients](../how-to/using-hipblas-clients.html#hipblas-clients).

### clients/benchmarks[#](#clients-benchmarks)

Code for the hipblas-bench client. This client is used to benchmark hipBLAS functions.
For more information, see [Using hipBLAS clients](../how-to/using-hipblas-clients.html#hipblas-clients).

### clients/include[#](#clients-include)

Code for testing and benchmarking individual hipBLAS functions and utility code for testing.

### clients/common[#](#clients-common)

Common code used by both hipblas-bench and hipblas-test.

### clients/samples[#](#clients-samples)

Sample code demonstrating how to call hipBLAS functions.

## Infrastructure[#](#infrastructure)

The following utilities support the hipBLAS infrastructure:

CMake is used to build and package hipBLAS. There are

`CMakeLists.txt`

files throughout the code.Doxygen, Breathe, Sphinx, and ReadTheDocs generate the documentation. The following sources supply content for the documentation:

Doxygen comments in the include files in the

`library/include`

directoryFiles in the

`docs`

directory

Jenkins is used to automate continuous integration (CI) testing.

clang-format is used to format C++ code.
