---
title: "Composable Kernel custom data types &#8212; Composable Kernel 1.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/composable_kernel/en/latest/reference/Composable_Kernel_custom_types.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:10:04.035027+00:00
content_hash: "00913226c2c2c737"
---

# Composable Kernel custom data types[#](#composable-kernel-custom-data-types)

Composable Kernel supports the use of custom types that provide a way to implement specialized numerical formats.

To use custom types, a C++ type that implements the necessary operations for tensor computations needs to be created. These should include:

Constructors and initialization methods

Arithmetic operators if the type will be used in computational operations

Any conversion functions needed to interface with other parts of an application


For example, to create a complex half-precision type:

```
struct complex_half_t
{
half_t real;
half_t img;
};
struct complex_half_t
{
using type = half_t;
type real;
type img;
complex_half_t() : real{type{}}, img{type{}} {}
complex_half_t(type real_init, type img_init) : real{real_init}, img{img_init} {}
};
```

Custom types can be particularly useful for specialized applications such as complex number arithmetic, custom quantization schemes, or domain-specific number representations.
