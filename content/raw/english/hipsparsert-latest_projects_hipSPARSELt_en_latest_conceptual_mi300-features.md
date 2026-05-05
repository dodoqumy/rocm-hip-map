---
title: "hipSPARSELt features for the Instinct MI300 series &#8212; hipSPARSELt 0.2.6 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipSPARSELt/en/latest/conceptual/mi300-features.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:10:08.238858+00:00
content_hash: "4f9e77365b4646d6"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="MI300 features for hipSPARSELt" name="description" />
<meta content="hipSPARSELt, ROCm, MI300" name="keywords" />

    <title>hipSPARSELt features for the Instinct MI300 series &#8212; hipSPARSELt 0.2.6 Documentation</title>
  
  
  
  <script data-cfasync="false">
    document.documentElement.dataset.mode = localStorage.getItem("mode") || "";
    document.documentElement.dataset.theme = localStorage.getItem("theme") || "";
  </script>
  <!--
    this give us a css class that will be invisible only if js is disabled
  -->
  <noscript>
    <style>
      .pst-js-only { display: none !important; }

    </style>
  </noscript>
  
  <!-- Loaded before other Sphinx assets -->
  <link href="../_static/styles/theme.css?digest=8878045cc6db502f8baf" rel="stylesheet" />
<link href="../_static/styles/pydata-sphinx-theme.css?digest=8878045cc6db502f8baf" rel="stylesheet" />

    <link rel="stylesheet" type="text/css" href="../_static/pygments.css?v=8f2a1f02" />
    <link rel="stylesheet" type="text/css" href="../_static/styles/sphinx-book-theme.css?v=a3416100" />
    <link rel="stylesheet" type="text/css" href="../_static/mystnb.8ecb98da25f57f5357bf6f572d296f466b2cfe2517ffebfabe82451661e28f02.css" />
    <link rel="stylesheet" type="text/css" href="../_static/copybutton.css?v=76b2166b" />
    <link rel="stylesheet" type="text/css" href="../_static/custom.css?v=643846e8" />
    <link rel="stylesheet" type="text/css" href="../_static/rocm_header.css?v=9557e3d1" />
    <link rel="stylesheet" type="text/css" href="../_static/rocm_footer.css?v=7095035a" />
    <link rel="stylesheet" type="text/css" href="../_static/fonts.css?v=fcff5274" />
    <link rel="stylesheet" type="text/css" href="../_static/sphinx-design.min.css?v=95c83b7e" />
  
  <!-- So that users can add custom icons -->
  <script src="../_static/scripts/fontawesome.js?digest=8878045cc6db502f8baf"></script>
  <!-- Pre-loaded scripts that we'll load fully later -->
  <link rel="preload" as="script" href="../_static/scripts/bootstrap.js?digest=8878045cc6db502f8baf" />
<link rel="preload" as="script" href="../_static/scripts/pydata-sphinx-theme.js?digest=8878045cc6db502f8baf" />

    <script src="../_static/documentation_options.js?v=519527b2"></script>
    <script src="../_static/doctools.js?v=9bcbadda"></script>
    <script src="../_static/sphinx_highlight.js?v=dc90522c"></script>
    <script src="../_static/clipboard.min.js?v=a7894cd8"></script>
    <script src="../_static/copybutton.js?v=91c4cb68"></script>
    <script async="async" src="../_static/code_word_breaks.js?v=327952c4"></script>
    <script async="async" src="../_static/renameVersionLinks.js?v=929fe5e4"></script>
    <script async="async" src="../_static/rdcMisc.js?v=01f88d96"></script>
    <script async="async" src="../_static/theme_mode_captions.js?v=15f4ec5d"></script>
    <script defer="defer" src="../_static/search.js?v=90a4452c"></script>
    <script src="../_static/scripts/sphinx-book-theme.js?v=887ef09a"></script>
    <script src="../_static/design-tabs.js?v=f930bc37"></script>
    <script>DOCUMENTATION_OPTIONS.pagename = 'conceptual/mi300-features';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />
    <link rel="next" title="HIP device and stream management" href="../how-to/device-stream-management.html" />
    <link rel="prev" title="hipSPARSELt storage format" href="storage-format.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hipsparselt" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/conceptual/mi300-features.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
  <body data-bs-spy="scroll" data-bs-target=".bd-toc-nav" data-offset="180" data-bs-root-margin="0px 0px -60%" data-default-mode="">

  
  
  <div id="pst-skip-link" class="skip-link d-print-none"><a href="#main-content">Skip to main content</a></div>
  
  <div id="pst-scroll-pixel-helper"></div>
  
  <button type="button" class="btn rounded-pill" id="pst-back-to-top">
    <i class="fa-solid fa-arrow-up"></i>Back to top</button>

  
  <dialog id="pst-search-dialog">
    
<form class="bd-search d-flex align-items-center"
      action="../search.html"
      method="get">
  <i class="fa-solid fa-magnifying-glass"></i>
  <input type="search"
         class="form-control"
         name="q"
         placeholder="Search..."
         aria-label="Search..."
         autocomplete="off"
         autocorrect="off"
         autocapitalize="off"
         spellcheck="false"/>
  <span class="search-button__kbd-shortcut"><kbd class="kbd-shortcut__modifier">Ctrl</kbd>+<kbd>K</kbd></span>
</form>
  </dialog>

  <div class="pst-async-banner-revealer d-none">
  <aside id="bd-header-version-warning" class="d-none d-print-none" aria-label="Version warning"></aside>
</div>

  

