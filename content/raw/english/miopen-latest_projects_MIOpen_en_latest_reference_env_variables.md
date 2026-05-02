---
title: "MIOpen environment variables &#8212; MIOpen 3.5.1 Documentation"
source_url: "https://rocm.docs.amd.com/projects/MIOpen/en/latest/reference/env_variables.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T18:09:57.750126+00:00
content_hash: "b16e866729691eb3"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="MIOpen environment variables reference" name="description" />
<meta content="MIOpen, ROCm, API, environment variables, environment, reference" name="keywords" />

    <title>MIOpen environment variables &#8212; MIOpen 3.5.1 Documentation</title>
  
  
  
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
    <link rel="stylesheet" type="text/css" href="../_static/styles/sphinx-book-theme.css?v=384b581d" />
    <link rel="stylesheet" type="text/css" href="../_static/mystnb.4510f1fc1dee50b3e5859aac5469c37c29e427902b24a333a5f9fcb2f0b3ac41.css" />
    <link rel="stylesheet" type="text/css" href="../_static/copybutton.css?v=76b2166b" />
    <link rel="stylesheet" type="text/css" href="../_static/custom.css?v=643846e8" />
    <link rel="stylesheet" type="text/css" href="../_static/rocm_header.css?v=9557e3d1" />
    <link rel="stylesheet" type="text/css" href="../_static/rocm_footer.css?v=7095035a" />
    <link rel="stylesheet" type="text/css" href="../_static/fonts.css?v=fcff5274" />
    <link rel="stylesheet" type="text/css" href="../_static/design-style.1e8bd061cd6da7fc9cf755528e8ffc24.min.css?v=0a3b3ea7" />
  
  <!-- So that users can add custom icons -->
  <script src="../_static/scripts/fontawesome.js?digest=8878045cc6db502f8baf"></script>
  <!-- Pre-loaded scripts that we'll load fully later -->
  <link rel="preload" as="script" href="../_static/scripts/bootstrap.js?digest=8878045cc6db502f8baf" />
<link rel="preload" as="script" href="../_static/scripts/pydata-sphinx-theme.js?digest=8878045cc6db502f8baf" />

    <script src="../_static/documentation_options.js?v=68edac4e"></script>
    <script src="../_static/doctools.js?v=9a2dae69"></script>
    <script src="../_static/sphinx_highlight.js?v=dc90522c"></script>
    <script src="../_static/clipboard.min.js?v=a7894cd8"></script>
    <script src="../_static/copybutton.js?v=91c4cb68"></script>
    <script async="async" src="../_static/code_word_breaks.js?v=327952c4"></script>
    <script async="async" src="../_static/renameVersionLinks.js?v=929fe5e4"></script>
    <script async="async" src="../_static/rdcMisc.js?v=01f88d96"></script>
    <script async="async" src="../_static/theme_mode_captions.js?v=15f4ec5d"></script>
    <script defer="defer" src="../_static/search.js?v=90a4452c"></script>
    <script src="../_static/scripts/sphinx-book-theme.js?v=efea14e4"></script>
    <script src="../_static/design-tabs.js?v=36754332"></script>
    <script>DOCUMENTATION_OPTIONS.pagename = 'reference/env_variables';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />
    <link rel="next" title="License" href="../license.html" />
    <link rel="prev" title="Datatypes" href="datatypes.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-miopen" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/reference/env_variables.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
  
  
  
  
  
  
    <p class="title logo__title">MIOpen 3.5.1 Documentation</p>
  
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
<li class="toctree-l1"><a class="reference internal" href="../install/prerequisites.html">MIOpen prerequisites</a></li>
<li class="toctree-l1"><a class="reference internal" href="../install/install.html">Install MIOpen</a></li>
<li class="toctree-l1"><a class="reference internal" href="../install/build-source.html">Build MIOpen from source</a></li>
<li class="toctree-l1"><a class="reference internal" href="../install/embed.html">Build MIOpen for embedded systems</a></li>
<li class="toctree-l1"><a class="reference internal" href="../install/docker-build.html">Build MIOpen using Docker</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Conceptual</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../conceptual/finddb.html">Find database</a></li>
<li class="toctree-l1"><a class="reference internal" href="../conceptual/cache.html">Kernel cache</a></li>
<li class="toctree-l1"><a class="reference internal" href="../conceptual/perfdb.html">Performance database</a></li>
<li class="toctree-l1"><a class="reference internal" href="../conceptual/tuningdb.html">Manual tuning</a></li>
<li class="toctree-l1"><a class="reference internal" href="../conceptual/MI200-alt-implementation.html">MI200 alternate implementation</a></li>
<li class="toctree-l1"><a class="reference internal" href="../conceptual/porting-guide.html">Porting to MIOpen</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">How to</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../how-to/use-fusion-api.html">Use the fusion API</a></li>
<li class="toctree-l1"><a class="reference internal" href="../how-to/debug-log.html">Log and debug</a></li>
<li class="toctree-l1"><a class="reference internal" href="../how-to/find-and-immediate.html">Use the find APIs and immediate mode</a></li>
<li class="toctree-l1"><a class="reference internal" href="../how-to/use-nhwc-batchnorm-in-pytorch.html">Use NHWC Batch Normalization with PyTorch</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Samples</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference external" href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/miopen/samples">MIOpen samples</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Reference</span></p>
<ul class="current nav bd-sidenav">
<li class="toctree-l1 current active has-children"><a class="reference internal" href="index.html">API library</a><details open="open"><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul class="current">
<li class="toctree-l2"><a class="reference internal" href="../doxygen/html/modules.html">Modules</a></li>
<li class="toctree-l2"><a class="reference internal" href="datatypes.html">Datatypes</a></li>
<li class="toctree-l2 current active"><a class="current reference internal" href="#">Environment variables</a></li>
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
    
    <li class="breadcrumb-item"><a href="index.html" class="nav-link">API reference library</a></li>
    
    <li class="breadcrumb-item active" aria-current="page"><span class="ellipsis">MIOpen environment variables</span></li>
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
<label class="sidebar-toggle secondary-toggle btn btn-sm" for="__secondary"title="Toggle secondary sidebar" data-bs-placement="bottom" data-bs-toggle="tooltip">
    <span class="fa-solid fa-list"></span>
