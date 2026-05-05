---
title: "MIVisionX environment variables &#8212; MIVisionX 3.5.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/MIVisionX/en/latest/reference/MIVisionX-env-variables.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:11:07.496853+00:00
content_hash: "91d7453c2af878b1"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="MIVisionX API" name="description" />
<meta content="MIVisionX, ROCm, API, reference, environment variable, environment" name="keywords" />

    <title>MIVisionX environment variables &#8212; MIVisionX 3.5.0 Documentation</title>
  
  
  
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

    <link rel="stylesheet" type="text/css" href="../_static/pygments.css?v=a746c00c" />
    <link rel="stylesheet" type="text/css" href="../_static/styles/sphinx-book-theme.css?v=a3416100" />
    <link rel="stylesheet" type="text/css" href="../_static/mystnb.4510f1fc1dee50b3e5859aac5469c37c29e427902b24a333a5f9fcb2f0b3ac41.css" />
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

    <script src="../_static/documentation_options.js?v=d3112e53"></script>
    <script src="../_static/doctools.js?v=9a2dae69"></script>
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'reference/MIVisionX-env-variables';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />
    <link rel="next" title="MIVisionX APIs" href="../doxygen/html/modules.html" />
    <link rel="prev" title="MIVisionX toolkits" href="MIVisionX-toolkits.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-mivisionx" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/reference/MIVisionX-env-variables.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<aside class="bd-header-announcement" aria-label="Announcement">
  <div class="bd-header-announcement__content">The ROCm 7.12.0 technology preview release documentation is available at <a id='rocm-banner' href='https://rocm.docs.amd.com/en/7.12.0-preview/'>ROCm Preview documentation</a>. For production use, continue to use ROCm 7.2.2 documentation.</div>
</aside>

  

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
                            <a class="nav-link top-level header-menu-links" href="https://github.com/ROCm/MIVisionX" id="navgithub" role="button" aria-expanded="false" target="_blank" >
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
                            <a class="nav-link top-level header-menu-links" href="https://github.com/ROCm/MIVisionX/issues/new/choose" id="navsupport" role="button" aria-expanded="false" target="_blank" >
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
  
  
  
  
  
  
    <p class="title logo__title">MIVisionX 3.5.0 Documentation</p>
  
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
<li class="toctree-l1"><a class="reference internal" href="../install/MIVisionX-prerequisites.html">Prerequisites</a></li>
<li class="toctree-l1"><a class="reference internal" href="../install/MIVisionX-linux-build-and-install.html">Build and install on Linux</a></li>
<li class="toctree-l1"><a class="reference internal" href="../install/MIVisionX-package-install.html">Install using the package installer on Linux</a></li>
<li class="toctree-l1"><a class="reference internal" href="../install/MIVisionX-windows-install.html">Install on Windows</a></li>
<li class="toctree-l1"><a class="reference internal" href="../install/MIVisionX-macOS-install.html">Install on macOS</a></li>
<li class="toctree-l1"><a class="reference internal" href="../install/MIVisionX-model-compiler-install.html">Install the model compiler</a></li>
<li class="toctree-l1"><a class="reference internal" href="../install/MIVisionX-install-OpenVX.html">Install OpenVX</a></li>
<li class="toctree-l1"><a class="reference internal" href="../install/MIVisionX-test-install.html">Test the installation</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">How to</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../how-to/MIVisionX-how-to-model-compiler.html">Use the model compiler</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Reference</span></p>
<ul class="current nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="MIVisionX-AMD-Openvx.html">AMD OpenVX</a></li>
<li class="toctree-l1"><a class="reference internal" href="MIVisionX-supported-models.html">Supported models and operators</a></li>
<li class="toctree-l1"><a class="reference internal" href="MIVisionX-toolkits.html">Toolkits</a></li>
<li class="toctree-l1 current active"><a class="current reference internal" href="#">Environment variables</a></li>
<li class="toctree-l1"><a class="reference internal" href="../doxygen/html/modules.html">API Reference</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Examples</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../tutorials/MIVisionX-apps-samples.html">Sample applications</a></li>
<li class="toctree-l1"><a class="reference internal" href="../tutorials/MIVisionX-model-comp-samples.html">Model compiler samples</a></li>
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
    <li class="breadcrumb-item active" aria-current="page"><span class="ellipsis">MIVisionX environment variables</span></li>
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
    <h1>MIVisionX environment variables</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#core-openvx-configuration">Core OpenVX Configuration</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#gpu-and-device-configuration">GPU and Device Configuration</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#opencl-configuration">OpenCL Configuration</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#debugging-and-profiling">Debugging and Profiling</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#stitching-configuration">Stitching Configuration</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#chroma-key-configuration">Chroma Key Configuration</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#file-i-o-and-auxiliary-operations">File I/O and Auxiliary Operations</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#model-deployment">Model Deployment</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#neural-network-configuration">Neural Network Configuration</a></li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="mivisionx-environment-variables">
