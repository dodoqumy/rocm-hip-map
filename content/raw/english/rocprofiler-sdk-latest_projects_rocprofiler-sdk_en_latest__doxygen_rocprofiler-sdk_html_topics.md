---
title: "ROCprofiler-SDK developer API: Topics &#8212; ROCprofiler-SDK 1.1.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/_doxygen/rocprofiler-sdk/html/topics.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:24:48.213312+00:00
content_hash: "5bf191385658bf33"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../../../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />

    <title>ROCprofiler-SDK developer API: Topics &#8212; ROCprofiler-SDK 1.1.0 Documentation</title>
  
  
  
  <script data-cfasync="false">
    document.documentElement.dataset.mode = localStorage.getItem("mode") || "";
    document.documentElement.dataset.theme = localStorage.getItem("theme") || "";
  </script>
  
  <!-- Loaded before other Sphinx assets -->
  <link href="../../../_static/styles/theme.css?digest=dfe6caa3a7d634c4db9b" rel="stylesheet" />
<link href="../../../_static/styles/bootstrap.css?digest=dfe6caa3a7d634c4db9b" rel="stylesheet" />
<link href="../../../_static/styles/pydata-sphinx-theme.css?digest=dfe6caa3a7d634c4db9b" rel="stylesheet" />

  
  <link href="../../../_static/vendor/fontawesome/6.5.2/css/all.min.css?digest=dfe6caa3a7d634c4db9b" rel="stylesheet" />
  <link rel="preload" as="font" type="font/woff2" crossorigin href="../../../_static/vendor/fontawesome/6.5.2/webfonts/fa-solid-900.woff2" />
<link rel="preload" as="font" type="font/woff2" crossorigin href="../../../_static/vendor/fontawesome/6.5.2/webfonts/fa-brands-400.woff2" />
<link rel="preload" as="font" type="font/woff2" crossorigin href="../../../_static/vendor/fontawesome/6.5.2/webfonts/fa-regular-400.woff2" />

    <link rel="stylesheet" type="text/css" href="../../../_static/pygments.css?v=8f2a1f02" />
    <link rel="stylesheet" type="text/css" href="../../../_static/styles/sphinx-book-theme.css?v=eba8b062" />
    <link rel="stylesheet" type="text/css" href="../../../_static/mystnb.11b39860a7a0cbfd473a3ad8a317855267ff0bd372690045ca344a6b62be495e.css" />
    <link rel="stylesheet" type="text/css" href="../../../_static/copybutton.css?v=76b2166b" />
    <link rel="stylesheet" type="text/css" href="../../../_static/custom.css?v=24396f60" />
    <link rel="stylesheet" type="text/css" href="../../../_static/rocm_header.css?v=fd5d9836" />
    <link rel="stylesheet" type="text/css" href="../../../_static/rocm_footer.css?v=7095035a" />
    <link rel="stylesheet" type="text/css" href="../../../_static/fonts.css?v=fcff5274" />
    <link rel="stylesheet" type="text/css" href="../../../_static/sphinx-design.min.css?v=95c83b7e" />
  
  <!-- Pre-loaded scripts that we'll load fully later -->
  <link rel="preload" as="script" href="../../../_static/scripts/bootstrap.js?digest=dfe6caa3a7d634c4db9b" />
