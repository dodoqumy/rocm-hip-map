---
title: "Python API reference &#8212; hipRAND 3.1.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipRAND/en/latest/api-reference/python-api.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T18:09:26.018123+00:00
content_hash: "508d23a964d3b8a2"
---

# Python API reference[#](#python-api-reference)

This document describes the hipRAND APIs in Python.

The APIs in this wrapper are similar to [pyculib.rand](http://pyculib.readthedocs.io/en/latest/curand.html).

## class PRNG[#](#class-prng)

-
*class*hiprand.PRNG(*rngtype=400*,*seed=None*,*offset=None*,*stream=None*,***,*is_host=False*)[#](#hiprand.PRNG) -
-
MRG32K3A
*= 402*[#](#hiprand.PRNG.MRG32K3A) MRG32k3a pseudo-random generator type


-
MT19937
*= 404*[#](#hiprand.PRNG.MT19937) Mersenne Twister 19937 pseudo-random generator type


-
MTGP32
*= 403*[#](#hiprand.PRNG.MTGP32) Mersenne Twister MTGP32 pseudo-random generator type


-
PHILOX4_32_10
*= 405*[#](#hiprand.PRNG.PHILOX4_32_10) PHILOX_4x32 (10 rounds) pseudo-random generator type


-
XORWOW
*= 401*[#](#hiprand.PRNG.XORWOW) XORWOW pseudo-random generator type


-
generate(
*ary*,*size=None*)[#](#hiprand.PRNG.generate) Generates uniformly distributed integers.

Generates

**size**(if present) or**ary.size**uniformly distributed integers and saves them to**ary**.- Supported
**dtype**of**ary**for 32-bits generators: `numpy.uint32`

,`numpy.int32`

.- Supported
**dtype**of**ary**for 64-bits generators: `numpy.uint64`

,`numpy.int64`

.

- Parameters:
**ary**– NumPy array (`numpy.ndarray`

) or HIP device-side array ()`DeviceNDArray`

**size**– Number of samples to generate, default to**ary.size**


- Supported

-
lognormal(
*ary*,*mean*,*stddev*,*size=None*)[#](#hiprand.PRNG.lognormal) Generates log-normally distributed floats.

Generates

**size**(if present) or**ary.size**log-normally distributed floats and saves them to**ary**.Supported

**dtype**of**ary**:`numpy.float32`

,`numpy.float64`

.- Parameters:
**ary**– NumPy array (`numpy.ndarray`

) or HIP device-side array ()`DeviceNDArray`

**mean**– Mean value of log normal distribution**stddev**– Standard deviation value of log normal distribution**size**– Number of samples to generate, default to**ary.size**



-
normal(
*ary*,*mean*,*stddev*,*size=None*)[#](#hiprand.PRNG.normal) Generates normally distributed floats.

Generates

**size**(if present) or**ary.size**normally distributed floats and saves them to**ary**.Supported

**dtype**of**ary**:`numpy.float32`

,`numpy.float64`

.- Parameters:
**ary**– NumPy array (`numpy.ndarray`

) or HIP device-side array ()`DeviceNDArray`

**mean**– Mean value of normal distribution**stddev**– Standard deviation value of normal distribution**size**– Number of samples to generate, default to**ary.size**



-
*property*offset[#](#hiprand.PRNG.offset) Mutable attribute of the offset of random numbers sequence.

Setting this attribute resets the sequence.


-
poisson(
*ary*,*lmbd*,*size=None*)[#](#hiprand.PRNG.poisson) Generates Poisson-distributed integers.

Generates

**size**(if present) or**ary.size**Poisson-distributed integers and saves them to**ary**.Supported

**dtype**of**ary**:`numpy.uint32`

,`numpy.int32`

.- Parameters:
**ary**– NumPy array (`numpy.ndarray`

) or HIP device-side array ()`DeviceNDArray`

**lmbd**– lambda for the Poisson distribution**size**– Number of samples to generate, default to**ary.size**



-
*property*seed[#](#hiprand.PRNG.seed) Mutable attribute of the seed of random numbers sequence.

Setting this attribute resets the sequence.


-
uniform(
*ary*,*size=None*)[#](#hiprand.PRNG.uniform) Generates uniformly distributed floats.

Generates

**size**(if present) or**ary.size**uniformly distributed floats and saves them to**ary**.Supported

**dtype**of**ary**:`numpy.float32`

,`numpy.float64`

.Generated numbers are between 0.0 and 1.0, excluding 0.0 and including 1.0.

- Parameters:
**ary**– NumPy array (`numpy.ndarray`

) or HIP device-side array ()`DeviceNDArray`

**size**– Number of samples to generate, default to**ary.size**



-
MRG32K3A

## class QRNG[#](#class-qrng)

-
*class*hiprand.QRNG(*rngtype=500*,*ndim=None*,*offset=None*,*stream=None*,***,*is_host=False*)[#](#hiprand.QRNG) -
-
SCRAMBLED_SOBOL32
*= 502*[#](#hiprand.QRNG.SCRAMBLED_SOBOL32) Scrambled Sobol32 quasi-random generator type


-
SCRAMBLED_SOBOL64
*= 504*[#](#hiprand.QRNG.SCRAMBLED_SOBOL64) Scrambled Sobol64 quasi-random generator type


-
SOBOL32
*= 501*[#](#hiprand.QRNG.SOBOL32) Sobol32 quasi-random generator type


-
SOBOL64
*= 503*[#](#hiprand.QRNG.SOBOL64) Sobol64 quasi-random generator type


-
generate(
*ary*,*size=None*)[#](#hiprand.QRNG.generate) Generates uniformly distributed integers.

Generates

**size**(if present) or**ary.size**uniformly distributed integers and saves them to**ary**.- Supported
**dtype**of**ary**for 32-bits generators: `numpy.uint32`

,`numpy.int32`

.- Supported
**dtype**of**ary**for 64-bits generators: `numpy.uint64`

,`numpy.int64`

.

- Parameters:
**ary**– NumPy array (`numpy.ndarray`

) or HIP device-side array ()`DeviceNDArray`

**size**– Number of samples to generate, default to**ary.size**


- Supported

-
lognormal(
*ary*,*mean*,*stddev*,*size=None*)[#](#hiprand.QRNG.lognormal) Generates log-normally distributed floats.

Generates

**size**(if present) or**ary.size**log-normally distributed floats and saves them to**ary**.Supported

**dtype**of**ary**:`numpy.float32`

,`numpy.float64`

.- Parameters:
**ary**– NumPy array (`numpy.ndarray`

) or HIP device-side array ()`DeviceNDArray`

**mean**– Mean value of log normal distribution**stddev**– Standard deviation value of log normal distribution**size**– Number of samples to generate, default to**ary.size**



-
*property*ndim[#](#hiprand.QRNG.ndim) Mutable attribute of the number of dimensions of random numbers sequence.

Supported values are 1 to 20000. Setting this attribute resets the sequence.


-
normal(
*ary*,*mean*,*stddev*,*size=None*)[#](#hiprand.QRNG.normal) Generates normally distributed floats.

Generates

**size**(if present) or**ary.size**normally distributed floats and saves them to**ary**.Supported

**dtype**of**ary**:`numpy.float32`

,`numpy.float64`

.- Parameters:
**ary**– NumPy array (`numpy.ndarray`

) or HIP device-side array ()`DeviceNDArray`

**mean**– Mean value of normal distribution**stddev**– Standard deviation value of normal distribution**size**– Number of samples to generate, default to**ary.size**



-
*property*offset[#](#hiprand.QRNG.offset) Mutable attribute of the offset of random numbers sequence.

Setting this attribute resets the sequence.


-
poisson(
*ary*,*lmbd*,*size=None*)[#](#hiprand.QRNG.poisson) Generates Poisson-distributed integers.

Generates

**size**(if present) or**ary.size**Poisson-distributed integers and saves them to**ary**.Supported

**dtype**of**ary**:`numpy.uint32`

,`numpy.int32`

.- Parameters:
**ary**– NumPy array (`numpy.ndarray`

) or HIP device-side array ()`DeviceNDArray`

**lmbd**– lambda for the Poisson distribution**size**– Number of samples to generate, default to**ary.size**



-
uniform(
*ary*,*size=None*)[#](#hiprand.QRNG.uniform) Generates uniformly distributed floats.

Generates

**size**(if present) or**ary.size**uniformly distributed floats and saves them to**ary**.Supported

**dtype**of**ary**:`numpy.float32`

,`numpy.float64`

.Generated numbers are between 0.0 and 1.0, excluding 0.0 and including 1.0.

- Parameters:
**ary**– NumPy array (`numpy.ndarray`

) or HIP device-side array ()`DeviceNDArray`

**size**– Number of samples to generate, default to**ary.size**



-
SCRAMBLED_SOBOL32

## Exceptions[#](#exceptions)

-
*exception*hiprand.HipRandError(*value*)[#](#hiprand.HipRandError) Run-time hipRAND error.


-
*exception*hiprand.HipError(*value*)[#](#hiprand.HipError) Run-time HIP error.


## Utilities[#](#utilities)

-
*class*hiprand.DeviceNDArray(*shape*,*dtype*,*data=None*)[#](#hiprand.DeviceNDArray) Device-side array.

This class is a limited version of

`numpy.ndarray`

for device-side arrays.See

`empty()`

-
copy_to_host(
*ary=None*)[#](#hiprand.DeviceNDArray.copy_to_host) Copy from data device memory to host memory.

If

**ary**is passed then**ary**must have the same**dtype**and greater or equal**size**as**self**has.If

**ary**is not passed then a new`numpy.ndarray`

will be created.- Parameters:
**ary**– NumPy array (`numpy.ndarray`

)- Returns:
a new array or

**ary**


-
copy_to_host(

-
hiprand.empty(
*shape*,*dtype*)[#](#hiprand.empty) Create a new device-side array of given shape and type, without initializing entries.

This function is a limited version of

`numpy.empty()`

for device-side arrays.Example:

import hiprand import numpy as np gen = hiprand.QRNG(ndim=5) d_a = hiprand.empty((5, 10000), dtype=np.float32) gen.uniform(d_a) a = d_a.copy_to_host() print(a)

See

`DeviceNDArray`


-
hiprand.get_version()
[#](#hiprand.get_version) Returns the version number of the rocRAND or cuRAND library.
