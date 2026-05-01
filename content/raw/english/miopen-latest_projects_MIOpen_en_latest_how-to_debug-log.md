---
title: "Logging and debugging &#8212; MIOpen 3.5.1 Documentation"
source_url: "https://rocm.docs.amd.com/projects/MIOpen/en/latest/how-to/debug-log.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:11:11.511928+00:00
content_hash: "47b3b78c7c535a50"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="How to log and debug MIOpen" name="description" />
<meta content="MIOpen, ROCm, API, documentation, logging, debugging" name="keywords" />

    <title>Logging and debugging &#8212; MIOpen 3.5.1 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'how-to/debug-log';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />
    <link rel="next" title="Using the find APIs and immediate mode" href="find-and-immediate.html" />
    <link rel="prev" title="Using the fusion API" href="use-fusion-api.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-miopen" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/how-to/debug-log.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<ul class="current nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="use-fusion-api.html">Use the fusion API</a></li>
<li class="toctree-l1 current active"><a class="current reference internal" href="#">Log and debug</a></li>
<li class="toctree-l1"><a class="reference internal" href="find-and-immediate.html">Use the find APIs and immediate mode</a></li>
<li class="toctree-l1"><a class="reference internal" href="use-nhwc-batchnorm-in-pytorch.html">Use NHWC Batch Normalization with PyTorch</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Samples</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference external" href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/miopen/samples">MIOpen samples</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Reference</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1 has-children"><a class="reference internal" href="../reference/index.html">API library</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2"><a class="reference internal" href="../doxygen/html/modules.html">Modules</a></li>
<li class="toctree-l2"><a class="reference internal" href="../reference/datatypes.html">Datatypes</a></li>
<li class="toctree-l2"><a class="reference internal" href="../reference/env_variables.html">Environment variables</a></li>
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
    <li class="breadcrumb-item active" aria-current="page"><span class="ellipsis">Logging and debugging</span></li>
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
    <h1>Logging and debugging</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#layer-filtering">Layer filtering</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#filtering-by-algorithm">Filtering by algorithm</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#filtering-by-build-method">Filtering by build method</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#filtering-out-all-but-one-solution">Filtering out all but one solution</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#filtering-the-solutions-on-an-individual-basis">Filtering the solutions on an individual basis</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#gemm-logging-and-behavior">GEMM logging and behavior</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#numerical-checking">Numerical checking</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#check-for-gpu-sub-buffer-out-of-bounds-memory-accesses">Check for GPU sub-buffer out-of-bounds memory accesses</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#controlling-parallel-compilation">Controlling parallel compilation</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#experimental-controls">Experimental controls</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#code-object-version-selection-experimental">Code Object version selection (experimental)</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#winograd-multi-pass-maximum-workspace-throttling">Winograd multi-pass maximum workspace throttling</a></li>