<link rel="preload" as="script" href="../../../_static/scripts/pydata-sphinx-theme.js?digest=dfe6caa3a7d634c4db9b" />
  <script src="../../../_static/vendor/fontawesome/6.5.2/js/all.min.js?digest=dfe6caa3a7d634c4db9b"></script>

    <script src="../../../_static/documentation_options.js?v=051bfb12"></script>
    <script src="../../../_static/doctools.js?v=9bcbadda"></script>
    <script src="../../../_static/sphinx_highlight.js?v=dc90522c"></script>
    <script src="../../../_static/clipboard.min.js?v=a7894cd8"></script>
    <script src="../../../_static/copybutton.js?v=91c4cb68"></script>
    <script async="async" src="../../../_static/code_word_breaks.js?v=327952c4"></script>
    <script async="async" src="../../../_static/renameVersionLinks.js?v=929fe5e4"></script>
    <script async="async" src="../../../_static/rdcMisc.js?v=01f88d96"></script>
    <script async="async" src="../../../_static/theme_mode_captions.js?v=15f4ec5d"></script>
    <script defer="defer" src="../../../_static/search.js?v=90a4452c"></script>
    <script src="../../../_static/scripts/sphinx-book-theme.js?v=887ef09a"></script>
    <script src="../../../_static/design-tabs.js?v=f930bc37"></script>
    <script>DOCUMENTATION_OPTIONS.pagename = '_doxygen/rocprofiler-sdk/html/topics';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../../../genindex.html" />
    <link rel="search" title="Search" href="../../../search.html" />
    <link rel="next" title="Data Structures" href="annotated.html" />
    <link rel="prev" title="Global Basic Data Types" href="../../../api-reference/rocprofiler-sdk_api/global_data_structures_topics_files/global_basic_data_types.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-rocprofiler-sdk" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/_doxygen/rocprofiler-sdk/html/topics.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
  <body data-bs-spy="scroll" data-bs-target=".bd-toc-nav" data-offset="180" data-bs-root-margin="0px 0px -60%" data-default-mode="">

  
  
  <div id="pst-skip-link" class="skip-link d-print-none"><a href="#main-content">Skip to main content</a></div>
  
  <div id="pst-scroll-pixel-helper"></div>
  
  <button type="button" class="btn rounded-pill" id="pst-back-to-top">
    <i class="fa-solid fa-arrow-up"></i>Back to top</button>

  
  <input type="checkbox"
          class="sidebar-toggle"
          id="pst-primary-sidebar-checkbox"/>
  <label class="overlay overlay-primary" for="pst-primary-sidebar-checkbox"></label>
  
  <input type="checkbox"
          class="sidebar-toggle"
          id="pst-secondary-sidebar-checkbox"/>
  <label class="overlay overlay-secondary" for="pst-secondary-sidebar-checkbox"></label>
  
  <div class="search-button__wrapper">
    <div class="search-button__overlay"></div>
    <div class="search-button__search-container">
<form class="bd-search d-flex align-items-center"
      action="../../../search.html"
      method="get">
  <i class="fa-solid fa-magnifying-glass"></i>
  <input type="search"
         class="form-control"
         name="q"
         id="search-input"
         placeholder="Search..."
         aria-label="Search..."
         autocomplete="off"
         autocorrect="off"
         autocapitalize="off"
         spellcheck="false"/>
  <span class="search-button__kbd-shortcut"><kbd class="kbd-shortcut__modifier">Ctrl</kbd>+<kbd>K</kbd></span>
</form></div>
  </div>

  <div class="pst-async-banner-revealer d-none">
  <aside id="bd-header-version-warning" class="d-none d-print-none" aria-label="Version warning"></aside>
</div>
<aside class="bd-header-announcement" aria-label="Announcement">
  <div class="bd-header-announcement__content">The ROCm 7.12.0 technology preview release documentation is available at <a id='rocm-banner' href='https://rocm.docs.amd.com/en/7.12.0-preview/'>ROCm Preview documentation</a>. For production use, continue to use ROCm 7.2.2 documentation.</div>
</aside>

  

