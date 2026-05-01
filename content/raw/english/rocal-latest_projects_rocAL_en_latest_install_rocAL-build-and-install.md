---
title: "Building and installing rocAL from source code &#8212; rocAL 2.5.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocAL/en/latest/install/rocAL-build-and-install.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:22:41.300183+00:00
content_hash: "0811b08fb46bc437"
---

# Building and installing rocAL from source code[#](#building-and-installing-rocal-from-source-code)

Before building and installing rocAL, ensure ROCm has been installed with the [AMDGPU installer](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-6.4.1/install/install-methods/amdgpu-installer-index.html) and the `rocm`

usecase.

The rocAL source code is available from [ROCm/rocAL](https://github.com/ROCm/rocAL). Use the rocAL version that corresponds to the installed version of ROCm.

rocAL supports the HIP backend.

rocAL is installed in the ROCm installation directory by default. If rocAL for both HIP and OpenCL backends will be installed on the system, each version must be installed in its own custom directory and not in the default directory.

You can choose to use the `rocAL-setup.py`

setup script to install most [prerequisites](rocAL-prerequisites.html)

Note

`FFmpeg-dev`

package must be installed manually.To build and install rocAL, create the `build`

directory under the `rocAL`

root directory. Change directory to `build`

:

```
build
cd build
```

Use `cmake`

to generate a makefile:

```
../
```

Use the `-DCMAKE_INSTALL_PREFIX`

directive to set the installation directory. For example:

```
-DCMAKE_INSTALL_PREFIX=/opt/rocAL/
```

Run make:


Run `cmake`

again to generate Python bindings for `rocal_pybind`

then install:

```
cmake --build . --target PyPackageInstall
sudo make install
```

After the installation, the rocAL files will be installed under `/opt/rocm/`

unless `-DCMAKE_INSTALL_PREFIX`

was specified. If `-DCMAKE_INSTALL_PREFIX`

was specified, the rocAL files will be installed under the specified directory.

To make and run the tests, use `make test`

.
