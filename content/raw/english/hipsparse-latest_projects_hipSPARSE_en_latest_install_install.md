---
title: "Installing and building hipSPARSE for Linux &#8212; hipSPARSE 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipSPARSE/en/latest/install/install.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:09:37.291475+00:00
content_hash: "c3faf1c0d4eb53e9"
---

# Installing and building hipSPARSE for Linux[#](#installing-and-building-hipsparse-for-linux)

This topic explains how to install and build the hipSPARSE library on Linux by using prebuilt packages or building from source.
For information on installing and building hipSPARSE on Microsoft Windows, see [hipSPARSE for Windows](install-windows.html).

## Prerequisites[#](#prerequisites)

hipSPARSE requires a ROCm enabled platform.

## Installing prebuilt packages[#](#installing-prebuilt-packages)

hipSPARSE can be installed from the AMD ROCm repository.
For detailed instructions on installing ROCm, see [ROCm installation](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/index.html).

To install hipSPARSE on Ubuntu, run these commands:

```
apt-get update
sudo apt-get install hipsparse
```

After hipSPARSE is installed, it can be used just like any other library with a C API. To call hipSPARSE, the header file must be included in the user code. This means the hipSPARSE shared library becomes a link-time and run-time dependency for the user application.

## Building hipSPARSE from source[#](#building-hipsparse-from-source)

It isn’t necessary to build hipSPARSE from source because it’s ready to use after installing the prebuilt packages, as described above. To build hipSPARSE from source, follow the instructions in this section.

To compile and run hipSPARSE, the [AMD ROCm Platform](https://github.com/ROCm/ROCm) is required.
The build also requires the following compile-time dependencies:

[CMake](https://cmake.org/)(Version 3.5 or later)[GoogleTest](https://github.com/google/googletest)(Optional: only required to build the clients)

### Downloading hipSPARSE[#](#downloading-hipsparse)

The hipSPARSE source code is available from the [hipSPARSE folder](https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipsparse)
of the [rocm-libraries GitHub](https://github.com/ROCm/rocm-libraries).
Download the develop branch using either a sparse checkout or a full clone of the rocm-libraries repository.

To limit your local checkout to only the hipSPARSE project, configure `sparse-checkout`

before cloning.
This uses the Git partial clone feature (`--filter=blob:none`

) to reduce how much data is downloaded.
Use the following commands for a sparse checkout:

Note

To include the rocSPARSE dependencies, set the projects for the sparse checkout using
`git sparse-checkout set projects/hipsparse projects/rocsparse`

.

```
clone --no-checkout --filter=blob:none https://github.com/ROCm/rocm-libraries.git
cd rocm-libraries
git sparse-checkout init --cone
git sparse-checkout set projects/hipsparse # add projects/rocsparse to include dependencies
git checkout develop # or use the branch you want to work with
```

To download the develop branch for all projects in rocm-libraries, use these commands. This process takes longer but is recommended for those working with a large number of libraries.

```
clone -b develop https://github.com/ROCm/rocm-libraries.git
cd rocm-libraries/projects/hipsparse
```

### Building hipSPARSE using the install script[#](#building-hipsparse-using-the-install-script)

It’s recommended to use the `install.sh`

script to install hipSPARSE.
Here are the steps required to build different packages of the library, including the dependencies and clients.

Note

You can run the `install.sh`

script from the `projects/hipsparse`

directory.

#### Using install.sh to build hipSPARSE with dependencies[#](#using-install-sh-to-build-hipsparse-with-dependencies)

The following table lists the common ways to use `install.sh`

to build the hipSPARSE dependencies and library.

Command |
Description |
|---|---|
|
Print the help information. |
|
Build the dependencies and library in your local directory. The |
|
Build the library in your local directory. The script assumes the dependencies are available. |
|
Build the library, then build and install the hipSPARSE package in |

#### Using install.sh to build hipSPARSE with dependencies and clients[#](#using-install-sh-to-build-hipsparse-with-dependencies-and-clients)

The clients contains example code and unit tests. Common use cases of `install.sh`

to build them are listed in the table below.

Command |
Description |
|---|---|
|
Print the help information. |
|
Build the dependencies, library, and client in your local directory. The |
|
Build the library and client in your local directory. The script assumes the dependencies are available. |
|
Build the library, dependencies, and client, then build and install the hipSPARSE package in |
|
Build the library and client, then build and install the hipSPARSE package in |

### Building hipSPARSE using individual make commands[#](#building-hipsparse-using-individual-make-commands)

You can build hipSPARSE using the following commands:

Note

Run these commands from the `projects/hipsparse`

directory.

Note

CMake 3.5 or later is required to build hipSPARSE.

```
# Create and change to build directory
mkdir -p build/release ; cd build/release
# Default install path is /opt/rocm, use -DCMAKE_INSTALL_PREFIX=<path> to adjust it
cmake ../..
# Compile hipSPARSE library
make -j$(nproc)
# Install hipSPARSE to /opt/rocm
make install
```

You can build hipSPARSE with the dependencies and clients using the following commands:

Note

GoogleTest is required to build the hipSPARSE clients.

```
# Install GoogleTest
mkdir -p build/release/deps ; cd build/release/deps
cmake ../../../deps
make -j$(nproc) install
# Change to build directory
cd ..
# Default install path is /opt/rocm, use -DCMAKE_INSTALL_PREFIX=<path> to adjust it
cmake ../.. -DBUILD_CLIENTS_TESTS=ON -DBUILD_CLIENTS_SAMPLES=ON
# Compile hipSPARSE library
make -j$(nproc)
# Install hipSPARSE to /opt/rocm
make install
```

## Testing hipSPARSE[#](#testing-hipsparse)

You can test the installation by running one of the hipSPARSE examples after successfully compiling the library with the clients.

```
# Navigate to clients binary directory
cd build/release/clients/staging
# Execute hipSPARSE example
./example_csrmv 1000
```

## Supported targets[#](#supported-targets)

For a list of the currently supported operating systems, see the [ROCm compatibility matrix](https://rocm.docs.amd.com/en/latest/compatibility/compatibility-matrix.html).