<header class="common-header" >
    <nav class="navbar navbar-expand-xl">
        <div class="container-fluid main-nav rocm-header">
            <div class="header-logo">
                <div class="header-logo-title">
                    
                        <button class="navbar-toggler collapsed" id="nav-icon" data-tracking-information="mainMenuToggle" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                            <span></span>
                            <span></span>
                            <span></span>
                        </button>
                    
                    <a class="navbar-brand" href="https://www.amd.com/">
                        <img src="../../../_static/images/amd-header-logo.svg" alt="AMD Logo" title="AMD Logo" width="90" class="d-inline-block align-text-top hover-opacity"/>
                    </a>
                    <div class="vr mx-40 my-25"></div>
                    
        
    
    <a class="klavika-font hover-opacity" href="https://rocm.docs.amd.com/en/latest">ROCm&#8482; Software 7.2.2</a>
                </div>
                <a class="header-all-versions hover-opacity" href="https://rocm.docs.amd.com/en/latest/release/versions.html">Version List</a>
            </div>
            <div class="icon-nav text-center d-flex ms-auto"></div>
        </div>
    </nav>
    
    <nav class="navbar navbar-expand-xl second-level-nav">
        <div class="container-fluid main-nav">
            <div class="navbar-nav-container collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav nav-mega me-auto mb-2 mb-lg-0 col-xl-10">
                    
                        <li class="nav-item">
                            <a class="nav-link top-level header-menu-links" href="https://github.com/ROCm/rocm-systems" id="navgithub" role="button" aria-expanded="false" target="_blank" >
                                GitHub
                            </a>
                        </li>
                    
                        <li class="nav-item">
                            <a class="nav-link top-level header-menu-links" href="https://github.com/ROCm/ROCm/discussions" id="navcommunity" role="button" aria-expanded="false" target="_blank" >
                                Community
                            </a>
                        </li>
                    
                        <li class="nav-item">
                            <a class="nav-link top-level header-menu-links" href="https://rocm.blogs.amd.com/" id="navblogs" role="button" aria-expanded="false" target="_blank" >
                                Blogs
                            </a>
                        </li>
                    
                        <li class="nav-item">
                            <a class="nav-link top-level header-menu-links" href="https://www.amd.com/en/developer/resources/rocm-hub.html" id="navrocm-developer-hub" role="button" aria-expanded="false" target="_blank" >
                                ROCm Developer Hub
                            </a>
                        </li>
                    
                        <li class="nav-item">
                            <a class="nav-link top-level header-menu-links" href="https://instinct.docs.amd.com" id="navsystems-and-infra-docs" role="button" aria-expanded="false" target="_blank" >
                                Systems and Infra Docs
                            </a>
                        </li>
                    
                        <li class="nav-item">
                            <a class="nav-link top-level header-menu-links" href="https://www.amd.com/en/developer/resources/infinity-hub.html" id="navinfinity-hub" role="button" aria-expanded="false" target="_blank" >
                                Infinity Hub
                            </a>
                        </li>
                    
                        <li class="nav-item">
                            <a class="nav-link top-level header-menu-links" href="https://github.com/ROCm/rocm-systems/issues/new/choose" id="navsupport" role="button" aria-expanded="false" target="_blank" >
                                Support
                            </a>
                        </li>
                    
                </ul>
            </div>
        </div>
    </nav>
    
</header>


  <div class="bd-container">
    <div class="bd-container__inner bd-page-width">
      
      
      
      <div class="bd-sidebar-primary bd-sidebar">
        

  
  <div class="sidebar-header-items sidebar-primary__section">
    
    
      <div class="sidebar-header-items__center">
        
          
          
            <div class="navbar-item">

<a class="navbar-brand logo" href="https://rocm.docs.amd.com/en/latest">
    <p>ROCm documentation</p>
</a></div>
          
        
      </div>
    
    
    
  </div>
  
    <div class="sidebar-primary-items__start sidebar-primary__section">
        <div class="sidebar-primary-item">

  
    
  

<a class="navbar-brand logo" href="../../../index.html">
  
  
  
  
  
  
    <p class="title logo__title">ROCprofiler-SDK 1.1.0 Documentation</p>
  
