---
title: "hipBLASLt library source code organization &#8212; hipBLASLt 1.2.2 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipBLASLt/en/latest/conceptual/hipblaslt-library-organization.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:21:07.812427+00:00
content_hash: "71c17d1b3868ba76"
---

# hipBLASLt library source code organization[#](#hipblaslt-library-source-code-organization)

The hipBLASLt source code resides in the following two directories:

The

`library`

directory contains all source code for the library.The

`clients`

directory contains all test code and the code to build the clients.

## The library directory[#](#the-library-directory)

Here are the subdirectories within the `library`

directory:

`library/include`

Contains C98 include files for the external API. These files also contain Doxygen comments that document the API.

`library/src/amd_detail`

Contains the implementation of the hipBLASLt interface that is compatible with the rocBLASLt APIs.

`library/src/include`

Contains internal include files for converting C++ exceptions to hipBLAS statuses.


## The clients directory[#](#the-clients-directory)

Here is the subdirectory within the `clients`

directory:

`clients/samples`

Contains sample code for calling the hipBLASLt functions.


## Infrastructure[#](#infrastructure)

`CMake`

is used to build and package hipBLASLt. There are`CMakeLists.txt`

files throughout the code.Doxygen, Breathe, Sphinx, and ReadTheDocs generate the documentation based on these sources:

Doxygen comments in the

`include`

files in the`library/include`

directory.Files in the

`docs/source`

directory.

Jenkins is used to automate continuous integration testing.

`clang-format`

is used to format the C++ code.
