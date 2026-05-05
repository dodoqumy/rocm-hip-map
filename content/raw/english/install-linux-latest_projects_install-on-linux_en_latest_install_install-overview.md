---
title: "ROCm installation overview"
source_url: "https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/install-overview.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:14:14.954552+00:00
content_hash: "9fa93dfa69d41e20"
---

# ROCm installation overview[#](#rocm-installation-overview)

2026-04-17

2 min read time

If you’re new to ROCm, we recommend using the [Quick start installation guide](quick-start.html#rocm-install-quick).

Note

If you’re using ROCm with AMD Radeon™ GPUs or Ryzen™ APUs for graphics workloads, see the

[Use ROCm on Radeon and Ryzen](https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/index.html).The AMDGPU installer documentation has been removed to encourage the use of the package manager for ROCm installation. While the package manager is the recommended method, you can still install ROCm using the AMDGPU installer by following the

[legacy process](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-6.4.1/install/install-methods/amdgpu-installer-index.html). Ensure to update the command with the intended ROCm version before running it.

To install ROCm, you can use the package manager. You can also opt for single-version or multi-version installation. These topics are described in detail in the following sections.

## Installation methods[#](#installation-methods)

### Package manager[#](#package-manager)

The distribution’s package manager lets the user install,
upgrade and uninstall using familiar commands and workflows. Third party
ecosystem support is the same as your OS package manager. See [Installation via native package manager](install-methods/package-manager-index.html) for instructions based on the operating system.

### Multi-version installation[#](#multi-version-installation)

A multi-version ROCm installation handles situations where users need multiple
versions of ROCm on the same machine for compatibility with different
applications and hardware, testing, and other use cases.
For instructions, see [Installing multiple ROCm versions](install-methods/multi-version-install-index.html).

### ROCm Runfile Installer[#](#rocm-runfile-installer)

The ROCm Runfile Installer lets you install ROCm without using a native Linux package management system.
It can be used with or without network or internet access.
See [ROCm Runfile Installer](rocm-runfile-installer.html) for instructions.