</a></div>
        <div class="sidebar-primary-item">

 <script>
 document.write(`
   <button class="btn search-button-field search-button__button" title="Search" aria-label="Search" data-bs-placement="bottom" data-bs-toggle="tooltip">
    <i class="fa-solid fa-magnifying-glass"></i>
    <span class="search-button__default-text">Search</span>
    <span class="search-button__kbd-shortcut"><kbd class="kbd-shortcut__modifier">Ctrl</kbd>+<kbd class="kbd-shortcut__modifier">K</kbd></span>
   </button>
 `);
 </script></div>
        <div class="sidebar-primary-item"><nav class="bd-links bd-docs-nav" aria-label="Main">
    <div class="bd-toc-item navbar-nav active">
        <p aria-level="2" class="caption" role="heading"><span class="caption-text">Install</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../../../install/installation.html">Installing ROCprofiler-SDK</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Quick Reference</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../../../quick_guide.html">ROCprofiler-SDK Quick Reference Guide</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">How to</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../../../how-to/samples.html">Samples</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../how-to/using-rocprofv3.html">Using rocprofv3</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../how-to/using-rocprofv3-avail.html">Using rocprofv3-avail</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../how-to/using-rocprofv3-process-attachment.html">Dynamic process attachment using rocprofv3</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../how-to/using-rocpd-output-format.html">Using rocpd output format</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../how-to/using-rocprofiler-sdk-roctx.html">Using ROCTx</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../how-to/using-rocprofv3-with-mpi.html">Using rocprofv3 with MPI</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../how-to/using-rocprofv3-with-openmp.html">Using rocprofv3 with OpenMP</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../how-to/using-pc-sampling.html">Using PC sampling</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../how-to/using-thread-trace.html">Using thread trace</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">API reference</span></p>
<ul class="current nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../../../api-reference/tool_library.html">Tool library</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../api-reference/intercept_table.html">Runtime intercept tables</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../api-reference/process_attachment.html">Process attachment</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../api-reference/buffered_services.html">Buffered services</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../api-reference/callback_services.html">Callback tracing services</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../api-reference/counter_collection_services.html">Counter collection services</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../api-reference/pc_sampling.html">PC sampling</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../api-reference/thread_trace.html">Thread trace and ROCprof Trace Decoder</a></li>
<li class="toctree-l1 current active has-children"><a class="reference internal" href="../../../api-reference/rocprofiler-sdk_api_reference.html">ROCprofiler-SDK API library</a><details open="open"><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul class="current">
<li class="toctree-l2 has-children"><a class="reference internal" href="../../../api-reference/rocprofiler-sdk_api/modules.html">Modules</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="../../../api-reference/rocprofiler-sdk_api/modules/agent_information.html">Agent Information</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../api-reference/rocprofiler-sdk_api/modules/buffer_handling.html">Buffer handling</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../api-reference/rocprofiler-sdk_api/modules/buffer_tracing.html">Buffer tracing</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../api-reference/rocprofiler-sdk_api/modules/callback_tracing.html">Callback tracing</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../api-reference/rocprofiler-sdk_api/modules/context_management.html">Context management</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../api-reference/rocprofiler-sdk_api/modules/counter_config.html">Counter config</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../api-reference/rocprofiler-sdk_api/modules/counters.html">Counters</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../api-reference/rocprofiler-sdk_api/modules/device_counting_service.html">Device counting service</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../api-reference/rocprofiler-sdk_api/modules/dispatch_counting_service.html">Dispatch counting service</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../api-reference/rocprofiler-sdk_api/modules/external_correalation.html">External correlation</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../api-reference/rocprofiler-sdk_api/modules/intercept_table.html">Intercept table</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../api-reference/rocprofiler-sdk_api/modules/internal_threading_management.html">Internal threading management</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../api-reference/rocprofiler-sdk_api/modules/ompt_registration.html">OMPT Registration</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../api-reference/rocprofiler-sdk_api/modules/pc_sampling_service.html">PC Sampling service</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../api-reference/rocprofiler-sdk_api/modules/thread_trace.html">Thread trace</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../api-reference/rocprofiler-sdk_api/modules/tool_registration.html">Tool registration</a></li>
</ul>
</details></li>
<li class="toctree-l2 current active has-children"><a class="reference internal" href="../../../api-reference/rocprofiler-sdk_api/global_data_structures_topics_files.html">Global Data structures, topics, files</a><details open="open"><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul class="current">
<li class="toctree-l3"><a class="reference internal" href="../../../api-reference/rocprofiler-sdk_api/global_data_structures_topics_files/global_basic_data_types.html">Global Basic Data Types</a></li>
<li class="toctree-l3 current active"><a class="current reference internal" href="#">Topics</a></li>
<li class="toctree-l3"><a class="reference internal" href="annotated.html">Data Structures</a></li>
<li class="toctree-l3"><a class="reference internal" href="files.html">File List</a></li>
</ul>
</details></li>
</ul>
</details></li>
<li class="toctree-l1 has-children"><a class="reference internal" href="../../../api-reference/rocprofiler-sdk-roctx_api_reference.html">ROCTx API</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2 has-children"><a class="reference internal" href="../../../api-reference/rocprofiler-sdk-roctx_api/roctx_modules.html">Modules</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="../../../api-reference/rocprofiler-sdk-roctx_api/roctx_modules/markers.html">Markers Information</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../api-reference/rocprofiler-sdk-roctx_api/roctx_modules/ranges.html">Ranges Information</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../api-reference/rocprofiler-sdk-roctx_api/roctx_modules/profiler-control.html">Profiler Control Information</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../api-reference/rocprofiler-sdk-roctx_api/roctx_modules/naming-utilities.html">Naming Information</a></li>
</ul>
</details></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="../../../api-reference/rocprofiler-sdk-roctx_api/global_roctx_data_structures_topics_files.html">Global Data structures, topics, files</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="../../../api-reference/rocprofiler-sdk-roctx_api/global_roctx_data_structures_topics_files/global_roctx_basic_data_types.html">Global Basic Data Types</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../roctx/html/topics.html">Topics</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../roctx/html/files.html">File List</a></li>
</ul>
</details></li>
</ul>
</details></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Conceptual</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../../../conceptual/comparing-with-legacy-tools.html">Comparing ROCprofiler-SDK to other ROCm profiling tools</a></li>



