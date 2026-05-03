---
title: "Building AMD SMI &#8212; AMD SMI 26.2.2 documentation"
source_url: "https://rocm.docs.amd.com/projects/amdsmi/en/latest/install/build.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-03T06:25:01.632727+00:00
content_hash: "2d4030cdd3cd4e9b"
---

# Building AMD SMI[#](#building-amd-smi)

This section describes the prerequisites and steps to build AMD SMI from source.

## Required software[#](#required-software)

To build the AMD SMI library, the following components are required. Note that the software versions specified were used during development; earlier versions are not guaranteed to work.

CMake (v3.15.0 or later) –

`python3 -m pip install cmake`

g++ (v5.4.0 or later)

libdrm-dev (for Ubuntu and Debian)

libdrm-devel (for RPM-based distributions)


In order to build the AMD SMI Python package, the following components are required:

Python (3.6.8 or later)

virtualenv –

`python3 -m pip install virtualenv`


## Build steps[#](#build-steps)

Clone the rocm-systems repository to your local Linux machine and sparse-checkout the AMD SMI project.

clone --filter=blob:none --sparse https://github.com/ROCm/rocm-systems.git git -C rocm-systems sparse-checkout set projects/amdsmi cd rocm-systems/projects/amdsmi

The default installation location for the library and headers is

`/opt/rocm`

. Before installation, any old ROCm directories should be deleted:`/opt/rocm`

`/opt/rocm-<version_number>`


Build the library by following the typical CMake build sequence (run as root user or use

`sudo`

before`make install`

command); for instance:-p build cd build cmake .. make -j $(nproc) make install

The built library is located in the

`build/`

directory. To build the`rpm`

and`deb`

packages use the following command:`package`


## Rebuild the Python wrapper[#](#rebuild-the-python-wrapper)

The Python wrapper for the AMD SMI library is found in the [auto-generated
file](../how-to/amdsmi-py-lib.html#py-lib-fs) `py-interface/amdsmi_wrapper.py`

. It is essential to
regenerate this wrapper whenever there are changes to the C++ API. It is not
regenerated automatically.

To regenerate the wrapper, use the following command.


After this command, the file in `py-interface/amdsmi_wrapper.py`

will be updated
on compile.

Note

You need Docker installed on your system to regenerate the Python wrapper.

## Build the tests[#](#build-the-tests)

To verify the build and capabilities of AMD SMI on your system, as well as to
see practical examples of its usage, you can build and run the available [tests
in the repository](https://github.com/ROCm/rocm-systems/tree/develop/projects/amdsmi/tests).
Follow these steps to build the tests:

```
-p build
cd build
cmake -DBUILD_TESTS=ON ..
make -j $(nproc)
```

### Run the tests[#](#run-the-tests)

Once the tests are [built](#build-tests), you can run them by executing the
`amdsmitst`

program. The executable can be found at `build/tests/amd_smi_test/`

.

## Build the docs[#](#build-the-docs)

The [C/C++ API reference](#../reference/amdsmi-cpp-api/index.md) is generated
with [Doxygen 1.9.8](https://www.doxygen.nl/manual/changelog.html#log_1_9_8),
which must be installed separately and available on your PATH.

Create a Python virtual environment and install documentation dependencies.

# From rocm-systems/projects/amdsmi python3.12 -m venv docs/.venv source docs/.venv/bin/activate pip install -r docs/sphinx/requirements.txt

Use the following command to build the documentation using

[Sphinx](https://www.sphinx-doc.org/en/master/).-m sphinx docs docs/_build -j auto -E -v

Open

`docs/_build/index.html`

in your web browser to view the documentation. To serve the site locally instead, run:-m http.server -d docs/_build # Go to http://localhost:8000 in your browser


For related information, see [Building
documentation](https://rocm.docs.amd.com/en/latest/contribute/building.html).
