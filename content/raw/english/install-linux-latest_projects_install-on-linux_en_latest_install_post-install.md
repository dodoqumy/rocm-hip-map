---
title: "Post-installation instructions"
source_url: "https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/post-install.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:14:30.442425+00:00
content_hash: "30627043ae733bc2"
---

# Post-installation instructions[#](#post-installation-instructions)

2026-04-22

5 min read time

After installing ROCm, follow these steps to finalize and validate the installation.

## Environment Configuration[#](#environment-configuration)

### 2. Configure ROCm `PATH`

[#](#configure-rocm-path)

Configure the path to the ROCm binary using one of the following Linux utilities or manually update the `PATH`

variable.
The ROCm installation process adds the ROCm executables to these systems, provided they are installed on the system.

**Option A:** `update-alternatives`


The `update-alternatives`

utility is available on most Linux distributions. It helps
manage multiple versions of a command or program.
For more information about `update-alternatives`

, see
[Linux man](https://man7.org/linux/man-pages/man1/update-alternatives.1.html).

To use `update-alternatives`

, follow these steps:

Display a list of all ROCm versions available:

update-alternatives --display rocm

If multiple ROCm versions are installed, switch between them using this command and selecting the ROCm version:

update-alternatives --config rocm


**Option B:** `environment-modules`


The `environment-modules`

tool simplifies shell initialization. It lets you modify
your session environment using module files. For more information, see
[Environment Modules](https://modules.readthedocs.io/en/latest/).

Note

The `environment-modules`

package should be installed on the system before ROCm can be configured using modules. For more information, see [prerequisites](prerequisites.html#additional-dev-packages).

To use `environment-modules`

, follow these instructions:

Enable

`environment-modules`

:source /etc/profile.d/modules.sh

Display a list of all available modules (including ROCm modules):

`avail`

Display a list of all currently loaded modules:

`list`

If multiple ROCm versions are installed, and no other ROCm modules are currently loaded, set ROCm by version:

load rocm/7.2.2

If multiple ROCm versions are installed with a current ROCm module in use, switch to another ROCm version as follows:

switch rocm/7.2.2


Note

If modules are used for ROCm, any `update-alternatives`

ROCm setting will be overwritten for the terminal session.

**Option C:** `PATH`


If `update-alternatives`

or `environment-modules`

are not available on the system, configure the ROCm path by setting the `PATH`

variable to `/opt/rocm-<version>/bin`

.

```
export PATH=$PATH:/opt/rocm-7.2.2/bin
```

### 3. Configure `LD_LIBRARY_PATH`

[#](#configure-ld-library-path)

```
export LD_LIBRARY_PATH=/opt/rocm-7.2.2/lib
```

## Install verification[#](#install-verification)

Once ROCm has been configured, validate the installation.

### 1. Verify the package installation[#](#verify-the-package-installation)

Use the package manager to validate the list of ROCm component packages installed on the system.
If package installation was successful, the list will contain `rocm*`

and `hip*`

packages currently installed on the system.

```
list --installed
```

```
list --installed
```

```
list installed
```

```
list installed
```

```
list installed
```

```
search --installed-only
```

### 2. Verify the ROCm installation[#](#verify-the-rocm-installation)

Use the following ROCm tools to verify that installation was successful:

```
| grep -i "Marketing Name:"
```

**Example output:**

```
Name: AMD EPYC 9654 96-Core Processor
Marketing Name: AMD EPYC 9654 96-Core Processor
Marketing Name: AMD Instinct MI300X
```

```
| grep -i "Board name:"
```

**Example output:**

```
name: AMD Instinct MI300X
```

```
version
```

**Example output:**

```
Tool: 26.2.2+671d39a71e | AMDSMI Library version: 26.2.2 | ROCm version: 7.2.2 | amdgpu version: 6.16.13 | hsmp version: N/A
```

## Troubleshooting[#](#troubleshooting)

**What if environment-modules is not installed before installing ROCm?**You can still install

`environment-modules`

package after installing ROCm. However, no ROCm modules will be listed for the`module avail`

command. As an alternative to the standard method of loading the ROCm modules, you can load each version-specific module directly from the`/opt/rocm-<version>`

directory:load /opt/rocm-7.2.2/lib/rocmmod

**Will the ROCm path configuration persist once I set it?**If you are using update-alternatives to configure ROCm, then yes, the currently set configuration will persist even after a system reboot.

If you are using environment-modules to configure ROCm, then no, the current set configuration will only last for the current terminal session.
