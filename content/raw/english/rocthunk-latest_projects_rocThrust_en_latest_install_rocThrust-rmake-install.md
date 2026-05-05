---
title: "Building and installing rocThrust on Windows with rmake.py &#8212; rocThrust Documentation 4.2.0 documentation"
source_url: "https://rocm.docs.amd.com/projects/rocThrust/en/latest/install/rocThrust-rmake-install.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:19:02.592445+00:00
content_hash: "5dcb5a3a3fb69976"
---

# Building and installing rocThrust on Windows with rmake.py[#](#building-and-installing-rocthrust-on-windows-with-rmake-py)

You can use `rmake.py`

to build and install rocThrust on Windows. You can also use [CMake](./rocThrust-install-with-cmake.html) if you want more build and installation options.

[Clone the rocThrust project](rocThrust-install-overview.html). `rmake.py`

will be located in the `rocthrust`

root directory.

To build and install rocThrust with `rmake.py`

, run:

```
rmake.py -i
```

This command also downloads [rocPRIM](https://rocm.docs.amd.com/projects/rocPRIM/en/latest/index.html) and installs it in `C:\hipSDK`

.

The `-c`

option builds all clients, including the unit tests:

```
rmake.py -c
```

To see a complete list of `rmake.py`

options, run:

```
rmake.py --help
```
