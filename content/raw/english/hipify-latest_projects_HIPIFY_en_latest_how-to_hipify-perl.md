---
title: "Using hipify-perl &#8212; HIPIFY Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIPIFY/en/latest/how-to/hipify-perl.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:12:25.958777+00:00
content_hash: "03c21f8ea3646a76"
---

# Using hipify-perl[#](#using-hipify-perl)

`hipify-perl`

is perl-based script that heavily uses regular expressions, that is automatically generated from `hipify-clang`

.

**Advantages:**

Ease of use

No checks for input source NVIDIA CUDA code for correctness required

No dependency on third party tools, including CUDA


**Disadvantages:**

Inability or difficulty in implementing the following constructs:

Macros expansion

Namespaces:

Redefinition of CUDA entities in user namespaces

Using directive


Templates (some cases)

Device or host function calls differentiation

Correct injection of header files

Parsing complicated argument lists



## Example[#](#example)

For additional details on the following `hipify-perl`

command options, see [hipify-perl commands](../reference/hipify-perl-cmd.html#hipify-perl-cmd). For more advanced translation needs use `hipify-clang`

as it is more comprehensive and accurate.

Convert a simple CUDA file (`square.cu`

) to HIP using `hipify-perl`

:

```
square.cu -o square.cu.hip
```

This command translates the input file and writes the result to `square.cu.hip`

.
