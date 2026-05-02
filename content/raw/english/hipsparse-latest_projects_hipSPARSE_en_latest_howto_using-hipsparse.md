---
title: "Using hipSPARSE &#8212; hipSPARSE 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipSPARSE/en/latest/howto/using-hipsparse.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:09:29.251379+00:00
content_hash: "976c02e06185e2be"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="rocSPARSE usage guide and documentation" name="description" />
<meta content="rocSPARSE, ROCm, API, documentation, usage guide, device management, stream management, storage format, pointer mode" name="keywords" />

    <title>Using hipSPARSE &#8212; hipSPARSE 4.2.0 Documentation</title>
  
  
  
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
    <script>window.MathJax = {"options": {"processHtmlClass": "tex2jax_process|mathjax_process|math|output_area"}}</script>
    <script defer="defer" src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <script>DOCUMENTATION_OPTIONS.pagename = 'howto/using-hipsparse';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />
    <link rel="next" title="hipSPARSE API reference guide" href="../reference/reference.html" />
    <link rel="prev" title="Installing and building hipSPARSE for Microsoft Windows" href="../install/install-windows.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hipsparse" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/howto/using-hipsparse.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
  
  
  
  
  
  
    <p class="title logo__title">hipSPARSE 4.2.0 Documentation</p>
  
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
<li class="toctree-l1"><a class="reference internal" href="../what-is-hipsparse.html">What is hipSPARSE?</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Install</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../install/install.html">Linux installation guide</a></li>
<li class="toctree-l1"><a class="reference internal" href="../install/install-windows.html">Windows installation guide</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">How to</span></p>
<ul class="current nav bd-sidenav">
<li class="toctree-l1 current active"><a class="current reference internal" href="#">Use hipSPARSE</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Examples</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference external" href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipsparse/clients/samples">Client samples</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Examples</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1 has-children"><a class="reference internal" href="../reference/reference.html">API reference</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2"><a class="reference internal" href="../reference/api.html">Exported functions</a></li>
<li class="toctree-l2"><a class="reference internal" href="../reference/types.html">hipSPARSE data types</a></li>
<li class="toctree-l2"><a class="reference internal" href="../reference/precision.html">hipSPARSE precision support</a></li>
<li class="toctree-l2"><a class="reference internal" href="../reference/auxiliary.html">Sparse auxiliary functions</a></li>
<li class="toctree-l2"><a class="reference internal" href="../reference/level1.html">Sparse level 1 functions</a></li>
<li class="toctree-l2"><a class="reference internal" href="../reference/level2.html">Sparse level 2 functions</a></li>
<li class="toctree-l2"><a class="reference internal" href="../reference/level3.html">Sparse level 3 functions</a></li>
<li class="toctree-l2"><a class="reference internal" href="../reference/extra.html">Sparse extra functions</a></li>
<li class="toctree-l2"><a class="reference internal" href="../reference/precond.html">Preconditioner functions</a></li>
<li class="toctree-l2"><a class="reference internal" href="../reference/conversion.html">Sparse conversion functions</a></li>
<li class="toctree-l2"><a class="reference internal" href="../reference/reorder.html">Sparse reordering functions</a></li>
<li class="toctree-l2"><a class="reference internal" href="../reference/generic.html">Sparse generic functions</a></li>
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
    <li class="breadcrumb-item active" aria-current="page"><span class="ellipsis">Using hipSPARSE</span></li>
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
    <h1>Using hipSPARSE</h1>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#interface-examples">Interface examples</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#storage-formats">Storage formats</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#coo-storage-format">COO storage format</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#coo-aos-storage-format">COO (AoS) storage format</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#csr-storage-format">CSR storage format</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#csc-storage-format">CSC storage format</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#bsr-storage-format">BSR storage format</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#gebsr-storage-format">GEBSR storage format</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#ell-storage-format">ELL storage format</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hyb-storage-format">HYB storage format</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#storage-schemes-and-indexing-base">Storage schemes and indexing base</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#pointer-mode">Pointer mode</a></li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="using-hipsparse">