<header class="common-header" >
    <nav class="navbar navbar-expand-xl">
        <div class="container-fluid main-nav rocm-header">
            
            <button class="navbar-toggler collapsed" id="nav-icon" data-tracking-information="mainMenuToggle" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span></span>
                <span></span>
                <span></span>
            </button>
            
            <div class="header-logo">
                <a class="navbar-brand" href="https://www.amd.com/">
                    <img src="../_static/images/amd-header-logo.svg" alt="AMD Logo" title="AMD Logo" width="90" class="d-inline-block align-text-top hover-opacity"/>
                </a>
                <div class="vr vr mx-40 my-25"></div>
                
        
    
    <a class="klavika-font hover-opacity" href="https://rocm.docs.amd.com/en/latest">ROCm&#8482; Software 7.2.2</a>
                <a class="header-all-versions" href="https://rocm.docs.amd.com/en/latest/release/versions.html">Version List</a>
            </div>
            <div class="icon-nav text-center d-flex ms-auto">
            </div>
        </div>
    </nav>
    
    <nav class="navbar navbar-expand-xl second-level-nav">
        <div class="container-fluid main-nav">
            <div class="navbar-nav-container collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav nav-mega me-auto mb-2 mb-lg-0 col-xl-10">
                    
                        <li class="nav-item">
                            <a class="nav-link top-level header-menu-links" href="https://github.com/ROCm/rocm-libraries" id="navgithub" role="button" aria-expanded="false" target="_blank" >
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
                            <a class="nav-link top-level header-menu-links" href="https://instinct.docs.amd.com" id="navinstinct&#8482;-docs" role="button" aria-expanded="false" target="_blank" >
                                Instinct&#8482; Docs
                            </a>
                        </li>
                    
                        <li class="nav-item">
                            <a class="nav-link top-level header-menu-links" href="https://www.amd.com/en/developer/resources/infinity-hub.html" id="navinfinity-hub" role="button" aria-expanded="false" target="_blank" >
                                Infinity Hub
                            </a>
                        </li>
                    
                        <li class="nav-item">
                            <a class="nav-link top-level header-menu-links" href="https://github.com/ROCm/rocm-libraries/issues/new/choose" id="navsupport" role="button" aria-expanded="false" target="_blank" >
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
      
      
      
      <dialog id="pst-primary-sidebar-modal"></dialog>
      <div id="pst-primary-sidebar" class="bd-sidebar-primary bd-sidebar">
        

  
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

  
    
  

<a class="navbar-brand logo" href="../index.html">
  
  
  
  
  
  
    <p class="title logo__title">hipSPARSELt 0.2.6 Documentation</p>
  
</a></div>
        <div class="sidebar-primary-item">

<button class="btn search-button-field search-button__button pst-js-only" title="Search" aria-label="Search" data-bs-placement="bottom" data-bs-toggle="tooltip">
 <i class="fa-solid fa-magnifying-glass"></i>
 <span class="search-button__default-text">Search</span>
 <span class="search-button__kbd-shortcut"><kbd class="kbd-shortcut__modifier">Ctrl</kbd>+<kbd class="kbd-shortcut__modifier">K</kbd></span>
</button></div>
        <div class="sidebar-primary-item"><nav class="bd-links bd-docs-nav" aria-label="Main">
    <div class="bd-toc-item navbar-nav active">
        <ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../what-is-hipsparselt.html">What is hipSPARSELt?</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Install</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../install/quick-start-install.html">Quick start installation guide</a></li>
<li class="toctree-l1"><a class="reference internal" href="../install/install-hipsparselt.html">Detailed installation guide</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Conceptual</span></p>
<ul class="current nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="storage-format.html">Storage formats</a></li>
<li class="toctree-l1 current active"><a class="current reference internal" href="#">Features for the Instinct MI300 series</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">How to</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../how-to/device-stream-management.html">Manage devices and streams</a></li>
<li class="toctree-l1"><a class="reference internal" href="../how-to/porting.html">Port from NVIDIA CUDA</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Examples</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference external" href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipsparselt/clients/samples">Client samples</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">API Reference</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../reference/supported-functions.html">Supported functions</a></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/data-type-support.html">Data type support</a></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/env-variables.html">Environment variables</a></li>
<li class="toctree-l1 has-children"><a class="reference internal" href="../doxygen/html/index.html">API library</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2"><a class="reference internal" href="../doxygen/html/modules.html">Modules</a></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="../doxygen/html/annotated_data_structures.html">Data Structures</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="../doxygen/html/annotated.html">Data Structures</a></li>
<li class="toctree-l3"><a class="reference internal" href="../doxygen/html/classes.html">Data Structure Index</a></li>
<li class="toctree-l3 has-children"><a class="reference internal" href="../doxygen/html/functions_data_fields.html">Data Fields</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="../doxygen/html/functions.html">All</a></li>
<li class="toctree-l4"><a class="reference internal" href="../doxygen/html/functions_vars.html">Variables</a></li>
</ul>
</details></li>
</ul>
</details></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="../doxygen/html/files_files.html">Files</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="../doxygen/html/files.html">File List</a></li>
<li class="toctree-l3 has-children"><a class="reference internal" href="../doxygen/html/globals_globals.html">Globals</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="../doxygen/html/globals.html">All</a></li>
<li class="toctree-l4"><a class="reference internal" href="../doxygen/html/globals_func.html">Functions</a></li>
<li class="toctree-l4"><a class="reference internal" href="../doxygen/html/globals_enum.html">Enumerations</a></li>
<li class="toctree-l4"><a class="reference internal" href="../doxygen/html/globals_eval.html">Enumerator</a></li>
<li class="toctree-l4"><a class="reference internal" href="../doxygen/html/globals_defs.html">Macros</a></li>
</ul>
</details></li>
</ul>
</details></li>
</ul>
</details></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">About</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../license.html">License</a></li>
</ul>

    </div>
</nav></div>
    </div>
  
  
  <div class="sidebar-primary-items__end sidebar-primary__section">
      <div class="sidebar-primary-item">
<div id="ethical-ad-placement"
      class="flat"
      data-ea-publisher="readthedocs"
      data-ea-type="readthedocs-sidebar"
      data-ea-manual="true">
</div></div>
  </div>


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
      <a href="../index.html" class="nav-link" aria-label="Home">
        <i class="fa-solid fa-home"></i>
      </a>
    </li>
    <li class="breadcrumb-item active" aria-current="page"><span class="ellipsis">hipSPARSELt features for the Instinct MI300 series</span></li>
  </ul>
</nav>
</div>
      
    </div>
  
  
    <div class="header-article-items__end">
      
        <div class="header-article-item">

<div class="article-header-buttons">


<button class="btn btn-sm nav-link pst-navbar-icon theme-switch-button pst-js-only" aria-label="Color mode" data-bs-title="Color mode"  data-bs-placement="bottom" data-bs-toggle="tooltip">
  <i class="theme-switch fa-solid fa-sun                fa-lg" data-mode="light" title="Light"></i>
  <i class="theme-switch fa-solid fa-moon               fa-lg" data-mode="dark"  title="Dark"></i>
  <i class="theme-switch fa-solid fa-circle-half-stroke fa-lg" data-mode="auto"  title="System Settings"></i>