<span id="env-variables"></span><h1>MIVisionX environment variables<a class="headerlink" href="#mivisionx-environment-variables" title="Link to this heading">#</a></h1>
<p>This section describes the most important MIVisionX environment variables,
which are grouped by functionality.</p>
<section id="core-openvx-configuration">
<h2>Core OpenVX Configuration<a class="headerlink" href="#core-openvx-configuration" title="Link to this heading">#</a></h2>
<p>The core OpenVX configuration environment variables for MIVisionX are collected in the following table.</p>
<div class="pst-scrollable-table-container"><table class="table">
<colgroup>
<col style="width: 70.0%" />
<col style="width: 30.0%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Environment variable</strong></p></th>
<th class="head"><p><strong>Value</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">AGO_DEFAULT_TARGET</span></code></div>
<div class="line">Sets the default execution target for OpenVX kernels.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">“GPU”: Execute kernels on GPU</div>
<div class="line">“CPU”: Execute kernels on CPU</div>
<div class="line">Unset: Use library default target</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">AGO_BUFFER_MERGE_FLAGS</span></code></div>
<div class="line">Controls buffer merging optimization flags.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">Integer bitmask value</div>
<div class="line">Higher values: More aggressive merging</div>
<div class="line">0: Disable buffer merging</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">AGO_THREAD_CONFIG</span></code></div>
<div class="line">Configures thread usage for CPU execution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">Integer value (likely number of threads)</div>
<div class="line">0: Use default threading</div>
<div class="line">Positive integer: Specific thread count</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">VX_GRAPH_ATTRIBUTE_AMD_OPTIMIZER_FLAGS</span></code></div>
<div class="line">Sets OpenVX graph optimizer flags for AMD extensions.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">Integer bitmask value</div>
<div class="line">0: Disable optimizations</div>
<div class="line">Positive values: Enable specific optimizations</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="gpu-and-device-configuration">
<h2>GPU and Device Configuration<a class="headerlink" href="#gpu-and-device-configuration" title="Link to this heading">#</a></h2>
<p>The GPU and device configuration environment variables for MIVisionX are collected in the following table.</p>
<div class="pst-scrollable-table-container"><table class="table">
<colgroup>
<col style="width: 70.0%" />
<col style="width: 30.0%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Environment variable</strong></p></th>
<th class="head"><p><strong>Value</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">GPU_ENABLE_WGP_MODE</span></code></div>
<div class="line">Controls Workgroup Processor (WGP) mode on RDNA GPUs that support both CU and WGP modes.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable WGP mode (use CU mode)</div>
<div class="line">1 or any non-zero: Enable WGP mode (default)</div>
<div class="line">Only applies to GPUs with major version &gt;= 10</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="opencl-configuration">
<h2>OpenCL Configuration<a class="headerlink" href="#opencl-configuration" title="Link to this heading">#</a></h2>
<p>The OpenCL configuration environment variables for MIVisionX are collected in the following table.</p>
<div class="pst-scrollable-table-container"><table class="table">
<colgroup>
<col style="width: 70.0%" />
<col style="width: 30.0%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Environment variable</strong></p></th>
<th class="head"><p><strong>Value</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">AGO_OPENCL_PLATFORM</span></code></div>
<div class="line">Overrides the default OpenCL platform selection.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">String specifying OpenCL platform name</div>
<div class="line">Used to select specific OpenCL implementation</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">AGO_OPENCL_VERSION_CHECK</span></code></div>
<div class="line">Controls OpenCL version checking behavior.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">String value controlling version validation</div>
<div class="line">May disable or modify version requirements</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">AGO_OPENCL_BUILD_OPTIONS</span></code></div>
<div class="line">Specifies additional OpenCL kernel build options.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">String containing OpenCL compiler flags</div>
<div class="line">Passed to OpenCL kernel compilation</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">AGO_OPENCL_DEVICE_INFO</span></code></div>
<div class="line">Controls OpenCL device information reporting.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">String value controlling device info output</div>
<div class="line">Used for debugging device capabilities</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="debugging-and-profiling">
<h2>Debugging and Profiling<a class="headerlink" href="#debugging-and-profiling" title="Link to this heading">#</a></h2>
<p>The debugging and profiling environment variables for MIVisionX are collected in the following table.</p>
<div class="pst-scrollable-table-container"><table class="table">
<colgroup>
<col style="width: 70.0%" />
<col style="width: 30.0%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Environment variable</strong></p></th>
<th class="head"><p><strong>Value</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">AGO_DUMP_GPU</span></code></div>
<div class="line">Enables GPU kernel dumping for debugging purposes.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">String value enabling GPU kernel dump</div>
<div class="line">Used for analyzing GPU kernel behavior</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="stitching-configuration">
<h2>Stitching Configuration<a class="headerlink" href="#stitching-configuration" title="Link to this heading">#</a></h2>
<p>The stitching configuration environment variables for MIVisionX are collected in the following table.</p>
<div class="pst-scrollable-table-container"><table class="table">
<colgroup>
<col style="width: 70.0%" />
<col style="width: 30.0%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Environment variable</strong></p></th>
<th class="head"><p><strong>Value</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">DRAW_SEAM</span></code></div>
<div class="line">Enables drawing of seam lines for verification in stitching operations.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable seam drawing (default)</div>
<div class="line">1: Enable seam drawing visualization</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">SEAM_ADJUST</span></code></div>
<div class="line">Controls seam adjustment behavior in stitching.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable seam adjustment (default)</div>
<div class="line">1: Enable dynamic seam adjustment</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">PRINT_COST</span></code></div>
<div class="line">Enables printing of cost calculations during seam finding.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable cost printing (default)</div>
<div class="line">1: Print cost matrix values for debugging</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">SEAM_FIND_TARGET</span></code></div>
<div class="line">Sets the target method for seam finding algorithms.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">Integer value (algorithm selector)</div>
<div class="line">Different values select different seam finding methods</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">VIEW_SCENE_CHANGE</span></code></div>
<div class="line">Controls view scene change detection behavior.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable scene change detection</div>
<div class="line">1: Enable scene change detection</div>
<div class="line">Higher values: More sensitive detection</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">SEAM_THRESHOLD</span></code></div>
<div class="line">Sets threshold value for seam detection algorithms.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">Integer value (0-255 typical range)</div>
<div class="line">Lower values: More sensitive seam detection</div>
<div class="line">Higher values: Less sensitive seam detection</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">SCENE_DURATION</span></code></div>
<div class="line">Sets duration for scene analysis in stitching.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">Integer value (likely in frames or milliseconds)</div>
<div class="line">Controls temporal window for scene analysis</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">SEAM_FREQUENCY</span></code></div>
<div class="line">Controls frequency of seam finding operations.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">Integer value (likely in frames)</div>
<div class="line">1: Find seams every frame</div>
<div class="line">Higher values: Find seams less frequently</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">SEAM_FIND_MODE</span></code></div>
<div class="line">Sets the operational mode for seam finding algorithms.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">Integer value (mode selector)</div>
<div class="line">Different values select different seam finding strategies</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">LOOM_SEAM_FIND_DISABLE</span></code></div>
<div class="line">Disables seam finding in LOOM stitching operations.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">“1”: Disable seam finding</div>
<div class="line">“0” or unset: Enable seam finding</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="chroma-key-configuration">
<h2>Chroma Key Configuration<a class="headerlink" href="#chroma-key-configuration" title="Link to this heading">#</a></h2>
<p>The chroma key configuration environment variables for MIVisionX are collected in the following table.</p>
<div class="pst-scrollable-table-container"><table class="table">
<colgroup>
<col style="width: 70.0%" />
<col style="width: 30.0%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Environment variable</strong></p></th>
<th class="head"><p><strong>Value</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">CHROMAKEY_MASK</span></code></div>
<div class="line">Controls chroma key masking behavior.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">Integer value specifying chroma key mask settings</div>
<div class="line">Used for green screen/chroma key operations</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">CHROMAKEY_MERGE</span></code></div>
<div class="line">Controls chroma key merging operations.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">Integer value specifying chroma key merge settings</div>
<div class="line">Controls how chroma key layers are combined</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="file-i-o-and-auxiliary-operations">
<h2>File I/O and Auxiliary Operations<a class="headerlink" href="#file-i-o-and-auxiliary-operations" title="Link to this heading">#</a></h2>
<p>The file I/O and auxiliary operation environment variables for MIVisionX are collected in the following table.</p>
<div class="pst-scrollable-table-container"><table class="table">
<colgroup>
<col style="width: 70.0%" />
<col style="width: 30.0%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Environment variable</strong></p></th>
<th class="head"><p><strong>Value</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">LOOMIO_AUX_DUMP</span></code></div>
<div class="line">Specifies file path for auxiliary LOOM I/O data dumping.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">String path to dump file</div>
<div class="line">Enables debugging of LOOM I/O operations</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="model-deployment">
<h2>Model Deployment<a class="headerlink" href="#model-deployment" title="Link to this heading">#</a></h2>
<p>The model deployment environment variables for MIVisionX are collected in the following table.</p>
<div class="pst-scrollable-table-container"><table class="table">
<colgroup>
<col style="width: 70.0%" />
<col style="width: 30.0%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Environment variable</strong></p></th>
<th class="head"><p><strong>Value</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIVISIONX_MODEL_COMPILER_PATH</span></code></div>
<div class="line">Overrides the default path to the MIVisionX model compiler.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">String path to model compiler executable</div>
<div class="line">Default: “/opt/rocm/libexec/mivisionx/model_compiler”</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="neural-network-configuration">
<h2>Neural Network Configuration<a class="headerlink" href="#neural-network-configuration" title="Link to this heading">#</a></h2>
<p>The neural network configuration environment variables for MIVisionX are collected in the following table.</p>
<div class="pst-scrollable-table-container"><table class="table">
<colgroup>
<col style="width: 70.0%" />
<col style="width: 30.0%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Environment variable</strong></p></th>
<th class="head"><p><strong>Value</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">NN_MIOPEN_CBR_MODE</span></code></div>
<div class="line">Controls MIOpen Convolution-BatchNorm-ReLU fusion mode for neural networks.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">Integer value specifying CBR mode</div>
<div class="line">Default: 1 (enabled)</div>
<div class="line">Controls operator fusion optimization</div>
</div>
</td>
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
       href="MIVisionX-toolkits.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">MIVisionX toolkits</p>
      </div>
    </a>
    <a class="right-next"
       href="../doxygen/html/modules.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">MIVisionX APIs</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#core-openvx-configuration">Core OpenVX Configuration</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#gpu-and-device-configuration">GPU and Device Configuration</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#opencl-configuration">OpenCL Configuration</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#debugging-and-profiling">Debugging and Profiling</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#stitching-configuration">Stitching Configuration</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#chroma-key-configuration">Chroma Key Configuration</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#file-i-o-and-auxiliary-operations">File I/O and Auxiliary Operations</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#model-deployment">Model Deployment</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#neural-network-configuration">Neural Network Configuration</a></li>
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
