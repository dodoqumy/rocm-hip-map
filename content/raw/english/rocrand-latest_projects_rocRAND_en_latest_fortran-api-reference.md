---
title: "Fortran API reference &#8212; rocRAND 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocRAND/en/latest/fortran-api-reference.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T18:08:45.683664+00:00
content_hash: "70ee0fe58048af22"
---

# Fortran API reference[#](#fortran-api-reference)

This library provides a pure Fortran interface for the rocRAND API.

This interface is intended to target only Host API functions. It provides a mapping to some of the C Host API functions in rocRAND. For documentation of these functions, see the C Host API functions documentation.

## Deprecation notice[#](#deprecation-notice)

This library is currently deprecated in favor of [hipfort](https://github.com/ROCm/hipfort).

## Build and install[#](#build-and-install)

The Fortran interface is installed as part of the rocRAND package. Add the build
option `-DBUILD_FORTRAN_WRAPPER=ON`

when configuring the project, as shown below:

```
-DBUILD_FORTRAN_WRAPPER=ON ...
```

## Running unit tests[#](#running-unit-tests)

Configure the project with testing enabled, using the `-DBUILD_TEST=ON`

option, then follow the steps below
to build and run the unit tests.

Go to the rocRAND

`build`

directory:

```
cd /path/to/rocRAND/build
```

Build the unit tests for the Fortran interface:


```
--build . --target test_rocrand_fortran_wrapper
```

Run the unit tests:



## Usage[#](#usage)

Here is an example of how to write a simple Fortran program that generates a set of uniform values.

```
integer(kind =8) :: gen
real, target, dimension(128) :: h_x
type(c_ptr) :: d_x
integer(c_int) :: status
integer(c_size_t), parameter :: output_size = 128
status = hipMalloc(d_x, output_size * sizeof(h_x(1)))
status = rocrand_create_generator(gen, ROCRAND_RNG_PSEUDO_DEFAULT)
status = rocrand_generate_uniform(gen, d_x, output_size)
status = hipMemcpy(c_loc(h_x), d_x, output_size * sizeof(h_x(1)), hipMemcpyDeviceToHost)
status = hipFree(d_x)
status = rocrand_destroy_generator(gen)
```

When compiling the source code with a Fortran compiler, the following items should be linked[[1]](#id2):

```
# Compile on an AMD platform (link HIP library: ${HIP_ROOT_DIR}/lib).
# Note: ${HIP_ROOT_DIR} points to the directory where HIP was installed.
gfortran <input-file>.f90 hip_m.f90 rocrand_m.f90 -lrocrand_fortran -lrocrand -L${HIP_ROOT_DIR}/lib
```
