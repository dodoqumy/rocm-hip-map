---
title: "Oracle Linux native installation"
source_url: "https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/install-methods/package-manager/package-manager-ol.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-03T06:26:01.509775+00:00
content_hash: "65f7159282f7e9dd"
---

# Oracle Linux native installation[#](#oracle-linux-native-installation)

2026-04-22

5 min read time

Note

The following installation steps also apply when upgrading from a previous ROCm version.

## Register ROCm repositories[#](#register-rocm-repositories)

```
tee /etc/yum.repos.d/rocm.repo <<EOF
[rocm]
name=ROCm 7.2.2 repository
baseurl=https://repo.radeon.com/rocm/el10/7.2.2/main
enabled=1
priority=50
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
[amdgraphics]
name=AMD Graphics 7.2.1 repository
baseurl=https://repo.radeon.com/graphics/7.2.1/el/10/main/x86_64/
enabled=1
priority=50
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
EOF
sudo dnf clean all
```

```
tee /etc/yum.repos.d/rocm.repo <<EOF
[rocm]
name=ROCm 7.2.2 repository
baseurl=https://repo.radeon.com/rocm/el9/7.2.2/main
enabled=1
priority=50
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
[amdgraphics]
name=AMD Graphics 7.2.1 repository
baseurl=https://repo.radeon.com/graphics/7.2.1/el/9.7/main/x86_64/
enabled=1
priority=50
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
EOF
sudo dnf clean all
```

```
tee /etc/yum.repos.d/rocm.repo <<EOF
[rocm]
name=ROCm 7.2.2 repository
baseurl=https://repo.radeon.com/rocm/el8/7.2.2/main
enabled=1
priority=50
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
[amdgraphics]
name=AMD Graphics 7.2.1 repository
baseurl=https://repo.radeon.com/graphics/7.2.1/el/8/main/x86_64/
enabled=1
priority=50
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
EOF
sudo dnf clean all
```

## Installing[#](#installing)

### Install kernel driver[#](#install-kernel-driver)

For information about the AMDGPU driver installation, see the [Oracle Linux native installation](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/install/detailed-install/package-manager/package-manager-ol.html) in the AMD Instinct Data Center GPU Documentation.

For information about driver compatibility, see [User and AMD GPU Driver (amdgpu) support matrix](../../../reference/user-kernel-space-compat-matrix.html).

### Install ROCm[#](#install-rocm)

```
dnf install rocm
```

ROCm installation can be tailored to your requirements using one more combinations of ROCm meta packages:

To use pre-built ROCm libraries and tools, include

[ROCm runtime packages](../../../reference/package-manager-integration.html#rocm-runtime)in the installation step.To develop and build individual ROCm libraries and tools, include

[ROCm developer packages](../../../reference/package-manager-integration.html#rocm-dev)in the installation step.

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

## Post-installation[#](#post-installation)

Complete the [Post-installation instructions](../../post-install.html).

## Uninstalling[#](#uninstalling)

### Uninstall ROCm meta packages[#](#uninstall-rocm-meta-packages)

```
dnf remove rocm
sudo dnf remove rocm-core amdgpu-core
```

### Remove ROCm repositories[#](#remove-rocm-repositories)

```
# Remove the repositories
sudo rm /etc/yum.repos.d/rocm.repo*
# Clear the cache and clean the system
sudo rm -rf /var/cache/dnf
sudo dnf clean all
```

Important

To apply all settings, reboot your system.
