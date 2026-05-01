---
title: "Composable Kernel vector template utilities &#8212; Composable Kernel 1.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/composable_kernel/en/latest/reference/Composable_Kernel_vector_utilities.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:17:03.879233+00:00
content_hash: "8c42c0afde7983cb"
---

# Composable Kernel vector template utilities[#](#composable-kernel-vector-template-utilities)

Composable Kernel includes template utilities for creating vector types with customizable widths. These template utilities also flatten nested vector types into a single, wider vector, preventing the creation of vectors of vectors.

Vectors composed of supported scalar and custom types can be created with the `ck::vector_type`

template.

For example, `ck::vector_type<float, 4>`

creates a vector composed of four floats and `ck::vector_type<ck::half_t, 8>`

creates a vector composed of eight half-precision scalars.

For vector operations to be valid, the underlying types must be either a [supported scalar type](Composable_Kernel_supported_scalar_types.html) or [a custom type](Composable_Kernel_custom_types.html) that implements the required operations.
