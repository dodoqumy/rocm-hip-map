---
title: "Installation prerequisites"
source_url: "https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/prerequisites.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:14:32.103708+00:00
content_hash: "bfc9df5d360861a6"
---

# Installation prerequisites[#](#installation-prerequisites)

2026-02-24

14 min read time

Before installing ROCm, complete the following prerequisites.

Confirm the system has a supported Linux version.

To obtain the Linux distribution information, use the following command:

-m && cat /etc/*release

Confirm that your Linux distribution matches a

[supported distribution](../reference/system-requirements.html#supported-distributions).**Example:**Running the preceding command on an Ubuntu system produces the following output:DISTRIB_ID=Ubuntu DISTRIB_RELEASE=24.04 DISTRIB_CODENAME=noble DISTRIB_DESCRIPTION="Ubuntu 24.04.3 LTS"



Verify the kernel version.

To check the kernel version of your Linux system, type the following command:

`-srmv`

**Example:**The preceding command lists the kernel version in the following format:6.8.0-50-generic #51-Ubuntu SMP PREEMPT_DYNAMIC Sat Nov 9 17:58:29 UTC 2024 x86_64

Confirm that your kernel version matches the system requirements, as listed in

[Supported operating systems](../reference/system-requirements.html#supported-distributions).


## Register your Enterprise Linux[#](#register-your-enterprise-linux)

If you’re using Red Hat Enterprise Linux (RHEL) or SUSE Linux Enterprise Server (SLES), register your operating system to ensure you’re able to download and install packages.

There is no registration required for Ubuntu.

There is no registration required for Debian.

Typically you can register by following the step-by-step user interface. If you need to register by command line, use the following commands:

```
register --username <username> --password <password>
```

More details about [registering for RHEL](https://access.redhat.com/solutions/253273)

Typically you can register by following the step-by-step user interface. If you need to register by command line, use the following commands:

```
register --username <username> --password <password>
```

More details about [registering for RHEL](https://access.redhat.com/solutions/253273)

Typically you can register by following the step-by-step user interface. If you need to register by command line, use the following commands:

```
register --username <username> --password <password>
subscription-manager attach --auto
```

More details about [registering for RHEL](https://access.redhat.com/solutions/253273)

Typically you can register by following the step-by-step user interface. If you need to register by command line, use the following commands:

```
register --username <username> --password <password>
subscription-manager attach --auto
```

More details about [registering for RHEL](https://access.redhat.com/solutions/253273)

Typically you can register by following the step-by-step user interface. If you need to register by command line, use the following commands:

```
register --username <username> --password <password>
subscription-manager attach --auto
```

More details about [registering for RHEL](https://access.redhat.com/solutions/253273)

Typically you can register by following the step-by-step user interface. If you need to register by command line, use the following commands:

```
register --username <username> --password <password>
subscription-manager attach --auto
```

More details about [registering for RHEL](https://access.redhat.com/solutions/253273)

There is no registration required for Oracle Linux.

Typically you can register by following the step-by-step user interface. If you need to register by command line, use the following commands:

```
SUSEConnect -r <REGCODE>
```

More details about [registering for SLES](https://www.suse.com/support/kb/doc/?id=000018564)

There is no registration required for Rocky Linux.

## Update your Enterprise Linux[#](#update-your-enterprise-linux)

If you are using Red Hat Enterprise Linux (RHEL), SUSE Linux Enterprise Servers (SLES), or Oracle Linux (OL), it is recommended that you update your operating system to the latest packages from the Linux distribution. This is a requirement for newer hardware on older versions of RHEL, SLES, or OL.

There is no update required for Ubuntu.

There is no update required for Debian.

```
dnf update redhat-release
sudo dnf update --releasever=10.1 --exclude=\*release\*
```

```
dnf update --releasever=10.0 --exclude=\*release\*
```

```
dnf update --releasever=9.7 --exclude=\*release\*
```

```
dnf update --releasever=9.6 --exclude=\*release\*
```

```
dnf update --releasever=9.4 --exclude=\*release\*
```

```
dnf update --releasever=8.10 --exclude=\*release\*
```

```
dnf update --releasever=10.1 --exclude=\*release\*
```

```
dnf update --releasever=9.7 --exclude=\*release\*
```

```
dnf update --releasever=8.10 --exclude=\*release\*
```

```
zypper update
```

There is no update required for Rocky Linux.

Important

To apply all settings, reboot your system.

## Additional package repositories[#](#additional-package-repositories)

For some distributions, the ROCm installation packages depend on packages that aren’t included in the default package repositories. These external repositories need to be sourced before installation. Use the following instructions specific to your distribution to add the necessary repositories.

All ROCm installation packages are available in the default Ubuntu repositories.

All ROCm installation packages are available in the default Debian repositories.

Add the EPEL repository.

https://dl.fedoraproject.org/pub/epel/epel-release-latest-10.noarch.rpm sudo rpm -ivh epel-release-latest-10.noarch.rpm

https://dl.fedoraproject.org/pub/epel/epel-release-latest-10.noarch.rpm sudo rpm -ivh epel-release-latest-10.noarch.rpm

https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm sudo rpm -ivh epel-release-latest-9.noarch.rpm

https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm sudo rpm -ivh epel-release-latest-9.noarch.rpm

https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm sudo rpm -ivh epel-release-latest-9.noarch.rpm

https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm sudo rpm -ivh epel-release-latest-8.noarch.rpm

Enable the CodeReady Linux Builder (CRB) repository.

dnf config-manager --enable codeready-builder-for-rhel-10-x86_64-rpms

dnf config-manager --enable codeready-builder-for-rhel-10-x86_64-rpms

dnf config-manager --enable codeready-builder-for-rhel-9-x86_64-rpms

dnf config-manager --enable codeready-builder-for-rhel-9-x86_64-rpms

dnf config-manager --enable codeready-builder-for-rhel-9-x86_64-rpms

dnf config-manager --enable codeready-builder-for-rhel-8-x86_64-rpms


Add the EPEL repository.

https://dl.fedoraproject.org/pub/epel/epel-release-latest-10.noarch.rpm sudo rpm -ivh epel-release-latest-10.noarch.rpm

https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm sudo rpm -ivh epel-release-latest-9.noarch.rpm

https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm sudo rpm -ivh epel-release-latest-8.noarch.rpm

Enable the CodeReady Linux Builder (CRB) repository.

crb enable


Add a few modules with SUSEConnect and the science repository.

```
SUSEConnect -p sle-module-desktop-applications/15.7/x86_64
sudo SUSEConnect -p sle-module-development-tools/15.7/x86_64
sudo SUSEConnect -p PackageHub/15.7/x86_64
sudo zypper install zypper
sudo zypper addrepo https://download.opensuse.org/repositories/science/SLE_15_SP5/science.repo
```

Add the EPEL repository.

https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm sudo rpm -ivh epel-release-latest-9.noarch.rpm

Enable the CodeReady Linux Builder (CRB) repository.

In order to enable CRB, you may need to install

`dnf-plugin-config-manager`

first.dnf install dnf-plugin-config-manager sudo crb enable


## Additional development packages[#](#additional-development-packages)

ROCm installation requires additional packages for operation and development.

To install the required packages, use the following instructions specific to your distribution:

```
apt install python3-setuptools python3-wheel
```

```
apt install python3-setuptools python3-wheel
```

```
dnf install python3-setuptools python3-wheel
```

```
dnf install python3-setuptools python3-wheel
```

```
zypper install python3-setuptools python3-wheel
```

```
dnf install python3-setuptools python3-wheel
```

Optionally, if configuring the [post-ROCm installation](post-install.html#config-rocm-path) using `environment-modules`

, install the following:

```
apt install environment-modules
```

```
apt install environment-modules
```

```
dnf install environment-modules
```

```
dnf install environment-modules
```

```
zypper install environment-modules
# Create a link for installed modules version
version=$(rpm -qa | grep '^Modules-' | awk -F'-' '{print $2}')
sudo ln -s /usr/share/Modules/$version/modulefiles /usr/share/Modules/modulefiles
```

```
dnf install environment-modules
```

## Configuring permissions for GPU access[#](#configuring-permissions-for-gpu-access)

There are two primary methods to configure GPU access for ROCm: group membership or udev rules. Each method has its own advantages, and the choice depends on your specific requirements and system management preferences.

### 1. Using group membership[#](#using-group-membership)

By default, GPU access is managed through membership in the `video`

and `render`

groups.
The `video`

and `render`

groups are system groups in Linux used to manage access
to graphics hardware and related functionality. Traditionally, the `video`

group is used
to control access to video devices, including graphics cards and video capture devices.
The `render`

group is more recent and specifically controls access to GPU rendering capabilities
through Direct Rendering Manager (DRM) render nodes.

To check the groups in your system, issue the following command:

Add yourself to the

`video`

and`render`

groups:usermod -a -G video,render $LOGNAME

Optionally, add other users to the

`video`

and`render`

groups:usermod -a -G video,render user1 sudo usermod -a -G video,render user2

To add all future users to the render and video groups by default, run the following commands:

echo 'ADD_EXTRA_GROUPS=1' | sudo tee -a /etc/adduser.conf echo 'EXTRA_GROUPS=video' | sudo tee -a /etc/adduser.conf echo 'EXTRA_GROUPS=render' | sudo tee -a /etc/adduser.conf


### 2. Using udev rules[#](#using-udev-rules)

A flexible way to manage device permissions is to use udev rules. They apply system-wide, can be easily deployed via configuration management tools, and eliminate the need for user group management. This method provides more granular control over GPU access.

GPU access may be granted to either all users or a custom group:

#### a. Grant GPU access to all users on the system[#](#a-grant-gpu-access-to-all-users-on-the-system)

To set up udev rules, install the package using the following instructions specific to your distribution:

```
apt update
wget https://repo.radeon.com/amdgpu/30.30.2/ubuntu/pool/main/a/amdgpu-insecure-instinct-udev-rules/amdgpu-insecure-instinct-udev-rules_30.30.2.0-2317211.24.04_all.deb
sudo apt install ./amdgpu-insecure-instinct-udev-rules_30.30.2.0-2317211.24.04_all.deb
```

```
apt update
wget https://repo.radeon.com/amdgpu/30.30.2/ubuntu/pool/main/a/amdgpu-insecure-instinct-udev-rules/amdgpu-insecure-instinct-udev-rules_30.30.2.0-2317211.22.04_all.deb
sudo apt install ./amdgpu-insecure-instinct-udev-rules_30.30.2.0-2317211.22.04_all.deb
```

```
apt update
wget https://repo.radeon.com/amdgpu/30.30.2/ubuntu/pool/main/a/amdgpu-insecure-instinct-udev-rules/amdgpu-insecure-instinct-udev-rules_30.30.2.0-2317211.24.04_all.deb
sudo apt install ./amdgpu-insecure-instinct-udev-rules_30.30.2.0-2317211.24.04_all.deb
```

```
apt update
wget https://repo.radeon.com/amdgpu/30.30.2/ubuntu/pool/main/a/amdgpu-insecure-instinct-udev-rules/amdgpu-insecure-instinct-udev-rules_30.30.2.0-2317211.22.04_all.deb
sudo apt install ./amdgpu-insecure-instinct-udev-rules_30.30.2.0-2317211.22.04_all.deb
```

```
dnf install https://repo.radeon.com/amdgpu/30.30.2/el/10/main/x86_64/amdgpu-insecure-instinct-udev-rules-30.30.2.0-2317211.el10.noarch.rpm
```

```
dnf install https://repo.radeon.com/amdgpu/30.30.2/el/10/main/x86_64/amdgpu-insecure-instinct-udev-rules-30.30.2.0-2317211.el10.noarch.rpm
```

```
dnf install https://repo.radeon.com/amdgpu/30.30.2/el/9.7/main/x86_64/amdgpu-insecure-instinct-udev-rules-30.30.2.0-2317211.el9.noarch.rpm
```

```
dnf install https://repo.radeon.com/amdgpu/30.30.2/el/9.6/main/x86_64/amdgpu-insecure-instinct-udev-rules-30.30.2.0-2317211.el9.noarch.rpm
```

```
dnf install https://repo.radeon.com/amdgpu/30.30.2/el/9.4/main/x86_64/amdgpu-insecure-instinct-udev-rules-30.30.2.0-2317211.el9.noarch.rpm
```

```
dnf install https://repo.radeon.com/amdgpu/30.30.2/el/8/main/x86_64/amdgpu-insecure-instinct-udev-rules-30.30.2.0-2317211.el8.noarch.rpm
```

```
dnf install https://repo.radeon.com/amdgpu/30.30.2/el/10/main/x86_64/amdgpu-insecure-instinct-udev-rules-30.30.2.0-2317211.el10.noarch.rpm
```

```
dnf install https://repo.radeon.com/amdgpu/30.30.2/el/9.7/main/x86_64/amdgpu-insecure-instinct-udev-rules-30.30.2.0-2317211.el9.noarch.rpm
```

```
dnf install https://repo.radeon.com/amdgpu/30.30.2/el/8/main/x86_64/amdgpu-insecure-instinct-udev-rules-30.30.2.0-2317211.el8.noarch.rpm
```

```
zypper --no-gpg-checks install https://repo.radeon.com/amdgpu/30.30.2/sle/15.7/main/x86_64/amdgpu-insecure-instinct-udev-rules-30.30.2.0-2317211.noarch.rpm
```

```
dnf install https://repo.radeon.com/amdgpu/30.30.2/el/9.7/main/x86_64/amdgpu-insecure-instinct-udev-rules-30.30.2.0-2317211.el9.noarch.rpm
```

#### b. Grant GPU access to a custom group[#](#b-grant-gpu-access-to-a-custom-group)

Create a new group (e.g.,

`devteam`

):groupadd devteam

Add users to the new group:

usermod -a -G devteam dev1 sudo usermod -a -G devteam dev2

Create udev rules to assign GPU devices to this group:

Create a file

`/etc/udev/rules.d/70-amdgpu.rules`

with:KERNEL=="kfd", GROUP="devteam", MODE="0660" SUBSYSTEM=="drm", KERNEL=="renderD*", GROUP="devteam", MODE="0660"

Reload the udev rules:

udevadm control --reload-rules && sudo udevadm trigger


This configuration grants all users in the `devteam`

group read and write access to AMD GPU resources,
including the AMD Kernel-mode GPU Driver (KMD) and Direct Rendering Manager (DRM) devices.

## Disable integrated graphics (IGP)[#](#disable-integrated-graphics-igp)

ROCm doesn’t currently support integrated graphics. If your system has an
AMD IGP installed, disable it in the BIOS prior to using ROCm. If the driver can
enumerate the IGP, the ROCm runtime might crash the system, even when omission was specified
via [HIP_VISIBLE_DEVICES](https://rocm.docs.amd.com/en/latest/conceptual/gpu-isolation.html#hip-visible-devices).

## Secure Boot[#](#secure-boot)

When installing the AMDGPU driver with Secure Boot enabled, you must sign `amdgpu-dkms`

to prevent potential system loading issues.
For more information, see [Secure Boot Support](https://amdgpu-install.readthedocs.io/en/latest/install-installing.html#secure-boot-support).
If you prefer not to sign the AMDGPU driver, you can disable Secure Boot from the BIOS settings instead.
