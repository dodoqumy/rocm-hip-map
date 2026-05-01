---
title: "rocAL prerequisites &#8212; rocAL 2.5.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocAL/en/latest/install/rocAL-prerequisites.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:22:37.543302+00:00
content_hash: "b53316b0f4efeef7"
---

# rocAL prerequisites[#](#rocal-prerequisites)

rocAL requires ROCm running on [GPUs based on the CDNA architecture](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html) installed with the [AMDGPU installer](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-6.4.1/install/install-methods/amdgpu-installer-index.html).

rocAL has been tested on the following Linux environments:

Ubuntu 22.04 and 24.04

RHEL 8 and 9

SLES 15 SP7


See [Supported operating systems](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html#supported-operating-systems) for the complete list of ROCm supported Linux environments.

[Building rocAL from source](rocAL-build-and-install.html) requires CMake Version 3.10 or later, AMD Clang++ Version 18.0.0 or later, and the following compiler support:

C++17

OpenMP

Threads


Most prerequisites are installed with the [package installer](rocAL-package-install.html).

When building rocAL from source, the `rocAL-setup.py`

setup script can be used to install prerequisites:

```
[-h] [--directory DIRECTORY; default ~/] \
[--rocm_path ROCM_PATH; default /opt/rocm] \
[--backend HIP|OCL; default HIP] \
[--ffmpeg ON|OFF; default OFF] \
[--reinstall ON|OFF; default OFF]
```

The following prerequisites are required and are installed with both the package installer and the setup script:

[MIVisionX](https://rocm.docs.amd.com/projects/MIVisionX/en/latest/index.html)with[AMD OpenVX™](https://rocm.docs.amd.com/projects/MIVisionX/en/latest/install/MIVisionX-install-OpenVX.html)and the VX_RPP and AMD Media extensions[The half-precision floating-point library](https://half.sourceforge.net)version 1.12.0 or later[Google Protobuf](https://developers.google.com/protocol-buffers)version 3.12.4 or later[PyBind11](https://github.com/pybind/pybind11/releases/tag/v2.11.1)version 2.11.1Python3, Python3 pip, and Python3 wheel


libstdc++-12-dev is required on Ubuntu 22.04 only and must be installed manually.

[FFMPEG](https://www.ffmpeg.org) is not required, but is installed by the package installer. It can also be installed with the setup script using the `--ffmpeg`

option.

[rocDecode](https://rocm.docs.amd.com/projects/rocDecode/en/latest/index.html) and [rocJPEG](https://rocm.docs.amd.com/projects/rocJPEG/en/latest/index.html) are installed by the package installer and the setup script, but aren’t required by rocAL. When installed, rocJPEG is used as the hardware image decoder and rocDecode is used as the hardware video decoder.

Note

`FFMPeg-dev`

package must be installed manually.
