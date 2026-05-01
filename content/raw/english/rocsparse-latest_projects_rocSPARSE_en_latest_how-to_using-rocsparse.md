---
title: "rocSPARSE user guide &#8212; rocSPARSE 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocSPARSE/en/latest/how-to/using-rocsparse.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:17:04.620528+00:00
content_hash: "0053309d86d6ffd9"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="rocSPARSE user guide and documentation" name="description" />
<meta content="rocSPARSE, ROCm, API, documentation, user guide" name="keywords" />

    <title>rocSPARSE user guide &#8212; rocSPARSE 4.2.0 Documentation</title>
  
  
  
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

    <script src="../_static/documentation_options.js?v=830d3dd9"></script>
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'how-to/using-rocsparse';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />
    <link rel="next" title="rocSPARSE API reference guide" href="../reference/reference.html" />
    <link rel="prev" title="rocSPARSE storage formats" href="../conceptual/storage-formats-sparse.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-rocsparse" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/how-to/using-rocsparse.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
  
  
  
  
  
  
    <p class="title logo__title">rocSPARSE 4.2.0 Documentation</p>
  
</a></div>
        <div class="sidebar-primary-item">

<button class="btn search-button-field search-button__button pst-js-only" title="Search" aria-label="Search" data-bs-placement="bottom" data-bs-toggle="tooltip">
 <i class="fa-solid fa-magnifying-glass"></i>
 <span class="search-button__default-text">Search</span>
 <span class="search-button__kbd-shortcut"><kbd class="kbd-shortcut__modifier">Ctrl</kbd>+<kbd class="kbd-shortcut__modifier">K</kbd></span>
</button></div>
        <div class="sidebar-primary-item"><nav class="bd-links bd-docs-nav" aria-label="Main">
    <div class="bd-toc-item navbar-nav active">
        <p aria-level="2" class="caption" role="heading"><span class="caption-text">Install</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../install/Linux_Install_Guide.html">Linux installation guide</a></li>
<li class="toctree-l1"><a class="reference internal" href="../install/Windows_Install_Guide.html">Windows installation guide</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Conceptual</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../conceptual/rocsparse-design.html">rocSPARSE design</a></li>
<li class="toctree-l1"><a class="reference internal" href="../conceptual/storage-formats-sparse.html">Storage formats</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">How to</span></p>
<ul class="current nav bd-sidenav">
<li class="toctree-l1 current active"><a class="current reference internal" href="#">Use rocSPARSE</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Examples</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference external" href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/rocsparse/clients/samples">Client samples</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">API reference</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1 has-children"><a class="reference internal" href="../reference/reference.html">API reference</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2"><a class="reference internal" href="../reference/api.html">Exported rocSPARSE functions</a></li>
<li class="toctree-l2"><a class="reference internal" href="../reference/debugging.html">Debugging rocSPARSE functions</a></li>
<li class="toctree-l2"><a class="reference internal" href="../reference/types.html">rocSPARSE data types</a></li>
<li class="toctree-l2"><a class="reference internal" href="../reference/precision.html">rocSPARSE precision support</a></li>
<li class="toctree-l2"><a class="reference internal" href="../reference/env_variables.html">rocSPARSE environment variables</a></li>
<li class="toctree-l2"><a class="reference internal" href="../reference/roctx.html">rocSPARSE profiling functions</a></li>
<li class="toctree-l2"><a class="reference internal" href="../reference/enumerations.html">rocSPARSE enumerations</a></li>
<li class="toctree-l2"><a class="reference internal" href="../reference/auxiliary.html">Sparse auxiliary functions</a></li>
<li class="toctree-l2"><a class="reference internal" href="../reference/level1.html">Sparse level 1 functions</a></li>
<li class="toctree-l2"><a class="reference internal" href="../reference/level2.html">Sparse level 2 functions</a></li>
<li class="toctree-l2"><a class="reference internal" href="../reference/level3.html">Sparse level 3 functions</a></li>
<li class="toctree-l2"><a class="reference internal" href="../reference/extra.html">Sparse extra functions</a></li>
<li class="toctree-l2"><a class="reference internal" href="../reference/precond.html">Sparse preconditioner functions</a></li>
<li class="toctree-l2"><a class="reference internal" href="../reference/conversion.html">Sparse conversion functions</a></li>
<li class="toctree-l2"><a class="reference internal" href="../reference/reorder.html">Sparse reordering functions</a></li>
<li class="toctree-l2"><a class="reference internal" href="../reference/utility.html">Sparse utility functions</a></li>
<li class="toctree-l2"><a class="reference internal" href="../reference/generic.html">Sparse generic functions</a></li>
<li class="toctree-l2"><a class="reference internal" href="../reference/reproducibility.html">Bitwise reproducibility</a></li>
</ul>
</details></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">About</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../license.html">License</a></li>
<li class="toctree-l1"><a class="reference internal" href="../contribute.html">Contribute to rocSPARSE</a></li>
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
    <li class="breadcrumb-item active" aria-current="page"><span class="ellipsis">rocSPARSE user guide</span></li>
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
    <h1>rocSPARSE user guide</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-device-management">HIP device management</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-stream-management">HIP stream management</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#asynchronous-execution">Asynchronous execution</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#multiple-streams-and-multiple-devices">Multiple streams and multiple devices</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#graph-support-for-rocsparse">Graph support for rocSPARSE</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#functions-supported-with-graph-capture">Functions supported with graph capture</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#sparse-level-1-functions">Sparse level 1 functions</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#sparse-level-2-functions">Sparse level 2 functions</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#sparse-level-3-functions">Sparse level 3 functions</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#sparse-extra-functions">Sparse extra functions</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#preconditioner-functions">Preconditioner functions</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#conversion-functions">Conversion functions</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#reordering-functions">Reordering functions</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#utility-functions">Utility functions</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#sparse-generic-functions">Sparse generic functions</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#storage-formats">Storage formats</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#pointer-mode">Pointer mode</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#activity-logging-deprecated">Activity logging [Deprecated]</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#roc-tx-support-in-rocsparse">ROC-TX support in rocSPARSE</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsparse-fortran-bindings">rocSPARSE Fortran bindings</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsparse">hipSPARSE</a></li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="rocsparse-user-guide">
