---
title: "Installing rocAL with the package installer &#8212; rocAL 2.5.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocAL/en/latest/install/rocAL-package-install.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:22:39.501349+00:00
content_hash: "b04f75da23cd4a92"
---

# Installing rocAL with the package installer[#](#installing-rocal-with-the-package-installer)

Three rocAL packages are available:

`rocal`

: The rocAL runtime package. This is the basic rocAL package that only provides dynamic libraries. It must always be installed.`rocal-dev`

: The rocAL development package. This package installs a full suite of libraries, header files, and samples. This package needs to be installed to use samples.`rocal-test`

: A test package that provides a CTest to verify the installation.All the required prerequisites are installed when the package installation method is used.

Note

`FFMPeg-dev`

package must be installed manually.## Basic installation[#](#basic-installation)

Use the following commands to install only the rocAL runtime package:

```
apt install rocal
```

```
yum install rocal
```

```
zypper install rocal
```

## Complete installation[#](#complete-installation)

Use the following commands to install `rocal`

, `rocal-dev`

, and `rocal-test`

:

```
apt-get install rocal rocal-dev rocal-test
```

```
yum install rocal rocal-devel rocal-test
```

```
zypper install rocal rocal-devel rocal-test
```

The rocAL test package will install a CTest module. Use the following steps to test the installation:

```
rocAL-test
cd rocAL-test
cmake /opt/rocm/share/rocal/test/
ctest -VV
```