</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">License</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../../../license.html">License</a></li>
</ul>

    </div>
</nav></div>
    </div>
  
  
  <div class="sidebar-primary-items__end sidebar-primary__section">
  </div>
  
  <div id="rtd-footer-container"></div>


      </div>
      
      <main id="main-content" class="bd-main" role="main">
        
        

<div class="sbt-scroll-pixel-helper"></div>

          <div class="bd-content">
            <div class="bd-article-container">
              
              <div class="bd-header-article d-print-none">
<div class="header-article-items header-article__inner">
  
    <div class="header-article-items__start">
      
        <div class="header-article-item"><label class="sidebar-toggle primary-toggle btn btn-sm" for="__primary" title="Toggle primary sidebar" data-bs-placement="bottom" data-bs-toggle="tooltip">
    <span class="fa-solid fa-angle-right"></span>
  </label></div>
      
        <div class="header-article-item">



<nav aria-label="Breadcrumb" class="d-print-none">
  <ul class="bd-breadcrumbs">
    
    <li class="breadcrumb-item breadcrumb-home">
      <a href="../../../index.html" class="nav-link" aria-label="Home">
        <i class="fa-solid fa-home"></i>
      </a>
    </li>
    
    <li class="breadcrumb-item"><a href="../../../api-reference/rocprofiler-sdk_api_reference.html" class="nav-link">ROCprofiler-SDK API library</a></li>
    
    
    <li class="breadcrumb-item"><a href="../../../api-reference/rocprofiler-sdk_api/global_data_structures_topics_files.html" class="nav-link">Global Data structures, topics, files</a></li>
    
    <li class="breadcrumb-item active" aria-current="page">ROCprofiler-...</li>
  </ul>
</nav>
</div>
      
    </div>
  
  
    <div class="header-article-items__end">
      
        <div class="header-article-item">

<div class="article-header-buttons">