</button>


<button class="btn btn-sm pst-navbar-icon search-button search-button__button pst-js-only" title="Search" aria-label="Search" data-bs-placement="bottom" data-bs-toggle="tooltip">
    <i class="fa-solid fa-magnifying-glass fa-lg"></i>
</button>
<button class="sidebar-toggle secondary-toggle btn btn-sm" title="Toggle secondary sidebar" data-bs-placement="bottom" data-bs-toggle="tooltip">
    <span class="fa-solid fa-list"></span>
</button>
</div></div>
      
    </div>
  
</div>
</div>
              
              

<div id="jb-print-docs-body" class="onlyprint">
    <h1>hipSPARSELt features for the Instinct MI300 series</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#data-types-and-precision">Data types and precision</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#matrix-format-requirements">Matrix format requirements</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#sparse-matrix">Sparse matrix</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#dense-matrix">Dense matrix</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#matrix-preparation">Matrix preparation</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#understanding-the-pruning-and-compression-process">Understanding the pruning and compression process</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#pruning-and-compression-workflow">Pruning and compression workflow</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#detailed-implementation-example">Detailed implementation example</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#pruning-options-and-parameters">Pruning options and parameters</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#performance-considerations">Performance considerations</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#matrix-operation-setup">Matrix operation setup</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#descriptor-configuration">Descriptor configuration</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#plan-creation-and-execution">Plan creation and execution</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#stream-usage-notes">Stream usage notes</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#supported-operations">Supported operations</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#standard-matrix-multiplication">Standard matrix multiplication</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#batched-operations">Batched operations</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#fused-operations">Fused operations</a></li>
</ul>
</li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="hipsparselt-features-for-the-instinct-mi300-series">
<span id="mi300-features"></span><h1>hipSPARSELt features for the Instinct MI300 series<a class="headerlink" href="#hipsparselt-features-for-the-instinct-mi300-series" title="Link to this heading">#</a></h1>
<p>hipSPARSELt provides hardware acceleration support for sparse matrix multiplication operations
on AMD Instinct™ MI300 series GPUs using SMFMA (Sparse Matrix Fused Multiply Add) matrix instructions.</p>
<p>For hardware-accelerated sparse-dense matrix operations, the following conditions apply:</p>
<ul class="simple">
<li><p>One matrix must be structurally sparse. Two out of every four elements on the K axis must be zero.</p></li>
<li><p>The other matrix must be dense.</p></li>
<li><p>The output matrix serves as the accumulation (destination) matrix.</p></li>
<li><p>The sparse indexes determine which two elements out of every four are non-zero, where for each index pair,
<code class="docutils literal notranslate"><span class="pre">index0</span> <span class="pre">&lt;</span> <span class="pre">index1</span></code> and <code class="docutils literal notranslate"><span class="pre">index0</span> <span class="pre">!=</span> <span class="pre">index1</span></code>.</p></li>
</ul>
<section id="data-types-and-precision">
<h2>Data types and precision<a class="headerlink" href="#data-types-and-precision" title="Link to this heading">#</a></h2>
<p>While the Instinct MI300 series supports multiple data types for hardware-accelerated sparse matrix operations,
the hipSPARSELt library currently enables hardware acceleration for a subset of these types:</p>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Input/output type</p></th>
<th class="head"><p>Library data type</p></th>
<th class="head"><p>Hardware acceleration in hipSPARSELt</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>float16</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">HIP_R_16F</span></code></p></td>
<td><p>✅</p></td>
</tr>
<tr class="row-odd"><td><p>bfloat16</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">HIP_R_16BF</span></code></p></td>
<td><p>✅</p></td>
</tr>
<tr class="row-even"><td><p>int8</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">HIP_R_8I</span></code></p></td>
<td><p>✅</p></td>
</tr>
</tbody>
</table>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>While the Instinct MI300 series supports additional formats such as <code class="docutils literal notranslate"><span class="pre">FP8</span></code> (E4M3 and E5M2) and <code class="docutils literal notranslate"><span class="pre">BF8</span></code>, these are not currently
enabled at the library level for hardware acceleration.
All floating-point operations accumulate in <code class="docutils literal notranslate"><span class="pre">float32</span></code>, while integer operations accumulate in <code class="docutils literal notranslate"><span class="pre">int32</span></code>.</p>
<p>For comprehensive information on the supported data types and their characteristics, see the
<a class="reference internal" href="../reference/data-type-support.html#data-type-support"><span class="std std-ref">Data type support</span></a> page.</p>
</div>
</section>
<section id="matrix-format-requirements">
<h2>Matrix format requirements<a class="headerlink" href="#matrix-format-requirements" title="Link to this heading">#</a></h2>
<p>For MI300 hardware acceleration, the matrices must meet the specific format requirements for the matrix type.</p>
<section id="sparse-matrix">
<h3>Sparse matrix<a class="headerlink" href="#sparse-matrix" title="Link to this heading">#</a></h3>
<p>Sparse matrices must:</p>
<ul class="simple">
<li><p>Follow a 2:4 structured sparsity pattern</p></li>
<li><p>Use a compressed sparse format</p></li>
<li><p>Meet the alignment requirements for the selected data type</p></li>
</ul>
</section>
<section id="dense-matrix">
<h3>Dense matrix<a class="headerlink" href="#dense-matrix" title="Link to this heading">#</a></h3>
<p>Dense matrices must:</p>
<ul class="simple">
<li><p>Be in standard dense format</p></li>
<li><p>Meet the alignment requirements for the selected data type</p></li>
</ul>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The hipSPARSELt library supports configurations where either the first or second operand is the
structured sparse matrix. The other operand must be a dense matrix. This flexibility is achieved
through library-level handling that adjusts the memory layout and operation order accordingly.</p>
</div>
</section>
</section>
<section id="matrix-preparation">
<h2>Matrix preparation<a class="headerlink" href="#matrix-preparation" title="Link to this heading">#</a></h2>
<p>The sparse matrix must be prepared for SMFMA operations through a two-step process of pruning and compression.</p>
<section id="understanding-the-pruning-and-compression-process">
<h3>Understanding the pruning and compression process<a class="headerlink" href="#understanding-the-pruning-and-compression-process" title="Link to this heading">#</a></h3>
<p><strong>Pruning</strong> involves converting a dense matrix into a structured sparse format by selectively zeroing
out elements according to a specific pattern. For MI300 SMFMA operations, the matrix must use the 2:4
pattern (50% sparsity) where exactly two out of every four consecutive elements along the K dimension are
preserved, with the rest set to zero.</p>
<p><strong>Compression</strong> follows pruning and converts the pruned matrix into a hardware-optimized format that
stores only the non-zero values and their corresponding indices. This reduces the memory requirements
and enables direct use of the SMFMA hardware instructions.</p>
</section>
<section id="pruning-and-compression-workflow">
<h3>Pruning and compression workflow<a class="headerlink" href="#pruning-and-compression-workflow" title="Link to this heading">#</a></h3>
<p>The complete process involves several steps:</p>
<ol class="arabic simple">
<li><p>Initialize the matrix descriptors and matmul descriptor.</p></li>
<li><p>Determine the workspace requirements for compression.</p></li>
<li><p>Allocate memory for the pruned and compressed matrices.</p></li>
<li><p>Perform pruning using the 2:4 sparsity pattern.</p></li>
<li><p>Verify the pruning was successful.</p></li>
<li><p>Compress the pruned matrix.</p></li>
</ol>
<figure class="align-default">
<img alt="../_images/prune-workflow.svg" src="../_images/prune-workflow.svg" />
</figure>
</section>
<section id="detailed-implementation-example">
<h3>Detailed implementation example<a class="headerlink" href="#detailed-implementation-example" title="Link to this heading">#</a></h3>
<p>Here’s a detailed implementation of the pruning and compression process:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="c1">// Step 1: Set up matrix and matmul descriptors (see Descriptor Configuration section)</span>
<span class="c1">// ...</span>

