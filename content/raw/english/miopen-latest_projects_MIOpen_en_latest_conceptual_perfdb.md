---
title: "Using the performance database &#8212; MIOpen 3.5.1 Documentation"
source_url: "https://rocm.docs.amd.com/projects/MIOpen/en/latest/conceptual/perfdb.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:09:05.512897+00:00
content_hash: "0beea84c18335bb7"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="Using the MIOpen performance database" name="description" />
<meta content="MIOpen, ROCm, API, documentation, performance database" name="keywords" />

    <title>Using the performance database &#8212; MIOpen 3.5.1 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'conceptual/perfdb';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />
    <link rel="next" title="Tuning performance databases" href="tuningdb.html" />
    <link rel="prev" title="Kernel cache" href="cache.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-miopen" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/conceptual/perfdb.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<ul class="current nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="finddb.html">Find database</a></li>
<li class="toctree-l1"><a class="reference internal" href="cache.html">Kernel cache</a></li>
<li class="toctree-l1 current active"><a class="current reference internal" href="#">Performance database</a></li>
<li class="toctree-l1"><a class="reference internal" href="tuningdb.html">Manual tuning</a></li>
<li class="toctree-l1"><a class="reference internal" href="MI200-alt-implementation.html">MI200 alternate implementation</a></li>
<li class="toctree-l1"><a class="reference internal" href="porting-guide.html">Porting to MIOpen</a></li>
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
    <li class="breadcrumb-item active" aria-current="page"><span class="ellipsis">Using the performance database</span></li>
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
    <h1>Using the performance database</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#auto-tuning-kernels">Auto-tuning kernels</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#using-miopen-find-enforce-or-miopensettuningpolicy-to-control-auto-tuning">Using MIOPEN_FIND_ENFORCE or miopenSetTuningPolicy() to control auto-tuning</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#updating-miopen-and-user-perfdb">Updating MIOpen and User PerfDb</a></li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="using-the-performance-database">
