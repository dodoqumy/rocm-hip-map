---
title: "Ubuntu native installation"
source_url: "https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/install-methods/package-manager/package-manager-ubuntu.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:14:01.076960+00:00
content_hash: "559315bf9c1d7126"
---

# Ubuntu native installation[#](#ubuntu-native-installation)

2026-04-22

5 min read time

Note

The following installation steps also apply when upgrading from a previous ROCm version.

## Registering ROCm repositories[#](#registering-rocm-repositories)

### Package signing key[#](#package-signing-key)

Download and convert the package signing key.

```
# Make the directory if it doesn't exist yet.
# This location is recommended by the distribution maintainers.
sudo mkdir --parents --mode=0755 /etc/apt/keyrings
# Download the key, convert the signing-key to a full
# keyring required by apt and store in the keyring directory
wget https://repo.radeon.com/rocm/rocm.gpg.key -O - | \
gpg --dearmor | sudo tee /etc/apt/keyrings/rocm.gpg > /dev/null
```

Note

The GPG key may change; ensure it is updated when installing a new release. If the key signature verification fails while updating, re-add the key from the ROCm to the apt repository as mentioned above.

### Register packages[#](#register-packages)

```
tee /etc/apt/sources.list.d/rocm.list << EOF
deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/rocm/apt/7.2.2 noble main
deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/graphics/7.2.1/ubuntu noble main
EOF
sudo tee /etc/apt/preferences.d/rocm-pin-600 << EOF
Package: *
Pin: release o=repo.radeon.com
Pin-Priority: 600
EOF
sudo apt update
```

```
tee /etc/apt/sources.list.d/rocm.list << EOF
deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/rocm/apt/7.2.2 jammy main
deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/graphics/7.2.1/ubuntu jammy main
EOF
sudo tee /etc/apt/preferences.d/rocm-pin-600 << EOF
Package: *
Pin: release o=repo.radeon.com
Pin-Priority: 600
EOF
sudo apt update
```

## Installing[#](#installing)

### Install kernel driver[#](#install-kernel-driver)

For information about the AMDGPU driver installation, see the [Ubuntu native installation](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/install/detailed-install/package-manager/package-manager-ubuntu.html) in the AMD Instinct Data Center GPU Documentation.

For information about driver compatibility, see [User and AMD GPU Driver (amdgpu) support matrix](../../../reference/user-kernel-space-compat-matrix.html).

### Install ROCm[#](#install-rocm)

```
apt install rocm
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
apt autoremove rocm
sudo apt autoremove rocm-core
```

### Remove ROCm repositories[#](#remove-rocm-repositories)

```
# Remove the repositories
sudo rm /etc/apt/sources.list.d/rocm.list
# Clear the cache and clean the system
sudo rm -rf /var/cache/apt/*
sudo apt clean all
sudo apt update
```

Important

To apply all settings, reboot your system.
