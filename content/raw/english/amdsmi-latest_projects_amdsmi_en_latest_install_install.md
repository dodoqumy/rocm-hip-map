---
title: "Install the AMD SMI library and CLI tool &#8212; AMD SMI 26.2.2 documentation"
source_url: "https://rocm.docs.amd.com/projects/amdsmi/en/latest/install/install.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-03T06:25:20.082899+00:00
content_hash: "98199b03ee599a41"
---

# Install the AMD SMI library and CLI tool[#](#install-the-amd-smi-library-and-cli-tool)

This section describes how to install the AMD SMI library, Python interface,
and command line tool either as part of the
[ROCm software stack](https://rocm.docs.amd.com/en/latest/what-is-rocm.html) – or manually.

## Requirements[#](#requirements)

The following are required to install and use the AMD SMI library through its language interfaces and CLI.

The

`amdgpu`

driver must be loaded for AMD SMI initialization to work. See[Install the amdgpu driver](#install-amdgpu-driver).Export

`LD_LIBRARY_PATH`

to the`amdsmi`

installation directory.export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/rocm/lib:/opt/rocm/lib64


### Supported platforms[#](#supported-platforms)

The AMD SMI library supports Linux bare metal and Linux virtual machine guest
for AMD GPUs and AMD EPYC™ CPUs via
[esmi_ib_lirary](https://github.com/amd/esmi_ib_library). To use AMD SMI for virtualization, refer to
the [AMD SMI for Virtualization documentation](https://instinct.docs.amd.com/projects/amd-smi-virt/en/latest/index.html).

AMD SMI library can run on AMD ROCm supported platforms. Refer to
[System requirements (Linux)](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html)
for more information.

To run the AMD SMI library, the `amdgpu`

driver and the `amd_hsmp`

or `hsmp_acpi`

driver need to be installed. Optionally, `libdrm`

can be installed to query firmware
information and hardware IPs.

### Python interface and CLI tool prerequisites[#](#python-interface-and-cli-tool-prerequisites)

Python version 3.6.8 or greater (64-bit)


Note

During the driver installation process on Azure Linux 3, you might encounter the `ModuleNotFoundError: No module named 'more_itertools'`

warning. This warning is a result of the reintroduction of `python3-wheel`

and `python3-setuptools`

dependencies in the CMake of AMD SMI, which requires `more_itertools`

to build these Python libraries. This issue will be fixed in a future ROCm release. As a workaround, use the following command before installation:

```
sudo python3 -m pip install more_itertools
```

### Go interface prerequisites[#](#go-interface-prerequisites)

Go version 1.20 or greater


## Install the amdgpu driver[#](#install-the-amdgpu-driver)

Note

As of ROCm 7.0.0, the `amdgpu`

driver is distributed separately from the ROCm
software stack. See
[User and AMD GPU Driver (amdgpu) support matrix](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/user-kernel-space-compat-matrix.html) for
driver to ROCm user space compatibility information.

Confirm that your Linux kernel version matches the system requirements described in
[Supported operating systems](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html#supported-distributions).

For up-to-date installation instructions, see the [AMD GPU Driver (amdgpu)
documentation](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/install/detailed-install/prerequisites.html).

## Install AMD SMI with ROCm[#](#install-amd-smi-with-rocm)

AMD SMI is included as a core package in the ROCm software stack as part of the
`rocm-developer-tools`

meta package. See [ROCm runtime
packages](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/package-manager-integration.html#id3)
for more information.

Note

The `amdgpu-install`

script is no longer the recommended way to install ROCm.
Install using your supported Linux distribution’s package manager instead.

For up-to-date installation instructions via package manager, see [ROCm installation for Linux](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/prerequisites.html).

After installing the `amdgpu`

driver and ROCm, verify your AMD SMI installation:


## Install AMD SMI without ROCm[#](#install-amd-smi-without-rocm)

The following are example steps to install the AMD SMI libraries and CLI tool on Ubuntu 22.04.

Install the library.

apt install amd-smi-lib

Add the installation directory to your PATH. If installed with ROCm, ignore this step.

export PATH="${PATH:+${PATH}:}~/opt/rocm/bin"

Verify your installation.

`--help`


## Optionally enable CLI autocompletion[#](#optionally-enable-cli-autocompletion)

The `amd-smi`

CLI application supports autocompletion. If `argcomplete`

is not
installed and enabled already, do so using the following commands.

```
-m pip install argcomplete
activate-global-python-argcomplete --user
# restart shell to enable
```

## Install the Python library for multiple ROCm instances[#](#install-the-python-library-for-multiple-rocm-instances)

If [multiple ROCm versions are installed](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/install-methods/multi-version-install-index.html) and you
are not using `pyenv`

, uninstall previous versions of AMD SMI before installing
the desired version from your ROCm instance.

### Manually install the Python library[#](#manually-install-the-python-library)

Multiple ROCm installations may cause `amd-smi`

failures.
Installing multiple versions of ROCm on the same system can result in the `amd-smi`

CLI not functioning correctly.

Remove previous AMD SMI installation.

-m pip list | grep amd python3 -m pip uninstall amdsmi

Install the AMD SMI Python library from your target ROCm instance.

# Install from target ROCm instance cd /opt/rocm/share/amd_smi python3 -m pip install --user .

**Note:**`sudo`

may be required. On some systems, use`--break-system-packages`

if pip installation fails.You should now have the AMD SMI Python library in your Python path:

~$ python3 Python 3.8.10 (default, May 26 2023, 14:05:08) [GCC 9.4.0] on linux Type "help", "copyright", "credits" or "license" for more information. >>> import amdsmi >>>
