---
title: "Using hipify-perl"
source_url: "https://rocm.docs.amd.com/projects/HIPIFY/en/latest/hipify-perl.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-04-28
---

::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}

::: header-article-item
- [](../index.html){.nav-link aria-label="Home"}
- [Using hipify-perl]{.ellipsis}

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons

[]{.fa-solid .fa-list}

# Using hipify-perl

## Contents

- [Example](#example){.reference .internal .nav-link}



# Using hipify-perl[\#](#using-hipify-perl "Link to this heading"){.headerlink}

[`hipify-perl`{.docutils .literal .notranslate}]{.pre} is perl-based script that heavily uses regular expressions, that is automatically generated from [`hipify-clang`{.docutils .literal .notranslate}]{.pre}.

**Advantages:**

- Ease of use

- No checks for input source NVIDIA CUDA code for correctness required

- No dependency on third party tools, including CUDA

**Disadvantages:**

- Inability or difficulty in implementing the following constructs:

  - Macros expansion

  - Namespaces:

    - Redefinition of CUDA entities in user namespaces

    - Using directive

  - Templates (some cases)

  - Device or host function calls differentiation

  - Correct injection of header files

  - Parsing complicated argument lists

## Example[\#](#example "Link to this heading"){.headerlink}

For additional details on the following [`hipify-perl`{.docutils .literal .notranslate}]{.pre} command options, see [[hipify-perl commands]{.std .std-ref}](../reference/hipify-perl-cmd.html#hipify-perl-cmd){.reference .internal}. For more advanced translation needs use [`hipify-clang`{.docutils .literal .notranslate}]{.pre} as it is more comprehensive and accurate.

Convert a simple CUDA file ([`square.cu`{.docutils .literal .notranslate}]{.pre}) to HIP using [`hipify-perl`{.docutils .literal .notranslate}]{.pre}:

::: highlight
    hipify-perl square.cu -o square.cu.hip

This command translates the input file and writes the result to [`square.cu.hip`{.docutils .literal .notranslate}]{.pre}.

::::: prev-next-area
[](hipify-clang.html "previous page"){.left-prev}

::: prev-next-info
previous

Using hipify-clang

[](../reference/hipify-clang-cmd.html "next page"){.right-next}

::: prev-next-info
next

hipify-clang commands

:::: sidebar-secondary-item
Contents

- [Example](#example){.reference .internal .nav-link}
