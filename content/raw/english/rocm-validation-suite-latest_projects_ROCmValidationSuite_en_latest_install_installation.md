---
title: "Installing ROCm Validation Suite &#8212; RVS 1.3.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/ROCmValidationSuite/en/latest/install/installation.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:26:44.707485+00:00
content_hash: "4825ea81c79776e5"
---

# Installing ROCm Validation Suite[#](#installing-rocm-validation-suite)

You can obtain ROCm Validation Suite (RVS) by building it from:

the source code base

a prebuilt package


## Building from source code[#](#building-from-source-code)

RVS is an open-source solution. For more details, refer to the [ROCm Validation Suite GitHub repository.](https://github.com/ROCm/ROCmValidationSuite)

## Package manager installation[#](#package-manager-installation)

Based on the OS, use the appropriate package manager to install the RVS package.

For more details, refer to the [ROCm Validation Suite GitHub repository.](https://github.com/ROCm/ROCmValidationSuite)

RVS package components are installed in `/opt/rocm`

. The package contains:

executable binary, located in

`_install-base_/bin/rvs`

.public shared libraries, located in

`_install-base_/lib`

.module specific shared libraries, located in

`_install-base_/lib/rvs`

.default configuration files, located in

`_install-base_/share/rocm-validation-suite/conf`

.GPU specific configuration files, located in

`_install-base_/share/rocm-validation-suite/conf/<GPU folder>`

.testscripts, located in

`_install-base_/share/rocm-validation-suite/testscripts`

.user guide, located in

`_install-base_/share/rocm-validation-suite/userguide`

.man page, located in

`_install-base_/share/man`

.

## Prerequisites[#](#prerequisites)

RVS has been tested on all ROCm-supported Linux environments except for RHEL 9.4. See [Supported operating systems](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html#supported-operating-systems) for the complete list of ROCm-supported Linux environments.

Note

This topic provides commands for the primary Linux distribution families. These commands are also applicable to other operating systems derived from the same families.

Ensure you review the following prerequisites carefully for each operating system before compiling or installing the RVS package.

```
apt-get -y update && sudo apt-get install -y libpci3 libpci-dev doxygen unzip cmake git libyaml-cpp-dev
```

```
yum install -y cmake3 doxygen rpm rpm-build git gcc-c++ yaml-cpp-devel pciutils-devel
```

```
zypper install -y cmake doxygen pciutils-devel libpci3 rpm git rpm-build gcc-c++ yaml-cpp-devel
```

## Install ROCm stack, rocBLAS, and SMI lib[#](#install-rocm-stack-rocblas-and-smi-lib)

Install the ROCm software stack for Ubuntu, SLES or RHEL. Refer to the

[ROCm installation guide](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html)for more details.Install rocBLAS. For ROCm 6.4 and earlier, install

`rocm-smi-lib`

. For ROCm 7.0 and later, install`amd-smi-lib`

.

```
apt-get install rocblas rocm-smi-lib
```

```
yum install --nogpgcheck rocblas rocm-smi-lib
```

```
zypper install rocblas rocm-smi-lib
```

If rocm-smi-lib is already installed, but `/opt/rocm/lib/librocm_smi64.so`

doesn’t exist, run the following commands as per the OS:

```
dpkg -r rocm-smi-lib && sudo apt install rocm-smi-lib
```

```
rpm -e rocm-smi-lib && sudo yum install rocm-smi-lib
```

```
rpm -e rocm-smi-lib && sudo zypper install rocm-smi-lib
```

## Building from source[#](#building-from-source)

This section explains how to get and compile the current development stream of RVS.

Clone the repository.


```
git clone https://github.com/ROCm/ROCmValidationSuite.git
```

Configure the build system for RVS.


```
cd ROCmValidationSuite
cmake -B ./build -DROCM_PATH=<rocm_installed_path> -DCMAKE_INSTALL_PREFIX=<rocm_installed_path> -DCPACK_PACKAGING_INSTALL_PREFIX=<rocm_installed_path>
```

For example, if ROCm 5.5 was installed, run the following command:

```
cmake -B ./build -DROCM_PATH=/opt/rocm-5.5.0 -DCMAKE_INSTALL_PREFIX=/opt/rocm-5.5.0 -DCPACK_PACKAGING_INSTALL_PREFIX=/opt/rocm-5.5.0
```

Build the binary.


```
make -C ./build
```

Build the package.


```
cd ./build
make package
```

Note

Depending on your OS, only DEB or RPM package will be built.

Note

You can ignore errors about unrelated configurations.

Install the built package.


```
sudo dpkg -i rocm-validation-suite*.deb
```

```
rpm -i --replacefiles --nodeps rocm-validation-suite*.rpm
```

```
rpm -i --replacefiles --nodeps rocm-validation-suite*.rpm
```

Note

RVS is packaged as part of the ROCm release starting from 3.0. You can install the pre-compiled package as indicated below. Ensure prerequisites, ROCm stack, rocblas and rocm-smi-lib64 are already installed.

Install the package included with the ROCm release.


```
sudo apt install rocm-validation-suite
```

```
yum install rocm-validation-suite
```

```
zypper install rocm-validation-suite
```

## Reporting[#](#reporting)

Test results, errors, and verbose logs are printed as terminal output. To enable JSON logging, use the `-j`

option. The JSON output file is stored in the `/var/tmp`

folder and the file name will be printed.

You can build RVS from the source code base or by installing from a pre-built package. See the preceding sections for more details.

## Running RVS[#](#running-rvs)

### Run the version built from source code[#](#run-the-version-built-from-source-code)

```
cd <source folder>/build/bin
Command examples
./rvs --help ; Lists all options to run RVS test suite
./rvs -g ; Lists supported GPUs available in the machine
./rvs -d 3 ; Run set of RVS default sanity tests (in rvs.conf) with verbose level 3
./rvs -c conf/gst_single.conf ; Run GST module default test configuration
```

### Run the version pre-compiled and packaged with the ROCm release[#](#run-the-version-pre-compiled-and-packaged-with-the-rocm-release)

```
cd /opt/rocm/bin
Command examples
./rvs --help ; Lists all options to run RVS test suite
./rvs -g ; Lists supported GPUs available in the machine
./rvs -d 3 ; Run set of RVS sanity tests (in rvs.conf) with verbose level 3
./rvs -c ../share/rocm-validation-suite/conf/gst_single.conf ; Run GST default test configuration
```

To run GPU-specific test configurations, use the configuration files in the GPU folders under `/opt/rocm/share/rocm-validation-suite/conf`

.

```
./rvs -c ../share/rocm-validation-suite/conf/MI300X/gst_single.conf ; Run MI300X specific GST test configuration
./rvs -c ../share/rocm-validation-suite/conf/nv32/gst_single.conf ; Run Navi 32 specific GST test configuration
```

Note

Always use GPU-specific configurations over the default test configurations.

## Building documentation[#](#building-documentation)

Run the following commands to build documentation locally.

```
cd docs
pip3 install -r .sphinx/requirements.txt
python3 -m sphinx -T -E -b html -d _build/doctrees -D language=en . _build/html
```