<script>
document.write(`
  <button class="btn btn-sm nav-link pst-navbar-icon theme-switch-button" title="light/dark" aria-label="light/dark" data-bs-placement="bottom" data-bs-toggle="tooltip">
    <i class="theme-switch fa-solid fa-sun fa-lg" data-mode="light"></i>
    <i class="theme-switch fa-solid fa-moon fa-lg" data-mode="dark"></i>
    <i class="theme-switch fa-solid fa-circle-half-stroke fa-lg" data-mode="auto"></i>
  </button>
`);
</script>


<script>
document.write(`
  <button class="btn btn-sm pst-navbar-icon search-button search-button__button" title="Search" aria-label="Search" data-bs-placement="bottom" data-bs-toggle="tooltip">
    <i class="fa-solid fa-magnifying-glass fa-lg"></i>
  </button>
`);
</script>

</div></div>
      
    </div>
  
</div>
</div>
              
              

<div id="jb-print-docs-body" class="onlyprint">
    <h1>Topics</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="topics">
<h1>Topics<a class="headerlink" href="#topics" title="Link to this heading">#</a></h1>
<div class="doxygen-content docutils container">
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en-US">
<head>
<meta http-equiv="Content-Type" content="text/xhtml;charset=UTF-8"/>
<meta http-equiv="X-UA-Compatible" content="IE=11"/>
<meta name="generator" content="Doxygen 1.9.8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>ROCprofiler-SDK developer API: Topics</title>
<link href="tabs.css" rel="stylesheet" type="text/css"/>
<script type="text/javascript" src="jquery.js"></script>
<script type="text/javascript" src="dynsections.js"></script>
<link href="doxygen.css" rel="stylesheet" type="text/css" />
<script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-rocprofiler-sdk" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/_doxygen/rocprofiler-sdk/html/topics.html" /><meta name="readthedocs-http-status" content="200" /></head>
<body>
<div id="top"><!-- do not remove this div, it is closed by doxygen! -->
<div id="titlearea">
<table cellspacing="0" cellpadding="0">
 <tbody>
 <tr id="projectrow">
  <td id="projectalign">
   <div id="projectname">ROCprofiler-SDK developer API<span id="projectnumber">&#160;1.1.0</span>
   </div>
   <div id="projectbrief">ROCm Profiling API and tools</div>
  </td>
 </tr>
 </tbody>
</table>
</div>
<!-- end header part -->
<!-- Generated by Doxygen 1.9.8 -->
<script type="text/javascript" src="menudata.js"></script>
<script type="text/javascript" src="menu.js"></script>
<script type="text/javascript">
/* @license magnet:?xt=urn:btih:d3d9a9a6595521f9666a5e94cc830dab83b65699&amp;dn=expat.txt MIT */
$(function() {
  initMenu('',false,false,'search.php','Search');
});
/* @license-end */
</script>
<div id="main-nav"></div>
</div><!-- top -->
<div class="header">
  <div class="headertitle"><div class="title">Topics</div></div>
