---
title: "Installing rocPRIM on Windows &#8212; rocPRIM 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocPRIM/en/latest/install/rocPRIM-build-install-windows.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-03T06:28:38.163800+00:00
content_hash: "e086e8e50b0d93b2"
---

# Installing rocPRIM on Windows[#](#installing-rocprim-on-windows)

rocPRIM is installed on Windows using the `rmake.py`

Python script. `rmake.py`

is also used to build rocPRIM examples, tests, and benchmarks.

In the [cloned](rocPRIM-install-overview.html) `rocprim`

directory, run `rmake.py -i`

to install rocPRIM to `C:\hipSDK\include\`

:

```
cd rocPRIM
python3 rmake.py -i
```

Use the `-c`

option to build the examples, tests, and benchmarks:

python3 rmake.py -c


You can also build Microsoft Visual Studio projects for the examples, tests, and benchmarks.

Change directory to the `example`

, `test`

, or `benchmark`

directory, and create the `build`

directory. For example:

```
cd benchmark
mkdir build
```

Change directory to the `build`

directory, and run `cmake`

:

```
cd build
cmake ../.
```

The Visual Studio projects and solutions will be created in the `build`

directory.