<h1>Using the performance database<a class="headerlink" href="#using-the-performance-database" title="Link to this heading">#</a></h1>
<p>Many MIOpen kernels have parameters that affect their performance. Setting these parameters to
optimal values allows for the best possible throughput. The optimal values depend on many factors,
including the network configuration, GPU type, clock frequencies, and ROCm version.</p>
<p>Due to the large number of possible configurations and settings, MIOpen provides a set of pre-tuned
values for the “most applicable” network configurations and a method for expanding the set of
optimized values. MIOpen’s performance database (PerfDb) contains these pre-tuned parameter values
in addition to any user-optimized parameters.</p>
<p>The PerfDb consists of two parts:</p>
<ul class="simple">
<li><p><strong>System PerfDb</strong>: A system-wide storage that holds pre-run values for the most applicable
configurations.</p></li>
<li><p><strong>User PerfDb</strong>: A per-user storage that holds optimized values for arbitrary configurations.</p></li>
</ul>
<p>The User PerfDb <em>always takes precedence</em> over System PerfDb.</p>
<p>MIOpen also has auto-tuning functionality, which is able to find optimized kernel parameter values for
a specific configuration. The auto-tune process might take a long time, but after the optimized values are
found, they’re stored in the User PerfDb. MIOpen then automatically reads and uses these parameter
values.</p>
<p>By default, System PerfDb resides within the MIOpen install location, while User PerfDb resides in your
home directory. For more information, see <a class="reference internal" href="../install/build-source.html#setting-up-locations"><span class="std std-ref">setting up locations</span></a>.</p>
<p>The System PerfDb is not modified during the MIOpen installation.</p>
<section id="auto-tuning-kernels">
<h2>Auto-tuning kernels<a class="headerlink" href="#auto-tuning-kernels" title="Link to this heading">#</a></h2>
<p>MIOpen performs auto-tuning during the these API calls:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">miopenFindConvolutionForwardAlgorithm()</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">miopenFindConvolutionBackwardDataAlgorithm()</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">miopenFindConvolutionBackwardWeightsAlgorithm()</span></code></p></li>
</ul>
<p>Auto-tuning is performed for only one “problem configuration”, which is implicitly defined by the
tensor descriptors that are passed to the API function.</p>
<p>In order for auto-tuning to begin, the following conditions must be met:</p>
<ul class="simple">
<li><p>The applicable kernels must have tuning parameters</p></li>
<li><p>The value of the <code class="docutils literal notranslate"><span class="pre">exhaustiveSearch</span></code> parameter is set to <code class="docutils literal notranslate"><span class="pre">true</span></code></p></li>
<li><p>Neither the System nor User PerfDb can contain values for the relevant “problem configuration”.</p></li>
</ul>
<p>You can override the latter two conditions and force the search using either the API call
<code class="docutils literal notranslate"><span class="pre">miopenSetTuningPolicy()</span></code> or the <code class="docutils literal notranslate"><span class="pre">-MIOPEN_FIND_ENFORCE</span></code> environment variable. In addition to
controlling the auto-tuning behaviour of convolutions, both <code class="docutils literal notranslate"><span class="pre">miopenSetTuningPolicy()</span></code> and
<code class="docutils literal notranslate"><span class="pre">-MIOPEN_FIND_ENFORCE</span></code> can be used to control the tuning for batch normalization.
See the following section for more details.</p>
<p>To optimize performance, MIOpen provides several find modes to accelerate find API calls.
These modes include:</p>
<ul class="simple">
<li><p>normal find</p></li>
<li><p>fast find</p></li>
<li><p>hybrid find</p></li>
<li><p>dynamic hybrid find</p></li>
</ul>
<p>For more information about the MIOpen find modes, see <a class="reference internal" href="../how-to/find-and-immediate.html#find-modes"><span class="std std-ref">Find modes</span></a>.</p>
<section id="using-miopen-find-enforce-or-miopensettuningpolicy-to-control-auto-tuning">
<h3>Using MIOPEN_FIND_ENFORCE or miopenSetTuningPolicy() to control auto-tuning<a class="headerlink" href="#using-miopen-find-enforce-or-miopensettuningpolicy-to-control-auto-tuning" title="Link to this heading">#</a></h3>
<p><code class="docutils literal notranslate"><span class="pre">MIOPEN_FIND_ENFORCE</span></code> supports case-insensitive symbolic and numeric values. The possible values
are:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">NONE</span></code>/<code class="docutils literal notranslate"><span class="pre">(1)</span></code>: No change in the default behavior.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">DB_UPDATE</span></code>/<code class="docutils literal notranslate"><span class="pre">(2)</span></code>: Do not skip auto-tune (even if PerfDb already contains optimized values). If you
request auto-tune via API, MIOpen performs it and updates PerfDb. You can use this mode for
fine-tuning the MIOpen installation on your system. However, this mode slows down the processes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">SEARCH</span></code>/<code class="docutils literal notranslate"><span class="pre">(3)</span></code>: Perform auto-tune even if not requested via API. In this case, the library behaves as
if the <code class="docutils literal notranslate"><span class="pre">exhaustiveSearch</span></code> parameter is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>. If PerfDb already contains optimized values,
auto-tune is not performed. You can use this mode to tune applications that don’t anticipate any means
of getting the best performance from MIOpen. When in this mode, your application’s first run might
take substantially longer than expected.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">SEARCH_DB_UPDATE</span></code>/<code class="docutils literal notranslate"><span class="pre">(4)</span></code>: A combination of <code class="docutils literal notranslate"><span class="pre">DB_UPDATE</span></code> and <code class="docutils literal notranslate"><span class="pre">SEARCH</span></code>. MIOpen performs
auto-tune and updates User PerfDb on each <code class="docutils literal notranslate"><span class="pre">miopenFindConvolution*()</span></code> call. This mode is
only recommended for debugging purposes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">DB_CLEAN</span></code>/<code class="docutils literal notranslate"><span class="pre">(5)</span></code>: Removes optimized values related to the “problem configuration” from User
PerfDb. Auto-tune is blocked, even if explicitly requested. System PerfDb is left intact.</p>
<div class="admonition caution">
<p class="admonition-title">Caution</p>
<p>Use the <code class="docutils literal notranslate"><span class="pre">DB_CLEAN</span></code> option with care.</p>
</div>
</li>
</ul>
<p>Note that the API call miopenSetTuningPolicy() can be used to set the same modes as
<code class="docutils literal notranslate"><span class="pre">MIOPEN_FIND_ENFORCE</span></code>.  For example, to set the <code class="docutils literal notranslate"><span class="pre">SEARCH</span></code> mode, code like the following could be used:
.. code-block:: c</p>
<blockquote>
<div><p>miopenSetTuningPolicy(handle, miopenTuningPolicySearch);
miopenBatchNorm*()
miopenSetTuningPolicy(handle, miopenTuningPolicyNone);</p>
</div></blockquote>
<p>Note that this API method is supported for both convolutions and batchnorms, although batchnorm does
not support a policy of <code class="docutils literal notranslate"><span class="pre">DB_UPDATE</span></code> (this will be a no-op and the user should specify <code class="docutils literal notranslate"><span class="pre">SEARCH_DB_UPDATE</span></code>
instead if they want <code class="docutils literal notranslate"><span class="pre">DB_UPDATE</span></code> behavior).</p>
<p>If both the API method and environment variable are used, then the API method takes precedence.</p>
</section>
</section>
<section id="updating-miopen-and-user-perfdb">
<h2>Updating MIOpen and User PerfDb<a class="headerlink" href="#updating-miopen-and-user-perfdb" title="Link to this heading">#</a></h2>
<p>If you install a new version of MIOpen, it is recommended that you move or delete your old User
PerfDb file. This prevents older database entries from affecting configurations within the newer system
database. The User PerfDb is named <code class="docutils literal notranslate"><span class="pre">miopen.udb</span></code> and can be found at the User PerfDb path location.</p>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="cache.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Kernel cache</p>
      </div>
    </a>
    <a class="right-next"
       href="tuningdb.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Tuning performance databases</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#auto-tuning-kernels">Auto-tuning kernels</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#using-miopen-find-enforce-or-miopensettuningpolicy-to-control-auto-tuning">Using MIOPEN_FIND_ENFORCE or miopenSetTuningPolicy() to control auto-tuning</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#updating-miopen-and-user-perfdb">Updating MIOpen and User PerfDb</a></li>
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