<span class="c1">// Step 2: Get workspace sizes for compression</span>
<span class="kt">size_t</span><span class="w"> </span><span class="n">workspace_size</span><span class="p">,</span><span class="w"> </span><span class="n">compressed_size</span><span class="p">,</span><span class="w"> </span><span class="n">compress_buffer_size</span><span class="p">;</span>
<span class="n">CHECK_HIPSPARSELT_ERROR</span><span class="p">(</span><span class="n">hipsparseLtSpMMACompressedSize</span><span class="p">(</span>
<span class="w">    </span><span class="o">&amp;</span><span class="n">handle</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">plan</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">compressed_size</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">compress_buffer_size</span><span class="p">));</span>

<span class="c1">// Step 3: Allocate memory</span>
<span class="c1">// Allocate compression buffers</span>
<span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">d_compressed</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">nullptr</span><span class="p">;</span><span class="w">             </span><span class="c1">// Will hold the final compressed matrix</span>
<span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">d_compressBuffer</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">nullptr</span><span class="p">;</span><span class="w">         </span><span class="c1">// Temporary buffer for compression</span>
<span class="n">CHECK_HIP_ERROR</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">d_compressed</span><span class="p">,</span><span class="w"> </span><span class="n">compressed_size</span><span class="p">));</span>
<span class="n">CHECK_HIP_ERROR</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">d_compressBuffer</span><span class="p">,</span><span class="w"> </span><span class="n">compress_buffer_size</span><span class="p">));</span>

<span class="c1">// Allocate temporary buffer for the pruned (but not yet compressed) matrix</span>
<span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">dp</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">nullptr</span><span class="p">;</span>
<span class="n">CHECK_HIP_ERROR</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">dp</span><span class="p">,</span><span class="w"> </span><span class="n">matrix_size</span><span class="p">));</span>

<span class="c1">// Step 4: Prune matrix A using 2:4 sparsity pattern</span>
<span class="c1">// The original dense matrix &#39;dA&#39; is pruned into the temporary buffer &#39;dp&#39;</span>
<span class="c1">// HIPSPARSELT_PRUNE_SPMMA_STRIP selects the two largest elements in each 1x4 strip</span>
<span class="n">CHECK_HIPSPARSELT_ERROR</span><span class="p">(</span><span class="n">hipsparseLtSpMMAPrune</span><span class="p">(</span>
<span class="w">    </span><span class="o">&amp;</span><span class="n">handle</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">matmul</span><span class="p">,</span><span class="w"> </span><span class="n">dA</span><span class="p">,</span><span class="w"> </span><span class="n">dp</span><span class="p">,</span><span class="w"> </span><span class="n">HIPSPARSELT_PRUNE_SPMMA_STRIP</span><span class="p">,</span><span class="w"> </span><span class="n">stream</span><span class="p">));</span>

<span class="c1">// Step 5: Verify pruning success</span>
<span class="c1">// Check if the pruned matrix maintains the required 2:4 sparsity pattern</span>
<span class="kt">bool</span><span class="w"> </span><span class="n">is_valid</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nb">false</span><span class="p">;</span>
<span class="n">CHECK_HIPSPARSELT_ERROR</span><span class="p">(</span><span class="n">hipsparseLtSpMMAPruneCheck</span><span class="p">(</span>
<span class="w">    </span><span class="o">&amp;</span><span class="n">handle</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">matmul</span><span class="p">,</span><span class="w"> </span><span class="n">dp</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">is_valid</span><span class="p">,</span><span class="w"> </span><span class="n">stream</span><span class="p">));</span>
<span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="o">!</span><span class="n">is_valid</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="n">fprintf</span><span class="p">(</span><span class="n">stderr</span><span class="p">,</span><span class="w"> </span><span class="s">&quot;Error: Matrix pruning failed to achieve required sparsity pattern</span><span class="se">\n</span><span class="s">&quot;</span><span class="p">);</span>
<span class="w">    </span><span class="k">goto</span><span class="w"> </span><span class="n">cleanup</span><span class="p">;</span>
<span class="p">}</span>

<span class="c1">// Step 6: Compress the pruned matrix</span>
<span class="c1">// Convert the pruned matrix &#39;dp&#39; into the compressed format &#39;d_compressed&#39;</span>
<span class="c1">// This format is optimized for direct use with the MI300 SMFMA hardware instructions</span>
<span class="n">CHECK_HIPSPARSELT_ERROR</span><span class="p">(</span>
<span class="w">    </span><span class="n">hipsparseLtSpMMACompress</span><span class="p">(</span><span class="o">&amp;</span><span class="n">handle</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">plan</span><span class="p">,</span><span class="w"> </span><span class="n">dp</span><span class="p">,</span><span class="w"> </span><span class="n">d_compressed</span><span class="p">,</span><span class="w"> </span><span class="n">d_compressBuffer</span><span class="p">,</span><span class="w"> </span><span class="n">stream</span><span class="p">));</span>

<span class="c1">// Once completed, &#39;d_compressed&#39; contains the matrix in a format ready for SMFMA operations</span>
<span class="c1">// This compressed matrix is used in place of the original dense matrix in subsequent operations</span>

<span class="c1">// Always clean up resources when done</span>
<span class="nl">cleanup</span><span class="p">:</span>
<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">dp</span><span class="p">)</span><span class="w"> </span><span class="n">CHECK_HIP_ERROR</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">dp</span><span class="p">));</span>
<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">d_compressBuffer</span><span class="p">)</span><span class="w"> </span><span class="n">CHECK_HIP_ERROR</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">d_compressBuffer</span><span class="p">));</span>
<span class="w">    </span><span class="c1">// Don&#39;t free d_compressed yet as it&#39;s needed for matmul operations</span>
</pre></div>
</div>
</section>
<section id="pruning-options-and-parameters">
<h3>Pruning options and parameters<a class="headerlink" href="#pruning-options-and-parameters" title="Link to this heading">#</a></h3>
<p>The pruning function supports different strategies through the <code class="docutils literal notranslate"><span class="pre">alg</span></code> parameter:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">HIPSPARSELT_PRUNE_SPMMA_STRIP</span></code>: Zeroes out two elements in a 1x4 strip. Non-zero elements
have the maximum L1-norm value in all combinations in the strip.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">HIPSPARSELT_PRUNE_SPMMA_TILE</span></code>: Zeroes out eight elements in a 4x4 tile. Non-zero elements
have the maximum L1-norm value in all combinations in the tile. There are exactly two elements in each
row and column.</p></li>
</ul>
</section>
<section id="performance-considerations">
<h3>Performance considerations<a class="headerlink" href="#performance-considerations" title="Link to this heading">#</a></h3>
<ul class="simple">
<li><p>Pruning is typically performed once during initialization, not in the critical computation path.</p></li>
<li><p>The quality of pruning affects the accuracy of matrix multiplication results.</p></li>
<li><p>For matrices that don’t naturally fit the 2:4 pattern, consider pretraining with
structured sparsity constraints.</p></li>
</ul>
</section>
</section>
<section id="matrix-operation-setup">
<h2>Matrix operation setup<a class="headerlink" href="#matrix-operation-setup" title="Link to this heading">#</a></h2>
<p>The following sections describe how to set up matrix operations with SMFMA, including
descriptor configuration and execution plans.</p>
<section id="descriptor-configuration">
<h3>Descriptor configuration<a class="headerlink" href="#descriptor-configuration" title="Link to this heading">#</a></h3>
<p>Matrix descriptors define the properties and memory layout for each matrix in the operation.
For SMFMA:</p>
<ul class="simple">
<li><p>Matrix A requires a structured descriptor with 50% sparsity (2:4 pattern).</p></li>
<li><p>Matrix B uses a dense descriptor.</p></li>
<li><p>The compute type should be set to <code class="docutils literal notranslate"><span class="pre">FP32</span></code> accumulation on AMD platforms.</p></li>
</ul>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="c1">// Initialize sparse matrix A descriptor</span>
<span class="n">CHECK_HIPSPARSELT_ERROR</span><span class="p">(</span>
<span class="w">    </span><span class="n">hipsparseLtStructuredDescriptorInit</span><span class="p">(</span><span class="o">&amp;</span><span class="n">handle</span><span class="p">,</span>
<span class="w">                                      </span><span class="o">&amp;</span><span class="n">matA</span><span class="p">,</span>
<span class="w">                                      </span><span class="n">row_a</span><span class="p">,</span>
<span class="w">                                      </span><span class="n">col_a</span><span class="p">,</span>
<span class="w">                                      </span><span class="n">lda</span><span class="p">,</span>
<span class="w">                                      </span><span class="mi">16</span><span class="p">,</span>
<span class="w">                                      </span><span class="n">HIP_R_16F</span><span class="p">,</span>
<span class="w">                                      </span><span class="n">HIPSPARSE_ORDER_COL</span><span class="p">,</span>
<span class="w">                                      </span><span class="n">HIPSPARSELT_SPARSITY_50_PERCENT</span><span class="p">));</span>

<span class="c1">// Initialize dense matrix B descriptor</span>
<span class="n">CHECK_HIPSPARSELT_ERROR</span><span class="p">(</span><span class="n">hipsparseLtDenseDescriptorInit</span><span class="p">(</span>
<span class="w">    </span><span class="o">&amp;</span><span class="n">handle</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">matB</span><span class="p">,</span><span class="w"> </span><span class="n">row_b</span><span class="p">,</span><span class="w"> </span><span class="n">col_b</span><span class="p">,</span><span class="w"> </span><span class="n">ldb</span><span class="p">,</span><span class="w"> </span><span class="mi">16</span><span class="p">,</span><span class="w"> </span><span class="n">HIP_R_16F</span><span class="p">,</span><span class="w"> </span><span class="n">HIPSPARSE_ORDER_COL</span><span class="p">));</span>

<span class="c1">// Initialize compute type</span>
<span class="k">auto</span><span class="w"> </span><span class="n">compute_type</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">HIPSPARSELT_COMPUTE_32F</span><span class="p">;</span><span class="w">  </span><span class="c1">// For AMD platforms</span>

<span class="c1">// Initialize matmul descriptor</span>
<span class="n">CHECK_HIPSPARSELT_ERROR</span><span class="p">(</span><span class="n">hipsparseLtMatmulDescriptorInit</span><span class="p">(</span>
<span class="w">    </span><span class="o">&amp;</span><span class="n">handle</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">matmul</span><span class="p">,</span><span class="w"> </span><span class="n">trans_a</span><span class="p">,</span><span class="w"> </span><span class="n">trans_b</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">matA</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">matB</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">matC</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">matD</span><span class="p">,</span><span class="w"> </span><span class="n">compute_type</span><span class="p">));</span>
</pre></div>
</div>
</section>
<section id="plan-creation-and-execution">
<h3>Plan creation and execution<a class="headerlink" href="#plan-creation-and-execution" title="Link to this heading">#</a></h3>
<p>Create and execute the matrix multiplication plan:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="c1">// Initialize matmul plan</span>
<span class="n">CHECK_HIPSPARSELT_ERROR</span><span class="p">(</span><span class="n">hipsparseLtMatmulAlgSelectionInit</span><span class="p">(</span>
<span class="w">    </span><span class="o">&amp;</span><span class="n">handle</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">alg_sel</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">matmul</span><span class="p">,</span><span class="w"> </span><span class="n">HIPSPARSELT_MATMUL_ALG_DEFAULT</span><span class="p">));</span>

<span class="n">CHECK_HIPSPARSELT_ERROR</span><span class="p">(</span><span class="n">hipsparseLtMatmulPlanInit</span><span class="p">(</span><span class="o">&amp;</span><span class="n">handle</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">plan</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">matmul</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">alg_sel</span><span class="p">));</span>

<span class="c1">// Get and allocate workspace if needed</span>
<span class="kt">size_t</span><span class="w"> </span><span class="n">workspace_size</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="n">CHECK_HIPSPARSELT_ERROR</span><span class="p">(</span><span class="n">hipsparseLtMatmulGetWorkspace</span><span class="p">(</span><span class="o">&amp;</span><span class="n">handle</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">plan</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">workspace_size</span><span class="p">));</span>
<span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">d_workspace</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">nullptr</span><span class="p">;</span>
<span class="k">if</span><span class="p">(</span><span class="n">workspace_size</span><span class="w"> </span><span class="o">&gt;</span><span class="w"> </span><span class="mi">0</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="n">CHECK_HIP_ERROR</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">d_workspace</span><span class="p">,</span><span class="w"> </span><span class="n">workspace_size</span><span class="p">));</span>
<span class="p">}</span>

<span class="c1">// Configure and create stream</span>
<span class="kt">int</span><span class="w"> </span><span class="n">num_streams</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span><span class="w">  </span><span class="c1">// Default to single stream</span>
<span class="n">hipStream_t</span><span class="w"> </span><span class="n">streams</span><span class="p">[</span><span class="mi">1</span><span class="p">];</span>
<span class="n">CHECK_HIP_ERROR</span><span class="p">(</span><span class="n">hipStreamCreate</span><span class="p">(</span><span class="o">&amp;</span><span class="n">streams</span><span class="p">[</span><span class="mi">0</span><span class="p">]));</span>

<span class="c1">// Execute matmul operation</span>
<span class="n">CHECK_HIPSPARSELT_ERROR</span><span class="p">(</span><span class="n">hipsparseLtMatmul</span><span class="p">(</span><span class="o">&amp;</span><span class="n">handle</span><span class="p">,</span>
<span class="w">                                         </span><span class="o">&amp;</span><span class="n">plan</span><span class="p">,</span>
<span class="w">                                         </span><span class="o">&amp;</span><span class="n">alpha</span><span class="p">,</span>
<span class="w">                                         </span><span class="n">d_compressed</span><span class="p">,</span><span class="w">  </span><span class="c1">// Compressed sparse matrix A</span>
<span class="w">                                         </span><span class="n">dB</span><span class="p">,</span><span class="w">           </span><span class="c1">// Dense matrix B</span>
<span class="w">                                         </span><span class="o">&amp;</span><span class="n">beta</span><span class="p">,</span>
<span class="w">                                         </span><span class="n">dC</span><span class="p">,</span>
<span class="w">                                         </span><span class="n">dD</span><span class="p">,</span>
<span class="w">                                         </span><span class="n">d_workspace</span><span class="p">,</span>
<span class="w">                                         </span><span class="o">&amp;</span><span class="n">streams</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span>
<span class="w">                                         </span><span class="n">num_streams</span><span class="p">));</span>

<span class="c1">// Cleanup resources</span>
<span class="n">CHECK_HIP_ERROR</span><span class="p">(</span><span class="n">hipStreamDestroy</span><span class="p">(</span><span class="n">streams</span><span class="p">[</span><span class="mi">0</span><span class="p">]));</span>
<span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">d_workspace</span><span class="p">)</span><span class="w"> </span><span class="n">CHECK_HIP_ERROR</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">d_workspace</span><span class="p">));</span>
</pre></div>
</div>
</section>
<section id="stream-usage-notes">
<h3>Stream usage notes<a class="headerlink" href="#stream-usage-notes" title="Link to this heading">#</a></h3>
<ul class="simple">
<li><p>Single stream is sufficient for most operations.</p></li>
<li><p>Multiple streams can improve performance when processing independent operations.</p></li>
<li><p>Ensure proper synchronization when using multiple streams with dependent operations.</p></li>
<li><p>The stream count is specified using the <code class="docutils literal notranslate"><span class="pre">num_streams</span></code> parameter.</p></li>
</ul>
</section>
</section>
<section id="supported-operations">
<h2>Supported operations<a class="headerlink" href="#supported-operations" title="Link to this heading">#</a></h2>
<p>hipSPARSELt with MI300 hardware acceleration supports several types of matrix operations,
described in detail below.</p>
<section id="standard-matrix-multiplication">
<h3>Standard matrix multiplication<a class="headerlink" href="#standard-matrix-multiplication" title="Link to this heading">#</a></h3>
<p>The basic operation performs sparse-dense matrix multiplication with optional scaling:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="c1">// D = α × op(sparse_matrix) × op(dense_matrix) + β × C</span>
<span class="c1">// Note: Either the first or second operand can be the sparse matrix</span>
<span class="n">CHECK_HIPSPARSELT_ERROR</span><span class="p">(</span><span class="n">hipsparseLtMatmul</span><span class="p">(</span><span class="o">&amp;</span><span class="n">handle</span><span class="p">,</span>
<span class="w">                                         </span><span class="o">&amp;</span><span class="n">plan</span><span class="p">,</span>
<span class="w">                                         </span><span class="o">&amp;</span><span class="n">alpha</span><span class="p">,</span>
<span class="w">                                         </span><span class="n">compressed_matrix</span><span class="p">,</span><span class="w">  </span><span class="c1">// Compressed sparse matrix</span>
<span class="w">                                         </span><span class="n">dense_matrix</span><span class="p">,</span><span class="w">      </span><span class="c1">// Dense matrix</span>
<span class="w">                                         </span><span class="o">&amp;</span><span class="n">beta</span><span class="p">,</span>
<span class="w">                                         </span><span class="n">dC</span><span class="p">,</span>
<span class="w">                                         </span><span class="n">dD</span><span class="p">,</span>
<span class="w">                                         </span><span class="n">d_workspace</span><span class="p">,</span>
<span class="w">                                         </span><span class="o">&amp;</span><span class="n">streams</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span>
<span class="w">                                         </span><span class="n">num_streams</span><span class="p">));</span>
</pre></div>
</div>
</section>
<section id="batched-operations">
<h3>Batched operations<a class="headerlink" href="#batched-operations" title="Link to this heading">#</a></h3>
<p>hipSPARSELt supports multiple types of batched operations, which provide support for
MI300 hardware acceleration:</p>
<ul>
<li><p>Broadcast mode (single sparse matrix/multiple dense matrices)</p>
<p>A single sparse matrix is multiplied with multiple dense matrices.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="c1">// Configure sparse matrix (constant across all batch operations)</span>
<span class="n">CHECK_HIPSPARSELT_ERROR</span><span class="p">(</span><span class="n">hipsparseLtMatDescSetAttribute</span><span class="p">(</span>
<span class="w">    </span><span class="o">&amp;</span><span class="n">handle</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">sparse_mat</span><span class="p">,</span><span class="w"> </span><span class="n">HIPSPARSELT_MAT_NUM_BATCHES</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">batch_count</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="n">batch_count</span><span class="p">)));</span>
<span class="n">CHECK_HIPSPARSELT_ERROR</span><span class="p">(</span><span class="n">hipsparseLtMatDescSetAttribute</span><span class="p">(</span>
<span class="w">    </span><span class="o">&amp;</span><span class="n">handle</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">sparse_mat</span><span class="p">,</span><span class="w"> </span><span class="n">HIPSPARSELT_MAT_BATCH_STRIDE</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">zero_stride</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="n">zero_stride</span><span class="p">)));</span>

<span class="c1">// Configure dense matrices (different for each batch operation)</span>
<span class="n">CHECK_HIPSPARSELT_ERROR</span><span class="p">(</span><span class="n">hipsparseLtMatDescSetAttribute</span><span class="p">(</span>
<span class="w">    </span><span class="o">&amp;</span><span class="n">handle</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">dense_mat</span><span class="p">,</span><span class="w"> </span><span class="n">HIPSPARSELT_MAT_NUM_BATCHES</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">batch_count</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="n">batch_count</span><span class="p">)));</span>
<span class="n">CHECK_HIPSPARSELT_ERROR</span><span class="p">(</span><span class="n">hipsparseLtMatDescSetAttribute</span><span class="p">(</span>
<span class="w">    </span><span class="o">&amp;</span><span class="n">handle</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">dense_mat</span><span class="p">,</span><span class="w"> </span><span class="n">HIPSPARSELT_MAT_BATCH_STRIDE</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">dense_stride</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="n">dense_stride</span><span class="p">)));</span>
</pre></div>
</div>
</li>
<li><p>Multiple sparse and dense matrices</p>
<p>Different sparse and dense matrix pairs are multiplied in each batch operation.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="c1">// Configure sparse matrices (different for each batch operation)</span>
<span class="n">CHECK_HIPSPARSELT_ERROR</span><span class="p">(</span><span class="n">hipsparseLtMatDescSetAttribute</span><span class="p">(</span>
<span class="w">    </span><span class="o">&amp;</span><span class="n">handle</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">sparse_mat</span><span class="p">,</span><span class="w"> </span><span class="n">HIPSPARSELT_MAT_NUM_BATCHES</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">batch_count</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="n">batch_count</span><span class="p">)));</span>
<span class="n">CHECK_HIPSPARSELT_ERROR</span><span class="p">(</span><span class="n">hipsparseLtMatDescSetAttribute</span><span class="p">(</span>
<span class="w">    </span><span class="o">&amp;</span><span class="n">handle</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">sparse_mat</span><span class="p">,</span><span class="w"> </span><span class="n">HIPSPARSELT_MAT_BATCH_STRIDE</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">sparse_stride</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="n">sparse_stride</span><span class="p">)));</span>

