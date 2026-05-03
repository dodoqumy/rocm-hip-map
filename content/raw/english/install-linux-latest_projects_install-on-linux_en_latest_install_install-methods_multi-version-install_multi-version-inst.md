---
title: "Ubuntu multi-version installation"
source_url: "https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/install-methods/multi-version-install/multi-version-install-ubuntu.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-03T06:25:56.464223+00:00
content_hash: "d3cb0dcf28343b4d"
---

# Ubuntu multi-version installation[#](#ubuntu-multi-version-installation)

2026-04-22

4 min read time

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
# Note: There is NO trailing .0 in the patch version for repositories
for ver in 7.2.2 7.2.1; do
sudo tee --append /etc/apt/sources.list.d/rocm.list << EOF
deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/rocm/apt/$ver noble main
EOF
done
sudo tee /etc/apt/preferences.d/rocm-pin-600 << EOF
Package: *
Pin: release o=repo.radeon.com
Pin-Priority: 600
EOF
sudo apt update
```

```
# Note: There is NO trailing .0 in the patch version for repositories
for ver in 7.2.2 7.2.1; do
sudo tee --append /etc/apt/sources.list.d/rocm.list << EOF
deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/rocm/apt/$ver jammy main
EOF
done
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

Before proceeding with a multi-version ROCm installation, you must remove ROCm packages that were previously installed from a single-version installation to avoid conflicts.

```
# Note: There IS a trailing .0 in the patch version for packages
for ver in 7.2.2 7.2.1; do
sudo apt install rocm$ver
done
```

Note

For versions earlier than ROCm 6.0.0, use `rocm-hip-sdk`

instead of `rocm`

(for example, `rocm-hip-sdk5.7.1`

).

## Post-installation[#](#post-installation)

Complete the [Post-installation instructions](../../post-install.html).

## Uninstalling[#](#uninstalling)

### Uninstall specific meta packages[#](#uninstall-specific-meta-packages)

```
# Note: There IS a trailing .0 in the patch version for packages
for ver in 7.2.2 7.2.1; do
sudo apt autoremove rocm$ver
done
```

### Uninstall ROCm packages[#](#uninstall-rocm-packages)

```
# Note: There IS a trailing .0 in the patch version for packages
for ver in 7.2.2 7.2.1; do
sudo apt autoremove rocm-core$ver
done
```

### Remove ROCm repositories[#](#remove-rocm-repositories)

```
# Remove ROCm repositories
sudo rm /etc/apt/sources.list.d/rocm.list
# Clear the cache and clean the system
sudo rm -rf /var/cache/apt/*
sudo apt clean all
sudo apt update
```

Important

To apply all settings, reboot your system.