</div><!--header-->
<div class="contents">
<div class="textblock">Here is a list of all topics with brief descriptions:</div><div class="directory">
<table class="directory">
<tr id="row_0_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><a class="el" href="group___a_g_e_n_t_s.html" target="_self">Agent Information</a></td><td class="desc">Needs brief description </td></tr>
<tr id="row_1_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><a class="el" href="group___b_u_f_f_e_r___h_a_n_d_l_i_n_g.html" target="_self">Buffer Handling</a></td><td class="desc">Creation, destruction, and flushing of buffers populated with data from rocprofiler </td></tr>
<tr id="row_2_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><a class="el" href="group___b_u_f_f_e_r___t_r_a_c_i_n_g___s_e_r_v_i_c_e.html" target="_self">Asynchronous Tracing Service</a></td><td class="desc">Receive callbacks for batches of records from an internal (background) thread </td></tr>
<tr id="row_3_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><a class="el" href="group___c_a_l_l_b_a_c_k___t_r_a_c_i_n_g___s_e_r_v_i_c_e.html" target="_self">Synchronous Tracing Services</a></td><td class="desc">Receive immediate callbacks on the calling thread </td></tr>
<tr id="row_4_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><a class="el" href="group___c_o_n_t_e_x_t___o_p_e_r_a_t_i_o_n_s.html" target="_self">Context Handling</a></td><td class="desc">Associate services with a handle. This handle is used to activate/deactivate the services during the application runtime </td></tr>
<tr id="row_5_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><a class="el" href="group___c_o_u_n_t_e_r___c_o_n_f_i_g.html" target="_self">HW Counter Configurations</a></td><td class="desc">Group one or more hardware counters into a unique handle </td></tr>
<tr id="row_6_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><a class="el" href="group___c_o_u_n_t_e_r_s.html" target="_self">Hardware counters Information</a></td><td class="desc">Query functions related to hardware counters </td></tr>
<tr id="row_7_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><a class="el" href="group___s_y_m_b_o_l___v_e_r_s_i_o_n_i_n_g___g_r_o_u_p.html" target="_self">Symbol Versions</a></td><td class="desc">The names used for the shared library versioned symbols </td></tr>
<tr id="row_8_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><a class="el" href="group__device__counting__service.html" target="_self">Agent Profile Counting Service</a></td><td class="desc">Needs brief description </td></tr>
<tr id="row_9_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><a class="el" href="group__dispatch__counting__service.html" target="_self">Dispatch Profile Counting Service</a></td><td class="desc">Per-dispatch hardware counter collection service </td></tr>
<tr id="row_10_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><a class="el" href="group___e_x_p_e_r_i_m_e_n_t_a_l___r_e_g_i_s_t_r_a_t_i_o_n___g_r_o_u_p.html" target="_self">Experimental tool registration</a></td><td class="desc">Data types and functions for tool registration with rocprofiler </td></tr>
<tr id="row_11_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><a class="el" href="group___t_h_r_e_a_d___t_r_a_c_e.html" target="_self">Thread Trace Service</a></td><td class="desc">Provides API calls to enable and handle thread trace data </td></tr>
<tr id="row_12_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><a class="el" href="group___e_x_t_e_r_n_a_l___c_o_r_r_e_l_a_t_i_o_n.html" target="_self">External Correlation IDs</a></td><td class="desc">User-defined correlation identifiers to supplement rocprofiler generated correlation ids </td></tr>
<tr id="row_13_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><a class="el" href="group___b_a_s_i_c___d_a_t_a___t_y_p_e_s.html" target="_self">Basic data types</a></td><td class="desc">Basic data types and typedefs </td></tr>
<tr id="row_14_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><a class="el" href="group___i_n_t_e_r_c_e_p_t___t_a_b_l_e.html" target="_self">Intercept table for runtime libraries</a></td><td class="desc">Enable tools to wrap the runtime API function calls of HIP, HSA, and ROCTx before and after the "real" implementation is called </td></tr>
<tr id="row_15_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><a class="el" href="group___i_n_t_e_r_n_a_l___t_h_r_e_a_d_i_n_g.html" target="_self">Internal Thread Handling</a></td><td class="desc">Callbacks before and after threads created internally by libraries </td></tr>
<tr id="row_16_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><a class="el" href="group___o_m_p_t___r_e_g_i_s_t_r_a_t_i_o_n.html" target="_self">Tool registration for OpenMP Tools</a></td><td class="desc"></td></tr>
<tr id="row_17_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><a class="el" href="group___p_c___s_a_m_p_l_i_n_g___s_e_r_v_i_c_e.html" target="_self">PC Sampling</a></td><td class="desc">Enabling PC (Program Counter) Sampling for GPU Activity </td></tr>
<tr id="row_18_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><a class="el" href="group___r_e_g_i_s_t_r_a_t_i_o_n___g_r_o_u_p.html" target="_self">Tool registration</a></td><td class="desc">Data types and functions for tool registration with rocprofiler </td></tr>
<tr id="row_19_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><a class="el" href="group___v_e_r_s_i_o_n_i_n_g___g_r_o_u_p.html" target="_self">Library Versioning</a></td><td class="desc">Version information about the interface and the associated installed library </td></tr>
<tr id="row_20_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><a class="el" href="group___m_i_s_c_e_l_l_a_n_e_o_u_s___g_r_o_u_p.html" target="_self">Miscellaneous Utility Functions</a></td><td class="desc">Utility functions for library </td></tr>
<tr id="row_21_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><a class="el" href="group___s_p_m___s_e_r_v_i_c_e.html" target="_self">SPM Service</a></td><td class="desc">Streaming Performance Monitoring </td></tr>
</table>
</div><!-- directory -->
</div><!-- contents -->
<!-- start footer part -->
<hr class="footer"/><address class="footer"><small>
Generated by&#160;<a href="https://www.doxygen.org/index.html"><img class="footer" src="doxygen.svg" width="104" height="31" alt="doxygen"/></a> 1.9.8
</small></address>
</body>
</html>
</div>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="../../../api-reference/rocprofiler-sdk_api/global_data_structures_topics_files/global_basic_data_types.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Global Basic Data Types</p>
      </div>
    </a>
    <a class="right-next"
       href="annotated.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Data Structures</p>
      </div>
      <i class="fa-solid fa-angle-right"></i>
    </a>