<span id="hipsparse-docs"></span><h1>Using hipSPARSE<a class="headerlink" href="#using-hipsparse" title="Link to this heading">#</a></h1>
<p>This topic discusses how to use hipSPARSE, including a discussion of device and stream
management, storage formats, and pointer mode.</p>
<section id="hip-device-management">
<h2>HIP device management<a class="headerlink" href="#hip-device-management" title="Link to this heading">#</a></h2>
<p>Before starting a HIP kernel, you can call <a class="reference external" href="https://rocm.docs.amd.com/projects/HIP/en/latest/reference/hip_runtime_api/modules/device_management.html#_CPPv412hipSetDevicei" title="(in HIP Documentation v7.2.53211)"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipSetDevice()</span></code></a> to set a device.
The system uses the default device if you don’t call the function. Unless you explicitly
call <a class="reference external" href="https://rocm.docs.amd.com/projects/HIP/en/latest/reference/hip_runtime_api/modules/device_management.html#_CPPv412hipSetDevicei" title="(in HIP Documentation v7.2.53211)"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipSetDevice()</span></code></a> to specify another device, HIP kernels are always launched on device <code class="docutils literal notranslate"><span class="pre">0</span></code>.
This HIP (and CUDA) device management approach is not specific to the hipSPARSE library.
hipSPARSE honors this approach and assumes you have already set the preferred device before a hipSPARSE routine call.</p>
<p>After you set the device, you can create a handle with <a class="reference internal" href="../reference/auxiliary.html#hipsparse-create-handle"><span class="std std-ref">hipsparseCreate()</span></a>.
Subsequent hipSPARSE routines take this handle as an input parameter.
hipSPARSE only queries the specified device (using <a class="reference external" href="https://rocm.docs.amd.com/projects/HIP/en/latest/reference/hip_runtime_api/modules/device_management.html#_CPPv412hipGetDevicePi" title="(in HIP Documentation v7.2.53211)"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipGetDevice()</span></code></a>).
You are responsible for providing a valid device to hipSPARSE and ensuring device safety.
If it’s not a valid device, hipSPARSE returns an error message.</p>
<p>To change to another device, you must destroy the current handle using <a class="reference internal" href="../reference/auxiliary.html#hipsparse-destroy-handle"><span class="std std-ref">hipsparseDestroy()</span></a>,
then create another handle using <a class="reference internal" href="../reference/auxiliary.html#hipsparse-create-handle"><span class="std std-ref">hipsparseCreate()</span></a>, specifying another device.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p><a class="reference external" href="https://rocm.docs.amd.com/projects/HIP/en/latest/reference/hip_runtime_api/modules/device_management.html#_CPPv412hipSetDevicei" title="(in HIP Documentation v7.2.53211)"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipSetDevice()</span></code></a> and <a class="reference external" href="https://rocm.docs.amd.com/projects/HIP/en/latest/reference/hip_runtime_api/modules/device_management.html#_CPPv412hipGetDevicePi" title="(in HIP Documentation v7.2.53211)"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipGetDevice()</span></code></a> are not part of the hipSPARSE API.
They are part of the <a class="reference external" href="https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___device.html">HIP runtime API for device management</a>.</p>
</div>
</section>
<section id="hip-stream-management">
<h2>HIP stream management<a class="headerlink" href="#hip-stream-management" title="Link to this heading">#</a></h2>
<p>HIP kernels are always launched in a queue (also known as a stream). If you don’t explicitly specify a stream,
the system provides and maintains a default stream, which you cannot create or destroy.
However, you can freely create new streams (using <a class="reference external" href="https://rocm.docs.amd.com/projects/HIP/en/latest/reference/hip_runtime_api/modules/stream_management.html#_CPPv415hipStreamCreateP11hipStream_t" title="(in HIP Documentation v7.2.53211)"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipStreamCreate()</span></code></a>) and bind them to the
hipSPARSE handle using <a class="reference internal" href="../reference/auxiliary.html#hipsparse-set-stream"><span class="std std-ref">hipsparseSetStream()</span></a>. The hipSPARSE routines invoke HIP kernels.
A hipSPARSE handle is always associated with a stream, which hipSPARSE passes to the kernels inside the routine.
One hipSPARSE routine only takes one stream in a single invocation.
If you create a stream, you are responsible for destroying it.
See the <a class="reference external" href="https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___stream.html">HIP stream management API</a> for more information.</p>
</section>
<section id="asynchronous-execution">
<h2>Asynchronous execution<a class="headerlink" href="#asynchronous-execution" title="Link to this heading">#</a></h2>
<p>Except for functions that allocate memory themselves, preventing asynchronicity,
all hipSPARSE library functions are non-blocking and execute asynchronously with respect to the host,
unless otherwise stated. These functions might return before the actual computation has finished.
To force synchronization, use either <a class="reference external" href="https://rocm.docs.amd.com/projects/HIP/en/latest/reference/hip_runtime_api/modules/device_management.html#_CPPv420hipDeviceSynchronizev" title="(in HIP Documentation v7.2.53211)"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipDeviceSynchronize()</span></code></a> or <a class="reference external" href="https://rocm.docs.amd.com/projects/HIP/en/latest/reference/hip_runtime_api/modules/stream_management.html#_CPPv420hipStreamSynchronize11hipStream_t" title="(in HIP Documentation v7.2.53211)"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipStreamSynchronize()</span></code></a>.
This ensures that all previously executed hipSPARSE functions on the device or stream have been completed.</p>
</section>
<section id="multiple-streams-and-multiple-devices">
<h2>Multiple streams and multiple devices<a class="headerlink" href="#multiple-streams-and-multiple-devices" title="Link to this heading">#</a></h2>
<p>If a system has multiple HIP devices, you can run multiple hipSPARSE handles concurrently.
However, you cannot run a single hipSPARSE handle on different discrete devices
because each handle is associated with a particular device. A new handle must be created for each additional device.</p>
</section>
<section id="interface-examples">
<h2>Interface examples<a class="headerlink" href="#interface-examples" title="Link to this heading">#</a></h2>
<p>The hipSPARSE interface is compatible with the <a class="reference external" href="https://rocm.docs.amd.com/projects/rocSPARSE/en/latest/index.html" title="(in rocSPARSE Documentation v4.2.0)"><span class="xref std std-doc">rocSPARSE</span></a> and NVIDIA CUDA cuSPARSE-v2 APIs.
Porting a CUDA application that calls the CUDA cuSPARSE API to an application that calls the hipSPARSE API
is relatively straightforward. For example, the hipSPARSE SCSRMV API interface is as follows:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipsparseStatus_t</span>
<span class="nf">hipsparseScsrmv</span><span class="p">(</span><span class="n">hipsparseHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">               </span><span class="n">hipsparseOperation_t</span><span class="w"> </span><span class="n">transA</span><span class="p">,</span>
<span class="w">               </span><span class="kt">int</span><span class="w"> </span><span class="n">m</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">n</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">nnz</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="kt">float</span><span class="w"> </span><span class="o">*</span><span class="n">alpha</span><span class="p">,</span>
<span class="w">               </span><span class="k">const</span><span class="w"> </span><span class="n">hipsparseMatDescr_t</span><span class="w"> </span><span class="n">descrA</span><span class="p">,</span>
<span class="w">               </span><span class="k">const</span><span class="w"> </span><span class="kt">float</span><span class="w"> </span><span class="o">*</span><span class="n">csrValA</span><span class="p">,</span>
<span class="w">               </span><span class="k">const</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">csrRowPtrA</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">csrColIndA</span><span class="p">,</span>
<span class="w">               </span><span class="k">const</span><span class="w"> </span><span class="kt">float</span><span class="w"> </span><span class="o">*</span><span class="n">x</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="kt">float</span><span class="w"> </span><span class="o">*</span><span class="n">beta</span><span class="p">,</span>
<span class="w">               </span><span class="kt">float</span><span class="w"> </span><span class="o">*</span><span class="n">y</span><span class="p">);</span>
</pre></div>
</div>
<p>hipSPARSE assumes matrix <code class="docutils literal notranslate"><span class="pre">A</span></code> and vectors <code class="docutils literal notranslate"><span class="pre">x</span></code> and <code class="docutils literal notranslate"><span class="pre">y</span></code> are allocated in the GPU memory space and filled with data.
You are responsible for copying data to and from the host and device memory.</p>
</section>
<section id="storage-formats">
<h2>Storage formats<a class="headerlink" href="#storage-formats" title="Link to this heading">#</a></h2>
<p>This section describes the supported matrix storage formats.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The different storage formats support indexing with a base of 0 or 1, as described in <a class="reference internal" href="#index-base"><span class="std std-ref">Storage schemes and indexing base</span></a>.</p>
</div>
<section id="coo-storage-format">
<h3>COO storage format<a class="headerlink" href="#coo-storage-format" title="Link to this heading">#</a></h3>
<p>The Coordinate (COO) storage format represents an <span class="math notranslate nohighlight">\(m \times n\)</span> matrix by:</p>
<div class="pst-scrollable-table-container"><table class="table">
<tbody>
<tr class="row-odd"><td><p>m</p></td>
<td><p>Number of rows (integer).</p></td>
</tr>
<tr class="row-even"><td><p>n</p></td>
<td><p>Number of columns (integer).</p></td>
</tr>
<tr class="row-odd"><td><p>nnz</p></td>
<td><p>Number of non-zero elements (integer).</p></td>
</tr>
<tr class="row-even"><td><p>coo_val</p></td>
<td><p>Array of <code class="docutils literal notranslate"><span class="pre">nnz</span></code> elements containing the data (floating point).</p></td>
</tr>
<tr class="row-odd"><td><p>coo_row_ind</p></td>
<td><p>Array of <code class="docutils literal notranslate"><span class="pre">nnz</span></code> elements containing the row indices (integer).</p></td>
</tr>
<tr class="row-even"><td><p>coo_col_ind</p></td>
<td><p>Array of <code class="docutils literal notranslate"><span class="pre">nnz</span></code> elements containing the column indices (integer).</p></td>
</tr>
</tbody>
</table>
</div>
<p>The COO matrix is expected to be sorted by row indices and column indices per row.
Furthermore, each pair of indices should appear only once.
Consider the following <span class="math notranslate nohighlight">\(3 \times 5\)</span> matrix and the corresponding COO structures,
with <span class="math notranslate nohighlight">\(m = 3, n = 5\)</span> and <span class="math notranslate nohighlight">\(\text{nnz} = 8\)</span> using zero-based indexing:</p>
<div class="math notranslate nohighlight">
\[\begin{split}A = \begin{pmatrix}
      1.0 &amp; 2.0 &amp; 0.0 &amp; 3.0 &amp; 0.0 \\
      0.0 &amp; 4.0 &amp; 5.0 &amp; 0.0 &amp; 0.0 \\
      6.0 &amp; 0.0 &amp; 0.0 &amp; 7.0 &amp; 8.0 \\
    \end{pmatrix}\end{split}\]</div>
