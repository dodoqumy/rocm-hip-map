---
title: "rocThrust installation overview &#8212; rocThrust Documentation 4.2.0 documentation"
source_url: "https://rocm.docs.amd.com/projects/rocThrust/en/latest/install/rocThrust-install-overview.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:19:27.372323+00:00
content_hash: "712fc18a9b589d66"
---

# rocThrust installation overview[#](#rocthrust-installation-overview)

The rocThrust source code is available from the [ROCm libraries GitHub Repository](https://github.com/ROCm/rocm-libraries/tree/develop/projects/rocthrust). Use sparse checkout when cloning the rocThrust project:

```
git clone --no-checkout --filter=blob:none https://github.com/ROCm/rocm-libraries.git
cd rocm-libraries
git sparse-checkout init --cone
git sparse-checkout set projects/rocthrust
```

Then use `git checkout`

to check out the branch you need.

The develop branch is intended for users who want to preview new features or contribute to the rocThrust code base.

If you don’t intend to contribute to the rocThrust code base and won’t be previewing features, use a branch that matches the version of ROCm installed on your system.

rocThrust can be built and installed with [ install](./rocThrust-install-script.html) on Linux,

[on Windows, or](./rocThrust-rmake-install.html)

`rmake.py`

[CMake](./rocThrust-install-with-cmake.html)on Windows and Linux.

CMake provides the most flexibility in building and installing rocThrust.
