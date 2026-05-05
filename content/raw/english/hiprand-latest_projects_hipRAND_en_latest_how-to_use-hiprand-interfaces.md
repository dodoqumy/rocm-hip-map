---
title: "Using hipRAND interfaces &#8212; hipRAND 3.1.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipRAND/en/latest/how-to/use-hiprand-interfaces.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T18:09:27.933127+00:00
content_hash: "a410ecec2b9b64b7"
---

# Using hipRAND interfaces[#](#using-hiprand-interfaces)

The hipRAND interface is compatible with the rocRAND API. Porting a CUDA application that calls the cuRAND API to an application that calls the hipRAND API is relatively straightforward.

## Host API[#](#host-api)

For example, to create a generator, follow this example:

```
hiprandStatus_t
hiprandCreateGenerator(
hiprandGenerator_t* generator,
hiprandRngType_t rng_type
)
```

## Device API[#](#device-api)

Here is an example that generates a log-normally distributed float from a generator. These functions are templated for all generators.

```
__device__ double
hiprand_log_normal_double(
hiprandStateSobol64_t* state,
double mean,
double stddev
)
```