<p>where</p>
<div class="math notranslate nohighlight">
\[\begin{split}\begin{array}{ll}
  \text{coo_val}[8] &amp; = \{1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0\} \\
  \text{coo_row_ind}[8] &amp; = \{0, 0, 0, 1, 1, 2, 2, 2\} \\
  \text{coo_col_ind}[8] &amp; = \{0, 1, 3, 1, 2, 0, 3, 4\}
\end{array}\end{split}\]</div>
</section>
<section id="coo-aos-storage-format">
<h3>COO (AoS) storage format<a class="headerlink" href="#coo-aos-storage-format" title="Link to this heading">#</a></h3>
<p>The Coordinate (COO) Array of Structure (AoS) storage format represents an <span class="math notranslate nohighlight">\(m \times n\)</span> matrix by:</p>
<div class="pst-scrollable-table-container"><table class="table">
<tbody>
<tr class="row-odd"><td><p>m</p></td>
<td><p>Number of rows (integer).</p></td>
</tr>
<tr class="row-even"><td><p>n</p></td>
<td><p>Number of columns (integer).</p></td>
</tr>
<tr class="row-odd"><td><p>nnz</p></td>
<td><p>Number of non-zero elements (integer).</p></td>
</tr>
<tr class="row-even"><td><p>coo_val</p></td>
<td><p>Array of <code class="docutils literal notranslate"><span class="pre">nnz</span></code> elements containing the data (floating point).</p></td>
</tr>
<tr class="row-odd"><td><p>coo_ind</p></td>
<td><p>Array of <code class="docutils literal notranslate"><span class="pre">2</span> <span class="pre">*</span> <span class="pre">nnz</span></code> elements containing alternating row and column indices (integer).</p></td>
</tr>
</tbody>
</table>
</div>
<p>The COO (AoS) matrix is expected to be sorted by row indices and column indices per row.
Furthermore, each pair of indices should appear only once.
Consider the following <span class="math notranslate nohighlight">\(3 \times 5\)</span> matrix and the corresponding COO (AoS) structures,
with <span class="math notranslate nohighlight">\(m = 3, n = 5\)</span> and <span class="math notranslate nohighlight">\(\text{nnz} = 8\)</span> using zero-based indexing:</p>
<div class="math notranslate nohighlight">
\[\begin{split}A = \begin{pmatrix}
      1.0 &amp; 2.0 &amp; 0.0 &amp; 3.0 &amp; 0.0 \\
      0.0 &amp; 4.0 &amp; 5.0 &amp; 0.0 &amp; 0.0 \\
      6.0 &amp; 0.0 &amp; 0.0 &amp; 7.0 &amp; 8.0 \\
    \end{pmatrix}\end{split}\]</div>
