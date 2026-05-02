---
title: "Building and installing rocThrust on Linux with the install script &#8212; rocThrust Documentation 4.2.0 documentation"
source_url: "https://rocm.docs.amd.com/projects/rocThrust/en/latest/install/rocThrust-install-script.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:19:04.617831+00:00
content_hash: "b3d3cc127ddd6e93"
---

# Building and installing rocThrust on Linux with the install script[#](#building-and-installing-rocthrust-on-linux-with-the-install-script)

You can use the `install`

script to build and install rocThrust on Linux. You can also use [CMake](./rocThrust-install-with-cmake.html) if you want more build and installation options.

[Clone the rocThrust project](rocThrust-install-overview.html). The `install`

script will be located in the `rocthrust`

root directory.

To build and install rocThrust with the `install`

script, run:

```
--install
```

This command will also download and install rocPRIM.

To build rocThrust and generate tar, zip, and debian packages, run:

```
--package
```

To see a complete list of options, run:

```
--help
```