</label>
</div></div>
      
    </div>
  
</div>
</div>
              
              

<div id="jb-print-docs-body" class="onlyprint">
    <h1>MIOpen environment variables</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#logging-and-debugging">Logging and debugging</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#find-mode-configuration">Find mode configuration</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#algorithm-control">Algorithm control</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#kernel-build-method-control">Kernel build method control</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#solution-selection">Solution selection</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#direct-solution-control">Direct solution control</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#winograd-solution-control">Winograd solution control</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#multi-pass-winograd-solution-control">Multi-pass Winograd solution control</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#asm-implicit-gemm-solution-control">ASM implicit GEMM solution control</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-implicit-gemm-solution-control">HIP implicit GEMM solution control</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#d-implicit-gemm-solution-control">3D implicit GEMM solution control</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#gemm-backend-control">GEMM backend control</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#convolution-attributes">Convolution attributes</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#compilation-control">Compilation control</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#experimental-controls">Experimental controls</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rnn-control">RNN control</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#composable-kernel-ck-solution-control">Composable Kernel (CK) solution control</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#mlir-solution-control">MLIR solution control</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#attention-and-softmax-control">Attention and softmax control</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#driver-and-testing-advanced">Driver and testing (Advanced)</a></li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="miopen-environment-variables">
<h1>MIOpen environment variables<a class="headerlink" href="#miopen-environment-variables" title="Link to this heading">#</a></h1>
<p>This section describes the important MIOpen environment variables,
which are grouped by functionality.</p>
<section id="logging-and-debugging">
<h2>Logging and debugging<a class="headerlink" href="#logging-and-debugging" title="Link to this heading">#</a></h2>
<p>The logging and debugging environment variables for MIOpen are collected in the following table.
For more information, see <a class="reference internal" href="../how-to/debug-log.html"><span class="doc">Logging and debugging</span></a>.</p>
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
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_ENABLE_LOGGING</span></code></div>
<div class="line">Prints basic layer-by-layer MIOpen API call information with parameters and configurations.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_ENABLE_LOGGING_CMD</span></code></div>
<div class="line">Outputs associated MIOpenDriver command lines to console.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_LOG_LEVEL</span></code></div>
<div class="line">Controls verbosity of internal operation logging messages.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Default (level 4 for release, level 5 for debug builds)</div>
<div class="line">1: Quiet (no logging)</div>
<div class="line">2: Fatal errors only (unused)</div>
<div class="line">3: Errors including fatal errors</div>
<div class="line">4: All errors and warnings</div>
<div class="line">5: Info level debugging</div>
<div class="line">6: Detailed debugging information</div>
<div class="line">7: Trace level with additional details</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_ENABLE_LOGGING_MPMT</span></code></div>
<div class="line">Prefixes each log line with process/thread identification for multi-process/multi-threaded debugging.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_ENABLE_LOGGING_ELAPSED_TIME</span></code></div>
<div class="line">Adds timestamp showing elapsed time in milliseconds since previous log message.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_CHECK_NUMERICS</span></code></div>
<div class="line">Scans inputs/outputs for numerical abnormalities (inf, NaN, zeros).</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0x01: Fully informative (print all check results)</div>
<div class="line">0x02: Warning information (print only abnormalities)</div>
<div class="line">0x04: Throw error on detection</div>
<div class="line">0x08: Abort on abnormal result</div>
<div class="line">0x10: Print statistics (mean/absmean/min/max)</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CHECK_SUB_BUFFER_OOB_MEMORY_ACCESS</span></code></div>
<div class="line">Checks for GPU sub-buffer out-of-bounds memory access errors.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0 or unset: No OOB detection</div>
<div class="line">1: Check for OOBs before sub-buffer start</div>
<div class="line">2: Check for OOBs after sub-buffer end</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="find-mode-configuration">
<h2>Find mode configuration<a class="headerlink" href="#find-mode-configuration" title="Link to this heading">#</a></h2>
<p>The find mode configuration environment variables for MIOpen are collected in the following table.
For more information, see <a class="reference internal" href="../conceptual/finddb.html"><span class="doc">Find database</span></a>, <a class="reference internal" href="../how-to/find-and-immediate.html"><span class="doc">Use the find APIs and immediate mode</span></a>
and <a class="reference internal" href="../conceptual/perfdb.html"><span class="doc">Performance database</span></a>.</p>
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
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_FIND_MODE</span></code></div>
<div class="line">Sets find mode to accelerate find API calls.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">“NORMAL” or 1: Full find mode (benchmarks all solvers)</div>
<div class="line">“FAST” or 2: Fast find (use FindDb or immediate fallback)</div>
<div class="line">“HYBRID” or 3: Hybrid find (FindDb hit or full find)</div>
<div class="line">4: Reserved (do not use)</div>
<div class="line">“DYNAMIC_HYBRID” or 5: Dynamic hybrid (default, skip non-dynamic kernels)</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_FIND_ENFORCE</span></code></div>
<div class="line">Controls auto-tune behavior and database updates.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">“NONE” or 1: No change in default behavior</div>
<div class="line">“DB_UPDATE” or 2: Always perform auto-tune and update PerfDb</div>
<div class="line">“SEARCH” or 3: Auto-tune even if not requested via API</div>
<div class="line">“SEARCH_DB_UPDATE” or 4: Combination of DB_UPDATE and SEARCH</div>
<div class="line">“DB_CLEAN” or 5: Remove optimized values from User PerfDb</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_DISABLE_FIND_DB</span></code></div>
<div class="line">Disables FindDb functionality.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">1: Disable FindDb</div>
<div class="line">0 or unset: Enable FindDb</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="algorithm-control">
<h2>Algorithm control<a class="headerlink" href="#algorithm-control" title="Link to this heading">#</a></h2>
<p>The algorithm control environment variables for MIOpen are collected in the following table.
For more information, see <a class="reference internal" href="../how-to/debug-log.html"><span class="doc">Logging and debugging</span></a>.</p>
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
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_FFT</span></code></div>
<div class="line">Controls FFT convolution algorithm.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_DIRECT</span></code></div>
<div class="line">Controls direct convolution algorithm.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_GEMM</span></code></div>
<div class="line">Controls GEMM convolution algorithm.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_WINOGRAD</span></code></div>
<div class="line">Controls Winograd convolution algorithm.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM</span></code></div>
<div class="line">Controls implicit GEMM convolution algorithm.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMMED_FALLBACK</span></code></div>
<div class="line">Controls immediate fallback for convolution algorithms.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_ENABLE_AI_IMMED_MODE_FALLBACK</span></code></div>
<div class="line">Controls AI immediate mode fallback behavior.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_FORCE_IMMED_MODE_FALLBACK</span></code></div>
<div class="line">Forces immediate mode fallback for convolution operations.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="kernel-build-method-control">
<h2>Kernel build method control<a class="headerlink" href="#kernel-build-method-control" title="Link to this heading">#</a></h2>
<p>The kernel build method control environment variables for MIOpen are collected in the following table.
For more information, see <a class="reference internal" href="../how-to/debug-log.html"><span class="doc">Logging and debugging</span></a>.</p>
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
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_GCN_ASM_KERNELS</span></code></div>
<div class="line">Controls assembly language kernels for convolutions and batch normalization.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_HIP_KERNELS</span></code></div>
<div class="line">Controls HIP-written convolution kernels (ImplicitGemm algorithm).</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_OPENCL_CONVOLUTIONS</span></code></div>
<div class="line">Controls OpenCL-written convolution kernels.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_OPENCL_WAVE64_NOWGP</span></code></div>
<div class="line">Controls OpenCL Wave64 without workgroup behavior.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="solution-selection">
<h2>Solution selection<a class="headerlink" href="#solution-selection" title="Link to this heading">#</a></h2>
<p>The solution selection environment variables for MIOpen are collected in the following table.
For more information, see <a class="reference internal" href="../how-to/debug-log.html"><span class="doc">Logging and debugging</span></a>.</p>
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
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_FIND_ONLY_SOLVER</span></code></div>
<div class="line">Forces use of only one specific solution. Affects <code class="docutils literal notranslate"><span class="pre">*Find()</span></code> calls only.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">Numeric or string solution identifier</div>
<div class="line">If valid and applicable: only that solution is found</div>
<div class="line">If valid but not applicable: <code class="docutils literal notranslate"><span class="pre">*Find()</span></code> fails</div>
<div class="line">If invalid: <code class="docutils literal notranslate"><span class="pre">*Find()</span></code> call fails</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="direct-solution-control">
<h2>Direct solution control<a class="headerlink" href="#direct-solution-control" title="Link to this heading">#</a></h2>
<p>The direct solution control environment variables for MIOpen are collected in the following table.
For more information, see <a class="reference internal" href="../how-to/debug-log.html"><span class="doc">Logging and debugging</span></a>.</p>
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
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_DIRECT_ASM_3X3U</span></code></div>
<div class="line">Controls ConvAsm3x3U direct solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_DIRECT_ASM_1X1U</span></code></div>
<div class="line">Controls ConvAsm1x1U direct solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_DIRECT_ASM_1X1UV2</span></code></div>
<div class="line">Controls ConvAsm1x1UV2 direct solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_DIRECT_ASM_5X10U2V2</span></code></div>
<div class="line">Controls ConvAsm5x10u2v2f1 and ConvAsm5x10u2v2b1 direct solutions.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_DIRECT_ASM_7X7C3H224W224</span></code></div>
<div class="line">Controls ConvAsm7x7c3h224w224k64u2v2p3q3f1 direct solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_DIRECT_ASM_WRW3X3</span></code></div>
<div class="line">Controls ConvAsmBwdWrW3x3 direct solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_DIRECT_ASM_WRW1X1</span></code></div>
<div class="line">Controls ConvAsmBwdWrW1x1 direct solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_DIRECT_OCL_FWD11X11</span></code></div>
<div class="line">Controls ConvOclDirectFwd11x11 direct solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_DIRECT_OCL_FWDGEN</span></code></div>
<div class="line">Controls ConvOclDirectFwdGen direct solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_DIRECT_OCL_FWD</span></code></div>
<div class="line">Controls ConvOclDirectFwd direct solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_DIRECT_OCL_FWD1X1</span></code></div>
<div class="line">Controls ConvOclDirectFwd1x1 direct solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_DIRECT_OCL_WRW2</span></code></div>
<div class="line">Controls ConvOclBwdWrW2&lt;n&gt; (n={1,2,4,8,16}) and ConvOclBwdWrW2NonTunable solutions.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_DIRECT_OCL_WRW53</span></code></div>
<div class="line">Controls ConvOclBwdWrW53 direct solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_DIRECT_OCL_WRW1X1</span></code></div>
<div class="line">Controls ConvOclBwdWrW1x1 direct solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_DIRECT_ASM_1X1U_PERF_VALS</span></code></div>
<div class="line">Controls performance values for ConvAsm1x1U direct solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_DIRECT_ASM_1X1U_SEARCH_OPTIMIZED</span></code></div>
<div class="line">Controls optimized search for ConvAsm1x1U direct solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_DIRECT_ASM_1X1U_AI_HEUR</span></code></div>
<div class="line">Controls AI heuristics for ConvAsm1x1U direct solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_DIRECT_NAIVE_CONV_FWD</span></code></div>
<div class="line">Controls naive convolution forward direct solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="winograd-solution-control">
<h2>Winograd solution control<a class="headerlink" href="#winograd-solution-control" title="Link to this heading">#</a></h2>
<p>The Winograd solution control environment variables for MIOpen are collected in the following table.
For more information, see <a class="reference internal" href="../how-to/debug-log.html"><span class="doc">Logging and debugging</span></a>.</p>
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
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_3X3</span></code></div>
<div class="line">Controls ConvBinWinograd3x3U FP32 Winograd Fwd/Bwd (filter size 3x3).</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_RXS</span></code></div>
<div class="line">Controls ConvBinWinogradRxS FP32/FP16 F(3,3) Fwd/Bwd and FP32 F(3,2) WrW Winograd.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_RXS_WRW</span></code></div>
<div class="line">Controls FP32 F(3,2) WrW convolutions only (subset of <code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_RXS</span></code>).</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_RXS_FWD_BWD</span></code></div>
<div class="line">Controls FP32/FP16 F(3,3) Fwd/Bwd (subset of <code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_RXS</span></code>).</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_RXS_F3X2</span></code></div>
<div class="line">Controls ConvBinWinogradRxSf3x2 FP32/FP16 Fwd/Bwd F(3,2) Winograd.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_RXS_F2X3</span></code></div>
<div class="line">Controls ConvBinWinogradRxSf2x3 FP32/FP16 Fwd/Bwd F(2,3) Winograd (group convolutions only).</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_RXS_F2X3_G1</span></code></div>
<div class="line">Controls ConvBinWinogradRxSf2x3g1 FP32/FP16 Fwd/Bwd F(2,3) Winograd (non-group convolutions).</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_FUSED_WINOGRAD</span></code></div>
<div class="line">Controls Fused FP32 F(3,3) Winograd with variable filter size.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_RXS_F2X3_PERF_VALS</span></code></div>
<div class="line">Controls performance values for Winograd RxS F(2,3) solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_FURY_RXS_F2X3</span></code></div>
<div class="line">Controls Winograd Fury RxS F(2,3) solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_FURY_RXS_F3X2</span></code></div>
<div class="line">Controls Winograd Fury RxS F(3,2) solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="multi-pass-winograd-solution-control">
<h2>Multi-pass Winograd solution control<a class="headerlink" href="#multi-pass-winograd-solution-control" title="Link to this heading">#</a></h2>
<p>The multi-pass Winograd solution control environment variables for MIOpen are collected in the
following table. For more information, see <a class="reference internal" href="../how-to/debug-log.html"><span class="doc">Logging and debugging</span></a>.</p>
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
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_MPASS_F3X2</span></code></div>
<div class="line">Controls ConvWinograd3x3MultipassWrW&lt;3-2&gt; WrW F(3,2), stride 2 only.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_MPASS_F3X3</span></code></div>
<div class="line">Controls ConvWinograd3x3MultipassWrW&lt;3-3&gt; WrW F(3,3), stride 2 only.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_MPASS_F3X4</span></code></div>
<div class="line">Controls ConvWinograd3x3MultipassWrW&lt;3-4&gt; WrW F(3,4).</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_MPASS_F3X5</span></code></div>
<div class="line">Controls ConvWinograd3x3MultipassWrW&lt;3-5&gt; WrW F(3,5).</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_MPASS_F3X6</span></code></div>
<div class="line">Controls ConvWinograd3x3MultipassWrW&lt;3-6&gt; WrW F(3,6).</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_MPASS_F5X3</span></code></div>
<div class="line">Controls ConvWinograd3x3MultipassWrW&lt;5-3&gt; WrW F(5,3).</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_MPASS_F5X4</span></code></div>
<div class="line">Controls ConvWinograd3x3MultipassWrW&lt;5-4&gt; WrW F(5,4).</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_MPASS_F7X2</span></code></div>
<div class="line">Controls ConvWinograd3x3MultipassWrW&lt;7-2&gt;, &lt;7-2-1-1&gt;, and &lt;1-1-7-2&gt; WrW F(7,2) variants.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_MPASS_F7X3</span></code></div>
<div class="line">Controls ConvWinograd3x3MultipassWrW&lt;7-3&gt;, &lt;7-3-1-1&gt;, and &lt;1-1-7-3&gt; WrW F(7,3) variants.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_MP_BD_WINOGRAD_F2X3</span></code></div>
<div class="line">Controls ConvMPBidirectWinograd&lt;2-3&gt; FWD/BWD F(2,3).</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_MP_BD_WINOGRAD_F3X3</span></code></div>
<div class="line">Controls ConvMPBidirectWinograd&lt;3-3&gt; FWD/BWD F(3,3).</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_MP_BD_WINOGRAD_F4X3</span></code></div>
<div class="line">Controls ConvMPBidirectWinograd&lt;4-3&gt; FWD/BWD F(4,3).</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_MP_BD_WINOGRAD_F5X3</span></code></div>
<div class="line">Controls ConvMPBidirectWinograd&lt;5-3&gt; FWD/BWD F(5,3).</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_MP_BD_WINOGRAD_F6X3</span></code></div>
<div class="line">Controls ConvMPBidirectWinograd&lt;6-3&gt; FWD/BWD F(6,3).</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_MP_BD_XDLOPS_WINOGRAD_F2X3</span></code></div>
<div class="line">Controls ConvMPBidirectWinograd_xdlops&lt;2-3&gt; FWD/BWD F(2,3).</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_MP_BD_XDLOPS_WINOGRAD_F3X3</span></code></div>
<div class="line">Controls ConvMPBidirectWinograd_xdlops&lt;3-3&gt; FWD/BWD F(3,3).</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_MP_BD_XDLOPS_WINOGRAD_F4X3</span></code></div>
<div class="line">Controls ConvMPBidirectWinograd_xdlops&lt;4-3&gt; FWD/BWD F(4,3).</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_MP_BD_XDLOPS_WINOGRAD_F5X3</span></code></div>
<div class="line">Controls ConvMPBidirectWinograd_xdlops&lt;5-3&gt; FWD/BWD F(5,3).</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_MP_BD_XDLOPS_WINOGRAD_F6X3</span></code></div>
<div class="line">Controls ConvMPBidirectWinograd_xdlops&lt;6-3&gt; FWD/BWD F(6,3).</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_MP_BD_WINOGRAD_EXPEREMENTAL_FP16_TRANSFORM</span></code></div>
<div class="line">Controls ConvMPBidirectWinograd* FWD/BWD FP16 experimental mode (use at your own risk).</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_MPASS_WORKSPACE_MAX</span></code></div>
<div class="line">Sets workspace size limit for ConvWinograd3x3MultipassWrW solutions.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">Decimal or hex value (64-bit unsigned integer) in bytes</div>
<div class="line">Default: 2000000000 (~1.862 GiB) for gfx900 and gfx906/60</div>
<div class="line">0: Use default limit</div>
<div class="line">1: Prohibit workspace use</div>
<div class="line">-1: Remove default limit</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_MP_BD_WINOGRAD_WORKSPACE_MAX</span></code></div>
<div class="line">Sets workspace size limit for ConvMPBidirectWinograd solutions.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">Decimal or hex value (64-bit unsigned integer) in bytes</div>
<div class="line">0: Use default limit</div>
<div class="line">1: Prohibit workspace use</div>
<div class="line">-1: Remove default limit</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="asm-implicit-gemm-solution-control">
<h2>ASM implicit GEMM solution control<a class="headerlink" href="#asm-implicit-gemm-solution-control" title="Link to this heading">#</a></h2>
<p>The ASM implicit GEMM solution control environment variables for MIOpen are collected in the
following table. For more information, see <a class="reference internal" href="../how-to/debug-log.html"><span class="doc">Logging and debugging</span></a>.</p>
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
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_ASM_FWD_V4R1</span></code></div>
<div class="line">Controls ConvAsmImplicitGemmV4R1DynamicFwd solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_ASM_FWD_V4R1_1X1</span></code></div>
<div class="line">Controls ConvAsmImplicitGemmV4R1DynamicFwd_1x1 solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_ASM_BWD_V4R1</span></code></div>
<div class="line">Controls ConvAsmImplicitGemmV4R1DynamicBwd solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_ASM_WRW_V4R1</span></code></div>
<div class="line">Controls ConvAsmImplicitGemmV4R1DynamicWrw solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_ASM_FWD_GTC_XDLOPS</span></code></div>
<div class="line">Controls ConvAsmImplicitGemmGTCDynamicFwdXdlops solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_ASM_BWD_GTC_XDLOPS</span></code></div>
<div class="line">Controls ConvAsmImplicitGemmGTCDynamicBwdXdlops solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_ASM_WRW_GTC_XDLOPS</span></code></div>
<div class="line">Controls ConvAsmImplicitGemmGTCDynamicWrwXdlops solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_ASM_FWD_GTC_XDLOPS_NHWC</span></code></div>
<div class="line">Controls ConvAsmImplicitGemmGTCFwdXdlopsNHWC solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_ASM_BWD_GTC_XDLOPS_NHWC</span></code></div>
<div class="line">Controls ConvAsmImplicitGemmGTCBwdXdlopsNHWC solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_ASM_WRW_GTC_XDLOPS_NHWC</span></code></div>
<div class="line">Controls ConvAsmImplicitGemmGTCWrwXdlopsNHWC solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_ASM_FWD_GTC_DLOPS_NCHWC</span></code></div>
<div class="line">Controls ConvAsmImplicitGemmGTCFwdDlopsNCHWC solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_ASM_PK_ATOMIC_ADD_FP16</span></code></div>
<div class="line">Controls packed atomic add FP16 behavior for ASM implicit GEMM solutions.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable packed atomic add FP16</div>
<div class="line">1: Enable packed atomic add FP16</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_HIP_GROUP_BWD_XDLOPS</span></code></div>
<div class="line">Controls grouped convolution HIP implicit GEMM backward XDLOPS solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_GROUP_CONV_IMPLICIT_GEMM_HIP_BWD_XDLOPS_AI_HEUR</span></code></div>
<div class="line">Controls AI heuristics for grouped convolution HIP implicit GEMM backward XDLOPS.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_FWD_V4R4_XDLOPS_ADD_VECTOR_LOAD_GEMMN_TUNE_PARAM</span></code></div>
<div class="line">Controls vector load GEMM-N tuning parameters for implicit GEMM forward V4R4 XDLOPS.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="hip-implicit-gemm-solution-control">
<h2>HIP implicit GEMM solution control<a class="headerlink" href="#hip-implicit-gemm-solution-control" title="Link to this heading">#</a></h2>
<p>The HIP implicit GEMM solution control environment variables for MIOpen are collected in the
following table. For more information, see <a class="reference internal" href="../how-to/debug-log.html"><span class="doc">Logging and debugging</span></a>.</p>
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
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_HIP_FWD_V4R1</span></code></div>
<div class="line">Controls ConvHipImplicitGemmV4R1Fwd solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_HIP_FWD_V4R4</span></code></div>
<div class="line">Controls ConvHipImplicitGemmV4R4Fwd solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_HIP_BWD_V1R1</span></code></div>
<div class="line">Controls ConvHipImplicitGemmBwdDataV1R1 solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_HIP_BWD_V4R1</span></code></div>
<div class="line">Controls ConvHipImplicitGemmBwdDataV4R1 solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_HIP_WRW_V4R1</span></code></div>
<div class="line">Controls ConvHipImplicitGemmV4R1WrW solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_HIP_WRW_V4R4</span></code></div>
<div class="line">Controls ConvHipImplicitGemmV4R4WrW solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_HIP_FWD_V4R4_XDLOPS</span></code></div>
<div class="line">Controls ConvHipImplicitGemmForwardV4R4Xdlops solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_HIP_FWD_V4R5_XDLOPS</span></code></div>
<div class="line">Controls ConvHipImplicitGemmForwardV4R5Xdlops solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_HIP_BWD_V1R1_XDLOPS</span></code></div>
<div class="line">Controls ConvHipImplicitGemmBwdDataV1R1Xdlops solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_HIP_BWD_V4R1_XDLOPS</span></code></div>
<div class="line">Controls ConvHipImplicitGemmBwdDataV4R1Xdlops solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_HIP_WRW_V4R4_XDLOPS</span></code></div>
<div class="line">Controls ConvHipImplicitGemmWrwV4R4Xdlops solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_HIP_FWD_V4R4_PADDED_GEMM_XDLOPS</span></code></div>
<div class="line">Controls ConvHipImplicitGemmForwardV4R4Xdlops_Padded_Gemm solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_HIP_WRW_V4R4_PADDED_GEMM_XDLOPS</span></code></div>
<div class="line">Controls ConvHipImplicitGemmWrwV4R4Xdlops_Padded_Gemm solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_HIP_FWD_XDLOPS</span></code></div>
<div class="line">Controls ConvHipImplicitGemmFwdXdlops solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_HIP_BWD_XDLOPS</span></code></div>
<div class="line">Controls ConvHipImplicitGemmBwdXdlops solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_HIP_WRW_XDLOPS</span></code></div>
<div class="line">Controls ConvHipImplicitGemmWrwXdlops solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_XDLOPS</span></code></div>
<div class="line">Controls implicit GEMM XDLOPS solutions.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_XDLOPS_EMULATE</span></code></div>
<div class="line">Controls XDLOPS emulation for implicit GEMM solutions.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_IMPLICIT_GEMM_XDLOPS_INLINE_ASM</span></code></div>
<div class="line">Controls inline assembly for implicit GEMM XDLOPS solutions.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="d-implicit-gemm-solution-control">
<h2>3D implicit GEMM solution control<a class="headerlink" href="#d-implicit-gemm-solution-control" title="Link to this heading">#</a></h2>
<p>The 3D implicit GEMM solution control environment variables for MIOpen are collected in the
following table. For more information, see <a class="reference internal" href="../how-to/debug-log.html"><span class="doc">Logging and debugging</span></a>.</p>
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
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_3D_CONV_IMPLICIT_GEMM_HIP_FWD_XDLOPS</span></code></div>
<div class="line">Controls 3D ConvHipImplicitGemmFwdXdlops solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_3D_CONV_IMPLICIT_GEMM_HIP_BWD_XDLOPS</span></code></div>
<div class="line">Controls 3D ConvHipImplicitGemmBwdXdlops solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_3D_CONV_IMPLICIT_GEMM_HIP_WRW_XDLOPS</span></code></div>
<div class="line">Controls 3D ConvHipImplicitGemmWrwXdlops solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="gemm-backend-control">
<h2>GEMM backend control<a class="headerlink" href="#gemm-backend-control" title="Link to this heading">#</a></h2>
<p>The GEMM backend control environment variables for MIOpen are collected in the following table.
For more information, see <a class="reference internal" href="../how-to/debug-log.html"><span class="doc">Logging and debugging</span></a>.</p>
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
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_GEMM_ENFORCE_BACKEND</span></code></div>
<div class="line">Overrides default GEMM backend (rocBLAS).</div>
</div>
</td>
<td><div class="line-block">
<div class="line">1: Use rocBLAS if enabled</div>
<div class="line">2: Reserved</div>
<div class="line">3: No GEMM is called</div>
<div class="line">4: Reserved</div>
<div class="line">5: Use hipBLASLt if enabled</div>
<div class="line">Any other value: Use default behavior</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">ROCBLAS_LAYER</span></code></div>
<div class="line">Controls rocBLAS GEMM logging output.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">Unset: No logging</div>
<div class="line">1: Trace logging</div>
<div class="line">2: Bench logging</div>
<div class="line">3: Trace and bench logging</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">HIPBLASLT_LOG_LEVEL</span></code></div>
<div class="line">Controls hipBLASLt GEMM logging output.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Off (default)</div>
<div class="line">1: Error logging</div>
<div class="line">2: Trace (API calls with parameters)</div>
<div class="line">3: Hints (performance improvement suggestions)</div>
<div class="line">4: Info (general execution information)</div>
<div class="line">5: API trace (detailed API parameters)</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="convolution-attributes">
<h2>Convolution attributes<a class="headerlink" href="#convolution-attributes" title="Link to this heading">#</a></h2>
<p>The convolution attribute environment variables for MIOpen are collected in the following table.
For more information, see <a class="reference internal" href="../conceptual/MI200-alt-implementation.html"><span class="doc">MI200 alternate implementation</span></a>.</p>
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
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONVOLUTION_ATTRIB_FP16_ALT_IMPL</span></code></div>
<div class="line">Controls the alternate <code class="docutils literal notranslate"><span class="pre">FP16</span></code> implementation that uses the <code class="docutils literal notranslate"><span class="pre">BFloat16</span></code> larger exponent</div>
<div class="line">range for all convolution directions.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_CONVOLUTION_ATTRIB_FP16_ALT_IMPL</span></code></div>
<div class="line">Controls the alternate <code class="docutils literal notranslate"><span class="pre">FP16</span></code> implementation that uses the <code class="docutils literal notranslate"><span class="pre">BFloat16</span></code> larger exponent</div>
<div class="line">range (alternative to the miopenSetConvolutionAttribute API).</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONVOLUTION_DETERMINISTIC</span></code></div>
<div class="line">Controls deterministic convolution behavior.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONVOLUTION_ATTRIB_FP8_ROUNDING_MODE</span></code></div>
<div class="line">Controls FP8 rounding mode for convolution attributes.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">Integer value specifying FP8 rounding mode</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONVOLUTION_ATTRIB_FP8_ROUNDING_SEED</span></code></div>
<div class="line">Controls FP8 rounding seed for convolution attributes.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">Integer value specifying FP8 rounding seed</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="compilation-control">
<h2>Compilation control<a class="headerlink" href="#compilation-control" title="Link to this heading">#</a></h2>
<p>The compilation control environment variables for MIOpen are collected in the following table.
For more information, see <a class="reference internal" href="../how-to/debug-log.html"><span class="doc">Logging and debugging</span></a>.</p>
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
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_COMPILE_PARALLEL_LEVEL</span></code></div>
<div class="line">Controls parallel compilation thread count for <code class="docutils literal notranslate"><span class="pre">*Find()</span></code> calls.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">Integer value</div>
<div class="line">Default: 1 when using <code class="docutils literal notranslate"><span class="pre">COMGR</span></code>, otherwise half the number of available hardware threads</div>
<div class="line">1: Disable multi-threaded compilation</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_COMPILE_ONLY</span></code></div>
<div class="line">Controls compile-only mode for debugging.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="experimental-controls">
<h2>Experimental controls<a class="headerlink" href="#experimental-controls" title="Link to this heading">#</a></h2>
<p>The experimental control environment variables for MIOpen are collected in the following table.
For more information, see <a class="reference internal" href="../how-to/debug-log.html"><span class="doc">Logging and debugging</span></a>.</p>
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
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_ROCM_METADATA_ENFORCE</span></code></div>
<div class="line">Controls Code Object (CO) version for GCN assembly kernels.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0 or unset: Auto-detect CO version (default)</div>
<div class="line">1: Always assemble v2 COs</div>
<div class="line">2: Behave as if both v2 and v3 COs supported</div>
<div class="line">3: Always assemble v3 COs</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_ROCM_METADATA_PREFER_OLDER</span></code></div>
<div class="line">Prefers older CO format when both v2 and v3 are supported.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">1, “yes”, “true”, “enable”, “enabled”: Prefer v2 over v3</div>
<div class="line">0, “no”, “false”, “disable”, “disabled”: Use newer format</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_OPENCL_ENFORCE_CODE_OBJECT_VERSION</span></code></div>
<div class="line">Enforces CO format for OpenCL kernels (HIP backend only).</div>
</div>
</td>
<td><div class="line-block">
<div class="line">Unset: Auto-detect CO version (default)</div>
<div class="line">2: Always build to v2 CO</div>
<div class="line">3: Always build to v3 CO</div>
<div class="line">4: Always build to v4 CO</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="rnn-control">
<h2>RNN control<a class="headerlink" href="#rnn-control" title="Link to this heading">#</a></h2>
<p>The RNN control environment variables for MIOpen are collected in the following table.</p>
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
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_RNNBWDMS_EXP</span></code></div>
<div class="line">Controls experimental RNN backward multi-stream behavior.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_RNNBWMS_EXP</span></code></div>
<div class="line">Controls experimental RNN backward multi-stream behavior.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_RNN_DYNAMIC_FORCE</span></code></div>
<div class="line">Forces dynamic RNN behavior.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_RNNFWD_EXP</span></code></div>
<div class="line">Controls experimental RNN forward behavior.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_RNNFWD_MS_DISPATCH</span></code></div>
<div class="line">Controls multi-stream dispatch for RNN forward operations.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_RNN_MS_STREAM_CNT</span></code></div>
<div class="line">Controls stream count for RNN multi-stream operations.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">Integer value specifying stream count</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="composable-kernel-ck-solution-control">
<h2>Composable Kernel (CK) solution control<a class="headerlink" href="#composable-kernel-ck-solution-control" title="Link to this heading">#</a></h2>
<p>The Composable Kernel (CK) solution control environment variables for MIOpen are collected in the
following table.</p>
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
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_CK_IGEMM_FWD_V6R1_DLOPS_NCHW</span></code></div>
<div class="line">Controls CK implicit GEMM forward V6R1 DLOPS NCHW solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_CK_IGEMM_FWD_BIAS_ACTIV</span></code></div>
<div class="line">Controls CK implicit GEMM forward bias activation fused solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_CK_IGEMM_FWD_BIAS_RES_ADD_ACTIV</span></code></div>
<div class="line">Controls CK implicit GEMM forward bias residual add activation fused solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="mlir-solution-control">
<h2>MLIR solution control<a class="headerlink" href="#mlir-solution-control" title="Link to this heading">#</a></h2>
<p>The MLIR solution control environment variables for MIOpen are collected in the following table.</p>
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
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_MLIR_IGEMM_WRW_XDLOPS</span></code></div>
<div class="line">Controls MLIR implicit GEMM weight-gradient XDLOPS solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_MLIR_IGEMM_BWD_XDLOPS</span></code></div>
<div class="line">Controls MLIR implicit GEMM backward XDLOPS solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="attention-and-softmax-control">
<h2>Attention and softmax control<a class="headerlink" href="#attention-and-softmax-control" title="Link to this heading">#</a></h2>
<p>The attention and softmax control environment variables for MIOpen are collected in the following table.</p>
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
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_ATTN_SOFTMAX</span></code></div>
<div class="line">Controls attention softmax solution.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="driver-and-testing-advanced">
<h2>Driver and testing (Advanced)<a class="headerlink" href="#driver-and-testing-advanced" title="Link to this heading">#</a></h2>
<p>The driver and testing environment variables for MIOpen are collected in the following table. These
variables are primarily intended for testing and driver purposes.</p>
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
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DRIVER_PAD_BUFFERS_2M</span></code></div>
<div class="line">Controls 2M buffer padding in MIOpen driver.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DRIVER_USE_GPU_REFERENCE</span></code></div>
<div class="line">Controls GPU reference usage in MIOpen driver.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">0: Disable</div>
<div class="line">1: Enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">MIOPEN_DRIVER_SUBNORM_PERCENTAGE</span></code></div>
<div class="line">Controls subnormal percentage in MIOpen driver.</div>
</div>
</td>
<td><div class="line-block">
<div class="line">Integer value specifying subnormal percentage</div>
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
       href="datatypes.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Datatypes</p>
      </div>
    </a>
    <a class="right-next"
       href="../license.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">License</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#logging-and-debugging">Logging and debugging</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#find-mode-configuration">Find mode configuration</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#algorithm-control">Algorithm control</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#kernel-build-method-control">Kernel build method control</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#solution-selection">Solution selection</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#direct-solution-control">Direct solution control</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#winograd-solution-control">Winograd solution control</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#multi-pass-winograd-solution-control">Multi-pass Winograd solution control</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#asm-implicit-gemm-solution-control">ASM implicit GEMM solution control</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-implicit-gemm-solution-control">HIP implicit GEMM solution control</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#d-implicit-gemm-solution-control">3D implicit GEMM solution control</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#gemm-backend-control">GEMM backend control</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#convolution-attributes">Convolution attributes</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#compilation-control">Compilation control</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#experimental-controls">Experimental controls</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rnn-control">RNN control</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#composable-kernel-ck-solution-control">Composable Kernel (CK) solution control</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#mlir-solution-control">MLIR solution control</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#attention-and-softmax-control">Attention and softmax control</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#driver-and-testing-advanced">Driver and testing (Advanced)</a></li>
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