<p>where</p>
<div class="math notranslate nohighlight">
\[\begin{split}\begin{array}{ll}
  \text{coo_val}[8] &amp; = \{1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0\} \\
  \text{coo_ind}[16] &amp; = \{0, 0, 0, 1, 0, 3, 1, 1, 1, 2, 2, 0, 2, 3, 2, 4\} \\
\end{array}\end{split}\]</div>
</section>
<section id="csr-storage-format">
<h3>CSR storage format<a class="headerlink" href="#csr-storage-format" title="Link to this heading">#</a></h3>
<p>The Compressed Sparse Row (CSR) storage format represents an <span class="math notranslate nohighlight">\(m \times n\)</span> matrix by:</p>
<div class="pst-scrollable-table-container"><table class="table">
<tbody>
<tr class="row-odd"><td><p>m</p></td>
<td><p>Number of rows (integer).</p></td>
</tr>
<tr class="row-even"><td><p>n</p></td>
<td><p>Number of columns (integer).</p></td>
</tr>
<tr class="row-odd"><td><p>nnz</p></td>
<td><p>Number of non-zero elements (integer).</p></td>
</tr>
<tr class="row-even"><td><p>csr_val</p></td>
<td><p>Array of <code class="docutils literal notranslate"><span class="pre">nnz</span></code> elements containing the data (floating point).</p></td>
</tr>
<tr class="row-odd"><td><p>csr_row_ptr</p></td>
<td><p>Array of <code class="docutils literal notranslate"><span class="pre">m+1</span></code> elements that point to the start of every row (integer).</p></td>
</tr>
<tr class="row-even"><td><p>csr_col_ind</p></td>
<td><p>Array of <code class="docutils literal notranslate"><span class="pre">nnz</span></code> elements containing the column indices (integer).</p></td>
</tr>
</tbody>
</table>
</div>
<p>The CSR matrix is expected to be sorted by column indices within each row.
Furthermore, each pair of indices should appear only once.
Consider the following <span class="math notranslate nohighlight">\(3 \times 5\)</span> matrix and the corresponding CSR structures,
with <span class="math notranslate nohighlight">\(m = 3, n = 5\)</span> and <span class="math notranslate nohighlight">\(\text{nnz} = 8\)</span> using one-based indexing:</p>
<div class="math notranslate nohighlight">
\[\begin{split}A = \begin{pmatrix}
      1.0 &amp; 2.0 &amp; 0.0 &amp; 3.0 &amp; 0.0 \\
      0.0 &amp; 4.0 &amp; 5.0 &amp; 0.0 &amp; 0.0 \\
      6.0 &amp; 0.0 &amp; 0.0 &amp; 7.0 &amp; 8.0 \\
    \end{pmatrix}\end{split}\]</div>
<p>where</p>
<div class="math notranslate nohighlight">
\[\begin{split}\begin{array}{ll}
  \text{csr_val}[8] &amp; = \{1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0\} \\
  \text{csr_row_ptr}[4] &amp; = \{1, 4, 6, 9\} \\
  \text{csr_col_ind}[8] &amp; = \{1, 2, 4, 2, 3, 1, 4, 5\}
\end{array}\end{split}\]</div>
</section>
<section id="csc-storage-format">
<h3>CSC storage format<a class="headerlink" href="#csc-storage-format" title="Link to this heading">#</a></h3>
<p>The Compressed Sparse Column (CSC) storage format represents an <span class="math notranslate nohighlight">\(m \times n\)</span> matrix by:</p>
<div class="pst-scrollable-table-container"><table class="table">
<tbody>
<tr class="row-odd"><td><p>m</p></td>
<td><p>Number of rows (integer).</p></td>
</tr>
<tr class="row-even"><td><p>n</p></td>
<td><p>Number of columns (integer).</p></td>
</tr>
<tr class="row-odd"><td><p>nnz</p></td>
<td><p>Number of non-zero elements (integer).</p></td>
</tr>
<tr class="row-even"><td><p>csc_val</p></td>
<td><p>Array of <code class="docutils literal notranslate"><span class="pre">nnz</span></code> elements containing the data (floating point).</p></td>
</tr>
<tr class="row-odd"><td><p>csc_col_ptr</p></td>
<td><p>Array of <code class="docutils literal notranslate"><span class="pre">n+1</span></code> elements that point to the start of every column (integer).</p></td>
</tr>
<tr class="row-even"><td><p>csc_row_ind</p></td>
<td><p>Array of <code class="docutils literal notranslate"><span class="pre">nnz</span></code> elements containing the row indices (integer).</p></td>
</tr>
</tbody>
</table>
</div>
<p>The CSC matrix is expected to be sorted by row indices within each column.
Furthermore, each pair of indices should appear only once.
Consider the following <span class="math notranslate nohighlight">\(3 \times 5\)</span> matrix and the corresponding CSC structures,
with <span class="math notranslate nohighlight">\(m = 3, n = 5\)</span> and <span class="math notranslate nohighlight">\(\text{nnz} = 8\)</span> using one-based indexing:</p>
<div class="math notranslate nohighlight">
\[\begin{split}A = \begin{pmatrix}
      1.0 &amp; 2.0 &amp; 0.0 &amp; 3.0 &amp; 0.0 \\
      0.0 &amp; 4.0 &amp; 5.0 &amp; 0.0 &amp; 0.0 \\
      6.0 &amp; 0.0 &amp; 0.0 &amp; 7.0 &amp; 8.0 \\
    \end{pmatrix}\end{split}\]</div>
