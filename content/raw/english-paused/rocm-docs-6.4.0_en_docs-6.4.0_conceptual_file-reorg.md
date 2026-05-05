---
title: "ROCm Linux Filesystem Hierarchy Standard reorganization"
source_url: "https://rocm.docs.amd.com/en/docs-6.4.0/conceptual/file-reorg.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:21:25.424989+00:00
content_hash: "1104e2793559b8ae"
---

# ROCm Linux Filesystem Hierarchy Standard reorganization[#](#rocm-linux-filesystem-hierarchy-standard-reorganization)

2025-04-07

7 min read time

## Introduction[#](#introduction)

The ROCm Software has adopted the Linux Filesystem Hierarchy Standard (FHS) [https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html) in order to to ensure ROCm is consistent with standard open source conventions. The following sections specify how current and future releases of ROCm adhere to FHS, how the previous ROCm file system is supported, and how improved versioning specifications are applied to ROCm.

## Adopting the FHS[#](#adopting-the-fhs)

In order to standardize ROCm directory structure and directory content layout ROCm has adopted the [FHS](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html), adhering to open source conventions for Linux-based distribution. FHS ensures internal consistency within the ROCm stack, as well as external consistency with other systems and distributions. The ROCm proposed file structure is outlined below:


## Changes from earlier ROCm versions[#](#changes-from-earlier-rocm-versions)

The following table provides a brief overview of the new ROCm FHS layout, compared to the layout of earlier ROCm versions. Note that /opt/ is used to denote the default rocm-installation-path and should be replaced in case of a non-standard installation location of the ROCm distribution.


## ROCm FHS reorganization: backward compatibility[#](#rocm-fhs-reorganization-backward-compatibility)

The FHS file organization for ROCm was first introduced in the release of ROCm 5.2 . Backward compatibility was implemented to make sure users could still run their ROCm applications while transitioning to the new FHS. ROCm has moved header files and libraries to their new locations as indicated in the above structure, and included symbolic-links and wrapper header files in their old location for backward compatibility. The following sections detail ROCm backward compatibility implementation for wrapper header files, executable files, library files and CMake config files.

### Wrapper header files[#](#wrapper-header-files)

Wrapper header files are placed in the old location (
`/opt/rocm-<ver>/<component>/include`

) with a warning message to include files
from the new location (`/opt/rocm-<ver>/include`

) as shown in the example below.

```
#pragma message "This file is deprecated. Use file from include path /opt/rocm-ver/include/ and prefix with hip."
#include <hip/hip_runtime.h>
```

Starting at ROCm 5.2 release, the deprecation for backward compatibility wrapper header files is:

`#pragma`

message announcing`#warning`

.Starting from ROCm 6.0 (tentatively) backward compatibility for wrapper header files will be removed, and the

`#pragma`

message will be announcing`#error`

.

### Executable files[#](#executable-files)

Executable files are available in the `/opt/rocm-<ver>/bin`

folder. For backward
compatibility, the old library location (`/opt/rocm-<ver>/<component>/bin`

) has a
soft link to the library at the new location. Soft links will be removed in a
future release, tentatively ROCm v6.0.

```
ls -l /opt/rocm/hip/bin/
lrwxrwxrwx 1 root root 24 Jan 1 23:32 hipcc -> ../../bin/hipcc
```

### Library files[#](#library-files)

Library files are available in the `/opt/rocm-<ver>/lib`

folder. For backward
compatibility, the old library location (`/opt/rocm-<ver>/<component>/lib`

) has a
soft link to the library at the new location. Soft links will be removed in a
future release, tentatively ROCm v6.0.

```
ls -l /opt/rocm/hip/lib/
drwxr-xr-x 4 root root 4096 Jan 1 10:45 cmake
lrwxrwxrwx 1 root root 24 Jan 1 23:32 libamdhip64.so -> ../../lib/libamdhip64.so
```

### CMake config files[#](#cmake-config-files)

All CMake configuration files are available in the
`/opt/rocm-<ver>/lib/cmake/<component>`

folder. For backward compatibility, the
old CMake locations (`/opt/rocm-<ver>/<component>/lib/cmake`

) consist of a soft
link to the new CMake config. Soft links will be removed in a future release,
tentatively ROCm v6.0.

```
ls -l /opt/rocm/hip/lib/cmake/hip/
lrwxrwxrwx 1 root root 42 Jan 1 23:32 hip-config.cmake -> ../../../../lib/cmake/hip/hip-config.cmake
```

## Changes required in applications using ROCm[#](#changes-required-in-applications-using-rocm)

Applications using ROCm are advised to use the new file paths. As the old files will be deprecated in a future release. Applications have to make sure to include correct header file and use correct search paths.

`#include<header_file.h>`

needs to be changed to`#include <component/header_file.h>`

For example:

`#include <hip.h>`

needs to change to`#include <hip/hip.h>`

Any variable in CMake or Makefiles pointing to component folder needs to changed.

For example:

`VAR1=/opt/rocm/hip`

needs to be changed to`VAR1=/opt/rocm`

`VAR2=/opt/rocm/hsa`

needs to be changed to`VAR2=/opt/rocm`

Any reference to

`/opt/rocm/<component>/bin`

or`/opt/rocm/<component>/lib`

needs to be changed to`/opt/rocm/bin`

and`/opt/rocm/lib/`

, respectively.

## Changes in versioning specifications[#](#changes-in-versioning-specifications)

In order to better manage ROCm dependencies specification and allow smoother releases of ROCm while avoiding dependency conflicts, ROCm software shall adhere to the following scheme when numbering and incrementing ROCm files versions:

rocm-<ver>, where <ver> = <x.y.z>

x.y.z denote: MAJOR.MINOR.PATCH

z: PATCH - increment z when implementing backward compatible bug fixes.

y: MINOR - increment y when implementing minor changes that add functionality but are still backward compatible.

x: MAJOR - increment x when implementing major changes that are not backward compatible.
