---
title: "Data types and precision support"
source_url: "https://rocm.docs.amd.com/en/latest/reference/precision-support.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-01
---

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-content
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-article-container
:::::::::: {.bd-header-article .d-print-none}
::::::::: {.header-article-items .header-article__inner}
::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}
:::

::: header-article-item
- [](../index.html){.nav-link aria-label="Home"}
- Data types\...
:::
:::::

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons
[]{.fa-solid .fa-list}
:::
::::
:::::
:::::::::
::::::::::

:::::: {#jb-print-docs-body .onlyprint}
# Data types and precision support

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [Integral types](#integral-types){.reference .internal .nav-link}
- [Floating-point types](#floating-point-types){.reference .internal .nav-link}
- [Level of support definitions](#level-of-support-definitions){.reference .internal .nav-link}
- [Data type support by hardware architecture](#data-type-support-by-hardware-architecture){.reference .internal .nav-link}
  - [HIP C++ type implementation support](#hip-c-type-implementation-support){.reference .internal .nav-link}
  - [Compute units support](#compute-units-support){.reference .internal .nav-link}
  - [Matrix core support](#matrix-core-support){.reference .internal .nav-link}
  - [Atomic operations support](#atomic-operations-support){.reference .internal .nav-link}
- [Data type support in ROCm libraries](#data-type-support-in-rocm-libraries){.reference .internal .nav-link}
  - [Libraries input/output type support](#libraries-input-output-type-support){.reference .internal .nav-link}
  - [hipDataType enumeration](#hipdatatype-enumeration){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#data-types-and-precision-support .section}
# Data types and precision support[\#](#data-types-and-precision-support "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 12 min read time
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils style="color:gray;"}
Applies to Linux and Windows
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
:::
:::::::
::::::::
:::::::::
::::::::::
:::::::::::

This topic summarizes the data types supported on AMD GPUs and ROCm libraries, along with corresponding [[HIP]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/HIP/en/latest/index.html "(in HIP Documentation v7.2.53211)"){.reference .external} data types.

:::: {#integral-types .section}
## Integral types[\#](#integral-types "Link to this heading"){.headerlink}

The signed and unsigned integral types supported by ROCm are listed in the following table.

::: pst-scrollable-table-container
+-----------+---------------------------------------------------------------------------------------------------------+-------------------------------------+
| Type name | HIP type                                                                                                | Description                         |
+===========+=========================================================================================================+=====================================+
| int8      | [`int8_t`{.docutils .literal .notranslate}]{.pre}, [`uint8_t`{.docutils .literal .notranslate}]{.pre}   | A signed or unsigned 8-bit integer  |
+-----------+---------------------------------------------------------------------------------------------------------+-------------------------------------+
| int16     | [`int16_t`{.docutils .literal .notranslate}]{.pre}, [`uint16_t`{.docutils .literal .notranslate}]{.pre} | A signed or unsigned 16-bit integer |
+-----------+---------------------------------------------------------------------------------------------------------+-------------------------------------+
| int32     | [`int32_t`{.docutils .literal .notranslate}]{.pre}, [`uint32_t`{.docutils .literal .notranslate}]{.pre} | A signed or unsigned 32-bit integer |
+-----------+---------------------------------------------------------------------------------------------------------+-------------------------------------+
| int64     | [`int64_t`{.docutils .literal .notranslate}]{.pre}, [`uint64_t`{.docutils .literal .notranslate}]{.pre} | A signed or unsigned 64-bit integer |
+-----------+---------------------------------------------------------------------------------------------------------+-------------------------------------+
:::
::::

::::: {#floating-point-types .section}
[]{#precision-support-floating-point-types}

## Floating-point types[\#](#floating-point-types "Link to this heading"){.headerlink}

The floating-point types supported by ROCm are listed in the following table.

![Supported floating-point types](../_images/floating-point-data-types.png)

::: pst-scrollable-table-container
+---------------+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Type name     | HIP type                                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+===============+=================================================================+==================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| float4 (E2M1) | ::: line                                                        | A 4-bit floating-point number with **E2M1** bit layout, as described in [[low precision floating point types page]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/HIP/en/latest/reference/low_fp_types.html "(in HIP Documentation v7.2.53211)"){.reference .external}.                                                                                                                                                                                |
|               | [`__hip_fp4_e2m1`{.docutils .literal .notranslate}]{.pre}       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|               | :::                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+---------------+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| float6 (E3M2) | ::: line                                                        | A 6-bit floating-point number with **E3M2** bit layout, as described in [[low precision floating point types page]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/HIP/en/latest/reference/low_fp_types.html "(in HIP Documentation v7.2.53211)"){.reference .external}.                                                                                                                                                                                |
|               | [`__hip_fp6_e3m2`{.docutils .literal .notranslate}]{.pre}       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|               | :::                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+---------------+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| float6 (E2M3) | ::: line                                                        | A 6-bit floating-point number with **E2M3** bit layout, as described in [[low precision floating point types page]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/HIP/en/latest/reference/low_fp_types.html "(in HIP Documentation v7.2.53211)"){.reference .external}.                                                                                                                                                                                |
|               | [`__hip_fp6_e2m3`{.docutils .literal .notranslate}]{.pre}       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|               | :::                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+---------------+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| float8 (E4M3) | ::: line                                                        | An 8-bit floating-point number with **E4M3** bit layout, as described in [[low precision floating point types page]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/HIP/en/latest/reference/low_fp_types.html "(in HIP Documentation v7.2.53211)"){.reference .external}. The FNUZ variant has expanded range with no infinity or signed zero (NaN represented as negative zero), while the OCP variant follows the Open Compute Project specification. |
|               | [`__hip_fp8_e4m3_fnuz`{.docutils .literal .notranslate}]{.pre}, |                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|               | :::                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|               |                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|               | ::: line                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|               | [`__hip_fp8_e4m3`{.docutils .literal .notranslate}]{.pre}       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|               | :::                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+---------------+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| float8 (E5M2) | ::: line                                                        | An 8-bit floating-point number with **E5M2** bit layout, as described in [[low precision floating point types page]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/HIP/en/latest/reference/low_fp_types.html "(in HIP Documentation v7.2.53211)"){.reference .external}. The FNUZ variant has expanded range with no infinity or signed zero (NaN represented as negative zero), while the OCP variant follows the Open Compute Project specification. |
|               | [`__hip_fp8_e5m2_fnuz`{.docutils .literal .notranslate}]{.pre}, |                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|               | :::                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|               |                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|               | ::: line                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|               | [`__hip_fp8_e5m2`{.docutils .literal .notranslate}]{.pre}       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|               | :::                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+---------------+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| float16       | [`half`{.docutils .literal .notranslate}]{.pre}                 | A 16-bit floating-point number that conforms to the IEEE 754-2008 half-precision storage format.                                                                                                                                                                                                                                                                                                                                                                 |
+---------------+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| bfloat16      | [`bfloat16`{.docutils .literal .notranslate}]{.pre}             | A shortened 16-bit version of the IEEE 754 single-precision storage format.                                                                                                                                                                                                                                                                                                                                                                                      |
+---------------+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| tensorfloat32 | Not available                                                   | A floating-point number that occupies 32 bits or less of storage, providing improved range compared to half (16-bit) format, at (potentially) greater throughput than single-precision (32-bit) formats.                                                                                                                                                                                                                                                         |
+---------------+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| float32       | [`float`{.docutils .literal .notranslate}]{.pre}                | A 32-bit floating-point number that conforms to the IEEE 754 single-precision storage format.                                                                                                                                                                                                                                                                                                                                                                    |
+---------------+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| float64       | [`double`{.docutils .literal .notranslate}]{.pre}               | A 64-bit floating-point number that conforms to the IEEE 754 double-precision storage format.                                                                                                                                                                                                                                                                                                                                                                    |
+---------------+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
:::

::: {.admonition .note}
Note

- The float8 and tensorfloat32 types are internal types used in calculations in Matrix Cores and can be stored in any type of the same size.

- CDNA3 natively supports FP8 FNUZ (E4M3 and E5M2), which differs from the customized FP8 format used with NVIDIA H100 ([FP8 Formats for Deep Learning](https://arxiv.org/abs/2209.05433){.reference .external}).

- In some AMD documents and articles, float8 (E5M2) is referred to as bfloat8.

- The [[low precision floating point types page]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/HIP/en/latest/reference/low_fp_types.html "(in HIP Documentation v7.2.53211)"){.reference .external} describes how to use these types in HIP with examples.
:::
:::::

::::: {#level-of-support-definitions .section}
## Level of support definitions[\#](#level-of-support-definitions "Link to this heading"){.headerlink}

In the following sections, icons represent the level of support. These icons, described in the following table, are also used in the library data type support pages.

::: pst-scrollable-table-container
  Icon   Definition
  ------ -----------------
  NA     Not applicable
  ❌     Not supported
  ⚠️     Partial support
  ✅     Full support
:::

::: {.admonition .note}
Note

- Full support means that the type is supported natively or with hardware emulation.

- Native support means that the operations for that type are implemented in hardware. Types that are not natively supported are emulated with the available hardware. The performance of non-natively supported types can differ from the full instruction throughput rate. For example, 16-bit integer operations can be performed on the 32-bit integer ALUs at full rate; however, 64-bit integer operations might need several instructions on the 32-bit integer ALUs.

- Any type can be emulated by software, but this page does not cover such cases.
:::
:::::

::::::::::::::::::::::::::::::: {#data-type-support-by-hardware-architecture .section}
## Data type support by hardware architecture[\#](#data-type-support-by-hardware-architecture "Link to this heading"){.headerlink}

AMD's GPU lineup spans multiple architecture generations:

- CDNA1 such as MI100

- CDNA2 such as MI210, MI250, and MI250X

- CDNA3 such as MI300A, MI300X, and MI325X

- CDNA4 such as MI350X and MI355X

- RDNA2 such as PRO W6800 and PRO V620

- RDNA3 such as RX 7900XT and RX 7900XTX

- RDNA4 such as RX 9070 and RX 9070XT

::::: {#hip-c-type-implementation-support .section}
### HIP C++ type implementation support[\#](#hip-c-type-implementation-support "Link to this heading"){.headerlink}

The HIP C++ types available on different hardware platforms are listed in the following table.

::: pst-scrollable-table-container
  HIP C++ Type                                                                                              CDNA1   CDNA2   CDNA3   CDNA4   RDNA2   RDNA3   RDNA4
  --------------------------------------------------------------------------------------------------------- ------- ------- ------- ------- ------- ------- -------
  [`int8_t`{.docutils .literal .notranslate}]{.pre}, [`uint8_t`{.docutils .literal .notranslate}]{.pre}     ✅      ✅      ✅      ✅      ✅      ✅      ✅
  [`int16_t`{.docutils .literal .notranslate}]{.pre}, [`uint16_t`{.docutils .literal .notranslate}]{.pre}   ✅      ✅      ✅      ✅      ✅      ✅      ✅
  [`int32_t`{.docutils .literal .notranslate}]{.pre}, [`uint32_t`{.docutils .literal .notranslate}]{.pre}   ✅      ✅      ✅      ✅      ✅      ✅      ✅
  [`int64_t`{.docutils .literal .notranslate}]{.pre}, [`uint64_t`{.docutils .literal .notranslate}]{.pre}   ✅      ✅      ✅      ✅      ✅      ✅      ✅
  [`__hip_fp4_e2m1`{.docutils .literal .notranslate}]{.pre}                                                 ❌      ❌      ❌      ✅      ❌      ❌      ❌
  [`__hip_fp6_e2m3`{.docutils .literal .notranslate}]{.pre}                                                 ❌      ❌      ❌      ✅      ❌      ❌      ❌
  [`__hip_fp6_e3m2`{.docutils .literal .notranslate}]{.pre}                                                 ❌      ❌      ❌      ✅      ❌      ❌      ❌
  [`__hip_fp8_e4m3_fnuz`{.docutils .literal .notranslate}]{.pre}                                            ❌      ❌      ✅      ❌      ❌      ❌      ❌
  [`__hip_fp8_e5m2_fnuz`{.docutils .literal .notranslate}]{.pre}                                            ❌      ❌      ✅      ❌      ❌      ❌      ❌
  [`__hip_fp8_e4m3`{.docutils .literal .notranslate}]{.pre}                                                 ❌      ❌      ❌      ✅      ❌      ❌      ✅
  [`__hip_fp8_e5m2`{.docutils .literal .notranslate}]{.pre}                                                 ❌      ❌      ❌      ✅      ❌      ❌      ✅
  [`half`{.docutils .literal .notranslate}]{.pre}                                                           ✅      ✅      ✅      ✅      ✅      ✅      ✅
  [`bfloat16`{.docutils .literal .notranslate}]{.pre}                                                       ✅      ✅      ✅      ✅      ✅      ✅      ✅
  [`float`{.docutils .literal .notranslate}]{.pre}                                                          ✅      ✅      ✅      ✅      ✅      ✅      ✅
  [`double`{.docutils .literal .notranslate}]{.pre}                                                         ✅      ✅      ✅      ✅      ✅      ✅      ✅
:::

::: {.admonition .note}
Note

Library support for specific data types is contingent upon hardware support. Even if a ROCm library indicates support for a particular data type, that type will only be fully functional if the underlying hardware architecture (as shown in the table above) also supports it. For example, fp8 types are only available on architectures shown with a checkmark in the relevant rows.
:::
:::::

:::::::::: {#compute-units-support .section}
### Compute units support[\#](#compute-units-support "Link to this heading"){.headerlink}

The following table lists data type support for compute units.

::::::::: {.sd-tab-set .docutils}
Integral types

:::: {.sd-tab-content .docutils}
::: pst-scrollable-table-container
  Type name   int8   int16   int32   int64
  ----------- ------ ------- ------- -------
  CDNA1       ✅     ✅      ✅      ✅
  CDNA2       ✅     ✅      ✅      ✅
  CDNA3       ✅     ✅      ✅      ✅
  CDNA4       ✅     ✅      ✅      ✅
  RDNA2       ✅     ✅      ✅      ✅
  RDNA3       ✅     ✅      ✅      ✅
  RDNA4       ✅     ✅      ✅      ✅
:::
::::

Low precision floating-point types

:::: {.sd-tab-content .docutils}
::: pst-scrollable-table-container
  Type name   float4   float6 (E2M3)   float6 (E3M2)   float8 (E4M3)   float8 (E5M2)
  ----------- -------- --------------- --------------- --------------- ---------------
  CDNA1       ❌       ❌              ❌              ❌              ❌
  CDNA2       ❌       ❌              ❌              ❌              ❌
  CDNA3       ❌       ❌              ❌              ❌              ❌
  CDNA4       ❌       ❌              ❌              ❌              ❌
  RDNA2       ❌       ❌              ❌              ❌              ❌
  RDNA3       ❌       ❌              ❌              ❌              ❌
  RDNA4       ❌       ❌              ❌              ❌              ❌
:::
::::

High precision floating-point types

:::: {.sd-tab-content .docutils}
::: pst-scrollable-table-container
  Type name   float16   bfloat16   tensorfloat32   float32   float64
  ----------- --------- ---------- --------------- --------- ---------
  CDNA1       ✅        ✅         ❌              ✅        ✅
  CDNA2       ✅        ✅         ❌              ✅        ✅
  CDNA3       ✅        ✅         ❌              ✅        ✅
  CDNA4       ✅        ✅         ❌              ✅        ✅
  RDNA2       ✅        ✅         ❌              ✅        ✅
  RDNA3       ✅        ✅         ❌              ✅        ✅
  RDNA4       ✅        ✅         ❌              ✅        ✅
:::
::::
:::::::::
::::::::::

:::::::::: {#matrix-core-support .section}
### Matrix core support[\#](#matrix-core-support "Link to this heading"){.headerlink}

The following table lists data type support for AMD GPU matrix cores.

::::::::: {.sd-tab-set .docutils}
Integral types

:::: {.sd-tab-content .docutils}
::: pst-scrollable-table-container
  Type name   int8   int16   int32   int64
  ----------- ------ ------- ------- -------
  CDNA1       ✅     ❌      ❌      ❌
  CDNA2       ✅     ❌      ❌      ❌
  CDNA3       ✅     ❌      ❌      ❌
  CDNA4       ✅     ❌      ❌      ❌
  RDNA2       ✅     ❌      ❌      ❌
  RDNA3       ✅     ❌      ❌      ❌
  RDNA4       ✅     ❌      ❌      ❌
:::
::::

Low precision floating-point types

:::: {.sd-tab-content .docutils}
::: pst-scrollable-table-container
  Type name   float4   float6 (E2M3)   float6 (E3M2)   float8 (E4M3)   float8 (E5M2)
  ----------- -------- --------------- --------------- --------------- ---------------
  CDNA1       ❌       ❌              ❌              ❌              ❌
  CDNA2       ❌       ❌              ❌              ❌              ❌
  CDNA3       ❌       ❌              ❌              ✅              ✅
  CDNA4       ✅       ✅              ✅              ✅              ✅
  RDNA2       ❌       ❌              ❌              ❌              ❌
  RDNA3       ❌       ❌              ❌              ❌              ❌
  RDNA4       ❌       ❌              ❌              ✅              ✅
:::
::::

High precision floating-point types

:::: {.sd-tab-content .docutils}
::: pst-scrollable-table-container
  Type name   float16   bfloat16   tensorfloat32   float32   float64
  ----------- --------- ---------- --------------- --------- ---------
  CDNA1       ✅        ✅         ❌              ✅        ❌
  CDNA2       ✅        ✅         ❌              ✅        ✅
  CDNA3       ✅        ✅         ✅              ✅        ✅
  CDNA4       ✅        ✅         ✅              ✅        ✅
  RDNA2       ✅        ✅         ❌              ❌        ❌
  RDNA3       ✅        ✅         ❌              ❌        ❌
  RDNA4       ✅        ✅         ❌              ❌        ❌
:::
::::
:::::::::
::::::::::

::::::::::: {#atomic-operations-support .section}
### Atomic operations support[\#](#atomic-operations-support "Link to this heading"){.headerlink}

The following table lists which data types are supported for atomic operations on AMD GPUs. The atomics operation type behavior is affected by the memory locations, memory granularity, or scope of operations. For detailed various support of atomic read-modify-write (atomicRMW) operations collected on the [[Hardware atomics operation support]{.std .std-ref}](gpu-atomics-operation.html#hw-atomics-operation-support){.reference .internal} page.

::::::::: {.sd-tab-set .docutils}
Integral types

:::: {.sd-tab-content .docutils}
::: pst-scrollable-table-container
  Type name   int8   int16   int32   int64
  ----------- ------ ------- ------- -------
  CDNA1       ❌     ❌      ✅      ✅
  CDNA2       ❌     ❌      ✅      ✅
  CDNA3       ❌     ❌      ✅      ✅
  RDNA3       ❌     ❌      ✅      ✅
  RDNA4       ❌     ❌      ✅      ✅
:::
::::

Low precision floating-point types

:::: {.sd-tab-content .docutils}
::: pst-scrollable-table-container
  Type name   float4   float6 (E2M3)   float6 (E3M2)   float8 (E4M3)   float8 (E5M2)
  ----------- -------- --------------- --------------- --------------- ---------------
  CDNA1       ❌       ❌              ❌              ❌              ❌
  CDNA2       ❌       ❌              ❌              ❌              ❌
  CDNA3       ❌       ❌              ❌              ❌              ❌
  CDNA4       ❌       ❌              ❌              ❌              ❌
  RDNA2       ❌       ❌              ❌              ❌              ❌
  RDNA3       ❌       ❌              ❌              ❌              ❌
  RDNA4       ❌       ❌              ❌              ❌              ❌
:::
::::

High precision floating-point types

:::: {.sd-tab-content .docutils}
::: pst-scrollable-table-container
  Type name   2 x float16   2 x bfloat16   tensorfloat32   float32   float64
  ----------- ------------- -------------- --------------- --------- ---------
  CDNA1       ✅            ✅             ❌              ✅        ❌
  CDNA2       ✅            ✅             ❌              ✅        ✅
  CDNA3       ✅            ✅             ❌              ✅        ✅
  CDNA4       ✅            ✅             ❌              ✅        ✅
  RDNA2       ❌            ❌             ❌              ✅        ❌
  RDNA3       ❌            ❌             ❌              ✅        ❌
  RDNA4       ✅            ✅             ❌              ✅        ❌
:::
::::
:::::::::

::: {.admonition .note}
Note

You can emulate atomic operations using software for cases that are not natively supported. Software-emulated atomic operations have a high negative performance impact when they frequently access the same memory address.
:::
:::::::::::
:::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#data-type-support-in-rocm-libraries .section}
## Data type support in ROCm libraries[\#](#data-type-support-in-rocm-libraries "Link to this heading"){.headerlink}

ROCm library support for int8, float8 (E4M3), float8 (E5M2), int16, float16, bfloat16, int32, tensorfloat32, float32, int64, and float64 is listed in the following tables.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#libraries-input-output-type-support .section}
### Libraries input/output type support[\#](#libraries-input-output-type-support "Link to this heading"){.headerlink}

The following tables list ROCm library support for specific input and output data types. Select a library from the below table to view the supported data types.

::::::::::::::::::::::::::::::::::: {#vllm-benchmark-ud-params-picker .container-fluid}
::::::::: row
::: {.col-2 .me-2 .model-param-head}
Category
:::

::::::: {.row .col-10}
::: {.col-6 .model-param param-k="model-group" param-v="ml-cv" tabindex="0"}
ML & Computer Vision
:::

::: {.col-6 .model-param param-k="model-group" param-v="communication" tabindex="0"}
Communication
:::

::: {.col-6 .model-param param-k="model-group" param-v="math-libs" tabindex="0"}
Math Libraries
:::

::: {.col-6 .model-param param-k="model-group" param-v="primitives" tabindex="0"}
Primitives
:::
:::::::
:::::::::

::::::::::::::::::::::::::: {.row .mt-1}
::: {.col-2 .me-2 .model-param-head}
Library
:::

::::::::::::::::::::::::: {.row .col-10}
::: {.col-6 .model-param param-group="ml-cv" param-k="model" param-v="composable-kernel" tabindex="0"}
Composable Kernel
:::

::: {.col-6 .model-param param-group="ml-cv" param-k="model" param-v="migraphx" tabindex="0"}
MIGraphX
:::

::: {.col-6 .model-param param-group="ml-cv" param-k="model" param-v="miopen" tabindex="0"}
MIOpen
:::

::: {.col-6 .model-param param-group="communication" param-k="model" param-v="rccl" tabindex="0"}
RCCL
:::

::: {.col-6 .model-param param-group="math-libs" param-k="model" param-v="hipblas" tabindex="0"}
hipBLAS
:::

::: {.col-6 .model-param param-group="math-libs" param-k="model" param-v="hipblaslt" tabindex="0"}
hipBLASLt
:::

::: {.col-6 .model-param param-group="math-libs" param-k="model" param-v="hipfft" tabindex="0"}
hipFFT
:::

::: {.col-6 .model-param param-group="math-libs" param-k="model" param-v="hiprand" tabindex="0"}
hipRAND
:::

::: {.col-6 .model-param param-group="math-libs" param-k="model" param-v="hipsolver" tabindex="0"}
hipSOLVER
:::

::: {.col-6 .model-param param-group="math-libs" param-k="model" param-v="hipsparse" tabindex="0"}
hipSPARSE
:::

::: {.col-6 .model-param param-group="math-libs" param-k="model" param-v="hipsparselt" tabindex="0"}
hipSPARSELt
:::

::: {.col-6 .model-param param-group="math-libs" param-k="model" param-v="rocblas" tabindex="0"}
rocBLAS
:::

::: {.col-6 .model-param param-group="math-libs" param-k="model" param-v="rocfft" tabindex="0"}
rocFFT
:::

::: {.col-6 .model-param param-group="math-libs" param-k="model" param-v="rocrand" tabindex="0"}
rocRAND
:::

::: {.col-6 .model-param param-group="math-libs" param-k="model" param-v="rocsolver" tabindex="0"}
rocSOLVER
:::

::: {.col-6 .model-param param-group="math-libs" param-k="model" param-v="rocsparse" tabindex="0"}
rocSPARSE
:::

::: {.col-6 .model-param param-group="math-libs" param-k="model" param-v="rocwmma" tabindex="0"}
rocWMMA
:::

::: {.col-6 .model-param param-group="math-libs" param-k="model" param-v="tensile" tabindex="0"}
Tensile
:::

::: {.col-6 .model-param param-group="primitives" param-k="model" param-v="hipcub" tabindex="0"}
hipCUB
:::

::: {.col-6 .model-param param-group="primitives" param-k="model" param-v="hiptensor" tabindex="0"}
hipTensor
:::

::: {.col-6 .model-param param-group="primitives" param-k="model" param-v="rocprim" tabindex="0"}
rocPRIM
:::

::: {.col-6 .model-param param-group="primitives" param-k="model" param-v="rocthrust" tabindex="0"}
rocThrust
:::
:::::::::::::::::::::::::
:::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::

:::: {.model-doc .composable-kernel .docutils .container}
For more information, please visit [[Composable Kernel]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/composable_kernel/en/latest/reference/Composable_Kernel_supported_scalar_types.html "(in Composable Kernel Documentation v1.2.0)"){.reference .external}.

::: pst-scrollable-table-container
+-------------------------------------------------+--------------------+
| Data Type                                       | Support            |
+=================================================+====================+
| int8                                            | ✅                 |
+-------------------------------------------------+--------------------+
| int32                                           | ✅                 |
+-------------------------------------------------+--------------------+
| float4                                          | ✅                 |
+-------------------------------------------------+--------------------+
| float6 (E2M3)                                   | ✅                 |
+-------------------------------------------------+--------------------+
| float6 (E3M2)                                   | ✅                 |
+-------------------------------------------------+--------------------+
| float8 (E4M3)                                   | ✅                 |
+-------------------------------------------------+--------------------+
| float8 (E5M2)                                   | ✅                 |
+-------------------------------------------------+--------------------+
| float16                                         | ✅                 |
+-------------------------------------------------+--------------------+
| bfloat16                                        | ✅                 |
+-------------------------------------------------+--------------------+
| float32                                         | ✅                 |
+-------------------------------------------------+--------------------+
| float64                                         | ✅                 |
+-------------------------------------------------+--------------------+
:::
::::

:::: {.model-doc .migraphx .docutils .container}
For more information, please visit [[MIGraphX]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/AMDMIGraphX/en/latest/reference/MIGraphX-cpp.html "(in MIGraphX v2.15.0)"){.reference .external}.

::: pst-scrollable-table-container
+-------------------------------------------------+--------------------+
| Data Type                                       | Support            |
+=================================================+====================+
| int8                                            | ⚠️                 |
+-------------------------------------------------+--------------------+
| int16                                           | ✅                 |
+-------------------------------------------------+--------------------+
| int32                                           | ✅                 |
+-------------------------------------------------+--------------------+
| int64                                           | ✅                 |
+-------------------------------------------------+--------------------+
| float8 (E4M3)                                   | ✅                 |
+-------------------------------------------------+--------------------+
| float8 (E5M2)                                   | ✅                 |
+-------------------------------------------------+--------------------+
| float16                                         | ✅                 |
+-------------------------------------------------+--------------------+
| bfloat16                                        | ✅                 |
+-------------------------------------------------+--------------------+
| float32                                         | ✅                 |
+-------------------------------------------------+--------------------+
| float64                                         | ✅                 |
+-------------------------------------------------+--------------------+
:::
::::

:::: {.model-doc .miopen .docutils .container}
For more information, please visit [[MIOpen]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/MIOpen/en/latest/reference/datatypes.html "(in MIOpen Documentation v3.5.1)"){.reference .external}.

::: pst-scrollable-table-container
+-------------------------------------------------+--------------------+
| Data Type                                       | Support            |
+=================================================+====================+
| int8                                            | ⚠️                 |
+-------------------------------------------------+--------------------+
| int32                                           | ⚠️                 |
+-------------------------------------------------+--------------------+
| float8 (E4M3)                                   | ⚠️                 |
+-------------------------------------------------+--------------------+
| float8 (E5M2)                                   | ⚠️                 |
+-------------------------------------------------+--------------------+
| float16                                         | ✅                 |
+-------------------------------------------------+--------------------+
| bfloat16                                        | ⚠️                 |
+-------------------------------------------------+--------------------+
| float32                                         | ✅                 |
+-------------------------------------------------+--------------------+
| float64                                         | ⚠️                 |
+-------------------------------------------------+--------------------+
:::
::::

:::: {.model-doc .rccl .docutils .container}
For more information, please visit [[RCCL]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rccl/en/latest/api-reference/library-specification.html "(in RCCL Documentation v2.27.7)"){.reference .external}.

::: pst-scrollable-table-container
+-------------------------------------------------+--------------------+
| Data Type                                       | Support            |
+=================================================+====================+
| int8                                            | ✅                 |
+-------------------------------------------------+--------------------+
| int32                                           | ✅                 |
+-------------------------------------------------+--------------------+
| int64                                           | ✅                 |
+-------------------------------------------------+--------------------+
| float8 (E4M3)                                   | ✅                 |
+-------------------------------------------------+--------------------+
| float8 (E5M2)                                   | ✅                 |
+-------------------------------------------------+--------------------+
| float16                                         | ✅                 |
+-------------------------------------------------+--------------------+
| bfloat16                                        | ✅                 |
+-------------------------------------------------+--------------------+
| float32                                         | ✅                 |
+-------------------------------------------------+--------------------+
| float64                                         | ✅                 |
+-------------------------------------------------+--------------------+
:::
::::

:::: {.model-doc .hipblas .docutils .container}
For more information, please visit [[hipBLAS]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/hipBLAS/en/latest/reference/data-type-support.html "(in hipBLAS Documentation v3.2.0)"){.reference .external}.

::: pst-scrollable-table-container
+-------------------------------------------------+--------------------+
| Data Type                                       | Support            |
+=================================================+====================+
| float16                                         | ⚠️                 |
+-------------------------------------------------+--------------------+
| bfloat16                                        | ⚠️                 |
+-------------------------------------------------+--------------------+
| float32                                         | ✅                 |
+-------------------------------------------------+--------------------+
| float64                                         | ✅                 |
+-------------------------------------------------+--------------------+
:::
::::

:::: {.model-doc .hipblaslt .docutils .container}
For more information, please visit [[hipBLASLt]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/hipBLASLt/en/latest/reference/data-type-support.html "(in hipBLASLt Documentation v1.2.2)"){.reference .external}.

::: pst-scrollable-table-container
+-------------------------------------------------+--------------------+
| Data Type                                       | Support            |
+=================================================+====================+
| int8                                            | ✅                 |
+-------------------------------------------------+--------------------+
| float4                                          | ✅                 |
+-------------------------------------------------+--------------------+
| float6 (E2M3)                                   | ✅                 |
+-------------------------------------------------+--------------------+
| float6 (E3M2)                                   | ✅                 |
+-------------------------------------------------+--------------------+
| float8 (E4M3)                                   | ✅                 |
+-------------------------------------------------+--------------------+
| float8 (E5M2)                                   | ✅                 |
+-------------------------------------------------+--------------------+
| float16                                         | ✅                 |
+-------------------------------------------------+--------------------+
| bfloat16                                        | ✅                 |
+-------------------------------------------------+--------------------+
| float32                                         | ✅                 |
+-------------------------------------------------+--------------------+
:::
::::

:::: {.model-doc .hipfft .docutils .container}
For more information, please visit [hipFFT]{.xref .std .std-doc}.

::: pst-scrollable-table-container
+-------------------------------------------------+--------------------+
| Data Type                                       | Support            |
+=================================================+====================+
| float32                                         | ✅                 |
+-------------------------------------------------+--------------------+
| float64                                         | ✅                 |
+-------------------------------------------------+--------------------+
:::
::::

:::: {.model-doc .hiprand .docutils .container}
For more information, please visit [[hipRAND]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/hipRAND/en/latest/api-reference/data-type-support.html "(in hipRAND Documentation v3.1.0)"){.reference .external}.

::: pst-scrollable-table-container
+-------------------------------------------------+--------------------+
| Data Type                                       | Support            |
+=================================================+====================+
| int8                                            | Output only        |
+-------------------------------------------------+--------------------+
| int16                                           | Output only        |
+-------------------------------------------------+--------------------+
| int32                                           | Output only        |
+-------------------------------------------------+--------------------+
| int64                                           | Output only        |
+-------------------------------------------------+--------------------+
| float16                                         | Output only        |
+-------------------------------------------------+--------------------+
| float32                                         | Output only        |
+-------------------------------------------------+--------------------+
| float64                                         | Output only        |
+-------------------------------------------------+--------------------+
:::
::::

:::: {.model-doc .hipsolver .docutils .container}
For more information, please visit [[hipSOLVER]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/precision.html "(in hipSOLVER Documentation v3.2.0)"){.reference .external}.

::: pst-scrollable-table-container
+-------------------------------------------------+--------------------+
| Data Type                                       | Support            |
+=================================================+====================+
| float32                                         | ✅                 |
+-------------------------------------------------+--------------------+
| float64                                         | ✅                 |
+-------------------------------------------------+--------------------+
:::
::::

:::: {.model-doc .hipsparse .docutils .container}
For more information, please visit [[hipSPARSE]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/hipSPARSE/en/latest/reference/precision.html "(in hipSPARSE Documentation v4.2.0)"){.reference .external}.

::: pst-scrollable-table-container
+-------------------------------------------------+--------------------+
| Data Type                                       | Support            |
+=================================================+====================+
| float32                                         | ✅                 |
+-------------------------------------------------+--------------------+
| float64                                         | ✅                 |
+-------------------------------------------------+--------------------+
:::
::::

:::: {.model-doc .hipsparselt .docutils .container}
For more information, please visit [[hipSPARSELt]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/hipSPARSELt/en/latest/reference/data-type-support.html "(in hipSPARSELt Documentation v0.2.6)"){.reference .external}.

::: pst-scrollable-table-container
+-------------------------------------------------+--------------------+
| Data Type                                       | Support            |
+=================================================+====================+
| int8                                            | ✅                 |
+-------------------------------------------------+--------------------+
| float8 (E4M3)                                   | ✅                 |
+-------------------------------------------------+--------------------+
| float8 (E5M2)                                   | ✅                 |
+-------------------------------------------------+--------------------+
| float16                                         | ✅                 |
+-------------------------------------------------+--------------------+
| bfloat16                                        | ✅                 |
+-------------------------------------------------+--------------------+
| float32                                         | ✅                 |
+-------------------------------------------------+--------------------+
:::
::::

:::: {.model-doc .rocblas .docutils .container}
For more information, please visit [[rocBLAS]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/data-type-support.html "(in rocBLAS Documentation v5.2.0)"){.reference .external}.

::: pst-scrollable-table-container
+-------------------------------------------------+--------------------+
| Data Type                                       | Support            |
+=================================================+====================+
| float16                                         | ⚠️                 |
+-------------------------------------------------+--------------------+
| bfloat16                                        | ⚠️                 |
+-------------------------------------------------+--------------------+
| float32                                         | ✅                 |
+-------------------------------------------------+--------------------+
| float64                                         | ✅                 |
+-------------------------------------------------+--------------------+
:::
::::

:::: {.model-doc .rocfft .docutils .container}
For more information, please visit [[rocFFT]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocFFT/en/latest/reference/api.html "(in rocFFT Documentation v1.0.36)"){.reference .external}.

::: pst-scrollable-table-container
+-------------------------------------------------+--------------------+
| Data Type                                       | Support            |
+=================================================+====================+
| float16                                         | ✅                 |
+-------------------------------------------------+--------------------+
| float32                                         | ✅                 |
+-------------------------------------------------+--------------------+
| float64                                         | ✅                 |
+-------------------------------------------------+--------------------+
:::
::::

:::: {.model-doc .rocrand .docutils .container}
For more information, please visit [[rocRAND]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocRAND/en/latest/api-reference/data-type-support.html "(in rocRAND Documentation v4.2.0)"){.reference .external}.

::: pst-scrollable-table-container
+-------------------------------------------------+--------------------+
| Data Type                                       | Support            |
+=================================================+====================+
| int8                                            | Output only        |
+-------------------------------------------------+--------------------+
| int16                                           | Output only        |
+-------------------------------------------------+--------------------+
| int32                                           | Output only        |
+-------------------------------------------------+--------------------+
| int64                                           | Output only        |
+-------------------------------------------------+--------------------+
| float16                                         | Output only        |
+-------------------------------------------------+--------------------+
| float32                                         | Output only        |
+-------------------------------------------------+--------------------+
| float64                                         | Output only        |
+-------------------------------------------------+--------------------+
:::
::::

:::: {.model-doc .rocsolver .docutils .container}
For more information, please visit [[rocSOLVER]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocSOLVER/en/latest/reference/precision.html "(in rocSOLVER Documentation v3.32.0)"){.reference .external}.

::: pst-scrollable-table-container
+-------------------------------------------------+--------------------+
| Data Type                                       | Support            |
+=================================================+====================+
| float32                                         | ✅                 |
+-------------------------------------------------+--------------------+
| float64                                         | ✅                 |
+-------------------------------------------------+--------------------+
:::
::::

:::: {.model-doc .rocsparse .docutils .container}
For more information, please visit [[rocSPARSE]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocSPARSE/en/latest/reference/precision.html "(in rocSPARSE Documentation v4.2.0)"){.reference .external}.

::: pst-scrollable-table-container
+-------------------------------------------------+--------------------+
| Data Type                                       | Support            |
+=================================================+====================+
| float32                                         | ✅                 |
+-------------------------------------------------+--------------------+
| float64                                         | ✅                 |
+-------------------------------------------------+--------------------+
:::
::::

:::: {.model-doc .rocwmma .docutils .container}
For more information, please visit [[rocWMMA]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocWMMA/en/latest/api-reference/api-reference-guide.html "(in rocWMMA Documentation v2.2.0)"){.reference .external}.

::: pst-scrollable-table-container
+-------------------------------------------------+--------------------+
| Data Type                                       | Support            |
+=================================================+====================+
| int8                                            | ✅                 |
+-------------------------------------------------+--------------------+
| int32                                           | Output only        |
+-------------------------------------------------+--------------------+
| float8 (E4M3)                                   | Input only         |
+-------------------------------------------------+--------------------+
| float8 (E5M2)                                   | Input only         |
+-------------------------------------------------+--------------------+
| float16                                         | ✅                 |
+-------------------------------------------------+--------------------+
| bfloat16                                        | ✅                 |
+-------------------------------------------------+--------------------+
| tensorfloat32                                   | ✅                 |
+-------------------------------------------------+--------------------+
| float32                                         | ✅                 |
+-------------------------------------------------+--------------------+
| float64                                         | ✅                 |
+-------------------------------------------------+--------------------+
:::
::::

:::: {.model-doc .tensile .docutils .container}
For more information, please visit [[Tensile]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/Tensile/en/latest/src/reference/precision-support.html "(in Tensile Documentation v4.45.0)"){.reference .external}.

::: pst-scrollable-table-container
+-------------------------------------------------+--------------------+
| Data Type                                       | Support            |
+=================================================+====================+
| int8                                            | ✅                 |
+-------------------------------------------------+--------------------+
| int32                                           | ✅                 |
+-------------------------------------------------+--------------------+
| float8 (E4M3)                                   | ✅                 |
+-------------------------------------------------+--------------------+
| float8 (E5M2)                                   | ✅                 |
+-------------------------------------------------+--------------------+
| float16                                         | ✅                 |
+-------------------------------------------------+--------------------+
| bfloat16                                        | ✅                 |
+-------------------------------------------------+--------------------+
| tensorfloat32                                   | ✅                 |
+-------------------------------------------------+--------------------+
| float32                                         | ✅                 |
+-------------------------------------------------+--------------------+
| float64                                         | ✅                 |
+-------------------------------------------------+--------------------+
:::
::::

:::: {.model-doc .hipcub .docutils .container}
For more information, please visit [hipCUB]{.xref .std .std-doc}.

::: pst-scrollable-table-container
+-------------------------------------------------+--------------------+
| Data Type                                       | Support            |
+=================================================+====================+
| int8                                            | ✅                 |
+-------------------------------------------------+--------------------+
| int16                                           | ✅                 |
+-------------------------------------------------+--------------------+
| int32                                           | ✅                 |
+-------------------------------------------------+--------------------+
| int64                                           | ✅                 |
+-------------------------------------------------+--------------------+
| float16                                         | ✅                 |
+-------------------------------------------------+--------------------+
| bfloat16                                        | ✅                 |
+-------------------------------------------------+--------------------+
| float32                                         | ✅                 |
+-------------------------------------------------+--------------------+
| float64                                         | ✅                 |
+-------------------------------------------------+--------------------+
:::
::::

:::: {.model-doc .hiptensor .docutils .container}
For more information, please visit [[hipTensor]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/hipTensor/en/latest/api-reference/api-reference.html "(in hipTensor Documentation v2.2.0)"){.reference .external}.

::: pst-scrollable-table-container
+-------------------------------------------------+--------------------+
| Data Type                                       | Support            |
+=================================================+====================+
| float16                                         | ✅                 |
+-------------------------------------------------+--------------------+
| bfloat16                                        | ✅                 |
+-------------------------------------------------+--------------------+
| float32                                         | ✅                 |
+-------------------------------------------------+--------------------+
| float64                                         | ✅                 |
+-------------------------------------------------+--------------------+
:::
::::

:::: {.model-doc .rocprim .docutils .container}
For more information, please visit [[rocPRIM]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocPRIM/en/latest/reference/data-type-support.html "(in rocPRIM Documentation v4.2.0)"){.reference .external}.

::: pst-scrollable-table-container
+-------------------------------------------------+--------------------+
| Data Type                                       | Support            |
+=================================================+====================+
| int8                                            | ✅                 |
+-------------------------------------------------+--------------------+
| int16                                           | ✅                 |
+-------------------------------------------------+--------------------+
| int32                                           | ✅                 |
+-------------------------------------------------+--------------------+
| int64                                           | ✅                 |
+-------------------------------------------------+--------------------+
| float16                                         | ✅                 |
+-------------------------------------------------+--------------------+
| bfloat16                                        | ✅                 |
+-------------------------------------------------+--------------------+
| float32                                         | ✅                 |
+-------------------------------------------------+--------------------+
| float64                                         | ✅                 |
+-------------------------------------------------+--------------------+
:::
::::

:::: {.model-doc .rocthrust .docutils .container}
For more information, please visit [rocThrust]{.xref .std .std-doc}.

::: pst-scrollable-table-container
+-------------------------------------------------+--------------------+
| Data Type                                       | Support            |
+=================================================+====================+
| int8                                            | ✅                 |
+-------------------------------------------------+--------------------+
| int16                                           | ✅                 |
+-------------------------------------------------+--------------------+
| int32                                           | ✅                 |
+-------------------------------------------------+--------------------+
| int64                                           | ✅                 |
+-------------------------------------------------+--------------------+
| float16                                         | ⚠️                 |
+-------------------------------------------------+--------------------+
| bfloat16                                        | ⚠️                 |
+-------------------------------------------------+--------------------+
| float32                                         | ✅                 |
+-------------------------------------------------+--------------------+
| float64                                         | ✅                 |
+-------------------------------------------------+--------------------+
:::
::::

::: {.admonition .note}
Note

The meaning of partial support depends on the library. Please refer to the individual libraries' documentation for more information.
:::

::: {.admonition .note}
Note

As random number generation libraries, rocRAND and hipRAND only specify output data types for the random values they generate, with no need for input data types.
:::

::: {.admonition .note}
Note

hipBLASLt supports additional data types as internal compute types, which may differ from the supported input/output types shown in the tables above. While TensorFloat32 is not supported as an input or output type in this library, it is available as an internal compute type. For complete details on supported compute types, refer to the [[hipBLASLt]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/hipBLASLt/en/latest/reference/data-type-support.html "(in hipBLASLt Documentation v1.2.2)"){.reference .external} documentation.
:::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::: {#hipdatatype-enumeration .section}
### hipDataType enumeration[\#](#hipdatatype-enumeration "Link to this heading"){.headerlink}

The [`hipDataType`{.docutils .literal .notranslate}]{.pre} enumeration defines data precision types and is primarily used when the data reference itself does not include type information, such as in [`void*`{.docutils .literal .notranslate}]{.pre} pointers. This enumeration is mainly utilized in BLAS libraries. The HIP type equivalents of the [`hipDataType`{.docutils .literal .notranslate}]{.pre} enumeration are listed in the following table with descriptions and values.

::: pst-scrollable-table-container
+---------------------------------------------------------------+----------------------------------------------------------------+-------+-------------------------------------------------------------+
| hipDataType                                                   | HIP type                                                       | Value | Description                                                 |
+===============================================================+================================================================+=======+=============================================================+
| [`HIP_R_8I`{.docutils .literal .notranslate}]{.pre}           | [`int8_t`{.docutils .literal .notranslate}]{.pre}              | 3     | 8-bit real signed integer.                                  |
+---------------------------------------------------------------+----------------------------------------------------------------+-------+-------------------------------------------------------------+
| [`HIP_R_8U`{.docutils .literal .notranslate}]{.pre}           | [`uint8_t`{.docutils .literal .notranslate}]{.pre}             | 8     | 8-bit real unsigned integer.                                |
+---------------------------------------------------------------+----------------------------------------------------------------+-------+-------------------------------------------------------------+
| [`HIP_R_16I`{.docutils .literal .notranslate}]{.pre}          | [`int16_t`{.docutils .literal .notranslate}]{.pre}             | 20    | 16-bit real signed integer.                                 |
+---------------------------------------------------------------+----------------------------------------------------------------+-------+-------------------------------------------------------------+
| [`HIP_R_16U`{.docutils .literal .notranslate}]{.pre}          | [`uint16_t`{.docutils .literal .notranslate}]{.pre}            | 22    | 16-bit real unsigned integer.                               |
+---------------------------------------------------------------+----------------------------------------------------------------+-------+-------------------------------------------------------------+
| [`HIP_R_32I`{.docutils .literal .notranslate}]{.pre}          | [`int32_t`{.docutils .literal .notranslate}]{.pre}             | 10    | 32-bit real signed integer.                                 |
+---------------------------------------------------------------+----------------------------------------------------------------+-------+-------------------------------------------------------------+
| [`HIP_R_32U`{.docutils .literal .notranslate}]{.pre}          | [`uint32_t`{.docutils .literal .notranslate}]{.pre}            | 12    | 32-bit real unsigned integer.                               |
+---------------------------------------------------------------+----------------------------------------------------------------+-------+-------------------------------------------------------------+
| [`HIP_R_32F`{.docutils .literal .notranslate}]{.pre}          | [`float`{.docutils .literal .notranslate}]{.pre}               | 0     | 32-bit real single precision floating-point.                |
+---------------------------------------------------------------+----------------------------------------------------------------+-------+-------------------------------------------------------------+
| [`HIP_R_64F`{.docutils .literal .notranslate}]{.pre}          | [`double`{.docutils .literal .notranslate}]{.pre}              | 1     | 64-bit real double precision floating-point.                |
+---------------------------------------------------------------+----------------------------------------------------------------+-------+-------------------------------------------------------------+
| [`HIP_R_16F`{.docutils .literal .notranslate}]{.pre}          | [`half`{.docutils .literal .notranslate}]{.pre}                | 2     | 16-bit real half precision floating-point.                  |
+---------------------------------------------------------------+----------------------------------------------------------------+-------+-------------------------------------------------------------+
| [`HIP_R_16BF`{.docutils .literal .notranslate}]{.pre}         | [`bfloat16`{.docutils .literal .notranslate}]{.pre}            | 14    | 16-bit real bfloat16 precision floating-point.              |
+---------------------------------------------------------------+----------------------------------------------------------------+-------+-------------------------------------------------------------+
| [`HIP_R_8F_E4M3`{.docutils .literal .notranslate}]{.pre}      | [`__hip_fp8_e4m3`{.docutils .literal .notranslate}]{.pre}      | 28    | 8-bit real float8 precision floating-point (OCP version).   |
+---------------------------------------------------------------+----------------------------------------------------------------+-------+-------------------------------------------------------------+
| [`HIP_R_8F_E5M2`{.docutils .literal .notranslate}]{.pre}      | [`__hip_fp8_e5m2`{.docutils .literal .notranslate}]{.pre}      | 29    | 8-bit real bfloat8 precision floating-point (OCP version).  |
+---------------------------------------------------------------+----------------------------------------------------------------+-------+-------------------------------------------------------------+
| [`HIP_R_6F_E2M3`{.docutils .literal .notranslate}]{.pre}      | [`__hip_fp6_e2m3`{.docutils .literal .notranslate}]{.pre}      | 31    | 6-bit real float6 precision floating-point.                 |
+---------------------------------------------------------------+----------------------------------------------------------------+-------+-------------------------------------------------------------+
| [`HIP_R_6F_E3M2`{.docutils .literal .notranslate}]{.pre}      | [`__hip_fp6_e3m2`{.docutils .literal .notranslate}]{.pre}      | 32    | 6-bit real bfloat6 precision floating-point.                |
+---------------------------------------------------------------+----------------------------------------------------------------+-------+-------------------------------------------------------------+
| [`HIP_R_4F_E2M1`{.docutils .literal .notranslate}]{.pre}      | [`__hip_fp4_e2m1`{.docutils .literal .notranslate}]{.pre}      | 33    | 4-bit real float4 precision floating-point.                 |
+---------------------------------------------------------------+----------------------------------------------------------------+-------+-------------------------------------------------------------+
| [`HIP_R_8F_E4M3_FNUZ`{.docutils .literal .notranslate}]{.pre} | [`__hip_fp8_e4m3_fnuz`{.docutils .literal .notranslate}]{.pre} | 1000  | 8-bit real float8 precision floating-point (FNUZ version).  |
+---------------------------------------------------------------+----------------------------------------------------------------+-------+-------------------------------------------------------------+
| [`HIP_R_8F_E5M2_FNUZ`{.docutils .literal .notranslate}]{.pre} | [`__hip_fp8_e5m2_fnuz`{.docutils .literal .notranslate}]{.pre} | 1001  | 8-bit real bfloat8 precision floating-point (FNUZ version). |
+---------------------------------------------------------------+----------------------------------------------------------------+-------+-------------------------------------------------------------+
:::

The full list of the [`hipDataType`{.docutils .literal .notranslate}]{.pre} enumeration listed in [library_types.h](https://github.com/ROCm/hip/blob/amd-staging/include/hip/library_types.h){.reference .external}.
::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::: prev-next-area
[](env-variables.html "previous page"){.left-prev}

::: prev-next-info
previous

ROCm environment variables
:::

[](graph-safe-support.html "next page"){.right-next}

::: prev-next-info
next

Graph-safe support for ROCm libraries
:::
:::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::: {.bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {.page-toc .tocsection .onthispage}
Contents
:::

- [Integral types](#integral-types){.reference .internal .nav-link}
- [Floating-point types](#floating-point-types){.reference .internal .nav-link}
- [Level of support definitions](#level-of-support-definitions){.reference .internal .nav-link}
- [Data type support by hardware architecture](#data-type-support-by-hardware-architecture){.reference .internal .nav-link}
  - [HIP C++ type implementation support](#hip-c-type-implementation-support){.reference .internal .nav-link}
  - [Compute units support](#compute-units-support){.reference .internal .nav-link}
  - [Matrix core support](#matrix-core-support){.reference .internal .nav-link}
  - [Atomic operations support](#atomic-operations-support){.reference .internal .nav-link}
- [Data type support in ROCm libraries](#data-type-support-in-rocm-libraries){.reference .internal .nav-link}
  - [Libraries input/output type support](#libraries-input-output-type-support){.reference .internal .nav-link}
  - [hipDataType enumeration](#hipdatatype-enumeration){.reference .internal .nav-link}
::::
:::::
::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
