---
title: "What is rocFFT? &#8212; rocFFT 1.0.36 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocFFT/en/latest/what-is-rocfft.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:07:01.928645+00:00
content_hash: "11f6bbb003246045"
---

# What is rocFFT?[#](#what-is-rocfft)

The rocFFT library implements the discrete Fast Fourier Transform (FFT) in HIP for GPU devices.
It provides a fast and accurate platform for calculating discrete FFTs.
The source code can be found at [ROCm/rocm-libraries](https://github.com/ROCm/rocm-libraries/tree/develop/projects/rocfft).

rocFFT supports the following features:

Half (

`FP16`

), single, and double precision floating point formats1D, 2D, and 3D transforms

Computation of transforms in batches

Real and complex FFTs

Arbitrary lengths, with optimizations for combinations of powers of 2, 3, 5, 7, 11, 13, and 17


rocFFT also provides experimental support for:

Distributing transforms across multiple GPU devices in a single process

Distributing transforms across multiple MPI (Message Passing Interface) processes


For information about how rocFFT computes FFTs, see [FFT computation](conceptual/fft-computation.html).