<span class="c1">// Configure dense matrices (different for each batch operation)</span>
<span class="n">CHECK_HIPSPARSELT_ERROR</span><span class="p">(</span><span class="n">hipsparseLtMatDescSetAttribute</span><span class="p">(</span>
<span class="w">    </span><span class="o">&amp;</span><span class="n">handle</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">dense_mat</span><span class="p">,</span><span class="w"> </span><span class="n">HIPSPARSELT_MAT_NUM_BATCHES</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">batch_count</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="n">batch_count</span><span class="p">)));</span>
<span class="n">CHECK_HIPSPARSELT_ERROR</span><span class="p">(</span><span class="n">hipsparseLtMatDescSetAttribute</span><span class="p">(</span>
<span class="w">    </span><span class="o">&amp;</span><span class="n">handle</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">dense_mat</span><span class="p">,</span><span class="w"> </span><span class="n">HIPSPARSELT_MAT_BATCH_STRIDE</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">dense_stride</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="n">dense_stride</span><span class="p">)));</span>
</pre></div>
</div>
</li>
<li><p>Batched bias addition</p>
<p>This feature can be combined with matrix multiplication operations to add
different bias vectors for each batch operation. The bias addition is supported as
a fused operation alongside hardware-accelerated matrix multiplication.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="c1">// Configure batched bias vectors</span>
<span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">bias_ptr</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">d_bias</span><span class="p">;</span><span class="w">  </span><span class="c1">// Pointer to the first bias vector</span>
<span class="kt">size_t</span><span class="w"> </span><span class="n">bias_stride</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">bias_vector_size</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="n">data_type</span><span class="p">);</span>