<p>where</p>
<div class="math notranslate nohighlight">
\[\begin{split}\begin{array}{ll}
  \text{csc_val}[8] &amp; = \{1.0, 6.0, 2.0, 4.0, 5.0, 3.0, 7.0, 8.0\} \\
  \text{csc_col_ptr}[6] &amp; = \{1, 3, 5, 6, 8, 9\} \\
  \text{csc_row_ind}[8] &amp; = \{1, 3, 1, 2, 2, 1, 3, 3\}
\end{array}\end{split}\]</div>
</section>
<section id="bsr-storage-format">
<h3>BSR storage format<a class="headerlink" href="#bsr-storage-format" title="Link to this heading">#</a></h3>
<p>The Block Compressed Sparse Row (BSR) storage format represents an <span class="math notranslate nohighlight">\((mb \cdot \text{bsr_dim}) \times (nb \cdot \text{bsr_dim})\)</span> matrix by:</p>
<div class="pst-scrollable-table-container"><table class="table">
<tbody>
<tr class="row-odd"><td><p>mb</p></td>
<td><p>Number of block rows (integer).</p></td>
</tr>
<tr class="row-even"><td><p>nb</p></td>
<td><p>Number of block columns (integer).</p></td>
</tr>
<tr class="row-odd"><td><p>nnzb</p></td>
<td><p>Number of non-zero blocks (integer).</p></td>
</tr>
<tr class="row-even"><td><p>bsr_val</p></td>
<td><p>Array of <code class="docutils literal notranslate"><span class="pre">nnzb</span> <span class="pre">*</span> <span class="pre">bsr_dim</span> <span class="pre">*</span> <span class="pre">bsr_dim</span></code> elements containing the data (floating point). Blocks can be stored in column-major or row-major format.</p></td>
</tr>
<tr class="row-odd"><td><p>bsr_row_ptr</p></td>
<td><p>Array of <code class="docutils literal notranslate"><span class="pre">mb+1</span></code> elements that point to the start of every block row (integer).</p></td>
</tr>
<tr class="row-even"><td><p>bsr_col_ind</p></td>
<td><p>Array of <code class="docutils literal notranslate"><span class="pre">nnzb</span></code> elements containing the block column indices (integer).</p></td>
</tr>
<tr class="row-odd"><td><p>bsr_dim</p></td>
<td><p>Dimension of each block (integer).</p></td>
</tr>
</tbody>
</table>
</div>
<p>The BSR matrix is sorted by column indices within each row.
This matrix is defined as having a number of rows equivalent to <span class="math notranslate nohighlight">\(\text{block_dim} \times \text{number_of_row_blocks}\)</span>.
Consider the following <span class="math notranslate nohighlight">\(4 \times 3\)</span> matrix and the corresponding BSR structures,
with <span class="math notranslate nohighlight">\(\text{bsr_dim} = 2, mb = 2, nb = 2\)</span> and <span class="math notranslate nohighlight">\(\text{nnzb} = 4\)</span> using zero-based indexing and column-major storage:</p>
<div class="math notranslate nohighlight">
\[\begin{split}A = \begin{pmatrix}
      1.0 &amp; 0.0 &amp; 2.0 \\
      3.0 &amp; 0.0 &amp; 4.0 \\
      5.0 &amp; 6.0 &amp; 0.0 \\
      7.0 &amp; 0.0 &amp; 8.0 \\
    \end{pmatrix}\end{split}\]</div>
<p>with the blocks <span class="math notranslate nohighlight">\(A_{ij}\)</span></p>
<div class="math notranslate nohighlight">
\[\begin{split}A_{00} = \begin{pmatrix}
           1.0 &amp; 0.0 \\
           3.0 &amp; 0.0 \\
         \end{pmatrix},
A_{01} = \begin{pmatrix}
           2.0 &amp; 0.0 \\
           4.0 &amp; 0.0 \\
         \end{pmatrix},
A_{10} = \begin{pmatrix}
           5.0 &amp; 6.0 \\
           7.0 &amp; 0.0 \\
         \end{pmatrix},
A_{11} = \begin{pmatrix}
           0.0 &amp; 0.0 \\
           8.0 &amp; 0.0 \\
         \end{pmatrix}\end{split}\]</div>
<p>such that</p>
<div class="math notranslate nohighlight">
\[\begin{split}A = \begin{pmatrix}
      A_{00} &amp; A_{01} \\
      A_{10} &amp; A_{11} \\
    \end{pmatrix}\end{split}\]</div>
<p>with arrays represented as</p>
<div class="math notranslate nohighlight">
\[\begin{split}\begin{array}{ll}
  \text{bsr_val}[16] &amp; = \{1.0, 3.0, 0.0, 0.0, 2.0, 4.0, 0.0, 0.0, 5.0, 7.0, 6.0, 0.0, 0.0, 8.0, 0.0, 0.0\} \\
  \text{bsr_row_ptr}[3] &amp; = \{0, 2, 4\} \\
  \text{bsr_col_ind}[4] &amp; = \{0, 1, 0, 1\}
\end{array}\end{split}\]</div>
</section>
<section id="gebsr-storage-format">
<h3>GEBSR storage format<a class="headerlink" href="#gebsr-storage-format" title="Link to this heading">#</a></h3>
<p>The General Block Compressed Sparse Row (GEBSR) storage format represents an <span class="math notranslate nohighlight">\((mb \cdot \text{bsr_row_dim}) \times (nb \cdot \text{bsr_col_dim})\)</span> matrix by:</p>
<div class="pst-scrollable-table-container"><table class="table">
<tbody>
<tr class="row-odd"><td><p>mb</p></td>
<td><p>Number of block rows (integer).</p></td>
</tr>
<tr class="row-even"><td><p>nb</p></td>
<td><p>Number of block columns (integer).</p></td>
</tr>
<tr class="row-odd"><td><p>nnzb</p></td>
<td><p>Number of non-zero blocks (integer).</p></td>
</tr>
<tr class="row-even"><td><p>bsr_val</p></td>
<td><p>Array of <code class="docutils literal notranslate"><span class="pre">nnzb</span> <span class="pre">*</span> <span class="pre">bsr_row_dim</span> <span class="pre">*</span> <span class="pre">bsr_col_dim</span></code> elements containing the data (floating point). Blocks can be stored in column-major or row-major format.</p></td>
</tr>
<tr class="row-odd"><td><p>bsr_row_ptr</p></td>
<td><p>Array of <code class="docutils literal notranslate"><span class="pre">mb+1</span></code> elements that point to the start of every block row (integer).</p></td>
</tr>
<tr class="row-even"><td><p>bsr_col_ind</p></td>
<td><p>Array of <code class="docutils literal notranslate"><span class="pre">nnzb</span></code> elements containing the block column indices (integer).</p></td>
</tr>
<tr class="row-odd"><td><p>bsr_row_dim</p></td>
<td><p>Row dimension of each block (integer).</p></td>
</tr>
<tr class="row-even"><td><p>bsr_col_dim</p></td>
<td><p>Column dimension of each block (integer).</p></td>
</tr>
</tbody>
</table>
</div>
<p>The GEBSR matrix is expected to be sorted by column indices within each row.
If <span class="math notranslate nohighlight">\(m\)</span> is not evenly divisible by the row block dimension or <span class="math notranslate nohighlight">\(n\)</span> is not evenly
divisible by the column block dimension, then zeros are padded to the matrix,
such that <span class="math notranslate nohighlight">\(mb = (m + \text{bsr_row_dim} - 1) / \text{bsr_row_dim}\)</span> and
<span class="math notranslate nohighlight">\(nb = (n + \text{bsr_col_dim} - 1) / \text{bsr_col_dim}\)</span>. Consider the following <span class="math notranslate nohighlight">\(4 \times 5\)</span> matrix
and the corresponding GEBSR structures,
with <span class="math notranslate nohighlight">\(\text{bsr_row_dim} = 2\)</span>, <span class="math notranslate nohighlight">\(\text{bsr_col_dim} = 3\)</span>, <span class="math notranslate nohighlight">\(mb = 2\)</span>, <span class="math notranslate nohighlight">\(nb = 2\)</span>, and <span class="math notranslate nohighlight">\(\text{nnzb} = 4\)</span>
using zero-based indexing and column-major storage:</p>
<div class="math notranslate nohighlight">
\[\begin{split}A = \begin{pmatrix}
      1.0 &amp; 0.0 &amp; 0.0 &amp; 2.0 &amp; 0.0 \\
      3.0 &amp; 0.0 &amp; 4.0 &amp; 0.0 &amp; 0.0 \\
      5.0 &amp; 6.0 &amp; 0.0 &amp; 7.0 &amp; 0.0 \\
      0.0 &amp; 0.0 &amp; 8.0 &amp; 0.0 &amp; 9.0 \\
    \end{pmatrix}\end{split}\]</div>
