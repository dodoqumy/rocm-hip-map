---
title: "Installing ROCprofiler-SDK &#8212; ROCprofiler-SDK 1.1.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/install/installation.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T18:21:27.521741+00:00
content_hash: "6e1637eebab19401"
---

# Installing ROCprofiler-SDK[#](#installing-rocprofiler-sdk)

This document provides information required to install ROCprofiler-SDK from source.

## Supported systems[#](#supported-systems)

ROCprofiler-SDK is supported on the Linux distributions specified in the [system requirements](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html#supported-operating-systems).

## Identifying the operating system[#](#identifying-the-operating-system)

To identify the Linux distribution and version, see the `/etc/os-release`

and `/usr/lib/os-release`

files:

```
cat /etc/os-release
NAME="Ubuntu"
VERSION="20.04.4 LTS (Focal Fossa)"
ID=ubuntu
...
VERSION_ID="20.04"
...
```

The relevant fields are `ID`

and the `VERSION_ID`

.

## Build requirements[#](#build-requirements)

Install the following dependencies:

Debian/Ubuntu


```
apt install -y libdw-dev libsqlite3-dev
```

Red Hat Enterprise Linux/Alma Linux/Rocky Linux/Fedora


```
dnf install elfutils elfutils-devel sqlite-devel clang-tools-extra gcc gcc-c++ cmake make openssl-devel
python3 -m pip install --upgrade pip
python3 -m pip install scikit-build
```

SUSE Linux Enterprise Server


```
zypper install gcc12 gcc12-c++ cmake make python3-devel elfutils sqlite3-devel libelf-devel libdw-devel
export CXX=/usr/bin/g++-12
export CC=/usr/bin/gcc-12
```

Note

The above `export`

statements set the compiler environment variables only for the current terminal session. If you open a new terminal or log out, these variables will be unset. To make these settings permanent, add the following lines to your `~/.bashrc`

file:

```
export CXX=/usr/bin/g++-12
export CC=/usr/bin/gcc-12
```

Alternatively, ensure these variables are set before building ROCprofiler-SDK.

To build ROCprofiler-SDK, install `CMake`

as explained in the following section.

### Install CMake[#](#install-cmake)

Install [CMake](https://cmake.org/) version 3.21 (or later).

Note

If the `CMake`

installed on the system is too old, you can install a new version using various methods. One of the easiest options is to use PyPi (Python’s pip).

```
-m pip install --user 'cmake==3.22.0'
export PATH=${HOME}/.local/bin:${PATH}
```

## Building ROCprofiler-SDK from source[#](#building-rocprofiler-sdk-from-source)

```
clone --no-checkout --filter=blob:none https://github.com/ROCm/rocm-systems.git
cd rocm-systems
git sparse-checkout init --cone
git sparse-checkout set projects/rocprofiler-sdk
git checkout develop
python3 -m pip install -r projects/rocprofiler-sdk/requirements.txt
cmake \
-B rocprofiler-sdk-build \
-DCMAKE_INSTALL_PREFIX=/opt/rocm \
-DCMAKE_PREFIX_PATH=/opt/rocm \
projects/rocprofiler-sdk
cmake --build rocprofiler-sdk-build --target all --parallel $(nproc)
```

## Installing ROCprofiler-SDK[#](#id2)

To install ROCprofiler-SDK from the `rocprofiler-sdk-build`

directory, run:

```
--build rocprofiler-sdk-build --target install
```

## Testing ROCprofiler-SDK[#](#testing-rocprofiler-sdk)

To run the built tests, `cd`

into the `rocprofiler-sdk-build`

directory and run:

```
--output-on-failure -O ctest.all.log
```

```
-m pip install -r requirements.txt
```

## Install using package manager[#](#install-using-package-manager)

If you have ROCm version 6.2 or later installed, you can use the package manager to install a prebuilt copy of ROCprofiler-SDK.

```
sudo apt install rocprofiler-sdk
```

```
sudo dnf install rocprofiler-sdk
```
