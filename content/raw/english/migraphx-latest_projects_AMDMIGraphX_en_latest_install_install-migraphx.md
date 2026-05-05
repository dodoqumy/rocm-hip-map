---
title: "MIGraphX on ROCm installation"
source_url: "https://rocm.docs.amd.com/projects/AMDMIGraphX/en/latest/install/install-migraphx.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:24:45.801725+00:00
content_hash: "6d6bcc32e1309814"
---

# MIGraphX on ROCm installation[#](#migraphx-on-rocm-installation)

2025-11-11

2 min read time

ROCm must be installed before installing MIGraphX. See [ROCm installation
for Linux](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/)
for instructions.

Installing MIGraphX using a package installer is sufficient for most users
who want to use the MIGraphX API. If you plan to develop for MIGraphX or
contribute to the source code, see [Developing for MIGraphX](../dev/contributing-to-migraphx.html)

## Install MIGraphX with a package installer[#](#install-migraphx-with-a-package-installer)

The package installer will install all the prerequisites you need for MIGraphX.

Use the following command to install MIGraphX:

```
apt update && sudo apt install -y migraphx
```

## Build MIGraphX from source[#](#build-migraphx-from-source)

Note

This method for building MIGraphX requires using `sudo`

.

Install

`rocm-cmake`

,`pip3`

,`rocblas`

, and`miopen-hip`

:

```
apt install -y rocm-cmake python3-pip rocblas miopen-hip
```

Install

[rbuild](https://github.com/RadeonOpenCompute/rbuild):

```
install --prefix /usr/local https://github.com/RadeonOpenCompute/rbuild/archive/master.tar.gz
```

Build MIGraphX source code:


```
rbuild build -d depend -B build -DGPU_TARGETS=$(/opt/rocm/bin/rocminfo | grep -o -m1 'gfx.*')
```