<p>with the blocks <span class="math notranslate nohighlight">\(A_{ij}\)</span></p>
<div class="math notranslate nohighlight">
\[\begin{split}A_{00} = \begin{pmatrix}
           1.0 &amp; 0.0 &amp; 0.0 \\
           3.0 &amp; 0.0 &amp; 4.0 \\
         \end{pmatrix},
A_{01} = \begin{pmatrix}
           2.0 &amp; 0.0 &amp; 0.0 \\
           0.0 &amp; 0.0 &amp; 0.0 \\
         \end{pmatrix},
A_{10} = \begin{pmatrix}
           5.0 &amp; 6.0 &amp; 0.0 \\
           0.0 &amp; 0.0 &amp; 8.0 \\
         \end{pmatrix},
A_{11} = \begin{pmatrix}
           7.0 &amp; 0.0 &amp; 0.0 \\
           0.0 &amp; 9.0 &amp; 0.0 \\
         \end{pmatrix}\end{split}\]</div>
<p>such that</p>
<div class="math notranslate nohighlight">
\[\begin{split}A = \begin{pmatrix}
      A_{00} &amp; A_{01} \\
      A_{10} &amp; A_{11} \\
    \end{pmatrix}\end{split}\]</div>
<p>with arrays represented as</p>
<div class="math notranslate nohighlight">
\[\begin{split}\begin{array}{ll}
  \text{bsr_val}[24] &amp; = \{1.0, 3.0, 0.0, 0.0, 0.0, 4.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 5.0, 0.0, 6.0, 0.0, 0.0, 8.0, 7.0, 0.0, 0.0, 9.0, 0.0, 0.0\} \\
  \text{bsr_row_ptr}[3] &amp; = \{0, 2, 4\} \\
  \text{bsr_col_ind}[4] &amp; = \{0, 1, 0, 1\}
\end{array}\end{split}\]</div>
</section>
<section id="ell-storage-format">
<h3>ELL storage format<a class="headerlink" href="#ell-storage-format" title="Link to this heading">#</a></h3>
<p>The Ellpack-Itpack (ELL) storage format represents an <span class="math notranslate nohighlight">\(m \times n\)</span> matrix by:</p>
<div class="pst-scrollable-table-container"><table class="table">
<tbody>
<tr class="row-odd"><td><p>m</p></td>
<td><p>Number of rows (integer).</p></td>
</tr>
<tr class="row-even"><td><p>n</p></td>
<td><p>Number of columns (integer).</p></td>
</tr>
<tr class="row-odd"><td><p>ell_width</p></td>
<td><p>Maximum number of non-zero elements per row (integer)</p></td>
</tr>
<tr class="row-even"><td><p>ell_val</p></td>
<td><p>Array of <code class="docutils literal notranslate"><span class="pre">m</span> <span class="pre">*</span> <span class="pre">ell_width</span></code> elements containing the data (floating point).</p></td>
</tr>
<tr class="row-odd"><td><p>ell_col_ind</p></td>
<td><p>Array of <code class="docutils literal notranslate"><span class="pre">m</span> <span class="pre">*</span> <span class="pre">ell_width</span></code> elements containing the column indices (integer).</p></td>
</tr>
</tbody>
</table>
</div>
<p>The ELL matrix is assumed to be stored in column-major format.
Rows with less than <code class="docutils literal notranslate"><span class="pre">ell_width</span></code> non-zero elements are padded with zeros (<code class="docutils literal notranslate"><span class="pre">ell_val</span></code>) and <span class="math notranslate nohighlight">\(-1\)</span> (<code class="docutils literal notranslate"><span class="pre">ell_col_ind</span></code>).
Consider the following <span class="math notranslate nohighlight">\(3 \times 5\)</span> matrix and the corresponding ELL structures,
with <span class="math notranslate nohighlight">\(m = 3, n = 5\)</span>, and <span class="math notranslate nohighlight">\(\text{ell_width} = 3\)</span> using zero-based indexing:</p>
<div class="math notranslate nohighlight">
\[\begin{split}A = \begin{pmatrix}
      1.0 &amp; 2.0 &amp; 0.0 &amp; 3.0 &amp; 0.0 \\
      0.0 &amp; 4.0 &amp; 5.0 &amp; 0.0 &amp; 0.0 \\
      6.0 &amp; 0.0 &amp; 0.0 &amp; 7.0 &amp; 8.0 \\
    \end{pmatrix}\end{split}\]</div>
