---
title: "ROCgdb Installation Guide"
source_url: "https://rocm.docs.amd.com/projects/ROCgdb/en/latest/install/installation.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T16:03:32.547346+00:00
content_hash: "fd0593535ecbe5a9"
---

# Installing ROCgdb[#](#installing-rocgdb)

This topic provides information required to build and install ROCgdb.

## System requirements[#](#system-requirements)

A system supporting ROCm. See the

[supported operating systems](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html#supported-operating-systems).A C++17 compiler such as GCC 9 or Clang 5.

AMD Debugger API Library (

`ROCdbgapi`

) that can be installed as part of the ROCm release using the`rocm-dbgapi`

package.Install the required packages according to the OS:


```
install bison flex gcc make ncurses-dev texinfo g++ zlib1g-dev \
libexpat-dev python3-dev liblzma-dev libgmp-dev libmpfr-dev
```

```
install -y epel-release centos-release-scl bison flex gcc make \
texinfo texinfo-tex gcc-c++ zlib-devel expat-devel python3-devel \
xz-devel gmp-devel ncurses-devel mpfr-devel
```

```
in bison flex gcc make texinfo gcc-c++ zlib-devel libexpat-devel \
python3-devel xz-devel gmp-devel ncurses-devel mpfr-devel
```

## Building ROCgdb[#](#building-rocgdb)

An example command line to build ROCgdb on Linux:

```
cd rocgdb
mkdir build
cd build
../configure --program-prefix=roc \
--enable-64-bit-bfd --enable-targets="x86_64-linux-gnu,amdgcn-amd-amdhsa" \
--disable-ld --disable-gas --disable-gdbserver --disable-sim --enable-tui \
--disable-gdbtk --disable-gprofng --disable-shared --with-expat \
--with-system-zlib --without-guile --without-babeltrace --with-lzma \
--with-python=python3
make
```

If `ROCdbgapi`

is not installed in the system’s default location, specify `PKG_CONFIG_PATH`

to make the correct build configuration available to `pkg-config`

.
If `ROCdbgapi`

is installed in `/opt/rocm-$ROCM_VERSION`

(default for ROCm packages), use `PKG_CONFIG_PATH=/opt/rocm-$ROCM_VERSION/share/pkgconfig`

.

If the system’s dynamic linker is not configured to locate `ROCdbgapi`

where it is
installed, configure and build ROCgdb using `LDFLAGS="-Wl,-rpath=/opt/rocm-$ROCM_VERSION/lib"`

.
Alternatively, use `LD_LIBRARY_PATH`

at runtime to indicate where `ROCdbgapi`

is installed.

You can find the built ROCgdb executable in `build/gdb/gdb`

and the user manual in `build/gdb/doc/gdb.info`

.

## Installing ROCgdb[#](#id1)

To install ROCgdb, use:

```
install
```

This installs ROCgdb in `<prefix>/bin/rocgdb`

.

## Installing libraries[#](#installing-libraries)

To execute ROCgdb, you must install the `ROCdbgapi`

library and its dependent `Comgr`

library. These can be installed as part of the ROCm release using the `rocm-dbgapi`

package:

`librocm-dbgapi.so.0`

`libamd_comgr.so`


To generate the ROCgdb user guide as a PDF, use:

```
pdf
```

This generates the PDF in `build/gdb/doc/gdb.pdf`

.