</div>
                </footer>
              
            </div>
            
            
              
            
          </div>
          <footer class="bd-footer-content">
            <p>
  </p>
          </footer>
        

      </main>
    </div>
  </div>
  
  <!-- Scripts loaded after <body> so the DOM is not blocked -->
  <script src="../../../_static/scripts/bootstrap.js?digest=dfe6caa3a7d634c4db9b"></script>
<script src="../../../_static/scripts/pydata-sphinx-theme.js?digest=dfe6caa3a7d634c4db9b"></script>

<footer class="rocm-footer">
    <div class="container-lg">
        <section class="bottom-menu menu py-45">
            <div class="row d-flex align-items-center">
                <div class="col-12 text-center">
                    <ul>
                        <li><a href="https://www.amd.com/en/corporate/copyright" target="_blank">Terms and Conditions</a></li>
                        <li><a href="https://rocm.docs.amd.com/en/latest/about/license.html">ROCm Licenses and Disclaimers</a></li>
                        <li><a href="https://www.amd.com/en/corporate/privacy" target="_blank">Privacy</a></li>
                        <li><a href="https://www.amd.com/en/corporate/trademarks" target="_blank">Trademarks</a></li>
                        <li><a href="https://www.amd.com/content/dam/amd/en/documents/corporate/cr/supply-chain-transparency.pdf" target="_blank">Supply Chain Transparency</a></li>
                        <li><a href="https://www.amd.com/en/corporate/competition" target="_blank">Fair and Open Competition</a></li>
                        <li><a href="https://www.amd.com/system/files/documents/amd-uk-tax-strategy.pdf" target="_blank">UK Tax Strategy</a></li>
                        <li><a href="https://www.amd.com/en/corporate/cookies" target="_blank">Cookie Policy</a></li>
                        <!-- OneTrust Cookies Settings button start -->
                        <li><a href="#cookie-settings" id="ot-sdk-btn" class="ot-sdk-show-settings">Cookie Settings</a></li>
                        <!-- OneTrust Cookies Settings button end -->
                    </ul>
                </div>
            </div>
            <div class="row d-flex align-items-center">
                <div class="col-12 text-center">
                    <div>
                        <span class="copyright">© 2026 Advanced Micro Devices, Inc</span>
                    </div>
                </div>
            </div>
        </section>
    </div>
</footer>

<!-- <div id="rdc-watermark-container">
    <img id="rdc-watermark" src="../../../_static/images/alpha-watermark.svg" alt="DRAFT watermark"/>
</div> -->
  </body>
</html>