<p>where</p>
<div class="math notranslate nohighlight">
\[\begin{split}\begin{array}{ll}
  \text{ell_val}[9] &amp; = \{1.0, 4.0, 6.0, 2.0, 5.0, 7.0, 3.0, 0.0, 8.0\} \\
  \text{ell_col_ind}[9] &amp; = \{0, 1, 0, 1, 2, 3, 3, -1, 4\}
\end{array}\end{split}\]</div>
</section>
<section id="hyb-storage-format">
<span id="id1"></span><h3>HYB storage format<a class="headerlink" href="#hyb-storage-format" title="Link to this heading">#</a></h3>
<p>The Hybrid (HYB) storage format represents an <span class="math notranslate nohighlight">\(m \times n\)</span> matrix by:</p>
<div class="pst-scrollable-table-container"><table class="table">
<tbody>
<tr class="row-odd"><td><p>m</p></td>
<td><p>Number of rows (integer).</p></td>
</tr>
<tr class="row-even"><td><p>n</p></td>
<td><p>Number of columns (integer).</p></td>
</tr>
<tr class="row-odd"><td><p>nnz</p></td>
<td><p>Number of non-zero elements of the COO part (integer).</p></td>
</tr>
<tr class="row-even"><td><p>ell_width</p></td>
<td><p>Maximum number of non-zero elements per row of the ELL part (integer).</p></td>
</tr>
<tr class="row-odd"><td><p>ell_val</p></td>
<td><p>Array of <code class="docutils literal notranslate"><span class="pre">m</span> <span class="pre">*</span> <span class="pre">ell_width</span></code> elements containing the data for the ELL part (floating point).</p></td>
</tr>
<tr class="row-even"><td><p>ell_col_ind</p></td>
<td><p>Array of <code class="docutils literal notranslate"><span class="pre">m</span> <span class="pre">*</span> <span class="pre">ell_width</span></code> elements containing the column indices for the ELL part (integer).</p></td>
</tr>
<tr class="row-odd"><td><p>coo_val</p></td>
<td><p>Array of <code class="docutils literal notranslate"><span class="pre">nnz</span></code> elements containing the data for the COO part (floating point).</p></td>
</tr>
<tr class="row-even"><td><p>coo_row_ind</p></td>
<td><p>Array of <code class="docutils literal notranslate"><span class="pre">nnz</span></code> elements containing the row indices for the COO part (integer).</p></td>
</tr>
<tr class="row-odd"><td><p>coo_col_ind</p></td>
<td><p>Array of <code class="docutils literal notranslate"><span class="pre">nnz</span></code> elements containing the column indices for the COO part (integer).</p></td>
</tr>
</tbody>
</table>
</div>
<p>The HYB format is a combination of the ELL and COO sparse matrix formats.
Typically, the regular part of the matrix is stored in
ELL storage format, and the irregular part of the matrix is stored
in COO storage format. Three different partitioning schemes can
be applied when converting a CSR matrix to a matrix in
HYB storage format. For further details on the partitioning schemes,
see <a class="reference external" href="https://rocm.docs.amd.com/projects/rocSPARSE/en/latest/reference/enumerations.html#rocsparse-hyb-partition" title="(in rocSPARSE Documentation v4.2.0)"><span>rocsparse_hyb_partition</span></a>.</p>
</section>
</section>
<section id="storage-schemes-and-indexing-base">
<span id="index-base"></span><h2>Storage schemes and indexing base<a class="headerlink" href="#storage-schemes-and-indexing-base" title="Link to this heading">#</a></h2>
<p>hipSPARSE supports 0-based and 1-based indexing.
The index base is selected by the <a class="reference internal" href="../reference/types.html#_CPPv420hipsparseIndexBase_t" title="hipsparseIndexBase_t"><code class="xref cpp cpp-enum docutils literal notranslate"><span class="pre">hipsparseIndexBase_t</span></code></a> type, which is either passed
as a standalone parameter or as part of the <a class="reference internal" href="../reference/types.html#_CPPv419hipsparseMatDescr_t" title="hipsparseMatDescr_t"><code class="xref cpp cpp-type docutils literal notranslate"><span class="pre">hipsparseMatDescr_t</span></code></a> type.</p>
<p>Dense vectors are represented with a 1D array, stored linearly in memory.
Sparse vectors are represented by a 1D data array stored linearly in memory that holds all non-zero elements
and a 1D indexing array stored linearly in memory that holds the positions of the corresponding non-zero elements.</p>
</section>
<section id="pointer-mode">
<h2>Pointer mode<a class="headerlink" href="#pointer-mode" title="Link to this heading">#</a></h2>
<p>The auxiliary functions <a class="reference internal" href="../reference/auxiliary.html#_CPPv423hipsparseSetPointerMode17hipsparseHandle_t22hipsparsePointerMode_t" title="hipsparseSetPointerMode"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipsparseSetPointerMode()</span></code></a> and <a class="reference internal" href="../reference/auxiliary.html#_CPPv423hipsparseGetPointerMode17hipsparseHandle_tP22hipsparsePointerMode_t" title="hipsparseGetPointerMode"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipsparseGetPointerMode()</span></code></a> are
used to set and get the value of the state variable <a class="reference internal" href="../reference/types.html#_CPPv422hipsparsePointerMode_t" title="hipsparsePointerMode_t"><code class="xref cpp cpp-enum docutils literal notranslate"><span class="pre">hipsparsePointerMode_t</span></code></a>.
If <a class="reference internal" href="../reference/types.html#_CPPv422hipsparsePointerMode_t" title="hipsparsePointerMode_t"><code class="xref cpp cpp-enum docutils literal notranslate"><span class="pre">hipsparsePointerMode_t</span></code></a> is equal to <a class="reference internal" href="../reference/types.html#_CPPv4N22hipsparsePointerMode_t27HIPSPARSE_POINTER_MODE_HOSTE" title="HIPSPARSE_POINTER_MODE_HOST"><code class="xref cpp cpp-enumerator docutils literal notranslate"><span class="pre">HIPSPARSE_POINTER_MODE_HOST</span></code></a>,
then scalar parameters must be allocated on the host.
If <a class="reference internal" href="../reference/types.html#_CPPv422hipsparsePointerMode_t" title="hipsparsePointerMode_t"><code class="xref cpp cpp-enum docutils literal notranslate"><span class="pre">hipsparsePointerMode_t</span></code></a> is equal to <a class="reference internal" href="../reference/types.html#_CPPv4N22hipsparsePointerMode_t29HIPSPARSE_POINTER_MODE_DEVICEE" title="HIPSPARSE_POINTER_MODE_DEVICE"><code class="xref cpp cpp-enumerator docutils literal notranslate"><span class="pre">HIPSPARSE_POINTER_MODE_DEVICE</span></code></a>,
then scalar parameters must be allocated on the device.</p>
<p>There are two types of scalar parameter:</p>
<ol class="arabic simple">
<li><p>Scaling parameters, such as <code class="docutils literal notranslate"><span class="pre">alpha</span></code> and <code class="docutils literal notranslate"><span class="pre">beta</span></code>, that are used, for example, in <a class="reference internal" href="../reference/level2.html#_CPPv415hipsparseScsrmv17hipsparseHandle_t20hipsparseOperation_tiiiPKfK19hipsparseMatDescr_tPKfPKiPKiPKfPKfPf" title="hipsparseScsrmv"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipsparseScsrmv()</span></code></a> and <a class="reference internal" href="../reference/level2.html#_CPPv415hipsparseSbsrmv17hipsparseHandle_t20hipsparseDirection_t20hipsparseOperation_tiiiPKfK19hipsparseMatDescr_tPKfPKiPKiiPKfPKfPf" title="hipsparseSbsrmv"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipsparseSbsrmv()</span></code></a></p></li>
<li><p>Scalar results from functions such as <a class="reference internal" href="../reference/level1.html#_CPPv414hipsparseSdoti17hipsparseHandle_tiPKfPKiPKfPf20hipsparseIndexBase_t" title="hipsparseSdoti"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipsparseSdoti()</span></code></a> or <a class="reference internal" href="../reference/level1.html#_CPPv415hipsparseCdotci17hipsparseHandle_tiPK10hipComplexPKiPK10hipComplexP10hipComplex20hipsparseIndexBase_t" title="hipsparseCdotci"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipsparseCdotci()</span></code></a></p></li>
</ol>
<p>For scalar parameters such as <code class="docutils literal notranslate"><span class="pre">alpha</span></code> and <code class="docutils literal notranslate"><span class="pre">beta</span></code>, memory can be allocated on the host heap or stack
when <a class="reference internal" href="../reference/types.html#_CPPv422hipsparsePointerMode_t" title="hipsparsePointerMode_t"><code class="xref cpp cpp-enum docutils literal notranslate"><span class="pre">hipsparsePointerMode_t</span></code></a> is equal to <a class="reference internal" href="../reference/types.html#_CPPv4N22hipsparsePointerMode_t27HIPSPARSE_POINTER_MODE_HOSTE" title="HIPSPARSE_POINTER_MODE_HOST"><code class="xref cpp cpp-enumerator docutils literal notranslate"><span class="pre">HIPSPARSE_POINTER_MODE_HOST</span></code></a>.
The kernel launch is asynchronous, and if the scalar parameter is on the heap, it can be freed after
the return from the kernel launch.
When <a class="reference internal" href="../reference/types.html#_CPPv422hipsparsePointerMode_t" title="hipsparsePointerMode_t"><code class="xref cpp cpp-enum docutils literal notranslate"><span class="pre">hipsparsePointerMode_t</span></code></a> is equal to <a class="reference internal" href="../reference/types.html#_CPPv4N22hipsparsePointerMode_t29HIPSPARSE_POINTER_MODE_DEVICEE" title="HIPSPARSE_POINTER_MODE_DEVICE"><code class="xref cpp cpp-enumerator docutils literal notranslate"><span class="pre">HIPSPARSE_POINTER_MODE_DEVICE</span></code></a>,
the scalar parameter must not be changed until the kernel completes.</p>
<p>For scalar results, when <a class="reference internal" href="../reference/types.html#_CPPv422hipsparsePointerMode_t" title="hipsparsePointerMode_t"><code class="xref cpp cpp-enum docutils literal notranslate"><span class="pre">hipsparsePointerMode_t</span></code></a> is equal to <a class="reference internal" href="../reference/types.html#_CPPv4N22hipsparsePointerMode_t27HIPSPARSE_POINTER_MODE_HOSTE" title="HIPSPARSE_POINTER_MODE_HOST"><code class="xref cpp cpp-enumerator docutils literal notranslate"><span class="pre">HIPSPARSE_POINTER_MODE_HOST</span></code></a>,
the function blocks the CPU until the GPU has copied the result back to the host.
When <a class="reference internal" href="../reference/types.html#_CPPv422hipsparsePointerMode_t" title="hipsparsePointerMode_t"><code class="xref cpp cpp-enum docutils literal notranslate"><span class="pre">hipsparsePointerMode_t</span></code></a> is equal to <a class="reference internal" href="../reference/types.html#_CPPv4N22hipsparsePointerMode_t29HIPSPARSE_POINTER_MODE_DEVICEE" title="HIPSPARSE_POINTER_MODE_DEVICE"><code class="xref cpp cpp-enumerator docutils literal notranslate"><span class="pre">HIPSPARSE_POINTER_MODE_DEVICE</span></code></a>,
the function returns after the asynchronous launch.
Similar to the vector and matrix results, the scalar result is only available when the kernel has completed execution.</p>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="../install/install-windows.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Installing and building hipSPARSE for Microsoft Windows</p>
      </div>
    </a>
    <a class="right-next"
       href="../reference/reference.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">hipSPARSE API reference guide</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#interface-examples">Interface examples</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#storage-formats">Storage formats</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#coo-storage-format">COO storage format</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#coo-aos-storage-format">COO (AoS) storage format</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#csr-storage-format">CSR storage format</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#csc-storage-format">CSC storage format</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#bsr-storage-format">BSR storage format</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#gebsr-storage-format">GEBSR storage format</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#ell-storage-format">ELL storage format</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hyb-storage-format">HYB storage format</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#storage-schemes-and-indexing-base">Storage schemes and indexing base</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#pointer-mode">Pointer mode</a></li>
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
