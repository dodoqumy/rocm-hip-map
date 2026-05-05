---
title: "Installation troubleshooting"
source_url: "https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/install-faq.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:14:09.188501+00:00
content_hash: "177f0940ddaf4841"
---

# Installation troubleshooting[#](#installation-troubleshooting)

2025-11-18

7 min read time

Troubleshooting describes issues that some users encounter when installing the ROCm tools or libraries.

## Issue #1: Installation methods[#](#issue-1-installation-methods)

As an example, the latest version of ROCm is 6.0.2, but the installation instructions result in release 6.0.0 being installed.

**Solution:** You may have used the quick-start installation method which only installs the latest major release. Use one of the other available installation methods:

[Quick-start installation](../install/quick-start.html)- Installs only the latest**major**release (i.e. 6.0.0, or 6.1.0)[Native package manager install method](../install/install-methods/package-manager-index.html)- Installs the specified*major and minor*release version (i.e. 6.0.0, 6.0.2)

Refer to [ROCm Issue #2422](https://github.com/ROCm/ROCm/issues/2422) for additional details.

## Issue #2: Install prerequisites[#](#issue-2-install-prerequisites)

When installing, I see the following message: `Problem: nothing provides perl-URI-Encode needed to be installed by ...`


**Solution:** Ensure that the [Installation prerequisites](../install/prerequisites.html) are installed. There are prerequisite PERL packages required for SUSE. RHEL also requires Extra Packages for Enterprise Linux (EPEL) to be installed, which is also mentioned in prerequisites. Be sure to install those first, then repeat your installation steps.

Refer to [ROCm Issue #1827](https://github.com/ROCm/ROCm/issues/1827).

## Issue #3: PATH variable[#](#issue-3-path-variable)

After successfully installing ROCm, when I run `rocminfo`

(or another ROCm tool) the command is not found.

**Solution:** You may need to update your `PATH`

environment variable as described in [Post-installation instructions](../install/post-install.html).

Refer to [ROCm Issue #1607](https://github.com/ROCm/ROCm/issues/1607).

## Issue #4: C++ libraries[#](#issue-4-c-libraries)

When compiling HIP programs, I get a linking error for `-lstdc++`

, or `fatal error: 'cmath' file not found`

.

**Solution:** You can install C++ libraries using your package manager. The following is an Ubuntu example:

```
apt-get install libstdc++-<gcc-version>-dev
```

For more information on how to determine the relevant `gcc-version`

, refer to [ROCm Issue #1843](https://github.com/ROCm/ROCm/issues/1843#issuecomment-1813746898).

## Issue #5: Application hangs on Multi-GPU systems[#](#issue-5-application-hangs-on-multi-gpu-systems)

Running on a system with multiple GPUs the application hangs with the GPU use at 100%, but without the expected GPU temperature buildup

This issue often results in the following message in the application transcript:

```
WARN Missing "iommu=pt" from kernel command line which can lead to system instablity or hang!
```

**Solution:** To resolve this issue add `iommu=pt`

to `GRUB_CMDLINE_LINUX_DEFAULT`

in `/etc/default/grub`

. Then run the following command:

```
update-grub
```

Reboot the system, and run the following command:

```
/proc/cmdline
```

The returned information should reflect the addition of `iommu`

:

```
BOOT_IMAGE=/vmlinuz-5.15.0-101-generic root=/dev/mapper/ubuntu--vg-ubuntu--lv ro iommu=pt
```

Refer to [RCCL Issue #1129](https://github.com/ROCm/rccl/issues/1129) for more information.

## Issue #6: Additional packages for Docker installations[#](#issue-6-additional-packages-for-docker-installations)

Docker images often come with minimal installations, meaning some essential packages might be missing. When installing ROCm within a Docker container, you might need to install additional packages for a successful ROCm installation. Use the following commands to install the prerequisite packages.

```
update
apt install sudo wget gpg
```

```
update
apt install sudo wget gpg
```

```
install sudo wget
```

```
install sudo wget
```

```
install sudo wget SUSEConnect awk
```

```
install sudo wget
```

After installing these packages, install ROCm using the [Quick start installation guide](../install/quick-start.html) in your Docker container.

## Issue #8: The AMDGPU driver is not loaded after installation[#](#issue-8-the-amdgpu-driver-is-not-loaded-after-installation)

When you are verifying the ROCm installation according to the [post-install instructions](../install/post-install.html),
the `rocm-smi`

and `rocminfo`

commands might fail with the error message
`Driver not initialized`

or not display any output. This could indicate
the AMDGPU driver is not loaded.

**Solution:** Ensure the AMDGPU driver is not on a denylist such as `/etc/modprobe.d/blacklist-amdgpu.conf`

.
The location of this file might vary depending on the system distribution and version.
To verify whether the driver is on a denylist, use the following command:

```
amdgpu /etc/modprobe.d/*
```

Note

When installing the AMDGPU driver with Secure Boot enabled, you must sign `amdgpu-dkms`

to prevent potential system loading issues.
For more information, see [Secure Boot Support](https://amdgpu-install.readthedocs.io/en/latest/install-installing.html#secure-boot-support).
If you prefer not to sign the AMDGPU driver, you can disable Secure Boot from the BIOS settings instead.

## Issue #9: Cannot access the AMD GPU after installation[#](#issue-9-cannot-access-the-amd-gpu-after-installation)

If the group permissions are not set properly during ROCm installation,
you might get an error similar to `Permission denied`

when attempting to access the AMD GPU.

**Solution:** You must be part of the `video`

and `render`

groups to access the AMD GPU.
To learn how to add an account to these groups, see [Configuring permissions for GPU access](../install/prerequisites.html#group-permissions).

## Issue #10: ROCm debugging tools might become unresponsive in SELinux-enabled distributions[#](#issue-10-rocm-debugging-tools-might-become-unresponsive-in-selinux-enabled-distributions)

Red Hat Enterprise Linux (RHEL) and related distributions automatically enable a security feature named Security-Enhanced Linux (SELinux) that may prevent ROCm debugging tools like ROCgdb, ROCdbgapi, and ROCR Debug Agent from working correctly.

The problem occurs when attempting to debug a program that contains code that runs on the GPU. The debugging session may become unresponsive while attempting to reach a breakpoint or doing instruction-stepping in device code. ROCgdb will still be responsive and accept interruption by pressing `Control+C`

, but the breakpoint in device code won’t be hit, and the instruction-stepping operation will not conclude.

The ROCR Debug Agent might also become unresponsive when attempting to capture data from a program that is running into queue errors, memory faults, and other triggering events.

As a workaround for this problem, either disable SELinux or configure it to use the permissive setting.

While ROCgdb or ROCR Debug Agent are being used, setting SELinux to permissive can be accomplished with the following command:

```
setenforce 0
```

After the session is over, it can be switched back to enforcing mode:

```
setenforce 1
```

Note

Changing the SELinux settings can have security implications. Ensure you review your system security settings before making any changes.
