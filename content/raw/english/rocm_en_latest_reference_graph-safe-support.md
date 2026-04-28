---
title: "Graph-safe support for ROCm libraries"
source_url: "https://rocm.docs.amd.com/en/latest/reference/graph-safe-support.html"
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
- Graph-safe\...

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons

# Graph-safe support for ROCm libraries



# Graph-safe support for ROCm libraries[\#](#graph-safe-support-for-rocm-libraries "Link to this heading"){.headerlink}

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 3 min read time

Applies to Linux and Windows


HIP graph-safe libraries operate safely in HIP execution graphs. [HIP graphs](https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_runtime_api/hipgraph.html#how-to-hip-graph "(in HIP Documentation v7.2.53211)"){.reference .external} are an alternative way of executing tasks on a GPU that can provide performance benefits over launching kernels using the standard method via streams.

Functions and routines from graph-safe libraries shouldn't result in issues like race conditions, deadlocks, or unintended dependencies.

The following table shows whether a ROCm library is graph-safe.

::: pst-scrollable-table-container
  ROCm library                                                                           Graph safe support
  -------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [Composable Kernel](https://github.com/ROCm/composable_kernel){.reference .external}   ❌
  [hipBLAS](https://github.com/ROCm/hipBLAS){.reference .external}                       ✅
  [hipBLASLt](https://github.com/ROCm/hipBLASLt){.reference .external}                   ⚠️
  [hipCUB](https://github.com/ROCm/hipCUB){.reference .external}                         ✅
  [hipFFT](https://github.com/ROCm/hipFFT){.reference .external}                         ✅ (see [[details]{.xref .std .std-ref}](https://rocm.docs.amd.com/projects/hipFFT/en/latest/reference/hipfft-api-usage.html#hip-graph-support-for-hipfft "(in hipFFT Documentation v1.0.22)"){.reference .external})
  [hipRAND](https://github.com/ROCm/hipRAND){.reference .external}                       ✅
  [hipSOLVER](https://github.com/ROCm/hipSOLVER){.reference .external}                   ⚠️ (experimental)
  [hipSPARSE](https://github.com/ROCm/hipSPARSE){.reference .external}                   ✅
  [hipSPARSELt](https://github.com/ROCm/hipSPARSELt){.reference .external}               ⚠️ (experimental)
  [hipTensor](https://github.com/ROCm/hipTensor){.reference .external}                   ❌
  [MIOpen](https://github.com/ROCm/MIOpen){.reference .external}                         ❌
  [RCCL](https://github.com/ROCm/rccl){.reference .external}                             ✅
  [rocAL](https://github.com/ROCm/rocAL){.reference .external}                           ❌
  [rocALUTION](https://github.com/ROCm/rocALUTION){.reference .external}                 ❌
  [rocBLAS](https://github.com/ROCm/rocBLAS){.reference .external}                       ✅ (see [[details]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/beta-features.html "(in rocBLAS Documentation v5.2.0)"){.reference .external})
  [rocDecode](https://github.com/ROCm/rocDecode){.reference .external}                   ❌
  [rocFFT](https://github.com/ROCm/rocFFT){.reference .external}                         ✅ (see [[details]{.xref .std .std-ref}](https://rocm.docs.amd.com/projects/rocFFT/en/latest/reference/api.html#hip-graph-support-for-rocfft "(in rocFFT Documentation v1.0.36)"){.reference .external})
  [rocHPCG](https://github.com/ROCm/rocHPCG){.reference .external}                       ❌
  [rocJPEG](https://github.com/ROCm/rocJPEG){.reference .external}                       ❌
  [rocPRIM](https://github.com/ROCm/rocPRIM){.reference .external}                       ✅
  [rocRAND](https://github.com/ROCm/rocRAND){.reference .external}                       ✅
  [rocSOLVER](https://github.com/ROCm/rocSOLVER){.reference .external}                   ⚠️ (experimental)
  [rocSPARSE](https://github.com/ROCm/rocSPARSE){.reference .external}                   ⚠️ (experimental)
  [rocThrust](https://github.com/ROCm/rocThrust){.reference .external}                   ❌
  [rocWMMA](https://github.com/ROCm/rocWMMA){.reference .external}                       ❌
  [RPP](https://github.com/ROCm/rpp){.reference .external}                               ⚠️
  [Tensile](https://github.com/ROCm/Tensile){.reference .external}                       ✅

✅: full support

⚠️: partial support

❌: not supported

::::: prev-next-area
[](precision-support.html "previous page"){.left-prev}

::: prev-next-info
previous

Data types and precision support

[](glossary.html "next page"){.right-next}

::: prev-next-info
next

ROCm glossary
