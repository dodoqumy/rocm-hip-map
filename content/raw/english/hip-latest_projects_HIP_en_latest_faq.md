---
title: "Frequently asked questions &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/faq.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:05:59.666733+00:00
content_hash: "a63bc8dfb6eb61b3"
---

# Frequently asked questions[#](#frequently-asked-questions)

This topic provides answers to frequently asked questions from new HIP users and users familiar with NVIDIA CUDA.

## HIP support[#](#hip-support)

### What hardware does HIP support?[#](#what-hardware-does-hip-support)

HIP supports AMD GPUs. See
[prerequisites of the install guide](install/install.html#install-prerequisites) for detailed
information.

### What operating systems does HIP support?[#](#what-operating-systems-does-hip-support)

Linux as well as Windows are supported by ROCm. The exact versions are listed in
the system requirements for [Supported operating systems](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html#supported-distributions)
and [Supported OSes](https://rocm.docs.amd.com/projects/install-on-windows/en/docs-7.1.1/reference/system-requirements.html#supported-oses).

### What libraries does HIP provide?[#](#what-libraries-does-hip-provide)

HIP provides key math and AI libraries. See [ROCm libraries](https://rocm.docs.amd.com/en/latest/reference/api-libraries.html)
for the full list.

### What CUDA features can be ported to HIP?[#](#what-cuda-features-can-be-ported-to-hip)

The [NVIDIA CUDA runtime API supported by HIP](https://rocm.docs.amd.com/projects/HIPIFY/en/latest/reference/tables/CUDA_Runtime_API_functions_supported_by_HIP.html)
and [NVIDIA CUDA driver API supported by HIP](https://rocm.docs.amd.com/projects/HIPIFY/en/latest/reference/tables/CUDA_Driver_API_functions_supported_by_HIP.html)
pages describe which CUDA APIs can be automatically converted to HIP equivalents.
The [HIP runtime API reference](reference/hip_runtime_api_reference.html#runtime-api-reference) describes each HIP API and
its limitations, if any, compared with the equivalent CUDA API.

The kernel language features are documented in the
[HIP C++ language extensions](how-to/hip_cpp_language_extensions.html) page.

## Relation to other GPGPU frameworks[#](#relation-to-other-gpgpu-frameworks)

### How easy is it to port CUDA code to HIP?[#](#how-easy-is-it-to-port-cuda-code-to-hip)

The [HIPIFY](https://github.com/ROCm/HIPIFY) tools can automatically convert
almost all CUDA runtime code to HIP. Most device code needs no additional
conversion because HIP and CUDA have the same signatures for math and built-in
functions except for the name. Once ported to HIP, code can be optimized for AMD GPU
architectures.

Additional porting might be required to deal with architecture feature queries or CUDA capabilities that HIP doesn’t support.

To better understand the syntax differences, see [CUDA to HIP API Function Comparison](reference/api_syntax.html)
or the [HIP porting guide](how-to/hip_porting_guide.html).