<span id="rocsparse-docs"></span><h1>rocSPARSE user guide<a class="headerlink" href="#rocsparse-user-guide" title="Link to this heading">#</a></h1>
<p>This topic discusses how to use rocSPARSE, including a discussion of device and stream management, storage formats, pointer mode,
and how hipSPARSE interacts with rocSPARSE.</p>
<section id="hip-device-management">
<h2>HIP device management<a class="headerlink" href="#hip-device-management" title="Link to this heading">#</a></h2>
<p>Before starting a HIP kernel, you can call <a class="reference external" href="https://rocm.docs.amd.com/projects/HIP/en/latest/reference/hip_runtime_api/modules/device_management.html#_CPPv412hipSetDevicei" title="(in HIP Documentation v7.2.53211)"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipSetDevice()</span></code></a> to set the device to run the kernel on,
for example, device <code class="docutils literal notranslate"><span class="pre">2</span></code>. Unless you explicitly specify a different device, HIP kernels always run on device <code class="docutils literal notranslate"><span class="pre">0</span></code>.
This HIP (and CUDA) device management approach is not specific to the rocSPARSE library.
rocSPARSE honors this approach and assumes you have already set the preferred device before a rocSPARSE routine call.</p>
<p>After you set the device, you can create a handle with <a class="reference internal" href="../reference/auxiliary.html#rocsparse-create-handle"><span class="std std-ref">rocsparse_create_handle()</span></a>.
Subsequent rocSPARSE routines take this handle as an input parameter.
rocSPARSE only queries the specified device (using <a class="reference external" href="https://rocm.docs.amd.com/projects/HIP/en/latest/reference/hip_runtime_api/modules/device_management.html#_CPPv412hipGetDevicePi" title="(in HIP Documentation v7.2.53211)"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipGetDevice()</span></code></a>) and does not set the device for users.
It’s your responsibility to provide a valid device to rocSPARSE and ensure device safety.
If it’s not a valid device, rocSPARSE returns an error message.</p>
<p>The handle should be destroyed at the end using <a class="reference internal" href="../reference/auxiliary.html#rocsparse-destroy-handle"><span class="std std-ref">rocsparse_destroy_handle()</span></a> to release the resources
consumed by the rocSPARSE library. You <strong>cannot</strong> switch devices
between <a class="reference internal" href="../reference/auxiliary.html#rocsparse-create-handle"><span class="std std-ref">rocsparse_create_handle()</span></a> and <a class="reference internal" href="../reference/auxiliary.html#rocsparse-destroy-handle"><span class="std std-ref">rocsparse_destroy_handle()</span></a>. To change the device,
you must destroy the current handle and create another rocSPARSE handle on a new device.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p><a class="reference external" href="https://rocm.docs.amd.com/projects/HIP/en/latest/reference/hip_runtime_api/modules/device_management.html#_CPPv412hipSetDevicei" title="(in HIP Documentation v7.2.53211)"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipSetDevice()</span></code></a> and <a class="reference external" href="https://rocm.docs.amd.com/projects/HIP/en/latest/reference/hip_runtime_api/modules/device_management.html#_CPPv412hipGetDevicePi" title="(in HIP Documentation v7.2.53211)"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipGetDevice()</span></code></a> are not part of the rocSPARSE API.
They are part of the <a class="reference external" href="https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___device.html">HIP Device Management API</a>.</p>
</div>
</section>
<section id="hip-stream-management">
<h2>HIP stream management<a class="headerlink" href="#hip-stream-management" title="Link to this heading">#</a></h2>
<p>HIP kernels are always launched in a queue, which is also known as a stream. If you don’t explicitly specify a stream,
the system provides and maintains a default stream, which you cannot create or destroy.
However, you can freely create a new stream using <a class="reference external" href="https://rocm.docs.amd.com/projects/HIP/en/latest/reference/hip_runtime_api/modules/stream_management.html#_CPPv415hipStreamCreateP11hipStream_t" title="(in HIP Documentation v7.2.53211)"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipStreamCreate()</span></code></a> and bind it to a rocSPARSE handle
using <a class="reference internal" href="../reference/auxiliary.html#rocsparse-set-stream"><span class="std std-ref">rocsparse_set_stream()</span></a>. The rocSPARSE routines invoke HIP kernels.
A rocSPARSE handle is always associated with a stream, which rocSPARSE passes to the kernels inside the routine.
One rocSPARSE routine only takes one stream in a single invocation.
If you create a stream, you are responsible for destroying it.
See the <a class="reference external" href="https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___stream.html">HIP Stream Management API</a> for more information.</p>
</section>
<section id="asynchronous-execution">
<h2>Asynchronous execution<a class="headerlink" href="#asynchronous-execution" title="Link to this heading">#</a></h2>
<p>All rocSPARSE library functions are non-blocking and execute asynchronously with respect to the host,
except for functions which allocate memory themselves, preventing asynchronicity.
These functions might return immediately or before the actual computation has finished.
To force synchronization, use either <a class="reference external" href="https://rocm.docs.amd.com/projects/HIP/en/latest/reference/hip_runtime_api/modules/device_management.html#_CPPv420hipDeviceSynchronizev" title="(in HIP Documentation v7.2.53211)"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipDeviceSynchronize()</span></code></a> or <a class="reference external" href="https://rocm.docs.amd.com/projects/HIP/en/latest/reference/hip_runtime_api/modules/stream_management.html#_CPPv420hipStreamSynchronize11hipStream_t" title="(in HIP Documentation v7.2.53211)"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipStreamSynchronize()</span></code></a>.
This ensures all previously executed rocSPARSE functions on the device or the stream have completed.</p>
</section>
<section id="multiple-streams-and-multiple-devices">
<h2>Multiple streams and multiple devices<a class="headerlink" href="#multiple-streams-and-multiple-devices" title="Link to this heading">#</a></h2>
<p>If a system has multiple HIP devices, you can run multiple rocSPARSE handles concurrently.
However, you <strong>cannot</strong> run a single rocSPARSE handle concurrently on multiple discrete devices.
Each handle can only be associated with a single device, and a new handle should be created for each additional device.</p>
</section>
<section id="graph-support-for-rocsparse">
<h2>Graph support for rocSPARSE<a class="headerlink" href="#graph-support-for-rocsparse" title="Link to this heading">#</a></h2>
<p>Many of the rocSPARSE functions can be captured into a graph node using the HIP Graph Management APIs. See <a class="reference internal" href="#functions-supported-with-graph-capture"><span class="std std-ref">Functions supported with graph capture</span></a> to determine
whether a rocSPARSE routine is supported or not. For a list of graph-related HIP APIs, see the <a class="reference external" href="https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#graph-management">HIP Graph Management API</a>.</p>
<p>The following code creates a graph with <code class="docutils literal notranslate"><span class="pre">rocsparse_function()</span></code> as the graph node.</p>
<div class="highlight-c++ notranslate"><div class="highlight"><pre><span></span><span class="n">CHECK_HIP_ERROR</span><span class="p">((</span><span class="n">hipStreamBeginCapture</span><span class="p">(</span><span class="n">stream</span><span class="p">,</span><span class="w"> </span><span class="n">hipStreamCaptureModeGlobal</span><span class="p">));</span>
<span class="n">rocsparse_</span><span class="o">&lt;</span><span class="n">function</span><span class="o">&gt;</span><span class="p">(</span><span class="o">&lt;</span><span class="n">arguments</span><span class="o">&gt;</span><span class="p">);</span>
<span class="n">CHECK_HIP_ERROR</span><span class="p">(</span><span class="n">hipStreamEndCapture</span><span class="p">(</span><span class="n">stream</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">graph</span><span class="p">));</span>
</pre></div>
</div>
<p>The captured graph can be launched as shown below:</p>
<div class="highlight-c++ notranslate"><div class="highlight"><pre><span></span><span class="n">CHECK_HIP_ERROR</span><span class="p">(</span><span class="n">hipGraphInstantiate</span><span class="p">(</span><span class="o">&amp;</span><span class="n">instance</span><span class="p">,</span><span class="w"> </span><span class="n">graph</span><span class="p">,</span><span class="w"> </span><span class="nb">NULL</span><span class="p">,</span><span class="w"> </span><span class="nb">NULL</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">));</span>
<span class="n">CHECK_HIP_ERROR</span><span class="p">(</span><span class="n">hipGraphLaunch</span><span class="p">(</span><span class="n">instance</span><span class="p">,</span><span class="w"> </span><span class="n">stream</span><span class="p">));</span>
</pre></div>
</div>
<p>Graph support requires asynchronous HIP APIs.</p>
</section>
<section id="functions-supported-with-graph-capture">
<span id="id1"></span><h2>Functions supported with graph capture<a class="headerlink" href="#functions-supported-with-graph-capture" title="Link to this heading">#</a></h2>
<p>The following functions support graph capture:</p>
<section id="sparse-level-1-functions">
<h3>Sparse level 1 functions<a class="headerlink" href="#sparse-level-1-functions" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Function name</p></th>
<th class="head"><p>yes</p></th>
<th class="head"><p>no</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/level1.html#_CPPv416rocsparse_saxpyi16rocsparse_handle13rocsparse_intPKfPKfPK13rocsparse_intPf20rocsparse_index_base" title="rocsparse_saxpyi"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xaxpyi()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/level1.html#_CPPv415rocsparse_sdoti16rocsparse_handle13rocsparse_intPKfPK13rocsparse_intPKfPf20rocsparse_index_base" title="rocsparse_sdoti"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xdoti()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/level1.html#_CPPv416rocsparse_cdotci16rocsparse_handle13rocsparse_intPK23rocsparse_float_complexPK13rocsparse_intPK23rocsparse_float_complexP23rocsparse_float_complex20rocsparse_index_base" title="rocsparse_cdotci"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xdotci()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/level1.html#_CPPv415rocsparse_sgthr16rocsparse_handle13rocsparse_intPKfPfPK13rocsparse_int20rocsparse_index_base" title="rocsparse_sgthr"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xgthr()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/level1.html#_CPPv416rocsparse_sgthrz16rocsparse_handle13rocsparse_intPfPfPK13rocsparse_int20rocsparse_index_base" title="rocsparse_sgthrz"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xgthrz()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/level1.html#_CPPv415rocsparse_sroti16rocsparse_handle13rocsparse_intPfPK13rocsparse_intPfPKfPKf20rocsparse_index_base" title="rocsparse_sroti"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xroti()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/level1.html#_CPPv415rocsparse_ssctr16rocsparse_handle13rocsparse_intPKfPK13rocsparse_intPf20rocsparse_index_base" title="rocsparse_ssctr"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xsctr()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="sparse-level-2-functions">
<h3>Sparse level 2 functions<a class="headerlink" href="#sparse-level-2-functions" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Function name</p></th>
<th class="head"><p>yes</p></th>
<th class="head"><p>no</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/level2.html#_CPPv425rocsparse_sbsrmv_analysis16rocsparse_handle19rocsparse_direction19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_info" title="rocsparse_sbsrmv_analysis"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xbsrmv_analysis()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/level2.html#_CPPv421rocsparse_bsrmv_clear16rocsparse_handle18rocsparse_mat_info" title="rocsparse_bsrmv_clear"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_bsrmv_clear()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/level2.html#_CPPv416rocsparse_sbsrmv16rocsparse_handle19rocsparse_direction19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_infoPKfPKfPf" title="rocsparse_sbsrmv"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xbsrmv()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/level2.html#_CPPv417rocsparse_sbsrxmv16rocsparse_handle19rocsparse_direction19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intPK13rocsparse_intPK13rocsparse_int13rocsparse_intPKfPKfPf" title="rocsparse_sbsrxmv"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xbsrxmv()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/level2.html#_CPPv428rocsparse_sbsrsv_buffer_size16rocsparse_handle19rocsparse_direction19rocsparse_operation13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_infoP6size_t" title="rocsparse_sbsrsv_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xbsrsv_buffer_size()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/level2.html#_CPPv425rocsparse_sbsrsv_analysis16rocsparse_handle19rocsparse_direction19rocsparse_operation13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv" title="rocsparse_sbsrsv_analysis"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xbsrsv_analysis()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/level2.html#_CPPv426rocsparse_bsrsv_zero_pivot16rocsparse_handle18rocsparse_mat_infoP13rocsparse_int" title="rocsparse_bsrsv_zero_pivot"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_bsrsv_zero_pivot()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/level2.html#_CPPv421rocsparse_bsrsv_clear16rocsparse_handle18rocsparse_mat_info" title="rocsparse_bsrsv_clear"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_bsrsv_clear()</span></code></a></p></td>
<td></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/level2.html#_CPPv422rocsparse_sbsrsv_solve16rocsparse_handle19rocsparse_direction19rocsparse_operation13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_infoPKfPf22rocsparse_solve_policyPv" title="rocsparse_sbsrsv_solve"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xbsrsv_solve()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/level2.html#_CPPv416rocsparse_scoomv16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intPKfPKfPf" title="rocsparse_scoomv"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcoomv()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/level2.html#_CPPv425rocsparse_scsrmv_analysis16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_info" title="rocsparse_scsrmv_analysis"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcsrmv_analysis()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/level2.html#_CPPv416rocsparse_scsrmv16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoPKfPKfPf" title="rocsparse_scsrmv"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcsrmv()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/level2.html#_CPPv421rocsparse_csrmv_clear16rocsparse_handle18rocsparse_mat_info" title="rocsparse_csrmv_clear"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_csrmv_clear()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/level2.html#_CPPv428rocsparse_scsrsv_buffer_size16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoP6size_t" title="rocsparse_scsrsv_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcsrsv_buffer_size()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/level2.html#_CPPv425rocsparse_scsrsv_analysis16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv" title="rocsparse_scsrsv_analysis"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcsrsv_analysis()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/level2.html#_CPPv426rocsparse_csrsv_zero_pivot16rocsparse_handleK19rocsparse_mat_descr18rocsparse_mat_infoP13rocsparse_int" title="rocsparse_csrsv_zero_pivot"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_csrsv_zero_pivot()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/level2.html#_CPPv421rocsparse_csrsv_clear16rocsparse_handleK19rocsparse_mat_descr18rocsparse_mat_info" title="rocsparse_csrsv_clear"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_csrsv_clear()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/level2.html#_CPPv422rocsparse_scsrsv_solve16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoPKfPf22rocsparse_solve_policyPv" title="rocsparse_scsrsv_solve"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcsrsv_solve()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/level2.html#_CPPv430rocsparse_scsritsv_buffer_size16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoP6size_t" title="rocsparse_scsritsv_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcsritsv_buffer_size()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/level2.html#_CPPv427rocsparse_scsritsv_analysis16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv" title="rocsparse_scsritsv_analysis"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcsritsv_analysis()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/level2.html#_CPPv428rocsparse_csritsv_zero_pivot16rocsparse_handleK19rocsparse_mat_descr18rocsparse_mat_infoP13rocsparse_int" title="rocsparse_csritsv_zero_pivot"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_csritsv_zero_pivot()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/level2.html#_CPPv423rocsparse_csritsv_clear16rocsparse_handleK19rocsparse_mat_descr18rocsparse_mat_info" title="rocsparse_csritsv_clear"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_csritsv_clear()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/level2.html#_CPPv424rocsparse_scsritsv_solve16rocsparse_handleP13rocsparse_intPKfPf19rocsparse_operation13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoPKfPf22rocsparse_solve_policyPv" title="rocsparse_scsritsv_solve"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcsritsv_solve()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcsritsv_solve()</span></code></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/level2.html#_CPPv416rocsparse_sellmv16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_int13rocsparse_intPKfPKfPf" title="rocsparse_sellmv"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xellmv()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/level2.html#_CPPv418rocsparse_sgebsrmv16rocsparse_handle19rocsparse_direction19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intPKfPKfPf" title="rocsparse_sgebsrmv"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xgebsrmv()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/level2.html#_CPPv428rocsparse_sgemvi_buffer_size16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intP6size_t" title="rocsparse_sgemvi_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xgemvi_buffer_size()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/level2.html#_CPPv416rocsparse_sgemvi16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_intPKfPKf13rocsparse_int13rocsparse_intPKfPK13rocsparse_intPKfPf20rocsparse_index_basePv" title="rocsparse_sgemvi"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xgemvi()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/level2.html#_CPPv416rocsparse_shybmv16rocsparse_handle19rocsparse_operationPKfK19rocsparse_mat_descrK17rocsparse_hyb_matPKfPKfPf" title="rocsparse_shybmv"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xhybmv()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="sparse-level-3-functions">
<h3>Sparse level 3 functions<a class="headerlink" href="#sparse-level-3-functions" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Function name</p></th>
<th class="head"><p>yes</p></th>
<th class="head"><p>no</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/level3.html#_CPPv416rocsparse_scsrmm16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intPKf13rocsparse_intPKfPf13rocsparse_int" title="rocsparse_scsrmm"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcsrmm()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/level3.html#_CPPv428rocsparse_scsrsm_buffer_size16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intPKf13rocsparse_int18rocsparse_mat_info22rocsparse_solve_policyP6size_t" title="rocsparse_scsrsm_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcsrsm_buffer_size()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/level3.html#_CPPv425rocsparse_scsrsm_analysis16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intPKf13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv" title="rocsparse_scsrsm_analysis"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcsrsm_analysis()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/level3.html#_CPPv426rocsparse_csrsm_zero_pivot16rocsparse_handle18rocsparse_mat_infoP13rocsparse_int" title="rocsparse_csrsm_zero_pivot"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_csrsm_zero_pivot()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/level3.html#_CPPv421rocsparse_csrsm_clear16rocsparse_handle18rocsparse_mat_info" title="rocsparse_csrsm_clear"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_csrsm_clear()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/level3.html#_CPPv422rocsparse_scsrsm_solve16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intPf13rocsparse_int18rocsparse_mat_info22rocsparse_solve_policyPv" title="rocsparse_scsrsm_solve"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcsrsm_solve()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/level3.html#_CPPv416rocsparse_sbsrmm16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_intPKf13rocsparse_intPKfPf13rocsparse_int" title="rocsparse_sbsrmm"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xbsrmm()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/level3.html#_CPPv428rocsparse_sbsrsm_buffer_size16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_infoP6size_t" title="rocsparse_sbsrsm_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xbsrsm_buffer_size()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/level3.html#_CPPv425rocsparse_sbsrsm_analysis16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv" title="rocsparse_sbsrsm_analysis"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xbsrsm_analysis()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/level3.html#_CPPv426rocsparse_bsrsm_zero_pivot16rocsparse_handle18rocsparse_mat_infoP13rocsparse_int" title="rocsparse_bsrsm_zero_pivot"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_bsrsm_zero_pivot()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/level3.html#_CPPv421rocsparse_bsrsm_clear16rocsparse_handle18rocsparse_mat_info" title="rocsparse_bsrsm_clear"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_bsrsm_clear()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/level3.html#_CPPv422rocsparse_sbsrsm_solve16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_infoPKf13rocsparse_intPf13rocsparse_int22rocsparse_solve_policyPv" title="rocsparse_sbsrsm_solve"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xbsrsm_solve()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/level3.html#_CPPv418rocsparse_sgebsrmm16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intPKf13rocsparse_intPKfPf13rocsparse_int" title="rocsparse_sgebsrmm"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xgebsrmm()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/level3.html#_CPPv416rocsparse_sgemmi16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPKfPKf13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intPKfPf13rocsparse_int" title="rocsparse_sgemmi"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xgemmi()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="sparse-extra-functions">
<h3>Sparse extra functions<a class="headerlink" href="#sparse-extra-functions" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Function name</p></th>
<th class="head"><p>yes</p></th>
<th class="head"><p>no</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/extra.html#_CPPv422rocsparse_bsrgeam_nnzb16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descrP13rocsparse_intP13rocsparse_int" title="rocsparse_bsrgeam_nnzb"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_bsrgeam_nnzb()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/extra.html#_CPPv418rocsparse_sbsrgeam16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descr13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_intPKfK19rocsparse_mat_descr13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descrPfPK13rocsparse_intP13rocsparse_int" title="rocsparse_sbsrgeam"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xbsrgeam()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/extra.html#_CPPv430rocsparse_sbsrgemm_buffer_size16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intPKfK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoP6size_t" title="rocsparse_sbsrgemm_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xbsrgemm_buffer_size()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/extra.html#_CPPv422rocsparse_bsrgemm_nnzb16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descrP13rocsparse_intP13rocsparse_intK18rocsparse_mat_infoPv" title="rocsparse_bsrgemm_nnzb"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_bsrgemm_nnzb()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/extra.html#_CPPv418rocsparse_sbsrgemm16rocsparse_handle19rocsparse_direction19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descr13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_intPKfK19rocsparse_mat_descr13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descrPfPK13rocsparse_intP13rocsparse_intK18rocsparse_mat_infoPv" title="rocsparse_sbsrgemm"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xbsrgemm()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/extra.html#_CPPv421rocsparse_csrgeam_nnz16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descrP13rocsparse_intP13rocsparse_int" title="rocsparse_csrgeam_nnz"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_csrgeam_nnz()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/extra.html#_CPPv418rocsparse_scsrgeam16rocsparse_handle13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descr13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_intPKfK19rocsparse_mat_descr13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descrPfPK13rocsparse_intP13rocsparse_int" title="rocsparse_scsrgeam"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcsrgeam()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/extra.html#_CPPv430rocsparse_scsrgemm_buffer_size16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intPKfK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoP6size_t" title="rocsparse_scsrgemm_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcsrgemm_buffer_size()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/extra.html#_CPPv421rocsparse_csrgemm_nnz16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descrP13rocsparse_intP13rocsparse_intK18rocsparse_mat_infoPv" title="rocsparse_csrgemm_nnz"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_csrgemm_nnz()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/extra.html#_CPPv426rocsparse_csrgemm_symbolic16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intP13rocsparse_intK18rocsparse_mat_infoPv" title="rocsparse_csrgemm_symbolic"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_csrgemm_symbolic()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/extra.html#_CPPv418rocsparse_scsrgemm16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descr13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_intPKfK19rocsparse_mat_descr13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descrPfPK13rocsparse_intP13rocsparse_intK18rocsparse_mat_infoPv" title="rocsparse_scsrgemm"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcsrgemm()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/extra.html#_CPPv426rocsparse_scsrgemm_numeric16rocsparse_handle19rocsparse_operation19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descr13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_intPKfK19rocsparse_mat_descr13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPfPK13rocsparse_intPK13rocsparse_intK18rocsparse_mat_infoPv" title="rocsparse_scsrgemm_numeric"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcsrgemm_numeric()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="preconditioner-functions">
<h3>Preconditioner functions<a class="headerlink" href="#preconditioner-functions" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Function name</p></th>
<th class="head"><p>yes</p></th>
<th class="head"><p>no</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/precond.html#_CPPv429rocsparse_sbsric0_buffer_size16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_infoP6size_t" title="rocsparse_sbsric0_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xbsric0_buffer_size()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/precond.html#_CPPv426rocsparse_sbsric0_analysis16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv" title="rocsparse_sbsric0_analysis"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xbsric0_analysis()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/precond.html#_CPPv427rocsparse_bsric0_zero_pivot16rocsparse_handle18rocsparse_mat_infoP13rocsparse_int" title="rocsparse_bsric0_zero_pivot"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_bsric0_zero_pivot()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/precond.html#_CPPv422rocsparse_bsric0_clear16rocsparse_handle18rocsparse_mat_info" title="rocsparse_bsric0_clear"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_bsric0_clear()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/precond.html#_CPPv417rocsparse_sbsric016rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPfPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_info22rocsparse_solve_policyPv" title="rocsparse_sbsric0"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xbsric0()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/precond.html#_CPPv430rocsparse_sbsrilu0_buffer_size16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_infoP6size_t" title="rocsparse_sbsrilu0_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xbsrilu0_buffer_size()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/precond.html#_CPPv427rocsparse_sbsrilu0_analysis16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv" title="rocsparse_sbsrilu0_analysis"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xbsrilu0_analysis()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/precond.html#_CPPv428rocsparse_bsrilu0_zero_pivot16rocsparse_handle18rocsparse_mat_infoP13rocsparse_int" title="rocsparse_bsrilu0_zero_pivot"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_bsrilu0_zero_pivot()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/precond.html#_CPPv432rocsparse_sbsrilu0_numeric_boost16rocsparse_handle18rocsparse_mat_infoiPKfPKf" title="rocsparse_sbsrilu0_numeric_boost"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xbsrilu0_numeric_boost()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/precond.html#_CPPv423rocsparse_bsrilu0_clear16rocsparse_handle18rocsparse_mat_info" title="rocsparse_bsrilu0_clear"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_bsrilu0_clear()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/precond.html#_CPPv418rocsparse_sbsrilu016rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPfPK13rocsparse_intPK13rocsparse_int13rocsparse_int18rocsparse_mat_info22rocsparse_solve_policyPv" title="rocsparse_sbsrilu0"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xbsrilu0()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/precond.html#_CPPv429rocsparse_scsric0_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoP6size_t" title="rocsparse_scsric0_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcsric0_buffer_size()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/precond.html#_CPPv426rocsparse_scsric0_analysis16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv" title="rocsparse_scsric0_analysis"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcsric0_analysis()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/precond.html#_CPPv427rocsparse_csric0_zero_pivot16rocsparse_handle18rocsparse_mat_infoP13rocsparse_int" title="rocsparse_csric0_zero_pivot"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_csric0_zero_pivot()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/precond.html#_CPPv422rocsparse_csric0_clear16rocsparse_handle18rocsparse_mat_info" title="rocsparse_csric0_clear"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_csric0_clear()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/precond.html#_CPPv417rocsparse_scsric016rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPfPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_info22rocsparse_solve_policyPv" title="rocsparse_scsric0"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcsric0()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/precond.html#_CPPv430rocsparse_scsrilu0_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoP6size_t" title="rocsparse_scsrilu0_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcsrilu0_buffer_size()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/precond.html#_CPPv432rocsparse_scsrilu0_numeric_boost16rocsparse_handle18rocsparse_mat_infoiPKfPKf" title="rocsparse_scsrilu0_numeric_boost"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcsrilu0_numeric_boost()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/precond.html#_CPPv427rocsparse_scsrilu0_analysis16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_info25rocsparse_analysis_policy22rocsparse_solve_policyPv" title="rocsparse_scsrilu0_analysis"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcsrilu0_analysis()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/precond.html#_CPPv428rocsparse_csrilu0_zero_pivot16rocsparse_handle18rocsparse_mat_infoP13rocsparse_int" title="rocsparse_csrilu0_zero_pivot"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_csrilu0_zero_pivot()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/precond.html#_CPPv423rocsparse_csrilu0_clear16rocsparse_handle18rocsparse_mat_info" title="rocsparse_csrilu0_clear"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_csrilu0_clear()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/precond.html#_CPPv418rocsparse_scsrilu016rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPfPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_info22rocsparse_solve_policyPv" title="rocsparse_scsrilu0"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcsrilu0()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/precond.html#_CPPv431rocsparse_csritilu0_buffer_size16rocsparse_handle20rocsparse_itilu0_alg13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base18rocsparse_datatypeP6size_t" title="rocsparse_csritilu0_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_csritilu0_buffer_size()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/precond.html#_CPPv430rocsparse_csritilu0_preprocess16rocsparse_handle20rocsparse_itilu0_alg13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base18rocsparse_datatype6size_tPv" title="rocsparse_csritilu0_preprocess"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_csritilu0_preprocess()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/precond.html#_CPPv428rocsparse_scsritilu0_compute16rocsparse_handle20rocsparse_itilu0_alg13rocsparse_intP13rocsparse_intf13rocsparse_int13rocsparse_intPK13rocsparse_intPK13rocsparse_intPKfPf20rocsparse_index_base6size_tPv" title="rocsparse_scsritilu0_compute"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcsritilu0_compute()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/precond.html#_CPPv431rocsparse_scsritilu0_compute_ex16rocsparse_handle20rocsparse_itilu0_alg13rocsparse_intP13rocsparse_int13rocsparse_intf13rocsparse_int13rocsparse_intPK13rocsparse_intPK13rocsparse_intPKfPf20rocsparse_index_base6size_tPv" title="rocsparse_scsritilu0_compute_ex"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcsritilu0_compute_ex()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/precond.html#_CPPv428rocsparse_scsritilu0_history16rocsparse_handle20rocsparse_itilu0_algP13rocsparse_intPf6size_tPv" title="rocsparse_scsritilu0_history"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcsritilu0_history()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/precond.html#_CPPv427rocsparse_sgtsv_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_intPKfPKfPKfPKf13rocsparse_intP6size_t" title="rocsparse_sgtsv_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xgtsv_buffer_size()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/precond.html#_CPPv415rocsparse_sgtsv16rocsparse_handle13rocsparse_int13rocsparse_intPKfPKfPKfPf13rocsparse_intPv" title="rocsparse_sgtsv"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xgtsv()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/precond.html#_CPPv436rocsparse_sgtsv_no_pivot_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_intPKfPKfPKfPKf13rocsparse_intP6size_t" title="rocsparse_sgtsv_no_pivot_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xgtsv_no_pivot_buffer_size()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/precond.html#_CPPv424rocsparse_sgtsv_no_pivot16rocsparse_handle13rocsparse_int13rocsparse_intPKfPKfPKfPf13rocsparse_intPv" title="rocsparse_sgtsv_no_pivot"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xgtsv_no_pivot()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/precond.html#_CPPv450rocsparse_sgtsv_no_pivot_strided_batch_buffer_size16rocsparse_handle13rocsparse_intPKfPKfPKfPKf13rocsparse_int13rocsparse_intP6size_t" title="rocsparse_sgtsv_no_pivot_strided_batch_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xgtsv_no_pivot_strided_batch_buffer_size()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/precond.html#_CPPv438rocsparse_sgtsv_no_pivot_strided_batch16rocsparse_handle13rocsparse_intPKfPKfPKfPf13rocsparse_int13rocsparse_intPv" title="rocsparse_sgtsv_no_pivot_strided_batch"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xgtsv_no_pivot_strided_batch()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/precond.html#_CPPv445rocsparse_sgtsv_interleaved_batch_buffer_size16rocsparse_handle30rocsparse_gtsv_interleaved_alg13rocsparse_intPKfPKfPKfPKf13rocsparse_int13rocsparse_intP6size_t" title="rocsparse_sgtsv_interleaved_batch_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xgtsv_interleaved_batch_buffer_size()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/precond.html#_CPPv433rocsparse_sgtsv_interleaved_batch16rocsparse_handle30rocsparse_gtsv_interleaved_alg13rocsparse_intPfPfPfPf13rocsparse_int13rocsparse_intPv" title="rocsparse_sgtsv_interleaved_batch"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xgtsv_interleaved_batch()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/precond.html#_CPPv445rocsparse_sgpsv_interleaved_batch_buffer_size16rocsparse_handle30rocsparse_gpsv_interleaved_alg13rocsparse_intPKfPKfPKfPKfPKfPKf13rocsparse_int13rocsparse_intP6size_t" title="rocsparse_sgpsv_interleaved_batch_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xgpsv_interleaved_batch_buffer_size()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/precond.html#_CPPv433rocsparse_sgpsv_interleaved_batch16rocsparse_handle30rocsparse_gpsv_interleaved_alg13rocsparse_intPfPfPfPfPfPf13rocsparse_int13rocsparse_intPv" title="rocsparse_sgpsv_interleaved_batch"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xgpsv_interleaved_batch()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="conversion-functions">
<h3>Conversion functions<a class="headerlink" href="#conversion-functions" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Function name</p></th>
<th class="head"><p>yes</p></th>
<th class="head"><p>no</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv417rocsparse_csr2coo16rocsparse_handlePK13rocsparse_int13rocsparse_int13rocsparse_intP13rocsparse_int20rocsparse_index_base" title="rocsparse_csr2coo"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_csr2coo()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv429rocsparse_csr2csc_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPK13rocsparse_intPK13rocsparse_int16rocsparse_actionP6size_t" title="rocsparse_csr2csc_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_csr2csc_buffer_size()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv418rocsparse_scsr2csc16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_intPfP13rocsparse_intP13rocsparse_int16rocsparse_action20rocsparse_index_basePv" title="rocsparse_scsr2csc"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcsr2csc()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv434rocsparse_sgebsr2gebsc_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intP6size_t" title="rocsparse_sgebsr2gebsc_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xgebsr2gebsc_buffer_size()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv422rocsparse_sgebsr2gebsc16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intPfP13rocsparse_intP13rocsparse_int16rocsparse_action20rocsparse_index_basePv" title="rocsparse_sgebsr2gebsc"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xgebsr2gebsc()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv423rocsparse_csr2ell_width16rocsparse_handle13rocsparse_intK19rocsparse_mat_descrPK13rocsparse_intK19rocsparse_mat_descrP13rocsparse_int" title="rocsparse_csr2ell_width"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_csr2ell_width()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv418rocsparse_scsr2ell16rocsparse_handle13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPfP13rocsparse_int" title="rocsparse_scsr2ell"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcsr2ell()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv418rocsparse_scsr2hyb16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int17rocsparse_hyb_mat13rocsparse_int23rocsparse_hyb_partition" title="rocsparse_scsr2hyb"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcsr2hyb()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv421rocsparse_csr2bsr_nnz16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK13rocsparse_intPK13rocsparse_int13rocsparse_intK19rocsparse_mat_descrP13rocsparse_intP13rocsparse_int" title="rocsparse_csr2bsr_nnz"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_csr2bsr_nnz()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv418rocsparse_scsr2bsr16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPfP13rocsparse_intP13rocsparse_int" title="rocsparse_scsr2bsr"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcsr2bsr()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv423rocsparse_csr2gebsr_nnz16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descrP13rocsparse_int13rocsparse_int13rocsparse_intP13rocsparse_intPv" title="rocsparse_csr2gebsr_nnz"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_csr2gebsr_nnz()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv432rocsparse_scsr2gebsr_buffer_size16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intP6size_t" title="rocsparse_scsr2gebsr_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcsr2gebsr_buffer_size()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv420rocsparse_scsr2gebsr16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descrPfP13rocsparse_intP13rocsparse_int13rocsparse_int13rocsparse_intPv" title="rocsparse_scsr2gebsr"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcsr2gebsr()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv417rocsparse_coo2csr16rocsparse_handlePK13rocsparse_int13rocsparse_int13rocsparse_intP13rocsparse_int20rocsparse_index_base" title="rocsparse_coo2csr"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_coo2csr()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv421rocsparse_ell2csr_nnz16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPK13rocsparse_intK19rocsparse_mat_descrP13rocsparse_intP13rocsparse_int" title="rocsparse_ell2csr_nnz"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_ell2csr_nnz()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv418rocsparse_sell2csr16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descr13rocsparse_intPKfPK13rocsparse_intK19rocsparse_mat_descrPfPK13rocsparse_intP13rocsparse_int" title="rocsparse_sell2csr"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xell2csr()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv429rocsparse_hyb2csr_buffer_size16rocsparse_handleK19rocsparse_mat_descrK17rocsparse_hyb_matPK13rocsparse_intP6size_t" title="rocsparse_hyb2csr_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_hyb2csr_buffer_size()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv418rocsparse_shyb2csr16rocsparse_handleK19rocsparse_mat_descrK17rocsparse_hyb_matPfP13rocsparse_intP13rocsparse_intPv" title="rocsparse_shyb2csr"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xhyb2csr()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv418rocsparse_sbsr2csr16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPfP13rocsparse_intP13rocsparse_int" title="rocsparse_sbsr2csr"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xbsr2csr()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv420rocsparse_sgebsr2csr16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPfP13rocsparse_intP13rocsparse_int" title="rocsparse_sgebsr2csr"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xgebsr2csr()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv434rocsparse_sgebsr2gebsr_buffer_size16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intP6size_t" title="rocsparse_sgebsr2gebsr_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xgebsr2gebsr_buffer_size()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv425rocsparse_gebsr2gebsr_nnz16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrP13rocsparse_int13rocsparse_int13rocsparse_intP13rocsparse_intPv" title="rocsparse_gebsr2gebsr_nnz"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_gebsr2gebsr_nnz()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv422rocsparse_sgebsr2gebsr16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPfP13rocsparse_intP13rocsparse_int13rocsparse_int13rocsparse_intPv" title="rocsparse_sgebsr2gebsr"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xgebsr2gebsr()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv427rocsparse_scsr2csr_compress16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int13rocsparse_intPK13rocsparse_intPfP13rocsparse_intP13rocsparse_intf" title="rocsparse_scsr2csr_compress"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcsr2csr_compress()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv437rocsparse_create_identity_permutation16rocsparse_handle13rocsparse_intP13rocsparse_int" title="rocsparse_create_identity_permutation"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_create_identity_permutation()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv429rocsparse_inverse_permutation16rocsparse_handle13rocsparse_intPK13rocsparse_intP13rocsparse_int20rocsparse_index_base" title="rocsparse_inverse_permutation"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_inverse_permutation()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv429rocsparse_cscsort_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPK13rocsparse_intPK13rocsparse_intP6size_t" title="rocsparse_cscsort_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_cscsort_buffer_size()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv417rocsparse_cscsort16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK13rocsparse_intP13rocsparse_intP13rocsparse_intPv" title="rocsparse_cscsort"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_cscsort()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv429rocsparse_csrsort_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPK13rocsparse_intPK13rocsparse_intP6size_t" title="rocsparse_csrsort_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_csrsort_buffer_size()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv417rocsparse_csrsort16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPK13rocsparse_intP13rocsparse_intP13rocsparse_intPv" title="rocsparse_csrsort"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_csrsort()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv429rocsparse_coosort_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPK13rocsparse_intPK13rocsparse_intP6size_t" title="rocsparse_coosort_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_coosort_buffer_size()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv424rocsparse_coosort_by_row16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intP13rocsparse_intP13rocsparse_intP13rocsparse_intPv" title="rocsparse_coosort_by_row"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_coosort_by_row()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv427rocsparse_coosort_by_column16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intP13rocsparse_intP13rocsparse_intP13rocsparse_intPv" title="rocsparse_coosort_by_column"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_coosort_by_column()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv420rocsparse_sdense2csr16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKf13rocsparse_intPK13rocsparse_intPfP13rocsparse_intP13rocsparse_int" title="rocsparse_sdense2csr"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xdense2csr()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv420rocsparse_sdense2csc16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKf13rocsparse_intPK13rocsparse_intPfP13rocsparse_intP13rocsparse_int" title="rocsparse_sdense2csc"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xdense2csc()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv420rocsparse_sdense2coo16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKf13rocsparse_intPK13rocsparse_intPfP13rocsparse_intP13rocsparse_int" title="rocsparse_sdense2coo"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xdense2coo()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv420rocsparse_scsr2dense16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intPf13rocsparse_int" title="rocsparse_scsr2dense"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcsr2dense()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv420rocsparse_scsc2dense16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intPf13rocsparse_int" title="rocsparse_scsc2dense"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcsc2dense()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv420rocsparse_scoo2dense16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intPf13rocsparse_int" title="rocsparse_scoo2dense"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcoo2dense()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv423rocsparse_snnz_compress16rocsparse_handle13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intP13rocsparse_intP13rocsparse_intf" title="rocsparse_snnz_compress"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xnnz_compress()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv414rocsparse_snnz16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKf13rocsparse_intP13rocsparse_intP13rocsparse_int" title="rocsparse_snnz"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xnnz()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv438rocsparse_sprune_dense2csr_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_intPKf13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intP6size_t" title="rocsparse_sprune_dense2csr_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xprune_dense2csr_buffer_size()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv430rocsparse_sprune_dense2csr_nnz16rocsparse_handle13rocsparse_int13rocsparse_intPKf13rocsparse_intPKfK19rocsparse_mat_descrP13rocsparse_intP13rocsparse_intPv" title="rocsparse_sprune_dense2csr_nnz"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xprune_dense2csr_nnz()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv426rocsparse_sprune_dense2csr16rocsparse_handle13rocsparse_int13rocsparse_intPKf13rocsparse_intPKfK19rocsparse_mat_descrPfPK13rocsparse_intP13rocsparse_intPv" title="rocsparse_sprune_dense2csr"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xprune_dense2csr()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv436rocsparse_sprune_csr2csr_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intP6size_t" title="rocsparse_sprune_csr2csr_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xprune_csr2csr_buffer_size()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv428rocsparse_sprune_csr2csr_nnz16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intPKfK19rocsparse_mat_descrP13rocsparse_intP13rocsparse_intPv" title="rocsparse_sprune_csr2csr_nnz"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xprune_csr2csr_nnz()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv424rocsparse_sprune_csr2csr16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intPKfK19rocsparse_mat_descrPfPK13rocsparse_intP13rocsparse_intPv" title="rocsparse_sprune_csr2csr"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xprune_csr2csr()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv452rocsparse_sprune_dense2csr_by_percentage_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_intPKf13rocsparse_intfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoP6size_t" title="rocsparse_sprune_dense2csr_by_percentage_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xprune_dense2csr_by_percentage_buffer_size()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv444rocsparse_sprune_dense2csr_nnz_by_percentage16rocsparse_handle13rocsparse_int13rocsparse_intPKf13rocsparse_intfK19rocsparse_mat_descrP13rocsparse_intP13rocsparse_int18rocsparse_mat_infoPv" title="rocsparse_sprune_dense2csr_nnz_by_percentage"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xprune_dense2csr_nnz_by_percentage()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv440rocsparse_sprune_dense2csr_by_percentage16rocsparse_handle13rocsparse_int13rocsparse_intPKf13rocsparse_intfK19rocsparse_mat_descrPfPK13rocsparse_intP13rocsparse_int18rocsparse_mat_infoPv" title="rocsparse_sprune_dense2csr_by_percentage"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xprune_dense2csr_by_percentage()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv450rocsparse_sprune_csr2csr_by_percentage_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoP6size_t" title="rocsparse_sprune_csr2csr_by_percentage_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xprune_csr2csr_by_percentage_buffer_size()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv442rocsparse_sprune_csr2csr_nnz_by_percentage16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intfK19rocsparse_mat_descrP13rocsparse_intP13rocsparse_int18rocsparse_mat_infoPv" title="rocsparse_sprune_csr2csr_nnz_by_percentage"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xprune_csr2csr_nnz_by_percentage()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv438rocsparse_sprune_csr2csr_by_percentage16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intfK19rocsparse_mat_descrPfPK13rocsparse_intP13rocsparse_int18rocsparse_mat_infoPv" title="rocsparse_sprune_csr2csr_by_percentage"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xprune_csr2csr_by_percentage()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/conversion.html#_CPPv423rocsparse_sbsrpad_value16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intfK19rocsparse_mat_descrPfPK13rocsparse_intPK13rocsparse_int" title="rocsparse_sbsrpad_value"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xbsrpad_value()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="reordering-functions">
<h3>Reordering functions<a class="headerlink" href="#reordering-functions" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Function name</p></th>
<th class="head"><p>yes</p></th>
<th class="head"><p>no</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/reorder.html#_CPPv419rocsparse_scsrcolor16rocsparse_handle13rocsparse_int13rocsparse_intK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intPKfP13rocsparse_intP13rocsparse_intP13rocsparse_int18rocsparse_mat_info" title="rocsparse_scsrcolor"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcsrcolor()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="utility-functions">
<h3>Utility functions<a class="headerlink" href="#utility-functions" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Function name</p></th>
<th class="head"><p>yes</p></th>
<th class="head"><p>no</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/utility.html#_CPPv439rocsparse_scheck_matrix_csr_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP6size_t" title="rocsparse_scheck_matrix_csr_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcheck_matrix_csr_buffer_size()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/utility.html#_CPPv427rocsparse_scheck_matrix_csr16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP21rocsparse_data_statusPv" title="rocsparse_scheck_matrix_csr"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcheck_matrix_csr()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/utility.html#_CPPv439rocsparse_scheck_matrix_csc_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP6size_t" title="rocsparse_scheck_matrix_csc_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcheck_matrix_csc_buffer_size()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/utility.html#_CPPv427rocsparse_scheck_matrix_csc16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP21rocsparse_data_statusPv" title="rocsparse_scheck_matrix_csc"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcheck_matrix_csc()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/utility.html#_CPPv439rocsparse_scheck_matrix_coo_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP6size_t" title="rocsparse_scheck_matrix_coo_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcheck_matrix_coo_buffer_size()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/utility.html#_CPPv427rocsparse_scheck_matrix_coo16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP21rocsparse_data_statusPv" title="rocsparse_scheck_matrix_coo"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcheck_matrix_coo()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/utility.html#_CPPv441rocsparse_scheck_matrix_gebsr_buffer_size16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP6size_t" title="rocsparse_scheck_matrix_gebsr_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcheck_matrix_gebsr_buffer_size()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/utility.html#_CPPv429rocsparse_scheck_matrix_gebsr16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP21rocsparse_data_statusPv" title="rocsparse_scheck_matrix_gebsr"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcheck_matrix_gebsr()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/utility.html#_CPPv441rocsparse_scheck_matrix_gebsc_buffer_size16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP6size_t" title="rocsparse_scheck_matrix_gebsc_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcheck_matrix_gebsc_buffer_size()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/utility.html#_CPPv429rocsparse_scheck_matrix_gebsc16rocsparse_handle19rocsparse_direction13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_int13rocsparse_intPKfPK13rocsparse_intPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP21rocsparse_data_statusPv" title="rocsparse_scheck_matrix_gebsc"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcheck_matrix_gebsc()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/utility.html#_CPPv439rocsparse_scheck_matrix_ell_buffer_size16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPKfPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP6size_t" title="rocsparse_scheck_matrix_ell_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcheck_matrix_ell_buffer_size()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/utility.html#_CPPv427rocsparse_scheck_matrix_ell16rocsparse_handle13rocsparse_int13rocsparse_int13rocsparse_intPKfPK13rocsparse_int20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP21rocsparse_data_statusPv" title="rocsparse_scheck_matrix_ell"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_Xcheck_matrix_ell()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/utility.html#_CPPv438rocsparse_check_matrix_hyb_buffer_size16rocsparse_handleK17rocsparse_hyb_mat20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP6size_t" title="rocsparse_check_matrix_hyb_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_check_matrix_hyb_buffer_size()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/utility.html#_CPPv426rocsparse_check_matrix_hyb16rocsparse_handleK17rocsparse_hyb_mat20rocsparse_index_base21rocsparse_matrix_type19rocsparse_fill_mode22rocsparse_storage_modeP21rocsparse_data_statusPv" title="rocsparse_check_matrix_hyb"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_check_matrix_hyb()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="sparse-generic-functions">
<h3>Sparse generic functions<a class="headerlink" href="#sparse-generic-functions" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Function name</p></th>
<th class="head"><p>yes</p></th>
<th class="head"><p>no</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/generic.html#_CPPv415rocsparse_axpby16rocsparse_handlePKv27rocsparse_const_spvec_descrPKv21rocsparse_dnvec_descr" title="rocsparse_axpby"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_axpby()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/generic.html#_CPPv416rocsparse_gather16rocsparse_handle27rocsparse_const_dnvec_descr21rocsparse_spvec_descr" title="rocsparse_gather"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_gather()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/generic.html#_CPPv417rocsparse_scatter16rocsparse_handle27rocsparse_const_spvec_descr21rocsparse_dnvec_descr" title="rocsparse_scatter"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_scatter()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/generic.html#_CPPv413rocsparse_rot16rocsparse_handlePKvPKv21rocsparse_spvec_descr21rocsparse_dnvec_descr" title="rocsparse_rot"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_rot()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/generic.html#_CPPv414rocsparse_spvv16rocsparse_handle19rocsparse_operation27rocsparse_const_spvec_descr27rocsparse_const_dnvec_descrPv18rocsparse_datatypeP6size_tPv" title="rocsparse_spvv"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_spvv()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/generic.html#_CPPv425rocsparse_sparse_to_dense16rocsparse_handle27rocsparse_const_spmat_descr21rocsparse_dnmat_descr29rocsparse_sparse_to_dense_algP6size_tPv" title="rocsparse_sparse_to_dense"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_sparse_to_dense()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/generic.html#_CPPv425rocsparse_dense_to_sparse16rocsparse_handle27rocsparse_const_dnmat_descr21rocsparse_spmat_descr29rocsparse_dense_to_sparse_algP6size_tPv" title="rocsparse_dense_to_sparse"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_dense_to_sparse()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/generic.html#_CPPv416rocsparse_spgemm16rocsparse_handle19rocsparse_operation19rocsparse_operationPKv27rocsparse_const_spmat_descr27rocsparse_const_spmat_descrPKv27rocsparse_const_spmat_descr21rocsparse_spmat_descr18rocsparse_datatype20rocsparse_spgemm_alg22rocsparse_spgemm_stageP6size_tPv" title="rocsparse_spgemm"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_spgemm()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/generic.html#_CPPv429rocsparse_v2_spmv_buffer_size16rocsparse_handle20rocsparse_spmv_descr27rocsparse_const_spmat_descr27rocsparse_const_dnvec_descr27rocsparse_const_dnvec_descr23rocsparse_v2_spmv_stageP6size_tP15rocsparse_error" title="rocsparse_v2_spmv_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_v2_spmv_buffer_size()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/generic.html#_CPPv428rocsparse_spgeam_buffer_size16rocsparse_handle22rocsparse_spgeam_descr27rocsparse_const_spmat_descr27rocsparse_const_spmat_descr27rocsparse_const_spmat_descr22rocsparse_spgeam_stageP6size_tP15rocsparse_error" title="rocsparse_spgeam_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_spgeam_buffer_size()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/generic.html#_CPPv416rocsparse_spgeam16rocsparse_handle22rocsparse_spgeam_descr27rocsparse_const_spmat_descr27rocsparse_const_spmat_descr21rocsparse_spmat_descr22rocsparse_spgeam_stage6size_tPvP15rocsparse_error" title="rocsparse_spgeam"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_spgeam()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/generic.html#_CPPv428rocsparse_sptrsv_buffer_size16rocsparse_handle22rocsparse_sptrsv_descr27rocsparse_const_spmat_descr27rocsparse_const_dnvec_descr27rocsparse_const_dnvec_descr22rocsparse_sptrsv_stageP6size_tP15rocsparse_error" title="rocsparse_sptrsv_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_sptrsv_buffer_size()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/generic.html#_CPPv428rocsparse_sptrsm_buffer_size16rocsparse_handle22rocsparse_sptrsm_descr27rocsparse_const_spmat_descr27rocsparse_const_dnmat_descr27rocsparse_const_dnmat_descr22rocsparse_sptrsm_stageP6size_tP15rocsparse_error" title="rocsparse_sptrsm_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_sptrsm_buffer_size()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/generic.html#_CPPv427rocsparse_sddmm_buffer_size16rocsparse_handle19rocsparse_operation19rocsparse_operationPKv27rocsparse_const_dnmat_descr27rocsparse_const_dnmat_descrPKv21rocsparse_spmat_descr18rocsparse_datatype19rocsparse_sddmm_algP6size_t" title="rocsparse_sddmm_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_sddmm_buffer_size()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/generic.html#_CPPv426rocsparse_sddmm_preprocess16rocsparse_handle19rocsparse_operation19rocsparse_operationPKv27rocsparse_const_dnmat_descr27rocsparse_const_dnmat_descrPKv21rocsparse_spmat_descr18rocsparse_datatype19rocsparse_sddmm_algPv" title="rocsparse_sddmm_preprocess"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_sddmm_preprocess()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/generic.html#_CPPv438rocsparse_sparse_to_sparse_buffer_size16rocsparse_handle32rocsparse_sparse_to_sparse_descr27rocsparse_const_spmat_descr21rocsparse_spmat_descr32rocsparse_sparse_to_sparse_stageP6size_t" title="rocsparse_sparse_to_sparse_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_sparse_to_sparse_buffer_size()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/generic.html#_CPPv426rocsparse_sparse_to_sparse16rocsparse_handle32rocsparse_sparse_to_sparse_descr27rocsparse_const_spmat_descr21rocsparse_spmat_descr32rocsparse_sparse_to_sparse_stage6size_tPv" title="rocsparse_sparse_to_sparse"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_sparse_to_sparse()</span></code></a></p></td>
<td></td>
<td><p>x</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/generic.html#_CPPv429rocsparse_extract_buffer_size16rocsparse_handle23rocsparse_extract_descr27rocsparse_const_spmat_descr21rocsparse_spmat_descr23rocsparse_extract_stageP6size_t" title="rocsparse_extract_buffer_size"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_extract_buffer_size()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../reference/generic.html#_CPPv421rocsparse_extract_nnz16rocsparse_handle23rocsparse_extract_descrP7int64_t" title="rocsparse_extract_nnz"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_extract_nnz()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../reference/generic.html#_CPPv417rocsparse_extract16rocsparse_handle23rocsparse_extract_descr27rocsparse_const_spmat_descr21rocsparse_spmat_descr23rocsparse_extract_stage6size_tPv" title="rocsparse_extract"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_extract()</span></code></a></p></td>
<td><p>x</p></td>
<td></td>
</tr>
</tbody>
</table>
</div>
<p>For <a class="reference internal" href="../reference/generic.html#_CPPv414rocsparse_spmv16rocsparse_handle19rocsparse_operationPKv27rocsparse_const_spmat_descr27rocsparse_const_dnvec_descrPKvK21rocsparse_dnvec_descr18rocsparse_datatype18rocsparse_spmv_alg20rocsparse_spmv_stageP6size_tPv" title="rocsparse_spmv"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_spmv()</span></code></a>, <a class="reference internal" href="../reference/generic.html#_CPPv414rocsparse_spmm16rocsparse_handle19rocsparse_operation19rocsparse_operationPKv27rocsparse_const_spmat_descr27rocsparse_const_dnmat_descrPKvK21rocsparse_dnmat_descr18rocsparse_datatype18rocsparse_spmm_alg20rocsparse_spmm_stageP6size_tPv" title="rocsparse_spmm"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_spmm()</span></code></a>, <a class="reference internal" href="../reference/generic.html#_CPPv414rocsparse_spsv16rocsparse_handle19rocsparse_operationPKv27rocsparse_const_spmat_descr27rocsparse_const_dnvec_descrK21rocsparse_dnvec_descr18rocsparse_datatype18rocsparse_spsv_alg20rocsparse_spsv_stageP6size_tPv" title="rocsparse_spsv"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_spsv()</span></code></a>, and <a class="reference internal" href="../reference/generic.html#_CPPv414rocsparse_spsm16rocsparse_handle19rocsparse_operation19rocsparse_operationPKv27rocsparse_const_spmat_descr27rocsparse_const_dnmat_descrK21rocsparse_dnmat_descr18rocsparse_datatype18rocsparse_spsm_alg20rocsparse_spsm_stageP6size_tPv" title="rocsparse_spsm"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_spsm()</span></code></a>,
<code class="docutils literal notranslate"><span class="pre">hipGraph</span></code> is supported when passing the buffer size or compute stages but is not supported when passing the preprocess stage.</p>
<p>For <a class="reference internal" href="../reference/generic.html#_CPPv417rocsparse_v2_spmv16rocsparse_handle20rocsparse_spmv_descrPKv27rocsparse_const_spmat_descr27rocsparse_const_dnvec_descrPKv21rocsparse_dnvec_descr23rocsparse_v2_spmv_stage6size_tPvP15rocsparse_error" title="rocsparse_v2_spmv"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_v2_spmv()</span></code></a>, <code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_v2_sptrsv()</span></code>, and <code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_v2_sptrsm()</span></code>,
<code class="docutils literal notranslate"><span class="pre">hipGraph</span></code> is supported when passing the compute stage but is not supported when passing the analysis stage.</p>
<p>For <a class="reference internal" href="../reference/generic.html#_CPPv415rocsparse_sddmm16rocsparse_handle19rocsparse_operation19rocsparse_operationPKv27rocsparse_const_dnmat_descr27rocsparse_const_dnmat_descrPKv21rocsparse_spmat_descr18rocsparse_datatype19rocsparse_sddmm_algPv" title="rocsparse_sddmm"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_sddmm()</span></code></a>, <code class="docutils literal notranslate"><span class="pre">hipGraph</span></code> is supported only when using the default algorithm.</p>
</section>
</section>
<section id="storage-formats">
<h2>Storage formats<a class="headerlink" href="#storage-formats" title="Link to this heading">#</a></h2>
<p>For information on the rocSPARSE sparse array storage formats,
see <a class="reference internal" href="../conceptual/storage-formats-sparse.html"><span class="doc">storage formats</span></a>.</p>
</section>
<section id="pointer-mode">
<h2>Pointer mode<a class="headerlink" href="#pointer-mode" title="Link to this heading">#</a></h2>
<p>The auxiliary functions <a class="reference internal" href="../reference/auxiliary.html#_CPPv426rocsparse_set_pointer_mode16rocsparse_handle22rocsparse_pointer_mode" title="rocsparse_set_pointer_mode"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_set_pointer_mode()</span></code></a> and <a class="reference internal" href="../reference/auxiliary.html#_CPPv426rocsparse_get_pointer_mode16rocsparse_handleP22rocsparse_pointer_mode" title="rocsparse_get_pointer_mode"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_get_pointer_mode()</span></code></a>
are used to set and get the value of the state variable <a class="reference internal" href="../reference/enumerations.html#_CPPv422rocsparse_pointer_mode" title="rocsparse_pointer_mode"><code class="xref cpp cpp-enum docutils literal notranslate"><span class="pre">rocsparse_pointer_mode</span></code></a>.
If <a class="reference internal" href="../reference/enumerations.html#_CPPv422rocsparse_pointer_mode" title="rocsparse_pointer_mode"><code class="xref cpp cpp-enum docutils literal notranslate"><span class="pre">rocsparse_pointer_mode</span></code></a> is equal to <a class="reference internal" href="../reference/enumerations.html#_CPPv4N22rocsparse_pointer_mode27rocsparse_pointer_mode_hostE" title="rocsparse_pointer_mode_host"><code class="xref cpp cpp-enumerator docutils literal notranslate"><span class="pre">rocsparse_pointer_mode_host</span></code></a>,
then scalar parameters must be allocated on the host.
If <a class="reference internal" href="../reference/enumerations.html#_CPPv422rocsparse_pointer_mode" title="rocsparse_pointer_mode"><code class="xref cpp cpp-enum docutils literal notranslate"><span class="pre">rocsparse_pointer_mode</span></code></a> is equal to <a class="reference internal" href="../reference/enumerations.html#_CPPv4N22rocsparse_pointer_mode29rocsparse_pointer_mode_deviceE" title="rocsparse_pointer_mode_device"><code class="xref cpp cpp-enumerator docutils literal notranslate"><span class="pre">rocsparse_pointer_mode_device</span></code></a>,
then scalar parameters must be allocated on the device.</p>
<p>There are two types of scalar parameter:</p>
<ol class="arabic simple">
<li><p>Scaling parameters, such as <code class="docutils literal notranslate"><span class="pre">alpha</span></code> and <code class="docutils literal notranslate"><span class="pre">beta</span></code>, used, for example, in <a class="reference internal" href="../reference/level2.html#_CPPv416rocsparse_scsrmv16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_int18rocsparse_mat_infoPKfPKfPf" title="rocsparse_scsrmv"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_scsrmv()</span></code></a> and <a class="reference internal" href="../reference/level2.html#_CPPv416rocsparse_scoomv16rocsparse_handle19rocsparse_operation13rocsparse_int13rocsparse_int13rocsparse_intPKfK19rocsparse_mat_descrPKfPK13rocsparse_intPK13rocsparse_intPKfPKfPf" title="rocsparse_scoomv"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_scoomv()</span></code></a>.</p></li>
<li><p>Scalar results from functions such as <a class="reference internal" href="../reference/level1.html#_CPPv415rocsparse_sdoti16rocsparse_handle13rocsparse_intPKfPK13rocsparse_intPKfPf20rocsparse_index_base" title="rocsparse_sdoti"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_sdoti()</span></code></a> or <a class="reference internal" href="../reference/level1.html#_CPPv416rocsparse_cdotci16rocsparse_handle13rocsparse_intPK23rocsparse_float_complexPK13rocsparse_intPK23rocsparse_float_complexP23rocsparse_float_complex20rocsparse_index_base" title="rocsparse_cdotci"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">rocsparse_cdotci()</span></code></a>.</p></li>
</ol>
<p>For scalar parameters such as <code class="docutils literal notranslate"><span class="pre">alpha</span></code> and <code class="docutils literal notranslate"><span class="pre">beta</span></code>, memory can be allocated on the host heap or stack
when <a class="reference internal" href="../reference/enumerations.html#_CPPv422rocsparse_pointer_mode" title="rocsparse_pointer_mode"><code class="xref cpp cpp-enum docutils literal notranslate"><span class="pre">rocsparse_pointer_mode</span></code></a> is equal to <a class="reference internal" href="../reference/enumerations.html#_CPPv4N22rocsparse_pointer_mode27rocsparse_pointer_mode_hostE" title="rocsparse_pointer_mode_host"><code class="xref cpp cpp-enumerator docutils literal notranslate"><span class="pre">rocsparse_pointer_mode_host</span></code></a>.
The kernel launch is asynchronous, and if the scalar parameter is on the heap, it can be freed after the kernel launch returns.
When <a class="reference internal" href="../reference/enumerations.html#_CPPv422rocsparse_pointer_mode" title="rocsparse_pointer_mode"><code class="xref cpp cpp-enum docutils literal notranslate"><span class="pre">rocsparse_pointer_mode</span></code></a> is equal to <a class="reference internal" href="../reference/enumerations.html#_CPPv4N22rocsparse_pointer_mode29rocsparse_pointer_mode_deviceE" title="rocsparse_pointer_mode_device"><code class="xref cpp cpp-enumerator docutils literal notranslate"><span class="pre">rocsparse_pointer_mode_device</span></code></a>,
the scalar parameter must not be changed until the kernel completes.</p>
<p>For scalar results, when <a class="reference internal" href="../reference/enumerations.html#_CPPv422rocsparse_pointer_mode" title="rocsparse_pointer_mode"><code class="xref cpp cpp-enum docutils literal notranslate"><span class="pre">rocsparse_pointer_mode</span></code></a> is equal to <a class="reference internal" href="../reference/enumerations.html#_CPPv4N22rocsparse_pointer_mode27rocsparse_pointer_mode_hostE" title="rocsparse_pointer_mode_host"><code class="xref cpp cpp-enumerator docutils literal notranslate"><span class="pre">rocsparse_pointer_mode_host</span></code></a>,
the function blocks the CPU until the GPU has copied the result back to the host.
When <a class="reference internal" href="../reference/enumerations.html#_CPPv422rocsparse_pointer_mode" title="rocsparse_pointer_mode"><code class="xref cpp cpp-enum docutils literal notranslate"><span class="pre">rocsparse_pointer_mode</span></code></a> is equal to <a class="reference internal" href="../reference/enumerations.html#_CPPv4N22rocsparse_pointer_mode29rocsparse_pointer_mode_deviceE" title="rocsparse_pointer_mode_device"><code class="xref cpp cpp-enumerator docutils literal notranslate"><span class="pre">rocsparse_pointer_mode_device</span></code></a>,
the function returns after the asynchronous launch.
Similar to the vector and matrix results, the scalar result is only available when the kernel has completed execution.</p>
</section>
<section id="activity-logging-deprecated">
<span id="rocsparse-logging"></span><h2>Activity logging [Deprecated]<a class="headerlink" href="#activity-logging-deprecated" title="Link to this heading">#</a></h2>
<p>Four different environment variables can be set to enable logging in rocSPARSE:
<code class="docutils literal notranslate"><span class="pre">ROCSPARSE_LAYER</span></code>, <code class="docutils literal notranslate"><span class="pre">ROCSPARSE_LOG_TRACE_PATH</span></code>, <code class="docutils literal notranslate"><span class="pre">ROCSPARSE_LOG_BENCH_PATH</span></code>, and <code class="docutils literal notranslate"><span class="pre">ROCSPARSE_LOG_DEBUG_PATH</span></code>.</p>
<p><code class="docutils literal notranslate"><span class="pre">ROCSPARSE_LAYER</span></code> is a bit mask that enables logging, where several logging modes for <a class="reference internal" href="../reference/enumerations.html#rocsparse-layer-mode"><span class="std std-ref">rocsparse_layer_mode</span></a>
can be specified as follows:</p>
<div class="pst-scrollable-table-container"><table class="table">
<tbody>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">ROCSPARSE_LAYER</span></code> not set</p></td>
<td><p>Logging is disabled.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">ROCSPARSE_LAYER</span></code> set to <code class="docutils literal notranslate"><span class="pre">1</span></code></p></td>
<td><p>Trace logging is enabled.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">ROCSPARSE_LAYER</span></code> set to <code class="docutils literal notranslate"><span class="pre">2</span></code></p></td>
<td><p>Bench logging is enabled.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">ROCSPARSE_LAYER</span></code> set to <code class="docutils literal notranslate"><span class="pre">3</span></code></p></td>
<td><p>Trace logging and bench logging are enabled.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">ROCSPARSE_LAYER</span></code> set to <code class="docutils literal notranslate"><span class="pre">4</span></code></p></td>
<td><p>Debug logging is enabled.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">ROCSPARSE_LAYER</span></code> set to <code class="docutils literal notranslate"><span class="pre">5</span></code></p></td>
<td><p>Trace logging and debug logging are enabled.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">ROCSPARSE_LAYER</span></code> set to <code class="docutils literal notranslate"><span class="pre">6</span></code></p></td>
<td><p>Bench logging and debug logging are enabled.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">ROCSPARSE_LAYER</span></code> set to <code class="docutils literal notranslate"><span class="pre">7</span></code></p></td>
<td><p>Trace logging and bench logging and debug logging are enabled.</p></td>
</tr>
</tbody>
</table>
</div>
<p>When logging is enabled, each rocSPARSE function call writes the function name and function arguments to the logging stream.
The default logging output is streamed to <code class="docutils literal notranslate"><span class="pre">stderr</span></code>.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Performance will degrade when logging is enabled. By default, the environment variable <code class="docutils literal notranslate"><span class="pre">ROCSPARSE_LAYER</span></code> is not set and
logging is disabled.</p>
</div>
<p>To capture activity logging in a file, set the following environment variables as required:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ROCSPARSE_LOG_TRACE_PATH</span></code> specifies a path and file name to capture trace logging streamed to that file.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ROCSPARSE_LOG_BENCH_PATH</span></code> specifies a path and file name to capture bench logging.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ROCSPARSE_LOG_DEBUG_PATH</span></code> specifies a path and file name to capture debug logging.</p></li>
</ul>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>If the file cannot be opened, the logging output is streamed to <code class="docutils literal notranslate"><span class="pre">stderr</span></code>.</p>
</div>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>Trace, debug, and bench logging is deprecated and will be removed in a future release</p>
</div>
</section>
<section id="roc-tx-support-in-rocsparse">
<h2>ROC-TX support in rocSPARSE<a class="headerlink" href="#roc-tx-support-in-rocsparse" title="Link to this heading">#</a></h2>
<p>The <a class="reference external" href="https://rocm.docs.amd.com/projects/roctracer/en/latest/reference/roctx-spec.html">ROC-TX</a> library contains application code
instrumentation APIs to support the high-level correlation of runtime API or activity events. When integrated with rocSPARSE, ROC-TX
enables users to view the call stack of rocSPARSE and HIP API functions in profiling tools such as <a class="reference external" href="https://rocm.docs.amd.com/projects/rocprofiler/en/latest/index.html" title="(in rocprofiler Documentation v2.0.0)"><span class="xref std std-doc">rocProfiler</span></a>, offering better insights
into runtime behavior and performance bottlenecks.</p>
<p>To enable ROC-TX profiling, set the environment variable <code class="docutils literal notranslate"><span class="pre">ROCSPARSE_ROCTX=1</span></code> when running the program with rocProf:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span><span class="nv">ROCSPARSE_ROCTX</span><span class="o">=</span><span class="m">1</span><span class="w"> </span>/opt/rocm/bin/rocprofv3<span class="w"> </span>--kernel-trace<span class="w"> </span>--marker-trace<span class="w"> </span>--hip-trace<span class="w"> </span>--output-format<span class="w"> </span>pftrace<span class="w"> </span>--<span class="w"> </span>./example_program
</pre></div>
</div>
<p>This will generate a <code class="docutils literal notranslate"><span class="pre">.pftrace</span></code> file which can then be viewed using the <a class="reference external" href="https://ui.perfetto.dev/">Perfetto UI</a>.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>ROC-TX support in rocSPARSE is unavailable on Windows and is not supported in the static library version on Linux.</p>
</div>
</section>
<section id="rocsparse-fortran-bindings">
<h2>rocSPARSE Fortran bindings<a class="headerlink" href="#rocsparse-fortran-bindings" title="Link to this heading">#</a></h2>
<p>Fortran functionality for rocSPARSE is offered by <a class="reference external" href="https://rocm.docs.amd.com/projects/hipfort/en/latest/index.html" title="(in hipfort Documentation v0.7.1)"><span class="xref std std-doc">hipFORT</span></a>. For more information,
consult the <a class="reference external" href="https://rocm.docs.amd.com/projects/hipfort/en/latest/doxygen/html/files.html" title="(in hipfort Documentation v0.7.1)"><span class="xref std std-doc">hipFORT API file list</span></a>.</p>
</section>
<section id="hipsparse">
<h2>hipSPARSE<a class="headerlink" href="#hipsparse" title="Link to this heading">#</a></h2>
<p><a class="reference external" href="https://rocm.docs.amd.com/projects/hipSPARSE/en/latest/index.html" title="(in hipSPARSE Documentation v4.2.0)"><span class="xref std std-doc">hipSPARSE</span></a> is a SPARSE marshalling library with multiple supported backends.
It sits between the application and a “worker”
SPARSE library, marshalling inputs into the backend library and marshalling results back to the application. hipSPARSE exports
an interface that does not require the client to change, regardless of the chosen backend.
hipSPARSE supports rocSPARSE and NVIDIA CUDA cuSPARSE as backends.</p>
<p>hipSPARSE focuses on convenience and portability.
If performance outweighs these factors, then it’s best to use rocSPARSE itself.
hipSPARSE can be found on <a class="reference external" href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipsparse">GitHub</a>.</p>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="../conceptual/storage-formats-sparse.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">rocSPARSE storage formats</p>
      </div>
    </a>
    <a class="right-next"
       href="../reference/reference.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">rocSPARSE API reference guide</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-device-management">HIP device management</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-stream-management">HIP stream management</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#asynchronous-execution">Asynchronous execution</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#multiple-streams-and-multiple-devices">Multiple streams and multiple devices</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#graph-support-for-rocsparse">Graph support for rocSPARSE</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#functions-supported-with-graph-capture">Functions supported with graph capture</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#sparse-level-1-functions">Sparse level 1 functions</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#sparse-level-2-functions">Sparse level 2 functions</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#sparse-level-3-functions">Sparse level 3 functions</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#sparse-extra-functions">Sparse extra functions</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#preconditioner-functions">Preconditioner functions</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#conversion-functions">Conversion functions</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#reordering-functions">Reordering functions</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#utility-functions">Utility functions</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#sparse-generic-functions">Sparse generic functions</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#storage-formats">Storage formats</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#pointer-mode">Pointer mode</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#activity-logging-deprecated">Activity logging [Deprecated]</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#roc-tx-support-in-rocsparse">ROC-TX support in rocSPARSE</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsparse-fortran-bindings">rocSPARSE Fortran bindings</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsparse">hipSPARSE</a></li>
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