<span class="n">CHECK_HIPSPARSELT_ERROR</span><span class="p">(</span><span class="n">hipsparseLtMatmulDescriptorSetAttribute</span><span class="p">(</span>
<span class="w">    </span><span class="o">&amp;</span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="o">&amp;</span><span class="n">matmul</span><span class="p">,</span>
<span class="w">    </span><span class="n">HIPSPARSELT_MATMUL_BIAS_POINTER</span><span class="p">,</span>
<span class="w">    </span><span class="o">&amp;</span><span class="n">bias_ptr</span><span class="p">,</span>
<span class="w">    </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">void</span><span class="o">*</span><span class="p">)));</span>

<span class="n">CHECK_HIPSPARSELT_ERROR</span><span class="p">(</span><span class="n">hipsparseLtMatmulDescriptorSetAttribute</span><span class="p">(</span>
<span class="w">    </span><span class="o">&amp;</span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="o">&amp;</span><span class="n">matmul</span><span class="p">,</span>
<span class="w">    </span><span class="n">HIPSPARSELT_MATMUL_BIAS_BATCH_STRIDE</span><span class="p">,</span>
<span class="w">    </span><span class="o">&amp;</span><span class="n">bias_stride</span><span class="p">,</span>
<span class="w">    </span><span class="k">sizeof</span><span class="p">(</span><span class="n">bias_stride</span><span class="p">)));</span>
</pre></div>
</div>
</li>
</ul>
</section>
<section id="fused-operations">
<h3>Fused operations<a class="headerlink" href="#fused-operations" title="Link to this heading">#</a></h3>
<p>Matrix multiplication operations can be fused with additional operations to improve performance:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="c1">// Configure bias addition</span>
<span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">bias_ptr</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">nullptr</span><span class="p">;</span>
<span class="n">CHECK_HIPSPARSELT_ERROR</span><span class="p">(</span><span class="n">hipsparseLtMatmulDescriptorSetAttribute</span><span class="p">(</span>
<span class="w">    </span><span class="o">&amp;</span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="o">&amp;</span><span class="n">matmul</span><span class="p">,</span>
<span class="w">    </span><span class="n">HIPSPARSELT_MATMUL_BIAS_POINTER</span><span class="p">,</span>
<span class="w">    </span><span class="o">&amp;</span><span class="n">bias_ptr</span><span class="p">,</span>
<span class="w">    </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">void</span><span class="o">*</span><span class="p">)));</span>

<span class="c1">// Configure activation function (for example, ReLU)</span>
<span class="n">hipsparseLtActivationType_t</span><span class="w"> </span><span class="n">act_type</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">HIPSPARSELT_ACTIVATION_RELU</span><span class="p">;</span>
<span class="n">CHECK_HIPSPARSELT_ERROR</span><span class="p">(</span><span class="n">hipsparseLtMatmulDescriptorSetAttribute</span><span class="p">(</span>
<span class="w">    </span><span class="o">&amp;</span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="o">&amp;</span><span class="n">matmul</span><span class="p">,</span>
<span class="w">    </span><span class="n">HIPSPARSELT_MATMUL_ACTIVATION_TYPE</span><span class="p">,</span>
<span class="w">    </span><span class="o">&amp;</span><span class="n">act_type</span><span class="p">,</span>
<span class="w">    </span><span class="k">sizeof</span><span class="p">(</span><span class="n">act_type</span><span class="p">)));</span>
</pre></div>
</div>
<p>Operations are executed in the following order:</p>
<ol class="arabic simple">
<li><p>Sparse-dense matrix multiplication</p></li>
<li><p>Scaling by alpha/beta</p></li>
<li><p>Bias addition (if configured)</p></li>
<li><p>Activation function (if configured)</p></li>
</ol>
<p>This fusion helps maximize performance by reducing intermediate memory operations.</p>
</section>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="storage-format.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">hipSPARSELt storage format</p>
      </div>
    </a>
    <a class="right-next"
       href="../how-to/device-stream-management.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">HIP device and stream management</p>
      </div>
      <i class="fa-solid fa-angle-right"></i>
    </a>
</div>
                </footer>
              
            </div>
            
            
              
                <dialog id="pst-secondary-sidebar-modal"></dialog>
                <div id="pst-secondary-sidebar" class="bd-sidebar-secondary bd-toc"><div class="sidebar-secondary-items sidebar-secondary__inner">


  <div class="sidebar-secondary-item">
  <div class="page-toc tocsection onthispage">
    <i class="fa-solid fa-list"></i> Contents
  </div>
  <nav class="bd-toc-nav page-toc">
    <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#data-types-and-precision">Data types and precision</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#matrix-format-requirements">Matrix format requirements</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#sparse-matrix">Sparse matrix</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#dense-matrix">Dense matrix</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#matrix-preparation">Matrix preparation</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#understanding-the-pruning-and-compression-process">Understanding the pruning and compression process</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#pruning-and-compression-workflow">Pruning and compression workflow</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#detailed-implementation-example">Detailed implementation example</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#pruning-options-and-parameters">Pruning options and parameters</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#performance-considerations">Performance considerations</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#matrix-operation-setup">Matrix operation setup</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#descriptor-configuration">Descriptor configuration</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#plan-creation-and-execution">Plan creation and execution</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#stream-usage-notes">Stream usage notes</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#supported-operations">Supported operations</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#standard-matrix-multiplication">Standard matrix multiplication</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#batched-operations">Batched operations</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#fused-operations">Fused operations</a></li>
</ul>
</li>
</ul>
  </nav></div>

</div></div>
              
            
          </div>
          <footer class="bd-footer-content">
            <p>
  </p>
          </footer>
        

      </main>
    </div>
  </div>
  
  <!-- Scripts loaded after <body> so the DOM is not blocked -->
  <script defer src="../_static/scripts/bootstrap.js?digest=8878045cc6db502f8baf"></script>
<script defer src="../_static/scripts/pydata-sphinx-theme.js?digest=8878045cc6db502f8baf"></script>

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
                        <span class="copyright">© 2025 Advanced Micro Devices, Inc</span>
                    </div>
                </div>
            </div>
        </section>
    </div>
</footer>

<!-- <div id="rdc-watermark-container">
    <img id="rdc-watermark" src="../_static/images/alpha-watermark.svg" alt="DRAFT watermark"/>
</div> -->
  </body>
</html>
