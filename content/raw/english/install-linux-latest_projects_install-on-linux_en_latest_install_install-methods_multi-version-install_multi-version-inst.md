---
title: "Oracle Linux multi-version installation"
source_url: "https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/install-methods/multi-version-install/multi-version-install-ol.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:14:16.421157+00:00
content_hash: "39ad1cd570549e2b"
---

# Oracle Linux multi-version installation[#](#oracle-linux-multi-version-installation)

2026-04-22

5 min read time

## Register ROCm repositories[#](#register-rocm-repositories)

```
# Note: There is NO trailing .0 in the patch version for repositories
for ver in 7.2.2 7.2.1; do
sudo tee --append /etc/yum.repos.d/rocm.repo <<EOF
[rocm-$ver]
name=ROCm $ver repository
baseurl=https://repo.radeon.com/rocm/el10/$ver/main
enabled=1
priority=50
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
EOF
done
sudo dnf clean all
```

```
# Note: There is NO trailing .0 in the patch version for repositories
for ver in 7.2.2 7.2.1; do
sudo tee --append /etc/yum.repos.d/rocm.repo <<EOF
[rocm-$ver]
name=ROCm $ver repository
baseurl=https://repo.radeon.com/rocm/el9/$ver/main
enabled=1
priority=50
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
EOF
done
sudo dnf clean all
```

```
# Note: There is NO trailing .0 in the patch version for repositories
for ver in 7.2.2 7.2.1; do
sudo tee --append /etc/yum.repos.d/rocm.repo <<EOF
[rocm-$ver]
name=ROCm $ver repository
baseurl=https://repo.radeon.com/rocm/el8/$ver/main
enabled=1
priority=50
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
EOF
done
sudo dnf clean all
```

## Installing[#](#installing)

### Install kernel driver[#](#install-kernel-driver)

For information about the AMDGPU driver installation, see the [Oracle Linux native installation](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/install/detailed-install/package-manager/package-manager-ol.html) in the AMD Instinct Data Center GPU Documentation.

For information about driver compatibility, see [User and AMD GPU Driver (amdgpu) support matrix](../../../reference/user-kernel-space-compat-matrix.html).

### Install ROCm[#](#install-rocm)

Before proceeding with a multi-version ROCm installation, you must remove ROCm packages that were previously installed from a single-version installation to avoid conflicts.

```
# Note: There IS a trailing .0 in the patch version for packages
for ver in 7.2.2 7.2.1; do
sudo dnf install rocm$ver
done
```

```
# Note: There IS a trailing .0 in the patch version for packages
for ver in 7.2.2 7.2.1; do
sudo dnf install rocm$ver
done
```

```
# Note: There IS a trailing .0 in the patch version for packages
for ver in 7.2.2 7.2.1; do
sudo dnf install rocm$ver
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
sudo dnf remove rocm$ver
done
```

```
# Note: There IS a trailing .0 in the patch version for packages
for ver in 7.2.2 7.2.1; do
sudo dnf remove rocm$ver
done
```

```
# Note: There IS a trailing .0 in the patch version for packages
for ver in 7.2.2 7.2.1; do
sudo dnf remove rocm$ver
done
```

### Uninstall ROCm packages[#](#uninstall-rocm-packages)

```
# Note: There IS a trailing .0 in the patch version for packages
for ver in 7.2.2 7.2.1; do
sudo dnf remove rocm-core$ver amdgpu-core$ver
done
```

```
# Note: There IS a trailing .0 in the patch version for packages
for ver in 7.2.2 7.2.1; do
sudo dnf remove rocm-core$ver amdgpu-core$ver
done
```

```
# Note: There IS a trailing .0 in the patch version for packages
for ver in 7.2.2 7.2.1; do
sudo dnf remove rocm-core$ver amdgpu-core$ver
done
```

### Remove ROCm repositories[#](#remove-rocm-repositories)

```
# Remove ROCm repositories
sudo rm /etc/yum.repos.d/rocm.repo*
# Clear the cache and clean the system
sudo rm -rf /var/cache/dnf
sudo dnf clean all
```

Important

To apply all settings, reboot your system.
