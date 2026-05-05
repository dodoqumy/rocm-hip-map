---
title: "Data type support &#8212; hipSPARSELt 0.2.6 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipSPARSELt/en/latest/reference/data-type-support.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T18:08:03.572297+00:00
content_hash: "a082d9bf4339d38e"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="hipSPARSELt API library data type support" name="description" />
<meta content="hipSPARSELt, ROCm, API library, API reference, data type, support" name="keywords" />

    <title>Data type support &#8212; hipSPARSELt 0.2.6 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'reference/data-type-support';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />
    <link rel="next" title="Environment variables" href="env-variables.html" />
    <link rel="prev" title="Supported ROCm and NVIDIA CUDA functions" href="supported-functions.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hipsparselt" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/reference/data-type-support.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../conceptual/storage-format.html">Storage formats</a></li>
<li class="toctree-l1"><a class="reference internal" href="../conceptual/mi300-features.html">Features for the Instinct MI300 series</a></li>
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
<ul class="current nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="supported-functions.html">Supported functions</a></li>
<li class="toctree-l1 current active"><a class="current reference internal" href="#">Data type support</a></li>
<li class="toctree-l1"><a class="reference internal" href="env-variables.html">Environment variables</a></li>
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
    <li class="breadcrumb-item active" aria-current="page"><span class="ellipsis">Data type support</span></li>
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
    <h1>Data type support</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#supported-input-and-output-types">Supported input and output types</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#supported-accumulator-types">Supported accumulator types</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#supported-compute-types">Supported compute types</a></li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="data-type-support">