</ul>
</li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="logging-and-debugging">
<h1>Logging and debugging<a class="headerlink" href="#logging-and-debugging" title="Link to this heading">#</a></h1>
<p>All logging messages are output to the standard error stream (<code class="docutils literal notranslate"><span class="pre">stderr</span></code>). You can use the following
environmental variables to control logging. Both variables are disabled by default.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_ENABLE_LOGGING</span></code>: Prints the basic layer-by-layer MIOpen API call
information with the actual parameters and configurations. This information is important for debugging.</p>
<ul>
<li><p>To enable the feature: <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">on</span></code>, <code class="docutils literal notranslate"><span class="pre">yes</span></code>, <code class="docutils literal notranslate"><span class="pre">true</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>, or <code class="docutils literal notranslate"><span class="pre">enabled</span></code></p></li>
<li><p>To disable the feature: <code class="docutils literal notranslate"><span class="pre">0</span></code>, <code class="docutils literal notranslate"><span class="pre">off</span></code>, <code class="docutils literal notranslate"><span class="pre">no</span></code>, <code class="docutils literal notranslate"><span class="pre">false</span></code>, <code class="docutils literal notranslate"><span class="pre">disable</span></code>, or <code class="docutils literal notranslate"><span class="pre">disabled</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_ENABLE_LOGGING_CMD</span></code>: Outputs the associated <code class="docutils literal notranslate"><span class="pre">MIOpenDriver</span></code> command lines to the
console.</p>
<ul>
<li><p>To enable the feature: <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">on</span></code>, <code class="docutils literal notranslate"><span class="pre">yes</span></code>, <code class="docutils literal notranslate"><span class="pre">true</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>, or <code class="docutils literal notranslate"><span class="pre">enabled</span></code></p></li>
<li><p>To disable the feature: <code class="docutils literal notranslate"><span class="pre">0</span></code>, <code class="docutils literal notranslate"><span class="pre">off</span></code>, <code class="docutils literal notranslate"><span class="pre">no</span></code>, <code class="docutils literal notranslate"><span class="pre">false</span></code>, <code class="docutils literal notranslate"><span class="pre">disable</span></code>, or <code class="docutils literal notranslate"><span class="pre">disabled</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_LOG_LEVEL</span></code>: In addition to API call information and driver commands, MIOpen logs
information related to the progress of its internal operations. This information can be useful for
debugging and understanding how the library works. <code class="docutils literal notranslate"><span class="pre">MIOPEN_LOG_LEVEL</span></code> controls the
verbosity of these messages. The allowed values are:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">0</span></code>: Default. Works as level <code class="docutils literal notranslate"><span class="pre">4</span></code> for release builds and level <code class="docutils literal notranslate"><span class="pre">5</span></code> for debug builds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">1</span></code>: Quiet. No logging messages.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">2</span></code>: Fatal errors only (unused).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">3</span></code>: Errors, including fatal errors.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">4</span></code>: All errors and warnings.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">5</span></code>: Info. All the preceding information, plus information for debugging purposes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">6</span></code>: Detailed information. All the preceding information, plus more detailed information for
debugging.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">7</span></code>: Trace. All the preceding information, plus additional details.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_ENABLE_LOGGING_MPMT</span></code>: Each log line is prefixed with information
to identify records printed from different processes or threads. This is useful for debugging
multi-process and multi-threaded applications.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_ENABLE_LOGGING_ELAPSED_TIME</span></code>: Adds a timestamp to each log line that indicates the
time elapsed (in milliseconds) since the previous log message.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_ENABLE_LOGGING_DATE_TIME</span></code>: Adds a timestamp to each log line that indicates the
system time (with milliseconds).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_WARN_SEARCH</span></code>: Elevate log messages for Search to warnings.</p></li>
</ul>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>If you require technical support, include the console log that is produced from these settings:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="k">export</span><span class="w"> </span><span class="n">MIOPEN_ENABLE_LOGGING</span><span class="o">=</span><span class="mi">1</span>
<span class="k">export</span><span class="w"> </span><span class="n">MIOPEN_ENABLE_LOGGING_CMD</span><span class="o">=</span><span class="mi">1</span>
<span class="k">export</span><span class="w"> </span><span class="n">MIOPEN_LOG_LEVEL</span><span class="o">=</span><span class="mi">6</span>
</pre></div>
</div>
</div>
<section id="layer-filtering">
<h2>Layer filtering<a class="headerlink" href="#layer-filtering" title="Link to this heading">#</a></h2>
<p>The following sections describe environment variables for enabling or disabling various
types of kernels and algorithms. These are helpful for debugging MIOpen and framework integrations.</p>
<p>For these environment variables, you can use the following values:</p>
<ul class="simple">
<li><p>To enable the kernel/algorithm: <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">yes</span></code>, <code class="docutils literal notranslate"><span class="pre">true</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>, or <code class="docutils literal notranslate"><span class="pre">enabled</span></code></p></li>
<li><p>To disable the kernel/algorithm: <code class="docutils literal notranslate"><span class="pre">0</span></code>, <code class="docutils literal notranslate"><span class="pre">no</span></code>, <code class="docutils literal notranslate"><span class="pre">false</span></code>, <code class="docutils literal notranslate"><span class="pre">disable</span></code>, or <code class="docutils literal notranslate"><span class="pre">disabled</span></code></p></li>
</ul>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>When you use the library with layer filtering, the results of <code class="docutils literal notranslate"><span class="pre">*Find()</span></code> calls become narrower than
during normal operation. This means that relevant FindDb entries won’t include all the solutions that
are normally present. Therefore, the subsequent immediate mode <code class="docutils literal notranslate"><span class="pre">*Get()</span></code> calls may return incomplete
information or run into the fallback path.</p>
</div>
<p>In order to repair immediate mode, you can:</p>
<ul class="simple">
<li><p>Re-enable all solvers and rerun the same <code class="docutils literal notranslate"><span class="pre">*Find()</span></code> calls from before</p></li>
<li><p>Completely remove the User FindDb</p></li>
</ul>
<p>If a variable is not set, MIOpen treats it as <code class="docutils literal notranslate"><span class="pre">enabled</span></code>. This means that kernels and
algorithms are enabled by default.</p>
<section id="filtering-by-algorithm">
<h3>Filtering by algorithm<a class="headerlink" href="#filtering-by-algorithm" title="Link to this heading">#</a></h3>
<p>These variables control the sets (families) of convolution solutions. For example, the direct algorithm
is implemented in several solutions that use OpenCL and GCN assembly. The corresponding variable
is used to disable them.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_FFT</span></code>: FFT convolution algorithm.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_DIRECT</span></code>: Direct convolution algorithm.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_GEMM</span></code>: GEMM convolution algorithm.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_WINOGRAD</span></code>: Winograd convolution algorithm.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM</span></code>: Implicit GEMM convolution algorithm.</p></li>
</ul>
</section>
<section id="filtering-by-build-method">
<h3>Filtering by build method<a class="headerlink" href="#filtering-by-build-method" title="Link to this heading">#</a></h3>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_GCN_ASM_KERNELS</span></code>: Kernels written in assembly language. These are used in
many convolutions (some direct solvers, Winograd kernels, and fused convolutions) and batch
normalization.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_HIP_KERNELS</span></code>: Convolution kernels written in HIP. These implement the
ImplicitGemm algorithm.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_OPENCL_CONVOLUTIONS</span></code>: Convolution kernels written in OpenCL. This only
affects convolutions.</p></li>
</ul>
</section>
<section id="filtering-out-all-but-one-solution">
<h3>Filtering out all but one solution<a class="headerlink" href="#filtering-out-all-but-one-solution" title="Link to this heading">#</a></h3>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_FIND_ONLY_SOLVER=solution_id</span></code>: Only directly affects <code class="docutils literal notranslate"><span class="pre">*Find()</span></code> calls. However,
there is an indirect connection to immediate mode (see the previous warning).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">solution_id</span></code> must be a numeric or a string identifier of some solution.</p></li>
<li><p>If the <code class="docutils literal notranslate"><span class="pre">solution_id</span></code> denotes an applicable solution, then only that solution is found (in addition to
GEMM and FFT, if applicable). See the note in this section.</p></li>
<li><p>If the <code class="docutils literal notranslate"><span class="pre">solution_id</span></code> is valid, but not applicable, then <code class="docutils literal notranslate"><span class="pre">*Find()</span></code> fails with all algorithms (except for GEMM
and FFT). See the note in this section.</p></li>
<li><p>Otherwise, the <code class="docutils literal notranslate"><span class="pre">solution_id</span></code> is invalid (for instance, it doesn’t match any existing solution) and the <code class="docutils literal notranslate"><span class="pre">*Find()</span></code>
call fails.</p></li>
</ul>
</li>
</ul>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This environmental variable doesn’t affect the GEMM and FFT solutions. For now, GEMM and FFT can
only be disabled at the algorithm level.</p>
</div>
</section>
<section id="filtering-the-solutions-on-an-individual-basis">
<h3>Filtering the solutions on an individual basis<a class="headerlink" href="#filtering-the-solutions-on-an-individual-basis" title="Link to this heading">#</a></h3>
<p>Some of the solutions have individual controls, which affect both find and immediate modes.</p>
<ul class="simple">
<li><p>Direct solutions:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_DIRECT_ASM_3X3U</span></code> – <code class="docutils literal notranslate"><span class="pre">ConvAsm3x3U</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_DIRECT_ASM_1X1U</span></code> – <code class="docutils literal notranslate"><span class="pre">ConvAsm1x1U</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_DIRECT_ASM_1X1UV2</span></code> – <code class="docutils literal notranslate"><span class="pre">ConvAsm1x1UV2</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_DIRECT_ASM_5X10U2V2</span></code> – <code class="docutils literal notranslate"><span class="pre">ConvAsm5x10u2v2f1`,</span> <span class="pre">`ConvAsm5x10u2v2b1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_DIRECT_ASM_7X7C3H224W224</span></code> – <code class="docutils literal notranslate"><span class="pre">ConvAsm7x7c3h224w224k64u2v2p3q3f1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_DIRECT_ASM_WRW3X3</span></code> – <code class="docutils literal notranslate"><span class="pre">ConvAsmBwdWrW3x3</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_DIRECT_ASM_WRW1X1</span></code> – <code class="docutils literal notranslate"><span class="pre">ConvAsmBwdWrW1x1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_DIRECT_OCL_FWD11X11</span></code> – <code class="docutils literal notranslate"><span class="pre">ConvOclDirectFwd11x11</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_DIRECT_OCL_FWDGEN</span></code> – <code class="docutils literal notranslate"><span class="pre">ConvOclDirectFwdGen</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_DIRECT_OCL_FWD</span></code> – <code class="docutils literal notranslate"><span class="pre">ConvOclDirectFwd</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_DIRECT_OCL_FWD1X1</span></code> – <code class="docutils literal notranslate"><span class="pre">ConvOclDirectFwd1x1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_DIRECT_OCL_WRW2</span></code> – <code class="docutils literal notranslate"><span class="pre">ConvOclBwdWrW2&lt;n&gt;</span></code> (where n =
<code class="docutils literal notranslate"><span class="pre">{1,2,4,8,16}</span></code>) and <code class="docutils literal notranslate"><span class="pre">ConvOclBwdWrW2NonTunable</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_DIRECT_OCL_WRW53</span></code> – <code class="docutils literal notranslate"><span class="pre">ConvOclBwdWrW53</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_DIRECT_OCL_WRW1X1</span></code> – <code class="docutils literal notranslate"><span class="pre">ConvOclBwdWrW1x1</span></code></p></li>
</ul>
</li>
<li><p>Winograd solutions:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_3X3</span></code> – <code class="docutils literal notranslate"><span class="pre">ConvBinWinograd3x3U</span></code>, <code class="docutils literal notranslate"><span class="pre">FP32</span></code> Winograd Fwd/Bwd,
filter size fixed to 3x3</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_RXS</span></code> – <code class="docutils literal notranslate"><span class="pre">ConvBinWinogradRxS</span></code>, <code class="docutils literal notranslate"><span class="pre">FP32</span></code>/<code class="docutils literal notranslate"><span class="pre">FP16</span></code> F(3,3) Fwd/Bwd
and <code class="docutils literal notranslate"><span class="pre">FP32</span></code> F(3,2) WrW Winograd. Subsets include:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_RXS_WRW</span></code> – <code class="docutils literal notranslate"><span class="pre">FP32</span></code> F(3,2) WrW convolutions only</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_RXS_FWD_BWD</span></code> – <code class="docutils literal notranslate"><span class="pre">FP32</span></code>/<code class="docutils literal notranslate"><span class="pre">FP16</span></code> F(3,3) Fwd/Bwd</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_RXS_F3X2</span></code> – <code class="docutils literal notranslate"><span class="pre">ConvBinWinogradRxSf3x2</span></code>, <code class="docutils literal notranslate"><span class="pre">FP32</span></code>/<code class="docutils literal notranslate"><span class="pre">FP16</span></code>
Fwd/Bwd F(3,2) Winograd</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_RXS_F2X3</span></code> – <code class="docutils literal notranslate"><span class="pre">ConvBinWinogradRxSf2x3</span></code>, <code class="docutils literal notranslate"><span class="pre">FP32</span></code>/<code class="docutils literal notranslate"><span class="pre">FP16</span></code>
Fwd/Bwd F(2,3) Winograd, serves group convolutions only</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_RXS_F2X3_G1</span></code> – <code class="docutils literal notranslate"><span class="pre">ConvBinWinogradRxSf2x3g1</span></code>, <code class="docutils literal notranslate"><span class="pre">FP32</span></code>/<code class="docutils literal notranslate"><span class="pre">FP16</span></code>
Fwd/Bwd F(2,3) Winograd, for non-group convolutions</p></li>
</ul>
</li>
<li><p>Multi-pass Winograd:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_MPASS_F3X2</span></code> – <code class="docutils literal notranslate"><span class="pre">ConvWinograd3x3MultipassWrW&lt;3-2&gt;</span></code>,
WrW F(3,2), stride 2 only</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_MPASS_F3X3</span></code> – <code class="docutils literal notranslate"><span class="pre">ConvWinograd3x3MultipassWrW&lt;3-3&gt;</span></code>,
WrW F(3,3), stride 2 only</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_MPASS_F3X4</span></code> – <code class="docutils literal notranslate"><span class="pre">ConvWinograd3x3MultipassWrW&lt;3-4&gt;</span></code>,
WrW F(3,4)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_MPASS_F3X5</span></code> – <code class="docutils literal notranslate"><span class="pre">ConvWinograd3x3MultipassWrW&lt;3-5&gt;</span></code>,
WrW F(3,5)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_MPASS_F3X6</span></code> – <code class="docutils literal notranslate"><span class="pre">ConvWinograd3x3MultipassWrW&lt;3-6&gt;</span></code>,
WrW F(3,6)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_MPASS_F5X3</span></code> – <code class="docutils literal notranslate"><span class="pre">ConvWinograd3x3MultipassWrW&lt;5-3&gt;</span></code>,
WrW F(5,3)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_MPASS_F5X4</span></code> – <code class="docutils literal notranslate"><span class="pre">ConvWinograd3x3MultipassWrW&lt;5-4&gt;</span></code>,
WrW F(5,4)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_MPASS_F7X2</span></code>:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ConvWinograd3x3MultipassWrW&lt;7-2&gt;</span></code>, WrW F(7,2)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ConvWinograd3x3MultipassWrW&lt;7-2-1-1&gt;</span></code>, WrW F(7x1,2x1)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ConvWinograd3x3MultipassWrW&lt;1-1-7-2&gt;</span></code>, WrW F(1x7,1x2)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_MPASS_F7X3</span></code>:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ConvWinograd3x3MultipassWrW&lt;7-3&gt;</span></code>, WrW F(7,3)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ConvWinograd3x3MultipassWrW&lt;7-3-1-1&gt;</span></code>, WrW F(7x1,3x1)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ConvWinograd3x3MultipassWrW&lt;1-1-7-3&gt;</span></code>, WrW F(1x7,1x3)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_MP_BD_WINOGRAD_F2X3</span></code> – <code class="docutils literal notranslate"><span class="pre">ConvMPBidirectWinograd&lt;2-3&gt;</span></code>,
FWD/BWD F(2,3)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_MP_BD_WINOGRAD_F3X3</span></code> – <code class="docutils literal notranslate"><span class="pre">ConvMPBidirectWinograd&lt;3-3&gt;</span></code>,
FWD/BWD F(3,3)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_MP_BD_WINOGRAD_F4X3</span></code> – <code class="docutils literal notranslate"><span class="pre">ConvMPBidirectWinograd&lt;4-3&gt;</span></code>,
FWD/BWD F(4,3)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_MP_BD_WINOGRAD_F5X3</span></code> – <code class="docutils literal notranslate"><span class="pre">ConvMPBidirectWinograd&lt;5-3&gt;</span></code>,
FWD/BWD F(5,3)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_MP_BD_WINOGRAD_F6X3</span></code> – <code class="docutils literal notranslate"><span class="pre">ConvMPBidirectWinograd&lt;6-3&gt;</span></code>,
FWD/BWD F(6,3)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_MP_BD_XDLOPS_WINOGRAD_F2X3</span></code> –
<code class="docutils literal notranslate"><span class="pre">ConvMPBidirectWinograd_xdlops&lt;2-3&gt;</span></code>, FWD/BWD F(2,3)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_MP_BD_XDLOPS_WINOGRAD_F3X3</span></code> –
<code class="docutils literal notranslate"><span class="pre">ConvMPBidirectWinograd_xdlops&lt;3-3&gt;</span></code>, FWD/BWD F(3,3)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_MP_BD_XDLOPS_WINOGRAD_F4X3</span></code> –
<code class="docutils literal notranslate"><span class="pre">ConvMPBidirectWinograd_xdlops&lt;4-3&gt;</span></code>, FWD/BWD F(4,3)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_MP_BD_XDLOPS_WINOGRAD_F5X3</span></code> –
<code class="docutils literal notranslate"><span class="pre">ConvMPBidirectWinograd_xdlops&lt;5-3&gt;</span></code>, FWD/BWD F(5,3)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_MP_BD_XDLOPS_WINOGRAD_F6X3</span></code> –
<code class="docutils literal notranslate"><span class="pre">ConvMPBidirectWinograd_xdlops&lt;6-3&gt;</span></code>, FWD/BWD F(6,3)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_MP_BD_WINOGRAD_EXPEREMENTAL_FP16_TRANSFORM</span></code> –
<code class="docutils literal notranslate"><span class="pre">ConvMPBidirectWinograd*</span></code>, FWD/BWD FP16 experimental mode (use at your own risk). Disabled
by default.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_FUSED_WINOGRAD</span></code> – Fused <code class="docutils literal notranslate"><span class="pre">FP32</span></code> F(3,3) Winograd, variable filter size.</p></li>
</ul>
</li>
</ul>
<p>Implicit GEMM solutions:</p>
<ul class="simple">
<li><p>ASM implicit GEMM</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_ASM_FWD_V4R1</span></code> –
<code class="docutils literal notranslate"><span class="pre">ConvAsmImplicitGemmV4R1DynamicFwd</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_ASM_FWD_V4R1_1X1</span></code> –
<code class="docutils literal notranslate"><span class="pre">ConvAsmImplicitGemmV4R1DynamicFwd_1x1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_ASM_BWD_V4R1</span></code> –
<code class="docutils literal notranslate"><span class="pre">ConvAsmImplicitGemmV4R1DynamicBwd</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_ASM_WRW_V4R1</span></code> –
<code class="docutils literal notranslate"><span class="pre">ConvAsmImplicitGemmV4R1DynamicWrw</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_ASM_FWD_GTC_XDLOPS</span></code> –
<code class="docutils literal notranslate"><span class="pre">ConvAsmImplicitGemmGTCDynamicFwdXdlops</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_ASM_BWD_GTC_XDLOPS</span></code> –
<code class="docutils literal notranslate"><span class="pre">ConvAsmImplicitGemmGTCDynamicBwdXdlops</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_ASM_WRW_GTC_XDLOPS</span></code> –
<code class="docutils literal notranslate"><span class="pre">ConvAsmImplicitGemmGTCDynamicWrwXdlops</span></code></p></li>
</ul>
</li>
<li><p>HIP implicit GEMM</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_HIP_FWD_V4R1</span></code> –
<code class="docutils literal notranslate"><span class="pre">ConvHipImplicitGemmV4R1Fwd</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_HIP_FWD_V4R4</span></code> –
<code class="docutils literal notranslate"><span class="pre">ConvHipImplicitGemmV4R4Fwd</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_HIP_BWD_V1R1</span></code> –
<code class="docutils literal notranslate"><span class="pre">ConvHipImplicitGemmBwdDataV1R1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_HIP_BWD_V4R1</span></code> –
<code class="docutils literal notranslate"><span class="pre">ConvHipImplicitGemmBwdDataV4R1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_HIP_WRW_V4R1</span></code> –
<code class="docutils literal notranslate"><span class="pre">ConvHipImplicitGemmV4R1WrW</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_HIP_WRW_V4R4</span></code> –
<code class="docutils literal notranslate"><span class="pre">ConvHipImplicitGemmV4R4WrW</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_HIP_FWD_V4R4_XDLOPS</span></code> –
<code class="docutils literal notranslate"><span class="pre">ConvHipImplicitGemmForwardV4R4Xdlops</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_HIP_FWD_V4R5_XDLOPS</span></code> –
<code class="docutils literal notranslate"><span class="pre">ConvHipImplicitGemmForwardV4R5Xdlops</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_HIP_BWD_V1R1_XDLOPS</span></code> –
<code class="docutils literal notranslate"><span class="pre">ConvHipImplicitGemmBwdDataV1R1Xdlops</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_HIP_BWD_V4R1_XDLOPS</span></code> –
<code class="docutils literal notranslate"><span class="pre">ConvHipImplicitGemmBwdDataV4R1Xdlops</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_HIP_WRW_V4R4_XDLOPS</span></code> –
<code class="docutils literal notranslate"><span class="pre">ConvHipImplicitGemmWrwV4R4Xdlops</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_HIP_FWD_V4R4_PADDED_GEMM_XDLOPS</span></code> –
<code class="docutils literal notranslate"><span class="pre">ConvHipImplicitGemmForwardV4R4Xdlops_Padded_Gemm</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_IMPLICIT_GEMM_HIP_WRW_V4R4_PADDED_GEMM_XDLOPS</span></code> –
<code class="docutils literal notranslate"><span class="pre">ConvHipImplicitGemmWrwV4R4Xdlops_Padded_Gemm</span></code></p></li>
</ul>
</li>
</ul>
</section>
</section>
<section id="gemm-logging-and-behavior">
<h2>GEMM logging and behavior<a class="headerlink" href="#gemm-logging-and-behavior" title="Link to this heading">#</a></h2>
<p>The <code class="docutils literal notranslate"><span class="pre">ROCBLAS_LAYER</span></code> environmental variable can be set to output GEMM information when using the rocBLAS GEMM backend:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ROCBLAS_LAYER=</span></code>: No logging (not set)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ROCBLAS_LAYER=1</span></code>: Trace logging</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ROCBLAS_LAYER=2</span></code>: Bench logging</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ROCBLAS_LAYER=3</span></code>: Trace and bench logging</p></li>
</ul>
<p>The <code class="docutils literal notranslate"><span class="pre">HIPBLASLT_LOG_LEVEL</span></code> environmental variable can be set to output GEMM information when using the hipBLASLt GEMM backend:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">HIPBLASLT_LOG_LEVEL=0</span></code>: Off – no logging (default)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">HIPBLASLT_LOG_LEVEL=1</span></code>: Error logging</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">HIPBLASLT_LOG_LEVEL=2</span></code>: Trace - API calls that launch HIP kernels log their parameters and important information</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">HIPBLASLT_LOG_LEVEL=3</span></code>: Hints - Hints that can potentially improve the application’s performance</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">HIPBLASLT_LOG_LEVEL=4</span></code>: Info - Provides general information about the library execution. Can contain details about heuristic status</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">HIPBLASLT_LOG_LEVEL=5</span></code>: API Trace - API calls log their parameters and important information</p></li>
</ul>
<p>You can also set the <code class="docutils literal notranslate"><span class="pre">MIOPEN_GEMM_ENFORCE_BACKEND</span></code> environment variable to override the
default GEMM backend, which is rocBLAS:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_GEMM_ENFORCE_BACKEND=1</span></code>: Use rocBLAS if enabled</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_GEMM_ENFORCE_BACKEND=2</span></code>: Reserved</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_GEMM_ENFORCE_BACKEND=3</span></code>: No GEMM is called</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_GEMM_ENFORCE_BACKEND=4</span></code>: Reserved</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_GEMM_ENFORCE_BACKEND=5</span></code>: Use hipBLASLt if enabled</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_GEMM_ENFORCE_BACKEND=&lt;any</span> <span class="pre">other</span> <span class="pre">value&gt;</span></code>: Use default behavior</p></li>
</ul>
<p>To disable the use of rocBLAS entirely, set the <code class="docutils literal notranslate"><span class="pre">-DMIOPEN_USE_ROCBLAS=Off</span></code> configuration flag during
MIOpen configuration. To disable the use of hipBLASLt entirely, set the <code class="docutils literal notranslate"><span class="pre">-DMIOPEN_USE_HIPBLASLT=Off</span></code> configuration flag during
MIOpen configuration.</p>
<p>For more information on how to use logging with rocBLAS, see the
<a class="reference external" href="https://rocm.docs.amd.com/projects/rocBLAS/en/latest/how-to/Programmers_Guide.html" title="(in rocBLAS Documentation v5.2.0)"><span class="xref std std-doc">rocBLAS programmer guide</span></a>.</p>
</section>
<section id="numerical-checking">
<h2>Numerical checking<a class="headerlink" href="#numerical-checking" title="Link to this heading">#</a></h2>
<p>Use the <code class="docutils literal notranslate"><span class="pre">MIOPEN_CHECK_NUMERICS</span></code> environmental variable to debug potential numerical
abnormalities. When this variable is set, MIOpen scans all inputs and outputs for each kernel called and attempts to
detect infinities (<code class="docutils literal notranslate"><span class="pre">infs</span></code>), not-a-number (<code class="docutils literal notranslate"><span class="pre">NaN</span></code>), and all zeros. This environment variable has several
settings to help with debugging:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_CHECK_NUMERICS=0x01</span></code>: Fully informative. Prints results from all checks to console.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_CHECK_NUMERICS=0x02</span></code>: Warning information. Prints results only if an abnormality is
detected.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_CHECK_NUMERICS=0x04</span></code>: Throw error on detection. MIOpen runs <code class="docutils literal notranslate"><span class="pre">MIOPEN_THROW</span></code>
upon an abnormal result.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_CHECK_NUMERICS=0x08</span></code>: Abort upon an abnormal result. Lets you drop into a
debugging session.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_CHECK_NUMERICS=0x10</span></code>: Print stats. Computes and prints mean/absmean/min/max
(note that this is slow).</p></li>
</ul>
</section>
<section id="check-for-gpu-sub-buffer-out-of-bounds-memory-accesses">
<span id="control-parallel-compilation"></span><h2>Check for GPU sub-buffer out-of-bounds memory accesses<a class="headerlink" href="#check-for-gpu-sub-buffer-out-of-bounds-memory-accesses" title="Link to this heading">#</a></h2>
<p>Use the <code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CHECK_SUB_BUFFER_OOB_MEMORY_ACCESS</span></code> to help debug potential out-of-bounds (OOBs)
memory access errors on GPU sub-buffers.  If the environment variable is undefined or set to zero, then no
sub-buffer out-of-bounds detection is performed. To verify the memory accesses, use one of these values:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CHECK_SUB_BUFFER_OOB_MEMORY_ACCESS=1</span></code>: Check for OOBs before the start of the sub-buffers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CHECK_SUB_BUFFER_OOB_MEMORY_ACCESS=2</span></code>: Check for OOBs after the end of the sub-buffers.</p></li>
</ul>
<p>Note that these checks are not intended for production use because they might cause a performance hit.</p>
</section>
<section id="controlling-parallel-compilation">
<h2>Controlling parallel compilation<a class="headerlink" href="#controlling-parallel-compilation" title="Link to this heading">#</a></h2>
<p>MIOpen’s convolution <code class="docutils literal notranslate"><span class="pre">*Find()</span></code> calls compile and benchmark a set of <code class="docutils literal notranslate"><span class="pre">solvers</span></code> contained in
<code class="docutils literal notranslate"><span class="pre">miopenConvAlgoPerf_t</span></code>. This is done in parallel with <code class="docutils literal notranslate"><span class="pre">miopenConvAlgorithm_t</span></code>. Parallelism per
algorithm is set to 20 threads. Typically, there are far fewer threads spawned due to the limited number
of kernels under any given algorithm.</p>
<p>You can control the level of parallelism using the <code class="docutils literal notranslate"><span class="pre">MIOPEN_COMPILE_PARALLEL_LEVEL</span></code> environment
variable.</p>
<p>To disable multi-threaded compilation, run:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="k">export</span><span class="w"> </span><span class="n">MIOPEN_COMPILE_PARALLEL_LEVEL</span><span class="o">=</span><span class="mi">1</span>
</pre></div>
</div>
</section>
<section id="experimental-controls">
<h2>Experimental controls<a class="headerlink" href="#experimental-controls" title="Link to this heading">#</a></h2>
<p>Using experimental controls might result in:</p>
<ul class="simple">
<li><p>Performance drops</p></li>
<li><p>Computation inaccuracies</p></li>
<li><p>Runtime errors</p></li>
<li><p>Other kinds of unexpected behavior</p></li>
</ul>
<p>We strongly recommended only using these controls at the explicit request of the library developers.</p>
<section id="code-object-version-selection-experimental">
<h3>Code Object version selection (experimental)<a class="headerlink" href="#code-object-version-selection-experimental" title="Link to this heading">#</a></h3>
<p>Different ROCm versions use Code Object (CO) files from different versions (formats). The library
automatically uses the most suitable version. The following variables allow for experimenting and
triaging possible problems related to the CO version:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_ROCM_METADATA_ENFORCE</span></code>: Affects kernels written in GCN assembly
language.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">0</span></code> (or unset): Automatically detects the required CO version and assembles the files to that version. This is
the default.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">1</span></code>: Do not auto-detect the CO version and always assemble v2 COs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">2</span></code>: Behave as if both v2 and v3 COs are supported (see
<code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_ROCM_METADATA_PREFER_OLDER</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">3</span></code>: Always assemble v3 COs.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_ROCM_METADATA_PREFER_OLDER</span></code>: This variable only affects assembly
kernels and only applies when ROCm supports both v2 and v3 COs. By default, the newer
format is used (v3 CO). When this variable is enabled, the behavior is reversed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_OPENCL_ENFORCE_CODE_OBJECT_VERSION</span></code>: Enforces the CO format for OpenCL
kernels. This only works with the HIP backend, when <code class="docutils literal notranslate"><span class="pre">cmake</span> <span class="pre">...</span> <span class="pre">-DMIOPEN_BACKEND=HIP...</span></code> is used.</p>
<ul>
<li><p>Unset - Automatically detects the required CO version. This is the default.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">2</span></code>: Always build to v2 CO.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">3</span></code>: Always build to v3 CO.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">4</span></code>: Always build to v4 CO.</p></li>
</ul>
</li>
</ul>
</section>
<section id="winograd-multi-pass-maximum-workspace-throttling">
<h3>Winograd multi-pass maximum workspace throttling<a class="headerlink" href="#winograd-multi-pass-maximum-workspace-throttling" title="Link to this heading">#</a></h3>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_WINOGRAD_MPASS_WORKSPACE_MAX</span></code>:
<code class="docutils literal notranslate"><span class="pre">ConvWinograd3x3MultipassWrW</span></code>, WrW</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_AMD_MP_BD_WINOGRAD_WORKSPACE_MAX</span></code>: <code class="docutils literal notranslate"><span class="pre">ConvMPBidirectWinograd*</span></code>,
FWD BWD</p></li>
</ul>
<p>Syntax of value:</p>
<ul class="simple">
<li><p>A decimal or hex (with <code class="docutils literal notranslate"><span class="pre">0x</span></code> prefix) value that must fit into a 64-bit unsigned integer</p></li>
<li><p>If the syntax is invalid, then the behavior is unspecified</p></li>
</ul>
<p>Usage notes:</p>
<ul class="simple">
<li><p>Sets the limit (max allowed workspace size) in bytes for multi-pass (MP) Winograd solutions.</p></li>
<li><p>The value affects all MP Winograd solutions. If a solution needs more workspace than the limit, it doesn’t apply.</p></li>
<li><p>If the value is not set, then the default limit is used. The current default is <code class="docutils literal notranslate"><span class="pre">2000000000</span></code> (~1.862 GiB) for the gfx900
and gfx906/60 (or fewer CUs). No default limit is defined for other GPUs.</p></li>
<li><p>Special values:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">0</span></code>: Use the default limit, as if the variable is unset</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">1</span></code>: Completely prohibit the use of workspace</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">-1</span></code>: Remove the default limit</p></li>
</ul>
</li>
</ul>
</section>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="use-fusion-api.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Using the fusion API</p>
      </div>
    </a>
    <a class="right-next"
       href="find-and-immediate.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Using the find APIs and immediate mode</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#layer-filtering">Layer filtering</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#filtering-by-algorithm">Filtering by algorithm</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#filtering-by-build-method">Filtering by build method</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#filtering-out-all-but-one-solution">Filtering out all but one solution</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#filtering-the-solutions-on-an-individual-basis">Filtering the solutions on an individual basis</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#gemm-logging-and-behavior">GEMM logging and behavior</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#numerical-checking">Numerical checking</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#check-for-gpu-sub-buffer-out-of-bounds-memory-accesses">Check for GPU sub-buffer out-of-bounds memory accesses</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#controlling-parallel-compilation">Controlling parallel compilation</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#experimental-controls">Experimental controls</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#code-object-version-selection-experimental">Code Object version selection (experimental)</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#winograd-multi-pass-maximum-workspace-throttling">Winograd multi-pass maximum workspace throttling</a></li>
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
