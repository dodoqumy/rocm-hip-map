---
title: "Quick start installation guide"
source_url: "https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:14:02.763179+00:00
content_hash: "9718f504c80151c1"
---

# Quick start installation guide[#](#quick-start-installation-guide)

2026-04-22

17 min read time

Note

See [Use ROCm on Radeon and Ryzen](https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/index.html) for instructions on installing ROCm on systems with AMD Radeon™ GPUs or Ryzen™ APUs for graphics workloads.

Before proceeding, ensure your kernel meets the [ROCm system requirements](../reference/system-requirements.html#supported-distributions). Then select your operating system and version, and run the provided commands to install the AMD GPU and ROCm.

For detailed guidance, see [Installation via native package manager](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/install/package-manager-index.html) for AMD GPU installation and [Detailed install](detailed-install.html) for ROCm installation.

## Installing[#](#installing)

### Register repositories[#](#register-repositories)

```
https://repo.radeon.com/amdgpu-install/7.2.2/ubuntu/noble/amdgpu-install_7.2.2.70202-1_all.deb
sudo apt install ./amdgpu-install_7.2.2.70202-1_all.deb
sudo sed -i "s|graphics/7.2.2|graphics/7.2.1|" /etc/apt/sources.list.d/rocm.list
sudo apt update
```

```
https://repo.radeon.com/amdgpu-install/7.2.2/ubuntu/jammy/amdgpu-install_7.2.2.70202-1_all.deb
sudo apt install ./amdgpu-install_7.2.2.70202-1_all.deb
sudo sed -i "s|graphics/7.2.2|graphics/7.2.1|" /etc/apt/sources.list.d/rocm.list
sudo apt update
```

```
https://repo.radeon.com/amdgpu-install/7.2.2/ubuntu/noble/amdgpu-install_7.2.2.70202-1_all.deb
sudo apt install ./amdgpu-install_7.2.2.70202-1_all.deb
sudo sed -i "s|graphics/7.2.2|graphics/7.2.1|" /etc/apt/sources.list.d/rocm.list
sudo apt update
```

```
https://repo.radeon.com/amdgpu-install/7.2.2/ubuntu/jammy/amdgpu-install_7.2.2.70202-1_all.deb
sudo apt install ./amdgpu-install_7.2.2.70202-1_all.deb
sudo sed -i "s|graphics/7.2.2|graphics/7.2.1|" /etc/apt/sources.list.d/rocm.list
sudo apt update
```

Before installing ROCm on RHEL, [register and update your Enterprise Linux](prerequisites.html#register-enterprise-linux).

```
dnf install https://repo.radeon.com/amdgpu-install/7.2.2/rhel/10/amdgpu-install-7.2.2.70202-1.el10.noarch.rpm
sudo sed -i "s|graphics/7\.2\.2|graphics/7.2.1|;s|AMD Graphics 7.2.2|AMD Graphics 7.2.1|" /etc/yum.repos.d/rocm.repo
sudo dnf clean all
```

Before installing ROCm on RHEL, [register and update your Enterprise Linux](prerequisites.html#register-enterprise-linux).

```
dnf install https://repo.radeon.com/amdgpu-install/7.2.2/rhel/10/amdgpu-install-7.2.2.70202-1.el10.noarch.rpm
sudo sed -i "s|graphics/7\.2\.2|graphics/7.2.1|;s|AMD Graphics 7.2.2|AMD Graphics 7.2.1|" /etc/yum.repos.d/rocm.repo
sudo dnf clean all
```

Before installing ROCm on RHEL, [register and update your Enterprise Linux](prerequisites.html#register-enterprise-linux).

```
dnf install https://repo.radeon.com/amdgpu-install/7.2.2/rhel/9.7/amdgpu-install-7.2.2.70202-1.el9.noarch.rpm
sudo sed -i "s|graphics/7\.2\.2|graphics/7.2.1|;s|AMD Graphics 7.2.2|AMD Graphics 7.2.1|" /etc/yum.repos.d/rocm.repo
sudo dnf clean all
```

Before installing ROCm on RHEL, [register and update your Enterprise Linux](prerequisites.html#register-enterprise-linux).

```
dnf install https://repo.radeon.com/amdgpu-install/7.2.2/rhel/9.6/amdgpu-install-7.2.2.70202-1.el9.noarch.rpm
sudo sed -i "s|graphics/7\.2\.2|graphics/7.2.1|;s|AMD Graphics 7.2.2|AMD Graphics 7.2.1|" /etc/yum.repos.d/rocm.repo
sudo dnf clean all
```

Before installing ROCm on RHEL, [register and update your Enterprise Linux](prerequisites.html#register-enterprise-linux).

```
dnf install https://repo.radeon.com/amdgpu-install/7.2.2/rhel/9.4/amdgpu-install-7.2.2.70202-1.el9.noarch.rpm
sudo sed -i "s|graphics/7\.2\.2|graphics/7.2.1|;s|AMD Graphics 7.2.2|AMD Graphics 7.2.1|" /etc/yum.repos.d/rocm.repo
sudo dnf clean all
```

Before installing ROCm on RHEL, [register and update your Enterprise Linux](prerequisites.html#register-enterprise-linux).

```
dnf install https://repo.radeon.com/amdgpu-install/7.2.2/rhel/8/amdgpu-install-7.2.2.70202-1.el8.noarch.rpm
sudo sed -i "s|graphics/7\.2\.2|graphics/7.2.1|;s|AMD Graphics 7.2.2|AMD Graphics 7.2.1|" /etc/yum.repos.d/rocm.repo
sudo dnf clean all
```

Before installing ROCm on OL, [update your Enterprise Linux](prerequisites.html#update-enterprise-linux).

```
dnf install https://repo.radeon.com/amdgpu-install/7.2.2/el/10/amdgpu-install-7.2.2.70202-1.el10.noarch.rpm
sudo sed -i "s|graphics/7\.2\.2|graphics/7.2.1|;s|AMD Graphics 7.2.2|AMD Graphics 7.2.1|" /etc/yum.repos.d/rocm.repo
sudo dnf clean all
```

Before installing ROCm on OL, [update your Enterprise Linux](prerequisites.html#update-enterprise-linux).

```
dnf install https://repo.radeon.com/amdgpu-install/7.2.2/el/9.7/amdgpu-install-7.2.2.70202-1.el9.noarch.rpm
sudo sed -i "s|graphics/7\.2\.2|graphics/7.2.1|;s|AMD Graphics 7.2.2|AMD Graphics 7.2.1|" /etc/yum.repos.d/rocm.repo
sudo dnf clean all
```

Before installing ROCm on OL, [update your Enterprise Linux](prerequisites.html#update-enterprise-linux).

```
dnf install https://repo.radeon.com/amdgpu-install/7.2.2/el/8/amdgpu-install-7.2.2.70202-1.el8.noarch.rpm
sudo sed -i "s|graphics/7\.2\.2|graphics/7.2.1|;s|AMD Graphics 7.2.2|AMD Graphics 7.2.1|" /etc/yum.repos.d/rocm.repo
sudo dnf clean all
```

Before installing ROCm on SLES, [register and update your Enterprise Linux](prerequisites.html#register-enterprise-linux).

```
SUSEConnect -p sle-module-desktop-applications/15.7/x86_64
sudo SUSEConnect -p sle-module-development-tools/15.7/x86_64
sudo SUSEConnect -p PackageHub/15.7/x86_64
sudo zypper install zypper
sudo zypper --no-gpg-checks install https://repo.radeon.com/amdgpu-install/7.2.2/sle/15.7/amdgpu-install-7.2.2.70202-1.noarch.rpm
sudo sed -i "s|graphics/7.2.2|graphics/7.2.1|;s|AMD Graphics 7.2.2|AMD Graphics 7.2.1|" /etc/zypp/repos.d/rocm.repo
sudo zypper --gpg-auto-import-keys refresh
```

```
dnf install https://repo.radeon.com/amdgpu-install/7.2.2/el/9.7/amdgpu-install-7.2.2.70202-1.el9.noarch.rpm
sudo sed -i "s|graphics/7\.2\.2|graphics/7.2.1|;s|AMD Graphics 7.2.2|AMD Graphics 7.2.1|" /etc/yum.repos.d/rocm.repo
sudo dnf clean all
```

### Install kernel driver[#](#install-kernel-driver)

Caution

Remove any AMD GPU driver from a previous installation by following the uninstall steps in [Uninstall kernel driver](#uninstall-kernel-driver).

```
apt install "linux-headers-$(uname -r)" "linux-modules-extra-$(uname -r)"
sudo apt install amdgpu-dkms
```

Caution

Remove any AMD GPU driver from a previous installation by following the uninstall steps in [Uninstall kernel driver](#uninstall-kernel-driver).

```
apt install "linux-headers-$(uname -r)" "linux-modules-extra-$(uname -r)"
sudo apt install amdgpu-dkms
```

Caution

Remove any AMD GPU driver from a previous installation by following uninstallation steps in [Uninstall kernel driver](#uninstall-kernel-driver).

```
dnf install "kernel-headers-$(uname -r)" "kernel-devel-$(uname -r)" "kernel-devel-matched-$(uname -r)"
sudo dnf install amdgpu-dkms
```

Caution

Remove any AMD GPU driver from a previous installation by following uninstallation steps in [Uninstall kernel driver](#uninstall-kernel-driver).

```
dnf install "kernel-headers-$(uname -r)" "kernel-devel-$(uname -r)" "kernel-devel-matched-$(uname -r)"
sudo dnf install amdgpu-dkms
```

Caution

Remove any AMD GPU driver from a previous installation by following uninstallation steps in [Uninstall kernel driver](#uninstall-kernel-driver).

```
dnf install "kernel-headers-$(uname -r)" "kernel-devel-$(uname -r)" "kernel-devel-matched-$(uname -r)"
sudo dnf install amdgpu-dkms
```

Caution

Remove any AMD GPU driver from a previous installation by following uninstallation steps in [Uninstall kernel driver](#uninstall-kernel-driver).

```
dnf install "kernel-headers-$(uname -r)" "kernel-devel-$(uname -r)" "kernel-devel-matched-$(uname -r)"
sudo dnf install amdgpu-dkms
```

Caution

Remove any AMD GPU driver from a previous installation by following uninstallation steps in [Uninstall kernel driver](#uninstall-kernel-driver).

```
dnf install "kernel-headers-$(uname -r)" "kernel-devel-$(uname -r)" "kernel-devel-matched-$(uname -r)"
sudo dnf install amdgpu-dkms
```

Caution

Remove any AMD GPU driver from a previous installation by following uninstallation steps in [Uninstall kernel driver](#uninstall-kernel-driver).

```
dnf install "kernel-headers-$(uname -r)" "kernel-devel-$(uname -r)"
sudo dnf install amdgpu-dkms
```

Caution

Remove any AMD GPU driver from a previous installation by following uninstallation steps in [Uninstall kernel driver](#uninstall-kernel-driver).

```
dnf install "kernel-uek-devel-$(uname -r)"
sudo dnf install amdgpu-dkms
```

Caution

Remove any AMD GPU driver from a previous installation by following uninstallation steps in [Uninstall kernel driver](#uninstall-kernel-driver).

```
dnf install "kernel-headers" "kernel-devel" "kernel-devel-matched"
sudo dnf install amdgpu-dkms
```

Important

To apply all settings, reboot your system.

### Install ROCm[#](#install-rocm)

```
apt install python3-setuptools python3-wheel
sudo usermod -a -G render,video $LOGNAME # Add the current user to the render and video groups
sudo apt install rocm
```

```
apt install python3-setuptools python3-wheel
sudo usermod -a -G render,video $LOGNAME # Add the current user to the render and video groups
sudo apt install rocm
```

```
apt install python3-setuptools python3-wheel
sudo usermod -a -G render,video $LOGNAME # Add the current user to the render and video groups
sudo apt install rocm
```

```
apt install python3-setuptools python3-wheel
sudo usermod -a -G render,video $LOGNAME # Add the current user to the render and video groups
sudo apt install rocm
```

```
https://dl.fedoraproject.org/pub/epel/epel-release-latest-10.noarch.rpm
sudo rpm -ivh epel-release-latest-10.noarch.rpm
sudo dnf config-manager --enable codeready-builder-for-rhel-10-x86_64-rpms
sudo dnf install python3-setuptools python3-wheel
sudo usermod -a -G render,video $LOGNAME # Add the current user to the render and video groups
sudo dnf install rocm
```

```
https://dl.fedoraproject.org/pub/epel/epel-release-latest-10.noarch.rpm
sudo rpm -ivh epel-release-latest-10.noarch.rpm
sudo dnf config-manager --enable codeready-builder-for-rhel-10-x86_64-rpms
sudo dnf install python3-setuptools python3-wheel
sudo usermod -a -G render,video $LOGNAME # Add the current user to the render and video groups
sudo dnf install rocm
```

```
https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm
sudo rpm -ivh epel-release-latest-9.noarch.rpm
sudo dnf config-manager --enable codeready-builder-for-rhel-9-x86_64-rpms
sudo dnf install python3-setuptools python3-wheel
sudo usermod -a -G render,video $LOGNAME # Add the current user to the render and video groups
sudo dnf install rocm
```

```
https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm
sudo rpm -ivh epel-release-latest-9.noarch.rpm
sudo dnf config-manager --enable codeready-builder-for-rhel-9-x86_64-rpms
sudo dnf install python3-setuptools python3-wheel
sudo usermod -a -G render,video $LOGNAME # Add the current user to the render and video groups
sudo dnf install rocm
```

```
https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm
sudo rpm -ivh epel-release-latest-9.noarch.rpm
sudo dnf config-manager --enable codeready-builder-for-rhel-9-x86_64-rpms
sudo dnf install python3-setuptools python3-wheel
sudo usermod -a -G render,video $LOGNAME # Add the current user to the render and video groups
sudo dnf install rocm
```

```
https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
sudo rpm -ivh epel-release-latest-8.noarch.rpm
sudo dnf config-manager --enable codeready-builder-for-rhel-8-x86_64-rpms
sudo dnf install python3-setuptools python3-wheel
sudo usermod -a -G render,video $LOGNAME # Add the current user to the render and video groups
sudo dnf install rocm
```

```
https://dl.fedoraproject.org/pub/epel/epel-release-latest-10.noarch.rpm
sudo rpm -ivh epel-release-latest-10.noarch.rpm
sudo crb enable
sudo dnf install python3-setuptools python3-wheel
sudo usermod -a -G render,video $LOGNAME # Add the current user to the render and video groups
sudo dnf install rocm
```

```
https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm
sudo rpm -ivh epel-release-latest-9.noarch.rpm
sudo crb enable
sudo dnf install python3-setuptools python3-wheel
sudo usermod -a -G render,video $LOGNAME # Add the current user to the render and video groups
sudo dnf install rocm
```

```
https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
sudo rpm -ivh epel-release-latest-8.noarch.rpm
sudo crb enable
sudo dnf install python3-setuptools python3-wheel
sudo usermod -a -G render,video $LOGNAME # Add the current user to the render and video groups
sudo dnf install rocm
```

```
zypper addrepo https://download.opensuse.org/repositories/science/SLE_15_SP5/science.repo
sudo zypper install python3-setuptools python3-wheel
sudo usermod -a -G render,video $LOGNAME # Add the current user to the render and video groups
sudo zypper install rocm
```

```
https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm
sudo rpm -ivh epel-release-latest-9.noarch.rpm
sudo dnf install dnf-plugin-config-manager
sudo crb enable
sudo dnf install python3-setuptools python3-wheel
sudo usermod -a -G render,video $LOGNAME # Add the current user to the render and video groups
sudo dnf install rocm
```

Important

To apply all settings, reboot your system.

Note

Quick Start enables GPU access for the current user only. To grant GPU access to all users, see [Configuring permissions for GPU access](prerequisites.html#group-permissions).

After completing the installation, review the [Post-installation instructions](post-install.html). If you have issues with your installation, see [Troubleshooting](../reference/install-faq.html).

## Uninstalling[#](#uninstalling)

### Uninstall ROCm[#](#uninstall-rocm)

```
apt autoremove rocm
sudo apt autoremove rocm-core
```

```
apt autoremove rocm
sudo apt autoremove rocm-core
```

```
apt autoremove rocm
sudo apt autoremove rocm-core
```

```
apt autoremove rocm
sudo apt autoremove rocm-core
```

```
dnf remove rocm
sudo dnf remove rocm-core amdgpu-core
```

```
dnf remove rocm
sudo dnf remove rocm-core amdgpu-core
```

```
dnf remove rocm
sudo dnf remove rocm-core amdgpu-core
```

```
dnf remove rocm
sudo dnf remove rocm-core amdgpu-core
```

```
dnf remove rocm
sudo dnf remove rocm-core amdgpu-core
```

```
dnf remove rocm
sudo dnf remove rocm-core amdgpu-core
```

```
dnf remove rocm
sudo dnf remove rocm-core amdgpu-core
```

```
dnf remove rocm
sudo dnf remove rocm-core amdgpu-core
```

```
dnf remove rocm
sudo dnf remove rocm-core amdgpu-core
```

```
zypper remove rocm
sudo zypper remove rocm-core amdgpu-core
```

```
dnf remove rocm
sudo dnf remove rocm-core amdgpu-core
```

### Uninstall kernel driver[#](#uninstall-kernel-driver)

```
apt autoremove amdgpu-dkms
```

```
apt autoremove amdgpu-dkms
```

```
apt autoremove amdgpu-dkms
```

```
apt autoremove amdgpu-dkms
```

```
dnf remove amdgpu-dkms
```

```
dnf remove amdgpu-dkms
```

```
dnf remove amdgpu-dkms
```

```
dnf remove amdgpu-dkms
```

```
dnf remove amdgpu-dkms
```

```
dnf remove amdgpu-dkms
```

```
dnf remove amdgpu-dkms
```

```
dnf remove amdgpu-dkms
```

```
dnf remove amdgpu-dkms
```

```
zypper remove amdgpu-dkms amdgpu-dkms-firmware
```

```
dnf remove amdgpu-dkms
```

Important

To apply all settings, reboot your system.

### Remove repositories[#](#remove-repositories)

```
sudo apt purge amdgpu-install
sudo apt autoremove
# Clear the cache and clean the system
sudo rm -rf /var/cache/apt/*
sudo apt clean all
sudo apt update
```

```
sudo apt purge amdgpu-install
sudo apt autoremove
# Clear the cache and clean the system
sudo rm -rf /var/cache/apt/*
sudo apt clean all
sudo apt update
```

```
sudo apt purge amdgpu-install
sudo apt autoremove
# Clear the cache and clean the system
sudo rm -rf /var/cache/apt/*
sudo apt clean all
sudo apt update
```

```
sudo apt purge amdgpu-install
sudo apt autoremove
# Clear the cache and clean the system
sudo rm -rf /var/cache/apt/*
sudo apt clean all
sudo apt update
```

```
sudo dnf remove amdgpu-install
# Clear the cache and clean the system
sudo rm -rf /var/cache/dnf
sudo dnf clean all
```

```
sudo dnf remove amdgpu-install
# Clear the cache and clean the system
sudo rm -rf /var/cache/dnf
sudo dnf clean all
```

```
sudo dnf remove amdgpu-install
# Clear the cache and clean the system
sudo rm -rf /var/cache/dnf
sudo dnf clean all
```

```
sudo dnf remove amdgpu-install
# Clear the cache and clean the system
sudo rm -rf /var/cache/dnf
sudo dnf clean all
```

```
sudo dnf remove amdgpu-install
# Clear the cache and clean the system
sudo rm -rf /var/cache/dnf
sudo dnf clean all
```

```
sudo dnf remove amdgpu-install
# Clear the cache and clean the system
sudo rm -rf /var/cache/dnf
sudo dnf clean all
```

```
sudo dnf remove amdgpu-install
# Clear the cache and clean the system
sudo rm -rf /var/cache/dnf
sudo dnf clean all
```

```
sudo dnf remove amdgpu-install
# Clear the cache and clean the system
sudo rm -rf /var/cache/dnf
sudo dnf clean all
```

```
sudo dnf remove amdgpu-install
# Clear the cache and clean the system
sudo rm -rf /var/cache/dnf
sudo dnf clean all
```

```
sudo zypper remove amdgpu-install
# Clear the cache and clean the system
sudo zypper clean --all
sudo zypper refresh
```

```
sudo dnf remove amdgpu-install
# Clear the cache and clean the system
sudo rm -rf /var/cache/dnf
sudo dnf clean all
```