<span id="id1"></span><h1>Data type support<a class="headerlink" href="#data-type-support" title="Link to this heading">#</a></h1>
<p>This topic lists the data type support for the hipSPARSELt library on AMD and
NVIDIA GPUs. The icons representing different levels of support are explained in
the following table.</p>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Icon</p></th>
<th class="head"><p>Definition</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>❌</p></td>
<td><p>Not supported</p></td>
</tr>
<tr class="row-odd"><td><p>✅</p></td>
<td><p>Full support</p></td>
</tr>
</tbody>
</table>
</div>
<p>For more information about data type support for the other ROCm libraries, see
<a class="reference external" href="https://rocm.docs.amd.com/en/latest/reference/precision-support.html" title="(in ROCm Documentation v7.2.2)"><span class="xref std std-doc">Data types and precision support page</span></a>.</p>
<section id="supported-input-and-output-types">
<h2>Supported input and output types<a class="headerlink" href="#supported-input-and-output-types" title="Link to this heading">#</a></h2>
<p>List of supported input and output types:</p>
<div class="pst-scrollable-table-container"><table class="table" id="supported-input-output-types">
<caption><span class="caption-number">Table 1 </span><span class="caption-text">Supported Input/Output Types</span><a class="headerlink" href="#supported-input-output-types" title="Link to this table">#</a></caption>
<thead>
<tr class="row-odd"><th class="head"><p>Input/output types</p></th>
<th class="head"><p>Library data type</p></th>
<th class="head"><p>AMD supports</p></th>
<th class="head"><p>NVIDIA supports</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>int8</p></td>
<td><p>HIP_R_8I</p></td>
<td><p>✅</p></td>
<td><p>✅</p></td>
</tr>
<tr class="row-odd"><td><p>float8</p></td>
<td><p>HIP_R_8F_E4M3</p></td>
<td><p>✅</p></td>
<td><p>✅</p></td>
</tr>
<tr class="row-even"><td><p>bfloat8</p></td>
<td><p>HIP_R_8F_E5M2</p></td>
<td><p>✅</p></td>
<td><p>✅</p></td>
</tr>
<tr class="row-odd"><td><p>int16</p></td>
<td><p>Not supported</p></td>
<td><p>❌</p></td>
<td><p>❌</p></td>
</tr>
<tr class="row-even"><td><p>float16</p></td>
<td><p>HIP_R_16F</p></td>
<td><p>✅</p></td>
<td><p>✅</p></td>
</tr>
<tr class="row-odd"><td><p>bfloat16</p></td>
<td><p>HIP_R_16BF</p></td>
<td><p>✅</p></td>
<td><p>✅</p></td>
</tr>
<tr class="row-even"><td><p>int32</p></td>
<td><p>HIP_R_32I</p></td>
<td><p>❌</p></td>
<td><p>✅</p></td>
</tr>
<tr class="row-odd"><td><p>tensorfloat32</p></td>
<td><p>Not supported</p></td>
<td><p>❌</p></td>
<td><p>❌</p></td>
</tr>
<tr class="row-even"><td><p>float32</p></td>
<td><p>HIP_R_32F</p></td>
<td><p>❌</p></td>
<td><p>✅</p></td>
</tr>
<tr class="row-odd"><td><p>float64</p></td>
<td><p>Not supported</p></td>
<td><p>❌</p></td>
<td><p>❌</p></td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="supported-accumulator-types">
<h2>Supported accumulator types<a class="headerlink" href="#supported-accumulator-types" title="Link to this heading">#</a></h2>
<p>List of supported accumulator types:</p>
<div class="pst-scrollable-table-container"><table class="table" id="id2">
<caption><span class="caption-number">Table 2 </span><span class="caption-text">Supported Compute Types</span><a class="headerlink" href="#id2" title="Link to this table">#</a></caption>
<thead>
<tr class="row-odd"><th class="head"><p>Accumulator types</p></th>
<th class="head"><p>Library data type</p></th>
<th class="head"><p>AMD supports</p></th>
<th class="head"><p>NVIDIA supports</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>int8</p></td>
<td><p>Not supported</p></td>
<td><p>❌</p></td>
<td><p>❌</p></td>
</tr>
<tr class="row-odd"><td><p>float8</p></td>
<td><p>Not supported</p></td>
<td><p>❌</p></td>
<td><p>❌</p></td>
</tr>
<tr class="row-even"><td><p>bfloat8</p></td>
<td><p>Not supported</p></td>
<td><p>❌</p></td>
<td><p>❌</p></td>
</tr>
<tr class="row-odd"><td><p>int16</p></td>
<td><p>Not supported</p></td>
<td><p>❌</p></td>
<td><p>❌</p></td>
</tr>
<tr class="row-even"><td><p>float16</p></td>
<td><p>HIPSPARSELT_COMPUTE_16F</p></td>
<td><p>❌</p></td>
<td><p>✅</p></td>
</tr>
<tr class="row-odd"><td><p>bfloat16</p></td>
<td><p>Not supported</p></td>
<td><p>❌</p></td>
<td><p>❌</p></td>
</tr>
<tr class="row-even"><td><p>int32</p></td>
<td><p>HIPSPARSELT_COMPUTE_32I</p></td>
<td><p>✅</p></td>
<td><p>✅</p></td>
</tr>
<tr class="row-odd"><td><p>tensorfloat32</p></td>
<td><p>Not supported</p></td>
<td><p>❌</p></td>
<td><p>❌</p></td>
</tr>
<tr class="row-even"><td><p>float32</p></td>
<td><p>HIPSPARSELT_COMPUTE_32F</p></td>
<td><p>✅</p></td>
<td><p>✅</p></td>
</tr>
<tr class="row-odd"><td><p>float64</p></td>
<td><p>Not supported</p></td>
<td><p>❌</p></td>
<td><p>❌</p></td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="supported-compute-types">
<h2>Supported compute types<a class="headerlink" href="#supported-compute-types" title="Link to this heading">#</a></h2>
<p>List of supported compute types for specific input and output types:</p>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Input A/B</p></th>
<th class="head"><p>Input C</p></th>
<th class="head"><p>Output D</p></th>
<th class="head"><p>Compute type</p></th>
<th class="head"><p>Backend</p></th>
<th class="head"><p>Support LLVM target for HIP backend</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>HIP_R_32F</p></td>
<td><p>HIP_R_32F</p></td>
<td><p>HIP_R_32F</p></td>
<td><p>HIPSPARSELT_COMPUTE_32F</p></td>
<td><p>CUDA</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>HIP_R_16F</p></td>
<td><p>HIP_R_16F</p></td>
<td><p>HIP_R_16F</p></td>
<td><p>HIPSPARSELT_COMPUTE_32F</p></td>
<td><p>HIP / CUDA</p></td>
<td><p>gfx942, gfx950</p></td>
</tr>
<tr class="row-even"><td><p>HIP_R_16F</p></td>
<td><p>HIP_R_16F</p></td>
<td><p>HIP_R_16F</p></td>
<td><p>HIPSPARSELT_COMPUTE_16F</p></td>
<td><p>CUDA</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>HIP_R_16BF</p></td>
<td><p>HIP_R_16BF</p></td>
<td><p>HIP_R_16BF</p></td>
<td><p>HIPSPARSELT_COMPUTE_32F</p></td>
<td><p>HIP / CUDA</p></td>
<td><p>gfx942, gfx950</p></td>
</tr>
<tr class="row-even"><td><p>HIP_R_8I</p></td>
<td><p>HIP_R_8I</p></td>
<td><p>HIP_R_8I</p></td>
<td><p>HIPSPARSELT_COMPUTE_32I</p></td>
<td><p>HIP / CUDA</p></td>
<td><p>gfx942, gfx950</p></td>
</tr>
<tr class="row-odd"><td><p>HIP_R_8I</p></td>
<td><p>HIP_R_32I</p></td>
<td><p>HIP_R_32I</p></td>
<td><p>HIPSPARSELT_COMPUTE_32I</p></td>
<td><p>CUDA</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>HIP_R_8I</p></td>
<td><p>HIP_R_16F</p></td>
<td><p>HIP_R_16F</p></td>
<td><p>HIPSPARSELT_COMPUTE_32I</p></td>
<td><p>HIP / CUDA</p></td>
<td><p>gfx942, gfx950</p></td>
</tr>
<tr class="row-odd"><td><p>HIP_R_8I</p></td>
<td><p>HIP_R_16BF</p></td>
<td><p>HIP_R_16BF</p></td>
<td><p>HIPSPARSELT_COMPUTE_32I</p></td>
<td><p>HIP / CUDA</p></td>
<td><p>gfx942, gfx950</p></td>
</tr>
<tr class="row-even"><td><p>HIP_R_8F_E4M3</p></td>
<td><p>HIP_R_16F</p></td>
<td><p>HIP_R_8F_E4M3</p></td>
<td><p>HIPSPARSELT_COMPUTE_32F</p></td>
<td><p>CUDA</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>HIP_R_8F_E4M3</p></td>
<td><p>HIP_R_16BF</p></td>
<td><p>HIP_R_8F_E4M3</p></td>
<td><p>HIPSPARSELT_COMPUTE_32F</p></td>
<td><p>CUDA</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>HIP_R_8F_E4M3</p></td>
<td><p>HIP_R_16F</p></td>
<td><p>HIP_R_16F</p></td>
<td><p>HIPSPARSELT_COMPUTE_32F</p></td>
<td><p>CUDA</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>HIP_R_8F_E4M3</p></td>
<td><p>HIP_R_16BF</p></td>
<td><p>HIP_R_16BF</p></td>
<td><p>HIPSPARSELT_COMPUTE_32F</p></td>
<td><p>CUDA</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>HIP_R_8F_E4M3</p></td>
<td><p>HIP_R_32F</p></td>
<td><p>HIP_R_32F</p></td>
<td><p>HIPSPARSELT_COMPUTE_32F</p></td>
<td><p>HIP / CUDA</p></td>
<td><p>gfx950</p></td>
</tr>
<tr class="row-odd"><td><p>HIP_R_8F_E5M2</p></td>
<td><p>HIP_R_16F</p></td>
<td><p>HIP_R_8F_E5M2</p></td>
<td><p>HIPSPARSELT_COMPUTE_32F</p></td>
<td><p>CUDA</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>HIP_R_8F_E5M2</p></td>
<td><p>HIP_R_16BF</p></td>
<td><p>HIP_R_8F_E5M2</p></td>
<td><p>HIPSPARSELT_COMPUTE_32F</p></td>
<td><p>CUDA</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>HIP_R_8F_E5M2</p></td>
<td><p>HIP_R_16F</p></td>
<td><p>HIP_R_16F</p></td>
<td><p>HIPSPARSELT_COMPUTE_32F</p></td>
<td><p>CUDA</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>HIP_R_8F_E5M2</p></td>
<td><p>HIP_R_16BF</p></td>
<td><p>HIP_R_16BF</p></td>
<td><p>HIPSPARSELT_COMPUTE_32F</p></td>
<td><p>CUDA</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>HIP_R_8F_E5M2</p></td>
<td><p>HIP_R_32F</p></td>
<td><p>HIP_R_32F</p></td>
<td><p>HIPSPARSELT_COMPUTE_32F</p></td>
<td><p>HIP / CUDA</p></td>
<td><p>gfx950</p></td>
</tr>
</tbody>
</table>
</div>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="supported-functions.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Supported ROCm and NVIDIA CUDA functions</p>
      </div>
    </a>
    <a class="right-next"
       href="env-variables.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Environment variables</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#supported-input-and-output-types">Supported input and output types</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#supported-accumulator-types">Supported accumulator types</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#supported-compute-types">Supported compute types</a></li>
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
