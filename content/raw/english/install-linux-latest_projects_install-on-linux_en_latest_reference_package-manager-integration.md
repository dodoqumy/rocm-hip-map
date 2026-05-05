---
title: "Package details"
source_url: "https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/package-manager-integration.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:13:55.288186+00:00
content_hash: "80461af2e9930f4c"
---

# Package details[#](#package-details)

2026-03-10

7 min read time

This section provides information about the required meta-packages for the following AMD ROCm programming models:

Heterogeneous-Computing Interface for Portability (HIP)

OpenCL™

OpenMP™


## ROCm package naming conventions[#](#rocm-package-naming-conventions)

A meta-package is a grouping of related packages and dependencies used to support a specific use case.

**Example:** Running HIP applications

All meta-packages exist in both versioned and non-versioned forms.

Non-versioned packages: For a single-version installation of the ROCm stack

Versioned packages: For multi-version installations of the ROCm stack


The figure above demonstrates the single and multi-version ROCm packages’ naming structure, including examples for various Linux distributions. See terms below:

*Module* - It is the part of the package that represents the name of the ROCm
component.

**Example:** The examples mentioned in the image represent the ROCm HIP module.

*Module version* - It is the version of the library released in that package. It
should increase with a newer release.

*Release version* - It shows the ROCm release version when the package was
released.

**Example:** 50400 points to the ROCm 5.4.0 release.

*Build id* - It represents the build number for that release.

*Arch* - It shows the architecture for which the package was created.

*Distro* - It describes the distribution for which the package was created. It is
valid only for rpm packages.

**Example:** el8 represents RHEL 8.x packages.

## Components of ROCm programming models[#](#components-of-rocm-programming-models)

The figure below demonstrates the high-level layered architecture of ROCm programming models and their meta-packages. All meta-packages are a combination of required packages and libraries.


Note

The preceding figure is for informational purposes only. The individual packages in a meta-package are subject to change. To avoid conflicts, install meta-packages, not individual packages.

**Example:**

`rocm-hip-runtime`

is used to deploy on supported machines to execute HIP applications.`rocm-hip-sdk`

contains runtime components to deploy and execute HIP applications.

Note

`rocm-llvm`

is not a meta-package; it’s a single package that installs the ROCm Clang compiler files.

ROCm installation can be tailored to your requirements using one more combinations of ROCm meta packages:

To use pre-built ROCm libraries and tools, include

[ROCm runtime packages](#rocm-runtime)in the installation step.To develop and build individual ROCm libraries and tools, include

[ROCm developer packages](#rocm-dev)in the installation step.

### ROCm runtime packages[#](#rocm-runtime-packages)

Meta package |
Description |
Legacy use case |
|---|---|---|
|
All ROCm core packages, tools, and libraries. |
|
|
HIP libraries optimized for the AMD platform. |
Legacy use case does not exist. |
|
Run HIP applications written for the AMD platform. |
|
|
ROCm runtime environment for running applications on the AMD platform. |
|
|
Key machine learning libraries. Includes MIOpen. |
|
|
Run OpenCL-based applications on the AMD platform. |
|
|
||
|
For users of graphics applications which require the open source Mesa 3D graphics and multimedia libraries. This package is primarily used for Radeon GPUs. |
|

### ROCm developer packages[#](#rocm-developer-packages)

Meta package |
Description |
Legacy use case |
|---|---|---|
|
Debug and profile HIP applications. |
|
|
Develop applications on HIP or port from CUDA. |
Legacy use case does not exist. |
|
Develop or port HIP applications and libraries for the AMD platform. |
|
|
Develop and run machine learning applications for AMD. |
|
|
Develop OpenCL-based applications for the AMD platform. |
|
|
Develop OpenMP-based applications for the AMD software. |
|

Footnotes

## Packages in ROCm programming models[#](#packages-in-rocm-programming-models)

The following tables show the meta-packages and their associated (meta-)packages in a ROCm programming model.

Note

Some meta packages and dependencies in the tables below have names ending with `-dev`

, as they are based on Ubuntu.
On RPM-based systems like RHEL, these packages use a different naming convention and typically end with `-devel`

instead.

### ROCm runtime packages[#](#id5)

Meta package |
Associated meta packages or packages |
|---|---|
|
Meta packages: Packages: |
|
Meta package: Packages: |
|
Meta package: Packages: |
|
Packages: |
|
Meta package: Packages: |
|
Meta package: Packages: |

### ROCm developer packages[#](#id6)

Meta package |
Associated meta packages or packages |
|---|---|
|
Packages: |
|
Meta package: Packages: |
|
Meta packages: Packages: |
|
Meta packages: Packages: |
|
Packages: |
|
Meta package: Packages: |
