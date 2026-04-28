---
title: "Supported CUDA APIs"
source_url: "https://rocm.docs.amd.com/projects/HIPIFY/en/latest/supported_apis.html"
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
- [Supported CUDA APIs]{.ellipsis}

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons

# Supported CUDA APIs



# Supported CUDA APIs[\#](#supported-cuda-apis "Link to this heading"){.headerlink}

::: pst-scrollable-table-container
  **CUDA**           **HIP**                                                                                                     **ROC**                                                                                              **HIP & ROC**
  ------------------ ----------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------
  CUDA Runtime API   [[HIP API]{.std .std-doc}](tables/CUDA_Runtime_API_functions_supported_by_HIP.html){.reference .internal}                                                                                                        
  CUDA Driver API    [[HIP API]{.std .std-doc}](tables/CUDA_Driver_API_functions_supported_by_HIP.html){.reference .internal}                                                                                                         
  CUComplex API      [[HIP API]{.std .std-doc}](tables/cuComplex_API_supported_by_HIP.html){.reference .internal}                                                                                                                     
  CUDA Device API    [[HIP Device API]{.std .std-doc}](tables/CUDA_Device_API_supported_by_HIP.html){.reference .internal}                                                                                                            
  CUDA RTC API       [[HIP RTC API]{.std .std-doc}](tables/CUDA_RTC_API_supported_by_HIP.html){.reference .internal}                                                                                                                  
  CUBLAS API         [[HIP BLAS API]{.std .std-doc}](tables/CUBLAS_API_supported_by_HIP.html){.reference .internal}              [[ROC BLAS API]{.std .std-doc}](tables/CUBLAS_API_supported_by_ROC.html){.reference .internal}       [[HIP + ROC BLAS API]{.std .std-doc}](tables/CUBLAS_API_supported_by_HIP_and_ROC.html){.reference .internal}
  CUSPARSE API       [[HIP SPARSE API]{.std .std-doc}](tables/CUSPARSE_API_supported_by_HIP.html){.reference .internal}          [[ROC SPARSE API]{.std .std-doc}](tables/CUSPARSE_API_supported_by_ROC.html){.reference .internal}   [[HIP + ROC SPARSE API]{.std .std-doc}](tables/CUSPARSE_API_supported_by_HIP_and_ROC.html){.reference .internal}
  CUSOLVER API       [[HIP SOLVER API]{.std .std-doc}](tables/CUSOLVER_API_supported_by_HIP.html){.reference .internal}                                                                                                               
  CURAND API         [[HIP RAND API]{.std .std-doc}](tables/CURAND_API_supported_by_HIP.html){.reference .internal}              [[ROC RAND API]{.std .std-doc}](tables/CURAND_API_supported_by_ROC.html){.reference .internal}       [[HIP + ROC RAND API]{.std .std-doc}](tables/CURAND_API_supported_by_HIP_and_ROC.html){.reference .internal}
  CUFFT API          [[HIP FFT API]{.std .std-doc}](tables/CUFFT_API_supported_by_HIP.html){.reference .internal}                                                                                                                     
  CUDNN API                                                                                                                      [[MIOPEN API]{.std .std-doc}](tables/CUDNN_API_supported_by_MIOPEN.html){.reference .internal}       
  CUTENSOR API       [[HIP TENSOR API]{.std .std-doc}](tables/CUTENSOR_API_supported_by_HIP.html){.reference .internal}                                                                                                               
  CUB API            [[HIP CUB API]{.std .std-doc}](tables/CUB_API_supported_by_HIP.html){.reference .internal}                                                                                                                       

To generate the above documentation with the information about all supported CUDA APIs in Markdown format, run [`hipify-clang`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--md`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--doc-format=full`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--doc-roc=joint`{.docutils .literal .notranslate}]{.pre} with or without specifying the output directory ([`-o`{.docutils .literal .notranslate}]{.pre}). By running [`hipify-clang`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--csv`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--doc-format=full`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--doc-roc=joint`{.docutils .literal .notranslate}]{.pre}, the documentation will be generated in CSV format.

::::: prev-next-area
[](hipify-perl-cmd.html "previous page"){.left-prev}

::: prev-next-info
previous

hipify-perl commands

[](hip_supported_apis.html "next page"){.right-next}

::: prev-next-info
next

CUDA APIs supported by HIP
